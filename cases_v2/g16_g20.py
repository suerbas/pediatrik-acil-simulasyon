# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - G16-G20 (Yeniden Yazılmış v2)
G17, G18, G19, G20 vakaları Yeşil Alana başvurup muayenede saptanan kritik bulgular nedeniyle
Sarı Alana devredilerek yönetimine Sarı Alanda devam edilen vakalardır.
"""

CASES = [
    {
        "id": "G16",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "4 Yaş",
        "gender": "Erkek",
        "complaint": "Burun delikleri ve ağız çevresinde kaşıntılı, sarı-kehribar rengi kabuklu yaralar",
        "history": (
            "Annesi anlatıyor: '4-5 gün önce burnunun altında sinek ısırığı gibi küçük bir kızarıklık vardı, "
            "kaşıdıkça yayıldı. Şimdi burun kenarında ve çenesinde üzeri sarı bal kurumuş gibi kabuklu 3-4 "
            "tane yara oldu. Ateşi yok, keyfi ve iştahı yerinde.'"
        ),
        "final_diagnosis": "Büllöz Olmayan İmpetigo (Non-büllöz İmpetigo - S. aureus / S. pyogenes)",
        "disposition": "Yeşil Alandan Topikal Antibiyotik (Mupirosin/Fusidik Asit) ve Hijyen Eğitimi ile Taburculuk",
        "case_pearl": (
            "Çocuklarda en sık bakteriyel deri enfeksiyonu olan non-büllöz impetigoda burun ve ağız "
            "çevresinde eritemli zeminde 'bal rengi krutlar' (honey-colored crusts) tipiktir. Sınırlı ve "
            "az sayıda lezyonu olan, sistemik bulgusu bulunmayan vakalarda ilk tercih tedavi kabukların "
            "ılık sabunlu suyla yumuşatılarak temizlenmesi ve topikal Mupirosin veya Fusidik asit "
            "uygulanmasıdır."
        ),
        "steps": [
            {
                "stage_title": "Dermatolojik ve Sistemik Fizik Muayene",
                "question": "Perioral ve perinazal kabuklu lezyonlarla başvuran bu çocukta fizik muayenede öncelikle neleri değerlendirmelisiniz?",
                "options": [
                    {
                        "text": "Lezyon zeminindeki bakteriyel yükü hızla azaltmak amacıyla kabukları kuru gazlı bezle kazıyarak tamamen kaldırmak ve kanayan zemine povidon iyot solüsyonu sürerek sıkı kapalı pansuman yapmak",
                        "is_correct": False,
                        "scenario_update": "Kuru halde zorla kaldırılan kabuklar yüzeyel dermiste kanamaya, şiddetli ağrıya ve çevre sağlam deriye oto-inokülasyon riskine yol açtı.",
                        "teaching_point": "Yüzeyel epidermal kabuklar asla kuru kuruya kazınarak koparılmamalı; ılık su veya serum fizyolojikli kompresle yumuşatılarak nazikçe temizlenmelidir.",
                    },
                    {
                        "text": "Lezyonların sayısını ve dağılımını, sarı-kehribar rengi krut yapısını, çevre deride basmakla soyulma veya derin endürasyon varlığını ve bölgesel lenf nodlarını muayene etmek",
                        "is_correct": True,
                        "explanation": "Yüzeyel sınırlı epidermal enfeksiyonu yaygın büllöz tablolardan, eksfoliyatif toksin aracılı soyulmalardan veya derin yumuşak doku enfeksiyonundan ayırt etmek tedavi yolunu belirler.",
                        "new_finding": "Vital Bulgular: Ateş 36.7°C, KTA 95/dk. Perioral ve perinazal bölgede toplam 4 adet, 0.5-1 cm çapında, eritemli zeminde sarı-bal rengi krutlu plaklar mevcut. Yaygın bül yok, basmakla epidermis soyulması negatif, derin doku endürasyonu veya ısı artışı yok. Submandibuler 0.8 cm mobil reaktif lenf nodu dışında sistemik muayene doğal.",
                    },
                    {
                        "text": "Yüzün orta hattındaki deri enfeksiyonlarının kavernöz sinüs komşuluğu taşıması nedeniyle hastayı acil gözleme yatırarak damar yolu açmak ve kraniyal-oftalmolojik konsültasyon istemek",
                        "is_correct": False,
                        "scenario_update": "Ateşi, periorbital ödemi veya derin selülit bulgusu olmayan tamamen yüzeyel 4 adet lezyon için gereksiz invaziv girişim ve konsültasyon planlandı.",
                        "teaching_point": "Kavernöz sinüs trombozu riski fasiyal üçgendeki derin fronkül veya ağır selülitlerde söz konusudur; epidermise sınırlı yüzeyel krutlu lezyonlarda yatış gerekmez.",
                    },
                    {
                        "text": "Fizik muayeneyi yalnızca burun çevresiyle sınırlı tutup vezikül-krut ayrımı veya tüm vücut deri kontrolü yapmadan doğrudan geniş spektrumlu ampirik oral antibiyotik reçete etmek",
                        "is_correct": False,
                        "scenario_update": "Gövde ve ekstremiteler kontrol edilmediği için lezyonların gerçekten sınırlı olup olmadığı ve büllöz tutulum varlığı doğrulanamadı.",
                        "teaching_point": "Deri enfeksiyonlarında tedavi seçimi lezyonların toplam yaygınlığına ve bül varlığına göre yapıldığından tüm deri yüzeyi incelenmelidir.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik İstem Kararı",
                "question": "Sınırlı sayıda (4 adet) perioral krutlu lezyonu olan, ateşi ve derin doku bulgusu bulunmayan bu çocukta hangi tetkikler istenmelidir?",
                "options": [
                    {
                        "text": "Topikal veya sistemik tedaviye başlamadan önce krut altından bakteriyolojik yara sürüntü kültürü ve antibiyogram alarak üreme sonucuna göre hedefe yönelik antibiyotik planlamak",
                        "is_correct": False,
                        "scenario_update": "Kültür sonucu 48-72 saat sonra S. aureus olarak raporlandı; bu sürede tedavisiz bekleyen çocukta oto-inokülasyonla yeni lezyonlar çıktı.",
                        "teaching_point": "Tipik ve sınırlı yüzeyel piyodermilerde rutin yara kültürü önerilmez; kültür yalnızca tedaviye dirençli, tekrarlayan veya MRSA salgını şüphesi olan vakalarda alınır.",
                    },
                    {
                        "text": "Bakteriyel deri enfeksiyonu sonrası akut böbrek tutulumu riskini erken saptamak amacıyla tam idrar tetkiki, serum ASO titresi, kompleman C3 düzeyi ve renal fonksiyon testleri istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR: TİT normal, ASO 80 IU/mL, C3 125 mg/dL, Kreatinin 0.35 mg/dL. Sonuçlar klinik yönetimi hiçbir şekilde değiştirmedi.",
                        "teaching_point": "Akut poststreptokoksik glomerülonefrit deri enfeksiyonundan 2-6 hafta sonra gelişebilir; aktif, asemptomatik yüzeyel lezyon aşamasında rutin C3 veya idrar taraması endike değildir.",
                    },
                    {
                        "text": "Klinik görünüm yüzeyel epidermise sınırlı olduğu ve sistemik enfeksiyon bulgusu saptanmadığı için ek kan tetkiki veya sürüntü kültürü istemeden tanıya yönelmek",
                        "is_correct": True,
                        "explanation": "Genel durumu iyi, ateşi olmayan ve sınırlı sayıda tipik yüzeyel krutlu lezyonu bulunan çocuklarda tanı kliniktir; laboratuvar veya kültür tetkiki gerekmez.",
                        "new_finding": "Ek laboratuvar veya kültür tetkiki istenmedi; klinik bulgularla tanı ve tedavi aşamasına geçildi.",
                    },
                    {
                        "text": "Enfeksiyonun derin yumuşak dokuya yayılımını ve sistemik inflamatuar yanıtı değerlendirmek amacıyla tam kan sayımı, CRP, prokalsitonin ve periferik kan kültürü tetkikleri istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR: WBC 8.400/mm³, CRP 2.1 mg/L, Prokalsitonin 0.04 ng/mL. Ateşsiz çocukta gereksiz kan alma işlemi yapıldı.",
                        "teaching_point": "Ateş, bölgesel selülit veya toksik görünüm eşlik etmeyen lokalize yüzeyel deri enfeksiyonlarında sistemik akut faz reaktanları ve kan kültürü istenmez.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik öykü ve fizik muayene bulgularıyla bu hastada en doğru tanı hangisidir?",
                "options": [
                    {
                        "text": "Non-büllöz İmpetigo",
                        "is_correct": True,
                        "explanation": "Burun ve ağız çevresinde kaşıma/mikrotravma sonrası gelişen, eritemli zeminde bal rengi kalın krutlarla karakterize yüzeyel lezyonlar non-büllöz impetigo için tipiktir.",
                        "new_finding": "Kesin Tanı: Lokalize Non-büllöz İmpetigo.",
                    },
                    {
                        "text": "Eksfoliyatif Büllöz İmpetigo",
                        "is_correct": False,
                        "scenario_update": "Hastada eksfoliyatif toksin A'ya bağlı gevşek, şeffaf-sarı sıvı dolu intakt büller veya bül yırtılması sonrası ince vernik benzeri yakalık (collarette) görünümü yoktur.",
                        "teaching_point": "Büllöz impetigoda sağlam deride gelişen gevşek büller ve açıldığında çevresinde kalan ince skuamlı halka görülür; kalın bal rengi krutlar non-büllöz formun özelliğidir.",
                    },
                    {
                        "text": "Sekonder Enfekte Perioral Atopik Dermatit",
                        "is_correct": False,
                        "scenario_update": "Çocuğun özgeçmişinde kronik tekrarlayan kuruluk, fleksüral egzama veya atopi öyküsü olmayıp lezyonlar sağlıklı deride sinek ısırığı sonrası akut başlamıştır.",
                        "teaching_point": "Kronik kserozis ve egzamatöz zemin olmadan sağlıklı deride akut başlayan bal rengi krutlu plaklar primer non-büllöz impetigodur.",
                    },
                    {
                        "text": "Rekürren Herpes Simpleks Labialis",
                        "is_correct": False,
                        "scenario_update": "Lezyonlar dudak vermilion sınırında ağrılı-yanmalı prodromla çıkan grup halinde milimetrik veziküller değil, burun altı ve çene derisinde kaşıntılı bal rengi krutlu plaklardır.",
                        "teaching_point": "Herpes labialis dudak mukokutanöz birleşiminde eritemli zeminde küme yapmış ağrılı küçük veziküllerle seyreder.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Sınırlı sayıda (4 adet) lokalize non-büllöz impetigo lezyonu olan bu çocukta kılavuzlara göre ilk basamak tedavi ne olmalıdır?",
                "options": [
                    {
                        "text": "Krutları ılık sabunlu suyla yumuşatarak temizlemek, günde 3 kez topikal %2 mupirosin krem sürmek ve 24 saat sonra kreşe dönebileceği bilgisiyle taburcu etmek",
                        "is_correct": True,
                        "explanation": "IDSA ve pediatrik dermatoloji rehberlerine göre sınırlı ve komplike olmayan non-büllöz impetigoda topikal mupirosin veya fusidik asit ilk tercihtir; oral antibiyotik kadar etkilidir ve yan etkisi daha azdır.",
                        "new_finding": "Topikal %2 mupirosin krem, tırnakların kısa kesilmesi ve havlu ayrımı eğitimi verilerek hasta şifayla taburcu edildi.",
                    },
                    {
                        "text": "Topikal tedavinin yüz bölgesinde yetersiz kalacağı düşüncesiyle doğrudan 10 gün süreyle oral amoksisilin-klavulanat (45 mg/kg/gün) reçete edip lezyonlar tamamen iyileşene dek kreşi yasaklamak",
                        "is_correct": False,
                        "scenario_update": "Sınırlı 4 lezyon için verilen 10 günlük sistemik geniş spektrumlu antibiyotik çocukta antibiyotik ilişkili ishale yol açtı.",
                        "teaching_point": "Oral antibiyotik (sefaleksin veya amoksisilin-klavulanat) yalnızca çok sayıda/yaygın lezyon varlığında, büllöz impetigoda veya kreş salgınlarında tercih edilir; kreş izolasyonu etkili tedavinin 24. saatine kadardır.",
                    },
                    {
                        "text": "Kaşıntı ve eritemi hızla baskılamak amacıyla günde 2 kez topikal mometazon furoat krem ile topikal ketokonazol kremi birlikte reçete ederek 1 hafta sonra poliklinik kontrolüne çağırmak",
                        "is_correct": False,
                        "scenario_update": "Bakteriyel piyodermiye uygulanan topikal kortikosteroid lokal bağışıklığı baskılayarak lezyonların tüm yanaklara yayılmasına neden oldu.",
                        "teaching_point": "İmpetigo S. aureus ve S. pyogenes kaynaklı bakteriyel bir enfeksiyondur; topikal steroid ve antifungal kremler tabloyu ağırlaştırır.",
                    },
                    {
                        "text": "Poststreptokoksik nefriti önlemek amacıyla tek doz intramüsküler benzatin penisilin G uygulamak ve lezyonların üzerini hava almayacak şekilde steril oklüzif sargıyla kapatarak evde izlemek",
                        "is_correct": False,
                        "scenario_update": "Non-büllöz impetigoda en sık etken beta-laktamaz salgılayan S. aureus olduğu için penisilin G etkisiz kaldı ve lezyonlar gerilemedi.",
                        "teaching_point": "Non-büllöz impetigoda başat etken S. aureus olduğundan dar spektrumlu penisilinler etkisizdir; ayrıca antibiyotik tedavisi poststreptokoksik glomerülonefrit gelişimini engellemez.",
                    },
                ],
            },
        ],
    },
    {
        "id": "G17",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "9 Yaş",
        "gender": "Erkek",
        "complaint": "Karın ağrısı, iştahsızlık ve 2 kez kusma",
        "history": (
            "Annesi Yeşil Alan polikliniğine 'üşüttü, midesini bozdu' diyerek getiriyor: 'Dün akşam "
            "göbeğinin etrafında başlayan bir karın ağrısı vardı, gece 2 kez kustu. Bu sabah ağrısı karnının "
            "sağ alt tarafına indi. Çok sevdiği börekten bile bir lokma yemedi. Arabayla hastaneye gelirken "
            "kasislere girdikçe karnını tutup inledi ve muayene odasına hafif öne eğilerek yavaş yavaş "
            "yürüdü.'"
        ),
        "final_diagnosis": "Akut Apandisit (Yeşil Alandan Sarı Alana Devir ve Cerrahi Yatış)",
        "disposition": "Yeşil Alanda Saptanıp Sarı Alana Devir -> İV Sıvı/Analjezi/USG Doğrulaması -> Çocuk Cerrahisi Yatışı",
        "case_pearl": (
            "Göbek çevresinden (periumbilikal) başlayıp sağ alt kadrana (McBurney) göç eden ağrı, "
            "iştahsızlık (anoreksi), ağrıdan sonra başlayan kusma ve sarsıntıyla/yürümekle artan ağrı "
            "(topuk testi / kasis belirtisi) akut apandisit için çok güçlü ipuçlarıdır. Yeşil alana "
            "'basit karın ağrısı/gastroenterit' diye başvuran bu hastalar muayene ile yakalanıp Sarı "
            "Alana devredilmelidir."
        ),
        "steps": [
            {
                "stage_title": "Yeşil Alanda Fizik Muayene ve Alan Kararı",
                "question": "Yeşil alana mide üşütmesi düşüncesiyle getirilen bu 9 yaşındaki çocukta ilk muayene ve alan kararınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Kusma ve karın ağrısını viral mide-bağırsak enfeksiyonu olarak değerlendirip Yeşil Alanda intramüsküler ondansetron uygulamak, oral rehidratasyon sıvısı başlayarak 2 saat sonra ağızdan beslenme toleransını kontrol etmek",
                        "is_correct": False,
                        "scenario_update": "İshali olmayan ve sağ alt kadran peritoneal irritasyon bulgusu bulunan çocukta oral sıvı verilmesi kusmayı artırdı ve cerrahi tanı gecikti.",
                        "teaching_point": "Ağrının kusmadan önce başladığı, ishali olmayan ve yürümekle/sarsıntıyla sağ alt kadran ağrısı tarifleyen çocukta batın muayenesi yapılmadan viral enfeksiyon tedavisi başlanmaz.",
                    },
                    {
                        "text": "Sağ alt kadrandaki ağrıyı dışkı stazına bağlı kolik olarak yorumlayıp Yeşil Alanda rektal sodyum fosfat lavman uygulamak ve defekasyon sonrası ağrının tamamen gerileyip gerilemediğini gözlemlemek",
                        "is_correct": False,
                        "scenario_update": "Akut peritoneal irritasyon bulgusu olan hastaya yapılan rektal lavman intraluminal basıncı ve karın ağrısını şiddetlendirdi.",
                        "teaching_point": "Ateş, anoreksi, göç eden karın ağrısı ve peritoneal duyarlılığı olan çocuklarda akut cerrahi batın dışlanmadan rektal lavman uygulanmaz.",
                    },
                    {
                        "text": "Sağ alt kadranda spina iliaka anterior superior ile umblikus hattının dış üçte birlik noktasında lokalize defans ve geri çekme hassasiyetini değerlendirip hastayı Sarı Alana devretmek",
                        "is_correct": True,
                        "triggers_yellow_transfer": True,
                        "explanation": "Göbek çevresinden sağ alt kadrana göç eden ağrı, anoreksi, kasislerde artan ağrı ve lokalize peritoneal irritasyon bulguları akut cerrahi batını gösterir; hasta derhal Sarı Alana alınmalıdır.",
                        "new_finding": "Vital Bulgular: Ateş 38.2°C, KTA 112/dk. Batın muayenesinde sağ alt kadranda spina iliaka anterior superior ile umblikus hattının dış üçte birlik noktasında lokalize defans ve geri çekme hassasiyeti pozitif; sol alt kadran palpasyonuyla sağ alt kadranda ağrı ve topuk sarsıntı testi pozitif. Hasta Sarı Alana devredildi!",
                    },
                    {
                        "text": "Hastayı Yeşil Alanda tutarak önce ayakta direkt batın grafisi ve tam idrar tetkiki istemek, sonuçlar çıkana kadar oral parasetamol süspansiyon içirerek bekleme salonunda klinik seyri izlemek",
                        "is_correct": False,
                        "scenario_update": "Olası cerrahi girişim gerektiren hastaya ağızdan ilaç/sıvı verilmesi anestezi açlık süresini bozdu ve direkt batın grafisi tanısal katkı sağlamadı.",
                        "teaching_point": "Akut cerrahi batın şüphesi saptanan hastada oral alım derhal kesilmeli, hasta Sarı Alana devredilmeli ve gereksiz direkt batın grafisi yerine ultrasonografi planlanmalıdır.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda İlk Yaklaşım ve Görüntüleme Kararı",
                "question": "Hastayı Sarı Alana devraldınız. Bu aşamada ilk yönetim ve tetkik isteminiz nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Ağızdan alımı kesmek, damar yolu açıp izotonik sıvı ve intravenöz analjezi başlamak; hemogram, CRP, tam idrar tetkiki ve kademeli kompresyonlu batın ultrasonografisi istemek",
                        "is_correct": True,
                        "explanation": "Cerrahi akut batın şüphesinde ağızdan alımın kesilmesi, intravenöz hidrasyon, muayene bulgularını maskelemeyen uygun doz analjezi ve radyasyon içermeyen ilk basamak görüntüleme olarak ultrasonografi altın standarttır.",
                        "new_finding": "LABORATUVAR: WBC 16.800/mm³ (%84 nötrofil), CRP 46 mg/L, TİT normal. BATIN USG: Sağ alt kadranda peristaltizmi olmayan, kompresyonla basılanamayan 9.5 mm çapında kör sonlanan tübüler lümen ve içinde 6 mm akustik gölgelenme veren kalsifiye odak ile çevre mezenterik yağ dokuda ekojenite artışı izlendi.",
                    },
                    {
                        "text": "Fizik muayene bulgularını ve peritoneal irritasyonu maskelememek adına cerrahi konsültasyon tamamlanana kadar hiçbir analjezik ilaç vermemek, doğrudan oral ve intravenöz kontrastlı tüm batın bilgisayarlı tomografisi çekmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk saatlerce şiddetli ağrı çekti ve ultrasonografi ile radyasyonsuz tanı konulabilecekken yüksek doz karın BT radyasyonuna maruz kaldı.",
                        "teaching_point": "Güncel pediatrik cerrahi kılavuzlarına göre uygun doz intravenöz analjezi fizik muayene bulgularını maskelemez; ilk görüntüleme seçeneği ise BT değil ultrasonografidir.",
                    },
                    {
                        "text": "Ağızdan alımı kesip damar yolu açmak, yalnızca ayakta direkt batın grafisi ve tam kan sayımı isteyerek görüntüleme yapmadan doğrudan ampirik intravenöz seftriakson ve metronidazol tedavisi başlamak",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografik doğrulama ve cerrahi değerlendirme yapılmadan başlanan geniş spektrumlu antibiyotik klinik tabloyu kısmen baskılayarak kesin cerrahi kararı geciktirdi.",
                        "teaching_point": "Sepsis veya yaygın peritonit bulgusu olmayan stabil hastada antibiyotik profilaksisi ultrasonografi ile tanı kesinleştirilip cerrahi karar verildikten sonra başlanır.",
                    },
                    {
                        "text": "Sağ alt kadran ağrısının mezenterik lenfadenit veya idrar yolu enfeksiyonuna bağlı olabileceği düşüncesiyle ultrasonografiyi erteleyip idrar kültürü, gaita mikroskopisi ve viral antijen testleri sonuçlanana dek gözlemlemek",
                        "is_correct": False,
                        "scenario_update": "Görüntüleme ertelendiği için geçen 8 saat sonunda hastanın ateşi 39.1°C'ye yükseldi ve sağ alt kadrandaki defans tüm alt batına yayıldı.",
                        "teaching_point": "Lokalize sağ alt kadran defansı ve geri çekme hassasiyeti olan çocukta ultrasonografi geciktirilmemelidir; lümende kalsifiye taş varlığında perforasyon riski saatler içinde artar.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Kesin Tanı",
                "question": "Klinik tablo, nötrofilik lökositoz ve ultrasonografi bulguları eşliğinde kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Akut Mezenterik Lenfadenit Sendromu",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografide çapı 9.5 mm'ye ulaşmış, basılanamayan ve içinde 6 mm apendikolit bulunan inflame apendiks doğrudan görüntülendi.",
                        "teaching_point": "Mezenterik lenfadenitte apendiks normal çapta (<6 mm) ve kompresyonla basılanabilir özellikte olup sağ alt kadranda büyümüş reaktif lenf nodları izlenir.",
                    },
                    {
                        "text": "Akut Süpüratif Apandisit",
                        "is_correct": True,
                        "explanation": "Yüksek klinik skor (PAS ≥7), nötrofilik lökositoz ve ultrasonografide >6 mm basılanamayan kör sonlanan apendiks ile lümende apendikolit saptanması Akut Apandisit tanısını kesinleştirir.",
                        "new_finding": "Kesin Tanı: Akut Apandisit.",
                    },
                    {
                        "text": "Akut İleokolik İntususepsiyon (İnvajinasyon)",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografide iç içe geçmiş bağırsak ansına ait hedef işareti (target sign) değil, kör sonlanan 9.5 mm çapında tübüler apendiks ve apendikolit saptandı.",
                        "teaching_point": "İnvajinasyon genellikle 3-36 ay arası çocuklarda kolik tarzı ağrı atakları ve ultrasonografide hedef/psödo-böbrek işareti ile seyreder.",
                    },
                    {
                        "text": "Sağ Distal Üreterolitiazis (Renal Kolik)",
                        "is_correct": False,
                        "scenario_update": "Tam idrar tetkikinde hematüri saptanmadı, üriner sistem toplayıcı yapıları doğal bulundu ve kalsifiye odak üreterde değil apendiks lümeninde izlendi.",
                        "teaching_point": "Normal idrar tetkiki, peritoneal irritasyon bulguları ve kalsifiye taşın kör sonlanan apendiks lümeninde yer alması üreter taşını dışlar.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Tedavi ve Yatış Planı",
                "question": "Apendikolit eşlikli akut apandisit tanısı kesinleşen bu 9 yaşındaki hastada en doğru yönetim hangisidir?",
                "options": [
                    {
                        "text": "Lümende apendikolit bulunmasına rağmen perforasyon gelişmediği için ameliyatsız yönetim (non-operatif tedavi) amacıyla 10 gün oral amoksisilin-klavulanat reçete edip poliklinik kontrolüyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Apendikolit varlığında ayaktan oral antibiyotikle eve gönderilen hasta 18 saat sonra perfore apandisit ve yaygın peritonit tablosuyla acile tekrar başvurdu.",
                        "teaching_point": "Apendikolit (fekalit) varlığı ameliyatsız (non-operatif) antibiyotik tedavisinde yüksek başarısızlık ve erken perforasyon kriteridir; kesinlikle ayaktan taburcu edilmez.",
                    },
                    {
                        "text": "Perforasyon bulgusu olmadığı için cerrahi konsültasyonu ertesi sabah poliklinik şartlarına bırakmak, acil serviste tek doz intramüsküler seftriakson uygulayarak ağrı kesici şurupla hastayı eve göndermek",
                        "is_correct": False,
                        "scenario_update": "Gece boyunca evde ağrısı ve ateşi artan hastada apendiks lümenindeki taş zemininde nekroz ve lokalize perforasyon gelişti.",
                        "teaching_point": "Akut apandisit tanısı konulan her çocuk acil servisten Çocuk Cerrahisi konsültasyonu ile yatırılarak izlenmelidir.",
                    },
                    {
                        "text": "Cerrahi girişim öncesinde kalın bağırsak temizliği sağlamak amacıyla yüksek hacimli rektal lavman ve oral polietilen glikol solüsyonu uygulayıp 24 saat sonra elektif cerrahi planlamak",
                        "is_correct": False,
                        "scenario_update": "Akut inflame apendiks ve apendikolit varlığında verilen oral laksatif ve lavman intraluminal basıncı artırarak iyatrojenik perforasyona zemin hazırladı.",
                        "teaching_point": "Akut apandisitte preoperatif mekanik bağırsak temizliği veya lavman kesinlikle kontrendikedir; hasta NPO tutulur.",
                    },
                    {
                        "text": "Ağızdan aç izlemi sürdürerek intravenöz idame sıvı ve preoperatif profilaktik antibiyotik başlamak, acil Çocuk Cerrahisi konsültasyonu ile apendektomi için cerrahi servise yatırmak",
                        "is_correct": True,
                        "explanation": "Apendikolit eşlikli akut apandisitte standart yaklaşım NPO, intravenöz hidrasyon, preoperatif profilaktik antibiyotik ve laparoskopik/açık apendektomi için Çocuk Cerrahisi servisine yatıştır.",
                        "new_finding": "Çocuk Cerrahisi tarafından değerlendirilen hasta preoperatif hazırlıkları tamamlanarak laparoskopik apendektomi yapılmak üzere servise yatırıldı.",
                    },
                ],
            },
        ],
    },
    {
        "id": "G18",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "15 Aylık",
        "gender": "Kız",
        "complaint": "Ateş, halsizlik ve bacaklarda yeni fark edilen küçük kırmızı-mor lekeler",
        "history": (
            "Annesi Yeşil Alana 'ateşi var ve isilik gibi birkaç döküntüsü çıktı' diyerek başvuruyor: "
            "'Öğleden beri 39.2°C ateşi var, bir kez kustu. Normalde çok hareketli bir çocuktur ama son 2 "
            "saattir omzuma başını koyup yatıyor, bacakları da biraz soğuk geldi. Bezini değiştirirken "
            "uyluğunda ve bacağında toplu iğne başı gibi koyu kırmızı-mor 5-6 tane leke gördüm.'"
        ),
        "final_diagnosis": "Meningokoksemi (Ateş + Peteşiyal/Purpurik Döküntü ve Kompanse Septik Şok)",
        "disposition": "Yeşil Alanda Saptanıp Derhal Sarı/Kırmızı Alana Devir -> Acil İV Seftriakson & Sıvı Resüsitasyonu -> Çocuk Yoğun Bakım Yatışı",
        "case_pearl": (
            "Ateşli bir çocukta BASMAKLA SOLMAYAN (cam bardak / vitropresyon testi pozitif) peteşi veya "
            "purpura varlığı aksi kanıtlanana kadar Meningokoksemi / İnvaziv Bakteriyel Enfeksiyon "
            "acilidir! Özellikle letarji, ekstremite soğukluğu ve kapiller dolum uzaması eşlik ediyorsa "
            "dakikalar hayati önem taşır; LP veya görüntüleme beklenmeden kan kültürü alınıp ilk 1 saat "
            "içinde İV 3. kuşak sefalosporin (Seftriakson/Sefotaksim) ve sıvı resüsitasyonu "
            "başlanmalıdır."
        ),
        "steps": [
            {
                "stage_title": "Yeşil Alanda İlk Değerlendirme ve Alan Kararı",
                "question": "Yeşil alana ateş, halsizlik ve bacaklarda yeni başlayan döküntü ile getirilen bu 15 aylık bebekte ilk muayene ve alan kararınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Çocuğu tamamen soyarak lezyonlara cam bardakla bası testi uygulamak; kapiller dolum zamanı, bilinç durumu ve periferik nabızları değerlendirip hastayı derhal Sarı Alana devretmek",
                        "is_correct": True,
                        "triggers_yellow_transfer": True,
                        "explanation": "Yüksek ateş, basmakla solmayan peteşi/purpura, letarji ve uzamış kapiller dolum zamanı fulminan seyirli invaziv bakteriyel enfeksiyon ve kompanse şokun alarm bulgularıdır; hasta saniyeler içinde Sarı/Kırmızı Alana alınmalıdır.",
                        "new_finding": "Vital Bulgular: Ateş 39.4°C, KTA 178/dk, SS 42/dk, TA 82/45 mmHg, SpO2 %95. Alt ekstremitelerde ve gövde altında basmakla solmayan 2-4 mm peteşi ve erken ekimotik purpurik lezyonlar mevcut! Ekstremiteler soğuk, kapiller dolum zamanı 4 saniye, çocuk uykuya meyilli. Hasta derhal Sarı Alana devredildi!",
                    },
                    {
                        "text": "Ateşi düşürüp taşikardi ve halsizliğin gerileyip gerilemediğini görmek amacıyla Yeşil Alanda oral parasetamol süspansiyon verip ılık uygulama yapmak ve 1 saat sonra yeniden değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Kritik 1 saatlik bekleme süresinde bacaklardaki mor lekeler hızla tüm gövdeye yayıldı, kapiller dolum 6 saniyeye çıktı ve hipotansif şok gelişti!",
                        "teaching_point": "Ateşli bir çocukta basmakla solmayan peteşi/purpura ve perfüzyon bozukluğu varlığında antipiretik yanıtı beklenmez; dakikalar içinde resüsitasyon başlatılmalıdır.",
                    },
                    {
                        "text": "Bacaklardaki döküntüleri viral ekzantem veya kusmaya bağlı mekanik peteşi olarak değerlendirip Yeşil Alanda tam kan sayımı ve idrar tetkiki isteyerek bekleme salonunda sonuçları beklemek",
                        "is_correct": False,
                        "scenario_update": "Bekleme salonunda geçen 45 dakika içinde purpuralar birleşerek ekimotik plaklara dönüştü ve çocukta bilinç kaybı gelişti.",
                        "teaching_point": "Kusmaya bağlı mekanik peteşiler yalnızca üst kaval kemiği hattının üzerinde, baş-boyun bölgesinde görülür; alt ekstremitedeki ateşli peteşi/purpura invaziv sepsis göstergesidir.",
                    },
                    {
                        "text": "Yüksek ateş ve uykuya meyil öyküsü nedeniyle santral sinir sistemi enfeksiyonunu doğrulamak üzere Yeşil Alanda sedasyon hazırlığı yaparak öncelikle tanısal lomber ponksiyon işlemi planlamak",
                        "is_correct": False,
                        "scenario_update": "Dolaşım bozukluğu ve olası koagülopatisi olan hastada resüsitasyon yapılmadan denenen lomber ponksiyon kardiyorespiratuar kollapsı tetikledi.",
                        "teaching_point": "Perfüzyon bozukluğu (soğuk ekstremite, uzamış KDZ, letarji) ve yaygın purpura varlığında lomber ponksiyon kontrendikedir; önce ABC stabilizasyonu ve antibiyotik uygulanır.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda İlk Saat Resüsitasyon ve Tetkik Yaklaşımı",
                "question": "Hastayı Sarı Alana aldınız ve monitörize ettiniz. İlk 15-30 dakikadaki en doğru müdahale ve tetkik sırası nedir?",
                "options": [
                    {
                        "text": "Beyin omurilik sıvısı kültürünün steril kalmasını önlemek amacıyla antibiyotik ve sıvı bolusu vermeden önce acil lomber ponksiyon uygulamak, ardından kraniyal bilgisayarlı tomografi görüntülemesine göndermek",
                        "is_correct": False,
                        "scenario_update": "Hemodinamisi unstabil ve trombositopenisi/koagülopatisi olan hastada LP ve BT için antibiyotiğin geciktirilmesi şoku derinleştirdi ve spinal hematom riski yarattı!",
                        "teaching_point": "Şok bulguları ve purpura/koagülopati varlığında lomber ponksiyon kesinlikle yapılmaz; parenteral antibiyotik tedavisi LP veya görüntüleme için geciktirilemez.",
                    },
                    {
                        "text": "Oksijen başlayıp damar yolu açarak kan kültürü, hemogram, koagülasyon, prokalsitonin ve kan gazı almak; beklemeksizin intravenöz seftriakson ve 20 mL/kg izotonik kristaloid bolusu uygulamak",
                        "is_correct": True,
                        "explanation": "Pediatrik sepsis kılavuzlarına göre damar yolu açılır açılmaz kan kültürü alınır, lomber ponksiyon beklenmeden ilk saat içinde intravenöz seftriakson (100 mg/kg/gün dozunda) ve 20 mL/kg %0.9 NaCl bolusu verilir.",
                        "new_finding": "Damar yolu açıldı, kan kültürü alındı ve ilk doz intravenöz seftriakson + 20 mL/kg %0.9 NaCl bolusu uygulandı. LABORATUVAR: WBC 21.400/mm³, PLT 88.000/mm³, CRP 115 mg/L, Prokalsitonin 18 ng/mL, Laktat 4.1 mmol/L, INR 1.6. Bolus sonrası KTA 145/dk'ya, KDZ 2 saniyeye geriledi.",
                    },
                    {
                        "text": "Kan basıncı henüz 82/45 mmHg düzeyinde korunduğu için intravenöz sıvı bolusu vermekten kaçınmak; yalnızca idame hızında sıvı başlayıp kültür ve koagülasyon sonuçları çıkınca antibiyotik seçmek",
                        "is_correct": False,
                        "scenario_update": "Çocuklarda hipotansiyon şokun çok geç bir bulgusudur; bolus verilmeyen ve antibiyotiği bekletilen hastada 30 dakika içinde dekompanse hipotansif şok gelişti.",
                        "teaching_point": "Pediatrik kompanse şokta taşikardi, uzamış kapiller dolum ve soğuk ekstremite varlığında hipotansiyon gelişmesi beklenmeden derhal 20 mL/kg izotonik sıvı bolusu ve ampirik seftriakson başlanmalıdır.",
                    },
                    {
                        "text": "Trombositopeni ve purpurik döküntülerin immün aracılı olabileceği düşüncesiyle antibiyotik başlamadan önce intravenöz immünglobulin ve yüksek doz metilprednizolon infüzyonu hazırlayarak acil çocuk hematoloji konsültasyonu istemek",
                        "is_correct": False,
                        "scenario_update": "Akut bakteriyel sepsis ve dissemine intravasküler koagülasyon tablosunda antibiyotik yerine immünsüpresif steroid verilmesi bakteriyemiyi hızlandırdı.",
                        "teaching_point": "Yüksek ateş, letarji ve şok bulguları eşliğindeki akut purpura ve trombositopeni aksi kanıtlanana kadar invaziv bakteriyel sepsis ve DİK olarak yönetilir.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Kesin Tanı",
                "question": "Klinik tablo ve laboratuvar bulguları (lökositoz, trombositopeni, yüksek prokalsitonin/laktat, INR uzaması ve ateşli purpura) ile kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Henoch-Schönlein Purpurası (IgA Vasküliti)",
                        "is_correct": False,
                        "scenario_update": "IgA vaskülitinde çocuk toksik görünmez, septik şok gelişmez ve trombosit sayısı ile koagülasyon parametreleri tamamen normaldir.",
                        "teaching_point": "Yüksek ateş, şok bulguları, yüksek prokalsitonin ve trombositopeni/koagülopati varlığında purpura vaskülit değil meningokoksemi ve DİK lehinedir.",
                    },
                    {
                        "text": "Akut İmmün Trombositopenik Purpura (İTP)",
                        "is_correct": False,
                        "scenario_update": "İTP'de genel durumu çok iyi olan afebril çocukta izole trombositopeni görülür; lökositoz, INR uzaması, laktat yüksekliği ve şok bulunmaz.",
                        "teaching_point": "Toksik görünüm, 39.4°C ateş, yüksek akut faz reaktanları ve koagülopati İTP tanısını kesin olarak dışlar.",
                    },
                    {
                        "text": "Meningokoksemi ve Septik Şok",
                        "is_correct": True,
                        "explanation": "Akut yüksek ateş, alt ekstremitelerden hızla yayılan basmakla solmayan peteşi/purpura, taşikardi, uzamış KDZ, hiperlaktatemi ve tüketim koagülopatisi Meningokoksemi ve kompanse septik şok için tanısaldır.",
                        "new_finding": "Kesin Tanı: Meningokoksemi (İnvaziv Meningokokal Hastalık) ve Kompanse Septik Şok.",
                    },
                    {
                        "text": "Tipik Hemolitik Üremik Sendrom (HÜS)",
                        "is_correct": False,
                        "scenario_update": "Öyküde kanlı ishal prodromu olmayıp birkaç saat içinde hiperakut başlayan yüksek ateş, yaygın purpura ve septik şok tablosu mevcuttur.",
                        "teaching_point": "HÜS genellikle kanlı ishal sonrası solukluk, oligo-anüri ve normal koagülasyon (INR normal) ile seyreder; hiperakut ateşli purpura ve şok meningokoksemidir.",
                    },
                ],
            },
            {
                "stage_title": "İzlem, İzolasyon ve Temaslı Kemoprofilaksisi",
                "question": "İlk resüsitasyonu yapılan bu meningokoksemi hastasında yatış, izolasyon ve halk sağlığı yönetimi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Sıvı bolusu sonrası kapiller dolum zamanı düzeldiği için hastayı izolasyonsuz genel pediatri servisine yatırmak ve yalnızca ateş gelişen aile bireylerine oral amoksisilin profilaksisi önermek",
                        "is_correct": False,
                        "scenario_update": "Genel serviste izlenen hastada 4. saatte dirençli hipotansiyon ve adrenal yetmezlik gelişti; ayrıca amoksisilin nazofaringeal meningokok taşıyıcılığını eradike edemedi.",
                        "teaching_point": "Meningokoksemi hastaları Çocuk Yoğun Bakım Ünitesinde damlacık izolasyonu altında izlenmeli ve tüm ev içi temaslılara asemptomatik olsalar dahi rifampisin, seftriakson veya siprofloksasin ile kemoprofilaksi verilmelidir.",
                    },
                    {
                        "text": "İlk doz intravenöz seftriakson ve sıvı resüsitasyonu sonrası vital bulguları stabilize olan hastayı 6 saat acil gözlemde tutup günlük intramüsküler seftriakson tedavisiyle ayaktan kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Meningokoksemi ve erken DİK tablosundaki hastanın taburcu edilmesi saatler içinde gelişebilecek Waterhouse-Friderichsen sendromu nedeniyle ölümcül risk oluşturdu.",
                        "teaching_point": "Meningokoksemi şüphesi veya tanısı olan hiçbir hasta acil servisten taburcu edilemez; yoğun bakım şartlarında yakın monitörizasyon zorunludur.",
                    },
                    {
                        "text": "Hava yolu (negatif basınçlı oda) izolasyonu altında Çocuk Yoğun Bakım Ünitesine yatırmak ve hastanın kreş ile ev içi temaslılarına 10 gün süreyle oral trimetoprim-sülfametoksazol profilaksisi başlamak",
                        "is_correct": False,
                        "scenario_update": "Neisseria meningitidis hava yoluyla değil büyük damlacıklarla bulaşır ve trimetoprim-sülfametoksazol meningokok kemoprofilaksisinde önerilen bir ajan değildir.",
                        "teaching_point": "Meningokok enfeksiyonlarında etkili antibiyotik tedavisinin ilk 24 saati boyunca damlacık izolasyonu uygulanır; kemoprofilakside rifampisin (2 gün), tek doz İM seftriakson veya erişkinde tek doz siprofloksasin kullanılır.",
                    },
                    {
                        "text": "Damlacık izolasyonuyla Çocuk Yoğun Bakım Ünitesine yatırmak, hemodinamik ve DİK izlemi yapmak, zorunlu bildirimde bulunup ev içi temaslılara rifampisin veya seftriakson kemoprofilaksisi planlamak",
                        "is_correct": True,
                        "explanation": "Meningokoksemi hastası ilk 24 saat damlacık izolasyonu ile Çocuk Yoğun Bakım Ünitesinde izlenmeli, Sağlık Bakanlığı bildirimi yapılmalı ve yakın temaslılara en kısa sürede (tercihen ilk 24 saatte) kemoprofilaksi başlanmalıdır.",
                        "new_finding": "Hasta damlacık izolasyonu altında Çocuk Yoğun Bakım Ünitesine yatırıldı ve ev içi yakın temaslılara kemoprofilaksi düzenlendi.",
                    },
                ],
            },
        ],
    },
    {
        "id": "G19",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "4.5 Aylık",
        "gender": "Erkek",
        "complaint": "Burun tıkanıklığı, öksürük ve bugün başlayan hızlı nefes alıp verme",
        "history": (
            "Annesi Yeşil Alana 'nezlesi ve öksürüğü var, şurup yazdırmak istiyorum' diyerek getiriyor: '3 "
            "gündür burnu akıyordu ve hapşırıyordu. Ama bu sabahtan beri nefes alırken karnı ve "
            "kaburgalarının arası içeri çöküyor, memeyi ağzına alıp 2-3 kez çekip nefes alamadığı için "
            "bırakıyor. Bez sayısı da bugün yarıya düştü.'"
        ),
        "final_diagnosis": "Orta-Ağır Akut Bronşiolit (Hipoksemik ve Beslenme Güçlüğü Olan Süt Çocuğu)",
        "disposition": "Yeşil Alanda Saptanıp Sarı Alana Devir -> Oksijen, Nazal Aspirasyon ve Hidrasyon -> Pediatri Servis Yatışı",
        "case_pearl": (
            "<2 yaş (özellikle <6 ay) bebeklerde viral ÜSYE prodromu sonrası gelişen ilk hışıltı "
            "(wheezing), takipne ve çekilme Akut Bronşiolittir. Yeşil alana 'öksürük/nezle' diye başvuran "
            "süt çocuklarında göğüs duvarı soyularak solunum sayısı, çekilmeler ve SpO2 mutlaka "
            "ölçülmelidir. SpO2 <%90-92, belirgin çekilme, takipne (>60/dk) ve beslenememe Sarı Alana "
            "devir ve yatış endikasyonudur."
        ),
        "steps": [
            {
                "stage_title": "Yeşil Alanda Solunum Değerlendirmesi ve Alan Kararı",
                "question": "Yeşil alana öksürük ve burun tıkanıklığı ile getirilen bu 4.5 aylık bebekte ilk muayene ve alan kararınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Üst solunum yolu enfeksiyonuna bağlı burun tıkanıklığı düşünerek Yeşil Alanda serum fizyolojik burun damlası uygulamak ve oksijen satürasyonu ölçmeden anneye bebeği emzirmesini söyleyerek bekletmek",
                        "is_correct": False,
                        "scenario_update": "Göğsü açılmayan ve SpO2 ölçümü yapılmayan bebekte emzirme sırasında şiddetli desatürasyon ve morarma gelişti.",
                        "teaching_point": "Öksürük, emmeme ve hızlı nefes alma öyküsü olan her süt çocuğunda göğüs tamamen açılarak çekilmeler değerlendirilmeli ve pulse oksimetre ile SpO2 ölçülmelidir.",
                    },
                    {
                        "text": "Bebeğin göğüs duvarını açarak solunum sayısını, interkostal-subkostal çekilmeleri, oskültasyon bulgularını ve oda havasında SpO2 değerini ölçüp hastayı Sarı Alana devretmek",
                        "is_correct": True,
                        "triggers_yellow_transfer": True,
                        "explanation": "Süt çocuğunda takipne (>60/dk), interkostal/subkostal çekilme, beslenememe ve hipoksemi akut alt solunum yolu obstrüksiyonunun ağırlaştığını gösterir; hasta derhal Sarı Alana devredilmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 37.9°C, KTA 156/dk, Solunum Sayısı 64/dk, Oda havasında SpO2 %89. Belirgin subkostal ve interkostal çekilmeler ile burun kanadı solunumu mevcut. Oskültasyonda ekspiryum uzun, bilateral yaygın sibilan ronküsler ve ince krepitan raller duyuluyor. Hasta Sarı Alana devredildi!",
                    },
                    {
                        "text": "Oskültasyonda duyulan sibilan ronküsler nedeniyle hastayı Yeşil Alanda tutarak 20 dakika arayla 3 doz nebülize salbutamol uygulamak ve oral prednizolon şurup vererek yanıtı beklemek",
                        "is_correct": False,
                        "scenario_update": "Oksijen desteği verilmeden Yeşil Alanda uygulanan ardışık salbutamol nebülleri bebeğin taşikardisini 190/dk'ya çıkardı, SpO2 %88'de kaldı ve solunum iş yükü azalmadı.",
                        "teaching_point": "Hipoksemik (SpO2 <%90) süt çocuğu Yeşil Alanda tutulamaz; ayrıca küçük süt çocuklarının ilk viral alt solunum yolu hışıltısında rutin bronkodilatör ve steroid önerilmez.",
                    },
                    {
                        "text": "Öksürük ve hızlı solunumu bakteriyel pnömoni başlangıcı kabul ederek Yeşil Alanda PA akciğer grafisi istemek ve oral amoksisilin-klavulanat ile dekstrometorfan şurup reçete edip eve göndermek",
                        "is_correct": False,
                        "scenario_update": "Hipoksemik ve beslenemeyen 4.5 aylık bebekte solunum yetmezliği riski atlandı ve süt çocuklarında kontrendike olan antitussif şurup reçete edildi.",
                        "teaching_point": "Süt çocuklarında öksürük kesici (antitussif/mukolitik) ilaçlar kesinlikle kontrendikedir; hipoksemik bebek acil gözleme alınmalıdır.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Stabilizasyon ve Tedavi Yaklaşımı",
                "question": "Sarı Alana devraldığınız (SpO2 %89, SS 64/dk, çekilmeleri olan ve ememeyen) bu 4.5 aylık bebekte kanıta dayalı ilk müdahale ne olmalıdır?",
                "options": [
                    {
                        "text": "Rutin olarak tam kan sayımı, CRP ve akciğer grafisi çekmek; intravenöz metilprednizolon, ampisilin-sulbaktam ve sekresyon mobilizasyonu için agresif göğüs fizyoterapisi (tapotman) uygulamak",
                        "is_correct": False,
                        "scenario_update": "Agresif göğüs perküsyonu/tapotman bebeğin ağlamasını ve oksijen tüketimini artırarak desatürasyonu derinleştirdi; steroid ve antibiyotik klinik fayda sağlamadı.",
                        "teaching_point": "Güncel uluslararası kılavuzlarda viral alt hava yolu obstrüksiyonunda rutin akciğer grafisi, kan tetkiki, sistemik/inhale kortikosteroidler, antibiyotikler ve göğüs fizyoterapisi önerilmemektedir.",
                    },
                    {
                        "text": "Solunum sayısı 64/dk iken dehidratasyonu önlemek amacıyla bebeği biberonla beslemeye devam etmek ve eş zamanlı ardışık nebülize ipratropium bromür ile salbutamol kombinasyonu uygulamak",
                        "is_correct": False,
                        "scenario_update": "Dakikada 64 kez nefes alan bebekte emme-yutma-solunum koordinasyonu bozulduğu için mama aspirasyonu ve akut desatürasyon gelişti!",
                        "teaching_point": "Solunum sayısı >60/dk olan süt çocuklarında aspirasyon riski çok yüksektir; takipne gerileyene kadar ağızdan beslenme kesilerek intravenöz veya nazogastrik hidrasyon sağlanmalıdır.",
                    },
                    {
                        "text": "Başı 30 derece yükseltip nazal aspirasyon yapmak, SpO2 >%92 tutacak şekilde oksijen başlamak ve aspirasyon riski nedeniyle oral beslenmeyi kesip intravenöz hidrasyon sağlamak",
                        "is_correct": True,
                        "explanation": "Zorunlu burun solunumu yapan süt çocuklarında yüzeyel nazal aspirasyon üst hava yolu direncini düşürür; SpO2 <%90-92 olduğunda oksijen desteği ve SS >60/dk iken intravenöz/NG hidrasyon tedavinin kanıtlanmış temel taşlarıdır.",
                        "new_finding": "Yüzeyel nazal aspirasyon ve 2 L/dk nemlendirilmiş oksijen desteği sonrası bebeğin SpO2 değeri %96'ya yükseldi, solunum sayısı 54/dk'ya geriledi. Damar yolu açılarak izotonik idame sıvı tedavisi başlandı.",
                    },
                    {
                        "text": "Nazal aspirasyon yapmadan doğrudan derin endotrakeal aspirasyon uygulamak, rutin arteriyel kan gazı almak ve solunum iş yükünü baskılamak amacıyla düşük doz intravenöz midazolam sedasyonu başlamak",
                        "is_correct": False,
                        "scenario_update": "Derin aspirasyon mukozal ödeme ve laringospazma yol açarken, verilen sedatif solunum dürtüsünü baskılayarak apne atağı tetikledi!",
                        "teaching_point": "Derin nazofaringeal/trakeal aspirasyon mukozal travma ve refleks bradikardi/apne yaptığı için önerilmez; entübe olmayan solunum sıkıntılı süt çocuğuna sedatif verilmez.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Kesin Tanı",
                "question": "Mevcut anamnez ve fizik muayene bulgularıyla bu 4.5 aylık bebekte kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Orta-Ağır Akut Bronşiolit",
                        "is_correct": True,
                        "explanation": "4.5 aylık süt çocuğunda 3 günlük viral ÜSYE prodromu sonrası gelişen ilk wheezing/ince ral atağı, takipne (64/dk), çekilmeler, hipoksemi (SpO2 %89) ve beslenme güçlüğü Orta-Ağır Akut Bronşiolit tanısını koydurur.",
                        "new_finding": "Kesin Tanı: Orta-Ağır Akut Bronşiolit.",
                    },
                    {
                        "text": "Akut Viral Laringotrakeit (Krup)",
                        "is_correct": False,
                        "scenario_update": "Hastada inspiratuar stridor ve havlar tarzda kaba öksürük değil, ekspiryum uzaması, yaygın sibilan ronküsler ve ince krepitan raller mevcuttur.",
                        "teaching_point": "Krup üst hava yolu (subglottik) darlığıdır ve inspiratuar stridorla seyreder; bronşiolit ise alt solunum yollarının (bronşiollerin) obstrüksiyonudur.",
                    },
                    {
                        "text": "Bronşiyal Yabancı Cisim Aspirasyonu",
                        "is_correct": False,
                        "scenario_update": "Henüz ek gıdaya geçmemiş 4.5 aylık bebekte ani başlayan boğulma/öksürük krizi öyküsü olmayıp 3 günlük rinit prodromu ve bilateral simetrik oskültasyon bulguları vardır.",
                        "teaching_point": "Viral prodrom ve bilateral simetrik sibilan ronküs/ince raller akut bronşiolit lehinedir; yabancı cisim aspirasyonunda ani başlangıç ve asimetrik solunum sesleri beklenir.",
                    },
                    {
                        "text": "Akut Bakteriyel Lober Pnömoni",
                        "is_correct": False,
                        "scenario_update": "Bebekte toksik görünüm, yüksek ateş veya fokal konsolidasyon (bronşiyal solunum sesi/matite) yerine yaygın bilateral sibilan ronküsler ve ekspiryum uzaması ön plandadır.",
                        "teaching_point": "Subfebril ateş ve yaygın bilateral wheezing/ince raller süt çocuğunda viral bronşiolit için tipiktir.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Yatış ve İzlem Kararı",
                "question": "Oda havasında hipoksemisi (SpO2 %89), takipnesi ve beslenme güçlüğü olan 4.5 aylık bu bebekte son kararınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Oksijen altında SpO2 değeri %96'ya yükseldiği için oksijen desteğini kesip evde kullanmak üzere nebülize salbutamol ve budesonid reçete ederek 24 saat sonra poliklinik kontrolüyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Oksijen kesildikten 20 dakika sonra bebeğin SpO2 değeri tekrar %88'e düştü, subkostal çekilmeleri arttı ve emmeyi reddetti.",
                        "teaching_point": "Oda havasında SpO2 <%90-92 olan ve oral alımı yarıdan fazla azalmış küçük süt çocuğu acil servisten taburcu edilemez.",
                    },
                    {
                        "text": "Acil gözlemde tek doz intramüsküler deksametazon ve seftriakson uyguladıktan sonra 2 saat izleyip solunum sayısı 54/dk düzeyindeyken oral beslenmeye geçerek hastayı eve göndermek",
                        "is_correct": False,
                        "scenario_update": "Etkisiz medikal tedavilerle eve gönderilen bebek gece solunum yorgunluğu ve dehidratasyon nedeniyle acil servise yeniden getirildi.",
                        "teaching_point": "Orta-ağır bronşiolitte parenteral steroid veya antibiyotik yatış ihtiyacını ortadan kaldırmaz; hasta oksijen ve hidrasyon desteği için yatırılmalıdır.",
                    },
                    {
                        "text": "Rutin olarak tüm orta-ağır bronşiolit hastalarına uygulanan erken endotrakeal entübasyon ve mekanik ventilasyon amacıyla bebeği doğrudan üçüncü basamak yoğun bakım ünitesine entübe ederek nakletmek",
                        "is_correct": False,
                        "scenario_update": "Nazal aspirasyon ve düşük akımlı oksijenle SpO2'si %96'ya çıkan ve apnesi olmayan bebekte gereksiz invaziv mekanik ventilasyon girişimi planlandı.",
                        "teaching_point": "Düşük akımlı oksijen veya HFNC ile stabilize olan, apnesi ve hiperkapnik solunum yetmezliği bulunmayan orta-ağır bronşiolit vakaları genel pediatri servisinde izlenir.",
                    },
                    {
                        "text": "Oda havasında hipoksemisi, takipnesi ve beslenme güçlüğü süren 4.5 aylık bebeği oksijen desteği, hidrasyon ve yakın solunum/apne izlemi amacıyla Pediatri servisine yatırmak",
                        "is_correct": True,
                        "explanation": "Oda havasında SpO2 <%90-92 olması, orta-ağır solunum sıkıntısı (belirgin çekilmeler, takipne) ve oral beslenmenin yarıdan fazla azalması kesin hastane yatış endikasyonudur.",
                        "new_finding": "Bebek nemlendirilmiş oksijen ve intravenöz hidrasyon desteği altında Çocuk Sağlığı ve Hastalıkları servisine yatırıldı.",
                    },
                ],
            },
        ],
    },
    {
        "id": "G20",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "7 Yaş",
        "gender": "Erkek",
        "complaint": "Kaşıntı, kızarıklık ve yeni başlayan öksürük / kusma",
        "history": (
            "Babası Yeşil Alana 'alerji oldu, kaşınıyor' diyerek getiriyor: 'Yarım saat önce doğum günü "
            "partisinde fıstıklı pasta yemişti. Önce boynunda ve kollarında kaşıntılı kabarıklıklar çıktı. "
            "Yeşil alan sırasında beklerken 2 kez kustu, şimdi de boğazım daralıyor diyor, sesi biraz "
            "çatallı çıkıyor ve kuru kuru öksürmeye başladı.'"
        ),
        "final_diagnosis": "Anafilaksi (Besin Alerjeni Tetikli Çoklu Sistem Tutulumu)",
        "disposition": "Yeşil Alanda Saptanıp Derhal Sarı/Kırmızı Alana Devir -> Acil İM Adrenalin -> Gözlem ve Adrenalin Oto-enjektör Reçetesi",
        "case_pearl": (
            "Bilinen veya olası bir alerjen maruziyeti sonrası dakikalar-saatler içinde başlayan "
            "deri/mukoza bulgularına (ürtiker, anjiyoödem, kaşıntı) SOLUNUM (stridor, ses kısıklığı, "
            "wheezing, dispne), DOLAŞIM (hipotansiyon, taşikardi, senkop) veya GİS (dirençli kusma, kramp "
            "tarzı karın ağrısı) bulgularından en az birinin eşlik etmesi ANAFİLAKSİDİR! İlk ve hayat "
            "kurtarıcı tedavi uyluk anterolateraline (vastus lateralis) İM Adrenalin (0.01 mg/kg, 1:1000) "
            "uygulanmasıdır."
        ),
        "steps": [
            {
                "stage_title": "Yeşil Alanda Değerlendirme ve Acil Müdahale Kararı",
                "question": "Yeşil alana kaşıntı ve döküntü şikayetiyle giren ancak kusma, ses boğukluğu ve öksürük eklenen bu 7 yaşındaki çocukta ilk kararınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Hastayı Sarı Alana devredip periferik damar yolu açarak öncelikle intravenöz feniramin ve 1-2 mg/kg metilprednizolon uygulamak, yalnızca arteriyel hipotansiyon gelişirse intramüsküler adrenalin planlamak",
                        "is_correct": False,
                        "scenario_update": "Antihistaminik ve etkisi saatler sonra başlayan kortikosteroid laringeal ödemi durduramadı; hastanın stridoru artarak SpO2 değeri %84'e geriledi!",
                        "teaching_point": "Çoklu sistem tutulumu ve hava yolu obstrüksiyonu bulgularında adrenalin için hipotansiyon gelişmesi beklenmez; antihistaminik ve steroidler adrenalinin yerini asla tutmaz.",
                    },
                    {
                        "text": "Yeşil Alanda oral setirizin şurup ve soğuk buhar uygulayarak 30 dakika beklemek, kusması devam ederse intramüsküler ondansetron yapıp klinik semptomların gerileyip gerilemediğini kontrol etmek",
                        "is_correct": False,
                        "scenario_update": "Oral antihistaminik ve antiemetik ile Yeşil Alanda bekletilen çocukta dakikalar içinde tam üst hava yolu obstrüksiyonu ve hipoksik bradikardi gelişti!",
                        "teaching_point": "Alerjen maruziyeti sonrası deri bulgularına solunum ve gastrointestinal semptomların eklenmesi hayatı tehdit eden sistemik reaksiyonu gösterir; Yeşil Alanda bekletilemez.",
                    },
                    {
                        "text": "Çoklu sistem tutulumu (deri-mukoza, gastrointestinal ve akut solunum obstrüksiyonu) saptayarak hastayı Sarı/Kırmızı Alana devretmek ve vastus lateralis kas içine 0.01 mg/kg adrenalin uygulamak",
                        "is_correct": True,
                        "triggers_yellow_transfer": True,
                        "explanation": "Şüpheli besin alımı sonrası dakikalar içinde gelişen ürtiker + tekrarlayan kusma + laringeal/bronşiyal obstrüksiyon bulgularında ilk ve hayat kurtarıcı basamak uyluk üst-dış yanından (vastus lateralis) intramüsküler 0.01 mg/kg (1:1000) adrenalin uygulanması ve Sarı/Kırmızı Alana devirdir.",
                        "new_finding": "Vital Bulgular: KTA 142/dk, SS 32/dk, TA 88/52 mmHg, SpO2 %92. Yaygın ürtiker plakları, alt dudakta ödem, seste boğukluk, inspiratuar stridor ve bilateral ekspiratuar wheezing mevcut. Hasta derhal Sarı Alana alındı ve sol uyluk anterolateralinden 0.25 mg intramüsküler adrenalin uygulandı!",
                    },
                    {
                        "text": "Solunum seslerindeki boğukluk ve hışıltıyı akut bronkospazm olarak değerlendirip Yeşil Alanda yalnızca ardışık nebülize salbutamol ve inhale budesonid uygulayarak hastayı oturur pozisyonda yakından izlemek",
                        "is_correct": False,
                        "scenario_update": "Nebülize salbutamol üst hava yolundaki (laringeal) anjiyoödemi ve sistemik mediyatör salınımını engelleyemediği için stridor ve dolaşım bozukluğu ilerledi.",
                        "teaching_point": "İnhale beta-2 agonistler laringeal ödemi ve mukozal kapiller sızıntıyı düzeltmez; birincil tedavi alfa-1 ve beta-2 agonisti olan intramüsküler adrenalindir.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda İkincil Destek ve Resüsitasyon Yönetimi",
                "question": "Sarı Alanda ilk doz intramüsküler adrenalin uygulandı. Bu aşamada eş zamanlı yapılması gereken doğru destek tedavileri nelerdir?",
                "options": [
                    {
                        "text": "Uygun pozisyon verip oksijen başlamak, damar yolu açarak 20 mL/kg izotonik kristaloid, bronkospazm için nebülize salbutamol ve yardımcı olarak H1-antihistaminik ile metilprednizolon uygulamak",
                        "is_correct": True,
                        "explanation": "İntramüsküler adrenalin sonrası hava yolu/oksijen desteği, damar yolu açılarak intravasküler hacim desteği (%0.9 NaCl), alt hava yolu obstrüksiyonu için nebülize salbutamol ve ikincil ilaçlar uygulanır; 5-15 dakikada yanıt değerlendirilir.",
                        "new_finding": "İntramüsküler adrenalin, oksijen, izotonik sıvı desteği ve nebülize salbutamol sonrası 8. dakikada ses boğukluğu ve wheezing düzeldi; SpO2 %99, TA 105/68 mmHg, KTA 110/dk ölçüldü.",
                    },
                    {
                        "text": "İlk doz intramüsküler adrenalinden hemen 2 dakika sonra tam yanıt alınamadığı düşüncesiyle 1:1000 konsantrasyondaki adrenalini sulandırmadan 0.25 mg dozunda hızlı intravenöz puşe olarak uygulamak",
                        "is_correct": False,
                        "scenario_update": "Sulandırılmamış (1:1000) adrenalinin hızlı intravenöz puşe yapılması şiddetli hipertansif kriz ve ventriküler taşikardi atağı tetikledi!",
                        "teaching_point": "Adrenalin 5-15 dakika arayla intramüsküler olarak tekrarlanabilir; sulandırılmamış (1:1000) intravenöz puşe adrenalin ölümcül kardiyak aritmi ve miyokardiyal iskemiye yol açar.",
                    },
                    {
                        "text": "Solunumunun rahatlaması ve kusmasının geçmesi için çocuğu sedyeden kaldırarak acil servis koridorunda yürütmek ve ağızdan bol su içirerek alerjenin mideden hızla temizlenmesini sağlamak",
                        "is_correct": False,
                        "scenario_update": "Vazodilatasyon ve kapiller sızıntısı olan hastanın aniden ayağa kaldırılması venöz dönüşü düşürerek senkop ve hipotansif kollapsa neden oldu!",
                        "teaching_point": "Akut sistemik alerjik reaksiyon sırasında hasta kesinlikle ayağa kaldırılmaz veya yürütülmez (boş ventrikül sendromu / ani kardiyak arrest riski); sırtüstü bacaklar yükseltilmiş veya solunum sıkıntısı varsa bacaklar uzatılarak yarı oturur pozisyonda tutulur.",
                    },
                    {
                        "text": "Stridor ve wheezing bulguları devam ederken oksijen veya sıvı desteği vermeden önce kesin tanı koymak amacıyla serum triptaz düzeyi ve spesifik IgE sonuçları çıkana dek beklemek",
                        "is_correct": False,
                        "scenario_update": "Laboratuvar sonucu beklenirken oksijen ve sıvı desteği geciktirildiği için hipoksemi ve taşikardi derinleşti.",
                        "teaching_point": "Serum triptaz düzeyi tanıyı retrospektif desteklemek için alınabilir ancak sonuçları saatler-günler sürer; acil stabilizasyon hiçbir laboratuvar testi için bekletilmez.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Kesin Tanı",
                "question": "Öykü, fizik muayene ve tedavi yanıtı birlikte değerlendirildiğinde bu hastada kesin tanınız nedir?",
                "options": [
                    {
                        "text": "İzole Akut Ürtiker ve Anjiyoödem",
                        "is_correct": False,
                        "scenario_update": "Hastada yalnızca deri-mukoza bulguları değil, eş zamanlı ses boğukluğu/stridor, bilateral wheezing, hipoksemi ve tekrarlayan kusma mevcuttur.",
                        "teaching_point": "Deri-mukoza bulgularına solunum, dolaşım veya şiddetli gastrointestinal sistem bulgularından en az birinin eşlik etmesi izole ürtiker değil anafilaksidir.",
                    },
                    {
                        "text": "Akut Trakeobronşiyal Yabancı Cisim Aspirasyonu",
                        "is_correct": False,
                        "scenario_update": "Fıstıklı pasta yedikten 30 dakika sonra yaygın ürtiker, dudak ödemi ve kusma ile başlayan ve intramüsküler adrenaline hızla yanıt veren tablo mevcuttur.",
                        "teaching_point": "Yaygın ürtiker-anjiyoödem, kusma ve intramüsküler adrenaline dramatik yanıt mekanik obstrüksiyonu değil sistemik IgE aracılı anafilaksiyi gösterir.",
                    },
                    {
                        "text": "Besin Kaynaklı Akut Bakteriyel Gastroenterit",
                        "is_correct": False,
                        "scenario_update": "Enterotoksin kaynaklı besin zehirlenmesinde yaygın ürtiker, dudak anjiyoödemi, laringeal stridor ve bronkospazm görülmez.",
                        "teaching_point": "Alerjen besin alımı sonrası dakikalar içinde gelişen kusmaya deri ve solunum yolu obstrüksiyonunun eşlik etmesi anafilaksi tanı kriteridir.",
                    },
                    {
                        "text": "Besin Tetikli Akut Anafilaksi",
                        "is_correct": True,
                        "explanation": "WAO/EAACI kriterlerine göre olası alerjen (yer fıstığı) maruziyeti sonrası dakikalar içinde başlayan deri/mukoza tutulumuna (ürtiker, dudak ödemi) solunum (stridor, wheezing, hipoksemi) ve GİS (kusma) bulgularının eşlik etmesi kesin Anafilaksi tanısı koydurur.",
                        "new_finding": "Kesin Tanı: Besin (Yer Fıstığı) Tetikli Anafilaksi.",
                    },
                ],
            },
            {
                "stage_title": "Gözlem Süresi ve Taburculuk Planı",
                "question": "Tedavi sonrası semptomları tamamen düzelen bu anafilaksi hastasında gözlem süresi ve taburculuk planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "İntramüsküler adrenalin sonrası 15. dakikada tüm bulgular ve vital değerler tamamen normale döndüğü için oral antihistaminik reçete ederek hastayı 1. saatin sonunda eve taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Erken taburcu edilen hastada 5 saat sonra evde alerjenle yeni temas olmaksızın bifazik anafilaksi atağı gelişti ve evde oto-enjektör bulunmadığı için hayati tehlike yaşandı!",
                        "teaching_point": "Anafilaksi hastalarının %5-20'sinde ilk ataktan 4-24 saat sonra bifazik reaksiyon gelişebildiğinden hastalar en az 6-12 saat (ağır solunum/hipotansiyon varsa daha uzun) gözlemlenmelidir.",
                    },
                    {
                        "text": "Bifazik reaksiyon riski nedeniyle hastayı en az 6-12 saat gözlemlemek; taburculukta adrenalin oto-enjektör reçete edip kullanım eğitimi, fıstık eliminasyonu ve Çocuk Alerji randevusu vermek",
                        "is_correct": True,
                        "explanation": "Bifazik anafilaksi riski nedeniyle özellikle solunum/dolaşım tutulumu olan vakalar en az 6-12 saat izlenmeli; taburculukta 0.15 mg/0.30 mg kiloya uygun Adrenalin oto-enjektör reçetesi, yazılı eylem planı ve Çocuk Alerji yönlendirmesi mutlaka yapılmalıdır.",
                        "new_finding": "Hasta Sarı Alanda 8 saat sorunsuz izlendi; Adrenalin oto-enjektör kullanım eğitimi, yazılı anafilaksi eylem planı ve Çocuk Alerji randevusu verilerek güvenle taburcu edildi.",
                    },
                    {
                        "text": "Hastayı 8 saat gözlemledikten sonra sadece oral prednizolon ve desloratadin şurup reçete etmek, adrenalin oto-enjektör kararını 1 ay sonraki Çocuk Alerji poliklinik kontrolüne bırakmak",
                        "is_correct": False,
                        "scenario_update": "Poliklinik randevusunu bekleyen çocuk 10 gün sonra eser miktarda fıstık içeren bir bisküvi yedikten sonra evde tekrar anafilaksi geçirdi ve oto-enjektörü olmadığı için müdahale gecikti.",
                        "teaching_point": "Besin tetikli anafilaksi geçiren her hastaya Adrenalin oto-enjektör acil servisten taburcu edilirken reçete edilmeli ve aileye uygulama pratiği gösterilmelidir.",
                    },
                    {
                        "text": "Reaksiyonun gerçekten yer fıstığına bağlı olup olmadığını kesinleştirmek amacıyla taburculuk öncesinde acil gözlem odasında doktor gözetiminde düşük doz oral besin yükleme (provokasyon) testi yapmak",
                        "is_correct": False,
                        "scenario_update": "Akut anafilaksi atağından hemen sonra acil serviste tekrar alerjen verilmesi şiddetli ve dirençli ikinci bir anafilaktik şok tablosunu tetikledi!",
                        "teaching_point": "Acil serviste besin provokasyon testi kesinlikle yapılmaz; şüpheli besin diyetten tamamen çıkarılır ve tanısal testler ataktan en az 4-6 hafta sonra Çocuk Alerji kliniğinde planlanır.",
                    },
                ],
            },
        ],
    },
]
