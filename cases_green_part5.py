# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Yeşil Alan Vakaları (Part 5: G41 - G50)
Odak: Bulantı, Kusma, Karın Ağrısı, İshal (GİS Acilleri - Yeşil Alan Ayaktan Yönetim)
Kılavuzlar: ESPGHAN, AAP, NASPGHAN, NICE
"""

GREEN_CASES_PART5 = [ { 'age': '2 Yaşında',
    'case_pearl': 'ESPGHAN ve AAP kılavuzlarına göre çocukluk çağı akut viral gastroenteritlerinde rutin antibiyotik, '
                  'antidiyareik (loperamid vb.) veya antispazmodiklerin yeri yoktur. Hafif dehidratasyonda temel '
                  'yaklaşım her sulu dışkı sonrası 10 mL/kg ORS verilmesi ve yaşa uygun normal beslenmenin kesilmeden '
                  'sürdürülmesidir.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Dün başlayan sulu ishal, günde 5-6 kez dışkılama ve hafif ateş',
    'disposition': 'Yeşil Alandan Oral Rehidratasyon Sıvısı (ORS) Eğitimi ve Beslenme Önerileri ile Ayaktan Taburculuk',
    'final_diagnosis': 'Akut Viral Gastroenterit (Hafif Dehidratasyon - ESPGHAN Evre 1)',
    'gender': 'Erkek',
    'history': "Annesi anlatıyor: 'Dün sabah kreşten geldikten sonra sulu, mukussuz, kansız dışkılamaya başladı. Ateşi "
               'evde 37.8°C ölçüldü. Dün iki kez kustu ama bugün kusması yok. Ağızdan su ve çorba içebiliyor, idrarını '
               'bezine 3-4 kez yaptı, ağlarken gözyaşı bol. Kreşteki birkaç arkadaşında da benzer ishal salgını '
               "varmış.'",
    'id': 'G41',
    'steps': [ { 'options': [ { 'explanation': 'Akut gastroenteritli çocukta klinik dehidratasyon skalası (gözyaşı, '
                                               'mukoza nemliliği, deri turgoru, KDZ ve kilo kaybı) tedavi planının '
                                               '(oral vs. IV) temel belirleyicisidir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.5°C, KTA 110/dk, SS 24/dk, SpO2 %99, TA 92/58 '
                                               'mmHg, KDZ 1.5 sn. Genel durumu iyi, aktif, çevreyle ilgili. Göz '
                                               'küreleri normal, ağlarken gözyaşı bol, ağız mukozası hafif nemli, deri '
                                               'turgoru anında geri dönüyor. Karın rahat, defans veya rebound yok, '
                                               'bağırsak sesleri normoaktif.',
                                'text': 'Genel görünüm, mukoza nemliliği, gözyaşı varlığı, kapiller dolum zamanı ve '
                                        'deri turgorunu değerlendirip tartı almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Oral alabilen, gözyaşı olan ve şok bulgusu taşımayan çocukta '
                                                   'gereksiz damar yolu açılması ajitasyona yol açtı.',
                                'teaching_point': 'Oral alabilen ve hafif dehidrate çocuklarda IV hidrasyon değil, '
                                                  'öncelikle Oral Rehidratasyon Sıvısı (ORS) endikedir.',
                                'text': 'İshal sayısı beşi aştığı için fizik muayeneden önce derhal damar yolu açıp '
                                        'izotonik sıvı infüzyonu başlatmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Kansız ve mukussuz akut sulu ishalde ampirik antibiyotik '
                                                   'başlanması bağırsak mikrobiyotasını bozarak ishali uzattı.',
                                'teaching_point': "Kreş ilişkili akut sulu ishallerin %80'den fazlası viral "
                                                  'kaynaklıdır. Kansız ishalde rutin antibiyotik verilmez.',
                                'text': 'Kreş salgını olması nedeniyle gaitada amip ve parazit taraması çıkana kadar '
                                        'ampirik oral sefiksim başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Grafide sadece non-spesifik gaz dağılımı izlendi; çocuk gereksiz '
                                                   'iyonizan radyasyona maruz kaldı.',
                                'teaching_point': 'Akut gastroenteritte batın grafisi endikasyonu yoktur; sadece '
                                                  'obstrüksiyon veya perforasyon şüphesinde istenir.',
                                'text': 'Karın ağrısı tariflenmese bile ishale bağlı perforasyon riskini dışlamak için '
                                        'acil ayakta direkt batın grafisi çekmek'}],
                 'question': 'Bu hastada dehidratasyon derecesini ve klinik stabiliteyi değerlendirmek için en uygun '
                             'ilk yaklaşım hangisidir?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'ESPGHAN kılavuzlarına göre hafif dehidratasyonlu, oral hidrasyona '
                                               'uyumlu ve kanlı dışkısı olmayan çocuklarda rutin biyokimya, hemogram '
                                               'veya gaita tetkiki gerekmez; klinik tanı yeterlidir.',
                                'is_correct': True,
                                'new_finding': 'Gereksiz kan alımından kaçınıldı. Anneye ORS hazırlama ve uygulama '
                                               'protokolü açıklandı.',
                                'text': 'Oral alımı iyi olan hafif dehidrate hastada rutin kan tahlili veya dışkı '
                                        'kültürü istemeden takip planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Alınan kan tetkiklerinde sodyum 138 mEq/L, potasyum 4.2 mEq/L, üre '
                                                   've kreatinin tamamen normal sınırlarda geldi.',
                                'teaching_point': 'Oral hidrasyonu tolere eden hafif dehidratasyonlu çocuklarda rutin '
                                                  'venöz kan tetkiki endike değildir.',
                                'text': 'Elektrolit bozukluğu olasılığına karşı tam biyokimya, kan gazı, hemogram ve '
                                        'gaitada viral antijen paneli istemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Dışkı mikroskopisinde eritrosit veya lökosit saptanmadı; tedavi '
                                                   'stratejisinde bir değişiklik olmadı.',
                                'teaching_point': 'Makroskopik olarak sulu ve kansız olan tipik viral ishallerde gaita '
                                                  'mikroskopisi klinik karar sürecini değiştirmez.',
                                'text': 'Dışkıda gizli kan ve lökosit varlığını doğrulamak amacıyla acil mikroskopik '
                                        'gaita incelemesi tetkiklerini istemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Amilaz ve lipaz normal sınırlarda geldi; çocuğun kolunda kan '
                                                   'alımına bağlı hematom oluştu.',
                                'teaching_point': 'Tipik gastroenterit seyriyle uyumlu hafif kusmalarda pankreas '
                                                  'enzimi bakılması aşırı tetkiktir.',
                                'text': 'Kusma öyküsü bulunduğu için serum amilaz ve lipaz düzeylerini kontrol ederek '
                                        'akut pankreatit tablosunu dışlamak'}],
                 'question': 'Genel durumu iyi, hafif dehidrate ve kusması olmayan bu 2 yaşındaki hastada hangi '
                             'tetkikler planlanmalıdır?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Sulu mukussuz ishal, hafif ateş, kreş salgını ve iyi genel durum akut '
                                               'viral gastroenterit ile tipiktir.',
                                'is_correct': True,
                                'new_finding': 'Klinik Tanı: Akut Viral Gastroenterit (Hafif Dehidratasyon).',
                                'text': 'Akut viral gastroenterit enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Dizanteride yüksek ateş, toksik görünüm, tenesmus ve kanlı mukuslu '
                                                   'dışkı beklenir; bu çocukta yoktur.',
                                'teaching_point': 'Kansız ve sulu kreş ishalleri viral kaynaklıdır; invaziv bakteriyel '
                                                  'kolit bulgusu taşımaz.',
                                'text': 'Akut bakteriyel dizanteri tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'İBH kronik kilo kaybı, anemi ve haftalar süren kanlı ishal yapar; '
                                                   'akut 1 günlük tabloda düşünülmez.',
                                'teaching_point': 'Bir günlük akut ishalde kronik inflamatuar bağırsak hastalığı '
                                                  'düşünülmez.',
                                'text': 'Kronik inflamatuar bağırsak hastalığı'},
                              { 'is_correct': False,
                                'scenario_update': 'Giardia haftalarca süren kötü kokulu yağlı ishal, gaz ve kilo '
                                                   'kaybı yapar; akut başlangıçlı değildir.',
                                'teaching_point': 'Giardia subakut ve kronik seyreder; 24 saatlik akut sulu kreş '
                                                  'salgınında ilk etken virüslerdir.',
                                'text': 'Giardiazis paraziter malabsorpsiyon sendromu'}],
                 'question': 'Kreş teması, hafif ateş, kansız sulu ishal ve hafif dehidratasyon ile en olası klinik '
                             'tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Her sulu gaita sonrası 10 mL/kg ORS kayıpları yerine koyar. Laktozsuz '
                                               'veya aç bırakıcı diyet önerilmez; erken enteral beslenme bağırsak '
                                               'enterositlerinin rejenerasyonunu hızlandırır.',
                                'is_correct': True,
                                'new_finding': "Çocuk acil serviste 100 mL ORS'yi istekle içti, kusmadı. Anneye 24 "
                                               'saatte idrar çıkışı olmaması, sürekli uyku hali, safralı kusma veya '
                                               'kanlı dışkı durumunda acile dönüş anlatıldı.',
                                'text': 'Her sulu dışkı sonrası on mililitre kilogram oral rehidratasyon sıvısı '
                                        'verilmesi ve yaşa uygun beslenmenin sürdürülmesi'},
                              { 'is_correct': False,
                                'scenario_update': 'Loperamid kullanımı sonrası çocukta paralitik ileus, batın '
                                                   'distansiyonu ve letarji gelişti.',
                                'teaching_point': 'Loperamid ve motilite azaltıcı ajanlar çocuklarda toksik megakolon '
                                                  've ölümcül yan etkiler nedeniyle KONTRENDİKEDİR.',
                                'text': 'İshali hemen durdurmak için loperamid şurup ve bağırsak spazmı için '
                                        'antispazmodik damla reçete ederek göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Katı gıdaların kesilmesi çocuğun enerji açığını artırdı, dışkı '
                                                   'toparlanması gecikti.',
                                'teaching_point': 'Aç bırakma hipoglisemiye yol açar ve villus atrofisini artırır. '
                                                  'Normal beslenme derhal sürdürülmelidir.',
                                'text': 'Bağırsakları dinlendirmek amacıyla ilk yirmi dört saat katı gıdaları tamamen '
                                        'kesip sadece pirinç suyu içirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Antiprotozoal ve antibiyotik ilaç ishal süresini kısaltmadı; çocuk '
                                                   'ilacın tadı nedeniyle ağızdan alımı reddetti.',
                                'teaching_point': 'Kanıtlanmış amip veya Giardia olmadan akut sulu ishalde ampirik '
                                                  'metronidazol verilmez.',
                                'text': 'Oral rehidratasyon yerine ampirik metronidazol şurup ve geniş spektrumlu '
                                        'florokinolon başlayarak hastayı taburcu etmek'}],
                 'question': 'Bu hastanın taburculuğunda aileye verilecek en uygun tedavi ve beslenme reçetesi '
                             'hangisidir?',
                 'stage_title': 'Tedavi Yönetimi ve Taburculuk Planı'}]},
  { 'age': '6 Yaşında',
    'case_pearl': 'Gıda alımından sonraki 1-6 saat içinde gelişen hiperakut bulantı ve inatçı kusma tablolarında '
                  'önceden oluşmuş bakteriyel enterotoksinler (özellikle Staphylococcus aureus veya Bacillus cereus '
                  'emetik toksini) düşünülmelidir. Ateş genellikle yoktur; tablo toksin aracılıdır. Akut '
                  'gastroenterit/gastrit ilişkili inatçı kusmalarda tek doz oral ondansetron (0.15 mg/kg) oral '
                  'rehidratasyon başarısını anlamlı derecede artırır ve IV sıvı ihtiyacını azaltır.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Dışarıda pasta ve mayonezli tavuk yedikten 3 saat sonra başlayan ani şiddetli kusma ve kramp tarzı '
                 'karın ağrısı',
    'disposition': 'Yeşil Alanda Tek Doz Oral Ondansetron + ORS ile Rehidrasyon ve Ayaktan Taburculuk',
    'final_diagnosis': 'Besin Zehirlenmesi (Stafilokoksik Enterotoksin Kaynaklı Akut Gastrit)',
    'gender': 'Kız',
    'history': "Altı yaşındaki kız çocuğu ailesi tarafından Yeşil Alana getiriliyor: 'Yaklaşık 3 saat önce bir doğum "
               'günü partisinde kremalı pasta ve tavuklu sandviç yedi. Eve geldikten hemen sonra aniden şiddetli '
               'bulantı ve fışkırır tarzda kusmaya başladı. Son 2 saatte 6 kez kustu, su bile içemiyor. Partideki 3 '
               "çocukta daha aynı saatlerde kusma başlamış. Ateşi yok, ishali henüz başlamamış.'",
    'id': 'G42',
    'steps': [ { 'options': [ { 'explanation': '1-6 saatlik kısa inkübasyon süresi preforme toksinleri gösterir. Batın '
                                               'muayenesinde apandisit gibi cerrahi aciller dışlanmalı ve hidrasyon '
                                               'durumu incelenmelidir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 104/dk, SS 20/dk, SpO2 %99, TA 98/62 '
                                               'mmHg, KDZ 1.5 sn. Genel durumu iyi-orta, bulantı nedeniyle halsiz. '
                                               'Batın rahat, epigastriumda hafif hassasiyet var; defans, rebound yok. '
                                               'Ağız mukozası hafif kuru, gözyaşı mevcut, çevreyle koopere.',
                                'text': 'Besin öyküsünü, inkübasyon süresini sorgulamak, batın muayenesinde akut '
                                        'cerrahiyi dışlamak ve dehidratasyonu değerlendirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Muayenesiz cerrahiye yönlendirilen hastada gereksiz ameliyathane '
                                                   'paniği oluştu.',
                                'teaching_point': 'Kısa inkübasyonlu besin zehirlenmesinde batın rahattır; cerrahi '
                                                  'akut batın değildir.',
                                'text': 'Akut batın kabul ederek fizik muayene yapmadan hastayı derhal acil '
                                        'ameliyathaneye cerrahi eksplorasyona göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Metoklopramid sonrası çocukta akut distoni, okulojirik kriz ve '
                                                   'boyunda istemsiz kasılmalar gelişti.',
                                'teaching_point': 'Çocuklarda metoklopramid ekstrapiramidal yan etkiler nedeniyle '
                                                  'önerilmez; ilk tercih ondansetrondur.',
                                'text': 'Kusmayı durdurmak amacıyla hastaya intramüsküler yüksek doz metoklopramid '
                                        'enjeksiyonu yaparak taburcu etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Süt içirilen çocuk anında masif şekilde kustu ve içeriği aspire '
                                                   'etme tehlikesi yaşadı.',
                                'teaching_point': 'Aktif kusan çocuğa süt gibi ağır besinler verilmez; aspirasyon '
                                                  'riski doğurur.',
                                'text': 'Kusan çocuğa acil serviste zorla bir litre soğuk süt içirerek mide asidini '
                                        'nötralize etmeye çalışmak'}],
                 'question': 'Besin alımından 3 saat sonra ani kusma ile başvuran bu çocukta ilk klinik değerlendirme '
                             'nasıl olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'Tipik kısa inkübasyonlu besin zehirlenmesinde rutin biyokimya veya '
                                               'radyoloji endike değildir; klinik tanı yeterlidir.',
                                'is_correct': True,
                                'new_finding': 'Gereksiz invaziv girişim yapılmadı. Çocuğun hidrasyonu ve oral '
                                               'toleransı izlendi.',
                                'text': 'Tipik klinik öyküsü olan bu hastada gereksiz kan tahlili veya batın grafisi '
                                        'istemeden semptomatik izlem planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tomografi ve tetkikler normal geldi; çocuk gereksiz iyonizan '
                                                   'radyasyon aldı.',
                                'teaching_point': 'Besin zehirlenmesinde tomografi ve rutin kan tetkiklerinin yeri '
                                                  'yoktur.',
                                'text': 'Toksini kanda saptamak amacıyla hastadan kan kültürü, tam biyokimya ve '
                                        'kontrastlı batın tomografisi çekmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Preforme toksin tablosunda antibiyotik verilmesi fayda sağlamadı; '
                                                   'ek yan etki riski doğurdu.',
                                'teaching_point': 'Stafilokoksik besin zehirlenmesi toksin aracılıdır; canlı bakteri '
                                                  'invazyonu olmadığından antibiyotik etkisizdir.',
                                'text': 'Mide içeriğindeki bakterileri öldürmek için hiçbir tahlil yapmadan intravenöz '
                                        'yüksek doz siprofloksasin başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Anestezi gazı hastada derin hipoventilasyon ve laringospazma yol '
                                                   'açtı.',
                                'teaching_point': 'Kusma tedavisinde anestezi gazları kullanılmaz; kanıta dayalı '
                                                  'antiemetikler uygulanır.',
                                'text': 'Kusma refleksini tamamen felç etmek amacıyla hastaya yüksek doz genel '
                                        'anestezi gazı koklatmak'}],
                 'question': 'Besin zehirlenmesi kliniği olan, genel durumu stabil bu çocukta tetkik yaklaşımı nasıl '
                             'olmalıdır?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Kremalı/tavuklu besin alımından 1-6 saat sonra başlayan afebril kusma '
                                               'fırtınası S. aureus enterotoksini ile uyumludur.',
                                'is_correct': True,
                                'new_finding': 'Klinik Tanı: Preforme Toksin Kaynaklı Besin Zehirlenmesi '
                                               '(Staphylococcus aureus enterotoksini).',
                                'text': 'Stafilokoksik besin zehirlenmesi tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Apandisitte peritonit defansı ve lökositoz olur; aynı anda birden '
                                                   'çok çocukta gıda sonrası hiperakut kusma yapmaz.',
                                'teaching_point': 'Toplu besin zehirlenmesi salgınları cerrahi akut batın ile '
                                                  'karıştırılmamalıdır.',
                                'text': 'Akut apandisit perforasyonu atağı'},
                              { 'is_correct': False,
                                'scenario_update': 'Rotavirüs inkübasyonu 24-48 saattir; besinden 3 saat sonra aniden '
                                                   'gelişen toksin tablosuyla uyumsuzdur.',
                                'teaching_point': 'Viral gastroenteritlerin inkübasyon süresi en az 12-48 saattir; 3 '
                                                  'saatlik başlangıç toksin lehindedir.',
                                'text': 'Rotavirüs gastroenterit enfeksiyonu salgını'},
                              { 'is_correct': False,
                                'scenario_update': 'İnvajinasyonda aralıklı kolik krizleri ve çilek jölesi gaita olur; '
                                                   'gıda ilişkili çoklu kusma yapmaz.',
                                'teaching_point': 'İnvajinasyon 6 yaş grubunda nadirdir ve besin zehirlenmesi '
                                                  'epidemiyolojisi göstermez.',
                                'text': 'İntestinal invajinasyon tıkanıklığı anomalisi'}],
                 'question': 'Partide kremalı pasta tüketimi sonrası 3. saatte başlayan kusma ve çoklu olgu öyküsüyle '
                             'en olası tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'AAP ve ESPGHAN kılavuzlarına göre akut gastroenterit ve besin '
                                               'zehirlenmesinde tek doz oral ondansetron (6 yaş/20 kg için 4 mg oral) '
                                               'kusmayı başarıyla durdurur ve oral toleransı sağlar.',
                                'is_correct': True,
                                'new_finding': '4 mg oral parçalanan ondansetron tableti verildi. 30 dakika sonra '
                                               "çocuk kusmadı, 150 mL ORS'yi istekle içti. Kusması tekrarlamayan hasta "
                                               'ayaktan önerilerle taburcu edildi.',
                                'text': 'Kilo uygun tek doz oral ondansetron verip otuz dakika sonra yavaş yudumlarla '
                                        'oral rehidratasyon sıvısı başlatmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Uzun süreli açlık hastada ketotik hipoglisemiye ve halsizliğin '
                                                   'derinleşmesine yol açtı.',
                                'teaching_point': 'Kusma kontrol altına alındıktan sonra erken rehidrasyon ve beslenme '
                                                  'esastır; uzun süreli açlık zararlıdır.',
                                'text': 'Kusma devam ettiği sürece hastayı kırk sekiz saat boyunca acilde hiçbir besin '
                                        'vermeden aç bekletmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Çamaşır sodası içirilen çocukta ağız mukozasında kimyasal alkali '
                                                   'yanık ve kusma spazmı gelişti.',
                                'teaching_point': 'Toksin aracılı besin zehirlenmesinde aşındırıcı ev kimyasalları '
                                                  'verilmesi ölümcül zehirlenmelere neden olur.',
                                'text': 'Toksinleri bağlamak amacıyla hastaya oral yoldan yoğun çamaşır sodası ve '
                                        'aktif kömür karışımı içirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz antibiyotik çocuğun bağırsak florasını tahrip ederek '
                                                   'sekonder ishal başlattı.',
                                'teaching_point': 'Stafilokoksik besin zehirlenmesinde antibiyotiklerin yeri yoktur; '
                                                  'self-limit bir klinik tablodur.',
                                'text': 'Hastaya acil şartlarda geniş spektrumlu aminoglikozid ampulünü ağızdan '
                                        'içirerek bağırsak florasını tamamen sıfırlamak'}],
                 'question': 'Bu çocukta kusmayı kontrol altına almak ve hidrasyonu sağlamak için en uygun tedavi '
                             'yaklaşımı hangisidir?',
                 'stage_title': 'Tedavi Yönetimi ve Taburculuk Planı'}]},
  { 'age': '5 Yaşında',
    'case_pearl': 'Pediatrik fonksiyonel kabızlıkta rektumda biriken sert fekal kitle (fekal impaksiyon) duyusal '
                  'adaptasyon yaratarak dışkılama hissini köreltir. Sert kitlenin etrafından sızan sıvı dışkı çamaşırı '
                  "kirletir (enkoprezis / taşma ishali / overflow). Bu tablo sıklıkla yanlışlıkla 'kronik ishal' "
                  'sanılarak antidiyareik başlanması faciasına yol açar! NASPGHAN/ESPGHAN kılavuzlarına göre ilk adım '
                  'disimpaksiyondur: Yüksek doz oral Polietilen Glikol (PEG 3350, 1-1.5 g/kg/gün, 3-6 gün). Ardından '
                  'en az 2 ay idame laksatif tedavisi (PEG 0.4 g/kg/gün) ve tuvalet eğitimi sürdürülmelidir.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Çamaşırında sürekli çamur gibi dışkı kaçırma, karnında şişlik ve sert dışkılama korkusu',
    'disposition': 'Yeşil Alandan Oral Polietilen Glikol (PEG 3350) Disimpaksiyon Protokolü ve Tuvalet Eğitimi ile '
                   'Taburculuk',
    'final_diagnosis': 'Fonksiyonel Kabızlık, Fekal İmpaksiyon ve Enkoprezis (Taşma İshali / Overflow İnkontinans)',
    'gender': 'Erkek',
    'history': "Beş yaşındaki erkek çocuğu annesi tarafından getiriliyor: 'Yaklaşık 1 aydır külodunu kirletiyor, ishal "
               'gibi çamur kıvamında lekeleniyor. Ama haftada sadece 1 kez taş gibi, kalın dışkı yapıyor. Tuvalete '
               'oturmak istemiyor, bacaklarını çaprazlayıp parmak ucunda yürüyerek kakasını tutuyor. Karın ağrısı ve '
               "şişkinliği oluyor, iştahı azaldı.'",
    'id': 'G43',
    'steps': [ { 'options': [ { 'explanation': 'Sol alt kadranda sert fekaloid kitle (fekaloma), anal fissür ve spina '
                                               'bifida okülta gibi spinal disrafizm bulgularının taranması fizik '
                                               'muayenenin temel taşıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 94/dk, SS 20/dk, SpO2 %99, TA 96/60 '
                                               'mmHg. Batın muayenesinde sol alt kadranda sigmoide uyan alanda sert, '
                                               'hareketli, silindirik dışkı kitlesi palpe edildi. Lumbosakral omurga '
                                               'doğal, gamze veya kıl yumağı yok. Perianal muayenede sfinkter tonusu '
                                               'doğal, hafif anal kızarıklık mevcut.',
                                'text': 'Batın palpasyonunda sol alt kadrandaki sert fekal kitleyi, perianal bölgeyi '
                                        've omurga anomalilerini sistemik incelemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Metronidazol verilmesi kabızlığı daha da ağırlaştırarak fekal '
                                                   'impaksiyonu taşlaşmış kitleye çevirdi.',
                                'teaching_point': 'Enkoprezis bir enfeksiyon değildir; sert fekal kitlenin etrafından '
                                                  'sızan taşma dışkısıdır.',
                                'text': 'Çamaşır lekelenmesini enfeksiyöz amip dizanterisi kabul edip fizik muayene '
                                        'yapmadan oral metronidazol başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Cerrahi ekip batında sadece dolgun kolon palpe ederek hastayı '
                                                   'tekrar polikliniğe yönlendirdi.',
                                'teaching_point': 'Kronik kabızlık ve enkoprezis akut apandisit değildir; sol alt '
                                                  'kadranda fekal kitle palpe edilir.',
                                'text': 'Karnı şiş olan hastada akut apandisit perforasyonu düşünerek hiçbir palpasyon '
                                        'yapmadan cerrahiye devretmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Ailenin cezalandırıcı tutumu çocuğun dışkı tutma davranışını daha '
                                                   'da pekiştirdi ve psikolojik travma yarattı.',
                                'teaching_point': 'Enkoprezis istem dışı sızıntıdır; suçlayıcı yaklaşım çocuğun dışkı '
                                                  'tutma korkusunu derinleştirir.',
                                'text': 'Hastanın çamaşır kirletmesini şımarıklık olarak niteleyip aileye çocuğu '
                                        'azarlamasını önererek taburcu etmek'}],
                 'question': 'Çamaşır kirletme ve karın ağrısı yakınması olan bu çocukta ilk fizik muayene '
                             'yaklaşımınız ne olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'NASPGHAN ve ESPGHAN kılavuzlarına göre fonksiyonel kabızlık ve fekal '
                                               'impaksiyonda rutin ayakta batın grafisi veya kolonoskopi önerilmez; '
                                               'fizik muayenede kitlenin palpe edilmesi tanı için yeterlidir.',
                                'is_correct': True,
                                'new_finding': 'Gereksiz radyasyondan kaçınıldı. Fekal impaksiyon için oral '
                                               'disimpaksiyon protokolü planlandı.',
                                'text': 'Klinik muayene ile fekal impaksiyon tanısı kesinleştiğinden hastayı gereksiz '
                                        'radyolojik tetkik yapmadan tedaviye almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tomografi sadece fekal içeriği gösterdi; 5 yaşındaki çocuk '
                                                   'gereksiz iyonizan radyasyon aldı.',
                                'teaching_point': 'Basit kabızlık ve impaksiyonda bilgisayarlı tomografi kesinlikle '
                                                  'endike değildir.',
                                'text': 'Fekal kitlenin sertliğini ölçmek amacıyla hastaya acil koşullarda kontrastlı '
                                        'tüm batın tomografisi çekmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gaita testleri tamamen normal geldi; hastanın disimpaksiyon '
                                                   'tedavisi saatlerce gecikti.',
                                'teaching_point': 'Taşma dışkılamasında mikrobiyolojik gaita tetkiklerinin hiçbir '
                                                  'tanısal değeri yoktur.',
                                'text': 'Taşma ishalini araştırmak için genişletilmiş viral ve bakteriyel gaita kültür '
                                        'panellerini acil serviste istemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Rektal biyopsi hazırlığı hastanede yatış süresini uzattı ve '
                                                   'çocukta gereksiz cerrahi kaygı yarattı.',
                                'teaching_point': 'Hirschsprung kırmızı bayrakları (mekonyum gecikmesi vb.) olmayan 5 '
                                                  'yaşındaki çocukta erken biyopsi gerekmez.',
                                'text': 'Herhangi bir tedavi vermeden önce hastaya genel anestezi altında tanısal '
                                        'rektal emme biyopsisi planlamak'}],
                 'question': 'Fizik muayenede sol alt kadranda fekal kitle saptanan bu stabil hastada hangi tetkikler '
                             'planlanmalıdır?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Haftada bir sert dışkılama, dışkı tutma davranışı, çamaşır kirletme ve '
                                               'palpe edilen fekaloid kitle enkoprezisli fonksiyonel kabızlıktır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Fonksiyonel Kabızlık, Fekal İmpaksiyon ve Taşma İshali '
                                               '(Enkoprezis).',
                                'text': 'Fekal impaksiyon ve enkoprezis tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Amipli dizanteride sol kadranda haftalık sert dışkı kütlesi palpe '
                                                   'edilmez; kramp ve kanlı dışkı olur.',
                                'teaching_point': 'Taşma lekelenmesi gerçek ishal değildir; rektal tıkaç etrafından '
                                                  'sızan fekal sıvıdır.',
                                'text': 'Akut enfeksiyöz amip gastroenteriti'},
                              { 'is_correct': False,
                                'scenario_update': 'Hirschsprung hastalığında enkoprezis (taşma kaçırması) görülmez '
                                                   'çünkü aganglionik rektum boştur ve sfinkter gevşeyemez.',
                                'teaching_point': 'Enkoprezis fonksiyonel kabızlığa özgüdür; Hirschsprung hastalığında '
                                                  'rektal ampulla boş olup enkoprezis beklenmez.',
                                'text': 'Klasik konjenital megakolon hastalığı'},
                              { 'is_correct': False,
                                'scenario_update': 'Çölyakta kronik yağlı ishal ve büyüme geriliği olur; sol alt '
                                                   'kadranda sert fekal taşlaşma görülmez.',
                                'teaching_point': 'Çölyak hastalığı malabsorptif kronik ishal yapar; dışkı tutma '
                                                  'kaynaklı enkoprezis değildir.',
                                'text': 'Çölyak otoimmün malabsorpsiyon enteropatisi'}],
                 'question': 'Dışkı tutma manevraları, haftada bir sert dışkılama, taşma lekelenmesi ve sol kadranda '
                             'kitle ile kesin tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'ESPGHAN/NASPGHAN kılavuzlarına göre ilk adım oral PEG 3350 ile '
                                               'disimpaksiyondur (1-1.5 g/kg/gün, 3-6 gün). Tıkaç temizlendikten sonra '
                                               'relapsı önlemek için en az 2 ay idame laksatif (0.4 g/kg/gün) ve '
                                               'tuvalet eğitimi sürdürülmelidir.',
                                'is_correct': True,
                                'new_finding': 'Anneye PEG 3350 tozunun su veya meyve suyu ile hazırlanışı anlatıldı. '
                                               '3 gün içinde rektumdaki sert kitle ağrısız boşaldı; ardından idame '
                                               'doza geçildi. Çamaşır kirletmesi tamamen düzeldi.',
                                'text': 'Yüksek doz oral polietilen glikol ile üç ila altı günde disimpaksiyon '
                                        'sağlamak ve ardından idame tedaviye geçmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Tıkaç açılmadan verilen yüksek lif bağırsakta masif gaz ve '
                                                   'şiddetli kramp ağrılarına yol açtı.',
                                'teaching_point': 'Disimpaksiyon yapılmadan lif artırılması ağrıyı artırır; önce tıkaç '
                                                  'boşaltılmalı, sonra beslenme düzenlenmelidir.',
                                'text': 'İmpaksiyonu temizlemeden sadece günlük lif miktarını artırıp hastaya laksatif '
                                        'vermeden eve göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Tekrarlayan travmatik lavmanlar çocukta anal fissür ve derin '
                                                   'psikolojik fobiye neden oldu.',
                                'teaching_point': 'Rektal girişimler travmatiktir; disimpaksiyonda oral PEG ilk '
                                                  'tercihtir ve rektal lavmandan daha etkilidir.',
                                'text': 'Çocuğu her gün sabah akşam acil servise çağırarak üç ay boyunca invaziv '
                                        'rektal sabunlu lavman uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Loperamid verilmesi kolondaki sert kitleyi taşlaştırarak tam '
                                                   'mekanik bağırsak obstrüksiyonuna yol açtı.',
                                'teaching_point': 'Enkopreziste motilite azaltıcı verilmesi tam bağırsak tıkanıklığı '
                                                  'yaratır; KESİNLİKLE KONTRENDİKEDİR.',
                                'text': 'İshal gibi kaçırdığı için hastaya derhal yüksek doz loperamid ve bağırsak '
                                        'hareketlerini dondurucu şurup yazmak'}],
                 'question': 'Fekal impaksiyonu olan bu 5 yaşındaki hastada ilk basamak doğru tedavi protokolü '
                             'hangisidir?',
                 'stage_title': 'Tedavi Yönetimi ve Taburculuk Planı'}]},
  { 'age': '6 Haftalık',
    'case_pearl': 'İnfantil kolik klasik Wessel kriterleri ile tanımlanır: Sağlıklı ve iyi beslenen bir süt çocuğunda, '
                  'günde 3 saatten fazla süren, haftada en az 3 gün görülen ve en az 3 haftadır devam eden '
                  'açıklanamayan paroksizmal ağlama krizleridir. Genellikle yaşamın 2-3. haftasında başlar, 6. haftada '
                  'pik yapar ve 3-4. aylarda kendiliğinden düzelir. En kritik kural: Organik nedenler (korneal '
                  'abrazyon, saç turnikesi, fıtık inkarserasyonu, İYE, otit) MUTLAKA dışlanmalıdır. Rutin ilaç '
                  '(simetikon, antispazmodik) veya tetkik endike değildir. Sedatifler ve dicyclomine KONTRENDİKEDİR '
                  "(apne riski). Tedavi aileye güvence vermek, sallama/sarılma/beyaz gürültü (Karp'ın 5S yöntemi) ve "
                  'ebeveyn tükenmişliğini önlemektir.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Her akşam saatlerinde başlayan, saatlerce süren, susturulamayan şiddetli ağlama nöbetleri',
    'disposition': 'Yeşil Alandan Aileye Güvence Verilmesi, Yatıştırma Teknikleri (5S) Eğitimi ve Destekleyici '
                   'Yaklaşımla Taburculuk',
    'final_diagnosis': 'İnfantil Kolik (Wessel Kriterleri / Üçler Kuralı ile Uyumlu Paroksizmal Ağlama)',
    'gender': 'Kız',
    'history': "Altı haftalık kız bebek ailesi tarafından getiriliyor: 'Yaklaşık 3 haftadır her akşam saat 18:00 "
               'civarında başlıyor. Yüzü kızarıyor, bacaklarını karnına çekiyor, ellerini yumruk yapıp 3-4 saat '
               'durmaksızın çığlık atarak ağlıyor. Gaz çıkarınca biraz rahatlıyor gibi ama sonra tekrar başlıyor. Gün '
               'içinde gayet neşeli, emmesi çok iyi, kilo alımı mükemmel. Ateşi veya kusması hiç olmadı ama biz '
               "uykusuzluktan ve çaresizlikten tükendik.'",
    'id': 'G44',
    'steps': [ { 'options': [ { 'explanation': 'Ağlayan bebekte organik aciller (korneal abrazyon, saç/iplik '
                                               'turnikesi, inkarsere herni, otitis media, anal fissür) bebek tamamen '
                                               'soyularak dışlanmalıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.9°C, KTA 132/dk, SS 34/dk, SpO2 %99, Tartı: '
                                               'Doğum kilosuna göre günde 35 gram almış (mükemmel). Bebek tamamen '
                                               'soyuldu. Kornealar doğal, saç turnikesi yok. Kulak zarları bilateral '
                                               'doğal. Kasık kanalları serbest, fıtık saptanmadı. Batın rahat, '
                                               'organomegali yok. Nörolojik muayene ve tonus tamamen doğal.',
                                'text': 'Gözleri flöresein ile incelemek, parmaklarda saç turnikesi, kasıkta fıtık '
                                        'aramak ve tepeden tırnağa tam muayene yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Soyulmayan bebeğin ayak parmağındaki saç turnikesi atlandı ve '
                                                   'parmakta iskemik kangren riski oluştu.',
                                'teaching_point': 'Ağlayan her bebek tamamen soyulmalı; parmaklar, kornea ve kasıklar '
                                                  'organik odak açısından taranmalıdır.',
                                'text': 'Ağlamanın gazdan kaynaklandığı kesin olduğu için bebeği hiç soymadan doğrudan '
                                        'reçeteye gaz damlası yazmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Narkotik analjezik süt çocuğunda ağır solunum depresyonuna ve '
                                                   'entübasyon ihtiyacına yol açtı.',
                                'teaching_point': 'İnfantil kolikte narkotik veya sedatif ilaçlar KESİNLİKLE '
                                                  'KONTRENDİKEDİR; solunum durmasına yol açar.',
                                'text': 'Ağlamayı kesmek amacıyla bebeğe acil serviste intramüsküler yüksek doz '
                                        'narkotik analjezik enjeksiyonu uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz cerrahi girişime alınan bebekte hiçbir patoloji '
                                                   'bulunamadı ve cerrahi stres oluştu.',
                                'teaching_point': '6 haftalık bebekte apandisit son derece nadirdir; genel durumu iyi '
                                                  've kilo alımı normalse kolik düşünülür.',
                                'text': 'Karın ağrısını apandisit kabul ederek 6 haftalık bebeğe genel anestezi '
                                        'altında tanısal laparotomi planlamak'}],
                 'question': 'Akşamları saatlerce ağlayan 6 haftalık bu bebekte acil fizik muayene yaklaşımınız nasıl '
                             'olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'Wessel kriterlerini karşılayan, genel muayenesi ve büyümesi normal '
                                               'olan bebeklerde laboratuvar veya radyoloji tetkiklerinin yeri yoktur; '
                                               'gereksiz tetkik ailenin kaygısını artırır.',
                                'is_correct': True,
                                'new_finding': 'Gereksiz kan veya idrar alımından kaçınıldı. Aile ile güven verici '
                                               'iletişim kuruldu.',
                                'text': 'Klinik muayenede organik patoloji saptanmayan ve iyi kilo alan bu bebekte '
                                        'hiçbir laboratuvar tetkiki istememek'},
                              { 'is_correct': False,
                                'scenario_update': 'Tetkikler tamamen normal geldi; ancak kan alma esnasında bebeğin '
                                                   'ajitasyonu ve ağlaması katlandı.',
                                'teaching_point': 'Sağlıklı büyüyen kolikli bebekte aşırı tetkik yapılması ailenin '
                                                  "'bebeğim hasta' kaygısını besler.",
                                'text': 'Ağlama nedenini netleştirmek amacıyla tam biyokimya, kan gazı, idrar kültürü '
                                        've tüm batın ultrasonografisi çekmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz anestezi alan bebekte solunum depresyonu gelişti ve MR '
                                                   'tamamen normal sonuçlandı.',
                                'teaching_point': 'Fontaneli normal ve nörolojik muayenesi doğal bebekte intrakraniyal '
                                                  'görüntüleme endike değildir.',
                                'text': 'Kafa içi basınç artışını dışlamak amacıyla bebeğe kontrastlı beyin manyetik '
                                        'rezonans görüntülemesi planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tekrarlayan batın grafileri 6 haftalık bebeği yüksek kümülatif '
                                                   'radyasyona maruz bıraktı.',
                                'teaching_point': 'Kolik tanısında direkt grafinin yeri yoktur; bağırsaktaki '
                                                  'fizyolojik gazı görmek klinik kararı değiştirmez.',
                                'text': 'Bebeğin gazını radyolojik olarak göstermek amacıyla bebeğe her ağlama '
                                        'krizinde ayakta direkt batın grafisi çekmek'}],
                 'question': 'Fizik muayenesi tamamen doğal, büyüme gelişmesi mükemmel olan bu bebekte tetkik '
                             'kararınız ne olmalıdır?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Sağlıklı, iyi kilo alan 6 haftalık süt çocuğunda Wessel kriterlerini '
                                               'karşılayan akşam ağlama krizleri infantil koliktir.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: İnfantil Kolik (Wessel Kriterleri Pozitif).',
                                'text': 'Tipik infantil kolik tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Flöresein boyamasında korneada epitel defekti saptanmadı; abrazyon '
                                                   'dışlandı.',
                                'teaching_point': 'Korneal abrazyon sürekli ağlama yapar ve flöresein ile yeşil '
                                                  'boyanır; akşam saatleriyle sınırlı değildir.',
                                'text': 'Akut korneal abrazyon yaralanması'},
                              { 'is_correct': False,
                                'scenario_update': 'İnvajinasyonda safralı kusma, letarji ve çilek jölesi gaita olur; '
                                                   '6 haftalık iyi büyüyen bebekte beklenmez.',
                                'teaching_point': 'İnvajinasyon 3 aydan sonra sıktır ve safralı kusma/kanlı dışkıyla '
                                                  'seyreder; kolik ile karışmamalıdır.',
                                'text': 'İleokolik invajinasyon anomalisi'},
                              { 'is_correct': False,
                                'scenario_update': 'Sadece anne sütü alan, egzama veya kanlı dışkısı olmayan bebekte '
                                                   'izole akşam ağlaması besin alerjisi değildir.',
                                'teaching_point': 'Besin alerjisinde mukuslu/kanlı dışkı, kusma veya egzama beklenir; '
                                                  'izole kolik alerji göstergesi değildir.',
                                'text': 'Şiddetli inek sütü alerjisi'}],
                 'question': 'Haftada 3 günden fazla, akşamları günde 3 saatten uzun süren paroksizmal ağlama ve '
                             'normal muayene ile tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'En etkili yaklaşım aileyi sakinleştirmek, 3-4. ayda geçeceğini '
                                               'anlatmak ve yatıştırma tekniklerini (Swaddle/Kundak, Side/Yan '
                                               'pozisyon, Shush/Beyaz gürültü, Swing/Ritmik sallama, Suck/Emme) '
                                               'öğretmektir. Antispazmodikler apne riski nedeniyle kontrendikedir.',
                                'is_correct': True,
                                'new_finding': 'Aileye bebeğin tamamen sağlıklı olduğu anlatıldı. Ebeveynlerin '
                                               'dönüşümlü dinlenmesi ve beyaz gürültü kullanımı önerildi. Ailenin '
                                               'kaygısı azaldı, ilaçsız takip planıyla taburcu edildi.',
                                'text': 'Durumun selim ve geçici olduğunu anlatmak, Karp beş es yatıştırma '
                                        'tekniklerini öğretmek ve gereksiz ilaçtan kaçınmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Dicyclomine damla verilen 6 haftalık bebekte apne, nöbet ve koma '
                                                   'tablosu gelişti.',
                                'teaching_point': 'Dicyclomine süt çocuklarında apne ve ölüm riski nedeniyle '
                                                  'KESİNLİKLE KONTRENDİKEDİR (FDA kara kutu uyarısı).',
                                'text': 'Ağlamayı durdurmak için bebeğe günde üç kez dicyclomine veya fenobarbital '
                                        'damla başlayarak taburcu etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Anne sütünün kesilmesi bebeğin immün korumasını yok etti ve '
                                                   'kabızlığa yol açtı.',
                                'teaching_point': 'Kolik nedeniyle anne sütü asla kesilmemelidir; anne sütü en kolay '
                                                  'sindirilen besindir.',
                                'text': 'Anne sütünün gaz yaptığını söyleyerek emzirmeyi tamamen kestirip bebeğe soya '
                                        'bazlı mama başlatmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Bebeğin sarsılması sarsılmış bebek sendromuna ve subdural hematoma '
                                                   'yol açtı.',
                                'teaching_point': 'Bebekler asla sarsılmamalıdır (Shaken Baby Sendromu); aileye öfke '
                                                  'kontrolü eğitimi verilmelidir.',
                                'text': 'Bebeği her ağladığında susturmak için kuvvetlice sarsarak sakinleştirmeye '
                                        'çalışmasını aileye önermek'}],
                 'question': 'İnfantil kolik tanısı konulan bu bebeğin ailesine verilecek en uygun yönetim ve '
                             'taburculuk rehberliği hangisidir?',
                 'stage_title': 'Tedavi Yönetimi ve Taburculuk Planı'}]},
  { 'age': '2 Aylık',
    'case_pearl': 'Besin Proteini İlişkili Alerjik Proktokolit (FPIAP), anne sütüyle beslenen sağlıklı süt '
                  'çocuklarında en sık rektal kanama nedenidir. Klasik olarak yaşamın ilk 2-8. haftalarında '
                  'makroskopik olarak sağlıklı, iyi kilo alan bebeğin bezinde mukuslu dışkıda taze kan çizgileri ile '
                  'prezante olur. Sistemik bulgu, ateş veya anemi yoktur. Tanı kliniktir; endoskopi veya biyopsi '
                  'gerekmez. İlk basamak tedavi emziren annenin diyetinden tüm süt ve süt ürünlerinin (peynir, yoğurt, '
                  'tereyağı, kazein/peyniraltı suyu içeren paketli gıdalar) en az 2-4 hafta tamamen çıkarılmasıdır. '
                  'Kanama genellikle 48-72 saatte azalır ve 1-2 haftada tamamen kaybolur. Anneye kalsiyum desteği '
                  'verilmelidir.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Bezinde çizgi şeklinde taze kırmızı kan ve sümüksü mukus görülmesi',
    'disposition': 'Yeşil Alandan Anne Diyetinden İnek Sütü ve Süt Ürünlerinin Çıkarılması (Eliminasyon) ile '
                   'Taburculuk',
    'final_diagnosis': 'Besin Proteini İlişkili Alerjik Proktokolit (FPIAP - İnek Sütü Proteini Alerjisi)',
    'gender': 'Erkek',
    'history': "İki aylık sadece anne sütü alan erkek bebek annesi tarafından getiriliyor: 'Bezinde son birkaç gündür "
               'hardal sarısı dışkının içinde ince iplik şeklinde taze kırmızı kan çizgileri ve sümüksü mukus fark '
               'ettik. Bebeğimin ateşi, kusması veya karın şişliği yok. Emmesi gayet neşeli, kilo alımı persentilinde '
               "seyrediyor.'",
    'id': 'G45',
    'steps': [ { 'options': [ { 'explanation': 'Bebekte anal fissür, nekrotizan enterokolit veya invajinasyon gibi '
                                               'organik nedenler dışlanmalı, bebeğin genel sağlığı ve büyümesi '
                                               'değerlendirilmelidir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 124/dk, SS 28/dk, SpO2 %100, TA 84/52 '
                                               'mmHg. Genel durumu çok iyi, güleryüzlü, çevreyle ilgili. Batın '
                                               'yumuşak, organomegali veya kitle yok. Perianal inspeksiyonda çatlak, '
                                               'anal fissür veya hemoroid saptanmadı. Bezde mukuslu sarı gaita içinde '
                                               'kılcal taze kan çizgileri görüldü.',
                                'text': 'Genel durumu, hidrasyonu, batın rahatlığını kontrol edip perianal bölgede '
                                        'anal fissür olup olmadığını muayene etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Genel durumu mükemmel olan bebeğe yapılan gereksiz anestezi ve '
                                                   'cerrahi komplikasyon riski yarattı.',
                                'teaching_point': 'Genel durumu iyi, ateşi ve distansiyonu olmayan bebekte izole kan '
                                                  'çizgileri cerrahi akut batın değildir.',
                                'text': 'Rektal kanamayı cerrahi acil kabul edip bebeği derhal genel anestezi altında '
                                        'tanısal laparotomiye almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz antibiyotik bağırsak mikrobiyotasını tahrip ederek '
                                                   'bebeğin dışkısını sulandırdı.',
                                'teaching_point': 'Ateşsiz, sağlıklı büyüyen bebekte mukuslu taze kan enfeksiyon '
                                                  'değil, alerjik proktokolittir.',
                                'text': 'Kanlı bez gördüğü için hastaya fizik muayene yapmadan derhal geniş spektrumlu '
                                        'intravenöz antibiyotik başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Bez ve anüs muayenesi yapılmadığı için anal fissür veya diğer '
                                                   'rektal lezyonlar dışlanamadı.',
                                'teaching_point': 'Rektal kanamayla başvuran her bebekte perianal bölge ve dışkı '
                                                  'karakteri mutlaka doğrudan görülmelidir.',
                                'text': 'Kanamanın önemsiz olduğunu söyleyerek bebeğin alt bezini hiç açmadan aileyi '
                                        'evine geri göndermek'}],
                 'question': 'Sadece anne sütü alan, bezinde kan çizgileri olan bu 2 aylık bebekte ilk muayene '
                             'yaklaşımı nasıl olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'FPIAP tanısı kliniktir. Sağlıklı, iyi büyüyen bebekte rutin '
                                               'kolonoskopi, biyopsi, kan tahlili veya IgE testleri endike değildir '
                                               '(FPIAP non-IgE aracılıdır, alerji deri testi negatiftir).',
                                'is_correct': True,
                                'new_finding': 'İnvaziv girişim ve gereksiz tetkiklerden kaçınıldı. Diyet eliminasyon '
                                               'planına geçildi.',
                                'text': 'Klinik tablosu stabil olan bu bebekte invaziv tetkik veya kolonoskopi '
                                        'yapmadan klinik izlem planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'İki aylık sağlıklı bebeğe yapılan kolonoskopi anestezi riski ve '
                                                   'iyatrojenik kolon perforasyonu riski oluşturdu.',
                                'teaching_point': 'Alerjik proktokolit tanısı için kolonoskopi gerekmez; maternal '
                                                  'diyet eliminasyonuna klinik yanıt tanı koydurur.',
                                'text': 'Tanıyı kesinleştirmek amacıyla bebeğe genel anestezi altında acil total '
                                        'kolonoskopi ve çoklu biyopsi yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Spesifik IgE negatif geldi ve anneye süt içebileceği söylendi; '
                                                   'bebeğin kanaması daha da arttı.',
                                'teaching_point': 'FPIAP non-IgE aracılı hücresel bir alerjidir; kanda IgE testleri '
                                                  'tamamen negatiftir, yanıltıcıdır.',
                                'text': 'Alerjiyi doğrulamak için kanda total IgE ve süt spesifik IgE testlerine '
                                        'bakarak sonuca göre diyet açmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tomografi normal geldi ancak 2 aylık bebek gereksiz iyonizan '
                                                   'radyasyon yüküne maruz kaldı.',
                                'teaching_point': 'Süt çocukluğu proktokolitinde bilgisayarlı tomografinin kesinlikle '
                                                  'yeri yoktur.',
                                'text': 'Kanama odağını bulmak amacıyla bebeğe intravenöz kontrastlı tüm batın '
                                        'bilgisayarlı tomografisi çektirmek'}],
                 'question': 'Fizik muayenesi tamamen doğal, büyümesi iyi ve fissürü olmayan bu bebekte tetkik planı '
                             'ne olmalıdır?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Genel durumu iyi, iyi büyüyen anne sütlü bebekte mukuslu kanlı dışkı '
                                               'Besin Proteini İlişkili Alerjik Proktokolit tanısıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Besin Proteini İlişkili Alerjik Proktokolit (FPIAP - İnek '
                                               'Sütü Proteini Kaynaklı).',
                                'text': 'Alerjik proktokolit tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Bakteriyel kolitte yüksek ateş, toksik görünüm ve dehidratasyon '
                                                   'olur; bu bebek tamamen afebril ve sağlıklıdır.',
                                'teaching_point': 'Afebril, sağlıklı büyüyen bebeğin bezindeki izole kan enfeksiyöz '
                                                  'kolit değildir.',
                                'text': 'Akut bakteriyel kolit enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Meckel divertikülü masif, pıhtılı vişne çürüğü kanama ve derin '
                                                   'anemi yapar; kılcal mukuslu kan çizgileri yapmaz.',
                                'teaching_point': 'Meckel divertikülü bol miktarda ağrısız masif rektal kanama ile '
                                                  'gelir; mukuslu çizgilenme proktokolite özgüdür.',
                                'text': 'Meckel divertikülü kanaması anomalisi'},
                              { 'is_correct': False,
                                'scenario_update': 'İnvajinasyonda şiddetli ağrı krizleri, safralı kusma ve çilek '
                                                   'jölesi gaita olur; bu bebek neşeli ve emmektedir.',
                                'teaching_point': 'İnvajinasyon akut cerrahi obstrüksiyondur; proktokolitte ise bebek '
                                                  'tamamen huzurlu ve stabildir.',
                                'text': 'İleokolik invajinasyon obstrüksiyonu'}],
                 'question': 'Anne sütü alan, sağlıklı, iyi kilo alan 2 aylık bebeğin bezinde mukuslu taze kan '
                             'çizgileri ile tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'İlk basamak tedavi emziren annenin diyetinden tüm süt ürünlerinin '
                                               '(süt, yoğurt, peynir, tereyağı, bisküvi vb.) en az 2-4 hafta '
                                               'çıkarılmasıdır. Anne sütü kesilmez! Anneye günlük 1000 mg kalsiyum ve '
                                               'D vitamini desteği verilmelidir.',
                                'is_correct': True,
                                'new_finding': 'Anneye süt eliminasyon diyeti ayrıntılı anlatıldı. 5 gün sonra bezdeki '
                                               'kan çizgileri tamamen kayboldu, bebeğin kilo alımı sağlıklı devam '
                                               'etti. Anne sütünün güvenle sürdürülmesi sağlandı.',
                                'text': 'Emziren annenin diyetinden tüm inek sütü ve süt ürünlerini tamamen çıkarmak '
                                        've anneye kalsiyum desteği vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Soya maması başlanan bebekte soyanın çapraz reaksiyonu nedeniyle '
                                                   'daha şiddetli kolit gelişti.',
                                'teaching_point': 'İnek sütü alerjisinde anne sütü kesilmez! Ayrıca 6 ay altında soya '
                                                  'mamaları çapraz alerji riskiyle önerilmez.',
                                'text': 'Anne sütünü anında tamamen keserek bebeğe eczaneden soya bazlı standart mama '
                                        'başlamasını önermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz steroid verilen bebekte immünsüpresyon, huzursuzluk ve '
                                                   'büyüme baskılanması gelişti.',
                                'teaching_point': 'Basit proktokolitte sistemik steroidlerin yeri yoktur; sadece '
                                                  'maternal diyet eliminasyonu yeterlidir.',
                                'text': 'Kanamayı durdurmak amacıyla 2 aylık bebeğe ağızdan yüksek doz sistemik '
                                        'kortikosteroid şurup başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Diyet yapılmadığı için kolit ilerledi ve bebekte mikroanjiyopatik '
                                                   'demir eksikliği anemisi gelişti.',
                                'teaching_point': 'Antijen eliminasyonu yapılmazsa rektal mukozal inflamasyon sürer ve '
                                                  'anemiye yol açabilir.',
                                'text': 'Diyete hiç dokunmayıp kanamanın bebek büyüdükçe kendi kendine geçmesini '
                                        'bekleyerek taburcu etmek'}],
                 'question': 'Alerjik proktokolit tanısı konulan bu bebeğin anne ve beslenme yönetimi nasıl '
                             'planlanmalıdır?',
                 'stage_title': 'Tedavi Yönetimi ve Taburculuk Planı'}]},
  { 'age': '4 Yaşında',
    'case_pearl': 'Giardia lamblia duodenal ve jejunal mukozaya tutunarak fırçamsı kenar enzimlerini bozar; '
                  'malabsorpsiyon, aşırı gaz, distansiyon, kötü kokulu yağlı dışkı (steatore) ve kilo kaybı yapar. İki '
                  'haftayı aşan uzamış ishallerde arıtılmamış su teması öyküsü tipiktir. Tanıda dışkı mikroskopisinde '
                  'kist/trofozoit aranır veya dışkıda Giardia antijeni (ELISA/hızlı test) bakılır. İlk tercih oral '
                  'metronidazol (30 mg/kg/gün 3 dozda, 5-7 gün) veya tinidazoldür.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'İki haftadır geçmeyen kötü kokulu cıvık ishal, karında şişkinlik ve gaz sancısı',
    'disposition': 'Yeşil Alandan Oral Metronidazol Tedavisi ve Hijyen/Su Güvenliği Önerileri ile Taburculuk',
    'final_diagnosis': 'Giardiazis (Giardia lamblia / duodenalis Paraziter Malabsorpsiyonu)',
    'gender': 'Kız',
    'history': 'Dört yaşındaki kız çocuğu: İki hafta önce köyde kuyu suyundan içtikten sonra başlayan, günde 3-4 kez '
               'çıkan, açık renkli, aşırı kötü kokulu, köpüklü ve yağlı cıvık dışkılaması var. Kan içermiyor. Karında '
               'sürekli gurultu, geğirme ve iştahsızlık tarifliyor. Kilosu son 2 haftada yarım kilo azalmış.',
    'id': 'G46',
    'steps': [ { 'options': [ { 'explanation': 'Uzamış ishalde kilo kaybı, batın distansiyonu, subfebril seyir ve '
                                               'malabsorpsiyon bulguları paraziter etkenleri düşündürür.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 98/dk, SS 20/dk, SpO2 %99, TA 94/60 '
                                               'mmHg. Son 1 ayda 500 gram kilo kaybı tespit edildi. Batın hafif '
                                               'distandü, timpanik, epigastrik ve periumbilikal alanda hafif '
                                               'hassasiyet mevcut; defans veya rebound yok. Bağırsak sesleri '
                                               'hiperaktif.',
                                'text': 'Büyüme eğrisi kaybını, karın distansiyonunu, malabsorpsiyon bulgularını ve '
                                        'dehidratasyon derecesini sistemik muayene etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Vital bulguları stabil hastaya yoğun bakım yatağı ayrılması '
                                                   'gereksiz panik yarattı.',
                                'teaching_point': 'Genel durumu iyi ve dehidrate olmayan subakut ishaller Yeşil Alanda '
                                                  'ayaktan yönetilir.',
                                'text': 'İki haftadır ishal olduğu için fizik muayene yapmadan hastayı derhal cerrahi '
                                        'yoğun bakıma yatırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Kömür tableti paraziter etkeni yok etmedi; çocuğun ağızdan alımını '
                                                   'zorlaştırdı.',
                                'teaching_point': 'Paraziter malabsorpsiyonda aktif kömür etkisizdir; hedefe yönelik '
                                                  'antiparaziter gerekir.',
                                'text': 'Kötü kokulu gazı gidermek amacıyla çocuğa acil serviste yüksek doz oral kömür '
                                        'tableti içirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Paraziter enfeksiyonu olan çocuğa travmatik kemik iliği biyopsisi '
                                                   'hazırlığı başlatıldı.',
                                'teaching_point': 'Kuyu suyu teması sonrası kilo kaybı ve ishalde öncelikle enfeksiyöz '
                                                  'parazitler düşünülmelidir.',
                                'text': 'Kilo kaybını kanser ön tanısı kabul ederek fizik muayene yapmadan kemik iliği '
                                        'biyopsisi planlamak'}],
                 'question': 'İki haftadır süren kötü kokulu ishal ve kilo kaybı olan bu çocukta ilk muayene '
                             'yaklaşımınız ne olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'Giardia kistleri aralıklı atıldığından 3 ayrı gün gaita mikroskopisi '
                                               'veya yüksek duyarlılıklı dışkı Giardia antijen testi (ELISA) altın '
                                               'standarttır.',
                                'is_correct': True,
                                'new_finding': 'Dışkı Giardia Antijen Testi: POZİTİF. Gaita Mikroskopisi: Bol miktarda '
                                               'Giardia lamblia kistleri ve hareketli trofozoitleri izlendi; lökosit '
                                               'veya eritrosit saptanmadı.',
                                'text': 'Dışkıda Giardia antijeni araştırmak veya üç ardışık günde mikroskopik gaita '
                                        'parazit incelemesi istemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Basit dışkı testiyle konacak tanı için çocuk gereksiz genel '
                                                   'anestezi ve invaziv biyopsiye maruz kaldı.',
                                'teaching_point': 'Giardiazis non-invaziv dışkı antijeni veya mikroskopisi ile kolayca '
                                                  'saptanır; endoskopi ilk adım değildir.',
                                'text': 'Parazit aramadan önce hastaya genel anestezi altında acil tanısal '
                                        'özofagogastroduodenoskopi ve biyopsi yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tiroid testleri normal geldi ancak parazit teşhis edilemediği için '
                                                   'ishal ve kilo kaybı devam etti.',
                                'teaching_point': 'Su teması sonrası uzamış kötü kokulu ishalde dışkıda parazit '
                                                  'incelemesi zorunludur.',
                                'text': 'Tanıyı dışlamak için sadece kanda kalsiyum ve tiroid fonksiyon testleri '
                                        'bakarak hastayı göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Antiviral ilaç parazite hiçbir etki göstermedi ve çocukta ilaca '
                                                   'bağlı kusma başladı.',
                                'teaching_point': 'Giardia bir protozoondur; antiviral ilaçların hiçbir etkinliği '
                                                  'yoktur.',
                                'text': 'Hiçbir tetkik yapmadan hastaya doğrudan ampirik yüksek doz antiviral '
                                        'oseltamivir şurup başlamak'}],
                 'question': 'Giardiazis şüphesi olan bu çocukta tanıyı doğrulamak için yapılması gereken en uygun '
                             'tetkik hangisidir?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Kuyu suyu öyküsü, kötü kokulu köpüklü ishal, kilo kaybı ve dışkıda '
                                               'Giardia kistleri giardiazis tanısını kesinleştirir.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Giardia lamblia Enfeksiyonu (Paraziter Malabsorpsiyon).',
                                'text': 'Akut giardiazis parazit enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Çölyakta kuyu suyu sonrası akut başlangıç ve dışkıda parazit '
                                                   'trofozoitleri izlenmez.',
                                'teaching_point': 'Çölyak kronik gluten enteropatisidir; dışkıda Giardia antijeni '
                                                  'bulunması parazitozu kanıtlar.',
                                'text': 'Çölyak hastalığı otoimmün enteropatisi'},
                              { 'is_correct': False,
                                'scenario_update': 'Kistik fibroziste yenidoğandan itibaren kronik öksürük ve mekonyum '
                                                   'ileusu vardır; kuyu suyuyla bulaşmaz.',
                                'teaching_point': 'Kistik fibrozis genetik multisistemik bir hastalıktır; akut '
                                                  'enfeksiyöz parazit tablosu değildir.',
                                'text': 'Kistik fibrozis ekzokrin yetmezliği'},
                              { 'is_correct': False,
                                'scenario_update': "Toddler's diyarede kilo alımı tamamen normaldir; kilo kaybı ve "
                                                   'dışkıda parazit pozitifliği görülmez.',
                                'teaching_point': "Toddler's diyarede büyüme bozulmaz ve parazit saptanmaz; bu hastada "
                                                  'kilo kaybı ve pozitif parazit vardır.',
                                'text': 'Kronik nonspesifik yürümeye başlayan diyaresi'}],
                 'question': 'Kuyu suyu teması, 2 haftadır uzamış yağlı ishal, gaz ve dışkıda parazit tespiti ile '
                             'kesin tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Giardiazis tedavisinde oral metronidazol (30 mg/kg/gün, 3 dozda, 5-7 '
                                               'gün) veya tek doz tinidazol ilk tercihtir. Aileye kuyu sularının '
                                               'kaynatılması veya filtrelenmesi, el hijyeni ve kreş sanitasyonu '
                                               'anlatılmalıdır.',
                                'is_correct': True,
                                'new_finding': 'Metronidazol tedavisi başlandı. Aileye su hijyeni anlatıldı. 5 gün '
                                               'sonra dışkı kıvamı tamamen düzeldi, karın şişliği geçti ve çocuk '
                                               'tekrar kilo almaya başladı.',
                                'text': 'Oral metronidazol tedavisini beş ila yedi gün uygulamak ve içme sularının '
                                        'kaynatılması eğitimini vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Antibakteriyel seftriakson protozoonlara etki etmedi; çocuğun '
                                                   'ishal şikayeti kesintisiz sürdü.',
                                'teaching_point': "Sefalosporinlerin Giardia'ya etkinliği yoktur; antiprotozoal "
                                                  'ajanlar (metronidazol) şarttır.',
                                'text': 'Parazitleri öldürmek için hastaya acil koşullarda damardan yüksek doz '
                                        'seftriakson infüzyonu uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Sarımsak mide mukozasını tahriş ederek çocukta akut gastrit ve '
                                                   'şiddetli epigastrik ağrı yaptı.',
                                'teaching_point': 'Kanıta dayalı antiparaziter tedavi yerine uygunsuz alternatif '
                                                  'yöntemler komplikasyon doğurur.',
                                'text': 'İlaç vermeden hastaya sadece her gün iki baş çiğ sarımsak yedirerek taburcu '
                                        'etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Loperamid bağırsak motilitesini durdurarak parazitlerin mukozada '
                                                   'çoğalmasına ve toksik distansiyona yol açtı.',
                                'teaching_point': 'Enfeksiyöz ve paraziter ishallerde motilite azaltıcı ilaçlar '
                                                  'kesinlikle verilmemelidir.',
                                'text': 'İshali hemen kesmek için hastaya yüksek doz loperamid ve opiat türevi şurup '
                                        'reçete etmek'}],
                 'question': 'Giardiazis tanısı kesinleşen 4 yaşındaki bu hastanın tedavisi ve aile eğitimi nasıl '
                             'olmalıdır?',
                 'stage_title': 'Tedavi Yönetimi ve Taburculuk Planı'}]},
  { 'age': '7 Yaşında',
    'case_pearl': 'Akut mezenterik lenfadenit, geçirilmiş viral üst solunum yolu veya enterik enfeksiyon sonrası '
                  'mezenterik lenf nodlarının reaktif hiperplazisidir. Sağ alt kadran ağrısıyla pediatrik acilde en '
                  'sık akut apandisiti taklit eden selim tablodur. Ağrı apandisite göre daha yaygın, gezici ve daha az '
                  "şiddetlidir; çocuk genellikle zıplayabilir. Batın USG'de kriterler: Sağ alt kadranda apendiksin "
                  'tamamen normal ve basılabilir olması + en az 3 adet, kısa aksı ≥8 mm (veya uzun aksı ≥10 mm) oval, '
                  'ekojen hiluslu, hipervasküler lenf nodu kümelenmesi. Tedavi semptomatiktir (analjezi, hidrasyon).',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Bir hafta önce geçirdiği gripten sonra başlayan sağ alt kadran karın ağrısı ve subfebril ateş',
    'disposition': 'Yeşil Alandan Batın USG ile Apandisitin Dışlanması, Semptomatik Tedavi ve Alarm Bulguları ile '
                   'Taburculuk',
    'final_diagnosis': 'Akut Mezenterik Lenfadenit (Reaktif Lenfoid Hiperplazi)',
    'gender': 'Erkek',
    'history': "Yedi yaşındaki erkek çocuk ailesi tarafından Yeşil Alana getiriliyor: 'Bir hafta önce yüksek ateş, "
               'burun akıntısı ve boğaz ağrısı geçirmişti, tam iyileşti derken 2 gündür sağ alt kadranda sızlayıcı '
               'karın ağrısı başladı. Ateşi evde 37.6°C ölçüldü. Kusması veya ishali yok, iştahı hafif azalmış ama '
               "yemek yiyebiliyor. Zıplayınca sağ tarafında hafif batma oluyor ancak yürüyebiliyor.'",
    'id': 'G47',
    'steps': [ { 'options': [ { 'explanation': 'Apandisit ile mezenterik lenfadenit ayrımında periton irritasyonu '
                                               '(istemsiz defans, zıplama ağrısı) dikkatle taranmalıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.5°C, KTA 92/dk, SS 20/dk, SpO2 %99, TA 102/64 '
                                               'mmHg. Genel durumu iyi, rahat yürüyebiliyor. Orofarenks hafif '
                                               'hiperemik. Batın muayenesinde sağ alt kadranda hafif-orta palpasyon '
                                               'hassasiyeti mevcut; istemsiz defans yok, rebound yok. Çocuk tek ayak '
                                               'üzerinde zıplayabiliyor.',
                                'text': 'Sağ alt kadranda McBurney hassasiyeti, istemsiz defans, psoas ve zıplama '
                                        'ağrısını nazik muayene ile incelemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Muayenesiz cerrahiye alınan hastada normal apendiks çıkarıldı; '
                                                   'gereksiz cerrahi morbidite gelişti.',
                                'teaching_point': 'Her sağ alt kadran ağrısı apandisit değildir; viral lenfadenit '
                                                  'dikkatli muayene ile ayırt edilebilir.',
                                'text': 'Sağ alt kadran ağrısı olduğu için fizik muayene yapmadan hastayı doğrudan '
                                        'acil apendektomi ameliyatına almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Muayene edilmeyen çocukta olası apandisit riski dışlanamadı ve '
                                                   'ailede güvensizlik oluştu.',
                                'teaching_point': 'Sağ alt kadran ağrısı olan her çocukta tam bir batın muayenesi ve '
                                                  'gerekirse görüntüleme şarttır.',
                                'text': 'Karın ağrısını tamamen psikolojik kabul edip batına hiç dokunmadan hastayı '
                                        'derhal Yeşil Alandan taburcu etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Taş semptomu olmayan hastada uygunsuz ürolojik girişim hazırlığı '
                                                   'gereksiz maliyet ve kaygı yarattı.',
                                'teaching_point': 'Sağ alt kadran ağrısında öncelik apandisit ve mezenterik '
                                                  'lenfadenittir; renal kolik muayenesiz düşünülmez.',
                                'text': 'Ağrının böbrek taşından kaynaklandığını varsayarak hastaya fizik muayene '
                                        'yapmadan acil litotripsi planlamak'}],
                 'question': 'Geçirilmiş viral enfeksiyon sonrası sağ alt kadran ağrısı olan bu çocukta ilk muayene '
                             'yaklaşımı nasıl olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'Batın USG normal çaplı basılabilen apendiksi göstererek cerrahiyi '
                                               'dışlar; sağ alt kadranda kümelenmiş büyümüş lenf nodları mezenterik '
                                               'lenfadenit tanısını doğrular.',
                                'is_correct': True,
                                'new_finding': 'Batın USG: Apendiks normal kalibrede (4.2 mm), komprese edilebilir ve '
                                               'lümeni açık izlendi. Sağ alt kadranda mezenterik alanda en büyüğü 11x6 '
                                               'mm boyutlarında, oval, ekojen hilusu korunmuş çok sayıda büyümüş '
                                               'reaktif lenf nodu kümelenmesi saptandı. Serbest sıvı izlenmedi. Tam '
                                               'kan: Lökosit 8.400/mm³, CRP 8 mg/L.',
                                'text': 'İyonizan radyasyon içermeyen batın ultrasonografisi ile apendiks çapını ve '
                                        'mezenterik lenf nodlarını incelemek'},
                              { 'is_correct': False,
                                'scenario_update': '7 yaşındaki çocuk gereksiz yere yüksek doz radyasyona maruz '
                                                   'bırakıldı; USG yeterliydi.',
                                'teaching_point': 'Çocuklarda apandisit ve lenfadenit ayrımında ilk tercih her zaman '
                                                  'ultrasonografidir; BT ilk adım olamaz.',
                                'text': 'Radyolojik ultrasonografiyi atlayıp kesin tanı için doğrudan kontrastlı tüm '
                                        'batın tomografisi çektirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Reaktif lenf noduna yapılan invaziv girişim batın içi hematom ve '
                                                   'bağırsak delinmesi riski yarattı.',
                                'teaching_point': 'Mezenterik lenfadenit selim bir tablodur; biyopsi kesinlikle endike '
                                                  'değildir ve tehlikelidir.',
                                'text': 'Lenf nodu boyutunu öğrenmek için acil serviste perkütan iğne ile lenf bezi '
                                        'biyopsisi yapmaya kalkışmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Viral kökenli lenfadenitte antibiyotik fayda sağlamadı; gereksiz '
                                                   'hastane yatışı yapıldı.',
                                'teaching_point': 'Mezenterik lenfadenit viral kökenlidir; antibiyotik tedavisi '
                                                  'gerekmez.',
                                'text': 'Hiçbir tetkik yapmadan hastaya doğrudan ampirik intravenöz geniş spektrumlu '
                                        'meropenem başlamak'}],
                 'question': 'Apandisit şüphesini netleştirmek ve lenfadeniti doğrulamak için en uygun görüntüleme ve '
                             'tetkik hangisidir?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': "ÜSYE sonrası sağ alt kadran ağrısı, normal apendiks ve USG'de "
                                               'mezenterik büyümüş lenf nodları mezenterik lenfadenit tanısıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Akut Mezenterik Lenfadenit (Reaktif Benign Lenfadenopati).',
                                'text': 'Akut mezenterik lenfadenit tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Apendiks ultrasonografide tamamen normal çapta ve komprese '
                                                   'edilebilir bulunmuştur; apandisit dışlanmıştır.',
                                'teaching_point': 'Apendiks çapı <6 mm ve komprese edilebiliyorsa akut apandisit '
                                                  'ekarte edilir.',
                                'text': 'Akut cerrahi flegmonöz apandisit'},
                              { 'is_correct': False,
                                'scenario_update': 'İdrar tahlili tamamen temizdir ve böbrek lojları doğaldır; idrar '
                                                   'yolu enfeksiyonu yoktur.',
                                'teaching_point': 'İYE idrar tahliliyle tanı alır; mezenterik lenfadenitte idrar '
                                                  'temizdir.',
                                'text': 'Komplike piyelonefrit idrar yolu'},
                              { 'is_correct': False,
                                'scenario_update': 'Meckel divertikülitinde kalın duvarlı kör tübüler yapı ve lokal '
                                                   'peritonit olur; reaktif lenf nodu kümesi olmaz.',
                                'teaching_point': 'Meckel divertiküliti cerrahi peritonittir; mezenterik lenfadenit '
                                                  'ise selim lenf nodu büyümesidir.',
                                'text': 'İnflame Meckel divertiküliti tablosu'}],
                 'question': "Geçirilmiş viral enfeksiyon, normal apendiks ve USG'de sağ alt kadranda büyümüş reaktif "
                             'lenf nodları ile tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Mezenterik lenfadenit kendini sınırlayan selim bir hastalıktır. '
                                               'Antibiyotik gerekmez. Oral hidrasyon, ihtiyaç halinde parasetamol '
                                               'verilir. Ateşin yükselmesi, safralı kusma veya ağrının şiddetlenmesi '
                                               'durumunda tekrar başvuru anlatılır.',
                                'is_correct': True,
                                'new_finding': 'Aileye durum açıklandı. Parasetamol şurup önerildi. 48 saat sonra '
                                               'ağrısı tamamen geriledi, çocuk normal okul aktivitelerine döndü.',
                                'text': 'Tablonun selim olduğunu anlatmak, hidrasyon ve oral parasetamol önerip '
                                        'kırmızı bayraklarla ayaktan taburcu etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz steroid kullanımı çocukta immünsüpresyona ve viral '
                                                   'enfeksiyonun nüksetmesine yol açtı.',
                                'teaching_point': 'Reaktif lenfadenitte kortikosteroid verilmez; lenf nodları haftalar '
                                                  'içinde kendiliğinden geriler.',
                                'text': 'Lenf nodlarını yok etmek için hastaya iki hafta boyunca oral yüksek doz '
                                        'kortikosteroid şurup başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Normal apendiksi olan hastaya cerrahi yapılması anestezi ve yara '
                                                   'yeri enfeksiyonu riski oluşturdu.',
                                'teaching_point': 'Mezenterik lenfadenitte cerrahi girişim endikasyonu yoktur; '
                                                  'gereksiz cerrahiden kaçınılmalıdır.',
                                'text': 'Ağrının nüksetmesini önlemek amacıyla hastayı ameliyathaneye alıp profilaktik '
                                        'apendektomi ameliyatı yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz besin kısıtlaması çocuğun kilo kaybetmesine ve kas '
                                                   'zayıflığına yol açtı.',
                                'teaching_point': 'Mezenterik lenfadenitte katı gıda kısıtlaması veya yatak hapsi '
                                                  'önerilmez; normal beslenme sürdürülür.',
                                'text': 'Hastalık tamamen geçene kadar çocuğu bir ay boyunca yatak istirahatine alıp '
                                        'katı gıdaları yasaklamak'}],
                 'question': 'Akut mezenterik lenfadenit tanısı konulan bu hastada en uygun tedavi ve taburculuk '
                             'stratejisi hangisidir?',
                 'stage_title': 'Tedavi Yönetimi ve Taburculuk Planı'}]},
  { 'age': '2.5 Yaşında',
    'case_pearl': "Toddler's Diarrhea (Kronik Non-spesifik Diyare), 1-3 yaş grubundaki sağlıklı çocuklarda uzamış "
                  'ishalin en sık nedenidir. En kritik anahtar: BÜYÜME VE GELİŞMENİN TAMAMEN NORMAL OLMASIDIR (kilo '
                  'kaybı, boy kısalığı veya anemi yoktur). Dışkıda mukus veya sindirilmemiş gıda parçaları tipiktir; '
                  'gece dışkılama ve kanama görülmez. Patofizyolojide aşırı fruktoz ve sorbitol içeren meyve suları '
                  "(ozmotik ishal), düşük yağlı ve dengesiz beslenme rol oynar. Tedavi '4F Kuralı'dır: 1) Fat "
                  '(Diyetteki yağı artır, motiliteyi yavaşlatır), 2) Fiber (Normal lif), 3) Fluid (Aşırı sıvı alımını '
                  'sınırlat), 4) Fruit juice (Meyve sularını tamamen kes). Tetkik ve ilaç gerekmez.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Günde 4-5 kez sindirilmemiş besin artıkları içeren cıvık dışkılama, büyüme gelişmesi tamamen normal',
    'disposition': 'Yeşil Alandan Beslenme Eğitimi (4F Kuralı: Meyve Suyunun Kısıtlanması, Lif ve Yağ Dengesi) ile '
                   'Taburculuk',
    'final_diagnosis': "Kronik Non-spesifik Diyare (Toddler's Diarrhea / Aşırı Meyve Suyu ve Düşük Yağ Tüketimi)",
    'gender': 'Erkek',
    'history': "Annesi anlatıyor: 'Yaklaşık 2 aydır günde 4-5 kez kaka yapıyor. Sabah ilk kakası şekilli ve katı "
               'çıkıyor, öğleden sonra ve akşama doğru cıvıklaşıyor. Kakanın içinde dün yediği bezelye, havuç ve mısır '
               'parçaları aynen duruyor. Geceleri uykusunda hiç kaka yapmıyor. Çocuk günde 1 litre elma suyu ve meyve '
               "suyu içiyor. Kilosu ve boyu 50. persentilde, gayet neşeli, koşup oynuyor.'",
    'id': 'G48',
    'steps': [ { 'options': [ { 'explanation': 'Büyüme eğrisinin korunmuş olması (persentil düşüşü olmaması) organik '
                                               'malabsorpsiyonu (çölyak, KF vb.) dışlar; gece dışkılamasının olmaması '
                                               'fonksiyonel kökeni destekler.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 96/dk, SS 22/dk, SpO2 %99, TA 92/56 '
                                               'mmHg. Tartı: 13.5 kg (50. persentil), Boy: 92 cm (50. persentil), '
                                               'persentil kaybı yok. Genel durumu çok iyi, canlı, hareketli. Batın '
                                               'rahat, organomegali yok, perianal bölge doğal. Ödem veya solukluk yok.',
                                'text': 'Büyüme eğrisi persentillerini, dehidratasyon olmadığını ve batının rahat '
                                        'olduğunu sistemik muayene ile doğrulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Büyümesi mükemmel ve canlı olan çocuğun yoğun bakıma alınması '
                                                   'ailede haksız panik yarattı.',
                                'teaching_point': 'Gelişimi normal, kilo kaybı ve alarm bulgusu olmayan çocukta '
                                                  'hastaneye yatış endike değildir.',
                                'text': 'İki aydır süren ishali ağır malabsorpsiyon kabul edip hastayı derhal '
                                        'gastrointestinal yoğun bakıma yatırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Loperamid verilmesi çocukta paralitik ileus ve karın '
                                                   'distansiyonuna neden oldu.',
                                'teaching_point': "Küçük çocuklarda loperamid KONTRENDİKEDİR; toddler's diyarede ilaç "
                                                  'değil, diyet düzenlemesi yapılır.',
                                'text': 'İshali hemen kesmek amacıyla hastaya acil serviste yüksek doz motilite '
                                        'baskılayıcı loperamid enjekte etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Sağlıklı büyüyen çocukta invaziv endoskopi yapılması gereksiz '
                                                   'anestezi ve delinme riski yarattı.',
                                'teaching_point': 'Sindirilmemiş sebze parçaları hızlı intestinal geçişe bağlıdır; '
                                                  'endoskopi endikasyonu değildir.',
                                'text': 'Sindirilmemiş gıda gördüğü için hastayı derhal genel anestezi altında acil '
                                        'gastrointestinal endoskopiye almak'}],
                 'question': 'İki aydır cıvık dışkılayan bu 2.5 yaşındaki çocukta ilk klinik değerlendirme nasıl '
                             'olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': "Kilo kaybı, anemi, kanlı dışkı veya gece dışkılaması olmayan toddler's "
                                               'diyarede rutin kan tahlili, dışkı kültürü veya kolonoskopi önerilmez; '
                                               'ayrıntılı beslenme anamnezi tanı koydurur.',
                                'is_correct': True,
                                'new_finding': 'Ayrıntılı beslenme anamnezinde çocuğun günde 4-5 biberon (yaklaşık '
                                               '1000 mL) hazır elma suyu içtiği, az yağlı ve az lifli beslendiği '
                                               'öğrenildi. İnvaziv tetkik istenmedi.',
                                'text': 'Kırmızı bayrak taşımayan ve iyi büyüyen bu çocukta gereksiz pahalı '
                                        'laboratuvar tetkiklerinden kaçınarak diyeti sorgulamak'},
                              { 'is_correct': False,
                                'scenario_update': "Tüm testler normal geldi ancak aile 'çocuğumda amansız bir "
                                                   "hastalık var' kaygısına girdi.",
                                'teaching_point': 'Alarm semptomu olmayan çocukta aşırı tetkik yapılması ailenin '
                                                  'hastalık kaygısını besler.',
                                'text': 'Kesin tanı için kolonoskopi, ter testi, çölyak paneli ve gaitada alfa bir '
                                        'antitripsin tetkiklerini istemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Alerji testleri negatif geldi; tanı ve klinik yönetimde hiçbir '
                                                   'değişiklik olmadı.',
                                'teaching_point': "Toddler's diyare besin alerjisi değildir; ozmotik meyve suyu yükü "
                                                  've diyet dengesizliğidir.',
                                'text': 'Besin alerjisi şüphesiyle hastadan yüz parametreli alerji paneli ve kanda '
                                        'immünglobülinleri göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Uzun süreli açlık sağlıklı çocuğun kilo kaybetmesine ve ketozis '
                                                   'geliştirmesine neden oldu.',
                                'teaching_point': "Aç bırakma testi toddler's diyarede uygulanmaz; büyümenin "
                                                  'bozulmasına yol açar.',
                                'text': 'İshal nedenini anlamak için hastayı 1 hafta boyunca acil serviste aç bırakıp '
                                        'dışkı miktarını ölçmek'}],
                 'question': 'Büyümesi normal, alarm bulgusu ve dehidratasyonu olmayan bu çocukta tetkik yaklaşımı '
                             'nasıl olmalıdır?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': '1-3 yaş arası normal büyüyen çocukta gündüz sindirilmemiş gıdalı cıvık '
                                               "dışkılama Toddler's Diarrhea tanısıdır.",
                                'is_correct': True,
                                'new_finding': "Kesin Tanı: Kronik Non-spesifik Diyare (Toddler's Diarrhea / Meyve "
                                               'Suyu Ozmotik İshali).',
                                'text': 'Kronik nonspesifik yürümeye başlayan diyaresi'},
                              { 'is_correct': False,
                                'scenario_update': 'Çölyakta persentil kaybı, karın distansiyonu ve anemi olur; bu '
                                                   'çocukta büyüme persentili mükemmeldir.',
                                'teaching_point': "Çölyakta kilo alımı durur veya geriler; toddler's diyarede ise "
                                                  'büyüme tamamen normaldir.',
                                'text': 'Klasik çölyak hastalığı malabsorpsiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Giardiada yağlı dışkı, kramp ve kilo kaybı olur; meyve suyu '
                                                   'tüketimiyle ilişkili benign seyir beklenmez.',
                                'teaching_point': "Giardia kilo kaybı yapar; toddler's diyarede çocuk kilo kaybetmez, "
                                                  'persentilinde büyür.',
                                'text': 'Kronik giardiazis parazit enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': "İBH'de kanlı dışkı, gece dışkılaması, ateş ve büyüme geriliği "
                                                   'olur; bu çocukta bunların hiçbiri yoktur.',
                                'teaching_point': 'Gece dışkılamasının olmaması ve kan bulunmaması fonksiyonel '
                                                  'ishallerin temel özelliğidir.',
                                'text': 'İnflamatuar bağırsak hastalığı atağı'}],
                 'question': 'Normal büyüme, gündüz cıvık dışkılama, sindirilmemiş parçalar ve aşırı meyve suyu '
                             'tüketimi ile tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': "Toddler's diyare tedavisi diyettir: Meyve suları (fruktoz/sorbitol) "
                                               'kesilir, süt çocukluğundan kalan yağ kısıtlaması kaldırılır (tam yağlı '
                                               'süt, yoğurt, zeytinyağı eklenerek motilite yavaşlatılır), normal lif '
                                               'verilir. İlaç gerekmez.',
                                'is_correct': True,
                                'new_finding': 'Aileye elma suyu yerine su içirilmesi, yemeklere yağ eklenmesi '
                                               "önerildi. 2 hafta sonra dışkılama sayısı günde 1-2'ye indi ve dışkı "
                                               'tamamen şekilli hale geldi. Ailenin kaygısı tamamen yatıştı.',
                                'text': 'Dört f kuralını uygulamak, meyve sularını tamamen kesmek, diyetteki yağ '
                                        'oranını artırmak ve aileye güven vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz antibiyotikler bağırsak florasını bozarak sekonder '
                                                   'psödomembranöz kolit başlattı.',
                                'teaching_point': "Toddler's diyare bir enfeksiyon değildir; antibiyotik veya "
                                                  'antifungal kesinlikle kullanılmaz.',
                                'text': 'İshali kurutmak için hastaya altı ay boyunca antibiyotik ve antifungal şurup '
                                        'tedavisi başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Aşırı katı eliminasyon diyeti çocukta malnütrisyon ve mikrobesin '
                                                   'eksikliğine yol açtı.',
                                'teaching_point': "Toddler's diyarede besin alerjisi yoktur; katı kısıtlama diyetleri "
                                                  'çocuğun büyümesini bozar.',
                                'text': 'Tüm süt, yoğurt, ekmek ve meyveleri tamamen kesip hastayı sadece patates '
                                        'püresiyle beslemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Rektal lavmanlar rektal mukozayı travmatize etti ve çocukta anal '
                                                   'spazm oluşturdu.',
                                'teaching_point': 'Fonksiyonel ishalde rektal lavmanların hiçbir yeri yoktur; diyetle '
                                                  'kendiliğinden düzelir.',
                                'text': 'İshali durdurmak için hastaya her gün rektal sertleştirici lavmanlar '
                                        'uygulayarak taburcu etmek'}],
                 'question': "Toddler's diyare tanısı konulan bu çocuğun ailesine verilecek en uygun tedavi ve "
                             'beslenme eğitimi hangisidir?',
                 'stage_title': 'Diyet Düzenlemesi ve Aile Rehberliği'}]},
  { 'age': '3 Aylık',
    'case_pearl': 'Gastroözofageal Reflü (GÖR), mide içeriğinin istemsizce özofagusa geri kaçmasıdır ve sağlıklı süt '
                  "çocuklarının %50'sinde görülen fizyolojik bir süreçtir. 'Mutlu Kusan Bebek' (Happy Spitter): Bebek "
                  'kusar ancak kilo alımı mükemmeldir, öksürük/apne/boğulma yoktur, huzursuzluk veya beslenme reddi '
                  'yoktur. Bu tablo bir HASTALIK DEĞİLDİR (Gastroözofageal Reflü Hastalığı - GÖRH değildir). '
                  'NASPGHAN/ESPGHAN kılavuzlarına göre fizyolojik reflüde PPI (omeprazol vb.) veya H2 blokerlerin '
                  'KESİNLİKLE YERİ YOKTUR! Gereksiz asit süpresyonu pnömoni ve gastroenterit riskini artırır. Tedavi: '
                  'Aileye güvence vermek, aşırı beslemeyi önlemek, beslenme sonrası 20-30 dakika dik tutmak ve gazını '
                  'çıkarmaktır. 12-14. aylarda yürümeyle kendiliğinden düzelir.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Her beslenme sonrası ağzından peynirimsi süt çıkarması, ancak bebeğin gayet neşeli olması ve kilo '
                 'alması',
    'disposition': 'Yeşil Alandan Aile Eğitimi, Gereksiz Asit Baskılayıcı İlaçlardan Kaçınma ve Postüral Önlemler ile '
                   'Taburculuk',
    'final_diagnosis': "Fizyolojik Gastroözofageal Reflü ('Mutlu Kusan Bebek' - Happy Spitter)",
    'gender': 'Kız',
    'history': "Üç aylık kız bebek annesi tarafından getiriliyor: 'Emzirdikten hemen sonra veya gaz çıkarırken günde "
               '5-6 kez ağzından süt veya yoğurt gibi kesilmiş süt akıtıyor. Kusarken hiç ağlamıyor, aksine '
               'gülümsüyor. Boğulur gibi olmuyor, öksürmüyor, morarmıyor. Son bir ayda 900 gram almış, gelişimi çok '
               "iyi. Ama komşularımız reflü ilacı başlamamız gerektiğini söylüyor, endişelendik.'",
    'id': 'G49',
    'steps': [ { 'options': [ { 'explanation': 'Kilo alımının mükemmel olması, safrasız kusma, solunum sıkıntısı ve '
                                               'huzursuzluk olmaması fizyolojik reflüyü patolojik GÖRH ve pilor '
                                               'darlığından ayırır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 122/dk, SS 28/dk, SpO2 %100, Tartı: '
                                               'Günde 30 gram alıyor (mükemmel persentilde). Genel durumu çok neşeli, '
                                               'muayene masasında gülümsüyor. Solunum sesleri bilateral doğal, hışıltı '
                                               'veya ral yok. Batın yumuşak, organomegali veya kitle yok. Ön fontanel '
                                               'bombeliği veya çöküklüğü yok.',
                                'text': 'Büyüme persentillerini, solunum seslerini, batın rahatlığını ve kırmızı '
                                        'bayrak olmadığını sistemik muayene ile doğrulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz cerrahi hazırlığı yapılan mutlu bebekte hiçbir darlık '
                                                   'saptanmadı ve cerrahi iptal edildi.',
                                'teaching_point': 'Pilor darlığında bebek sürekli açtır, fışkırır kusar ve kilo '
                                                  'kaybeder; mutlu kusan bebekte olmaz.',
                                'text': 'Kusması olduğu için fizik muayene yapmadan bebeği derhal ameliyathaneye pilor '
                                        'stenozu cerrahisine almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Antiemetik verilmesi süt çocuğunda sedasyon ve solunum '
                                                   'düzensizliğine yol açtı.',
                                'teaching_point': 'Süt çocukluğu fizyolojik reflüsünde antiemetik ilaçların yeri '
                                                  'yoktur; zararlıdır.',
                                'text': 'Kusmayı durdurmak amacıyla 3 aylık bebeğe ağızdan yüksek doz santral etkili '
                                        'antiemetik şurup vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Yüzüstü yatırılan bebekte Ani Bebek Ölümü Sendromu (SIDS) riski '
                                                   'oluştu.',
                                'teaching_point': 'Bebekler reflü olsa dahi ASLA yüzüstü uyutulmamalıdır; SIDS riski '
                                                  'nedeniyle sırtüstü yatırılmalıdır.',
                                'text': 'Reflüyü tedavi etmek için bebeği her beslenmeden sonra yüzüstü yatırarak '
                                        'uyutmasını aileye önermek'}],
                 'question': 'Her beslenme sonrası kusması olan ancak mutlu ve iyi kilo alan bu bebekte ilk fizik '
                             'muayene yaklaşımı nasıl olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'Kılavuzlara göre uyarıcı semptomu olmayan (kilo kaybı, hematemez, apne '
                                               'vb.) fizyolojik reflüde batın USG, baryumlu pasaj grafisi veya '
                                               'pH-metri endike değildir; klinik tanı yeterlidir.',
                                'is_correct': True,
                                'new_finding': 'Gereksiz radyasyon ve tetkikten kaçınıldı. Anneye fizyolojik mekanizma '
                                               'anlatıldı.',
                                'text': 'Sağlıklı büyüyen mutlu kusan bebekte hiçbir radyolojik görüntüleme, ultrason '
                                        'veya kan tetkiki istememek'},
                              { 'is_correct': False,
                                'scenario_update': 'Baryum aspirasyon tehlikesi yarattı ve grafide sadece fizyolojik '
                                                   'reflü izlendi.',
                                'teaching_point': 'Baryumlu pasaj grafisi GÖRH tanısı koyduramaz; anatomik darlık '
                                                  'şüphesi yoksa çekilmez.',
                                'text': 'Mide çıkışını görmek amacıyla bebeğe yüksek doz baryum içirerek seri üst '
                                        'gastrointestinal grafiler çekmek'},
                              { 'is_correct': False,
                                'scenario_update': 'İnvaziv kateter bebeği aşırı ajite etti ve fizyolojik reflü '
                                                   'indeksini gösterdi.',
                                'teaching_point': 'Kilo alımı iyi olan bebekte invaziv pH impedans takibi '
                                                  'KONTRENDİKEDİR; aşırı tetkiktir.',
                                'text': 'Kesin tanı için 3 aylık bebeğe genel anestezi altında yirmi dört saatlik pH '
                                        'impedans kateteri takmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Testler normal geldi; gereksiz kan alımı bebeği hırpaladı.',
                                'teaching_point': 'Süt çocukluğu fizyolojik reflüsünde H. pylori veya gastrin '
                                                  'ölçümünün hiçbir yeri yoktur.',
                                'text': 'Midede bakteri olup olmadığını anlamak için kanda Helicobacter pylori '
                                        'serolojisi ve gastrin istemek'}],
                 'question': 'Fizik muayenesi tamamen doğal, büyümesi mükemmel olan bu mutlu kusan bebekte tetkik '
                             'yaklaşımı ne olmalıdır?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Büyüme gelişmesi mükemmel, eforsuz kusan ve huzursuzluğu olmayan süt '
                                               'çocuğu tablosu fizyolojik reflüdür (Happy Spitter).',
                                'is_correct': True,
                                'new_finding': "Kesin Tanı: Fizyolojik Gastroözofageal Reflü ('Mutlu Kusan Bebek' - "
                                               'Happy Spitter).',
                                'text': 'Fizyolojik gastroözofageal reflü süreci'},
                              { 'is_correct': False,
                                'scenario_update': 'Pilor stenozunda safrasız fışkırır kusma, metabolik alkaloz ve '
                                                   'belirgin kilo kaybı olur; bu bebek kilo almaktadır.',
                                'teaching_point': 'Pilor stenozu kilo kaybı ve fışkırır kusma yapar; mutlu kusan '
                                                  'bebekte kilo alımı mükemmeldir.',
                                'text': 'İnfantil hipertrofik pilor darlığı'},
                              { 'is_correct': False,
                                'scenario_update': "GÖRH'de büyüme geriliği, beslenme reddi, hematemez veya apne olur; "
                                                   'fizyolojik reflüde ise komplikasyon yoktur.',
                                'teaching_point': 'Reflü fizyolojik bir olaydır; hastalık (GÖRH) diyebilmek için kilo '
                                                  'kaybı veya solunum komplikasyonu şarttır.',
                                'text': 'Patolojik gastroözofageal reflü hastalığı'},
                              { 'is_correct': False,
                                'scenario_update': 'Volvulusta yeşil safralı kusma ve akut batın distansiyonu olur; bu '
                                                   'bebekte kusmuk sütsüdür ve batın rahattır.',
                                'teaching_point': 'Yeşil safralı kusma cerrahi acildir; beyaz sütsü kusma ise '
                                                  'fizyolojik reflü ile uyumludur.',
                                'text': 'Malrotasyon ve volvulus tıkanıklığı'}],
                 'question': 'Beslenme sonrası eforsuz peynirimsi kusma, mükemmel kilo alımı ve neşeli genel durum ile '
                             'tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Kılavuzlara göre mutlu kusan bebekte PPI veya H2 bloker KESİNLİKLE '
                                               'VERİLMEZ (enfeksiyon riskini artırır). Aileye durumun 1 yaşında '
                                               'düzeleceği anlatılır, aşırı besleme önlenir, beslenme sonrası 20-30 '
                                               'dakika dik tutma önerilir.',
                                'is_correct': True,
                                'new_finding': 'Aileye tablonun hastalık olmadığı anlatıldı. İlaç verilmedi. Beslenme '
                                               'sonrası dik tutma uygulayan ailenin kaygısı geçti; bebeğin büyümesi '
                                               'sağlıklı şekilde devam etti.',
                                'text': 'Gereksiz asit baskılayıcı ilaç yazmaktan kaçınmak, besleme sonrası dik tutma '
                                        've gaz çıkarma eğitimi vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz PPI başlanan bebekte 3 hafta sonra alt solunum yolu '
                                                   'enfeksiyonu ve gastroenterit gelişti.',
                                'teaching_point': 'Süt çocuklarında gereksiz PPI kullanımı mide asit bariyerini yok '
                                                  'ederek pnömoni ve enfeksiyon riskini katlar.',
                                'text': 'Mide asidini tamamen sıfırlamak için bebeğe yüksek doz proton pompa '
                                        'inhibitörü ve prokinetik başlamak'},
                              { 'is_correct': False,
                                'scenario_update': '3 aylık bebeğe erken tahıl verilmesi bağırsak sindirim sorunlarına '
                                                   've kabızlığa yol açtı.',
                                'teaching_point': 'Anne sütü en değerli besindir; fizyolojik reflü nedeniyle anne sütü '
                                                  'asla kesilmez.',
                                'text': 'Anne sütünü anında kestirip bebeğe sadece pirinç unu ve koyulaştırılmış ağır '
                                        'tahıl çorbaları içirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Fizyolojik duruma yapılan cerrahi çocukta yutma güçlüğü ve '
                                                   'gaz-şişkinlik sendromuna neden oldu.',
                                'teaching_point': 'Fizyolojik reflüde cerrahinin kesinlikle yeri yoktur; 1 yaşında '
                                                  'kendiliğinden düzelen doğal bir süreçtir.',
                                'text': 'Reflüyü cerrahi olarak düzeltmek amacıyla 3 aylık bebeğe laparoskopik Nissen '
                                        'fundoplikasyonu planlamak'}],
                 'question': 'Fizyolojik reflüsü olan bu mutlu bebeğin ailesine verilecek en uygun yönetim stratejisi '
                             'hangisidir?',
                 'stage_title': 'Tedavi Yönetimi ve Taburculuk Planı'}]},
  { 'age': '8 Yaşında',
    'case_pearl': 'Nonsteroid antiinflamatuar ilaçlar (NSAİİ / ibuprofen, ketoprofen vb.) mide mukozasındaki koruyucu '
                  'prostaglandin sentezini (COX-1 inhibisyonu) engelleyerek eroziv gastrit ve mukozal kanamalara yol '
                  'açar. Özellikle aç karnına veya sık dozlandığında risk çok artar. Küçük kanamalarda mide asidiyle '
                  "temas eden hemoglobin hematine dönüşerek 'kahve telvesi' (coffee-ground) şeklinde kusulur. "
                  "Hemodinamisi stabil, anemisi olmayan çocukta acil endoskopi gerekmez. İlk adım NSAİİ'nin derhal "
                  'kesilmesi ve asit baskılayıcı tedavi (H2 reseptör blokeri famotidin veya PPI) başlanmasıdır.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Üç gündür yüksek ateş için aç karnına sık sık ibuprofen şurup içtikten sonra başlayan epigastrik '
                 'yanma ve kahve telvesi kusma',
    'disposition': 'Yeşil Alandan NSAİİ Kesilmesi, H2 Reseptör Blokeri (Famotidin) Tedavisi ve Beslenme Önerileri ile '
                   'Taburculuk',
    'final_diagnosis': 'Akut İlaç İlişkili Gastrit (NSAİİ / İbuprofen Kaynaklı Mide Mukozal Hasarı)',
    'gender': 'Kız',
    'history': 'Sekiz yaşındaki kız çocuğu: Grip nedeniyle evde günde 4-5 kez aç karnına ibuprofen şurup içirilmiş. '
               'Dün gece başlayan şiddetli mide kazınması ve yanma ağrısı olmuş. Sabah bir kez az miktarda kahve '
               'telvesi kıvamında koyu renkli kusmuş. Dışkısı henüz siyah değil. Çocuk halsiz ancak baş dönmesi veya '
               'bayılması olmamış.',
    'id': 'G50',
    'steps': [ { 'options': [ { 'explanation': 'Üst GİS kanaması şüphesinde taşikardi/hipotansiyon (şok) dışlanmalı, '
                                               'batında peritonit aranmalı ve melena varlığı kontrol edilmelidir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.0°C, KTA 94/dk, SS 20/dk, SpO2 %99, TA 104/66 '
                                               'mmHg, KDZ 1.5 sn. Genel durumu iyi, solukluk veya terleme yok. Batın '
                                               'rahat, epigastriumda orta derecede hassasiyet mevcut; defans ve '
                                               'rebound yok. Rektal tuşede normal kahverengi gaita izlendi, melena '
                                               'saptanmadı.',
                                'text': 'Hemodinamik stabiliteyi, perfüzyonu, epigastrik hassasiyeti ve rektal tuşede '
                                        'melena olup olmadığını incelemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Vital bulguları ve kan sayımı normal hastaya transfüzyon yapılması '
                                                   'hacim yüklenmesine yol açtı.',
                                'teaching_point': 'Küçük kahve telvesi kusmalarda hasta normovolemikse transfüzyon '
                                                  'endike değildir; önce klinik değerlendirilir.',
                                'text': 'Kahve telvesi kusmayı masif kanama kabul ederek fizik muayene yapmadan '
                                        'hastaya derhal dört ünite kan transfüzyonu yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Safra kesesi doğal olan hastada gereksiz cerrahi konsültasyon '
                                                   'süreci başlatıldı.',
                                'teaching_point': 'Aç karnına NSAİİ kullanımı sonrası epigastrik yanma tipik ilaç '
                                                  'gastritidir; kolesistit değildir.',
                                'text': 'Epigastrik ağrıyı safra kesesi iltihabı sanarak hastaya fizik muayene '
                                        'yapmadan acil kolesistektomi planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Ek ibuprofen verilmesi mide mukozasındaki erozyonu derinleştirerek '
                                                   'taze kırmızı kanamaya yol açtı.',
                                'teaching_point': 'NSAİİ gastritinde ilacın sürdürülmesi ülser ve perforasyon riskini '
                                                  'artırır; KESİNLİKLE YASAKTIR.',
                                'text': 'Mide ağrısını dindirmek amacıyla hastaya hemen acil serviste bir doz daha '
                                        'yüksek doz ibuprofen şurup içirmek'}],
                 'question': 'Aç karnına ibuprofen kullanımı sonrası epigastrik ağrı ve kahve telvesi kusması olan '
                             'çocukta ilk muayene nasıl olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'Stabil, az miktarda kahve telvesi kusan çocukta bazal hemogram '
                                               'yeterlidir. Aktif masif kanama veya şok yoksa acil endoskopi gerekmez; '
                                               'medikal tedaviye yanıt izlenir.',
                                'is_correct': True,
                                'new_finding': 'Laboratuvar: Hb 12.4 g/dL, Hct %37, Lökosit 7.800/mm³, Trombosit '
                                               '280.000/mm³. Anemi veya trombositopeni saptanmadı. Acil invaziv '
                                               'endoskopiye gerek görülmedi.',
                                'text': 'Bazal hemoglobin düzeyini görmek için tam kan sayımı istemek ve stabil '
                                        'hastada acil endoskopi yapmadan medikal tedavi planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Stabil hastaya yapılan acil endoskopi sadece yüzeyel eritem '
                                                   'gösterdi; anestezi riski gereksizce alındı.',
                                'teaching_point': 'Stabil hafif gastrit kanamalarında acil endoskopi endike değildir; '
                                                  'medikal tedavi ile hızla geriler.',
                                'text': 'Kahve telvesi kusmayı doğrulamak için genel anestezi altında hastaya derhal '
                                        'acil özofagogastroduodenoskopi yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Grafiler normal geldi ancak mide mukozal hasarı hakkında hiçbir '
                                                   'bilgi sağlamadı.',
                                'teaching_point': 'Gastritte akciğer veya sinüs grafilerinin hiçbir tanısal yeri '
                                                  'yoktur.',
                                'text': 'Kanamayı araştırmak amacıyla hastaya iki yönlü akciğer ve sinüs grafileri '
                                        'çekip sonucu beklemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Buzlu lavaj çocukta hipotermi ve vazospazma yol açarak mukozal '
                                                   'iskemiyi artırdı.',
                                'teaching_point': 'Buzlu su lavajı güncel tıp pratiğinde terk edilmiştir; mukozal '
                                                  'hasarı artırır.',
                                'text': 'Kanamanın mideden olduğunu anlamak için çocuğa acil serviste yarım litre '
                                        'buzlu su ile mide lavajı uygulamak'}],
                 'question': 'Hemodinamisi stabil olan bu çocukta tanısal tetkik ve kanama değerlendirmesi nasıl '
                             'planlanmalıdır?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'NSAİİ (ibuprofen) kullanım öyküsü, epigastrik yanma ağrısı ve kahve '
                                               'telvesi kusma akut ilaç gastritini doğrular.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: İbuprofen Kullanımına Bağlı Akut İlaç İlişkili Gastrit.',
                                'text': 'İlaç ilişkili akut eroziv gastrit'},
                              { 'is_correct': False,
                                'scenario_update': 'Apandisitte ağrı sağ alt kadrandadır ve kahve telvesi kusma '
                                                   'yapmaz; epigastrik gastrit tablosuyla uyumsuzdur.',
                                'teaching_point': 'Apandisit alt kadran peritonitidir; üst GİS kanaması ve epigastrik '
                                                  'yanma gastrite özgüdür.',
                                'text': 'Akut flegmonöz apandisit perforasyonu'},
                              { 'is_correct': False,
                                'scenario_update': "Ülser perforasyonunda tahta karın defansı ve ADBG'de serbest hava "
                                                   'olur; bu hastada batın tamamen rahattır.',
                                'teaching_point': 'Perforasyonda yaygın tahta karın ve peritonit olur; izole '
                                                  'epigastrik hassasiyette perforasyon yoktur.',
                                'text': 'Perfore duodenal ülser peritoniti'},
                              { 'is_correct': False,
                                'scenario_update': 'Kolesistitte sağ üst kadranda Murphy belirtisi olur; NSAİİ sonrası '
                                                   'kahve telvesi kusma yapmaz.',
                                'teaching_point': 'Kolesistit safra kesesi enfeksiyonudur; mide mukozal hematin '
                                                  'kanaması yapmaz.',
                                'text': 'Akut taşlı kolesistit atağı'}],
                 'question': 'Aç karnına sık ibuprofen kullanımı, epigastrik yanma, hafif hematin kusma ve normal '
                             'hemogram ile tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'İlk adım suçlu NSAİİ ilacın kesilmesidir. Mide asidini baskılamak için '
                                               'H2 reseptör blokeri (famotidin 1 mg/kg/gün) veya PPI başlanır. Ateş '
                                               'için gerekirse parasetamol önerilir. Baharatlı/asitli gıdalar '
                                               'kısıtlanır.',
                                'is_correct': True,
                                'new_finding': 'İbuprofen kesildi. Oral famotidin başlandı. Ağrı için gerekirse tok '
                                               'karnına parasetamol önerildi. 48 saat sonra mide yanması tamamen '
                                               'geçti, kusması tekrarlamadı ve çocuk şifayla iyileşti.',
                                'text': 'İbuprofen kullanımını derhal durdurmak, oral famotidin tedavisi başlamak ve '
                                        'mideyi koruyucu beslenme önerileri vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'İbuprofen ve aspirin kombinasyonu midede derin ülser '
                                                   'perforasyonuna ve masif kanamaya yol açtı.',
                                'teaching_point': 'Gastrit gelişen hastada NSAİİ sürdürülmesi veya aspirin eklenmesi '
                                                  'ölümcül kanama ve perforasyon yapar.',
                                'text': 'Ateşi olduğu için ibuprofen dozunu iki katına çıkarıp yanına bir de oral '
                                        'aspirin ekleyerek taburcu etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Asitli içecekler hasarlı mide mukozasını daha da yakarak şiddetli '
                                                   'kramp ve kusmaya yol açtı.',
                                'teaching_point': 'Gastritte asitli ve tahriş edici gıdalar yasaklanmalıdır; asit '
                                                  'süpresyonu esastır.',
                                'text': 'Mideyi temizlemek amacıyla hastaya evde her gün bir bardak elma sirkesi ve '
                                        'limon suyu içirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Hafif gastrit için yapılan radikal cerrahi hastada kalıcı anatomik '
                                                   've beslenme sakatlığı yarattı.',
                                'teaching_point': 'NSAİİ gastriti medikal olarak tamamen iyileşir; cerrahinin yeri '
                                                  'kesinlikle yoktur.',
                                'text': 'Kanamayı durdurmak amacıyla 8 yaşındaki çocuğa acil cerrahi ile total '
                                        'gastrektomi operasyonu planlamak'}],
                 'question': 'İlaç ilişkili akut gastrit tanısı konulan bu hastada en uygun tedavi ve taburculuk planı '
                             'hangisidir?',
                 'stage_title': 'Tedavi Yönetimi ve Taburculuk Planı'}]}]
