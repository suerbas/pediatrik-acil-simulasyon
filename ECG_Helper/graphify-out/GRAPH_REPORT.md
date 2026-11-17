# Graph Report - ECG_Helper  (2026-11-16)

## Corpus Check
- Corpus is ~38,645 words - fits in a single context window. You may not need a graph.

## Summary
- 312 nodes · 562 edges · 14 communities
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 33 edges (avg confidence: 0.83)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Frontend Uygulaması (React)
- Backend API ve Uç Noktalar
- LLM Akıl Yürütme Motoru
- Görüntü Ön İşleme
- Python Bağımlılıkları
- İstemci Tarafı EKG Motoru
- Görüntü Kütüphaneleri ve Derivasyon Kuralları
- Klinik Kılavuz ve QTc
- Frontend Bağımlılıkları
- Doğruluk Ölçümü ve Kaynaklar
- Serverless Analiz Fonksiyonu
- Serverless Analiz Fonksiyonu (kopya)
- Vercel Yapılandırması (frontend)
- Vercel Yapılandırması (kök)

## God Nodes (most connected - your core abstractions)
1. `preprocess_ecg_image()` - 15 edges
2. `App()` - 15 edges
3. `ECGReasoningEngine` - 14 edges
4. `calculate_qtc()` - 11 edges
5. `generate_synthetic_ecg()` - 11 edges
6. `analyzeEcgClientOrServer()` - 11 edges
7. `analyze_ecg()` - 10 edges
8. `preprocessEcgInBrowser()` - 10 edges
9. `update_config()` - 8 edges
10. `react` - 8 edges

## Surprising Connections (you probably didn't know these)
- `fastapi` --implements--> `FastAPI + OpenCV backend`  [INFERRED]
  backend/requirements.txt → DEVIR_NOTU.md
- `pydantic` --implements--> `FastAPI + OpenCV backend`  [INFERRED]
  backend/requirements.txt → DEVIR_NOTU.md
- `python-multipart` --implements--> `FastAPI + OpenCV backend`  [INFERRED]
  backend/requirements.txt → DEVIR_NOTU.md
- `uvicorn` --implements--> `FastAPI + OpenCV backend`  [INFERRED]
  backend/requirements.txt → DEVIR_NOTU.md
- `google-genai (Gemini sağlayıcısı)` --references--> `Üç çalışma modu (yerel FastAPI, tarayıcıdan doğrudan sağlayıcı, Vercel sunucu anahtarı)`  [INFERRED]
  backend/requirements.txt → DEVIR_NOTU.md

## Import Cycles
- None detected.

## Communities (14 total, 0 thin omitted)

### Community 0 - "Frontend Uygulaması (React)"
Cohesion: 0.08
Nodes (38): App(), buildPublicStatus(), DEFAULT_LOCAL_CFG, EMPTY_PATIENT, loadLocalConfig(), saveLocalConfig(), SECRET_KEYS, clampZoom() (+30 more)

### Community 1 - "Backend API ve Uç Noktalar"
Cohesion: 0.09
Nodes (15): analyze_ecg(), AnalyzeRequest, compute_qtc_endpoint(), ConfigUpdateRequest, _decode_b64_image(), get_config(), get_guidelines(), health_check() (+7 more)

### Community 2 - "LLM Akıl Yürütme Motoru"
Cohesion: 0.10
Nodes (7): _crop_label(), ECGReasoningEngine, _finalize_live(), _extract_json_block(), _lower_tr(), summarize_caliper_and_qtc(), _validate_llm_payload()

### Community 3 - "Görüntü Ön İşleme"
Cohesion: 0.14
Nodes (12): assess_image_quality(), crop_standard_leads(), encode_image_bytes_to_png_b64(), _encode_png_data_uri(), _enhance_clahe(), _extract_high_contrast_waveform(), _gaussian_wave(), _generate_lead_signal() (+4 more)

### Community 4 - "Python Bağımlılıkları"
Cohesion: 0.08
Nodes (24): fastapi, google-genai (Gemini sağlayıcısı), openai (OpenAI sağlayıcısı), pydantic, python-multipart, uvicorn, api/analyze.js (CommonJS, Vercel sunucusuz fonksiyon), FastAPI + OpenCV backend (+16 more)

### Community 5 - "İstemci Tarafı EKG Motoru"
Cohesion: 0.14
Nodes (27): buildClinicalPrompt(), summarizeCaliperAndQtc(), analyzeEcgClientOrServer(), assessImageQuality(), buildEnhancedCanvas(), buildLabeledImages(), buildWaveformCanvas(), callGeminiBrowser() (+19 more)

