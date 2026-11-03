# -*- coding: utf-8 -*-
YELLOW_CASES_PART1 = [{'id': 'Y01',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '14 Aylık',
  'gender': 'Kız',
  'complaint': 'Dirençli kusma, çok sayıda sulu dışkılama ve belirgin halsizlik',
  'history': "Annesi kucağında halsiz yatan bebeği Sarı Alana getiriyor: 'Dün geceden beri 10-12 kez kustu, "
             'ne içirsek hemen çıkarıyor. Bugün de bezinden taşacak şekilde 8 kez su gibi dışkıladı. '
             'Sabahtan beri bezini hiç ıslatmadı, ağlarken gözyaşı akmıyor, gözleri içine çöktü ve sürekli '
             "uyukluyor.'",
  'final_diagnosis': 'Akut Gastroenterit ve Orta-Ağır İzonatremik Dehidratasyon (Metabolik Asidozlu)',
  'disposition': 'Sarı Alanda İV İzotonik Bolus + Ondansetron + Rehidratasyon İzlemi Sonrası Oral Alımı '
                 'Açılıp Taburculuk',
  'case_pearl': 'Letarjiye eğilim, çökük göz küreleri, gözyaşı yokluğu, kuru mukozalar, deri turgorunda '
                'azalma, uzamış kapiller dolum ve anüri orta-ağır dehidratasyonu gösterir. Kan şekeri ve '
                'elektrolitler kontrol edilmeli, perfüzyon bozukluğu ve oral intolerans varlığında 20 mL/kg '
                '%0.9 NaCl İV bolus ve antiemetik olarak ondansetron ile rehidratasyon sağlanmalıdır.',
  'steps': [{'stage_title': 'Sarı Alanda İlk Değerlendirme ve Dolaşım Kontrolü',
             'question': 'Sarı Alana alınan bu 14 aylık bebekte ilk muayene ve yatak başı değerlendirmede '
                         'hangi yaklaşımı tercih edersiniz?',
             'options': [{'text': 'Öncelikle oral rehidratasyon sıvısını enjektörle beş dakikada bir küçük '
                                  'miktarlarda içirmeyi denemek ve kusup kusmayacağını iki saat boyunca '
                                  'yatak başında gözlemlemek',
                          'is_correct': False,
                          'scenario_update': 'Bebek verilen ilk 15 mL sıvıyı hemen fışkırır tarzda kustu; '
                                             'geçen sürede taşikardisi 178/dk düzeyine çıktı ve uykuya '
                                             'meyili belirginleşti.',
                          'teaching_point': 'Kapiller dolum süresi uzamış, letarjiye meyilli ve dirençli '
                                            'kusması olan bir süt çocuğunda doğrudan antiemetiksiz oral sıvı '
                                            'denemesi zaman kaybettirir ve perfüzyonu bozar.'},
                         {'text': 'Vital bulguları, kapiller dolum süresini, deri turgorunu, fontanel ve göz '
                                  'küresi çöküklüğünü, mukoza ıslaklığını değerlendirip parmak ucu kan '
                                  'şekeri ölçmek',
                          'is_correct': True,
                          'explanation': 'Tekrarlayan kusma, sulu dışkılama ve oral alım bozukluğu ile '
                                         'başvuran süt çocuğunda periferik perfüzyon, sıvı açığı bulguları '
                                         've kapiller glukoz düzeyi ilk dakikada değerlendirilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.8°C, KTA 164/dk, SS 38/dk, TA 80/48 mmHg, '
                                         'SpO2 %98. Bebek uykuya meyilli, uyaranla ağlıyor ancak gözyaşı '
                                         'yok. Göz küreleri ve ön fontanel çökük, ağız mukozası kuru, karın '
                                         'cildinde turgor azalmış, kapiller dolum süresi 3 saniye. Parmak '
                                         'ucu kan şekeri: 58 mg/dL. Tartı kaybı önceki ağırlığına göre %8.5 '
                                         'olarak hesaplandı.'},
                         {'text': 'Damar yolu açıp sıvı başlamadan önce invajinasyon veya ileus olasılığını '
                                  'dışlamak amacıyla ayakta direkt karın grafisi ve batın ultrasonografisi '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'Radyoloji ünitesinde sıra bekleyen bebeğin kapiller dolum '
                                             'süresi 4 saniyeye uzadı, ekstremiteleri soğudu ve kan şekeri '
                                             '46 mg/dL düzeyine geriledi.',
                          'teaching_point': 'Periferik perfüzyon bozukluğu ve sınırda hipoglisemisi olan '
                                            'bebek hemodinamik olarak stabilize edilmeden görüntüleme '
                                            'ünitesine gönderilmemelidir; ayrıca safrasız kusma ve sulu '
                                            'dışkılamada rutin grafi gerekmez.'},
                         {'text': 'Kusmayı hızlıca durdurmak amacıyla intramüsküler metoklopramid uygulayıp '
                                  'otuz dakika bekledikten sonra anne sütü ve su ile oral toleransı test '
                                  'etmek',
                          'is_correct': False,
                          'scenario_update': 'Enjeksiyondan yirmi dakika sonra bebekte boyunda kasılma, '
                                             'gözlerin yukarı kayması (okülojirik kriz) gelişti ve dolaşım '
                                             'bulguları daha da bozuldu.',
                          'teaching_point': 'Süt çocukları ve küçük çocuklarda metoklopramid akut distonik '
                                            'reaksiyon ve ekstrapiramidal yan etki riski nedeniyle '
                                            'kullanılmamalı; ayrıca dolaşım bozukluğu varken İM ilaç yerine '
                                            'damar yolu tercih edilmelidir.'}]},
            {'stage_title': 'Acil Tetkik ve İlk Saat Stabilizasyon Planı',
             'question': 'Taşikardisi (164/dk), kapiller dolum süresi 3 saniye, kan şekeri 58 mg/dL ve '
                         'dirençli kusması olan bu bebekte ilk müdahale ve tetkik planınız ne olmalıdır?',
             'options': [{'text': 'Damar yolu açıp %5 dekstroz ve %0.2 NaCl içeren hipotonik sıvıdan 20 '
                                  'mL/kg hızlı intravenöz bolus vermek ve bazal biyokimya tetkiklerini '
                                  'göndermek',
                          'is_correct': False,
                          'scenario_update': 'Hızlı verilen hipotonik sıvı intravasküler alanda kalmayıp '
                                             'hücre içine geçti; kapiller dolum süresi düzelmediği gibi '
                                             'kontrol sodyum değeri 129 mEq/L düzeyine düştü.',
                          'teaching_point': 'İntravasküler hacim genişletme (bolus) işlemi asla hipotonik '
                                            'sıvılarla (%5 dekstroz veya %0.2 NaCl) yapılmaz; akut '
                                            'hiponatremi ve beyin ödemine yol açabilir.'},
                         {'text': 'Kan gazı ve elektrolit tetkiklerini gönderip sonuçlar çıkana kadar sıvı '
                                  'vermeden beklemek, saptanan asidozu düzeltmek amacıyla intravenöz sodyum '
                                  'bikarbonat puşelemek',
                          'is_correct': False,
                          'scenario_update': 'Sonuç beklenirken bebeğin perfüzyonu daha da bozuldu; sıvı '
                                             'açığı yerine konmadan verilen sodyum bikarbonat sonrası serum '
                                             'potasyumu 2.9 mEq/L düzeyine geriledi.',
                          'teaching_point': 'Dolaşım bozukluğu bulguları varken laboratuvar sonuçları '
                                            'beklenmeden izotonik kristaloid bolusu başlanmalıdır; dışkıyla '
                                            'bikarbonat kaybına ve hipoperfüzyona bağlı asidoz hidrasyonla '
                                            'düzelir, rutin bikarbonat verilmez.'},
                         {'text': 'Kan gazı ve biyokimya alıp 20 mL/kg %0.9 NaCl intravenöz bolus, ardından '
                                  'dekstrozlu rehidratasyon sıvısı ve ondansetron uygulamak',
                          'is_correct': True,
                          'explanation': 'Perfüzyon bozukluğu ve sıvı açığı olan bebekte ilk adım 20 mL/kg '
                                         'izotonik kristaloid bolusu ile dolaşımı desteklemek, ardından '
                                         'dekstroz içeren rehidratasyon sıvısına geçmek ve ondansetron ile '
                                         'kusmayı kontrol etmektir.',
                          'new_finding': 'Laboratuvar: Kan gazında pH 7.28, pCO2 28 mmHg, HCO3 13 mmol/L, '
                                         'baz açığı -11 mmol/L, laktat 2.6 mmol/L; biyokimyada Na 136 mEq/L, '
                                         'K 3.9 mEq/L, Cl 108 mEq/L, üre 54 mg/dL, kreatinin 0.65 mg/dL. 20 '
                                         'mL/kg %0.9 NaCl bolusu, ardından %5 dekstrozlu izotonik sıvı ve '
                                         '0.15 mg/kg ondansetron sonrası KTA 128/dk, kapiller dolum süresi '
                                         '1.5 saniye ve kan şekeri 96 mg/dL ölçüldü.'},
                         {'text': 'Nazogastrik sonda yerleştirerek saatte 50 mL/kg hızında yüksek hacimli '
                                  'oral rehidratasyon solüsyonu infüzyonu başlatmak ve antiemetik ilaç '
                                  'kullanımından kaçınmak',
                          'is_correct': False,
                          'scenario_update': 'Yüksek hızda verilen enteral sıvı mide distansiyonuna ve '
                                             'tekrarlayan kusmaya yol açtı; periferik perfüzyon bozukluğu ve '
                                             'taşikardi gerilemedi.',
                          'teaching_point': 'Kapiller dolum uzaması, letarji eğilimi ve sınırda hipoglisemi '
                                            'varken başlangıçta hızlı intravenöz izotonik bolus tercih '
                                            'edilmeli; nazogastrik rehidratasyon perfüzyonu stabil '
                                            'hastalarda daha düşük hızda uygulanmalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Mevcut klinik bulgular ve laboratuvar sonuçlarıyla (Na 136 mEq/L, pH 7.28, HCO3 13 '
                         'mmol/L) bu hastada kesin tanınız nedir?',
             'options': [{'text': 'Akut Gastroenterit ve Orta-Ağır İzonatremik Dehidratasyon',
                          'is_correct': True,
                          'explanation': 'Yaklaşık %8-9 tartı kaybı, uzamış kapiller dolum ve letarji '
                                         'eğilimi orta-ağır dehidratasyonu; serum sodyumunun 135-145 mEq/L '
                                         'arasında olması izonatremik tabloyu ve dışkıyla bikarbonat kaybı '
                                         'ise normal anyon açıklı metabolik asidozu gösterir.',
                          'new_finding': 'Klinik tanı: Akut Gastroenterit, Orta-Ağır İzonatremik '
                                         'Dehidratasyon ve Metabolik Asidoz.'},
                         {'text': 'Akut Gastroenterit ve Ağır Hipernatremik Dehidratasyon',
                          'is_correct': False,
                          'scenario_update': 'Hastanın serum sodyum düzeyi 136 mEq/L olup normal referans '
                                             'aralığındadır; hipernatremi saptanmamıştır.',
                          'teaching_point': 'Hipernatremik dehidratasyon tanısı için serum sodyum düzeyinin '
                                            '150 mEq/L üzerinde olması gerekir; bu hastada su ve tuz dengeli '
                                            'kaybedildiği için tablo izonatremiktir.'},
                         {'text': 'Yeni Tanı Diyabetik Ketoasidoz ve Hipovolemi',
                          'is_correct': False,
                          'scenario_update': 'Hastanın başvuru kan şekeri 58 mg/dL olup hiperglisemi, '
                                             'glukozüri veya ketonemi bulunmamaktadır.',
                          'teaching_point': 'Diyabetik ketoasidozda belirgin hiperglisemi (>200 mg/dL) ve '
                                            'ketonemi vardır; süt çocuklarında akut ishal ve kusmada ise '
                                            'açlığa bağlı hipoglisemi eğilimi ve bikarbonat kaybına bağlı '
                                            'asidoz görülür.'},
                         {'text': 'Akut İnvajinasyon ve Dekompanse Septik Şok',
                          'is_correct': False,
                          'scenario_update': 'Kusmalar safrasızdır, kolik tarzda ağlama krizleri veya '
                                             'kanlı-mukuslu dışkılama yoktur ve tek doz sıvı bolusu ile '
                                             'hemodinami hızla düzelmiştir.',
                          'teaching_point': 'İnvajinasyonda aralıklı şiddetli karın ağrısı, safralı kusma ve '
                                            'çilek jölesi dışkılama beklenir; sık sulu dışkılama ve '
                                            'rehidratasyonla hızla düzelen tablo akut gastroenteriti '
                                            'destekler.'}]},
            {'stage_title': 'Sarı Alan İzlem ve Taburculuk Kararı',
             'question': 'Sarı Alanda 6 saatlik intravenöz rehidratasyon sonrası bilinci tamamen açılan, bol '
                         'idrar çıkışı olan ve oral rehidratasyon sıvısı ile anne sütünü kusmadan alan '
                         'hastada yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'İshal tamamen durana kadar anne sütünü ve katı gıdaları kesip yalnızca '
                                  'pirinç lapası ve elma suyu içeren kısıtlı diyetle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Anne sütünün kesilmesi ve düşük kalorili kısıtlı diyet '
                                             'verilmesi enterosit yenilenmesini geciktirerek ishal süresinin '
                                             'uzamasına ve kilo kaybına yol açtı.',
                          'teaching_point': 'ESPGHAN kılavuzuna göre akut gastroenteritte rehidratasyon '
                                            'tamamlanır tamamlanmaz anne sütüne ve çocuğun yaşına uygun '
                                            'normal beslenmeye kesintisiz devam edilmelidir; kısıtlı BRAT '
                                            'diyeti önerilmez.'},
                         {'text': 'Bağırsak motilitesini azaltarak sıvı kaybını durdurmak amacıyla oral '
                                  'loperamid ve ampirik oral siprofloksasin reçete ederek hastayı evine '
                                  'taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Verilen antimotilite ilaç sonrası bebekte batın distansiyonu, '
                                             'paralitik ileus ve letarji gelişti; hasta tekrar acil servise '
                                             'getirildi.',
                          'teaching_point': 'Çocuklarda akut gastroenteritte loperamid gibi antimotilite '
                                            'ilaçlar paralitik ileus, toksik megakolon ve santral sinir '
                                            'sistemi depresyonu riski nedeniyle kesinlikle kontrendikedir; '
                                            'sulu ishalde rutin antibiyotik verilmez.'},
                         {'text': 'Klinik düzelmeye rağmen metabolik asidoz öyküsü nedeniyle hastayı en az '
                                  '48 saat daha parenteral sıvı almak üzere servise yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Oral alımı tamamen açılan ve hidrasyonu düzelen bebeğin '
                                             'gereksiz yatışı hastane enfeksiyonu riskini artırdı ve yatak '
                                             'kapasitesini bloke etti.',
                          'teaching_point': 'Sarı Alanda 4-6 saatlik rehidratasyon sonrası vital bulguları '
                                            've diürezi normale dönen, oral sıvıyı ve beslenmeyi kusmadan '
                                            'tolere eden hastalar güvenle taburcu edilebilir.'},
                         {'text': 'Sulu dışkılama sonrası oral rehidratasyon sıvısı, çinko desteği, anne '
                                  'sütüne devam ve kırmızı bayrak eğitimi ile taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Hidrasyonu düzelen, diürezi başlayan ve oral alımı kusmadan tolere '
                                         'eden bebeklerde devam eden kayıplar için ORS, 10-14 gün çinko '
                                         'takviyesi, kesintisiz beslenme ve aile eğitimi ile taburculuk '
                                         'standart yaklaşımdır.',
                          'new_finding': 'Hasta oral rehidratasyon sıvısı, çinko desteği ve yeniden başvuru '
                                         'kriterleri anlatılarak Sarı Alandan şifa ile taburcu edildi.'}]}]},
 {'id': 'Y02',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '20 Aylık',
  'gender': 'Erkek',
  'complaint': 'Yüksek ateş sırasında evde 2 dakika süren tüm vücutta kasılma ve gözlerini dikme',
  'history': "Ailesi panikle Sarı Alana getiriyor: 'Bugün sabahtan beri burnu akıyordu ve ateşi çıktı. Yarım "
             'saat önce evde ateşi 39.4°C iken bir anda gözlerini yukarı dikti, dudakları morardı ve iki '
             'kolu ile bacağı simetrik olarak kasılmaya başladı. Yaklaşık 2 dakika sürdü ve kendiliğinden '
             'durdu. Ambulansta gelirken biraz uyukladı ama şimdi bizi tanıyor ve ağlıyor. Daha önce hiç '
             "nöbet geçirmedi.'",
  'final_diagnosis': 'Basit Febril Konvülziyon (Viral Üst Solunum Yolu Enfeksiyonu Zemininde)',
  'disposition': 'Sarı Alanda Ateş Kontrolü, Odak Muayenesi ve Gözlem Sonrası Aile Eğitimi ile Taburculuk',
  'case_pearl': '6 ay - 5 yaş arası çocuklarda merkezi sinir sistemi enfeksiyonu veya metabolik bozukluk '
                'olmaksızın ateşle birlikte gelişen, jeneralize, 15 dakikadan kısa süren ve 24 saat içinde '
                'tekrarlamayan nöbetler Basit Febril Konvülziyondur. Bilinci hızla normale dönen, meninks '
                'irritasyon bulgusu olmayan tam aşılı çocukta rutin lomber ponksiyon, EEG, kraniyal '
                'görüntüleme veya sürekli antiepileptik ilaç önerilmez.',
  'steps': [{'stage_title': 'Sarı Alanda Akut Değerlendirme ve Nörolojik Muayene',
             'question': 'Kasılması durmuş olarak Sarı Alana getirilen bu 20 aylık çocukta ilk '
                         'değerlendirmede nasıl bir yaklaşım izlemelisiniz?',
             'options': [{'text': 'Tekrar kasılma gelişmesini önlemek amacıyla hemen damar yolu açarak '
                                  'intravenöz diazepam uygulamak ve ardından yirmi dakikada fenitoin yükleme '
                                  'dozuna başlamak',
                          'is_correct': False,
                          'scenario_update': 'Aktif nöbeti olmayan çocuğa uygulanan intravenöz diazepam ve '
                                             'fenitoin sonrası çocukta derin sedasyon gelişti; nörolojik '
                                             'bilinç takibi bozuldu ve solunumu yüzeyelleşti.',
                          'teaching_point': 'Antikonvülzan ilaçlar yalnızca aktif devam eden (5 dakikayı '
                                            'aşan) nöbetleri sonlandırmak için uygulanır; nöbeti durmuş ve '
                                            'bilinci açılmış hastaya acilde profilaktik yükleme yapılmaz.'},
                         {'text': 'Ayrıntılı fizik muayene ve odak araması yapmadan önce santral sinir '
                                  'sistemi enfeksiyonunu dışlamak amacıyla çocuğu doğrudan lomber ponksiyon '
                                  'işlemine almak',
                          'is_correct': False,
                          'scenario_update': 'Bilinci açık, aktif ve huzursuz çocukta muayene edilmeden '
                                             'girişilen işlem ailede yoğun panik yarattı ve travmatik '
                                             'ponksiyonla sonuçlandı.',
                          'teaching_point': 'Ateş ve nöbetle başvuran çocukta öncelikle bilinç durumu, '
                                            'meninks irritasyon bulguları, fokal nörolojik muayene, aşı '
                                            'öyküsü ve ateş odağı değerlendirilmelidir.'},
                         {'text': 'Vital bulguları, kapiller kan şekerini, bilinç durumunu, fokal nörolojik '
                                  'defisit ve meninks irritasyon bulgularını değerlendirip ateş odağı '
                                  'muayenesi yapmak',
                          'is_correct': True,
                          'explanation': 'Ateşle birlikte kısa süreli nöbet geçiren çocukta en önemli ilk '
                                         'adım yaşamsal bulguları, kan şekerini, bilinç düzeyini, meninks '
                                         'irritasyon bulgularını ve ateşin kaynağını değerlendirmektir.',
                          'new_finding': 'Vital Bulgular: Ateş 39.1°C, KTA 135/dk, SS 26/dk, SpO2 %99, '
                                         'kapiller kan şekeri 104 mg/dL. Çocuk uyanık, annesiyle göz teması '
                                         'kuruyor, GKS 15. Ense sertliği yok, Brudzinski ve Kernig bulguları '
                                         'negatif, ekstremite kas güçleri simetrik ve fokal defisit yok. '
                                         'Otoskopi doğal, orofarenks hiperemik ve seröz burun akıntısı '
                                         'mevcut. Ulusal aşı takvimine göre tüm aşıları tam.'},
                         {'text': 'Vücut ısısını hızla düşürerek yeni bir atağı engellemek amacıyla soğuk su '
                                  'kompresi uygulamak ve intramüsküler metamizol sodyum enjeksiyonu yapmak',
                          'is_correct': False,
                          'scenario_update': 'Soğuk su uygulaması periferik vazokonstriksiyon ve titreme '
                                             'yaratarak çocuğun huzursuzluğunu artırdı; metamizol '
                                             'enjeksiyonu ise hipotansiyon ve agranülositoz riski taşıdığı '
                                             'için uygunsuzdu.',
                          'teaching_point': 'Ateş kontrolünde soğuk su veya alkol uygulaması titreme ve '
                                            'vazokonstriksiyonla merkezi ısıyı artırır; çocuklarda ilk '
                                            'tercih oral veya rektal parasetamol ya da ibuprofendir.'}]},
            {'stage_title': 'Tetkik ve Görüntüleme Kararı',
             'question': '20 aylık, aşıları tam, bilinci tamamen açılmış, meninks irritasyon bulgusu olmayan '
                         've üst solunum yolu enfeksiyonu saptanan bu çocukta hangi tetkik yaklaşımı '
                         'doğrudur?',
             'options': [{'text': 'Rutin lomber ponksiyon, kraniyal bilgisayarlı tomografi veya acil '
                                  'elektroensefalografi istemeden oral antipiretik verip Sarı Alanda klinik '
                                  'gözleme almak',
                          'is_correct': True,
                          'explanation': 'AAP kılavuzuna göre 18 aydan büyük, tam aşılı, bilinci tamamen '
                                         'normale dönmüş ve meninks irritasyon bulgusu olmayan ilk kısa '
                                         'jeneralize ateşli nöbette rutin LP, nörogörüntüleme, EEG veya '
                                         'geniş biyokimya endike değildir.',
                          'new_finding': '15 mg/kg oral parasetamol verildi. İzlemin 1. saatinde ateş 37.6°C '
                                         'düzeyine geriledi, çocuk Sarı Alan yatağında su içti ve '
                                         'oyuncaklarıyla oynamaya başladı.'},
                         {'text': 'İntrakraniyal yer kaplayıcı lezyon veya ödem olasılığını dışlamak '
                                  'amacıyla acil kontrastsız kraniyal bilgisayarlı tomografi ve rutin '
                                  'biyokimya istemek',
                          'is_correct': False,
                          'scenario_update': 'Çekilen kraniyal BT ve bakılan serum elektrolitleri tamamen '
                                             'normal saptandı; çocuk gelişmekte olan beyni için gereksiz '
                                             'iyonizan radyasyona maruz kaldı.',
                          'teaching_point': 'Fokal özelliği olmayan, 15 dakikadan kısa süren ve nörolojik '
                                            'muayenesi normal olan ilk ateşli nöbette intrakraniyal patoloji '
                                            'saptanma olasılığı çok düşüktür; rutin kraniyal BT çekilmez.'},
                         {'text': 'Klinik muayenesi normal olsa bile yirmi dört aylıktan küçük tüm ateşli '
                                  'nöbet hastalarında zorunlu olarak lomber ponksiyon ve kan kültürü yapmak',
                          'is_correct': False,
                          'scenario_update': 'Yapılan lomber ponksiyonda BOS hücre sayımı, protein ve glukoz '
                                             'değerleri tamamen normal geldi; invaziv işlem çocukta ve '
                                             'ailede gereksiz travma yarattı.',
                          'teaching_point': 'Haemophilus influenzae tip b ve pnömokok aşıları tam olan, '
                                            '12-18 ay üzerindeki ve menenjit bulgusu taşımayan çocuklarda '
                                            'rutin lomber ponksiyon önerilmemektedir.'},
                         {'text': 'İleride gelişebilecek epilepsi riskini öngörmek ve antiepileptik tedavi '
                                  'kararını netleştirmek için taburculuk öncesi acil uyku-uyanıklık '
                                  'elektroensefalografisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Acil koşullarda çekilen EEG postiktal dönemde nonspesifik '
                                             'hafif yavaşlama gösterdi; bu bulgu epilepsi gelişimini '
                                             'öngörmediği halde ailenin kaygısını artırdı.',
                          'teaching_point': 'Kısa süreli jeneralize ateşli nöbet sonrasında erken dönemde '
                                            'yapılan EEG gelecekteki nöbet tekrarını veya epilepsi '
                                            'gelişimini öngörmez ve tedavi kararını değiştirmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik seyri ve muayene bulguları değerlendirildiğinde bu hastada kesin tanınız '
                         'nedir?',
             'options': [{'text': 'Komplike Febril Konvülziyon',
                          'is_correct': False,
                          'scenario_update': 'Nöbet fokal başlamadı, 15 dakikadan uzun sürmedi ve 24 saat '
                                             'içinde tekrarlamadı.',
                          'teaching_point': 'Komplike febril konvülziyon diyebilmek için nöbetin fokal '
                                            'olması, 15 dakikadan uzun sürmesi veya aynı 24 saat içinde '
                                            'tekrarlaması gerekir.'},
                         {'text': 'Akut Bakteriyel Menenjit',
                          'is_correct': False,
                          'scenario_update': 'Çocuğun bilinci hızla açıldı, meninks irritasyon bulgusu yok '
                                             've ateş düştüğünde genel durumu tamamen normal.',
                          'teaching_point': 'Akut bakteriyel menenjitte letarji, huzursuzluk, ense sertliği '
                                            'veya toksik görünüm ateş düşse dahi devam eder.'},
                         {'text': 'Dravet Sendromu (Ağır Miyoklonik Epilepsi)',
                          'is_correct': False,
                          'scenario_update': 'İlk kez 20 aylıkken geçirilen 2 dakikalık tek jeneralize nöbet '
                                             'Dravet sendromu kriterleriyle uyumlu değildir.',
                          'teaching_point': 'Dravet sendromu genellikle yaşamın ilk yılında başlayan, uzamış '
                                            'hemiklonik veya jeneralize ateşli nöbetler ve gelişim geriliği '
                                            'ile seyreden nadir bir genetik epilepsidir.'},
                         {'text': 'Basit Febril Konvülziyon',
                          'is_correct': True,
                          'explanation': '6 ay - 5 yaş arasında, santral sinir sistemi enfeksiyonu '
                                         'olmaksızın ateşle tetiklenen, jeneralize, 15 dakikadan kısa süren '
                                         've 24 saatte tekrarlamayan nöbet Basit Febril Konvülziyondur.',
                          'new_finding': 'Klinik tanı: Basit Febril Konvülziyon.'}]},
            {'stage_title': 'Sarı Alan Gözlem Süresi ve Taburculuk Planı',
             'question': 'Sarı Alanda 4 saat izlenen, ateşi kontrol altına alınan, aktif oynayan ve nöbeti '
                         'tekrarlamayan bu hastada taburculuk yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Nöbet tekrarını önlemek amacıyla iki yıl boyunca düzenli kullanılmak '
                                  'üzere günlük oral sodyum valproat veya fenobarbital profilaksisi '
                                  'başlayarak taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Başlanan kronik antiepileptik ilaç çocukta sersemlik, davranış '
                                             'değişikliği ve karaciğer enzim yüksekliği riski oluştururken '
                                             'epilepsi gelişme riskini değiştirmedi.',
                          'teaching_point': 'Basit febril konvülziyonda sürekli antiepileptik ilaçların '
                                            'olası yan etkileri (hepatotoksisite, bilişsel etkilenme) '
                                            'potansiyel yararından çok daha fazladır ve kesinlikle '
                                            'önerilmez.'},
                         {'text': 'Antiepileptik başlamadan; aileye tablonun iyi huylu doğasını, tekrarlama '
                                  'riskini ve nöbet anında güvenli yan pozisyon ilk yardımını anlatarak '
                                  'taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Basit febril konvülziyonda en etkin yaklaşım ailenin '
                                         'bilgilendirilmesi, nöbet anında güvenli yan pozisyon (ağıza cisim '
                                         'sokmama, >5 dk sürerse 112 arama) eğitimi ve semptomatik ateş '
                                         'yönetimidir.',
                          'new_finding': 'Aileye detaylı nöbet ilk yardım eğitimi verildi ve yazılı '
                                         'bilgilendirme formu ile hasta Sarı Alandan güvenle taburcu '
                                         'edildi.'},
                         {'text': 'Her ateşli enfeksiyon başladığında kırk sekiz saat boyunca sekiz saatte '
                                  'bir düzenli oral diazepam verilmesini ve dönüşümlü antipiretik '
                                  'kullanılmasını reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Aralıklı oral diazepam kullanımı çocukta belirgin ataksi ve '
                                             'uykuya meyil yaparak olası bir santral sinir sistemi '
                                             'enfeksiyonunun klinik takibini maskeledi.',
                          'teaching_point': 'Ateşli dönemlerde rutin aralıklı oral diazepam profilaksisi '
                                            'sedasyon ve ataksi yaparak menenjit bulgularını '
                                            'maskeleyebileceğinden ilk basit febril konvülziyonda rutin '
                                            'önerilmez; antipiretikler de nöbet tekrarını önlemez.'},
                         {'text': 'İlk yirmi dört saatlik dönemde nöbetin tekrarlama olasılığına karşı damar '
                                  'yolunu açık tutarak hastayı çocuk nöroloji servisine yatırıp monitörize '
                                  'izlemek',
                          'is_correct': False,
                          'scenario_update': 'Bilinci tamamen normal olan ve ek risk faktörü taşımayan '
                                             'çocukta servis yatışı gereksiz hastane stresine yol açtı.',
                          'teaching_point': 'Acil gözlemde (Sarı Alan) birkaç saat izlenen, bilinci tam '
                                            'açık, nörolojik muayenesi doğal ve ateş odağı belli olan basit '
                                            'febril konvülziyon hastalarında hastane yatışı gerekmez.'}]}]},
 {'id': 'Y03',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '16 Aylık',
  'gender': 'Kız',
  'complaint': 'Ateşle birlikte 18 dakikadır devam eden, özellikle sağ kol ve bacakta belirgin ritmik '
               'kasılma',
  'history': "112 ambulansı ile Sarı Alana kasılmaları devam ederken getiriliyor: 'Evde 18 dakika önce ateşi "
             '39.6°C iken gözleri sağa kaydı ve özellikle sağ kolu ile sağ bacağında ritmik atmalar başladı. '
             "Yolda da hiç durmadı, bilinci kapalı!' Özgeçmişinde bilinen bir hastalık veya travma öyküsü "
             'yok.',
  'final_diagnosis': 'Komplike Febril Konvülziyon (Febril Status Epileptikus)',
  'disposition': 'Sarı Alanda Akut Antikonvülzan Müdahale, Santral Sinir Sistemi Enfeksiyonu Dışlanması ve '
                 'Çocuk Servisi Yatışı',
  'case_pearl': '5 dakikayı aşan her nöbet uzamış nöbet / erken status epileptikus kabul edilerek acil '
                'benzodiazepin (İV lorazepam/diazepam veya damar yolu yoksa İM/bukkal/nazal midazolam) ile '
                'durdurulmalıdır. Fokal olan ve 15 dakikadan uzun süren ateşli nöbet Komplike Febril '
                'Konvülziyondur; santral sinir sistemi enfeksiyonu (bakteriyel menenjit / HSV ensefaliti) '
                'dışlanmalı ve hasta yatırılarak izlenmelidir.',
  'steps': [{'stage_title': 'Aktif Kasılmaya İlk Beş Dakika Müdahalesi',
             'question': 'On sekiz dakikadır sağ yan ağırlıklı kasılması devam eden bu 16 aylık çocukta ilk '
                         'yapmanız gereken acil müdahale nedir?',
             'options': [{'text': 'Hava yolu açıklığını sağlayıp oksijen vermek, kapiller kan şekeri bakmak '
                                  've damar yolu açarak intravenöz midazolam veya diazepam uygulamak',
                          'is_correct': True,
                          'explanation': '5 dakikayı aşan aktif nöbette ilk basamak hava yolu ve '
                                         'oksijenizasyonun sağlanması, hipogliseminin hızla dışlanması ve '
                                         'birinci basamak hızlı etkili benzodiazepin uygulanmasıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 39.5°C, KTA 170/dk, rezervuarlı maske oksijen '
                                         'ile SpO2 %97, kapiller kan şekeri 112 mg/dL. İV 0.2 mg/kg '
                                         'midazolam uygulandıktan 2 dakika sonra sağ yanlı kasılmalar durdu. '
                                         'Postiktal dönemde çocuk uykuya meyilli ve sağ üst ekstremitesini '
                                         'sola kıyasla daha az hareket ettiriyor.'},
                         {'text': 'Benzodiazepinlerin olası solunum depresyonu riskinden kaçınmak amacıyla '
                                  'ilk basamakta doğrudan intravenöz levetirasetam veya fenitoin infüzyonu '
                                  'başlatıp yirmi dakika beklemek',
                          'is_correct': False,
                          'scenario_update': 'İnfüzyon süresince aktif kasılma devam etti; nöbet süresi otuz '
                                             'dakikayı aşarak hipoksi ve metabolik asidoz derinleşti.',
                          'teaching_point': 'İkinci basamak antiepileptikler (fenitoin, levetirasetam, '
                                            'valproat) infüzyon süresi gerektirdiğinden aktif nöbeti hızlıca '
                                            'sonlandıramaz; ilk basamakta mutlaka hızlı etkili benzodiazepin '
                                            'verilmelidir.'},
                         {'text': 'Yüksek ateşi hızla düşürerek kasılmayı sonlandırmak amacıyla intravenöz '
                                  'parasetamol infüzyonu ve ılık uygulama başlatıp on dakika klinik yanıt '
                                  'beklemek',
                          'is_correct': False,
                          'scenario_update': 'Antipiretik infüzyonuna rağmen sağ yanlı klonik atmalar '
                                             'kesilmedi, hastada siyanoz ve orofaringeal sekresyon birikimi '
                                             'gelişti.',
                          'teaching_point': 'Antipiretik ilaçlar devam eden aktif konvülziyonu durduramaz; 5 '
                                            'dakikayı geçen her nöbette zaman kaybetmeden antikonvülzan '
                                            'müdahale yapılmalıdır.'},
                         {'text': 'Sağ yanlı fokal kasılma nedeniyle intrakraniyal patolojiyi dışlamak '
                                  'amacıyla antikonvülzan vermeden önce çocuğu acil kraniyal bilgisayarlı '
                                  'tomografi çekimine göndermek',
                          'is_correct': False,
                          'scenario_update': 'Aktif kasılması sürerken radyoloji ünitesine nakledilen '
                                             'çocukta tomografi masasında desatürasyon ve aspirasyon '
                                             'gelişti.',
                          'teaching_point': 'Aktif nöbet geçiren hasta hava yolu güvenliği sağlanmadan ve '
                                            'nöbeti antikonvülzan ilaçla durdurulmadan kesinlikle '
                                            'görüntüleme ünitesine gönderilmez.'}]},
            {'stage_title': 'Postiktal Değerlendirme ve Tetkik Planı',
             'question': 'Sağ yan ağırlıklı 18 dakika süren kasılması durdurulan ve sağ kolunda geçici '
                         'güçsüzlük izlenen 16 aylık bu ateşli çocukta bir sonraki yaklaşımınız ne '
                         'olmalıdır?',
             'options': [{'text': 'Kasılma durduğu ve vital bulgular stabilize olduğu için ek laboratuvar '
                                  'tetkiki veya görüntüleme yapmadan antipiretik reçete ederek iki saat '
                                  'sonra taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Taburculuktan dört saat sonra çocuk evde tekrar sağ yanlı '
                                             'durdurulamayan kasılma ve bilinç kaybı ile yoğun bakıma kabul '
                                             'edildi.',
                          'teaching_point': '15 dakikayı aşan ve fokal özellik gösteren ateşli nöbetlerde '
                                            'altta yatan santral sinir sistemi enfeksiyonu veya yapısal '
                                            'patoloji mutlaka araştırılmalı, hasta erken taburcu '
                                            'edilmemelidir.'},
                         {'text': 'Postiktal fokal nörolojik bulguya rağmen kraniyal görüntüleme yapmadan '
                                  'hemen yatak başında lomber ponksiyon uygulamak ve ampirik oral '
                                  'antibiyotik tedavisi başlamak',
                          'is_correct': False,
                          'scenario_update': 'Fokal defisiti olan hastada görüntüleme öncesi yapılan lomber '
                                             'ponksiyon herniasyon riski taşıdığı gibi, olası santral sinir '
                                             'sistemi enfeksiyonunda oral antibiyotik yetersiz kaldı.',
                          'teaching_point': 'Postiktal fokal nörolojik defisiti ve uzamış fokal nöbeti olan '
                                            'hastada lomber ponksiyon öncesinde yer kaplayıcı lezyon veya '
                                            'ödemi dışlamak için acil kraniyal görüntüleme yapılmalıdır.'},
                         {'text': 'Elektrolit, kan gazı, hemogram, CRP ve kan kültürü alıp fokal bulgu '
                                  'nedeniyle acil kraniyal görüntüleme yapmak ve santral enfeksiyonu '
                                  'araştırmak',
                          'is_correct': True,
                          'explanation': 'Uzamış ve fokal karakterli ateşli nöbet sonrası sağ kolda '
                                         'güçsüzlük varlığında metabolik nedenler, akut bakteriyel menenjit, '
                                         'herpes ensefaliti ve intrakraniyal patolojiler titizlikle '
                                         'araştırılmalıdır.',
                          'new_finding': 'Laboratuvar: Na 137 mEq/L, K 4.2 mEq/L, Ca 9.6 mg/dL, Mg 2.1 '
                                         'mg/dL, WBC 14.200/mm³, CRP 22 mg/L. Acil kraniyal görüntülemede '
                                         'kitle, kanama veya şift saptanmadı. İzlemin 2. saatinde sağ '
                                         'koldaki güçsüzlük tamamen düzeldi ve bilinci açıldı; lomber '
                                         'ponksiyon değerlendirmesi yapıldı.'},
                         {'text': 'Sağ koldaki hareket azlığını nöbet sırasındaki omuz çıkığı veya kırığa '
                                  'bağlayarak iki yönlü sağ üst ekstremite grafisi ve ortopedi görüşü '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'Çekilen omuz ve kol grafileri tamamen normal saptandı; sağ '
                                             'koldaki güçsüzlük iki saat içinde kendiliğinden geriledi ancak '
                                             'asıl nörolojik tetkikler gecikti.',
                          'teaching_point': 'Fokal motor nöbet sonrasında aynı taraf ekstremitede gelişen ve '
                                            'saatler içinde düzelen geçici tek taraflı güçsüzlük postiktal '
                                            'parezidir (Todd paralizisi); travma olmadan ortopedik patoloji '
                                            'düşünülmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik özellikleri (sağ yanlı fokal kasılma, 18 dakika süre ve geçici postiktal '
                         'parezi) dikkate alındığında bu hastada tanınız nedir?',
             'options': [{'text': 'Basit Febril Konvülziyon',
                          'is_correct': False,
                          'scenario_update': 'Nöbetin 18 dakika sürmesi ve sağ hemikorpusta fokal karakter '
                                             'göstermesi basit febril konvülziyon kriterlerini dışlar.',
                          'teaching_point': 'Basit febril konvülziyon jeneralize karakterdedir, 15 dakikadan '
                                            'kısa sürer ve fokal nörolojik bulgu bırakmaz.'},
                         {'text': 'Komplike Febril Konvülziyon (Febril Status Epileptikus)',
                          'is_correct': True,
                          'explanation': 'Ateşli nöbetin hem fokal özellik taşıması (sağ yanlı kasılma ve '
                                         'postiktal Todd parezisi) hem de 15 dakikadan uzun sürmesi Komplike '
                                         'Febril Konvülziyon ve Febril Status Epileptikus tanısını koydurur.',
                          'new_finding': 'Klinik tanı: Komplike Febril Konvülziyon (Febril Status '
                                         'Epileptikus).'},
                         {'text': 'Siyanotik Katılma (Soluk Tutma) Nöbeti',
                          'is_correct': False,
                          'scenario_update': 'Katılma nöbeti ağlama veya korku sonrası gelişir ve 1 '
                                             'dakikadan kısa sürer; 18 dakikalık ateşli fokal klonik kasılma '
                                             'ile açıklanamaz.',
                          'teaching_point': 'Katılma nöbetleri afebril dönemde ağlama krizini takiben ortaya '
                                            'çıkan kısa süreli refleks anoksik senkop ataklarıdır.'},
                         {'text': 'Akut İskemik Arteriyel İnme',
                          'is_correct': False,
                          'scenario_update': 'Kraniyal görüntüleme normaldir ve sağ koldaki güçsüzlük 2 saat '
                                             'içinde sekelsiz olarak tamamen düzelmiştir.',
                          'teaching_point': 'Fokal nöbet sonrası gelişen ve birkaç saat içinde tam düzelen '
                                            'hemiparezi kalıcı vasküler inme değil, geçici postiktal Todd '
                                            'paralizisidir.'}]},
            {'stage_title': 'Sarı Alan Sonuç ve İkinci Basamak Yönetim Planı',
             'question': 'Nöbeti kontrol altına alınan, sağ koldaki güçsüzlüğü düzelen ancak ilk kez uzamış '
                         'fokal ateşli nöbet geçiren bu 16 aylık hastada nihai izlem ve tedavi planınız ne '
                         'olmalıdır?',
             'options': [{'text': 'Postiktal güçsüzlüğü düzeldiği ve bilinci açıldığı için uzun süreli oral '
                                  'karbamazepin başlayarak hastayı acil servisten doğrudan evine taburcu '
                                  'etmek',
                          'is_correct': False,
                          'scenario_update': 'Yatış yapılmadan taburcu edilen hastada gece tekrar ateş '
                                             'yükselmesiyle uzamış nöbet gelişti; ayrıca karbamazepin febril '
                                             'nöbetlerde etkisiz ve uygunsuz bir seçimdi.',
                          'teaching_point': 'İlk kez febril status epileptikus ve fokal nöbet geçiren süt '
                                            'çocuğu acilden taburcu edilmez; ayrıca karbamazepin febril '
                                            'konvülziyon profilaksisinde kullanılmaz.'},
                         {'text': 'Hastayı servise yatırıp santral sinir sistemi enfeksiyonu dışlansa bile '
                                  'tüm komplike febril nöbetlerde ömür boyu ikili antiepileptik tedavi '
                                  'başlamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz yere başlanan çoklu kronik antiepileptik tedavi süt '
                                             'çocuğunda ağır sedasyon ve gelişimsel yan etkilere yol açtı.',
                          'teaching_point': 'Komplike febril konvülziyonda bile altta yatan yapısal veya '
                                            'metabolik anomali yoksa hemen çoklu ömür boyu antiepileptik '
                                            'başlanmaz; EEG ve çocuk nörolojisi izlemiyle '
                                            'bireyselleştirilmiş karar verilir.'},
                         {'text': 'Nöbet tekrarlamasın diye çocuğu entübe edip tiyopental infüzyonu altında '
                                  'kırk sekiz saat boyunca çocuk yoğun bakım ünitesinde uyutmak',
                          'is_correct': False,
                          'scenario_update': 'Nöbeti durmuş ve bilinci açılmış çocuğa uygulanan gereksiz '
                                             'entübasyon ve barbitürat koması mekanik ventilasyon '
                                             'komplikasyonlarına ve hipotansiyona neden oldu.',
                          'teaching_point': 'Genel anestezik infüzyonu ve entübasyon yalnızca birinci ve '
                                            'ikinci basamak antiepileptiklere yanıt vermeyen refrakter '
                                            'status epileptikus tablosunda endikedir.'},
                         {'text': 'Hastayı yakın nörolojik izlem, santral sinir sistemi enfeksiyonu '
                                  'ekartasyonu, elektroensefalografi ve çocuk nörolojisi değerlendirmesi '
                                  'için çocuk servisine yatırmak',
                          'is_correct': True,
                          'explanation': 'İlk kez geçirilen komplike febril konvülziyon ve febril status '
                                         'epileptikus olguları yakın nörolojik gözlem, etiyolojik inceleme '
                                         '(LP/HSV/EEG) ve nöroloji konsültasyonu amacıyla servise '
                                         'yatırılmalıdır.',
                          'new_finding': 'Hasta Çocuk Sağlığı ve Hastalıkları servisine yatırıldı; santral '
                                         'sinir sistemi enfeksiyonu dışlandı, aileye acil kurtarıcı bukkal '
                                         'midazolam eğitimi verilerek çocuk nörolojisi poliklinik takibine '
                                         'alındı.'}]}]},
 {'id': 'Y04',
  'category': '🫁 Hırıltı & Solunum Sıkıntısı',
  'age': '8 Yaş',
  'gender': 'Erkek',
  'complaint': 'Nefes darlığı, hışıltı, öksürük ve cümleleri tamamlayamama',
  'history': 'Sarı Alana tekerlekli sandalye ile hafif öne eğilmiş oturur pozisyonda getiriliyor. Çocuk '
             "kesik kesik kelimelerle 'Nefesim... yetmiyor...' diyebiliyor. Annesi anlatıyor: 'Daha önce de "
             'kış aylarında tekrarlayan hışıltı atakları olmuştu ve evde inhaler kullanıyordu, 2 gündür '
             'nezleydi. Bu sabah nefes darlığı başladı, evde 2 puf mavi fısfısını (salbutamol) sıktık ama '
             "hiç açılmadı, göğsünden ıslık sesi geliyor.'",
  'final_diagnosis': 'Orta-Ağır Akut Astım Atağı (Viral ÜSYE Tetikli)',
  'disposition': 'Sarı Alanda Oksijen + Ardışık Nebülize Salbutamol/İpratropium + Erken Sistemik Steroid '
                 'Sonrası Yanıt Değerlendirmesi ve Taburculuk',
  'case_pearl': 'Kelime veya kısa cümle konuşabilme, yardımcı solunum kası kullanımı, yaygın wheezing ve oda '
                'havasında SpO2 <%92 olması orta-ağır akut astım atağını gösterir. İlk 1 saatte: Oksijen '
                '(hedef SpO2 %94-98), 20 dakikada bir 3 doz nebülize salbutamol + ipratropium bromür ve '
                'ERKEN (ilk 1 saat içinde) sistemik kortikosteroid (oral prednizolon veya İV '
                'metilprednizolon) verilmelidir.',
  'steps': [{'stage_title': 'Sarı Alanda Solunum Sıkıntısı Şiddetinin Değerlendirilmesi',
             'question': 'Akut nefes darlığı ve hışıltı ile başvuran bu 8 yaşındaki çocukta ilk '
                         'değerlendirmede neleri kontrol etmelisiniz?',
             'options': [{'text': 'Bronkodilatatör ve oksijen tedavisi vermeden önce hava yolu '
                                  'obstrüksiyonunun derecesini objektif ölçmek amacıyla çocuğu solunum '
                                  'fonksiyon testi laboratuvarına göndermek',
                          'is_correct': False,
                          'scenario_update': 'Kelimelerle konuşabilen ve hipoksemisi olan çocuk zorlu '
                                             'ekspirasyon manevrasını yapamadı; işlem sırasında dispnesi ve '
                                             'siyanozu derinleşti.',
                          'teaching_point': 'Akut belirgin solunum sıkıntısı ve hipoksemisi olan çocukta '
                                            'spirometri çektirmek için acil oksijen ve bronkodilatatör '
                                            'tedavi geciktirilmez.'},
                         {'text': 'Konuşma şeklini, bilinç durumunu, solunum sayısını, yardımcı solunum kası '
                                  'çekilmelerini, akciğer oskültasyonunu ve oda havasında oksijen '
                                  'satürasyonunu değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Akut bronkospazm ve hışıltı ile gelen çocukta konuşma kapasitesi, '
                                         'bilinç, çekilmeler, oskültasyonda hava girişi ve SpO2 düzeyi '
                                         'atağın şiddetini ve ilk saat tedavisini doğrudan belirler.',
                          'new_finding': 'Vital Bulgular: Ateş 37.1°C, KTA 136/dk, SS 36/dk, oda havasında '
                                         'SpO2 %90. Çocuk 2-3 kelimelik kesik ifadelerle konuşabiliyor, '
                                         'suprasternal ve interkostal çekilmeleri belirgin. Oskültasyonda '
                                         'ekspiryum uzamış ve her iki hemitoraksta yaygın '
                                         'inspiratuar-ekspiratuar sibilan ronküsler (wheezing) duyuluyor.'},
                         {'text': 'Fizik muayeneyi kolaylaştırmak amacıyla çocuğu sedyeye tam düz sırtüstü '
                                  'yatırıp radyal arterden kan gazı almak ve grafi sonucunu beklemek',
                          'is_correct': False,
                          'scenario_update': 'Supin pozisyona zorla yatırılan çocukta diyafram hareketi '
                                             'kısıtlandığı ve ağrılı arteriyel girişim yapıldığı için '
                                             'ajitasyon arttı, SpO2 %86 düzeyine düştü.',
                          'teaching_point': 'Solunum sıkıntısı olan çocuk en rahat ettiği oturur/yarı oturur '
                                            'pozisyonda tutulmalı ve ilk değerlendirmede rutin arteriyel kan '
                                            'gazı veya grafi için tedavi geciktirilmemelidir.'},
                         {'text': 'Evde iki puf salbutamol aldığı için inhale beta agonistleri etkisiz kabul '
                                  'edip ilk basamakta doğrudan intravenöz aminofilin yüklemesi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Oksijen ve uygun doz nebülize bronkodilatatör verilmeden '
                                             'başlanan intravenöz aminofilin çocukta şiddetli bulantı, kusma '
                                             've sinüs taşikardisine yol açtı.',
                          'teaching_point': 'Evde aracı tüp (spacer) olmadan sıkılan 2 puf inhaler '
                                            'yetersizdir; acil serviste ilk basamak her zaman oksijen, '
                                            'yüksek doz nebülize/spacer salbutamol, ipratropium ve sistemik '
                                            'steroiddir.'}]},
            {'stage_title': 'İlk Bir Saat Akut Tedavi Protokolü',
             'question': 'Oda havasında SpO2 %90 olan, kelimelerle konuşabilen ve yaygın sibilan ronküsleri '
                         'duyulan bu 8 yaşındaki çocukta ilk 1 saatteki en doğru tedavi protokolü '
                         'hangisidir?',
             'options': [{'text': 'Maske ile oksijen başlayıp yalnızca tek doz nebülize salbutamol '
                                  'uygulamak, sistemik kortikosteroid tedavisini ise dördüncü saatin '
                                  'sonundaki klinik yanıta göre ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Tek doz salbutamol sonrası otuzuncu dakikada bronkospazm '
                                             'tekrar arttı; erken sistemik steroid verilmediği için hava '
                                             'yolu ödemi gerilemedi ve SpO2 %89 düzeyinde kaldı.',
                          'teaching_point': 'Belirgin dispne ve hipoksemisi olan akut bronkospazm atağında '
                                            'sistemik kortikosteroidlerin etkisi 3-4 saatte başladığından '
                                            'ilk 1 saat içinde erken verilmesi şarttır; ayrıca ilk saatte 20 '
                                            'dakikada bir 3 doz SABA + ipratropium uygulanmalıdır.'},
                         {'text': 'Tek başına yüksek doz nebülize budesonid ve soğuk buhar uygulayıp kalp '
                                  'hızını artırmaması amacıyla kısa etkili beta-2 agonist ilaçlardan '
                                  'kaçınmak',
                          'is_correct': False,
                          'scenario_update': 'Soğuk buhar hiperreaktif hava yollarında bronkospazmı daha da '
                                             'tetikledi; hızlı etkili bronkodilatatör verilmediği için '
                                             'solunum sıkıntısı ağırlaştı.',
                          'teaching_point': 'Akut bronkospazm atağında kurtarıcı temel ilaç kısa etkili '
                                            'beta-2 agonisttir (salbutamol); soğuk buhar bronkospazmı '
                                            'artırır ve tek başına inhale steroid akut atağı çözmez.'},
                         {'text': 'Nebülize salbutamol ile birlikte çocuğun hızlı solunumunu ve '
                                  'anksiyetesini azaltmak amacıyla düşük doz intravenöz midazolam '
                                  'uygulayarak hafif sedasyon sağlamak',
                          'is_correct': False,
                          'scenario_update': 'Verilen sedatif ilaç çocuğun yardımcı solunum kaslarını ve '
                                             'solunum dürtüsünü baskılayarak akut karbondioksit '
                                             'retansiyonuna ve letarjiye yol açtı.',
                          'teaching_point': 'Akut obstrüktif solunum sıkıntısı atağında sedatif ve '
                                            'anksiyolitik ilaçlar solunum depresyonu ve solunum arresti '
                                            'riski nedeniyle kesinlikle kontrendikedir.'},
                         {'text': 'Oksijen (hedef SpO2 %94-98), yirmi dakika arayla üç doz nebülize '
                                  'salbutamol ve ipratropium bromür ile erken sistemik kortikosteroid '
                                  'başlamak',
                          'is_correct': True,
                          'explanation': 'Güncel uluslararası rehberlere göre hipoksemik orta-ağır '
                                         'bronkospazm atağında ilk 1 saatte hedefe yönelik oksijen, 20 '
                                         'dakika arayla 3 doz nebülize SABA + ipratropium bromür '
                                         'kombinasyonu ve erken sistemik steroid (1-2 mg/kg '
                                         'prednizolon/metilprednizolon) standart tedavidir.',
                          'new_finding': '1. saat sonunda (3 doz nebülize salbutamol + ipratropium bromür ve '
                                         '1.5 mg/kg sistemik metilprednizolon sonrası): Solunum sayısı 24/dk '
                                         'düzeyine geriledi, suprasternal çekilme kayboldu, çocuk tam '
                                         'cümlelerle rahat konuşmaya başladı ve oda havasında SpO2 %96 '
                                         'ölçüldü.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Öyküsü, fizik muayene bulguları ve bronkodilatatör tedaviye verdiği hızlı yanıt '
                         'doğrultusunda bu hastada kesin tanınız nedir?',
             'options': [{'text': 'Akut Yabancı Cisim Aspirasyonu',
                          'is_correct': False,
                          'scenario_update': 'Ani boğulma öyküsü yoktur, oskültasyon bulguları iki taraflı '
                                             'simetriktir ve bronkodilatatör tedavi ile tablo tamamen '
                                             'düzelmiştir.',
                          'teaching_point': 'Yabancı cisim aspirasyonunda genellikle ani başlayan '
                                            'öksürük/boğulma öyküsü ve tek taraflı havalanma azlığı görülür; '
                                            'bronkodilatatöre tam yanıt beklenmez.'},
                         {'text': 'Spontan Akut Tansiyon Pnömotoraks',
                          'is_correct': False,
                          'scenario_update': 'Her iki hemitoraksta solunum sesleri duyulmaktadır, trakea '
                                             'orta hattadır ve hipotansiyon yoktur.',
                          'teaching_point': 'Tansiyon pnömotoraksta tek taraflı solunum sesi kaybı, '
                                            'hipersonorite, trakea deviasyonu ve obstrüktif şok bulguları '
                                            'saptanır.'},
                         {'text': 'Orta-Ağır Akut Astım Atağı',
                          'is_correct': True,
                          'explanation': 'Tekrarlayan hışıltı öyküsü, viral üst solunum yolu enfeksiyonu '
                                         'sonrası gelişen dispne, kesik kelimelerle konuşma, yardımcı kas '
                                         'kullanımı, yaygın wheezing, SpO2 %90 olması ve '
                                         'SABA+ipratropium+steroid tedavisine dramatik yanıt Orta-Ağır Akut '
                                         'Astım Atağını doğrular.',
                          'new_finding': 'Klinik tanı: Orta-Ağır Akut Astım Atağı.'},
                         {'text': 'Psikojenik Hiperventilasyon Sendromu',
                          'is_correct': False,
                          'scenario_update': 'Hastanın oda havasında oksijen satürasyonu %90 olup '
                                             'oskültasyonda yaygın sibilan ronküsler ve suprasternal '
                                             'çekilmeler mevcuttu.',
                          'teaching_point': 'Psikojenik hiperventilasyonda SpO2 normaldir (%99-100), '
                                            'yardımcı solunum kası çekilmesi ve yaygın wheezing bulunmaz.'}]},
            {'stage_title': 'Sarı Alan İzlem ve Taburculuk Planı',
             'question': 'Sarı Alanda 4 saat izlenen, son 2 saattir bronkodilatatör ihtiyacı olmadan oda '
                         'havasında SpO2 değeri %97 olan, çekilmesi kalmayan ve rahat konuşup yürüyebilen bu '
                         'hastada taburculuk planınız ne olmalıdır?',
             'options': [{'text': '3-5 günlük oral steroid kürünü tamamlamak, aracı tüp tekniğini göstererek '
                                  'salbutamol ve inhale kortikosteroid düzenleyip eylem planıyla taburcu '
                                  'etmek',
                          'is_correct': True,
                          'explanation': 'Tedaviye tam yanıt veren ve oda havasında SpO2 >%94 stabil kalan '
                                         'hastada erken relapsı önlemek için 3-5 günlük oral steroid kürü, '
                                         'doğru aracı tüp (spacer) tekniğiyle kurtarıcı+koruyucu inhaler '
                                         'tedavi, yazılı astım eylem planı ve 48 saat içinde kontrol '
                                         'önerilir.',
                          'new_finding': 'Aracı tüp (spacer) olmadan doğrudan ağza sıkma hatası düzeltildi; '
                                         '4 günlük oral steroid, düzenli inhale kortikosteroid ve yazılı '
                                         'astım eylem planı ile hasta taburcu edildi.'},
                         {'text': 'Acilde tek doz steroid yapıldığı için evde ek oral steroid vermeden '
                                  'yalnızca gerektiğinde kullanmak üzere salbutamol reçete ederek taburcu '
                                  'etmek',
                          'is_correct': False,
                          'scenario_update': 'Sistemik steroid kürü devam ettirilmeyen ve kontrol edici '
                                             'inhale steroid başlanmayan çocukta geç faz inflamasyon '
                                             'nedeniyle aynı gece ağır atak tekrarladı.',
                          'teaching_point': 'Orta-ağır astım atağı sonrasında hava yolu inflamasyonunun '
                                            'baskılanması ve erken relapsın önlenmesi için 3-5 günlük oral '
                                            'sistemik steroid kürü tamamlanmalı ve düzenli İKS '
                                            'başlanmalıdır.'},
                         {'text': 'Balgamı yumuşatmak ve gece öksürüğünü kesmek amacıyla oral mukolitik '
                                  'şurup, birinci kuşak antihistaminik ve antitüssif reçete ederek '
                                  'inhalerleri kesmek',
                          'is_correct': False,
                          'scenario_update': 'İnhaler tedavisi kesilen ve antitüssif verilen çocukta mukus '
                                             'tıkaçları ve şiddetli bronkospazm gelişerek ertesi gün acil '
                                             'servise yeniden başvuru oldu.',
                          'teaching_point': 'Astım atağı taburculuğunda antitüssif, mukolitik ve sedatif '
                                            'antihistaminiklerin yeri yoktur; temel tedavi inhaler '
                                            'bronkodilatatör, inhale/oral kortikosteroid ve doğru cihaz '
                                            'eğitimidir.'},
                         {'text': 'Viral üst solunum yolu enfeksiyonu tetiklediği için on günlük oral '
                                  'amoksisilin-klavulanat başlamak ve aracı tüp olmadan doğrudan inhaler '
                                  'kullandırmak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz antibiyotik ishal yaparken, aracı tüp (spacer) '
                                             'kullanılmadığı için inhaler ilacın büyük kısmı orofarenkste '
                                             'kalarak akciğerlere ulaşmadı.',
                          'teaching_point': 'Viral tetikli astım ataklarında rutin antibiyotik endikasyonu '
                                            'yoktur; ayrıca 8 yaşındaki çocukta ölçülü doz inhaler (MDI) '
                                            'mutlaka aracı tüp (spacer) ile kullanılmalıdır.'}]}]},
 {'id': 'Y05',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '3 Yaş (15 kg)',
  'gender': 'Kız',
  'complaint': 'Evde parasetamol şurup şişesini içme',
  'history': 'Annesi elinde boş bir parasetamol süspansiyon (120 mg/5 mL, 150 mL şişe) ile Sarı Alana '
             "koşarak geliyor: 'Hocam, şişede yaklaşık 100-110 mL şurup vardı, tadı çilekli olduğu için 45 "
             'dakika önce mutfakta hepsini kafasına dikip içmiş! Ağzının kenarı hep pembe şuruptu. Şu an '
             "neşesi yerinde, sadece 1 kez hafif öğürdü, hiç kusmadı.'",
  'final_diagnosis': 'Akut Toksik Dozda Parasetamol (Asetaminofen) Zehirlenmesi',
  'disposition': 'Sarı Alanda Aktif Kömür, 4. Saat Serum Parasetamol Düzeyi (Rumack-Matthew) Değerlendirmesi '
                 've İV N-Asetilsistein (NAC) İnfüzyonu ile Servis Yatışı',
  'case_pearl': 'Çocuklarda tek seferde ≥150-200 mg/kg parasetamol alımı akut hepatotoksik dozdur (100 mL x '
                '24 mg/mL = 2400 mg -> 15 kg çocukta 160 mg/kg). Parasetamol zehirlenmesinin ilk 24 saatinde '
                '(Evre 1) hasta tamamen asemptomatik olabilir. İlk 1-2 saat içinde başvuruda 1 g/kg aktif '
                'kömür verilir; serum parasetamol düzeyi alımdan sonraki 4. saatte bakılarak Rumack-Matthew '
                'nomogramında değerlendirilir ve tedavi eşiği üzerindeyse ilk 8 saat içinde N-Asetilsistein '
                '(NAC) başlanır.',
  'steps': [{'stage_title': 'Alınan Dozun Hesaplanması ve İlk Saat Dekontaminasyon',
             'question': 'Alımdan 45 dakika sonra başvuran, 15 kg ağırlığında ve yaklaşık 100-110 mL (120 '
                         'mg/5 mL) parasetamol süspansiyon içtiği belirtilen bilinci açık bu çocukta ilk '
                         'adımınız ne olmalıdır?',
             'options': [{'text': 'Çocuğun genel durumu iyi, vital bulguları stabil ve aktif yakınması '
                                  'olmadığı için alınan miktarı zararsız kabul ederek doğrudan eve taburcu '
                                  'etmek',
                          'is_correct': False,
                          'scenario_update': 'Taburcu edilen çocukta ilk gün yakınma olmazken 36. saatten '
                                             'itibaren sağ üst kadran ağrısı, sarılık, koagülopati ve akut '
                                             'karaciğer yetmezliği gelişti.',
                          'teaching_point': 'Akut yüksek doz parasetamol alımının ilk 24 saatinde (Evre 1) '
                                            'hastalar çoğunlukla asemptomatiktir; klinik görünüme '
                                            'aldanılarak doz hesaplanmadan taburculuk yapılması ölümcül '
                                            'karaciğer hasarına yol açar.'},
                         {'text': 'Midedeki şurubu hızla dışarı çıkarmak amacıyla çocuğa tuzlu su içirerek '
                                  'veya arka farenksi mekanik uyararak yatak başında kusturmaya çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Zorla kusturma girişimi sırasında çocukta aspirasyon tehlikesi '
                                             'gelişti ve inatçı öğürme başladığı için oral aktif kömür '
                                             'uygulanamadı.',
                          'teaching_point': 'Zehirlenmelerde mekanik uyarım, tuzlu su veya ipeka şurubu ile '
                                            'kusturma işlemi aspirasyon riski ve etkinliğinin olmaması '
                                            'nedeniyle kesinlikle kontrendikedir.'},
                         {'text': 'Alınan dozun 160-176 mg/kg olduğunu hesaplamak, vital bulguları alıp ilk '
                                  'saat içinde olduğundan 1 g/kg oral aktif kömür vermek',
                          'is_correct': True,
                          'explanation': '100-110 mL (24 mg/mL) şurup toplam 2400-2640 mg, yani 15 kg '
                                         'çocukta 160-176 mg/kg doza karşılık gelir; ≥150 mg/kg alımlarda '
                                         'ilk 1-2 saat içinde bilinci açık hastaya 1 g/kg oral aktif kömür '
                                         'verilmesi gastrointestinal emilimi anlamlı ölçüde azaltır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 108/dk, SS 22/dk, TA 95/60 mmHg, '
                                         'SpO2 %99, GKS 15. Hesaplanan alım dozu 160-176 mg/kg. Alımın 45. '
                                         'dakikasında 15 gram (1 g/kg) oral aktif kömür uygulandı ve çocuk '
                                         'kusmadan tolere etti.'},
                         {'text': 'Sıvı süspansiyon formlarında aktif kömürün bağlama etkisi olmadığı '
                                  'gerekçesiyle kalın orogastrik tüp yerleştirerek yüksek hacimli gastrik '
                                  'lavaj işlemi uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Bilinci açık 3 yaşındaki çocukta zorla yapılan kalın tüplü '
                                             'gastrik lavaj özofagus mukozasında travmaya, laringospazma ve '
                                             'hipoksiye neden oldu.',
                          'teaching_point': 'Parasetamol aktif kömüre çok iyi bağlanır; hızlı emilen sıvı '
                                            'süspansiyon alımlarında rutin gastrik lavaj yerine ilk 1-2 saat '
                                            'içinde oral aktif kömür uygulaması tercih edilir.'}]},
            {'stage_title': 'Laboratuvar İzlemi ve Kan Düzeyi Zamanlaması',
             'question': 'Aktif kömür uygulanan ve şu an alımın 1. saatinde olan bu çocukta biyokimyasal '
                         'izlem ve plazma ilaç düzeyi ölçümü için en doğru zamanlama nedir?',
             'options': [{'text': 'Alımın birinci saatinde hemen plazma parasetamol düzeyi ve karaciğer '
                                  'enzimlerini gönderip sonuçlar düşük çıkarsa çocuğu dördüncü saati '
                                  'beklemeden taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Birinci saatte bakılan plazma ilaç düzeyi 65 mcg/mL ve AST/ALT '
                                             'normal geldi; ancak gastrointestinal emilim devam ettiği için '
                                             'dördüncü saatte kan düzeyi 185 mcg/mL değerine yükseldi.',
                          'teaching_point': 'Akut tek doz alımlarda gastrointestinal emilim ve doku dağılımı '
                                            '4. saate kadar tamamlanmaz; 4. saatten önce bakılan kan ilaç '
                                            'düzeyi ve erken AST/ALT değerleri toksisiteyi dışlamak için '
                                            'kullanılamaz.'},
                         {'text': 'Bazal karaciğer-böbrek fonksiyonları, INR ve glukoz bakmak; anlamlı '
                                  'plazma parasetamol konsantrasyonu için alımdan sonraki dördüncü saatte '
                                  'kan örneği almak',
                          'is_correct': True,
                          'explanation': 'Akut tek seferlik yüksek doz parasetamol alımında emilim ve '
                                         'dağılım fazı 4. saatte tamamlandığından, tedavi kararını '
                                         'belirleyen plazma ilaç konsantrasyonu alımdan sonraki 4. saatte '
                                         'ölçülmelidir.',
                          'new_finding': 'Bazal (1. saat) laboratuvar: AST 26 U/L, ALT 19 U/L, INR 1.0, üre '
                                         '22 mg/dL, kreatinin 0.4 mg/dL, glukoz 94 mg/dL. Alımdan tam 4 saat '
                                         'sonra alınan plazma parasetamol konsantrasyonu: 185 mcg/mL.'},
                         {'text': 'Plazma ilaç düzeyi bakmak yerine idrarda kalitatif ilaç taraması istemek '
                                  've sadece yirmi dördüncü saatte kontrol AST/ALT değerlerini görmek',
                          'is_correct': False,
                          'scenario_update': 'İdrar taraması pozitif saptandı ancak kandaki kantitatif '
                                             'konsantrasyon ölçülmediği için dördüncü saatteki yüksek plazma '
                                             'düzeyi fark edilemedi ve spesifik tedavi gecikti.',
                          'teaching_point': 'İdrarda kalitatif ilaç taraması terapötik dozlarda bile pozitif '
                                            'çıkar ve toksisite şiddetini göstermez; yönetim kararı mutlaka '
                                            '4. saat kantitatif plazma parasetamol konsantrasyonu ile '
                                            'verilmelidir.'},
                         {'text': 'İlaç yarı ömrünün geçmesini beklemek amacıyla ilk kan örneğini alımdan '
                                  'sonraki on ikinci saatte almak ve o zamana kadar beklemek',
                          'is_correct': False,
                          'scenario_update': 'On ikinci saate kadar hiçbir düzey bakılmadan beklenmesi, '
                                             'koruyucu tedavinin en etkili olduğu ilk sekiz saatlik altın '
                                             'pencerenin kaçırılmasına yol açtı.',
                          'teaching_point': 'Akut alımlarda plazma ilaç düzeyi 4. saatte bakılmalı ve '
                                            'koruyucu tedavi gerekiyorsa alımdan sonraki ilk 8 saat içinde '
                                            'başlanmalıdır; 12. saati beklemek karaciğer hasarı riskini '
                                            'artırır.'}]},
            {'stage_title': 'Klinik Tanı ve Toksisite Risk Değerlendirmesi',
             'question': 'Yaklaşık 160-176 mg/kg alım öyküsü ve 4. saat plazma parasetamol konsantrasyonu '
                         '185 mcg/mL olan bu hastada Rumack-Matthew nomogramına göre tanınız ve risk '
                         'değerlendirmeniz nedir?',
             'options': [{'text': 'Toksik Olmayan Terapötik Doz Parasetamol Maruziyeti',
                          'is_correct': False,
                          'scenario_update': '4. saat plazma parasetamol düzeyi 185 mcg/mL olup '
                                             'Rumack-Matthew nomogramındaki 150 mcg/mL tedavi eşiğinin '
                                             'belirgin üzerindedir.',
                          'teaching_point': 'Rumack-Matthew nomogramında 4. saatte ≥150 mcg/mL olan plazma '
                                            'parasetamol düzeyleri akut hepatotoksisite riski taşır ve '
                                            'antidot tedavisi gerektirir.'},
                         {'text': 'Akut Salisilat İntoksikasyonu ve Solunumsal Alkaloz',
                          'is_correct': False,
                          'scenario_update': 'Hastanın içtiği ilaç parasetamol (asetaminofen) '
                                             'süspansiyondur; Done nomogramı veya salisilat toksisitesi söz '
                                             'konusu değildir.',
                          'teaching_point': 'Parasetamol ve salisilat farklı analjezik-antipiretik '
                                            'ilaçlardır; parasetamol NAPQI aracılı karaciğer nekrozu '
                                            'yaparken salisilat solunumsal alkaloz ve metabolik asidoz '
                                            'yapar.'},
                         {'text': 'Evre 3 Fulminan Hepatik Yetmezlik Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Hasta henüz alımın 4. saatindedir (Evre 1), bilinci açıktır ve '
                                             'bazal AST, ALT ve INR değerleri normaldir.',
                          'teaching_point': 'Parasetamol zehirlenmesinde Evre 1 (ilk 24 saat) '
                                            'asemptomatik/hafif GİS bulgularıyla seyreder; Evre 3 fulminan '
                                            'karaciğer yetmezliği tedavi edilmeyen vakalarda 72-96. '
                                            'saatlerde gelişir.'},
                         {'text': 'Akut Toksik Parasetamol Zehirlenmesi (Yüksek Hepatotoksisite Riski)',
                          'is_correct': True,
                          'explanation': 'Rumack-Matthew nomogramında 4. saat plazma parasetamol '
                                         'konsantrasyonunun 150 mcg/mL tedavi çizgisinin üzerinde (185 '
                                         'mcg/mL) olması yüksek hepatotoksisite riskini ve acil antidot '
                                         'endikasyonunu gösterir.',
                          'new_finding': 'Klinik tanı: Akut Toksik Dozda Parasetamol Zehirlenmesi '
                                         '(Rumack-Matthew tedavi eşiği üzerinde, antidot endikasyonu '
                                         'mevcut).'}]},
            {'stage_title': 'Spesifik Antidot Protokolü ve Yatış Planı',
             'question': '4. saat plazma parasetamol düzeyi 185 mcg/mL saptanan bu hastada karaciğer '
                         'nekrozunu (NAPQI toksisitesini) önlemek için uygulanması gereken spesifik antidot '
                         've izlem planı nedir?',
             'options': [{'text': 'İlk sekiz saat içinde intravenöz N-Asetilsistein (NAC) infüzyon protokolü '
                                  'başlamak ve günlük AST, ALT, INR takibiyle servise yatırmak',
                          'is_correct': True,
                          'explanation': 'Parasetamol zehirlenmesinin spesifik antidotu N-Asetilsisteindir '
                                         '(NAC); glutatyon depolarını yenileyerek toksik metabolit '
                                         'NAPQI-kaynaklı hepatik nekrozu önler ve ilk 8 saat içinde '
                                         "başlandığında koruyuculuğu %100'e yakındır.",
                          'new_finding': 'Alımın 5. saatinde İV N-Asetilsistein infüzyon protokolü '
                                         'başlanarak hasta çocuk servisine yatırıldı. İzlemde AST, ALT ve '
                                         'INR değerleri normal seyreden hasta tedavi sonunda sekelsiz '
                                         'taburcu edildi.'},
                         {'text': 'Bazal AST, ALT ve INR değerleri tamamen normal olduğu için antidot '
                                  'başlamadan yirmi dört saat sonra poliklinik kontrolü önermek',
                          'is_correct': False,
                          'scenario_update': 'Antidot başlanmadan eve gönderilen çocukta 36. saatte AST ve '
                                             'ALT 3500 U/L üzerine çıktı ve akut karaciğer yetmezliği '
                                             'gelişti.',
                          'teaching_point': 'N-Asetilsistein tedavisine transaminazlar yükselmeden önce, 4. '
                                            'saat plazma parasetamol düzeyine göre ilk 8 saat içinde '
                                            'başlanmalıdır; AST/ALT yükselmesini beklemek koruyucu pencereyi '
                                            'kaçırtır.'},
                         {'text': 'İdrar pH değerini 7.5 üzerine çıkararak parasetamolün böbreklerden '
                                  'atılımını hızlandırmak amacıyla intravenöz sodyum bikarbonat ile idrar '
                                  'alkalinizasyonu protokolü başlatmak',
                          'is_correct': False,
                          'scenario_update': 'İdrar alkalinizasyonu parasetamol eliminasyonunu artırmadığı '
                                             'gibi, spesifik antidot verilmediği için toksik metabolit NAPQI '
                                             'birikimi ve karaciğer hasarı gelişti.',
                          'teaching_point': 'İdrar alkalinizasyonu salisilat ve fenobarbital zehirlenmesinde '
                                            'kullanılır; parasetamol zehirlenmesinde etkinliği yoktur, '
                                            'spesifik tedavi N-Asetilsisteindir.'},
                         {'text': 'Spesifik antidot olarak intravenöz fomepizol veya nalokson puşe uygulayıp '
                                  'altı saatlik Sarı Alan gözlemi sonrasında hastayı evine taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Fomepizol ve nalokson parasetamol metabolizması üzerinde '
                                             'koruyucu etki göstermedi; hastada ikinci günde ciddi '
                                             'hepatotoksisite tablosu ortaya çıktı.',
                          'teaching_point': 'Fomepizol metanol/etilen glikol, nalokson ise opioid '
                                            'zehirlenmesinin antidotudur; parasetamol intoksikasyonunda tek '
                                            'spesifik antidot N-Asetilsisteindir (NAC).'}]}]},
 {'id': 'Y06',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '10 Yaş',
  'gender': 'Kız',
  'complaint': 'Karın ağrısı, tekrarlayan kusma, derin ve hızlı nefes alma, belirgin halsizlik',
  'history': "Sarı Alana halsiz ve bitkin halde getiriliyor: 'Dün akşamdan beri karnı çok ağrıyor ve 6 kez "
             'kustu. İshali veya ateşi hiç olmadı ama çok derin ve hızlı nefes alıp veriyor. Son 3 haftadır '
             'çok su içiyordu, geceleri 3-4 kez idrara kalkıyordu ve iştahı açık olmasına rağmen 4 kilo '
             "zayıfladı.'",
  'final_diagnosis': 'Diyabetik Ketoasidoz (DKA - Yeni Tanı Tip 1 Diabetes Mellitus)',
  'disposition': 'Sarı Alanda İlk Saat İzotonik Sıvı Restorasyonu + Potasyum Destekli Rehidratasyon ve İV '
                 'Regüler İnsülin İnfüzyonu -> Çocuk Yoğun Bakım Yatışı',
  'case_pearl': 'Karın ağrısı, kusma ve takipne ile başvuran çocuklarda ishal yoksa ve poliüri, polidipsi, '
                'kilo kaybı eşlik ediyorsa Diyabetik Ketoasidoz (DKA) akut batın veya solunum yolu '
                'enfeksiyonu ile sıkça karışır. ISPAD 2022 kılavuzuna göre İV bolus insülin ve rutin sodyum '
                'bikarbonat serebral ödem riskini artırdığı için kontrendikedir; ilk saat %0.9 NaCl '
                'restorasyonu sonrası 0.05-0.1 U/kg/saat İV regüler insülin infüzyonu başlanır.',
  'steps': [{'stage_title': 'Sarı Alanda İlk Değerlendirme ve Yatak Başı Yaklaşım',
             'question': 'Karın ağrısı, kusma ve derin-hızlı solunumla getirilen 10 yaşındaki bu hastada ilk '
                         'değerlendirmede öncelikli yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Solunum sıkıntısı ve takipne ön planda olduğu için hemen geri solumasız '
                                  'maskeyle oksijen başlayıp ardışık üç doz nebülize salbutamol ve sistemik '
                                  'metilprednizolon uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Akciğer oskültasyonu tamamen doğal ve SpO2 değeri %100 olan '
                                             'hastada verilen beta-agonist ve sistemik kortikosteroid '
                                             'sonrası kan şekeri 610 mg/dL düzeyine yükseldi, takipnesi ve '
                                             'letarjisi daha da derinleşti.',
                          'teaching_point': 'Akciğer oskültasyonu doğal ve satürasyonu normal olan bir '
                                            'çocukta derin ve hızlı solunum paterni alt solunum yolu '
                                            'obstrüksiyonunu değil, ağır metabolik asidozun solunumsal '
                                            'kompansasyonunu düşündürmelidir.'},
                         {'text': 'Asidotik tipte derin ve takipneik solunum paternini, dehidratasyon '
                                  'derecesini ve bilinç durumunu değerlendirip derhal parmak ucu kan şekeri '
                                  'ile kan ketonu bakmak',
                          'is_correct': True,
                          'explanation': 'Poliüri, polidipsi, kilo kaybı, kusma ve akciğer bulgusu '
                                         'olmaksızın derin-hızlı solunumla başvuran çocukta ağır '
                                         'hiperglisemi ve metabolik asidoz tablosu yatak başı kapiller '
                                         'glukoz ve keton ölçümüyle ilk dakikada saptanmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 132/dk, SS 34/dk, TA 100/65 mmHg, '
                                         'SpO2 %100. Solunum asidotik tipte derin ve takipneik paternde; '
                                         'akciğer oskültasyonu bilateral doğal. Nefeste belirgin aseton '
                                         'kokusu mevcut. Ağız mukozası kuru, kapiller dolum 3 saniye, GKS '
                                         '14. Parmak ucu kan şekeri 465 mg/dL, kapiller kan ketonu 5.8 '
                                         'mmol/L saptandı.'},
                         {'text': 'Şiddetli karın ağrısı ve tekrarlayan kusma nedeniyle akut cerrahi batın '
                                  'düşünerek oral alımı kesmek, nazogastrik dekompresyon yapmak ve acil '
                                  'batın ultrasonografisi için radyolojiye göndermek',
                          'is_correct': False,
                          'scenario_update': 'Yatak başı kan şekeri bakılmadan radyoloji ünitesine '
                                             'gönderilen hastanın ultrasonografisinde serbest sıvı veya akut '
                                             'cerrahi patoloji saptanmadı; ancak işlem sırasında hastanın '
                                             'uykuya meyili ve dehidratasyonu belirgin şekilde arttı.',
                          'teaching_point': 'Ağır metabolik asidoz ve ketonemi tablosu şiddetli karın ağrısı '
                                            've kusma ile akut cerrahi batını taklit edebilir; görüntüleme '
                                            'öncesinde yatak başı kan şekeri ve kan gazı mutlaka kontrol '
                                            'edilmelidir.'},
                         {'text': 'Tekrarlayan kusma ve dehidratasyon nedeniyle damar yolu açıp intravenöz '
                                  'ondansetron uygulamak ve kan şekeri bakmadan %5 dekstroz içeren hipotonik '
                                  'sıvıyı hızlı infüzyonla başlamak',
                          'is_correct': False,
                          'scenario_update': 'Kan şekeri ölçülmeden verilen dekstrozlu hipotonik sıvı '
                                             'sonrası hastanın mevcut hiperglisemisi daha da arttı ve serum '
                                             'efektif osmolaritesindeki ani dalgalanma nedeniyle baş ağrısı '
                                             'ile konvülziyon riski ortaya çıktı.',
                          'teaching_point': 'Hiperglisemi ve dehidratasyon kuşkusu olan hastalarda kapiller '
                                            'glukoz görülmeden dekstroz içeren veya hipotonik sıvılar '
                                            'kesinlikle başlanmamalı; ilk hacim genişletme yalnız izotonik '
                                            'kristaloid ile yapılmalıdır.'}]},
            {'stage_title': 'Laboratuvar İncelemesi ve Metabolik Değerlendirme',
             'question': 'Parmak ucu kan şekeri 465 mg/dL ve kan ketonu 5.8 mmol/L saptanan bu hastada ilk '
                         'laboratuvar ve izlem planınız ne olmalıdır?',
             'options': [{'text': 'Sadece venöz glukoz ve tam idrar tetkiki göndermek, sonuçları beklemeden '
                                  'kan şekerini hızla düşürmek için 0.15 U/kg intravenöz puşe regüler '
                                  'insülin uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Serum potasyum düzeyi ve asidoz derecesi görülmeden yapılan '
                                             'intravenöz bolus insülin sonrası potasyum hızla hücre içine '
                                             'kaydı; monitörde T dalga düzleşmesi, belirgin U dalgaları ve '
                                             'ventriküler ekstrasistoller gelişti.',
                          'teaching_point': 'Ağır hiperglisemi ve ketonemi yönetiminde intravenöz bolus '
                                            'insülin hem akut hipokalemik aritmi hem de hızlı osmolarite '
                                            'düşüşüne bağlı beyin ödemi riskini artırdığı için kesinlikle '
                                            'kontrendikedir.'},
                         {'text': 'Arteriyel kan gazı ve serum elektrolitlerini almak, derin takipneyi '
                                  'azaltmak amacıyla kan gazı sonucunu beklemeden 2 mEq/kg intravenöz sodyum '
                                  'bikarbonat infüzyonu başlamak',
                          'is_correct': False,
                          'scenario_update': 'Erken uygulanan sodyum bikarbonat infüzyonu sonrası hastada '
                                             'paradoksal santral sinir sistemi asidozu, hipokalemi eğilimi '
                                             've doku oksijen sunumunda bozulma gelişerek bilinç durumu GKS '
                                             '11 düzeyine geriledi.',
                          'teaching_point': 'Metabolik asidozlu hiperglisemik krizlerde rutin sodyum '
                                            'bikarbonat uygulaması paradoksal serebral asidoz ve beyin ödemi '
                                            'riski taşır; sıvı ve insülin infüzyonu ile keton üretimi '
                                            'durduğunda asidoz kendiliğinden düzelir.'},
                         {'text': 'Venöz kan gazı, biyokimya ve HbA1c istemek, ancak ilk saat sıvı '
                                  'tedavisini beklemeden eş zamanlı olarak 0.1 U/kg/saat hızında intravenöz '
                                  'insülin infüzyonunu başlatmak',
                          'is_correct': False,
                          'scenario_update': 'İlk saat izotonik sıvı restorasyonu tamamlanmadan erken '
                                             'başlanan insülin infüzyonu, intravasküler hacim henüz dolmadan '
                                             'glukozun hızla düşmesine ve sistemik hipotansiyon ile serebral '
                                             'hipoperfüzyona yol açtı.',
                          'teaching_point': 'Güncel kılavuzlara göre insülin infüzyonu ilk başvuruda hemen '
                                            'başlanmaz; önce 1 saatlik izotonik sıvı restorasyonu yapılmalı '
                                            've serum potasyum düzeyi görüldükten sonra insülin infüzyonuna '
                                            'geçilmelidir.'},
                         {'text': 'Venöz kan gazı, serum elektrolitleri, düzeltilmiş sodyum hesabı, üre, '
                                  'kreatinin, fosfor, magnezyum, tam idrar tetkiki, HbA1c ve potasyum izlemi '
                                  'için EKG istemek',
                          'is_correct': True,
                          'explanation': 'Venöz pH ve bikarbonat ile metabolik tablonun ağırlığı belirlenir; '
                                         'ölçülen sodyum üzerinden düzeltilmiş sodyum hesaplanmalı ve '
                                         'insülin öncesi bazal potasyum düzeyi ile EKG mutlaka '
                                         'değerlendirilmelidir.',
                          'new_finding': 'LABORATUVAR: Venöz Kan Gazı pH 7.12, pCO2 20 mmHg, HCO3 6.4 '
                                         'mmol/L, Baz Açığı -21, Laktat 1.8 mmol/L. Glukoz 465 mg/dL, '
                                         'Ölçülen Na 131 mEq/L, Hesaplanan Düzeltilmiş Na 137 mEq/L, K 4.6 '
                                         'mEq/L, Cl 96 mEq/L, Fosfor 3.8 mg/dL, Üre 42 mg/dL, Kreatinin 0.72 '
                                         'mg/dL. TİT: Glukoz +++, Keton +++. HbA1c %11.8. EKG: Sinüs '
                                         'taşikardisi, T dalgaları normal.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Mevcut klinik bulgular ve laboratuvar sonuçları (Glukoz 465 mg/dL, venöz pH 7.12, '
                         'HCO3 6.4 mmol/L, kan ketonu 5.8 mmol/L) doğrultusunda kesin tanınız nedir?',
             'options': [{'text': 'Orta-Ağır Diyabetik Ketoasidoz (Yeni Tanı Tip 1 DM)',
                          'is_correct': True,
                          'explanation': 'ISPAD 2022 kriterlerine göre kan şekeri >200 mg/dL, venöz pH <7.30 '
                                         'veya HCO3 <15 mmol/L ve ketonemi ≥3.0 mmol/L varlığı DKA tanısını '
                                         'koydurur; pH 7.12 ve HCO3 6.4 mmol/L orta-ağır DKA ile uyumludur.',
                          'new_finding': 'Kesin Tanı: Orta-Ağır Diyabetik Ketoasidoz (Yeni Tanı Tip 1 '
                                         'Diabetes Mellitus).'},
                         {'text': 'Ketoasidoz Olmayan Hiperglisemik Hiperosmolar Durum (HHD)',
                          'is_correct': False,
                          'scenario_update': 'Hastada belirgin ketonemi (5.8 mmol/L) ve derin metabolik '
                                             'asidoz (pH 7.12, HCO3 6.4 mmol/L) mevcut olup tablo HHD '
                                             'kriterleri ile uyumlu değildir.',
                          'teaching_point': 'Hiperglisemik Hiperosmolar Durumda kan şekeri >600 mg/dL ve '
                                            'efektif osmolarite >320 mOsm/kg iken belirgin ketozis ve ağır '
                                            'asidoz (pH >7.25, HCO3 >15) beklenmez.'},
                         {'text': 'Akut Dekompanse Metabolik Asidoz ve Stres Hiperglisemisi',
                          'is_correct': False,
                          'scenario_update': 'Hastanın 3 haftalık poliüri-polidipsi öyküsü, 465 mg/dL glukoz '
                                             'değeri, 5.8 mmol/L ketonemisi ve %11.8 HbA1c düzeyi geçici '
                                             'stres hiperglisemisini dışlamaktadır.',
                          'teaching_point': 'Stres hiperglisemisinde HbA1c normaldir (<%5.7) ve ağır '
                                            'ketonemi ile derin metabolik asidoz görülmez.'},
                         {'text': 'Akut Salisilat İntoksikasyonuna Bağlı Metabolik Asidoz',
                          'is_correct': False,
                          'scenario_update': 'Hastada ilaç alım öyküsü yoktur; üç haftalık ozmotik diürez '
                                             'semptomları, aşikâr hiperglisemi ve yüksek HbA1c salisilat '
                                             'zehirlenmesiyle açıklanamaz.',
                          'teaching_point': 'Salisilat zehirlenmesi solunumsal alkaloz ve yüksek anyon '
                                            'açıklı metabolik asidoz yapabilir ancak kan şekeri 465 mg/dL ve '
                                            'HbA1c %11.8 yeni tanı Tip 1 DM göstergesidir.'}]},
            {'stage_title': 'Sarı Alanda İlk Saat Tedavisi ve Serebral Ödemden Korunma',
             'question': 'Orta-ağır DKA tanısı konulan ve serum potasyumu 4.6 mEq/L olan bu hastada beyin '
                         'ödemi riskini en aza indiren tedavi planı hangisidir?',
             'options': [{'text': 'İlk saatte 20 mL/kg %0.45 NaCl hipotonik sıvı yüklemek, 0.1 U/kg İV puşe '
                                  'insülin yapmak ve pH 7.12 olduğu için 1 mEq/kg sodyum bikarbonat vermek',
                          'is_correct': False,
                          'scenario_update': 'Hipotonik sıvı yüklemesi, İV bolus insülin ve sodyum '
                                             'bikarbonat uygulaması sonrası 3. saatte hastada şiddetli baş '
                                             'ağrısı, bradikardi, sistemik hipertansiyon ve bilinç kaybı ile '
                                             'akut serebral ödem gelişti.',
                          'teaching_point': 'DKA tedavisinde hipotonik sıvı bolusu, İV puşe insülin ve rutin '
                                            'bikarbonat verilmesi serum efektif osmolaritesini hızla '
                                            'düşürerek ölümcül beyin ödemine yol açar.'},
                         {'text': 'İlk saatte 10 mL/kg %0.9 NaCl vermek, potasyum 4.6 mEq/L olduğu için '
                                  'sıvıya hiç potasyum eklemeden 0.2 U/kg/saat yüksek doz İV insülin '
                                  'infüzyonu başlamak',
                          'is_correct': False,
                          'scenario_update': 'Potasyum desteği eklenmeden yüksek dozda başlanan insülin '
                                             'infüzyonu sonrası 2. saatte serum potasyumu 2.4 mEq/L düzeyine '
                                             'düştü ve hastada ciddi hipokalemik aritmi gelişti.',
                          'teaching_point': 'İnsülin potasyumu hızla hücre içine sokar; idrar çıkışı olan ve '
                                            'serum K <5.5 mEq/L olan her DKA hastasında rehidratasyon '
                                            'sıvısına mutlaka 40 mEq/L potasyum eklenmelidir.'},
                         {'text': 'İlk saat 10-20 mL/kg %0.9 NaCl verdikten sonra 40 mEq/L potasyum eklenmiş '
                                  'sıvıyla defisiti 24-48 saate yaymak ve 0.05-0.1 U/kg/saat İV regüler '
                                  'insülin başlamak',
                          'is_correct': True,
                          'explanation': 'ISPAD 2022 kılavuzuna göre ilk saat yalnız izotonik sıvı verilir; '
                                         '1. saatin sonunda potasyum içeren rehidratasyon sıvısı ve 0.05-0.1 '
                                         'U/kg/saat düşük doz İV regüler insülin infüzyonu başlanarak hasta '
                                         'yoğun bakıma yatırılır.',
                          'new_finding': 'İlk saat %0.9 NaCl restorasyonu sonrası potasyum destekli sıvı ve '
                                         '0.1 U/kg/saat İV regüler insülin infüzyonu başlandı; kan şekeri '
                                         '250 mg/dL altına indiğinde sıvıya %5 dekstroz eklenerek Çocuk '
                                         'Yoğun Bakım Ünitesine devredildi.'},
                         {'text': 'İlk saatte %0.9 NaCl infüzyonu ile birlikte subkütan hızlı etkili insülin '
                                  'lispro uygulamak ve kusması durunca hastayı endokrinoloji poliklinik '
                                  'kontrolü önerisiyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Orta-ağır dehidratasyonu ve pH 7.12 asidozu olan hastada '
                                             'subkütan insülin emilimi yetersiz kaldı; 4. saatte metabolik '
                                             'asidozu derinleşen hastada bilinç bulanıklığı arttı.',
                          'teaching_point': 'Orta ve ağır DKA (pH <7.20) hastalarında doku perfüzyonu bozuk '
                                            'olduğundan subkütan insülin yerine titre edilebilir İV regüler '
                                            'insülin infüzyonu kullanılmalı ve hasta mutlaka '
                                            'yatırılmalıdır.'}]}]},
 {'id': 'Y07',
  'category': '👶 Ağlayan, Emmeyen, Huzursuz Bebek',
  'age': '9 Aylık',
  'gender': 'Erkek',
  'complaint': 'Aralıklı şiddetli ağlama krizleri, bacaklarını karnına çekme, safralı kusma ve ataklar '
               'arasında belirgin uyuklama',
  'history': "Annesi Sarı Alana getiriyor: 'Sabah saatlerinden beri 15-20 dakikada bir aniden çığlık atarak "
             'ağlamaya başlıyor, rengi soluyor ve iki bacağını karnına doğru çekiyor. Kriz 2-3 dakika sürüp '
             "geçince tamamen bitkin düşüp uyukluyor. Az önce 2 kez sarı-yeşil renkli kustu.'",
  'final_diagnosis': 'İleoçekal İnvajinasyon (İntususepsiyon)',
  'disposition': 'Sarı Alanda NPO + Nazogastrik Dekompresyon + İV Sıvı Resüsitasyonu -> USG Eşliğinde '
                 'Hidrostatik/Pnömatik Redüksiyon ve Çocuk Cerrahisi Yatışı',
  'case_pearl': '3 ay - 3 yaş arası süt çocuklarında periyodik kıvrandırıcı ağlama atakları, ataklar '
                'arasında belirgin letarji ve safralı kusma İleoçekal İnvajinasyon için tipiktir. '
                'Mukuslu-kanlı dışkılama geç bir bulgudur. Tanıda altın standart Batın USG (transvers '
                'kesitte hedef tahtası / target sign) olup, perforasyon veya peritonit yoksa ilk basamak '
                'tedavi hidrostatik veya pnömatik enema redüksiyonudur.',
  'steps': [{'stage_title': 'Sarı Alanda İlk Değerlendirme ve Fizik Muayene',
             'question': 'Periyodik kıvrandırıcı ağlama atakları, ataklar arası letarji ve safralı kusması '
                         'olan 9 aylık bu bebekte ilk muayenede öncelikli yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Ataklar arasındaki belirgin uykuya meyil ve kusmayı santral sinir sistemi '
                                  'enfeksiyonu bulgusu kabul ederek batın muayenesini erteleyip acil lomber '
                                  'ponksiyon hazırlığı yapmak',
                          'is_correct': False,
                          'scenario_update': 'Lomber ponksiyon hazırlığı sırasında bebek tekrar bacaklarını '
                                             'karnına çekerek şiddetli ağlama krizi geçirdi ve bol miktarda '
                                             'safralı kustu; işlem sonunda BOS bulguları tamamen normal '
                                             'saptandı.',
                          'teaching_point': 'Süt çocuklarında periyodik karın ağrısı atakları arasında '
                                            'gelişen derin letarji, endojen opioid salınımına bağlı klasik '
                                            'bir klinik bulgudur; safralı kusma varlığında öncelikle akut '
                                            'batın muayenesi yapılmalıdır.'},
                         {'text': 'Ağlama krizlerini süt çocuğu gaz sancısı olarak değerlendirip simetikon '
                                  'damla ve rektal gliserin fitil uyguladıktan sonra bebeği Yeşil Alanda '
                                  'gözleme almak',
                          'is_correct': False,
                          'scenario_update': 'Uygulanan gliserin fitil sonrası bezde mukuslu ve koyu '
                                             'pembe-kırmızı kanlı dışkı görüldü; bebeğin safralı kusmaları '
                                             'devam etti ve taşikardisi derinleşerek kapiller dolum zamanı 4 '
                                             'saniyeye uzadı.',
                          'teaching_point': 'Dokuz aylık bir bebekte yeni başlayan periyodik kıvrandırıcı '
                                            'ağlama krizleri, letarji ve safralı kusma asla fonksiyonel gaz '
                                            'sancısı olarak değerlendirilemez; mekanik bağırsak tıkanıklığı '
                                            'dışlanmalıdır.'},
                         {'text': 'Vital bulguları, atak dışı bilinç durumunu, sağ üst kadran palpasyonu ile '
                                  'sağ alt kadran boşluğunu ve bezdeki dışkıyı değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Kolik tarzda ağlama atakları, safralı kusma ve letarji ile '
                                         'başvuran süt çocuğunda batın kadranlarının dikkatli palpasyonu, '
                                         'peritoneal irritasyon kontrolü ve rektal/bez muayenesi en kritik '
                                         'ilk adımdır.',
                          'new_finding': 'Vital Bulgular: Ateş 37.3°C, KTA 148/dk, SS 32/dk, TA 88/52 mmHg, '
                                         'KDZ 2-3 sn. Bebek muayene başında uykuya meyilli iken aniden '
                                         'bacaklarını karnına çekerek ağlama atağı geçirdi. Sakinleştiğinde '
                                         'sağ üst kadranda 3x2 cm boyutunda silindirik kitle palpe edildi, '
                                         'sağ alt kadran boş hissedildi. Bezde mukuslu ve pembe-kırmızı '
                                         'kanlı dışkı bulaşı görüldü. Tahta karın bulgusu yok.'},
                         {'text': 'Kusmayı durdurmak amacıyla hemen intravenöz ondansetron yapıp ağızdan '
                                  'oral rehidratasyon sıvısı denemesine başlamak ve iki saat sonra batın '
                                  'muayenesini tekrarlamak',
                          'is_correct': False,
                          'scenario_update': 'Ağızdan verilen sıvıyı hemen safralı olarak kusan bebekte '
                                             'batın distansiyonu belirginleşti ve 2 saatlik gecikme '
                                             'sonucunda kapiller dolum zamanı uzayarak hipovolemi bulguları '
                                             'ağırlaştı.',
                          'teaching_point': 'Safralı kusma aksi kanıtlanana kadar mekanik intestinal '
                                            'obstrüksiyon göstergesidir; bu hastalarda oral alım derhal '
                                            'kesilmeli ve antiemetik verilerek oral besleme denemesi '
                                            'yapılmamalıdır.'}]},
            {'stage_title': 'Sarı Alanda Stabilizasyon ve Görüntüleme Seçimi',
             'question': 'Safralı kusması, sağ üst kadranda palpe edilen kitlesi ve mukuslu-kanlı dışkısı '
                         'olan bu bebekte ilk stabilizasyon ve görüntüleme planınız ne olmalıdır?',
             'options': [{'text': 'Oral alımı kesmek, nazogastrik dekompresyon sağlamak, %0.9 NaCl ile '
                                  'intravenöz sıvı resüsitasyonu başlamak ve acil batın ultrasonografisi '
                                  'istemek',
                          'is_correct': True,
                          'explanation': 'Akut mekanik bağırsak obstrüksiyonu şüphesinde oral alımın '
                                         'kesilmesi, nazogastrik dekompresyon, izotonik sıvı desteği ve '
                                         'yüksek duyarlılığa sahip batın ultrasonografisi altın standart '
                                         'yaklaşımdır.',
                          'new_finding': 'Nazogastrik sondadan safralı mide içeriği drene edildi ve 20 mL/kg '
                                         '%0.9 NaCl bolusu sonrası KTA 126/dk düzeyine geriledi. BATIN USG: '
                                         'Sağ üst kadranda transvers kesitte iç içe geçmiş konsantrik '
                                         'ekojenik ve hipoekoik bağırsak halkaları (3.2 cm çapında), '
                                         'longitudinal kesitte ise tübüler katmanlı bağırsak segmenti '
                                         'izlendi. Batın içinde serbest hava saptanmadı.',
                          'image': 'assets/images/usg_intussusception.png',
                          'image_caption': 'Batın USG: Konsantrik hipoekoik ve hiperekoik halkalar (Target '
                                           'Sign)'},
                         {'text': 'Sadece ayakta direkt batın grafisi çekmek ve grafide hava-sıvı seviyesi '
                                  'görülmezse mekanik tıkanıklığı dışlayarak hastaya oral beslenme denemesi '
                                  'yapmak',
                          'is_correct': False,
                          'scenario_update': 'Çekilen direkt batın grafisinde yalnızca sağ alt kadranda gaz '
                                             'azlığı izlendi, belirgin hava-sıvı seviyesi görülmedi; ancak '
                                             'oral besleme sonrası bebeğin safralı kusması ve letarjisi '
                                             'şiddetlendi.',
                          'teaching_point': 'Direkt batın grafisi erken dönemde %25-30 oranında tamamen '
                                            'normal olabilir ve mekanik obstrüksiyonu dışlamaz; yalnızca '
                                            'perforasyon (serbest hava) şüphesinde ek bilgi sağlar.'},
                         {'text': 'Damar yolu açıp sedasyon uyguladıktan sonra ultrasonografi beklemeksizin '
                                  'kontrastlı tüm batın bilgisayarlı tomografisi çekerek bağırsak lümenini '
                                  've mezenteri değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Dokuz aylık bebek yüksek doz iyonizan radyasyona ve sedasyon '
                                             'riskine maruz kaldı; ayrıca kontrast hazırlığı nedeniyle kesin '
                                             'tedavi 2 saat gecikti.',
                          'teaching_point': 'Süt çocuklarında bu klinik tabloda ultrasonografi %98-100 '
                                            'duyarlılık ve özgüllüğe sahiptir; radyasyon ve sedasyon '
                                            'gerektiren bilgisayarlı tomografi ilk basamakta endike '
                                            'değildir.'},
                         {'text': 'Mukuslu ve kanlı dışkılama nedeniyle akut bakteriyel enterokolit '
                                  'düşünerek gaita kültürü göndermek, intravenöz seftriakson başlamak ve '
                                  'görüntülemeyi ertesi güne bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik tedavisine rağmen bebeğin kıvrandırıcı ağlama '
                                             'atakları ve safralı kusmaları devam etti; 12 saat sonra batın '
                                             'distansiyonu, ateş ve peritoneal irritasyon bulguları gelişti.',
                          'teaching_point': 'Mukuslu-kanlı dışkı bakteriyel dizanteri ile karışabilir; ancak '
                                            'safralı kusma, periyodik ağlama krizleri ve sağ üst kadranda '
                                            'kitle varlığında acil ultrasonografi geciktirilmemelidir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik tablo ve batın ultrasonografisinde saptanan iç içe geçmiş konsantrik '
                         'bağırsak halkaları görünümü doğrultusunda kesin tanınız nedir?',
             'options': [{'text': 'İnfantil Hipertrofik Pilor Stenozu',
                          'is_correct': False,
                          'scenario_update': 'Pilor stenozu yaşamın ilk 3-6 haftasında safrasız fışkırır '
                                             'kusma ile seyreder; 9 aylık bebekte safralı kusma ve kanlı '
                                             'dışkı pilor stenozu ile uyumsuzdur.',
                          'teaching_point': 'Hipertrofik pilor stenozunda tıkanıklık pilor düzeyinde olduğu '
                                            'için kusma her zaman safrasızdır ve hipokloremik hipokalemik '
                                            'metabolik alkaloz görülür.'},
                         {'text': 'Akut İnvaziv Bakteriyel Gastroenterit (Şigelloz)',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografide saptanan 3.2 cm çapındaki iç içe geçmiş '
                                             'bağırsak halkaları (hedef işareti) enfeksiyöz koliti değil '
                                             'mekanik invajinasyonu göstermektedir.',
                          'teaching_point': 'Bakteriyel enterokolitte yüksek ateş ve sık sulu-kanlı ishal ön '
                                            'plandadır; USG de hedef tahtası (target sign) bulgusu '
                                            'görülmez.'},
                         {'text': 'Meckel Divertikülüne Bağlı Alt GİS Kanaması',
                          'is_correct': False,
                          'scenario_update': 'Meckel divertikülü tipik olarak ağrısız masif rektal kanama '
                                             'yapar; bu hastada ise şiddetli kolik ağrı atakları ve USG ile '
                                             'kanıtlanmış invajinasyon mevcuttur.',
                          'teaching_point': 'Meckel divertikülü süt çocuğunda invajinasyon için bir '
                                            'sürükleyici nokta (lead point) olabilir ancak mevcut akut '
                                            'klinik tablo ileoçekal invajinasyondur.'},
                         {'text': 'Akut İleoçekal İnvajinasyon (İntususepsiyon)',
                          'is_correct': True,
                          'explanation': 'Distal ileumun çekum ve çıkan kolon lümeni içine teleskop gibi '
                                         'girmesiyle oluşan ileoçekal invajinasyon, USG de transvers kesitte '
                                         'hedef tahtası (target/donut sign) ve longitudinal kesitte '
                                         'psödo-böbrek görünümü verir.',
                          'new_finding': 'Kesin Tanı: Akut İleoçekal İnvajinasyon (İntususepsiyon).'}]},
            {'stage_title': 'Sarı Alanda Tedavi Seçimi ve Yatış Planı',
             'question': 'Perforasyon, peritonit veya dekompanse şok bulgusu olmayan bu ileoçekal '
                         'invajinasyon hastasında en uygun tedavi ve izlem yaklaşımı hangisidir?',
             'options': [{'text': 'Radyolojik redüksiyon girişimi perforasyon riski taşıdığı için enema '
                                  'denemeden hastayı doğrudan acil eksploratris laparotomi ve bağırsak '
                                  'rezeksiyonu için ameliyathaneye almak',
                          'is_correct': False,
                          'scenario_update': 'Peritonit veya perforasyon bulgusu olmayan hastada ameliyatsız '
                                             'redüksiyon şansı kullanılmadan yapılan laparotomi, gereksiz '
                                             'genel anestezi ve cerrahi morbiditeye yol açtı.',
                          'teaching_point': 'Cerrahi laparotomi yalnızca serbest hava (perforasyon), yaygın '
                                            'peritonit, refrakter şok veya radyolojik redüksiyonun başarısız '
                                            'olduğu durumlarda endikedir.'},
                         {'text': 'Çocuk Cerrahisi konsültasyonu ile ultrasonografi veya skopi eşliğinde '
                                  'hidrostatik veya pnömatik enema redüksiyonu uygulamak ve gözlem için '
                                  'yatırmak',
                          'is_correct': True,
                          'explanation': 'Komplike olmayan ileoçekal invajinasyonda ilk tercih %85-90 başarı '
                                         'oranına sahip ultrasonografi eşliğinde hidrostatik (serum '
                                         'fizyolojik) veya skopi eşliğinde pnömatik (hava) redüksiyondur; '
                                         'işlem sonrası erken nüks (%5-10) açısından hasta izlenir.',
                          'new_finding': 'Çocuk Cerrahisi ve Radyoloji işbirliği ile USG kılavuzluğunda '
                                         'hidrostatik redüksiyon başarıyla uygulandı; ileoçekal valvden '
                                         'serbest sıvı geçişi doğrulandı ve hasta 24 saatlik gözlem için '
                                         'yatırıldı.'},
                         {'text': 'Ultrasonografi eşliğinde hidrostatik redüksiyon başarıyla tamamlandıktan '
                                  'hemen sonra oral beslenmeye geçip hastayı 1. saatte acil servisten eve '
                                  'taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'İşlemden 1 saat sonra eve gönderilen bebekte 6 saat sonra evde '
                                             'tekrar şiddetli ağlama krizleri ve safralı kusma ile erken '
                                             'rekürrens (nüks) gelişti.',
                          'teaching_point': 'Başarılı hidrostatik veya pnömatik redüksiyon sonrasında '
                                            'vakaların %5-10 unda özellikle ilk 24 saat içinde erken nüks '
                                            'görülebileceğinden hastalar yakın gözlem altında tutulmalıdır.'},
                         {'text': 'Bağırsak ansının kendiliğinden açılabileceğini düşünerek enema '
                                  'redüksiyonu yapmadan sadece intravenöz sıvı ve spazmolitik ilaç verip 24 '
                                  'saat klinik izlemde beklemek',
                          'is_correct': False,
                          'scenario_update': 'İleoçekal invajinasyonda sadece sıvı ve spazmolitik ile '
                                             'beklenmesi sonucu bağırsak duvarında venöz konjesyon, '
                                             'transmural iskemi, nekroz ve 18. saatte perforasyon gelişti.',
                          'teaching_point': 'İleoçekal (kolonik) invajinasyonlar kendiliğinden açılmaz ve '
                                            'acil redüksiyon gerektirir; yalnız asemptomatik, kısa segment '
                                            '(<2 cm) ince bağırsak (ileo-ileal) invajinasyonları yakın USG '
                                            'takibiyle izlenebilir.'}]}]},
 {'id': 'Y08',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '4 Yaş',
  'gender': 'Erkek',
  'complaint': 'Yüksek ateş (40.1°C), şiddetli baş ağrısı, fışkırır tarzda kusma, ışıktan rahatsız olma ve '
               'uykuya meyil',
  'history': "Sarı Alana kucakta getiriliyor: 'Dün akşamdan beri ateşi 40°C'ye çıktı, ateş düşürücülere "
             'rağmen düşmüyor. Başım çok ağrıyor deyip ağlıyor, odanın ışığını açtığımızda gözlerini sıkıca '
             'kapatıyor. Bugün 4 kez fışkırır gibi kustu ve boynunu öne doğru eğmek istemiyor. Son 1 saattir '
             "sorularımıza çok yavaş cevap veriyor.'",
  'final_diagnosis': 'Akut Bakteriyel Menenjit (Pnömokoksik Menenjit - S. pneumoniae)',
  'disposition': 'Sarı Alanda Kan Kültürü + Lomber Ponksiyon -> İlk Antibiyotik Dozu Öncesi İV Deksametazon '
                 '+ Menenjit Dozunda Seftriakson ve Vankomisin -> Çocuk Yoğun Bakım Yatışı',
  'case_pearl': 'Yüksek ateş, baş ağrısı, fışkırır tarzda kusma, fotofobi, letarji ve meninks irritasyon '
                'bulguları (ense sertliği, Kernig ve Brudzinski) Akut Bakteriyel Menenjit için klasiktir. '
                'Lomber ponksiyon kontrendikasyonu (herniasyon bulgusu, fokal nörolojik defisit, '
                'kardiyopulmoner instabilite, koagülopati/purpura) yoksa hızla LP yapılmalı; ilk antibiyotik '
                'dozundan hemen önce/eş zamanlı 0.15 mg/kg İV Deksametazon ve ardından menenjit dozunda '
                'Seftriakson (100 mg/kg/gün) + Vankomisin (60 mg/kg/gün) başlanmalıdır.',
  'steps': [{'stage_title': 'Sarı Alanda Nörolojik ve Sistemik Değerlendirme',
             'question': '40.1°C ateşi, fotofobisi, fışkırır tarzda kusması ve uykuya meyili olan 4 '
                         'yaşındaki bu çocukta ilk muayenede öncelikli yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Vital bulguları, GKS ve pupilleri, fokal nörolojik defisitleri, pasif '
                                  'boyun fleksiyonunda direnç ile kalça-diz ekstansiyon manevralarını ve '
                                  'döküntüyü değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Akut santral sinir sistemi enfeksiyonu şüphesinde hem spinal zar '
                                         'irritasyon bulguları hem de kafa içi basınç artışı bulguları '
                                         '(bradikardi, hipertansiyon, anizokori, fokal defisit) ve purpurik '
                                         'döküntü hızla kontrol edilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 40.0°C, KTA 138/dk, SS 28/dk, TA 102/65 mmHg, '
                                         'SpO2 %98, KDZ 2 sn. GKS 13 (uykuya meyilli, sesli uyaranla göz '
                                         'açıyor). Pasif boyun fleksiyonunda belirgin direnç mevcut; boyun '
                                         'öne eğildiğinde kalça ve dizlerde refleks fleksiyon gelişiyor ve '
                                         'uyluk fleksiyonda iken bacak ekstansiyonunda ağrılı kısıtlılık '
                                         'saptanıyor. Pupiller izokorik, papilödem veya fokal nörolojik '
                                         'defisit yok, ciltte peteşi/purpura yok.'},
                         {'text': 'Şiddetli baş ağrısı, kusma ve ışıktan rahatsız olmayı pediatrik migren '
                                  'atağı olarak değerlendirip karanlık odada intravenöz parasetamol ve '
                                  'ondansetron vererek izlemek',
                          'is_correct': False,
                          'scenario_update': 'Yalnızca analjezik ve antiemetik verilerek bekletilen çocukta '
                                             '1 saat sonra jeneralize tonik-klonik konvülziyon gelişti ve '
                                             'bilinç durumu GKS 9 düzeyine geriledi.',
                          'teaching_point': 'Kırk derece ateş, letarji ve pasif boyun fleksiyonunda direnç '
                                            'bulunan bir çocukta tablo asla primer baş ağrısı veya migren '
                                            'olarak açıklanamaz; akut santral sinir sistemi enfeksiyonu '
                                            'dışlanmalıdır.'},
                         {'text': 'Yüksek ateş ve baş ağrısını akut bakteriyel rinosinüzite bağlayarak '
                                  'nörolojik muayene yapmadan intravenöz amoksisilin-klavulanat uygulayıp '
                                  'gözlem odasında ateşin düşmesini beklemek',
                          'is_correct': False,
                          'scenario_update': 'Standart dozda verilen amoksisilin-klavulanat kan-beyin '
                                             'bariyerini yeterli düzeyde geçemedi; 3 saat içinde hastanın '
                                             'uykuya meyili derinleşti ve periferik dolaşım bozukluğu '
                                             'gelişti.',
                          'teaching_point': 'Fışkırır tarzda kusma, fotofobi, bilinç değişikliği ve boyun '
                                            'hareketlerinde kısıtlılık varlığında üst solunum yolu '
                                            'enfeksiyonu düşünülerek standart doz antibiyotikle yetinilmesi '
                                            'ağır komplikasyonlara yol açar.'},
                         {'text': 'Uykuya meyilli çocuğu muayene etmeden ve damar yolu açmadan önce kafa içi '
                                  'kitleyi dışlamak amacıyla doğrudan kraniyal manyetik rezonans '
                                  'görüntülemeye göndermek',
                          'is_correct': False,
                          'scenario_update': 'Stabilizasyon ve ilk değerlendirme yapılmadan uzun süreli MR '
                                             'çekimine gönderilen hastada radyoloji ünitesinde ateşli '
                                             'konvülziyon gelişti ve acil müdahale gecikti.',
                          'teaching_point': 'Akut ateşli ve letarjik çocukta ilk adım yatak başı vital '
                                            'bulguların, dolaşımın ve nörolojik muayenenin '
                                            'değerlendirilmesidir; stabilizasyon sağlanmadan hasta uzun '
                                            'süreli görüntülemeye gönderilmez.'}]},
            {'stage_title': 'Laboratuvar ve Beyin Omurilik Sıvısı İnceleme Yaklaşımı',
             'question': 'Hemodinamisi stabil olan, papilödemi, fokal nörolojik defisiti veya cilt döküntüsü '
                         'bulunmayan bu hastada inceleme ve girişim planınız ne olmalıdır?',
             'options': [{'text': 'Kan kültürü ve lomber ponksiyon yapmadan hemen antibiyotik başlamak, 24 '
                                  'saat sonra klinik yanıt alındıktan sonra beyin omurilik sıvısı örneği '
                                  'almak',
                          'is_correct': False,
                          'scenario_update': 'Kontrendikasyon olmadığı halde ertelenen ve antibiyotik '
                                             'verildikten 24 saat sonra yapılan lomber ponksiyonda beyin '
                                             'omurilik sıvısı kültürü steril kaldı; etken ve antibiyotik '
                                             'duyarlılığı saptanamadı.',
                          'teaching_point': 'Herniasyon riski, fokal defisit, şok veya koagülopati gibi bir '
                                            'kontrendikasyon yoksa antibiyotik dozundan hemen önce kan '
                                            'kültürü ve lomber ponksiyon yapılarak etken izolasyonu '
                                            'sağlanmalıdır.'},
                         {'text': 'Papilödem ve fokal defisit olmamasına rağmen önce kraniyal bilgisayarlı '
                                  'tomografi çekmek ve radyoloji raporu çıkana kadar 3 saat boyunca '
                                  'antibiyotik vermeden beklemek',
                          'is_correct': False,
                          'scenario_update': 'Kraniyal BT tamamen normal raporlandı; ancak 3 saatlik süreçte '
                                             'antibiyotik başlanmadığı için hastada septik şok ve ağır '
                                             'nörolojik kötüleşme gelişti.',
                          'teaching_point': 'Fokal nörolojik defisit, papilödem, koma (GKS <10) veya '
                                            'immünsüpresyon yoksa lomber ponksiyon öncesi rutin kraniyal BT '
                                            'endike değildir; görüntüleme yapılacaksa bile kan kültürü '
                                            'alınıp ampirik tedavi geciktirilmeden başlanmalıdır.'},
                         {'text': 'Damar yolu açarak kan kültürü, hemogram, CRP, prokalsitonin ve eş zamanlı '
                                  'glukoz alıp kontrendikasyon bulunmadığından steril koşullarda lomber '
                                  'ponksiyon uygulamak',
                          'is_correct': True,
                          'explanation': 'Hemodinamik instabilite, fokal nörolojik bulgu veya papilödem '
                                         'olmayan hastada kan kültürü ve eş zamanlı kan şekeri alınarak '
                                         'derhal lomber ponksiyon yapılmalı ve beyin omurilik sıvısı '
                                         'incelenmelidir.',
                          'new_finding': 'KAN: WBC 24.500/mm³, CRP 165 mg/L, Prokalsitonin 14 ng/mL, Eş '
                                         'zamanlı Kan Şekeri 100 mg/dL, Koagülasyon normal. BOS BULGULARI: '
                                         'Görünüm bulanık, açılış basıncı artmış, hücre sayımı 1.850/mm³ '
                                         '(%92 parçalı çekirdekli lökosit), BOS proteini 185 mg/dL, BOS '
                                         'glukozu 18 mg/dL (BOS/kan glukoz oranı 0.18). Gram boyamada bol '
                                         'lökosit ve Gram pozitif diplokoklar görüldü.'},
                         {'text': 'Lomber ponksiyon invaziv bir işlem olduğu için yalnızca kan kültürü, tam '
                                  'idrar tetkiki ve nazofarengeal viral sürüntü göndererek klinik izleme '
                                  'almak',
                          'is_correct': False,
                          'scenario_update': 'Nazofarengeal sürüntü ve idrar tetkiki negatif sonuçlandı; '
                                             'beyin omurilik sıvısı incelenmediği için santral sinir sistemi '
                                             'enfeksiyonunun şiddeti ve etkeni belirlenemedi.',
                          'teaching_point': 'Santral sinir sistemi enfeksiyonu şüphesinde kesin etiyolojik '
                                            'ayrım ve uygun tedavi süresi yalnızca beyin omurilik sıvısı '
                                            'analizi (hücre, protein, glukoz, Gram boyama ve kültür/PCR) ile '
                                            'belirlenebilir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulanık görünümde BOS, 1.850/mm³ nötrofil hakimiyetli pleositoz, yüksek BOS '
                         'proteini (185 mg/dL), düşük BOS glukozu (18 mg/dL) ve Gram (+) diplokok bulgusu '
                         'ile kesin tanınız nedir?',
             'options': [{'text': 'Akut Enteroviral (Aseptik) Menenjit',
                          'is_correct': False,
                          'scenario_update': 'Viral menenjitlerde BOS genellikle berraktır, hücre sayısı '
                                             'çoğunlukla <500/mm³ olup lenfosit hakimiyeti vardır, BOS '
                                             'glukozu normaldir ve Gram boyamada bakteri görülmez.',
                          'teaching_point': 'Belirgin hipoglikoraji (BOS/kan glukoz oranı <0.4), yüksek '
                                            'protein (>100 mg/dL), >1000/mm³ nötrofilik pleositoz ve pozitif '
                                            'Gram boyama bakteriyel menenjiti gösterir.'},
                         {'text': 'Akut Bakteriyel Menenjit (Pnömokoksik Menenjit)',
                          'is_correct': True,
                          'explanation': 'Bulanık BOS, >1000/mm³ PNL hakimiyeti, belirgin hipoglikoraji (18 '
                                         'mg/dL), yüksek protein ve Gram boyamada Gram (+) diplokokların '
                                         'görülmesi Streptococcus pneumoniae kaynaklı akut bakteriyel '
                                         'menenjit için tanısaldır.',
                          'new_finding': 'Kesin Tanı: Akut Bakteriyel Menenjit (Streptococcus pneumoniae).'},
                         {'text': 'Herpes Simpleks Virüs (HSV-1) Ensefaliti',
                          'is_correct': False,
                          'scenario_update': 'HSV ensefalitinde fokal nöbetler, temporal lob bulguları, BOS '
                                             'ta lenfositik pleositoz, eritrosit varlığı ve normal/hafif '
                                             'düşük glukoz beklenir; Gram (+) diplokok görülmez.',
                          'teaching_point': 'Gram boyamada Gram (+) diplokok saptanması ve ağır '
                                            'hipoglikoraji doğrudan pnömokoksik bakteriyel menenjiti '
                                            'doğrular.'},
                         {'text': 'Santral Sinir Sistemi Tüberküloz Menenjiti',
                          'is_correct': False,
                          'scenario_update': 'Tüberküloz menenjiti haftalar süren subakut prodromla başlar, '
                                             'BOS ta lenfosit hakimiyeti vardır ve Gram boyamada Gram (+) '
                                             'diplokok izlenmez.',
                          'teaching_point': 'Akut 24 saatlik fulminan başlangıç, nötrofilik pleositoz ve '
                                            'Gram (+) diplokoklar akut piyojenik pnömokoksik menenjit '
                                            'tablosudur.'}]},
            {'stage_title': 'Sarı Alanda Ampirik Antibiyoterapi, Steroid Zamanlaması ve Yatış',
             'question': 'Akut bakteriyel menenjit tanısı konulan 4 yaşındaki bu hastada kılavuzlara en '
                         'uygun ilk doz tedavi ve yatış protokolü hangisidir?',
             'options': [{'text': 'Standart enfeksiyon dozunda 50 mg/kg/gün İV seftriakson monoterapisi '
                                  'başlamak, vankomisin eklememek ve inflamasyonu baskılamak için '
                                  'deksametazonu antibiyotikten 6 saat sonra uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Düşük doz seftriakson BOS ta yeterli bakterisidal '
                                             'konsantrasyona ulaşamadı, sefalosporin dirençli pnömokok '
                                             'olasılığı kapsanmadı ve antibiyotikten saatler sonra verilen '
                                             'deksametazon işitme kaybını önlemede etkisiz kaldı.',
                          'teaching_point': 'Bakteriyel menenjitte seftriakson mutlaka 100 mg/kg/gün '
                                            '(menenjit dozu) verilmeli, dirençli S. pneumoniae için '
                                            'vankomisin (60 mg/kg/gün) eklenmeli ve deksametazon ilk '
                                            'antibiyotik dozundan önce/eş zamanlı uygulanmalıdır.'},
                         {'text': 'Kan-beyin bariyerini geçmesi için İV ampisilin ve gentamisin kombinasyonu '
                                  'başlamak, enfeksiyonu yayabileceği düşüncesiyle kortikosteroid vermekten '
                                  'kaçınmak ve genel servise yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Yenidoğan döneminden sonra ampisilin + gentamisin kombinasyonu '
                                             'penisilin dirençli S. pneumoniae için yetersiz kaldı ve '
                                             'hastada sensorinöral işitme kaybı gelişti.',
                          'teaching_point': 'Bir aydan büyük çocuklarda ampirik bakteriyel menenjit '
                                            'tedavisinde 3. kuşak sefalosporin (seftriakson/sefotaksim) + '
                                            'vankomisin kullanılır; ilk doz öncesi deksametazon işitme kaybı '
                                            've nörolojik sekeli azaltır.'},
                         {'text': 'Menenjit dozunda 100 mg/kg/gün İV seftriakson ve 60 mg/kg/gün İV '
                                  'vankomisin başlamak, ödemi azaltmak için hastaya günlük %50 fazla '
                                  'hipotonik idame sıvısı vermek',
                          'is_correct': False,
                          'scenario_update': 'Aşırı ve hipotonik sıvı verilen hastada uygunsuz ADH salınımı '
                                             'sendromu (SIADH) zemininde serum sodyumu 124 mEq/L düzeyine '
                                             'düştü ve beyin ödemi ile konvülziyon gelişti.',
                          'teaching_point': 'Bakteriyel menenjitte SIADH riski yüksek olduğundan aşırı ve '
                                            'hipotonik sıvı yüklemesinden kaçınılmalı; övolemiyi koruyacak '
                                            'şekilde izotonik idame sıvısı tercih edilerek sodyum yakından '
                                            'izlenmelidir.'},
                         {'text': 'İlk antibiyotik dozundan önce 0.15 mg/kg İV deksametazon uygulayıp 100 '
                                  'mg/kg/gün İV seftriakson ve 60 mg/kg/gün İV vankomisin başlayarak '
                                  'yatırmak',
                          'is_correct': True,
                          'explanation': 'IDSA ve AAP kılavuzlarına göre >1 ay çocuklarda ampirik menenjit '
                                         'tedavisi Seftriakson (100 mg/kg/gün, 2 dozda) + Vankomisin (60 '
                                         'mg/kg/gün, 4 dozda) kombinasyonudur; ilk antibiyotik dozundan '
                                         'hemen önce/eş zamanlı verilen Deksametazon (0.15 mg/kg) '
                                         'bakteriyolize bağlı subaraknoid inflamasyonu ve işitme kaybını '
                                         'azaltır.',
                          'new_finding': 'İlk doz öncesi 0.15 mg/kg İV Deksametazon, ardından menenjit '
                                         'dozunda İV Seftriakson ve Vankomisin uygulandı; hasta yakın '
                                         'nörolojik izlem ve SIADH/elektrolit takibi amacıyla Çocuk Yoğun '
                                         'Bakım Ünitesine yatırıldı.'}]}]},
 {'id': 'Y09',
  'category': '👶 Ağlayan, Emmeyen, Huzursuz Bebek',
  'age': '6 Aylık',
  'gender': 'Kız',
  'complaint': 'İki gündür düşmeyen 39.8°C ateş, belirgin huzursuzluk, tekrarlayan kusma ve emmede azalma',
  'history': "Annesi Sarı Alana getiriyor: 'İki gündür ateşi 39.8°C'ye kadar çıkıyor, ateş düşürücü verince "
             "38.5°C'ye ancak iniyor ve titreyerek tekrar yükseliyor. Burnu akmıyor, öksürmüyor, ishali de "
             'yok ama bugün 3 kez kustu ve çok huzursuz. Bezini açtığımızda idrarının normalden daha ağır '
             "koktuğunu fark ettik.'",
  'final_diagnosis': 'Akut Piyelonefrit (Ateşli Üst İdrar Yolu Enfeksiyonu)',
  'disposition': 'Sarı Alanda Steril Mesane Kateterizasyonu ile Kültür + Kan Tetkikleri -> Parenteral '
                 'Antibiyoterapi (İV Seftriakson), Üriner USG Planı ve Çocuk Servisi Yatışı',
  'case_pearl': '2-24 ay arası süt çocuklarında odağı belirsiz ≥39°C ateş varlığında en sık ciddi bakteriyel '
                'enfeksiyon Akut Piyelonefrittir. Tuvalet eğitimi olmayan ateşli bebekte antibiyotik '
                'başlanmadan önce steril mesane kateterizasyonu veya suprapubik aspirasyon ile idrar kültürü '
                'alınmalıdır; torba idrarı yüksek kontaminasyon oranı nedeniyle kültür için kullanılmaz. '
                'Kusması olan veya küçük süt çocuklarında parenteral antibiyoterapi başlanır ve Üriner '
                'Sistem USG planlanır.',
  'steps': [{'stage_title': 'Sarı Alanda Odak Araştırması ve Sistemik Muayene',
             'question': 'İki gündür 39.8°C ateşi, huzursuzluğu ve kusması olan 6 aylık bu kız bebekte ilk '
                         'değerlendirmede yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Solunum semptomu olmasa bile yüksek ateş ve kusmayı gizli bakteriyel '
                                  'pnömoni bulgusu kabul ederek fizik muayeneyi erteleyip doğrudan arka-ön '
                                  'akciğer grafisi çektirmek',
                          'is_correct': False,
                          'scenario_update': 'Takipnesi, çekilmesi ve öksürüğü olmayan bebekte çekilen '
                                             'akciğer grafisi tamamen normal saptandı; bebek gereksiz '
                                             'radyasyona maruz kaldı ve asıl enfeksiyon odağı '
                                             'aydınlatılamadı.',
                          'teaching_point': 'Solunum sayısı ve akciğer oskültasyonu tamamen normal olan, '
                                            'öksürük veya rinit bulgusu bulunmayan ateşli süt çocuklarında '
                                            'rutin akciğer grafisi önerilmez.'},
                         {'text': 'Altıncı ayda başlayan yüksek ateş ve huzursuzluğu diş çıkarma dönemine '
                                  'bağlayarak oral ibuprofen şurup verip bebeği Yeşil Alandan eve taburcu '
                                  'etmek',
                          'is_correct': False,
                          'scenario_update': 'Ateş düşürücü verilerek eve gönderilen bebek 18 saat sonra '
                                             '40.2°C ateş, letarji, uzamış kapiller dolum zamanı ve septik '
                                             'şok tablosuyla acil servise tekrar getirildi.',
                          'teaching_point': 'Diş çıkarma süreci hiçbir zaman ≥38.5°C üzerinde yüksek ateş ve '
                                            'tekrarlayan kusma nedeni olarak kabul edilemez; 39.8°C ateşte '
                                            'gizli bakteriyel enfeksiyon odağı mutlaka araştırılmalıdır.'},
                         {'text': 'Ateşi hızla kontrol altına almak ve bakteriyemi riskini önlemek için '
                                  'kültür örnekleri almadan hemen intramüsküler 50 mg/kg seftriakson '
                                  'uygulayıp gözleme almak',
                          'is_correct': False,
                          'scenario_update': 'Örnek alınmadan yapılan seftriakson enjeksiyonu sonrasında '
                                             'bebeğin ateşi kısmen geriledi ancak daha sonra alınan '
                                             'kültürlerde üreme olmadığından kesin tanı ve antibiyogram '
                                             'duyarlılığı belirlenemedi.',
                          'teaching_point': 'Hemodinamik olarak stabil olan ateşli süt çocuğunda ampirik '
                                            'antibiyotik verilmeden önce mutlaka uygun yöntemle '
                                            'mikrobiyolojik kültür örnekleri alınmalıdır.'},
                         {'text': 'Vital bulguları, periferik dolaşımı, ön fontanel ve nörolojik durumu, '
                                  'kulak-boğaz-akciğer-cilt muayenesini ve suprapubik ile kostovertebral '
                                  'bölge hassasiyetini eksiksiz olarak değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Odağı ilk bakışta belli olmayan ≥39°C ateşli süt çocuğunda tüm '
                                         'sistemlerin muayenesi yapılmalı, meninks irritasyonu dışlanmalı ve '
                                         'üriner sistem muayenesi dahil gizli enfeksiyon odakları '
                                         'taranmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 39.7°C, KTA 160/dk, SS 36/dk, TA 86/50 mmHg, '
                                         'KDZ 2 sn. Bebek huzursuz ancak uyanık, ön fontanel normal '
                                         'bombelikte, pasif boyun fleksiyonu serbest. Otoskopi, orofarenks '
                                         've akciğer oskültasyonu tamamen doğal, ciltte döküntü yok. '
                                         'Suprapubik bölge ve kostovertebral açı palpasyonunda bebeğin '
                                         'ağlaması ve huzursuzluğu belirgin artıyor.'}]},
            {'stage_title': 'Uygun Örnek Alma Yöntemi ve Laboratuvar Planı',
             'question': 'Görünür üst solunum yolu odağı saptanmayan, 39.7°C ateşi ve kusması olan 6 aylık '
                         'bu kız bebekte kesin odak tespiti için hangi tetkikleri nasıl istemelisiniz?',
             'options': [{'text': 'Perine cildine steril olmayan toplama torbası yapıştırarak hem tam idrar '
                                  'tetkiki hem de idrar kültürü göndermek ve kan tetkiki almadan sonucu '
                                  'beklemek',
                          'is_correct': False,
                          'scenario_update': 'Torba örneğinde lökosit esteraz pozitif saptandı; ancak aynı '
                                             'torbadan gönderilen kültürde perine florası bulaşına bağlı üç '
                                             'farklı mikroorganizma (karışık deri florası) ürediği için '
                                             'sonuç geçersiz sayıldı.',
                          'teaching_point': 'Tuvalet eğitimi olmayan çocuklarda torba örneği %85 e varan '
                                            'yalancı pozitiflik (kontaminasyon) oranına sahiptir; torba '
                                            'yalnız taramada negatif çıkarsa dışlama sağlar, kültür için '
                                            'asla kullanılmaz.'},
                         {'text': 'Steril mesane kateterizasyonu ile tam idrar tetkiki, mikroskopi ve idrar '
                                  'kültürü almak; hemogram, CRP, prokalsitonin ve kan kültürü göndermek',
                          'is_correct': True,
                          'explanation': 'AAP kılavuzuna göre tuvalet eğitimi olmayan ateşli süt çocuğunda '
                                         'antibiyotik öncesi kültür için altın standart steril mesane '
                                         'kateterizasyonu veya suprapubik aspirasyondur; kusması olan '
                                         'bebekte akut faz reaktanları ve kan kültürü de alınmalıdır.',
                          'new_finding': 'KATETER İDRARI: Görünüm bulanık, Lökosit Esteraz +++, Nitrit '
                                         'Pozitif (+), Mikroskopide her sahada 40-50 lökosit ve bol bakteri. '
                                         'KAN TETKİKLERİ: WBC 19.600/mm³ (%80 nötrofil), CRP 94 mg/L, '
                                         'Prokalsitonin 3.8 ng/mL, Üre 24 mg/dL, Kreatinin 0.35 mg/dL. İdrar '
                                         've kan kültürleri ekime gönderildi.'},
                         {'text': 'Yalnızca parmak ucu CRP ve tam kan sayımı bakmak, lökositoz saptanırsa '
                                  'kateterizasyon ile bebeği huzursuz etmeden doğrudan oral '
                                  'amoksisilin-klavulanat başlamak',
                          'is_correct': False,
                          'scenario_update': 'İdrar incelemesi ve kültürü alınmadan başlanan oral '
                                             'antibiyotik kusma nedeniyle tolere edilemedi; ayrıca '
                                             'enfeksiyon odağı kanıtlanamadığı için uygun görüntüleme ve '
                                             'izlem planı yapılamadı.',
                          'teaching_point': 'Odağı belirsiz yüksek ateşi olan <24 ay süt çocuklarında tek '
                                            'başına hemogram ve CRP odak belirlemez; antibiyotik öncesi '
                                            'mutlaka kateter veya suprapubik aspirasyonla idrar örneği '
                                            'alınmalıdır.'},
                         {'text': 'Kateterizasyon yerine bebeğin bezini sıkıp alınan idrarda dipstick testi '
                                  'yapmak ve negatif çıkarsa üriner kaynaklı enfeksiyonu tamamen dışlayarak '
                                  'taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Bezden sıkılarak alınan örnekte bezin emici polimerleri '
                                             'lökositleri tuttuğu ve küçük bebeklerde sık mesane boşalması '
                                             'nedeniyle nitrit negatif kaldığı için tanı atlandı.',
                          'teaching_point': 'Bezden sıkılarak alınan örnek güvenilir değildir; ayrıca süt '
                                            'çocukları sık idrar yaptığından mesanede bekleme süresi kısa '
                                            'olur ve nitrit testi %50 den fazla vakada yalancı negatif '
                                            'çıkabilir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': '39.8°C ateş, kusma, CRP 94 mg/L, Prokalsitonin 3.8 ng/mL ve kateter idrarında '
                         'belirgin piyüri ile nitrit pozitifliği saptanan bu bebekte kesin tanınız nedir?',
             'options': [{'text': 'Ateşsiz Akut Basit Sistit (Alt İYE)',
                          'is_correct': False,
                          'scenario_update': 'Hastada 39.8°C ateş, tekrarlayan kusma ve belirgin akut faz '
                                             'reaktan yüksekliği (CRP 94 mg/L, PCT 3.8 ng/mL) mevcut olup '
                                             'tablo alt üriner sistemle sınırlı değildir.',
                          'teaching_point': 'Süt çocuklarında ≥38.5-39°C ateş ve sistemik inflamasyon '
                                            'bulguları eşlik eden idrar yolu enfeksiyonları renal parankim '
                                            'tutulumunu (akut piyelonefrit) gösterir.'},
                         {'text': 'Asemptomatik Bakteriüri ve Viral ÜSYE',
                          'is_correct': False,
                          'scenario_update': 'Hastada viral üst solunum yolu bulgusu yoktur; kateter '
                                             'idrarında her sahada 40-50 lökosit (belirgin piyüri) ve yüksek '
                                             'prokalsitonin gerçek doku invazyonunu kanıtlamaktadır.',
                          'teaching_point': 'Asemptomatik bakteriüride klinik semptom, yüksek akut faz '
                                            'reaktanı ve gerçek piyüri bulunmaz; tedavi gerektirmez.'},
                         {'text': 'Akut Piyelonefrit (Ateşli Üst İdrar Yolu Enfeksiyonu)',
                          'is_correct': True,
                          'explanation': 'Yüksek ateş, kusma, CRP ve prokalsitonin yüksekliği ile birlikte '
                                         'kateter idrarında piyüri ve nitrit pozitifliği akut renal '
                                         'parankimal enfeksiyonu (Akut Piyelonefrit) doğrular.',
                          'new_finding': 'Kesin Tanı: Akut Piyelonefrit (Ateşli Üst İdrar Yolu '
                                         'Enfeksiyonu).'},
                         {'text': 'Akut Poststreptokoksik Glomerülonefrit (APSGN)',
                          'is_correct': False,
                          'scenario_update': 'Altı aylık bebekte APSGN son derece nadirdir; ayrıca yüksek '
                                             'ateş, prokalsitonin yüksekliği ve nitrit pozitifliği '
                                             'bakteriyel piyelonefrit için tipiktir.',
                          'teaching_point': 'APSGN genellikle >2-3 yaş çocuklarda streptokoksik '
                                            'enfeksiyondan 1-3 hafta sonra makroskopik hematüri, ödem ve '
                                            'hipertansiyon ile başvurur; nitrit pozitifliği görülmez.'}]},
            {'stage_title': 'Sarı Alanda Tedavi, Görüntüleme Zamanlaması ve Yatış Planı',
             'question': 'Tekrarlayan kusması olan 6 aylık bu akut piyelonefrit hastasında kılavuzlara en '
                         'uygun antibiyoterapi, görüntüleme ve izlem planı hangisidir?',
             'options': [{'text': 'Servise yatırarak İV seftriakson ve sıvı tedavisi başlamak, üriner sistem '
                                  'ultrasonografisi planlamak ve toplam antibiyoterapi süresini 10-14 güne '
                                  'tamamlamak',
                          'is_correct': True,
                          'explanation': 'Kusması/oral intoleransı olan 6 aylık akut piyelonefrit hastası '
                                         'yatırılarak parenteral 3. kuşak sefalosporin (örn. Seftriakson '
                                         '50-75 mg/kg/gün) ile tedavi edilir; <2 yaş ilk ateşli İYE de '
                                         'anatomik anomalileri değerlendirmek için Üriner USG yapılır ve '
                                         'tedavi 10-14 güne tamamlanır.',
                          'new_finding': 'Hasta Çocuk Servisine yatırılarak İV Seftriakson ve hidrasyon '
                                         'başlandı. 48. saatte ateşi düştü, kusması durdu; kateter '
                                         'kültüründe >100.000 CFU/mL duyarlı E. coli üredi. Yapılan Üriner '
                                         'USG normal saptandı ve 10 günlük tedaviye tamamlanmak üzere oral '
                                         'sefiksim ile taburcu edildi.'},
                         {'text': 'Oral nitrofurantoin süspansiyon reçete ederek kusması için ondansetron '
                                  'vermek ve poliklinikte kontrol edilmek üzere hastayı acil servisten eve '
                                  'taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Nitrofurantoin renal parankimde ve kanda terapötik '
                                             'konsantrasyona ulaşamadığı ve bebek oral ilacı kustuğu için 24 '
                                             'saat sonra ürosepsis tablosu gelişti.',
                          'teaching_point': 'Nitrofurantoin ve fosfomisin yalnızca ateşsiz alt İYE (sistit) '
                                            'tedavisinde kullanılır; böbrek dokusu düzeyleri yetersiz '
                                            'olduğundan akut piyelonefrit tedavisinde kesinlikle '
                                            'kontrendikedir.'},
                         {'text': 'İntravenöz seftriakson başlamak ve vezikoüreteral reflüyü saptamak '
                                  'amacıyla henüz ateşli enfeksiyon devam ederken hemen bugün işeme '
                                  'sistoüretrografisi (VSUG) çekmek',
                          'is_correct': False,
                          'scenario_update': 'Aktif piyelonefrit sırasında yapılan retrograd kontrastlı '
                                             'mesane kateterizasyonu bakteriyemiyi tetikledi ve enflamasyona '
                                             'bağlı geçici vezikoüreteral reflü nedeniyle yanıltıcı sonuç '
                                             'elde edildi.',
                          'teaching_point': 'İlk ateşli İYE geçiren <2 yaş çocukta ilk basamak görüntüleme '
                                            'Üriner USG dir; VSUG rutin yapılmaz (yalnız USG de '
                                            'hidronefroz/skar bulgusu veya atipik/tekrarlayan İYE varsa '
                                            'enfeksiyon düzeldikten sonra çekilir).'},
                         {'text': 'Acil serviste tek doz intramüsküler seftriakson uyguladıktan sonra toplam '
                                  '3 günlük kısa süreli oral trimetoprim-sülfametoksazol reçete ederek '
                                  'hastayı taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Kusması devam eden 6 aylık bebekte 3 günlük kısa süreli ve E. '
                                             'coli direnci yüksek olan TMP-SMX tedavisi yetersiz kaldı; '
                                             'enfeksiyon nüks ederek renal skar riski arttı.',
                          'teaching_point': 'Akut piyelonefritte 3 günlük kısa süreli tedavi yetersizdir '
                                            '(7-14 gün gerekir); ayrıca kusması olan süt çocuğunda başlangıç '
                                            'tedavisi parenteral yoldan yapılmalıdır.'}]}]},
 {'id': 'Y10',
  'category': '🫁 Hırıltı & Solunum Sıkıntısı',
  'age': '2 Yaş',
  'gender': 'Erkek',
  'complaint': 'Sakin dururken bile duyulan tiz nefes alma sesi (stridor), kaba öksürük ve boyun çukurunda '
               'çekilme',
  'history': "Gece 03:30'da ailesi kucağında Sarı Alana getiriyor: 'Dün akşamdan beri sesi kısıktı ve hafif "
             'nezlesi vardı, gece yarısı havlar gibi kaba bir öksürük başladı. Son 1 saattir hiç ağlamazken, '
             'kucağımızda sakin otururken bile nefes alırken boğazından tiz bir ses çıkıyor ve boynunun '
             "çukuru içeri çöküyor.'",
  'final_diagnosis': 'Orta-Ağır Akut Viral Laringotrakeit (Orta-Ağır Krup)',
  'disposition': 'Sarı Alanda Nebülize L-Adrenalin + Tek Doz 0.6 mg/kg Deksametazon -> En Az 3-4 Saat '
                 'Rebound Stridor Gözlemi Sonrası Taburculuk',
  'case_pearl': 'İstirahatte (çocuk sakinken) duyulan inspiratuar stridor ve suprasternal/interkostal '
                'çekilmeler Orta-Ağır Krup (Westley skoru ≥3) göstergesidir. Tedavide tek doz Deksametazon '
                '(0.6 mg/kg oral/İM) ile birlikte Nebülize L-Adrenalin (0.5 mL/kg, maks 5 mL, 1:1000) '
                'uygulanır. Nebülize adrenalinin etkisi ~2 saatte sona erip rebound stridor '
                'gelişebileceğinden hasta en az 3-4 saat Sarı Alanda gözlemlenmeden taburcu edilmez.',
  'steps': [{'stage_title': 'Sarı Alanda Sakin Değerlendirme ve Hava Yolu Muayenesi',
             'question': 'Gece yarısı başlayan kaba öksürük, istirahatte inspiratuar stridor ve suprasternal '
                         'çekilme ile getirilen 2 yaşındaki bu çocukta ilk yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Hava yolu açıklığını net görmek için çocuğu annesinden ayırıp muayene '
                                  'masasına yatırarak abeslang ile zorlu orofarenks muayenesi yapmak ve '
                                  'damar yolu açmak',
                          'is_correct': False,
                          'scenario_update': 'Annesinden ayrılan ve abeslang ile zorlanan çocuğun şiddetli '
                                             'ağlaması dinamik üst hava yolu darlığını artırdı; türbülan '
                                             'hava akımı sonucu stridor şiddetlendi ve SpO2 %85 düzeyine '
                                             'düştü.',
                          'teaching_point': 'Akut üst hava yolu obstrüksiyonu ve stridoru olan çocuklarda '
                                            'ağlama ve ajitasyon negatif intratorasik basıncı artırarak '
                                            'dinamik darlığı ağırlaştırır; zorlu orofarenks muayenesi ve '
                                            'gereksiz ağrılı işlemlerden kaçınılmalıdır.'},
                         {'text': 'Çocuğu anne kucağında hiç ağlatmadan genel görünümünü, bilinç durumunu, '
                                  'istirahatteki stridorunu, suprasternal-interkostal çekilmelerini, akciğer '
                                  'hava girişini ve oksijen satürasyonunu değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Akut üst hava yolu darlığı olan çocukta ajitasyonu önlemek temel '
                                         'ilkedir; çocuk ebeveyn kucağında sakin tutulurken bilinç, '
                                         'istirahatte stridor, çekilmeler, hava girişi ve SpO2 '
                                         'değerlendirilerek klinik ağırlık belirlenir.',
                          'new_finding': 'Vital Bulgular: Ateş 38.0°C, KTA 144/dk, SS 38/dk, Oda havasında '
                                         'SpO2 %93. Çocuk anne kucağında sakin otururken dahi belirgin '
                                         'inspiratuar stridor duyuluyor, suprasternal ve interkostal '
                                         'çekilmeleri mevcut, akciğer bazallerinde hava girişi hafif '
                                         'azalmış. Bilinci açık, siyanoz yok, toksik görünüm veya ağızdan '
                                         'salya akışı (drooling) yok.'},
                         {'text': 'Sakinleştirmek ve solunum çabasını azaltmak amacıyla hemen 0.1 mg/kg '
                                  'intravenöz midazolam uygulayıp çocuğu sırtüstü düz pozisyonda monitörize '
                                  'izleme almak',
                          'is_correct': False,
                          'scenario_update': 'Verilen sedatif ilaç üst hava yolu kas tonusunu ve solunum '
                                             'dürtüsünü baskıladı; düz yatırılan çocukta tam hava yolu '
                                             'obstrüksiyonu ve derin hipoksemi gelişti.',
                          'teaching_point': 'Üst hava yolu obstrüksiyonu olan çocuklarda sedatif ilaçlar '
                                            'solunum çabasını ve hava yolu tonusunu baskılayarak solunum '
                                            'arrestine yol açabileceği için kesinlikle kontrendikedir.'},
                         {'text': 'Subglottik darlık derecesini objektif olarak görüntülemek için tedavi '
                                  'başlamadan önce çocuğu radyoloji ünitesine göndererek ön-arka ve yan '
                                  'boyun grafisi çektirmek',
                          'is_correct': False,
                          'scenario_update': 'Tedavi verilmeden radyolojiye gönderilen ve çekim sırasında '
                                             'pozisyon verilmeye çalışılan çocukta ağlama ile birlikte '
                                             'stridor ve retraksiyonlar ağırlaşarak hipoksemi derinleşti.',
                          'teaching_point': 'Tipik klinik bulgularla başvuran akut üst hava yolu '
                                            'obstrüksiyonunda boyun grafisi rutin olarak endike değildir ve '
                                            'acil medikal tedaviyi geciktirmemelidir.'}]},
            {'stage_title': 'Sarı Alanda Akut Medikal Müdahale Seçimi',
             'question': 'İstirahatte belirgin inspiratuar stridoru, suprasternal çekilmeleri ve oda '
                         'havasında %93 satürasyonu olan bu çocukta hemen uygulanması gereken tedavi '
                         'protokolü hangisidir?',
             'options': [{'text': 'Yalnızca soğuk buhar (mist) uygulaması yapmak ve subglottik mukozal ödemi '
                                  'çözmek için 20 dakika arayla üç doz nebülize salbutamol başlamak',
                          'is_correct': False,
                          'scenario_update': 'Soğuk buhar çocuğun yüzünü rahatsız ederek ağlamasını artırdı; '
                                             'verilen nebülize salbutamol üst hava yolu ödemini çözmediği '
                                             'gibi taşikardiyi artırdı ve stridor devam etti.',
                          'teaching_point': 'Soğuk buhar uygulamasının klinik etkinliği kanıtlanmamıştır; '
                                            'beta-2 agonist olan salbutamol ise alt hava yolu '
                                            'bronkospazmında etkilidir, subglottik üst hava yolu ödeminde '
                                            'kullanılmaz.'},
                         {'text': 'Tek başına 0.15 mg/kg oral deksametazon verip taşikardi yan etkisinden '
                                  'kaçınmak amacıyla nebülize adrenalin uygulamadan stridorun geçmesini 30 '
                                  'dakika beklemek',
                          'is_correct': False,
                          'scenario_update': 'Kortikosteroidlerin antiinflamatuar etkisi en erken 2-4 saat '
                                             'içinde başladığından, nebülize adrenalin verilmeyen hastanın '
                                             'istirahatteki stridoru, çekilmeleri ve hipoksemisi ilk saat '
                                             'boyunca devam etti.',
                          'teaching_point': 'İstirahatte stridor ve belirgin çekilmesi olan orta-ağır '
                                            'vakalarda yalnız deksametazon yeterli hızlı rahatlama sağlamaz; '
                                            'dakikalar içinde etki eden nebülize L-adrenalin mutlaka '
                                            'eklenmelidir.'},
                         {'text': 'Nebülize L-adrenalin (0.5 mL/kg, maksimum 5 mL, 1:1000) ile birlikte tek '
                                  'doz 0.6 mg/kg deksametazon uygulamak ve oksijen sağlamak',
                          'is_correct': True,
                          'explanation': 'Alfa-adrenerjik vazokonstriksiyon yapan nebülize L-adrenalin '
                                         'subglottik mukozal ödemi 10-30 dakikada hızla çözer; eş zamanlı '
                                         'verilen 0.6 mg/kg deksametazon ise 2-4 saatte devreye girerek '
                                         'kalıcı antiinflamatuar etki sağlar.',
                          'new_finding': '5 mL (1:1000) Nebülize L-Adrenalin, 0.6 mg/kg Deksametazon ve '
                                         'oksijen desteği uygulandıktan 20 dakika sonra istirahatteki '
                                         'stridor tamamen kayboldu, suprasternal çekilmeler geriledi ve oda '
                                         'havasında SpO2 %98 düzeyine yükseldi.'},
                         {'text': 'Üst hava yolu enfeksiyonunu kontrol altına almak için intravenöz '
                                  'ampisilin-sulbaktam ve metilprednizolon yükleyip eş zamanlı intramüsküler '
                                  'feniramin maleat uygulamak',
                          'is_correct': False,
                          'scenario_update': 'İntramüsküler enjeksiyon ve damar yolu işlemi çocuğu şiddetle '
                                             'ağlattı; viral kaynaklı non-histaminerjik subglottik ödemde '
                                             'antibiyotik ve antihistaminik hiçbir akut yarar sağlamadı.',
                          'teaching_point': 'Viral subglottik ödemde antibiyotiklerin ve H1 '
                                            'antihistaminiklerin yeri yoktur; akut hava yolu rahatlaması '
                                            'için nebülize adrenalin ve sistemik deksametazon standart '
                                            'tedavidir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Havlar tarzda kaba öksürük, ses kısıklığı, istirahatte inspiratuar stridor ve '
                         'nebülize adrenalin + deksametazon tedavisine hızlı yanıt doğrultusunda kesin '
                         'tanınız nedir?',
             'options': [{'text': 'Orta-Ağır Akut Viral Laringotrakeit (Orta-Ağır Krup)',
                          'is_correct': True,
                          'explanation': 'Viral prodrom sonrası gece başlayan havlar tarzda öksürük, ses '
                                         'kısıklığı, istirahatte inspiratuar stridor, çekilmeler (Westley '
                                         'skoru 5) ve nebülize adrenaline hızlı yanıt Orta-Ağır Viral Krup '
                                         'tanısını doğrular.',
                          'new_finding': 'Kesin Tanı: Orta-Ağır Akut Viral Laringotrakeit (Orta-Ağır Krup - '
                                         'Westley Skoru 5).'},
                         {'text': 'Sekonder Akut Eksüdatif Bakteriyel Trakeit',
                          'is_correct': False,
                          'scenario_update': 'Bakteriyel trakeitte çok yüksek ateş, toksik görünüm, koyu '
                                             'pürülan trakeal sekresyonlar ve nebülize adrenaline '
                                             'yanıtsızlık görülür; bu hasta ise adrenaline 20 dakikada tam '
                                             'yanıt verdi.',
                          'teaching_point': 'Nebülize adrenalin ve deksametazona dramatik yanıt veren, '
                                            'toksik görünümü olmayan tablo viral laringotrakeittir.'},
                         {'text': 'Akut Bakteriyel Supraglottit (Akut Epiglottit)',
                          'is_correct': False,
                          'scenario_update': 'Akut epiglottitte havlar tarzda öksürük beklenmez; ani '
                                             'başlayan yüksek ateş, toksik görünüm, yutma güçlüğü, ağızdan '
                                             'salya akışı (drooling) ve tripod pozisyonu görülür.',
                          'teaching_point': 'Havlar tarzda öksürük ve ses kısıklığı subglottik bölge (krup) '
                                            'tutulumunu gösterir; supraglottitte ise boğuk (hot potato) ses '
                                            've salya akışı ön plandadır.'},
                         {'text': 'Konjenital Laringomalazi ve Gastroözofageal Reflü',
                          'is_correct': False,
                          'scenario_update': 'Laringomalazi yaşamın ilk haftalarında başlayan, sırtüstü '
                                             'yatınca ve beslenirken artan kronik stridor nedenidir; 2 '
                                             'yaşında akut başlayan ateşli tablo viral kruptur.',
                          'teaching_point': 'İki yaşında akut viral prodromla başlayan havlar öksürük ve '
                                            'stridor konjenital laringomalazi değil akut viral '
                                            'laringotrakeittir.'}]},
            {'stage_title': 'Sarı Alan Gözlem Süresi (Rebound Stridor İzlemi) ve Taburculuk',
             'question': 'Nebülize L-adrenalin uygulamasından 30 dakika sonra stridoru ve çekilmeleri '
                         'tamamen düzelen çocuk için ailesi eve gitmek istiyor. Doğru yaklaşımınız nedir?',
             'options': [{'text': 'Çocuğun istirahatte stridoru kalmadığı ve oksijen satürasyonu %98 olduğu '
                                  'için evde kullanmak üzere salbutamol şurup reçete ederek hemen taburcu '
                                  'etmek',
                          'is_correct': False,
                          'scenario_update': 'Tedaviden 30 dakika sonra taburcu edilen çocukta 90. dakikada '
                                             'nebülize adrenalinin vazokonstriktör etkisi sona erdi; evde '
                                             'ağır rebound stridor ve çekilmeler tekrarlayarak acil servise '
                                             'geri getirildi.',
                          'teaching_point': 'Nebülize L-adrenalinin etkisi yaklaşık 2 saat içinde biter ve '
                                            'subglottik ödem tekrarlayabilir (rebound fenomeni); bu nedenle '
                                            'hiçbir hasta ilk 1 saat içinde taburcu edilmemelidir.'},
                         {'text': 'Hastayı sadece 1 saat gözlemde tutup stridor tekrarlamazsa evde buhar '
                                  'makinesiyle uygulamaları için aileye adrenalin ampul reçete ederek '
                                  'taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Bir saatlik gözlem rebound stridoru dışlamak için yetersiz '
                                             'kaldı; ayrıca evde kontrolsüz dozda uygulanan nebülize '
                                             'adrenalin çocukta ciddi taşikardi ve ajitasyona yol açtı.',
                          'teaching_point': 'Nebülize adrenalin sonrası gözlem süresi en az 3-4 saat '
                                            'olmalıdır ve nebülize adrenalin yalnızca hastane ortamında '
                                            'monitörize edilerek uygulanır, eve reçete edilmez.'},
                         {'text': 'Tek doz nebülize adrenalin alan her krup hastasında entübasyon riski '
                                  'yüksek olduğundan klinik yanıt tam olsa bile çocuk yoğun bakıma yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Tek doz nebülize adrenalin ve deksametazon sonrası tamamen '
                                             'düzelen ve 4 saat boyunca istirahatte stridoru tekrarlamayan '
                                             'hastada gereksiz yoğun bakım yatışı yapıldı.',
                          'teaching_point': 'Tek doz nebülize adrenalin ve deksametazon sonrası 3-4 saatlik '
                                            'gözlemde istirahatte stridoru ve çekilmesi tekrarlamayan '
                                            'hastalar yatış gerekmeden güvenle taburcu edilebilir; yatış '
                                            'tekrarlayan adrenalin gereksiniminde endikedir.'},
                         {'text': 'Rebound stridor riski nedeniyle en az 3-4 saat izlemek; 4. saatte '
                                  'istirahatte stridor ve çekilme yoksa kırmızı bayraklarla taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Nebülize adrenalinin etkisi ~2 saatte geçerken deksametazonun '
                                         'etkisi 2-4 saatte başlar; hasta en az 3-4 saat izlenmeli, bu '
                                         'sürede istirahatte stridor tekrarlamaz, SpO2 normal ve oral alımı '
                                         'iyi ise taburcu edilmelidir.',
                          'new_finding': 'Hasta Sarı Alanda 4 saat boyunca izlendi; rebound stridor veya '
                                         'çekilme gelişmedi, oda havasında SpO2 %99 ve sıvı alımı iyi olduğu '
                                         'görülerek aileye kırmızı bayrak eğitimi verilip taburcu '
                                         'edildi.'}]}]}]
