# Pediatrik Acil Vaka Arşivi — Web (React + Vite)

Streamlit arşivinin statik sürümü. Sunucu gerektirmez; Vercel'de statik site olarak yayınlanır.

## Vakalar nereden geliyor?

Vakaların tek kaynağı kök dizindeki `cases_green_part*.py` / `cases_yellow_part*.py` dosyalarıdır.
Bir vaka değiştiğinde JSON'u yeniden üretin ve değişen dosyaları commit edin:

```bash
python web/scripts/export_cases.py
```

Bu betik `src/data/index.json` (kart listesi), `public/cases/<ID>.json` (vaka detayı),
`public/search.json` (arama havuzu) ve `public/assets/images/` (görüntüler) dosyalarını yazar.
Vital bulgu işaretleri (`pediatric_evaluator.py`) dışa aktarma sırasında hesaplanır.

## Yerelde çalıştırma

```bash
cd web
npm install
npm run dev
```

## Vercel

Projeyi içe aktarırken **Root Directory** olarak `web` seçin. Framework: Vite,
build komutu `npm run build`, çıktı klasörü `dist` (bunlar `vercel.json` içinde de tanımlı).
