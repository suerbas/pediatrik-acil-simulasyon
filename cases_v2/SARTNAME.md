# Vaka Yeniden Yazım Şartnamesi (v2)

Amaç: Pediatrik acil simülasyonundaki vakaları **zorlayıcı, gerçekçi ve ipucu sızdırmayan** hale getirmek.
Kullanıcı (deneyimli pediatrist) şikayeti: "Seçenekleri geçerken tanı hakkında fikir veren bilgiler çıkıyor; doğru seçenek hep
ilk, uzun ve detaylı; yanlışlar o kadar alakasız ki hata yapmak mümkün değil."

## Veri yapısı (değişmeyecek)
Her vaka bir dict:
```python
{'id': 'Y01', 'category': '<mevcut kategoriyi AYNEN koru>', 'age': ..., 'gender': ..., 'complaint': ..., 'history': ...,
 'final_diagnosis': ..., 'disposition': ..., 'case_pearl': ...,
 'steps': [ {'stage_title': ..., 'question': ..., 'options': [ ... 4 seçenek ... ]}, ... ]}
```
Doğru seçenek: `{'text', 'is_correct': True, 'explanation', 'new_finding'}` (+ gerekiyorsa `'triggers_yellow_transfer': True`)
Yanlış seçenek: `{'text', 'is_correct': False, 'scenario_update', 'teaching_point'}`

Uygulama seçenekleri her vakada rastgele karıştırıyor, yine de ham veride doğru seçeneğin indeksini çeşitlendir.

## Zorunlu kurallar
1. **Her adımda tam 4 seçenek**, tam 1 doğru.
2. **Uzunluk dengesi:** Her seçeneğin `text`'i 12–35 kelime. Aynı adımdaki en uzun seçenek en kısanın 1.6 katını geçmesin.
   Doğru seçenek en uzun olmak ZORUNDA değil; çoğu adımda bir yanlış seçenek en uzun olsun. Tümü aynı profesyonel tıbbi dilde.
