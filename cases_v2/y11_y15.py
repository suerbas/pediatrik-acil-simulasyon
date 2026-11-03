# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - Y11-Y15 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "Y11",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "8 Yaş",
        "gender": "Erkek",
        "complaint": "Göbek çevresinde başlayıp sağ alt kadrana yerleşen karın ağrısı, iştahsızlık, hafif ateş ve yürürken aksama",
        "history": (
            "Ailesi 8 yaşındaki erkek çocuğu Sarı Alana getiriyor: 'Dün akşamüstü göbeğinin etrafında ağrı "
            "başladı, akşam yemeğini hiç yemedi, en sevdiği yiyeceklere bile bakmadı. Gece ağrısı sağ kasığına "
            "doğru kaydı ve sabah hafif ateşi (38.1°C) çıktı. Arabayla gelirken kasisten geçtiğimizde karnını "
            "tutarak bağırdı, yürürken sağ bacağını hafif bükerek aksıyor ve öksürünce sağ alt karnı ağrıyor.'"
        ),
        "final_diagnosis": "Akut Apandisit (Komplike Olmamış Akut Flegmonöz Apandisit)",
        "disposition": "Sarı Alanda İV Sıvı + Analjezi + Preoperatif Antibiyotik + Çocuk Cerrahisi Konsültasyonu ile Acil Operasyona Yatış",
        "case_pearl": (
            "Çocuklarda akut cerrahi batının en sık nedeni akut apandisittir. Periumbilikal başlayıp sağ alt "
            "kadrana (McBurney noktası) göç eden ağrı, anoreksi, sarsıntıyla artan peritoneal irritasyon ve "
            "psoas irritasyonuna bağlı sağ kalça fleksiyonu tipiktir. Uygun analjezi (İV parasetamol veya "
            "düşük doz opioid) peritoneal bulguları maskelemez; aksine istemli savunmayı azaltarak muayene "
            "güvenilirliğini artırır. ALARA prensibi gereği çocuklarda ilk tercih görüntüleme ultrasonografidir "
            "(komprese edilemeyen, dış çapı >6 mm, kör sonlanan aperistaltik tübüler yapı)."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Akut Batın Muayenesi",
                "question": "Sağ alt kadrana yer değiştiren karın ağrısı ve yürürken aksaması olan 8 yaşındaki bu çocukta ilk muayene ve semptomatik yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Vital bulguları ve batın muayenesini tamamladıktan sonra cerrahi konsültasyon öncesinde peritonit bulgularını maskelememek amacıyla hiçbir analjezik vermeden yalnızca damar yolu açıp izotonik sıvı başlamak",
                        "is_correct": False,
                        "scenario_update": "Ağrısı dindirilmeyen çocukta şiddetli ajitasyon ve yaygın istemli karın kasılması devam ettiği için lokalize peritoneal irritasyon bulgularını net değerlendirmek güçleşti.",
                        "teaching_point": "Akut karın ağrılı çocuklarda intravenöz parasetamol veya uygun doz analjezik verilmesi cerrahi muayeneyi bozmaz; aksine anksiyete kaynaklı istemli defansı azaltarak gerçek peritoneal bulguların saptanmasını kolaylaştırır.",
                    },
                    {
                        "text": "Vital bulguları ölçmek, sağ alt kadran defans ve rebound varlığını, psoas bulgusunu ve skrotal muayeneyi değerlendirip ağrı için intravenöz parasetamol uygulamak",
                        "is_correct": True,
                        "explanation": "Akut batın şüphesinde vital bulgular, lokalize peritoneal irritasyon ve psoas bulgusu sistematik değerlendirilmeli; erkek çocuklarda yansıyan skrotal patolojiler mutlaka dışlanmalı ve erken analjezi sağlanmalıdır.",
                        "new_finding": "Vital bulgular: Ateş 38.2°C, KTA 112/dk, SS 22/dk, TA 105/65 mmHg. Sağ alt kadranda belirgin lokalize hassasiyet, istemli defans ve pozitif rebound mevcut. Sağ uyluk ekstansiyonunda ağrı artıyor (pozitif psoas bulgusu). Bilateral skrotum ve testisler doğal, kremaster refleksi intakt. İntravenöz parasetamol sonrası ajitasyon azaldı ancak sağ alt kadran hassasiyeti devam etti.",
                    },
                    {
                        "text": "Batın muayenesinde sağ alt kadran hassasiyetini saptadıktan sonra bağırsak pasajını rahatlatıp gaz sancısını dışlamak amacıyla rektal gliserinli lavman uygulayarak iki saat gözlemlemek",
                        "is_correct": False,
                        "scenario_update": "Rektal lavman uygulaması intraluminal basıncı artırarak çocuğun sağ alt kadran ağrısını ve peritoneal irritasyon bulgularını belirgin şekilde şiddetlendirdi.",
                        "teaching_point": "Lokalize peritoneal irritasyon bulguları, ateş ve anoreksisi olan akut batın şüpheli çocuklarda intraluminal basıncı ve perforasyon riskini artıran lavman veya laksatif uygulamaları kontrendikedir.",
                    },
                    {
                        "text": "Çocuğun yürürken sağ bacağını bükerek aksamasını ve subfebril ateşini ön planda tutarak kalça eklemi muayenesine odaklanıp batın palpasyonunu ortopedi değerlendirmesi sonrasına bırakmak",
                        "is_correct": False,
                        "scenario_update": "Kalça eklem hareketleri pasif rotasyonda açık olmasına rağmen retroçekal/pelvik inflamasyonun psoas kası irritasyonu gözden kaçırıldı ve batın değerlendirmesi gecikti.",
                        "teaching_point": "Retroçekal yerleşimli sağ alt kadran inflamasyonları iliopsoas kasını irrite ederek sağ kalçada antaljik fleksiyon ve yürüme güçlüğü yapabilir; bu tablo primer kalça patolojisi ile karıştırılmamalıdır.",
                    },
                ],
            },
            {
                "stage_title": "Laboratuvar Tetkikleri ve İlk Basamak Görüntüleme Seçimi",
                "question": "Lokalize sağ alt kadran peritoneal irritasyon bulguları ve psoas pozitifliği saptanan bu hastada tanısal tetkik ve görüntüleme planınız nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Oral alımı kesip intravenöz hidrasyon başlayarak hemogram, CRP ve tam idrar tetkiki göndermek; görüntüleme olarak yalnızca ayakta direkt batın grafisi çekip hava-sıvı seviyesi aramak",
                        "is_correct": False,
                        "scenario_update": "Ayakta direkt batın grafisinde sağ alt kadranda nonspesifik birkaç gaz gölgesi dışında tanısal bulgu saptanmadı ve kesin tanı için zaman kaybedildi.",
                        "teaching_point": "Direkt batın grafisinin akut sağ alt kadran patolojilerinde duyarlılığı ve özgüllüğü çok düşüktür; mekanik obstrüksiyon veya serbest hava şüphesi dışında rutin ilk basamak görüntüleme olarak önerilmez.",
                    },
                    {
                        "text": "Ultrasonografinin kullanıcı bağımlı olması ve gaz süperpozisyonu riski nedeniyle zaman kaybetmeden doğrudan intravenöz kontrastlı alt-üst abdomen bilgisayarlı tomografisi çekerek kesin anatomik görüntüleme sağlamak",
                        "is_correct": False,
                        "scenario_update": "BT'de sağ alt kadranda 8.5 mm çaplı inflamatuar tübüler yapı gösterildi ancak 8 yaşındaki çocuk ultrasonografi ile kolayca konulabilecek bir tanı için yüksek doz iyonizan radyasyona maruz kaldı.",
                        "teaching_point": "Pediatrik yaş grubunda ALARA prensibi gereği sağ alt kadran ağrısında ilk basamak görüntüleme her zaman kademeli kompresyon ultrasonografisidir; BT yalnızca ultrasonografinin sonuçsuz kaldığı seçilmiş olgularda düşünülür.",
                    },
                    {
                        "text": "Oral alımı durdurup intravenöz izotonik sıvı başlamak; tam kan sayımı, CRP ve tam idrar tetkiki göndererek ilk basamak görüntüleme olarak batın ultrasonografisi istemek",
                        "is_correct": True,
                        "explanation": "Olası cerrahi girişim hazırlığı için oral alım kapatılıp İV hidrasyon başlanmalı; inflamatuar belirteçler, üriner patolojileri dışlamak için TİT ve radyasyon içermeyen batın ultrasonografisi istenmelidir.",
                        "new_finding": "Laboratuvar: Lökosit 15.800/mm³ (%84 nötrofil), CRP 42 mg/L, tam idrar tetkikinde lökosit ve eritrosit yok, dansite 1022. Ultrasonografi: Sağ alt kadranda komprese edilemeyen, kör sonlanan, aperistaltik, duvar kalınlığı artmış, dış çapı 8.5 mm ölçülen tübüler intestinal yapı, çevresinde hiperekojen mezenterik yağ dokusu ve minimal serbest sıvı izlendi.",
                    },
                    {
                        "text": "Kan ve idrar tetkiklerini gönderdikten sonra radyolojik görüntüleme istemeden önce on iki saatlik seri batın muayenesi ve lökosit takibi ile klinik seyri izlemek",
                        "is_correct": False,
                        "scenario_update": "Lökosit 15.800/mm³ ve CRP 42 mg/L gelmesine rağmen görüntüleme ertelenince takip sürecinde ateş 39.1°C'ye yükseldi ve peritoneal irritasyon tüm alt batına yayıldı.",
                        "teaching_point": "Tipik klinik öykü, lokalize rebound ve yüksek akut faz yanıtı bulunan hastalarda ultrasonografi geciktirilmemeli; seri gözlem yalnızca düşük-orta riskli ve görüntülemesi şüpheli olgularda tercih edilmelidir.",
                    },
                ],
            },
            {
                "stage_title": "Klinik ve Radyolojik Bulgularla Kesin Tanı",
                "question": "Sağ alt kadran peritoneal irritasyon bulguları, nötrofilik lökositoz ve ultrasonografide 8.5 mm çaplı komprese edilemeyen kör uçlu tübüler yapı saptanan hastada kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Akut komplike olmamış flegmonöz apandisit",
                        "is_correct": True,
                        "explanation": "Periumbilikal başlayıp sağ alt kadrana yerleşen ağrı, anoreksi, nötrofilik lökositoz ve ultrasonografide >6 mm komprese edilemeyen kör sonlanan apendiks görünümü akut apandisit tanısını kesinleştirir.",
                        "new_finding": "Kesin tanı: Akut komplike olmamış apandisit. Hastada serbest perforasyon veya apse formasyonu saptanmadı.",
                    },
                    {
                        "text": "Akut mezenterik lenfadenit ve terminal ileit",
                        "is_correct": False,
                        "scenario_update": "Mezenterik lenfadenitte apendiks normal çapta (<6 mm) ve komprese edilebilir görünümde olup mezenterde kümelenmiş reaktif lenf nodları izlenir.",
                        "teaching_point": "Ultrasonografide dış çapı 6 mm'yi aşan, aperistaltik ve basıyla komprese olmayan kör uçlu yapı varlığında tanı mezenterik lenfadenit değil akut apandisittir.",
                    },
                    {
                        "text": "Komplike olmayan akut çekal divertükülit",
                        "is_correct": False,
                        "scenario_update": "Çekal divertükülit pediatrik yaş grubunda son derece nadirdir ve ultrasonografide normal apendiks yanında çekum duvarından kaynaklanan fokal keseleşme olarak görülür.",
                        "teaching_point": "Çocuklarda sağ alt kadranın kör sonlanan tübüler inflamasyonu aksi kanıtlanmadıkça akut apandisittir.",
                    },
                    {
                        "text": "Enfekte Meckel divertikülü (Meckel divertiküliti)",
                        "is_correct": False,
                        "scenario_update": "Meckel divertiküliti klinik olarak benzer tablo yapabilse de ultrasonografide sağ alt kadranda tipik kör sonlanan apendiks inflamasyonu saptanmıştır.",
                        "teaching_point": "Ultrasonografide anatomik olarak sağ iliak fossada komprese olmayan şişmiş apendiksin doğrudan görüntülenmesi akut apandisit tanısını doğrular.",
                    },
                ],
            },
            {
                "stage_title": "Preoperatif Hazırlık ve Cerrahi Yönetim Planı",
                "question": "Akut apandisit tanısı kesinleşen 8 yaşındaki bu hastanın Sarı Alandaki preoperatif hazırlık ve nihai yönetim planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Oral alımı kapatıp sadece intravenöz sıvı ve analjezi ile hastayı ameliyathaneye devretmek; profilaktik antibiyotiği cerrahi ekip batını açtıktan sonra intraoperatif dönemde başlamak",
                        "is_correct": False,
                        "scenario_update": "Preoperatif antibiyotik dozu insizyondan önce verilmediği için postoperatif dönemde cerrahi alan enfeksiyonu riski anlamlı derecede arttı.",
                        "teaching_point": "Akut apandisitte cerrahi alan enfeksiyonu ve intraabdominal apse gelişimini azaltmak için gram-negatif ve anaerob spektrumlu intravenöz antibiyotik profilaksisi cerrahi insizyondan 30-60 dakika önce başlanmalıdır.",
                    },
                    {
                        "text": "Perforasyon bulgusu olmadığı için cerrahi konsültasyon istemeden intravenöz seftriakson ve metronidazol başlayarak hastayı kırk sekiz saat acil gözlem ünitesinde medikal olarak izlemek",
                        "is_correct": False,
                        "scenario_update": "Cerrahi ekip değerlendirmesi olmaksızın acil gözlemde tutulan hastada 18. saatte artan karın ağrısı ve perfore apandisit tablosu gelişti.",
                        "teaching_point": "Çocuklarda akut apandisitin standart tedavisi apendektomidir; seçilmiş olgularda non-operatif yönetim dahi mutlaka çocuk cerrahisi konsültasyonu ve servis yatışı altında yürütülür.",
                    },
                    {
                        "text": "Oral amoksisilin-klavulanat ve analjezik reçete ederek hastayı ayaktan çocuk cerrahisi poliklinik kontrolüne yönlendirmek ve ateş yükselirse tekrar acil servise başvurmasını tembihleyerek taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Taburcu edilen hasta 24 saat sonra yaygın peritonit, yüksek ateş ve septik görünümle acil servise tekrar getirildi.",
                        "teaching_point": "Akut apandisit tanısı alan hiçbir hasta acil servisten oral antibiyotikle taburcu edilemez; acil cerrahi yatış ve müdahale şarttır.",
                    },
                    {
                        "text": "Oral alımı kapatıp intravenöz sıvıyı sürdürmek, gram-negatif ve anaerob etkili intravenöz antibiyotik profilaksisi başlayarak acil apendektomi için çocuk cerrahisine devretmek",
                        "is_correct": True,
                        "explanation": "Komplike olmamış akut apandisitte oral stop, İV hidrasyon, uygun preoperatif İV antibiyotik (örn. sefazolin + metronidazol veya ampisilin-sulbaktam) ve acil apendektomi standart yaklaşımdır.",
                        "new_finding": "Çocuk cerrahisi konsültasyonu ile hasta ameliyathaneye devredildi; preoperatif antibiyotik profilaksisi altında başarılı laparoskopik apendektomi yapıldı ve hasta komplikasyonsuz taburcu edildi.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y12",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "5 Aylık",
        "gender": "Erkek",
        "complaint": "Burun akıntısı sonrası başlayan hızlı nefes alma, göğüs kafesinde çekilmeler, hırıltı ve memeyi emememe",
        "history": (
            "Annesi 5 aylık erkek bebeği Sarı Alana getiriyor: 'Üç gün önce hafif burun tıkanıklığı ve "
            "hapşırıkla başladı. Dün gece öksürüğü arttı, bu sabahtan beri göğsü körük gibi hızlı inip kalkıyor, "
            "nefes alırken kaburgalarının altı içeri çöküyor ve hırıltısı dışarıdan duyuluyor. Memeyi ağzına "
            "alıyor ama nefes nefese kalıp hemen bırakıyor, son 8 saattir neredeyse hiç ememedi ve bezi kuru kaldı.'"
        ),
        "final_diagnosis": "Akut Viral Bronşiyolit (Orta-Ağır Şiddette - RSV Enfeksiyonu)",
        "disposition": "Sarı Alanda Yüzeyel Nazal Aspirasyon + Nemlendirilmiş Oksijen + İV Hidrasyon Sonrası Pediatri Servisine Yatış",
        "case_pearl": (
            "Akut viral bronşiyolit 2 yaş altı çocuklarda en sık alt solunum yolu enfeksiyonudur (en sık etken RSV). "
            "Patofizyolojide bronkospazmdan ziyade bronşiyol lümeninde mukus tıkacı, epitel nekrozu ve ödem "
            "bulunduğundan AAP ve güncel kılavuzlara göre rutin bronkodilatör (salbutamol), sistemik/inhale "
            "kortikosteroid, antibiyotik ve rutin akciğer grafisi önerilmez. Tedavinin kanıtlanmış üç temel taşı: "
            "yüzeyel nazal aspirasyon, hipoksemi (SpO2 <%90-92) varlığında nemlendirilmiş oksijen ve oral alımı "
            "bozulan/takipneik (SS >60/dk) bebekte NG veya İV hidrasyon desteğidir."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda Solunum Değerlendirmesi ve Klinik Ciddiyet Tayini",
                "question": "Üst solunum yolu enfeksiyonu bulgularını takiben hızlı nefes alma, çekilmeler ve beslenememe ile başvuran 5 aylık bebekte ilk değerlendirmeniz nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Muayeneyi tamamlamadan önce hava yolu ödemini ve spazmını hızla çözmek amacıyla bebeğe ardışık üç doz nebulize salbutamol ve intravenöz metilprednizolon uygulamak",
                        "is_correct": False,
                        "scenario_update": "Uygulanan nebulize beta-agonist sonrası bebeğin kalp hızı 195/dk'ya yükseldi ve ajitasyonu arttı; ancak solunum sayısı ve çekilmelerinde anlamlı düzelme olmadı.",
                        "teaching_point": "Süt çocuklarının ilk viral alt solunum yolu hırıltı atağında patoloji bronkospazm değil mukus ödemi ve hücresel debristir; rutin bronkodilatör ve sistemik steroid tedavisi önerilmez.",
                    },
                    {
                        "text": "Bebeğin 8 saattir ememediğini dikkate alarak solunum muayenesinden önce hipoglisemiyi önlemek için annenin kucağında biberonla formül mama içirip beslenme toleransını görmek",
                        "is_correct": False,
                        "scenario_update": "Dakikada 60'ın üzerinde nefes alan bebek biberonla beslenmeye çalışılırken öksürük krizi, desatürasyon ve aspirasyon tehlikesi geçirdi.",
                        "teaching_point": "Belirgin takipnesi (solunum sayısı >60/dk) ve çekilmeleri olan süt çocuklarında yutma-solunum koordinasyonu bozulduğundan aspirasyon riski yüksektir; önce solunum stabilize edilmelidir.",
                    },
                    {
                        "text": "Pediatrik Değerlendirme Üçgeni, vital bulgular, oda havası oksijen satürasyonu, solunum iş yükü, bilateral akciğer oskültasyonu ve hidrasyon durumunu sistematik değerlendirmek",
                        "is_correct": True,
                        "explanation": "Alt solunum yolu obstrüksiyonu ile başvuran süt çocuğunda hastalık şiddeti; takipne derecesi, retraksiyonlar, oda havası SpO2 düzeyi ve hidrasyon/beslenme durumu ile klinik olarak belirlenir.",
                        "new_finding": "Vital bulgular: Ateş 37.9°C, KTA 158/dk, SS 64/dk, oda havasında SpO2 %89. Muayenede belirgin subkostal ve interkostal çekilmeler, burun kanadı solunumu, bilateral yaygın ekspiratuar hırıltı (wheezing) ve bazallerde ince krepitan raller saptandı. Ağız mukozası hafif kuru, ön fontanel normal bombelikte, kapiller dolum zamanı 2 saniye.",
                    },
                    {
                        "text": "Solunum sıkıntısının nedenini netleştirmek için fizik muayene ve oksijen satürasyonu ölçümünü bekletip bebeği doğrudan radyoloji ünitesine iki yönlü akciğer grafisine göndermek",
                        "is_correct": False,
                        "scenario_update": "Oda havasında hipoksemik (%89) olan bebek oksijen desteği verilmeden radyolojiye gönderildiği için işlem sırasında siyanoz gelişti ve grafide yalnızca nonspesifik havalanma artışı görüldü.",
                        "teaching_point": "Hipoksemik ve solunum sıkıntılı bebek stabilize edilmeden görüntülemeye gönderilmez; ayrıca tipik viral alt solunum yolu hırıltısında rutin akciğer grafisi gereksiz antibiyotik kullanımını artırdığı için önerilmez.",
                    },
                ],
            },
            {
                "stage_title": "İlk Basamak Acil Destek Tedavisi ve Tetkik Planı",
                "question": "Oda havasında SpO2 %89, solunum sayısı 64/dk olan ve oral beslenemeyen bu 5 aylık bebekte kılavuzlara uygun ilk müdahaleniz ne olmalıdır?",
                "options": [
                    {
                        "text": "Serum fizyolojik ile yüzeyel nazal aspirasyon uygulamak, nemlendirilmiş oksijenle satürasyonu %90-92 üzerinde tutmak ve oral alımı kesip intravenöz izotonik sıvı başlamak",
                        "is_correct": True,
                        "explanation": "Küçük süt çocukları zorunlu burun soluyucusu olduğundan nazal pasajın açılması solunum iş yükünü belirgin azaltır; SpO2 <%90-92 ise oksijen ve SS >60/dk olup beslenemiyorsa İV/NG hidrasyon temel tedavidir.",
                        "new_finding": "Yüzeyel nazal aspirasyon sonrası üst hava yolu pasajı rahatladı. Nazal kanülle 1.5 L/dk nemlendirilmiş oksijen altında SpO2 %95 düzeyine yükseldi, solunum sayısı 54/dk oldu. Damar yolu açılarak %5 dekstrozlu %0.9 NaCl idame sıvısı başlandı; rutin laboratuvar ve radyolojik tetkik istenmedi.",
                    },
                    {
                        "text": "Rutin akciğer grafisi, tam kan sayımı ve kan kültürü göndererek ikincil bakteriyel enfeksiyon profilaksisi için ampirik intravenöz seftriakson ve nebulize budesonid başlamak",
                        "is_correct": False,
                        "scenario_update": "Hemogramda lökosit 9.800/mm³ (lenfosit hakimiyeti), grafide peribronşiyal kalınlaşma ve hiperinflasyon saptandı; verilen antibiyotik ve inhale steroid klinik tabloda hiçbir iyileşme sağlamadı.",
                        "teaching_point": "Viral alt solunum yolu obstrüksiyonunda eşlik eden bakteriyel enfeksiyon oranı çok düşüktür (<%1-2); yüksek ateş, toksik görünüm veya fokal konsolidasyon yoksa rutin laboratuvar, grafi ve antibiyotik endike değildir.",
                    },
                    {
                        "text": "Nazal aspirasyon yapmadan doğrudan yüksek doz nebulize salbutamol ve ipratropium bromür kombinasyonu başlayarak yanıt alınamazsa intravenöz magnezyum sülfat infüzyonuna hızla geçmek",
                        "is_correct": False,
                        "scenario_update": "Üst hava yolundaki yoğun mukus temizlenmediği ve oksijen verilmediği için SpO2 %88 düzeyinde kaldı; antikolinerjik ve magnezyum tedavisi sekresyonları koyulaştırıp taşikardi yaptı.",
                        "teaching_point": "Süt çocuklarında ipratropium bromür ve magnezyum sülfatın viral küçük hava yolu obstrüksiyonunda yeri yoktur; öncelik nazal temizlik ve oksijenizasyondur.",
                    },
                    {
                        "text": "Bebeği sakinleştirmek ve öksürük nöbetlerini azaltmak amacıyla oral antihistaminik ve dekstrometorfan içeren şurup vererek oksijen desteği olmadan iki saat boyunca izlemek",
                        "is_correct": False,
                        "scenario_update": "Verilen sedatif ve antitussif şurup sonrasında bebeğin öksürük refleksi baskılandı, mukus tıkaçları arttı ve solunum depresyonu ile desatürasyon gelişti.",
                        "teaching_point": "Süt çocukları ve küçük çocuklarda öksürük kesici (antitussif) ve antihistaminik preparatlar mukus klirensini bozup apne ve solunum depresyonu yaptığı için kesinlikle kontrendikedir.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Bulgular Doğrultusunda Tanı",
                "question": "Süt çocuğunda prodromal rinit sonrası gelişen ilk hırıltı atağı, takipne, çekilmeler ve yaygın ekspiratuar wheezing ile krepitan raller hangi tanıyı gösterir?",
                "options": [
                    {
                        "text": "Fokal bakteriyel lobar pnömoni",
                        "is_correct": False,
                        "scenario_update": "Bakteriyel lobar pnömonide yüksek ateş, toksik görünüm ve oskültasyonda tek taraflı fokal krepitasyon veya solunum seslerinde azalma beklenir.",
                        "teaching_point": "ÜSYE prodromu sonrası bilateral yaygın ekspiratuar wheezing ve sibilan/krepitan raller bakteriyel lobar pnömoniden ziyade yaygın bronşiyoler tutulumu gösterir.",
                    },
                    {
                        "text": "Akut orta-ağır viral bronşiyolit",
                        "is_correct": True,
                        "explanation": "İki yaş altı çocukta viral ÜSYE prodromunu izleyen ilk wheezing atağı, takipne, retraksiyonlar ve ince raller akut viral bronşiyolit tanısını koydurur; tanı kliniktir.",
                        "new_finding": "Kesin tanı: Akut Viral Bronşiyolit (Orta-Ağır Şiddette).",
                    },
                    {
                        "text": "Akut viral laringotrakeobronşit (krup)",
                        "is_correct": False,
                        "scenario_update": "Krup sendromunda havlar tarzda öksürük, ses kısıklığı ve inspiratuar stridor ön plandadır; bu bebekte ise ekspiratuar hırıltı ve alt solunum yolu bulguları mevcuttur.",
                        "teaching_point": "İnspiratuar stridor ekstratorasik üst hava yolu darlığını, ekspiratuar wheezing ve ince raller ise intratorasik alt hava yolu (bronşiyol) darlığını işaret eder.",
                    },
                    {
                        "text": "Boğmaca (Bordetella pertussis) pnömonisi",
                        "is_correct": False,
                        "scenario_update": "Boğmacada paroksismal boğulur tarzda öksürük nöbetleri, inspiratuar 'whoop' sesi, öksürük sonrası kusma ve belirgin lenfositoz görülür.",
                        "teaching_point": "Akut başlayan rinit sonrası yaygın ekspiratuar wheezing ve raller tipik viral bronşiyolit tablosudur.",
                    },
                ],
            },
            {
                "stage_title": "Klinik İzlem Yanıtı ve Yatış Kararı",
                "question": "Sarı Alanda 4 saatlik izlemde oksijen kesildiğinde SpO2'si %89'a düşen, solunum sayısı 56/dk olan ve emmeyi sürdüremeyen 5 aylık bebeğin yönetim kararı ne olmalıdır?",
                "options": [
                    {
                        "text": "Nebulize %3 hipertonik salin ve evde kullanmak üzere salbutamol inhaler reçete ederek aileyi ertesi gün poliklinik kontrolüne çağırmak üzere taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Evde oksijen desteği alamayan ve beslenemeyen bebek gece saatlerinde derin hipoksemi ve dehidratasyon tablosuyla acil servise geri getirildi.",
                        "teaching_point": "Oda havasında SpO2 <%90-92 olan (oksijen bağımlılığı süren) ve oral alımı yetersiz olan bronşiyolitli bebekler kesin yatış endikasyonu taşır; eve taburcu edilemez.",
                    },
                    {
                        "text": "Bebeğe tek doz intramusküler deksametazon ve seftriakson uyguladıktan sonra oksijen satürasyonu %90 sınırına yaklaştığı için evde anne sütüyle beslenmek üzere göndermek",
                        "is_correct": False,
                        "scenario_update": "Parenteral steroid ve antibiyotik bronşiyolit seyrini değiştirmedi; evde ememeyen bebekte hipoksemi ve solunum yorgunluğu ilerledi.",
                        "teaching_point": "Bronşiyolitte parenteral steroid ve antibiyotik uygulayarak hastayı taburcu etmek kılavuzlara aykırıdır; hipoksemi ve beslenme bozukluğu servis yatışı gerektirir.",
                    },
                    {
                        "text": "Mevcut klinik tabloyu ağır solunum yetmezliği kabul ederek bebeği derhal entübe edip mekanik ventilasyon desteği için çocuk yoğun bakım ünitesine yatırmak",
                        "is_correct": False,
                        "scenario_update": "Düşük akımlı nazal oksijenle SpO2'si %95 olan ve apnesi bulunmayan bebeğe gereksiz endotrakeal entübasyon uygulanması barotravma ve ventilatör ilişkili komplikasyonlara yol açtı.",
                        "teaching_point": "Düşük akımlı nazal kanül oksijen ile satürasyonu düzelen, apnesi veya ağır hiperkapnik solunum yetmezliği olmayan orta-ağır bronşiyolit olguları genel pediatri servisinde izlenir.",
                    },
                    {
                        "text": "Devam eden oksijen ihtiyacı, takipne ve beslenme yetersizliği nedeniyle bebeği nemlendirilmiş oksijen, nazal temizlik ve hidrasyon takibi için pediatri servisine yatırmak",
                        "is_correct": True,
                        "explanation": "Bronşiyolitte oda havasında SpO2 <%90-92 olması, belirgin takipne/çekilme ve oral alımın <%50'ye düşmesi pediatri servisine yatışın temel kriterleridir.",
                        "new_finding": "Bebek pediatri servisine yatırıldı; nemlendirilmiş oksijen, aralıklı nazal aspirasyon ve İV/NG hidrasyon desteği ile 3. günde oksijen ihtiyacı kalmadı, aktif emmeye başladı ve şifayla taburcu edildi.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y13",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "6 Yaş",
        "gender": "Kız",
        "complaint": "Bacaklarda ve kalçada basmakla solmayan kırmızı-mor döküntüler, diz ve ayak bileklerinde şişlik-ağrı ve aralıklı kıvrandıran karın ağrısı",
        "history": (
            "Annesi 6 yaşındaki kızını Sarı Alana getiriyor: 'Yaklaşık 10 gün önce üst solunum yolu enfeksiyonu "
            "geçirmişti. Dün bacaklarında kırmızı lekeler belirdi, bugün lekeler çoğalarak ele gelen morumsu "
            "kabartılara dönüştü. Ayak bilekleri ve sağ dizi şişti, üzerine basamıyor. Ayrıca sabahtan beri "
            "aralıklarla karnını tutup iki büklüm kıvranarak ağlıyor; ağrı nöbet şeklinde gelip sonra hafifliyor.'"
        ),
        "final_diagnosis": "Henoch-Schönlein Purpurası (HSP / IgA Vasküliti - Gastrointestinal, Eklem ve Renal Tutulumlu)",
        "disposition": "Sarı Alanda Batın USG (İnvajinasyon Dışlama), TİT ve Böbrek Fonksiyon Testleri Sonrası Pediatri Servisine Yatış",
        "case_pearl": (
            "Henoch-Schönlein Purpurası (IgA vasküliti), çocukluk çağının en sık sistemik küçük damar vaskülitidir. "
            "EULAR/PRINTO/PRES kriterlerine göre trombositopeni olmaksızın alt ekstremite/gluteal bölgede baskın "
            "palpabl purpura zorunlu kriterdir; buna artrit/artralji, kolik karın ağrısı/GİS kanaması ve renal "
            "tutulum (hematüri/proteinüri) eşlik eder. En önemli akut cerrahi komplikasyon bağırsak duvarı ödemi "
            "ve submukozal hematomun 'lead point' oluşturmasıyla gelişen ileo-ileal invajinasyondur (ultrasonografi "
            "ile dışlanır). Uzun dönem prognozu ise böbrek tutulumu belirler; tüm hastalar en az 6 ay TİT ve kan "
            "basıncı ile izlenmelidir."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda Döküntü, Eklem ve Batın Muayenesi",
                "question": "Alt ekstremitelerde döküntü, eklem şişliği ve kolik karın ağrısı ile başvuran 6 yaşındaki bu çocukta ilk muayenede neleri değerlendirmelisiniz?",
                "options": [
                    {
                        "text": "Döküntülerin kaşıntılı papüler karakterde olduğunu varsayarak yalnızca cilt yüzeyini incelemek ve eklem ağrısını büyüme ağrısına bağlayıp batın muayenesini sonraya ertelemek",
                        "is_correct": False,
                        "scenario_update": "Döküntülerin basmakla solmayan purpurik karakteri, hipertansiyon sınırındaki kan basıncı ve akut batın riski gözden kaçırıldı.",
                        "teaching_point": "Alt ekstremitede basmakla solmayan purpura, periartiküler şişlik ve kolik karın ağrısı birlikteliği sistemik bir hastalığı gösterir; tam kan basıncı ve batın muayenesi zorunludur.",
                    },
                    {
                        "text": "Döküntünün basmakla solup solmadığını ve ele gelip gelmediğini, alt ekstremite dağılımını, eklem şişliğini, kan basıncını ve batın bulgularını değerlendirmek",
                        "is_correct": True,
                        "explanation": "Yerçekimine bağımlı simetrik palpabl purpura, periartiküler ödem/artrit, olası nefrit için kan basıncı ölçümü ve akut batın komplikasyonları için karın muayenesi ilk adımda değerlendirilmelidir.",
                        "new_finding": "Vital bulgular: TA 118/74 mmHg (yaş ve boya göre 90-95. persentil), KTA 104/dk, Ateş 37.2°C. Bilateral alt ekstremite ekstansör yüzlerde ve gluteal bölgede simetrik, basmakla solmayan, ele gelen (palpabl) purpurik lezyonlar saptandı. Sağ diz ve sol ayak bileğinde periartiküler ödem ve hareket kısıtlılığı mevcut. Batında periumbilikal hassasiyet var, defans veya ele gelen kitle yok.",
                    },
                    {
                        "text": "Yaygın purpurik döküntüleri akut trombositopenik kanama kabul ederek fizik muayeneyi bekletip hastaya derhal acil trombosit süspansiyonu ve taze donmuş plazma hazırlamak",
                        "is_correct": False,
                        "scenario_update": "Laboratuvar sonucu görülmeden hazırlanan kan ürünleri gereksiz transfüzyon riski oluşturdu; oysa hastanın döküntüleri trombositopenik peteşi değil ele gelen palpabl purpuraydı.",
                        "teaching_point": "Ele gelen (palpabl) ve yerçekimine bağımlı simetrik purpura trombositopeniden ziyade küçük damar inflamasyonunu düşündürür; hemogram görülmeden ve hayatı tehdit eden kanama olmadan trombosit verilmez.",
                    },
                    {
                        "text": "Eklem şişliği ve yürüyememe yakınmasını ön planda tutarak septik artrit şüphesiyle sağ diz ekleminden acil yatak başı artrosentez işlemi uygulamak",
                        "is_correct": False,
                        "scenario_update": "Ateşi olmayan ve simetrik purpurik döküntüleri bulunan çocuğa yapılan invaziv eklem ponksiyonu gereksiz ağrı ve eklem içi kanama/enfeksiyon riski yarattı.",
                        "teaching_point": "Alt ekstremite purpurasına eşlik eden gezici ve periartiküler ağırlıklı oligoartrit tablosu genellikle sekonder ve sekel bırakmayan inflamatuar karakterdedir; rutin artrosentez endike değildir.",
                    },
                ],
            },
            {
                "stage_title": "Laboratuvar Tetkikleri ve Batın Görüntülemesi",
                "question": "Simetrik palpabl purpura, artrit ve kolik karın ağrısı bulunan bu çocukta ayırıcı tanı ve komplikasyon taraması için hangi tetkikleri istemelisiniz?",
                "options": [
                    {
                        "text": "Yalnızca tam kan sayımı ve periferik yayma isteyerek trombosit sayısı normal gelirse idrar tetkiki veya batın görüntülemesi yapmadan hastayı izleme almak",
                        "is_correct": False,
                        "scenario_update": "Trombosit sayısı 420.000/mm³ gelince ek tetkik yapılmadı; ancak hastanın mikroskopik hematürisi, proteinürisi ve bağırsak duvarı ödemi atlandı.",
                        "teaching_point": "Palpabl purpura ve kolik karın ağrısı olan her çocukta trombosit sayısına ek olarak böbrek tutulumu için tam idrar tetkiki ve cerrahi komplikasyonlar için batın ultrasonografisi şarttır.",
                    },
                    {
                        "text": "Kesin tanı koymak amacıyla acil serviste cilt punch biyopsisi ve kemik iliği aspirasyonu planlayarak batın ağrısı için direkt karın grafisi çekmek",
                        "is_correct": False,
                        "scenario_update": "Tipik klinik bulguları olan hastaya gereksiz invaziv işlemler planlandı; direkt batın grafisi ise bağırsak duvarı ödemini ve olası invajinasyonu değerlendirmede yetersiz kaldı.",
                        "teaching_point": "Tipik alt ekstremite palpabl purpurası ve normal trombosit sayısı olan çocuklarda tanı kliniktir; cilt veya kemik iliği biyopsisi yalnızca atipik prezentasyonlarda düşünülür.",
                    },
                    {
                        "text": "Kan kültürü, lomber ponksiyon ve kraniyal bilgisayarlı tomografi isteyerek sonuçları beklemeden yüksek doz intravenöz seftriakson ve vankomisin tedavisi derhal başlamak",
                        "is_correct": False,
                        "scenario_update": "Ateşi olmayan, genel durumu iyi ve hemodinamisi stabil olan çocuğa gereksiz lomber ponksiyon, radyasyon ve geniş spektrumlu antibiyotik uygulandı.",
                        "teaching_point": "Genel durumu iyi, afebril ve lezyonları alt ekstremite-gluteal bölgeye sınırlı palpabl purpura olgularında santral sinir sistemi enfeksiyonu taraması ve ampirik antibiyotik endike değildir.",
                    },
                    {
                        "text": "Tam kan sayımı, koagülasyon, üre-kreatinin, tam idrar tetkiki, gaitada gizli kan istemek ve akut komplikasyonlar için batın ultrasonografisi planlamak",
                        "is_correct": True,
                        "explanation": "Trombositopeni ve koagülopatiyi dışlamak için CBC/koagülasyon, nefrit taraması için TİT ve üre/kreatinin, GİS tutulumu ve özellikle ileo-ileal invajinasyonu dışlamak için batın USG zorunludur.",
                        "new_finding": "Laboratuvar: Lökosit 11.200/mm³, Hb 12.4 g/dL, Trombosit 420.000/mm³, PT ve aPTT normal. Tam idrar tetkikinde mikroskopik hematüri (her sahada 25-30 eritrosit) ve (+1) proteinüri saptandı. Üre 28 mg/dL, Kreatinin 0.52 mg/dL, gaitada gizli kan pozitif. Batın ultrasonografisinde ileal duvarlarda ödemli kalınlaşma izlendi, iç içe geçmiş bağırsak ansı (hedef görünümü) saptanmadı.",
                    },
                ],
            },
            {
                "stage_title": "Klinik ve Laboratuvar Bulgularıyla Kesin Tanı",
                "question": "Trombositopeni olmaksızın alt ekstremitede palpabl purpura, artrit, kolik karın ağrısı ve mikroskopik hematüri saptanan hastanın kesin tanısı nedir?",
                "options": [
                    {
                        "text": "Akut immün trombositopenik purpura (İTP)",
                        "is_correct": False,
                        "scenario_update": "İTP'de izole derin trombositopeni ve basmakla solmayan düz peteşiler/ekimozlar görülür; bu hastada trombosit sayısı 420.000/mm³ olup lezyonlar palpabldır.",
                        "teaching_point": "Normal veya yüksek trombosit sayısı ile birlikte ele gelen purpura, artrit ve nefrit varlığı İTP'yi kesin olarak dışlar.",
                    },
                    {
                        "text": "Akut fulminan meningokoksemi ve sepsis",
                        "is_correct": False,
                        "scenario_update": "Meningokoksemide yüksek ateş, toksik görünüm, hemodinamik instabilite, hızlı yayılan nekrotik purpura ve tüketim koagülopatisi bulunur.",
                        "teaching_point": "Afebril, genel durumu iyi, normal koagülasyon ve trombosit değerlerine sahip simetrik alt ekstremite purpurası meningokoksemi değil küçük damar vaskülitidir.",
                    },
                    {
                        "text": "Henoch-Schönlein purpurası (IgA vasküliti)",
                        "is_correct": True,
                        "explanation": "Trombositopeni olmadan alt ekstremite baskın palpabl purpuraya eşlik eden artrit, kolik karın ağrısı (GİS tutulumu) ve hematüri/proteinüri (renal tutulum) EULAR/PRINTO/PRES tanı kriterlerini tam karşılar.",
                        "new_finding": "Kesin tanı: Henoch-Schönlein Purpurası (IgA Vasküliti - GİS, Eklem ve Renal Tutulumlu).",
                    },
                    {
                        "text": "Tipik hemolitik üremik sendrom (HÜS)",
                        "is_correct": False,
                        "scenario_update": "HÜS tablosunda mikroanjiyopatik hemolitik anemi, belirgin trombositopeni ve akut böbrek hasarı triadı görülür; hastamızda Hb ve trombosit normaldir.",
                        "teaching_point": "Hemoglobin, trombosit ve kreatinin değerlerinin normal olması hemolitik üremik sendromu dışlar.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi Planı ve Uzun Dönem Renal İzlem",
                "question": "Gastrointestinal tutulumu, eklem ağrısı ve mikroskopik hematürisi olan 6 yaşındaki bu HSP hastasının tedavi ve takip planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Şiddetli karın ağrısı için sistemik prednizolon (1-2 mg/kg/gün) ve parasetamol başlayıp servise yatırmak; en az altı ay idrar ve tansiyon izlemi planlamak",
                        "is_correct": True,
                        "explanation": "Şiddetli kolik karın ağrısı ve submukozal bağırsak ödemi olan HSP olgularında kısa süreli sistemik kortikosteroid (1-2 mg/kg/gün prednizolon/metilprednizolon) semptomları hızla geriletir. Renal tutulum ilk 4-6 haftada veya 6 aya kadar gelişebileceğinden düzenli TİT ve tansiyon izlemi zorunludur.",
                        "new_finding": "Servis yatışı ve sistemik prednizolon tedavisi ile 24 saat içinde kolik karın ağrısı ve eklem şişliği geriledi. Hasta 6 aylık düzenli tam idrar tetkiki ve kan basıncı izlem planıyla pediatrik nefroloji takibine alındı.",
                    },
                    {
                        "text": "Eklem ve karın ağrısını kontrol altına almak için yüksek doz oral ibuprofen başlayıp steroid vermeden hastayı bir ay sonra nefroloji poliklinik kontrolüne çağırmak",
                        "is_correct": False,
                        "scenario_update": "Verilen nonsteroid antiinflamatuar ilaç (ibuprofen) gastrointestinal mukoza kanamasını artırdı ve mevcut renal tutulum (hematüri/proteinüri) üzerinde nefrotoksik etki yarattı.",
                        "teaching_point": "Aktif gastrointestinal tutulumu (gaitada gizli kan pozitifliği, şiddetli karın ağrısı) ve renal tutulumu (hematüri/proteinüri) olan HSP hastalarında NSAİİ'ler kontrendikedir; analjezi için parasetamol, şiddetli GİS ödemi için kortikosteroid tercih edilir.",
                    },
                    {
                        "text": "Böbrek tutulumunun ilerlemesini kesin olarak engellemek amacıyla tüm hastalarda rutin uygulanan intravenöz siklofosfamid ve plazmaferez protokolünü acil serviste derhal ve gecikmeden başlatmak",
                        "is_correct": False,
                        "scenario_update": "Kreatinini normal ve yalnızca hafif mikroskopik hematürisi olan hastaya uygulanan ağır immünsüpresif tedavi kemik iliği baskılanması ve enfeksiyon riskine yol açtı.",
                        "teaching_point": "Siklofosfamid, azatioprin veya plazmaferez gibi agresif tedaviler yalnızca biyopsi ile kanıtlanmış kresentik glomerülonefrit, hızlı ilerleyen nefrit veya nefrotik düzeyde dirençli proteinüride endikedir.",
                    },
                    {
                        "text": "Batın ultrasonografisinde invajinasyon saptanmadığı için hiçbir medikal tedavi başlamadan hastayı taburcu etmek ve yalnızca cilt döküntüleri tekrarlarsa polikliniğe başvurmasını aileye önermek",
                        "is_correct": False,
                        "scenario_update": "Şiddetli karın ağrısı ve oral alım güçlüğü olan çocuk evde dehidrate kaldı; ayrıca idrar takibi yapılmadığı için ilerleyen nefrit tablosu geç fark edildi.",
                        "teaching_point": "Şiddetli karın ağrısı olan HSP hastaları oral alım ve cerrahi komplikasyon (invajinasyon) takibi için yatırılmalı; döküntüler tamamen geçse bile en az 6 ay boyunca TİT ve kan basıncı izlemi sürdürülmelidir.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y14",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "4 Yaş",
        "gender": "Erkek",
        "complaint": "Göğsünde kuş çırpınması hissi, aniden başlayan kalp çarpıntısı, halsizlik ve hafif solukluk",
        "history": (
            "Annesi 4 yaşındaki oğlunu Sarı Alana getiriyor: 'Parkta oynarken birden yanıma geldi, anne kalbim "
            "göğsümden fırlayacak gibi atıyor, içeride kuş çırpınıyor dedi. Elimi göğsüne koyduğumda sayamayacağım "
            "kadar hızlı çarptığını fark ettim. Yaklaşık 45 dakikadır hiç durmadan aynı hızda devam ediyor. "
            "Rengi hafif soldu ve halsizleşti. Ateşi, kusması, ishali veya bilinen bir kalp hastalığı yok.'"
        ),
        "final_diagnosis": "Paroksismal Supraventriküler Taşikardi (SVT - Hemodinamik Olarak Stabil)",
        "disposition": "Sarı Alanda Otonomik Manevra / Hızlı İV Adenozin Puşe ile Sinüs Ritmine Döndürme, Kontrol EKG ve Pediatrik Kardiyoloji Konsültasyonu",
        "case_pearl": (
            "Supraventriküler Taşikardi (SVT), çocukluk çağının en sık semptomatik taşiaritmisidir. Süt çocuklarında "
            "KTA >220/dk, çocuklarda >180/dk olup R-R aralıkları tamamen sabittir, P dalgaları seçilemez/retrograddır "
            "ve QRS dardır (<0.09 sn). Hemodinamik olarak stabil hastada ilk adım vagal manevradır (küçük çocukta "
            "yüze 10-15 sn buz torbası; göz küresi basısı ve karotis masajı kontrendikedir!). Yanıtsızsa kalbe yakın "
            "antekübital damar yolundan üç yollu muslukla hızlı İV adenozin (ilk doz 0.1 mg/kg, maks 6 mg; ikinci doz "
            "0.2 mg/kg, maks 12 mg) ve hemen ardından 5-10 mL SF puşe uygulanır. Sinüs ritmine döndükten sonra WPW "
            "(delta dalgası) açısından mutlaka 12 derivasyonlu kontrol EKG çekilmelidir."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda Acil Monitörizasyon, EKG ve Hemodinamik Değerlendirme",
                "question": "Kalp hızı sayılamayacak kadar hızlı olan 4 yaşındaki bu çocukta tedavi algoritmasını belirlemek için ilk yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Çocuğu kardiyak monitöre bağlamak, 12 derivasyonlu EKG çekmek ve bilinç, kapiller dolum, nabızlar ile kan basıncını ölçerek hemodinamik stabiliteyi değerlendirmek",
                        "is_correct": True,
                        "explanation": "Pediatrik taşiaritmilerde ilk adım QRS genişliğini ve ritim düzenini EKG ile saptamak, eş zamanlı olarak hastanın hemodinamik açıdan stabil mi yoksa dekompanse şokta mı olduğunu belirlemektir.",
                        "new_finding": "Monitör ve 12 derivasyonlu EKG: Kalp hızı 245/dk, P dalgalarının seçilemediği, QRS süresinin 0.06 saniye olduğu, R-R aralıkları tamamen sabit, atımdan atıma değişkenlik göstermeyen dar kompleksli taşiaritmi izlendi. Hemodinamik değerlendirme: Bilinç açık (GKS 15), kapiller dolum zamanı 2 saniye, santral ve periferik nabızlar alınıyor, TA 94/58 mmHg (yaşa göre normotansif).",
                    },
                    {
                        "text": "Kalp hızının yüksekliğini oyun sonrası gelişen anksiyete ve sıvı kaybına bağlayarak EKG çekmeden önce hastaya oral su içirip sakin bir odada otuz dakika dinlendirmek",
                        "is_correct": False,
                        "scenario_update": "Monitörizasyon yapılmadan bekletilen çocukta 245/dk hızındaki taşiaritmi devam etti ve miyokardiyal yorgunluğa bağlı perfüzyon bozukluğu gelişmeye başladı.",
                        "teaching_point": "4 yaşındaki bir çocukta 180/dk üzerindeki ani başlangıçlı çarpıntı fizyolojik sinüs taşikardisi ile açıklanamaz; derhal monitörizasyon ve 12 derivasyonlu EKG gerektirir.",
                    },
                    {
                        "text": "Çarpıntının olası elektrolit bozukluğu veya tirotoksikoz kaynaklı olduğunu düşünerek EKG ve monitörizasyonu biyokimya ve tiroid fonksiyon testi sonuçları çıkana kadar ertelemek",
                        "is_correct": False,
                        "scenario_update": "Biyokimya sonuçları beklenirken geçen bir saat boyunca kalp hızı 245/dk düzeyinde kaldı ve hastada hipotansiyon gelişti.",
                        "teaching_point": "Akut taşiaritmilerde laboratuvar tetkikleri ritim tanısını ve acil hız/ritim kontrolünü asla geciktirmemelidir.",
                    },
                    {
                        "text": "Hastayı monitöre bağlamadan önce çarpıntıyı hızla sonlandırmak amacıyla ağızdan propranolol tablet kırarak içirmek ve bir saat sonra tekrar kontrol muayenesi yapmak",
                        "is_correct": False,
                        "scenario_update": "EKG çekilmeden verilen oral beta-blokerin etkisi başlamadığı gibi ritim kaynağı belgelenemedi ve akut yönetim gecikti.",
                        "teaching_point": "Akut semptomatik taşiaritmide EKG ile QRS süresi ve ritim tanımlanmadan oral antiaritmik verilmez.",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda İlk Non-İnvaziv Müdahale ve Damar Yolu Hazırlığı",
                "question": "Hemodinamik olarak stabil olan ve EKG'de 245/dk sabit hızlı dar kompleksli taşiaritmi saptanan 4 yaşındaki çocukta ilk müdahale adımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Bilinç açık ve kan basıncı normal olmasına rağmen kalp hızı 240/dk üzerinde olduğu için sedasyon vermeden derhal 1 J/kg dozunda senkronize kardiyoversiyon uygulamak",
                        "is_correct": False,
                        "scenario_update": "Bilinci tamamen açık ve perfüzyonu normal olan çocuğa sedasyonsuz uygulanan elektriksel şok ciddi ağrı ve travmaya neden oldu.",
                        "teaching_point": "Acil senkronize kardiyoversiyon yalnızca hemodinamik instabilite (hipotansiyon, şok, bilinç bozukluğu) varlığında ilk basamaktır; stabil hastada önce non-invaziv otonomik uyarı ve farmakolojik tedavi uygulanır.",
                    },
                    {
                        "text": "Hava yolunu kapatmadan yüze 10-15 saniye buzlu su torbası uygulayarak otonomik dalış refleksini uyarmak ve antekübital geniş damar yolu açmak",
                        "is_correct": True,
                        "explanation": "Hemodinamik açıdan stabil dar kompleksli taşiaritmide ilk adım parasempatik tonusu artırarak atriyoventriküler düğüm iletimini yavaşlatmaktır; küçük çocuklarda en güvenli yöntem ağız-burun kapatılmadan alına/yüze buz torbası uygulanmasıdır.",
                        "new_finding": "Yüze 15 saniye buz torbası uygulanması sırasında kalp hızı monitörde 245/dk olarak sabit kaldı, atımdan atıma hız değişikliği veya geçici yavaşlama gözlenmedi. Sol antekübital venden geniş lümenli damar yolu açıldı ve üç yollu musluk takılarak sürekli EKG kaydı altında farmakolojik müdahale hazırlığı tamamlandı.",
                    },
                    {
                        "text": "Çocuğun iki göz küresine başparmaklarla kuvvetlice bastırarak okülokardiyak refleksi uyarmak ve yanıt alınamazsa boyundan iki taraflı karotis sinüs masajı uygulamak",
                        "is_correct": False,
                        "scenario_update": "Uygulanan göz küresi basısı ve karotis masajı taşiaritmiyi sonlandırmadığı gibi çocukta retinal kanama, korneal travma ve serebral iskemi riski yarattı.",
                        "teaching_point": "Pediatrik yaş grubunda okülokardiyak refleks (göz basısı) retina dekolmanı ve glob hasarı riski nedeniyle, karotis masajı ise etkisiz ve komplikasyonlu olması nedeniyle kesinlikle kontrendikedir.",
                    },
                    {
                        "text": "Taşiaritminin gizli hipovolemiye bağlı olduğunu düşünerek 20 mL/kg izotonik sodyum klorür bolusu başlamak ve intravenöz kalsiyum kanal blokeri infüzyonu hazırlamak",
                        "is_correct": False,
                        "scenario_update": "İzotonik sıvı bolusu sabit 245/dk olan kalp hızında hiçbir değişiklik yapmadı; küçük çocukta hazırlanan kalsiyum kanal blokeri ise ağır hipotansiyon ve miyokardiyal depresyon riski taşıdı.",
                        "teaching_point": "Atımdan atıma hiç değişmeyen 245/dk sabit hızlı ve P dalgasız dar QRS taşiaritmi hipovolemik yanıt değildir; ayrıca küçük çocuklarda kalsiyum kanal blokerleri kardiyovasküler kollaps riski nedeniyle kontrendikedir.",
                    },
                ],
            },
            {
                "stage_title": "EKG ve Klinik Bulgularla Kesin Ritim Tanısı",
                "question": "Kalp hızı 245/dk, R-R aralıkları tamamen sabit, P dalgaları seçilemeyen ve QRS süresi 0.06 saniye olan bu dar kompleksli taşiaritminin kesin tanısı nedir?",
                "options": [
                    {
                        "text": "Belirgin fizyolojik sinüs taşikardisi",
                        "is_correct": False,
                        "scenario_update": "Sinüs taşikardisinde ateş, ağrı veya hipovolemi gibi bir neden bulunur, her QRS önünde normal P dalgası seçilir ve kalp hızı aktiviteyle değişkenlik gösterir.",
                        "teaching_point": "Kalp hızının >220/dk (çocukta >180/dk) olması, R-R mesafesinin tamamen sabit kalması ve P dalgalarının seçilememesi sinüs taşikardisini dışlar.",
                    },
                    {
                        "text": "Sürekli monomorfik ventriküler taşikardi",
                        "is_correct": False,
                        "scenario_update": "Ventriküler taşikardide QRS süresi yaşa göre uzamıştır (>0.09 sn) ve atriyoventriküler disosiasyon görülür; bu hastada QRS süresi 0.06 sn olup dardır.",
                        "teaching_point": "Normal ve dar QRS kompleksi (<0.09 sn), ventrikül aktivasyonunun normal His-Purkinje sistemi üzerinden gerçekleştiğini ve aritminin supraventriküler kaynaklı olduğunu gösterir.",
                    },
                    {
                        "text": "Düzensiz iletili atriyal fibrilasyon",
                        "is_correct": False,
                        "scenario_update": "Atriyal fibrilasyonda R-R aralıkları tamamen düzensizdir (aritmi absoluta) ve izoelektrik hatta fibrilasyon dalgaları izlenir.",
                        "teaching_point": "Milimetrik olarak eşit R-R aralıkları ile seyreden düzenli dar QRS taşikardi atriyal fibrilasyon değil reentran taşikardidir.",
                    },
                    {
                        "text": "Paroksismal supraventriküler taşikardi (SVT)",
                        "is_correct": True,
                        "explanation": "Ani başlayan, R-R aralıkları sabit, KTA >180-220/dk olan, P dalgalarının seçilemediği ve dar QRS (<0.09 sn) ile seyreden tablo atriyoventriküler düğüm bağımlı reentran SVT için tipiktir.",
                        "new_finding": "Kesin tanı: Paroksismal Supraventriküler Taşikardi (SVT - Hemodinamik Olarak Stabil).",
                    },
                ],
            },
            {
                "stage_title": "Farmakolojik Ritim Kontrolü ve Kardiyoloji İzlemi",
                "question": "Buz uygulamasına yanıt vermeyen hemodinamik olarak stabil SVT hastasında ilk tercih farmakolojik ajan, uygulama tekniği ve ritim dönüşü sonrası planınız ne olmalıdır?",
                "options": [
                    {
                        "text": "El sırtındaki ince damar yolundan 0.1 mg/kg adenozini 2 dakikada yavaş infüzyonla vermek ve ritim döner dönmez çocuğu poliklinik kontrolüyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Adenozinin plazma yarılanma ömrü 10 saniyenin altında olduğundan distal venden yavaş verildiğinde kalbe ulaşmadan eritrositler tarafından yıkıldı ve taşikardi sonlanmadı.",
                        "teaching_point": "Adenozin mutlaka kalbe yakın geniş bir venden (tercihen antekübital) üç yollu musluk kullanılarak çok hızlı bolus puşe ve hemen ardından 5-10 mL serum fizyolojik yıkaması (çift enjektör tekniği) ile verilmelidir.",
                    },
                    {
                        "text": "İlk tercih ilaç olarak intravenöz verapamil (0.1 mg/kg) puşelemek ve ritim sinüse döndükten sonra rekürrensi önlemek için oral digoksin yüklemesi yapmak",
                        "is_correct": False,
                        "scenario_update": "İntravenöz verapamil sonrası çocukta derin hipotansiyon gelişti; ayrıca olası aksesuar yolak (WPW) dışlanmadan digoksin verilmesi malign ventriküler aritmi riski doğurdu.",
                        "teaching_point": "Pediatrik SVT'de ilk tercih farmakolojik ajan her zaman adenozindir; verapamil miyokardiyal depresyon yapar, digoksin ise WPW sendromu dışlanmadan kullanılmaz.",
                    },
                    {
                        "text": "Antekübital venden üç yollu muslukla 0.1 mg/kg hızlı adenozin puşe ve serum fizyolojik yıkaması uygulayıp sinüs ritminde kontrol EKG çekmek",
                        "is_correct": True,
                        "explanation": "Stabil SVT'de vagal manevra başarısız olduğunda ilk tercih ilaç hızlı İV adenozindir (ilk doz 0.1 mg/kg, maks 6 mg; gerekirse ikinci doz 0.2 mg/kg, maks 12 mg). Sinüs ritmine döndükten sonra WPW (delta dalgası, kısa PR) varlığını araştırmak için 12 derivasyonlu EKG çekilir ve pediatrik kardiyoloji konsültasyonu istenir.",
                        "new_finding": "Sol antekübital venden 0.1 mg/kg (1.6 mg) adenozin hızlı puşe ve ardından 5 mL serum fizyolojik yıkaması ile saniyeler içinde sinüs ritmine (KTA 96/dk) dönüş sağlandı. Sinüs ritminde çekilen kontrol 12 derivasyonlu EKG'de PR mesafesi normaldi ve delta dalgası izlenmedi. Pediatrik kardiyoloji konsültasyonu ve 6 saatlik monitörize izlem sonrası hasta stabil olarak taburcu edildi.",
                    },
                    {
                        "text": "Farmakolojik tedaviyi atlayıp doğrudan 5 mg/kg intravenöz amiodaron yüklemesi başlamak ve ritim döndükten sonra hastayı entübe ederek yoğun bakıma devretmek",
                        "is_correct": False,
                        "scenario_update": "Yirmi dakikada verilen amiodaron infüzyonu sırasında ritim dönüşü gecikti ve bradikardi/hipotansiyon riski oluştu; stabil çocukta entübasyon tamamen gereksizdi.",
                        "teaching_point": "Amiodaron veya prokainamid yalnızca adenozinin (0.1 ve 0.2 mg/kg dozlarının) başarısız olduğu dirençli SVT olgularında kardiyoloji eşliğinde ikinci basamak olarak kullanılır.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y15",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "2.5 Yaş",
        "gender": "Kız",
        "complaint": "Yer fıstığı yerken aniden boğulur gibi morarıp öksürme, ardından nefes alırken tek taraflı hırıltı ve solunum sesinde azalma",
        "history": (
            "Ailesi 2.5 yaşındaki kız çocuğunu panikle Sarı Alana getiriyor: 'Yaklaşık 2 saat önce oturma odasında "
            "tabaktaki yer fıstıklarından yerken birden boğulur gibi şiddetle öksürmeye başladı, gözleri kızardı "
            "ve dudakları morardı. Birkaç kez öksürdükten sonra morarması geçti ve nefes alabildi ama o andan "
            "beri sürekli hırıltılı nefes alıyor ve aralıklı kuru öksürüğü devam ediyor. Daha önce astım veya "
            "benzer bir hırıltı öyküsü hiç yoktu.'"
        ),
        "final_diagnosis": "Trakeobronşiyal Yabancı Cisim Aspirasyonu (Sağ Ana Bronşta Organik Cisim ve Obstrüktif Hava Hapsi)",
        "disposition": "Sarı Alanda Sakin Pozisyon + Oksijen Desteği + İnspiratuar/Ekspiratuar Akciğer Grafisi Sonrası Genel Anestezi Altında Acil Rijit Bronkoskopi",
        "case_pearl": (
            "1-3 yaş arası çocukta kuruyemiş/oyuncak temasını takiben ani başlayan boğulma-öksürük-morarma "
            "(penetrasyon sendromu) ve oskültasyonda tek taraflı solunum seslerinde azalma/lokalize wheezing "
            "aksi kanıtlanana kadar trakeobronşiyal yabancı cisim aspirasyonudur. Organik cisimler (yer fıstığı, "
            "fındık, çekirdek) radyolüsendir ve grafide doğrudan görülmez; ekspiratuar veya lateral dekübit "
            "grafisinde check-valve (tek yönlü valf) mekanizmasına bağlı 'tek taraflı obstrüktif hava hapsi' "
            "ve karşı tarafa mediastinal şift saptanır. Normal akciğer grafisi tanıyı asla dışlamaz; kesin tanı "
            "ve tedavi ameliyathanede genel anestezi altında rijit bronkoskopidir."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda Hava Yolu Güvenliği ve Oskültasyon Değerlendirmesi",
                "question": "Yer fıstığı yerken ani boğulma ve morarma atağı geçiren, sonrasında öksürük ve hırıltısı süren 2.5 yaşındaki çocukta ilk yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Çocuğu ağlatmadan sakin tutarak hava yolu açıklığını, ses kalitesini, oksijen satürasyonunu ve bilateral akciğer oskültasyonunda solunum seslerinin simetrisini dikkatle değerlendirmek",
                        "is_correct": True,
                        "explanation": "Ses çıkarabilen ve etkili öksürebilen çocukta kısmi hava yolu obstrüksiyonu vardır; bu aşamada çocuk ajite edilmemeli, körlemesine manevralardan kaçınılmalı ve oskültasyonla asimetrik bulgular değerlendirilmelidir.",
                        "new_finding": "Vital bulgular: SS 38/dk, KTA 124/dk, oda havasında SpO2 %92, Ateş 36.7°C. Çocuk sakinleştirildiğinde ses çıkarabiliyor ve öksürebiliyor (kısmi hava yolu açıklığı korunmuş). Akciğer oskültasyonunda sağ hemitoraksta solunum sesleri belirgin azalmış ve sağ orta-alt zonda lokalize monofonik ekspiratuar wheezing duyuluyor; sol akciğer solunum sesleri doğal.",
                    },
                    {
                        "text": "Çocuğun ağzını dil basacağı ile zorla açıp farenks ve hipofarenkse işaret parmağıyla körlemesine süpürme manevrası uygulayarak takılan parçayı çıkarmaya çalışmak",
                        "is_correct": False,
                        "scenario_update": "Ağız içine yapılan körlemesine parmak manevrası çocuğu şiddetle ağlattı ve öğürme refleksiyle hava yolu güvenliğini tehlikeye soktu.",
                        "teaching_point": "Pediatrik ileri yaşam desteği kılavuzlarına göre ağız içinde doğrudan görülmeyen hiçbir cisim için körlemesine parmak süpürmesi yapılmaz; cismi subglottik alana iterek tam obstrüksiyona yol açabilir.",
                    },
                    {
                        "text": "Çocuk nefes alıp ağlayabildiği halde zaman kaybetmeden baş aşağı pozisyona getirip skapulalar arasına beş kez sert sırt vuruşu ve Heimlich manevrası uygulamak",
                        "is_correct": False,
                        "scenario_update": "Bronşa yerleşmiş olan fıstık parçası sert sırt vuruşu ve pozisyon değişikliğiyle karinadan trakeaya hareket ederek akut stridor ve siyanoza neden oldu.",
                        "teaching_point": "Sırt vuruşu ve abdominal bası (Heimlich) yalnızca tam hava yolu tıkanıklığında (etkisiz öksürük, ses çıkaramama, siyanoz) uygulanır; kısmi/bronşiyal obstrüksiyonda cismi trakeaya fırlatıp tam tıkanma yapabileceği için kontrendikedir.",
                    },
                    {
                        "text": "Ani başlayan ekspiratuar hırıltıyı akut bronkospazm atağı kabul ederek oskültasyon yapmadan önce ardışık üç doz nebulize salbutamol ve sistemik steroid başlamak",
                        "is_correct": False,
                        "scenario_update": "Nebulize salbutamol sonrası sağ hemitorakstaki solunum sesi azalması ve lokalize monofonik wheezing hiç değişmedi; mekanik obstrüksiyon tanısı gecikti.",
                        "teaching_point": "Öncesinde sağlıklı olan küçük çocukta yemek yerken ani başlayan öksürük ve tek taraflı monofonik wheezing difüz bronkospazm değil mekanik endobronşiyal obstrüksiyonu gösterir.",
                    },
                ],
            },
            {
                "stage_title": "Radyolojik Görüntüleme Seçimi ve Bulguların Yorumlanması",
                "question": "Sağ hemitoraksta solunum sesleri azalan ve lokalize ekspiratuar wheezing saptanan bu çocukta radyolojik görüntüleme yaklaşımınız nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Tek yönlü inspiratuar akciğer grafisi çekmek ve grafide radyoopak bir dansite görülmezse bronşiyal tıkanıklığı dışlayarak nebülize bronkodilatör tedaviyle izleme almak",
                        "is_correct": False,
                        "scenario_update": "Standart inspiratuar grafide radyoopak cisim görülmediği için mekanik tıkanıklık yanlışlıkla dışlandı; ancak yer fıstığının salgıladığı yağ asitleri 24 saat içinde ağır kimyasal pnömonit başlattı.",
                        "teaching_point": "Çocuklarda solunum yoluna kaçan cisimlerin %80-90'ı organik gıdalardır (fıstık, fındık, çekirdek) ve radyoopak değildir; ayrıca tek başına inspiratuar grafi tamamen normal görünebilir.",
                    },
                    {
                        "text": "Gıda parçasının özofagus üst uçta kalarak trakeaya dıştan bası yaptığını göstermek amacıyla hastaya acil baryumlu özofagus pasaj grafisi hemen çekmek",
                        "is_correct": False,
                        "scenario_update": "Solunum sıkıntısı olan çocuğa içirilen baryumlu kontrast madde aspirasyon riski yarattı ve yapılacak endoskopik havayolu girişiminin görüş alanını bozdu.",
                        "teaching_point": "Akut trakeobronşiyal obstrüksiyon şüphesinde kontrastlı özofagus pasaj grafisi endike değildir; hem aspirasyon riski taşır hem de genel anestezi öncesi oral alım yasağını bozar.",
                    },
                    {
                        "text": "İnspiratuar ve ekspiratuar akciğer grafileri çekerek tek taraflı obstrüktif hava hapsi, diyafram düzleşmesi ve mediastinal şift varlığını değerlendirmek",
                        "is_correct": True,
                        "explanation": "Radyolüsen organik cisimlerin oluşturduğu tek yönlü valf (check-valve) etkisini göstermek için inspiratuar grafiye ek olarak ekspiratuar grafi (küçük çocukta kooperasyon zor olduğundan bilateral lateral dekübit grafisi) çekilir.",
                        "new_finding": "Radyolojik İnceleme: Ekspiratuar akciğer grafisinde sağ hemitoraksta havalanma fazlalığı (check-valve mekanizmasına bağlı obstrüktif hava hapsi), sağ hemidiyaframda düzleşme, interkostal aralıklarda genişleme ve mediastenin sola doğru yer değiştirdiği izlendi. Radyoopak dansite saptanmadı.",
                    },
                    {
                        "text": "Direkt grafilerin organik maddeleri göstermede yetersiz olması nedeniyle çocuğu sedatize ederek doğrudan intravenöz kontrastlı toraks bilgisayarlı tomografisine acilen göndermek",
                        "is_correct": False,
                        "scenario_update": "Kısmi hava yolu obstrüksiyonu olan çocuğa BT çekimi için verilen sedasyon hava yolu tonusunu düşürerek desatürasyona yol açtı ve çocuğu gereksiz radyasyona maruz bıraktı.",
                        "teaching_point": "Tipik penetrasyon sendromu öyküsü ve tek taraflı oskültasyon/grafi bulgusu olan çocukta BT'ye gerek yoktur; doğrudan kesin girişimsel tanı ve tedaviye geçilir.",
                    },
                ],
            },
            {
                "stage_title": "Öykü, Fizik Muayene ve Radyolojik Bulgularla Kesin Tanı",
                "question": "Ani boğulma öyküsü, sağda solunum seslerinde azalma ve ekspiratuar grafide sağ hemitoraksta obstrüktif hava hapsi saptanan hastada kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Sağ spontan tansiyon pnömotoraks tablosu",
                        "is_correct": False,
                        "scenario_update": "Pnömotoraksta visseral plevra çizgisi ve periferde damar izi olmayan avasküler hiperlüsen alan görülür; bu hastada ise parankimal bronkovasküler izler korunmuş olup obstrüktif amfizem vardır.",
                        "teaching_point": "Ekspiryumda sönmeyen ancak bronkovasküler dallanmanın devam ettiği tek taraflı hiperlüsensi pnömotoraks değil endobronşiyal check-valve obstrüksiyonuna bağlı hava hapsidir.",
                    },
                    {
                        "text": "Trakeobronşiyal yabancı cisim aspirasyonu",
                        "is_correct": True,
                        "explanation": "Yer fıstığı yerken gelişen penetrasyon sendromu, sağda azalmış solunum sesleri ve ekspiratuar grafide sağ obstrüktif hava hapsi sağ ana bronş yabancı cisim aspirasyonu için tanısaldır.",
                        "new_finding": "Kesin tanı: Trakeobronşiyal Yabancı Cisim Aspirasyonu (Sağ Ana Bronşta Organik Yabancı Cisim).",
                    },
                    {
                        "text": "Akut viral laringotrakeobronşit (krup) atağı",
                        "is_correct": False,
                        "scenario_update": "Krup sendromu viral prodrom sonrası havlar tarzda öksürük ve inspiratuar stridorla seyreder; tek taraflı solunum sesi azalması ve asimetrik hava hapsi yapmaz.",
                        "teaching_point": "Asimetrik oskültasyon bulgusu ve tek taraflı obstrüktif amfizem üst hava yolu enfeksiyonunu dışlar.",
                    },
                    {
                        "text": "Konjenital sağ üst lober amfizem",
                        "is_correct": False,
                        "scenario_update": "Konjenital lober amfizem genellikle yenidoğan ve erken süt çocukluğu döneminde progresif solunum sıkıntısı ile başvurur ve en sık sol üst lobu tutar.",
                        "teaching_point": "2.5 yaşında sağlıklı bir çocukta kuruyemiş yerken akut başlayan tek taraflı hava hapsi edinsel endobronşiyal obstrüksiyondur.",
                    },
                ],
            },
            {
                "stage_title": "Kesin Girişimsel Tedavi ve Preoperatif Hazırlık",
                "question": "Sağ ana bronşta organik yabancı cisim aspirasyonu tanısı kesinleşen 2.5 yaşındaki çocuğun nihai tedavi yönetimi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Nebulize adrenalin ve göğüs fizyoterapisi ile postural drenaj uygulayarak sağ bronştaki fıstık parçasının öksürük refleksiyle kendiliğinden çıkmasını yirmi dört saat beklemek",
                        "is_correct": False,
                        "scenario_update": "Göğüs perküsyonu ve postural drenaj sırasında yerinden oynayan yer fıstığı subglottik darlığa sıkışarak tam hava yolu obstrüksiyonuna ve hipoksik arreste yol açtı.",
                        "teaching_point": "Trakeobronşiyal yabancı cisimlerde göğüs fizyoterapisi ve postural drenaj cismin ana trakeaya veya larenkse yer değiştirip asfiksi yapma riski nedeniyle kesinlikle kontrendikedir.",
                    },
                    {
                        "text": "Sarı Alanda yatak başında sedoanaljezi altında fleksibl fiberoptik nazofaringolaringoskop ile karinaya kadar ilerleyip fıstık parçasını biyopsi forsepsiyle çıkarmayı hemen denemek",
                        "is_correct": False,
                        "scenario_update": "Yatak başında güvensiz hava yolu koşullarında yapılan girişimde şişmiş yer fıstığı parçalandı, laringospazm ve ağır hipoksemi gelişti.",
                        "teaching_point": "Çocuklarda kesinleşmiş alt solunum yolu yabancı cisimlerinin çıkarılmasında altın standart, hem ventilasyonu sağlayan hem de optik forsepslerle güvenli kavrama imkanı veren genel anestezi altında rijit bronkoskopidir.",
                    },
                    {
                        "text": "Çocuğun oksijen satürasyonu %92 üzerinde olduğu için oral amoksisilin-klavulanat başlayarak bir hafta sonra kontrol akciğer grafisi ve elektif işlem planlamak",
                        "is_correct": False,
                        "scenario_update": "Organik yer fıstığı bronş sekresyonlarıyla şişerek tam obstrüksiyon, atelektazi, kimyasal arakidonik asit pnömoniti ve granülasyon dokusu geliştirdi.",
                        "teaching_point": "Özellikle yer fıstığı gibi yağlı organik yabancı cisimler su çekerek hızla şişer ve şiddetli kimyasal bronşit/granülasyon yapar; tanı konulduğunda geciktirilmeden çıkarılmalıdır.",
                    },
                    {
                        "text": "Oral alımı kesip çocuğu sakin tutarak oksijen desteğini sürdürmek ve ameliyathanede genel anestezi altında acil rijit bronkoskopi için cerrahiye devretmek",
                        "is_correct": True,
                        "explanation": "Pediatrik trakeobronşiyal yabancı cisim aspirasyonunda kesin tanı ve tedavi ameliyathane koşullarında genel anestezi altında yapılan rijit bronkoskopidir; işlem öncesi çocuk aç bırakılır ve ajitasyondan korunur.",
                        "new_finding": "Hasta çocuk cerrahisi tarafından ameliyathaneye alındı; genel anestezi altında rijit bronkoskopi ile sağ ana bronşu tıkayan yer fıstığı parçalanmadan çıkarıldı ve bronş lavajı yapıldı. İşlem sonrası sağ akciğer sesleri normale döndü ve hasta şifayla taburcu edildi.",
                    },
                ],
            },
        ],
    },
]
