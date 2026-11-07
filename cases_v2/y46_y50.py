# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - Y46-Y50 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "Y46",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "4 Yaşında",
        "gender": "Kız",
        "complaint": "İki haftadır geçmeyen kötü kokulu cıvık ishal, karında şişkinlik ve gaz sancısı",
        "history": "Annesi anlatıyor: 'Yaklaşık iki hafta önce köydeki yazlıktan döndük, orada kuyu suyu içiyordu. Dönüşten birkaç gün sonra günde 3-4 kez açık renkli, çok kötü kokulu, köpüklü, yağlı gibi parlayan cıvık kaka yapmaya başladı. Kan görmedim. Karnı sürekli guruldıyor, çok geğiriyor, iştahı azaldı. Ateşi olmadı. Pantolonları bollaştı.' Kreşe gidiyor. Tartı: 15.5 kg (iki hafta önce 16 kg).",
        "final_diagnosis": "Giardiyaz (Giardia duodenalis Enfeksiyonu)",
        "disposition": "Yeşil Alandan Oral Metronidazol, Hijyen ve Su Güvenliği Eğitimi ile Ayaktan Taburculuk",
        "case_pearl": "İki haftayı aşan, yağlı-köpüklü, kötü kokulu ishal, şişkinlik, geğirme ve kilo kaybı Giardia enfeksiyonunu düşündürür; kuyu suyu, kreş ve kamp öyküsü önemli ipuçlarıdır. Tanıda dışkı antijen testi veya PCR tek mikroskopiden daha duyarlıdır; mikroskopi seçilirse kistler aralıklı atıldığı için farklı günlerde 3 örnek incelenmelidir. Tedavide metronidazol 15 mg/kg/gün (3 dozda, 5-7 gün), tek doz tinidazol 50 mg/kg veya 3 gün nitazoksanid kullanılır; asemptomatik taşıyıcıların rutin tedavisi önerilmez.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "İki haftadır yağlı görünümlü ishali ve kilo kaybı olan bu 4 yaşındaki kız çocuğunda ilk değerlendirmede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "İshalin sürmesini laktoz intoleransı kabul ederek beslenme öyküsünü sorgulamak, süt ürünlerini kesip bir hafta sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Süt ürünleri kesildi; bir hafta sonra ishal ve kilo kaybı devam ediyordu, etken araştırılmamıştı.",
                        "teaching_point": "Sekonder laktoz intoleransı birçok enterik enfeksiyona eşlik edebilir; ancak altta yatan etken araştırılmadan diyet değişikliği tek başına yeterli değildir."
                    },
                    {
                        "text": "Uzamış ishali olan çocukta önce damar yolu açarak elektrolit, albümin ve tam kan sayımı almak, muayeneyi sonuçlar geldikten sonra tamamlamak",
                        "is_correct": False,
                        "scenario_update": "Elektrolitler ve albümin normal geldi; hidrasyonu iyi olan çocuğa gereksiz girişim yapıldı ve öykü eksik kaldı.",
                        "teaching_point": "Hidrasyonu iyi, genel durumu iyi çocukta ilk adım öykü ve muayenedir; kan tetkikleri seçici istenir."
                    },
                    {
                        "text": "Uzamış ishal nedeniyle hidrasyon durumunu, büyüme eğrisini, karın distansiyonunu ve ödem-solukluk gibi malabsorpsiyon bulgularını değerlendirip ayrıntılı maruziyet öyküsü almak",
                        "is_correct": True,
                        "explanation": "İki haftayı aşan ishalde akut dehidratasyonun yanı sıra büyüme etkilenmesi ve malabsorpsiyon bulguları değerlendirilmelidir. Su kaynağı, seyahat, kreş ve hayvan teması gibi maruziyetler etiyolojiye yön verir.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 98/dk, SS 20/dk, TA 94/60 mmHg, KDZ 1.5 sn. Tartı 15.5 kg (iki haftada 500 g kayıp), boy persentili korunmuş. Hidrasyonu iyi. Karın hafif distandü, timpanik, periumbilikal hafif hassasiyet; defans yok. Bağırsak sesleri hiperaktif. Ödem, solukluk, ağız kenarında çatlak yok. Perianal bölge doğal."
                    },
                    {
                        "text": "Karın distansiyonu nedeniyle cerrahi bir sorunu ekarte etmek için sağ alt kadranı ve rebound bulgusunu değerlendirip ayakta direkt batın grafisi planlamak",
                        "is_correct": False,
                        "scenario_update": "Peritoneal bulgu saptanmadı. Grafide yaygın gaz distansiyonu görüldü ve non-spesifik olarak raporlandı; maruziyet öyküsü alınmadı.",
                        "teaching_point": "Ateşsiz, iki haftalık yağlı ishal ve gaz şişkinliği cerrahi tablo düşündürmez; öykü ve malabsorpsiyon bulgularına odaklanılmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Stratejisi",
                "question": "Kuyu suyu maruziyeti olan, iki haftadır yağlı-köpüklü ishali süren bu çocukta en uygun tanısal yaklaşım hangisidir?",
                "options": [
                    {
                        "text": "Dışkıda protozoon antijen testi istemek veya farklı günlerde alınan üç örnekte mikroskopik inceleme yapmak; kan tetkikini klinik gerektirmedikçe istememek",
                        "is_correct": True,
                        "explanation": "Uzamış yağlı ishal ve su maruziyetinde protozoon araştırması önceliklidir. Dışkı antijen testi veya PCR tek mikroskopiden duyarlıdır; mikroskopide kistler aralıklı atıldığından üç ayrı örnek incelenmelidir.",
                        "new_finding": "Dışkı protozoon antijen testi pozitif. Mikroskopide armut biçimli, iki çekirdekli, hareketli kamçılı trofozoitler ve oval dört çekirdekli kistler görüldü; lökosit ve eritrosit yok. Gizli kan negatif."
                    },
                    {
                        "text": "Karın şişliği ve kilo kaybını değerlendirmek için batın ultrasonografisi ve tam kan sayımı isteyip dışkı incelemesini ultrason sonucuna göre planlamak",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografide sıvı dolu ince bağırsak ansları dışında bulgu yoktu; tam kan sayımı normaldi ve tablo aydınlatılamadı.",
                        "teaching_point": "Uzamış ishalde görüntüleme etkeni göstermez; dışkı incelemesi ilk basamak tetkiktir."
                    },
                    {
                        "text": "Dışkı kültürü göndermek ve sonuç gelene kadar ampirik oral siprofloksasin başlayarak bakteriyel etkenleri kapsamak, bir hafta sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Dışkı kültüründe patojen üremedi. Antibiyotik sonrası ishal azalmadı; çocuk bir hafta sonra aynı şikayetlerle geldi.",
                        "teaching_point": "Ateşsiz, kansız, yağlı uzamış ishalde bakteriyel etken olasılığı düşüktür; ampirik antibiyotik tanıyı geciktirir."
                    },
                    {
                        "text": "Malabsorpsiyon nedeniyle doku transglutaminaz IgA, total IgA, ter testi ve dışkı elastaz düzeyini birlikte isteyip sonuçlara göre gastroenterolojiye yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Serolojik testler ve elastaz normal geldi; ter testi için randevu verildi. Sonuçlar beklenirken ishal sürdü ve etken araştırılmadı.",
                        "teaching_point": "Akut maruziyet sonrası başlayan iki haftalık ishalde kronik malabsorpsiyon taramasından önce enfeksiyöz etkenler araştırılmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Kuyu suyu maruziyeti, yağlı-köpüklü uzamış ishal, şişkinlik ve dışkıda armut biçimli iki çekirdekli trofozoitler görülen bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Kriptosporidium enfeksiyonu",
                        "is_correct": False,
                        "scenario_update": "Kriptosporidiyumda bol sulu ishal baskındır ve tanı modifiye asit-fast boyama veya PCR ile konur; kamçılı trofozoit görülmez.",
                        "teaching_point": "Mikroskopik morfoloji protozoonların ayırıcı tanısında belirleyicidir."
                    },
                    {
                        "text": "Çölyak hastalığı",
                        "is_correct": False,
                        "scenario_update": "Akut maruziyet sonrası başlangıç ve dışkıda protozoonların görülmesi şikayetleri açıklıyor.",
                        "teaching_point": "Çölyak hastalığı uzun süreli malabsorpsiyon ve büyüme geriliğiyle seyreder; enfeksiyon dışlanmadan düşünülmez."
                    },
                    {
                        "text": "Giardia duodenalis enfeksiyonu",
                        "is_correct": True,
                        "explanation": "Kontamine su maruziyeti, yağlı-köpüklü kötü kokulu ishal, şişkinlik, geğirme, kilo kaybı ve dışkıda iki çekirdekli kamçılı trofozoitler Giardia duodenalis enfeksiyonunu doğrular.",
                        "new_finding": "Tanı: Giardiyaz (Giardia duodenalis)."
                    },
                    {
                        "text": "Amipli dizanteri",
                        "is_correct": False,
                        "scenario_update": "Amip enfeksiyonunda kanlı-mukuslu dışkı ve tenezm beklenir; bu çocukta dışkıda kan ve lökosit yok.",
                        "teaching_point": "Entamoeba trofozoitleri tek çekirdekli ve eritrosit fagosite eder; kamçılı değildir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu 15.5 kg'lık çocuğun tedavi ve izlem planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Oral metronidazol 30-50 mg/kg/gün dozunu üç eşit dozda on gün vermek ve tedavi sonrası iyileşmeyi göstermek için dışkı antijen testini tekrarlamak",
                        "is_correct": False,
                        "scenario_update": "Yüksek doz ve uzun süreli tedaviyle çocukta bulantı, metalik tat ve iştahsızlık gelişti; tekrar testi semptomsuz çocukta gereksiz bulundu.",
                        "teaching_point": "Bu doz aralığı amip enfeksiyonu için kullanılır; giardiyazda 15 mg/kg/gün yeterlidir. Semptomları düzelen çocukta kontrol testi gerekmez."
                    },
                    {
                        "text": "Oral metronidazol 15 mg/kg/gün dozunu üç eşit dozda 5-7 gün vermek, el hijyeni ve kaynatılmış su kullanımını anlatmak, semptomlu aile bireylerini değerlendirmek",
                        "is_correct": True,
                        "explanation": "Semptomatik giardiyazda metronidazol 15 mg/kg/gün (3 dozda, 5-7 gün) etkin bir seçenektir; alternatif olarak tek doz tinidazol 50 mg/kg veya 3 gün nitazoksanid kullanılabilir. Bulaşın önlenmesi için hijyen ve su güvenliği eğitimi verilir.",
                        "new_finding": "Metronidazol başlandı, aileye su kaynatma ve el yıkama önerileri verildi. Bir hafta sonraki kontrolde dışkı kıvamı normale döndü, şişkinlik geçti ve çocuk 300 g aldı."
                    },
                    {
                        "text": "Tek doz oral mebendazol vermek ve iki hafta sonra dozu tekrarlamak, tüm aile bireylerine de aynı tedaviyi eş zamanlı uygulamak",
                        "is_correct": False,
                        "scenario_update": "İki doz mebendazole rağmen ishal ve şişkinlik sürdü; çocuk üç hafta sonra kilo kaybıyla başvurdu.",
                        "teaching_point": "Mebendazol helmintlere etkilidir; protozoon enfeksiyonlarında ilk seçenek değildir."
                    },
                    {
                        "text": "Tablo kendiliğinden düzeleceği için antiparaziter vermeden yalnızca laktozsuz diyet, probiyotik ve hijyen önerileriyle iki hafta izlemek",
                        "is_correct": False,
                        "scenario_update": "İki hafta sonra ishal devam ediyordu, kilo kaybı 1 kg'a ulaştı ve kardeşinde de benzer şikayet başladı.",
                        "teaching_point": "Semptomatik ve kilo kaybı olan çocukta tedavi önerilir; tedavisiz izlem yalnızca asemptomatik taşıyıcılar için uygundur."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y47",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "3 Yaşında",
        "gender": "Erkek",
        "complaint": "Yarım saat önce ağzındaki madeni bir cismi yuttuğu düşünülüyor",
        "history": "Babası anlatıyor: 'Ablasının kumbarasıyla oynuyordu, ağzına bir şey attığını gördüm, öksürdü ve sonra yuttu. Ne olduğunu tam göremedim, para olabilir. Evde kumandalar ve oyuncaklar da var.' Şu anda ağlamıyor, su içti. Kusma, salya akması, yutma güçlüğü, öksürük veya hırıltı yok. Daha önce yutma sorunu, özofagus ameliyatı veya kronik hastalık yok.",
        "final_diagnosis": "Asemptomatik Midede Madeni Para (Gastrik Yabancı Cisim)",
        "disposition": "Normal Beslenme ve Dışkı Takibi Önerileriyle Yeşil Alandan Taburculuk",
        "case_pearl": "Yutulan madeni bir cisimde ilk soru pil olup olmadığıdır. Boyundan anüse ön-arka ve gerekirse yan grafi çekilir: düğme pil kenarda çift halka (halo) ve yan grafide basamak görüntüsü verir, madeni para tek ve düzgün konturludur. Özofagustaki para semptomluysa acil, asemptomatikse 12-24 saat içinde çıkarılır. Mideye geçmiş asemptomatik para evden izlenir. 2-4 hafta içinde dışkıyla çıktığı görülmezse grafi tekrarlanır.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Ne olduğu tam bilinmeyen metal bir cisim yutan, şu an yakınması olmayan bu çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Havayolu, solunum sesleri, salya, yutma ve göğüs ağrısını değerlendirip cismin pil olup olmadığını sorgulamak ve görüntülemeyle yerini belirlemeyi planlamak",
                        "is_correct": True,
                        "explanation": "Önce havayolu ve solunum güvenliği değerlendirilir. Cismin niteliği, özellikle düğme pil olasılığı yönetimi tamamen değiştirdiği için öyküde ve görüntülemede netleştirilmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 36.7°C, KTA 108/dk, SS 24/dk, SpO2 %99. Huzursuzluk yok, salya akması yok, sıvı yutuyor. Solunum sesleri eşit, stridor veya hışıltı yok. Karın yumuşak, hassasiyet yok. Baba evdeki pil kapaklarının kapalı olduğunu ve kumbaranın yanında bir eksik para bulunduğunu doğruladı."
                    },
                    {
                        "text": "Cismi geri çıkarması için tuzlu su içirerek ya da parmakla öğürterek kusturmaya çalışmak, cisim gelmezse görüntüleme planlamak",
                        "is_correct": False,
                        "scenario_update": "Kusturma girişimi sırasında çocuk öksürdü ve ağladı; cisim çıkmadı, aspirasyon riski yaratıldı.",
                        "teaching_point": "Yabancı cisim yutmada kusturma kontrendikedir; özofagusta takılma, mukozal yaralanma ve aspirasyon riskini artırır."
                    },
                    {
                        "text": "Çocuk sıvı yutabildiğine ve hiçbir yakınması olmadığına göre görüntülemeye gerek görmeden dışkı takibi önererek ailesiyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Cismin niteliği ve yeri belirlenmeden taburcu edildi; aile ertesi gün evde bir pilin eksik olduğunu fark edip geri döndü.",
                        "teaching_point": "Asemptomatik olmak özofagusta takılı cismi veya pili dışlamaz; niteliği bilinmeyen metal cisimde görüntüleme yapılmalıdır."
                    },
                    {
                        "text": "Cismin aşağı inmesini kolaylaştırmak için bir dilim ekmek veya muz yedirip ardından bol su içirmek, sonra görüntüleme yapmak",
                        "is_correct": False,
                        "scenario_update": "Katı besin verildikten sonra çocuk iki kez öğürdü; olası bir endoskopi için açlık süresi de uzadı.",
                        "teaching_point": "Yeri belirlenmeden katı besin vermek özofagusta takılmayı ağırlaştırabilir ve gerekebilecek endoskopiyi geciktirir."
                    }
                ]
            },
            {
                "stage_title": "Görüntüleme Kararı",
                "question": "Cismin niteliği ve yerini belirlemek için en uygun görüntüleme hangisidir?",
                "options": [
                    {
                        "text": "Radyasyondan kaçınmak için yalnızca batın ultrasonografisi istemek ve cisim görülmezse mideye geçmiş kabul ederek izlem planlamak",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografide gaz nedeniyle cisim görülemedi; özofagus ise hiç değerlendirilemedi.",
                        "teaching_point": "Metal yabancı cisimde ultrasonografi özofagusu göstermez; ilk basamak boyundan anüse direkt grafidir."
                    },
                    {
                        "text": "Yalnızca ayakta direkt batın grafisi çekmek, cisim batında görülmezse dışkıyla çıkacağını varsayarak aileyi bilgilendirmek",
                        "is_correct": False,
                        "scenario_update": "Batın grafisinde cisim görülmedi; boyun ve göğüs alana dahil edilmediği için özofagustaki olası takılma değerlendirilmemiş oldu.",
                        "teaching_point": "Görüntü alanı boyundan anüse uzanmalıdır; özofagus en kritik takılma yeridir."
                    },
                    {
                        "text": "Boyundan anüse kadar ön-arka direkt grafi çekmek, cismin kenar konturunu değerlendirmek ve gerekirse yan grafiyle tamamlamak",
                        "is_correct": True,
                        "explanation": "Tek ön-arka grafi cismin yerini ve konturunu gösterir. Kenarda çift halka veya yan grafide basamak görüntüsü pili düşündürür; düzgün tek kontur madeni parayı destekler.",
                        "new_finding": "Boyun-göğüs-batın ön-arka grafi: Sol üst kadranda, diyafram altında, yaklaşık 23 mm çaplı, tek ve düzgün konturlu, yuvarlak radyoopak cisim. Kenarda çift halka görünümü yok. Boyun ve göğüs bölgesinde yabancı cisim yok. Serbest hava yok."
                    },
                    {
                        "text": "Cismin yerini ve olası mukozal hasarı aynı anda görmek için kontrastsız toraks ve batın bilgisayarlı tomografisi istemek",
                        "is_correct": False,
                        "scenario_update": "Tomografi için çocuk sedasyon ihtiyacıyla birlikte bekletildi; aynı bilgi tek bir direkt grafiyle elde edilebilirdi.",
                        "teaching_point": "Komplikasyon şüphesi olmayan çocukta tomografi gereksiz radyasyon ve sedasyon getirir; ilk tetkik direkt grafidir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Öykü ve görüntüleme bulgularına göre tanınız nedir?",
                "options": [
                    {
                        "text": "Midede düğme pil",
                        "is_correct": False,
                        "scenario_update": "Kenarda çift halka görünümü yoktu ve baba pillerin yerinde olduğunu doğrulamıştı.",
                        "teaching_point": "Düğme pil kenarda halo ve yan grafide basamak görüntüsü verir."
                    },
                    {
                        "text": "Özofagusta takılı madeni para",
                        "is_correct": False,
                        "scenario_update": "Cisim diyafram altında, sol üst kadrandaydı; boyun ve göğüs temizdi.",
                        "teaching_point": "Özofagustaki para çoğunlukla üst darlık düzeyinde, ön-arka grafide tam yüz olarak görülür."
                    },
                    {
                        "text": "Midede asemptomatik madeni para",
                        "is_correct": True,
                        "explanation": "Diyafram altında, sol üst kadranda tek ve düzgün konturlu yuvarlak cisim, yakınması olmayan çocukta mideye geçmiş madeni parayı gösterir.",
                        "new_finding": "Tanı: Asemptomatik gastrik madeni para."
                    },
                    {
                        "text": "Trakeobronşiyal yabancı cisim aspirasyonu",
                        "is_correct": False,
                        "scenario_update": "Solunum sesleri eşitti, hışıltı yoktu ve göğüs grafisinde yabancı cisim görülmedi.",
                        "teaching_point": "Aspirasyonda öksürük krizi sonrası tek taraflı hışıltı ve hava hapsi beklenir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Mideye geçmiş, yakınması olmayan madeni para için en uygun izlem planı hangisidir?",
                "options": [
                    {
                        "text": "Normal beslenmeyle taburcu edip dışkı takibini önermek; karın ağrısı, kusma veya kanama olursa dönmeleri, 2-4 haftada çıkmazsa grafi tekrarlamak",
                        "is_correct": True,
                        "explanation": "Mideye geçmiş asemptomatik madeni para çoğunlukla kendiliğinden atılır. Rutin endoskopi veya laksatif gerekmez; uyarı bulguları ve tekrar grafi zamanı aileye anlatılır.",
                        "new_finding": "Aile bilgilendirildi ve normal beslenmeyle taburcu edildi. Dördüncü gün dışkıda madeni paranın çıktığını telefonla bildirdiler."
                    },
                    {
                        "text": "Cisim midede beklerken mukozal hasar yapabileceği için aynı gün gastroenteroloji ile elektif üst gastrointestinal endoskopi ayarlamak",
                        "is_correct": False,
                        "scenario_update": "Endoskopi için çocuk aç bırakıldı ve genel anestezi aldı; işlem sırasında para zaten duodenuma geçmişti.",
                        "teaching_point": "Mideye geçmiş asemptomatik madeni parada rutin endoskopi gerekmez; endoskopi pil, mıknatıs, sivri cisim veya semptom varlığında düşünülür."
                    },
                    {
                        "text": "Bağırsak geçişini hızlandırmak için birkaç gün laktüloz ya da polietilen glikol başlamak ve günlük dışkıyı elekle kontrol etmelerini istemek",
                        "is_correct": False,
                        "scenario_update": "Laksatif ishale neden oldu ve dışkı takibi zorlaştı; paranın geçişi hızlanmadı.",
                        "teaching_point": "Laksatiflerin madeni para geçişini hızlandırdığına dair kanıt yoktur; normal beslenme yeterlidir."
                    },
                    {
                        "text": "Paranın pilora geçişini görmek için çocuğu 24 saat hastanede gözleme alıp sabah kontrol grafisiyle değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk bir gece gereksiz yere yatırıldı; sabah grafisinde para hâlâ midedeydi ve yönetim değişmedi.",
                        "teaching_point": "Asemptomatik gastrik madeni para için hastanede gözlem veya erken kontrol grafisi gerekmez; ayaktan izlenir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y48",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "2.5 Yaşında",
        "gender": "Erkek",
        "complaint": "İki aydır günde 4-5 kez, içinde sindirilmemiş besin parçaları olan cıvık dışkılama",
        "history": "Annesi anlatıyor: 'Yaklaşık 2 aydır günde 4-5 kez kaka yapıyor. Sabah ilk kakası şekilli, öğleden sonra ve akşama doğru cıvıklaşıyor. İçinde bezelye, havuç, mısır parçaları aynen duruyor. Geceleri uykusunda hiç kaka yapmıyor. Kan veya mukus görmedim. Çok hareketli, iştahlı, neşeli. Kuzeninin çölyak olması bizi çok korkuttu.' Çocuk gün içinde biberonla içecek tüketiyor; ayrıntılı beslenme öyküsü henüz alınmadı.",
        "final_diagnosis": "Kronik Non-spesifik Diyare (Toddler Diyaresi)",
        "disposition": "Yeşil Alandan Beslenme Düzenlemesi (Meyve Suyu Kısıtlaması, Yeterli Yağ ve Lif) ve Güvence ile Taburculuk",
        "case_pearl": "6 ay-5 yaş arasında, büyümesi normal, gündüz olan, gece kesilen, sindirilmemiş sebze parçaları içeren cıvık dışkılama toddler diyaresini düşündürür. Neden çoğunlukla aşırı meyve suyu (fruktoz-sorbitol) ve düşük yağlı diyettir. Tanı büyümenin normal olması ve alarm bulgularının yokluğuna dayanır; meyve suyu kısıtlanır, yağ alımı normalleştirilir, ilaç gerekmez. Büyüme geriliği varsa çölyak ve diğer malabsorpsiyon nedenleri araştırılır.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "İki aydır gündüz cıvık dışkılaması olan, aktif görünen bu 2.5 yaşındaki çocukta değerlendirmenin en kritik bileşeni nedir?",
                "options": [
                    {
                        "text": "Kreş öyküsü nedeniyle paraziter enfeksiyonu öncelikli düşünüp perianal bölgeyi muayene etmek ve ampirik tek doz mebendazol vermek",
                        "is_correct": False,
                        "scenario_update": "Perianal bölge doğaldı; mebendazol sonrası dışkılama paterni değişmedi.",
                        "teaching_point": "Ampirik antiparaziter tedavi ishalin nedenini aydınlatmaz; önce büyüme ve beslenme öyküsü değerlendirilmelidir."
                    },
                    {
                        "text": "Büyüme eğrisini önceki ölçümlerle karşılaştırmak, ayrıntılı 24 saatlik beslenme ve sıvı öyküsü almak, malabsorpsiyon ve kronik hastalık bulgularını muayenede aramak",
                        "is_correct": True,
                        "explanation": "Kronik ishalde büyüme hızının korunup korunmadığı organik ve fonksiyonel nedenleri ayıran en önemli bulgudur. Ayrıntılı beslenme öyküsü fonksiyonel ishalin nedenini sıklıkla ortaya koyar.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 96/dk, TA 92/56 mmHg. Tartı 13.5 kg (50. p), boy 92 cm (50. p); son 1 yılda persentil kaybı yok. Canlı, hareketli. Karın yumuşak, distansiyon yok, organomegali yok. Ödem, solukluk, dermatit, çomak parmak yok. Perianal bölge doğal. Beslenme öyküsü: günde 4-5 biberon (yaklaşık 1 litre) hazır elma suyu, yağsız süt, az yağlı yemekler."
                    },
                    {
                        "text": "Dışkıda besin parçaları görülmesini pankreas yetersizliği bulgusu kabul ederek solunum sistemi muayenesine ve ter testi planlamasına odaklanmak",
                        "is_correct": False,
                        "scenario_update": "Akciğer muayenesi normaldi. Ter testi için randevu alındı; büyüme ve beslenme öyküsü değerlendirilmedi.",
                        "teaching_point": "Sindirilmemiş sebze parçaları küçük çocukta hızlı geçişe bağlı olabilir; normal büyüyen çocukta pankreas yetersizliği düşük olasılıktır."
                    },
                    {
                        "text": "Kronik ishal nedeniyle hidrasyon bulgularını değerlendirip karın palpasyonu yapmak ve kuzenindeki tanıyı göz önüne alarak muayene sonrası çölyak serolojisini hemen istemek",
                        "is_correct": False,
                        "scenario_update": "Hidrasyon normal bulundu; çölyak serolojisi gönderildi. Büyüme eğrisi ve beslenme öyküsü değerlendirilmediği için tablonun nedeni ortaya çıkmadı.",
                        "teaching_point": "Kronik ishalde tetkik kararı büyüme eğrisi ve ayrıntılı beslenme öyküsüyle verilir; aile öyküsü tek başına serolojiyi zorunlu kılmaz."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Büyümesi normal, alarm bulgusu olmayan ve günde yaklaşık 1 litre meyve suyu içen bu çocukta tetkik yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Kuzende çölyak bulunduğu için doku transglutaminaz IgA ile birlikte tam kan sayımı, ferritin, albümin ve dışkı elastaz düzeyini istemek, sonuçlara göre diyet planlamak",
                        "is_correct": False,
                        "scenario_update": "Tüm sonuçlar normal geldi; aile sonuç beklerken yoğun kaygı yaşadı ve diyet önerisi ertelendi.",
                        "teaching_point": "İkinci derece akrabada çölyak tek başına tarama endikasyonu değildir; büyümesi normal, alarm bulgusu olmayan çocukta önce diyet düzenlemesi yapılır."
                    },
                    {
                        "text": "Dışkıda gizli kan, kalprotektin, parazit incelemesi ve dışkı kültürü isteyip sonuçlar normalse iki hafta sonra diyet değişikliği önermek",
                        "is_correct": False,
                        "scenario_update": "Kalprotektin sınırda yüksek geldi ve tekrar ölçüm planlandı; bu süre içinde meyve suyu tüketimi devam etti.",
                        "teaching_point": "Küçük çocuklarda kalprotektin normal değerleri daha yüksektir ve gereksiz tetkik zinciri başlatabilir; tetkik klinik şüpheye göre istenmelidir."
                    },
                    {
                        "text": "İshal kronikleştiği için çocuğu gastroenteroloji polikliniğine sevk etmek ve endoskopi değerlendirmesi yapılana kadar glutensiz diyet başlatmak",
                        "is_correct": False,
                        "scenario_update": "Glutensiz diyet sonrası dışkılama değişmedi; diyetle birlikte olası bir serolojik tanı da değerlendirilemez hale geldi.",
                        "teaching_point": "Tanı konmadan glutensiz diyet başlanmamalıdır; bu hem gereksiz kısıtlamaya hem de olası tanının maskelenmesine yol açar."
                    },
                    {
                        "text": "Tetkik istemeden meyve suyu tüketimini kısıtlayıp yağ ve lif alımını düzenleyen bir deneme yapmak, iki hafta sonra dışkılama günlüğüyle kontrol etmek",
                        "is_correct": True,
                        "explanation": "Büyümesi normal, gece dışkılaması, kan ve kilo kaybı olmayan çocukta aşırı meyve suyu ve düşük yağ alımı fonksiyonel ishali açıklar. Tetkik yerine diyet denemesi hem tanısal hem tedavidir.",
                        "new_finding": "Laboratuvar tetkiki istenmedi. Aile ile birlikte iki haftalık beslenme planı ve dışkılama günlüğü hazırlandı."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Normal büyüyen, gündüz cıvık, gece dışkılaması olmayan, sebze parçaları içeren dışkılaması ve yüksek meyve suyu tüketimi olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Çölyak hastalığı",
                        "is_correct": False,
                        "scenario_update": "Büyüme eğrisi korunmuş, distansiyon, anemi ve hipoalbüminemi bulgusu yok.",
                        "teaching_point": "Malabsorpsiyon tablosunda büyüme hızında yavaşlama beklenir."
                    },
                    {
                        "text": "Postenfeksiyöz laktoz intoleransı",
                        "is_correct": False,
                        "scenario_update": "Öncesinde akut gastroenterit öyküsü yok; dışkılama süt alımıyla değil meyve suyu ile ilişkili.",
                        "teaching_point": "Sekonder laktoz intoleransı genellikle akut enfeksiyon sonrası gelişir ve şişkinlik, asidik dışkı eşlik eder."
                    },
                    {
                        "text": "İnflamatuvar bağırsak hastalığı",
                        "is_correct": False,
                        "scenario_update": "Kanlı dışkı, gece dışkılaması, kilo kaybı ve perianal hastalık yok.",
                        "teaching_point": "İnflamatuvar hastalıkta alarm bulguları ve büyüme etkilenmesi beklenir."
                    },
                    {
                        "text": "Kronik non-spesifik (toddler) diyare",
                        "is_correct": True,
                        "explanation": "6 ay-5 yaş arası, büyümesi normal, gündüz cıvık, gece dışkılaması olmayan çocukta aşırı fruktoz-sorbitol içeren meyve suyu ve düşük yağ alımı toddler diyaresine neden olur.",
                        "new_finding": "Tanı: Kronik Non-spesifik Diyare (Toddler Diyaresi)."
                    }
                ]
            },
            {
                "stage_title": "Diyet Düzenlemesi ve Aile Rehberliği",
                "question": "Bu çocuğun ailesine verilecek en uygun öneri hangisidir?",
                "options": [
                    {
                        "text": "Dışkı sıklığını azaltmak için birkaç gün düşük doz loperamid vermek ve aynı süre içinde meyve suyu tüketimini yarıya indirmesini önermek",
                        "is_correct": False,
                        "scenario_update": "Loperamid sonrası çocukta karın şişliği ve uykuya meyil gelişti; aile ilacı kesip acile başvurdu.",
                        "teaching_point": "Küçük çocuklarda loperamid ileus ve santral sinir sistemi yan etkileri nedeniyle önerilmez."
                    },
                    {
                        "text": "Meyve suyunu sulandırarak sürdürmek, posalı gıdaları ve sebzeleri tamamen kesmek ve bağırsağı dinlendirmek için bir hafta pirinç lapası ağırlıklı beslemek",
                        "is_correct": False,
                        "scenario_update": "Kısıtlı diyetle dışkılama azalmadı, çocuk iştahsızlaştı ve kilo almadı.",
                        "teaching_point": "Lif kısıtlaması ve kısıtlayıcı diyetler önerilmez; asıl hedef fruktoz-sorbitol yükünü azaltmak ve yeterli yağ alımını sağlamaktır."
                    },
                    {
                        "text": "Meyve suyunu kesip su vermek, tam yağlı süt ve yemeklere yağ eklemek, lifi sürdürmek ve aileye güvence vermek",
                        "is_correct": True,
                        "explanation": "Meyve suyunun kısıtlanması ozmotik yükü azaltır; yeterli yağ alımı gastrik boşalmayı ve bağırsak geçişini yavaşlatır. Lif normal düzeyde sürdürülür. Tablonun büyümeyi etkilemediği konusunda aileye güvence verilir.",
                        "new_finding": "İki hafta sonraki kontrolde meyve suyu kesilmişti; dışkılama sayısı günde 1-2'ye indi, dışkı şekilli hale geldi. Çocuk kilosunu korudu."
                    },
                    {
                        "text": "Dışkı sıklığını azaltmak için bir hafta probiyotik ve günlük çinko desteği başlamak, mevcut beslenme düzenini değiştirmeden kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "İki hafta sonra dışkılama paterni aynıydı; meyve suyu tüketimi sürüyordu.",
                        "teaching_point": "Toddler diyaresinde ilaç veya takviyenin yeri yoktur; tedavi diyetin düzenlenmesidir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y49",
        "category": "👶 Yenidoğan Acilleri",
        "age": "3 Haftalık",
        "gender": "Kız",
        "complaint": "Doğumdan sonraki ilk hafta başlayan ve hâlâ geçmeyen ciltte ve göz akında sararma",
        "history": "Annesi anlatıyor: 'Doğumdan sonra 3. gün sarardı, çok yüksek değil denildi ve ışık tedavisi almadı. Üç haftadır sarılık geçmedi, yüzü ve göğsü hâlâ sarı.' 39. haftada normal doğum, doğum ağırlığı 3200 g. Yalnız anne sütü alıyor, günde 9-10 kez emiyor, günde 6-7 bez ıslatıyor. Dışkısı sarı ve hardal kıvamında, idrarı açık renkli. Uykusu ve emmesi iyi. Anne ve bebeğin kan grubu aynı. Yenidoğan tarama testlerinin sonuçları normal bildirilmiş.",
        "final_diagnosis": "Anne Sütü Sarılığı (Uzamış İndirekt Hiperbilirubinemi)",
        "disposition": "Emzirmeye Devam Edilerek Aile Hekimi ve Bilirubin Takibiyle Yeşil Alandan Taburculuk",
        "case_pearl": "Term bebekte 14 günü aşan sarılık 'uzamış sarılık' olarak değerlendirilir ve her bebekte direkt (konjuge) bilirubin bakılmalıdır. Direkt bilirubin >1 mg/dL veya totalin %20'sinden fazlaysa kolestaz vardır ve biliyer atrezi için acil ileri tetkik gerekir. Akolik dışkı ve koyu idrar sorgulanır. İyi kilo alan, dışkısı renkli, indirekt hiperbilirubinemili bebekte anne sütü sarılığı en sık nedendir. Emzirme kesilmez.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Üç haftalık, yalnız anne sütü alan ve hâlâ sarı olan bu bebeğin değerlendirmesinde öncelikli olarak ne yaparsınız?",
                "options": [
                    {
                        "text": "Sarılığın göğüs hizasında kaldığını görerek bunun beklenen bir süreç olduğunu söyleyip herhangi bir değerlendirme yapmadan aileyi rahatlatmak",
                        "is_correct": False,
                        "scenario_update": "Bebek muayene edilmeden gönderildi; dışkı rengi, kilo alımı ve bilirubin fraksiyonu hiç değerlendirilmedi.",
                        "teaching_point": "İki haftayı aşan sarılık her zaman değerlendirilmelidir; kolestaz atlanırsa biliyer atrezide ameliyat şansı kaybedilebilir."
                    },
                    {
                        "text": "Sarılık uzadığı için emzirmeyi hemen kesip mama başlatmak ve 48 saat sonra sararmanın azalıp azalmadığını görmek üzere kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Anne emzirmeyi bıraktı, süt üretimi azaldı; bebek mamayı istemedi ve tetkik yapılmadığı için neden belirsiz kaldı.",
                        "teaching_point": "Emzirmeyi rutin olarak kesmek önerilmez; önce uzamış sarılığın nedeni araştırılmalıdır."
                    },
                    {
                        "text": "Büyüme eğrisi, beslenme, dışkı ve idrar rengini sorgulayıp genel durumu, hepatosplenomegaliyi ve sarılığın yaygınlığını muayenede değerlendirmek",
                        "is_correct": True,
                        "explanation": "Uzamış sarılıkta kilo alımı, dışkının renkli olup olmadığı, idrar rengi ve organomegali kolestatik ve hemolitik nedenleri ayırmada ilk ipuçlarıdır.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 142/dk, SS 40/dk, SpO2 %99. Tartı 4150 g (doğum ağırlığının üzerinde, günlük ortalama 45 g artış). Yüz, göğüs ve karın üst kısmında sarılık, sklera ikterik. Karaciğer kosta kenarında, dalak ele gelmiyor. Bezdeki dışkı sarı-hardal renginde, idrar açık sarı. Emme refleksi ve tonus normal."
                    },
                    {
                        "text": "Sarılık derin görünmese de bebeği hemen yenidoğan servisine yatırıp tetkik sonuçları gelmeden yoğun fototerapi başlatmak",
                        "is_correct": False,
                        "scenario_update": "Bebek anneden ayrıldı ve fototerapiye alındı; sonradan bilirubin değerinin tedavi eşiğinin çok altında olduğu görüldü.",
                        "teaching_point": "Fototerapi kararı ölçülen bilirubin, saat-yaş ve risk faktörlerine göre verilir; uzamış sarılıkta önce fraksiyon bakılır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "İyi kilo alan, dışkısı renkli bu bebekte hangi tetkikler uygun olur?",
                "options": [
                    {
                        "text": "Total ve direkt bilirubin, tam kan sayımı ile retikülosit, tam idrar ve tiroid fonksiyonunu istemek, yenidoğan tarama sonuçlarını teyit etmek",
                        "is_correct": True,
                        "explanation": "Uzamış sarılıkta kolestazı dışlamak için direkt bilirubin şarttır. Hemoliz, idrar yolu enfeksiyonu ve hipotiroidi de basit tetkiklerle dışlanır.",
                        "new_finding": "Total bilirubin 13.8 mg/dL, direkt bilirubin 0.5 mg/dL. Hb 14.6 g/dL, retikülosit %1.2, periferik yaymada hemoliz bulgusu yok. Tam idrar normal. TSH 3.1 mIU/L, serbest T4 normal."
                    },
                    {
                        "text": "Yalnızca transkutan bilirubin ölçmek ve değer fototerapi eşiğinin altındaysa başka bir tetkik yapmadan iki hafta sonraya kontrol vermek",
                        "is_correct": False,
                        "scenario_update": "Transkutan değer 13 mg/dL çıktı; ancak direkt fraksiyon bilinmediği için kolestaz dışlanamadı.",
                        "teaching_point": "Transkutan ölçüm fraksiyon ayırmaz; uzamış sarılıkta serumda direkt bilirubin mutlaka bakılmalıdır."
                    },
                    {
                        "text": "Kolestaz şüphesiyle tetkik beklemeden hepatobiliyer sintigrafi ve batın ultrasonografisi isteyip çocuk gastroenterolojiye acil sevk planlamak",
                        "is_correct": False,
                        "scenario_update": "Sintigrafi için randevu verildi; sonradan direkt bilirubinin normal olduğu ve tetkikin gereksiz olduğu anlaşıldı.",
                        "teaching_point": "İleri görüntüleme yalnızca direkt hiperbilirubinemi saptandığında gerekir; ilk adım serum fraksiyonlarıdır."
                    },
                    {
                        "text": "Enfeksiyon olasılığı nedeniyle tam kan sayımı, CRP, kan kültürü ve lomber ponksiyon yapıp sonuçlar çıkana kadar ampirik antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "İyi görünen ve kilo alan bebek invaziv girişimler ve antibiyotikle hastanede tutuldu; kültürler negatif geldi.",
                        "teaching_point": "Genel durumu iyi, ateşsiz ve kilo alan bebekte uzamış sarılık tek başına sepsis taraması gerektirmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik ve laboratuvar bulgularına göre en olası tanınız nedir?",
                "options": [
                    {
                        "text": "Biliyer atrezi (erken dönem)",
                        "is_correct": False,
                        "scenario_update": "Direkt bilirubin normaldi, dışkı renkliydi ve karaciğer büyük değildi.",
                        "teaching_point": "Biliyer atrezide direkt hiperbilirubinemi, akolik dışkı ve koyu idrar olur."
                    },
                    {
                        "text": "Konjenital hipotiroidiye bağlı uzamış sarılık",
                        "is_correct": False,
                        "scenario_update": "TSH ve serbest T4 normaldi, kabızlık, makroglossi veya letarji yoktu.",
                        "teaching_point": "Hipotiroidide kabızlık, hipotoni, geniş fontanel ve yüksek TSH beklenir."
                    },
                    {
                        "text": "Hemolitik hastalığa bağlı hiperbilirubinemi",
                        "is_correct": False,
                        "scenario_update": "Hb ve retikülosit normaldi, kan grubu uyuşmazlığı ve yaymada hemoliz yoktu.",
                        "teaching_point": "Hemolizde düşen hemoglobin, artmış retikülosit ve yaymada sferosit veya fragmente eritrosit görülür."
                    },
                    {
                        "text": "Anne sütü sarılığı",
                        "is_correct": True,
                        "explanation": "İyi kilo alan, renkli dışkılı, yalnız anne sütüyle beslenen ve indirekt hiperbilirubinemisi olan bebekte diğer nedenler dışlandığında en olası tanıdır.",
                        "new_finding": "Tanı: Anne sütü sarılığı."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu bebek için en uygun yönetim planı hangisidir?",
                "options": [
                    {
                        "text": "Emzirmeye 48 saat ara verip mama ile beslemek ve bilirubin düşüşü görülürse tanıyı kesinleştirmiş olarak emzirmeye geri dönmek",
                        "is_correct": False,
                        "scenario_update": "Emzirme ara verilince anne sütü azaldı; bebek huzursuzlandı ve anne kendini suçlu hissetti.",
                        "teaching_point": "Tanısal amaçlı emzirmeye ara vermek rutin önerilmez; emzirmeyi sürdürmek ve izlemek yeterlidir."
                    },
                    {
                        "text": "Bilirubini hızlı düşürmek için evde güneş ışığında tutmayı ve öğün aralarında şekerli su ya da bitki çayı vermeyi önermek",
                        "is_correct": False,
                        "scenario_update": "Bebeğe ek sıvılar verildi; emme sayısı azaldı ve kilo alımı yavaşladı.",
                        "teaching_point": "Su, şekerli su ve bitki çayı bilirubini düşürmez, emzirmeyi azaltır; güneş ışığı güvenli bir tedavi yöntemi değildir."
                    },
                    {
                        "text": "Emzirmeye devam etmeyi önermek, dışkı rengi kartını vermek ve aile hekimiyle 1-2 hafta sonra bilirubin izlemi planlayarak taburcu etmek",
                        "is_correct": True,
                        "explanation": "Anne sütü sarılığı zararsızdır ve haftalar içinde kendiliğinden geriler. Emzirme sürdürülür, akolik dışkı veya koyu idrar fark edilirse hemen başvurmaları söylenir.",
                        "new_finding": "Aileye dışkı renk kartı verildi, emzirmenin sürdürülmesi önerildi. İki hafta sonraki kontrolde total bilirubin 8.4 mg/dL'ye geriledi, tartı 4850 g."
                    },
                    {
                        "text": "Bilirubin metabolizmasını hızlandırmak için iki hafta ursodeoksikolik asit başlamak ve tedavi sonunda yeniden bilirubin ölçümü yapmak",
                        "is_correct": False,
                        "scenario_update": "İlaç gereksiz yere başlandı; indirekt hiperbilirubinemide etkisi olmadığından seyir değişmedi.",
                        "teaching_point": "Ursodeoksikolik asit kolestatik hastalıklarda kullanılır; indirekt hiperbilirubinemide yeri yoktur."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y50",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "8 Yaşında",
        "gender": "Kız",
        "complaint": "Ateş için sık ibuprofen kullanımı sonrası başlayan mide yanması ve bir kez koyu renkli kusma",
        "history": "Annesi anlatıyor: 'Üç gündür grip nedeniyle ateşi vardı; ateş düşmediği için günde 4-5 kez, çoğu zaman aç karnına ibuprofen şurup verdim. Dün gece mide kazınması ve yanma başladı. Bu sabah bir kez az miktarda kahve telvesi gibi koyu renkli kustu. Kakası siyah değil. Baş dönmesi veya bayılması olmadı.' Ateşi bugün yok. Daha önce mide şikayeti yok. Kullanılan şurup 100 mg/5 mL; dozları ölçü kaşığıyla değil çay kaşığıyla vermiş. Tartı: 26 kg.",
        "final_diagnosis": "NSAİİ (İbuprofen) İlişkili Akut Hemorajik Gastrit",
        "disposition": "Yeşil Alandan NSAİİ Kesilmesi, Oral Proton Pompa İnhibitörü ve Kırmızı Bayrak Eğitimi ile Taburculuk",
        "case_pearl": "Aç karnına ve sık aralıklarla kullanılan NSAİİ çocukta da mukozal hasara ve üst gastrointestinal kanamaya yol açabilir. Hemodinamisi stabil, hemoglobini normal, melenası olmayan ve kanaması kendiliğinden durmuş çocukta ilacın kesilmesi ve oral PPI (omeprazol yaklaşık 1 mg/kg/gün) yeterlidir; acil endoskopi gerekmez. Tekrarlayan kanama, melena, taşikardi veya Hb düşüşünde yatış ve endoskopi planlanır. Ailenin doz ölçümü ve dozlar arası süre konusunda eğitimi önemlidir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Bir kez koyu renkli kusan, mide yanması tarif eden bu çocukta ilk değerlendirmede önceliğiniz nedir?",
                "options": [
                    {
                        "text": "Ortostatik nabız ve tansiyon dahil hemodinamiyi, kapiller dolumu, konjonktiva solukluğunu değerlendirmek, karın muayenesi yapıp perianal inspeksiyonla dışkı rengini kontrol etmek",
                        "is_correct": True,
                        "explanation": "Üst gastrointestinal kanama şüphesinde ilk öncelik hemodinamik stabilitenin değerlendirilmesidir. Ortostatik değişiklikler, solukluk ve melena kanamanın boyutunu gösterir; karın muayenesi perforasyon bulgularını dışlar.",
                        "new_finding": "Vital Bulgular: Ateş 37.0°C, KTA 94/dk (ayağa kalkınca 100/dk), SS 20/dk, TA 104/66 mmHg, KDZ 1.5 sn. Genel durumu iyi, konjonktivalar pembe. Karın yumuşak, epigastriumda orta hassasiyet; defans ve rebound yok. Perianal inspeksiyonda bezde normal kahverengi dışkı, melena yok. Ağız ve burunda kanama odağı yok."
                    },
                    {
                        "text": "Kahve telvesi kusmanın kaynağını doğrulamak için nazogastrik sonda takıp serum fizyolojik ile lavaj yapmak, aspirat temizlenince vital bulgu ve karın muayenesini tamamlamak",
                        "is_correct": False,
                        "scenario_update": "Lavaj sıvısı berrak geldi; çocuk işlem sırasında çok ağladı ve öğürdü. Hemodinami değerlendirmesi gecikti.",
                        "teaching_point": "Stabil çocukta nazogastrik lavaj tanısal ya da tedavi edici değildir; ilk adım hemodinamik değerlendirmedir."
                    },
                    {
                        "text": "Kusmanın burun kanamasından yutulan kan olabileceğini düşünüp ağırlıklı olarak kulak-burun-boğaz muayenesi yapmak ve ardından taburculuğu değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Burunda kanama odağı saptanmadı. Hemodinami ve karın muayenesi sistematik yapılmadığı için kanamanın kaynağı ve boyutu belirsiz kaldı.",
                        "teaching_point": "Yutulan kan ayırıcı tanıda düşünülmelidir ancak hemodinamik ve karın muayenesinin yerini almaz."
                    },
                    {
                        "text": "Epigastrik ağrı nedeniyle muayene öncesinde intravenöz parasetamol ve ondansetron yapmak, ağrı geçince karın muayenesini ve vital bulguları değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "İlaçlar sonrası çocuk rahatladı; ancak ilk vital bulgular ve ortostatik değerlendirme yapılmadan zaman geçti.",
                        "teaching_point": "Kanama şüphesinde semptomatik tedavi öncesinde hemodinami ve muayene kaydedilmelidir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Stratejisi",
                "question": "Hemodinamisi stabil, melenası olmayan, bir kez az miktarda koyu kusan bu çocukta tetkik yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Helicobacter pylori enfeksiyonunu dışlamak için dışkı antijen testi istemek ve sonuç pozitif gelirse eradikasyon tedavisi planlamak",
                        "is_correct": False,
                        "scenario_update": "Test sonucu iki gün sonra negatif geldi; acil yönetim açısından bilgi sağlamadı.",
                        "teaching_point": "Akut kanamada dışkı antijen testi ve eradikasyon planı ilk basamak değildir; ayrıca yakın dönem PPI kullanımı yanlış negatifliğe yol açabilir."
                    },
                    {
                        "text": "Ateş öyküsü nedeniyle tam kan sayımı, CRP, kan kültürü ve batın ultrasonografisi isteyip kanamanın enfeksiyonla ilişkisini araştırmak",
                        "is_correct": False,
                        "scenario_update": "CRP hafif yüksek, kültür negatif ve ultrasonografi normal geldi; sonuçlar kanamanın nedenini açıklamadı.",
                        "teaching_point": "Tetkikler klinik soruya yönelik olmalıdır; kanamanın en olası nedeni ilaç öyküsünde saklıdır."
                    },
                    {
                        "text": "Tam kan sayımı ve dışkıda gizli kan istemek, hemoglobin normal ve kusma tekrarlamıyorsa ek tetkik planlamadan ilaç öyküsünü ayrıntılı netleştirmek",
                        "is_correct": True,
                        "explanation": "Stabil hastada başlangıç hemoglobini kanamanın boyutunu ve izlem gereksinimini belirler. Ayrıntılı ilaç öyküsü (doz, sıklık, aç karnına kullanım) mukozal hasarın nedenini ortaya koyar.",
                        "new_finding": "Hb 12.4 g/dL, Hct %37, trombosit 280.000/mm³, MCV normal. Dışkıda gizli kan pozitif. İlaç öyküsünde günde 4-5 kez, her seferinde yaklaşık 10-12 mg/kg ibuprofen verildiği, dozlar arasında 4 saatten kısa aralıklar olduğu ve çoğunun aç karnına olduğu belirlendi."
                    },
                    {
                        "text": "Tam kan sayımı, kan grubu ve koagülasyon testleri istemek ve bilinmeyen kaynaklı kanama nedeniyle aynı gün çocuk gastroenterolojisinden acil endoskopi talep etmek",
                        "is_correct": False,
                        "scenario_update": "Hemoglobin normal geldi; gastroenterolog stabil hastada acil endoskopi gerekmediğini belirtti ve çocuk saatlerce aç bekletildi.",
                        "teaching_point": "Stabil, kanaması durmuş ve açık bir tetikleyicisi olan çocukta acil endoskopi endike değildir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Aç karnına sık NSAİİ kullanımı sonrası epigastrik yanma, kahve telvesi kusma, stabil hemodinami ve normal hemoglobin varlığında en olası tanı nedir?",
                "options": [
                    {
                        "text": "Mallory-Weiss yırtığı",
                        "is_correct": False,
                        "scenario_update": "Kanamadan önce tekrarlayan şiddetli öğürme veya kusma öyküsü yok.",
                        "teaching_point": "Mallory-Weiss yırtığında hematemez tekrarlayan kusmaların ardından gelişir."
                    },
                    {
                        "text": "NSAİİ ilişkili akut hemorajik gastrit",
                        "is_correct": True,
                        "explanation": "Sık ve aç karnına ibuprofen kullanımı prostaglandin aracılı mukozal korumayı bozarak erozif-hemorajik gastrite yol açar; az miktarda hematemez ve epigastrik yanma tipik bulgulardır.",
                        "new_finding": "Tanı: NSAİİ (İbuprofen) İlişkili Akut Hemorajik Gastrit."
                    },
                    {
                        "text": "Akut kolesistit",
                        "is_correct": False,
                        "scenario_update": "Sağ üst kadran hassasiyeti, Murphy bulgusu ve sarılık yok; hematemez kolesistit bulgusu değildir.",
                        "teaching_point": "Epigastrik yanma ve hematemez mide-duodenum kaynaklı patolojiyi düşündürür."
                    },
                    {
                        "text": "Özofageal varis kanaması",
                        "is_correct": False,
                        "scenario_update": "Kronik karaciğer hastalığı, splenomegali veya portal hipertansiyon bulgusu yok.",
                        "teaching_point": "Varis kanaması genellikle masif ve hemodinamik etkilenmeyle seyreder."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Hemoglobini normal ve stabil olan bu 26 kg'lık çocuğun tedavi planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "İbuprofen dozunu azaltıp parasetamol ile dönüşümlü vermeyi sürdürmek, mide koruması için her dozdan önce antasit süspansiyonu kullanmasını ve ilacı tok karnına vermesini önermek",
                        "is_correct": False,
                        "scenario_update": "İbuprofen sürdürülünce iki gün sonra epigastrik ağrı arttı ve çocuk tekrar koyu renkli kustu.",
                        "teaching_point": "Mukozal kanama gelişen çocukta NSAİİ kesilmelidir; antasit tek başına yeterli koruma sağlamaz."
                    },
                    {
                        "text": "İbuprofeni kesmek, yaklaşık 1 mg/kg/gün oral omeprazol başlamak, ateş için parasetamol önermek ve melena veya kan kusmada dönüşü anlatmak",
                        "is_correct": True,
                        "explanation": "Tedavinin temeli suçlu ilacın kesilmesi ve mukozal iyileşmeyi sağlayan asit baskılamadır. Ateş için doğru dozda parasetamol kullanımı ve kırmızı bayraklar ayrıntılı anlatılır; 2-4 hafta PPI genellikle yeterlidir.",
                        "new_finding": "Omeprazol 20 mg/gün başlandı, aileye parasetamol doz tablosu ve ölçü kaşığı kullanımı gösterildi. 48 saat sonraki kontrolde mide yanması gerilemişti, kusma tekrarlamadı, dışkı rengi normaldi."
                    },
                    {
                        "text": "Yatırarak intravenöz pantoprazol infüzyonu başlamak, 24 saat oral alımı kapatmak ve ertesi gün kontrol hemoglobini ile endoskopi planlamak",
                        "is_correct": False,
                        "scenario_update": "Stabil çocuk gereksiz yere yatırıldı ve aç bırakıldı; kontrol hemoglobini değişmedi, endoskopi iptal edildi.",
                        "teaching_point": "Hemodinamisi stabil, Hb'si normal ve kanaması durmuş çocukta yatış, intravenöz PPI ve acil endoskopi gerekmez."
                    },
                    {
                        "text": "İbuprofeni kesip yalnızca sukralfat süspansiyonu başlamak, beslenmeyi sulu gıdalarla sınırlamak ve bir hafta sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Sukralfat sonrası çocuk kabızlık geliştirdi; yanma yakınması yavaş geriledi.",
                        "teaching_point": "Asit baskılama ilk seçenektir; sukralfat ikinci basamak bir mukozal koruyucudur ve kısıtlayıcı diyet gerekmez."
                    }
                ]
            }
        ]
    }
]
