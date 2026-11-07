# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - S01-S05 (v2 Şartnameye Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "S01",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "14 Aylık",
        "gender": "Kız",
        "complaint": "Dirençli kusma, çok sayıda sulu dışkılama ve belirgin halsizlik",
        "history": (
            "Annesi kucağında halsiz yatan bebeği Sarı Alana getiriyor: 'Dün geceden beri 10-12 kez kustu, "
            "ne içirsek hemen çıkarıyor. Bugün de bezinden taşacak şekilde 8 kez su gibi dışkıladı. "
            "Sabahtan beri bezini hiç ıslatmadı, ağlarken gözyaşı akmıyor, gözleri içine çöktü ve sürekli uyukluyor.'"
        ),
        "final_diagnosis": "Akut Gastroenterit ve Orta-Ağır İzonatremik Dehidratasyon (Metabolik Asidozlu)",
        "disposition": "Sarı Alanda İV İzotonik Bolus + Ondansetron + Rehidratasyon İzlemi Sonrası Oral Alımı Açılıp Taburculuk",
        "case_pearl": (
            "Letarjiye eğilim, çökük göz küreleri, gözyaşı yokluğu, kuru mukozalar, deri turgorunda azalma, "
            "uzamış kapiller dolum ve anüri orta-ağır dehidratasyonu gösterir. Kan şekeri ve elektrolitler "
            "kontrol edilmeli, perfüzyon bozukluğu ve oral intolerans varlığında 20 mL/kg %0.9 NaCl İV bolus "
            "ve antiemetik olarak ondansetron ile rehidratasyon sağlanmalıdır."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Dolaşım Kontrolü",
                "question": "Sarı Alana alınan bu 14 aylık bebekte ilk muayene ve yatak başı değerlendirmede hangi yaklaşımı tercih edersiniz?",
                "options": [
                    {
                        "text": "Öncelikle oral rehidratasyon sıvısını enjektörle beş dakikada bir küçük miktarlarda içirmeyi denemek ve kusup kusmayacağını iki saat boyunca yatak başında gözlemlemek",
                        "is_correct": False,
                        "scenario_update": "Bebek verilen ilk 15 mL sıvıyı hemen fışkırır tarzda kustu; geçen sürede taşikardisi 178/dk düzeyine çıktı ve uykuya meyili belirginleşti.",
                        "teaching_point": "Kapiller dolum süresi uzamış, letarjiye meyilli ve dirençli kusması olan bir süt çocuğunda doğrudan antiemetiksiz oral sıvı denemesi zaman kaybettirir ve perfüzyonu bozar.",
                    },
                    {
                        "text": "Vital bulguları, kapiller dolum süresini, deri turgorunu, fontanel ve göz küresi çöküklüğünü, mukoza ıslaklığını değerlendirip parmak ucu kan şekeri ölçmek",
                        "is_correct": True,
                        "explanation": "Tekrarlayan kusma, sulu dışkılama ve oral alım bozukluğu ile başvuran süt çocuğunda periferik perfüzyon, sıvı açığı bulguları ve kapiller glukoz düzeyi ilk dakikada değerlendirilmelidir.",
                        "new_finding": (
                            "Vital Bulgular: Ateş 37.8°C, KTA 164/dk, SS 38/dk, TA 80/48 mmHg, SpO2 %98. "
                            "Bebek uykuya meyilli, uyaranla ağlıyor ancak gözyaşı yok. Göz küreleri ve ön fontanel çökük, "
                            "ağız mukozası kuru, karın cildinde turgor azalmış, kapiller dolum süresi 3 saniye. "
                            "Parmak ucu kan şekeri: 58 mg/dL. Tartı kaybı önceki ağırlığına göre %8.5 olarak hesaplandı."
                        ),
                    },
                    {
                        "text": "Damar yolu açıp sıvı başlamadan önce invajinasyon veya ileus olasılığını dışlamak amacıyla ayakta direkt karın grafisi ve batın ultrasonografisi istemek",
                        "is_correct": False,
                        "scenario_update": "Radyoloji ünitesinde sıra bekleyen bebeğin kapiller dolum süresi 4 saniyeye uzadı, ekstremiteleri soğudu ve kan şekeri 46 mg/dL düzeyine geriledi.",
                        "teaching_point": "Periferik perfüzyon bozukluğu ve sınırda hipoglisemisi olan bebek hemodinamik olarak stabilize edilmeden görüntüleme ünitesine gönderilmemelidir; ayrıca safrasız kusma ve sulu dışkılamada rutin grafi gerekmez.",
                    },
                    {
                        "text": "Kusmayı hızlıca durdurmak amacıyla intramüsküler metoklopramid uygulayıp otuz dakika bekledikten sonra anne sütü ve su ile oral toleransı test etmek",
                        "is_correct": False,
                        "scenario_update": "Enjeksiyondan yirmi dakika sonra bebekte boyunda kasılma, gözlerin yukarı kayması (okülojirik kriz) gelişti ve dolaşım bulguları daha da bozuldu.",
                        "teaching_point": "Süt çocukları ve küçük çocuklarda metoklopramid akut distonik reaksiyon ve ekstrapiramidal yan etki riski nedeniyle kullanılmamalı; ayrıca dolaşım bozukluğu varken İM ilaç yerine damar yolu tercih edilmelidir.",
                    },
                ],
            },
            {
                "stage_title": "Acil Tetkik ve İlk Saat Stabilizasyon Planı",
                "question": "Taşikardisi (164/dk), kapiller dolum süresi 3 saniye, kan şekeri 58 mg/dL ve dirençli kusması olan bu bebekte ilk müdahale ve tetkik planınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Damar yolu açıp %5 dekstroz ve %0.2 NaCl içeren hipotonik sıvıdan 20 mL/kg hızlı intravenöz bolus vermek ve bazal biyokimya tetkiklerini göndermek",
                        "is_correct": False,
                        "scenario_update": "Hızlı verilen hipotonik sıvı intravasküler alanda kalmayıp hücre içine geçti; kapiller dolum süresi düzelmediği gibi kontrol sodyum değeri 129 mEq/L düzeyine düştü.",
                        "teaching_point": "İntravasküler hacim genişletme (bolus) işlemi asla hipotonik sıvılarla (%5 dekstroz veya %0.2 NaCl) yapılmaz; akut hiponatremi ve beyin ödemine yol açabilir.",
                    },
                    {
                        "text": "Kan gazı ve elektrolit tetkiklerini gönderip sonuçlar çıkana kadar sıvı vermeden beklemek, saptanan asidozu düzeltmek amacıyla intravenöz sodyum bikarbonat puşelemek",
                        "is_correct": False,
                        "scenario_update": "Sonuç beklenirken bebeğin perfüzyonu daha da bozuldu; sıvı açığı yerine konmadan verilen sodyum bikarbonat sonrası serum potasyumu 2.9 mEq/L düzeyine geriledi.",
                        "teaching_point": "Dolaşım bozukluğu bulguları varken laboratuvar sonuçları beklenmeden izotonik kristaloid bolusu başlanmalıdır; dışkıyla bikarbonat kaybına ve hipoperfüzyona bağlı asidoz hidrasyonla düzelir, rutin bikarbonat verilmez.",
                    },
                    {
                        "text": "Kan gazı ve biyokimya alıp 20 mL/kg %0.9 NaCl intravenöz bolus, ardından dekstrozlu rehidratasyon sıvısı ve ondansetron uygulamak",
                        "is_correct": True,
                        "explanation": "Perfüzyon bozukluğu ve sıvı açığı olan bebekte ilk adım 20 mL/kg izotonik kristaloid bolusu ile dolaşımı desteklemek, ardından dekstroz içeren rehidratasyon sıvısına geçmek ve ondansetron ile kusmayı kontrol etmektir.",
                        "new_finding": (
                            "Laboratuvar: Kan gazında pH 7.28, pCO2 28 mmHg, HCO3 13 mmol/L, baz açığı -11 mmol/L, laktat 2.6 mmol/L; "
                            "biyokimyada Na 136 mEq/L, K 3.9 mEq/L, Cl 108 mEq/L, üre 54 mg/dL, kreatinin 0.65 mg/dL. "
                            "20 mL/kg %0.9 NaCl bolusu, ardından %5 dekstrozlu izotonik sıvı ve 0.15 mg/kg ondansetron sonrası "
                            "KTA 128/dk, kapiller dolum süresi 1.5 saniye ve kan şekeri 96 mg/dL ölçüldü."
                        ),
                    },
                    {
                        "text": "Nazogastrik sonda yerleştirerek saatte 50 mL/kg hızında yüksek hacimli oral rehidratasyon solüsyonu infüzyonu başlatmak ve antiemetik ilaç kullanımından kaçınmak",
                        "is_correct": False,
                        "scenario_update": "Yüksek hızda verilen enteral sıvı mide distansiyonuna ve tekrarlayan kusmaya yol açtı; periferik perfüzyon bozukluğu ve taşikardi gerilemedi.",
                        "teaching_point": "Kapiller dolum uzaması, letarji eğilimi ve sınırda hipoglisemi varken başlangıçta hızlı intravenöz izotonik bolus tercih edilmeli; nazogastrik rehidratasyon perfüzyonu stabil hastalarda daha düşük hızda uygulanmalıdır.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Mevcut klinik bulgular ve laboratuvar sonuçlarıyla (Na 136 mEq/L, pH 7.28, HCO3 13 mmol/L) bu hastada kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Akut Gastroenterit ve Orta-Ağır İzonatremik Dehidratasyon",
                        "is_correct": True,
                        "explanation": "Yaklaşık %8-9 tartı kaybı, uzamış kapiller dolum ve letarji eğilimi orta-ağır dehidratasyonu; serum sodyumunun 135-145 mEq/L arasında olması izonatremik tabloyu ve dışkıyla bikarbonat kaybı ise normal anyon açıklı metabolik asidozu gösterir.",
                        "new_finding": "Klinik tanı: Akut Gastroenterit, Orta-Ağır İzonatremik Dehidratasyon ve Metabolik Asidoz.",
                    },
                    {
                        "text": "Akut Gastroenterit ve Ağır Hipernatremik Dehidratasyon",
                        "is_correct": False,
                        "scenario_update": "Hastanın serum sodyum düzeyi 136 mEq/L olup normal referans aralığındadır; hipernatremi saptanmamıştır.",
                        "teaching_point": "Hipernatremik dehidratasyon tanısı için serum sodyum düzeyinin 150 mEq/L üzerinde olması gerekir; bu hastada su ve tuz dengeli kaybedildiği için tablo izonatremiktir.",
                    },
                    {
                        "text": "Yeni Tanı Diyabetik Ketoasidoz ve Hipovolemi",
                        "is_correct": False,
                        "scenario_update": "Hastanın başvuru kan şekeri 58 mg/dL olup hiperglisemi, glukozüri veya ketonemi bulunmamaktadır.",
                        "teaching_point": "Diyabetik ketoasidozda belirgin hiperglisemi (>200 mg/dL) ve ketonemi vardır; süt çocuklarında akut ishal ve kusmada ise açlığa bağlı hipoglisemi eğilimi ve bikarbonat kaybına bağlı asidoz görülür.",
                    },
                    {
                        "text": "Akut İnvajinasyon ve Dekompanse Septik Şok",
                        "is_correct": False,
                        "scenario_update": "Kusmalar safrasızdır, kolik tarzda ağlama krizleri veya kanlı-mukuslu dışkılama yoktur ve tek doz sıvı bolusu ile hemodinami hızla düzelmiştir.",
                        "teaching_point": "İnvajinasyonda aralıklı şiddetli karın ağrısı, safralı kusma ve çilek jölesi dışkılama beklenir; sık sulu dışkılama ve rehidratasyonla hızla düzelen tablo akut gastroenteriti destekler.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alan İzlem ve Taburculuk Kararı",
                "question": "Sarı Alanda 6 saatlik intravenöz rehidratasyon sonrası bilinci tamamen açılan, bol idrar çıkışı olan ve oral rehidratasyon sıvısı ile anne sütünü kusmadan alan hastada yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "İshal tamamen durana kadar anne sütünü ve katı gıdaları kesip yalnızca pirinç lapası ve elma suyu içeren kısıtlı diyetle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Anne sütünün kesilmesi ve düşük kalorili kısıtlı diyet verilmesi enterosit yenilenmesini geciktirerek ishal süresinin uzamasına ve kilo kaybına yol açtı.",
                        "teaching_point": "ESPGHAN kılavuzuna göre akut gastroenteritte rehidratasyon tamamlanır tamamlanmaz anne sütüne ve çocuğun yaşına uygun normal beslenmeye kesintisiz devam edilmelidir; kısıtlı BRAT diyeti önerilmez.",
                    },
                    {
                        "text": "Bağırsak motilitesini azaltarak sıvı kaybını durdurmak amacıyla oral loperamid ve ampirik oral siprofloksasin reçete ederek hastayı evine taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Verilen antimotilite ilaç sonrası bebekte batın distansiyonu, paralitik ileus ve letarji gelişti; hasta tekrar acil servise getirildi.",
                        "teaching_point": "Çocuklarda akut gastroenteritte loperamid gibi antimotilite ilaçlar paralitik ileus, toksik megakolon ve santral sinir sistemi depresyonu riski nedeniyle kesinlikle kontrendikedir; sulu ishalde rutin antibiyotik verilmez.",
                    },
                    {
                        "text": "Klinik düzelmeye rağmen metabolik asidoz öyküsü nedeniyle hastayı en az 48 saat daha parenteral sıvı almak üzere servise yatırmak",
                        "is_correct": False,
                        "scenario_update": "Oral alımı tamamen açılan ve hidrasyonu düzelen bebeğin gereksiz yatışı hastane enfeksiyonu riskini artırdı ve yatak kapasitesini bloke etti.",
                        "teaching_point": "Sarı Alanda 4-6 saatlik rehidratasyon sonrası vital bulguları ve diürezi normale dönen, oral sıvıyı ve beslenmeyi kusmadan tolere eden hastalar güvenle taburcu edilebilir.",
                    },
                    {
                        "text": "Sulu dışkılama sonrası oral rehidratasyon sıvısı, çinko desteği, anne sütüne devam ve kırmızı bayrak eğitimi ile taburcu etmek",
                        "is_correct": True,
                        "explanation": "Hidrasyonu düzelen, diürezi başlayan ve oral alımı kusmadan tolere eden bebeklerde devam eden kayıplar için ORS, 10-14 gün çinko takviyesi, kesintisiz beslenme ve aile eğitimi ile taburculuk standart yaklaşımdır.",
                        "new_finding": "Hasta oral rehidratasyon sıvısı, çinko desteği ve yeniden başvuru kriterleri anlatılarak Sarı Alandan şifa ile taburcu edildi.",
                    },
                ],
            },
        ],
    },
    {
        "id": "S02",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "20 Aylık",
        "gender": "Erkek",
        "complaint": "Yüksek ateş sırasında evde 2 dakika süren tüm vücutta kasılma ve gözlerini dikme",
        "history": (
            "Ailesi panikle Sarı Alana getiriyor: 'Bugün sabahtan beri burnu akıyordu ve ateşi çıktı. "
            "Yarım saat önce evde ateşi 39.4°C iken bir anda gözlerini yukarı dikti, dudakları morardı ve "
            "iki kolu ile bacağı simetrik olarak kasılmaya başladı. Yaklaşık 2 dakika sürdü ve kendiliğinden durdu. "
            "Ambulansta gelirken biraz uyukladı ama şimdi bizi tanıyor ve ağlıyor. Daha önce hiç nöbet geçirmedi.'"
        ),
        "final_diagnosis": "Basit Febril Konvülziyon (Viral Üst Solunum Yolu Enfeksiyonu Zemininde)",
        "disposition": "Sarı Alanda Ateş Kontrolü, Odak Muayenesi ve Gözlem Sonrası Aile Eğitimi ile Taburculuk",
        "case_pearl": (
            "6 ay - 5 yaş arası çocuklarda merkezi sinir sistemi enfeksiyonu veya metabolik bozukluk olmaksızın "
            "ateşle birlikte gelişen, jeneralize, 15 dakikadan kısa süren ve 24 saat içinde tekrarlamayan nöbetler "
            "Basit Febril Konvülziyondur. Bilinci hızla normale dönen, meninks irritasyon bulgusu olmayan tam aşılı "
            "çocukta rutin lomber ponksiyon, EEG, kraniyal görüntüleme veya sürekli antiepileptik ilaç önerilmez."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda Akut Değerlendirme ve Nörolojik Muayene",
                "question": "Kasılması durmuş olarak Sarı Alana getirilen bu 20 aylık çocukta ilk değerlendirmede nasıl bir yaklaşım izlemelisiniz?",
                "options": [
                    {
                        "text": "Tekrar kasılma gelişmesini önlemek amacıyla hemen damar yolu açarak intravenöz diazepam uygulamak ve ardından yirmi dakikada fenitoin yükleme dozuna başlamak",
                        "is_correct": False,
                        "scenario_update": "Aktif nöbeti olmayan çocuğa uygulanan intravenöz diazepam ve fenitoin sonrası çocukta derin sedasyon gelişti; nörolojik bilinç takibi bozuldu ve solunumu yüzeyelleşti.",
                        "teaching_point": "Antikonvülzan ilaçlar yalnızca aktif devam eden (5 dakikayı aşan) nöbetleri sonlandırmak için uygulanır; nöbeti durmuş ve bilinci açılmış hastaya acilde profilaktik yükleme yapılmaz.",
                    },
                    {
                        "text": "Ayrıntılı fizik muayene ve odak araması yapmadan önce santral sinir sistemi enfeksiyonunu dışlamak amacıyla çocuğu doğrudan lomber ponksiyon işlemine almak",
                        "is_correct": False,
                        "scenario_update": "Bilinci açık, aktif ve huzursuz çocukta muayene edilmeden girişilen işlem ailede yoğun panik yarattı ve travmatik ponksiyonla sonuçlandı.",
                        "teaching_point": "Ateş ve nöbetle başvuran çocukta öncelikle bilinç durumu, meninks irritasyon bulguları, fokal nörolojik muayene, aşı öyküsü ve ateş odağı değerlendirilmelidir.",
                    },
                    {
                        "text": "Vital bulguları, kapiller kan şekerini, bilinç durumunu, fokal nörolojik defisit ve meninks irritasyon bulgularını değerlendirip ateş odağı muayenesi yapmak",
                        "is_correct": True,
                        "explanation": "Ateşle birlikte kısa süreli nöbet geçiren çocukta en önemli ilk adım yaşamsal bulguları, kan şekerini, bilinç düzeyini, meninks irritasyon bulgularını ve ateşin kaynağını değerlendirmektir.",
                        "new_finding": (
                            "Vital Bulgular: Ateş 39.1°C, KTA 135/dk, SS 26/dk, SpO2 %99, kapiller kan şekeri 104 mg/dL. "
                            "Çocuk uyanık, annesiyle göz teması kuruyor, GKS 15. Ense sertliği yok, Brudzinski ve Kernig bulguları negatif, "
                            "ekstremite kas güçleri simetrik ve fokal defisit yok. Otoskopi doğal, orofarenks hiperemik ve seröz burun akıntısı mevcut. "
                            "Ulusal aşı takvimine göre tüm aşıları tam."
                        ),
                    },
                    {
                        "text": "Vücut ısısını hızla düşürerek yeni bir atağı engellemek amacıyla soğuk su kompresi uygulamak ve intramüsküler metamizol sodyum enjeksiyonu yapmak",
                        "is_correct": False,
                        "scenario_update": "Soğuk su uygulaması periferik vazokonstriksiyon ve titreme yaratarak çocuğun huzursuzluğunu artırdı; metamizol enjeksiyonu ise hipotansiyon ve agranülositoz riski taşıdığı için uygunsuzdu.",
                        "teaching_point": "Ateş kontrolünde soğuk su veya alkol uygulaması titreme ve vazokonstriksiyonla merkezi ısıyı artırır; çocuklarda ilk tercih oral veya rektal parasetamol ya da ibuprofendir.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Görüntüleme Kararı",
                "question": "20 aylık, aşıları tam, bilinci tamamen açılmış, meninks irritasyon bulgusu olmayan ve üst solunum yolu enfeksiyonu saptanan bu çocukta hangi tetkik yaklaşımı doğrudur?",
                "options": [
                    {
                        "text": "Rutin lomber ponksiyon, kraniyal bilgisayarlı tomografi veya acil elektroensefalografi istemeden oral antipiretik verip Sarı Alanda klinik gözleme almak",
                        "is_correct": True,
                        "explanation": "AAP kılavuzuna göre 18 aydan büyük, tam aşılı, bilinci tamamen normale dönmüş ve meninks irritasyon bulgusu olmayan ilk kısa jeneralize ateşli nöbette rutin LP, nörogörüntüleme, EEG veya geniş biyokimya endike değildir.",
                        "new_finding": "15 mg/kg oral parasetamol verildi. İzlemin 1. saatinde ateş 37.6°C düzeyine geriledi, çocuk Sarı Alan yatağında su içti ve oyuncaklarıyla oynamaya başladı.",
                    },
                    {
                        "text": "İntrakraniyal yer kaplayıcı lezyon veya ödem olasılığını dışlamak amacıyla acil kontrastsız kraniyal bilgisayarlı tomografi ve rutin biyokimya istemek",
                        "is_correct": False,
                        "scenario_update": "Çekilen kraniyal BT ve bakılan serum elektrolitleri tamamen normal saptandı; çocuk gelişmekte olan beyni için gereksiz iyonizan radyasyona maruz kaldı.",
                        "teaching_point": "Fokal özelliği olmayan, 15 dakikadan kısa süren ve nörolojik muayenesi normal olan ilk ateşli nöbette intrakraniyal patoloji saptanma olasılığı çok düşüktür; rutin kraniyal BT çekilmez.",
                    },
                    {
                        "text": "Klinik muayenesi normal olsa bile yirmi dört aylıktan küçük tüm ateşli nöbet hastalarında zorunlu olarak lomber ponksiyon ve kan kültürü yapmak",
                        "is_correct": False,
                        "scenario_update": "Yapılan lomber ponksiyonda BOS hücre sayımı, protein ve glukoz değerleri tamamen normal geldi; invaziv işlem çocukta ve ailede gereksiz travma yarattı.",
                        "teaching_point": "Haemophilus influenzae tip b ve pnömokok aşıları tam olan, 12-18 ay üzerindeki ve menenjit bulgusu taşımayan çocuklarda rutin lomber ponksiyon önerilmemektedir.",
                    },
                    {
                        "text": "İleride gelişebilecek epilepsi riskini öngörmek ve antiepileptik tedavi kararını netleştirmek için taburculuk öncesi acil uyku-uyanıklık elektroensefalografisi çekmek",
                        "is_correct": False,
                        "scenario_update": "Acil koşullarda çekilen EEG postiktal dönemde nonspesifik hafif yavaşlama gösterdi; bu bulgu epilepsi gelişimini öngörmediği halde ailenin kaygısını artırdı.",
                        "teaching_point": "Kısa süreli jeneralize ateşli nöbet sonrasında erken dönemde yapılan EEG gelecekteki nöbet tekrarını veya epilepsi gelişimini öngörmez ve tedavi kararını değiştirmez.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik seyri ve muayene bulguları değerlendirildiğinde bu hastada kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Komplike Febril Konvülziyon",
                        "is_correct": False,
                        "scenario_update": "Nöbet fokal başlamadı, 15 dakikadan uzun sürmedi ve 24 saat içinde tekrarlamadı.",
                        "teaching_point": "Komplike febril konvülziyon diyebilmek için nöbetin fokal olması, 15 dakikadan uzun sürmesi veya aynı 24 saat içinde tekrarlaması gerekir.",
                    },
                    {
                        "text": "Akut Bakteriyel Menenjit",
                        "is_correct": False,
                        "scenario_update": "Çocuğun bilinci hızla açıldı, meninks irritasyon bulgusu yok ve ateş düştüğünde genel durumu tamamen normal.",
                        "teaching_point": "Akut bakteriyel menenjitte letarji, huzursuzluk, ense sertliği veya toksik görünüm ateş düşse dahi devam eder.",
                    },
                    {
                        "text": "Dravet Sendromu (Ağır Miyoklonik Epilepsi)",
                        "is_correct": False,
                        "scenario_update": "İlk kez 20 aylıkken geçirilen 2 dakikalık tek jeneralize nöbet Dravet sendromu kriterleriyle uyumlu değildir.",
                        "teaching_point": "Dravet sendromu genellikle yaşamın ilk yılında başlayan, uzamış hemiklonik veya jeneralize ateşli nöbetler ve gelişim geriliği ile seyreden nadir bir genetik epilepsidir.",
                    },
                    {
                        "text": "Basit Febril Konvülziyon",
                        "is_correct": True,
                        "explanation": "6 ay - 5 yaş arasında, santral sinir sistemi enfeksiyonu olmaksızın ateşle tetiklenen, jeneralize, 15 dakikadan kısa süren ve 24 saatte tekrarlamayan nöbet Basit Febril Konvülziyondur.",
                        "new_finding": "Klinik tanı: Basit Febril Konvülziyon.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alan Gözlem Süresi ve Taburculuk Planı",
                "question": "Sarı Alanda 4 saat izlenen, ateşi kontrol altına alınan, aktif oynayan ve nöbeti tekrarlamayan bu hastada taburculuk yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Nöbet tekrarını önlemek amacıyla iki yıl boyunca düzenli kullanılmak üzere günlük oral sodyum valproat veya fenobarbital profilaksisi başlayarak taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Başlanan kronik antiepileptik ilaç çocukta sersemlik, davranış değişikliği ve karaciğer enzim yüksekliği riski oluştururken epilepsi gelişme riskini değiştirmedi.",
                        "teaching_point": "Basit febril konvülziyonda sürekli antiepileptik ilaçların olası yan etkileri (hepatotoksisite, bilişsel etkilenme) potansiyel yararından çok daha fazladır ve kesinlikle önerilmez.",
                    },
                    {
                        "text": "Antiepileptik başlamadan; aileye tablonun iyi huylu doğasını, tekrarlama riskini ve nöbet anında güvenli yan pozisyon ilk yardımını anlatarak taburcu etmek",
                        "is_correct": True,
                        "explanation": "Basit febril konvülziyonda en etkin yaklaşım ailenin bilgilendirilmesi, nöbet anında güvenli yan pozisyon (ağıza cisim sokmama, >5 dk sürerse 112 arama) eğitimi ve semptomatik ateş yönetimidir.",
                        "new_finding": "Aileye detaylı nöbet ilk yardım eğitimi verildi ve yazılı bilgilendirme formu ile hasta Sarı Alandan güvenle taburcu edildi.",
                    },
                    {
                        "text": "Her ateşli enfeksiyon başladığında kırk sekiz saat boyunca sekiz saatte bir düzenli oral diazepam verilmesini ve dönüşümlü antipiretik kullanılmasını reçete etmek",
                        "is_correct": False,
                        "scenario_update": "Aralıklı oral diazepam kullanımı çocukta belirgin ataksi ve uykuya meyil yaparak olası bir santral sinir sistemi enfeksiyonunun klinik takibini maskeledi.",
                        "teaching_point": "Ateşli dönemlerde rutin aralıklı oral diazepam profilaksisi sedasyon ve ataksi yaparak menenjit bulgularını maskeleyebileceğinden ilk basit febril konvülziyonda rutin önerilmez; antipiretikler de nöbet tekrarını önlemez.",
                    },
                    {
                        "text": "İlk yirmi dört saatlik dönemde nöbetin tekrarlama olasılığına karşı damar yolunu açık tutarak hastayı çocuk nöroloji servisine yatırıp monitörize izlemek",
                        "is_correct": False,
                        "scenario_update": "Bilinci tamamen normal olan ve ek risk faktörü taşımayan çocukta servis yatışı gereksiz hastane stresine yol açtı.",
                        "teaching_point": "Acil gözlemde (Sarı Alan) birkaç saat izlenen, bilinci tam açık, nörolojik muayenesi doğal ve ateş odağı belli olan basit febril konvülziyon hastalarında hastane yatışı gerekmez.",
                    },
                ],
            },
        ],
    },
    {
        "id": "S03",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "16 Aylık",
        "gender": "Kız",
        "complaint": "Ateşle birlikte 18 dakikadır devam eden, özellikle sağ kol ve bacakta belirgin ritmik kasılma",
        "history": (
            "112 ambulansı ile Sarı Alana kasılmaları devam ederken getiriliyor: 'Evde 18 dakika önce ateşi 39.6°C iken "
            "gözleri sağa kaydı ve özellikle sağ kolu ile sağ bacağında ritmik atmalar başladı. Yolda da hiç durmadı, "
            "bilinci kapalı!' Özgeçmişinde bilinen bir hastalık veya travma öyküsü yok."
        ),
        "final_diagnosis": "Komplike Febril Konvülziyon (Febril Status Epileptikus)",
        "disposition": "Sarı Alanda Akut Antikonvülzan Müdahale, Santral Sinir Sistemi Enfeksiyonu Dışlanması ve Çocuk Servisi Yatışı",
        "case_pearl": (
            "5 dakikayı aşan her nöbet uzamış nöbet / erken status epileptikus kabul edilerek acil benzodiazepin "
            "(İV lorazepam/diazepam veya damar yolu yoksa İM/bukkal/nazal midazolam) ile durdurulmalıdır. "
            "Fokal olan ve 15 dakikadan uzun süren ateşli nöbet Komplike Febril Konvülziyondur; santral sinir sistemi "
            "enfeksiyonu (bakteriyel menenjit / HSV ensefaliti) dışlanmalı ve hasta yatırılarak izlenmelidir."
        ),
        "steps": [
            {
                "stage_title": "Aktif Kasılmaya İlk Beş Dakika Müdahalesi",
                "question": "On sekiz dakikadır sağ yan ağırlıklı kasılması devam eden bu 16 aylık çocukta ilk yapmanız gereken acil müdahale nedir?",
                "options": [
                    {
                        "text": "Hava yolu açıklığını sağlayıp oksijen vermek, kapiller kan şekeri bakmak ve damar yolu açarak intravenöz midazolam veya diazepam uygulamak",
                        "is_correct": True,
                        "explanation": "5 dakikayı aşan aktif nöbette ilk basamak hava yolu ve oksijenizasyonun sağlanması, hipogliseminin hızla dışlanması ve birinci basamak hızlı etkili benzodiazepin uygulanmasıdır.",
                        "new_finding": (
                            "Vital Bulgular: Ateş 39.5°C, KTA 170/dk, rezervuarlı maske oksijen ile SpO2 %97, kapiller kan şekeri 112 mg/dL. "
                            "İV 0.2 mg/kg midazolam uygulandıktan 2 dakika sonra sağ yanlı kasılmalar durdu. "
                            "Postiktal dönemde çocuk uykuya meyilli ve sağ üst ekstremitesini sola kıyasla daha az hareket ettiriyor."
                        ),
                    },
                    {
                        "text": "Benzodiazepinlerin olası solunum depresyonu riskinden kaçınmak amacıyla ilk basamakta doğrudan intravenöz levetirasetam veya fenitoin infüzyonu başlatıp yirmi dakika beklemek",
                        "is_correct": False,
                        "scenario_update": "İnfüzyon süresince aktif kasılma devam etti; nöbet süresi otuz dakikayı aşarak hipoksi ve metabolik asidoz derinleşti.",
                        "teaching_point": "İkinci basamak antiepileptikler (fenitoin, levetirasetam, valproat) infüzyon süresi gerektirdiğinden aktif nöbeti hızlıca sonlandıramaz; ilk basamakta mutlaka hızlı etkili benzodiazepin verilmelidir.",
                    },
                    {
                        "text": "Yüksek ateşi hızla düşürerek kasılmayı sonlandırmak amacıyla intravenöz parasetamol infüzyonu ve ılık uygulama başlatıp on dakika klinik yanıt beklemek",
                        "is_correct": False,
                        "scenario_update": "Antipiretik infüzyonuna rağmen sağ yanlı klonik atmalar kesilmedi, hastada siyanoz ve orofaringeal sekresyon birikimi gelişti.",
                        "teaching_point": "Antipiretik ilaçlar devam eden aktif konvülziyonu durduramaz; 5 dakikayı geçen her nöbette zaman kaybetmeden antikonvülzan müdahale yapılmalıdır.",
                    },
                    {
                        "text": "Sağ yanlı fokal kasılma nedeniyle intrakraniyal patolojiyi dışlamak amacıyla antikonvülzan vermeden önce çocuğu acil kraniyal bilgisayarlı tomografi çekimine göndermek",
                        "is_correct": False,
                        "scenario_update": "Aktif kasılması sürerken radyoloji ünitesine nakledilen çocukta tomografi masasında desatürasyon ve aspirasyon gelişti.",
                        "teaching_point": "Aktif nöbet geçiren hasta hava yolu güvenliği sağlanmadan ve nöbeti antikonvülzan ilaçla durdurulmadan kesinlikle görüntüleme ünitesine gönderilmez.",
                    },
                ],
            },
            {
                "stage_title": "Postiktal Değerlendirme ve Tetkik Planı",
                "question": "Sağ yan ağırlıklı 18 dakika süren kasılması durdurulan ve sağ kolunda geçici güçsüzlük izlenen 16 aylık bu ateşli çocukta bir sonraki yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Kasılma durduğu ve vital bulgular stabilize olduğu için ek laboratuvar tetkiki veya görüntüleme yapmadan antipiretik reçete ederek iki saat sonra taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Taburculuktan dört saat sonra çocuk evde tekrar sağ yanlı durdurulamayan kasılma ve bilinç kaybı ile yoğun bakıma kabul edildi.",
                        "teaching_point": "15 dakikayı aşan ve fokal özellik gösteren ateşli nöbetlerde altta yatan santral sinir sistemi enfeksiyonu veya yapısal patoloji mutlaka araştırılmalı, hasta erken taburcu edilmemelidir.",
                    },
                    {
                        "text": "Postiktal fokal nörolojik bulguya rağmen kraniyal görüntüleme yapmadan hemen yatak başında lomber ponksiyon uygulamak ve ampirik oral antibiyotik tedavisi başlamak",
                        "is_correct": False,
                        "scenario_update": "Fokal defisiti olan hastada görüntüleme öncesi yapılan lomber ponksiyon herniasyon riski taşıdığı gibi, olası santral sinir sistemi enfeksiyonunda oral antibiyotik yetersiz kaldı.",
                        "teaching_point": "Postiktal fokal nörolojik defisiti ve uzamış fokal nöbeti olan hastada lomber ponksiyon öncesinde yer kaplayıcı lezyon veya ödemi dışlamak için acil kraniyal görüntüleme yapılmalıdır.",
                    },
                    {
                        "text": "Elektrolit, kan gazı, hemogram, CRP ve kan kültürü alıp fokal bulgu nedeniyle acil kraniyal görüntüleme yapmak ve santral enfeksiyonu araştırmak",
                        "is_correct": True,
                        "explanation": "Uzamış ve fokal karakterli ateşli nöbet sonrası sağ kolda güçsüzlük varlığında metabolik nedenler, akut bakteriyel menenjit, herpes ensefaliti ve intrakraniyal patolojiler titizlikle araştırılmalıdır.",
                        "new_finding": (
                            "Laboratuvar: Na 137 mEq/L, K 4.2 mEq/L, Ca 9.6 mg/dL, Mg 2.1 mg/dL, WBC 14.200/mm³, CRP 22 mg/L. "
                            "Acil kraniyal görüntülemede kitle, kanama veya şift saptanmadı. İzlemin 2. saatinde sağ koldaki güçsüzlük "
                            "tamamen düzeldi ve bilinci açıldı; lomber ponksiyon değerlendirmesi yapıldı."
                        ),
                    },
                    {
                        "text": "Sağ koldaki hareket azlığını nöbet sırasındaki omuz çıkığı veya kırığa bağlayarak iki yönlü sağ üst ekstremite grafisi ve ortopedi görüşü istemek",
                        "is_correct": False,
                        "scenario_update": "Çekilen omuz ve kol grafileri tamamen normal saptandı; sağ koldaki güçsüzlük iki saat içinde kendiliğinden geriledi ancak asıl nörolojik tetkikler gecikti.",
                        "teaching_point": "Fokal motor nöbet sonrasında aynı taraf ekstremitede gelişen ve saatler içinde düzelen geçici tek taraflı güçsüzlük postiktal parezidir (Todd paralizisi); travma olmadan ortopedik patoloji düşünülmez.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik özellikleri (sağ yanlı fokal kasılma, 18 dakika süre ve geçici postiktal parezi) dikkate alındığında bu hastada tanınız nedir?",
                "options": [
                    {
                        "text": "Basit Febril Konvülziyon",
                        "is_correct": False,
                        "scenario_update": "Nöbetin 18 dakika sürmesi ve sağ hemikorpusta fokal karakter göstermesi basit febril konvülziyon kriterlerini dışlar.",
                        "teaching_point": "Basit febril konvülziyon jeneralize karakterdedir, 15 dakikadan kısa sürer ve fokal nörolojik bulgu bırakmaz.",
                    },
                    {
                        "text": "Komplike Febril Konvülziyon (Febril Status Epileptikus)",
                        "is_correct": True,
                        "explanation": "Ateşli nöbetin hem fokal özellik taşıması (sağ yanlı kasılma ve postiktal Todd parezisi) hem de 15 dakikadan uzun sürmesi Komplike Febril Konvülziyon ve Febril Status Epileptikus tanısını koydurur.",
                        "new_finding": "Klinik tanı: Komplike Febril Konvülziyon (Febril Status Epileptikus).",
                    },
                    {
                        "text": "Siyanotik Katılma (Soluk Tutma) Nöbeti",
                        "is_correct": False,
                        "scenario_update": "Katılma nöbeti ağlama veya korku sonrası gelişir ve 1 dakikadan kısa sürer; 18 dakikalık ateşli fokal klonik kasılma ile açıklanamaz.",
                        "teaching_point": "Katılma nöbetleri afebril dönemde ağlama krizini takiben ortaya çıkan kısa süreli refleks anoksik senkop ataklarıdır.",
                    },
                    {
                        "text": "Akut İskemik Arteriyel İnme",
                        "is_correct": False,
                        "scenario_update": "Kraniyal görüntüleme normaldir ve sağ koldaki güçsüzlük 2 saat içinde sekelsiz olarak tamamen düzelmiştir.",
                        "teaching_point": "Fokal nöbet sonrası gelişen ve birkaç saat içinde tam düzelen hemiparezi kalıcı vasküler inme değil, geçici postiktal Todd paralizisidir.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alan Sonuç ve İkinci Basamak Yönetim Planı",
                "question": "Nöbeti kontrol altına alınan, sağ koldaki güçsüzlüğü düzelen ancak ilk kez uzamış fokal ateşli nöbet geçiren bu 16 aylık hastada nihai izlem ve tedavi planınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Postiktal güçsüzlüğü düzeldiği ve bilinci açıldığı için uzun süreli oral karbamazepin başlayarak hastayı acil servisten doğrudan evine taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Yatış yapılmadan taburcu edilen hastada gece tekrar ateş yükselmesiyle uzamış nöbet gelişti; ayrıca karbamazepin febril nöbetlerde etkisiz ve uygunsuz bir seçimdi.",
                        "teaching_point": "İlk kez febril status epileptikus ve fokal nöbet geçiren süt çocuğu acilden taburcu edilmez; ayrıca karbamazepin febril konvülziyon profilaksisinde kullanılmaz.",
                    },
                    {
                        "text": "Hastayı servise yatırıp santral sinir sistemi enfeksiyonu dışlansa bile tüm komplike febril nöbetlerde ömür boyu ikili antiepileptik tedavi başlamak",
                        "is_correct": False,
                        "scenario_update": "Gereksiz yere başlanan çoklu kronik antiepileptik tedavi süt çocuğunda ağır sedasyon ve gelişimsel yan etkilere yol açtı.",
                        "teaching_point": "Komplike febril konvülziyonda bile altta yatan yapısal veya metabolik anomali yoksa hemen çoklu ömür boyu antiepileptik başlanmaz; EEG ve çocuk nörolojisi izlemiyle bireyselleştirilmiş karar verilir.",
                    },
                    {
                        "text": "Nöbet tekrarlamasın diye çocuğu entübe edip tiyopental infüzyonu altında kırk sekiz saat boyunca çocuk yoğun bakım ünitesinde uyutmak",
                        "is_correct": False,
                        "scenario_update": "Nöbeti durmuş ve bilinci açılmış çocuğa uygulanan gereksiz entübasyon ve barbitürat koması mekanik ventilasyon komplikasyonlarına ve hipotansiyona neden oldu.",
                        "teaching_point": "Genel anestezik infüzyonu ve entübasyon yalnızca birinci ve ikinci basamak antiepileptiklere yanıt vermeyen refrakter status epileptikus tablosunda endikedir.",
                    },
                    {
                        "text": "Hastayı yakın nörolojik izlem, santral sinir sistemi enfeksiyonu ekartasyonu, elektroensefalografi ve çocuk nörolojisi değerlendirmesi için çocuk servisine yatırmak",
                        "is_correct": True,
                        "explanation": "İlk kez geçirilen komplike febril konvülziyon ve febril status epileptikus olguları yakın nörolojik gözlem, etiyolojik inceleme (LP/HSV/EEG) ve nöroloji konsültasyonu amacıyla servise yatırılmalıdır.",
                        "new_finding": "Hasta Çocuk Sağlığı ve Hastalıkları servisine yatırıldı; santral sinir sistemi enfeksiyonu dışlandı, aileye acil kurtarıcı bukkal midazolam eğitimi verilerek çocuk nörolojisi poliklinik takibine alındı.",
                    },
                ],
            },
        ],
    },
    {
        "id": "S04",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "8 Yaş",
        "gender": "Erkek",
        "complaint": "Nefes darlığı, hışıltı, öksürük ve cümleleri tamamlayamama",
        "history": (
            "Sarı Alana tekerlekli sandalye ile hafif öne eğilmiş oturur pozisyonda getiriliyor. "
            "Çocuk kesik kesik kelimelerle 'Nefesim... yetmiyor...' diyebiliyor. Annesi anlatıyor: "
            "'Daha önce de kış aylarında tekrarlayan hışıltı atakları olmuştu ve evde inhaler kullanıyordu, "
            "2 gündür nezleydi. Bu sabah nefes darlığı başladı, evde 2 puf mavi fısfısını (salbutamol) sıktık "
            "ama hiç açılmadı, göğsünden ıslık sesi geliyor.'"
        ),
        "final_diagnosis": "Orta-Ağır Akut Astım Atağı (Viral ÜSYE Tetikli)",
        "disposition": "Sarı Alanda Oksijen + Ardışık Nebülize Salbutamol/İpratropium + Erken Sistemik Steroid Sonrası Yanıt Değerlendirmesi ve Taburculuk",
        "case_pearl": (
            "Kelime veya kısa cümle konuşabilme, yardımcı solunum kası kullanımı, yaygın wheezing ve oda havasında "
            "SpO2 <%92 olması orta-ağır akut astım atağını gösterir. İlk 1 saatte: Oksijen (hedef SpO2 %94-98), "
            "20 dakikada bir 3 doz nebülize salbutamol + ipratropium bromür ve ERKEN (ilk 1 saat içinde) sistemik "
            "kortikosteroid (oral prednizolon veya İV metilprednizolon) verilmelidir."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda Solunum Sıkıntısı Şiddetinin Değerlendirilmesi",
                "question": "Akut nefes darlığı ve hışıltı ile başvuran bu 8 yaşındaki çocukta ilk değerlendirmede neleri kontrol etmelisiniz?",
                "options": [
                    {
                        "text": "Bronkodilatatör ve oksijen tedavisi vermeden önce hava yolu obstrüksiyonunun derecesini objektif ölçmek amacıyla çocuğu solunum fonksiyon testi laboratuvarına göndermek",
                        "is_correct": False,
                        "scenario_update": "Kelimelerle konuşabilen ve hipoksemisi olan çocuk zorlu ekspirasyon manevrasını yapamadı; işlem sırasında dispnesi ve siyanozu derinleşti.",
                        "teaching_point": "Akut belirgin solunum sıkıntısı ve hipoksemisi olan çocukta spirometri çektirmek için acil oksijen ve bronkodilatatör tedavi geciktirilmez.",
                    },
                    {
                        "text": "Konuşma şeklini, bilinç durumunu, solunum sayısını, yardımcı solunum kası çekilmelerini, akciğer oskültasyonunu ve oda havasında oksijen satürasyonunu değerlendirmek",
                        "is_correct": True,
                        "explanation": "Akut bronkospazm ve hışıltı ile gelen çocukta konuşma kapasitesi, bilinç, çekilmeler, oskültasyonda hava girişi ve SpO2 düzeyi atağın şiddetini ve ilk saat tedavisini doğrudan belirler.",
                        "new_finding": (
                            "Vital Bulgular: Ateş 37.1°C, KTA 136/dk, SS 36/dk, oda havasında SpO2 %90. "
                            "Çocuk 2-3 kelimelik kesik ifadelerle konuşabiliyor, suprasternal ve interkostal çekilmeleri belirgin. "
                            "Oskültasyonda ekspiryum uzamış ve her iki hemitoraksta yaygın inspiratuar-ekspiratuar sibilan ronküsler (wheezing) duyuluyor."
                        ),
                    },
                    {
                        "text": "Fizik muayeneyi kolaylaştırmak amacıyla çocuğu sedyeye tam düz sırtüstü yatırıp radyal arterden kan gazı almak ve grafi sonucunu beklemek",
                        "is_correct": False,
                        "scenario_update": "Supin pozisyona zorla yatırılan çocukta diyafram hareketi kısıtlandığı ve ağrılı arteriyel girişim yapıldığı için ajitasyon arttı, SpO2 %86 düzeyine düştü.",
                        "teaching_point": "Solunum sıkıntısı olan çocuk en rahat ettiği oturur/yarı oturur pozisyonda tutulmalı ve ilk değerlendirmede rutin arteriyel kan gazı veya grafi için tedavi geciktirilmemelidir.",
                    },
                    {
                        "text": "Evde iki puf salbutamol aldığı için inhale beta agonistleri etkisiz kabul edip ilk basamakta doğrudan intravenöz aminofilin yüklemesi planlamak",
                        "is_correct": False,
                        "scenario_update": "Oksijen ve uygun doz nebülize bronkodilatatör verilmeden başlanan intravenöz aminofilin çocukta şiddetli bulantı, kusma ve sinüs taşikardisine yol açtı.",
                        "teaching_point": "Evde aracı tüp (spacer) olmadan sıkılan 2 puf inhaler yetersizdir; acil serviste ilk basamak her zaman oksijen, yüksek doz nebülize/spacer salbutamol, ipratropium ve sistemik steroiddir.",
                    },
                ],
            },
            {
                "stage_title": "İlk Bir Saat Akut Tedavi Protokolü",
                "question": "Oda havasında SpO2 %90 olan, kelimelerle konuşabilen ve yaygın sibilan ronküsleri duyulan bu 8 yaşındaki çocukta ilk 1 saatteki en doğru tedavi protokolü hangisidir?",
                "options": [
                    {
                        "text": "Maske ile oksijen başlayıp yalnızca tek doz nebülize salbutamol uygulamak, sistemik kortikosteroid tedavisini ise dördüncü saatin sonundaki klinik yanıta göre ertelemek",
                        "is_correct": False,
                        "scenario_update": "Tek doz salbutamol sonrası otuzuncu dakikada bronkospazm tekrar arttı; erken sistemik steroid verilmediği için hava yolu ödemi gerilemedi ve SpO2 %89 düzeyinde kaldı.",
                        "teaching_point": "Belirgin dispne ve hipoksemisi olan akut bronkospazm atağında sistemik kortikosteroidlerin etkisi 3-4 saatte başladığından ilk 1 saat içinde erken verilmesi şarttır; ayrıca ilk saatte 20 dakikada bir 3 doz SABA + ipratropium uygulanmalıdır.",
                    },
                    {
                        "text": "Tek başına yüksek doz nebülize budesonid ve soğuk buhar uygulayıp kalp hızını artırmaması amacıyla kısa etkili beta-2 agonist ilaçlardan kaçınmak",
                        "is_correct": False,
                        "scenario_update": "Soğuk buhar hiperreaktif hava yollarında bronkospazmı daha da tetikledi; hızlı etkili bronkodilatatör verilmediği için solunum sıkıntısı ağırlaştı.",
                        "teaching_point": "Akut bronkospazm atağında kurtarıcı temel ilaç kısa etkili beta-2 agonisttir (salbutamol); soğuk buhar bronkospazmı artırır ve tek başına inhale steroid akut atağı çözmez.",
                    },
                    {
                        "text": "Nebülize salbutamol ile birlikte çocuğun hızlı solunumunu ve anksiyetesini azaltmak amacıyla düşük doz intravenöz midazolam uygulayarak hafif sedasyon sağlamak",
                        "is_correct": False,
                        "scenario_update": "Verilen sedatif ilaç çocuğun yardımcı solunum kaslarını ve solunum dürtüsünü baskılayarak akut karbondioksit retansiyonuna ve letarjiye yol açtı.",
                        "teaching_point": "Akut obstrüktif solunum sıkıntısı atağında sedatif ve anksiyolitik ilaçlar solunum depresyonu ve solunum arresti riski nedeniyle kesinlikle kontrendikedir.",
                    },
                    {
                        "text": "Oksijen (hedef SpO2 %94-98), yirmi dakika arayla üç doz nebülize salbutamol ve ipratropium bromür ile erken sistemik kortikosteroid başlamak",
                        "is_correct": True,
                        "explanation": "Güncel uluslararası rehberlere göre hipoksemik orta-ağır bronkospazm atağında ilk 1 saatte hedefe yönelik oksijen, 20 dakika arayla 3 doz nebülize SABA + ipratropium bromür kombinasyonu ve erken sistemik steroid (1-2 mg/kg prednizolon/metilprednizolon) standart tedavidir.",
                        "new_finding": (
                            "1. saat sonunda (3 doz nebülize salbutamol + ipratropium bromür ve 1.5 mg/kg sistemik metilprednizolon sonrası): "
                            "Solunum sayısı 24/dk düzeyine geriledi, suprasternal çekilme kayboldu, çocuk tam cümlelerle rahat konuşmaya başladı "
                            "ve oda havasında SpO2 %96 ölçüldü."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Öyküsü, fizik muayene bulguları ve bronkodilatatör tedaviye verdiği hızlı yanıt doğrultusunda bu hastada kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Akut Yabancı Cisim Aspirasyonu",
                        "is_correct": False,
                        "scenario_update": "Ani boğulma öyküsü yoktur, oskültasyon bulguları iki taraflı simetriktir ve bronkodilatatör tedavi ile tablo tamamen düzelmiştir.",
                        "teaching_point": "Yabancı cisim aspirasyonunda genellikle ani başlayan öksürük/boğulma öyküsü ve tek taraflı havalanma azlığı görülür; bronkodilatatöre tam yanıt beklenmez.",
                    },
                    {
                        "text": "Spontan Akut Tansiyon Pnömotoraks",
                        "is_correct": False,
                        "scenario_update": "Her iki hemitoraksta solunum sesleri duyulmaktadır, trakea orta hattadır ve hipotansiyon yoktur.",
                        "teaching_point": "Tansiyon pnömotoraksta tek taraflı solunum sesi kaybı, hipersonorite, trakea deviasyonu ve obstrüktif şok bulguları saptanır.",
                    },
                    {
                        "text": "Orta-Ağır Akut Astım Atağı",
                        "is_correct": True,
                        "explanation": "Tekrarlayan hışıltı öyküsü, viral üst solunum yolu enfeksiyonu sonrası gelişen dispne, kesik kelimelerle konuşma, yardımcı kas kullanımı, yaygın wheezing, SpO2 %90 olması ve SABA+ipratropium+steroid tedavisine dramatik yanıt Orta-Ağır Akut Astım Atağını doğrular.",
                        "new_finding": "Klinik tanı: Orta-Ağır Akut Astım Atağı.",
                    },
                    {
                        "text": "Psikojenik Hiperventilasyon Sendromu",
                        "is_correct": False,
                        "scenario_update": "Hastanın oda havasında oksijen satürasyonu %90 olup oskültasyonda yaygın sibilan ronküsler ve suprasternal çekilmeler mevcuttu.",
                        "teaching_point": "Psikojenik hiperventilasyonda SpO2 normaldir (%99-100), yardımcı solunum kası çekilmesi ve yaygın wheezing bulunmaz.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alan İzlem ve Taburculuk Planı",
                "question": "Sarı Alanda 4 saat izlenen, son 2 saattir bronkodilatatör ihtiyacı olmadan oda havasında SpO2 değeri %97 olan, çekilmesi kalmayan ve rahat konuşup yürüyebilen bu hastada taburculuk planınız ne olmalıdır?",
                "options": [
                    {
                        "text": "3-5 günlük oral steroid kürünü tamamlamak, aracı tüp tekniğini göstererek salbutamol ve inhale kortikosteroid düzenleyip eylem planıyla taburcu etmek",
                        "is_correct": True,
                        "explanation": "Tedaviye tam yanıt veren ve oda havasında SpO2 >%94 stabil kalan hastada erken relapsı önlemek için 3-5 günlük oral steroid kürü, doğru aracı tüp (spacer) tekniğiyle kurtarıcı+koruyucu inhaler tedavi, yazılı astım eylem planı ve 48 saat içinde kontrol önerilir.",
                        "new_finding": "Aracı tüp (spacer) olmadan doğrudan ağza sıkma hatası düzeltildi; 4 günlük oral steroid, düzenli inhale kortikosteroid ve yazılı astım eylem planı ile hasta taburcu edildi.",
                    },
                    {
                        "text": "Acilde tek doz steroid yapıldığı için evde ek oral steroid vermeden yalnızca gerektiğinde kullanmak üzere salbutamol reçete ederek taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Sistemik steroid kürü devam ettirilmeyen ve kontrol edici inhale steroid başlanmayan çocukta geç faz inflamasyon nedeniyle aynı gece ağır atak tekrarladı.",
                        "teaching_point": "Orta-ağır astım atağı sonrasında hava yolu inflamasyonunun baskılanması ve erken relapsın önlenmesi için 3-5 günlük oral sistemik steroid kürü tamamlanmalı ve düzenli İKS başlanmalıdır.",
                    },
                    {
                        "text": "Balgamı yumuşatmak ve gece öksürüğünü kesmek amacıyla oral mukolitik şurup, birinci kuşak antihistaminik ve antitüssif reçete ederek inhalerleri kesmek",
                        "is_correct": False,
                        "scenario_update": "İnhaler tedavisi kesilen ve antitüssif verilen çocukta mukus tıkaçları ve şiddetli bronkospazm gelişerek ertesi gün acil servise yeniden başvuru oldu.",
                        "teaching_point": "Astım atağı taburculuğunda antitüssif, mukolitik ve sedatif antihistaminiklerin yeri yoktur; temel tedavi inhaler bronkodilatatör, inhale/oral kortikosteroid ve doğru cihaz eğitimidir.",
                    },
                    {
                        "text": "Viral üst solunum yolu enfeksiyonu tetiklediği için on günlük oral amoksisilin-klavulanat başlamak ve aracı tüp olmadan doğrudan inhaler kullandırmak",
                        "is_correct": False,
                        "scenario_update": "Gereksiz antibiyotik ishal yaparken, aracı tüp (spacer) kullanılmadığı için inhaler ilacın büyük kısmı orofarenkste kalarak akciğerlere ulaşmadı.",
                        "teaching_point": "Viral tetikli astım ataklarında rutin antibiyotik endikasyonu yoktur; ayrıca 8 yaşındaki çocukta ölçülü doz inhaler (MDI) mutlaka aracı tüp (spacer) ile kullanılmalıdır.",
                    },
                ],
            },
        ],
    },
    {
        "id": "S05",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "3 Yaş (15 kg)",
        "gender": "Kız",
        "complaint": "Evde parasetamol şurup şişesini içme",
        "history": (
            "Annesi elinde boş bir parasetamol süspansiyon (120 mg/5 mL, 150 mL şişe) ile Sarı Alana koşarak geliyor: "
            "'Hocam, şişede yaklaşık 100-110 mL şurup vardı, tadı çilekli olduğu için 45 dakika önce mutfakta hepsini "
            "kafasına dikip içmiş! Ağzının kenarı hep pembe şuruptu. Şu an neşesi yerinde, sadece 1 kez hafif öğürdü, hiç kusmadı.'"
        ),
        "final_diagnosis": "Akut Toksik Dozda Parasetamol (Asetaminofen) Zehirlenmesi",
        "disposition": "Sarı Alanda Aktif Kömür, 4. Saat Serum Parasetamol Düzeyi (Rumack-Matthew) Değerlendirmesi ve İV N-Asetilsistein (NAC) İnfüzyonu ile Servis Yatışı",
        "case_pearl": (
            "Çocuklarda tek seferde ≥150-200 mg/kg parasetamol alımı akut hepatotoksik dozdur (100 mL x 24 mg/mL = 2400 mg -> "
            "15 kg çocukta 160 mg/kg). Parasetamol zehirlenmesinin ilk 24 saatinde (Evre 1) hasta tamamen asemptomatik olabilir. "
            "İlk 1-2 saat içinde başvuruda 1 g/kg aktif kömür verilir; serum parasetamol düzeyi alımdan sonraki 4. saatte bakılarak "
            "Rumack-Matthew nomogramında değerlendirilir ve tedavi eşiği üzerindeyse ilk 8 saat içinde N-Asetilsistein (NAC) başlanır."
        ),
        "steps": [
            {
                "stage_title": "Alınan Dozun Hesaplanması ve İlk Saat Dekontaminasyon",
                "question": "Alımdan 45 dakika sonra başvuran, 15 kg ağırlığında ve yaklaşık 100-110 mL (120 mg/5 mL) parasetamol süspansiyon içtiği belirtilen bilinci açık bu çocukta ilk adımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Çocuğun genel durumu iyi, vital bulguları stabil ve aktif yakınması olmadığı için alınan miktarı zararsız kabul ederek doğrudan eve taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Taburcu edilen çocukta ilk gün yakınma olmazken 36. saatten itibaren sağ üst kadran ağrısı, sarılık, koagülopati ve akut karaciğer yetmezliği gelişti.",
                        "teaching_point": "Akut yüksek doz parasetamol alımının ilk 24 saatinde (Evre 1) hastalar çoğunlukla asemptomatiktir; klinik görünüme aldanılarak doz hesaplanmadan taburculuk yapılması ölümcül karaciğer hasarına yol açar.",
                    },
                    {
                        "text": "Midedeki şurubu hızla dışarı çıkarmak amacıyla çocuğa tuzlu su içirerek veya arka farenksi mekanik uyararak yatak başında kusturmaya çalışmak",
                        "is_correct": False,
                        "scenario_update": "Zorla kusturma girişimi sırasında çocukta aspirasyon tehlikesi gelişti ve inatçı öğürme başladığı için oral aktif kömür uygulanamadı.",
                        "teaching_point": "Zehirlenmelerde mekanik uyarım, tuzlu su veya ipeka şurubu ile kusturma işlemi aspirasyon riski ve etkinliğinin olmaması nedeniyle kesinlikle kontrendikedir.",
                    },
                    {
                        "text": "Alınan dozun 160-176 mg/kg olduğunu hesaplamak, vital bulguları alıp ilk saat içinde olduğundan 1 g/kg oral aktif kömür vermek",
                        "is_correct": True,
                        "explanation": "100-110 mL (24 mg/mL) şurup toplam 2400-2640 mg, yani 15 kg çocukta 160-176 mg/kg doza karşılık gelir; ≥150 mg/kg alımlarda ilk 1-2 saat içinde bilinci açık hastaya 1 g/kg oral aktif kömür verilmesi gastrointestinal emilimi anlamlı ölçüde azaltır.",
                        "new_finding": (
                            "Vital Bulgular: Ateş 36.7°C, KTA 108/dk, SS 22/dk, TA 95/60 mmHg, SpO2 %99, GKS 15. "
                            "Hesaplanan alım dozu 160-176 mg/kg. Alımın 45. dakikasında 15 gram (1 g/kg) oral aktif kömür "
                            "uygulandı ve çocuk kusmadan tolere etti."
                        ),
                    },
                    {
                        "text": "Sıvı süspansiyon formlarında aktif kömürün bağlama etkisi olmadığı gerekçesiyle kalın orogastrik tüp yerleştirerek yüksek hacimli gastrik lavaj işlemi uygulamak",
                        "is_correct": False,
                        "scenario_update": "Bilinci açık 3 yaşındaki çocukta zorla yapılan kalın tüplü gastrik lavaj özofagus mukozasında travmaya, laringospazma ve hipoksiye neden oldu.",
                        "teaching_point": "Parasetamol aktif kömüre çok iyi bağlanır; hızlı emilen sıvı süspansiyon alımlarında rutin gastrik lavaj yerine ilk 1-2 saat içinde oral aktif kömür uygulaması tercih edilir.",
                    },
                ],
            },
            {
                "stage_title": "Laboratuvar İzlemi ve Kan Düzeyi Zamanlaması",
                "question": "Aktif kömür uygulanan ve şu an alımın 1. saatinde olan bu çocukta biyokimyasal izlem ve plazma ilaç düzeyi ölçümü için en doğru zamanlama nedir?",
                "options": [
                    {
                        "text": "Alımın birinci saatinde hemen plazma parasetamol düzeyi ve karaciğer enzimlerini gönderip sonuçlar düşük çıkarsa çocuğu dördüncü saati beklemeden taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Birinci saatte bakılan plazma ilaç düzeyi 65 mcg/mL ve AST/ALT normal geldi; ancak gastrointestinal emilim devam ettiği için dördüncü saatte kan düzeyi 185 mcg/mL değerine yükseldi.",
                        "teaching_point": "Akut tek doz alımlarda gastrointestinal emilim ve doku dağılımı 4. saate kadar tamamlanmaz; 4. saatten önce bakılan kan ilaç düzeyi ve erken AST/ALT değerleri toksisiteyi dışlamak için kullanılamaz.",
                    },
                    {
                        "text": "Bazal karaciğer-böbrek fonksiyonları, INR ve glukoz bakmak; anlamlı plazma parasetamol konsantrasyonu için alımdan sonraki dördüncü saatte kan örneği almak",
                        "is_correct": True,
                        "explanation": "Akut tek seferlik yüksek doz parasetamol alımında emilim ve dağılım fazı 4. saatte tamamlandığından, tedavi kararını belirleyen plazma ilaç konsantrasyonu alımdan sonraki 4. saatte ölçülmelidir.",
                        "new_finding": (
                            "Bazal (1. saat) laboratuvar: AST 26 U/L, ALT 19 U/L, INR 1.0, üre 22 mg/dL, kreatinin 0.4 mg/dL, glukoz 94 mg/dL. "
                            "Alımdan tam 4 saat sonra alınan plazma parasetamol konsantrasyonu: 185 mcg/mL."
                        ),
                    },
                    {
                        "text": "Plazma ilaç düzeyi bakmak yerine idrarda kalitatif ilaç taraması istemek ve sadece yirmi dördüncü saatte kontrol AST/ALT değerlerini görmek",
                        "is_correct": False,
                        "scenario_update": "İdrar taraması pozitif saptandı ancak kandaki kantitatif konsantrasyon ölçülmediği için dördüncü saatteki yüksek plazma düzeyi fark edilemedi ve spesifik tedavi gecikti.",
                        "teaching_point": "İdrarda kalitatif ilaç taraması terapötik dozlarda bile pozitif çıkar ve toksisite şiddetini göstermez; yönetim kararı mutlaka 4. saat kantitatif plazma parasetamol konsantrasyonu ile verilmelidir.",
                    },
                    {
                        "text": "İlaç yarı ömrünün geçmesini beklemek amacıyla ilk kan örneğini alımdan sonraki on ikinci saatte almak ve o zamana kadar beklemek",
                        "is_correct": False,
                        "scenario_update": "On ikinci saate kadar hiçbir düzey bakılmadan beklenmesi, koruyucu tedavinin en etkili olduğu ilk sekiz saatlik altın pencerenin kaçırılmasına yol açtı.",
                        "teaching_point": "Akut alımlarda plazma ilaç düzeyi 4. saatte bakılmalı ve koruyucu tedavi gerekiyorsa alımdan sonraki ilk 8 saat içinde başlanmalıdır; 12. saati beklemek karaciğer hasarı riskini artırır.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı ve Toksisite Risk Değerlendirmesi",
                "question": "Yaklaşık 160-176 mg/kg alım öyküsü ve 4. saat plazma parasetamol konsantrasyonu 185 mcg/mL olan bu hastada Rumack-Matthew nomogramına göre tanınız ve risk değerlendirmeniz nedir?",
                "options": [
                    {
                        "text": "Toksik Olmayan Terapötik Doz Parasetamol Maruziyeti",
                        "is_correct": False,
                        "scenario_update": "4. saat plazma parasetamol düzeyi 185 mcg/mL olup Rumack-Matthew nomogramındaki 150 mcg/mL tedavi eşiğinin belirgin üzerindedir.",
                        "teaching_point": "Rumack-Matthew nomogramında 4. saatte ≥150 mcg/mL olan plazma parasetamol düzeyleri akut hepatotoksisite riski taşır ve antidot tedavisi gerektirir.",
                    },
                    {
                        "text": "Akut Salisilat İntoksikasyonu ve Solunumsal Alkaloz",
                        "is_correct": False,
                        "scenario_update": "Hastanın içtiği ilaç parasetamol (asetaminofen) süspansiyondur; Done nomogramı veya salisilat toksisitesi söz konusu değildir.",
                        "teaching_point": "Parasetamol ve salisilat farklı analjezik-antipiretik ilaçlardır; parasetamol NAPQI aracılı karaciğer nekrozu yaparken salisilat solunumsal alkaloz ve metabolik asidoz yapar.",
                    },
                    {
                        "text": "Evre 3 Fulminan Hepatik Yetmezlik Tablosu",
                        "is_correct": False,
                        "scenario_update": "Hasta henüz alımın 4. saatindedir (Evre 1), bilinci açıktır ve bazal AST, ALT ve INR değerleri normaldir.",
                        "teaching_point": "Parasetamol zehirlenmesinde Evre 1 (ilk 24 saat) asemptomatik/hafif GİS bulgularıyla seyreder; Evre 3 fulminan karaciğer yetmezliği tedavi edilmeyen vakalarda 72-96. saatlerde gelişir.",
                    },
                    {
                        "text": "Akut Toksik Parasetamol Zehirlenmesi (Yüksek Hepatotoksisite Riski)",
                        "is_correct": True,
                        "explanation": "Rumack-Matthew nomogramında 4. saat plazma parasetamol konsantrasyonunun 150 mcg/mL tedavi çizgisinin üzerinde (185 mcg/mL) olması yüksek hepatotoksisite riskini ve acil antidot endikasyonunu gösterir.",
                        "new_finding": "Klinik tanı: Akut Toksik Dozda Parasetamol Zehirlenmesi (Rumack-Matthew tedavi eşiği üzerinde, antidot endikasyonu mevcut).",
                    },
                ],
            },
            {
                "stage_title": "Spesifik Antidot Protokolü ve Yatış Planı",
                "question": "4. saat plazma parasetamol düzeyi 185 mcg/mL saptanan bu hastada karaciğer nekrozunu (NAPQI toksisitesini) önlemek için uygulanması gereken spesifik antidot ve izlem planı nedir?",
                "options": [
                    {
                        "text": "İlk sekiz saat içinde intravenöz N-Asetilsistein (NAC) infüzyon protokolü başlamak ve günlük AST, ALT, INR takibiyle servise yatırmak",
                        "is_correct": True,
                        "explanation": "Parasetamol zehirlenmesinin spesifik antidotu N-Asetilsisteindir (NAC); glutatyon depolarını yenileyerek toksik metabolit NAPQI-kaynaklı hepatik nekrozu önler ve ilk 8 saat içinde başlandığında koruyuculuğu %100'e yakındır.",
                        "new_finding": "Alımın 5. saatinde İV N-Asetilsistein infüzyon protokolü başlanarak hasta çocuk servisine yatırıldı. İzlemde AST, ALT ve INR değerleri normal seyreden hasta tedavi sonunda sekelsiz taburcu edildi.",
                    },
                    {
                        "text": "Bazal AST, ALT ve INR değerleri tamamen normal olduğu için antidot başlamadan yirmi dört saat sonra poliklinik kontrolü önermek",
                        "is_correct": False,
                        "scenario_update": "Antidot başlanmadan eve gönderilen çocukta 36. saatte AST ve ALT 3500 U/L üzerine çıktı ve akut karaciğer yetmezliği gelişti.",
                        "teaching_point": "N-Asetilsistein tedavisine transaminazlar yükselmeden önce, 4. saat plazma parasetamol düzeyine göre ilk 8 saat içinde başlanmalıdır; AST/ALT yükselmesini beklemek koruyucu pencereyi kaçırtır.",
                    },
                    {
                        "text": "İdrar pH değerini 7.5 üzerine çıkararak parasetamolün böbreklerden atılımını hızlandırmak amacıyla intravenöz sodyum bikarbonat ile idrar alkalinizasyonu protokolü başlatmak",
                        "is_correct": False,
                        "scenario_update": "İdrar alkalinizasyonu parasetamol eliminasyonunu artırmadığı gibi, spesifik antidot verilmediği için toksik metabolit NAPQI birikimi ve karaciğer hasarı gelişti.",
                        "teaching_point": "İdrar alkalinizasyonu salisilat ve fenobarbital zehirlenmesinde kullanılır; parasetamol zehirlenmesinde etkinliği yoktur, spesifik tedavi N-Asetilsisteindir.",
                    },
                    {
                        "text": "Spesifik antidot olarak intravenöz fomepizol veya nalokson puşe uygulayıp altı saatlik Sarı Alan gözlemi sonrasında hastayı evine taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Fomepizol ve nalokson parasetamol metabolizması üzerinde koruyucu etki göstermedi; hastada ikinci günde ciddi hepatotoksisite tablosu ortaya çıktı.",
                        "teaching_point": "Fomepizol metanol/etilen glikol, nalokson ise opioid zehirlenmesinin antidotudur; parasetamol intoksikasyonunda tek spesifik antidot N-Asetilsisteindir (NAC).",
                    },
                ],
            },
        ],
    },
]
