# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Yeşil Alan Vakaları (Part 5: Y41 - Y50)
Odak: Bulantı, Kusma, Karın Ağrısı, İshal (GİS Acilleri - Yeşil Alan Ayaktan Yönetim)
Kılavuzlar: ESPGHAN, AAP, NASPGHAN, NICE
"""

GREEN_CASES_PART5 = [{'id': 'Y41',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '2 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Dün başlayan sulu ishal, günde 5-6 kez dışkılama ve hafif ateş',
  'history': "Annesi anlatıyor: 'Dün sabah kreşten geldikten sonra sulu, mukussuz, kansız dışkılamaya başladı. Ateşi "
             'evde 37.8°C ölçüldü. Dün iki kez kustu ama bugün kusması yok. Su ve çorba içebiliyor, bezini günde 3-4 '
             'kez ıslatıyor. Kreşteki birkaç arkadaşında da benzer şikayet varmış. Komşumuz pirinç lapası ve muz '
             "dışında bir şey vermememi söyledi.' Tartı: 12.4 kg.",
  'final_diagnosis': 'Akut Viral Gastroenterit (Hafif Dehidratasyon)',
  'disposition': 'Yeşil Alandan ORS Eğitimi, Yaşa Uygun Beslenme ve Kırmızı Bayrak Eğitimi ile Ayaktan Taburculuk',
  'case_pearl': 'Akut viral gastroenteritte dehidratasyon derecesi klinik olarak (genel durum, gözler, mukozalar, '
                'turgor, KDZ, idrar çıkışı) belirlenir; hafif dehidratasyonda kan tetkiki ve dışkı kültürü gerekmez. '
                'ESPGHAN önerisi düşük osmolariteli ORS ile her sulu dışkı sonrası 10 mL/kg kayıp replasmanı ve '
                'kısıtlamasız yaşa uygun beslenmedir; BRAT diyeti, laktozsuz formül rutini ve antidiyareik ilaçlar '
                'önerilmez.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Bir gündür sulu dışkılaması olan, oral alımı kısmen korunmuş bu 2 yaşındaki çocukta '
                         'muayenede önceliğiniz ne olmalıdır?',
             'options': [{'text': 'Genel durum, göz küreleri, gözyaşı, mukoza nemi, deri turgoru, kapiller dolum '
                                  'zamanı ve tartıyı değerlendirip batını palpe etmek',
                          'is_correct': True,
                          'explanation': 'Sulu ishalli çocukta dehidratasyon derecesi standart klinik bulgularla '
                                         'belirlenir ve tüm yönetim (oral, nazogastrik veya intravenöz sıvı) bu '
                                         'sınıflamaya göre planlanır. Batın muayenesi cerrahi patolojiyi dışlamak için '
                                         'gereklidir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.5°C, KTA 112/dk, SS 24/dk, SpO2 %99, KDZ 1.5 sn. '
                                         'Tartı 12.0 kg (2 hafta önceki aşı kontrolünde 12.4 kg). Aktif, oyuncakla '
                                         'ilgileniyor. Göz küreleri normal, ağlarken gözyaşı var, ağız mukozası hafif '
                                         'kuru, turgor anında dönüyor. Karın yumuşak, hassasiyet yok, bağırsak sesleri '
                                         'hiperaktif.'},
                         {'text': 'Ateş ve kreş öyküsü nedeniyle önce kulak zarları ile orofarenksi detaylı incelemek, '
                                  'hidrasyon değerlendirmesini oral sıvı denemesi sonrasına bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Kulak zarları ve orofarenks doğal bulundu. Hidrasyon değerlendirmesi '
                                             'ertelendiği için çocuğun sıvı açığı ve oral tolerans planı ilk saatte '
                                             'netleşmedi.',
                          'teaching_point': 'İshalli çocukta ilk hedef sıvı açığının klinik olarak '
                                            'derecelendirilmesidir; odak taraması önemlidir ama hidrasyon '
                                            'değerlendirmesinin yerine geçmez.'},
                         {'text': 'Kusma öyküsü nedeniyle muayene öncesinde intravenöz ondansetron yapıp ardından sıvı '
                                  'açığını hesaplamak için tartı almak ve batını değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Bugün hiç kusması olmayan çocuğa gereksiz damar yolu açıldı; muayene ve '
                                             'hidrasyon sınıflaması 30 dakika gecikti.',
                          'teaching_point': 'Antiemetik yalnızca oral alımı engelleyen aktif kusmada düşünülür ve oral '
                                            'form yeterlidir; önce dehidratasyon derecesi belirlenmelidir.'},
                         {'text': 'Ateşli ishalde bakteriyemi olasılığını değerlendirmek için muayeneyle eş zamanlı '
                                  'damar yolu açıp hemogram, CRP ve kan kültürü almak',
                          'is_correct': False,
                          'scenario_update': 'Damar yolu iki denemede açılabildi; çocuk ajite oldu ve sonrasında sıvı '
                                             'içmeyi reddetti. Hemogram ve CRP sınırda normal geldi, yönetimi '
                                             'değiştirmedi.',
                          'teaching_point': 'Genel durumu iyi, kanlı dışkısı olmayan ishalli çocukta rutin kan tetkiki '
                                            'önerilmez; invaziv girişim oral rehidratasyon başarısını da '
                                            'azaltabilir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Tartısında yaklaşık %3 kayıp olan, aktif ve hafif mukozal kuruluğu bulunan bu çocukta hangi '
                         'tetkik yaklaşımı uygundur?',
             'options': [{'text': 'Karın ağrısı ve hiperaktif bağırsak seslerini değerlendirmek için ayakta direkt '
                                  'batın grafisi ve batın ultrasonografisi isteyip cerrahi patolojiyi dışlamak',
                          'is_correct': False,
                          'scenario_update': 'Grafide yaygın gaz-sıvı içerikli ince bağırsak ansları görüldü; bulgu '
                                             'non-spesifik olarak raporlandı ve aile kaygılandı.',
                          'teaching_point': 'Yumuşak, hassasiyetsiz karın ve sulu ishal tablosunda görüntüleme endike '
                                            'değildir; non-spesifik bulgular gereksiz endişe ve tetkik zincirine yol '
                                            'açar.'},
                         {'text': 'Ek tetkik istemeden acilde gözetimli oral sıvı denemesi yapmak, kusmadan '
                                  'içebildiğini ve idrar çıkışının sürdüğünü teyit etmek',
                          'is_correct': True,
                          'explanation': 'Hafif sıvı kaybı olan, genel durumu iyi ve kanlı dışkısı olmayan çocukta '
                                         "tanı kliniktir. En değerli 'tetkik' gözetimli oral tolerans denemesidir; kan "
                                         've dışkı incelemeleri yönetimi değiştirmez.',
                          'new_finding': 'Çocuk 1 saat içinde kaşıkla ve bardakla toplam 150 mL düşük osmolariteli ORS '
                                         'içti, kusmadı. Bezini bir kez ıslattı. Gözlem sırasında bir kez sulu, kansız '
                                         'dışkılama oldu.'},
                         {'text': 'Kreşte benzer olgular bulunduğu için etkenin belirlenmesi amacıyla dışkı kültürü ve '
                                  'viral antijen paneli gönderip sonuca göre tedaviyi düzenlemek',
                          'is_correct': False,
                          'scenario_update': 'Dışkı viral antijen testi 2 gün sonra pozitif geldi; sonuç tedaviyi '
                                             'değiştirmedi ve aile kontrol için gereksiz yere tekrar başvurdu.',
                          'teaching_point': 'Etken tespiti salgın araştırması veya kanlı ishal dışında bireysel '
                                            'tedaviyi değiştirmez; rutin dışkı tetkiki önerilmez.'},
                         {'text': 'Hafif sıvı kaybı nedeniyle elektrolit bozukluğu olabileceğini düşünerek venöz kan '
                                  'gazı, sodyum, potasyum ve kan şekeri ölçümü istemek',
                          'is_correct': False,
                          'scenario_update': 'Venöz kan gazında HCO3 20 mmol/L, sodyum 137 mEq/L, potasyum 3.9 mEq/L '
                                             'bulundu; sonuçlar normal sınırlarda olup yönetimi değiştirmedi.',
                          'teaching_point': 'Elektrolit ölçümü orta-ağır dehidratasyonda, intravenöz sıvı planlanan '
                                            'veya öykü ve muayenesi uyumsuz çocuklarda gereklidir; hafif olguda '
                                            'katkısı yoktur.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Kreş temaslı, akut başlangıçlı sulu ishal, hafif ateş, %3 kilo kaybı ve oral toleransı '
                         'korunmuş bu çocuktaki en olası tanı nedir?',
             'options': [{'text': 'Akut giardiyaz',
                          'is_correct': False,
                          'scenario_update': 'Giardiyazda tablo genellikle sinsi başlar; yağlı, kötü kokulu dışkı, '
                                             'şişkinlik ve haftalarca süren şikayetler beklenir.',
                          'teaching_point': 'Bir günlük akut sulu ishal ve ateş, protozoon enfeksiyonundan çok viral '
                                            'etiyolojiye uyar.'},
                         {'text': 'Akut invaziv bakteriyel enterokolit',
                          'is_correct': False,
                          'scenario_update': 'İnvaziv bakteriyel enterokolitte genellikle yüksek ateş, kanlı-mukuslu '
                                             'dışkı ve tenezm beklenir; bu çocukta bu bulgular yok.',
                          'teaching_point': 'Kansız sulu ishal ve hafif ateş invaziv bakteriyel enfeksiyondan çok '
                                            'viral etkenleri düşündürür.'},
                         {'text': 'Antibiyotik ilişkili ishal',
                          'is_correct': False,
                          'scenario_update': 'Öyküde son 8 haftada antibiyotik kullanımı yok; kreş kümelenmesi '
                                             'bulaşıcı bir etkeni destekliyor.',
                          'teaching_point': 'Antibiyotik ilişkili ishal tanısı yakın dönem antibiyotik kullanımı '
                                            'öyküsü gerektirir.'},
                         {'text': 'Akut viral gastroenterit, hafif dehidratasyon',
                          'is_correct': True,
                          'explanation': 'Kreş kümelenmesi, akut sulu kansız ishal ve hafif ateş viral etiyolojiyi '
                                         'düşündürür. %3-5 kilo kaybı, aktif genel durum ve hafif mukozal kuruluk '
                                         'hafif dehidratasyonla uyumludur.',
                          'new_finding': 'Tanı: Akut Viral Gastroenterit - Hafif Dehidratasyon (<%5).'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': "Oral sıvıyı tolere eden bu 12 kg'lık çocuk için en uygun taburculuk önerisi hangisidir?",
             'options': [{'text': 'Her sulu dışkı sonrası yaklaşık 120 mL düşük osmolariteli ORS, yaşa uygun normal '
                                  'beslenmeye devam ve dehidratasyon bulguları için dönüş eğitimi vermek',
                          'is_correct': True,
                          'explanation': 'ESPGHAN önerisine göre devam eden kayıplar her sulu dışkı sonrası 10 mL/kg '
                                         'ORS ile karşılanır, diyet kısıtlanmaz. Azalan idrar, uykuya meyil, kanlı '
                                         'dışkı veya inatçı kusmada dönüş anlatılır.',
                          'new_finding': 'Aileye ORS hazırlanışı gösterildi, yazılı dönüş kriterleri verildi. 48. '
                                         "saatteki telefon kontrolünde ishal sıklığı günde 2'ye indi, çocuk normal "
                                         'besleniyordu.'},
                         {'text': 'Ateş ve kreş kümelenmesi nedeniyle beş gün oral azitromisin başlamak, ORS ve normal '
                                  'beslenmeyi sürdürmek ve kreşe ara verdirmek',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik başlanan çocukta ikinci gün kusma ve ishal sıklığı arttı; '
                                             'tablo kendi seyrinde dördüncü günde düzeldi.',
                          'teaching_point': 'Kansız sulu ishalde ampirik antibiyotik endikasyonu yoktur; yan etki ve '
                                            'direnç riskini artırır.'},
                         {'text': 'Dışkı sayısını azaltmak için yaşa uygun dozda oral loperamid başlamak, ORS ve '
                                  'normal beslenmeyi sürdürüp üç gün sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Loperamid sonrası çocukta karın şişliği ve uyku hali gelişti; aile acile '
                                             'geri getirdi.',
                          'teaching_point': 'Loperamid çocuklarda ileus ve santral sinir sistemi depresyonu riski '
                                            'nedeniyle akut gastroenteritte önerilmez.'},
                         {'text': 'Barsağı dinlendirmek için 24 saat yalnızca ORS ve pirinç lapası vermek, süt '
                                  'ürünlerini bir hafta kesmek, sonra normal diyete geçmek',
                          'is_correct': False,
                          'scenario_update': 'Kısıtlı diyetle çocuk 3 gün sonra halsiz ve iştahsız başvurdu; ishal '
                                             'süresi kısalmadı, kilo kaybı derinleşti.',
                          'teaching_point': 'Hafif-orta dehidratasyonda rehidratasyonla birlikte yaşa uygun normal '
                                            'beslenmeye hemen devam edilir; BRAT diyeti ve rutin süt kısıtlaması '
                                            'önerilmez.'}]}]},
 {'id': 'Y42',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '6 Yaşında',
  'gender': 'Kız',
  'complaint': 'Bir doğum günü partisinden 3 saat sonra başlayan ani, tekrarlayan kusma ve kramp tarzı karın ağrısı',
  'history': "Ailesi anlatıyor: 'Öğleden sonra bir doğum günü partisinde kremalı pasta ve tavuklu sandviç yedi. Eve "
             'geldikten kısa süre sonra aniden fışkırır tarzda kusmaya başladı; son 2 saatte 6 kez kustu, su bile '
             "içemiyor. Partideki 3 çocukta da aynı saatlerde kusma başlamış. Ateşi yok, henüz ishali olmadı.' Kusmuk "
             'safralı veya kanlı değil. Tartı: 20 kg.',
  'final_diagnosis': 'Besin Zehirlenmesi (Stafilokoksik Enterotoksin Kaynaklı)',
  'disposition': 'Yeşil Alanda Tek Doz Oral Ondansetron + ORS ile Rehidrasyon ve Ayaktan Taburculuk',
  'case_pearl': 'Yemekten 1-6 saat sonra başlayan ani şiddetli kusma, kramp ve aynı yemeği yiyenlerde kümelenme S. '
                'aureus veya B. cereus kaynaklı hazır toksin aracılı besin zehirlenmesini düşündürür. Tablo 24 saat '
                'içinde kendiliğinden geriler; tetkik ve antibiyotik gerekmez. Tek doz oral ondansetron (8-15 kg: 2 '
                'mg, 15-30 kg: 4 mg, >30 kg: 8 mg) oral rehidratasyon başarısını artırır. Toplu olgular halk sağlığına '
                'bildirilmelidir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Ani başlangıçlı tekrarlayan kusması olan, partideki diğer çocuklarda da benzer şikayet '
                         'bulunan bu kız çocuğunda ilk değerlendirmede neye odaklanırsınız?',
             'options': [{'text': 'Kusmuk niteliğini sorgulayıp vital bulguları, hidrasyon durumunu, bilinç düzeyini '
                                  've karın muayenesini değerlendirerek cerrahi ve sistemik kırmızı bayrakları '
                                  'dışlamak',
                          'is_correct': True,
                          'explanation': 'Akut kusmada safralı veya kanlı kusma, peritoneal irritasyon, bilinç '
                                         'değişikliği ve ağır dehidratasyon gibi kırmızı bayraklar ilk muayenede '
                                         'aranmalıdır; yönetim hidrasyon durumuna göre planlanır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 108/dk, SS 20/dk, SpO2 %99, TA 98/62 mmHg, '
                                         'KDZ 1.5 sn. Bilinç açık, bulantılı ve halsiz. Ağız mukozası hafif kuru, '
                                         'gözyaşı var. Karın yumuşak, epigastriumda hafif hassasiyet; defans, rebound '
                                         've kitle yok. Meningeal irritasyon bulgusu yok.'},
                         {'text': 'Kusmanın hızla durdurulması için muayeneden önce intramüsküler metoklopramid yapıp '
                                  'bulantı geçtikten sonra karın ve hidrasyon muayenesini tamamlamak',
                          'is_correct': False,
                          'scenario_update': 'Metoklopramid sonrası çocukta huzursuzluk ve boyunda istemsiz kasılma '
                                             'gelişti; biperiden gerekti, muayene gecikti.',
                          'teaching_point': 'Metoklopramid çocuklarda ekstrapiramidal yan etki riski taşır; antiemetik '
                                            'gerekiyorsa tercih ondansetrondur ve önce muayene yapılmalıdır.'},
                         {'text': 'Epigastrik ağrı ve kusma nedeniyle muayeneden önce damar yolu açıp tam kan sayımı, '
                                  'amilaz, lipaz ve karaciğer enzimlerini göndermek',
                          'is_correct': False,
                          'scenario_update': 'Kan alımı sırasında çocuk iki kez daha kustu. Amilaz, lipaz ve karaciğer '
                                             'enzimleri normal geldi; tetkikler yönetimi değiştirmedi.',
                          'teaching_point': 'Öykü ve muayene uyumluyken rutin biyokimya gerekmez; tetkik kararı '
                                            'muayene bulgularına göre verilmelidir.'},
                         {'text': 'Toplu başvuru nedeniyle olası kimyasal maruziyeti düşünerek önce pupilla, '
                                  'salivasyon ve terleme muayenesi yapıp zehir danışma merkezini aramak',
                          'is_correct': False,
                          'scenario_update': 'Pupillalar normal, salivasyon ve terleme artışı yok. Zehir danışma '
                                             'görüşmesi kolinerjik tablo olmadığını teyit etti; hidrasyon '
                                             'değerlendirmesi 20 dakika gecikti.',
                          'teaching_point': 'Kolinerjik bulgu olmayan, yemekle zaman ilişkisi net kusmada ilk öncelik '
                                            'hidrasyon ve akut batın değerlendirmesidir.'}]},
            {'stage_title': 'Tetkik ve İlk Destek Kararı',
             'question': 'Hafif sıvı kaybı olan, karın muayenesi rahat ve ateşsiz bu çocukta tetkik ve ilk destek '
                         'yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Karın ağrısının cerrahi nedenlerini ekarte etmek için batın ultrasonografisi '
                                  'isteyip sonuç çıkana kadar oral alımı tamamen kapalı tutmak',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografi 2 saat sonra çekildi ve normaldi. Bu sürede oral alımı '
                                             'kapatılan çocuğun ağız kuruluğu belirginleşti.',
                          'teaching_point': 'Yumuşak karın ve kısa süreli kramp tarzı ağrıda görüntüleme gerekmez; '
                                            'oral alımın gereksiz kesilmesi dehidratasyonu derinleştirir.'},
                         {'text': 'Kan tetkiki istemeden kiloya uygun tek doz oral ondansetron vermek ve yarım saat '
                                  'sonra küçük yudumlarla ORS denemesi başlatmak',
                          'is_correct': True,
                          'explanation': 'Hafif dehidratasyonlu ve kırmızı bayrağı olmayan kusmada laboratuvar tetkiki '
                                         'gerekmez. Tek doz oral ondansetron kusmayı azaltır, oral rehidratasyon '
                                         'başarısını artırır ve intravenöz sıvı ihtiyacını düşürür.',
                          'new_finding': '20 kg için 4 mg oral dağılan ondansetron verildi. 30 dakika sonra 5 dakikada '
                                         'bir 10-15 mL ORS başlandı; 1 saatte 200 mL içti, kusmadı. Bir kez sulu '
                                         'dışkılama oldu.'},
                         {'text': 'Altı kez kusma nedeniyle damar yolu açıp elektrolitleri göndermek ve 20 mL/kg serum '
                                  'fizyolojik bolusunu ardından idame sıvıyla sürdürmek',
                          'is_correct': False,
                          'scenario_update': 'Elektrolitler normal geldi. İntravenöz sıvı sırasında çocuk 3 saat '
                                             'acilde kaldı; oral alım hiç denenmediği için taburculuk gecikti.',
                          'teaching_point': 'Hafif dehidratasyonda ilk seçenek oral rehidratasyondur; intravenöz sıvı '
                                            'oral tedavinin başarısız olduğu veya ağır dehidratasyonda gerekir.'},
                         {'text': 'Partideki diğer çocuklarla kümelenme olduğu için dışkı kültürü ve kusmuk örneğinden '
                                  'toksin analizi isteyip sonuçlar gelene dek gözlemde tutmak',
                          'is_correct': False,
                          'scenario_update': 'Çocuğun ishali olmadığından dışkı örneği alınamadı; kusmuk örneği '
                                             'laboratuvarca kabul edilmedi ve gözlem süresi gereksiz uzadı.',
                          'teaching_point': 'Örnekleme salgın araştırmasında halk sağlığı birimince planlanır; '
                                            'bireysel hastanın acil yönetimini değiştirmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Yemekten 1-3 saat sonra başlayan ani kusma, kramp, ateş yokluğu ve aynı yemeği yiyenlerde '
                         'kümelenme varlığında en olası tanı nedir?',
             'options': [{'text': 'Stafilokok enterotoksini kaynaklı besin zehirlenmesi',
                          'is_correct': True,
                          'explanation': 'Kremalı tatlı ve tavuklu sandviç gibi oda ısısında bekleyen gıdalarda S. '
                                         "aureus'un ürettiği ısıya dayanıklı enterotoksin 1-6 saat içinde ani kusma ve "
                                         'kramp yapar; ateş genellikle yoktur ve tablo 24 saatte geriler.',
                          'new_finding': 'Tanı: Stafilokokal Enterotoksin Kaynaklı Akut Besin Zehirlenmesi. Toplu olgu '
                                         'nedeniyle İl Sağlık Müdürlüğüne bildirim yapıldı.'},
                         {'text': 'Salmonella gastroenteriti',
                          'is_correct': False,
                          'scenario_update': 'Salmonella enfeksiyonunda kuluçka süresi 6-72 saattir ve tabloya '
                                             'genellikle ateş ile ishal hakimdir.',
                          'teaching_point': 'Ateşsiz, birkaç saat içinde başlayan kusma baskın tablo invaziv '
                                            'bakteriyel enfeksiyondan çok toksin aracılıdır.'},
                         {'text': 'Diyabetik ketoasidoz',
                          'is_correct': False,
                          'scenario_update': 'Poliüri-polidipsi öyküsü, Kussmaul solunumu ve hiperglisemi yok; '
                                             'kümelenen olgular metabolik bir nedenle açıklanamaz.',
                          'teaching_point': 'Kusan çocukta ketoasidoz akılda tutulmalıdır ancak toplu ve zamanla '
                                            'ilişkili başvuru ortak maruziyeti gösterir.'},
                         {'text': 'Akut viral gastroenterit',
                          'is_correct': False,
                          'scenario_update': 'Viral gastroenterit de kümelenebilir ancak kuluçka süresi genellikle '
                                             '12-48 saattir; tüm çocukların aynı saatlerde başlaması ortak gıda '
                                             'maruziyetini düşündürür.',
                          'teaching_point': 'Birkaç saatlik kısa kuluçka ve ortak yemek, bulaşıcı virüsten çok hazır '
                                            'toksin aracılı tabloyu düşündürür.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': "Ondansetron sonrası ORS'yi tolere eden bu çocuğun taburculuk planı nasıl olmalıdır?",
             'options': [{'text': 'Ortak gıda kaynağı ve kümelenme nedeniyle ampirik beş günlük oral siprofloksasin '
                                  'başlayıp ORS ve normal beslenme ile taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik toksin aracılı tabloya etki etmedi; çocuk ikinci gün '
                                             'antibiyotiğe bağlı bulantı ile tekrar başvurdu.',
                          'teaching_point': 'Hazır toksinle oluşan besin zehirlenmesinde bakteri invazyonu yoktur; '
                                            'antibiyotik endikasyonu bulunmaz.'},
                         {'text': 'Evde kullanmak üzere üç gün boyunca günde iki kez oral ondansetron reçete edip ORS '
                                  'ile normal beslenmeyi sürdürmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Kusması zaten 12 saatte duran çocuğa verilen tekrarlayan dozlar sonrası '
                                             'ishal sıklığı arttı.',
                          'teaching_point': 'Ondansetronun kanıtı acilde tek doz kullanım içindir; evde çoklu doz '
                                            'rutin önerilmez ve ishali artırabilir.'},
                         {'text': 'Sıvı açığını güvenceye almak için tolere etse de 6 saat intravenöz idame sıvı '
                                  'vererek gözlemlemek ve sabah taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Oral alımı iyi olan çocuk gereksiz yere gece boyunca acilde kaldı; serum '
                                             'yerinde flebit gelişti.',
                          'teaching_point': 'Oral toleransı sağlanmış hafif dehidratasyonlu çocuk ayaktan izlenir; '
                                            'gereksiz intravenöz sıvı ve uzun gözlem komplikasyon riskini artırır.'},
                         {'text': 'ORS ve yaşa uygun beslenmeye devam, kusma tekrarlarsa küçük yudumlar, kırmızı '
                                  'bayrak eğitimi ve toplu olgu nedeniyle halk sağlığına bildirim yapmak',
                          'is_correct': True,
                          'explanation': 'Tablo kendini sınırlar; destek tedavi yeterlidir. Safralı veya kanlı kusma, '
                                         'uykuya meyil, idrar azalması ya da 24 saati aşan şikayetlerde dönüş '
                                         'anlatılır. Ortak kaynaklı toplu olgular bildirimi zorunlu durumlardır.',
                          'new_finding': 'Çocuk ayaktan taburcu edildi. Ertesi gün aile ile yapılan görüşmede '
                                         'kusmasının gece kesildiği, sabah kahvaltı yaptığı öğrenildi. Partideki diğer '
                                         'çocuklar da 24 saat içinde iyileşti.'}]}]},
 {'id': 'Y43',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '5 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Bir aydır iç çamaşırını sık sık kirletme, karın şişliği ve tuvalete gitmek istememe',
  'history': "Annesi anlatıyor: 'Yaklaşık 1 aydır külodunu kirletiyor, çamur kıvamında lekeler buluyorum, ishal mi "
             'diye düşündük. Ama tuvalette haftada bir kez kalın, sert dışkı yapıyor, bazen tuvaleti tıkıyor. Tuvalete '
             'oturmak istemiyor, bacaklarını çaprazlayıp parmak ucunda kasılarak bekliyor. Ara ara karnı ağrıyor, '
             "iştahı azaldı. Kreşte arkadaşları kokudan dolayı onunla dalga geçiyor.' Yenidoğan döneminde mekonyumunu "
             'ilk gün çıkarmış. Kilo-boy gelişimi persentilinde.',
  'final_diagnosis': 'Fonksiyonel Kabızlık, Fekal İmpaksiyon ve Taşma Tipi Fekal İnkontinans (Enkoprezis)',
  'disposition': 'Yeşil Alandan Oral PEG Disimpaksiyon, İdame Laksatif ve Davranışsal Tuvalet Eğitimi ile Taburculuk',
  'case_pearl': "Çamaşır kirletmesi olan çocukta 'ishal' yakınması sıklıkla rektumdaki sert kitlenin etrafından sızan "
                'sıvı dışkıdır. Fonksiyonel kabızlıkta tanı Roma IV kriterleri ve muayeneye dayanır; alarm bulgusu '
                "yoksa rutin batın grafisi ve kan tetkiki gerekmez. ESPGHAN/NASPGHAN'a göre ilk seçenek oral PEG ile "
                'disimpaksiyon (1-1.5 g/kg/gün, 3-6 gün), ardından en az 2 ay idame (0.4-0.8 g/kg/gün) ve davranışsal '
                'tuvalet eğitimidir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Çamaşır kirletmesi, seyrek sert dışkılama ve tutma davranışı tarif edilen bu çocukta '
                         'muayenede neyi mutlaka değerlendirmelisiniz?',
             'options': [{'text': 'Karın ağrısı ve iştahsızlık nedeniyle sağ alt kadran hassasiyeti, rebound ve psoas '
                                  'bulgularını değerlendirip cerrahi konsültasyon gerekliliğine karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Sağ alt kadran hassasiyeti ve peritoneal bulgu saptanmadı. Sol alt '
                                             'kadrandaki kitle ve perianal bulgular bu odakla değerlendirilmedi.',
                          'teaching_point': 'Bir aylık seyrek-sert dışkılama ve tutma davranışında öncelik peritonit '
                                            'aramak değil, dışkı kitlesi ve organik neden alarm bulgularını '
                                            'değerlendirmektir.'},
                         {'text': 'Davranışsal bir sorun olduğunu düşünüp çocuğun tuvalet alışkanlıklarını ve okul '
                                  'stresini sorgulamak, fizik muayene sonrasında çocuk psikiyatrisine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Psikiyatri randevusu 3 ay sonraya verildi; bu sürede çamaşır kirletmesi '
                                             've karın ağrısı arttı.',
                          'teaching_point': 'Tutma davranışı ve sosyal sorunlar sonuçtur; altta yatan dışkı birikimi '
                                            'tedavi edilmeden psikososyal destek tek başına yetersiz kalır.'},
                         {'text': 'Karın palpasyonunda kitle aramak, lumbosakral bölgeyi ve alt ekstremite nörolojik '
                                  'muayenesini değerlendirmek, perianal inspeksiyon ve gerekirse rektal muayene yapmak',
                          'is_correct': True,
                          'explanation': 'Kabızlıkta abdominal fekal kitle, perianal fissür ve sfinkter '
                                         'değerlendirmesi tanıyı destekler. Lumbosakral gamze, kıl yumağı, alt '
                                         'ekstremite refleks ve kuvvet kaybı spinal disrafizm gibi organik nedenler '
                                         'için alarm bulgularıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 94/dk, SS 20/dk, TA 96/60 mmHg. Sol alt '
                                         'kadrandan göbek altına uzanan, sert, hareketli, ağrısız kitle palpe edildi. '
                                         'Lumbosakral bölge doğal, gamze veya kıl yumağı yok. Alt ekstremite refleks '
                                         've kas gücü normal. Perianal bölgede dışkı bulaşı ve saat 6 hizasında küçük '
                                         'fissür; anal açıklıkta sert dışkı görülüyor.'},
                         {'text': 'Dışkı sızıntısını ishal kabul edip hidrasyon bulgularını, perianal cildi ve karın '
                                  'muayenesini değerlendirmek, dışkı mikroskopisi için örnek istemek',
                          'is_correct': False,
                          'scenario_update': 'Hidrasyon normal bulundu. Dışkı mikroskopisinde parazit görülmedi; '
                                             'şikayetin nedeni hakkında yol gösterici bilgi elde edilmedi.',
                          'teaching_point': 'Sert ve seyrek dışkılama ile birlikte olan çamaşır kirletmesinde '
                                            'sızıntının kaynağı rektumdaki dışkı kitlesi olabilir; bu ayrım muayeneyle '
                                            'yapılır.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Alarm bulgusu olmayan, abdominal kitle ve anal fissür saptanan bu çocukta tetkik '
                         'yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Organik nedenleri dışlamak için tam kan sayımı, tiroid fonksiyon testleri, '
                                  'kalsiyum, çölyak serolojisi ve kurşun düzeyi istemek',
                          'is_correct': False,
                          'scenario_update': 'Tüm sonuçlar normal geldi; çocuk 4 tüp kan için iki kez venöz girişime '
                                             'maruz kaldı ve aile tedaviyi sonuçlar gelene kadar erteledi.',
                          'teaching_point': 'Büyüme gelişmesi normal ve alarm bulgusu olmayan çocukta rutin '
                                            'laboratuvar taraması gerekmez; tedavi gecikmemelidir.'},
                         {'text': 'Ek tetkik yapmadan klinik tanıyla tedaviye başlamak; büyüme, nörolojik muayene ve '
                                  'mekonyum öyküsü normal olduğundan organik neden aramamak',
                          'is_correct': True,
                          'explanation': 'Roma IV kriterlerini karşılayan ve alarm bulgusu olmayan çocukta tanı '
                                         'kliniktir. Normal büyüme, ilk gün mekonyum çıkışı ve normal nörolojik '
                                         'muayene organik nedenleri büyük ölçüde dışlar; tetkikler yönetimi '
                                         'değiştirmez.',
                          'new_finding': 'Laboratuvar veya görüntüleme istenmedi. Aileye şikayetlerin kaynağı muayene '
                                         'bulguları üzerinden görsel bir çizimle anlatıldı; sızıntının ishal olmadığı '
                                         'açıklandı.'},
                         {'text': 'Mekonyum öyküsü normal olsa da hastalığı dışlamak için baryumlu kolon grafisi ve '
                                  'rektal emme biyopsisi planlamak üzere gastroenterolojiye yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Kontrast grafide rektumda dilatasyon ve dışkı görüldü, geçiş zonu yoktu. '
                                             'Biyopsi randevusu beklenirken tedavi başlanmadı.',
                          'teaching_point': 'İlk 48 saatte mekonyum çıkışı, geç başlangıç ve tutma davranışı organik '
                                            'aganglionozis olasılığını düşürür; invaziv tetkik alarm bulgusuna göre '
                                            'planlanır.'},
                         {'text': 'Kitlenin niteliğini ve kolondaki dışkı yükünü belgelemek amacıyla ayakta direkt '
                                  'batın grafisi çekip tedavi planını grafi bulgusuna göre yapmak',
                          'is_correct': False,
                          'scenario_update': 'Grafide kolonda yoğun dışkı görüldü; muayenede zaten belirlenen bulguyu '
                                             'doğruladı ve yönetimi değiştirmedi, çocuk radyasyona maruz kaldı.',
                          'teaching_point': 'ESPGHAN/NASPGHAN rutin batın grafisini önermez; rektal muayene '
                                            'yapılamayan veya öykü güvenilmeyen seçilmiş olgularda düşünülebilir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Tutma davranışı, haftada bir sert dışkılama, abdominal fekal kitle ve çamaşır kirletmesi '
                         'olan bu çocuktaki tanı nedir?',
             'options': [{'text': 'Fonksiyonel kabızlık, fekal impaksiyon ve taşma inkontinansı',
                          'is_correct': True,
                          'explanation': 'Tutma davranışı, seyrek iri sert dışkı, palpabl fekal kitle ve sıvı dışkı '
                                         'sızıntısı Roma IV fonksiyonel kabızlık ve impaksiyona bağlı taşma '
                                         'inkontinansını gösterir.',
                          'new_finding': 'Tanı: Fonksiyonel Kabızlık, Fekal İmpaksiyon ve Retentif Fekal İnkontinans '
                                         '(Enkoprezis).'},
                         {'text': 'Hirschsprung hastalığı',
                          'is_correct': False,
                          'scenario_update': 'İlk gün mekonyum çıkışı, geç başlangıç ve rektumda dışkı bulunması bu '
                                             'tanıyla uyumlu değildir.',
                          'teaching_point': 'Aganglionoziste rektum genellikle boştur ve şikayetler yenidoğan '
                                            'döneminde başlar; çamaşır kirletmesi nadirdir.'},
                         {'text': 'Akut infeksiyöz ishal',
                          'is_correct': False,
                          'scenario_update': 'Bir aylık seyir, sert seyrek dışkılama ve ateş yokluğu enfeksiyöz '
                                             'ishalle açıklanamaz.',
                          'teaching_point': 'Çamaşırdaki sıvı dışkı, sert kitle etrafından sızan taşma ishali '
                                            'olabilir.'},
                         {'text': 'Hipotiroidiye bağlı kabızlık',
                          'is_correct': False,
                          'scenario_update': 'Büyüme hızı normal, yorgunluk, soğuk intoleransı veya kuru cilt gibi '
                                             'bulgular yok.',
                          'teaching_point': 'Endokrin nedenler büyüme geriliği ve sistemik bulgularla birlikte '
                                            'düşünülür.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': "Bu 18 kg'lık çocukta ilk tedavi planı nasıl olmalıdır?",
             'options': [{'text': 'Acilde iki gün üst üste fosfatlı rektal lavman uygulayıp dışkı boşaldıktan sonra '
                                  'lif ağırlıklı diyet ve bol sıvı önererek ilaçsız izlemek',
                          'is_correct': False,
                          'scenario_update': 'Lavman sonrası çocuk tuvaletten korkmaya başladı; idame tedavi '
                                             'verilmediği için 3 hafta içinde impaksiyon tekrarladı.',
                          'teaching_point': 'Oral PEG disimpaksiyonda lavman kadar etkilidir ve daha az travmatiktir; '
                                            'idame laksatif verilmeden yalnız diyetle nüks kaçınılmazdır.'},
                         {'text': 'Uyarıcı laksatif olarak her gece oral senna başlamak, yanına simetikon eklemek ve '
                                  'sızıntı için çocuğa gece bezi kullandırmak',
                          'is_correct': False,
                          'scenario_update': 'Senna ile karın krampları arttı; çocuk ağrılı dışkılamadan daha çok '
                                             'korkarak tutma davranışını sürdürdü.',
                          'teaching_point': 'Uyarıcı laksatifler ilk basamak değildir; ozmotik laksatif ve davranışsal '
                                            'tedavi temel yaklaşımdır.'},
                         {'text': 'Günlük oral laktüloz 1 mL/kg ile başlamak, dışkı yumuşadığında bir hafta içinde '
                                  'kesmek ve tuvalet eğitimini kreşe bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Mevcut impaksiyon çözülmeden başlanan düşük doz laktüloz şişkinlik ve '
                                             'sızıntıyı artırdı; erken kesilince şikayetler tekrarladı.',
                          'teaching_point': 'Önce impaksiyon temizlenmeli, ardından idame tedavi en az 2 ay ve düzenli '
                                            'dışkılama sağlandıktan sonra kademeli azaltılmalıdır.'},
                         {'text': 'Oral PEG ile 1-1.5 g/kg/gün dozda 3-6 gün disimpaksiyon, ardından en az iki ay '
                                  'idame dozu, yemek sonrası tuvalet oturuşu ve ödül çizelgesi',
                          'is_correct': True,
                          'explanation': 'ESPGHAN/NASPGHAN önerisi oral PEG ile disimpaksiyon, ardından 0.4-0.8 '
                                         'g/kg/gün idame ve en az 2 ay sürdürülen davranışsal tedavidir. Fissür için '
                                         'oturma banyosu ve bariyer krem eklenir.',
                          'new_finding': 'PEG 3350 ile 3 gün disimpaksiyon yapıldı, karındaki kitle kayboldu. İdame '
                                         'doza geçildi; 2 hafta sonraki kontrolde günlük yumuşak dışkılama başladı, '
                                         'çamaşır kirletmesi durdu.'}]}]},
 {'id': 'Y44',
  'category': '👶 Ağlayan, Emmeyen, Huzursuz Bebek',
  'age': '6 Haftalık',
  'gender': 'Kız',
  'complaint': 'Üç saattir aniden başlayan, emzirmeyle ve kucakta sallamayla susmayan şiddetli ağlama',
  'history': "Annesi anlatıyor: 'Normalde çok sakin bir bebek, akşamları biraz huysuzlanır ama hemen susar. Bugün "
             'öğleden sonra uykusundan çığlıkla uyandı, üç saattir ara vermeden ağlıyor. Memeyi birkaç kez aldı ama '
             "hemen bırakıp yeniden ağladı.' Ateş, kusma, ishal yok. Gaz ve dışkı çıkışı olağan. Term doğmuş, gebelik "
             've doğum sorunsuz. Yalnız anne sütü alıyor, kilo alımı iyi. Evde düşme veya bilinen bir kaza yok. Kat '
             'kat giydirilmiş, ayağında çorap ve patik var.',
  'final_diagnosis': 'Ayak Parmağında Kıl (Saç Teli) Turnike Sendromu',
  'disposition': 'Saç Telinin Tam Çıkarılması ve Perfüzyon Kontrolü Sonrası Yeşil Alandan Taburculuk',
  'case_pearl': 'Ani başlayan, avutulamayan ağlamada bebek mutlaka tamamen soyularak muayene edilmelidir: parmaklar, '
                'penis/klitoris ve uvula çevresine dolanan saç teli ya da iplik zamanla ödemle gömülerek iskemi yapar. '
                'Doğum sonrası anne saç dökülmesi tipik risk dönemidir. Lif tamamen çıkarılmalı; gömülü kalan ikinci '
                'bir tur sık gözden kaçar. Parmak tabanında lif kalmadığından emin olunmalı ve perfüzyonun düzeldiği '
                'izlenerek taburcu edilmelidir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Ateşsiz, iyi beslenen ama üç saattir avutulamayan bu 6 haftalık bebeğin değerlendirmesinde '
                         'ilk yaklaşımınız nedir?',
             'options': [{'text': 'Akşam saatlerinde artan ağlama öyküsü nedeniyle tabloyu fonksiyonel kabul edip '
                                  'simetikon damla ve gaz masajı önererek aileyi rahatlatmak',
                          'is_correct': False,
                          'scenario_update': 'Bebek eve gönderildi; ağlama gece boyu sürdü ve sabah sağ ayakta '
                                             'belirgin morarma ile geri getirildi.',
                          'teaching_point': 'Ani başlayan, alışılmış örüntüye uymayan ve avutulamayan ağlama '
                                            'fonksiyonel kabul edilmeden önce organik nedenler için baştan ayağa '
                                            'muayene gerekir.'},
                         {'text': 'Vital bulguları aldıktan sonra bebeği tamamen soyup parmakları, genital bölgeyi, '
                                  'gözleri, ağız içini ve fontaneli sistematik olarak muayene etmek',
                          'is_correct': True,
                          'explanation': 'Avutulamayan ağlamada nedenlerin önemli bir kısmı yalnızca bebek tamamen '
                                         'soyulduğunda görülebilen bulgulardır. Parmaklar, genital bölge, kornea, ağız '
                                         'içi ve fontanel atlanmadan değerlendirilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.9°C, KTA 168/dk (ağlarken), SS 42/dk, SpO2 %99, KDZ '
                                         '2 sn. Fontanel normal, karın yumuşak, fıtık yok, genital muayene olağan. Sağ '
                                         'ayak 3. parmak tabanında derin, çevresel bir oluk; oluk distalinde belirgin '
                                         'ödem ve kızarıklık var. Olukta ince, koyu renkli bir lif seçiliyor. Parmak '
                                         'ucu pembe, kapiller dolum 3 sn.'},
                         {'text': 'Ateş olmasa da genç süt çocuğunda ciddi enfeksiyon dışlanmalı diyerek tam kan '
                                  'sayımı, CRP, kan kültürü, idrar sondası ve lomber ponksiyon planlamak',
                          'is_correct': False,
                          'scenario_update': 'Girişimler sırasında bebek daha da huzursuzlandı; tüm sonuçlar normal '
                                             'geldi, ağlamanın nedeni saatlerce bulunamadı.',
                          'teaching_point': 'Ateşsiz ve iyi görünen bebekte invaziv sepsis taraması tam bir fizik '
                                            'muayenenin yerini tutmaz; önce bebek soyularak dikkatle muayene '
                                            'edilmelidir.'},
                         {'text': 'Bağırsak kaynaklı aralıklı bir tıkanıklığı dışlamak için muayeneyi kısa tutup '
                                  'hızlıca batın ultrasonografisi istemek ve sonucuna göre karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografi normal raporlandı; bekleme sırasında ayaktaki ödem arttı '
                                             've patik çıkarılınca morarma fark edildi.',
                          'teaching_point': 'Görüntüleme, tam muayene yapılmadan istenirse çorap içinde kalan ve '
                                            'süreye duyarlı bulgular gecikir.'}]},
            {'stage_title': 'Dolaşım Değerlendirmesi ve Aciliyet Kararı',
             'question': 'Parmak tabanındaki oluk ve distal ödem saptandı. Bir sonraki adımınız ne olmalıdır?',
             'options': [{'text': 'Parmakta kırık veya kemik yaralanması ihtimalini dışlamak için önce ayak grafisi '
                                  'çektirmek, ardından ortopedi değerlendirmesi sonrasında girişim planlamak',
                          'is_correct': False,
                          'scenario_update': 'Grafi normal geldi; bekleme sürecinde parmak ucunda soluklaşma başladı.',
                          'teaching_point': 'Çevresel sıkıştırma bulgusunda süreyle artan iskemi riski vardır; grafi '
                                            'tanıya katkı sağlamaz ve girişimi geciktirir.'},
                         {'text': 'Ödemi azaltmak için ayağı yükseltip soğuk uygulama yapmak ve bir saat sonra oluğun '
                                  'daha net görülmesini bekleyerek yeniden değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Bir saatlik beklemede ödem gerilemedi, aksine lif daha derine gömüldü ve '
                                             'görünmez hale geldi.',
                          'teaching_point': 'Sıkıştıran lif yerindeyken ödem kendiliğinden azalmaz; beklemek lifin '
                                            'dokuya gömülmesini ve iskemiyi artırır.'},
                         {'text': 'Arteriyel akımı belgelemek için girişimden önce acil renkli Doppler ultrasonografi '
                                  'istemek ve radyoloji raporu gelince müdahaleye karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Doppler için yaklaşık iki saat beklenildi; bu sürede bebek ağlamaya '
                                             'devam etti ve ödem arttı.',
                          'teaching_point': 'Tanı klinik muayeneyle konur; görüntüleme beklenmeden sıkıştıran cismin '
                                            'hemen çıkarılması gerekir.'},
                         {'text': 'Distal renk, ısı ve kapiller dolumu kaydedip iyi ışık ve büyüteçle oluğu '
                                  'inceleyerek sıkıştıran cismi beklemeden çıkarmaya hazırlanmak',
                          'is_correct': True,
                          'explanation': 'Çevresel sıkıştırmada iskemi süreye bağlıdır. Başlangıç perfüzyonu '
                                         'belgelenir ve görüntüleme beklenmeden aydınlatma ve büyütme altında girişime '
                                         'geçilir.',
                          'new_finding': 'Büyüteç altında oluk tabanında iki tur sarılmış, yaklaşık 0.1 mm '
                                         'kalınlığında koyu kahverengi ince bir lif görüldü. Parmak ucu ılık ve pembe, '
                                         'kapiller dolum 3 sn, dokuda nekroz bulgusu yok.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Öykü ve muayene bulgularına göre en olası tanınız nedir?',
             'options': [{'text': 'Ayak parmağında akut paronişi',
                          'is_correct': False,
                          'scenario_update': 'Tırnak kıvrımında püy veya fluktuasyon yoktu; oluk tırnak çevresinde '
                                             'değil parmak tabanındaydı.',
                          'teaching_point': 'Paronişi tırnak kıvrımında lokalize şişlik ve püy ile seyreder, çevresel '
                                            'oluk yapmaz.'},
                         {'text': 'Böcek ısırığına bağlı lokal reaksiyon',
                          'is_correct': False,
                          'scenario_update': 'Isırık noktası yoktu ve şişliği çevreleyen keskin sınırlı bir oluk '
                                             'saptandı.',
                          'teaching_point': 'Isırık reaksiyonunda merkezi punktum olur, çevresel daralma görülmez.'},
                         {'text': 'Ayak parmağında kıl turnike sendromu',
                          'is_correct': True,
                          'explanation': 'Parmak tabanında çevresel oluk, distal ödem ve olukta görülen ince lif saç '
                                         'teli turnikesini gösterir. Doğum sonrası anne saç dökülmesi ve çorap içi '
                                         'tipik kaynaktır.',
                          'new_finding': 'Tanı: Sağ ayak 3. parmakta saç teli turnikesi.'},
                         {'text': 'Ayak parmağında başlangıç selüliti',
                          'is_correct': False,
                          'scenario_update': 'Kızarıklık oluk distalinde sınırlıydı, ateş yoktu ve sıcaklık artışı '
                                             'yoktu.',
                          'teaching_point': 'Selülitte sınırları belirsiz yayılan eritem olur; keskin çevresel oluk '
                                            'mekanik sıkışmayı gösterir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Saç teli turnikesi olan bu bebekte doğru tedavi ve taburculuk yaklaşımı hangisidir?',
             'options': [{'text': 'Kızarıklık enfeksiyon başlangıcı olabileceği için önce oral sefaleksin başlamak, '
                                  'lifi çıkarmayı ödem azaldıktan sonraki kontrol muayenesine bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Lif yerinde kaldığı için ertesi gün parmakta koyu morarma ve epidermal '
                                             'soyulma gelişti.',
                          'teaching_point': 'Tedavinin temeli sıkıştıran lifin hemen ve tamamen çıkarılmasıdır; '
                                            'antibiyotik bunun yerini tutmaz.'},
                         {'text': 'Büyüteç altında künt prob ve ince pensle lifi tamamen çıkarmak, oluk tabanında '
                                  'kalıntı olmadığını doğrulayıp perfüzyonu 30-60 dakika izlemek',
                          'is_correct': True,
                          'explanation': 'Lif tamamen çıkarılmalı, ikinci bir tur kalmadığı büyütme altında '
                                         'doğrulanmalıdır. Lif görülemiyor veya çıkarılamıyorsa cerrahi kesi gerekir. '
                                         'Perfüzyon düzeldikten sonra taburculuk yapılır.',
                          'new_finding': 'Lif iki tur halinde tamamen çıkarıldı. 45 dakika sonra ödem gerilemiş, '
                                         'parmak ucu pembe, kapiller dolum 2 sn. Bebek sakinleşti ve emzirildi. Aileye '
                                         'çorap ve eldiven içini kontrol etmesi anlatıldı.'},
                         {'text': 'Lifin bir turu kesilip parmağın rengi düzelince işlemi yeterli kabul etmek ve '
                                  'aileye ertesi gün aile hekimine kontrole gitmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Ertesi gün ödem yeniden arttı; oluk tabanında gömülü kalmış ikinci bir '
                                             'tur saptandı.',
                          'teaching_point': 'Saç teli genellikle birden fazla tur sarılır; tek turun kesilmesi yetmez, '
                                            'büyütme altında tam çıkarım doğrulanmalıdır.'},
                         {'text': 'Lifi kesmeye çalışmadan bölgeye tüy dökücü krem sürüp üzerini kapatmak, 24 saat '
                                  'sonra lifin kendiliğinden çözülmesini evde beklemelerini istemek',
                          'is_correct': False,
                          'scenario_update': 'Krem gömülü life ulaşmadı, bölgede kimyasal tahriş gelişti ve sıkışma '
                                             'sürdü.',
                          'teaching_point': 'Tüy dökücü krem yalnızca seçilmiş, yüzeyel saç telinde acil serviste kısa '
                                            'süreli ve gözetim altında denenebilir; gömülü lifte etkisizdir ve evde '
                                            'beklemek uygun değildir.'}]}]},
 {'id': 'Y45',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '2 Aylık',
  'gender': 'Erkek',
  'complaint': 'Son birkaç gündür bezinde dışkıyla karışık ince kırmızı kan çizgileri ve mukus',
  'history': "Annesi anlatıyor: 'Sadece anne sütü alıyor. Son 4-5 gündür hardal sarısı dışkısının içinde ince iplik "
             'şeklinde kırmızı kan çizgileri ve sümük gibi mukus görüyorum. Ateşi, kusması veya karın şişliği yok. '
             "Emmesi iyi, keyfi yerinde, kilo alıyor.' Doğumda K vitamini yapılmış. Aile öyküsünde atopi var. Anne son "
             'zamanlarda günde 3-4 bardak süt içtiğini söylüyor.',
  'final_diagnosis': 'Besin Proteini İlişkili Alerjik Proktokolit (İnek Sütü Proteini Kaynaklı)',
  'disposition': 'Yeşil Alandan Emzirmeye Devam, Anne Diyetinden İnek Sütü Eliminasyonu ve Pediatri Kontrolü ile '
                 'Taburculuk',
  'case_pearl': 'Sağlıklı görünen, iyi kilo alan, yalnız anne sütü ile beslenen süt çocuğunda dışkıda kan çizgileri ve '
                'mukusun en sık nedeni anne diyetindeki inek sütü proteinine bağlı alerjik proktokolittir. Anal '
                'fissür, enfeksiyon ve cerrahi nedenler muayeneyle dışlanır; tanı kliniktir ve anne diyetinden 2-4 '
                'hafta süt eliminasyonu ile kanamanın kaybolmasıyla desteklenir. Emzirme kesilmez, anneye kalsiyum-D '
                'vitamini desteği verilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Dışkısında kan çizgileri ve mukus görülen, genel durumu iyi 2 aylık bu bebekte muayenede '
                         'neye odaklanmalısınız?',
             'options': [{'text': 'Dışkıdaki kanın gerçekten kan olup olmadığını anlamak için bezi inceleyip muayeneyi '
                                  'büyüme eğrisi değerlendirmesi ve hızlı batın palpasyonuyla sınırlı tutmak',
                          'is_correct': False,
                          'scenario_update': 'Bezde kan çizgileri doğrulandı ancak perianal bölge, cilt ve genel '
                                             'sistemik muayene yapılmadığı için kanamanın kaynağı değerlendirilmedi.',
                          'teaching_point': 'Rektal kanamada perianal inspeksiyon ve tam sistemik muayene fissür, '
                                            'enfeksiyon ve kanama diyatezini ayırt etmek için zorunludur.'},
                         {'text': 'Karın muayenesini yapıp sağ üst kadranda kitle aramak ve bebeği kucakta sallayarak '
                                  'ağlama nöbeti olup olmadığını izlemek için bir saat gözleme almak',
                          'is_correct': False,
                          'scenario_update': 'Kitle palpe edilmedi; bir saatlik gözlemde ağlama nöbeti olmadı. Cilt ve '
                                             'perianal muayene yapılmadığı için tablo netleşmedi.',
                          'teaching_point': 'Kanlı dışkıda cerrahi neden aranmalıdır ancak bu bebekte kolik ağlama, '
                                            'kusma ve letarji yok; muayene sistemik olarak tamamlanmalıdır.'},
                         {'text': 'Kanamanın üst gastrointestinal kaynaklı olabileceğini düşünerek nazogastrik sonda '
                                  'takıp mide içeriğini aspire etmek, ardından batını muayene etmek',
                          'is_correct': False,
                          'scenario_update': 'Nazogastrik aspiratta kan yoktu; bebek işlem sırasında öğürüp kustu ve '
                                             'aile ciddi biçimde endişelendi.',
                          'teaching_point': 'Dışkıyla karışık taze kan çizgileri alt gastrointestinal kaynağı '
                                            'gösterir; stabil bebekte nazogastrik aspirasyon gereksizdir.'},
                         {'text': 'Vitalleri, büyüme eğrisini, ciltte peteşi ve egzamayı, batında distansiyon ve '
                                  'kitleyi değerlendirip perianal bölgede fissür ve perianal dermatit aramak',
                          'is_correct': True,
                          'explanation': 'Kanlı dışkılı süt çocuğunda genel durum, büyüme, karın muayenesi '
                                         '(obstrüksiyon, invajinasyon), cilt (kanama diyatezi, atopik dermatit) ve '
                                         'perianal bölge (fissür) sistematik değerlendirilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 128/dk, SS 30/dk, SpO2 %100. Tartı 5.4 kg '
                                         '(50. persentil, düzenli artış). Genel durumu çok iyi, güleryüzlü. Yanaklarda '
                                         'hafif kuru egzamatöz alanlar. Peteşi veya ekimoz yok. Karın yumuşak, '
                                         'distansiyon ve kitle yok. Perianal inspeksiyonda fissür veya hemoroid yok. '
                                         'Bezde mukuslu sarı dışkı içinde kılcal kan çizgileri.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Genel durumu çok iyi, büyümesi normal, fissürü olmayan ve yanaklarında hafif egzaması '
                         'bulunan bu bebekte tetkik planınız nedir?',
             'options': [{'text': 'Kolonda polip veya vasküler malformasyonu dışlamak için batın ultrasonografisi '
                                  'isteyip çocuk gastroenterolojisine kolonoskopi değerlendirmesi için yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografi normal geldi; kolonoskopi için anestezi gerektiği '
                                             'belirtilince aile çok endişelendi.',
                          'teaching_point': 'İyi görünen süt çocuğunda hafif rektal kanama için endoskopi ilk basamak '
                                            'değildir; seçilmiş, eliminasyona yanıtsız olgularda düşünülür.'},
                         {'text': 'Ek tetkik istemeden klinik değerlendirmeyle yetinmek; yalnızca annenin diyet '
                                  'öyküsünü ayrıntılı almak ve kanamanın seyrini izlemeyi planlamak',
                          'is_correct': True,
                          'explanation': 'İyi görünen, normal büyüyen, fissürü ve sistemik bulgusu olmayan bebekte '
                                         'tanı kliniktir. Hemogram, dışkı tetkikleri ve görüntüleme yönetimi '
                                         'değiştirmez; annenin diyet öyküsü tanıya en çok katkı sağlayan bilgidir.',
                          'new_finding': 'Annenin son 3 haftadır kalsiyum alması için günde 3-4 bardak süt, yoğurt ve '
                                         'peynir tükettiği öğrenildi. Bebekte anemi bulgusu yok. Tetkik istenmedi.'},
                         {'text': 'Kanama nedeniyle tam kan sayımı, protrombin zamanı ve aPTT ile birlikte inek sütü '
                                  'spesifik IgE ve deri prick testini planlamak',
                          'is_correct': False,
                          'scenario_update': 'Hemogram ve koagülasyon normal geldi. Spesifik IgE ve deri testi negatif '
                                             'bulundu; aile alerji olmadığı sonucuna vararak diyet önerisine uymadı.',
                          'teaching_point': 'Bu tablo IgE aracılı değildir; spesifik IgE ve deri testleri negatiftir '
                                            've tanıyı dışlamaz, yanlış güvence verir.'},
                         {'text': 'Enfeksiyöz kolit olasılığını dışlamak için dışkı kültürü, parazit incelemesi ve '
                                  'Clostridioides toksin testi göndermek ve sonuca göre tedaviyi düzenlemek',
                          'is_correct': False,
                          'scenario_update': 'Dışkı kültürü negatif geldi; toksin testi pozitif bulundu ve aile '
                                             'yanlışlıkla enfeksiyon olduğu düşüncesiyle kaygılandı.',
                          'teaching_point': 'Bir yaş altı bebeklerde Clostridioides kolonizasyonu sıktır ve test '
                                            'sonucu yanıltıcıdır; ateşsiz, iyi görünen bebekte rutin dışkı tetkiki '
                                            'önerilmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Yalnız anne sütü alan, iyi büyüyen, mukuslu dışkıda kan çizgileri olan ve annesi bol süt '
                         'ürünü tüketen bu bebekte en olası tanı nedir?',
             'options': [{'text': 'İleokolik invajinasyon',
                          'is_correct': False,
                          'scenario_update': 'Kolik ağlama nöbetleri, kusma, letarji veya palpabl kitle yok; bebek '
                                             'neşeli.',
                          'teaching_point': 'Cerrahi nedenli kanamada genel durum bozulur ve obstrüksiyon bulguları '
                                            'eşlik eder.'},
                         {'text': 'Yenidoğanın hemorajik hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Doğumda K vitamini yapılmış, peteşi-ekimoz veya başka odaktan kanama '
                                             'yok.',
                          'teaching_point': 'K vitamini eksikliği kanaması genellikle çoklu odaktan ve profilaksi '
                                            'almamış bebeklerde görülür.'},
                         {'text': 'İnek sütü proteini ilişkili alerjik proktokolit',
                          'is_correct': True,
                          'explanation': 'Sağlıklı görünen, yalnız anne sütü alan süt çocuğunda mukuslu dışkıda kan '
                                         'çizgileri ve annenin süt ürünü tüketimi, anne sütüne geçen inek sütü '
                                         'proteinine bağlı alerjik proktokoliti düşündürür.',
                          'new_finding': 'Tanı: Besin Proteini İlişkili Alerjik Proktokolit (İnek Sütü Proteini).'},
                         {'text': 'Anal fissür',
                          'is_correct': False,
                          'scenario_update': 'Perianal inspeksiyonda fissür saptanmadı; dışkı sert değil, mukuslu ve '
                                             'yumuşak.',
                          'teaching_point': 'Fissür kanaması genellikle sert dışkı yüzeyinde ve ağrılı dışkılamayla '
                                            'birliktedir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu bebeğin tedavi ve izlem planı nasıl olmalıdır?',
             'options': [{'text': 'Emzirmeye devam, anne diyetinden tüm inek sütü ürünlerini 2-4 hafta çıkarmak, '
                                  'anneye kalsiyum-D vitamini desteği ve kanama seyri için kontrol planlamak',
                          'is_correct': True,
                          'explanation': 'Annenin diyetinden süt proteini çıkarıldığında kanama çoğunlukla 72 saat-2 '
                                         'hafta içinde azalır. Emzirme sürdürülür, anneye günlük kalsiyum ve D '
                                         'vitamini desteği verilir. Tablo genellikle 1 yaşında tolerans gelişmesiyle '
                                         'düzelir; yeniden maruziyet testi pediatri kontrolünde planlanır.',
                          'new_finding': 'Anneye süt içeren gizli ürünler listesi verildi, kalsiyum-D vitamini reçete '
                                         'edildi. İkinci haftadaki kontrolde bebeğin dışkısında kan görülmediği, kilo '
                                         'alımının sürdüğü belirlendi.'},
                         {'text': 'Emzirmeye devam etmek ancak annenin diyetinden süt, yumurta, buğday, soya, fındık '
                                  've balığı birlikte çıkarıp altı hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Anne kısıtlı diyete uyum sağlayamadı ve kilo kaybetti; emzirmeyi '
                                             'bırakmayı düşünmeye başladı.',
                          'teaching_point': 'Çoklu besin eliminasyonu ilk basamak değildir; çoğu olgu yalnız süt '
                                            'eliminasyonuna yanıt verir. Yanıt yoksa kademeli olarak soya veya yumurta '
                                            'değerlendirilir.'},
                         {'text': 'Anne sütünü kesip aminoasit bazlı formüle geçmek ve formül sonrası kanama '
                                  'düzeldiğinde altı ay boyunca aynı mamayla devam etmek',
                          'is_correct': False,
                          'scenario_update': 'Emzirme sonlandırıldı; aile pahalı formülü temin etmekte zorlandı. '
                                             'Kanama bir haftada geriledi ancak anne sütünün yararları kaybedildi.',
                          'teaching_point': 'Anne sütüyle beslenen bebekte ilk basamak emzirmeyi sürdürmek ve anne '
                                            'diyetinden süt eliminasyonu yapmaktır.'},
                         {'text': 'Diyette değişiklik yapmadan mukozal iyileşmeyi hızlandırmak için oral demir ve '
                                  'probiyotik başlamak, kanama sürerse bir ay sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Bir ay boyunca kanama devam etti; kontrolde hafif anemi gelişmeye '
                                             'başladığı görüldü.',
                          'teaching_point': 'Alerjik proktokolitte nedensel tedavi alerjen eliminasyonudur; '
                                            'probiyotikler tek başına yeterli değildir.'}]}]},
 {'id': 'Y46',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '4 Yaşında',
  'gender': 'Kız',
  'complaint': 'İki haftadır geçmeyen kötü kokulu cıvık ishal, karında şişkinlik ve gaz sancısı',
  'history': "Annesi anlatıyor: 'Yaklaşık iki hafta önce köydeki yazlıktan döndük, orada kuyu suyu içiyordu. Dönüşten "
             'birkaç gün sonra günde 3-4 kez açık renkli, çok kötü kokulu, köpüklü, yağlı gibi parlayan cıvık kaka '
             'yapmaya başladı. Kan görmedim. Karnı sürekli guruldıyor, çok geğiriyor, iştahı azaldı. Ateşi olmadı. '
             "Pantolonları bollaştı.' Kreşe gidiyor. Tartı: 15.5 kg (iki hafta önce 16 kg).",
  'final_diagnosis': 'Giardiyaz (Giardia duodenalis Enfeksiyonu)',
  'disposition': 'Yeşil Alandan Oral Metronidazol, Hijyen ve Su Güvenliği Eğitimi ile Ayaktan Taburculuk',
  'case_pearl': 'İki haftayı aşan, yağlı-köpüklü, kötü kokulu ishal, şişkinlik, geğirme ve kilo kaybı Giardia '
                'enfeksiyonunu düşündürür; kuyu suyu, kreş ve kamp öyküsü önemli ipuçlarıdır. Tanıda dışkı antijen '
                'testi veya PCR tek mikroskopiden daha duyarlıdır; mikroskopi seçilirse kistler aralıklı atıldığı için '
                'farklı günlerde 3 örnek incelenmelidir. Tedavide metronidazol 15 mg/kg/gün (3 dozda, 5-7 gün), tek '
                'doz tinidazol 50 mg/kg veya 3 gün nitazoksanid kullanılır; asemptomatik taşıyıcıların rutin tedavisi '
                'önerilmez.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'İki haftadır yağlı görünümlü ishali ve kilo kaybı olan bu 4 yaşındaki kız çocuğunda ilk '
                         'değerlendirmede neye odaklanırsınız?',
             'options': [{'text': 'İshalin sürmesini laktoz intoleransı kabul ederek beslenme öyküsünü sorgulamak, süt '
                                  'ürünlerini kesip bir hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Süt ürünleri kesildi; bir hafta sonra ishal ve kilo kaybı devam '
                                             'ediyordu, etken araştırılmamıştı.',
                          'teaching_point': 'Sekonder laktoz intoleransı birçok enterik enfeksiyona eşlik edebilir; '
                                            'ancak altta yatan etken araştırılmadan diyet değişikliği tek başına '
                                            'yeterli değildir.'},
                         {'text': 'Uzamış ishali olan çocukta önce damar yolu açarak elektrolit, albümin ve tam kan '
                                  'sayımı almak, muayeneyi sonuçlar geldikten sonra tamamlamak',
                          'is_correct': False,
                          'scenario_update': 'Elektrolitler ve albümin normal geldi; hidrasyonu iyi olan çocuğa '
                                             'gereksiz girişim yapıldı ve öykü eksik kaldı.',
                          'teaching_point': 'Hidrasyonu iyi, genel durumu iyi çocukta ilk adım öykü ve muayenedir; kan '
                                            'tetkikleri seçici istenir.'},
                         {'text': 'Uzamış ishal nedeniyle hidrasyon durumunu, büyüme eğrisini, karın distansiyonunu ve '
                                  'ödem-solukluk gibi malabsorpsiyon bulgularını değerlendirip ayrıntılı maruziyet '
                                  'öyküsü almak',
                          'is_correct': True,
                          'explanation': 'İki haftayı aşan ishalde akut dehidratasyonun yanı sıra büyüme etkilenmesi '
                                         've malabsorpsiyon bulguları değerlendirilmelidir. Su kaynağı, seyahat, kreş '
                                         've hayvan teması gibi maruziyetler etiyolojiye yön verir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 98/dk, SS 20/dk, TA 94/60 mmHg, KDZ 1.5 sn. '
                                         'Tartı 15.5 kg (iki haftada 500 g kayıp), boy persentili korunmuş. Hidrasyonu '
                                         'iyi. Karın hafif distandü, timpanik, periumbilikal hafif hassasiyet; defans '
                                         'yok. Bağırsak sesleri hiperaktif. Ödem, solukluk, ağız kenarında çatlak yok. '
                                         'Perianal bölge doğal.'},
                         {'text': 'Karın distansiyonu nedeniyle cerrahi bir sorunu ekarte etmek için sağ alt kadranı '
                                  've rebound bulgusunu değerlendirip ayakta direkt batın grafisi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Peritoneal bulgu saptanmadı. Grafide yaygın gaz distansiyonu görüldü ve '
                                             'non-spesifik olarak raporlandı; maruziyet öyküsü alınmadı.',
                          'teaching_point': 'Ateşsiz, iki haftalık yağlı ishal ve gaz şişkinliği cerrahi tablo '
                                            'düşündürmez; öykü ve malabsorpsiyon bulgularına odaklanılmalıdır.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Kuyu suyu maruziyeti olan, iki haftadır yağlı-köpüklü ishali süren bu çocukta en uygun '
                         'tanısal yaklaşım hangisidir?',
             'options': [{'text': 'Dışkıda protozoon antijen testi istemek veya farklı günlerde alınan üç örnekte '
                                  'mikroskopik inceleme yapmak; kan tetkikini klinik gerektirmedikçe istememek',
                          'is_correct': True,
                          'explanation': 'Uzamış yağlı ishal ve su maruziyetinde protozoon araştırması önceliklidir. '
                                         'Dışkı antijen testi veya PCR tek mikroskopiden duyarlıdır; mikroskopide '
                                         'kistler aralıklı atıldığından üç ayrı örnek incelenmelidir.',
                          'new_finding': 'Dışkı protozoon antijen testi pozitif. Mikroskopide armut biçimli, iki '
                                         'çekirdekli, hareketli kamçılı trofozoitler ve oval dört çekirdekli kistler '
                                         'görüldü; lökosit ve eritrosit yok. Gizli kan negatif.'},
                         {'text': 'Karın şişliği ve kilo kaybını değerlendirmek için batın ultrasonografisi ve tam kan '
                                  'sayımı isteyip dışkı incelemesini ultrason sonucuna göre planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografide sıvı dolu ince bağırsak ansları dışında bulgu yoktu; '
                                             'tam kan sayımı normaldi ve tablo aydınlatılamadı.',
                          'teaching_point': 'Uzamış ishalde görüntüleme etkeni göstermez; dışkı incelemesi ilk basamak '
                                            'tetkiktir.'},
                         {'text': 'Dışkı kültürü göndermek ve sonuç gelene kadar ampirik oral siprofloksasin '
                                  'başlayarak bakteriyel etkenleri kapsamak, bir hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Dışkı kültüründe patojen üremedi. Antibiyotik sonrası ishal azalmadı; '
                                             'çocuk bir hafta sonra aynı şikayetlerle geldi.',
                          'teaching_point': 'Ateşsiz, kansız, yağlı uzamış ishalde bakteriyel etken olasılığı '
                                            'düşüktür; ampirik antibiyotik tanıyı geciktirir.'},
                         {'text': 'Malabsorpsiyon nedeniyle doku transglutaminaz IgA, total IgA, ter testi ve dışkı '
                                  'elastaz düzeyini birlikte isteyip sonuçlara göre gastroenterolojiye yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Serolojik testler ve elastaz normal geldi; ter testi için randevu '
                                             'verildi. Sonuçlar beklenirken ishal sürdü ve etken araştırılmadı.',
                          'teaching_point': 'Akut maruziyet sonrası başlayan iki haftalık ishalde kronik '
                                            'malabsorpsiyon taramasından önce enfeksiyöz etkenler araştırılmalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Kuyu suyu maruziyeti, yağlı-köpüklü uzamış ishal, şişkinlik ve dışkıda armut biçimli iki '
                         'çekirdekli trofozoitler görülen bu çocukta tanı nedir?',
             'options': [{'text': 'Kriptosporidium enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Kriptosporidiyumda bol sulu ishal baskındır ve tanı modifiye asit-fast '
                                             'boyama veya PCR ile konur; kamçılı trofozoit görülmez.',
                          'teaching_point': 'Mikroskopik morfoloji protozoonların ayırıcı tanısında belirleyicidir.'},
                         {'text': 'Çölyak hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Akut maruziyet sonrası başlangıç ve dışkıda protozoonların görülmesi '
                                             'şikayetleri açıklıyor.',
                          'teaching_point': 'Çölyak hastalığı uzun süreli malabsorpsiyon ve büyüme geriliğiyle '
                                            'seyreder; enfeksiyon dışlanmadan düşünülmez.'},
                         {'text': 'Giardia duodenalis enfeksiyonu',
                          'is_correct': True,
                          'explanation': 'Kontamine su maruziyeti, yağlı-köpüklü kötü kokulu ishal, şişkinlik, '
                                         'geğirme, kilo kaybı ve dışkıda iki çekirdekli kamçılı trofozoitler Giardia '
                                         'duodenalis enfeksiyonunu doğrular.',
                          'new_finding': 'Tanı: Giardiyaz (Giardia duodenalis).'},
                         {'text': 'Amipli dizanteri',
                          'is_correct': False,
                          'scenario_update': 'Amip enfeksiyonunda kanlı-mukuslu dışkı ve tenezm beklenir; bu çocukta '
                                             'dışkıda kan ve lökosit yok.',
                          'teaching_point': 'Entamoeba trofozoitleri tek çekirdekli ve eritrosit fagosite eder; '
                                            'kamçılı değildir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': "Bu 15.5 kg'lık çocuğun tedavi ve izlem planı nasıl olmalıdır?",
             'options': [{'text': 'Oral metronidazol 30-50 mg/kg/gün dozunu üç eşit dozda on gün vermek ve tedavi '
                                  'sonrası iyileşmeyi göstermek için dışkı antijen testini tekrarlamak',
                          'is_correct': False,
                          'scenario_update': 'Yüksek doz ve uzun süreli tedaviyle çocukta bulantı, metalik tat ve '
                                             'iştahsızlık gelişti; tekrar testi semptomsuz çocukta gereksiz bulundu.',
                          'teaching_point': 'Bu doz aralığı amip enfeksiyonu için kullanılır; giardiyazda 15 mg/kg/gün '
                                            'yeterlidir. Semptomları düzelen çocukta kontrol testi gerekmez.'},
                         {'text': 'Oral metronidazol 15 mg/kg/gün dozunu üç eşit dozda 5-7 gün vermek, el hijyeni ve '
                                  'kaynatılmış su kullanımını anlatmak, semptomlu aile bireylerini değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Semptomatik giardiyazda metronidazol 15 mg/kg/gün (3 dozda, 5-7 gün) etkin '
                                         'bir seçenektir; alternatif olarak tek doz tinidazol 50 mg/kg veya 3 gün '
                                         'nitazoksanid kullanılabilir. Bulaşın önlenmesi için hijyen ve su güvenliği '
                                         'eğitimi verilir.',
                          'new_finding': 'Metronidazol başlandı, aileye su kaynatma ve el yıkama önerileri verildi. '
                                         'Bir hafta sonraki kontrolde dışkı kıvamı normale döndü, şişkinlik geçti ve '
                                         'çocuk 300 g aldı.'},
                         {'text': 'Tek doz oral mebendazol vermek ve iki hafta sonra dozu tekrarlamak, tüm aile '
                                  'bireylerine de aynı tedaviyi eş zamanlı uygulamak',
                          'is_correct': False,
                          'scenario_update': 'İki doz mebendazole rağmen ishal ve şişkinlik sürdü; çocuk üç hafta '
                                             'sonra kilo kaybıyla başvurdu.',
                          'teaching_point': 'Mebendazol helmintlere etkilidir; protozoon enfeksiyonlarında ilk seçenek '
                                            'değildir.'},
                         {'text': 'Tablo kendiliğinden düzeleceği için antiparaziter vermeden yalnızca laktozsuz '
                                  'diyet, probiyotik ve hijyen önerileriyle iki hafta izlemek',
                          'is_correct': False,
                          'scenario_update': "İki hafta sonra ishal devam ediyordu, kilo kaybı 1 kg'a ulaştı ve "
                                             'kardeşinde de benzer şikayet başladı.',
                          'teaching_point': 'Semptomatik ve kilo kaybı olan çocukta tedavi önerilir; tedavisiz izlem '
                                            'yalnızca asemptomatik taşıyıcılar için uygundur.'}]}]},
 {'id': 'Y47',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '3 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Yarım saat önce ağzındaki madeni bir cismi yuttuğu düşünülüyor',
  'history': "Babası anlatıyor: 'Ablasının kumbarasıyla oynuyordu, ağzına bir şey attığını gördüm, öksürdü ve sonra "
             "yuttu. Ne olduğunu tam göremedim, para olabilir. Evde kumandalar ve oyuncaklar da var.' Şu anda "
             'ağlamıyor, su içti. Kusma, salya akması, yutma güçlüğü, öksürük veya hırıltı yok. Daha önce yutma '
             'sorunu, özofagus ameliyatı veya kronik hastalık yok.',
  'final_diagnosis': 'Asemptomatik Midede Madeni Para (Gastrik Yabancı Cisim)',
  'disposition': 'Normal Beslenme ve Dışkı Takibi Önerileriyle Yeşil Alandan Taburculuk',
  'case_pearl': 'Yutulan madeni bir cisimde ilk soru pil olup olmadığıdır. Boyundan anüse ön-arka ve gerekirse yan '
                'grafi çekilir: düğme pil kenarda çift halka (halo) ve yan grafide basamak görüntüsü verir, madeni '
                'para tek ve düzgün konturludur. Özofagustaki para semptomluysa acil, asemptomatikse 12-24 saat içinde '
                'çıkarılır. Mideye geçmiş asemptomatik para evden izlenir. 2-4 hafta içinde dışkıyla çıktığı '
                'görülmezse grafi tekrarlanır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Ne olduğu tam bilinmeyen metal bir cisim yutan, şu an yakınması olmayan bu çocukta ilk '
                         'yaklaşımınız nedir?',
             'options': [{'text': 'Havayolu, solunum sesleri, salya, yutma ve göğüs ağrısını değerlendirip cismin pil '
                                  'olup olmadığını sorgulamak ve görüntülemeyle yerini belirlemeyi planlamak',
                          'is_correct': True,
                          'explanation': 'Önce havayolu ve solunum güvenliği değerlendirilir. Cismin niteliği, '
                                         'özellikle düğme pil olasılığı yönetimi tamamen değiştirdiği için öyküde ve '
                                         'görüntülemede netleştirilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 108/dk, SS 24/dk, SpO2 %99. Huzursuzluk '
                                         'yok, salya akması yok, sıvı yutuyor. Solunum sesleri eşit, stridor veya '
                                         'hışıltı yok. Karın yumuşak, hassasiyet yok. Baba evdeki pil kapaklarının '
                                         'kapalı olduğunu ve kumbaranın yanında bir eksik para bulunduğunu doğruladı.'},
                         {'text': 'Cismi geri çıkarması için tuzlu su içirerek ya da parmakla öğürterek kusturmaya '
                                  'çalışmak, cisim gelmezse görüntüleme planlamak',
                          'is_correct': False,
                          'scenario_update': 'Kusturma girişimi sırasında çocuk öksürdü ve ağladı; cisim çıkmadı, '
                                             'aspirasyon riski yaratıldı.',
                          'teaching_point': 'Yabancı cisim yutmada kusturma kontrendikedir; özofagusta takılma, '
                                            'mukozal yaralanma ve aspirasyon riskini artırır.'},
                         {'text': 'Çocuk sıvı yutabildiğine ve hiçbir yakınması olmadığına göre görüntülemeye gerek '
                                  'görmeden dışkı takibi önererek ailesiyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Cismin niteliği ve yeri belirlenmeden taburcu edildi; aile ertesi gün '
                                             'evde bir pilin eksik olduğunu fark edip geri döndü.',
                          'teaching_point': 'Asemptomatik olmak özofagusta takılı cismi veya pili dışlamaz; niteliği '
                                            'bilinmeyen metal cisimde görüntüleme yapılmalıdır.'},
                         {'text': 'Cismin aşağı inmesini kolaylaştırmak için bir dilim ekmek veya muz yedirip ardından '
                                  'bol su içirmek, sonra görüntüleme yapmak',
                          'is_correct': False,
                          'scenario_update': 'Katı besin verildikten sonra çocuk iki kez öğürdü; olası bir endoskopi '
                                             'için açlık süresi de uzadı.',
                          'teaching_point': 'Yeri belirlenmeden katı besin vermek özofagusta takılmayı '
                                            'ağırlaştırabilir ve gerekebilecek endoskopiyi geciktirir.'}]},
            {'stage_title': 'Görüntüleme Kararı',
             'question': 'Cismin niteliği ve yerini belirlemek için en uygun görüntüleme hangisidir?',
             'options': [{'text': 'Radyasyondan kaçınmak için yalnızca batın ultrasonografisi istemek ve cisim '
                                  'görülmezse mideye geçmiş kabul ederek izlem planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografide gaz nedeniyle cisim görülemedi; özofagus ise hiç '
                                             'değerlendirilemedi.',
                          'teaching_point': 'Metal yabancı cisimde ultrasonografi özofagusu göstermez; ilk basamak '
                                            'boyundan anüse direkt grafidir.'},
                         {'text': 'Yalnızca ayakta direkt batın grafisi çekmek, cisim batında görülmezse dışkıyla '
                                  'çıkacağını varsayarak aileyi bilgilendirmek',
                          'is_correct': False,
                          'scenario_update': 'Batın grafisinde cisim görülmedi; boyun ve göğüs alana dahil edilmediği '
                                             'için özofagustaki olası takılma değerlendirilmemiş oldu.',
                          'teaching_point': 'Görüntü alanı boyundan anüse uzanmalıdır; özofagus en kritik takılma '
                                            'yeridir.'},
                         {'text': 'Boyundan anüse kadar ön-arka direkt grafi çekmek, cismin kenar konturunu '
                                  'değerlendirmek ve gerekirse yan grafiyle tamamlamak',
                          'is_correct': True,
                          'explanation': 'Tek ön-arka grafi cismin yerini ve konturunu gösterir. Kenarda çift halka '
                                         'veya yan grafide basamak görüntüsü pili düşündürür; düzgün tek kontur madeni '
                                         'parayı destekler.',
                          'new_finding': 'Boyun-göğüs-batın ön-arka grafi: Sol üst kadranda, diyafram altında, '
                                         'yaklaşık 23 mm çaplı, tek ve düzgün konturlu, yuvarlak radyoopak cisim. '
                                         'Kenarda çift halka görünümü yok. Boyun ve göğüs bölgesinde yabancı cisim '
                                         'yok. Serbest hava yok.'},
                         {'text': 'Cismin yerini ve olası mukozal hasarı aynı anda görmek için kontrastsız toraks ve '
                                  'batın bilgisayarlı tomografisi istemek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi için çocuk sedasyon ihtiyacıyla birlikte bekletildi; aynı '
                                             'bilgi tek bir direkt grafiyle elde edilebilirdi.',
                          'teaching_point': 'Komplikasyon şüphesi olmayan çocukta tomografi gereksiz radyasyon ve '
                                            'sedasyon getirir; ilk tetkik direkt grafidir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Öykü ve görüntüleme bulgularına göre tanınız nedir?',
             'options': [{'text': 'Midede düğme pil',
                          'is_correct': False,
                          'scenario_update': 'Kenarda çift halka görünümü yoktu ve baba pillerin yerinde olduğunu '
                                             'doğrulamıştı.',
                          'teaching_point': 'Düğme pil kenarda halo ve yan grafide basamak görüntüsü verir.'},
                         {'text': 'Özofagusta takılı madeni para',
                          'is_correct': False,
                          'scenario_update': 'Cisim diyafram altında, sol üst kadrandaydı; boyun ve göğüs temizdi.',
                          'teaching_point': 'Özofagustaki para çoğunlukla üst darlık düzeyinde, ön-arka grafide tam '
                                            'yüz olarak görülür.'},
                         {'text': 'Midede asemptomatik madeni para',
                          'is_correct': True,
                          'explanation': 'Diyafram altında, sol üst kadranda tek ve düzgün konturlu yuvarlak cisim, '
                                         'yakınması olmayan çocukta mideye geçmiş madeni parayı gösterir.',
                          'new_finding': 'Tanı: Asemptomatik gastrik madeni para.'},
                         {'text': 'Trakeobronşiyal yabancı cisim aspirasyonu',
                          'is_correct': False,
                          'scenario_update': 'Solunum sesleri eşitti, hışıltı yoktu ve göğüs grafisinde yabancı cisim '
                                             'görülmedi.',
                          'teaching_point': 'Aspirasyonda öksürük krizi sonrası tek taraflı hışıltı ve hava hapsi '
                                            'beklenir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Mideye geçmiş, yakınması olmayan madeni para için en uygun izlem planı hangisidir?',
             'options': [{'text': 'Normal beslenmeyle taburcu edip dışkı takibini önermek; karın ağrısı, kusma veya '
                                  'kanama olursa dönmeleri, 2-4 haftada çıkmazsa grafi tekrarlamak',
                          'is_correct': True,
                          'explanation': 'Mideye geçmiş asemptomatik madeni para çoğunlukla kendiliğinden atılır. '
                                         'Rutin endoskopi veya laksatif gerekmez; uyarı bulguları ve tekrar grafi '
                                         'zamanı aileye anlatılır.',
                          'new_finding': 'Aile bilgilendirildi ve normal beslenmeyle taburcu edildi. Dördüncü gün '
                                         'dışkıda madeni paranın çıktığını telefonla bildirdiler.'},
                         {'text': 'Cisim midede beklerken mukozal hasar yapabileceği için aynı gün gastroenteroloji '
                                  'ile elektif üst gastrointestinal endoskopi ayarlamak',
                          'is_correct': False,
                          'scenario_update': 'Endoskopi için çocuk aç bırakıldı ve genel anestezi aldı; işlem '
                                             'sırasında para zaten duodenuma geçmişti.',
                          'teaching_point': 'Mideye geçmiş asemptomatik madeni parada rutin endoskopi gerekmez; '
                                            'endoskopi pil, mıknatıs, sivri cisim veya semptom varlığında düşünülür.'},
                         {'text': 'Bağırsak geçişini hızlandırmak için birkaç gün laktüloz ya da polietilen glikol '
                                  'başlamak ve günlük dışkıyı elekle kontrol etmelerini istemek',
                          'is_correct': False,
                          'scenario_update': 'Laksatif ishale neden oldu ve dışkı takibi zorlaştı; paranın geçişi '
                                             'hızlanmadı.',
                          'teaching_point': 'Laksatiflerin madeni para geçişini hızlandırdığına dair kanıt yoktur; '
                                            'normal beslenme yeterlidir.'},
                         {'text': 'Paranın pilora geçişini görmek için çocuğu 24 saat hastanede gözleme alıp sabah '
                                  'kontrol grafisiyle değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk bir gece gereksiz yere yatırıldı; sabah grafisinde para hâlâ '
                                             'midedeydi ve yönetim değişmedi.',
                          'teaching_point': 'Asemptomatik gastrik madeni para için hastanede gözlem veya erken kontrol '
                                            'grafisi gerekmez; ayaktan izlenir.'}]}]},
 {'id': 'Y48',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '2.5 Yaşında',
  'gender': 'Erkek',
  'complaint': 'İki aydır günde 4-5 kez, içinde sindirilmemiş besin parçaları olan cıvık dışkılama',
  'history': "Annesi anlatıyor: 'Yaklaşık 2 aydır günde 4-5 kez kaka yapıyor. Sabah ilk kakası şekilli, öğleden sonra "
             've akşama doğru cıvıklaşıyor. İçinde bezelye, havuç, mısır parçaları aynen duruyor. Geceleri uykusunda '
             'hiç kaka yapmıyor. Kan veya mukus görmedim. Çok hareketli, iştahlı, neşeli. Kuzeninin çölyak olması bizi '
             "çok korkuttu.' Çocuk gün içinde biberonla içecek tüketiyor; ayrıntılı beslenme öyküsü henüz alınmadı.",
  'final_diagnosis': 'Kronik Non-spesifik Diyare (Toddler Diyaresi)',
  'disposition': 'Yeşil Alandan Beslenme Düzenlemesi (Meyve Suyu Kısıtlaması, Yeterli Yağ ve Lif) ve Güvence ile '
                 'Taburculuk',
  'case_pearl': '6 ay-5 yaş arasında, büyümesi normal, gündüz olan, gece kesilen, sindirilmemiş sebze parçaları içeren '
                'cıvık dışkılama toddler diyaresini düşündürür. Neden çoğunlukla aşırı meyve suyu (fruktoz-sorbitol) '
                've düşük yağlı diyettir. Tanı büyümenin normal olması ve alarm bulgularının yokluğuna dayanır; meyve '
                'suyu kısıtlanır, yağ alımı normalleştirilir, ilaç gerekmez. Büyüme geriliği varsa çölyak ve diğer '
                'malabsorpsiyon nedenleri araştırılır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'İki aydır gündüz cıvık dışkılaması olan, aktif görünen bu 2.5 yaşındaki çocukta '
                         'değerlendirmenin en kritik bileşeni nedir?',
             'options': [{'text': 'Kreş öyküsü nedeniyle paraziter enfeksiyonu öncelikli düşünüp perianal bölgeyi '
                                  'muayene etmek ve ampirik tek doz mebendazol vermek',
                          'is_correct': False,
                          'scenario_update': 'Perianal bölge doğaldı; mebendazol sonrası dışkılama paterni değişmedi.',
                          'teaching_point': 'Ampirik antiparaziter tedavi ishalin nedenini aydınlatmaz; önce büyüme ve '
                                            'beslenme öyküsü değerlendirilmelidir.'},
                         {'text': 'Büyüme eğrisini önceki ölçümlerle karşılaştırmak, ayrıntılı 24 saatlik beslenme ve '
                                  'sıvı öyküsü almak, malabsorpsiyon ve kronik hastalık bulgularını muayenede aramak',
                          'is_correct': True,
                          'explanation': 'Kronik ishalde büyüme hızının korunup korunmadığı organik ve fonksiyonel '
                                         'nedenleri ayıran en önemli bulgudur. Ayrıntılı beslenme öyküsü fonksiyonel '
                                         'ishalin nedenini sıklıkla ortaya koyar.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 96/dk, TA 92/56 mmHg. Tartı 13.5 kg (50. '
                                         'p), boy 92 cm (50. p); son 1 yılda persentil kaybı yok. Canlı, hareketli. '
                                         'Karın yumuşak, distansiyon yok, organomegali yok. Ödem, solukluk, dermatit, '
                                         'çomak parmak yok. Perianal bölge doğal. Beslenme öyküsü: günde 4-5 biberon '
                                         '(yaklaşık 1 litre) hazır elma suyu, yağsız süt, az yağlı yemekler.'},
                         {'text': 'Dışkıda besin parçaları görülmesini pankreas yetersizliği bulgusu kabul ederek '
                                  'solunum sistemi muayenesine ve ter testi planlamasına odaklanmak',
                          'is_correct': False,
                          'scenario_update': 'Akciğer muayenesi normaldi. Ter testi için randevu alındı; büyüme ve '
                                             'beslenme öyküsü değerlendirilmedi.',
                          'teaching_point': 'Sindirilmemiş sebze parçaları küçük çocukta hızlı geçişe bağlı olabilir; '
                                            'normal büyüyen çocukta pankreas yetersizliği düşük olasılıktır.'},
                         {'text': 'Kronik ishal nedeniyle hidrasyon bulgularını değerlendirip karın palpasyonu yapmak '
                                  've kuzenindeki tanıyı göz önüne alarak muayene sonrası çölyak serolojisini hemen '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'Hidrasyon normal bulundu; çölyak serolojisi gönderildi. Büyüme eğrisi ve '
                                             'beslenme öyküsü değerlendirilmediği için tablonun nedeni ortaya çıkmadı.',
                          'teaching_point': 'Kronik ishalde tetkik kararı büyüme eğrisi ve ayrıntılı beslenme '
                                            'öyküsüyle verilir; aile öyküsü tek başına serolojiyi zorunlu kılmaz.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Büyümesi normal, alarm bulgusu olmayan ve günde yaklaşık 1 litre meyve suyu içen bu çocukta '
                         'tetkik yaklaşımınız nedir?',
             'options': [{'text': 'Kuzende çölyak bulunduğu için doku transglutaminaz IgA ile birlikte tam kan sayımı, '
                                  'ferritin, albümin ve dışkı elastaz düzeyini istemek, sonuçlara göre diyet planlamak',
                          'is_correct': False,
                          'scenario_update': 'Tüm sonuçlar normal geldi; aile sonuç beklerken yoğun kaygı yaşadı ve '
                                             'diyet önerisi ertelendi.',
                          'teaching_point': 'İkinci derece akrabada çölyak tek başına tarama endikasyonu değildir; '
                                            'büyümesi normal, alarm bulgusu olmayan çocukta önce diyet düzenlemesi '
                                            'yapılır.'},
                         {'text': 'Dışkıda gizli kan, kalprotektin, parazit incelemesi ve dışkı kültürü isteyip '
                                  'sonuçlar normalse iki hafta sonra diyet değişikliği önermek',
                          'is_correct': False,
                          'scenario_update': 'Kalprotektin sınırda yüksek geldi ve tekrar ölçüm planlandı; bu süre '
                                             'içinde meyve suyu tüketimi devam etti.',
                          'teaching_point': 'Küçük çocuklarda kalprotektin normal değerleri daha yüksektir ve gereksiz '
                                            'tetkik zinciri başlatabilir; tetkik klinik şüpheye göre istenmelidir.'},
                         {'text': 'İshal kronikleştiği için çocuğu gastroenteroloji polikliniğine sevk etmek ve '
                                  'endoskopi değerlendirmesi yapılana kadar glutensiz diyet başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Glutensiz diyet sonrası dışkılama değişmedi; diyetle birlikte olası bir '
                                             'serolojik tanı da değerlendirilemez hale geldi.',
                          'teaching_point': 'Tanı konmadan glutensiz diyet başlanmamalıdır; bu hem gereksiz '
                                            'kısıtlamaya hem de olası tanının maskelenmesine yol açar.'},
                         {'text': 'Tetkik istemeden meyve suyu tüketimini kısıtlayıp yağ ve lif alımını düzenleyen bir '
                                  'deneme yapmak, iki hafta sonra dışkılama günlüğüyle kontrol etmek',
                          'is_correct': True,
                          'explanation': 'Büyümesi normal, gece dışkılaması, kan ve kilo kaybı olmayan çocukta aşırı '
                                         'meyve suyu ve düşük yağ alımı fonksiyonel ishali açıklar. Tetkik yerine '
                                         'diyet denemesi hem tanısal hem tedavidir.',
                          'new_finding': 'Laboratuvar tetkiki istenmedi. Aile ile birlikte iki haftalık beslenme planı '
                                         've dışkılama günlüğü hazırlandı.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Normal büyüyen, gündüz cıvık, gece dışkılaması olmayan, sebze parçaları içeren dışkılaması '
                         've yüksek meyve suyu tüketimi olan bu çocukta tanı nedir?',
             'options': [{'text': 'Çölyak hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Büyüme eğrisi korunmuş, distansiyon, anemi ve hipoalbüminemi bulgusu '
                                             'yok.',
                          'teaching_point': 'Malabsorpsiyon tablosunda büyüme hızında yavaşlama beklenir.'},
                         {'text': 'Postenfeksiyöz laktoz intoleransı',
                          'is_correct': False,
                          'scenario_update': 'Öncesinde akut gastroenterit öyküsü yok; dışkılama süt alımıyla değil '
                                             'meyve suyu ile ilişkili.',
                          'teaching_point': 'Sekonder laktoz intoleransı genellikle akut enfeksiyon sonrası gelişir ve '
                                            'şişkinlik, asidik dışkı eşlik eder.'},
                         {'text': 'İnflamatuvar bağırsak hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Kanlı dışkı, gece dışkılaması, kilo kaybı ve perianal hastalık yok.',
                          'teaching_point': 'İnflamatuvar hastalıkta alarm bulguları ve büyüme etkilenmesi beklenir.'},
                         {'text': 'Kronik non-spesifik (toddler) diyare',
                          'is_correct': True,
                          'explanation': '6 ay-5 yaş arası, büyümesi normal, gündüz cıvık, gece dışkılaması olmayan '
                                         'çocukta aşırı fruktoz-sorbitol içeren meyve suyu ve düşük yağ alımı toddler '
                                         'diyaresine neden olur.',
                          'new_finding': 'Tanı: Kronik Non-spesifik Diyare (Toddler Diyaresi).'}]},
            {'stage_title': 'Diyet Düzenlemesi ve Aile Rehberliği',
             'question': 'Bu çocuğun ailesine verilecek en uygun öneri hangisidir?',
             'options': [{'text': 'Dışkı sıklığını azaltmak için birkaç gün düşük doz loperamid vermek ve aynı süre '
                                  'içinde meyve suyu tüketimini yarıya indirmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Loperamid sonrası çocukta karın şişliği ve uykuya meyil gelişti; aile '
                                             'ilacı kesip acile başvurdu.',
                          'teaching_point': 'Küçük çocuklarda loperamid ileus ve santral sinir sistemi yan etkileri '
                                            'nedeniyle önerilmez.'},
                         {'text': 'Meyve suyunu sulandırarak sürdürmek, posalı gıdaları ve sebzeleri tamamen kesmek ve '
                                  'bağırsağı dinlendirmek için bir hafta pirinç lapası ağırlıklı beslemek',
                          'is_correct': False,
                          'scenario_update': 'Kısıtlı diyetle dışkılama azalmadı, çocuk iştahsızlaştı ve kilo almadı.',
                          'teaching_point': 'Lif kısıtlaması ve kısıtlayıcı diyetler önerilmez; asıl hedef '
                                            'fruktoz-sorbitol yükünü azaltmak ve yeterli yağ alımını sağlamaktır.'},
                         {'text': 'Meyve suyunu kesip su vermek, tam yağlı süt ve yemeklere yağ eklemek, lifi '
                                  'sürdürmek ve aileye güvence vermek',
                          'is_correct': True,
                          'explanation': 'Meyve suyunun kısıtlanması ozmotik yükü azaltır; yeterli yağ alımı gastrik '
                                         'boşalmayı ve bağırsak geçişini yavaşlatır. Lif normal düzeyde sürdürülür. '
                                         'Tablonun büyümeyi etkilemediği konusunda aileye güvence verilir.',
                          'new_finding': 'İki hafta sonraki kontrolde meyve suyu kesilmişti; dışkılama sayısı günde '
                                         "1-2'ye indi, dışkı şekilli hale geldi. Çocuk kilosunu korudu."},
                         {'text': 'Dışkı sıklığını azaltmak için bir hafta probiyotik ve günlük çinko desteği '
                                  'başlamak, mevcut beslenme düzenini değiştirmeden kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'İki hafta sonra dışkılama paterni aynıydı; meyve suyu tüketimi '
                                             'sürüyordu.',
                          'teaching_point': 'Toddler diyaresinde ilaç veya takviyenin yeri yoktur; tedavi diyetin '
                                            'düzenlenmesidir.'}]}]},
 {'id': 'Y49',
  'category': '👶 Yenidoğan Acilleri',
  'age': '3 Haftalık',
  'gender': 'Kız',
  'complaint': 'Doğumdan sonraki ilk hafta başlayan ve hâlâ geçmeyen ciltte ve göz akında sararma',
  'history': "Annesi anlatıyor: 'Doğumdan sonra 3. gün sarardı, çok yüksek değil denildi ve ışık tedavisi almadı. Üç "
             "haftadır sarılık geçmedi, yüzü ve göğsü hâlâ sarı.' 39. haftada normal doğum, doğum ağırlığı 3200 g. "
             'Yalnız anne sütü alıyor, günde 9-10 kez emiyor, günde 6-7 bez ıslatıyor. Dışkısı sarı ve hardal '
             'kıvamında, idrarı açık renkli. Uykusu ve emmesi iyi. Anne ve bebeğin kan grubu aynı. Yenidoğan tarama '
             'testlerinin sonuçları normal bildirilmiş.',
  'final_diagnosis': 'Anne Sütü Sarılığı (Uzamış İndirekt Hiperbilirubinemi)',
  'disposition': 'Emzirmeye Devam Edilerek Aile Hekimi ve Bilirubin Takibiyle Yeşil Alandan Taburculuk',
  'case_pearl': "Term bebekte 14 günü aşan sarılık 'uzamış sarılık' olarak değerlendirilir ve her bebekte direkt "
                "(konjuge) bilirubin bakılmalıdır. Direkt bilirubin >1 mg/dL veya totalin %20'sinden fazlaysa kolestaz "
                'vardır ve biliyer atrezi için acil ileri tetkik gerekir. Akolik dışkı ve koyu idrar sorgulanır. İyi '
                'kilo alan, dışkısı renkli, indirekt hiperbilirubinemili bebekte anne sütü sarılığı en sık nedendir. '
                'Emzirme kesilmez.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Üç haftalık, yalnız anne sütü alan ve hâlâ sarı olan bu bebeğin değerlendirmesinde öncelikli '
                         'olarak ne yaparsınız?',
             'options': [{'text': 'Sarılığın göğüs hizasında kaldığını görerek bunun beklenen bir süreç olduğunu '
                                  'söyleyip herhangi bir değerlendirme yapmadan aileyi rahatlatmak',
                          'is_correct': False,
                          'scenario_update': 'Bebek muayene edilmeden gönderildi; dışkı rengi, kilo alımı ve bilirubin '
                                             'fraksiyonu hiç değerlendirilmedi.',
                          'teaching_point': 'İki haftayı aşan sarılık her zaman değerlendirilmelidir; kolestaz '
                                            'atlanırsa biliyer atrezide ameliyat şansı kaybedilebilir.'},
                         {'text': 'Sarılık uzadığı için emzirmeyi hemen kesip mama başlatmak ve 48 saat sonra '
                                  'sararmanın azalıp azalmadığını görmek üzere kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Anne emzirmeyi bıraktı, süt üretimi azaldı; bebek mamayı istemedi ve '
                                             'tetkik yapılmadığı için neden belirsiz kaldı.',
                          'teaching_point': 'Emzirmeyi rutin olarak kesmek önerilmez; önce uzamış sarılığın nedeni '
                                            'araştırılmalıdır.'},
                         {'text': 'Büyüme eğrisi, beslenme, dışkı ve idrar rengini sorgulayıp genel durumu, '
                                  'hepatosplenomegaliyi ve sarılığın yaygınlığını muayenede değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Uzamış sarılıkta kilo alımı, dışkının renkli olup olmadığı, idrar rengi ve '
                                         'organomegali kolestatik ve hemolitik nedenleri ayırmada ilk ipuçlarıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 142/dk, SS 40/dk, SpO2 %99. Tartı 4150 g '
                                         '(doğum ağırlığının üzerinde, günlük ortalama 45 g artış). Yüz, göğüs ve '
                                         'karın üst kısmında sarılık, sklera ikterik. Karaciğer kosta kenarında, dalak '
                                         'ele gelmiyor. Bezdeki dışkı sarı-hardal renginde, idrar açık sarı. Emme '
                                         'refleksi ve tonus normal.'},
                         {'text': 'Sarılık derin görünmese de bebeği hemen yenidoğan servisine yatırıp tetkik '
                                  'sonuçları gelmeden yoğun fototerapi başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Bebek anneden ayrıldı ve fototerapiye alındı; sonradan bilirubin '
                                             'değerinin tedavi eşiğinin çok altında olduğu görüldü.',
                          'teaching_point': 'Fototerapi kararı ölçülen bilirubin, saat-yaş ve risk faktörlerine göre '
                                            'verilir; uzamış sarılıkta önce fraksiyon bakılır.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'İyi kilo alan, dışkısı renkli bu bebekte hangi tetkikler uygun olur?',
             'options': [{'text': 'Total ve direkt bilirubin, tam kan sayımı ile retikülosit, tam idrar ve tiroid '
                                  'fonksiyonunu istemek, yenidoğan tarama sonuçlarını teyit etmek',
                          'is_correct': True,
                          'explanation': 'Uzamış sarılıkta kolestazı dışlamak için direkt bilirubin şarttır. Hemoliz, '
                                         'idrar yolu enfeksiyonu ve hipotiroidi de basit tetkiklerle dışlanır.',
                          'new_finding': 'Total bilirubin 13.8 mg/dL, direkt bilirubin 0.5 mg/dL. Hb 14.6 g/dL, '
                                         'retikülosit %1.2, periferik yaymada hemoliz bulgusu yok. Tam idrar normal. '
                                         'TSH 3.1 mIU/L, serbest T4 normal.'},
                         {'text': 'Yalnızca transkutan bilirubin ölçmek ve değer fototerapi eşiğinin altındaysa başka '
                                  'bir tetkik yapmadan iki hafta sonraya kontrol vermek',
                          'is_correct': False,
                          'scenario_update': 'Transkutan değer 13 mg/dL çıktı; ancak direkt fraksiyon bilinmediği için '
                                             'kolestaz dışlanamadı.',
                          'teaching_point': 'Transkutan ölçüm fraksiyon ayırmaz; uzamış sarılıkta serumda direkt '
                                            'bilirubin mutlaka bakılmalıdır.'},
                         {'text': 'Kolestaz şüphesiyle tetkik beklemeden hepatobiliyer sintigrafi ve batın '
                                  'ultrasonografisi isteyip çocuk gastroenterolojiye acil sevk planlamak',
                          'is_correct': False,
                          'scenario_update': 'Sintigrafi için randevu verildi; sonradan direkt bilirubinin normal '
                                             'olduğu ve tetkikin gereksiz olduğu anlaşıldı.',
                          'teaching_point': 'İleri görüntüleme yalnızca direkt hiperbilirubinemi saptandığında '
                                            'gerekir; ilk adım serum fraksiyonlarıdır.'},
                         {'text': 'Enfeksiyon olasılığı nedeniyle tam kan sayımı, CRP, kan kültürü ve lomber ponksiyon '
                                  'yapıp sonuçlar çıkana kadar ampirik antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'İyi görünen ve kilo alan bebek invaziv girişimler ve antibiyotikle '
                                             'hastanede tutuldu; kültürler negatif geldi.',
                          'teaching_point': 'Genel durumu iyi, ateşsiz ve kilo alan bebekte uzamış sarılık tek başına '
                                            'sepsis taraması gerektirmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik ve laboratuvar bulgularına göre en olası tanınız nedir?',
             'options': [{'text': 'Biliyer atrezi (erken dönem)',
                          'is_correct': False,
                          'scenario_update': 'Direkt bilirubin normaldi, dışkı renkliydi ve karaciğer büyük değildi.',
                          'teaching_point': 'Biliyer atrezide direkt hiperbilirubinemi, akolik dışkı ve koyu idrar '
                                            'olur.'},
                         {'text': 'Konjenital hipotiroidiye bağlı uzamış sarılık',
                          'is_correct': False,
                          'scenario_update': 'TSH ve serbest T4 normaldi, kabızlık, makroglossi veya letarji yoktu.',
                          'teaching_point': 'Hipotiroidide kabızlık, hipotoni, geniş fontanel ve yüksek TSH beklenir.'},
                         {'text': 'Hemolitik hastalığa bağlı hiperbilirubinemi',
                          'is_correct': False,
                          'scenario_update': 'Hb ve retikülosit normaldi, kan grubu uyuşmazlığı ve yaymada hemoliz '
                                             'yoktu.',
                          'teaching_point': 'Hemolizde düşen hemoglobin, artmış retikülosit ve yaymada sferosit veya '
                                            'fragmente eritrosit görülür.'},
                         {'text': 'Anne sütü sarılığı',
                          'is_correct': True,
                          'explanation': 'İyi kilo alan, renkli dışkılı, yalnız anne sütüyle beslenen ve indirekt '
                                         'hiperbilirubinemisi olan bebekte diğer nedenler dışlandığında en olası '
                                         'tanıdır.',
                          'new_finding': 'Tanı: Anne sütü sarılığı.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu bebek için en uygun yönetim planı hangisidir?',
             'options': [{'text': 'Emzirmeye 48 saat ara verip mama ile beslemek ve bilirubin düşüşü görülürse tanıyı '
                                  'kesinleştirmiş olarak emzirmeye geri dönmek',
                          'is_correct': False,
                          'scenario_update': 'Emzirme ara verilince anne sütü azaldı; bebek huzursuzlandı ve anne '
                                             'kendini suçlu hissetti.',
                          'teaching_point': 'Tanısal amaçlı emzirmeye ara vermek rutin önerilmez; emzirmeyi sürdürmek '
                                            've izlemek yeterlidir.'},
                         {'text': 'Bilirubini hızlı düşürmek için evde güneş ışığında tutmayı ve öğün aralarında '
                                  'şekerli su ya da bitki çayı vermeyi önermek',
                          'is_correct': False,
                          'scenario_update': 'Bebeğe ek sıvılar verildi; emme sayısı azaldı ve kilo alımı yavaşladı.',
                          'teaching_point': 'Su, şekerli su ve bitki çayı bilirubini düşürmez, emzirmeyi azaltır; '
                                            'güneş ışığı güvenli bir tedavi yöntemi değildir.'},
                         {'text': 'Emzirmeye devam etmeyi önermek, dışkı rengi kartını vermek ve aile hekimiyle 1-2 '
                                  'hafta sonra bilirubin izlemi planlayarak taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Anne sütü sarılığı zararsızdır ve haftalar içinde kendiliğinden geriler. '
                                         'Emzirme sürdürülür, akolik dışkı veya koyu idrar fark edilirse hemen '
                                         'başvurmaları söylenir.',
                          'new_finding': 'Aileye dışkı renk kartı verildi, emzirmenin sürdürülmesi önerildi. İki hafta '
                                         "sonraki kontrolde total bilirubin 8.4 mg/dL'ye geriledi, tartı 4850 g."},
                         {'text': 'Bilirubin metabolizmasını hızlandırmak için iki hafta ursodeoksikolik asit başlamak '
                                  've tedavi sonunda yeniden bilirubin ölçümü yapmak',
                          'is_correct': False,
                          'scenario_update': 'İlaç gereksiz yere başlandı; indirekt hiperbilirubinemide etkisi '
                                             'olmadığından seyir değişmedi.',
                          'teaching_point': 'Ursodeoksikolik asit kolestatik hastalıklarda kullanılır; indirekt '
                                            'hiperbilirubinemide yeri yoktur.'}]}]},
 {'id': 'Y50',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '8 Yaşında',
  'gender': 'Kız',
  'complaint': 'Ateş için sık ibuprofen kullanımı sonrası başlayan mide yanması ve bir kez koyu renkli kusma',
  'history': "Annesi anlatıyor: 'Üç gündür grip nedeniyle ateşi vardı; ateş düşmediği için günde 4-5 kez, çoğu zaman "
             'aç karnına ibuprofen şurup verdim. Dün gece mide kazınması ve yanma başladı. Bu sabah bir kez az '
             "miktarda kahve telvesi gibi koyu renkli kustu. Kakası siyah değil. Baş dönmesi veya bayılması olmadı.' "
             'Ateşi bugün yok. Daha önce mide şikayeti yok. Kullanılan şurup 100 mg/5 mL; dozları ölçü kaşığıyla değil '
             'çay kaşığıyla vermiş. Tartı: 26 kg.',
  'final_diagnosis': 'NSAİİ (İbuprofen) İlişkili Akut Hemorajik Gastrit',
  'disposition': 'Yeşil Alandan NSAİİ Kesilmesi, Oral Proton Pompa İnhibitörü ve Kırmızı Bayrak Eğitimi ile Taburculuk',
  'case_pearl': 'Aç karnına ve sık aralıklarla kullanılan NSAİİ çocukta da mukozal hasara ve üst gastrointestinal '
                'kanamaya yol açabilir. Hemodinamisi stabil, hemoglobini normal, melenası olmayan ve kanaması '
                'kendiliğinden durmuş çocukta ilacın kesilmesi ve oral PPI (omeprazol yaklaşık 1 mg/kg/gün) '
                'yeterlidir; acil endoskopi gerekmez. Tekrarlayan kanama, melena, taşikardi veya Hb düşüşünde yatış ve '
                'endoskopi planlanır. Ailenin doz ölçümü ve dozlar arası süre konusunda eğitimi önemlidir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Bir kez koyu renkli kusan, mide yanması tarif eden bu çocukta ilk değerlendirmede '
                         'önceliğiniz nedir?',
             'options': [{'text': 'Ortostatik nabız ve tansiyon dahil hemodinamiyi, kapiller dolumu, konjonktiva '
                                  'solukluğunu değerlendirmek, karın muayenesi yapıp perianal inspeksiyonla dışkı '
                                  'rengini kontrol etmek',
                          'is_correct': True,
                          'explanation': 'Üst gastrointestinal kanama şüphesinde ilk öncelik hemodinamik stabilitenin '
                                         'değerlendirilmesidir. Ortostatik değişiklikler, solukluk ve melena kanamanın '
                                         'boyutunu gösterir; karın muayenesi perforasyon bulgularını dışlar.',
                          'new_finding': 'Vital Bulgular: Ateş 37.0°C, KTA 94/dk (ayağa kalkınca 100/dk), SS 20/dk, TA '
                                         '104/66 mmHg, KDZ 1.5 sn. Genel durumu iyi, konjonktivalar pembe. Karın '
                                         'yumuşak, epigastriumda orta hassasiyet; defans ve rebound yok. Perianal '
                                         'inspeksiyonda bezde normal kahverengi dışkı, melena yok. Ağız ve burunda '
                                         'kanama odağı yok.'},
                         {'text': 'Kahve telvesi kusmanın kaynağını doğrulamak için nazogastrik sonda takıp serum '
                                  'fizyolojik ile lavaj yapmak, aspirat temizlenince vital bulgu ve karın muayenesini '
                                  'tamamlamak',
                          'is_correct': False,
                          'scenario_update': 'Lavaj sıvısı berrak geldi; çocuk işlem sırasında çok ağladı ve öğürdü. '
                                             'Hemodinami değerlendirmesi gecikti.',
                          'teaching_point': 'Stabil çocukta nazogastrik lavaj tanısal ya da tedavi edici değildir; ilk '
                                            'adım hemodinamik değerlendirmedir.'},
                         {'text': 'Kusmanın burun kanamasından yutulan kan olabileceğini düşünüp ağırlıklı olarak '
                                  'kulak-burun-boğaz muayenesi yapmak ve ardından taburculuğu değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Burunda kanama odağı saptanmadı. Hemodinami ve karın muayenesi '
                                             'sistematik yapılmadığı için kanamanın kaynağı ve boyutu belirsiz kaldı.',
                          'teaching_point': 'Yutulan kan ayırıcı tanıda düşünülmelidir ancak hemodinamik ve karın '
                                            'muayenesinin yerini almaz.'},
                         {'text': 'Epigastrik ağrı nedeniyle muayene öncesinde intravenöz parasetamol ve ondansetron '
                                  'yapmak, ağrı geçince karın muayenesini ve vital bulguları değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'İlaçlar sonrası çocuk rahatladı; ancak ilk vital bulgular ve ortostatik '
                                             'değerlendirme yapılmadan zaman geçti.',
                          'teaching_point': 'Kanama şüphesinde semptomatik tedavi öncesinde hemodinami ve muayene '
                                            'kaydedilmelidir.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Hemodinamisi stabil, melenası olmayan, bir kez az miktarda koyu kusan bu çocukta tetkik '
                         'yaklaşımınız nedir?',
             'options': [{'text': 'Helicobacter pylori enfeksiyonunu dışlamak için dışkı antijen testi istemek ve '
                                  'sonuç pozitif gelirse eradikasyon tedavisi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Test sonucu iki gün sonra negatif geldi; acil yönetim açısından bilgi '
                                             'sağlamadı.',
                          'teaching_point': 'Akut kanamada dışkı antijen testi ve eradikasyon planı ilk basamak '
                                            'değildir; ayrıca yakın dönem PPI kullanımı yanlış negatifliğe yol '
                                            'açabilir.'},
                         {'text': 'Ateş öyküsü nedeniyle tam kan sayımı, CRP, kan kültürü ve batın ultrasonografisi '
                                  'isteyip kanamanın enfeksiyonla ilişkisini araştırmak',
                          'is_correct': False,
                          'scenario_update': 'CRP hafif yüksek, kültür negatif ve ultrasonografi normal geldi; '
                                             'sonuçlar kanamanın nedenini açıklamadı.',
                          'teaching_point': 'Tetkikler klinik soruya yönelik olmalıdır; kanamanın en olası nedeni ilaç '
                                            'öyküsünde saklıdır.'},
                         {'text': 'Tam kan sayımı ve dışkıda gizli kan istemek, hemoglobin normal ve kusma '
                                  'tekrarlamıyorsa ek tetkik planlamadan ilaç öyküsünü ayrıntılı netleştirmek',
                          'is_correct': True,
                          'explanation': 'Stabil hastada başlangıç hemoglobini kanamanın boyutunu ve izlem '
                                         'gereksinimini belirler. Ayrıntılı ilaç öyküsü (doz, sıklık, aç karnına '
                                         'kullanım) mukozal hasarın nedenini ortaya koyar.',
                          'new_finding': 'Hb 12.4 g/dL, Hct %37, trombosit 280.000/mm³, MCV normal. Dışkıda gizli kan '
                                         'pozitif. İlaç öyküsünde günde 4-5 kez, her seferinde yaklaşık 10-12 mg/kg '
                                         'ibuprofen verildiği, dozlar arasında 4 saatten kısa aralıklar olduğu ve '
                                         'çoğunun aç karnına olduğu belirlendi.'},
                         {'text': 'Tam kan sayımı, kan grubu ve koagülasyon testleri istemek ve bilinmeyen kaynaklı '
                                  'kanama nedeniyle aynı gün çocuk gastroenterolojisinden acil endoskopi talep etmek',
                          'is_correct': False,
                          'scenario_update': 'Hemoglobin normal geldi; gastroenterolog stabil hastada acil endoskopi '
                                             'gerekmediğini belirtti ve çocuk saatlerce aç bekletildi.',
                          'teaching_point': 'Stabil, kanaması durmuş ve açık bir tetikleyicisi olan çocukta acil '
                                            'endoskopi endike değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Aç karnına sık NSAİİ kullanımı sonrası epigastrik yanma, kahve telvesi kusma, stabil '
                         'hemodinami ve normal hemoglobin varlığında en olası tanı nedir?',
             'options': [{'text': 'Mallory-Weiss yırtığı',
                          'is_correct': False,
                          'scenario_update': 'Kanamadan önce tekrarlayan şiddetli öğürme veya kusma öyküsü yok.',
                          'teaching_point': 'Mallory-Weiss yırtığında hematemez tekrarlayan kusmaların ardından '
                                            'gelişir.'},
                         {'text': 'NSAİİ ilişkili akut hemorajik gastrit',
                          'is_correct': True,
                          'explanation': 'Sık ve aç karnına ibuprofen kullanımı prostaglandin aracılı mukozal korumayı '
                                         'bozarak erozif-hemorajik gastrite yol açar; az miktarda hematemez ve '
                                         'epigastrik yanma tipik bulgulardır.',
                          'new_finding': 'Tanı: NSAİİ (İbuprofen) İlişkili Akut Hemorajik Gastrit.'},
                         {'text': 'Akut kolesistit',
                          'is_correct': False,
                          'scenario_update': 'Sağ üst kadran hassasiyeti, Murphy bulgusu ve sarılık yok; hematemez '
                                             'kolesistit bulgusu değildir.',
                          'teaching_point': 'Epigastrik yanma ve hematemez mide-duodenum kaynaklı patolojiyi '
                                            'düşündürür.'},
                         {'text': 'Özofageal varis kanaması',
                          'is_correct': False,
                          'scenario_update': 'Kronik karaciğer hastalığı, splenomegali veya portal hipertansiyon '
                                             'bulgusu yok.',
                          'teaching_point': 'Varis kanaması genellikle masif ve hemodinamik etkilenmeyle seyreder.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': "Hemoglobini normal ve stabil olan bu 26 kg'lık çocuğun tedavi planı nasıl olmalıdır?",
             'options': [{'text': 'İbuprofen dozunu azaltıp parasetamol ile dönüşümlü vermeyi sürdürmek, mide koruması '
                                  'için her dozdan önce antasit süspansiyonu kullanmasını ve ilacı tok karnına '
                                  'vermesini önermek',
                          'is_correct': False,
                          'scenario_update': 'İbuprofen sürdürülünce iki gün sonra epigastrik ağrı arttı ve çocuk '
                                             'tekrar koyu renkli kustu.',
                          'teaching_point': 'Mukozal kanama gelişen çocukta NSAİİ kesilmelidir; antasit tek başına '
                                            'yeterli koruma sağlamaz.'},
                         {'text': 'İbuprofeni kesmek, yaklaşık 1 mg/kg/gün oral omeprazol başlamak, ateş için '
                                  'parasetamol önermek ve melena veya kan kusmada dönüşü anlatmak',
                          'is_correct': True,
                          'explanation': 'Tedavinin temeli suçlu ilacın kesilmesi ve mukozal iyileşmeyi sağlayan asit '
                                         'baskılamadır. Ateş için doğru dozda parasetamol kullanımı ve kırmızı '
                                         'bayraklar ayrıntılı anlatılır; 2-4 hafta PPI genellikle yeterlidir.',
                          'new_finding': 'Omeprazol 20 mg/gün başlandı, aileye parasetamol doz tablosu ve ölçü kaşığı '
                                         'kullanımı gösterildi. 48 saat sonraki kontrolde mide yanması gerilemişti, '
                                         'kusma tekrarlamadı, dışkı rengi normaldi.'},
                         {'text': 'Yatırarak intravenöz pantoprazol infüzyonu başlamak, 24 saat oral alımı kapatmak ve '
                                  'ertesi gün kontrol hemoglobini ile endoskopi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Stabil çocuk gereksiz yere yatırıldı ve aç bırakıldı; kontrol '
                                             'hemoglobini değişmedi, endoskopi iptal edildi.',
                          'teaching_point': "Hemodinamisi stabil, Hb'si normal ve kanaması durmuş çocukta yatış, "
                                            'intravenöz PPI ve acil endoskopi gerekmez.'},
                         {'text': 'İbuprofeni kesip yalnızca sukralfat süspansiyonu başlamak, beslenmeyi sulu '
                                  'gıdalarla sınırlamak ve bir hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Sukralfat sonrası çocuk kabızlık geliştirdi; yanma yakınması yavaş '
                                             'geriledi.',
                          'teaching_point': 'Asit baskılama ilk seçenektir; sukralfat ikinci basamak bir mukozal '
                                            'koruyucudur ve kısıtlayıcı diyet gerekmez.'}]}]}]