3. **Spoiler yasağı (tanı adımından ÖNCEKİ tüm adımlarda):** `stage_title`, `question`, tüm seçeneklerin `text`'i,
   `new_finding`, `explanation`, `scenario_update`, `teaching_point` alanlarında **final tanının adı, eş anlamlısı,
   kısaltması veya ona özgü skor/eponim yorumu GEÇMEYECEK**. Örn. impetigo vakasında 1-2. adımlarda "impetigo",
   "bal rengi krut impetigo için tipik" vb. yok. Apandisit vakasında "apendiks", "apandisit", "PAS skoru 8" yok;
   USG bulgusu ham verilir ("sağ alt kadranda 9.5 mm, kompresyonla basılmayan kör uçlu tübüler yapı...").
   - `new_finding`: yalnızca HAM objektif bulgu (vital, muayene, lab değeri, görüntüleme tarifi). Parantez içi yorum
     ("(Krup skoru 1 – hafif)", "(apandisit ile uyumlu)", "Centor 5 puan") YOK.
   - `explanation`: mantığı patofizyoloji/yaklaşım düzeyinde anlat ("lokalize yüzeyel lezyonlarda sistemik tetkik
     yönetimi değiştirmez") ama tanıyı söyleme.
   - Seçeneklerde parantezli ipucu ("(SSSS dışlamak için)", "(mastoidit açısından)", "(torsiyonu ekarte etmek için)") YOK.
   - `final_diagnosis` alanı ve tanı adımı/sonrası adımlar tanıyı serbestçe içerebilir.
   - `complaint` ve `history` de tanıyı söylememeli (zaten çoğu söylemiyor; kontrol et). `stage_title`'larda
     "Sarı Alana devir" gibi ifadeler Y17–Y20'de 1. adımda tanı vermiyorsa kalabilir ama sonucu önceden söylemesin
     (örn. 1. adım başlığı "Yeşil Alanda Değerlendirme ve Alan Kararı" olsun, "...ve Sarı Alana Devir" değil).
4. **Çeldiriciler gerçekçi olmalı.** Absürt/malpraktis karikatürü (hiç muayene etmeden BT, 14 gün meropenem, krutu kanatarak
   koparmak, nöroloji servisine yatırmak, ameliyathaneye indirmek) YASAK. Her yanlış seçenek, gerçek acil serviste iyi niyetli
   bir hekimin yapabileceği, savunulabilir görünen ama kılavuza göre eksik/hatalı bir yaklaşım olmalı:
   - **Muayene/triyaj adımı:** Hepsi makul muayene yaklaşımları; doğru olan kritik bir manevrayı/kırmızı bayrağı içerir,
     yanlışlar ya bir kilit noktayı atlar, ya erken hedefe yönelik tedavi/tetkike sıçrar, ya gereksiz alan değişikliği yapar,
     ya da yanlış önceliklendirir. (Y17–Y20 dışında Sarı Alana devretmek makul görünen bir çeldirici olabilir.)
   - **Tetkik adımı:** Gerçek ikilemler: hiç tetkik vs hızlı antijen/sürüntü vs hemogram+CRP vs idrar tetkiki vs USG vs
     grafi vs kültür; doğru olan kılavuza en uygun olan. Yanlış seçeneklerin `scenario_update`'i istenen tetkikin
     gerçekçi (çoğu zaman sınırda/yanıltıcı) sonucunu verip neden yönetimi değiştirmediğini/yanılttığını göstersin.
   - **Tanı adımı:** 4 yakın ayırıcı tanı, aynı başvuru tablosuna gerçekten uyabilecek olanlar (örn. non-büllöz impetigo /
     büllöz impetigo / sekonder enfekte perioral dermatit-egzama / rekürren herpes labialis). Absürtler (variola, ITP vb.
     bağlamsızsa) yok. Tanı seçenekleri kısa olabilir (2–8 kelime); bu adımda uzunluk kuralı 2–12 kelime, dengeli.
   - **Tedavi/izlem adımı:** İlaç seçimi, doz (mg/kg), yol, süre, izlem süresi, izolasyon/okula dönüş, yatış-taburculuk
     nüansları. Örn: amoksisilin 40-45 vs 80-90 mg/kg/gün; 5 vs 10 gün; deksametazon 0.15 vs 0.6 mg/kg ve gözlem süresi;
     topikal mupirosin vs oral sefaleksin vs topikal + oral; adrenalin sonrası 1 saat vs 4-6 saat vs 12-24 saat gözlem.
     Yanlışlar "neredeyse doğru" olsun.
5. **Klinik doğruluk:** Güncel kılavuzlar (AAP 2013 AOM, IDSA, GINA 2024, NICE, ESPGHAN 2014/güncel, WAO/EAACI anafilaksi,
   ISPAD 2022 DKA, AHA/PALS, NICE sepsis, Rumack-Matthew, AAP bronşiolit 2014/2023, Westley vb.). Dozlar doğru olsun.
   Türkiye pratiğinde ulaşılabilir ilaçlar tercih edilsin.
6. **Travma vakası yok.** Mevcut vaka konusunu/tanısını, yaş/cinsiyeti, kategoriyi ve Y17–Y20'nin Sarı Alana devir yapısını
   (1. adım doğru seçeneğinde `'triggers_yellow_transfer': True`) KORU. Adım sayısı mevcutla aynı kalabilir (genelde 4).
   Gerekirse history'yi zenginleştirebilirsin ama tanıyı söyletme.
7. Her yanlış seçenekte `scenario_update` (seçime göre senaryoda ne oldu — somut sonuç/değer) ve `teaching_point`
   (neden hatalı, doğrusu ne) dolu ve öğretici olsun. Bunlar tanı adımından önceyse tanı adı içermesin; doğru yaklaşımı
   tarif etsin ("bu bulgularda kılavuz ... önerir").
8. Dil: Türkçe, akıcı tıbbi dil. Python dosyası `# -*- coding: utf-8 -*-` ile başlasın, geçerli Python olsun
   (çift tırnak/tek tırnak kaçışlarına dikkat; tercihen string'lerde çift tırnak kullan, içerdeki alıntılar için tek tırnak).

## Çıktı
`cases_v2/<dosya>.py` içinde `CASES = [ ... ]` listesi. Sonra şunu çalıştır ve tüm hataları düzelt:
`python cases_v2/dogrula.py cases_v2/<dosya>.py`
