# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Sarı Alan Vakaları (Part 6: Y51 - Y60)
Odak: Bulantı, Kusma, Karın Ağrısı, İshal (GİS Acilleri - Sarı Alan Monitörizasyon & Stabilizasyon)
Kılavuzlar: ESPGHAN, AAP, PALS, NASPGHAN, APSA (Pediatric Surgery)
"""

YELLOW_CASES_PART6 = [ { 'age': '5 Yaşında',
    'case_pearl': 'Geçirilmiş batın cerrahisi olan bir çocukta safralı kusma, karın distansiyonu ve gaz-gaita '
                  'çıkaramama aksi kanıtlanana kadar adezyona bağlı mekanik ince bağırsak obstrüksiyonudur (ileus). '
                  'Ayakta direkt batın grafisinde (ADBG) santral yerleşimli dilate ince bağırsak ansları ve merdiven '
                  'basamağı tarzında multipl hava-sıvı seviyeleri patognomoniktir; kolonda gaz görülmez. Temel acil '
                  'yaklaşım: oral alımı durdurmak, geniş lümenli nazogastrik sondayla aktif dekompresyon ve izotonik '
                  'kristaloid ile agresif hidrasyon sağlamaktır. Strangülasyon veya perforasyon riski yakından '
                  'izlenir.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Karnında aşırı şişkinlik, safralı kusma, gaz ve gaita çıkaramama ile kramp tarzı karın ağrısı',
    'disposition': 'Sarı Alanda Nazogastrik Dekompresyon + Damar Yolu + IV Sıvı Resüsitasyonu + Çocuk Cerrahisi ile '
                   'Yatış',
    'final_diagnosis': 'Adezyona Bağlı Mekanik İntestinal Obstrüksiyon (İleus)',
    'gender': 'Kız',
    'history': 'Beş yaşındaki kız çocuğu ailesi tarafından Sarı Alana getiriliyor: Bir yıl önce perfore apandisit '
               'nedeniyle açık cerrahi operasyon geçirmiş. Dün akşam başlayan kramp tarzı aralıklı karın ağrısı ve '
               'bugün sabah eklenen koyu yeşil safralı kusmaları olmuş. Son 24 saattir hiç gaz ve gaita çıkarmamış. '
               'Karnı davul gibi şişmiş ve ağızdan aldığı her yudum suyu derhal safrayla kusuyor.',
    'id': 'Y51',
    'steps': [ { 'options': [ { 'explanation': 'Eski batın skarı adezyon riskini gösterir. Distandü timpanik batın, '
                                               'metalik çınlama tarzında hiperaktif veya hipoaktif bağırsak sesleri '
                                               'mekanik ileus muayenesinin temel özellikleridir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.5°C, KTA 134/dk, SS 28/dk, TA 94/58 mmHg, SpO2 '
                                               '%98, KDZ 2.5 sn. Sağ alt kadranda eski laparotomi insizyon skarı '
                                               'mevcut. Batın belirgin distandü, timpanik, metalik tınlama veren '
                                               'bağırsak sesleri alınıyor; yaygın hassasiyet var ancak defans ve '
                                               'rebound yok. Rektal ampulla boş.',
                                'text': 'Eski insizyon skarı, batın distansiyonu, bağırsak sesleri ve dehidratasyon '
                                        'bulgularını sistemik muayene ile değerlendirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Mekanik obstrüksiyonda uygulanan yüksek basınçlı lavman şiddetli '
                                                   'ağrı krizine ve bağırsak perforasyonu riskine yol açtı.',
                                'teaching_point': 'Mekanik ince bağırsak obstrüksiyonlarında retrograd lavman '
                                                  'verilmesi basıncı artırarak perforasyona neden olur; '
                                                  'KONTRENDİKEDİR.',
                                'text': 'Gaz çıkaramadığı için fizik muayene yapmadan hastaya derhal yüksek basınçlı '
                                        'rektal sabunlu lavman uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'İçirilen laksatif mide ve proksimal bağırsak basıncını patlama '
                                                   'noktasına getirerek masif safralı kusmayı tetikledi.',
                                'teaching_point': 'Tıkalı bağırsak lümenine oral yoldan besin veya laksatif verilmesi '
                                                  'lümen içi basıncı artırarak gangrene yol açar.',
                                'text': 'Kusmayı durdurmak amacıyla oral yoldan katı gıdalar ve yüksek doz posalı '
                                        'laksatif şuruplar içirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Antispazmodik verilmesi bağırsak düz kaslarını felç ederek mekanik '
                                                   'tabloyu paralitik iskemiye çevirdi.',
                                'teaching_point': 'Mekanik obstrüksiyonda antispazmodikler bağırsak tonusunu ve '
                                                  'perfüzyonunu bozar; kesinlikle verilmemelidir.',
                                'text': 'Karın ağrısının bağırsak spazmı olduğunu varsayarak hiçbir görüntüleme '
                                        'planlamadan hastaya güçlü antispazmodik enjekte etmek'}],
                 'question': 'Geçirilmiş apandisit operasyonu, safralı kusma ve gaz çıkaramama öyküsü olan bu çocukta '
                             'ilk muayene yaklaşımı ne olmalıdır?',
                 'stage_title': 'Sarı Alanda İlk Triyaj ve Obstrüksiyon Muayenesi'},
               { 'options': [ { 'explanation': 'Ayakta direkt batın grafisi (ADBG) mekanik obstrüksiyon tanısında ilk '
                                               'tercihtir; dilate ince bağırsak ansları, merdiven basamağı hava-sıvı '
                                               'seviyeleri ve distal kolonda gaz yokluğu tanıyı kanıtlar.',
                                'image': 'assets/images/adbg_air_fluid.png',
                                'is_correct': True,
                                'new_finding': 'Ayakta Direkt Batın Grafisi (ADBG): Santral yerleşimli dilate ince '
                                               'bağırsak ansları, tipik merdiven basamağı tarzında multipl hava-sıvı '
                                               'seviyeleri izlendi; kolonda gaz izlenmedi, subdiafragmatik serbest '
                                               'hava saptanmadı. Laboratuvar: Lökosit 12.800/mm³, Na 134 mEq/L, K 3.4 '
                                               'mEq/L, Klor 96 mEq/L, Üre 44 mg/dL.',
                                'text': 'İnce bağırsak genişlemesini ve olası hava-sıvı seviyelerini görmek için acil '
                                        'ayakta direkt batın grafisi çekmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Obstrükte bağırsakta baryum proksimalde göllendi ve çocuk masif '
                                                   'baryumu aspire ederek yoğun bakıma kaldırıldı.',
                                'teaching_point': 'İnce bağırsak obstrüksiyonunda oral baryum verilmesi kesinlikle '
                                                  'kontrendikedir; aspirasyon ve peritonit yapar.',
                                'text': 'Radyolojik grafi çekmeden önce hastaya yüksek doz oral baryum içirerek tüm '
                                        'bağırsağı kontrastla doldurmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Grafi çekilmediği için mekanik tıkanıklık tanısı gecikti ve '
                                                   'bağırsak anslarında vasküler boğulma başladı.',
                                'teaching_point': 'Safralı kusan ve distandü batını olan hastada acil ADBG çekilerek '
                                                  'obstrüksiyon ve perforasyon hızla dışlanmalıdır.',
                                'text': 'Direkt grafi çekmek yerine sadece idrar kültürü alıp 48 saat sonraki sonuca '
                                        'göre hareket etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Distandü ve hipovolemik hastada anestezi indüksiyonunda aspirasyon '
                                                   've kardiyovasküler instabilite yaşandı.',
                                'teaching_point': 'İnce bağırsak adezyon ileusunda kolonoskopi tanısal değildir ve '
                                                  'obstrükte hastada aşırı risklidir.',
                                'text': 'Hastaya genel anestezi verip radyoloji olmaksızın sadece kolonoskopi ile '
                                        'ileumu incelemeye çalışmak'}],
                 'question': 'Mekanik ileus şüphesi olan bu çocukta obstrüksiyon seviyesini ve serbest havayı '
                             'değerlendirmek için en uygun radyolojik tetkik hangisidir?',
                 'stage_title': 'Radyolojik ve Laboratuvar İncelemeleri'},
               { 'options': [ { 'explanation': 'Geçirilmiş batın cerrahisi skarı, safralı kusma, gaz-gaita çıkışının '
                                               "durması ve ADBG'de multipl hava-sıvı seviyeleri adezyon ileusunu "
                                               'kesinleştirir.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Geçirilmiş Cerrahiye Sekonder Adezyona Bağlı Mekanik '
                                               'İntestinal Obstrüksiyon.',
                                'text': 'Adezyona bağlı mekanik intestinal obstrüksiyon'},
                              { 'is_correct': False,
                                'scenario_update': 'Gastroenteritte bol sulu ishal beklenir; bu hastada gaz-gaita '
                                                   'çıkışı tamamen durmuş ve mekanik hava-sıvı seviyeleri '
                                                   'saptanmıştır.',
                                'teaching_point': 'Gastroenterit aşırı ishal yapar; gaz ve gaita çıkaramama ile '
                                                  'multipl hava-sıvı seviyeleri mekanik obstrüksiyona özgüdür.',
                                'text': 'Akut toksik rotavirüs gastroenteriti'},
                              { 'is_correct': False,
                                'scenario_update': 'Primer peritonitte yaygın defans ve asit bulunur; geçirilmiş '
                                                   'operasyon zemininde mekanik lümen tıkanıklığı ve hava-sıvı '
                                                   'seviyeleri olmaz.',
                                'teaching_point': 'Primer peritonit asitli hastalarda görülür; mekanik ileus mekanik '
                                                  'bir bant tıkanıklığıdır.',
                                'text': 'Primer bakteriyel peritonit enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Kabızlıkta safralı fışkırır kusma, distandü ince bağırsaklar ve '
                                                   "ADBG'de hava-sıvı seviyeleri izlenmez.",
                                'teaching_point': 'Yeşil safralı kusma kabızlık semptomu olamaz; mutlaka ince bağırsak '
                                                  'düzeyindeki obstrüksiyonu işaret eder.',
                                'text': 'Basit çocukluk çağı kabızlığı'}],
                 'question': "Geçirilmiş cerrahi, safralı kusma, distansiyon ve ADBG'de merdiven basamağı hava-sıvı "
                             'seviyeleri ile kesin tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Mekanik ileusta oral alım durdurulmalı, nazogastrik sonda serbest '
                                               'drenaja alınmalı, üçüncü boşluk kayıpları izotonik kristaloid ile '
                                               'karşılanmalı ve çocuk cerrahisi tarafından acil eksplorasyon veya '
                                               'dekompresyon takibine alınmalıdır.',
                                'is_correct': True,
                                'new_finding': '10 Fr nazogastrik sonda takılarak serbest drenaja alındı, 120 mL '
                                               'safralı mide içeriği drene edildi ve karın gerginliği azaldı. İzotonik '
                                               'sıvı replasmanı başlandı. Çocuk cerrahisi servisine yatırılarak yakın '
                                               'batın muayenesi takibine alındı.',
                                'text': 'Geniş lümenli nazogastrik sonda ile aktif mide dekompresyonu sağlamak, '
                                        'izotonik sıvı infüzyonuyla cerrahiye yatırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Oral sıvı verilen çocuk tekrar safralı kustu ve mide içeriğini '
                                                   'aspire ederek asfiksiye girdi.',
                                'teaching_point': 'Mekanik obstrüksiyonda oral hidrasyon KONTRENDİKEDİR; nazogastrik '
                                                  'dekompresyon hayat kurtarıcıdır.',
                                'text': 'Nazogastrik sonda takmadan hastaya oral yoldan bol elma suyu içirip eve '
                                        'göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Cerrahi takibe alınmayan hastanın bağırsak duvarında iskemi ve '
                                                   'nekroz gelişti; acil rezeksiyon gerekti.',
                                'teaching_point': 'Adezyon ileusu strangülasyon riski taşır; çocuk cerrahisi takibinde '
                                                  'olmadan acilde bekletilemez.',
                                'text': 'Cerrahi konsültasyon istemeden hastayı 48 saat boyunca acil serviste oral '
                                        'antibiyotikle takip etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Mekanik tıkalı lümene prokinetik verilmesi intralüminal basıncı '
                                                   'fırlatarak bağırsak ansının patlamasına yol açtı.',
                                'teaching_point': 'Mekanik tıkanıklıkta prokinetik ajanlar perforasyon riskini '
                                                  'artırır; kesinlikle KONTRENDİKEDİR.',
                                'text': 'Bağırsağı zorla çalıştırmak amacıyla hastaya intravenöz yüksek doz prokinetik '
                                        'eritromisin ve neostigmin vermek'}],
                 'question': 'Mekanik obstrüksiyon tanısı doğrulanan bu çocukta Sarı Alanda uygulanacak en uygun acil '
                             'yönetim stratejisi hangisidir?',
                 'stage_title': 'Dekompresyon, Sıvı Resüsitasyonu ve Cerrahi İzlem'}]},
  { 'age': '8 Yaşında',
    'case_pearl': 'Geniş spektrumlu antibiyotik kullanımı (sefalosporinler, klindamisin, aminopenisilinler) sonrası '
                  'veya esnasında gelişen ağır ishal ve ateşte Clostridioides difficile enfeksiyonu (CDI) '
                  'düşünülmelidir. Toksin A (enterotoksin) ve Toksin B (sitotoksin) mukozal nekroz ve '
                  'pseudomembranlara yol açar. Ağır olgularda belirgin lökositoz (>15.000-25.000/mm³), hipoalbüminemi '
                  've karın distansiyonu görülür. En korkulan komplikasyon toksik megakolon ve perforasyondur. Tanı '
                  'dışkıda C. difficile toksin A/B veya GDH/PCR ile doğrulanır. Motilite azaltıcı ilaçlar (loperamid '
                  'vb.) toksin retansiyonuna ve fatal perforasyona yol açtığı için KESİNLİKLE YASAKTIR! İlk tercih '
                  'oral vankomisin veya fidaksomisindir.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Geniş spektrumlu antibiyotik tedavisi sonrası başlayan şiddetli kanlı ishal, yüksek ateş ve karında '
                 'gerginlik',
    'disposition': 'Sarı Alanda Temas İzolasyonu + Oral Vankomisin Tedavisi + Toksik Megakolon ve Perforasyon Takibi '
                   'ile Yatış',
    'final_diagnosis': 'Clostridioides difficile İlişkili Pseudomembranöz Kolit (Ağır Toksik Kolit)',
    'gender': 'Erkek',
    'history': 'Sekiz yaşındaki erkek çocuk ailesi tarafından Sarı Alana getiriliyor: On gün önce komplike sinüzit '
               'nedeniyle oral amoksisilin-klavulanat ve ardından sefiksim kullanmış. İlaçların bitiminden 3 gün sonra '
               'günde 10-12 kez çıkan, aşırı kötü kokulu, mukuslu ve kanlı ishal başlamış. Karın ağrısı çok şiddetli, '
               'ateşi evde 39.1°C ölçülmüş ve karnı son 12 saatte belirgin şekilde gerilip şişmiş.',
    'id': 'Y52',
    'steps': [ { 'options': [ { 'explanation': 'Antibiyotik öyküsü, toksik görünüm, kolon trasesi boyunca hassasiyet '
                                               've batın distansiyonu Clostridioides difficile kaynaklı toksik kolit '
                                               'açısından kritik öneme sahiptir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 38.9°C, KTA 128/dk, SS 24/dk, TA 102/62 mmHg, '
                                               'SpO2 %98. Çocuk toksik ve bitkin görünüyor. Batın distandü, timpanik, '
                                               'kolon trasesi boyunca yaygın hassasiyet ve istemli defans mevcut; '
                                               'belirgin rebound saptanmadı. Rektal tuşede aşırı pis kokulu, mukuslu '
                                               've kanlı gaita izlendi.',
                                'text': 'İlaç anamnezini derinleştirmek, sistemik toksisite bulgularını, batın '
                                        'distansiyonunu ve periton irritasyonunu muayene etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Ağır koliti olan hasta evde toksik megakolon ve kolonik '
                                                   'perforasyon tablosuna girdi.',
                                'teaching_point': 'Yüksek ateş, distansiyon ve kanlı dışkı basit antibiyotik ishali '
                                                  'değil; hayatı tehdit eden C. diff kolitidir.',
                                'text': 'İshalin antibiyotik yan etkisi olduğunu söyleyerek muayene yapmadan hastayı '
                                        'evine gönderip ilacı kesmesini söylemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Loperamid verilmesi toksinlerin kolonda hapsolmasına, masif '
                                                   'megakolona ve septik şoka yol açtı.',
                                'teaching_point': 'İnflamatuar ve toksik kolitlerde motilite azaltıcı ajanlar toksik '
                                                  'megakolon ve ölüme neden olur; KONTRENDİKEDİR.',
                                'text': 'Karnı şiş olan hastaya peristaltizmi durdurmak için derhal yüksek doz '
                                        'loperamid ve opiat vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Kontrolsüz soğuk sıvı yüklemesi hastada titreme ve hipotermi '
                                                   'krizine yol açtı.',
                                'teaching_point': 'Hemodinamisi stabil olan hastada agresif puşeler değil; sistemik '
                                                  'muayene ve hedefe yönelik tedavi esastır.',
                                'text': 'Ateşi düşürmek için fizik muayene yapmadan hastaya damardan bol miktarda '
                                        'soğuk serum fizyolojik puşelemek'}],
                 'question': 'Geniş spektrumlu antibiyotik sonrası yüksek ateş, şiddetli kanlı ishal ve karın '
                             'distansiyonu olan çocukta ilk yaklaşım ne olmalıdır?',
                 'stage_title': 'Sarı Alanda Antibiyotik Öyküsü ve Toksik Tablo Değerlendirmesi'},
               { 'options': [ { 'explanation': 'Dışkıda C. diff toksin A/B ELISA veya PCR tanı koydurur. Aşırı '
                                               'lökositoz (>15.000/mm³) ve hipoalbüminemi hastalığın şiddet derecesini '
                                               'belirler. Direkt grafi toksik megakolonu tarar.',
                                'is_correct': True,
                                'new_finding': 'Laboratuvar: Lökosit 24.800/mm³ (%86 nötrofil), CRP 94 mg/L, Serum '
                                               'Albümin 2.6 g/dL (hipoalbüminemi). Dışkı Testi: C. difficile Toksin A '
                                               've Toksin B POZİTİF saptandı. Ayakta Batın Grafisi: Transvers kolonda '
                                               'dilatasyon izlendi (çekum çapı 5.2 cm), serbest hava saptanmadı.',
                                'text': 'Dışkıda Clostridioides difficile toksin A ve B antijenlerini aramak, tam kan '
                                        've albümin düzeyini incelemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Şiddetli inflamasyonlu ve nekrotik kolonda yapılan agresif '
                                                   'kolonoskopi iyatrojenik perforasyona yol açtı.',
                                'teaching_point': 'Ağır akut toksik kolitte total kolonoskopi ve mekanik lavman '
                                                  'perforasyon riski nedeniyle KONTRENDİKEDİR.',
                                'text': 'Dışkı tetkiki yapmadan hastaya acil koşullarda tam mekanik bağırsak temizliği '
                                        'eşliğinde total kolonoskopi yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Çölyak paneli beklenirken toksik kolit tablosu derinleşti ve '
                                                   'sepsis gelişti.',
                                'teaching_point': 'Akut antibiyotik ilişkili toksik kanlı ishalde çölyak tespiti '
                                                  'öncelikli değildir; C. diff toksini aranmalıdır.',
                                'text': 'Laboratuvar tetkiklerini reddedip hastaya sadece çölyak antikoru paneli '
                                        'isteyerek sonucu beklemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Tedavi edilmeyen pseudomembranöz kolit 12 saat sonra toksik şoka '
                                                   'ilerledi.',
                                'teaching_point': 'Ağır C. diff koliti agresif medikal tedavi ve yakın hospitalizasyon '
                                                  'gerektirir.',
                                'text': 'Sadece idrar tahlili yaparak hastayı antibiyotik verilmeden Yeşil Alana geri '
                                        'göndermek'}],
                 'question': 'Ağır C. difficile koliti şüphesi olan bu hastada tanıyı doğrulamak ve komplikasyonları '
                             'taramak için en uygun tetkikler hangileridir?',
                 'stage_title': 'Laboratuvar ve Görüntüleme İncelemeleri'},
               { 'options': [ { 'explanation': 'Geniş spektrumlu antibiyotik sonrası yüksek lökositoz, hipoalbüminemi '
                                               've dışkıda toksin A/B pozitifliği ağır C. difficile kolitini kanıtlar.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Clostridioides difficile İlişkili Ağır Pseudomembranöz '
                                               'Kolit.',
                                'text': 'Clostridioides difficile pseudomembranöz koliti'},
                              { 'is_correct': False,
                                'scenario_update': 'Ülseratif kolit kronik otoimmün bir süreçtir; antibiyotik sonrası '
                                                   'akut başlayan toksin pozitifliğini açıklamaz.',
                                'teaching_point': 'Ülseratif kolitte C. diff süperenfeksiyonu olabilir ancak primer '
                                                  'neden toksin A/B pozitif kolittir.',
                                'text': 'Akut ülseratif kolit alevlenmesi'},
                              { 'is_correct': False,
                                'scenario_update': 'Shigella gıda/su kaynaklı salgın yapar; geniş spektrumlu '
                                                   'antibiyotik maruziyeti ve C. diff toksini ile uyumlu değildir.',
                                'teaching_point': 'Antibiyotik sonrası flora kaybına bağlı tablolarda Shigella değil, '
                                                  'C. diff baş sorumludur.',
                                'text': 'Shigella sonnei basil dizanterisi'},
                              { 'is_correct': False,
                                'scenario_update': 'Amipli dizanteride C. diff toksinleri saptanmaz ve antibiyotik '
                                                   'sonrası masif lökositoz beklenmez.',
                                'teaching_point': 'Amipli dizanteride lökositoz hafiftir; 25.000 lökosit ve '
                                                  'antibiyotik öyküsü C. diff kolitine özgüdür.',
                                'text': 'Basit amip kaynaklı dizanteri'}],
                 'question': 'Antibiyotik öyküsü, toksisite, masif lökositoz ve gaitada C. difficile toksin '
                             'pozitifliği ile kesin klinik tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Pediatrik IDSA kılavuzlarına göre ağır CDI olgularında ilk seçenek '
                                               'ORAL VANKOMİSİN (10 mg/kg/doz, günde 4 kez, maksimum 500 mg/gün) veya '
                                               'oral fidaksomisindir. İV vankomisin kolon lümenine geçmez! Motilite '
                                               'azaltıcılar yasaktır.',
                                'is_correct': True,
                                'new_finding': 'Hasta tek kişilik odaya alınarak temas izolasyonu uygulandı. Oral '
                                               'vankomisin (40 mg/kg/gün 4 doza bölünerek) başlandı. İntravenöz '
                                               'hidrasyon sağlandı. 48 saat içinde ateş düştü, lökositoz geriledi ve '
                                               'kolon çapı normale döndü.',
                                'text': 'Temas izolasyonu uygulayarak oral vankomisin tedavisi başlamak ve motilite '
                                        'azaltıcı ajanlardan kesinlikle kaçınmak'},
                              { 'is_correct': False,
                                'scenario_update': 'İntravenöz vankomisin kolon lümenine salgılanmadığı için kolitte '
                                                   'hiçbir iyileşme sağlanamadı.',
                                'teaching_point': 'İV vankomisin bağırsak lümenine geçmez; C. difficile kolitinde '
                                                  'vankomisin MUTLAKA ORAL yoldan verilmelidir.',
                                'text': 'İlacın kolona daha hızlı ulaşması amacıyla sadece damardan intravenöz '
                                        'vankomisin infüzyonu uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Verilen antibiyotik florayı daha da yok etti, loperamid toksik '
                                                   'megakolona ve cerrahi rezeksiyona yol açtı.',
                                'teaching_point': "Loperamid CDI'de toksik megakolon riskini katlar; etken antibiyotik "
                                                  'derhal kesilmelidir.',
                                'text': 'İshali hemen durdurmak için hastaya yüksek doz loperamid ve parenteral '
                                        'amoksisilin başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Ağır koliti olan hasta evde hipovolemik şok ve kolon nekrozuna '
                                                   'ilerledi.',
                                'teaching_point': 'Ağır C. diff koliti probiyotikle iyileşmez; hedefe yönelik oral '
                                                  'vankomisin şarttır.',
                                'text': 'Hiçbir antibiyotik vermeden hastaya sadece bol miktarda yoğurt yedirip evine '
                                        'taburcu etmek'}],
                 'question': 'Ağır C. difficile koliti saptanan bu çocukta Sarı Alanda başlanacak en uygun kanıta '
                             'dayalı tedavi hangisidir?',
                 'stage_title': 'Hedefe Yönelik Antimikrobiyal Tedavi ve İzolasyon'}]},
  { 'age': '11 Yaşında',
    'case_pearl': 'Pediatrik akut pankreatit insidansı giderek artmaktadır. NASPGHAN kriterlerine göre tanı için 3 '
                  "kriterden en az 2'si gereklidir: 1) Karakteristik karın ağrısı (epigastrik, sırta vuran, öne "
                  'eğilmekle hafifleyen), 2) Serum amilaz veya lipaz düzeyinin normalin üst sınırının EN AZ 3 KATI '
                  'olması (lipaz daha duyarlı ve özgüldür), 3) Görüntülemede (USG/BT) pankreatit bulguları. '
                  'Etiyolojide safra taşları, ilaçlar (valproat, asparaginaz, azatioprin vb.), enfeksiyonlar ve travma '
                  'yer alır. Tedavide en kritik adım: ilk 24 saatte agresif hedefe yönelik izotonik kristaloid (SF '
                  'veya Ringer Laktat) infüzyonu ile mikrovasküler perfüzyonun korunması, etkili analjezi ve tolere '
                  'edilir edilmez erken enteral beslenmedir.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Epigastriumda başlayıp sırta kuşak tarzında yayılan şiddetli karın ağrısı, inatçı kusma ve kıvranma',
    'disposition': 'Sarı Alanda İki Damar Yolu + Agresif İzotonik Hidrasyon + İntravenöz Analjezi ve Pediatri '
                   'Servisine Yatış',
    'final_diagnosis': 'Akut Pediatrik Pankreatit (Ödematöz İnterstisyel Form)',
    'gender': 'Kız',
    'history': 'On bir yaşındaki kız çocuk ailesi tarafından Sarı Alana getiriliyor: Dün akşam başlayan, göbeğin üst '
               'kısmında yerleşip sırta doğru bıçak gibi vuran çok şiddetli karın ağrısı tarifliyor. Hasta öne eğilip '
               'dizlerini göğsüne çektiğinde ağrısının bir miktar hafiflediğini, sırtüstü yattığında ise ağrının '
               'dayanılmaz olduğunu söylüyor. Beş kez safrasız mide içeriği kusmuş, ağızdan su bile içemiyor ve '
               'kıvranıyor.',
    'id': 'Y53',
    'steps': [ { 'options': [ { 'explanation': 'Öne eğilmekle hafifleyen epigastrik ve sırta vuran kuşak tarzı ağrı '
                                               'pankreatit için karakteristiktir. Epigastrik hassasiyet ve peritoneal '
                                               'bulgular araştırılmalıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.7°C, KTA 122/dk, SS 24/dk, TA 108/68 mmHg, '
                                               'SpO2 %99. Hasta muayene sedyesinde öne eğilmiş pozisyonda oturuyor. '
                                               'Batın muayenesinde epigastrik bölgede belirgin palpasyon hassasiyeti '
                                               've istemsiz savunma mevcut; yaygın rebound veya peritonit yok. '
                                               'Bağırsak sesleri hipoaktif.',
                                'text': 'Ağrının lokalizasyonunu, yayılımını, pozisyonla ilişkisini inceleyip batın '
                                        'muayenesinde epigastrik hassasiyet ve defansı değerlendirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Sırtüstü yatırılma peripankreatik retroperitoneal gerilimi '
                                                   'artırarak hastanın ağrıdan bayılmasına yol açtı.',
                                'teaching_point': 'Pankreatitli hastalar öne eğilerek rahatlar; zorla sırtüstü '
                                                  'yatırılması ağrıyı katastrofik derecede şiddetlendirir.',
                                'text': 'Ağrıyı incelemeden çocuğu zorla sırtüstü düz yatırıp karnına sertçe ve aniden '
                                        'bastırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Oral antiasit verilen hasta anında kustu ve dehidratasyona bağlı '
                                                   'taşikardisi derinleşti.',
                                'teaching_point': 'Sırta vuran şiddetli epigastrik ağrı basit gastrit değildir; '
                                                  'pankreatit ve cerrahi aciller araştırılmalıdır.',
                                'text': 'Kusmayı basit gastrit kabul edip hiçbir muayene yapmadan oral antiasit '
                                        'çiğneterek Yeşil Alana göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Üst batın muayene edilmediği için pankreatit kliniği gözden kaçtı '
                                                   've hasta yanlışlıkla apendektomiye hazırlandı.',
                                'teaching_point': 'Çocuklarda karın muayenesi tüm kadranları, epigastriumu ve böbrek '
                                                  'lojlarını eksiksiz kapsamalıdır.',
                                'text': 'Ağrının apandisite bağlı olduğunu varsayıp sadece sağ alt kadrana odaklanarak '
                                        'üst batını tamamen atlamak'}],
                 'question': 'Epigastrik ağrısı sırta vuran ve öne eğilerek oturan bu çocukta ilk fizik muayene '
                             'yaklaşımı nasıl olmalıdır?',
                 'stage_title': 'Sarı Alanda Pozisyonel Ağrı Karakteri ve Batın Muayenesi'},
               { 'options': [ { 'explanation': 'Lipaz ve amilazın normal üst sınırın ≥3 katı olması tanı koydurur '
                                               '(lipaz daha duyarlıdır). Batın USG ödemli pankreası, peripankreatik '
                                               'sıvıyı ve bilier etiyolojiyi (kolelitiyazis) tarar.',
                                'is_correct': True,
                                'new_finding': 'Biyokimya: Serum Lipaz 1380 U/L (normalin 23 katı), Serum Amilaz 860 '
                                               'U/L (normalin 8 katı), ALT 32 U/L, AST 38 U/L, Kalsiyum 8.9 mg/dL, '
                                               'Trigliserid normal. Lökosit 13.400/mm³, CRP 36 mg/L. Batın USG: '
                                               'Pankreas gövde ve kuyruğunda diffüz hipoekoik ödematöz büyüme ve '
                                               'minimal peripankreatik serbest sıvı izlendi; safra kesesi ve yolları '
                                               'doğal.',
                                'text': 'Serum amilaz ve lipaz düzeylerini ölçmek, karaciğer enzimleri ve kalsiyum ile '
                                        'birlikte batın ultrasonografisi istemek'},
                              { 'is_correct': False,
                                'scenario_update': 'İlk 24 saatte çekilen tomografi nekrozu gösteremediği gibi hastayı '
                                                   'gereksiz yüksek radyasyona maruz bıraktı.',
                                'teaching_point': 'Pankreatitin ilk 48-72 saatinde BT nekrozu ayırt edemez; tanı '
                                                  'enzimler ve USG ile konur, erken rutin BT endike değildir.',
                                'text': 'Enzim testlerine gerek görmeden hastaya derhal yüksek radyasyonlu kontrastlı '
                                        'tüm vücut tomografisi çekmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Pankreatit enzimlerine bakılmadığı için tanı atlandı ve agresif '
                                                   'sıvı resüsitasyonu gecikti.',
                                'teaching_point': 'Şiddetli epigastrik ağrıda amilaz ve lipaz bakılması tanının '
                                                  'olmazsa olmaz ilk basamağıdır.',
                                'text': 'Pankreas enzimlerini istemeden sadece gaitada parazit mikroskopisi yaparak '
                                        'hastayı gözlem odasına almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Akciğer grafisi normal geldi ancak karındaki pankreas ödemi tespit '
                                                   'edilemedi.',
                                'teaching_point': 'Akut pankreatit karın içi inflamasyondur; toraks grafisi primer '
                                                  'tanı yöntemi olamaz.',
                                'text': 'Sadece akciğer grafisi çekip kardiyotorasik orana bakarak taburculuk kararı '
                                        'vermek'}],
                 'question': 'Akut pankreatit şüphesi olan bu hastada tanıyı doğrulamak için yapılması gereken en '
                             'uygun tetkik kombinasyonu hangisidir?',
                 'stage_title': 'Laboratuvar ve Görüntüleme İncelemeleri'},
               { 'options': [ { 'explanation': 'Karakteristik epigastrik ağrı, serum lipazının normalin 3 katından '
                                               'belirgin yüksek olması ve USG bulguları akut pankreatiti '
                                               'kesinleştirir.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Akut Pediatrik İnterstisyel Ödematöz Pankreatit.',
                                'text': 'Akut interstisyel ödematöz pankreatit'},
                              { 'is_correct': False,
                                'scenario_update': "Peptik ülserde lipaz 1380 U/L düzeyine çıkmaz ve USG'de diffüz "
                                                   'pankreas ödemi izlenmez.',
                                'teaching_point': 'Peptik ülser amilazı hafif yükseltebilir ancak lipazın 3 katı '
                                                  'aşması pankreatite özgüdür.',
                                'text': 'Akut gastroduodenal peptik ülser'},
                              { 'is_correct': False,
                                'scenario_update': 'Kolesistitte sağ üst kadranda Murphy belirtisi ve safra kesesi '
                                                   "duvar kalınlaşması olur; USG'de safra kesesi doğal bulundu.",
                                'teaching_point': 'Kolesistit safra kesesi inflamasyonudur; bu olguda patoloji izole '
                                                  'pankreas parankimindedir.',
                                'text': 'Akut taşlı kolesistit atağı'},
                              { 'is_correct': False,
                                'scenario_update': 'Apandisitte ağrı sağ alt kadrana yerleşir; sırta vuran epigastrik '
                                                   'ağrı ve lipaz yüksekliği yapmaz.',
                                'teaching_point': 'Apandisit alt kadran hastalığıdır; amilaz/lipazı normal sınırlar '
                                                  'içinde seyreder.',
                                'text': 'Akut flegmonöz apandisit tablosu'}],
                 'question': "Sırta yayılan epigastrik ağrı, lipaz düzeyinin >3 kat artışı ve USG'de ödematöz pankreas "
                             'ile kesin tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Pediatrik pankreatit tedavisinin temel taşı ilk 24 saatte hedefe '
                                               'yönelik izotonik sıvı infüzyonudur (idamenin 1.5-2 katı). Ağrı '
                                               'kontrolü için parenteral analjezikler (tramadol/fentanil) verilir. '
                                               'Tolere edilir edilmez erken enteral beslenme başlatılır.',
                                'is_correct': True,
                                'new_finding': 'İki damar yolu açıldı, 1.5 kat idame hızında izotonik kristaloid '
                                               'başlandı. İntravenöz analjezi ile ağrısı dindirildi. Kusması durduktan '
                                               'sonra düşük yağlı enteral beslenmeye geçildi ve komplikasyonsuz '
                                               'iyileşerek taburcu edildi.',
                                'text': 'İntravenöz izotonik kristaloid infüzyonu ile hidrasyonu sağlamak, opioid '
                                        'analjezi uygulamak ve klinik gözleme almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Sıvı verilmeyen hastada pankreatik mikrosirkülasyon bozuldu ve '
                                                   'ödematöz tablo nekrotizan pankreatite dönüştü.',
                                'teaching_point': 'Sıvı kısıtlaması pankreatik nekrozu tetikler; agresif hidrasyon '
                                                  'nekrozu önleyen en kritik tedavidir.',
                                'text': 'Pankreası dinlendirmek amacıyla hastayı iki hafta boyunca tamamen aç bırakıp '
                                        'hiçbir sıvı vermemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Şiddetli ağrı hastada sempatik fırtınaya, hipertansiyona ve derin '
                                                   'ajitasyona yol açtı.',
                                'teaching_point': 'Pankreatit ağrısı çok şiddetlidir; analjezi verilmesi insani ve '
                                                  'tıbbi bir zorunluluktur.',
                                'text': 'Ağrıyı maskelememek adına hastaya hiçbir ağrı kesici ilaç vermeden '
                                        'kıvranmasını beklemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz profilaktik antibiyotik dirençli fungal enfeksiyon '
                                                   'gelişimine zemin hazırladı.',
                                'teaching_point': 'Akut ödematöz pankreatitte profilaktik antibiyotik kullanımının '
                                                  'yeri yoktur; kılavuzlarca önerilmez.',
                                'text': 'Enfeksiyonu önlemek için ampirik profilaktik en geniş spektrumlu karbapenem '
                                        'antibiyotik infüzyonu başlatmak'}],
                 'question': 'Akut pankreatit tanısı konulan bu hastada Sarı Alanda uygulanacak en uygun tedavi ve '
                             'hidrasyon protokolü hangisidir?',
                 'stage_title': 'Sıvı Resüsitasyonu, Analjezi ve Klinik Yönetim'}]},
  { 'age': '2 Aylık',
    'case_pearl': 'Hirschsprung ilişkili enterokolit (HAEC), Hirschsprung hastalığının en korkulan ve ölümcül '
                  "komplikasyonudur (%30'a varan mortalite). Mekonyum gecikmesi (>24-48 saat) veya kronik kabızlık "
                  'öyküsü olan bebekte batın distansiyonu, ateş, letarji ve ardından PATLAYICI PİS KOKULU İSHAL '
                  'gelişmesi tipiktir. Distal aganglionik segmentteki spazma bağlı proksimal kolonda staz, bakteriyel '
                  'aşırı çoğalma, mukozal bariyer yıkımı, translokasyon ve sepsis gelişir. Rektal tuşede sfinkter '
                  'hipertoniktir; parmak çekilince patlayıcı gaz ve gaita fışkırır (pozitif blast sign). Tedavide '
                  'hayat kurtarıcı adım: nazogastrik dekompresyon, IV sıvı, geniş spektrumlu antibiyotik '
                  '(ampisilin+gentamisin+metronidazol) ve geniş lümenli kateterle ılık SF ile REKTAL İRRİGASYON '
                  '(yıkayarak dekompresyon sağlama) dur.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Karnında aşırı şişkinlik, safralı kusma, patlayıcı pis kokulu ishal, ateş ve solukluk',
    'disposition': 'Sarı Alanda Nazogastrik Dekompresyon + Geniş Spektrumlu IV Antibiyotik + Rektal İrrigasyon ve '
                   'Yoğun Bakım',
    'final_diagnosis': 'Hirschsprung Hastalığı İlişkili Toksik Enterokolit (HAEC)',
    'gender': 'Erkek',
    'history': 'İki aylık erkek bebek ailesi tarafından Sarı Alana getiriliyor: Doğumda ilk mekonyumunu 48 saatten '
               "sonra zorla çıkarmış ve sonrasında sürekli kabızlık çekmiş. Dün aniden ateşi 38.8°C'ye çıkmış, karnı "
               'balon gibi şişmiş ve bugün fışkırır tarzda yeşil safralı kusmanın ardından bezinden patlayıcı, '
               'fışkırır tarzda aşırı pis kokulu sulu gaita gelmeye başlamış. Bebek iniltili nefes alıyor ve soluk '
               'görünüyor.',
    'id': 'Y54',
    'steps': [ { 'options': [ { 'explanation': 'Mekonyum gecikmesi Hirschsprung zeminini gösterir. Batın distansiyonu, '
                                               'fışkırır pis kokulu ishal ve ateş hayatı tehdit eden enterokolit '
                                               '(HAEC) ve sepsis bulgusudur.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 38.7°C, KTA 164/dk, SS 46/dk, TA 74/42 mmHg, SpO2 '
                                               '%96, KDZ 3 sn. Bebek iniltili, soluk ve letarjik. Batın ileri derecede '
                                               'distandü, parlak, venöz dolgunluk belirgin. Rektal tuşede anal kanal '
                                               'dar ve hipertonik hissedildi; parmak çıkarıldığında patlayıcı şekilde '
                                               'pis kokulu gaz ve sıvı gaita fışkırdı (blast sign pozitif).',
                                'text': 'Mekonyum çıkış öyküsünü sorgulamak, batın distansiyonunu ölçmek, perfüzyon ve '
                                        'sepsis bulgularını acil incelemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Viral ishal sanılan bebekte aganglionik staz kolonik perforasyona '
                                                   've septik şok arrestine yol açtı.',
                                'teaching_point': 'Mekonyum gecikmesi olan bebekte distandü batın ve patlayıcı ishal '
                                                  'HAEC acilidir; asla basit gastroenterit değildir.',
                                'text': 'Patlayıcı ishali basit viral gastroenterit sanarak bebeğe evde ORS '
                                        'içirilmesini önerip Yeşil Alana göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Motilite azaltıcı verilmesi toksik bakteriyel stazı artırarak 2 '
                                                   'saat içinde kolonu patlattı.',
                                'teaching_point': "HAEC'de motilite azaltıcı ilaçlar kesinlikle KONTRENDİKEDİR; toksik "
                                                  'megakolon ve ölüm yapar.',
                                'text': 'İshali hemen durdurmak için bebeğe yüksek doz loperamid ve bağırsak '
                                        'motilitesini baskılayıcı damla vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Alttaki cerrahi obstrüksiyon çözülmediği için bebeğin asidozu '
                                                   'derinleşti ve solunum durması gelişti.',
                                'teaching_point': "HAEC'de ateş bir sepsis bulgusudur; acil dekompresyon ve "
                                                  'antibiyoterapi hayat kurtarır.',
                                'text': 'Batın distansiyonunu önemsemeyip sadece bebeğin ateşini düşürmek için soğuk '
                                        'kompresle vakit kaybetmek'}],
                 'question': 'Mekonyum gecikmesi, batın distansiyonu, ateş ve patlayıcı pis kokulu ishali olan bu '
                             'bebekte ilk yaklaşım ne olmalıdır?',
                 'stage_title': 'Sarı Alanda Yenidoğan Öyküsü ve Sepsis Şüphesi'},
               { 'options': [ { 'explanation': "HAEC'de laktik asidoz ve lökositoz sepsisi gösterir. Ayakta/sol "
                                               'lateral direkt batın grafisi serbest havayı (pnömoperitoneum) ve '
                                               'bağırsak duvarındaki gazı (pnömatozis) tarar.',
                                'is_correct': True,
                                'new_finding': 'Laboratuvar: Lökosit 21.400/mm³ (sola kayma, %20 çomak), CRP 92 mg/L, '
                                               'Venöz Kan Gazı pH 7.24, Laktat 3.8 mmol/L. Batın Grafisi: Kolonda '
                                               'masif hava distansiyonu, bağırsak duvarında ödem izlendi; '
                                               'subdiafragmatik serbest hava saptanmadı.',
                                'text': 'Kan kültürü, kan gazı ve enfeksiyon belirteçlerini almak ve olası '
                                        'perforasyonu dışlamak için direkt grafi çekmek'},
                              { 'is_correct': False,
                                'scenario_update': 'İnflame ve nekrotik kolonda yüksek basınçlı baryum lavmanı kolon '
                                                   'perforasyonuna ve baryum peritonitine yol açtı.',
                                'teaching_point': 'Akut HAEC tablosunda baryumlu kolon grafisi perforasyon riski '
                                                  'nedeniyle KESİNLİKLE KONTRENDİKEDİR.',
                                'text': 'Radyolojik grafi çekmeden önce bebeğe rektal yoldan yüksek hacimli yoğun '
                                        'baryum lavmanı uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Laboratuvar ve müdahale geciktirilen bebek 6 saat içinde septik '
                                                   'şok nedeniyle kaybedildi.',
                                'teaching_point': 'HAEC saatler içinde mortal seyredebilen hiperakut bir cerrahi '
                                                  'tablodur; anında tedavi edilmelidir.',
                                'text': 'Laboratuvar tetkiki yapmadan hastayı 3 gün sonra çocuk cerrahisi '
                                        'polikliniğine kontrole çağırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Metabolik asidoz ve lökositoz fark edilemediği için sıvı ve '
                                                   'antibiyotik tedavisi yetersiz kaldı.',
                                'teaching_point': 'Septik bebekte kan gazı, laktat ve enfeksiyon parametreleri '
                                                  'resüsitasyonun rehberidir.',
                                'text': 'Sadece idrar tahlili alıp kan gazı ve enfeksiyon belirteçlerini tamamen ihmal '
                                        'etmek'}],
                 'question': 'HAEC şüphesi olan bu septik bebekte perforasyon ve sistemik enfeksiyonu değerlendirmek '
                             'için en uygun tetkikler hangileridir?',
                 'stage_title': 'Laboratuvar ve Görüntüleme İncelemeleri'},
               { 'options': [ { 'explanation': 'Mekonyum gecikmesi zemininde gelişen batın distansiyonu, ateş, '
                                               'patlayıcı pis kokulu ishal ve rektal tuşede fışkırma HAEC tanısıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Hirschsprung Hastalığı Zemininde Akut Toksik Enterokolit '
                                               '(HAEC).',
                                'text': 'Hirschsprung ilişkili toksik enterokolit'},
                              { 'is_correct': False,
                                'scenario_update': 'Rotavirüste mekonyum gecikmesi, aganglionik anal spazm ve '
                                                   'patlayıcı fışkırır blast belirtisi olmaz.',
                                'teaching_point': 'Rotavirüs tipik sulu ishaldir; konjenital aganglionozis ve toksik '
                                                  'distansiyon yapmaz.',
                                'text': 'Akut rotavirüs enfeksiyon ishali'},
                              { 'is_correct': False,
                                'scenario_update': 'NEK prematüre ve düşük doğum ağırlıklı bebeklerin erken dönem '
                                                   'hastalığıdır; 2 aylık term bebekte beklenmez.',
                                'teaching_point': 'Term süt çocuğunda kabızlık sonrası enterokolit NEK değil, '
                                                  'Hirschsprung enterokolitidir.',
                                'text': 'Erken evre nekrotizan enterokolit'},
                              { 'is_correct': False,
                                'scenario_update': 'Anal stenozda anatomik darlık vardır ancak akut toksik '
                                                   'enterokolit, sepsis ve masif kolonik gaz birikimi yapmaz.',
                                'teaching_point': 'Anal stenoz basit anatomik darlıktır; HAEC gibi sistemik toksisite '
                                                  've lökositoz oluşturmaz.',
                                'text': 'Konjenital anal stenoz anomalisi'}],
                 'question': 'Mekonyum gecikmesi, kronik kabızlık, patlayıcı pis kokulu ishal, sepsis ve rektal blast '
                             'belirtisi ile kesin tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'HAEC tedavisinde en kritik hayat kurtarıcı adım geniş lümenli '
                                               'kateterle ılık SF kullanılarak yapılan REKTAL İRRİGASYONDUR (kolonu '
                                               'yıkayarak dekomprese eder). Eş zamanlı geniş spektrumlu IV antibiyotik '
                                               '(ampisilin + gentamisin + metronidazol) ve sıvı resüsitasyonu ile '
                                               'cerrahi yoğun bakıma alınır.',
                                'is_correct': True,
                                'new_finding': '14 Fr rektal tüp nazikçe yerleştirilerek ılık SF ile rektal irrigasyon '
                                               'yapıldı; bol miktarda pis kokulu gaz ve gaita boşaldı, karın '
                                               'distansiyonu hızla söndü. Üçlü IV antibiyotik başlandı. Çocuk '
                                               'cerrahisi yoğun bakımına yatırıldı.',
                                'text': 'Ilık serum fizyolojikle rektal irrigasyon uygulayarak dekompresyon sağlamak, '
                                        'üçlü antibiyotik başlamak ve acil cerrahiye devretmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Dekomprese edilmeyen tıkalı kolonda bakteriyel translokasyon '
                                                   'septik şoka ve ölüme yol açtı.',
                                'teaching_point': "HAEC'de rektal irrigasyon hayat kurtarır; oral antibiyotikle evde "
                                                  'takip fatal bir hatadır.',
                                'text': 'Rektal bölgeye kesinlikle dokunmayıp bebeği sadece oral antibiyotik şurupla '
                                        'evde izlemeye almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Obstrükte ve nekrotik kolona oral laksatif verilmesi masif '
                                                   'bağırsak rüptürüne neden oldu.',
                                'teaching_point': 'Obstrüksiyon ve enterokolitte oral laksatif verilmesi bağırsak '
                                                  'yırtılmasına yol açar.',
                                'text': 'Bebeğe yüksek doz oral laksatif içirerek bağırsağın tüm içeriğini '
                                        'kendiliğinden boşaltmasını beklemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Septik ve dekompanse bebekte rektal lavmansız acil radikal cerrahi '
                                                   'yüksek intraoperatif mortaliteyle sonuçlandı.',
                                'teaching_point': "HAEC'de ilk hedef cerrahi rezeksiyon değil, rektal irrigasyon ve "
                                                  'medikal resüsitasyon ile stabilizasyondur.',
                                'text': 'Acil şartlarda ameliyathaneye alıp rektal lavman yapmadan derhal total '
                                        'kolektomi operasyonu uygulamak'}],
                 'question': 'HAEC tanısı doğrulanan bu bebekte hayat kurtarıcı acil dekompresyon ve tedavi basamağı '
                             'hangisidir?',
                 'stage_title': 'Rektal Dekompresyon, Antibiyoterapi ve Yoğun Bakım'}]},
  { 'age': '4 Yaşında',
    'case_pearl': 'Pediatrik Akut Karaciğer Yetmezliği (PALF) tanı kriterleri: 1) Önceden bilinen kronik karaciğer '
                  'hastalığı olmaması, 2) Biyokimyasal karaciğer hasarı (ALT/AST belirgin yüksekliği), 3) Koagülopati: '
                  'K vitamini uygulanmasına rağmen INR ≥1.5 (ensefalopati varsa) veya INR ≥2.0 (ensefalopati olmasa '
                  'bile). Çocuklarda erken hepatik ensefalopati (Evre 1-2) yetişkinlerden farklı olarak sinsi seyreder '
                  '(uyku düzeninde bozulma, huzursuzluk, hafif konfüzyon). En kritik acil metabolik tehdit '
                  'HİPOGLİSEMİDİR; glukoz depoları tükendiği için %10 dekstroz infüzyonu kesintisiz sürdürülmelidir. '
                  'Aktif masif kanama veya invaziv girişim olmadıkça TAZE DONMUŞ PLAZMA VERİLMEMELİDİR; çünkü TDP '
                  'verilmesi en değerli prognostik parametre olan INR takibini bozar!',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Gözlerde ve ciltte belirgin sararma, sürekli uyuklama hali, inatçı kusma ve karaciğer bölgesinde '
                 'hassasiyet',
    'disposition': 'Sarı Alanda Damar Yolu + IV Glukoz Desteği + K Vitamini + Karaciğer Nakil Merkezi Olan Üniteye '
                   'Acil Sevk',
    'final_diagnosis': 'Pediatrik Akut Karaciğer Yetmezliği (PALF - Erken Hepatik Ensefalopati Evresi)',
    'gender': 'Kız',
    'history': 'Dört yaşındaki kız çocuk ailesi tarafından Sarı Alana getiriliyor: Bir hafta önce halsizlik ve bulantı '
               'başlamış. Son iki günde göz akları ve cildi belirgin sararmış, idrarı koyu çay rengine dönmüş. Bugün '
               'sabah sürekli uyumak istiyor, uyandırıldığında anlamsız bakıyor ve annesini tanımakta güçlük çekiyor. '
               'Diş etlerinde fırçalarken kanama olmuş ve bacaklarında kendiliğinden morluklar oluştuğu fark edilmiş.',
    'id': 'Y55',
    'steps': [ { 'options': [ { 'explanation': 'Hepatik ensefalopati (bilinç dalgalanması), kutanöz/skleral ikter, '
                                               'hepatomegali ve kanama diyatezi (peteşi/ekimoz) karaciğer '
                                               'yetmezliğinin acil klinik belirteçleridir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 110/dk, SS 22/dk, TA 98/58 mmHg, SpO2 '
                                               '%99. Yatak başı kan şekeri: 56 mg/dL (hipoglisemi). Skleralarda ve '
                                               'ciltte derin sarılık izlendi. Çocuk letarjik, sesli uyaranla gözlerini '
                                               'açıyor ancak çevresini tanımıyor (Evre 2 Hepatik Ensefalopati). '
                                               'Karaciğer kot kavsini 4 cm geçiyor, hassas. Bacaklarda ve kollarda '
                                               'dağınık ekimozlar mevcut.',
                                'text': 'Bilinç düzeyini, ensefalopati evresini, ikter derinliğini ve karaciğer '
                                        'sınırlarını dikkatle muayene etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Hipoglisemisi fark edilmeyen letarjik çocuk evde derin '
                                                   'hipoglisemik komaya ve kardiyak arreste girdi.',
                                'teaching_point': 'Dört yaşında sarılık ve letarji asla fizyolojik olamaz; akut '
                                                  'karaciğer yetmezliği acilidir.',
                                'text': 'Sarılığı basit fizyolojik sarılık kabul edip kan şekeri bakmadan hastayı '
                                        'evine dinlenmeye göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Metabolize edilemeyen stimülan ilaçlar hastada taşikardi ve '
                                                   'konvülziyonu tetikledi.',
                                'teaching_point': 'Ensefalopati santral stimülanla düzeltilmez; alttaki amonyak ve '
                                                  'metabolik toksinler temizlenmelidir.',
                                'text': 'Uykulu çocuğu uyandırmak amacıyla hastaya intravenöz yüksek doz kafein ve '
                                        'santral stimülan ilaçlar vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Koagülopatisi olan hasta anesteziye alındığında masif kontrolsüz '
                                                   'cerrahi kanama riski oluştu.',
                                'teaching_point': "PALF'te karaciğer hassasiyeti kapsül gerilmesine bağlıdır; cerrahi "
                                                  'kolesistit değildir.',
                                'text': 'Karaciğer hassasiyetini safra kesesi iltihabı sanarak acil koşullarda '
                                        'ameliyathane hazırlığı başlatmak'}],
                 'question': 'Sarılık, letarji, kusma ve diş eti kanaması olan 4 yaşındaki çocukta ilk klinik '
                             'değerlendirme nasıl olmalıdır?',
                 'stage_title': 'Sarı Alanda Nörolojik Durum ve Hepatomegali Değerlendirmesi'},
               { 'options': [ { 'explanation': 'K vitamini sonrası INR ≥1.5-2.0, transaminaz fırlaması (ALT/AST >1000 '
                                               'U/L), hiperamonyemi ve hipoglisemi pediatrik akut karaciğer '
                                               'yetmezliğini laboratuvar olarak kanıtlar.',
                                'is_correct': True,
                                'new_finding': 'Biyokimya: ALT 2460 U/L, AST 3100 U/L, Total Bilirubin 9.6 mg/dL, '
                                               'Direkt Bilirubin 6.8 mg/dL, Glukoz 56 mg/dL. Koagülasyon: PT 29 sn, '
                                               'INR 2.6 (10 mg K vitamini sonrası kontrol INR 2.5 kaldı). Venöz '
                                               'Amonyak: 118 µmol/L (yüksek). Batın USG: Karaciğerde ekojenite artışı, '
                                               'safra kesesi duvarında ödem izlendi.',
                                'text': 'Transaminazlar, bilirubinler, PT/INR, amonyak ve kan şekerini çalışarak '
                                        'hepatik yetmezliği doğrulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Koagülopati ve hipoglisemi fark edilemediği için hasta '
                                                   'intrakraniyal kanamaya girdi.',
                                'teaching_point': "PALF'te ilk basamak acil testler INR, glukoz, amonyak ve "
                                                  'transaminazlardır; saç analizi anlamsızdır.',
                                'text': 'Koagülasyon ve kan şekeri bakmadan hastaya sadece saç teli analizi yaparak '
                                        'toksin taraması istemek'},
                              { 'is_correct': False,
                                'scenario_update': 'INR 2.6 olan hastada karaciğer biyopsisi masif intraabdominal '
                                                   'ölümcül hemorajiye yol açtı.',
                                'teaching_point': "PALF'te ağır koagülopati nedeniyle perkütan karaciğer biyopsisi "
                                                  'KESİNLİKLE KONTRENDİKEDİR.',
                                'text': 'Laboratuvarı geciktirip kesin tanı için derhal perkütan karaciğer biyopsisi '
                                        'yapmaya çalışmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Takipsiz bırakılan çocukta saatler içinde beyin ödemi ve serebral '
                                                   'herniasyon gelişti.',
                                'teaching_point': 'PALF yoğun bakım ve transplantasyon merkezi koordinasyonu '
                                                  'gerektiren en kritik pediatrik acillerdendir.',
                                'text': 'Sadece idrarda bilirubin arayarak hastayı bir hafta sonraki gastroenteroloji '
                                        'polikliniğine çağırmak'}],
                 'question': 'PALF şüphesi olan bu hastada yetmezlik kriterlerini ve etiyolojiyi doğrulamak için en '
                             'kritik tetkikler hangileridir?',
                 'stage_title': 'Laboratuvar ve Görüntüleme İncelemeleri'},
               { 'options': [ { 'explanation': 'Biyokimyasal karaciğer hasarı, K vitaminiyle düzelmeyen INR >1.5 ve '
                                               'ensefalopati varlığı PALF kriterlerini eksiksiz karşılar.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Akut Hepatit zemininde gelişen Pediatrik Akut Karaciğer '
                                               'Yetmezliği (PALF).',
                                'text': 'Pediatrik akut karaciğer yetmezliği'},
                              { 'is_correct': False,
                                'scenario_update': 'Basit hepatitte karaciğer sentez fonksiyonu korunur, INR normaldir '
                                                   '(<1.3) ve asla ensefalopati gelişmez.',
                                'teaching_point': "INR'nin uzaması ve ensefalopati basit hepatiti yetmezliğe (fulminan "
                                                  'tabloya) dönüştüren alarmdır.',
                                'text': 'Basit selim akut viral hepatit'},
                              { 'is_correct': False,
                                'scenario_update': 'Gilbert sendromunda transaminazlar normaldir, karaciğer hasarı '
                                                   'veya koagülopati görülmez; izole hafif indirekt sarılık vardır.',
                                'teaching_point': 'Gilbert selim enzim eksikliğidir; masif transaminaz yüksekliği ve '
                                                  'koagülopati yapmaz.',
                                'text': 'Akut Gilbert sendromu atağı'},
                              { 'is_correct': False,
                                'scenario_update': 'Hemolizde direkt bilirubin normaldir, ALT/AST binlere çıkmaz ve '
                                                   "karaciğer yetmezliği INR'si görülmez.",
                                'teaching_point': 'Hemolitik anemide indirekt bilirubin yükselir; transaminaz '
                                                  'fırlaması ve koagülopati hepatoselüler hasara özgüdür.',
                                'text': 'İntravasküler otoimmün hemolitik kriz'}],
                 'question': 'Akut sarılık, ALT/AST >2000 U/L, K vitaminiyle düzelmeyen INR 2.5 ve ensefalopati ile '
                             'kesin klinik tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': "PALF'te hipoglisemi derhal %10 Dekstroz (GİR 4-6 mg/kg/dk) ile "
                                               'düzeltilmelidir. Aktif kanama yoksa TDP verilmemeli (INR takibini '
                                               'bozar). Amonyak ve serebral ödem takibi yapılmalı ve hasta acilen '
                                               'karaciğer nakil merkezine devredilmelidir.',
                                'is_correct': True,
                                'new_finding': "İntravenöz %10 Dekstroz infüzyonu başlandı, kan şekeri 105 mg/dL'ye "
                                               'yükseldi. Baş 30 derece eleve edildi. Plazma verilmeden INR takibi '
                                               'korundu. Pediatrik karaciğer nakil yoğun bakımına acil 112 sevki '
                                               'organize edildi.',
                                'text': 'İntravenöz glukoz infüzyonu sağlamak, kafa içi basınç takibi yapmak ve acil '
                                        'karaciğer nakil merkezine sevk etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'TDP verilmesi en kritik prognoz göstergesi olan bazal INR eğrisini '
                                                   'bozdu ve nakil endikasyonunun konmasını engelledi.',
                                'teaching_point': "PALF'te profilaktik TDP verilmesi kılavuzlarca önerilmez; spontan "
                                                  'INR seyrini maskeleyerek nakil kararını geciktirir.',
                                'text': 'INR yüksekliğini sıfırlamak için hastaya aktif kanaması olmasa bile masif '
                                        'taze donmuş plazma infüzyonları yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Karaciğerde metabolize edilemeyen sedatifler hastayı derin komaya '
                                                   'soktu ve solunum depresyonu yarattı.',
                                'teaching_point': 'Hepatik ensefalopatide sedatifler KONTRENDİKEDİR; nörolojik takibi '
                                                  'bozar ve solunumu durdurur.',
                                'text': 'Hastayı sakinleştirmek amacıyla yüksek doz uzun etkili benzodiazepin ve '
                                        'sedatif ilaçlar uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Glukoz desteği kesilen çocukta derin hipoglisemik beyin hasarı ve '
                                                   'irreversibl nöron ölümü gelişti.',
                                'teaching_point': "PALF'te glukoz infüzyonu hayatidir; karaciğer glukoneogenez "
                                                  'yapamadığı için glukozsuz hasta kaybedilir.',
                                'text': 'Karaciğeri dinlendirmek amacıyla damar yolu açmadan hastayı 3 gün sadece su '
                                        'ile beslemek'}],
                 'question': 'PALF tanısı doğrulanan ve hipoglisemisi olan bu hastada Sarı Alanda uygulanacak en doğru '
                             'yönetim protokolü hangisidir?',
                 'stage_title': 'Metabolik Destek, Ensefalopati Yönetimi ve Nakil Merkezi Sevki'}]},
  { 'age': '5 Yaşında',
    'case_pearl': 'Meckel divertikülü omfalomezenterik kanal kalıntısıdır ve sadece rektal kanamayla gelmez! '
                  'Divertikül boynu fekalit, yabancı cisim veya lenfoid hiperplazi ile tıkandığında akut divertikülit '
                  'gelişir ve fizik muayenede akut apandisitten kesinlikle ayırt edilemez. Klinik olarak apandisiti '
                  "düşündüren ancak USG'de apendiksin tamamen normal ve basılabilir olduğu sağ alt kadran "
                  'peritonitlerinde Meckel divertiküliti ilk sırada düşünülmelidir! Divertikül duvarı apendiksten daha '
                  'ince olduğu için perforasyon riski çok daha erkendir. Tedavi acil cerrahi kama rezeksiyonudur.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Sağ alt kadranda şiddetli karın ağrısı, ateş ve periton irritasyonu bulguları',
    'disposition': 'Sarı Alanda Damar Yolu + IV Sıvı ve Antibiyoterapi + Çocuk Cerrahisi ile Acil '
                   'Laparatomi/Laparoskopi',
    'final_diagnosis': 'İnflame Meckel Divertiküliti (Perforasyon Adayı Divertikülit)',
    'gender': 'Erkek',
    'history': 'Beş yaşındaki erkek çocuk ailesi tarafından Sarı Alana getiriliyor: Dün başlayan ve hızla şiddetlenen '
               'sağ alt kadran karın ağrısı ve kusması var. Ateşi evde 38.6°C ölçülmüş. Çocuk akut apandisit ön '
               'tanısıyla değerlendirilirken yapılan apendiks odaklı ultrasonografide retroçekal yerleşimli normal '
               'çapta apendiks görüntülenmiş ancak çocukta sağ alt kadranda belirgin defans, hassasiyet ve periton '
               'irritasyonu devam ediyor.',
    'id': 'Y56',
    'steps': [ { 'options': [ { 'explanation': 'Sağ alt kadran peritonit bulguları cerrahi akut batını kanıtlar. '
                                               'İstemsiz defans ve fokal periton irritasyonu acil müdahaleyi '
                                               'gerektirir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 38.6°C, KTA 132/dk, SS 26/dk, TA 102/64 mmHg, '
                                               'SpO2 %98. Genel durumu orta, çocuk bacaklarını karnına toplayarak '
                                               'yatıyor. Batında sağ alt kadranda istemsiz belirgin defans, McBurney '
                                               'medialinde lokalize şiddetli hassasiyet ve pozitif rebound mevcut; '
                                               'diğer kadranlar rahat.',
                                'text': 'Batın muayenesinde sağ alt kadran hassasiyetini, istemsiz defansı, reboundu '
                                        've peritonit bulgularını sistemik değerlendirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Laksatif verilmesi inflame divertikülün anında delinmesine ve '
                                                   'fekal peritonit sepsisine yol açtı.',
                                'teaching_point': 'Fizik muayenede peritonit varsa görüntüleme normal olsa bile '
                                                  'cerrahi patoloji dışlanamaz; laksatif KONTRENDİKEDİR.',
                                'text': "Apendiks USG'si normal geldiği için peritonit bulgularını yok sayarak hastaya "
                                        'Yeşil Alanda laksatif başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Sarsıntı inflame peritonu uyardı ve çocuk şiddetli ağrı '
                                                   'çığlıklarıyla baygınlık geçirdi.',
                                'teaching_point': 'Akut batın hastası sarsılmamalı ve travmatize edilmemelidir; nazik '
                                                  'muayene esastır.',
                                'text': 'Karın ağrısını ekarte etmek amacıyla çocuğa koşu ve zıplama egzersizleri '
                                        'yaptırarak batını esnetmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Soğuk şoku çocukta periferik vazokonstriksiyona ve titremeye neden '
                                                   'oldu; muayene imkansızlaştı.',
                                'teaching_point': 'Ateşli peritonit hastasında öncelik cerrahi odağın '
                                                  'aydınlatılmasıdır; uygunsuz fiziksel soğutma zararlıdır.',
                                'text': 'Ateşi düşürmek için fizik muayeneyi tamamlamadan hastayı derhal soğuk su '
                                        'küvetine sokmak'}],
                 'question': 'Sağ alt kadran ağrısı ve periton irritasyonu olan bu çocukta ilk fizik muayene '
                             'yaklaşımınız ne olmalıdır?',
                 'stage_title': 'Sarı Alanda Peritonit Bulguları ve Ağrı Lokalizasyonu'},
               { 'options': [ { 'explanation': "Deneyimli ellerde yüksek çözünürlüklü USG veya kontrastlı batın BT'si "
                                               'sağ alt kadranda normal apendiksten bağımsız, kör sonlanan kalın '
                                               'duvarlı inflame Meckel divertikülünü saptayabilir.',
                                'is_correct': True,
                                'new_finding': 'Laboratuvar: Lökosit 17.200/mm³ (%88 nötrofil), CRP 76 mg/L. Ayrıntılı '
                                               'Batın USG: Retroçekal normal çapta (4 mm) basılabilen apendiks teyit '
                                               'edildi. Ancak apendiksin medialinde, ileum anslarına komşu, kör '
                                               'sonlanan, kalın duvarlı, lümeni distandü, çevresinde inflamatuar '
                                               'ekojen yağ dokusu bulunan 13 mm çapında inflame divertikül yapısı '
                                               'izlendi.',
                                'text': 'Ayrıntılı batın ultrasonografisi veya şüpheli olgularda kontrastlı batın '
                                        'tomografisi ile patolojiyi netleştirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Sintigrafi beklenirken divertikül perfore oldu ve yaygın pürülan '
                                                   'peritonit gelişti.',
                                'teaching_point': 'Meckel sintigrafisi ektopik mukozalı KANAMA olgularında duyarlıdır; '
                                                  'akut inflame divertikülitte duyarlılığı düşüktür ve cerrahiyi '
                                                  'geciktiremez.',
                                'text': 'Kanama olmadığı halde hastaya acil sintigrafi çekmek için 48 saat boyunca '
                                        'hiçbir cerrahi girişim yapmamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Evde delinen divertikül septik şoka neden oldu.',
                                'teaching_point': 'Peritonit bulgusu olan çocuk tetkiksiz ve cerrahi konsültasyonsuz '
                                                  'taburcu edilemez.',
                                'text': 'Hiçbir tetkik yapmadan hastaya oral demir damlası başlayarak eve göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Oral baryum inflame divertikülden batın içine sızarak kimyasal '
                                                   'baryum peritonitine yol açtı.',
                                'teaching_point': 'Akut batın ve perforasyon şüphesinde oral baryum verilmesi ölümcül '
                                                  'peritonit yapar; KONTRENDİKEDİR.',
                                'text': 'Hastaya oral baryum içirerek baryumun apendikse dolup dolmadığını 24 saat '
                                        'grafilerle izlemek'}],
                 'question': 'Apendiksi normal olan ancak sağ alt kadranda belirgin peritoniti süren çocukta tanısal '
                             'strateji nasıl olmalıdır?',
                 'stage_title': 'Laboratuvar ve Görüntüleme İncelemeleri'},
               { 'options': [ { 'explanation': 'Apandisiti taklit eden sağ alt kadran peritoniti, normal apendiks ve '
                                               'ileal kör sonlanan inflame kese Meckel divertikülitini doğrular.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Akut İnflame Meckel Divertiküliti (Pre-perfore Evre).',
                                'text': 'Akut inflame Meckel divertiküliti'},
                              { 'is_correct': False,
                                'scenario_update': 'Ultrasonografide apendiks tamamen normal ve basılabilir olarak '
                                                   'görüntülenmiştir; patoloji apendiks dışıdır.',
                                'teaching_point': 'Apendiksin normal olduğu kanıtlandığında apandisiti taklit eden '
                                                  'divertikülit akla gelmelidir.',
                                'text': 'Akut flegmonöz apandisit tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Mezenterik lenfadenitte periton defansı ve 13 mm kör tübüler '
                                                   'inflame kitle görülmez.',
                                'teaching_point': 'Mezenterik lenfadenit selim büyümüş lenf nodlarıdır; lokal tübüler '
                                                  'bağırsak inflamasyonu yapmaz.',
                                'text': 'Akut mezenterik adenit enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Omental enfarktüste lümenli tübüler bağırsak yapısı bulunmaz; '
                                                   'hiperekojen yağ kitlesi izlenir.',
                                'teaching_point': 'Omental infarkt yağ nekrozudur; Meckel divertikülü ise epitelyal '
                                                  'bağırsak divertikülüdür.',
                                'text': 'Primer omental enfarktüs nekrozu'}],
                 'question': "Normal apendiks, sağ alt kadranda peritonit ve USG'de ileum komşuluğunda inflame kör "
                             'sonlanan tübüler kese ile tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Akut Meckel divertikülitinin tedavisi acil ameliyattır '
                                               '(laparoskopik/açık divertikülektomi veya segmental ileal rezeksiyon). '
                                               'Hasta oral stop tutulur, IV hidrasyon ve antibiyotik '
                                               '(ampisilin-sulbaktam/seftriakson+metronidazol) başlanır.',
                                'is_correct': True,
                                'new_finding': 'Hasta oral alıma kapatıldı. IV hidrasyon ve seftriakson+metronidazol '
                                               'başlandı. Acil laparoskopik eksplorasyona alındı; perfore olmak üzere '
                                               "olan 4 cm'lik inflame Meckel divertikülü tabanından kama şeklinde "
                                               'rezeke edildi. Şifayla iyileşti.',
                                'text': 'Oral alımı durdurup intravenöz izotonik mayi ve geniş spektrumlu antibiyotik '
                                        'eşliğinde cerrahi rezeksiyona almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Evde takip edilen hastanın divertikülü 12 saat içinde delindi ve '
                                                   'yaygın peritonit gelişti.',
                                'teaching_point': 'İnflame Meckel divertikülü medikal tedaviyle gerilemez; ince duvarı '
                                                  'nedeniyle acil cerrahi şarttır.',
                                'text': 'Ameliyattan kaçınmak için hastaya sadece evde oral antibiyotik şurup verip '
                                        'taburculuk planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Laksatif divertikülün intralüminal basıncını fırlatarak acil '
                                                   'ameliyat öncesi perforasyona yol açtı.',
                                'teaching_point': 'Akut karın tablosunda laksatif verilmesi perforasyonu tetikler; '
                                                  'KONTRENDİKEDİR.',
                                'text': 'Ağrıyı geçirmek için hastaya yüksek doz laksatif ve bağırsak temizleme tozu '
                                        'içirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'On gün aç bekleyen çocukta çoklu organ yetmezliği ve metabolik '
                                                   'asidoz gelişti.',
                                'teaching_point': 'Cerrahi endikasyonu olan akut batın saatler içinde ameliyathaneye '
                                                  'alınmalıdır.',
                                'text': 'Hastayı ameliyata almadan önce 10 gün boyunca Sarı Alanda aç ve susuz '
                                        'izlemek'}],
                 'question': 'İnflame Meckel divertiküliti tanısı konulan bu hastada en uygun nihai yönetim basamağı '
                             'hangisidir?',
                 'stage_title': 'Cerrahi Hazırlık ve Preoperatif Yönetim'}]},
  { 'age': '18 Aylık',
    'case_pearl': 'Gastroenteritte tuz ve su kaybı varken sadece elektrolitsiz su veya aşırı dilüe gıdalar verilmesi '
                  "akut hiponatremiye (serum sodyumu <125 mEq/L) yol açar ('su zehirlenmesi'). Ekstraselüler "
                  'ozmolaritenin hızla düşmesiyle su ozmotik olarak beyin hücrelerine hücum eder; akut serebral ödem, '
                  'intrakraniyal basınç artışı, bilinç bozukluğu ve nöbet gelişir. AKUT SEMPTOMATİK (NÖBETLİ) '
                  'HİPONATREMİDE İLK TEDAVİ: 3 mL/kg %3 hipertonik NaCl çözeltisinin 10-20 dakikada IV verilmesidir '
                  '(serum sodyumunu 3-5 mEq/L yükselterek beyin ödemini hızla geriletir ve nöbeti durdurur). Gerekirse '
                  'doz tekrarlanır. Daha sonra sodyumun aşırı hızlı düzeltilmesinden kaçınılmalıdır (24 saatte en '
                  'fazla 8-10 mEq/L; ozmotik demiyelinizasyon riski).',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Gastroenterit sırasında aşırı su içirilmesi sonrası başlayan dalgınlık, kas seyirmeleri ve '
                 'jeneralize nöbet',
    'disposition': 'Sarı Alanda Hava Yolu Güvenliği + %3 Hipertonik NaCl İnfüzyonu ile Nöbet Kontrolü + Yoğun Bakım '
                   'Yatışı',
    'final_diagnosis': 'Ağır Semptomatik Hiponatremi (Gastroenteritte Hipotonik Sıvı İntoksikasyonu)',
    'gender': 'Kız',
    'history': 'On sekiz aylık kız çocuğu ailesi tarafından Sarı Alana getiriliyor: Üç gündür akut gastroenterit '
               'nedeniyle sulu ishal ve kusması varmış. Aile tuzlu sıvı veya ORS yerine çocuğa sadece kaynatılmış saf '
               'su ve açık çay içirmiş. Bugün öğleden sonra çocukta belirgin uyuklama, ardından kollarda ve bacaklarda '
               'sıçramalar başlamış ve acil kapısında 3 dakika süren jeneralize tonik-klonik nöbet geçirmiş.',
    'id': 'Y57',
    'steps': [ { 'options': [ { 'explanation': 'Nöbet geçiren çocukta ABC (Hava Yolu, Solunum, Dolaşım) güvenceye '
                                               'alınmalı, metabolik nöbet etiyolojisi için yatak başı kan şekeri ve '
                                               'acil serum elektrolitleri ölçülmelidir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: KTA 148/dk, SS 28/dk, TA 106/66 mmHg, SpO2 %98. Çocuk '
                                               'postiktal konfüze, kas seyirmeleri devam ediyor. Pupiller izokorik ve '
                                               'ışık refleksi bilateral mevcut; fokal nörolojik defisit yok. Yatak '
                                               'başı Glukoz: 98 mg/dL. Acil Kan Gazı ve Biyokimya: Serum Sodyumu 116 '
                                               'mEq/L (ağır hiponatremi), Potasyum 3.8 mEq/L, Klor 86 mEq/L.',
                                'text': 'Hava yolunu ve oksijenasyonu güvenceye alıp nöbet aktivitesini sonlandırmak '
                                        'için acil kan gazı ve elektrolit bakmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Ağır hiponatremi fark edilmediği için nöbet status epileptikusa '
                                                   'ilerledi ve beyin herniasyonu gelişti.',
                                'teaching_point': 'Ateşi olmayan veya gastroenteritte aşırı su içen çocukta nöbet '
                                                  'febril değil; elektrolit kaynaklıdır.',
                                'text': 'Nöbeti basit febril nöbet kabul edip hastayı hiçbir kan tahlili yapmadan '
                                        'Yeşil Alana yönlendirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Antiepileptik ilaçlar metabolik hiponatremik nöbeti durduramadı ve '
                                                   'kardiyak aritmilere yol açtı.',
                                'teaching_point': 'Hiponatremik nöbet antiepileptiklere dirençlidir; kesin tedavisi '
                                                  'hipertonik sodyum infüzyonudur.',
                                'text': 'Elektrolit bakmadan hastaya derhal yüksek doz damardan fenitoin yükleyip '
                                        'beyin cerrahisine sevk etmek'},
                              { 'is_correct': False,
                                'scenario_update': "Verilen saf su sodyumu 110 mEq/L'ye düşürerek solunum arrestine ve "
                                                   'komaya neden oldu.',
                                'teaching_point': 'Hiponatremide serbest su verilmesi beyin ödemini katlayarak '
                                                  'herniasyona yol açar; KESİNLİKLE YASAKTIR.',
                                'text': 'Çocuğun susuz kaldığını düşünerek hastaya oral yoldan bir litre musluk suyu '
                                        'içirmeye çalışmak'}],
                 'question': 'Gastroenterit sırasında aşırı su içme öyküsü ve nöbet ile getirilen bu çocukta ilk acil '
                             'yaklaşım ne olmalıdır?',
                 'stage_title': 'Sarı Alanda Nöbet Yönetimi ve Acil Elektrolit Ölçümü'},
               { 'options': [ { 'explanation': 'Nöbet veya bilinç bozukluğu ile giden ağır hiponatremide ilk tercih 3 '
                                               'mL/kg %3 NaCl solüsyonunun 10-20 dakikada IV verilmesidir. Bu uygulama '
                                               'sodyumu 3-5 mEq/L artırarak serebral ödemi ve nöbeti hızla durdurur.',
                                'is_correct': True,
                                'new_finding': '3 mL/kg %3 NaCl (yaklaşık 33 mL) 15 dakikada IV infüze edildi. '
                                               "Tekrarlanan kontrol serum sodyumu 121 mEq/L'ye yükseldi. Çocuğun kas "
                                               'seyirmeleri ve konfüzyonu geriledi, gözlerini açarak annesini tanıdı.',
                                'text': 'Akut semptomatik hiponatremik nöbette derhal üç mililitre bölü kilogram yüzde '
                                        'üç hipertonik sodyum klorür infüzyonu uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Hipotonik mayi verilmesi serum sodyumunu daha da düşürerek '
                                                   'intrakraniyal basıncı artırdı.',
                                'teaching_point': 'Semptomatik hiponatremide hipotonik sıvı verilmesi ölümcül '
                                                  'herniasyona yol açar; hipertonik tuz şarttır.',
                                'text': 'Sodyumu yavaş düzeltmek amacıyla hastaya yüzde beş dekstroz içeren hipotonik '
                                        'mayiyi hızlı bolus yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Diüretik idrarla daha fazla sodyum atılmasına neden olarak '
                                                   'hipovolemik şoku tetikledi.',
                                'teaching_point': 'Hipovolemik hiponatremide furosemid sodyum ve hacim kaybını '
                                                  'artırır; KONTRENDİKEDİR.',
                                'text': 'Hiçbir sodyum solüsyonu vermeden hastaya sadece yüksek doz idrar söktürücü '
                                        'furosemid enjekte etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Aşırı hızlı sodyum yükselmesi 48 saat sonra santral pontin '
                                                   'miyelinolizis ve kuadriplejiye yol açtı.',
                                'teaching_point': "Sodyumun 24 saatte 8-10 mEq/L'den fazla yükseltilmesi ozmotik "
                                                  'demiyelinizasyon sendromu (santral pontin miyelinolizis) yapar.',
                                'text': 'Sodyum düzeyini 1 saat içinde hızla 145 mEq/L düzeyine çıkaracak şekilde '
                                        'kontrolsüz tuz yüklemesi yapmak'}],
                 'question': 'Serum sodyumu 116 mEq/L ölçülen ve nöbeti olan bu hastada acil uygulanacak doğru tedavi '
                             'protokolü hangisidir?',
                 'stage_title': 'Laboratuvar ve Görüntüleme İncelemeleri'},
               { 'options': [ { 'explanation': 'Serum sodyumunun <120 mEq/L olması ve nörolojik semptomların '
                                               '(nöbet/letarji) eşlik etmesi ağır semptomatik hiponatremi tanısıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Hipotonik Sıvı İntoksikasyonuna Bağlı Ağır Semptomatik '
                                               'Hiponatremi ve Serebral Ödem.',
                                'text': 'Ağır semptomatik akut hiponatremi'},
                              { 'is_correct': False,
                                'scenario_update': 'Epilepside serum sodyumu normaldir; bu hastadaki nöbet ağır '
                                                   'hiponatremiye sekonder metabolik nöbettir.',
                                'teaching_point': 'Elektrolit bozukluğuna sekonder nöbetler epilepsi değildir; '
                                                  'metabolik dengesizlik düzeltilince tekrarlamaz.',
                                'text': 'Basit çocukluk çağı epilepsisi'},
                              { 'is_correct': False,
                                'scenario_update': 'Hastanın kan şekeri 98 mg/dL olup tamamen normal sınırlardadır; '
                                                   'hipoglisemi dışlanmıştır.',
                                'teaching_point': 'Hipoglisemi için glukoz <50-60 mg/dL olmalıdır; bu hastada sorun '
                                                  'sodyum çöküşüdür.',
                                'text': 'Akut hipoglisemik konvülziyon krizi'},
                              { 'is_correct': False,
                                'scenario_update': 'Hastanın ateşi normaldir (36.8°C); ateş olmadan febril konvülziyon '
                                                   'tanısı konulamaz.',
                                'teaching_point': 'Febril konvülziyon ateş varlığında tanımlanır; afebril nöbette '
                                                  'elektrolit ve intrakraniyal patolojiler aranır.',
                                'text': 'Komplike febril konvülziyon atağı'}],
                 'question': 'Aşırı hipotonik sıvı alımı sonrası akut ensefalopati, konvülziyon ve Na 116 mEq/L ile '
                             'kesin klinik tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Akut semptomlar yatıştıktan sonra sodyum yükselme hızı '
                                               'sınırlandırılmalıdır (saatte 0.5 mEq/L, günde maksimum 8-10 mEq/L). '
                                               'İdame sıvı dengeli izotonik solüsyonlarla verilmeli ve hasta çocuk '
                                               'yoğun bakımda sık elektrolit takibiyle izlenmelidir.',
                                'is_correct': True,
                                'new_finding': 'Serum sodyumu 4 saatlik aralıklarla izlendi. 24 saat sonunda sodyum '
                                               '124 mEq/L seviyesine ulaştı. Nörolojik defisit gelişmedi. Anneye '
                                               'gastroenteritte saf su yerine mutlaka ORS verilmesi gerektiği '
                                               'anlatıldı.',
                                'text': 'Günlük sodyum yükselmesini sekiz ila on milieşdeğeri aşmayacak şekilde '
                                        'planlayıp izotonik mayi ile çocuk yoğun bakıma almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Hızlı yükselen sodyum pontin demiyelinizasyona ve geri dönüşümsüz '
                                                   'nörolojik sekellere yol açtı.',
                                'teaching_point': 'Nöbet durduktan sonra hipertonik NaCl kesilmeli, düzeltme zamana '
                                                  'yayılmalıdır.',
                                'text': 'Sodyumu bir an önce normale getirmek için hastaya aralıksız hipertonik tuz '
                                        'infüzyonuna devam etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Eve gönderilen hastada rebound hiponatremi gelişti ve çocuk evde '
                                                   'status epileptikusa girdi.',
                                'teaching_point': 'Ağır elektrolit bozukluğu olan hastalar stabilize edildikten sonra '
                                                  'en az 24-48 saat yoğun bakımda izlenmelidir.',
                                'text': 'Çocuğun nöbeti durduğu için hiçbir sıvı vermeden hastayı acil servisten '
                                        'doğrudan evine göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Mannitol ozmotik diürezle ek sodyum ve su kaybına yol açarak '
                                                   'hipovolemik şoku tetikledi.',
                                'teaching_point': 'Hipovolemik hiponatremide mannitol dehidratasyonu artırır; serebral '
                                                  'ödem hipertonik tuzla kontrol edilir.',
                                'text': 'Beyin ödemini tamamen boşaltmak amacıyla hastaya yüksek doz konsantre '
                                        'mannitol puşeleri yapmak'}],
                 'question': 'Nöbeti %3 NaCl ile durdurulan hastada ozmotik demiyelinizasyonu önlemek için idame sıvı '
                             'planı nasıl olmalıdır?',
                 'stage_title': 'Osmotik Demiyelinizasyon Önleme ve Devam Sıvısı'}]},
  { 'age': '3 Yaşında',
    'case_pearl': 'Pediatrik akut böbrek hasarının (ABH) en sık nedeni dehidratasyona ve hipovolemiye bağlı renal '
                  'hipoperfüzyondur (prerenal azotemi). Tübüler fonksiyonlar henüz sağlamdır; böbrek suyu ve sodyumu '
                  'korumak için konsantre idrar çıkarır (İdrar Dansitesi >1.020, İdrar Osmolaritesi >500 mOsm/kg, '
                  'İdrar Sodyumu <20 mEq/L, Fraksiyonel Sodyum Ekskresyonu FeNa <%1). Kanda BUN/Kreatinin oranı '
                  'belirgin artar (>20-30). Akut tübüler nekroz (ATN) oturmadan önce zamanında verilen izotonik '
                  'kristaloid bolusları (20 mL/kg SF) ile intravasküler hacim düzeltildiğinde böbrekler hızla yanıt '
                  'verir ve idrar çıkışı saatler içinde başlar. İdrar çıkışı kesinleşene kadar intravenöz sıvılara '
                  'ASLA POTASYUM EKLENMEZ!',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Üç gündür süren şiddetli ishal ve kusma sonrası 24 saattir hiç idrar yapmama, solukluk ve halsizlik',
    'disposition': 'Sarı Alanda Hacim Genişletici İzotonik Kristaloid Bolusları + İdrar Çıkışı Monitörizasyonu ve '
                   'Servis Yatışı',
    'final_diagnosis': 'Prerenal Akut Böbrek Hasarı (Ciddi Dehidratasyona Sekonder Prerenal Azotemi)',
    'gender': 'Erkek',
    'history': 'Üç yaşındaki erkek çocuk ailesi tarafından Sarı Alana getiriliyor: Üç gündür günde 10 kez sulu ishal '
               've kusması varmış. Aile ağızdan sıvı içirememiş. Son 24 saattir bezi tamamen kuru kalmış, hiç idrar '
               'yapmamış. Çocuk aşırı halsiz, gözlerini açmakta zorlanıyor ve çevreye ilgisiz yatıyor. Ailesi çocuğun '
               'böbreklerinin iflas ettiğinden endişe ediyor.',
    'id': 'Y58',
    'steps': [ { 'options': [ { 'explanation': 'Hacim durumu, deri turgoru, mukoza kuruluğu, fontanel/göz küreleri, '
                                               'kapiller dolum zamanı ve mesane doluluğu prerenal azoteminin tespiti '
                                               'için temel muayene adımlarıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.3°C, KTA 146/dk, SS 30/dk, TA 80/48 mmHg (yaşa '
                                               'göre hipotansif eğilimli), SpO2 %98, KDZ 3.5 sn. Göz küreleri belirgin '
                                               'çökük, ağız mukozası kuru, deri turgoru 2.5 saniyede düzeliyor. Batın '
                                               'muayenesi rahat, suprapubik palpasyonda ve perküsyonda mesane boş.',
                                'text': 'İntravasküler hacim durumunu, periferik dolaşımı, mukoza kuruluğunu ve son '
                                        'idrar saatini detaylı değerlendirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Boş mesaneye yapılan travmatik zorlama üretral kanamaya ve mukozal '
                                                   'yırtığa yol açtı.',
                                'teaching_point': 'Prerenal yetmezlikte mesane boştur; idrar olmamasının nedeni idrar '
                                                  'yolu tıkanıklığı değil, böbrek perfüzyon kaybıdır.',
                                'text': 'İdrar yapamadığı için anüriyi dışlamak amacıyla metal kateterle steriliteye '
                                        'bakmadan üretraya müdahale etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Geri döndürülebilir hacim açığı olan hastada gereksiz invaziv '
                                                   'hemodiyaliz kateter komplikasyonları doğurdu.',
                                'teaching_point': 'Dehidratasyona bağlı prerenal yetmezlik hızla geri döndürülebilir; '
                                                  'ilk basamak diyaliz değil, sıvı resüsitasyonudur.',
                                'text': 'Böbreklerin tamamen bittiğini söyleyerek hiçbir sıvı vermeden hastayı acilen '
                                        'kronik hemodiyaliz programına sokmak'},
                              { 'is_correct': False,
                                'scenario_update': '24 saattir idrar yapmayan çocuk evde anürik komaya ve hiperkalemik '
                                                   'kardiyak arreste girdi.',
                                'teaching_point': 'Anüri ve hipotansiyon Sarı/Kırmızı alan acilidir; taburculuk '
                                                  'kesinlikle yapılamaz.',
                                'text': 'Hastada ateş olmadığı için muayeneyi sonlandırıp hastayı Yeşil Alanda oral '
                                        'antibiyotik ile taburcu etmek'}],
                 'question': 'Dehidratasyon öyküsü ve 24 saattir anürisi olan bu çocukta ilk fizik muayene '
                             'yaklaşımınız ne olmalıdır?',
                 'stage_title': 'Sarı Alanda Hacim Durumu ve Renal Perfüzyon Muayenesi'},
               { 'options': [ { 'explanation': 'BUN/Kreatinin yüksekliği ve elektrolitler kontrol edilirken 20 mL/kg '
                                               'izotonik SF infüzyonu renal perfüzyonu açar. Sıvı yüklemesine idrarla '
                                               'yanıt alınması prerenal etiyolojiyi doğrular.',
                                'is_correct': True,
                                'new_finding': 'Biyokimya: Üre 102 mg/dL, Kreatinin 1.9 mg/dL (yaşına göre 4 kat '
                                               'yüksek), Potasyum 5.0 mEq/L, Sodyum 135 mEq/L. 20 mL/kg SF bolusunun '
                                               'ardından 2. saatte bebek 35 mL konsantre idrar çıkardı (idrar '
                                               'dansitesi 1.025, spot idrar sodyumu 11 mEq/L, FeNa %0.4).',
                                'text': 'Serum kreatinin, üre, elektrolitleri göndermek ve yirmi mililitre bölü '
                                        'kilogram izotonik kristaloid infüzyonuyla renal yanıtı sınamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Hipovolemik hastaya diüretik verilmesi intravasküler volümü daha '
                                                   'da tüketerek akut tübüler nekroza yol açtı.',
                                'teaching_point': 'Hipovolemide diüretik verilmesi KONTRENDİKEDİR; perfüzyon olmadan '
                                                  'diüretik vermek böbreği kalıcı olarak öldürür.',
                                'text': 'Sıvı vermeden önce hastaya yüksek doz intravenöz furosemid enjekte ederek '
                                        'böbreği zorla idrar yapmaya zorlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Anürik hastaya kontrolsüz potasyum verilmesi potasyumu 8.5 '
                                                   "mEq/L'ye çıkararak ventriküler fibrilasyon yarattı.",
                                'teaching_point': 'İdrar çıkışı teyit edilmemiş anürik hastaya damardan potasyum '
                                                  'verilmesi KESİNLİKLE KONTRENDİKEDİR.',
                                'text': 'İdrar söktürmek için potasyum klorür içeren hipertonik solüsyonları damardan '
                                        'hızlı puşe yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Sirke içirilmesi hastada şiddetli kusmayı tetikledi ve '
                                                   'dehidratasyonu daha da ağırlaştırdı.',
                                'teaching_point': 'Akut böbrek yetmezliğinde kanıta dayalı olmayan alternatif '
                                                  'yaklaşımlar zaman kaybına ve ölüme yol açar.',
                                'text': 'Tetkik istemeden hastaya sadece oral elma sirkesi içirerek böbrek taşlarının '
                                        'erimesini beklemek'}],
                 'question': 'Prerenal azotemi şüphesi olan bu dehidrate çocukta böbrek fonksiyonunu değerlendirmek ve '
                             'yanıtı sınamak için en uygun yaklaşım hangisidir?',
                 'stage_title': 'Laboratuvar ve Görüntüleme İncelemeleri'},
               { 'options': [ { 'explanation': 'Hipovolemi öyküsü, yüksek BUN/Kreatinin oranı, FeNa <%1 ve izotonik '
                                               'sıvı bolusuyla idrar çıkışının başlaması prerenal hasarı kanıtlar.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Ciddi Dehidratasyona Bağlı Prerenal Akut Böbrek Hasarı '
                                               '(Prerenal Azotemi).',
                                'text': 'Prerenal akut böbrek hasarı'},
                              { 'is_correct': False,
                                'scenario_update': "ATN'de tübüler hücreler ölmüştür; FeNa >%2'dir ve sıvı bolusuna "
                                                   'rağmen idrar çıkışı olmaz.',
                                'teaching_point': 'Prerenal hasar sıvıya anında idrarla yanıt verir; ATN ise sıvı '
                                                  'verilmesine rağmen yanıtsız kalır.',
                                'text': 'İntrensek akut tübüler nekroz'},
                              { 'is_correct': False,
                                'scenario_update': "APSGN'de hipertansiyon, ödem, makroskopik kola renkli hematüri ve "
                                                   'eritrosit silendirleri vardır; dehidratasyon görülmez.',
                                'teaching_point': 'APSGN hipervolemi ve nefrit ile seyreder; gastroenterit '
                                                  'dehidratasyonuna bağlı prerenal tabloyla ilgisi yoktur.',
                                'text': 'Akut poststreptokokal glomerülonefrit'},
                              { 'is_correct': False,
                                'scenario_update': 'Hastada mikroanjiyopatik hemolitik anemi, şistositler ve '
                                                   'trombositopeni yoktur; kan sayımı doğaldır.',
                                'teaching_point': "HÜS'te trombositopeni ve anemi şarttır; izole dehidratasyon "
                                                  'azotemisinde kan tablosu normaldir.',
                                'text': 'Hemolitik üremik sendrom triyadı'}],
                 'question': 'Dehidratasyon, BUN/Kreatinin yüksekliği, FeNa <%1 ve sıvı bolusuna idrarla dramatik '
                             'yanıt ile kesin tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'İdrar çıkışı sağlandıktan sonra hipokalemiyi önlemek için idame sıvıya '
                                               'potasyum (20 mEq/L) eklenebilir. Kalan dehidratasyon açığı dengeli '
                                               'solüsyonlarla 24 saatte tamamlanır ve kreatinin takibi yapılır.',
                                'is_correct': True,
                                'new_finding': 'İdrar çıkışı saatte 2.2 mL/kg olarak devam etti. Sıvı replasmanı '
                                               'tamamlandı. 24 saat sonra üre 28 mg/dL, kreatinin 0.4 mg/dL düzeyine '
                                               'geriledi (tam kür). Oral hidrasyona geçilerek şifayla taburcu edildi.',
                                'text': 'İdrar çıkışı teyit edildikten sonra potasyumlu dengeli parenteral sıvıya '
                                        'geçerek böbrek parametrelerini izlemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Defisiti tamamlanmayan çocuk eve gittikten sonra tekrar anürik '
                                                   'faza girdi.',
                                'teaching_point': 'İlk idrar böbreğin canlı olduğunu gösterir ancak defisit ve idame '
                                                  'tamamlanmadan taburculuk yapılamaz.',
                                'text': 'Bir kez idrar yaptığı için damar yolunu anında çıkarıp hastayı hiçbir tedavi '
                                        'vermeden taburcu etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Aşırı kontrolsüz sıvı yüklemesi hastada akut akciğer ödemi ve '
                                                   'hipoksemiye yol açtı.',
                                'teaching_point': 'İdrar çıkışı başladıktan sonra sıvılar zamana yayılarak dengeli '
                                                  'verilmelidir; aşırı yükleme volüm fazlalığı yapar.',
                                'text': 'İdrar çıkışını daha da artırmak için hastaya kontrolsüz şekilde 80 mL/kg '
                                        'sıvıyı yarım saatte vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Aminoglikozid verilmesi yeni toparlanan tübülleri zehirleyerek '
                                                   "gerçek ATN'ye yol açtı.",
                                'teaching_point': 'İyileşen böbrekte nefrotoksik ilaçlardan kesinlikle kaçınılmalıdır.',
                                'text': 'Böbrekleri korumak amacıyla hastaya profilaktik olarak oral nefrotoksik '
                                        'aminoglikozid şurup başlamak'}],
                 'question': 'İzotonik bolus ile idrar çıkışı başlayan bu çocukta bundan sonraki sıvı ve izlem '
                             'yönetimi nasıl olmalıdır?',
                 'stage_title': 'Rehidrasyon Sıvı Planı ve Renal Fonksiyon İzlemi'}]},
  { 'age': '5 Yaşında',
    'case_pearl': 'Nefrotik sendromlu çocuklarda idrarla immünglobülin ve kompleman faktörlerinin (faktör B ve I) '
                  'kaybı nedeniyle opsonizasyon defekti vardır; bu durum kapsüllü bakterilere (özellikle Streptococcus '
                  'pneumoniae ve E. coli) karşı aşırı duyarlılık yaratır. Asiti olan nefrotik çocukta aniden gelişen '
                  'ateş ve karın ağrısında aksi kanıtlanana kadar Spontan Bakteriyel Peritonit (SBP) düşünülmelidir! '
                  'Tanı ultrason eşliğinde tanısal parasentez ile konur. Asit sıvısında polimorfonükleer lökosit (PNL '
                  '/ nötrofil) sayısının ≥250/mm³ olması SBP için TANI KOYDURUCUDUR. Tedavide gecikmeden intravenöz 3. '
                  'kuşak sefalosporin (sefotaksim veya seftriakson) başlanmalıdır.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Nefrotik sendrom tanılı çocukta aniden başlayan şiddetli karın ağrısı, ateş ve karında yaygın '
                 'hassasiyet',
    'disposition': 'Sarı Alanda Tanısal Parasentez + Kan Kültürü + İntravenöz 3. Kuşak Sefalosporin Başlanması ve '
                   'Servis Yatışı',
    'final_diagnosis': 'Spontan Bakteriyel Peritonit (SBP - Nefrotik Sendrom Zemininde Asit Enfeksiyonu)',
    'gender': 'Kız',
    'history': 'Beş yaşındaki kız çocuk ailesi tarafından Sarı Alana getiriliyor: Bilinen idiyopatik nefrotik sendrom '
               'tanısıyla remisyonda olmayan, batında belirgin asiti ve yaygın ödemi olan bir hasta. Dün gece aniden '
               "ateşi 38.8°C'ye yükselmiş, karnında yaygın şiddetli ağrı başlamış ve 3 kez safrasız kusmuş. Çocuk "
               'nefes alırken bile karnının battığını söyleyerek hareketsiz yatıyor.',
    'id': 'Y59',
    'steps': [ { 'options': [ { 'explanation': 'Asit sıvısı enfeksiyonu (peritonit) yaygın defans, rebound hassasiyeti '
                                               've ateşle seyreder. Genel ödem ve hemodinami muayene edilmelidir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 38.7°C, KTA 138/dk, SS 32/dk, TA 96/60 mmHg, SpO2 '
                                               '%98. Periorbital ve bilateral pretibial belirgin gode bırakan ödem. '
                                               'Batında masif asit, dalgalanma hissi ve tüm kadranlarda belirgin '
                                               'istemsiz defans ile yaygın rebound hassasiyeti mevcut.',
                                'text': 'Asit varlığını, batın distansiyonunu, rebound hassasiyetini ve nefrotik '
                                        'sendromun genel ödem durumunu değerlendirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Peritoniti olan hastada diüretik verilmesi intravasküler volümü '
                                                   'tüketerek septik şoku tetikledi.',
                                'teaching_point': 'Asiti olan nefrotik çocukta ateş ve karın ağrısı peritonit '
                                                  'alarmıdır; muayenesiz diüretik verilemez.',
                                'text': 'Karın ağrısını basit nefrotik ödeme bağlayarak hiçbir batın muayenesi '
                                        'yapmadan hastaya oral diüretik vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Nefrotik sendrom zemininde verilen NSAİİ akut böbrek hasarını ve '
                                                   'anüriyi tetikledi.',
                                'teaching_point': 'Nefrotik çocuklarda NSAİİ ilaçlar glomerüler filtrasyonu çökertir; '
                                                  'KESİNLİKLE KONTRENDİKEDİR.',
                                'text': 'Ağrıyı kesmek amacıyla hastaya derin intramüsküler nonsteroid antiinflamatuar '
                                        'enjeksiyonu uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tanısal parasentez yapılmadan cerrahiye alınan hastada medikal '
                                                   'tedavi edilecek SBP tablosuna gereksiz laparotomi yapıldı.',
                                'teaching_point': 'Nefrotik asit zeminindeki peritonit primerdir (SBP); cerrahi '
                                                  'apandisit değildir, medikal antibiyotikle tedavi edilir.',
                                'text': 'Hastada apandisit olduğunu varsayarak asit sıvısını incelemeden hastayı '
                                        'derhal genel anesteziye vermek'}],
                 'question': 'Nefrotik sendromlu, asiti olan ve yüksek ateşle karın ağrısı başlayan bu çocukta ilk '
                             'fizik muayene yaklaşımı nasıl olmalıdır?',
                 'stage_title': 'Sarı Alanda Nefrotik Zemin ve Peritoneal Hassasiyet Muayenesi'},
               { 'options': [ { 'explanation': 'SBP tanısı tanısal parasentez ile konur. Asit sıvısında hücre sayımı '
                                               '(PNL >250/mm³), gram boyama ve kültür tanıyı ve antibiyotik seçimini '
                                               'kesinleştirir.',
                                'is_correct': True,
                                'new_finding': 'USG eşliğinde tanısal parasentez yapıldı; asit sıvısı bulanık izlendi. '
                                               'Asit Analizi: Lökosit 1850/mm³, PNL oranı %86 (Nötrofil sayısı '
                                               '1590/mm³ > 250 kriteri pozitif), Gram boyamada gram pozitif '
                                               'diplokoklar izlendi. Laboratuvar: Lökosit 18.200/mm³, CRP 88 mg/L, '
                                               'Serum Albümin 1.8 g/dL.',
                                'text': 'Enfeksiyon odağını kanıtlamak ve etkeni izole etmek için ultrason eşliğinde '
                                        'acil tanısal parasentez uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Parasentez geciktirildiği için peritonit sepsise ve septik şoka '
                                                   'ilerledi.',
                                'teaching_point': 'SBP şüphesinde tanısal parasentez acil serviste gecikmeden '
                                                  'yapılmalı ve derhal ampirik tedavi başlanmalıdır.',
                                'text': 'Parasentez yapmadan sadece boğaz kültürü alıp 48 saat sonraki sonuca göre '
                                        'antibiyotik planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tomografi asiti gösterdi ancak hücresel enfeksiyonu kanıtlayamadı '
                                                   've kontrast böbreği zorladı.',
                                'teaching_point': 'SBP tanısı radyolojik değil, parasentez sıvısındaki nötrofil '
                                                  'sayımıyla konur.',
                                'text': 'Kesin tanı için asit sıvısını boşaltmak yerine tüm batın kontrastlı '
                                        'bilgisayarlı tomografisi çektirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Bakteriyel peritonit tedavi edilmediği için çocuk septik şok '
                                                   'komasına girdi.',
                                'teaching_point': 'SBP hayatı tehdit eden bakteriyel bir enfeksiyondur; parenteral '
                                                  'antibiyoterapi zorunludur.',
                                'text': 'Parasentez yapmadan hastaya sadece oral probiyotik başlayıp Yeşil Alanda '
                                        'takip etmek'}],
                 'question': 'SBP şüphesi olan bu nefrotik çocukta kesin tanıyı koymak için yapılması gereken en '
                             'kritik tanısal işlem hangisidir?',
                 'stage_title': 'Laboratuvar ve Görüntüleme İncelemeleri'},
               { 'options': [ { 'explanation': 'Nefrotik sendromlu çocukta asit sıvısında PNL sayısının >250/mm³ '
                                               'olması Spontan Bakteriyel Peritonit için tanı koydurucudur.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: İdiyopatik Nefrotik Sendrom zemininde gelişen Spontan '
                                               'Bakteriyel Peritonit (Streptococcus pneumoniae şüpheli).',
                                'text': 'Spontan bakteriyel peritonit enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Sekonder cerrahi peritonitte multipl polimikrobiyal enterik flora '
                                                   "bulunur; bu hastada monomikrobiyal pnömokok SBP'si mevcuttur.",
                                'teaching_point': 'Nefrotik asit zemininde spontan tek etkenli (özellikle pnömokok) '
                                                  "enfeksiyon SBP'dir; cerrahi delinme değildir.",
                                'text': 'Akut perfore apandisit peritoniti'},
                              { 'is_correct': False,
                                'scenario_update': 'Gastroenteritte asit sıvısında lökosit fırlaması ve yaygın periton '
                                                   'irritasyonu görülmez.',
                                'teaching_point': 'Gastroenterit lüminal bağırsak enfeksiyonudur; periton sıvısında '
                                                  'PNL >250 yapmaz.',
                                'text': 'Akut bakteriyel gastroenterit tablosu'},
                              { 'is_correct': False,
                                'scenario_update': "HSP'de palpabl purpura ve eklem tutulumu beklenir; masif asit "
                                                   'enfeksiyonu ve diplokok peritoniti olmaz.',
                                'teaching_point': 'HSP lökositoklastik vaskülittir; nefrotik asit sıvısı bakteriyel '
                                                  'enfeksiyonu değildir.',
                                'text': 'Henoch-Schönlein purpura vasküliti'}],
                 'question': 'Nefrotik zemin, akut periton irritasyonu ve parasentezde PNL >250/mm³ ile kesin klinik '
                             'tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': "SBP'de en sık etken S. pneumoniae ve Gram-negatif basillerdir (E. "
                                               "coli). İlk tercih intravenöz SEFOTAKSİM veya SEFTRİAKSON'dur. "
                                               'Hipoalbüminemi ve hipovolemi için %20 albümin infüzyonu ve pediatrik '
                                               'nefroloji takibi planlanır.',
                                'is_correct': True,
                                'new_finding': 'İntravenöz sefotaksim (150 mg/kg/gün) başlandı. %20 human albümin '
                                               'infüzyonu ile intravasküler volüm desteklendi. 48 saat sonra ateşi '
                                               'düştü, batın hassasiyeti tamamen kayboldu ve asit kültürü sterilize '
                                               'oldu.',
                                'text': 'Derhal intravenöz üçüncü kuşak sefalosporin başlamak, albümin desteğini '
                                        'planlamak ve çocuk servisine yatırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz cerrahi müdahale nefrotik çocukta yara yeri enfeksiyonu '
                                                   've cerrahi strese bağlı nükse yol açtı.',
                                'teaching_point': 'SBP cerrahi bir hastalık değildir; medikal intravenöz antibiyotikle '
                                                  'tamamen şifa bulur, ameliyat KONTRENDİKEDİR.',
                                'text': 'Antibiyotik vermeden hastayı derhal acil ameliyathaneye alıp tüm peritonu '
                                        'açık cerrahiyle yıkamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Oral antibiyotik asit içine yeterli konsantrasyonda geçmediği için '
                                                   'enfeksiyon bakteriyemiye ve septik şoka ilerledi.',
                                'teaching_point': 'SBP hayatı tehdit eden derin bir enfeksiyondur; mutlak surette '
                                                  'intravenöz yüksek doz antibiyoterapi gerektirir.',
                                'text': 'Hastaya sadece oral amoksisilin şurup verip evinde istirahat etmesini '
                                        'söylemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Albümin replasmanı yapılmadan hızlı masif parasentez hastada derin '
                                                   'hipovolemik şok ve dolaşım kollapsına yol açtı.',
                                'teaching_point': 'Parasentez kaynaklı dolaşım disfonksiyonu (PCDD) ölümcüldür; asit '
                                                  'hızla boşaltılmamalı, antibiyotikle tedavi edilmelidir.',
                                'text': 'Asit enfeksiyonunu kurutmak için hastanın tüm asit sıvısını tek seferde hızla '
                                        've tamamen boşaltmak'}],
                 'question': 'SBP tanısı doğrulanan bu nefrotik çocukta Sarı Alanda başlanacak en uygun medikal tedavi '
                             'protokolü hangisidir?',
                 'stage_title': 'Parenteral Antibiyoterapi ve Nefrolojik Yönetim'}]},
  { 'age': '2 Yaşında',
    'case_pearl': 'Özofagusta takılı kalan düğme piller PEDİATRİK ACİLLERİN EN ZAMAN KRİTİK TABLOLARINDANDIR! Pil '
                  'özofagusun ıslak mukozasına temas ettiği andan itibaren dış devreyi tamamlar; anotta elektrik akımı '
                  'oluşur ve hidroksit iyonları (ağır alkali yanık / likefaksiyon nekrozu) üretilir. Sadece 2 SAAT '
                  'İÇİNDE özofagus perforasyonu, trakeoözofageal fistül ve ölümcül aortoözofageal fistül (masif fatal '
                  'kanama) gelişebilir! Ön-arka grafide tipik ÇİFT HALKA (double-ring / halo) işareti ve lateral '
                  'grafide basamaklanma (step-off) izlenir. Madeni paradan bu şekilde ayrılır. 2 SAAT İÇİNDE ACİL '
                  'RİJİT/FLEKSİBL ENDOSKOPİK ÇIKARMA ŞARTTIR! Endoskopiye kadar geçen sürede perforasyon şüphesi yoksa '
                  've çocuk ≥1 yaş ise her 10 dakikada 10 mL bal (honey) verilmesi alkali nötralizasyonu sağlayarak '
                  'doku hasarını anlamlı düzeyde azaltır.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Oyuncak kumandasının pilini yuttuktan sonra başlayan göğüs ağrısı, tükürüğünü yutamama ve '
                 'huzursuzluk',
    'disposition': 'Sarı Alanda Oral Alımın Kapatılması + Acil Radyoloji + İlk 2 Saatte Acil Endoskopik Çıkarma',
    'final_diagnosis': 'Özofagusta Takılı Kalan Düğme Pil (Button Battery İmpaksiyonu)',
    'gender': 'Erkek',
    'history': 'İki yaşındaki erkek çocuk ailesi tarafından Sarı Alana panikle getiriliyor: Yaklaşık 45 dakika önce '
               'evde oyuncak arabasının arkasındaki lityum düğme pili ağzına atıp yutmuş. Çocuk o andan itibaren '
               'göğsünün üst kısmını göstererek ağlıyor, tükürüğünü yutamayıp ağzından salyalar akıtıyor ve annesinin '
               'içirmeye çalıştığı suyu içer içmez öğürerek çıkarıyor.',
    'id': 'Y60',
    'steps': [ { 'options': [ { 'explanation': 'Hava yolu açıklığı (stridor/dispne) ve özofagus tıkanıklığı '
                                               '(hipersalivasyon/yutamama) hızla incelenmeli, acil endoskopi ve '
                                               'anestezi güvenliği için oral alım kapatılmalıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.0°C, KTA 128/dk, SS 26/dk, TA 94/56 mmHg, SpO2 '
                                               '%99. Çocuk ajite, sürekli göğsünün üst kısmını göstererek ağlıyor; '
                                               'ağzından berrak sekresyonlar akıyor, yutkunamıyor. Stridor veya '
                                               'solunum sıkıntısı yok, akciğer oskültasyonu doğal. Oral alım '
                                               'kapatıldı.',
                                'text': 'Tükürük yutma güçlüğü, stridor, solunum sıkıntısı ve retrosternal ağrıyı '
                                        'hızla değerlendirip oral alımı kapatmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Katı ekmek özofagusta takılı olan pilin üzerine bindi ve mukozal '
                                                   'perforasyonu daha da hızlandırdı.',
                                'teaching_point': 'Özofagusta takılı yabancı cisim varken katı gıda verilmesi '
                                                  'obstrüksiyonu ve yırtılma riskini artırır; KONTRENDİKEDİR.',
                                'text': 'Pilin mideye inmesini sağlamak amacıyla çocuğa derhal zorla bir somun ekmek '
                                        've katı gıda yedirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Kusturma manevrası pilin özofagus duvarını yırtmasına ve pil '
                                                   'içeriğinin hava yoluna kaçmasına neden oldu.',
                                'teaching_point': 'Pil ve kostik madde yutulmasında kusturma KESİNLİKLE '
                                                  'KONTRENDİKEDİR; perforasyon ve aspirasyon yapar.',
                                'text': 'Pili kusturmak amacıyla çocuğun boğazına parmak sokup yüksek doz ipeka şurubu '
                                        'içirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Özofagusta kalan pil 3 saat sonra aortaya fistülize oldu ve çocuk '
                                                   'masif kanamayla kaybedildi.',
                                'teaching_point': 'Özofagustaki düğme pil 2 saatte perforasyon ve ölümcül kanama '
                                                  'yapabilen hiperakut bir acildir.',
                                'text': 'Pilin kendiliğinden kakayla çıkacağını söyleyerek hastayı hiçbir tetkik '
                                        'yapmadan Yeşil Alandan eve göndermek'}],
                 'question': 'Düğme pil yutan, tükürüğünü yutamayan ve ağlayan 2 yaşındaki çocukta ilk yaklaşım ne '
                             'olmalıdır?',
                 'stage_title': 'Sarı Alanda Yabancı Cisim Tipi ve Hava Yolu Muayenesi'},
               { 'options': [ { 'explanation': 'İki yönlü grafide ön-arkada çift halka (halo / double-ring) ve lateral '
                                               'grafide basamak (step-off) işareti düğme pili madeni paradan ayırt '
                                               'eder ve acil endoskopi endikasyonunu netleştirir.',
                                'image': 'assets/images/adbg_button_battery.png',
                                'is_correct': True,
                                'new_finding': 'Ön-Arka ve Yan Boyun/Toraks Grafisi: Üst özofagus düzeyinde (C6-T1 '
                                               'seviyesinde) takılı kalmış, ön-arka grafide karakteristik ÇİFT HALKA '
                                               '(halo) görünümü, yan grafide pilin katot/anot basamaklanma (step-off) '
                                               'işareti veren 20 mm çapında metalik düğme pil izlendi. Subkutan '
                                               'amfizem saptanmadı.',
                                'text': 'Pilin seviyesini ve pil olduğunu madeni paradan ayırt etmek amacıyla ön-arka '
                                        've yan grafiler çekmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Kılavuz aranırken geçen 2 saatte özofagus lümeni nekroze oldu ve '
                                                   'mediastinit gelişti.',
                                'teaching_point': 'Radyolojik doğrulama dakikalar içinde yapılmalıdır; zaman kaybı '
                                                  'trakeoözofageal fistüle yol açar.',
                                'text': 'Grafi çekmeden önce pilin tipini öğrenmek için aileyi eve gönderip pilin '
                                        'kullanma kılavuzunu aratmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Metalik pil manyetik alanda hareket ederek özofagus duvarını '
                                                   'parçaladı ve termal yanığı artırdı.',
                                'teaching_point': 'Metalik yabancı cisim ve pillerde manyetik rezonans (MRG) '
                                                  'KESİNLİKLE KONTRENDİKEDİR.',
                                'text': 'Kesin tanı için radyolojiyi atlayıp hastaya derhal acil manyetik rezonans '
                                        'görüntüleme planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Ultrason boyun ve toraks özofagusunu gösteremedi; pilin özofagusta '
                                                   'takılı kaldığı anlaşılamadı.',
                                'teaching_point': 'Özofagus yabancı cisimlerinde USG tanısal değildir; iki yönlü '
                                                  'direkt grafiler standarttır.',
                                'text': 'Sadece batın ultrasonografisi çekerek midede pil olup olmadığını ve yabancı '
                                        'cisim varlığını araştırmak'}],
                 'question': 'Düğme pil şüphesi olan bu hastada cismin yerini ve pil olduğunu doğrulamak için en uygun '
                             'radyolojik inceleme hangisidir?',
                 'stage_title': 'Laboratuvar ve Görüntüleme İncelemeleri'},
               { 'options': [ { 'explanation': 'Üst özofagusta takılı kalma, grafide çift halka (halo) ve lateralde '
                                               'step-off basamaklanması düğme pil impaksiyonunu kanıtlar.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Özofagusta Takılı Kalan Lityum Düğme Pil (Akut Perforasyon '
                                               'Riski).',
                                'text': 'Özofageal düğme pil impaksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Madeni paralarda çift halka halo işareti ve basamaklanma olmaz; '
                                                   'homojen tek disk şeklinde opak görünür.',
                                'teaching_point': 'Madeni para düzgün tek sınırlıdır; düğme pil ise çift halka ve '
                                                  'basamaklanma (step-off) gösterir.',
                                'text': 'Özofagusta takılı madeni para'},
                              { 'is_correct': False,
                                'scenario_update': 'Trakeal aspirasyonda stridor ve tek taraflı havalanma kaybı olur; '
                                                   'grafide özofagus koronal düzleminde disk görülmez.',
                                'teaching_point': 'Özofagustaki disk koronal planda düz görünür; trakeadaki disk ise '
                                                  'sagital planda kenar şeklinde durur.',
                                'text': 'Trakeobronşiyal yabancı cisim aspirasyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Kostik içiminde sıvı kimyasal temas vardır; grafide radyoopak '
                                                   'metalik pil diski izlenmez.',
                                'teaching_point': 'Düğme pil lokalize elektrik ve alkali yanığı yapan katı metalik '
                                                  'pildir; kostik sıvı değildir.',
                                'text': 'Akut kostik asit içimi'}],
                 'question': 'Özofagusta takılı kalmış, çift halka ve step-off belirtisi veren metalik opak cisim ile '
                             'kesin klinik tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Özofagustaki düğme pil mutlak cerrahi acildir (ilk 2 saat). Hasta '
                                               'derhal çocuk cerrahisi / gastroenteroloji tarafından rijit veya '
                                               'fleksibl endoskopi ile ameliyathaneye alınmalıdır. Mukozal hasar ve '
                                               'nekroz derinliği endoskopik olarak değerlendirilir.',
                                'is_correct': True,
                                'new_finding': 'Çocuk cerrahisi ve anestezi koordinesiyle hasta yarım saat içinde '
                                               'ameliyathaneye alındı (yutmanın 75. dakikası). Rijit endoskopiyle '
                                               'düğme pil başarıyla çıkarıldı. Özofagus mukozasında yüzeyel yanık '
                                               'görüldü, perforasyon gelişmediği teyit edildi. Hasta yoğun bakımda '
                                               'izleme alındı ve komplikasyonsuz iyileşti.',
                                'text': 'Perforasyon ve fistül gelişimini önlemek için çocuğu iki saat içinde acil '
                                        'endoskopik çıkarma amacıyla ameliyathaneye almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Pil erimedi; aksine alkali sızıntı aortayı delerek dakikalar '
                                                   'içinde ölümcül masif kanamaya yol açtı.',
                                'teaching_point': 'Özofagustaki pil beklenemez; her geçen dakika doku nekrozu ve fatal '
                                                  'fistül riskini katlar.',
                                'text': 'Pilin kendi kendine erimesini beklemek amacıyla hastaya 48 saat boyunca '
                                        'antiasit şurup içirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Körlemesine itme manevrası nekrotik özofagus duvarının '
                                                   'yırtılmasına ve pilin mediastene düşmesine yol açtı.',
                                'teaching_point': 'Körlemesine tüp ile pili itmek perforasyon riskini artırır; '
                                                  'KESİNLİKLE KONTRENDİKEDİR.',
                                'text': 'Endoskopiye gerek duymadan mide sondası ile pili zorla aşağı mideye doğru '
                                        'itmeye çalışmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Evde bekleyen çocukta trakeoözofageal fistül ve solunum yetmezliği '
                                                   'gelişti.',
                                'teaching_point': 'Özofagusta takılı kalan pil saatler içinde cerrahi acildir; eve '
                                                  'taburculuk yapılamaz.',
                                'text': 'Pili çıkartmadan önce hastayı 24 saat süreyle evine gönderip dışkı kontrolü '
                                        'yaptırmak'}],
                 'question': 'Özofagusta takılı düğme pil tanısı doğrulanan bu çocukta en uygun ve hayat kurtarıcı '
                             'yönetim adımı hangisidir?',
                 'stage_title': 'Zamanla Yarış ve Acil Endoskopik Çıkarma'}]}]