### Community 6 - "Görüntü Kütüphaneleri ve Derivasyon Kuralları"
Cohesion: 0.09
Nodes (23): numpy, opencv-python, Pillow, 12x1 derivasyon düzeni (her derivasyon tam genişlikte tek satır), Bazal hat kayması (pediatrik EKG'lerde derivasyona göre değişen sorun; görüntü döndürme eklenmedi), Derivasyon çerçevesi modu (hekim köşe işaretleriyle düzen seçer, kırpmalar tarayıcıda üretilir), Pergel kalibrasyon kapısı (yatayda 5 büyük kare = 25 mm işaretlenmeden ölçüm kaydedilmez), ST (3 Nokta) ölçümü: PR1 - J - PR2, sapma PR-PR çizgisine göre (+15 more)

### Community 7 - "Klinik Kılavuz ve QTc"
Cohesion: 0.14
Nodes (6): calculate_qtc(), format_guidelines_for_prompt(), load_erb_benchmark_trees(), _normalize_sex(), _parse_age(), _data_uri_to_bytes()

### Community 8 - "Frontend Bağımlılıkları"
Cohesion: 0.12
Nodes (18): dependencies, lucide-react@0.460.0, react@18.3.1, react-dom@18.3.1, devDependencies, vite@5.4.11, @vitejs/plugin-react@4.3.4, name (+10 more)

### Community 9 - "Doğruluk Ölçümü ve Kaynaklar"
Cohesion: 0.31
Nodes (7): 6 adımlı LLM çıktı şeması doğrulaması (EXPECTED_STEP_KEYS), Üç modelin doğruluk ölçümü (durum belirsiz: başlıkta ONAY BEKLİYOR, 15 Kasım notunda iptal edildi), Jwoo5 ecg-reasoning-benchmark (6 adımlı CoT protokolü, 17 tanı karar ağacı), Kaynaklar (Jwoo5 repo, arXiv 2603.14326, BenchLM derlemesi), Model fiyat ve maliyet tahminleri (gemini-3.8-flash, gpt-6.1-terra, gpt-6.1-sol), Varsayılan OpenRouter modeli google/gemini-3.8-flash, PTB-XL benchmark verisi (Hugging Face Jwoo5/ECG-Reasoning-Benchmark)

### Community 10 - "Serverless Analiz Fonksiyonu"
Cohesion: 0.50
Nodes (7): callGemini(), callOpenAiCompatible(), EXPECTED_STEP_KEYS, extractJsonBlock(), fetchWithTimeout(), handler(), resolveServerProvider()

### Community 11 - "Serverless Analiz Fonksiyonu (kopya)"
Cohesion: 0.48
Nodes (5): callGemini(), callOpenAiCompatible(), EXPECTED_STEP_KEYS, extractJsonBlock(), fetchWithTimeout()

### Community 12 - "Vercel Yapılandırması (frontend)"
Cohesion: 0.40
Nodes (4): buildCommand, framework, outputDirectory, $schema

### Community 13 - "Vercel Yapılandırması (kök)"
Cohesion: 0.40
Nodes (4): buildCommand, installCommand, outputDirectory, $schema

## Ambiguous Edges - Review These
- `Varsayılan OpenRouter modeli google/gemini-3.8-flash` → `Üç modelin doğruluk ölçümü (durum belirsiz: başlıkta ONAY BEKLİYOR, 15 Kasım notunda iptal edildi)`  [AMBIGUOUS]
  DEVIR_NOTU.md · relation: conceptually_related_to

## Knowledge Gaps
- **22 isolated node(s):** `frontend/api/analyze.js (ESM kopya)`, `12x1 derivasyon düzeni (her derivasyon tam genişlikte tek satır)`, `Vercel SSO koruması (ssoProtection all; anonim /api/analyze 401)`, `Sentetik EKG üretecinde T dalgası zamanlama düzeltmesi (sentetik QT yaklaşık 369/378 ms)`, `Pergel kalibrasyon kapısı (yatayda 5 büyük kare = 25 mm işaretlenmeden ölçüm kaydedilmez)` (+17 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 118 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `6 adımlı klinik muhakeme motoru (6-Step CoT)` connect `Görüntü Kütüphaneleri ve Derivasyon Kuralları` to `Klinik Kılavuz ve QTc`?**
  _High betweenness centrality (0.167) - this node is a cross-community bridge._
- **What connects `frontend/api/analyze.js (ESM kopya)`, `12x1 derivasyon düzeni (her derivasyon tam genişlikte tek satır)`, `Vercel SSO koruması (ssoProtection all; anonim /api/analyze 401)` to the rest of the system?**
  _22 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Frontend Uygulaması (React)` be split into smaller, more focused modules?**
  _Cohesion score 0.0786308973172988 - nodes in this community are weakly interconnected._
- **Should `Backend API ve Uç Noktalar` be split into smaller, more focused modules?**
  _Cohesion score 0.09246088193456614 - nodes in this community are weakly interconnected._
- **Should `LLM Akıl Yürütme Motoru` be split into smaller, more focused modules?**
  _Cohesion score 0.09841269841269841 - nodes in this community are weakly interconnected._
- **Should `Görüntü Ön İşleme` be split into smaller, more focused modules?**
  _Cohesion score 0.14408602150537633 - nodes in this community are weakly interconnected._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Varsayılan OpenRouter modeli google/gemini-3.8-flash` and `Üç modelin doğruluk ölçümü (durum belirsiz: başlıkta ONAY BEKLİYOR, 15 Kasım notunda iptal edildi)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._