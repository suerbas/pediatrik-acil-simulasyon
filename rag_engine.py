import os
import re
import json
import time
from pathlib import Path
from typing import List, Dict, Any, Tuple
import requests

import chromadb

# Windows OpenMP fix
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


class PalliativeRAGEngine:
    """Palyatif Bakım RAG Motoru: Markdown dokümanlarını indeksler ve soruları yanıtlar."""

    def __init__(self, db_path: str = "chroma_db", collection_name: str = "palyatif_rehberler"):
        self.db_path = db_path
        self.collection_name = collection_name
        self.client = chromadb.PersistentClient(path=self.db_path)
        self.collection = self.client.get_or_create_collection(self.collection_name)
        self.config_path = Path("rag_config.json")
        self.config = self.load_config()

    def load_config(self) -> dict:
        default_cfg = {
            "provider": "gemini",  # gemini, groq, ollama
            "gemini_api_key": "",
            "gemini_model": "gemini-3.6-flash",
            "groq_api_key": "",
            "groq_model": "llama-3.3-70b-versatile",
            "ollama_url": "http://localhost:11434",
            "ollama_model": "llama3.2"
        }
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    saved = json.load(f)
                    default_cfg.update(saved)
            except Exception:
                pass
        # Eğer eski model tanımlıysa otomatik 3.6'ya güncelle
        if default_cfg.get("gemini_model") in ("gemini-1.5-flash", "gemini-2.0-flash", "gemini-2.5-flash"):
            default_cfg["gemini_model"] = "gemini-3.6-flash"
        return default_cfg

    def save_config(self, new_cfg: dict):
        self.config.update(new_cfg)
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def get_indexed_stats(self) -> Dict[str, Any]:
        count = self.collection.count()
        # İndekslenmiş benzersiz dosya adlarını bul
        sources = set()
        if count > 0:
            # Metadataları al
            sample = self.collection.get(include=["metadatas"])
            for m in sample.get("metadatas", []):
                if m and "source" in m:
                    sources.add(m["source"])
        return {
            "total_chunks": count,
            "sources": sorted(list(sources))
        }

    def index_markdown_files(self, md_folder: str = "md_cikti") -> Tuple[int, int]:
        """md_cikti klasöründeki tüm .md dosyalarını okur ve ChromaDB'ye ekler."""
        p = Path(md_folder)
        if not p.exists():
            return 0, 0

        md_files = list(p.glob("*.md"))
        total_chunks_added = 0

        for md_file in md_files:
            try:
                content = md_file.read_text(encoding="utf-8")
            except Exception:
                continue

            # Markdown başlıklarına göre böl (#, ##, ###)
            raw_sections = re.split(r'(?=\n#{1,3}\s+)', content)

            docs = []
            metadatas = []
            ids = []

            for idx, sec in enumerate(raw_sections):
                sec = sec.strip()
                if len(sec) < 40:
                    continue

                lines = sec.split('\n')
                header_line = lines[0].strip() if lines else md_file.stem
                # Eğer ilk satır başlık değilse (örn dosya başı metadata)
                if not header_line.startswith("#"):
                    header_line = f"# {md_file.stem} (Giriş)"

                # Parça çok uzunsa alt parçalara böl (max 1800 karakter)
                max_chars = 1800
                if len(sec) <= max_chars:
                    chunks = [sec]
                else:
                    # Paragraf bazlı böl
                    paragraphs = sec.split("\n\n")
                    chunks = []
                    cur_chunk = header_line + "\n\n"
                    for para in paragraphs:
                        if len(cur_chunk) + len(para) < max_chars:
                            cur_chunk += para + "\n\n"
                        else:
                            chunks.append(cur_chunk.strip())
                            cur_chunk = header_line + "\n\n" + para + "\n\n"
                    if cur_chunk.strip():
                        chunks.append(cur_chunk.strip())

                for c_idx, chunk in enumerate(chunks):
                    chunk_id = f"{md_file.stem}_{idx}_{c_idx}"
                    docs.append(chunk)
                    metadatas.append({
                        "source": md_file.name,
                        "header": header_line[:120],
                        "length": len(chunk)
                    })
                    ids.append(chunk_id)

            if docs:
                # 50'şerli paketlerle Chroma'ya kaydet
                for i in range(0, len(docs), 50):
                    self.collection.upsert(
                        documents=docs[i:i+50],
                        metadatas=metadatas[i:i+50],
                        ids=ids[i:i+50]
                    )
                total_chunks_added += len(docs)

        return len(md_files), total_chunks_added

    def retrieve(self, query: str, top_k: int = 10, candidate_k: int = 35) -> List[Dict[str, Any]]:
        """Hibrit Arama: Vektör benzerliği + Anahtar kelime eşleşmesini birleştirerek en alakalı bölümleri çeker."""
        if self.collection.count() == 0:
            return []

        # 1. Geniş aday havuzu çek (35 aday)
        results = self.collection.query(query_texts=[query], n_results=min(candidate_k, self.collection.count()))
        if not results or not results.get("documents") or not results["documents"][0]:
            return []

        docs = results["documents"][0]
        metas = results["metadatas"][0]
        dists = results["distances"][0] if "distances" in results and results["distances"] else [0.5] * len(docs)

        # 2. Sorgudaki anlamlı anahtar kelimeleri ayıkla
        stopwords = {
            "palyatif", "bakım", "bakımı", "bakımında", "hastasında", "hastada", "hangi", 
            "nelerdir", "nedir", "nasıl", "ve", "ile", "için", "bir", "bu", "da", "de", 
            "mi", "mu", "mı", "olarak", "olan", "önerilmektedir", "önerilir"
        }
        words = [w.lower() for w in re.findall(r'\w+', query) if len(w) > 2 and w.lower() not in stopwords]

        # 3. Hibrit puanlama: Vektör benzerliği + Kelime eşleşmesi (özellikle başlıkta geçiyorsa ekstra ağırlık)
        scored = []
        for doc, meta, dist in zip(docs, metas, dists):
            doc_lower = doc.lower()
            hdr_lower = meta.get("header", "").lower()
            kw_hits = sum(doc_lower.count(w) for w in words)
            hdr_hits = sum(hdr_lower.count(w) for w in words)

            score = (1.0 - dist) + (kw_hits * 0.15) + (hdr_hits * 0.35)
            scored.append((score, doc, meta, dist))

        scored.sort(key=lambda x: x[0], reverse=True)

        retrieved_items = []
        for score, doc, meta, dist in scored[:top_k]:
            retrieved_items.append({
                "content": doc,
                "source": meta.get("source", "Bilinmeyen"),
                "header": meta.get("header", "Başlık yok"),
                "distance": dist,
                "hybrid_score": score
            })
        return retrieved_items

    def ask(self, query: str, top_k: int = 8) -> Dict[str, Any]:
        """Soru sorar, bağlamı çeker ve seçili AI modelinden yanıt alır."""
        contexts = self.retrieve(query, top_k=top_k)

        if not contexts:
            return {
                "answer": "⚠️ Veritabanında henüz indekslenmiş doküman bulunamadı. Lütfen önce 'Dokümanları İndeksle' butonuna tıklayın.",
                "sources": []
            }

        # Bağlam metnini oluştur
        context_str = ""
        for i, c in enumerate(contexts, 1):
            context_str += f"\n--- [KAYNAK {i}: {c['source']} | {c['header']}] ---\n{c['content']}\n"

        system_prompt = (
            "Sen T.C. Aile Hekimliği standartlarına ve kanıta dayalı tıp kılavuzlarına hakim bir "
            "'Palyatif Bakım Klinik Karar Destek Asistanı'sın.\n\n"
            "GÖREVİN:\n"
            "Aşağıdaki [KLİNİK KAYNAK DOKÜMANLARI] dikkatlice analiz ederek hekimin sorusuna profesyonel, "
            "doğrudan uygulanabilir, net ve güvenilir bir yanıt vermektir.\n\n"
            "KURALLAR:\n"
            "1. SADECE sağlanan kaynak metinlerdeki bilgiye ve tablolara dayan. Kaynakta açıkça yer almayan bir tedaviyi veya dozu uydurma.\n"
            "2. İlaç isimleri, uygulama yolları (Oral, IV, Transdermal vb.), dozlar, uygulama sıklıkları ve "
            "kritik kontrendikasyon/uyarıları şematik (madde madde) olarak ver.\n"
            "3. Varsa kılavuzdaki tablolardan (örneğin Tablo 5 vb.) ve basamak protokollerinden doğrudan yararlan.\n"
            "4. Yanıtının sonuna hangi rehberden ve başlıktan yararlandığını özetle.\n"
            "5. Dilin hekimlik ciddiyetine uygun, saygılı ve akıcı Türkçe olmalıdır."
        )

        user_content = f"[KLİNİK KAYNAK DOKÜMANLARI]:\n{context_str}\n\n[DOKTORUN SORUSU]:\n{query}"

        provider = self.config.get("provider", "gemini")
        try:
            if provider == "gemini":
                answer = self._call_gemini(system_prompt, user_content)
            elif provider == "groq":
                answer = self._call_groq(system_prompt, user_content)
            elif provider == "ollama":
                answer = self._call_ollama(system_prompt, user_content)
            else:
                answer = "Bilinmeyen AI sağlayıcısı."
        except Exception as e:
            answer = f"❌ AI Yanıt Üretirken Hata Oluştu: {str(e)}"

        return {
            "answer": answer,
            "sources": contexts
        }

    def _call_gemini(self, system_prompt: str, user_content: str) -> str:
        api_key = self.config.get("gemini_api_key", "").strip()
        if not api_key:
            return (
                "⚠️ Google Gemini API Anahtarı girilmemiş!\n\n"
                "Nasıl Alınır? (Tamamen Ücretsizdir):\n"
                "1. https://aistudio.google.com/app/apikey adresine gidin.\n"
                "2. 'Create API Key' butonuna basıp anahtarınızı kopyalayın.\n"
                "3. Uygulamanın üst panelindeki 'Gemini API Key' kutusuna yapıştırıp 'Kaydet'e tıklayın."
            )

        # Denenecek model öncelik sırası (404 hatasını önlemek için otomatik geçiş)
        preferred_model = self.config.get("gemini_model", "gemini-3.6-flash")
        candidate_models = [preferred_model, "gemini-3.6-flash", "gemini-flash-latest", "gemini-3.5-flash"]
        # Tekrar edenleri temizle
        models_to_try = []
        for m in candidate_models:
            if m not in models_to_try:
                models_to_try.append(m)

        last_err = ""
        for model in models_to_try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
            payload = {
                "system_instruction": {"parts": [{"text": system_prompt}]},
                "contents": [{"parts": [{"text": user_content}]}],
                "generationConfig": {
                    "temperature": 0.2,
                    "maxOutputTokens": 4096
                }
            }

            resp = requests.post(url, json=payload, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                try:
                    # Başarılı olan modeli kaydet
                    if self.config.get("gemini_model") != model:
                        self.save_config({"gemini_model": model})
                    return data["candidates"][0]["content"]["parts"][0]["text"]
                except (KeyError, IndexError):
                    return "Gemini geçerli bir yanıt döndürmedi."
            else:
                last_err = f"Gemini API Hatası ({resp.status_code}): {resp.text}"

        return last_err

    def _call_groq(self, system_prompt: str, user_content: str) -> str:
        api_key = self.config.get("groq_api_key", "").strip()
        if not api_key:
            return "⚠️ Groq API Anahtarı girilmemiş! Lütfen ayarlardan Groq API anahtarınızı girin."

        model = self.config.get("groq_model", "llama-3.3-70b-versatile")
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ],
            "temperature": 0.2
        }

        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        if resp.status_code != 200:
            return f"Groq API Hatası ({resp.status_code}): {resp.text}"

        return resp.json()["choices"][0]["message"]["content"]

    def _call_ollama(self, system_prompt: str, user_content: str) -> str:
        ollama_url = self.config.get("ollama_url", "http://localhost:11434").rstrip('/')
        model = self.config.get("ollama_model", "llama3.2")
        url = f"{ollama_url}/api/chat"

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ],
            "stream": False,
            "options": {"temperature": 0.2}
        }

        try:
            resp = requests.post(url, json=payload, timeout=90)
            if resp.status_code != 200:
                return f"Ollama Hatası ({resp.status_code}): {resp.text}"
            return resp.json()["message"]["content"]
        except requests.exceptions.ConnectionError:
            return "❌ Ollama çalışmıyor! Lütfen bilgisayarınızda Ollama uygulamasını başlatın veya model indirin (`ollama run llama3.2`)."
