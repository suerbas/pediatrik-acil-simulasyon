# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Yeşil Alan Vakaları (Part 4: Y31 - Y40)
"""

GREEN_CASES_PART4 = [{'id': 'Y31',
  'category': '🫁 Hırıltı & Solunum Sıkıntısı',
  'age': '9 Yaş',
  'gender': 'Erkek',
  'complaint': 'Bir haftadır geçmeyen kuru öksürük, halsizlik, hafif ateş ve baş ağrısı',
  'history': 'Dokuz yaşındaki erkek çocuk, yaklaşık bir haftadır devam eden inatçı, kesik kesik kuru öksürük '
             'şikayetiyle getirildi. Ailesi çocuğun okul performansının belirgin düştüğünü, eşlik eden baş ağrısı, '
             'boğazda gıcıklanma ve hafif ateşinin (en yüksek 37.8°C) olduğunu belirtiyor. Evde verilen parasetamol ve '
             'soğuk algınlığı şuruplarına rağmen öksürük nöbetlerinde gerileme olmamış; nefes darlığı, göğüs ağrısı ya '
             'da dudaklarında morarma tarif edilmiyor.',
  'final_diagnosis': 'Toplum Kökenli Atipik Pnömoni (Mycoplasma pneumoniae Enfeksiyonu)',
  'disposition': 'Yeşil Alandan Ayaktan Oral Makrolid Tedavisi ve Poliklinik Kontrolü ile Taburculuk',
  'case_pearl': 'Okul çağı çocuklarında ve adolesanlarda sinsi başlangıçlı inatçı kuru öksürük, baş ağrısı ve '
                'subfebril ateşe eşlik eden bilateral dağınık raller varlığında atipik pnömoni akla gelmelidir. Fizik '
                'muayene ve radyolojik bulgular hastanın genel klinik tablosuna göre beklenenden çok daha belirgindir '
                '(klinik-radyolojik diskordans). Hücre duvarı bulunmayan bu etkene karşı beta-laktamlar etkisiz olup '
                'birinci basamak ampirik tedavide oral makrolidler (klaritromisin veya azitromisin) ilk seçenektir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Bu hastada ilk değerlendirmede odaklanmanız gereken en uygun klinik muayene yaklaşımı '
                         'hangisidir?',
             'options': [{'text': 'Genel durumu ve vital bulguları hızlıca kontrol edip hastayı beklemeden acil '
                                  'bronkodilatatör nebülizasyonu amacıyla Sarı Alana devretmek',
                          'is_correct': False,
                          'scenario_update': 'Nebülize salbutamol inhalasyonu sonrasında hastanın kalp tepe atımı '
                                             "124/dk'ya yükseldi ancak inatçı kuru öksürüğünde ve dinleme bulgularında "
                                             'hiçbir rahatlama sağlanamadı.',
                          'teaching_point': 'Solunum sıkıntısı, çekilme ve belirgin bronkospazmı olmayan stabil '
                                            'hastalarda ayırıcı muayene tamamlanmadan Sarı Alana devir ve ampirik '
                                            'bronkodilatatör uygulaması gereksizdir.'},
                         {'text': 'Vital bulguları, solunum sayısını, oksijen satürasyonunu ölçmek ve bilateral tüm '
                                  'akciğer alanlarını derin inspiryumda dikkatle dinlemek',
                          'is_correct': True,
                          'explanation': 'Okul çağı çocuğunda uzamış öksürük varlığında solunum iş yükü '
                                         'değerlendirilmeli ve fokal veya yaygın akciğer sesleri eksiksiz oskülte '
                                         'edilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.7°C, KTA 86/dk, Solunum Sayısı 20/dk, SpO2 %98 (oda '
                                         'havasında), Kan Basıncı 105/65 mmHg. Çocuk rahat, dispne veya retraksiyon '
                                         'yok. Orofarenks hafif hiperemik. Akciğer oskültasyonunda bilateral alt '
                                         'zonlarda dağınık ince raller ve hafif bilateral ekspiratuar hışıltı duyuldu; '
                                         'tübüler ses veya fokal sessiz alan saptanmadı.'},
                         {'text': 'Üst solunum yolu semptomları ön planda olduğundan orofarenks ve otoskopik '
                                  'muayeneyle yetinip akciğer oskültasyonunu derinleştirmeden semptomatik tedaviye '
                                  'geçmek',
                          'is_correct': False,
                          'scenario_update': 'Yalnızca orofarenks incelenerek postnazal akıntı tanısıyla gönderilmek '
                                             'istenen hastada derin oskültasyon yapılmadığı için akciğer '
                                             'parankimindeki yaygın raller atlanmış oldu.',
                          'teaching_point': 'Bir haftadır süren inatçı öksürük ve baş ağrısı olan okul çağı çocuğunda '
                                            'alt solunum yolu tutulumunu dışlamak için ayrıntılı akciğer oskültasyonu '
                                            'zorunludur.'},
                         {'text': 'Ateş ve uzamış öksürüğü olan hastada kardiyopulmoner muayeneyi öteleyip hızlıca '
                                  'damar yolu açarak kan tetkikleri hazırlığına girişmek',
                          'is_correct': False,
                          'scenario_update': 'Genel durumu iyi ve satürasyonu normal olan hastada invaziv damar yolu '
                                             'girişimi çocukta aşırı ajitasyon ve strese yol açtı.',
                          'teaching_point': 'Hemodinamisi stabil, oda havasında oksijenasyonu normal çocuklarda '
                                            'invaziv girişimlerden önce ayrıntılı fizik muayene ve klinik '
                                            'değerlendirme tamamlanmalıdır.'}]},
            {'stage_title': 'Tetkik ve Radyolojik Görüntüleme Kararı',
             'question': 'Akciğer oskültasyonunda bilateral yaygın ince raller ve hafif hışıltı duyulan hastada en '
                         'uygun tetkik ve görüntüleme yaklaşımı hangisidir?',
             'options': [{'text': 'İnfiltrasyon varlığını ve komplikasyonları acil servis şartlarında en duyarlı '
                                  'şekilde netleştirmek için kontrastlı toraks tomografisi çekilmesini planlamak',
                          'is_correct': False,
                          'scenario_update': 'Toraks tomografisi çekilmesi hastanın yüksek dozda iyonizan radyasyona '
                                             'maruz kalmasına yol açtı ve klinik yönetimde beklenen ek faydayı '
                                             'sağlamadı.',
                          'teaching_point': 'Çocukluk çağı toplum kökenli alt solunum yolu enfeksiyonlarında '
                                            'bilgisayarlı tomografi rutin tanı aracı değildir; gereksiz radyasyon '
                                            'riski taşır.'},
                         {'text': 'Akut enfeksiyon odağını dışlamak amacıyla rutin tam kan sayımı, sedimentasyon, CRP '
                                  've prokalsitonin düzeylerini içeren geniş biyokimya paneli istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR: WBC 8.400/mm³ (nötrofil %58, lenfosit %34), Hb 13.1 g/dL, '
                                             'PLT 285.000/mm³, CRP 16 mg/L, Prokalsitonin 0.08 ng/mL. Sonuçlar '
                                             'patognomonik ayrım sağlamadı.',
                          'teaching_point': 'Klinik tablosu hafif, genel durumu iyi olan okul çağı çocuklarında kan '
                                            'parametreleri bakteriyel ve viral ayrımında özgül değildir.'},
                         {'text': 'Akciğer parankim tutulumunu ve infiltrasyon paternini değerlendirmek amacıyla '
                                  'arka-ön (PA) akciğer grafisi çekilmesini talep etmek',
                          'is_correct': True,
                          'explanation': 'Oskültasyonda dinleme bulgusu olan ve uzamış öksürüğü bulunan çocukta PA '
                                         'akciğer grafisi parankimal tutulumun yaygınlığını ve paternini göstermede '
                                         'temel incelemedir.',
                          'new_finding': 'PA Akciğer Grafisi: Bilateral perihiler belirginleşme, alt zonlarda yaygın '
                                         'retikülonodüler ve peribronşial interstisyel infiltratlar saptandı; lober '
                                         'konsolidasyon veya plevral sıvı izlenmedi.',
                          'image': 'assets/images/cxr_atypical_pneumonia.png',
                          'image_caption': 'PA Akciğer Grafisi: Bilateral perihiler ve retikülonodüler infiltratlar'},
                         {'text': 'Klinik bulguların viral bronşiolit düşündürdüğünü varsayarak hiçbir görüntüleme '
                                  'veya tetkik yapmadan hastayı doğrudan semptomatik tedavilerle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Görüntüleme yapılmadığı için bilateral belirgin interstisyel '
                                             'infiltrasyon tespit edilemedi ve uygun antimikrobiyal başlanması '
                                             'gecikti.',
                          'teaching_point': 'Dokuz yaşındaki bir çocukta bir haftadır süren öksürük ve bilateral '
                                            'raller varlığında görüntüleme yapılmadan alt solunum yolu parankim '
                                            'tutulumu dışlanamaz.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik seyri, fizik muayene bulguları ve akciğer grafisi değerlendirildiğinde bu hastada en '
                         'olası tanı hangisidir?',
             'options': [{'text': 'Toplum Kökenli Atipik Pnömoni',
                          'is_correct': True,
                          'explanation': 'Okul çağında sinsi seyirli kuru öksürük, subfebril ateş, baş ağrısı ve '
                                         'bilateral retikülonodüler infiltrasyon Mycoplasma pneumoniae kaynaklı atipik '
                                         'pnömoni ile tipiktir.',
                          'new_finding': 'Klinik ve radyolojik bulgularla Atipik Pnömoni tanısı doğrulandı.'},
                         {'text': 'Pnömokok Kaynaklı Lober Pnömoni',
                          'is_correct': False,
                          'scenario_update': 'Lober pnömonide beklenen ani yüksek ateş, toksik görünüm, takipne ve '
                                             'grafide segmental veya lober yoğun konsolidasyon bulguları hastada '
                                             'saptanmadı.',
                          'teaching_point': 'Tipik bakteriyel pnömonilerde ani başlangıç, yüksek ateş, taşipne, inleme '
                                            've grafide fokal konsolidasyon ile bronkogram bulguları ön plandadır.'},
                         {'text': 'Akut Viral Trakeobronşit',
                          'is_correct': False,
                          'scenario_update': 'Grafide saptanan belirgin bilateral retikülonodüler ve peribronşial '
                                             'parankim infiltrasyonu basit trakeobronşit tablosunun çok ötesinde '
                                             'parankimal tutuluma işaret etti.',
                          'teaching_point': 'Akut bronşitte akciğer grafisi genellikle doğaldır; parankimal '
                                            'interstisyel ve alveoler infiltratların varlığı pnömoni lehinedir.'},
                         {'text': 'Yabancı Cisim Aspirasyonu',
                          'is_correct': False,
                          'scenario_update': 'Hastada ani gelişen boğulma öyküsü, tek taraflı lokalize havalanma '
                                             'azlığı, atelektazi veya hava hapsi bulgusu izlenmedi.',
                          'teaching_point': 'Yabancı cisim aspirasyonu ani başlangıçlı öksürük ve tek taraflı '
                                            'oskültasyon/grafi bulgularıyla seyreder; bir haftalık sinsi enfeksiyöz '
                                            'prodrom beklenmez.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Atipik pnömoni tanısı konulan genel durumu iyi bu çocuk için en uygun tedavi ve taburculuk '
                         'protokolü hangisidir?',
             'options': [{'text': 'Ampirik olarak oral yüksek doz amoksisilin-klavulanat süspansiyon reçete edip yedi '
                                  'gün sonra çocuk hastalıkları polikliniği kontrolüne çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Hücre duvarı sentez inhibitörü olan aminopenisilin başlanan hastanın 72 '
                                             'saat sonraki kontrolünde kuru öksürük ve halsizlik yakınmalarında hiçbir '
                                             'gerileme olmadı.',
                          'teaching_point': 'Mycoplasma pneumoniae hücre duvarına sahip olmadığından penisilinler, '
                                            'sefalosporinler ve diğer beta-laktam antibiyotiklere yapısal olarak '
                                            'tamamen dirençlidir.'},
                         {'text': 'Çocuğu acil serviste müşahedeye alıp intravenöz seftriakson infüzyonu ve eş zamanlı '
                                  'nebülize kortikosteroid tedavisi uygulayarak pediatri servisine yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Solunum sıkıntısı ve hipoksemisi olmayan stabil hasta gereksiz yere '
                                             'hastaneye yatırıldı ve etkisiz bir antibiyotik grubuna maruz bırakıldı.',
                          'teaching_point': 'Hafif seyirli, oral alımı tam ve satürasyonu normal atipik pnömoni '
                                            'olguları ayaktan oral makrolid tedavisiyle güvenle yönetilebilir; yatış '
                                            'endikasyonu yoktur.'},
                         {'text': 'Antibiyotik başlamaksızın yalnızca oral dekstrometorfan içeren antitussif şurup ve '
                                  'antipiretik parasetamol vererek hastayı semptomatik taburculuk planıyla evine '
                                  'göndermek',
                          'is_correct': False,
                          'scenario_update': 'Öksürük kesici şurup sekresyonların atılmasını engelleyerek öksürük '
                                             'krizlerini artırdı ve hastanın klinik semptomları iki gün içinde '
                                             'kötüleşti.',
                          'teaching_point': 'Çocukluk çağı pnömonilerinde antitussif şurupların yeri yoktur; '
                                            'etiyolojiye yönelik makrolid başlanması klinik iyileşmeyi hızlandırır ve '
                                            'bulaşıcılığı azaltır.'},
                         {'text': 'Ayaktan oral makrolid (klaritromisin veya azitromisin) tedavisi planlayıp, '
                                  'hidrasyon ve kırmızı bayrak eğitimiyle kontrole çağırmak',
                          'is_correct': True,
                          'explanation': 'Okul çağı atipik pnömonisinde mikoplazmaya etkili ilk seçenek oral '
                                         'makrolidlerdir; genel durumu iyi hasta ayaktan güvenle izlenebilir.',
                          'new_finding': 'Hastaya oral klaritromisin tedavisi planlandı, dinlenme ve hidrasyon '
                                         'önerildi; 48-72 saat içinde kontrol veya nefes darlığında acile başvuru '
                                         'anlatıldı.'}]}]},
 {'id': 'Y32',
  'category': '👁️ Göz Şikayetleri',
  'age': '7 Yaş',
  'gender': 'Kız',
  'complaint': 'Her iki gözde yoğun kaşıntı, ovuşturma, sulanma ve göz kapaklarında şişlik',
  'history': 'Yedi yaşındaki kız çocuk, ilkbahar aylarının başlamasıyla birlikte her iki gözünde yaklaşık 5 gündür '
             'giderek artan şiddetli kaşıntı, sürekli gözlerini ovuşturma, sulanma ve kızarıklık yakınmasıyla '
             'getirildi. Ailesi sabahları çapaklanma olmadığını, göz kapaklarının hafif şiş göründüğünü ve akıntının '
             'berrak su gibi olduğunu ifade ediyor. Çocuğun daha önce bilinen astım veya besin duyarlılığı öyküsü '
             'bulunmuyor; ancak son günlerde açık havada ve parkta vakit geçirdikten sonra göz şikayetlerinin '
             'belirginleştiği belirtiliyor. Görmede bulanıklık, gözde zonklayıcı ağrı veya ateş bildirilmiyor.',
  'final_diagnosis': 'Akut Alerjik Konjonktivit',
  'disposition': 'Yeşil Alandan Ayaktan Topikal Antihistaminik/Mast Hücre Stabilizatörü ve Korunma Önlemleriyle '
                 'Taburculuk',
  'case_pearl': 'Alerjik konjonktivitin kardinal semptomu yoğun kaşıntı ve gözleri ovuşturmadır. Genellikle bilateral '
                'tutulum, seröz sulanma, kemozis ve tarsal konjonktivada papiller reaksiyon görülür; pürülan '
                'çapaklanma ve görme kaybı beklenmez. Tedavide birinci basamak yaklaşım alerjenden korunma, soğuk '
                'kompres, koruyucusuz suni gözyaşı ve topikal çift etkili H1-antihistaminik / mast hücre stabilizatörü '
                '(örn. olopatadin damla) kombinasyonudur. Göz hekimi kontrolü olmadan topikal kortikosteroidler asla '
                'başlanmamalıdır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Oftalmolojik Muayene',
             'question': 'Bu hastada göz semptomlarını değerlendirirken ilk aşamada uygulamanız gereken en uygun '
                         'muayene yaklaşımı hangisidir?',
             'options': [{'text': 'Görme keskinliğini test etmeden doğrudan topikal lokal anestezik damlatıp kornea '
                                  'duyarlılığını pamuk uçlu aplikatörle değerlendirmeye odaklanmak',
                          'is_correct': False,
                          'scenario_update': 'Topikal anestezik uygulanması geçici rahatlama sağlasa da görme '
                                             'keskinliği baştan belgelenmedi ve gereksiz kornea manipülasyonu '
                                             'huzursuzluğa yol açtı.',
                          'teaching_point': 'Tüm göz başvurularında invaziv veya ağrılı işlemlerden önce görme '
                                            'keskinliği mutlaka değerlendirilmeli; rutin anestezik damla '
                                            'kullanılmamalıdır.'},
                         {'text': 'Şikayetlerin yalnızca tek bir gözde yoğunlaştığını varsayıp diğer gözü muayene '
                                  'etmeden doğrudan fundus oftalmoskopik incelemesine geçmek',
                          'is_correct': False,
                          'scenario_update': 'Oftalmoskop ışığı çocuğun fotofobisini artırırken, her iki göz kapağı ve '
                                             'konjonktiva karşılaştırmalı olarak yeterince incelenemedi.',
                          'teaching_point': 'Kaşıntı ve sulanma yakınmalarında bilateral karşılaştırmalı ön segment '
                                            'muayenesi esastır; arka segment incelemesi ilk basamak muayene önceliği '
                                            'değildir.'},
                         {'text': 'Görme keskinliğini değerlendirmek, göz kapaklarını, konjonktival hiperemiyi, akıntı '
                                  'niteliğini ve üst kapak tarsal konjonktivasını dikkatle incelemek',
                          'is_correct': True,
                          'explanation': 'Bilateral kaşıntı ve sulanmada görme keskinliği belgelenmeli, tarsal '
                                         'papiller yapılar, hiperemi paterni ve çapak niteliği ayırt edilmelidir.',
                          'new_finding': 'Görme keskinliği bilateral tam (Snellen 10/10). Göz kapaklarında hafif ödem, '
                                         'bilateral bulber konjonktivada yaygın soluk pembe hiperemi ve hafif kemozis '
                                         'saptandı. Pürülan çapak yok, sulu berrak sekresyon mevcut. Üst göz kapağı '
                                         'eversiyonunda üst tarsal konjonktivada ince diffüz papiller hipertrofi '
                                         'izlendi. Kornea berrak, pupil ışık refleksleri bilateral doğal.'},
                         {'text': 'Göz muayenesini inspeksiyonla sınırlı tutup hastayı hızla sedate ederek acil '
                                  'şartlarda genişletilmiş biyomikroskopik yarık lamba incelemesine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Kooperasyonu tam olan yedi yaşındaki çocukta gereksiz sedasyon '
                                             'planlanması aileyi endişelendirdi ve acil servis işleyişini aksattı.',
                          'teaching_point': 'Kooperatif çocuklarda sedasyona gerek olmaksızın basit büyüteç, el '
                                            'lambası ve gerekirse biyomikroskopla ayrıntılı ön segment muayenesi '
                                            'rahatlıkla yapılabilir.'}]},
            {'stage_title': 'Tetkik ve İleri İnceleme Kararı',
             'question': 'Bilateral papiller konjonktival hiperemi, berrak sulanma ve yoğun kaşıntısı olan bu çocukta '
                         'en uygun tetkik yaklaşımı hangisidir?',
             'options': [{'text': 'Klinik bulgular tanı için yeterli olduğundan gereksiz laboratuvar tetkiki veya '
                                  'konjonktival sürüntü kültürü almadan tanıya ilerlemek',
                          'is_correct': True,
                          'explanation': 'Mevsimsel özellik gösteren, pürülan olmayan kaşıntılı bilateral tablolarda '
                                         'öykü ve tipik muayene tanı koydurucudur, laboratuvar gerekmez.',
                          'new_finding': 'Tetkik istenmedi; hastanın klinik ve muayene bulgularının tipik mevsimsel ön '
                                         'segment inflamasyonuyla örtüştüğü belirlendi.'},
                         {'text': 'Bakteriyel veya klamidyal patojenleri ekarte etmek amacıyla bilateral konjonktival '
                                  'kazıntı örneği alarak Giemsa ve Gram boyama yaptırmak',
                          'is_correct': False,
                          'scenario_update': 'Konjonktivadan invaziv sürüntü ve kazıntı alınması çocukta yoğun ağrıya, '
                                             'submukozal peteşiyel kanamaya ve belirgin huzursuzluğa yol açtı.',
                          'teaching_point': 'Pürülan akıntısı veya neonatal dönem öyküsü olmayan çocuklarda ağrılı '
                                            'konjonktival kazıntı veya yayma endike değildir.'},
                         {'text': 'Etiyolojiyi saptamak amacıyla acil serviste geniş inhalan spesifik IgE paneli, '
                                  'total IgE ve periferik yaymada eozinofil sayımı istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR: Total IgE 140 IU/mL, Eozinofil %4, tam kan sayımı normal. '
                                             'Spesifik IgE paneli sonuçlarının ise günler sonra çıkacağı öğrenildi.',
                          'teaching_point': 'Akut acil başvurularda spesifik IgE veya alerji panelleri yönetimi '
                                            'değiştirmez; bu testler gerekirse elektif poliklinik şartlarında '
                                            'planlanmalıdır.'},
                         {'text': 'Sistemik vaskülit ve otoimmün üveit birlikteliğini dışlamak amacıyla ANA, RF, '
                                  'eritrosit sedimentasyon hızı ve HLA-B27 tarama testleri göndermek',
                          'is_correct': False,
                          'scenario_update': 'Gönderilen otoantikor ve romatolojik paneller tamamen negatif '
                                             'sonuçlandı; gereksiz kan alımı ve yüksek maliyet dışında katkı '
                                             'sağlamadı.',
                          'teaching_point': 'Görme bozukluğu, siliyer enjeksiyon, pupil düzensizliği veya ön kamara '
                                            'hücresi olmayan saf yüzeyel tablolarda sistemik otoimmün tarama endike '
                                            'değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Anamnez, mevsimsel özellikler ve fizik muayene bulguları ışığında bu hastada en olası klinik '
                         'tanınız nedir?',
             'options': [{'text': 'Akut Bakteriyel Konjonktivit',
                          'is_correct': False,
                          'scenario_update': 'Bakteriyel enfeksiyonlarda beklenen sabahları göz kapaklarını yapıştıran '
                                             'kalın pürülan akıntı ve mat hiperemi tablosu hastada bulunmadı.',
                          'teaching_point': 'Bakteriyel formlarda pürülan sekresyon ve kirpiklerde kabuklanma '
                                            'belirgindir; yoğun kaşıntı ve seröz sulanma ise tipik değildir.'},
                         {'text': 'Epidemik Keratokonjonktivit',
                          'is_correct': False,
                          'scenario_update': 'Adenoviral keratokonjonktivitte sık rastlanan preauriküler hassas '
                                             'lenfadenopati, korneal subepitelyal infiltratlar ve yoğun ağrı hastada '
                                             'saptanmadı.',
                          'teaching_point': 'Viral epidemik tablolarda preauriküler lenf nodu büyümesi, folliküler '
                                            'hipertrofi ve bulaşıcılık belirginken, kaşıntı ana semptom değildir.'},
                         {'text': 'Ön Blefarit ve Meibomian Disfonksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Kapak kenarlarında kepeklenme, kirpik diplerinde silendirik manşonlar '
                                             'veya meibomian bezi tıkanıklığı muayenede izlenmedi.',
                          'teaching_point': 'Blefaritte inflamasyon göz kapağı kenarında ve kirpik diplerinde '
                                            'lokalizedir; konjonktival papiller hipertrofi ve kemozis ön planda '
                                            'olmaz.'},
                         {'text': 'Akut Alerjik Konjonktivit',
                          'is_correct': True,
                          'explanation': 'Mevsimsel artış, her iki gözde yoğun kaşıntı, berrak sulanma, kemozis ve üst '
                                         'tarsal papiller hipertrofi alerjik konjonktivit için klasiktir.',
                          'new_finding': 'Klinik tanı Akut Alerjik Konjonktivit olarak kesinleşti.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Akut alerjik konjonktivit tanısı kesinleşen bu hastanın tedavisinde en uygun yaklaşım ve '
                         'aile bilgilendirmesi hangisidir?',
             'options': [{'text': 'Enflamasyonu hızla baskılamak amacıyla topikal deksametazon damlayı günde dört kez '
                                  'iki hafta süreyle kullanması talimatıyla reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Göz hekimi kontrolü olmaksızın başlanan topikal steroid damla nedeniyle '
                                             'hastada ilerleyen haftalarda intraoküler basınç artışı riski doğdu.',
                          'teaching_point': 'Topikal kortikosteroidler katarakt ve glokom gibi ciddi komplikasyon '
                                            'riskleri nedeniyle oftalmolog takibi olmadan acil servisten asla '
                                            'başlanmamalıdır.'},
                         {'text': 'Topikal olopatadin damla, koruyucusuz suni gözyaşı, soğuk kompres uygulaması ve '
                                  'gözleri ovuşturmaktan kaçınma eğitimiyle ayaktan taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Çift etkili H1-antihistaminik/mast hücre stabilizatörü (olopatadin), suni '
                                         'gözyaşı ve soğuk uygulama kaşıntıyı hızla dindirir ve güvenlidir.',
                          'new_finding': 'Reçetesi düzenlenen hastanın ailesine polen mevsiminde pencereleri kapalı '
                                         'tutma, güneş gözlüğü takma ve ovuşturmama uyarısı yapıldı.'},
                         {'text': 'Sekonder enfeksiyon gelişimini önlemek amacıyla profilaktik topikal tobramisin '
                                  'damla ile birlikte sistemik birinci kuşak oral antihistaminik şurup başlamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz antibiyotik kullanımı oküler florayı bozdu; sedatif oral '
                                             'antihistaminik ise okul çağındaki çocukta belirgin uyuklama ve dikkat '
                                             'dağınıklığı yaptı.',
                          'teaching_point': 'Alerjik olgularda profilaktik topikal antibiyotiğin yeri yoktur; sistemik '
                                            'birinci kuşak antihistaminikler ise sedasyon yapar ve göz kuruluğunu '
                                            'artırabilir.'},
                         {'text': 'Semptomları hızla geriletmek amacıyla gözleri steril gazlı bezle 48 saat kapatıp '
                                  '(oklüzyon pansumanı) kesin istirahat önermek',
                          'is_correct': False,
                          'scenario_update': 'Göz kapama işlemi lokal sıcaklığı ve alerjen temas süresini artırarak '
                                             'kaşıntıyı şiddetlendirdi ve çocukta aşırı tedirginliğe yol açtı.',
                          'teaching_point': 'Alerjik veya enfeksiyöz oküler inflamasyonlarda gözün kapatılması lokal '
                                            'ısıyı ve nemi artırarak tabloyu kötüleştirir; oklüzyon '
                                            'kontrendikedir.'}]}]},
 {'id': 'Y33',
  'category': '👁️ Göz Şikayetleri',
  'age': '2.5 Aylık',
  'gender': 'Erkek',
  'complaint': 'Doğumdan beri sağ gözde sürekli sulanma ve kirpikte hafif mukoid yapışma',
  'history': 'İki buçuk aylık erkek bebek, annesi tarafından sağ gözünde neredeyse doğumdan itibaren devam eden '
             'sürekli sulanma, yaşarma ve özellikle sabahları uyanırken kirpik diplerinde hafif yapışkan sarımsı-beyaz '
             'akıntı şikayetiyle getirildi. Annesi sol gözünde hiçbir sorun olmadığını, sağ gözünü ise günde birkaç '
             'kez temizlemek zorunda kaldığını belirtiyor. Bebeğin gözünde kızarıklık, kapaklarda belirgin şişlik veya '
             'morarma tarif edilmiyor. Emmesi, kilo alımı ve genel gelişimi mükemmel olan bebeğin ateşi hiç olmamış; '
             'dış merkezde daha önce verilen antibiyotikli damlalar kullanıldığı sürece akıntıyı azaltmış ancak '
             'kesildikten sonra sulanma aynen devam etmiş.',
  'final_diagnosis': 'Konjenital Nazolakrimal Kanal Tıkanıklığı (Dakriyostenoz)',
  'disposition': 'Yeşil Alandan Ayaktan Lakrimal Kese Masajı (Crigler Masajı) ve Aile Eğitimi ile Taburculuk',
  'case_pearl': 'Süt çocukluğunda doğumdan itibaren görülen, tek veya çift taraflı persistan sulanma ve mukoid '
                'akıntının en sık nedeni Hasner valvinin açılmamasıyla karakterize konjenital nazolakrimal kanal '
                'tıkanıklığıdır (dakriyostenoz). Sklera beyaz, kornea saydamdır ve konjonktival hiperemi eşlik etmez '
                "(akut konjonktivitten temel farkı). Olguların %90'ından fazlası 1 yaşına kadar konservatif izlem ve "
                'doğru uygulanan Crigler masajı ile kendiliğinden düzelir. Akut dakriyosistit (medial kantusta '
                'hiperemi, fluktuasyon, ateş) gelişmedikçe rutin profilaktik antibiyotik veya erken invaziv sondalama '
                'önerilmez.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Bu bebekte semptomların kaynağını netleştirmek ve acil patolojileri dışlamak için en uygun '
                         'fizik muayene yaklaşımı hangisidir?',
             'options': [{'text': 'Bilateral kornea saydamlığını, sklera ve konjonktivayı incelemek, medial kantal '
                                  'bölgeye nazik bası uygulayarak reflüyü değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Tek taraflı sulanmada kornea saydamlığı kontrol edilmeli (glokom '
                                         'dışlanmalı), konjonktivanın sakinliği görülmeli ve kese basısıyla mukoid '
                                         'reflü aranmalıdır.',
                          'new_finding': 'Sağ gözde artmış lakrimal göllenme mevcut. Sklera beyaz, bulber konjonktiva '
                                         'tamamen sakin, kızarıklık veya hiperemi yok. Kornea tamamen saydam ve çapı '
                                         'normal (buftalmus bulgusu yok), ışık refleksi doğal. Sağ medial kantal '
                                         'lakrimal kese üzerine işaret parmağıyla basıldığında punktumdan '
                                         'berrak-mukoid sekresyon reflüsü izlendi; lakrimal kese üzerinde eritem, '
                                         'endurasyon veya fluktuasyon yok. Sol göz muayenesi tamamen doğal.'},
                         {'text': 'Bebekte konjenital glokomu kesinleştirmek amacıyla acil serviste lokal anestezik '
                                  'eşliğinde doğrudan tonometri ile göz içi basıncı ölçmek',
                          'is_correct': False,
                          'scenario_update': 'Bebek ajite oldu ve ağladı; ağlama sırasında ölçülen göz içi basıncı '
                                             'yalancı yüksek çıktı ve gereksiz yere endişe yarattı.',
                          'teaching_point': 'Kornea çapı normal, korneası tamamen saydam olan ve fotofobisi bulunmayan '
                                            'bir süt çocuğunda acil invaziv tonometri endike değildir.'},
                         {'text': 'Yalnızca dış inspeksiyonla yetinip göz küresine ve lakrimal bölgeye hiç dokunmadan '
                                  'bebeği hızla göz hastalıkları servisine yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Medial kantal bası testi yapılmadığı için sekresyonun lakrimal keseden '
                                             'kaynaklandığı anlaşılamadı ve gereksiz yatış talebi konsültan hekimce '
                                             'reddedildi.',
                          'teaching_point': 'İnflamatuar odak veya kitle bulgusu olmayan izole sulanmalarda lakrimal '
                                            'kese palpasyonu yapılmalı, yatış yerine ayaktan yönetim planlanmalıdır.'},
                         {'text': 'Göz kapağını forsepsle zorlayarak evert etmek ve konjonktiva fornikslerinde gizli '
                                  'yabancı cisim veya forseps travması aramak',
                          'is_correct': False,
                          'scenario_update': 'Forsepsle zorlu eversiyon bebeğin konjonktivasında travmatik '
                                             'mikrohematoma ve yoğun ağlamaya yol açarak muayeneyi imkansız hale '
                                             'getirdi.',
                          'teaching_point': 'Doğumdan beri süregelen, kapak lezyonu veya akut batma bulgusu olmayan '
                                            'bebeklerde travmatik forseps uygulamaları kontrendikedir.'}]},
            {'stage_title': 'Tetkik ve Yaklaşım Stratejisi',
             'question': 'Kornea ve sklerası doğal, yalnızca kese basısıyla punktumdan mukoid reflü veren bu bebekte '
                         'en uygun tanısal yaklaşım hangisidir?',
             'options': [{'text': 'Akut dakriyosistit ve apse formasyonunu ekarte etmek amacıyla acil intravenöz '
                                  'kontrastlı paranazal ve orbita bilgisayarlı tomografisi çektirmek',
                          'is_correct': False,
                          'scenario_update': 'Medial kantusta selülit, ısı artışı veya fluktuasyon olmayan bebeğe '
                                             'yüksek doz radyasyon verilmiş oldu ve tomografi normal raporlandı.',
                          'teaching_point': 'Medial kantusta eritem, hassasiyet ve kitle gibi akut inflamasyon bulgusu '
                                            'yoksa görüntüleme (BT/MRG) gereksizdir.'},
                         {'text': 'Bakteriyel kolonizasyonu tam tanımlamak için punktumdan gelen mukoid sekresyondan '
                                  'acil aerop-anaerop kültür ve antibiyogram örneği göndermek',
                          'is_correct': False,
                          'scenario_update': 'Kültürde normal flora elemanı olan koagülaz negatif stafilokok üredi; bu '
                                             'durum gereksiz geniş spektrumlu antibiyotik başlanması ikilemi yarattı.',
                          'teaching_point': 'Konjonktival hiperemi ve sistemik bulgu olmayan izole mukoid '
                                            'göllenmelerde rutin sekresyon kültürü yönetimi değiştirmez.'},
                         {'text': 'Drenaj yollarının anatomik açıklığını doğrulamak için genel anestezi altında acil '
                                  'dakriyosistografi ve floroskopik kontrast inceleme planlamak',
                          'is_correct': False,
                          'scenario_update': 'İki buçuk aylık asemptomatik bebekte gereksiz genel anestezi riski ve '
                                             'floroskopi maruziyeti gündeme gelerek işlem ertelendi.',
                          'teaching_point': 'Süt çocuklarında lakrimal sistem radyolojik kontrast incelemeleri '
                                            'invazivdir; komplikasyonsuz olgularda birinci basamakta yeri yoktur.'},
                         {'text': 'Ek bir laboratuvar veya görüntüleme tetkiki istemeden, fizik muayene bulgularıyla '
                                  'klinik tanıya varıp aile eğitimine odaklanmak',
                          'is_correct': True,
                          'explanation': 'Öykü ve tipik kese bası bulgusuyla klinik tanı kesinleştirilir; infant '
                                         'döneminde komplikasyonsuz olgularda hiçbir tetkik gerekmez.',
                          'new_finding': 'Tetkik istenmedi; lakrimal kese bölgesinde inflamasyon veya selülit bulgusu '
                                         'olmadığı, tablonun selim seyirli konjenital süreçle uyumlu olduğu teyit '
                                         'edildi.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Doğumdan beri tek taraflı sulanma, beyaz sklera ve punktum reflüsü olan bu bebekte en olası '
                         'tanı hangisidir?',
             'options': [{'text': 'Akut Bakteriyel Konjonktivit',
                          'is_correct': False,
                          'scenario_update': 'Konjonktivitte beklenen belirgin konjonktival hiperemi, kemozis ve '
                                             'yaygın pürülan eksüda bu bebekte mevcut değildi.',
                          'teaching_point': 'Bakteriyel konjonktivitte bulber konjonktiva kırmızıdır; skleranın beyaz '
                                            've sakin olması akıntının lakrimal göllenmeye bağlı olduğunu gösterir.'},
                         {'text': 'Konjenital Nazolakrimal Kanal Tıkanıklığı',
                          'is_correct': True,
                          'explanation': 'Doğumdan itibaren tek taraflı epifora, mukoid göllenme, beyaz sklera ve kese '
                                         'basısıyla punktumdan reflü dakriyostenoz için patognomoniktir.',
                          'new_finding': 'Klinik tanı Konjenital Nazolakrimal Kanal Tıkanıklığı (Dakriyostenoz) olarak '
                                         'kesinleşti.'},
                         {'text': 'Konjenital İnfantil Glokom',
                          'is_correct': False,
                          'scenario_update': 'Glokomda görülen korneal bulanıklık (ödem), kornea çapında genişleme '
                                             '(buftalmus) ve belirgin fotofobi hastada saptanmadı.',
                          'teaching_point': 'Konjenital glokomda kornea mat ve büyüktür, bebek ışıktan aşırı rahatsız '
                                            'olur; korneanın berrak ve normal çapta olması bu tanıyı dışlar.'},
                         {'text': 'Akut Enfeksiyöz Dakriyosistit',
                          'is_correct': False,
                          'scenario_update': 'Dakriyosistitte medial kantusta kızarıklık, gergin şişlik, fluktuasyon, '
                                             'yoğun ağrı ve sistemik ateş bulunur; bu bebekte kese sakindir.',
                          'teaching_point': 'Dakriyosistit kanal tıkanıklığının akut pürülan ve flegmonöz bir '
                                            'komplikasyonudur; lokal eritem ve kitle olmadan tanı konulamaz.'}]},
            {'stage_title': 'Tedavi ve Aile Eğitimi',
             'question': 'Konjenital nazolakrimal kanal tıkanıklığı tanısı alan 2.5 aylık bebeğin yönetiminde en uygun '
                         'yaklaşım hangisidir?',
             'options': [{'text': 'Kanalı mekanik olarak hemen açmak amacıyla bebeğe acil sedasyon altında genel '
                                  'anesteziyle lakrimal kanal sondalaması (probing) uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Erken dönemde gereksiz invaziv girişim planlanması ailede büyük '
                                             'tedirginlik yarattı ve anestezi komplikasyonu riski oluşturdu.',
                          'teaching_point': "Konjenital dakriyostenozda spontan düzelme oranı bir yaşına kadar %90'ın "
                                            'üzerindedir; erken sondalama ilk basamakta önerilmez.'},
                         {'text': 'Gözdeki mukoid sekresyonu tamamen baskılamak için günde dört kez topikal tobramisin '
                                  've deksametazon kombine damlasını bir ay kullandırmak',
                          'is_correct': False,
                          'scenario_update': 'Uzun süreli topikal steroid kullanımı bebekte göz içi basınç artışı '
                                             'riski yaratırken, antibiyotik kesildiğinde göllenme aynen devam etti.',
                          'teaching_point': 'Akut enfeksiyon olmaksızın rutin topikal antibiyotik veya steroid '
                                            'kullanımı etkisizdir ve dirençli mikroorganizma ile glokom riski taşır.'},
                         {'text': 'Ilık suyla temizlik, nazolakrimal kese üzerine Crigler masajı tekniği eğitimi ve '
                                  'bir yaşına kadar konservatif izlem önermek',
                          'is_correct': True,
                          'explanation': 'Hasner membranını açmak için günde 2-3 kez uygulanan Crigler masajı (aşağı '
                                         'hidrostatik bası) ve hijyen birinci basamak standart tedavidir.',
                          'new_finding': 'Anneye lakrimal keseden aşağıya burun kanadına doğru hidrostatik masaj '
                                         'tekniği gösterildi; akut dakriyosistit uyarı işaretleri anlatılarak taburcu '
                                         'edildi.'},
                         {'text': 'Lakrimal yollara silikon tüp entübasyonu yapılması amacıyla hastayı acilen üçüncü '
                                  'basamak oküloplastik cerrahi kliniğine sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'Henüz konservatif yöntemler denenmeden üçüncü basamağa sevk edilmesi '
                                             'ailenin gereksiz sağlık kurumu dolaşmasına yol açtı.',
                          'teaching_point': 'Silikon tüp entübasyonu veya cerrahi müdahaleler tekrarlayan başarısız '
                                            'sondalamalar sonrası ileri yaşlarda düşünülen invaziv tedavilerdir.'}]}]},
 {'id': 'Y34',
  'category': '👁️ Göz Şikayetleri',
  'age': '5 Yaş',
  'gender': 'Erkek',
  'complaint': 'Sağ gözde ani başlayan batma, yabancı cisim hissi, sulanma ve ışıktan rahatsız olma',
  'history': 'Beş yaşındaki erkek çocuk, yaklaşık 2 saat önce parkta kum havuzunda oynarken arkadaşının savurduğu kum '
             've tozların yüzüne gelmesi sonrası sağ gözünde aniden gelişen şiddetli ağrı, batma hissi, sürekli göz '
             'kırpma, sulanma ve ışığa bakamama şikayetiyle getirildi. Annesi çocuğun sağ gözünü eliyle sürekli '
             'ovuşturmaya çalıştığını, gözünü açmakta çok zorlandığını ve evde suyla yıkamalarına rağmen batma '
             'hissinin hiç geçmediğini ifade ediyor. Çocuğun delici bir cisim teması, göze darbe veya kimyasal madde '
             'maruziyeti öyküsü bulunmuyor.',
  'final_diagnosis': 'Korneal Abrazyon (Yüzeyel Kornea Epitel Defekti)',
  'disposition': 'Yeşil Alandan Ayaktan Topikal Profilaktik Antibiyotikli Damla, Analjezi ve Kontrol Randevusu ile '
                 'Taburculuk',
  'case_pearl': 'Çocuklarda yabancı cisim veya sürtünme öyküsü sonrası ani başlayan tek taraflı batma, ağrı, fotofobi '
                've blefarospazm varlığında korneal abrazyon ilk akla gelmelidir. Muayenede üst ve alt göz kapakları '
                'evert edilerek fornikslerde saklı yabancı cisim taranmalı, ardından vital boyama stripi ve kobalt '
                'mavisi ışıkla epitel defekti gösterilmelidir. Tedavide profilaktik topikal antibiyotik damla ve oral '
                'analjezik yeterlidir. Gözün kapatılması (oklüzyon) epitel rejenerasyonunu geciktirdiği ve enfeksiyon '
                'riskini artırdığı için güncel kılavuzlarda kontrendikedir. Topikal anestezikler toksik keratit riski '
                'nedeniyle asla eve reçete edilmemelidir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Parkta gözüne kum kaçtığı belirtilen ve blefarospazmı olan bu çocukta ilk aşamada en uygun '
                         'muayene yaklaşımı hangisidir?',
             'options': [{'text': 'Blefarospazmı aşmak için göz kapaklarını ekartörle zorlayarak aralamak ve kornea '
                                  'yüzeyini steril kuru gazlı bezle silerek temizlemek',
                          'is_correct': False,
                          'scenario_update': 'Kuru gazlı bezle mekanik silme girişimi kornea yüzeyel dokusunda ek '
                                             'mikrotravmaya ve çocuğun şiddetli ağlamasına neden oldu.',
                          'teaching_point': 'Göz yüzeyi asla kuru gazlı bezle silinmemelidir; kornea epitel '
                                            'bütünlüğünü korumak için nazik irrigasyon ve dikkatli inspeksiyon '
                                            'esastır.'},
                         {'text': 'Ayrıntılı ön segment muayenesini yapmadan önce hastaya ağrıyı kesmesi için eve '
                                  'reçete edilmek üzere topikal proparakain damlatmak',
                          'is_correct': False,
                          'scenario_update': 'Muayene tamamlanmadan damla verilmesi semptomları maskeledi; topikal '
                                             'anesteziklerin kontrolsüz kullanımı ciddi toksik keratit riski taşır.',
                          'teaching_point': 'Topikal anestezikler yalnızca hekim gözetiminde tanısal amaçla tek doz '
                                            'uygulanabilir; evde analjezik amaçlı kullanımı kesinlikle '
                                            'kontrendikedir.'},
                         {'text': 'Göz kapaklarını muayene etmeksizin penetran göz yaralanması şüphesiyle çocuğu '
                                  'hiçbir işlem yapmadan doğrudan cerrahi ameliyathaneye sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'Basit kum teması olan çocuk gereksiz cerrahi hazırlığa alındı; ön '
                                             'segment ve kapak değerlendirmesi yapılmadığı için süreç aksadı.',
                          'teaching_point': 'Öyküde künt veya penetran delici yaralanma mekanizması yoksa, gereksiz '
                                            'sevk öncesinde standart acil ön segment muayenesi tamamlanmalıdır.'},
                         {'text': 'Görme keskinliğini değerlendirmek, tek damla anestezik sonrası kapakları evert '
                                  'ederek fornikslerde saklı partikülleri serum fizyolojikle yıkamak',
                          'is_correct': True,
                          'explanation': 'Şiddetli blefarospazmda tek damla anestezik muayeneyi kolaylaştırır; kapak '
                                         'eversiyonu fornikste gizli yabancı cisimleri temizlemek için zorunludur.',
                          'new_finding': 'Görme keskinliği sol gözde 10/10, sağ gözde fotofobi nedeniyle 8/10. Sağ '
                                         'gözde siliyer ve konjonktival hiperemi mevcut, ön kamara derinliği normal, '
                                         'hifema yok, pupil ışık refleksleri doğal. Üst ve alt göz kapakları evert '
                                         'edilerek forniksler serum fizyolojikle yıkandı; konjonktivada kalıcı yabancı '
                                         'cisim veya çapak izlenmedi.'}]},
            {'stage_title': 'Tetkik ve İleri İnceleme Kararı',
             'question': 'Forniksleri yıkanan ancak kornea yüzeyinde batması devam eden bu çocukta epitel bütünlüğünü '
                         'değerlendirmek için en uygun adım hangisidir?',
             'options': [{'text': 'Göz küresi bütünlüğünü ve intraoküler yabancı cisim varlığını değerlendirmek '
                                  'amacıyla acil bilgisayarlı orbita ve kafa tomografisi çektirmek',
                          'is_correct': False,
                          'scenario_update': 'Yüzeyel toz teması olan hastaya çekilen orbita tomografisi normal '
                                             'sonuçlandı; çocuk gereksiz iyonizan radyasyon almış oldu.',
                          'teaching_point': 'Metalik veya yüksek enerjili delici yabancı cisim şüphesi bulunmayan '
                                            'yüzeyel irritasyon olgularında bilgisayarlı tomografi endike değildir.'},
                         {'text': 'Vital boyama stripi uygulayarak biyomikroskop veya oftalmoskop altında kobalt '
                                  'mavisi filtreli ışıkla kornea epitel yüzeyini incelemek',
                          'is_correct': True,
                          'explanation': 'Kobalt mavisi ışık altında vital boyama epitel defektlerini net olarak '
                                         'görünür kılar ve perforasyon bulgusu olan Seidel testine olanak tanır.',
                          'new_finding': 'Kobalt mavisi ışık altında kornea alt-orta kadranda yüzeyel epitel '
                                         'defektiyle uyumlu parlak yeşil boyanma izlendi. Ön kamara derinliği doğal, '
                                         'Seidel testi negatif (aköz sızıntısı yok).',
                          'image': 'assets/images/corneal_abrasion.png',
                          'image_caption': 'Korneal Flöresein İncelemesi: Kornea yüzeyinde lineer epitel abrazyonu'},
                         {'text': 'Olası fungal veya bakteriyel keratitleri erkenden tespit etmek için kornea '
                                  'yüzeyinden bistüri ucuyla kazıntı alıp mikrobiyolojiye göndermek',
                          'is_correct': False,
                          'scenario_update': 'Akut travmatik yüzeyel defekti olan çocukta korneal kazıntı uygulanması '
                                             'ağrıyı artırdı ve iyileşme sürecini geciktirerek lezyonu derinleştirdi.',
                          'teaching_point': 'İnfiltrat veya ülser tablosu olmayan akut travmatik epitel hasarlarında '
                                            'kornea kazıntısı yapılmaz; epitel rejenerasyonuna zarar verir.'},
                         {'text': 'Korneal lezyonu doğrulamak amacıyla ultrasonik pakimetri ile kornea kalınlığını ve '
                                  'endotel hücre yoğunluğunu acil serviste cihazla ölçmek',
                          'is_correct': False,
                          'scenario_update': 'Pakimetri probunun korneaya teması çocukta yoğun batmaya ve iritasyona '
                                             'yol açtı, yüzey hasarının genişlemesine sebep oldu.',
                          'teaching_point': 'Ultrasonik pakimetri veya endotel mikroskopisi akut yüzey epitel '
                                            'defektlerinin acil yönetiminde yeri olmayan elektif oftalmolojik '
                                            'incelemelerdir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Vital boyama altında korneada yeşil renkli lineer epitel defekti saptanan bu hastada en '
                         'olası klinik tanı nedir?',
             'options': [{'text': 'Bakteriyel Kornea Ülseri',
                          'is_correct': False,
                          'scenario_update': 'Kornea ülserinde (mikrobik keratit) beklenen stromal beyaz infiltrat, ön '
                                             'kamarada hipopiyon ve çevre dokuda yoğun nekroz hastada yoktu.',
                          'teaching_point': 'Bakteriyel keratitte stromal infiltrasyon ve pürülan eksüda görülür; akut '
                                            'travmatik yüzeyel abrazyonda ise stroma saydamdır.'},
                         {'text': 'Akut Ön Üveit',
                          'is_correct': False,
                          'scenario_update': 'Ön üveitte görülen siliyer kızarıklık, ön kamara hücresi (tyndall), '
                                             'miyotik ve düzensiz pupil gibi bulgular hastada mevcut değildi.',
                          'teaching_point': 'Ön üveit intraoküler inflamasyondur; kornea epitel defekti ve vital boya '
                                            'tutulumu üveitin primer bir bulgusu değildir.'},
                         {'text': 'Korneal Abrazyon',
                          'is_correct': True,
                          'explanation': 'Toz kaçması öyküsü, ani batma, fotofobi ve vital boyamada yüzeyel epitel '
                                         'defekti görülmesi korneal abrazyon için tanı koydurucudur.',
                          'new_finding': 'Klinik tanı Korneal Abrazyon (Yüzeyel Epitel Defekti) olarak '
                                         'kesinleştirildi.'},
                         {'text': 'Akut Açı Kapanması Glokomu',
                          'is_correct': False,
                          'scenario_update': 'Glokom krizinde izlenen fikse dilate pupil, sığ ön kamara, tahta '
                                             'sertliğinde göz küresi ve kornea epitel ödemi hastada yoktu.',
                          'teaching_point': 'Akut glokom çocuklarda son derece nadirdir ve yüksek göz içi basıncıyla '
                                            'seyreder; yüzeyel lineer epitel defekti oluşturmaz.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Protokolü',
             'question': 'Korneal abrazyon tanısı alan bu hastanın acil servis tedavisi ve taburculuk planı '
                         'aşağıdakilerden hangisi olmalıdır?',
             'options': [{'text': 'Topikal profilaktik antibiyotik damla, oral analjezik reçete edip, gözü kesinlikle '
                                  'kapatmayarak ertesi gün kontrole çağırmak',
                          'is_correct': True,
                          'explanation': 'Topikal antibiyotik sekonder enfeksiyonu önler; gözün kapatılmaması '
                                         '(oklüzyon yapılmaması) epitelin oksijenlenmesini ve hızla iyileşmesini '
                                         'sağlar.',
                          'new_finding': 'Hastaya topikal tobramisin damla ve oral analjezik başlandı; gözün '
                                         'kapatılmaması gerektiği tembihlendi ve ertesi gün kontrolü planlandı.'},
                         {'text': 'Ağrıyı dindirmek amacıyla göze kırk sekiz saat sıkı basılı göz bandajı uygulayıp '
                                  'antibiyotiksiz şekilde evine göndermek',
                          'is_correct': False,
                          'scenario_update': 'Gözün kapatılması kornea yüzeyinde hipoksiye yol açarak epitel '
                                             'iyileşmesini geciktirdi ve bakteriyel süperenfeksiyon riskini belirgin '
                                             'şekilde artırdı.',
                          'teaching_point': 'Güncel rehberlere göre korneal abrazyonlarda gözün kapatılması (patching) '
                                            'iyileşmeyi hızlandırmaz, ağrıyı azaltmaz ve enfeksiyon riskini artırır.'},
                         {'text': 'Hastanın göz ağrısı oldukça evde kendi kendine damlatması için topikal proparakain '
                                  'içeren lokal anestezik damlayı reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Evde kontrolsüz anestezik kullanan hastada kornea epitel rejenerasyonu '
                                             'durdu ve toksik keratite bağlı kalıcı korneal opasite gelişti.',
                          'teaching_point': 'Topikal anesteziklerin reçete edilmesi kornea epitel hücre toksisitesi, '
                                            'kalıcı erozyon ve korneal perforasyon riski nedeniyle kesinlikle '
                                            'kontrendikedir.'},
                         {'text': 'Korneadaki reaktif inflamasyonu hızla baskılamak amacıyla topikal deksametazon '
                                  'içeren kortikosteroidli göz damlasını bir hafta boyunca günde altı kez uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Steroid damla lokal immün yanıtı baskılayarak epitel defektinin '
                                             'derinleşmesine ve sekonder bakteriyel keratit gelişmesine yol açtı.',
                          'teaching_point': 'Epitel defekti varlığında topikal steroid kullanımı enfeksiyonu '
                                            'alevlendirir, yara iyileşmesini bozar ve korneal erimeye neden '
                                            'olabilir.'}]}]},
 {'id': 'Y35',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '2 Aylık',
  'gender': 'Kız',
  'complaint': 'Uykuya dalarken kollarda ve bacaklarda ani sıçrama ve titreme hareketleri',
  'history': 'İki aylık kız bebek, anne ve babası tarafından uykuya dalma esnasında kollarında ve bacaklarında ortaya '
             'çıkan tekrarlayıcı, hızlı, sıçrama ve atma benzeri hareketler nedeniyle panik halinde acil servise '
             'getirildi. Ailesi bu hareketlerin yaklaşık bir haftadır özellikle gece uykuya dalarken ve hafif uykuda '
             'fark edildiğini, günde birkaç kez 15-30 saniye sürdüğünü ve nöbet geçirdiğinden korktuklarını ifade '
             'ediyor. Anne, bebeğe dokunup uyandırdıklarında veya sıçrayan kolunu/bacağını nazikçe tuttuklarında '
             'hareketlerin hemen durduğunu fark ettiklerini belirtiyor. Uyanıkken bebeğin hareketleri, etrafa ilgisi, '
             'gülümsemesi ve anne sütüyle emmesi tamamen normaldir; ateş, kusma, kafa travması veya ailede erken yaşta '
             'epilepsi öyküsü yoktur.',
  'final_diagnosis': 'Yenidoğanın / İnfantın Selim Uyku Miyoklonusu (Benign Sleep Myoclonus)',
  'disposition': 'Yeşil Alandan Aileye Ayrıntılı Bilgilendirme ve Güvence Verilerek İlaçsız Taburculuk',
  'case_pearl': 'Yenidoğanın ve infantın selim uyku miyoklonusu, yalnızca uyku sırasında (özellikle Non-REM uykusunda) '
                'ortaya çıkan, ritmik veya aritmik hızlı sıçramalarla karakterize tamamen fizyolojik ve geçici bir '
                'tablodur. En kritik tanısal ve ayırt edici özelliği: Bebek uyandırıldığında veya sıçrayan ekstremite '
                'nazikçe tutulduğunda hareketlerin anında sonlanmasıdır (epileptik nöbetlerde ekstremiteyi tutmak veya '
                'uyandırmak hareketi durdurmaz). Uyanıkken nörolojik muayene ve gelişim tamamen normaldir, EEG '
                'negatiftir. Antiepileptik tedavi kesinlikle kontrendikedir (fenobarbital veya benzodiazepinler '
                'tabloyu kötüleştirebilir). Genellikle yaşamın ilk 6 ayı içinde kendiliğinden tamamen kaybolur.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Uyku sırasında sıçrama şikayetiyle getirilen bu bebekte patolojiyi aydınlatmak için en uygun '
                         'ilk klinik yaklaşım hangisidir?',
             'options': [{'text': 'Ailenin video kaydını ve öyküyü dinlemeksizin bebeği hızla solunum arresti riskiyle '
                                  'entübasyon hazırlığı yaparak resüsitasyon odasına almak',
                          'is_correct': False,
                          'scenario_update': 'Genel durumu mükemmel, pembe ve spontan soluyan bebekte agresif '
                                             'resüsitasyon hazırlığı ailede yoğun panik ve travmaya yol açtı.',
                          'teaching_point': 'Uyanıkken tamamen normal, vital bulguları stabil ve aktif sıkıntısı '
                                            'olmayan bebeklerde gereksiz invaziv resüsitatif yaklaşımlardan '
                                            'kaçınılmalıdır.'},
                         {'text': 'Vital bulguları, uyanıkken nörolojik muayeneyi, primitif refleksleri değerlendirmek '
                                  've uykudaki hareketlerin ekstremiteyi tutmakla durup durmadığını sorgulamak',
                          'is_correct': True,
                          'explanation': 'Uyanıkken nörolojik normallik ve hareketlerin ekstremite nazikçe '
                                         'tutulduğunda veya uyandığında anında durması fizyolojik ve epileptik olmayan '
                                         'ayrımında anahtardır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 128/dk, SS 34/dk, SpO2 %99, Kan Şekeri 94 '
                                         'mg/dL. Genel durum çok iyi, etrafla ilgili, aktif hareketli. Fontanel normal '
                                         'bombelikte, baş çevresi persentili %50. Nörolojik muayenede kas tonusu, '
                                         'derin tendon refleksleri, Moro, yakalama ve emme refleksleri tamamen '
                                         'fizyolojik. Ailenin telefonla çektiği video izlendiğinde uykuya dalarken '
                                         'bilateral kollarda senkron ve asenkron ritmik sıçramalar izlendi; anne kolu '
                                         'tuttuğunda hareketin derhal durduğu görüldü.'},
                         {'text': 'Hareketleri epileptik status olarak kabul edip damar yolu dahi açılmadan rektal '
                                  'diazepam uygulayarak nöroloji yoğun bakımına sevki başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Uykudan uyandırıldığında tamamen normal olan bebeğe gereksiz '
                                             'benzodiazepin uygulanması solunum depresyonuna ve sedasyona yol açtı.',
                          'teaching_point': 'Ekstremite tutulmasıyla duran ve uyanıkken görülmeyen hareketler '
                                            'epileptik değildir; gereksiz antiepileptik uygulanması zararlıdır.'},
                         {'text': 'Yalnızca kalp seslerini ve batın muayenesini yapıp nörolojik değerlendirmeyi ve '
                                  'hareketin videosunu incelemeyi sonraya ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Video kaydı incelenmediği ve nörolojik muayene yapılmadığı için '
                                             'paroksizmal hareketin karakteri ve epileptik olmayan doğası '
                                             'anlaşılamadı.',
                          'teaching_point': 'Paroksizmal motor olaylarda aile tarafından çekilen videolar ve ayrıntılı '
                                            'nörolojik muayene en değerli tanısal araçlardır.'}]},
            {'stage_title': 'Tetkik ve Klinik Yaklaşım Stratejisi',
             'question': 'Uyanıkken nörolojik muayenesi tamamen doğal olan ve tutmakla duran sıçramaları bulunan bu '
                         'bebekte en uygun inceleme yaklaşımı hangisidir?',
             'options': [{'text': 'Konvülziyon etiyolojisini ve santral sinir sistemi enfeksiyonlarını ekarte etmek '
                                  'amacıyla acil lomber ponksiyon yaparak beyin omurilik sıvısı incelemek',
                          'is_correct': False,
                          'scenario_update': 'Ateşi olmayan, uyanıkken aktif ve fontaneli sakin bebeğe invaziv lomber '
                                             'ponksiyon yapılması gereksiz komplikasyon riski yarattı.',
                          'teaching_point': 'Sistemik enfeksiyon bulgusu, ateşi veya nörolojik defisiti olmayan, '
                                            'fizyolojik hareket özellikleri taşıyan bebeklerde lomber ponksiyon endike '
                                            'değildir.'},
                         {'text': 'İntrakraniyal yapısal anomali veya kanamayı dışlamak amacıyla acil serviste genel '
                                  'anestezi altında kontrastlı kranial manyetik rezonans görüntüleme istemek',
                          'is_correct': False,
                          'scenario_update': "İki aylık sağlıklı bebeğin sedasyon ve anestezi alarak MRG'ye girmesi "
                                             'solunum sekresyon artışına ve hastanede gereksiz kalışa yol açtı.',
                          'teaching_point': 'Fokal nörolojik bulgusu olmayan, baş çevresi ve nöromotor gelişimi normal '
                                            'bebeklerde acil kranial MRG gereksiz bir tetkiktir.'},
                         {'text': 'Tipik klinik ve video özellikleri doğrultusunda acil invaziv tetkik veya '
                                  'görüntüleme yapmadan selim tabloyu açıklayıp izleme almak',
                          'is_correct': True,
                          'explanation': 'Öykü, tutulunca durma özelliği ve normal nörolojik muayene epileptik olmayan '
                                         'fizyolojik süreci gösterir; acil tetkik gerekmez.',
                          'new_finding': 'Tetkik istenmedi; paroksizmal olayın yalnızca uykuda ortaya çıkışı ve '
                                         'dokunmakla sonlanmasının selim fizyolojik bir motor fenomene işaret ettiği '
                                         'belirlendi.'},
                         {'text': 'Hemen acil 24 saatlik video-EEG monitorizasyonu başlatmak için bebeği üçüncü '
                                  'basamak epilepsi izlem merkezine yatış amacıyla sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'Acil sevk edilen bebeğe yapılan rutin uyanıklık ve uyku kayıtlarında '
                                             'epileptiform deşarj saptanmadı; aile aşırı anksiyeteye sürüklendi.',
                          'teaching_point': 'Tipik benign tablolarda acil EEG şart değildir; gerek duyulursa elektif '
                                            'şartlarda poliklinik kontrolünde planlanabilir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Yalnızca uykuda beliren, tutmakla anında duran sıçramaları ve normal nörolojik muayenesi '
                         'olan bu infantta en olası tanı nedir?',
             'options': [{'text': 'Yenidoğanın Selim Uyku Miyoklonusu',
                          'is_correct': True,
                          'explanation': 'Yalnızca uykuda görülen, ekstremite tutulunca veya bebek uyanınca derhal '
                                         'duran ve nörolojik gelişimi etkilemeyen tablo selim uyku miyoklonusudur.',
                          'new_finding': 'Klinik tanı Yenidoğanın / İnfantın Selim Uyku Miyoklonusu (Benign Sleep '
                                         'Myoclonus) olarak kesinleşti.'},
                         {'text': 'İnfantil Spazm Sendromu',
                          'is_correct': False,
                          'scenario_update': 'İnfantil spazmda (West sendromu) uyanırken kümelenen ani '
                                             'fleksiyon/ekstansiyon spazmları, hipsaritmi ve gelişimsel duraklama '
                                             'görülür.',
                          'teaching_point': 'İnfantil spazmlar uyanıkken kümeler halinde gelir, tutmakla durmaz ve '
                                            "ağır psikomotor gerileme ile EEG'de hipsaritmi eşlik eder."},
                         {'text': 'Erken İnfantil Epileptik Ensefalopati',
                          'is_correct': False,
                          'scenario_update': 'Ağır epileptik ensefalopatilerde bebeğin uyanıklığı bozuktur, hipotoni, '
                                             'emme güçlüğü ve tedaviye dirençli multifokal nöbetler mevcuttur.',
                          'teaching_point': 'Epileptik ensefalopatilerde ağır nörolojik bozukluk ve kesintisiz nöbet '
                                            'aktivitesi vardır; bu bebek uyanıkken tamamen sağlıklıdır.'},
                         {'text': 'Aşırı İrkilme Hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Hiperekplekside (aşırı irkilme) burun ucuna vurulduğunda uyanıkken '
                                             'abartılı irkilme ve yaygın hipertoni saptanır; bu hastada test '
                                             'negatiftir.',
                          'teaching_point': 'Hiperekpleksi dokunsal/işitsel uyaranla tetiklenen uyanıkken de olan '
                                            'şiddetli spazmdır; uykuda spontan oluşan izole sıçramalardan '
                                            'farklıdır.'}]},
            {'stage_title': 'Tedavi ve Aile Bilgilendirmesi',
             'question': 'Selim uyku miyoklonusu tanısı konulan 2 aylık bebeğin acil servis yönetimi ve taburculuk '
                         'yaklaşımı nasıl olmalıdır?',
             'options': [{'text': 'Nöbetlerin tekrarlamasını engellemek amacıyla idame oral fenobarbital şurup '
                                  'tedavisi başlayıp bir ay sonra çocuk nörolojisi polikliniğine kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Başlanan fenobarbital miyoklonik hareketleri baskılamadığı gibi bebekte '
                                             'derin sedasyon, emme tembelliği ve solunum ritim bozukluğuna yol açtı.',
                          'teaching_point': 'Selim uyku miyoklonusunda antiepileptikler etkisizdir; hatta '
                                            'benzodiazepin ve fenobarbital hareketlerin sıklığını paradoksal olarak '
                                            'artırabilir.'},
                         {'text': 'Bebeğin uyku esnasında hipoksiye girebileceği endişesiyle aileye ev tipi '
                                  'kardiyopulmoner monitör cihazı reçete ederek hastaneye yatış planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ev tipi monitör sürekli yalancı alarmlar vererek ailenin anksiyetesini '
                                             've tükenmişliğini artırdı; bebeğin uykusu gereksiz yere bölündü.',
                          'teaching_point': 'Bu durum solunum durması veya kardiyak aritmi yapmaz; ev monitörü '
                                            'endikasyonu yoktur ve ebeveyn kaygısını artırmaktan başka işe yaramaz.'},
                         {'text': 'İstemsiz kas spazmlarını çözmek amacıyla oral baklofen damla reçete ederek bebeği '
                                  'acil servisten herhangi bir takip önermeksizin taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Baklofen kullanımı iki aylık bebekte santral hipotoni ve letarji tablosu '
                                             'oluşturarak acil servise tekrar başvuruya neden oldu.',
                          'teaching_point': 'Fizyolojik ve selim olan bu durumda hiçbir kas gevşetici veya santral '
                                            'etkili ilacın yeri yoktur; ciddi yan etki doğurur.'},
                         {'text': 'İlaç vermeksizin aileyi tablonun selim ve geçici olduğu konusunda rahatlatıp rutin '
                                  'çocuk polikliniği takibiyle taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Tablo fizyolojiktir, 6-12 ayda kendiliğinden geçer; aileye güvence vermek, '
                                         'uyanıkken nöbet veya gelişim geriliği olursa başvurmasını tembihlemek '
                                         'esastır.',
                          'new_finding': 'Aileye durumun selim doğası açıklandı, hareketlerin genellikle ilk 6 ayda '
                                         'kaybolacağı anlatıldı ve gereksiz ilaçtan kaçınılarak taburcu edildi.'}]}]},
 {'id': 'Y36',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '5 Yaş',
  'gender': 'Erkek',
  'complaint': 'Akşamları ve gece uykudan uyandıran iki taraflı bacak ağrısı',
  'history': "Annesi anlatıyor: 'Oğlum son 2 aydır haftada 2-3 gece bacaklarım sızlıyor diyerek ağlayarak uyanıyor. "
             'Her iki kaval kemiği ve baldırlarını ovmamızı istiyor, masaj yapınca rahatlayıp tekrar uykuya dalıyor. '
             'Sabah kalktığında ise hiçbir şeyi kalmıyor, gün boyu kreşte koşturup oynuyor. Gündüz hiç topallamıyor, '
             'eklemlerinde şişlik veya kızarıklık olmadı. Bu gece ağrısı çok şiddetlenince endişelenip acile '
             "getirdik.'",
  'final_diagnosis': 'Büyüme Ağrıları (Benign Noktürnal Ekstremite Ağrısı)',
  'disposition': 'Yeşil Alandan Aileye Güvence, Masaj/Sıcak Uygulama Eğitimi ve Rutin Poliklinik Önerisi ile '
                 'Taburculuk',
  'case_pearl': 'Tipik olarak 3-12 yaş arası çocuklarda görülen büyüme ağrıları (benign noktürnal ekstremite ağrısı), '
                'akşam veya gece ortaya çıkan, iki taraflı, derin sızlayıcı, eklemleri tutmayan ve sabah tamamen '
                'kaybolan ağrılardır. Gündüz ağrı olmaması, topallama veya fizik muayenede lokalize '
                'şişlik/hassasiyet/kızarıklık bulunmaması ve sistemik bulgu (ateş, kilo kaybı) olmaması benign '
                'niteliği gösterir; tetkiksiz izlem esastır, aile güvencesi, lokal masaj ve sıcak uygulama yeterlidir.',
  'steps': [{'stage_title': 'Fizik ve Lokomotor Sistem Muayenesi',
             'question': 'Gece uykudan uyandıran iki taraflı bacak ağrısıyla Yeşil Alana getirilen 5 yaşındaki bu '
                         'çocukta fizik muayenede öncelikle ne yapmalısınız?',
             'options': [{'text': 'Ağrının nöropatik bası kaynaklı olabileceğini düşünerek lumbosakral vertebraları '
                                  'palpe etmek, alt ekstremite derin tendon reflekslerini ve duyu seviyesini ayrıntılı '
                                  'incelemek',
                          'is_correct': False,
                          'scenario_update': 'Lumbosakral omurga ve nörolojik muayene tamamen doğal bulundu; ancak alt '
                                             'ekstremite eklemleri ve kemik yapıları değerlendirilmediği için organik '
                                             'patolojiler dışlanamadı.',
                          'teaching_point': 'İki taraflı bacak ağrısı olan çocukta öncelikle eklemler, kemikler ve kas '
                                            'grupları doğrudan muayene edilerek lokal inflamasyon, efüzyon ve '
                                            'hassasiyet araştırılmalıdır.'},
                         {'text': 'Alt ekstremite eklemlerinin hareket açıklığını, tibia ve baldır kaslarını '
                                  'palpasyonla, yürüyüş paternini ve bölgesel eritem veya ödem varlığını detaylı '
                                  'incelemek',
                          'is_correct': True,
                          'explanation': 'Çocuklarda gece gelen ekstremite ağrılarında ilk adım; artrit, osteomiyelit '
                                         'veya maligniteyi dışlamak için eklem hareket açıklığı, kemik hassasiyeti ve '
                                         'yürüyüş muayenesini yapmaktır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 92/dk. Her iki diz, ayak bileği ve kalça '
                                         'eklemlerinde hareket açıklığı tam ve ağrısız; efüzyon, ısı artışı veya '
                                         'eritem yok. Tibia ve baldır kaslarında hassasiyet saptanmadı. Yürüyüş '
                                         'paterni simetrik ve normal; topallama yok. Sistemik muayene ve lenf nodu '
                                         'değerlendirmesi doğal.'},
                         {'text': 'Ağrının derin ven trombozuna bağlı olabileceğini varsayarak her iki baldır çapını '
                                  'mezura ile ölçmek ve acil kompresyon ultrasonografisi planlayarak çocuğu Sarı Alana '
                                  'almak',
                          'is_correct': False,
                          'scenario_update': 'Baldır çapları simetrik bulundu ve tromboz risk faktörü olmayan çocuk '
                                             'gereksiz yere ileri acil alanına devredildi.',
                          'teaching_point': 'Önceden sağlıklı, travma veya santral kateter öyküsü olmayan bir çocukta '
                                            'iki taraflı gece ağrısı derin ven trombozu lehine değildir; Sarı Alana '
                                            'devir gerekmez.'},
                         {'text': 'Muayeneyi yalnızca çocuğun bacaklarını görsel olarak incelemekle sınırlı tutup '
                                  'ağrıyı psikolojik kökenli kabul ederek aileye çocuk psikiyatrisi randevusu '
                                  'almalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Eklemler ve kemik yapıları palpe edilmeden yapılan yüzeysel '
                                             'değerlendirme olası organik patolojilerin atlanma riskini doğurdu ve '
                                             'aileyi tedirgin etti.',
                          'teaching_point': 'Geceleri çocuğu uykudan uyandıran ağrılarda fizik muayene ve lokomotor '
                                            'sistem muayenesi eksiksiz yapılmadan fonksiyonel veya psikolojik '
                                            'etiketleme yapılmamalıdır.'}]},
            {'stage_title': 'Tetkik ve Laboratuvar İstem Kararı',
             'question': 'Gündüz tamamen asemptomatik olan, fizik muayenesi normal bulunan ve alarm bulgusu taşımayan '
                         'bu çocukta yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Kemik kaynaklı primer tümör veya lösemiyi ekarte etmek amacıyla her iki kruris iki '
                                  'yönlü direkt radyografisi ve periferik yayma tetkikleri istemek',
                          'is_correct': False,
                          'scenario_update': 'Radyografilerde periost reaksiyonu veya litik lezyon izlenmedi; '
                                             'periferik yayma normal bulundu ancak çocuk gereksiz radyasyon aldı ve '
                                             'ailesi aşırı kaygılandı.',
                          'teaching_point': 'Lokalize kemik hassasiyeti, tek taraflı tutulum, gündüz ağrısı, kilo '
                                            'kaybı ve gece terlemesi olmayan tipik noktürnal ağrılarda rutin '
                                            'radyografi veya yayma gerekmez.'},
                         {'text': 'İnflamatuar eklem hastalığını dışlamak amacıyla tam kan sayımı, eritrosit '
                                  'sedimentasyon hızı, C-reaktif protein, romatoid faktör ve antinükleer antikor '
                                  'paneli istemek',
                          'is_correct': False,
                          'scenario_update': 'Laboratuvar sonuçları: Hemoglobin 12.8 g/dL, Lökosit 7.200/mm³, CRP 0.8 '
                                             'mg/L, ESH 6 mm/saat, ANA negatif çıktı; çocuğa gereksiz invaziv damar '
                                             'yolu işlemi uygulandı.',
                          'teaching_point': 'Ateş, eklemde şişlik, hareket kısıtlılığı veya sabah tutukluğu olmayan '
                                            'tipik iki taraflı ağrılarda romatolojik otoantikor ve akut faz '
                                            'reaktanları paneli istenmez.'},
                         {'text': 'Öykü ve fizik muayene tipik benign noktürnal paterni desteklediği ve alarm bulgusu '
                                  'bulunmadığı için ek radyolojik veya biyokimyasal tetkik istememek',
                          'is_correct': True,
                          'explanation': 'Tipik klinik prezentasyonda (iki taraflı, akşam/gece gelen, sabah kaybolan, '
                                         'gündüz aktivitesi ve muayenesi doğal) tanı tamamen kliniktir; hiçbir '
                                         'laboratuvar veya görüntüleme tetkiki gerekmez.',
                          'new_finding': 'Ek laboratuvar veya görüntüleme tetkiki istenmedi. Öykü ve fizik muayene '
                                         'bulgularıyla tanısal değerlendirmeye geçildi.'},
                         {'text': 'Eklem içi kıkırdak hasarı ve erken evre sinoviti değerlendirmek amacıyla her iki '
                                  'diz eklemine yönelik kontrastlı manyetik rezonans görüntüleme randevusu planlamak',
                          'is_correct': False,
                          'scenario_update': 'Sedasyon gerektiren pahalı ve ileri düzey görüntüleme randevusu '
                                             'planlandı; ancak muayenesi doğal çocukta gereksiz sağlık kaynağı '
                                             'tüketimine yol açtı.',
                          'teaching_point': 'Eklem efüzyonu, hareket kısıtlılığı veya inflamasyon belirtisi olmayan, '
                                            'ağrısı baldır ve kaval kemiğinde lokalize çocuklarda manyetik rezonans '
                                            'görüntüleme kesinlikle endike değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik öykü ve normal fizik muayene bulguları ışığında bu hastadaki en olası tanı '
                         'hangisidir?',
             'options': [{'text': 'Büyüme Ağrıları (Benign Noktürnal Ekstremite Ağrısı)',
                          'is_correct': True,
                          'explanation': '3-12 yaş arasında akşam veya gece uykudan uyandıran, her iki bacakta sızlama '
                                         'yapan, masajla rahatlayan ve sabah tamamen düzelen tablo tipik büyüme '
                                         'ağrısıdır.',
                          'new_finding': 'Kesin Tanı: Büyüme Ağrıları (Benign Noktürnal Ekstremite Ağrısı).'},
                         {'text': 'Juvenil İdiyopatik Artrit (Oligoartiküler Tip)',
                          'is_correct': False,
                          'scenario_update': 'Hastada eklemde şişlik, sabah tutukluğu veya hareket kısıtlılığı '
                                             'bulunmamaktadır; ağrı eklemde değil kas-kemik derin dokusundadır.',
                          'teaching_point': 'Juvenil idiyopatik artrit eklemde efüzyon, ısı artışı ve en az 6 hafta '
                                            'süren sabah tutukluğu ile karakterizedir; gece masajla geçen ağrılarla '
                                            'seyretmez.'},
                         {'text': 'Akut Geçici Sinovit (Toksik Sinovit)',
                          'is_correct': False,
                          'scenario_update': 'Hastada kalça eklemi tutulumu, topallama veya eklem hareketinde ağrılı '
                                             'kısıtlılık saptanmamıştır; ağrı iki taraflı baldır-kaval bölgesindedir.',
                          'teaching_point': 'Geçici sinovit genellikle tek taraflı kalça ağrısı ve belirgin topallama '
                                            'ile acile başvurur; iki taraflı baldır sızlaması şeklinde görülmez.'},
                         {'text': 'Akut Hematatojen Osteomiyelit (Tibia Enfeksiyonu)',
                          'is_correct': False,
                          'scenario_update': 'Hastanın ateşi yoktur, kemik üzerinde fokal palpasyon hassasiyeti, '
                                             'eritem veya basamama tablosu bulunmamaktadır.',
                          'teaching_point': 'Akut osteomiyelitte ateş, tek taraflı lokalize şiddetli kemik '
                                            'hassasiyeti, üzerine basamama ve laboratuvarda yüksek akut faz '
                                            'reaktanları tipiktir.'}]},
            {'stage_title': 'Tedavi ve Aile Eğitimi Planı',
             'question': 'Benign noktürnal ekstremite ağrısı saptanan ve alarm bulgusu bulunmayan bu hastanın acil '
                         'servis yönetimi ve taburculuk planı nasıl olmalıdır?',
             'options': [{'text': 'Ağrı ataklarının kalsiyum ve D vitamini eksikliğine bağlı olduğunu belirterek '
                                  'tetkik yapmadan yüksek doz intramüsküler D vitamini ampulü uygulamak ve taburcu '
                                  'etmek',
                          'is_correct': False,
                          'scenario_update': 'Büyüme ağrılarının D vitamini veya kalsiyum eksikliğiyle doğrudan '
                                             'ilişkisi kanıtlanmamıştır; kontrolsüz yüksek doz vitamin uygulaması '
                                             'hiperkalsemi ve toksisite riski oluşturdu.',
                          'teaching_point': 'Büyüme ağrıları vitamin eksikliğine bağlı değildir; ampirik yüksek doz D '
                                            'vitamini vermek hatalı ve toksisite açısından tehlikeli bir yaklaşımdır.'},
                         {'text': 'Atak sıklığını azaltmak amacıyla her gece yatmadan önce düzenli olarak bir ay '
                                  'boyunca oral ibuprofen şurup içmesini ve spordan uzak durmasını önermek',
                          'is_correct': False,
                          'scenario_update': 'Her gece profilaktik NSAİİ kullanımı çocukta gastrit ve gastrointestinal '
                                             'kanama riskini artırdı; ayrıca gereksiz fiziksel aktivite kısıtlaması '
                                             'çocuğun gelişimini olumsuz etkiledi.',
                          'teaching_point': 'Büyüme ağrılarında her gece düzenli koruyucu analjezik verilmez ve '
                                            'fiziksel aktivite kısıtlanmaz; analjezikler yalnızca şiddetli atağın '
                                            'olduğu anlarda kullanılır.'},
                         {'text': 'Bacak kaslarını gevşetmek amacıyla oral santral etkili kas gevşetici reçete etmek '
                                  've olası maligniteleri dışlamak için üç gün sonra acil servise kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Pediatrik yaş grubunda endikasyonu olmayan santral kas gevşetici çocukta '
                                             'aşırı sedasyon ve hipotoniye yol açtı; acil servis tekrar başvurusu aile '
                                             'kaygısını artırdı.',
                          'teaching_point': 'Çocuklarda benign noktürnal ağrılarda santral kas gevşeticilerin yeri '
                                            'yoktur; taburculuk sonrası kontrol acil serviste değil gereğinde pediatri '
                                            'polikliniğinde yapılır.'},
                         {'text': 'Aileyi durumun iyi huylu olduğu konusunda rahatlatmak, ataklarda lokal masaj, ılık '
                                  'kompres ve gerektiğinde parasetamol önermek, gündüz semptomu olursa polikliniğe '
                                  'yönlendirmek',
                          'is_correct': True,
                          'explanation': 'Büyüme ağrılarının temel tedavisi ailenin rahatlatılması (güvence), atak '
                                         'sırasında bacak masajı, ılık uygulama ve gerekirse basit analjeziktir. '
                                         'Gündüz ağrısı veya topallama gibi kırmızı bayraklar gelişirse poliklinik '
                                         'kontrolü önerilir.',
                          'new_finding': 'Aileye benign gidişat anlatılarak güven verildi; masaj, sıcak uygulama ve '
                                         'kırmızı bayrak eğitimi verilerek hasta Yeşil Alandan taburcu edildi.'}]}]},
 {'id': 'Y37',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '8 Yaş',
  'gender': 'Kız',
  'complaint': 'Karın ağrısı ve hafif ateş',
  'history': "Annesi 8 yaşındaki kızını Yeşil Alana getiriyor: 'Kızım yaklaşık 1 hafta önce boğaz enfeksiyonu "
             'geçirmişti, ateşi ve boğaz ağrısı vardı, şurupla düzeldi. Ancak dün akşamdan beri göbek çevresinde ve '
             'karnının sağ alt tarafında sızlayıcı bir ağrı başladı. Sabah ateşi 37.8°C ölçüldü. İştahı azaldı ama hiç '
             "kusmadı ve ishali olmadı. Yürürken karnını tutuyor.'",
  'final_diagnosis': 'Akut Mezenterik Lenfadenit (Yeşil Alandan Sarı Alana Devir ve Cerrahi Dışlama Sonrası Destek '
                     'Tedavisi)',
  'disposition': 'Yeşil Alanda Değerlendirilip Sarı Alana Devir -> İV Hidrasyon / Batın USG / Çocuk Cerrahisi '
                 'Konsültasyonu ile Apandisit Dışlanarak Poliklinik Kontrolüyle Taburculuk',
  'case_pearl': 'Akut mezenterik lenfadenit, sıklıkla geçirilmiş bir üst solunum yolu enfeksiyonu veya gastroenterit '
                'sonrası mezenterik lenf nodlarının reaktif hiperplazisiyle ortaya çıkar ve akut apandisiti taklit '
                'edebilir. Sağ alt kadranda peritoneal irritasyon veya belirgin hassasiyet olan çocuklar Sarı Alana '
                'devredilmeli; kademeli kompresyonlu batın ultrasonografisinde apendiksin normal kalibrede (<6 mm) '
                'görülmesi ve mezenterde büyümüş ovoid lenf nodları kümelenmesi ile cerrahi akut batın dışlanmalıdır.',
  'steps': [{'stage_title': 'Yeşil Alanda Fizik Muayene ve Alan Kararı',
             'question': 'Bir hafta önce geçirilmiş üst solunum yolu enfeksiyonu sonrası sağ alt kadran ağrısıyla '
                         'başvuran bu çocukta ilk yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Tablonun geçirilmiş viral üst solunum yolu enfeksiyonuna bağlı basit karın ağrısı '
                                  'olduğunu belirterek Yeşil Alanda oral ibuprofen şurup içirip evine göndermek',
                          'is_correct': False,
                          'scenario_update': 'Sağ alt kadranda palpasyon hassasiyeti ve defans şüphesi olan hastanın '
                                             'batın muayenesi derinleştirilmeden analjezikle taburcu edilmesi cerrahi '
                                             'patolojilerin atlanma riskini artırdı.',
                          'teaching_point': 'Sağ alt kadran ağrısı ve ateşi olan her çocukta cerrahi batın şüphesi '
                                            'taşındığından muayene tamamlanmadan analjezikle ayaktan taburcu edilmez.'},
                         {'text': 'Karın ağrısının bağırsak motilite bozukluğuna ve dışkı sıkışmasına bağlı olduğunu '
                                  'düşünerek Yeşil Alanda rektal lavman uygulamak ve tuvalet sonrası hastayı tekrar '
                                  'değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Sağ alt kadranda lokalize inflamatuar hassasiyeti olan hastaya yapılan '
                                             'lavman intraluminal basıncı artırarak çocuğun ağrısını daha da '
                                             'şiddetlendirdi.',
                          'teaching_point': 'Sağ alt kadran hassasiyeti ve ateş varlığında akut apandisit ve cerrahi '
                                            'patolojiler ekarte edilmeden rektal lavman uygulamak kontrendikedir.'},
                         {'text': 'Karın muayenesinde sağ alt kadrandaki hassasiyet ve savunma bulgularını '
                                  'değerlendirip akut cerrahi batın şüphesiyle hastayı derhal Sarı Alana devretmek',
                          'is_correct': True,
                          'triggers_yellow_transfer': True,
                          'explanation': 'Sağ alt kadranda lokalize hassasiyet ve defans şüphesi cerrahi batın '
                                         '(apandisit vb.) açısından kırmızı bayraktır; hasta damar yolu açılması, '
                                         'yakın takip ve görüntüleme için Sarı Alana devredilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.8°C, KTA 104/dk, TA 105/68 mmHg. Batın muayenesinde '
                                         'sağ alt kadranda ve periumbilikal bölgede belirgin palpasyon hassasiyeti '
                                         'mevcut; hafif istemli defans şüphesi var, rebound saptanmadı. Bağırsak '
                                         'sesleri normoaktif. Orofarenkste hiperemi ve soluk tonsiller hipertrofi '
                                         'izlendi. Hasta ileri tetkik ve izlem için Sarı Alana devredildi!'},
                         {'text': 'Hastayı Yeşil Alanda tutarak ayakta direkt batın grafisi ve tam idrar tetkiki '
                                  'istemek, sonuçlar çıkana kadar bekleme odasında oral beslenmesine izin vermek',
                          'is_correct': False,
                          'scenario_update': 'Olası cerrahi batın tablosunda hastaya ağızdan gıda verilmesi acil '
                                             'anestezi açlık süresini bozdu; ayrıca direkt batın grafisi tanısal değer '
                                             'sağlamadı.',
                          'teaching_point': 'Akut sağ alt kadran ağrısında cerrahi dışlanana kadar hasta aç (NPO) '
                                            'tutulmalı, Sarı Alana devredilmeli ve radyasyonsuz ilk seçenek olan '
                                            'ultrasonografi planlanmalıdır.'}]},
            {'stage_title': 'Sarı Alanda Tetkik ve Görüntüleme Kararı',
             'question': 'Sarı Alana devralınan ve sağ alt kadran hassasiyeti bulunan bu çocukta akut cerrahi '
                         'patolojiyi dışlamak için hangi tetkikler istenmelidir?',
             'options': [{'text': 'Damar yolu açarak hidrasyon sağlamak, hemogram ve C-reaktif protein düzeyini '
                                  'inceleyip radyasyonsuz ilk basamak görüntüleme olan batın ultrasonografisi istemek',
                          'is_correct': True,
                          'explanation': 'Sağ alt kadran ağrısında ilk basamak yaklaşım ağızdan alımın kesilmesi, '
                                         'intravenöz hidrasyon, enfeksiyon belirteçleri ve cerrahi patolojileri '
                                         'radyasyonsuz dışlayan kademeli kompresyonlu ultrasonografidir.',
                          'new_finding': 'LABORATUVAR: Lökosit 10.800/mm³ (%65 nötrofil, %28 lenfosit), CRP 14 mg/L, '
                                         'TİT normal. BATIN USG: Sağ alt kadranda kör uçlu tübüler yapı (apendiks çapı '
                                         '4.4 mm) normal kalibrede, basılabilir ve çevre dokusu doğaldır; terminal '
                                         'ileum komşuluğunda mezenterde en büyüğü 9x16 mm boyutlarında çok sayıda '
                                         'ovoid reaktif lenf bezi kümelenmesi ve minimal serbest sıvı izlendi.'},
                         {'text': 'Ultrasonografinin operatör bağımlı ve yanıltıcı olabileceğini öngörerek vakit '
                                  'kaybetmeden doğrudan oral ve intravenöz kontrastlı tüm batın bilgisayarlı '
                                  'tomografisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Stabil pediatrik hastaya yüksek doz radyasyon ve intravenöz nefrotoksik '
                                             'kontrast madde verildi; ultrasonografiyle kolayca konulabilecek tanı '
                                             'için gereksiz risk alındı.',
                          'teaching_point': 'Çocuklarda akut karın ağrısında kılavuzların ilk basamak görüntüleme '
                                            'önerisi daima ultrasonografidir; bilgisayarlı tomografi yalnızca USG '
                                            'yetersiz veya şüpheli kaldığında düşünülür.'},
                         {'text': 'Görüntüleme istemeden önce sağ alt kadrana ampirik seftriakson ve metronidazol '
                                  'infüzyonu başlamak, 24 saat sonra klinik düzelme olmazsa ultrasonografi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Cerrahi akut batın veya viral zemin netleşmeden başlanan geniş '
                                             'spektrumlu antibiyotik klinik tablonun ve inflamatuar yanıtın takibini '
                                             'güçleştirdi.',
                          'teaching_point': 'Peritonit veya sepsis bulgusu olmayan stabil sağ alt kadran ağrılı '
                                            'çocukta tanı görüntüleme ile kesinleştirilmeden ampirik antibiyotik '
                                            'başlanmaz.'},
                         {'text': 'Tablonun kesinlikle cerrahi apandisit olduğunu kabul ederek hiçbir görüntüleme veya '
                                  'laboratuvar tetkiki istemeden hastayı doğrudan acil laparoskopik apendektomiye '
                                  'almak',
                          'is_correct': False,
                          'scenario_update': 'Görüntüleme yapılmadan ameliyata alınan hastada apendiksin tamamen '
                                             'normal olduğu, inflamasyonun mezenterik lenf bezlerinde yer aldığı '
                                             'görüldü (negatif apendektomi).',
                          'teaching_point': 'Sağ alt kadran ağrılarında apandisit şüphesi olsa dahi ultrasonografi ile '
                                            'ayırıcı tanı yapılmalıdır; çocuklarda negatif apendektomi oranını '
                                            'düşürmek için görüntüleme şarttır.'}]},
            {'stage_title': 'Sarı Alanda Kesin Tanı',
             'question': 'Geçirilmiş farenjit öyküsü, ılımlı inflamatuar yanıt, normal kalibrede apendiks ve '
                         'mezenterde büyümüş lenf bezleriyle kesin tanınız nedir?',
             'options': [{'text': 'Akut Flegmonöz Apandisit',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografide apendiks normal kalibrede (4.4 mm), kompresyonla '
                                             'tamamen basılabilir ve çevre dokusu reaksiyonsuz olarak izlenmiştir.',
                          'teaching_point': 'Akut apandisitte apendiks çapı ≥6 mm olup kompresyonla basılamaz, lümende '
                                            'hiperemi ve çevre mezenterik yağ dokusunda ekojenite artışı görülür.'},
                         {'text': 'İleokolik İntususepsiyon (İnvajinasyon)',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografide iç içe geçmiş bağırsak anslarına ait hedef (target) '
                                             'işareti veya psödo-böbrek görünümü saptanmamıştır.',
                          'teaching_point': 'İntususepsiyon genellikle daha küçük çocuklarda (3-36 ay) kolik tarzı '
                                            'ağrı ve ultrasonografide tipik simit/hedef görünümü ile seyreder.'},
                         {'text': 'Meckel Divertiküliti',
                          'is_correct': False,
                          'scenario_update': 'Meckel divertikülitinde tipik olarak rektal ağrısız masif kanama veya '
                                             'lokalize apandisit benzeri nekrotizan inflamasyon görülür; '
                                             'ultrasonografide kör sonlanan kistik/tübüler kitle saptanmamıştır.',
                          'teaching_point': 'Meckel divertikülü gastrointestinal kanama veya divertikülit ile prezente '
                                            'olur; mezenterde yaygın reaktif lenf bezi kümelenmesi ve normal apendiks '
                                            'bu tabloyu açıklamaz.'},
                         {'text': 'Akut Mezenterik Lenfadenit',
                          'is_correct': True,
                          'explanation': 'Geçirilmiş üst solunum yolu enfeksiyonunu takiben sağ alt kadranda '
                                         "apandisiti taklit eden ağrı, USG'de normal apendiks ve mezenterde >8 mm "
                                         'multipl büyümüş reaktif lenf bezleri akut mezenterik lenfadeniti gösterir.',
                          'new_finding': 'Kesin Tanı: Akut Mezenterik Lenfadenit.'}]},
            {'stage_title': 'Sarı Alanda Tedavi ve İzlem Planı',
             'question': 'Ultrasonografi ve Çocuk Cerrahisi konsültasyonuyla apandisit dışlanan akut mezenterik '
                         'lenfadenitli bu hastanın tedavisi ve taburculuk planı nasıl olmalıdır?',
             'options': [{'text': 'Lenfadenopatinin bakteriyel süpürasyona ilerlemesini engellemek amacıyla 14 gün '
                                  'süreyle oral amoksisilin-klavulanat ve sefiksim kombinasyonu reçete edip hastayı '
                                  'taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Viral enfeksiyon sonrası gelişen reaktif lenf bezleri için verilen geniş '
                                             'spektrumlu antibiyotik ikilisi çocukta dirençli ishale ve bağırsak '
                                             'florası bozulmasına yol açtı.',
                          'teaching_point': 'Akut mezenterik lenfadenit genellikle viral veya post-enfeksiyöz reaktif '
                                            'bir süreçtir; bakteriyel süpürasyon veya sepsis bulgusu yoksa rutin '
                                            'antibiyotik tedavisi endike değildir.'},
                         {'text': 'Oral hidrasyon ve semptomatik analjezi sağlamak, antibiyotiksiz izlemek, aileye '
                                  'kırmızı bayrak eğitimi vererek çocuk cerrahisi kontrolüyle taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Akut mezenterik lenfadenitte tedavi destekleyicidir (hidrasyon, parasetamol '
                                         'vb.). Rutin antibiyotik gerekmez. Apandisitin erken dönemde atlanmadığından '
                                         'emin olmak için aileye alarm bulguları (artan kusma, dirençli ateş, '
                                         'şiddetlenen ağrı) anlatılarak 24-48 saat sonra kontrol önerilir.',
                          'new_finding': 'Çocuk Cerrahisi konsültasyonu ile cerrahi akut batın dışlandı. Destek '
                                         'tedavisi, diyet ve kırmızı bayrak eğitimi verilerek hasta 48 saat sonra '
                                         'poliklinik kontrolü şartıyla taburcu edildi.'},
                         {'text': 'Apendiksin daha sonra reaktif lenf bezlerinin basısıyla iltihaplanabileceği '
                                  'gerekçesiyle hastayı cerrahi servise yatırarak profilaktik apendektomi operasyonu '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'Tamamen selim ve kendini sınırlayan mezenterik lenf bezi büyümesi için '
                                             'hastaya gereksiz genel anestezi ve cerrahi girişim uygulandı.',
                          'teaching_point': 'Mezenterik lenfadenit cerrahi bir antite değildir; apendiks normal ise '
                                            'profilaktik cerrahi yapılmaz, hasta klinik olarak izlenir.'},
                         {'text': 'Sağ alt kadrandaki lenf bezlerinin lenfoma veya granülomatöz süreç olabileceği '
                                  'şüphesiyle hastayı taburcu etmeden acil laparoskopik lenf nodu biyopsisi için '
                                  'yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Akut enfeksiyon sonrası reaktif ovoid lenf nodları bulunan stabil '
                                             'çocukta gereksiz ileri invaziv biyopsi işlemi yapıldı.',
                          'teaching_point': 'Üst solunum yolu enfeksiyonu sonrası gelişen ovoid, kortikomedüller '
                                            'ayrımı korunmuş reaktif lenf bezlerinde sistemik B bulgusu (kilo kaybı '
                                            'vb.) yoksa acil biyopsi endike değildir.'}]}]},
 {'id': 'Y38',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '10 Yaş',
  'gender': 'Erkek',
  'complaint': 'Aniden başlayan şiddetli sağ yan ve kasık ağrısı, bulantı',
  'history': "Annesi 10 yaşındaki oğlunu acil Yeşil Alana getiriyor: 'Yaklaşık 3 saat önce evde otururken birdenbire "
             'sağ böğrüne şiddetli bir sancı girdi. Ağrı dalga dalga geliyor, kıvrandırıyor, durduğu yerde duramıyor '
             've sağ kasığına vuruyor. İki kez safrasız kustu, tuvalete gittiğinde idrarını yaparken çok yandığını '
             "söyledi. Daha önce hiç böyle bir şikayeti olmamıştı, ateşi yok.'",
  'final_diagnosis': 'Sağ Distal Üreter Taşına Bağlı Renal Kolik (Ürolitiyazis / Nefrolitiyazis)',
  'disposition': 'Yeşil Alandan Sarı Alana Devir -> İV Hidrasyon / Spazmolitik / NSAİİ Analjezisi -> Üriner USG '
                 'Doğrulaması -> Çocuk Ürolojisi/Nefrolojisi Poliklinik Takibi ile Taburculuk',
  'case_pearl': 'Pediatrik taş hastalığı (ürolitiyazis), ani başlayan, paroksismal dalgalar halinde gelen yan (flank) '
                've alt kadrana/kasığa yansıyan şiddetli ağrı, bulantı-kusma ve mikroskopik/makroskopik hematüri ile '
                'başvurur. Şiddetli kıvrandırıcı ağrısı olan hastalar Yeşil Alanda tutulmayıp intravenöz hidrasyon ve '
                'nonsteroid antiinflamatuar analjezi için Sarı Alana devredilmelidir. İlk basamak görüntüleme üriner '
                "sistem USG'dir; <5 mm distal taşlarda medikal ekspulsif/destekleyici tedavi ve poliklinik takibi "
                'esastır.',
  'steps': [{'stage_title': 'Yeşil Alanda Muayene ve Triyaj Değerlendirmesi',
             'question': 'Aniden başlayan dalgalı sağ yan ağrısı ve huzursuzlukla Yeşil Alana getirilen bu çocukta ilk '
                         'yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Kostovertebral açı hassasiyetini ve batın bulgularını kontrol edip şiddetli ağrı '
                                  'nedeniyle hastayı intravenöz analjezi için Sarı Alana devretmek',
                          'is_correct': True,
                          'triggers_yellow_transfer': True,
                          'explanation': 'Paroksismal dalgalar halinde gelen şiddetli flank ağrısı, bulantı ve '
                                         'kostovertebral açı hassasiyeti acil damar yolu açılması, analjezi ve '
                                         'hidrasyon gerektirir; hasta derhal Sarı Alana devredilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 118/dk (ağrıya bağlı taşikardik), TA 118/76 '
                                         'mmHg. Hasta huzursuz, ağrı nedeniyle kıvranıyor ve yatakta pozisyon '
                                         'bulamıyor. Batın muayenesinde peritoneal irritasyon (defans/rebound) yok; '
                                         'sağ alt kadranda hafif hassasiyet mevcut. Sağ kostovertebral açı hassasiyeti '
                                         'belirgin pozitif. Genital muayene doğal. Hasta Sarı Alana devredildi!'},
                         {'text': 'Ağrının kas spazmına veya basit bel tutulmasına bağlı olduğunu düşünerek Yeşil '
                                  'Alanda oral kas gevşetici verip evde istirahat önermek',
                          'is_correct': False,
                          'scenario_update': 'Bulantı, miksiyon güçlüğü ve şiddetli kostovertebral açı hassasiyeti '
                                             'olan hastanın üriner patolojisi atlandı ve ağrısı evde dayanılmaz hale '
                                             'geldi.',
                          'teaching_point': 'Ani başlayan dalgalı yan ağrısı, bulantı ve kostovertebral açı '
                                            'hassasiyeti mekanik kas ağrısı değildir; üriner sistem obstrüksiyonu '
                                            'araştırılmalıdır.'},
                         {'text': 'Tabloyu akut apandisit kabul ederek cerrahi konsültasyon istemek ve hasta bekleme '
                                  'salonundayken ağrı kesici vermeden muayene bulgularının netleşmesini beklemek',
                          'is_correct': False,
                          'scenario_update': 'Hasta saatlerce şiddetli kıvrandırıcı ağrı çekti; peritoneal irritasyonu '
                                             'olmayan hastada uygun analjezi geciktirildi.',
                          'teaching_point': 'Kıvrandırıcı, dalgalar halinde gelen ve yatakta sabit durdurmayan ağrılar '
                                            'peritoneal değil visseral/obstrüktif tiptedir; analjezi gereksiz yere '
                                            'geciktirilmemelidir.'},
                         {'text': 'Hastanın ağrısını hafifletmek amacıyla Yeşil Alanda sıcak su torbası uygulamak ve '
                                  'ağızdan bol miktarda soğuk su içirerek hastayı bekletmek',
                          'is_correct': False,
                          'scenario_update': 'Akut obstrüksiyon ve bulantısı olan hastaya ağızdan yüksek hacimli sıvı '
                                             'verilmesi kusmayı tetikledi ve renal pelvis içi basıncı artırdı.',
                          'teaching_point': 'Akut kolik atağı sırasında ağızdan kontrolsüz aşırı sıvı verilmesi '
                                            'intrarenal basıncı ve bulantıyı artırır; intravenöz kontrollü hidrasyon '
                                            've analjezi esastır.'}]},
            {'stage_title': 'Sarı Alanda Tetkik ve Görüntüleme İstem Kararı',
             'question': 'Sarı Alana devralınan, şiddetli sağ yan ağrısı ve miksiyon sırasında yanması olan bu çocukta '
                         'tanısal yaklaşımınız nasıl olmalıdır?',
             'options': [{'text': 'Doğrudan yüksek doz radyasyon içeren kontrastlı tüm batın bilgisayarlı tomografisi '
                                  'çekerek tanı kesinleşene kadar hastaya hiçbir analjezik ilaç vermemek',
                          'is_correct': False,
                          'scenario_update': 'Pediatrik hastaya radyasyonsuz ilk basamak ultrasonografi yerine yüksek '
                                             'radyasyonlu tetkik uygulandı ve hasta gereksiz yere şiddetli ağrı çekti.',
                          'teaching_point': 'Pediatrik üriner obstrüksiyon şüphesinde ilk basamak görüntüleme '
                                            'radyasyonsuz ultrasonografidir; ayrıca uygun analjezi tanı sürecini '
                                            'maskelemez.'},
                         {'text': 'Yalnızca intravenöz parasetamol infüzyonu uygulayıp hiçbir idrar tetkiki veya '
                                  'radyolojik görüntüleme istemeden hastayı doğrudan taburcu ederek poliklinik '
                                  'kontrolüne yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'İdrar tetkiki ve ultrasonografi yapılmadığı için toplayıcı sistem '
                                             'dilatasyonu ve obstrüksiyonun düzeyi aydınlatılamadı.',
                          'teaching_point': 'Kıvrandırıcı yan ağrısı olan çocukta hematüriyi saptamak için idrar '
                                            'tetkiki ve obstrüksiyonu görmek için ultrasonografi zorunludur.'},
                         {'text': 'Üriner sistem enfeksiyonu şüphesiyle yalnızca tam idrar tetkiki ve idrar kültürü '
                                  'isteyerek acil ultrasonografi yapmadan ampirik seftriakson infüzyonu başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Ateşi olmayan hastada mekanik obstrüksiyon görüntülenmeden gereksiz yere '
                                             'parenteral antibiyotik başlandı ve altta yatan kalsifiye odak '
                                             'araştırılmadı.',
                          'teaching_point': 'Ateş ve piyüri olmayan akut yan ağrısında antibiyotik değil; '
                                            'obstrüksiyonu saptamak için ultrasonografi ve analjezi önceliklidir.'},
                         {'text': 'Damar yolu açarak hidrasyon ve nonsteroid analjezi uygulamak, tam idrar tetkiki, '
                                  'böbrek fonksiyonları ve acil üriner ultrasonografi istemek',
                          'is_correct': True,
                          'explanation': 'Akut böğür ağrısı ve obstrüksiyon yönetiminde ilk adım nonsteroid '
                                         'antiinflamatuar analjezi ve hidrasyondur; mikroskopik hematüriyi gösteren '
                                         'TİT ve toplayıcı sistem dilatasyonunu/kalkülü gösteren USG ilk basamaktır.',
                          'new_finding': 'LABORATUVAR: Üre 24 mg/dL, Kreatinin 0.52 mg/dL. TİT: Dansite 1025, pH 5.5, '
                                         'Lökosit negatif, Nitrit negatif, Mikroskopi: 15-20 eritrosit (mikroskopik '
                                         'hematüri). ÜRİNER USG: Sağ böbrek boyutları normal, toplayıcı sistemde evre '
                                         '1 pelvikaliektazi izlendi; sağ üreterovezikal bileşkede 4 mm çapında '
                                         'posterior akustik gölgelenme veren intraluminal kalsifiye ekojen kalkül '
                                         'saptandı.'}]},
            {'stage_title': 'Sarı Alanda Kesin Tanı',
             'question': 'Kıvrandırıcı yan ağrısı, mikroskopik hematüri ve ultrasonografide üreterovezikal bileşkede '
                         'akustik gölgeli odak saptanan bu hastada kesin tanı nedir?',
             'options': [{'text': 'Akut Bakteriyel Piyelonefrit Enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Hastanın ateşi yoktur, idrar tetkikinde lökositüri veya nitrit '
                                             'saptanmamış, toplayıcı sistemde kalsifiye kalkül izlenmiştir.',
                          'teaching_point': 'Piyelonefrit yüksek ateş, titreme, sistemik toksisite ve piyüri ile '
                                            'seyreder; hematüri ve akustik gölgeli kalkül mekanik taş hastalığını '
                                            'gösterir.'},
                         {'text': 'Sağ Distal Üreter Taşı (Ürolitiyazis)',
                          'is_correct': True,
                          'explanation': 'Ani başlayan yan ağrısı, mikroskopik hematüri ve ultrasonografide '
                                         'üreterovezikal bileşkede 4 mm boyutunda akustik gölgeli kalkül ile hafif '
                                         'hidronefroz görülmesi ürolitiyazise bağlı renal kolik tanısını '
                                         'kesinleştirir.',
                          'new_finding': 'Kesin Tanı: Sağ Distal Üreter Taşına Bağlı Renal Kolik (Ürolitiyazis).'},
                         {'text': 'Akut Flegmonöz Apandisit Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Batın muayenesinde peritoneal irritasyon yoktur; tam idrar tetkikinde '
                                             'hematüri ve ultrasonografide üreter obstrüksiyonu saptanmıştır.',
                          'teaching_point': 'Apandisitte göbek çevresinden sağ alta göç eden ağrı, anoreksi ve '
                                            'peritonit bulguları tipiktir; belirgin hematüri ve üreterde kalkül '
                                            'beklenmez.'},
                         {'text': 'Sağ Akut Testiküler Epididimo-orşit',
                          'is_correct': False,
                          'scenario_update': 'Skrotal muayenede testisler ve epididimler tamamen doğal, ağrısız ve '
                                             'simetrik bulunmuştur.',
                          'teaching_point': 'Epididimit skrotumda şişlik, lokalize hassasiyet ve ısı artışı ile '
                                            'karakterizedir; flank ağrısı ve mikroskopik hematürinin primer nedeni '
                                            'değildir.'}]},
            {'stage_title': 'Sarı Alanda Tedavi ve Taburculuk Planı',
             'question': 'Distal üreterde 4 mm taş ve hafif dilatasyon saptanan, böbrek fonksiyonları normal bu '
                         'hastada taburculuk ve tedavi protokolü ne olmalıdır?',
             'options': [{'text': 'Taşın kendiliğinden düşme olasılığı bulunmadığını belirterek hastayı derhal acil '
                                  'ameliyathaneye almak ve cerrahi rijit üreterorenoskopi ile lazer litotripsi '
                                  'operasyonu uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Distal yerleşimli 4 mm boyutundaki taşların büyük çoğunluğu medikal '
                                             'tedaviyle kendiliğinden düşer; acil invaziv cerrahi girişim gereksiz '
                                             'anestezi ve üreter travması riski oluşturdu.',
                          'teaching_point': 'Çocuklarda <5 mm distal üreter taşlarında enfeksiyon veya inatçı '
                                            'obstrüksiyon yoksa ilk yaklaşım konservatif izlem ve medikal ekspulsif '
                                            'tedavidir; acil cerrahi gerekmez.'},
                         {'text': 'İdrar yolu enfeksiyonu profilaksisi amacıyla bir ay boyunca oral siprofloksasin '
                                  'tedavisi başlamak ve taş düşene dek hastanın yatak istirahatinde kalmasını önermek',
                          'is_correct': False,
                          'scenario_update': 'Enfeksiyonu olmayan hastada uygunsuz florokinolon kullanımı yan etkilere '
                                             'yol açtı; ayrıca yatak istirahati taşın idrar akımıyla ilerlemesini '
                                             'geciktirdi.',
                          'teaching_point': 'Steril ürolitiyaziste profilaktik antibiyotik endike değildir; aksine '
                                            'hastanın mobilize olması taşın spontan geçişini kolaylaştırır.'},
                         {'text': 'Ağrısı gerileyen hastaya bol sıvı alımı, analjezik ve idrar süzme eğitimi verip '
                                  'Çocuk Ürolojisi poliklinik kontrolüyle taburcu etmek',
                          'is_correct': True,
                          'explanation': "Komplike olmayan, 4 mm'lik distal taşlarda yaklaşım: bol hidrasyon, aralıklı "
                                         'analjezi, taş analizi için idrar süzme eğitimi ve elektif poliklinik '
                                         'takibidir.',
                          'new_finding': 'Analjezi ve hidrasyonla semptomları düzelen hasta, bol sıvı tüketimi ve '
                                         'idrar süzme önerileriyle Çocuk Ürolojisi takibine yönlendirilerek taburcu '
                                         'edildi.'},
                         {'text': 'Hafif pelvikaliektazi saptandığı için hastayı nefroloji servisine yatırmak, mutlak '
                                  'aç bırakıp 48 saat boyunca aralıksız intravenöz yüksek doz furosemid uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Obstrükte sisteme yüksek doz kıvrım diüretiği verilmesi intrapelvik '
                                             'basıncı aşırı artırarak şiddetli ağrı krizine ve elektrolit '
                                             'dengesizliğine neden oldu.',
                          'teaching_point': 'Akut taş obstrüksiyonunda furosemid gibi güçlü diüretikler intraluminal '
                                            'basıncı artırarak forniks rüptürü riski yaratır; kesinlikle '
                                            'uygulanmamalıdır.'}]}]},
 {'id': 'Y39',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '7 Yaş',
  'gender': 'Kız',
  'complaint': 'Son haftalarda aşırı su içme, sık idrara çıkma ve gece altını ıslatma',
  'history': "Annesi 7 yaşındaki kızını Yeşil Alana getiriyor: 'Kızım son 3 haftadır sürekli susadığını söylüyor, "
             'günde 3-4 litre su içiyor. Okulda ve evde neredeyse saat başı tuvalete gidiyor. 3 yaşından beri hiç gece '
             'altına kaçırmazken son 10 gündür her gece yatağını ıslatmaya başladı. İştahı iyi olmasına rağmen son 2 '
             "haftada kilo verdiğini ve hafif halsizleştiğini fark ettik. Ateşi, kusması veya nefes darlığı yok.'",
  'final_diagnosis': 'Yeni Başlangıçlı Tip 1 Diabetes Mellitus (Ketoasidoz Tablosu Olmayan Hafif Hiperglisemi)',
  'disposition': 'Yeşil Alandan Sarı Alana Devir -> Kan Gazı / Elektrolit / İdrar Ketonu Değerlendirmesi -> DKA '
                 'Dışlanarak Çocuk Endokrinoloji Servisine İnsülin Başlanması ve Eğitim İçin Yatış',
  'case_pearl': 'Çocuklarda polidipsi, poliüri, sekonder enürezis ve açıklanamayan kilo kaybı yeni başlangıçlı tip 1 '
                'diyabet için klasik dörtlüdür. Yeşil Alanda kapiller kan glukozu >200 mg/dL ölçülen her çocuk '
                'ketoasidoz (DKA) riski açısından derhal Sarı Alana devredilmeli; kan gazı (pH, HCO3) ve idrar/kan '
                'ketonu bakılmalıdır. Asidozu olmayan (pH ≥7.30, HCO3 ≥18) stabil vakalara intravenöz insülin '
                'infüzyonu yerine Çocuk Endokrinoloji servisinde subkutan insülin rejimi ve aile eğitimi başlanır.',
  'steps': [{'stage_title': 'Yeşil Alanda Klinik Değerlendirme ve Alan Kararı',
             'question': 'Polidipsi, poliüri ve sekonder enürezis öyküsüyle Yeşil Alana başvuran bu 7 yaşındaki '
                         'çocukta ilk basamak yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Şikayetleri primer enürezis noktürna ve idrar yolu enfeksiyonu olarak yorumlayıp '
                                  'Yeşil Alanda tam idrar tetkiki isteyerek oral antibiyotik reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Polidipsi ve kilo kaybı eşlik eden çocukta glukoz değerlendirilmediği '
                                             'için altta yatan metabolik bozukluk atlandı.',
                          'teaching_point': 'Kısa sürede gelişen polidipsi, poliüri ve kilo kaybı varlığında basit '
                                            'idrar yolu enfeksiyonu düşünülmeden önce mutlaka glukoz düzeyi kontrol '
                                            'edilmelidir.'},
                         {'text': 'Aşırı su içmenin psikojenik polidipsiye bağlı olduğunu varsayarak aileye evde sıkı '
                                  'sıvı kısıtlaması uygulamalarını önermek ve çocuğu taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Ozmotik diürezi olan çocukta sıvı kısıtlaması yapılması intravasküler '
                                             'volüm açığını hızla derinleştirerek hipovolemik şok tablosuna zemin '
                                             'hazırladı.',
                          'teaching_point': 'Ozmotik diürezi olan çocuklarda metabolik bozukluk ekarte edilmeden sıvı '
                                            'kısıtlaması yapılması ölümcül dehidratasyon ve şoka neden olabilir.'},
                         {'text': 'Bilinç açık ve solunum rahat olduğu için hastayı Yeşil Alanda tutarak ayaktan Çocuk '
                                  'Nefrolojisi polikliniğine tübüler fonksiyon testleri için yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Akut glukoz yüksekliği riski taşıyan çocuk poliklinik randevusu için eve '
                                             'gönderildi ve saatler içinde dehidratasyonu derinleşti.',
                          'teaching_point': 'Yeni başlangıçlı poliüri ve kilo kaybı olan çocukta acil serviste kan '
                                            'şekeri ölçülmeden hasta elektif polikliniklere sevk edilmemelidir.'},
                         {'text': 'Vital bulguları ve dehidratasyon derecesini değerlendirmek, acil parmaktan kapiller '
                                  'kan şekeri ölçümü yaparak hastayı izlem için Sarı Alana devretmek',
                          'is_correct': True,
                          'triggers_yellow_transfer': True,
                          'explanation': 'Polidipsi, poliüri, sekonder enürezis ve kilo kaybı klasik ozmotik diürez '
                                         'bulgularıdır; acil kapiller glukoz bakılmalı ve metabolik risk nedeniyle '
                                         'hasta Sarı Alana alınmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 98/dk, Solunum 20/dk, SpO2 %99, TA 102/64 '
                                         'mmHg. Bilinç açık ve oryante; Kussmaul solunumu veya nefeste aseton kokusu '
                                         'yok. Mukoza hafif kuru, kapiller dolum 2 saniye (hafif dehidratasyon). '
                                         'Parmaktan ölçülen kapiller kan şekeri 310 mg/dL bulundu. Hasta Sarı Alana '
                                         'devredildi!'}]},
            {'stage_title': 'Sarı Alanda Metabolik Tetkik ve Durum Değerlendirmesi',
             'question': 'Sarı Alana devralınan ve kan şekeri 310 mg/dL ölçülen hastada asidoz ve elektrolit '
                         'dengesizliğini dışlamak için hangi tetkikler istenmelidir?',
             'options': [{'text': 'Hemen intravenöz kristalize regüler insülin puşesi uygulamak ve ardından hiçbir kan '
                                  'tetkiki istemeden hastayı doğrudan yoğun bakıma transfer etmek',
                          'is_correct': False,
                          'scenario_update': 'Kan gazı ve potasyum düzeyi bilinmeden yapılan İV bolus insülin ani '
                                             'hipokalemiye, kardiyak aritmilere ve hızlı ozmotik kaymaya yol açtı.',
                          'teaching_point': 'Pediatrik yaş grubunda yüksek kan şekerinde asla intravenöz bolus insülin '
                                            'puşe yapılmaz; önce kan gazı, potasyum ve keton değerlendirilmelidir.'},
                         {'text': 'Venöz kan gazı, serum elektrolitleri, böbrek fonksiyon testleri, tam idrar '
                                  'tetkikinde keton incelemesi ve hemoglobin A1c konsantrasyonu istemek',
                          'is_correct': True,
                          'explanation': 'Kan şekeri yüksek saptanan çocukta temel amaç ketoasidoz tablosunu (asidemi, '
                                         'hipobikarbonatemi, ketonüri) değerlendirmek, elektrolit dengesini görmek ve '
                                         'kronik glisemik yükü (HbA1c) doğrulamaktır.',
                          'new_finding': 'LABORATUVAR: Venöz Kan Gazı: pH 7.38, pCO2 38 mmHg, HCO3 22 mmol/L, Baz '
                                         'açığı -1.8 mEq/L (asidoz yok). Serum Na 136 mEq/L, K 4.3 mEq/L, Glukoz 308 '
                                         'mg/dL, Üre 22 mg/dL, Kreatinin 0.48 mg/dL. TİT: Dansite 1030, Glukoz (++++), '
                                         'Keton negatif (eser), protein negatif. HbA1c: %10.4.'},
                         {'text': 'Metabolik tetkikleri erteleyerek yalnızca kraniyal bilgisayarlı tomografi çekmek ve '
                                  'intrakraniyal kitleye sekonder santral hormon yetmezliği tablosunu araştırmak',
                          'is_correct': False,
                          'scenario_update': 'Nörolojik defisiti olmayan çocuğa yüksek doz radyasyon verildi ve '
                                             'metabolik tablonun doğrulanması saatlerce gecikti.',
                          'teaching_point': 'Kilo kaybı, poliüri ve glukoz yüksekliği olan çocukta ilk incelenmesi '
                                            'gereken sistem santral sinir sistemi görüntülemesi değil metabolik kan '
                                            'tetkikleridir.'},
                         {'text': 'Oral rehidratasyon sıvısı verip laboratuvar tetkiki istemeden hastayı altı saat '
                                  'sonra tekrar kan şekeri ölçümü için sarı alanda bekletmek',
                          'is_correct': False,
                          'scenario_update': 'Kan gazı ve keton kontrolü yapılmadan bekletilen hastada olası asidoz '
                                             'tablosunun erken tanısı ve uygun servise sevki gecikti.',
                          'teaching_point': 'Yüksek kan şekeriyle başvuran çocukta asidoz ve ketoz varlığı acilen '
                                            'teyit edilmelidir; tetkiksiz saatlerce beklemek doğru bir yaklaşım '
                                            'değildir.'}]},
            {'stage_title': 'Sarı Alanda Kesin Tanı',
             'question': 'Poliüri, polidipsi, kan glukozu >200 mg/dL, HbA1c %10.4 ve normal kan gazı (pH 7.38, HCO3 '
                         '22) parametreleriyle kesin tanınız nedir?',
             'options': [{'text': 'Ağır Diyabetik Ketoasidoz Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Hastanın kan gazında pH 7.38 ve HCO3 22 mmol/L olup asidoz yoktur; '
                                             'idrarda belirgin keton saptanmamıştır.',
                          'teaching_point': 'Diyabetik ketoasidoz tanısı için hiperglisemiye ek olarak venöz pH <7.30 '
                                            'veya serum bikarbonatı <18 mmol/L ve belirgin ketonemi/ketonüri şarttır.'},
                         {'text': 'Primer Santral Diabetes İnsipidus',
                          'is_correct': False,
                          'scenario_update': 'Hastada masif glikozüri, kan glukozu 308 mg/dL ve HbA1c %10.4 '
                                             'saptanmıştır; tablo ADH eksikliğiyle uyumlu değildir.',
                          'teaching_point': 'Diabetes insipidusta idrar dansitesi düşüktür (<1005) ve kan şekeri '
                                            'normaldir; glukoz yüksekliği ve glikozüri görülmez.'},
                         {'text': 'Ketoasidozsuz Yeni Başlangıçlı Tip 1 Diabetes Mellitus',
                          'is_correct': True,
                          'explanation': 'Polidipsi, poliüri, kilo kaybı, rastgele venöz plazma glukozu ≥200 mg/dL ve '
                                         'yüksek HbA1c birlikteliği tip 1 diyabet tanısı koydurur. Kan gazının normal '
                                         'olması (pH >7.30, HCO3 >18) ve ketonüri bulunmaması ketoasidozun olmadığını '
                                         'gösterir.',
                          'new_finding': 'Kesin Tanı: Ketoasidozsuz Yeni Başlangıçlı Tip 1 Diabetes Mellitus.'},
                         {'text': 'Kalıtsal İzole Renal Glikozüri',
                          'is_correct': False,
                          'scenario_update': 'Renal glikozüride kan glukoz düzeyi ve HbA1c tamamen normaldir; tübüler '
                                             'emilim defekti nedeniyle yalnızca idrarda şeker çıkar.',
                          'teaching_point': 'Renal glikozüride sistemik hiperglisemi, yüksek HbA1c veya '
                                            'poliüri-polidipsi sendromu görülmez; kan şekeri daima fizyolojik '
                                            'sınırlardadır.'}]},
            {'stage_title': 'Sarı Alanda Tedavi ve Servis Yatış Planı',
             'question': 'Ketoasidoz tablosu bulunmayan (pH 7.38, HCO3 22 mmol/L), genel durumu stabil tip 1 diyabetli '
                         'bu çocuğun yönetim planı nasıl olmalıdır?',
             'options': [{'text': 'Asidozu olmadığı için intravenöz insülin vermemek, oral beslenmeyi sürdürerek '
                                  'subkutan insülin protokolü ve eğitimi için Çocuk Endokrinoloji servisine yatırmak',
                          'is_correct': True,
                          'explanation': 'Ketoasidozu olmayan yeni tanı tip 1 diyabetli çocuklarda yoğun İV insülin '
                                         'infüzyonu veya agresif mayi tedavisi endike değildir. Hasta oral '
                                         'beslenebilir; Çocuk Endokrinoloji servisine yatırılarak subkutan çoklu doz '
                                         'insülin başlanır ve aileye kapsamlı diyabet eğitimi verilir.',
                          'new_finding': 'Çocuk Endokrinoloji kliniği ile konsülte edilen hasta, subkutan insülin '
                                         'tedavisi başlanması ve kapsamlı aile diyabet eğitimi verilmesi amacıyla '
                                         'servise yatırıldı.'},
                         {'text': 'Kan şekerini hızla 100 mg/dL seviyesine indirmek için yüksek doz intravenöz regüler '
                                  'insülin infüzyonu ve hipotonik sıvı başlayarak yoğun bakıma yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Asidozu olmayan stabil hastaya yüksek doz İV insülin ve hipotonik sıvı '
                                             'verilmesi ani glukoz düşüşüne ve serebral ödem riskine yol açtı.',
                          'teaching_point': 'Ketoasidozu olmayan stabil diyabet hastalarında intravenöz insülin '
                                            'infüzyonu veya yoğun bakım yatışı gerekmez; subkutan rejim tercih '
                                            'edilir.'},
                         {'text': 'Tip 1 diyabetli çocukta ilk basamak olarak oral antidiyabetik metformin başlamak ve '
                                  'beslenme önerileriyle hastayı acil servisten evine taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Mutlak insülin eksikliği bulunan çocukta oral antidiyabetik etkisiz '
                                             'kaldı ve hasta günler sonra ağır ketoasidoz tablosuyla tekrar başvurdu.',
                          'teaching_point': 'Çocukluk çağı tip 1 diyabetinde mutlak otoimmün beta hücresi kaybı '
                                            'vardır; oral antidiyabetikler etkisizdir ve tedavi mutlaka insülindir.'},
                         {'text': 'Hafif dehidratasyon nedeniyle 24 saat boyunca hastayı tamamen aç tutarak izotonik '
                                  'sıvı infüzyonu uygulamak ve insülin tedavisini poliklinik kontrolüne bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Aç bırakılan ve insülini başlanmayan çocukta lipoliz hızlanarak keton '
                                             'üretimi tetiklendi ve metabolik tablo asidoza doğru ilerledi.',
                          'teaching_point': 'Ketoasidozu olmayan çocuk NPO tutulmaz; beslenme ile senkronize subkutan '
                                            'insülin başlanarak anabolik süreç sağlanmalıdır.'}]}]},
 {'id': 'Y40',
  'category': '👶 Ağlayan, Emmeyen, Huzursuz Bebek',
  'age': '4 Aylık',
  'gender': 'Erkek',
  'complaint': 'Sağ kasık bölgesinde aniden beliren şişlik, gerginlik ve durdurulamayan ağlama',
  'history': "Annesi 4 aylık erkek bebeğini Yeşil Alana getiriyor: 'Oğlum yaklaşık 2 saat önce aniden çığlık atarak "
             'ağlamaya başladı. Ne yaptıysak susturamadık, emmek istemiyor ve bacaklarını sürekli karnına çekiyor. '
             'Bezini değiştirirken sağ kasığında, torbaya doğru inen ceviz büyüklüğünde sert ve gergin bir şişlik fark '
             "ettik. Daha önce burada hiç böyle bir kabarıklık görmemiştik, dokununca daha çok bağırıyor.'",
  'final_diagnosis': 'İnkarsere Sağ İnguinal Fıtık (Yeşil Alandan Sarı Alana Devir, Başarılı Taksis ve Çocuk Cerrahisi '
                     'Yatışı)',
  'disposition': 'Yeşil Alandan Sarı Alana Devir -> Analjezi/Sedasyon Altında Nazik Manuel Redüksiyon (Taksis) -> '
                 'Başarılı Redüksiyon Sonrası Erken Elektif Onarım İçin Çocuk Cerrahisi Yatışı',
  'case_pearl': 'Süt çocuklarında persistan processus vaginalis açıklığına bağlı inguinal herniasyonlar, dar dış '
                'inguinal halka nedeniyle hızla inkarserasyona (sıkışma ve dolaşım bozukluğu riski) ilerleyebilir. Sağ '
                'kasıkta gergin, ağrılı, redükte edilemeyen kitle saptanan huzursuz bebekler derhal Sarı Alana '
                'devredilmelidir. Peritonit veya ciltte nekroz/iskemi bulgusu yoksa, analjezi ve hafif sedasyon '
                'altında trendelenburg pozisyonunda nazik manuel redüksiyon (taksis) uygulanır; başarılı redüksiyon '
                'sonrası nüks ve doku hasarı riskini önlemek için Çocuk Cerrahisi servisine yatırılarak 24-48 saat '
                'içinde cerrahi onarım planlanır.',
  'steps': [{'stage_title': 'Yeşil Alanda Fizik Muayene ve Triyaj Değerlendirmesi',
             'question': 'Durdurulamayan ağlama ve sağ kasıkta şişlikle getirilen 4 aylık bu bebekte ilk basamak fizik '
                         'muayene ve alan kararınız ne olmalıdır?',
             'options': [{'text': 'Ağlamayı infantil koliğe bağlayarak Yeşil Alanda oral simetikon damla vermek ve '
                                  'anneyi emzirme teknikleri konusunda bilgilendirerek evine taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Kasık muayenesi yapılmadan infantil kolik kabul edilen bebekte organ '
                                             'dolaşım bozukluğu ve iskemi riski taşıyan patoloji atlandı.',
                          'teaching_point': 'Ani başlayan huzursuzluk ve ağlama nöbeti olan her bebekte alt bezi '
                                            'tamamen açılarak inguinal ve genital bölgeler mutlaka muayene '
                                            'edilmelidir.'},
                         {'text': 'Kasık ve skrotumu palpasyonla inceleyip redükte edilemeyen gergin kitleyi '
                                  'değerlendirerek acil cerrahi risk nedeniyle bebeği Sarı Alana devretmek',
                          'is_correct': True,
                          'triggers_yellow_transfer': True,
                          'explanation': 'Kasık bölgesinde ağrılı, sert ve redükte edilemeyen kitle varlığı sıkışmış '
                                         'organ ansı ve dolaşım bozukluğu riski taşır; acil müdahale ve analjezi için '
                                         'bebek Sarı Alana alınmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 37.1°C, KTA 155/dk (ağlamaya sekonder taşikardik), '
                                         'Solunum 38/dk, SpO2 %99. Bebek ajite ve durdurulamayan ağlama nöbetinde. '
                                         'Genitoüriner muayenede sağ kasıktan hemiskrotuma uzanan yaklaşık 3x2 cm '
                                         'boyutlarında, palpasyonla son derece hassas, gergin, kendiliğinden '
                                         'gerilemeyen kitle saptandı. Kitle üzerindeki cilt rengi ve ısısı doğal; her '
                                         'iki testis skrotum tabanında palpe edildi. Sol kasık doğal. Bebek derhal '
                                         'Sarı Alana devredildi!'},
                         {'text': 'Sağ kasıktaki şişliği reaktif lenfadenit kabul ederek Yeşil Alanda intramüsküler '
                                  'ampisilin uygulamak ve ertesi gün Çocuk Cerrahisi polikliniğine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Akut organ sıkışması tablosuna antibiyotik verilerek bebek evine '
                                             'gönderildi ve saatler içinde kitlede dolaşım bozukluğu derinleşti.',
                          'teaching_point': 'Kasıktan skrotuma uzanan ani gelişmiş gergin ve ağrılı kitleler '
                                            'lenfadenit değildir; acil redüksiyon veya cerrahi değerlendirme '
                                            'gerektirir.'},
                         {'text': 'Kitleye hiçbir analjezi veya sedasyon uygulamadan Yeşil Alanda iki elle var gücüyle '
                                  'bastırarak zorlu kompresyonla kitleyi batına itmeye çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Analjezisiz ve kontrolsüz uygulanan aşırı kuvvetli bası bebekte şiddetli '
                                             'ağrı travmasına, hematoma ve bağırsak perforasyonu riskine yol açtı.',
                          'teaching_point': 'Ağlayan ve ıkınan bebekte zorlayıcı manevralar kontrendikedir; redüksiyon '
                                            'mutlaka analjezi/sedasyon altında nazikçe ve kontrollü uygulanmalıdır.'}]},
            {'stage_title': 'Sarı Alanda İlk Girişim ve Manuel Redüksiyon Kararı',
             'question': 'Sarı Alana alınan, kasık derisinde kızarıklık veya sistemik peritonit bulgusu olmayan bu '
                         'bebekte ilk aşamada ne yapılmalıdır?',
             'options': [{'text': 'Manuel redüksiyonu denemeden önce acil tüm batın bilgisayarlı tomografisi çekerek '
                                  'bağırsak anslarının lümen genişliğini ve duvar kalınlığını incelemek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz radyolojik tetkiklerle geçen süre boyunca kitle içindeki '
                                             'dokuların dolaşımı daha da bozuldu ve cerrahi aciliyet arttı.',
                          'teaching_point': 'Peritonit veya doku nekrozu bulgusu olmayan sıkışmış kasık kitlelerinde '
                                            'ilk basamak radyolojik incelemelerle vakit kaybetmeden analjezi altında '
                                            'nazik redüksiyondur.'},
                         {'text': 'Hiçbir manuel redüksiyon manevrası denemeden bebeği derhal genel anesteziye alarak '
                                  'ameliyathanede acil laparotomi ile cerrahi eksplorasyon planlamak',
                          'is_correct': False,
                          'scenario_update': 'Nazik taksis manevrasıyla dakikalar içinde ameliyatsız redükte '
                                             'edilebilecek olguda acil şartlarda yüksek anestezi ve operasyon '
                                             'komplikasyonları gelişti.',
                          'teaching_point': 'Peritonit veya ciltte morarma/gangren olmayan vakalarda ilk basamak '
                                            'analjezi altında nazik manuel redüksiyondur; başarılı olursa cerrahi '
                                            'elektif şartlara çekilir.'},
                         {'text': 'Bebeğe intravenöz analjezi ve hafif sedasyon sağlamak, Trendelenburg pozisyonunda '
                                  'ılık kompres uygulayıp nazik manuel redüksiyon manevrası denemek',
                          'is_correct': True,
                          'explanation': 'Ciltte renk değişikliği veya peritonit olmayan sıkışmış kasık kitlelerinde '
                                         'ilk yaklaşım analjezi/sedasyon, Trendelenburg pozisyonu ve nazik manuel '
                                         'redüksiyondur (taksis).',
                          'new_finding': 'İntravenöz analjezi (fentanil) sağlandı. Bebek gevşeyip Trendelenburg '
                                         'pozisyonuna alındıktan ve ılık kompres uygulandıktan sonra, eksternal halka '
                                         'tabanından uygulanan nazik taksis manevrasıyla kitle hava-sıvı gurultusu '
                                         'eşliğinde batına tamamen redükte oldu. Bebeğin ağlaması durdu, vitalleri '
                                         'rahatladı (KTA 115/dk).'},
                         {'text': 'Ağrıyı kesmek amacıyla kitlenin tam merkezine doğrudan lokal lidokain enjeksiyonu '
                                  'yapmak ve ardından enjektörle kitleden sıvı aspire etmeye çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Kitle içine körlemesine yapılan iğne aspirasyonu bağırsak duvarında '
                                             'delinmeye ve skrotal alana fekal kontaminasyona yol açtı.',
                          'teaching_point': 'İçinde bağırsak ansları bulunan kasık kitlelerine asla körlemesine iğne '
                                            'aspirasyonu veya lokal anestezik enjeksiyonu yapılmaz; perforasyon riski '
                                            'yaratır.'}]},
            {'stage_title': 'Sarı Alanda Kesin Tanı',
             'question': 'Kasıktan skrotuma uzanan gergin kitle, taksis manevrasıyla redükte olan barsak ansı ve '
                         'klinik tabloyla kesin tanınız nedir?',
             'options': [{'text': 'İnkarsere Sağ İnguinal Fıtık',
                          'is_correct': True,
                          'explanation': 'Persistan processus vaginalis açıklığından skrotuma inen, dış halkada '
                                         'sıkışarak huzursuzluk ve gerginlik yaratan, taksis ile batına redükte olan '
                                         'patoloji inkarsere inguinal fıtıktır.',
                          'new_finding': 'Kesin Tanı: İnkarsere Sağ İnguinal Fıtık.'},
                         {'text': 'Akut Testis Torsiyonu',
                          'is_correct': False,
                          'scenario_update': 'Testis torsiyonunda kitle inguinal kanaldan inen redükte edilebilir bir '
                                             'doku değildir; skrotumda yatay yerleşimli, aşırı ağrılı ve ödemli tek '
                                             'testis izlenir.',
                          'teaching_point': 'Testis torsiyonunda testis yukarı çekilmiştir ve kremaster refleksi '
                                            'negatiftir; kasıktan hava-sıvı sesiyle batına redüksiyon görülmez.'},
                         {'text': 'Akut İdiyopatik Skrotal Ödem',
                          'is_correct': False,
                          'scenario_update': 'İdiyopatik skrotal ödemde skrotum cildinde iki taraflı ağrısız eritem ve '
                                             'ödem vardır; inguinal kanalda sıkışmış kitle saptanmaz.',
                          'teaching_point': 'İdiyopatik skrotal ödem benign, ağrısız, kendiliğinden gerileyen bir cilt '
                                            'ödemidir; palpabl kasık kitlesi yapmaz.'},
                         {'text': 'İnflame Kominikan Hidrosel',
                          'is_correct': False,
                          'scenario_update': 'Hidrosel translüminasyon veren, gergin olmayan, ağrısız sıvı '
                                             'koleksiyonudur; akut sıkışma, aşırı huzursuzluk ve hava-sıvı sesiyle '
                                             'redüksiyon oluşturmaz.',
                          'teaching_point': 'Kominikan hidroselde periton sıvısı skrotuma geçiş gösterir ancak barsak '
                                            'ansları içermediğinden akut inkarserasyon tablosu yaratmaz.'}]},
            {'stage_title': 'Sarı Alanda Tedavi ve Cerrahi İzlem Planı',
             'question': 'Taksis ile başarıyla redükte edilen, ancak nüks ve doku hasarı riski yüksek olan bu bebeğin '
                         'ileri yönetimi nasıl olmalıdır?',
             'options': [{'text': 'Kitle tamamen redükte olduğu için bebeği acil servisten taburcu etmek ve nüks '
                                  'olursa tekrar getirmeleri tembihiyle hiçbir kontrole çağırmamak',
                          'is_correct': False,
                          'scenario_update': 'Eve gönderilen bebekte saatler sonra fıtık tekrar inkarsere oldu ve aile '
                                             'geç başvurduğu için bağırsak gangreni gelişti.',
                          'teaching_point': 'İnkarserasyon geçiren bebeklerde ilk 24-48 saatte tekrar sıkışma riski '
                                            'çok yüksektir; redüksiyon sonrası hasta mutlaka Çocuk Cerrahisi servisine '
                                            'yatırılmalıdır.'},
                         {'text': 'Redüksiyon sonrası bebeği altı ay boyunca inguinal fıtık bağı kullanarak '
                                  'ameliyatsız izlemek üzere ortopedi polikliniğine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Bebeklerde fıtık bağı kullanımı hiçbir anatomik iyileşme sağlamadı; '
                                             'basıya bağlı testis atrofisi ve deri nekrozu gelişti.',
                          'teaching_point': 'Çocukluk çağı inguinal hernilerinde fıtık bağı veya korse kullanımı '
                                            'kesinlikle kontrendikedir; definitif tedavi cerrahi yüksek ligasyondur.'},
                         {'text': 'Redüksiyonun tam başarısını teyit etmek amacıyla bebeğe oral baryum kontrastı '
                                  'içirerek acil floroskopik inceleme yapmak ve taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Yeni redükte olmuş ödemli bağırsak dokusuna verilen baryum aspirasyon '
                                             'riski yarattı ve olası cerrahi öncesi ek risk oluşturdu.',
                          'teaching_point': 'Başarılı taksis sonrası floroskopik kontrastlı inceleme gerekmez; '
                                            'hastanın klinik takibi, beslenme toleransı ve testis muayenesi esastır.'},
                         {'text': 'Bebeği acilden taburcu etmeyip barsak ve testis dolaşımını izlemek, erken elektif '
                                  'operasyon için Çocuk Cerrahisi servisine yatırmak',
                          'is_correct': True,
                          'explanation': 'İnkarserasyon öyküsü olan infantlarda tekrar inkarserasyon riski çok '
                                         'yüksektir. Başarılı redüksiyon sonrası ödemin gerilemesi için hasta '
                                         'yatırılır, 24-48 saat içinde Çocuk Cerrahisi tarafından elektif herniotomi '
                                         '(yüksek ligasyon) operasyonu planlanır.',
                          'new_finding': 'Çocuk Cerrahisi konsültasyonu sonrası hasta, peritonit ve testis iskemi '
                                         'takibi yapılmak ve 24-48 saat içinde elektif cerrahi uygulanmak üzere '
                                         'servise yatırıldı.'}]}]}]
