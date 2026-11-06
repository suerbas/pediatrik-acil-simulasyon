# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Yeşil Alan Vakaları (Part 5: G41 - G50)
Odak: Bulantı, Kusma, Karın Ağrısı, İshal (GİS Acilleri - Yeşil Alan Ayaktan Yönetim)
Kılavuzlar: ESPGHAN, AAP, NASPGHAN, NICE
"""

GREEN_CASES_PART5 = [{'id': 'G41',
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
 {'id': 'G42',
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
 {'id': 'G43',
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
 {'id': 'G44',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '6 Haftalık',
  'gender': 'Kız',
  'complaint': 'Üç haftadır her akşam saatlerce süren, susturulamayan ağlama nöbetleri',
  'history': "Ailesi anlatıyor: 'Üç haftadır her akşam saat 18:00 civarında başlıyor. Yüzü kızarıyor, bacaklarını "
             'karnına çekiyor, ellerini yumruk yapıp 3-4 saat çığlık atarak ağlıyor. Gaz çıkarınca biraz rahatlıyor '
             'gibi, sonra yine başlıyor. Gün içinde neşeli, emmesi iyi. Ateşi veya kusması olmadı. Bu akşam her '
             "zamankinden farklı olarak kucakta da hiç susmadı, bu yüzden geldik. Biz uykusuzluktan tükendik.' Term "
             'doğum, sadece anne sütü alıyor.',
  'final_diagnosis': 'İnfantil Kolik (Roma IV Kriterleri)',
  'disposition': 'Yeşil Alandan Aileye Güvence, Yatıştırma Teknikleri ve Ebeveyn Tükenmişliği Danışmanlığı ile '
                 'Taburculuk',
  'case_pearl': 'Beş aydan küçük, sağlıklı büyüyen bebekte açıklanamayan uzun ağlama nöbetleri infantil koliği '
                'düşündürür; ancak tanı tam soyarak yapılan muayeneyle organik nedenler (saç turnikesi, korneal '
                'abrazyon, fıtık, otitis, fraktür, idrar yolu enfeksiyonu) dışlandıktan sonra konur. Simetikon, '
                'antispazmodikler ve asit baskılayıcılar etkisizdir. Ebeveyn tükenmişliği sorgulanmalı ve sarsılmış '
                'bebek sendromu açısından önleyici danışmanlık verilmelidir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Akşamları uzun süre ağlayan, bu akşam kucakta da susmayan 6 haftalık bu bebekte muayenede '
                         'öncelikli yaklaşımınız nedir?',
             'options': [{'text': 'Ağlama sırasında bacakları karnına çekmesini karın kaynaklı kabul edip batın '
                                  'palpasyonu ve oskültasyonu yaparak gaz giderici damla vermek',
                          'is_correct': False,
                          'scenario_update': 'Batın muayenesi normal bulundu. Simetikon sonrası ağlama değişmedi; '
                                             'diğer sistemler muayene edilmeden bebek gözleme alındı.',
                          'teaching_point': 'Bacakları karna çekme spesifik değildir; gaz giderici damlaların '
                                            'etkinliği gösterilmemiştir ve kapsamlı muayenenin yerine geçemez.'},
                         {'text': 'Bebeği tamamen soyarak el-ayak parmaklarında saç turnikesi, korneada çizik, kasık '
                                  'fıtığı, kulak zarları ve uzun kemiklerde hassasiyet dahil baştan ayağa muayene '
                                  'etmek',
                          'is_correct': True,
                          'explanation': 'Susturulamayan ağlama ile başvuran süt çocuğunda organik nedenler sistematik '
                                         've tam soyulmuş muayeneyle aranmalıdır. Saç turnikesi, korneal abrazyon, '
                                         'inkarsere fıtık ve istismara bağlı fraktürler yalnızca bu şekilde fark '
                                         'edilir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.9°C, KTA 138/dk, SS 36/dk, SpO2 %99. Tartı 4.9 kg '
                                         '(doğum 3.4 kg; günlük ortalama 35 g artış). Saç turnikesi yok. Flöresein ile '
                                         'kornealar temiz. Kulak zarları doğal. Kasık kanallarında fıtık yok, dış '
                                         'genitalya doğal. Fontanel düz, tonus normal. Kemiklerde hassasiyet ve ciltte '
                                         'morluk yok. Muayene sırasında bebek emzik ile sakinleşti.'},
                         {'text': 'Susmayan ağlama nedeniyle muayeneden önce idrar sondası ile tam idrar tetkiki ve '
                                  'kültür almak, sonra bebeği giyinik halde muayene etmek',
                          'is_correct': False,
                          'scenario_update': 'İdrar tetkiki normal geldi. Giyinik muayenede sistemik bir sorun '
                                             'bulunmadı ancak ayak parmakları ve kornealar değerlendirilmedi.',
                          'teaching_point': 'Ateşsiz ve iyi görünen bebekte ilk adım tam soyulmuş fizik muayenedir; '
                                            'tetkikler muayene bulgularına göre seçilir.'},
                         {'text': 'Ailenin tükenmişliğini fark edip önce onlarla görüşmek, bebeğin vitallerini ve '
                                  'tartısını alarak muayeneyi bebek sakinleştikten sonraki bir zamana bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Bebek bir saat sonra uyudu ve muayene yüzeysel yapıldı; aile bebeğin '
                                             'neden ağladığına dair bir açıklama almadan bekledi.',
                          'teaching_point': 'Ebeveyn desteği önemlidir ancak organik nedenleri dışlayan tam muayene '
                                            'geciktirilmemelidir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Muayenesi tamamen normal olan, iyi kilo alan ve emzikle sakinleşen bu bebekte tetkik '
                         'yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Tetkik istemeden aileyle ağlama günlüğünü gözden geçirmek, bebeğin acilde bir '
                                  'beslenmesini ve sakinleşmesini gözlemleyip kırmızı bayrakları sorgulamak',
                          'is_correct': True,
                          'explanation': 'Normal muayene, iyi kilo alımı ve tipik ağlama paterni olan bebekte '
                                         'laboratuvar tetkiki tanıya katkı sağlamaz. Beslenme gözlemi ve kırmızı '
                                         'bayrak sorgusu (kusma, ateş, letarji, kilo kaybı) yeterlidir.',
                          'new_finding': 'Bebek acilde etkin emdi, kusmadı, gaz çıkardıktan sonra uyudu. Ağlama '
                                         'günlüğünde günde ortalama 3.5 saat, haftada 6 gün, akşam saatlerinde '
                                         'yoğunlaşan nöbetler kaydedildi. Ateş, kusma veya dışkıda kan yok.'},
                         {'text': 'Reflüye bağlı ağrıyı dışlamak için batın ultrasonografisi ve özofagus pH '
                                  'monitorizasyonu planlamak üzere bebeği gastroenteroloji polikliniğine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografi normal bulundu; pH monitorizasyonu için randevu 2 ay '
                                             'sonraya verildi ve aile kaygıyla beklemeye başladı.',
                          'teaching_point': 'Kusma, beslenme reddi veya kilo kaybı olmayan ağlayan bebekte reflü '
                                            'araştırması önerilmez; ağlama tek başına reflü göstergesi değildir.'},
                         {'text': 'Süt alerjisini dışlamak için kan eozinofil sayısı ve inek sütü spesifik IgE düzeyi '
                                  'istemek, sonuç gelene kadar annenin süt tüketimini kesmek',
                          'is_correct': False,
                          'scenario_update': 'Spesifik IgE negatif geldi. Bu sürede anneye gereksiz diyet kısıtlaması '
                                             'uygulandı ve emzirme motivasyonu azaldı.',
                          'teaching_point': 'Kanlı dışkı, egzama veya kusma gibi destekleyici bulgu yoksa alerji '
                                            'testleri önerilmez; diyet kısıtlaması rutin değildir.'},
                         {'text': 'Uzun ağlama nöbetleri nedeniyle olası nöbet aktivitesini değerlendirmek için kan '
                                  'şekeri, elektrolitler ve elektroensefalografi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Kan şekeri ve elektrolitler normal geldi; EEG randevusu verildi ve aile '
                                             'bebekte nörolojik bir hastalık olduğu endişesine kapıldı.',
                          'teaching_point': 'Nöbet düşündüren stereotipik hareket, göz deviasyonu veya bilinç '
                                            'değişikliği yoksa nörolojik tetkik gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Sağlıklı büyüyen, muayenesi normal 6 haftalık bebekte haftada 6 gün, günde 3 saati aşan '
                         'akşam ağlama nöbetlerinin en olası nedeni nedir?',
             'options': [{'text': 'İnek sütü proteini alerjisi',
                          'is_correct': False,
                          'scenario_update': 'Kanlı-mukuslu dışkı, egzama, kusma veya kilo alımında duraklama yok.',
                          'teaching_point': 'İzole ağlama, alerji tanısı için yeterli değildir.'},
                         {'text': 'İnfantil diskezi',
                          'is_correct': False,
                          'scenario_update': 'Diskezide ağlama ve ıkınma yumuşak dışkılama öncesinde kısa sürelidir; '
                                             'akşam saatlerinde uzun nöbetler beklenmez.',
                          'teaching_point': 'Diskezi dışkılama ile zamansal ilişkili ve dakikalarla sınırlı bir '
                                            'tablodur.'},
                         {'text': 'İnfantil kolik',
                          'is_correct': True,
                          'explanation': 'Beş aydan küçük, sağlıklı büyüyen bebekte belirgin bir neden olmadan '
                                         'tekrarlayan, uzun süreli, yatıştırılması güç ağlama nöbetleri ve normal '
                                         'muayene Roma IV infantil kolik tanısını karşılar.',
                          'new_finding': 'Tanı: İnfantil Kolik (Roma IV kriterleri, organik nedenler dışlandı).'},
                         {'text': 'Gastroözofageal reflü hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Kusma, beslenme reddi, kilo kaybı veya ark yapma yok; ağlama beslenmeyle '
                                             'ilişkili değil.',
                          'teaching_point': 'Reflü hastalığı tanısı için kusmaya eşlik eden komplikasyon bulguları '
                                            'gerekir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu bebeğin ailesine yönelik en uygun taburculuk planı hangisidir?',
             'options': [{'text': 'Ağlama nöbetlerinde kullanılmak üzere simetikon damla ve rezene çayı önermek, '
                                  'anneye süt ve kafein kısıtlaması yaparak taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'İki hafta sonra ağlama süresinde değişiklik olmadı; annenin kısıtlı '
                                             'diyeti nedeniyle süt miktarı azaldı.',
                          'teaching_point': 'Simetikonun etkinliği gösterilmemiştir, bitki çayları süt çocuğunda '
                                            'önerilmez ve rutin anne diyeti kısıtlaması gereksizdir.'},
                         {'text': 'Ağrıyı azaltmak amacıyla anne sütünü kesip hidrolize formüle geçmek ve bir hafta '
                                  'sonra kontrolde formülün etkisini değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Formüle geçişle ağlama değişmedi; emzirme sonlandı ve anne bu karardan '
                                             'pişmanlık duydu.',
                          'teaching_point': 'Alerji bulgusu olmayan bebekte anne sütünü kesmek önerilmez; hidrolize '
                                            'formül yalnızca seçilmiş olgularda düşünülür.'},
                         {'text': 'Tablonun selim olduğunu anlatıp yatıştırma tekniklerini göstermek, tükenince bebeği '
                                  'güvenle bırakıp ara vermeyi ve asla sarsmamayı öğretmek',
                          'is_correct': True,
                          'explanation': 'Tedavinin temeli aileye güvence, kundaklama, beyaz gürültü, ritmik sallama '
                                         'gibi yatıştırma teknikleri ve ebeveyn tükenmişliğine yönelik danışmanlıktır. '
                                         'Sarsılmış bebek sendromunu önleyici eğitim ve sosyal destek planı mutlaka '
                                         'verilmelidir.',
                          'new_finding': 'Ebeveynlere yatıştırma teknikleri uygulamalı gösterildi, dönüşümlü dinlenme '
                                         'planı yapıldı ve aile hekimine 1 hafta sonra kontrol yazıldı. Kontrolde '
                                         'ailenin baş etme becerisinin arttığı, ağlama süresinin azalmaya başladığı '
                                         'görüldü.'},
                         {'text': 'Ağlama nöbetlerinde kullanılmak üzere düşük doz oral antispazmodik damla başlamak '
                                  've bebeğin uykusunu düzenlemek için akşam emzirme aralığını uzatmak',
                          'is_correct': False,
                          'scenario_update': 'Antispazmodik sonrası bebekte uyku hali ve beslenme isteksizliği '
                                             'gelişti; aile ilacı kendisi kesti.',
                          'teaching_point': 'Antikolinerjik antispazmodikler 6 aydan küçük bebeklerde apne ve '
                                            'konvülziyon riski nedeniyle kontrendikedir.'}]}]},
 {'id': 'G45',
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
 {'id': 'G46',
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
 {'id': 'G47',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '7 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Üst solunum yolu enfeksiyonundan bir hafta sonra başlayan sağ alt karın ağrısı ve hafif ateş',
  'history': "Ailesi anlatıyor: 'Bir hafta önce ateş, burun akıntısı ve boğaz ağrısı geçirdi, tam iyileşti derken iki "
             'gündür karnının sağ alt tarafı sızlıyor. Ateşi evde 37.6°C ölçüldü. Kusması veya ishali yok, iştahı '
             "biraz azaldı ama yemek yiyor. Zıplayınca sağ tarafında hafif batma oluyor, yürüyebiliyor.' Daha önce "
             'benzer şikayeti olmamış.',
  'final_diagnosis': 'Akut Mezenterik Lenfadenit',
  'disposition': 'Yeşil Alanda USG ile Cerrahi Nedenlerin Dışlanması, Semptomatik Tedavi ve 24 Saatlik Yeniden '
                 'Değerlendirme Planıyla Taburculuk',
  'case_pearl': 'Viral üst solunum yolu enfeksiyonu sonrası sağ alt kadran ağrısı ve hafif ateşle gelen çocukta '
                'mezenterik lenfadenit sık bir nedendir; ancak tanı apandisit dışlanmadan konmamalıdır. Normal '
                'kalibrede (<6 mm), komprese edilebilen apendiksin USG ile gösterilmesi ve kümelenmiş, kısa aksı 8 '
                "mm'yi aşan mezenterik lenf nodları tanıyı destekler. Tablo destek tedavisiyle düzelir; ağrı artarsa "
                'yeniden değerlendirme şarttır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Yakın zamanda üst solunum yolu enfeksiyonu geçiren, sağ alt kadran ağrısı ve hafif ateşi '
                         'olan bu çocukta ilk değerlendirmeniz nasıl olmalıdır?',
             'options': [{'text': 'Karın ağrısının kabızlığa bağlı olabileceğini düşünüp dışkılama alışkanlığını '
                                  'sorgulamak ve muayene öncesinde gliserinli rektal lavman uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Lavman sonrası çocuk az miktarda normal dışkı çıkardı; ağrısı değişmedi '
                                             've karın muayenesi gecikti.',
                          'teaching_point': 'Ateşli sağ alt kadran ağrısında lavman öncesinde cerrahi patolojiler '
                                            'değerlendirilmelidir.'},
                         {'text': 'Ağrının zamanla yer değiştirip değiştirmediğini, kusma-iştah değişimini sorgulayıp '
                                  'sağ alt kadran hassasiyeti, defans, rebound, zıplama testi ve skrotal muayene '
                                  'yapmak',
                          'is_correct': True,
                          'explanation': 'Sağ alt kadran ağrısında ağrının göçü, anoreksi ve kusma öyküsü ile '
                                         'peritoneal irritasyon bulguları ve zıplama testi cerrahi patolojiyi '
                                         'değerlendirmede temel bileşenlerdir. Erkek çocukta skrotal muayene '
                                         'atlanmamalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 37.5°C, KTA 92/dk, SS 20/dk, SpO2 %99. Ağrı başından '
                                         'beri sağ alt kadranda, göç etmemiş. Kusma yok, iştah hafif azalmış. '
                                         'Orofarenks hafif hiperemik, servikal küçük lenf nodları. Sağ alt kadranda '
                                         'hafif-orta palpasyon hassasiyeti; istemsiz defans ve rebound yok. Tek ayak '
                                         'üzerinde zıplayabiliyor, hafif rahatsızlık tarif ediyor. Testisler doğal.'},
                         {'text': 'Ateş ve yakın zamandaki enfeksiyon öyküsü nedeniyle akciğer ve orofarenks '
                                  'muayenesini önceleyip karın muayenesini analjezik etkisi geçtikten sonra yapmak',
                          'is_correct': False,
                          'scenario_update': 'Akciğer muayenesi normal bulundu. Karın muayenesi bir saat ertelendi ve '
                                             'ağrının karakteri hakkında bilgi alınmadan zaman kaybedildi.',
                          'teaching_point': 'Sağ alt kadran ağrılı çocukta karın muayenesi önceliklidir; analjezi '
                                            'muayeneyi maskelemez ancak muayene ertelenmemelidir.'},
                         {'text': 'Sağ alt kadran ağrısıyla gelen her çocukta olduğu gibi oral alımı kesip intravenöz '
                                  'sıvı başlatmak ve muayeneden önce çocuk cerrahisini çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Cerrahi ekip muayeneden önce çağrıldı; peritoneal bulgu saptanmadı ve '
                                             'hasta ön değerlendirme yapılmadan acil konsülte edildiği için süreç '
                                             'uzadı.',
                          'teaching_point': 'Konsültasyon kararı klinik değerlendirme ve risk sınıflamasına göre '
                                            'verilir; iyi görünen çocukta önce tam muayene yapılır.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Peritoneal bulgusu olmayan ancak sağ alt kadranda hassasiyeti süren bu çocukta tetkik '
                         'yaklaşımınız nedir?',
             'options': [{'text': 'Radyasyon riskine rağmen kesin sonuç almak amacıyla intravenöz kontrastlı batın '
                                  'bilgisayarlı tomografisi çekip cerrahiye konsülte etmek',
                          'is_correct': False,
                          'scenario_update': 'Tomografide sağ alt kadranda birkaç lenf nodu görüldü; bulgu ultrasonla '
                                             'da gösterilebilecek düzeydeydi ve çocuk gereksiz radyasyona maruz kaldı.',
                          'teaching_point': 'Çocukta sağ alt kadran ağrısında ilk görüntüleme ultrasonografidir; '
                                            'tomografi yalnızca USG tanısal olmadığında ve klinik şüphe sürdüğünde '
                                            'düşünülür.'},
                         {'text': 'Laboratuvar tetkiki olmadan yalnızca ayakta direkt batın grafisi çekip apendikolit '
                                  'veya gaz-sıvı seviyesi yoksa taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Grafide patolojik bulgu yoktu; ancak grafi apendiksi değerlendiremediği '
                                             'için tablo aydınlatılmadan taburculuk düşünüldü.',
                          'teaching_point': 'Direkt grafi sağ alt kadran ağrısında düşük duyarlılığa sahiptir ve tek '
                                            'başına güvence vermez.'},
                         {'text': 'Ateşli karın ağrısında idrar yolu enfeksiyonunu dışlamak için yalnızca tam idrar '
                                  'tetkiki istemek ve normal gelirse antibiyotiksiz taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Tam idrar tetkiki normal geldi; sağ alt kadran hassasiyeti açıklanmadan '
                                             'çocuk taburcu edilecekti.',
                          'teaching_point': 'İdrar tetkiki ayırıcı tanıda yararlıdır ancak lokalize sağ alt kadran '
                                            'hassasiyetinde görüntüleme ve laboratuvar değerlendirmesinin yerini '
                                            'tutmaz.'},
                         {'text': 'Tam kan sayımı, CRP ve batın ultrasonografisi istemek; ultrasonda apendiksin '
                                  'görüntülenmesini, çapını ve kompresibilitesini özellikle sorgulamak',
                          'is_correct': True,
                          'explanation': 'Orta riskli sağ alt kadran ağrısında laboratuvar ve ultrasonografi birlikte '
                                         'risk sınıflamasını belirler. Normal kalibrede ve komprese edilebilen '
                                         'apendiksin gösterilmesi cerrahi patolojiyi büyük ölçüde dışlar.',
                          'new_finding': 'Lökosit 8.400/mm³ (%55 nötrofil), CRP 8 mg/L. Batın USG: Apendiks 4.2 mm '
                                         'çapında, komprese edilebilir, periapendiküler yağlanma yok. Sağ alt kadran '
                                         'mezenter kökünde en büyüğü 11x6 mm, oval, ekojen hilusu korunmuş çok sayıda '
                                         'kümelenmiş lenf nodu. Serbest sıvı yok.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Viral enfeksiyon sonrası sağ alt kadran ağrısı, normal apendiks ve kümelenmiş büyük lenf '
                         'nodları saptanan bu çocukta tanı nedir?',
             'options': [{'text': 'Akut mezenterik lenfadenit',
                          'is_correct': True,
                          'explanation': 'Üst solunum yolu enfeksiyonunu izleyen sağ alt kadran ağrısı, normal '
                                         "kalibrede komprese edilebilen apendiks ve kısa aksı 8 mm'yi aşan kümelenmiş "
                                         'mezenterik lenf nodları mezenterik lenfaditi destekler.',
                          'new_finding': 'Tanı: Akut Mezenterik Lenfadenit (apendiks normal).'},
                         {'text': 'Sağ üreter taşına bağlı kolik',
                          'is_correct': False,
                          'scenario_update': 'Kolik tarzda ağrı, hematüri ve hidronefroz yok.',
                          'teaching_point': 'Renal kolik ani başlangıçlı, dalgalı ağrı ve idrar bulgularıyla '
                                            'seyreder.'},
                         {'text': 'Meckel divertiküliti',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonda kör sonlanan inflame divertiküler yapı veya çevre yağlanması '
                                             'görülmedi.',
                          'teaching_point': 'Meckel divertiküliti ultrasonda apendiksten ayrı inflame yapı olarak '
                                            'izlenir.'},
                         {'text': 'Erken evre akut apandisit',
                          'is_correct': False,
                          'scenario_update': 'Apendiks 4.2 mm, komprese edilebilir ve çevresinde inflamasyon yok; '
                                             'laboratuvar normal.',
                          'teaching_point': 'Normal apendiksin gösterilmesi apandisiti büyük ölçüde dışlar ancak '
                                            'şikayet ilerlerse yeniden değerlendirme gerekir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuğun tedavi ve izlem planı nasıl olmalıdır?',
             'options': [{'text': 'Cerrahi patolojiyi kesin olarak dışlamak için çocuğu oral alımı kapalı olarak 24 '
                                  'saat çocuk cerrahisi servisinde seri muayeneyle izlemek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk 24 saat aç izlendi; şikayetleri hızla gerileyen hastada gereksiz '
                                             'yatış oldu.',
                          'teaching_point': "Genel durumu iyi, ağrısı hafif ve USG'de apendiksi normal çocukta "
                                            'güvenilir bir aileyle ayaktan izlem uygundur.'},
                         {'text': 'Parasetamol ve hidrasyon önerip, ağrının artması, kusma, yürürken zorlanma veya '
                                  'ateş yükselmesinde dönmeyi anlatarak 24 saat içinde yeniden değerlendirme planlamak',
                          'is_correct': True,
                          'explanation': 'Mezenterik lenfadenit kendini sınırlayan bir tablodur; destek tedavisi '
                                         "yeterlidir. Erken apandisitin USG'de gözden kaçabileceği unutulmamalı, net "
                                         'dönüş kriterleri ve 24 saatlik yeniden değerlendirme planlanmalıdır.',
                          'new_finding': 'Çocuk parasetamol ile taburcu edildi. 24. saatteki kontrolde ağrısı azalmış, '
                                         'karın muayenesi rahattı; 72 saatte şikayetleri tamamen geçti.'},
                         {'text': 'Lenf nodlarının boyutu nedeniyle lenfoma olasılığını dışlamak için tam kan sayımı, '
                                  'LDH, ürik asit ve periferik yayma istemek ve onkolojiye yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Tetkikler normal geldi; aile onkoloji yönlendirmesi nedeniyle büyük '
                                             'kaygı yaşadı.',
                          'teaching_point': 'Ekojen hilusu korunmuş, oval, kümelenmiş reaktif nodlar enfeksiyon '
                                            'sonrası beklenen bulgulardır; sistemik bulgu yoksa malignite araştırması '
                                            'gerekmez.'},
                         {'text': 'Bakteriyel süperenfeksiyon olasılığına karşı yedi gün oral amoksisilin-klavulanat '
                                  'başlamak ve ağrı için parasetamol önererek bir hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotikle çocukta ishal gelişti; ağrısı zaten 48 saatte geriliyordu.',
                          'teaching_point': 'Viral kökenli mezenterik lenfaditte rutin antibiyotik gerekmez.'}]}]},
 {'id': 'G48',
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
 {'id': 'G49',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '3 Aylık',
  'gender': 'Kız',
  'complaint': 'Her beslenme sonrası ağzından kesilmiş süt çıkarması',
  'history': "Annesi anlatıyor: 'Emzirdikten hemen sonra veya gaz çıkarırken günde 5-6 kez ağzından süt ya da yoğurt "
             'gibi kesilmiş süt geliyor. Bunu yaparken ağlamıyor, gülümsüyor bile. Boğulur gibi olmuyor, morarmıyor. '
             'Kilo alıyor. Ama komşular mutlaka mide ilacı başlamamız gerektiğini söylüyor, bir arkadaşımın bebeğine '
             "de şurup verilmiş. Endişelendik.' Term doğum, sadece anne sütü alıyor.",
  'final_diagnosis': 'Fizyolojik Gastroözofageal Reflü (Komplikasyonsuz)',
  'disposition': 'Yeşil Alandan Aile Eğitimi, Asit Baskılayıcı İlaçtan Kaçınma ve Beslenme Önerileri ile Taburculuk',
  'case_pearl': 'Süt çocuklarının yaklaşık yarısında görülen ağrısız, eforsuz, beslenme sonrası kusma; kilo alımı '
                'normal, beslenme reddi ve solunum komplikasyonu yoksa fizyolojiktir ve genellikle 12-14 ayda düzelir. '
                'Tanı kliniktir; tetkik ve asit baskılayıcı tedavi önerilmez (NASPGHAN/ESPGHAN 2018). Safralı veya '
                'fışkırır kusma, kilo kaybı, letarji, fontanel bombeliği, 6 aydan sonra başlangıç kırmızı bayraktır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Beslenme sonrası sık süt çıkaran, keyfi yerinde 3 aylık bu bebekte değerlendirmenin odağı ne '
                         'olmalıdır?',
             'options': [{'text': 'Kusma sıklığı nedeniyle sağ üst kadranda zeytin benzeri kitle aramak için bebeği '
                                  'beslerken epigastriumu palpe edip acil batın ultrasonografisi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Kitle palpe edilmedi; ultrasonografi normal geldi. Kusmaların fışkırır '
                                             'olmadığı ve bebeğin kilo aldığı sorgulanmamıştı.',
                          'teaching_point': 'Fışkırır kusma ve kilo alamama olmadan pilor görüntülemesi gerekmez; '
                                            'kusmanın niteliği öyküyle ayırt edilir.'},
                         {'text': 'Kusmalara bağlı aspirasyon riskini değerlendirmek için muayeneyle birlikte akciğer '
                                  'grafisi çekmek ve uyku sırasında apne monitörizasyonu önermek',
                          'is_correct': False,
                          'scenario_update': 'Akciğer grafisi normal geldi; aile apne monitörü almak için kaygıyla '
                                             'arayışa girdi.',
                          'teaching_point': 'Solunum belirtisi olmayan bebekte grafi ve monitörizasyon gereksizdir; '
                                            'endişeyi artırır.'},
                         {'text': 'Komşuların önerisini değerlendirip aileye güvence vermek amacıyla muayeneyi hızlıca '
                                  'yapıp yalnızca tartıya bakmak, kilo alımı iyiyse sonraki aşı kontrolüne '
                                  'yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Tartı normal bulundu ancak kırmızı bayraklar sistematik sorgulanmadığı '
                                             'için aile tam güvence alamadı ve ertesi gün başka merkeze başvurdu.',
                          'teaching_point': 'Güvence ancak sistematik öykü ve muayeneyle verilebilir; kırmızı '
                                            'bayrakların yokluğu açıkça belgelenmelidir.'},
                         {'text': 'Kusmanın safralı veya fışkırır olup olmadığını, beslenme reddini ve solunum '
                                  'belirtilerini sorgulayıp büyüme eğrisi ve fontanel muayenesiyle kırmızı bayrakları '
                                  'aramak',
                          'is_correct': True,
                          'explanation': 'Kusan süt çocuğunda ilk görev fizyolojik tabloyu organik nedenlerden '
                                         'ayırmaktır. Safralı veya fışkırır kusma, kilo kaybı, beslenme reddi, '
                                         'fontanel bombeliği ve letarji gibi kırmızı bayraklar yoksa tablo büyük '
                                         'olasılıkla fizyolojiktir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 122/dk, SS 28/dk, SpO2 %100. Tartı 6.0 kg '
                                         '(doğum 3.2 kg; günlük ortalama 31 g artış, 50. persentil). Muayene masasında '
                                         'gülümsüyor. Fontanel düz, tonus normal. Akciğer sesleri doğal. Karın '
                                         'yumuşak, epigastrik kitle yok. Kusmalar safrasız, fışkırır değil.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Kırmızı bayrağı olmayan, düzenli kilo alan bu bebekte tetkik yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Elektrolit kaybını değerlendirmek amacıyla venöz kan gazı ve serum klor düzeyine '
                                  'bakmak, normalse ilaç başlamadan taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Kan gazı ve elektrolitler normal geldi; bebek kan alımı sırasında uzun '
                                             'süre ağladı.',
                          'teaching_point': 'Kilo alan, dehidratasyon bulgusu olmayan bebekte kan tetkiki gerekmez.'},
                         {'text': 'Tetkik istemeden aileye mekanizmayı anlatmak ve acilde bir beslenmeyi gözlemleyerek '
                                  'beslenme miktarını, sıklığını ve gaz çıkarma tekniğini değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Komplikasyonsuz tabloda tanı kliniktir. pH-impedans, endoskopi veya grafi '
                                         'önerilmez. Beslenme gözlemi aşırı besleme veya teknik sorunları ortaya '
                                         'koyabilir.',
                          'new_finding': 'Gözlenen emzirmede bebek etkin emdi; ardından gaz çıkarırken az miktarda süt '
                                         'çıkardı, rahatsızlık göstermedi. Annenin bebeği beslenme hemen sonrasında '
                                         'yatırdığı öğrenildi.'},
                         {'text': 'Mide çıkış yolu ve anatomiyi değerlendirmek için baryumlu üst gastrointestinal '
                                  'pasaj grafisi istemek ve sonuca göre ilaç kararı vermek',
                          'is_correct': False,
                          'scenario_update': 'Grafide işlem sırasında birkaç kez geri kaçış görüldü; bulgu yönetimi '
                                             'değiştirmedi ve bebek radyasyona maruz kaldı.',
                          'teaching_point': 'Kontrastlı grafi geri kaçışı tanımlamak için uygun değildir; yalnızca '
                                            'anatomik anomali şüphesinde kullanılır.'},
                         {'text': 'Süt alerjisini dışlamak için kan eozinofil sayısı ve inek sütü spesifik IgE '
                                  'istemek, sonuç gelene dek annenin süt ürünlerini kesmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Testler normal geldi; anne gereksiz diyet kısıtlaması nedeniyle yorgun '
                                             'düştü.',
                          'teaching_point': 'Kanlı dışkı, egzama veya kilo alamama yoksa alerji testi önerilmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Ağrısız, eforsuz beslenme sonrası kusmaları olan, gülümseyen ve düzenli kilo alan 3 aylık '
                         'bebekte tanı nedir?',
             'options': [{'text': 'İnfantil hipertrofik pilor stenozu',
                          'is_correct': False,
                          'scenario_update': 'Kusmalar fışkırır değil, bebek kilo alıyor ve epigastrik kitle yok.',
                          'teaching_point': 'Pilor stenozu fışkırır kusma, açlık ve kilo kaybıyla seyreder.'},
                         {'text': 'Gastroözofageal reflü hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Beslenme reddi, kilo alamama, irritabilite veya solunum komplikasyonu '
                                             'yok.',
                          'teaching_point': 'Hastalık tanımı ancak komplikasyon veya rahatsız edici semptomlar varsa '
                                            'kullanılır.'},
                         {'text': 'İnek sütü proteini alerjisi',
                          'is_correct': False,
                          'scenario_update': 'Egzama, kanlı dışkı ve beslenme güçlüğü yok.',
                          'teaching_point': 'Alerji tanısı için kusmaya eşlik eden ek bulgular aranmalıdır.'},
                         {'text': 'Fizyolojik gastroözofageal reflü',
                          'is_correct': True,
                          'explanation': 'Kilo alımı normal, kırmızı bayrağı olmayan ve kusarken rahatsızlık '
                                         'göstermeyen süt çocuğunda geri kaçış fizyolojiktir ve kendiliğinden düzelir.',
                          'new_finding': 'Tanı: Fizyolojik Gastroözofageal Reflü (komplikasyonsuz).'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu bebeğin ailesine yönelik en uygun plan hangisidir?',
             'options': [{'text': 'Emzirmeyi bırakıp geri kaçışı azaltan özel koyulaştırılmış formüle geçmek ve '
                                  'formülün etkisini iki hafta sonra değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Formüle geçişle emzirme sona erdi; geri kaçış yalnızca hafifçe azaldı.',
                          'teaching_point': 'Anne sütüyle beslenen bebekte fizyolojik geri kaçış emzirmeyi bırakmak '
                                            'için gerekçe değildir.'},
                         {'text': 'Tablonun normal olduğunu ve 1 yaş civarında geçeceğini anlatmak, aşırı beslemeden '
                                  'kaçınmayı ve beslenme sonrası dik tutmayı önermek, kırmızı bayrakları öğretmek',
                          'is_correct': True,
                          'explanation': 'Fizyolojik geri kaçışta temel yaklaşım güvence ve beslenme önerileridir. '
                                         'Emzirme sürdürülür, ilaç verilmez. Safralı-fışkırır kusma, kilo kaybı veya '
                                         'beslenme reddinde dönüş anlatılır.',
                          'new_finding': 'Aileye yazılı bilgi verildi. Bir ay sonraki kontrolde kusmalar azalmış, '
                                         'bebek düzenli kilo almaya devam ediyordu.'},
                         {'text': 'Mide asidini azaltmak için dört hafta oral omeprazol başlamak, beslenme sonrası dik '
                                  'tutmayı önermek ve ilaç bitiminde kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Kusma sıklığı değişmedi; bebek ikinci haftada akut gastroenterit ile '
                                             'başvurdu.',
                          'teaching_point': 'Fizyolojik tabloda asit baskılayıcılar etkisizdir ve enfeksiyon riskini '
                                            'artırabilir.'},
                         {'text': 'Kusmayı azaltmak için sağılmış anne sütüne pirinç unu ekleyerek koyulaştırmayı ve '
                                  'bebeği gece yüzüstü yatırmayı önerip iki hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Aile pirinç unuyla biberon kullanmaya başladı ve emzirme azaldı; yüzüstü '
                                             'yatış önerisi ani bebek ölümü riski taşıyordu.',
                          'teaching_point': 'Yüzüstü yatırma ani bebek ölümü sendromu riski nedeniyle önerilmez; anne '
                                            'sütüyle beslenen bebekte kıvam artırıcı rutin değildir.'}]}]},
 {'id': 'G50',
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
