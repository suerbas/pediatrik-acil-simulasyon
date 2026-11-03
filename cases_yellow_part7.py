# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Sarı Alan Vakaları (Bölüm 7: Y61 - Y70)
"""

YELLOW_CASES_PART7 = [{'id': 'Y61',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '3 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Altı gündür düşmeyen 39.5°C ateş, gözlerde kanlanma, çilek dili, dudaklarda çatlak ve boyunda şişlik',
  'history': "Üç yaşındaki erkek çocuk ailesi tarafından Sarı Alana getiriliyor: 'Altı gündür ateşi 39.5°C'ye kadar "
             "çıkıyor, parasetamol ve ibuprofen ile ancak 38.5°C'ye düşüyor. Üç gün önce acilde farenjit denilerek "
             'oral sefalosporin başlandı fakat ateşi hiç gerilemedi. Gözlerinin akı kıpkırmızı oldu ancak hiç sarı '
             'çapak ya da akıntı akmıyor. Dudakları kuruyup yarıldı, dili kıpkırmızı kabardı, ellerinin ve ayaklarının '
             'üstü gerginleşip şişti. Sol boynunda ceviz büyüklüğünde bir şişlik fark ettik. Çocuk son derece '
             "huzursuz, sürekli ağlıyor.'",
  'final_diagnosis': 'Kawasaki Hastalığı (Tipik Mukokutanöz Lenf Nodu Sendromu / Akut Sistemik Vaskülit)',
  'disposition': 'Sarı Alanda Acil Ekokardiyografi, Tek Doz İVİG (2 g/kg) ve Yüksek Doz Oral Aspirin Tedavisi ile '
                 'Çocuk Kardiyoloji Yatışı',
  'case_pearl': 'Kawasaki hastalığı çocukluk çağının en sık edinsel kalp hastalığı nedenidir ve küçük/orta çaplı '
                'arterlerin (özellikle KORONER ARTERLERİN) vaskülitidir. TANI KRİTERLERİ: En az 5 GÜN SÜREN ATEŞ + '
                "Aşağıdaki 5 kriterden en az 4'ü: 1) Bilateral eksüdasız (non-pürülan) konjonktival enjeksiyon, 2) "
                'Oral mukoza değişiklikleri (çilek dili, dudaklarda kuruma/çatlama, orofarengeal eritem), 3) Periferik '
                'ekstremite değişiklikleri (akut evrede el ve ayaklarda sert eritematöz ödem; konvalesan evrede tırnak '
                'dibinden soyulma), 4) Polimorfik döküntü (vezikülsüz makülopapüler döküntü), 5) Servikal '
                'lenfadenopati (genellikle tek taraflı, ağrısız, >1.5 cm). TEDAVİ: Tanı konur konmaz (özellikle ilk 10 '
                'gün içinde) KORONER ARTER ANEVRİZMASINI ÖNLEMEK İÇİN TEK DOZ İNTRAVENÖZ İMMÜNOGLOBULİN (İVİG - 2 '
                'g/kg, 10-12 saatte) + YÜKSEK DOZ ASPİRİN (30-50 mg/kg/gün antiinflamatuar doz) başlanmalıdır. Ateş '
                'düştükten 48 saat sonra aspirin dozu antitrombositer doza (3-5 mg/kg/gün) indirilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Altı gündür inatçı yüksek ateşi ve mukozal bulguları olan bu çocukta fizik muayenede '
                         'öncelikle nelere bakmalısınız?',
             'options': [{'text': 'Vital bulguları, konjonktivaları, oral kaviteyi, servikal lenf nodunu ve ekstremite '
                                  'ödemini tam muayeneyle değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Sistemik vaskülit kriterlerini (eksüdasız konjonktivit, çilek dili, çatlak '
                                         'dudaklar, tek taraflı servikal LAP ve el-ayak dorsalinde endürasyonlu sert '
                                         'ödem) doğrulamak ve hemodinamiyi incelemek ilk hedeftir.',
                          'new_finding': 'Vital Bulgular: Ateş 39.4°C, KTA 142/dk, SS 28/dk, SpO2 %98, TA 94/58 mmHg, '
                                         'KDZ 2 sn. Fizik Muayene: Bilateral non-pürülan konjonktival enjeksiyon '
                                         "mevcut. Dudaklar kuru, çatlak ve kanamalı; dil parlak kırmızı 'çilek dili' "
                                         'görünümünde. Sol servikal zincirde 2x2 cm boyutunda tek, hassas lenf nodu '
                                         'palpe ediliyor. Gövdede polimorfik eritematöz döküntü var. Her iki el ve '
                                         'ayak sırtında gode bırakmayan sert eritematöz ödem mevcut. BCG aşı skarı '
                                         'çevresinde belirgin eritem izlendi.'},
                         {'text': 'Sadece kulak zarı muayenesi yapıp diğer sistemik organ bulgularını ve vaskülit '
                                  'ipuçlarını tamamen göz ardı etmek',
                          'is_correct': False,
                          'scenario_update': 'Gözden kaçan sistemik bulgular nedeniyle koroner arter tutulumu riski '
                                             'kritik seviyeye ulaştı.',
                          'teaching_point': 'Uzamış ateşi olan çocukta mukozalar, lenf nodları ve ekstremiteler '
                                            'eksiksiz taranmalıdır.'},
                         {'text': 'Ateşin tek nedeninin diş çıkarma olduğunu varsayıp çocuğu muayene etmeden karanlık '
                                  'odada sakinleştirmeye çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Tanıda gecikme vaskülitin koroner anevrizmaya ilerlemesine yol açtı.',
                          'teaching_point': '39°C üzeri inatçı ateş ve belirgin lenfadenopati asla fizyolojik diş '
                                            'çıkarma ile açıklanamaz.'},
                         {'text': 'Hastaya acil lomber ponksiyon uygulayarak intrakraniyal basınç artışı araştırmasını '
                                  'ilk ve tek hedef yapmak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz invaziv girişim aşırı ajitasyona ve hemodinamik bozulmaya sebep '
                                             'oldu.',
                          'teaching_point': 'Meningeal irritasyon bulgusu olmayan vaskülit şüpheli hastada öncelik '
                                            'klinik kriterleri toplamaktır.'}]},
            {'stage_title': 'Laboratuvar İncelemeleri ve Ekokardiyografi',
             'question': 'Vaskülit kriterlerini dolduran bu hastada tanıyı desteklemek ve komplikasyonları ekarte '
                         'etmek için hangi tetkikler istenmelidir?',
             'options': [{'text': 'Tam kan sayımı, sedimentasyon, C-reaktif protein, karaciğer enzimleri, albümin, '
                                  'idrar tetkiki ve acil ekokardiyografi istemek',
                          'is_correct': True,
                          'explanation': 'Vaskülitte belirgin sistemik inflamasyon (lökositoz, trombositoz, aşırı '
                                         'yüksek ESH/CRP), hipoalbüminemi, transaminaz yüksekliği ve steril piyüri '
                                         'tipiktir. En kritik adım koroner arter çaplarını ve miyokarditi '
                                         'değerlendirmek için transtorasik ekokardiyografidir.',
                          'new_finding': 'Hemogram: Lökosit 18.400/mm³ (%78 nötrofil), Hemoglobin 10.2 g/dL, Trombosit '
                                         '485.000/mm³. CRP: 142 mg/L (çok yüksek), ESH: 88 mm/saat. Biyokimya: AST 64 '
                                         'U/L, ALT 72 U/L, Albümin 2.8 g/dL (hipoalbüminemi). Tam İdrar Tetkiki: '
                                         'Steril piyüri (15-20 lökosit/saha, bakteri yok). Ekokardiyografi: Sol ön '
                                         'inen (LAD) ve sağ koroner arterde (RCA) dilatasyon ve perivasküler parlaklık '
                                         'izlendi, anevrizma henüz gelişmemiş, EF %62.'},
                         {'text': 'Sadece dışkıda gizli kan ve parazit mikroskopisi isteyerek kardiyovasküler ve '
                                  'inflamatuar tetkikleri tamamen ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Koroner arter dilatasyonu tespit edilemedi ve miyokardiyal iskemi '
                                             'tehlikesi arttı.',
                          'teaching_point': 'Uzamış ateş ve klinik mukoza bulgularında ekokardiyografi ve akut faz '
                                            'reaktanları hayatidir.'},
                         {'text': 'Akciğer tomografisi ve bronkoskopi planlayarak hastanın kan tahlillerini ve kalp '
                                  'ultrasonunu tamamen dışlamak',
                          'is_correct': False,
                          'scenario_update': 'Radyasyon maruziyeti ve anestezi riski hastanın tablosunu daha da '
                                             'ağırlaştırdı.',
                          'teaching_point': 'Solunum sıkıntısı olmayan vaskülit olgusunda invaziv hava yolu '
                                            'tetkiklerinin yeri yoktur.'},
                         {'text': 'Hastadan sadece ter testi ve genetik kistik fibrozis paneli göndererek saatlerce '
                                  'klinik gözlem yapmadan beklemek',
                          'is_correct': False,
                          'scenario_update': 'Akut vaskülit atağında saatler kaybedildi ve koroner hasar riski büyüdü.',
                          'teaching_point': 'Akut sistemik inflamatuar tablolarda öncelik vaskülit paneli ve koroner '
                                            'görüntülemedir.'}]},
            {'stage_title': 'Ayırıcı Tanı ve Nihai Tanının Belirlenmesi',
             'question': 'Altı gündür süren ateş, non-pürülan konjonktivit, çilek dili, ekstremite ödemi, servikal LAP '
                         've yüksek CRP birlikteliğinde kesin tanı nedir?',
             'options': [{'text': 'Tipik Kawasaki Hastalığı Akut Vasküliti',
                          'is_correct': True,
                          'explanation': '5 gün üzeri ateş + 4 tanı kriteri (konjonktivit, oral mukoza, servikal LAP, '
                                         'ekstremite ödemi, döküntü) ve koroner dilatasyon tipik Kawasaki hastalığı '
                                         'tanısını kesinleştirir.',
                          'new_finding': 'Kesin Tanı: Tipik Kawasaki Hastalığı (Akut Sistemik Vaskülit) '
                                         'doğrulanmıştır. Hastaya ve ailesine durum açıklanarak Sarı Alan acil tedavi '
                                         'protokolüne geçildi.'},
                         {'text': 'Kızıl Toksik Streptokok Farenjiti',
                          'is_correct': False,
                          'scenario_update': 'Sefalosporine yanıtsızlık ve ekokardiyografideki koroner genişleme basit '
                                             'streptokok farenjiti ile uyumsuzdur.',
                          'teaching_point': 'Kızılda konjonktivit ve ekstremitelerde sert endürasyonlu ödem görülmez.'},
                         {'text': 'Akut Ebstein-Barr Virüs Enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'EBV enfeksiyonunda bilateral eksüdasız konjonktivit ve koroner arter '
                                             'dilatasyonu beklenmez.',
                          'teaching_point': 'İnfeksiyöz mononükleozda yaygın LAP ve tonsillitte eksüda ön plandadır.'},
                         {'text': 'Stevens-Johnson İlaç Reaksiyonu Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Stevens-Johnson sendromunda büllöz epidermoliz ve mukoza nekrozu '
                                             'görülür.',
                          'teaching_point': 'Kawasaki hastalığında bül ve nekroz olmaz, polimorfik vezikülsüz döküntü '
                                            'vardır.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Tanısı kesinleşen ve koroner dilatasyonu saptanan 3 yaşındaki bu hastada Sarı Alanda derhal '
                         'başlanması gereken tedavi nedir?',
             'options': [{'text': 'Tek doz intravenöz immünoglobulin ve yüksek doz oral aspirin başlanarak çocuk '
                                  'kardiyoloji servisine yatırmak',
                          'is_correct': True,
                          'explanation': 'Kawasaki hastalığında ilk 10 gün içinde verilen İVİG (2 g/kg, 10-12 saatte '
                                         "infüzyon) koroner arter anevrizması gelişme riskini %25'ten %3-5'in altına "
                                         'düşürür. Eş zamanlı yüksek doz aspirin (30-50 mg/kg/gün) antiinflamatuar '
                                         'amaçla verilir.',
                          'new_finding': 'Damar yolu kontrol edildi, İVİG (2 g/kg) infüzyonu 12 saatte gidecek şekilde '
                                         'başlatıldı. Oral Aspirin (40 mg/kg/gün, 4 doza bölünerek) verildi. Çocuk '
                                         'kardiyoloji ve pediatri servisine yatışı yapıldı. İnfüzyonun 8. saatinde '
                                         "ateş 37.1°C'ye geriledi, konjonktival enjeksiyon ve huzursuzluk belirgin "
                                         'azaldı.'},
                         {'text': 'Sadece oral parasetamol şurubu vererek hastayı taburcu edip bir hafta sonra '
                                  'polikliniğe kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'İVİG verilmemesi dev koroner anevrizma ve akut miyokard enfarktüsü '
                                             'gelişimini tetikledi.',
                          'teaching_point': 'Kawasaki hastalığı koroner anevrizmayı önlemek için acil İVİG gerektiren '
                                            'bir tablodur.'},
                         {'text': 'Geniş spektrumlu oral florokinolon antibiyotik başlayıp kardiyak izlem yapmadan '
                                  'evde izlem önermek',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik vasküliti durduramadı; koroner arter rüptürü riski kritik '
                                             'aşamaya ulaştı.',
                          'teaching_point': 'Kawasaki enfeksiyon değil vaskülittir; antibiyotikler etkisizdir, İVİG '
                                            'esastır.'},
                         {'text': 'Ateşi düşürmek amacıyla hastaya intramüsküler yüksek doz penisilin enjeksiyonu '
                                  'yapıp göndermek',
                          'is_correct': False,
                          'scenario_update': 'Aspirin ve İVİG verilmediği için koroner arter çapları 8 mm üzerine '
                                             'çıkarak anevrizma oluştu.',
                          'teaching_point': 'Penisilinin Kawasaki patogenezinde ve koronerlerin korunmasında hiçbir '
                                            'yeri yoktur.'}]}]},
 {'id': 'Y62',
  'category': '🦴 Kas-İskelet & Eklem / Ortopedik Aciller',
  'age': '2 Yaşında',
  'gender': 'Kız',
  'complaint': 'Sağ dizde aşırı şişlik, kızarıklık, sıcaklık, 39.2°C ateş ve bacağına hiç basamama',
  'history': "İki yaşındaki kız çocuk ailesi tarafından kucakta Sarı Alana getiriliyor: 'Dün sabah hafif bir "
             'topallaması vardı. Ancak dün geceden itibaren sağ dizi belirgin şekilde şişti, kıpkırmızı oldu ve '
             "dokununca alev gibi yanıyor. Ateşi 39.2°C'ye çıktı. Sağ bacağını hafifçe bükük tutuyor, kesinlikle yere "
             'basmıyor, bacağına dokunmamıza bile izin vermiyor, çığlık atarak ağlıyor. Üç gün önce dizini halıya '
             "sürtüp hafifçe sıyırmıştı. Travma veya düşme öyküsü yok.'",
  'final_diagnosis': 'Septik Artrit (Akut Bakteriyel Eklem Enfeksiyonu / Staphylococcus aureus İlişkili Sağ Diz '
                     'Artriti)',
  'disposition': 'Sarı Alanda Acil Ortopedi Konsültasyonu ile Eklem Aspirasyonu / Drenajı, İV Antistafilokokal '
                 'Antibiyotik ve Yatış',
  'case_pearl': 'Pediatrik septik artrit kıkırdak yıkımını ve kalıcı eklem harabiyetini önlemek için ACİL DRENAJ '
                "gerektiren bir ortopedik acildir. En sık etken her yaş grubunda STAPHYLOCOCCUS AUREUS'tur (MRSA riski "
                'akılda tutulmalıdır; <2-3 yaşta Kingella kingae de önemli). KLİNİK: Akut başlangıçlı yüksek ateş, '
                'eklemde belirgin efüzyon, kızarıklık, lokal ısı artışı, psödoparalizi (eklemi hiç hareket ettirememe) '
                've hareketle şiddetli ağrı. KOC-HER KRİTERLERİ (özellikle kalça için geliştirilmiş olsa da eklem '
                'enfeksiyonunda kılavuzdur): 1) Ateş >38.5°C, 2) Ağırlık verememe, 3) ESH >40 mm/saat, 4) Lökosit '
                '>12.000/mm³. TANI VE YÖNETİM: Tanının altın standardı steril koşullarda ACİL DİAGNOSTİK VE TERAPÖTİK '
                'EKLEM ASPİRASYONUDUR. Sinoviyal sıvıda lökosit >50.000/mm³ (%75 üzeri nötrofil), gram boyama ve '
                'kültür septik artriti kanıtlar. Aspirasyon/drenaj sonrası vakit kaybetmeden İNTRAVENÖZ '
                'ANTİSTAFİLOKOKAL ANTİBİYOTİK (Sefazolin veya MRSA şüphesinde Vankomisin) başlanmalıdır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Tek eklemde akut şişlik, ısı artışı ve yüksek ateşi olan bu çocukta fizik muayenede öncelik '
                         'ne olmalıdır?',
             'options': [{'text': 'Vital bulguları, sağ dizdeki efüzyonu, lokal ısı artışını, aktif ve pasif eklem '
                                  'hareket açıklığını değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Enfeksiyöz monoartrit bulgularını (lokal ısı artışı, eritem, fluktuasyon '
                                         'veren efüzyon, psödoparalizi) ve sistemik toksisiteyi saptamak için tam '
                                         'eklem ve ekstremite muayenesi esastır.',
                          'new_finding': 'Vital Bulgular: Ateş 39.1°C, KTA 138/dk, SS 26/dk, SpO2 %99, TA 96/60 mmHg, '
                                         'KDZ 2 sn. Fizik Muayene: Sağ diz 30 derece fleksiyonda kilitli tutuluyor. '
                                         'Diz ekleminde belirgin şişlik, patellar ballotman pozitifliği, kızarıklık ve '
                                         'ileri derecede lokal ısı artışı mevcut. En ufak pasif ekstansiyon veya '
                                         'fleksiyonda çocuk çığlık atarak ağlıyor. Sağ bacağına kesinlikle ağırlık '
                                         'veremiyor. Sol diz ve diğer tüm eklemler tamamen doğal.'},
                         {'text': 'Sadece her iki kulak zarını inceleyip eklemi hiç muayene etmeden çocuğun ayağa '
                                  'kalkmasını emretmek',
                          'is_correct': False,
                          'scenario_update': 'Ağrıdan kıvranan çocuğa zorla basma yaptırılması eklem kıkırdağına '
                                             'mekanik travma verdi.',
                          'teaching_point': 'Akut enfekte ekleme asla zorla ağırlık verdirilmemeli, nazik eklem '
                                            'muayenesi yapılmalıdır.'},
                         {'text': 'Çocuğun şikayetini büyüme ağrısı sayarak muayenesiz şekilde masaj yapıp hemen evine '
                                  'göndermek',
                          'is_correct': False,
                          'scenario_update': 'Tedavisiz kalan bakteriyel artrit eklem kıkırdağında geri dönüşsüz '
                                             'erimeye yol açtı.',
                          'teaching_point': 'Ateş, kızarıklık ve tek taraflı eklem şişliği asla büyüme ağrısı olamaz; '
                                            'acil patolojidir.'},
                         {'text': 'Acil cerrahi apandisit şüphesiyle batın muayenesine odaklanıp dizdeki kızarıklığı '
                                  'böcek ısırığı saymak',
                          'is_correct': False,
                          'scenario_update': 'Eklem enfeksiyonu odağı atlandı ve sistemik bakteriyemiye zemin '
                                             'hazırlandı.',
                          'teaching_point': 'Lokalize ısı artışı ve efüzyon olan eklem doğrudan primer enfeksiyon '
                                            'odağı olarak ele alınmalıdır.'}]},
            {'stage_title': 'Laboratuvar İncelemeleri ve Eklem Ultrasonografisi',
             'question': 'Monoartrit ve yüksek ateş tablosunda Sarı Alanda tanıyı doğrulamak için hangi incelemeler '
                         'derhal yapılmalıdır?',
             'options': [{'text': 'Tam kan sayımı, sedimentasyon, C-reaktif protein, kan kültürü, sağ diz grafisi ve '
                                  'eklem ultrasonografisi istemek',
                          'is_correct': True,
                          'explanation': 'İnflamatuar belirteçler (lökositoz, yüksek ESH ve CRP) bakteriyel '
                                         'enfeksiyonu destekler. Radyografi osteomiyelit veya fraktürü dışlarken, '
                                         'eklem ultrasonografisi eklem içi sıvı koleksiyonunu kanıtlar ve aspirasyona '
                                         'kılavuzluk eder.',
                          'new_finding': 'Hemogram: Lökosit 19.800/mm³ (%84 nötrofil, sola kayma), Hemoglobin 11.0 '
                                         'g/dL, Trombosit 390.000/mm³. CRP: 112 mg/L (aşırı yüksek), ESH: 74 mm/saat. '
                                         'Kan kültürü alındı. Sağ Diz Grafisi: Kemik korteksi sağlam, fraktür yok, '
                                         'suprapatellar yumuşak doku planında belirgin şişlik ve eklem mesafesinde '
                                         'genişleme. Sağ Diz USG: Suprapatellar bursada ve eklem içi mesafede yoğun '
                                         'ekojenik partiküller içeren masif pürülan sıvı koleksiyonu izlendi.'},
                         {'text': 'Sadece idrar tahlili ve dışkı mikroskopisi isteyerek eklem ultrasonunu ve kan '
                                  'testlerini tamamen ihmal etmek',
                          'is_correct': False,
                          'scenario_update': 'Eklemdeki pürülan efüzyon görüntülenemediği için drenaj kararı gecikti.',
                          'teaching_point': "Septik monoartritte eklem USG'si sıvı varlığını ve derinliğini göstermede "
                                            'ilk tercihtir.'},
                         {'text': 'Hastadan sadece ter testi ve kistik fibrozis mutasyon analizi isteyerek ortopedik '
                                  'tetkikleri ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz testlerle kaybedilen saatler kıkırdak nekrozunu hızlandırdı.',
                          'teaching_point': 'Akut pürülan monoartritte hedef eklem sıvısının gösterilmesi ve acil '
                                            'boşaltılmasıdır.'},
                         {'text': 'Tüm vücut kemik sintigrafisi randevusu alarak çocuğu tahlilsiz ve tedavisiz üç gün '
                                  'bekletmek',
                          'is_correct': False,
                          'scenario_update': 'Eklem içi proteolitik enzimler eklem yüzeyini tamamen tahrip etti.',
                          'teaching_point': 'Bakteriyel artrit saatler içinde kıkırdak erimesi yapabilen acil bir '
                                            'klinik tablodur.'}]},
            {'stage_title': 'Ayırıcı Tanı ve Nihai Tanının Belirlenmesi',
             'question': 'Ateş 39.1°C, lökositoz, CRP 112 mg/L, dizde yoğun partiküllü efüzyon ve psödoparalizi hangi '
                         'klinik tanıyı kesinleştirir?',
             'options': [{'text': 'Akut Bakteriyel Septik Artrit Tablosu',
                          'is_correct': True,
                          'explanation': 'Ateş >38.5°C, ağırlık verememe, lökositoz, yüksek CRP ve ultrasonografik '
                                         'pürülan efüzyon akut bakteriyel septik monoartriti kesin olarak kanıtlar.',
                          'new_finding': 'Kesin Tanı: Akut Bakteriyel Septik Artrit (Sağ Diz) doğrulanmıştır. Hastaya '
                                         've ailesine durum açıklanarak Sarı Alan acil tedavi protokolüne geçildi.'},
                         {'text': 'Geçici Toksik Kalça Sinoviti',
                          'is_correct': False,
                          'scenario_update': 'Toksik sinovitte dizde eritem ve pürülan sıvı olmaz, CRP ve ateş bu '
                                             'denli yüksek seyretmez.',
                          'teaching_point': 'Toksik sinovit hafif seyreder ve kalça ekleminde sınırlıdır, dizde septik '
                                            'tablo yapmaz.'},
                         {'text': 'Osgood-Schlatter Traksiyon Apofiziti',
                          'is_correct': False,
                          'scenario_update': 'Osgood-Schlatter ergen sporcularda görülür; yüksek ateş ve masif eklem '
                                             'efüzyonu yapmaz.',
                          'teaching_point': 'Apofizit mekanik traksiyon hastalığıdır, sistemik enfeksiyon bulguları '
                                            'içermez.'},
                         {'text': 'Hafif Diz Eklem Burkulması',
                          'is_correct': False,
                          'scenario_update': 'Basit burkulmada 39°C üzeri ateş, lökositoz ve yoğun ekojenik eklem '
                                             'sıvısı görülmez.',
                          'teaching_point': 'Enfeksiyon kriterleri pozitifken travma tanısına sığınmak felaketle '
                                            'sonuçlanabilir.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Septik artrit tanısı kesinleşen bu hastada kıkırdak nekrozunu önlemek için Sarı Alandaki en '
                         'kritik yönetim adımı nedir?',
             'options': [{'text': 'Acil ortopedi konsültasyonu ile eklem aspirasyonu ve lavajı yapmak, ardından '
                                  'intravenöz antibiyotik başlayıp yatırmak',
                          'is_correct': True,
                          'explanation': 'Bakteriyel enzimlerin kıkırdağı eritmesini durdurmak için eklem sıvısının '
                                         'acilen boşaltılması (aspirasyon veya artrotomi) şarttır. Sinoviyal sıvı '
                                         'örneği mikrobiyolojiye gönderildikten hemen sonra İV sefazolin (veya '
                                         'vankomisin) başlanır.',
                          'new_finding': 'Ortopedi ekibi Sarı Alana çağrıldı. Steril şartlarda sağ dizden eklem '
                                         'aspirasyonu (artrosentez) yapıldı; 18 mL bulanık, pürülan (sarı-yeşil) sıvı '
                                         'aspire edildi. Sinoviyal Sıvı Analizi: Lökosit 92.000/mm³ (%88 parçalı '
                                         'lökosit). Gram boyamada Gram pozitif kok kümeleri (Stafilokok ile uyumlu) '
                                         'izlendi. Damar yolundan İV Sefazolin (100 mg/kg/gün) ve Vankomisin başlandı. '
                                         'Hasta acil artroskopik lavaj ve drenaj amacıyla ortopedi servisine '
                                         'devredildi.'},
                         {'text': 'Ekleme hiçbir girişim yapmadan hastaya sadece oral ibuprofen şurup verip evde '
                                  'bacağını dinlendirmesini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Basınç altındaki pürülan sıvı 24 saat içinde eklem kıkırdağını kalıcı '
                                             'olarak yıktı.',
                          'teaching_point': 'Septik artritte eklem aspirasyonu ve drenajı ertelenemez bir acil cerrahi '
                                            'kuralıdır.'},
                         {'text': 'Diz eklemini sıkı elastik bandajla sarıp antibiyotiksiz şekilde ayaktan poliklinik '
                                  'randevusu vermek',
                          'is_correct': False,
                          'scenario_update': 'Eklem içi basınç artışı femur başı ve tibia kıkırdağında avasküler '
                                             'nekroza yol açtı.',
                          'teaching_point': 'Septik eklemin sıkı sarılması basıncı artırarak doku iskemisini felaket '
                                            'boyutuna taşır.'},
                         {'text': 'Sadece geniş spektrumlu oral florokinolon yazıp hastayı ortopedi görüşü almadan '
                                  'evine taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Yetersiz oral tedavi ve drenaj yapılmaması kalıcı eklem ankilozuna yol '
                                             'açtı.',
                          'teaching_point': 'Septik artrit parenteral antibiyotik ve mekanik eklem drenajı ile '
                                            'yatırılarak tedavi edilir.'}]}]},
 {'id': 'Y63',
  'category': '💧 Sıvı-Elektrolit & Renal / Ürolojik Aciller',
  'age': '8 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Kola/çay rengi idrar yapma, göz kapaklarında ve bacaklarda şişlik, baş ağrısı ve tansiyon yüksekliği',
  'history': "Sekiz yaşındaki erkek çocuk ailesi tarafından Sarı Alana getiriliyor: 'Oğlumuz sabahtan beri çay veya "
             'kola renginde, koyu kahverengi idrar yapıyor. İdrar miktarı çok azaldı, günde sadece bir kez azıcık '
             'yaptı. Sabah uyandığında özellikle göz kapakları ve yüzü belirgin şekilde şişti, çorap lastikleri '
             'bacaklarında derin iz bıraktı. Ayrıca şiddetli zonklayıcı baş ağrısı var. Yaklaşık 2 hafta önce yüksek '
             'ateşli boğaz enfeksiyonu geçirmişti ve antibiyotik kullanıp iyileşmişti. Travma veya böcek ısırması '
             "öyküsü yok.'",
  'final_diagnosis': 'Akut Poststreptokoksik Glomerülonefrit (APSGN / Nefritik Sendrom ve Hipertansiyon)',
  'disposition': 'Sarı Alanda Sıvı-Tuz Kısıtlaması, İV Loop Diüretik (Furosemid), Tansiyon Takibi ve Çocuk Nefroloji '
                 'Yatışı',
  'case_pearl': 'Akut Poststreptokoksik Glomerülonefrit (APSGN), çocukluk çağında en sık görülen post-enfeksiyöz '
                'glomerülonefrittir. ETİYOLOJİ: A grubu beta-hemolitik streptokokların (GAS) nefritojenik suşları ile '
                'geçirilen farenjitten 1-2 hafta sonra, veya impetigo/cilt enfeksiyonundan 3-6 hafta sonra immün '
                'kompleks birikimiyle ortaya çıkar. KLASİK NEFRİTİK SENDROM TRİADI: 1) Makroskopik hematüri (çay veya '
                'kola rengi idrar; dismorfik eritrositler ve eritrosit silendirleri), 2) Ödem (özellikle sabahları '
                'belirgin periorbital ödem ve pretibial gode bırakan ödem), 3) Hipertansiyon (sodyum ve su '
                'retansiyonuna bağlı hipervolemik tansiyon yüksekliği). Oligüri eşlik edebilir. TANI: Serum C3 DÜZEYİ '
                "DÜŞÜKTÜR (%90'dan fazlasında geçici hipokomplemanemi; 6-8 haftada normale döner; C4 genellikle "
                'normaldir), ASO veya Anti-DNAse B yüksekliği geçirilmiş streptokok enfeksiyonunu kanıtlar. TEDAVİ: '
                'Temel yaklaşım HİPERVOLEMİ VE HİPERTANSİYONUN KONTROLÜDÜR: 1) Sodyum ve sıvı kısıtlaması (insensibl '
                'kayıp + idrar miktarı), 2) İntravenöz loop diüretikler (Furosemid 1-2 mg/kg İV), 3) Tansiyon kontrolü '
                '(diüretikle düşmezse KKB örneğin Amlodipin veya Nikardipin), 4) GAS eradikasyonu için oral penisilin.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Kola rengi idrar, ödem ve baş ağrısı ile başvuran bu çocukta fizik muayenede ilk dikkat '
                         'edilmesi gereken bulgular nelerdir?',
             'options': [{'text': 'Vital bulguları, özellikle kan basıncını, periorbital ödemi, pretibial ödemi ve '
                                  'hipervolemi belirtilerini tam muayeneyle değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Nefritik sendromda sodyum ve su tutulumuna bağlı hipervolemik hipertansiyon '
                                         'en tehlikeli komplikasyondur (hipertansif ensefalopati, nöbet veya kalp '
                                         'yetmezliği yapabilir). Kan basıncı persentili mutlaka ölçülmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 88/dk, SS 20/dk, SpO2 %99, Kan Basıncı: '
                                         '138/92 mmHg (>99. persentil + 5 mmHg, Evre 2 Hipertansiyon!). Fizik Muayene: '
                                         'Belirgin bilateral periorbital ödem ve yüzde dolgunluk mevcut. Her iki '
                                         'bacakta pretibial 2+ gode bırakan ödem var. Kardiyak odaklar doğal, S3 galo '
                                         'ritmi yok. Akciğer bazallerinde hafif krepitan ral duyuldu (hafif '
                                         'konjesyon). Batın rahat, hepatomegali yok. Nörolojik muayene: Bilinç açık, '
                                         'oryante, ense sertliği yok ancak zonklayıcı baş ağrısı devam ediyor.'},
                         {'text': 'Sadece kulak zarına bakıp tansiyon ölçümü yapmadan hastayı baş ağrısı için karanlık '
                                  'odaya almak',
                          'is_correct': False,
                          'scenario_update': 'Gözden kaçan Evre 2 hipertansiyon hastada hipertansif konvülziyonu '
                                             'tetikledi.',
                          'teaching_point': 'İdrar rengi koyulaşan ve ödemi olan her çocukta tansiyon ölçümü hayati '
                                            'ilk adımdır.'},
                         {'text': 'Hastanın idrar rengini gıda boyası veya pancar tüketimine bağlayıp hiçbir vital '
                                  'ölçüm yapmamak',
                          'is_correct': False,
                          'scenario_update': 'Glomerüler hematüri ve hipertansiyon ihmal edildiği için hasta akciğer '
                                             'ödemine girdi.',
                          'teaching_point': 'Kola rengi idrar aksi kanıtlanana kadar hematüri kabul edilmeli ve '
                                            'böbrekler taranmalıdır.'},
                         {'text': 'Acil cerrahi skrotal eksplorasyon amacıyla hastayı anesteziye hazırlayıp böbrek '
                                  'fonksiyonlarını unutmak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz cerrahi hazırlık sırasında kontrolsüz hipertansiyon '
                                             'intrakraniyal kanama riski doğurdu.',
                          'teaching_point': 'Nefritik sendrom medikal bir acildir; cerrahi yaklaşım endikasyonu '
                                            'yoktur.'}]},
            {'stage_title': 'Laboratuvar İncelemeleri ve İdrar Analizi',
             'question': 'Nefritik sendrom ve Evre 2 hipertansiyon saptanan bu çocukta Sarı Alanda hangi tetkikler '
                         'acilen planlanmalıdır?',
             'options': [{'text': 'Tam idrar tetkiki, idrar mikroskopisi, serum üre, kreatinin, elektrolitler, '
                                  'kompleman C3-C4 ve ASO titresi istemek',
                          'is_correct': True,
                          'explanation': 'TİT ve mikroskopide dismorfik eritrositler ve eritrosit silendirleri '
                                         'glomerüler hematüriyi kanıtlar. Böbrek fonksiyon testleri oligürik böbrek '
                                         'hasarını, serum C3 düşüklüğü ve ASO yüksekliği ise akut nefritik sendromu '
                                         'doğrular.',
                          'new_finding': 'Tam İdrar Tetkiki: Renk çay/kola rengi, Dansite 1025, Protein 2+, Kan 3+ '
                                         '(masif). İdrar Mikroskopisi: Bol dismorfik eritrosit, lökosit 3-5/saha ve '
                                         "patognomonik 'Eritrosit Silendirleri' saptandı. Biyokimya: Üre 48 mg/dL, "
                                         'Kreatinin 0.88 mg/dL (hafif yüksek), Sodyum 136 mEq/L, Potasyum 4.6 mEq/L, '
                                         'Albümin 3.4 g/dL. İmmünoloji: Serum Kompleman C3: 28 mg/dL (belirgin düşük, '
                                         'normal 90-180), Kompleman C4: 24 mg/dL (normal). ASO (Antistreptolizin O): '
                                         '680 IU/mL (belirgin yüksek, normal <200).'},
                         {'text': 'Sadece direkt üriner sistem grafisi ve kranial tomografi çekerek idrar ve kan '
                                  'tahlillerini ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Radyolojik tetkikler nefriti aydınlatamadı, akut böbrek hasarı tablosu '
                                             'derinleşti.',
                          'teaching_point': 'Akut nefritik tabloda temel tanı idrar mikroskopisi ve serum kompleman '
                                            'düzeyleridir.'},
                         {'text': 'Hastadan sadece ter testi ve gaytada parazit incelemesi isteyerek nefrolojik paneli '
                                  'tamamen dışlamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz tahlillerle kaybedilen zamanda hipertansif ansefalopati '
                                             'tehlikesi belirdi.',
                          'teaching_point': 'Hematüri ve ödemle gelen çocukta nefrit paneli ve komplemanlar derhal '
                                            'incelenmelidir.'},
                         {'text': 'Kemik iliği aspirasyonu ve eklem sıvısı analizi planlayarak idrar mikroskopisini '
                                  'laboratuvardan istememek',
                          'is_correct': False,
                          'scenario_update': 'İnvaziv girişimler glomerüler hasarı açıklayamadı ve hastaya ek travma '
                                             'yaşattı.',
                          'teaching_point': 'Eritrosit silindirleri nefritik sendromun mikroskopik imza bulgusudur.'}]},
            {'stage_title': 'Ayırıcı Tanı ve Nihai Tanının Belirlenmesi',
             'question': 'Geçirilmiş farenjit öyküsü, kola rengi idrar, eritrosit silendirleri, Evre 2 hipertansiyon, '
                         'yüksek ASO ve düşük C3 varlığında kesin tanı nedir?',
             'options': [{'text': 'Akut Poststreptokoksik Glomerülonefrit',
                          'is_correct': True,
                          'explanation': 'Geçirilmiş streptokok enfeksiyonu sonrası nefritik sendrom (hematüri, ödem, '
                                         'hipertansiyon) ve geçici C3 düşüklüğü akut poststreptokoksik '
                                         'glomerülonefritin (APSGN) klasik tanısal tablosudur.',
                          'new_finding': 'Kesin Tanı: Akut Poststreptokoksik Glomerülonefrit (APSGN / Nefritik '
                                         'Sendrom) doğrulanmıştır. Hastaya ve ailesine durum açıklanarak Sarı Alan '
                                         'acil tedavi protokolüne geçildi.'},
                         {'text': 'İdiyopatik Minimal Değişiklik Nefrozu',
                          'is_correct': False,
                          'scenario_update': 'Nefrotik sendromda masif proteinüri ve ağır hipoalbüminemi görülür; '
                                             'eritrosit silindiri ve C3 düşüklüğü olmaz.',
                          'teaching_point': 'Nefrotik sendromda hematüri ve hipokomplemanemi beklenmez, proteinüri ön '
                                            'plandadır.'},
                         {'text': 'Basit Alt İdrar Yolu Enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Sistitte dismorfik eritrosit ve eritrosit silendirleri oluşmaz, '
                                             'hipertansiyon ve ödem beklenmez.',
                          'teaching_point': 'Eritrosit silindirleri kanamanın alt idrar yollarından değil '
                                            'glomerüllerden geldiğini kanıtlar.'},
                         {'text': 'Mesane tümörü transizyonel kanseri',
                          'is_correct': False,
                          'scenario_update': 'Çocukluk çağında mesane kanseri neredeyse hiç görülmez; sistemik ödem ve '
                                             'C3 düşüklüğü yapmaz.',
                          'teaching_point': 'Pediatrik yaşta hematürinin en sık glomerüler nedeni poststreptokoksik '
                                            'glomerülonefrittir.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Evre 2 hipertansiyonu ve hipervolemik ödemi olan APSGN hastasında Sarı Alandaki en uygun '
                         'tedavi yönetimi nedir?',
             'options': [{'text': 'Sıvı ve sodyum kısıtlaması uygulamak, intravenöz furosemid vermek ve tansiyon '
                                  'takibiyle servise yatırmak',
                          'is_correct': True,
                          'explanation': 'APSGN tedavisinin temeli hipervolemiyi yönetmektir: Katı tuzsuz diyet, sıvı '
                                         'kısıtlaması (insensibl kayıp 400 mL/m²/gün + çıkarılan idrar), ve '
                                         'ödem/hipertansiyon için intravenöz loop diüretik (Furosemid 1-2 mg/kg). '
                                         'Tansiyon kontrol altına alınamazsa oral kalsiyum kanal blokeri eklenir. '
                                         'Çocuk nefrolojisi servisinde yakın tansiyon ve elektrolit izlemi yapılır.',
                          'new_finding': 'Sıvı kısıtlaması başlatıldı, tuzsuz diyete geçildi ve İV Furosemid (1 mg/kg) '
                                         'uygulandı. Hasta 2 saat içinde 450 mL bol idrar çıkardı. Kan basıncı 138/92 '
                                         "mmHg'den 112/72 mmHg'ye geriledi, baş ağrısı tamamen geçti. Nefroloji "
                                         'servisine devredilerek C3 takibine alındı.'},
                         {'text': 'Hastanın idrarını çoğaltmak amacıyla saatte beş yüz mililitre intravenöz serum '
                                  'fizyolojik yüklemesi yapmak',
                          'is_correct': False,
                          'scenario_update': 'Aşırı sıvı yüklemesi hipervolemik kalp yetmezliği ve solunum '
                                             'yetmezliğini tetikledi.',
                          'teaching_point': 'Nefritik sendromda sodyum ve su atılamaz; sıvı verilmesi tabloyu hızla '
                                            'pulmoner ödeme sokar.'},
                         {'text': 'Tansiyon yüksekliğini önemsemeyip hastaya hiçbir tedavi vermeden ayaktan eve '
                                  'göndermek',
                          'is_correct': False,
                          'scenario_update': 'Tedavisiz kalan kontrolsüz hipertansiyon evde hipertansif kriz ve '
                                             'jeneralize konvülziyon doğurdu.',
                          'teaching_point': 'Evre 2 hipertansiyonlu çocuk acil diüretik ve antihipertansif tedavi ile '
                                            'yatırılmalıdır.'},
                         {'text': 'Böbrekleri temizlemek amacıyla hastaya acil cerrahi laparoskopik böbrek masajı '
                                  'yapmak',
                          'is_correct': False,
                          'scenario_update': 'İnvaziv böbrek manipülasyonu perirenal hematom ve hemorajik şoka yol '
                                             'açtı.',
                          'teaching_point': 'Glomerülonefrit medikal bir hastalıktır; cerrahi girişimin hiçbir yeri '
                                            'yoktur.'}]}]},
 {'id': 'Y64',
  'category': '💧 Sıvı-Elektrolit & Renal / Ürolojik Aciller',
  'age': '4 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Sabahları göz kapaklarında başlayıp bacaklara ve karına yayılan yaygın şişlik, idrarda köpürme',
  'history': "Dört yaşındaki erkek çocuk ailesi tarafından Sarı Alana getiriliyor: 'Yaklaşık 5 gün önce sabah "
             'uyandığında göz kapakları ve yüzü şişmişti. Alerji sanıp bekledik ancak şişlik giderek bacaklarına, ayak '
             'bileklerine ve testislerine yayıldı. Karnı belirgin şekilde şişti, pantolonları kapanmıyor. Çocuğun '
             'idrar miktarı azaldı ve idrar yaparken köpük köpük olduğunu fark ettik. Ateşi, döküntüsü ya da idrarda '
             "kırmızı kan görmedik. Halsiz ve iştahsız.'",
  'final_diagnosis': 'İlk Atak İdiopatik Nefrotik Sendrom (Minimal Değişiklik Hastalığı / Ağır Hipoalbüminemi ve '
                     'Anazarka Ödem)',
  'disposition': 'Sarı Alanda Sıvı-Tuz Kısıtlaması, Ağır Ödemde İV Albümin ve Furosemid, Oral Prednizolon Başlanması '
                 've Çocuk Nefroloji Yatışı',
  'case_pearl': 'Pediatrik yaş grubunda nefrotik sendromun en sık nedeni (%85-90) Minimal Değişiklik Hastalığıdır. '
                'KLASİK TETRAD: 1) Masif proteinüri (spot idrar protein/kreatinin > 2 mg/mg veya 24 saatlik idrarda > '
                '40 mg/m²/saat; idrar çubuğunda 3+/4+ protein), 2) Ağır hipoalbüminemi (serum albümin < 2.5 g/dL), 3) '
                'Yaygın ödem (periorbital başlayıp skrotal ve batında asit oluşturan anazarka ödem), 4) Hiperlipidemi '
                '(özellikle kolesterol yüksekliği). TEDAVİ: İlk atakta oral prednizolon (60 mg/m²/gün veya 2 '
                'mg/kg/gün, maks 60 mg) başlanır. Ağır skrotal ödem, solunumu bozan asit veya hipovolemi varsa %20 İV '
                'albümin infüzyonu (0.5-1 g/kg, 2-4 saatte) ve infüzyonun sonuna doğru İV furosemid (1-2 mg/kg) '
                'verilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Yaygın anazarka ödem ve idrarda köpürme ile getirilen bu çocukta fizik muayenede öncelikli '
                         'odaklanmanız gereken klinik bulgular nelerdir?',
             'options': [{'text': 'Vital bulguları, kan basıncını, periorbital ve pretibial gode bırakan ödemi, '
                                  'batında asit varlığını ve skrotal ödemi değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Ödemin yaygınlığı (periorbital, pretibial, skrotal ve asit), intravasküler '
                                         'volüm durumu ve kan basıncı değerlendirilmelidir. İdiopatik nefrozda '
                                         'çocuklar genellikle normotansiftir ancak hipovolemiye veya aşırı su '
                                         'tutulumuna dikkat edilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 98/dk, SS 22/dk, SpO2 %99, TA 96/60 mmHg '
                                         '(Normotansif), Kilo 18 kg (ödem öncesi 15.5 kg). Fizik Muayene: Bilateral '
                                         'periorbital ödem, pretibial 3+ gode bırakan ödem, batında distansiyon ve '
                                         'açıklığı yukarı bakan matite (asit) ile masif skrotal ödem izlendi. Kardiyak '
                                         've akciğer sesleri doğal.'},
                         {'text': 'Sadece kulak zarını ve boğazını inceleyip enfeksiyon odağı aradıktan sonra diğer '
                                  'sistem muayenelerini tamamen ihmal etmek',
                          'is_correct': False,
                          'scenario_update': 'Gözden kaçan masif skrotal ödem ve asit hastanın solunum ve dolaşım '
                                             'konforunu bozdu.',
                          'teaching_point': 'Yaygın ödemle başvuran hastada vücut ağırlığı, tansiyon ve asit varlığı '
                                            'eksiksiz incelenmelidir.'},
                         {'text': 'Kafatasındaki fontanelleri ve temporal arterleri palpe ederek kafa içi basınç '
                                  'artışı semptomlarına odaklanıp beklemek',
                          'is_correct': False,
                          'scenario_update': 'Sistemik ödemin kaynağı araştırılmadı ve böbrek tutulumu göz ardı '
                                             'edildi.',
                          'teaching_point': 'Bilateral yaygın ödemde öncelik böbrek, karaciğer ve kalp '
                                            'fonksiyonlarının değerlendirilmesidir.'},
                         {'text': 'Acil cerrahi akut batın şüphesiyle rektal tuşe ve kasık fıtığı redüksiyonu '
                                  'manevralarını öncelikli olarak uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz invaziv girişim aşırı ağrı ve ajitasyona neden oldu.',
                          'teaching_point': 'Batın distansiyonu olan ödemli çocukta öncelikle asit matitesi ve renal '
                                            'kayıp araştırılmalıdır.'}]},
            {'stage_title': 'Laboratuvar İncelemeleri ve İdrar Protein Analizi',
             'question': 'Anazarka ödemi ve idrar köpürmesi olan hastada klinik tabloyu netleştirmek için Sarı Alanda '
                         'hangi tetkik kombinasyonu istenmelidir?',
             'options': [{'text': 'Tam idrar tetkiki, spot idrarda protein/kreatinin oranı, serum albümini, lipid '
                                  'paneli ve böbrek fonksiyon testleri istemek',
                          'is_correct': True,
                          'explanation': 'TİT ve spot idrar protein/kreatinin oranı masif proteinüriyi saptar. Serum '
                                         'albümin düşüklüğü (<2.5 g/dL) ve kolesterol yüksekliği masif protein kaçağı '
                                         'tablosunu belgeler. Böbrek fonksiyonları ve elektrolitler renal durumu '
                                         'gösterir.',
                          'new_finding': 'TİT: Dansite 1030, Protein 4+ (masif), Glukoz negatif, Lökosit/Eritrosit '
                                         'negatif. Spot İdrar Protein/Kreatinin: 8.4 mg/mg (belirgin masif aralık, >2 '
                                         'mg/mg). Biyokimya: Serum Albümin 1.6 g/dL (ağır hipoalbüminemi), Total '
                                         'Protein 3.8 g/dL, Kolesterol 380 mg/dL, Trigliserid 290 mg/dL, BUN 14 mg/dL, '
                                         'Kreatinin 0.42 mg/dL, Serum Sodyum 132 mEq/L, Potasyum 4.1 mEq/L. Kompleman '
                                         'C3 ve C4 normal düzeyde.'},
                         {'text': 'Sadece direkt kafa grafisi, paranasal sinüs tomografisi ve lomber ponksiyon ile '
                                  'beyin omurilik sıvısı örneği almak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz beyin tetkikleri masif protein kaybının saptanmasını saatlerce '
                                             'geciktirdi.',
                          'teaching_point': 'Ödemli hastada ilk yapılması gereken en ucuz ve en hızlı tetkik tam idrar '
                                            'tahlilidir.'},
                         {'text': 'Gaitada gizli kan, fekal kalprotektin ve kolonoskopi hazırlığı için oral laksatif '
                                  'solüsyon verilmesini planlamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz laksatif kullanımı dehidratasyon ve hipovolemik şok riskini '
                                             'artırdı.',
                          'teaching_point': 'İdrarda köpürme renal protein kaçağının tipik göstergesidir; bağırsak '
                                            'tetkiki öncelikli değildir.'},
                         {'text': 'Akut koroner sendrom şüphesiyle seri troponin, kreatin kinaz ve acil koroner '
                                  'anjiyografi laboratuvar paneli göndermek',
                          'is_correct': False,
                          'scenario_update': 'Yanlış kardiyak tanı nedeniyle renal protein kaybı ve hipoalbüminemi '
                                             'atlandı.',
                          'teaching_point': 'Pediatrik bilateral simetrik ödemde renal etiyoloji kardiyak iskemiye '
                                            'göre katbekat sıktır.'}]},
            {'stage_title': 'Ayırıcı Tanı ve Nihai Tanının Belirlenmesi',
             'question': 'Masif proteinüri, ağır hipoalbüminemi, hiperlipidemi ve yaygın ödem bulguları hangi klinik '
                         'tabloyu doğrulamaktadır?',
             'options': [{'text': 'İlk Atak İdiopatik Nefrotik Sendrom',
                          'is_correct': True,
                          'explanation': 'Masif proteinüri (spot idrar protein/kreatinin >2), serum albümin <2.5 g/dL, '
                                         'hiperkolesterolemi ve yaygın ödem çocukluk çağının en sık glomerüler tablosu '
                                         'olan İdiopatik Nefrotik Sendromu (Minimal Değişiklik Hastalığı) '
                                         'kesinleştirir.',
                          'new_finding': 'Kesin Tanı: İlk Atak İdiopatik Nefrotik Sendrom (Minimal Değişiklik '
                                         'Hastalığı) doğrulanmıştır. Hastaya ve ailesine durum açıklanarak Sarı Alan '
                                         'acil tedavi protokolüne geçildi.'},
                         {'text': 'Akut Glomerülonefritik Sendrom Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Glomerülonefritte makroskopik hematüri, eritrosit silendirleri ve '
                                             'hipertansiyon ön plandadır.',
                          'teaching_point': 'Nefritik sendromda hematüri ve hipertansiyon, nefrotik sendromda masif '
                                            'proteinüri ve ağır ödem vardır.'},
                         {'text': 'Konjestif Kalp Yetmezliği Atağı',
                          'is_correct': False,
                          'scenario_update': 'Kalp yetmezliğinde kardiyomegali, hepatomegali ve venöz dolgunluk '
                                             'beklenir; masif proteinüri olmaz.',
                          'teaching_point': 'İdrarda 4+ protein ve spot P/C >8 olması primer renal podosit '
                                            'patolojisini gösterir.'},
                         {'text': 'Protein Kaybettiren Enteropati Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Enteropatide gastrointestinal protein kaybı vardır; idrarda masif '
                                             'proteinüri görülmez.',
                          'teaching_point': 'İdrar tahlilinde masif protein saptanması gastrointestinal kayıpları '
                                            'kesin olarak dışlar.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Nefrotik sendrom ilk atağı ve masif skrotal/pretibial ödemi olan çocukta Sarı Alandaki en '
                         'uygun klinik yaklaşım nedir?',
             'options': [{'text': 'Sıvı-tuz kısıtlaması, semptomatik ağır ödemde intravenöz albümin ve furosemid, oral '
                                  'prednizolon başlanması ve yatış planlamak',
                          'is_correct': True,
                          'explanation': 'Tedavide tuz ve sıvı kısıtlaması esastır. Semptomatik ağır ödemde (skrotal '
                                         'ödem, asit) %20 İV Albümin (0.5-1 g/kg, 2-4 saatte) ve ardından İV Furosemid '
                                         '(1-2 mg/kg) ile sıvı çekilir. İlk atak tedavisinde oral Prednizolon (60 '
                                         'mg/m²/gün) başlanır ve nefrolojiye yatırılır.',
                          'new_finding': 'Tuzsuz diyete geçildi ve sıvı kısıtlaması uygulandı. Ağır skrotal ödem ve '
                                         'asit için %20 İV Albümin (1 g/kg) 4 saatlik infüzyonla verildi, infüzyon '
                                         'bitimine doğru İV Furosemid (1 mg/kg) uygulandı. Hasta 3 saat içinde 600 mL '
                                         'idrar çıkardı, skrotal ve batın gerginliği belirgin rahatladı. Oral '
                                         'Prednizolon (60 mg/m²/gün) başlanarak çocuk nefroloji servisine devredildi.'},
                         {'text': 'İdrar çıkışını artırmak için saatte beş yüz mililitre intravenöz serum fizyolojik '
                                  'yüklemesi yapıp acilen taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Aşırı serum fizyolojik yüklenmesi anazarka ödemi şiddetlendirip akut '
                                             'pulmoner ödeme yol açtı.',
                          'teaching_point': 'Düşük onkotik basınç varken aşırı kristalloid verilmesi sıvının doğrudan '
                                            'interstisyuma kaçmasına neden olur.'},
                         {'text': 'Çocuğa acil cerrahi skrotal dekompresyon insizyonu ve laparoskopik periton drenajı '
                                  'uygulayarak cerrahiye devretmek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz cerrahi insizyonlar sekonder bakteriyel peritonit ve sepsis '
                                             'tablosunu tetikledi.',
                          'teaching_point': 'Nefrotik ödem medikal onkotik tedaviye hızla yanıt verir; cerrahi drenaj '
                                            'kesinlikle kontrendikedir.'},
                         {'text': 'Ödemin kendiliğinden geçeceğini söyleyerek hiçbir medikal tedavi ve kısıtlama '
                                  'vermeden evine geri göndermek',
                          'is_correct': False,
                          'scenario_update': 'Tedavisiz kalan hipoalbüminemi tromboembolizm ve spontan bakteriyel '
                                             'peritonit riskini artırdı.',
                          'teaching_point': 'Nefrotik sendrom ilk atağı remisyon elde edilene kadar yakın '
                                            'hospitalizasyon ve steroid tedavisi gerektirir.'}]}]},
 {'id': 'Y65',
  'category': '🧠 Nörolojik Aciller',
  'age': '7 Yaşında',
  'gender': 'Kız',
  'complaint': 'Mide bulantısı ilacı aldıktan sonra boyunda kasılma, başın geriye bükülmesi, gözlerin yukarı dikilmesi '
               've konuşamama',
  'history': "Yedi yaşındaki kız çocuk Sarı Alana kucakta getiriliyor: 'Kızım dün geceden beri kusuyordu. Bugün öğlen "
             'aile hekimi mide bulantısı için damla şeklinde bir antiemetik reçete etti. İlaçtan öğleden sonra iki kez '
             'verdik. Yaklaşık 2 saat sonra aniden boynu sola doğru kilitlendi, başı geriye büküldü. Göz bebekleri '
             'yukarı dikildi ve gözlerini aşağı indiremiyor. Çenesi kilitlendi, dili dışarı fırlayacak gibi oluyor ve '
             'konuşamıyor. Bilinci açık, bizi duyuyor ve çok korkmuş halde ağlıyor. Daha önce hiç havale ya da kasılma '
             "öyküsü yoktu.'",
  'final_diagnosis': 'İlaca Bağlı Akut Ekstrapiramidal Reaksiyon (Antiemetik Kaynaklı Okülojirik Kriz ve Tortikolis)',
  'disposition': 'Sarı Alanda Acil Antikolinerjik Tedavi (Biperiden veya Difenhidramin İV/İM), İlaca Son Verilmesi ve '
                 'Klinik Gözlem',
  'case_pearl': 'Çocuklarda santral dopamin D2 reseptör blokajı yapan antiemetiklerin (özellikle metoklopramid, '
                'klorpromazin, prometazin) kullanımı akut ekstrapiramidal yan etkilere yol açabilir. En sık görülen '
                'tablo AKUT DİSTONİK REAKSİYONDUR. KLİNİK: İlaç alımından genellikle 1-24 saat sonra gelişen istemsiz, '
                'ağrılı kas kasılmaları; akut tortikolis (boyun kasılması), retrokollis, okülojirik kriz (göz '
                'kürelerinin yukarı deviye olup kilitlenmesi), trismus (çene kilitlenmesi) ve dil protrüzyonu. EN '
                'ÖNEMLİ AYIRICI TANI: BİLİNÇ TAMAMEN AÇIKTIR! Hasta çevreyi anlar ve panik içindedir (epileptik '
                'nöbetten temel fark). TEDAVİ: Santral antikolinerjik ajan olan BİPERİDEN (Akineton: 0.04-0.1 mg/kg, '
                'maks 2.5-5 mg, yavaş İV veya İM) veya DİFENHİDRAMİN (1 mg/kg İV/İM). İlaç uygulamasından sonra 5-15 '
                'dakika içinde semptomlar dramatik olarak tamamen düzelir. Nüksleri önlemek için şüpheli ilaç '
                'kesilmeli ve hasta 24 saat oral antikolinerjik/antihistaminik ile korunmalıdır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Antiemetik ilaç kullanımı sonrası boyun ve göz kasılması gelişen bu hastada fizik muayenede '
                         'öncelikli değerlendirme ne olmalıdır?',
             'options': [{'text': 'Bilinç durumunu, havayolu açıklığını, boyun kas spazmını, göz deviasyonunu ve diğer '
                                  'ekstrapiramidal motor bulguları incelemek',
                          'is_correct': True,
                          'explanation': 'Bilinç durumunun değerlendirilmesi (açık olması nöbeti dışlamada kritiktir), '
                                         'havayolu açıklığı (laringospazm riski) ve istemsiz kas spazm bölgeleri '
                                         '(tortikolis, okülojirik kriz, trismus) acilen belirlenmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 104/dk, SS 20/dk, SpO2 %99, TA 102/64 mmHg. '
                                         'Fizik Muayene: Bilinç tamamen açık, sorulanları anlıyor, korkulu ve ajite. '
                                         'Boyunda sternokleidomastoid kas spazmına bağlı sola tortikolis ve hafif '
                                         'retrokollis mevcut. Her iki göz küresi yukarı deviye ve fikse (okülojirik '
                                         'kriz). Çenede trismus ve dilde hafif protrüzyon izleniyor. Havayolu açık, '
                                         'stridor veya solunum sıkıntısı yok. Patolojik refleks yok.'},
                         {'text': 'Sadece kemik iliği aspirasyonu yaparak akut lösemi infiltrasyonunu ve '
                                  'lenfoproliferatif yayılımı araştırmaya girişmek',
                          'is_correct': False,
                          'scenario_update': 'İnvaziv ve gereksiz işlem korkmuş çocuğun ajitasyonunu ve laringeal '
                                             'spazm riskini artırdı.',
                          'teaching_point': 'Ani gelişen kasılmalarda öncelik havayolu, bilinç ve nörolojik '
                                            'muayenedir.'},
                         {'text': 'Çocuğa acil trakeostomi açarak entübe etmek ve mekanik ventilatör parametrelerini '
                                  'en yüksek basınca ayarlamak',
                          'is_correct': False,
                          'scenario_update': 'Havayolu açık hastaya uygulanan cerrahi girişim ciddi komplikasyonlara '
                                             'yol açtı.',
                          'teaching_point': 'Stridoru ve havayolu obstrüksiyonu olmayan kas spazmı hastasında cerrahi '
                                            'havayolu gerekmez.'},
                         {'text': 'Kardiyak cerrahi hazırlığı için femoral arter kateterizasyonu yapıp ekokardiyografi '
                                  'ile aort kapağını değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Nöromusküler kriz tablosu yanlış odaklanma nedeniyle tedavisiz kaldı.',
                          'teaching_point': 'İlaç maruziyeti sonrası ani boyun ve göz spazmında kardiyak '
                                            'kateterizasyon endikasyonu yoktur.'}]},
            {'stage_title': 'Laboratuvar İncelemeleri ve Toksikolojik Yaklaşım',
             'question': 'Bilinç açıkken ani başlangıçlı istemsiz kasılmaları olan bu hastada tanıyı netleştirmek için '
                         'ne yapılmalıdır?',
             'options': [{'text': 'Ayrıntılı ilaç maruziyet öyküsünü sorgulamak, kan şekeri ve elektrolitleri ölçüp '
                                  'epileptik nöbet ayırıcı tanısını dışlamak',
                          'is_correct': True,
                          'explanation': 'Hangi ilacın, ne dozda ve ne zaman alındığının sorgulanması tanı '
                                         'koydurucudur. Kan şekeri ve kalsiyum ölçümü hipoglisemi ve tetaniyi dışlar. '
                                         'Bilincin açık olması epileptik status tablosunu dışlar.',
                          'new_finding': 'İlaç sorgusunda: Çocuğa kusma için son 6 saatte hekimin önerdiği dozun iki '
                                         'katı dopamin antagonisti antiemetik damla verildiği öğrenildi. Glukoz: 98 '
                                         'mg/dL. Elektrolitler: Na 138 mEq/L, K 4.2 mEq/L, İyonize Kalsiyum 1.22 '
                                         'mmol/L (normal). Bilincin tamamen açık olması, postiktal konfüzyon olmaması '
                                         've maruziyet öyküsü ekstrapiramidal motor reaksiyonu destekledi.'},
                         {'text': 'Acil kontrastlı tüm vücut manyetik rezonans anjiyografisi çekerek serebral '
                                  'anevrizma ve disseksiyon aramak',
                          'is_correct': False,
                          'scenario_update': "Boynu kasılı haldeki hastanın MR'a sokulması sedasyon güçlüğü ve "
                                             'aspirasyon riski doğurdu.',
                          'teaching_point': 'Tipik ilaç ilişkili ekstrapiramidal krizde acil MR çekilmez, klinik tanı '
                                            'ile tedavi başlanır.'},
                         {'text': 'Menenjit şüphesiyle acil lomber ponksiyon uygulayıp beyin omurilik sıvısından viral '
                                  'kültür paneli beklemek',
                          'is_correct': False,
                          'scenario_update': 'Ateşi olmayan ve bilinci açık hastada lomber ponksiyon süreci gereksiz '
                                             'travmaya neden oldu.',
                          'teaching_point': 'Ateş ve ense sertliği yokken, bilincin açık olduğu izole spazmda lomber '
                                            'ponksiyon endike değildir.'},
                         {'text': 'Acil elektrokonvülsif terapi planı yaparak genel anestezi altında beyin biyopsisi '
                                  'örneği göndermeyi düşünmek',
                          'is_correct': False,
                          'scenario_update': 'Akut medikal spazm tablosu felaket niteliğinde yanlış bir cerrahi yöne '
                                             'kaydı.',
                          'teaching_point': 'İlaca bağlı ekstrapiramidal reaksiyonlar medikal antidot ile dakikalar '
                                            'içinde tamamen düzelir.'}]},
            {'stage_title': 'Ayırıcı Tanı ve Nihai Tanının Belirlenmesi',
             'question': 'Antiemetik maruziyeti sonrası gelişen tortikolis, okülojirik kriz ve trismus tablosunda '
                         'kesin klinik tanı nedir?',
             'options': [{'text': 'İlaca Bağlı Akut Ekstrapiramidal Reaksiyon',
                          'is_correct': True,
                          'explanation': 'Antiemetik ilaç kullanımı sonrası gelişen akut tortikolis, okülojirik kriz '
                                         've trismus, ilaca bağlı akut distonik reaksiyonun (ekstrapiramidal sendrom) '
                                         'klasik tablosudur.',
                          'new_finding': 'Kesin Tanı: İlaca Bağlı Akut Ekstrapiramidal Reaksiyon (Metoklopramid '
                                         'Kaynaklı Distonik Reaksiyon) doğrulanmıştır. Hastaya ve ailesine durum '
                                         'açıklanarak Sarı Alan acil tedavi protokolüne geçildi.'},
                         {'text': 'Febril Status Epileptikus Nöbeti',
                          'is_correct': False,
                          'scenario_update': 'Status epileptikusta bilinç kapalıdır, ritmik klonik kasılmalar görülür '
                                             've ateş mevcuttur.',
                          'teaching_point': 'Distonide bilinç tamamen açıktır ve hasta kasılmanın farkında olup korku '
                                            'duyar.'},
                         {'text': 'Akut Bakteriyel Menenjit Enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Menenjitte yüksek ateş, letarji, toksik görünüm ve ense sertliği vardır; '
                                             'okülojirik kriz görülmez.',
                          'teaching_point': 'Ateşsiz hastada izole boyun ve göz deviasyonu menenjit ile bağdaşmaz.'},
                         {'text': 'Tetanus Toksini Kas Spazmı',
                          'is_correct': False,
                          'scenario_update': 'Aşıları tam olan çocukta ani antiemetik sonrası gelişen tablo tetanus '
                                             'değildir.',
                          'teaching_point': 'Tetanus tam aşılı çocuklarda görülmez ve ilaç alım saatine bağlı '
                                            'gelişmez.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'İlaca bağlı akut kas spazmı ve okülojirik krizi olan bu çocukta Sarı Alandaki en uygun acil '
                         'tedavi nedir?',
             'options': [{'text': 'Şüpheli ilacı derhal kesmek, intravenöz biperiden veya difenhidramin uygulamak ve '
                                  'hastayı klinikte izlemek',
                          'is_correct': True,
                          'explanation': 'Santral dopamin/asetilkolin dengesini yeniden kurmak için antikolinerjik '
                                         'ajan olan Biperiden (Akineton 0.04-0.1 mg/kg İV/İM) veya Difenhidramin (1 '
                                         'mg/kg İV) uygulanır. Enjeksiyondan 5-15 dakika sonra kasılmalar tamamen '
                                         'çözülür.',
                          'new_finding': 'Şüpheli antiemetik ilaç derhal kesildi. İntravenöz damar yolundan Biperiden '
                                         '(0.05 mg/kg, 2.5 mg) yavaş İV olarak uygulandı. Uygulamanın 10. dakikasında '
                                         'boyundaki tortikolis ve trismus tamamen çözüldü, göz küreleri normal primer '
                                         'pozisyona döndü. Hasta rahatça konuşmaya başladı ve ağrısı tamamen geçti. 24 '
                                         'saatlik oral takip planıyla gözleme alındı.'},
                         {'text': 'Hastayı hemen genel anesteziye alıp kas gevşetici vererek acil kraniyotomi '
                                  'cerrahisine sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz anestezi ve cerrahi girişim geri dönüşümsüz morbidite yarattı.',
                          'teaching_point': 'Distonik kriz basit bir antikolinerjik enjeksiyonla dakikalar içinde '
                                            'tamamen düzelir.'},
                         {'text': 'Durumu psikolojik histeri kabul edip hastayı karanlık odaya kilitleyerek hiçbir '
                                  'tedavi vermemek',
                          'is_correct': False,
                          'scenario_update': 'Tedavisiz kalan laringeal spazm hipoksi ve solunum sıkıntısına neden '
                                             'oldu.',
                          'teaching_point': 'Distonik reaksiyonlar organik nörolojik acillerdir; histeri veya rol '
                                            'yapma olarak nitelendirilemez.'},
                         {'text': 'Bulantısı sürdüğü için aynı ilacın dozunu iki katına çıkarıp intravenöz infüzyonla '
                                  'vermek',
                          'is_correct': False,
                          'scenario_update': 'Sorumlu dopamin blokerinin tekrar verilmesi jeneralize kas rijiditesi ve '
                                             'laringospazm doğurdu.',
                          'teaching_point': 'Reaksiyona neden olan dopaminerjik antiemetik derhal kesilmeli ve bir '
                                            'daha verilmemelidir.'}]}]},
 {'id': 'Y66',
  'category': '🩸 Hematolojik & Onkolojik Aciller',
  'age': '6 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Akut lenfoblastik lösemi tedavisi gören çocukta 38.8°C yüksek ateş, titreme ve halsizlik',
  'history': "Altı yaşındaki erkek çocuk ailesi tarafından Sarı Alana getiriliyor: 'Oğlumuz Akut Lenfoblastik Lösemi "
             '(ALL) tanısıyla kemoterapi alıyor, son kemoterapi kürünü 8 gün önce aldı. Göğsünde implante port '
             'kateteri mevcut. Yaklaşık 3 saat önce başlayan titreme ve ateş şikayeti oldu, evde ölçtüğümüz ateş '
             "38.8°C'ye ulaştı. Onkoloji ekibimiz ateş çıkarsa hiç beklemeden acil servise başvurmamızı söylemişti. "
             "Çocuk halsiz, iştahsız ve yorgun görünüyor. Öksürük, kusma ya da ishal eşlik etmiyor.'",
  'final_diagnosis': 'Onkolojik Acil - Febril Nötropeni (Port Kateterli Lösemi Hastasında Ciddi Enfeksiyon Riski)',
  'disposition': 'Sarı Alanda İlk 60 Dakikada Kan Kültürleri Sonrası Acil Geniş Spektrumlu Antipsödomonal İV '
                 'Antibiyotik ve Onkoloji Yatışı',
  'case_pearl': 'Febril nötropeni pediatrik onkolojinin en kritik medikal acilidir. TANIM: Tek bir oral/aksiller ateş '
                'ölçümünün ≥38.3°C olması veya 1 saatten uzun süre ≥38.0°C seyretmesi VE Mutlak Nötrofil Sayısının '
                "(ANC) <500/mm³ olması (veya 48 saat içinde <500/mm³'e düşmesi beklenen <1000/mm³ değer). ALTIN SAAT "
                '(GOLDEN HOUR) KURALI: Acil servise başvuru anından itibaren İLK 60 DAKİKA İÇİNDE port kateterden ve '
                'periferik venden kan kültürleri alınmalı, ardından HİÇ VAKİT KAYBETMEDEN geniş spektrumlu '
                'antipsödomonal bakterisidal monoterapi (Piperasilin-Tazobaktam 100 mg/kg veya Sefepim 50 mg/kg veya '
                'Seftazidim; hemodinamik instabilite veya kateter enfeksiyonu bulgusunda Vankomisin eklenir) '
                'intravenöz yoldan başlanmalıdır. KESİNLİKLE YAPILMAMASI GEREKENLER: Rektal ateş ölçümü ve rektal tuşe '
                'KESİNLİKLE KONTRENDİKEDİR (mukozal mikro-yırtık ve ölümcül bakteriyemi riski).',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Kemoterapi alan ve ateşi 38.8°C olan port kateterli bu çocukta Sarı Alandaki fizik muayene '
                         'yaklaşımı ne olmalıdır?',
             'options': [{'text': 'Vital bulguları, şok belirtilerini, port kateter giriş yerini, oral mukozayı ve '
                                  'perianal bölgeyi rektal tuşe yapmadan değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Hemodinamik stabilite (taşikardi, hipotansiyon, kapiller dolum), port giriş '
                                         'yeri enfeksiyonu, mukozit ve perianal cilt lezyonları aranmalıdır. Rektal '
                                         'tuşe veya rektal derece mukozal yırtık ve bakteriyemi riski nedeniyle ASLA '
                                         'yapılmamalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 38.9°C, KTA 136/dk (taşikardik), SS 26/dk, SpO2 %98, TA '
                                         '94/60 mmHg, KDZ 2 sn. Fizik Muayene: Soluk ve bitkin görünümde. Sağ göğüs ön '
                                         'duvarındaki port kateter lojunda eritem, ısı artışı veya akıntı yok. Ağız '
                                         'mukozasında hafif kuruluk var, aktif aftöz lezyon yok. Akciğer sesleri '
                                         'doğal, batın rahat. Perianal bölge inspeksiyonla intakt (rektal tuşe ve '
                                         'rektal ölçümden kesinlikle kaçınıldı).'},
                         {'text': 'Enfeksiyon odağını saptamak için hemen derin rektal tuşe ve anal manometri '
                                  'tetkiklerini zorlayarak uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Rektal mukozanın zedelenmesi bağırsak florasının kana karışmasına ve '
                                             'gram negatif sepsise yol açtı.',
                          'teaching_point': 'İmmünsüprese hastalarda rektal tuşe ve lavman kesinlikle kontrendikedir.'},
                         {'text': 'Çocuğun port kateterini yerinden derhal cerrahi aletle çekip çıkarmak ve pansuman '
                                  'yapmadan bekletmek',
                          'is_correct': False,
                          'scenario_update': 'Port kateterin plansız koparılması masif kanama ve damar hasarı doğurdu.',
                          'teaching_point': 'Kateter enfeksiyonu kanıtlanmadıkça veya septik tromboflebit olmadıkça '
                                            'port acilde sökülmez.'},
                         {'text': 'Sadece ekstremite reflekslerine ve kemik mineral dansitesine bakarak diğer klinik '
                                  'bulguları tamamen göz ardı etmek',
                          'is_correct': False,
                          'scenario_update': 'Sistemik ateş odağı araştırılmadı ve septik şok riskine karşı '
                                             'hazırlıksız kalındı.',
                          'teaching_point': 'Onkolojik acilde vital bulgular ve enfeksiyon kapıları eksiksiz '
                                            'taranmalıdır.'}]},
            {'stage_title': 'Laboratuvar İncelemeleri ve Acil Kültür Protokolü',
             'question': 'Kemoterapi alan ve ateşi çıkan onkoloji hastasında Sarı Alanda acil olarak hangi tetkikler '
                         'planlanmalıdır?',
             'options': [{'text': 'Tam kan sayımı, periferik ve porttan kan kültürleri, idrar tetkiki, biyokimya ve '
                                  'C-reaktif protein istemek',
                          'is_correct': True,
                          'explanation': 'Mutlak Nötrofil Sayısını (ANC) hesaplamak için tam kan sayımı şarttır. '
                                         'Antibiyotik öncesinde hem port lümeninden hem de periferik damar yolundan '
                                         'aerob/anaerob kan kültürleri alınmalı, biyokimya ve akut faz reaktanları '
                                         'incelenmelidir.',
                          'new_finding': 'Hemogram: Lökosit 900/mm³, Nötrofil %18, Lenfosit %75, Mutlak Nötrofil '
                                         'Sayısı (ANC): 162/mm³ (ciddi derin düşüklük, <500/mm³), Hemoglobin 8.8 g/dL, '
                                         'Trombosit 42.000/mm³. CRP: 48 mg/L (yüksek), Prokalsitonin: 1.4 ng/mL. Port '
                                         'lümeninden ve periferik koldan iki ayrı şişeye kan kültürleri alındı. İdrar '
                                         'tahlili gönderildi.'},
                         {'text': 'Sadece direkt kıkırdak grafileri ve kemik biyopsisi planlayarak kültür almadan '
                                  'saatlerce beklemek',
                          'is_correct': False,
                          'scenario_update': 'Kültür alınmadan bekletilen hastada patojen saptanamadı ve tedavi '
                                             'gecikti.',
                          'teaching_point': 'Kemoterapi sonrası ateşte antibiyotik öncesi çift kan kültürü altın '
                                            'standarttır.'},
                         {'text': 'Kemoterapötik ilaç dozlarını üç katına çıkarıp kan sayımı sonucunu görmeden hemen '
                                  'uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Aplastik krizdeki hastaya kemoterapi verilmesi fatal kemik iliği '
                                             'durmasına yol açtı.',
                          'teaching_point': 'Ateş ve nötropeni varken kemoterapi durdurulur ve acil antibiyotik '
                                            'tedavisine odaklanılır.'},
                         {'text': 'Hastaya acil kolonoskopi ve bronkoskopi ayarlayarak enfeksiyon belirteçlerini hiç '
                                  'araştırmamak',
                          'is_correct': False,
                          'scenario_update': 'İnvaziv endoskopik işlemler kemoterapi alan hastada masif kanama ve '
                                             'sepsise neden oldu.',
                          'teaching_point': 'İnvaziv endoskopi nötropenide kontrendikedir; temel yaklaşım periferik '
                                            'kültürlerdir.'}]},
            {'stage_title': 'Ayırıcı Tanı ve Nihai Tanının Belirlenmesi',
             'question': 'ALL hastasında 38.9°C ateş ve ANC 162/mm³ tablosunda kesin acil tanı nedir?',
             'options': [{'text': 'Onkolojik Acil Febril Nötropeni Tablosu',
                          'is_correct': True,
                          'explanation': 'Ateş ≥38.3°C ve Mutlak Nötrofil Sayısının (ANC) <500/mm³ olması acil '
                                         'intravenöz antibiyoterapi gerektiren febril nötropeni sendromunun kesin '
                                         'tanısıdır.',
                          'new_finding': 'Kesin Tanı: Onkolojik Acil - Febril Nötropeni doğrulanmıştır. Hastaya ve '
                                         'ailesine durum açıklanarak Sarı Alan acil tedavi protokolüne geçildi.'},
                         {'text': 'Basit Viral Üst Solunum Enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'ANC 162 olan onkoloji hastasında ateş asla basit viral enfeksiyon kabul '
                                             'edilip evde takip edilemez.',
                          'teaching_point': 'Nötropenik hastada her ateş aksi kanıtlanana kadar ölümcül bakteriyel '
                                            'enfeksiyon gibi yönetilir.'},
                         {'text': 'Aseptik İlaç Alerjisi Döküntüsü',
                          'is_correct': False,
                          'scenario_update': 'Döküntüsü olmayan ve derin nötropenisi olan çocukta antibiyotiksiz '
                                             'beklemek şoka yol açar.',
                          'teaching_point': 'Kemoterapötik nötropenide primer risk immün yetmezlik zemininde gelişen '
                                            'bakteriyel sepsistir.'},
                         {'text': 'İdiyopatik Juvenil Artrit Atağı',
                          'is_correct': False,
                          'scenario_update': 'Lösemi tedavisi gören hastanın ateşi romatolojik bir atak değildir.',
                          'teaching_point': 'Kemoterapi ilişkili immünsüpresyonda nötropenik ateş onkolojik bir '
                                            'acildir.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'ANC <500/mm³ ve ateşi olan bu hastada Sarı Alanda ilk 60 dakikada uygulanması gereken en '
                         'kritik tedavi nedir?',
             'options': [{'text': 'Kan kültürleri sonrası vakit kaybetmeden intravenöz geniş spektrumlu antipsödomonal '
                                  'beta-laktam antibiyotik başlamak ve yatırmak',
                          'is_correct': True,
                          'explanation': 'Altın saat ilkesi: Kültürler alındıktan sonraki ilk 60 dakikada '
                                         'antipsödomonal monoterapi (Piperasilin-Tazobaktam veya Sefepim) İV yoldan '
                                         'başlanmalıdır. Ateş takibi ve nötropeni gerileyene kadar parenteral tedavi '
                                         'amacıyla onkoloji servisine yatırılır.',
                          'new_finding': 'Port ve periferik kan kültürleri alındıktan hemen sonra, başvurunun 40. '
                                         'dakikasında İV Piperasilin-Tazobaktam (100 mg/kg) infüzyonu başlatıldı. Ateş '
                                         'için İV Parasetamol verildi (oral veya rektal yoldan kaçınıldı). İdame '
                                         'hidrasyonu açıldı. Hasta acil pediatrik onkoloji servisine devredildi.'},
                         {'text': 'Kültür sonuçları üç gün sonra çıkana kadar hiçbir antibiyotik vermeden sadece '
                                  'parasetamol ile evde bekletmek',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotiğin gecikmesi hastanın 12 saat içinde refrakter septik şoka ve '
                                             'multiorgan yetmezliğine girmesine yol açtı.',
                          'teaching_point': 'Febril nötropenide antibiyotik gecikmesi mortaliteyi katlayarak artırır; '
                                            'ilk 60 dakikada başlanmalıdır.'},
                         {'text': 'Ateşi düşürmek amacıyla hastayı buzlu küvete yatırıp oral aspirin ve rektal fitil '
                                  'uygulaması yapmak',
                          'is_correct': False,
                          'scenario_update': 'Rektal fitil perianal apseye, aspirin trombositopenik kanamaya ve '
                                             'hipotermi şoka yol açtı.',
                          'teaching_point': 'Trombositopenik ve nötropenik çocukta rektal uygulamalar ve aspirin '
                                            'kesinlikle kontrendikedir.'},
                         {'text': 'Hastanın port kateterinden yüksek doz intramüsküler aşı uygulayarak ayaktan '
                                  'poliklinik kontrolüne yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Nötropenik krize aşı yapılması enfeksiyonu derinleştirdi ve kateter '
                                             'hasarı yarattı.',
                          'teaching_point': 'Aktif febril nötropenide aşı yapılmaz, acil geniş spektrumlu İV '
                                            'antibiyoterapi verilir.'}]}]},
 {'id': 'Y67',
  'category': '🩸 Hematolojik & Onkolojik Aciller',
  'age': '9 Yaşında',
  'gender': 'Kız',
  'complaint': 'Kronik hemolitik anemisi olan çocukta her iki bacakta ve sırtta dayanılmaz kemik ağrısı ve yürüyememe',
  'history': "Dokuz yaşındaki kız çocuk Sarı Alana ağlayarak getiriliyor: 'Kızımızda doğuştan bilinen "
             'hemoglobinopatisi (kronik hemolitik anemi) var. İki gün önce soğuk havada dışarıda kaldıktan sonra '
             'başlayan hafif bacak ağrısı, bugün dayanılmaz kemik ve sırt ağrısına dönüştü. Evde parasetamol ve '
             'ibuprofen verdik fakat ağrısı hiç azalmadı. Ağrıdan yürüyemiyor, bacaklarına dokundurmuyor, ağrı skoru '
             "10 üzerinden 9. Ateşi yok, öksürük veya solunum sıkıntısı yok. Çocuğumuz kıvranıyor.'",
  'final_diagnosis': 'Orak Hücreli Anemi - Akut Vazo-Oklüzif Ağrı Krizi (Ağrılı Kemik / Ekstremite Krizi)',
  'disposition': 'Sarı Alanda Agresif İntravenöz Hidrasyon, Basamaklı Multimodal Analjezi (İV Opioid + NSAİİ) ve '
                 'Hematoloji Servis Yatışı',
  'case_pearl': 'Orak hücreli anemide deoksijenasyon, dehidratasyon, enfeksiyon veya soğuk maruziyeti sonucu HbS '
                'polimerize olur, eritrositler oraklaşır ve mikrosirkülasyonu tıkayarak iskemik doku hasarına ve '
                'şiddetli vazo-oklüzif krize (VOC) yol açar. TEDAVİ İLKELERİ: 1) HIZLI VE AGRESİF ANALJEZİ: İlk 30-60 '
                'dakikada başlanmalıdır. Şiddetli ağrıda (skor ≥7) İV opioidler (Morfin 0.1 mg/kg İV her 2-4 saatte '
                'bir veya İV Fentanil) basamaklı olarak verilir ve parenteral NSAİİ (Ketorolak veya İbuprofen) ile '
                'kombine edilir. 2) HİDRASYON: İdame sıvısının 1.25 - 1.5 katı (hipotonik mayi: %5 Dekstroz + 1/2 SF; '
                'hipertonik sıvılar oraklaşmayı artıracağından verilmez; aşırı sıvı pulmoner ödeme yol açabileceğinden '
                'dikkatle titre edilir). 3) OKSİJEN TUZAĞI: Oksijen YALNIZCA SpO2 <%95 ise verilmelidir; normoksik '
                'hastada rutin oksijen kemik iliğinde eritropoezi baskılayabilir! 4) AKUT GÖĞÜS SENDROMU (ACS) RİSKİ: '
                'Takipne, hipoksi ve göğüs ağrısı gelişimi yönünden solunum sesleri yakından izlenmelidir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Bilinen hemoglobinopatisi olup şiddetli kemik ağrısıyla başvuran bu çocukta ilk '
                         'odaklanılması gerekenler nelerdir?',
             'options': [{'text': 'Vital bulguları, ağrı skorunu, periferik nabızları, ekstremite hassasiyetini ve '
                                  'solunum sistemi bulgularını değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Ağrı şiddetinin objektif skorlanması (Wong-Baker skalası), solunum sıkıntısı '
                                         '(akut göğüs sendromunu ekarte etmek için) ve dolaşım durumu hızla '
                                         'incelenmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.0°C, KTA 118/dk (ağrıya sekonder taşikardi), SS '
                                         '22/dk, SpO2 %98 (oda havasında), TA 108/68 mmHg, KDZ 2 sn. Ağrı skoru '
                                         '(Wong-Baker): 9/10 (şiddetli ağrı). Fizik Muayene: Her iki femur ve tibia '
                                         'üzerinde belirgin palpasyon hassasiyeti mevcut, lokal kızarıklık veya eklem '
                                         'efüzyonu yok. Akciğer sesleri doğal, ral veya hırıltı yok. Dalak palpe '
                                         'edilmiyor (oto-splenektomi ile uyumlu).'},
                         {'text': 'Sadece kulak zarı perforasyonunu inceleyip ağrı skorunu ve periferik dolaşımı '
                                  'tamamen ihmal etmek',
                          'is_correct': False,
                          'scenario_update': 'Ağrı skoru ölçülmediği için analjezi gecikti ve hasta ağrı şokuna girdi.',
                          'teaching_point': 'Akut iskemik kemik ağrısında ilk adım ağrının şiddetini standart '
                                            'skalalarla belirlemektir.'},
                         {'text': 'Hastaya acil lomber ponksiyon uygulayarak intrakraniyal basınç artışı araştırmasına '
                                  'girişip zaman kaybetmek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz invaziv girişim aşırı stres yaratarak eritrosit oraklaşmasını '
                                             'daha da artırdı.',
                          'teaching_point': 'Serebral semptomu olmayan ağrı krizinde lomber ponksiyon endikasyonu '
                                            'yoktur.'},
                         {'text': 'Ağrının psikolojik olduğunu varsayıp hiçbir muayene yapmadan hastayı psikiyatri '
                                  'polikliniğine göndermek',
                          'is_correct': False,
                          'scenario_update': 'İskemik kemik infarktı ilerledi ve kemik iliği nekrozu gelişti.',
                          'teaching_point': 'Hemoglobinopatili çocukların ağrısı gerçektir ve gerçek doku iskemisinden '
                                            'kaynaklanır.'}]},
            {'stage_title': 'Laboratuvar İncelemeleri ve Radyolojik Tarama',
             'question': 'Şiddetli kemik ağrısı kriziyle gelen hemoglobinopati hastasında Sarı Alanda hangi tetkikler '
                         'istenmelidir?',
             'options': [{'text': 'Tam kan sayımı, retikülosit sayısı, periferik yayma, biyokimya, bilirubinler ve '
                                  'bazal akciğer grafisi istemek',
                          'is_correct': True,
                          'explanation': 'Hemoglobin bazal değerle kıyaslanmalı (aplastik kriz veya sekestrasyonu '
                                         'dışlamak için), retikülosit kemik iliği aktivitesini göstermeli, hemoliz '
                                         'belirteçleri ve Akut Göğüs Sendromunu ekarte etmek için bazal akciğer '
                                         'grafisi değerlendirilmelidir.',
                          'new_finding': 'Hemogram: Hb 7.6 g/dL (hastanın bilinen bazal düzeyi 7.8 g/dL), Lökosit '
                                         '13.500/mm³, Trombosit 340.000/mm³, Retikülosit %8.2 (yüksek, kemik iliği '
                                         'yanıtı aktif). Periferik Yayma: Hilal şeklinde kıvrılmış anormal '
                                         'eritrositler, hedef hücreleri ve Howell-Jolly cisimcikleri. Total Bilirubin: '
                                         '3.2 mg/dL, İndirekt Bilirubin: 2.6 mg/dL. Akciğer Grafisi: Akut göğüs '
                                         'sendromu bulgusu yok, parankim temiz.'},
                         {'text': 'Sadece kemik iliği aspirasyonu ve kraniyal tomografi çekerek kan sayımı ve '
                                  'biyokimyayı ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Temel laboratuvar geciktiği için hidrasyon ve anemi derinliği '
                                             'değerlendirilemedi.',
                          'teaching_point': 'Akut krizde bazal hemoglobin ve retikülosit seviyesinin bilinmesi hayati '
                                            'öneme sahiptir.'},
                         {'text': 'Gaitada parazit mikroskopisi ve ter testi isteyerek ağrı yönetimine hiç '
                                  'odaklanmamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz tahlillerle kaybedilen zamanda doku iskemisi kalıcı hasara '
                                             'neden oldu.',
                          'teaching_point': 'Ağrılı krizde amaç hızla doku perfüzyonunu sağlamak ve komplikasyonları '
                                            'taramaktır.'},
                         {'text': 'Acil eklem artroskopisi planlayıp anestezi konsültasyonuyla ameliyathaneye sevk '
                                  'hazırlığı yapmak',
                          'is_correct': False,
                          'scenario_update': 'Genel anestezi ve cerrahi stres oraklaşma krizini multiorgan '
                                             'yetmezliğine dönüştürdü.',
                          'teaching_point': 'Septik artrit bulgusu yoksa kemik iskemi krizi tamamen medikal olarak '
                                            'tedavi edilir.'}]},
            {'stage_title': 'Ayırıcı Tanı ve Nihai Tanının Belirlenmesi',
             'question': 'Hemoglobinopati hastasında soğuk maruziyeti sonrası gelişen şiddetli kemik ağrısı krizinde '
                         'klinik tanı nedir?',
             'options': [{'text': 'Orak Hücreli Anemi Vazo-Oklüzif Ağrı Krizi',
                          'is_correct': True,
                          'explanation': 'Bilinen kronik hemolitik anemili hastada soğuk tetiklemesi sonrası ortaya '
                                         'çıkan şiddetli kemik ağrıları, retikülositoz ve yaymada orak eritrositler '
                                         'akut vazo-oklüzif ağrı krizini belgeler.',
                          'new_finding': 'Kesin Tanı: Orak Hücreli Anemi - Vazo-Oklüzif Ağrı Krizi doğrulanmıştır. '
                                         'Hastaya ve ailesine durum açıklanarak Sarı Alan acil tedavi protokolüne '
                                         'geçildi.'},
                         {'text': 'Akut Bakteriyel Kemik Osteomiyelit Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Ateşin olmaması ve ağrının iki taraflı yaygın kemiklerde bulunması '
                                             'osteomiyelitle uyumsuzdur.',
                          'teaching_point': 'Osteomiyelit genellikle tek odaklıdır ve yüksek ateş ile lokal '
                                            'enflamasyon eşlik eder.'},
                         {'text': 'Çocukluk Çağı Juvenil Romatoid Artrit',
                          'is_correct': False,
                          'scenario_update': 'Kronik otoimmün artrit ani şiddetli 9/10 kemik şaftı ağrısı ve periferik '
                                             'yayma bulgusu yapmaz.',
                          'teaching_point': 'Hemoglobinopatilerde kemik ağrısı krizleri otoimmün artritlerden tamamen '
                                            'farklıdır.'},
                         {'text': 'Akut D Vitamini Eksikliği Raşitizmi',
                          'is_correct': False,
                          'scenario_update': 'Raşitizm kronik metafiz genişlemesi yapar; ani başlayan dayanılmaz ağrı '
                                             'krizi yapmaz.',
                          'teaching_point': 'Besinsel raşitizm tablosu akut mikrovasküler iskemi kliniğini '
                                            'açıklamaz.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Ağrı skoru 9/10 olan bu hastada Sarı Alandaki en uygun multimodal tedavi yönetimi nasıl '
                         'olmalıdır?',
             'options': [{'text': 'İntravenöz hidrasyon sağlamak, basamaklı opioid analjezik ile antienflamatuar '
                                  'vermek ve hematoloji servisine yatırmak',
                          'is_correct': True,
                          'explanation': 'Tedavinin sacayağı: İntravenöz idame sıvısının 1.25-1.5 katı hidrasyon (%5 '
                                         'Dekstroz + 1/2 SF) ve şiddetli ağrıda derhal İV Morfin (0.1 mg/kg) ile İV '
                                         'NSAİİ (İbuprofen veya Ketorolak) kombinasyonudur. SpO2 normal olduğu için '
                                         'rutin oksijen verilmez.',
                          'new_finding': 'Damar yolu açıldı, %5 Dekstroz 1/2 SF ile idamenin 1.5 katı hızında '
                                         'hidrasyon başlatıldı. İntravenöz Morfin (0.1 mg/kg) ve İV İbuprofen '
                                         "uygulandı. 45 dakika sonra ağrı skoru 9/10'dan 3/10'a geriledi. SpO2 %98 "
                                         'olduğu için oksijen başlanmadı (oksijen tuzağından kaçınıldı). Pediatrik '
                                         'hematoloji servisine yatışı yapıldı.'},
                         {'text': 'Hastaya hiçbir ağrı kesici vermeyip sadece oda havasında derin nefes egzersizi '
                                  'yaptırarak bekletmek',
                          'is_correct': False,
                          'scenario_update': 'Tedavi edilmeyen şiddetli ağrı taşikardi ve hiperventilasyona yol açarak '
                                             'oraklaşmayı şiddetlendirdi.',
                          'teaching_point': 'Ağrı krizinde ilk 30 dakikada yeterli analjezi verilmesi uluslararası bir '
                                            'klinik zorunluluktur.'},
                         {'text': 'Ağrıyı dindirmek amacıyla bacaklarına sıkı kompresyon bandajı sarıp hastayı soğuk '
                                  'odaya almak',
                          'is_correct': False,
                          'scenario_update': 'Soğuk ve kompresyon ekstremite vazokonstrüksiyonunu artırarak yaygın '
                                             'kemik nekrozu doğurdu.',
                          'teaching_point': 'Soğuk ve kompresyon vazooklüzyonu artırır; sıcak ve rahatlatıcı ortam '
                                            'sağlanmalıdır.'},
                         {'text': 'Oksijen satürasyonu yüzde doksan sekiz olmasına rağmen hastaya yüksek basınçlı '
                                  'mekanik ventilasyon uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz yüksek basınçlı ventilasyon barotravma ve hemodinamik bozulmaya '
                                             'neden oldu.',
                          'teaching_point': 'Orak hücreli krizde hipoksi yoksa rutin oksijen eritropoezi '
                                            'baskılayabileceğinden verilmez.'}]}]},
 {'id': 'Y68',
  'category': '👶 Yenidoğan Acilleri',
  'age': '3 Günlük',
  'gender': 'Erkek',
  'complaint': 'Doğumun 3. gününde baştan ayağa yayılan belirgin sarılık, emmede zayıflama ve aşırı uyku meyli',
  'history': "Üç günlük erkek bebek anne ve babası tarafından Sarı Alana getiriliyor: 'Bebeğimiz 38. haftada normal "
             'spontan doğumla, 3200 gram doğdu. Hastaneden 24. saatte taburcu edilirken hafif yüzünde sarılık vardı. '
             'Ancak dün akşamdan beri sarılığı hızla göğsüne, karnına, bacaklarına ve ayak tabanlarına kadar indi. '
             'Cildi adeta portakal rengi oldu. Bugün memeyi kavramakta çok zorlanıyor, birkaç yudum emip hemen '
             'uyuyakalıyor. Bezi günde sadece 2 kez azıcık ıslanıyor, hiç kaka yapmadı. Ateşi yok ama uyandırmakta çok '
             "zorlanıyoruz.'",
  'final_diagnosis': 'Yenidoğan Ağır İndirekt Hiperbilirubinemisi (ABO Uygunsuzluğuna Bağlı Akut İzoimmün Hemolitik '
                     'Sarılık)',
  'disposition': 'Sarı Alanda Acil Çift Yönlü Yoğun Fototerapi, İntravenöz Sıvı Desteği, Kan Değişimi Hazırlığı ve YBÜ '
                 'Yatışı',
  'case_pearl': 'Yenidoğanda sarılık sefalokaudal yönde (baştan ayaklara doğru) ilerler. Göbek altına ve ayak '
                'tabanlarına inen sarılık TSB düzeyinin >15 mg/dL olduğunu düşündürür. ETİYOLOJİ: Anne kan grubu O, '
                'bebek A veya B ise ABO uyuşmazlığına bağlı izoimmün hemoliz riski yüksektir (Direkt Coombs testi '
                'pozitifliği). RİSK DEĞERLENDİRMESİ: Yaş saatine göre total serum bilirubini (TSB) değerlendirilir; '
                '72. saatte TSB >17-18 mg/dL yüksek risk bölgesindedir ve ACİL YOĞUN FOTOTERAPİ (irradiance ≥30 '
                'µW/cm²/nm) gerektirir. KAN DEĞİŞİMİ (EXCHANGE TRANSFUSION) EŞİĞİ: TSB düzeyi kan değişimi sınırına '
                '(genellikle >20-22 mg/dL) yaklaştığında veya akut bilirubin ensefalopatisi bulguları (letarji, '
                'hipotonisite, retrokollis) varlığında acil kan hazırlığı yapılmalıdır. KOMPLİKASYON: Serbest indirekt '
                "bilirubin kan-beyin bariyerini geçerek bazal gangliyonlarda birikir ve geri dönüşümsüz KERNİKTERUS'a "
                'yol açar.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Üç günlük yenidoğanda ayak tabanlarına kadar inen sarılık ve letarji varlığında fizik '
                         'muayene önceliği ne olmalıdır?',
             'options': [{'text': 'Vital bulguları, sarılığın sefalokaudal yayılımını, emme ve moro reflekslerini ve '
                                  'dehidratasyon bulgularını değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Sarılığın Kramer dermal zonlarına göre yayılımı (ayak tabanına inmesi >15 '
                                         'mg/dL düşündürür), nörolojik refleksler (akut bilirubin ensefalopatisi erken '
                                         'bulgusu olan letarji ve hipotonisite) ve dehidratasyon derecesi hızla '
                                         'incelenmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 144/dk, SS 44/dk, SpO2 %98, TA 64/38 mmHg, '
                                         'Ağırlık 2910 g (%9 kilo kaybı, dehidratasyon). Fizik Muayene: Kramer Bölge 5 '
                                         '(ayak tabanları ve avuç içleri dahil tüm vücut derin sarı-turuncu renkte). '
                                         'Nörolojik Değerlendirme: Emme refleksi zayıf, Moro refleksi tembel, belirgin '
                                         'hipotonik ve letarjik. Karaciğer kot altı 1.5 cm palpe ediliyor, dalak ele '
                                         'gelmiyor. Sefalohematom saptanmadı.'},
                         {'text': 'Sadece periferik kemik kırığı ve kalça çıkığı muayenesi yaparak nörolojik '
                                  'refleksleri tamamen ihmal etmek',
                          'is_correct': False,
                          'scenario_update': 'Nörolojik ensefalopati bulguları atlandı ve kernikterus riski kritik '
                                             'sınıra ulaştı.',
                          'teaching_point': 'Ağır sarılıkta emme ve moro refleksleri nörotoksisiteyi saptamada ilk '
                                            'basamaktır.'},
                         {'text': 'Bebeğe acil katarakt ameliyatı planlamak amacıyla oftalmolojik kornea biyopsisi '
                                  'tetkikini öncelikli görmek',
                          'is_correct': False,
                          'scenario_update': 'İnvaziv ve yanlış yönelimli işlem sırasında bilirubin toksisitesi '
                                             'ilerledi.',
                          'teaching_point': 'Yenidoğan sarılığı sistemik metabolik bir durumdur; kornea biyopsisi '
                                            'endikasyonu yoktur.'},
                         {'text': 'Sarılığın sadece güneşte bekletilerek geçeceğini söyleyip hiçbir klinik ve '
                                  'nörolojik muayene yapmamak',
                          'is_correct': False,
                          'scenario_update': 'Muayenesiz bırakılan bebekte bilirubin düzeyi toksik eşiği aşarak '
                                             'konvülziyonu tetikledi.',
                          'teaching_point': 'Kramer 5 düzeyinde sarılık acil objektif laboratuvar ölçümü gerektiren '
                                            'ciddi bir tablodur.'}]},
            {'stage_title': 'Laboratuvar İncelemeleri ve Kan Grubu Tayini',
             'question': 'Ağır sarılık ve beslenme güçlüğü olan 3 günlük yenidoğanda Sarı Alanda hangi acil tetkikler '
                         'istenmelidir?',
             'options': [{'text': 'Total ve direkt bilirubin, anne ve bebek kan grubu, direkt Coombs testi, tam kan '
                                  'sayımı ve retikülosit istemek',
                          'is_correct': True,
                          'explanation': 'Total ve direkt bilirubin düzeyi fototerapi ve kan değişimi sınırını '
                                         'belirler. Anne ve bebek kan grubu ile Direkt Coombs testi izoimmün hemolizi '
                                         '(ABO veya Rh uygunsuzluğu) kanıtlar; hemogram ve retikülosit hemolizin '
                                         'şiddetini gösterir.',
                          'new_finding': 'Laboratuvar: Total Serum Bilirubini (TSB): 20.4 mg/dL (72. saatte yaş '
                                         'nomogramında yüksek risk zonunun üzerinde, kan değişimi sınırına yakın), '
                                         'Direkt Bilirubin: 0.6 mg/dL. Anne kan grubu: O Rh(+), Bebek kan grubu: A '
                                         'Rh(+). Direkt Antiglobulin (Coombs) Testi: Pozitif (+). Hemogram: Hb 12.8 '
                                         'g/dL, Hematokrit %38, Retikülosit %9.4 (belirgin hemolitik süreç). Periferik '
                                         'yaymada mikrosferositler izlendi.'},
                         {'text': 'Sadece kraniyal manyetik rezonans spektroskopi ve ter testi isteyerek kan grubu ve '
                                  'bilirubin ölçümünü dışlamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz ileri görüntüleme beklenirken bilirubin ensefalopatisi geri '
                                             'dönüşsüz aşamaya geldi.',
                          'teaching_point': 'Yenidoğan sarılığında ilk ve en acil tetkik kantitatif serum bilirubin '
                                            'düzeyidir.'},
                         {'text': 'Gaitada rota antijeni ve idrar aminoasit kromatografisi gönderip bilirubin düzeyini '
                                  'ölçmeyi gereksiz saymak',
                          'is_correct': False,
                          'scenario_update': 'Hemolitik sarılık atlandı ve bazal ganglion toksisitesi derinleşti.',
                          'teaching_point': 'Yenidoğanda sarılık tetkiklerinin başında kan grubu uygunsuzluğu ve '
                                            'bilirubin gelir.'},
                         {'text': 'Acil lomber ponksiyon yaparak beyin omurilik sıvısı kültürünü tek tanısal yöntem '
                                  'olarak kabul etmek',
                          'is_correct': False,
                          'scenario_update': 'Lomber ponksiyon kan grubu uyuşmazlığını ve patolojik hemolizi '
                                             'aydınlatamadı.',
                          'teaching_point': 'İzoimmün hemolizde tanı kanda antikor ve bilirubin tayini ile konur.'}]},
            {'stage_title': 'Ayırıcı Tanı ve Nihai Tanının Belirlenmesi',
             'question': 'Anne O, bebek A kan grubunda 72. saatte TSB 20.4 mg/dL ve Coombs pozitifliği hangi klinik '
                         'tanıyı koydurur?',
             'options': [{'text': 'Yenidoğan Ağır İzoimmün Hemolitik Hiperbilirubinemisi',
                          'is_correct': True,
                          'explanation': 'Anne O, bebek A kan grubu uyumsuzluğunda pozitif Coombs testi, yüksek '
                                         'retikülosit ve 72. saatte TSB >20 mg/dL akut izoimmün hemolitik sarılık '
                                         'tablosunu kesinleştirir.',
                          'new_finding': 'Kesin Tanı: Yenidoğan Ağır İzoimmün Hemolitik Hiperbilirubinemisi (ABO '
                                         'Uyuşmazlığı) doğrulanmıştır. Hastaya ve ailesine durum açıklanarak Sarı Alan '
                                         'acil tedavi protokolüne geçildi.'},
                         {'text': 'Anne Sütü Sarılığı Sendromu',
                          'is_correct': False,
                          'scenario_update': 'Anne sütü sarılığı 2. haftada pik yapar; 3. günde Coombs pozitifliği ve '
                                             '20 mg/dL bilirubin yapmaz.',
                          'teaching_point': 'İlk günlerdeki hızlı yükselen hemolitik sarılıklar anne sütü sarılığı '
                                            'olamaz.'},
                         {'text': 'Biliyer Atrezi Kolestaz Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Biliyer atrezide direkt (konjuge) bilirubin yüksektir ve akolik gaita '
                                             'görülür; burada indirekt bilirubin yüksektir.',
                          'teaching_point': 'İndirekt bilirubinin baskın olduğu erken sarılıklarda kolestaz '
                                            'düşünülmez.'},
                         {'text': 'Fizyolojik Yenidoğan Sarılığı Süreci',
                          'is_correct': False,
                          'scenario_update': "Fizyolojik sarılıkta TSB 12-13 mg/dL'yi geçmez, Coombs negatiftir ve "
                                             'hemoliz görülmez.',
                          'teaching_point': 'TSB 20 mg/dL üzeri değerler asla fizyolojik kabul edilemez; acil tedavi '
                                            'şarttır.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'TSB 20.4 mg/dL olan ve dehidratasyon gelişen bu yenidoğanda Sarı Alandaki en uygun acil '
                         'yönetim nedir?',
             'options': [{'text': 'Acil çift yönlü yoğun fototerapi başlatmak, hidrasyonu sağlamak, kan değişimi '
                                  'hazırlığı yapmak ve yoğun bakıma yatırmak',
                          'is_correct': True,
                          'explanation': 'TSB fototerapi eşiğini belirgin aşmış ve kan değişimi sınırına yaklaşmıştır. '
                                         'Acilen yoğun LED fototerapi (gözler ve gonadlar korunarak) başlanmalı, İV '
                                         'hidrasyon verilmeli, kan bankasıyla iletişime geçilerek uygun kan (O grubu, '
                                         "Rh uygun) ile kan değişimi hazırlığı yapılmalı ve yenidoğan YBÜ'ye "
                                         'yatırılmalıdır.',
                          'new_finding': 'Bebeğin gözlerine koruyucu bant takıldı ve acilen çift yönlü yoğun LED '
                                         'fototerapi altına alındı. Damar yolundan %10 Dekstroz + 1/5 SF infüzyonu '
                                         'başlatılarak dehidratasyon düzeltildi. Kan merkezine acil kan değişimi için '
                                         'taze O grubu Rh(+) kan hazırlığı emri verildi. Bebek yenidoğan yoğun bakım '
                                         "ünitesine (YYBÜ) transfer edildi. 4 saat sonraki kontrol TSB 17.1 mg/dL'ye "
                                         'geriledi.'},
                         {'text': 'Bebeği pencere kenarına yatırıp güneş ışığı almasını önererek herhangi bir '
                                  'fototerapi vermeden eve göndermek',
                          'is_correct': False,
                          'scenario_update': "Yetersiz ışık maruziyeti nedeniyle bilirubin 25 mg/dL'ye tırmandı ve "
                                             'kalıcı kernikterus gelişti.',
                          'teaching_point': 'Güneş ışığı patolojik hiperbilirubinemide etkisiz ve tehlikelidir; yoğun '
                                            'tıbbi fototerapi şarttır.'},
                         {'text': 'Sarılığın emzirmeyle kendiliğinden geçeceğini söyleyip hiçbir tetkik ve tedavi '
                                  'vermeden üç gün sonraya çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Tedavisiz kalan bebek akut bilirubin ensefalopatisi nöbeti geçirdi.',
                          'teaching_point': 'Risk sınırındaki sarılık acil müdahale gerektirir; izlemsiz taburculuk '
                                            'malpraktistir.'},
                         {'text': 'Bebeğe acil genel anestezi altında laparoskopik safra kesesi eksizyonu ve '
                                  'splenektomi ameliyatı planlamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz cerrahi müdahale 3 günlük yenidoğanda cerrahi mortaliteye neden '
                                             'oldu.',
                          'teaching_point': 'İzoimmün sarılık medikal fototerapi ve gerekirse kan değişimi ile tedavi '
                                            'edilir.'}]}]},
 {'id': 'Y69',
  'category': '💊 Toksikoloji & Metabolik / Endokrin Aciller',
  'age': '14 Günlük',
  'gender': 'Kız',
  'complaint': 'Fışkırır tarzda kusma, kilo kaybı, aşırı emmeme, uykuya meyil, tansiyon düşüklüğü ve genital bölgede '
               'koyuluk',
  'history': "On dört günlük kız bebek anne ve babası tarafından Sarı Alana getiriliyor: 'Kızımız miadında 3300 gram "
             'doğdu. Son 4 gündür her beslenmeden sonra safrasız, fışkırır tarzda kusuyor. Hiç meme emmek istemiyor, '
             'sürekli uyuyor ve uyandırmakta çok zorlanıyoruz. Bezi sabahtan beri hiç ıslanmadı. Doğum kilosunun çok '
             'altına indi, gözleri çukura kaçtı. Ayrıca genital bölgesinin renginin diğer bebeklere göre belirgin '
             "şekilde koyu ve klitorisinin belirgin büyük olduğunu fark ettik. Çocuk adeta kendinden geçiyor.'",
  'final_diagnosis': 'Konjenital Adrenal Hiperplaziye Bağlı Akut Tuz Kaybettiren Adrenal Kriz (21-Hidroksilaz '
                     'Eksikliği)',
  'disposition': 'Sarı Alanda Acil Sıvı Resüsitasyonu (İV %0.9 SF + %10 Dekstroz), İntravenöz Hidrokortizon ve '
                 'Pediatrik YBÜ Yatışı',
  'case_pearl': 'Konjenital Adrenal Hiperplazi (KAH) en sık 21-hidroksilaz enzim eksikliğinden (%95) kaynaklanır. TUZ '
                'KAYBETTİREN FORM: Aldosteron ve kortizol sentezlenemez; adrenal androjenler aşırı üretilir. '
                'PATOFİZYOLOJİ: 1) ALDOSTERON EKSİKLİĞİ: Böbrekten sodyum atılımı ve potasyum tutulumu -> AĞIR '
                "HİPONATREMİ (Na <120 mEq/L), HİPERKALEMİ (K >7 mEq/L; EKG'de sivri T dalgaları ve ventriküler aritmi "
                'riski), hipovolemik şok ve dehidratasyon. 2) KORTİZOL EKSİKLİĞİ: Hipoglisemi, vasküler kollaps ve '
                'ACTH artışına bağlı hiperpigmentasyon (genitalya ve areolada). 3) ANDROJEN FAZLALIĞI: Kız bebeklerde '
                'virilizasyon (klitoromegali, labial füzyon, Prader evrelemesi). ACİL TEDAVİ: 1) Hipovolemik şok için '
                'derhal İZOTONİK SERUM FİZYOLOJİK (20 mL/kg SF; potasyumsuz mayi!), 2) Hipoglisemi için %10 Dekstroz, '
                '3) ACİL İV HİDROKORTİZON (stres dozu: 25 mg İV bolus, ardından 50-100 mg/m²/gün infüzyon). 4) '
                'Hiperkalemi kardiyotoksik ise İV Kalsiyum Glukonat.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'On dört günlük bebekte fışkırır kusma, letarji ve şok tablosunda fizik muayenede öncelikle '
                         'nelere bakılmalıdır?',
             'options': [{'text': 'Vital bulguları, şok belirtilerini, dehidratasyon derecesini, hiperpigmentasyonu ve '
                                  'dış genital organ anatomisini incelemek',
                          'is_correct': True,
                          'explanation': 'Hipovolemik şok bulguları (hipotansiyon, zayıf nabız, uzamış kapiller '
                                         'dolum), ağır dehidratasyon derecesi, ACTH yüksekliğini gösteren '
                                         'hiperpigmentasyon ve kız bebekte virilizasyon (klitoromegali) mutlaka '
                                         'değerlendirilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.2°C, KTA 168/dk (taşikardik, zayıf nabızlar), SS '
                                         '48/dk, SpO2 %97, TA 52/30 mmHg (belirgin hipotansiyon), KDZ 4 sn (uzamış). '
                                         'Kilo 2650 g (%20 ağır kilo kaybı ve dehidratasyon). Fizik Muayene: Letarjik, '
                                         'göz küreleri çökmüş, fontanel çökük, mukoza kuru. Genital Muayene: '
                                         'Labiumlarda ve genital bölgede belirgin hiperpigmentasyon (koyulaşma), '
                                         'klitoromegali (Prader Evre 2-3 görünüm) izlendi. Testis palpe edilmedi.'},
                         {'text': 'Sadece kas iskelet sisteminde skolyoz ve ekstremite uzunluk farkı taraması yaparak '
                                  'hemodinamiyi ihmal etmek',
                          'is_correct': False,
                          'scenario_update': 'Şok ve dehidratasyon derinleşti; hasta kardiyak arrest sınırına geldi.',
                          'teaching_point': 'Kusan ve letarjik bebekte ilk hedef dolaşım ve dehidratasyon derecesini '
                                            'saptamaktır.'},
                         {'text': 'Çocuğa acil lomber ponksiyon uygulayarak hidrosefali varlığını ve kafa içi '
                                  'basıncını değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Şoktaki hipotansif yenidoğana invaziv girişim yapılması arrest riskini '
                                             'tetikledi.',
                          'teaching_point': 'Hipotansif ve şoktaki bebekte önce vasküler resüsitasyon sağlanmalıdır.'},
                         {'text': 'Kusmanın gaz sancısından kaynaklandığını düşünerek hiçbir muayene yapmadan bebeği '
                                  'gaz damlasıyla göndermek',
                          'is_correct': False,
                          'scenario_update': 'Taburcu edilmeye çalışılan bebek Sarı Alanda kardiyak aritmiye girdi.',
                          'teaching_point': 'Yenidoğanda fışkırır tarzda kusma ve kilo kaybı asla basit gaz sancısı '
                                            'olamaz.'}]},
            {'stage_title': 'Laboratuvar İncelemeleri ve Elektrolit Paneli',
             'question': 'Şokta olan, genital ambigiusu ve hiperpigmentasyonu bulunan bu bebekte acil hangi tetkikler '
                         'istenmelidir?',
             'options': [{'text': 'Acil kan gazı, kan şekeri, serum elektrolitleri, EKG, 17-hidroksiprogesteron ve '
                                  'serum kortizol düzeyi istemek',
                          'is_correct': True,
                          'explanation': "Hiponatremi, hiperkalemi ve hipoglisemiyi doğrulamak acildir. EKG'de sivri T "
                                         'dalgaları hiperkalemi riskini gösterir. 17-OH Progesteron yüksekliği ve '
                                         'düşük kortizol 21-hidroksilaz eksikliğini kesinleştirir.',
                          'new_finding': 'Glukoz: 48 mg/dL (hipoglisemi). Kan Gazı: pH 7.21, HCO3 11 mEq/L, BE -14 '
                                         '(ciddi metabolik asidoz). Elektrolitler: Na 116 mEq/L (ağır hiponatremi), K '
                                         '7.6 mEq/L (ağır hiperkalemi), Klor 86 mEq/L. EKG: Sivri ve yüksek T '
                                         'dalgaları, PR uzaması (hiperkalemi bulguları). Hormon: 17-OH Progesteron >50 '
                                         'ng/mL (belirgin yüksek), Kortizol çok düşük (<1 µg/dL), ACTH belirgin '
                                         'yüksek.'},
                         {'text': 'Sadece kontrastlı kraniyal tomografi ve üst gastrointestinal sistem floroskopik '
                                  'pasaj grafisi çektirmek',
                          'is_correct': False,
                          'scenario_update': 'Elektrolitlerin ölçülmemesi ölümcül hiperkalemiye bağlı ventriküler '
                                             'taşikardiye yol açtı.',
                          'teaching_point': 'Kusan yenidoğanda kan şekeri ve elektrolitler (Na, K) ilk bakılması '
                                            'gereken testtir.'},
                         {'text': 'Gaitada gizli kan, kalprotektin ve ter testi isteyerek elektrolit ölçümünü gün '
                                  'sonuna ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Hiperkalemik kardiyotoksisite fark edilemedi ve aritmi gelişti.',
                          'teaching_point': 'Hiponatremi ve hiperkalemi birlikteliği tuz kaybettiren sendrom için acil '
                                            'uyarı sinyalidir.'},
                         {'text': 'Acil kemik iliği aspirasyonu ve kas biyopsisi planlayarak metabolik incelemeleri '
                                  'tamamen dışlamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz biyopsiler hipovolemik şoku geri dönüşsüz aşamaya sürükledi.',
                          'teaching_point': 'Endokrin krizlerde hızlı kan gazı ve elektrolit tayini hayat kurtarır.'}]},
            {'stage_title': 'Ayırıcı Tanı ve Nihai Tanının Belirlenmesi',
             'question': 'Hiponatremi, hiperkalemi, hipoglisemi, şok ve klitoromegali birlikteliğinde kesin tanı '
                         'nedir?',
             'options': [{'text': 'Akut Tuz Kaybettiren Adrenal Kriz',
                          'is_correct': True,
                          'explanation': 'Kusma, ağır dehidratasyon, hiponatremi (Na 116), hiperkalemi (K 7.6), '
                                         'hipoglisemi ve kız bebekte virilizasyon Konjenital Adrenal Hiperplaziye '
                                         'bağlı tuz kaybettiren adrenal krizin klasik tablosudur.',
                          'new_finding': 'Kesin Tanı: Konjenital Adrenal Hiperplaziye Bağlı Akut Tuz Kaybettiren '
                                         'Adrenal Kriz doğrulanmıştır. Hastaya ve ailesine durum açıklanarak Sarı Alan '
                                         'acil tedavi protokolüne geçildi.'},
                         {'text': 'İnfantil Hipertrofik Pilor Stenozu',
                          'is_correct': False,
                          'scenario_update': 'Pilor stenozunda hipokalemik, hipokloremik metabolik alkaloz görülür; '
                                             "KAH'ta ise hiperkalemik asidoz vardır.",
                          'teaching_point': 'Pilor stenozunda potasyum düşüktür; hiperkalemi varsa adrenal kriz '
                                            'düşünülmelidir.'},
                         {'text': 'Bakteriyel Sepsis Hipovolemik Şok',
                          'is_correct': False,
                          'scenario_update': 'Sepsis virilizasyon ve izole tuz kaybı tablosunu açıklayamaz.',
                          'teaching_point': 'Genital ambigius ve hiperpigmentasyon adrenal patolojinin somut '
                                            'kanıtlarıdır.'},
                         {'text': 'Konjenital Hirschsprung Enterokolit Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Hirschsprung enterokolitinde mekonyum çıkışı gecikmesi ve toksik '
                                             'megakolon ön plandadır.',
                          'teaching_point': 'İzole kusma ve tuz kaybı endokrinolojik enzim eksikliğini işaret eder.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Ağır hiponatremi, hiperkalemi ve şok tablosundaki bu bebekte Sarı Alandaki en kritik acil '
                         'tedavi nedir?',
             'options': [{'text': 'İntravenöz potasyumsuz serum fizyolojik ve dekstroz ile hidrokortizon uygulamak, '
                                  'EKG takibiyle yoğun bakıma yatırmak',
                          'is_correct': True,
                          'explanation': 'İlk adım şoku düzeltmek için 20 mL/kg SF bolusudur (asla potasyum içeren '
                                         'sıvı verilmez!). Hipoglisemi için %10 Dekstroz verilir. Hayati adım: Acil İV '
                                         "Hidrokortizon (25 mg puşe, ardından 50-100 mg/m²/gün) uygulanmasıdır. EKG'de "
                                         "sivri T dalgaları için gerekirse İV Kalsiyum Glukonat verilir ve YBÜ'ye "
                                         'yatırılır.',
                          'new_finding': 'Acil damar yolu açıldı; 20 mL/kg intravenöz Serum Fizyolojik (%0.9 NaCl) ve '
                                         '%10 Dekstroz (2 mL/kg) puşe yapıldı. Acil İntravenöz Hidrokortizon (25 mg) '
                                         "uygulandı. EKG'deki sivri T dalgaları nedeniyle kardiyak membran "
                                         'stabilizasyonu için %10 Kalsiyum Glukonat (0.5 mL/kg) yavaş İV verildi. Kan '
                                         "basıncı 74/46 mmHg'ye yükseldi, KDZ 2 saniyeye indi. Hasta pediatrik yoğun "
                                         'bakım ünitesine (PYBÜ) devredildi.'},
                         {'text': 'Potasyum eksikliği düşünerek hastaya acil intravenöz yüksek doz potasyum klorür '
                                  'infüzyonu başlatıp taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Zaten 7.6 olan potasyuma ek potasyum verilmesi hastada ventriküler '
                                             'fibrilasyon ve arrest doğurdu.',
                          'teaching_point': 'Adrenal krizde potasyum aşırı yüksektir; potasyum içeren sıvılar '
                                            'kesinlikle kontrendikedir.'},
                         {'text': 'Kusmayı durdurmak için hastaya yüksek doz metoklopramid enjekte edip cerrahi '
                                  'pilorotomi ameliyatına almak',
                          'is_correct': False,
                          'scenario_update': 'Metabolik kriz düzeltilmeden ameliyata alınan bebekte anestezi '
                                             'indüksiyonunda kardiyak kollaps gelişti.',
                          'teaching_point': 'Adrenal kriz medikal resüsitasyon gerektirir; cerrahi yaklaşım '
                                            'ölümcüldür.'},
                         {'text': 'Durumun geçici olduğunu söyleyerek hiçbir sıvı ve steroid vermeden sadece anne '
                                  'sütüyle beslenmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Tedavisiz kalan dehidratasyon ve şok bebeğin kaybedilmesine yol açtı.',
                          'teaching_point': 'Tuz kaybettiren kriz acil intravenöz izotonik sıvı ve hidrokortizon '
                                            'verilmezse ölümcüldür.'}]}]},
 {'id': 'Y70',
  'category': '💊 Toksikoloji & Metabolik / Endokrin Aciller',
  'age': '11 Yaşında',
  'gender': 'Kız',
  'complaint': 'Kış sabahı sobalı evde uyandıktan sonra zonklayıcı baş ağrısı, bulantı, baş dönmesi ve bayılma',
  'history': "On bir yaşındaki kız çocuk Sarı Alana sedye ile getiriliyor: 'Kış gecesi köy evimizde kömür sobasını "
             'yakıp yattık. Sabah uyandığımızda kızımızın başı çok şiddetli zonkluyordu. Yataktan kalkmaya çalışırken '
             'başı dönüp yere yığıldı, kısa süreli baygınlık geçirdi. Sürekli öğürüyor ve kusuyor. Anne ve babasında '
             'da hafif baş ağrısı ve halsizlik var. Çocuk son derece bitkin, uykuya meyilli ve sorduğumuz sorulara '
             "güçlükle yanıt veriyor.'",
  'final_diagnosis': 'Akut Karbonmonoksit İntoksikasyonu (Soba Zehirlenmesi / Dokusal Hipoksi ve Hipoksemi)',
  'disposition': 'Sarı Alanda Rezervuarlı Maske ile %100 Yüksek Akım Oksijen Tedavisi, EKG/Kardiyak Takip ve Gerekirse '
                 'Hiperbarik O2 Sevk',
  'case_pearl': "Karbonmonoksit (CO) renksiz, kokusuz, tatsız ve irritan olmayan bir gazdır ('sessiz katil'). "
                'PATOFİZYOLOJİ: Hemoglobine afinitesi oksijenden 200-250 kat daha fazladır; karboksihemoglobin (CO-Hb) '
                'oluşturur. Oksihemoglobin dissosiasyon eğrisini sola kaydırarak dokulara oksijen sunumunu felce '
                'uğratır; hücresel hipoksi ve sitokrom oksidaz inhibisyonu yapar. HAYATİ TUZAK: STANDART PULSE '
                'OKSİMETRE (SpO2) YANILGISI! Standart pulse oksimetreler oksihemoglobin ile karboksihemoglobini AYIRT '
                'EDEMEZ ve hastayı YALANCI NORMAL (%98-100) gösterir! TANI: Arteriyel veya venöz kan gazında '
                'KO-OKSİMETRE ile CO-Hb düzeyinin ölçülmesidir (sigara içmeyende >%3-5, maruziyette >%10 '
                'patolojiktir). TEDAVİ: Rezervuarlı geri solumasız maske ile DERHAL %100 NORMOBARİK OKSİJEN (12-15 '
                'L/dk) başlanmalıdır. Oksijen yarı ömrü oda havasında 320 dakika iken, %100 O2 ile 60-80 dakikaya, '
                'Hiperbarik O2 (HBO) ile 20-30 dakikaya iner. HİPERBARİK OKSİJEN ENDİKASYONLARI: Bilinç kaybı/senkop '
                'öyküsü, nörolojik defisit, iskemik EKG değişikliği veya troponin yüksekliği, ciddi metabolik asidoz '
                'veya CO-Hb >%25 (gebede >%15).',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene Bulguları',
             'question': 'Sobalı evde uyandıktan sonra senkop ve baş ağrısıyla getirilen bu çocukta ilk odaklanılması '
                         'gerekenler nelerdir?',
             'options': [{'text': 'Vital bulguları, nörolojik durumunu, bilinç düzeyini, kardiyak ritmini ve pulse '
                                  'oksimetre yanılgısını değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Nörolojik durum (senkop, konfüzyon), kardiyak iskemi belirtileri ve standart '
                                         'pulse oksimetrenin yalancı normal (%99) olabileceği gerçeği göz önünde '
                                         'bulundurularak vital bulgular tam taranmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 116/dk (sinüzal taşikardi), SS 22/dk, SpO2 '
                                         '%99 (oda havasında standart pulse oksimetre ile yalancı normal!), TA 106/68 '
                                         'mmHg, KDZ 2 sn. Fizik Muayene: Bilinç konfüze, Glaskow Koma Skoru 13 '
                                         "(E3M6V4), letarjik ve bitkin. Ciltte klasik 'kiraz kırmızısı' renk "
                                         'görülmüyor (kitabi bir bulgudur, pratikte nadiren görülür). Pupiller '
                                         'izokorik, ışık refleksi bilateral mevcut, ense sertliği yok. Kardiyak sesler '
                                         'taşikardik, üfürüm yok.'},
                         {'text': 'Sadece batın ultrasonografisi çekerek apandisit ve mezenterik lenfadenit varlığına '
                                  'odaklanıp nörolojiyi ihmal etmek',
                          'is_correct': False,
                          'scenario_update': 'Sobalı evde toplu zehirlenme öyküsü atlandı; serebral hipoksi '
                                             'derinleşti.',
                          'teaching_point': 'Sobalı ortamda senkop ve baş ağrısı toksik gaz zehirlenmesini akla '
                                            'getirmelidir.'},
                         {'text': 'Hastanın baş ağrısını migren kabul edip hiçbir değerlendirme yapmadan karanlık '
                                  'odaya alıp uyutmak',
                          'is_correct': False,
                          'scenario_update': 'Hipoksik beyin hasarı ilerledi ve hasta derin komaya girdi.',
                          'teaching_point': 'Birden fazla aile bireyinde eş zamanlı baş ağrısı ve bulantı çevresel '
                                            'toksisite kanıtıdır.'},
                         {'text': 'Acil kulak burun boğaz konsültasyonu ile timpanometri yaparak kulak zarı basıncını '
                                  'incelemeye çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz kulak muayenesi oksijen tedavisinin gecikmesine neden oldu.',
                          'teaching_point': 'Senkop ve letarji ile başvuran hastada öncelik vital fonksiyonlar ve doku '
                                            'oksijenasyonudur.'}]},
            {'stage_title': 'Laboratuvar İncelemeleri ve Ko-Oksimetre Analizi',
             'question': 'Sobalı ortamda senkop öyküsü ve konfüzyonu olan çocukta tanıyı doğrulamak için hangi acil '
                         'tetkikler istenmelidir?',
             'options': [{'text': 'Ko-oksimetreli kan gazında gaz intoksikasyon paneli, elektrokardiyografi, kardiyak '
                                  'enzimler ve biyokimya istemek',
                          'is_correct': True,
                          'explanation': 'Standart kan gazı yetersizdir; ko-oksimetreli kan gazında CO-Hb düzeyi '
                                         'ölçülmelidir. Miyokardiyal doku hipoksisini ve iskemiyi taramak için EKG ve '
                                         'troponin düzeyleri mutlaka görülmelidir.',
                          'new_finding': 'Kan Gazı (Ko-oksimetre): pH 7.32, pCO2 34 mmHg, pO2 88 mmHg, HCO3 17 mEq/L, '
                                         'Laktat 3.8 mmol/L. Gaz Satürasyonu (CO-Hb): %28.4 (ağır toksik maruziyet '
                                         'düzeyi, normal sigara içmeyende <%2). Troponin I: 0.01 ng/mL (normal). EKG: '
                                         'Sinüzal taşikardi (116/dk), ST depresyonu veya iskemi saptanmadı.'},
                         {'text': 'Sadece direkt ayak bileği grafisi ve kanda romatoid faktör düzeyi gönderip beklemek',
                          'is_correct': False,
                          'scenario_update': 'Doku hipoksisi değerlendirilemedi ve kardiyak komplikasyon riski arttı.',
                          'teaching_point': 'Gaz intoksikasyonlarında tanı ko-oksimetre ile kanda gaz düzeyinin '
                                            'saptanmasıdır.'},
                         {'text': 'Gaitada parazit mikroskopisi ve ter testi isteyerek kan gazı analizinden kaçınmak',
                          'is_correct': False,
                          'scenario_update': 'Kandaki yüksek toksik gaz düzeyi saptanamadı ve tedaviye başlanamadı.',
                          'teaching_point': 'Senkop ve baş ağrısında acil kan gazı ve metabolik asidoz taraması '
                                            'esastır.'},
                         {'text': 'Hastaya acil baryumlu kolon grafisi çekerek bağırsak pasajını floroskopiyle izlemek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz radyolojik floroskopi hastanın genel durumunu daha da bozdu.',
                          'teaching_point': 'Hücresel asfiksi yapan gaz zehirlenmesinde gastrointestinal kontrast '
                                            'grafisinin yeri yoktur.'}]},
            {'stage_title': 'Ayırıcı Tanı ve Nihai Tanının Belirlenmesi',
             'question': 'Sobalı odada toplu semptom, senkop, konfüzyon ve kanda yüksek toksik gaz saptanan hastada '
                         'kesin klinik tanı nedir?',
             'options': [{'text': 'Akut Karbonmonoksit Gaz İntoksikasyonu Tablosu',
                          'is_correct': True,
                          'explanation': 'Sobalı ortamda maruziyet, senkop öyküsü, konfüzyon, metabolik asidoz ve '
                                         'kanda CO-Hb düzeyinin %28.4 saptanması Akut Karbonmonoksit İntoksikasyonunu '
                                         'kesinleştirir.',
                          'new_finding': 'Kesin Tanı: Akut Karbonmonoksit Gaz İntoksikasyonu doğrulanmıştır. Hastaya '
                                         've ailesine durum açıklanarak Sarı Alan acil tedavi protokolüne geçildi.'},
                         {'text': 'Akut Besin Zehirlenmesi Gastroenteriti',
                          'is_correct': False,
                          'scenario_update': 'Besin zehirlenmesinde senkop, konfüzyon ve ko-oksimetrede gaz yüksekliği '
                                             'görülmez.',
                          'teaching_point': 'Kusma ve bulantı tek başına gastroenterit değildir; hipoksik ensefalopati '
                                            'bulgusu olabilir.'},
                         {'text': 'Çocukluk Çağı Aurasız Migren',
                          'is_correct': False,
                          'scenario_update': 'Migren aynı odada kalan aile bireylerinde eş zamanlı semptom ve kanda '
                                             'gaz yüksekliği yapmaz.',
                          'teaching_point': 'Kolektif baş ağrısı ve senkop çevresel toksisitenin en belirgin '
                                            'işaretidir.'},
                         {'text': 'Akut Bakteriyel Menenjit Enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Menenjitte yüksek ateş ve ense sertliği vardır; kanda toksik gaz düzeyi '
                                             'saptanmaz.',
                          'teaching_point': 'Ateşsiz senkop ve baş ağrısında toksik inhalasyon etiyolojisi ön '
                                            'plandadır.'}]},
            {'stage_title': 'Tedavi Protokolü ve Klinik Yönetim',
             'question': 'Senkop öyküsü ve CO-Hb %28.4 saptanan bu hastada Sarı Alandaki en uygun acil tedavi '
                         'yaklaşımı nedir?',
             'options': [{'text': 'Rezervuarlı geri solumasız maskeyle yüzde yüz oksijen vermek, nörolojik takip '
                                  'yapmak ve hiperbarik oksijen merkezine danışmak',
                          'is_correct': True,
                          'explanation': 'Tedavinin temeli rezervuarlı maske ile %100 normobarik oksijendir (12-15 '
                                         'L/dk). Bu uygulama CO yarı ömrünü 320 dakikadan 80 dakikaya indirir. Hastada '
                                         'senkop (bilinç kaybı) öyküsü ve CO-Hb >%25 olması kesin Hiperbarik Oksijen '
                                         '(HBO) endikasyonudur; bölge HBO merkeziyle temasa geçilmelidir.',
                          'new_finding': 'Hastaya derhal rezervuarlı geri solumasız maske takılarak 15 L/dk akımla '
                                         '%100 Oksijen tedavisi başlatıldı. Senkop öyküsü ve CO-Hb %28.4 olması '
                                         'nedeniyle Hiperbarik Oksijen Tedavisi (HBOT) merkezine danışıldı. Oksijen '
                                         'tedavisinin 2. saatinde hastanın baş ağrısı geriledi, bilinci tamamen açıldı '
                                         "(GKS 15). Kontrol kan gazında CO-Hb %4.8'e geriledi. Nörolojik sekeller ve "
                                         'kardiyak ritim açısından gözlem servisine yatırıldı.'},
                         {'text': 'Pulse oksimetrede oksijen satürasyonu yüzde doksan dokuz olduğu için hastaya hiçbir '
                                  'oksijen desteği vermemek',
                          'is_correct': False,
                          'scenario_update': 'Standart oksimetreye aldanılıp oksijen verilmemesi doku iskemisini ve '
                                             'nörolojik hasarı kalıcı kıldı.',
                          'teaching_point': 'Pulse oksimetrenin yalancı normal değeri CO zehirlenmesinde en ölümcül '
                                            'tuzaktır; oksijen şarttır.'},
                         {'text': 'Hastanın baş ağrısını geçirmek için hemen genel anestezi verip acil dekompresif '
                                  'kraniyotomi ameliyatı planlamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz beyin ameliyatı hipoksik hastada masif kanama ve arrest '
                                             'doğurdu.',
                          'teaching_point': 'Zehirlenme medikal bir tablodur; antidotu %100 oksijen ve hiperbarik '
                                            'oksijendir.'},
                         {'text': 'Zehirlenmeyi gidermek amacıyla hastaya yüksek doz oral aktif kömür içirip evine '
                                  'istirahate göndermek',
                          'is_correct': False,
                          'scenario_update': 'İnhalasyon zehirlenmesinde aktif kömür etkisizdir; letarjik hastada '
                                             'aspirasyon pnömonisi gelişti.',
                          'teaching_point': 'Solunum yoluyla alınan gazlarda aktif kömürün hiçbir yeri yoktur; tedavi '
                                            'solunum yoluyla oksijendir.'}]}]}]
