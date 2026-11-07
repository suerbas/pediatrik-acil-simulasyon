# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - Y36-Y40 (v2 Şartname ve Doğrulama Uyumlu)
Y37, Y38, Y39, Y40 vakaları Yeşil Alana başvurup muayenede saptanan kritik bulgular nedeniyle
1. Adımda Sarı Alana devredilerek yönetimine Sarı Alanda devam edilen vakalardır.
"""

CASES = [
    {
        "id": "Y36",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "5 Yaş",
        "gender": "Erkek",
        "complaint": "Akşamları ve gece uykudan uyandıran iki taraflı bacak ağrısı",
        "history": (
            "Annesi anlatıyor: 'Oğlum son 2 aydır haftada 2-3 gece bacaklarım sızlıyor diyerek "
            "ağlayarak uyanıyor. Her iki kaval kemiği ve baldırlarını ovmamızı istiyor, masaj yapınca "
            "rahatlayıp tekrar uykuya dalıyor. Sabah kalktığında ise hiçbir şeyi kalmıyor, gün boyu "
            "kreşte koşturup oynuyor. Gündüz hiç topallamıyor, eklemlerinde şişlik veya kızarıklık "
            "olmadı. Bu gece ağrısı çok şiddetlenince endişelenip acile getirdik.'"
        ),
        "final_diagnosis": "Büyüme Ağrıları (Benign Noktürnal Ekstremite Ağrısı)",
        "disposition": "Yeşil Alandan Aileye Güvence, Masaj/Sıcak Uygulama Eğitimi ve Rutin Poliklinik Önerisi ile Taburculuk",
        "case_pearl": (
            "Tipik olarak 3-12 yaş arası çocuklarda görülen büyüme ağrıları (benign noktürnal "
            "ekstremite ağrısı), akşam veya gece ortaya çıkan, iki taraflı, derin sızlayıcı, eklemleri "
            "tutmayan ve sabah tamamen kaybolan ağrılardır. Gündüz ağrı olmaması, topallama veya "
            "fizik muayenede lokalize şişlik/hassasiyet/kızarıklık bulunmaması ve sistemik bulgu "
            "(ateş, kilo kaybı) olmaması benign niteliği gösterir; tetkiksiz izlem esastır, aile "
            "güvencesi, lokal masaj ve sıcak uygulama yeterlidir."
        ),
        "steps": [
            {
                "stage_title": "Fizik ve Lokomotor Sistem Muayenesi",
                "question": "Gece uykudan uyandıran iki taraflı bacak ağrısıyla Yeşil Alana getirilen 5 yaşındaki bu çocukta fizik muayenede öncelikle ne yapmalısınız?",
                "options": [
                    {
                        "text": "Ağrının nöropatik bası kaynaklı olabileceğini düşünerek lumbosakral vertebraları palpe etmek, alt ekstremite derin tendon reflekslerini ve duyu seviyesini ayrıntılı incelemek",
                        "is_correct": False,
                        "scenario_update": "Lumbosakral omurga ve nörolojik muayene tamamen doğal bulundu; ancak alt ekstremite eklemleri ve kemik yapıları değerlendirilmediği için organik patolojiler dışlanamadı.",
                        "teaching_point": "İki taraflı bacak ağrısı olan çocukta öncelikle eklemler, kemikler ve kas grupları doğrudan muayene edilerek lokal inflamasyon, efüzyon ve hassasiyet araştırılmalıdır.",
                    },
                    {
                        "text": "Alt ekstremite eklemlerinin hareket açıklığını, tibia ve baldır kaslarını palpasyonla, yürüyüş paternini ve bölgesel eritem veya ödem varlığını detaylı incelemek",
                        "is_correct": True,
                        "explanation": "Çocuklarda gece gelen ekstremite ağrılarında ilk adım; artrit, osteomiyelit veya maligniteyi dışlamak için eklem hareket açıklığı, kemik hassasiyeti ve yürüyüş muayenesini yapmaktır.",
                        "new_finding": "Vital Bulgular: Ateş 36.6°C, KTA 92/dk. Her iki diz, ayak bileği ve kalça eklemlerinde hareket açıklığı tam ve ağrısız; efüzyon, ısı artışı veya eritem yok. Tibia ve baldır kaslarında hassasiyet saptanmadı. Yürüyüş paterni simetrik ve normal; topallama yok. Sistemik muayene ve lenf nodu değerlendirmesi doğal.",
                    },
                    {
                        "text": "Ağrının derin ven trombozuna bağlı olabileceğini varsayarak her iki baldır çapını mezura ile ölçmek ve acil kompresyon ultrasonografisi planlayarak çocuğu Sarı Alana almak",
                        "is_correct": False,
                        "scenario_update": "Baldır çapları simetrik bulundu ve tromboz risk faktörü olmayan çocuk gereksiz yere ileri acil alanına devredildi.",
                        "teaching_point": "Önceden sağlıklı, travma veya santral kateter öyküsü olmayan bir çocukta iki taraflı gece ağrısı derin ven trombozu lehine değildir; Sarı Alana devir gerekmez.",
                    },
                    {
                        "text": "Muayeneyi yalnızca çocuğun bacaklarını görsel olarak incelemekle sınırlı tutup ağrıyı psikolojik kökenli kabul ederek aileye çocuk psikiyatrisi randevusu almalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Eklemler ve kemik yapıları palpe edilmeden yapılan yüzeysel değerlendirme olası organik patolojilerin atlanma riskini doğurdu ve aileyi tedirgin etti.",
                        "teaching_point": "Geceleri çocuğu uykudan uyandıran ağrılarda fizik muayene ve lokomotor sistem muayenesi eksiksiz yapılmadan fonksiyonel veya psikolojik etiketleme yapılmamalıdır.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Laboratuvar İstem Kararı",
                "question": "Gündüz tamamen asemptomatik olan, fizik muayenesi normal bulunan ve alarm bulgusu taşımayan bu çocukta yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Kemik kaynaklı primer tümör veya lösemiyi ekarte etmek amacıyla her iki kruris iki yönlü direkt radyografisi ve periferik yayma tetkikleri istemek",
                        "is_correct": False,
                        "scenario_update": "Radyografilerde periost reaksiyonu veya litik lezyon izlenmedi; periferik yayma normal bulundu ancak çocuk gereksiz radyasyon aldı ve ailesi aşırı kaygılandı.",
                        "teaching_point": "Lokalize kemik hassasiyeti, tek taraflı tutulum, gündüz ağrısı, kilo kaybı ve gece terlemesi olmayan tipik noktürnal ağrılarda rutin radyografi veya yayma gerekmez.",
                    },
                    {
                        "text": "İnflamatuar eklem hastalığını dışlamak amacıyla tam kan sayımı, eritrosit sedimentasyon hızı, C-reaktif protein, romatoid faktör ve antinükleer antikor paneli istemek",
                        "is_correct": False,
                        "scenario_update": "Laboratuvar sonuçları: Hemoglobin 12.8 g/dL, Lökosit 7.200/mm³, CRP 0.8 mg/L, ESH 6 mm/saat, ANA negatif çıktı; çocuğa gereksiz invaziv damar yolu işlemi uygulandı.",
                        "teaching_point": "Ateş, eklemde şişlik, hareket kısıtlılığı veya sabah tutukluğu olmayan tipik iki taraflı ağrılarda romatolojik otoantikor ve akut faz reaktanları paneli istenmez.",
                    },
                    {
                        "text": "Öykü ve fizik muayene tipik benign noktürnal paterni desteklediği ve alarm bulgusu bulunmadığı için ek radyolojik veya biyokimyasal tetkik istememek",
                        "is_correct": True,
                        "explanation": "Tipik klinik prezentasyonda (iki taraflı, akşam/gece gelen, sabah kaybolan, gündüz aktivitesi ve muayenesi doğal) tanı tamamen kliniktir; hiçbir laboratuvar veya görüntüleme tetkiki gerekmez.",
                        "new_finding": "Ek laboratuvar veya görüntüleme tetkiki istenmedi. Öykü ve fizik muayene bulgularıyla tanısal değerlendirmeye geçildi.",
                    },
                    {
                        "text": "Eklem içi kıkırdak hasarı ve erken evre sinoviti değerlendirmek amacıyla her iki diz eklemine yönelik kontrastlı manyetik rezonans görüntüleme randevusu planlamak",
                        "is_correct": False,
                        "scenario_update": "Sedasyon gerektiren pahalı ve ileri düzey görüntüleme randevusu planlandı; ancak muayenesi doğal çocukta gereksiz sağlık kaynağı tüketimine yol açtı.",
                        "teaching_point": "Eklem efüzyonu, hareket kısıtlılığı veya inflamasyon belirtisi olmayan, ağrısı baldır ve kaval kemiğinde lokalize çocuklarda manyetik rezonans görüntüleme kesinlikle endike değildir.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik öykü ve normal fizik muayene bulguları ışığında bu hastadaki en olası tanı hangisidir?",
                "options": [
                    {
                        "text": "Büyüme Ağrıları (Benign Noktürnal Ekstremite Ağrısı)",
                        "is_correct": True,
                        "explanation": "3-12 yaş arasında akşam veya gece uykudan uyandıran, her iki bacakta sızlama yapan, masajla rahatlayan ve sabah tamamen düzelen tablo tipik büyüme ağrısıdır.",
                        "new_finding": "Kesin Tanı: Büyüme Ağrıları (Benign Noktürnal Ekstremite Ağrısı).",
                    },
                    {
                        "text": "Juvenil İdiyopatik Artrit (Oligoartiküler Tip)",
                        "is_correct": False,
                        "scenario_update": "Hastada eklemde şişlik, sabah tutukluğu veya hareket kısıtlılığı bulunmamaktadır; ağrı eklemde değil kas-kemik derin dokusundadır.",
                        "teaching_point": "Juvenil idiyopatik artrit eklemde efüzyon, ısı artışı ve en az 6 hafta süren sabah tutukluğu ile karakterizedir; gece masajla geçen ağrılarla seyretmez.",
                    },
                    {
                        "text": "Akut Geçici Sinovit (Toksik Sinovit)",
                        "is_correct": False,
                        "scenario_update": "Hastada kalça eklemi tutulumu, topallama veya eklem hareketinde ağrılı kısıtlılık saptanmamıştır; ağrı iki taraflı baldır-kaval bölgesindedir.",
                        "teaching_point": "Geçici sinovit genellikle tek taraflı kalça ağrısı ve belirgin topallama ile acile başvurur; iki taraflı baldır sızlaması şeklinde görülmez.",
                    },
                    {
                        "text": "Akut Hematatojen Osteomiyelit (Tibia Enfeksiyonu)",
                        "is_correct": False,
                        "scenario_update": "Hastanın ateşi yoktur, kemik üzerinde fokal palpasyon hassasiyeti, eritem veya basamama tablosu bulunmamaktadır.",
                        "teaching_point": "Akut osteomiyelitte ateş, tek taraflı lokalize şiddetli kemik hassasiyeti, üzerine basamama ve laboratuvarda yüksek akut faz reaktanları tipiktir.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Aile Eğitimi Planı",
                "question": "Benign noktürnal ekstremite ağrısı saptanan ve alarm bulgusu bulunmayan bu hastanın acil servis yönetimi ve taburculuk planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Ağrı ataklarının kalsiyum ve D vitamini eksikliğine bağlı olduğunu belirterek tetkik yapmadan yüksek doz intramüsküler D vitamini ampulü uygulamak ve taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Büyüme ağrılarının D vitamini veya kalsiyum eksikliğiyle doğrudan ilişkisi kanıtlanmamıştır; kontrolsüz yüksek doz vitamin uygulaması hiperkalsemi ve toksisite riski oluşturdu.",
                        "teaching_point": "Büyüme ağrıları vitamin eksikliğine bağlı değildir; ampirik yüksek doz D vitamini vermek hatalı ve toksisite açısından tehlikeli bir yaklaşımdır.",
                    },
                    {
                        "text": "Atak sıklığını azaltmak amacıyla her gece yatmadan önce düzenli olarak bir ay boyunca oral ibuprofen şurup içmesini ve spordan uzak durmasını önermek",
                        "is_correct": False,
                        "scenario_update": "Her gece profilaktik NSAİİ kullanımı çocukta gastrit ve gastrointestinal kanama riskini artırdı; ayrıca gereksiz fiziksel aktivite kısıtlaması çocuğun gelişimini olumsuz etkiledi.",
                        "teaching_point": "Büyüme ağrılarında her gece düzenli koruyucu analjezik verilmez ve fiziksel aktivite kısıtlanmaz; analjezikler yalnızca şiddetli atağın olduğu anlarda kullanılır.",
                    },
                    {
                        "text": "Bacak kaslarını gevşetmek amacıyla oral santral etkili kas gevşetici reçete etmek ve olası maligniteleri dışlamak için üç gün sonra acil servise kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Pediatrik yaş grubunda endikasyonu olmayan santral kas gevşetici çocukta aşırı sedasyon ve hipotoniye yol açtı; acil servis tekrar başvurusu aile kaygısını artırdı.",
                        "teaching_point": "Çocuklarda benign noktürnal ağrılarda santral kas gevşeticilerin yeri yoktur; taburculuk sonrası kontrol acil serviste değil gereğinde pediatri polikliniğinde yapılır.",
                    },
                    {
                        "text": "Aileyi durumun iyi huylu olduğu konusunda rahatlatmak, ataklarda lokal masaj, ılık kompres ve gerektiğinde parasetamol önermek, gündüz semptomu olursa polikliniğe yönlendirmek",
                        "is_correct": True,
                        "explanation": "Büyüme ağrılarının temel tedavisi ailenin rahatlatılması (güvence), atak sırasında bacak masajı, ılık uygulama ve gerekirse basit analjeziktir. Gündüz ağrısı veya topallama gibi kırmızı bayraklar gelişirse poliklinik kontrolü önerilir.",
                        "new_finding": "Aileye benign gidişat anlatılarak güven verildi; masaj, sıcak uygulama ve kırmızı bayrak eğitimi verilerek hasta Yeşil Alandan taburcu edildi.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y37",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "8 Yaş",
        "gender": "Kız",
        "complaint": "Karın ağrısı ve hafif ateş",
        "history": (
            "Annesi 8 yaşındaki kızını Yeşil Alana getiriyor: 'Kızım yaklaşık 1 hafta önce boğaz "
            "enfeksiyonu geçirmişti, ateşi ve boğaz ağrısı vardı, şurupla düzeldi. Ancak dün akşamdan "
            "beri göbek çevresinde ve karnının sağ alt tarafında sızlayıcı bir ağrı başladı. Sabah ateşi "
            "37.8°C ölçüldü. İştahı azaldı ama hiç kusmadı ve ishali olmadı. Yürürken karnını tutuyor.'"
        ),
        "final_diagnosis": "Akut Mezenterik Lenfadenit (Yeşil Alandan Sarı Alana Devir ve Cerrahi Dışlama Sonrası Destek Tedavisi)",
        "disposition": "Yeşil Alanda Değerlendirilip Sarı Alana Devir -> İV Hidrasyon / Batın USG / Çocuk Cerrahisi Konsültasyonu ile Apandisit Dışlanarak Poliklinik Kontrolüyle Taburculuk",
        "case_pearl": (
            "Akut mezenterik lenfadenit, sıklıkla geçirilmiş bir üst solunum yolu enfeksiyonu veya "
            "gastroenterit sonrası mezenterik lenf nodlarının reaktif hiperplazisiyle ortaya çıkar ve "
            "akut apandisiti taklit edebilir. Sağ alt kadranda peritoneal irritasyon veya belirgin "
            "hassasiyet olan çocuklar Sarı Alana devredilmeli; kademeli kompresyonlu batın "
            "ultrasonografisinde apendiksin normal kalibrede (<6 mm) görülmesi ve mezenterde büyümüş "
            "ovoid lenf nodları kümelenmesi ile cerrahi akut batın dışlanmalıdır."
        ),
        "steps": [
            {
                "stage_title": "Yeşil Alanda Fizik Muayene ve Alan Kararı",
                "question": "Bir hafta önce geçirilmiş üst solunum yolu enfeksiyonu sonrası sağ alt kadran ağrısıyla başvuran bu çocukta ilk yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Tablonun geçirilmiş viral üst solunum yolu enfeksiyonuna bağlı basit karın ağrısı olduğunu belirterek Yeşil Alanda oral ibuprofen şurup içirip evine göndermek",
                        "is_correct": False,
                        "scenario_update": "Sağ alt kadranda palpasyon hassasiyeti ve defans şüphesi olan hastanın batın muayenesi derinleştirilmeden analjezikle taburcu edilmesi cerrahi patolojilerin atlanma riskini artırdı.",
                        "teaching_point": "Sağ alt kadran ağrısı ve ateşi olan her çocukta cerrahi batın şüphesi taşındığından muayene tamamlanmadan analjezikle ayaktan taburcu edilmez.",
                    },
                    {
                        "text": "Karın ağrısının bağırsak motilite bozukluğuna ve dışkı sıkışmasına bağlı olduğunu düşünerek Yeşil Alanda rektal lavman uygulamak ve tuvalet sonrası hastayı tekrar değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Sağ alt kadranda lokalize inflamatuar hassasiyeti olan hastaya yapılan lavman intraluminal basıncı artırarak çocuğun ağrısını daha da şiddetlendirdi.",
                        "teaching_point": "Sağ alt kadran hassasiyeti ve ateş varlığında akut apandisit ve cerrahi patolojiler ekarte edilmeden rektal lavman uygulamak kontrendikedir.",
                    },
                    {
                        "text": "Karın muayenesinde sağ alt kadrandaki hassasiyet ve savunma bulgularını değerlendirip akut cerrahi batın şüphesiyle hastayı derhal Sarı Alana devretmek",
                        "is_correct": True,
                        "triggers_yellow_transfer": True,
                        "explanation": "Sağ alt kadranda lokalize hassasiyet ve defans şüphesi cerrahi batın (apandisit vb.) açısından kırmızı bayraktır; hasta damar yolu açılması, yakın takip ve görüntüleme için Sarı Alana devredilmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 37.8°C, KTA 104/dk, TA 105/68 mmHg. Batın muayenesinde sağ alt kadranda ve periumbilikal bölgede belirgin palpasyon hassasiyeti mevcut; hafif istemli defans şüphesi var, rebound saptanmadı. Bağırsak sesleri normoaktif. Orofarenkste hiperemi ve soluk tonsiller hipertrofi izlendi. Hasta ileri tetkik ve izlem için Sarı Alana devredildi!",
                    },
                    {
                        "text": "Hastayı Yeşil Alanda tutarak ayakta direkt batın grafisi ve tam idrar tetkiki istemek, sonuçlar çıkana kadar bekleme odasında oral beslenmesine izin vermek",
                        "is_correct": False,
                        "scenario_update": "Olası cerrahi batın tablosunda hastaya ağızdan gıda verilmesi acil anestezi açlık süresini bozdu; ayrıca direkt batın grafisi tanısal değer sağlamadı.",
                        "teaching_point": "Akut sağ alt kadran ağrısında cerrahi dışlanana kadar hasta aç (NPO) tutulmalı, Sarı Alana devredilmeli ve radyasyonsuz ilk seçenek olan ultrasonografi planlanmalıdır.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Tetkik ve Görüntüleme Kararı",
                "question": "Sarı Alana devralınan ve sağ alt kadran hassasiyeti bulunan bu çocukta akut cerrahi patolojiyi dışlamak için hangi tetkikler istenmelidir?",
                "options": [
                    {
                        "text": "Damar yolu açarak hidrasyon sağlamak, hemogram ve C-reaktif protein düzeyini inceleyip radyasyonsuz ilk basamak görüntüleme olan batın ultrasonografisi istemek",
                        "is_correct": True,
                        "explanation": "Sağ alt kadran ağrısında ilk basamak yaklaşım ağızdan alımın kesilmesi, intravenöz hidrasyon, enfeksiyon belirteçleri ve cerrahi patolojileri radyasyonsuz dışlayan kademeli kompresyonlu ultrasonografidir.",
                        "new_finding": "LABORATUVAR: Lökosit 10.800/mm³ (%65 nötrofil, %28 lenfosit), CRP 14 mg/L, TİT normal. BATIN USG: Sağ alt kadranda kör uçlu tübüler yapı (apendiks çapı 4.4 mm) normal kalibrede, basılabilir ve çevre dokusu doğaldır; terminal ileum komşuluğunda mezenterde en büyüğü 9x16 mm boyutlarında çok sayıda ovoid reaktif lenf bezi kümelenmesi ve minimal serbest sıvı izlendi.",
                    },
                    {
                        "text": "Ultrasonografinin operatör bağımlı ve yanıltıcı olabileceğini öngörerek vakit kaybetmeden doğrudan oral ve intravenöz kontrastlı tüm batın bilgisayarlı tomografisi çekmek",
                        "is_correct": False,
                        "scenario_update": "Stabil pediatrik hastaya yüksek doz radyasyon ve intravenöz nefrotoksik kontrast madde verildi; ultrasonografiyle kolayca konulabilecek tanı için gereksiz risk alındı.",
                        "teaching_point": "Çocuklarda akut karın ağrısında kılavuzların ilk basamak görüntüleme önerisi daima ultrasonografidir; bilgisayarlı tomografi yalnızca USG yetersiz veya şüpheli kaldığında düşünülür.",
                    },
                    {
                        "text": "Görüntüleme istemeden önce sağ alt kadrana ampirik seftriakson ve metronidazol infüzyonu başlamak, 24 saat sonra klinik düzelme olmazsa ultrasonografi planlamak",
                        "is_correct": False,
                        "scenario_update": "Cerrahi akut batın veya viral zemin netleşmeden başlanan geniş spektrumlu antibiyotik klinik tablonun ve inflamatuar yanıtın takibini güçleştirdi.",
                        "teaching_point": "Peritonit veya sepsis bulgusu olmayan stabil sağ alt kadran ağrılı çocukta tanı görüntüleme ile kesinleştirilmeden ampirik antibiyotik başlanmaz.",
                    },
                    {
                        "text": "Tablonun kesinlikle cerrahi apandisit olduğunu kabul ederek hiçbir görüntüleme veya laboratuvar tetkiki istemeden hastayı doğrudan acil laparoskopik apendektomiye almak",
                        "is_correct": False,
                        "scenario_update": "Görüntüleme yapılmadan ameliyata alınan hastada apendiksin tamamen normal olduğu, inflamasyonun mezenterik lenf bezlerinde yer aldığı görüldü (negatif apendektomi).",
                        "teaching_point": "Sağ alt kadran ağrılarında apandisit şüphesi olsa dahi ultrasonografi ile ayırıcı tanı yapılmalıdır; çocuklarda negatif apendektomi oranını düşürmek için görüntüleme şarttır.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Kesin Tanı",
                "question": "Geçirilmiş farenjit öyküsü, ılımlı inflamatuar yanıt, normal kalibrede apendiks ve mezenterde büyümüş lenf bezleriyle kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Akut Flegmonöz Apandisit",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografide apendiks normal kalibrede (4.4 mm), kompresyonla tamamen basılabilir ve çevre dokusu reaksiyonsuz olarak izlenmiştir.",
                        "teaching_point": "Akut apandisitte apendiks çapı ≥6 mm olup kompresyonla basılamaz, lümende hiperemi ve çevre mezenterik yağ dokusunda ekojenite artışı görülür.",
                    },
                    {
                        "text": "İleokolik İntususepsiyon (İnvajinasyon)",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografide iç içe geçmiş bağırsak anslarına ait hedef (target) işareti veya psödo-böbrek görünümü saptanmamıştır.",
                        "teaching_point": "İntususepsiyon genellikle daha küçük çocuklarda (3-36 ay) kolik tarzı ağrı ve ultrasonografide tipik simit/hedef görünümü ile seyreder.",
                    },
                    {
                        "text": "Meckel Divertiküliti",
                        "is_correct": False,
                        "scenario_update": "Meckel divertikülitinde tipik olarak rektal ağrısız masif kanama veya lokalize apandisit benzeri nekrotizan inflamasyon görülür; ultrasonografide kör sonlanan kistik/tübüler kitle saptanmamıştır.",
                        "teaching_point": "Meckel divertikülü gastrointestinal kanama veya divertikülit ile prezente olur; mezenterde yaygın reaktif lenf bezi kümelenmesi ve normal apendiks bu tabloyu açıklamaz.",
                    },
                    {
                        "text": "Akut Mezenterik Lenfadenit",
                        "is_correct": True,
                        "explanation": "Geçirilmiş üst solunum yolu enfeksiyonunu takiben sağ alt kadranda apandisiti taklit eden ağrı, USG'de normal apendiks ve mezenterde >8 mm multipl büyümüş reaktif lenf bezleri akut mezenterik lenfadeniti gösterir.",
                        "new_finding": "Kesin Tanı: Akut Mezenterik Lenfadenit.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Tedavi ve İzlem Planı",
                "question": "Ultrasonografi ve Çocuk Cerrahisi konsültasyonuyla apandisit dışlanan akut mezenterik lenfadenitli bu hastanın tedavisi ve taburculuk planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Lenfadenopatinin bakteriyel süpürasyona ilerlemesini engellemek amacıyla 14 gün süreyle oral amoksisilin-klavulanat ve sefiksim kombinasyonu reçete edip hastayı taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Viral enfeksiyon sonrası gelişen reaktif lenf bezleri için verilen geniş spektrumlu antibiyotik ikilisi çocukta dirençli ishale ve bağırsak florası bozulmasına yol açtı.",
                        "teaching_point": "Akut mezenterik lenfadenit genellikle viral veya post-enfeksiyöz reaktif bir süreçtir; bakteriyel süpürasyon veya sepsis bulgusu yoksa rutin antibiyotik tedavisi endike değildir.",
                    },
                    {
                        "text": "Oral hidrasyon ve semptomatik analjezi sağlamak, antibiyotiksiz izlemek, aileye kırmızı bayrak eğitimi vererek çocuk cerrahisi kontrolüyle taburcu etmek",
                        "is_correct": True,
                        "explanation": "Akut mezenterik lenfadenitte tedavi destekleyicidir (hidrasyon, parasetamol vb.). Rutin antibiyotik gerekmez. Apandisitin erken dönemde atlanmadığından emin olmak için aileye alarm bulguları (artan kusma, dirençli ateş, şiddetlenen ağrı) anlatılarak 24-48 saat sonra kontrol önerilir.",
                        "new_finding": "Çocuk Cerrahisi konsültasyonu ile cerrahi akut batın dışlandı. Destek tedavisi, diyet ve kırmızı bayrak eğitimi verilerek hasta 48 saat sonra poliklinik kontrolü şartıyla taburcu edildi.",
                    },
                    {
                        "text": "Apendiksin daha sonra reaktif lenf bezlerinin basısıyla iltihaplanabileceği gerekçesiyle hastayı cerrahi servise yatırarak profilaktik apendektomi operasyonu planlamak",
                        "is_correct": False,
                        "scenario_update": "Tamamen selim ve kendini sınırlayan mezenterik lenf bezi büyümesi için hastaya gereksiz genel anestezi ve cerrahi girişim uygulandı.",
                        "teaching_point": "Mezenterik lenfadenit cerrahi bir antite değildir; apendiks normal ise profilaktik cerrahi yapılmaz, hasta klinik olarak izlenir.",
                    },
                    {
                        "text": "Sağ alt kadrandaki lenf bezlerinin lenfoma veya granülomatöz süreç olabileceği şüphesiyle hastayı taburcu etmeden acil laparoskopik lenf nodu biyopsisi için yatırmak",
                        "is_correct": False,
                        "scenario_update": "Akut enfeksiyon sonrası reaktif ovoid lenf nodları bulunan stabil çocukta gereksiz ileri invaziv biyopsi işlemi yapıldı.",
                        "teaching_point": "Üst solunum yolu enfeksiyonu sonrası gelişen ovoid, kortikomedüller ayrımı korunmuş reaktif lenf bezlerinde sistemik B bulgusu (kilo kaybı vb.) yoksa acil biyopsi endike değildir.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y38",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "10 Yaş",
        "gender": "Erkek",
        "complaint": "Aniden başlayan şiddetli sağ yan ve kasık ağrısı, bulantı",
        "history": (
            "Annesi 10 yaşındaki oğlunu acil Yeşil Alana getiriyor: 'Yaklaşık 3 saat önce evde otururken "
            "birdenbire sağ böğrüne şiddetli bir sancı girdi. Ağrı dalga dalga geliyor, kıvrandırıyor, "
            "durduğu yerde duramıyor ve sağ kasığına vuruyor. İki kez safrasız kustu, tuvalete gittiğinde "
            "idrarını yaparken çok yandığını söyledi. Daha önce hiç böyle bir şikayeti olmamıştı, ateşi yok.'"
        ),
        "final_diagnosis": "Sağ Distal Üreter Taşına Bağlı Renal Kolik (Ürolitiyazis / Nefrolitiyazis)",
        "disposition": "Yeşil Alandan Sarı Alana Devir -> İV Hidrasyon / Spazmolitik / NSAİİ Analjezisi -> Üriner USG Doğrulaması -> Çocuk Ürolojisi/Nefrolojisi Poliklinik Takibi ile Taburculuk",
        "case_pearl": (
            "Pediatrik taş hastalığı (ürolitiyazis), ani başlayan, paroksismal dalgalar halinde gelen yan "
            "(flank) ve alt kadrana/kasığa yansıyan şiddetli ağrı, bulantı-kusma ve mikroskopik/makroskopik "
            "hematüri ile başvurur. Şiddetli kıvrandırıcı ağrısı olan hastalar Yeşil Alanda tutulmayıp "
            "intravenöz hidrasyon ve nonsteroid antiinflamatuar analjezi için Sarı Alana devredilmelidir. "
            "İlk basamak görüntüleme üriner sistem USG'dir; <5 mm distal taşlarda medikal ekspulsif/destekleyici "
            "tedavi ve poliklinik takibi esastır."
        ),
        "steps": [
            {
                "stage_title": "Yeşil Alanda Muayene ve Triyaj Değerlendirmesi",
                "question": "Aniden başlayan dalgalı sağ yan ağrısı ve huzursuzlukla Yeşil Alana getirilen bu çocukta ilk yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Kostovertebral açı hassasiyetini ve batın bulgularını kontrol edip şiddetli ağrı nedeniyle hastayı intravenöz analjezi için Sarı Alana devretmek",
                        "is_correct": True,
                        "triggers_yellow_transfer": True,
                        "explanation": "Paroksismal dalgalar halinde gelen şiddetli flank ağrısı, bulantı ve kostovertebral açı hassasiyeti acil damar yolu açılması, analjezi ve hidrasyon gerektirir; hasta derhal Sarı Alana devredilmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 118/dk (ağrıya bağlı taşikardik), TA 118/76 mmHg. Hasta huzursuz, ağrı nedeniyle kıvranıyor ve yatakta pozisyon bulamıyor. Batın muayenesinde peritoneal irritasyon (defans/rebound) yok; sağ alt kadranda hafif hassasiyet mevcut. Sağ kostovertebral açı hassasiyeti belirgin pozitif. Genital muayene doğal. Hasta Sarı Alana devredildi!",
                    },
                    {
                        "text": "Ağrının kas spazmına veya basit bel tutulmasına bağlı olduğunu düşünerek Yeşil Alanda oral kas gevşetici verip evde istirahat önermek",
                        "is_correct": False,
                        "scenario_update": "Bulantı, miksiyon güçlüğü ve şiddetli kostovertebral açı hassasiyeti olan hastanın üriner patolojisi atlandı ve ağrısı evde dayanılmaz hale geldi.",
                        "teaching_point": "Ani başlayan dalgalı yan ağrısı, bulantı ve kostovertebral açı hassasiyeti mekanik kas ağrısı değildir; üriner sistem obstrüksiyonu araştırılmalıdır.",
                    },
                    {
                        "text": "Tabloyu akut apandisit kabul ederek cerrahi konsültasyon istemek ve hasta bekleme salonundayken ağrı kesici vermeden muayene bulgularının netleşmesini beklemek",
                        "is_correct": False,
                        "scenario_update": "Hasta saatlerce şiddetli kıvrandırıcı ağrı çekti; peritoneal irritasyonu olmayan hastada uygun analjezi geciktirildi.",
                        "teaching_point": "Kıvrandırıcı, dalgalar halinde gelen ve yatakta sabit durdurmayan ağrılar peritoneal değil visseral/obstrüktif tiptedir; analjezi gereksiz yere geciktirilmemelidir.",
                    },
                    {
                        "text": "Hastanın ağrısını hafifletmek amacıyla Yeşil Alanda sıcak su torbası uygulamak ve ağızdan bol miktarda soğuk su içirerek hastayı bekletmek",
                        "is_correct": False,
                        "scenario_update": "Akut obstrüksiyon ve bulantısı olan hastaya ağızdan yüksek hacimli sıvı verilmesi kusmayı tetikledi ve renal pelvis içi basıncı artırdı.",
                        "teaching_point": "Akut kolik atağı sırasında ağızdan kontrolsüz aşırı sıvı verilmesi intrarenal basıncı ve bulantıyı artırır; intravenöz kontrollü hidrasyon ve analjezi esastır.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Tetkik ve Görüntüleme İstem Kararı",
                "question": "Sarı Alana devralınan, şiddetli sağ yan ağrısı ve miksiyon sırasında yanması olan bu çocukta tanısal yaklaşımınız nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Doğrudan yüksek doz radyasyon içeren kontrastlı tüm batın bilgisayarlı tomografisi çekerek tanı kesinleşene kadar hastaya hiçbir analjezik ilaç vermemek",
                        "is_correct": False,
                        "scenario_update": "Pediatrik hastaya radyasyonsuz ilk basamak ultrasonografi yerine yüksek radyasyonlu tetkik uygulandı ve hasta gereksiz yere şiddetli ağrı çekti.",
                        "teaching_point": "Pediatrik üriner obstrüksiyon şüphesinde ilk basamak görüntüleme radyasyonsuz ultrasonografidir; ayrıca uygun analjezi tanı sürecini maskelemez.",
                    },
                    {
                        "text": "Yalnızca intravenöz parasetamol infüzyonu uygulayıp hiçbir idrar tetkiki veya radyolojik görüntüleme istemeden hastayı doğrudan taburcu ederek poliklinik kontrolüne yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "İdrar tetkiki ve ultrasonografi yapılmadığı için toplayıcı sistem dilatasyonu ve obstrüksiyonun düzeyi aydınlatılamadı.",
                        "teaching_point": "Kıvrandırıcı yan ağrısı olan çocukta hematüriyi saptamak için idrar tetkiki ve obstrüksiyonu görmek için ultrasonografi zorunludur.",
                    },
                    {
                        "text": "Üriner sistem enfeksiyonu şüphesiyle yalnızca tam idrar tetkiki ve idrar kültürü isteyerek acil ultrasonografi yapmadan ampirik seftriakson infüzyonu başlatmak",
                        "is_correct": False,
                        "scenario_update": "Ateşi olmayan hastada mekanik obstrüksiyon görüntülenmeden gereksiz yere parenteral antibiyotik başlandı ve altta yatan kalsifiye odak araştırılmadı.",
                        "teaching_point": "Ateş ve piyüri olmayan akut yan ağrısında antibiyotik değil; obstrüksiyonu saptamak için ultrasonografi ve analjezi önceliklidir.",
                    },
                    {
                        "text": "Damar yolu açarak hidrasyon ve nonsteroid analjezi uygulamak, tam idrar tetkiki, böbrek fonksiyonları ve acil üriner ultrasonografi istemek",
                        "is_correct": True,
                        "explanation": "Akut böğür ağrısı ve obstrüksiyon yönetiminde ilk adım nonsteroid antiinflamatuar analjezi ve hidrasyondur; mikroskopik hematüriyi gösteren TİT ve toplayıcı sistem dilatasyonunu/kalkülü gösteren USG ilk basamaktır.",
                        "new_finding": "LABORATUVAR: Üre 24 mg/dL, Kreatinin 0.52 mg/dL. TİT: Dansite 1025, pH 5.5, Lökosit negatif, Nitrit negatif, Mikroskopi: 15-20 eritrosit (mikroskopik hematüri). ÜRİNER USG: Sağ böbrek boyutları normal, toplayıcı sistemde evre 1 pelvikaliektazi izlendi; sağ üreterovezikal bileşkede 4 mm çapında posterior akustik gölgelenme veren intraluminal kalsifiye ekojen kalkül saptandı.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Kesin Tanı",
                "question": "Kıvrandırıcı yan ağrısı, mikroskopik hematüri ve ultrasonografide üreterovezikal bileşkede akustik gölgeli odak saptanan bu hastada kesin tanı nedir?",
                "options": [
                    {
                        "text": "Akut Bakteriyel Piyelonefrit Enfeksiyonu",
                        "is_correct": False,
                        "scenario_update": "Hastanın ateşi yoktur, idrar tetkikinde lökositüri veya nitrit saptanmamış, toplayıcı sistemde kalsifiye kalkül izlenmiştir.",
                        "teaching_point": "Piyelonefrit yüksek ateş, titreme, sistemik toksisite ve piyüri ile seyreder; hematüri ve akustik gölgeli kalkül mekanik taş hastalığını gösterir.",
                    },
                    {
                        "text": "Sağ Distal Üreter Taşı (Ürolitiyazis)",
                        "is_correct": True,
                        "explanation": "Ani başlayan yan ağrısı, mikroskopik hematüri ve ultrasonografide üreterovezikal bileşkede 4 mm boyutunda akustik gölgeli kalkül ile hafif hidronefroz görülmesi ürolitiyazise bağlı renal kolik tanısını kesinleştirir.",
                        "new_finding": "Kesin Tanı: Sağ Distal Üreter Taşına Bağlı Renal Kolik (Ürolitiyazis).",
                    },
                    {
                        "text": "Akut Flegmonöz Apandisit Tablosu",
                        "is_correct": False,
                        "scenario_update": "Batın muayenesinde peritoneal irritasyon yoktur; tam idrar tetkikinde hematüri ve ultrasonografide üreter obstrüksiyonu saptanmıştır.",
                        "teaching_point": "Apandisitte göbek çevresinden sağ alta göç eden ağrı, anoreksi ve peritonit bulguları tipiktir; belirgin hematüri ve üreterde kalkül beklenmez.",
                    },
                    {
                        "text": "Sağ Akut Testiküler Epididimo-orşit",
                        "is_correct": False,
                        "scenario_update": "Skrotal muayenede testisler ve epididimler tamamen doğal, ağrısız ve simetrik bulunmuştur.",
                        "teaching_point": "Epididimit skrotumda şişlik, lokalize hassasiyet ve ısı artışı ile karakterizedir; flank ağrısı ve mikroskopik hematürinin primer nedeni değildir.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Tedavi ve Taburculuk Planı",
                "question": "Distal üreterde 4 mm taş ve hafif dilatasyon saptanan, böbrek fonksiyonları normal bu hastada taburculuk ve tedavi protokolü ne olmalıdır?",
                "options": [
                    {
                        "text": "Taşın kendiliğinden düşme olasılığı bulunmadığını belirterek hastayı derhal acil ameliyathaneye almak ve cerrahi rijit üreterorenoskopi ile lazer litotripsi operasyonu uygulamak",
                        "is_correct": False,
                        "scenario_update": "Distal yerleşimli 4 mm boyutundaki taşların büyük çoğunluğu medikal tedaviyle kendiliğinden düşer; acil invaziv cerrahi girişim gereksiz anestezi ve üreter travması riski oluşturdu.",
                        "teaching_point": "Çocuklarda <5 mm distal üreter taşlarında enfeksiyon veya inatçı obstrüksiyon yoksa ilk yaklaşım konservatif izlem ve medikal ekspulsif tedavidir; acil cerrahi gerekmez.",
                    },
                    {
                        "text": "İdrar yolu enfeksiyonu profilaksisi amacıyla bir ay boyunca oral siprofloksasin tedavisi başlamak ve taş düşene dek hastanın yatak istirahatinde kalmasını önermek",
                        "is_correct": False,
                        "scenario_update": "Enfeksiyonu olmayan hastada uygunsuz florokinolon kullanımı yan etkilere yol açtı; ayrıca yatak istirahati taşın idrar akımıyla ilerlemesini geciktirdi.",
                        "teaching_point": "Steril ürolitiyaziste profilaktik antibiyotik endike değildir; aksine hastanın mobilize olması taşın spontan geçişini kolaylaştırır.",
                    },
                    {
                        "text": "Ağrısı gerileyen hastaya bol sıvı alımı, analjezik ve idrar süzme eğitimi verip Çocuk Ürolojisi poliklinik kontrolüyle taburcu etmek",
                        "is_correct": True,
                        "explanation": "Komplike olmayan, 4 mm'lik distal taşlarda yaklaşım: bol hidrasyon, aralıklı analjezi, taş analizi için idrar süzme eğitimi ve elektif poliklinik takibidir.",
                        "new_finding": "Analjezi ve hidrasyonla semptomları düzelen hasta, bol sıvı tüketimi ve idrar süzme önerileriyle Çocuk Ürolojisi takibine yönlendirilerek taburcu edildi.",
                    },
                    {
                        "text": "Hafif pelvikaliektazi saptandığı için hastayı nefroloji servisine yatırmak, mutlak aç bırakıp 48 saat boyunca aralıksız intravenöz yüksek doz furosemid uygulamak",
                        "is_correct": False,
                        "scenario_update": "Obstrükte sisteme yüksek doz kıvrım diüretiği verilmesi intrapelvik basıncı aşırı artırarak şiddetli ağrı krizine ve elektrolit dengesizliğine neden oldu.",
                        "teaching_point": "Akut taş obstrüksiyonunda furosemid gibi güçlü diüretikler intraluminal basıncı artırarak forniks rüptürü riski yaratır; kesinlikle uygulanmamalıdır.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y39",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "7 Yaş",
        "gender": "Kız",
        "complaint": "Son haftalarda aşırı su içme, sık idrara çıkma ve gece altını ıslatma",
        "history": (
            "Annesi 7 yaşındaki kızını Yeşil Alana getiriyor: 'Kızım son 3 haftadır sürekli susadığını "
            "söylüyor, günde 3-4 litre su içiyor. Okulda ve evde neredeyse saat başı tuvalete gidiyor. "
            "3 yaşından beri hiç gece altına kaçırmazken son 10 gündür her gece yatağını ıslatmaya "
            "başladı. İştahı iyi olmasına rağmen son 2 haftada kilo verdiğini ve hafif halsizleştiğini "
            "fark ettik. Ateşi, kusması veya nefes darlığı yok.'"
        ),
        "final_diagnosis": "Yeni Başlangıçlı Tip 1 Diabetes Mellitus (Ketoasidoz Tablosu Olmayan Hafif Hiperglisemi)",
        "disposition": "Yeşil Alandan Sarı Alana Devir -> Kan Gazı / Elektrolit / İdrar Ketonu Değerlendirmesi -> DKA Dışlanarak Çocuk Endokrinoloji Servisine İnsülin Başlanması ve Eğitim İçin Yatış",
        "case_pearl": (
            "Çocuklarda polidipsi, poliüri, sekonder enürezis ve açıklanamayan kilo kaybı yeni başlangıçlı "
            "tip 1 diyabet için klasik dörtlüdür. Yeşil Alanda kapiller kan glukozu >200 mg/dL ölçülen "
            "her çocuk ketoasidoz (DKA) riski açısından derhal Sarı Alana devredilmeli; kan gazı "
            "(pH, HCO3) ve idrar/kan ketonu bakılmalıdır. Asidozu olmayan (pH ≥7.30, HCO3 ≥18) stabil "
            "vakalara intravenöz insülin infüzyonu yerine Çocuk Endokrinoloji servisinde subkutan insülin "
            "rejimi ve aile eğitimi başlanır."
        ),
        "steps": [
            {
                "stage_title": "Yeşil Alanda Klinik Değerlendirme ve Alan Kararı",
                "question": "Polidipsi, poliüri ve sekonder enürezis öyküsüyle Yeşil Alana başvuran bu 7 yaşındaki çocukta ilk basamak yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Şikayetleri primer enürezis noktürna ve idrar yolu enfeksiyonu olarak yorumlayıp Yeşil Alanda tam idrar tetkiki isteyerek oral antibiyotik reçete etmek",
                        "is_correct": False,
                        "scenario_update": "Polidipsi ve kilo kaybı eşlik eden çocukta glukoz değerlendirilmediği için altta yatan metabolik bozukluk atlandı.",
                        "teaching_point": "Kısa sürede gelişen polidipsi, poliüri ve kilo kaybı varlığında basit idrar yolu enfeksiyonu düşünülmeden önce mutlaka glukoz düzeyi kontrol edilmelidir.",
                    },
                    {
                        "text": "Aşırı su içmenin psikojenik polidipsiye bağlı olduğunu varsayarak aileye evde sıkı sıvı kısıtlaması uygulamalarını önermek ve çocuğu taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Ozmotik diürezi olan çocukta sıvı kısıtlaması yapılması intravasküler volüm açığını hızla derinleştirerek hipovolemik şok tablosuna zemin hazırladı.",
                        "teaching_point": "Ozmotik diürezi olan çocuklarda metabolik bozukluk ekarte edilmeden sıvı kısıtlaması yapılması ölümcül dehidratasyon ve şoka neden olabilir.",
                    },
                    {
                        "text": "Bilinç açık ve solunum rahat olduğu için hastayı Yeşil Alanda tutarak ayaktan Çocuk Nefrolojisi polikliniğine tübüler fonksiyon testleri için yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Akut glukoz yüksekliği riski taşıyan çocuk poliklinik randevusu için eve gönderildi ve saatler içinde dehidratasyonu derinleşti.",
                        "teaching_point": "Yeni başlangıçlı poliüri ve kilo kaybı olan çocukta acil serviste kan şekeri ölçülmeden hasta elektif polikliniklere sevk edilmemelidir.",
                    },
                    {
                        "text": "Vital bulguları ve dehidratasyon derecesini değerlendirmek, acil parmaktan kapiller kan şekeri ölçümü yaparak hastayı izlem için Sarı Alana devretmek",
                        "is_correct": True,
                        "triggers_yellow_transfer": True,
                        "explanation": "Polidipsi, poliüri, sekonder enürezis ve kilo kaybı klasik ozmotik diürez bulgularıdır; acil kapiller glukoz bakılmalı ve metabolik risk nedeniyle hasta Sarı Alana alınmalıdır.",
                        "new_finding": "Vital Bulgular: Ateş 36.7°C, KTA 98/dk, Solunum 20/dk, SpO2 %99, TA 102/64 mmHg. Bilinç açık ve oryante; Kussmaul solunumu veya nefeste aseton kokusu yok. Mukoza hafif kuru, kapiller dolum 2 saniye (hafif dehidratasyon). Parmaktan ölçülen kapiller kan şekeri 310 mg/dL bulundu. Hasta Sarı Alana devredildi!",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Metabolik Tetkik ve Durum Değerlendirmesi",
                "question": "Sarı Alana devralınan ve kan şekeri 310 mg/dL ölçülen hastada asidoz ve elektrolit dengesizliğini dışlamak için hangi tetkikler istenmelidir?",
                "options": [
                    {
                        "text": "Hemen intravenöz kristalize regüler insülin puşesi uygulamak ve ardından hiçbir kan tetkiki istemeden hastayı doğrudan yoğun bakıma transfer etmek",
                        "is_correct": False,
                        "scenario_update": "Kan gazı ve potasyum düzeyi bilinmeden yapılan İV bolus insülin ani hipokalemiye, kardiyak aritmilere ve hızlı ozmotik kaymaya yol açtı.",
                        "teaching_point": "Pediatrik yaş grubunda yüksek kan şekerinde asla intravenöz bolus insülin puşe yapılmaz; önce kan gazı, potasyum ve keton değerlendirilmelidir.",
                    },
                    {
                        "text": "Venöz kan gazı, serum elektrolitleri, böbrek fonksiyon testleri, tam idrar tetkikinde keton incelemesi ve hemoglobin A1c konsantrasyonu istemek",
                        "is_correct": True,
                        "explanation": "Kan şekeri yüksek saptanan çocukta temel amaç ketoasidoz tablosunu (asidemi, hipobikarbonatemi, ketonüri) değerlendirmek, elektrolit dengesini görmek ve kronik glisemik yükü (HbA1c) doğrulamaktır.",
                        "new_finding": "LABORATUVAR: Venöz Kan Gazı: pH 7.38, pCO2 38 mmHg, HCO3 22 mmol/L, Baz açığı -1.8 mEq/L (asidoz yok). Serum Na 136 mEq/L, K 4.3 mEq/L, Glukoz 308 mg/dL, Üre 22 mg/dL, Kreatinin 0.48 mg/dL. TİT: Dansite 1030, Glukoz (++++), Keton negatif (eser), protein negatif. HbA1c: %10.4.",
                    },
                    {
                        "text": "Metabolik tetkikleri erteleyerek yalnızca kraniyal bilgisayarlı tomografi çekmek ve intrakraniyal kitleye sekonder santral hormon yetmezliği tablosunu araştırmak",
                        "is_correct": False,
                        "scenario_update": "Nörolojik defisiti olmayan çocuğa yüksek doz radyasyon verildi ve metabolik tablonun doğrulanması saatlerce gecikti.",
                        "teaching_point": "Kilo kaybı, poliüri ve glukoz yüksekliği olan çocukta ilk incelenmesi gereken sistem santral sinir sistemi görüntülemesi değil metabolik kan tetkikleridir.",
                    },
                    {
                        "text": "Oral rehidratasyon sıvısı verip laboratuvar tetkiki istemeden hastayı altı saat sonra tekrar kan şekeri ölçümü için sarı alanda bekletmek",
                        "is_correct": False,
                        "scenario_update": "Kan gazı ve keton kontrolü yapılmadan bekletilen hastada olası asidoz tablosunun erken tanısı ve uygun servise sevki gecikti.",
                        "teaching_point": "Yüksek kan şekeriyle başvuran çocukta asidoz ve ketoz varlığı acilen teyit edilmelidir; tetkiksiz saatlerce beklemek doğru bir yaklaşım değildir.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Kesin Tanı",
                "question": "Poliüri, polidipsi, kan glukozu >200 mg/dL, HbA1c %10.4 ve normal kan gazı (pH 7.38, HCO3 22) parametreleriyle kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Ağır Diyabetik Ketoasidoz Tablosu",
                        "is_correct": False,
                        "scenario_update": "Hastanın kan gazında pH 7.38 ve HCO3 22 mmol/L olup asidoz yoktur; idrarda belirgin keton saptanmamıştır.",
                        "teaching_point": "Diyabetik ketoasidoz tanısı için hiperglisemiye ek olarak venöz pH <7.30 veya serum bikarbonatı <18 mmol/L ve belirgin ketonemi/ketonüri şarttır.",
                    },
                    {
                        "text": "Primer Santral Diabetes İnsipidus",
                        "is_correct": False,
                        "scenario_update": "Hastada masif glikozüri, kan glukozu 308 mg/dL ve HbA1c %10.4 saptanmıştır; tablo ADH eksikliğiyle uyumlu değildir.",
                        "teaching_point": "Diabetes insipidusta idrar dansitesi düşüktür (<1005) ve kan şekeri normaldir; glukoz yüksekliği ve glikozüri görülmez.",
                    },
                    {
                        "text": "Ketoasidozsuz Yeni Başlangıçlı Tip 1 Diabetes Mellitus",
                        "is_correct": True,
                        "explanation": "Polidipsi, poliüri, kilo kaybı, rastgele venöz plazma glukozu ≥200 mg/dL ve yüksek HbA1c birlikteliği tip 1 diyabet tanısı koydurur. Kan gazının normal olması (pH >7.30, HCO3 >18) ve ketonüri bulunmaması ketoasidozun olmadığını gösterir.",
                        "new_finding": "Kesin Tanı: Ketoasidozsuz Yeni Başlangıçlı Tip 1 Diabetes Mellitus.",
                    },
                    {
                        "text": "Kalıtsal İzole Renal Glikozüri",
                        "is_correct": False,
                        "scenario_update": "Renal glikozüride kan glukoz düzeyi ve HbA1c tamamen normaldir; tübüler emilim defekti nedeniyle yalnızca idrarda şeker çıkar.",
                        "teaching_point": "Renal glikozüride sistemik hiperglisemi, yüksek HbA1c veya poliüri-polidipsi sendromu görülmez; kan şekeri daima fizyolojik sınırlardadır.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Tedavi ve Servis Yatış Planı",
                "question": "Ketoasidoz tablosu bulunmayan (pH 7.38, HCO3 22 mmol/L), genel durumu stabil tip 1 diyabetli bu çocuğun yönetim planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Asidozu olmadığı için intravenöz insülin vermemek, oral beslenmeyi sürdürerek subkutan insülin protokolü ve eğitimi için Çocuk Endokrinoloji servisine yatırmak",
                        "is_correct": True,
                        "explanation": "Ketoasidozu olmayan yeni tanı tip 1 diyabetli çocuklarda yoğun İV insülin infüzyonu veya agresif mayi tedavisi endike değildir. Hasta oral beslenebilir; Çocuk Endokrinoloji servisine yatırılarak subkutan çoklu doz insülin başlanır ve aileye kapsamlı diyabet eğitimi verilir.",
                        "new_finding": "Çocuk Endokrinoloji kliniği ile konsülte edilen hasta, subkutan insülin tedavisi başlanması ve kapsamlı aile diyabet eğitimi verilmesi amacıyla servise yatırıldı.",
                    },
                    {
                        "text": "Kan şekerini hızla 100 mg/dL seviyesine indirmek için yüksek doz intravenöz regüler insülin infüzyonu ve hipotonik sıvı başlayarak yoğun bakıma yatırmak",
                        "is_correct": False,
                        "scenario_update": "Asidozu olmayan stabil hastaya yüksek doz İV insülin ve hipotonik sıvı verilmesi ani glukoz düşüşüne ve serebral ödem riskine yol açtı.",
                        "teaching_point": "Ketoasidozu olmayan stabil diyabet hastalarında intravenöz insülin infüzyonu veya yoğun bakım yatışı gerekmez; subkutan rejim tercih edilir.",
                    },
                    {
                        "text": "Tip 1 diyabetli çocukta ilk basamak olarak oral antidiyabetik metformin başlamak ve beslenme önerileriyle hastayı acil servisten evine taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Mutlak insülin eksikliği bulunan çocukta oral antidiyabetik etkisiz kaldı ve hasta günler sonra ağır ketoasidoz tablosuyla tekrar başvurdu.",
                        "teaching_point": "Çocukluk çağı tip 1 diyabetinde mutlak otoimmün beta hücresi kaybı vardır; oral antidiyabetikler etkisizdir ve tedavi mutlaka insülindir.",
                    },
                    {
                        "text": "Hafif dehidratasyon nedeniyle 24 saat boyunca hastayı tamamen aç tutarak izotonik sıvı infüzyonu uygulamak ve insülin tedavisini poliklinik kontrolüne bırakmak",
                        "is_correct": False,
                        "scenario_update": "Aç bırakılan ve insülini başlanmayan çocukta lipoliz hızlanarak keton üretimi tetiklendi ve metabolik tablo asidoza doğru ilerledi.",
                        "teaching_point": "Ketoasidozu olmayan çocuk NPO tutulmaz; beslenme ile senkronize subkutan insülin başlanarak anabolik süreç sağlanmalıdır.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y40",
        "category": "👶 Ağlayan, Emmeyen, Huzursuz Bebek",
        "age": "4 Aylık",
        "gender": "Erkek",
        "complaint": "Sağ kasık bölgesinde aniden beliren şişlik, gerginlik ve durdurulamayan ağlama",
        "history": (
            "Annesi 4 aylık erkek bebeğini Yeşil Alana getiriyor: 'Oğlum yaklaşık 2 saat önce aniden "
            "çığlık atarak ağlamaya başladı. Ne yaptıysak susturamadık, emmek istemiyor ve bacaklarını "
            "sürekli karnına çekiyor. Bezini değiştirirken sağ kasığında, torbaya doğru inen ceviz "
            "büyüklüğünde sert ve gergin bir şişlik fark ettik. Daha önce burada hiç böyle bir kabarıklık "
            "görmemiştik, dokununca daha çok bağırıyor.'"
        ),
        "final_diagnosis": "İnkarsere Sağ İnguinal Fıtık (Yeşil Alandan Sarı Alana Devir, Başarılı Taksis ve Çocuk Cerrahisi Yatışı)",
        "disposition": "Yeşil Alandan Sarı Alana Devir -> Analjezi/Sedasyon Altında Nazik Manuel Redüksiyon (Taksis) -> Başarılı Redüksiyon Sonrası Erken Elektif Onarım İçin Çocuk Cerrahisi Yatışı",
        "case_pearl": (
            "Süt çocuklarında persistan processus vaginalis açıklığına bağlı inguinal herniasyonlar, "
            "dar dış inguinal halka nedeniyle hızla inkarserasyona (sıkışma ve dolaşım bozukluğu riski) "
            "ilerleyebilir. Sağ kasıkta gergin, ağrılı, redükte edilemeyen kitle saptanan huzursuz bebekler "
            "derhal Sarı Alana devredilmelidir. Peritonit veya ciltte nekroz/iskemi bulgusu yoksa, analjezi "
            "ve hafif sedasyon altında trendelenburg pozisyonunda nazik manuel redüksiyon (taksis) "
            "uygulanır; başarılı redüksiyon sonrası nüks ve doku hasarı riskini önlemek için Çocuk Cerrahisi "
            "servisine yatırılarak 24-48 saat içinde cerrahi onarım planlanır."
        ),
        "steps": [
            {
                "stage_title": "Yeşil Alanda Fizik Muayene ve Triyaj Değerlendirmesi",
                "question": "Durdurulamayan ağlama ve sağ kasıkta şişlikle getirilen 4 aylık bu bebekte ilk basamak fizik muayene ve alan kararınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Ağlamayı infantil koliğe bağlayarak Yeşil Alanda oral simetikon damla vermek ve anneyi emzirme teknikleri konusunda bilgilendirerek evine taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Kasık muayenesi yapılmadan infantil kolik kabul edilen bebekte organ dolaşım bozukluğu ve iskemi riski taşıyan patoloji atlandı.",
                        "teaching_point": "Ani başlayan huzursuzluk ve ağlama nöbeti olan her bebekte alt bezi tamamen açılarak inguinal ve genital bölgeler mutlaka muayene edilmelidir.",
                    },
                    {
                        "text": "Kasık ve skrotumu palpasyonla inceleyip redükte edilemeyen gergin kitleyi değerlendirerek acil cerrahi risk nedeniyle bebeği Sarı Alana devretmek",
                        "is_correct": True,
                        "triggers_yellow_transfer": True,
                        "explanation": "Kasık bölgesinde ağrılı, sert ve redükte edilemeyen kitle varlığı sıkışmış organ ansı ve dolaşım bozukluğu riski taşır; acil müdahale ve analjezi için bebek Sarı Alana alınmalıdır.",
                        "new_finding": "Vital Bulgular: Ateş 37.1°C, KTA 155/dk (ağlamaya sekonder taşikardik), Solunum 38/dk, SpO2 %99. Bebek ajite ve durdurulamayan ağlama nöbetinde. Genitoüriner muayenede sağ kasıktan hemiskrotuma uzanan yaklaşık 3x2 cm boyutlarında, palpasyonla son derece hassas, gergin, kendiliğinden gerilemeyen kitle saptandı. Kitle üzerindeki cilt rengi ve ısısı doğal; her iki testis skrotum tabanında palpe edildi. Sol kasık doğal. Bebek derhal Sarı Alana devredildi!",
                    },
                    {
                        "text": "Sağ kasıktaki şişliği reaktif lenfadenit kabul ederek Yeşil Alanda intramüsküler ampisilin uygulamak ve ertesi gün Çocuk Cerrahisi polikliniğine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Akut organ sıkışması tablosuna antibiyotik verilerek bebek evine gönderildi ve saatler içinde kitlede dolaşım bozukluğu derinleşti.",
                        "teaching_point": "Kasıktan skrotuma uzanan ani gelişmiş gergin ve ağrılı kitleler lenfadenit değildir; acil redüksiyon veya cerrahi değerlendirme gerektirir.",
                    },
                    {
                        "text": "Kitleye hiçbir analjezi veya sedasyon uygulamadan Yeşil Alanda iki elle var gücüyle bastırarak zorlu kompresyonla kitleyi batına itmeye çalışmak",
                        "is_correct": False,
                        "scenario_update": "Analjezisiz ve kontrolsüz uygulanan aşırı kuvvetli bası bebekte şiddetli ağrı travmasına, hematoma ve bağırsak perforasyonu riskine yol açtı.",
                        "teaching_point": "Ağlayan ve ıkınan bebekte zorlayıcı manevralar kontrendikedir; redüksiyon mutlaka analjezi/sedasyon altında nazikçe ve kontrollü uygulanmalıdır.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda İlk Girişim ve Manuel Redüksiyon Kararı",
                "question": "Sarı Alana alınan, kasık derisinde kızarıklık veya sistemik peritonit bulgusu olmayan bu bebekte ilk aşamada ne yapılmalıdır?",
                "options": [
                    {
                        "text": "Manuel redüksiyonu denemeden önce acil tüm batın bilgisayarlı tomografisi çekerek bağırsak anslarının lümen genişliğini ve duvar kalınlığını incelemek",
                        "is_correct": False,
                        "scenario_update": "Gereksiz radyolojik tetkiklerle geçen süre boyunca kitle içindeki dokuların dolaşımı daha da bozuldu ve cerrahi aciliyet arttı.",
                        "teaching_point": "Peritonit veya doku nekrozu bulgusu olmayan sıkışmış kasık kitlelerinde ilk basamak radyolojik incelemelerle vakit kaybetmeden analjezi altında nazik redüksiyondur.",
                    },
                    {
                        "text": "Hiçbir manuel redüksiyon manevrası denemeden bebeği derhal genel anesteziye alarak ameliyathanede acil laparotomi ile cerrahi eksplorasyon planlamak",
                        "is_correct": False,
                        "scenario_update": "Nazik taksis manevrasıyla dakikalar içinde ameliyatsız redükte edilebilecek olguda acil şartlarda yüksek anestezi ve operasyon komplikasyonları gelişti.",
                        "teaching_point": "Peritonit veya ciltte morarma/gangren olmayan vakalarda ilk basamak analjezi altında nazik manuel redüksiyondur; başarılı olursa cerrahi elektif şartlara çekilir.",
                    },
                    {
                        "text": "Bebeğe intravenöz analjezi ve hafif sedasyon sağlamak, Trendelenburg pozisyonunda ılık kompres uygulayıp nazik manuel redüksiyon manevrası denemek",
                        "is_correct": True,
                        "explanation": "Ciltte renk değişikliği veya peritonit olmayan sıkışmış kasık kitlelerinde ilk yaklaşım analjezi/sedasyon, Trendelenburg pozisyonu ve nazik manuel redüksiyondur (taksis).",
                        "new_finding": "İntravenöz analjezi (fentanil) sağlandı. Bebek gevşeyip Trendelenburg pozisyonuna alındıktan ve ılık kompres uygulandıktan sonra, eksternal halka tabanından uygulanan nazik taksis manevrasıyla kitle hava-sıvı gurultusu eşliğinde batına tamamen redükte oldu. Bebeğin ağlaması durdu, vitalleri rahatladı (KTA 115/dk).",
                    },
                    {
                        "text": "Ağrıyı kesmek amacıyla kitlenin tam merkezine doğrudan lokal lidokain enjeksiyonu yapmak ve ardından enjektörle kitleden sıvı aspire etmeye çalışmak",
                        "is_correct": False,
                        "scenario_update": "Kitle içine körlemesine yapılan iğne aspirasyonu bağırsak duvarında delinmeye ve skrotal alana fekal kontaminasyona yol açtı.",
                        "teaching_point": "İçinde bağırsak ansları bulunan kasık kitlelerine asla körlemesine iğne aspirasyonu veya lokal anestezik enjeksiyonu yapılmaz; perforasyon riski yaratır.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Kesin Tanı",
                "question": "Kasıktan skrotuma uzanan gergin kitle, taksis manevrasıyla redükte olan barsak ansı ve klinik tabloyla kesin tanınız nedir?",
                "options": [
                    {
                        "text": "İnkarsere Sağ İnguinal Fıtık",
                        "is_correct": True,
                        "explanation": "Persistan processus vaginalis açıklığından skrotuma inen, dış halkada sıkışarak huzursuzluk ve gerginlik yaratan, taksis ile batına redükte olan patoloji inkarsere inguinal fıtıktır.",
                        "new_finding": "Kesin Tanı: İnkarsere Sağ İnguinal Fıtık.",
                    },
                    {
                        "text": "Akut Testis Torsiyonu",
                        "is_correct": False,
                        "scenario_update": "Testis torsiyonunda kitle inguinal kanaldan inen redükte edilebilir bir doku değildir; skrotumda yatay yerleşimli, aşırı ağrılı ve ödemli tek testis izlenir.",
                        "teaching_point": "Testis torsiyonunda testis yukarı çekilmiştir ve kremaster refleksi negatiftir; kasıktan hava-sıvı sesiyle batına redüksiyon görülmez.",
                    },
                    {
                        "text": "Akut İdiyopatik Skrotal Ödem",
                        "is_correct": False,
                        "scenario_update": "İdiyopatik skrotal ödemde skrotum cildinde iki taraflı ağrısız eritem ve ödem vardır; inguinal kanalda sıkışmış kitle saptanmaz.",
                        "teaching_point": "İdiyopatik skrotal ödem benign, ağrısız, kendiliğinden gerileyen bir cilt ödemidir; palpabl kasık kitlesi yapmaz.",
                    },
                    {
                        "text": "İnflame Kominikan Hidrosel",
                        "is_correct": False,
                        "scenario_update": "Hidrosel translüminasyon veren, gergin olmayan, ağrısız sıvı koleksiyonudur; akut sıkışma, aşırı huzursuzluk ve hava-sıvı sesiyle redüksiyon oluşturmaz.",
                        "teaching_point": "Kominikan hidroselde periton sıvısı skrotuma geçiş gösterir ancak barsak ansları içermediğinden akut inkarserasyon tablosu yaratmaz.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Tedavi ve Cerrahi İzlem Planı",
                "question": "Taksis ile başarıyla redükte edilen, ancak nüks ve doku hasarı riski yüksek olan bu bebeğin ileri yönetimi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Kitle tamamen redükte olduğu için bebeği acil servisten taburcu etmek ve nüks olursa tekrar getirmeleri tembihiyle hiçbir kontrole çağırmamak",
                        "is_correct": False,
                        "scenario_update": "Eve gönderilen bebekte saatler sonra fıtık tekrar inkarsere oldu ve aile geç başvurduğu için bağırsak gangreni gelişti.",
                        "teaching_point": "İnkarserasyon geçiren bebeklerde ilk 24-48 saatte tekrar sıkışma riski çok yüksektir; redüksiyon sonrası hasta mutlaka Çocuk Cerrahisi servisine yatırılmalıdır.",
                    },
                    {
                        "text": "Redüksiyon sonrası bebeği altı ay boyunca inguinal fıtık bağı kullanarak ameliyatsız izlemek üzere ortopedi polikliniğine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Bebeklerde fıtık bağı kullanımı hiçbir anatomik iyileşme sağlamadı; basıya bağlı testis atrofisi ve deri nekrozu gelişti.",
                        "teaching_point": "Çocukluk çağı inguinal hernilerinde fıtık bağı veya korse kullanımı kesinlikle kontrendikedir; definitif tedavi cerrahi yüksek ligasyondur.",
                    },
                    {
                        "text": "Redüksiyonun tam başarısını teyit etmek amacıyla bebeğe oral baryum kontrastı içirerek acil floroskopik inceleme yapmak ve taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Yeni redükte olmuş ödemli bağırsak dokusuna verilen baryum aspirasyon riski yarattı ve olası cerrahi öncesi ek risk oluşturdu.",
                        "teaching_point": "Başarılı taksis sonrası floroskopik kontrastlı inceleme gerekmez; hastanın klinik takibi, beslenme toleransı ve testis muayenesi esastır.",
                    },
                    {
                        "text": "Bebeği acilden taburcu etmeyip barsak ve testis dolaşımını izlemek, erken elektif operasyon için Çocuk Cerrahisi servisine yatırmak",
                        "is_correct": True,
                        "explanation": "İnkarserasyon öyküsü olan infantlarda tekrar inkarserasyon riski çok yüksektir. Başarılı redüksiyon sonrası ödemin gerilemesi için hasta yatırılır, 24-48 saat içinde Çocuk Cerrahisi tarafından elektif herniotomi (yüksek ligasyon) operasyonu planlanır.",
                        "new_finding": "Çocuk Cerrahisi konsültasyonu sonrası hasta, peritonit ve testis iskemi takibi yapılmak ve 24-48 saat içinde elektif cerrahi uygulanmak üzere servise yatırıldı.",
                    },
                ],
            },
        ],
    },
]
