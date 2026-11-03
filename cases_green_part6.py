# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Yeşil Alan Vakaları (Part 6: G51 - G60)
Odak: Bulantı, Kusma, Karın Ağrısı, İshal (GİS Acilleri - Yeşil Alan Ayaktan Yönetim)
Kılavuzlar: ESPGHAN, AAP, NASPGHAN, NICE, Centor/McIsaac
"""

GREEN_CASES_PART6 = [ { 'age': '4 Yaşında',
    'case_pearl': 'Asetonemik kusma (açlık ketozu), 2-7 yaş arası çocuklarda glikojen depolarının sınırlı olması '
                  'nedeniyle ateş, enfeksiyon ve uzamış açlık sonrasında yağların hızla yakılmasıyla keton '
                  'cisimciklerinin (asetoasetat, beta-hidroksibütirat) birikmesi sonucu gelişir. Ketonlar beyindeki '
                  'kusma merkezini uyararak kısır bir döngü başlatır: Açlık -> Ketozis -> Kusma -> Daha çok açlık. En '
                  'kritik ayırıcı tanı DİYABETİK KETOASİDOZDUR (DKA)! Açlık ketozunda kan şekeri normal veya düşüktür '
                  '(60-95 mg/dL), venöz pH normaldir (>7.30). Tedavi bu kısır döngüyü kırmaktır: Damardan veya azar '
                  'azar ağızdan şekerli sıvılar (tatlı çay, meyve suyu, glukozlu ORS) verilerek insülin salgılanması '
                  'tetiklenir, lipoliz durur ve ketoz dakikalar içinde kırılır.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Ateşli hastalık sırasında bir gündür süren inatçı kusma, ağızda aseton kokusu ve halsizlik',
    'disposition': 'Yeşil Alanda Yatak Başı Glukoz/Keton Doğrulaması, Şekerli Sıvı ile Ketozun Kırılması ve Taburculuk',
    'final_diagnosis': 'Asetonemik Kusma / Açlık Ketozu (Ateş ve Açlığa Sekonder Benign Ketotik Kusma)',
    'gender': 'Erkek',
    'history': "Dört yaşındaki erkek çocuk annesi tarafından getiriliyor: 'İki gündür hafif ateşi ve boğaz ağrısı "
               'vardı, iştahı tamamen kesildi ve hiçbir şey yemedi. Dün akşamdan beri bir yudum su içse bile '
               'fışkırtarak kusuyor. Ağzından çürük elma veya aseton gibi bir koku geliyor. Çocuk halsiz, gözlerini '
               "açmakta zorlanıyor. İdrarını bugün sadece bir kez az miktarda yaptı. Diyabetimiz yok ama çok korktuk.'",
    'id': 'G51',
    'steps': [ { 'options': [ { 'explanation': "Kussmaul solunumu (derin hızlı solunum) ve letarji DKA'yı gösterir. "
                                               "DKA'yı ekarte etmek ve dehidratasyonu belirlemek ilk muayene "
                                               'hedefidir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.2°C, KTA 108/dk, SS 22/dk (solunum paterni '
                                               'doğal, takipne veya Kussmaul yok, ağızda hafif aseton kokusu), SpO2 '
                                               '%99, TA 96/60 mmHg, KDZ 2 sn. Çocuk halsiz ancak seslenince gözlerini '
                                               'açıyor, koopere. Ağız mukozası hafif kuru, ağlarken gözyaşı var. Batın '
                                               'rahat, defans ve rebound yok.',
                                'text': 'Bilinç durumunu, solunum derinliğini, periferik dolaşımı ve dehidratasyon '
                                        'bulgularını sistemik muayene ile değerlendirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Muayenesiz cerrahiye yönlendirilen hastada gereksiz laparotomi '
                                                   'hazırlığı başlatıldı.',
                                'teaching_point': 'Asetonemik kusmada batın rahattır; peritonit defansı bulunmaz, '
                                                  'cerrahi akut batın değildir.',
                                'text': 'Kusmayı apandisit perforasyonu kabul ederek fizik muayene yapmadan hastayı '
                                        'derhal acil ameliyathaneye almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Yağlı besin lipolizi ve keton üretimini artırarak çocuğun fışkırır '
                                                   'tarzda kusmasını tetikledi.',
                                'teaching_point': 'Açlık ketozunda yağlı besinler ketozu alevlendirir; basit '
                                                  'karbonhidratlı şekerli sıvılar verilmelidir.',
                                'text': 'Kusan çocuğa acil serviste zorla bir kase yağlı et çorbası içirerek kalori '
                                        'açığını kapatmaya çalışmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Sistemik ketozisi fark edilmeyen çocuk evde dehidratasyona ve '
                                                   'hipoglisemiye girdi.',
                                'teaching_point': 'Aseton kokusu ketonemi göstergesidir; metabolik durum mutlaka kan '
                                                  'şekeriyle taranmalıdır.',
                                'text': 'Ağızdaki aseton kokusunu diş çürüğü sanarak hiçbir muayene yapmadan hastayı '
                                        'diş hekimliğine sevk etmek'}],
                 'question': 'Açlık sonrası inatçı kusması ve ağzında aseton kokusu olan bu çocukta ilk muayene '
                             'yaklaşımı nasıl olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': "DKA'da kan şekeri >200-300 mg/dL iken açlık ketozunda kan şekeri "
                                               'normal veya hafif düşüktür (70-95 mg/dL). Her ikisinde de keton '
                                               'pozitiftir; glukoz düzeyi ayırıcı tanıyı anında koydurur.',
                                'is_correct': True,
                                'new_finding': 'Yatak Başı Glukometre: Kan Şekeri 76 mg/dL (normoglisemik, DKA '
                                               'dışlandı). İdrar Stix: Glukoz negatif, Keton (+++) pozitif. Venöz Kan '
                                               'Gazı: pH 7.34, HCO3 19 mmol/L, Baz Açığı -3 (asidoz yok).',
                                'text': 'Yatak başı kapiller kan şekeri ve idrar çubuğu ile keton bakarak metabolik '
                                        'durumu hızla doğrulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Kan şekeri 76 mg/dL olan çocuğa insülin yapılması derin '
                                                   'hipoglisemik komaya ve konvülziyona yol açtı.',
                                'teaching_point': 'Kan şekeri doğrulanmadan asla insülin verilemez; açlık ketozunda '
                                                  'insülin ölümcül hipoglisemi yapar.',
                                'text': 'Kan şekeri bakmadan hastaya acil koşullarda damardan yüksek doz intravenöz '
                                        'regüler insülin puşelemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Tomografi tamamen normal geldi; çocuk gereksiz yere yüksek doz '
                                                   'kraniyal radyasyon aldı.',
                                'teaching_point': 'Açlık ve enfeksiyon zeminindeki ketotik kusmada santral görüntüleme '
                                                  'endike değildir.',
                                'text': 'Kesin tanı koymak amacıyla hastaya genel anestezi altında acil kraniyal '
                                        'bilgisayarlı tomografi çektirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Aç bırakılan çocukta lipoliz daha da şiddetlendi ve derin '
                                                   'hipoglisemi gelişti.',
                                'teaching_point': 'Açlık ketozunun çözümü glukoz vermektir; aç bekletilmesi tabloyu '
                                                  'derinleştirir.',
                                'text': 'Tetkik istemeden hastayı 48 saat boyunca acil serviste tamamen aç ve susuz '
                                        'şekilde bekletmek'}],
                 'question': 'Asetonemik kusma ile DKA ayırıcı tanısını saniyeler içinde yapmak için en uygun tanısal '
                             'yaklaşım hangisidir?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Açlık sonrası inatçı kusma, normoglisemi (glukoz 76 mg/dL), ketonüri '
                                               've normal kan gazı açlık ketozu (asetonemik kusma) tanısıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Açlık ve Enfeksiyona Sekonder Benign Ketotik Kusma '
                                               '(Asetonemik Kusma).',
                                'text': 'Asetonemik kusma açlık ketozu'},
                              { 'is_correct': False,
                                'scenario_update': "DKA'da hiperglisemi (>250 mg/dL), glukozüri ve derin asidoz (pH "
                                                   "<7.20) olur; bu çocukta kan şekeri 76 mg/dL'dir.",
                                'teaching_point': "Açlık ketozunda kan şekeri normaldir; DKA'daki hiperglisemi ve "
                                                  'metabolik asidoz bulunmaz.',
                                'text': 'Ağır diyabetik ketoasidoz koması'},
                              { 'is_correct': False,
                                'scenario_update': 'Dizanteride yüksek ateş ve kanlı ishal olur; bu hastada ishal '
                                                   'yoktur, tablo ketotik kusmadır.',
                                'teaching_point': 'Dizanteri kolit tablosudur; izole açlık ketozu ve inatçı kusma '
                                                  'yapmaz.',
                                'text': 'Akut bakteriyel dizanteri enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': "KİBAS'ta sabah fışkırır kusmalar, baş ağrısı ve papilödem olur; "
                                                   'enfeksiyon sonrası akut açlık ketonürisi yapmaz.',
                                'teaching_point': 'Enfeksiyon ve açlıkla tetiklenen ketotik tablo intrakraniyal tümör '
                                                  'değildir.',
                                'text': 'Kafa içi kitle lezyonu'}],
                 'question': 'Uzamış açlık, normal kan şekeri, idrarda masif ketonüri ve hafif dehidratasyon ile kesin '
                             'tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Açlık ketozunun tedavisi glukoz vermektir. Verilen şeker insülin '
                                               'salgısını tetikler, yağ yıkımını durdurur ve ketonemi 1-2 saatte '
                                               'geriler. Tolere edemezse %5-10 Dekstrozlu IV hidrasyon verilir.',
                                'is_correct': True,
                                'new_finding': 'Çocuğa azar azar 100 mL tatlı elma suyu ve glukozlu ORS içirildi. '
                                               'Çocuk kusmadı. 1 saat sonra halsizliği geçti, idrarında keton tek '
                                               'pozitife geriledi ve şifayla taburcu edildi.',
                                'text': 'Küçük yudumlarla tatlı çay, elma suyu veya şekerli oral rehidratasyon sıvısı '
                                        'içirerek ketozu hızla kırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Şekersiz saf su verilmesi keton üretimini durduramadı ve çocuk '
                                                   'kusmaya devam etti.',
                                'teaching_point': 'Açlık ketozunda sadece su vermek yetmez; ketogenezi durdurmak için '
                                                  'mutlaka glukoz gereklidir.',
                                'text': 'Ketozu kırmak için hastaya bol miktarda saf su içirip şekerli besinleri '
                                        'kesinlikle yasaklamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Ağır sedatif ilaç çocukta derin hipotansiyon ve ekstrapiramidal '
                                                   'distoniye yol açtı.',
                                'teaching_point': 'Ketotik kusmada nöroleptik antiemetikler tehlikelidir; fizyolojik '
                                                  'tedavi karbonhidrattır.',
                                'text': 'Kusmayı durdurmak amacıyla 4 yaşındaki çocuğa intramüsküler yüksek doz '
                                        'klorpromazin enjeksiyonu yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Aşırı tuz verilmesi hipernatremiye ve şiddetli mide yanmasına '
                                                   'neden oldu.',
                                'teaching_point': 'Ketoziste tuzlu salamura değil, tatlı içeceklerle insülin uyarısı '
                                                  'yapılmalıdır.',
                                'text': 'Hastaya oral yoldan yoğun tuzlu salamura suyu içirerek mideyi temizlemeye '
                                        'çalışmak'}],
                 'question': 'Açlık ketozu saptanan bu çocuğun kısır döngüsünü kırmak için en uygun tedavi yaklaşımı '
                             'hangisidir?',
                 'stage_title': 'Tedavi Yönetimi ve Taburculuk Planı'}]},
  { 'age': '3 Yaşında',
    'case_pearl': 'Küçük çocuklarda akut idrar yolu enfeksiyonu (özellikle piyelonefrit) sıklıkla dizüri yerine karın '
                  'ağrısı, kusma, iştahsızlık ve açıklanamayan yüksek ateş ile prezante olur ve yanlışlıkla akut '
                  'apandisit veya gastroenterit sanılır! Muayenede suprapubik hassasiyet ve tek taraflı kostovertebral '
                  'açı (KVA) hassasiyeti saptanabilir. Tam idrar tahlilinde (TİT) lökosit esteraz ve nitrit '
                  'pozitifliği, mikroskopide bol lökosit ve bakteri görülmesi tanıyı koydurur; kesin tanı idrar '
                  'kültürüyle konur. Komplike olmayan, oral alabilen çocuklarda oral 3. kuşak sefalosporin (sefiksim 8 '
                  'mg/kg/gün tek doz, 10 gün) İV tedavi kadar etkilidir. Tedavi sonrası üriner USG planlanmalıdır.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Karın ağrısı, kusma, iştahsızlık ve 3 gündür düşmeyen yüksek ateş',
    'disposition': 'Yeşil Alandan İdrar Tahlili/Kültürü Doğrulaması, Oral Sefiksim Tedavisi ve Üriner USG Planıyla '
                   'Taburculuk',
    'final_diagnosis': 'Akut Piyelonefrit / İdrar Yolu Enfeksiyonuna İkincil Karın Ağrısı ve Kusma',
    'gender': 'Kız',
    'history': "Üç yaşındaki kız çocuk annesi tarafından getiriliyor: 'Üç gündür 39°C'ye varan ateşi var. Karnım "
               'ağrıyor diye ağlıyor, iki gündür günde 3-4 kez kusuyor. İshal veya öksürük yok. Annesi çişini yaparken '
               "ağladığını, son günlerde çok sık idrara gittiğini ve bezinin çok ağır koktuğunu söylüyor.'",
    'id': 'G52',
    'steps': [ { 'options': [ { 'explanation': 'Küçük çocuklarda İYE karın ağrısı ve kusmayla gelir. Suprapubik '
                                               'hassasiyet, KVA hassasiyeti ve apandisit dışlaması muayenenin '
                                               'odağıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 38.8°C, KTA 126/dk, SS 24/dk, SpO2 %99, TA 98/62 '
                                               'mmHg. Genel durumu orta, huzursuz. Akciğer ve KBB muayenesi doğal. '
                                               'Batında sağ alt kadranda hafif hassasiyet var ancak defans ve rebound '
                                               'yok; suprapubik alanda belirgin hassasiyet ve sağ kostovertebral açıda '
                                               'hassasiyet mevcut.',
                                'text': 'Karın hassasiyetini, suprapubik bölgeyi, böbrek lojlarını ve eksternal '
                                        'genital organları sistemik olarak muayene etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Muayenesiz cerrahiye alınan hastada gereksiz apendektomi yapıldı '
                                                   've ateş ameliyat sonrası devam etti.',
                                'teaching_point': 'Küçük kız çocuklarında ateş ve karın ağrısında idrar yolu '
                                                  'enfeksiyonu dışlanmadan cerrahiye gidilemez.',
                                'text': 'Karın ağrısını apandisit kabul edip idrar sorgulamadan çocuğu derhal acil '
                                        'ameliyathaneye cerrahiye göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Kas gevşetici verilmesi çocukta solunum zaafiyeti ve mesane '
                                                   'atonisine yol açtı.',
                                'teaching_point': 'Enfeksiyöz kusmada kas gevşetici ilaçların hiçbir yeri yoktur; odak '
                                                  'tespit edilmelidir.',
                                'text': 'Kusmayı durdurmak için hastaya fizik muayene yapmadan acil serviste yüksek '
                                        'doz kas gevşetici vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Soğuk su küveti çocukta titreme ve periferik vazokonstriksiyona '
                                                   'neden oldu.',
                                'teaching_point': 'Ateşli çocukta fiziksel soğuk küvet uygulaması travmatiktir; '
                                                  'enfeksiyon odağı araştırılmalıdır.',
                                'text': 'Hastada ateş olduğu için batına hiç dokunmadan çocuğu derhal soğuk su '
                                        'küvetine sokup bekletmek'}],
                 'question': 'Ateş, karın ağrısı ve kusması olan 3 yaşındaki kız çocukta ilk muayene yaklaşımınız ne '
                             'olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': "TİT'te lökositüri ve nitrit pozitifliği hızlı tanı sağlar. Antibiyotik "
                                               'öncesi steril idrar kültürü (orta akım veya kateterle) kesin tanı ve '
                                               'duyarlılık için altın standarttır.',
                                'is_correct': True,
                                'new_finding': 'Tam İdrar Tahlili: Dansite 1.018, Lökosit Esteraz (+++), Nitrit (+), '
                                               'Mikroskopi: Bol lökosit kümeleri, bol bakteri, eritrosit 3-4. İdrar '
                                               'kültürü gönderildi. Tam Kan: Lökosit 14.800/mm³ (%78 nötrofil), CRP 42 '
                                               'mg/L.',
                                'text': 'Steril şartlarda tam idrar tahlili ve eş zamanlı kantitatif idrar kültürü '
                                        'alarak piyüriyi incelemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Tomografi böbrekte hafif ödem gösterdi ancak basit idrar testi '
                                                   'yapılmadığı için kültür alınamadı.',
                                'teaching_point': 'İYE tanısı tomografiyle değil, idrar analizi ve kültürüyle konur; '
                                                  'BT aşırı radyasyondur.',
                                'text': 'İdrar tahlili yapmadan hastaya derhal yüksek doz radyasyonlu tüm batın '
                                        'bilgisayarlı tomografisi çektirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Boğaz ve gaita testleri negatif geldi; idrar yolu enfeksiyonunun '
                                                   'teşhisi 2 gün gecikti.',
                                'teaching_point': 'Dizüri ve kokulu idrar tariflenen çocukta idrar tahlili birincil '
                                                  'öncelikli testtir.',
                                'text': 'İdrar tahlili istemeden sadece boğaz kültürü ve dışkıda parazit testi '
                                        'göndererek sonucu beklemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Akut enfeksiyon sırasında yapılan travmatik sistoskopi bakteriyemi '
                                                   've ürosepsise yol açtı.',
                                'teaching_point': 'Akut İYE sırasında invaziv sistoskopi KONTRENDİKEDİR; enfeksiyonu '
                                                  'böbreğe yayabilir.',
                                'text': 'Kesin tanı için çocuğu ameliyathaneye alıp acil rijit sistoskopi ve üreteral '
                                        'kateterizasyon yapmak'}],
                 'question': 'Suprapubik ve böbrek loju hassasiyeti olan bu çocukta tanıyı doğrulamak için en kritik '
                             'tetkik hangisidir?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': "Yüksek ateş, kusma, karın ve KVA hassasiyeti ile TİT'te masif "
                                               'lökositüri/nitrit akut piyelonefriti kanıtlar.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Akut Piyelonefrit (Üst İdrar Yolu Enfeksiyonuna Sekonder '
                                               'Karın Ağrısı ve Kusma).',
                                'text': 'Akut piyelonefrit enfeksiyonu tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Apandisitte idrarda masif bakteri ve nitrit pozitifliği olmaz; '
                                                   'tablo primer üriner sistem enfeksiyonudur.',
                                'teaching_point': 'Apandisitte sekonder hafif lökositüri olabilir ancak nitrit ve '
                                                  "bakteri varlığı primer İYE'yi gösterir.",
                                'text': 'Akut cerrahi flegmonöz apandisit'},
                              { 'is_correct': False,
                                'scenario_update': 'Gastroenteritte ishal ön plandadır ve idrarda masif piyüri '
                                                   'görülmez; bu hastada ishal yoktur.',
                                'teaching_point': 'İshali olmayan kusan çocukta idrar tahlili yapılmadan gastroenterit '
                                                  'tanısı konulamaz.',
                                'text': 'Akut viral gastroenterit hastalığı'},
                              { 'is_correct': False,
                                'scenario_update': "Mezenterik lenfadenitte idrar tamamen temizdir; TİT'te nitrit ve "
                                                   'bol bakteri piyelonefrite özgüdür.',
                                'teaching_point': 'Mezenterik lenfadenit selim lenf nodu büyümesidir; idrar yolu '
                                                  'enfeksiyonu bulguları yapmaz.',
                                'text': 'Akut mezenterik adenit enfeksiyonu'}],
                 'question': 'Yüksek ateş, kusma, KVA hassasiyeti, piyüri ve nitrit pozitifliği ile en olası klinik '
                             'tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Genel durumu iyi, kusan ancak oral alabilen çocuklarda oral sefiksim '
                                               '(8 mg/kg/gün, 10 gün) parenteral tedavi kadar etkilidir. Ateş ve ağrı '
                                               'için parasetamol verilir. İlk febril İYE geçiren çocuklarda anatomik '
                                               'anomali taraması için USG planlanır.',
                                'is_correct': True,
                                'new_finding': 'Oral sefiksim süspansiyon başlandı. 48 saat sonra ateşi tamamen düştü, '
                                               'kusması kesildi. Kültürde 100.000 cfu/mL E. coli üredi (sefiksime '
                                               'duyarlı). Tedavi sonrası çekilen üriner USG doğal bulundu.',
                                'text': 'Oral üçüncü kuşak sefalosporin tedavisi başlamak, ateş düşürücü önermek ve '
                                        'tedavi bitiminde üriner ultrasonografi planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Piyelonefriti tedavi edilmeyen çocukta böbrek parankim absesi ve '
                                                   'renal skar gelişti.',
                                'teaching_point': 'Febril İYE / piyelonefrit mutlaka kanıta dayalı antibiyotikle '
                                                  'tedavi edilmelidir; bitkisel sular yetersizdir.',
                                'text': 'Antibiyotik vermeden hastaya sadece bol miktarda kızılcık suyu içirerek '
                                        'enfeksiyonu kurutmaya çalışmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz takılan kateter hastada sekonder hastane kökenli dirençli '
                                                   'süperenfeksiyon yarattı.',
                                'teaching_point': 'Normal idrar yapan çocukta foley sonda endikasyonu yoktur; kateter '
                                                  'enfeksiyon kaynağıdır.',
                                'text': 'İdrar yolu enfeksiyonunu önlemek amacıyla hastaya acil koşullarda kalıcı '
                                        'üretral foley sonda takıp taburcu etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Oral alabilen stabil hastanın haftalarca acilde tutulması gereksiz '
                                                   'hastane enfeksiyonu riski doğurdu.',
                                'teaching_point': 'Oral alabilen febril İYE olguları ayaktan güvenle tedavi '
                                                  'edilebilir; uzamış acil yatışı gerekmez.',
                                'text': 'Hastalık tamamen geçene kadar hastayı üç hafta boyunca acil serviste damardan '
                                        'çift antibiyotikle yatırmak'}],
                 'question': 'Oral alımı iyi, stabil akut piyelonefrit tanılı bu çocukta en uygun tedavi ve izlem '
                             'planı hangisidir?',
                 'stage_title': 'Tedavi Seçimi ve Taburculuk Stratejisi'}]},
  { 'age': '8 Yaşında',
    'case_pearl': 'Roma IV kriterlerine göre Fonksiyonel Karın Ağrısı: En az 2 aydır devam eden, ayda en az 4 kez '
                  'görülen, organik bir hastalıkla açıklanamayan göbek çevresi karın ağrısıdır. En kritik basamak '
                  'KIRMIZI BAYRAKLARIN (alarm bulguları) EKARTE EDİLMESİDİR: Kilo kaybı/büyüme geriliği, gece uykudan '
                  'uyandıran ağrı, gastrointestinal kanama, açıklanamayan ateş, inatçı kusma, artrit, perianal '
                  'hastalık ve ailede İBH öyküsü olmamalıdır. Kırmızı bayrak yoksa kapsamlı invaziv tetkik (endoskopi, '
                  "BT) zararlıdır. Tedavide temel kural: Ağrının 'gerçek' olduğunu (numara yapmadığını) kabul etmek, "
                  'organik hastalık olmadığını anlatmak ve EN ÖNEMLİSİ ÇOCUĞUN OKULA DÜZENLİ GİTMESİNİ SAĞLAMAKTIR '
                  '(okuldan alıkoymak anksiyeteyi ve ağrıyı pekiştirir).',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'İki aydır hafta içi sabahları okula gitmeden önce başlayan göbek çevresinde karın ağrısı',
    'disposition': 'Yeşil Alandan Organik Kırmızı Bayrakların Dışlanması, Aileye Güvence, Okul Devamlılığı ve '
                   'Psikososyal Rehberlik',
    'final_diagnosis': 'Fonksiyonel Karın Ağrısı (Roma IV / Okul Kaygısı İlişkili Karın Ağrısı)',
    'gender': 'Kız',
    'history': "Sekiz yaşındaki kız çocuğu ailesi tarafından getiriliyor: 'Yaklaşık iki aydır özellikle hafta içi "
               'sabahları okula gitmeden önce göbeğini tutup kıvranıyor, midem bulanıyor diyor. Okula gitmeyip evde '
               'kalınca veya hafta sonları tatilde ağrı tamamen kayboluyor. Gece ağrıyla hiç uyanmıyor. Kilo kaybı, '
               'ateş veya ishali yok. Büyümesi ve ders başarısı çok iyi ama annesi okulda zorbalık veya öğretmen '
               "kaygısı olabileceğinden şüpheleniyor.'",
    'id': 'G53',
    'steps': [ { 'options': [ { 'explanation': 'Büyüme eğrisinin korunmuş olması, gece ağrısının olmaması ve batın '
                                               'muayenesinin rahatlığı fonksiyonel kökeni organik patolojilerden '
                                               'ayıran temel adımdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 84/dk, SS 18/dk, SpO2 %99, TA 102/64 '
                                               'mmHg. Boy ve Tartı: 50. persentilde, büyüme eğrisi mükemmel. Genel '
                                               'durumu rahat, neşeli. Batın yumuşak, organomegali yok; periumbilikal '
                                               'alanda hafif non-spesifik hassasiyet tarifliyor ancak defans ve '
                                               'rebound yok.',
                                'text': 'Büyüme persentillerini incelemek, kırmızı bayrakları sorgulamak ve batın '
                                        'muayenesinde peritonit olmadığını doğrulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'İki aydır süren sabah ağrısına yapılan gereksiz cerrahi hazırlığı '
                                                   'çocukta travmaya yol açtı.',
                                'teaching_point': 'İki aydır sadece sabahları olan ağrı cerrahi akut batın değildir; '
                                                  'fizik muayene ile defans olmadığı görülür.',
                                'text': 'Karın ağrısını apandisit kabul edip fizik muayene yapmadan hastayı derhal '
                                        'acil ameliyathaneye almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Çocuğun anlaşılamadığı hissi kaygısını artırdı ve somatizasyon '
                                                   'ağrıları daha da şiddetlendi.',
                                'teaching_point': "Fonksiyonel ağrılar 'uydurma' değildir; beyin-bağırsak aksının "
                                                  'hiperaljezisidir, ciddiye alınmalıdır.',
                                'text': 'Ağrının numara olduğunu söyleyerek muayene etmeden çocuğu azarlayıp acil '
                                        'servisten göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Opioid verilmesi çocukta solunum depresyonu, bulantı ve bağırsak '
                                                   'kabızlığına yol açtı.',
                                'teaching_point': 'Fonksiyonel karın ağrısında opioidler KESİNLİKLE KONTRENDİKEDİR; '
                                                  'bağımlılık ve dismotilite yapar.',
                                'text': 'Ağrıyı kesmek amacıyla hastaya acil serviste intravenöz yüksek doz opioid '
                                        'infüzyonu uygulamak'}],
                 'question': 'Okul günleri sabahları karın ağrısı olan bu 8 yaşındaki çocukta ilk muayene yaklaşımı '
                             'nasıl olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'Roma IV kılavuzlarına göre kırmızı bayrağı olmayan (gece uyanma, kilo '
                                               'kaybı vb. yok) fonksiyonel ağrılarda kolonoskopi, tomografi veya geniş '
                                               'kan taramaları gereksizdir; hekim güvencesi tanı için yeterlidir.',
                                'is_correct': True,
                                'new_finding': 'Gereksiz invaziv girişim yapılmadı. Temel tarama amaçlı tam kan sayımı '
                                               've tam idrar tahlili tamamen normal geldi. İleri endoskopik tetkike '
                                               'gerek görülmedi.',
                                'text': 'Kırmızı bayrak bulunmayan bu hastada gereksiz invaziv ve radyolojik '
                                        'tetkiklerden kaçınarak klinik izlem planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Endoskopi tamamen normal geldi ancak çocuk gereksiz invaziv travma '
                                                   've anestezi riski yaşadı.',
                                'teaching_point': 'Alarm bulgusu olmayan fonksiyonel karın ağrısında rutin endoskopi '
                                                  'önerilmez; tanı klinik kriterlerle konur.',
                                'text': 'Kesin organik odak bulmak amacıyla hastaya genel anestezi altında acil '
                                        'kolonoskopi ve gastroskopi yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tekrarlayan tomografiler 8 yaşındaki çocuğu yüksek iyonizan '
                                                   'radyasyon kümülatif dozuna maruz bıraktı.',
                                'teaching_point': 'Fonksiyonel karın ağrısında bilgisayarlı tomografinin kesinlikle '
                                                  'yeri yoktur.',
                                'text': 'Karnı ağrıdığı için hastaya her sabah acil serviste kontrastlı tüm batın '
                                        'tomografisi çektirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Hastaneye yatırılan çocuk okuldan tamamen koptu ve hastalık rolü '
                                                   'pekişerek ağrıları kronikleşti.',
                                'teaching_point': 'Fonksiyonel ağrılarda hastaneye yatış sakatlayıcıdır; çocuk normal '
                                                  'hayatına devam etmelidir.',
                                'text': 'Ağrının nedenini netleştirmek için hastayı 1 ay boyunca hastanede damardan '
                                        'beslenmeye almak'}],
                 'question': 'Kırmızı bayrak taşımayan, büyümesi normal bu çocukta tanısal tetkik stratejisi nasıl '
                             'olmalıdır?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Büyüme gelişmesi normal, organik alarm bulgusu olmayan ve okul '
                                               'stresiyle tetiklenen göbek çevresi ağrı Fonksiyonel Karın Ağrısıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Fonksiyonel Karın Ağrısı (Roma IV Kriterleri Pozitif - '
                                               'Okul Kaygısı İlişkili).',
                                'text': 'Fonksiyonel karın ağrısı tablosu'},
                              { 'is_correct': False,
                                'scenario_update': "İBH'de kilo kaybı, anemi, kanlı ishal ve gece ağrıyla uyanma olur; "
                                                   'bu hastada büyüme ve dışkılama tamamen doğaldır.',
                                'teaching_point': 'İBH organik destrüktif hastalıktır; kilo kaybı ve gece semptomları '
                                                  'olmadan düşünülmez.',
                                'text': 'İnflamatuar bağırsak kronik hastalığı'},
                              { 'is_correct': False,
                                'scenario_update': 'Peptik ülserde yemekle ilişkili epigastrik ağrı ve gece uyanma '
                                                   'olur; okul sabahıyla sınırlı göbek çevresi ağrısı yapmaz.',
                                'teaching_point': 'Ülser ağrısı gece uyandırır; fonksiyonel ağrı ise sadece uyanıkken '
                                                  've stres anında hissedilir.',
                                'text': 'Kronik gastrit peptik ülseri'},
                              { 'is_correct': False,
                                'scenario_update': 'İdrar tahlili tamamen temizdir; dizüri veya polaküri yoktur.',
                                'teaching_point': 'İdrar tahlili normalse karın ağrısı idrar yolu enfeksiyonuna '
                                                  'bağlanamaz.',
                                'text': 'Kronik tekrarlayan idrar yolu'}],
                 'question': 'Okul sabahları ağrı, hafta sonu rahatlama, normal büyüme ve kırmızı bayrak yokluğu ile '
                             'tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'En önemli kural okul devamlılığıdır (okula gitmemek anksiyete '
                                               'döngüsünü besler). Aileye ve çocuğa beyin-bağırsak aksı anlatılır, '
                                               'ağrı anında nefes egzersizleri ve dikkat dağıtma önerilir. '
                                               'Gerektiğinde okul rehberliği ve psikoterapi planlanır.',
                                'is_correct': True,
                                'new_finding': 'Aileye ve çocuğa durum açıklandı. Çocuğun okula devamı sağlandı, okul '
                                               'rehberlik servisiyle iletişime geçildi. 1 ay içinde sabah ağrıları '
                                               'azalarak kayboldu ve çocuğun okul başarısı arttı.',
                                'text': 'Ağrının gerçek olduğunu kabul etmek, organik hastalık olmadığını anlatmak ve '
                                        'çocuğun okula düzenli devamını sağlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Okuldan alınan çocukta sosyal fobi, anksiyete derinleşmesi ve '
                                                   'kronik sakatlık davranışı gelişti.',
                                'teaching_point': 'Okuldan alıkoymak fonksiyonel ağrılarda en zararlı yaklaşımdır; '
                                                  'okula devam tedavinin temel parçasıdır.',
                                'text': 'Ağrı tamamen geçene kadar çocuğu altı ay boyunca okuldan tamamen alıp evde '
                                        'yatak hapsinde tutmak'},
                              { 'is_correct': False,
                                'scenario_update': "İlaç verilmesi çocuğun 'ben hastayım' inancını pekiştirdi ve "
                                                   'ağrıyı sonlandıramadı.',
                                'teaching_point': 'Fonksiyonel ağrılarda asit baskılayıcıların yeri yoktur; plasebodan '
                                                  'farksızdır ve yan etki riski taşır.',
                                'text': 'Ağrıyı dindirmek için hastaya her sabah düzenli yüksek doz antiasit ve proton '
                                        'pompa inhibitörü başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Cerrahi yapılan hastada ameliyat sonrası ameliyat skarı bölgesinde '
                                                   'somatizasyon ağrıları sürdü.',
                                'teaching_point': 'Fonksiyonel karın ağrısına cerrahi girişim uygulanması '
                                                  'kontrendikedir; cerrahi ağrıyı çözmez.',
                                'text': 'Karın ağrısını yok etmek amacıyla hastaya acil cerrahi ile profilaktik '
                                        'laparoskopik apendektomi yapmak'}],
                 'question': 'Fonksiyonel karın ağrısı tanısı konulan bu hastada en uygun tedavi ve psikososyal '
                             'yönetim hangisidir?',
                 'stage_title': 'Tedavi, Aile Güvencesi ve Okul Devamlılığı'}]},
  { 'age': '20 Aylık',
    'case_pearl': 'Çölyak hastalığının klasik pediatrik formu genellikle buğday/arpa/çavdar (gluten) içeren ek '
                  'gıdaların başlanmasından aylar sonra (9-24. aylar arasında) ortaya çıkar. Klasik triyad: Kronik '
                  'malabsorptif ishal (açık renkli, hacimli, yağlı), karın distansiyonu ve belirgin kas erimesi '
                  "(özellikle gluteal kas atrofisi / 'düz tabak popo' görünümü) ile persentil kaybıdır. ESPGHAN "
                  'kılavuzlarına göre ilk basamak tarama testi: DOKU TRANSGLUTAMİNAZ IgA (Anti-tTG IgA) ve TOTAL IgA '
                  'düzeyidir (IgA eksikliği varsa yanlış negatifliği önlemek için IgG bazlı testler istenir). EN '
                  'KRİTİK KLİNİK KURAL: Tanı kesinleşene kadar (gerekirse endoskopi ve biyopsi tamamlanana kadar) '
                  'ÇOCUĞUN DİYETİNDEN GLUTEN ASLA KESİLMEMELİDİR! Erken gluten kesilmesi serolojiyi ve biyopsiyi '
                  'normale çevirerek tanıyı imkansız kılar.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Ek gıdaya geçtikten sonra giderek belirginleşen karın şişliği, açık renkli yağlı ishal ve popoda '
                 'erime',
    'disposition': 'Yeşil Alandan Serolojik Testler (Anti-tTG IgA + Total IgA) İstenmesi, Biyopsi Öncesi Gluten '
                   'Kesilmeyerek Sevk',
    'final_diagnosis': 'Çölyak Hastalığı (Klasik Malabsorptif Form / Gluten Enteropatisi)',
    'gender': 'Erkek',
    'history': "Yirmi aylık erkek bebek annesi tarafından getiriliyor: 'Sekiz aylıkken ek gıdaya (tahıllar, bisküvi, "
               'ekmek) başlandıktan sonra dışkısı giderek cıvıklaştı, açık renkli, aşırı parlak ve kötü kokulu oldu. '
               'Son 6 aydır kilo alımı tamamen durdu, 75. persentilden 10. persentile geriledi. Karnı kurbağa karnı '
               "gibi şişiyor, bacakları ve poposu ip gibi eridi. Sürekli huysuz ve mutsuz, yemek seçiyor.'",
    'id': 'G54',
    'steps': [ { 'options': [ { 'explanation': "Kronik enteropati ve malabsorpsiyon tablolarında persentil düşüşü, distandü batın ('kurbağa karnı') "
                                               've gluteal bölge kas erimesi (tabak popo) fizik muayenenin en '
                                               'karakteristik bulgularıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 102/dk, SS 22/dk, SpO2 %99, TA 90/58 '
                                               'mmHg. Tartı: 75. persentilden 10. persentilin altına düşmüş (kronik '
                                               'malnütrisyon). Genel görünüm soluk, apatik ve mutsuz. Batın belirgin '
                                               'distandü, timpanik, defans veya rebound yok. Bilateral gluteal kaslar '
                                               "tamamen erimiş, deri kıvrımları sarkmış ('tabak popo' görünümü). "
                                               'Pretibial ödem yok.',
                                'text': 'Büyüme eğrisi kaybını, karın distansiyonunu, gluteal kas atrofisini ve '
                                        'malnütrisyon bulgularını sistemik muayene etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Muayenesiz cerrahi hazırlığı kronik malnütrisyonlu çocukta '
                                                   'gereksiz ameliyathane travması yarattı.',
                                'teaching_point': 'Kronik malabsorpsiyondaki karın distansiyonu bağırsak hipotonisine ve gaz birikimine '
                                                  'bağlıdır; akut cerrahi batın değildir.',
                                'text': 'Karın şişliğini akut cerrahi peritonit kabul edip çocuğu muayene etmeden acil '
                                        'laparotomiye hazırlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Loperamid verilmesi malabsorptif bağırsakta paralitik ileusa ve '
                                                   'ağır distansiyona yol açtı.',
                                'teaching_point': 'Malabsorpsiyonlu çocuklarda loperamid KESİNLİKLE KONTRENDİKEDİR; '
                                                  'toksik ileus yapar.',
                                'text': 'İshali hemen durdurmak için hastaya acil serviste yüksek doz motilite '
                                        'baskılayıcı loperamid içirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Nörolojik muayenesi doğal olan çocukta uygunsuz cerrahi '
                                                   'konsültasyon süreci başlatıldı.',
                                'teaching_point': 'Gluteal kas erimesi tipik malnütrisyon bulgusudur; nörolojik felç '
                                                  'tablosu değildir.',
                                'text': 'Kas erimesini felç sanarak hastaya fizik muayene yapmadan acil beyin ve '
                                        'omurilik cerrahisi konsültasyonu istemek'}],
                 'question': 'Ek gıda sonrası kronik ishal, karın şişliği ve kas erimesi olan bu çocukta ilk muayene '
                             'yaklaşımı nasıl olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'ESPGHAN kılavuzlarına göre bu klinik tablonun taranmasında ilk tercih Anti-tTG IgA '
                                               "ve Total IgA'dır. Total IgA düzeyi, çölyaklılarda sık görülen selektif "
                                               'IgA eksikliğine bağlı yalancı negatiflikleri dışlamak için şarttır.',
                                'is_correct': True,
                                'new_finding': 'Laboratuvar: Anti-tTG IgA: >200 U/mL (normal üst sınırın 10 katından '
                                               'yüksek, >10x ULN). Total IgA: 68 mg/dL (yaşına göre normal, IgA '
                                               'eksikliği yok). Hemogram: Hb 9.8 g/dL (hafif mikrositer demir '
                                               'eksikliği anemisi), Ferritin 8 ng/mL (düşük).',
                                'text': 'Kanda Doku Transglutaminaz IgA antikor düzeyi ile birlikte selektif eksikliği '
                                        'dışlamak için Total IgA düzeyini istemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Kolonoskopi normal geldi çünkü çölyak kolonu değil, ince '
                                                   'bağırsağın proksimalini (duodenum) tutar.',
                                'teaching_point': 'Bu enteropati ince bağırsak hastalığıdır; kolonoskopi tanısal değildir, '
                                                  'duodenal biyopsi gerekir.',
                                'text': 'Antikor bakmadan hastaya derhal genel anestezi altında kolonoskopi yaparak '
                                        'kalın bağırsaktan biyopsi almak'},
                              { 'is_correct': False,
                                'scenario_update': 'İdrar ve gaita testleri normal çıktı ancak spesifik seroloji '
                                                   'bakılmadığı için tanı atlandı.',
                                'teaching_point': 'Kronik malabsorpsiyon serolojik antikorlarla taranır; idrar veya dışkı gizli kanı '
                                                  'tanı koydurmaz.',
                                'text': 'Etiyolojiyi araştırmadan sadece dışkıda gizli kan ve idrar kültürü bakarak hastayı '
                                        'evine göndermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Test yapılmadan diyet verilen çocukta tanı serolojik olarak asla '
                                                   'kanıtlanamaz hale geldi.',
                                'teaching_point': 'Seroloji doğrulanmadan ampirik diyet başlanması tanıyı imkansız '
                                                  'kılar; KESİNLİKLE YASAKTIR.',
                                'text': 'Antikor istemeden hastaya doğrudan ömür boyu tüm tahılları, eti ve sütü '
                                        'yasaklayan katı diyet vermek'}],
                 'question': 'Ek gıdaya geçiş sonrası kronik malabsorpsiyon ve persentil kaybı gelişen bu çocukta altın '
                             'standart tarama tetkiki hangisidir?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Gluten sonrası kronik ishal, kas erimesi, persentil kaybı ve Anti-tTG '
                                               "IgA'nın normalin 10 katını aşması klasik çölyak tanısıdır.",
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Çölyak Hastalığı (Klasik Malabsorptif Form / Gluten '
                                               'Enteropatisi).',
                                'text': 'Klasik çölyak hastalığı malabsorpsiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Kistik fibroziste ter testi pozitiftir ve çölyak antikorları '
                                                   'negatiftir; bu çocukta Anti-tTG masif yüksektir.',
                                'teaching_point': 'Kistik fibrozis ter testiyle ayrılır; Anti-tTG IgA >10 kat '
                                                  'yüksekliği çölyak için spesifiktir.',
                                'text': 'Kistik fibrozis ekzokrin yetmezliği'},
                              { 'is_correct': False,
                                'scenario_update': 'İnek sütü enteropatisi erken süt çocukluğunda başlar; gluten ek '
                                                   'gıdasıyla Anti-tTG antikoru üretmez.',
                                'teaching_point': 'Süt alerjisinde tTG antikoru oluşmaz; tTG glutene spesifik '
                                                  'otoantimikrobiyal yanıttır.',
                                'text': 'İnek sütü proteini enteropatisi'},
                              { 'is_correct': False,
                                'scenario_update': 'Giardiada dışkıda kistler olur; kronik otoimmün Anti-tTG IgA '
                                                   'pozitifliği ve gluteal erime yapmaz.',
                                'teaching_point': 'Giardia parazitozdur; masif çölyak seroloji pozitifliği oluşturmaz.',
                                'text': 'Giardiazis paraziter malabsorpsiyon sendromu'}],
                 'question': 'Gluten alımı sonrası malabsorpsiyon, persentil kaybı, gluteal erime ve Anti-tTG IgA >10 '
                             'kat yüksekliği ile tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'ESPGHAN kılavuzlarına göre kesin tanı gastroenterolog tarafından '
                                               'endoskopik duodenal biyopsi ile (veya Anti-tTG >10x ULN + pozitif EMA '
                                               'durumunda biyopsisiz protokolle) kesinleştirilene kadar GLUTEN '
                                               'KESİLMEMELİDİR. Gluten kesilirse mukoza hızla iyileşir ve tanı '
                                               'doğrulaması imkansızlaşır.',
                                'is_correct': True,
                                'new_finding': 'Aileye gastroenteroloji randevusuna kadar çocuğun ekmek/makarna yemeye '
                                               'devam etmesi gerektiği açıklandı. Pediatrik Gastroenterolojiye '
                                               'yönlendirildi; tanı doğrulanarak ömür boyu glutensiz diyet ve demir '
                                               'tedavisi başlandı.',
                                'text': 'Çocuk gastroenteroloji uzmanı değerlendirene kadar diyetten gluteni '
                                        'kesinlikle kesmemek ve normal beslenmeyi sürdürmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gluteni erken kesilen çocukta 3 hafta sonra yapılan endoskopik '
                                                   'biyopsi normal geldi ve kesin tanı konulamadı.',
                                'teaching_point': 'Tanı kesinleşmeden glutenin kesilmesi mukoza biyopsisini yalancı '
                                                  'negatif yapar; en sık yapılan klinik hatadır.',
                                'text': 'Gastroenteroloji konsültasyonunu beklemeden hastanın diyetindeki tüm buğdayı '
                                        've tahılları anında sıfırlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Antibiyotik verilmesi otoimmün enteropatiyi düzeltmedi; ek '
                                                   'bağırsak florası hasarı yarattı.',
                                'teaching_point': 'Çölyak bakteriyel enfeksiyon değildir; antibiyotiklerin hiçbir '
                                                  'etkinliği yoktur.',
                                'text': 'Çölyak hastalığını tamamen iyileştirmek amacıyla hastaya yüksek doz oral '
                                        'geniş spektrumlu antibiyotik başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Medikal diyetle tamamen düzelecek çölyak hastasına cerrahi '
                                                   'düşünülmesi malpraktis oluşturdu.',
                                'teaching_point': 'Çölyak hastalığı cerrahi bir antite değildir; tedavisi ömür boyu '
                                                  'glutensiz diyettir.',
                                'text': 'Hastaya acil cerrahi ile ince bağırsak rezeksiyonu ve ostomi açılması '
                                        'planıyla yatış vermek'}],
                 'question': 'Anti-tTG IgA düzeyi normalin 10 katından yüksek çıkan bu hastada yapılması gereken en '
                             'kritik sevk ve beslenme kuralı hangisidir?',
                 'stage_title': 'Kritik Klinik Kural ve Sevk Yönetimi'}]},
  { 'age': '6 Yaşında',
    'case_pearl': 'Pediatrik acilde sağ alt kadran karın ağrısı ve ateşle başvuran bir çocukta diafragmatik plörit '
                  'kaynaklı YANSIYAN KARIN AĞRISI (Referred Pain - T8-T11 interkostal sinir irritasyonu) mutlaka akla '
                  'gelmelidir! Sağ alt lob lober pnömonisi, apandisiti mükemmel taklit eder ve gereksiz laparotomilere '
                  'yol açabilir. En kritik fizik muayene ipucu: Solunum sayısı (takipne), burun kanadı solunumu, '
                  'inleme ve sağ bazal oskültasyonda tübüler solunum sesi (bronşiyal solunum) veya krepitan rallerdir. '
                  'Karın muayenesinde defans yüzeyseldir, derin palpasyonda gerçek peritoneal rijidite ve rebound '
                  'saptanmaz. Arka-ön akciğer grafisi tanıyı anında koydurur. Toplum kökenli tipik lober pnömonide ilk '
                  'seçenek yüksek doz oral amoksisilindir (80-90 mg/kg/gün).',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Sağ alt kadran karın ağrısı, kusma ve yüksek ateş',
    'disposition': 'Yeşil Alandan Akciğer Grafisi ile Lober Konsolidasyon Doğrulaması, Oral Amoksisilin Tedavisi ile '
                   'Taburculuk',
    'final_diagnosis': 'Sağ Alt Lob Pnömokok Lober Pnömonisi (Diafragmatik Plörit / Yansıyan Karın Ağrısı)',
    'gender': 'Erkek',
    'history': "Altı yaşındaki erkek çocuk ailesi tarafından Sarı Alana/Yeşil Alana getiriliyor: 'İki gündür 39°C "
               'ateşi ve karnının sağ tarafında şiddetli ağrısı var. İki kez kustu. Sağ kasığındaki ağrı nedeniyle dış '
               'merkezden apandisit şüphesiyle acil servise sevk edilmiş. Ancak çocuk konuşurken nefes nefese kalıyor '
               "ve hafif inliyor. Annesi dünden beri kuru kuru öksürdüğünü söylüyor.'",
    'id': 'G55',
    'steps': [ { 'options': [ { 'explanation': 'Yansıyan karın ağrısında takipne, burun kanadı solunumu ve akciğer '
                                               'dinleme bulguları (tübüler ses/ral) karın ağrısının torakal kökenli '
                                               'olduğunu ele verir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 39.1°C, KTA 134/dk, SS 42/dk (yaşa göre belirgin '
                                               'takipneik), SpO2 %96 (oda havasında), TA 102/64 mmHg. Hafif burun '
                                               'kanadı solunumu ve ekspiratuar inleme mevcut. Akciğer Oskültasyonu: '
                                               'Sağ hemitoraks bazalinde solunum sesleri azalmış, bronşiyal tübüler '
                                               'solunum sesi ve krepitan raller mevcut. Batın Muayenesi: Sağ üst ve '
                                               'alt kadranda yüzeysel hassasiyet var ancak istemsiz gerçek defans veya '
                                               'rebound saptanmadı.',
                                'text': 'Solunum sayısını, göğüs çekilmelerini, akciğer taban seslerini ve batında '
                                        'gerçek defans olup olmadığını muayene etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Pnömonisi olan çocuk ameliyata alındığında anestezi indüksiyonunda '
                                                   'ağır hipoksemi ve bronkospazm gelişti.',
                                'teaching_point': 'Karın ağrılı çocukta akciğer muayenesi ve solunum sayısı atlanırsa '
                                                  'lober pnömoni apandisit sanılarak ameliyat edilir.',
                                'text': 'Karın ağrısı sağda olduğu için akciğer oskültasyonu yapmadan çocuğu derhal '
                                        'acil apendektomi ameliyatına almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Pnömonik konsolidasyonu olan hipoksemik çocuğa kağıt torba '
                                                   'solutulması hipoksik arrest tehlikesi yarattı.',
                                'teaching_point': '39°C ateşli ve inleyen çocukta takipne solunum yolu enfeksiyonu '
                                                  'bulgusudur; panik atak değildir.',
                                'text': 'Hızlı solunumu panik atağa bağlayarak hastaya fizik muayene yapmadan acil '
                                        'serviste kağıt torbadan solutmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz ilaç verilmesi hastanın solunum reflekslerini '
                                                   'baskılayarak sekresyon birikimine yol açtı.',
                                'teaching_point': 'Pnömonide kusma öksürük ve yüksek ateşe sekonderdir; motilite '
                                                  'azaltıcı verilmez.',
                                'text': 'Kusmayı durdurmak amacıyla 6 yaşındaki çocuğa acil serviste yüksek doz '
                                        'motilite felç edici ilaç vermek'}],
                 'question': 'Apandisit şüphesiyle sevk edilen, yüksek ateş ve inlemesi olan bu çocukta ilk muayene '
                             'yaklaşımı nasıl olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'Arka-ön akciğer grafisi sağ alt lobdaki lober konsolidasyonu ve hava '
                                               'bronkogramlarını göstererek karın ağrısının plöritik yansıyan ağrı '
                                               'olduğunu kanıtlar ve cerrahiyi önler.',
                                'image': 'assets/images/cxr_lobar_pneumonia.png',
                                'is_correct': True,
                                'new_finding': 'Akciğer Grafisi (PA): Sağ akciğer alt lobunda homojen lober '
                                               'konsolidasyon, hava bronkogramları ve silüet belirtisi izlendi; '
                                               'plevral efüzyon veya pnömotoraks saptanmadı. Sol akciğer doğal. '
                                               'Laboratuvar: Lökosit 16.400/mm³ (%82 nötrofil), CRP 68 mg/L.',
                                'text': 'Lober konsolidasyonu ve olası plevral efüzyonu doğrulamak amacıyla arka-ön '
                                        'akciğer grafisi çekilmesini planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Laparoskopide apendiks tamamen normal bulundu; çocuk ameliyat '
                                                   'sonrası pnömoni komplikasyonlarıyla servise çıktı.',
                                'teaching_point': 'Takipnesi ve bazal dinleme bulgusu olan çocukta basit bir akciğer '
                                                  'grafisi gereksiz batın cerrahisini önler.',
                                'text': 'Akciğer grafisi çekmeden hastaya genel anestezi altında acil tanısal '
                                        'laparoskopi operasyonu planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Lober pnömonisi tedavi edilmeyen çocukta 24 saat içinde ampiyem ve '
                                                   'solunum yetmezliği gelişti.',
                                'teaching_point': 'Lober pnömoni acil antibiyoterapi gerektirir; taburcu edilerek '
                                                  'bekletilemez.',
                                'text': 'Grafi çekmek yerine sadece idrar tahlili alıp sonucu 24 saat sonra kontrol '
                                        'etmek üzere hastayı taburcu etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Sintigrafi pnömoni tanısında hiçbir bilgi sağlamadı ve acil '
                                                   'tedaviyi saatlerce geciktirdi.',
                                'teaching_point': 'Akut solunum enfeksiyonunda sintigrafinin yeri yoktur; PA akciğer '
                                                  'grafisi standarttır.',
                                'text': 'Tanıyı radyolojik olarak koymak amacıyla hastaya acil koşullarda tüm vücut '
                                        'kemik sintigrafisi planlamak'}],
                 'question': 'Sağ bazalde ral ve tübüler ses saptanan bu takipneik çocukta tanıyı netleştirmek için en '
                             'uygun tetkik hangisidir?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Yüksek ateş, takipne, inleme ve grafide lober infiltrasyon ile '
                                               'diafragmatik plöritik karın ağrısı lober pnömoni tanısıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Sağ Alt Lob Lober Pnömonisi (Diafragmatik Plörit Kaynaklı '
                                               'Yansıyan Karın Ağrısı).',
                                'text': 'Pnömokok lober pnömonisi konsolidasyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Akciğer grafisinde belirgin lober konsolidasyon vardır; karın '
                                                   'ağrısı plöritik yansıyan ağrıdır, apandisit dışlanmıştır.',
                                'teaching_point': 'Pnömoniye sekonder yansıyan ağrıda gerçek peritoneal defans yoktur; '
                                                  'pnömoni tedavi edilince karın ağrısı geçer.',
                                'text': 'Akut cerrahi flegmonöz apandisit'},
                              { 'is_correct': False,
                                'scenario_update': 'Gastroenteritte lober akciğer konsolidasyonu ve tübüler ses olmaz; '
                                                   'tablo alt solunum yolu parankim enfeksiyonudur.',
                                'teaching_point': 'Gastroenterit akciğerde konsolidasyon yapmaz; ateş ve kusma '
                                                  'pnömoniye ikincildir.',
                                'text': 'Akut enfeksiyöz gastroenterit tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Kolesistitte safra kesesi duvar kalınlaşması olur; PA grafide '
                                                   'lober akciğer tutulumu ve takipne beklenmez.',
                                'teaching_point': 'Pnömoni torakal patolojidir; kolesistitle karıştırılmamalıdır.',
                                'text': 'Akut taşlı kolesistit atağı'}],
                 'question': 'Yüksek ateş, takipne, sağ bazalde tübüler solunum sesi ve PA grafide sağ alt lob '
                             'konsolidasyonu ile tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Pediatrik IDSA ve NICE kılavuzlarına göre toplum kökenli tipik lober '
                                               'pnömonide (Streptococcus pneumoniae) ilk basamak tedavi YÜKSEK DOZ '
                                               'ORAL AMOKSİSİLİNDİR (80-90 mg/kg/gün 2-3 doza bölünerek, 7-10 gün). '
                                               'Oral alabilen, hipoksemisi olmayan çocuk ayaktan güvenle tedavi '
                                               'edilir.',
                                'is_correct': True,
                                'new_finding': 'Yüksek doz oral amoksisilin başlandı. 48 saat sonra ateşi tamamen '
                                               'düştü, takipnesi geriledi ve akciğer konsolidasyonu açıldıkça yansıyan '
                                               'karın ağrısı tamamen kayboldu.',
                                'text': 'Yüksek doz oral amoksisilin başlamak, parasetamol önermek ve kırk sekiz saat '
                                        'sonra kontrole çağırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz cerrahi pnömonik hastada ağır postoperatif atelektazi ve '
                                                   'solunum yetmezliği yarattı.',
                                'teaching_point': 'Karın ağrısı pnömoni kaynaklıdır; cerrahi kesinlikle endike '
                                                  'değildir, pnömoni antibiyotikle tedavi edilir.',
                                'text': 'Hastayı ameliyathaneye alıp batın boşluğunu yıkamak amacıyla acil tanısal '
                                        'batın cerrahisi uygulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tedavi edilmeyen bakteriyel lober pnömoni ampiyem ve nekrotizan '
                                                   'pnömoniye ilerledi.',
                                'teaching_point': 'Tipik lober pnömoni bakteriyeldir (S. pneumoniae); antibiyotiksiz '
                                                  'takip fatal komplikasyonlar doğurur.',
                                'text': 'Antibiyotik vermeden hastaya sadece evde sıcak buhar banyosu yaptırarak '
                                        'ayaktan taburcu etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Aminoglikozidler oral yoldan kana emilmez; pnömoniye hiçbir etkisi '
                                                   'olmadı.',
                                'teaching_point': 'Oral aminoglikozid sistemik emilmez; solunum yolu enfeksiyonlarında '
                                                  'yeri yoktur.',
                                'text': 'Hastaya oral yoldan yüksek doz geniş spektrumlu aminoglikozid şurup verip '
                                        'ayaktan takip etmek'}],
                 'question': 'Genel durumu stabil, SpO2 %96 olan toplum kökenli lober pnömonili bu çocukta en uygun '
                             'tedavi hangisidir?',
                 'stage_title': 'Pnömoni ve Karın Ağrısının Tedavisi'}]},
  { 'age': '11 Aylık',
    'case_pearl': 'Dünya Sağlık Örgütü (DSÖ) ve UNICEF, akut gastroenteritli 6 ay - 5 yaş arası tüm çocuklara akut '
                  'ishal tedavisinde ve sonraki 2-3 ay içindeki ishal nükslerini önlemede GÜNLÜK 20 MG ELEMENTAL ÇİNKO '
                  'DESTEĞİNİN (6 ay altı: 10 mg/gün) 10-14 GÜN SÜREYLE verilmesini en yüksek kanıt düzeyiyle '
                  'önermektedir. Çinko bağırsak mukozal rejenerasyonunu hızlandırır, fırçamsı kenar enzimlerini korur, '
                  'hücresel immüniteyi güçlendirir ve ishal süresini/şiddetini anlamlı derecede azaltır. Sulu kansız '
                  'ishalde rutin antibiyotik verilmemelidir.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Üç gündür günde 6 kez sulu sarı ishal, perianal bölgede asidik kızarıklık',
    'disposition': 'Yeşil Alandan DSÖ/UNICEF Protokolüyle 20 mg Elemental Çinko Desteği, ORS ve Bariyer Kremle '
                   'Taburculuk',
    'final_diagnosis': 'Akut Viral İshalde Çinko Desteği ve Kanıta Dayalı Destek Tedavisi',
    'gender': 'Erkek',
    'history': "On bir aylık erkek bebek annesi tarafından getiriliyor: 'Üç gündür sulu sarı renkte kaka yapıyor. "
               'Ateşi hafif, emmesi ve su içmesi gayet iyi. Komşumuz eczaneden antibiyotik şurup alıp içirmemizi '
               'söyledi ancak size danışmak istedik. Bez bölgesinde dışkı asidine bağlı hafif kızarıklık başladı. '
               "Kusması yok.'",
    'id': 'G56',
    'steps': [ { 'options': [ { 'explanation': 'Dehidratasyon derecesini derecelendirmek ve sık dışkılamaya sekonder '
                                               'gelişen perianal dermatit varlığını değerlendirmek fizik muayenenin '
                                               'temelidir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 37.4°C, KTA 114/dk, SS 26/dk, SpO2 %99, TA 88/54 '
                                               'mmHg, KDZ 1.5 sn. Genel durumu iyi, çevreyle ilgili. Ağız mukozası '
                                               'nemli, gözyaşı bol, deri turgoru anında geri dönüyor. Batın rahat, '
                                               'bağırsak sesleri normoaktif. Perianal bölgede hafif eritematöz asidik '
                                               'dışkı tahrişi mevcut.',
                                'text': 'Hidrasyon durumunu, mukoza nemini, kapiller dolumu ve bez bölgesindeki asidik '
                                        'eritemi muayene etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Dehidrate olmayan stabil bebeğe yoğun bakım ayrılması gereksiz '
                                                   'yatak işgaline yol açtı.',
                                'teaching_point': 'Genel durumu iyi, hidrasyonu tam olan bebekler Yeşil Alanda ayaktan '
                                                  'izlenir.',
                                'text': 'İshal sayısı altıyı aştığı için fizik muayene yapmadan hastayı derhal acil '
                                        'yoğun bakıma yatırmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Travmatik kesi bebekte derin kanama ve sekonder bakteriyel '
                                                   'enfeksiyona neden oldu.',
                                'teaching_point': 'İshale bağlı perianal eritem asidik tahriştir; abse değildir, '
                                                  'cerrahi drenaj yapılmaz.',
                                'text': 'Pişik bölgesini enfekte abse kabul ederek acil serviste steril olmadan '
                                        'bistüriyle insizyon yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Loperamid süt çocuğunda paralitik ileus ve karın distansiyonu '
                                                   'tablosu yarattı.',
                                'teaching_point': 'Süt çocuklarında motilite azaltıcı ajanlar kesinlikle '
                                                  'KONTRENDİKEDİR.',
                                'text': 'İshali hemen durdurmak için 11 aylık bebeğe ağızdan yüksek doz loperamid ve '
                                        'opiat vermek'}],
                 'question': 'Üç gündür sulu ishali olan 11 aylık bu bebekte ilk klinik değerlendirme nasıl olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'DSÖ ve ESPGHAN kılavuzlarına göre hafif, kansız, oral toleransı iyi '
                                               'akut ishallerde rutin dışkı kültürü veya biyokimya endike değildir; '
                                               'klinik tanı yeterlidir.',
                                'is_correct': True,
                                'new_finding': 'Gereksiz invaziv girişim yapılmadı. Anneye kanıta dayalı destek '
                                               'tedavisi anlatıldı.',
                                'text': 'Klinik olarak hafif seyirli sulu ishalde gereksiz kan tahlili veya dışkı '
                                        'kültürü istemeden takip planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Genel anestezi ve invaziv işlem 11 aylık bebekte komplikasyon '
                                                   'riski yarattı.',
                                'teaching_point': 'Akut sulu ishalde endoskopik inceleme kesinlikle endike değildir; '
                                                  'aşırı tetkiktir.',
                                'text': 'İshali araştırmak için bebeğe genel anestezi altında acil kolonoskopi ve '
                                        'rektoskopi yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz intravenöz antibiyotik bebeğin damar yapısını bozdu ve '
                                                   'florasını tahrip etti.',
                                'teaching_point': 'Basit sulu ishallerde geniş spektrumlu antibiyotiklerin yeri '
                                                  'yoktur; viral kaynaklıdır.',
                                'text': 'Dışkıyı sterilize etmek amacıyla hiçbir tahlil yapmadan damardan geniş '
                                        'spektrumlu vankomisin başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tekrarlayan batın grafileri bebeği gereksiz yere yüksek radyasyon '
                                                   'dozuna maruz bıraktı.',
                                'teaching_point': 'Akut gastroenteritte direkt grafi endikasyonu yoktur; radyasyon '
                                                  'zararlıdır.',
                                'text': 'Karında gaz olup olmadığını görmek için bebeğe her saat başı seri direkt '
                                        'batın grafisi çekmek'}],
                 'question': 'Oral alımı iyi, hafif dehidratasyonu bile olmayan bu bebekte tetkik planı ne olmalıdır?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Sulu dışkılama, stabil genel durum, hafif ateş ve asidik dışkı teması '
                                               'tipik akut viral gastroenterittir.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Akut Viral Gastroenterit (Hafif Seyirli / '
                                               'Dehidratasyonsuz).',
                                'text': 'Akut viral gastroenterit enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Kolerada pirinç suyu şeklinde masif şok dehidratasyonu olur; bu '
                                                   'bebek normovolemiktir.',
                                'teaching_point': 'Kolera ağır hipovolemik şokla seyreder; hafif seyirli kreş '
                                                  'ishaliyle uyumlu değildir.',
                                'text': 'Ağır kolera salgını dizanterisi'},
                              { 'is_correct': False,
                                'scenario_update': 'Kronik malabsorpsiyon haftalarca sürer ve kilo kaybı yapar; 3 '
                                                   'günlük akut tabloda düşünülmez.',
                                'teaching_point': '3 günlük ishal akut tablodur; kronik malabsorpsiyon en az 2-4 hafta '
                                                  'sürmelidir.',
                                'text': 'Kronik malabsorpsiyon sendromu diyaresi'},
                              { 'is_correct': False,
                                'scenario_update': 'Toksik megakolonda masif batın distansiyonu, peritonit ve septik '
                                                   'şok olur; bu bebeğin karnı yumuşaktır.',
                                'teaching_point': 'Toksik megakolon ölümcül bir komplikasyondur; stabil bebekte '
                                                  'görülmez.',
                                'text': 'Toksik megakolon dilatasyon tablosu'}],
                 'question': 'Üç gündür süren sulu kansız ishal, iyi hidrasyon ve perianal asidik eritem ile tanınız '
                             'nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'DSÖ/UNICEF kanıta dayalı protokolü: >6 ay çocuklarda 10-14 gün süreyle '
                                               'günlük 20 mg elemental çinko sülfat ishal süresini kısaltır, şiddetini '
                                               'azaltır ve sonraki aylarda nüksü önler. Çinko oksitli pişik kremi '
                                               'önerilir.',
                                'is_correct': True,
                                'new_finding': 'Günlük 20 mg çinko şurubu başlandı. Her dışkı sonrası ORS ve perianal '
                                               'bölgeye çinko oksitli krem önerildi. 48 saat sonra ishal sıklığı '
                                               'azaldı, 4. günde dışkı tamamen toparladı ve pişik geriledi.',
                                'text': 'Günde yirmi miligram elemental çinko desteğini on ila on dört gün süreyle '
                                        'vermek ve oral rehidratasyon sağlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Loperamid kullanımı sonrası bebekte bağırsak spazmı ve distansiyon '
                                                   'gelişti.',
                                'teaching_point': 'Çocukluk çağı ishallerinde loperamid ve gereksiz antibiyotik '
                                                  'kontrendikedir; çinko ve ORS esastır.',
                                'text': 'İshali hemen kesmek için hastaya oral antibiyotik şurup ve loperamid '
                                        'kombinasyonu reçete etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Anne sütünün kesilmesi bebeğin immün savunmasını zayıflattı ve '
                                                   'toparlanmayı geciktirdi.',
                                'teaching_point': 'İshalde anne sütü ASLA kesilmez; bağırsak iyileşmesini sağlayan en '
                                                  'değerli besindir.',
                                'text': 'Anne sütünü tamamen kestirip bebeğe sadece kaynatılmış saf su ve un çorbası '
                                        'içirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Steroid verilmesi immünsüpresyona ve viral çoğalmanın uzamasına '
                                                   'yol açtı.',
                                'teaching_point': 'Basit gastroenteritte sistemik steroidlerin yeri yoktur; '
                                                  'zararlıdır.',
                                'text': 'Çinko yerine hastaya yüksek doz sistemik kortikosteroid ampulü içirerek '
                                        'bağırsak mukozasını kurutmak'}],
                 'question': 'DSÖ ve UNICEF kılavuzlarına göre bu bebeğin tedavisinde yer alması gereken kanıta dayalı '
                             'en önemli destek tedavisi hangisidir?',
                 'stage_title': 'Kanıta Dayalı Destek Tedavi Seçimi'}]},
  { 'age': '15 Aylık',
    'case_pearl': 'Rotavirüs ve diğer viral enteropatojenler ince bağırsak villus uçlarını enfekte ederek döker '
                  '(villus atrofisi). Laktaz enzimi villusların en uç kısmında yer aldığı için hasardan en erken ve en '
                  'ağır etkilenen enzimdir. Sindirilmemiş laktoz kolona geçer; bakterilerce fermente edilerek hidrojen '
                  'gazı, metan ve laktik aside dönüşür. Sonuç: Aşırı gaz, distansiyon, kolik kramplar, patlayıcı '
                  "köpüklü sulu dışkı ve asidik dışkıya bağlı ağır perianal pişik! Dışkı pH'sı <5.5'tir ve dışkıda "
                  'redüktan madde POZİTİF saptanır. Bu durum kalıcı bir hastalık veya süt alerjisi DEĞİLDİR; sekonder '
                  'geçici bir enzim yetmezliğidir. Tedavi: 2-4 hafta süreyle laktozsuz mama/süt kullanılmasıdır. '
                  'Villuslar rejenere olunca laktoz yavaşça tekrar açılır.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Rotavirüs ishalinden sonra süt veya yoğurt yediğinde karnında aşırı gurultu, patlayıcı köpüklü sulu '
                 'ishal ve pişik',
    'disposition': 'Yeşil Alandan Geçici 2-4 Hafta Laktozsuz Diyet / Süt, Perianal Çinko Oksit Bariyer ve Diyet '
                   'Yeniden Açma Eğitimi',
    'final_diagnosis': 'Sekonder (Post-Enfeksiyöz) Laktoz İntoleransı (Rotavirüs Sonrası Geçici Laktaz Enzim '
                       'Yetmezliği)',
    'gender': 'Kız',
    'history': "On beş aylık kız çocuk annesi tarafından getiriliyor: 'On gün önce rotavirüs ishali geçirdi, ateşi ve "
               'kusması düzeldi. Ancak ne zaman inek sütü veya yoğurt yedirsem yarım saat sonra karnında fırtına '
               'kopuyor, gurul gurul sesler geliyor ve bezinden fışkırır tarzda köpüklü, asidik, sapsarı sulu kaka '
               'çıkıyor. Kakası poposunu anında yakıp kıpkırmızı yapıyor. Süt vermediğim zaman kakası düzeliyor gibi '
               "ama süt içer içmez tekrar patlıyor.'",
    'id': 'G57',
    'steps': [ { 'options': [ { 'explanation': 'Asidik laktik asitli dışkının yaptığı perianal haşlanma benzeri '
                                               'eritem, batında gaz distansiyonu ve hiperaktif sesler karbonhidrat '
                                               'malabsorpsiyonunun tipik bulgularıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 104/dk, SS 22/dk, SpO2 %99, TA 94/58 '
                                               'mmHg. Genel durumu iyi, neşeli. Batın hafif distandü, timpanik, '
                                               'palpasyonla yaygın gaz gurultusu alınıyor; defans ve rebound yok. '
                                               'Perianal bölgede asidik dışkı temas alanında belirgin parlak kırmızı, '
                                               'yanık benzeri eritematöz pişik mevcut.',
                                'text': 'Perianal asidik yanık eritemini, batın distansiyonunu, bağırsak seslerini ve '
                                        'hidrasyon durumunu sistemik olarak muayene etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Asidik tahriş olan cilde yapılan cerrahi müdahale derin doku '
                                                   'hasarı ve kanamaya yol açtı.',
                                'teaching_point': 'Perianal eritem laktik asit tahrişidir; cerrahi debridman '
                                                  'kesinlikle kontrendikedir.',
                                'text': 'Perianal kızarıklığı cerrahi nekroz sanarak acil serviste steril olmadan '
                                        'bölgeye geniş cerrahi debridman yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Loperamid verilmesi kolondaki laktoz fermantasyon gazını '
                                                   'hapsederek masif karın ağrısı ve ileus yarattı.',
                                'teaching_point': 'Karbonhidrat malabsorpsiyonunda motilite azaltıcılar gaz birikimini '
                                                  've krampı fırlatır; KONTRENDİKEDİR.',
                                'text': 'İshali hemen durdurmak için hastaya acil serviste yüksek doz motilite '
                                        'baskılayıcı loperamid enjekte etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz antimalaryal ilaç çocukta hepatotoksisite ve kusma '
                                                   'geliştirdi.',
                                'teaching_point': 'Köpüklü asidik gaita fermente laktoz gazına bağlıdır; parazitoz '
                                                  'değildir.',
                                'text': 'Kakanın köpüklü olmasını parazit kabul edip hiçbir muayene yapmadan hastaya '
                                        'oral klorokin başlamak'}],
                 'question': 'Viral ishal sonrası sütle tetiklenen köpüklü asidik ishali olan bu çocukta ilk muayene '
                             'yaklaşımı nasıl olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': "Dışkı pH'sının <5.5 olması (asidik fermantasyon) ve Clinitest ile "
                                               'dışkıda redüktan madde pozitifliği (sindirilmemiş laktoz) sekonder '
                                               'laktoz intoleransı için basit ve kesin tanı koydurur.',
                                'is_correct': True,
                                'new_finding': 'Taze Dışkı Analizi: Dışkı pH: 5.0 (belirgin asidik), Dışkıda Redüktan '
                                               'Madde: POZİTİF (++). Gaita Mikroskopisi: Lökosit yok, eritrosit yok, '
                                               'parazit veya kist saptanmadı.',
                                'text': 'Taze dışkıda pH ölçümü ve dışkıda redüktan madde testi yaparak karbonhidrat '
                                        'malabsorpsiyonunu kanıtlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Çocuk basit bir geçici tablo için invaziv anestezi ve biyopsi '
                                                   'riskine maruz bırakıldı.',
                                'teaching_point': 'Sekonder laktoz intoleransında jejunal biyopsi gerekmez; dışkı pH '
                                                  've redüktan madde yeterlidir.',
                                'text': 'Kesin tanı için 15 aylık çocuğa genel anestezi altında jejunal biyopsi ve '
                                        'mukozal enzim ölçümü yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Yüksek laktoz yüklemesi masif patlayıcı ishali tetikleyerek çocuğu '
                                                   'dehidrate etti.',
                                'teaching_point': 'Akut iyileşme evresindeki süt çocuğuna provokatif oral laktoz '
                                                  'yüklemesi yapılması zararlıdır.',
                                'text': 'Tanıyı dışlamak amacıyla hastaya oral yüksek doz laktoz içirip 24 saat acil '
                                        'serviste bekletmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Genetik test gereksiz maliyet yarattı ve sonuç haftalar sonra '
                                                   'normal olarak çıktı.',
                                'teaching_point': 'Post-enfeksiyöz laktaz eksikliği edinseldir; genetik mutasyon '
                                                  'aranmaz.',
                                'text': 'Süt alerjisi olduğunu kanıtlamak için derhal kanda genetik kazein mutasyon '
                                        'analizi istemek'}],
                 'question': 'Sekonder laktoz intoleransı şüphesini doğrulamak için en uygun ve pratik tanısal test '
                             'hangisidir?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Viral enterit sonrası villus hasarına bağlı gelişen, sütle tetiklenen '
                                               'asidik köpüklü ishal ve pozitif redüktan madde sekonder laktoz '
                                               'intoleransıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Rotavirüs Enfeksiyonuna Sekonder Geçici Laktoz '
                                               'İntoleransı.',
                                'text': 'Sekonder post-enfeksiyöz laktoz intoleransı'},
                              { 'is_correct': False,
                                'scenario_update': 'Primer konjenital eksiklik doğumun ilk gününden itibaren hayatı '
                                                   'tehdit eden ishal yapar; 15 aylıkken enfeksiyon sonrası başlamaz.',
                                'teaching_point': 'Primer konjenital laktaz eksikliği doğumda başlar ve çok nadirdir; '
                                                  'enfeksiyon sonrası gelişen sekonderdir.',
                                'text': 'Primer konjenital laktaz eksikliği'},
                              { 'is_correct': False,
                                'scenario_update': 'Süt proteini alerjisi immünolojik bir reaksiyondur (mukus/kan); '
                                                   'laktaz enzim eksikliğine bağlı redüktan madde pozitifliği yapmaz.',
                                'teaching_point': 'Laktoz intoleransı enzim eksikliğidir; inek sütü alerjisi ise '
                                                  'protein immün reaksiyonudur, ikisi farklıdır.',
                                'text': 'İnek sütü proteini alerjisi'},
                              { 'is_correct': False,
                                'scenario_update': 'Çölyak glutenle tetiklenir; izole süt alımından yarım saat sonra '
                                                   'patlayıcı asidik köpüklü dışkılama yapmaz.',
                                'teaching_point': 'Çölyak kronik gluten hasarıdır; post-viral süt intoleransıyla '
                                                  'karışmaz.',
                                'text': 'Çölyak otoimmün enteropatisi hastalığı'}],
                 'question': "Gastroenterit sonrası süt alımıyla artan köpüklü ishal, asidik dışkı pH'sı ve pozitif "
                             'redüktan madde ile tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Tedavi geçicidir: İnce bağırsak villuslarının ve laktaz enziminin '
                                               'kendini yenilemesi için 2-4 hafta laktozsuz süt/mama verilir. Asidik '
                                               'pişik için bariyer çinko oksit krem kullanılır. 3-4 hafta sonra normal '
                                               'süt ürünleri yavaşça diyete yeniden eklenir; kalıcı diyet kısıtlaması '
                                               'yapılmaz.',
                                'is_correct': True,
                                'new_finding': 'Laktozsuz süte geçildi, çinko oksitli krem başlandı. 48 saat içinde '
                                               'patlayıcı ishal tamamen durdu, dışkı şekillendi ve pişik geriledi. 3 '
                                               'hafta sonra normal yoğurt ve süt sorunsuz yeniden başlandı.',
                                'text': 'İki ila dört hafta laktozsuz süte geçmek, çinko oksit uygulamak ve sonra '
                                        'laktozu yavaşça açmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz ömür boyu kısıtlama çocukta kalsiyum eksikliği ve kemik '
                                                   'mineralizasyon bozukluğu yarattı.',
                                'teaching_point': 'Sekonder laktoz intoleransı geçicidir (2-4 hafta); ömür boyu süt '
                                                  'kısıtlaması yapılmaz.',
                                'text': 'Çocuğa ömür boyu tüm süt ve süt ürünlerini tamamen yasaklayarak katı vegan '
                                        'beslenme başlatmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz antibiyotikler bağırsak villus hasarını uzatarak laktaz '
                                                   'enziminin toparlanmasını geciktirdi.',
                                'teaching_point': 'Enzim yetmezliğinde antibiyotiklerin yeri yoktur; mukozayı daha da '
                                                  'tahriş eder.',
                                'text': 'İshali hemen durdurmak amacıyla çocuğa acil antibiyotik ve antifungal '
                                        'süspansiyon kombinasyonu başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Aşırı laktoz yüklemesi masif asidik ishali ve derin cilt nekrozunu '
                                                   'tetikledi.',
                                'teaching_point': 'Akut evrede laktoz kısıtlanmazsa mukozal iyileşme gecikir ve ağır '
                                                  'pişik devam eder.',
                                'text': 'Diyete hiç dokunmayıp bağırsakların alışması için günde iki litre yağlı inek '
                                        'sütü içirmeye zorlamak'}],
                 'question': 'Sekonder laktoz intoleransı saptanan bu çocuğun beslenme tedavisi ve aile rehberliği '
                             'nasıl olmalıdır?',
                 'stage_title': 'Diyet Yönetimi ve İyileşme Süreci Eğitimi'}]},
  { 'age': '7 Yaşında',
    'case_pearl': 'Hareket Hastalığı (Kinetozis / Taşıt Tutması), vestibüler sistem (iç kulak), görsel uyaranlar '
                  '(gözler) ve proprioseptif duyular (kas-eklem alıcıları) arasındaki duyu uyuşmazlığından (sensory '
                  'mismatch / sensory conflict) kaynaklanan fizyolojik bir tablodur. Özellikle 2-12 yaş grubundaki '
                  'çocuklarda çok sıktır. Araç hareket halindeyken iç kulak hareketi algılarken, çocuğun kitap okuması '
                  'veya ekrana bakması nedeniyle gözler ortamı sabit algılar. Bu çatışma otonomik semptomları (esneme, '
                  'solukluk, soğuk terleme, mide kazınması) ve ardından kusmayı tetikler. Nörolojik muayene tamamen '
                  'doğaldır. Tedavide davranışsal önlemler esastır: Ön koltuğa oturtmak, ufuk çizgisine baktırmak, '
                  'araç içinde kitap/ekran yasağı, hafif karbonhidratlı atıştırmalık, temiz hava girişi. Şiddetli '
                  'olgularda yolculuktan 30-60 dakika önce 1. kuşak antihistaminik (dimenhidrinat vb.) profilaktik '
                  'verilebilir.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Uzun araba yolculuklarında arka koltukta telefonla oynarken başlayan şiddetli bulantı, kusma ve '
                 'soğuk terleme',
    'disposition': 'Yeşil Alandan Nörolojik Muayenenin Doğrulanması, Davranışsal Önlemler ve Yolculuk Profilaksisi '
                   'Eğitimi ile Taburculuk',
    'final_diagnosis': 'Hareket Hastalığı (Taşıt Tutması / Motion Sickness / Kinetozis)',
    'gender': 'Kız',
    'history': "Yedi yaşındaki kız çocuk ailesi tarafından Yeşil Alana getiriliyor: 'Ailecek arabayla seyahat ederken "
               'yolculuğun ilk saatinde çocukta esneme, solukluk, soğuk soğuk terleme ve ardından fışkırır tarzda '
               'kusma başladı. Arka koltukta oturup elinde telefonla çizgi film izliyordu. Arabayı kenara çekip açık '
               'havaya çıkarınca 15-20 dakikada tamamen kendine geldi, su içti, güldü. Ancak arabaya binip virajlı '
               'yollara girince aynı bulantı ve kusma tekrar etti. Evdeyken hiçbir şikayeti yok. Beyninde tümör mü var '
               "diye çok korktuk.'",
    'id': 'G58',
    'steps': [ { 'options': [ { 'explanation': 'KİBAS (tümör), serebellar patolojiler ve iç kulak vestibülopatilerini '
                                               'dışlamak için tam nörolojik ve serebellar değerlendirme yapılmalıdır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 86/dk, SS 18/dk, SpO2 %100, TA 102/64 '
                                               'mmHg. Genel durumu çok iyi, arabadan inince tamamen toparlamış, '
                                               'neşeli. Nörolojik Muayene: Kraniyal sinirler intakt, nistagmus yok, '
                                               'parmak-burun testi doğal, disdiadokokinezi yok, Romberg negatif, '
                                               'tandem yürüyüşü kusursuz. Kulak zarları doğal. Batın rahat, hassasiyet '
                                               'veya defans yok.',
                                'text': 'Nörolojik muayeneyi, serebellar testleri, dengesini, yürüyüşünü ve batın '
                                        'muayenesini sistemik olarak incelemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Muayenesiz cerrahiye yönlendirilen hastada ailede haksız derin '
                                                   'korku ve panik yaratıldı.',
                                'teaching_point': 'Sadece araçta olan ve araç durunca düzelen kusma intrakraniyal '
                                                  'kitle değildir; kinetozistir.',
                                'text': 'Kusan çocuğu derhal beyin tümörü kabul ederek fizik muayene yapmadan acil '
                                        'ameliyathaneye sevk etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Antipsikotik verilmesi çocukta akut distoni ve derin uyku hali '
                                                   'oluşturdu.',
                                'teaching_point': 'Taşıt tutmasında nöroleptikler kullanılmaz; tablo araçtan inince '
                                                  'zaten spontan düzelir.',
                                'text': 'Kusmayı durdurmak amacıyla 7 yaşındaki çocuğa acil serviste yüksek doz '
                                        'antipsikotik ilaç enjeksiyonu yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Gereksiz antibiyotik çocuğun midesini tahriş ederek bulantıyı daha '
                                                   'da artırdı.',
                                'teaching_point': 'Araç hareketine bağlı kusma enfeksiyon veya gıda zehirlenmesi '
                                                  'değildir; antibiyotik verilmez.',
                                'text': 'Kusmanın gıda zehirlenmesi olduğunu varsayıp fizik muayene yapmadan hastaya '
                                        'oral antibiyotik başlamak'}],
                 'question': 'Araç yolculuklarında tekrarlayan kusması olan bu çocukta ilk fizik muayene yaklaşımı '
                             'nasıl olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'Tipik kinetozis anamnezi olan ve nörolojik muayenesi kusursuz çocukta '
                                               'kraniyal BT, MRG veya laboratuvar tetkiklerinin yeri yoktur; klinik '
                                               'tanı yeterlidir.',
                                'is_correct': True,
                                'new_finding': 'Gereksiz kraniyal radyasyon ve invaziv tetkiklerden kaçınıldı. Aileye '
                                               'durumun fizyolojisi açıklandı.',
                                'text': 'Nörolojik odak bulgusu olmayan ve araç durunca tamamen düzelen bu hastada '
                                        'hiçbir radyolojik tetkik istememek'},
                              { 'is_correct': False,
                                'scenario_update': 'MRG tamamen normal geldi ancak çocuk gereksiz kontrast madde ve '
                                                   'hastane anksiyetesine maruz kaldı.',
                                'teaching_point': 'Tipik hareket hastalığında intrakraniyal görüntüleme endike '
                                                  'değildir; sensory mismatch tablosudur.',
                                'text': 'Kusmayı aydınlatmak için hastaya kontrastlı beyin ve tüm omurilik manyetik '
                                        'rezonans görüntülemesi planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Normal kulak zarına yapılan parasentez çocukta travmatik '
                                                   'perforasyon ve işitme kaybı yarattı.',
                                'teaching_point': 'Kinetozis iç kulak enfeksiyonu değildir; invaziv kulak girişimleri '
                                                  'kontrendikedir.',
                                'text': 'İç kulakta enfeksiyon aramak amacıyla genel anestezi altında acil tanısal '
                                        'orta kulak parasentezi yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Normal tetkikler için hasta saatlerce acil serviste tutuldu; '
                                                   'yolculuk planı aksadı.',
                                'teaching_point': 'Araç içi hareket ilişkili kusmada toksikolojik tarama endikasyonu '
                                                  'yoktur.',
                                'text': 'Kanda zehirlenme taraması yapmak amacıyla ağır metal paneli ve tam biyokimya '
                                        'gönderip yatış vermek'}],
                 'question': 'Nörolojik muayenesi tamamen doğal olan ve araç durunca düzelen bu çocukta tetkik planı '
                             'ne olmalıdır?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Araç hareketi ve ekran bakışıyla tetiklenen, dinlenmeyle geçen '
                                               'otonomik semptomlar ve kusma Kinetozis (Hareket Hastalığı) tanısıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Hareket Hastalığı (Taşıt Tutması / Kinetozis / Motion '
                                               'Sickness).',
                                'text': 'Hareket hastalığı kinetozis tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Posterior fossa kitlesinde ataksi, sabah kusmaları, nistagmus ve '
                                                   'papilödem olur; araç durunca semptomlar sıfırlanmaz.',
                                'teaching_point': 'Beyin tümörü ilerleyicidir ve fokal bulgu verir; kinetozis ise araç '
                                                  'dışında tamamen asemptomatiktir.',
                                'text': 'Posterior fossa tümörü kütlesi'},
                              { 'is_correct': False,
                                'scenario_update': 'Vertigoda baş dönmesi nöbetleri olur ve nistagmus eşlik eder; araç '
                                                   'içi ekran bakışıyla sınırlı kusma değildir.',
                                'teaching_point': 'Vertigo istirahatte de nöbet yapar; kinetozis ise pasif hareket ve '
                                                  'duyusal çelişkiyle tetiklenir.',
                                'text': 'Akut benign paroksizmal vertigo'},
                              { 'is_correct': False,
                                'scenario_update': 'Siklik kusmada saatlerce/günlerce süren, araçtan bağımsız '
                                                   'periyodik kusma fırtınaları olur.',
                                'teaching_point': 'Siklik kusma dehidrate eden uzamış ataklardır; kinetozis gibi araç '
                                                  'durunca 15 dakikada düzelmez.',
                                'text': 'Siklik kusma sendromu atağı'}],
                 'question': 'Sadece araba hareket halindeyken olan, açık havada hızla düzelen kusma ve normal '
                             'nöroloji ile tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Duyusal çelişkiyi önlemek için araçta telefon/kitap yasaklanır; çocuk '
                                               'ön koltuğa oturtulup uzak ufka bakması sağlanır. Araç iyi '
                                               'havalandırılır, yolculuk öncesi hafif kraker yedirilir. Gerekirse '
                                               'seyahatten 30-60 dk önce profilaktik antihistaminik verilir.',
                                'is_correct': True,
                                'new_finding': 'Aileye davranışsal önlemler anlatıldı. Dönüş yolculuğunda çocuk ön '
                                               'koltukta ufka bakarak ve müzik dinleyerek seyahat etti; hiç kusmadı ve '
                                               'yolculuğu rahat tamamladı.',
                                'text': 'Yolculukta ekran ve kitap okumayı yasaklamak, ufuk çizgisine baktırmak, '
                                        'havalandırma sağlamak ve gerekirse antihistaminik vermek'},
                              { 'is_correct': False,
                                'scenario_update': 'Ulaşım yasağı çocuğun ve ailenin sosyal hayatını felç etti.',
                                'teaching_point': 'Kinetozis basit önlemlerle yönetilir; seyahat kısıtlaması '
                                                  'kesinlikle gerekmez.',
                                'text': 'Çocuğun bir daha ömür boyu hiçbir arabaya, otobüse veya uçağa binmesini '
                                        'kesinlikle yasaklamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Ağır yemek mide boşalmasını geciktirerek ilk tümsekte masif '
                                                   'fışkırır kusmaya yol açtı.',
                                'teaching_point': 'Yolculuk öncesi ağır yağlı yemekler kusmayı tetikler; hafif '
                                                  'karbonhidratlı atıştırmalıklar önerilir.',
                                'text': 'Yolculuk öncesinde çocuğun midesini tamamen doldurmak için bol yağlı ağır '
                                        'yemekler yedirmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Gözleri bağlanan çocuk vestibüler uyaranı dengeleyemediği için '
                                                   'daha şiddetli baş dönmesine girdi.',
                                'teaching_point': 'Gözlerin ufuk çizgisini görmesi duyusal uyumu sağlar; gözün '
                                                  'bağlanması çelişkiyi çözmez.',
                                'text': 'Kusmayı önlemek amacıyla çocuğun gözlerini yolculuk boyunca sıkı bir bezle '
                                        'bağlayıp uyutmaya zorlamak'}],
                 'question': 'Kinetozis tanısı konulan bu çocuğun ailesine verilecek en uygun davranışsal ve medikal '
                             'profilaksi eğitimi hangisidir?',
                 'stage_title': 'Profilaksi ve Gelecek Yolculuklar İçin Öneriler'}]},
  { 'age': '6 Yaşında',
    'case_pearl': 'Enterobius vermicularis (kıl kurdu / pinworm), dünya genelinde çocuklarda en sık görülen nematod '
                  'enfeksiyonudur. Dişi parazit geceleri rektumdan çıkarak perianal deriye binlerce mikroskobik '
                  'yumurta bırakır; bu durum gece şiddetlenen yoğun perianal kaşıntıya (pruritus ani), uyku '
                  'bozukluklarına ve diş gıcırdatmaya (bruksizm) yol açar. Enfeksiyon fekal-oral yolla (tırnak altı '
                  'yumurtaların ağza götürülmesi, yatak çarşafları) son derece kolay bulaşır. Rutin gaita '
                  'mikroskopisinde yumurtalar NADİREN görülür (dışkıya değil perianal deriye bırakılır). Tanıda altın '
                  'standart sabah uyanınca dışkılama ve banyo öncesi yapılan SELOFAN BANT TESTİDİR (Sellotape testi). '
                  'EN KRİTİK TEDAVİ KURALI: 1) Semptomu olsun olmasın TÜM AİLE BİREYLERİ AYNI GÜN TEDAVİ EDİLMELİDİR! '
                  '2) İlaçlar (pirantel pamoat veya mebendazol) sadece erişkin kurtları öldürür, yumurtaları öldürmez; '
                  'bu nedenle yeni çıkan larvaları yok etmek için İKİ HAFTA SONRA MUTLAKA İKİNCİ DOZ TEKRARLANMALIDIR! '
                  'Çarşaflar sıcakta yıkanmalıdır.',
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Özellikle geceleri yatağa girdikten sonra başlayan şiddetli makat kaşıntısı, huzursuz uyku ve diş '
                 'gıcırdatma',
    'disposition': 'Yeşil Alandan Selofan Bant Yöntemi Eğitimi, Tek Doz Pirantel Pamoat ile TÜM AİLE TEDAVİSİ ve 2 '
                   'Hafta Sonra Tekrar',
    'final_diagnosis': 'Enterobiyazis (Kıl Kurdu / Enterobius vermicularis Enfeksiyonu)',
    'gender': 'Erkek',
    'history': "Altı yaşındaki erkek çocuk annesi tarafından getiriliyor: 'Yaklaşık üç haftadır özellikle geceleri "
               'uyuduktan 1-2 saat sonra poposunu kaşıyarak ağlayarak uyanıyor. Gündüzleri kaşıntısı çok daha az. '
               'Annesi dün gece fenerle baktığında makatının etrafında 1 cm boyunda beyaz ince pamuk ipliği gibi '
               'kıpırdayan bir kurtçuk gördüğünü söylüyor. Çocuk geceleri dişlerini gıcırdatıyor, iştahı azaldı. Evde '
               "4 yaşındaki kardeşinde de benzer kaşıntı başlamış.'",
    'id': 'G59',
    'steps': [ { 'options': [ { 'explanation': 'Perianal kaşıntı izleri (ekskoriasyon), sekonder bakteriyel enfeksiyon '
                                               've tırnak aralarındaki hijyen durumu paraziter bulaşı değerlendirmede '
                                               'esastır.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 88/dk, SS 18/dk, SpO2 %100, TA 98/62 '
                                               'mmHg. Genel durumu iyi. Batın rahat, organomegali yok. Perianal '
                                               'muayenede anal girim çevresinde tırnakla kaşımaya bağlı lineer '
                                               'ekskoriasyonlar ve hafif eritem izlendi; aktif kanayan anal fissür '
                                               'veya hemoroid saptanmadı.',
                                'text': 'Perianal bölgeyi ekskoriasyon, eritem ve tırnak altlarını hijyen yönünden '
                                        'dikkatle muayene etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Paraziter kaşıntısı olan çocuğa gereksiz cerrahi hazırlığı '
                                                   'yapılması derin endişe yarattı.',
                                'teaching_point': 'Gece kaşıntısı paraziterdir; cerrahi anal stenoz veya anatomik '
                                                  'kusur değildir.',
                                'text': 'Kaşıntıyı cerrahi anal stenoz kabul edip fizik muayene yapmadan acil '
                                        'anoplasti operasyonu planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Alkol ve çamaşır suyu anal mukozada şiddetli kimyasal yanık ve '
                                                   'dayanılmaz acı oluşturdu.',
                                'teaching_point': 'Perianal mukozaya kostik veya tahriş edici maddeler sürülmesi '
                                                  'kimyasal yanık yapar; KONTRENDİKEDİR.',
                                'text': 'Kaşıntıyı durdurmak amacıyla perianal bölgeye acil serviste saf alkol ve '
                                        'konsantre çamaşır suyu sürmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Tedavi edilmeyen enfeksiyon tüm aileye yayıldı ve çocukta sekonder '
                                                   'impetigo gelişti.',
                                'teaching_point': "Gözle görülen beyaz kurtçuk aksi kanıtlanana kadar Enterobius'tur; "
                                                  'ailece tedavi şarttır.',
                                'text': 'Ailenin gördüğü kurdu önemsemeyip hiçbir muayene yapmadan çocuğu Yeşil '
                                        'Alandan derhal eve göndermek'}],
                 'question': 'Gece perianal kaşıntısı olan bu 6 yaşındaki çocukta ilk muayene yaklaşımı nasıl '
                             'olmalıdır?',
                 'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene'},
               { 'options': [ { 'explanation': 'Enterobius yumurtaları perianal deriye bırakıldığı için dışkı '
                                               'incelemesinde nadiren çıkar (%5-10). Sabah kalkınca dışkılamadan önce '
                                               "yapılan selofan bant testi (lam üzerine yapıştırılarak) %90'ın "
                                               'üzerinde tanı koydurur.',
                                'is_correct': True,
                                'new_finding': 'Selofan Bant Testi: Mikroskopide karakteristik asimetrik, bir yüzü düz '
                                               'diğer yüzü bombeli (D harfi şeklinde) bol miktarda Enterobius '
                                               'vermicularis yumurtası izlendi.',
                                'text': 'Sabah yataktan kalkınca yıkanmadan önce perianal bölgeye şeffaf selofan bant '
                                        'testi uygulayarak yumurta aramak'},
                              { 'is_correct': False,
                                'scenario_update': 'Basit bant testiyle konan tanı için çocuk gereksiz yere invaziv '
                                                   'kolonoskopiye alındı.',
                                'teaching_point': 'Kıl kurdu tanısında kolonoskopinin yeri yoktur; selofan bant testi '
                                                  'altın standarttır.',
                                'text': 'Tanıyı kesinleştirmek amacıyla hastaya genel anestezi altında acil total '
                                        'kolonoskopi ve ileoskopi yapmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Genetik test sonuç vermedi; invaziv kan alımı çocuğu gereksiz yere '
                                                   'hırpaladı.',
                                'teaching_point': 'Kıl kurdunun kanda serolojisi veya genetik testi yoktur; lüminal '
                                                  'bir parazittir.',
                                'text': 'Kanda parazit antikorlarını aramak için hastadan elli mililitre kan alarak '
                                        'genetik sekanslama istemek'},
                              { 'is_correct': False,
                                'scenario_update': 'İdrar kültürü steril geldi; paraziter enfeksiyon tanısı ve '
                                                   'tedavisi atlandı.',
                                'teaching_point': 'Perianal kaşıntıda idrar kültürü tanısal değildir; selofan bant '
                                                  'testi yapılmalıdır.',
                                'text': 'Sadece idrar kültürü alıp perianal bölgeyi hiç incelemeden hastayı '
                                        'antibiyotikle taburcu etmek'}],
                 'question': 'Kıl kurdu tanısını mikroskopik olarak doğrulamak için en uygun ve altın standart yöntem '
                             'hangisidir?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Gece perianal kaşıntı, beyaz ipliksi kurtçuk ve selofan bantta tipik '
                                               'yumurtalar Enterobius vermicularis (kıl kurdu) tanısıdır.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Enterobius vermicularis Enfeksiyonu (Enterobiyazis / Kıl '
                                               'Kurdu).',
                                'text': 'Enterobiyazis kıl kurdu enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Streptokok dermatitinde makat çevresinde parlak kırmızı, sınırları '
                                                   'net selülit benzeri eritem olur; hareketli kurtçuk olmaz.',
                                'teaching_point': 'Streptokok dermatiti bakteriyeldir ve parlak eritem yapar; parazit '
                                                  'yumurtası ve kurt içermez.',
                                'text': 'Perianal streptokok dermatiti enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Anal fissürde dışkılama sırasında cam keser gibi şiddetli ağrı ve '
                                                   'taze kanama olur; gece izole kaşıntı yapmaz.',
                                'teaching_point': 'Fissür ağrılı dışkılama ve kanama yapar; kıl kurdu ise ağrısız gece '
                                                  'kaşıntısı yapar.',
                                'text': 'Akut anal fissür yırtığı'},
                              { 'is_correct': False,
                                'scenario_update': 'Uyuzda parmak araları, el bilekleri ve aksillada tüneller ve '
                                                   'kaşıntılı papüller olur; izole perianal kurt görülmez.',
                                'teaching_point': 'Uyuz tüm vücudu tutar; perianal ipliksi kurtçuklar kıl kurduna '
                                                  'özgüdür.',
                                'text': 'Skabiyez uyuz parazit enfeksiyonu'}],
                 'question': 'Gece artan anal kaşıntı, gözle görülen beyaz ipliksi kurt ve selofan bantta asimetrik '
                             'yumurtalar ile tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'Antihelmintikler (pirantel pamoat 11 mg/kg tek doz veya tek doz '
                                               'mebendazol 100 mg) sadece erişkin kurtları öldürür, yumurtalara etki '
                                               'etmez. Bu nedenle 2 hafta sonra MUTLAKA 2. DOZ verilmelidir. '
                                               'Asemptomatik taşıyıcılar nedeniyle evdeki herkes aynı anda tedavi '
                                               'edilmeli, çarşaflar sıcakta yıkanmalı ve tırnaklar kısa kesilmelidir.',
                                'is_correct': True,
                                'new_finding': 'Tüm aile bireylerine tek doz pirantel pamoat verildi. İki hafta sonra '
                                               "ikinci doz tekrarlandı. Çarşaf ve pijamalar 60°C'de yıkandı. Kaşıntı "
                                               'tamamen bitti, tüm ailede reenfeksiyon önlendi.',
                                'text': 'Tüm aile bireylerini aynı anda tedavi etmek ve iki hafta sonra ikinci dozu '
                                        'mutlaka tekrarlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Asemptomatik ebeveynlerden çocuğa 3 hafta sonra parazit yeniden '
                                                   'bulaştı ve kaşıntı tekrarladı.',
                                'teaching_point': 'Kıl kurdunda tek kişiyi tedavi etmek başarısızlıktır; ev içi bulaş '
                                                  'nedeniyle tüm aile tedavi edilmelidir.',
                                'text': 'Sadece kaşınan çocuğu tedavi edip diğer aile bireylerine hiçbir ilaç vermeden '
                                        'taburcu etmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Kalan yumurtalardan 2 hafta sonra yeni kurtçuklar çıktı ve '
                                                   'enfeksiyon başa döndü.',
                                'teaching_point': 'İlaçlar yumurtaları öldürmez; 2 hafta sonraki 2. doz döngüyü kırmak '
                                                  'için zorunludur.',
                                'text': 'Tek bir doz ilaç verip iki hafta sonraki ikinci dozu kesinlikle uygulamamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Antibiyotik parazite etki etmedi ve çocukta ilaca bağlı '
                                                   'antibiyotik ishali başladı.',
                                'teaching_point': 'Nematodlar bakteriyel antibiyotiklerle ölmez; spesifik '
                                                  'antihelmintik (pirantel/mebendazol) gerekir.',
                                'text': 'Paraziti öldürmek için hastaya bir ay boyunca aralıksız oral sefalosporin '
                                        'antibiyotik tedavisi vermek'}],
                 'question': 'Kıl kurdu tanısı konulan bu hastanın ve ailesinin tedavisinde uygulanacak en kritik '
                             'kanıta dayalı kural hangisidir?',
                 'stage_title': 'Tedavi Protokolü ve Ailece Tedavi Kuralı'}]},
  { 'age': '6 Yaşında',
    'case_pearl': 'A Grubu Beta Hemolitik Streptokok (AGBHS / Streptococcus pyogenes) farenjiti, okul çağı '
                  'çocuklarında tipik olarak ani başlangıçlı yüksek ateş, boğaz ağrısı, eksüdatif tonsillit, hassas '
                  'anterior servikal LAP ve ÖKSÜRÜK YOKLUĞU (Centor / McIsaac kriterleri) ile seyreder. Küçük '
                  'çocuklarda streptokok enfeksiyonları sistemik lenfoid yanıt ve mezenterik lenfadenit uyarısıyla '
                  'sıklıkla BULANTI, KUSMA VE GÖBEK ÇEVRESİ KARIN AĞRISINA yol açar! Bu durum sıklıkla yanlışlıkla '
                  'akut apandisit veya gastroenterit sanılarak boğaz muayenesinin atlanmasına neden olur. Hızlı '
                  'Antijen Testi (RAT) dakikalar içinde tanı koydurur. Tedavinin temel amacı semptomları kısaltmak, '
                  'süpüratif komplikasyonları (peritonsiller apse) ve en önemlisi AKUT ROMATİZMAL ATEŞİ (ARA) '
                  'ÖNLEMEKTİR! İlk tercih oral amoksisilin (50 mg/kg/gün tek doz veya 2 dozda, 10 gün) veya tek doz '
                  "intramüsküler Benzatin Penisilin G'dir. Tedavinin 24. saatinden sonra bulaşıcılık biter.",
    'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
    'complaint': 'Yüksek ateş, boğaz ağrısı, boyunda şişlik ve eşlik eden göbek çevresi karın ağrısı ile kusma',
    'disposition': 'Yeşil Alandan Hızlı Antijen Testi Doğrulaması, Oral Amoksisilin Tedavisi ve ARA Profilaksisi ile '
                   'Taburculuk',
    'final_diagnosis': 'Akut Streptokokal Tonsillofarenjit (AGBHS - Mezenterik Lenfoid İrritasyona Bağlı Karın Ağrısı)',
    'gender': 'Kız',
    'history': "Altı yaşındaki kız çocuk ailesi tarafından Yeşil Alana getiriliyor: 'Dün aniden 39.2°C ateş ve "
               'şiddetli boğaz ağrısı başladı, yutkunamıyor. Bugün sabah iki kez kustu ve karnının göbeğinin etrafında '
               'kramp şeklinde ağrı olduğunu söylüyor. Öksürüğü, burun akıntısı veya hapşırması hiç yok. Boynunda '
               'dokunmakla çok acıyan şişlikler fark ettik. Karnı ağrıdığı ve kustuğu için apandisit olmasından '
               "endişelendik.'",
    'id': 'G60',
    'steps': [ { 'options': [ { 'explanation': 'Karın ağrılı çocukta tonsillitin sistemik mezenterik lenfoid yanıtı '
                                               'dışlanmalı, Centor kriterleri (eksüda, servikal LAP, öksürük yokluğu) '
                                               'aranmalı ve batında cerrahi akut batın ekarte edilmelidir.',
                                'is_correct': True,
                                'new_finding': 'Vital Bulgular: Ateş 39.2°C, KTA 128/dk, SS 22/dk, SpO2 %99, TA 100/62 '
                                               'mmHg. Burun akıntısı veya konjonktivit yok, öksürük yok. Orofarenks '
                                               'Muayenesi: Tonsiller bilateral hipertrofik, hiperemik ve üzerinde '
                                               'yaygın beyaz-krem renkli pürülan eksüdalar mevcut; uvula ödemli, '
                                               'peteşiler izlendi. Bilateral anterior servikal zincirde 2x1.5 cm '
                                               'boyutlarında aşırı hassas LAP palpe edildi. Batın Muayenesi: Yumuşak, '
                                               'periumbilikal hafif hassasiyet var; defans ve rebound yok.',
                                'text': 'Orofarenksi, tonsilleri, servikal lenf nodlarını muayene edip batında '
                                        'peritonit olmadığını sistemik muayeneyle doğrulamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Ağır tonsilliti olan çocuk gereksiz apandisit cerrahisine alındı; '
                                                   'postoperatif yüksek ateş devam etti.',
                                'teaching_point': 'Karın ağrılı çocuklarda orofarenks muayenesi asla atlanmamalıdır; '
                                                  'streptokok karın ağrısı yapabilir.',
                                'text': 'Karın ağrısı olduğu için boğaz muayenesini atlayıp hastayı doğrudan apandisit '
                                        'şüphesiyle ameliyata almak'},
                              { 'is_correct': False,
                                'scenario_update': 'Buzlu su boğaz ağrısını şiddetlendirerek çocuğun ağlamasına ve '
                                                   'kusmasına yol açtı.',
                                'teaching_point': 'Boğaz enfeksiyonu olan kusan çocukta zorlayıcı uygunsuz içecekler '
                                                  'aspirasyon riski doğurur.',
                                'text': 'Kusan çocuğa fizik muayene yapmadan acil serviste zorla bir litre buzlu su '
                                        'içirmeye çalışmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Bakteriyel tonsillit tedavi edilmediği için çocukta peritonsiller '
                                                   'apse ve yüksek ateş gelişti.',
                                'teaching_point': 'Okul çağında eksüdatif tonsillit aksi kanıtlanana kadar AGBHS '
                                                  'bakteriyel farenjitidir; kandida değildir.',
                                'text': 'Tonsillerdeki eksüdayı pamukçuk sanarak hiçbir tetkik yapmadan hastaya oral '
                                        'antifungal damla vermek'}],
                 'question': 'Ateş, boğaz ağrısı, karın ağrısı ve kusması olan bu çocukta fizik muayene yaklaşımı '
                             'nasıl olmalıdır?',
                 'stage_title': 'Orofarenks ve Batın Muayenesi Entegrasyonu'},
               { 'options': [ { 'explanation': "Hızlı Antijen Testi (RAT) dakikalar içinde yüksek özgüllükle AGBHS'yi "
                                               'doğrular. Böylece gereksiz batın tetkiklerinden (USG, BT) kaçınılarak '
                                               'hedefe yönelik antibiyotik başlanır.',
                                'is_correct': True,
                                'new_finding': 'Boğaz Sürüntüsü Hızlı Antijen Testi (Strep-A RAT): POZİTİF (+). '
                                               'Laboratuvar: Lökosit 15.200/mm³ (%80 nötrofil), CRP 38 mg/L. Gereksiz '
                                               'batın ultrasonografisi veya tomografisinden kaçınıldı.',
                                'text': 'Tonsillerden sürüntü alarak A grubu streptokok hızlı antijen testi ve '
                                        'gerekirse boğaz kültürü istemek'},
                              { 'is_correct': False,
                                'scenario_update': 'Tomografide sadece reaktif lenfoid doku izlendi; çocuk gereksiz '
                                                   'iyonizan radyasyon aldı.',
                                'teaching_point': 'Basit bir boğaz testiyle aydınlatılacak tablo için batın '
                                                  'tomografisi çekilmesi aşırı ve zararlı tetkiktir.',
                                'text': 'Boğaz sürüntüsü almadan karın ağrısını aydınlatmak için acil kontrastlı tüm '
                                        'batın tomografisi çekmek'},
                              { 'is_correct': False,
                                'scenario_update': 'Tonsilliti olan hastaya yapılan aşırı invaziv girişimler çocukta '
                                                   'derin travma ve enfeksiyon riski yarattı.',
                                'teaching_point': 'Fokal tonsillit bulguları olan çocukta menenjit veya lösemi '
                                                  'araştırması için invaziv ponksiyon endike değildir.',
                                'text': 'Tanıyı doğrulamak için hastadan derhal kemik iliği aspirasyonu ve lomber '
                                        'ponksiyon planlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tedavi edilmeyen streptokok enfeksiyonu 2 hafta sonra akut '
                                                   'romatizmal ateş ve kardite yol açtı.',
                                'teaching_point': 'AGBHS farenjiti ARA profilaksisi için ilk 9 gün içinde uygun '
                                                  'antibiyotikle tedavi edilmelidir.',
                                'text': 'Hiçbir tetkik yapmadan hastayı 1 hafta sonraki kulak burun boğaz '
                                        'polikliniğine yönlendirip göndermek'}],
                 'question': 'Eksüdatif tonsilliti ve karın ağrısı olan bu çocukta tanıyı doğrulamak için en uygun '
                             'tetkik hangisidir?',
                 'stage_title': 'Laboratuvar ve Tetkik Stratejisi'},
               { 'options': [ { 'explanation': 'Eksüdatif tonsillit, servikal lenfadenit, öksürük yokluğu ve pozitif '
                                               'hızlı antijen testi AGBHS farenjiti tanısını kesinleştirir.',
                                'is_correct': True,
                                'new_finding': 'Kesin Tanı: Akut Streptokokal Tonsillofarenjit (Mezenterik Reaktif '
                                               'Karın Ağrısı ile Seyreden).',
                                'text': 'Akut streptokokal tonsillofarenjit enfeksiyonu'},
                              { 'is_correct': False,
                                'scenario_update': 'Batın muayenesinde defans yoktur ve boğazda masif streptokok '
                                                   'enfeksiyonu kanıtlanmıştır; apandisit dışlanmıştır.',
                                'teaching_point': 'Streptokok farenjiti mezenterik lenfadenit üzerinden karın ağrısı '
                                                  'yapar; cerrahi apandisit değildir.',
                                'text': 'Akut cerrahi flegmonöz apandisit'},
                              { 'is_correct': False,
                                'scenario_update': "EBV'de posterior servikal LAP, belirgin splenomegali ve haftalar "
                                                   'süren prodrom olur; Strep-A testi negatif çıkar.',
                                'teaching_point': "EBV'de posterior lenfadenopati ve splenomegali tipiktir; hızlı "
                                                  "Strep-A pozitifliği AGBHS'yi kanıtlar.",
                                'text': 'Enfeksiyöz mononükleoz ebv tablosu'},
                              { 'is_correct': False,
                                'scenario_update': 'Dizanteride kanlı mukuslu ishal ön plandadır; eksüdatif tonsillit '
                                                   've boğaz ağrısı görülmez.',
                                'teaching_point': 'Dizanteri kolondadır; bu hastada enfeksiyon odağı orofarenks ve '
                                                  'tonsillerdir.',
                                'text': 'Akut bakteriyel dizanteri koliti'}],
                 'question': 'Eksüdatif tonsillit, hassas servikal LAP, öksürük yokluğu ve pozitif Strep-A testi ile '
                             'tanınız nedir?',
                 'stage_title': 'Klinik Tanı'},
               { 'options': [ { 'explanation': 'İlk seçenek oral amoksisilindir (50 mg/kg/gün tek doz veya 2 dozda, 10 '
                                               "gün) veya tek doz İM Benzatin Penisilin G'dir. Akut Romatizmal Ateşi "
                                               '(ARA) önlemek için 10 günlük süre tam tamamlanmalıdır. Antibiyotik '
                                               'başlandıktan 24 saat sonra bulaşıcılık sona erer ve çocuk okula '
                                               'dönebilir.',
                                'is_correct': True,
                                'new_finding': 'Oral amoksisilin süspansiyon ve parasetamol başlandı. 24 saat sonra '
                                               'ateşi düştü, yutkunması rahatladı ve mezenterik irritasyona bağlı '
                                               'karın ağrısı ile kusması tamamen kayboldu. Aile 10 günlük kürü '
                                               'tamamladı.',
                                'text': 'Oral amoksisilin tedavisini on gün uygulamak, parasetamol vermek ve yirmi '
                                        'dört saat sonra okula dönebileceğini anlatmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Tedavisi erken kesilen çocukta streptokok eradike edilemedi ve '
                                                   'akut romatizmal ateş karditi gelişti.',
                                'teaching_point': "AGBHS'de antibiyotik süresi semptomlar geçse bile mutlak 10 güne "
                                                  'tamamlanmalıdır (ARA profilaksisi).',
                                'text': 'Ateş düştüğü anda üçüncü günde antibiyotik tedavisini tamamen kesip hastayı '
                                        'ilaçsız bırakmak'},
                              { 'is_correct': False,
                                'scenario_update': 'Aminoglikozid streptokoklara etkisizdir ve çocukta böbrek '
                                                   'fonksiyon bozukluğuna yol açtı.',
                                'teaching_point': 'AGBHS tedavisinde penisilin/amoksisilin altın standarttır; '
                                                  'aminoglikozidler etkisiz ve zararlıdır.',
                                'text': 'Bakterileri öldürmek için hastaya derhal intravenöz yüksek doz nefrotoksik '
                                        'aminoglikozid başlamak'},
                              { 'is_correct': False,
                                'scenario_update': 'Akut enfeksiyon sırasında yapılan acil tonsillektomi masif '
                                                   'kontrolsüz cerrahi kanamaya neden oldu.',
                                'teaching_point': 'Akut farenjit enfeksiyonu esnasında tonsillektomi KONTRENDİKEDİR; '
                                                  'medikal antibiyotikle tedavi edilir.',
                                'text': 'Tonsilliti tedavi etmek amacıyla çocuğu acil serviste derhal ameliyathaneye '
                                        'alıp acil tonsillektomi yapmak'}],
                 'question': 'AGBHS tonsillofarenjiti kesinleşen bu çocuğun tedavisi, bulaşıcılığı ve ARA profilaksisi '
                             'nasıl olmalıdır?',
                 'stage_title': 'Antibiyotik Tedavisi ve ARA Profilaksisi'}]}]
