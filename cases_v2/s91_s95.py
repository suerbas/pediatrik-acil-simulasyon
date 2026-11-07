# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - S91-S95 (Enfeksiyon ve Deri Acilleri)
"""

SPOILERS = {
    "S91": ["boğmaca", "pertussis", "bordetella"],
    "S92": ["tüberküloz", "tbc", "verem", "tüberküloz menenjit"],
    "S93": ["osteomiyelit"],
    "S94": ["stevens", "johnson", "sjs", "toksik epidermal"],
    "S95": ["herpetikum", "kaposi", "variselliform"],
}

CASES = [
    {
        "id": "S91",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "7 Haftalık (4.4 kg)",
        "gender": "Kız",
        "complaint": "On gündür artan öksürük nöbetleri, nöbet sonrası morarma ve bugün bir kez nefesinin durması",
        "history": "Annesi anlatıyor: 'İlk günlerde biraz burnu aktı, hafif öksürüyordu. Sonra öksürükleri nöbet nöbet oldu; art arda öksürüyor, kıpkırmızı sonra mosmor oluyor, sonunda kusuyor. Nöbetler arasında gayet iyi, gülüyor. Bugün öksürük nöbetinden sonra nefesi durdu, sallayınca düzeldi.' Ateşi hiç olmamış. Henüz aşı olmamış (2. ay aşıları önümüzdeki hafta). Annenin ve babanın üç haftadır geçmeyen öksürüğü var, babanınki geceleri kusma yaptıracak kadar şiddetli. Anne gebelikte aşı olmamış.",
        "final_diagnosis": "Boğmaca (Bordetella pertussis) - Apne ve Siyanozla Seyreden Genç Süt Çocuğu",
        "disposition": "Damlacık İzolasyonunda Apne Monitörizasyonu, Azitromisin ve Temaslı Profilaksisiyle Pediatri Servisine (Gerekirse Yoğun Bakıma) Yatış",
        "case_pearl": "Aşısız veya eksik aşılı genç süt çocuklarında en ağır seyreden form görülür. Tipik çocukta kataral dönemden sonra paroksismal öksürük nöbetleri, nöbet sonrası kusma ve siyanoz gelişir; genç bebeklerde 'kükreme' sesi olmayabilir, apne tek bulgu olabilir. Nöbetler arasında bebek iyi görünür ve ateş yoktur. Belirgin lenfositoz tipiktir; çok yüksek lökosit sayısı (>30.000/mm³) pulmoner hipertansiyon ve ölüm riskini gösterir. Tanı nazofaringeal sürüntüde PCR ile konur. Bir aydan küçüklerde ve tüm genç bebeklerde azitromisin tercih edilir. Hane içi tüm temaslılara profilaksi verilir. Gebelikte Tdap aşısı bebekleri korur.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme",
                "question": "Öksürük nöbetleri ve apne öyküsü olan bu bebekte ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Nöbetler arasında iyi göründüğü için ağızdan sıvı ve öksürük şurubu önerip aşı randevusuna kadar evde izlemelerini söylemek",
                        "is_correct": False,
                        "scenario_update": "Bebek evde uzun bir apne geçirdi ve kardiyopulmoner resüsitasyon gerektirdi.",
                        "teaching_point": "Apne öyküsü olan genç süt çocuğu monitörize edilerek hastanede izlenmelidir."
                    },
                    {
                        "text": "Damlacık izolasyonunda monitöre ve pulse oksimetreye bağlamak, bir öksürük nöbetini gözlemlemek ve solunum ile beslenmeyi değerlendirmek",
                        "is_correct": True,
                        "explanation": "Öksürük nöbetinin doğrudan gözlemlenmesi tabloyu netleştirir. İzolasyon diğer bebekleri korur, monitör apne ve desatürasyonu yakalar.",
                        "new_finding": "Nöbetler arasında: ateş 36.8°C, KTA 148/dk, SS 40/dk, SpO2 %98, solunum sıkıntısı yok, akciğerler temiz. Gözlenen nöbette art arda 15-20 kısa öksürük, yüz kızarıp morardı, SpO2 %72'ye düştü, ardından 12 saniye apne ve bradikardi (80/dk), sonunda kusma oldu. Uyarıyla düzeldi. Konjonktivalarda subkonjonktival kanama. Beslenme sırasında yorulma."
                    },
                    {
                        "text": "Hışıltısı olmasa da bronşiolit kabul edip salbutamol ve adrenalin nebülü vermek, nöbetler geçerse taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Nebüller öksürük nöbetlerini etkilemedi; bebek gece ağır bir apne geçirdi.",
                        "teaching_point": "Nöbetler arasında temiz akciğer ve paroksismal öksürük bu tabloyu bronşiolitten ayırır."
                    },
                    {
                        "text": "Morarma nedeniyle doğuştan kalp hastalığı kabul edip yalnızca ekokardiyografi istemek ve kardiyoloji görüşünü beklemek",
                        "is_correct": False,
                        "scenario_update": "Bekleme süresinde izolasyon yapılmadı; bekleme alanında başka bir bebek temaslı oldu.",
                        "teaching_point": "Morarma öksürük nöbetiyle ilişkiliyse solunum yolu kaynaklıdır; önce izolasyon ve monitörizasyon gerekir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Bu bebekte hangi tetkikler en uygundur?",
                "options": [
                    {
                        "text": "Tam kan sayımı ile nazofaringeal sürüntüden PCR göndermek; akciğer grafisi çekmek ve ekokardiyografiyi planlamak",
                        "is_correct": True,
                        "explanation": "Lenfositoz tanıyı destekler, çok yüksek lökosit sayısı ağır seyri öngörür. PCR tanıyı doğrular. Ekokardiyografi pulmoner hipertansiyonu değerlendirir.",
                        "new_finding": "Lökosit 34.600/mm³ (%76 lenfosit), trombosit 612.000/mm³, CRP 4 mg/L. Akciğer grafisinde kalp kenarlarında tüylü görünüm, konsolidasyon yok. Nazofaringeal PCR pozitif. Ekokardiyografide pulmoner basınç hafif yüksek."
                    },
                    {
                        "text": "Nöbetler epileptik olabileceği için acil EEG ve beyin ultrasonografisi istemek, sonuçlarına göre antiepileptik başlamak",
                        "is_correct": False,
                        "scenario_update": "EEG normal geldi; asıl tanı gecikti.",
                        "teaching_point": "Morarma ve apne öksürük nöbetiyle birlikteyse nedeni solunumsaldır."
                    },
                    {
                        "text": "Sepsis kuşkusuyla lomber ponksiyon, kan ve idrar kültürü yapıp sonuçlar gelene kadar ampisilin ve sefotaksim başlamak",
                        "is_correct": False,
                        "scenario_update": "Ateşsiz ve nöbetler arasında iyi görünen bebekte gereksiz girişimler yapıldı.",
                        "teaching_point": "Tetkikler klinik tabloya göre seçilir; bu bebekte ateş ve sepsis bulgusu yoktur."
                    },
                    {
                        "text": "Yalnızca boğaz kültürü almak ve sonucu bir hafta sonra değerlendirmek üzere bebeği taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Boğaz kültürü bu etken için uygun örnek değildi ve bebek evde kötüleşti.",
                        "teaching_point": "Tanı nazofaringeal örnekten PCR ile konur; apneli bebek taburcu edilmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Akut bronşiolit", "is_correct": False, "scenario_update": "Nöbetler arasında akciğerler temiz, solunum sıkıntısı yoktu ve belirgin lenfositoz vardı.", "teaching_point": "Bronşiolitte sürekli takipne, raller ve hışıltı vardır."},
                    {"text": "Klamidya pnömonisi", "is_correct": False, "scenario_update": "Konjonktivit öyküsü ve kesik kesik öksürük yoktu, eozinofili saptanmadı.", "teaching_point": "Klamidya pnömonisinde staccato öksürük, takipne ve eozinofili görülür."},
                    {"text": "Boğmaca (pertussis)", "is_correct": True, "explanation": "Aşısız genç bebekte kataral dönemi izleyen paroksismal öksürük, nöbet sonrası siyanoz, apne ve kusma, nöbetler arası iyilik, ateş olmaması, belirgin lenfositoz, uzun süre öksüren ebeveynler ve PCR pozitifliği boğmacayı gösterir.", "new_finding": "Tanı: Boğmaca (Bordetella pertussis)."},
                    {"text": "Gastroözofageal reflü hastalığı", "is_correct": False, "scenario_update": "Kusma öksürük nöbetlerinden sonra geliyordu ve lenfositoz vardı.", "teaching_point": "Reflüde kusma beslenmeyle ilişkilidir, öksürük nöbetleri ve lenfositoz beklenmez."}
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu bebek ve ailesi için en uygun plan hangisidir?",
                "options": [
                    {
                        "text": "Öksürük nöbetlerini azaltmak için oral kortikosteroid ve salbutamol şurubu başlayıp antibiyotiği gereksiz bulmak",
                        "is_correct": False,
                        "scenario_update": "Nöbetler azalmadı ve bebek bulaştırıcı kalmaya devam etti.",
                        "teaching_point": "Bu ilaçların öksürük nöbetlerine etkisi gösterilmemiştir; antibiyotik bulaştırıcılığı azaltır."
                    },
                    {
                        "text": "Bebeğe beş gün azitromisin başlamak, monitörle yatırmak ve hane içi tüm temaslılara profilaktik antibiyotik vermek",
                        "is_correct": True,
                        "explanation": "Azitromisin bu yaşta güvenle kullanılır ve bulaştırıcılığı azaltır. Temaslı profilaksisi hane içindeki yeni olguları önler. Yüksek lökosit nedeniyle yoğun bakımla iletişim sürdürülür.",
                        "new_finding": "Azitromisin başlandı, anne, baba ve kardeşe profilaksi verildi, olgu bildirildi. Lökosit 41.000/mm³'e yükselince yoğun bakıma alındı; öksürük nöbetleri iki hafta içinde azaldı ve bebek dördüncü haftada taburcu edildi."
                    },
                    {
                        "text": "Bebeğe hemen ilk doz aşısını yapıp antibiyotik vermeden taburcu etmek ve ailenin öksürüğünü önemsememek",
                        "is_correct": False,
                        "scenario_update": "Aşı mevcut hastalığı tedavi etmedi; ailede yeni olgular gelişti.",
                        "teaching_point": "Aşı hastalığı tedavi etmez; temaslılar profilaksi almalıdır."
                    },
                    {
                        "text": "Yalnızca bebeği tedavi edip anne ve babanın öksürüğünü viral kabul ederek profilaksi vermemek",
                        "is_correct": False,
                        "scenario_update": "Bulaş kaynağı olan ebeveynler tedavi edilmedi ve yeni doğan kuzenine hastalık bulaştı.",
                        "teaching_point": "Genç bebeklerde kaynak çoğunlukla aile bireyleridir; tüm hane profilaksi almalıdır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S92",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "2 Yaşında (10.5 kg)",
        "gender": "Erkek",
        "complaint": "İki haftadır düşük dereceli ateş, iştahsızlık ve huzursuzluk; son iki gündür aşırı uyku hali ve kusma",
        "history": "Annesi anlatıyor: 'İki haftadır ateşi 38 civarında, hiç iştahı yok, kilo verdi. Hep huzursuz, ağlıyor. İki gündür sürekli uyuyor, kusuyor, bugün sol gözü kaydı.' İki kez farklı merkezlerde 'viral enfeksiyon' tanısı almış. Aile kalabalık bir evde yaşıyor. Dedesinin birkaç aydır kanlı balgamlı öksürüğü varmış ve 'akciğer' tedavisi başlanmış. Çocuğun BCG skarı yok, aşıları eksik. Kafa travması yok.",
        "final_diagnosis": "Tüberküloz Menenjit (Evre 2) ve Hidrosefali",
        "disposition": "Dörtlü Antitüberküloz Tedavi ve Deksametazon Başlanarak Çocuk Enfeksiyon ve Beyin Cerrahisi İzlemiyle Yatış; Bildirim ve Temaslı Taraması",
        "case_pearl": "Özellikle 5 yaş altında, BCG'siz ve erişkin olgu ile teması olan çocuklarda görülür. Haftalara yayılan sinsi başlangıç (ateş, iştahsızlık, huzursuzluk), ardından bilinç değişikliği, kusma ve kranial sinir felçleri (en sık 6. sinir) tipiktir. BOS'ta lenfosit baskın pleositoz, belirgin protein artışı ve düşük glukoz görülür. Görüntülemede bazal meninkslerde kontrastlanma, hidrosefali ve infarktlar olabilir. Tanı beklenmeden dörtlü tedavi (izoniazid, rifampisin, pirazinamid, etambutol veya etiyonamid) ve deksametazon başlanır. Erişkin kaynak olgunun ilaç duyarlılığı tedavi seçiminde önemlidir. Olgu bildirilir ve tüm temaslılar taranır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme",
                "question": "Haftalardır süren ateş ve yeni gelişen bilinç değişikliği olan bu çocukta ilk değerlendirmeniz nedir?",
                "options": [
                    {
                        "text": "Daha önce viral enfeksiyon dendiği için ateş düşürücü ve antiemetikle izleyip uykululuğu ateşe bağlamak",
                        "is_correct": False,
                        "scenario_update": "Çocuk gece nöbet geçirdi ve bilinci daha da kötüleşti.",
                        "teaching_point": "Uzamış ateş ve yeni bilinç değişikliği merkezi sinir sistemi enfeksiyonu açısından değerlendirilmelidir."
                    },
                    {
                        "text": "Hava yolu ve kan şekerini kontrol edip bilinç, pupiller, kranial sinirler ve menenjit bulgularını değerlendirmek, temas öyküsünü sormak",
                        "is_correct": True,
                        "explanation": "Bilinç değişikliği ve kranial sinir tutulumu kafa içi basınç artışını ve bazal meninks tutulumunu düşündürür. Ailede uzun süreli öksürüğü olan bir erişkin önemli bir ipucudur.",
                        "new_finding": "Ateş 38.3°C, KTA 128/dk, KB 104/68 mmHg, SS 28/dk. Kan şekeri 92 mg/dL. GKS 11. Ense sertliği belirgin, Kernig pozitif. Sol gözde dışa bakış kısıtlılığı. Pupiller eşit, ışık yanıtı var. Fundus muayenesinde hafif papilödem. Tartı yaşına göre 10. persentilin altında. BCG skarı yok. Akciğerlerde ince raller."
                    },
                    {
                        "text": "Huzursuzluk ve kusma nedeniyle intussusepsiyon kabul edip karın ultrasonografisi isteyip nörolojik muayeneyi ertelemek",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografi normal geldi ve nörolojik değerlendirme gecikti.",
                        "teaching_point": "Ense sertliği ve kranial sinir felci olan çocukta önce nörolojik değerlendirme yapılır."
                    },
                    {
                        "text": "Hemen lomber ponksiyon yapıp sonuçlara göre tedavi kararını vermek ve bu sürede tedavi başlamamak",
                        "is_correct": False,
                        "scenario_update": "Papilödem ve kranial sinir felci olan çocukta görüntülemesiz ponksiyon herniasyon riskini artırdı.",
                        "teaching_point": "Kafa içi basınç artışı bulgularında ponksiyondan önce görüntüleme yapılır."
                    }
                ]
            },
            {
                "stage_title": "Görüntüleme ve BOS Değerlendirmesi",
                "question": "Görüntüleme ve BOS sonuçları aşağıdaki gibidir. Bu bulgular hangi tabloyla en uyumludur?",
                "options": [
                    {
                        "text": "BOS'ta nötrofil baskın 4.000/mm³ hücre, çok düşük glukoz; BT'de normal ventriküller ve konveksite meninkslerinde kontrastlanma",
                        "is_correct": False,
                        "scenario_update": "Hastanın sonuçları bu tabloyla uyumlu değildi.",
                        "teaching_point": "Bu tablo akut bakteriyel menenjiti düşündürür; haftalara yayılan sinsi seyir beklenmez."
                    },
                    {
                        "text": "BOS'ta lenfosit baskın 50-300/mm³ hücre, belirgin protein artışı, düşük glukoz; BT'de bazal kontrastlanma ve hidrosefali",
                        "is_correct": True,
                        "explanation": "Lenfositik pleositoz, yüksek protein ve düşük glukoz birlikteliği ile bazal meninks tutulumu ve hidrosefali haftalara yayılan kronik granülomatöz menenjiti gösterir.",
                        "new_finding": "Kontrastlı BT: Bazal sisternlerde yoğun kontrastlanma, lateral ve üçüncü ventriküllerde genişleme, sol bazal gangliyonda küçük infarkt. BOS (BT sonrası): lökosit 180/mm³ (%85 lenfosit), protein 260 mg/dL, glukoz 22 mg/dL (kan 92). ARB boyaması negatif, PCR ve kültür gönderildi. Akciğer grafisinde milier görünüm. Dedenin balgamında ARB pozitif."
                    },
                    {
                        "text": "BOS'ta lenfosit baskın hafif pleositoz, normal glukoz ve eritrositler; MR'da tek taraflı temporal lob tutulumu",
                        "is_correct": False,
                        "scenario_update": "Hastanın sonuçları bu tabloyla uyumlu değildi.",
                        "teaching_point": "Bu tablo herpes ensefalitini düşündürür; akut başlangıç ve fokal nöbetle gelir."
                    },
                    {
                        "text": "BOS tamamen normal, BT'de posterior fossada kontrast tutan kitle ve buna bağlı obstrüktif hidrosefali",
                        "is_correct": False,
                        "scenario_update": "Hastanın sonuçları bu tabloyla uyumlu değildi.",
                        "teaching_point": "Bu tablo bir kitle lezyonunu düşündürür; ateş ve meninks bulguları beklenmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Kısmen tedavi edilmiş bakteriyel menenjit", "is_correct": False, "scenario_update": "Daha önce antibiyotik kullanılmamıştı, bazal tutulum, milier akciğer ve erişkin temaslı vardı.", "teaching_point": "Kısmen tedavi edilmiş menenjitte de lenfositoz görülebilir; öykü ve görüntüleme ayrımda önemlidir."},
                    {"text": "Tüberküloz menenjit ve hidrosefali", "is_correct": True, "explanation": "BCG'siz, aktif akciğer hastalığı olan dede ile temaslı çocukta haftalara yayılan sinsi başlangıç, altıncı sinir felci, lenfositik pleositoz, çok yüksek protein, düşük glukoz, bazal kontrastlanma, hidrosefali ve milier akciğer tüberküloz menenjiti gösterir.", "new_finding": "Tanı: Tüberküloz menenjit (evre 2) ve hidrosefali, milier tüberküloz."},
                    {"text": "Viral ensefalit", "is_correct": False, "scenario_update": "Glukoz çok düşük ve protein çok yüksekti, bazal tutulum vardı.", "teaching_point": "Viral ensefalitte glukoz normaldir, protein hafif artar."},
                    {"text": "Kriptokok menenjiti", "is_correct": False, "scenario_update": "Bilinen immün yetmezlik yoktu ve erişkin temaslının balgamında ARB vardı.", "teaching_point": "Kriptokok menenjiti büyük ölçüde immün yetmezlikli hastalarda görülür."}
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Kültür ve duyarlılık sonuçlarını beklemek için tedaviyi altı hafta ertelemek ve bu sürede seftriakson vermek",
                        "is_correct": False,
                        "scenario_update": "Tedavi gecikince çocuk komaya girdi ve kalıcı nörolojik hasar gelişti.",
                        "teaching_point": "Bu tanıda kültür beklenmeden tedavi başlanmalıdır; gecikme ölüm ve sekel riskini artırır."
                    },
                    {
                        "text": "Yalnızca izoniazid ve rifampisinle tedaviye başlamak ve kortikosteroid vermeden genel serviste izlemek",
                        "is_correct": False,
                        "scenario_update": "İkili tedavi menenjit için yetersizdi; ödem ve hidrosefali ilerledi.",
                        "teaching_point": "Merkezi sinir sistemi tutulumunda dörtlü tedavi ve kortikosteroid gerekir."
                    },
                    {
                        "text": "Dörtlü antitüberküloz tedavi ve deksametazon başlamak, hidrosefali için beyin cerrahisine danışmak, olguyu bildirip temaslıları taramak",
                        "is_correct": True,
                        "explanation": "Erken dörtlü tedavi ve kortikosteroid ölüm ve sekel riskini azaltır. Hidrosefali drenaj gerektirebilir. Temaslı taraması diğer çocukları korur.",
                        "new_finding": "İzoniazid, rifampisin, pirazinamid, etiyonamid ve deksametazon başlandı. Hidrosefali için ventriküloperitoneal şant takıldı. Dedenin suşu ilaçlara duyarlı çıktı. Evdeki diğer çocuklara koruyucu tedavi başlandı. Çocuk hafif sol hemiparezi ile yatışının altıncı haftasında taburcu edildi."
                    },
                    {
                        "text": "Ampirik antiviral ve antifungal tedavi başlayıp tanı doğrulanınca antitüberküloz tedaviyi eklemeyi düşünmek",
                        "is_correct": False,
                        "scenario_update": "Gerekli tedavi gecikti ve çocuğun bilinci kötüleşti.",
                        "teaching_point": "Klinik ve BOS bulguları güçlü şüphe oluşturduğunda antitüberküloz tedavi hemen başlanır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S93",
        "category": "🦴 Kas-İskelet & Eklem / Ortopedik Aciller",
        "age": "6 Yaşında (21 kg)",
        "gender": "Erkek",
        "complaint": "Dört gündür ateş ve sağ bacakta dizin altında giderek artan ağrı, bugün bacağına basamama",
        "history": "Annesi anlatıyor: 'Dört gün önce parkta düştü, dizinin altı hafifçe sıyrıldı. Sonraki gün ateşi çıktı, bacağı ağrımaya başladı. Ateşi 39'a çıkıyor, ağrı gece daha fazla. Bugün bacağına hiç basmıyor.' Başka bir merkezde 'kas zedelenmesi' denip ibuprofen verilmiş. Dizini hareket ettirebiliyor ama kaval kemiğine dokunulmasına izin vermiyor. Bilinen hastalığı yok, aşıları tam.",
        "final_diagnosis": "Sağ Proksimal Tibia Akut Hematojen Osteomiyeliti (Metisiline Duyarlı Staphylococcus aureus)",
        "disposition": "Kan Kültürü Sonrası İV Sefazolin ile Çocuk Ortopedi ve Enfeksiyon İzleminde Servise Yatış",
        "case_pearl": "Çocuklarda en sık uzun kemiklerin metafizinde (tibia, femur) görülür; en sık etken S. aureus'tur. Ateş, lokalize kemik hassasiyeti ve yük vermeyi reddetme tipiktir. Hafif bir travma öyküsü tanıyı yanıltabilir. Direkt grafi ilk iki haftada çoğu zaman normaldir; erken tanıda en duyarlı yöntem MR'dır. CRP ve sedimantasyon yüksektir, kan kültürü yaklaşık yarısında pozitiftir. Kültür alındıktan sonra antistafilokokal ampirik tedavi (sefazolin; MRSA yüksek bölgelerde klindamisin veya vankomisin) başlanır. Subperiostal apse cerrahi drenaj gerektirir. Klinik ve CRP düzelince oral tedaviye geçilir, toplam süre en az 3-4 haftadır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Ateşli ve bacağına basamayan bu çocukta muayenede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Düşme öyküsü olduğu için kas zedelenmesi kabul edip yalnızca soğuk uygulama ve ibuprofen önerisiyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk üç gün sonra bacakta belirgin şişlik ve septik tabloyla getirildi.",
                        "teaching_point": "Ateş ve yük vermeyi reddetme hafif travmayla açıklanmaz; enfeksiyon dışlanmalıdır."
                    },
                    {
                        "text": "Ağrının eklemden mi kemikten mi kaynaklandığını ayırmak için eklem hareketlerini ve kemik üzerindeki hassasiyeti değerlendirmek",
                        "is_correct": True,
                        "explanation": "Eklem hareketleri serbest olup kemik üzerinde lokalize hassasiyet olması kemik enfeksiyonunu, hareketle belirgin ağrı ve eklem sıvısı ise eklem enfeksiyonunu düşündürür.",
                        "new_finding": "Ateş 39.1°C, KTA 126/dk, KB 100/64 mmHg, KDZ 2 sn. Sağ tibia proksimal metafizi üzerinde nokta hassasiyet, hafif ısı artışı ve ödem. Diz pasif hareketleri tam ve ağrısız, eklemde sıvı yok. Dizin altında iyileşmekte olan yüzeyel sıyrık. Kalça ve ayak bileği normal. Başka odak yok."
                    },
                    {
                        "text": "Diz ekleminde septik artrit kabul edip muayeneyi kısa tutarak hemen eklem aspirasyonu yapmak",
                        "is_correct": False,
                        "scenario_update": "Eklemde sıvı yoktu; girişim gereksiz yere yapıldı.",
                        "teaching_point": "Eklem hareketleri serbestse önce kemik kaynaklı enfeksiyon düşünülmelidir."
                    },
                    {
                        "text": "Gece artan kemik ağrısı nedeniyle doğrudan lösemi kabul edip kemik iliği aspirasyonu için onkolojiye sevk etmek",
                        "is_correct": False,
                        "scenario_update": "Kan sayımı ve görüntüleme yapılmadan sevk edildi; tedavi gecikti.",
                        "teaching_point": "Ateşli lokalize kemik ağrısında önce enfeksiyon araştırılır; malignite kan sayımı ve yaymayla değerlendirilir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik ve Görüntüleme",
                "question": "Bu çocukta hangi tetkik ve görüntüleme yaklaşımı uygundur?",
                "options": [
                    {
                        "text": "Yalnızca direkt grafi çekmek, grafi normalse kemik enfeksiyonunu dışlamak ve ağrı kesiciyle evde izlem önerip taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Normal grafi yanıltıcı oldu; tedavi bir hafta gecikti.",
                        "teaching_point": "Direkt grafide kemik değişiklikleri 10-14 günden önce genellikle görülmez."
                    },
                    {
                        "text": "Tam kan sayımı, CRP, sedimantasyon ve kan kültürü almak; grafi çekip normalse MR istemek",
                        "is_correct": True,
                        "explanation": "Kan kültürü etkeni gösterebilir. Grafi kırık ve tümörü dışlar ama erken dönemde normaldir. MR kemik iliği ödemini ve apseyi erken gösterir.",
                        "new_finding": "Lökosit 16.400/mm³, CRP 124 mg/L, sedimantasyon 72 mm/sa, trombosit normal, yaymada blast yok. Direkt grafi normal. MR'da sağ proksimal tibia metafizinde kemik iliği ödemi ve kontrastlanma, 8 mm'lik subperiostal sıvı birikimi. Kan kültüründe gram pozitif koklar üredi."
                    },
                    {
                        "text": "Kemik sintigrafisi ve tüm vücut tomografisi istemek, sonuçlar gelene kadar antibiyotik başlamamak",
                        "is_correct": False,
                        "scenario_update": "Tetkikler günler aldı ve çocuk ateşli kalmaya devam etti.",
                        "teaching_point": "MR tercih edilen yöntemdir; görüntüleme antibiyotiği geciktirmemelidir."
                    },
                    {
                        "text": "Kan kültürü almadan hemen oral amoksisilin başlayıp bir hafta sonra kontrol grafisiyle değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Kültür alınmadığı için etken saptanamadı ve oral tedavi yetersiz kaldı.",
                        "teaching_point": "Antibiyotik öncesi kültür alınmalı; başlangıç tedavisi intravenöz olmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Septik artrit (diz)", "is_correct": False, "scenario_update": "Eklem hareketleri ağrısızdı ve eklemde sıvı yoktu.", "teaching_point": "Septik artritte eklem hareketleri belirgin ağrılı ve kısıtlıdır."},
                    {"text": "Ewing sarkomu", "is_correct": False, "scenario_update": "MR bulguları enfeksiyonla uyumluydu ve kan kültüründe üreme oldu.", "teaching_point": "Ewing sarkomu ateş ve yüksek akut fazla gelebilir; grafide soğan zarı görünümü ve kitle görülür."},
                    {"text": "Akut hematojen osteomiyelit", "is_correct": True, "explanation": "Ateş, tibia metafizinde lokalize hassasiyet ve ısı artışı, yük vermeyi reddetme, yüksek akut faz belirteçleri, normal grafi, MR'da kemik iliği ödemi ve subperiostal sıvı ile kan kültürü üremesi akut hematojen osteomiyeliti gösterir.", "new_finding": "Tanı: Sağ proksimal tibia akut hematojen osteomiyeliti. Kan kültürü: metisiline duyarlı S. aureus."},
                    {"text": "Alt bacak selüliti", "is_correct": False, "scenario_update": "Deri bulguları sınırlıydı ve hassasiyet kemik üzerindeydi; MR'da kemik tutulumu vardı.", "teaching_point": "Selülitte yayılan eritem ve deri hassasiyeti ön plandadır."}
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "İV sefazolin başlamak, subperiostal sıvı için ortopediye danışmak ve klinik ile CRP düzelince oral tedaviye geçmek",
                        "is_correct": True,
                        "explanation": "Sefazolin metisiline duyarlı stafilokoklara etkilidir. Subperiostal birikim drenaj gerektirebilir. İyi yanıt alınınca oral tedaviyle toplam süre en az 3-4 haftaya tamamlanır.",
                        "new_finding": "Sefazolin başlandı, ortopedi tarafından subperiostal apse drene edildi. Ateş 48 saatte düştü, CRP beşinci günde 32 mg/L'ye indi. Oral sefaleksine geçilip toplam dört haftalık tedaviyle iyileşti."
                    },
                    {
                        "text": "Bir haftalık oral sefaleksinle evde tedavi edip CRP ve grafiyle iki hafta sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Kısa oral tedaviyle apse büyüdü ve çocuk sepsis tablosuyla yatırıldı.",
                        "teaching_point": "Başlangıç tedavisi hastanede ve intravenöz olarak verilir; tedavi süresi en az birkaç haftadır."
                    },
                    {
                        "text": "Ağrıyı azaltmak için bacağı alçıya alıp antibiyotik olmadan istirahatle iyileşmesini beklemek",
                        "is_correct": False,
                        "scenario_update": "Enfeksiyon ilerleyip kemik nekrozu ve büyüme plağı hasarı gelişti.",
                        "teaching_point": "Kemik enfeksiyonu antibiyotik tedavisi gerektirir; immobilizasyon tek başına yeterli değildir."
                    },
                    {
                        "text": "Ampirik olarak yalnızca İV gentamisin başlayıp kültür sonucuna göre gerekirse tedaviyi değiştirmek",
                        "is_correct": False,
                        "scenario_update": "Gentamisin stafilokoka yeterli etki göstermedi; ateş sürdü.",
                        "teaching_point": "Ampirik tedavi en sık etken olan stafilokoku mutlaka kapsamalıdır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S94",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "11 Yaşında (35 kg)",
        "gender": "Kız",
        "complaint": "İki gündür ateş, ağızda yaralar, gözlerde yanma ve gövdeden yayılan, içi su toplayan döküntü",
        "history": "Annesi anlatıyor: 'İki hafta önce ilk kez nöbet geçirdi, karbamazepin başlandı. Dört gün önce ateşi, boğaz ağrısı ve halsizliği oldu, grip sandık. Dün göğsünde koyu kırmızı lekeler çıktı, bugün yayıldı, bazılarının ortası kabarıp su topladı. Dudakları yara oldu, yemek yiyemiyor, gözleri yanıyor, çişini yaparken yanıyor.' Daha önce ilaç alerjisi bilinmiyor.",
        "final_diagnosis": "Karbamazepine Bağlı Stevens-Johnson Sendromu (Vücut Yüzeyinin <%10 Epidermal Ayrılması)",
        "disposition": "Sorumlu İlacın Kesilmesi, Alternatif Antiepileptik ve Multidisipliner Destek Tedavisiyle Yanık Ünitesi veya Çocuk Yoğun Bakıma Yatış",
        "case_pearl": "Bu ağır deri reaksiyonu çoğunlukla yeni başlanan bir ilaçtan (antiepileptikler: karbamazepin, fenitoin, lamotrijin, fenobarbital; sülfonamidler; allopürinol) 4-28 gün sonra gelişir. Ateş ve grip benzeri prodromu izleyerek koyu, atipik hedef lezyonlar, büller ve en az iki mukozada (ağız, göz, genital) erozyonlar ortaya çıkar. Nikolsky işareti pozitiftir. Vücut yüzeyinin %10'undan azının ayrılması bu tanıyı, %30'dan fazlası toksik epidermal nekrolizi gösterir. En önemli adım sorumlu ilacın hemen kesilmesidir; aromatik antiepileptikler arasında çapraz reaksiyon olabileceği için levetirasetam gibi bir ilaç seçilir. Yanık hastası gibi sıvı, ağrı ve yara bakımı yapılır, göz için oftalmoloji erkenden çağrılır. Eritema multiforme minörde mukoza tutulumu sınırlıdır ve tipik lezyonlar ekstremitelerdedir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme",
                "question": "Ateş, mukozal yaralar ve büllü döküntüsü olan bu çocukta ilk değerlendirmeniz nedir?",
                "options": [
                    {
                        "text": "Döküntüyü suçiçeği kabul edip ilaç öyküsü almadan oral asiklovir, antihistaminik ve ateş için ibuprofen vererek evde izlem önermek",
                        "is_correct": False,
                        "scenario_update": "İlaç kesilmediği için döküntü ertesi gün yayıldı ve geniş alanlarda deri soyuldu.",
                        "teaching_point": "Mukozal tutulumlu büllü döküntüde yeni başlanmış ilaç mutlaka sorgulanmalıdır."
                    },
                    {
                        "text": "Vital bulgular ve hidrasyonu değerlendirip mukozaları, deri ayrılmasının yüzdesini ve Nikolsky işaretini incelemek; ilaç öyküsü almak",
                        "is_correct": True,
                        "explanation": "Deri ayrılmasının yaygınlığı ve mukozal tutulum şiddeti ve tedavi yerini belirler. Yeni başlanan ilaç olası tetikleyicidir.",
                        "new_finding": "Ateş 38.9°C, KTA 128/dk, KB 106/64 mmHg, SS 22/dk, SpO2 %98. Mukozalar kuru. Gövde ve proksimal kollarda birleşme eğiliminde koyu kırmızı-mor maküller, ortalarında büller ve gevşek kabarcıklar; dokunmakla deri kayıyor (Nikolsky pozitif). Epidermal ayrılma vücut yüzeyinin yaklaşık %6'sı. Dudaklarda hemorajik kabuklu erozyonlar, ağız içinde yaygın erozyonlar. Bilateral konjonktivit ve göz kapaklarında yapışma eğilimi. Genital mukozada erozyon."
                    },
                    {
                        "text": "Döküntüyü stafilokoksik haşlanmış deri sendromu kabul edip İV klindamisin başlamak ve ilacı sürdürmek",
                        "is_correct": False,
                        "scenario_update": "Tetikleyici ilaç kesilmediği için mukozal tutulum ağırlaştı.",
                        "teaching_point": "Haşlanmış deri sendromunda mukozalar tutulmaz; burada belirgin mukozal tutulum vardır."
                    },
                    {
                        "text": "Nöbet riskini artırmamak için karbamazepini sürdürüp döküntüye yüksek doz oral kortikosteroid eklemek",
                        "is_correct": False,
                        "scenario_update": "İlaç sürdürüldüğü için deri ayrılması %25'e ilerledi.",
                        "teaching_point": "Sorumlu ilacın hemen kesilmesi bu tablodaki en önemli tedavi adımıdır."
                    }
                ]
            },
            {
                "stage_title": "Acil Önlemler",
                "question": "Bu çocukta acilde hangi adımlar öncelikli olmalıdır?",
                "options": [
                    {
                        "text": "Karbamazepini hemen kesip yerine fenitoin başlamak ve kabarcıkları steril iğneyle açarak bandajla kapatmak",
                        "is_correct": False,
                        "scenario_update": "Fenitoin çapraz reaksiyonla tabloyu ağırlaştırdı; açılan kabarcıklar enfekte oldu.",
                        "teaching_point": "Aromatik antiepileptikler arasında çapraz reaksiyon olabilir; büller yerinde bırakılır."
                    },
                    {
                        "text": "Karbamazepini kesip levetirasetama geçmek, İV sıvı ve ağrı tedavisi vermek, yapışmayan örtülerle yara bakımı yapıp oftalmolojiyi çağırmak",
                        "is_correct": True,
                        "explanation": "Sorumlu ilacın kesilmesi ilerlemeyi durdurur. Levetirasetam aromatik yapıda değildir. Deri kaybı sıvı kaybına yol açar. Erken göz bakımı kalıcı görme sorunlarını önler.",
                        "new_finding": "Karbamazepin kesildi, levetirasetam başlandı. Sıvı ve morfin infüzyonu başlandı. Oftalmoloji yapışıklıkları açtı, göz damlaları başlandı. Ağız bakımı için antiseptik gargara verildi. Mesane kateteri takıldı."
                    },
                    {
                        "text": "Ağrı ve ateş için ibuprofen başlayıp deri lezyonlarını antibiyotikli pomatla kapatmak ve dermatoloji randevusu vermek",
                        "is_correct": False,
                        "scenario_update": "Ayaktan izlenen çocukta dehidratasyon ve göz komplikasyonları gelişti.",
                        "teaching_point": "Bu ağırlıkta tablo ayaktan izlenmez; sıvı, göz ve deri bakımı hastanede yapılır."
                    },
                    {
                        "text": "Enfeksiyonu önlemek için profilaktik olarak geniş spektrumlu İV antibiyotik başlayıp antiepileptik ilacı nöroloji görüşü alınana kadar sürdürmek",
                        "is_correct": False,
                        "scenario_update": "İlaç sürdürüldü; deri ayrılması ilerledi ve gereksiz antibiyotik direnç riskini artırdı.",
                        "teaching_point": "Profilaktik antibiyotik önerilmez; tetikleyici ilaç hemen kesilmelidir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Eritema multiforme minör", "is_correct": False, "scenario_update": "Lezyonlar gövdede yoğunlaşmıştı, atipik ve büllüydü, üç mukoza belirgin tutulmuştu.", "teaching_point": "Eritema multiforme minörde tipik üç halkalı hedef lezyonlar ekstremitelerdedir, mukoza tutulumu yoktur veya hafiftir."},
                    {"text": "Stafilokoksik haşlanmış deri sendromu", "is_correct": False, "scenario_update": "Mukozalar tutulmuştu ve yeni başlanmış bir ilaç vardı.", "teaching_point": "Bu sendromda mukozalar korunur ve ayrılma yüzeyeldir."},
                    {"text": "Büllöz impetigo", "is_correct": False, "scenario_update": "Lezyonlar yaygındı, sistemik bulgular ve mukoza tutulumu vardı.", "teaching_point": "Büllöz impetigoda lokalize gevşek büller olur, mukoza tutulmaz."},
                    {"text": "Karbamazepine bağlı Stevens-Johnson sendromu", "is_correct": True, "explanation": "Yeni başlanan karbamazepinden iki hafta sonra ateşli prodrom, gövdede atipik hedef lezyonlar ve büller, Nikolsky pozitifliği, üç mukozada erozyon ve vücut yüzeyinin %10'undan az ayrılması Stevens-Johnson sendromunu gösterir.", "new_finding": "Tanı: Karbamazepine bağlı Stevens-Johnson sendromu."}
                ]
            },
            {
                "stage_title": "Yatış ve İzlem",
                "question": "Bu çocuk için en uygun yatış ve izlem planı hangisidir?",
                "options": [
                    {
                        "text": "Ağız yaraları nedeniyle beslenemeyeceği için yalnızca İV sıvıyla genel pediatri servisinde rutin izlemek",
                        "is_correct": False,
                        "scenario_update": "Serviste deri bakımı ve sıvı dengesi yeterli izlenemedi; sepsis gelişti.",
                        "teaching_point": "Bu hastalar yanık ünitesi veya yoğun bakım deneyimi olan merkezlerde izlenmelidir."
                    },
                    {
                        "text": "Yanık ünitesi veya yoğun bakıma yatırıp göz, ağız ve genital bakımı yürütmek; ilacı alerji kaydına işlemek",
                        "is_correct": True,
                        "explanation": "Deri kaybı sıvı ve ısı kaybı, enfeksiyon ve ağrı yönetimi gerektirir. Göz ve genital mukozanın bakımı kalıcı yapışıklıkları önler. İlacın kaydedilmesi tekrar maruziyeti önler.",
                        "new_finding": "Yanık ünitesine yatırıldı. Deri ayrılması %8'de durdu. Üçüncü haftada epitelizasyon tamamlandı; hafif kuru göz kaldı. Karbamazepin ve diğer aromatik antiepileptikler alerji kaydına işlendi, aileye yazılı belge verildi."
                    },
                    {
                        "text": "Döküntü hafiflediğinde karbamazepini düşük dozda yeniden başlayıp tolere edip etmediğini görmek",
                        "is_correct": False,
                        "scenario_update": "Yeniden başlanan ilaçla birkaç saat içinde çok daha ağır bir reaksiyon gelişti.",
                        "teaching_point": "Sorumlu ilaç ömür boyu bir daha verilmez."
                    },
                    {
                        "text": "Bir hafta İV immünglobulin ve ardından altı hafta oral kortikosteroid tedavisi başlayıp ayaktan izlemek",
                        "is_correct": False,
                        "scenario_update": "Uzun steroid enfeksiyon riskini artırdı ve yara iyileşmesini geciktirdi.",
                        "teaching_point": "İmmünomodülatör tedaviler tartışmalıdır; temel tedavi destek bakımıdır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S95",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "2 Yaşında (12 kg)",
        "gender": "Erkek",
        "complaint": "Bilinen egzaması olan çocukta iki gündür yüzde ve boyunda hızla yayılan, içi su dolu yaralar ve yüksek ateş",
        "history": "Annesi anlatıyor: 'Bebekliğinden beri egzaması var, kortizonlu kremi kullanıyoruz. İki gün önce yüzünde küçük su toplamış kabarcıklar çıktı, egzama alevlendi sandık, kremi sıklaştırdık. Hızla yayıldı, patlayıp kabuklandı. Dünden beri ateşi 39.5, huzursuz, yemiyor.' Bir hafta önce babasının dudağında uçuk varmış ve çocuğu öpmüş. Suçiçeği aşısı yapılmış, kardeşlerde suçiçeği yok.",
        "final_diagnosis": "Ekzema Herpetikum (Kaposi Variselliform Erüpsiyonu - HSV-1)",
        "disposition": "İV Asiklovir, Göz Değerlendirmesi ve İkincil Bakteriyel Enfeksiyon Tedavisiyle Pediatri Servisine Yatış",
        "case_pearl": "Atopik dermatitli çocuklarda HSV'nin bozulmuş deri bariyeri üzerinde yaygınlaşmasıdır. Egzamanın alevlenmesi sanılıp gecikilebilir; tedaviye yanıtsız alevlenmede akla gelmelidir. Tek tip görünümlü, çukurlaşmış (göbekli) veziküller, 'zımbayla delinmiş' görünümlü yuvarlak erozyonlar ve hemorajik kabuklar tipiktir; ateş ve halsizlik eşlik eder. Tanı veziküllerden PCR ile doğrulanır. Ağır olgularda ve sistemik bulgu varsa İV asiklovir verilir. Göz çevresi tutulumunda keratit açısından acil göz muayenesi gerekir. İkincil stafilokok veya streptokok enfeksiyonu sıktır. Topikal kortikosteroid aktif lezyonlara sürülmez.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme",
                "question": "Egzaması olan, ateşli ve yaygın veziküllü yaraları olan bu çocukta ilk değerlendirmeniz nedir?",
                "options": [
                    {
                        "text": "Egzama alevlenmesi kabul edip daha güçlü kortikosteroidli krem ve antihistaminik önererek bir hafta sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Lezyonlar göz çevresine yayıldı ve çocuk ateşi süren, beslenemeyen halde getirildi.",
                        "teaching_point": "Ateşli, hızla yayılan veziküllü lezyonlarda viral enfeksiyon düşünülmeli, kortikosteroid artırılmamalıdır."
                    },
                    {
                        "text": "Genel durumu ve hidrasyonu değerlendirip lezyonların morfolojisini ve dağılımını incelemek; göz çevresi tutulumunu ve ikincil enfeksiyonu aramak",
                        "is_correct": True,
                        "explanation": "Lezyonların tek tip, göbekli ve zımbayla delinmiş görünümü tanıya yönlendirir. Göz çevresi tutulumu keratit riski taşır. Bal sarısı kabuklar ikincil bakteriyel enfeksiyonu düşündürür.",
                        "new_finding": "Ateş 39.4°C, KTA 146/dk, SS 30/dk, KB 96/60 mmHg, KDZ 2 sn. Huzursuz, mukozalar hafif kuru. Yüz, boyun ve üst göğüste egzamalı alanlar üzerinde kümeleşmiş, tek tip, 2-3 mm'lik göbekli veziküller; birçoğu patlamış, zımbayla delinmiş görünümlü yuvarlak erozyonlar ve hemorajik kabuklar. Yanakta bal sarısı kabuklu alanlar. Sağ alt göz kapağında veziküller, konjonktiva hafif hiperemik. Servikal lenfadenopati."
                    },
                    {
                        "text": "Lezyonları büllöz impetigo kabul edip yalnızca topikal mupirosinle tedavi edip ayaktan izlemek",
                        "is_correct": False,
                        "scenario_update": "Viral enfeksiyon tedavi edilmeden yaygınlaştı ve göz tutulumu gelişti.",
                        "teaching_point": "Bal sarısı kabuklar ikincil enfeksiyonu gösterebilir, ancak altta yatan viral süreç atlanmamalıdır."
                    },
                    {
                        "text": "Aşılı olmasına rağmen suçiçeği kabul edip ailenin çocuğu evde izole ederek izlemesini ve yalnızca ateş düşürücü vermesini önermek",
                        "is_correct": False,
                        "scenario_update": "Çocuk evde dehidrate oldu ve göz lezyonları ilerledi.",
                        "teaching_point": "Suçiçeğinde lezyonlar farklı evrelerde ve tüm vücuda yaygındır; burada lezyonlar egzamalı alanlarda kümelenmişti."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Bu çocukta hangi tetkikler en uygundur?",
                "options": [
                    {
                        "text": "Deri biyopsisi yapmak ve histopatoloji sonucu gelene kadar antiviral tedaviyi ertelemek",
                        "is_correct": False,
                        "scenario_update": "Biyopsi sonucu günler sürdü ve tedavi gecikti.",
                        "teaching_point": "Tanı vezikül sıvısından hızlı PCR ile konur; tedavi sonucu beklemeden başlanır."
                    },
                    {
                        "text": "Taze bir vezikülden virüs PCR'ı ve kabuklu alandan bakteri kültürü almak, kan sayımı ve kan kültürü göndermek",
                        "is_correct": True,
                        "explanation": "PCR tanıyı doğrular. Bakteri kültürü ikincil enfeksiyon etkenini gösterir. Yüksek ateşte kan kültürü bakteriyemiyi araştırır.",
                        "new_finding": "Vezikül sıvısında HSV-1 PCR pozitif. Kabuklu alandan alınan kültürde metisiline duyarlı S. aureus üredi. Lökosit 13.800/mm³, CRP 42 mg/L. Kan kültüründe üreme olmadı."
                    },
                    {
                        "text": "Alerjik bir reaksiyonu dışlamak için total IgE, geniş besin alerjen paneli ve deri prik testi istemek, sonuca göre tedavi seçmek",
                        "is_correct": False,
                        "scenario_update": "Testler tanıya katkı sağlamadı ve enfeksiyon tedavisi gecikti.",
                        "teaching_point": "Akut ateşli veziküler tabloda alerji testleri gereksizdir."
                    },
                    {
                        "text": "Yalnızca bakteri kültürü alıp sonuç gelene kadar oral sefaleksin başlamak ve virüs araştırması yapmamak",
                        "is_correct": False,
                        "scenario_update": "Bakteri tedavisine rağmen yeni veziküller çıkmaya devam etti.",
                        "teaching_point": "Asıl tablo viraldir; ikincil enfeksiyon tedavisi tek başına yeterli değildir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Ekzema herpetikum", "is_correct": True, "explanation": "Atopik dermatitli çocukta uçuklu bir yakınla temastan sonra egzamalı alanlarda kümelenen tek tip göbekli veziküller, zımbayla delinmiş erozyonlar, yüksek ateş ve HSV-1 PCR pozitifliği ekzema herpetikumu gösterir.", "new_finding": "Tanı: Ekzema herpetikum (Kaposi variselliform erüpsiyonu), ikincil stafilokok enfeksiyonu."},
                    {"text": "Atopik dermatit alevlenmesi", "is_correct": False, "scenario_update": "Lezyonlar veziküllü ve göbekliydi, yüksek ateş vardı ve PCR pozitifti.", "teaching_point": "Basit alevlenmede yüksek ateş ve göbekli veziküller beklenmez."},
                    {"text": "Suçiçeği (varisella)", "is_correct": False, "scenario_update": "Aşılıydı, lezyonlar egzamalı alanlarla sınırlı ve tek tipti.", "teaching_point": "Suçiçeğinde farklı evrelerde lezyonlar saçlı deri ve gövdeden başlayarak yayılır."},
                    {"text": "Eritema multiforme", "is_correct": False, "scenario_update": "Hedef lezyonlar yoktu, lezyonlar veziküler ve kümelenmişti.", "teaching_point": "Eritema multiformede tipik hedef lezyonlar el ve ayaklarda görülür."}
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Topikal asiklovir krem sürüp kortikosteroidli kremi sürdürmek ve ayaktan izlemek",
                        "is_correct": False,
                        "scenario_update": "Topikal tedavi yetersiz kaldı, kortikosteroid virüs yayılımını kolaylaştırdı.",
                        "teaching_point": "Yaygın ve sistemik bulgulu tabloda sistemik antiviral gerekir; aktif lezyonlara kortikosteroid sürülmez."
                    },
                    {
                        "text": "İV asiklovir ve stafilokoka etkili antibiyotik başlamak, acil göz muayenesi yaptırıp çocuğu yatırmak",
                        "is_correct": True,
                        "explanation": "Sistemik bulgulu ve yaygın tabloda İV asiklovir yayılımı durdurur. İkincil bakteriyel enfeksiyon tedavi edilir. Göz kapağı tutulumu keratit açısından değerlendirilmelidir.",
                        "new_finding": "İV asiklovir ve sefazolin başlandı. Oftalmoloji muayenesinde kornea tutulumu yoktu, profilaktik göz merhemi verildi. Ateş 48 saatte düştü, yeni vezikül çıkmadı. Beşinci günde oral tedaviye geçilerek taburcu edildi; egzama bakımı yeniden düzenlendi."
                    },
                    {
                        "text": "Yalnızca oral antibiyotik ve antihistaminik başlayıp lezyonlar kabuklanınca yeniden değerlendirmek üzere taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Antiviral verilmeyen çocukta lezyonlar yayıldı ve bakteriyemi gelişti.",
                        "teaching_point": "Viral etken tedavi edilmeden tablo kontrol altına alınamaz."
                    },
                    {
                        "text": "Sistemik kortikosteroid ve immünglobulin vererek bağışıklık yanıtını baskılamak ve ateşi izlemek",
                        "is_correct": False,
                        "scenario_update": "Kortikosteroid viral yayılımı artırdı ve tablo ağırlaştı.",
                        "teaching_point": "Sistemik kortikosteroid viral deri enfeksiyonunu ağırlaştırabilir."
                    }
                ]
            }
        ]
    }
]
