# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Sarı Alan Vakaları (Part 10: S91 - S100)
"""

YELLOW_CASES_PART10 = [{'id': 'S91',
  'category': '🫁 Hırıltı & Solunum Sıkıntısı',
  'age': '7 Haftalık (4.4 kg)',
  'gender': 'Kız',
  'complaint': 'On gündür artan öksürük nöbetleri, nöbet sonrası morarma ve bugün bir kez nefesinin durması',
  'history': "Annesi anlatıyor: 'İlk günlerde biraz burnu aktı, hafif öksürüyordu. Sonra öksürükleri nöbet nöbet oldu; "
             'art arda öksürüyor, kıpkırmızı sonra mosmor oluyor, sonunda kusuyor. Nöbetler arasında gayet iyi, '
             "gülüyor. Bugün öksürük nöbetinden sonra nefesi durdu, sallayınca düzeldi.' Ateşi hiç olmamış. Henüz aşı "
             'olmamış (2. ay aşıları önümüzdeki hafta). Annenin ve babanın üç haftadır geçmeyen öksürüğü var, '
             'babanınki geceleri kusma yaptıracak kadar şiddetli. Anne gebelikte aşı olmamış.',
  'final_diagnosis': 'Boğmaca (Bordetella pertussis) - Apne ve Siyanozla Seyreden Genç Süt Çocuğu',
  'disposition': 'Damlacık İzolasyonunda Apne Monitörizasyonu, Azitromisin ve Temaslı Profilaksisiyle Pediatri '
                 'Servisine (Gerekirse Yoğun Bakıma) Yatış',
  'case_pearl': 'Aşısız veya eksik aşılı genç süt çocuklarında en ağır seyreden form görülür. Tipik çocukta kataral '
                'dönemden sonra paroksismal öksürük nöbetleri, nöbet sonrası kusma ve siyanoz gelişir; genç bebeklerde '
                "'kükreme' sesi olmayabilir, apne tek bulgu olabilir. Nöbetler arasında bebek iyi görünür ve ateş "
                'yoktur. Belirgin lenfositoz tipiktir; çok yüksek lökosit sayısı (>30.000/mm³) pulmoner hipertansiyon '
                've ölüm riskini gösterir. Tanı nazofaringeal sürüntüde PCR ile konur. Bir aydan küçüklerde ve tüm '
                'genç bebeklerde azitromisin tercih edilir. Hane içi tüm temaslılara profilaksi verilir. Gebelikte '
                'Tdap aşısı bebekleri korur.',
  'steps': [{'stage_title': 'İlk Değerlendirme',
             'question': 'Öksürük nöbetleri ve apne öyküsü olan bu bebekte ilk yaklaşımınız nedir?',
             'options': [{'text': 'Nöbetler arasında iyi göründüğü için ağızdan sıvı ve öksürük şurubu önerip aşı '
                                  'randevusuna kadar evde izlemelerini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Bebek evde uzun bir apne geçirdi ve kardiyopulmoner resüsitasyon '
                                             'gerektirdi.',
                          'teaching_point': 'Apne öyküsü olan genç süt çocuğu monitörize edilerek hastanede '
                                            'izlenmelidir.'},
                         {'text': 'Damlacık izolasyonunda monitöre ve pulse oksimetreye bağlamak, bir öksürük nöbetini '
                                  'gözlemlemek ve solunum ile beslenmeyi değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Öksürük nöbetinin doğrudan gözlemlenmesi tabloyu netleştirir. İzolasyon '
                                         'diğer bebekleri korur, monitör apne ve desatürasyonu yakalar.',
                          'new_finding': 'Nöbetler arasında: ateş 36.8°C, KTA 148/dk, SS 40/dk, SpO2 %98, solunum '
                                         'sıkıntısı yok, akciğerler temiz. Gözlenen nöbette art arda 15-20 kısa '
                                         "öksürük, yüz kızarıp morardı, SpO2 %72'ye düştü, ardından 12 saniye apne ve "
                                         'bradikardi (80/dk), sonunda kusma oldu. Uyarıyla düzeldi. Konjonktivalarda '
                                         'subkonjonktival kanama. Beslenme sırasında yorulma.'},
                         {'text': 'Hışıltısı olmasa da bronşiolit kabul edip salbutamol ve adrenalin nebülü vermek, '
                                  'nöbetler geçerse taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Nebüller öksürük nöbetlerini etkilemedi; bebek gece ağır bir apne '
                                             'geçirdi.',
                          'teaching_point': 'Nöbetler arasında temiz akciğer ve paroksismal öksürük bu tabloyu '
                                            'bronşiolitten ayırır.'},
                         {'text': 'Morarma nedeniyle doğuştan kalp hastalığı kabul edip yalnızca ekokardiyografi '
                                  'istemek ve kardiyoloji görüşünü beklemek',
                          'is_correct': False,
                          'scenario_update': 'Bekleme süresinde izolasyon yapılmadı; bekleme alanında başka bir bebek '
                                             'temaslı oldu.',
                          'teaching_point': 'Morarma öksürük nöbetiyle ilişkiliyse solunum yolu kaynaklıdır; önce '
                                            'izolasyon ve monitörizasyon gerekir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Bu bebekte hangi tetkikler en uygundur?',
             'options': [{'text': 'Tam kan sayımı ile nazofaringeal sürüntüden PCR göndermek; akciğer grafisi çekmek '
                                  've ekokardiyografiyi planlamak',
                          'is_correct': True,
                          'explanation': 'Lenfositoz tanıyı destekler, çok yüksek lökosit sayısı ağır seyri öngörür. '
                                         'PCR tanıyı doğrular. Ekokardiyografi pulmoner hipertansiyonu değerlendirir.',
                          'new_finding': 'Lökosit 34.600/mm³ (%76 lenfosit), trombosit 612.000/mm³, CRP 4 mg/L. '
                                         'Akciğer grafisinde kalp kenarlarında tüylü görünüm, konsolidasyon yok. '
                                         'Nazofaringeal PCR pozitif. Ekokardiyografide pulmoner basınç hafif yüksek.'},
                         {'text': 'Nöbetler epileptik olabileceği için acil EEG ve beyin ultrasonografisi istemek, '
                                  'sonuçlarına göre antiepileptik başlamak',
                          'is_correct': False,
                          'scenario_update': 'EEG normal geldi; asıl tanı gecikti.',
                          'teaching_point': 'Morarma ve apne öksürük nöbetiyle birlikteyse nedeni solunumsaldır.'},
                         {'text': 'Sepsis kuşkusuyla lomber ponksiyon, kan ve idrar kültürü yapıp sonuçlar gelene '
                                  'kadar ampisilin ve sefotaksim başlamak',
                          'is_correct': False,
                          'scenario_update': 'Ateşsiz ve nöbetler arasında iyi görünen bebekte gereksiz girişimler '
                                             'yapıldı.',
                          'teaching_point': 'Tetkikler klinik tabloya göre seçilir; bu bebekte ateş ve sepsis bulgusu '
                                            'yoktur.'},
                         {'text': 'Yalnızca boğaz kültürü almak ve sonucu bir hafta sonra değerlendirmek üzere bebeği '
                                  'taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Boğaz kültürü bu etken için uygun örnek değildi ve bebek evde kötüleşti.',
                          'teaching_point': 'Tanı nazofaringeal örnekten PCR ile konur; apneli bebek taburcu '
                                            'edilmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Akut bronşiolit',
                          'is_correct': False,
                          'scenario_update': 'Nöbetler arasında akciğerler temiz, solunum sıkıntısı yoktu ve belirgin '
                                             'lenfositoz vardı.',
                          'teaching_point': 'Bronşiolitte sürekli takipne, raller ve hışıltı vardır.'},
                         {'text': 'Klamidya pnömonisi',
                          'is_correct': False,
                          'scenario_update': 'Konjonktivit öyküsü ve kesik kesik öksürük yoktu, eozinofili saptanmadı.',
                          'teaching_point': 'Klamidya pnömonisinde staccato öksürük, takipne ve eozinofili görülür.'},
                         {'text': 'Boğmaca (pertussis)',
                          'is_correct': True,
                          'explanation': 'Aşısız genç bebekte kataral dönemi izleyen paroksismal öksürük, nöbet '
                                         'sonrası siyanoz, apne ve kusma, nöbetler arası iyilik, ateş olmaması, '
                                         'belirgin lenfositoz, uzun süre öksüren ebeveynler ve PCR pozitifliği '
                                         'boğmacayı gösterir.',
                          'new_finding': 'Tanı: Boğmaca (Bordetella pertussis).'},
                         {'text': 'Gastroözofageal reflü hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Kusma öksürük nöbetlerinden sonra geliyordu ve lenfositoz vardı.',
                          'teaching_point': 'Reflüde kusma beslenmeyle ilişkilidir, öksürük nöbetleri ve lenfositoz '
                                            'beklenmez.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu bebek ve ailesi için en uygun plan hangisidir?',
             'options': [{'text': 'Öksürük nöbetlerini azaltmak için oral kortikosteroid ve salbutamol şurubu başlayıp '
                                  'antibiyotiği gereksiz bulmak',
                          'is_correct': False,
                          'scenario_update': 'Nöbetler azalmadı ve bebek bulaştırıcı kalmaya devam etti.',
                          'teaching_point': 'Bu ilaçların öksürük nöbetlerine etkisi gösterilmemiştir; antibiyotik '
                                            'bulaştırıcılığı azaltır.'},
                         {'text': 'Bebeğe beş gün azitromisin başlamak, monitörle yatırmak ve hane içi tüm temaslılara '
                                  'profilaktik antibiyotik vermek',
                          'is_correct': True,
                          'explanation': 'Azitromisin bu yaşta güvenle kullanılır ve bulaştırıcılığı azaltır. Temaslı '
                                         'profilaksisi hane içindeki yeni olguları önler. Yüksek lökosit nedeniyle '
                                         'yoğun bakımla iletişim sürdürülür.',
                          'new_finding': 'Azitromisin başlandı, anne, baba ve kardeşe profilaksi verildi, olgu '
                                         "bildirildi. Lökosit 41.000/mm³'e yükselince yoğun bakıma alındı; öksürük "
                                         'nöbetleri iki hafta içinde azaldı ve bebek dördüncü haftada taburcu edildi.'},
                         {'text': 'Bebeğe hemen ilk doz aşısını yapıp antibiyotik vermeden taburcu etmek ve ailenin '
                                  'öksürüğünü önemsememek',
                          'is_correct': False,
                          'scenario_update': 'Aşı mevcut hastalığı tedavi etmedi; ailede yeni olgular gelişti.',
                          'teaching_point': 'Aşı hastalığı tedavi etmez; temaslılar profilaksi almalıdır.'},
                         {'text': 'Yalnızca bebeği tedavi edip anne ve babanın öksürüğünü viral kabul ederek '
                                  'profilaksi vermemek',
                          'is_correct': False,
                          'scenario_update': 'Bulaş kaynağı olan ebeveynler tedavi edilmedi ve yeni doğan kuzenine '
                                             'hastalık bulaştı.',
                          'teaching_point': 'Genç bebeklerde kaynak çoğunlukla aile bireyleridir; tüm hane profilaksi '
                                            'almalıdır.'}]}]},
 {'id': 'S92',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '2 Yaşında (10.5 kg)',
  'gender': 'Erkek',
  'complaint': 'İki haftadır düşük dereceli ateş, iştahsızlık ve huzursuzluk; son iki gündür aşırı uyku hali ve kusma',
  'history': "Annesi anlatıyor: 'İki haftadır ateşi 38 civarında, hiç iştahı yok, kilo verdi. Hep huzursuz, ağlıyor. "
             "İki gündür sürekli uyuyor, kusuyor, bugün sol gözü kaydı.' İki kez farklı merkezlerde 'viral enfeksiyon' "
             'tanısı almış. Aile kalabalık bir evde yaşıyor. Dedesinin birkaç aydır kanlı balgamlı öksürüğü varmış ve '
             "'akciğer' tedavisi başlanmış. Çocuğun BCG skarı yok, aşıları eksik. Kafa travması yok.",
  'final_diagnosis': 'Tüberküloz Menenjit (Evre 2) ve Hidrosefali',
  'disposition': 'Dörtlü Antitüberküloz Tedavi ve Deksametazon Başlanarak Çocuk Enfeksiyon ve Beyin Cerrahisi '
                 'İzlemiyle Yatış; Bildirim ve Temaslı Taraması',
  'case_pearl': "Özellikle 5 yaş altında, BCG'siz ve erişkin olgu ile teması olan çocuklarda görülür. Haftalara "
                'yayılan sinsi başlangıç (ateş, iştahsızlık, huzursuzluk), ardından bilinç değişikliği, kusma ve '
                "kranial sinir felçleri (en sık 6. sinir) tipiktir. BOS'ta lenfosit baskın pleositoz, belirgin protein "
                'artışı ve düşük glukoz görülür. Görüntülemede bazal meninkslerde kontrastlanma, hidrosefali ve '
                'infarktlar olabilir. Tanı beklenmeden dörtlü tedavi (izoniazid, rifampisin, pirazinamid, etambutol '
                'veya etiyonamid) ve deksametazon başlanır. Erişkin kaynak olgunun ilaç duyarlılığı tedavi seçiminde '
                'önemlidir. Olgu bildirilir ve tüm temaslılar taranır.',
  'steps': [{'stage_title': 'İlk Değerlendirme',
             'question': 'Haftalardır süren ateş ve yeni gelişen bilinç değişikliği olan bu çocukta ilk '
                         'değerlendirmeniz nedir?',
             'options': [{'text': 'Daha önce viral enfeksiyon dendiği için ateş düşürücü ve antiemetikle izleyip '
                                  'uykululuğu ateşe bağlamak',
                          'is_correct': False,
                          'scenario_update': 'Çocuk gece nöbet geçirdi ve bilinci daha da kötüleşti.',
                          'teaching_point': 'Uzamış ateş ve yeni bilinç değişikliği merkezi sinir sistemi enfeksiyonu '
                                            'açısından değerlendirilmelidir.'},
                         {'text': 'Hava yolu ve kan şekerini kontrol edip bilinç, pupiller, kranial sinirler ve '
                                  'menenjit bulgularını değerlendirmek, temas öyküsünü sormak',
                          'is_correct': True,
                          'explanation': 'Bilinç değişikliği ve kranial sinir tutulumu kafa içi basınç artışını ve '
                                         'bazal meninks tutulumunu düşündürür. Ailede uzun süreli öksürüğü olan bir '
                                         'erişkin önemli bir ipucudur.',
                          'new_finding': 'Ateş 38.3°C, KTA 128/dk, KB 104/68 mmHg, SS 28/dk. Kan şekeri 92 mg/dL. GKS '
                                         '11. Ense sertliği belirgin, Kernig pozitif. Sol gözde dışa bakış '
                                         'kısıtlılığı. Pupiller eşit, ışık yanıtı var. Fundus muayenesinde hafif '
                                         'papilödem. Tartı yaşına göre 10. persentilin altında. BCG skarı yok. '
                                         'Akciğerlerde ince raller.'},
                         {'text': 'Huzursuzluk ve kusma nedeniyle intussusepsiyon kabul edip karın ultrasonografisi '
                                  'isteyip nörolojik muayeneyi ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografi normal geldi ve nörolojik değerlendirme gecikti.',
                          'teaching_point': 'Ense sertliği ve kranial sinir felci olan çocukta önce nörolojik '
                                            'değerlendirme yapılır.'},
                         {'text': 'Hemen lomber ponksiyon yapıp sonuçlara göre tedavi kararını vermek ve bu sürede '
                                  'tedavi başlamamak',
                          'is_correct': False,
                          'scenario_update': 'Papilödem ve kranial sinir felci olan çocukta görüntülemesiz ponksiyon '
                                             'herniasyon riskini artırdı.',
                          'teaching_point': 'Kafa içi basınç artışı bulgularında ponksiyondan önce görüntüleme '
                                            'yapılır.'}]},
            {'stage_title': 'Görüntüleme ve BOS Değerlendirmesi',
             'question': 'Görüntüleme ve BOS sonuçları aşağıdaki gibidir. Bu bulgular hangi tabloyla en uyumludur?',
             'options': [{'text': "BOS'ta nötrofil baskın 4.000/mm³ hücre, çok düşük glukoz; BT'de normal ventriküller "
                                  've konveksite meninkslerinde kontrastlanma',
                          'is_correct': False,
                          'scenario_update': 'Hastanın sonuçları bu tabloyla uyumlu değildi.',
                          'teaching_point': 'Bu tablo akut bakteriyel menenjiti düşündürür; haftalara yayılan sinsi '
                                            'seyir beklenmez.'},
                         {'text': "BOS'ta lenfosit baskın 50-300/mm³ hücre, belirgin protein artışı, düşük glukoz; "
                                  "BT'de bazal kontrastlanma ve hidrosefali",
                          'is_correct': True,
                          'explanation': 'Lenfositik pleositoz, yüksek protein ve düşük glukoz birlikteliği ile bazal '
                                         'meninks tutulumu ve hidrosefali haftalara yayılan kronik granülomatöz '
                                         'menenjiti gösterir.',
                          'new_finding': 'Kontrastlı BT: Bazal sisternlerde yoğun kontrastlanma, lateral ve üçüncü '
                                         'ventriküllerde genişleme, sol bazal gangliyonda küçük infarkt. BOS (BT '
                                         'sonrası): lökosit 180/mm³ (%85 lenfosit), protein 260 mg/dL, glukoz 22 mg/dL '
                                         '(kan 92). ARB boyaması negatif, PCR ve kültür gönderildi. Akciğer grafisinde '
                                         'milier görünüm. Dedenin balgamında ARB pozitif.'},
                         {'text': "BOS'ta lenfosit baskın hafif pleositoz, normal glukoz ve eritrositler; MR'da tek "
                                  'taraflı temporal lob tutulumu',
                          'is_correct': False,
                          'scenario_update': 'Hastanın sonuçları bu tabloyla uyumlu değildi.',
                          'teaching_point': 'Bu tablo herpes ensefalitini düşündürür; akut başlangıç ve fokal nöbetle '
                                            'gelir.'},
                         {'text': "BOS tamamen normal, BT'de posterior fossada kontrast tutan kitle ve buna bağlı "
                                  'obstrüktif hidrosefali',
                          'is_correct': False,
                          'scenario_update': 'Hastanın sonuçları bu tabloyla uyumlu değildi.',
                          'teaching_point': 'Bu tablo bir kitle lezyonunu düşündürür; ateş ve meninks bulguları '
                                            'beklenmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Kısmen tedavi edilmiş bakteriyel menenjit',
                          'is_correct': False,
                          'scenario_update': 'Daha önce antibiyotik kullanılmamıştı, bazal tutulum, milier akciğer ve '
                                             'erişkin temaslı vardı.',
                          'teaching_point': 'Kısmen tedavi edilmiş menenjitte de lenfositoz görülebilir; öykü ve '
                                            'görüntüleme ayrımda önemlidir.'},
                         {'text': 'Tüberküloz menenjit ve hidrosefali',
                          'is_correct': True,
                          'explanation': "BCG'siz, aktif akciğer hastalığı olan dede ile temaslı çocukta haftalara "
                                         'yayılan sinsi başlangıç, altıncı sinir felci, lenfositik pleositoz, çok '
                                         'yüksek protein, düşük glukoz, bazal kontrastlanma, hidrosefali ve milier '
                                         'akciğer tüberküloz menenjiti gösterir.',
                          'new_finding': 'Tanı: Tüberküloz menenjit (evre 2) ve hidrosefali, milier tüberküloz.'},
                         {'text': 'Viral ensefalit',
                          'is_correct': False,
                          'scenario_update': 'Glukoz çok düşük ve protein çok yüksekti, bazal tutulum vardı.',
                          'teaching_point': 'Viral ensefalitte glukoz normaldir, protein hafif artar.'},
                         {'text': 'Kriptokok menenjiti',
                          'is_correct': False,
                          'scenario_update': 'Bilinen immün yetmezlik yoktu ve erişkin temaslının balgamında ARB '
                                             'vardı.',
                          'teaching_point': 'Kriptokok menenjiti büyük ölçüde immün yetmezlikli hastalarda görülür.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Kültür ve duyarlılık sonuçlarını beklemek için tedaviyi altı hafta ertelemek ve bu '
                                  'sürede seftriakson vermek',
                          'is_correct': False,
                          'scenario_update': 'Tedavi gecikince çocuk komaya girdi ve kalıcı nörolojik hasar gelişti.',
                          'teaching_point': 'Bu tanıda kültür beklenmeden tedavi başlanmalıdır; gecikme ölüm ve sekel '
                                            'riskini artırır.'},
                         {'text': 'Yalnızca izoniazid ve rifampisinle tedaviye başlamak ve kortikosteroid vermeden '
                                  'genel serviste izlemek',
                          'is_correct': False,
                          'scenario_update': 'İkili tedavi menenjit için yetersizdi; ödem ve hidrosefali ilerledi.',
                          'teaching_point': 'Merkezi sinir sistemi tutulumunda dörtlü tedavi ve kortikosteroid '
                                            'gerekir.'},
                         {'text': 'Dörtlü antitüberküloz tedavi ve deksametazon başlamak, hidrosefali için beyin '
                                  'cerrahisine danışmak, olguyu bildirip temaslıları taramak',
                          'is_correct': True,
                          'explanation': 'Erken dörtlü tedavi ve kortikosteroid ölüm ve sekel riskini azaltır. '
                                         'Hidrosefali drenaj gerektirebilir. Temaslı taraması diğer çocukları korur.',
                          'new_finding': 'İzoniazid, rifampisin, pirazinamid, etiyonamid ve deksametazon başlandı. '
                                         'Hidrosefali için ventriküloperitoneal şant takıldı. Dedenin suşu ilaçlara '
                                         'duyarlı çıktı. Evdeki diğer çocuklara koruyucu tedavi başlandı. Çocuk hafif '
                                         'sol hemiparezi ile yatışının altıncı haftasında taburcu edildi.'},
                         {'text': 'Ampirik antiviral ve antifungal tedavi başlayıp tanı doğrulanınca antitüberküloz '
                                  'tedaviyi eklemeyi düşünmek',
                          'is_correct': False,
                          'scenario_update': 'Gerekli tedavi gecikti ve çocuğun bilinci kötüleşti.',
                          'teaching_point': 'Klinik ve BOS bulguları güçlü şüphe oluşturduğunda antitüberküloz tedavi '
                                            'hemen başlanır.'}]}]},
 {'id': 'S93',
  'category': '🦴 Kas-İskelet & Eklem / Ortopedik Aciller',
  'age': '6 Yaşında (21 kg)',
  'gender': 'Erkek',
  'complaint': 'Dört gündür ateş ve sağ bacakta dizin altında giderek artan ağrı, bugün bacağına basamama',
  'history': "Annesi anlatıyor: 'Dört gün önce parkta düştü, dizinin altı hafifçe sıyrıldı. Sonraki gün ateşi çıktı, "
             "bacağı ağrımaya başladı. Ateşi 39'a çıkıyor, ağrı gece daha fazla. Bugün bacağına hiç basmıyor.' Başka "
             "bir merkezde 'kas zedelenmesi' denip ibuprofen verilmiş. Dizini hareket ettirebiliyor ama kaval kemiğine "
             'dokunulmasına izin vermiyor. Bilinen hastalığı yok, aşıları tam.',
  'final_diagnosis': 'Sağ Proksimal Tibia Akut Hematojen Osteomiyeliti (Metisiline Duyarlı Staphylococcus aureus)',
  'disposition': 'Kan Kültürü Sonrası İV Sefazolin ile Çocuk Ortopedi ve Enfeksiyon İzleminde Servise Yatış',
  'case_pearl': "Çocuklarda en sık uzun kemiklerin metafizinde (tibia, femur) görülür; en sık etken S. aureus'tur. "
                'Ateş, lokalize kemik hassasiyeti ve yük vermeyi reddetme tipiktir. Hafif bir travma öyküsü tanıyı '
                'yanıltabilir. Direkt grafi ilk iki haftada çoğu zaman normaldir; erken tanıda en duyarlı yöntem '
                "MR'dır. CRP ve sedimantasyon yüksektir, kan kültürü yaklaşık yarısında pozitiftir. Kültür alındıktan "
                'sonra antistafilokokal ampirik tedavi (sefazolin; MRSA yüksek bölgelerde klindamisin veya vankomisin) '
                'başlanır. Subperiostal apse cerrahi drenaj gerektirir. Klinik ve CRP düzelince oral tedaviye geçilir, '
                'toplam süre en az 3-4 haftadır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Ateşli ve bacağına basamayan bu çocukta muayenede neye odaklanırsınız?',
             'options': [{'text': 'Düşme öyküsü olduğu için kas zedelenmesi kabul edip yalnızca soğuk uygulama ve '
                                  'ibuprofen önerisiyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk üç gün sonra bacakta belirgin şişlik ve septik tabloyla getirildi.',
                          'teaching_point': 'Ateş ve yük vermeyi reddetme hafif travmayla açıklanmaz; enfeksiyon '
                                            'dışlanmalıdır.'},
                         {'text': 'Ağrının eklemden mi kemikten mi kaynaklandığını ayırmak için eklem hareketlerini ve '
                                  'kemik üzerindeki hassasiyeti değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Eklem hareketleri serbest olup kemik üzerinde lokalize hassasiyet olması '
                                         'kemik enfeksiyonunu, hareketle belirgin ağrı ve eklem sıvısı ise eklem '
                                         'enfeksiyonunu düşündürür.',
                          'new_finding': 'Ateş 39.1°C, KTA 126/dk, KB 100/64 mmHg, KDZ 2 sn. Sağ tibia proksimal '
                                         'metafizi üzerinde nokta hassasiyet, hafif ısı artışı ve ödem. Diz pasif '
                                         'hareketleri tam ve ağrısız, eklemde sıvı yok. Dizin altında iyileşmekte olan '
                                         'yüzeyel sıyrık. Kalça ve ayak bileği normal. Başka odak yok.'},
                         {'text': 'Diz ekleminde septik artrit kabul edip muayeneyi kısa tutarak hemen eklem '
                                  'aspirasyonu yapmak',
                          'is_correct': False,
                          'scenario_update': 'Eklemde sıvı yoktu; girişim gereksiz yere yapıldı.',
                          'teaching_point': 'Eklem hareketleri serbestse önce kemik kaynaklı enfeksiyon '
                                            'düşünülmelidir.'},
                         {'text': 'Gece artan kemik ağrısı nedeniyle doğrudan lösemi kabul edip kemik iliği '
                                  'aspirasyonu için onkolojiye sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'Kan sayımı ve görüntüleme yapılmadan sevk edildi; tedavi gecikti.',
                          'teaching_point': 'Ateşli lokalize kemik ağrısında önce enfeksiyon araştırılır; malignite '
                                            'kan sayımı ve yaymayla değerlendirilir.'}]},
            {'stage_title': 'Tetkik ve Görüntüleme',
             'question': 'Bu çocukta hangi tetkik ve görüntüleme yaklaşımı uygundur?',
             'options': [{'text': 'Yalnızca direkt grafi çekmek, grafi normalse kemik enfeksiyonunu dışlamak ve ağrı '
                                  'kesiciyle evde izlem önerip taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Normal grafi yanıltıcı oldu; tedavi bir hafta gecikti.',
                          'teaching_point': 'Direkt grafide kemik değişiklikleri 10-14 günden önce genellikle '
                                            'görülmez.'},
                         {'text': 'Tam kan sayımı, CRP, sedimantasyon ve kan kültürü almak; grafi çekip normalse MR '
                                  'istemek',
                          'is_correct': True,
                          'explanation': 'Kan kültürü etkeni gösterebilir. Grafi kırık ve tümörü dışlar ama erken '
                                         'dönemde normaldir. MR kemik iliği ödemini ve apseyi erken gösterir.',
                          'new_finding': 'Lökosit 16.400/mm³, CRP 124 mg/L, sedimantasyon 72 mm/sa, trombosit normal, '
                                         "yaymada blast yok. Direkt grafi normal. MR'da sağ proksimal tibia "
                                         "metafizinde kemik iliği ödemi ve kontrastlanma, 8 mm'lik subperiostal sıvı "
                                         'birikimi. Kan kültüründe gram pozitif koklar üredi.'},
                         {'text': 'Kemik sintigrafisi ve tüm vücut tomografisi istemek, sonuçlar gelene kadar '
                                  'antibiyotik başlamamak',
                          'is_correct': False,
                          'scenario_update': 'Tetkikler günler aldı ve çocuk ateşli kalmaya devam etti.',
                          'teaching_point': 'MR tercih edilen yöntemdir; görüntüleme antibiyotiği geciktirmemelidir.'},
                         {'text': 'Kan kültürü almadan hemen oral amoksisilin başlayıp bir hafta sonra kontrol '
                                  'grafisiyle değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Kültür alınmadığı için etken saptanamadı ve oral tedavi yetersiz kaldı.',
                          'teaching_point': 'Antibiyotik öncesi kültür alınmalı; başlangıç tedavisi intravenöz '
                                            'olmalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Septik artrit (diz)',
                          'is_correct': False,
                          'scenario_update': 'Eklem hareketleri ağrısızdı ve eklemde sıvı yoktu.',
                          'teaching_point': 'Septik artritte eklem hareketleri belirgin ağrılı ve kısıtlıdır.'},
                         {'text': 'Ewing sarkomu',
                          'is_correct': False,
                          'scenario_update': 'MR bulguları enfeksiyonla uyumluydu ve kan kültüründe üreme oldu.',
                          'teaching_point': 'Ewing sarkomu ateş ve yüksek akut fazla gelebilir; grafide soğan zarı '
                                            'görünümü ve kitle görülür.'},
                         {'text': 'Akut hematojen osteomiyelit',
                          'is_correct': True,
                          'explanation': 'Ateş, tibia metafizinde lokalize hassasiyet ve ısı artışı, yük vermeyi '
                                         "reddetme, yüksek akut faz belirteçleri, normal grafi, MR'da kemik iliği "
                                         'ödemi ve subperiostal sıvı ile kan kültürü üremesi akut hematojen '
                                         'osteomiyeliti gösterir.',
                          'new_finding': 'Tanı: Sağ proksimal tibia akut hematojen osteomiyeliti. Kan kültürü: '
                                         'metisiline duyarlı S. aureus.'},
                         {'text': 'Alt bacak selüliti',
                          'is_correct': False,
                          'scenario_update': "Deri bulguları sınırlıydı ve hassasiyet kemik üzerindeydi; MR'da kemik "
                                             'tutulumu vardı.',
                          'teaching_point': 'Selülitte yayılan eritem ve deri hassasiyeti ön plandadır.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'İV sefazolin başlamak, subperiostal sıvı için ortopediye danışmak ve klinik ile CRP '
                                  'düzelince oral tedaviye geçmek',
                          'is_correct': True,
                          'explanation': 'Sefazolin metisiline duyarlı stafilokoklara etkilidir. Subperiostal birikim '
                                         'drenaj gerektirebilir. İyi yanıt alınınca oral tedaviyle toplam süre en az '
                                         '3-4 haftaya tamamlanır.',
                          'new_finding': 'Sefazolin başlandı, ortopedi tarafından subperiostal apse drene edildi. Ateş '
                                         "48 saatte düştü, CRP beşinci günde 32 mg/L'ye indi. Oral sefaleksine geçilip "
                                         'toplam dört haftalık tedaviyle iyileşti.'},
                         {'text': 'Bir haftalık oral sefaleksinle evde tedavi edip CRP ve grafiyle iki hafta sonra '
                                  'kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Kısa oral tedaviyle apse büyüdü ve çocuk sepsis tablosuyla yatırıldı.',
                          'teaching_point': 'Başlangıç tedavisi hastanede ve intravenöz olarak verilir; tedavi süresi '
                                            'en az birkaç haftadır.'},
                         {'text': 'Ağrıyı azaltmak için bacağı alçıya alıp antibiyotik olmadan istirahatle '
                                  'iyileşmesini beklemek',
                          'is_correct': False,
                          'scenario_update': 'Enfeksiyon ilerleyip kemik nekrozu ve büyüme plağı hasarı gelişti.',
                          'teaching_point': 'Kemik enfeksiyonu antibiyotik tedavisi gerektirir; immobilizasyon tek '
                                            'başına yeterli değildir.'},
                         {'text': 'Ampirik olarak yalnızca İV gentamisin başlayıp kültür sonucuna göre gerekirse '
                                  'tedaviyi değiştirmek',
                          'is_correct': False,
                          'scenario_update': 'Gentamisin stafilokoka yeterli etki göstermedi; ateş sürdü.',
                          'teaching_point': 'Ampirik tedavi en sık etken olan stafilokoku mutlaka kapsamalıdır.'}]}]},
 {'id': 'S94',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '11 Yaşında (35 kg)',
  'gender': 'Kız',
  'complaint': 'İki gündür ateş, ağızda yaralar, gözlerde yanma ve gövdeden yayılan, içi su toplayan döküntü',
  'history': "Annesi anlatıyor: 'İki hafta önce ilk kez nöbet geçirdi, karbamazepin başlandı. Dört gün önce ateşi, "
             'boğaz ağrısı ve halsizliği oldu, grip sandık. Dün göğsünde koyu kırmızı lekeler çıktı, bugün yayıldı, '
             'bazılarının ortası kabarıp su topladı. Dudakları yara oldu, yemek yiyemiyor, gözleri yanıyor, çişini '
             "yaparken yanıyor.' Daha önce ilaç alerjisi bilinmiyor.",
  'final_diagnosis': 'Karbamazepine Bağlı Stevens-Johnson Sendromu (Vücut Yüzeyinin <%10 Epidermal Ayrılması)',
  'disposition': 'Sorumlu İlacın Kesilmesi, Alternatif Antiepileptik ve Multidisipliner Destek Tedavisiyle Yanık '
                 'Ünitesi veya Çocuk Yoğun Bakıma Yatış',
  'case_pearl': 'Bu ağır deri reaksiyonu çoğunlukla yeni başlanan bir ilaçtan (antiepileptikler: karbamazepin, '
                'fenitoin, lamotrijin, fenobarbital; sülfonamidler; allopürinol) 4-28 gün sonra gelişir. Ateş ve grip '
                'benzeri prodromu izleyerek koyu, atipik hedef lezyonlar, büller ve en az iki mukozada (ağız, göz, '
                "genital) erozyonlar ortaya çıkar. Nikolsky işareti pozitiftir. Vücut yüzeyinin %10'undan azının "
                "ayrılması bu tanıyı, %30'dan fazlası toksik epidermal nekrolizi gösterir. En önemli adım sorumlu "
                'ilacın hemen kesilmesidir; aromatik antiepileptikler arasında çapraz reaksiyon olabileceği için '
                'levetirasetam gibi bir ilaç seçilir. Yanık hastası gibi sıvı, ağrı ve yara bakımı yapılır, göz için '
                'oftalmoloji erkenden çağrılır. Eritema multiforme minörde mukoza tutulumu sınırlıdır ve tipik '
                'lezyonlar ekstremitelerdedir.',
  'steps': [{'stage_title': 'İlk Değerlendirme',
             'question': 'Ateş, mukozal yaralar ve büllü döküntüsü olan bu çocukta ilk değerlendirmeniz nedir?',
             'options': [{'text': 'Döküntüyü suçiçeği kabul edip ilaç öyküsü almadan oral asiklovir, antihistaminik ve '
                                  'ateş için ibuprofen vererek evde izlem önermek',
                          'is_correct': False,
                          'scenario_update': 'İlaç kesilmediği için döküntü ertesi gün yayıldı ve geniş alanlarda deri '
                                             'soyuldu.',
                          'teaching_point': 'Mukozal tutulumlu büllü döküntüde yeni başlanmış ilaç mutlaka '
                                            'sorgulanmalıdır.'},
                         {'text': 'Vital bulgular ve hidrasyonu değerlendirip mukozaları, deri ayrılmasının yüzdesini '
                                  've Nikolsky işaretini incelemek; ilaç öyküsü almak',
                          'is_correct': True,
                          'explanation': 'Deri ayrılmasının yaygınlığı ve mukozal tutulum şiddeti ve tedavi yerini '
                                         'belirler. Yeni başlanan ilaç olası tetikleyicidir.',
                          'new_finding': 'Ateş 38.9°C, KTA 128/dk, KB 106/64 mmHg, SS 22/dk, SpO2 %98. Mukozalar kuru. '
                                         'Gövde ve proksimal kollarda birleşme eğiliminde koyu kırmızı-mor maküller, '
                                         'ortalarında büller ve gevşek kabarcıklar; dokunmakla deri kayıyor (Nikolsky '
                                         "pozitif). Epidermal ayrılma vücut yüzeyinin yaklaşık %6'sı. Dudaklarda "
                                         'hemorajik kabuklu erozyonlar, ağız içinde yaygın erozyonlar. Bilateral '
                                         'konjonktivit ve göz kapaklarında yapışma eğilimi. Genital mukozada erozyon.'},
                         {'text': 'Döküntüyü stafilokoksik haşlanmış deri sendromu kabul edip İV klindamisin başlamak '
                                  've ilacı sürdürmek',
                          'is_correct': False,
                          'scenario_update': 'Tetikleyici ilaç kesilmediği için mukozal tutulum ağırlaştı.',
                          'teaching_point': 'Haşlanmış deri sendromunda mukozalar tutulmaz; burada belirgin mukozal '
                                            'tutulum vardır.'},
                         {'text': 'Nöbet riskini artırmamak için karbamazepini sürdürüp döküntüye yüksek doz oral '
                                  'kortikosteroid eklemek',
                          'is_correct': False,
                          'scenario_update': "İlaç sürdürüldüğü için deri ayrılması %25'e ilerledi.",
                          'teaching_point': 'Sorumlu ilacın hemen kesilmesi bu tablodaki en önemli tedavi adımıdır.'}]},
            {'stage_title': 'Acil Önlemler',
             'question': 'Bu çocukta acilde hangi adımlar öncelikli olmalıdır?',
             'options': [{'text': 'Karbamazepini hemen kesip yerine fenitoin başlamak ve kabarcıkları steril iğneyle '
                                  'açarak bandajla kapatmak',
                          'is_correct': False,
                          'scenario_update': 'Fenitoin çapraz reaksiyonla tabloyu ağırlaştırdı; açılan kabarcıklar '
                                             'enfekte oldu.',
                          'teaching_point': 'Aromatik antiepileptikler arasında çapraz reaksiyon olabilir; büller '
                                            'yerinde bırakılır.'},
                         {'text': 'Karbamazepini kesip levetirasetama geçmek, İV sıvı ve ağrı tedavisi vermek, '
                                  'yapışmayan örtülerle yara bakımı yapıp oftalmolojiyi çağırmak',
                          'is_correct': True,
                          'explanation': 'Sorumlu ilacın kesilmesi ilerlemeyi durdurur. Levetirasetam aromatik yapıda '
                                         'değildir. Deri kaybı sıvı kaybına yol açar. Erken göz bakımı kalıcı görme '
                                         'sorunlarını önler.',
                          'new_finding': 'Karbamazepin kesildi, levetirasetam başlandı. Sıvı ve morfin infüzyonu '
                                         'başlandı. Oftalmoloji yapışıklıkları açtı, göz damlaları başlandı. Ağız '
                                         'bakımı için antiseptik gargara verildi. Mesane kateteri takıldı.'},
                         {'text': 'Ağrı ve ateş için ibuprofen başlayıp deri lezyonlarını antibiyotikli pomatla '
                                  'kapatmak ve dermatoloji randevusu vermek',
                          'is_correct': False,
                          'scenario_update': 'Ayaktan izlenen çocukta dehidratasyon ve göz komplikasyonları gelişti.',
                          'teaching_point': 'Bu ağırlıkta tablo ayaktan izlenmez; sıvı, göz ve deri bakımı hastanede '
                                            'yapılır.'},
                         {'text': 'Enfeksiyonu önlemek için profilaktik olarak geniş spektrumlu İV antibiyotik '
                                  'başlayıp antiepileptik ilacı nöroloji görüşü alınana kadar sürdürmek',
                          'is_correct': False,
                          'scenario_update': 'İlaç sürdürüldü; deri ayrılması ilerledi ve gereksiz antibiyotik direnç '
                                             'riskini artırdı.',
                          'teaching_point': 'Profilaktik antibiyotik önerilmez; tetikleyici ilaç hemen '
                                            'kesilmelidir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Eritema multiforme minör',
                          'is_correct': False,
                          'scenario_update': 'Lezyonlar gövdede yoğunlaşmıştı, atipik ve büllüydü, üç mukoza belirgin '
                                             'tutulmuştu.',
                          'teaching_point': 'Eritema multiforme minörde tipik üç halkalı hedef lezyonlar '
                                            'ekstremitelerdedir, mukoza tutulumu yoktur veya hafiftir.'},
                         {'text': 'Stafilokoksik haşlanmış deri sendromu',
                          'is_correct': False,
                          'scenario_update': 'Mukozalar tutulmuştu ve yeni başlanmış bir ilaç vardı.',
                          'teaching_point': 'Bu sendromda mukozalar korunur ve ayrılma yüzeyeldir.'},
                         {'text': 'Büllöz impetigo',
                          'is_correct': False,
                          'scenario_update': 'Lezyonlar yaygındı, sistemik bulgular ve mukoza tutulumu vardı.',
                          'teaching_point': 'Büllöz impetigoda lokalize gevşek büller olur, mukoza tutulmaz.'},
                         {'text': 'Karbamazepine bağlı Stevens-Johnson sendromu',
                          'is_correct': True,
                          'explanation': 'Yeni başlanan karbamazepinden iki hafta sonra ateşli prodrom, gövdede atipik '
                                         'hedef lezyonlar ve büller, Nikolsky pozitifliği, üç mukozada erozyon ve '
                                         "vücut yüzeyinin %10'undan az ayrılması Stevens-Johnson sendromunu gösterir.",
                          'new_finding': 'Tanı: Karbamazepine bağlı Stevens-Johnson sendromu.'}]},
            {'stage_title': 'Yatış ve İzlem',
             'question': 'Bu çocuk için en uygun yatış ve izlem planı hangisidir?',
             'options': [{'text': 'Ağız yaraları nedeniyle beslenemeyeceği için yalnızca İV sıvıyla genel pediatri '
                                  'servisinde rutin izlemek',
                          'is_correct': False,
                          'scenario_update': 'Serviste deri bakımı ve sıvı dengesi yeterli izlenemedi; sepsis gelişti.',
                          'teaching_point': 'Bu hastalar yanık ünitesi veya yoğun bakım deneyimi olan merkezlerde '
                                            'izlenmelidir.'},
                         {'text': 'Yanık ünitesi veya yoğun bakıma yatırıp göz, ağız ve genital bakımı yürütmek; ilacı '
                                  'alerji kaydına işlemek',
                          'is_correct': True,
                          'explanation': 'Deri kaybı sıvı ve ısı kaybı, enfeksiyon ve ağrı yönetimi gerektirir. Göz ve '
                                         'genital mukozanın bakımı kalıcı yapışıklıkları önler. İlacın kaydedilmesi '
                                         'tekrar maruziyeti önler.',
                          'new_finding': "Yanık ünitesine yatırıldı. Deri ayrılması %8'de durdu. Üçüncü haftada "
                                         'epitelizasyon tamamlandı; hafif kuru göz kaldı. Karbamazepin ve diğer '
                                         'aromatik antiepileptikler alerji kaydına işlendi, aileye yazılı belge '
                                         'verildi.'},
                         {'text': 'Döküntü hafiflediğinde karbamazepini düşük dozda yeniden başlayıp tolere edip '
                                  'etmediğini görmek',
                          'is_correct': False,
                          'scenario_update': 'Yeniden başlanan ilaçla birkaç saat içinde çok daha ağır bir reaksiyon '
                                             'gelişti.',
                          'teaching_point': 'Sorumlu ilaç ömür boyu bir daha verilmez.'},
                         {'text': 'Bir hafta İV immünglobulin ve ardından altı hafta oral kortikosteroid tedavisi '
                                  'başlayıp ayaktan izlemek',
                          'is_correct': False,
                          'scenario_update': 'Uzun steroid enfeksiyon riskini artırdı ve yara iyileşmesini geciktirdi.',
                          'teaching_point': 'İmmünomodülatör tedaviler tartışmalıdır; temel tedavi destek '
                                            'bakımıdır.'}]}]},
 {'id': 'S95',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '2 Yaşında (12 kg)',
  'gender': 'Erkek',
  'complaint': 'Bilinen egzaması olan çocukta iki gündür yüzde ve boyunda hızla yayılan, içi su dolu yaralar ve yüksek '
               'ateş',
  'history': "Annesi anlatıyor: 'Bebekliğinden beri egzaması var, kortizonlu kremi kullanıyoruz. İki gün önce yüzünde "
             'küçük su toplamış kabarcıklar çıktı, egzama alevlendi sandık, kremi sıklaştırdık. Hızla yayıldı, '
             "patlayıp kabuklandı. Dünden beri ateşi 39.5, huzursuz, yemiyor.' Bir hafta önce babasının dudağında uçuk "
             'varmış ve çocuğu öpmüş. Suçiçeği aşısı yapılmış, kardeşlerde suçiçeği yok.',
  'final_diagnosis': 'Ekzema Herpetikum (Kaposi Variselliform Erüpsiyonu - HSV-1)',
  'disposition': 'İV Asiklovir, Göz Değerlendirmesi ve İkincil Bakteriyel Enfeksiyon Tedavisiyle Pediatri Servisine '
                 'Yatış',
  'case_pearl': "Atopik dermatitli çocuklarda HSV'nin bozulmuş deri bariyeri üzerinde yaygınlaşmasıdır. Egzamanın "
                'alevlenmesi sanılıp gecikilebilir; tedaviye yanıtsız alevlenmede akla gelmelidir. Tek tip görünümlü, '
                "çukurlaşmış (göbekli) veziküller, 'zımbayla delinmiş' görünümlü yuvarlak erozyonlar ve hemorajik "
                'kabuklar tipiktir; ateş ve halsizlik eşlik eder. Tanı veziküllerden PCR ile doğrulanır. Ağır '
                'olgularda ve sistemik bulgu varsa İV asiklovir verilir. Göz çevresi tutulumunda keratit açısından '
                'acil göz muayenesi gerekir. İkincil stafilokok veya streptokok enfeksiyonu sıktır. Topikal '
                'kortikosteroid aktif lezyonlara sürülmez.',
  'steps': [{'stage_title': 'İlk Değerlendirme',
             'question': 'Egzaması olan, ateşli ve yaygın veziküllü yaraları olan bu çocukta ilk değerlendirmeniz '
                         'nedir?',
             'options': [{'text': 'Egzama alevlenmesi kabul edip daha güçlü kortikosteroidli krem ve antihistaminik '
                                  'önererek bir hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Lezyonlar göz çevresine yayıldı ve çocuk ateşi süren, beslenemeyen halde '
                                             'getirildi.',
                          'teaching_point': 'Ateşli, hızla yayılan veziküllü lezyonlarda viral enfeksiyon düşünülmeli, '
                                            'kortikosteroid artırılmamalıdır.'},
                         {'text': 'Genel durumu ve hidrasyonu değerlendirip lezyonların morfolojisini ve dağılımını '
                                  'incelemek; göz çevresi tutulumunu ve ikincil enfeksiyonu aramak',
                          'is_correct': True,
                          'explanation': 'Lezyonların tek tip, göbekli ve zımbayla delinmiş görünümü tanıya '
                                         'yönlendirir. Göz çevresi tutulumu keratit riski taşır. Bal sarısı kabuklar '
                                         'ikincil bakteriyel enfeksiyonu düşündürür.',
                          'new_finding': 'Ateş 39.4°C, KTA 146/dk, SS 30/dk, KB 96/60 mmHg, KDZ 2 sn. Huzursuz, '
                                         'mukozalar hafif kuru. Yüz, boyun ve üst göğüste egzamalı alanlar üzerinde '
                                         "kümeleşmiş, tek tip, 2-3 mm'lik göbekli veziküller; birçoğu patlamış, "
                                         'zımbayla delinmiş görünümlü yuvarlak erozyonlar ve hemorajik kabuklar. '
                                         'Yanakta bal sarısı kabuklu alanlar. Sağ alt göz kapağında veziküller, '
                                         'konjonktiva hafif hiperemik. Servikal lenfadenopati.'},
                         {'text': 'Lezyonları büllöz impetigo kabul edip yalnızca topikal mupirosinle tedavi edip '
                                  'ayaktan izlemek',
                          'is_correct': False,
                          'scenario_update': 'Viral enfeksiyon tedavi edilmeden yaygınlaştı ve göz tutulumu gelişti.',
                          'teaching_point': 'Bal sarısı kabuklar ikincil enfeksiyonu gösterebilir, ancak altta yatan '
                                            'viral süreç atlanmamalıdır.'},
                         {'text': 'Aşılı olmasına rağmen suçiçeği kabul edip ailenin çocuğu evde izole ederek '
                                  'izlemesini ve yalnızca ateş düşürücü vermesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk evde dehidrate oldu ve göz lezyonları ilerledi.',
                          'teaching_point': 'Suçiçeğinde lezyonlar farklı evrelerde ve tüm vücuda yaygındır; burada '
                                            'lezyonlar egzamalı alanlarda kümelenmişti.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Bu çocukta hangi tetkikler en uygundur?',
             'options': [{'text': 'Deri biyopsisi yapmak ve histopatoloji sonucu gelene kadar antiviral tedaviyi '
                                  'ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Biyopsi sonucu günler sürdü ve tedavi gecikti.',
                          'teaching_point': 'Tanı vezikül sıvısından hızlı PCR ile konur; tedavi sonucu beklemeden '
                                            'başlanır.'},
                         {'text': "Taze bir vezikülden virüs PCR'ı ve kabuklu alandan bakteri kültürü almak, kan "
                                  'sayımı ve kan kültürü göndermek',
                          'is_correct': True,
                          'explanation': 'PCR tanıyı doğrular. Bakteri kültürü ikincil enfeksiyon etkenini gösterir. '
                                         'Yüksek ateşte kan kültürü bakteriyemiyi araştırır.',
                          'new_finding': 'Vezikül sıvısında HSV-1 PCR pozitif. Kabuklu alandan alınan kültürde '
                                         'metisiline duyarlı S. aureus üredi. Lökosit 13.800/mm³, CRP 42 mg/L. Kan '
                                         'kültüründe üreme olmadı.'},
                         {'text': 'Alerjik bir reaksiyonu dışlamak için total IgE, geniş besin alerjen paneli ve deri '
                                  'prik testi istemek, sonuca göre tedavi seçmek',
                          'is_correct': False,
                          'scenario_update': 'Testler tanıya katkı sağlamadı ve enfeksiyon tedavisi gecikti.',
                          'teaching_point': 'Akut ateşli veziküler tabloda alerji testleri gereksizdir.'},
                         {'text': 'Yalnızca bakteri kültürü alıp sonuç gelene kadar oral sefaleksin başlamak ve virüs '
                                  'araştırması yapmamak',
                          'is_correct': False,
                          'scenario_update': 'Bakteri tedavisine rağmen yeni veziküller çıkmaya devam etti.',
                          'teaching_point': 'Asıl tablo viraldir; ikincil enfeksiyon tedavisi tek başına yeterli '
                                            'değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Ekzema herpetikum',
                          'is_correct': True,
                          'explanation': 'Atopik dermatitli çocukta uçuklu bir yakınla temastan sonra egzamalı '
                                         'alanlarda kümelenen tek tip göbekli veziküller, zımbayla delinmiş '
                                         'erozyonlar, yüksek ateş ve HSV-1 PCR pozitifliği ekzema herpetikumu '
                                         'gösterir.',
                          'new_finding': 'Tanı: Ekzema herpetikum (Kaposi variselliform erüpsiyonu), ikincil '
                                         'stafilokok enfeksiyonu.'},
                         {'text': 'Atopik dermatit alevlenmesi',
                          'is_correct': False,
                          'scenario_update': 'Lezyonlar veziküllü ve göbekliydi, yüksek ateş vardı ve PCR pozitifti.',
                          'teaching_point': 'Basit alevlenmede yüksek ateş ve göbekli veziküller beklenmez.'},
                         {'text': 'Suçiçeği (varisella)',
                          'is_correct': False,
                          'scenario_update': 'Aşılıydı, lezyonlar egzamalı alanlarla sınırlı ve tek tipti.',
                          'teaching_point': 'Suçiçeğinde farklı evrelerde lezyonlar saçlı deri ve gövdeden başlayarak '
                                            'yayılır.'},
                         {'text': 'Eritema multiforme',
                          'is_correct': False,
                          'scenario_update': 'Hedef lezyonlar yoktu, lezyonlar veziküler ve kümelenmişti.',
                          'teaching_point': 'Eritema multiformede tipik hedef lezyonlar el ve ayaklarda görülür.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Topikal asiklovir krem sürüp kortikosteroidli kremi sürdürmek ve ayaktan izlemek',
                          'is_correct': False,
                          'scenario_update': 'Topikal tedavi yetersiz kaldı, kortikosteroid virüs yayılımını '
                                             'kolaylaştırdı.',
                          'teaching_point': 'Yaygın ve sistemik bulgulu tabloda sistemik antiviral gerekir; aktif '
                                            'lezyonlara kortikosteroid sürülmez.'},
                         {'text': 'İV asiklovir ve stafilokoka etkili antibiyotik başlamak, acil göz muayenesi '
                                  'yaptırıp çocuğu yatırmak',
                          'is_correct': True,
                          'explanation': 'Sistemik bulgulu ve yaygın tabloda İV asiklovir yayılımı durdurur. İkincil '
                                         'bakteriyel enfeksiyon tedavi edilir. Göz kapağı tutulumu keratit açısından '
                                         'değerlendirilmelidir.',
                          'new_finding': 'İV asiklovir ve sefazolin başlandı. Oftalmoloji muayenesinde kornea tutulumu '
                                         'yoktu, profilaktik göz merhemi verildi. Ateş 48 saatte düştü, yeni vezikül '
                                         'çıkmadı. Beşinci günde oral tedaviye geçilerek taburcu edildi; egzama bakımı '
                                         'yeniden düzenlendi.'},
                         {'text': 'Yalnızca oral antibiyotik ve antihistaminik başlayıp lezyonlar kabuklanınca yeniden '
                                  'değerlendirmek üzere taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Antiviral verilmeyen çocukta lezyonlar yayıldı ve bakteriyemi gelişti.',
                          'teaching_point': 'Viral etken tedavi edilmeden tablo kontrol altına alınamaz.'},
                         {'text': 'Sistemik kortikosteroid ve immünglobulin vererek bağışıklık yanıtını baskılamak ve '
                                  'ateşi izlemek',
                          'is_correct': False,
                          'scenario_update': 'Kortikosteroid viral yayılımı artırdı ve tablo ağırlaştı.',
                          'teaching_point': 'Sistemik kortikosteroid viral deri enfeksiyonunu ağırlaştırabilir.'}]}]},
 {'id': 'S96',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '4 Yaşında (16 kg)',
  'gender': 'Erkek',
  'complaint': 'Suçiçeğinin beşinci gününde yeniden yükselen ateş ve sol uylukta şiddetli ağrı ve şişlik',
  'history': "Annesi anlatıyor: 'Beş gün önce suçiçeği çıktı, iki gün ateşi oldu sonra düştü. Dün akşam ateşi yeniden "
             "40'a çıktı. Sol bacağında kaşıyıp yara yaptığı bir suçiçeği vardı, oranın çevresi kızardı. Bacağına "
             "dokundurmuyor, çok ağlıyor, basamıyor.' Ateş için iki gündür ibuprofen veriliyor. Bilinen hastalığı yok. "
             'Suçiçeği aşısı yapılmamış.',
  'final_diagnosis': 'Suçiçeği Sonrası İnvaziv Grup A Streptokok Enfeksiyonu: Nekrotizan Fasiit ve Streptokokal Toksik '
                     'Şok',
  'disposition': 'Resüsitasyon, İV Penisilin + Klindamisin, İVİG ve Acil Cerrahi Debridmanla Çocuk Yoğun Bakım Yatışı',
  'case_pearl': 'Suçiçeği lezyonları grup A streptokok için giriş kapısıdır. Ateşin düştükten sonra yeniden yükselmesi '
                'veya 4. günden sonra sürmesi ikincil bakteriyel enfeksiyonun uyarı bulgusudur. Derin yumuşak doku '
                'enfeksiyonunda en erken ve en önemli bulgu görünümle orantısız şiddetli ağrıdır; deri bulguları '
                'başlangıçta hafif olabilir. Hızla yayılan eritem, odun sertliğinde ödem, bül, deride morarma, '
                'krepitasyon ve sistemik toksisite eşlik eder. Tedavi gecikmeden cerrahi debridman ve İV '
                'antibiyotiktir; klindamisin toksin üretimini baskılar. Toksik şokta İVİG eklenebilir. Görüntüleme '
                'cerrahiyi geciktirmemelidir. Suçiçeği sırasında NSAİİ kullanımı riskle ilişkilendirilmiştir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Resüsitasyon',
             'question': 'Suçiçeği sonrası ateşi yeniden yükselen ve bacağına dokundurmayan bu çocukta ilk '
                         'yaklaşımınız nedir?',
             'options': [{'text': 'Suçiçeğinin olağan seyri kabul edip ateş için ibuprofeni sürdürmek ve kaşıntı için '
                                  'antihistaminik önermek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk gece bilinç bulanıklığı ve hipotansiyonla getirildi; uyluktaki '
                                             'kızarıklık kalçaya yayılmıştı.',
                          'teaching_point': 'Suçiçeğinde ateşin yeniden yükselmesi ikincil bakteriyel enfeksiyonun '
                                            'uyarı bulgusudur.'},
                         {'text': 'Vital bulgular ve perfüzyonu değerlendirmek, iki damar yolu açıp kültür ve laktat '
                                  'almak, ağrının şiddetini muayene bulgularıyla karşılaştırmak',
                          'is_correct': True,
                          'explanation': 'Sistemik toksisite ve şok bulguları erkenden aranmalıdır. Görünümle '
                                         'orantısız şiddetli ağrı derin doku enfeksiyonunun en önemli ipucudur.',
                          'new_finding': 'Ateş 40.1°C, KTA 172/dk, KB 76/40 mmHg, SS 36/dk, SpO2 %95, KDZ 4 sn. '
                                         'Uykulu, uyarana huzursuzlukla yanıt veriyor. Sol uylukta kızarık, sınırları '
                                         'belirsiz, hızla yayılan eritem; çevresinde odun sertliğinde ödem; ortasında '
                                         'mor-gri renk değişikliği ve hemorajik bül. Ağrı kızarıklığın sınırlarının '
                                         'ötesine uzanıyor. Gövdede kabuklanmış suçiçeği lezyonları. Laktat 4.9 '
                                         'mmol/L.'},
                         {'text': 'Lezyonu basit selülit kabul edip oral sefaleksin başlayarak kızarıklığın '
                                  'sınırlarını kalemle çizmek ve ertesi gün kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Kızarıklık birkaç saat içinde işaretli sınırları aştı; çocuk şoka girdi.',
                          'teaching_point': 'Sistemik toksisite ve orantısız ağrı basit selülitle bağdaşmaz; ayaktan '
                                            'tedavi edilmez.'},
                         {'text': 'Ağrı nedeniyle kırık olabileceğini düşünüp önce femur grafisi çektirmek ve ortopedi '
                                  'görüşüne göre karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Grafi için beklenen sürede kan basıncı daha da düştü.',
                          'teaching_point': 'Travma öyküsü olmayan ateşli ve şoktaki çocukta önce resüsitasyon ve '
                                            'enfeksiyon yönetimi yapılır.'}]},
            {'stage_title': 'Acil Tedavi Kararları',
             'question': 'Sıvı resüsitasyonu başlanan bu çocukta hangi tedavi yaklaşımı uygundur?',
             'options': [{'text': "Ceftriakson tek başına başlamak ve tanıyı kesinleştirmek için bacak MR'ı çekilene "
                                  'kadar cerrahi kararı ertelemek',
                          'is_correct': False,
                          'scenario_update': 'MR için bekleme sırasında nekroz yayıldı ve çocuk vazopresör gerektirdi.',
                          'teaching_point': 'Klinik şüphe yüksekse görüntüleme cerrahiyi geciktirmemelidir; '
                                            'klindamisin eklenmelidir.'},
                         {'text': 'İV penisilin ve klindamisin başlamak, İVİG düşünmek ve tanı ile debridman için '
                                  'çocuk cerrahisini acil çağırmak',
                          'is_correct': True,
                          'explanation': 'Klindamisin toksin üretimini baskılar ve bakteri yükünden bağımsız '
                                         'etkilidir. Ölü dokunun çıkarılması enfeksiyonun kontrolü için zorunludur. '
                                         'İVİG toksinleri nötralize edebilir.',
                          'new_finding': 'Penisilin, klindamisin ve vankomisin başlandı. 60 mL/kg sıvıya rağmen '
                                         'hipotansiyon sürdü, adrenalin başlandı. İVİG verildi. Çocuk cerrahisi '
                                         'ameliyata aldı.'},
                         {'text': 'Bülü steril iğneyle boşaltıp sıvıdan kültür almak ve bölgeye soğuk kompres '
                                  'uygulayarak antibiyotiği kültüre göre seçmek',
                          'is_correct': False,
                          'scenario_update': 'Kültür sonucu beklenirken enfeksiyon gövdeye doğru ilerledi.',
                          'teaching_point': 'Ampirik antibiyotik ve cerrahi gecikmeden başlanmalıdır.'},
                         {'text': 'Asiklovir başlayıp suçiçeği tedavisinin bacağı da düzelteceğini düşünmek ve '
                                  'antibiyotiği ertesi güne bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Bakteriyel enfeksiyon tedavisiz ilerledi ve çocuk çoklu organ '
                                             'yetmezliğine girdi.',
                          'teaching_point': 'Bu tablo bakteriyel ikincil enfeksiyondur; antiviral tek başına '
                                            'etkisizdir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': "Ameliyatta fasya gri ve kanlanması bozuk, parmakla kolayca ayrılıyor, bulanık 'bulaşık suyu' "
                         'sıvı var. En olası tanınız nedir?',
             'options': [{'text': 'Suçiçeğinde komplike olmayan selülit',
                          'is_correct': False,
                          'scenario_update': 'Fasya tutulmuştu ve sistemik şok vardı.',
                          'teaching_point': 'Selülitte enfeksiyon dermis ve deri altıyla sınırlıdır.'},
                         {'text': 'Stafilokoksik haşlanmış deri sendromu',
                          'is_correct': False,
                          'scenario_update': 'Yaygın yüzeyel soyulma yoktu, enfeksiyon derin dokulardaydı.',
                          'teaching_point': 'Bu sendromda yüzeyel epidermal soyulma görülür, derin doku tutulmaz.'},
                         {'text': 'Grup A streptokok nekrotizan fasiiti ve toksik şok',
                          'is_correct': True,
                          'explanation': 'Suçiçeği lezyonundan başlayan, orantısız ağrılı, hızla yayılan eritem, '
                                         'sertlik, bül ve deri renk değişikliği, şok ve ameliyatta nekrotik fasya grup '
                                         'A streptokok nekrotizan fasiitini ve toksik şoku gösterir.',
                          'new_finding': 'Tanı: Suçiçeği sonrası grup A streptokok nekrotizan fasiiti ve streptokokal '
                                         'toksik şok. Doku ve kan kültüründe S. pyogenes üredi.'},
                         {'text': 'Derin ven trombozu',
                          'is_correct': False,
                          'scenario_update': 'Ateş, şok ve deri nekrozu vardı; ameliyatta fasya nekrozu görüldü.',
                          'teaching_point': 'Derin ven trombozu çocuklarda nadirdir ve ateşli şok yapmaz.'}]},
            {'stage_title': 'Yoğun Bakım ve İzlem',
             'question': 'Debridman sonrası en uygun izlem planı hangisidir?',
             'options': [{'text': 'Tek debridmanın yeterli olduğunu kabul edip antibiyotiği üçüncü günde orale '
                                  'geçirerek servise almak',
                          'is_correct': False,
                          'scenario_update': 'Kalan nekrotik doku nedeniyle enfeksiyon yeniden alevlendi.',
                          'teaching_point': 'Bu tabloda tekrarlayan debridmanlar ve uzun süreli İV tedavi gerekir.'},
                         {'text': 'Yoğun bakımda izleyip 24-48 saatte yeniden cerrahi değerlendirme yapmak; hane '
                                  'temaslılarını izlemek ve olguyu bildirmek',
                          'is_correct': True,
                          'explanation': 'Nekroz sınırı ilk ameliyatta tam belirlenemeyebilir; tekrar değerlendirme '
                                         'gerekir. Ev içi temaslılarda invaziv hastalık riski artmıştır ve semptomlar '
                                         'açısından izlenmeleri gerekir.',
                          'new_finding': 'İkinci ve üçüncü debridmanlar yapıldı. Adrenalin dördüncü günde kesildi. '
                                         'Klindamisin beşinci günde kesildi, penisilin üç haftaya tamamlandı. Deri '
                                         'grefti uygulandı, fizik tedavi planlandı. Aile bireyleri bilgilendirildi.'},
                         {'text': 'Ağrıyı ve ateşi kontrol etmek için ibuprofeni yüksek dozda sürdürmek ve analjezi '
                                  'için başka ilaç eklememek',
                          'is_correct': False,
                          'scenario_update': 'NSAİİ böbrek hasarını artırdı ve kreatinin yükseldi.',
                          'teaching_point': 'Şok ve böbrek hasarı riskinde NSAİİ kullanılmaz; uygun analjezi verilir.'},
                         {'text': 'Ailedeki tüm çocuklara bir yıl boyunca aylık benzatin penisilin profilaksisi yapmak '
                                  've suçiçeği aşısını ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz uzun profilaksi yapıldı ve aşısız kardeşler suçiçeğine açık '
                                             'kaldı.',
                          'teaching_point': 'Rutin uzun süreli profilaksi önerilmez; aşısız kardeşler suçiçeği '
                                            'aşısıyla korunur.'}]}]},
 {'id': 'S97',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '15 Yaşında (62 kg)',
  'gender': 'Erkek',
  'complaint': 'Temmuz öğleden sonrası futbol antrenmanında yere yığılma, anlamsız konuşma ve saldırganlık',
  'history': "Antrenörü getirdi: 'Adana'da hava 41 derece, nem yüksekti. Turnuva öncesi saat 14'te kondisyon "
             'antrenmanı yaptık. Bir saat sonra sendelemeye başladı, saçma sapan konuştu, sonra yere düştü. Su verdik, '
             "içemedi.' Kendisi daha önce sağlıklı. Bir haftadır antrenmanlar yoğun. Son günlerde ishal geçirmiş. "
             'İlaç, takviye, enerji içeceği veya madde kullanımı bilinmiyor. Diyabeti yok.',
  'final_diagnosis': 'Eforla İlişkili Isı Çarpması (Rabdomiyoliz ve Akut Böbrek Hasarı ile)',
  'disposition': 'Hızlı Soğuk Su Daldırma ile Soğutma, Sıvı Tedavisi ve Organ Hasarı İzlemi İçin Çocuk Yoğun Bakım '
                 'Yatışı',
  'case_pearl': "Sıcak ve nemli ortamda efor sırasında vücut ısısının 40°C'nin üzerine çıkması ve merkezi sinir "
                'sistemi bozukluğu (konfüzyon, saldırganlık, nöbet, koma) tanıyı koydurur; terleme devam edebilir. Isı '
                'ölçümü rektal veya özofageal yolla yapılmalıdır. En önemli tedavi hızlı soğutmadır: soğuk-buzlu suya '
                "daldırma en etkili yöntemdir, 'önce soğut, sonra taşı' ilkesi uygulanır. Ateş düşürücüler etkisizdir, "
                "çünkü sorun hipotalamik ayar noktasında değildir. Isı 38.5-39°C'ye düşünce aşırı soğumayı önlemek "
                'için soğutma durdurulur. Rabdomiyoliz, akut böbrek hasarı, karaciğer hasarı, DİK ve elektrolit '
                'bozuklukları izlenir. Kan şekeri ve sodyum her zaman kontrol edilmelidir.',
  'steps': [{'stage_title': 'İlk Değerlendirme',
             'question': 'Sıcakta antrenman sırasında bilinci bozulan bu ergende ilk değerlendirmeniz nedir?',
             'options': [{'text': 'Hava yolunu ve dolaşımı değerlendirmek, rektal ısıyı ölçmek ve kan şekerine bakmak; '
                                  'nöbet ve travma bulgularını aramak',
                          'is_correct': True,
                          'explanation': 'Bilinci bozuk ergende rektal ısı ve kan şekeri hemen ölçülür. Koltuk altı '
                                         'veya timpanik ölçüm gerçek iç ısıyı yansıtmayabilir.',
                          'new_finding': 'Rektal ısı 41.4°C, KTA 156/dk, KB 96/50 mmHg, SS 32/dk, SpO2 %96. GKS 11, '
                                         'ajite ve konfüze. Cilt sıcak, hâlâ hafif terli. Pupiller eşit, ışık yanıtı '
                                         'var. Ense sertliği yok. Travma bulgusu yok. Kan şekeri 94 mg/dL.'},
                         {'text': 'Koltuk altı ısısını ölçmek, ateşi düşürmek için İV parasetamol vermek ve yarım saat '
                                  'sonra yeniden değerlendirmek',
                          'is_correct': False,
                          'scenario_update': "Parasetamol ısıyı düşürmedi; yarım saat içinde rektal ısı 42°C'ye çıktı "
                                             've ergen nöbet geçirdi.',
                          'teaching_point': 'Bu tabloda ateş düşürücüler etkisizdir; ısı rektal ölçülmeli ve fiziksel '
                                            'soğutma hemen yapılmalıdır.'},
                         {'text': 'Saldırganlık nedeniyle madde kullanımı kabul edip güvenlik görevlileriyle '
                                  'kısıtlamak ve toksikoloji taramasını beklemek',
                          'is_correct': False,
                          'scenario_update': 'Kısıtlamaya karşı direnen ergenin ısısı daha da yükseldi ve CK hızla '
                                             'arttı.',
                          'teaching_point': 'Sıcakta eforla gelişen bilinç bozukluğunda önce ısı ölçülmeli ve soğutma '
                                            'yapılmalıdır.'},
                         {'text': 'Bilinç değişikliği nedeniyle önce acil beyin tomografisine göndermek ve ardından '
                                  'lomber ponksiyon yapmak',
                          'is_correct': False,
                          'scenario_update': 'Tomografi sürecinde soğutma yapılmadı ve beyin hasarı riski arttı.',
                          'teaching_point': 'Soğutma tanı amaçlı tetkiklerden önce gelir.'}]},
            {'stage_title': 'Soğutma Yöntemi',
             'question': 'Rektal ısısı 41.4°C olan bu ergende en etkili soğutma yöntemi hangisidir?',
             'options': [{'text': 'Islak havlu ile alnını ve bileklerini silmek, oda sıcaklığındaki serum fizyolojiği '
                                  'yavaş infüzyonla vermek',
                          'is_correct': False,
                          'scenario_update': 'Isı bir saatte yalnızca 0.5°C düştü; çoklu organ hasarı belirteçleri '
                                             'yükseldi.',
                          'teaching_point': 'Yavaş soğutma yöntemleri yetersizdir; iç ısı 30 dakika içinde '
                                            'düşürülmelidir.'},
                         {'text': 'Isıyı sıvılarla dengelemek için hızla 60 mL/kg serum fizyolojik verip sıcaklığın '
                                  'kendiliğinden düşmesini beklemek',
                          'is_correct': False,
                          'scenario_update': 'Fazla sıvı akciğer ödemine yol açtı; ısı yüksek kalmaya devam etti.',
                          'teaching_point': 'Sıvı gereksinimi ölçülü verilir; ısı fiziksel soğutmayla düşürülür.'},
                         {'text': 'Boynuna kadar soğuk-buzlu suya daldırıp rektal ısıyı sürekli izlemek ve '
                                  "38.5-39°C'de soğutmayı durdurmak",
                          'is_correct': True,
                          'explanation': 'Soğuk suya daldırma en hızlı ısı kaybını sağlar ve sağkalımı artırır. '
                                         'Hedefte durmak aşırı soğumayı önler. Daldırma yapılamıyorsa buz-ıslak havlu '
                                         'dönüşümlü uygulama ve fan kullanılır.',
                          'new_finding': "Buzlu su küvetine alındı. Yirmi dakikada rektal ısı 38.9°C'ye düştü, soğutma "
                                         "durduruldu. GKS 14'e yükseldi. KTA 118/dk, KB 112/64 mmHg."},
                         {'text': 'Yalnızca klimalı odaya alıp yelpazelemek, buz paketlerini koltuk altına koyup '
                                  'ısının yavaşça düşmesini beklemek',
                          'is_correct': False,
                          'scenario_update': 'Isı bir saat boyunca 40°C üzerinde kaldı ve ergen nöbet geçirdi.',
                          'teaching_point': 'Bu yöntemler tek başına yavaştır; daldırma mümkünse ilk tercih edilir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Soğutma sonrası laboratuvarda CK 18.400 U/L, kreatinin 1.9 mg/dL, AST 420 U/L, Na 134 mmol/L '
                         'bulundu. En olası tanınız nedir?',
             'options': [{'text': 'Eforla ilişkili ısı çarpması ve rabdomiyoliz',
                          'is_correct': True,
                          'explanation': 'Sıcak ve nemli ortamda yoğun efor sırasında 40°C üzeri iç ısı ve merkezi '
                                         'sinir sistemi bozukluğu, soğutmayla nörolojik düzelme, CK, kreatinin ve '
                                         'transaminaz yüksekliği eforla ilişkili ısı çarpması ve rabdomiyolizi '
                                         'gösterir.',
                          'new_finding': 'Tanı: Eforla ilişkili ısı çarpması, rabdomiyoliz ve akut böbrek hasarı.'},
                         {'text': 'Isı bitkinliği',
                          'is_correct': False,
                          'scenario_update': 'Belirgin bilinç değişikliği ve 41.4°C iç ısı vardı.',
                          'teaching_point': 'Isı bitkinliğinde iç ısı 40°C altındadır ve bilinç korunur.'},
                         {'text': 'Bakteriyel menenjit',
                          'is_correct': False,
                          'scenario_update': 'Ense sertliği yoktu ve soğutmayla bilinç hızla düzeldi.',
                          'teaching_point': 'Enfeksiyon kuşkusu sürerse soğutma sonrası ayrıca değerlendirilir.'},
                         {'text': 'Egzersizle ilişkili hiponatremi',
                          'is_correct': False,
                          'scenario_update': 'Sodyum 134 mmol/L idi ve iç ısı çok yüksekti.',
                          'teaching_point': 'Bu tabloda sodyum genellikle 130 mmol/L altındadır ve aşırı su içimi '
                                            'öyküsü vardır.'}]},
            {'stage_title': 'Sonraki Yönetim ve Yatış',
             'question': 'Bu ergenin sonraki yönetimi nasıl olmalıdır?',
             'options': [{'text': 'Bilinci düzeldiği için birkaç saat gözlem sonrası taburcu etmek ve iki gün sonra '
                                  'antrenmana dönmesine izin vermek',
                          'is_correct': False,
                          'scenario_update': 'Evde idrar miktarı azaldı ve koyulaştı; ergen akut böbrek hasarıyla '
                                             'yeniden getirildi.',
                          'teaching_point': 'Organ hasarı izlenmeden taburculuk yapılmaz; spora dönüş kademeli ve '
                                            'hekim onayıyla olur.'},
                         {'text': 'Kas hasarı nedeniyle furosemid başlayıp sıvıyı kısıtlamak ve idrarı alkalileştirmek '
                                  'için yüksek doz bikarbonat vermek',
                          'is_correct': False,
                          'scenario_update': 'Sıvı kısıtlaması ve diüretik böbrek hasarını ağırlaştırdı.',
                          'teaching_point': 'Kas hasarında temel tedavi yeterli sıvıyla idrar çıkışını korumaktır.'},
                         {'text': 'Yoğun bakımda yeterli sıvıyla idrar çıkışını korumak; CK, kreatinin, potasyum, '
                                  'karaciğer ve pıhtılaşmayı izlemek',
                          'is_correct': True,
                          'explanation': 'Kas hasarına bağlı böbrek hasarı yeterli sıvıyla önlenir. Hiperkalemi, '
                                         'karaciğer hasarı ve pıhtılaşma bozukluğu ilk 24-72 saatte gelişebilir.',
                          'new_finding': 'Sıvı tedavisiyle idrar çıkışı 2 mL/kg/saat tutuldu. CK 36. saatte 42.000 U/L '
                                         'ile pik yaptı, sonra düştü; kreatinin beşinci günde normale döndü. '
                                         'Taburculukta antrenöre sıcakta antrenman, sıvı ve dinlenme önerileri '
                                         'verildi; kademeli spora dönüş planlandı.'},
                         {'text': 'Isının tekrar yükselmesini önlemek için düzenli parasetamol ve ibuprofen başlayıp '
                                  'genel serviste izlemek',
                          'is_correct': False,
                          'scenario_update': 'İlaçlar ısıyı etkilemedi; ibuprofen böbrek hasarını artırdı, parasetamol '
                                             'karaciğer hasarına eklendi.',
                          'teaching_point': 'Antipiretikler etkisizdir ve böbrek ile karaciğer hasarı olan hastada '
                                            'zararlı olabilir.'}]}]},
 {'id': 'S98',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '16 Yaşında (55 kg)',
  'gender': 'Kız',
  'complaint': 'Saatler içinde gelişen huzursuzluk, titreme, aşırı terleme, ishal ve bacaklarda istemsiz sıçramalar',
  'history': "Annesi anlatıyor: 'Üç aydır depresyon için sertralin kullanıyor. Doktoru iki hafta önce dozunu artırdı. "
             'Dün diş ağrısı için eczaneden tramadol aldı, bugün de öksürük için dekstrometorfanlı şurup içti. Öğleden '
             "sonra titremeye, terlemeye başladı, yerinde duramıyor, ishal oldu.' Kızla yalnız görüşüldüğünde kendine "
             'zarar verme amacıyla fazla ilaç almadığını söylüyor. Alkol veya madde kullanımı yok. Ateşli bir hastalık '
             'öyküsü yok.',
  'final_diagnosis': 'Serotonin Sendromu (Sertralin + Tramadol + Dekstrometorfan Etkileşimi, Orta Şiddette)',
  'disposition': 'Serotonerjik İlaçların Kesilmesi, Benzodiazepin, Soğutma ve Gerekirse Siproheptadin ile Monitörlü '
                 'Yatış; Psikiyatri İzlemi',
  'case_pearl': 'Serotonerjik ilaçların (SSRI, SNRI, tramadol, dekstrometorfan, linezolid, triptanlar, MDMA) birlikte '
                'kullanımı veya doz artışı sonrası saatler içinde başlar. Üçlü tablo: mental durum değişikliği '
                '(ajitasyon), otonom instabilite (taşikardi, terleme, hipertermi, ishal, midriyazis) ve nöromüsküler '
                'bulgular (alt ekstremitede belirgin klonus, hiperrefleksi, tremor). Hunter kriterleri tanıda '
                'kullanılır. Tedavi: tüm serotonerjik ilaçların kesilmesi, benzodiazepin, soğutma ve destek; süren '
                'bulgularda siproheptadin. Ağır hipertermide paralizi ve entübasyon gerekir; antipiretikler '
                'etkisizdir. Nöroleptik malign sendrom günler içinde gelişir, bradirefleksi ve kurşun boru rijiditesi '
                'gösterir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Huzursuz, titreyen ve terleyen bu ergende muayenede neye odaklanırsınız?',
             'options': [{'text': 'Kaygı bozukluğuna bağlı panik atak kabul edip nefes egzersizi önermek ve ayaktan '
                                  'psikiyatri polikliniğine randevu verip yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Fizik muayene yapılmadan gönderilen ergen evde 40°C ateş ve bilinç '
                                             'bulanıklığıyla getirildi.',
                          'teaching_point': 'Yeni ilaç başlanan ve otonom bulguları olan hastada organik nedenler önce '
                                            'dışlanır.'},
                         {'text': 'Vital bulgular ve ısıyı ölçüp pupilleri, terlemeyi, bağırsak seslerini, kas '
                                  'tonusunu, refleksleri ve klonusu değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Zehirlenme tablolarının ayrımı pupil, cilt nemi, bağırsak sesleri ve '
                                         'nöromüsküler bulgularla yapılır. Alt ekstremitede belirgin klonus ve '
                                         'hiperrefleksi ayırıcı tanıda en değerli bulgulardır.',
                          'new_finding': 'Ateş 38.9°C, KTA 136/dk, KB 148/92 mmHg, SS 24/dk, SpO2 %99. Ajite, '
                                         'huzursuz, yönelimi kısmen bozuk. Pupiller geniş, ışığa yanıtlı. Cilt terli. '
                                         'Bağırsak sesleri artmış. Tremor; alt ekstremitelerde belirgin hiperrefleksi, '
                                         'ayak bileğinde uyarılabilen ve kendiliğinden olan klonus, oküler klonus. Kas '
                                         'tonusu alt ekstremitelerde artmış.'},
                         {'text': 'Ajitasyon için hemen İM haloperidol yapıp sakinleşince öykü ve muayeneyi tamamlamak',
                          'is_correct': False,
                          'scenario_update': "Haloperidol sonrası rijidite arttı ve ısı 40.2°C'ye yükseldi.",
                          'teaching_point': 'Antipsikotikler bu tabloyu ağırlaştırabilir ve nöroleptik malign '
                                            'sendromla karışıklığa yol açar.'},
                         {'text': 'Ateş nedeniyle sepsis kabul edip lomber ponksiyon yapmak ve İV seftriakson ile '
                                  'asiklovir başlamak',
                          'is_correct': False,
                          'scenario_update': 'BOS normal geldi; asıl neden olan ilaçlar kesilmediği için tablo '
                                             'ilerledi.',
                          'teaching_point': 'İlaç öyküsü ve nöromüsküler bulgular ayrıntılı değerlendirilmeden invaziv '
                                            'tetkiklere geçilmez.'}]},
            {'stage_title': 'Acil Tedavi',
             'question': 'Bu ergende acil tedavi yaklaşımı nasıl olmalıdır?',
             'options': [{'text': 'Sertralini sürdürüp yalnızca tramadol ve şurubu kesmek, ateş için parasetamol verip '
                                  'izlemek',
                          'is_correct': False,
                          'scenario_update': 'Sertralin sürdürüldüğü için bulgular gerilemedi; ateş parasetamole yanıt '
                                             'vermedi.',
                          'teaching_point': 'Tüm sorumlu ilaçlar kesilmelidir; ısı artışı kas aktivitesinden '
                                            'kaynaklandığı için antipiretik etkisizdir.'},
                         {'text': 'Ajitasyon nedeniyle kollarını ve bacaklarını sedyeye bağlayıp ilaç vermeden '
                                  'fiziksel kısıtlamayla izlemek',
                          'is_correct': False,
                          'scenario_update': "Kısıtlamaya karşı izometrik kasılma ısıyı 40.5°C'ye çıkardı ve laktik "
                                             'asidoz gelişti.',
                          'teaching_point': 'Fiziksel kısıtlama ısı üretimini artırır; kimyasal sedasyon tercih '
                                            'edilir.'},
                         {'text': 'Tüm ilgili ilaçları kesmek, İV benzodiazepin ve sıvı vermek, dış soğutma yapıp '
                                  'monitörize etmek',
                          'is_correct': True,
                          'explanation': 'İlaçların kesilmesi tablonun nedenini ortadan kaldırır. Benzodiazepin '
                                         'ajitasyon, kas aktivitesi ve otonom bulguları azaltır. Soğutma ısıyı kontrol '
                                         'eder.',
                          'new_finding': 'Tüm ilaçlar kesildi, diazepam İV verildi, sıvı ve soğutma uygulandı. Bir '
                                         'saat sonra KTA 108/dk, ısı 38.1°C, klonus azaldı. CK 980 U/L, kreatinin '
                                         "normal, parasetamol ve salisilat düzeyi negatif. EKG'de QTc 450 ms."},
                         {'text': 'Ağır bir tablo olarak hemen entübe edip paralizi yapmak ve yoğun bakıma almak',
                          'is_correct': False,
                          'scenario_update': 'Benzodiazepine yanıt verebilecek orta şiddetteki hasta gereksiz yere '
                                             'entübe edildi.',
                          'teaching_point': 'Entübasyon ve paralizi 41°C üzeri ısı ve şiddetli rijiditede gereklidir; '
                                            'önce benzodiazepin ve soğutma uygulanır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Nöroleptik malign sendrom',
                          'is_correct': False,
                          'scenario_update': 'Antipsikotik kullanımı yoktu, tablo saatler içinde başlamıştı ve '
                                             'refleksler artmıştı.',
                          'teaching_point': 'Nöroleptik malign sendrom günler içinde gelişir, bradirefleksi ve kurşun '
                                            'boru rijiditesi gösterir.'},
                         {'text': 'İlaç etkileşimine bağlı serotonin sendromu',
                          'is_correct': True,
                          'explanation': 'Sertralin doz artışı sonrası tramadol ve dekstrometorfan eklenmesiyle '
                                         'saatler içinde gelişen ajitasyon, ateş, taşikardi, terleme, midriyazis, '
                                         'ishal, alt ekstremitede belirgin klonus ve hiperrefleksi serotonin '
                                         'sendromunu gösterir.',
                          'new_finding': 'Tanı: Sertralin, tramadol ve dekstrometorfan etkileşimine bağlı serotonin '
                                         'sendromu (orta şiddette).'},
                         {'text': 'Tiroid fırtınası',
                          'is_correct': False,
                          'scenario_update': 'Guatr ve tiroid hastalığı öyküsü yoktu, klonus belirgindi.',
                          'teaching_point': 'Tiroid fırtınasında guatr, kilo kaybı ve tiroid hormon yüksekliği '
                                            'beklenir.'},
                         {'text': 'Sempatomimetik madde zehirlenmesi',
                          'is_correct': False,
                          'scenario_update': 'Madde kullanımı yoktu ve belirgin klonus ile hiperrefleksi vardı.',
                          'teaching_point': 'Sempatomimetiklerde klonus belirgin değildir, ilaç öyküsü '
                                            'yönlendiricidir.'}]},
            {'stage_title': 'Yatış ve Taburculuk Planı',
             'question': 'Bu ergenin sonraki yönetimi nasıl olmalıdır?',
             'options': [{'text': 'Bulgular gerileyince ertesi gün sertralini aynı dozda yeniden başlatıp tramadolu '
                                  'düzenli ağrı kesici olarak sürdürmek',
                          'is_correct': False,
                          'scenario_update': 'Aynı ilaçlar yeniden başlanınca tablo iki gün içinde tekrarladı.',
                          'teaching_point': 'Serotonerjik ilaçlar birlikte kullanılmamalı; antidepresan tedavisi '
                                            'psikiyatri ile yeniden düzenlenir.'},
                         {'text': 'Monitörlü yatışta 24 saat izlemek, süren bulgularda siproheptadin vermek; '
                                  'psikiyatriyle tedaviyi düzenleyip etkileşen ilaçları öğretmek',
                          'is_correct': True,
                          'explanation': 'Bulgular çoğu zaman 24 saat içinde geriler. Siproheptadin serotonin '
                                         'reseptörlerini bloke eder. Aileye ve hastaya etkileşen ilaçların öğretilmesi '
                                         'tekrarı önler.',
                          'new_finding': 'Siproheptadin bir kez verildi. Yirmi dört saatte bulgular tamamen geriledi. '
                                         'Psikiyatri antidepresan planını düzenledi; etkileşen ilaç listesi verildi ve '
                                         'ağrı için parasetamol önerildi.'},
                         {'text': 'Sertralinin kesilmesiyle depresyonun kötüleşeceğini düşünüp yerine hemen yüksek doz '
                                  'başka bir antidepresan başlamak',
                          'is_correct': False,
                          'scenario_update': 'Yeni serotonerjik ilaç tablonun gerilemesini engelledi.',
                          'teaching_point': 'Yeni antidepresan, ilaçlar vücuttan uzaklaşıp tablo düzeldikten sonra '
                                            'psikiyatri tarafından planlanır.'},
                         {'text': 'Tablonun alerjik reaksiyon olduğunu kabul edip ilaçları alerji kaydına işlemek ve '
                                  'antihistaminikle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Yanlış kayıt nedeniyle hasta gereksiz yere etkili tedavilerden mahrum '
                                             'bırakıldı.',
                          'teaching_point': 'Bu tablo alerji değil ilaç etkileşimidir; kayıt buna göre '
                                            'yapılmalıdır.'}]}]},
 {'id': 'S99',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '3 Aylık (5.6 kg)',
  'gender': 'Erkek',
  'complaint': 'Gaz sancısı için evde hazırlanan bitki çayı içirildikten sonra uyandırılamayan, nefesi yavaşlayan '
               'bebek',
  'history': "Ailesi Afyonkarahisar'ın bir köyünde yaşıyor. Annesi anlatıyor: 'Bebek geceleri çok ağlıyordu, "
             'babaannesi köyden getirdiği kurutulmuş bitki kozalarını kaynatıp çayından bir biberon içirdi, eskiden '
             'hep böyle yapılırmış. İki saat sonra derin uykuya daldı, uyanmıyor, nefesi çok yavaşladı, dudakları '
             "morardı.' Ateş, kusma, ishal yok. Daha önce sağlıklı, term doğmuş. Evde başka ilaç yok.",
  'final_diagnosis': 'Haşhaş Kozası (Papaver somniferum) Çayına Bağlı Opiat Zehirlenmesi',
  'disposition': 'Nalokson ile Solunum Depresyonunun Geri Döndürülmesi, Gerekirse Nalokson İnfüzyonu ve En Az 24 Saat '
                 'Monitörlü Çocuk Yoğun Bakım İzlemi',
  'case_pearl': 'Bazı yörelerde ağlayan bebekleri uyutmak için haşhaş kozası çayı verilmesi geleneği sürmektedir; '
                'içerdiği morfin ve kodein süt çocuklarında ağır solunum depresyonu yapar. Üçlü tablo: bilinç '
                'azalması, solunum depresyonu (bradipne, apne) ve iğne ucu pupillerdir. Önce hava yolu açılır ve '
                'balon-maske ile ventilasyon sağlanır. Nalokson 0.1 mg/kg İV (veya İM, intranazal, intraosseöz) '
                'verilir, yanıta göre tekrarlanır. Naloksonun etki süresi opiatlardan kısa olduğundan solunum '
                'depresyonu yeniden gelişebilir; infüzyon ve en az 12-24 saatlik monitörlü gözlem gerekir. Doz miktarı '
                'belirsiz olduğu için zehir danışma merkezi (UZEM 114) aranır. Aileye eğitim ve gerekirse sosyal '
                'hizmet desteği sağlanır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Stabilizasyon',
             'question': 'Uyandırılamayan ve nefesi yavaşlamış bu bebekte ilk yaklaşımınız nedir?',
             'options': [{'text': 'Hava yolunu açıp balon-maske ile ventile etmek, oksijen vermek, monitörize edip kan '
                                  'şekerini ölçmek ve pupillere bakmak',
                          'is_correct': True,
                          'explanation': 'Yetersiz solunumda öncelik ventilasyondur. Kan şekeri bilinç bozukluğunun '
                                         'geri döndürülebilir nedenidir. Pupil boyutu zehirlenme tablosunu ayırt '
                                         'etmede yol gösterir.',
                          'new_finding': 'Başlangıçta: SS 6/dk, yüzeyel; SpO2 %78; KTA 92/dk; KB 68/38 mmHg; ısı '
                                         '36.0°C. Ağrılı uyarana minimal yanıt. Pupiller iğne ucu, ışığa yanıt zor '
                                         'değerlendiriliyor. Kas tonusu azalmış. Kan şekeri 82 mg/dL. Balon-maske '
                                         "ventilasyonla SpO2 %96'ya çıktı."},
                         {'text': 'Bebeği uyandırmak için sırtına vurmak, yüzüne soğuk su serpmek ve ayak tabanlarını '
                                  'uyarmaya devam etmek',
                          'is_correct': False,
                          'scenario_update': "Uyarılar solunumu düzeltmedi; SpO2 %65'e düştü ve bradikardi gelişti.",
                          'teaching_point': 'Solunum depresyonunda uyarı değil ventilasyon desteği gerekir.'},
                         {'text': 'Bitkiyi midesinden boşaltmak için hemen nazogastrik sondadan gastrik lavaj yapmak '
                                  've aktif kömür vermek',
                          'is_correct': False,
                          'scenario_update': 'Hava yolu korunmadan yapılan lavaj sırasında bebek aspirasyon yaptı.',
                          'teaching_point': 'Bilinci bozuk bebekte hava yolu güvenliği sağlanmadan gastrik '
                                            'dekontaminasyon yapılmaz.'},
                         {'text': 'Uyku hali nedeniyle sepsis kabul edip lomber ponksiyon ve kültür almak, bu sırada '
                                  'bebeği kendi solunumuyla izlemek',
                          'is_correct': False,
                          'scenario_update': 'Girişim sırasında bebek apneye girdi; ventilasyon geç başlandı.',
                          'teaching_point': 'Önce hava yolu ve solunum desteklenir; girişimler hasta stabilken '
                                            'yapılır.'}]},
            {'stage_title': 'Antidot Tedavisi',
             'question': 'Balon-maske ile ventile edilen ve iğne ucu pupilleri olan bu bebekte sıradaki adım nedir?',
             'options': [{'text': 'Flumazenil 0.01 mg/kg İV vermek ve bilinçte düzelme olmazsa dozu tekrarlamak',
                          'is_correct': False,
                          'scenario_update': 'Flumazenil etkisiz kaldı; bebek ventilasyon desteğine bağımlı kaldı.',
                          'teaching_point': 'Flumazenil benzodiazepin antidotudur; bu tabloda etkisizdir.'},
                         {'text': 'Nalokson 0.1 mg/kg İV vermek, yanıta göre tekrarlamak ve solunum yeniden '
                                  'baskılanırsa infüzyon başlamak',
                          'is_correct': True,
                          'explanation': 'Nalokson reseptör düzeyinde etkiyi geri çevirir. Etkisi alınan maddeden kısa '
                                         'sürdüğü için solunum depresyonu tekrarlayabilir ve infüzyon gerekebilir.',
                          'new_finding': 'Nalokson 0.56 mg İV verildi. İki dakika içinde bebek ağlamaya başladı, SS '
                                         '36/dk, SpO2 %98 (oda havası), pupiller genişledi. Yetmiş beşinci dakikada '
                                         'yeniden uykuya meyil ve SS 14/dk görüldü; tekrar doz sonrası nalokson '
                                         'infüzyonu başlandı.'},
                         {'text': 'Uyanmasını sağlamak için kafein yükleme dozu ve ardından aminofilin infüzyonu '
                                  'başlamak',
                          'is_correct': False,
                          'scenario_update': 'Solunum düzelmedi ve taşikardi gelişti.',
                          'teaching_point': 'Solunum uyarıcılar bu tabloda yetersizdir; özgül antidot kullanılır.'},
                         {'text': 'Antidot vermeden hemen entübe edip mekanik ventilasyona almak ve maddenin vücuttan '
                                  'kendiliğinden atılmasını yoğun bakımda beklemek',
                          'is_correct': False,
                          'scenario_update': 'Kolayca geri döndürülebilecek bir tablo için invaziv girişim yapıldı.',
                          'teaching_point': 'Özgül antidot hızla etkili olduğunda entübasyon çoğu zaman gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Antikolinerjik bitki zehirlenmesi',
                          'is_correct': False,
                          'scenario_update': 'Pupiller geniş değil iğne ucuydu ve cilt kuru-sıcak değildi.',
                          'teaching_point': 'Antikolinerjik tabloda midriyazis, taşikardi ve sıcak kuru cilt görülür.'},
                         {'text': 'İnfantil botulizm',
                          'is_correct': False,
                          'scenario_update': 'Pupiller iğne ucuydu ve nalokson tabloyu hızla düzeltti.',
                          'teaching_point': 'Bebek botulizminde kabızlık, inen paralizi ve geniş pupiller görülür; '
                                            'nalokson etkisizdir.'},
                         {'text': 'Haşhaş kozası çayına bağlı opiat zehirlenmesi',
                          'is_correct': True,
                          'explanation': 'Kurutulmuş bitki kozası çayından sonra gelişen bilinç azalması, solunum '
                                         'depresyonu, iğne ucu pupiller ve naloksona hızlı yanıt haşhaş kozası çayına '
                                         'bağlı opiat zehirlenmesini gösterir.',
                          'new_finding': 'Tanı: Haşhaş kozası çayına bağlı opiat zehirlenmesi. İdrar taramasında '
                                         'morfin pozitif.'},
                         {'text': 'İstismara bağlı kafa travması',
                          'is_correct': False,
                          'scenario_update': 'Fontanel normaldi, travma bulgusu yoktu ve nalokson bilinci tamamen '
                                             'düzeltti.',
                          'teaching_point': 'Kafa travmasında nalokson yanıtı beklenmez; fontanel ve göz dibi '
                                            'muayenesi önemlidir.'}]},
            {'stage_title': 'İzlem ve Taburculuk Planı',
             'question': 'Bu bebek için en uygun izlem planı hangisidir?',
             'options': [{'text': 'Naloksona iyi yanıt verdiği için bir saat gözlemleyip evde dikkatli olmaları '
                                  'önerisiyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Bebek evde nalokson etkisi geçince yeniden apneye girdi.',
                          'teaching_point': 'Naloksonun etkisi kısa sürer; uzun süreli monitörlü gözlem gerekir.'},
                         {'text': "Nalokson infüzyonuyla en az 24 saat yoğun bakımda izlemek; UZEM 114'e danışıp "
                                  'aileyi eğitmek',
                          'is_correct': True,
                          'explanation': 'Alınan miktar belirsiz ve etki uzun olabileceğinden yakın izlem gerekir. '
                                         'Aile eğitimi geleneksel uygulamanın tekrarını önler.',
                          'new_finding': 'Nalokson infüzyonu 14 saat sürdü, kesildikten sonra 12 saat solunum '
                                         'depresyonu tekrarlamadı. Aileye eğitim verildi, sosyal hizmet ev ziyareti '
                                         'planladı. Bebek kolik için önerilerle taburcu edildi.'},
                         {'text': 'Bağımlılık gelişmiş olabileceğini düşünüp bebeğe bir hafta azalan dozda oral morfin '
                                  'başlamak',
                          'is_correct': False,
                          'scenario_update': 'Tek seferlik maruziyette gereksiz opiat verildi ve bebek yeniden '
                                             'uyuklamaya başladı.',
                          'teaching_point': 'Tek seferlik maruziyette yoksunluk tedavisi gerekmez.'},
                         {'text': 'Aileye hiçbir açıklama yapmadan polise bildirip bebeği ailesinden ayırmak ve koruma '
                                  'altına almak',
                          'is_correct': False,
                          'scenario_update': 'Bilgisizlikten kaynaklanan durum cezalandırıcı bir süreçle yönetildi; '
                                             'aile hekime güvenini kaybetti.',
                          'teaching_point': 'Sosyal hizmet değerlendirmesi önemlidir; ancak öncelik eğitim ve destek '
                                            'odaklı yaklaşımdır.'}]}]},
 {'id': 'S100',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '6 Yaşında (21 kg)',
  'gender': 'Kız',
  'complaint': 'Piknikten döndükten birkaç saat sonra başlayan saçma konuşma, olmayan şeyleri görme, kızarıklık ve '
               'ateş',
  'history': "Annesi anlatıyor: 'Öğlen piknikteydik. Kuzeniyle birlikte oynarken bahçe kenarındaki dikenli meyveli bir "
             'bitkinin içindeki küçük siyah tohumlardan yemişler. Akşam olunca kızım havada bir şeyler toplamaya '
             'çalıştı, örümcek var diye bağırdı, bizi tanımıyor. Yüzü kıpkırmızı, ateşi çıktı, ağzı kurumuş, öğleden '
             "beri çişini yapmadı.' Kuzeninde de benzer şikâyetler başlamış. İlaç kullanımı yok. Daha önce sağlıklı.",
  'final_diagnosis': 'Datura stramonium (Tatula) Tohumu Yutmasına Bağlı Antikolinerjik Zehirlenme',
  'disposition': 'Benzodiazepin, Soğutma, Mesane Kateteri ve Monitörizasyon ile Yatış; Ağır Merkezi Bulgularda Zehir '
                 'Danışmanlığıyla Fizostigmin',
  'case_pearl': "Türkiye'de kırsal alanda sık bulunan bu bitkinin tohumları atropin ve skopolamin içerir. Klasik "
                "tablo: 'tavşan gibi sıcak (hipertermi), kemik gibi kuru (terlemenin kesilmesi), pancar gibi kırmızı "
                '(kızarıklık), yarasa gibi kör (midriyazis, bulanık görme), tavuk gibi deli (deliryum, halüsinasyon), '
                "dolu mesane (idrar retansiyonu)'. Taşikardi ve bağırsak seslerinde azalma eşlik eder. Benzer yaştaki "
                'birden fazla çocukta aynı anda deliryum ortak bir maruziyeti düşündürür. Tedavi: ajitasyonda '
                'benzodiazepin, dış soğutma, mesane kateteri ve monitörizasyon. Mide boşalması yavaşladığından hava '
                'yolu güvenliyse geç dönemde de aktif kömür düşünülebilir. Ağır deliryum ve normal QRS varlığında '
                'zehir danışmanlığıyla fizostigmin verilebilir. Fenotiyazinler ve antihistaminikler tabloyu '
                'ağırlaştırır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Deliryumdaki bu çocukta muayenede hangi bulgulara odaklanırsınız?',
             'options': [{'text': 'Ateş ve bilinç değişikliği nedeniyle ensefalit kabul edip öykü ve muayeneyi kısa '
                                  'tutarak lomber ponksiyon yapmak',
                          'is_correct': False,
                          'scenario_update': 'Ajite çocukta ponksiyon zorlu oldu; BOS normal geldi ve tanı gecikti.',
                          'teaching_point': 'Ortak maruziyet öyküsü ve tipik fizik bulgular varken önce zehirlenme '
                                            'değerlendirilmelidir.'},
                         {'text': 'Vital bulgular ve ısıyı ölçmek; pupilleri, cilt nemini ve rengini, bağırsak '
                                  'seslerini ve mesane dolgunluğunu değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Zehirlenme tablolarının ayrımı pupil, cilt nemi, bağırsak sesleri ve mesane '
                                         'muayenesiyle yapılır. Bu bulgular tedavi seçimini doğrudan etkiler.',
                          'new_finding': 'Ateş 38.7°C, KTA 162/dk, KB 124/80 mmHg, SS 24/dk, SpO2 %98. Yüz ve gövdede '
                                         'yaygın kızarıklık, cilt sıcak ve kuru, koltuk altı kuru. Pupiller çok geniş, '
                                         'ışığa yanıt zayıf. Ağız mukozası kuru. Bağırsak sesleri azalmış. Suprapubik '
                                         'bölgede dolu mesane ele geliyor. Ajite, havada bir şeyler topluyor, yönelimi '
                                         'bozuk. Kan şekeri 104 mg/dL.'},
                         {'text': 'Halüsinasyonlar nedeniyle akut psikoz kabul edip çocuk psikiyatrisine yönlendirmek '
                                  've İM haloperidol yapmak',
                          'is_correct': False,
                          'scenario_update': 'Haloperidol sonrası ısı ve kalp hızı arttı, çocuk nöbet geçirdi.',
                          'teaching_point': 'Bu yaşta akut psikoz nadirdir; organik ve toksik nedenler önce dışlanır.'},
                         {'text': 'Kızarıklık nedeniyle alerjik reaksiyon kabul edip İV antihistaminik ve '
                                  'kortikosteroid vermek',
                          'is_correct': False,
                          'scenario_update': 'Antihistaminik sonrası ajitasyon ve taşikardi belirgin arttı.',
                          'teaching_point': 'Antihistaminikler benzer reseptör etkileri nedeniyle bu tabloyu '
                                            'ağırlaştırabilir.'}]},
            {'stage_title': 'Acil Tedavi',
             'question': 'Ajite, ateşli ve idrar yapamayan bu çocukta en uygun acil tedavi nedir?',
             'options': [{'text': 'Ateş için İV parasetamol verip ajitasyon için fiziksel kısıtlama uygulamak ve '
                                  'kendiliğinden düzelmeyi beklemek',
                          'is_correct': False,
                          'scenario_update': 'Kısıtlama ısıyı artırdı; mesane dolgunluğu huzursuzluğu sürdürdü.',
                          'teaching_point': 'Isı artışı terleme kaybı ve kas aktivitesinden kaynaklanır; dış soğutma '
                                            've sedasyon gerekir.'},
                         {'text': 'Monitörize edip İV benzodiazepin vermek, dış soğutma yapmak, mesane kateteri takmak '
                                  've EKG çekmek',
                          'is_correct': True,
                          'explanation': 'Benzodiazepin ajitasyonu ve kas aktivitesini azaltır. Mesanenin boşaltılması '
                                         'huzursuzluğun önemli bir nedenini giderir. EKG ileti bozukluğunu gösterir ve '
                                         'olası antidot kararını etkiler.',
                          'new_finding': 'Midazolam İV sonrası sakinleşti. Kateterden 420 mL idrar boşaltıldı. Dış '
                                         "soğutmayla ısı 37.9°C'ye indi. EKG: sinüs taşikardisi, QRS 78 ms, QTc 430 "
                                         'ms. Zehir danışma merkezi (UZEM 114) ile görüşüldü.'},
                         {'text': 'Mide içeriğini boşaltmak için ipeka şurubuyla kusturmak ve ardından bol su içirmek',
                          'is_correct': False,
                          'scenario_update': 'Bilinci bulanık çocuk kusarken aspirasyon yaptı.',
                          'teaching_point': 'Kusturma önerilmez; bilinç bozukluğunda aspirasyon riski yüksektir.'},
                         {'text': 'Fizostigmini EKG ve danışmanlık olmadan hızlı İV bolus vermek ve gerekirse beş '
                                  'dakikada bir tekrarlamak',
                          'is_correct': False,
                          'scenario_update': 'Hızlı ve kontrolsüz uygulama bradikardi, bronkospazm ve aşırı salgı '
                                             'artışına yol açtı.',
                          'teaching_point': 'Fizostigmin yalnızca uygun hastada, EKG değerlendirmesi ve uzman '
                                            'danışmanlığıyla yavaş verilir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Organofosfat zehirlenmesi',
                          'is_correct': False,
                          'scenario_update': 'Pupiller dar değil genişti, cilt ve mukozalar kuruydu.',
                          'teaching_point': 'Organofosfatta miyozis, aşırı salgı, terleme, bradikardi ve ishal '
                                            'görülür.'},
                         {'text': 'Sempatomimetik zehirlenme',
                          'is_correct': False,
                          'scenario_update': 'Cilt terli değil kuruydu ve mesane dolgunluğu vardı.',
                          'teaching_point': 'Sempatomimetik tabloda cilt terlidir ve bağırsak sesleri normaldir.'},
                         {'text': 'Tatula tohumuna bağlı antikolinerjik zehirlenme',
                          'is_correct': True,
                          'explanation': 'Dikenli meyveli bitkinin siyah tohumlarını yedikten sonra iki çocukta '
                                         'birlikte gelişen deliryum, halüsinasyon, ateş, kızarıklık, kuru cilt ve '
                                         'mukozalar, midriyazis, taşikardi, azalmış bağırsak sesleri ve idrar '
                                         'retansiyonu tatula tohumuna bağlı antikolinerjik zehirlenmeyi gösterir.',
                          'new_finding': 'Tanı: Datura stramonium (tatula) tohumu yutmasına bağlı antikolinerjik '
                                         'zehirlenme.'},
                         {'text': 'Viral ensefalit',
                          'is_correct': False,
                          'scenario_update': 'Aynı anda iki çocuk etkilenmişti, ortak bir maruziyet ve tipik toksik '
                                             'bulgular vardı.',
                          'teaching_point': 'Birden fazla çocukta aynı anda deliryum ortak toksik maruziyeti '
                                            'düşündürür.'}]},
            {'stage_title': 'Yatış ve İzlem',
             'question': 'Bu çocuk ve kuzeni için en uygun plan hangisidir?',
             'options': [{'text': 'Sakinleşen çocuğu iki saat gözlem sonrası taburcu etmek, kuzenin evde izlenmesinin '
                                  'yeterli olduğunu söylemek',
                          'is_correct': False,
                          'scenario_update': 'Kuzen evde nöbet geçirdi; çocuğun deliryumu gece yeniden başladı.',
                          'teaching_point': 'Tohumların etkisi 24-48 saat sürebilir; tüm maruz kalanlar '
                                            'değerlendirilmelidir.'},
                         {'text': 'Ağır deliryuma rağmen benzodiazepin verilmesini yasaklamak ve kuzeni aynı odada '
                                  'aynı tedaviyle izlemek',
                          'is_correct': False,
                          'scenario_update': 'Kuzenin daha az bitki tükettiği anlaşıldı; aynı tedavi gereksiz '
                                             'sedasyona yol açtı.',
                          'teaching_point': 'Tedavi her çocuğun klinik bulgularına göre ayrı ayrı belirlenir.'},
                         {'text': 'Monitörlü yatışta 24 saat izlemek, gerektikçe benzodiazepin vermek; kuzeni de '
                                  'değerlendirmeye almak ve bitkiyi aileye tanıtmak',
                          'is_correct': True,
                          'explanation': 'Mide boşalması yavaşladığı için etkiler uzun sürer ve dalgalanabilir. Aynı '
                                         'maruziyetteki çocuk da değerlendirilmelidir. Bitkinin tanıtılması tekrar '
                                         'maruziyeti önler.',
                          'new_finding': 'Çocuk 30 saatte tamamen düzeldi, sonraki saatlerde idrarını kendiliğinden '
                                         'yaptı. Kuzende daha hafif bulgular vardı ve 18 saatte düzeldi. Aileye ve '
                                         'okul öncesi kuruma bitki hakkında bilgi verildi.'},
                         {'text': 'Karaciğere zarar verebileceğini düşünüp N-asetilsistein infüzyonu başlamak ve '
                                  'günlük karaciğer testleriyle izlemek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz tedavi verildi; karaciğer testleri sürekli normal kaldı.',
                          'teaching_point': 'N-asetilsistein parasetamol zehirlenmesinin antidotudur; bu tabloda '
                                            'endikasyonu yoktur.'}]}]}]
