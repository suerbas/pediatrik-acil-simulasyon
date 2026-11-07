# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - Y81-Y85 (Deri ve Yumuşak Doku)
"""

SPOILERS = {
    "Y81": ["atopik dermatit", "egzama", "ekzema"],
    "Y82": ["skabiyez", "uyuz", "sarcoptes", "permetrin"],
    "Y83": ["büyük lokal reaksiyon", "skeeter"],
    "Y84": ["selülit", "erizipel"],
    "Y85": ["paronişi", "dolama"],
}

CASES = [
    {
        "id": "Y81",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "3 Yaşında",
        "gender": "Kız",
        "complaint": "Kollarında, dizlerinin arkasında ve boynunda kaşıntılı, pullu kızarıklıklar; geceleri kaşınmaktan uyuyamama",
        "history": "Annesi anlatıyor: 'Bebekliğinden beri yanaklarında ara ara kuruluk oluyordu. Bu kış çok arttı, dirsek ve diz içleri kıpkırmızı, geceleri kanatana kadar kaşıyor. Her gün köpüklü banyo yaptırıyorum, kremi seyrek sürüyorum. Kortizonlu krem verilmişti ama zararlı diye kullanmadım.' Ateş, sulu yara, içi su dolu kabarcık yok. Ailede babada astım ve saman nezlesi var. Komşu 'süt ve yumurtayı kesin' demiş.",
        "final_diagnosis": "Atopik Dermatit Alevlenmesi (Orta Şiddet, Enfeksiyonsuz)",
        "disposition": "Nemlendirici, Topikal Kortikosteroid ve Cilt Bakım Eğitimiyle Yeşil Alandan Taburculuk",
        "case_pearl": "Atopik dermatit tanısı kliniktir. Kaşıntı, yaşa özgü dağılım (küçük çocukta yüz ve ekstansör yüzler, büyüklerde fleksural bölgeler), kronik-tekrarlayıcı seyir ve atopi öyküsü aranır. Rutin besin alerji testleri ve eliminasyon diyeti önerilmez. Tedavinin temeli bol nemlendiricidir. Alevlenmede gövdede orta potensli, yüzde düşük potensli topikal kortikosteroid günde bir kez 1-2 hafta, ardından haftada iki gün koruyucu kullanılır. Sarı kabuklanma, delinmiş görünümlü erozyonlar veya ateş enfeksiyonu düşündürür.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Kaşıntılı kızarıklıklarla gelen bu çocukta muayenede nelere dikkat edersiniz?",
                "options": [
                    {
                        "text": "Lezyonların dağılımını, yaygınlığını ve kaşıntının uykuya etkisini değerlendirip sarı kabuk, delinmiş erozyon, vezikül ve ateş gibi enfeksiyon bulgularını aramak",
                        "is_correct": True,
                        "explanation": "Dağılım ve yaygınlık şiddeti belirler. Bakteriyel veya viral süperenfeksiyon tedaviyi tamamen değiştirdiği için mutlaka aranmalıdır.",
                        "new_finding": "Vital Bulgular: Ateş 36.7°C, genel durum iyi. Dirsek ve diz fleksural yüzlerinde, boyun önünde ve el bileklerinde sınırları belirsiz, eritemli, kepeklenen, yer yer likenifiye plaklar ve kaşıntı izleri. Yüzde hafif kuruluk. Vücut yüzeyinin yaklaşık %15'i tutulmuş. Sarı kabuk, delinmiş görünümlü erozyon veya vezikül yok. Parmak araları ve el ayasında lezyon yok. Lenf nodları küçük."
                    },
                    {
                        "text": "Kızarıklıkları besin alerjisine bağlayıp muayeneyi kısa tutmak ve aileye süt ile yumurtayı hemen diyetten çıkarmalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Aile süt ve yumurtayı kesti; lezyonlar değişmedi, çocuğun kalsiyum alımı azaldı.",
                        "teaching_point": "Kanıtlanmış bir besin alerjisi olmadan eliminasyon diyeti önerilmez; beslenme eksikliği riski taşır."
                    },
                    {
                        "text": "Kaşıntılı papüller nedeniyle tüm ailede kaşıntı olup olmadığını sormadan bulaşıcı bir parazit enfeksiyonu kabul edip tüm aileyi tedavi etmek",
                        "is_correct": False,
                        "scenario_update": "Ailedeki kimsede kaşıntı yoktu; uygulanan tedavi cildi daha da tahriş etti.",
                        "teaching_point": "Dağılım, parmak arası tutulumu ve ailede kaşıntı sorgulanmadan bu tanıya gidilmemelidir."
                    },
                    {
                        "text": "Lezyonların mantar olabileceğini düşünüp muayene sırasında yalnızca en belirgin plağa bakarak topikal antifungal krem önermek",
                        "is_correct": False,
                        "scenario_update": "Antifungal krem kaşıntıyı azaltmadı; plaklar yaygınlaşmaya devam etti.",
                        "teaching_point": "Simetrik fleksural tutulum ve kronik seyir mantar enfeksiyonundan farklıdır; tüm deri muayene edilmelidir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Enfeksiyon bulgusu olmayan bu çocukta hangi tetkik yaklaşımı uygundur?",
                "options": [
                    {
                        "text": "Besin alerjenlerine karşı spesifik IgE paneli istemek ve pozitif çıkan tüm besinleri diyetten çıkarmak üzere aileyi bilgilendirmek",
                        "is_correct": False,
                        "scenario_update": "Panelde süt ve yumurtaya düşük düzeyde IgE pozitifliği çıktı; klinik reaksiyon olmamasına rağmen besinler kesildi.",
                        "teaching_point": "Duyarlılık klinik alerji demek değildir; rutin IgE paneli gereksiz diyet kısıtlamalarına yol açar."
                    },
                    {
                        "text": "Tüm lezyonlardan bakteri kültürü almak ve kültürde üreme olursa oral antibiyotik başlamak üzere kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Kültürde S. aureus üredi; enfeksiyon bulgusu olmayan çocukta gereksiz antibiyotik başlandı.",
                        "teaching_point": "Bu cilt S. aureus ile sık kolonizedir; klinik enfeksiyon yoksa kültür ve antibiyotik gerekmez."
                    },
                    {
                        "text": "Tanının klinik olduğunu kabul edip tetkik istememek, şiddet ve tetikleyicileri belirleyerek tedavi planına geçmek",
                        "is_correct": True,
                        "explanation": "Tanı öykü ve muayeneyle konur. Tetkik ancak tedaviye dirençli, atipik veya besinle açık ilişki gösteren olgularda düşünülür.",
                        "new_finding": "Tetkik istenmedi. Tetikleyiciler: sık köpüklü banyo, yetersiz nemlendirici kullanımı, kışın kuru ortam ve yünlü giysiler."
                    },
                    {
                        "text": "Tam kan sayımı, eozinofil sayısı ve total IgE istemek; değerler yüksekse sistemik antihistaminik ve oral steroid başlamak",
                        "is_correct": False,
                        "scenario_update": "Eozinofil ve total IgE hafif yüksek geldi; oral steroid sonrası lezyonlar kısa süre gerileyip kesince rebound alevlendi.",
                        "teaching_point": "Kan tetkikleri tedaviyi yönlendirmez; sistemik steroid rebound alevlenmeye yol açtığı için önerilmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu çocukta en olası tanınız nedir?",
                "options": [
                    {"text": "Atopik dermatit alevlenmesi", "is_correct": True, "explanation": "Kaşıntı, fleksural dağılım, bebeklikten beri tekrarlayan seyir ve ailede atopi atopik dermatiti gösterir. Enfeksiyon bulgusu yoktur.", "new_finding": "Tanı: Atopik dermatit alevlenmesi (orta şiddet, enfeksiyonsuz)."},
                    {"text": "Seboreik dermatit", "is_correct": False, "scenario_update": "Saçlı deri ve kıvrım yerlerinde yağlı sarı kepek yoktu, kaşıntı çok belirgindi.", "teaching_point": "Seboreik dermatit daha az kaşıntılıdır ve saçlı deri, kaş ve nazolabial bölgeyi tutar."},
                    {"text": "Allerjik kontakt dermatit", "is_correct": False, "scenario_update": "Lezyonlar bir temas alanıyla sınırlı değil, simetrik ve kronikti.", "teaching_point": "Kontakt dermatit temas alanıyla sınırlı, keskin sınırlı lezyonlar yapar."},
                    {"text": "Psoriazis vulgaris", "is_correct": False, "scenario_update": "Plaklar ekstansör değil fleksural yüzlerdeydi ve keskin sınırlı gümüşi pul yoktu.", "teaching_point": "Psoriazis genellikle ekstansör yüzlerde keskin sınırlı kalın gümüşi pullu plaklar yapar."}
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Ailenin kortizon kaygısına saygı göstererek steroidsiz yalnızca nemlendirici önermek ve kaşıntı için düzenli sedatif antihistaminik başlamak",
                        "is_correct": False,
                        "scenario_update": "İki hafta sonra lezyonlar yaygınlaştı ve kaşıntı nedeniyle sekonder enfeksiyon gelişti.",
                        "teaching_point": "Alevlenmede topikal kortikosteroid tedavinin temelidir; doğru potens ve sürede güvenlidir. Kaygı bilgilendirmeyle giderilmelidir."
                    },
                    {
                        "text": "Günde 2-3 kez bol nemlendirici, gövdeye orta potensli steroidi 1-2 hafta günde bir kez sürmek; kısa ılık banyo önermek ve kaygıyı gidermek",
                        "is_correct": True,
                        "explanation": "Nemlendirici deri bariyerini onarır. Orta potensli steroid alevlenmeyi kontrol eder; ardından haftada iki gün koruyucu kullanım yeni alevlenmeleri azaltır. Parmak ucu birimiyle doz eğitimi uyumu artırır.",
                        "new_finding": "Metilprednizolon aseponat krem ve nemlendirici ile taburcu edildi, parmak ucu birimi gösterildi. İkinci hafta kontrolünde lezyonlar %80 geriledi, çocuk geceleri uyuyordu."
                    },
                    {
                        "text": "Hızlı etki için yüze ve gövdeye çok yüksek potensli klobetazol kremi günde iki kez bir ay sürmelerini söylemek",
                        "is_correct": False,
                        "scenario_update": "Bir ay sonra yüzde atrofi ve telenjiektazi gelişti.",
                        "teaching_point": "Küçük çocukta, özellikle yüzde çok yüksek potensli steroid uzun süre kullanılmaz; potens bölgeye göre seçilir."
                    },
                    {
                        "text": "Beş gün oral prednizolon başlamak, banyoyu haftada bire indirip cildin kurumasını önlemek için evde bebek yağı kullanmalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Oral steroid kesilince lezyonlar daha ağır alevlendi; bebek yağı yeterli nem sağlamadı.",
                        "teaching_point": "Sistemik steroid rebound yaptığı için önerilmez; kısa ılık banyo sonrası nemlendirici uygulaması faydalıdır."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y82",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "7 Yaşında (24 kg)",
        "gender": "Erkek",
        "complaint": "Üç haftadır özellikle geceleri artan, uykudan uyandıran şiddetli kaşıntı ve elde, bilekte, belde kabarcıklar",
        "history": "Annesi anlatıyor: 'Üç haftadır geceleri kaşınmaktan uyuyamıyor. Önce parmak aralarında küçük kabarcıklar çıktı, sonra bileklere, karna, kasığa yayıldı. Ben de ve küçük kardeşi de son bir haftadır kaşınıyoruz.' Kalabalık bir apartman dairesinde yaşıyorlar, bir ay önce yurt dışından gelen akrabaları evde kalmış. Daha önce verilen antihistaminik ve kortizonlu krem kaşıntıyı azaltmamış. Ateş yok.",
        "final_diagnosis": "Skabiyez (Uyuz)",
        "disposition": "Tüm Ev Halkının Eş Zamanlı Permetrin Tedavisi ve Çevresel Önlemlerle Yeşil Alandan Taburculuk",
        "case_pearl": "Geceleri artan kaşıntı, ailede benzer yakınma ve parmak araları, el bileği, bel, aksiller ön kıvrım, genital bölge ve meme başı çevresindeki papül ve tüneller skabiyezi düşündürür. Tanı kliniktir, dermoskopi doğrulamaya yardımcı olur. Permetrin %5 krem boyundan aşağı tüm vücuda (2 yaş altında saçlı deri ve yüz dahil) sürülür, 8-12 saat sonra yıkanır ve 7 gün sonra tekrarlanır. Tüm ev halkı aynı gün tedavi edilmelidir. Kaşıntı tedaviden sonra 2-4 hafta sürebilir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Geceleri artan kaşıntısı olan bu çocukta muayenede nelere dikkat edersiniz?",
                "options": [
                    {
                        "text": "Yalnızca annenin gösterdiği el bölgesine bakıp lezyonları kontakt dermatit kabul ederek daha güçlü bir kortizonlu krem yazmak",
                        "is_correct": False,
                        "scenario_update": "Güçlü steroid kaşıntıyı kısa süre bastırdı, lezyonlar yaygınlaştı ve kardeşte de tablo ağırlaştı.",
                        "teaching_point": "Topikal steroid altta yatan nedeni tedavi etmez, tabloyu maskeleyerek yaygınlaşmasına yol açabilir."
                    },
                    {
                        "text": "Tüm deriyi muayene edip parmak araları, el bilekleri, bel, aksilla, genital bölgedeki papül ve tünelleri aramak; ev halkında kaşıntıyı sorgulamak",
                        "is_correct": True,
                        "explanation": "Tipik dağılım, tüneller ve ailede kaşıntı birlikteliği tanıya en çok katkı sağlayan bulgulardır. Genital bölgedeki nodüller sık atlanır.",
                        "new_finding": "Genel durum iyi, ateş yok. Parmak aralarında, el bileklerinin iç yüzünde ve bel çevresinde yaygın eritemli papüller, ekskoriasyonlar ve 3-5 mm'lik ince, kıvrımlı gri çizgiler. Penis gövdesinde ve skrotumda birkaç kaşıntılı nodül. Aksilla ön kıvrımında papüller. Yüz ve saçlı deri temiz. Sekonder enfeksiyon bulgusu yok."
                    },
                    {
                        "text": "Kaşıntıyı stres ve kuru cilde bağlayarak muayeneyi kısa tutmak, nemlendirici ve gece için sedatif antihistaminik önermek",
                        "is_correct": False,
                        "scenario_update": "Kaşıntı sürdü; iki hafta sonra okul arkadaşlarında da benzer yakınma başladı.",
                        "teaching_point": "Ailede eş zamanlı kaşıntı bulaşıcı bir nedene işaret eder; tüm deri muayenesi atlanmamalıdır."
                    },
                    {
                        "text": "Ateş olmamasına rağmen yaygın papüller nedeniyle suçiçeği kabul edip çocuğu okuldan izole etmek ve asiklovir başlamak",
                        "is_correct": False,
                        "scenario_update": "Asiklovir etkisiz kaldı; lezyonların üç haftalık süresi ve dağılımı bu tanıyla uyuşmadı.",
                        "teaching_point": "Suçiçeği ateşle, farklı evrelerde veziküllerle, gövdeden başlayarak ve birkaç gün içinde seyreder."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Tanıyı desteklemek için hangi yaklaşım en uygundur?",
                "options": [
                    {
                        "text": "Tam kan sayımında eozinofil sayısı ve total IgE istemek, değerler yüksekse alerjik bir tablo kabul edip alerji polikliniğine sevk etmek",
                        "is_correct": False,
                        "scenario_update": "Eozinofil hafif yüksek geldi ve çocuk alerji polikliniğine yönlendirildi; tedavi haftalarca gecikti.",
                        "teaching_point": "Eozinofili nonspesifiktir; tanıyı koydurmaz ve bulaşıcı tabloyu geciktirir."
                    },
                    {
                        "text": "Lezyonlardan mantar kültürü ve KOH incelemesi istemek, sonuçlar çıkana dek topikal antifungal tedavi başlatmak",
                        "is_correct": False,
                        "scenario_update": "KOH negatif geldi, antifungal tedavi yararsız kaldı.",
                        "teaching_point": "Dağılım ve tüneller mantar enfeksiyonuyla uyumlu değildir."
                    },
                    {
                        "text": "Tanıyı kliniğe dayandırmak; mümkünse tünel ucundan dermoskopi yapmak, gerekirse kazıma örneğini mikroskopta incelemek",
                        "is_correct": True,
                        "explanation": "Tanı genellikle klinik bulgularla konur. Dermoskopi ve kazıma doğrulamaya yardımcıdır ancak negatif sonuç tanıyı dışlamaz.",
                        "new_finding": "Dermoskopide tünel ucunda koyu üçgen bir yapı ve arkasında ince bir iz görüldü. Kazıma mikroskopisinde akar ve yumurtalar saptandı."
                    },
                    {
                        "text": "Nodüler lezyonlar nedeniyle genital bölgedeki nodülden punch biyopsi almak ve patoloji sonucuna göre tedavi planı yapmak",
                        "is_correct": False,
                        "scenario_update": "Biyopsi sonucu iki hafta sürdü; bu sürede ev halkının yakınmaları arttı.",
                        "teaching_point": "Tipik tabloda biyopsi gereksizdir ve tedaviyi geciktirir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Papüler ürtiker", "is_correct": False, "scenario_update": "Lezyonlar parmak arası, bilek ve genital bölgedeydi ve tüneller vardı.", "teaching_point": "Papüler ürtiker açık bölgelerde gruplaşan ısırık papülleridir; tünel ve genital tutulum yoktur."},
                    {"text": "Atopik dermatit", "is_correct": False, "scenario_update": "Daha önce cilt hastalığı yoktu, ev halkında aynı anda başlayan kaşıntı vardı.", "teaching_point": "Atopik dermatit kronik seyirlidir ve ailede eş zamanlı başlamaz."},
                    {"text": "Skabiyez (uyuz)", "is_correct": True, "explanation": "Geceleri artan kaşıntı, ev halkında benzer yakınma, tipik dağılım, tüneller, genital nodüller ve mikroskopide akar skabiyezi gösterir.", "new_finding": "Tanı: Skabiyez."},
                    {"text": "Tinea korporis", "is_correct": False, "scenario_update": "Halka şeklinde aktif kenarlı plak yoktu ve KOH incelemesine gerek kalmadan akar gösterildi.", "teaching_point": "Tinea halka şeklinde, ortası açılan, kenarı aktif plaklar yapar."}
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk ve ailesi için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Yalnızca çocuğa permetrin kremi bir kez uygulamak, kaşıntısı olan anne ve kardeşi kendi hekimlerine başvurmaları için yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk iki hafta sonra yeniden enfekte oldu; tedavi edilmeyen ev halkı bulaşı sürdürdü.",
                        "teaching_point": "Tüm ev halkı belirti olsun olmasın aynı gün tedavi edilmeli ve tedavi 7 gün sonra tekrarlanmalıdır."
                    },
                    {
                        "text": "Permetrini boyundan aşağı tüm vücuda sürüp 8-12 saat sonra yıkamak, 7 gün sonra tekrarlamak ve tüm ev halkını aynı gün tedavi etmek",
                        "is_correct": True,
                        "explanation": "Eş zamanlı ev halkı tedavisi ve tekrar doz yeniden enfeksiyonu önler. Çamaşırlar 60°C'de yıkanmalı ya da 72 saat kapalı poşette bekletilmelidir. Kaşıntının 2-4 hafta sürmesi tedavi başarısızlığı değildir.",
                        "new_finding": "Tüm aile aynı gece tedavi edildi ve tedavi bir hafta sonra tekrarlandı. Dördüncü haftada kaşıntı tamamen geçti, yeni lezyon çıkmadı."
                    },
                    {
                        "text": "Kaşıntıyı hızla azaltmak için yüksek potensli topikal steroid ve oral antihistaminik başlamak, lezyonlar iki hafta sonra hâlâ sürerse ancak o zaman yeniden değerlendirip antiparaziter tedaviyi planlamak",
                        "is_correct": False,
                        "scenario_update": "Steroid altında lezyonlar yaygınlaştı ve kabuklanma arttı.",
                        "teaching_point": "Topikal steroid bu tabloda tedavi değildir; önce antiparaziter tedavi yapılmalıdır."
                    },
                    {
                        "text": "Permetrin kremini yalnızca lezyonlu bölgelere günde iki kez bir hafta sürmelerini ve kaşıntı geçene dek tedaviyi sürdürmelerini önermek",
                        "is_correct": False,
                        "scenario_update": "Lezyonsuz bölgelerdeki akarlar tedavi edilmedi; kaşıntı nedeniyle krem gereksiz uzun kullanıldı ve irritasyon gelişti.",
                        "teaching_point": "Krem tüm vücuda uygulanır; kaşıntının sürmesi tedavinin uzatılmasını gerektirmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y83",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "5 Yaşında (18 kg)",
        "gender": "Kız",
        "complaint": "Sağ bacakta dün akşam başlayıp sabah büyüyen kırmızı, şiş ve kaşıntılı alan",
        "history": "Annesi anlatıyor: 'Yazlıktayız, akşam bahçede çok sivrisinek vardı. Gece kaşındı, sabah baldırında avuç içi büyüklüğünde kırmızı ve şiş bir alan vardı. Ortasında küçük bir sivrisinek ısırığı izi var.' Ateş, kusma, nefes darlığı, dudak ve göz şişliği yok. Daha önceki yazlarda da ısırıklar çok şişiyormuş. Bilinen ilaç alerjisi yok. Çocuk oyun oynuyor ve basabiliyor.",
        "final_diagnosis": "Sivrisinek Isırığına Büyük Lokal Reaksiyon",
        "disposition": "Soğuk Uygulama, Oral Antihistaminik ve Isırıktan Korunma Önerileriyle Yeşil Alandan Taburculuk",
        "case_pearl": "Isırıktan sonraki saatler içinde başlayan, kaşıntının ağrıdan baskın olduğu, ateşsiz ve sistemik bulgusuz büyük, kızarık ve şiş alan büyük lokal reaksiyondur ve sıklıkla selülitle karıştırılır. Selülit genellikle ısırıktan 1-3 gün sonra başlar, ağrılıdır, yayılır ve ateş eşlik edebilir. Büyük lokal reaksiyon 24-48 saatte zirve yapıp 3-10 günde geriler. Antibiyotik gerekmez. Sistemik reaksiyon olmadığı için adrenalin oto-enjektörü veya alerji testi gerekmez.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Bacağında kızarık ve şiş alan olan bu çocukta muayenede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Bacaktaki kızarıklığı enfeksiyon kabul ederek yalnızca lezyonu değerlendirmek ve sistemik bulguları sorgulamadan oral antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik başlandı; reaksiyon üç günde kendiliğinden geriledi ve aile her ısırıkta antibiyotik istemeye başladı.",
                        "teaching_point": "Başlangıç zamanı, kaşıntı-ağrı dengesi ve sistemik bulgular sorgulanmadan antibiyotik kararı verilmemelidir."
                    },
                    {
                        "text": "Havayolu, solunum ve deri muayenesiyle sistemik reaksiyonu dışlamak; alanın sıcaklığını, hassasiyetini, sınırını, ısırık izini ve lenfanjiti değerlendirmek",
                        "is_correct": True,
                        "explanation": "Önce sistemik alerjik reaksiyon dışlanır. Lezyonun başlangıç zamanı, kaşıntının ağrıya baskınlığı, hassasiyet ve lenfanjit alerjik-inflamatuvar bir yanıtı bakteriyel enfeksiyondan ayırmada yol gösterir.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 98/dk, SS 20/dk, SpO2 %99. Ürtiker, anjiyoödem, hışıltı yok. Sağ baldırda 8x6 cm, ortasında ısırık noktası olan, açık kırmızı, ödemli, hafif ılık, çok kaşıntılı ancak az hassas alan. Lenfanjit çizgisi ve fluktuasyon yok. Popliteal ve inguinal lenf nodları ele gelmiyor. Diğer bacakta birkaç küçük ısırık papülü."
                    },
                    {
                        "text": "Şişlik nedeniyle anafilaksi riskini düşünüp muayeneyi tamamlamadan intramüsküler adrenalin uygulamak ve çocuğu Sarı Alanda 6 saat izlemek",
                        "is_correct": False,
                        "scenario_update": "Adrenalin sonrası çocukta çarpıntı ve solukluk gelişti; sistemik tutulum bulgusu yoktu.",
                        "teaching_point": "Adrenalin sistemik reaksiyon için verilir; yalnız lokal şişlikte endikasyonu yoktur."
                    },
                    {
                        "text": "Derin ven trombozunu dışlamak için muayeneyi kısa tutup acil alt ekstremite venöz Doppler ultrasonografisi ve D-dimer istemek",
                        "is_correct": False,
                        "scenario_update": "Doppler normal geldi, D-dimer hafif yüksekti; çocuk saatlerce gereksiz tetkikle bekletildi.",
                        "teaching_point": "Risk faktörü olmayan çocukta ısırık sonrası lokal şişlik tromboz düşündürmez; görüntüleme gereksizdir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Sistemik bulgusu olmayan bu çocukta hangi yaklaşım uygundur?",
                "options": [
                    {
                        "text": "Tam kan sayımı, CRP ve kan kültürü istemek; lökosit ve CRP yüksekse intravenöz antibiyotikle yatış planlamak",
                        "is_correct": False,
                        "scenario_update": "CRP 8 mg/L, lökosit normal geldi; kan alımı çocuğu çok korkuttu ve yönetim değişmedi.",
                        "teaching_point": "Lokal reaksiyon ile basit cilt enfeksiyonunun ayrımı kliniktir; kan tetkikleri katkı sağlamaz."
                    },
                    {
                        "text": "Lezyon altında apse olup olmadığını görmek için yumuşak doku ultrasonografisi istemek ve sonucuna göre drenaj planlamak",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografide yalnızca cilt altı ödemi görüldü, sıvı koleksiyonu yoktu.",
                        "teaching_point": "Fluktuasyon ve püy yokken ultrasonografi yönetimi değiştirmez."
                    },
                    {
                        "text": "Tetkik istemeden lezyon sınırını kalemle çizip fotoğraflamak, saati not etmek ve ilerleme olursa yeniden değerlendirme planlamak",
                        "is_correct": True,
                        "explanation": "Klinik tanı yeterlidir. Sınırın işaretlenmesi seyrin nesnel izlenmesini sağlar ve aile için yeniden başvuru ölçütü oluşturur.",
                        "new_finding": "Lezyon sınırı işaretlendi ve fotoğraflandı. Bir saatlik gözlemde sınır değişmedi, çocuk iyi görünüyordu."
                    },
                    {
                        "text": "Sivrisinek alerjisini doğrulamak için spesifik IgE testi ve deri prick testi planlayıp sonuç gelene kadar ısırıklardan korunmayı önermek",
                        "is_correct": False,
                        "scenario_update": "Testler pahalı ve yorumu belirsiz oldu; acil yönetimi değiştirmedi.",
                        "teaching_point": "Yalnız ısırık bölgesiyle sınırlı reaksiyonda rutin alerji testi önerilmez; sistemik reaksiyon riski düşüktür."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Sivrisinek ısırığına büyük lokal reaksiyon", "is_correct": True, "explanation": "Isırıktan saatler sonra başlayan, kaşıntının baskın olduğu, ateşsiz ve sistemik bulgusuz, ortasında ısırık noktası olan geniş şişlik ve önceki yazlarda benzer öykü büyük lokal reaksiyonu gösterir.", "new_finding": "Tanı: Sivrisinek ısırığına büyük lokal reaksiyon."},
                    {"text": "Nonpürülan selülit", "is_correct": False, "scenario_update": "Lezyon ısırıktan saatler sonra başlamıştı, çok kaşıntılıydı, az hassastı ve ateş yoktu.", "teaching_point": "Selülit genellikle 1-3 gün sonra, ağrılı ve ilerleyici biçimde gelişir."},
                    {"text": "Sistemik alerjik reaksiyon", "is_correct": False, "scenario_update": "Ürtiker, anjiyoödem, solunum veya dolaşım bulgusu yoktu.", "teaching_point": "Sistemik reaksiyonda ısırık alanı dışında deri, solunum veya dolaşım tutulumu olur."},
                    {"text": "Kontakt dermatit", "is_correct": False, "scenario_update": "Lezyonun ortasında ısırık noktası vardı ve bir temas maddesi öyküsü yoktu.", "teaching_point": "Kontakt dermatitte temas alanına uyan, sıklıkla veziküler, keskin sınırlı lezyon olur."}
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun taburculuk planı hangisidir?",
                "options": [
                    {
                        "text": "Olası enfeksiyona karşı oral sefaleksin 5 gün başlamak ve lezyon tamamen geçene kadar bacağı sargıyla kapatmalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik sonrası çocukta ishal gelişti; sargı altında kaşıntı arttı.",
                        "teaching_point": "Büyük lokal reaksiyonda antibiyotik gerekmez."
                    },
                    {
                        "text": "Soğuk kompres ve oral setirizin önermek, gerekirse kısa süre orta potensli steroid krem sürmek; sivrisinek kovucu ve cibinlik önerip uyarı bulgularını anlatmak",
                        "is_correct": True,
                        "explanation": "Semptomatik tedavi yeterlidir. Çocuklara uygun kovucular (DEET ≤%30 veya ikaridin) ve fiziksel korunma yeni ısırıkları önler. Ateş, artan ağrı, kırmızı çizgi veya sınırın yayılması başvuru nedenidir.",
                        "new_finding": "Setirizin ve soğuk uygulama ile taburcu edildi. Şişlik ikinci gün azalmaya başladı ve beşinci gün tamamen geçti."
                    },
                    {
                        "text": "Sonraki ısırıklarda anafilaksi gelişebileceğini söyleyip adrenalin oto-enjektörü reçete etmek ve çocuk alerji polikliniğine sevk etmek",
                        "is_correct": False,
                        "scenario_update": "Aile her ısırıkta panikle oto-enjektör kullanmayı düşündü; alerji polikliniği ek bir risk saptamadı.",
                        "teaching_point": "Büyük lokal reaksiyon sonrası sistemik reaksiyon riski düşüktür; oto-enjektör gerekmez."
                    },
                    {
                        "text": "Beş gün yüksek doz oral prednizolon başlamak ve şişliğin geçmesini hızlandırmak için lezyon bölgesine sıcak kompres uygulamalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Sıcak uygulama kaşıntı ve şişliği artırdı; sistemik steroid gereksiz yan etki riski oluşturdu.",
                        "teaching_point": "Soğuk uygulama ödemi ve kaşıntıyı azaltır; rutin sistemik steroid önerilmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y84",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "8 Yaşında (26 kg)",
        "gender": "Erkek",
        "complaint": "Sol bacakta iki gündür giderek büyüyen ağrılı kızarıklık, şişlik ve bugün başlayan ateş",
        "history": "Annesi anlatıyor: 'Dört gün önce böcek ısırdı, çok kaşıdı, yara oldu. İki gün önce etrafı kızardı, her gün biraz daha büyüyor, dokununca çok acıyor. Bu sabah ateşi 38.3°C oldu.' Basmakta zorlanıyor ama yürüyebiliyor. İçinde cerahat birikmesi fark etmemişler. Kronik hastalık, diyabet veya bağışıklık sorunu yok. Aşıları tam. İlaç alerjisi yok.",
        "final_diagnosis": "Nonpürülan Selülit (Alt Ekstremite)",
        "disposition": "Oral Sefaleksin ve 48 Saat Sonra Kontrolle Yeşil Alandan Taburculuk",
        "case_pearl": "Nonpürülan selülit sınırları belirsiz, sıcak, ağrılı ve yayılan eritemle seyreder. Etken çoğunlukla A grubu streptokok ve S. aureus'tur. Genel durumu iyi çocukta kan tetkiki ve kültür gerekmez. Fluktuasyon şüphesi varsa ultrasonografi apseyi gösterir. Ağızdan sefaleksin 5 gün yeterlidir ve yanıta göre uzatılır. Ekstremite yükseltilir, sınır işaretlenir ve 48 saatte kontrol edilir. Ağrının bulgularla orantısız olması, hızlı yayılım, bül veya toksik görünüm nekrotizan fasiiti düşündürür.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Bacağında yayılan ağrılı kızarıklık ve ateşi olan bu çocukta muayenede neye dikkat edersiniz?",
                "options": [
                    {
                        "text": "Genel görünümü ve vitalleri değerlendirip eritemin sınırlarını, fluktuasyonu, lenfanjiti, krepitasyonu, eklem hareketini ve ağrının bulgularla orantısını incelemek",
                        "is_correct": True,
                        "explanation": "Fluktuasyon apseyi, krepitasyon ve orantısız ağrı derin enfeksiyonu, eklem hareket kısıtlılığı eklem tutulumunu düşündürür. Genel durum yatış kararını belirler.",
                        "new_finding": "Vital Bulgular: Ateş 38.2°C, KTA 108/dk, SS 20/dk, TA 104/66 mmHg, KDZ 2 sn. Genel durum iyi. Sol baldır ön yüzünde 10x7 cm, sınırları belirsiz, parlak kırmızı, sıcak, ödemli ve hassas alan; merkezde kabuklu küçük bir yara. Fluktuasyon, bül ve krepitasyon yok. Diz ve ayak bileği hareketleri ağrısız ve tam. Sol inguinal bölgede 1.5 cm hassas lenf nodu. Lenfanjit çizgisi yok."
                    },
                    {
                        "text": "Kızarıklığı böcek ısırığının lokal reaksiyonu kabul edip yalnız lezyona bakmak, antihistaminik ve soğuk uygulamayla aileyi rahatlatmak",
                        "is_correct": False,
                        "scenario_update": "İki gün sonra kızarıklık uyluğa yayıldı ve ateş 39°C'ye çıktı.",
                        "teaching_point": "Isırıktan günler sonra başlayan, ağrılı, yayılan kızarıklık ve ateş bakteriyel enfeksiyonu düşündürür."
                    },
                    {
                        "text": "Ateş nedeniyle hemen Sarı Alana alıp damar yolu açmak ve muayene tamamlanmadan intravenöz geniş spektrumlu antibiyotik başlatmak",
                        "is_correct": False,
                        "scenario_update": "Genel durumu iyi olan çocuk gereksiz yere damar yolu ve yatış sürecine alındı.",
                        "teaching_point": "Genel durumu iyi, sistemik toksisitesi olmayan çocukta ağızdan tedavi yeterlidir."
                    },
                    {
                        "text": "Kızarıklığın ortasındaki yarayı bistüriyle açıp drene etmek ve içinden kültür almak, sonra muayeneyi tamamlamak",
                        "is_correct": False,
                        "scenario_update": "Kesiden püy gelmedi; gereksiz bir yara oluşturuldu.",
                        "teaching_point": "Fluktuasyon olmayan lezyonda kesi yapılmaz; drenaj yalnızca apse varlığında yapılır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Genel durumu iyi ve fluktuasyonu olmayan bu çocukta hangi tetkik yaklaşımı uygundur?",
                "options": [
                    {
                        "text": "Kemik tutulumunu dışlamak için acil alt ekstremite MR görüntülemesi istemek ve sonucu gelene kadar antibiyotiği ertelemek",
                        "is_correct": False,
                        "scenario_update": "MR için sedasyon gerekti ve tedavi saatlerce gecikti; kemik tutulumu yoktu.",
                        "teaching_point": "Kemik ağrısı veya eklem kısıtlılığı olmadan MR gerekmez; antibiyotik geciktirilmemelidir."
                    },
                    {
                        "text": "Kan tetkiki ve kültür istemeden eritem sınırlarını kalemle işaretleyip fotoğraflamak ve tedaviye yanıtı izleme planı yapmak",
                        "is_correct": True,
                        "explanation": "Genel durumu iyi, komplike olmayan olguda kan kültürü çok nadir pozitiftir ve yönetimi değiştirmez. Sınırın işaretlenmesi yanıtın değerlendirilmesini sağlar.",
                        "new_finding": "Eritem sınırı işaretlendi ve fotoğraflandı. Tetkik istenmedi."
                    },
                    {
                        "text": "Tam kan sayımı, CRP, sedimantasyon ve kan kültürü istemek; CRP 40 mg/L'nin üzerindeyse intravenöz tedavi için yatış planlamak",
                        "is_correct": False,
                        "scenario_update": "CRP 46 mg/L geldi ve çocuk yatırıldı; genel durumu iyi olduğu için yatış gereksiz oldu.",
                        "teaching_point": "CRP tek başına yatış ölçütü değildir; karar genel duruma ve ağızdan tedaviyi tolere etmeye göre verilir."
                    },
                    {
                        "text": "Lezyon yüzeyinden sürüntü kültürü alıp antibiyogram sonucuna göre tedavi seçmek ve o zamana dek yalnızca topikal antibiyotik vermek",
                        "is_correct": False,
                        "scenario_update": "Yüzey kültüründe deri florası üredi; topikal tedavi derin dokuya etki etmedi ve kızarıklık yayıldı.",
                        "teaching_point": "Yüzey kültürü derin dokudaki etkeni yansıtmaz; topikal antibiyotik derin deri enfeksiyonunda etkisizdir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Deri apsesi", "is_correct": False, "scenario_update": "Fluktuasyon ve püy yoktu.", "teaching_point": "Apsede fluktuan, sınırlı koleksiyon bulunur ve tedavinin esası drenajdır."},
                    {"text": "Nonpürülan selülit", "is_correct": True, "explanation": "Isırık sonrası gelişen, sınırları belirsiz, sıcak, ağrılı, yayılan eritem, hafif ateş ve bölgesel lenfadenopati, fluktuasyon olmadan nonpürülan selüliti gösterir.", "new_finding": "Tanı: Nonpürülan selülit."},
                    {"text": "Nekrotizan fasiit", "is_correct": False, "scenario_update": "Genel durum iyiydi, ağrı bulgularla orantılıydı, bül ve krepitasyon yoktu.", "teaching_point": "Nekrotizan fasiitte toksik görünüm, orantısız ağrı, hızlı yayılım, bül ve krepitasyon görülür."},
                    {"text": "Büyük lokal ısırık reaksiyonu", "is_correct": False, "scenario_update": "Kızarıklık ısırıktan iki gün sonra başlamış, ağrılı ve yayılıcıydı ve ateş vardı.", "teaching_point": "Lokal reaksiyon saatler içinde başlar, kaşıntılıdır ve ateş yapmaz."}
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Ağızdan tek başına trimetoprim-sülfametoksazol 7 gün başlamak, bacağı dinlendirmeden günlük aktivitelerine devam etmesini önermek",
                        "is_correct": False,
                        "scenario_update": "İki gün sonra kızarıklık yayılmaya devam etti; tedavi streptokokları yeterince kapsamadı.",
                        "teaching_point": "Nonpürülan selülitte streptokok kapsamı gerekir; tek başına trimetoprim-sülfametoksazol yeterli değildir."
                    },
                    {
                        "text": "Ağızdan sefaleksin 5 gün, bacağı yükseltmek ve analjezi önermek; 48 saat sonra işaretli sınırla kontrol yapıp yanıt yoksa tedaviyi uzatmak",
                        "is_correct": True,
                        "explanation": "Sefaleksin streptokok ve metisiline duyarlı S. aureus'u kapsar. 5 gün çoğu olguda yeterlidir. İlk 24-48 saatte kızarıklığın hafif artması beklenebilir.",
                        "new_finding": "Sefaleksin 50 mg/kg/gün dört dozda başlandı. 48. saat kontrolünde ateş yoktu ve kızarıklık işaretli sınırın içine çekilmişti. Beşinci gün tamamen düzeldi."
                    },
                    {
                        "text": "Ateş olduğu için intravenöz klindamisinle servise yatırmak, ateş tamamen düşene kadar en az 72 saat parenteral tedaviyi sürdürmek",
                        "is_correct": False,
                        "scenario_update": "Genel durumu iyi çocuk üç gün gereksiz yere hastanede yattı.",
                        "teaching_point": "Hafif ateş tek başına yatış endikasyonu değildir; toksik görünüm veya ağızdan alamama yatış gerektirir."
                    },
                    {
                        "text": "Topikal mupirosin ve sıcak kompresle izlemek, kızarıklık bir hafta içinde gerilemezse oral antibiyotik başlamak üzere kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Kızarıklık üç günde uyluğa yayıldı ve çocuk yüksek ateşle geri geldi.",
                        "teaching_point": "Selülit sistemik antibiyotik gerektirir; topikal tedavi yalnızca yüzeyel enfeksiyonlarda kullanılır."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y85",
        "category": "🦴 Kas-İskelet & Eklem / Ortopedik Aciller",
        "age": "10 Yaşında",
        "gender": "Kız",
        "complaint": "Sağ işaret parmağında tırnak kenarında iki gündür artan zonklayıcı ağrı ve şişlik",
        "history": "Kendisi anlatıyor: 'Tırnaklarımı ve etlerini yiyorum. İki gün önce tırnağımın yanı kızardı, şimdi şişti, zonkluyor, gece uyutmadı.' Ateş yok. Annesi sıcak su ile pansuman yapmış. Parmakta kabarcık, su toplama veya ağız çevresinde uçuk öyküsü yok. Parmak ucunun ön yüzü (pulpa) ağrılı değil. Diyabet yok.",
        "final_diagnosis": "Apseleşmiş Akut Paronişi",
        "disposition": "Lokal Anestezi Altında Drenaj ve Ilık Pansuman Önerileriyle Yeşil Alandan Taburculuk",
        "case_pearl": "Akut paronişi tırnak kıvrımının, çoğunlukla S. aureus ve streptokoklara bağlı enfeksiyonudur ve tırnak yeme ile tetiklenir. Fluktuasyon yoksa ılık su banyosu yeterlidir. Apse varsa tırnak kıvrımının künt bir aletle ya da bistüriyle kaldırılarak drenajı esastır. Drenajdan sonra yayılan selülit yoksa rutin antibiyotik gerekmez. Herpetik dolamada (veziküller, ağrının orantısız olması) kesi yapılmaz. Pulpada gerginlik ve ağrı felonu düşündürür.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Tırnak kenarında ağrılı şişliği olan bu çocukta muayenede neye dikkat edersiniz?",
                "options": [
                    {
                        "text": "Şişliğin yerini ve fluktuasyonu, tırnak altına uzanımı, pulpada gerginliği, vezikül varlığını, yayılan kızarıklık ve lenfanjiti değerlendirmek",
                        "is_correct": True,
                        "explanation": "Fluktuasyon drenaj ihtiyacını, pulpa tutulumu derin enfeksiyonu, veziküller viral nedeni gösterir. Bu ayrım yanlış kesiden korur.",
                        "new_finding": "Ateş 36.8°C. Sağ işaret parmağında radiyal tırnak kıvrımı ve eponişiyumda kırmızı, gergin şişlik; derinin altından sarı-beyaz bir koleksiyon seçiliyor, fluktuasyon pozitif. Tırnak altına uzanım yok. Pulpa yumuşak ve ağrısız. Vezikül yok. Kızarıklık parmağın proksimaline yayılmıyor, lenfanjit yok. Eklem hareketleri tam."
                    },
                    {
                        "text": "Ağrıyı kemik enfeksiyonuna bağlayıp muayeneyi kısa tutarak el grafisi istemek ve grafi sonucuna göre ortopedi konsültasyonu planlamak",
                        "is_correct": False,
                        "scenario_update": "Grafi normal geldi; ortopedi beklenirken çocuk saatlerce ağrı çekti.",
                        "teaching_point": "İki günlük lokal tırnak kıvrımı şişliğinde kemik tutulumu beklenmez; grafi gerekmez."
                    },
                    {
                        "text": "Şişliği uçuk virüsüne bağlı kabul edip muayeneye gerek duymadan oral asiklovir başlamak ve ağrı kesici önermek",
                        "is_correct": False,
                        "scenario_update": "Asiklovir verildi; apse büyüdü ve ağrı arttı.",
                        "teaching_point": "Viral parmak enfeksiyonunda veziküller görülür; püy dolu koleksiyon bakteriyel apseyi gösterir."
                    },
                    {
                        "text": "Parmaktaki şişliği ilk günlerde sık görülen basit bir kızarıklık kabul edip muayene etmeden yalnız sıcak su pansumanına devam etmelerini söylemek",
                        "is_correct": False,
                        "scenario_update": "Koleksiyon tırnak altına uzandı ve tedavi daha karmaşık hale geldi.",
                        "teaching_point": "Fluktuasyon varsa ılık banyo tek başına yeterli değildir; drenaj gerekir."
                    }
                ]
            },
            {
                "stage_title": "Girişim Kararı",
                "question": "Fluktuasyonu olan bu lezyonda bir sonraki adımınız nedir?",
                "options": [
                    {
                        "text": "Drenaj yapmadan ağızdan amoksisilin-klavulanat başlamak ve bir hafta içinde kendiliğinden açılmasını beklemek üzere aileyi bilgilendirmek",
                        "is_correct": False,
                        "scenario_update": "Bir hafta antibiyotiğe rağmen apse sürdü ve tırnak altına yayıldı.",
                        "teaching_point": "Apsede antibiyotik drenajın yerini tutmaz; fluktuan koleksiyon boşaltılmalıdır."
                    },
                    {
                        "text": "Dijital blok yapıp tırnak kıvrımını künt bir aletle veya bistüri sırtıyla tırnaktan kaldırarak koleksiyonu boşaltmak",
                        "is_correct": True,
                        "explanation": "Tırnak kıvrımının kaldırılması çoğu zaman cilt kesisi gerektirmeden drenaj sağlar. Dijital blok işlemi ağrısız yapar.",
                        "new_finding": "Dijital blok sonrası radiyal tırnak kıvrımı kaldırıldı, yaklaşık 0.5 mL koyu sarı püy boşaltıldı. Bölge serum fizyolojikle yıkandı. Ağrı belirgin azaldı."
                    },
                    {
                        "text": "Tırnağın tamamını çekmek için ortopedi veya el cerrahisine sevk etmek, işlem sonrasına kadar parmağa atel uygulamak",
                        "is_correct": False,
                        "scenario_update": "Tırnak çekimi gereksiz yere yapıldı; iyileşme süresi uzadı.",
                        "teaching_point": "Tırnak kıvrımı apsesinde tırnak çekimi gerekmez; yalnızca tırnak altına uzanan apsede kısmi çıkarım düşünülür."
                    },
                    {
                        "text": "Koleksiyonu ince iğneyle birkaç kez aspire etmek ve kalan kısmın antibiyotikli kremle emilmesini beklemek",
                        "is_correct": False,
                        "scenario_update": "Aspirasyon yetersiz kaldı; koleksiyon iki gün içinde yeniden doldu.",
                        "teaching_point": "Yetersiz drenaj nüksle sonuçlanır; tırnak kıvrımı kaldırılarak tam boşaltım yapılmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Herpetik dolama", "is_correct": False, "scenario_update": "Vezikül yoktu ve drenajda püy geldi.", "teaching_point": "Herpetik dolamada gruplaşmış veziküller ve berrak sıvı vardır; kesi kontrendikedir."},
                    {"text": "Felon (pulpa apsesi)", "is_correct": False, "scenario_update": "Pulpa yumuşak ve ağrısızdı.", "teaching_point": "Felonda parmak ucunun ön yüzünde gergin, şiddetli ağrılı şişlik olur."},
                    {"text": "Kronik paronişi", "is_correct": False, "scenario_update": "Yakınma iki gündür vardı ve akut apse gelişmişti.", "teaching_point": "Kronik paronişi 6 haftayı aşan, sıklıkla ıslak işle ilişkili, birden fazla parmağı tutan tablodur."},
                    {"text": "Apseleşmiş akut paronişi", "is_correct": True, "explanation": "Tırnak yeme öyküsü, tırnak kıvrımında akut, fluktuan ve püylü şişlik akut apseleşmiş paronişiyi gösterir.", "new_finding": "Tanı: Apseleşmiş akut paronişi."}
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Drenaj sonrası en uygun taburculuk planı hangisidir?",
                "options": [
                    {
                        "text": "Günde 3-4 kez ılık su banyosu ve analjezi önermek, yayılan kızarıklık olmadığı için antibiyotik vermemek ve tırnak yemeyi bırakmasını desteklemek",
                        "is_correct": True,
                        "explanation": "Yeterli drenaj sonrası ılık banyo iyileşmeyi hızlandırır. Selülit yoksa antibiyotik gerekmez. Tırnak yeme tekrarın en önemli nedenidir.",
                        "new_finding": "Çocuk ılık banyo önerisiyle taburcu edildi. 48 saat sonraki kontrolde şişlik ve ağrı belirgin azalmıştı."
                    },
                    {
                        "text": "Drenaj sonrası enfeksiyonun tekrar etmemesi için iki hafta oral amoksisilin-klavulanat ve topikal steroidli antibiyotik krem önermek",
                        "is_correct": False,
                        "scenario_update": "Uzun antibiyotik ishale neden oldu; steroidli krem iyileşmeye katkı sağlamadı.",
                        "teaching_point": "Yeterli drenaj sonrası rutin uzun antibiyotik önerilmez; steroid enfekte alanda iyileşmeyi geciktirebilir."
                    },
                    {
                        "text": "Yarayı sıkı kapalı pansumanla kapatıp bir hafta ıslatmamasını ve pansumanı açmamasını söylemek, kontrol planlamamak",
                        "is_correct": False,
                        "scenario_update": "Kapalı pansuman altında yara nemli kaldı ve yeniden püy birikti.",
                        "teaching_point": "Drenaj sonrası ılık banyo ve açık iyileşme önerilir; kontrol planlanmalıdır."
                    },
                    {
                        "text": "Tekrarı önlemek için tırnak kıvrımına haftalık steroid enjeksiyonu planlamak ve parmağı birkaç gün tamamen hareketsiz tutmasını istemek",
                        "is_correct": False,
                        "scenario_update": "Enjeksiyon gereksiz ağrıya neden oldu, hareketsizlik parmakta sertlik yaptı.",
                        "teaching_point": "Akut paronişide steroid enjeksiyonunun yeri yoktur; tekrar önlemenin yolu tırnak yemeyi bırakmaktır."
                    }
                ]
            }
        ]
    }
]
