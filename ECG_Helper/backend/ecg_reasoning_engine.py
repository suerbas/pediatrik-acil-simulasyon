"""Jwoo5/ecg-reasoning-benchmark metodolojisine dayalı 6 adımlı EKG klinik muhakeme motoru."""

import base64
import json
import os
import re
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

from clinical_guidelines import calculate_qtc, format_guidelines_for_prompt


CONFIG_PATH = Path(__file__).resolve().parent / "config.json"


def _extract_json_block(raw_text: str) -> Dict[str, Any]:
    """LLM çıktısından geçerli JSON nesnesini güvenli biçimde ayıklar."""
    text = raw_text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        raise


EXPECTED_STEP_KEYS = (
    "step1_calibration_quality",
    "step2_rate_rhythm",
    "step3_axis",
    "step4_intervals",
    "step5_morphology_st_t",
    "step6_clinical_synthesis",
)

FULL_IMAGE_LABEL = "GÖRSEL 1 — Tam 12 derivasyonlu EKG görüntüsü (kontrastı iyileştirilmiş)."

URGENT_COMPLAINT_KEYWORDS = ("göğüs", "ağrı", "senkop", "bayıl", "nefes", "çarpıntı")


def _lower_tr(text: Any) -> str:
    """Türkçe büyük harfleri (I/İ) doğru küçülterek anahtar kelime eşleşmesine hazırlar."""
    return str(text or "").replace("I", "ı").replace("İ", "i").lower()


def _validate_llm_payload(parsed: Any) -> Dict[str, Any]:
    """Model çıktısının beklenen 6 adımlı şemaya uyan bir JSON nesnesi olduğunu doğrular."""
    if not isinstance(parsed, dict):
        raise ValueError("Model çıktısı bir JSON nesnesi değil.")
    if not any(isinstance(parsed.get(key), dict) for key in EXPECTED_STEP_KEYS):
        raise ValueError("Model çıktısında beklenen 6 adımlı şema alanları bulunamadı.")
    return parsed


def _crop_label(index: int, crop: Dict[str, Any]) -> str:
    """Bölge kırpması için modele gönderilecek açıklayıcı etiketi üretir."""
    title = crop.get("title") or crop.get("id") or "Bölge"
    return (
        f"GÖRSEL {index} — Yakınlaştırılmış bölge kırpması (beklenen içerik: {title}). "
        "Kırpma standart 3x4 + ritim şeridi düzeni varsayılarak sabit oranlarla alınmıştır; "
        "derivasyon kimliğini kağıt üzerindeki yazılı etiketlerden doğrula."
    )


def _data_uri_to_bytes(data_uri: str) -> Optional[bytes]:
    """Base64 data URI dizesini ham görüntü baytlarına çevirir."""
    if not data_uri or "," not in data_uri:
        return None
    _, b64_part = data_uri.split(",", 1)
    try:
        return base64.b64decode(b64_part)
    except Exception:
        return None


