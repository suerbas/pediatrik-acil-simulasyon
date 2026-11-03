# -*- coding: utf-8 -*-
"""
Yeşil Alan Simülasyon Vakaları - Bölüm 7 (G61 - G70)
"""

GREEN_CASES_PART7 = [{'id': 'G61',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '4 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Bir hafta önceki soğuk algınlığının ardından bu sabah aniden başlayan sağ bacağına basamama ve '
               'topallama',
  'history': "Dört yaşındaki erkek çocuk babasının kucağında getiriliyor: 'Bir hafta önce hafif burun akıntısı ve "
             'öksürüğü olmuştu, ilaçsız düzelmişti. Bu sabah uyandığında yataktan kalkamadı, sağ bacağının üzerine '
             'basınca acıdığını söyleyip ağladı ve topallayarak yürüdü. Ateşi hiç çıkmadı, düşme ya da çarpma öyküsü '
             "kesinlikle yok. İştahı ve neşesi gayet yerinde.'",
  'final_diagnosis': 'Geçici Toksik Sinovit (Transient Synovitis / Viral Enfeksiyon Sonrası Benign Kalça Efüzyonu)',
  'disposition': 'Yeşil Alandan İstirahat ve Oral NSAİİ Önerisi, 48-72 Saat Sonra Poliklinik Kontrolü ile Taburculuk',
  'case_pearl': 'Geçici toksik sinovit, 3-8 yaş arası çocuklarda ani başlayan ağrısız veya hafif ağrılı topallamanın '
                "EN SIK nedenidir. Genellikle viral bir ÜSYE'den 1-2 hafta sonra gelişir. En kritik ayırıcı tanı "
                'SEPTİK ARTRİTTİR! Septik artrit ayrımında KOCHER KRİTERLERİ kullanılır: 1) Ateş >38.5°C, 2) Ağırlık '
                'verememe, 3) ESH >40 mm/saat, 4) BK >12.000/mm³. Toksik sinovitte çocuk sistemik olarak sağlıklıdır, '
                "toksik değildir, USG'de her iki kalçada minimal sıvı görülebilir. Tedavi yatak istirahati ve "
                "ibuprofen gibi NSAİİ'lerdir; tablo 7-10 günde sekel bırakmadan tamamen geriler.",
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Ateşi olmayan ancak topallayan bu çocukta fizik muayenede öncelikle hangi bulguları '
                         'değerlendirmelisiniz?',
             'options': [{'text': 'Kalça eklem hareket açıklığını, lokal ısı artışını, hassasiyeti ve yürüyüş '
                                  'paternini dikkatlice değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Kalçada pasif hareket açıklığı (özellikle iç rotasyon ve abdüksiyon) '
                                         'değerlendirilir. Benign post-viral kalça efüzyonunda hareket açıklığı hafif '
                                         'kısıtlıdır ancak septik artritteki gibi psödoparalizi ve çığlık olmaz.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 94/dk, SS 20/dk, SpO2 %99, TA 94/60 mmHg. '
                                         'Çocuk muayene masasında otururken neşeli. Sağ kalça pasif iç rotasyon ve '
                                         'abdüksiyonunun son derecelerinde hafif huzursuzlanıyor ancak hareket '
                                         'serbest. Ciltte kızarıklık, şişlik veya belirgin ısı artışı yok. Diz ve ayak '
                                         'bileği eklemleri tamamen doğal, nörovasküler muayene tam.'},
                         {'text': 'Hastaya derhal genel anestezi altında acil kalça eklemi artrotomi cerrahisi '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ateşsiz ve stabil çocukta gereksiz invaziv cerrahi girişim eklem içi '
                                             'iyatrojenik enfeksiyona yol açtı.',
                          'teaching_point': 'Ateşi olmayan, vital bulguları stabil çocukta cerrahi artrotomi '
                                            'kesinlikle ilk basamak değildir.'},
                         {'text': 'Bacak ağrısını lomber disk hernisi lehine yorumlayıp acil omurga ameliyatı istemek',
                          'is_correct': False,
                          'scenario_update': 'Pediatrik yaş grubunda disk hernisi son derece nadirdir; gereksiz omurga '
                                             'incelemeleri zaman kaybettirdi.',
                          'teaching_point': 'Küçük çocukta kalça patolojileri sıklıkla diz veya uyluk ağrısı olarak '
                                            'yansır; disk hernisi düşünülmez.'},
                         {'text': 'Topallamayı basit büyüme ağrısı sayıp çocuğu hiçbir muayene yapmadan eve göndermek',
                          'is_correct': False,
                          'scenario_update': 'Muayenesiz taburculuk ailede güvensizlik yarattı; olası septik artrit '
                                             'dışlanamadı.',
                          'teaching_point': 'Gündüz olan, tek taraflı topallama asla büyüme ağrısı değildir; mutlaka '
                                            'fizik muayene gerektirir.'}]},
            {'stage_title': 'Laboratuvar ve İleri İncelemeler',
             'question': 'Septik artrit şüphesini ekarte etmek ve tanıyı netleştirmek için en uygun inceleme '
                         'kombinasyonu hangisidir?',
             'options': [{'text': 'Tam kan sayımı, CRP, sedimentasyon düzeyi ve her iki kalçanın bilateral '
                                  'ultrasonografisini istemek',
                          'is_correct': True,
                          'explanation': 'Kocher kriterlerini değerlendirmek için WBC ve ESH/CRP bakılır. Kalça USG '
                                         'eklem efüzyonunu ve kapsül kalınlaşmasını göstermede en duyarlı, '
                                         'radyasyonsuz ilk basamak yöntemdir.',
                          'new_finding': 'Laboratuvar: WBC 7.800/mm³ (Normal), CRP 2.1 mg/L (Normal), ESH 12 mm/saat '
                                         '(Normal). Bilateral Kalça USG: Sağ kalça eklem aralığında yaklaşık 4 mm '
                                         'kalınlığında, anekoik, temiz minimal seröz sıvı birikimi (hafif kapsüler '
                                         'distansiyon) izlendi; sol kalça eklemi tamamen doğal. Kemik korteksleri '
                                         'intakt.'},
                         {'text': 'Hastalık şüphesiyle acil olarak tüm vücut kemik sintigrafisi ve tüm omurga '
                                  'tomografisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk gereksiz yere yüksek doz radyasyona maruz kaldı; USG ile kolayca '
                                             'çözülecek vaka uzadı.',
                          'teaching_point': 'Kalça efüzyonunda ilk basamak radyasyonsuz ultrasonografidir; tomografi '
                                            've sintigrafi endike değildir.'},
                         {'text': 'Septik artriti kesin dışlamak amacıyla floroskopi eşliğinde acil körleme eklem '
                                  'aspirasyonu yapmak',
                          'is_correct': False,
                          'scenario_update': 'Kocher kriterleri negatif olan ve efüzyonu minimal olan ekleme iğne '
                                             'sokulması enfeksiyon riski yarattı.',
                          'teaching_point': 'Enflamatuar belirteçleri normal ve efüzyonu hafif çocukta invaziv eklem '
                                            'ponksiyonu yapılmaz.'},
                         {'text': 'Hiçbir tetkik yapmadan çocuğa doğrudan geniş spektrumlu intravenöz antibiyotik '
                                  'kombinasyonu başlamak',
                          'is_correct': False,
                          'scenario_update': 'Viral kökenli benign efüzyonda gereksiz antibiyotik kullanımı bağırsak '
                                             'florasını bozdu ve ishal başlattı.',
                          'teaching_point': 'Benign eklem efüzyonunda antibiyotiklerin yeri yoktur; bakteriyel kanıt '
                                            'olmadan antibiyotik verilmez.'}]},
            {'stage_title': 'Klinik Ön Tanı ve Ayırıcı Tanı',
             'question': "Viral enfeksiyon sonrası gelişen, belirteçleri normal ve USG'de seröz efüzyon saptanan "
                         'hastada tanınız nedir?',
             'options': [{'text': 'Geçici toksik sinovit tablosu',
                          'is_correct': True,
                          'explanation': 'Viral enfeksiyon öyküsü, ateşsizlik, normal inflamatuar belirteçler ve '
                                         "USG'de seröz efüzyon geçici toksik sinovit için klasik tablodur.",
                          'new_finding': 'Kesin Tanı: Geçici Toksik Sinovit doğrulanmıştır. Aileye durum açıklanarak '
                                         'tedavi aşamasına geçildi.'},
                         {'text': 'Akut bakteriyel septik artrit',
                          'is_correct': False,
                          'scenario_update': 'Septik artritte yüksek ateş, lökositoz, yüksek CRP ve eklemde pürülan '
                                             'yoğun sıvı beklenirdi.',
                          'teaching_point': 'Septik artrit kliniği çok daha gürültülüdür; belirteçler yüksektir ve '
                                            'eklem hareketleri tamamen kilitlidir.'},
                         {'text': 'Legg-Calve-Perthes femur başı nekrozu',
                          'is_correct': False,
                          'scenario_update': 'Perthes haftalarca süren sinsi ağrı ve grafide femur başında avasküler '
                                             'nekroz bulguları ile seyreder.',
                          'teaching_point': 'Perthes sinsi ve kronik bir tablodur; akut post-viral başlangıç toksik '
                                            'sinoviti işaret eder.'},
                         {'text': 'Juvenil idiopatik artrit atağı',
                          'is_correct': False,
                          'scenario_update': 'JİA tanısı için artritin en az 6 hafta sürmesi gerekir; akut başlangıçlı '
                                             'tek taraflı tabloda düşünülmez.',
                          'teaching_point': 'JİA kronik artrit kategorisindedir; 6 haftadan kısa süreli tablolarda bu '
                                            'tanı konulamaz.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Geçici toksik sinovit tanısı kesinleşen bu çocuğun Yeşil Alandaki en uygun tedavisi ve '
                         'taburculuk planı nedir?',
             'options': [{'text': 'Yatak istirahati ve oral ibuprofen tedavisi önermek, üç gün sonra poliklinik '
                                  'kontrolüne çağırmak',
                          'is_correct': True,
                          'explanation': 'Tedavinin temeli ağırlık bindirmekten kaçınmak (yatak istirahati) ve oral '
                                         "NSAİİ'dir (İbuprofen 30-40 mg/kg/gün). Ateş çıkarsa veya ağrı artarsa derhal "
                                         'acile dönmesi tembihlenir; 48-72 saat sonra poliklinikte kontrol edilir.',
                          'new_finding': 'İbuprofen başlandı ve istirahat önerildi. Aileye alarm bulguları anlatıldı. '
                                         '3 gün sonra kontrolde topallamasının tamamen geçtiği, koşup oynadığı ve '
                                         "USG'deki sıvının kaybolduğu görüldü."},
                         {'text': 'Hastanın sağ bacağını altı hafta süreyle tam sirküler kalça alçısına alıp '
                                  'hareketsiz bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz alçı uygulaması kas atrofisine, eklem sertliğine ve cilt bası '
                                             'yaralarına neden oldu.',
                          'teaching_point': 'Toksik sinovitte alçı veya traksiyon uygulanmaz; kısa süreli istirahat ve '
                                            'analjezik yeterlidir.'},
                         {'text': 'Hemen damar yolu açarak hastaya üç hafta boyunca parenteral aminoglikozid '
                                  'antibiyotik tedavisi vermek',
                          'is_correct': False,
                          'scenario_update': 'Steril post-viral efüzyonda gereksiz yatış ve nefrotoksik antibiyotik '
                                             'uygulaması böbrek hasarı doğurdu.',
                          'teaching_point': 'Hastalık enfeksiyöz değil, post-viral reaktiftir; antibiyotik endikasyonu '
                                            'kesinlikle yoktur.'},
                         {'text': 'Eklemdeki sıvıyı tamamen boşaltmak amacıyla günde üç kez tekrarlayan iğne '
                                  'aspirasyonları uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Tekrarlayan eklem ponksiyonları steril eklemi bakteriyel enfeksiyona '
                                             'açarak iyatrojenik septik artrit yaptı.',
                          'teaching_point': 'Küçük miktardaki benign sıvı vücut tarafından günler içinde kendiliğinden '
                                            'emilir; aspire edilmez.'}]}]},
 {'id': 'G62',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '9 Yaşında',
  'gender': 'Kız',
  'complaint': 'Dört saattir süren şiddetli zonklayıcı baş ağrısı, bulantı, odanın ışığından ve sesten rahatsız olma',
  'history': "Dokuz yaşındaki kız çocuğu annesiyle Yeşil Alana başvuruyor: 'Bugün okulda öğleden sonra aniden başının "
             'sağ tarafında zonklayıcı, damar atar gibi çok şiddetli bir ağrı başladı. Eve gelince iki kez safra '
             'kustu. Gözlerini açamıyor, ışık ve televizyon sesi ağrısını çok artırıyor, karanlık odaya kapanmak '
             'istiyor. Annesinde de gençliğinden beri benzer zonklayıcı baş ağrıları var. Ateşi yok, sabah fışkırır '
             "kusması veya uykudan uyandıran baş ağrısı daha önce hiç olmamıştı.'",
  'final_diagnosis': 'Pediatrik Migren (Çocukluk Çağı Aurasız Migren Atağı)',
  'disposition': 'Yeşil Alanda Karanlık/Sessiz Odada Dinlendirme, Erken Basamak Analjezi, Hidrasyon ve Taburculuk',
  'case_pearl': 'Pediatrik migren çocuklarda tekrarlayan baş ağrılarının en sık primer nedenlerinden biridir. '
                'Erişkinlerin aksine çocuklarda migren ağrısı sıklıkla BİLATERAL (frontotemporal) olabilir ve atak '
                "süresi daha kısadır (2-72 saat). Tanıda EN ÖNEMLİ basamak 'Kırmızı Bayrakları' (Red Flags) "
                'dışlamaktır: 1) Sabah fışkırır kusma, 2) Uykudan uyandıran ağrı, 3) Egzersiz/öksürükle artış, 4) '
                'Nörolojik defisit, 5) Papilödem, 6) <3 yaş baş ağrısı. Kırmızı bayrak yoksa acil beyin BT/MRG '
                'ÇEKİLMEZ! Tedavide en kritik kural İLAÇLARIN ATAĞIN EN BAŞINDA (ilk 30 dakika içinde) verilmesidir: '
                'İbuprofen (10 mg/kg) veya Parasetamol (15 mg/kg), karanlık/sessiz oda, oral hidrasyon ve uyku.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Zonklayıcı baş ağrısı ve fotofobisi olan bu çocukta fizik muayenede öncelikle hangi '
                         'bulguları araştırmalısınız?',
             'options': [{'text': 'Kapsamlı nörolojik muayene yapmak, meningeal irritasyon bulgularını ve fundoskopide '
                                  'papilödemi titizlikle değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Kafa içi basınç artışı sendromu (KİBAS) ve intrakraniyal lezyonları dışlamak '
                                         'için nörolojik muayene, ense sertliği ve optik disk sınırları (papilödem) '
                                         'değerlendirilir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 82/dk, SS 18/dk, SpO2 %99, TA 102/64 mmHg. '
                                         'Çocuk ışıktan gözlerini kısıyor, alnını tutuyor. Bilinç açık, koopere ve '
                                         'oryante. Kraniyal sinir muayenesi intakt. Ense sertliği, Kernig ve '
                                         'Brudzinski negatif. Serebellar testler normal. Fundoskopik muayenede her iki '
                                         'optik disk sınırları net, venöz pulsasyon mevcut, papilödem saptanmadı.'},
                         {'text': 'Hastayı hiç muayene etmeden baş ağrısının histerik olduğunu söyleyip psikiyatriye '
                                  'sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'Muayenesiz psikiyatrik etiketleme aileyi öfkelendirdi ve organik '
                                             'patolojiler dışlanamadı.',
                          'teaching_point': 'Her akut baş ağrısı organik ve intrakraniyal aciller dışlanana kadar '
                                            'tıbbi bir acil olarak ele alınır.'},
                         {'text': 'Menenjit şüphesiyle çocuğu derhal izole edip acil floroskopi altında lomber '
                                  'ponksiyon yapmak',
                          'is_correct': False,
                          'scenario_update': 'Ateşi olmayan, ense sertliği bulunmayan ve bilinci berrak çocukta '
                                             'invaziv ponksiyon anksiyete yarattı.',
                          'teaching_point': 'Ateş, letarji veya menenjizm bulgusu olmayan tipik baş ağrısında lomber '
                                            'ponksiyon endike değildir.'},
                         {'text': 'Kafasında anevrizma kanaması düşünerek hiçbir inceleme yapmadan acil kraniyotomi '
                                  'ameliyatına almak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz cerrahi hazırlığı ve sedasyon stabil hastada solunum '
                                             'depresyonuna yol açtı.',
                          'teaching_point': 'Ani gök gürültüsü baş ağrısı (thunderclap) veya koma olmadan anevrizma '
                                            'cerrahisi düşünülmez.'}]},
            {'stage_title': 'Laboratuvar ve İleri İncelemeler',
             'question': 'Nörolojik muayenesi tamamen doğal, kırmızı bayrağı olmayan bu hastada tanısal yaklaşım nasıl '
                         'olmalıdır?',
             'options': [{'text': 'Kırmızı bayrak bulunmadığı için acil nörogörüntüleme yapmadan tanıyı klinik '
                                  'kriterlerle güvenle koymak',
                          'is_correct': True,
                          'explanation': 'Amerikan Nöroloji Akademisi (AAN) kılavuzuna göre nörolojik muayenesi normal '
                                         'olan, kırmızı bayrak taşımayan çocukluk çağı primer vasküler ataklarında '
                                         'acil BT veya MRG ÇEKİLMESİ ÖNERİLMEZ. Tanı tamamen kliniktir.',
                          'new_finding': 'Hastada kırmızı bayrak (fışkırır kusma, papilödem, fokal defisit, travma) '
                                         'saptanmadı. Anne ve teyzede benzer baş ağrısı öyküsü mevcut. Klinik tablo '
                                         'Uluslararası Baş Ağrısı Sınıflaması (ICHD-3) çocukluk çağı vasküler baş '
                                         'ağrısı kriterlerini tam olarak karşılamaktadır. Gereksiz iyonizan '
                                         'radyasyondan kaçınıldı.'},
                         {'text': 'Tümör şüphesini tamamen dışlamak amacıyla acil kontrastlı tüm kafa beyin '
                                  'tomografisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz kontrastlı BT çekimi çocuğa yüksek doz iyonize radyasyon '
                                             'yükledi ve alerjik reaksiyon yarattı.',
                          'teaching_point': 'Nörolojik muayenesi normal çocukta rutin BT çekilmez; kanserojen '
                                            'radyasyon riskinden kaçınılmalıdır.'},
                         {'text': 'Beyin kan akımını görmek için acil dört damar invaziv serebral kateter '
                                  'anjiyografisi uygulamak',
                          'is_correct': False,
                          'scenario_update': 'İnvaziv kateter anjiyografi femoral arter hematomuna ve ciddi spazma '
                                             'neden oldu.',
                          'teaching_point': 'Primer baş ağrılarında invaziv anjiyografinin hiçbir yeri yoktur; '
                                            'tehlikeli ve gereksizdir.'},
                         {'text': 'Baş ağrısı tanısını laboratuvarda doğrulamak için hastadan yüz elli parametrelik '
                                  'otoantikor paneli göndermek',
                          'is_correct': False,
                          'scenario_update': 'Pahalı ve gereksiz romatolojik testlerin tamamı negatif geldi, aileye '
                                             'yüksek maliyet bindi.',
                          'teaching_point': 'Primer baş ağrıları biyokimyasal bir testle tanı almaz; tanı klinik '
                                            'anamnez ve muayene ile konur.'}]},
            {'stage_title': 'Klinik Ön Tanı ve Ayırıcı Tanı',
             'question': 'Zonklayıcı tek taraflı baş ağrısı, bulantı ve fotofobisi olan, nörolojisi doğal bu hastada '
                         'tanınız nedir?',
             'options': [{'text': 'Pediatrik aurasız migren atağı',
                          'is_correct': True,
                          'explanation': 'Zonklayıcı baş ağrısı, fotofobi, fonofobi, kusma ve aile öyküsü ile normal '
                                         'nörolojik muayene çocukluk çağı migreni için patognomoniktir.',
                          'new_finding': 'Kesin Tanı: Pediatrik Aurasız Migren Atağı doğrulanmıştır. Aileye durum '
                                         'açıklanarak tedavi basamağına geçildi.'},
                         {'text': 'Akut bakteriyel menenjit tablosu',
                          'is_correct': False,
                          'scenario_update': 'Menenjitte yüksek ateş, ense sertliği, toksik görünüm ve letarji '
                                             'beklenirdi; hastada ateş yoktur.',
                          'teaching_point': 'Ateşsiz ve ense sertliği olmayan hastada menenjit düşünülmez.'},
                         {'text': 'Kronik gerilim tipi baş ağrısı',
                          'is_correct': False,
                          'scenario_update': 'Gerilim baş ağrısı zonklayıcı değildir; bant şeklinde basıcıdır ve kusma '
                                             'veya fotofobi beklenmez.',
                          'teaching_point': 'Gerilim tipi baş ağrısında zonklama, kusma ve fotofobi/fonofobi '
                                            'birlikteliği görülmez.'},
                         {'text': 'Akut intrakraniyal epidural hematom',
                          'is_correct': False,
                          'scenario_update': 'Epidural hematomda kafa travması öyküsü, berrak aralık ve giderek '
                                             'derinleşen koma görülür.',
                          'teaching_point': 'Travma öyküsü ve nörolojik kayıp olmadan epidural hematom düşünülmez.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Akut migren atağındaki bu çocuğun Yeşil Alandaki en uygun kanıta dayalı tedavisi hangisidir?',
             'options': [{'text': 'Karanlık sessiz odaya almak, oral ibuprofen ve hidrasyon verip uyumasını '
                                  'desteklemek',
                          'is_correct': True,
                          'explanation': 'Pediatrik migren atağında ilk basamak kanıta dayalı tedavi oral İbuprofen '
                                         '(10 mg/kg) veya Parasetamoldür (15 mg/kg). Karanlık, serin ve sessiz bir '
                                         'ortamda uyku atağı en hızlı sonlandıran faktördür. Sıvı desteği sağlanır.',
                          'new_finding': 'Karanlık ve sessiz gözlem odasına alındı. Oral ibuprofen ve soğuk kompres '
                                         'uygulandı. Yaklaşık 1 saatlik derin uykunun ardından uyandığında baş '
                                         'ağrısının ve bulantısının tamamen geçtiği görüldü.'},
                         {'text': 'Ağrıyı hemen kesmek amacıyla hastaya intravenöz yüksek doz morfin infüzyonu '
                                  'başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Opioid uygulaması çocukta şiddetli solunum depresyonu ve bağımlılık '
                                             'riski yarattı.',
                          'teaching_point': 'Migrende opioidlerin yeri yoktur; rebound baş ağrısı ve solunum '
                                            'depresyonu yapar.'},
                         {'text': 'Ağrı geçene kadar çocuğa aralıksız parlak floresan ışıklı odada matematik testi '
                                  'çözdürmek',
                          'is_correct': False,
                          'scenario_update': 'Görsel ve bilişsel stres fotofobik migren atağını şiddetlendirdi ve '
                                             'inatçı kusma tetikledi.',
                          'teaching_point': 'Fotofobisi olan çocuk mutlak loş ve sessiz ortama alınmalıdır; duyusal '
                                            'uyaranlar ağrıyı artırır.'},
                         {'text': 'Hiçbir ağrı kesici vermeden hastayı derhal genel anestezi ile acil elektroşok '
                                  'tedavisine almak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz anestezi ve orantısız müdahale hastada ciddi psikolojik travma '
                                             've taşikardi yarattı.',
                          'teaching_point': 'Akut migren basit oral analjezikler ve istirahatle tedavi edilir; invaziv '
                                            'girişim yapılamaz.'}]}]},
 {'id': 'G63',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '6 Yaşında',
  'gender': 'Kız',
  'complaint': 'İki gündür idrar yaparken yanma, tuvalete yetişememe ve sık sık idrara çıkma şikayeti',
  'history': "Altı yaşındaki kız çocuğu annesiyle Yeşil Alana geliyor: 'İki gündür çişini yaparken çok yandığını "
             'söyleyip ağlıyor. Günde on beş kez tuvalete koşuyor ama her seferinde sadece birkaç damla yapıyor. Dün '
             'okulda iki kez altına kaçırdı. Ateşi hiç çıkmadı, karnında ya da böğründe şiddetli ağrısı yok, kusması '
             "olmadı. Bir ay önce havuz tatiline gitmiştik.'",
  'final_diagnosis': 'Akut Basit Sistit (Ateşsiz Alt İdrar Yolu Enfeksiyonu)',
  'disposition': 'Yeşil Alandan İdrar Tetkiki ve Kültürü Sonrası Oral Antibiyotik Tedavisi ile Taburculuk',
  'case_pearl': 'Akut sistit, kız çocuklarında kısa üretra nedeniyle özellikle tuvalet eğitimi ve havuz sonrası sık '
                'görülen alt İYE tablosudur. En önemli klinik ayrım PİYELONEFRİTTİR (Üst İYE): Sistitte sistemik '
                'bulgular (yüksek ateş, kusma, toksisite, böğür hassasiyeti) YOKTUR! Sadece lokal mesane irritasyon '
                "bulguları (dizüri, pollaküri, sıkışma, sekonder gündüz enürezisi) vardır. TİT'te lökositüri ve nitrit "
                'pozitifliği tanıyı destekler, idrar kültürü mutlaka antibiyotik öncesi alınmalıdır. Tedavi ayaktan '
                '3-5 günlük oral antibiyotiktir (Amoksisilin-klavulanat, Sefaleksin veya Sefiksim); yatış gerekmez.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'İdrar yaparken yanma ve sık idrara çıkma şikayeti olan bu çocukta fizik muayenede öncelikle '
                         'nelere bakılmalıdır?',
             'options': [{'text': 'Vital bulguları, kostovertebral açı hassasiyetini, suprapubik duyarlılığı ve '
                                  'eksternal genital bölgeyi muayene etmek',
                          'is_correct': True,
                          'explanation': 'Piyelonefriti dışlamak için ateş ve kostovertebral açı (KVA) hassasiyetine '
                                         'bakılır. Mesane enfeksiyonlarında suprapubik hassasiyet olabilir ancak KVA '
                                         'hassasiyeti negatiftir. Vulvovajinit açısından genital muayene yapılır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 86/dk, SS 18/dk, SpO2 %99, TA 98/62 mmHg. '
                                         'Genel durumu iyi, aktif, neşeli. Batın muayenesinde defans veya rebound yok; '
                                         'hafif suprapubik hassasiyet mevcut. Bilateral kostovertebral açı hassasiyeti '
                                         '(KVAH) kesinlikle yok. Eksternal genital muayenede belirgin vulvit veya '
                                         'akıntı saptanmadı, labial sinekşi yok.'},
                         {'text': 'Hastada akut apandisit perforasyonu düşünerek acil cerrahi eksplorasyon ameliyatı '
                                  'başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Ateşsiz ve sağ alt kadran hassasiyeti olmayan hastada gereksiz cerrahi '
                                             'komplikasyon yarattı.',
                          'teaching_point': 'İzole dizüri ve pollaküri alt üriner sistem bulgularıdır; apandisit '
                                            'kliniğiyle uyumsuzdur.'},
                         {'text': 'Mesane tümörü şüphesiyle çocuğu derhal genel anestezi altında acil sistoskopiye '
                                  'almak',
                          'is_correct': False,
                          'scenario_update': 'Pediatrik yaşta mesane tümörü son derece nadirdir; invaziv sistoskopi '
                                             'üretral darlık oluşturdu.',
                          'teaching_point': 'Basit dizüride invaziv sistoskopi yapılmaz; idrar tahlili ile başlanır.'},
                         {'text': 'Hastanın şikayetlerini tamamen psikolojik sayıp hiçbir tetkik yapmadan eve yollamak',
                          'is_correct': False,
                          'scenario_update': 'Tedavi edilmeyen bakteriyel enfeksiyon yukarı tırmanarak akut '
                                             'piyelonefrit ve yüksek ateşe yol açtı.',
                          'teaching_point': 'Akut başlayan dizüri ve ani gündüz kaçırmaları aksi kanıtlanana kadar '
                                            'organik İYE kabul edilir.'}]},
            {'stage_title': 'Laboratuvar ve İleri İncelemeler',
             'question': 'Ateşi ve böğür hassasiyeti olmayan bu hastada tanıyı doğrulamak için en uygun tetkik '
                         'yaklaşımı hangisidir?',
             'options': [{'text': 'Temiz orta akım idrar örneğinden tam idrar tahlili yapmak ve idrar kültürü '
                                  'göndermek',
                          'is_correct': True,
                          'explanation': 'İdrar çubuğunda (dipstick) lökosit esteraz ve nitrit pozitifliği, '
                                         'mikroskopide piyüri bakteriyel enfeksiyonu gösterir. Antibiyotik başlanmadan '
                                         'önce etkeni ve duyarlılığı belirlemek için idrar kültürü mutlaka '
                                         'alınmalıdır.',
                          'new_finding': 'Tam İdrar Tahlili (TİT): Dansite 1020, pH 6.0, Lökosit esteraz (+++), Nitrit '
                                         '(+), Protein negatif, Glukoz negatif. Mikroskopi: Her sahada 35-40 lökosit, '
                                         'bol bakteri, eritrosit 1-2. İdrar kültürü antibiyotik öncesi besiyerine '
                                         'ekildi.'},
                         {'text': 'Tüm böbrek fonksiyonlarını değerlendirmek için acil bilateral invaziv renal '
                                  'anjiyografi çekmek',
                          'is_correct': False,
                          'scenario_update': 'İnvaziv renal anjiyografi kontrast nefropatisi ve femoral hematom '
                                             'geliştirdi.',
                          'teaching_point': 'Alt İYE tanısında anjiyografinin yeri yoktur; basit idrar analizi '
                                            'yeterlidir.'},
                         {'text': 'Böbrek yetmezliği şüphesiyle hastaya acil hemodiyaliz kateteri takarak diyalize '
                                  'başlamak',
                          'is_correct': False,
                          'scenario_update': 'Normal böbrek fonksiyonlarına sahip stabil çocukta diyaliz kateteri '
                                             'ciddi enfeksiyon kaynağı oldu.',
                          'teaching_point': 'Basit alt İYE böbrek fonksiyonlarını bozmaz; üre/kreatinin normaldir, '
                                            'diyaliz gerekmez.'},
                         {'text': 'İdrar tahlili yapmadan sadece kanda sedef ve egzama otoantikor panellerini çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz dermatolojik antikorlar negatif geldi; idrar tahlili '
                                             'yapılmadığı için tanı gecikti.',
                          'teaching_point': 'Üriner yakınmalarda ilk ve vazgeçilmez inceleme tam idrar tahlilidir.'}]},
            {'stage_title': 'Klinik Ön Tanı ve Ayırıcı Tanı',
             'question': 'Ateşsiz seyreden, dizüri ve pollakürisi olan, idrarında piyüri ve nitrit pozitif saptanan '
                         'hastada tanınız nedir?',
             'options': [{'text': 'Akut basit sistit enfeksiyonu',
                          'is_correct': True,
                          'explanation': 'Yüksek ateş, kusma ve kostovertebral açı hassasiyeti olmaksızın izole '
                                         'dizüri, pollaküri, piyüri ve nitrit pozitifliği akut sistit için tam '
                                         'uyumludur.',
                          'new_finding': 'Kesin Tanı: Akut Basit Sistit doğrulanmıştır. Aileye durum açıklanarak oral '
                                         'tedaviye geçildi.'},
                         {'text': 'Akut piyelonefrit böbrek enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Piyelonefritte yüksek ateş (genellikle >38.5°C), böğür ağrısı, kusma ve '
                                             'toksisite beklenir.',
                          'teaching_point': 'Sistiti piyelonefritten ayıran en temel fark ateş ve sistemik '
                                            'toksisitenin olmamasıdır.'},
                         {'text': 'Primer noktürnal monosemptomatik enürezis',
                          'is_correct': False,
                          'scenario_update': 'Enüreziste idrar tahlili tamamen normaldir; dizüri, piyüri ve gündüz '
                                             'pollakürisi olmaz.',
                          'teaching_point': 'Piyüri ve dizüri varlığı primer enürezisi dışlar; altta yatan enfeksiyonu '
                                            'kanıtlar.'},
                         {'text': 'Akut glomerülonefrit nefritik sendrom',
                          'is_correct': False,
                          'scenario_update': 'Glomerülonefritte çay rengi idrar, masif hematüri, hipertansiyon ve ödem '
                                             'görülür.',
                          'teaching_point': 'Glomerülonefrit mikroskopisinde eritrosit silendirleri görülür; '
                                            'lökositüri ve nitrit ön planda değildir.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Akut basit sistit tanısı alan genel durumu stabil bu çocuğun en uygun tedavisi ve aile '
                         'eğitimi nedir?',
             'options': [{'text': 'Oral antibiyotik başlamak, bol su içmesini ve genital hijyen kurallarını anlatıp '
                                  'taburcu etmek',
                          'is_correct': True,
                          'explanation': "Pediatrik alt İYE'de ilk seçenek oral amoksisilin-klavulanat (40-50 "
                                         'mg/kg/gün) veya oral sefalosporindir (örn. sefiksim/sefaleksin) ve süre 3-5 '
                                         'gündür. Bol sıvı tüketimi bakterilerin yıkanmasını sağlar. Arkadan öne değil '
                                         'önden arkaya silme eğitimi verilir.',
                          'new_finding': 'Oral amoksisilin-klavulanat başlandı. Bol su tüketimi ve hijyen eğitimi '
                                         'verildi. Tedavinin 48. saatinde idrar yaparken yanması tamamen düzeldi. '
                                         'Kültürde 100.000 cfu/mL E. coli üredi ve başlanan ilaca duyarlı geldi.'},
                         {'text': 'Hastayı yoğun bakıma yatırarak üç hafta boyunca santral yoldan üçlü parenteral '
                                  'antibiyotik vermek',
                          'is_correct': False,
                          'scenario_update': 'Basit sistitte gereksiz santral kateter ve yoğun bakım yatışı kateter '
                                             'sepsisi doğurdu.',
                          'teaching_point': 'Ateşsiz basit sistit tamamen ayaktan oral yolla tedavi edilir; hastaneye '
                                            'yatış endikasyonu yoktur.'},
                         {'text': 'Antibiyotik vermeyip sadece günde dört kez mesane içine formaldehit solüsyonu '
                                  'yıkaması yapmak',
                          'is_correct': False,
                          'scenario_update': 'Mesane içi toksik kimyasal yıkama masif kimyasal sistit ve nekroza neden '
                                             'oldu.',
                          'teaching_point': 'Mesane içi kimyasal lavaj kesinlikle kontrendikedir; bakteriyel sistit '
                                            'oral antibiyotikle çözülür.'},
                         {'text': 'İdrar çıkışını tamamen durdurmak için hastaya sıvı kısıtlaması uygulayıp mesanesini '
                                  'bağlamak',
                          'is_correct': False,
                          'scenario_update': 'Sıvı kısıtlaması idrarı konsantre ederek yanmayı şiddetlendirdi ve '
                                             'bakteriyel kolonizasyonu artırdı.',
                          'teaching_point': 'İYE tedavisinde bol sıvı tüketimi ve sık idrara çıkma mesanenin yıkanması '
                                            'için esastır.'}]}]},
 {'id': 'G64',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '11 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Temmuz sıcağında açık sahada futbol oynadıktan sonra başlayan yoğun baş dönmesi, halsizlik ve bulantı',
  'history': "On bir yaşındaki erkek çocuk yaz tatilinde saat 14:00'te güneşin altında 2 saat arkadaşlarıyla futbol "
             "oynadıktan sonra Yeşil Alana getiriliyor: 'Maçın sonuna doğru başı döndü, dizlerinin bağı çözüldü ve "
             'yere oturdu. Aşırı derecede terliyor, bütün tişörtü sırılsıklam. Midesi çok bulanıyor, su içince bir kez '
             "kustu. Bilinci tamamen açık, bizi tanıyor, sorulara doğru cevap veriyor. Nöbet geçirmemiş, bayılmamış.'",
  'final_diagnosis': 'Sıcak Bitkinliği (Heat Exhaustion / Dehidratasyon ve Elektrolit Kaybı ile Giden Termoregülasyon '
                     'Tablosu)',
  'disposition': 'Yeşil Alanda Serin Ortamda Dinlendirme, Aktif Soğutma, Oral/İV Elektrolit Sıvısı ve Taburculuk',
  'case_pearl': 'Sıcak ilişkili hastalıklar bir spektrumdur: Sıcak Krampları -> Sıcak Bitkinliği (Heat Exhaustion) -> '
                'Sıcak Çarpması (Heat Stroke). Sıcak bitkinliğinde vücut ısısı hafif-orta derecede yüksektir (<40°C, '
                'genellikle 38-39°C), TERLEME DEVAM EDER ve EN ÖNEMLİSİ SANTRAL SİNİR SİSTEMİ FONKSİYONLARI '
                'KORUNMUŞTUR (Bilinç açıktır, konfüzyon, ataksi, koma veya nöbet YOKTUR). Eğer vücut ısısı >40°C ise, '
                'anhidroz (terlemenin durması) ve mental durum değişikliği (deliryum, nöbet, koma) varsa tablo SICAK '
                'ÇARPMASIDIR (Heat Stroke - Kırmızı Alan Acili!). Sıcak bitkinliğinde hasta serin/klimalı alana '
                'alınır, giysileri gevşetilir, fan/ıslak kompresle soğutulur, tuz ve glukoz içeren soğuk sıvılarla '
                'hidrate edilir; prognozu mükemmeldir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Sıcakta egzersiz sonrası baş dönmesi ve halsizliği olan bu çocukta ilk muayene hedefiniz ne '
                         'olmalıdır?',
             'options': [{'text': 'Bilinç durumunu, vücut sıcaklığını, periferik nabızları ve terleme varlığını hızla '
                                  'değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Ciddi hipertermi ile ılımlı termal stres ayrımı için bilinç durumu ve '
                                         'çekirdek vücut sıcaklığı değerlendirilir. Ilımlı tabloda mental durum '
                                         'normaldir.',
                          'new_finding': 'Vital Bulgular: Vücut Sıcaklığı (Aksiller) 38.2°C, KTA 108/dk, SS 22/dk, '
                                         'SpO2 %99, TA 100/65 mmHg. Çocuk yorgun görünüyor ancak bilinci tamamen açık, '
                                         'koopere ve oryante. Cildi sıcak ve belirgin şekilde nemli/terli. '
                                         'Gözbebekleri izokorik ve ışığa duyarlı. Ense sertliği yok, nörolojik defisit '
                                         'yok. Mukozalar hafif kuru, cilt turgoru 2 saniyede geri dönüyor.'},
                         {'text': 'Hastada akut meningoensefalit düşünerek derhal acil genel anestezi ve solunum '
                                  'desteği vermek',
                          'is_correct': False,
                          'scenario_update': 'Güneş maruziyeti öyküsü net olan berrak bilinçli hastada gereksiz '
                                             'entübasyon laringospazm yarattı.',
                          'teaching_point': 'Bilinç açık ve ense sertliği yokken sıcak maruziyeti öyküsü olan çocukta '
                                            'öncelikle termoregülasyon düşünülür.'},
                         {'text': 'Hastaya kardiyojenik şok tanısı koyup acil yüksek doz adrenalin infüzyonu başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Dehidrate hastaya gereksiz adrenalin verilmesi taşikardiyi tetikleyerek '
                                             'aritmi riskini artırdı.',
                          'teaching_point': 'Taşikardi egzersiz ve sıvı kaybına sekonder kompanzatuvardır; inotrop '
                                            'endikasyonu yoktur.'},
                         {'text': 'Hastanın terlemesini durdurmak amacıyla onu kalın yün battaniyelerle sıkıca '
                                  'sarmalamak',
                          'is_correct': False,
                          'scenario_update': "Sıcak ortamda battaniyeye sarılması vücut ısısını 40.5°C'ye fırlatarak "
                                             'sıcak çarpmasını tetikledi.',
                          'teaching_point': 'Hipertermik hasta kesinlikle sarılmaz; aksine giysileri çıkarılıp '
                                            'soğutulmalıdır.'}]},
            {'stage_title': 'Laboratuvar ve İleri İncelemeler',
             'question': 'Aşırı sıcak maruziyeti olan bu hastada hidrasyon ve organ fonksiyonlarını değerlendirmek '
                         'için ne yapılmalıdır?',
             'options': [{'text': 'Serum elektrolitleri, böbrek fonksiyon testleri ve kan şekeri düzeyini yatak '
                                  'başında değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Terlemeyle sodyum ve su kaybı geliştiğinden hiponatremi/hipernatremi, '
                                         'dehidratasyona bağlı üre/kreatinin artışı ve egzersize bağlı hipoglisemi '
                                         'hızla taranır.',
                          'new_finding': 'Laboratuvar: Glukoz 88 mg/dL, Sodyum 137 mEq/L, Potasyum 4.1 mEq/L, Klor 102 '
                                         'mEq/L, BUN 16 mg/dL, Kreatinin 0.6 mg/dL (Normal). İdrar Tahlili: Dansite '
                                         '1028 (Konsantre), protein ve keton negatif. Hastada rabdomiyoliz bulgusu '
                                         'saptanmadı (idrarda miyoglobin yok).'},
                         {'text': 'Hastaya intrakraniyal kanama şüphesiyle acil dört fazlı kontrastlı tüm kafa '
                                  'anjiyo-tomografisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Bilinç açık ve travma öyküsü yokken yapılan çekim hastayı boş yere '
                                             'yüksek radyasyona maruz bıraktı.',
                          'teaching_point': 'Nörolojik defisiti ve travması olmayan termal yorgunlukta acil beyin '
                                            'görüntülemesi gerekmez.'},
                         {'text': 'Kanda tüm genetik kas distrofisi mutasyon panellerini ve kas biyopsisini acil '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'Aşırı sıcak yorgunluğunda istenen genetik paneller aileyi gereksiz maddi '
                                             've manevi kaygıya soktu.',
                          'teaching_point': 'Akut çevresel hipertermi tablosunda genetik kas hastalıkları düşünülmez.'},
                         {'text': 'Laboratuvar tetkiklerini reddedip hastayı hemen sıcak buhar banyosuna sokarak '
                                  'terletmek',
                          'is_correct': False,
                          'scenario_update': 'Buhar banyosu hastayı ağır dehidratasyon ve hipertermi ile '
                                             'kardiyovasküler kollapsa soktu.',
                          'teaching_point': 'Sıcak kaynaklı rahatsızlıklarda buhar banyosu ölümcül bir hatadır; '
                                            'soğutma esastır.'}]},
            {'stage_title': 'Klinik Ön Tanı ve Ayırıcı Tanı',
             'question': 'Sıcakta egzersiz sonrası terlemesi olan, bilinci açık, vücut ısısı 38.2°C saptanan hastada '
                         'tanınız nedir?',
             'options': [{'text': 'Akut sıcak bitkinliği tablosu',
                          'is_correct': True,
                          'explanation': 'Sıcakta ağır egzersiz öyküsü, terlemenin sürmesi, ısının <40°C olması ve en '
                                         'önemlisi santral sinir sistemi disfonksiyonunun olmaması sıcak bitkinliğini '
                                         'doğrular.',
                          'new_finding': 'Kesin Tanı: Sıcak Bitkinliği (Heat Exhaustion) doğrulanmıştır. Soğutma ve '
                                         'hidrasyona geçildi.'},
                         {'text': 'Fulminan sıcak çarpması acili',
                          'is_correct': False,
                          'scenario_update': 'Sıcak çarpmasında (Heat stroke) vücut ısısı >40°C olur, terleme durur ve '
                                             'derin koma/deliryum gelişir.',
                          'teaching_point': 'Bilinç normalse ve terleme devam ediyorsa tablo sıcak çarpması değil, '
                                            'sıcak bitkinliğidir.'},
                         {'text': 'Akut septik şok tablosu',
                          'is_correct': False,
                          'scenario_update': 'Septik şokta hipotansiyon, bozulmuş kapiller dolum, periferik '
                                             'vazodilatasyon ve enfeksiyon odağı olur.',
                          'teaching_point': 'Enfeksiyon odağı olmadan sıcakta egzersiz öyküsüyle gelen tabloda öncelik '
                                            'septik şok değildir.'},
                         {'text': 'Diyabetik ketoasidoz koması',
                          'is_correct': False,
                          'scenario_update': "DKA'da kan şekeri çok yüksektir, Kussmaul solunumu ve ketonüri vardır; "
                                             'hastanın şekeri normaldir.',
                          'teaching_point': 'Normoglisemik ve ketonu olmayan hastada DKA dışlanır.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Sıcak bitkinliği tanısı alan bu hastada Yeşil Alanda uygulanacak en uygun tedavi ve '
                         'hidrasyon yöntemi nedir?',
             'options': [{'text': 'Serin klimalı odaya almak, giysilerini gevşetmek, fanla soğutmak ve soğuk oral '
                                  'sıvılar içirmek',
                          'is_correct': True,
                          'explanation': 'İlk adım hastayı sıcak ortamdan çıkarıp serin/klimalı alana almaktır. Fazla '
                                         'giysiler çıkarılır, buharlaşmayla soğutma (fan + ılık/soğuk su püskürtme) '
                                         'uygulanır. Kusması azaldığında oral elektrolit içeren sıvılar (ORS/soğuk su) '
                                         'verilir.',
                          'new_finding': 'Klimalı dinlenme odasına alındı, forması çıkarıldı, vantilatör ve ıslak '
                                         'kompresle soğutuldu. Azar azar soğuk elektrolitli sıvı içirildi. 1 saat '
                                         "içinde vücut ısısı 37.0°C'ye düştü, nabzı 78/dk'ya geriledi, baş dönmesi "
                                         'tamamen geçti.'},
                         {'text': 'Hastayı hemen dondurucu buz banyosuna atıp vücut ısısını otuz iki dereceye düşürmek',
                          'is_correct': False,
                          'scenario_update': 'Aşırı agresif buz banyosu periferik vazokonstriksiyon yaparak titremeye '
                                             've aritmiye yol açtı.',
                          'teaching_point': 'Sıcak bitkinliğinde aşırı agresif buz banyosu hipotermi ve shivering '
                                            '(titreme) yapar; ılımlı soğutma yeterlidir.'},
                         {'text': 'Vücut ısısını düşürmek amacıyla yüksek doz intravenöz antibiyotik ve antipiretik '
                                  'infüzyonu yapmak',
                          'is_correct': False,
                          'scenario_update': 'Parasetamol çevresel hipertermide hipotalamik ayar noktasını '
                                             'değiştirmez; karaciğere gereksiz yük bindi.',
                          'teaching_point': 'Sıcak bitkinliğinde ateş pirojen kaynaklı değildir; bu nedenle '
                                            'parasetamol ve ibuprofen etkisizdir.'},
                         {'text': 'Sıvı vermeden hastayı hemen güneşin altına geri gönderip futbol maçına devam '
                                  'ettirmek',
                          'is_correct': False,
                          'scenario_update': "Güneşe dönen çocukta terleme durdu, ısısı 40.8°C'ye fırlayarak koma ve "
                                             'sıcak çarpmasına girdi.',
                          'teaching_point': 'Sıcak bitkinliği tedavi edilmezse ölümcül sıcak çarpmasına ilerler; '
                                            'istirahat şarttır.'}]}]},
 {'id': 'G65',
  'category': '👁️ Göz Şikayetleri',
  'age': '5 Yaşında',
  'gender': 'Kız',
  'complaint': 'Sağ göz kapağında iki gündür giderek artan kızarıklık, şişlik ve dokunmakla hassasiyet',
  'history': "Beş yaşındaki kız çocuk annesi tarafından Yeşil Alana getiriliyor: 'Üç gün önce sağ kaşının kenarını bir "
             'sinek ısırmıştı, çocuk da orayı tırnaklarıyla çok kaşıdı. Dünden beri sağ üst ve alt göz kapağı kızardı, '
             'şişti ve hafif kapandı. Gözünün beyazında kızarıklık yok, sarı akıntısı gelmiyor. Görmesinde bir bozulma '
             'olmadığını, çizgi filmi net gördüğünü söylüyor. Ateşi hafif 37.4°C oldu. Gözünü oynatırken canının '
             "acımadığını söylüyor.'",
  'final_diagnosis': 'Preseptal (Periorbital) Selülit (Cilt Bütünlüğü Bozulmasına Sekonder Preseptal Yumuşak Doku '
                     'Enfeksiyonu)',
  'disposition': 'Yeşil Alandan Oral Geniş Spektrumlu Antibiyoterapi, Yakın 24-48 Saatlik Poliklinik Kontrolü ile '
                 'Taburculuk',
  'case_pearl': 'Göz kapağı şişliklerinde en hayati pediatrik klinik karar: PRESEPTAL SELÜLİT vs. ORBİTAL (POSTSEPTAL) '
                'SELÜLİTTİR! Orbital septum göz kapağını derin orbita yapılarından ayıran anatomik bariyerdir. '
                'Preseptal selülitte enfeksiyon septumun ÖNÜNDEDİR (cilt kaynaklıdır; böcek ısırığı, çizik, arpacık '
                'sonrası). ORBİTAL SELÜLİTTE İSE (genellikle sinüzit komplikasyonu) 4 KRİTİK BULGU VARDIR: 1) '
                'Proptozis (gözün öne fırlaması), 2) Ağrılı oftalmopleji (göz hareketlerinde kısıtlılık ve şiddetli '
                'ağrı), 3) Görme keskinliğinde azalma, 4) Rölatif afferent pupil defekti (RAPD). Bu 4 bulgunun hiçbiri '
                'yoksa hasta preseptal selülittir; bilinci açık, beslenen çocuk oral antibiyotikle '
                '(Amoksisilin-klavulanat) ayaktan tedavi edilebilir ve 24-48 saat sonra göz kontrolüne çağrılır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Tek taraflı göz kapağı şişliği ve kızarıklığı olan bu çocukta fizik muayenede öncelikle '
                         'nelere bakmalısınız?',
             'options': [{'text': 'Göz küresi hareketlerini, proptozis varlığını, görme keskinliğini ve pupilla ışık '
                                  'refleksini değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Derin orbital enfeksiyonu ekarte etmek için ekstraoküler kas hareketleri '
                                         '(ağrı ve kısıtlılık), proptozis, görme keskinliği ve pupilla ışık refleksi '
                                         'muayene edilir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.3°C, KTA 92/dk, SS 20/dk, SpO2 %99, TA 96/60 mmHg. '
                                         'Sağ üst ve alt göz kapağında eritem, ödem ve dokunmakla hafif hassasiyet '
                                         'mevcut. Kaş kenarında küçük ekskoryasyon (kaşıma izi) izlendi. Göz küresi '
                                         'muayenesinde: Ekstraoküler hareketler her yöne TAM ve tamamen AĞRISIZ. '
                                         'Proptozis yok. Görme keskinliği her iki gözde tam (objeleri ve parmakları '
                                         'net sayıyor). Direkt ve indirekt pupilla ışık refleksleri doğal, RAPD yok. '
                                         'Konjonktivada kemozis yok.'},
                         {'text': 'Hastada akut glokom krizi düşünerek acil olarak göz küresine körleme cerrahi '
                                  'ponksiyon yapmak',
                          'is_correct': False,
                          'scenario_update': 'Göz kapağı cilt enfeksiyonunda göz küresine iğne sokulması glob rüptürü '
                                             've kalıcı körlük yarattı.',
                          'teaching_point': 'Kapak selülitinde göz içi basınç krizi düşünülmez; invaziv intraoküler '
                                            'girişim kontrendikedir.'},
                         {'text': 'Kızarıklığı basit uyku şişliği sayıp çocuğu hiçbir göz muayenesi yapmadan eve '
                                  'göndermek',
                          'is_correct': False,
                          'scenario_update': 'Muayenesiz bırakılan yüzeyel kapak enfeksiyonu ilerleyerek derin orbita '
                                             'apsesine dönüştü.',
                          'teaching_point': 'Eritematöz kapak şişlikleri mutlaka tam oftalmolojik değerlendirme '
                                            'gerektirir.'},
                         {'text': 'Görme kaybı şüphesiyle hastanın her iki gözünü cerrahi olarak enüklee etmeye karar '
                                  'vermek',
                          'is_correct': False,
                          'scenario_update': 'Yüzeyel kapak enfeksiyonunda organ kaybına yol açan kabul edilemez bir '
                                             'tıbbi hata oluştu.',
                          'teaching_point': 'Kapak selüliti selim bir cilt enfeksiyonudur; basit antibiyoterapi ile '
                                            'tamamen iyileşir.'}]},
            {'stage_title': 'Laboratuvar ve İleri İncelemeler',
             'question': 'Göz hareketleri tam ve ağrısız, proptozisi olmayan bu hastada tanısal görüntüleme yaklaşımı '
                         'nasıl olmalıdır?',
             'options': [{'text': 'Klinik muayene yüzeyel kapak tutulumunu gösterdiğinden radyasyon içeren acil orbita '
                                  'tomografisinden kaçınmak',
                          'is_correct': True,
                          'explanation': 'Pediatrik kılavuzlara göre proptozisi, oftalmoplejisi, görme kaybı ve '
                                         'toksisitesi olmayan tipik yüzeyel kapak selüliti olgularında acil '
                                         'orbita/paranazal BT gerekmez; çocuk radyasyondan korunur.',
                          'new_finding': 'Klinik tablo septum önü kapak enfeksiyonu ile tam uyumludur. Orbital tutulum '
                                         'bulgusu (proptozis, oftalmopleji, görme kusuru, kemozis) kesinlikle '
                                         'saptanmadı. WBC 8.400/mm³, CRP 5.2 mg/L (hafif yüksek). Gereksiz iyonizan '
                                         'orbita BT çekilmedi; klinik izlem kararı alındı.'},
                         {'text': 'Tüm kafa, boyun ve toraksı içine alan yüksek doz anjiyo-bilgisayarlı tomografi '
                                  'serisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Hafif kapak enfeksiyonunda aşırı radyasyon katarakt ve malignite riskini '
                                             'gereksiz yere artırdı.',
                          'teaching_point': 'Derin orbita tutulum bulgusu olmayan yüzeyel vakalarda rutin BT '
                                            'çekilmez.'},
                         {'text': 'Enfeksiyon etkenini bulmak için göz kapağı derisinden derin tam kat eksizyonel '
                                  'cerrahi biyopsi almak',
                          'is_correct': False,
                          'scenario_update': 'Göz kapağından gereksiz derin biyopsi kapak çekintisine ve lagoftalmiye '
                                             'neden oldu.',
                          'teaching_point': 'Selülitte doku biyopsisi yapılmaz; enfeksiyon yayılır ve kozmetik defekt '
                                            'kalır.'},
                         {'text': 'Kandaki enfeksiyonu temizlemek amacıyla hastaya acil tam kan değişimi prosedürü '
                                  'uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Lokalize cilt enfeksiyonunda kan değişimi masif transfüzyon reaksiyonu '
                                             'doğurdu.',
                          'teaching_point': 'Kapak selüliti lokal bir enfeksiyondur; kan değişimi gibi agresif '
                                            'işlemlerin yeri yoktur.'}]},
            {'stage_title': 'Klinik Ön Tanı ve Ayırıcı Tanı',
             'question': 'Göz hareketleri tam, görmesi doğal, proptozisi olmayan kapak eritemli bu çocukta tanınız '
                         'nedir?',
             'options': [{'text': 'Akut preseptal periorbital selülit',
                          'is_correct': True,
                          'explanation': 'Böcek ısırığı sonrası gelişen, septum önünde sınırlı, göz hareketlerini ve '
                                         'görmeyi etkilemeyen eritematöz kapak tablosu preseptal selülittir.',
                          'new_finding': 'Kesin Tanı: Preseptal (Periorbital) Selülit doğrulanmıştır. Oral '
                                         'antibiyoterapi planlandı.'},
                         {'text': 'Akut retroorbital abse tablosu',
                          'is_correct': False,
                          'scenario_update': 'Orbita absesinde belirgin proptozis, göz hareketlerinde şiddetli ağrılı '
                                             'kısıtlılık ve görme kaybı olur.',
                          'teaching_point': 'Normal göz hareketleri ve proptozis yokluğu retroorbital abseyi kesin '
                                            'olarak dışlar.'},
                         {'text': 'Konjenital nazolakrimal kanal tıkanıklığı',
                          'is_correct': False,
                          'scenario_update': 'Nazolakrimal tıkanıklık doğumdan beri olan çapaklanmadır; akut eritemli '
                                             'kapak selüliti yapmaz.',
                          'teaching_point': 'Akut kızarıklık ve ödem nazolakrimal tıkanıklıkla açıklanamaz; aktif '
                                            'enfeksiyon vardır.'},
                         {'text': 'Akut herpetik keratit ülseri',
                          'is_correct': False,
                          'scenario_update': 'Keratitte korneada dendritik ülser ve şiddetli fotofobi olur; izole '
                                             'kapak selüliti görülmez.',
                          'teaching_point': 'Korneal tutulum ve flöresein boyanması olmadan keratit düşünülmez.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Genel durumu iyi, oral alabilen preseptal selülitli bu hastanın en uygun tedavisi ve '
                         'taburculuk planı nedir?',
             'options': [{'text': 'Oral amoksisilin-klavulanat başlamak, alarm bulgularını anlatıp kırk sekiz saat '
                                  'sonra kontrole çağırmak',
                          'is_correct': True,
                          'explanation': 'Etkenler çoğunlukla S. aureus ve S. pyogenes olduğundan oral '
                                         'Amoksisilin-klavulanat (50-80 mg/kg/gün) ilk seçenektir. Aileye göz '
                                         'hareketlerinde ağrı, görmede bozulma veya ateş çıkarsa derhal acile gelmesi '
                                         'söylenir; 24-48 saat sonra kontrol şarttır.',
                          'new_finding': 'Oral amoksisilin-klavulanat başlandı, sıcak pansuman önerildi. Kırmızı '
                                         'bayraklar anlatıldı. 48 saat sonraki kontrolde göz kapağındaki şişlik ve '
                                         'kızarıklığın tamamen solduğu, gözün rahatça açıldığı görüldü.'},
                         {'text': 'Hastalık tehlikeli olduğu için çocuğu derhal yoğun bakıma yatırıp genel anesteziyle '
                                  'uyutmak',
                          'is_correct': False,
                          'scenario_update': 'Stabil ve oral alabilen hastada gereksiz yoğun bakım yatışı nozokomiyal '
                                             'pnömoni yarattı.',
                          'teaching_point': 'Hafif preseptal selülit ayaktan oral tedaviyle güvenle iyileşir; yoğun '
                                            'bakım endikasyonu yoktur.'},
                         {'text': 'Antibiyotik vermeden göz kapağını bıçakla boydan boya keserek açık drenaj pansumanı '
                                  'yapmak',
                          'is_correct': False,
                          'scenario_update': 'Fluktuasyon vermeyen selülite bistüri atılması göz kapağında kalıcı '
                                             'estetik skar ve pitozis yaptı.',
                          'teaching_point': 'Toplanmış abse olmadan selülit kesilmez; tedavi medikal antibiyotiktir.'},
                         {'text': 'Hiçbir tedavi vermeyip göz kapağına günde beş kez çiğ sarımsak lapası bağlatmak',
                          'is_correct': False,
                          'scenario_update': 'Sarımsak kimyasal yanık ve toksik keratit yaparak kornea epiteline ağır '
                                             'zarar verdi.',
                          'teaching_point': 'Göz çevresine tahriş edici bitkisel maddeler uygulanması kornea hasarına '
                                            'yol açar.'}]}]},
 {'id': 'G66',
  'category': '👶 Ağlayan, Emmeyen, Huzursuz Bebek',
  'age': '2 Aylık',
  'gender': 'Erkek',
  'complaint': 'Her kaka yapmadan önce on beş dakika boyunca yüzü kıpkırmızı kesilerek ağlama ve bacaklarını karnına '
               'çekme',
  'history': "İki aylık sadece anne sütü alan erkek bebek ebeveynleri tarafından panikle getiriliyor: 'Bebeğimiz son "
             'iki haftadır kaka yapmadan önce adeta canı çıkarcasına 15-20 dakika ağlıyor, ıkınıyor, yüzü morarıyor. '
             'Sonunda kaka yaptığında ise çıkan kaka taş gibi değil, tamamen yumuşacık, hardal sarısı cıvık kıvamda. '
             'Kaka yaptıktan sonra hemen sakinleşip gülümsüyor. Kabız oldu diye makatına zeytinyağlı kulak çubuğu '
             'soktuk ve gliserin fitil verdik ama her kaka öncesi aynı dram yaşanıyor. Kilo alımı ayda 900 gram, '
             "kusması veya ateşi yok.'",
  'final_diagnosis': 'İnfant Diskezi (Fonksiyonel İnfant Dışkılama Koordinasyon Bozukluğu / Roma IV Kriterleri)',
  'disposition': 'Yeşil Alandan Aileye Fizyolojik Sürecin Anlatılması, Rektal Manipülasyondan Kaçınma Eğitimi ile '
                 'Taburculuk',
  'case_pearl': 'İnfant diskezi (Roma IV kriterleri), <9 aylık sağlıklı süt çocuklarında görülen tamamen BENİGN ve '
                'geçici bir gelişimsel tablodur. Bebek dışkılama sırasında karın içi basıncını artırmayı (ıkınmayı) '
                'öğrenmiştir ancak PELVİK TABAN KASLARINI (puborektalis ve anal sfinkter) gevşetmeyi henüz koordine '
                'edememektedir. Kapalı bir kapıya doğru ıkındığı için 10-20 dakika ağlar, sonunda yorulup sfinkter '
                'gevşeyince tamamen YUMUŞAK/SULU normal dışkı çıkarır ve anında rahatlar. Bu kesinlikle KABIZLIK '
                'DEĞİLDİR! En kritik klinik kural: Makata derece, kulak çubuğu sokulması, gliserin kansuk fitil veya '
                'lavman YAPILMAMALIDIR! Rektal stimülasyon bebeğin kendi sfinkterini gevşetmeyi öğrenmesini geciktirir '
                've bağımlılık yaratır. Tedavi sadece ailenin eğitilmesi ve rahatlatılmasıdır; birkaç hafta içinde '
                'kendiliğinden düzelir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Dışkılama öncesi şiddetli ıkınma ve ağlaması olan bu süt çocuğunda fizik muayenede öncelikle '
                         'nelere bakmalısınız?',
             'options': [{'text': 'Karın rahatlığını, organomegali yokluğunu, perineal bölgeyi, anüs açıklığını ve '
                                  'anal refleksi değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Organik patolojileri (anal fissür, anal stenoz, Hirschsprung, spinal '
                                         'disrafizm) dışlamak için batın, perineal bölge, anüs anatomisi ve anal '
                                         'refleks değerlendirilir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 128/dk, SS 34/dk, SpO2 %100, Kilo 5.400 g '
                                         '(Persentilinde büyüme mükemmel). Bebek muayenede gayet sakin ve neşeli. '
                                         'Batın yumuşak, distansiyon yok, kitle veya organomegali palpe edilmedi. '
                                         'Perianal bölge muayenesinde anüs normal lokalizasyonda, anal fissür veya '
                                         'hemoroid yok. Anal refleks canlı, lumbosakral omurga doğal, gamze veya kıl '
                                         'tutamı yok.'},
                         {'text': 'Hastada akut cerrahi peritonit düşünerek derhal acil genel anestezi ve laparotomi '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'Batını yumuşak ve neşeli süt çocuğunda gereksiz invaziv cerrahi '
                                             'laparotomi komplikasyon doğurdu.',
                          'teaching_point': 'Peritonitte tahta karın ve toksisite olur; yumuşak dışkı çıkaran neşeli '
                                            'bebekte peritonit düşünülmez.'},
                         {'text': 'Ağlamayı kafa içi kanama sayıp hiçbir muayene yapmadan acil kafa deliği cerrahisi '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'Klinik değerlendirme yapılmadan istenen invaziv nöroşirürji girişimi '
                                             'büyük bir tıbbi hatadır.',
                          'teaching_point': 'Yalnızca dışkılama öncesi ağlayan ve motor gelişimi normal bebekte '
                                            'intrakraniyal acil aranmaz.'},
                         {'text': 'Bebeği muayene etmeden annenin sütünün zehirli olduğunu iddia edip emzirmeyi hemen '
                                  'yasaklamak',
                          'is_correct': False,
                          'scenario_update': 'Anne sütünün haksız kesilmesi bebekte beslenme yetersizliği ve anne sütü '
                                             'travması yarattı.',
                          'teaching_point': 'Dışkılama koordinasyon sorunu anne sütüyle ilgili değildir; anne sütü '
                                            'kesilmemeli ve desteklenmelidir.'}]},
            {'stage_title': 'Laboratuvar ve İleri İncelemeler',
             'question': 'Büyümesi normal, muayenesi tamamen doğal ve çıkan dışkısı yumuşak olan bu bebekte tetkik '
                         'yaklaşımı ne olmalıdır?',
             'options': [{'text': 'Klinik kriterler selim koordinasyon güçlüğünü net doğruladığından radyasyonlu ve '
                                  'invaziv tetkiklerden kesinlikle kaçınmak',
                          'is_correct': True,
                          'explanation': 'Roma IV kriterlerine göre 9 aydan küçük, büyümesi normal, nörolojik ve '
                                         'perineal muayenesi doğal olan ve yumuşak dışkı çıkaran bebeklerde tanı '
                                         'kliniktir; radyoloji veya biyopsi gerekmez.',
                          'new_finding': 'Hastada kırmızı bayrak bulgusu (safralı kusma, karın distansiyonu, mekonyum '
                                         'çıkışında gecikme, anal darlık) saptanmadı. Dışkı kıvamının yumuşak olması '
                                         'gerçek organik kabızlığı (fonksiyonel konstipasyon veya Hirschsprung) kesin '
                                         'olarak ekarte etti. Bebek gereksiz kontrastlı kolon grafisi veya manometri '
                                         'travmasından korundu.'},
                         {'text': 'Hirschsprung şüphesiyle acil genel anestezi altında tüm rektumdan tam kat cerrahi '
                                  'biyopsi almak',
                          'is_correct': False,
                          'scenario_update': 'Normal yumuşak dışkı çıkaran 2 aylık bebekte rektal cerrahi biyopsi '
                                             'masif rektal kanamaya yol açtı.',
                          'teaching_point': 'Dışkısı yumuşak olan ve distansiyonu olmayan bebekte rektum biyopsisi '
                                            'endike değildir.'},
                         {'text': 'Kaka yapamadığı için acil tüm batın ve pelvik anjiyo-bilgisayarlı tomografi serisi '
                                  'çekmek',
                          'is_correct': False,
                          'scenario_update': 'Sağlıklı bebeğe boş yere yüksek doz iyonize radyasyon verildi ve '
                                             'kontrast madde alerjisi gelişti.',
                          'teaching_point': 'Koordinasyon güçlüğü gelişimsel bir durumdur; tomografide görülebilecek '
                                            'anatomik bir lezyon yoktur.'},
                         {'text': 'Dışkılamadaki ağlamanın nedenini bulmak amacıyla kanda tüm viral ve bakteriyel '
                                  'kültürleri göndermek',
                          'is_correct': False,
                          'scenario_update': 'Ateşi olmayan sağlıklı bebekten defalarca kan alınması hematom ve derin '
                                             'anksiyete doğurdu.',
                          'teaching_point': 'Ateşsiz ve enfeksiyon bulgusu olmayan selim dışkılama zorluğunda '
                                            'mikrobiyolojik kültürler gerekmez.'}]},
            {'stage_title': 'Klinik Ön Tanı ve Ayırıcı Tanı',
             'question': 'Dışkılama öncesi ıkınan ancak sonunda tamamen yumuşak dışkı çıkaran sağlıklı bebekte tanınız '
                         'nedir?',
             'options': [{'text': 'Benign infant diskezi tablosu',
                          'is_correct': True,
                          'explanation': 'Dışkılama öncesi en az 10 dakika ıkınma/ağlama ve ardından tamamen yumuşak '
                                         'normal kıvamda dışkı çıkarma Roma IV infant diskezi kriteridir.',
                          'new_finding': 'Kesin Tanı: İnfant Diskezi doğrulanmıştır. Aileye sürecin fizyolojik olduğu '
                                         'anlatıldı.'},
                         {'text': 'Fekal impaksiyonlu fonksiyonel kabızlık',
                          'is_correct': False,
                          'scenario_update': 'Gerçek kabızlıkta dışkı sert, keçi pisliği gibi veya çapı geniştir; '
                                             'diskezide ise dışkı tamamen yumuşaktır.',
                          'teaching_point': 'Dışkının yumuşak olması kabızlık tanısını kesin olarak dışlar.'},
                         {'text': 'Hirschsprung aganglionik megakolon hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Hirschsprung hastalığında ilk 48 saatte mekonyum çıkmaz, masif karın '
                                             'distansiyonu ve safralı kusma olur.',
                          'teaching_point': 'Mekonyumu zamanında çıkan ve kilo alımı mükemmel olan bebekte '
                                            'Hirschsprung beklenmez.'},
                         {'text': 'Akut inkarserasyonlu inguinal herni',
                          'is_correct': False,
                          'scenario_update': 'Boğulmuş fıtıkta kasıkta ağrılı, sert ve mor kitle olur; dışkılama ile '
                                             'ilişkisiz sürekli ağlar.',
                          'teaching_point': 'İnguinal herni palpasyonla kasıkta kitle olarak saptanır; diskezi ile '
                                            'ilgisi yoktur.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'İnfant diskezi saptanan bu bebeğin ailesine verilecek en kritik kanıta dayalı tıbbi öneri '
                         'hangisidir?',
             'options': [{'text': 'Rektal uyarı ve fitilden kesinlikle kaçınmak, sürecin selim ve geçici olduğunu '
                                  'aileye anlatmak',
                          'is_correct': True,
                          'explanation': "En önemli kural 'bekle ve gör' yaklaşımıdır. Rektal manipülasyon (derece, "
                                         'pamuklu çubuk, fitil) bebeğin kendi pelvik tabanını gevşetmeyi öğrenmesini '
                                         'engeller. Aileye sürecin geçici olduğu, dışkının yumuşak olduğu ve birkaç '
                                         'haftada bebeğin koordinasyonu kazanacağı anlatılarak güvence verilir.',
                          'new_finding': 'Aileye sfinkter dissinerjisi açıklandı, fitil ve rektal çubuk uygulamaları '
                                         'derhal durduruldu. 3 hafta sonra kontrolde bebeğin artık ağlamadan rahatça '
                                         'yumuşak kakasını yaptığı ve tablonun tamamen düzeldiği görüldü.'},
                         {'text': 'Kakasını daha kolay yapması için günde üç kez makatına gliserinli fitil ve lavman '
                                  'uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Sürekli fitil kullanımı rektal mukozayı tahriş etti ve sfinkterin kendi '
                                             'kendine gevşeme refleksini köreltti.',
                          'teaching_point': 'İnfant diskezisinde rektal stimülasyon refleks gelişimini bozar ve '
                                            'bağımlılık yapar; kesinlikle yapılmamalıdır.'},
                         {'text': 'Bebeğe bağırsaklarını tamamen boşaltmak amacıyla yüksek doz senozid içeren sert '
                                  'laksatif şurup başlamak',
                          'is_correct': False,
                          'scenario_update': 'İki aylık bebeğe verilen kimyasal laksatif masif sulu ishal ve ağır '
                                             'elektrolit kaybına neden oldu.',
                          'teaching_point': 'Diskezide dışkı zaten yumuşaktır; kimyasal laksatifler ciddi '
                                            'dehidratasyon ve kramp yapar.'},
                         {'text': 'Dışkılama kaslarını gevşetmek için bebeğe acil cerrahi sfinkterotomi operasyonu '
                                  'uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz cerrahi sfinkterotomi bebekte ömür boyu kalıcı gaita '
                                             'inkontinansına yol açtı.',
                          'teaching_point': 'İnfant diskezi cerrahi bir patoloji değildir; kendiliğinden olgunlaşan '
                                            'fizyolojik bir süreçtir.'}]}]},
 {'id': 'G67',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '18 Aylık',
  'gender': 'Kız',
  'complaint': 'Annesinin altını temizlerken idrar deliği ve vajina girişinin tamamen kapalı olduğunu fark etmesi',
  'history': "On sekiz aylık kız bebek annesi tarafından endişe içinde Yeşil Alana getiriliyor: 'Dün akşam alt bezini "
             'değiştirirken fark ettim, vajina girişi sanki hiç yokmuş gibi tamamen birbirine yapışmış, deriyle '
             'örtülmüş. İdrarını yaparken zorlanıyor ve idrarı öne doğru ince bir çizgi halinde fışkırıyor. Ateşi yok, '
             'bez bölgesinde geçmişte sık sık pişik oluyordu. Doğduğunda her şeyi normaldi, sonradan mı kapandı, '
             "ameliyat mı gerekecek çok korktuk.'",
  'final_diagnosis': 'Labial Füzyon / Labial Sinekşi (Düşük Östrojen ve Kronik İnflamasyona Sekonder Benign '
                     'Yapışıklık)',
  'disposition': 'Yeşil Alandan Travmatik Ayırmadan Kaçınma, Topikal Östrojenli Krem Eğitimi ile Taburculuk',
  'case_pearl': 'Labial füzyon (sinekşi), 3 ay ile 6 yaş arasındaki kız çocuklarında sık görülen, labia minoraların '
                'orta hatta birbirine ince, avasküler, yarı saydam bir zarla yapışması durumudur. Etiyolojide bebeklik '
                'dönemindeki fizyolojik hipoöstrojenizm ve bez dermatiti/ıslak mendil tahrişine bağlı kronik yüzeyel '
                'inflamasyon yatar. Kız çocuklarında doğuştan genital anomali sanılarak büyük panik yaratır; oysa '
                'edinsel ve benign bir tablodur. EN BÜYÜK KLİNİK HATA: Poliklinikte elle veya aletle ZORLAYARAK YIRTIP '
                'AYIRMAKTIR! Mekanik zorlama kanama, yoğun ağrı, psikolojik travma ve daha kalın skarlı nüks '
                'yapışıklığa neden olur. Asemptomatik olgularda kendiliğinden açılması beklenir veya saf vazelin '
                'sürülür. İdrar akımında göllenme, zorlanma veya sık İYE varsa tedavi günde 1-2 kez ince tabaka '
                'TOPİKAL ÖSTROJENLİ KREMDİR (1-2 hafta); zar kendiliğinden nazikçe eriyerek açılır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Genital yapışıklık şüphesiyle getirilen bu kız çocukta fizik muayenede öncelikle neye dikkat '
                         'etmelisiniz?',
             'options': [{'text': 'Genital bölgeyi dikkatlice gözlemlemek, yapışıklığın şeffaflığını ve idrar çıkış '
                                  'deliğinin açıklığını değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Çocuk kurbağa pozisyonunda (frog-leg) yatırılır, labia majoralar nazikçe '
                                         'laterale çekilir. Orta hatta grimsi-beyaz, avasküler, yarı saydam bir hat '
                                         'görülür. Üstte üretral orifis açıklığı kontrol edilir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 98/dk, SS 22/dk, SpO2 %99. Çocuk sakin. '
                                         'Genital Muayene: Labia minoralar forşetten klitoris tabanına doğru orta '
                                         'hatta yarı saydam, ince, avasküler fibröz bir zar ile birbirine yapışık '
                                         'izlendi. Klitoris normal boyutta ve yapıda. En üst kısımda idrar çıkışına '
                                         "izin veren yaklaşık 2-3 mm'lik küçük bir açıklık mevcut. Aktif vulvit, "
                                         'pürülan akıntı veya travma bulgusu saptanmadı.'},
                         {'text': 'Zarı açmak için acil olarak cerrahi pensetle tutarak var gücüyle iki yana doğru '
                                  'çekip yırtmak',
                          'is_correct': False,
                          'scenario_update': 'Mekanik zorlama labialarda derin yırtık, yoğun kanama ve çocukta '
                                             'şiddetli ağlama travması yarattı.',
                          'teaching_point': 'Bu tür yapışıklıklar kesinlikle mekanik olarak zorlanarak yırtılmaz; '
                                            'travma daha ağır skarlı nükse yol açar.'},
                         {'text': 'Vajina agenezisi düşünerek hastaya derhal acil yapay vajina rekonstrüksiyon '
                                  'cerrahisi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Benign yüzeyel zar için planlanan majör cerrahi girişim aileyi gereksiz '
                                             'yere dehşete düşürdü.',
                          'teaching_point': 'Bu durum vajina agenezisi değildir; labia minoraların yüzeyel ve geçici '
                                            'bir adezyonudur.'},
                         {'text': 'İdrar yapamadığını varsayıp mesaneye körlemesine kalın metal dilatatör bujisi '
                                  'sokmaya çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Metal buji üretral mukozayı zedeledi ve ciddi üretroraji ile hematüriye '
                                             'yol açtı.',
                          'teaching_point': 'İdrar açıklığı varken üretral dilatasyon veya kateterizasyon '
                                            'kontrendikedir.'}]},
            {'stage_title': 'Laboratuvar ve İleri İncelemeler',
             'question': 'Fizik muayenede tipik labial adezyon saptanan, ateşi olmayan bu çocukta tanısal inceleme '
                         'yaklaşımı ne olmalıdır?',
             'options': [{'text': 'İdrar yolu enfeksiyonunu dışlamak amacıyla tam idrar tahlili istemek, invaziv '
                                  'tetkiklerden kaçınmak',
                          'is_correct': True,
                          'explanation': 'İdrarın geriye göllenmesine bağlı asemptomatik bakteriüri veya lökositüri '
                                         'gelişip gelişmediğini anlamak için TİT yeterlidir. Hormon paneli, genetik '
                                         'test veya ileri görüntüleme gerekmez.',
                          'new_finding': 'Tam İdrar Tahlili: Dansite 1018, pH 6.5, lökosit esteraz negatif, nitrit '
                                         'negatif, mikroskopide lökosit 1-2. İdrar yolu enfeksiyonu saptanmadı. '
                                         'Klitoris normal ve ambigus genitalya bulunmadığı için kromozom analizi veya '
                                         '17-OH progesteron gibi endokrinolojik tetkiklere gerek görülmedi.'},
                         {'text': 'Ambigus genitalya şüphesiyle hastadan acil karyotip analizi ve tüm adrenal bez '
                                  'tomografisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Normal klitoris ve dişi genital yapısına rağmen yapılan tetkikler ailede '
                                             'kuşkulu cinsiyet paniği yarattı.',
                          'teaching_point': 'Normal klitoral yapı ve tipik ince şeffaf zar varlığında karyotip veya '
                                            'adrenal tomografi gerekmez.'},
                         {'text': 'Vajina içini görmek için bebeğe genel anestezi altında acil kontrastlı vajinoskopi '
                                  'uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz anestezi ve invaziv vajinoskopi vajinal duvarda laserasyona '
                                             'neden oldu.',
                          'teaching_point': 'Bu yapışıklıkta intrakaviter vajinal patoloji yoktur; vajinoskopi '
                                            'endikasyonu bulunmaz.'},
                         {'text': 'Zarın arkasındaki sıvıyı aspire etmek için ultrason eşliğinde kalın trokar iğnesi '
                                  'batırmak',
                          'is_correct': False,
                          'scenario_update': 'İğne girişi vulvada hematom oluşturdu ve enfeksiyon odağı yarattı.',
                          'teaching_point': 'Yapışıklıkta aspire edilecek kistik sıvı yoktur; cerrahi ponksiyon '
                                            'yapılmaz.'}]},
            {'stage_title': 'Klinik Ön Tanı ve Ayırıcı Tanı',
             'question': 'Labia minoraları orta hatta ince şeffaf zarla yapışık, klitorisi normal bu kız çocukta '
                         'tanınız nedir?',
             'options': [{'text': 'Benign edinsel labial füzyon sinekşi',
                          'is_correct': True,
                          'explanation': 'Kız çocuklarında bez dermatiti ve fizyolojik düşük östrojen zemininde '
                                         'gelişen, orta hatta ince yarı saydam zarla karakterize tablo labial '
                                         'füzyondur.',
                          'new_finding': 'Kesin Tanı: Labial Füzyon (Sinekşi) doğrulanmıştır. Topikal tedavi planına '
                                         'geçildi.'},
                         {'text': 'Konjenital adrenal hiperplazi virilizasyonu',
                          'is_correct': False,
                          'scenario_update': "KAH'ta klitoromegali (büyük klitoris) ve labial füzyondan ziyade "
                                             'labioskrotal kıvrımlarda koyu pigmentasyon olur.',
                          'teaching_point': 'Klitoris normal boyuttaysa ve zar sonradan oluşmuşsa virilizasyon '
                                            'düşünülmez.'},
                         {'text': 'İmperfore hymen vajinal obstrüksiyonu',
                          'is_correct': False,
                          'scenario_update': 'İmperfore hymende yapışıklık labiumlarda değil hymen halkasındadır; '
                                             'introitus açıktır.',
                          'teaching_point': 'Labial füzyon labia minoraların yapışıklığıdır; imperfore hymen ise '
                                            'introitusun kapalı olmasıdır.'},
                         {'text': 'Akut flegmonöz vulvovajinit absesi',
                          'is_correct': False,
                          'scenario_update': 'Vulvovajinitte yoğun pürülan akıntı, şiddetli ısı artışı ve ödem olur; '
                                             'şeffaf ince zar olmaz.',
                          'teaching_point': 'Akut flegmon pürülan ve kızarıktır; sinekşi ise inflamasyonsuz şeffaf bir '
                                            'yapışıklıktır.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'İdrar yaparken zorlanma hissi olan bu çocuğun en uygun tedavisi ve aile eğitimi nedir?',
             'options': [{'text': 'Orta hatta günde iki kez topikal östrojenli krem uygulamak, zorlamadan kaçınmayı '
                                  'tembihlemek',
                          'is_correct': True,
                          'explanation': 'Semptomatik (idrar akımında sapma, zorlanma veya göllenme olan) olgularda '
                                         'günde 1-2 kez adezyon hattına nazikçe topikal östrojenli krem (örn. estriol '
                                         'veya konjuge östrojen) sürülür (1-2 hafta). Zar kendiliğinden yumuşayıp '
                                         'açılır. Açıldıktan sonra nüksü önlemek için saf vazelin kullanılır. '
                                         'Kesinlikle elle zorlanmaz.',
                          'new_finding': 'Topikal östrojenli krem reçete edildi, pamuklu çubukla sadece zar hattına '
                                         'nazikçe sürme tekniği anlatıldı. 10 gün sonra kontrolde zarın kendiliğinden '
                                         'tamamen eriyip açıldığı, idrar akımının normale döndüğü görüldü.'},
                         {'text': 'Zarı açmak için hastayı hemen ameliyathaneye alıp labiumları cerrahi neşterle '
                                  'boydan boya kesmek',
                          'is_correct': False,
                          'scenario_update': 'Cerrahi insizyon postoperatif iyileşme döneminde daha kalın ve yoğun '
                                             'fibrotik yapışıklık yarattı.',
                          'teaching_point': 'Bu tabloda ilk basamak cerrahi neşter değildir; medikal topikal tedavi '
                                            '%90 başarılıdır.'},
                         {'text': 'Hiçbir krem vermeyip ailenin evde her banyoda zarı tırnaklarıyla zorlayarak '
                                  'yırtmasını önermek',
                          'is_correct': False,
                          'scenario_update': 'Tırnakla yırtma girişimi enfeksiyon, kanama ve çocukta banyo fobisi ile '
                                             'idrar tutma geliştirdi.',
                          'teaching_point': 'Ailenin mekanik olarak ayırması yasaklanmalıdır; travma durumu '
                                            'kötüleştirir.'},
                         {'text': 'Zarın erimesi için çocuğun genital bölgesine günde üç kez saf aseton ve alkol '
                                  'dökmek',
                          'is_correct': False,
                          'scenario_update': 'Aseton ve alkol genital mukozada ağır kimyasal yanık ve nekroz '
                                             'oluşturdu.',
                          'teaching_point': 'Genital bölgeye kimyasal yakıcı maddeler asla uygulanmaz.'}]}]},
 {'id': 'G68',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '12 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Üç haftadır okul günleri öğleden sonra başlayan, başın etrafında mengene gibi sıkıştırıcı ağrı',
  'history': "On iki yaşındaki erkek çocuk ailesiyle Yeşil Alana başvuruyor: 'Son üç haftadır özellikle hafta içi "
             'okuldan çıkınca tüm başını saran, sanki başına sıkı bir şapka takılmış veya mengene ile sıkılıyormuş '
             'gibi künt bir ağrıdan yakınıyor. Ağrı zonklamıyor, kusması veya bulantısı olmuyor, ışıktan kaçmıyor. '
             'Ağrısına rağmen oyun oynayabiliyor ama çok yorulduğunu söylüyor. Hafta sonları ve tatil günlerinde baş '
             'ağrısı hiç olmuyor. Günde 5-6 saat telefon ve tablet başında oyun oynuyor, geceleri geç yatıyor. Görme '
             "kusuru veya ateş öyküsü yok.'",
  'final_diagnosis': 'Pediatrik Gerilim Tipi Baş Ağrısı (Aşırı Ekran Maruziyeti ve Duruş Bozukluğuna Sekonder)',
  'disposition': 'Yeşil Alandan Nörolojik Değerlendirme, Ekran Kısıtlaması, Ergonomi ve Yaşam Tarzı Önerisi ile '
                 'Taburculuk',
  'case_pearl': 'Gerilim tipi baş ağrısı (GTBA), adolesan ve okul çağı çocuklarında en sık görülen primer baş ağrısı '
                'türüdür. Migrenden temel farkları: 1) ZONKLAYICI DEĞİLDİR; künt, basıcı, başı bir mengene gibi sıkan '
                'veya bant tarzındadır. 2) Fiziksel aktiviteyle artmaz (çocuk hareket edebilir). 3) Bulantı, kusma, '
                'belirgin fotofobi/fonofobi EŞLİK ETMEZ. En sık tetikleyiciler: Uzun ekran süresi (mavi ışık), '
                'servikal kas spazmı (kötü postür/öne eğik boyun), uykusuzluk, dehidratasyon ve okul stresidir. '
                'Nörolojik muayene ve fundoskopi tamamen normaldir; nörogörüntüleme (BT/MRG) gerekmez. Tedavi '
                'analjezik haplara bağımlı olmak DEĞİL; ekran süresini kısıtlamak (<2 saat), boyun germe egzersizleri, '
                'düzenli uyku ve yeterli su tüketimidir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Bant tarzı sıkıştırıcı baş ağrısı olan bu çocukta fizik muayenede öncelikle nelere '
                         'bakmalısınız?',
             'options': [{'text': 'Nörolojik muayene yapmak, fundoskopide optik diski incelemek ve perikraniyoservikal '
                                  'kas hassasiyetini değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Sekonder intrakraniyal patolojileri dışlamak için nörolojik muayene ve '
                                         'fundoskopi yapılır. Kas kaynaklı baş ağrılarında sıklıkla trapezius ve '
                                         'suboksipital kaslarda spazm ve hassasiyet saptanır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 76/dk, SS 16/dk, SpO2 %99, TA 105/68 mmHg. '
                                         'Genel durumu iyi, oryantasyon ve kooperasyon tam. Kraniyal sinirler intakt, '
                                         'motor/duyu defisiti yok. Serebellar testler ve yürüyüş doğal. Ense sertliği '
                                         'yok. Fundoskopide optik disk sınırları net, venöz pulsasyon mevcut, '
                                         'papilödem yok. Bilateral boyun arka kaslarında (trapezius ve '
                                         'sternokleidomastoid) belirgin kas spazmı ve tetik nokta hassasiyeti '
                                         'saptandı.'},
                         {'text': 'Hastada akut subaraknoid kanama düşünerek acil olarak ameliyathanede kraniyotomi '
                                  'başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Haftalardır süren hafif ağrıda kanama düşünülerek yapılan cerrahi '
                                             'hazırlığı gereksiz panik yarattı.',
                          'teaching_point': 'Subaraknoid kanama ani gök gürültüsü ağrısı ve koma ile gelir; kronik '
                                            'hafif ağrıyla ilgisizdir.'},
                         {'text': 'Ağrının nedenini bulmak için çocuğa hiçbir klinik muayene yapmadan derhal '
                                  'psikiyatrik yatış vermek',
                          'is_correct': False,
                          'scenario_update': 'Fizik muayenesiz psikiyatrik yatış kas spazmını gözden kaçırdı ve ailede '
                                             'tepki doğurdu.',
                          'teaching_point': 'Tüm baş ağrılarında önce tam organik nörolojik muayene tamamlanmalıdır.'},
                         {'text': 'Beyin sapı ölümü düşünerek hastayı acil yapay solunum cihazına bağlayıp entübe '
                                  'etmek',
                          'is_correct': False,
                          'scenario_update': 'Konuşan ve yürüyen bilinçli çocuğa entübasyon girişimi ağır laringeal '
                                             'travma yarattı.',
                          'teaching_point': 'GKS skoru 15 olan uyanık hastada solunum cihazı endikasyonu yoktur.'}]},
            {'stage_title': 'Laboratuvar ve İleri İncelemeler',
             'question': 'Nörolojik muayenesi tamamen normal, papilödemi olmayan ve kas spazmı bulunan hastada tetkik '
                         'yaklaşımı nedir?',
             'options': [{'text': 'Kırmızı bayrak bulunmadığı ve klinik kriterler karşılandığı için acil '
                                  'nörogörüntüleme yapmaktan kaçınmak',
                          'is_correct': True,
                          'explanation': 'Amerikan Baş Ağrısı Derneği ve Pediatri Akademisi kılavuzlarına göre '
                                         'nörolojik muayenesi normal, papilödemi ve kırmızı bayrağı olmayan primer '
                                         'basıcı baş ağrılarında BT veya MRG ÇEKİLMESİ ÖNERİLMEZ.',
                          'new_finding': 'Hastada sabah uykudan uyandıran ağrı, fışkırır kusma, görme alanı defisiti '
                                         've nörolojik kayıp yoktur. Öykü ve muayene primer basıcı baş ağrısı tanı '
                                         'kriterlerini tam karşılamaktadır. Gereksiz iyonizan kafa tomografisi ve '
                                         'anestezi gerektirecek MRG incelemelerinden kaçınıldı.'},
                         {'text': 'En ufak baş ağrısında bile mutlaka rutin olarak tüm omurga ve beyin tomografisi '
                                  'çekmek',
                          'is_correct': False,
                          'scenario_update': 'Her baş ağrısına BT çekilmesi çocukta gereksiz kanserojen kümülatif '
                                             'radyasyon birikimi yaptı.',
                          'teaching_point': 'Kırmızı bayrağı olmayan pediatrik baş ağrılarında rutin radyolojik tarama '
                                            'yapılmaz.'},
                         {'text': 'Tanıyı teyit etmek için hastaya acil olarak dört ekstremiteden invaziv iğne '
                                  'elektromiyografisi yapmak',
                          'is_correct': False,
                          'scenario_update': 'Ağrılı iğne EMG işlemi çocukta şiddetli anksiyete ve kas spazmında artış '
                                             'yarattı.',
                          'teaching_point': "Kas kaynaklı baş ağrılarında invaziv EMG'nin yeri yoktur; tanı anamnez "
                                            'ile konur.'},
                         {'text': 'Kanda beyin tümörü belirteçlerini aramak amacıyla hastadan yirmi tüp genetik panel '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'Kanda primer beyin tümörünü gösteren rutin bir kan testi yoktur; aileye '
                                             'yüksek masraf çıktı.',
                          'teaching_point': 'Baş ağrılarında tümör kandan bakılmaz; klinik nörolojik muayene ve '
                                            'kırmızı bayraklar esastır.'}]},
            {'stage_title': 'Klinik Ön Tanı ve Ayırıcı Tanı',
             'question': 'Bant tarzında basıcı, zonklamayan, bulantısız ve aşırı ekran maruziyeti olan bu çocukta '
                         'tanınız nedir?',
             'options': [{'text': 'Epizodik gerilim tipi baş ağrısı',
                          'is_correct': True,
                          'explanation': 'Bilateral mengene tarzı sıkıştırıcı karakter, fiziksel aktiviteyle '
                                         'kötüleşmeme, bulantı/kusmanın olmaması ve boyun kas spazmı gerilim tipi baş '
                                         'ağrısına özgüdür.',
                          'new_finding': 'Kesin Tanı: Epizodik Gerilim Tipi Baş Ağrısı doğrulanmıştır. Yaşam tarzı '
                                         'planına geçildi.'},
                         {'text': 'Şiddetli auralı migren atağı',
                          'is_correct': False,
                          'scenario_update': 'Migrende zonklayıcı tek taraflı ağrı, fotofobi, fonofobi ve '
                                             'bulantı/kusma beklenir; hastada bunlar yoktur.',
                          'teaching_point': 'Zonklama ve kusmanın olmaması migreni gerilim baş ağrısından ayıran en '
                                            'kritik noktadır.'},
                         {'text': 'Akut bakteriyel pürülan sinüzit',
                          'is_correct': False,
                          'scenario_update': 'Sinüzitte pürülan burun akıntısı, yüzde dolgunluk, ateş ve öne eğilmekle '
                                             'artan zonklayıcı ağrı olur.',
                          'teaching_point': 'Burun akıntısı ve yüzde bası hissi olmadan izole gerilim ağrısı sinüzit '
                                            'değildir.'},
                         {'text': 'Beyin içi yer kaplayan tümör',
                          'is_correct': False,
                          'scenario_update': 'Tümörde sabah fışkırır kusmalar, nörolojik kayıplar ve fundoskopide '
                                             'papilödem görülür.',
                          'teaching_point': 'Hafta sonu kaybolan ve papilödemi olmayan ağrılarda beyin tümörü '
                                            'beklenmez.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Gerilim tipi baş ağrısı tanısı alan bu hastada en uygun kanıta dayalı yaşam tarzı ve tedavi '
                         'yönetimi nedir?',
             'options': [{'text': 'Ekran süresini kısıtlamak, boyun germe egzersizleri, düzenli uyku ve hidrasyon '
                                  'önermek',
                          'is_correct': True,
                          'explanation': 'Gerilim baş ağrısında temel tedavi tetikleyicilerin eliminasyonudur: Günlük '
                                         'ekran süresi <1-2 saate indirilir, duruş (postür) düzeltilir, boyun ve omuz '
                                         'germe egzersizleri yapılır, günde en az 1.5-2 litre su içilir. Gereksiz '
                                         "aşırı analjezik kullanımı 'ilaç aşırı kullanım baş ağrısına' (MOH) yol "
                                         'açabileceğinden ilaç kısıtlanır.',
                          'new_finding': 'Aileye ekran kısıtlaması, ergonomik çalışma masası ve uyku düzeni eğitimi '
                                         'verildi. İki hafta sonra kontrolde ekran süresi azaltıldıktan sonra baş '
                                         'ağrılarının tamamen geçtiği ve ilaç gerekmediği öğrenildi.'},
                         {'text': 'Günde dört kez aralıksız yüksek doz ergotamin ve kodeinli narkotik analjezik şurup '
                                  'reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Sürekli analjezik alımı çocukta ilaca bağlı analjezik bağımlılığı ve '
                                             'kronik baş ağrısı başlattı.',
                          'teaching_point': 'Sık analjezik kullanımı ilaç aşırı kullanım baş ağrısı (Medication '
                                            'Overuse Headache) yapar.'},
                         {'text': 'Ağrıyı kesmek amacıyla hastanın saçlarını tamamen kazıtıp başına cerrahi akupunktur '
                                  'dikişleri atmak',
                          'is_correct': False,
                          'scenario_update': 'Saçlı deride dikiş izleri ve sekonder enfeksiyon oluşarak ağrıyı daha da '
                                             'artırdı.',
                          'teaching_point': 'Gerilim baş ağrısında invaziv saçlı deri cerrahisi kesinlikle yoktur; '
                                            'yaşam tarzı değişimi esastır.'},
                         {'text': 'Çocuğun hiç hareket etmemesi için boynuna ömür boyu rijit çelik boyunluk taktırmak',
                          'is_correct': False,
                          'scenario_update': 'Uzun süreli rijit boyunluk boyun kaslarında atrofiye ve boyun '
                                             'hareketlerinde donmaya yol açtı.',
                          'teaching_point': 'Boyunluk kasları zayıflatır; aksine aktif boyun germe ve güçlendirme '
                                            'egzersizleri yapılmalıdır.'}]}]},
 {'id': 'G69',
  'category': '👂 Kulak Ağrısı & KBB',
  'age': '7 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Burun karıştırma sonrası sağ burun deliğinden başlayan taze kırmızı renkli burun kanaması',
  'history': "Yedi yaşındaki erkek çocuk burnuna pamuk tıkanmış halde Yeşil Alana getiriliyor: 'Yarım saat önce "
             'televizyon izlerken parmağıyla burnunu karıştırmış, ardından sağ burnundan şarıl şarıl kan akmaya '
             'başladı. Annesi panikle çocuğun kafasını arkaya doğru yatırmış, bu sefer de çocuk kanı yutup öğürmüş ve '
             'bir miktar pıhtılı kan çıkarmış. Daha önce belirgin kanama öyküsü, vücudunda morluk veya diş eti '
             "kanaması yok. Ailede kanama hastalığı bulunmuyor. Ateşi veya düşme çarpma travması yok.'",
  'final_diagnosis': 'Akut Anterior Epistaksis (Kiesselbach Pleksusu / Little Bölgesi Dijital Travmasına Bağlı Basit '
                     'Burun Kanaması)',
  'disposition': 'Yeşil Alanda Doğru Bası Tekniği ile Kanamayı Durdurma, Nemlendirici Merhem Eğitimi ile Taburculuk',
  'case_pearl': "Çocukluk çağındaki burun kanamalarının %90'ından fazlası ANTERİOR (ön) kaynaklıdır ve septumun ön-alt "
                'kısmındaki KİESSELBACH PLEKSUSUNDAN (Little bölgesi) kaynaklanır. Burası 4 arterin anastomoz yaptığı '
                'çok zengin bir damar yumağıdır. En sık tetikleyiciler: Kuru hava, burun karıştırma (dijital '
                "mikrotravma) ve viral rinit/alerjidir. TOPLUMDAKİ EN BÜYÜK YANLIŞ: 'Kafayı geriye yatırmak'tır! "
                'Kafayı arkaya yatırmak kanamayı durdurmaz; kanın yutağa akmasına, yutulup bulantı/kusmaya veya hava '
                'yoluna kaçarak asfiksiye yol açar! DOĞRU YAKLAŞIM: 1) Baş hafifçe ÖNE EĞİLİR, 2) Burun deliklerinin '
                'yumuşak kanatları (ala nasi) parmaklarla iki yandan KARTİLAJ SEPTUMA DOĞRU 10-15 DAKİKA ARALIKSIZ '
                'SIKILIR, 3) Ağızdan nefes alması ve ağza gelen kanı tükürmesi söylenir. Kanama durduktan sonra '
                'mukozal kuruluk için topikal nemlendirici merhem (vazelin) önerilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Aktif burun kanamasıyla gelen bu çocukta ilk klinik değerlendirme ve kanama odağı tespiti '
                         'nasıl yapılmalıdır?',
             'options': [{'text': 'Vital bulguları kontrol etmek, başı hafif öne eğerek anterior rinoskopi ile ön '
                                  'septum bölgesini incelemek',
                          'is_correct': True,
                          'explanation': 'Hemodinamik stabilite (KTA, TA) değerlendirilir. Kanın hava yoluna kaçmaması '
                                         've yutulmaması için baş hafif öne eğilir. Işık kaynağı ve burun spekulumu '
                                         'ile ön damar ağı taranır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 88/dk, SS 18/dk, SpO2 %100, TA 98/62 mmHg. '
                                         'Çocuk biraz korkmuş ancak stabil. Anterior Rinoskopi: Sağ nazal septumun ön '
                                         'kısmında küçük bir mukozal abrazyon ve oradan sızan taze kapiller kanama '
                                         'odağı görüldü. Orofarenks arka duvarında aktif kan akışı izlenmedi. Ciltte '
                                         'peteşi, purpura veya ekimoz saptanmadı.'},
                         {'text': 'Kanamayı durdurmak için çocuğun kafasını derhal tam geriye yatırıp tavana baktırmak',
                          'is_correct': False,
                          'scenario_update': 'Kafanın arkaya atılması kanın yutağa dolmasına, aspirasyon öksürüğüne ve '
                                             'kanlı kusmaya yol açtı.',
                          'teaching_point': 'Burun kanamasında baş asla arkaya atılmaz; kan yutulur ve hava yoluna '
                                            'aspire olabilir, baş öne eğilmelidir.'},
                         {'text': 'Hastada masif karotis arter rüptürü düşünerek acil boyun cerrahisi ile şah damarını '
                                  'bağlamak',
                          'is_correct': False,
                          'scenario_update': 'Basit burun kanamasında yapılan boyun cerrahisi hastada inme ve kalıcı '
                                             'hemipleji doğurdu.',
                          'teaching_point': 'Basit kapiller kanamalarda karotis rüptürü düşünülmez; lokal kompresyon '
                                            'yeterlidir.'},
                         {'text': 'Kanama durana kadar çocuğun ağzını ve her iki burun deliğini bantlayarak nefesini '
                                  'tıkamak',
                          'is_correct': False,
                          'scenario_update': 'Ağız ve burnun kapatılması çocukta akut hipoksi, solunum arresti ve '
                                             'panik yarattı.',
                          'teaching_point': 'Hastanın ağızdan serbestçe nefes almasına izin verilmelidir.'}]},
            {'stage_title': 'Laboratuvar ve İleri İncelemeler',
             'question': 'İlk kez burun karıştırma sonrası kanayan ve vitalleri stabil olan bu çocukta tanısal tetkik '
                         'yaklaşımı nedir?',
             'options': [{'text': 'Kanamaya yatkınlık bulgusu ve travma olmadığından kan tahlili yapmadan lokal '
                                  'tedaviye odaklanmak',
                          'is_correct': True,
                          'explanation': 'İlk kez olan, tetikleyicisi net (burun karıştırma), sistemik kanama bulgusu '
                                         '(peteşi, ekimoz, hematüri) olmayan izole ön burun kanamalarında pıhtılaşma '
                                         'testi veya tam kan sayımı gerekmez.',
                          'new_finding': 'Hastanın kişisel ve ailevi kanama öyküsü negatiftir. Karaciğer hastalığı '
                                         'veya antikoagülan kullanımı yoktur. Lokal ön septum kaynaklı basit mekanik '
                                         'kanama olduğu doğrulandı. Gereksiz iğne ponksiyonu ile pıhtılaşma paneli '
                                         '(PT, aPTT, INR) çalışılmasına gerek görülmedi.'},
                         {'text': 'Kanamanın nedenini bulmak amacıyla acil genel anestezi altında paranazal sinüs '
                                  'cerrahi eksplorasyonu yapmak',
                          'is_correct': False,
                          'scenario_update': 'Basit septum kanamasında yapılan cerrahi eksplorasyon nazal konkalarda '
                                             'kalıcı sineşiye yol açtı.',
                          'teaching_point': 'Ön burun kanamalarında sinüs cerrahisi kesinlikle endike değildir; basit '
                                            'kompresyonla durur.'},
                         {'text': 'Kemik iliği yetmezliği şüphesiyle hastaya derhal acil yatak başı kemik iliği '
                                  'biyopsisi uygulamak',
                          'is_correct': False,
                          'scenario_update': 'İzole burun kanamasında yapılan kemik iliği ponksiyonu çocukta ağır '
                                             'travma ve hematom yarattı.',
                          'teaching_point': 'Tekrarlamayan, izole ve mekanik burun kanamalarında kemik iliği biyopsisi '
                                            'endikasyonu yoktur.'},
                         {'text': 'Kanamayı teyit etmek için kafa tabanına dört yönlü kateterli anjiyografi serisi '
                                  'çekmek',
                          'is_correct': False,
                          'scenario_update': 'İnvaziv serebral anjiyografi çocukta vasküler disseksiyon ve anestezi '
                                             'komplikasyonu geliştirdi.',
                          'teaching_point': 'Ön burun kanamasında invaziv vasküler anjiyografi çekilmez.'}]},
            {'stage_title': 'Klinik Ön Tanı ve Ayırıcı Tanı',
             'question': 'Burun karıştırma sonrası ön septumdan sızan, vitalleri normal bu çocukta tanınız nedir?',
             'options': [{'text': 'Akut anterior basit epistaksis',
                          'is_correct': True,
                          'explanation': 'Little bölgesindeki damar ağının dijital travmasına bağlı lokal yüzeyel '
                                         'kapiller kanama tablosu anterior epistaksistir.',
                          'new_finding': 'Kesin Tanı: Akut Anterior Epistaksis doğrulanmıştır. Doğru bası tedavisine '
                                         'geçildi.'},
                         {'text': 'Masif posterior sfenopalatin arter kanaması',
                          'is_correct': False,
                          'scenario_update': 'Posterior kanamalarda kan yutağın arkasından sürekli oluk gibi akar ve '
                                             'ön kompresyonla durmaz.',
                          'teaching_point': 'Posterior kanamalar genellikle yaşlılarda veya ağır yüz travmalarında '
                                            'olur; çocuklarda %90 ön kaynaklıdır.'},
                         {'text': 'Ağır hemofili A kanama krizi',
                          'is_correct': False,
                          'scenario_update': 'Hemofilide derin eklem içi kanamalar (hemartroz) ve uzamış hematomlar '
                                             'görülür; izole basit epistaksis beklenmez.',
                          'teaching_point': 'Eklem kanaması öyküsü ve pıhtılaşma bozukluğu olmadan hemofili '
                                            'düşünülmez.'},
                         {'text': 'Juvenil nazofarengeal anjiyofibrom tümörü',
                          'is_correct': False,
                          'scenario_update': 'Anjiyofibrom adölesan erkeklerde tekrarlayan masif kanamalar ve tek '
                                             'taraflı burun tıkanıklığı ile seyreder.',
                          'teaching_point': 'İlk kez burun karıştırmayla olan basit kanamada vasküler tümör '
                                            'düşünülmez.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Anterior burun kanaması olan bu çocukta Yeşil Alanda kanamayı durduracak en uygun ilk '
                         'basamak müdahale nedir?',
             'options': [{'text': 'Başı öne eğerek burun kanatlarını septuma doğru on dakika kesintisiz sıkmak ve '
                                  'nemlendirici önermek',
                          'is_correct': True,
                          'explanation': 'Doğru bası tekniği: Baş hafif öne eğilir, burun deliklerinin yumuşak '
                                         'kıkırdak kanatları (ala nasi) parmaklarla septum kemiğine doğru 10-15 dakika '
                                         'boyunca hiç bırakmadan sıkıştırılır. Kanama durduktan sonra mukozanın '
                                         'kurumasını önlemek için burun içine günde 2 kez vazelin veya nemlendirici '
                                         'damla sürülmesi önerilir.',
                          'new_finding': 'Baş öne eğilip burun kanatlarına 10 dakika kesintisiz kompresyon uygulandı. '
                                         '10 dakika sonra bası kaldırıldığında kanamanın tamamen durduğu görüldü. '
                                         'Mukoza nemlendirici merhem sürüldü ve taburcu edildi.'},
                         {'text': 'Hastanın her iki burun deliğine çekiçle metal cerrahi tıkaçlar çakıp hava yolunu '
                                  'kapatmak',
                          'is_correct': False,
                          'scenario_update': 'Metal cisim çakılması nazal septumda parçalı kırık ve nekroza neden '
                                             'oldu.',
                          'teaching_point': 'Basit ön kanamalarda koter veya cerrahi tampon bile gerekmez; elle bası '
                                            '%95 yeterlidir.'},
                         {'text': 'Kanamayı pıhtılaştırmak için burun deliğinin içine kaynar zeytinyağı ve sirke '
                                  'damlatmak',
                          'is_correct': False,
                          'scenario_update': 'Kaynar sıvı burun mukozasında üçüncü derece yanık ve kalıcı septal '
                                             'perforasyon yaptı.',
                          'teaching_point': 'Burun içine tahriş edici ve sıcak maddeler asla sokulmamalıdır.'},
                         {'text': 'Hiçbir bası yapmadan kanamanın kendiliğinden durması için çocuğu koşup zıplatmak',
                          'is_correct': False,
                          'scenario_update': 'Egzersiz ve taşikardi kan basıncını yükselterek burun kanamasını daha da '
                                             'şiddetlendirdi.',
                          'teaching_point': 'Kanama sırasında çocuk sakinleştirilmeli ve istirahat halinde kompresyon '
                                            'uygulanmalıdır.'}]}]},
 {'id': 'G70',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '8 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Sağ kolunda ve boynunda iki haftadır giderek genişleyen, kenarları kaşıntılı ve pütürlü kırmızı halka',
  'history': "Sekiz yaşındaki erkek çocuk annesi tarafından Yeşil Alana getiriliyor: 'Yaklaşık iki hafta önce sağ "
             'kolunda küçük kırmızı bir sivilce gibi başlamıştı. Gün geçtikçe madeni para büyüklüğünde bir halka gibi '
             'genişledi. Ortası soluklaştı, kenarları ise kırmızı, kabarık ve minik pütürlü bir çizgi halini aldı. '
             'Şimdi benzer bir halka boynunda da çıkmaya başladı. Hafif kaşıntısı var ama canı acımıyor. Bir ay önce '
             'sokakta buldukları yavru bir kediyi eve alıp sevmişlerdi. Ateşi veya boğaz ağrısı yok. Eczaneden '
             "aldıkları kortizonlu kremi sürdüklerinde lezyon daha da yayılmış.'",
  'final_diagnosis': 'Tinea Korporis (Dermatofitoz / Microsporum canis Kaynaklı Vücut Mantar Enfeksiyonu)',
  'disposition': 'Yeşil Alandan Topikal Antifungal Tedavi, Kortizon Kısıtlaması ve Hayvan Teması Rehberliği ile '
                 'Taburculuk',
  'case_pearl': 'Tinea korporis (vücut mantarı / ringworm), çocuklarda dermatofit mantarların (en sık zoofilik '
                'Microsporum canis veya Trichophyton rubrum) keratinize stratum korneuma yerleşmesiyle gelişen son '
                'derece sık bir yüzeyel mikozdur. Kedi/köpek teması anamnezde çok tipiktir. TİPİK MORFOLOJİ: Anüler '
                '(halka şeklinde), sınırları keskin, kenarları aktif-eritematöz-skuamlı-papüllü, merkezi ise iyileşme '
                'gösteren (santral solukluk) lezyonlardır. EN BÜYÜK YANLIŞ: Lezyona TOPİKAL KORTİKOSTEROİD '
                'sürülmesidir! Kortizon lokal immüniteyi baskılayarak mantarın hızla büyümesine, morfolojisinin '
                "bozulmasına ve 'TİNEA İNCOGNİTO' tablosuna dönüşmesine yol açar! Tedavi günde 1-2 kez 2-4 hafta "
                'süreyle TOPİKAL ANTİFUNGALDİR (Terbinafin, Klotrimazol veya Mikonazol). Evdeki temaslı hayvan '
                'veteriner kontrolüne gönderilmelidir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Halka şeklinde genişleyen cilt lezyonu olan bu çocukta dermatolojik muayenede nelere dikkat '
                         'etmelisiniz?',
             'options': [{'text': 'Lezyonun anüler morfolojisini, sınırlarını, santral solukluğunu, skuam dağılımını '
                                  've diğer vücut bölgelerini incelemek',
                          'is_correct': True,
                          'explanation': 'Lezyonun halkasal yapısı, kenar aktifliği (eritem ve kepeklenme) ve '
                                         'merkezdeki iyileşme değerlendirilir. Saçlı deri, ayak veya tırnak tutulumu '
                                         'olup olmadığını anlamak için tüm cilt taranır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 80/dk, SS 18/dk, SpO2 %99. Çocuk aktif ve '
                                         'neşeli. Dermatolojik Muayene: Sağ ön kolda yaklaşık 3 cm çapında, sınırları '
                                         'belirgin, anüler (halka) lezyon izlendi. Lezyonun kenarları kabarık, '
                                         'eritematöz, hafif pütürlü ve ince skuamlı (kepekli); merkezi ise soluk ve '
                                         'basık. Sağ boyun lateralinde 1.5 cm benzer bir uydu halka lezyon mevcut. '
                                         'Saçlı deri, tırnaklar ve kasık bölgesi tamamen temiz. Sistemik muayenede '
                                         'patoloji yok.'},
                         {'text': 'Lezyonun malign melanom olduğunu düşünerek acil olarak kolun tamamını cerrahi '
                                  'ampütasyona almak',
                          'is_correct': False,
                          'scenario_update': 'Benign mantar enfeksiyonunda yapılan fahiş cerrahi girişim geri dönüşsüz '
                                             'uzuv kaybına yol açtı.',
                          'teaching_point': 'Anüler pullanan lezyonlar yüzeyel mantar enfeksiyonudur; melanomla klinik '
                                            'olarak hiçbir benzerliği yoktur.'},
                         {'text': 'Döküntüyü suçiçeği sayıp hastayı negatif basınçlı yoğun bakım odasına kilitleyerek '
                                  'takip etmek',
                          'is_correct': False,
                          'scenario_update': 'Vezikülü ve ateşi olmayan çocukta gereksiz karantina büyük panik ve okul '
                                             'kaybı doğurdu.',
                          'teaching_point': 'Suçiçeğinde kaşıntılı içi su dolu veziküller ve ateş olur; tek tük anüler '
                                            'halka lezyonlar olmaz.'},
                         {'text': 'Mantar enfeksiyonunu önlemek amacıyla tüm vücut derisini çamaşır suyu ile '
                                  'fırçalamak',
                          'is_correct': False,
                          'scenario_update': 'Çamaşır suyu tüm ciltte derin kimyasal erozyon, nekroz ve şiddetli yanık '
                                             'acısı oluşturdu.',
                          'teaching_point': 'Kimyasal toksik maddeler cilde asla temas ettirilmez; epitel bariyerini '
                                            'yok eder.'}]},
            {'stage_title': 'Laboratuvar ve İleri İncelemeler',
             'question': 'Anüler lezyonun fungal kökenini klinik veya laboratuvarda doğrulamak için en uygun yaklaşım '
                         'hangisidir?',
             'options': [{'text': 'Lezyonun aktif kenarından kazıntı alarak potasyum hidroksit ile mikroskopta hif ve '
                                  'sporları aramak',
                          'is_correct': True,
                          'explanation': "Tanıyı kesinleştirmede altın standart kenar skuamlarından yapılan %10-20'lik "
                                         'KOH (potasyum hidroksit) preparatıdır. Mikroskopta dallanan septalı fungal '
                                         'hifler ve artrokonidyalar görülür. Wood ışığında da floresans bakılabilir.',
                          'new_finding': 'Lezyonun kabarık kenarından bistüri sırtıyla hafif kazıntı yapıldı. Yatak '
                                         'Başı KOH İncelemesi: Keratinositler eridikten sonra dallanma gösteren tipik '
                                         'şeffaf septalı hif yapıları ve zincir şeklinde sporlar mikroskop altında net '
                                         'olarak görüntülendi. Fungal dermatofit etkeni kesin olarak doğrulandı.'},
                         {'text': 'Tanıyı koymak için hastaya genel anestezi verip derin tam kat cerrahi kemik '
                                  'biyopsisi yapmak',
                          'is_correct': False,
                          'scenario_update': 'Yüzeyel cilt lezyonunda kemik biyopsisi yapılması osteomiyelit ve kırık '
                                             'riski doğurdu.',
                          'teaching_point': 'Dermatofitler sadece cansız stratum korneuma yerleşir; derin dokuya ve '
                                            'kemiğe inmez.'},
                         {'text': 'Kanda sistemik mantar yayılımı düşünerek acil intrakraniyal omurilik sıvısı '
                                  'incelemesi yapmak',
                          'is_correct': False,
                          'scenario_update': "Lokal cilt lezyonunda lomber ponksiyon yapılması steril BOS'ta travmatik "
                                             'kanamaya yol açtı.',
                          'teaching_point': 'Yüzeyel halka lezyonu lokalize bir tablodur; sistemik menenjit yapmaz.'},
                         {'text': 'Halka lezyonunu araştırmak için hastaya tüm vücut pozitron emisyon tomografisi '
                                  'çektirmek',
                          'is_correct': False,
                          'scenario_update': 'Lokal mantar lezyonunda çekilen PET/BT hastaya devasa maliyet ve '
                                             'gereksiz radyoaktif yük bindirdi.',
                          'teaching_point': 'Yüzeyel dermatofitlerde ileri nükleer tıp taramaları kesinlikle '
                                            'yapılmaz.'}]},
            {'stage_title': 'Klinik Ön Tanı ve Ayırıcı Tanı',
             'question': "Kedi teması olan, ortası soluk kenarları pullu anüler lezyonda ve KOH'ta hif saptanan "
                         'hastada tanınız nedir?',
             'options': [{'text': 'Tinea korporis vücut mantarı',
                          'is_correct': True,
                          'explanation': 'Kedi teması öyküsü, anüler halka şeklinde kenarı aktif lezyon ve '
                                         'mikroskopide septalı hifler tinea korporis (vücut mantarı) için tanı '
                                         'koydurucudur.',
                          'new_finding': 'Kesin Tanı: Tinea Korporis doğrulanmıştır. Topikal antifungal tedaviye '
                                         'geçildi.'},
                         {'text': 'Eritema migrans lyme hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Eritema migrans kene ısırığı sonrası olur; lezyonun kenarında kepeklenme '
                                             'veya pütür olmaz, düz eritemdir.',
                          'teaching_point': 'Eritema migransta skuam (kepek) olmaz; tinea lezyonlarının kenarı ise '
                                            'tipik olarak kepeklidir.'},
                         {'text': 'Granüloma anülare lezyonu',
                          'is_correct': False,
                          'scenario_update': 'Granüloma anülarede lezyon dermal papüllerden oluşur, yüzeyinde asla '
                                             'skuam veya kepek bulunmaz.',
                          'teaching_point': 'Granüloma anülare dermistedir, skuam içermez ve KOH incelemesi '
                                            'negatiftir.'},
                         {'text': 'Pitriyazis rozea madalyon plağı',
                          'is_correct': False,
                          'scenario_update': 'Madalyon plağı içe bakan yakalık tarzı kepeğe sahiptir ve KOH '
                                             'incelemesinde hif görülmez.',
                          'teaching_point': 'Pitriyazis rozeada KOH incelemesi negatiftir; fungal hif görülmesi tinea '
                                            'tanısını kesinleştirir.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Tinea korporis tanısı kesinleşen bu çocuğun Yeşil Alandaki en uygun tedavisi ve kaçınılması '
                         'gereken ilaç nedir?',
             'options': [{'text': 'Topikal terbinafin krem uygulamak, kortizonlu kremlerden kesinlikle kaçınmak ve '
                                  'kediyi veteriner hekime götürmek',
                          'is_correct': True,
                          'explanation': 'İlk basamak tedavi topikal antifungaldir (Terbinafin %1 veya '
                                         'Klotrimazol/Mikonazol krem günde 1-2 kez, 2-3 hafta). Lezyon kaybolduktan '
                                         'sonra nüksü önlemek için 1 hafta daha devam edilir. Kortizonlu kremler '
                                         'KESİNLİKLE KONTRENDİKEDİR (Tinea incognito yapar). Kedinin veterinerde '
                                         'tedavisi şarttır.',
                          'new_finding': 'Topikal terbinafin başlandı, kortizonlu kremler derhal kestirildi. Evdeki '
                                         'yavru kedi veterinere götürüldü. İki hafta sonra kontrolde halka lezyonların '
                                         'tamamen solduğu, kepeklenmenin kaybolduğu ve cildin tamamen iyileştiği '
                                         'görüldü.'},
                         {'text': 'Lezyonun üzerine günde dört kez en güçlü florlu kortizonlu merhem sürerek deriyi '
                                  'inceltmek',
                          'is_correct': False,
                          'scenario_update': 'Güçlü kortizon mantar florasını patlatarak lezyonu tüm gövdeye yaydı ve '
                                             'tinea incognito oluşturdu.',
                          'teaching_point': 'Fungal enfeksiyonlara steroid sürülmesi mantarı besler; tinea tedavisinde '
                                            'steroid kesinlikle yasaktır.'},
                         {'text': 'Mantar sporlarını yok etmek için çocuğa bir ay boyunca aralıksız yüksek doz '
                                  'sefalosporin içirmek',
                          'is_correct': False,
                          'scenario_update': 'Bakteriyel antibiyotik mantara hiç etki etmedi ve çocukta antibiyotik '
                                             'ishali başlattı.',
                          'teaching_point': 'Antibiyotikler mantarlara etki etmez; aksine florayı bozarak fungal '
                                            'çoğalmayı kolaylaştırır.'},
                         {'text': 'Halkayı çıkarmak amacıyla lezyonlu bölgeyi kızgın demirle dağlayarak koterize etmek',
                          'is_correct': False,
                          'scenario_update': 'Kızgın demir kolda derin üçüncü derece termal yanık ve hipertrofik '
                                             'keloid skarı bıraktı.',
                          'teaching_point': 'Yüzeyel mikozlar basit topikal kremlerle tamamen iyileşir; travmatik '
                                            'uygulamalar kabul edilemez.'}]}]}]
