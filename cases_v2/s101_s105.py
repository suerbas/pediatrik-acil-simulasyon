# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - S101 - S102 (v2 Şartnamesine Uygun)
"""

CASES = [
    {
        "id": "S101",
        "category": "👂 Kulak Ağrısı & KBB",
        "age": "10 Yaşında (32 kg)",
        "gender": "Erkek",
        "complaint": "Sağ kulak önü ve çene köşesinde giderek büyüyen ağrılı şişlik, ağzını açarken artan ağrı, yemek yiyememe ve yüksek ateş",
        "history": "Gece 01:30'da annesiyle Sarı Alana getiriliyor. Annesi anlatıyor: 'Dün akşam sağ kulağının önü şişmeye başladı, gece iyice büyüdü. Ağzını tam açamıyor, çiğnerken ve bir şey yerken çok ağrıyor, akşam yemeğini yiyemedi. Ateşi 39 dereceye çıktı, parasetamol verdim. Geçen hafta üç gün ishal oldu, o günlerden beri az su içiyor. Diş ağrısından hiç şikâyet etmedi.' Aşı kartında KKK aşısının iki dozu tam. Okulunda benzer şişliği olan bilinen öğrenci yok. Kronik hastalığı ve ilaç alerjisi yok.",
        "final_diagnosis": "Sağ Akut Süpüratif (Bakteriyel) Parotit (Metisiline Duyarlı Staphylococcus aureus, Dehidratasyon Zemininde)",
        "disposition": "Sarı Alandan Servis Yatışı: İV Ampisilin-Sulbaktam, İV Hidrasyon, Sialogog, Sıcak Kompres ve Bez Masajı; Abse Açısından Ultrasonografi İzlemi",
        "case_pearl": "Çene köşesinde ağrılı şişlik ve trismusla gelen çocukta ayırıcı tanı muayeneyle büyük ölçüde yapılabilir. Parotis şişliği kulak önünden çene açısının altına uzanır, mandibula açısını siler ve kulak memesini yukarı-dışa iter; servikal lenf nodu ise açının altında, bezden ayrı ele gelir ve kulak memesini itmez. En değerli manevra, üst ikinci azı diş hizasındaki Stensen kanalı ağzına bakıp bezi masaj etmektir: pürülan akıntı bakteriyel parotiti gösterir, kabakulakta kanal ağzı kızarık olabilir ama tükürük berraktır. Kabakulak sıklıkla iki taraflıdır ve belirgin nötrofilik lökositoz yapmaz; amilaz her iki durumda da yükselebileceği için ayırımda işe yaramaz. Odontojenik apsede çürük, perküsyonla ağrıyan diş ve yanak/ağız tabanı şişliği öne çıkar. Bakteriyel parotitin en sık etkeni S. aureus'tur; dehidratasyon ve tükürük akımının azalması zemin hazırlar. Derleme kaynaklar süpüratif parotitte derin dokulara yayılım riski nedeniyle yatış ve İV antibiyotik önerir (anti-stafilokokal ve ağız anaerobunu kapsayan ampisilin-sulbaktam uygun bir seçenektir); hidrasyon, sialogog, sıcak kompres ve masaj tedavinin parçasıdır. İlk görüntüleme yöntemi ultrasonografidir. Salya akması, stridor, boyun hareket kısıtlılığı, tonsil veya farenks yan duvarının içe itilmesi, toksik görünüm ya da 48 saatte yanıtsızlık derin boyun enfeksiyonu açısından acil kontrastlı BT ve KBB konsültasyonu gerektirir.",
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Fizik Muayene",
                "question": "Gece yarısı sağ kulak önü ve çene köşesinde ağrılı şişlik, ağız açma kısıtlılığı ve 39°C ateşle getirilen 10 yaşındaki çocukta ilk muayene yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Aşı kartında iki doz KKK olduğu için viral nedeni dışlamak, şişliği dıştan palpe edip ateş düşürücü vermek ve sabah polikliniğe yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Ağız içi muayene yapılmadan eve gönderilen çocuk sabaha karşı ateşin 39.8°C'ye çıkması, şişliğin artması ve sıvı alamaması nedeniyle yeniden başvurdu.",
                        "teaching_point": "Tam aşılı çocukta da çene köşesi şişliğinin ayırıcı tanısı dış palpasyonla yapılamaz; ağız içi muayene, kanal ağızlarının incelenmesi ve diş muayenesi kilit adımlardır."
                    },
                    {
                        "text": "Hava yolu ve boyun hareketlerini değerlendirip şişliğin sınırlarını belirlemek; dişleri, tonsil simetrisini ve yanak mukozasındaki kanal ağzını bezi masaj ederek incelemek",
                        "is_correct": True,
                        "explanation": "Çene köşesi şişliği ve trismusta önce derin boyun enfeksiyonunun kırmızı bayrakları (salya, stridor, boyun kısıtlılığı, farenks yan duvarında itilme) aranır; ardından şişliğin anatomik sınırları, diş kaynağı ve kanal ağzından gelen salgının niteliği ayırıcı tanıyı büyük ölçüde belirler.",
                        "new_finding": "Vital Bulgular: Ateş 38.9°C, Nabız 118/dk, SS 20/dk, TA 108/66 mmHg, SpO2 %98. Genel durum orta, toksik görünüm yok; salya akması ve stridor yok, boyun hareketleri ağrılı ama serbest. Sağda kulak önünden mandibula açısının altına uzanan, açıyı silen ve kulak memesini yukarı-dışa iten, sert, sıcak, kızarık, çok hassas şişlik; fluktuasyon yok. Ağız açıklığı iki parmak. Sağ üst ikinci azı diş hizasındaki yanak mukozasında kanal ağzı ödemli ve kızarık; bez masajıyla kanal ağzından sarı-koyu kıvamlı akıntı geliyor. Dişlerde çürük ve perküsyon hassasiyeti yok, ağız tabanı yumuşak. Tonsiller simetrik, farenks yan duvarı itilmemiş. Sol taraf doğal, servikal bölgede ayrıca ele gelen lenf nodu yok. Mukozalar kuru."
                    },
                    {
                        "text": "Ağız açıklığı kısıtlı olduğundan ağız içi muayeneyi zorlamadan doğrudan kontrastlı boyun bilgisayarlı tomografisi istemek ve tedaviyi sonuca göre planlamak",
                        "is_correct": False,
                        "scenario_update": "Tomografi için sedasyon gerekti ve iki saat sürdü; sonuç gelene kadar ağız içinde kolayca görülebilecek akıntı ve kültür fırsatı değerlendirilmedi.",
                        "teaching_point": "Kırmızı bayrak yokken ilk adım dikkatli fizik muayenedir; kontrastlı BT derin boyun enfeksiyonu bulguları, hava yolu tehlikesi veya tedaviye yanıtsızlık durumunda istenir."
                    },
                    {
                        "text": "Ağrının çiğnemeyle artması nedeniyle çene ekleminden kaynaklandığını düşünüp eklemi muayene etmek, diş hekimine yönlendirip nonsteroid antiinflamatuvarla izlemek",
                        "is_correct": False,
                        "scenario_update": "Çene eklemi muayenesi olağan bulundu; ateşli ve sıvı alamayan çocuk ertesi gün diş hekiminden acil servise geri yönlendirildi.",
                        "teaching_point": "Ateş, sıcak-kızarık şişlik ve trismus enflamatuvar-enfeksiyöz bir süreci düşündürür; eklem sorunu gibi değerlendirmek tanıyı geciktirir."
                    }
                ]
            },
            {
                "stage_title": "Gece Tetkik ve Görüntüleme Kararı",
                "question": "Saat 02:00 ve ultrasonografi sabaha kadar yapılamıyor. Muayene bulguları saptanan bu çocukta hangi tetkik yaklaşımı en uygundur?",
                "options": [
                    {
                        "text": "Ayırımı kesinleştirmek için serum amilaz ve lipaz istemek; amilaz yüksek çıkarsa viral kökenli kabul edip destek tedavisiyle eve göndermek",
                        "is_correct": False,
                        "scenario_update": "Amilaz 310 U/L yüksek geldi ve viral kabul edildi; oysa kanal ağzından gelen akıntı kültüre gönderilmemiş, lökositoz ve CRP yüksekliği değerlendirilmemişti.",
                        "teaching_point": "Tükürük bezi enflamasyonunda amilaz viral ve bakteriyel nedenlerde benzer şekilde yükselebilir; ayırımda klinik muayene, akıntının niteliği ve inflamatuvar belirteçler belirleyicidir."
                    },
                    {
                        "text": "Gece ultrasonografi yapılamadığı için kontrastlı boyun tomografisi çekmek, abse saptanmazsa tedaviyi yalnızca sonuca göre planlayıp kültür almamak",
                        "is_correct": False,
                        "scenario_update": "Tomografide drene edilecek koleksiyon görülmedi; ancak kültür alınmadığı için etken ve duyarlılık bilgisi elde edilemedi.",
                        "teaching_point": "Derin boyun enfeksiyonu bulgusu olmayan çocukta ilk görüntüleme ultrasonografidir; BT kırmızı bayrak varlığında veya tedaviye yanıtsızlıkta tercih edilir."
                    },
                    {
                        "text": "Kızamık-kabakulak-kızamıkçık serolojisi göndermek, sonuç çıkana kadar okul izolasyonu önerip çocuğu eve göndermek ve üç gün sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Seroloji sonucu günler sonra çıkacaktı; ateşli, ağızdan beslenemeyen ve mukozaları kuru çocuk ertesi gün daha kötü durumda başvurdu.",
                        "teaching_point": "Serolojik testler akut yönetim kararını değiştirmez; pürülan akıntı, nötrofilik lökositoz ve dehidratasyon bulguları olan çocukta yatış değerlendirmesi gerekir."
                    },
                    {
                        "text": "Hemogram, CRP, elektrolitler ve kan kültürü almak; kanal ağzından gelen akıntıdan Gram boyama ve kültür göndermek, ultrasonografiyi en erken saatte planlamak",
                        "is_correct": True,
                        "explanation": "Kanal ağzından gelen akıntının Gram boyaması ve kültürü etkeni ve duyarlılığı gösterir; hemogram ve CRP bakteriyel enflamasyonu destekler, elektrolitler dehidratasyonu değerlendirir. Kırmızı bayrak yoksa abse araştırması için ultrasonografinin sabaha planlanması güvenlidir.",
                        "new_finding": "Lökosit 19.800/mm³ (%84 nötrofil), CRP 96 mg/L, Na 146 mEq/L, BUN 24 mg/dL, kreatinin 0.5 mg/dL, amilaz 310 U/L. Akıntının Gram boyamasında bol polimorf nüveli lökosit ve küme yapan Gram pozitif koklar görüldü; akıntı ve kan kültürü gönderildi. Ultrasonografi sabah 08:00'e planlandı."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Tek taraflı şişlik, kanal ağzından pürülan akıntı, nötrofilik lökositoz, yüksek CRP ve dehidratasyon zemini olan bu çocukta en olası tanı nedir?",
                "options": [
                    {
                        "text": "Kabakulak (viral parotit)",
                        "is_correct": False,
                        "scenario_update": "Kabakulak sıklıkla iki taraflıdır, kanal ağzı kızarık olsa da tükürük berraktır ve belirgin nötrofilik lökositoz beklenmez.",
                        "teaching_point": "Kanal ağzından pürülan akıntı viral parotitte görülmez; iki doz aşı da tanıyı uzaklaştırır."
                    },
                    {
                        "text": "Süpüratif servikal lenfadenit",
                        "is_correct": False,
                        "scenario_update": "Lenfadenit çene açısının altında, bezden ayrı bir kitle olarak ele gelir; kulak memesini itmez ve kanal ağzından akıntı yapmaz.",
                        "teaching_point": "Şişliğin mandibula açısını silmesi ve kulak memesini itmesi bezin kendisinin tutulduğunu gösterir."
                    },
                    {
                        "text": "Akut süpüratif (bakteriyel) parotit",
                        "is_correct": True,
                        "explanation": "Tek taraflı ağrılı parotis şişliği, Stensen kanalından pürülan akıntı, Gram pozitif kok kümeleri, nötrofilik lökositoz ve dehidratasyon zemini akut süpüratif parotit tanısını koydurur.",
                        "new_finding": "Tanı: Sağ akut süpüratif (bakteriyel) parotit. Trismus bezin ve çiğneme kaslarının enflamasyonuna bağlı; derin boyun enfeksiyonu bulgusu yok."
                    },
                    {
                        "text": "Odontojenik bukkal boşluk apsesi",
                        "is_correct": False,
                        "scenario_update": "Odontojenik apsede çürük veya perküsyonla ağrıyan bir diş, yanak ya da ağız tabanında şişlik beklenir; bu çocuğun dişleri sağlam.",
                        "teaching_point": "Diş muayenesi normal ve akıntının kaynağı tükürük kanalı olduğunda öncelikli tanı tükürük bezi enfeksiyonudur."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış Kararı",
                "question": "Akut süpüratif parotit tanısı alan, trismusu olan, ağızdan beslenemeyen ve hafif dehidrate bu çocukta en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Oral amoksisilin-klavulanat ile ayaktan tedavi verip bol sıvı ve ekşi şeker önermek, sabah ultrasonografi ve kontrol için yeniden başvurmasını istemek",
                        "is_correct": False,
                        "scenario_update": "Trismus nedeniyle ilaçlarını ve sıvıyı yeterince alamayan çocuk ertesi gün daha belirgin dehidratasyon ve artan şişlikle başvurdu.",
                        "teaching_point": "Derleme kaynaklar süpüratif parotitte derin dokulara yayılım riski nedeniyle yatış ve İV antibiyotik önerir; özellikle ağızdan beslenemeyen ve dehidrate çocukta ayaktan oral tedavi yetersiz kalabilir."
                    },
                    {
                        "text": "Servise yatırıp İV ampisilin-sulbaktam 200 mg/kg/gün (ampisilin bileşeni, 4 dozda) başlamak; İV sıvı, analjezi, sialogog, sıcak kompres ve masajla izlemek",
                        "is_correct": True,
                        "explanation": "En sık etken S. aureus olup streptokoklar ve ağız anaerobları da rol oynar; ampisilin-sulbaktam bunları kapsar (doz 100-200 mg/kg/gün ampisilin bileşeni, 6 saatte bir, en fazla 8 g/gün ampisilin). Hidrasyon, tükürük akımını artıran sialogoglar, sıcak kompres ve bez masajı drenajı kolaylaştırır; abse ultrasonografiyle izlenir.",
                        "new_finding": "Sabah ultrasonografisi: Sağ bez difüz büyümüş, heterojen ve hipervasküler; drene edilecek koleksiyon yok. Kültürde metisiline duyarlı S. aureus üredi. 48. saatte ateş düştü, ağız açıklığı arttı ve ağızdan beslenmeye başladı; 72. saatte kültür duyarlılığına göre oral tedaviye geçilerek taburcu edildi ve kontrol planlandı."
                    },
                    {
                        "text": "Yatırıp tek başına İV seftriakson başlamak, sıvı alımını sınırlamak ve bez masajıyla tükürük uyarıcılarını enfeksiyonu yayabileceği gerekçesiyle önermemek",
                        "is_correct": False,
                        "scenario_update": "Sıvısı kısıtlanan çocukta tükürük akımı daha da azaldı ve şişlik 48 saatte belirgin gerilemedi; kültürde üreyen etken için anti-stafilokokal kapsam yetersiz kaldı.",
                        "teaching_point": "Tedavi anti-stafilokokal ve anaerob kapsamlı antibiyotikle birlikte hidrasyon, sialogog ve masajı içerir; tükürük akımını azaltan yaklaşımlar staza ve iyileşmenin gecikmesine yol açar."
                    },
                    {
                        "text": "Fluktuasyon olmasa da trismus nedeniyle acil serviste iğne aspirasyonu ve insizyonla drenaj yapmak, ardından oral antibiyotikle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Kör aspirasyonda pürülan materyal gelmedi; işlem sonrası ağrı ve şişlik arttı, çocuk yine yatırılmak zorunda kalındı.",
                        "teaching_point": "Cerrahi veya ultrasonografi eşliğinde drenaj, görüntülemede abse gösterildiğinde ya da uygun tedaviye yanıt alınamadığında düşünülür; kör girişim yüz siniri komşuluğu nedeniyle de risklidir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S102",
        "category": "🦴 Kas-İskelet & Eklem / Ortopedik Aciller",
        "age": "3 Yaşında (14 kg)",
        "gender": "Erkek",
        "complaint": "Dünden beri sol bacağına basmama, bez değişiminde bacağı oynatılınca ağlama, gece ağrıyla uyanma ve yüksek ateş",
        "history": "Annesi anlatıyor: 'Bir hafta önce burun akıntısı ve öksürüğü oldu, geçti sanıyorduk. Dün öğleden sonra sol bacağına basmak istemedi, sürekli kucağa geldi. Gece ateşi 39.4 dereceye çıktı, ağlayarak uyandı. Bezini değiştirirken bacağını oynatınca çığlık atıyor. Dizini gösteriyor.' Düşme veya darbe olmamış. Aşıları tam, kronik hastalığı yok. Daha önce benzer şikâyeti olmamış.",
        "final_diagnosis": "Sol Kalça Septik Artriti (Metisiline Duyarlı Staphylococcus aureus)",
        "disposition": "Sarı Alandan Acil Ortopedi Konsültasyonu, Ameliyathanede Eklem Drenajı ve İV Sefazolin ile Servis Yatışı",
        "case_pearl": "Ateşli ve basamayan küçük çocukta kalça septik artriti cerrahi bir acildir; kalça eklemi içindeki basınç femur başı kanlanmasını bozarak avasküler nekroza yol açabilir. Kalça ağrısı sıklıkla dize yansır; bu nedenle 'dizini gösteren' çocukta kalça mutlaka muayene edilmelidir. Kocher kriterleri (basamama, ateş >38.5°C, ESH >40 mm/saat, lökosit >12.000/mm³) geçici sinovitten ayırımda yol gösterir: bir kriterde olasılık yaklaşık %3, iki kriterde %40, üç kriterde %93, dördünde %99'dur; Caird CRP >2 mg/dL'yi ek öngörücü olarak tanımlamıştır. Bu kriterlerin doğrulaması tartışmalıdır ve kısmen tedavi edilmiş çocukta normal belirteçler tanıyı dışlamaz. Ultrasonografi eklem içi sıvıyı gösterir; kesin tanı eklem sıvısı incelemesi ve kültürle konur. Hemodinamik durum izin veriyorsa kan kültürü ve eklem sıvısı alındıktan hemen sonra antibiyotik başlanmalıdır. PIDS/IDSA 2023 kılavuzu ampirik tedavinin S. aureus'u hedeflemesini ve 6-48 ay arası çocuklarda Kingella kingae'nin kapsanmasını önerir; sefazolin bu iki etkeni kapsar, klindamisin ise Kingella'ya etkisizdir. Hastane protokollerinde sefazolin 100-120 mg/kg/gün, 8 saatte bir (doz başı en fazla 2 g) kullanılır; oral tedaviye geçiş ve toplam süre klinik yanıt ve CRP gerilemesine göre çocuk enfeksiyon hastalıklarıyla planlanır.",
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Fizik Muayene",
                "question": "Bir gündür sol bacağına basmayan, ateşli ve annesine dizini gösteren 3 yaşındaki çocukta ilk muayene yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Çocuk dizini gösterdiği için dizi ayrıntılı muayene etmek, iki yönlü diz grafisi istemek ve grafi normal çıkarsa ibuprofenle eve göndermek",
                        "is_correct": False,
                        "scenario_update": "Diz muayenesi ve grafisi normal bulundu; eve gönderilen çocuk ertesi gün yüksek ateş ve bacağını hiç oynatamama ile yeniden getirildi.",
                        "teaching_point": "Küçük çocuklarda kalça ağrısı sıklıkla dize yansır; basamayan çocukta kalça, diz, ayak bileği, omurga ve deri sırayla muayene edilmelidir."
                    },
                    {
                        "text": "Bir hafta önceki üst solunum yolu enfeksiyonunu öne çıkarıp viral kökenli bir eklem enflamasyonu kabul etmek, ibuprofen verip kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "İbuprofen ateşi geçici olarak düşürdü ve ağrıyı maskeledi; tanı 24 saat gecikti ve eklem içi basınç bu sürede arttı.",
                        "teaching_point": "Yüksek ateş ve tam basamama, geçici sinovitten çok daha ciddi bir enfeksiyonu düşündürür; antiinflamatuvar ilaçla izlem kararı tetkikler sonuçlanmadan verilmemelidir."
                    },
                    {
                        "text": "Bacağın tutuluş pozisyonunu, kalçanın iç-dış rotasyon ve abdüksiyonunu, diz-ayak bileği, omurga ve deriyi sırayla muayene edip basmayı gözlemek",
                        "is_correct": True,
                        "explanation": "Basamayan ateşli çocukta yansıyan ağrı sık olduğundan tüm alt ekstremite ve omurga sistematik muayene edilir; kalçanın fleksiyon-abdüksiyon-dış rotasyonda tutulması ve iç rotasyonda şiddetli ağrı eklem içi sıvı ve basınç artışını düşündürür.",
                        "new_finding": "Vital Bulgular: Ateş 39.1°C, Nabız 140/dk, SS 28/dk, TA 96/60 mmHg, SpO2 %99, kapiller dolum 2 sn. Huzursuz ama toksik görünümlü değil. Sol kalça fleksiyon, abdüksiyon ve dış rotasyonda tutuluyor; pasif iç rotasyon ve ekstansiyonda şiddetli ağrı var, bacak yatakta yuvarlanınca ağlıyor. Basmayı tamamen reddediyor. Diz, ayak bileği, omurga muayenesi ve deri doğal; döküntü, lenfadenopati ve organomegali yok."
                    },
                    {
                        "text": "Ağrılı çocuğu yormadan muayeneyi kısa tutmak, sedasyon altında aynı gece pelvis manyetik rezonans görüntülemesi planlayıp sonuç gelene kadar beklemek",
                        "is_correct": False,
                        "scenario_update": "MR için sedasyon ve görüntüleme sırası saatler aldı; bu sürede kan kültürü alınmadı ve ortopediye haber verilmedi.",
                        "teaching_point": "İlk basamak sistematik fizik muayene, kan tetkikleri ve kalça ultrasonografisidir; MR, osteomiyelit veya komşu odak şüphesinde ilk değerlendirmeyi geciktirmeyecek şekilde planlanır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik ve Görüntüleme Stratejisi",
                "question": "Sol kalçada hareket kısıtlılığı ve şiddetli rotasyon ağrısı saptanan ateşli bu çocukta bir sonraki adımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Hemogram, eritrosit sedimantasyon hızı, CRP ve kan kültürü almak; kalça ultrasonografisiyle eklem içi sıvıyı değerlendirip ortopediyi erkenden bilgilendirmek",
                        "is_correct": True,
                        "explanation": "Eklem içi sıvı ultrasonografiyle hızla gösterilir; lökosit, ESH, CRP ve ateş birlikte değerlendirilerek enfeksiyon olasılığı tahmin edilir. Kan kültürü antibiyotik öncesi alınır ve olası drenaj için ortopedi erken çağrılır.",
                        "new_finding": "Lökosit 18.600/mm³ (%78 nötrofil), ESH 52 mm/saat, CRP 11.4 mg/dL (114 mg/L). Kan kültürü alındı. Kalça ultrasonografisi: Sol kalça ekleminde anterior kapsülü 7 mm uzaklaştıran, ince ekojen partiküller içeren efüzyon; sağ kalçada 2 mm fizyolojik sıvı. Ortopedi bilgilendirildi."
                    },
                    {
                        "text": "Pelvis ön-arka grafisi çekmek; kemikte yapısal değişiklik yoksa ibuprofen başlayıp 48 saat sonra klinik ve laboratuvar kontrolüyle yeniden değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Grafide kemik değişikliği izlenmedi ve hasta izleme alındı; 48 saat sonra yapılan değerlendirmede eklem içi basınç artmış ve ateş sürmüştü.",
                        "teaching_point": "Erken dönemde direkt grafi çoğunlukla normaldir ve eklem içi sıvıyı göstermez; ateşli basamayan çocukta kalça ultrasonografisi ve inflamatuvar belirteçler gereklidir."
                    },
                    {
                        "text": "Hasta ateşli olduğu için tetkik sonuçlarını beklemeden önce İV antibiyotik başlamak, kan kültürü ve diğer tetkikleri antibiyotikten sonra göndermek",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik sonrası alınan kan kültürü ve daha sonra alınan eklem sıvısı kültüründe üreme olmadı; etken ve duyarlılık belirlenemedi.",
                        "teaching_point": "Hemodinamik olarak stabil çocukta kültürler (kan ve mümkünse eklem sıvısı) antibiyotikten önce alınmalı, ancak bu işlem antibiyotiği uzun süre geciktirmemelidir."
                    },
                    {
                        "text": "Yalnızca hemogram ve CRP istemek; değerler sınırda çıkarsa görüntüleme yapmadan geçici bir enflamasyon kabul edip yatak istirahatiyle izlemek",
                        "is_correct": False,
                        "scenario_update": "Lökosit ve CRP yüksek bulunmasına rağmen görüntüleme yapılmadı; eklem içi sıvının niteliği ve miktarı bilinmeden izleme kararı verildi.",
                        "teaching_point": "Laboratuvar değerleri tek başına ayırım yapmaz; eklem içi sıvının gösterilmesi ve gerekirse aspirasyonu tanı için esastır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Ateş 39.1°C, tam basamama, lökosit 18.600/mm³, ESH 52 mm/saat, CRP 11.4 mg/dL ve sol kalçada efüzyon saptanan bu çocukta en olası tanı nedir?",
                "options": [
                    {
                        "text": "Geçici (toksik) sinovit",
                        "is_correct": False,
                        "scenario_update": "Geçici sinovitte çocuk genellikle ateşsiz veya hafif ateşlidir, kısmen basabilir ve inflamatuvar belirteçler normale yakındır.",
                        "teaching_point": "Dört Kocher kriterinin tümünün ve CRP >2 mg/dL'nin varlığı geçici sinovitten çok septik artriti destekler."
                    },
                    {
                        "text": "Sol kalça septik artriti",
                        "is_correct": True,
                        "explanation": "Basamama, ateş >38.5°C, ESH >40 mm/saat ve lökosit >12.000/mm³ ile dört Kocher kriterinin tümü ve CRP >2 mg/dL mevcut; ultrasonografide ekojen efüzyon septik artrit olasılığını çok yüksek kılar. Kesin tanı eklem sıvısı incelemesiyle konur.",
                        "new_finding": "Ön tanı: Sol kalça septik artriti (4/4 Kocher kriteri, CRP 11.4 mg/dL)."
                    },
                    {
                        "text": "Proksimal femur akut osteomiyeliti",
                        "is_correct": False,
                        "scenario_update": "Osteomiyelit eşlik edebilir ve MR ile araştırılabilir; ancak ultrasonografide belirgin eklem içi efüzyon ve şiddetli rotasyon ağrısı öncelikle eklem enfeksiyonunu gösterir.",
                        "teaching_point": "Kalçada septik artrit ile komşu osteomiyelit birlikte olabilir; drenaj sonrası yanıt yetersizse MR ile değerlendirilir."
                    },
                    {
                        "text": "Legg-Calvé-Perthes hastalığı",
                        "is_correct": False,
                        "scenario_update": "Perthes hastalığı daha sinsi başlar, ateş ve belirgin inflamatuvar yanıt beklenmez; tipik olarak 4-8 yaş arasında görülür.",
                        "teaching_point": "Ani başlangıç, yüksek ateş ve yüksek akut faz yanıtı avasküler süreçten çok enfeksiyonu düşündürür."
                    }
                ]
            },
            {
                "stage_title": "Acil Tedavi ve Yönlendirme",
                "question": "Sol kalça septik artriti düşünülen 3 yaşındaki bu çocukta en uygun tedavi yaklaşımı hangisidir?",
                "options": [
                    {
                        "text": "İV klindamisin 40 mg/kg/gün tek başına başlamak, eklem drenajı kararını 48 saatlik antibiyotik yanıtına göre vermek üzere çocuğu servise yatırmak",
                        "is_correct": False,
                        "scenario_update": "Drenajı ertelenen kalçada 48 saatte ateş sürdü; eklem sıvısı kültüründe Kingella kingae üredi ve klindamisinin bu etkene etkisiz olduğu anlaşıldı.",
                        "teaching_point": "Kalça septik artriti acil drenaj gerektirir; PIDS/IDSA 2023, 6-48 ay arası çocuklarda Kingella kingae'nin kapsanmasını önerir ve klindamisin bu etkeni kapsamaz."
                    },
                    {
                        "text": "Ağrıyı kontrol edip oral sefaleksinle ayaktan tedavi başlamak, 48 saat sonra ultrasonografi ve CRP kontrolü için çocuk ortopedi polikliniğine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Evde ateşi sürdü ve çocuk bacağını hiç oynatamaz hale geldi; ikinci başvuruda eklem içi basınç artışı nedeniyle femur başı kanlanması risk altındaydı.",
                        "teaching_point": "Kalça septik artriti ayaktan tedavi edilmez; eklem drenajı ve İV antibiyotikle yatış gerekir."
                    },
                    {
                        "text": "Ortopediyle acil eklem aspirasyonu ve drenajı planlayıp, eklem sıvısı ve kan kültürü alındıktan hemen sonra İV sefazolin 100 mg/kg/gün üç dozda başlamak",
                        "is_correct": True,
                        "explanation": "Kalça eklemi içindeki basınç femur başı kanlanmasını tehdit ettiğinden acil drenaj gerekir. Ampirik tedavi S. aureus ve bu yaş grubunda Kingella kingae'yi kapsamalıdır; sefazolin her ikisini kapsar (hastane protokollerinde 100-120 mg/kg/gün, 8 saatte bir, doz başı en fazla 2 g).",
                        "new_finding": "Ultrasonografi eşliğinde aspirasyonda bulanık sinovyal sıvı geldi: lökosit 86.000/mm³, %90 nötrofil, Gram boyamada Gram pozitif koklar. Ameliyathanede artrotomi ve eklem yıkaması yapıldı. Kültürde metisiline duyarlı S. aureus üredi. 72. saatte ateş düştü ve CRP geriledi; oral tedaviye geçiş ve toplam süre çocuk enfeksiyon hastalıklarıyla planlandı."
                    },
                    {
                        "text": "Yatak istirahati ve ibuprofenle 24 saat izleyip yanıt yoksa aspirasyon yapmak, bu sürede antibiyotiği kültür sonucuna kadar ertelemek",
                        "is_correct": False,
                        "scenario_update": "24 saatlik izlemde ateş ve ağrı geriledi gibi görünse de antiinflamatuvar etki enfeksiyonu maskeledi; drenaj ve antibiyotik bir gün gecikti.",
                        "teaching_point": "Bu yaklaşım geçici sinovit için uygundur; septik artrit olasılığı yüksek çocukta drenaj ve antibiyotik geciktirilmemelidir."
                    }
                ]
            }
        ]
    }
]