def summarize_caliper_and_qtc(
    caliper_measurements: Optional[Dict[str, Any]],
    patient_context: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Kullanıcının dijital pergel ile işaretlediği ölçümleri çözümler ve mümkünse QTc hesaplar."""
    if not caliper_measurements:
        return {"has_measurements": False, "computed_qtc": None, "summary_lines": [], "raw": {}}

    lines: List[str] = []

    for key, val in caliper_measurements.items():
        if val is None or val == "":
            continue
        lines.append(f"- {key}: {val}")

    # Sayısal QT ve HR/RR değerlerini yakalamayı dene
    def _parse_num(raw: Any) -> Optional[float]:
        if isinstance(raw, (int, float)):
            return float(raw)
        if isinstance(raw, str):
            m = re.search(r"(\d+(?:\.\d+)?)", raw)
            if m:
                return float(m.group(1))
        return None

    qt_candidate = _parse_num(caliper_measurements.get("QT")) or _parse_num(caliper_measurements.get("qt_ms"))
    rr_candidate = _parse_num(caliper_measurements.get("R-R")) or _parse_num(caliper_measurements.get("rr_ms"))
    hr_candidate = _parse_num(caliper_measurements.get("HR")) or _parse_num(caliper_measurements.get("hr_bpm"))

    if rr_candidate and rr_candidate > 150 and not hr_candidate:
        hr_candidate = round(60000.0 / rr_candidate, 1)

    computed_qtc = None
    if qt_candidate and hr_candidate and qt_candidate > 0 and hr_candidate > 0:
        try:
            ctx = patient_context or {}
            computed_qtc = calculate_qtc(qt_candidate, hr_candidate, sex=ctx.get("sex"), age=ctx.get("age"))
            lines.append(
                f"- Uygulama Tarafından Hesaplanan QTc (Bazett): {computed_qtc['qtc_bazett_ms']} ms | "
                f"Fridericia: {computed_qtc['qtc_fridericia_ms']} ms | "
                f"Esas alınan: {computed_qtc['recommended_formula']} = {computed_qtc['reference_qtc_ms']} ms "
                f"-> {computed_qtc['interpretation']}"
            )
        except ValueError:
            computed_qtc = None

    return {
        "has_measurements": len(lines) > 0,
        "computed_qtc": computed_qtc,
        "summary_lines": lines,
        "raw": caliper_measurements,
    }


class ECGReasoningEngine:
    """Çok adımlı klinik muhakeme (Chain-of-Thought) ile EKG görsellerini analiz eden motor."""

    DEFAULT_CONFIG: Dict[str, Any] = {
        "provider": "openrouter",
        "openrouter_api_key": "",
        "openrouter_model": "google/gemini-3.8-flash",
        "openrouter_base_url": "https://openrouter.ai/api/v1",
        "gemini_api_key": "",
        "gemini_model": "gemini-2.0-flash",
        "openai_api_key": "",
        "openai_model": "gpt-4o",
    }

    def __init__(self) -> None:
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Yapılandırmayı config.json ve ortam değişkenlerinden yükler."""
        cfg = dict(self.DEFAULT_CONFIG)
        if CONFIG_PATH.exists():
            try:
                saved = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
                cfg.update({k: v for k, v in saved.items() if v is not None})
            except Exception:
                pass

        if not cfg.get("openrouter_api_key") and os.environ.get("OPENROUTER_API_KEY"):
            cfg["openrouter_api_key"] = os.environ["OPENROUTER_API_KEY"]
        if not cfg.get("gemini_api_key") and os.environ.get("GEMINI_API_KEY"):
            cfg["gemini_api_key"] = os.environ["GEMINI_API_KEY"]
        if not cfg.get("openai_api_key") and os.environ.get("OPENAI_API_KEY"):
            cfg["openai_api_key"] = os.environ["OPENAI_API_KEY"]
        return cfg

    def save_config(self, updates: Dict[str, Any]) -> Dict[str, Any]:
        """Yeni ayarları kaydeder; boş bırakılan gizli anahtar alanlarını mevcut değerle korur."""
        current = self.load_config()
        for key in ("provider", "openrouter_model", "openrouter_base_url", "gemini_model", "openai_model"):
            if key in updates and updates[key]:
                current[key] = str(updates[key]).strip()
        for secret_key in ("openrouter_api_key", "gemini_api_key", "openai_api_key"):
            if secret_key in updates and updates[secret_key] is not None:
                val = str(updates[secret_key]).strip()
                if val and not val.startswith("••••"):
                    current[secret_key] = val
                elif val == "":
                    current[secret_key] = ""

        CONFIG_PATH.write_text(json.dumps(current, ensure_ascii=False, indent=2), encoding="utf-8")
        self.config = current
        return current

    def get_public_status(self) -> Dict[str, Any]:
        """Frontend'e güvenli yapılandırma özeti (anahtarları maskeleyerek) döndürür."""
        cfg = self.load_config()
        provider = cfg.get("provider", "openrouter")
        has_openrouter = bool(cfg.get("openrouter_api_key"))
        has_gemini = bool(cfg.get("gemini_api_key"))
        has_openai = bool(cfg.get("openai_api_key"))
        key_map = {
            "openrouter": has_openrouter,
            "gemini": has_gemini,
            "openai": has_openai,
        }
        active_key_configured = key_map.get(provider, False)
        return {
            "provider": provider,
            "openrouter_model": cfg.get("openrouter_model", "google/gemini-3.8-flash"),
            "openrouter_base_url": cfg.get("openrouter_base_url", "https://openrouter.ai/api/v1"),
            "gemini_model": cfg.get("gemini_model", "gemini-2.0-flash"),
            "openai_model": cfg.get("openai_model", "gpt-4o"),
            "has_openrouter_key": has_openrouter,
            "has_gemini_key": has_gemini,
            "has_openai_key": has_openai,
            "active_key_configured": active_key_configured,
            "mode": "live_llm" if active_key_configured else "demo_simulation",
        }

    def build_clinical_prompt(
        self,
        patient_context: Dict[str, Any],
        caliper_measurements: Optional[Dict[str, Any]] = None,
    ) -> str:
        """Jwoo5/ecg-reasoning-benchmark sistematiğine göre 6 adımlı klinik prompt üretir."""
        caliper_info = summarize_caliper_and_qtc(caliper_measurements, patient_context)

        # Arayüz boş alanları "" olarak gönderdiği için get() varsayılanı yerine `or` kullanılır
        age = patient_context.get("age") or "Belirtilmedi"
        sex = patient_context.get("sex") or "Belirtilmedi"
        complaint = patient_context.get("chief_complaint") or "Belirtilmedi"
        history = patient_context.get("history") or "Belirtilmedi"
        notes = patient_context.get("notes") or ""

        caliper_block = (
            "\n".join(caliper_info["summary_lines"])
            if caliper_info["has_measurements"]
            else "Kullanıcı dijital pergel ölçümü girmedi; görseldeki kalibrasyon ve karelerden tahmin yapın."
        )

        guidelines_block = format_guidelines_for_prompt()

        return f"""Sen kıdemli bir kardiyoloji uzmanısın. Sana verilen tam 12 derivasyonlu EKG görüntüsünü ve yakınlaştırılmış bölgesel derivasyon kırpmalarını (I-III, aVR-aVF, V1-V3, V4-V6 ve Ritim Şeridi) inceleyerek adım adım klinik akıl yürütme (ECG-Reasoning-Benchmark protokolü) yapacaksın.

ÖNEMLİ KURALLAR:
1. Görüntüde gerçekten görmediğin hiçbir dalga değişikliğini varsayma (görsel doğrulama zorunludur).
2. Eğer kullanıcı dijital pergel (caliper) ölçümleri sağladıysa, aralık ve hız hesaplarında bu ölçümleri kesin referans olarak kullan. "Uygulama Tarafından Hesaplanan QTc" satırı varsa QTc'yi yeniden hesaplama; verilen değeri ve yorumu aynen kullan.
3. Doğrudan tanıya atlama; aşağıdaki 6 adımı ve erb_reasoning_chain alanını sırasıyla doldur ve SADECE geçerli bir JSON objesi döndür.
4. Dil tamamen Türkçe, tıbbi terminoloji ise uluslararası kardiyoloji standardında olmalıdır.
5. Bölge kırpmaları standart 3x4 + ritim şeridi düzeni varsayılarak sabit oranlarla alınmıştır. Kağıt düzeni farklıysa kırpma etiketlerine güvenme; derivasyonları görseldeki yazılı etiketlerden tanı ve emin olamadığın derivasyonu belirt.
6. Görüntü kalitesi bir bulguyu değerlendirmeye yetmiyorsa tahmin yürütme; ilgili alana "Değerlendirilemedi" yaz ve duvar durumunu "UNASSESSED" olarak işaretle.

=== HASTA KLİNİK BİLGİLERİ ===
- Yaş / Cinsiyet: {age} / {sex}
- Başvuru Şikayeti: {complaint}
- Özgeçmiş / Risk Faktörleri: {history}
- Ek Klinik Notlar: {notes or "Yok"}

=== DİJİTAL PERGEL (CALIPER) ÖLÇÜMLERİ ===
{caliper_block}

{guidelines_block}

=== İSTENEN ÇIKTI JSON ŞEMASI ===
{{
  "step1_calibration_quality": {{
    "status": "ADEQUATE" | "SUBOPTIMAL",
    "paper_speed_and_gain": "Örn: 25 mm/s ve 10 mm/mV kalibrasyon doğrulandı (veya kağıtta görünmüyor)",
    "image_quality_notes": "Görüntü netliği, bazal hat kayması veya artefakt değerlendirmesi",
    "findings": ["Gözlem 1", "Gözlem 2"]
  }},
  "step2_rate_rhythm": {{
    "heart_rate_bpm": 75,
    "rhythm_regularity": "Düzenli" | "Düzensiz-düzensiz" | "Düzenli düzensiz",
    "p_wave_assessment": "P dalgası varlığı, morfolojisi ve ekseni (I, II pozitif; aVR negatif vb.)",
    "av_relationship": "Her P'yi QRS takip ediyor mu, AV iletim ilişkisi nedir?",
    "summary": "Adım 2 klinik özeti"
  }},
  "step3_axis": {{
    "axis_classification": "Normal Eksen" | "Sol Aks Deviasyonu" | "Sağ Aks Deviasyonu" | "Aşırı Sağ Aks",
    "lead_i_polarity": "Pozitif / Bifazik / Negatif",
    "lead_avf_polarity": "Pozitif / Bifazik / Negatif",
    "summary": "Adım 3 eksen açıklaması"
  }},
  "step4_intervals": {{
    "pr_interval_ms": "Ölçülen değer ve yorumu (Normal 120-200 ms)",
    "qrs_duration_ms": "Ölçülen değer ve dar/geniş yorumu (<120 ms)",
    "qt_qtc_ms": "QT / QTc değerlendirmesi",
    "caliper_used": {str(caliper_info["has_measurements"]).lower()},
    "summary": "Adım 4 aralık analizi özeti"
  }},
  "step5_morphology_st_t": {{
    "territories": [
      {{
        "wall": "Inferior (II, III, aVF)",
        "st_segment": "İzoelektrik / ST elevasyonu / ST depresyonu detayı",
        "t_wave": "Pozitif / Negatif / Hiperakut / Bifazik",
        "q_wave": "Patolojik Q var/yok",
        "status": "NORMAL" | "ABNORMAL" | "RECIPROCAL" | "UNASSESSED"
      }},
      {{
        "wall": "Septal & Anterior (V1-V4)",
        "st_segment": "...",
        "t_wave": "...",
        "q_wave": "...",
        "status": "NORMAL" | "ABNORMAL" | "RECIPROCAL" | "UNASSESSED"
      }},
      {{
        "wall": "Lateral (I, aVL, V5, V6)",
        "st_segment": "...",
        "t_wave": "...",
        "q_wave": "...",
        "status": "NORMAL" | "ABNORMAL" | "RECIPROCAL" | "UNASSESSED"
      }},
      {{
        "wall": "aVR",
        "st_segment": "...",
        "t_wave": "...",
        "q_wave": "...",
        "status": "NORMAL" | "ABNORMAL" | "RECIPROCAL" | "UNASSESSED"
      }}
    ],
    "summary": "Morfoloji ve anatomik duvar tutulum özeti"
  }},
  "step6_clinical_synthesis": {{
    "primary_diagnosis": "En olası ana EKG tanısı",
    "urgency": "CRITICAL" | "URGENT" | "ROUTINE",
    "confidence_score": 85,
    "differential_diagnoses": [
      {{"diagnosis": "Ayırıcı tanı 1", "likelihood": "Orta/Düşük", "rationale": "Klinik/EKG gerekçesi"}}
    ],
    "red_flags": ["Acil dikkat gerektiren bulgular (yoksa boş liste)"],
    "guideline_matches": ["Eşleşen ESC/AHA kılavuz kriteri"],
    "recommended_actions": ["Somut sonraki klinik/tanısal adımlar"]
  }},
  "erb_reasoning_chain": {{
    "target_dx": "17 benchmark tanısından en uygunu (örn. inferior_myocardial_infarction, first_degree_av_block, complete_left_bundle_branch_block); hiçbiri uymuyorsa normal_sinus_rhythm, atrial_fibrillation veya other",
    "steps": [
      {{
        "criterion_selection": "Seçilen ve değerlendirilen klinik kriter (ECG-Reasoning-Benchmark ağacına uygun)",
        "finding_identification": "Kriterin görselde karşılanıp karşılanmadığı (Evet/Hayır ve gerekçe)",
        "ecg_grounding": {{
          "lead_grounding": ["Bulguların görüldüğü derivasyonlar (örn. Lead II, Lead III, Lead aVF)"],
          "wave_grounding": "Hangi dalga/segmentte görüldüğü (örn. J-noktası ve ST segmenti)",
          "measurement_grounding": "Ölçülen değer/aralık (örn. 2.6 - 3.2 mm veya 160 ms)"
        }},
        "diagnostic_decision": "Doğrulandı" | "Ek bulgu gerekli" | "Dışlandı"
      }}
    ]
  }}
}}"""

    def _call_gemini(
        self,
        api_key: str,
        model_name: str,
        prompt: str,
        images: List[Tuple[str, bytes]],
    ) -> Dict[str, Any]:
        """Google GenAI SDK ile etiketli görselleri ve klinik promptu Gemini modeline gönderir."""
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=api_key)
        contents: List[Any] = [prompt]
        for label, img_bytes in images:
            contents.append(label)
            contents.append(types.Part.from_bytes(data=img_bytes, mime_type="image/png"))

        response = client.models.generate_content(
            model=model_name,
            contents=contents,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.15,
            ),
        )
        return _extract_json_block(response.text or "{}")

    def _call_openai_compatible(
        self,
        api_key: str,
        model_name: str,
        prompt: str,
        images: List[Tuple[str, bytes]],
        base_url: Optional[str] = None,
        extra_headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """OpenAI ve OpenRouter uyumlu Vision API ile görselleri ve klinik promptu analiz eder."""
        from openai import APIStatusError, OpenAI

        client_kwargs: Dict[str, Any] = {"api_key": api_key, "timeout": 120.0}
        if base_url:
            client_kwargs["base_url"] = base_url
        if extra_headers:
            client_kwargs["default_headers"] = extra_headers

        client = OpenAI(**client_kwargs)
        content_parts: List[Dict[str, Any]] = [{"type": "text", "text": prompt}]
        for label, img_bytes in images:
            b64 = base64.b64encode(img_bytes).decode("ascii")
            content_parts.append({"type": "text", "text": label})
            content_parts.append(
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{b64}", "detail": "high"},
                }
            )

        request_kwargs: Dict[str, Any] = {
            "model": model_name,
            "messages": [{"role": "user", "content": content_parts}],
        }
        try:
            completion = client.chat.completions.create(
                **request_kwargs,
                temperature=0.15,
                response_format={"type": "json_object"},
            )
        except APIStatusError as exc:
            # Yalnızca "parametre desteklenmiyor" türü hatalarda (400/422) yalın istekle yinele;
            # 401/402/429 gibi hatalarda aynı isteği tekrarlamak kota tüketmekten başka işe yaramaz.
            if exc.status_code not in (400, 422):
                raise
            completion = client.chat.completions.create(**request_kwargs)

        text = completion.choices[0].message.content or "{}"
        return _extract_json_block(text)

    def _call_openrouter(
        self,
        api_key: str,
        model_name: str,
        base_url: str,
        prompt: str,
        images: List[Tuple[str, bytes]],
    ) -> Dict[str, Any]:
        """OpenRouter API üzerinden seçili multimodal modeli çağırır."""
        return self._call_openai_compatible(
            api_key=api_key,
            model_name=model_name,
            prompt=prompt,
            images=images,
            base_url=base_url,
            extra_headers={"HTTP-Referer": "http://localhost:5173", "X-Title": "ECG_Helper"},
        )

    def _call_openai(
        self,
        api_key: str,
        model_name: str,
        prompt: str,
        images: List[Tuple[str, bytes]],
    ) -> Dict[str, Any]:
        """OpenAI Vision API ile görselleri ve klinik promptu analiz eder."""
        return self._call_openai_compatible(
            api_key=api_key,
            model_name=model_name,
            prompt=prompt,
            images=images,
        )

    def _generate_demo_response(
        self,
        patient_context: Dict[str, Any],
        caliper_info: Dict[str, Any],
        case_hint: Optional[str],
        quality: Optional[Dict[str, Any]],
        fallback_reason: Optional[str] = None,
    ) -> Dict[str, Any]:
        """API anahtarı olmadığında veya demo modunda eğitici 6 adımlı yapılandırılmış analiz üretir."""
        caliper_used = caliper_info["has_measurements"]
        caliper_note = (
            " | Dijital pergel ölçümleri: " + "; ".join(caliper_info["summary_lines"])
            if caliper_used
            else ""
        )
        q_status = "ADEQUATE" if not quality or quality.get("overall_status") != "POOR" else "SUBOPTIMAL"
        q_notes = (
            "Görüntü ön işleme uygulandı. "
            + (", ".join(quality.get("warnings", [])) if quality and quality.get("warnings") else "Çözünürlük ve kontrast analiz için uygun.")
        )

        complaint = _lower_tr(patient_context.get("chief_complaint"))
        inferred_case = case_hint

        if inferred_case == "inferior_stemi":
            result = {
                "step1_calibration_quality": {
                    "status": q_status,
                    "paper_speed_and_gain": "25 mm/s hız ve 10 mm/mV kalibrasyon dikdörtgeni doğrulandı.",
                    "image_quality_notes": q_notes,
                    "findings": [
                        "12 derivasyon + uzun DII ritim şeridi eksiksiz izleniyor.",
                        "Izgara çizgileri net, bazal hat artefaktı saptanmadı.",
                    ],
                },
                "step2_rate_rhythm": {
                    "heart_rate_bpm": 68,
                    "rhythm_regularity": "Düzenli",
                    "p_wave_assessment": "I, II, aVF'de pozitif, aVR'de negatif sinüs P dalgaları seçiliyor.",
                    "av_relationship": "1:1 AV iletim mevcut (PR sabit). İnferior MI seyrinde AV blok gelişimi açısından yakın takip gerekir.",
                    "summary": "68/dk hızında düzenli Sinüs Ritmi.",
                },
                "step3_axis": {
                    "axis_classification": "Normal Eksen",
                    "lead_i_polarity": "Pozitif (QRS ağırlıklı yukarı)",
                    "lead_avf_polarity": "Pozitif (QRS ağırlıklı yukarı)",
                    "summary": "I (+) ve aVF (+) olduğundan QRS ekseni normal aralıkta (~ +45° ile +60°).",
                },
                "step4_intervals": {
                    "pr_interval_ms": "160 ms (Normal, 120-200 ms arası)" + caliper_note,
                    "qrs_duration_ms": "90 ms (Dar QRS, < 120 ms)",
                    "qt_qtc_ms": (
                        f"Hesaplanan Bazett QTc: {caliper_info['computed_qtc']['qtc_bazett_ms']} ms"
                        if caliper_info["computed_qtc"]
                        else "QT ~370 ms, QTc ~395 ms (Normal sınırlarda)"
                    ),
                    "caliper_used": caliper_used,
                    "summary": "İletim süreleri normal sınırlarda; dal bloğu veya uzamış QT saptanmadı.",
                },
                "step5_morphology_st_t": {
                    "territories": [
                        {
                            "wall": "Inferior (II, III, aVF)",
                            "st_segment": "II, III ve aVF derivasyonlarında J noktasında 2.5 - 3.2 mm konveks (kubbeli) ST elevasyonu.",
                            "t_wave": "ST elevasyonu ile birleşen hiperakut/belirgin pozitif T dalgaları.",
                            "q_wave": "III ve aVF'de gelişmekte olan Q dalgaları.",
                            "status": "ABNORMAL",
                        },
                        {
                            "wall": "Septal & Anterior (V1-V4)",
                            "st_segment": "İzoelektrik hatta yakın.",
                            "t_wave": "Normal morfoloji.",
                            "q_wave": "Patolojik Q yok.",
                            "status": "NORMAL",
                        },
                        {
                            "wall": "Lateral (I, aVL, V5, V6)",
                            "st_segment": "I ve özellikle aVL'de 1.5 - 2.0 mm belirgin resiprokal ST depresyonu.",
                            "t_wave": "I ve aVL'de T dalgası negatifliği.",
                            "q_wave": "Yok.",
                            "status": "RECIPROCAL",
                        },
                        {
                            "wall": "aVR",
                            "st_segment": "İzoelektrik.",
                            "t_wave": "Negatif (beklenen polarite).",
                            "q_wave": "Yok.",
                            "status": "NORMAL",
                        },
                    ],
                    "summary": "İnferior duvarda (II, III, aVF) akut transmural iskemi ile uyumlu ST elevasyonu ve yüksek lateralde (I, aVL) klasik resiprokal ST depresyonu.",
                },
                "step6_clinical_synthesis": {
                    "primary_diagnosis": "Akut İnferior ST-Elevasyonlu Miyokard İnfarktüsü (İnferior STEMI)",
                    "urgency": "CRITICAL",
                    "confidence_score": 95,
                    "differential_diagnoses": [
                        {
                            "diagnosis": "Akut Perikardit",
                            "likelihood": "Düşük",
                            "rationale": "Resiprokal ST depresyonunun (I, aVL) varlığı ve bölgesel dağılım perikarditten uzaklaştırır.",
                        },
                        {
                            "diagnosis": "Erken Repolarizasyon",
                            "likelihood": "Çok Düşük",
                            "rationale": "Konveks ST morfolojisi, resiprokal değişiklik ve tipik göğüs ağrısı ile uyumsuzdur.",
                        },
                    ],
                    "red_flags": [
                        "ACİL REPERFÜZYON ENDİKASYONU: Primer PKG (PCI) veya trombolitik zaman penceresi aktive edilmeli.",
                        "Sağ Ventrikül İnfarktüsü ekartasyonu için mutlaka sağ derivasyonlar (özellikle V4R) çekilmeli (RV tutulumunda nitratlar kontrendikedir).",
                        "Posterior tutulum için V7-V9 çekilmesi ve bradiaritmi/AV blok açısından monitörizasyon önerilir.",
                    ],
                    "guideline_matches": [
                        "ESC/AHA Akut STEMI Kriteri: Komşu >= 2 inferior derivasyonda (II, III, aVF) >= 1 mm ST elevasyonu.",
                        "Anatomik Eşleşme: Muhtemel Sağ Koroner Arter (RCA) oklüzyonu (III > II elevasyon eğilimi ve I/aVL resiprokal depresyon).",
                    ],
                    "recommended_actions": [
                        "Acil Kardiyoloji / Kateter Laboratuvarı aktivasyonu (Kapı-balon süresi < 90 dk).",
                        "Sağ derivasyonlar (V4R) ve posterior derivasyonlar (V7-V9) ile 18 derivasyonlu EKG kaydı.",
                        "Kılavuzlara uygun antiagregan/antikoagülan yükleme (kontrendikasyon yoksa) ve sürekli ritim monitörizasyonu.",
                    ],
                },
                "erb_reasoning_chain": {
                    "target_dx": "inferior_myocardial_infarction",
                    "steps": [
                        {
                            "criterion_selection": "İnferior derivasyonlarda J-noktasında ST-segment elevasyonu varlığı (Presence of ST-segment elevation in inferior leads)",
                            "finding_identification": "Evet — II, III ve aVF derivasyonlarında komşu >= 2 derivasyonda > 1 mm (0.1 mV) ST elevasyonu ve I, aVL'de resiprokal depresyon mevcut.",
                            "ecg_grounding": {
                                "lead_grounding": ["Lead II", "Lead III", "Lead aVF"],
                                "wave_grounding": "QRS sonrası J-noktası ve ST segmenti",
                                "measurement_grounding": "2.6 - 3.2 mm ST elevasyonu",
                            },
                            "diagnostic_decision": "Doğrulandı",
                        }
                    ],
                },
            }
        elif inferred_case == "afib":
            result = {
                "step1_calibration_quality": {
                    "status": q_status,
                    "paper_speed_and_gain": "25 mm/s hız ve 10 mm/mV kalibrasyon doğrulandı.",
                    "image_quality_notes": q_notes,
                    "findings": [
                        "Uzun DII ritim şeridi ritim düzensizliğini doğrulamak için yeterli netlikte.",
                        "Bazal hatta hızlı fibrilasyon osilasyonları görülebiliyor.",
                    ],
                },
                "step2_rate_rhythm": {
                    "heart_rate_bpm": 132,
                    "rhythm_regularity": "Düzensiz-düzensiz (Irregularly irregular)",
                    "p_wave_assessment": "Organize sinüs P dalgası seçilmiyor; yerine bazal hatta düzensiz fibrilasyon (f) dalgaları mevcut.",
                    "av_relationship": "AV düğüm üzerinden değişken refrakterlik ile düzensiz ventriküler yanıt.",
                    "summary": "Ortalama ~132/dk ventrikül hızlı Atriyal Fibrilasyon (AF with RVR).",
                },
                "step3_axis": {
                    "axis_classification": "Normal Eksen",
                    "lead_i_polarity": "Pozitif",
                    "lead_avf_polarity": "Pozitif",
                    "summary": "QRS ekseni normal aralıkta.",
                },
                "step4_intervals": {
                    "pr_interval_ms": "Ölçülemez (P dalgası yok)",
                    "qrs_duration_ms": "88 ms (Dar QRS — supraventriküler iletim)" + caliper_note,
                    "qt_qtc_ms": (
                        f"Hesaplanan QTc (Fridericia): {caliper_info['computed_qtc']['qtc_fridericia_ms']} ms"
                        if caliper_info["computed_qtc"]
                        else "Düzensiz R-R nedeniyle ortalama QT değerlendirmesi gerekir (~415 ms)"
                    ),
                    "caliper_used": caliper_used,
                    "summary": "Dar QRS kompleksi supraventriküler kökeni doğrular; aberran iletim saptanmadı.",
                },
                "step5_morphology_st_t": {
                    "territories": [
                        {
                            "wall": "Inferior (II, III, aVF)",
                            "st_segment": "İzoelektrik (hıza sekonder hafif düzleşme).",
                            "t_wave": "Düşük amplitüdlü pozitif.",
                            "q_wave": "Patolojik Q yok.",
                            "status": "NORMAL",
                        },
                        {
                            "wall": "Septal & Anterior (V1-V4)",
                            "st_segment": "İzoelektrik.",
                            "t_wave": "Normal morfoloji.",
                            "q_wave": "Yok.",
                            "status": "NORMAL",
                        },
                        {
                            "wall": "Lateral (I, aVL, V5, V6)",
                            "st_segment": "Belirgin iskemik ST depresyonu yok.",
                            "t_wave": "Hafif düzleşmiş.",
                            "q_wave": "Yok.",
                            "status": "NORMAL",
                        },
                        {
                            "wall": "aVR",
                            "st_segment": "İzoelektrik.",
                            "t_wave": "Negatif.",
                            "q_wave": "Yok.",
                            "status": "NORMAL",
                        },
                    ],
                    "summary": "Akut ST elevasyonlu iskemi bulgusu yok; hızlı ventriküler yanıta bağlı hafif repolarizasyon düzleşmesi izleniyor.",
                },
                "step6_clinical_synthesis": {
                    "primary_diagnosis": "Hızlı Ventrikül Yanıtlı Atriyal Fibrilasyon (AFib with RVR)",
                    "urgency": "URGENT",
                    "confidence_score": 93,
                    "differential_diagnoses": [
                        {
                            "diagnosis": "Değişken Bloklu Atriyal Flutter",
                            "likelihood": "Düşük-Orta",
                            "rationale": "Tipik düzenli testere dişi F dalgaları izlenmediğinden AF ön plandadır.",
                        },
                        {
                            "diagnosis": "Multifokal Atriyal Taşikardi (MAT)",
                            "likelihood": "Düşük",
                            "rationale": "En az 3 farklı morfolojide belirgin P dalgası yerine kaotik f dalgaları mevcut.",
                        },
                    ],
                    "red_flags": [
                        "Hemodinamik instabilite (hipotansiyon, pulmoner ödem, akut göğüs ağrısı, bilinç değişikliği) varsa acil senkronize kardiyoversiyon düşünülmelidir.",
                        "Antikoagülan kullanmayan hastada başlangıç süresi (> 48 saat veya belirsiz) tromboembolik risk açısından kritiktir.",
                    ],
                    "guideline_matches": [
                        "ESC AF Kılavuzu: Düzensiz R-R aralıkları + belirgin P dalgası yokluğu = Atriyal Fibrilasyon.",
                        "CHA2DS2-VASc skoru hesaplanmalı (yaş, cinsiyet ve HT öyküsü nedeniyle yüksek inme riski olasılığı).",
                    ],
                    "recommended_actions": [
                        "Hemodinamik durumun ve vital bulguların değerlendirilmesi.",
                        "Altta yatan tetikleyicilerin taranması (tiroid fonksiyonları/TSH, elektrolitler, enfeksiyon, anemi).",
                        "Kontrendikasyon yoksa hız kontrolü (beta-bloker veya non-DHP kalsiyum kanal blokeri) ve CHA2DS2-VASc / HAS-BLED ile antikoagülasyon planlanması.",
                    ],
                },
                "erb_reasoning_chain": {
                    "target_dx": "atrial_fibrillation",
                    "steps": [
                        {
                            "criterion_selection": "R-R aralıklarının düzensizliği (Irregularly irregular RR intervals)",
                            "finding_identification": "Evet — Uzun DII ritim şeridinde ardışık R-R mesafeleri tamamen düzensiz (350-620 ms arası değişken).",
                            "ecg_grounding": {
                                "lead_grounding": ["Lead II (Ritim Şeridi)"],
                                "wave_grounding": "R-R aralıkları (QRS tepeleri arası)",
                                "measurement_grounding": "Ortalama ~132/dk (hızlı ventrikül yanıtlı)",
                            },
                            "diagnostic_decision": "Ek bulgu gerekli",
                        },
                        {
                            "criterion_selection": "Organize P dalgalarının yokluğu ve bazal f dalgaları",
                            "finding_identification": "Evet — QRS öncesi düzenli P dalgası izlenmiyor, bazal hatta kaotik fibrilasyon osilasyonları mevcut.",
                            "ecg_grounding": {
                                "lead_grounding": ["Lead II", "Lead V1"],
                                "wave_grounding": "İzoelektrik hat / PR bölgesi",
                                "measurement_grounding": "P dalgası yok",
                            },
                            "diagnostic_decision": "Doğrulandı",
                        },
                    ],
                },
            }
        elif inferred_case == "nsr":
            result = {
                "step1_calibration_quality": {
                    "status": q_status,
                    "paper_speed_and_gain": "25 mm/s hız ve 10 mm/mV kalibrasyon doğrulandı.",
                    "image_quality_notes": q_notes,
                    "findings": ["Tüm 12 derivasyon ve ritim şeridi temiz ve artefaktsız."],
                },
                "step2_rate_rhythm": {
                    "heart_rate_bpm": 75,
                    "rhythm_regularity": "Düzenli",
                    "p_wave_assessment": "I, II, aVF'de pozitif, aVR'de negatif; normal morfolojili sinüs P dalgaları.",
                    "av_relationship": "Sabit PR aralığı ile 1:1 AV iletim.",
                    "summary": "75/dk hızında Normal Sinüs Ritmi.",
                },
                "step3_axis": {
                    "axis_classification": "Normal Eksen",
                    "lead_i_polarity": "Pozitif",
                    "lead_avf_polarity": "Pozitif",
                    "summary": "Kardiyak eksen normal kadran (-30° ile +90° arası) içerisinde.",
                },
                "step4_intervals": {
                    "pr_interval_ms": "160 ms (Normal)" + caliper_note,
                    "qrs_duration_ms": "85 ms (Dar, normal)",
                    "qt_qtc_ms": (
                        f"Hesaplanan Bazett QTc: {caliper_info['computed_qtc']['qtc_bazett_ms']} ms"
                        if caliper_info["computed_qtc"]
                        else "QT ~370 ms, QTc ~415 ms (Normal)"
                    ),
                    "caliper_used": caliper_used,
                    "summary": "PR, QRS ve QTc süreleri normal fizyolojik sınırlarda.",
                },
                "step5_morphology_st_t": {
                    "territories": [
                        {
                            "wall": "Inferior (II, III, aVF)",
                            "st_segment": "İzoelektrik",
                            "t_wave": "Pozitif, normal",
                            "q_wave": "Patolojik Q yok",
                            "status": "NORMAL",
                        },
                        {
                            "wall": "Septal & Anterior (V1-V4)",
                            "st_segment": "İzoelektrik",
                            "t_wave": "Normal R dalgası progresyonu, T pozitif (V1 hariç)",
                            "q_wave": "Yok",
                            "status": "NORMAL",
                        },
                        {
                            "wall": "Lateral (I, aVL, V5, V6)",
                            "st_segment": "İzoelektrik",
                            "t_wave": "Pozitif, simetrik",
                            "q_wave": "Fizyolojik septal q",
                            "status": "NORMAL",
                        },
                        {
                            "wall": "aVR",
                            "st_segment": "İzoelektrik",
                            "t_wave": "Negatif (normal)",
                            "q_wave": "Yok",
                            "status": "NORMAL",
                        },
                    ],
                    "summary": "Akut iskemi, hipertrofi veya iletim bozukluğu bulgusu izlenmedi.",
                },
                "step6_clinical_synthesis": {
                    "primary_diagnosis": "Normal 12-Derivasyonlu EKG (Normal Sinüs Ritmi)",
                    "urgency": "ROUTINE",
                    "confidence_score": 96,
                    "differential_diagnoses": [],
                    "red_flags": [],
                    "guideline_matches": [
                        "Kalp hızı (60-100/dk), P dalga ekseni, PR (120-200 ms), QRS (<120 ms) ve ST-T normal referans aralığındadır."
                    ],
                    "recommended_actions": [
                        "Klinik bulgularla uyumlu ise ek acil EKG girişimi gerekmez.",
                        "Semptom gelişimi halinde seri EKG takibi her zaman önceliklidir.",
                    ],
                },
                "erb_reasoning_chain": {
                    "target_dx": "normal_sinus_rhythm",
                    "steps": [
                        {
                            "criterion_selection": "1:1 AV iletim ve sinüs P dalga ekseni (I, II pozitif; aVR negatif)",
                            "finding_identification": "Evet — Her P dalgasını sabit PR aralığı ile dar bir QRS kompleksi izliyor.",
                            "ecg_grounding": {
                                "lead_grounding": ["Lead I", "Lead II", "Lead aVR"],
                                "wave_grounding": "P dalgası ve PR segmenti",
                                "measurement_grounding": "PR ~160 ms, QRS ~85 ms, Hız 75/dk",
                            },
                            "diagnostic_decision": "Doğrulandı",
                        }
                    ],
                },
            }
        else:
            # Kullanıcının kendi yüklediği özel fotoğraf + API anahtarı yok durumu
            hr_from_caliper = None
            if caliper_info["computed_qtc"]:
                hr_from_caliper = round(caliper_info["computed_qtc"]["hr_bpm"], 0)
            result = {
                "step1_calibration_quality": {
                    "status": "SUBOPTIMAL" if q_status == "SUBOPTIMAL" else "UNASSESSED",
                    "paper_speed_and_gain": "Görsel üzerindeki kalibrasyon (genellikle 25 mm/s, 10 mm/mV) hekim tarafından doğrulanmalıdır.",
                    "image_quality_notes": q_notes,
                    "findings": [
                        "Görüntü OpenCV CLAHE ve yüksek kontrast dalga filtresi ile analiz için hazırlandı.",
                        "Sağ üstteki 'API Ayarları' bölümünden OpenRouter, Gemini veya OpenAI anahtarı girildiğinde canlı multimodal LLM görsel okuması aktifleşir.",
                    ],
                },
                "step2_rate_rhythm": {
                    "heart_rate_bpm": int(hr_from_caliper) if hr_from_caliper else None,
                    "rhythm_regularity": "Çevrimdışı Demo Modu — Canlı LLM bağlantısı gerektirir",
                    "p_wave_assessment": "DII ritim şeridi kırpmasından her QRS öncesi P dalgası varlığını kontrol ediniz.",
                    "av_relationship": "PR sabitliğini ardışık atımlarda dijital pergel ile doğrulayınız.",
                    "summary": "Özel fotoğraf yüklendi; canlı görsel ritim çıkarımı için API anahtarı yapılandırılmalıdır.",
                },
                "step3_axis": {
                    "axis_classification": "Görsel Kontrol Bekleniyor",
                    "lead_i_polarity": "Sol üst sütun (I) kırpmasından kontrol ediniz",
                    "lead_avf_polarity": "2. sütun alt (aVF) kırpmasından kontrol ediniz",
                    "summary": "I (+) ve aVF (+) ise normal eksen; I (+) ve aVF (-) ise sol aks deviasyonu açısından değerlendiriniz.",
                },
                "step4_intervals": {
                    "pr_interval_ms": str(caliper_info.get("raw", {}).get("PR", "Dijital pergel ile ölçülebilir")),
                    "qrs_duration_ms": str(caliper_info.get("raw", {}).get("QRS", "Dijital pergel ile ölçülebilir")),
                    "qt_qtc_ms": (
                        f"Hesaplanan QTc (Bazett): {caliper_info['computed_qtc']['qtc_bazett_ms']} ms"
                        if caliper_info["computed_qtc"]
                        else "QT ve R-R ölçümü girildiğinde otomatik hesaplanır"
                    ),
                    "caliper_used": caliper_used,
                    "summary": (
                        "Girdiğiniz pergel ölçümleri kaydedildi" + caliper_note
                        if caliper_used
                        else "Tuval üzerindeki 'Dijital Pergel' aracını kullanarak PR, QRS ve QT ölçebilirsiniz."
                    ),
                },
                "step5_morphology_st_t": {
                    "territories": [
                        {
                            "wall": "Inferior (II, III, aVF)",
                            "st_segment": "Kırpılmış I-III ve aVR-aVF bölgelerinden J noktasını inceleyiniz.",
                            "t_wave": "T dalgası polaritesini doğrulayınız.",
                            "q_wave": "Patolojik Q (>1 mm geniş, >%25 R) kontrolü.",
                            "status": "UNASSESSED",
                        },
                        {
                            "wall": "Septal & Anterior (V1-V4)",
                            "st_segment": "V2-V3 cinsiyet/yaş ST elevasyon eşiklerine dikkat ediniz.",
                            "t_wave": "Wellens Tip A/B (V2-V3) yönünden dikkatle inceleyiniz.",
                            "q_wave": "R dalgası progresyonunu kontrol ediniz.",
                            "status": "UNASSESSED",
                        },
                    ],
                    "summary": "Yapılandırılmış 6 adımlı şablon hazır; canlı görsel tanı yorumu için OpenRouter, Gemini veya OpenAI API anahtarı ekleyebilirsiniz.",
                },
                "step6_clinical_synthesis": {
                    "primary_diagnosis": "Canlı LLM Görsel Analizi İçin API Anahtarı Bekleniyor (Ön İşleme Tamamlandı)",
                    # Görsel okunmadığı için EKG'ye dayalı aciliyet atanamaz; "ROUTINE" yanlış güvence verir
                    "urgency": "URGENT" if any(k in complaint for k in URGENT_COMPLAINT_KEYWORDS) else "UNASSESSED",
                    "confidence_score": 0,
                    "differential_diagnoses": [],
                    "red_flags": (
                        [f"Hasta şikayeti ('{patient_context.get('chief_complaint')}') nedeniyle yüksek klinik öncelik ile hekim değerlendirmesi önerilir."]
                        if any(k in complaint for k in URGENT_COMPLAINT_KEYWORDS)
                        else ["Bu EKG henüz yorumlanmadı; aşağıdaki şablon bir tanı veya 'normal' sonucu değildir."]
                    ),
                    "guideline_matches": [
                        "Görüntü ön işleme ve anatomik derivasyon kırpma adımları başarıyla tamamlandı."
                    ],
                    "recommended_actions": [
                        "Sağ üstteki 'API Ayarları' butonundan veya backend/config.json dosyasından OpenRouter API anahtarınızı ve modelinizi girerek '6 Adımlı Klinik Analizi Başlat' butonuna basın.",
                        "Ya da üst menüden hazır Demo Vakaları (Normal Sinüs, İnferior STEMI, AFib) yükleyerek tam yapay zekâ muhakemesini test edin.",
                    ],
                },
                "erb_reasoning_chain": {
                    "target_dx": "awaiting_live_mllm_grounding",
                    "steps": [
                        {
                            "criterion_selection": "Jwoo5/ecg-reasoning-benchmark 17 tanı karar ağacı prompta bağlandı",
                            "finding_identification": "Canlı MLLM çağrısı yapıldığında görsel bulgular otomatik doğrulanacaktır.",
                            "ecg_grounding": {
                                "lead_grounding": ["I-III", "aVR-aVF", "V1-V3", "V4-V6", "Ritim Şeridi"],
                                "wave_grounding": "Tüm derivasyon kırpmaları modele gönderilmeye hazır",
                                "measurement_grounding": caliper_note.lstrip(" | ") or "Dijital pergel ölçümü bekleniyor",
                            },
                            "diagnostic_decision": "Ek bulgu gerekli",
                        }
                    ],
                },
            }

        result["mode"] = "demo_simulation"
        result["model_used"] = "Klinik Simülasyon Motoru (Çevrimdışı Demo)"
        if fallback_reason:
            result["fallback_note"] = fallback_reason
        result["computed_qtc"] = caliper_info["computed_qtc"]
        result["disclaimer"] = (
            "Bu çıktı eğitim ve klinik karar destek amaçlıdır; kesin tanı ve tedavi kararı hekim değerlendirmesi gerektirir."
        )
        return result

    def analyze(
        self,
        enhanced_bytes: bytes,
        lead_crops: List[Dict[str, Any]],
        patient_context: Dict[str, Any],
        caliper_measurements: Optional[Dict[str, Any]] = None,
        case_hint: Optional[str] = None,
        quality: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """EKG görüntüsünü (ve kırpmalarını) aktif LLM sağlayıcısı veya demo simülasyon ile analiz eder."""
        cfg = self.load_config()
        caliper_info = summarize_caliper_and_qtc(caliper_measurements, patient_context)
        provider = cfg.get("provider", "openrouter")

        images: List[Tuple[str, bytes]] = [(FULL_IMAGE_LABEL, enhanced_bytes)]
        for crop in lead_crops[:5]:
            raw = _data_uri_to_bytes(crop.get("image_b64", ""))
            if raw:
                images.append((_crop_label(len(images) + 1, crop), raw))

        prompt = self.build_clinical_prompt(patient_context, caliper_measurements)

        def _finalize_live(parsed: Dict[str, Any], label: str) -> Dict[str, Any]:
            parsed = _validate_llm_payload(parsed)
            parsed["mode"] = "live_llm"
            parsed["model_used"] = label
            parsed["computed_qtc"] = caliper_info["computed_qtc"]
            parsed["disclaimer"] = (
                "Bu çıktı yapay zekâ klinik karar destek analizidir; kesin tanı ve tedavi kararı hekim değerlendirmesi gerektirir."
            )
            return parsed

        if provider == "openrouter" and cfg.get("openrouter_api_key"):
            model_name = cfg.get("openrouter_model", "google/gemini-3.8-flash")
            base_url = cfg.get("openrouter_base_url", "https://openrouter.ai/api/v1")
            try:
                parsed = self._call_openrouter(cfg["openrouter_api_key"], model_name, base_url, prompt, images)
                return _finalize_live(parsed, f"OpenRouter ({model_name})")
            except Exception as exc:
                return self._generate_demo_response(
                    patient_context,
                    caliper_info,
                    case_hint,
                    quality,
                    fallback_reason=f"OpenRouter API çağrısı başarısız oldu ({exc}); demo simülasyona düşüldü.",
                )

        if provider == "gemini" and cfg.get("gemini_api_key"):
            model_name = cfg.get("gemini_model", "gemini-2.0-flash")
            try:
                parsed = self._call_gemini(cfg["gemini_api_key"], model_name, prompt, images)
                return _finalize_live(parsed, f"Gemini ({model_name})")
            except Exception as exc:
                return self._generate_demo_response(
                    patient_context,
                    caliper_info,
                    case_hint,
                    quality,
                    fallback_reason=f"Gemini API çağrısı başarısız oldu ({exc}); demo simülasyona düşüldü.",
                )

        if provider == "openai" and cfg.get("openai_api_key"):
            model_name = cfg.get("openai_model", "gpt-4o")
            try:
                parsed = self._call_openai(cfg["openai_api_key"], model_name, prompt, images)
                return _finalize_live(parsed, f"OpenAI ({model_name})")
            except Exception as exc:
                return self._generate_demo_response(
                    patient_context,
                    caliper_info,
                    case_hint,
                    quality,
                    fallback_reason=f"OpenAI API çağrısı başarısız oldu ({exc}); demo simülasyona düşüldü.",
                )

        return self._generate_demo_response(patient_context, caliper_info, case_hint, quality)
