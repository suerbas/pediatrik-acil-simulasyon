# ECG_Helper — EKG Klinik Karar Destek Sistemi

`Jwoo5/ecg-reasoning-benchmark` makalesindeki **çok adımlı klinik muhakeme (6-Step Chain-of-Thought)** protokolü ile **OpenCV görüntü ön işleme** ve **interaktif dijital EKG pergelini (caliper)** birleştiren FastAPI + React (Vite) uygulamasıdır.

## Özellikler

- **OpenCV Görüntü Ön İşleme (`backend/ecg_preprocessor.py`):**
  - **CLAHE Netleştirme:** Gölgeleri ve aydınlatma farklarını dengeler.
  - **Yüksek Kontrast Sinyal Çıkarımı:** Pembe/kırmızı EKG ızgarasını baskılayıp dalga formunu öne çıkarır.
  - **Otomatik 12-Derivasyon + Ritim Şeridi Kırpma:** `I-III`, `aVR-aVF`, `V1-V3`, `V4-V6` ve `Uzun DII` bölgelerini ayrı ayrı yakınlaştırır.
  - **Görüntü Kalitesi Analizi:** Çözünürlük, Laplacian netlik skoru ve parlaklık uyarıları üretir.
- **İnteraktif Dijital EKG Pergeli (`frontend/src/components/EcgCanvasViewer.jsx`):**
  - Akıcı zoom/pan ve 3 görüntü modu arasında anlık geçiş.
  - İki nokta işaretleyerek `ms`, `bpm` ve `mV (mm)` ölçümü; kağıt hızı (`25/50 mm/sn`) ve kazanç (`5/10/20 mm/mV`) seçilebilir.
  - Fare ve dokunmatik aynı Pointer Events akışını kullanır: dokunuş/tıklama nokta koyar, sürükleme kaydırır, iki parmak yakınlaştırır.
  - Yüklenen fotoğraflarda px/mm değeri yalnızca tahmindir; **Kalibre Et** ile yatayda 5 büyük kare (25 mm) işaretlenmeden ölçüm kaydedilemez.
  - Ölçümleri `PR`, `QRS`, `QT`, `R-R`, `ST Sapması` (işaretli: + elevasyon / − depresyon; 1. nokta izoelektrik hat, 2. nokta J noktası) olarak kaydedip LLM'e kesin referans gönderme.
  - **Deterministik QTc:** Bazett ve Fridericia uygulama tarafından hesaplanır (kalp hızı 60-100/dk dışında Fridericia esas alınır). Erişkin eşikleri cinsiyete özgüdür — Erkek: sınırda 431-450, uzamış > 450 ms; Kadın: sınırda 451-470, uzamış > 470 ms (Goldenberg, Moss & Zareba 2006); >= 500 ms kritik. Cinsiyet girilmediyse veya hasta < 16 yaş ise bu durum yorumda belirtilir. Aynı mantık `backend/clinical_guidelines.py` ve `frontend/src/utils/clinicalData.js` dosyalarında birebir tutulmalıdır.
- **6 Adımlı Klinik Muhakeme Motoru (`backend/ecg_reasoning_engine.py`):**
  1. Kalibrasyon & Kalite
  2. Hız & Ritim
  3. Kardiyak Eksen
  4. İletim Aralıkları (PR, QRS, QT/QTc — Bazett & Fridericia)
  5. Anatomik Duvar Morfolojisi (Inferior, Septal/Anterior, Lateral, aVR)
  6. Klinik Sentez, Ayırıcı Tanı, Kırmızı Bayraklar ve ESC/AHA Kılavuz Eşleşmesi
- **Yorumlanmamış EKG güvenliği:** API anahtarı yokken yüklenen bir fotoğraf için rapor `EKG HENÜZ YORUMLANMADI` / `DEĞERLENDİRİLMEDİ` etiketleriyle döner; hiçbir duvar "NORMAL", aciliyet "RUTİN" olarak gösterilmez.
- **Çevrimdışı Hazır Demo Vakalar:** API anahtarı olmadan bile test edebilmeniz için sentetik 12-derivasyon EKG üreteci (`Normal Sinüs Ritmi`, `Akut İnferior STEMI`, `Atriyal Fibrilasyon`).

## Kurulum ve Çalıştırma

### Otomatik Başlatma (Windows)
`baslat.bat` dosyasına çift tıklamanız yeterlidir. Backend (`8000`) ve Frontend (`5173`) otomatik başlatılır.

### Manuel Başlatma
1. **Backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ```
2. **Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
Tarayıcıda `http://localhost:5173` adresini açın. Canlı görsel LLM yorumu için `backend/config.json` dosyasına veya sağ üstteki **API Ayarları** butonuna OpenRouter (veya Gemini/OpenAI) API anahtarınızı ve model kimliğinizi ekleyebilirsiniz.

## Güvenlik Notları

- Yerel FastAPI sunucusu CORS'u yalnızca `localhost` / `127.0.0.1` kökenlerine açar; arayüz Vite proxy'si üzerinden aynı kökenden konuşur.
- Yerel sunucu modunda API anahtarları yalnızca `backend/config.json` dosyasında tutulur. Sunucusuz (Vercel / yalnızca tarayıcı) modda girilen anahtar tarayıcının `localStorage` alanında saklanır ve doğrudan sağlayıcıya gönderilir; paylaşılan cihazlarda anahtar girmeyin.
- Vercel'de `OPENROUTER_API_KEY` (veya `GEMINI_API_KEY` / `OPENAI_API_KEY`) ortam değişkeni tanımlanırsa `/api/analyze` bu anahtarla herkese açık çalışır. Dağıtımı Vercel Deployment Protection veya benzeri bir erişim kontrolüyle korumanız önerilir.
- `api/analyze.js` (CommonJS) ile `frontend/api/analyze.js` (ESM) aynı mantığı içerir; biri değişince diğeri de güncellenmelidir.
