# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - S21 - S25 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "S21",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "4 Yaş",
        "gender": "Erkek",
        "complaint": "İki gündür düşmeyen 39.5°C yüksek ateş, titreme, nefes alıp verirken sağ böğründe batıcı ağrı ve hızlı soluma",
        "history": "Ailesi 4 yaşındaki (17 kg) erkek çocuğu Sarı Alana getiriyor: 'İki gündür ateşi düşürücülerle bile 39.5°C'den aşağı inmiyor, sürekli titriyor. Bugün sağ yanını tutarak her nefeste canının yandığını söylüyor. Karnı ve göğsü hızla inip kalkıyor, hiçbir şey yemiyor ve sürekli inliyor.' Travma veya aspirasyon öyküsü bulunmuyor.",
        "final_diagnosis": "Akut Tipik Bakteriyel Lober Pnömoni (Streptococcus pneumoniae)",
        "disposition": "Sarı Alanda Nazal Oksijen Desteği + İntravenöz Hidrasyon + İntravenöz Ampisilin (150-200 mg/kg/gün) Tedavisi ile Pediatri Servisine Yatış",
        "case_pearl": "Okul öncesi ve okul çağı çocuklarda ani başlayan yüksek ateş, titreme, plörotik göğüs ağrısı, takipne ve lokalize dinleme bulguları (tübüler solunum sesi, fokal krepitan raller) tipik bakteriyel lober pnömoniyi düşündürür. En sık etken Streptococcus pneumoniae'dir. Hastaneye yatış endikasyonu olan komplike olmayan olgularda ilk tercih parenteral tedavi İV ampisilindir (150-200 mg/kg/gün). Plörotik ağrı çocuklarda sıklıkla batın sağ alt kadrana yansıyarak akut batını taklit edebilir; dikkatli solunum sistemi ve akciğer muayenesi gereksiz cerrahi girişimleri önler.",
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Solunum Desteği",
                "question": "Yüksek ateş, takipne ve sağ tarafta batıcı plörotik göğüs ağrısı ile getirilen 4 yaşındaki çocukta ilk öncelikli yaklaşım ne olmalıdır?",
                "options": [
                    {
                        "text": "Solunum seslerindeki kabalaşmayı ve bronkospazmı gidermek amacıyla acilen yüksek doz nebulize salbutamol ve ipratropiyum bromür inhalasyonu başlatarak yanıtı beklemek",
                        "is_correct": False,
                        "scenario_update": "Uygulanan inhale beta-mimetik sonrası çocuğun kalp tepe atımı 172/dk düzeyine fırladı; takipne, plörotik göğüs ağrısı ve solunum sıkıntısı gerilemedi.",
                        "teaching_point": "Fokal parankimal enfeksiyonlarda hışıltı ve bronkospazm primer patoloji değildir; gereksiz bronkodilatör uygulaması taşikardiyi tetikler ve klinik tabloyu rahatlatmaz."
                    },
                    {
                        "text": "Hastaya nemlendirilmiş oksijen başlamak, kardiyorespiratuar monitörizasyon sağlamak, solunum seslerini ve periferik perfüzyonu dikkatle değerlendirerek damar yolu açmak",
                        "is_correct": True,
                        "explanation": "Takipne, hipoksi ve solunum iş yükü artışı olan febril çocukta ilk basamak oksijen desteği, sürekli monitörizasyon ve solunum sistemi odaklı detaylı fizik muayenedir.",
                        "new_finding": "Vital Bulgular: Ateş 39.5°C, KTA 146/dk, SS 48/dk, SpO2 %91 (oda havasında, oksijenle %98), TA 96/60 mmHg, KDZ 2 sn. Fizik Muayene: Sağ alt zonda belirgin krepitan raller ve tübüler solunum sesi, sağ bazalde submatite, interkostal çekilmeler ve hafif burun kanadı solunumu izlendi."
                    },
                    {
                        "text": "Sağ taraftaki batıcı ağrının akut batın kaynaklı olduğunu düşünerek derhal acil çocuk cerrahisi konsültasyonu istemek ve batın ultrasonografisi çekilmesini planlamak",
                        "is_correct": False,
                        "scenario_update": "Çocuk cerrahisi değerlendirmesinde batında defans saptanmadı; sağ alt zon patolojisinin diyafragma komşuluğu nedeniyle batına yansıyan yalancı akut batın tablosu olduğu belirlendi.",
                        "teaching_point": "Sağ bazal akciğer enfeksiyonları diyafragmatik plevra uyarısıyla çocuklarda akut apandisiti taklit eden yalancı batın ağrısına yol açabilir; öncelikle göğüs muayenesine odaklanılmalıdır."
                    },
                    {
                        "text": "Ateşi düşürmek ve ağrıyı hafifletmek için yüksek doz intramusküler metamizol sodyum enjekte ederek hastayı sakinleşmesi için 30 dakika bekletmek",
                        "is_correct": False,
                        "scenario_update": "İntramusküler enjeksiyon çocuğu aşırı ajite etti, solunum iş yükünü artırdı ve hipoksemiye rağmen oksijen başlanmadığı için satürasyonu %88'e kadar geriledi.",
                        "teaching_point": "Solunum sıkıntısı ve hipoksemisi olan ajite çocukta invaziv kas içi enjeksiyonlar solunum eforunu tüketebilir; öncelik non-invaziv oksijenasyon ve damar yolundan uygun hidrasyondur."
                    }
                ]
            },
            {
                "stage_title": "Radyolojik İnceleme ve Laboratuvar Değerlendirmesi",
                "question": "Fizik muayenesinde sağ alt zonda tübüler solunum sesleri ve raller duyulan bu hastada en uygun tetkik ve görüntüleme yaklaşımı nedir?",
                "options": [
                    {
                        "text": "Hemen ayakta posteroanterior akciğer grafisi çekmek, tam kan sayımı, C-reaktif protein ve kan kültürü örnekleri alarak enfeksiyon belirteçlerini incelemek",
                        "is_correct": True,
                        "image": "assets/images/cxr_lobar_pneumonia.png",
                        "image_caption": "PA Akciğer Grafisi: Sağ alt/orta zonda homojen lober konsolidasyon ve hava bronkogramları",
                        "explanation": "Fokal dinleme bulguları ve plörotik ağrısı olan yüksek ateşli çocukta tanıyı doğrulamak, komplikasyonları dışlamak ve etkeni belirlemek için akciğer grafisi ve kan kültürü endikedir.",
                        "new_finding": "PA Akciğer Grafisi: Sağ hemitoraks orta ve alt zonda homojen radyoopasite artışı ve içerisinde tübüler hava bronkogramları izlendi; sinüsler açık, efüzyon hattı saptanmadı. Laboratuvar: BK 22.400/mm3 (%84 nötrofil, %8 çomak), CRP 168 mg/L, Prokalsitonin 4.2 ng/mL. Kan kültürü alındı."
                    },
                    {
                        "text": "Grafi çekmeden önce akciğer patolojisini ve olası komplikasyonları ekarte etmek amacıyla acilen yüksek çözünürlüklü kontrastlı toraks bilgisayarlı tomografisi istemek",
                        "is_correct": False,
                        "scenario_update": "Toraks BT çekimi hastaya yüksek doz radyasyon maruziyeti getirdi ve klinik yönetimde iki yönlü direkt grafiye kıyasla ek bir cerrahi endikasyon sağlamadı.",
                        "teaching_point": "Pediatrik toplum kaynaklı alt solunum yolu enfeksiyonlarında rutin ilk basamak radyolojik inceleme direkt grafidir; bilgisayarlı tomografi nekrotizan şüphe veya tedaviye yanıtsızlıkta saklanmalıdır."
                    },
                    {
                        "text": "Çocuklarda radyasyon riskinden kaçınmak amacıyla hiçbir görüntüleme yapmadan yalnızca derin trakeal aspirat örneğinden polimeraz zincir reaksiyonu paneli çalışmak",
                        "is_correct": False,
                        "scenario_update": "Görüntüleme yapılmadığı için parankimal tutulumun yaygınlığı ve olası plevral komplikasyonlar netleştirilemedi, viral panel sonuçları ise saatler sonra negatif çıktı.",
                        "teaching_point": "Hastaneye yatış gerektiren fokal muayene bulgulu çocuklarda direkt grafi komplikasyonların dışlanması ve parankim tutulumunun teyidi açısından kılavuzlarca önerilen standart tetkiktir."
                    },
                    {
                        "text": "Enfeksiyon odağını netleştirmek için lomber ponksiyon yaparak beyin omurilik sıvısı incelemek ve eş zamanlı ayrıntılı batın manyetik rezonans görüntülemesi planlamak",
                        "is_correct": False,
                        "scenario_update": "Klinik odağı açıkça akciğer olan hastada yapılan lomber ponksiyon ve MRG tetkikleri çocuğun stresini artırdı, BOS bulguları tamamen normal sonuçlandı.",
                        "teaching_point": "Açık bir fokal solunum muayene bulgusu ve takipnesi olan çocukta santral sinir sistemi ve batın odaklı ileri invaziv tetkikler gereksizdir ve tedaviyi geciktirir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Yüksek ateş, plörotik yan ağrısı, fokal raller ve grafide homojen radyoopak parankim infiltrasyonu olan bu hastada kesin tanı nedir?",
                "options": [
                    {
                        "text": "Atipik Mikoplazma Pnömonisi",
                        "is_correct": False,
                        "scenario_update": "Mikoplazma pnömonisi genellikle okul çağı çocuklarda subakut başlangıçlı, kuru öksürük ve bilateral yamalı interstisiyel infiltrasyonlarla seyreder; bu akut lober tabloya uymaz.",
                        "teaching_point": "Atipik pnömoniler sinsi başlangıç, kuru inatçı öksürük ve yaygın bilateral infiltrasyonla karakterizedir; yüksek ateş, akut lober tutulum ve belirgin lökositoz tipik bakteriyel etkenleri gösterir."
                    },
                    {
                        "text": "Akut Viral Bronşiolit",
                        "is_correct": False,
                        "scenario_update": "Bronşiolit iki yaş altı infantlarda hışıltı ve hiperenflasyonla seyreder; 4 yaşındaki çocukta tek taraflı lober infiltrasyon ve yüksek ateş bronşiolit tablosu değildir.",
                        "teaching_point": "Bronşiolit 2 yaş altı bebeklerin bilateral wheezing ve hiperenflasyonla giden viral tablosudur; 4 yaşındaki çocukta fokal tübüler solunum sesi ve lober opasite bakteriyel parankim enfeksiyonunu işaret eder."
                    },
                    {
                        "text": "Tipik Bakteriyel Lober Pnömoni",
                        "is_correct": True,
                        "explanation": "Ani başlangıçlı yüksek ateş, takipne, tek taraflı plörotik göğüs ağrısı, tübüler solunum sesleri ve grafide segmental/lober homojen dansite artışı Streptococcus pneumoniae kaynaklı tipik bakteriyel lober pnömoninin klasik tablosudur.",
                        "new_finding": "Kesin tanı: Tipik Bakteriyel Lober Pnömoni (Streptococcus pneumoniae). Kan tablosundaki belirgin nötrofilik lökositoz ve yüksek CRP bakteriyel etiyolojiyi doğrulamaktadır."
                    },
                    {
                        "text": "Akut Pulmoner Emboli",
                        "is_correct": False,
                        "scenario_update": "Pulmoner emboli çocuklarda son derece nadir olup altta yatan derin ven trombozu veya hiperkoagülabilite gerektirir; 39.5°C ateş ve lober parankim tutulumunu açıklamaz.",
                        "teaching_point": "Pediatrik yaş grubunda pulmoner emboli risk faktörleri (santral kateter, nefrotik sendrom, malignite) olmaksızın beklenmez ve yüksek ateşle seyreden lober konsolidasyon tablosu oluşturmaz."
                    }
                ]
            },
            {
                "stage_title": "Tedavi, Antibiyoterapi ve Yatış Yönetimi",
                "question": "Tipik lober pnömoni tanısı kesinleşen, takipneik ve hipoksik 4 yaşındaki bu hastada en uygun tedavi ve yatış planı ne olmalıdır?",
                "options": [
                    {
                        "text": "Klinik tablonun viral olabileceğini düşünerek antibiyotik vermeden yalnızca parasetamol şurup ve oral hidrasyon önerisiyle hastayı acil servisten evine taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Tedavisiz evine gönderilen çocuğun ertesi gün solunum sıkıntısı derinleşti, hipoksisi arttı ve parapnömonik komplikasyon gelişerek ambulansla tekrar getirildi.",
                        "teaching_point": "Takipnesi, hipoksemisi ve lober tutulumu olan bakteriyel pnömonili çocukların hastaneye yatırılarak parenteral antibiyotik ve oksijen desteğiyle izlenmesi şarttır."
                    },
                    {
                        "text": "Dirençli suş olasılığı nedeniyle doğrudan intravenöz meropenem ve vankomisin kombinasyonu başlayarak hastayı acilen entübe etmek ve çocuk yoğun bakıma almak",
                        "is_correct": False,
                        "scenario_update": "Gereksiz aşırı geniş spektrumlu antibiyotik ve elektif entübasyon hastada nozokomiyal enfeksiyon riskini artırdı ve yoğun bakım morbiditesine neden oldu.",
                        "teaching_point": "Komplike olmayan toplum kaynaklı pnömonilerde ilk basamakta karbapenem veya vankomisin endikasyonu yoktur; gereksiz entübasyon ve geniş spektrum antibiyotik direnç gelişimine yol açar."
                    },
                    {
                        "text": "Oral yoldan düşük doz amoksisilin 40 mg/kg/gün reçete ederek hastayı Sarı Alanda iki saat izledikten sonra poliklinik kontrolü şartıyla taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Takipneik ve iştahsız çocuk oral ilacı tolere edemedi, yetersiz doz nedeniyle klinik gerileme sağlanamadı ve hipoksemisi derinleşti.",
                        "teaching_point": "Hipoksisi ve solunum iş yükü artışı olan yatan hastalarda parenteral tedavi endikedir; oral tedavide ise pnömokok direnci için yüksek doz (80-90 mg/kg/gün) gereklidir."
                    },
                    {
                        "text": "Hastayı servise yatırarak nazal oksijen sağlamak, hidrasyonu düzenlemek ve intravenöz ampisilin 150-200 mg/kg/gün tedavisini dört eşit dozda başlatmak",
                        "is_correct": True,
                        "explanation": "Hastaneye yatırılan aşılı çocuklarda komplike olmayan toplum kaynaklı tipik bakteriyel pnömonide ilk tercih parenteral antibiyotik yüksek doz İV ampisilindir (150-200 mg/kg/gün).",
                        "new_finding": "Çocuk pediatri servisine yatırıldı. İV ampisilin (50 mg/kg/doz, 6 saatte bir) ve nazal kanülle 2 L/dk nemlendirilmiş oksijen başlandı. Tedavinin 36. saatinde ateş düştü, takipnesi ve solunum sıkıntısı belirgin geriledi."
                    }
                ]
            }
        ]
    },
    {
        "id": "S22",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "6 Yaş",
        "gender": "Kız",
        "complaint": "Üç gündür oral antibiyotik almasına rağmen düşmeyen 39.8°C ateş, nefes darlığı, sol yan ağrısı ve halsizlik",
        "history": "Ailesi 6 yaşındaki (20 kg) kız çocuğu Sarı Alana getiriyor: 'Dört gün önce ateş ve öksürük nedeniyle sağlık ocağında antibiyotik (amoksisilin-klavulanat) başlandı. İlacı düzenli vermemize rağmen ateşi 39.8°C'den düşmüyor. Dünden beri sol yanını tutarak öne eğik oturuyor, nefes alırken inliyor ve göğsü sol tarafta hiç kalkmıyor.' Hasta aşırı soluk ve bitkin görünüyor.",
        "final_diagnosis": "Komplike Parapnömonik Plevral Efüzyon ve Ampiyem (Streptococcus pneumoniae / Staphylococcus aureus)",
        "disposition": "Sarı Alanda Oksijen ve İV Hidrasyon Desteği + Tanısal Torasentez / Tüp Torakostomi (Göğüs Tüpü) ve Genişletilmiş İV Antibiyoterapi İçin Çocuk Cerrahisi / Pediatri Servisine Yatış",
        "case_pearl": "Uygun oral antibiyotik tedavisine rağmen 48-72 saat içinde ateşi düşmeyen, solunum sıkıntısı kötüleşen veya tek taraflı solunum seslerinde ileri derecede azalma ve perküsyonda tahta matitesi saptanan çocuklarda komplike parapnömonik plevral efüzyon ve ampiyem mutlaka düşünülmelidir. Tanıda PA grafi (kostofrenik sinüs küntleşmesi, menisküs belirtisi) ve plevral USG (sıvı miktarı, septasyon, lokülasyon) altın standarttır. Plevral sıvı pH < 7.20, glukoz < 40 mg/dL, LDH > 1000 U/L veya loküle/pürülan sıvı varlığı tüp torakostomi (göğüs tüpü) veya intraplevral fibrinolitik/VATS endikasyonudur. Tedavide plevral drenaj ile birlikte İV 3. kuşak sefalosporin + anti-stafilokoksik (klindamisin veya vankomisin) kombinasyonu uygulanmalıdır.",
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Solunum Muayenesi",
                "question": "Oral antibiyotik altında düşmeyen yüksek ateş, sol yan ağrısı ve takipnesi olan 6 yaşındaki hastada ilk yaklaşım ne olmalıdır?",
                "options": [
                    {
                        "text": "Sol taraftaki solunum sıkıntısını bronkospazma bağlayarak derhal aralıksız yüksek doz nebulize salbutamol vermek ve oral antibiyotiğe devam etmek",
                        "is_correct": False,
                        "scenario_update": "Nebulize bronkodilatör sonrası solunum seslerindeki kayıp ve tahta matitesi değişmedi; hastanın taşikardisi belirginleşti ve solunum yorgunluğu arttı.",
                        "teaching_point": "Tek taraflı solunum sesi kaybı ve perküsyonda matite parankim dışı sıvı birikimi veya atelektaziyi düşündürür; bronkospazm tablosu değildir ve bronkodilatöre yanıt vermez."
                    },
                    {
                        "text": "Ateşin dirençli olmasını viral koinfeksiyona bağlayarak oral oseltamivir başlamak ve herhangi bir ileri tetkik yapmadan evinde dinlenmesini önermek",
                        "is_correct": False,
                        "scenario_update": "Taburcu edilmeye çalışılan hastanın solunum güçlüğü derinleşti, siyanoz gelişti ve solunum arresti riski nedeniyle hasta yakınları panikledi.",
                        "teaching_point": "Antibiyoterapiye rağmen düşmeyen yüksek ateş ve tek taraflı matite ciddi bir akciğer komplikasyonunun göstergesidir; viral enfeksiyon denilerek evine gönderilemez."
                    },
                    {
                        "text": "Hastaya nemlendirilmiş oksijen başlamak, kardiyorespiratuar monitörizasyon sağlamak ve solunum sesleri ile göğüs perküsyonunu karşılaştırmalı olarak dikkatle değerlendirmek",
                        "is_correct": True,
                        "explanation": "Antibiyotik tedavisine yanıtsız persistan ateş ve tek taraflı solunum sıkıntısı olan çocukta öncelik oksijenasyonun sağlanması ve ayrıntılı solunum muayenesidir.",
                        "new_finding": "Vital Bulgular: Ateş 39.8°C, KTA 152/dk, SS 44/dk, SpO2 %91 (oda havasında, maske ile %97), TA 94/58 mmHg, KDZ 2 sn. Fizik Muayene: Sol hemitoraksta solunuma katılım belirgin azalmış, sol orta ve alt zonda solunum sesleri neredeyse hiç duyulmuyor (abolished), perküsyonda belirgin tahta matitesi mevcut; sağ akciğer alanları doğal."
                    },
                    {
                        "text": "Hastada derin ven trombozuna bağlı pulmoner infarktüs düşünerek derhal terapötik doz düşük molekül ağırlıklı heparin başlamak ve izlemek",
                        "is_correct": False,
                        "scenario_update": "Gereksiz antikoagülan başlanması sonrasında olası invaziv torasentez veya göğüs tüpü girişimi öncesinde kanama riski artarak klinik tabloyu riske soktu.",
                        "teaching_point": "Önceden sağlıklı 6 yaşındaki febril çocukta tek taraflı solunum sesi azalması ve matite enfeksiyöz komplikasyonları işaret eder; antikoagülasyon endikasyonu yoktur."
                    }
                ]
            },
            {
                "stage_title": "Radyolojik Görüntüleme ve Plevral Değerlendirme",
                "question": "Sol hemitoraksta solunum sesi kaybı ve tahta matitesi saptanan bu hastada en uygun radyolojik yaklaşım nedir?",
                "options": [
                    {
                        "text": "Görüntüleme yapmadan sol hemitoraksa körlemesine geniş çaplı iğne ile batarak kontrolsüz şekilde sıvıyı aspire etmeye çalışmak",
                        "is_correct": False,
                        "scenario_update": "Ultrason kılavuzluğu olmadan yapılan kör girişim sonucunda akciğer parankimi zedelendi ve yetersiz plevral örnek elde edildi.",
                        "teaching_point": "Çocuklarda plevral sıvı koleksiyonlarına müdahale öncesinde radyolojik teyit ve mümkünse ultrason kılavuzluğu komplikasyonları önlemek açısından şarttır."
                    },
                    {
                        "text": "Hemen ayakta posteroanterior akciğer grafisi çekmek ve sıvı varlığını, septasyonları ve lokülasyonu değerlendirmek için toraks ultrasonografisi planlamak",
                        "is_correct": True,
                        "image": "assets/images/cxr_pleural_effusion.png",
                        "image_caption": "PA Akciğer Grafisi: Sol hemitoraksta kostofrenik sinüs küntleşmesi ve menisküs belirtisi",
                        "explanation": "Tek taraflı solunum sesi kaybı ve matitede direkt grafi tanı koydurucudur; toraks ultrasonografisi ise plevral sıvı miktarını, fibrin bantlarını ve drenaj gerekliliğini gösterir.",
                        "new_finding": "PA Akciğer Grafisi: Sol hemitoraksta kostofrenik ve kardiyofrenik sinüsler tamamen kapalı, diyafragma silinmiş ve lateral göğüs duvarı boyunca yükselen konkav menisküs hattı (radyoopasite) mevcut; mediastende hafif sağa deviasyon izlendi. Toraks USG: Sol plevral boşlukta 35 mm kalınlığında, yoğun fibrin septasyonları ve ekojenik partiküller içeren plevral sıvı koleksiyonu saptandı. Lab: BK 26.800/mm3, CRP 240 mg/L."
                    },
                    {
                        "text": "Akciğer grafisi çekmeden derhal genel anestezi altında acil açık torakotomi ve dekortikasyon planlayarak hastayı doğrudan ameliyathaneye almak",
                        "is_correct": False,
                        "scenario_update": "Öncesinde temel radyolojik değerlendirme ve torasentez yapılmadan ameliyata alınan hastada gereksiz majör cerrahi morbidite ve anestezi riski oluştu.",
                        "teaching_point": "Akciğer enfeksiyonu komplikasyonlarında ilk basamak ameliyat değil; direkt grafi, ultrasonografi ve tüp drenajı veya medikal tedavidir."
                    },
                    {
                        "text": "Sadece boğaz kültürü ve idrarda pnömokok antijeni isteyerek radyolojik tetkik yapmaksızın mevcut oral antibiyotiğin dozunu iki katına çıkarmak",
                        "is_correct": False,
                        "scenario_update": "Radyolojik inceleme geciktirildiği için geniş plevral sıvı koleksiyonu bası yaparak mediasteni daha da itti ve kardiyopulmoner dekompansasyon gelişti.",
                        "teaching_point": "Solunum seslerinin kaybolduğu ve tahta matitesinin alındığı tedaviye dirençli olgularda direkt görüntüleme yapılmaması hayatı tehdit eden gecikmelere yol açar."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Tedaviye dirençli yüksek ateş, sol hemitoraksta solunum sesi kaybı, grafide menisküs hattı ve ultrasonografide septalı plevral sıvı olan hastada tanı nedir?",
                "options": [
                    {
                        "text": "Komplike Parapnömonik Plevral Efüzyon ve Ampiyem",
                        "is_correct": True,
                        "explanation": "Bakteriyel pnömoni tedavisi sırasında gelişen, grafide menisküs belirtisi veren ve ultrasonda fibrin septasyonları ile pürülan koleksiyon gösteren tablo komplike parapnömonik plevral efüzyon ve ampiyemdir.",
                        "new_finding": "Kesin tanı: Komplike Parapnömonik Plevral Efüzyon ve Ampiyem. Plevral boşluktaki lokülasyon ve septasyonlar acil drenaj ihtiyacını doğrulamaktadır."
                    },
                    {
                        "text": "Komplike Olmayan Akut Lober Pnömoni",
                        "is_correct": False,
                        "scenario_update": "Komplike olmayan pnömonide plevral boşlukta loküle sıvı koleksiyonu, menisküs hattı ve solunum seslerinde tam kayıp görülmez.",
                        "teaching_point": "Geniş sıvı birikimi, fibrinöz septasyonlar ve antibiyotiğe dirençli persistan ateş tablonun basit pnömoniden komplike efüzyon/ampiyem evresine ilerlediğini gösterir."
                    },
                    {
                        "text": "Mukus Tıkacına Bağlı Pulmoner Atelektazi",
                        "is_correct": False,
                        "scenario_update": "Atelektazide mediasten lezyon tarafına çekilir; bu hastada ise geniş sıvı basısıyla mediasten karşı tarafa itilmiştir.",
                        "teaching_point": "Atelektazi hacim kaybı yaparak trakea ve mediasteni aynı tarafa çeker; plevral sıvı koleksiyonlarında ise itici kitle etkisiyle mediasten karşı tarafa itilir."
                    },
                    {
                        "text": "Konjenital Sol Diyafragma Hernisi",
                        "is_correct": False,
                        "scenario_update": "Diyafragma hernisinde toraks içinde bağırsak ansları görülür; akut 3 günlük febril seyir ve pürülan plevral koleksiyon oluşturmaz.",
                        "teaching_point": "Geç başlangıçlı diyafragma hernisi toraks içinde hava-sıvı seviyeli bağırsak lupları ile karakterizedir; persistan yüksek ateş ve fibrinli septalı efüzyon ampiyem lehinedir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi, Cerrahi Drenaj ve Servis Yatış Planı",
                "question": "Ultrasonografide septalı kalın plevral koleksiyonu saptanan bu hastada en uygun tedavi ve girişimsel yaklaşım ne olmalıdır?",
                "options": [
                    {
                        "text": "Göğüs tüpü takmadan yalnızca oral amoksisilin dozunu artırmak ve hastayı evde buhar banyosu ile günlük poliklinik kontrolüne çağırmak",
                        "is_correct": False,
                        "scenario_update": "Drenaj uygulanmayan pürülan ampiyem hızla organize oldu, akciğer parankiminde hapsolma (trapped lung) ve ciddi restriktif solunum yetmezliği gelişti.",
                        "teaching_point": "pH < 7.20, glukoz < 40 mg/dL veya pürülan/septalı olan plevral koleksiyonlar cerrahi drenaj olmaksızın medikal tedaviyle gerilemez; gecikme kalıcı fibrotoraks yaratır."
                    },
                    {
                        "text": "Herhangi bir antibiyotik tedavisi vermeden yalnızca plevral boşluğa yüksek doz kortikosteroid enjekte etmek ve hastayı genel pediatri servisinde izlemek",
                        "is_correct": False,
                        "scenario_update": "Bakteriyel enfeksiyon zemininde lokal steroid enjeksiyonu ampiyemin hızla yayılmasına, bakteremiye ve septik şok tablosuna yol açtı.",
                        "teaching_point": "Bakteriyel plevral ampiyemde intraplevral kortikosteroid uygulaması kontrendikedir; tedavi uygun antibiyoterapi ve mekanik/fibrinolitik drenajdır."
                    },
                    {
                        "text": "Tanısal torasentez ve tüp torakostomiyle sıvıyı drene etmek, intravenöz seftriakson ve klindamisin başlayıp çocuk cerrahisi servisine yatırmak",
                        "is_correct": True,
                        "explanation": "Komplike parapnömonik efüzyon ve ampiyemde plevral sıvının drenajı (göğüs tüpü veya VATS) ve genişlemiş spektrumlu parenteral antibiyoterapi (3. kuşak sefalosporin + antistafilokoksik) temel tedavidir.",
                        "new_finding": "Göğüs tüpü takılarak 350 mL pürülan plevral sıvı drene edildi. Plevral Sıvı Analizi: pH 7.08, Glukoz 22 mg/dL, LDH 2850 U/L, lökosit 65.000/mm3 (ampiyem ile uyumlu). İV seftriakson (100 mg/kg/gün) ve klindamisin (40 mg/kg/gün) başlandı."
                    },
                    {
                        "text": "Sıvı örneği almadan hastaya acilen sol tam akciğer rezeksiyonu uygulamak ve ameliyat sonrasında ampirik geniş spektrumlu antitüberküloz tedavisi başlatmak",
                        "is_correct": False,
                        "scenario_update": "Gereksiz radikal rezeksiyon hastada geri dönüşsüz solunum kapasitesi kaybına ve tüberküloz ilaçlarına bağlı toksisiteye neden oldu.",
                        "teaching_point": "Parapnömonik ampiyemde akciğer dokusu rezeke edilmez; amaç plevral drenaj ve antibiyotikle enfeksiyonu temizleyip akciğerin yeniden ekspanse olmasını sağlamaktır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S23",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "15 Yaş",
        "gender": "Erkek",
        "complaint": "İstirahat halindeyken aniden başlayan şiddetli sağ taraflı batıcı göğüs ağrısı ve nefes darlığı",
        "history": "15 yaşında (182 cm, 54 kg - uzun boylu, zayıf, astenik yapıda) erkek hasta Sarı Alana getiriliyor: 'Evde bilgisayar başında ders çalışırken hiçbir darbe veya zorlanma olmadan aniden sağ göğsüme bir bıçak saplandı gibi oldu. Derin nefes almaya çalıştığımda sağ tarafım çok şiddetli batıyor ve nefesim yetmiyor.' Özgeçmişinde astım, travma veya sigara öyküsü bulunmuyor.",
        "final_diagnosis": "Primer Spontan Pnömotoraks (PSP - Subplevral Bleb Rüptürü)",
        "disposition": "Sarı Alanda Yüksek Akımlı (%100) Geri Solumasız Maske ile Oksijen Desteği + Toraks Cerrahisi Konsültasyonu ve Tüp Torakostomi (Göğüs Tüpü) İçin Yatış",
        "case_pearl": "Primer spontan pnömotoraks (PSP), altta yatan belirgin bir akciğer hastalığı veya travma olmaksızın, genellikle uzun boylu ve zayıf adölesan erkeklerde apikal subplevral bül/bleblerin rüptürü sonucu gelişir. Ani başlangıçlı plörotik göğüs ağrısı ve dispne tipiktir. Fizik muayenede etkilenen tarafta solunum seslerinde azalma/kayıp ve perküsyonda hipersonorite (timpanik ses) saptanır. Ayakta ekspiryum PA akciğer grafisinde visseral plevra hattı ve periferik damarlanma kaybı tanıyı kesinleştirir. Hipotansiyon, juguler venöz dolgunluk ve trakeal deviasyon gelişirse derhal tansiyon pnömotoraks düşünülüp 2. interkostal aralık midklavikuler hattan veya 4-5. İKA ön aksiller hattan acil iğne dekompresyonu yapılmalıdır. Semptomatik veya geniş PSP olgularında yüksek akımlı oksijen (%100 O2, plevral havanın rezorpsiyonunu 4-6 kat hızlandırır) ve tüp torakostomi uygulanır.",
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Fizik Muayene",
                "question": "İstirahat halindeyken ani batıcı göğüs ağrısı ve nefes darlığı gelişen 15 yaşındaki astenik yapılı hastada ilk yaklaşım ne olmalıdır?",
                "options": [
                    {
                        "text": "Hastaya rezervuarlı maskeyle yüksek akımlı oksijen başlamak, kardiyopulmoner monitörizasyon sağlamak, solunum seslerini ve trakea pozisyonunu değerlendirmek",
                        "is_correct": True,
                        "explanation": "Ani başlayan plörotik göğüs ağrısı ve dispnede ilk öncelik oksijen desteği, hemodinaminin değerlendirilmesi ve tansiyon bulgularının (trakeal deviasyon, hipotansiyon) dışlanmasıdır.",
                        "new_finding": "Vital Bulgular: KTA 118/dk, SS 28/dk, SpO2 %92 (oda havasında, rezervuarlı maske ile %99), TA 116/74 mmHg. Fizik Muayene: Sağ hemitoraksta solunuma katılım belirgin azalmış, oskültasyonda sağda solunum sesleri apikal ve bazalde tamamen kaybolmuş, perküsyonda sağ hemitoraksta belirgin hipersonorite (timpanik ses) mevcut; trakea orta hatta, boyun venöz dolgunluğu yok."
                    },
                    {
                        "text": "Ağrının kas spazmı kaynaklı olduğunu düşünerek yalnızca intramusküler diklofenak enjekte etmek ve hastayı sedyede dinlendirerek evine göndermek",
                        "is_correct": False,
                        "scenario_update": "Analjezik sonrası göğüs ağrısı hafiflese de hastanın solunum sıkıntısı sürdü; fizik muayene yapılmadığı için tek taraflı patoloji gözden kaçtı.",
                        "teaching_point": "Ani başlayan şiddetli göğüs ağrısı ve dispnede kas spazmı tanısı ancak hayatı tehdit eden torakal patolojiler dışlandıktan sonra konulabilir."
                    },
                    {
                        "text": "Akut bronkospazm atağı düşünerek hastaya derhal aralıksız yüksek doz nebulize salbutamol başlamak ve ardından klinik yanıtı beklemek",
                        "is_correct": False,
                        "scenario_update": "Nebulize tedavi sonrası hastanın taşikardisi arttı; tek taraflı ses kaybı ve belirgin perküsyon timpanizmi bronkodilatör ile gerilemedi.",
                        "teaching_point": "Bronkospazm bilateral hışıltı ve ekspiryum uzamasıyla seyreder; tek taraflı ani ses kaybı ve timpanik ses hava yolu daralmasıyla açıklanamaz."
                    },
                    {
                        "text": "Akut koroner sendrom ön tanısıyla hastaya hemen çiğnetme şeklinde asetilsalisilik asit vermek ve sublingual nitrogliserin uygulayarak izlemek",
                        "is_correct": False,
                        "scenario_update": "Verilen sublingual nitrogliserin hastada şiddetli baş ağrısı ve hipotansiyona yol açtı; tek taraflı solunum bulguları değişmedi.",
                        "teaching_point": "15 yaşındaki önceden sağlıklı adölesanda ani tek taraflı batıcı ağrıda koroner iskemi beklenmez; vazodilatatörler hipotansiyona yol açarak tabloyu ağırlaştırabilir."
                    }
                ]
            },
            {
                "stage_title": "Radyolojik İnceleme ve Plevral Değerlendirme",
                "question": "Sağda solunum sesleri kaybolan ve perküsyonda hipersonorite saptanan bu hastada en uygun radyolojik inceleme hangisidir?",
                "options": [
                    {
                        "text": "Tanıyı doğrulamak amacıyla zaman kaybettiren yüksek doz kontrastlı tüm vücut bilgisayarlı tomografisi ve kardiyak koroner anjiyografi planlamak",
                        "is_correct": False,
                        "scenario_update": "Acil toraks patolojisi varken hastanın BT ünitesine transferi sırasında takipnesi arttı ve hemodinamik dekompansasyon riski yaşandı.",
                        "teaching_point": "Stabil adölesanda plevral serbest havanın tespitinde iki yönlü akciğer grafisi yeterlidir; gereksiz anjiyografi ve tüm vücut BT zaman kaybettirir."
                    },
                    {
                        "text": "Grafi çekmeden önce solunum kapasitesini ölçmek amacıyla hastaya zorlu ekspirasyon gerektiren spirometrik solunum fonksiyon testi yaptırmak",
                        "is_correct": False,
                        "scenario_update": "Zorlu ekspirasyon ve spirometri manevrası sırasında plevral bası aniden arttı, parankim hava kaçağı genişledi ve solunum sıkıntısı derinleşti.",
                        "teaching_point": "Plevral hava kaçağı şüphesinde zorlu ekspiratuar solunum testleri kesinlikle kontrendikedir; intratorasik basıncı artırarak kaçak alanını büyütebilir."
                    },
                    {
                        "text": "Radyolojik inceleme yapmadan derhal sağ ikinci interkostal aralık midklavikuler hattan acil kör iğne torakostomi uygulayarak doğrudan plevraya girmek",
                        "is_correct": False,
                        "scenario_update": "Hemodinamisi stabil ve trakeası orta hatta olan hastaya kontrolsüz acil iğne batırılması sağlıklı akciğer parankimine iatrojenik hasar verdi.",
                        "teaching_point": "Tansiyon bulgusu (hipotansiyon, şok, trakeal deviasyon) olmayan stabil hastalarda ampirik kör iğne dekompresyonu yapılmaz; önce grafi çekilmelidir."
                    },
                    {
                        "text": "Ayakta ekspiryum posteroanterior akciğer grafisi çekerek plevral hava birikimini ve parankim kollapsını radyolojik olarak incelemek",
                        "is_correct": True,
                        "image": "assets/images/cxr_pneumothorax.png",
                        "image_caption": "PA Akciğer Grafisi: Sağda visseral plevra çizgisi ve apikalde damarlanma kaybı",
                        "explanation": "Akut tek taraflı solunum sesi kaybı ve hipersonorite varlığında ayakta ekspiryum PA akciğer grafisi plevral boşluktaki serbest havanın ve sınır hattının görüntülenmesinde altın standarttır.",
                        "new_finding": "PA Akciğer Grafisi: Sağ hemitoraks apeksinde ve lateralinde parankim damar gölgelerinin aniden sonlandığı lüsent ve avasküler serbest hava sahası, akciğer dokusunun hilusa doğru kollabe olduğu sınır hattı izlendi; mediastende ve trakeada belirgin bir deviasyon saptanmadı."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Uzun boylu astenik yapıda, istirahatte ani göğüs ağrısı başlayan ve grafide serbest hava hattı görülen hastada kesin tanı nedir?",
                "options": [
                    {
                        "text": "Akut Kostokondrit Sendromu",
                        "is_correct": False,
                        "scenario_update": "Kostokondritte kostosternal eklemlerde lokalize palpasyon hassasiyeti olur; solunum sesi kaybı ve grafide plevral serbest hava görülmez.",
                        "teaching_point": "Kostokondrit palpasyonla artan göğüs ön duvarı hassasiyeti ile giden kas-iskelet patolojisidir; akciğer grafisi ve solunum sesleri tamamen normaldir."
                    },
                    {
                        "text": "Primer Spontan Pnömotoraks",
                        "is_correct": True,
                        "explanation": "Altta yatan akciğer hastalığı veya travma olmaksızın, uzun boylu astenik gençlerde apikal subplevral bleb rüptürüne bağlı gelişen hava kaçağı primer spontan pnömotorakstır.",
                        "new_finding": "Kesin tanı: Primer Spontan Pnömotoraks (PSP). Apikal subplevral bleb rüptürü kaynaklı plevral hava birikimi teyit edildi."
                    },
                    {
                        "text": "Akut Miyoperikardit Atağı",
                        "is_correct": False,
                        "scenario_update": "Miyoperikarditte EKG'de yaygın ST elevasyonları ve troponin yüksekliği beklenir; tek taraflı solunum sesi kaybı ve plevral hava oluşmaz.",
                        "teaching_point": "Miyoperikardit kardiyak enzim yüksekliği, sürtünme sesi ve EKG değişiklikleri ile seyreder; plevral hava kaçağı ve tek taraflı timpanizm yapmaz."
                    },
                    {
                        "text": "Akut Pulmoner Tromboemboli",
                        "is_correct": False,
                        "scenario_update": "Pulmoner embolide grafi çoğunlukla normaldir veya kama şeklinde opasite görülür; avasküler plevral hava sahası emboli bulgusu değildir.",
                        "teaching_point": "Pulmoner emboli risk faktörü olan hastalarda hipoksi ve taşikardi ile seyreder; plevral boşlukta geniş avasküler hava birikimi oluşturmaz."
                    }
                ]
            },
            {
                "stage_title": "Tedavi, Cerrahi Konsültasyon ve Girişim Planı",
                "question": "Akciğer grafisinde belirgin hava kaçağı ve dispnesi olan bu primer spontan pnömotoraks olgusunda en uygun tedavi yaklaşımı nedir?",
                "options": [
                    {
                        "text": "Yüksek akımlı oksijen başlamak, toraks cerrahisi konsültasyonuyla tüp torakostomi uygulayarak hastayı kapalı su altı drenajına bağlamak",
                        "is_correct": True,
                        "explanation": "Semptomatik veya geniş plevral hava kaçağında yüksek akımlı (%100) oksijen rezorpsiyon hızını 4-6 kat artırır; göğüs tüpü takılması akciğerin re-ekspansiyonunu sağlar.",
                        "new_finding": "Toraks cerrahisi tarafından sağ 5. interkostal aralık orta aksiller hattan küçük çaplı göğüs tüpü yerleştirildi ve su altı drenajına bağlandı. Aktif hava çıkışı izlendi. Hastanın dispnesi hızla geriledi, SpO2 %99'a yükseldi. Kontrol grafisinde akciğer parankimi tam olarak ekspanse oldu."
                    },
                    {
                        "text": "Hiçbir oksijen veya girişim uygulamadan yalnızca oral parasetamol reçete ederek hastayı ertesi gün poliklinik kontrolüne göndermek",
                        "is_correct": False,
                        "scenario_update": "Tedavisiz evine gönderilen hastada hava kaçağının ilerlemesi sonucu gece saatlerinde tansiyon tablosu ve kardiyorespiratuar kollaps gelişti.",
                        "teaching_point": "Belirgin semptomatik ve geniş plevral hava birikimi olan adölesanlar taburcu edilemez; acil drenaj ve yakın klinik takip gerektirir."
                    },
                    {
                        "text": "Plevral havanın hızla dağılması amacıyla hastayı derhal acil pozitif basınçlı mekanik ventilasyon desteğine bağlayarak entübe etmek",
                        "is_correct": False,
                        "scenario_update": "Göğüs tüpü takılmadan uygulanan pozitif basınçlı ventilasyon plevral boşluğa hava girişini katlayarak ani kardiyak arresti tetikledi.",
                        "teaching_point": "Drene edilmemiş plevral hava kaçağında pozitif basınçlı ventilasyon uygulanması mortal tansiyon tablosunu tetikleyen kritik bir tıbbi hatadır."
                    },
                    {
                        "text": "Acil açık torakotomi ve lobektomi planlayarak hastayı ilk spontan atakta doğrudan genel anestezi altında cerrahi ameliyathaneye hızla almak",
                        "is_correct": False,
                        "scenario_update": "İlk atakta doğrudan açık majör cerrahi rezeksiyon uygulanması hastada gereksiz ameliyat morbiditesi ve uzamış hastane yatışına yol açtı.",
                        "teaching_point": "İlk atak spontan olgularda ilk tercih göğüs tüpü veya kateter aspirasyonudur; cerrahi (VATS/blebektomi) nüks veya persistan kaçakta endikedir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S24",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "8 Yaş",
        "gender": "Kız",
        "complaint": "40.2°C inatçı yüksek ateş, tüm vücutta güneş yanığı benzeri yaygın döküntü, kusma, tansiyon düşüklüğü ve baygınlık hissi",
        "history": "Ailesi 8 yaşındaki (25 kg) kız çocuğu acil Sarı Alana getiriyor: 'İki gün önce hafif boğaz ağrısı ve burun akıntısı vardı. Dün ateşi 40.2°C'ye fırladı, ardından tüm vücudu sanki güneşte kalmış gibi kıpkırmızı oldu. Bugün sürekli kusuyor, sulu ishal oldu, ayakta duramıyor, gözleri kan çanağı gibi ve dili kıpkırmızı kabardı.' Çocuğun bilinci uykulu ve yanıtlara güçlükle odaklanıyor.",
        "final_diagnosis": "Stafilokoksik Toksik Şok Sendromu (TŞS / TSS - TSST-1 Aracılı Süperantijenik Sepsis Tablosu)",
        "disposition": "Sarı Alanda Agresif İntravenöz Kristaloid Sıvı Resüsitasyonu (20 mL/kg boluslar) + İntravenöz Vankomisin ve Klindamisin Tedavisi ile Çocuk Yoğun Bakım Ünitesine (ÇYBÜ) Acil Yatış",
        "case_pearl": "Toksik Şok Sendromu (TŞS), Staphylococcus aureus (TSST-1, enterotoksinler) veya Streptococcus pyogenes (pirojenik ekzotoksinler) süperantijenlerinin T lenfositlerin %20'den fazlasını non-spesifik aktive ederek kontrolsüz masif sitokin fırtınasına yol açtığı yaşamı tehdit eden bir sendromdur. Klasik tanı kriterleri: >38.9°C ateş, diffüz maküler eritrodermi (güneş yanığı benzeri döküntü, 1-2 hafta sonra el-ayak parmaklarında deskuamasyonla sonuçlanır), hipotansiyon ve en az 3 organ sistemi tutulumudur (GİS: kusma/ishal, mukoza: konjonktival hiperemi/çilek dili, renal, hepatik, hematolojik, SSS). Acil yönetimde ilk basamak agresif izotonik sıvı resüsitasyonudur (şok tablosunda tekrarlayan 20 mL/kg boluslar). Antimikrobiyal tedavide hücre duvarına etkili antibiyotiğe (vankomisin/seftriakson) ek olarak ribosomal protein ve toksin sentezini hızla durduran KLİNDAMİSİN (Eagle etkisi/toksin inhibisyonu) mutlaka eklenmeli ve hasta Çocuk Yoğun Bakım Ünitesinde izlenmelidir.",
        "steps": [
            {
                "stage_title": "Sarı Alanda Acil Hemodinamik Değerlendirme ve Resüsitasyon",
                "question": "40.2°C ateş, yaygın eritrodermi ve kan basıncı 70/40 mmHg olan 25 kg ağırlığındaki çocukta ilk basamak acil müdahale ne olmalıdır?",
                "options": [
                    {
                        "text": "Hipotansiyonu düzeltmek amacıyla sıvı vermeden önce hastaya derhal yüksek doz oral antihipertansif ilaç içirmeye çalışarak klinik yanıtı beklemek",
                        "is_correct": False,
                        "scenario_update": "Zaten derin hipotansiyonda olan hastada antihipertansif verilmesi vasküler tonusu tamamen çökertti ve kardiyovasküler kollapsı tetikledi.",
                        "teaching_point": "Hipotansif şok tablosundaki hastaya vazodilatatör veya antihipertansif verilmesi ölümcül bir hatadır; öncelik damar içi volümün kristaloidle hızla doldurulmasıdır."
                    },
                    {
                        "text": "Yalnızca soğuk uygulama ve oral parasetamol şurup vererek hastayı vital monitörizasyon yapmaksızın yeşil alan gözlem odasında beklemeye almak",
                        "is_correct": False,
                        "scenario_update": "Damar yolu açılmayan ve sıvı resüsitasyonu geciken çocukta kapiller dolum 5 saniyeye uzadı, periferik nabızlar palpe edilemez hale geldi.",
                        "teaching_point": "Hipotansiyon, taşikardi ve letarji septik şok bulgularıdır; oral antipiretik ve bekleme yaklaşımı hastanın ölümüne neden olabilir."
                    },
                    {
                        "text": "Ciltteki yaygın kızarıklığı kontakt alerji kabul ederek yalnızca tek doz subkutan antihistaminik uygulayıp hastayı poliklinik kontrolüyle evine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Alerji sanılarak evine gönderilmeye çalışılan çocuk Sarı Alan kapısında senkop geçirdi, kardiyojenik ve distributif şok tablosu ağırlaştı.",
                        "teaching_point": "Yüksek ateş, mukozal hiperemi ve hipotansiyonla seyreden eritrodermi sistemik enfeksiyöz şok tablosudur; basit alerjik döküntü kabul edilemez."
                    },
                    {
                        "text": "Geniş damar yolu açarak 20 mL/kg izotonik sodyum klorür bolusu başlatmak, oksijen vermek ve kardiyovasküler monitörizasyon sağlamak",
                        "is_correct": True,
                        "explanation": "Ağır hipotansiyon ve hipoperfüzyon bulguları olan septik hemodinamik tabloda ilk öncelik havayolu-oksijenasyon ve 20 mL/kg izotonik kristaloid sıvı resüsitasyonudur.",
                        "new_finding": "Vital Bulgular: Ateş 40.2°C, KTA 162/dk, SS 36/dk, TA 70/40 mmHg (ağır hipotansiyon), SpO2 %94, KDZ 4 saniye, periferik nabızlar filiform. Fizik Muayene: Tüm vücutta yaygın diffüz maküler eritem (güneş yanığı görünümü), bilateral eksüdasız konjonktival hiperemi, orofarenkste hiperemi ve belirgin çilek dili görünümü; bilinç letarjik, oryantasyon bozuk. 500 mL %0.9 NaCl sonrası TA 82/48 mmHg oldu."
                    }
                ]
            },
            {
                "stage_title": "İleri Laboratuvar ve Çoklu Organ Değerlendirmesi",
                "question": "Sıvı resüsitasyonu sürdürülen, yüksek ateşi ve diffüz eritrodermisi olan bu çocukta laboratuvar ve tetkik planı ne olmalıdır?",
                "options": [
                    {
                        "text": "Organ disfonksiyonunu değerlendirmeksizin yalnızca parmak ucu glukoz ölçümü yapıp hastayı başka hiçbir laboratuvar tetkiki istemeden derhal taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Laboratuvar tetkikleri yapılmadığı için hastanın ağır laktik asidozu, akut böbrek yetmezliği ve koagülopatisi saptanamadı ve arrest gelişti.",
                        "teaching_point": "Hipotansif ve yüksek febril çocuklarda çoklu organ yetmezliği parametreleri değerlendirilmeden taburculuk kararı verilmesi ölümcül ihmaldir."
                    },
                    {
                        "text": "Sadece gıda alerjisi paneli ve spesifik IgE antikorları isteyerek hastanın tüm sonuçlarını ayaktan alerji polikliniğinde değerlendirmeyi planlamak",
                        "is_correct": False,
                        "scenario_update": "Spesifik IgE sonuçları günler sonra çıkacağı için hastanın fulminan sepsisi ve organ disfonksiyonu tanısız kaldı.",
                        "teaching_point": "Akut septik ve eritrodermik tablolar acil yoğun bakım patolojisidir; ayaktan poliklinik alerji tetkiklerinin bu aşamada yeri yoktur."
                    },
                    {
                        "text": "Tam kan, kan gazı, biyokimya, koagülasyon paneli, kreatin kinaz incelemek ve kan, boğaz, idrar kültürleri göndermek",
                        "is_correct": True,
                        "explanation": "Süperantijen aracılı sistemik inflamatuar yanıtta çoklu organ yetmezliğinin (böbrek, karaciğer, kas, hematolojik, metabolik asidoz) tespiti ve mikrobiyolojik odak araştırması şarttır.",
                        "new_finding": "Laboratuvar Bulguları: BK 28.400/mm3 (%88 nötrofil, %12 bant formu), Trombosit 84.000/mm3 (trombositopeni), CRP 260 mg/L, Prokalsitonin 28 ng/mL. Biyokimya: Üre 78 mg/dL, Kreatinin 1.8 mg/dL (akut böbrek hasarı), AST 184 U/L, ALT 165 U/L, Total Bilirubin 2.4 mg/dL. Kreatin kinaz (CK) 890 U/L. Kan Gazı: pH 7.24, HCO3 14 mmol/L, Laktat 4.8 mmol/L. Boğaz sürüntüsünde ve kanda Gram-pozitif koklar üremesi için kültürler gönderildi."
                    },
                    {
                        "text": "Hiçbir kan tetkiki yapmadan yalnızca tüm vücut manyetik rezonans görüntülemesi planlayarak hastayı iki saatlik radyoloji çekimine göndermek",
                        "is_correct": False,
                        "scenario_update": "Kararsız hemodinamisi olan çocuk MRG odasında monitörsüz kaldı; hipotansiyonu derinleşti ve acil resüsitasyon gerekti.",
                        "teaching_point": "Hemodinamik instabilitesi olan septik çocuklarda acil resüsitasyon tamamlanmadan ve organ fonksiyonları belirlenmeden uzun süreli görüntülemeye gönderilmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Yüksek ateş, hipotansiyon, diffüz eritrodermi, çilek dili ve çoklu organ yetmezliği (renal, hepatik, hematolojik) tablosunun tanısı nedir?",
                "options": [
                    {
                        "text": "Klasik Kawasaki Hastalığı",
                        "is_correct": False,
                        "scenario_update": "Kawasaki hastalığında en az 5 gün inatçı ateş, lenfadenopati ve ekstremite değişiklikleri görülür; ilk 48 saatte dekompanse hipotansif şok oluşturmaz.",
                        "teaching_point": "Kawasaki hastalığı tipik olarak en az 5 günlük ateş gerektirir ve nadiren erken şok yapar; akut başlangıçlı ağır hipotansiyon ve çoklu organ yetmezliği TŞS'yi gösterir."
                    },
                    {
                        "text": "Akut Fulminan Meningokoksemi",
                        "is_correct": False,
                        "scenario_update": "Meningokoksemide tipik olarak hızla birleşen purpurik ve ekimotik döküntüler (purpura fulminans) görülür; yaygın güneş yanığı benzeri eritrodermi görülmez.",
                        "teaching_point": "Meningokoksemi peteşiyal ve nekrotik purpurik lezyonlarla seyreder; diffüz güneşte yanmış gibi basmakla solan maküler eritem ve çilek dili TŞS lehinedir."
                    },
                    {
                        "text": "Komplike Olmayan Kızıl",
                        "is_correct": False,
                        "scenario_update": "Kızılda çilek dili ve zımpara kağıdı benzeri döküntü olabilir ancak dekompanse hipotansiyon, çoklu organ yetmezliği ve şok tablosu gelişmez.",
                        "teaching_point": "Kızıl hafif-orta seyirli streptokoksik bir toksin tablosudur; organ yetmezliği, koagülopati ve hipotansif şok geliştiğinde tablo artık TŞS olarak adlandırılır."
                    },
                    {
                        "text": "Toksik Şok Sendromu",
                        "is_correct": True,
                        "explanation": "Yüksek ateş (>38.9°C), diffüz maküler eritrodermi, hipotansiyon ve en az üç organ sistemi tutulumu (GİS, mukoza hiperemisi/çilek dili, renal, hepatik, hematolojik) klasik Toksik Şok Sendromu tanı kriterlerini tam olarak karşılar.",
                        "new_finding": "Kesin tanı: Stafilokoksik Toksik Şok Sendromu (TŞS). Süperantijen salınımına bağlı ağır kapiller kaçak ve distributif şok doğrulanmıştır."
                    }
                ]
            },
            {
                "stage_title": "Antimikrobiyal Tedavi ve Yoğun Bakım Planı",
                "question": "Toksik şok sendromu ve distributif şok tablosundaki bu hastada en uygun antimikrobiyal rejim ve yatış kararı ne olmalıdır?",
                "options": [
                    {
                        "text": "Yalnızca oral amoksisilin şurup reçete ederek hastayı servise bile yatırmadan acil servis yeşil alandan evine taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Yoğun bakıma alınmayan ve parenteral tedavi verilmeyen hasta ev yolunda kardiyopulmoner arrest geçirerek acile geri döndü.",
                        "teaching_point": "TŞS ve septik şok tablosundaki çocukların Çocuk Yoğun Bakım Ünitesine yatırılması ve acil kombine parenteral antibiyotik alması zorunludur."
                    },
                    {
                        "text": "İntravenöz vankomisin ve toksin üretimini baskılamak için klindamisin başlayarak hastayı acilen çocuk yoğun bakım ünitesine yatırmak",
                        "is_correct": True,
                        "explanation": "TŞS tedavisinde hücre duvarına etkili antibiyotiğe (vankomisin) ek olarak, Eagle etkisini kırıp protein ve süperantijen toksin üretimini ribozomal düzeyde baskılayan klindamisin esastır; hasta ÇYBÜ'de izlenmelidir.",
                        "new_finding": "Hasta Çocuk Yoğun Bakım Ünitesine (ÇYBÜ) kabul edildi. İntravenöz vankomisin (60 mg/kg/gün) ve klindamisin (40 mg/kg/gün, 3 doza bölünerek) başlandı. İkinci 20 mL/kg kristaloid bolusu ve santral venöz kateterizasyon uygulandı; noradrenalin infüzyonu ile hemodinamik stabilite sağlandı."
                    },
                    {
                        "text": "Klindamisin eklemeden yalnızca tek başına sefazolin başlamak ve hastayı monitörizasyon yapmaksızın normal cerrahi servis yatağına transfer etmek",
                        "is_correct": False,
                        "scenario_update": "Sadece hücre duvarı antibiyotiği verilmesi toksin sentezini durduramadı; süperantijenik fırtına devam etti ve organ yetmezliği derinleşti.",
                        "teaching_point": "TŞS'de tek başına hücre duvarı inhibitörleri yetersizdir; klindamisin süperantijen ve ekzotoksin sentezini hızla kapatan hayat kurtarıcı ikinci ajandır."
                    },
                    {
                        "text": "Tüm antibiyotikleri keserek hastaya yalnızca yüksek doz oral asetilsalisilik asit vermek ve standart kardiyoloji servisinde izlemek",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik kesilmesi üzerine bakteremi ve kontrolsüz toksin salınımı katlandı, trombositopenik hastada gastrointestinal kanama gelişti.",
                        "teaching_point": "TŞS bakteriyel toksin aracılı akut bir şoktur; antibiyoterapi kesilemez ve yüksek doz aspirin Reye sendromu ile kanama riskini artırır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S25",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "14 Aylık",
        "gender": "Erkek",
        "complaint": "Ağız çevresi ve bez bölgesinden başlayıp tüm vücuda yayılan parlak kızarıklık, cilde dokunmakla çığlık atarak ağlama ve deride soyulmalar",
        "history": "Ailesi 14 aylık (10 kg) erkek bebeği Sarı Alana getiriyor: 'Üç gün önce hafif burun akıntısı ve huysuzluğu vardı. Dün ağzının kenarında kabuklanma ve boynunda kızarıklık başladı. Bugün ise bütün vücudu kıpkırmızı oldu; bezini değiştirirken veya kucağımıza alırken derisine hafifçe dokunsak bile canı çok yanıyor gibi çığlık çığlığa ağlıyor. Kollarında ve göbeğinde ince su dolu kabarcıklar patladı ve derisi çarşaf gibi soyulmaya başladı.' Bebeğin ateşi 38.4°C ölçülmüş.",
        "final_diagnosis": "Stafilokoksik Haşlanmış Deri Sendromu (SSSS / Ritter Hastalığı - Eksfolyatif Toksin A ve B Aracılı Büllöz Epidermolizis)",
        "disposition": "Sarı Alanda Damar Yolu + İntravenöz Kristaloid Hidrasyonu + İntravenöz Antistafilokoksik Antibiyoterapi (Sefazolin / Nafsilin veya Vankomisin) + Steril Parafinli Nemlendirici Pansuman ile Pediatri Servisine Yatış",
        "case_pearl": "Stafilokoksik Haşlanmış Deri Sendromu (SSSS / Ritter Hastalığı), genellikle yenidoğan ve <5 yaş çocuklarda Staphylococcus aureus suşlarının ürettiği eksfolyatif toksinlerin (ET-A, ET-B) kan yoluyla yayılıp epidermis stratum granulosum tabakasındaki dezmoglein-1 proteinini parçalamasıyla gelişen büllöz bir tablodur. Toksin böbreklerden atıldığı için renal fonksiyonları immatür olan süt çocuklarında sık görülür. Karakteristik özellikleri: perioral/fleksural eritem, perioral radyal fissür ve kabuklanmalar, aşırı kutanöz hiperestezi (dokunmakla şiddetli ağlama), gevşek büller ve pozitif Nikolsky belirtisidir (teğetsel sürtünmeyle epidermisin kolayca soyulması). EN KRİTİK AYIRICI TANI NOKTASI: SSSS'de ORAL VE GENİTAL MUKOZALAR KORUNMUŞTUR (mukoza tutulumu yoktur). Mukozal tutulum varsa Stevens-Johnson Sendromu (SJS) veya Toksik Epidermal Nekroliz (TEN) düşünülmelidir (ayrıca SJS/TEN'de ayrılma dermal-epidermal bileşkededir). Büller sterildir çünkü patoloji bakterinin kendisinden değil uzaktaki odaktan (nazofarenks, konjonktiva, göbek vb.) salınan toksinden kaynaklanır. Tedavide İV antistafilokoksik antibiyotik, sıvı-elektrolit kaybının karşılanması, steril yara bakımı (yapışmayan pansumanlar) ve analjezi esastır; kortikosteroidler kontrendikedir.",
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Mukoza Muayenesi",
                "question": "Yaygın kızarıklık, cilde dokunmakla aşırı ağlama ve deride soyulmaları olan 14 aylık bebekte ilk kritik muayene adımı ne olmalıdır?",
                "options": [
                    {
                        "text": "Derideki soyulmaları debride etmek için lezyonları gazlı bezle sertçe ovalayarak soymak ve üzerine alkol bazlı dezenfektan sürmek",
                        "is_correct": False,
                        "scenario_update": "Sert mekanik travma ve alkol uygulaması bebekte dayanılmaz ağrıya, yaygın epidermal doku kaybına ve toksisiteye yol açtı.",
                        "teaching_point": "Yüzeyel büllöz soyulmalarda cilde sert sürtünme ve alkollü solüsyonlar kesinlikle yasaktır; bariyer kaybını ve sıvı kaybını ağırlaştırır."
                    },
                    {
                        "text": "Ağız mukozasını ve konjonktivayı incelemek, teğetsel sürtünmeyle cilt ayrılmasını değerlendirmek ve nazikçe vital bulguları ölçmek",
                        "is_correct": True,
                        "explanation": "Gevşek bül ve soyulmayla giden yaygın eritematöz tablolarda oral mukoza tutulumunun olup olmaması ve Nikolsky bulgusu ayırıcı tanıda en kritik basamaktır.",
                        "new_finding": "Vital Bulgular: Ateş 38.3°C, KTA 136/dk, SS 28/dk, TA 88/54 mmHg, SpO2 %98, KDZ 2 sn. Fizik Muayene: Perioral bölgede radyal çatlaklar ve bal rengi benzeri kabuklanmalar mevcut. Ağız içi oral mukoza, dil ve konjonktivalar tamamen doğal ve nemli (mukoza tutulumu yok). Gövde ve fleksural bölgelerde yaygın parlak eritem; cilde hafif teğetsel sürtünmeyle epidermis tabaka halinde ayrılıyor (pozitif Nikolsky bulgusu), patlamış büllerden seröz sızıntı var, cilt dokunmaya aşırı duyarlı (şiddetli hiperestezi)."
                    },
                    {
                        "text": "Tabloyu basit pişik ve atopik dermatit alevlenmesi kabul ederek yalnızca çinko oksitli krem sürüp bebeği hemen evine göndermek",
                        "is_correct": False,
                        "scenario_update": "Evine gönderilen bebeğin tüm vücut epidermisi soyuldu, sıvı-elektrolit kaybına bağlı dehidratasyon ve sekonder sepsis tablosu gelişti.",
                        "teaching_point": "Pozitif Nikolsky bulgusu, aşırı hiperestezi ve perioral çatlaklar basit pişik değildir; hastaneye yatış gerektiren ciddi toksin ilişkili tablodur."
                    },
                    {
                        "text": "Otoimmün büllöz hastalık düşünerek herhangi bir muayene yapmadan doğrudan yüksek doz oral sistemik prednizolon tedavisi başlatmak",
                        "is_correct": False,
                        "scenario_update": "Bakteriyel toksin zemininde verilen sistemik immünsüpresif kortikosteroid enfeksiyonun kontrolsüzce yayılmasına ve bakteremiye neden oldu.",
                        "teaching_point": "Toksin aracılı soyulma tablolarında kortikosteroidler immünsüpresyon yaparak enfeksiyon kontrolünü bozar ve kesinlikle kontrendikedir."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar Tetkikleri ve Enfeksiyon Odağı Araştırması",
                "question": "Oral mukozası salim, pozitif Nikolsky belirtisi ve belirgin kutanöz hiperestezisi olan bu bebekte en uygun laboratuvar ve tetkik yaklaşımı nedir?",
                "options": [
                    {
                        "text": "Tam kan, elektrolitler, böbrek fonksiyonları incelemek ve primer odağı saptamak için nazofarenks, konjonktiva ve göbekten kültür almak",
                        "is_correct": True,
                        "explanation": "Eksfolyatif toksin ilişkili tablolarda bül sıvısı genellikle sterildir; etken bakteri sıklıkla nazofarenks, konjonktiva, umbilikus veya perioral odakta kolonizedir.",
                        "new_finding": "Laboratuvar Bulguları: BK 16.400/mm3 (%72 nötrofil), CRP 38 mg/L. Biyokimya: Na 134 mEq/L, K 4.1 mEq/L, Üre 26 mg/dL, Kreatinin 0.35 mg/dL. İntak bül sıvısı Gram boyamasında bakteri görülmedi (steril). Nazofarenks ve perioral kabuk sürüntüsü kültüründe metisiline duyarlı Staphylococcus aureus üremesi saptandı."
                    },
                    {
                        "text": "Etkeni izole etmek amacıyla sağlam deriden ve bül tabanından bistüriyle derin cerrahi insizyonel cilt biyopsisi yapmayı planlamak",
                        "is_correct": False,
                        "scenario_update": "İnvaziv cerrahi biyopsi bebekte gereksiz kanamaya ve sekonder bakteriyel yara enfeksiyonuna neden oldu; patoloji yönetimini değiştirmedi.",
                        "teaching_point": "Ayrılma intraepidermal granüler tabakada olduğundan derin cerrahi biyopsi gereksizdir; tanı klinik bulgular ve odak kültürleri ile konur."
                    },
                    {
                        "text": "Hastalığın primer etkenini bulmak için bebeğe genel anestezi altında acilen tanısal fleksibl bronkoskopi ve üst gastrointestinal endoskopi uygulamak",
                        "is_correct": False,
                        "scenario_update": "Mukoza tutulumu olmayan bebekte anestezi altında yapılan invaziv endoskopi mukoza hasarı ve anestezi komplikasyonları yarattı.",
                        "teaching_point": "İç organ veya gastrointestinal mukoza tutulumu olmayan bu klinik antitede invaziv endoskopik incelemelerin yeri yoktur."
                    },
                    {
                        "text": "Hiçbir kan tetkiki ve mikrobiyolojik kültür almadan yalnızca viral seroloji panelini göndererek hastayı hemen antibiyotiksiz taburcu etmeyi planlamak",
                        "is_correct": False,
                        "scenario_update": "Kültür alınmadığı için bakteriyel etken ve antibiyotik duyarlılığı tespit edilemedi, hastanın cilt bariyer kaybı kontrolsüz ilerledi.",
                        "teaching_point": "Toksin salgılayan primer stafilokok odağının tespiti ve antibiyogram için nazofarenks/lezyon kültürü alınması tedavinin temelidir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Oral mukoza tutulumu olmayan, pozitif Nikolsky bulgusu, aşırı hiperestezi ve perioral kabuklanmaları olan bu hastada kesin tanı nedir?",
                "options": [
                    {
                        "text": "Toksik Epidermal Nekroliz",
                        "is_correct": False,
                        "scenario_update": "Toksik epidermal nekrolizde (TEN) en az iki mukozal bölgede (oral, oküler, genital) şiddetli nekrotizan erozyonlar ve tam kat epidermal ayrılma vardır; mukozalar salim kalmaz.",
                        "teaching_point": "TEN/SJS'de belirgin mukozal tutulum ve dermal-epidermal bileşke nekrozu mevcuttur; SSSS'de ise mukoza kesinlikle salimdir ve ayrılma granüler tabakadadır."
                    },
                    {
                        "text": "Yaygın Büllöz İmpetigo",
                        "is_correct": False,
                        "scenario_update": "Büllöz impetigo lokalize enfeksiyondur; büller bakteri içerir ve yaygın güneş yanığı benzeri eritrodermi veya pozitif Nikolsky bulgusu yapmaz.",
                        "teaching_point": "Büllöz impetigo lokalize bir enfeksiyon olup intak bül sıvısında bol stafilokok ürer; SSSS'de ise toksin sistemik dolaşımla yayılır, büller sterildir ve Nikolsky pozitiftir."
                    },
                    {
                        "text": "Stafilokoksik Haşlanmış Deri Sendromu",
                        "is_correct": True,
                        "explanation": "Süt çocuğunda eksfolyatif toksin aracılı gelişen, perioral kabuklanma, kutanöz hiperestezi, pozitif Nikolsky belirtisi ve en önemlisi oral mukoza tutulumunun olmaması ile karakterize tablo Stafilokoksik Haşlanmış Deri Sendromudur (SSSS / Ritter Hastalığı).",
                        "new_finding": "Kesin tanı: Stafilokoksik Haşlanmış Deri Sendromu (SSSS / Ritter Hastalığı). Toksin aracılı intraepidermal granüler tabaka ayrılması teyit edildi."
                    },
                    {
                        "text": "Termal Sıcak Su Yanığı",
                        "is_correct": False,
                        "scenario_update": "Termal haşlanma yanığında temas öyküsü, sınırları belirgin eritem ve derin doku hasarı olur; perioral çatlaklar veya pozitif Nikolsky görülmez.",
                        "teaching_point": "Haşlanma benzeri görünüm olsa da temas öyküsünün olmaması, perioral radyal fissürler ve teğetsel sürtünmeyle soyulma bakteriyel toksik tabloyu kanıtlar."
                    }
                ]
            },
            {
                "stage_title": "Tedavi, Yara Bakımı ve Yatış Yönetimi",
                "question": "Stafilokoksik haşlanmış deri sendromu tanısı kesinleşen 14 aylık bu bebekte en uygun tedavi ve bakım yaklaşımı ne olmalıdır?",
                "options": [
                    {
                        "text": "Herhangi bir antibiyotik vermeden yalnızca yüksek doz oral kortikosteroid şurup başlamak ve bebeği acil servisten hemen evine taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Kortikosteroid verilerek taburcu edilen bebekte bağışıklık baskılandı, stafilokoksik bakteremi ve septik şok tablosu gelişti.",
                        "teaching_point": "SSSS'de kortikosteroid kullanımı kesinlikle kontrendikedir; enfeksiyonun yayılmasına neden olur. Temel tedavi parenteral antistafilokoksik antibiyotiktir."
                    },
                    {
                        "text": "Lezyonları kurutmak amacıyla tüm vücuda alkollü tentürdiyot sürmek ve hidrasyon vermeksizin bebeği ayaktan poliklinik kontrolüne yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Açık epidermal alana uygulanan tentürdiyot sistemik iyot toksisitesi yarattı, şiddetli ağrı ve dehidratasyon tablosunu derinleştirdi.",
                        "teaching_point": "Epidermal bariyeri kaybolmuş deriye tahriş edici antiseptikler uygulanmaz; steril nemlendirici ve yapışmayan pansumanlarla cilt bütünlüğü korunmalıdır."
                    },
                    {
                        "text": "Cilt lezyonlarını cerrahi olarak debride etmek için bebeği acil ameliyathaneye alarak tüm cilde genel anestezi altında zımparalama uygulamak",
                        "is_correct": False,
                        "scenario_update": "Gereksiz agresif cerrahi debridman derin doku hasarı, kontrolsüz masif kanama ve kalıcı skarlaşma komplikasyonlarına yol açtı.",
                        "teaching_point": "SSSS'de doku nekrozu yoktur, ayrılma çok yüzeyeldir (granüler tabaka); kendiliğinden iz bırakmadan iyileşir, cerrahi debridman yapılmaz."
                    },
                    {
                        "text": "İntravenöz antistafilokoksik antibiyotik başlamak, sıvı ve elektrolit desteği sağlamak, steril yapışmayan nemlendirici pansumanlar uygulayarak servise yatırmak",
                        "is_correct": True,
                        "explanation": "SSSS tedavisinde İV antistafilokoksik antibiyotik (sefazolin veya vankomisin), epidermal bariyer kaybına bağlı hidrasyon desteği, steril yapışmayan parafinli pansumanlar ve analjezi esastır; kortikosteroidler kontrendikedir.",
                        "new_finding": "Bebek pediatri servisine yatırıldı. İV sefazolin (100 mg/kg/gün) ve idame + %20 fazlası izotonik hidrasyon başlandı. Lezyonlara steril beyaz vazelin/parafinli gazlı bezler uygulandı, sürtünmeden kaçınıldı. 48 saat içinde ateş düştü, deskuamasyon durdu ve 5. günde iz bırakmadan tam re-epitelizasyon sağlandı."
                    }
                ]
            }
        ]
    }
]
