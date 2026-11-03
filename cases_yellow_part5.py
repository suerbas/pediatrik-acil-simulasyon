# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Sarı Alan Vakaları (Part 5: Y41 - Y50)
Odak: Bulantı, Kusma, Karın Ağrısı, İshal (GİS Acilleri - Sarı Alan Monitörizasyon & Stabilizasyon)
Kılavuzlar: ESPGHAN, AAP, PALS, NASPGHAN, APSA (Pediatric Surgery)
"""

YELLOW_CASES_PART5 = [ { 'age': '9 Yaşında',
    'case_pearl': 'Pediatrik akut apandisitte ağrının periumbilikal bölgeden sağ alt kadrana migrasyonu ve '
                  'zıplama/sarsıntı hassasiyeti en değerli anamnez bulgularıdır. Çocuklarda ilk tercih edilecek '
                  "görüntüleme yöntemi USG'dir (>6 mm çap, komprese edilemeyen, aperistaltik kör uçlu tübüler yapı ve "
                  'apendikolit varlığı). Erken evrede analjezi verilmesi peritonit bulgularını maskelemez; aksine '
                  'hastanın rahat muayene edilmesini sağlar.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Dün göbek çevresinde başlayıp sağ alt kadrana yerleşen şiddetli karın ağrısı, bulantı ve iştahsızlık',
    'disposition': 'Sarı Alanda Damar Yolu + IV Sıvı + Analjezi + Çocuk Cerrahisi Konsültasyonu ile Erken Laparoskopik '
                   'Apendektomi İçin Yatış',
    'final_diagnosis': 'Akut Flegmonöz Apandisit (Non-perfore)',
    'gender': 'Erkek',
    'history': 'Ailesi 9 yaşındaki erkek çocuğu şiddetli karın ağrısı nedeniyle Sarı Alana getiriyor: Dün sabah göbek '
               'çevresinde künt bir sızı başlamış, akşam saatlerinde ağrı sağ alt kadrana kaymış ve adım attıkça bıçak '
               'saplanır gibi batmaya başlamış. İki kez safrasız kusmuş, iştahı tamamen kesilmiş. Arabayla hastaneye '
               'gelirken tümseklerden geçerken karnının sarsılmasıyla çığlık atarak ağlamış.',
    'id': 'Y41',
    'steps': [ { 'options': [ { 'explanation': 'Apandisit şüphesinde sağ alt kadran hassasiyeti (McBurney), istemsiz '
                                               'defans, Rovsing ve öksürük/zıplama testi periton tutulumunu gösteren '
                                               'en güvenilir fizik muayene basamaklarıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 38.3°C, KTA 118/dk, SS 22/dk, TA 106/66 mmHg, '
                                               'SpO2 %99. Genel durumu orta, hasta bacaklarını karnına çekerek '
                                               'yatıyor. Batın muayenesinde sağ alt kadranda belirgin hassasiyet, '
                                               'istemsiz defans, pozitif Rovsing belirtisi ve zıplama ağrısı mevcut; '
                                               'diğer kadranlar rahat.',
                                'text': 'Karın ağrısının periton irritasyonuna ilerleyip ilerlemediğini anlamak '
                                        'amacıyla McBurney hassasiyeti, defans ve zıplama ağrısını nazikçe '
                                        'değerlendirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Sert ve derin palpasyon çocuğun şiddetli ağrı ve panikle '
                                                   'kasılmasına yol açtı; batın muayenesi yapılamaz hale geldi.',
                                'teaching_point': 'Çocuklarda sert rebound testi travmatiktir ve istemsiz savunmayı '
                                                  'artırır; nazik perküsyon veya zıplama testi tercih edilmelidir.',
                                'text': 'Fizik muayeneyi derin palpasyonla başlatarak apendiksin perfore olup '
                                        'olmadığını anlamak için sertçe rebound testi uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Cerrahi ekip ayrıntılı fizik muayene ve bazal vital bulguları '
                                                   'belgelenmediği için hastayı tekrar servise yönlendirdi.',
                                'teaching_point': 'Her cerrahi kararı öncesinde sistemik muayene, vital bulgular ve '
                                                  'hemodinamik stabilite tam olarak değerlendirilmelidir.',
                                'text': 'Akut apandisit kliniği kesin olduğu için fizik muayene yapmadan hastayı '
                                        'derhal doğrudan acil ameliyathaneye devretmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Yüzüstü pozisyonda batın ön duvarına binen basınç periton '
                                                   'hassasiyetini şiddetlendirerek çocuğun kusmasını tetikledi.',
                                'teaching_point': 'Akut batın şüphesi olan çocuklar bacaklar hafif fleksiyonda '
                                                  'sırtüstü pozisyonda tutulmalı, batına ek bası uygulanmamalıdır.',
                                'text': 'Karın ağrısını hafifletmek amacıyla hastayı yüzüstü yatırarak derin '
                                        'palpasyonla retroperitoneal böbrek lojlarını kontrol etmek'}],
                 'question': 'Sağ alt kadranda lokalize karın ağrısı ve kusması olan bu çocukta ilk fizik muayene '
                             'yaklaşımınız ne olmalıdır?',
                 'stage_title': 'Sarı Alanda İlk Değerlendirme ve Batın Muayenesi'},
               { 'options': [ { 'explanation': 'Pediatrik yaş grubunda apandisit tanısında ilk basamak görüntüleme '
                                               "radyasyon içermeyen batın USG'sidir. Lökositoz ve CRP yüksekliği "
                                               'klinik tanıyı güçlendirir.',
                                'image': 'assets/images/usg_appendicitis.png',
                                'is_correct': True,
                                'new_finding': 'Laboratuvar: Lökosit 15.600/mm³ (%84 nötrofil), CRP 46 mg/L, TİT '
                                               'normal. Batın USG: Sağ alt kadranda kör sonlanan, komprese edilemeyen, '
                                               'transvers çapı 8.4 mm ölçülen kalınlaşmış aperistaltik tübüler '
                                               'apendiks ve lümen içinde apendikolit izlendi.',
                                'text': 'Enfeksiyon belirteçlerini görmek için tam kan ve CRP tetkiki ile radyasyonsuz '
                                        'ilk seçenek olarak acil batın ultrasonografisi istemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Ultrason denenmeden çekilen tomografi çocuğu yüksek doz iyonizan '
                                                   'radyasyona maruz bıraktı; tanı kılavuzlarına aykırı bulundu.',
                                'teaching_point': "Çocuklarda apandisit şüphesinde ilk basamak görüntüleme USG'dir; BT "
                                                  "yalnızca USG'nin yetersiz veya şüpheli kaldığı durumlarda "
                                                  'seçilmelidir.',
                                'text': 'Radyolojik görüntüleme yapmadan önce kesin tanı amacıyla doğrudan kontrastlı '
                                        'tüm batın bilgisayarlı tomografisi çektirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Direkt grafide yalnızca sağ alt kadranda non-spesifik gaz azlığı '
                                                   'izlendi; apandisit tanısını doğrulayamadı veya dışlayamadı.',
                                'teaching_point': 'Ayakta direkt batın grafisi apandisit tanısında duyarsızdır; '
                                                  'yalnızca perforasyon (serbest hava) veya ileus şüphesinde '
                                                  'yardımcıdır.',
                                'text': 'Tanıyı radyolojik olarak dışlamak amacıyla sadece ayakta direkt batın grafisi '
                                        'çekip gaz dağılımına göre taburculuk planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Evde izleme kararı sonrası çocuğun ağrısı arttı ve 12 saat sonra '
                                                   'apendiks perforasyonu ve yaygın peritonitle acile döndü.',
                                'teaching_point': 'Sağ alt kadran peritonit bulguları olan çocuk tetkik ve cerrahi '
                                                  'değerlendirme yapılmadan kesinlikle taburcu edilmemelidir.',
                                'text': 'Hiçbir tetkik ve görüntüleme istemeden sadece oral parasetamol verip çocuğu '
                                        'evde izlenmek üzere Yeşil Alana geri göndermek'}],
                 'question': 'Muayenede peritonit bulgusu veren bu hastada tanıyı netleştirmek için en uygun tetkik ve '
                             'görüntüleme kombinasyonu hangisidir?',
                 'stage_title': 'Laboratuvar Tetkikleri ve İleri Görüntüleme'},
               { 'options': [ { 'explanation': "Sağ alt kadrana göç eden ağrı, lokal defans, lökositoz ve USG'de >6 mm "
                                               'çaplı aperistaltik non-komprese tübüler yapı akut apandisiti '
                                               'kesinleştirir.',
                                'is_correct': True,
                                'new_finding': 'Klinik ve ultrasonografik tanı: Akut Non-perfore Flegmonöz Apandisit.',
                                'text': 'Akut non-perfore flegmonöz apandisit'},
                              { 'is_correct': False,
                                'scenario_update': 'Mezenterik lenfadenitte apendiks çapı normaldir ve çok sayıda '
                                                   'büyümüş lenf nodu izlenir; bu hastada apendiks lümeni 8.4 mm ve '
                                                   'apendikolitli bulundu.',
                                'teaching_point': "Mezenterik lenfadenit apandisiti taklit eder ancak USG'de "
                                                  'apendiksin kalınlaşması ve aperistaltik olması apandisite özgüdür.',
                                'text': 'Akut mezenterik lenfadenit tablosu'},
                              { 'is_correct': False,
                                'scenario_update': "TİT tamamen temiz geldi ve USG'de böbrekler ve mesane doğal "
                                                   'izlendi; tabloyu açıklamadı.',
                                'teaching_point': 'İdrar yolu enfeksiyonu sağ alt kadran kitle etkisi ve aperistaltik '
                                                  'apendiks bulgusu yapmaz.',
                                'text': 'Komplike idrar yolu enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Primer peritonit genellikle asiti olan nefrotik veya sirotik '
                                                   'hastalarda görülür; lokalize apandisit kliniğiyle uyumsuzdur.',
                                'teaching_point': 'Sağlıklı çocukta fokal peritonit hemen her zaman apandisit gibi '
                                                  'cerrahi bir odağa sekonderdir.',
                                'text': 'Primer bakteriyel peritonit enfeksiyonu'}],
                 'question': 'Mevcut anamnez, fizik muayene ve ultrasonografi bulgularıyla bu hastada en olası klinik '
                             'tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Akut apandisitte hasta aç bırakılmalı (NPO), dehidratasyon izotonik '
                                               'kristaloid ile düzeltilmeli, intravenöz analjezi '
                                               '(parasetamol/tramadol) verilmeli ve acil apendektomi için çocuk '
                                               'cerrahisine devredilmelidir.',
                                'is_correct': True,
                                'new_finding': 'Hasta oral alıma kapatıldı. IV hidrasyon ve analjezi uygulandı. Çocuk '
                                               'cerrahisi tarafından değerlendirilerek erken laparoskopik apendektomi '
                                               'planıyla servise yatışı yapıldı.',
                                'text': 'Oral alımı derhal durdurup damar yolu açarak izotonik sıvı infüzyonu, '
                                        'analjezi başlamak ve acil çocuk cerrahisi konsültasyonu istemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Laksatif verilmesi apendiks içi basıncı artırarak lümenin '
                                                   'delinmesine ve fekal peritonit gelişmesine neden oldu.',
                                'teaching_point': 'Akut apandisitte laksatif veya lavman uygulanması perforasyon '
                                                  'riskini dramatik şekilde artırır; KONTRENDİKEDİR.',
                                'text': 'Cerrahiye gerek kalmadan tabloyu yatıştırmak amacıyla hastaya oral '
                                        'antibiyotik şurup ve laksatif verip evine göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Ağrısı kesilmeyen çocuk şiddetli ajitasyon ve taşikardiye girdi, '
                                                   'preoperatif anksiyetesi dayanılmaz hale geldi.',
                                'teaching_point': 'Güncel kılavuzlara göre analjezi verilmesi apandisit muayenesini '
                                                  'maskelemez; çocuğun ağrısını dindirmek insani ve tıbbi bir '
                                                  'zorunluluktur.',
                                'text': 'Karın ağrısı tanısını cerraha göstermeden maskelememek için ameliyat masasına '
                                        'kadar hiçbir analjezik ilaç uygulamamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Oral beslenen çocuk genel anestezi indüksiyonunda yüksek '
                                                   'aspirasyon riski taşıdığı için cerrahiye alınması gecikti.',
                                'teaching_point': 'Cerrahi planlanan akut batın olgularında anestezi güvenliği için '
                                                  'hasta mutlak oral stop (NPO) tutulmalıdır.',
                                'text': 'Ağızdan berrak sıvılarla beslenmeye devam ederek acil serviste 48 saat '
                                        'boyunca aralıksız antibiyotik infüzyonu uygulamak'}],
                 'question': 'Akut apandisit tanısı kesinleşen bu hastada Sarı Alanda uygulanacak en uygun tedavi ve '
                             'konsültasyon adımı hangisidir?',
                 'stage_title': 'Nihai Tedavi, Konsültasyon ve Preoperatif Hazırlık'}]},
  { 'age': '8 Aylık',
    'case_pearl': 'İnvajinasyon 3 ay - 3 yaş arası çocuklarda en sık bağırsak obstrüksiyonu nedenidir. Klasik triyad '
                  '(aralıklı kramp tarzı karın ağrısı, palpabl abdominal sosis kitle, çilek jölesi gaita) olguların '
                  'sadece üçte birinde tam bulunur. Ağrı nöbetleri arasındaki uyuşukluk/letarji sepsisle karışabilir. '
                  "Tanıda batın USG altın standarttır (%100'e yakın duyarlılık; hedef tahtası / donut işareti veya "
                  'psödoböbrek görünümü). Peritonit ve perforasyon yoksa ilk tedavi cerrahi değil, floroskopi veya USG '
                  'eşliğinde pnömatik (hava) veya hidrostatik (serum fizyolojik) redüksiyondur.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Aralıklı bacaklarını karnına çekerek ağlama nöbetleri, safralı kusma ve bezinde çilek jölesi benzeri '
                 'kanlı dışkı',
    'disposition': 'Sarı Alanda Damar Yolu + IV Sıvı Resüsitasyonu + USG Eşliğinde Pnömatik/Hidrostatik Redüksiyon + '
                   'Yatış',
    'final_diagnosis': 'İleokolik İnvajinasyon (İntussusepsiyon)',
    'gender': 'Erkek',
    'history': 'Sekiz aylık daha önce sağlıklı erkek bebek ailesi tarafından Sarı Alana getiriliyor: Sabah aniden '
               'başlayan, 15-20 dakika aralıklarla bacaklarını karnına toplayıp tiz çığlıklarla ağlama atakları olmuş. '
               'Ataklar arasında çocuk bitkin ve uykuya meyilli görünüyor. İki kez yeşil safralı kusmuş ve son bezinde '
               'parlak kırmızı, jelatinöz çilek jölesini andıran kanlı mukuslu dışkı fark edilmiş.',
    'id': 'Y42',
    'steps': [ { 'options': [ { 'explanation': 'İnvajinasyonda sağ üst kadranda sosis kitle, sağ alt kadranda boşluk '
                                               '(Dance belirtisi) ve rektal tuşede çilek jölesi gaita aranmalı, '
                                               'hemodinamik durum değerlendirilmelidir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.4°C, KTA 144/dk, SS 32/dk, TA 88/54 mmHg, SpO2 '
                                               '%98, KDZ 2.5 sn. Bebek ataksız dönemde letarjik duruyor. Batın '
                                               'muayenesinde sağ hipokondriyumda transvers yerleşimli düzgün sınırlı '
                                               'sosis benzeri kitle palpe edildi; sağ alt kadranda boşluk hissi '
                                               'mevcut. Rektal tuşede çilek jölesi gaita bulaştı.',
                                'text': 'Bilinç durumu, perfüzyon, batında palpabl sosis kitle ve rektal tuşede kanlı '
                                        'mukus varlığını sistemik olarak incelemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Emzirilen bebek yeşil safralı mayiyi aspire etme tehlikesi geçirdi '
                                                   've karın ağrısı daha da şiddetlendi.',
                                'teaching_point': 'Sekiz aylık bir bebekte safralı kusma ve rektal kanama asla kolik '
                                                  'olamaz; derhal cerrahi aciller araştırılmalıdır.',
                                'text': 'Bebek aralıklı ağladığı için basit infantil kolik düşünerek annesine bebeği '
                                        'kucağında sallayıp emzirmesini önermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Antibiyotik başlanması bağırsak peristaltizmini etkileyerek '
                                                   'invajine segmentin gangren riskini artırdı.',
                                'teaching_point': 'Aralıklı şiddetli ağrı ve safralı kusma mekanik obstrüksiyona '
                                                  'işaret eder; dizanteri ampirik antibiyotiğiyle zaman kaybedilemez.',
                                'text': 'Kanlı dışkı nedeniyle invaziv bakteriyel dizanteri kabul edip fizik muayene '
                                        'yapmadan oral sefiksim tedavisi başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Antispazmodik enjeksiyonu bebeğin letarjisini derinleştirdi ve '
                                                   'bağırsak dolaşım bozukluğunun fark edilmesini geciktirdi.',
                                'teaching_point': 'Mekanik obstrüksiyon ve invajinasyonda antispazmodikler bağırsak '
                                                  'perforasyonu ve iskemi riskini artırır; KONTRENDİKEDİR.',
                                'text': 'Karın ağrısının barsak spazmına bağlı olduğunu varsayıp intramüsküler '
                                        'antispazmodik enjeksiyonu yaparak hastayı gözleme almak'}],
                 'question': 'Aralıklı ağlama atakları ve safralı kusması olan bu bebekte Sarı Alanda ilk yapılması '
                             'gereken klinik değerlendirme hangisidir?',
                 'stage_title': 'Sarı Alanda İlk Değerlendirme ve Hemodinamik Yaklaşım'},
               { 'options': [ { 'explanation': 'Batın USG invajinasyon tanısında altın standarttır. Transvers kesitte '
                                               'iç içe geçmiş konsantrik halkalar (target / donut), longitudinal '
                                               'kesitte psödoböbrek görünümü verir.',
                                'image': 'assets/images/usg_intussusception.png',
                                'is_correct': True,
                                'new_finding': 'Batın USG: Sağ subhepatik alanda transvers planda iç içe geçmiş '
                                               'bağırsak segmentlerine ait konsantrik hipo/hiperekojen halkalar (hedef '
                                               'tahtası / donut işareti) ve longitudinal planda psödoböbrek görünümü '
                                               'izlendi. Serbest hava veya nekroz saptanmadı.',
                                'text': 'Radyasyon riski içermeyen ve tanısal duyarlılığı yüzde yüze yakın olan acil '
                                        'batın ultrasonografisi çekilmesini planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Görüntüleme yapılmadan cerrahiye alınması ameliyatsız non-operatif '
                                                   'redüksiyon şansını tamamen yok etti.',
                                'teaching_point': 'Peritonit ve perforasyon yoksa invajinasyonda ilk tedavi ameliyat '
                                                  'değil, non-operatif radyolojik redüksiyondur.',
                                'text': 'Kesin tanı için radyolojiyi atlayıp çocuğu derhal genel anestezi altında acil '
                                        'açık tanısal laparotomiye almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Oral baryum aspirasyona yol açtı ve olası cerrahi girişim öncesi '
                                                   'batın içini baryumla kontamine etti.',
                                'teaching_point': 'İnvajinasyonda oral kontrast verilmesi kontrendikedir; redüksiyon '
                                                  'retrograd yolla (rektal) yapılmalıdır.',
                                'text': 'Bağırsak lümenini görmek amacıyla hastaya oral baryum içirerek seri üst '
                                        'gastrointestinal geçiş grafileri çektirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Akciğer grafisi normal sınırlarda geldi ancak karındaki mekanik '
                                                   'obstrüksiyon hakkında hiçbir bilgi vermedi.',
                                'teaching_point': 'Akut batın ve safralı kusma tablosunda akciğer grafisi primer '
                                                  'tanısal yöntem olamaz; batın USG şarttır.',
                                'text': 'Tanıyı radyolojik olarak dışlamak için yalnızca iki yönlü akciğer grafisi '
                                        'çekip kardiyotorasik indeksi hesaplamak'}],
                 'question': 'Klinik muayenede invajinasyon şüphesi güçlenen bu stabil bebekte öncelikli tanısal '
                             'görüntüleme yöntemi hangisi olmalıdır?',
                 'stage_title': 'Radyolojik Görüntüleme ve Girişim Kararı'},
               { 'options': [ { 'explanation': "Aralıklı kolik ağrılar, safralı kusma, çilek jölesi gaita ve USG'de "
                                               'hedef tahtası (donut) işareti ileokolik invajinasyonun kesin '
                                               'tanısıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: İleokolik İnvajinasyon (İntussusepsiyon).',
                                'text': 'İleokolik invajinasyon tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Bakteriyel dizanteride aralıklı nöbetler, sosis şeklinde batın '
                                                   "kitlesi ve USG'de donut halkaları görülmez.",
                                'teaching_point': 'Dizanteri diffüz mukozal inflamasyondur; segmental invajinasyon '
                                                  'kitlesi ve safralı kusma yapmaz.',
                                'text': 'Akut bakteriyel dizanteri koliti'},
                              { 'is_correct': False,
                                'scenario_update': 'Meckel kanaması tipik olarak ağrısızdır; bu hastadaki şiddetli '
                                                   'aralıklı kolik atakları ve safralı kusmayı açıklamaz.',
                                'teaching_point': 'Meckel divertikülü ağrısız masif rektal kanama ile gelir; '
                                                  'invajinasyonda ise şiddetli kolik ağrı ön plandadır.',
                                'text': 'Ağrısız Meckel divertikülü kanaması'},
                              { 'is_correct': False,
                                'scenario_update': 'Nekrotizan enterokolit erken prematüre yenidoğanlarda pnömatozis '
                                                   'ile seyreder; 8 aylık sağlıklı term bebekte beklenmez.',
                                'teaching_point': 'NEK bir erken yenidoğan hastalığıdır; süt çocukluğu döneminde '
                                                  'invajinasyonla karıştırılmamalıdır.',
                                'text': 'Nekrotizan enterokolit perforasyonu'}],
                 'question': "Aralıklı kolik ağrı, palpabl sosis kitle ve USG'de hedef tahtası bulgusu olan bu bebekte "
                             'kesin klinik tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Perforasyon veya peritonit bulgusu olmayan invajinasyonda ilk tercih '
                                               'pnömatik (hava) veya hidrostatik (serum fizyolojik) redüksiyondur; '
                                               "başarı oranı %80-90'ın üzerindedir. Başarısızlık durumunda acil "
                                               'cerrahiye geçilir.',
                                'is_correct': True,
                                'new_finding': 'USG eşliğinde ılık SF ile hidrostatik redüksiyon uygulandı. İleum '
                                               'anslarının çekumdan çıktığı ve sıvının terminal ileuma serbestçe '
                                               'dolduğu görüldü (tam redüksiyon). Bebeğin ağrısı geçti, rahatlayıp '
                                               'uykuya daldı; 24 saat gözlem için yatırıldı.',
                                'text': 'Çocuk cerrahisi hazır bulunurken ultrason veya floroskopi rehberliğinde '
                                        'pnömatik ya da hidrostatik redüksiyon uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz cerrahi insizyon ve laparatomiye maruz kalan bebekte '
                                                   'adezyon ve cerrahi komplikasyon riski oluştu.',
                                'teaching_point': 'Stabil ve perforasyonu olmayan invajinasyon vakalarında ameliyatsız '
                                                  'redüksiyon ilk standart tedavi yöntemidir.',
                                'text': 'Non-operatif redüksiyon yöntemlerini hiç denemeden bebeği derhal genel '
                                        'anestezi altında açık rezeksiyon cerrahisine almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Müdahale edilmeyen invajine segmentte 6 saat sonra venöz '
                                                   'tıkanıklık, bağırsak nekrozu ve perforasyon gelişti.',
                                'teaching_point': 'İnvajinasyon aktif redüksiyon gerektiren acil bir tablodur; spontan '
                                                  'açılma beklenerek zaman kaybedilemez.',
                                'text': 'Redüksiyon işlemi yapmadan bebeği sadece damardan mayi vererek kendi kendine '
                                        'açılması için serviste takip etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Oral laksatif verilmesi tıkanıklığın proksimalindeki basıncı aşırı '
                                                   'artırarak bağırsak yırtılmasına yol açtı.',
                                'teaching_point': 'Mekanik obstrüksiyonu olan hastaya oral laksatif verilmesi bağırsak '
                                                  'perforasyonuna neden olabilen ölümcül bir hatadır.',
                                'text': 'Bebeğe oral yoldan yüksek doz laksatif solüsyon içirerek bağırsağın kitleyi '
                                        'ileri itmesini sağlamaya çalışmak'}],
                 'question': 'Peritonit veya perforasyon bulgusu olmayan, hemodinamik olarak stabilize edilen bu '
                             'bebekte ilk tedavi yaklaşımı ne olmalıdır?',
                 'stage_title': 'Tedavi Yöntemi, Redüksiyon ve Gözlem'}]},
  { 'age': '5 Haftalık',
    'case_pearl': 'İnfantil hipertrofik pilor stenozu 3-6 haftalık ilk doğan erkek bebeklerde sıktır. Kusma '
                  'safrasızdır çünkü darlık ampulla Vaterinin proksimalindedir. Sürekli gastrik asit (HCl) kaybı '
                  "patognomonik hipokloremik, hipokalemik metabolik alkaloza yol açar. Pilor USG'sinde pilor kas "
                  'kalınlığı ≥3 mm veya kanal uzunluğu ≥14-15 mm tanı koydurur. Pilor stenozu cerrahi bir acil değil, '
                  'TIBBİ BİR METABOLİK ACİLDİR! Bebek elektrolitleri (klor >100 mEq/L, potasyum normal) ve alkalozu '
                  '(bikarbonat <30 mmol/L) düzeltilmeden kesinlikle ameliyata verilemez; aksi takdirde postoperatif '
                  'santral apne riski gelişir.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Her beslenme sonrasında fışkırır tarzda safrasız kusma, sürekli açlık hali ve kilo alamama',
    'disposition': 'Sarı Alanda Damar Yolu + Nazogastrik Dekompresyon + Elektrolit/Alkaloz Düzeltilmesi Sonrası '
                   'Elektif Piloromiyotomi',
    'final_diagnosis': 'İnfantil Hipertrofik Pilor Stenozu',
    'gender': 'Erkek',
    'history': 'İlk çocuk olan 5 haftalık erkek bebek annesi tarafından Sarı Alana getiriliyor: Yaklaşık 10 gündür '
               'emdikten hemen sonra tüm sütü bir metre ileri fışkırtarak kusuyor. Kusmukta kesinlikle yeşil safra '
               'yok, sadece ekşimiş süt geliyor. Bebek kustuktan hemen sonra tekrar iştahla emmek istiyor. Son bir '
               'haftadır bezi belirgin hafiflemiş, idrar sıklığı azalmış ve tartısı düşmüş.',
    'id': 'Y43',
    'steps': [ { 'options': [ { 'explanation': 'Pilor stenozunda soldan sağa ilerleyen epigastrik peristaltik dalgalar '
                                               've sağ üst kadranda sert, hareketli zeytin büyüklüğünde kitle (oliva) '
                                               'muayenenin en karakteristik bulgularıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 152/dk, SS 34/dk, TA 82/48 mmHg, SpO2 '
                                               '%99, KDZ 3 sn. Ön fontanel çökük, mukozalar kuru, deri turgoru '
                                               'azalmış. Epigastriumda peristaltik dalgalar izlendi ve sağ rektus '
                                               'kenarında derin palpasyonda hareketli, sert, zeytin benzeri (oliva) '
                                               'kitle palpe edildi.',
                                'text': 'Dehidratasyon derecesini saptamak, epigastrik peristaltik dalgaları ve zeytin '
                                        'büyüklüğündeki kitleyi değerlendirmek için nazik batın muayenesi yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tomografi normal geldi ancak 5 haftalık bebek gereksiz yere yüksek '
                                                   'doz kraniyal radyasyona maruz kaldı.',
                                'teaching_point': 'Beslenme sonrası fışkırır safrasız kusan ve sürekli aç olan süt '
                                                  'çocuğunda öncelik GİS obstrüksiyonudur; KİBAS değil.',
                                'text': 'Kusmanın nörolojik kafa içi basınç artışına bağlı olduğunu varsayıp derhal '
                                        'acil beyin tomografisi çektirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'İçirilen mama anında masif şekilde fışkırarak kusuldu ve bebeğin '
                                                   'hava yoluna aspire olma tehlikesi yaşandı.',
                                'teaching_point': 'Mide çıkış obstrüksiyonu şüphesi olan bebeklere oral besin '
                                                  'verilmesi aspirasyon riski nedeniyle KONTRENDİKEDİR.',
                                'text': 'Kusan bebeği tok karnına derinlemesine muayene etmek amacıyla acil serviste '
                                        'bol miktarda formül mama içirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gaz damlası verilen bebek evde dehidratasyona girdi ve 2 gün sonra '
                                                   'hipovolemik şok tablosunda Sarı Alana döndü.',
                                'teaching_point': 'Fışkırır tarzda kusma ve kilo kaybı olan bebekte metabolik ve '
                                                  'cerrahi aciller dışlanmadan taburculuk yapılamaz.',
                                'text': 'Bebekte ateş olmadığı için hiçbir muayene yapmadan reçeteye oral gaz giderici '
                                        'damla yazıp Yeşil Alana yönlendirmek'}],
                 'question': 'Fışkırır tarzda safrasız kusması olan 5 haftalık bu bebekte ilk fizik muayene '
                             'yaklaşımınız ne olmalıdır?',
                 'stage_title': 'Sarı Alanda İlk Değerlendirme ve Dehidratasyon Muayenesi'},
               { 'options': [ { 'explanation': 'Sürekli asit kaybı hipokloremik, hipokalemik metabolik alkaloza yol '
                                               "açar. Batın USG'de pilor kas kalınlığı ≥3 mm ve kanal uzunluğu ≥14 mm "
                                               'olması altın standart tanı yöntemidir.',
                                'image': 'assets/images/usg_pyloric_stenosis.png',
                                'is_correct': True,
                                'new_finding': 'Kan Gazı ve Biyokimya: pH 7.54, pCO2 48 mmHg, HCO3 36 mmol/L, K 3.1 '
                                               'mEq/L, Cl 86 mEq/L (hipokloremik hipokalemik metabolik alkaloz), BUN '
                                               '36 mg/dL. Batın USG: Pilorik kas kalınlığı 4.3 mm (normal <3 mm), '
                                               'pilor kanal uzunluğu 17 mm (normal <14 mm), mide çıkışı tam obstrükte.',
                                'text': 'Venöz kan gazı, serum elektrolitleri istemek ve pilor kas anatomisini '
                                        'netleştirmek amacıyla acil batın ultrasonografisi yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'İdrar kültürü beklenirken bebeğin dehidratasyonu ve metabolik '
                                                   'alkalozu derinleşti, tanı konulamadı.',
                                'teaching_point': 'İdrar yolu enfeksiyonu fışkırır kusma ve oliva kitlesi yapmaz; '
                                                  'elektrolitler ve USG önceliklidir.',
                                'text': 'Radyolojik inceleme yapmadan sadece idrar yolu enfeksiyonunu dışlamak '
                                        'amacıyla idrar kültürü alıp beklemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Baryum mide çıkışında tıkandı, bebek kustu ve kimyasal baryum '
                                                   'pnömonisi komplikasyonu gelişti.',
                                'teaching_point': 'USG varken baryumlu pasaj grafisine gerek yoktur; obstrüksiyon '
                                                  'varlığında baryum aspirasyonu öldürücüdür.',
                                'text': 'Pilor kanalını görmek amacıyla bebeğe yüksek hacimli oral baryum içirerek '
                                        'seri pasaj grafileri çekmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Ağır metabolik alkaloz ve hipokalemisi olan bebek anestezi '
                                                   'indüksiyonunda uzamış apneye girdi.',
                                'teaching_point': 'Alkaloz ve elektrolit bozukluğu düzeltilmeden sedasyon veya '
                                                  'anestezi verilmesi santral apne riskini katlar.',
                                'text': 'Elektrolit bakmadan bebeğe derhal genel anestezi altında acil tanısal '
                                        'özofagogastroduodenoskopi yapmak'}],
                 'question': 'Pilor stenozu şüphesi olan bu dehidrate bebekte yapılması gereken öncelikli laboratuvar '
                             've görüntüleme incelemesi hangisidir?',
                 'stage_title': 'Biyokimyasal Analiz ve Ultrasonografi İncelemesi'},
               { 'options': [ { 'explanation': 'Beslenme sonrası safrasız fışkırır kusma, hipokloremik hipokalemik '
                                               "metabolik alkaloz ve USG'de pilor kas kalınlığının >3 mm olması "
                                               'tabloyu kesinleştirir.',
                                'is_correct': True,
                                'new_finding': 'Klinik ve Ultrasonografik Tanı: İnfantil Hipertrofik Pilor Stenozu.',
                                'text': 'İnfantil hipertrofik pilor stenozu'},
                              { 'is_correct': False,
                                'scenario_update': 'Fizyolojik reflüde fışkırır kusma, metabolik alkaloz, kilo kaybı '
                                                   've pilor kas kalınlaşması görülmez.',
                                'teaching_point': 'Reflüde bebek huzurludur, kilo alımı normaldir ve asla hipokloremik '
                                                  'alkaloz gelişmez.',
                                'text': 'Fizyolojik gastroözofageal reflü tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Duodenal atrezi hayatın ilk gününde safralı kusma ve direkt '
                                                   'grafide çift hava kabarcığı (double-bubble) ile prezante olur.',
                                'teaching_point': 'Duodenal atrezide kusma safralıdır ve yenidoğan ilk gününde semptom '
                                                  'verir; 5 haftalık gecikmiş başlangıç olmaz.',
                                'text': 'Duodenal atrezi anomalisi'},
                              { 'is_correct': False,
                                'scenario_update': 'KAH krizinde kusma ve dehidratasyona hiponatremi, hiperkalemi ve '
                                                   'metabolik ASİDOZ eşlik eder; alkaloz değil.',
                                'teaching_point': 'KAH krizinde potasyum yüksek, asidoz vardır; pilor stenozunda ise '
                                                  'potasyum düşük, ALKALOZ vardır.',
                                'text': 'Konjenital adrenal hiperplazi krizi'}],
                 'question': 'Fışkırır safrasız kusma, oliva kitlesi, hipokloremik metabolik alkaloz ve USG bulguları '
                             'ile en olası klinik tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Pilor stenozu elektif bir cerrahidir. Ameliyat öncesinde hipokloremik '
                                               'metabolik alkaloz %0.9 NaCl + 20-30 mEq/L KCl ile mutlaka '
                                               'düzeltilmelidir (Klor >100 mEq/L, HCO3 <30 mmol/L). Aksi takdirde '
                                               'postoperatif hipoventilasyon ve apne gelişir.',
                                'is_correct': True,
                                'new_finding': 'Oral alım kesildi, NG sonda ile mide dekomprese edildi. Potasyumlu SF '
                                               'infüzyonu ile 24 saatte klor 104 mEq/L, potasyum 4.0 mEq/L, HCO3 24 '
                                               'mmol/L düzeyine getirildi. Elektrolit dengesi sağlandıktan sonra '
                                               'güvenle laparoskopik piloromiyotomiye alındı.',
                                'text': 'Oral alımı durdurup nazogastrik dekompresyon sağlamak ve potasyumlu izotonik '
                                        'mayi ile metabolik alkalozu ve klor açığını tamamen düzeltmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Alkalozu düzeltilmeden ameliyata alınan bebek ekstübe edildikten '
                                                   'sonra santral solunum durması (apne) yaşadı.',
                                'teaching_point': 'Pilor stenozu cerrahi acil değildir; metabolik dengesizlik '
                                                  'düzeltilmeden ameliyata verilmesi ölümcül solunum depresyonuna yol '
                                                  'açar.',
                                'text': 'Metabolik bozukluğu önemsemeyerek zaman kaybetmemek adına bebeği derhal yarım '
                                        'saat içinde acil ameliyathaneye indirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Elektrolitsiz saf su infüzyonu masif hemolize ve akut beyin ödemi '
                                                   'nöbetine yol açtı.',
                                'teaching_point': 'Saf su asla damardan verilemez; sıvı resüsitasyonunda mutlaka '
                                                  'izotonik kristaloid solüsyonlar kullanılmalıdır.',
                                'text': 'Hipokloremiyi düzeltmek için bebeğe damardan saf su infüzyonu yaparak sodyum '
                                        've bikarbonat düzeylerini hızla seyreltmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Mekanik tıkanıklık devam ettiği için bebek verilen tüm mamaları '
                                                   'kustu ve derin dehidratasyon gelişti.',
                                'teaching_point': 'Pilor stenozu mekanik bir hipertrofidir; kesin tedavisi cerrahi '
                                                  'piloromiyotomidir, medikal tedaviyle düzelmez.',
                                'text': 'Ameliyattan vazgeçip bebeğe sadece oral PPI şurup ve koyulaştırılmış mama '
                                        'başlayarak evine göndermek'}],
                 'question': 'Pilor stenozu tanısı konulan bu bebekte çocuk cerrahisine verilmeden önce Sarı Alanda '
                             'uygulanacak en kritik tıbbi adım hangisidir?',
                 'stage_title': 'Metabolik Resüsitasyon ve Preoperatif Yaklaşım'}]},
  { 'age': '14 Aylık',
    'case_pearl': 'Akut gastroenteritte ağır dehidratasyon (ağırlık kaybı >%9-10) hipovolemik şok öncesi kritik bir '
                  'acildir. Letarji, çökük göz küreleri, kuru mukozalar, uzamış KDZ (>3 sn) ve deri kıvrımının 2 '
                  'saniyeden geç düzelmesi temel bulgulardır. Ağır dehidratasyon veya inatçı kusmada oral hidrasyon '
                  '(ORS) denenmez, vakit kaybedilmeden 20 mL/kg izotonik kristaloid (%0.9 NaCl veya Ringer Laktat) '
                  '15-30 dakikada IV bolus verilmelidir. Hipotonik sıvılar şok resüsitasyonunda ASLA kullanılmaz.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Günde 12 kez sulu ishal, ağızdan verilen hiçbir şeyi tutamayan kusma, uykuya meyil ve idrar yapamama',
    'disposition': 'Sarı Alanda Acil Damar Yolu + 20 mL/kg İzotonik Kristaloid Bolusu + Elektrolit Takibi ile Gözlem '
                   'Yatışı',
    'final_diagnosis': 'Ağır Dehidratasyonlu Akut Gastroenterit (Hipovolemik Şok Öncesi Evre)',
    'gender': 'Kız',
    'history': 'On dört aylık kız çocuğu ailesi tarafından Sarı Alana getiriliyor: İki gündür aralıksız sulu ishal ve '
               'bugün sabah başlayan inatçı kusması var. Anne ağızdan bir kaşık su bile verse anında fışkırtarak '
               'çıkarıyor. Son 12 saattir bezi tamamen kuru kalmış, hiç idrar yapmamış. Çocuk muayene masasında '
               'sürekli uyukluyor, ağlarken hiç gözyaşı akmıyor ve çevreye ilgisi belirgin azalmış.',
    'id': 'Y44',
    'steps': [ { 'options': [ { 'explanation': 'Ağır dehidrate ve letarjik çocukta hipovolemik şok riski nedeniyle '
                                               'acil vasküler erişim ve perfüzyon değerlendirmesi birinci önceliktir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 38.2°C, KTA 168/dk (belirgin taşikardi), SS '
                                               '38/dk, TA 78/46 mmHg (hipotansif eğilimli), SpO2 %97, KDZ 4 saniye, '
                                               'periferik nabızlar filiform. Çocuk letarjik, göz küreleri derinden '
                                               'çökmüş, ağız mukozası kupkuru, karın derisi sıkıldığında kıvrım 3 '
                                               'saniyede düzeliyor. Batın rahat, organomegali yok.',
                                'text': 'Bilinç düzeyi, kapiller dolum zamanı, periferik nabızlar ve vital bulguları '
                                        'inceleyerek derhal intravenöz damar yolu açmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Ağızdan verilen sıvıyı anında kusan letarjik bebek aspire etti; '
                                                   'öksürük ve solunum sıkıntısı gelişti.',
                                'teaching_point': 'Letarjik, şok sınırındaki ağır dehidrate çocuklarda oral hidrasyon '
                                                  'kontrendikedir; aspirasyona yol açar.',
                                'text': 'Kusmayı durdurmak için ağızdan bol şekerli su içirip çocuğu Yeşil Alan '
                                        'bekleme salonuna göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Sıvı resüsitasyonu geciktirilen çocukta kan basıncı 60/35 mmHg '
                                                   'düzeyine geriledi ve dekompanse şok tablosu oturdu.',
                                'teaching_point': 'Şok bulguları olan çocukta sıvı resüsitasyonu için idrar beklenmez; '
                                                  'gecikme kardiyovasküler kollapsa neden olur.',
                                'text': 'Dehidratasyon derecesini netleştirmek için sıvı vermeden önce hastayı iki '
                                        'saat idrar çıkışı açısından bekletmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Hipovolemik hastaya verilen sedatif kardiyak arreste zemin '
                                                   'hazırladı ve acil resüsitasyon gerekti.',
                                'teaching_point': 'Hipovolemisi ve doku hipoperfüzyonu olan çocukta resüsitasyon '
                                                  'tamamlanmadan sedasyon ve görüntüleme yapılamaz.',
                                'text': 'Karın ağrısını ekarte etmek için damar yolu açmadan önce çocuğu sedasyon '
                                        'vererek batın tomografisine göndermek'}],
                 'question': 'Letarjik, gözyaşı olmayan ve inatçı kusan bu bebekte ilk yapılması gereken acil klinik '
                             'yaklaşım hangisidir?',
                 'stage_title': 'Sarı Alanda İlk Triyaj ve Resüsitasyon İhtiyacı'},
               { 'options': [ { 'explanation': 'Pediatrik şok ve ağır dehidratasyonda standart başlangıç tedavisi 20 '
                                               'mL/kg izotonik kristaloidin (%0.9 SF veya Ringer Laktat) 15-30 '
                                               'dakikada IV hızlı infüzyonudur. Yanıt değerlendirildikten sonra '
                                               'gerekirse bolus tekrarlanır.',
                                'is_correct': True,
                                'new_finding': '20 mL/kg SF (200 mL) 20 dakikada IV bolus verildi. Bolus sonrası KTA '
                                               "134/dk'ya geriledi, periferik nabızlar güçlendi, KDZ 2 saniyeye indi. "
                                               'Laboratuvar: Na 136 mEq/L, K 3.6 mEq/L, Cl 102 mEq/L, Üre 58 mg/dL, '
                                               'Kreatinin 0.8 mg/dL (prerenal azotemi), Venöz Kan Gazı pH 7.29, HCO3 '
                                               '15 mmol/L (hafif metabolik asidoz).',
                                'text': 'Yirmi mililitre bölü kilogram izotonik serum fizyolojiyi hızlı intravenöz '
                                        'bolus verip elektrolit ve böbrek fonksiyonlarını göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Hipotonik dekstroz infüzyonu damar içi hacmi genişletemedi ve akut '
                                                   'hiponatremiye bağlı serebral ödem gelişti.',
                                'teaching_point': 'Hipotonik sıvılar (%5 dekstroz vb.) intravasküler alanda kalmaz, '
                                                  'hücre içine geçer; şok bolusunda ASLA kullanılmaz.',
                                'text': 'Beyin ödemini önlemek amacıyla çocuğa ilk basamakta yüzde beş dekstroz içeren '
                                        'hipotonik solüsyonu hızlı bolus yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Yüksek ozmolariteli şekerli içecekler ozmotik ishali katlayarak '
                                                   'artırdı ve dehidratasyonu daha da ağırlaştırdı.',
                                'teaching_point': 'Meyve suları ve kolalı içecekler hiperozmolardır ve ishali artırır; '
                                                  'dehidratasyon tedavisinde yeri yoktur.',
                                'text': 'Damar yolu açılamazsa oral yoldan saatte 100 mL elma suyu ve kola içirerek '
                                        'glukoz ihtiyacını karşılamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Çocukta toksik megakolon, paralitik ileus ve karın distansiyonu '
                                                   'gelişti; klinik durumu hızla kötüleşti.',
                                'teaching_point': 'Çocukluk çağında motilite azaltıcı ilaçlar toksik bağırsak '
                                                  'dilatasyonu ve ölüm riski nedeniyle kesinlikle yasaktır.',
                                'text': 'İshal sayısı çok fazla olduğu için sıvı infüzyonu yerine öncelikle damardan '
                                        'yüksek doz loperamid ve antispazmodik vermek'}],
                 'question': 'Ağır dehidratasyon ve kompanse hipovolemik şok bulguları olan bu hastada ilk sıvı '
                             'tedavisi protokolü nasıl olmalıdır?',
                 'stage_title': 'Sıvı Resüsitasyonu Protokolü ve Laboratuvar'},
               { 'options': [ { 'explanation': 'Masif gastrointestinal kayıplar, letarji, dolaşım bozukluğu (KDZ >3 '
                                               'sn), prerenal azotemi ağır dehidratasyonlu akut gastroenteriti '
                                               'tanımlar.',
                                'is_correct': True,
                                'new_finding': 'Tanı: Akut Gastroenterit zemininde gelişen Ağır Dehidratasyon ve '
                                               'Kompanse Hipovolemik Şok.',
                                'text': 'Ağır dehidratasyonlu akut gastroenterit'},
                              { 'is_correct': False,
                                'scenario_update': 'Hastada enfeksiyon odağı olarak fokal sepsis, purpura veya '
                                                   'vazodilatasyon saptanmadı; tablo sıvı kaybına bağlı hipovolemiydi.',
                                'teaching_point': 'Sıvı bolusuna dakikalar içinde hızla ve tamamen yanıt veren tablo '
                                                  'hipovolemik şoktur; septik şokta vazopressör ihtiyacı doğar.',
                                'text': 'Septik şok tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Hastanın kan şekeri 94 mg/dL ve idrarda keton negatif geldi; '
                                                   'diyabetik ketoasidoz dışlandı.',
                                'teaching_point': "DKA'da hiperglisemi, ketonüri ve derin asidoz vardır; normoglisemik "
                                                  'gastroenteritte görülmez.',
                                'text': 'Diyabetik ketoasidoz koması'},
                              { 'is_correct': False,
                                'scenario_update': 'Adrenal krizde hiponatremi ve hiperkalemi beklenir; bu hastada '
                                                   'elektrolitler izotonik sınırlardaydı.',
                                'teaching_point': 'Gastroenterit kaynaklı hipovolemide elektrolitler başlangıçta '
                                                  'dengelidir; adrenal yetmezlikteki hiperkalemi izlenmez.',
                                'text': 'Primer adrenokortikal yetmezlik krizi'}],
                 'question': 'Sulu ishal, inatçı kusma, letarji, uzamış KDZ ve prerenal azotemisi olan bu hastada '
                             'kesin tanısal sınıflamanız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'İlk resüsitasyon bolusundan sonra kalan sıvı açığı (genellikle %7-10 '
                                               'defisit) ve günlük idame sıvı toplanır; yarısı ilk 8 saatte, kalanı '
                                               'sonraki 16 saatte dengeli solüsyonlarla (%0.45-%0.9 NaCl + %5 '
                                               'Dekstroz) verilir.',
                                'is_correct': True,
                                'new_finding': 'Hasta Sarı Alan gözlem yatağına alındı. İdame + defisit sıvı infüzyonu '
                                               'başlandı. İdrar çıkışı 4. saatte sağlandı (1.8 mL/kg/saat). Kusması '
                                               'durduktan sonra azar azar ORS başlandı ve 24 saat sonra servise '
                                               'devredildi.',
                                'text': 'Kalan dehidratasyon defisitini ve günlük idame sıvıyı hesaplayarak dengeli '
                                        'elektrolit solüsyonu ile yirmi dört saatte tamamlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Hala defisiti olan ve devam eden ishali bulunan çocuk eve '
                                                   'gittikten birkaç saat sonra tekrar ağır şoka girdi.',
                                'teaching_point': 'İlk bolus sadece intravasküler alanı kurtarır; doku defisiti ve '
                                                  'devam eden kayıplar yerine konmadan taburculuk yapılamaz.',
                                'text': 'İlk bolus sonrası nabız düzeldiği için damar yolunu derhal çekip hastayı '
                                        'hiçbir sıvı vermeden evine göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Aşırı hızlı ve yüksek volümlü sıvı yüklemesi hastada akut akciğer '
                                                   'ödemi ve solunum yetmezliğini tetikledi.',
                                'teaching_point': 'İdame ve defisit sıvıları zamana yayılarak (24 saatte) '
                                                  'verilmelidir; kontrolsüz aşırı sıvı volüm yüklenmesine yol açar.',
                                'text': 'Hepsini tek seferde vermek için hastaya ek olarak 100 mL/kg sıvıyı yarım '
                                        'saatte serbest akışla damardan infüze etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Kanaması veya koagülopatisi olmayan hastaya gereksiz kan ürünü '
                                                   'verilmesi transfüzyon reaksiyonuna neden oldu.',
                                'teaching_point': 'Gastroenterit kaynaklı dehidratasyonun tedavisi kristalloid '
                                                  'sıvılardır; anemi veya kanama yoksa kan transfüzyonu endike '
                                                  'değildir.',
                                'text': 'Sıvı tedavisini tamamen sonlandırıp hastaya acil plazma veya tam kan '
                                        'transfüzyonu başlatmak'}],
                 'question': 'İlk 20 mL/kg izotonik bolus ile hemodinamisi toparlayan hastada bundan sonraki '
                             'parenteral sıvı yönetimi nasıl olmalıdır?',
                 'stage_title': 'İdame ve Defisit Sıvı Yönetimi Planı'}]},
  { 'age': '7 Yaşında',
    'case_pearl': 'Pediatrik Tip 1 Diyabetin ilk başvurularının üçte biri DKA ile gerçekleşir ve sıklıkla karın '
                  'ağrısı, bulantı ve kusma nedeniyle akut apandisit veya gastroenterit sanılarak atlanır! Karın '
                  'ağrısı mezenterik iskemi ve ketozisten kaynaklanır. Derin ve hızlı Kussmaul solunumu ve nefeste '
                  'aseton kokusu kritik ipucudur. Her karın ağrılı ve kusan çocukta yatak başı glukoz ZORUNLUDUR! DKA '
                  'yönetiminde en kritik kural: İLK BİR SAATTE SADECE İZOTONİK SIVI (%0.9 SF, 10-20 mL/kg) VERİLİR; '
                  'İNSÜLİN İLK SAATTE ASLA VERİLMEZ! İnsülin bolus yapılmaz, 1. saatten sonra 0.05-0.1 Ü/kg/saat '
                  'infüzyonla gidilir. Hızlı hipotonik sıvı veya erken insülin serebral ödem yapar.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Şiddetli karın ağrısı, inatçı kusma, derin ve hızlı soluk alıp verme ile dalgınlık',
    'disposition': 'Sarı Alanda İki Damar Yolu + Başlangıç İzotonik Sıvı Resüsitasyonu + IV Düşük Doz İnsülin + Çocuk '
                   'Yoğun Bakım Yatışı',
    'final_diagnosis': 'Diyabetik Ketoasidoz (DKA - Ağır Evre / Akut Batın Maskeli)',
    'gender': 'Erkek',
    'history': 'Yedi yaşındaki erkek çocuk ailesi tarafından Sarı Alana getiriliyor: İki gündür giderek artan karın '
               'ağrısı ve kusması var. Aile başlangıçta mide üşütmesi sanmış ancak çocuk bugün belirgin şekilde '
               'halsizleşmiş, konuşurken saçmalamaya başlamış ve nefesi çok derin ve hızlı hale gelmiş. Annesi son '
               'birkaç haftadır çocuğun aşırı su içtiğini, sık idrara çıktığını ve geceleri altını ıslatmaya '
               'başladığını ifade ediyor.',
    'id': 'Y45',
    'steps': [ { 'options': [ { 'explanation': 'Kussmaul solunumu ve aseton kokusu DKA için tipiktir. Karın ağrısı ve '
                                               'kusmayla gelen çocukta parmak ucu kan şekeri ölçümü saniyeler içinde '
                                               'hayat kurtarıcı tanı sağlar.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 142/dk, SS 36/dk (derin, iç çekici '
                                               'Kussmaul solunumu, ağızda belirgin çürük elma / aseton kokusu), TA '
                                               '92/56 mmHg, SpO2 %99, KDZ 3 sn. Bilinç konfüze, uykuya meyilli. '
                                               'Batında yaygın hassasiyet var ancak defans ve rebound yok. Yatak başı '
                                               'glukometre: Kan Şekeri 460 mg/dL. İdrar stix: Glukoz (++++), Keton '
                                               '(++++).',
                                'text': 'Bilinç durumunu, solunum paternini ve kokusunu inceleyip yatak başı kapiller '
                                        'kan şekeri ve keton ölçümü yapmak'},
                              { 'is_correct': False,
                                'scenario_update': "Tanınmamış DKA'lı hasta genel anesteziye alındığında ölümcül "
                                                   'kardiyovasküler kollaps ve derin asidoz gelişti.',
                                'teaching_point': 'DKA karın ağrısıyla apandisiti mükemmel taklit eder; kan şekeri '
                                                  'bakılmadan cerrahiye alınması katastrofiktir.',
                                'text': 'Karın ağrısını apandisit kabul edip kan şekeri bakmadan hastayı derhal acil '
                                        'ameliyathaneye apendektomiye göndermek'},
                              { 'is_correct': False,
                                'scenario_update': "Beta-mimetik salbutamol glukoz düzeyini 550 mg/dL'ye yükseltti ve "
                                                   "taşikardiyi 170/dk'ya fırlatarak asidozu artırdı.",
                                'teaching_point': 'Kussmaul solunumunda hışıltı veya ekspiratuar uzama yoktur; '
                                                  'metabolik asidoza kompansatuar takipnedir, astım değildir.',
                                'text': 'Hızlı solunumu astım atağı sanarak hastaya yüksek doz nebülize salbutamol ve '
                                        'steroid inhalasyonu başlatmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Hasta bekleme salonunda komaya girdi; kan şekeri ve kan gazı '
                                                   'bakılmadığı için DKA koması derinleşti.',
                                'teaching_point': 'Bilinç değişikliği ve Kussmaul solunumu olan hasta acil '
                                                  'Sarı/Kırmızı alanda monitörize edilmelidir.',
                                'text': 'Kusmayı kesmek amacıyla hastaya oral antiemetik tablet verip Yeşil Alan '
                                        'polikliniğinde sıraya sokmak'}],
                 'question': 'Karın ağrısı, kusma ve derin solunumu olan bu çocukta Sarı Alanda yapılması gereken ilk '
                             'acil değerlendirme hangisidir?',
                 'stage_title': 'Sarı Alanda İlk Değerlendirme ve Solunum Paterninin Analizi'},
               { 'options': [ { 'explanation': 'DKA kılavuzlarına (ISPAD) göre ilk 1 saatte 10-20 mL/kg izotonik SF '
                                               'infüzyonu verilir. İlk saatte İNSÜLİN KESİNLİKLE VERİLMEZ. Erken '
                                               'insülin intravasküler hacmi çökertir ve beyin ödemi riskini katlar.',
                                'is_correct': True,
                                'new_finding': 'Venöz Kan Gazı: pH 7.10, pCO2 18 mmHg, HCO3 5.8 mmol/L, Baz Defisiti '
                                               '-22 (ağır metabolik asidoz). Biyokimya: Na 129 mEq/L (düzeltilmiş Na '
                                               '135 mEq/L), K 4.9 mEq/L, Üre 48 mg/dL, Kreatinin 0.9 mg/dL, Anyon '
                                               'açığı 26. İlk bir saatte 10 mL/kg SF (250 mL) intravenöz infüzyonla '
                                               'verildi.',
                                'text': 'Kan gazı, elektrolitler ve ozmolariteyi gönderip ilk bir saatte yalnızca '
                                        'izotonik kristaloid infüzyonu başlatmak'},
                              { 'is_correct': False,
                                'scenario_update': 'İV bolus insülin sonrası kan şekeri hızla çakıldı; hastada akut '
                                                   'serebral ödem ve anizokori gelişti.',
                                'teaching_point': "Pediatrik DKA'da İV bolus insülin KONTRENDİKEDİR; serebral ödem ve "
                                                  'hipokalemik arrest riskini artırır.',
                                'text': 'Kan şekerini hızla düşürmek için derhal damardan yüksek doz intravenöz bolus '
                                        'insülin enjeksiyonu yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Bikarbonat verilmesi paradoksal santral sinir sistemi asidozuna ve '
                                                   'beyin ödemine yol açarak bilinci kapattı.',
                                'teaching_point': "DKA'da rutin bikarbonat verilmesi beyin ödemi ve hipokalemi riskini "
                                                  'artırır; pH <6.9 ve dirençli şok dışında yasaktır.',
                                'text': 'Asidozu derhal sıfırlamak amacıyla hastaya hızlı puşe şeklinde yüksek doz '
                                        'sodyum bikarbonat ampulü vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Konfüze çocuk suyu aspire etti ve serum ozmolaritesinin ani '
                                                   'düşmesiyle fokal konvülziyon geçirdi.',
                                'teaching_point': 'Bilinç değişikliği olan hastaya oral sıvı verilemez; ozmolaritenin '
                                                  'hızlı düşürülmesi herniasyona yol açar.',
                                'text': 'Hiperglisemiyi düzeltmek amacıyla hastaya bol miktarda serbest musluk suyu '
                                        'içirmeye çalışmak'}],
                 'question': 'Ağır hiperglisemi ve ketonürisi saptanan bu hastada Sarı Alanda atılacak ilk sıvı ve '
                             'tetkik adımı ne olmalıdır?',
                 'stage_title': 'Acil Biyokimya, Kan Gazı ve Başlangıç Sıvı Protokolü'},
               { 'options': [ { 'explanation': 'Kan şekeri >200 mg/dL, venöz pH <7.10, HCO3 <5 mmol/L ve '
                                               'ketonemi/ketonüri ağır evre diyabetik ketoasidoz (DKA) tanısıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Yeni Başlangıçlı Tip 1 Diabetes Mellitus zemininde Ağır '
                                               'Diyabetik Ketoasidoz.',
                                'text': 'Ağır diyabetik ketoasidoz tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Hastanın hiperglisemisi ve ketonürisi cerrahi peritonitle '
                                                   'açıklanamaz; asidoz ketoasit birikimine bağlıdır.',
                                'teaching_point': 'DKA akut karın tablosunu taklit eder; ancak idrarda masif keton ve '
                                                  'hiperglisemi diyabeti kanıtlar.',
                                'text': 'Perfore apandisite bağlı septik peritonit'},
                              { 'is_correct': False,
                                'scenario_update': 'Gastroenteritte hiperglisemi >400 mg/dL ve masif ketonüri ile '
                                                   'anyon açığı 26 düzeyine çıkmaz.',
                                'teaching_point': 'Gastroenteritte açlık ketozu hafif olabilir ancak kan şekeri normal '
                                                  'veya düşüktür; hiperglisemi olmaz.',
                                'text': 'Akut toksik rotavirüs gastroenteriti'},
                              { 'is_correct': False,
                                'scenario_update': 'Salisilat zehirlenmesi hiperventilasyon yapsa da masif '
                                                   'hiperglisemi ve diyabet öyküsü bulunmaz.',
                                'teaching_point': 'Salisilat zehirlenmesinde kan şekeri genellikle normal veya '
                                                  'düşüktür; glukozüri ve polidipsi öyküsü yoktur.',
                                'text': 'Akut salisilat intoksikasyonu tablosu'}],
                 'question': 'Ağır anyon açıklı metabolik asidoz, hiperglisemi, ketonüri ve karın ağrısı olan hastada '
                             'kesin klinik tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'İlk saatlik sıvıdan sonra 0.05-0.1 Ü/kg/saat dozunda regüler insülin '
                                               "sürekli infüzyonla başlanır. Kan şekeri saatte 50-75 mg/dL'den hızlı "
                                               'düşürülmemelidir. Glukoz <250-300 mg/dL olduğunda sıvıya dekstroz '
                                               'eklenir.',
                                'is_correct': True,
                                'new_finding': '0.05 Ü/kg/saat regüler insülin infüzyonu başlandı. Saatlik kan şekeri, '
                                               'kan gazı ve nörolojik muayene takibiyle çocuk yoğun bakım ünitesine '
                                               'nakledildi. Beyin ödemi gelişmeden ketozu 18 saatte başarıyla kırıldı.',
                                'text': 'Sıfır nokta sıfır beş ünite kilogram saat regüler insülin infüzyonuyla '
                                        'hastayı çocuk yoğun bakıma yatırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Subkutan insülin hipoperfüzyon nedeniyle emilemedi; asidoz '
                                                   'kırılmadı ve yoğun bakım takibi gecikti.',
                                'teaching_point': "Ağır DKA'da subkutan insülin emilimi düzensizdir; mutlak surette "
                                                  'intravenöz sürekli infüzyon kullanılmalıdır.',
                                'text': 'İnsülin ihtiyacını karşılamak için günde bir kez subkutan uzun etkili glargin '
                                        'insülin yapıp hastayı servise göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Sıvısız insülin verilmesi ozmotik sıvıyı hücre içine çekerek derin '
                                                   'hipovolemik şok ve kardiyak arreste yol açtı.',
                                'teaching_point': "DKA'da sıvı resüsitasyonu insülin kadar kritiktir; sıvı olmadan "
                                                  'insülin verilmesi dolaşım çöküşüne neden olur.',
                                'text': 'Kan şekeri düşene kadar hastaya hiçbir sıvı vermeyip sadece yüksek doz '
                                        'insülin infüzyonu uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'İnsülin kesilince keton üretimi yeniden alevlendi ve hasta 6 saat '
                                                   'sonra daha ağır bir ketoasidozla acile döndü.',
                                'teaching_point': 'İnsülin hedefi glukoz değil, asidozun ve ketozun kapanmasıdır; '
                                                  'glukoz düşünce sıvıya dekstroz eklenerek insüline devam edilir.',
                                'text': "Kan şekeri 400 mg/dL'nin altına düşer düşmez insülin infüzyonunu tamamen "
                                        'kesip hastayı taburcu etmek'}],
                 'question': 'İlk bir saatlik izotonik sıvı infüzyonu tamamlanan bu hastada ikinci basamakta '
                             'uygulanacak doğru insülin ve izlem protokolü hangisidir?',
                 'stage_title': 'İnsülin İnfüzyonu ve Yoğun Bakım Yatışı'}]},
  { 'age': '3 Yaşında',
    'case_pearl': 'Tipik HÜS, Shiga toksin üreten E. coli (STEC O157:H7) veya Shigella kaynaklı kanlı ishalden 5-10 '
                  'gün sonra gelişir. Klasik triyad: 1) Mikroanjiyopatik hemolitik anemi (şistositler, indirekt '
                  'hiperbilirubinemi, LDH yüksekliği, Coombs negatif), 2) Trombositopeni, 3) Akut böbrek hasarı '
                  '(oligüri/anüri, üre/kreatinin artışı). Kanlı ishalde ampirik antibiyotik verilmesi bakteri '
                  "lizisiyle toksin salınımını artırarak HÜS riskini KATLAR! HÜS'te aktif hayatı tehdit eden kanama "
                  'veya cerrahi olmadıkça TROMBOSİT TRANSFÜZYONU KONTRENDİKEDİR; verilen trombositler mikrovasküler '
                  'trombozu besleyerek böbrek hasarını alevlendirir.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Kanlı ishalin bitmesinin ardından başlayan aşırı halsizlik, solukluk, vücutta morluklar ve idrar '
                 'miktarında azalma',
    'disposition': 'Sarı Alanda Sıvı-Elektrolit Dengesi + Trombosit Transfüzyonundan Kaçınma + Diyaliz Hazırlığı ile '
                   'Yoğun Bakım',
    'final_diagnosis': 'Hemolitik Üremik Sendrom (STEC / E. coli O157:H7 İlişkili Tipik HÜS)',
    'gender': 'Kız',
    'history': 'Üç yaşındaki kız çocuk ailesi tarafından Sarı Alana getiriliyor: Beş gün önce ateş, kramp tarzı karın '
               'ağrısı ve kanlı ishal geçirmiş, dış merkezde enfeksiyon denilerek oral antibiyotik başlanmış. İshal '
               'iki gün önce azalmış ancak dünden beri çocuk aşırı soluklaşmış, bacaklarında küçük kırmızı-mor '
               'noktalar belirmiş ve son 18 saattir bezi tamamen kuru kalmış.',
    'id': 'Y46',
    'steps': [ { 'options': [ { 'explanation': "HÜS'te hemoliz (solukluk/ikter), trombositopeni (peteşi/purpura) ve "
                                               'böbrek tutulumu (hipertansiyon/ödem/anüri) fizik muayenenin odağını '
                                               'oluşturur.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.2°C, KTA 136/dk, SS 26/dk, TA 118/76 mmHg '
                                               '(yaşına göre belirgin hipertansif), SpO2 %98. Hasta ileri derecede '
                                               'soluk (balmumu rengi), skleralarda hafif subikter mevcut. Alt '
                                               'ekstremitelerde yaygın peteşiler ve pretibial hafif gode bırakan ödem '
                                               'izlendi. Batın rahat, son 18 saattir idrar çıkışı sıfır (anüri).',
                                'text': 'Solukluk, skleral ikter, mukozal kanama, periferik ödem, kan basıncı ve idrar '
                                        'çıkışını sistemik olarak incelemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Soluk ve anürik çocuk poliklinik kuyruğunda hipertansif '
                                                   'ensefalopati ve akciğer ödemi tablosuna girdi.',
                                'teaching_point': 'Kanlı ishal sonrası anüri ve solukluk gelişen çocuk HÜS adayıdır; '
                                                  'acil serviste monitörize edilmelidir.',
                                'text': 'Kanlı ishal öyküsü nedeniyle sadece rektal tuşe yapıp hastayı gastroenterit '
                                        'polikliniğine geri göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'NSAİİ verilmesi renal kan akımını keserek akut böbrek hasarını '
                                                   'daha da derinleştirdi.',
                                'teaching_point': 'Böbrek hasarı ve oligürisi olan çocuklarda nefrotoksik NSAİİ '
                                                  'ilaçlar kesinlikle KONTRENDİKEDİR.',
                                'text': 'Tansiyon yüksekliğini ağrıya bağlayarak kan basıncını ölçmeden hastaya oral '
                                        'NSAİİ şurup içirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Trombositopenik hastada üretral travmaya bağlı masif kontrolsüz '
                                                   'kanama meydana geldi.',
                                'teaching_point': 'Trombositopenik çocuklarda travmatik invaziv girişimlerden '
                                                  'kaçınılmalı, anürinin renal kaynaklı olduğu bilinmelidir.',
                                'text': 'Anüriyi mesane tıkanıklığı sanarak sterilizasyona uymadan hızla metalik '
                                        'üretral buji uygulamak'}],
                 'question': 'Kanlı ishal sonrası solukluk, peteşi ve anürisi olan bu çocukta ilk fizik muayene '
                             'yaklaşımınız ne olmalıdır?',
                 'stage_title': 'Sarı Alanda İlk Klinik Muayene ve Triyad Bulguları'},
               { 'options': [ { 'explanation': 'Periferik yaymada şistositlerin (parçalanmış eritrositler) görülmesi '
                                               'mikroanjiyopatik hemolitik anemiyi doğrular. Trombositopeni ve yüksek '
                                               'üre/kreatinin ile HÜS triyadı tamamlanır.',
                                'is_correct': True,
                                'new_finding': 'Hemogram: Hb 6.4 g/dL, Lökosit 14.200/mm³, Trombosit 36.000/mm³. '
                                               'Periferik Yayma: Bol miktarda şistosit (miğfer hücresi), polikromazi, '
                                               'trombosit kümeleri yok. Biyokimya: Üre 138 mg/dL, Kreatinin 2.7 mg/dL, '
                                               'LDH 1820 U/L, İndirekt Bilirubin 2.4 mg/dL, Direkt Coombs Negatif.',
                                'text': 'Tam kan sayımı, periferik yayma, böbrek fonksiyon testleri, LDH ve idrar '
                                        'analizini acil olarak çalışmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Kemik iliği hazırlığı yapılırken anürik ve hiperkalemik hastada '
                                                   'kardiyak ritim bozukluğu gelişti.',
                                'teaching_point': 'Kanlı ishal sonrası şistositik anemi ve trombositopenide kemik '
                                                  'iliği biyopsisi gerekmez; tanı periferik yayma ile konur.',
                                'text': 'Kemik iliği aspirasyonu yaparak akut lösemiyi dışlamadan hiçbir biyokimya '
                                        'veya böbrek testi yapmamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Laboratuvarı geciktirilen hastada potasyum 7.2 mEq/L düzeyine '
                                                   'çıkarak ventriküler aritmiyi tetikledi.',
                                'teaching_point': 'Akut böbrek yetmezliği şüphesinde elektrolitler ve renal panel '
                                                  'dakikalar içinde değerlendirilmelidir.',
                                'text': 'Yalnızca dışkıda rota ve adenovirüs antijeni bakıp kan tahlillerini '
                                        'poliklinik kontrolüne bırakmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Kanama zamanı uzamış bulundu ancak anemi derinliği ve böbrek '
                                                   'yetmezliği derecesi anlaşılamadı.',
                                'teaching_point': 'HÜS bir mikroanjiyopatidir; tanı periferik yayma, trombosit sayısı '
                                                  've renal fonksiyonlarla doğrulanır.',
                                'text': 'Sadece kanama zamanı testi yapıp pıhtılaşma faktörlerini ölçmeden hastayı '
                                        'gözlem odasına almak'}],
                 'question': 'HÜS şüphesi olan bu hastada tanıyı doğrulamak için yapılması gereken en kritik '
                             'laboratuvar testleri hangileridir?',
                 'stage_title': 'Periferik Yayma, Hemogram ve Renal Panel İncelemesi'},
               { 'options': [ { 'explanation': 'STEC enteritini takiben gelişen non-immün mikroanjiyopatik hemolitik '
                                               'anemi (şistositler), trombositopeni ve akut üremi HÜS tanısıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: STEC İlişkili Tipik Hemolitik Üremik Sendrom (HÜS).',
                                'text': 'Hemolitik üremik sendrom tablosu'},
                              { 'is_correct': False,
                                'scenario_update': "İTP'de sadece izole trombositopeni görülür; hemolitik anemi, "
                                                   'şistositler veya akut böbrek yetmezliği bulunmaz.',
                                'teaching_point': 'İTP izole trombositopenidir; anemi ve üremi triyadı varsa tanı İTP '
                                                  'olamaz, HÜS düşünülmelidir.',
                                'text': 'İmmün trombositopenik purpura hastalığı'},
                              { 'is_correct': False,
                                'scenario_update': 'DİK tablosunda PT ve aPTT belirgin uzar, fibrinojen düşer; bu '
                                                   'hastada koagülasyon testleri tamamen normaldi.',
                                'teaching_point': "HÜS'te primer patoloji trombosit tüketimidir, pıhtılaşma kaskadı "
                                                  'normaldir; bu nedenle PT ve aPTT normaldir.',
                                'text': 'Akut dissemine intravasküler koagülasyon'},
                              { 'is_correct': False,
                                'scenario_update': 'TTP çocuklarda son derece nadirdir, ateş ve baskın dalgalı '
                                                   'nörolojik bulgularla seyreder, ADAMTS13 eksikliği vardır.',
                                'teaching_point': 'Çocukluk çağında kanlı ishal sonrası gelişen tablo ezici çoğunlukla '
                                                  "TTP değil, tipik HÜS'tür.",
                                'text': 'Trombotik trombositopenik purpura sendromu'}],
                 'question': 'Kanlı ishal sonrası mikroanjiyopatik hemolitik anemi, trombositopeni ve akut böbrek '
                             'hasarı saptanan hastada kesin tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': "HÜS'te trombosit verilmesi mikrovasküler trombozu besler ('ateşe "
                                               "benzin dökmek'). Sıvı kısıtlaması, hipertansiyon kontrolü, gerekirse "
                                               'eritrosit süspansiyonu ve acil hemodiyaliz/periton diyalizi '
                                               'planlanmalıdır.',
                                'is_correct': True,
                                'new_finding': 'Trombosit verilmedi. Sıkı sıvı kısıtlaması (insensibl kayıp + idrar) '
                                               'yapıldı. Hb 6.4 g/dL için yavaş eritrosit transfüzyonu planlandı ve '
                                               'çocuk nefrolojisi tarafından renal replasman (diyaliz) hazırlığıyla '
                                               'yoğun bakıma yatırıldı.',
                                'text': 'Trombosit transfüzyonundan kesinlikle kaçınarak sıvı dengesini ayarlamak, kan '
                                        'basıncını kontrol etmek ve çocuk nefrolojisine devretmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Verilen trombositler glomerüler kapillerleri tıkayarak böbrek '
                                                   'hasarını derinleştirdi ve anüriyi kalıcı hale getirdi.',
                                'teaching_point': "HÜS'te aktif hayatı tehdit eden kanama olmadıkça trombosit "
                                                  'transfüzyonu kesinlikle KONTRENDİKEDİR.',
                                'text': 'Trombosit sayısı elli binin altında olduğu için derhal iki ünite aferez '
                                        'trombosit süspansiyonu infüzyonu yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Aminoglikozid akut tübüler nekrozu tetikleyerek zaten hasarlı olan '
                                                   'böbreği tamamen işlevsiz kıldı.',
                                'teaching_point': 'HÜS oturmuş olgularda antibiyotiklerin faydası yoktur ve '
                                                  'nefrotoksik antibiyotikler böbreği iflas ettirir.',
                                'text': 'İshali tamamen durdurmak için hastaya yüksek doz oral kinolon ve geniş '
                                        'spektrumlu intravenöz aminoglikozid başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Anürik hastaya kontrolsüz sıvı yüklenmesi masif akciğer ödemi ve '
                                                   'solunum arrestine yol açtı.',
                                'teaching_point': 'Anürik böbrek yetmezliğinde aşırı sıvı yüklenmesi ölümcül '
                                                  'hipervolemi ve akciğer ödemine neden olur; sıvı kısıtlanmalıdır.',
                                'text': 'Anüriyi kırmak amacıyla hastaya 1 saat içinde 60 mL/kg izotonik mayi yükleyip '
                                        'zorlu diürez başlatmak'}],
                 'question': 'HÜS tanısı kesinleşen, anürik ve trombositi 36.000/mm³ olan bu çocukta en uygun tedavi '
                             've yönetim stratejisi hangisidir?',
                 'stage_title': 'Trombosit Transfüzyon Tuzağından Kaçınma ve Tedavi'}]},
  { 'age': '3 Haftalık',
    'case_pearl': 'Yenidoğan ve erken süt çocukluğu döneminde aksi kanıtlanana kadar YEŞİL (SAFRALI) KUSMA MUTLAK BİR '
                  'CERRAHİ ACİLDİR! En korkulan patoloji bağırsakların embriyolojik rotasyon kusuru (malrotasyon) '
                  'zemininde dar mezenter kökü etrafında dönmesidir (midgut volvulusu). Süperior mezenterik arter '
                  'tıkanır ve birkaç saat içinde tüm ince bağırsaklar gangrene uğrar (kısa bağırsak sendromu veya '
                  'ölüm). Tanıda altın standart acil üst gastrointestinal floroskopik kontrast grafisidir (Treitz '
                  'ligamenti sağda yerleşir, duodenal burgu / tirbüşon görünümü). Müdahale dakikalarla yarışır; acil '
                  'cerrahi detorsiyon ve Ladd prosedürü uygulanmalıdır.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Aniden başlayan koyu yeşil safralı kusma, karında şişlik ve beslenmeyi tamamen reddetme',
    'disposition': 'Sarı Alanda Nazogastrik Dekompresyon + Damar Yolu + Acil Çocuk Cerrahisi ile Ladd Prosedürü',
    'final_diagnosis': 'İntestinal Malrotasyon ve Orta Bağırsak (Midgut) Volvulusu',
    'gender': 'Erkek',
    'history': 'Üç haftalık term doğmuş erkek bebek ailesi tarafından panikle Sarı Alana getiriliyor: Doğumundan bu '
               'yana sorunsuz emen bebek, 3 saat önce aniden fışkırır tarzda koyu zümrüt yeşili safralı kusmaya '
               'başlamış. Ardından iki kez daha yeşil safralı kusmuş. Bebek iniltili solumaya başlamış, karnı şişmiş '
               've aşırı halsizleşmiş. Annesi son birkaç saattir hiç gaz veya gaita çıkarmadığını ifade ediyor.',
    'id': 'Y47',
    'steps': [ { 'options': [ { 'explanation': 'Erken bebeklikte yeşil safralı kusma ampulla Vateri distalindeki '
                                               'mekanik tıkanıklığı gösterir ve volvulus dışlanana kadar en yüksek '
                                               'öncelikli cerrahi acildir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.1°C, KTA 166/dk, SS 44/dk, TA 72/42 mmHg, SpO2 '
                                               '%97, KDZ 3.5 sn. Bebek iniltili ve soluk. Batın belirgin distandü, '
                                               'epigastriumda hassasiyet mevcut. Nazogastrik tüp takıldı ve derhal 30 '
                                               'mL koyu zümrüt yeşili safralı sıvı aspire edildi; dekompresyonla bebek '
                                               'kısmen rahatladı.',
                                'text': 'Yeşil kusmuğu cerrahi acil olarak kabul edip, perfüzyon ve batın '
                                        'distansiyonunu değerlendirerek acil dekompresyon sağlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Emzirilen bebek tüm sütü tekrar yeşil safrayla kustu ve ince '
                                                   'bağırsak iskemisi dakikalar içinde ilerledi.',
                                'teaching_point': 'Anne diyeti safralı kusma yapmaz; yeşil kusmuk patolojik safradır '
                                                  've acil cerrahi inceleme gerektirir.',
                                'text': 'Yeşil rengin annenin yediği sebzelerden kaynaklandığını söyleyerek bebeği '
                                        'emzirmesi için anneye geri vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Reflü tedavisi verilen bebekte 3 saat sonra bağırsak nekrozu, '
                                                   'peritonit ve septik şok tablosu oturdu.',
                                'teaching_point': 'Fizyolojik reflüde kusmuk asla yeşil veya safralı değildir; safralı '
                                                  'kusmada reflü tanısı konulamaz.',
                                'text': 'Kusmayı basit gastroözofageal reflü kabul edip oral antiasit şurup vererek '
                                        'Yeşil Alanda takip etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Volvulus zeminindeki iskemik bağırsak yüksek basınçlı lavmanla '
                                                   'perfore oldu ve fekal peritonit gelişti.',
                                'teaching_point': 'Şüpheli intestinal volvulus vakalarında lavman perforasyona yol '
                                                  'açar; kesinlikle KONTRENDİKEDİR.',
                                'text': 'Bağırsak pasajını açmak için rektal yoldan yüksek basınçlı sabunlu su lavmanı '
                                        'uygulamak'}],
                 'question': 'Üç haftalık bebekte aniden başlayan yeşil safralı kusma karşısında Sarı Alandaki ilk '
                             'yaklaşım ne olmalıdır?',
                 'stage_title': 'Sarı Alanda İlk Değerlendirme ve Yeşil Safralı Kusmanın Önemi'},
               { 'options': [ { 'explanation': 'Hemodinamik resüsitasyon sağlanırken altın standart yöntem olan '
                                               'kontrastlı üst GİS grafisi çekilir. Treitz ligamentinin pozisyonu ve '
                                               'duodenal tirbüşon (corkscrew) görünümü volvulusu doğrular.',
                                'is_correct': True,
                                'new_finding': 'Damar yolu açıldı, 10 mL/kg SF bolus verildi. Kontrastlı Üst GİS '
                                               'Grafisi: Duodenojejunal bileşkenin (Treitz) omurganın soluna '
                                               'geçemediği, sağda yerleştiği ve kontrast maddenin burgu şeklinde '
                                               'kıvrılarak tıkandığı (tirbüşon / corkscrew işareti) izlendi.',
                                'text': 'İki damar yolu açıp izotonik sıvı bolusu başlatmak ve acil kontrastlı '
                                        'floroskopik grafi planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Bekleme sürecinde süperior mezenterik arter tamamen tıkandı ve tüm '
                                                   'ince bağırsaklar nekroze oldu.',
                                'teaching_point': 'Volvulus dakikalarla yarışan bir iskemidir; 24 saat beklenmesi '
                                                  'bağırsağın tamamen kaybedilmesine yol açar.',
                                'text': 'Kontrastlı grafi çekmeden sadece 24 saat sonra kontrol edilmek üzere direkt '
                                        'batın grafisi isteyip beklemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Cerrahi müdahale yapılmadığı için bebek ağır metabolik asidoz ve '
                                                   'çoklu organ yetmezliğine girdi.',
                                'teaching_point': 'Mekanik strangülasyon aç bırakılarak çözülmez; acil cerrahi '
                                                  'detorsiyon gereklidir.',
                                'text': 'Tanıyı netleştirmek amacıyla bebeği kırk sekiz saat aç bırakıp sadece idrar '
                                        'miktarını izleyerek beklemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gaita testi sonucu beklenirken geçen zamanda bağırsak gangreni '
                                                   'gelişti ve perforasyon oluştu.',
                                'teaching_point': 'Safralı kusan bebekte dışkı tahlili tanıyı koydurmaz; radyolojik '
                                                  'üst GİS anatomisi hızla görüntülenmelidir.',
                                'text': 'Tanı koymak için sadece gaitada gizli kan testi gönderip sonucunu acil '
                                        'serviste beklemek'}],
                 'question': 'Volvulus şüphesi olan bu bebekte kesin tanıyı koymak için yapılması gereken en uygun '
                             'acil tanısal yaklaşım hangisidir?',
                 'stage_title': 'Acil Resüsitasyon ve Kontrastlı Üst GİS Görüntülemesi'},
               { 'options': [ { 'explanation': 'Erken süt çocukluğunda safralı kusma ve floroskopide Treitz ligamenti '
                                               'malpozisyonu ile duodenal burgu malrotasyon ve volvulus tanısıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: İntestinal Malrotasyon zemininde Midgut (Orta Bağırsak) '
                                               'Volvulusu.',
                                'text': 'Malrotasyon ve midgut volvulusu'},
                              { 'is_correct': False,
                                'scenario_update': 'Pilor stenozunda kusma safrasızdır çünkü darlık ampulla Vaterinin '
                                                   'proksimalindedir; safralı kusma pilor stenozu olamaz.',
                                'teaching_point': 'Pilor darlığında kusmuk beyaz/sütsüdür; yeşil safralı kusma pilor '
                                                  'stenozunu kesin olarak ekarte eder.',
                                'text': 'İnfantil hipertrofik pilor stenozu'},
                              { 'is_correct': False,
                                'scenario_update': 'Besin alerjisinde ani safralı kusma, akut batın distansiyonu ve '
                                                   'duodenal rotasyon kusuru görülmez.',
                                'teaching_point': 'Besin alerjisi kronik kanlı mukuslu dışkıyla seyreder; akut safralı '
                                                  'cerrahi kusma yapmaz.',
                                'text': 'Basit inek sütü proteini alerjisi'},
                              { 'is_correct': False,
                                'scenario_update': 'Hirschsprung hastalığı kolonu tutar; üst duodenal tirbüşon '
                                                   'görünümü ve akut mezenterik iskemi yapmaz.',
                                'teaching_point': 'Hirschsprung distal obstrüksiyondur; midgut volvulusu proksimal '
                                                  'duodenojejunal bir rotasyon ve iskemi acilidir.',
                                'text': 'Konjenital megakolon hastalığı'}],
                 'question': 'Üç haftalık bebekte yeşil safralı kusma ve üst GİS grafisinde duodenal tirbüşon görünümü '
                             'ile kesin tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Midgut volvulusunun tek tedavisi acil ameliyattır (Ladd prosedürü: '
                                               'saatin tersi yönünde detorsiyon, Ladd bantlarının kesilmesi, mezenter '
                                               'kökünün genişletilmesi, apendektomi ve bağırsakların non-rotasyon '
                                               'pozisyonuna yerleştirilmesi).',
                                'is_correct': True,
                                'new_finding': 'Çocuk cerrahisi ekibi tarafından acil ameliyathaneye alındı. Ladd '
                                               'prosedürü ile volvulus açıldı, 360 derece dönmüş olan mezenter detorse '
                                               'edildi; dolaşımı geri dönen bağırsaklar nekroz gelişmeden kurtarıldı.',
                                'text': 'Hastayı derhal oral kapalı tutup geniş spektrumlu antibiyotik eşliğinde acil '
                                        'Ladd ameliyatı için çocuk cerrahisine teslim etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Volvulusun kendiliğinden açılması beklenirken bağırsak ansları '
                                                   'gangrene gitti ve bebek kaybedildi.',
                                'teaching_point': 'Volvulus kendiliğinden düzelmez; gecikilen her dakika bağırsak '
                                                  'nekrozuna ve ölüme yol açar.',
                                'text': 'Cerrahiye vermeden önce hastayı acil serviste 72 saat süreyle damardan '
                                        'besleyerek bağırsağın kendiliğinden dönmesini beklemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Laksatif verilmesi burgu yapmış bağırsak ansının yırtılmasına ve '
                                                   'periton boşluğuna safra sızmasına yol açtı.',
                                'teaching_point': 'Vasküler boğulması olan bağırsak ansına oral laksatif verilmesi '
                                                  'delinmeye ve ölüme neden olur.',
                                'text': 'Ameliyat yerine hastaya oral yoldan yoğun mineral yağı ve laksatif içirerek '
                                        'tıkanıklığı mekanik açmaya çalışmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Ağrı kesici fitil iskemiyi durduramadı; hastada derin laktik '
                                                   'asidoz ve kardiyak kollaps gelişti.',
                                'teaching_point': 'Volvulus cerrahi bir acildir; analjezik fitillerle zaman '
                                                  'kaybedilmesi kesinlikle kabul edilemez.',
                                'text': 'Bebeği entübe etmeden ve cerraha haber vermeden sadece ağrı kesici fitil '
                                        'uygulayıp gözlem odasına almak'}],
                 'question': 'Midgut volvulusu tanısı doğrulanan bu bebekte hayat kurtarıcı kesin tedavi ve yönetim '
                             'basamağı hangisidir?',
                 'stage_title': 'Cerrahi Konsültasyon ve Hayat Kurtarıcı Ladd Prosedürü'}]},
  { 'age': '13 Yaşında',
    'case_pearl': 'Karın ve alt kadran ağrısıyla başvuran her erkek çocukta ve adölesanda GENİTAL VE SKROTAL MUAYENE '
                  'ZORUNLUDUR! Testis torsiyonunda ağrı T10 sempatik dermatomu nedeniyle sağ veya sol alt kadrana, '
                  'kasığa ve bele yayılabilir; bulantı-kusma sıktır ve sıklıkla apandisitle karışır. Muayenede '
                  'skrotumda şişlik, testisin yukarı çekilmesi (yüksek transvers yerleşim) ve kremaster refleksinin '
                  'kaybı patognomoniktir. Prehn belirtisi negatiftir. İlk 6 saatte cerrahi detorsiyonla testis '
                  'canlılık oranı >%90 iken, 12 saatten sonra nekroz riski çok yüksektir. Karşı testise de profilaktik '
                  'orşiopeksi yapılmalıdır (çan dili deformitesi bilateraldir).',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Sağ alt kadran karın ağrısı, bulantı, iki kez kusma ve yürümekte güçlük',
    'disposition': 'Sarı Alanda Acil Renkli Skrotal Doppler USG + Aç Bırakma + İlk 6 Saatte Cerrahi Detorsiyon ve '
                   'Orşiopeksi',
    'final_diagnosis': 'Akut Testis Torsiyonu (Karın Ağrısı Maskeli Akut Skrotum)',
    'gender': 'Erkek',
    'history': 'On üç yaşındaki adölesan erkek çocuk Sarı Alana getiriliyor: Yaklaşık 3 saat önce aniden başlayan sağ '
               'alt kadran karın ve kasık ağrısı tarifliyor. İki kez safrasız kusmuş. Yürürken iki büklüm kalıyor ve '
               'adımlarını açamıyor. Acil triyajında apandisit şüphesiyle Sarı Alana yönlendirilmiş ancak hastanın '
               'kasık ve genital bölgesi sorgulanmamış.',
    'id': 'Y48',
    'steps': [ { 'options': [ { 'explanation': 'Karın ağrılı erkek çocuklarda yansıyan testis torsiyonu ağrısını '
                                               'dışlamak için skrotal inspeksiyon, palpasyon ve kremaster refleksi '
                                               'kontrolü zorunlu fizik muayene kuralıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.0°C, KTA 108/dk, SS 20/dk, TA 112/70 mmHg, '
                                               'SpO2 %99. Batın muayenesinde sağ alt kadranda hafif hassasiyet var '
                                               'ancak belirgin defans veya rebound yok. Skrotal muayenede sağ '
                                               'hemiskrotum ödemli, eritemli ve aşırı hassas; sağ testis skrotumda '
                                               'yukarı çekilmiş ve yatay planda duruyor. Sağ kremaster refleksi '
                                               'tamamen kayıp; Prehn belirtisi negatif (testisi kaldırmak ağrıyı '
                                               'dindirmiyor).',
                                'text': 'Karın muayenesinin hemen ardından skrotumu açarak testis pozisyonu, '
                                        'simetrisi, hassasiyeti ve kremaster refleksini muayene etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Genital muayene yapılmadığı için torsiyone testis fark edilemedi '
                                                   've saatler içinde iskemi nekroza ilerledi.',
                                'teaching_point': 'Karın ağrılı erkek hastada testis muayenesinin atlanması en sık '
                                                  'medikolegal malpraktis nedenlerindendir.',
                                'text': 'Ağrı sağ alt kadranda olduğu için genital muayeneyi mahremiyet gerekçesiyle '
                                        'tamamen atlayıp doğrudan apandisit ameliyatı planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Kas gevşetici verilmesi kremaster yanıtını tamamen baskıladı ve '
                                                   'ayırıcı tanı koymayı imkansızlaştırdı.',
                                'teaching_point': 'Fizik muayene refleksleri tamamlanmadan nöromüsküler veya kas '
                                                  'gevşetici ilaçlar verilmemelidir.',
                                'text': 'Kremaster refleksine bakmadan hastaya kas gevşetici ilaç enjekte edip '
                                        'bacaklarını düzleştirmeye çalışmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Muayenesiz sevk edilen adölesanda 12 saat sonra testisin tamamen '
                                                   'gangrene olduğu ve canlılığını yitirdiği görüldü.',
                                'teaching_point': 'Akut başlayan karın ve kasık ağrısı aksi kanıtlanana kadar organik '
                                                  'bir iskemi acilidir.',
                                'text': 'Ağrının psikolojik olduğunu düşünerek hiçbir fizik muayene yapmadan hastayı '
                                        'psikiyatri polikliniğine yönlendirmek'}],
                 'question': 'Sağ alt kadran karın ağrısı ve kusması olan 13 yaşındaki erkek çocukta atlanmaması '
                             'gereken en kritik muayene adımı hangisidir?',
                 'stage_title': 'Karın Ağrılı Erkek Çocukta Genital Muayenenin Kritik Rolü'},
               { 'options': [ { 'explanation': 'Renkli Doppler ultrasonografi testis torsiyonunda kan akımının '
                                               'yokluğunu (%0 akım) ve kord dönmesini (whirlpool belirtisi) gösteren '
                                               'altın standart görüntüleme yöntemidir.',
                                'is_correct': True,
                                'new_finding': 'Acil Renkli Skrotal Doppler USG: Sağ testiste ve epididimde '
                                               'intratektal arteriyel ve venöz kan akımı tamamen durmuş (sıfır '
                                               'vaskülarite), kord trasesinde torsiyonla uyumlu burgu (whirlpool) '
                                               'işareti mevcut. Sol testis boyutları ve parankim kanlanması doğal.',
                                'text': 'Testis dokusundaki arteriyel ve venöz akımı netleştirmek için vakit '
                                        'kaybetmeden acil renkli Doppler ultrasonografi istemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Tomografi için geçen 2 saatlik sürede testisin iskemik nekroza '
                                                   'uğrama riski dramatik şekilde yükseldi.',
                                'teaching_point': 'Akut skrotumda zamanla yarışılır; gereksiz batın tomografileriyle '
                                                  'testis kurtarma penceresi (ilk 6 saat) kaçırılmamalıdır.',
                                'text': 'Testisi incelemek yerine apandisiti aramak amacıyla hastaya kontrastlı tüm '
                                        'vücut tomografisi çektirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Epididimit sanılarak antibiyotik verilen hastada 24 saat sonra '
                                                   'testis nekrozu gelişti ve testis kaybedildi.',
                                'teaching_point': 'Torsiyon antibiyotikle düzelmez; epididimit ile karışan her akut '
                                                  'skrotumda acil Doppler USG şarttır.',
                                'text': 'Tanıyı radyolojik olarak doğrulamadan hastaya 14 gün süreyle geniş spektrumlu '
                                        'antibiyotik başlayıp göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Sıcak uygulama metabolik doku oksijen ihtiyacını artırarak iskemik '
                                                   'testis nekrozunu daha da hızlandırdı.',
                                'teaching_point': 'İskemik dokuya sıcak kompres uygulanması metabolik hasarı katlar; '
                                                  'kesinlikle KONTRENDİKEDİR.',
                                'text': 'Skrotuma sıcak su torbası uygulayarak damarların gevşemesini ve akımın kendi '
                                        'kendine düzelmesini beklemek'}],
                 'question': 'Sağ hemiskrotumda hassasiyet ve kremaster kaybı saptanan bu hastada iskemiyi doğrulamak '
                             'için en uygun görüntüleme yöntemi hangisidir?',
                 'stage_title': 'Vasküler Perfüzyonun Gösterilmesi İçin Acil Doppler USG'},
               { 'options': [ { 'explanation': "Kremaster refleksinin kaybı, yatay yüksek yerleşim ve Doppler'de "
                                               'arteriyel/venöz kan akımının olmaması akut testis torsiyonunu '
                                               'kanıtlar.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Akut Sağ Testis Torsiyonu (İntravajinal Torsiyon).',
                                'text': 'Akut sağ testis torsiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Epididimitte kremaster refleksi korunur, Prehn pozitiftir ve '
                                                   "Doppler'de belirgin hipervaskülarite (kan akımı artışı) görülür.",
                                'teaching_point': 'Epididimitte kan akımı artar, torsiyonda ise kan akımı tamamen '
                                                  'kesilir.',
                                'text': 'Akut bakteriyel epididimit enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Morgagni torsiyonunda mavi benek (blue dot) belirtisi vardır, '
                                                   'testis kan akımı ve kremaster refleksi tamamen korunur.',
                                'teaching_point': 'Apendiks torsiyonunda tüm testisin kanlanması bozulmaz; izole üst '
                                                  'polde küçük infarkt nodülü vardır.',
                                'text': 'Testis apandiksi (Morgagni) torsiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Apandisitte skrotal eritem, transvers testis malpozisyonu ve '
                                                   'testiste kan akımı kaybı görülmez.',
                                'teaching_point': 'Apandisit ağrısı skrotuma yayılsa bile testis muayenesi ve kan '
                                                  'akımı tamamen doğaldır.',
                                'text': 'Akut flegmonöz apandisit perforasyonu'}],
                 'question': "Ani başlayan ağrı, yüksek yerleşimli hassas sağ testis, kremaster kaybı ve Doppler'de "
                             'sıfır kan akımı ile kesin tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Testis torsiyonu mutlak bir cerrahi acildir (altın ilk 6 saat). Acil '
                                               'cerrahi detorsiyon yapılmalı, testis canlılığı değerlendirilmeli ve '
                                               'nüksü önlemek için her iki testise birden bilateral orşiopeksi '
                                               'uygulanmalıdır.',
                                'is_correct': True,
                                'new_finding': 'Hasta acil ameliyathaneye alındı (semptomların 4. saati). Sağ skrotal '
                                               'eksplorasyonda 540 derece dönmüş kord detorse edildi. Sıcak kompres '
                                               'sonrası parankim pembeye döndü ve canlılık korundu. Bilateral '
                                               'orşiopeksi yapılarak testis kurtarıldı.',
                                'text': 'Hastayı aç bırakarak cerrahi onam almak ve testis canlılığını kurtarmak için '
                                        'derhal acil skrotal eksplorasyona almak'},
                              { 'is_correct': False,
                                'scenario_update': "Rastgele manuel döndürme torsiyon derecesini 540'tan 720 dereceye "
                                                   'çıkararak iskemi süresini kısalttı.',
                                'teaching_point': 'Manuel detorsiyon cerrahiye hazırlık sırasında denenebilir ancak '
                                                  'cerrahi eksplorasyon ve bilateral fiksasyonun yerini tutmaz.',
                                'text': 'Cerrahiye gerek duymadan testisi skrotum dışından rastgele döndürerek hastayı '
                                        'evine göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Poliklinik randevusuna kadar geçen sürede testis tamamen nekrotik '
                                                   've atrofik hale geldi; orşiektomi gerekti.',
                                'teaching_point': 'Torsiyon medikal bir hastalık değildir; 6 saatten sonra geri '
                                                  'dönüşümsüz testis atrofisi gelişir.',
                                'text': 'Ağrıyı kesmek amacıyla yüksek doz steroid başlayıp hastayı 48 saat sonra '
                                        'üroloji polikliniğine çağırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gözlemde bekletilen sürede kurtarılabilir doku tamamen nekroze '
                                                   'oldu; ameliyat şansı kaçırıldı.',
                                'teaching_point': "Torsiyonda 'bekle ve gör' yaklaşımı kesinlikle kabul edilemez; "
                                                  'dakikalar içinde ameliyathaneye geçilmelidir.',
                                'text': 'Testisin canlı kalıp kalmayacağını anlamak için hastayı Sarı Alanda 24 saat '
                                        'aralıksız gözlemde tutmak'}],
                 'question': 'Semptomların 3. saatinde olan ve testis torsiyonu doğrulanan bu hastada en uygun nihai '
                             'yönetim basamağı hangisidir?',
                 'stage_title': 'Zamanla Yarış ve Acil Cerrahi Detorsiyon'}]},
  { 'age': '6 Yaşında',
    'case_pearl': 'Henoch-Schönlein Purpurası (IgA Vasküliti) çocukluk çağının en sık sistemik vaskülitidir. Tanı '
                  'kriteri: Trombositopeni olmaksızın alt ekstremite ve kalçalarda yerçekimine bağımlı palpabl purpura '
                  '+ en az biri: 1) Kolik karın ağrısı, 2) Artrit/artralji, 3) Renal tutulum (hematüri/proteinüri), 4) '
                  'Biyopsi. Bağırsak duvarındaki lökositoklastik vaskülit intramural hematoma yol açar; bu hematom '
                  'ileokolik invajinasyon için öncü odak (lead point) olabilir! Bu nedenle şiddetli karın ağrısında '
                  'batın USG ile invajinasyon mutlaka dışlanmalıdır. Ciddi GİS tutulumunda oral/IV steroid (1-2 '
                  'mg/kg/gün) endikedir.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Kıvrandırıcı şiddetli karın ağrısı, dışkıda vişne çürüğü kan, dizlerde şişlik ve bacaklarda kabarık '
                 'kırmızı döküntüler',
    'disposition': 'Sarı Alanda Damar Yolu + İnvajinasyon Dışlama USG + Sistemik Kortikosteroid + Pediatri Servis '
                   'Yatışı',
    'final_diagnosis': 'Henoch-Schönlein Purpurası (IgA Vasküliti - Ciddi Gastrointestinal ve Eklem Tutulumu)',
    'gender': 'Erkek',
    'history': 'Altı yaşındaki erkek çocuk ailesi tarafından Sarı Alana getiriliyor: İki hafta önce üst solunum yolu '
               'enfeksiyonu geçirmiş. Dün bacaklarında ve kalçasında basmakla solmayan kırmızı kabarık döküntüler '
               'çıkmış. Bugün sabah bacaklarını karnına toplayıp kıvrandıran çok şiddetli karın ağrısı başlamış ve bir '
               'kez vişne çürüğü renkli kanlı dışkılamış. İki diz ekleminde de şişlik, ağrı ve basamama şikayeti var.',
    'id': 'Y49',
    'steps': [ { 'options': [ { 'explanation': 'Ele gelen (palpabl) purpurik lezyonlar vaskülitin damar duvarı '
                                               'inflamasyonunu yansıtır. Batında periton irritasyonu ve eklem efüzyonu '
                                               'sistemik tutulumu doğrular.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.4°C, KTA 116/dk, SS 22/dk, TA 106/64 mmHg, '
                                               'SpO2 %99. Bilateral alt ekstremitelerde ve kalçada simetrik '
                                               'yerleşimli, basmakla solmayan, ele gelen palpabl purpurik döküntüler. '
                                               'Bilateral diz eklemlerinde şişlik, ısı artışı ve hareket kısıtlılığı. '
                                               'Batında yaygın kolik hassasiyet var; rektal tuşede kanlı mukuslu gaita '
                                               'bulaştı.',
                                'text': 'Alt ekstremitedeki döküntüleri basmakla solma ve palpabilite yönünden '
                                        'inceleyip batın ve eklem muayenesini tamamlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Antihistaminik palpabl purpuraya etki etmedi; çocuğun karın ağrısı '
                                                   've bağırsak iskemisi derinleşti.',
                                'teaching_point': 'Palpabl purpura basmakla solmaz ve ürtiker gibi kaşıntılı değildir; '
                                                  'vaskülit göstergesidir, antihistaminikle geçmez.',
                                'text': 'Döküntüleri basit alerjik ürtiker kabul edip karın muayenesi yapmadan oral '
                                        'antihistaminik şurup vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz artrosentez yapılan eklemde travma ve kanama gelişti; '
                                                   'karındaki vaskülit ihmal edildi.',
                                'teaching_point': 'HSP artriti non-eroziv, geçici ve simetriktir; septik artrit '
                                                  'değildir, invaziv eklem aspirasyonu gerektirmez.',
                                'text': 'Dizlerdeki şişliği septik artrit sanarak eklem sıvısını acil serviste iğneyle '
                                        'boşaltıp batın muayenesini atlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Evde karın ağrısı dayanılmaz olan çocukta sekonder invajinasyon ve '
                                                   'bağırsak perforasyonu gelişti.',
                                'teaching_point': "HSP'de en büyük morbidite ve acil cerrahi riski gastrointestinal "
                                                  'komplikasyonlardan (intususepsiyon) kaynaklanır.',
                                'text': 'Karın ağrısını tamamen göz ardı ederek çocuğu sadece dermatoloji '
                                        'polikliniğine sevk edip evine göndermek'}],
                 'question': 'Döküntü, şiddetli karın ağrısı ve eklem şişliği olan bu çocukta ilk fizik muayene '
                             'yaklaşımınız ne olmalıdır?',
                 'stage_title': 'Sarı Alanda Döküntü Karakteri ve Batın Değerlendirmesi'},
               { 'options': [ { 'explanation': "HSP'de trombositopeni olmaması (normal/yüksek PLT) İTP ve "
                                               'meningokoksemiden ayırır. İdrarda hematüri/proteinüri renal vasküliti '
                                               'gösterir. Batın USG intramural hematomun yol açabileceği invajinasyonu '
                                               'dışlamak için şarttır.',
                                'is_correct': True,
                                'new_finding': 'Laboratuvar: Trombosit 350.000/mm³ (normal), Lökosit 12.400/mm³, Hb '
                                               '11.8 g/dL, CRP 24 mg/L. Tam İdrar Tahlili: Mikroskopik hematüri (+), '
                                               'proteinüri (+). Batın USG: İleum duvarında intramural hematomla uyumlu '
                                               'diffüz kalınlaşma izlendi; hedef tahtası bulgusu veya intussusepsiyon '
                                               'saptanmadı.',
                                'text': 'Trombosit sayısını doğrulamak, idrar analizini yapmak ve sekonder '
                                        'invajinasyonu dışlamak amacıyla batın ultrasonografisi çekmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Tomografi intramural hematomu gösterdi ancak çocuk gereksiz '
                                                   'radyasyona maruz kaldı; USG yeterliydi.',
                                'teaching_point': "HSP'de bağırsak tutulumu ve invajinasyon taramasında ilk tercih "
                                                  "iyonizan radyasyon içermeyen batın USG'sidir.",
                                'text': 'İdrar tahlili ve USG yapmadan hastaya doğrudan tüm batın bilgisayarlı '
                                        'tomografisi çektirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Normal trombositi olan hastaya verilen transfüzyon gereksiz volüm '
                                                   'yüklenmesine ve hiperviskoziteye yol açtı.',
                                'teaching_point': "HSP'de trombosit sayısı normal veya reaktif yüksektir; "
                                                  'trombositopeni vaskülit tanısını sorgulatır.',
                                'text': 'Trombosit sayısına bakmadan hastaya acil profillaktik trombosit süspansiyonu '
                                        'infüze etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Renal tutulumu ve şiddetli GİS kanaması olan çocuk evde '
                                                   'hipovolemiye girdi.',
                                'teaching_point': 'GİS kanaması ve renal tutulumu olan HSP vakaları mutlaka '
                                                  'yatırılarak yakın takip edilmelidir.',
                                'text': 'Hiçbir tetkik yapmadan hastayı 10 gün sonra poliklinik kontrolüne çağırıp '
                                        'taburcu etmek'}],
                 'question': 'HSP tanısı düşünülen ve şiddetli karın ağrısı ile kanaması olan bu çocukta en uygun '
                             'tetkik ve görüntüleme kombinasyonu hangisidir?',
                 'stage_title': 'Laboratuvar Analizi ve İnvajinasyon Dışlama Ultrasonografisi'},
               { 'options': [ { 'explanation': 'Trombositopeni olmaksızın palpabl purpura, kolik karın ağrısı, artrit '
                                               've hematüri Henoch-Schönlein Purpurası (IgA Vasküliti) tanı '
                                               'kriterleridir.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Henoch-Schönlein Purpurası (IgA Vasküliti) - Ciddi GİS ve '
                                               'Renal Tutulum.',
                                'text': 'Henoch-Schönlein purpurası vasküliti'},
                              { 'is_correct': False,
                                'scenario_update': "İTP'de trombosit sayısı derin düşüktür (<20.000/mm³) ve döküntüler "
                                                   'düz peteşidir; palpabl purpura ve artrit görülmez.',
                                'teaching_point': "İTP'de döküntüler düzdür (maküler); ele gelen (palpabl) purpura "
                                                  'vaskülite özgüdür.',
                                'text': 'İmmün trombositopenik purpura'},
                              { 'is_correct': False,
                                'scenario_update': 'Meningokoksemide toksik görünüm, fulminan septik şok, hipotansiyon '
                                                   've derin lökositoz vardır; bu çocuk hemodinamik stabildir.',
                                'teaching_point': 'Meningokoksemi fulminan sepsistir; HSP ise afebril veya subfebril, '
                                                  'stabil seyirli lökositoklastik vaskülittir.',
                                'text': 'Akut meningokoksemi sepsisi'},
                              { 'is_correct': False,
                                'scenario_update': "S-JİA'da haftalarca süren her gün pik yapan yüksek ateş, somon "
                                                   'renkli geçici döküntü ve hepatosplenomegali vardır.',
                                'teaching_point': 'JİA döküntüsü purpurik veya palpabl değildir; somon renkli '
                                                  'eritematöz makülerdir.',
                                'text': 'Sistemik jüvenil idiyopatik artrit'}],
                 'question': 'Palpabl purpura, normal trombosit, kolik karın ağrısı, artrit ve nefrit bulguları ile '
                             'kesin tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': "HSP'de şiddetli karın ağrısı, GİS kanaması veya belirgin nefritte "
                                               'sistemik kortikosteroidler (1-2 mg/kg/gün '
                                               'prednizolon/metilprednizolon) bağırsak ödemini ve ağrıyı hızla '
                                               'geriletir. Böbrek fonksiyonları ve kan basıncı yakından izlenmelidir.',
                                'is_correct': True,
                                'new_finding': 'IV metilprednizolon (1 mg/kg) başlandı ve hidrasyon sağlandı. 12 saat '
                                               'içinde çocuğun karın ağrısı belirgin geriledi, gaita kanaması durdu. '
                                               'Çocuk nefrolojisi ve pediatri servisinde kan basıncı ve idrar '
                                               'takibiyle izleme alındı.',
                                'text': 'Ciddi karın ağrısı ve kanama nedeniyle intravenöz metilprednizolon başlamak, '
                                        'hidrasyonu sağlamak ve nefroloji kontrolüyle yatırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Aspirin ve heparin vaskülitik bağırsak mukozasındaki kanamayı '
                                                   'masif hale getirerek hipovolemik şoka soktu.',
                                'teaching_point': 'Aktif GİS kanaması ve vasküliti olan çocukta antikoagülan veya '
                                                  'antiagregan ilaçlar ölümcül kanamalara yol açar.',
                                'text': 'Kortikosteroidlerin hiçbir faydası olmadığı gerekçesiyle hastaya sadece '
                                        'yüksek doz aspirin ve heparin infüzyonu başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Ağrısı dinmeyen çocukta beslenme yetersizliği ve devam eden '
                                                   'bağırsak duvarı iskemisi gelişti.',
                                'teaching_point': 'Şiddetli GİS tutulumu olan HSP olgularında kortikosteroidler ağrıyı '
                                                  'kesmede ve invajinasyonu önlemede etkilidir.',
                                'text': 'Tüm semptomların kendiliğinden geçmesini bekleyerek hastaya hiçbir analjezik '
                                        'veya antiinflamatuar vermeden taburcu etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'İnvajinasyon veya perforasyon yokken yapılan cerrahi çocukta '
                                                   'gereksiz morbiditeye yol açtı.',
                                'teaching_point': 'İnvajinasyon veya perforasyon gibi cerrahi bir komplikasyon '
                                                  'gelişmedikçe HSP medikal olarak tedavi edilir.',
                                'text': 'Hastaya acil tanısal laparatomi uygulayarak tüm bağırsak anslarını cerrahi '
                                        'olarak dışarı çıkarmak'}],
                 'question': 'İnvajinasyon dışlanan ancak şiddetli karın ağrısı ve kanaması süren bu çocukta en uygun '
                             'tedavi adımı hangisidir?',
                 'stage_title': 'Ciddi GİS Tutulumunda İmmünsüpresif Tedavi ve İzlem'}]},
  { 'age': '4 Aylık',
    'case_pearl': 'Pediatrik inguinal herniler patent processus vaginalis kaynaklı indirekt hernilerdir. Süt '
                  'çocuklarında inkarserasyon (fıtığın boğulması) riski çok yüksektir (%15-30). Bağırsak ansları dar '
                  'iç halkada sıkışır, venöz dönüş bozulur, ödem ve ardından arteriyel iskemi (strangülasyon) ve '
                  'gangren gelişir. Şiddetli ağrı, safralı kusma ve mekanik ileus eşlik eder. İlk 1-2 saatte '
                  'peritonit, şok veya ciltte morarma/nekroz yoksa analjezi/sedasyon verilip bacaklar fleksiyona '
                  'alınarak (taxis manevrası) nazikçe redüksiyon denenir. Redükte olursa ödem geçtikten 24-48 saat '
                  'sonra elektif ameliyat planlanır. Redükte olmazsa veya peritonit/nekroz varsa taxis denenmez; '
                  'DERHAL ACİL AMELİYAT şarttır.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Kasıkta aniden beliren, moraran, içeri itilemeyen sert şişlik, durdurulamaz ağlama ve safralı kusma',
    'disposition': 'Sarı Alanda Analjezi ve Sedasyon ile Nazik Redüksiyon Denemesi + Başarısızlıkta Acil Cerrahi '
                   'Herniyotomi',
    'final_diagnosis': 'İnkarsere ve Strangüle Sağ İnguinal Herni (Boğulmuş Kasık Fıtığı)',
    'gender': 'Erkek',
    'history': 'Dört aylık erkek bebek ailesi tarafından panik halinde Sarı Alana getiriliyor: Yaklaşık 2 saat önce '
               'altı değiştirilirken sağ kasığında ceviz büyüklüğünde sert bir şişlik fark edilmiş. Anne daha önce '
               'ağladığında çıkıp inen fıtığı olduğunu ancak bu kez içeri gitmediğini ve cildinin kızarmaya '
               'başladığını söylüyor. Bebek son yarım saattir durmaksızın tiz çığlıklarla ağlıyor ve iki kez yeşil '
               'safralı kusmuş.',
    'id': 'Y50',
    'steps': [ { 'options': [ { 'explanation': 'İnkarsere hernide kitlenin sertliği, hassasiyeti, cilt rengi ve '
                                               'redükte olup olmadığı değerlendirilmeli; bağırsak obstrüksiyonu ve '
                                               'peritonit bulguları araştırılmalıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.8°C, KTA 168/dk, SS 40/dk, TA 84/50 mmHg, SpO2 '
                                               '%98, KDZ 2.5 sn. Bebek aşırı ajite. Sağ kasık kanalından skrotuma '
                                               'uzanan, 3x2 cm boyutlarında, ileri derecede hassas, gergin, üzerindeki '
                                               'cilt hafif eritemli, içeriye itilemeyen (redükte olmayan) kitle. Batın '
                                               'hafif distandü; bağırsak sesleri tizleşmiş.',
                                'text': 'Kasık kitlesinin boyutunu, rengini, sıcaklığını, redükte edilebilirliğini ve '
                                        'batın obstrüksiyon bulgularını dikkatle incelemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Boğulmuş fıtık fark edilmediği için bağırsak ansındaki arteriyel '
                                                   'dolaşım tamamen durdu.',
                                'teaching_point': 'Ağrılı, aniden büyüyen, safralı kusma yapan kitle hidrosel olamaz; '
                                                  'inkarsere hernidir.',
                                'text': 'Şişliğin basit hidrosel olduğunu varsayıp kitleye hiç dokunmadan bebeğe oral '
                                        'sakinleştirici damla vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Aşırı kuvvet uygulaması iskemik bağırsak ansının fıtık kesesi '
                                                   'içinde yırtılmasına yol açtı.',
                                'teaching_point': 'İnkarsere hernide aşırı kaba kuvvet bağırsak perforasyonuna neden '
                                                  'olur; manevra nazik ve sedasyonla yapılmalıdır.',
                                'text': 'Fıtığı hemen içeri sokmak amacıyla kitleye başparmakla var gücüyle sertçe ve '
                                        'aniden bastırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gecikilen saatlerde bağırsak gangrenine bağlı peritonit ve septik '
                                                   'şok tablosu gelişti.',
                                'teaching_point': 'İnkarsere fıtık acil cerrahi tablodur; poliklinik randevusuna '
                                                  'bırakılması fatal sonuçlar doğurur.',
                                'text': 'Kasık kitlesinin lenf bezi olduğunu düşünüp hastayı bir hafta sonraki cerrahi '
                                        'polikliniğine yönlendirmek'}],
                 'question': 'Kasıkta şişlik, inatçı ağlama ve safralı kusması olan bu bebekte ilk fizik muayene '
                             'yaklaşımınız ne olmalıdır?',
                 'stage_title': 'Sarı Alanda Kasık Kitle Muayenesi ve İskemi Değerlendirmesi'},
               { 'options': [ { 'explanation': 'İnkarsere fıtıkta hasta oral alıma kapatılmalı (NPO), dehidratasyon '
                                               'düzeltilmeli ve redüksiyon veya cerrahi hazırlık için çocuk cerrahı '
                                               'derhal haberdar edilmelidir.',
                                'is_correct': True,
                                'new_finding': 'Damar yolu açıldı, 10 mL/kg SF verildi. Oral alım kapatıldı, '
                                               'nazogastrik sonda ile 20 mL safralı sıvı boşaltıldı. Acil '
                                               'skrotal/inguinal USG: Sağ inguinal kanalda sıkışmış bağırsak ansı, '
                                               'duvar ödemi ve venöz dönüş bozukluğu izlendi; perforasyon serbest '
                                               'sıvısı saptanmadı.',
                                'text': 'Damar yolu açıp izotonik sıvı başlatmak, oral alımı kesmek ve çocuk '
                                        'cerrahisini acil yatak başına çağırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tıkanıklık nedeniyle bebek baryumu kustu ve akciğerine aspire '
                                                   'ederek solunum durması yaşadı.',
                                'teaching_point': 'Mekanik tıkanıklıkta oral kontrast verilmesi aspirasyona yol açar; '
                                                  'KONTRENDİKEDİR.',
                                'text': 'Hastaya oral kontrastlı baryum içirerek baryumun kasıktan geçip geçmediğini '
                                        'grafilerle takip etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Süt içirilmesi mide basıncını ve kusmayı artırarak kasıktaki '
                                                   'boğulmayı daha da şiddetlendirdi.',
                                'teaching_point': 'Obstrükte hastanın beslenmesi kusma ve aspirasyon riskini artırır; '
                                                  'mutlak oral stop (NPO) kuraldır.',
                                'text': 'Hiç damar yolu açmadan bebeğe bol miktarda süt içirerek bağırsağın ağırlıkla '
                                        'aşağı inmesini denemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Bekletilen saatlerde bağırsak ansı nekroze oldu ve testis atrofisi '
                                                   'meydana geldi.',
                                'teaching_point': 'İnkarsere fıtık çocuk cerrahisinin acil müdahale alanıdır; vakit '
                                                  'kaybetmeden konsülte edilmelidir.',
                                'text': 'Çocuk cerrahisine haber vermeden hastayı acil serviste tek başına sabaha '
                                        'kadar uyumaya bırakmak'}],
                 'question': 'İnkarsere herni saptanan bu dehidrate bebekte muayenenin hemen ardından atılacak en '
                             'uygun klinik adım hangisidir?',
                 'stage_title': 'Cerrahi İletişim, Sıvı Resüsitasyonu ve Radyolojik Değerlendirme'},
               { 'options': [ { 'explanation': 'Kasık kanalında boğulmuş, redükte olmayan bağırsak ansı, kusma ve '
                                               'obstrüksiyon bulguları inkarsere inguinal herni tanısını koydurur.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: İnkarsere Sağ İndirekt İnguinal Herni.',
                                'text': 'İnkarsere sağ inguinal herni'},
                              { 'is_correct': False,
                                'scenario_update': 'Hidroselde kitle kistik, ağrısız ve transillüminasyon verir; '
                                                   'safralı kusma ve mekanik ileus yapmaz.',
                                'teaching_point': 'Hidroselde bağırsak obstrüksiyonu ve kusma olmaz; kitle fluktuan ve '
                                                  'ışıltılıdır.',
                                'text': 'Akut enfekte komünikan hidrosel'},
                              { 'is_correct': False,
                                'scenario_update': 'Lenfadenitte kasık kanalına uzanan obstrükte bağırsak ansı ve '
                                                   'safralı kusma görülmez.',
                                'teaching_point': 'Lenf bezi büyümesi safralı kusma ve mekanik bağırsak tıkanıklığı '
                                                  'tablosu oluşturmaz.',
                                'text': 'İzole akut inguinal lenfadenit'},
                              { 'is_correct': False,
                                'scenario_update': 'Testis torsiyonu skrotum içindedir; bu hastada patoloji sağ kasık '
                                                   'kanalında sıkışmış bağırsak fıtığıdır.',
                                'teaching_point': 'Fıtık kasık kanalından skrotuma inen bağırsak kitlesidir; '
                                                  'intratektal testis torsiyonu değildir.',
                                'text': 'Sol taraflı testis torsiyonu'}],
                 'question': "Kasıkta ağrılı, redükte olmayan gergin kitle, safralı kusma ve USG'de sıkışmış bağırsak "
                             'ansı ile kesin tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Strangülasyon ve peritonit bulgusu yoksa, analjezi/sedasyon '
                                               '(fentanil/midazolam) verilip kalça fleksiyona alınarak nazikçe taksis '
                                               'manevrası denenir. Redükte olursa 24-48 saat sonra elektif ameliyat '
                                               'planlanır; redüksiyon başarısızsa acil herniyotomi yapılır.',
                                'is_correct': True,
                                'new_finding': 'Hafif sedasyon ve analjezi altında bacaklar fleksiyona alınarak nazik '
                                               "taksis manevrası uygulandı. Bağırsak ansı hafif bir 'klik' sesiyle "
                                               'karın içine redükte oldu. Bebeğin ağrısı geçti, batını rahatladı. '
                                               'Ödemin gerilemesi için 24 saat gözlem ve ardından cerrahi planlandı.',
                                'text': 'Uygun analjezi ve sedasyon altında nazik taksis manevrası denemek, redükte '
                                        'olmazsa derhal acil ameliyathaneye almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Redükte edilmeden eve gönderilen bebekte birkaç saat içinde fıtık '
                                                   'strangüle oldu ve bağırsak delindi.',
                                'teaching_point': 'İnkarsere fıtık hastanede çözülmelidir; hasta redükte edilmeden '
                                                  'veya ameliyat edilmeden kesinlikle taburcu edilemez.',
                                'text': 'Redüksiyon denemeden bebeği eve gönderip fıtığın kendiliğinden içeri '
                                        'kaçmasını beklemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Uygunsuz cerrahi girişim fıtık kesesi içindeki bağırsağın '
                                                   'kesilmesine ve kontrolsüz kanamaya neden oldu.',
                                'teaching_point': 'Herniyotomi operasyonu ameliyathane şartlarında ve uzman cerrah '
                                                  'tarafından yapılmalıdır.',
                                'text': 'Kasık bölgesine kesi atarak acil serviste steril olmayan şartlarda fıtığı '
                                        'bistüri ile kesmeye çalışmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Üç gün aç bekleyen bebekte derin metabolik asidoz ve dehidratasyon '
                                                   'gelişti.',
                                'teaching_point': 'Fıtık redüksiyonu veya cerrahisi ilk saatlerde planlanır; günlerce '
                                                  'acilde bekletilemez.',
                                'text': 'Fıtığın üzerine buz torbası koyup bebeği 3 gün boyunca acil serviste aç '
                                        'bekletmek'}],
                 'question': 'Peritonit veya doku nekrozu bulgusu olmayan bu 4 aylık bebekte Sarı Alanda uygulanacak '
                             'en uygun yaklaşım hangisidir?',
                 'stage_title': 'Redüksiyon (Taksis) Girişimi ve Acil Ameliyat Kararı'}]}]
