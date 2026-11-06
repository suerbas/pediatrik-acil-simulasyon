# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Sarı Alan Vakaları (Part 6: Y51 - Y60)
Odak: Bulantı, Kusma, Karın Ağrısı, İshal (GİS Acilleri - Sarı Alan Monitörizasyon & Stabilizasyon)
Kılavuzlar: ESPGHAN, AAP, PALS, NASPGHAN, APSA (Pediatric Surgery)
"""

YELLOW_CASES_PART6 = [{'id': 'Y51',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '5 Yaşında',
  'gender': 'Kız',
  'complaint': 'Kramp tarzında karın ağrısı, karında şişlik, yeşil kusma ve 24 saattir gaz-dışkı çıkaramama',
  'history': "Ailesi anlatıyor: 'Bir yıl önce patlamış apandisit nedeniyle açık ameliyat oldu. Dün akşam aralıklı "
             'kramp şeklinde karın ağrısı başladı, bu sabah koyu yeşil kusmaya başladı. Bir yudum su bile içse '
             "kusuyor. Bir gündür ne gaz ne kaka çıkardı, karnı davul gibi şişti.' Ateşi 37.5°C. Tartı: 19 kg.",
  'final_diagnosis': 'Adezyona Bağlı İnce Bağırsak Obstrüksiyonu (Strangülasyon Bulgusu Olmayan)',
  'disposition': 'Sarı Alanda Nazogastrik Dekompresyon, İntravenöz Sıvı-Elektrolit Düzeltmesi ve Çocuk Cerrahisiyle '
                 'Seri Muayene İçin Yatış',
  'case_pearl': 'Geçirilmiş karın ameliyatı sonrası kolik ağrı, safralı kusma, distansiyon ve gaz-dışkı çıkaramama '
                'yapışıklığa bağlı ince bağırsak tıkanıklığını düşündürür; çocuklarda en sık perfore apandisit sonrası '
                'görülür. Strangülasyon bulgusu (sürekli ağrı, ateş, taşikardi, peritonit, lökositoz, laktat artışı) '
                'yoksa nazogastrik dekompresyon, sıvı-elektrolit düzeltmesi ve seri muayene ile başlanır; suda çözünür '
                'kontrast hem tanısal hem tedavi edicidir. Klinik kötüleşme veya 24-48 saatte düzelmeme cerrahi '
                'gerektirir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Dekompresyon',
             'question': 'Geçirilmiş karın ameliyatı olan, safralı kusan ve karnı şiş bu 5 yaşındaki çocukta ilk '
                         'yaklaşımınız nedir?',
             'options': [{'text': 'Tıkanıklığı aşmak için metoklopramid ve laktüloz başlamak, çocuğu sıvı diyetle '
                                  'gözlem odasında izlemek',
                          'is_correct': False,
                          'scenario_update': 'Prokinetik sonrası kramp ağrıları arttı ve kusma sürdü.',
                          'teaching_point': 'Mekanik tıkanıklıkta prokinetik ve laksatifler kontrendikedir.'},
                         {'text': 'Kusmayı azaltmak için intravenöz ondansetron verip yarım saat sonra oral sıvı '
                                  'denemesi yapmak ve ağrı kesici olarak oral ibuprofen önermek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk sıvıyı hemen safralı kustu; aspirasyon riski oluştu ve sıvı açığı '
                                             'derinleşti.',
                          'teaching_point': 'Safralı kusması olan çocukta oral deneme yapılmaz; antiemetik tıkanıklığı '
                                            'maskeleyebilir.'},
                         {'text': 'Oral alımı kesip nazogastrik sondayla mideyi boşaltmak, damar yolu açıp sıvı ve '
                                  'analjezi vermek, iskemi bulgularını ve fıtık deliklerini değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Dekompresyon kusmayı ve aspirasyon riskini azaltır; sıvı kaybı izotonik '
                                         'sıvıyla düzeltilir. Sürekli ağrı, ateş, taşikardi ve peritoneal bulgular '
                                         'bağırsak iskemisini düşündürür; inguinal fıtık da tıkanıklık nedeni '
                                         'olabileceğinden muayene edilir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.5°C, KTA 134/dk, SS 28/dk, TA 94/58 mmHg, KDZ 2.5 '
                                         'sn. Sağ alt kadranda eski insizyon skarı. Karın belirgin distandü, timpanik; '
                                         'metalik tınlamalı bağırsak sesleri, yaygın hafif hassasiyet, defans ve '
                                         'rebound yok. Fıtık delikleri boş. Nazogastrik sondadan 180 mL safralı sıvı '
                                         'geldi. 20 mL/kg serum fizyolojik sonrası KTA 112/dk.'},
                         {'text': 'Uzun süredir dışkılamadığı için kabızlığa bağlı ağrı olduğunu düşünüp fosfatlı '
                                  'lavman uygulamak ve dışkılama sonrası ağrının azalmasını beklemek',
                          'is_correct': False,
                          'scenario_update': 'Lavman sonrası çok az dışkı geldi; kusma ve distansiyon sürdü, '
                                             'dekompresyon gecikti.',
                          'teaching_point': 'Safralı kusma ve distansiyonla birlikte gaz-dışkı çıkaramama kabızlıkla '
                                            'açıklanmaz; lavman bu tabloyu düzeltmez.'}]},
            {'stage_title': 'Laboratuvar ve Görüntüleme',
             'question': 'Dekompresyon ve sıvı tedavisi başlanan bu çocukta hangi tetkikler öncelikli olarak '
                         'istenmelidir?',
             'options': [{'text': 'Tam kan sayımı, elektrolitler, BUN-kreatinin, kan gazı ve laktat istemek; ayakta ve '
                                  'yatarak direkt batın grafisi çekmek',
                          'is_correct': True,
                          'explanation': 'Kusmayla oluşan elektrolit kayıpları ve böbrek fonksiyonu sıvı tedavisini '
                                         'belirler. Lökositoz, asidoz ve laktat artışı iskemiyi düşündürür. Direkt '
                                         'grafi tıkanıklığın düzeyini ve serbest havayı gösterir.',
                          'new_finding': 'Lökosit 12.800/mm³, Na 134, K 3.2, Cl 96 mEq/L, BUN 44 mg/dL, kreatinin 0.5 '
                                         'mg/dL, pH 7.38, laktat 1.4 mmol/L. Ayakta direkt grafi: santral yerleşimli '
                                         'dilate ince bağırsak ansları ve merdiven basamağı şeklinde çok sayıda '
                                         'hava-sıvı seviyesi; kolon ve rektumda gaz yok, diyafram altında serbest hava '
                                         'yok.',
                          'image': 'assets/images/adbg_air_fluid.png',
                          'image_caption': 'Ayakta Direkt Batın Grafisi'},
                         {'text': 'Kolon kaynaklı bir sorunu dışlamak için acil kolonoskopi planlamak ve barsak '
                                  'temizliği için oral solüsyon vermek',
                          'is_correct': False,
                          'scenario_update': 'Oral solüsyon verilen çocuk masif kustu ve distansiyon arttı.',
                          'teaching_point': 'Tıkanıklık bulguları olan çocukta oral barsak hazırlığı kontrendikedir.'},
                         {'text': 'Tıkanıklık yerini göstermek için oral baryumlu pasaj grafisi çekmek ve kontrast '
                                  'kolona geçene kadar seri grafilerle izlemek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk baryumu kustu; tıkanıklık proksimalinde biriken baryum olası '
                                             'cerrahiyi zorlaştıracaktı.',
                          'teaching_point': 'Tıkanıklıkta baryum kullanılmaz; gerekirse suda çözünür kontrast tercih '
                                            'edilir.'},
                         {'text': 'Yalnızca tam kan sayımı istemek, lökosit normal sınırdaysa enfeksiyon olmadığını '
                                  'kabul edip görüntüleme yapmadan çocuğu servise göndermek',
                          'is_correct': False,
                          'scenario_update': 'Elektrolit bozukluğu ve tıkanıklığın düzeyi değerlendirilmeden çocuk '
                                             'servise gönderildi.',
                          'teaching_point': 'Tıkanıklık şüphesinde görüntüleme ve elektrolit değerlendirmesi '
                                            'zorunludur.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Geçirilmiş laparotomi sonrası kolik ağrı, safralı kusma, distansiyon, gaz-dışkı çıkaramama '
                         've grafide merdiven basamağı hava-sıvı seviyeleri olan bu çocukta tanı nedir?',
             'options': [{'text': 'Adezyona bağlı ince bağırsak obstrüksiyonu',
                          'is_correct': True,
                          'explanation': 'Geçirilmiş perfore apandisit ameliyatı sonrası gelişen yapışıklıklar ince '
                                         'bağırsağı sıkıştırarak mekanik tıkanıklık yapar; ateş, peritonit ve laktat '
                                         'artışının olmaması strangülasyon lehine değildir.',
                          'new_finding': 'Tanı: Adezyona Bağlı İnce Bağırsak Obstrüksiyonu (strangülasyon bulgusu '
                                         'yok).'},
                         {'text': 'Hipokalemiye bağlı paralitik ileus',
                          'is_correct': False,
                          'scenario_update': 'Potasyum hafif düşük; kolik ağrı, metalik bağırsak sesleri ve kolonda '
                                             'gaz yokluğu mekanik bir nedeni gösteriyor.',
                          'teaching_point': 'Paralitik ileusta bağırsak sesleri azalır ve gaz kolona kadar yaygındır.'},
                         {'text': 'Sigmoid volvulusu',
                          'is_correct': False,
                          'scenario_update': 'Grafide kolon dilatasyonu yok; dilatasyon santral ince bağırsakta.',
                          'teaching_point': 'Sigmoid volvulusu çocuklarda nadirdir ve dev kolon ansı görüntüsü verir.'},
                         {'text': 'Akut viral gastroenterit',
                          'is_correct': False,
                          'scenario_update': 'İshal yok, gaz-dışkı çıkışı durmuş ve grafide tıkanıklık bulgusu var.',
                          'teaching_point': 'Gastroenteritte kusma genellikle safrasızdır ve ishal eşlik eder.'}]},
            {'stage_title': 'Tedavi ve İzlem',
             'question': 'Strangülasyon bulgusu olmayan bu çocuğun tedavi planı nasıl olmalıdır?',
             'options': [{'text': 'Tüm yapışıklık tıkanıklıklarının cerrahi gerektirdiğini düşünüp çocuğu hemen '
                                  'laparotomiye almak ve yapışıklıkları tamamen açmak',
                          'is_correct': False,
                          'scenario_update': 'Konservatif tedaviyle düzelebilecek tablo için erken cerrahi yapıldı; '
                                             'yeni yapışıklık riski arttı.',
                          'teaching_point': 'Strangülasyon bulgusu yoksa önce konservatif tedavi denenir.'},
                         {'text': 'Bakteriyel translokasyonu önlemek için geniş spektrumlu antibiyotik başlamak ve '
                                  'tıkanıklık çözülene kadar bir hafta total parenteral beslenmeyle izlemek',
                          'is_correct': False,
                          'scenario_update': 'Rutin antibiyotik ve uzun süreli bekleme gereksizdi; çocuk santral '
                                             'kateter komplikasyon riskiyle karşılaştı.',
                          'teaching_point': 'Basit tıkanıklıkta rutin antibiyotik önerilmez; 48 saatte düzelmeyen '
                                            'tablo cerrahiyle değerlendirilir.'},
                         {'text': 'Nazogastrik sondayı çekip sıvı diyete başlamak, gaz çıkışı olursa aynı gün taburcu '
                                  'etmek ve ağrı için oral analjezik önermek',
                          'is_correct': False,
                          'scenario_update': 'Erken beslenme sonrası yeniden safralı kusma başladı; çocuk tekrar '
                                             'başvurdu.',
                          'teaching_point': 'Beslenme tıkanıklığın çözüldüğüne dair klinik ve radyolojik kanıttan '
                                            'sonra başlanır.'},
                         {'text': 'Nazogastrik dekompresyonu, potasyumlu izotonik sıvıyı ve analjeziyi sürdürmek, '
                                  'çocuk cerrahisiyle seri muayene ve gerekirse suda çözünür kontrast çalışması '
                                  'planlamak',
                          'is_correct': True,
                          'explanation': 'Strangülasyon bulgusu olmayan yapışıklık tıkanıklıklarının çoğu konservatif '
                                         'tedaviyle çözülür. Suda çözünür kontrastın 24 saatte kolona geçmesi '
                                         'düzelmeyi öngörür. Kötüleşme veya 24-48 saatte yanıt alınamaması cerrahi '
                                         'gerektirir.',
                          'new_finding': 'Konservatif tedavi sürdürüldü; nazogastrik sondadan suda çözünür kontrast '
                                         'verildi. 18. saatte kontrast kolonda görüldü, çocuk gaz çıkardı. Sonda '
                                         'çekildi, beslenme başlandı ve dördüncü gün taburcu edildi.'}]}]},
 {'id': 'Y52',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '8 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Antibiyotik tedavisi sonrası başlayan şiddetli kanlı-mukuslu ishal, yüksek ateş ve karında şişlik',
  'history': "Ailesi anlatıyor: 'On gün önce sinüzit nedeniyle önce amoksisilin-klavulanat, sonra sefiksim kullandı. "
             'İlaçlar bittikten üç gün sonra günde 10-12 kez çok kötü kokulu, mukuslu, kanlı ishal başladı. Karın '
             "ağrısı çok şiddetli, ateşi 39.1°C'ye çıktı, son 12 saatte karnı belirgin şişti.' Yakın zamanda seyahat "
             'veya çiğ gıda öyküsü yok. Tartı: 26 kg.',
  'final_diagnosis': 'Ağır Clostridioides difficile Koliti (Psödomembranöz Kolit)',
  'disposition': 'Sarı Alanda Temas İzolasyonu, Gereksiz Antibiyotiklerin Kesilmesi, Oral Vankomisin ve Toksik '
                 'Megakolon İzlemi ile Yatış',
  'case_pearl': 'Antibiyotik kullanımı sırasında veya sonrasındaki 8-12 hafta içinde başlayan ishalde bu etken '
                'düşünülmelidir. Test yalnızca şekilsiz dışkıda yapılır; 1 yaş altında kolonizasyon sık olduğu için '
                'test önerilmez. Lökositoz >15.000/mm³, kreatinin artışı ve hipoalbüminemi ağır hastalığı, '
                'hipotansiyon, ileus veya megakolon fulminan hastalığı gösterir. Tedavide oral vankomisin (veya '
                'fidaksomisin) kullanılır; fulminan olguda intravenöz metronidazol eklenir. Sporlar alkole dirençli '
                'olduğundan el hijyeni su ve sabunla yapılır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Toksik Tablo',
             'question': 'Antibiyotik sonrası kanlı ishal, yüksek ateş ve karın şişliği olan bu çocukta ilk '
                         'yaklaşımınız nedir?',
             'options': [{'text': 'Hemodinamiyi, hidrasyonu ve toksik görünümü değerlendirmek; karın distansiyonu ve '
                                  'periton irritasyonunu aramak, damar yolu açıp temas izolasyonu başlatmak',
                          'is_correct': True,
                          'explanation': 'Toksik görünüm, distansiyon ve periton bulguları megakolon veya perforasyon '
                                         'gibi fulminan seyri düşündürür. Hastane içi bulaşı önlemek için temas '
                                         'izolasyonu tanı konmadan başlanır.',
                          'new_finding': 'Vital Bulgular: Ateş 38.9°C, KTA 128/dk, SS 24/dk, TA 102/62 mmHg, SpO2 %98, '
                                         'KDZ 2.5 sn. Toksik ve bitkin görünüyor. Karın distandü, timpanik, kolon '
                                         'trasesi boyunca yaygın hassasiyet ve istemli defans; belirgin rebound yok. '
                                         'Bezde kötü kokulu, mukuslu, kanlı sulu dışkı. Temas izolasyonu başlandı, '
                                         'damar yolu açıldı.'},
                         {'text': 'Sık dışkılamayı azaltmak için oral loperamid başlamak, oral rehidratasyon solüsyonu '
                                  'önermek ve dışkı sayısı azalırsa çocuğu evde izleme almak',
                          'is_correct': False,
                          'scenario_update': 'Loperamid sonrası dışkı sayısı azaldı ancak karın daha da gerildi ve '
                                             'ateş yükseldi.',
                          'teaching_point': 'Kanlı ve toksik kolitte antimotilite ajanlar megakolon riskini artırır.'},
                         {'text': 'Sinüzit tedavisinin yetersiz kaldığını düşünüp intravenöz seftriakson başlamak ve '
                                  'ishali ilaç yan etkisi olarak kabul etmek',
                          'is_correct': False,
                          'scenario_update': 'Yeni geniş spektrumlu antibiyotik ishali daha da ağırlaştırdı.',
                          'teaching_point': 'Gereksiz antibiyotikler kesilmeli; yeni antibiyotik ancak spesifik '
                                            'endikasyonla verilmelidir.'},
                         {'text': 'Kanlı ishal nedeniyle hemen ampirik siprofloksasin başlamak ve izolasyon '
                                  'önlemlerini dışkı kültürü sonucuna göre planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ampirik kinolon tabloyu düzeltmedi; izolasyon gecikince oda arkadaşı '
                                             'çocukta da ishal başladı.',
                          'teaching_point': 'Temas izolasyonu şüphe anında başlanır; bu tabloda ampirik kinolon '
                                            'yararsızdır.'}]},
            {'stage_title': 'Laboratuvar ve Görüntüleme',
             'question': 'Toksik görünümlü, karnı distandü bu çocukta hangi tetkikler öncelikli olarak istenmelidir?',
             'options': [{'text': 'Hemogram, CRP, kreatinin, albümin ve elektrolitler istemek; şekilsiz dışkıda GDH '
                                  'antijeni ve toksin testi yapmak, direkt batın grafisi çekmek',
                          'is_correct': True,
                          'explanation': 'Lökosit, kreatinin ve albümin hastalık şiddetini belirler. İki basamaklı '
                                         'dışkı testi (GDH ve toksin) tanıyı doğrular. Direkt grafi kolon '
                                         'dilatasyonunu ve perforasyonu gösterir.',
                          'new_finding': 'Lökosit 24.800/mm³ (%86 nötrofil), CRP 94 mg/L, albümin 2.6 g/dL, kreatinin '
                                         '0.7 mg/dL, Na 133 mEq/L. Dışkıda GDH antijeni ve toksin A/B pozitif; dışkı '
                                         'kültüründe Salmonella, Shigella ve Campylobacter üremedi. Direkt grafi: '
                                         'transvers kolon 5.2 cm genişlemiş, serbest hava yok.'},
                         {'text': 'Şiddetli karın ağrısı nedeniyle mezenterik iskemiyi dışlamak için acil BT '
                                  'anjiyografi çekmek ve böbrek fonksiyonlarını kontrast sonrası değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'BT kolit bulgularını gösterdi ancak dışkı testleri ve temel laboratuvar '
                                             'gecikti.',
                          'teaching_point': 'BT seçilmiş olgularda komplikasyon değerlendirmesi için kullanılır; ilk '
                                            'basamak değildir.'},
                         {'text': 'Kanlı ishalde amip ve diğer parazitleri dışlamak için üç ayrı gün dışkı örneği '
                                  'toplamak, sonuçlar gelene kadar tedaviyi ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Örnekler toplanırken çocuğun karnı daha da gerildi; asıl etken '
                                             'araştırılmadı.',
                          'teaching_point': 'Antibiyotik sonrası kanlı ishalde öncelikli olarak toksijenik bakteri '
                                            'araştırılmalıdır.'},
                         {'text': 'Mukozayı doğrudan görmek ve biyopsi almak için aynı gün sedasyonla tam kolonoskopi '
                                  'planlamak ve dışkı tetkiklerini sonrasına bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Gastroenteroloji, distandü ve toksik kolitte kolonoskopinin perforasyon '
                                             'riski taşıdığını belirterek işlemi reddetti.',
                          'teaching_point': 'Ağır kolitte tam kolonoskopi perforasyon riski nedeniyle kaçınılır; tanı '
                                            'dışkı testleriyle konur.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Antibiyotik sonrası kanlı ishal, ateş, belirgin lökositoz, hipoalbüminemi, kolon dilatasyonu '
                         've dışkıda GDH-toksin pozitifliği olan bu çocukta tanı nedir?',
             'options': [{'text': 'Shigella dizanterisi',
                          'is_correct': False,
                          'scenario_update': 'Dışkı kültürü negatif ve tablo antibiyotik sonrası gelişti.',
                          'teaching_point': 'Shigella dizanterisi salgın veya temas öyküsüyle birlikte kültürle '
                                            'doğrulanır.'},
                         {'text': 'Ülseratif kolit atağı',
                          'is_correct': False,
                          'scenario_update': 'Öncesinde kronik bağırsak yakınması yok; tablo antibiyotik sonrası '
                                             'başladı ve toksin pozitif.',
                          'teaching_point': 'İnflamatuvar bağırsak hastalığında da bu enfeksiyon gelişebilir; ancak '
                                            'öykü ve toksin pozitifliği burada enfeksiyonu gösteriyor.'},
                         {'text': 'Salmonella enterokoliti',
                          'is_correct': False,
                          'scenario_update': 'Dışkı kültürü negatif, çiğ gıda öyküsü yok ve toksin pozitif.',
                          'teaching_point': 'Salmonella enteritinde gıda öyküsü ve kültür pozitifliği beklenir.'},
                         {'text': 'Ağır Clostridioides difficile koliti',
                          'is_correct': True,
                          'explanation': 'Antibiyotik maruziyeti, kanlı ishal, lökosit >15.000/mm³, hipoalbüminemi, '
                                         'kolon dilatasyonu ve toksin pozitifliği ağır psödomembranöz koliti doğrular; '
                                         'megakolon gelişimi açısından yakın izlem gerekir.',
                          'new_finding': 'Tanı: Ağır Clostridioides difficile Koliti (psödomembranöz kolit).'}]},
            {'stage_title': 'Tedavi ve İzlem',
             'question': 'Bu çocuğun tedavi planı hangisidir?',
             'options': [{'text': 'Ağır tabloda kolona yeterli düzeyde ulaşacağını düşünerek vankomisini intravenöz '
                                  'yoldan başlamak ve ateş düşünce oral metronidazole geçerek tedaviyi tamamlamak',
                          'is_correct': False,
                          'scenario_update': 'İntravenöz vankomisin kolon lümenine ulaşmadı; ateş ve ishal sürdü.',
                          'teaching_point': 'Bu enfeksiyonda vankomisin yalnızca oral veya rektal yoldan etkilidir.'},
                         {'text': 'Diğer antibiyotikleri kesmek, oral vankomisin başlamak, sıvı-elektrolit desteği '
                                  'vermek, cerrahiyi bilgilendirip seri grafiyle izlemek ve su-sabunla el hijyenini '
                                  'anlatmak',
                          'is_correct': True,
                          'explanation': 'Ağır hastalıkta ilk seçenek oral vankomisin 10 mg/kg dozunda günde dört kez '
                                         '(maks 125 mg) 10 gündür; fulminan tabloda doz artırılır ve intravenöz '
                                         'metronidazol eklenir. Megakolon ve perforasyon açısından cerrahi '
                                         'bilgilendirilir. Sporlar alkole dirençlidir.',
                          'new_finding': 'Oral vankomisin ve sıvı tedavisi başlandı; cerrahi ekip bilgilendirildi. 72. '
                                         "saatte ateş düştü, dışkı sayısı azaldı ve kontrol grafide kolon çapı 4 cm'ye "
                                         'geriledi. Tedavi 10 güne tamamlandı.'},
                         {'text': 'Antibiyotik kullanmadan yüksek doz probiyotik başlamak, ishal kendiliğinden geçene '
                                  'kadar sıvı desteğiyle izlemek',
                          'is_correct': False,
                          'scenario_update': "Tedavisiz izlemde kolon çapı 6.5 cm'ye ulaştı ve fulminan tablo gelişti.",
                          'teaching_point': 'Ağır hastalık mutlaka spesifik antibiyotikle tedavi edilir; probiyotikler '
                                            'tedavi yerine geçmez.'},
                         {'text': 'Oral metronidazol başlamak ve el hijyeni için alkol bazlı dezenfektanın yeterli '
                                  'olduğunu söyleyerek çocuğu ertesi gün taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Ağır hastalıkta yanıt yetersiz kaldı; kardeşte de benzer ishal başladı.',
                          'teaching_point': 'Metronidazol ağır olmayan olgularda seçenektir; ağır hastalıkta oral '
                                            'vankomisin tercih edilir. Alkol sporları etkisizleştirmez.'}]}]},
 {'id': 'Y53',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '11 Yaşında',
  'gender': 'Kız',
  'complaint': 'Göbeğin üst kısmında başlayıp sırta kuşak tarzında yayılan şiddetli karın ağrısı ve inatçı kusma',
  'history': "Kendisi anlatıyor: 'Dün akşam göbeğimin üstünde, sırtıma doğru bıçak gibi saplanan çok şiddetli bir ağrı "
             "başladı. Öne eğilip dizlerimi göğsüme çekince biraz hafifliyor, sırtüstü yatınca dayanamıyorum.' Annesi "
             'beş kez safrasız kustuğunu söylüyor. İki gün önce bir doğum günü partisinde çok yağlı yemek yemiş. '
             'Travma, ilaç kullanımı ve ailede benzer hastalık yok. Tartı: 38 kg.',
  'final_diagnosis': 'Akut Pankreatit (Ödematöz İnterstisyel)',
  'disposition': 'Sarı Alanda Hedefe Yönelik Sıvı Tedavisi, İntravenöz Analjezi ve Erken Enteral Beslenme Planıyla '
                 'Pediatri Servisine Yatış',
  'case_pearl': 'INSPPIRE kriterlerine göre tanı için şu üç bulgudan ikisi yeterlidir: uyumlu karın ağrısı, lipaz veya '
                'amilazın normalin üst sınırının en az 3 katı olması ve görüntüleme bulgusu. Çocukta en sık nedenler '
                'safra yolu hastalığı, ilaçlar, travma, sistemik hastalıklar ve genetik yatkınlıktır. Tedavinin temeli '
                'hedefe yönelik sıvı (tercihen Ringer laktat), yeterli analjezi (gerekirse opioid) ve ilk 48-72 saatte '
                'enteral beslenmedir. Profilaktik antibiyotik önerilmez; erken kontrastlı BT rutin değildir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Analjezi',
             'question': 'Sırta yayılan şiddetli epigastrik ağrısı ve inatçı kusması olan bu 11 yaşındaki kızda ilk '
                         'yaklaşımınız nedir?',
             'options': [{'text': 'Opioidlerin safra yolu spazmı yapacağını düşünerek analjezi vermemek ve ağrının '
                                  'seyrini izlemek için çocuğu aç bekletmek',
                          'is_correct': False,
                          'scenario_update': 'Analjezi verilmeyen çocuk saatlerce şiddetli ağrı çekti; muayene '
                                             'güvenilir yapılamadı.',
                          'teaching_point': 'Opioidlerin bu tabloyu kötüleştirdiğine dair kanıt yoktur; yeterli '
                                            'analjezi verilmelidir.'},
                         {'text': 'Ağrıyı psikojenik kabul edip çocuğu sakinleştirmek için oral benzodiazepin vermek '
                                  've aileye stres yönetimi önermek',
                          'is_correct': False,
                          'scenario_update': 'Sedasyon sonrası çocuk uykuya meyilli oldu; kusma ve ağrı sürdü.',
                          'teaching_point': 'Organik nedenler dışlanmadan karın ağrısı psikojenik kabul edilmez.'},
                         {'text': 'Vital bulgular ve hidrasyonu değerlendirip damar yolu açmak, intravenöz analjezi '
                                  'vermek; karında hassasiyet, defans, sarılık ve böğürde-göbekte morarma bulgularını '
                                  'aramak',
                          'is_correct': True,
                          'explanation': 'Şiddetli ağrı ve kusma sıvı kaybına yol açar; erken analjezi ve sıvı '
                                         'tedavinin temelidir. Sarılık safra yolu tıkanıklığını, böğür ve göbek '
                                         'çevresinde morarma hemorajik ağır tabloyu düşündürür.',
                          'new_finding': 'Vital Bulgular: Ateş 37.7°C, KTA 122/dk, SS 24/dk, TA 108/68 mmHg, SpO2 %99, '
                                         'KDZ 2.5 sn. Öne eğilmiş oturuyor. Epigastriumda belirgin hassasiyet ve '
                                         'istemsiz defans; yaygın rebound yok. Bağırsak sesleri azalmış. Sarılık ve '
                                         "ciltte morarma yok. İntravenöz morfin sonrası ağrı skoru 9'dan 4'e indi."},
                         {'text': 'Yağlı yemek öyküsü nedeniyle ağrıyı akut gastrite bağlayıp antiasit süspansiyon ve '
                                  'oral proton pompası inhibitörü vermek, ağrı azalırsa çocuğu taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Antiasit sonrası ağrı değişmedi ve çocuk yeniden kustu; tanı gecikti.',
                          'teaching_point': 'Sırta yayılan, kusmayla seyreden şiddetli epigastrik ağrı basit gastritle '
                                            'açıklanmamalıdır.'}]},
            {'stage_title': 'Laboratuvar ve Görüntüleme',
             'question': 'Analjezi ve sıvı başlanan bu çocukta hangi tetkikler öncelikli olarak istenmelidir?',
             'options': [{'text': 'Maliyeti azaltmak için yalnızca serum amilazı istemek, değer normalin iki katından '
                                  'düşükse ciddi bir sorunu dışlayıp çocuğu oral beslenmeyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Amilaz erken dönemde normalin iki katı bulundu; lipaz bakılmadan tanı '
                                             'dışlanmak üzereydi.',
                          'teaching_point': 'Amilaz daha az duyarlı ve özgüldür; lipaz tercih edilir.'},
                         {'text': 'Safra yolu taşını dışlamak için acil endoskopik retrograd kolanjiyopankreatografi '
                                  'planlamak ve kan tetkiklerini işlem sonrasına bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Endoskopist, safra yolu tıkanıklığı bulgusu olmadan girişimin endike '
                                             'olmadığını belirtti.',
                          'teaching_point': 'ERCP yalnızca safra yolu tıkanıklığı veya kolanjit varlığında endikedir.'},
                         {'text': 'Ciddi bir komplikasyonu kaçırmamak için ilk saatlerde intravenöz kontrastlı batın '
                                  'bilgisayarlı tomografisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Erken BT nekrozu güvenilir göstermedi; çocuk gereksiz radyasyon ve '
                                             'kontrasta maruz kaldı.',
                          'teaching_point': 'Erken kontrastlı BT rutin değildir; tanı belirsizse veya 72 saat sonra '
                                            'komplikasyon şüphesinde kullanılır.'},
                         {'text': 'Lipaz, amilaz, karaciğer testleri, kalsiyum, trigliserit, glukoz, böbrek '
                                  'fonksiyonları, hemogram ve CRP istemek; batın ultrasonu yapmak',
                          'is_correct': True,
                          'explanation': 'Lipaz duyarlı ve özgül belirteçtir. Kalsiyum, trigliserit ve karaciğer '
                                         'testleri etiyolojiye, BUN ve hemokonsantrasyon şiddete ışık tutar. Ultrason '
                                         'safra taşı ve safra yolu dilatasyonunu radyasyonsuz gösterir.',
                          'new_finding': 'Lipaz 1380 U/L (normalin 23 katı), amilaz 860 U/L, ALT 32 U/L, AST 38 U/L, '
                                         'total bilirubin 0.8 mg/dL, kalsiyum 8.9 mg/dL, trigliserit 110 mg/dL, glukoz '
                                         '128 mg/dL, BUN 18 mg/dL, lökosit 13.400/mm³, CRP 36 mg/L. Ultrason: pankreas '
                                         'gövde ve kuyruğunda ödematöz hipoekoik büyüme, minimal peripankreatik sıvı; '
                                         'safra kesesi ve yolları normal.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Sırta yayılan epigastrik ağrı, lipazın normalin 23 katı olması ve ultrasonda ödematöz '
                         'pankreas görülen bu çocukta tanı nedir?',
             'options': [{'text': 'Akut taşlı kolesistit',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonda safra kesesi ve yolları normal.',
                          'teaching_point': 'Kolesistitte sağ üst kadran ağrısı, Murphy bulgusu ve kese duvarı '
                                            'kalınlaşması görülür.'},
                         {'text': 'Akut ödematöz pankreatit',
                          'is_correct': True,
                          'explanation': 'Tipik ağrı, lipazın normalin üst sınırının 3 katından fazla olması ve '
                                         'görüntüleme bulgusu INSPPIRE kriterlerinin üçünü de karşılar; nekroz bulgusu '
                                         'olmadığından ödematöz interstisyel formdur.',
                          'new_finding': 'Tanı: Akut Pankreatit (ödematöz interstisyel).'},
                         {'text': 'Perfore peptik ülser',
                          'is_correct': False,
                          'scenario_update': 'Yaygın periton irritasyonu ve serbest hava yok; lipaz belirgin yüksek.',
                          'teaching_point': 'Perfore ülserde ani yaygın ağrı ve diyafram altında serbest hava '
                                            'beklenir.'},
                         {'text': 'Diyabetik ketoasidoz',
                          'is_correct': False,
                          'scenario_update': 'Glukoz 128 mg/dL, asidoz ve ketonemi yok.',
                          'teaching_point': 'Karın ağrısı ve kusma metabolik nedenlerle de gelişebilir; kan şekeri ve '
                                            'kan gazı ayırıcı tanıda yardımcıdır.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu çocuğun tedavi planı nasıl olmalıdır?',
             'options': [{'text': 'Ağrı kontrol altına alındığı için sıvı tedavisini kesip çocuğu normal diyetle aynı '
                                  'gün taburcu etmek ve lipaz normale dönene kadar haftalık kontrol önermek',
                          'is_correct': False,
                          'scenario_update': 'Evde ağrı ve kusma yeniden başladı; çocuk dehidrate olarak ertesi gün '
                                             'geri geldi.',
                          'teaching_point': 'Lipaz düzeyi izlem kararını belirlemez; klinik iyileşme ve oral tolerans '
                                            'esastır.'},
                         {'text': 'Pankreası tamamen dinlendirmek için en az bir hafta oral ve nazogastrik alımı '
                                  'kesmek, santral kateterden total parenteral beslenme başlamak ve sıvıyı yalnızca '
                                  'idame hızında vermek',
                          'is_correct': False,
                          'scenario_update': 'Uzun açlık ve santral kateter sonrası kateter ilişkili enfeksiyon '
                                             'gelişti; hastanede kalış uzadı.',
                          'teaching_point': 'Uzun süreli açlık önerilmez; erken enteral beslenme daha güvenlidir.'},
                         {'text': 'Komplikasyonları önlemek için profilaktik imipenem başlamak, enzim salınımını '
                                  'azaltmak amacıyla oktreotid infüzyonu eklemek ve çocuğu en az bir hafta aç tutmak',
                          'is_correct': False,
                          'scenario_update': 'Bu tedaviler seyri değiştirmedi; çocuk gereksiz geniş spektrumlu '
                                             'antibiyotiğe maruz kaldı.',
                          'teaching_point': 'Profilaktik antibiyotik ve oktreotidin çocuklarda yararı '
                                            'gösterilmemiştir.'},
                         {'text': 'Ringer laktatla 1.5-2 kat idame hızında hedefe yönelik sıvı vermek, düzenli '
                                  'analjezi sürdürmek, kusma azalınca ilk 48-72 saatte enteral beslenmeye geçmek ve '
                                  'antibiyotik vermemek',
                          'is_correct': True,
                          'explanation': 'Hedefe yönelik sıvı tedavisi pankreas perfüzyonunu korur. Erken enteral '
                                         'beslenme bağırsak bariyerini destekler ve hastanede kalış süresini kısaltır. '
                                         'Profilaktik antibiyotik enfekte nekroz riskini azaltmaz.',
                          'new_finding': 'Ringer laktat ve morfin sürdürüldü. İkinci gün ağrı azaldı, düşük yağlı '
                                         'diyetle oral beslenme başlandı. Etiyoloji araştırması için poliklinik izlemi '
                                         'planlandı; çocuk beşinci gün taburcu edildi.'}]}]},
 {'id': 'Y54',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '2 Aylık',
  'gender': 'Erkek',
  'complaint': 'Ateş, karında aşırı şişlik, yeşil kusma, patlayıcı kötü kokulu ishal ve solukluk',
  'history': "Ailesi anlatıyor: 'Doğumdan sonra ilk kakasını ancak üçüncü gün yaptı. O günden beri hep kabız, fitille "
             "kaka yapıyordu ve karnı şişkindi. Dün aniden ateşi 38.8°C'ye çıktı, karnı balon gibi şişti. Bugün yeşil "
             "kustu, sonra bezine fışkırır gibi çok kötü kokulu, sulu kaka geldi. Emmiyor, inliyor.' Term doğmuş. "
             'Büyüme yavaş. Tartı: 4.8 kg.',
  'final_diagnosis': 'Hirschsprung Hastalığı İlişkili Enterokolit',
  'disposition': 'Sarı Alanda Sıvı Resüsitasyonu, Nazogastrik Dekompresyon, Geniş Spektrumlu İntravenöz Antibiyotik ve '
                 'Rektal İrrigasyon ile Çocuk Yoğun Bakım ve Cerrahi İzlemi',
  'case_pearl': 'Mekonyumun 48 saatten geç çıkması ve doğumdan beri süren kabızlık, distal kolonda ganglion hücresi '
                'yokluğunu düşündürür. Bu hastalarda gelişen ateş, distansiyon, patlayıcı kötü kokulu ishal ve letarji '
                'hayatı tehdit eden enterokolittir; ölümün en sık nedenidir. Tedavi resüsitasyon, dekompresyon, '
                'ampisilin-gentamisin-metronidazol gibi geniş spektrumlu antibiyotik ve serum fizyolojikle rektal '
                'irrigasyondur. Akut dönemde kontrastlı lavman yapılmaz; tanı sonradan rektal emme biyopsisiyle konur.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Resüsitasyon',
             'question': 'Ateşli, distandü, safralı kusan ve patlayıcı ishali olan bu 2 aylık bebekte ilk yaklaşımınız '
                         'nedir?',
             'options': [{'text': 'Sulu ishal nedeniyle biberonla oral rehidratasyon solüsyonu vermek, ateş için '
                                  'parasetamol önermek ve bebeği acil gözlem odasında iki saat izlemek',
                          'is_correct': False,
                          'scenario_update': "Bebek ORS'yi safralı kustu; gözlem sırasında perfüzyonu belirgin "
                                             'bozuldu.',
                          'teaching_point': 'Safralı kusma, distansiyon ve letarji acil resüsitasyon gerektirir; oral '
                                            'deneme yapılmaz.'},
                         {'text': 'Doğumdan beri süren kabızlık öyküsü nedeniyle karın şişliğini azaltmak için '
                                  'yetişkin dozunda fosfatlı lavman uygulamak ve dışkılama sonrası bebeği yeniden '
                                  'değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Fosfatlı lavman sonrası bebekte ciddi elektrolit bozukluğu gelişti ve '
                                             'tablo ağırlaştı.',
                          'teaching_point': 'Küçük bebekte fosfatlı lavman kontrendikedir; dekompresyon serum '
                                            'fizyolojikle yapılır.'},
                         {'text': 'İshali durdurmak için antimotilite damla başlamak ve karın şişliği için simetikon '
                                  'vermek, aileyi beslenme konusunda bilgilendirip taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Antimotilite ajan sonrası distansiyon arttı; bebek saatler sonra şokta '
                                             'geri getirildi.',
                          'teaching_point': 'Ateşli, distandü bebekte antimotilite ajanlar tehlikelidir.'},
                         {'text': 'Havayolu, solunum ve perfüzyonu değerlendirip damar yolu açmak, izotonik sıvı '
                                  'bolusu vermek, kan şekeri bakmak, oral alımı kesip nazogastrik dekompresyon yapmak',
                          'is_correct': True,
                          'explanation': 'Letarji, taşikardi ve uzamış kapiller dolum sepsis ve şoku düşündürür; hızlı '
                                         'sıvı ve dekompresyon gereklidir. Küçük bebekte hipoglisemi sık görülür.',
                          'new_finding': 'Vital Bulgular: Ateş 38.7°C, KTA 164/dk, SS 46/dk, TA 74/42 mmHg, SpO2 %96, '
                                         'KDZ 3 sn. İniltili, soluk, letarjik. Karın ileri derecede distandü, parlak, '
                                         'venöz dolgunluk belirgin. Rektal muayenede anal kanal dar ve sıkı; parmak '
                                         'çıkarılınca patlayıcı şekilde kötü kokulu gaz ve sıvı dışkı fışkırdı. Kan '
                                         "şekeri 68 mg/dL. 20 mL/kg serum fizyolojik sonrası KDZ 2 sn'ye indi."}]},
            {'stage_title': 'Laboratuvar, Görüntüleme ve Antibiyotik',
             'question': 'Resüsitasyona kısmi yanıt veren bu bebekte sonraki adım nedir?',
             'options': [{'text': 'Altta yatan yapısal nedeni göstermek için acil serviste hemen kontrastlı kolon '
                                  'grafisi çekmek ve antibiyotiği tanı kesinleştikten sonra başlamak',
                          'is_correct': False,
                          'scenario_update': 'Radyolog, akut inflamasyonda kontrastlı lavmanın perforasyon riski '
                                             'taşıdığını belirterek işlemi erteledi; antibiyotik gecikti.',
                          'teaching_point': 'Akut ağır kolitte kontrastlı lavman yapılmaz; antibiyotik geciktirilmez.'},
                         {'text': 'Kan kültürü, hemogram, CRP, kan gazı, laktat ve elektrolitler alıp hemen geniş '
                                  'spektrumlu intravenöz antibiyotik başlamak ve direkt grafi çekmek',
                          'is_correct': True,
                          'explanation': 'Sepsis bulgusu olan bebekte antibiyotik kültür alındıktan sonra '
                                         'geciktirilmez. Anaerop ve gram negatifleri kapsayan ampisilin, gentamisin ve '
                                         'metronidazol uygundur. Direkt grafi dilatasyonu, geçiş noktasını ve '
                                         'perforasyonu gösterir.',
                          'new_finding': 'Lökosit 21.400/mm³ (%20 çomak), CRP 92 mg/L, pH 7.24, laktat 3.8 mmol/L, Na '
                                         '132, K 3.4 mEq/L. Ampisilin, gentamisin ve metronidazol başlandı. Direkt '
                                         'grafi: kolonda yaygın gaz distansiyonu, rektosigmoid bölgede gazın aniden '
                                         'kesilmesi, bağırsak duvarında ödem; serbest hava yok.'},
                         {'text': 'Yalnızca dışkı kültürü ve rotavirüs antijeni göndermek, viral etken olasılığı '
                                  'yüksek olduğu için antibiyotik vermeden sıvı tedavisiyle bebeği izlemek',
                          'is_correct': False,
                          'scenario_update': "Antibiyotiksiz izlemde laktat 5.6 mmol/L'ye yükseldi ve bebek inotrop "
                                             'ihtiyacıyla yoğun bakıma alındı.',
                          'teaching_point': 'Ateşli, toksik ve distandü bebekte bakteriyel translokasyon ve sepsis '
                                            'riski yüksektir.'},
                         {'text': 'Ateşli küçük bebekte tam sepsis değerlendirmesi için önce lomber ponksiyon yapmak '
                                  've işlem tamamlanana kadar antibiyotik başlamamak',
                          'is_correct': False,
                          'scenario_update': 'Lomber ponksiyon hemodinamik instabilite nedeniyle yapılamadı; '
                                             'antibiyotik bir saat gecikti.',
                          'teaching_point': 'Stabil olmayan bebekte lomber ponksiyon ertelenir; antibiyotik beklemeden '
                                            'başlanır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Gecikmiş mekonyum ve doğumdan beri kabızlık öyküsü olan, ateş, distansiyon, patlayıcı kötü '
                         'kokulu ishal ve rektosigmoidde geçiş noktası saptanan bu bebekte tanı nedir?',
             'options': [{'text': 'Hirschsprung ilişkili enterokolit',
                          'is_correct': True,
                          'explanation': 'Gecikmiş mekonyum, kronik kabızlık, rektal muayenede patlayıcı boşalma ve '
                                         'rektosigmoidde geçiş noktası altta yatan aganglionozu; ateş, distansiyon ve '
                                         'kötü kokulu ishal ise hayatı tehdit eden enterokoliti gösterir.',
                          'new_finding': 'Tanı: Hirschsprung Hastalığı İlişkili Enterokolit.'},
                         {'text': 'Salmonella sepsisi',
                          'is_correct': False,
                          'scenario_update': 'Kronik kabızlık, gecikmiş mekonyum ve rektosigmoidde geçiş noktası '
                                             'enfeksiyonla açıklanmaz.',
                          'teaching_point': 'Altta yatan yapısal sorun tekrarlayan ağır tabloların nedenidir ve '
                                            'atlanmamalıdır.'},
                         {'text': 'Nekrotizan enterokolit',
                          'is_correct': False,
                          'scenario_update': 'Term ve 2 aylık bebek; grafide pnömatozis yok ve öykü doğumdan beri '
                                             'süren kabızlığı gösteriyor.',
                          'teaching_point': 'Nekrotizan enterokolit çoğunlukla prematürelerde, ilk haftalarda '
                                            'görülür.'},
                         {'text': 'Malrotasyon ve orta bağırsak volvulusu',
                          'is_correct': False,
                          'scenario_update': 'Distal kolon tutulumu ve kronik kabızlık öyküsü var; proksimal duodenal '
                                             'tıkanıklık bulgusu yok.',
                          'teaching_point': 'Volvulus ani başlangıçlı safralı kusmayla seyreder ve kronik kabızlık '
                                            'öyküsü beklenmez.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu bebeğin acil tedavisi nasıl sürdürülmelidir?',
             'options': [{'text': 'Antibiyotik ve sıvıyı sürdürüp rektal tüple serum fizyolojik irrigasyonu yapmak, '
                                  'dekompresyona devam etmek ve yoğun bakım-cerrahi izlemine almak',
                          'is_correct': True,
                          'explanation': 'Rektal irrigasyon kolonun dekompresyonunu ve bakteri yükünün azalmasını '
                                         'sağlar. Yanıt alınamazsa saptırıcı kolostomi gerekir. Akut dönem sonrasında '
                                         'rektal emme biyopsisiyle tanı doğrulanır ve kesin cerrahi planlanır.',
                          'new_finding': 'Günde iki kez 10-20 mL/kg serum fizyolojikle rektal irrigasyon yapıldı. 48 '
                                         'saatte ateş düştü, distansiyon azaldı. Rektal emme biyopsisinde ganglion '
                                         'hücresi saptanmadı; çocuk cerrahisi düzeltici ameliyat planladı.'},
                         {'text': 'Ateş düşünce intravenöz antibiyotiği oral metronidazole çevirip bebeği evde fitil '
                                  'uygulamasıyla izleme almak',
                          'is_correct': False,
                          'scenario_update': 'Evde distansiyon yeniden arttı; bebek iki gün sonra tekrar enterokolitle '
                                             'başvurdu.',
                          'teaching_point': 'Enterokolit atakları tekrarlayabilir; dekompresyon ve kesin tanı '
                                            'yapılmadan taburculuk uygun değildir.'},
                         {'text': 'Kolonu hızla boşaltmak için yüksek hacimli fosfatlı lavmanları günde birkaç kez '
                                  'tekrarlamak ve ateş düşünce antibiyotiği kesmek',
                          'is_correct': False,
                          'scenario_update': 'Fosfatlı lavmanlar sonrası ciddi hiperfosfatemi ve hipokalsemi gelişti.',
                          'teaching_point': 'İrrigasyon izotonik serum fizyolojikle yapılır; fosfatlı lavman bebekte '
                                            'toksiktir.'},
                         {'text': 'Kesin çözüm için bebeği aynı gün düzeltici ameliyata almak, hasarlı kolon '
                                  'segmentini çıkarıp tek seansta primer anastomoz yapmak',
                          'is_correct': False,
                          'scenario_update': 'Aktif enterokolit ve sepsis sırasında yapılan cerrahi yüksek '
                                             'komplikasyon riski taşıdı; cerrahi ekip ameliyatı erteledi.',
                          'teaching_point': 'Kesin cerrahi akut enterokolit tedavi edildikten sonra planlanır.'}]}]},
 {'id': 'Y55',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '4 Yaşında',
  'gender': 'Kız',
  'complaint': 'Gözlerde ve ciltte sararma, sürekli uyuklama, kusma, diş eti kanaması ve vücutta morluklar',
  'history': "Ailesi anlatıyor: 'Bir hafta önce halsizlik ve bulantı başladı. İki gündür gözlerinin akı ve cildi "
             'sarardı, idrarı çay rengi oldu. Bu sabahtan beri sürekli uyumak istiyor, uyandırınca anlamsız bakıyor, '
             "beni zor tanıyor. Dişlerini fırçalarken diş eti kanadı, bacaklarında kendiliğinden morluklar çıktı.' "
             'Evde parasetamol şurubunu önerilen dozda yalnızca iki kez vermişler. Mantar yeme veya bitkisel ürün '
             'öyküsü yok. Tartı: 16 kg.',
  'final_diagnosis': 'Pediatrik Akut Karaciğer Yetmezliği (Evre 2 Ensefalopati)',
  'disposition': 'Sarı Alanda Hipoglisemi Tedavisi, İntravenöz K Vitamini, Sedatiflerden Kaçınma ve Karaciğer Nakil '
                 'Merkezi Olan Çocuk Yoğun Bakıma Acil Sevk',
  'case_pearl': 'Tanım: bilinen kronik karaciğer hastalığı olmayan çocukta akut karaciğer hasarı ile birlikte K '
                'vitaminine yanıtsız INR ≥1.5 ve ensefalopati, ya da ensefalopati olmasa bile INR ≥2. Çocuklarda '
                'ensefalopati sinsi ve geç bulgu olabilir. Hipoglisemi sıktır ve sık izlenmelidir. Taze donmuş plazma '
                "yalnızca kanama veya girişim için verilir; INR'yi rutin düzeltmek prognostik değerini bozar. "
                'Sedatiflerden kaçınılır. Nakil merkeziyle erken iletişim sağkalımı belirler.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Acil Müdahale',
             'question': 'Sarılık, bilinç bulanıklığı ve kanama bulguları olan bu 4 yaşındaki çocukta ilk yaklaşımınız '
                         'nedir?',
             'options': [{'text': 'Havayolu ve solunumu değerlendirip kapiller kan şekeri bakmak, damar yolu açmak, '
                                  'bilinç düzeyini kaydetmek, kanama bulgularını ve ilaç-toksin maruziyetini '
                                  'sorgulamak',
                          'is_correct': True,
                          'explanation': 'Bilinç bulanıklığında hipoglisemi hızla düzeltilebilir bir nedendir. '
                                         'Başlangıç bilinç düzeyi kötüleşmeyi izlemek için referanstır. Parasetamol, '
                                         'mantar ve bitkisel ürünler etiyolojiyi ve özgül tedaviyi belirler.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 110/dk, SS 22/dk, TA 98/58 mmHg, SpO2 %99. '
                                         'Kapiller kan şekeri 56 mg/dL; 2 mL/kg %10 dekstroz verildi. Derin sarılık. '
                                         'Sesli uyaranla gözlerini açıyor, konfüze, annesini zor tanıyor; asteriksis '
                                         'var. Karaciğer kot kavsini 4 cm geçiyor ve hassas. Bacaklarda ekimozlar, diş '
                                         'etinde sızıntı tarzında kanama. Dalak ele gelmiyor, asit yok.'},
                         {'text': 'Sarılığı basit viral hepatite bağlayıp evde oral sıvı ve yatak istirahati önermek, '
                                  'kanama bulgularını trombositopeniye bağlayıp çocuğu hematoloji polikliniğine '
                                  'yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Hipoglisemi ve bilinç değişikliği atlandı; çocuk konvülziyon geçirerek '
                                             'geri getirildi.',
                          'teaching_point': 'Sarılıkla birlikte bilinç değişikliği ve kanama ağır karaciğer hasarının '
                                            'işaretidir.'},
                         {'text': 'Diş eti kanaması ve ekimozlar nedeniyle tetkik sonuçlarını beklemeden hemen 20 '
                                  'mL/kg taze donmuş plazma ve trombosit süspansiyonu vermek',
                          'is_correct': False,
                          'scenario_update': 'Plazma sonrası INR düzeldi ancak sevk merkezinde prognostik '
                                             'değerlendirme güçleşti; çocukta sıvı yüklenmesi gelişti.',
                          'teaching_point': 'Taze donmuş plazma ciddi kanama veya girişim için verilir; rutin INR '
                                            'düzeltmesi önerilmez.'},
                         {'text': 'Huzursuzluk ve konfüzyon nedeniyle muayeneyi kolaylaştırmak için çocuğu intravenöz '
                                  'midazolam ile sakinleştirmek ve ardından ayrıntılı sistemik muayene yapmak',
                          'is_correct': False,
                          'scenario_update': 'Midazolam sonrası çocuk derin uykuya daldı; nörolojik değerlendirme '
                                             'yapılamadı ve solunumu yüzeyelleşti.',
                          'teaching_point': 'Bilinç bulanıklığı olan karaciğer hastasında sedatifler ensefalopatiyi '
                                            'ağırlaştırır ve izlemi engeller.'}]},
            {'stage_title': 'Laboratuvar ve Sentez Fonksiyonu',
             'question': 'Hipoglisemisi düzeltilen bu çocukta hangi tetkikler öncelikli olarak istenmelidir?',
             'options': [{'text': 'Bilinç değişikliği nedeniyle kafa içi kanamayı dışlamak için önce kontrastsız beyin '
                                  'tomografisi çekmek, ardından karaciğer testlerini istemek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi normal geldi; sentez fonksiyonu ve amonyak bir saat geç '
                                             'değerlendirildi.',
                          'teaching_point': 'Sarılıklı çocukta bilinç değişikliğinin en olası nedeni metabolik olup '
                                            'ilk tetkikler laboratuvardır.'},
                         {'text': 'INR, transaminazlar, bilirubin, glukoz, amonyak, elektrolitler, kan gazı, laktat, '
                                  "kreatinin, kan grubu ve parasetamol düzeyi istemek; INR'yi K vitamini sonrası "
                                  'tekrarlamak',
                          'is_correct': True,
                          'explanation': 'K vitaminine yanıtsız koagülopati sentez yetersizliğini gösterir. Amonyak, '
                                         'laktat ve kreatinin prognozu ve yoğun bakım ihtiyacını belirler. Kan grubu '
                                         'olası nakil ve transfüzyon için, parasetamol düzeyi özgül tedavi için '
                                         'gereklidir.',
                          'new_finding': 'ALT 2460 U/L, AST 3100 U/L, total bilirubin 9.6 mg/dL, direkt 6.8 mg/dL, INR '
                                         '2.6 (10 mg intravenöz K vitamini sonrası 2.5), amonyak 118 µmol/L, laktat '
                                         '3.1 mmol/L, kreatinin 0.4 mg/dL, trombosit 142.000/mm³. Parasetamol düzeyi '
                                         'saptanamayacak kadar düşük. Viral seroloji ve otoimmün belirteçler '
                                         'gönderildi.'},
                         {'text': "Yalnızca bilirubin ve transaminazları isteyip ALT 1000 U/L'nin üzerindeyse "
                                  'ursodeoksikolik asit ve silimarin gibi hepatoprotektif tedavi başlayarak çocuğu '
                                  'servise yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Sentez fonksiyonu bakılmadı; çocuk serviste izlenirken bilinci daha da '
                                             'bozuldu.',
                          'teaching_point': 'Prognozu transaminaz değil INR, bilinç düzeyi ve glukoz belirler.'},
                         {'text': 'Etiyolojiyi kesinleştirmek için aynı gün acil perkütan karaciğer biyopsisi '
                                  'planlamak ve tüm tedavi kararlarını biyopsi sonucuna göre vermek',
                          'is_correct': False,
                          'scenario_update': 'Koagülopatisi olan çocukta biyopsi ciddi kanama riski taşıdığı için '
                                             'işlem iptal edildi.',
                          'teaching_point': 'Koagülopatide perkütan biyopsi kontrendikedir; gerekirse transjuguler yol '
                                            'seçilir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Kronik karaciğer hastalığı olmayan, K vitaminine yanıtsız INR 2.5, konfüzyon ve asteriksis, '
                         'hipoglisemi ve yüksek amonyağı olan bu çocukta tanı nedir?',
             'options': [{'text': 'Ağır seyirli akut viral hepatit',
                          'is_correct': False,
                          'scenario_update': 'Hepatit tablosunun ötesinde, K vitaminine yanıtsız koagülopati ve '
                                             'ensefalopati var.',
                          'teaching_point': 'Sentez yetersizliği ve ensefalopati eklendiğinde tablo yetmezlik olarak '
                                            'tanımlanır.'},
                         {'text': 'Reye sendromu',
                          'is_correct': False,
                          'scenario_update': 'Salisilat maruziyeti yok ve belirgin sarılık var; Reye sendromunda '
                                             'sarılık genellikle yoktur.',
                          'teaching_point': 'Reye sendromu viral enfeksiyon sırasında aspirin kullanımı sonrası '
                                            'ensefalopati ve mikroveziküler yağlanmayla seyreder.'},
                         {'text': 'Akut karaciğer yetmezliği (evre 2 ensefalopati)',
                          'is_correct': True,
                          'explanation': 'Kronik hastalığı olmayan çocukta akut hepatosellüler hasar, K vitaminine '
                                         'yanıtsız INR ≥1.5 ve ensefalopati pediatrik akut karaciğer yetmezliği '
                                         'tanımını karşılar; konfüzyon ve asteriksis evre 2 ensefalopatiyle uyumludur.',
                          'new_finding': 'Tanı: Pediatrik Akut Karaciğer Yetmezliği (evre 2 hepatik ensefalopati).'},
                         {'text': 'Sepsise bağlı yaygın damar içi pıhtılaşma',
                          'is_correct': False,
                          'scenario_update': 'Ateş ve enfeksiyon odağı yok; trombosit sayısı korunmuş ve tablo '
                                             'karaciğer kaynaklı.',
                          'teaching_point': 'Yaygın damar içi pıhtılaşmada trombositopeni ve fibrinojen tüketimi ön '
                                            'plandadır.'}]},
            {'stage_title': 'Tedavi ve Sevk',
             'question': 'Bu çocuğun acil serviste tedavisi ve yönlendirmesi nasıl olmalıdır?',
             'options': [{'text': 'Laktüloz başlamak, proteini tamamen kısıtlamak ve çocuğu genel pediatri servisinde '
                                  'günlük INR takibiyle izleyip kötüleşirse sevk etmek',
                          'is_correct': False,
                          'scenario_update': "Serviste ensefalopati evre 3'e ilerledi; sevk için entübasyon gerekti ve "
                                             'nakil değerlendirmesi gecikti.',
                          'teaching_point': 'Ensefalopatili akut yetmezlikte sevk kötüleşmeyi beklemeden yapılır; '
                                            'protein tamamen kısıtlanmaz.'},
                         {'text': 'Karaciğer hücrelerini korumak için N-asetilsistein ve yüksek doz metilprednizolon '
                                  "başlamak, INR'yi taze donmuş plazmayla normal düzeye getirip sevki ertelemek",
                          'is_correct': False,
                          'scenario_update': 'Plazma ile düzeltilen INR sevk kararını geciktirdi; steroid ve '
                                             'N-asetilsistein seyri değiştirmedi.',
                          'teaching_point': 'Parasetamol dışı nedenlerde N-asetilsisteinin çocukta yararı '
                                            "gösterilmemiştir; INR'nin rutin düzeltilmesi önerilmez."},
                         {'text': 'Ensefalopati nedeniyle hava yolunu güvenceye almak için hemen entübe edip derin '
                                  'sedasyon başlamak ve beyin ödemini önlemek için rutin mannitol infüzyonu vermek',
                          'is_correct': False,
                          'scenario_update': 'Hava yolunu koruyabilen çocuk gereksiz yere entübe edildi; derin '
                                             'sedasyon nörolojik izlemi engelledi.',
                          'teaching_point': 'Entübasyon evre 3-4 ensefalopati veya hava yolu korunamadığında yapılır; '
                                            'mannitol kafa içi basınç artışı bulgusunda verilir.'},
                         {'text': 'Dekstrozlu sıvıyla kan şekerini 70 mg/dL üstünde tutmak, K vitamini vermek, '
                                  'sedatiflerden kaçınmak, başı yükseltmek ve nakil merkezine acil sevk etmek',
                          'is_correct': True,
                          'explanation': 'Hipoglisemi sıktır ve sürekli dekstroz gerekir. Sedatifler ensefalopatiyi '
                                         'maskeler. Baş yükseltme kafa içi basıncı azaltır. Ensefalopatili akut '
                                         'yetmezlikte nakil merkezinin erken katılımı sağkalımı belirler.',
                          'new_finding': '%10 dekstrozlu izotonik sıvı, intravenöz K vitamini ve pantoprazol başlandı; '
                                         'saatlik kan şekeri ve nörolojik izlem yapıldı. Nakil merkeziyle görüşülerek '
                                         'çocuk yoğun bakım ambulansıyla sevk edildi; orada nakil listesine '
                                         'alındı.'}]}]},
 {'id': 'Y56',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '5 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Hızla şiddetlenen sağ alt karın ağrısı, kusma ve ateş',
  'history': "Ailesi anlatıyor: 'Dün göbeğinin altında ağrı başladı, hızla şiddetlendi, üç kez kustu. Ateşi 38.6°C'ye "
             'çıktı. Başka bir hastanede ultrason çektiler, apandisit normal görünüyor deyip ağrı kesiciyle '
             "gönderdiler ama ağrısı daha da arttı.' Daha önce birkaç kez nedeni bulunamayan karın ağrısı atakları "
             'olmuş. Dışkıda kan görülmemiş. Tartı: 19 kg.',
  'final_diagnosis': 'İnflame Meckel Divertikülü (Meckel Divertiküliti)',
  'disposition': 'Sarı Alanda Oral Alımın Kesilmesi, İntravenöz Sıvı-Analjezi-Antibiyotik ve Çocuk Cerrahisiyle Acil '
                 'Laparoskopik Rezeksiyon',
  'case_pearl': 'Normal apendiks görüntülenen ancak lokal periton irritasyonu süren çocukta alternatif nedenler '
                "aranmalıdır. Meckel divertikülü '2 kuralı' ile anılır: toplumun yaklaşık %2'si, ileoçekal valvden "
                'yaklaşık 60 cm proksimalde, çoğunlukla 2 yaş altında semptom verir. Ağrısız masif rektal kanama, '
                'obstrüksiyon (invajinasyon, volvulus) veya divertikülit ile başvurabilir. Divertikülit klinik olarak '
                'apandisite çok benzer; tedavi cerrahi rezeksiyondur. Teknesyum sintigrafisi kanayan olgularda '
                'yararlıdır, inflamasyonda tanısal değeri sınırlıdır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Karın Muayenesi',
             'question': 'Dış merkezde apendiksi normal bildirilen ancak ağrısı artan bu ateşli 5 yaşındaki çocukta '
                         'yaklaşımınız nedir?',
             'options': [{'text': 'Dış merkez ultrasonunda apendiks normal olduğu için cerrahi tabloyu dışlamak, '
                                  'ağrıyı mezenterik lenfadenite bağlayıp oral analjezikle yeniden taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk evde kötüleşti; 12 saat sonra yaygın karın hassasiyeti ve yüksek '
                                             'ateşle geri getirildi.',
                          'teaching_point': 'Normal görüntüleme ile klinik bulgular çeliştiğinde klinik bulgular esas '
                                            'alınır ve yeniden değerlendirme yapılır.'},
                         {'text': 'Ağrının kabızlığa bağlı olabileceğini düşünüp lavman uygulamak, ardından laksatif '
                                  'reçete edip bir gün sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Lavman sonrası ağrı değişmedi; ateş yükseldi ve peritoneal bulgular '
                                             'belirginleşti.',
                          'teaching_point': 'Ateş ve lokal periton irritasyonu olan çocukta lavman uygunsuzdur.'},
                         {'text': 'Analjezi verip oral alımı kesmek, damar yolu açmak ve karını peritoneal bulgular '
                                  'ile ağrının tam yeri açısından yeniden muayene etmek',
                          'is_correct': True,
                          'explanation': 'Önceki normal görüntüleme ilerleyen klinik bulguları geçersiz kılmaz. Lokal '
                                         'peritoneal irritasyon cerrahi bir nedenin sürdüğünü gösterir; olası cerrahi '
                                         'için çocuk aç tutulur.',
                          'new_finding': 'Vital Bulgular: Ateş 38.6°C, KTA 132/dk, SS 26/dk, TA 102/64 mmHg, SpO2 %98, '
                                         'KDZ 2 sn. Bacaklarını karnına çekerek yatıyor. Sağ alt kadranda, klasik '
                                         'apendiks noktasının medialinde belirgin hassasiyet, istemsiz defans ve '
                                         'rebound. Diğer kadranlar rahat. Testisler normal, akciğer sesleri eşit.'},
                         {'text': 'Ateş nedeniyle idrar yolu enfeksiyonu düşünüp idrar tetkiki istemek, sonuç gelene '
                                  'kadar oral antibiyotik başlayıp oral sıvı vermek',
                          'is_correct': False,
                          'scenario_update': 'İdrar tetkiki normal geldi; oral sıvı verilen çocuk kustu ve cerrahi '
                                             'değerlendirme gecikti.',
                          'teaching_point': 'Karın muayenesi bulgularını açıklamayan tetkiklere odaklanmak tanıyı '
                                            'geciktirir.'}]},
            {'stage_title': 'Laboratuvar ve Ayrıntılı Görüntüleme',
             'question': 'Apendiksi normal bildirilmiş ancak lokal periton irritasyonu olan bu çocukta hangi tetkik '
                         'yaklaşımı uygundur?',
             'options': [{'text': 'Terminal ileumu değerlendirmek için acil kolonoskopi planlamak ve hazırlık için '
                                  'oral barsak temizleme solüsyonu vermek',
                          'is_correct': False,
                          'scenario_update': 'Oral solüsyon sonrası çocuk kustu ve ağrısı arttı; işlem güvenli '
                                             'bulunmadı.',
                          'teaching_point': 'Akut peritoneal bulgularda kolonoskopi ve oral barsak hazırlığı '
                                            'kontrendikedir.'},
                         {'text': 'Ultrasonu yinelemek yerine ertesi sabah tekrar muayene etmek üzere çocuğu '
                                  'antibiyotiksiz olarak servise yatırmak',
                          'is_correct': False,
                          'scenario_update': "Gece ateş 39.5°C'ye çıktı ve yaygın hassasiyet gelişti.",
                          'teaching_point': 'Peritoneal bulgusu olan ateşli çocukta tanısal değerlendirme '
                                            'ertelenmemelidir.'},
                         {'text': 'Ektopik mide mukozasını göstermek için teknesyum-99m perteknetat sintigrafisi '
                                  'planlamak ve sonuç gelene kadar çocuğu oral beslenmeyle izlemek',
                          'is_correct': False,
                          'scenario_update': 'Sintigrafi ertesi güne planlandı; inflamasyonlu yapıda tanısal değeri '
                                             'sınırlıydı ve tedavi gecikti.',
                          'teaching_point': 'Bu sintigrafi ağrısız rektal kanamada değerlidir; akut inflamatuvar '
                                            'tabloda ilk tetkik değildir.'},
                         {'text': 'Hemogram, CRP ve tam idrar istemek; deneyimli radyologla apendiks dışındaki '
                                  'yapıları da kapsayan ayrıntılı karın ultrasonu yaptırmak',
                          'is_correct': True,
                          'explanation': 'Laboratuvar inflamasyonu destekler. Ultrasonun yalnızca apendikse '
                                         'odaklanması diğer nedenlerin atlanmasına yol açabilir; ileum, mezenter ve '
                                         'over-testis gibi yapılar da değerlendirilmelidir.',
                          'new_finding': 'Lökosit 17.200/mm³ (%88 nötrofil), CRP 76 mg/L, tam idrar normal. Ultrason: '
                                         'retroçekal yerleşimli, 4 mm, basılabilen normal apendiks. Medialinde '
                                         'terminal ileumun antimezenterik kenarından kaynaklanan, kör sonlanan, 13 mm '
                                         'çaplı, kalın duvarlı, lümeni distandü tübüler yapı ve çevresinde '
                                         'inflamatuvar yağ dokusu.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Normal apendiks, sağ alt kadranda periton irritasyonu ve ultrasonda terminal ileumdan '
                         'kaynaklanan inflame kör sonlanan yapı olan bu çocukta tanı nedir?',
             'options': [{'text': 'Crohn hastalığına bağlı terminal ileit',
                          'is_correct': False,
                          'scenario_update': 'Kronik ishal, kilo kaybı ve büyüme geriliği yok; ileum duvarında '
                                             'segmenter kalınlaşma değil kör sonlanan yapı var.',
                          'teaching_point': 'Crohn hastalığında kronik semptomlar ve uzun segment ileum duvar '
                                            'kalınlaşması beklenir.'},
                         {'text': 'Meckel divertiküliti',
                          'is_correct': True,
                          'explanation': 'Terminal ileumun antimezenterik kenarından kaynaklanan, kör sonlanan inflame '
                                         'yapı Meckel divertikülünün iltihabını gösterir; klinik apandisiti taklit '
                                         'eder.',
                          'new_finding': 'Tanı: İnflame Meckel Divertikülü (Meckel Divertiküliti).'},
                         {'text': 'Retroçekal akut apandisit',
                          'is_correct': False,
                          'scenario_update': 'Apendiks 4 mm, basılabilir ve çevresinde inflamasyon yok.',
                          'teaching_point': 'Normal çaplı, basılabilen apendiks apandisit lehine değildir.'},
                         {'text': 'Omental infarkt',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonda hiperekoik omental kitle yok; tübüler inflame yapı ileumla '
                                             'ilişkili.',
                          'teaching_point': 'Omental infarkt genellikle obez çocuklarda, ateşsiz ve sağ tarafta lokal '
                                            'ağrıyla seyreder.'}]},
            {'stage_title': 'Tedavi ve Cerrahi',
             'question': 'Bu çocuğun tedavi planı hangisidir?',
             'options': [{'text': 'Ektopik mide mukozasına bağlı inflamasyonu azaltmak için intravenöz proton pompası '
                                  'inhibitörü başlamak ve iyileşme olursa cerrahiden kaçınmak',
                          'is_correct': False,
                          'scenario_update': 'Proton pompası inhibitörü inflamasyonu geriletmedi; çocuğun ateşi ve '
                                             'hassasiyeti sürdü.',
                          'teaching_point': 'Asit baskılama inflame yapının kesin tedavisi değildir.'},
                         {'text': 'Ateş ve ağrı azaldığı için oral amoksisilin-klavulanat ile taburcu edip iki hafta '
                                  'sonra elektif cerrahi değerlendirme planlamak',
                          'is_correct': False,
                          'scenario_update': 'Evde ağrı ve ateş yeniden başladı; çocuk perforasyon bulgularıyla geri '
                                             'geldi.',
                          'teaching_point': 'İnflame yapı perforasyon riskini sürdürür; tedavisi cerrahidir.'},
                         {'text': 'Oral alımı kesip intravenöz sıvı, analjezi ve geniş spektrumlu antibiyotik vermek, '
                                  'çocuk cerrahisiyle acil laparoskopik rezeksiyon planlamak',
                          'is_correct': True,
                          'explanation': 'İnflame yapı perforasyon ve obstrüksiyon riski taşır. Antibiyotik ve sıvı '
                                         'cerrahi hazırlığın parçasıdır; laparoskopik veya açık rezeksiyon kesin '
                                         'tedavidir.',
                          'new_finding': 'Seftriakson ve metronidazol başlandı. Laparoskopide ileoçekal valvin 60 cm '
                                         'proksimalinde inflame, perforasyon öncesi evrede divertikül saptandı ve '
                                         'rezeke edildi; patolojide ektopik mide mukozası doğrulandı. Çocuk üçüncü gün '
                                         'taburcu edildi.'},
                         {'text': 'Görüntüleme eşliğinde perkütan drenaj yapıp antibiyotikle altı hafta izlemek ve '
                                  'kontrol ultrasonuna göre karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Drene edilecek apse olmadığı için girişim yapılamadı; zaman kaybedildi.',
                          'teaching_point': 'Perkütan drenaj apse varlığında uygulanır; inflame yapı rezeksiyon '
                                            'gerektirir.'}]}]},
 {'id': 'Y57',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '18 Aylık',
  'gender': 'Kız',
  'complaint': 'Üç gündür süren ishal sırasında başlayan uyuklama, kas seyirmeleri ve acil kapısında nöbet',
  'history': "Ailesi anlatıyor: 'Üç gündür sulu ishali ve kusması vardı. Kaybettiği sıvıyı yerine koymak için sürekli "
             'kaynamış su ve açık çay içirdik, tuzlu sıvı vermedik. Bugün öğleden sonra çok uyuklamaya başladı, '
             "kollarında ve bacaklarında sıçramalar oldu.' Acil kapısında 3 dakika süren, kendiliğinden duran "
             'jeneralize tonik-klonik nöbet geçirdi. Ateşi yok, travma yok. Tartı: 11 kg.',
  'final_diagnosis': 'Ağır Semptomatik Hiponatremi (Hipotonik Sıvı Alımına Bağlı)',
  'disposition': 'Sarı Alanda Hava Yolu Güvenliği, %3 NaCl Bolusu ile Akut Düzeltme ve Kontrollü Sodyum Yükselişi İçin '
                 'Çocuk Yoğun Bakım Yatışı',
  'case_pearl': 'Ishalli çocuğa elektrolitsiz sıvı (su, çay, seyreltilmiş mama) verilmesi sodyumu hızla düşürebilir; '
                'akut düşüş beyin ödemi, nöbet ve solunum durmasına yol açar. Nöbet, bilinç bozukluğu veya solunum '
                'değişikliği varsa %3 NaCl 2-3 mL/kg 10-15 dakikada verilir, belirtiler sürerse 2-3 kez tekrarlanır; '
                "hedef ilk saatlerde 4-6 mEq/L yükseliştir. İlk 24 saatte toplam yükseliş 8-10 mEq/L'yi geçmemelidir "
                '(osmotik demiyelinizasyon riski). Önleme için ishalde ORS kullanımı öğretilmelidir.',
  'steps': [{'stage_title': 'Nöbet Yönetimi ve İlk Değerlendirme',
             'question': 'Nöbeti kendiliğinden duran, postiktal ve kas seyirmeleri süren bu çocukta ilk yaklaşımınız '
                         'nedir?',
             'options': [{'text': 'Ateşsiz nöbette santral sinir sistemi enfeksiyonunu dışlamak için lomber ponksiyon '
                                  'yapmak ve sonuç çıkana kadar asiklovir başlamak',
                          'is_correct': False,
                          'scenario_update': 'Lomber ponksiyon için hazırlanırken çocuğun seyirmeleri arttı; '
                                             'elektrolitler bakılmamıştı.',
                          'teaching_point': 'Ateşsiz ve ishal sonrası nöbette önce metabolik nedenler '
                                            'değerlendirilir.'},
                         {'text': 'İshale bağlı sıvı kaybı nedeniyle 20 mL/kg %0.45 NaCl ile %5 dekstroz bolusu vermek '
                                  've nöbeti dehidratasyona bağlamak',
                          'is_correct': False,
                          'scenario_update': 'Hipotonik sıvı sonrası çocukta ikinci nöbet gelişti ve sodyum daha da '
                                             'düştü.',
                          'teaching_point': 'Bolus sıvılar izotonik olmalıdır; hipotonik sıvı serbest su yükünü '
                                            'artırır.'},
                         {'text': 'Hava yolu ve solunumu güvenceye alıp oksijen vermek, damar yolu açmak, kapiller kan '
                                  'şekeri ve yatak başı kan gazında elektrolitlere bakmak',
                          'is_correct': True,
                          'explanation': 'Nöbet sonrası hava yolu ve oksijenasyon önceliklidir. Hipoglisemi ve '
                                         'elektrolit bozuklukları ishalli çocukta nöbetin hızla düzeltilebilir '
                                         'nedenleridir; yatak başı kan gazı dakikalar içinde sodyumu gösterir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.9°C, KTA 148/dk, SS 28/dk, TA 106/66 mmHg, SpO2 %94 '
                                         '(oksijenle %99). Postiktal konfüze, kollarında seyirmeler sürüyor. Pupiller '
                                         'izokorik, ışık refleksi var; fokal defisit yok. Mukozalar nemli, KDZ 2 sn. '
                                         'Kan şekeri 98 mg/dL. Kan gazı: Na 116 mEq/L, K 3.8 mEq/L, Cl 86 mEq/L, pH '
                                         '7.34.'},
                         {'text': 'Nöbet tekrarını önlemek için hemen intravenöz fenitoin yüklemesi yapıp kafa içi '
                                  'patolojiyi dışlamak amacıyla kontrastsız beyin tomografisi çekmek ve elektrolitleri '
                                  'sonrasında istemek',
                          'is_correct': False,
                          'scenario_update': 'Fenitoin seyirmeleri durdurmadı; tomografi için beklerken çocuk yeniden '
                                             'nöbet geçirdi.',
                          'teaching_point': 'Elektrolit bozukluğuna bağlı nöbette antiepileptikler etkisizdir; neden '
                                            'hızla düzeltilmelidir.'}]},
            {'stage_title': 'Acil Düzeltme',
             'question': 'Serum sodyumu 116 mEq/L olan, seyirmeleri ve konfüzyonu süren bu çocukta acil tedavi nasıl '
                         'olmalıdır?',
             'options': [{'text': 'Sodyumu düzeltmek için 20 mL/kg serum fizyolojik bolusu vermek ve iki saat sonra '
                                  'sodyumu yeniden ölçmek',
                          'is_correct': False,
                          'scenario_update': 'Serum fizyolojik sodyumu ancak 1-2 mEq/L yükseltti; seyirmeler sürdü.',
                          'teaching_point': 'Nörolojik belirtili akut düşüşte izotonik sıvı yetersizdir; hipertonik '
                                            'salin gerekir.'},
                         {'text': 'Yalnızca sıvı kısıtlaması yapıp oral yoldan tuz tableti vermek ve sodyumun '
                                  'kendiliğinden yükselmesini beklemek',
                          'is_correct': False,
                          'scenario_update': 'Bilinci bulanık çocuk tableti yutamadı; bir saat içinde yeniden nöbet '
                                             'geçirdi.',
                          'teaching_point': 'Nörolojik belirti varsa kısıtlama ve oral tedavi yetersizdir; acil '
                                            'hipertonik salin gerekir.'},
                         {'text': '%3 NaCl 3 mL/kg dozunu 10-15 dakikada intravenöz vermek, belirtiler sürerse '
                                  'tekrarlamak ve sodyumu yakından ölçmek',
                          'is_correct': True,
                          'explanation': 'Hipertonik salin bolusu sodyumu hızla 2-3 mEq/L yükselterek beyin ödemini '
                                         'azaltır ve nöbeti sonlandırır. İlk hedef belirtilerin düzelmesi ve 4-6 mEq/L '
                                         'yükseliştir.',
                          'new_finding': '33 mL %3 NaCl 15 dakikada verildi. Kontrol sodyum 121 mEq/L; seyirmeler ve '
                                         'konfüzyon geriledi, çocuk gözlerini açıp annesini tanıdı.'},
                         {'text': 'Sodyumu birkaç saat içinde normale getirmek için yüksek hızda sürekli %3 NaCl '
                                  'infüzyonu başlamak ve hedefi 135 mEq/L olarak belirlemek',
                          'is_correct': False,
                          'scenario_update': "Altı saatte sodyum 132 mEq/L'ye yükseldi; çok hızlı düzeltme nedeniyle "
                                             'osmotik demiyelinizasyon riski oluştu.',
                          'teaching_point': 'Akut düzeltmenin hedefi belirtilerin kontrolüdür; 24 saatte 8-10 '
                                            "mEq/L'den fazla yükselişten kaçınılır."}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'İshal sırasında yalnızca su ve çay içirilen, nöbet ve konfüzyonla gelen, serum sodyumu 116 '
                         'mEq/L olan bu çocukta tanı nedir?',
             'options': [{'text': 'Viral ensefalit',
                          'is_correct': False,
                          'scenario_update': 'Ateş yok; bulgular hipertonik salinle hızla düzeldi.',
                          'teaching_point': 'Ensefalitte ateş, ilerleyici bilinç değişikliği ve beyin omurilik sıvısı '
                                            'bulguları beklenir.'},
                         {'text': 'Basit febril nöbet',
                          'is_correct': False,
                          'scenario_update': 'Ateş yok ve serum sodyumu belirgin düşük.',
                          'teaching_point': 'Febril nöbet tanısı ateş varlığı ve metabolik nedenlerin dışlanmasıyla '
                                            'konur.'},
                         {'text': 'Ağır semptomatik hiponatremi',
                          'is_correct': True,
                          'explanation': 'Kayıpların elektrolitsiz sıvıyla yerine konması serbest su yükü oluşturarak '
                                         'sodyumu akut düşürür; nöbet ve konfüzyon beyin ödemine bağlı ağır '
                                         'belirtilerdir.',
                          'new_finding': 'Tanı: Ağır Semptomatik Hiponatremi (hipotonik sıvı alımına bağlı).'},
                         {'text': 'Hipoglisemik nöbet',
                          'is_correct': False,
                          'scenario_update': 'Kan şekeri 98 mg/dL.',
                          'teaching_point': 'Nöbetli her çocukta kan şekeri bakılmalıdır; burada normaldir.'}]},
            {'stage_title': 'İzlem ve Önleme',
             'question': 'Belirtileri düzelen bu çocuğun sonraki tedavisi ve izlemi nasıl olmalıdır?',
             'options': [{'text': 'Belirtiler düzeldiği için birkaç saat gözlem sonrası taburcu etmek ve aileye ishal '
                                  'geçene kadar bol su içirmelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'Evde bol su içirilen çocuk ertesi gün yeniden nöbetle getirildi.',
                          'teaching_point': 'Sodyum normale yaklaşmadan taburculuk yapılmaz; ishalde sade su yerine '
                                            'ORS önerilir.'},
                         {'text': 'Yoğun bakımda 2-4 saatte bir sodyum ölçmek, 24 saatte yükselişi 8-10 mEq/L ile '
                                  'sınırlamak, izotonik sıvı vermek ve aileye ishalde ORS kullanımını öğretmek',
                          'is_correct': True,
                          'explanation': 'Sık ölçüm aşırı hızlı düzeltmeyi önler. İzotonik idame sıvısı yeni düşüşü '
                                         'engeller. Aile eğitimi tekrarın önlenmesinde temeldir.',
                          'new_finding': 'Yoğun bakımda izotonik sıvı sürdürüldü; sodyum 24 saatte 125, 48 saatte 132 '
                                         'mEq/L oldu. Yeni nöbet olmadı. Aileye ORS hazırlama ve kullanımı uygulamalı '
                                         'anlatıldı.'},
                         {'text': 'Yeni nöbetleri önlemek için sodyum 135 mEq/L olana kadar her saat %3 NaCl bolusunu '
                                  'tekrarlamak ve bu süre boyunca diğer tüm sıvıları tamamen kısıtlamak',
                          'is_correct': False,
                          'scenario_update': 'Sodyum 12 saatte 18 mEq/L yükseldi; çocukta osmotik demiyelinizasyon '
                                             'açısından yüksek risk oluştu.',
                          'teaching_point': 'Belirtiler düzeldikten sonra hipertonik bolus tekrarlanmaz; yükseliş '
                                            'sınırlandırılır.'},
                         {'text': 'Nöbet durduğu için sodyum ölçümünü bırakmak, idame sıvısı olarak %0.18 NaCl ve %5 '
                                  'dekstroz başlamak ve çocuğu genel servise yatırmak',
                          'is_correct': False,
                          'scenario_update': "Hipotonik idame sıvısıyla sodyum yeniden 118 mEq/L'ye düştü ve çocukta "
                                             'yeni seyirmeler başladı.',
                          'teaching_point': 'Hasta çocuklarda hipotonik idame sıvısı hiponatremiyi ağırlaştırır; izlem '
                                            'sürdürülmelidir.'}]}]},
 {'id': 'Y58',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '3 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Üç gündür süren ishal ve kusma sonrası 24 saattir hiç idrar yapmama, solukluk ve halsizlik',
  'history': "Ailesi anlatıyor: 'Üç gündür günde on kez sulu ishali ve kusması var, ağızdan sıvı içiremedik. Ateşi "
             'için iki gündür ibuprofen şurubu veriyoruz. Son 24 saattir bezi kupkuru, hiç çiş yapmadı. Çok halsiz, '
             "gözlerini açmakta zorlanıyor. Böbrekleri iflas mı etti diye çok korkuyoruz.' Dışkıda kan yok. Bilinen "
             'böbrek hastalığı yok. Hastalık öncesi tartısı: 14 kg.',
  'final_diagnosis': 'Dehidratasyona Bağlı Prerenal Akut Böbrek Hasarı',
  'disposition': 'Sarı Alanda İzotonik Sıvı Bolusları, Nefrotoksik İlaçların Kesilmesi, İdrar Çıkışı ve Böbrek '
                 'Fonksiyon İzlemi ile Servis Yatışı',
  'case_pearl': 'Hipovolemide böbrek perfüzyonu azalır; tübüller sağlam olduğundan sodyum ve su tutulur (idrar sodyumu '
                '<20 mEq/L, FENa <%1, dansite yüksek, BUN/kreatinin oranı >20). Hızlı ve yeterli hacim replasmanıyla '
                "tablo genellikle 24-72 saatte geri döner. Uzarsa akut tübüler nekroza ilerleyebilir. NSAİİ'ler "
                'afferent arteriyolü daraltarak hasarı artırır ve kesilmelidir. İdrar çıkışı sıvı tedavisine yanıtın '
                'en iyi göstergesidir.',
  'steps': [{'stage_title': 'Hacim Durumu ve Acil Resüsitasyon',
             'question': '24 saattir idrar yapmayan, halsiz bu 3 yaşındaki çocukta ilk yaklaşımınız nedir?',
             'options': [{'text': 'Ondansetron verip oral rehidratasyon solüsyonunu kaşıkla denemek ve çocuk idrar '
                                  'yapana kadar acil serviste beklemek',
                          'is_correct': False,
                          'scenario_update': 'Halsiz çocuk sıvıyı yeterli içemedi; iki saat sonra perfüzyonu daha da '
                                             'bozuldu.',
                          'teaching_point': 'Dolaşım bozukluğu bulgusu olan çocukta oral deneme yerine intravenöz '
                                            'bolus gerekir.'},
                         {'text': 'Perfüzyon, kan basıncı ve hidrasyonu değerlendirip mesanenin dolu olup olmadığına '
                                  'bakmak, damar yolu açıp 20 mL/kg izotonik sıvı bolusu vermek',
                          'is_correct': True,
                          'explanation': 'İdrar yokluğunun en sık nedeni hipovolemidir; hızlı izotonik bolus '
                                         'perfüzyonu ve böbrek kan akımını düzeltir. Dolu mesane idrar retansiyonunu '
                                         'gösterir ve yaklaşımı değiştirir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.3°C, KTA 146/dk, SS 30/dk, TA 80/48 mmHg, SpO2 %98, '
                                         'KDZ 3.5 sn. Gözler çökük, mukozalar kuru, deri turgoru 2.5 sn. Ödem yok, '
                                         'akciğerler temiz. Suprapubik bölgede mesane ele gelmiyor, yatak başı '
                                         'ultrasonda mesane boş. 20 mL/kg serum fizyolojik verildi; KTA 124/dk, KDZ '
                                         '2.5 sn.'},
                         {'text': 'Mesane kateteri takıp idrar gelmezse acil nefroloji konsültasyonu istemek ve sıvı '
                                  'tedavisini nefroloji önerisine kadar ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Kateterden idrar gelmedi; nefroloji beklenirken bir saat sıvı verilmedi '
                                             've taşikardi arttı.',
                          'teaching_point': 'Hipovolemi bulgusu varsa sıvı resüsitasyonu konsültasyon beklenmeden '
                                            'başlanır.'},
                         {'text': '24 saattir idrar yapmadığı için gelişmiş böbrek yetmezliği kabul edip sıvıyı '
                                  'kısıtlamak ve idrar çıkışını sağlamak için yüksek doz intravenöz furosemid vermek',
                          'is_correct': False,
                          'scenario_update': 'Furosemid sonrası idrar gelmedi; kan basıncı daha da düştü ve çocuk '
                                             'letarjikleşti.',
                          'teaching_point': 'Hipovolemik çocukta diüretik ve sıvı kısıtlaması perfüzyonu daha da '
                                            'bozar.'}]},
            {'stage_title': 'Laboratuvar Değerlendirmesi',
             'question': 'Bolusa yanıt veren bu çocukta hangi tetkikler istenmelidir?',
             'options': [{'text': 'BUN, kreatinin, elektrolitler, kan gazı ve tam idrar istemek; ilk idrarda sodyum, '
                                  'kreatinin ve dansiteye bakarak sodyum atılım fraksiyonunu hesaplamak',
                          'is_correct': True,
                          'explanation': 'BUN/kreatinin oranı, düşük idrar sodyumu, FENa <%1 ve yüksek dansite tübül '
                                         'fonksiyonunun korunduğunu, yani hasarın perfüzyona bağlı olduğunu gösterir. '
                                         'Potasyum ve asidoz acil tedavi gerektirebilir.',
                          'new_finding': 'BUN 102 mg/dL, kreatinin 1.9 mg/dL (bazal beklenen ~0.4), Na 135, K 5.0 '
                                         'mEq/L, HCO3 17 mmol/L. Bolustan sonraki ikinci saatte 35 mL idrar: dansite '
                                         '1025, idrar sodyumu 11 mEq/L, FENa %0.4, idrar sedimenti temiz.'},
                         {'text': 'Glomerülonefrit ve diğer parankim hastalıklarını dışlamak için acil perkütan böbrek '
                                  'biyopsisi planlamak ve sıvı tedavisini biyopsi sonucuna göre ayarlamak',
                          'is_correct': False,
                          'scenario_update': 'Biyopsi bu klinik tabloda endike değildi; nefroloji işlemi reddetti ve '
                                             'zaman kaybedildi.',
                          'teaching_point': 'Böbrek biyopsisi açıklanamayan veya ilerleyici böbrek hasarında '
                                            'düşünülür.'},
                         {'text': 'Böbrekleri ayrıntılı görmek için intravenöz kontrastlı batın tomografisi çekmek ve '
                                  'laboratuvarı görüntüleme sonrasına bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Kontrast madde zaten bozulmuş böbrek fonksiyonunu daha da kötüleştirdi.',
                          'teaching_point': 'Böbrek fonksiyonu bozulmuş çocukta nefrotoksik kontrast maddelerden '
                                            'kaçınılır; gerekirse ultrason yeterlidir.'},
                         {'text': 'Böbrek skarını değerlendirmek için DMSA sintigrafisi planlamak ve sonuç çıkana '
                                  'kadar çocuğu oral sıvıyla izlemek',
                          'is_correct': False,
                          'scenario_update': 'Sintigrafi akut dönemde yönetime katkı sağlamadı; temel laboratuvar '
                                             'tetkikleri gecikti.',
                          'teaching_point': 'DMSA sintigrafisi akut tabloda değil, seçilmiş olgularda geç dönemde '
                                            'kullanılır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Dehidratasyon sonrası idrar yokluğu, kreatinin artışı, idrar sodyumu 11 mEq/L, FENa %0.4 ve '
                         'bolusa idrar çıkışıyla yanıt veren bu çocukta tanı nedir?',
             'options': [{'text': 'Posterior üretral valve bağlı obstrüksiyon',
                          'is_correct': False,
                          'scenario_update': 'Mesane boş, idrar akımı bolus sonrası başladı ve bilinen idrar yolu '
                                             'sorunu yok.',
                          'teaching_point': 'Postrenal nedenlerde dolu mesane ve hidronefroz beklenir.'},
                         {'text': 'Akut tübüler nekroz',
                          'is_correct': False,
                          'scenario_update': "FENa %1'in altında, idrar sodyumu düşük, dansite yüksek ve sediment "
                                             'temiz.',
                          'teaching_point': 'Akut tübüler nekrozda FENa >%2, idrar sodyumu >40 mEq/L ve granüler '
                                            'silendirler görülür.'},
                         {'text': 'Dehidratasyona bağlı prerenal akut böbrek hasarı',
                          'is_correct': True,
                          'explanation': 'Hipovolemiye bağlı azalmış böbrek perfüzyonunda tübüller sodyumu tutmaya '
                                         'devam eder; düşük idrar sodyumu, FENa <%1 ve sıvıya hızlı yanıt prerenal '
                                         'hasarı doğrular. NSAİİ kullanımı tabloya katkıda bulunmuştur.',
                          'new_finding': 'Tanı: Dehidratasyona Bağlı Prerenal Akut Böbrek Hasarı (NSAİİ katkılı).'},
                         {'text': 'Hemolitik üremik sendrom',
                          'is_correct': False,
                          'scenario_update': 'Kanlı ishal öyküsü yok; anemi ve trombositopeni saptanmadı.',
                          'teaching_point': 'Hemolitik üremik sendromda mikroanjiyopatik hemoliz ve trombositopeni '
                                            'böbrek hasarına eşlik eder.'}]},
            {'stage_title': 'Sıvı Tedavisi ve İzlem',
             'question': 'Bu çocuğun sonraki tedavisi ve izlemi nasıl olmalıdır?',
             'options': [{'text': 'Kreatinin yüksek olduğu için hemen periton diyalizi başlatmak üzere nefrolojiye '
                                  'devretmek ve sıvıyı idame hızının altında tutmak',
                          'is_correct': False,
                          'scenario_update': 'Nefroloji diyaliz endikasyonu olmadığını belirtti; kısıtlı sıvı '
                                             'nedeniyle idrar çıkışı yeniden azaldı.',
                          'teaching_point': 'Diyaliz hiperkalemi, sıvı yüklenmesi, ağır asidoz veya üremi gibi '
                                            'endikasyonlarda yapılır.'},
                         {'text': 'İdrar çıkışı başladığı için ateş için ibuprofene devam ederek çocuğu oral sıvıyla '
                                  'taburcu etmek ve bir hafta sonra kreatinin kontrolü yapmak',
                          'is_correct': False,
                          'scenario_update': 'Evde yeterli içemeyen ve ibuprofen almaya devam eden çocuk iki gün sonra '
                                             'yeniden idrarsız getirildi.',
                          'teaching_point': 'Kreatinin düşmeden ve oral alım güvenceye alınmadan taburculuk yapılmaz; '
                                            'NSAİİ kesilir.'},
                         {'text': 'Ibuprofeni kesip izotonik sıvıyla açığı ve idameyi vermek, idrar çıkışını ve sıvı '
                                  'dengesini saatlik izlemek, 12-24 saatte kreatinin ve elektrolitleri tekrarlamak',
                          'is_correct': True,
                          'explanation': "Hacim açığının kapatılması böbrek perfüzyonunu düzeltir. NSAİİ'ler hasarı "
                                         'artırır. Yeterli sıvıya rağmen idrar çıkışı düzelmezse intrinsik böbrek '
                                         'hasarı düşünülür ve nefroloji ile değerlendirilir.',
                          'new_finding': 'İbuprofen kesildi, izotonik sıvı sürdürüldü. İdrar çıkışı 1.5-2 mL/kg/saat '
                                         "oldu. Kreatinin 24 saatte 0.9, 72 saatte 0.4 mg/dL'ye geriledi; çocuk "
                                         'dördüncü gün taburcu edildi.'},
                         {'text': 'İdrar çıkışını artırmak için saatlik 20 mL/kg bolusları idrar dansitesi normale '
                                  'dönene kadar tekrarlamak ve furosemid eklemek',
                          'is_correct': False,
                          'scenario_update': 'Tekrarlanan boluslar sonrası çocukta göz kapağı ödemi ve takipne '
                                             'gelişti.',
                          'teaching_point': 'Bolus yalnızca perfüzyon bozukluğu sürüyorsa tekrarlanır; sonrasında '
                                            'hesaplanmış açık ve idame verilir.'}]}]},
 {'id': 'Y59',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '5 Yaşında',
  'gender': 'Kız',
  'complaint': 'Nefrotik sendrom tanılı çocukta aniden başlayan ateş, yaygın şiddetli karın ağrısı ve kusma',
  'history': "Ailesi anlatıyor: 'Bir aydır nefrotik sendrom atağında, günlük yüksek doz prednizolon kullanıyor; karnı "
             "ve bacakları şiş. Dün gece aniden ateşi 38.8°C'ye çıktı, karnının her yerinde çok şiddetli ağrı başladı, "
             "üç kez kustu. Nefes alırken bile karnının battığını söylüyor, kıpırdamadan yatıyor.' Pnömokok aşıları "
             'eksik. Tartı: 20 kg (ödemli; kuru ağırlığı 17 kg).',
  'final_diagnosis': 'Nefrotik Sendrom Zemininde Spontan Bakteriyel Peritonit',
  'disposition': 'Sarı Alanda Kan Kültürü ve Tanısal Parasentez Sonrası İntravenöz Seftriakson, Dikkatli Hacim Desteği '
                 've Stres Dozu Steroid ile Servis Yatışı',
  'case_pearl': 'Nefrotik sendromda idrarla immünoglobulin ve kompleman kaybı, asit ve steroid kullanımı nedeniyle '
                'kapsüllü bakterilerle (en sık S. pneumoniae) asit enfeksiyonu gelişebilir. Asit sıvısında nötrofil '
                '>250/mm³ tanı koydurur. Tedavi pnömokok ve gram negatifleri kapsayan üçüncü kuşak sefalosporindir. '
                'Ödemli olmasına rağmen damar içi hacim azalmış olabilir; hipovolemi ve tromboz açısından dikkatli '
                'olunmalıdır. Uzun süreli steroid kullananlarda stres dozu gerekir; asit varlığında steroid bulguları '
                'maskeleyebilir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Sepsis Yaklaşımı',
             'question': 'Nefrotik sendrom atağında, yüksek doz steroid kullanan, ateşli ve yaygın karın ağrılı bu '
                         'çocukta ilk yaklaşımınız nedir?',
             'options': [{'text': 'Sepsis ve damar içi hacim azlığı bulgularını değerlendirmek, karını ayrıntılı '
                                  'muayene etmek, damar yolu açıp kan kültürü almak',
                          'is_correct': True,
                          'explanation': 'Ödemli çocukta damar içi hacim azalmış olabilir; taşikardi ve soğuk '
                                         'ekstremiteler hipovolemiyi düşündürür. Steroid kullanımı karın bulgularını '
                                         'hafifletebilir. Kan kültürü antibiyotik öncesi alınmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 38.7°C, KTA 138/dk, SS 32/dk, TA 96/60 mmHg, SpO2 %98, '
                                         'KDZ 3 sn, ekstremiteler soğuk. Periorbital ve pretibial gode bırakan ödem. '
                                         'Karında masif asit, dalgalanma hissi; tüm kadranlarda istemsiz defans ve '
                                         'yaygın rebound. Bağırsak sesleri azalmış. Kan kültürü alındı.'},
                         {'text': 'Ateşi uzun süreli steroid kullanımının yan etkisine bağlayıp prednizolonu hemen '
                                  'kesmek ve oral antipiretikle çocuğu gözlem odasına almak',
                          'is_correct': False,
                          'scenario_update': 'Steroidin ani kesilmesi hipotansiyona katkıda bulundu; enfeksiyon '
                                             'kaynağı aranmadı.',
                          'teaching_point': 'Uzun süre steroid kullanan çocukta ilaç aniden kesilmez; stres altında '
                                            'doz artırılabilir.'},
                         {'text': 'Yaygın karın hassasiyeti nedeniyle perfore apandisit düşünüp doğrudan çocuk '
                                  'cerrahisine laparotomi için yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Cerrahi ekip, nefrotik çocukta asit enfeksiyonunun önce dışlanması '
                                             'gerektiğini belirterek laparotomiyi erteledi.',
                          'teaching_point': 'Nefrotik sendromlu çocukta yaygın karın bulguları çoğunlukla cerrahi dışı '
                                            'bir enfeksiyondan kaynaklanır.'},
                         {'text': 'Karındaki sıvıyı azaltmak için intravenöz albümin ve furosemid vermek, ağrı '
                                  'azalırsa çocuğu nefroloji servisine yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Furosemid sonrası kan basıncı düştü ve taşikardi arttı; ateşin nedeni '
                                             'araştırılmadı.',
                          'teaching_point': 'Ateşli, hipovolemik ve karın bulguları olan çocukta diüretik '
                                            'tehlikelidir; önce enfeksiyon değerlendirilir.'}]},
            {'stage_title': 'Parasentez ve Laboratuvar',
             'question': 'Kan kültürü alınan bu çocukta tanıyı kesinleştirmek için hangi tetkik yapılmalıdır?',
             'options': [{'text': 'Ultrason eşliğinde tanısal parasentez yapıp asitte hücre sayımı, Gram boyama ve '
                                  'kültür istemek; hemogram, CRP, albümin ve kreatinine bakmak',
                          'is_correct': True,
                          'explanation': 'Asit sıvısında nötrofil sayısı >250/mm³ tanı koydurur; Gram boyama ve kan '
                                         'kültürü şişelerine ekilen kültür etkeni belirler. Albümin ve kreatinin hacim '
                                         'durumu ve böbrek fonksiyonunu gösterir.',
                          'new_finding': 'Asit sıvısı bulanık: lökosit 1850/mm³ (%86 nötrofil; nötrofil 1590/mm³), '
                                         'Gram boyamada gram pozitif diplokoklar. Kan: lökosit 18.200/mm³, CRP 88 '
                                         'mg/L, albümin 1.8 g/dL, kreatinin 0.5 mg/dL.'},
                         {'text': 'Parasentezin kanama riski taşıdığını düşünerek yapmamak ve tanıyı kesinleştirmek '
                                  'için tanısal laparoskopi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Laparoskopi genel anestezi gerektirdi; hemodinamik olarak hassas çocukta '
                                             'risk ve gecikme oluştu.',
                          'teaching_point': 'Ultrason eşliğinde parasentez güvenli ve tanısaldır; cerrahi tanısal '
                                            'yöntem ilk tercih değildir.'},
                         {'text': 'Karın ağrısının kaynağını göstermek için intravenöz kontrastlı batın tomografisi '
                                  'çekmek ve sonuca göre antibiyotik kararı vermek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi yaygın asit gösterdi ancak sıvının enfekte olup olmadığını '
                                             'ayırt edemedi; tedavi gecikti.',
                          'teaching_point': 'Asit enfeksiyonunun tanısı görüntülemeyle değil, sıvı analiziyle konur.'},
                         {'text': 'Yalnızca tam idrar tetkiki ve idrar kültürü göndermek, proteinüri arttıysa ateşi '
                                  'nefrotik atağın alevlenmesine bağlayıp steroid dozunu artırmak',
                          'is_correct': False,
                          'scenario_update': 'İdrar tetkiki enfeksiyon kaynağını göstermedi; asit enfeksiyonu '
                                             'tedavisiz kaldı.',
                          'teaching_point': 'Nefrotik atak ateş yapmaz; ateşli nefrotik çocukta ciddi enfeksiyon '
                                            'aranmalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Nefrotik sendromlu çocukta ateş, yaygın karın hassasiyeti ve asit sıvısında 1590/mm³ '
                         'nötrofil ile gram pozitif diplokoklar saptanırsa tanı nedir?',
             'options': [{'text': 'Akut pankreatit',
                          'is_correct': False,
                          'scenario_update': 'Asit sıvısında belirgin nötrofil ve bakteri var; tablo enfeksiyonu '
                                             'gösteriyor.',
                          'teaching_point': 'Steroid kullananlarda pankreatit görülebilir ancak asitte bakteri '
                                            'beklenmez.'},
                         {'text': 'Spontan bakteriyel peritonit',
                          'is_correct': True,
                          'explanation': 'Nefrotik zeminde asit sıvısında nötrofil >250/mm³ ve tek tip gram pozitif '
                                         'diplokok (olası pnömokok) cerrahi odak olmadan gelişen spontan bakteriyel '
                                         'peritoniti doğrular.',
                          'new_finding': 'Tanı: Nefrotik Sendrom Zemininde Spontan Bakteriyel Peritonit (olası S. '
                                         'pneumoniae).'},
                         {'text': 'Perfore apandisite bağlı sekonder peritonit',
                          'is_correct': False,
                          'scenario_update': 'Tek bir mikroorganizma görüldü; çoklu bakteri, serbest hava veya lokal '
                                             'odak yok.',
                          'teaching_point': 'Sekonder peritonitte asitte çoklu flora, çok yüksek protein ve düşük '
                                            'glukoz beklenir.'},
                         {'text': 'Renal ven trombozu',
                          'is_correct': False,
                          'scenario_update': 'Hematüri ve böğür ağrısı yok; asit enfeksiyonu bulguları tabloyu '
                                             'açıklıyor.',
                          'teaching_point': 'Nefrotik sendromda tromboz riski yüksektir ancak burada tablo '
                                            'enfeksiyöz.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu çocuğun tedavi planı hangisidir?',
             'options': [{'text': 'Asiti tamamen boşaltmak için büyük hacimli parasentez yapmak ve enfeksiyonu kontrol '
                                  'etmek için laparotomiyle periton lavajı planlamak',
                          'is_correct': False,
                          'scenario_update': 'Büyük hacimli boşaltma sonrası hipotansiyon gelişti; cerrahi ekip '
                                             'laparotomiyi gereksiz buldu.',
                          'teaching_point': 'Spontan enfeksiyon antibiyotikle tedavi edilir; cerrahi lavaj gerekmez.'},
                         {'text': 'Antipiretik sonrası ağrı ve ateş azalınca çocuğu oral amoksisilin ile taburcu etmek '
                                  've steroid tedavisini aynı dozda sürdürmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Evde ateş sürdü; çocuk hipotansiyonla geri getirildi.',
                          'teaching_point': 'Asit enfeksiyonu parenteral tedavi ve hastane izlemi gerektirir.'},
                         {'text': 'Enfeksiyonla savaşmak için steroidi tamamen kesip intravenöz immünoglobulin vermek '
                                  've antibiyotiği kültür sonucuna kadar ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik gecikti ve steroidin ani kesilmesiyle çocukta dirençli '
                                             'hipotansiyon gelişti.',
                          'teaching_point': 'Antibiyotik kültür alınır alınmaz başlanır; steroid aniden kesilmez.'},
                         {'text': 'İntravenöz seftriakson başlamak, hipovolemi varsa albümin ve izotonik sıvı vermek, '
                                  'stres dozu steroid planlamak ve tromboz açısından izlemek',
                          'is_correct': True,
                          'explanation': 'Üçüncü kuşak sefalosporin pnömokok ve gram negatifleri kapsar; 7-10 gün '
                                         'verilir. Damar içi hacim azlığında albümin desteği perfüzyonu düzeltir. Uzun '
                                         'süreli steroid kullananlarda adrenal baskılanma olabileceğinden stres dozu '
                                         'düşünülür. İyileşme sonrası aşılar tamamlanır.',
                          'new_finding': 'Seftriakson başlandı, albümin ve izotonik sıvıyla perfüzyon düzeldi, stres '
                                         'dozu hidrokortizon planlandı. Kan ve asit kültüründe penisiline duyarlı S. '
                                         'pneumoniae üredi. 72 saatte ateş düştü; tedavi 10 güne tamamlandı ve '
                                         'pnömokok aşıları planlandı.'}]}]},
 {'id': 'Y60',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '2 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Oyuncak kumandasındaki yassı yuvarlak pili yuttuktan sonra göğüs ağrısı, salya akıtma ve yutamama',
  'history': "Ailesi anlatıyor: 'Yaklaşık 45 dakika önce oyuncak arabanın kumandasının kapağını açmış, içindeki madeni "
             'para büyüklüğündeki yassı yuvarlak lityum pili ağzına atıp yutmuş. O andan beri göğsünün üstünü gösterip '
             "ağlıyor, tükürüğünü yutamıyor, salyası akıyor. Su içirmeye çalıştık, hemen öğürüp çıkardı.' Öksürük ve "
             'nefes darlığı yok. Bilinen hastalığı yok. Tartı: 12 kg.',
  'final_diagnosis': 'Özofagusta Takılı Düğme Pil',
  'disposition': 'Sarı Alanda Oral Alımın Kesilmesi, Bal Uygulaması ve İlk 2 Saat İçinde Acil Endoskopik Çıkarma, '
                 'Sonrasında Gecikmiş Komplikasyon İzlemi',
  'case_pearl': 'Özofagusta takılan lityum düğme pil, mukozada hidroksit iyonu oluşturarak 2 saat içinde ciddi yanık '
                'yapabilir; perforasyon, trakeoözofageal fistül ve aortoözofageal fistül gelişebilir. Çıkarma süresi '
                'saatlerle ölçülür. Çocuk 1 yaşından büyükse ve yutma 12 saat içindeyse endoskopiyi geciktirmeden 10 '
                'dakikada bir 10 mL bal verilmesi (en fazla 6 doz) hasarı azaltır. Ön-arka grafide çift halka, yan '
                'grafide basamaklanma görülür. Çıkarma sonrası haftalarca gecikmiş komplikasyonlar açısından izlem '
                'gerekir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Acil Önlemler',
             'question': '45 dakika önce yassı yuvarlak lityum pil yutan, salya akıtan ve yutamayan bu 2 yaşındaki '
                         'çocukta ilk yaklaşımınız nedir?',
             'options': [{'text': 'Hava yolunu değerlendirip oral alımı kesmek, işlemi geciktirmeden 10 mL bal vermek, '
                                  'acil grafi çekip endoskopi ekibini çağırmak',
                          'is_correct': True,
                          'explanation': 'Salya ve yutamama özofagusta takılmayı düşündürür. 1 yaşından büyük çocukta '
                                         'ilk 12 saat içinde bal, pil yüzeyini kaplayarak mukoza hasarını azaltır; '
                                         'ancak çıkarma işlemi asla geciktirilmez.',
                          'new_finding': 'Vital Bulgular: Ateş 37.0°C, KTA 128/dk, SS 26/dk, TA 94/56 mmHg, SpO2 %99. '
                                         'Ajite, göğsünün üstünü gösteriyor, salya akıyor. Stridor ve solunum '
                                         'sıkıntısı yok, akciğer sesleri eşit. Hematemez yok. 10 mL bal verildi; '
                                         'endoskopi ekibi bilgilendirildi.'},
                         {'text': 'Pili mideye itmek için bol su ve ekmek yedirmek, ardından dışkıyla çıkmasını '
                                  'beklemek üzere aileyi evde izleme yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk suyu ve ekmeği kustu; özofagusta takılı pil yerinde kalmaya devam '
                                             'etti.',
                          'teaching_point': 'Özofagusta takılı cisim için zorlama beslenme aspirasyon riskini artırır '
                                            've hasarı durdurmaz.'},
                         {'text': 'Pilin ağızdan çıkması için ipeka şurubu ile kusturmaya çalışmak ve yarım saat '
                                  'içinde kusma olmazsa boyun-göğüs grafisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Kusturma girişimi sonrası çocuk öğürdü ama pil çıkmadı; aspirasyon riski '
                                             'oluştu.',
                          'teaching_point': 'Yutulan cisimlerde kusturma kontrendikedir; aspirasyon riskini artırır.'},
                         {'text': 'Çocuk stabil olduğu için ailenin aç kalma süresini tamamlamasını bekleyip '
                                  'endoskopiyi ertesi sabaha planlamak',
                          'is_correct': False,
                          'scenario_update': 'Bekleme süresinde çocukta hematemez gelişti; endoskopide derin özofagus '
                                             'yanığı saptandı.',
                          'teaching_point': 'Bu tabloda endoskopi aç kalma süresi beklenmeden acil yapılır; hasar '
                                            'dakikalar-saatler içinde gelişir.'}]},
            {'stage_title': 'Görüntüleme',
             'question': 'Bal verilen ve endoskopi ekibi bilgilendirilen bu çocukta hangi görüntüleme yapılmalıdır?',
             'options': [{'text': 'Özofagus hasarını değerlendirmek için endoskopiden önce intravenöz kontrastlı '
                                  'toraks tomografisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi endoskopiyi bir saat geciktirdi; bu sürede mukoza hasarı '
                                             'ilerledi.',
                          'teaching_point': 'Tomografi gerekirse çıkarma sonrası komplikasyon değerlendirmesi için '
                                            'yapılır; çıkarmayı geciktirmez.'},
                         {'text': 'Cismin yerini ve özofagus hasarını kesinleştirmek için oral kontrastlı özofagus '
                                  'grafisi çekmek ve kontrastın mideye geçişini izlemek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk kontrastı aspire etti ve öksürmeye başladı.',
                          'teaching_point': 'Yutamayan çocukta oral kontrast aspirasyon riski taşır ve gereksizdir.'},
                         {'text': 'Boyun, göğüs ve karını kapsayan ön-arka ve yan grafi çekmek; cismin yerini, şeklini '
                                  've kenar özelliklerini değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Ön-arka grafide çift halka, yan grafide basamaklanma lityum pili madeni '
                                         'paradan ayırır. Yan grafi negatif kutbun yönünü ve hasarın en çok olacağı '
                                         'tarafı gösterir.',
                          'new_finding': 'Ön-arka ve yan grafi: üst özofagusta (C6-T1 düzeyi) 20 mm çaplı yuvarlak '
                                         'metalik opasite; ön-arka görüntüde çift halka, yan görüntüde kenarda '
                                         'basamaklanma. Cilt altı amfizem ve mediastinal hava yok.',
                          'image': 'assets/images/adbg_button_battery.png',
                          'image_caption': 'Boyun-Göğüs Grafisi (Ön-Arka ve Yan)'},
                         {'text': 'Radyasyon riskini azaltmak için grafi çekmeden yalnızca metal dedektörüyle yerini '
                                  'belirlemek ve endoskopiyi buna göre planlamak',
                          'is_correct': False,
                          'scenario_update': 'Dedektör cismin şeklini ve türünü göstermedi; madeni para ile pil ayrımı '
                                             'yapılamadı.',
                          'teaching_point': 'Grafi cismin türünü, yerini ve komplikasyonları gösterdiği için '
                                            'zorunludur.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': "Grafide üst özofagusta çift halka ve basamaklanma gösteren 20 mm'lik yuvarlak metalik "
                         'opasite saptanan bu çocukta tanı nedir?',
             'options': [{'text': 'Özofagusta takılı düğme pil',
                          'is_correct': True,
                          'explanation': 'Öyküyle birlikte çift halka ve basamaklanma işareti özofagusta takılı lityum '
                                         'düğme pili doğrular; acil endoskopik çıkarma gerektirir.',
                          'new_finding': 'Tanı: Özofagusta Takılı Lityum Düğme Pil.'},
                         {'text': 'Retrofaringeal apse',
                          'is_correct': False,
                          'scenario_update': 'Ateş ve boyun hareket kısıtlılığı yok; grafide metalik cisim var.',
                          'teaching_point': 'Retrofaringeal apse ateş, boyun sertliği ve prevertebral yumuşak doku '
                                            'genişlemesiyle seyreder.'},
                         {'text': 'Akut viral krup',
                          'is_correct': False,
                          'scenario_update': 'Stridor ve havlar tarzda öksürük yok; yutma öyküsü ve metalik cisim var.',
                          'teaching_point': 'Krupta inspiratuvar stridor ve havlar öksürük öne çıkar.'},
                         {'text': 'Özofagusta takılı madeni para',
                          'is_correct': False,
                          'scenario_update': 'Madeni para grafide tek, homojen bir disk olarak görülür; çift halka ve '
                                             'basamaklanma yoktur.',
                          'teaching_point': 'Çift halka işareti lityum pili madeni paradan ayırır ve aciliyeti '
                                            'belirler.'}]},
            {'stage_title': 'Çıkarma ve İzlem',
             'question': 'Bu çocuğun tedavi ve izlem planı nasıl olmalıdır?',
             'options': [{'text': 'İlk 2 saat içinde genel anestezi altında endoskopik çıkarma yapmak, mukoza hasarını '
                                  'değerlendirmek ve gecikmiş fistül-perforasyon belirtileri için haftalarca izlemek',
                          'is_correct': True,
                          'explanation': 'Hasar süreyle orantılı olduğundan çıkarma acil yapılır. Endoskopide yanığın '
                                         'derinliği ve yönü kaydedilir; aortoözofageal fistül gibi hayatı tehdit eden '
                                         'komplikasyonlar haftalar sonra gelişebileceğinden aile hematemez, ateş ve '
                                         'göğüs ağrısı konusunda bilgilendirilir.',
                          'new_finding': 'Yutmadan 1 saat 40 dakika sonra endoskopik olarak çıkarıldı; arka duvarda '
                                         'yüzeyel yanık saptandı, asetik asitle yıkandı. Aileye gecikmiş komplikasyon '
                                         'belirtileri anlatıldı; iki hafta sonraki kontrolde yutma normaldi.'},
                         {'text': 'Mukozayı korumak için intravenöz proton pompası inhibitörü ve sukralfat başlamak, '
                                  'pil mideye geçebileceği için 24 saat sonra kontrol grafisiyle endoskopi '
                                  'gereksinimini değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Bekleme sırasında mukoza hasarı ilerledi; endoskopide derin nekroz '
                                             'saptandı.',
                          'teaching_point': 'İlaçlar çıkarmanın yerini tutmaz; pil acilen çıkarılmalıdır.'},
                         {'text': 'Acil serviste sedasyonsuz Foley kateteriyle körlemesine çekerek pili çıkarmak ve '
                                  'çocuğu hemen taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Girişim sırasında çocuk öğürdü ve pil hava yoluna doğru yer değiştirdi; '
                                             'acil anestezi gerekti.',
                          'teaching_point': 'Lityum pil doğrudan görüş altında çıkarılmalı ve mukoza hasarı '
                                            'değerlendirilmelidir.'},
                         {'text': 'Pilin mideye geçmesi için laksatif vermek ve dışkıyla çıkana kadar günlük grafiyle '
                                  'evde izlemek',
                          'is_correct': False,
                          'scenario_update': 'Pil özofagusta kaldı; ikinci gün ateş ve hematemez gelişti.',
                          'teaching_point': 'Özofagustaki pil kendiliğinden ilerlemeyi beklemeden acil '
                                            'çıkarılmalıdır.'}]}]}]
