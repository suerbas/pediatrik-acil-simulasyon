# Mesai Planlayıcı

Yeşil ve sarı alan için eşit ve çakışmasız mesai paylaşımı yapan React (Vite) uygulaması.

- Sabah şifti: 08:00–16:30 · Akşam şifti: 16:30–01:30
- Her an yeşilde 1, sarıda 1 kişi bulunur; bir kişi aynı anda iki alanda olamaz.
- Kişiler harflerle gösterilir (sabah A'dan başlar, akşam sabahın devamından sürer).
- Çift kişi sayısında ikili eşleşme: A yeşil/B sarı → B yeşil/A sarı.
- Tek kişi sayısında döngü: A/B → B/C → C/A …
- "2'ye böl" / "3'e böl" seçeneği ile her kişinin süresi parçalara bölünür (3 kişi → 6 kişilik gibi).

## Geliştirme

```bash
npm install
npm run dev
npm test   # plan mantığı doğrulaması
```

## Vercel

Projeyi Vercel'e eklerken **Root Directory** olarak `mesai-planlayici` seçin. Framework (Vite), build komutu ve çıktı klasörü `vercel.json` ile ayarlıdır.
