# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Sarı Alan Vakaları (Part 2: S11 - S20)
"""

YELLOW_CASES_PART2 = [{'id': 'S11',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '8 Yaş',
  'gender': 'Erkek',
  'complaint': 'Göbek çevresinde başlayıp sağ alt kadrana yerleşen karın ağrısı, iştahsızlık, hafif ateş ve yürürken '
               'aksama',
  'history': "Ailesi 8 yaşındaki erkek çocuğu Sarı Alana getiriyor: 'Dün akşamüstü göbeğinin etrafında ağrı başladı, "
             'akşam yemeğini hiç yemedi, en sevdiği yiyeceklere bile bakmadı. Gece ağrısı sağ kasığına doğru kaydı ve '
             'sabah hafif ateşi (38.1°C) çıktı. Arabayla gelirken kasisten geçtiğimizde karnını tutarak bağırdı, '
             "yürürken sağ bacağını hafif bükerek aksıyor ve öksürünce sağ alt karnı ağrıyor.'",
  'final_diagnosis': 'Akut Apandisit (Komplike Olmamış Akut Flegmonöz Apandisit)',
  'disposition': 'Sarı Alanda İV Sıvı + Analjezi + Preoperatif Antibiyotik + Çocuk Cerrahisi Konsültasyonu ile Acil '
                 'Operasyona Yatış',
  'case_pearl': 'Çocuklarda akut cerrahi batının en sık nedeni akut apandisittir. Periumbilikal başlayıp sağ alt '
                'kadrana (McBurney noktası) göç eden ağrı, anoreksi, sarsıntıyla artan peritoneal irritasyon ve psoas '
                'irritasyonuna bağlı sağ kalça fleksiyonu tipiktir. Uygun analjezi (İV parasetamol veya düşük doz '
                'opioid) peritoneal bulguları maskelemez; aksine istemli savunmayı azaltarak muayene güvenilirliğini '
                'artırır. ALARA prensibi gereği çocuklarda ilk tercih görüntüleme ultrasonografidir (komprese '
                'edilemeyen, dış çapı >6 mm, kör sonlanan aperistaltik tübüler yapı).',
  'steps': [{'stage_title': 'Sarı Alanda İlk Değerlendirme ve Akut Batın Muayenesi',
             'question': 'Sağ alt kadrana yer değiştiren karın ağrısı ve yürürken aksaması olan 8 yaşındaki bu çocukta '
                         'ilk muayene ve semptomatik yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Vital bulguları ve batın muayenesini tamamladıktan sonra cerrahi konsültasyon '
                                  'öncesinde peritonit bulgularını maskelememek amacıyla hiçbir analjezik vermeden '
                                  'yalnızca damar yolu açıp izotonik sıvı başlamak',
                          'is_correct': False,
                          'scenario_update': 'Ağrısı dindirilmeyen çocukta şiddetli ajitasyon ve yaygın istemli karın '
                                             'kasılması devam ettiği için lokalize peritoneal irritasyon bulgularını '
                                             'net değerlendirmek güçleşti.',
                          'teaching_point': 'Akut karın ağrılı çocuklarda intravenöz parasetamol veya uygun doz '
                                            'analjezik verilmesi cerrahi muayeneyi bozmaz; aksine anksiyete kaynaklı '
                                            'istemli defansı azaltarak gerçek peritoneal bulguların saptanmasını '
                                            'kolaylaştırır.'},
                         {'text': 'Vital bulguları ölçmek, sağ alt kadran defans ve rebound varlığını, psoas bulgusunu '
                                  've skrotal muayeneyi değerlendirip ağrı için intravenöz parasetamol uygulamak',
                          'is_correct': True,
                          'explanation': 'Akut batın şüphesinde vital bulgular, lokalize peritoneal irritasyon ve '
                                         'psoas bulgusu sistematik değerlendirilmeli; erkek çocuklarda yansıyan '
                                         'skrotal patolojiler mutlaka dışlanmalı ve erken analjezi sağlanmalıdır.',
                          'new_finding': 'Vital bulgular: Ateş 38.2°C, KTA 112/dk, SS 22/dk, TA 105/65 mmHg. Sağ alt '
                                         'kadranda belirgin lokalize hassasiyet, istemli defans ve pozitif rebound '
                                         'mevcut. Sağ uyluk ekstansiyonunda ağrı artıyor (pozitif psoas bulgusu). '
                                         'Bilateral skrotum ve testisler doğal, kremaster refleksi intakt. İntravenöz '
                                         'parasetamol sonrası ajitasyon azaldı ancak sağ alt kadran hassasiyeti devam '
                                         'etti.'},
                         {'text': 'Batın muayenesinde sağ alt kadran hassasiyetini saptadıktan sonra bağırsak pasajını '
                                  'rahatlatıp gaz sancısını dışlamak amacıyla rektal gliserinli lavman uygulayarak iki '
                                  'saat gözlemlemek',
                          'is_correct': False,
                          'scenario_update': 'Rektal lavman uygulaması intraluminal basıncı artırarak çocuğun sağ alt '
                                             'kadran ağrısını ve peritoneal irritasyon bulgularını belirgin şekilde '
                                             'şiddetlendirdi.',
                          'teaching_point': 'Lokalize peritoneal irritasyon bulguları, ateş ve anoreksisi olan akut '
                                            'batın şüpheli çocuklarda intraluminal basıncı ve perforasyon riskini '
                                            'artıran lavman veya laksatif uygulamaları kontrendikedir.'},
                         {'text': 'Çocuğun yürürken sağ bacağını bükerek aksamasını ve subfebril ateşini ön planda '
                                  'tutarak kalça eklemi muayenesine odaklanıp batın palpasyonunu ortopedi '
                                  'değerlendirmesi sonrasına bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Kalça eklem hareketleri pasif rotasyonda açık olmasına rağmen '
                                             'retroçekal/pelvik inflamasyonun psoas kası irritasyonu gözden kaçırıldı '
                                             've batın değerlendirmesi gecikti.',
                          'teaching_point': 'Retroçekal yerleşimli sağ alt kadran inflamasyonları iliopsoas kasını '
                                            'irrite ederek sağ kalçada antaljik fleksiyon ve yürüme güçlüğü yapabilir; '
                                            'bu tablo primer kalça patolojisi ile karıştırılmamalıdır.'}]},
            {'stage_title': 'Laboratuvar Tetkikleri ve İlk Basamak Görüntüleme Seçimi',
             'question': 'Lokalize sağ alt kadran peritoneal irritasyon bulguları ve psoas pozitifliği saptanan bu '
                         'hastada tanısal tetkik ve görüntüleme planınız nasıl olmalıdır?',
             'options': [{'text': 'Oral alımı kesip intravenöz hidrasyon başlayarak hemogram, CRP ve tam idrar tetkiki '
                                  'göndermek; görüntüleme olarak yalnızca ayakta direkt batın grafisi çekip hava-sıvı '
                                  'seviyesi aramak',
                          'is_correct': False,
                          'scenario_update': 'Ayakta direkt batın grafisinde sağ alt kadranda nonspesifik birkaç gaz '
                                             'gölgesi dışında tanısal bulgu saptanmadı ve kesin tanı için zaman '
                                             'kaybedildi.',
                          'teaching_point': 'Direkt batın grafisinin akut sağ alt kadran patolojilerinde duyarlılığı '
                                            've özgüllüğü çok düşüktür; mekanik obstrüksiyon veya serbest hava şüphesi '
                                            'dışında rutin ilk basamak görüntüleme olarak önerilmez.'},
                         {'text': 'Ultrasonografinin kullanıcı bağımlı olması ve gaz süperpozisyonu riski nedeniyle '
                                  'zaman kaybetmeden doğrudan intravenöz kontrastlı alt-üst abdomen bilgisayarlı '
                                  'tomografisi çekerek kesin anatomik görüntüleme sağlamak',
                          'is_correct': False,
                          'scenario_update': "BT'de sağ alt kadranda 8.5 mm çaplı inflamatuar tübüler yapı gösterildi "
                                             'ancak 8 yaşındaki çocuk ultrasonografi ile kolayca konulabilecek bir '
                                             'tanı için yüksek doz iyonizan radyasyona maruz kaldı.',
                          'teaching_point': 'Pediatrik yaş grubunda ALARA prensibi gereği sağ alt kadran ağrısında ilk '
                                            'basamak görüntüleme her zaman kademeli kompresyon ultrasonografisidir; BT '
                                            'yalnızca ultrasonografinin sonuçsuz kaldığı seçilmiş olgularda '
                                            'düşünülür.'},
                         {'text': 'Oral alımı durdurup intravenöz izotonik sıvı başlamak; tam kan sayımı, CRP ve tam '
                                  'idrar tetkiki göndererek ilk basamak görüntüleme olarak batın ultrasonografisi '
                                  'istemek',
                          'is_correct': True,
                          'explanation': 'Olası cerrahi girişim hazırlığı için oral alım kapatılıp İV hidrasyon '
                                         'başlanmalı; inflamatuar belirteçler, üriner patolojileri dışlamak için TİT '
                                         've radyasyon içermeyen batın ultrasonografisi istenmelidir.',
                          'new_finding': 'Laboratuvar: Lökosit 15.800/mm³ (%84 nötrofil), CRP 42 mg/L, tam idrar '
                                         'tetkikinde lökosit ve eritrosit yok, dansite 1022. Ultrasonografi: Sağ alt '
                                         'kadranda komprese edilemeyen, kör sonlanan, aperistaltik, duvar kalınlığı '
                                         'artmış, dış çapı 8.5 mm ölçülen tübüler intestinal yapı, çevresinde '
                                         'hiperekojen mezenterik yağ dokusu ve minimal serbest sıvı izlendi.',
                          'image': 'assets/images/usg_appendicitis.png'},
                         {'text': 'Kan ve idrar tetkiklerini gönderdikten sonra radyolojik görüntüleme istemeden önce '
                                  'on iki saatlik seri batın muayenesi ve lökosit takibi ile klinik seyri izlemek',
                          'is_correct': False,
                          'scenario_update': 'Lökosit 15.800/mm³ ve CRP 42 mg/L gelmesine rağmen görüntüleme '
                                             "ertelenince takip sürecinde ateş 39.1°C'ye yükseldi ve peritoneal "
                                             'irritasyon tüm alt batına yayıldı.',
                          'teaching_point': 'Tipik klinik öykü, lokalize rebound ve yüksek akut faz yanıtı bulunan '
                                            'hastalarda ultrasonografi geciktirilmemeli; seri gözlem yalnızca '
                                            'düşük-orta riskli ve görüntülemesi şüpheli olgularda tercih '
                                            'edilmelidir.'}]},
            {'stage_title': 'Klinik ve Radyolojik Bulgularla Kesin Tanı',
             'question': 'Sağ alt kadran peritoneal irritasyon bulguları, nötrofilik lökositoz ve ultrasonografide 8.5 '
                         'mm çaplı komprese edilemeyen kör uçlu tübüler yapı saptanan hastada kesin tanınız nedir?',
             'options': [{'text': 'Akut komplike olmamış flegmonöz apandisit',
                          'is_correct': True,
                          'explanation': 'Periumbilikal başlayıp sağ alt kadrana yerleşen ağrı, anoreksi, nötrofilik '
                                         'lökositoz ve ultrasonografide >6 mm komprese edilemeyen kör sonlanan '
                                         'apendiks görünümü akut apandisit tanısını kesinleştirir.',
                          'new_finding': 'Kesin tanı: Akut komplike olmamış apandisit. Hastada serbest perforasyon '
                                         'veya apse formasyonu saptanmadı.'},
                         {'text': 'Akut mezenterik lenfadenit ve terminal ileit',
                          'is_correct': False,
                          'scenario_update': 'Mezenterik lenfadenitte apendiks normal çapta (<6 mm) ve komprese '
                                             'edilebilir görünümde olup mezenterde kümelenmiş reaktif lenf nodları '
                                             'izlenir.',
                          'teaching_point': "Ultrasonografide dış çapı 6 mm'yi aşan, aperistaltik ve basıyla komprese "
                                            'olmayan kör uçlu yapı varlığında tanı mezenterik lenfadenit değil akut '
                                            'apandisittir.'},
                         {'text': 'Komplike olmayan akut çekal divertükülit',
                          'is_correct': False,
                          'scenario_update': 'Çekal divertükülit pediatrik yaş grubunda son derece nadirdir ve '
                                             'ultrasonografide normal apendiks yanında çekum duvarından kaynaklanan '
                                             'fokal keseleşme olarak görülür.',
                          'teaching_point': 'Çocuklarda sağ alt kadranın kör sonlanan tübüler inflamasyonu aksi '
                                            'kanıtlanmadıkça akut apandisittir.'},
                         {'text': 'Enfekte Meckel divertikülü (Meckel divertiküliti)',
                          'is_correct': False,
                          'scenario_update': 'Meckel divertiküliti klinik olarak benzer tablo yapabilse de '
                                             'ultrasonografide sağ alt kadranda tipik kör sonlanan apendiks '
                                             'inflamasyonu saptanmıştır.',
                          'teaching_point': 'Ultrasonografide anatomik olarak sağ iliak fossada komprese olmayan '
                                            'şişmiş apendiksin doğrudan görüntülenmesi akut apandisit tanısını '
                                            'doğrular.'}]},
            {'stage_title': 'Preoperatif Hazırlık ve Cerrahi Yönetim Planı',
             'question': 'Akut apandisit tanısı kesinleşen 8 yaşındaki bu hastanın Sarı Alandaki preoperatif hazırlık '
                         've nihai yönetim planı nasıl olmalıdır?',
             'options': [{'text': 'Oral alımı kapatıp sadece intravenöz sıvı ve analjezi ile hastayı ameliyathaneye '
                                  'devretmek; profilaktik antibiyotiği cerrahi ekip batını açtıktan sonra '
                                  'intraoperatif dönemde başlamak',
                          'is_correct': False,
                          'scenario_update': 'Preoperatif antibiyotik dozu insizyondan önce verilmediği için '
                                             'postoperatif dönemde cerrahi alan enfeksiyonu riski anlamlı derecede '
                                             'arttı.',
                          'teaching_point': 'Akut apandisitte cerrahi alan enfeksiyonu ve intraabdominal apse '
                                            'gelişimini azaltmak için gram-negatif ve anaerob spektrumlu intravenöz '
                                            'antibiyotik profilaksisi cerrahi insizyondan 30-60 dakika önce '
                                            'başlanmalıdır.'},
                         {'text': 'Perforasyon bulgusu olmadığı için cerrahi konsültasyon istemeden intravenöz '
                                  'seftriakson ve metronidazol başlayarak hastayı kırk sekiz saat acil gözlem '
                                  'ünitesinde medikal olarak izlemek',
                          'is_correct': False,
                          'scenario_update': 'Cerrahi ekip değerlendirmesi olmaksızın acil gözlemde tutulan hastada '
                                             '18. saatte artan karın ağrısı ve perfore apandisit tablosu gelişti.',
                          'teaching_point': 'Çocuklarda akut apandisitin standart tedavisi apendektomidir; seçilmiş '
                                            'olgularda non-operatif yönetim dahi mutlaka çocuk cerrahisi konsültasyonu '
                                            've servis yatışı altında yürütülür.'},
                         {'text': 'Oral amoksisilin-klavulanat ve analjezik reçete ederek hastayı ayaktan çocuk '
                                  'cerrahisi poliklinik kontrolüne yönlendirmek ve ateş yükselirse tekrar acil servise '
                                  'başvurmasını tembihleyerek taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Taburcu edilen hasta 24 saat sonra yaygın peritonit, yüksek ateş ve '
                                             'septik görünümle acil servise tekrar getirildi.',
                          'teaching_point': 'Akut apandisit tanısı alan hiçbir hasta acil servisten oral antibiyotikle '
                                            'taburcu edilemez; acil cerrahi yatış ve müdahale şarttır.'},
                         {'text': 'Oral alımı kapatıp intravenöz sıvıyı sürdürmek, gram-negatif ve anaerob etkili '
                                  'intravenöz antibiyotik profilaksisi başlayarak acil apendektomi için çocuk '
                                  'cerrahisine devretmek',
                          'is_correct': True,
                          'explanation': 'Komplike olmamış akut apandisitte oral stop, İV hidrasyon, uygun preoperatif '
                                         'İV antibiyotik (örn. sefazolin + metronidazol veya ampisilin-sulbaktam) ve '
                                         'acil apendektomi standart yaklaşımdır.',
                          'new_finding': 'Çocuk cerrahisi konsültasyonu ile hasta ameliyathaneye devredildi; '
                                         'preoperatif antibiyotik profilaksisi altında başarılı laparoskopik '
                                         'apendektomi yapıldı ve hasta komplikasyonsuz taburcu edildi.'}]}]},
 {'id': 'S12',
  'category': '🫁 Hırıltı & Solunum Sıkıntısı',
  'age': '5 Aylık',
  'gender': 'Erkek',
  'complaint': 'Burun akıntısı sonrası başlayan hızlı nefes alma, göğüs kafesinde çekilmeler, hırıltı ve memeyi '
               'emememe',
  'history': "Annesi 5 aylık erkek bebeği Sarı Alana getiriyor: 'Üç gün önce hafif burun tıkanıklığı ve hapşırıkla "
             'başladı. Dün gece öksürüğü arttı, bu sabahtan beri göğsü körük gibi hızlı inip kalkıyor, nefes alırken '
             'kaburgalarının altı içeri çöküyor ve hırıltısı dışarıdan duyuluyor. Memeyi ağzına alıyor ama nefes '
             "nefese kalıp hemen bırakıyor, son 8 saattir neredeyse hiç ememedi ve bezi kuru kaldı.'",
  'final_diagnosis': 'Akut Viral Bronşiyolit (Orta-Ağır Şiddette - RSV Enfeksiyonu)',
  'disposition': 'Sarı Alanda Yüzeyel Nazal Aspirasyon + Nemlendirilmiş Oksijen + İV Hidrasyon Sonrası Pediatri '
                 'Servisine Yatış',
  'case_pearl': 'Akut viral bronşiyolit 2 yaş altı çocuklarda en sık alt solunum yolu enfeksiyonudur (en sık etken '
                'RSV). Patofizyolojide bronkospazmdan ziyade bronşiyol lümeninde mukus tıkacı, epitel nekrozu ve ödem '
                'bulunduğundan AAP ve güncel kılavuzlara göre rutin bronkodilatör (salbutamol), sistemik/inhale '
                'kortikosteroid, antibiyotik ve rutin akciğer grafisi önerilmez. Tedavinin kanıtlanmış üç temel taşı: '
                'yüzeyel nazal aspirasyon, hipoksemi (SpO2 <%90-92) varlığında nemlendirilmiş oksijen ve oral alımı '
                'bozulan/takipneik (SS >60/dk) bebekte NG veya İV hidrasyon desteğidir.',
  'steps': [{'stage_title': 'Sarı Alanda Solunum Değerlendirmesi ve Klinik Ciddiyet Tayini',
             'question': 'Üst solunum yolu enfeksiyonu bulgularını takiben hızlı nefes alma, çekilmeler ve beslenememe '
                         'ile başvuran 5 aylık bebekte ilk değerlendirmeniz nasıl olmalıdır?',
             'options': [{'text': 'Muayeneyi tamamlamadan önce hava yolu ödemini ve spazmını hızla çözmek amacıyla '
                                  'bebeğe ardışık üç doz nebulize salbutamol ve intravenöz metilprednizolon uygulamak',
                          'is_correct': False,
                          'scenario_update': "Uygulanan nebulize beta-agonist sonrası bebeğin kalp hızı 195/dk'ya "
                                             'yükseldi ve ajitasyonu arttı; ancak solunum sayısı ve çekilmelerinde '
                                             'anlamlı düzelme olmadı.',
                          'teaching_point': 'Süt çocuklarının ilk viral alt solunum yolu hırıltı atağında patoloji '
                                            'bronkospazm değil mukus ödemi ve hücresel debristir; rutin bronkodilatör '
                                            've sistemik steroid tedavisi önerilmez.'},
                         {'text': 'Bebeğin 8 saattir ememediğini dikkate alarak solunum muayenesinden önce '
                                  'hipoglisemiyi önlemek için annenin kucağında biberonla formül mama içirip beslenme '
                                  'toleransını görmek',
                          'is_correct': False,
                          'scenario_update': "Dakikada 60'ın üzerinde nefes alan bebek biberonla beslenmeye "
                                             'çalışılırken öksürük krizi, desatürasyon ve aspirasyon tehlikesi '
                                             'geçirdi.',
                          'teaching_point': 'Belirgin takipnesi (solunum sayısı >60/dk) ve çekilmeleri olan süt '
                                            'çocuklarında yutma-solunum koordinasyonu bozulduğundan aspirasyon riski '
                                            'yüksektir; önce solunum stabilize edilmelidir.'},
                         {'text': 'Pediatrik Değerlendirme Üçgeni, vital bulgular, oda havası oksijen satürasyonu, '
                                  'solunum iş yükü, bilateral akciğer oskültasyonu ve hidrasyon durumunu sistematik '
                                  'değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Alt solunum yolu obstrüksiyonu ile başvuran süt çocuğunda hastalık şiddeti; '
                                         'takipne derecesi, retraksiyonlar, oda havası SpO2 düzeyi ve '
                                         'hidrasyon/beslenme durumu ile klinik olarak belirlenir.',
                          'new_finding': 'Vital bulgular: Ateş 37.9°C, KTA 158/dk, SS 64/dk, oda havasında SpO2 %89. '
                                         'Muayenede belirgin subkostal ve interkostal çekilmeler, burun kanadı '
                                         'solunumu, bilateral yaygın ekspiratuar hırıltı (wheezing) ve bazallerde ince '
                                         'krepitan raller saptandı. Ağız mukozası hafif kuru, ön fontanel normal '
                                         'bombelikte, kapiller dolum zamanı 2 saniye.'},
                         {'text': 'Solunum sıkıntısının nedenini netleştirmek için fizik muayene ve oksijen '
                                  'satürasyonu ölçümünü bekletip bebeği doğrudan radyoloji ünitesine iki yönlü akciğer '
                                  'grafisine göndermek',
                          'is_correct': False,
                          'scenario_update': 'Oda havasında hipoksemik (%89) olan bebek oksijen desteği verilmeden '
                                             'radyolojiye gönderildiği için işlem sırasında siyanoz gelişti ve grafide '
                                             'yalnızca nonspesifik havalanma artışı görüldü.',
                          'teaching_point': 'Hipoksemik ve solunum sıkıntılı bebek stabilize edilmeden görüntülemeye '
                                            'gönderilmez; ayrıca tipik viral alt solunum yolu hırıltısında rutin '
                                            'akciğer grafisi gereksiz antibiyotik kullanımını artırdığı için '
                                            'önerilmez.'}]},
            {'stage_title': 'İlk Basamak Acil Destek Tedavisi ve Tetkik Planı',
             'question': 'Oda havasında SpO2 %89, solunum sayısı 64/dk olan ve oral beslenemeyen bu 5 aylık bebekte '
                         'kılavuzlara uygun ilk müdahaleniz ne olmalıdır?',
             'options': [{'text': 'Serum fizyolojik ile yüzeyel nazal aspirasyon uygulamak, nemlendirilmiş oksijenle '
                                  'satürasyonu %90-92 üzerinde tutmak ve oral alımı kesip intravenöz izotonik sıvı '
                                  'başlamak',
                          'is_correct': True,
                          'explanation': 'Küçük süt çocukları zorunlu burun soluyucusu olduğundan nazal pasajın '
                                         'açılması solunum iş yükünü belirgin azaltır; SpO2 <%90-92 ise oksijen ve SS '
                                         '>60/dk olup beslenemiyorsa İV/NG hidrasyon temel tedavidir.',
                          'new_finding': 'Yüzeyel nazal aspirasyon sonrası üst hava yolu pasajı rahatladı. Nazal '
                                         'kanülle 1.5 L/dk nemlendirilmiş oksijen altında SpO2 %95 düzeyine yükseldi, '
                                         'solunum sayısı 54/dk oldu. Damar yolu açılarak %5 dekstrozlu %0.9 NaCl idame '
                                         'sıvısı başlandı; rutin laboratuvar ve radyolojik tetkik istenmedi.'},
                         {'text': 'Rutin akciğer grafisi, tam kan sayımı ve kan kültürü göndererek ikincil bakteriyel '
                                  'enfeksiyon profilaksisi için ampirik intravenöz seftriakson ve nebulize budesonid '
                                  'başlamak',
                          'is_correct': False,
                          'scenario_update': 'Hemogramda lökosit 9.800/mm³ (lenfosit hakimiyeti), grafide '
                                             'peribronşiyal kalınlaşma ve hiperinflasyon saptandı; verilen antibiyotik '
                                             've inhale steroid klinik tabloda hiçbir iyileşme sağlamadı.',
                          'teaching_point': 'Viral alt solunum yolu obstrüksiyonunda eşlik eden bakteriyel enfeksiyon '
                                            'oranı çok düşüktür (<%1-2); yüksek ateş, toksik görünüm veya fokal '
                                            'konsolidasyon yoksa rutin laboratuvar, grafi ve antibiyotik endike '
                                            'değildir.'},
                         {'text': 'Nazal aspirasyon yapmadan doğrudan yüksek doz nebulize salbutamol ve ipratropium '
                                  'bromür kombinasyonu başlayarak yanıt alınamazsa intravenöz magnezyum sülfat '
                                  'infüzyonuna hızla geçmek',
                          'is_correct': False,
                          'scenario_update': 'Üst hava yolundaki yoğun mukus temizlenmediği ve oksijen verilmediği '
                                             'için SpO2 %88 düzeyinde kaldı; antikolinerjik ve magnezyum tedavisi '
                                             'sekresyonları koyulaştırıp taşikardi yaptı.',
                          'teaching_point': 'Süt çocuklarında ipratropium bromür ve magnezyum sülfatın viral küçük '
                                            'hava yolu obstrüksiyonunda yeri yoktur; öncelik nazal temizlik ve '
                                            'oksijenizasyondur.'},
                         {'text': 'Bebeği sakinleştirmek ve öksürük nöbetlerini azaltmak amacıyla oral antihistaminik '
                                  've dekstrometorfan içeren şurup vererek oksijen desteği olmadan iki saat boyunca '
                                  'izlemek',
                          'is_correct': False,
                          'scenario_update': 'Verilen sedatif ve antitussif şurup sonrasında bebeğin öksürük refleksi '
                                             'baskılandı, mukus tıkaçları arttı ve solunum depresyonu ile desatürasyon '
                                             'gelişti.',
                          'teaching_point': 'Süt çocukları ve küçük çocuklarda öksürük kesici (antitussif) ve '
                                            'antihistaminik preparatlar mukus klirensini bozup apne ve solunum '
                                            'depresyonu yaptığı için kesinlikle kontrendikedir.'}]},
            {'stage_title': 'Klinik Bulgular Doğrultusunda Tanı',
             'question': 'Süt çocuğunda prodromal rinit sonrası gelişen ilk hırıltı atağı, takipne, çekilmeler ve '
                         'yaygın ekspiratuar wheezing ile krepitan raller hangi tanıyı gösterir?',
             'options': [{'text': 'Fokal bakteriyel lobar pnömoni',
                          'is_correct': False,
                          'scenario_update': 'Bakteriyel lobar pnömonide yüksek ateş, toksik görünüm ve oskültasyonda '
                                             'tek taraflı fokal krepitasyon veya solunum seslerinde azalma beklenir.',
                          'teaching_point': 'ÜSYE prodromu sonrası bilateral yaygın ekspiratuar wheezing ve '
                                            'sibilan/krepitan raller bakteriyel lobar pnömoniden ziyade yaygın '
                                            'bronşiyoler tutulumu gösterir.'},
                         {'text': 'Akut orta-ağır viral bronşiyolit',
                          'is_correct': True,
                          'explanation': 'İki yaş altı çocukta viral ÜSYE prodromunu izleyen ilk wheezing atağı, '
                                         'takipne, retraksiyonlar ve ince raller akut viral bronşiyolit tanısını '
                                         'koydurur; tanı kliniktir.',
                          'new_finding': 'Kesin tanı: Akut Viral Bronşiyolit (Orta-Ağır Şiddette).'},
                         {'text': 'Akut viral laringotrakeobronşit (krup)',
                          'is_correct': False,
                          'scenario_update': 'Krup sendromunda havlar tarzda öksürük, ses kısıklığı ve inspiratuar '
                                             'stridor ön plandadır; bu bebekte ise ekspiratuar hırıltı ve alt solunum '
                                             'yolu bulguları mevcuttur.',
                          'teaching_point': 'İnspiratuar stridor ekstratorasik üst hava yolu darlığını, ekspiratuar '
                                            'wheezing ve ince raller ise intratorasik alt hava yolu (bronşiyol) '
                                            'darlığını işaret eder.'},
                         {'text': 'Boğmaca (Bordetella pertussis) pnömonisi',
                          'is_correct': False,
                          'scenario_update': 'Boğmacada paroksismal boğulur tarzda öksürük nöbetleri, inspiratuar '
                                             "'whoop' sesi, öksürük sonrası kusma ve belirgin lenfositoz görülür.",
                          'teaching_point': 'Akut başlayan rinit sonrası yaygın ekspiratuar wheezing ve raller tipik '
                                            'viral bronşiyolit tablosudur.'}]},
            {'stage_title': 'Klinik İzlem Yanıtı ve Yatış Kararı',
             'question': "Sarı Alanda 4 saatlik izlemde oksijen kesildiğinde SpO2'si %89'a düşen, solunum sayısı 56/dk "
                         'olan ve emmeyi sürdüremeyen 5 aylık bebeğin yönetim kararı ne olmalıdır?',
             'options': [{'text': 'Nebulize %3 hipertonik salin ve evde kullanmak üzere salbutamol inhaler reçete '
                                  'ederek aileyi ertesi gün poliklinik kontrolüne çağırmak üzere taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Evde oksijen desteği alamayan ve beslenemeyen bebek gece saatlerinde '
                                             'derin hipoksemi ve dehidratasyon tablosuyla acil servise geri getirildi.',
                          'teaching_point': 'Oda havasında SpO2 <%90-92 olan (oksijen bağımlılığı süren) ve oral alımı '
                                            'yetersiz olan bronşiyolitli bebekler kesin yatış endikasyonu taşır; eve '
                                            'taburcu edilemez.'},
                         {'text': 'Bebeğe tek doz intramusküler deksametazon ve seftriakson uyguladıktan sonra oksijen '
                                  'satürasyonu %90 sınırına yaklaştığı için evde anne sütüyle beslenmek üzere '
                                  'göndermek',
                          'is_correct': False,
                          'scenario_update': 'Parenteral steroid ve antibiyotik bronşiyolit seyrini değiştirmedi; evde '
                                             'ememeyen bebekte hipoksemi ve solunum yorgunluğu ilerledi.',
                          'teaching_point': 'Bronşiyolitte parenteral steroid ve antibiyotik uygulayarak hastayı '
                                            'taburcu etmek kılavuzlara aykırıdır; hipoksemi ve beslenme bozukluğu '
                                            'servis yatışı gerektirir.'},
                         {'text': 'Mevcut klinik tabloyu ağır solunum yetmezliği kabul ederek bebeği derhal entübe '
                                  'edip mekanik ventilasyon desteği için çocuk yoğun bakım ünitesine yatırmak',
                          'is_correct': False,
                          'scenario_update': "Düşük akımlı nazal oksijenle SpO2'si %95 olan ve apnesi bulunmayan "
                                             'bebeğe gereksiz endotrakeal entübasyon uygulanması barotravma ve '
                                             'ventilatör ilişkili komplikasyonlara yol açtı.',
                          'teaching_point': 'Düşük akımlı nazal kanül oksijen ile satürasyonu düzelen, apnesi veya '
                                            'ağır hiperkapnik solunum yetmezliği olmayan orta-ağır bronşiyolit '
                                            'olguları genel pediatri servisinde izlenir.'},
                         {'text': 'Devam eden oksijen ihtiyacı, takipne ve beslenme yetersizliği nedeniyle bebeği '
                                  'nemlendirilmiş oksijen, nazal temizlik ve hidrasyon takibi için pediatri servisine '
                                  'yatırmak',
                          'is_correct': True,
                          'explanation': 'Bronşiyolitte oda havasında SpO2 <%90-92 olması, belirgin takipne/çekilme ve '
                                         "oral alımın <%50'ye düşmesi pediatri servisine yatışın temel kriterleridir.",
                          'new_finding': 'Bebek pediatri servisine yatırıldı; nemlendirilmiş oksijen, aralıklı nazal '
                                         'aspirasyon ve İV/NG hidrasyon desteği ile 3. günde oksijen ihtiyacı kalmadı, '
                                         'aktif emmeye başladı ve şifayla taburcu edildi.'}]}]},
 {'id': 'S13',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '6 Yaş',
  'gender': 'Kız',
  'complaint': 'Bacaklarda ve kalçada basmakla solmayan kırmızı-mor döküntüler, diz ve ayak bileklerinde şişlik-ağrı '
               've aralıklı kıvrandıran karın ağrısı',
  'history': "Annesi 6 yaşındaki kızını Sarı Alana getiriyor: 'Yaklaşık 10 gün önce üst solunum yolu enfeksiyonu "
             'geçirmişti. Dün bacaklarında kırmızı lekeler belirdi, bugün lekeler çoğalarak ele gelen morumsu '
             'kabartılara dönüştü. Ayak bilekleri ve sağ dizi şişti, üzerine basamıyor. Ayrıca sabahtan beri '
             "aralıklarla karnını tutup iki büklüm kıvranarak ağlıyor; ağrı nöbet şeklinde gelip sonra hafifliyor.'",
  'final_diagnosis': 'Henoch-Schönlein Purpurası (HSP / IgA Vasküliti - Gastrointestinal, Eklem ve Renal Tutulumlu)',
  'disposition': 'Sarı Alanda Batın USG (İnvajinasyon Dışlama), TİT ve Böbrek Fonksiyon Testleri Sonrası Pediatri '
                 'Servisine Yatış',
  'case_pearl': 'Henoch-Schönlein Purpurası (IgA vasküliti), çocukluk çağının en sık sistemik küçük damar '
                'vaskülitidir. EULAR/PRINTO/PRES kriterlerine göre trombositopeni olmaksızın alt ekstremite/gluteal '
                'bölgede baskın palpabl purpura zorunlu kriterdir; buna artrit/artralji, kolik karın ağrısı/GİS '
                'kanaması ve renal tutulum (hematüri/proteinüri) eşlik eder. En önemli akut cerrahi komplikasyon '
                "bağırsak duvarı ödemi ve submukozal hematomun 'lead point' oluşturmasıyla gelişen ileo-ileal "
                'invajinasyondur (ultrasonografi ile dışlanır). Uzun dönem prognozu ise böbrek tutulumu belirler; tüm '
                'hastalar en az 6 ay TİT ve kan basıncı ile izlenmelidir.',
  'steps': [{'stage_title': 'Sarı Alanda Döküntü, Eklem ve Batın Muayenesi',
             'question': 'Alt ekstremitelerde döküntü, eklem şişliği ve kolik karın ağrısı ile başvuran 6 yaşındaki bu '
                         'çocukta ilk muayenede neleri değerlendirmelisiniz?',
             'options': [{'text': 'Döküntülerin kaşıntılı papüler karakterde olduğunu varsayarak yalnızca cilt '
                                  'yüzeyini incelemek ve eklem ağrısını büyüme ağrısına bağlayıp batın muayenesini '
                                  'sonraya ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Döküntülerin basmakla solmayan purpurik karakteri, hipertansiyon '
                                             'sınırındaki kan basıncı ve akut batın riski gözden kaçırıldı.',
                          'teaching_point': 'Alt ekstremitede basmakla solmayan purpura, periartiküler şişlik ve kolik '
                                            'karın ağrısı birlikteliği sistemik bir hastalığı gösterir; tam kan '
                                            'basıncı ve batın muayenesi zorunludur.'},
                         {'text': 'Döküntünün basmakla solup solmadığını ve ele gelip gelmediğini, alt ekstremite '
                                  'dağılımını, eklem şişliğini, kan basıncını ve batın bulgularını değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Yerçekimine bağımlı simetrik palpabl purpura, periartiküler ödem/artrit, '
                                         'olası nefrit için kan basıncı ölçümü ve akut batın komplikasyonları için '
                                         'karın muayenesi ilk adımda değerlendirilmelidir.',
                          'new_finding': 'Vital bulgular: TA 118/74 mmHg (yaş ve boya göre 90-95. persentil), KTA '
                                         '104/dk, Ateş 37.2°C. Bilateral alt ekstremite ekstansör yüzlerde ve gluteal '
                                         'bölgede simetrik, basmakla solmayan, ele gelen (palpabl) purpurik lezyonlar '
                                         'saptandı. Sağ diz ve sol ayak bileğinde periartiküler ödem ve hareket '
                                         'kısıtlılığı mevcut. Batında periumbilikal hassasiyet var, defans veya ele '
                                         'gelen kitle yok.'},
                         {'text': 'Yaygın purpurik döküntüleri akut trombositopenik kanama kabul ederek fizik '
                                  'muayeneyi bekletip hastaya derhal acil trombosit süspansiyonu ve taze donmuş plazma '
                                  'hazırlamak',
                          'is_correct': False,
                          'scenario_update': 'Laboratuvar sonucu görülmeden hazırlanan kan ürünleri gereksiz '
                                             'transfüzyon riski oluşturdu; oysa hastanın döküntüleri trombositopenik '
                                             'peteşi değil ele gelen palpabl purpuraydı.',
                          'teaching_point': 'Ele gelen (palpabl) ve yerçekimine bağımlı simetrik purpura '
                                            'trombositopeniden ziyade küçük damar inflamasyonunu düşündürür; hemogram '
                                            'görülmeden ve hayatı tehdit eden kanama olmadan trombosit verilmez.'},
                         {'text': 'Eklem şişliği ve yürüyememe yakınmasını ön planda tutarak septik artrit şüphesiyle '
                                  'sağ diz ekleminden acil yatak başı artrosentez işlemi uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Ateşi olmayan ve simetrik purpurik döküntüleri bulunan çocuğa yapılan '
                                             'invaziv eklem ponksiyonu gereksiz ağrı ve eklem içi kanama/enfeksiyon '
                                             'riski yarattı.',
                          'teaching_point': 'Alt ekstremite purpurasına eşlik eden gezici ve periartiküler ağırlıklı '
                                            'oligoartrit tablosu genellikle sekonder ve sekel bırakmayan inflamatuar '
                                            'karakterdedir; rutin artrosentez endike değildir.'}]},
            {'stage_title': 'Laboratuvar Tetkikleri ve Batın Görüntülemesi',
             'question': 'Simetrik palpabl purpura, artrit ve kolik karın ağrısı bulunan bu çocukta ayırıcı tanı ve '
                         'komplikasyon taraması için hangi tetkikleri istemelisiniz?',
             'options': [{'text': 'Yalnızca tam kan sayımı ve periferik yayma isteyerek trombosit sayısı normal '
                                  'gelirse idrar tetkiki veya batın görüntülemesi yapmadan hastayı izleme almak',
                          'is_correct': False,
                          'scenario_update': 'Trombosit sayısı 420.000/mm³ gelince ek tetkik yapılmadı; ancak hastanın '
                                             'mikroskopik hematürisi, proteinürisi ve bağırsak duvarı ödemi atlandı.',
                          'teaching_point': 'Palpabl purpura ve kolik karın ağrısı olan her çocukta trombosit sayısına '
                                            'ek olarak böbrek tutulumu için tam idrar tetkiki ve cerrahi '
                                            'komplikasyonlar için batın ultrasonografisi şarttır.'},
                         {'text': 'Kesin tanı koymak amacıyla acil serviste cilt punch biyopsisi ve kemik iliği '
                                  'aspirasyonu planlayarak batın ağrısı için direkt karın grafisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Tipik klinik bulguları olan hastaya gereksiz invaziv işlemler planlandı; '
                                             'direkt batın grafisi ise bağırsak duvarı ödemini ve olası invajinasyonu '
                                             'değerlendirmede yetersiz kaldı.',
                          'teaching_point': 'Tipik alt ekstremite palpabl purpurası ve normal trombosit sayısı olan '
                                            'çocuklarda tanı kliniktir; cilt veya kemik iliği biyopsisi yalnızca '
                                            'atipik prezentasyonlarda düşünülür.'},
                         {'text': 'Kan kültürü, lomber ponksiyon ve kraniyal bilgisayarlı tomografi isteyerek '
                                  'sonuçları beklemeden yüksek doz intravenöz seftriakson ve vankomisin tedavisi '
                                  'derhal başlamak',
                          'is_correct': False,
                          'scenario_update': 'Ateşi olmayan, genel durumu iyi ve hemodinamisi stabil olan çocuğa '
                                             'gereksiz lomber ponksiyon, radyasyon ve geniş spektrumlu antibiyotik '
                                             'uygulandı.',
                          'teaching_point': 'Genel durumu iyi, afebril ve lezyonları alt ekstremite-gluteal bölgeye '
                                            'sınırlı palpabl purpura olgularında santral sinir sistemi enfeksiyonu '
                                            'taraması ve ampirik antibiyotik endike değildir.'},
                         {'text': 'Tam kan sayımı, koagülasyon, üre-kreatinin, tam idrar tetkiki, gaitada gizli kan '
                                  'istemek ve akut komplikasyonlar için batın ultrasonografisi planlamak',
                          'is_correct': True,
                          'explanation': 'Trombositopeni ve koagülopatiyi dışlamak için CBC/koagülasyon, nefrit '
                                         'taraması için TİT ve üre/kreatinin, GİS tutulumu ve özellikle ileo-ileal '
                                         'invajinasyonu dışlamak için batın USG zorunludur.',
                          'new_finding': 'Laboratuvar: Lökosit 11.200/mm³, Hb 12.4 g/dL, Trombosit 420.000/mm³, PT ve '
                                         'aPTT normal. Tam idrar tetkikinde mikroskopik hematüri (her sahada 25-30 '
                                         'eritrosit) ve (+1) proteinüri saptandı. Üre 28 mg/dL, Kreatinin 0.52 mg/dL, '
                                         'gaitada gizli kan pozitif. Batın ultrasonografisinde ileal duvarlarda ödemli '
                                         'kalınlaşma izlendi, iç içe geçmiş bağırsak ansı (hedef görünümü) '
                                         'saptanmadı.'}]},
            {'stage_title': 'Klinik ve Laboratuvar Bulgularıyla Kesin Tanı',
             'question': 'Trombositopeni olmaksızın alt ekstremitede palpabl purpura, artrit, kolik karın ağrısı ve '
                         'mikroskopik hematüri saptanan hastanın kesin tanısı nedir?',
             'options': [{'text': 'Akut immün trombositopenik purpura (İTP)',
                          'is_correct': False,
                          'scenario_update': "İTP'de izole derin trombositopeni ve basmakla solmayan düz "
                                             'peteşiler/ekimozlar görülür; bu hastada trombosit sayısı 420.000/mm³ '
                                             'olup lezyonlar palpabldır.',
                          'teaching_point': 'Normal veya yüksek trombosit sayısı ile birlikte ele gelen purpura, '
                                            "artrit ve nefrit varlığı İTP'yi kesin olarak dışlar."},
                         {'text': 'Akut fulminan meningokoksemi ve sepsis',
                          'is_correct': False,
                          'scenario_update': 'Meningokoksemide yüksek ateş, toksik görünüm, hemodinamik instabilite, '
                                             'hızlı yayılan nekrotik purpura ve tüketim koagülopatisi bulunur.',
                          'teaching_point': 'Afebril, genel durumu iyi, normal koagülasyon ve trombosit değerlerine '
                                            'sahip simetrik alt ekstremite purpurası meningokoksemi değil küçük damar '
                                            'vaskülitidir.'},
                         {'text': 'Henoch-Schönlein purpurası (IgA vasküliti)',
                          'is_correct': True,
                          'explanation': 'Trombositopeni olmadan alt ekstremite baskın palpabl purpuraya eşlik eden '
                                         'artrit, kolik karın ağrısı (GİS tutulumu) ve hematüri/proteinüri (renal '
                                         'tutulum) EULAR/PRINTO/PRES tanı kriterlerini tam karşılar.',
                          'new_finding': 'Kesin tanı: Henoch-Schönlein Purpurası (IgA Vasküliti - GİS, Eklem ve Renal '
                                         'Tutulumlu).'},
                         {'text': 'Tipik hemolitik üremik sendrom (HÜS)',
                          'is_correct': False,
                          'scenario_update': 'HÜS tablosunda mikroanjiyopatik hemolitik anemi, belirgin trombositopeni '
                                             've akut böbrek hasarı triadı görülür; hastamızda Hb ve trombosit '
                                             'normaldir.',
                          'teaching_point': 'Hemoglobin, trombosit ve kreatinin değerlerinin normal olması hemolitik '
                                            'üremik sendromu dışlar.'}]},
            {'stage_title': 'Tedavi Planı ve Uzun Dönem Renal İzlem',
             'question': 'Gastrointestinal tutulumu, eklem ağrısı ve mikroskopik hematürisi olan 6 yaşındaki bu HSP '
                         'hastasının tedavi ve takip planı nasıl olmalıdır?',
             'options': [{'text': 'Şiddetli karın ağrısı için sistemik prednizolon (1-2 mg/kg/gün) ve parasetamol '
                                  'başlayıp servise yatırmak; en az altı ay idrar ve tansiyon izlemi planlamak',
                          'is_correct': True,
                          'explanation': 'Şiddetli kolik karın ağrısı ve submukozal bağırsak ödemi olan HSP '
                                         'olgularında kısa süreli sistemik kortikosteroid (1-2 mg/kg/gün '
                                         'prednizolon/metilprednizolon) semptomları hızla geriletir. Renal tutulum ilk '
                                         '4-6 haftada veya 6 aya kadar gelişebileceğinden düzenli TİT ve tansiyon '
                                         'izlemi zorunludur.',
                          'new_finding': 'Servis yatışı ve sistemik prednizolon tedavisi ile 24 saat içinde kolik '
                                         'karın ağrısı ve eklem şişliği geriledi. Hasta 6 aylık düzenli tam idrar '
                                         'tetkiki ve kan basıncı izlem planıyla pediatrik nefroloji takibine alındı.'},
                         {'text': 'Eklem ve karın ağrısını kontrol altına almak için yüksek doz oral ibuprofen '
                                  'başlayıp steroid vermeden hastayı bir ay sonra nefroloji poliklinik kontrolüne '
                                  'çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Verilen nonsteroid antiinflamatuar ilaç (ibuprofen) gastrointestinal '
                                             'mukoza kanamasını artırdı ve mevcut renal tutulum (hematüri/proteinüri) '
                                             'üzerinde nefrotoksik etki yarattı.',
                          'teaching_point': 'Aktif gastrointestinal tutulumu (gaitada gizli kan pozitifliği, şiddetli '
                                            'karın ağrısı) ve renal tutulumu (hematüri/proteinüri) olan HSP '
                                            "hastalarında NSAİİ'ler kontrendikedir; analjezi için parasetamol, "
                                            'şiddetli GİS ödemi için kortikosteroid tercih edilir.'},
                         {'text': 'Böbrek tutulumunun ilerlemesini kesin olarak engellemek amacıyla tüm hastalarda '
                                  'rutin uygulanan intravenöz siklofosfamid ve plazmaferez protokolünü acil serviste '
                                  'derhal ve gecikmeden başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Kreatinini normal ve yalnızca hafif mikroskopik hematürisi olan hastaya '
                                             'uygulanan ağır immünsüpresif tedavi kemik iliği baskılanması ve '
                                             'enfeksiyon riskine yol açtı.',
                          'teaching_point': 'Siklofosfamid, azatioprin veya plazmaferez gibi agresif tedaviler '
                                            'yalnızca biyopsi ile kanıtlanmış kresentik glomerülonefrit, hızlı '
                                            'ilerleyen nefrit veya nefrotik düzeyde dirençli proteinüride endikedir.'},
                         {'text': 'Batın ultrasonografisinde invajinasyon saptanmadığı için hiçbir medikal tedavi '
                                  'başlamadan hastayı taburcu etmek ve yalnızca cilt döküntüleri tekrarlarsa '
                                  'polikliniğe başvurmasını aileye önermek',
                          'is_correct': False,
                          'scenario_update': 'Şiddetli karın ağrısı ve oral alım güçlüğü olan çocuk evde dehidrate '
                                             'kaldı; ayrıca idrar takibi yapılmadığı için ilerleyen nefrit tablosu geç '
                                             'fark edildi.',
                          'teaching_point': 'Şiddetli karın ağrısı olan HSP hastaları oral alım ve cerrahi '
                                            'komplikasyon (invajinasyon) takibi için yatırılmalı; döküntüler tamamen '
                                            'geçse bile en az 6 ay boyunca TİT ve kan basıncı izlemi '
                                            'sürdürülmelidir.'}]}]},
 {'id': 'S14',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '4 Yaş',
  'gender': 'Erkek',
  'complaint': 'Göğsünde kuş çırpınması hissi, aniden başlayan kalp çarpıntısı, halsizlik ve hafif solukluk',
  'history': "Annesi 4 yaşındaki oğlunu Sarı Alana getiriyor: 'Parkta oynarken birden yanıma geldi, anne kalbim "
             'göğsümden fırlayacak gibi atıyor, içeride kuş çırpınıyor dedi. Elimi göğsüne koyduğumda sayamayacağım '
             'kadar hızlı çarptığını fark ettim. Yaklaşık 45 dakikadır hiç durmadan aynı hızda devam ediyor. Rengi '
             "hafif soldu ve halsizleşti. Ateşi, kusması, ishali veya bilinen bir kalp hastalığı yok.'",
  'final_diagnosis': 'Paroksismal Supraventriküler Taşikardi (SVT - Hemodinamik Olarak Stabil)',
  'disposition': 'Sarı Alanda Otonomik Manevra / Hızlı İV Adenozin Puşe ile Sinüs Ritmine Döndürme, Kontrol EKG ve '
                 'Pediatrik Kardiyoloji Konsültasyonu',
  'case_pearl': 'Supraventriküler Taşikardi (SVT), çocukluk çağının en sık semptomatik taşiaritmisidir. Süt '
                'çocuklarında KTA >220/dk, çocuklarda >180/dk olup R-R aralıkları tamamen sabittir, P dalgaları '
                'seçilemez/retrograddır ve QRS dardır (<0.09 sn). Hemodinamik olarak stabil hastada ilk adım vagal '
                'manevradır (küçük çocukta yüze 10-15 sn buz torbası; göz küresi basısı ve karotis masajı '
                'kontrendikedir!). Yanıtsızsa kalbe yakın antekübital damar yolundan üç yollu muslukla hızlı İV '
                'adenozin (ilk doz 0.1 mg/kg, maks 6 mg; ikinci doz 0.2 mg/kg, maks 12 mg) ve hemen ardından 5-10 mL '
                'SF puşe uygulanır. Sinüs ritmine döndükten sonra WPW (delta dalgası) açısından mutlaka 12 '
                'derivasyonlu kontrol EKG çekilmelidir.',
  'steps': [{'stage_title': 'Sarı Alanda Acil Monitörizasyon, EKG ve Hemodinamik Değerlendirme',
             'question': 'Kalp hızı sayılamayacak kadar hızlı olan 4 yaşındaki bu çocukta tedavi algoritmasını '
                         'belirlemek için ilk yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Çocuğu kardiyak monitöre bağlamak, 12 derivasyonlu EKG çekmek ve bilinç, kapiller '
                                  'dolum, nabızlar ile kan basıncını ölçerek hemodinamik stabiliteyi değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Pediatrik taşiaritmilerde ilk adım QRS genişliğini ve ritim düzenini EKG ile '
                                         'saptamak, eş zamanlı olarak hastanın hemodinamik açıdan stabil mi yoksa '
                                         'dekompanse şokta mı olduğunu belirlemektir.',
                          'new_finding': 'Monitör ve 12 derivasyonlu EKG: Kalp hızı 245/dk, P dalgalarının '
                                         'seçilemediği, QRS süresinin 0.06 saniye olduğu, R-R aralıkları tamamen '
                                         'sabit, atımdan atıma değişkenlik göstermeyen dar kompleksli taşiaritmi '
                                         'izlendi. Hemodinamik değerlendirme: Bilinç açık (GKS 15), kapiller dolum '
                                         'zamanı 2 saniye, santral ve periferik nabızlar alınıyor, TA 94/58 mmHg (yaşa '
                                         'göre normotansif).'},
                         {'text': 'Kalp hızının yüksekliğini oyun sonrası gelişen anksiyete ve sıvı kaybına bağlayarak '
                                  'EKG çekmeden önce hastaya oral su içirip sakin bir odada otuz dakika dinlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Monitörizasyon yapılmadan bekletilen çocukta 245/dk hızındaki taşiaritmi '
                                             'devam etti ve miyokardiyal yorgunluğa bağlı perfüzyon bozukluğu '
                                             'gelişmeye başladı.',
                          'teaching_point': '4 yaşındaki bir çocukta 180/dk üzerindeki ani başlangıçlı çarpıntı '
                                            'fizyolojik sinüs taşikardisi ile açıklanamaz; derhal monitörizasyon ve 12 '
                                            'derivasyonlu EKG gerektirir.'},
                         {'text': 'Çarpıntının olası elektrolit bozukluğu veya tirotoksikoz kaynaklı olduğunu '
                                  'düşünerek EKG ve monitörizasyonu biyokimya ve tiroid fonksiyon testi sonuçları '
                                  'çıkana kadar ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Biyokimya sonuçları beklenirken geçen bir saat boyunca kalp hızı 245/dk '
                                             'düzeyinde kaldı ve hastada hipotansiyon gelişti.',
                          'teaching_point': 'Akut taşiaritmilerde laboratuvar tetkikleri ritim tanısını ve acil '
                                            'hız/ritim kontrolünü asla geciktirmemelidir.'},
                         {'text': 'Hastayı monitöre bağlamadan önce çarpıntıyı hızla sonlandırmak amacıyla ağızdan '
                                  'propranolol tablet kırarak içirmek ve bir saat sonra tekrar kontrol muayenesi '
                                  'yapmak',
                          'is_correct': False,
                          'scenario_update': 'EKG çekilmeden verilen oral beta-blokerin etkisi başlamadığı gibi ritim '
                                             'kaynağı belgelenemedi ve akut yönetim gecikti.',
                          'teaching_point': 'Akut semptomatik taşiaritmide EKG ile QRS süresi ve ritim tanımlanmadan '
                                            'oral antiaritmik verilmez.'}]},
            {'stage_title': 'Sarı Alanda İlk Non-İnvaziv Müdahale ve Damar Yolu Hazırlığı',
             'question': "Hemodinamik olarak stabil olan ve EKG'de 245/dk sabit hızlı dar kompleksli taşiaritmi "
                         'saptanan 4 yaşındaki çocukta ilk müdahale adımınız ne olmalıdır?',
             'options': [{'text': 'Bilinç açık ve kan basıncı normal olmasına rağmen kalp hızı 240/dk üzerinde olduğu '
                                  'için sedasyon vermeden derhal 1 J/kg dozunda senkronize kardiyoversiyon uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Bilinci tamamen açık ve perfüzyonu normal olan çocuğa sedasyonsuz '
                                             'uygulanan elektriksel şok ciddi ağrı ve travmaya neden oldu.',
                          'teaching_point': 'Acil senkronize kardiyoversiyon yalnızca hemodinamik instabilite '
                                            '(hipotansiyon, şok, bilinç bozukluğu) varlığında ilk basamaktır; stabil '
                                            'hastada önce non-invaziv otonomik uyarı ve farmakolojik tedavi '
                                            'uygulanır.'},
                         {'text': 'Hava yolunu kapatmadan yüze 10-15 saniye buzlu su torbası uygulayarak otonomik '
                                  'dalış refleksini uyarmak ve antekübital geniş damar yolu açmak',
                          'is_correct': True,
                          'explanation': 'Hemodinamik açıdan stabil dar kompleksli taşiaritmide ilk adım parasempatik '
                                         'tonusu artırarak atriyoventriküler düğüm iletimini yavaşlatmaktır; küçük '
                                         'çocuklarda en güvenli yöntem ağız-burun kapatılmadan alına/yüze buz torbası '
                                         'uygulanmasıdır.',
                          'new_finding': 'Yüze 15 saniye buz torbası uygulanması sırasında kalp hızı monitörde 245/dk '
                                         'olarak sabit kaldı, atımdan atıma hız değişikliği veya geçici yavaşlama '
                                         'gözlenmedi. Sol antekübital venden geniş lümenli damar yolu açıldı ve üç '
                                         'yollu musluk takılarak sürekli EKG kaydı altında farmakolojik müdahale '
                                         'hazırlığı tamamlandı.'},
                         {'text': 'Çocuğun iki göz küresine başparmaklarla kuvvetlice bastırarak okülokardiyak '
                                  'refleksi uyarmak ve yanıt alınamazsa boyundan iki taraflı karotis sinüs masajı '
                                  'uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Uygulanan göz küresi basısı ve karotis masajı taşiaritmiyi '
                                             'sonlandırmadığı gibi çocukta retinal kanama, korneal travma ve serebral '
                                             'iskemi riski yarattı.',
                          'teaching_point': 'Pediatrik yaş grubunda okülokardiyak refleks (göz basısı) retina '
                                            'dekolmanı ve glob hasarı riski nedeniyle, karotis masajı ise etkisiz ve '
                                            'komplikasyonlu olması nedeniyle kesinlikle kontrendikedir.'},
                         {'text': 'Taşiaritminin gizli hipovolemiye bağlı olduğunu düşünerek 20 mL/kg izotonik sodyum '
                                  'klorür bolusu başlamak ve intravenöz kalsiyum kanal blokeri infüzyonu hazırlamak',
                          'is_correct': False,
                          'scenario_update': 'İzotonik sıvı bolusu sabit 245/dk olan kalp hızında hiçbir değişiklik '
                                             'yapmadı; küçük çocukta hazırlanan kalsiyum kanal blokeri ise ağır '
                                             'hipotansiyon ve miyokardiyal depresyon riski taşıdı.',
                          'teaching_point': 'Atımdan atıma hiç değişmeyen 245/dk sabit hızlı ve P dalgasız dar QRS '
                                            'taşiaritmi hipovolemik yanıt değildir; ayrıca küçük çocuklarda kalsiyum '
                                            'kanal blokerleri kardiyovasküler kollaps riski nedeniyle '
                                            'kontrendikedir.'}]},
            {'stage_title': 'EKG ve Klinik Bulgularla Kesin Ritim Tanısı',
             'question': 'Kalp hızı 245/dk, R-R aralıkları tamamen sabit, P dalgaları seçilemeyen ve QRS süresi 0.06 '
                         'saniye olan bu dar kompleksli taşiaritminin kesin tanısı nedir?',
             'options': [{'text': 'Belirgin fizyolojik sinüs taşikardisi',
                          'is_correct': False,
                          'scenario_update': 'Sinüs taşikardisinde ateş, ağrı veya hipovolemi gibi bir neden bulunur, '
                                             'her QRS önünde normal P dalgası seçilir ve kalp hızı aktiviteyle '
                                             'değişkenlik gösterir.',
                          'teaching_point': 'Kalp hızının >220/dk (çocukta >180/dk) olması, R-R mesafesinin tamamen '
                                            'sabit kalması ve P dalgalarının seçilememesi sinüs taşikardisini dışlar.'},
                         {'text': 'Sürekli monomorfik ventriküler taşikardi',
                          'is_correct': False,
                          'scenario_update': 'Ventriküler taşikardide QRS süresi yaşa göre uzamıştır (>0.09 sn) ve '
                                             'atriyoventriküler disosiasyon görülür; bu hastada QRS süresi 0.06 sn '
                                             'olup dardır.',
                          'teaching_point': 'Normal ve dar QRS kompleksi (<0.09 sn), ventrikül aktivasyonunun normal '
                                            'His-Purkinje sistemi üzerinden gerçekleştiğini ve aritminin '
                                            'supraventriküler kaynaklı olduğunu gösterir.'},
                         {'text': 'Düzensiz iletili atriyal fibrilasyon',
                          'is_correct': False,
                          'scenario_update': 'Atriyal fibrilasyonda R-R aralıkları tamamen düzensizdir (aritmi '
                                             'absoluta) ve izoelektrik hatta fibrilasyon dalgaları izlenir.',
                          'teaching_point': 'Milimetrik olarak eşit R-R aralıkları ile seyreden düzenli dar QRS '
                                            'taşikardi atriyal fibrilasyon değil reentran taşikardidir.'},
                         {'text': 'Paroksismal supraventriküler taşikardi (SVT)',
                          'is_correct': True,
                          'explanation': 'Ani başlayan, R-R aralıkları sabit, KTA >180-220/dk olan, P dalgalarının '
                                         'seçilemediği ve dar QRS (<0.09 sn) ile seyreden tablo atriyoventriküler '
                                         'düğüm bağımlı reentran SVT için tipiktir.',
                          'new_finding': 'Kesin tanı: Paroksismal Supraventriküler Taşikardi (SVT - Hemodinamik Olarak '
                                         'Stabil).'}]},
            {'stage_title': 'Farmakolojik Ritim Kontrolü ve Kardiyoloji İzlemi',
             'question': 'Buz uygulamasına yanıt vermeyen hemodinamik olarak stabil SVT hastasında ilk tercih '
                         'farmakolojik ajan, uygulama tekniği ve ritim dönüşü sonrası planınız ne olmalıdır?',
             'options': [{'text': 'El sırtındaki ince damar yolundan 0.1 mg/kg adenozini 2 dakikada yavaş infüzyonla '
                                  'vermek ve ritim döner dönmez çocuğu poliklinik kontrolüyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Adenozinin plazma yarılanma ömrü 10 saniyenin altında olduğundan distal '
                                             'venden yavaş verildiğinde kalbe ulaşmadan eritrositler tarafından '
                                             'yıkıldı ve taşikardi sonlanmadı.',
                          'teaching_point': 'Adenozin mutlaka kalbe yakın geniş bir venden (tercihen antekübital) üç '
                                            'yollu musluk kullanılarak çok hızlı bolus puşe ve hemen ardından 5-10 mL '
                                            'serum fizyolojik yıkaması (çift enjektör tekniği) ile verilmelidir.'},
                         {'text': 'İlk tercih ilaç olarak intravenöz verapamil (0.1 mg/kg) puşelemek ve ritim sinüse '
                                  'döndükten sonra rekürrensi önlemek için oral digoksin yüklemesi yapmak',
                          'is_correct': False,
                          'scenario_update': 'İntravenöz verapamil sonrası çocukta derin hipotansiyon gelişti; ayrıca '
                                             'olası aksesuar yolak (WPW) dışlanmadan digoksin verilmesi malign '
                                             'ventriküler aritmi riski doğurdu.',
                          'teaching_point': "Pediatrik SVT'de ilk tercih farmakolojik ajan her zaman adenozindir; "
                                            'verapamil miyokardiyal depresyon yapar, digoksin ise WPW sendromu '
                                            'dışlanmadan kullanılmaz.'},
                         {'text': 'Antekübital venden üç yollu muslukla 0.1 mg/kg hızlı adenozin puşe ve serum '
                                  'fizyolojik yıkaması uygulayıp sinüs ritminde kontrol EKG çekmek',
                          'is_correct': True,
                          'explanation': "Stabil SVT'de vagal manevra başarısız olduğunda ilk tercih ilaç hızlı İV "
                                         'adenozindir (ilk doz 0.1 mg/kg, maks 6 mg; gerekirse ikinci doz 0.2 mg/kg, '
                                         'maks 12 mg). Sinüs ritmine döndükten sonra WPW (delta dalgası, kısa PR) '
                                         'varlığını araştırmak için 12 derivasyonlu EKG çekilir ve pediatrik '
                                         'kardiyoloji konsültasyonu istenir.',
                          'new_finding': 'Sol antekübital venden 0.1 mg/kg (1.6 mg) adenozin hızlı puşe ve ardından 5 '
                                         'mL serum fizyolojik yıkaması ile saniyeler içinde sinüs ritmine (KTA 96/dk) '
                                         "dönüş sağlandı. Sinüs ritminde çekilen kontrol 12 derivasyonlu EKG'de PR "
                                         'mesafesi normaldi ve delta dalgası izlenmedi. Pediatrik kardiyoloji '
                                         'konsültasyonu ve 6 saatlik monitörize izlem sonrası hasta stabil olarak '
                                         'taburcu edildi.'},
                         {'text': 'Farmakolojik tedaviyi atlayıp doğrudan 5 mg/kg intravenöz amiodaron yüklemesi '
                                  'başlamak ve ritim döndükten sonra hastayı entübe ederek yoğun bakıma devretmek',
                          'is_correct': False,
                          'scenario_update': 'Yirmi dakikada verilen amiodaron infüzyonu sırasında ritim dönüşü '
                                             'gecikti ve bradikardi/hipotansiyon riski oluştu; stabil çocukta '
                                             'entübasyon tamamen gereksizdi.',
                          'teaching_point': 'Amiodaron veya prokainamid yalnızca adenozinin (0.1 ve 0.2 mg/kg '
                                            'dozlarının) başarısız olduğu dirençli SVT olgularında kardiyoloji '
                                            'eşliğinde ikinci basamak olarak kullanılır.'}]}]},
 {'id': 'S15',
  'category': '🫁 Hırıltı & Solunum Sıkıntısı',
  'age': '2.5 Yaş',
  'gender': 'Kız',
  'complaint': 'Yer fıstığı yerken aniden boğulur gibi morarıp öksürme, ardından nefes alırken tek taraflı hırıltı ve '
               'solunum sesinde azalma',
  'history': "Ailesi 2.5 yaşındaki kız çocuğunu panikle Sarı Alana getiriyor: 'Yaklaşık 2 saat önce oturma odasında "
             'tabaktaki yer fıstıklarından yerken birden boğulur gibi şiddetle öksürmeye başladı, gözleri kızardı ve '
             'dudakları morardı. Birkaç kez öksürdükten sonra morarması geçti ve nefes alabildi ama o andan beri '
             'sürekli hırıltılı nefes alıyor ve aralıklı kuru öksürüğü devam ediyor. Daha önce astım veya benzer bir '
             "hırıltı öyküsü hiç yoktu.'",
  'final_diagnosis': 'Trakeobronşiyal Yabancı Cisim Aspirasyonu (Sağ Ana Bronşta Organik Cisim ve Obstrüktif Hava '
                     'Hapsi)',
  'disposition': 'Sarı Alanda Sakin Pozisyon + Oksijen Desteği + İnspiratuar/Ekspiratuar Akciğer Grafisi Sonrası Genel '
                 'Anestezi Altında Acil Rijit Bronkoskopi',
  'case_pearl': '1-3 yaş arası çocukta kuruyemiş/oyuncak temasını takiben ani başlayan boğulma-öksürük-morarma '
                '(penetrasyon sendromu) ve oskültasyonda tek taraflı solunum seslerinde azalma/lokalize wheezing aksi '
                'kanıtlanana kadar trakeobronşiyal yabancı cisim aspirasyonudur. Organik cisimler (yer fıstığı, '
                'fındık, çekirdek) radyolüsendir ve grafide doğrudan görülmez; ekspiratuar veya lateral dekübit '
                "grafisinde check-valve (tek yönlü valf) mekanizmasına bağlı 'tek taraflı obstrüktif hava hapsi' ve "
                'karşı tarafa mediastinal şift saptanır. Normal akciğer grafisi tanıyı asla dışlamaz; kesin tanı ve '
                'tedavi ameliyathanede genel anestezi altında rijit bronkoskopidir.',
  'steps': [{'stage_title': 'Sarı Alanda Hava Yolu Güvenliği ve Oskültasyon Değerlendirmesi',
             'question': 'Yer fıstığı yerken ani boğulma ve morarma atağı geçiren, sonrasında öksürük ve hırıltısı '
                         'süren 2.5 yaşındaki çocukta ilk yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Çocuğu ağlatmadan sakin tutarak hava yolu açıklığını, ses kalitesini, oksijen '
                                  'satürasyonunu ve bilateral akciğer oskültasyonunda solunum seslerinin simetrisini '
                                  'dikkatle değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Ses çıkarabilen ve etkili öksürebilen çocukta kısmi hava yolu obstrüksiyonu '
                                         'vardır; bu aşamada çocuk ajite edilmemeli, körlemesine manevralardan '
                                         'kaçınılmalı ve oskültasyonla asimetrik bulgular değerlendirilmelidir.',
                          'new_finding': 'Vital bulgular: SS 38/dk, KTA 124/dk, oda havasında SpO2 %92, Ateş 36.7°C. '
                                         'Çocuk sakinleştirildiğinde ses çıkarabiliyor ve öksürebiliyor (kısmi hava '
                                         'yolu açıklığı korunmuş). Akciğer oskültasyonunda sağ hemitoraksta solunum '
                                         'sesleri belirgin azalmış ve sağ orta-alt zonda lokalize monofonik '
                                         'ekspiratuar wheezing duyuluyor; sol akciğer solunum sesleri doğal.'},
                         {'text': 'Çocuğun ağzını dil basacağı ile zorla açıp farenks ve hipofarenkse işaret '
                                  'parmağıyla körlemesine süpürme manevrası uygulayarak takılan parçayı çıkarmaya '
                                  'çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Ağız içine yapılan körlemesine parmak manevrası çocuğu şiddetle ağlattı '
                                             've öğürme refleksiyle hava yolu güvenliğini tehlikeye soktu.',
                          'teaching_point': 'Pediatrik ileri yaşam desteği kılavuzlarına göre ağız içinde doğrudan '
                                            'görülmeyen hiçbir cisim için körlemesine parmak süpürmesi yapılmaz; cismi '
                                            'subglottik alana iterek tam obstrüksiyona yol açabilir.'},
                         {'text': 'Çocuk nefes alıp ağlayabildiği halde zaman kaybetmeden baş aşağı pozisyona getirip '
                                  'skapulalar arasına beş kez sert sırt vuruşu ve Heimlich manevrası uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Bronşa yerleşmiş olan fıstık parçası sert sırt vuruşu ve pozisyon '
                                             'değişikliğiyle karinadan trakeaya hareket ederek akut stridor ve '
                                             'siyanoza neden oldu.',
                          'teaching_point': 'Sırt vuruşu ve abdominal bası (Heimlich) yalnızca tam hava yolu '
                                            'tıkanıklığında (etkisiz öksürük, ses çıkaramama, siyanoz) uygulanır; '
                                            'kısmi/bronşiyal obstrüksiyonda cismi trakeaya fırlatıp tam tıkanma '
                                            'yapabileceği için kontrendikedir.'},
                         {'text': 'Ani başlayan ekspiratuar hırıltıyı akut bronkospazm atağı kabul ederek oskültasyon '
                                  'yapmadan önce ardışık üç doz nebulize salbutamol ve sistemik steroid başlamak',
                          'is_correct': False,
                          'scenario_update': 'Nebulize salbutamol sonrası sağ hemitorakstaki solunum sesi azalması ve '
                                             'lokalize monofonik wheezing hiç değişmedi; mekanik obstrüksiyon tanısı '
                                             'gecikti.',
                          'teaching_point': 'Öncesinde sağlıklı olan küçük çocukta yemek yerken ani başlayan öksürük '
                                            've tek taraflı monofonik wheezing difüz bronkospazm değil mekanik '
                                            'endobronşiyal obstrüksiyonu gösterir.'}]},
            {'stage_title': 'Radyolojik Görüntüleme Seçimi ve Bulguların Yorumlanması',
             'question': 'Sağ hemitoraksta solunum sesleri azalan ve lokalize ekspiratuar wheezing saptanan bu çocukta '
                         'radyolojik görüntüleme yaklaşımınız nasıl olmalıdır?',
             'options': [{'text': 'Tek yönlü inspiratuar akciğer grafisi çekmek ve grafide radyoopak bir dansite '
                                  'görülmezse bronşiyal tıkanıklığı dışlayarak nebülize bronkodilatör tedaviyle izleme '
                                  'almak',
                          'is_correct': False,
                          'scenario_update': 'Standart inspiratuar grafide radyoopak cisim görülmediği için mekanik '
                                             'tıkanıklık yanlışlıkla dışlandı; ancak yer fıstığının salgıladığı yağ '
                                             'asitleri 24 saat içinde ağır kimyasal pnömonit başlattı.',
                          'teaching_point': "Çocuklarda solunum yoluna kaçan cisimlerin %80-90'ı organik gıdalardır "
                                            '(fıstık, fındık, çekirdek) ve radyoopak değildir; ayrıca tek başına '
                                            'inspiratuar grafi tamamen normal görünebilir.'},
                         {'text': 'Gıda parçasının özofagus üst uçta kalarak trakeaya dıştan bası yaptığını göstermek '
                                  'amacıyla hastaya acil baryumlu özofagus pasaj grafisi hemen çekmek',
                          'is_correct': False,
                          'scenario_update': 'Solunum sıkıntısı olan çocuğa içirilen baryumlu kontrast madde '
                                             'aspirasyon riski yarattı ve yapılacak endoskopik havayolu girişiminin '
                                             'görüş alanını bozdu.',
                          'teaching_point': 'Akut trakeobronşiyal obstrüksiyon şüphesinde kontrastlı özofagus pasaj '
                                            'grafisi endike değildir; hem aspirasyon riski taşır hem de genel anestezi '
                                            'öncesi oral alım yasağını bozar.'},
                         {'text': 'İnspiratuar ve ekspiratuar akciğer grafileri çekerek tek taraflı obstrüktif hava '
                                  'hapsi, diyafram düzleşmesi ve mediastinal şift varlığını değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Radyolüsen organik cisimlerin oluşturduğu tek yönlü valf (check-valve) '
                                         'etkisini göstermek için inspiratuar grafiye ek olarak ekspiratuar grafi '
                                         '(küçük çocukta kooperasyon zor olduğundan bilateral lateral dekübit grafisi) '
                                         'çekilir.',
                          'new_finding': 'Radyolojik İnceleme: Ekspiratuar akciğer grafisinde sağ hemitoraksta '
                                         'havalanma fazlalığı (check-valve mekanizmasına bağlı obstrüktif hava hapsi), '
                                         'sağ hemidiyaframda düzleşme, interkostal aralıklarda genişleme ve '
                                         'mediastenin sola doğru yer değiştirdiği izlendi. Radyoopak dansite '
                                         'saptanmadı.'},
                         {'text': 'Direkt grafilerin organik maddeleri göstermede yetersiz olması nedeniyle çocuğu '
                                  'sedatize ederek doğrudan intravenöz kontrastlı toraks bilgisayarlı tomografisine '
                                  'acilen göndermek',
                          'is_correct': False,
                          'scenario_update': 'Kısmi hava yolu obstrüksiyonu olan çocuğa BT çekimi için verilen '
                                             'sedasyon hava yolu tonusunu düşürerek desatürasyona yol açtı ve çocuğu '
                                             'gereksiz radyasyona maruz bıraktı.',
                          'teaching_point': 'Tipik penetrasyon sendromu öyküsü ve tek taraflı oskültasyon/grafi '
                                            "bulgusu olan çocukta BT'ye gerek yoktur; doğrudan kesin girişimsel tanı "
                                            've tedaviye geçilir.'}]},
            {'stage_title': 'Öykü, Fizik Muayene ve Radyolojik Bulgularla Kesin Tanı',
             'question': 'Ani boğulma öyküsü, sağda solunum seslerinde azalma ve ekspiratuar grafide sağ hemitoraksta '
                         'obstrüktif hava hapsi saptanan hastada kesin tanınız nedir?',
             'options': [{'text': 'Sağ spontan tansiyon pnömotoraks tablosu',
                          'is_correct': False,
                          'scenario_update': 'Pnömotoraksta visseral plevra çizgisi ve periferde damar izi olmayan '
                                             'avasküler hiperlüsen alan görülür; bu hastada ise parankimal '
                                             'bronkovasküler izler korunmuş olup obstrüktif amfizem vardır.',
                          'teaching_point': 'Ekspiryumda sönmeyen ancak bronkovasküler dallanmanın devam ettiği tek '
                                            'taraflı hiperlüsensi pnömotoraks değil endobronşiyal check-valve '
                                            'obstrüksiyonuna bağlı hava hapsidir.'},
                         {'text': 'Trakeobronşiyal yabancı cisim aspirasyonu',
                          'is_correct': True,
                          'explanation': 'Yer fıstığı yerken gelişen penetrasyon sendromu, sağda azalmış solunum '
                                         'sesleri ve ekspiratuar grafide sağ obstrüktif hava hapsi sağ ana bronş '
                                         'yabancı cisim aspirasyonu için tanısaldır.',
                          'new_finding': 'Kesin tanı: Trakeobronşiyal Yabancı Cisim Aspirasyonu (Sağ Ana Bronşta '
                                         'Organik Yabancı Cisim).'},
                         {'text': 'Akut viral laringotrakeobronşit (krup) atağı',
                          'is_correct': False,
                          'scenario_update': 'Krup sendromu viral prodrom sonrası havlar tarzda öksürük ve inspiratuar '
                                             'stridorla seyreder; tek taraflı solunum sesi azalması ve asimetrik hava '
                                             'hapsi yapmaz.',
                          'teaching_point': 'Asimetrik oskültasyon bulgusu ve tek taraflı obstrüktif amfizem üst hava '
                                            'yolu enfeksiyonunu dışlar.'},
                         {'text': 'Konjenital sağ üst lober amfizem',
                          'is_correct': False,
                          'scenario_update': 'Konjenital lober amfizem genellikle yenidoğan ve erken süt çocukluğu '
                                             'döneminde progresif solunum sıkıntısı ile başvurur ve en sık sol üst '
                                             'lobu tutar.',
                          'teaching_point': '2.5 yaşında sağlıklı bir çocukta kuruyemiş yerken akut başlayan tek '
                                            'taraflı hava hapsi edinsel endobronşiyal obstrüksiyondur.'}]},
            {'stage_title': 'Kesin Girişimsel Tedavi ve Preoperatif Hazırlık',
             'question': 'Sağ ana bronşta organik yabancı cisim aspirasyonu tanısı kesinleşen 2.5 yaşındaki çocuğun '
                         'nihai tedavi yönetimi nasıl olmalıdır?',
             'options': [{'text': 'Nebulize adrenalin ve göğüs fizyoterapisi ile postural drenaj uygulayarak sağ '
                                  'bronştaki fıstık parçasının öksürük refleksiyle kendiliğinden çıkmasını yirmi dört '
                                  'saat beklemek',
                          'is_correct': False,
                          'scenario_update': 'Göğüs perküsyonu ve postural drenaj sırasında yerinden oynayan yer '
                                             'fıstığı subglottik darlığa sıkışarak tam hava yolu obstrüksiyonuna ve '
                                             'hipoksik arreste yol açtı.',
                          'teaching_point': 'Trakeobronşiyal yabancı cisimlerde göğüs fizyoterapisi ve postural drenaj '
                                            'cismin ana trakeaya veya larenkse yer değiştirip asfiksi yapma riski '
                                            'nedeniyle kesinlikle kontrendikedir.'},
                         {'text': 'Sarı Alanda yatak başında sedoanaljezi altında fleksibl fiberoptik '
                                  'nazofaringolaringoskop ile karinaya kadar ilerleyip fıstık parçasını biyopsi '
                                  'forsepsiyle çıkarmayı hemen denemek',
                          'is_correct': False,
                          'scenario_update': 'Yatak başında güvensiz hava yolu koşullarında yapılan girişimde şişmiş '
                                             'yer fıstığı parçalandı, laringospazm ve ağır hipoksemi gelişti.',
                          'teaching_point': 'Çocuklarda kesinleşmiş alt solunum yolu yabancı cisimlerinin '
                                            'çıkarılmasında altın standart, hem ventilasyonu sağlayan hem de optik '
                                            'forsepslerle güvenli kavrama imkanı veren genel anestezi altında rijit '
                                            'bronkoskopidir.'},
                         {'text': 'Çocuğun oksijen satürasyonu %92 üzerinde olduğu için oral amoksisilin-klavulanat '
                                  'başlayarak bir hafta sonra kontrol akciğer grafisi ve elektif işlem planlamak',
                          'is_correct': False,
                          'scenario_update': 'Organik yer fıstığı bronş sekresyonlarıyla şişerek tam obstrüksiyon, '
                                             'atelektazi, kimyasal arakidonik asit pnömoniti ve granülasyon dokusu '
                                             'geliştirdi.',
                          'teaching_point': 'Özellikle yer fıstığı gibi yağlı organik yabancı cisimler su çekerek '
                                            'hızla şişer ve şiddetli kimyasal bronşit/granülasyon yapar; tanı '
                                            'konulduğunda geciktirilmeden çıkarılmalıdır.'},
                         {'text': 'Oral alımı kesip çocuğu sakin tutarak oksijen desteğini sürdürmek ve ameliyathanede '
                                  'genel anestezi altında acil rijit bronkoskopi için cerrahiye devretmek',
                          'is_correct': True,
                          'explanation': 'Pediatrik trakeobronşiyal yabancı cisim aspirasyonunda kesin tanı ve tedavi '
                                         'ameliyathane koşullarında genel anestezi altında yapılan rijit '
                                         'bronkoskopidir; işlem öncesi çocuk aç bırakılır ve ajitasyondan korunur.',
                          'new_finding': 'Hasta çocuk cerrahisi tarafından ameliyathaneye alındı; genel anestezi '
                                         'altında rijit bronkoskopi ile sağ ana bronşu tıkayan yer fıstığı '
                                         'parçalanmadan çıkarıldı ve bronş lavajı yapıldı. İşlem sonrası sağ akciğer '
                                         'sesleri normale döndü ve hasta şifayla taburcu edildi.'}]}]},
 {'id': 'S16',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '7 Yaş',
  'gender': 'Erkek',
  'complaint': 'Fındıklı çikolata yedikten 15 dakika sonra vücutta yaygın kaşıntılı kabarıklıklar, dudaklarda şişlik, '
               'ses kısıklığı ve kıvrandırıcı karın ağrısı',
  'history': "Ailesi 7 yaşındaki (25 kg) erkek çocuğu kucaklarında Sarı Alana getiriyor: 'Okuldan gelince arkadaşının "
             'ikram ettiği fındıklı çikolatadan iki ısırık aldı. Yaklaşık 10-15 dakika içinde boynu ve gövdesi '
             'kıpkırmızı olup kabardı, dudakları şişti. Şimdi boğazım düğümleniyor diyor, sesi boğuklaştı, hafif '
             "hırıltısı başladı ve karnım çok ağrıyor diyerek iki büklüm kıvranıyor.'",
  'final_diagnosis': 'Akut Sistemik Anafilaksi (Besin Kaynaklı IgE Aracılı Tip 1 Hipersensitivite Reaksiyonu)',
  'disposition': 'Sarı Alanda Acil İntramusküler Adrenalin (0.01 mg/kg) + Oksijen + İV Kristaloid Desteği + En Az 6-8 '
                 'Saatlik Bifazik Reaksiyon Monitörizasyonu ve Otoenjektör Reçetesi ile Taburculuk',
  'case_pearl': 'Anafilaksi, alerjen maruziyeti sonrası dakikalar içinde cilt/mukoza bulgularına (ürtiker, anjiyoödem) '
                'ek olarak solunum (stridor, bronkospazm, dispne), dolaşım (hipotansiyon, taşikardi, hipoperfüzyon) '
                'veya şiddetli gastrointestinal semptomların (kıvrandırıcı kolik karın ağrısı, tekrarlayan kusma) '
                'eşlik ettiği yaşamı tehdit eden sistemik reaksiyondur. Tek birinci basamak hayat kurtarıcı ilaç uyluk '
                'anterolateral (vastus lateralis) kasına uygulanan İNTRAMUSKÜLER ADRENALİNDİR (1:1000, 0.01 mg/kg, '
                'çocukta maks 0.3-0.5 mg). Hasta sırtüstü yatırılıp bacakları yükseltilmeli, boş ventrikül sendromu '
                'riski nedeniyle aniden dik oturtulmamalı veya ayağa kaldırılmamalıdır. Bifazik reaksiyon riskine '
                'karşı en az 6-8 saat izlenmeli ve adrenalin otoenjektörü eğitimiyle taburcu edilmelidir.',
  'steps': [{'stage_title': 'Sarı Alanda İlk Değerlendirme ve Hasta Pozisyonu',
             'question': 'Şüpheli besin alımı sonrası cilt bulguları, ses kısıklığı ve karın ağrısı ile başvuran 7 '
                         'yaşındaki (25 kg) çocukta ilk değerlendirme ve pozisyonlandırma yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Hastayı solunumunu rahatlatmak amacıyla sedyede tam dik oturtmak, vital bulgularını '
                                  'ölçmek ve ağızdan hızlı etkili setirizin şurubu içirerek gözleme almak',
                          'is_correct': False,
                          'scenario_update': 'Dik oturtulan çocukta venöz dönüşün aniden azalmasıyla baş dönmesi ve '
                                             'hipotansiyon gelişti; ayrıca yutma güçlüğü nedeniyle oral şurubu aspire '
                                             'etme tehlikesi yaşandı.',
                          'teaching_point': 'Sistemik aşırı duyarlılık tablolarında hasta aniden dik oturtulmamalı '
                                            'veya ayağa kaldırılmamalıdır; üst hava yolu ödemi bulgusu varken oral '
                                            'ilaç verilmesi aspirasyon riski taşır.'},
                         {'text': 'Hastayı hızla sırtüstü yatırıp alt ekstremitelerini yükseltmek, havayolu '
                                  'açıklığını, solunum seslerini, periferik perfüzyonu ve kan basıncını '
                                  'değerlendirerek monitörize oksijen başlamak',
                          'is_correct': True,
                          'explanation': 'Çoklu sistem tutulumu düşündüren akut aşırı duyarlılık tablolarında venöz '
                                         'dönüşü korumak için hasta supin pozisyona alınmalı ve hızla ABCDE '
                                         'değerlendirmesi yapılmalıdır.',
                          'new_finding': 'Vital Bulgular: KTA 142/dk, SS 30/dk, TA 84/50 mmHg, SpO2 %93, KDZ 3 saniye. '
                                         'Fizik Muayene: Alt ve üst dudakta belirgin ödem, uvula ödemli, gövdede '
                                         'yaygın eritematöz plaklar, inspiratuar kaba ses ve ses kısıklığı, '
                                         'oskültasyonda bilateral ekspiratuar hışıltı, batında yaygın hassasiyet '
                                         'mevcut.'},
                         {'text': 'Öncelikle alerjen spesifik IgE ve triptaz düzeyi için kan örneği alıp damar yolu '
                                  'açmak, laboratuvar sonuçları çıkana kadar ilaç uygulamadan izlemek',
                          'is_correct': False,
                          'scenario_update': 'Damar yolu açılması ve kan alınması sürecinde geçen dakikalar içinde üst '
                                             'hava yolu ödemi ilerledi, inspiratuar ses belirginleşti ve oksijen '
                                             'satürasyonu %88 düzeyine geriledi.',
                          'teaching_point': 'Akut solunum ve dolaşım tutulumu olan aşırı duyarlılık reaksiyonlarında '
                                            'tanı tamamen klinik bulgulara dayanır; laboratuvar tetkikleri acil '
                                            'müdahaleyi asla geciktirmemelidir.'},
                         {'text': 'Solunum sıkıntısını gidermek için öncelikle soğuk buhar ve nebulize salbutamol '
                                  'uygulamak, cilt döküntüleri için topikal kortikosteroid losyon sürerek yanıtı '
                                  'beklemek',
                          'is_correct': False,
                          'scenario_update': 'Nebulize salbutamol uygulamasına rağmen hastanın ses kısıklığı ve üst '
                                             'hava yolu obstrüksiyon bulguları gerilemedi, arteriyel kan basıncı 76/42 '
                                             'mmHg düzeyine düştü.',
                          'teaching_point': 'Nebulize bronkodilatörler üst hava yolu ödemini ve sistemik vasküler '
                                            'permeabilite artışını düzeltmez; yalnızca birincil parenteral tedaviye ek '
                                            'destek olarak kullanılabilir.'}]},
            {'stage_title': 'Acil Farmakolojik Müdahale ve Uygulama Yolu',
             'question': 'Üst hava yolu ödemi, bronkospazm ve sınırda hipotansiyonu saptanan 25 kg ağırlığındaki bu '
                         'hastada derhal uygulanması gereken ilk basamak ilaç ve uygulama şekli hangisidir?',
             'options': [{'text': 'Damar yolundan 1 mg/kg metilprednizolon ve 1 mg/kg feniramin maleat yavaş puşe '
                                  'olarak uygulamak, klinik yanıt olmazsa ikinci basamakta vazopresör eklemek',
                          'is_correct': False,
                          'scenario_update': 'İntravenöz antihistaminik ve kortikosteroid uygulamasından 10 dakika '
                                             'sonra hastanın stridoru şiddetlendi, siyanoz gelişti ve kan basıncı '
                                             '68/35 mmHg düzeyine geriledi.',
                          'teaching_point': 'H1-antihistaminikler yalnızca cilt semptomlarını hafifletir, '
                                            'kortikosteroidlerin etkisi ise saatler sonra başlar; her iki ilaç da akut '
                                            'laringeal ödemi ve şoku önleyemez.'},
                         {'text': '1:1000 konsantrasyondaki adrenalinden 0.25 mg çekerek sulandırmadan doğrudan '
                                  'periferik damar yolundan hızlı intravenöz bolus şeklinde puşe etmek ve sıvı '
                                  'yüklemek',
                          'is_correct': False,
                          'scenario_update': 'Konsantre intravenöz adrenalin bolusu sonrasında hastada şiddetli '
                                             'hipertansif atak, göğüs ağrısı ve monitörde polimorfik ventriküler '
                                             'ekstrasistoller ile taşiaritmi gelişti.',
                          'teaching_point': '1:1000 konsantrasyondaki adrenalin yalnızca intramusküler kullanım '
                                            'içindir; doğrudan intravenöz bolus uygulanması ölümcül ventriküler '
                                            'aritmilere ve intrakraniyal kanamaya yol açabilir.'},
                         {'text': '1:1000 konsantrasyondaki adrenalinden 0.25 mg dozunda uyluk anterolateral vastus '
                                  'lateralis kasına intramusküler uygulamak ve izotonik kristaloid desteği başlamak',
                          'is_correct': True,
                          'explanation': 'Alfa-1 vazokonstriktör etkisiyle mukozal ödemi azaltan, beta-2 etkisiyle '
                                         'bronkodilatasyon sağlayan ve mast hücre degranülasyonunu durduran tek '
                                         'birinci basamak tedavi intramusküler adrenalindir.',
                          'new_finding': 'Sol vastus lateralis kasına 0.25 mg intramusküler adrenalin uygulandı ve 20 '
                                         'mL/kg %0.9 NaCl infüzyonu başlandı. 5 dakika içinde ses kısıklığı ve stridor '
                                         'geriledi, SpO2 %98, TA 102/64 mmHg, KTA 116/dk ölçüldü, döküntüler solmaya '
                                         'başladı.'},
                         {'text': '1:1000 konsantrasyondaki adrenalinden 0.25 mg dozunda kolun deltoid bölgesine cilt '
                                  'altına enjekte etmek ve eş zamanlı nebulize budesonid tedavisi başlamak',
                          'is_correct': False,
                          'scenario_update': 'Subkutan enjeksiyon sonrası ciltteki vazokonstriksiyon nedeniyle ilacın '
                                             'sistemik emilimi gecikti, 15 dakika geçmesine rağmen solunum sıkıntısı '
                                             've hipotansiyon düzelmedi.',
                          'teaching_point': 'Uyluk anterolateral (vastus lateralis) kasına intramusküler uygulama, '
                                            'subkutan veya deltoid kası uygulamasına göre çok daha hızlı ve yüksek '
                                            'zirve plazma konsantrasyonu sağlar.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Alerjen besin teması sonrası dakikalar içinde cilt-mukoza, solunum ve gastrointestinal '
                         'sistem bulgularının birlikte geliştiği bu tablonun kesin tanısı nedir?',
             'options': [{'text': 'Besin Kaynaklı Akut Sistemik Anafilaksi',
                          'is_correct': True,
                          'explanation': 'Bilinen veya olası bir alerjen maruziyeti sonrası dakikalar içinde '
                                         'cilt/mukoza tutulumuna solunum ve persistan gastrointestinal bulguların '
                                         'eşlik etmesi WAO/EAACI kriterlerine göre kesin anafilaksi tanısı koydurur.',
                          'new_finding': 'Kesin tanı: Besin Kaynaklı Akut Sistemik Anafilaksi. İlk doz İM adrenalin '
                                         'ile havayolu ve dolaşım stabilizasyonu sağlandı.'},
                         {'text': 'Akut Jeneralize Ürtiker ve Anjiyoödem',
                          'is_correct': False,
                          'scenario_update': 'İzole ürtiker ve anjiyoödemde laringeal stridor, bronkospazm, '
                                             'hipotansiyon veya şiddetli gastrointestinal sistem tutulumu bulunmaz.',
                          'teaching_point': 'Cilt ve mukoza bulgularına solunum, dolaşım veya şiddetli '
                                            'gastrointestinal semptomlardan en az birinin eşlik etmesi tabloyu izole '
                                            'ürtikerden çıkarıp anafilaksiye taşır.'},
                         {'text': 'Herediter Anjiyoödem Akut Laringeal Atağı',
                          'is_correct': False,
                          'scenario_update': 'Herediter anjiyoödem bradikinin aracılıdır; kaşıntılı ürtiker plakları '
                                             'eşlik etmez ve adrenalin tedavisine yanıt vermez.',
                          'teaching_point': 'Herediter anjiyoödemde C1 esteraz inhibitör eksikliğine bağlı ürtikersiz, '
                                            'kaşıntısız ödem görülür; bu hastada yaygın kaşıntılı ürtiker ve '
                                            'adrenaline hızlı yanıt mevcuttur.'},
                         {'text': 'Besin Proteini İlişkili Enterokolit Sendromu',
                          'is_correct': False,
                          'scenario_update': 'Besin proteini ilişkili enterokolit sendromu (FPIES) IgE aracılı '
                                             'değildir; alımdan 1-4 saat sonra gecikmiş inatçı kusma ile seyreder, '
                                             'ürtiker ve stridor yapmaz.',
                          'teaching_point': 'Dakikalar içinde gelişen ürtiker, anjiyoödem ve laringeal ödem IgE '
                                            'aracılı Tip 1 aşırı duyarlılık reaksiyonunu (anafilaksi) gösterir.'}]},
            {'stage_title': 'Sarı Alan Gözlem Süresi ve Taburculuk Planı',
             'question': 'İlk doz intramusküler adrenalin sonrası klinik bulguları tamamen düzelen 25 kg ağırlığındaki '
                         'bu hastanın izlem ve taburculuk yönetimi nasıl olmalıdır?',
             'options': [{'text': 'Semptomları tamamen gerilediği için 1 saatlik gözlem sonunda oral antihistaminik '
                                  'reçete ederek taburcu etmek ve 1 hafta sonra alerji polikliniğine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Erken taburcu edilen çocukta ilk ataktan 5 saat sonra evde tekrar '
                                             'alerjen teması olmaksızın şiddetli stridor ve hipotansiyonla seyreden '
                                             'bifazik reaksiyon gelişti.',
                          'teaching_point': 'Anafilaksi olgularının %5-20 kadarında ilk semptomlar düzeldikten saatler '
                                            'sonra bifazik reaksiyon gelişebildiğinden hastalar en az 6-8 saat gözlem '
                                            'altında tutulmalıdır.'},
                         {'text': 'Hastayı 2 saat gözlemde tuttuktan sonra yalnızca oral metilprednizolon ve '
                                  'desloratadin şurup reçete ederek, adrenalin otoenjektörü yazmadan aileye diyet '
                                  'listesiyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Adrenalin otoenjektörü reçete edilmeyen hasta birkaç hafta sonra okulda '
                                             'gelişen kazara maruziyette ilk müdahale yapılamadığı için ağır solunum '
                                             'yetmezliği ile acile getirildi.',
                          'teaching_point': 'Besin anafilaksisi geçiren her çocuğa taburculukta mutlaka ağırlığına '
                                            'uygun adrenalin otoenjektörü reçete edilmeli ve aileye yazılı acil eylem '
                                            'planı verilmelidir.'},
                         {'text': 'Bifazik reaksiyonu kesin olarak engellemek amacıyla 6 saatlik gözlem süresince her '
                                  '2 saatte bir profilaktik düşük doz intramusküler adrenalin enjeksiyonu tekrarlamak',
                          'is_correct': False,
                          'scenario_update': 'Semptomu kalmayan hastaya yapılan tekrarlayan gereksiz adrenalin '
                                             'enjeksiyonları şiddetli taşikardi, hipertansiyon, tremor ve anksiyeteye '
                                             'yol açtı.',
                          'teaching_point': 'Adrenalin yalnızca aktif semptom varlığında (ilk doza 5-15 dakikada yanıt '
                                            'alınamazsa veya semptomlar nüksederse) tekrarlanır; asemptomatik hastaya '
                                            'profilaktik tekrar doz yapılmaz.'},
                         {'text': 'Bifazik reaksiyon riski açısından en az 6-8 saat monitörize gözlemde tutmak, '
                                  'taburculukta adrenalin otoenjektörü reçete ederek aileye uygulamalı eğitim vermek',
                          'is_correct': True,
                          'explanation': 'Solunum tutulumu olan anafilaksi hastaları bifazik reaksiyon açısından en az '
                                         '6-8 saat izlenmeli, taburculukta adrenalin otoenjektörü reçete edilerek '
                                         'çocuk alerji bölümüne yönlendirilmelidir.',
                          'new_finding': 'Hasta Sarı Alanda 8 saat boyunca monitörize izlendi ve bifazik reaksiyon '
                                         'gelişmedi. Aileye adrenalin otoenjektörü kullanımı maket üzerinde uygulamalı '
                                         'olarak öğretildi, yazılı eylem planı ve Çocuk Alerji randevusu verilerek '
                                         'güvenle taburcu edildi.'}]}]},
 {'id': 'S17',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '13 Yaş',
  'gender': 'Erkek',
  'complaint': 'Otizm spektrum bozukluğu olan, konuşmayan çocukta gece başlayan durmaksızın ağlama, bağırma, kendine '
               'vurma ve iki kez kusma',
  'history': "Otizm spektrum bozukluğu tanılı, sözel iletişimi olmayan 13 yaşındaki erkek hasta sabah 06:00'da "
             'annesiyle Yeşil Alana getiriliyor; triyajda yoğun ajitasyon nedeniyle Sarı Alana devrediliyor. Öyküyü '
             "annesi veriyor: 'Gece 03:00 gibi çığlık atarak uyandı, o zamandan beri susmuyor. Başını duvara vuruyor, "
             'kendi bacaklarını tokatlıyor, iki kez kustu. Elini sık sık karnının altına götürüyor ama dokunmamıza '
             'izin vermiyor. Yürümek istemiyor, yatakta kıvrılıp yatıyor. Ateşi yok, ishali yok. Kabız kaldığında da '
             'böyle huzursuz olur ama hiç bu kadar değil. Kalabalıktan ve dokunulmaktan hoşlanmaz, kulaklığını takınca '
             "biraz sakinleşir.' Düzenli risperidon kullanıyor. Bilinen başka hastalığı yok.",
  'final_diagnosis': 'Akut Sol Testis Torsiyonu (Spermatik Kord Torsiyonu ve Akut Testiküler İskemi; Sözel İletişimi '
                     'Olmayan Otizmli Adölesan)',
  'disposition': 'Sarı Alanda Acil Renkli Doppler USG + Eş Zamanlı Çocuk Cerrahisi / Üroloji Konsültasyonu ile Altın 6 '
                 'Saat İçinde Acil Cerrahi Detorsiyon ve Bilateral Orşiopeksi',
  'case_pearl': 'Sözel iletişimi olmayan otizmli çocukta ağrı çoğu zaman ağlama, bağırma, kendine vurma, uyku '
                'bozukluğu, yeme reddi veya hareket etmek istememe gibi davranış değişiklikleriyle kendini gösterir. '
                "Bu belirtileri 'davranış krizi' sayıp sedasyonla geçiştirmek, altta yatan cerrahi acillerin "
                'atlanmasına yol açabilir (diagnostic overshadowing: belirtilerin bilinen tanıya bağlanması). Ebeveyn '
                "çocuğun olağan davranışını en iyi bilen kişidir; 'hiç bu kadar değil' ifadesi ciddiye alınmalıdır. "
                'Muayene sakin, az uyaranlı bir ortamda, ebeveyn yanında ve onun önerdiği yöntemlerle (kulaklık, '
                'sevdiği nesne, adım adım anlatım) yapılmalı ve genital bölge dahil baştan ayağa sistematik olmalıdır. '
                'Akut skrotal ağrı ve kusma ile başvuran her çocuk ve adölesanda aksi kanıtlanana kadar testis '
                'torsiyonu düşünülmelidir. Fizik muayenede en duyarlı bulgu ipsilateral kremasterik refleks kaybıdır; '
                'testisin skrotumda yüksek ve transvers (yatay) yerleşimi ile skrotal elevasyonla ağrının azalmaması '
                '(negatif Prehn bulgusu) tanıyı destekler. Organın kurtarılabilmesi için altın pencere ilk 6 saattir '
                "(>%90 kurtarılma oranı). Renkli Doppler USG'de parankimal kan akımının izlenmemesi ve spermatik "
                'kordda girdap (whirlpool) görünümü tipiktir. Zemininde sıklıkla bilateral çan tokmağı (bell-clapper) '
                'deformitesi bulunduğundan cerrahi eksplorasyonda detorsiyon sonrası mutlaka her iki testise bilateral '
                'orşiopeksi yapılmalıdır.',
  'steps': [{'stage_title': 'Sarı Alanda İletişim ve Sistematik Muayene',
             'question': "Konuşmayan, gece 03:00'ten beri ağlayıp bağıran, kendine vuran ve iki kez kusan otizmli 13 "
                         'yaşındaki bu hastada ilk yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Bağırma ve kendine vurmayı otizme bağlı davranış krizi olarak değerlendirip İM '
                                  'midazolamla sakinleştirmek, sakinleşince muayene etmeden çocuk psikiyatrisine '
                                  'yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Sedasyonla sakinleşen hasta muayene edilmeden psikiyatri randevusu '
                                             'verilerek gözleme alındı; saatler sonra annenin ısrarıyla bakıldığında '
                                             'sol skrotum belirgin şiş ve morumsu renkteydi.',
                          'teaching_point': 'Konuşamayan çocukta yeni ve olağandışı huzursuzluk önce organik bir ağrı '
                                            'nedeni olarak düşünülmelidir; belirtileri bilinen tanıya bağlamak '
                                            '(diagnostic overshadowing) cerrahi acilleri atlatır.'},
                         {'text': 'Karnını tuttuğu ve kustuğu için yalnızca karın muayenesi yapıp ayakta direkt karın '
                                  'grafisi ve tüm batın ultrasonografisi istemek, kasık ve genital muayeneyi ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Karın grafisinde yalnızca kolonda gaita gölgeleri görüldü ve kabızlık '
                                             'düşünüldü; batın ultrasonografisi sırası beklenirken geçen sürede iskemi '
                                             'süresi uzadı.',
                          'teaching_point': 'Elini karnının altına götüren ve kusan erkek çocukta kasık ve skrotum '
                                            'muayenesi atlanmamalıdır; skrotal ağrı sıklıkla karın ağrısı gibi '
                                            'yansır.'},
                         {'text': 'Annesini yanında tutup sakin, az uyaranlı bir odada annenin önerdiği yöntemlerle '
                                  'yaklaşmak; genital bölge dahil baştan ayağa sistematik muayene yapmak',
                          'is_correct': True,
                          'explanation': 'Sözel iletişimi olmayan çocukta ağrının kaynağını bulmanın yolu ebeveynin '
                                         'rehberliğinde sakin bir ortamda yapılan tam ve sistematik muayenedir. Kusma '
                                         've elin karnın altına götürülmesi, kasık ve skrotumun mutlaka muayene '
                                         'edilmesini gerektirir.',
                          'new_finding': 'Vital Bulgular: TA 124/78 mmHg, KTA 118/dk, Ateş 36.7°C, SpO2 %99. Işıkları '
                                         'kısılmış odada, kulaklığı takılı ve annesi elini tutarken muayene edildi. '
                                         'Kulak, boğaz, diş ve karın muayenesi doğal; karın palpasyonuna belirgin '
                                         'tepki yok. Sol hemiskrotuma dokunulunca çığlık atıp bacaklarını kapatıyor. '
                                         'Sol hemiskrotum hiperemik ve ödemli; sol gonad skrotum üst polünde yüksek ve '
                                         'transvers yerleşimli, palpasyonla ileri derecede hassas. Skrotal elevasyonla '
                                         'huzursuzlukta azalma olmadı. Sol kremasterik refleks alınamadı. Sağ gonad ve '
                                         'sağ kremasterik refleks doğal.'},
                         {'text': 'İletişim kurulamadığı için İV metamizolle ağrıyı dindirip bir saat sonra yeniden '
                                  'değerlendirmek, bu sürede anneyi bekleme salonuna alıp çocuğu yalnız izlemek',
                          'is_correct': False,
                          'scenario_update': 'Annesinden ayrılan çocuğun ajitasyonu arttı, damar yolu çıktı ve muayene '
                                             'bir saatten fazla gecikti.',
                          'teaching_point': 'Otizmli çocukta ebeveyni ayırmak ajitasyonu artırır; analjezi verilebilir '
                                            'ancak muayeneyi ertelemenin gerekçesi olmamalıdır.'}]},
            {'stage_title': 'Radyolojik Görüntüleme ve Zamanlama Stratejisi',
             'question': 'Kremasterik refleks kaybı, sol gonadda yüksek-transvers yerleşim ve elevasyonla '
                         'huzursuzluğun azalmaması saptanan 3. saatindeki hastada bir sonraki adımınız ne olmalıdır?',
             'options': [{'text': 'Öncelikle tam kan sayımı, CRP, sedimantasyon ve idrar kültürü sonuçlarını beklemek, '
                                  'inflamatuar belirteçler normal gelirse radyolojik görüntüleme ve konsültasyon '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'Laboratuvar sonuçlarının çıkması için geçen 90 dakika sonunda lökosit ve '
                                             'CRP hafif yüksek saptandı, bu sırada iskemi süresi 4.5 saati aştı.',
                          'teaching_point': 'Akut vasküler skrotal patolojilerde akut faz reaktanları normal veya '
                                            'hafif yüksek olabilir; laboratuvar beklemek organ kaybına yol açan '
                                            'tehlikeli bir gecikmedir.'},
                         {'text': 'Semptomların başlangıcından itibaren henüz 3 saat geçtiği için sabah mesai saatinde '
                                  'elektif skrotal manyetik rezonans görüntüleme planlayarak hastayı gözlemde tutmak',
                          'is_correct': False,
                          'scenario_update': 'Sabah mesai saatine kadar bekletilen hastada toplam iskemi süresi 8 '
                                             'saati geçti ve sol parankimde kalıcı koagülasyon nekrozu gelişti.',
                          'teaching_point': 'Akut skrotal perfüzyon bozukluğunda organın kurtarılabilmesi için altın '
                                            'pencere ilk 6 saattir; elektif görüntüleme için asla beklenemez.'},
                         {'text': 'Radyolojik görüntüleme veya cerrahi konsültasyon istemeden önce acil serviste '
                                  'sedasyon altında dışarıdan zorlu manuel rotasyon manevrasını defalarca '
                                  'tekrarlayarak uygulamaya çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Körlemesine yapılan zorlu manuel manevra korddaki dolanmayı daha da '
                                             'sıkılaştırarak ağrıyı şiddetlendirdi ve cerrahi ekip çağrılmadığı için '
                                             'zaman kaybedildi.',
                          'teaching_point': 'Manuel müdahale asla acil cerrahi konsültasyonun ve ameliyathane '
                                            'hazırlığının yerini tutmaz; kontrolsüz manevralar rotasyon derecesini '
                                            'artırabilir.'},
                         {'text': 'Oral alımı durdurup İV analjezi başlamak, derhal Çocuk Cerrahisi/Üroloji '
                                  'konsültasyonu isteyerek gecikmeden acil skrotal Renkli Doppler USG yaptırmak',
                          'is_correct': True,
                          'explanation': 'Yüksek klinik şüphede hasta derhal ameliyata hazırlanmalı, cerrahi ekip eş '
                                         'zamanlı çağrılmalı ve ameliyatı geciktirmeyecek şekilde hızlıca Renkli '
                                         'Doppler USG ile kan akımı değerlendirilmelidir.',
                          'new_finding': 'Tam İdrar Tetkiki: Lökosit ve eritrosit yok. Acil Skrotal Renkli Doppler '
                                         'USG: Sol gonad boyutları sağa göre artmış, parankim ekojenitesi heterojen '
                                         'görünümde; sol parankimde arteriyel ve venöz kan akımının tamamen '
                                         'izlenmemesi ve kord yapılarında girdap görünümü saptandı. Sağ gonadda '
                                         'kanlanmanın doğal olduğu raporlandı.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Kremasterik refleks kaybı, yüksek-transvers gonad yerleşimi ve Renkli Doppler USG bulguları '
                         'ışığında bu hastanın kesin tanısı nedir?',
             'options': [{'text': 'Akut Bakteriyel Epididimo-Orşit',
                          'is_correct': False,
                          'scenario_update': 'Akut epididimo-orşitte kremasterik refleks genellikle korunmuştur ve '
                                             'Renkli Doppler USG incelemesinde parankim ve epididimde kan akımı '
                                             'belirgin artmıştır.',
                          'teaching_point': 'Epididimo-orşitte inflamasyona bağlı hipervaskülarite görülürken, bu '
                                            'hastada arteriyel ve venöz kan akımı tamamen kesilmiştir.'},
                         {'text': 'Akut Sol Testis Torsiyonu',
                          'is_correct': True,
                          'explanation': 'Ani başlayan skrotal ağrı, kusma, ipsilateral kremasterik refleks kaybı, '
                                         "yüksek-transvers yerleşim ve Doppler USG'de kan akımının izlenmemesi ile "
                                         'kordda girdap görünümü akut testis torsiyonunu kesinleştirir.',
                          'new_finding': 'Kesin tanı: Akut Sol Testis Torsiyonu. Semptom süresi 3.5 saat olup altın 6 '
                                         'saatlik cerrahi pencere içindedir.'},
                         {'text': 'Testiküler Apendiks (Morgagni Hidatidi) Torsiyonu',
                          'is_correct': False,
                          'scenario_update': 'Apendiks testis torsiyonunda ağrı daha hafif seyreder, testis üst '
                                             'polünde mavi nokta (blue dot) bulgusu görülür ve testisin kendi parankim '
                                             'kanlanması normaldir.',
                          'teaching_point': "Morgagni hidatidi torsiyonunda Doppler USG'de testis parankim kan akımı "
                                            'korunmuştur; tam akım kaybı ve kordda girdap işareti spermatik kord '
                                            'torsiyonunu gösterir.'},
                         {'text': 'İnkarsere İnguinal Herni ve Reaktif Hidrosel',
                          'is_correct': False,
                          'scenario_update': 'Hastanın inguinal kanalında uzanan barsak ansı saptanmamış olup Doppler '
                                             "USG'de spermatik kordda girdap görünümü ve testiküler avaskülarite "
                                             'mevcuttur.',
                          'teaching_point': 'İnguinal hernide kasık kanalından skrotuma uzanan kitle ve barsak sesleri '
                                            'saptanır; bu vakada primer patoloji spermatik kord torsiyonudur.'}]},
            {'stage_title': 'Acil Cerrahi Yönetim ve Operasyon İlkeleri',
             'question': 'Semptomların 3.5 saatinde akut sol testis torsiyonu tanısı kesinleşen bu hastada uygulanması '
                         'gereken doğru cerrahi yönetim hangisidir?',
             'options': [{'text': 'İntravenöz fraksiyone olmayan heparin antikoagülasyonu ve vazodilatatör ilaç '
                                  'infüzyonu başlayarak 6 saat izlemek, kontrol görüntülemede akım dönmezse ameliyata '
                                  'almak',
                          'is_correct': False,
                          'scenario_update': 'Mekanik olarak kendi etrafında dönmüş olan spermatik kord antikoagülan '
                                             'tedaviyle açılmadı ve 6 saatlik kritik süre aşılarak sol testis nekroze '
                                             'oldu.',
                          'teaching_point': 'Testis torsiyonu mekanik bir rotasyon sonucu gelişir; trombolitik veya '
                                            'antikoagülan tedavinin yeri yoktur, tek tedavi acil cerrahi '
                                            'detorsiyondur.'},
                         {'text': 'Acil cerrahi eksplorasyona alarak sol spermatik kord detorsiyonu ve sol orşiopeksi '
                                  'yapmak, sağlam olan sağ testise ise hiçbir cerrahi işlem uygulamamak',
                          'is_correct': False,
                          'scenario_update': 'Sol testis kurtarıldı ancak anatomik yatkınlığı devam eden karşı testise '
                                             'fiksasyon yapılmadığı için 8 ay sonra sağ testis torsiyonu gelişti.',
                          'teaching_point': 'İntravajinal testis torsiyonunun temel nedeni olan çan tokmağı '
                                            '(bell-clapper) deformitesi olguların çoğunda bilateraldir; bu nedenle '
                                            'karşı testise de profilaktik orşiopeksi yapılması zorunludur.'},
                         {'text': 'Altın 6 saat dolmadan acil cerrahi eksplorasyona almak, sol detorsiyon ve '
                                  'reperfüzyon sonrası her iki testise bilateral orşiopeksi uygulamak',
                          'is_correct': True,
                          'explanation': 'İlk 6 saat içinde yapılan acil cerrahi eksplorasyon ve detorsiyon ile '
                                         "testisin kurtarılma şansı %90'ın üzerindedir; karşı testisteki anatomik "
                                         'anomali riski nedeniyle bilateral orşiopeksi standart yaklaşımdır.',
                          'new_finding': 'Hasta 4. saatinde acil ameliyathaneye alındı; 540 derece dönmüş olan sol '
                                         'spermatik kord detorsiyone edildi. Ilık serum fizyolojik uygulaması sonrası '
                                         'sol testis hızla pembeleşti ve kanlanması geri döndü. Her iki testise '
                                         'bilateral orşiopeksi uygulanarak organ kaybı olmadan taburcu edildi.'},
                         {'text': 'Doppler USG incelemesinde arteriyel kan akımı hiç izlenmediği için testisin nekroze '
                                  'olduğunu kabul ederek detorsiyon denemeden doğrudan sol orşiektomi yapmak',
                          'is_correct': False,
                          'scenario_update': 'Henüz 3.5 saatlik iskemisi olan ve detorsiyonla kurtarılabilecek '
                                             'canlılıktaki sol testis, reperfüzyon yanıtı beklenmeden gereksiz yere '
                                             'çıkarılmış oldu.',
                          'teaching_point': "Doppler USG'de akım olmaması testisin öldüğünü değil torsiyone olduğunu "
                                            'gösterir; ameliyatta detorsiyon ve ılık kompres sonrası canlılık mutlaka '
                                            'değerlendirilmelidir.'}]}]},
 {'id': 'S18',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '3.5 Yaş',
  'gender': 'Kız',
  'complaint': 'Vücutta aniden ortaya çıkan çok sayıda toplu iğne başı büyüklüğünde kırmızı-mor döküntüler, bacaklarda '
               'morluklar ve diş eti kanaması',
  'history': "Annesi 3.5 yaşındaki kızını Sarı Alana getiriyor: 'Yaklaşık iki hafta önce hafif bir üst solunum yolu "
             'enfeksiyonu geçirmişti ve tamamen iyileşmişti. Dün akşam banyo yaptırırken cildinde hiçbir şey yoktu; bu '
             'sabah uyandığında bacaklarında, kollarında ve gövdesinde yüzlerce minik kırmızı nokta ve birkaç büyük '
             'morluk fark ettim. Sabah dişini fırçalarken diş etleri kanadı ve ağız içinde kanlı kabarcıklar gördüm. '
             "Ateşi yok, iştahı ve neşesi yerinde.'",
  'final_diagnosis': 'Akut İmmün Trombositopenik Purpura (Primer Akut Pediatrik İTP - Mukozal Kanamalı)',
  'disposition': 'Sarı Alanda Tam Kan Sayımı ve Periferik Yayma Doğrulaması + Aktif Mukozal Kanama (Islak Purpura) ve '
                 'Derin Trombositopeni Nedeniyle IVIG (0.8-1 g/kg) Tedavisi ve Servis Yatışı',
  'case_pearl': 'Pediatrik akut İTP, sıklıkla viral bir enfeksiyondan 1-4 hafta sonra genel durumu iyi olan çocukta '
                'aniden gelişen peteşi, ekimoz ve izole trombositopeni tablosudur. Tanıda altın kural: Fizik muayenede '
                'hepatosplenomegali veya patolojik lenfadenopati olmamalı, hemogramda diğer seriler (Hb, WBC) normal '
                'olmalı ve periferik yaymada blast veya şistosit bulunmadığı teyit edilmelidir. Ağız içi hemorajik '
                "büller ve diş eti kanaması ('ıslak purpura') ile PLT <10.000-20.000/mm³ varlığında intrakraniyal "
                'kanama riskini önlemek için IVIG (0.8-1 g/kg tek doz) veya kortikosteroid başlanır. Hayatı tehdit '
                'eden masif kanama olmadıkça trombosit transfüzyonu, İM enjeksiyon ve NSAİİ/aspirin kontrendikedir.',
  'steps': [{'stage_title': 'Sarı Alanda Fizik Muayene ve Kanama Değerlendirmesi',
             'question': 'Yaygın peteşi, ekimoz ve diş eti kanaması ile başvuran ancak genel durumu iyi olan 3.5 '
                         'yaşındaki çocukta ilk muayene ve yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Koagülopati olasılığına karşı kan tetkiki öncesinde uyluk kasından intramusküler 5 '
                                  'mg K vitamini uygulamak ve diş eti ağrısı için oral ibuprofen vermek',
                          'is_correct': False,
                          'scenario_update': 'İntramusküler enjeksiyon yapılan uyluk bölgesinde kısa sürede derin doku '
                                             'içi hematom gelişti ve verilen ibuprofen sonrası diş eti kanaması '
                                             'şiddetlendi.',
                          'teaching_point': 'Kanama diyatezi veya peteşiyal döküntüsü olan hastalarda kas içi '
                                            'enjeksiyonlar derin hematom riski nedeniyle, NSAİİ grubu ilaçlar ise '
                                            'agregasyon bozukluğu nedeniyle kontrendikedir.'},
                         {'text': 'Vital bulguları ve nörolojik durumu değerlendirmek, ağız mukozasında hemorajik '
                                  'bülleri, lenfadenopati ve hepatosplenomegali varlığını kontrol ederek travmadan '
                                  'korumak',
                          'is_correct': True,
                          'explanation': 'Peteşi ve ekimozla başvuran çocukta mukozal kanama varlığı intrakraniyal '
                                         'kanama riskini belirlerken, organomegali ve lenfadenopati kontrolü malign '
                                         'infiltratif süreçleri dışlamak için kritiktir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 96/dk, SS 20/dk, TA 94/58 mmHg. Genel '
                                         'durumu iyi, bilinci açık, aktif. Ciltte yaygın basmakla solmayan peteşiler '
                                         've alt ekstremitelerde 2-3 cm çapında ekimozlar mevcut. Bukkal mukozada iki '
                                         'adet hemorajik bül ve diş eti kenarında sızıntı tarzında kanama izlendi. '
                                         'Servikal/aksiller patolojik lenfadenopati yok, karaciğer ve dalak kot '
                                         'altında ele gelmiyor, nörolojik muayene doğal.'},
                         {'text': 'Basmakla solmayan döküntüleri invaziv bakteriyel enfeksiyon kabul ederek fizik '
                                  'muayeneyi tamamlamadan lomber ponksiyon yapmak ve yüksek doz seftriakson başlamak',
                          'is_correct': False,
                          'scenario_update': 'Hemodinamik olarak stabil ve ateşsiz olan hastada trombosit düzeyi '
                                             'görülmeden yapılan lomber ponksiyon spinal epidural hematom riskini '
                                             'ciddi ölçüde artırdı.',
                          'teaching_point': 'Ateşi olmayan ve genel durumu iyi olan peteşili çocukta öncelikle kanama '
                                            'diyatezi değerlendirilmelidir; hemostaz teyit edilmeden lomber ponksiyon '
                                            'yapılması spinal hematom açısından kontrendikedir.'},
                         {'text': 'Ağız içi hemorajik bülleri lokal travmaya bağlayıp kanama odaklarını povidon iyotlu '
                                  'gazlı bezle sertçe kazıyarak temizlemek ve gargara önermek',
                          'is_correct': False,
                          'scenario_update': 'Mukozal hemorajik büllerin mekanik olarak kazınması durdurulamayan '
                                             'yaygın mukozal sızıntı kanamasına ve çocuğun kanı yutarak kusmasına yol '
                                             'açtı.',
                          'teaching_point': 'Ağız mukozasındaki hemorajik büller ciddi mukozal kanama göstergesidir; '
                                            'kesinlikle mekanik olarak patlatılmamalı veya travmatize '
                                            'edilmemelidir.'}]},
            {'stage_title': 'Laboratuvar Tetkikleri ve Morfolojik İnceleme',
             'question': 'Organomegalisi olmayan ancak yaygın peteşi ve oral mukozal hemorajik bülleri saptanan bu '
                         'çocukta doğrulama için hangi tetkikleri istemelisiniz?',
             'options': [{'text': 'Tam kan sayımı, retikülosit, koagülasyon parametreleri (PT, aPTT) ve mutlaka '
                                  'periferik kan yayması isteyerek diğer hücre serilerini ve morfolojiyi '
                                  'değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Edinsel izole kanama diyatezlerinde hemogramda hemoglobin ve lökosit '
                                         'serisinin normal olduğunun görülmesi ve periferik yaymada atipik hücre, '
                                         'blast veya şistosit bulunmadığının doğrulanması şarttır.',
                          'new_finding': 'Laboratuvar: WBC 7.600/mm³, Hb 12.6 g/dL, MCV 79 fL, PLT 6.000/mm³, '
                                         'Retikülosit %1.1, PT 12.1 sn, aPTT 28 sn, Fibrinojen 260 mg/dL. Periferik '
                                         'Yayma: Eritrosit normokrom normositer, şistosit veya fragmente eritrosit '
                                         'yok; lökosit dağılımı normal, blast veya atipik hücre izlenmedi; '
                                         'trombositler her alanda tekli ve nadir, yer yer iri trombositler görüldü.'},
                         {'text': 'Periferik kan yayması değerlendirmesi yapmadan doğrudan acil ameliyathane '
                                  'koşullarında genel sedasyon altında kemik iliği aspirasyonu ve trepan biyopsisi '
                                  'işlemi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Tipik öyküsü ve normal fizik muayenesi olan küçük çocukta periferik '
                                             'yayma görülmeden yapılan invaziv kemik iliği girişimi işlem yerinde '
                                             'ciddi kanamaya neden oldu.',
                          'teaching_point': 'ASH ve uluslararası pediatrik hematoloji kılavuzlarına göre, fizik '
                                            'muayenesi ve periferik yayması tipik olan çocuklarda tanı için rutin '
                                            'kemik iliği aspirasyonu önerilmez.'},
                         {'text': 'Yalnızca cilt kanama zamanı, sedimantasyon ve CRP testleri isteyerek periferik '
                                  'yayma bakmadan hastaya acil taze donmuş plazma infüzyonu uygulamaya başlamak',
                          'is_correct': False,
                          'scenario_update': 'Koagülasyon faktör eksikliği olmayan hastaya verilen taze donmuş plazma '
                                             'kanamayı durdurmadı ve periferik yayma bakılmadığı için ayırıcı tanı '
                                             'eksik kaldı.',
                          'teaching_point': 'Peteşiyal ve mukozal kanamalarda birincil hemostaz bozukluğu ön '
                                            'plandadır; tanı için tam kan sayımı ve periferik yayma incelemesi '
                                            'zorunludur.'},
                         {'text': 'Henüz hiçbir kan örneği almadan önce olası iç kanamaları taramak amacıyla sedasyon '
                                  'vererek kontrastlı beyin tomografisi ve batın ultrasonografisi çektirmek',
                          'is_correct': False,
                          'scenario_update': 'Nörolojik muayenesi tamamen normal olan çocukta laboratuvar tetkiki '
                                             'yapılmadan radyoloji ünitesinde vakit kaybedildi ve sedasyon işlemi ek '
                                             'risk oluşturdu.',
                          'teaching_point': 'Nörolojik semptom veya bulgusu olmayan hastalarda rutin kraniyal '
                                            'görüntüleme endike değildir; öncelik hızlıca tam kan sayımı ve periferik '
                                            'yayma değerlendirmesidir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Viral enfeksiyon sonrası gelişen peteşi, oral mukozal hemorajik büller, PLT 6.000/mm³ ve '
                         'normal periferik yayma bulgularıyla kesin tanınız nedir?',
             'options': [{'text': 'Pediatrik Akut Lenfoblastik Lösemi (ALL)',
                          'is_correct': False,
                          'scenario_update': 'Akut lösemide genellikle anemi/nötropeni gibi diğer serilerin tutulumu, '
                                             'hepatosplenomegali, lenfadenopati ve periferik yaymada blast hücreleri '
                                             'görülür.',
                          'teaching_point': 'Bu hastada organomegali yoktur, hemoglobin ve lökosit değerleri normaldir '
                                            've periferik yaymada blast izlenmemiştir.'},
                         {'text': 'Edinsel Trombotik Trombositopenik Purpura (TTP)',
                          'is_correct': False,
                          'scenario_update': 'Trombotik mikroanjiyopatilerde hemolitik anemi, retikülositoz ve '
                                             'periferik yaymada parçalanmış eritrositler (şistositler) bulunur.',
                          'teaching_point': 'Hastanın hemoglobini normal olup periferik yaymasında şistosit ve '
                                            'mikroanjiyopatik hemoliz bulgusu yoktur.'},
                         {'text': 'Akut İmmün Trombositopenik Purpura (İTP)',
                          'is_correct': True,
                          'explanation': 'Viral enfeksiyon sonrası sağlıklı görünümde çocukta gelişen izole derin '
                                         'trombositopeni, normal eritrosit/lökosit serisi ve iri trombositler içeren '
                                         'normal periferik yayma akut primer İTP için tanısaldır.',
                          'new_finding': 'Kesin tanı: Akut İmmün Trombositopenik Purpura (Primer Akut İTP). Ağız içi '
                                         'ıslak purpura ve diş eti kanaması mevcut.'},
                         {'text': 'Kalıtsal Von Willebrand Hastalığı Tip 1',
                          'is_correct': False,
                          'scenario_update': "Von Willebrand hastalığı Tip 1'de trombosit sayısı tamamen normaldir; "
                                             'trombosit fonksiyon bozukluğuna bağlı mukozal kanama görülür.',
                          'teaching_point': 'PLT 6.000/mm³ düzeyinde derin trombositopeni Von Willebrand Tip 1 ile '
                                            "açıklanamaz; tablo edinsel immün yıkıma bağlı akut İTP'dir."}]},
            {'stage_title': 'Sarı Alanda Tedavi Seçimi ve Kanama Yönetimi',
             'question': 'Trombosit sayısı 6.000/mm³ olan ve ağız mukozasında aktif hemorajik bülleri (ıslak purpura) '
                         'bulunan 3.5 yaşındaki İTP hastasında en uygun tedavi yaklaşımı hangisidir?',
             'options': [{'text': 'Trombosit sayısını hızla normale getirmek amacıyla acilen 2 ünite aferez trombosit '
                                  'süspansiyonu transfüze etmek ve 4 saat sonra taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Transfüze edilen trombositler dolaşımdaki anti-trombosit otoantikorlar '
                                             'tarafından kısa sürede yıkıma uğradı, kontrol trombosit sayısı 8.000/mm³ '
                                             'kaldı ve mukozal kanama sürdü.',
                          'teaching_point': 'İTP patofizyolojisinde otoantikor aracılı periferik yıkım olduğundan, '
                                            'yaşamı tehdit eden masif kanama olmadıkça tek başına trombosit '
                                            'transfüzyonu etkisizdir ve önerilmez.'},
                         {'text': 'Aktif mukozal kanama ve derin trombositopeni nedeniyle 0.8-1 g/kg tek doz IVIG '
                                  'infüzyonu (veya prednizolon) başlayarak hastayı servise yatırmak',
                          'is_correct': True,
                          'explanation': 'Ağız içi ıslak purpura ve diş eti kanaması varlığında intrakraniyal ve majör '
                                         'kanama riskini azaltmak için trombosit sayısını en hızlı yükselten IVIG '
                                         '(0.8-1 g/kg) veya kortikosteroid tedavisiyle yatış endikedir.',
                          'new_finding': 'Hastaya 0.8 g/kg dozunda IVIG infüzyonu uygulandı ve travma önlemleri '
                                         'alınarak pediatri servisine yatırıldı. 24. saatte yapılan kontrol hemogramda '
                                         'trombosit sayısı 52.000/mm³ düzeyine yükseldi, mukozal kanama tamamen '
                                         'durdu.'},
                         {'text': 'Genel durumu iyi olduğu için aktif mukozal kanamaya rağmen hiçbir ilaç vermeden 3 '
                                  'ay sonra kontrole gelmek üzere eve göndermek',
                          'is_correct': False,
                          'scenario_update': 'Tedavisiz eve gönderilen çocukta gece şiddetli epistaksis ve '
                                             'gastrointestinal sistem kanaması gelişerek acil servise hipovolemik '
                                             'tabloda tekrar başvuru gerçekleşti.',
                          'teaching_point': 'Sadece cilt bulgusu (kuru purpura) olan hafif olgularda yakın izlem '
                                            'seçilebilir; ancak ıslak purpura (aktif mukozal kanama) ve PLT '
                                            '<10.000/mm³ varlığında farmakolojik tedavi ve yatış gerekir.'},
                         {'text': 'Birinci basamak acil tedavi olarak hastayı çocuk cerrahisine danışıp acil '
                                  'splenektomi ameliyatına hazırlamak ve profilaktik intravenöz antibiyotik tedavisi '
                                  'başlamak',
                          'is_correct': False,
                          'scenario_update': 'Akut yeni tanı pediatrik olguda medikal tedavi denenmeden cerrahi '
                                             'planlanması hematoloji konsültasyonu ile durdurularak gereksiz organ '
                                             'kaybı önlendi.',
                          'teaching_point': 'Çocukluk çağı akut İTP olgularının %80-85 kadarı 6-12 ay içinde '
                                            'kendiliğinden tam remisyona girer; splenektomi yalnızca 12 aydan uzun '
                                            'süren dirençli kronik olgularda son basamakta düşünülür.'}]}]},
 {'id': 'S19',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '2 Yaş',
  'gender': 'Erkek',
  'complaint': 'Büyükannesinin komodinin üzerindeki antihipertansif ilaç kutusundaki tabletlerden yutma; 2 saat sonra '
               'başlayan halsizlik, uyuklama, baş dönmesi ve soğuk terleme',
  'history': "Ailesi 2 yaşındaki (12 kg) erkek çocuğu Sarı Alana getiriyor: 'Yaklaşık 1.5 saat önce büyükannesinin "
             'komodinin üzerindeki antihipertansif ilaç kutusunu açmış. Yerde üzerinde isim yazmayan yırtılmış boş '
             "blister folyolar bulduk, 10 mg'lık yuvarlak beyaz tabletlerden en az 5-6 tanesini çiğneyip yuttuğunu "
             'düşünüyoruz. İlk saatte hareketliydi ancak son yarım saattir rengi soldu, soğuk terliyor, ayakta '
             "duramıyor ve uykuya meyilli hale geldi.'",
  'final_diagnosis': 'Kalsiyum Kanal Blokeri (Amlodipin) İntoksikasyonu (Vazoplejik Şok, Metabolik Laktik Asidoz ve '
                     'Hiperglisemi)',
  'disposition': 'Sarı Alanda Aktif Kömür + Kristaloid Bolusu + İV %10 Kalsiyum Glukonat + Yüksek Doz İnsülin-Öglisemi '
                 'Tedavisi (HIET) ve Norepinefrin İnfüzyonu ile Çocuk Yoğun Bakım Ünitesine Yatış',
  'case_pearl': 'Kalsiyum Kanal Blokerleri (KKB - özellikle amlodipin, verapamil, diltiazem) küçük çocuklarda tek bir '
                "tabletle bile ölümcül olabilen ('One Pill Can Kill') kardiyovasküler toksinlerdir. Diğer "
                'antihipertansiflerden (beta-bloker, klonidin, ACEİ) en önemli ayırıcı özelliği: Pankreas beta '
                'hücrelerindeki L-tipi kalsiyum kanallarını bloke ederek insülin salınımını baskılaması ve '
                'HİPERGLİSEMİ + LAKTİK ASİDOZ + DİRENÇLİ HİPOTANSİYON yapmasıdır (beta-blokerler hipoglisemi ve '
                'bradikardi, klonidin ise miyozis ve solunum depresyonu yapar). Dihidropiridin grubu (amlodipin) erken '
                'dönemde refleks sinüs taşikardisi ile derin vazopleji yapar. Tedavide aktif kömür, izotonik sıvı, İV '
                'kalsiyum glukonat, norepinefrin ve en kritik metabolik antidot olarak Yüksek Doz İnsülin-Öglisemi '
                'Tedavisi (HIET: 1 Ü/kg bolus + 0.5-1 Ü/kg/saat infüzyon ve dekstroz desteği) uygulanır.',
  'steps': [{'stage_title': 'Sarı Alanda Toksikolojik Değerlendirme ve Monitörizasyon',
             'question': 'Ne olduğu bilinmeyen antihipertansif tabletlerden çoklu miktarda yutma sonrası perfüzyon '
                         'bozukluğu ve letarji ile başvuran 2 yaşındaki çocukta ilk değerlendirme yaklaşımınız ne '
                         'olmalıdır?',
             'options': [{'text': 'Midedeki tabletleri hızla uzaklaştırmak amacıyla çocuğa acil serviste hipertonik '
                                  'tuzlu su içirerek veya farenksi uyararak zorla kusturma işlemi uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Uykuya meyilli olan çocukta zorla kusturma girişimi sırasında öğürme '
                                             'refleksi yetersiz kaldığı için mide içeriği akciğerlere aspire edildi ve '
                                             'hipoksi gelişti.',
                          'teaching_point': 'Akut zehirlenmelerde mekanik uyarıyla veya tuzlu su/ipeka ile kusturma '
                                            'girişimi aspirasyon pnömonisi ve hipernatremi riski nedeniyle kesinlikle '
                                            'kontrendikedir.'},
                         {'text': 'Kan basıncı ölçümü ve kan şekeri kontrolü yapmadan önce toksik ilacın böbreklerden '
                                  'atılımını hızlandırmak için intravenöz furosemid uygulayarak diürezi zorlamak',
                          'is_correct': False,
                          'scenario_update': 'Zaten periferik vazodilatasyon ve hipotansiyonu olan hastada uygulanan '
                                             'loop diüretik intravasküler hacmi daha da azaltarak derin '
                                             'kardiyovasküler kollapsa yol açtı.',
                          'teaching_point': 'Antihipertansif ilaç zehirlenmelerinde zorlu diürezin yeri yoktur; '
                                            'diüretik verilmesi hipovolemiyi ve şok tablosunu ağırlaştırır.'},
                         {'text': 'Pupil çaplarına bakarak opioid/alfa-2 agonist zehirlenmesi varsaymak ve vital '
                                  'bulguları görmeden doğrudan intravenöz yüksek doz nalokson bolusu puşe etmek',
                          'is_correct': False,
                          'scenario_update': 'Pupilleri izokorik olan ve solunum depresyonu bulunmayan hastada ampirik '
                                             'nalokson uygulamasına rağmen hipotansiyon ve perfüzyon bozukluğu hiç '
                                             'düzelmedi.',
                          'teaching_point': 'Farklı antihipertansif sınıflarını ayırt etmek için öncelikle kan '
                                            'basıncı, kalp hızı, EKG, kapiller kan şekeri ve kan gazı parametreleri '
                                            'bütünsel değerlendirilmelidir.'},
                         {'text': 'Kardiyak monitörizasyon, 12 derivasyonlu EKG, kan basıncı, kapiller dolum zamanı, '
                                  'kan şekeri ve kan gazı/laktat ölçümünü hızla yapmak',
                          'is_correct': True,
                          'explanation': 'Bilinmeyen antihipertansif zehirlenmelerinde hipotansiyon derecesi, kalp '
                                         'hızı/ritmi, laktik asidoz ve özellikle glukoz düzeyi etken ilaç grubunu '
                                         'ayırt etmede en önemli klinik ipuçlarıdır.',
                          'new_finding': 'Vital Bulgular: TA 64/34 mmHg, KTA 142/dk, SS 28/dk, SpO2 %97, KDZ 4 saniye, '
                                         'ekstremiteler soğuk, pupiller izokorik ve miyozis yok. EKG: Sinüs '
                                         'taşikardisi, PR 130 ms, QRS 80 ms. Parmak ucu kan şekeri: 246 mg/dL. Venöz '
                                         'Kan Gazı: pH 7.24, HCO3 15 mmol/L, Baz Açığı -11, Laktat 4.8 mmol/L, K+ 3.9 '
                                         'mEq/L.'}]},
            {'stage_title': 'Gastrointestinal Dekontaminasyon ve İlk Resüsitasyon',
             'question': 'Alımdan 1.5 saat sonra başvuran, derin hipotansiyonu (64/34 mmHg), metabolik laktik asidozu '
                         've belirgin hiperglisemisi (246 mg/dL) olan 12 kg çocukta ilk basamak müdahaleniz ne '
                         'olmalıdır?',
             'options': [{'text': 'Hava yolunu koruyarak 1 g/kg aktif kömür vermek, 20 mL/kg izotonik kristaloid '
                                  'bolusu ve İV %10 kalsiyum glukonat (0.6 mL/kg) uygulamak',
                          'is_correct': True,
                          'explanation': 'Erken dönemde aktif kömür gastrointestinal emilimi azaltır; izotonik sıvı '
                                         'bolusu damar içi hacmi desteklerken intravenöz kalsiyum tuzu miyokardiyal '
                                         'kontraktiliteyi ve vasküler tonusu artırır.',
                          'new_finding': '12 gram aktif kömür uygulandı, 20 mL/kg %0.9 NaCl bolusu ve 0.6 mL/kg %10 '
                                         'kalsiyum glukonat yavaş intravenöz infüzyonla verildi. Müdahale sonrası kan '
                                         'basıncı 72/40 mmHg, KTA 136/dk, kan şekeri 258 mg/dL, kontrol laktat 4.5 '
                                         'mmol/L ölçüldü; hipoperfüzyon bulguları devam ediyor.'},
                         {'text': 'Kan şekeri 246 mg/dL olduğu için diyabetik ketoasidoz protokolü başlatarak sadece '
                                  '0.05 Ü/kg/saat düşük doz insülin ve hipotonik sıvı infüzyonu vermek',
                          'is_correct': False,
                          'scenario_update': 'İdrarda ketonu negatif olan ve ilaç kaynaklı pankreatik insülin salınım '
                                             'baskılanması yaşayan hastada hipotonik sıvı uygulaması hipotansiyonu '
                                             'daha da derinleştirdi.',
                          'teaching_point': 'Vazoplejik şoktaki zehirlenme hastasında hiperglisemi primer diyabete '
                                            'değil, pankreas beta hücrelerindeki iyon kanalı blokajına bağlıdır; '
                                            'hipotonik sıvı verilmemelidir.'},
                         {'text': 'Derin hipotansiyonu düzeltmek amacıyla kristaloid sıvı veya kalsiyum desteği '
                                  'vermeden doğrudan periferik damardan beta-agonist izoproterenol ve sodyum '
                                  'nitroprusid infüzyonu başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Periferik vazodilatatör etki mekanizmasına sahip bu ilaçların verilmesi '
                                             'sistemik vasküler direnci tamamen düşürerek kan basıncını ölçülemeyecek '
                                             'düzeye indirdi.',
                          'teaching_point': 'Periferik vazodilatasyonun ön planda olduğu antihipertansif '
                                            'toksisitelerinde vazodilatatör ajanlar ve saf beta-2 agonistler '
                                            'hipotansiyonu ağırlaştırır.'},
                         {'text': 'Alımdan 1.5 saat geçtiği için çok geniş çaplı orogastrik tüp takarak 3 litre musluk '
                                  'suyu ile mide lavajı yapmak ve aktif kömür vermemek',
                          'is_correct': False,
                          'scenario_update': 'Küçük çocukta musluk suyu ile yapılan yüksek hacimli gastrik lavaj '
                                             'hiponatremiye, hipotermiye ve mide mukozası travmasına yol açarken '
                                             'emilimi engellemedi.',
                          'teaching_point': 'Çocuklarda rutin mide lavajı önerilmez ve musluk suyu su zehirlenmesine '
                                            'yol açar; uygun vakalarda 1 g/kg aktif kömür tercih edilmelidir.'}]},
            {'stage_title': 'Klinik Tanı ve Toksidrom Ayrımı',
             'question': 'Antihipertansif alımı sonrası derin hipotansiyon, refleks taşikardi, metabolik laktik asidoz '
                         've belirgin hiperglisemi (258 mg/dL) birlikteliği hangi ilaç grubu zehirlenmesini gösterir?',
             'options': [{'text': 'Beta-Bloker (Propranolol) Akut İntoksikasyonu',
                          'is_correct': False,
                          'scenario_update': 'Beta-bloker zehirlenmesinde belirgin bradikardi ve '
                                             'glukoneogenez/glikojenoliz baskılanmasına bağlı hipoglisemi görülür; bu '
                                             'hastada refleks taşikardi ve belirgin hiperglisemi mevcuttur.',
                          'teaching_point': 'Antihipertansif zehirlenmesinde hiperglisemi kalsiyum kanal blokerlerini, '
                                            'hipoglisemi ise beta-blokerleri işaret eden en önemli metabolik ayırıcı '
                                            'bulgudur.'},
                         {'text': 'Santral Alfa-2 Agonist (Klonidin) İntoksikasyonu',
                          'is_correct': False,
                          'scenario_update': 'Klonidin zehirlenmesinde opioid benzeri toksidrom (toplu iğne başı '
                                             'miyozis, bradikardi, apne/solunum depresyonu ve koma) görülür; belirgin '
                                             'hiperglisemi beklenmez.',
                          'teaching_point': 'Hastada miyozis ve solunum depresyonu olmaması, aksine hiperglisemi ve '
                                            'laktik asidozla giden vazoplejik şok bulunması klonidin toksisitesini '
                                            'dışlar.'},
                         {'text': 'Kalsiyum Kanal Blokeri (Amlodipin) İntoksikasyonu',
                          'is_correct': True,
                          'explanation': 'L-tipi kalsiyum kanallarının blokajı vasküler düz kasta gevşeme (derin '
                                         'hipotansiyon ve refleks taşikardi), doku hipoperfüzyonu (laktik asidoz) ve '
                                         'pankreas beta hücrelerinden insülin salınımının durmasıyla karakteristik '
                                         'hiperglisemiye yol açar.',
                          'new_finding': 'Kesin tanı: Kalsiyum Kanal Blokeri (Amlodipin) İntoksikasyonu. Ailenin evden '
                                         'getirdiği ilaç kutusu da Amlodipin 10 mg olarak doğrulandı.'},
                         {'text': 'Anjiyotensin Dönüştürücü Enzim İnhibitörü İntoksikasyonu',
                          'is_correct': False,
                          'scenario_update': 'ACE inhibitörü alımları çocuklarda genellikle hafif-orta hipotansiyon ve '
                                             'hiperkalemi ile seyreder; erken dönemde ağır laktik asidoz ve 258 mg/dL '
                                             'düzeyinde hiperglisemi yapmaz.',
                          'teaching_point': 'Dirençli vazoplejik şok, laktik asidoz ve pankreatik insülin blokajına '
                                            'bağlı hiperglisemi triadı ACE inhibitörlerinden ziyade kalsiyum kanal '
                                            'blokeri toksisitesine özgüdür.'}]},
            {'stage_title': 'Spesifik Antidot (HIET) ve Yoğun Bakım Yönetimi',
             'question': 'Sıvı ve İV kalsiyum glukonata rağmen hipotansiyonu (72/40 mmHg) ve laktik asidozu süren '
                         'Kalsiyum Kanal Blokeri zehirlenmeli bu çocukta en etkili spesifik tedavi nedir?',
             'options': [{'text': 'Yalnızca intravenöz glukagon (0.05 mg/kg) tek doz puşe uygulayıp Dekstroz veya '
                                  'insülin vermeden hastayı 6 saat sonra pediatri servisine çıkarmak',
                          'is_correct': False,
                          'scenario_update': 'Tek doz glukagon uygulaması kusmayı tetikledi ve kalsiyum kanal '
                                             'blokajına bağlı vazoplejik şoku düzeltmekte yetersiz kalarak '
                                             'hipotansiyonun derinleşmesine yol açtı.',
                          'teaching_point': 'Glukagon beta-bloker zehirlenmelerinde cAMP artışıyla yardımcı olabilir '
                                            'ancak ağır kalsiyum kanal blokeri şokunda tek başına yetersizdir; temel '
                                            'metabolik antidot yüksek doz insülindir.'},
                         {'text': 'Yüksek doz insülin-öglisemi protokolü (1 Ü/kg bolus, 0.5-1 Ü/kg/saat infüzyon + '
                                  'dekstroz) ve norepinefrin başlayarak Çocuk Yoğun Bakıma yatırmak',
                          'is_correct': True,
                          'explanation': 'Kalsiyum kanal blokeri toksisitesinde yüksek doz insülin-öglisemi tedavisi '
                                         '(HIET) miyokardın karbonhidrat kullanımını sağlayarak güçlü inotropik etki '
                                         'gösterir; vazopleji için norepinefrin eklenerek yoğun bakımda izlenir.',
                          'new_finding': 'Yüksek doz insülin (1 Ü/kg bolus ardından 1 Ü/kg/saat infüzyon), %10 '
                                         'Dekstroz ve norepinefrin infüzyonu başlatıldı. Saatlik glukoz ve potasyum '
                                         'takibiyle Çocuk Yoğun Bakım Ünitesine alınan hastanın 3. saatte kan basıncı '
                                         '94/56 mmHg düzeyine ulaştı ve laktat 1.6 mmol/L değerine geriledi.'},
                         {'text': 'İdrar pH değerini 7.5-8.0 aralığında tutacak şekilde yüksek doz intravenöz sodyum '
                                  'bikarbonat alkalinizasyonu ve acil aralıklı hemodiyaliz işlemi başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Plazma proteinlerine yüksek oranda (%95 üzerinde) bağlanan ve dağılım '
                                             'hacmi geniş olan ilaç hemodiyalizle temizlenemedi ve hemodinamik '
                                             'instabilite sürdü.',
                          'teaching_point': 'Amlodipin gibi kalsiyum kanal blokerleri proteine yüksek oranda '
                                            'bağlandığı ve geniş dağılım hacmine sahip olduğu için hemodiyaliz veya '
                                            'idrar alkalinizasyonu ile uzaklaştırılamaz.'},
                         {'text': 'Kalsiyum kanal blokajını geri döndürmek amacıyla intravenöz fizostigmin salisilat '
                                  've pridostigmin vererek kolinerjik uyarıyı artırmak ve genel serviste izlemek',
                          'is_correct': False,
                          'scenario_update': 'Kolinerjik ajanların uygulanması miyokardiyal iletimi baskılayarak '
                                             'hastada ağır bradikardi, atriyoventriküler blok ve bronkore gelişmesine '
                                             'neden oldu.',
                          'teaching_point': 'Antikolinesteraz ilaçların kalsiyum kanal blokeri zehirlenmesinde yeri '
                                            'yoktur; ağır bradikardi ve AV blok yaparak kardiyovasküler kollapsı '
                                            'hızlandırırlar.'}]}]},
 {'id': 'S20',
  'category': '👁️ Göz Şikayetleri',
  'age': '4 Yaş',
  'gender': 'Erkek',
  'complaint': 'Sol göz kapaklarında kızarıklık, şiddetli şişlik, gözünü açamama, göz hareketleriyle artan ağrı ve '
               'yüksek ateş',
  'history': "Ailesi 4 yaşındaki erkek çocuğu Sarı Alana getiriyor: 'Dört gündür koyu kıvamlı burun akıntısı ve hafif "
             'ateşi vardı. Dün sabah sol gözünün iç köşesinde ve kapaklarında kızarıklık başladı; bu sabah ise göz '
             "kapakları tamamen şişti, morumsu-kırmızı bir renk aldı ve ateşi 39.2°C'ye yükseldi. Sağa sola bakmasını "
             'istediğimizde sol gözünü ettiremiyor ve gözünün arkasında çok şiddetli ağrı olduğunu söyleyerek '
             "ağlıyor.'",
  'final_diagnosis': 'Akut Orbital Selülit ve Medial Subperiosteal Abse (Akut Etmoid Sinüzit Komplikasyonu)',
  'disposition': 'Sarı Alanda Acil Kontrastlı Orbital ve Paranazal Sinüs BT + İV Geniş Spektrumlu Antibiyotik '
                 '(Seftriakson + Vankomisin) + Oftalmoloji ve KBB Konsültasyonu ile Yatış',
  'case_pearl': 'Göz kapağında kızarıklık ve şişlikle başvuran çocukta en kritik adım yüzeyel (preseptal) enfeksiyonu '
                'derin (orbital/postseptal) enfeksiyondan ayırt etmektir. Orbital selülit en sık akut etmoid sinüzitin '
                'ince lamina papyracea kemiğinden orbita içine yayılmasıyla gelişir. Klinik kırmızı bayraklar: 1) '
                'Ekstraoküler göz hareketlerinde kısıtlılık (oftalmopleji), 2) Göz hareketleriyle şiddetli ağrı, 3) '
                'Proptozis (globun öne yer değiştirmesi), 4) Kemozis (konjonktival ödem), 5) Görme azalması veya '
                'aferent pupil defektidir (RAPD). Bu bulgulardan biri bile varsa acil İV kontrastlı Orbital ve '
                'Paranazal BT çekilmeli, subperiosteal abse araştırılmalı, İV Seftriakson + Vankomisin (veya '
                'Ampisilin-Sulbaktam) başlanarak KBB ve Göz konsültasyonu ile yatırılmalıdır.',
  'steps': [{'stage_title': 'Sarı Alanda Oftalmolojik Muayene ve Kırmızı Bayraklar',
             'question': 'Akut rinosinüzit öyküsü sonrası tek taraflı göz kapağı ödemi, eritem ve yüksek ateşle '
                         'başvuran 4 yaşındaki çocukta ilk fizik muayenede neleri değerlendirmelisiniz?',
             'options': [{'text': 'Göz kapakları çok ödemli olduğu için kapakları hiç aralamadan dıştan inspeksiyonla '
                                  'yetinmek ve topikal tobramisin damla başlayıp 48 saat sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Göz küresi ve ekstraoküler hareketler değerlendirilmeden eve gönderilen '
                                             'hastada 12 saat içinde sol gözde aferent pupil defekti ve kalıcı görme '
                                             'kaybı gelişti.',
                          'teaching_point': 'Ateşli periorbital ödem ve eritemle başvuran her çocukta göz kapakları '
                                            'nazikçe aralanarak göz küresi pozisyonu, göz hareketleri ve pupil '
                                            'refleksleri mutlaka değerlendirilmelidir.'},
                         {'text': 'Şişliği indirmek amacıyla sol göz üzerine sıcak nemli kompres uygulamak ve ağrısını '
                                  'kesmek için topikal tetrakain anestezik göz damlası damlatmak',
                          'is_correct': False,
                          'scenario_update': 'Yüzeyel anestezik damla derin oküler ağrıyı geçirmediği gibi kornea '
                                             'epitel toksisitesine yol açtı ve sıcak uygulama derin dokulardaki ödemi '
                                             'artırdı.',
                          'teaching_point': 'Derin orbita dokularını ilgilendiren akut bakteriyel enfeksiyon '
                                            'şüphesinde sıcak kompres ve topikal anestezik damlalar tanısal süreci '
                                            'geciktirir ve kontrendikedir.'},
                         {'text': 'Vital bulgularla birlikte görme keskinliğini, ekstraoküler göz hareketlerini, '
                                  'globun öne yer değiştirmesini, konjonktival ödemi ve aferent pupil defektini '
                                  'değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Göz kapağı enfeksiyonlarında derin orbita yapıların etkilenip '
                                         'etkilenmediğini belirleyen temel bulgular ekstraoküler hareket kısıtlılığı, '
                                         'ağrılı göz hareketleri, proptozis, kemozis ve pupil reaksiyonlarıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 39.2°C, KTA 132/dk, SS 24/dk, TA 100/62 mmHg. '
                                         'Oftalmolojik Muayene: Sol alt ve üst göz kapağında şiddetli eritem, ısı '
                                         'artışı ve ödem; sol gözde öne doğru yer değiştirme (proptozis), yukarı ve '
                                         'dışa bakışta ağrılı hareket kısıtlılığı, konjonktival ödem (kemozis) '
                                         'saptandı. Pupiller izokorik, direkt ve indirekt ışık refleksleri pozitif, '
                                         'rölatif aferent pupil defekti yok.'},
                         {'text': 'Böcek ısırığına bağlı lokal alerjik reaksiyon düşünerek göz muayenesini '
                                  'tamamlamadan intramusküler feniramin ve deksametazon uygulayıp hastayı 2 saat '
                                  'gözleme almak',
                          'is_correct': False,
                          'scenario_update': 'Antihistaminik ve tek doz steroid uygulamasına rağmen hastanın yüksek '
                                             'ateşi, göz ağrısı ve göz hareket kısıtlılığı ilerlemeye devam etti.',
                          'teaching_point': 'Yüksek ateş, pürülan rinit öyküsü ve tek taraflı ağrılı göz kapağı '
                                            'şişliğinde alerjik anjiyoödemden önce akut bakteriyel enfeksiyon ve derin '
                                            'doku yayılımı dışlanmalıdır.'}]},
            {'stage_title': 'Radyolojik Görüntüleme ve Laboratuvar Planı',
             'question': 'Sol gözde proptozis, yukarı ve dışa bakışta ağrılı hareket kısıtlılığı ve kemozis saptanan '
                         'bu hastada en uygun tetkik yaklaşımı hangisidir?',
             'options': [{'text': 'Yalnızca iki yönlü direkt Waters ve Caldwell paranazal sinüs grafisi çekmek, '
                                  'hemogram alarak radyasyon riski nedeniyle kesitsel görüntülemeden kaçınmak',
                          'is_correct': False,
                          'scenario_update': 'Direkt sinüs grafisinde etmoid sinüslerde bulanıklık görülse de orbita '
                                             'içi yumuşak dokular ve kemik duvar komşuluğundaki koleksiyon '
                                             'değerlendirilemedi.',
                          'teaching_point': 'Proptozis ve ekstraoküler hareket kısıtlılığı varlığında direkt grafiler '
                                            'orbita içi yayılımı ve abse formasyonunu göstermede tamamen yetersizdir.'},
                         {'text': 'Damar yolu açıp hemogram, CRP ve kan kültürü almak; acil intravenöz kontrastlı '
                                  'orbital ve paranazal sinüs BT çekmek',
                          'is_correct': True,
                          'explanation': 'Proptozis, kemozis ve ağrılı göz hareket kısıtlılığı derin intraorbital '
                                         'tutulumu gösterir; koleksiyon veya abse varlığını saptamak için altın '
                                         'standart ilk görüntüleme kontrastlı orbital ve paranazal BT çekimidir.',
                          'new_finding': 'Laboratuvar: WBC 19.200/mm³ (%85 nötrofil), CRP 112 mg/L, kan kültürü '
                                         'alındı. İV Kontrastlı Orbital ve Paranazal Sinüs BT: Sol etmoid ve maksiller '
                                         'sinüste tam opasifikasyon, lamina papyracea komşuluğunda orbita medial '
                                         'duvarında 12x5 mm boyutunda periferik kontrastlanan koleksiyon, sol medial '
                                         'rektus kasında ödem ve globda anterolateral yer değiştirme saptandı. '
                                         'Kavernöz sinüs yapıları doğal izlendi.'},
                         {'text': 'Radyolojik görüntüleme yapmadan önce olası intrakraniyal yayılımı dışlamak amacıyla '
                                  'acil serviste lomber ponksiyon yapmak ve konjonktival sürüntü kültürü sonucunu '
                                  'beklemek',
                          'is_correct': False,
                          'scenario_update': 'Meninks irritasyon bulgusu olmayan hastada kesitsel görüntüleme öncesi '
                                             'lomber ponksiyon planlanması asıl anatomik odağın ve koleksiyonun '
                                             'saptanmasını geciktirdi.',
                          'teaching_point': 'Fokal intraorbital bulguları olan hastada öncelikli tanı aracı kontrastlı '
                                            'orbital ve paranazal BT incelemesidir; konjonktival sürüntü kültürü derin '
                                            'doku etkenini yansıtmaz.'},
                         {'text': 'Herhangi bir radyolojik görüntüleme yapmadan doğrudan acil serviste lokal anestezi '
                                  'altında üst göz kapağı oluğundan enjektörle ponksiyon ve aspirasyon denemek',
                          'is_correct': False,
                          'scenario_update': 'Körlemesine yapılan iğne aspirasyonu girişimi sırasında derin '
                                             'koleksiyona ulaşılamadığı gibi ekstraoküler kas ve glob perforasyonu '
                                             'tehlikesi yaşandı.',
                          'teaching_point': 'Orbita içi koleksiyonlar anatomik olarak kemik duvar ile periorbita '
                                            'arasında derin yerleşimlidir; kesitsel görüntüleme olmadan acil serviste '
                                            'körlemesine iğne girişimi kesinlikle kontrendikedir.'}]},
            {'stage_title': 'Klinik ve Radyolojik Kesin Tanı',
             'question': 'Proptozis, ağrılı oftalmopleji, kemozis ve BT incelemesinde sol orbita medial duvarında 12x5 '
                         'mm koleksiyon saptanan hastanın kesin tanısı nedir?',
             'options': [{'text': 'Komplike Olmayan Akut Preseptal (Periorbital) Selülit',
                          'is_correct': False,
                          'scenario_update': 'Preseptal selülitte enfeksiyon septum orbitale önündeki cilt ve cilt '
                                             'altı dokuyla sınırlıdır; proptozis, ağrılı hareket kısıtlılığı ve '
                                             'intraorbital koleksiyon görülmez.',
                          'teaching_point': 'Proptozis, kemozis ve ekstraoküler hareket kısıtlılığı varlığı preseptal '
                                            'selüliti dışlar ve postseptal (orbital) tutulumu kanıtlar.'},
                         {'text': 'Akut Bakteriyel Dakriyosistit ve Pürülan Konjonktivit',
                          'is_correct': False,
                          'scenario_update': 'Dakriyosistit lakrimal kese bölgesinde lokalize şişlik yapar; globda öne '
                                             'itilme, ekstraoküler kas ödemi ve medial duvar koleksiyonu oluşturmaz.',
                          'teaching_point': 'Hastadaki bulgular lakrimal kese ile sınırlı olmayıp etmoid sinüzite '
                                            'sekonder postseptal orbita boşluğu tutulumunu göstermektedir.'},
                         {'text': 'Steril İdiyopatik Orbital İnflamatuar Psödotümör Sendromu',
                          'is_correct': False,
                          'scenario_update': 'Orbital psödotümör enfeksiyöz olmayan steril bir inflamasyondur; akut '
                                             'pürülan rinosinüzit, yüksek ateş, belirgin lökositoz ve etmoid '
                                             'komşuluğunda abse ile seyretmez.',
                          'teaching_point': 'Akut rinosinüzit zemininde yüksek ateş, CRP yüksekliği ve lamina '
                                            'papyracea komşuluğunda koleksiyon varlığı bakteriyel orbital selüliti '
                                            'doğrular.'},
                         {'text': 'Akut Orbital Selülit ve Subperiosteal Abse',
                          'is_correct': True,
                          'explanation': "Proptozis, ağrılı oftalmopleji ve kemozis kliniğine BT'de etmoid sinüzit ve "
                                         'lamina papyracea komşuluğunda periferik kontrastlanan koleksiyon eşlik '
                                         'etmesi akut orbital selülit ve subperiosteal abse tanısını kesinleştirir.',
                          'new_finding': 'Kesin tanı: Akut Orbital Selülit ve Sol Medial Subperiosteal Abse (Chandler '
                                         'Evre III - Etmoid Sinüzit Komplikasyonu).'}]},
            {'stage_title': 'Multidisipliner Konsültasyon ve Tedavi Yönetimi',
             'question': 'Etmoid sinüzite sekonder akut orbital selülit ve 12x5 mm medial subperiosteal abse tanısı '
                         'alan 4 yaşındaki hastada doğru yönetim planı hangisidir?',
             'options': [{'text': 'İV Seftriakson ve Vankomisin (veya Ampisilin-Sulbaktam) başlayarak hastayı '
                                  'yatırmak, acil Göz ve KBB konsültasyonu ile cerrahi drenaj açısından değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Orbital selülit ve subperiosteal abse varlığında S. pneumoniae, S. aureus '
                                         '(MRSA dahil), H. influenzae ve anaeropları kapsayan geniş spektrumlu '
                                         'parenteral antibiyotik başlanmalı, >10 mm abse veya görme tehdidinde '
                                         'KBB/Oftalmoloji ile endoskopik drenaj planlanmalıdır.',
                          'new_finding': 'Hastaya İV Seftriakson (100 mg/kg/gün) ve İV Vankomisin (60 mg/kg/gün) '
                                         'başlanarak yatışı yapıldı. KBB ve Göz Hastalıkları konsültasyonu ile '
                                         'endoskopik etmoidektomi ve subperiosteal abse drenajı gerçekleştirildi; '
                                         'hasta görme kaybı gelişmeden şifayla taburcu edildi.'},
                         {'text': 'Yüksek doz oral amoksisilin-klavulanat (90 mg/kg/gün) şurup ve nazal dekonjestan '
                                  'sprey reçete ederek günlük poliklinik kontrolü şartıyla hastayı taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Ayaktan oral antibiyotikle eve gönderilen hastada subperiosteal abse '
                                             'genişleyerek optik sinir basısına ve kavernöz sinüs trombozuna ilerledi.',
                          'teaching_point': 'Oral antibiyotik tedavisi yalnızca komplike olmayan hafif preseptal '
                                            'selülitte düşünülebilir; orbital selülit ve subperiosteal abse mutlak '
                                            'hastane yatışı ve İV tedavi endikasyonudur.'},
                         {'text': 'Parenteral antibiyotik tedavisi başlamadan önce 48 saat süreyle yalnızca intravenöz '
                                  'yüksek doz metilprednizolon uygulayarak intraorbital doku ödeminin gerilemesini '
                                  'beklemek',
                          'is_correct': False,
                          'scenario_update': 'Etkin antimikrobiyal koruma olmadan tek başına verilen yüksek doz '
                                             'sistemik steroid bakteriyel enfeksiyonun intrakraniyal boşluğa hızla '
                                             'yayılmasına neden oldu.',
                          'teaching_point': 'Bakteriyel orbital selülitte uygun intravenöz antibiyotik tedavisi '
                                            'başlanmadan tek başına sistemik kortikosteroid uygulanması enfeksiyonun '
                                            'yayılımını hızlandırır.'},
                         {'text': 'Yalnızca topikal moksifloksasin göz damlası ve düşük doz intramusküler sefazolin '
                                  'uygulayarak KBB veya Göz konsültasyonu istemeden acil gözlemde izlemek',
                          'is_correct': False,
                          'scenario_update': 'Kan-beyin ve orbita geçişi yetersiz olan birinci kuşak sefalosporin ve '
                                             'topikal damla altında abse boyutu büyüdü ve görme keskinliği azaldı.',
                          'teaching_point': 'Subperiosteal abseli orbital selülitte santral sinir sistemi geçişi '
                                            'yüksek geniş spektrumlu İV antibiyotikler ve acil Oftalmoloji/KBB '
                                            'değerlendirmesi şarttır.'}]}]}]
