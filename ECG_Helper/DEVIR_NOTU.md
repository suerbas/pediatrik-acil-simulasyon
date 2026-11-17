# ECG_Helper — Devir Notu

Son güncelleme: 15 Kasım 2026. Bu not, projeye başka bir modelle/oturumla devam edebilmek için yazıldı.

## Proje nedir

12 derivasyonlu EKG fotoğraflarını ön işleyen (kalite kontrol, kontrast/ızgara bastırma, 5 anatomik bölge kırpma), dijital pergel + deterministik QTc hesabı sunan ve `Jwoo5/ecg-reasoning-benchmark` deposunun 17 tanı karar ağacıyla 6 adımlı LLM klinik muhakemesi üreten prototip. Klinik karar destek amaçlıdır; kesin tanı aracı değildir.

- **Backend:** FastAPI + OpenCV (`backend/`), yalnızca yerelde çalışır.
- **Frontend:** React 18 + Vite 5 (`frontend/`).
- **Vercel:** Serverless fonksiyon `api/analyze.js` (CommonJS) ve onun ESM kopyası `frontend/api/analyze.js`. İkisi aynı mantığı taşımalı; biri değişince diğeri de güncellenmeli.

Üç çalışma modu var: yerel FastAPI (Vite proxy `/api` → 127.0.0.1:8000), tarayıcıdan doğrudan sağlayıcı çağrısı (anahtar localStorage'da), Vercel sunucu anahtarı (ortam değişkeni).

## Kullanıcı ve çalışma kuralları

- Kullanıcı hekim; Türkçe ve "siz" hitabıyla yazılır.
- **Klinik eşik/doz/ilaç bilgisi** değiştirilmeden önce web'den kaynakla doğrulanır, yanıtta kaynak verilir, doğrulanamadıysa açıkça söylenir, kılavuzdan sapma belirtilir.
- **Git:** Kullanıcı ayrı dal açılınca hemen `main`'e birleştirip dalı sildirdi; küçük değişiklikler doğrudan `main`'e commit edilebilir. Commit ve push yalnızca kullanıcı isteyince yapılır.
- **Maliyet doğuran işler** (ücretli API çağrısı, ölçüm) kullanıcı onayı olmadan başlatılmaz.
- `backend/config.json` API anahtarı içerebilir: içeriği yazdırılmaz, commit edilmez, Vercel'e yüklenmez (gitignore ve `.vercelignore` kapsamında).
- Parola/oturum açma adımları kullanıcıya bırakılır.

## Depo ve dağıtım

- **Git kökü:** `C:\Users\Suat\OneDrive\Desktop\Kerem\Video_analiz` (ECG_Helper bunun alt klasörü).
- **Remote'lar:** `origin` = `github.com/suerbas/pediatrik-acil-simulasyon` (push buraya). İkinci remote `arsiv` = `pediatrik-vaka-arsivi`; oraya **push edilmez**.
- Üst klasördeki `../.claude/` başka projeye aittir, dokunulmaz.
- **Son commit:** `e435a11 chore(ecg): varsayilan OpenRouter modeli google/gemini-3.8-flash yapildi` (origin/main'e push edildi).
- **Vercel:** proje `suerbas-projects/ecg-helper`, adres `https://ecg-helper.vercel.app`, hobby plan. Proje GitHub'a bağlı değil; güncellemek için `ECG_Helper` klasöründe `vercel --prod` çalıştırılır. `.vercel/project.json` elle yazıldı (`vercel link` Windows'ta symlink hatası veriyor).
- **Gizlilik:** Site Vercel oturum korumasında (`ssoProtection: all`). Anonim erişim giriş sayfasına yönlenir, `/api/analyze` 401 döner.
- **Sunucu anahtarı:** Vercel'de API anahtarı tanımlı **değil**; canlı site anahtarsız demo modunda ya da kullanıcının tarayıcıdaki kendi anahtarıyla çalışır.

## Yapılanlar (kod taraması ve düzeltmeler)

**QTc ve klinik mantık**
- `calculate_qtc` (Python) ve `calculateQtc` (JS) yeniden yazıldı ve birebir eşit tutuluyor: Bazett + Fridericia; kalp hızı 60–100 dışında Fridericia esas.
- Erişkin eşikleri: erkek sınırda 431–450 / uzamış >450; kadın 451–470 / >470; ≥500 kritik; <350 kısa. Cinsiyet yoksa veya yaş <16 ise 451–470 / >470 bandı + açıklama.
- Doğrulama durumu: erişkin eşikleri ikincil kaynaklarla doğrulandı. Pediatrik eşikler doğrulanamadı ve eklenmedi. Kısa QT <350 ve ≥500 yeniden doğrulanmadı. Bazı yeni kaynaklar eşikleri yukarı çekiyor (erkek >470, kadın >480); bu sapma kullanıcıya bildirildi.

**Rapor güvenliği**
- Yorumlanmamış EKG artık "NORMAL/ROUTINE" yerine "UNASSESSED" gösterilir.
- LLM çıktısı 6 adımlı şemaya göre doğrulanır (`EXPECTED_STEP_KEYS`).
- Görseller etiketli gönderilir (tam görüntü + 5 kırpma); 400/422'de yalın istekle tek yineleme; 120 sn zaman aşımı.

**Güvenlik**
- CORS yalnızca localhost; `openrouter_base_url` https doğrulaması; Gemini anahtarı URL yerine başlıkta.
- Yerel sunucu modunda anahtarlar localStorage'a yazılmaz.

**Arayüz**
- `EcgCanvasViewer.jsx` Pointer Events ile yeniden yazıldı (dokunma = nokta, sürükleme = kaydırma, iki parmak = yakınlaştırma, imleç etrafında zoom).
- Kalibrasyon kapısı, kağıt hızı/kazanç ayarı, ST sapması işareti.
- Yarış koşulu koruması (`ecgSessionRef`), sunucu anahtarı rozeti, görsel olmayan dosya reddi, yüklemede hasta bilgisinin sıfırlanması.

**Diğer**
- Sentetik EKG üretecinde T dalgası zamanlaması düzeltildi (sentetik QT ≈ 369/378 ms).
- Varsayılan OpenRouter modeli `google/gemini-3.8-flash` yapıldı (backend, arayüz, serverless).
- `README.md` güncellendi; `.vercelignore` ve `.claude/launch.json` (ön yüz, port 5183) eklendi.

## Doğrulananlar ve doğrulanmayanlar

**Geçen testler:** backend duman testleri, JS/serverless sahte (mock) testleri, Python–JS QTc eşitliği (14 örnek), `vite build`, tarayıcıda pergel etkileşimleri ve UNASSESSED raporu.

**Doğrulanmadı:**
- Gerçek API anahtarıyla canlı model çağrısı hiç yapılmadı.
- `google/gemini-3.8-flash`, `openai/gpt-6.1-terra`, `openai/gpt-6.1-sol` modellerinin görsel girdi kabul ettiği teyit edilmedi.
- Gerçek telefonda deneme yapılmadı.
- Model fiyatları OpenRouter'ın kendi sayfasından değil, 11 Kasım 2026 tarihli BenchLM derlemesinden.

## Model önerisi ve maliyet tahminleri

| Model | Giriş / Çıkış ($/1M token) | Tipik bir EKG okuması |
|---|---|---|
| `google/gemini-3.8-flash` (varsayılan) | 0,82 / 4,13 | ~0,018 $ |
| `openai/gpt-6.1-terra` | 1,00 / 5,00 | ~0,022 $ |
| `openai/gpt-6.1-sol` | 2,00 / 10,00 | ~0,043 $ |

Bir okuma kabaca 9 bin giriş + 2,5 bin çıkış token'ı (tahmin, ölçüm değil).

## Açık iş: üç modelin doğruluk ölçümü (ONAY BEKLİYOR)

Kullanıcı repodaki sorularla üç modelin doğruluğunu ölçmek istedi, ancak önce maliyet öngörüsü istedi ve **"Ben onaylamadan ölçüm yapma"** dedi. Öngörü sunuldu; kullanıcı henüz kapsam seçmedi. Ölçüm başlatılmadı, hiçbir betik yazılmadı, hiçbir veri indirilmedi.

**Benchmark hakkında bilinenler**
- Veri: Hugging Face `Jwoo5/ECG-Reasoning-Benchmark` (ve depoda `data/ptbxl.jsonl`, `data/mimic_iv_ecg.jsonl`). PTB-XL 3.084, MIMIC-IV-ECG 3.359 örnek; 17 tanı. Yalnızca PTB-XL önerildi.
- Her örnek çok turlu bir diyalog: ilk tanı sorusu + döngüler (kriter seçimi, bulgu, derivasyon/dalga gösterme, karar). İncelenen 3 örnekte 9'ar soru vardı. Her soru ayrı çağrı; görsel her çağrıda yeniden gider.
- EKG görselleri depoda yok: PTB-XL kayıtları PhysioNet'ten indirilip `ecg-plot` ile görüntüye çevrilir (ücretsiz).
- Yerelde yalnızca karar ağaçları var: `backend/erb_benchmark_trees.json` ve `frontend/src/utils/erb_benchmark_trees.json`.

**Sunulan maliyet öngörüsü (üç model toplamı)**

| Kapsam | Çağrı | Düşük | Beklenen | Yüksek |
|---|---|---|---|---|
| Pilot: 34 örnek (tanı başına 1+1) | ~900 | 3 $ | 5 $ | 9 $ |
| Önerilen: 170 örnek (tanı başına 5+5) | ~4.600 | 15 $ | 23 $ | 42 $ |
| Yalnızca ilk tanı sorusu, 170 örnek | ~500 | 1,5 $ | 2,5 $ | 5 $ |
| PTB-XL'in tamamı | ~83.000 | 265 $ | 425 $ | 770 $ |

Varsayım: çağrı başına ~2.200 giriş token'ı, örnek başına 9 çağrı. En büyük belirsizlik modellerin gizli akıl yürütme token'ları.

**Onay gelirse izlenecek yol**
1. Kullanıcıdan harcama limitli ayrı bir OpenRouter anahtarı istenir (ör. 30 $); anahtar sohbete yazılmaz, ortam değişkenine konur. `backend/config.json` içindeki anahtar izinsiz kullanılmaz.
2. Seçilen PTB-XL kayıtları indirilir, görüntüye çevrilir.
3. Önce 5 örnek çalıştırılıp gerçek token tüketimi kullanıcıya bildirilir; öngörüden belirgin saparsa durulur.
4. Sonuç: model × tanı doğruluk tablosu. Not: bu ölçüm uygulamanın fotoğraf ön işlemesini ve 6 adımlı istemini değil, modelin temiz EKG görüntüsünü okuma becerisini sınar.

## 15 Kasım 2026 oturumu: ilk gerçek EKG ve derivasyon çerçevesi

- Kullanıcı doğruluk ölçümünü **iptal etti** (10 $ kota, verimli harcamak istiyor). Ölçüm yapılmayacak.
- İlk canlı çağrı yapıldı (kullanıcının kendi anahtarı, `gemini-3.8-flash`, ~0,02 $). Model, DII'si açıkça pozitif bir trasede LAFB + 1. derece AV blok dedi (%92 güven); hızı ~96 verdi, gözle ~130–140. Neden: sabit oranlı kırpmalar başlıksız fotoğrafta aVR, V4 ve birçok etiketi dışarıda bırakıyordu.
- Yapılan düzeltme (`50313c8`, origin/main'e push edildi, `vercel --prod` ile canlıya alındı):
  - Görüntüleyicide **"Derivasyon Çerçevesi"** modu: hekim trase alanının sol üst ve sağ alt köşesine dokunur, düzeni seçer (3×4 + ritim / 3×4). `computeFrameRegions` + `cropLeadsFromFrame` (`ecgClientEngine.js`) kırpmaları tarayıcıda yeniden üretir; üç modda da kırpmalar analiz isteğiyle tarayıcıdan gider.
  - Yüklenen fotoğrafta çerçeve seçilmezse sabit kırpmalar **modele gönderilmez** (yalnızca tam görüntü), galeri ve bindirme gizlenir, uyarı rozeti çıkar. Sentetik demo vakalar eskisi gibi.
  - Kırpma etiketi kaynağa göre değişir (`source: "manual_frame"`; JS `cropLabel` ve Python `_crop_label` aynı metin).
  - İstemlere (JS + Python) kural 7: eksen I, II, aVF polaritesinden türetilir; DII net pozitifse sol aks deviasyonu denmez. Şemaya `lead_ii_polarity` eklendi, raporda gösteriliyor.
- Doğrulama: `vite build` geçti; tarayıcıda kullanıcının EKG'siyle çerçeve seçildi, 5 kırpma doğru sütunları ve etiketleri içeriyor; demo vaka galerisi bozulmadı. Yeni istemle canlı çağrı yapılmadı.
- Kalan öneri: kırpma kenarına değen trase için kalite uyarısı (yapılmadı).
- Kullanıcı iki pediatrik EKG fotoğrafı gösterdi: ızgara düz, sorun derivasyona göre değişen **bazal hat kayması**. Bu yüzden görüntüyü döndürme (eğiklik düzeltme) **eklenmedi**.
- Eklenen (`a79e328`, push edildi ve canlıda): pergelde **"ST (3 Nokta)"** modu (`computeStThreePoint`, `EcgCanvasViewer.jsx`): PR1 → J → PR2, sapma PR–PR çizgisine göre; derivasyon seçilerek `ST Sapması (<derivasyon>)` anahtarıyla kaydedilir, kalibrasyon şart. İstemlere (JS + Python) kural 8: derivasyon bazında kayma bildirimi, kaymalı derivasyonda ST/T yorumu yok, çoğunluk kaymalıysa duvar UNASSESSED, 3 noktalı ölçüm kesin referans.
- Doğrulama: `vite build` geçti; 2. örnekte DI'de eğimli atımda 3 noktalı ölçüm ~0 mm verdi (aynı noktalarla 2 noktalı yöntem ~1 mm sahte depresyon verirdi); kayıt rozeti doğru. Yeni istemle canlı çağrı yapılmadı.
- Not: cihaz raporlarında "Age not entered, assumed to be 50" yazıyor; çocuk EKG'lerinde yaş alanı doldurulmalı.
- Eklenen (`e9cd8c0`, push edildi ve canlıda): çerçevede **12×1** düzeni (her derivasyon tam genişlikte tek satır). 12 eşit satır, üçerli gruplar → 4 kırpma (ritim şeridi yok), dikey pay satır yüksekliğinin yarısı. Kırpma etiketi `layout: "12x1"` ile ayrı metin (JS + Python). Sentetik 12 satırlı görüntüyle denendi: 4 kırpma doğru başlıklarla üretildi; tarayıcı bölmesi ekran görüntüsü vermediği için görsel kontrol yerine geometri hesapla doğrulandı. Gerçek 12×1 fotoğrafla denenmedi.

## Diğer öneriler (istenmedi, beklemede)

- Tanısı bilinen gerçek bir EKG ile `gemini-3.8-flash` denemesi.
- Pediatrik QTc eşiklerinin kaynakla doğrulanıp eklenmesi.

## Kaynaklar

- https://github.com/Jwoo5/ecg-reasoning-benchmark
- https://arxiv.org/abs/2603.14326
- https://benchlm.ai/hosts/openrouter
