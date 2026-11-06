# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Yeşil Alan Vakaları (Part 6: G51 - G60)
Odak: Bulantı, Kusma, Karın Ağrısı, İshal (GİS Acilleri - Yeşil Alan Ayaktan Yönetim)
Kılavuzlar: ESPGHAN, AAP, NASPGHAN, NICE, Centor/McIsaac
"""

GREEN_CASES_PART6 = [{'id': 'G51',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '4 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Ateşli hastalık sırasında bir gündür süren tekrarlayan kusma, ağızda meyvemsi koku ve halsizlik',
  'history': "Annesi anlatıyor: 'İki gündür hafif ateşi ve boğaz ağrısı var, iştahı tamamen kesildi, neredeyse hiçbir "
             'şey yemedi. Dün akşamdan beri bir yudum su içse bile kusuyor; kusmuk safralı değil. Ağzından çürük elma '
             'gibi bir koku geliyor. Halsiz, sürekli uyumak istiyor. Bugün bir kez az miktarda çiş yaptı. Ailede '
             "diyabet yok ama komşumuz şekeri olabilir dedi.' Son haftalarda çok su içme veya sık idrara çıkma tarif "
             'edilmiyor. Tartı: 16 kg.',
  'final_diagnosis': 'Açlık Ketozuna Bağlı Ketotik Kusma (Asetonemik Kusma)',
  'disposition': 'Yeşil Alanda Yatak Başı Glukoz-Keton Değerlendirmesi, Ondansetron ve Glukozlu Oral Sıvı ile Ketozun '
                 'Kırılması ve Taburculuk',
  'case_pearl': 'Ateşli hastalık ve açlık sırasında küçük çocuklarda yağ yıkımına bağlı ketonemi kusmayı tetikler, '
                'kusma da açlığı derinleştirerek kısır döngü yaratır. Yatak başı kan şekeri ve keton ölçümü diyabetik '
                'ketoasidozu (hiperglisemi + asidoz) ve hipoglisemiyi ayırt etmek için zorunludur. Normoglisemik, '
                'asidozu olmayan çocukta tedavi glukoz içeren sıvılarla ketozun kırılmasıdır; oral tolerans '
                'sağlanamazsa %5-10 dekstrozlu intravenöz sıvı verilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Açlık, ateş ve tekrarlayan kusma ile gelen, ağzında meyvemsi koku olan bu halsiz çocukta ilk '
                         'değerlendirmede önceliğiniz nedir?',
             'options': [{'text': 'Bilinç düzeyini, solunum paternini, hidrasyon bulgularını ve karın muayenesini '
                                  'değerlendirirken eş zamanlı yatak başı kapiller kan şekeri ve keton ölçümü yapmak',
                          'is_correct': True,
                          'explanation': 'Kusma ve ketotik nefes kokusu olan çocukta hipoglisemi ve hiperglisemik '
                                         'ketoasidoz hayatı tehdit eden ayırıcı tanılardır; yatak başı glukoz ve keton '
                                         'ölçümü dakikalar içinde yönetimi belirler. Derin-hızlı solunum asidozu, '
                                         'karın bulguları cerrahi nedeni düşündürür.',
                          'new_finding': 'Vital Bulgular: Ateş 37.4°C, KTA 112/dk, SS 22/dk (düzenli, derin-hızlı '
                                         'solunum yok), SpO2 %99, TA 96/60 mmHg, KDZ 2 sn. Halsiz ancak seslenince '
                                         'gözlerini açıyor, koopere. Ağız mukozası kuru, gözyaşı az. Farenks '
                                         'hiperemik. Karın yumuşak, hassasiyet yok. Kapiller kan şekeri 68 mg/dL, '
                                         'kapiller beta-hidroksibutirat 3.8 mmol/L.'},
                         {'text': 'Ağızdaki koku ve ailenin endişesi nedeniyle diyabetik ketoasidoz protokolünü '
                                  'başlatıp kan şekeri sonucu gelmeden serum fizyolojik bolusu ve insülin infüzyonu '
                                  'hazırlamak',
                          'is_correct': False,
                          'scenario_update': 'İnsülin hazırlığı sürerken ölçülen kan şekeri 68 mg/dL geldi; protokol '
                                             'iptal edildi, gereksiz yere damar yolu açıldı.',
                          'teaching_point': 'Tedavi kararı yatak başı ölçümle verilmelidir; normoglisemik çocukta '
                                            'insülin ölümcül hipoglisemiye yol açar.'},
                         {'text': 'Kusmayı durdurmak için muayeneden önce intramüsküler metoklopramid yapıp yarım saat '
                                  'sonra çocuğa bol miktarda su içirerek oral toleransı denemek',
                          'is_correct': False,
                          'scenario_update': 'Metoklopramid sonrası çocuk yine kustu; şekersiz su ile ketoz devam etti '
                                             've halsizliği arttı.',
                          'teaching_point': 'Metoklopramid çocuklarda ekstrapiramidal etki riski taşır; ayrıca glukoz '
                                            'içermeyen sıvılar keton üretimini durdurmaz.'},
                         {'text': 'Halsizlik ve uykuya meyil nedeniyle meningeal irritasyon bulgularını ayrıntılı '
                                  'değerlendirip ensefalit olasılığına karşı acil kraniyal görüntüleme planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ense sertliği ve fokal nörolojik bulgu saptanmadı. Görüntüleme '
                                             'planlanırken kan şekeri ölçülmedi ve çocuk bir kez daha kustu.',
                          'teaching_point': 'Kusan, halsiz çocukta ilk yapılması gereken basit ve hızlı test kapiller '
                                            'kan şekeridir; nörolojik bulgusu olmayan çocukta görüntüleme öncelikli '
                                            'değildir.'}]},
            {'stage_title': 'Tetkik ve İlk Destek Kararı',
             'question': 'Kan şekeri 68 mg/dL, kapiller ketonu 3.8 mmol/L olan, solunumu düzenli ve karnı rahat bu '
                         'çocukta sonraki adımınız nedir?',
             'options': [{'text': 'Kan şekeri normal olduğu için keton ölçümünü tekrarlamadan çocuğa yalnızca su ve '
                                  'ayran içirerek oral toleransı denemek ve uyumasına izin vermek',
                          'is_correct': False,
                          'scenario_update': 'Glukoz içermeyen sıvılar sonrası çocuk iki kez kustu; bir saat sonra kan '
                                             "şekeri 58 mg/dL'ye düştü.",
                          'teaching_point': 'Ketonemide glukoz içeren sıvı gereklidir; şekersiz sıvılar ve uyku ile '
                                            'açlığın uzaması hipoglisemiyi derinleştirir.'},
                         {'text': 'Hipoglisemi sınırına yakın olduğu için damar yolu açıp 2 mL/kg %10 dekstroz bolusu '
                                  'vermek ve ardından %0.9 NaCl ile idame sıvıya geçmek',
                          'is_correct': False,
                          'scenario_update': 'Dekstroz bolusu sonrası kan şekeri 110 mg/dL oldu; ancak dekstroz '
                                             'içermeyen idame sıvıyla ketoz sürdü ve kusmalar devam etti.',
                          'teaching_point': 'Ketozu kırmak için sürekli glukoz sağlanmalıdır; bolus sonrası '
                                            'dekstrozsuz sıvı ketozu düzeltmez. Bilinci açık ve kusması kontrol '
                                            'edilebilen çocukta önce oral glukoz denenir.'},
                         {'text': 'Venöz kan gazı ile asidozu değerlendirmek, kiloya uygun tek doz oral ondansetron '
                                  'vermek ve 20-30 dakika sonra glukozlu sıvıyla küçük yudumlarla oral deneme '
                                  'başlatmak',
                          'is_correct': True,
                          'explanation': "Normoglisemik ketonemide kan gazı belirgin asidozu ve DKA'yı dışlamak için "
                                         'yeterlidir. Ondansetron kusmayı kırar; glukoz içeren sıvılar insülin '
                                         'salınımını uyararak lipolizi ve keton üretimini durdurur.',
                          'new_finding': 'Venöz kan gazı: pH 7.33, HCO3 18 mmol/L, Na 136 mEq/L, K 4.1 mEq/L. 16 kg '
                                         'için 2 mg oral ondansetron verildi. 30 dakika sonra 5 dakikada bir 10 mL '
                                         'elma suyu ve glukozlu ORS başlandı; 1 saatte 180 mL içti, kusmadı.'},
                         {'text': 'Ateş odağını belirlemek amacıyla tam kan sayımı, CRP, kan kültürü, boğaz kültürü ve '
                                  'tam idrar tetkikini isteyip sonuçlar gelene kadar oral alımı kapalı tutmak',
                          'is_correct': False,
                          'scenario_update': 'Sonuçlar 2 saat içinde geldi ve belirgin bir bakteriyel odak göstermedi; '
                                             "bu sürede aç bekleyen çocuğun ketonu 4.5 mmol/L'ye yükseldi.",
                          'teaching_point': 'Ketotik çocukta oral alımın kapatılması ketozu derinleştirir; odak '
                                            'araştırması klinik bulgulara göre seçici yapılmalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Açlık ve ateşli hastalık zemininde kusma, yüksek keton, normal-düşük kan şekeri ve belirgin '
                         'olmayan asidozu olan bu çocukta tanı nedir?',
             'options': [{'text': 'Yağ asidi oksidasyon bozukluğu',
                          'is_correct': False,
                          'scenario_update': 'Bu bozukluklarda açlıkta hipoketotik hipoglisemi beklenir; bu çocukta '
                                             'keton belirgin yüksek.',
                          'teaching_point': 'Yüksek ketonemi, yağ asidi oksidasyonunun çalıştığını gösterir.'},
                         {'text': 'Döngüsel kusma sendromu atağı',
                          'is_correct': False,
                          'scenario_update': 'Öyküde benzer, stereotipik ve aralarında tamamen sağlıklı dönemler olan '
                                             'tekrarlayan ataklar yok.',
                          'teaching_point': 'Döngüsel kusma tanısı tekrarlayan ve birbirine benzer atakların varlığını '
                                            'gerektirir.'},
                         {'text': 'Diyabetik ketoasidoz',
                          'is_correct': False,
                          'scenario_update': 'Kan şekeri 68 mg/dL, pH 7.33; hiperglisemi ve belirgin asidoz yok.',
                          'teaching_point': 'DKA tanısı hiperglisemi (>200 mg/dL), pH <7.30 veya HCO3 <18 ve ketonemi '
                                            'gerektirir.'},
                         {'text': 'Açlık ketozuna bağlı ketotik kusma',
                          'is_correct': True,
                          'explanation': 'Enfeksiyon ve açlık sırasında gelişen ketonemi, normal-düşük kan şekeri ve '
                                         'hafif metabolik etkilenme ketotik (asetonemik) kusma ile uyumludur.',
                          'new_finding': 'Tanı: Açlık Ketozuna Bağlı Ketotik Kusma (Asetonemik Kusma).'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Glukozlu sıvıyı tolere eden ve halsizliği azalan bu çocuğun taburculuk planı nasıl '
                         'olmalıdır?',
             'options': [{'text': 'Sık aralıklarla glukoz içeren sıvılar ve karbonhidrat ağırlıklı küçük öğünler '
                                  'önermek, ateşi kontrol etmek ve kusma, uykuya meyil veya idrar azalmasında dönmeyi '
                                  'anlatmak',
                          'is_correct': True,
                          'explanation': 'Ketozun tekrarlamaması için açlık süresi kısaltılmalı, glukoz içeren sıvı ve '
                                         'karbonhidrat ağırlıklı öğünler sık verilmelidir. Oral alım yetersiz kalırsa '
                                         'intravenöz dekstroz gerekebileceği için dönüş kriterleri net anlatılır.',
                          'new_finding': "İki saat sonra kapiller keton 1.6 mmol/L'ye geriledi, çocuk bisküvi yedi ve "
                                         'idrar yaptı. Aile eğitimiyle taburcu edildi; ertesi gün telefonla yapılan '
                                         'kontrolde kusmanın tekrarlamadığı öğrenildi.'},
                         {'text': 'Ailede diyabet olmasa da olası başlangıç dönemini kaçırmamak için taburculukta '
                                  'HbA1c, C-peptid ve adacık otoantikorlarını isteyip endokrinolojiye yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Sonuçlar normal geldi; aile gereksiz endokrinoloji randevusu nedeniyle '
                                             'kaygı yaşadı.',
                          'teaching_point': 'Normoglisemik ketotik kusmada poliüri-polidipsi gibi bulgular yoksa '
                                            'diyabet taraması gerekmez.'},
                         {'text': 'Kusma tekrarlarsa evde kullanmak üzere oral ondansetron reçete etmek, yağlı ve '
                                  'proteinli besinleri öne çıkarıp şekerli içecekleri kısıtlamasını önermek',
                          'is_correct': False,
                          'scenario_update': 'Yağlı beslenme önerisi sonrası çocuk ertesi gün yine kusmaya başladı ve '
                                             'halsizlik tekrarladı.',
                          'teaching_point': 'Ketotik kusmada karbonhidrat ağırlıklı, sık ve küçük öğünler önerilir; '
                                            'yağ ağırlıklı beslenme ketozu artırır.'},
                         {'text': 'Ketonun tamamen kaybolmasını görmek için çocuğu 12 saat %5 dekstrozlu intravenöz '
                                  'sıvıyla gözleme almak ve sabah idrar ketonu negatifse taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Oral alımı iyi olan çocuk gece boyunca acilde kaldı; gereksiz damar yolu '
                                             'nedeniyle huzursuzlaştı.',
                          'teaching_point': 'Kapiller keton düşmeye başlayan ve oral glukozu tolere eden çocuk taburcu '
                                            'edilebilir; idrar ketonu kandan geç negatifleşir.'}]}]},
 {'id': 'G52',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '3 Yaşında',
  'gender': 'Kız',
  'complaint': 'Üç gündür düşmeyen yüksek ateş, karın ağrısı ve kusma',
  'history': "Annesi anlatıyor: 'Üç gündür 39°C'ye çıkan ateşi var. Karnım ağrıyor diye ağlıyor, iki gündür günde 2-3 "
             'kez kusuyor ama aralarda su ve çorba içebiliyor. İshal veya öksürük yok. Tuvalet eğitimi yeni bitti, son '
             "iki gündür altına kaçırıyor ve çişini yaparken ağlıyor.' Daha önce benzer ateşli hastalık geçirmemiş. "
             'Aşıları tam. Tartı: 14 kg.',
  'final_diagnosis': 'Akut Piyelonefrit (Ateşli İdrar Yolu Enfeksiyonu)',
  'disposition': 'Yeşil Alanda Oral Tolerans Doğrulaması, Kültür Sonrası Oral Sefalosporin ve Üriner USG Planıyla '
                 'Ayaktan Tedavi',
  'case_pearl': 'Küçük çocukta ateş, kusma ve karın ağrısı üriner sistem enfeksiyonunun sık prezentasyonudur; dizüri '
                've yeni başlayan idrar kaçırma önemli ipuçlarıdır. Tanı uygun yöntemle alınmış idrar örneğinde piyüri '
                've kültürde anlamlı üremeye dayanır. Genel durumu iyi, oral tolere edebilen çocukta oral 3. kuşak '
                'sefalosporin (sefiksim 8 mg/kg/gün) parenteral tedavi kadar etkilidir; toplam süre 7-14 gündür. İlk '
                'ateşli enfeksiyon sonrası üriner USG önerilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Üç gündür yüksek ateşi, karın ağrısı ve kusması olan, son günlerde altını ıslatan bu çocukta '
                         'muayenede neye odaklanmalısınız?',
             'options': [{'text': 'Karın ağrısı ve kusma nedeniyle sağ alt kadran hassasiyeti, psoas ve obturator '
                                  'bulgularını değerlendirip çocuk cerrahisi konsültasyonunu muayeneyle eş zamanlı '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'Peritoneal bulgu yoktu; cerrahi ekip akut batın düşünmediğini belirtti. '
                                             'Kostovertebral açı ve genitalya muayenesi yapılmamıştı.',
                          'teaching_point': 'Küçük çocukta ateş ve karın ağrısı sıklıkla karın dışı veya üriner '
                                            'kaynaklıdır; muayene sistematik olmalıdır.'},
                         {'text': 'Ateşi düşürüp yeniden değerlendirmek için muayeneden önce ibuprofen vermek, bir '
                                  'saat sonra genel durumu iyiyse odak aramadan taburculuğu planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ateş düştükten sonra çocuk rahatladı ve aile taburculuk bekledi; ateşin '
                                             'odağı belirlenmedi.',
                          'teaching_point': 'Antipiretik yanıtı ciddi bakteriyel enfeksiyonu dışlamaz; üç günlük '
                                            'ateşte odak mutlaka araştırılmalıdır.'},
                         {'text': 'Genel durum ve hidrasyonu değerlendirip karın, suprapubik bölge ve kostovertebral '
                                  'açıyı muayene etmek, dış genitalyayı ve odak açısından KBB-akciğeri incelemek',
                          'is_correct': True,
                          'explanation': 'Ateşli küçük çocukta odak araştırması sistematik yapılmalıdır. '
                                         'Kostovertebral açı ve suprapubik hassasiyet üst ve alt üriner tutulumu '
                                         'düşündürür; dış genitalya muayenesi vulvovajinit ve labial füzyon gibi '
                                         'nedenleri dışlar.',
                          'new_finding': 'Vital Bulgular: Ateş 38.8°C, KTA 126/dk, SS 24/dk, SpO2 %99, TA 98/62 mmHg, '
                                         'KDZ 2 sn. Huzursuz ama çevreyle ilgili, mukozalar hafif kuru. KBB ve akciğer '
                                         'muayenesi doğal. Karın yumuşak; suprapubik ve sağ kostovertebral açıda '
                                         'belirgin hassasiyet. Defans, rebound yok. Dış genitalya doğal, akıntı yok.'},
                         {'text': 'Üç günlük yüksek ateş nedeniyle döküntü, konjonktival hiperemi, dudak '
                                  'değişiklikleri ve ekstremite ödemi aramak, servikal lenf nodlarını ayrıntılı '
                                  'değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Mukokutanöz bulgu saptanmadı. Karın ve kostovertebral açı muayenesi '
                                             'ikinci planda kaldı.',
                          'teaching_point': 'Uzamış ateşte vaskülit bulguları sorgulanmalıdır ancak bu çocukta dizüri '
                                            've idrar kaçırma üriner odağa yönlendirir.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Suprapubik ve sağ kostovertebral açı hassasiyeti olan, tuvalet eğitimli bu 3 yaşındaki kızda '
                         'idrar değerlendirmesini nasıl planlarsınız?',
             'options': [{'text': 'Yalnızca idrar strip testi yapıp lökosit esteraz ve nitrit pozitifse kültür '
                                  'göndermeden ampirik tedavi başlatmak ve kontrolde stripi tekrarlamak',
                          'is_correct': False,
                          'scenario_update': 'Kültür alınmadan antibiyotik başlandı; 48 saat sonra ateş sürünce '
                                             'etkenin duyarlılığı bilinmediği için tedavi düzenlenemedi.',
                          'teaching_point': 'Ateşli üriner enfeksiyon şüphesinde antibiyotik öncesinde kültür '
                                            'alınmalıdır; kültür hem tanıyı doğrular hem tedaviyi yönlendirir.'},
                         {'text': 'Temiz orta akım idrarında tam idrar tetkiki ve kültür göndermek; sistemik etkilenme '
                                  'için hemogram, CRP ve kreatinin istemek',
                          'is_correct': True,
                          'explanation': 'Tuvalet eğitimli çocukta temiz orta akım idrarı kültür için uygundur. Piyüri '
                                         've nitrit pozitifliği ön tanıyı destekler; hemogram, CRP ve kreatinin üst '
                                         'üriner tutulum ve böbrek fonksiyonunu değerlendirmeye yardımcı olur.',
                          'new_finding': 'Tam idrar: dansite 1.020, lökosit esteraz +++, nitrit pozitif, mikroskopide '
                                         'her alanda bol lökosit ve lökosit kümeleri, bol bakteri. Kültür gönderildi. '
                                         'Lökosit 14.800/mm³ (%78 nötrofil), CRP 42 mg/L, kreatinin 0.38 mg/dL.'},
                         {'text': 'Karın ağrısının cerrahi nedenlerini dışlamak için önce batın ultrasonografisi '
                                  'istemek, ultrasonda böbrek bulgusu varsa idrar örneği alarak tetkik etmek',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografide sağ böbrekte hafif ekojenite artışı dışında bulgu '
                                             'yoktu; idrar tetkiki 2 saat gecikti.',
                          'teaching_point': 'Ateşli çocukta idrar tetkiki ilk basamaktır; ultrasonografi tanı koymaz, '
                                            'anatomik değerlendirme için tedaviden sonra planlanır.'},
                         {'text': 'Perineye yapıştırılan steril torba ile idrar toplayıp hem tam idrar tetkiki hem de '
                                  'kültür göndermek, kültürde üreme olursa tedaviyi başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Torba kültüründe karışık üreme bildirildi; sonuç yorumlanamadı ve örnek '
                                             'tekrarlanmak zorunda kalındı, tedavi gecikti.',
                          'teaching_point': 'Torba ile alınan örneğin kontaminasyon oranı yüksektir; kültür için orta '
                                            'akım, kateter veya suprapubik aspirasyon örneği kullanılmalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Ateş, kusma, dizüri, kostovertebral açı hassasiyeti, piyüri, nitrit pozitifliği ve CRP '
                         'yüksekliği olan bu çocukta tanı nedir?',
             'options': [{'text': 'Akut piyelonefrit',
                          'is_correct': True,
                          'explanation': 'Ateş, sistemik inflamasyon bulguları ve kostovertebral açı hassasiyeti ile '
                                         'birlikte piyüri ve nitrit pozitifliği üst üriner sistem enfeksiyonunu '
                                         'gösterir.',
                          'new_finding': 'Tanı: Akut Piyelonefrit (ateşli idrar yolu enfeksiyonu). Kültür sonucu '
                                         'beklenmekte.'},
                         {'text': 'Akut sistit',
                          'is_correct': False,
                          'scenario_update': 'Yüksek ateş, kusma, kostovertebral açı hassasiyeti ve CRP yüksekliği alt '
                                             'üriner sistemle sınırlı bir enfeksiyonu açıklamaz.',
                          'teaching_point': 'Sistit genellikle ateşsiz veya düşük ateşlidir ve sistemik bulgu vermez.'},
                         {'text': 'Akut apandisit',
                          'is_correct': False,
                          'scenario_update': 'Sağ alt kadranda lokalize peritoneal bulgu yok; piyüri ve nitrit '
                                             'pozitifliği üriner kaynağı gösteriyor.',
                          'teaching_point': 'Apandisitte hafif piyüri olabilir ancak nitrit pozitifliği ve '
                                            'kostovertebral hassasiyet üriner enfeksiyonu destekler.'},
                         {'text': 'Nonspesifik vulvovajinit',
                          'is_correct': False,
                          'scenario_update': 'Dış genitalya doğal, akıntı yok ve tablo sistemik ateşle seyrediyor.',
                          'teaching_point': 'Vulvovajinit dizüri yapabilir ancak yüksek ateş ve böbrek hassasiyeti '
                                            'beklenmez.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': "Acilde ondansetron sonrası oral sıvıyı tolere eden, genel durumu iyi bu 14 kg'lık çocuğun "
                         'tedavisi nasıl olmalıdır?',
             'options': [{'text': 'Oral sefiksim başlamakla birlikte tekrarlayan enfeksiyonları önlemek için tedavi '
                                  'bitiminde düşük doz profilaksi ve işeme sistoüretrografisi planlamak',
                          'is_correct': False,
                          'scenario_update': 'İlk enfeksiyon sonrası rutin profilaksi ve invaziv işeme grafisi planı '
                                             'aileyi kaygılandırdı; çocuk gereksiz radyasyona maruz kalacaktı.',
                          'teaching_point': 'İlk ateşli enfeksiyon sonrası USG normalse rutin işeme sistoüretrografisi '
                                            "ve profilaksi önerilmez; tekrarlayan enfeksiyon veya anormal USG'de "
                                            'düşünülür.'},
                         {'text': 'Oral nitrofurantoin başlayıp beş gün sürdürmek, bol sıvı ve hijyen önerileriyle '
                                  'taburcu etmek ve kültür sonucunu kontrolde değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Ateşi 72 saat sonra hâlâ sürüyordu; çocuk kusma ve halsizlikle yeniden '
                                             'başvurdu.',
                          'teaching_point': 'Nitrofurantoin böbrek parankiminde yeterli düzeye ulaşmaz; ateşli üriner '
                                            'enfeksiyonda kullanılmaz.'},
                         {'text': 'Ateşli üriner enfeksiyonun parenteral tedavi gerektirdiğini düşünüp servise '
                                  'yatırmak, intravenöz seftriakson ile 10 gün tedaviyi hastanede tamamlamak',
                          'is_correct': False,
                          'scenario_update': 'Çocuk 10 gün hastanede kaldı; ikinci günden itibaren oral alımı ve ateşi '
                                             'normal olmasına rağmen taburculuk ertelendi.',
                          'teaching_point': 'Oral tolerans sağlanmış, toksik görünümlü olmayan çocukta yatış gerekmez; '
                                            'parenteral başlanan tedavi de klinik düzelmede orale geçirilebilir.'},
                         {'text': 'Kültür sonrası oral sefiksim 8 mg/kg/gün başlayıp 7-10 güne tamamlamak, 48-72. '
                                  'saatte kontrol ve sonrasında üriner ultrasonografi planlamak',
                          'is_correct': True,
                          'explanation': 'Oral alabilen ve toksik görünümü olmayan çocukta oral 3. kuşak sefalosporin '
                                         'parenteral tedavi kadar etkilidir. 48-72 saatte ateş yanıtı ve kültür '
                                         'duyarlılığı değerlendirilir; ilk ateşli enfeksiyon sonrası üriner USG '
                                         'yapılır.',
                          'new_finding': 'Oral sefiksim başlandı. 48. saatte ateşi düştü, kusma kesildi. Kültürde '
                                         '100.000 cfu/mL sefiksime duyarlı E. coli üredi. Tedavi 10 güne tamamlandı; '
                                         'üriner USG normal bulundu.'}]}]},
 {'id': 'G53',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '8 Yaşında',
  'gender': 'Kız',
  'complaint': 'İki aydır hafta içi sabahları başlayan göbek çevresinde karın ağrısı ve bulantı',
  'history': "Ailesi anlatıyor: 'Yaklaşık iki aydır hafta içi sabahları kahvaltıdan sonra göbeğini tutup kıvranıyor, "
             'midem bulanıyor diyor. Hafta sonları ve tatilde ağrısı çoğunlukla olmuyor. Gece ağrıyla hiç uyanmıyor. '
             'Kilo kaybı, ateş, ishal veya kusması yok. Bu sabah ağrısı çok şiddetli olunca geldik. Yeni bir okula '
             "geçti, arkadaş edinmekte zorlandığını söylüyor.' Babasında yıllardır mide yanması var. Büyümesi "
             'persentilinde.',
  'final_diagnosis': 'Fonksiyonel Karın Ağrısı (Roma IV)',
  'disposition': 'Yeşil Alanda Alarm Bulgularının Dışlanması, Biyopsikososyal Açıklama, Okul Devamlılığı ve Pediatri '
                 'Poliklinik Takibi',
  'case_pearl': 'Okul çağında tekrarlayan periumbilikal ağrının çoğu fonksiyoneldir. Tanı Roma IV kriterlerine ve '
                'alarm bulgularının (gece uyandıran ağrı, kilo kaybı, büyüme geriliği, kanlı dışkı, ateş, persistan '
                'kusma, sağ kadranlarda lokalize ağrı, ailede inflamatuvar bağırsak hastalığı) yokluğuna dayanır; '
                'geniş tetkik gerekmez. Tedavide ağrının gerçek olduğunun kabulü, beyin-bağırsak ilişkisinin '
                'açıklanması, okula devamın sürdürülmesi ve gerekirse bilişsel davranışçı terapi esastır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'İki aydır hafta içi sabahları tekrarlayan göbek çevresinde ağrısı olan bu 8 yaşındaki kızda '
                         'değerlendirmenin temel amacı nedir?',
             'options': [{'text': 'Babadaki mide yanması öyküsü nedeniyle epigastrik hassasiyete odaklanıp muayeneyi '
                                  'kısa tutmak ve dışkıda Helicobacter pylori antijeni istemek',
                          'is_correct': False,
                          'scenario_update': 'Dışkı antijeni negatif geldi; alarm bulguları ve büyüme '
                                             'değerlendirilmediği için aile ne olduğunu anlamadan beklemeye devam '
                                             'etti.',
                          'teaching_point': 'Alarm bulgusu olmayan tekrarlayan karın ağrısında H. pylori araştırması '
                                            'önerilmez; tetkik ancak alarm bulgusu veya endoskopi endikasyonu varsa '
                                            'yapılır.'},
                         {'text': 'Ağrının sabah okul öncesi olması nedeniyle temaruz olasılığını değerlendirmek için '
                                  'muayeneyi kısa tutup çocukla ebeveynler olmadan görüşmeye öncelik vermek',
                          'is_correct': False,
                          'scenario_update': 'Görüşme sırasında çocuk ağrısının ciddiye alınmadığını hissetti ve '
                                             'ağladı; organik alarm bulguları sistematik sorgulanmadı.',
                          'teaching_point': "Tekrarlayan karın ağrısı gerçek bir ağrıdır; 'uydurma' yaklaşımı güveni "
                                            'zedeler. Önce alarm bulguları sistematik değerlendirilmelidir.'},
                         {'text': 'Gece uyandıran ağrı, kilo kaybı, kanlı dışkı, ateş, kusma ve aile öyküsü gibi alarm '
                                  'bulgularını sorgulayıp büyüme eğrisi, karın ve perianal muayene yapmak',
                          'is_correct': True,
                          'explanation': 'Tekrarlayan karın ağrısında organik ve fonksiyonel nedenleri ayırmanın en '
                                         'güçlü aracı alarm bulgularının sistematik sorgulanması ve büyüme ile fizik '
                                         'muayenenin değerlendirilmesidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 84/dk, TA 102/64 mmHg. Boy ve tartı 50. '
                                         'persentilde, persentil kaybı yok. Gece uyandıran ağrı, kilo kaybı, kanlı '
                                         'dışkı, ateş, kusma yok; ailede inflamatuvar bağırsak hastalığı veya çölyak '
                                         'yok. Karın yumuşak, periumbilikal hafif hassasiyet tarifliyor; organomegali, '
                                         'kitle, defans yok. Perianal bölge doğal.'},
                         {'text': 'Bu sabahki şiddetli ağrı nedeniyle oral alımı kapatıp intravenöz analjezi yapmak, '
                                  'ağrı geçene kadar seri karın muayeneleriyle acilde izlemek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk 4 saat aç bekletildi, ağrısı oyun sırasında kendiliğinden geçti; '
                                             'ailenin hastalık algısı güçlendi.',
                          'teaching_point': 'Peritoneal bulgu yokken gereksiz invaziv yaklaşım ve uzun gözlem hastalık '
                                            'davranışını pekiştirir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Alarm bulgusu olmayan, büyümesi normal ve muayenesi rahat bu çocukta tetkik yaklaşımınız '
                         'nedir?',
             'options': [{'text': 'Ailenin endişesini gidermek için tam kan sayımı, sedimantasyon, CRP, karaciğer ve '
                                  'böbrek testleri, çölyak serolojisi, dışkı kalprotektini, gaitada parazit ve batın '
                                  'ultrasonografisini birlikte istemek',
                          'is_correct': False,
                          'scenario_update': "Ultrasonografide 'ince bağırsaklarda gaz' raporu çıktı ve aile yeni bir "
                                             'hastalık olduğundan endişelendi; diğer sonuçlar normaldi.',
                          'teaching_point': 'Geniş tetkik paneli güvence vermez; anlamsız bulgular ek tetkik zinciri '
                                            've kaygıyı artırır.'},
                         {'text': 'Ağrının yemek sonrası başlaması nedeniyle laktoz intoleransı düşünerek hidrojen '
                                  'nefes testi istemek ve süt ürünlerini iki hafta kesmeyi önermek',
                          'is_correct': False,
                          'scenario_update': 'Süt ürünleri kesildi; ağrı paterni değişmedi ve okul günleriyle ilişkisi '
                                             'sürdü.',
                          'teaching_point': 'Tetkik ve diyet değişikliği klinik ipuçlarına göre yapılmalıdır; burada '
                                            'ağrının belirleyicisi okul günleridir.'},
                         {'text': 'Alarm bulgusu olmadığından en fazla tam kan sayımı ve tam idrar tetkiki ile '
                                  'yetinmek, ağrı günlüğü önermek ve sonuçları aileyle birlikte değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Alarm bulgusu olmayan çocukta tanı klinik olarak konur; birçok klinisyen '
                                         'güvence amacıyla sınırlı tarama (hemogram, idrar) yapar. Ağrı günlüğü '
                                         'tetikleyicileri ve psikososyal ilişkiyi görünür kılar.',
                          'new_finding': 'Tam kan sayımı ve tam idrar tetkiki normal. Kısa görüşmede çocuğun yeni '
                                         'okulda yalnız kaldığını, sabahları okula gitmekten çekindiğini anlattığı '
                                         'öğrenildi.'},
                         {'text': 'Ağrının sabah oluşu ve bulantı nedeniyle çocuk gastroenterolojisine yönlendirip üst '
                                  'gastrointestinal endoskopi değerlendirmesi yapılmasını istemek',
                          'is_correct': False,
                          'scenario_update': 'Endoskopi için 2 ay sonrasına randevu verildi; bu sürede çocuk okula '
                                             'düzensiz gitmeye başladı.',
                          'teaching_point': 'Alarm bulgusu olmayan tekrarlayan karın ağrısında endoskopi rutin '
                                            'önerilmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Alarm bulgusu olmayan, iki aydır okul günlerinde tekrarlayan periumbilikal ağrısı ve '
                         'psikososyal stresörü olan bu çocukta tanı nedir?',
             'options': [{'text': 'Helicobacter pylori gastriti',
                          'is_correct': False,
                          'scenario_update': 'Epigastrik ağrı, gece ağrısı veya kanama bulgusu yok; ağrı okul '
                                             'günleriyle ilişkili.',
                          'teaching_point': 'H. pylori çocukta tekrarlayan fonksiyonel ağrının nedeni olarak kabul '
                                            'edilmez.'},
                         {'text': 'Abdominal migren',
                          'is_correct': False,
                          'scenario_update': 'Saatlerce süren, bulantı-solukluk eşlik eden ve aralarında haftalarca '
                                             'tamamen sağlıklı olunan stereotipik ataklar tarif edilmiyor.',
                          'teaching_point': 'Abdominal migren paroksismal, stereotipik ve şiddetli ataklarla '
                                            'seyreder.'},
                         {'text': 'Fonksiyonel karın ağrısı',
                          'is_correct': True,
                          'explanation': 'Ayda en az 4 kez, en az 2 aydır süren, başka bir fonksiyonel tanıya uymayan, '
                                         'alarm bulgusu olmayan periumbilikal ağrı Roma IV fonksiyonel karın ağrısı '
                                         'kriterlerini karşılar; okul stresi sık bir tetikleyicidir.',
                          'new_finding': 'Tanı: Fonksiyonel Karın Ağrısı - Başka Türlü Tanımlanmamış (Roma IV).'},
                         {'text': 'Fonksiyonel dispepsi',
                          'is_correct': False,
                          'scenario_update': 'Ağrı epigastrik değil, periumbilikal; erken doyma veya postprandiyal '
                                             'dolgunluk ön planda değil.',
                          'teaching_point': 'Fonksiyonel dispepside semptomlar epigastriuma lokalizedir.'}]},
            {'stage_title': 'Tedavi ve Aile Rehberliği',
             'question': 'Bu çocuğun ve ailesinin yönetimi nasıl olmalıdır?',
             'options': [{'text': 'Ağrı atakları için iki hafta oral antispazmodik ve proton pompa inhibitörü '
                                  'başlamak, ağrının sürdüğü günlerde çocuğun evde dinlenmesine izin vermek',
                          'is_correct': False,
                          'scenario_update': 'İlaçlar ağrıyı değiştirmedi; evde kalmaya izin verilen çocuk iki hafta '
                                             'içinde 5 gün okul kaçırdı.',
                          'teaching_point': 'Okula gitmemek kaçınma döngüsünü güçlendirir; ilaçların fonksiyonel '
                                            'ağrıda katkısı sınırlıdır.'},
                         {'text': 'Ağrı şiddetli olduğunda kullanmak üzere düşük doz oral tramadol reçete edip ağrı '
                                  'günlüğüne göre doz ayarlaması için iki hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Tramadol sonrası çocukta bulantı ve uyku hali gelişti; aile ilacı keyfi '
                                             'kullanmaya başladı.',
                          'teaching_point': 'Fonksiyonel karın ağrısında opioidler kontrendikedir; bağımlılık ve '
                                            'opioid ilişkili bağırsak hiperaljezisi riski taşır.'},
                         {'text': 'Ailenin içini rahatlatmak için gastroenteroloji, çocuk psikiyatrisi ve diyetisyene '
                                  'aynı anda sevk etmek ve tüm değerlendirmeler bitene kadar okula ara verdirmek',
                          'is_correct': False,
                          'scenario_update': 'Çoklu sevk aileye ciddi bir hastalık mesajı verdi; okula ara verilmesi '
                                             'sosyal kaygıyı artırdı.',
                          'teaching_point': 'İlk basamak birinci basamak/pediatri takibi ve güvencedir; çoklu sevk ve '
                                            'okul izni hastalık algısını güçlendirir.'},
                         {'text': 'Ağrının gerçek olduğunu kabul edip beyin-bağırsak ilişkisini anlatmak, okula '
                                  'düzenli devamı sürdürmek, okul rehberliğiyle iletişim ve pediatri kontrolü '
                                  'planlamak',
                          'is_correct': True,
                          'explanation': 'Tedavinin temeli biyopsikososyal açıklama ve aileye güvencedir. Okula devam, '
                                         'kaçınma davranışını kırar; okul ile işbirliği ve gerekirse bilişsel '
                                         'davranışçı terapi en etkili yaklaşımlardır.',
                          'new_finding': 'Aile ve çocukla ağrının mekanizması konuşuldu; okul rehber öğretmeniyle '
                                         'görüşme planlandı. Bir ay sonraki kontrolde sabah ağrılarının belirgin '
                                         'azaldığı, çocuğun okula düzenli gittiği öğrenildi.'}]}]},
 {'id': 'G54',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '20 Aylık',
  'gender': 'Erkek',
  'complaint': 'Ek gıdaya geçtikten sonra giderek belirginleşen karın şişliği, açık renkli kötü kokulu ishal ve kilo '
               'kaybı',
  'history': "Annesi anlatıyor: 'Sekiz aylıkken ek gıdaya, tahıllara, bisküvi ve ekmeğe başladıktan sonra kakası "
             'giderek cıvıklaştı; açık renkli, parlak ve çok kötü kokulu. Son 6 aydır kilo almıyor, eskiden 75. '
             "persentildeydi. Karnı çok şişti, bacakları ve poposu eridi. Sürekli huysuz ve mutsuz, iştahı azaldı.' "
             'Kistik fibrozis tarama testi yenidoğanda negatif. Tartı: 9.8 kg (10. persentilin altı), boy: 82 cm (25. '
             'persentil).',
  'final_diagnosis': 'Çölyak Hastalığı (Klasik Malabsorptif Form)',
  'disposition': 'Yeşil Alandan Diyette Gluten Sürdürülerek Pediatrik Gastroenterolojiye Öncelikli Sevk ve Demir '
                 'Desteği',
  'case_pearl': 'Glutenli gıdalara geçişten sonra başlayan kronik ishal, karın distansiyonu, kas kaybı, irritabilite '
                "ve büyüme geriliği klasik çölyak tablosudur. İlk tetkik doku transglutaminaz IgA ve total IgA'dır. "
                "ESPGHAN 2020'ye göre tTG-IgA ≥10 kat yüksek ve ayrı örnekte endomisyum antikoru pozitifse biyopsisiz "
                'tanı konulabilir. Tanı doğrulanana kadar gluten kesilmemelidir; erken kesilmesi serolojiyi ve '
                'histolojiyi normalleştirerek tanıyı imkansızlaştırır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Altı aydır kilo almayan, karın şişliği ve yağlı ishali olan 20 aylık bu çocukta ilk '
                         'değerlendirmenizde neye odaklanırsınız?',
             'options': [{'text': 'Büyüme eğrisini önceki ölçümlerle karşılaştırıp beslenme öyküsünü ve başlangıçla '
                                  'ilişkisini sorgulamak, malnütrisyon, kas kaybı, distansiyon, ödem ve solukluk '
                                  'bulgularını değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Kronik ishal ve büyüme geriliğinde semptomların belirli gıdalara geçişle '
                                         'zamansal ilişkisi, büyüme eğrisi ve malnütrisyon bulguları ayırıcı tanıyı '
                                         'daraltan temel bilgilerdir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 104/dk, TA 90/58 mmHg. Tartı 75. '
                                         'persentilden 10. persentilin altına düşmüş; boy 25. persentil. Soluk, '
                                         'apatik, irritabl. Karın belirgin distandü, timpanik, hassasiyet yok. Gluteal '
                                         've uyluk kas kitlesi belirgin azalmış, cilt kıvrımları sarkık. Ödem yok. '
                                         'Hepatosplenomegali yok.'},
                         {'text': 'İrritabilite ve apati nedeniyle nörolojik muayeneye ve gelişim basamaklarına '
                                  'odaklanıp tablo nörometabolik olabilir diyerek amonyak ve laktat istemek',
                          'is_correct': False,
                          'scenario_update': 'Nörolojik muayene ve metabolik tetkikler normal geldi; gastrointestinal '
                                             'bulgular ikinci planda kaldı.',
                          'teaching_point': 'Malnütrisyonlu çocukta irritabilite sık görülür; tablonun merkezinde '
                                            'kronik ishal ve büyüme duraklaması vardır.'},
                         {'text': 'Akut gastroenterit kabul edip hidrasyon bulgularını değerlendirmek, kısa bir oral '
                                  'sıvı denemesi yapmak ve büyüme eğrisini sonraki aşı kontrolüne bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Hidrasyon normal bulundu ve çocuk ORS ile taburcu edilecekti; altı aylık '
                                             'büyüme duraklaması göz ardı edildi.',
                          'teaching_point': 'Aylardır süren ishal ve kilo alamama akut gastroenteritle açıklanamaz; '
                                            'büyüme eğrisi ilk değerlendirmenin parçasıdır.'},
                         {'text': 'Karın distansiyonu nedeniyle intraabdominal kitle olasılığını ön planda tutup derin '
                                  'palpasyon yapmak ve aynı gün acil batın ultrasonografisi istemek',
                          'is_correct': False,
                          'scenario_update': 'Kitle palpe edilmedi; ultrasonografide gazla dolu ince bağırsak ansları '
                                             'dışında bulgu yoktu. Beslenme öyküsü alınmadı.',
                          'teaching_point': 'Kronik ishal ve büyüme geriliğiyle seyreden distansiyonda malabsorpsiyon '
                                            'öncelikli düşünülmeli; görüntüleme seçici yapılmalıdır.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Tahıllara geçişten sonra başlayan kronik ishal, distansiyon ve büyüme geriliği olan bu '
                         'çocukta ilk tetkik planınız nedir?',
             'options': [{'text': 'Ter testi, dışkı elastaz ve yağ atılımını isteyip pankreas kaynaklı malabsorpsiyon '
                                  'dışlanana kadar diğer tetkikleri ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Ter testi ve elastaz normal geldi; bu süreçte bir ay kaybedildi ve çocuk '
                                             '300 g daha kaybetti.',
                          'teaching_point': 'Yenidoğan taraması negatif ve klinik tablo gluten maruziyetiyle '
                                            'ilişkiliyken ilk basamak serolojik tetkiklerdir.'},
                         {'text': 'Doku transglutaminaz IgA ile total IgA, tam kan sayımı, ferritin, albümin ve '
                                  'karaciğer testlerini istemek; diyette herhangi bir değişiklik yapmamak',
                          'is_correct': True,
                          'explanation': "Glutenle ilişkili malabsorpsiyon şüphesinde ilk tetkik tTG-IgA'dır; total "
                                         'IgA eksikliği yanlış negatifliğe yol açacağı için birlikte bakılır. '
                                         'Hemogram, ferritin ve albümin malabsorpsiyonun sonuçlarını gösterir. '
                                         'Seroloji doğru sonuç vermesi için diyette gluten sürmelidir.',
                          'new_finding': 'tTG-IgA >200 U/mL (normal üst sınır 10 U/mL; >10 kat). Total IgA 68 mg/dL '
                                         '(yaşa göre normal). Hb 9.8 g/dL, MCV 66 fL, ferritin 8 ng/mL. Albümin 3.4 '
                                         'g/dL. AST/ALT hafif yüksek (48/52 U/L).'},
                         {'text': 'Dışkıda parazit, kültür, kalprotektin ve rotavirüs antijeni isteyip sonuçlar '
                                  'normalse iki hafta sonra kontrol tartısı ile yeniden değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Dışkı tetkikleri normal geldi; iki haftalık bekleme sonunda çocuk yine '
                                             'kilo kaybetmişti.',
                          'teaching_point': 'Aylar süren ishal ve büyüme geriliğinde enfeksiyöz tetkikler tek başına '
                                            'yetersizdir; gluten ilişkili enteropati için seroloji önceliklidir.'},
                         {'text': 'Olası besin alerjisini değerlendirmek için buğday, süt ve yumurta spesifik IgE ile '
                                  'deri prick testi yapmak ve sonucu pozitif olan gıdaları diyetten çıkarmak',
                          'is_correct': False,
                          'scenario_update': 'Buğday spesifik IgE düşük pozitif geldi; aile buğdayı diyetten çıkardı, '
                                             'ardından yapılan serolojik testler yanlış negatif çıkabilecekti.',
                          'teaching_point': 'IgE aracılı alerji testleri malabsorpsiyonu açıklamaz; serolojiden önce '
                                            'gluten kesilmesi tanıyı engeller.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Gluten maruziyeti sonrası başlayan malabsorpsiyon, büyüme geriliği, demir eksikliği ve 10 '
                         'kattan yüksek tTG-IgA olan bu çocukta tanı nedir?',
             'options': [{'text': 'İnek sütü proteinine bağlı enteropati',
                          'is_correct': False,
                          'scenario_update': 'Başlangıç inek sütü değil tahıllarla ilişkili ve tTG-IgA belirgin '
                                             'yüksek.',
                          'teaching_point': 'Besin proteini enteropatisi genellikle ilk yılda başlar ve seroloji '
                                            'tanısal değildir.'},
                         {'text': 'Kistik fibrozise bağlı pankreas yetersizliği',
                          'is_correct': False,
                          'scenario_update': 'Yenidoğan taraması negatif, solunum bulgusu yok ve seroloji başka bir '
                                             'tanıyı gösteriyor.',
                          'teaching_point': 'Pankreas yetersizliğinde semptomlar genellikle ilk aylardan itibaren '
                                            'başlar.'},
                         {'text': 'Çölyak hastalığı',
                          'is_correct': True,
                          'explanation': 'Glutene geçişle başlayan kronik ishal, distansiyon, kas kaybı, büyüme '
                                         'geriliği, demir eksikliği ve 10 katı aşan tTG-IgA çölyak hastalığının klasik '
                                         'formunu gösterir.',
                          'new_finding': 'Ön Tanı: Çölyak Hastalığı (klasik form). Biyopsisiz tanı için ayrı örnekte '
                                         'endomisyum antikoru gerekir.'},
                         {'text': 'Kronik nonspesifik ishal',
                          'is_correct': False,
                          'scenario_update': 'Toddler diyaresinde büyüme normaldir; bu çocukta belirgin büyüme '
                                             'duraklaması ve kas kaybı var.',
                          'teaching_point': 'Büyüme geriliği fonksiyonel ishali dışlar.'}]},
            {'stage_title': 'Sevk ve Tedavi Planı',
             'question': 'Bu çocuk için acil servisten yapılacak en uygun plan hangisidir?',
             'options': [{'text': 'Malnütrisyon nedeniyle hastayı servise yatırıp intravenöz albümin ve parenteral '
                                  'beslenme başlatmak, tanıyı kesinleştirmek için yatışta endoskopi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Hemodinamisi stabil ve oral beslenebilen çocuk gereksiz yere yatırıldı; '
                                             'parenteral beslenme kateter enfeksiyonu riski yarattı.',
                          'teaching_point': 'Ağır malnütrisyon veya çölyak krizi yoksa ayaktan öncelikli sevk '
                                            'yeterlidir.'},
                         {'text': 'Gluteni yarıya azaltıp yoğurt ve probiyotik eklemek, demir başlamadan önce '
                                  'gastroenteroloji görüşü almak ve iki hafta sonra kilo kontrolü yapmak',
                          'is_correct': False,
                          'scenario_update': 'Kısmi gluten azaltması serolojinin güvenilirliğini düşürdü; demir '
                                             'başlanmadığı için anemi derinleşti.',
                          'teaching_point': 'Tanı sürecinde gluten miktarı değiştirilmemelidir; demir eksikliği '
                                            'beklemeden tedavi edilir.'},
                         {'text': 'Diyette glutene devam ederek pediatrik gastroenterolojiye öncelikli sevk etmek, '
                                  'demir eksikliği için oral demir başlamak ve beslenme desteği önermek',
                          'is_correct': True,
                          'explanation': "ESPGHAN'a göre tanı biyopsi ya da tTG-IgA ≥10 kat + pozitif endomisyum "
                                         'antikoru ile gastroenterolog tarafından doğrulanmalıdır; bu süreçte gluten '
                                         'sürdürülür. Demir eksikliği eş zamanlı tedavi edilir.',
                          'new_finding': 'Çocuk bir hafta içinde gastroenterolojiye görüldü; endomisyum antikoru '
                                         'pozitif bulundu ve biyopsisiz tanı doğrulandı. Glutensiz diyet ve demir '
                                         'tedavisiyle üç ayda kilo alımı yeniden başladı.'},
                         {'text': 'Seroloji kesin pozitif olduğu için hemen glutensiz diyet başlatıp aileye diyet '
                                  'listesi vermek, gastroenteroloji randevusunu diyetin etkisini görmek için üç ay '
                                  'sonraya planlamak',
                          'is_correct': False,
                          'scenario_update': 'Glutensiz diyetle çocuk iyileşti ancak gastroenterolojide doğrulayıcı '
                                             'endomisyum antikoru ve biyopsi yapılamadı; tanı belirsiz kaldı.',
                          'teaching_point': 'Tanı uzman tarafından doğrulanmadan gluten kesilmemelidir; diyet '
                                            'serolojiyi ve histolojiyi normalleştirir.'}]}]},
 {'id': 'G55',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '6 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Sağ tarafta karın ağrısı, kusma ve yüksek ateş',
  'history': "Ailesi anlatıyor: 'İki gündür 39°C'ye çıkan ateşi ve karnının sağ tarafında ağrısı var, iki kez kustu. "
             'Aile hekimimiz sağ alt tarafta hassasiyet bulunca acile gönderdi. Dünden beri ara ara kuru öksürüyor, '
             "derin nefes alınca ağrısı artıyor.' Aşıları tam, pnömokok aşısı yapılmış. Daha önce bir hastalığı yok. "
             'Tartı: 20 kg.',
  'final_diagnosis': 'Sağ Alt Lob Lober Pnömoni (Diyafragmatik Plevral İrritasyona Bağlı Yansıyan Karın Ağrısı)',
  'disposition': 'Yeşil Alandan Yüksek Doz Oral Amoksisilin ve 48 Saatlik Kontrolle Ayaktan Tedavi',
  'case_pearl': 'Alt lob pnömonisinde diyafragmatik plevranın irritasyonu ağrıyı karına yansıtabilir ve tablo akut '
                'batını taklit eder. Ateşli karın ağrısında solunum sayısı, oksijen satürasyonu ve akciğer '
                'oskültasyonu atlanmamalıdır. Hipoksemisi ve ağır solunum sıkıntısı olmayan, oral alabilen çocukta '
                'yüksek doz oral amoksisilin (90 mg/kg/gün, 2 dozda) ayaktan tedavide ilk seçenektir; 48-72 saatte '
                'klinik yanıt değerlendirilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Ateş, kusma ve sağ taraflı karın ağrısıyla sevk edilen bu çocukta ilk değerlendirmeniz nasıl '
                         'olmalıdır?',
             'options': [{'text': 'Kusma nedeniyle önce ondansetron ve intravenöz parasetamol vermek, ağrı ve ateş '
                                  'düştükten sonra karın muayenesini tekrarlayarak cerrahi gerekliliği değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Ateş düştü ama takipne devam etti; vital bulgular ve akciğer '
                                             'oskültasyonu kaydedilmeden değerlendirme gecikti.',
                          'teaching_point': 'Semptomatik tedavi öncesi vital bulgular ve sistemik muayene kayıt altına '
                                            'alınmalıdır.'},
                         {'text': 'Sevk nedeni doğrultusunda oral alımı kapatıp intravenöz sıvı başlatmak ve karın '
                                  'muayenesini çocuk cerrahisinin değerlendirmesiyle birlikte yapmak',
                          'is_correct': False,
                          'scenario_update': 'Cerrahi ekip karında gerçek defans bulmadı; solunum sayısı ve akciğer '
                                             'muayenesi yapılmadan bir saat geçti.',
                          'teaching_point': 'Sevk tanısı yeniden değerlendirilmeden kabul edilmemelidir; ateşli karın '
                                            'ağrısında sistemik muayene tamamlanmalıdır.'},
                         {'text': 'Solunum sayısı ve oksijen satürasyonu dahil vital bulguları almak, akciğerleri '
                                  'dinlemek, ardından karın muayenesinde gerçek defans ve rebound aramak',
                          'is_correct': True,
                          'explanation': 'Ateşli karın ağrısında takipne, hipoksemi ve akciğer oskültasyon bulguları '
                                         'karın dışı nedenleri ortaya koyar. Yansıyan ağrıda karında yüzeyel '
                                         'hassasiyet olabilir ancak istemsiz defans ve rebound beklenmez.',
                          'new_finding': 'Vital Bulgular: Ateş 39.1°C, KTA 128/dk, SS 34/dk (takipneik), SpO2 %96 (oda '
                                         'havası), TA 102/64 mmHg. Burun kanadı solunumu ve inleme yok, hafif '
                                         'interkostal çekilme. Sağ akciğer bazalinde solunum sesleri azalmış, '
                                         'bronşiyal solunum sesi ve ince raller. Karında sağ üst ve alt kadranda '
                                         'yüzeyel hassasiyet; istemsiz defans ve rebound yok. Derin inspiryumla ağrı '
                                         'artıyor.'},
                         {'text': 'Sağ alt kadran hassasiyeti nedeniyle risk skorunu hesaplamak için tam kan sayımı, '
                                  'CRP ve batın ultrasonografisini muayeneyi tamamlamadan istemek',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografide apendiks görüntülenemedi ve sonuç belirsiz raporlandı; '
                                             'solunum bulguları değerlendirilmediği için tablo karıştı.',
                          'teaching_point': 'Tetkikler eksiksiz bir muayeneden sonra seçilmelidir; tam muayene '
                                            'gereksiz görüntülemeyi önler.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Takipneik, sağ bazalde bronşiyal solunum sesi olan ve karında gerçek peritoneal bulgusu '
                         'olmayan bu çocukta hangi tetkik uygundur?',
             'options': [{'text': 'Ateş, sağ taraflı karın ağrısı ve kusma nedeniyle intravenöz kontrastlı batın ve '
                                  'alt toraks bilgisayarlı tomografisi çekip cerrahiye danışmak',
                          'is_correct': False,
                          'scenario_update': 'Tomografide akciğer bazalinde bulgu görüldü, batın normaldi; çocuk '
                                             'akciğer grafisiyle konabilecek tanı için yüksek radyasyona maruz kaldı.',
                          'teaching_point': 'Çocukta ilk basamak düşük radyasyonlu ve hedefe yönelik tetkiktir; '
                                            'tomografi rutin değildir.'},
                         {'text': 'Tek yönlü akciğer grafisi istemek; genel durumu değerlendirmek için tam kan sayımı '
                                  've CRP almak, klinik gerektirmedikçe batın görüntülemesi yapmamak',
                          'is_correct': True,
                          'explanation': 'Ateş, takipne ve fokal oskültasyon bulgusu olan çocukta akciğer grafisi '
                                         'karın ağrısının kaynağını gösterir. Rutin kan tetkiki hafif olgularda '
                                         'zorunlu değildir ancak tanısal belirsizlik ve yatış kararında yardımcıdır.',
                          'new_finding': 'Akciğer grafisi (PA): Sağ alt zonda homojen dansite artışı, içinde hava '
                                         'bronkogramları, sağ hemidiyafram konturunda silinme. Sinüsler açık, sıvı '
                                         'izlenmedi. Lökosit 16.400/mm³ (%82 nötrofil), CRP 68 mg/L.',
                          'image': 'assets/images/cxr_lobar_pneumonia.png',
                          'image_caption': 'Akciğer Grafisi (PA)'},
                         {'text': 'Sevk tanısını dışlamak için önce batın ultrasonografisi istemek, apendiks normalse '
                                  'akciğer grafisini ertesi gün kontrol muayenesinde değerlendirmek ve sonuç gelene '
                                  'kadar çocuğu aç tutmak',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografide apendiks görülemedi ve sonuç belirsiz kaldı; akciğer '
                                             'grafisi ertelendiği için tedavi başlanmadı.',
                          'teaching_point': 'Akciğer bulguları olan ateşli çocukta öncelikli tetkik akciğer '
                                            'grafisidir; batın görüntülemesi seçici yapılmalıdır.'},
                         {'text': 'Nazofaringeal sürüntüden solunum yolu viral PCR paneli göndermek ve sonuç viral '
                                  'gelirse antibiyotiksiz izlem planlayıp ateş için antipiretik önermek',
                          'is_correct': False,
                          'scenario_update': "PCR'de rinovirüs pozitif geldi; fokal akciğer bulguları olan çocuk "
                                             'antibiyotiksiz taburcu edilecekti.',
                          'teaching_point': 'Viral pozitiflik bakteriyel koenfeksiyonu dışlamaz; fokal bulgu '
                                            'varlığında görüntüleme ve klinik karar esastır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Ateş, takipne, sağ bazalde bronşiyal solunum sesi, grafide hava bronkogramlı homojen opasite '
                         've yansıyan karın ağrısı olan bu çocukta tanı nedir?',
             'options': [{'text': 'Akut viral bronşit',
                          'is_correct': False,
                          'scenario_update': 'Fokal konsolidasyon bulgusu, yüksek ateş ve inflamatuvar yanıt viral '
                                             'bronşitle uyumlu değil.',
                          'teaching_point': 'Bronşitte grafide lober opasite beklenmez.'},
                         {'text': 'Akut apandisit',
                          'is_correct': False,
                          'scenario_update': 'Karında istemsiz defans ve rebound yok; ağrı derin inspiryumla artıyor '
                                             've akciğer bulguları belirgin.',
                          'teaching_point': 'Alt lob tutulumu akut batını taklit edebilir.'},
                         {'text': 'Sağ alt lob lober pnömoni',
                          'is_correct': True,
                          'explanation': 'Ateş, takipne, fokal bronşiyal solunum sesi ve hava bronkogramlı homojen '
                                         'lober opasite tipik bakteriyel pnömoniyi gösterir; diyafragmatik plevra '
                                         'irritasyonu ağrıyı karına yansıtır.',
                          'new_finding': 'Tanı: Sağ Alt Lob Lober Pnömoni (yansıyan karın ağrısı ile).'},
                         {'text': 'Parapnömonik plevral efüzyon',
                          'is_correct': False,
                          'scenario_update': 'Grafide kostofrenik sinüsler açık, sıvı izlenmiyor.',
                          'teaching_point': 'Efüzyon kuşkusunda grafide sinüs kapanması veya menisküs görülür; USG ile '
                                            'doğrulanır.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': "SpO2'si %96 olan, oral alabilen ve ciddi solunum sıkıntısı bulunmayan bu 20 kg'lık çocuğun "
                         'tedavisi nasıl olmalıdır?',
             'options': [{'text': 'Lober tutulum nedeniyle servise yatırıp intravenöz ampisilin 200 mg/kg/gün başlamak '
                                  've klinik düzelme sonrası kontrol akciğer grafisi çekerek taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Oral tedaviye uygun çocuk 4 gün hastanede kaldı; kontrol grafisi '
                                             'gereksiz radyasyon ekledi.',
                          'teaching_point': 'Lober tutulum tek başına yatış endikasyonu değildir; hipoksemi, ağır '
                                            'solunum sıkıntısı ve oral intolerans yatışı belirler. Komplike olmayan '
                                            'olguda kontrol grafisi gerekmez.'},
                         {'text': 'Atipik etkenleri de kapsamak için yüksek doz amoksisiline ek olarak oral '
                                  'klaritromisin başlamak ve ayaktan izlemle 48 saat sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Kombinasyon tedavisiyle çocukta bulantı ve ishal gelişti; tipik lober '
                                             'tabloda makrolidin ek yararı olmadı.',
                          'teaching_point': 'Tipik lober pnömonide ampirik makrolid eklenmesi rutin önerilmez; atipik '
                                            'etken şüphesinde düşünülür.'},
                         {'text': 'Tek doz intramüsküler seftriakson yapıp ertesi gün oral sefuroksim aksetil ile on '
                                  'güne tamamlamak ve tedavi sonunda kontrol akciğer grafisi planlamak',
                          'is_correct': False,
                          'scenario_update': 'İntramüsküler enjeksiyon ağrılıydı; geniş spektrumlu tedavi gereksizdi '
                                             've kontrol grafisi yönetimi değiştirmedi.',
                          'teaching_point': 'Ayaktan tedavide ilk seçenek dar spektrumlu yüksek doz amoksisilindir; '
                                            'rutin kontrol grafisi önerilmez.'},
                         {'text': 'Yüksek doz oral amoksisilin 90 mg/kg/gün iki dozda başlamak, ateş ve ağrı için '
                                  'parasetamol önermek, 48 saatte kontrol ve solunum sıkıntısında dönüşü anlatmak',
                          'is_correct': True,
                          'explanation': 'Hipoksemisi ve ağır solunum sıkıntısı olmayan, oral alabilen çocukta IDSA ve '
                                         'BTS önerisi yüksek doz oral amoksisilindir. Klinik yanıt 48-72 saatte '
                                         'değerlendirilir; yanıtsızlıkta efüzyon gibi komplikasyonlar araştırılır.',
                          'new_finding': 'Oral amoksisilin başlandı. 48. saatteki kontrolde ateşi düşmüş, solunum '
                                         "sayısı 24/dk'ya inmiş ve karın ağrısı kaybolmuştu. Tedavi tamamlandı."}]}]},
 {'id': 'G56',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '7 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Bir haftadır halsizlik, bulantı ve iştahsızlık; son iki gündür gözlerde sararma ve koyu renkli idrar',
  'history': "Annesi anlatıyor: 'Bir hafta önce hafif ateşi, halsizliği ve bulantısı başladı, hiçbir şey yemek "
             'istemedi, karnının sağ üst tarafı ağrıyordu. Ateşi geçti ama iki gündür gözlerinin akı sarardı, çişi çay '
             "rengi, kakası açık renkli oldu. Sınıfında üç arkadaşında da benzer şikayet olmuş.' Kan nakli, ilaç veya "
             'bitki çayı kullanımı yok. Aşı kartında 18. ay sonrası takvim aşılarının yapılmadığı görüldü (aile göç '
             'nedeniyle aşıları kaçırmış). Tartı: 24 kg.',
  'final_diagnosis': 'Akut Viral Hepatit A',
  'disposition': 'Yeşil Alanda Karaciğer Sentez Fonksiyonunun Doğrulanması, Destek Tedavisi, Temaslı Profilaksisi ve '
                 'Bildirim ile Ayaktan İzlem',
  'case_pearl': 'Okul çağında prodrom (halsizlik, bulantı, sağ üst kadran ağrısı) sonrası ateşin düşüp sarılığın '
                "başlaması ve kümelenme hepatit A'yı düşündürür. Tanı anti-HAV IgM ile konur. Prognozu belirleyen "
                'transaminaz düzeyi değil, sentez fonksiyonu (INR), kan şekeri ve bilinç durumudur; INR ≥1.5 veya '
                'ensefalopati akut karaciğer yetmezliği kriteridir. Tedavi destekleyicidir; parasetamol düşük dozda '
                'kısa süre kullanılabilir, hepatotoksik ilaç ve bitkisel ürünlerden kaçınılır. Temaslılara iki hafta '
                'içinde aşı ile profilaksi önerilir ve bildirim zorunludur.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Prodrom sonrası sarılık, koyu idrar ve açık renkli dışkısı olan bu 7 yaşındaki çocukta '
                         'muayenede öncelikle neyi değerlendirirsiniz?',
             'options': [{'text': 'Sağ üst kadran ağrısı nedeniyle Murphy bulgusunu aramak ve safra yolu taşı '
                                  'olasılığına karşı muayeneyi karın palpasyonuyla sınırlı tutup cerrahiye danışmak',
                          'is_correct': False,
                          'scenario_update': 'Murphy bulgusu negatifti. Bilinç, kanama ve maruziyet değerlendirilmeden '
                                             'cerrahi konsültasyon istendi; cerrahi ekip akut cerrahi tablo düşünmedi.',
                          'teaching_point': 'Prodrom ve kümelenme sonrası gelişen sarılıkta öncelik karaciğer '
                                            'fonksiyonunu tehdit eden bulguları aramaktır; safra taşı çocukta '
                                            'nadirdir.'},
                         {'text': 'Sınıftaki kümelenme nedeniyle izolasyon önlemlerine odaklanıp çocuğu ayrı bir odaya '
                                  'almak ve muayeneyi laboratuvar sonuçları geldikten sonra ayrıntılandırmak',
                          'is_correct': False,
                          'scenario_update': 'Çocuk bir saat odada bekletildi; ensefalopati ve kanama bulguları '
                                             'sorgulanmadan zaman geçti.',
                          'teaching_point': 'Temas önlemleri gereklidir ancak sistematik muayeneyi geciktirmemelidir.'},
                         {'text': 'Bulantı ve iştahsızlık nedeniyle önce intravenöz sıvı ve ondansetron başlatmak, '
                                  'sarılığın derecesini değerlendirmek için transkutan bilirubin ölçümü yapmak',
                          'is_correct': False,
                          'scenario_update': 'İntravenöz sıvı başlandı; çocuk oral alabildiği halde damar yolu açıldı '
                                             've karaciğer yetmezliği bulguları sistematik değerlendirilmedi.',
                          'teaching_point': 'Transkutan ölçüm yenidoğan dışında güvenilir değildir; oral alabilen '
                                            'çocukta intravenöz sıvı gerekmez.'},
                         {'text': 'Bilinç ve davranış değişikliğini, asteriksisi, kanama bulgularını, hidrasyonu ve '
                                  'karaciğer-dalak boyutunu değerlendirip ilaç, bitki ve toksin maruziyetini '
                                  'sorgulamak',
                          'is_correct': True,
                          'explanation': 'Sarılıklı çocukta ilk öncelik akut karaciğer yetmezliği bulgularını '
                                         '(ensefalopati, kanama) erkenden tanımaktır. Karaciğer boyutu, hassasiyet, '
                                         'dalak ve ilaç-bitki maruziyeti ayırıcı tanıyı yönlendirir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.2°C, KTA 92/dk, SS 20/dk, TA 104/66 mmHg. Bilinç '
                                         'açık, oryante, davranış değişikliği ve asteriksis yok. Skleralar ikterik. '
                                         'Peteşi, ekimoz, burun kanaması yok. Karaciğer kot kavsini 3 cm geçiyor, '
                                         'kenarı yumuşak ve hassas. Dalak ele gelmiyor. Asit yok. Hidrasyonu iyi. İlaç '
                                         'olarak yalnızca iki gün parasetamol kullanılmış (15 mg/kg, günde 3 kez).'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Bilinci açık, kanama bulgusu olmayan ve hepatomegalisi olan bu sarılıklı çocukta hangi '
                         'tetkikler öncelikli olarak istenmelidir?',
             'options': [{'text': 'Kolestaz paterni nedeniyle önce batın ultrasonografisi ve manyetik rezonans '
                                  'kolanjiyografi isteyip laboratuvar tetkiklerini görüntüleme sonucuna göre planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografide hepatomegali ve safra kesesi duvar ödemi dışında bulgu '
                                             'yoktu; MR kolanjiyografi için sedasyon gerekecekti.',
                          'teaching_point': 'Hepatosellüler hasar paterni olan çocukta ilk basamak laboratuvar ve '
                                            'viral seroloji olmalıdır; ileri görüntüleme seçici kullanılır.'},
                         {'text': "AST, ALT ve bilirubin düzeylerini istemek, transaminazlar 1000 U/L'nin üzerindeyse "
                                  'hastayı karaciğer nakil merkezine sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'ALT 1840 U/L geldi; sentez fonksiyonu bilinmeden çocuk nakil merkezine '
                                             'sevk edilmek üzereydi.',
                          'teaching_point': 'Transaminaz yüksekliği prognozu belirlemez; sentez fonksiyonu (INR), kan '
                                            'şekeri ve bilinç durumu belirleyicidir.'},
                         {'text': 'Yalnızca total bilirubin ve tam idrar tetkiki isteyip idrarda bilirubin pozitifse '
                                  'ek tetkik yapmadan aile hekimi kontrolü ile taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'İdrarda bilirubin pozitif bulundu; sentez fonksiyonu ve etiyoloji '
                                             'değerlendirilmeden çocuk taburcu edilecekti.',
                          'teaching_point': 'Sarılıklı çocukta INR ve kan şekeri bakılmadan güvenli taburculuk kararı '
                                            'verilemez.'},
                         {'text': 'Transaminazlar, total-direkt bilirubin, INR, kan şekeri, albümin ve tam kan sayımı '
                                  'ile birlikte hepatotropik virüs serolojilerini istemek',
                          'is_correct': True,
                          'explanation': 'Akut hepatitte sentez fonksiyonu (INR, albümin) ve kan şekeri yetmezlik '
                                         'riskini gösterir. Akut viral seroloji paneli (A, B ve C tipi belirteçler) '
                                         'etiyolojiyi belirler.',
                          'new_finding': 'AST 1420 U/L, ALT 1840 U/L, total bilirubin 5.8 mg/dL, direkt 4.1 mg/dL, INR '
                                         '1.1, kan şekeri 92 mg/dL, albümin 3.9 g/dL, hemogram normal. Viral seroloji: '
                                         'A tipi IgM antikoru pozitif; B tipi yüzey antijeni ve çekirdek IgM '
                                         'negatif.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Prodrom sonrası sarılık, belirgin transaminaz yüksekliği, normal INR ve A tipi IgM antikoru '
                         'pozitifliği olan bu çocukta tanı nedir?',
             'options': [{'text': 'Otoimmün hepatit',
                          'is_correct': False,
                          'scenario_update': 'Kümelenme, akut prodrom ve viral seroloji pozitifliği otoimmün süreci '
                                             'düşündürmez.',
                          'teaching_point': 'Otoimmün hepatit viral etiyoloji dışlandıktan sonra düşünülür.'},
                         {'text': 'Parasetamol hepatotoksisitesi',
                          'is_correct': False,
                          'scenario_update': 'Terapötik dozda kısa süreli kullanım ve pozitif anti-HAV IgM bu tanıyı '
                                             'desteklemez.',
                          'teaching_point': 'Parasetamol toksisitesi aşırı doz öyküsü ve genellikle prodrom olmadan '
                                            'gelişir.'},
                         {'text': 'Akut hepatit A',
                          'is_correct': True,
                          'explanation': 'Okul kümelenmesi, aşısız çocuk, prodrom sonrası sarılık, hepatosellüler '
                                         "hasar ve anti-HAV IgM pozitifliği akut hepatit A'yı doğrular. INR normal "
                                         'olduğundan karaciğer yetmezliği yoktur.',
                          'new_finding': 'Tanı: Akut Viral Hepatit A (sentez fonksiyonu korunmuş).'},
                         {'text': 'Koledok kisti',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonda safra yollarında dilatasyon yok; tablo hepatosellüler.',
                          'teaching_point': 'Koledok kistinde kolestatik patern ve safra yolu dilatasyonu beklenir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': "Oral alabilen, INR'si normal bu çocuğun yönetimi nasıl olmalıdır?",
             'options': [{'text': 'Akut karaciğer yetmezliği gelişme riskine karşı çocuğu servise yatırıp intravenöz '
                                  'dekstrozlu sıvı başlatmak ve transaminazlar normale dönene kadar hastanede tutmak',
                          'is_correct': False,
                          'scenario_update': 'Stabil çocuk iki hafta hastanede kaldı; transaminazlar haftalar içinde '
                                             'yavaş düştüğü için taburculuk gereksiz uzadı.',
                          'teaching_point': 'INR normal, bilinci açık ve oral alabilen çocuk ayaktan izlenir; yatış '
                                            'ölçütü transaminaz değil sentez fonksiyonu ve klinik bulgulardır.'},
                         {'text': 'Ev temaslılarına profilaksi için immünoglobulin yapmak ve çocuğa enfeksiyonu '
                                  'sınırlamak amacıyla antiviral tedavi başlayıp bir hafta sonra kontrol etmek',
                          'is_correct': False,
                          'scenario_update': 'Antiviral tedavi için bir endikasyon bulunmadığı belirtildi; sağlıklı '
                                             'okul çağı temaslılarda immünoglobulin yerine aşı tercih edilecekti.',
                          'teaching_point': 'Hepatit A için antiviral tedavi yoktur; 12 ay-40 yaş sağlıklı '
                                            'temaslılarda temas sonrası profilakside tercih aşıdır.'},
                         {'text': 'Karaciğeri korumak için ursodeoksikolik asit ve silimarin başlamak, yağ ve protein '
                                  'kısıtlı diyet önermek ve iki hafta okula gönderilmemesini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Kısıtlı diyetle çocuk iştahsızlaşıp kilo kaybetti; ilaçlar seyri '
                                             'değiştirmedi.',
                          'teaching_point': "Akut hepatit A'da spesifik tedavi yoktur; diyet kısıtlaması ve "
                                            'hepatoprotektif ürünlerin yararı gösterilmemiştir.'},
                         {'text': 'Destek tedavisi, gerekirse kısa süreli düşük doz parasetamol, sarılık '
                                  'başlangıcından bir hafta okula ara, temaslılara aşı profilaksisi, bildirim ve 3-5 '
                                  'günde INR kontrolü',
                          'is_correct': True,
                          'explanation': 'Tedavi destekleyicidir; hepatotoksik ilaç ve bitkisel ürünlerden kaçınılır. '
                                         'Bulaştırıcılık sarılık başlangıcından yaklaşık bir hafta sonra azalır. Ev ve '
                                         'sınıf temaslılarına iki hafta içinde aşı uygulanır; INR ve bilinç izlemi '
                                         'karaciğer yetmezliğini erken yakalamak için yapılır.',
                          'new_finding': 'Bildirim yapıldı, kardeşe ve sınıf temaslılarına hepatit A aşısı önerildi. '
                                         'Dördüncü gün kontrolünde INR 1.0, bilirubin 4.2 mg/dL; çocuk iştahla yemek '
                                         'yiyordu. Üç haftada sarılık geriledi.'}]}]},
 {'id': 'G57',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '15 Aylık',
  'gender': 'Kız',
  'complaint': 'Geçirilmiş ishal sonrasında süt ve yoğurt alınca tekrarlayan köpüklü sulu dışkılama, şişkinlik ve '
               'pişik',
  'history': "Annesi anlatıyor: 'On gün önce ateşli, kusmalı bir ishal geçirdi; ateşi ve kusması geçti. Ama ne zaman "
             'inek sütü veya yoğurt versem yarım saat sonra karnından gurultular geliyor, bezine fışkırır gibi '
             'köpüklü, sapsarı, ekşi kokulu sulu kaka yapıyor. Popo bölgesi kıpkırmızı oldu. Süt vermediğim günlerde '
             "kakası düzeliyor gibi.' İştahı iyi, oyun oynuyor. Kreşe gidiyor. Tartı: 10 kg (hastalık öncesi 10.2 kg).",
  'final_diagnosis': 'Sekonder (Postenfeksiyöz) Laktoz İntoleransı',
  'disposition': 'Yeşil Alandan 2-4 Hafta Laktozu Azaltılmış Beslenme, Bariyer Krem ve Kademeli Yeniden Başlama '
                 'Eğitimi ile Taburculuk',
  'case_pearl': 'Viral gastroenterit sonrası ince bağırsak fırça kenarı hasarı geçici laktaz eksikliğine yol açabilir. '
                'Süt ürünleriyle ilişkili köpüklü, asidik ishal, şişkinlik ve perianal eritem tipiktir; dışkı pH <5.5 '
                've redüktan madde pozitifliği tanıyı destekler. Tedavi geçici (2-4 hafta) laktozu azaltılmış '
                'beslenmedir; yoğurt ve peynir gibi fermente ürünler çoğunlukla tolere edilir. Kalıcı kısıtlama ve '
                'rutin laktozsuz mama önerilmez.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Geçirilmiş ishal sonrası belirli gıdalarla tetiklenen köpüklü dışkılaması olan bu bebekte '
                         'değerlendirmenin odağı nedir?',
             'options': [{'text': 'Dışkılamanın tetikleyici gıdalarla zamansal ilişkisini ayrıntılı sorgulayıp '
                                  'hidrasyon, büyüme, karın distansiyonu ve perianal cildi değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Postenfeksiyöz dönemde belirli gıdalarla tetiklenen ishalde gıda-semptom '
                                         'ilişkisi tanının anahtarıdır. Hidrasyon ve büyüme klinik ciddiyeti, perianal '
                                         'eritem dışkının asiditesini yansıtır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 104/dk, SS 22/dk, KDZ 1.5 sn. Hidrasyonu '
                                         'iyi, aktif. Tartı 10 kg (%2 kayıp). Karın hafif distandü, timpanik, yaygın '
                                         'gurultu; hassasiyet yok. Perianal bölgede parlak kırmızı, dışkı temas '
                                         'alanıyla sınırlı eritem; satellit lezyon yok. Annenin tuttuğu bezde köpüklü, '
                                         'sulu, sarı dışkı.'},
                         {'text': 'Uzayan ishal nedeniyle bakteriyel bir etken olabileceğini düşünüp hidrasyon '
                                  'değerlendirmesi sonrasında dışkı kültürü ve Clostridioides toksin testi istemek',
                          'is_correct': False,
                          'scenario_update': 'Kültür negatif geldi; toksin testi pozitif bildirildi ve iki yaş altı '
                                             'çocukta kolonizasyon olabileceği için yorumlanamadı. Aile kaygılandı.',
                          'teaching_point': 'Ateşsiz, iyi görünen ve belirli gıdalarla tetiklenen ishalde rutin '
                                            'bakteriyel tetkik yönetimi değiştirmez.'},
                         {'text': 'Perianal kızarıklığı kandida dermatiti kabul edip antifungal krem önermek, ishal '
                                  'için mevcut beslenmeyi sürdürüp bir hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Antifungal kreme rağmen kızarıklık sürdü; dışkının niteliği değişmediği '
                                             'için cilt iyileşmedi.',
                          'teaching_point': 'Satellit lezyonu olmayan, dışkı temas alanıyla sınırlı eritem asidik '
                                            'dışkıya bağlı irritan dermatittir; altta yatan nedene yönelinmelidir.'},
                         {'text': 'Köpüklü ve yağlı görünümlü dışkı nedeniyle pankreas yetersizliğini düşünüp solunum '
                                  'öyküsünü sorgulamak ve ter testi için yönlendirme planlamak',
                          'is_correct': False,
                          'scenario_update': 'Solunum öyküsü yoktu; ter testi randevusu verildi ve gıda-semptom '
                                             'ilişkisi ayrıntılı sorgulanmadı.',
                          'teaching_point': 'Akut enfeksiyon sonrası başlayan ve belirli gıdalarla tetiklenen ishal '
                                            'kronik malabsorpsiyon hastalıklarından önce geçici enzim eksikliklerini '
                                            'düşündürür.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Hidrasyonu iyi, perianal asidik eritemi ve köpüklü dışkısı olan bu bebekte hangi basit '
                         'tetkik tanıyı destekler?',
             'options': [{'text': 'Taze dışkı örneğinde pH ölçümü ve redüktan madde testi yapmak, mikroskopide lökosit '
                                  've parazit bakmak; kan tetkiki istememek',
                          'is_correct': True,
                          'explanation': 'Fermente edilmemiş karbonhidratların kolonda bakteriyel fermantasyonu asidik '
                                         '(pH <5.5) ve redüktan madde içeren dışkıya yol açar. Bu basit tetkikler kan '
                                         'tetkikine gerek kalmadan tanıyı destekler.',
                          'new_finding': 'Taze dışkı: pH 5.0, redüktan madde ++ pozitif. Mikroskopide lökosit, '
                                         'eritrosit, parazit ve kist yok.'},
                         {'text': 'Tanıyı kesinleştirmek için acil serviste 2 g/kg oral yükleme verip iki saat sonra '
                                  'kan şekeri artışını ve gelişen semptomları gözlemek',
                          'is_correct': False,
                          'scenario_update': 'Yükleme sonrası bebekte şiddetli gaz sancısı ve dört kez patlayıcı ishal '
                                             'gelişti; kan şekeri ölçümü güvenilir sonuç vermedi.',
                          'teaching_point': 'Provokatif yükleme testleri akut dönemdeki küçük çocukta rahatsızlık '
                                            'verir ve gereksizdir.'},
                         {'text': 'Hidrojen nefes testi ile karbonhidrat emilimini değerlendirmek amacıyla çocuk '
                                  'gastroenteroloji polikliniğine randevu verip testi yapılana kadar mevcut beslenmeyi '
                                  'sürdürmek',
                          'is_correct': False,
                          'scenario_update': 'Randevu üç hafta sonraya verildi; bu sürede ishal ve pişik sürdü.',
                          'teaching_point': 'Hidrojen nefes testi küçük çocukta uygulaması güç ve bu klinik tabloda '
                                            'gereksizdir; basit dışkı testleri yeterlidir.'},
                         {'text': 'Malabsorpsiyonu değerlendirmek için doku transglutaminaz IgA, total IgA, albümin, '
                                  'demir ve çinko düzeylerini isteyip sonuçlara göre diyet planlamak',
                          'is_correct': False,
                          'scenario_update': 'Sonuçlar normal geldi; bebek kan alımı sırasında çok ağladı ve diyet '
                                             'önerisi ertelendi.',
                          'teaching_point': 'Yeni başlayan, enfeksiyon sonrası, büyümeyi etkilememiş ishalde kronik '
                                            'malabsorpsiyon taraması gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Viral ishal sonrası süt ürünleriyle tetiklenen köpüklü ishal, asidik dışkı ve redüktan madde '
                         'pozitifliği olan bu bebekte tanı nedir?',
             'options': [{'text': 'Giardia duodenalis enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Mikroskopide trofozoit veya kist görülmedi ve ishal süt alımıyla '
                                             'tetikleniyor.',
                          'teaching_point': 'Protozoon enfeksiyonu belirli gıdayla tetiklenmeyen uzamış ishal yapar.'},
                         {'text': 'İnek sütü proteini alerjisi',
                          'is_correct': False,
                          'scenario_update': 'Yakınma enfeksiyon sonrası başlamış; kanlı dışkı, ürtiker veya egzama '
                                             'yok ve dışkı bulguları karbonhidrat malabsorpsiyonunu gösteriyor.',
                          'teaching_point': 'Asidik dışkı ve redüktan madde pozitifliği protein alerjisinden çok '
                                            'karbonhidrat malabsorpsiyonunu düşündürür.'},
                         {'text': 'Konjenital sukraz-izomaltaz eksikliği',
                          'is_correct': False,
                          'scenario_update': 'Konjenital eksiklikte şikayet sükroz içeren gıdalara geçişle başlar; '
                                             'burada belirleyici olan enfeksiyon sonrası süt ürünleri.',
                          'teaching_point': 'Konjenital disakkaridaz eksiklikleri enfeksiyon öyküsünden bağımsız ve '
                                            'kalıcıdır.'},
                         {'text': 'Sekonder (postenfeksiyöz) laktoz intoleransı',
                          'is_correct': True,
                          'explanation': 'Viral enterit sonrası fırça kenarı hasarına bağlı geçici laktaz eksikliği '
                                         'süt alımıyla ozmotik-fermentatif ishale neden olur; asidik dışkı ve redüktan '
                                         'madde pozitifliği tanıyı destekler.',
                          'new_finding': 'Tanı: Postenfeksiyöz (Sekonder) Laktoz İntoleransı.'}]},
            {'stage_title': 'Diyet Yönetimi ve İyileşme Planı',
             'question': 'Bu bebeğin beslenme planı nasıl düzenlenmelidir?',
             'options': [{'text': 'İnek sütü ve süt ürünlerini kalıcı olarak kesip soya bazlı mamaya geçmek, kalsiyum '
                                  'desteği başlamak ve okul çağında yeniden değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Kalıcı kısıtlama gereksiz yere uygulandı; aile yıllarca süt ürünlerinden '
                                             'kaçındı.',
                          'teaching_point': 'Sekonder laktoz intoleransı geçicidir; kalıcı kısıtlama ve soya mamaya '
                                            'geçiş gereksizdir.'},
                         {'text': 'İki-dört hafta laktozu azaltılmış süt kullanmak, yoğurt ve peynire devam etmek, '
                                  'bariyer krem önermek ve ardından sütü kademeli olarak yeniden başlatmak',
                          'is_correct': True,
                          'explanation': 'Fırça kenarının yenilenmesi için 2-4 haftalık laktoz azaltımı yeterlidir. '
                                         'Fermente ürünler daha az laktoz içerdiği için genellikle tolere edilir. '
                                         'Sonrasında süt ürünleri kademeli açılır; perianal bölge bariyer kremle '
                                         'korunur.',
                          'new_finding': 'Laktozu azaltılmış süte geçildi, çinko oksitli bariyer krem başlandı. 48 '
                                         'saatte patlayıcı ishal durdu, pişik geriledi. Üç hafta sonra normal süt '
                                         'sorunsuz yeniden başlandı.'},
                         {'text': 'Bağırsak enzimlerinin hızla yenilenmesi için iki hafta probiyotik ve çinko vermek, '
                                  'süt ürünlerine aynı miktarda devam edip şikayetleri izlemek',
                          'is_correct': False,
                          'scenario_update': 'Süt ürünlerine devam edilince ishal ve pişik sürdü; bebeğin tartısı 200 '
                                             'g daha azaldı.',
                          'teaching_point': 'Takviyeler tek başına yeterli değildir; semptomların kontrolü için geçici '
                                            'laktoz azaltımı gerekir.'},
                         {'text': 'İshali durdurmak için 24 saat yalnızca ORS ile beslemek, ardından pirinç lapası ve '
                                  'muzla sınırlı bir diyetle bir hafta devam etmek',
                          'is_correct': False,
                          'scenario_update': 'Kısıtlı diyetle bebek huzursuzlaştı ve kilo kaybı derinleşti; süt '
                                             'yeniden başlanınca ishal tekrarladı.',
                          'teaching_point': 'Aç bırakma ve kısıtlı diyetler önerilmez; hedef yalnızca laktoz yükünü '
                                            'geçici olarak azaltmaktır.'}]}]},
 {'id': 'G58',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '7 Yaşında',
  'gender': 'Kız',
  'complaint': 'Araba yolculuğu sırasında başlayan bulantı, kusma, solukluk ve soğuk terleme',
  'history': "Ailesi anlatıyor: 'Ailecek bayram için şehir dışına arabayla gidiyorduk. Yolun ilk saatinde arka "
             'koltukta tablette çizgi film izlerken esnemeye başladı, rengi soldu, soğuk soğuk terledi ve ardından '
             'kustu. Arabayı kenara çekip açık havaya çıkınca 15-20 dakikada toparlandı. Tekrar yola çıkıp virajlara '
             'girince yine kustu. Evde hiç şikayeti yok. Baş ağrısı, sabah kusması veya dengesizliği olmadı. Daha önce '
             "otobüs yolculuklarında da midesi bulanmıştı. Beyninde bir şey mi var diye çok korktuk.'",
  'final_diagnosis': 'Hareket Hastalığı (Taşıt Tutması)',
  'disposition': 'Yeşil Alandan Nörolojik Muayenenin Doğrulanması, Davranışsal Önlemler ve Gerekirse Yolculuk Öncesi '
                 'Profilaksi Eğitimi ile Taburculuk',
  'case_pearl': 'Taşıt hareketiyle başlayıp hareket bitince geçen bulantı, solukluk, terleme ve kusma; vestibüler, '
                'görsel ve proprioseptif girdiler arasındaki uyumsuzluktan kaynaklanır. Normal nörolojik muayenede '
                'görüntüleme gerekmez. Kırmızı bayraklar: sabah kusmaları, uykudan uyandıran baş ağrısı, ataksi, '
                'nistagmus, papilödem. Tedavide ön koltukta ufka bakmak, ekran-okuma yasağı, havalandırma ve hafif '
                'öğün; gerekirse 2 yaş üstünde yolculuktan 30-60 dakika önce birinci kuşak antihistaminik.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Yolculuk sırasında tekrarlayan kusması olan, ailesi beyinle ilgili bir hastalıktan endişe '
                         'eden bu çocukta muayenede neye odaklanırsınız?',
             'options': [{'text': 'Kusma ve solukluk nedeniyle hipoglisemiyi düşünüp kapiller kan şekeri bakmak, '
                                  'normalse ek muayene yapmadan oral sıvı denemesiyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Kan şekeri normal geldi. Nörolojik muayene yapılmadığı için ailenin '
                                             'endişesi giderilemedi ve aile başka bir merkezde tomografi istedi.',
                          'teaching_point': 'Ailenin intrakraniyal hastalık kaygısı ancak sistematik nörolojik '
                                            'muayeneyle giderilebilir.'},
                         {'text': 'Kusmaların gastrointestinal kaynaklı olabileceğini düşünüp karın muayenesine '
                                  'odaklanmak, ardından ondansetron vererek ailenin yolculuğa devam etmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Karın muayenesi normaldi; nörolojik muayene yapılmadan çocuk taburcu '
                                             'edildi ve aile endişesini sürdürdü.',
                          'teaching_point': 'Tekrarlayan kusmada nörolojik kırmızı bayraklar mutlaka '
                                            'değerlendirilmelidir.'},
                         {'text': 'Viraj sırasında kusma olduğu için vestibüler nörit olasılığını değerlendirmek '
                                  'amacıyla Dix-Hallpike manevrası yapıp kulak burun boğaz konsültasyonu istemek',
                          'is_correct': False,
                          'scenario_update': 'Dix-Hallpike negatifti; çocuk manevra sırasında yeniden bulantı '
                                             'hissetti. KBB randevusu ertesi güne verildi.',
                          'teaching_point': 'Vestibüler nörit sürekli vertigo ve spontan nistagmusla seyreder; yalnız '
                                            'taşıt içinde ortaya çıkan semptomlar bu tabloya uymaz.'},
                         {'text': 'Baş ağrısı, sabah kusması ve dengesizlik gibi kırmızı bayrakları sorgulayıp '
                                  'fundoskopi, nistagmus, serebellar testler, Romberg ve tandem yürüyüşü içeren '
                                  'nörolojik muayene yapmak',
                          'is_correct': True,
                          'explanation': 'Kusan çocukta intrakraniyal basınç artışı ve arka çukur patolojileri kırmızı '
                                         'bayraklar ve ayrıntılı nörolojik muayeneyle dışlanır. Normal muayene ve '
                                         'hareketle ilişkili örüntü aileye güvence vermek için temel dayanaktır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 86/dk, SS 18/dk, TA 102/64 mmHg. Genel '
                                         'durumu iyi, toparlanmış. Fundoskopide optik disk sınırları keskin. Kraniyal '
                                         'sinirler normal, nistagmus yok, parmak-burun ve topuk-diz testleri normal, '
                                         'Romberg negatif, tandem yürüyüş normal. Kulak zarları doğal. Karın rahat, '
                                         'hidrasyonu iyi.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Nörolojik muayenesi tamamen normal, şikayetleri yalnızca taşıt içinde olan bu çocukta tetkik '
                         'yaklaşımınız nedir?',
             'options': [{'text': 'Görüntüleme veya laboratuvar istemeden, şikayetlerin yalnızca taşıt hareketiyle '
                                  'başlayıp durduğunu ve kırmızı bayrak olmadığını aileyle birlikte netleştirmek',
                          'is_correct': True,
                          'explanation': 'Tanı öykü ve normal nörolojik muayeneye dayanır. Semptomların taşıt '
                                         'hareketiyle tetiklenip hareket bitince geçmesi tipik örüntüdür; tetkikler '
                                         'yönetimi değiştirmez ve kaygıyı artırabilir.',
                          'new_finding': 'Tetkik istenmedi. Ayrıntılı öyküde çocuğun salıncak ve lunaparktaki dönen '
                                         'oyuncaklarda da benzer bulantı yaşadığı, evde hiç şikayeti olmadığı '
                                         'öğrenildi.'},
                         {'text': 'Paroksismal vertigo atağı olabileceğini düşünüp elektroensefalografi ve odyometri '
                                  'planlamak, sonuçlar çıkana kadar uzun yolculuklardan kaçınmasını önermek',
                          'is_correct': False,
                          'scenario_update': 'Tetkik randevuları haftalar sonrasına verildi; aile bayram ziyaretini '
                                             'iptal etti.',
                          'teaching_point': 'Benign paroksismal vertigo taşıttan bağımsız, ani başlangıçlı kısa '
                                            'ataklarla seyreder; burada tetkik gerekmez.'},
                         {'text': 'Ailenin endişesini gidermek ve arka çukur kitlesini kesin olarak dışlamak için '
                                  'kontrastsız beyin tomografisi çekip sonucu aileyle paylaşmak',
                          'is_correct': False,
                          'scenario_update': 'Tomografi normal geldi; çocuk gereksiz radyasyona maruz kaldı ve aile '
                                             'bir sonraki yolculukta yeniden görüntüleme istedi.',
                          'teaching_point': 'Normal nörolojik muayenede görüntüleme endike değildir; güvence muayene '
                                            'bulgularıyla verilir.'},
                         {'text': 'Tekrarlayan kusma nedeniyle elektrolit, kan gazı ve tam idrar tetkiki isteyip '
                                  'metabolik bir neden dışlanana kadar oral alımı kısıtlamak',
                          'is_correct': False,
                          'scenario_update': 'Sonuçlar normal geldi; toparlanmış ve yemek isteyen çocuk iki saat aç '
                                             'bekletildi.',
                          'teaching_point': 'Hidrasyonu iyi ve semptomları geçmiş çocukta laboratuvar tetkikinin '
                                            'katkısı yoktur.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Yalnızca taşıt ve dönen oyuncaklarda başlayan, hareket bitince geçen bulantı-kusma, solukluk '
                         've terlemesi olan bu çocukta tanı nedir?',
             'options': [{'text': 'Döngüsel kusma sendromu',
                          'is_correct': False,
                          'scenario_update': 'Ataklar taşıt hareketiyle tetikleniyor ve dakikalar içinde geçiyor; '
                                             'saatler-günler süren stereotipik ataklar yok.',
                          'teaching_point': 'Döngüsel kusma tetikleyiciden bağımsız uzun ataklarla seyreder.'},
                         {'text': 'Çocukluk çağı benign paroksismal vertigosu',
                          'is_correct': False,
                          'scenario_update': 'Ataklar taşıt dışında spontan olmuyor ve kusma ön planda.',
                          'teaching_point': 'Benign paroksismal vertigo ani başlangıçlı, kısa süreli ve spontan '
                                            'dengesizlik ataklarıdır.'},
                         {'text': 'Arka çukur tümörü',
                          'is_correct': False,
                          'scenario_update': 'Sabah kusmaları, baş ağrısı, ataksi ve papilödem yok; nörolojik muayene '
                                             'normal.',
                          'teaching_point': 'Kafa içi basınç artışı taşıttan bağımsız, ilerleyici bulgularla '
                                            'seyreder.'},
                         {'text': 'Hareket hastalığı (taşıt tutması)',
                          'is_correct': True,
                          'explanation': 'Görsel, vestibüler ve proprioseptif girdiler arasındaki uyumsuzluk taşıt '
                                         'hareketi sırasında bulantı, solukluk, terleme ve kusmaya yol açar; hareket '
                                         'bitince semptomlar geriler.',
                          'new_finding': 'Tanı: Hareket Hastalığı (Taşıt Tutması).'}]},
            {'stage_title': 'Önlemler ve Yolculuk Planı',
             'question': 'Ailenin dönüş yolculuğu için en uygun öneri hangisidir?',
             'options': [{'text': 'Yolculuk öncesinde mideyi boşaltmak için çocuğu aç bırakmak, araba içinde kapalı '
                                  'camla klimayı açık tutmak ve uyuması için hafif sedatif şurup vermek',
                          'is_correct': False,
                          'scenario_update': 'Aç bırakılan çocukta bulantı daha erken başladı; sedatif şurup sonrası '
                                             'aşırı uyku hali gelişti.',
                          'teaching_point': 'Tamamen aç kalmak bulantıyı artırabilir; hafif öğün ve temiz hava '
                                            'önerilir, rutin sedatif kullanımı uygun değildir.'},
                         {'text': 'Yolculuk sırasında bulantı başlayınca ağızdan çözünen ondansetron vermek ve çocuğun '
                                  'dikkatini dağıtmak için tablette film izlemeye devam etmesine izin vermek',
                          'is_correct': False,
                          'scenario_update': 'Ekran izlemeye devam eden çocuk yine kustu; ondansetron hareketle '
                                             'ilişkili bulantıda sınırlı etki gösterdi.',
                          'teaching_point': 'Ekrana bakmak görsel-vestibüler uyumsuzluğu artırır; ondansetronun bu '
                                            'durumda etkinliği düşüktür.'},
                         {'text': 'Tekrarlayan kusma nedeniyle yolculuk öncesi intramüsküler metoklopramid uygulamak, '
                                  'çocuğu arka koltukta yatırıp gözlerini kapatarak uyumasını sağlamak',
                          'is_correct': False,
                          'scenario_update': 'Metoklopramid sonrası çocukta huzursuzluk ve istemsiz kasılmalar '
                                             'gelişti; yolculuk ertelendi.',
                          'teaching_point': 'Metoklopramid çocuklarda ekstrapiramidal yan etki riski nedeniyle bu '
                                            'amaçla önerilmez.'},
                         {'text': 'Ekran ve kitaptan kaçınmasını, mümkünse ön koltukta ufka bakmasını, havalandırmayı '
                                  've hafif öğünü önermek; gerekirse yolculuktan 30-60 dakika önce antihistaminik '
                                  'kullanmak',
                          'is_correct': True,
                          'explanation': 'Davranışsal önlemler duyusal uyumsuzluğu azaltır. Gerekirse 2 yaş üstünde '
                                         'yolculuk öncesi birinci kuşak antihistaminik (örn. dimenhidrinat) '
                                         'profilaktik kullanılabilir; sedasyon yan etkisi anlatılır.',
                          'new_finding': 'Dönüş yolculuğunda çocuk ön koltukta, camı aralık, müzik dinleyerek ve ufka '
                                         'bakarak seyahat etti; ilaca gerek kalmadan kusmadan yolculuğu '
                                         'tamamladı.'}]}]},
 {'id': 'G59',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '6 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Özellikle geceleri artan makat kaşıntısı ve huzursuz uyku',
  'history': "Annesi anlatıyor: 'Üç haftadır geceleri uyuduktan bir-iki saat sonra poposunu kaşıyarak ağlayarak "
             'uyanıyor. Gündüz kaşıntısı çok daha az. Dün gece fenerle baktığımda makatının etrafında yarım santim '
             'boyunda, beyaz, ince iplik gibi kıpırdayan bir şey gördüm. İştahı biraz azaldı. Dört yaşındaki kızımda '
             "da benzer kaşıntı başladı.' Çocuk kreşe ve futbol kursuna gidiyor. Kilo kaybı, ishal veya kanlı dışkı "
             'yok. Tartı: 21 kg.',
  'final_diagnosis': 'Enterobiyazis (Kıl Kurdu Enfeksiyonu)',
  'disposition': 'Yeşil Alandan Tek Doz Antihelmintik, İki Hafta Sonra Tekrar Doz, Tüm Hane Halkının Eş Zamanlı '
                 'Tedavisi ve Hijyen Eğitimi ile Taburculuk',
  'case_pearl': 'Gece artan perianal kaşıntı, ailede benzer yakınma ve perianal bölgede görülen ince beyaz kurtlar '
                'enterobiyazisi düşündürür. Dişi kurtlar geceleri perianal deriye yumurta bırakır; dışkı mikroskopisi '
                'duyarsızdır, tanı sabah tuvalet ve banyo öncesi şeffaf yapışkan bant yöntemiyle konur. Tedavide '
                'mebendazol 100 mg veya pirantel pamoat 11 mg/kg tek doz verilir ve 2 hafta sonra tekrarlanır; tüm '
                'hane halkı eş zamanlı tedavi edilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Gece artan makat kaşıntısı ve kardeşinde benzer yakınması olan bu çocukta muayenede neye '
                         'dikkat edersiniz?',
             'options': [{'text': 'Perianal bölgeyi ekskoriasyon, sekonder enfeksiyon, fissür ve streptokokal dermatit '
                                  'açısından incelemek, kız kardeşte vulvovajinit sorgulamak ve büyüme durumunu '
                                  'değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Perianal kaşıntıda muayene kaşıntının komplikasyonlarını (ekskoriasyon, '
                                         'sekonder bakteriyel enfeksiyon) ve ayırıcı tanıları (fissür, perianal '
                                         'streptokokal dermatit) ortaya koyar. Kız çocuklarında kurtlar vulvovajinite '
                                         'yol açabilir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 88/dk, TA 98/62 mmHg. Genel durumu iyi, '
                                         'büyümesi normal. Karın rahat. Perianal bölgede kaşımaya bağlı lineer '
                                         'ekskoriasyonlar ve hafif eritem; keskin sınırlı parlak kırmızı eritem, '
                                         'fissür veya akıntı yok. Muayene sırasında görülebilen hareketli yapı '
                                         'izlenmedi.'},
                         {'text': 'Ailenin gördüğü yapıyı doğrulamak için muayenede rektal tuşe yapıp parmakta dışkı '
                                  'örneği almak ve mikroskopiye göndermek',
                          'is_correct': False,
                          'scenario_update': 'Rektal tuşe çocuk için travmatik oldu; dışkı örneğinde yumurta '
                                             'görülmedi.',
                          'teaching_point': 'Bu tabloda rektal tuşenin tanısal değeri yoktur; yumurtalar dışkıda değil '
                                            'perianal deride bulunur.'},
                         {'text': 'Huzursuz uyku ve iştahsızlık nedeniyle demir eksikliği ve davranış sorunlarını '
                                  'öncelikli değerlendirip uyku hijyeni önermek ve hemogram istemek',
                          'is_correct': False,
                          'scenario_update': 'Hemogram normal geldi; perianal bölge muayene edilmediği için kaşıntının '
                                             'nedeni belirlenmedi.',
                          'teaching_point': 'Huzursuz uyku burada kaşıntının sonucudur; öncelik perianal '
                                            'değerlendirmedir.'},
                         {'text': 'Perianal kaşıntıyı mantar enfeksiyonu kabul edip bölgeyi yüzeysel incelemek, '
                                  'topikal antifungal krem başlamak ve iki hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Antifungal kreme rağmen gece kaşıntıları sürdü; kız kardeşteki '
                                             'şikayetler de arttı.',
                          'teaching_point': 'Gece artan kaşıntı ve ailede benzer yakınma paraziter etiyolojiyi '
                                            'düşündürür; ampirik antifungal tedavi tanıyı geciktirir.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Tanıyı doğrulamak için en uygun tetkik yöntemi hangisidir?',
             'options': [{'text': 'Sabah uyanınca tuvalet ve banyodan önce perianal bölgeye şeffaf yapışkan bant '
                                  'bastırıp lam üzerine yapıştırmak ve mikroskopta incelemek',
                          'is_correct': True,
                          'explanation': 'Dişi kurtlar geceleri perianal deriye yumurta bırakır; sabah yıkanmadan önce '
                                         'şeffaf bantla alınan örnek en duyarlı yöntemdir. Üç ardışık sabah yapılırsa '
                                         "duyarlılık %90'ı aşar.",
                          'new_finding': 'Ertesi sabah aile tarafından alınan bant örneğinin mikroskopisinde bir yüzü '
                                         'düz, diğer yüzü bombeli, asimetrik, oval, ince kabuklu çok sayıda yumurta '
                                         'görüldü.'},
                         {'text': 'Üç ayrı günde dışkı örneği alarak parazit yumurtası ve kist açısından mikroskopik '
                                  'inceleme yapmak, sonuçlar çıkana kadar tedaviyi ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Üç dışkı örneği de negatif geldi; aile enfeksiyon olmadığını düşünerek '
                                             'önlem almayı bıraktı.',
                          'teaching_point': 'Bu parazitin yumurtaları dışkıya nadiren geçer; dışkı mikroskopisinin '
                                            'duyarlılığı çok düşüktür.'},
                         {'text': 'Perianal bölgeden steril eküvyonla sürüntü alıp bakteriyel ve fungal kültür '
                                  'göndermek, kültür sonucuna göre tedaviyi düzenlemek',
                          'is_correct': False,
                          'scenario_update': 'Kültürde cilt florası üredi; sonuç yönetimi değiştirmedi ve tanı '
                                             'gecikti.',
                          'teaching_point': 'Kültür paraziter tanıda yararsızdır; yumurtaları göstermek için bant '
                                            'yöntemi kullanılır.'},
                         {'text': 'Eozinofil sayısı ve total IgE düzeyi için kan alıp eozinofili saptanırsa paraziter '
                                  'enfeksiyon kabul ederek ampirik tedavi başlamak',
                          'is_correct': False,
                          'scenario_update': 'Eozinofil sayısı normal geldi; aile tedaviye gerek olmadığı sonucuna '
                                             'vardı.',
                          'teaching_point': 'Bu enfeksiyon dokuya invaze olmadığından eozinofili genellikle yoktur; '
                                            'kan tetkikleri tanısal değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Gece artan perianal kaşıntı, ailede benzer şikayet ve bant örneğinde asimetrik oval '
                         'yumurtalar görülen bu çocukta tanı nedir?',
             'options': [{'text': 'Perianal streptokokal dermatit',
                          'is_correct': False,
                          'scenario_update': 'Keskin sınırlı parlak eritem, ağrılı dışkılama veya kanlı dışkı yok; '
                                             'bant örneğinde yumurtalar görüldü.',
                          'teaching_point': 'Perianal streptokokal dermatitte hızlı antijen testi pozitiftir ve '
                                            'parazit yumurtası görülmez.'},
                         {'text': 'Ascaris lumbricoides enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Askaris yumurtaları dışkıda görülür ve perianal kaşıntı tipik değildir.',
                          'teaching_point': 'Askariyazis çoğunlukla asemptomatik veya karın ağrısı, obstrüksiyon ve '
                                            'akciğer bulgularıyla seyreder.'},
                         {'text': 'Enterobiyazis (kıl kurdu)',
                          'is_correct': True,
                          'explanation': 'Gece perianal kaşıntı, ailede bulaş ve bant örneğinde bir yüzü düz, diğer '
                                         'yüzü bombeli yumurtalar Enterobius vermicularis enfeksiyonunu doğrular.',
                          'new_finding': 'Tanı: Enterobiyazis (Enterobius vermicularis).'},
                         {'text': 'Atopik dermatit alevlenmesi',
                          'is_correct': False,
                          'scenario_update': 'Başka bölgelerde egzama yok, kaşıntı perianal bölgeye sınırlı ve ailede '
                                             'bulaş var.',
                          'teaching_point': 'Ailede eş zamanlı benzer kaşıntı bulaşıcı bir etkeni düşündürür.'}]},
            {'stage_title': 'Tedavi ve Aile Planı',
             'question': 'Bu çocuk ve ailesi için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Yalnızca semptomlu çocuk ve kız kardeşine tek doz mebendazol vermek, diğer aile '
                                  'bireylerini şikayet başlarsa tedavi etmek',
                          'is_correct': False,
                          'scenario_update': 'Asemptomatik ebeveynden yeniden bulaş oldu; altı hafta sonra her iki '
                                             'çocukta da kaşıntı tekrarladı.',
                          'teaching_point': 'Hane halkında asemptomatik taşıyıcılık sıktır; tüm aile eş zamanlı tedavi '
                                            'edilmelidir.'},
                         {'text': 'Tüm hane halkına aynı gün tek doz mebendazol 100 mg veya pirantel pamoat 11 mg/kg '
                                  'vermek, iki hafta sonra dozu tekrarlamak ve hijyen önlemlerini anlatmak',
                          'is_correct': True,
                          'explanation': 'Antihelmintikler erişkin kurtları öldürür ancak yumurtalara etkisizdir; iki '
                                         'hafta sonra yumurtadan çıkan yeni kurtlar için ikinci doz gerekir. Tırnak '
                                         'kesimi, sabah banyo, el yıkama ve çarşaf-pijamaların sıcak yıkanması yeniden '
                                         'bulaşı önler.',
                          'new_finding': 'Tüm aileye aynı gün tek doz mebendazol verildi, iki hafta sonra tekrarlandı. '
                                         'Çarşaf ve pijamalar sıcak suda yıkandı. Bir ay sonra iki çocuğun da '
                                         'kaşıntısı tamamen geçmişti.'},
                         {'text': 'Çocuğa tek doz albendazol 400 mg verip kontrol bant testi negatif olana kadar '
                                  'haftalık örnek almak ve kardeşini ayrı odada yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Tek doz sonrası iki hafta içinde yeni kurtlar çıktı ve kaşıntı '
                                             'tekrarladı; aile içi bulaş sürdü.',
                          'teaching_point': 'Tek doz yetersizdir; iki hafta sonra tekrar doz ve tüm hanenin tedavisi '
                                            'esastır.'},
                         {'text': 'Çocuğa yedi gün boyunca günde iki kez mebendazol vermek, kreşe tedavi bitene kadar '
                                  'göndermemek ve evcil hayvanı veterinere götürmek',
                          'is_correct': False,
                          'scenario_update': 'Uzun süreli tedavi gereksizdi; çocuk kreşten uzak kaldı ve evcil hayvan '
                                             'gereksiz yere tedavi edildi.',
                          'teaching_point': 'Bu parazit yalnızca insanda yaşar; evcil hayvanlar kaynak değildir. Kreşe '
                                            'ara vermek gerekmez.'}]}]},
 {'id': 'G60',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '6 Yaşında',
  'gender': 'Kız',
  'complaint': 'Ani başlayan yüksek ateş, yutma güçlüğü, göbek çevresinde karın ağrısı ve kusma',
  'history': "Ailesi anlatıyor: 'Dün aniden 39.2°C ateş başladı, yutkunurken ağladı. Bu sabah iki kez kustu ve "
             'göbeğinin etrafında kramp tarzında ağrısı oldu. Öksürüğü, burun akıntısı veya hapşırması yok. Boynunun '
             "yanında dokununca acıyan şişlikler fark ettik. Karnı ağrıdığı ve kustuğu için apandisitten korktuk.' "
             'Sınıfında son haftalarda benzer hastalık geçiren çocuklar var. Penisilin alerjisi yok. Tartı: 22 kg.',
  'final_diagnosis': 'Akut Streptokokal Tonsillofarenjit (Karın Ağrısı ile Seyreden)',
  'disposition': 'Yeşil Alandan Hızlı Antijen Testi ile Doğrulama, Oral Amoksisilin ve Okula Dönüş Eğitimi ile '
                 'Taburculuk',
  'case_pearl': 'Okul çağında ani ateş, boğaz ağrısı, tonsiller eksüda, hassas ön servikal lenfadenopati ve '
                'öksürük-burun akıntısı yokluğu A grubu streptokok enfeksiyonunu düşündürür; bu çocuklarda karın '
                'ağrısı ve kusma sıktır ve akut batını taklit edebilir. Tanı hızlı antijen testi veya kültürle konur. '
                'Tedavide amoksisilin 50 mg/kg/gün (tek veya iki dozda, maks 1 g/gün) 10 gün ya da tek doz benzatin '
                'penisilin G kullanılır; antibiyotiğin 12-24. saatinden sonra okula dönülebilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Ani ateş, yutma güçlüğü, karın ağrısı ve kusması olan bu 6 yaşındaki kızda muayeneniz nasıl '
                         'olmalıdır?',
             'options': [{'text': 'Orofarenkste eksüda ve peteşi, ön servikal lenf nodlarını ve öksürük-burun akıntısı '
                                  'varlığını değerlendirmek; karında peritoneal bulgu aramak ve hidrasyonu kontrol '
                                  'etmek',
                          'is_correct': True,
                          'explanation': 'Ateşli karın ağrısında sistematik muayene karın dışı odakları ortaya koyar. '
                                         'Tonsiller eksüda, palatal peteşi, hassas ön servikal lenfadenopati ve viral '
                                         'bulguların yokluğu bakteriyel farenjiti düşündürür; peritoneal bulguların '
                                         'yokluğu cerrahi olasılığı azaltır.',
                          'new_finding': 'Vital Bulgular: Ateş 39.2°C, KTA 128/dk, SS 22/dk, SpO2 %99, KDZ 2 sn. '
                                         'Konjonktivit, burun akıntısı ve öksürük yok. Tonsiller hipertrofik, '
                                         'hiperemik, üzerinde beyaz-krem eksüda; yumuşak damakta peteşiler, uvula '
                                         'ödemli. Bilateral ön servikal zincirde 2x1.5 cm hassas lenf nodları. Karın '
                                         'yumuşak, periumbilikal hafif hassasiyet; defans ve rebound yok, '
                                         'zıplayabiliyor. Döküntü yok.'},
                         {'text': 'Ateş ve kusma nedeniyle muayene öncesinde intravenöz parasetamol ve ondansetron '
                                  'yapıp ateş düştükten sonra sistemleri ayrıntılı değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Ateş düştü ve çocuk rahatladı; ilk muayene bulguları kaydedilmeden 45 '
                                             'dakika geçti.',
                          'teaching_point': 'Semptomatik tedavi öncesinde vital bulgular ve sistemik muayene kayıt '
                                            'altına alınmalıdır; oral alabilen çocukta intravenöz yol gerekmez.'},
                         {'text': 'Yutma güçlüğü nedeniyle hava yolu tehlikesini düşünerek orofarenksi dil basacağıyla '
                                  'muayene etmeden çocuğu oturur pozisyonda tutmak ve kulak burun boğaz uzmanını '
                                  'çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Çocukta salya akması, stridor ve tripod pozisyon yoktu; KBB uzmanı '
                                             'orofarenks muayenesinin güvenle yapılabileceğini belirtti, zaman '
                                             'kaybedildi.',
                          'teaching_point': 'Dil basacağı ile muayeneden kaçınma yalnızca salya akması, stridor ve '
                                            'toksik görünüm gibi epiglottit bulgularında gereklidir.'},
                         {'text': 'Karın ağrısı ve kusma nedeniyle önce sağ alt kadran, rebound ve zıplama testini '
                                  'değerlendirmek, orofarenks muayenesini batın ultrasonografisinden sonraya bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Karında peritoneal bulgu saptanmadı; ultrasonografi beklenirken '
                                             'orofarenks muayenesi yapılmadığından tablonun kaynağı bir saat belirsiz '
                                             'kaldı.',
                          'teaching_point': 'Ateşli karın ağrısı olan çocukta orofarenks ve servikal lenf nodu '
                                            'muayenesi atlanmamalıdır; karın dışı nedenler sık görülür.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Tonsiller eksüda, hassas ön servikal lenfadenopati ve öksürük yokluğu olan, karnı rahat bu '
                         'çocukta tetkik yaklaşımınız nedir?',
             'options': [{'text': 'Monomükleoz olasılığına karşı periferik yayma ve heterofil antikor testi isteyip '
                                  'sonuç çıkana kadar antibiyotik vermeden izlemek',
                          'is_correct': False,
                          'scenario_update': 'Periferik yaymada atipik lenfosit görülmedi, heterofil antikor '
                                             'negatifti; tanı bir gün gecikti.',
                          'teaching_point': 'Monomükleoz arka servikal lenfadenopati, hepatosplenomegali ve '
                                            'yorgunlukla seyreder; burada ilk tetkik boğaz sürüntüsüdür.'},
                         {'text': 'Klinik bulgular tipik olduğu için hiçbir tetkik istemeden ampirik antibiyotik '
                                  'başlamak ve kusma nedeniyle ilk dozu intramüsküler seftriakson olarak yapmak',
                          'is_correct': False,
                          'scenario_update': 'Seftriakson enjeksiyonu ağrılı oldu; mikrobiyolojik doğrulama '
                                             'yapılmadığı için tedavinin gerekliliği belirsiz kaldı.',
                          'teaching_point': 'Viral farenjitlerle örtüşme nedeniyle klinik skorlar tek başına '
                                            'antibiyotik kararı için yeterli değildir; geniş spektrumlu parenteral '
                                            'tedavi gereksizdir.'},
                         {'text': 'Boğaz sürüntüsünden hızlı antijen testi yapmak, negatif olursa kültür göndermek; '
                                  'karın bulguları rahat olduğu için batın görüntülemesi istememek',
                          'is_correct': True,
                          'explanation': 'Klinik bulgular tek başına bakteriyel ve viral farenjiti güvenle ayıramaz; '
                                         'tedavi kararı hızlı antijen testi veya kültürle verilir. Çocukta negatif '
                                         'hızlı test kültürle doğrulanmalıdır. Peritoneal bulgu olmadığından '
                                         'görüntüleme gerekmez.',
                          'new_finding': 'Boğaz sürüntüsü hızlı antijen testi: POZİTİF. Karında bulgu gerilemesi için '
                                         'görüntüleme istenmedi.'},
                         {'text': 'Akut batını dışlamak için tam kan sayımı, CRP ve batın ultrasonografisi istemek, '
                                  'sonuçlar normalse boğaz sürüntüsü almadan ampirik antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'Lökosit 15.200/mm³, CRP 38 mg/L geldi; ultrasonografide yalnızca reaktif '
                                             'mezenterik lenf nodları görüldü. Etiyoloji doğrulanmadan antibiyotik '
                                             'başlandı.',
                          'teaching_point': 'Lökosit ve CRP viral ve bakteriyel farenjiti ayırmaz; antibiyotik kararı '
                                            'mikrobiyolojik doğrulamaya dayanmalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Ani ateş, tonsiller eksüda, palatal peteşi, hassas ön servikal lenfadenopati, karın ağrısı '
                         've pozitif hızlı antijen testi olan bu çocukta tanı nedir?',
             'options': [{'text': 'Adenoviral faringokonjonktival ateş',
                          'is_correct': False,
                          'scenario_update': 'Konjonktivit, öksürük ve burun akıntısı yok.',
                          'teaching_point': 'Adenovirüs farenjiti konjonktivit ve diğer viral bulgularla birlikte '
                                            'görülür.'},
                         {'text': 'Akut apandisit',
                          'is_correct': False,
                          'scenario_update': 'Karında defans ve rebound yok, çocuk zıplayabiliyor ve tablo orofarenks '
                                             'bulgularıyla açıklanıyor.',
                          'teaching_point': 'Farenjite eşlik eden karın ağrısı mezenterik lenfoid yanıtla ilişkilidir; '
                                            'peritoneal bulgu yoksa cerrahi tablo düşünülmez.'},
                         {'text': 'Akut streptokokal tonsillofarenjit',
                          'is_correct': True,
                          'explanation': 'Pozitif hızlı antijen testi ile birlikte tipik klinik bulgular A grubu '
                                         'streptokok tonsillofarenjitini doğrular; karın ağrısı ve kusma bu '
                                         'enfeksiyonda sık görülür.',
                          'new_finding': 'Tanı: Akut A Grubu Streptokok Tonsillofarenjiti (karın ağrısı ve kusma '
                                         'ile).'},
                         {'text': 'Enfeksiyöz mononükleoz',
                          'is_correct': False,
                          'scenario_update': 'Arka servikal lenfadenopati ve splenomegali yok, hızlı antijen testi '
                                             'pozitif.',
                          'teaching_point': 'Mononükleozda eksüdatif farenjit olabilir ancak lenfadenopati yaygın ve '
                                            'organomegali eşlik eder.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': "Oral alabilen bu 22 kg'lık çocuk için en uygun tedavi planı hangisidir?",
             'options': [{'text': 'Oral amoksisilin-klavulanat 90 mg/kg/gün dozunu üç gün vermek, ateş düşünce kesmek '
                                  've bir hafta sonra kontrol boğaz kültürü almak',
                          'is_correct': False,
                          'scenario_update': 'Kısa süreli tedavi sonrası iki hafta içinde semptomlar tekrarladı; '
                                             'kontrol kültürü taşıyıcılığı gösterdi ve aile kafası karıştı.',
                          'teaching_point': 'Geniş spektrumlu ve kısa süreli tedavi önerilmez; 10 günlük süre '
                                            'eradikasyon ve romatizmal ateşin önlenmesi için gereklidir. Asemptomatik '
                                            'hastada kontrol kültürü yapılmaz.'},
                         {'text': 'Karın ağrısı ve kusma nedeniyle yatırıp intravenöz ampisilin başlamak, çocuk '
                                  'cerrahisi ile seri muayene planlamak ve kusma kesilince orale geçmek',
                          'is_correct': False,
                          'scenario_update': 'Oral alabilen ve karnı rahat çocuk gereksiz yere yatırıldı; ertesi gün '
                                             'cerrahi ekip izlem gerekmediğini belirtti.',
                          'teaching_point': 'Oral tolere eden, peritoneal bulgusu olmayan çocukta yatış ve parenteral '
                                            'tedavi gerekmez.'},
                         {'text': 'Oral azitromisin 12 mg/kg/gün dozunu beş gün vermek, kısa süreli tedavinin uyumu '
                                  'artıracağını anlatmak ve okula üç gün sonra dönmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Makrolid direnci nedeniyle 72. saatte ateş sürüyordu; tedavi '
                                             'amoksisiline değiştirildi.',
                          'teaching_point': 'Makrolidler yalnızca ciddi penisilin alerjisinde alternatiftir; direnç '
                                            'oranları yüksek olabilir.'},
                         {'text': 'Oral amoksisilin 50 mg/kg/gün dozunu iki dozda 10 gün vermek, ateş ve ağrı için '
                                  'parasetamol önermek, antibiyotiğin ilk gününden sonra okula dönüşe izin vermek',
                          'is_correct': True,
                          'explanation': 'A grubu streptokok tonsillofarenjitinde amoksisilin 50 mg/kg/gün (maks 1 '
                                         'g/gün) 10 gün etkin ve iyi tolere edilen ilk seçenektir. Tedavinin '
                                         'tamamlanması akut romatizmal ateşi önler; 12-24 saat antibiyotik sonrası '
                                         'bulaştırıcılık belirgin azalır.',
                          'new_finding': 'Oral amoksisilin ve parasetamol başlandı. 24 saat sonra ateşi düştü, '
                                         'yutkunması rahatladı; karın ağrısı ve kusması kayboldu. Aile 10 günlük '
                                         'tedaviyi tamamladı.'}]}]}]
