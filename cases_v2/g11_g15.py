# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - G11-G15 (v2 Yeniden Yazım)
"""

CASES = [
    {
        "id": "G11",
        "category": "👶 Ağlayan, Emmeyen, Huzursuz Bebek",
        "age": "6 Haftalık",
        "gender": "Erkek",
        "complaint": (
            "Her akşamüstü saat 18:00'den sonra başlayan, saatlerce süren durdurulamayan şiddetli ağlama "
            "krizleri, bacaklarını karnına çekme ve yüzünde kızarma"
        ),
        "history": (
            "Genç anne-baba 6 haftalık ilk bebeklerini akşam saat 20:30'da büyük bir panik içinde Yeşil "
            "Alana getiriyor: 'Doktor bey/hanım, bebeğimiz son 10 gündür her akşam aynı saatlerde aralıksız "
            "çığlık atarak ağlıyor! Ne kucağımıza alınca susuyor ne memeyi verince. Karnı taş gibi "
            "sertleşiyor, bacaklarını karnına çekiyor, ellerini yumruk yapıyor ve kıpkırmızı oluyor. Gazını "
            "çıkarmaya çalıştık ama hiç fayda etmedi. Acaba bir yeri mi kırıldı, bağırsakları mı düğümlendi? "
            "Ne olur yardım edin!' Anne bebeğin gündüzleri huzurlu uyuduğunu, yalnız anne sütü aldığını, "
            "kilo alımının çok iyi olduğunu (son ayda 900 gram almış), kusma, kanlı kaka veya ateşinin "
            "olmadığını belirtiyor."
        ),
        "final_diagnosis": "İnfantil Kolik (Wessel '3'ler Kuralı' ile Uyumlu Paroksismal Aşırı Ağlama)",
        "disposition": (
            "Yeşil Alanda Kapsamlı 'Tepeden Tırnağa' Muayene (Organik Patolojilerin Dışlanması), Aile "
            "Eğitimi, 5S Yatıştırma Teknikleri ve Kırmızı Bayraklarla Taburculuk"
        ),
        "case_pearl": (
            "İnfantil kolik sağlıklı, büyüme-gelişmesi mükemmel süt çocuklarında yaşamın 2-3. haftasında "
            "başlayıp 3-4. ayda kendiliğinden sonlanan, genellikle akşam saatlerinde tekrarlayan "
            "paroksismal ağlama nöbetleridir (Wessel '3'ler Kuralı': Günde >3 saat, haftada >3 gün, en az "
            "3 hafta süren sebepsiz ağlama). Acil hekiminin EN KRİTİK GÖREVİ bebeği tamamen soyup tepeden "
            "tırnağa muayene ederek ağlamaya yol açabilecek organik patolojileri dışlamaktır: 1) Korneal "
            "abrazyon (floresein boyama), 2) Parmak veya peniste saç-ip turnikesi, 3) İnkarsere inguinal "
            "fıtık / testis torsiyonu, 4) Akut otit, 5) İdrar yolu enfeksiyonu, 6) Non-aksidental travma. "
            "Muayenesi normal olan bebekte gereksiz lavman, batın grafisi, proton pompa inhibitörü veya "
            "antibiyotik uygulanmaz. Aileye durumun iyi huylu ve geçici olduğu anlatılmalı, tükenmişlik "
            "hissine karşı destek olunmalı ve 'Sarsılmış Bebek Sendromu'na karşı mutlaka uyarı yapılmalıdır."
        ),
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": (
                    "Durdurulamayan şiddetli akşam ağlama atakları ile getirilen altı haftalık bu bebekte "
                    "ilk klinik yaklaşımınız nasıl olmalıdır?"
                ),
                "options": [
                    {
                        "text": (
                            "Genel görünümü iyi ve emmesi aktif olduğundan bebeği soymadan yalnızca karın "
                            "oskültasyonu yapmak, gaz sancısı düşünerek acil serviste simetikon damla ve "
                            "rektal gliserin fitil uygulamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Bebek soyulmadan uygulanan rektal fitil ve gaz damlası ağlamayı durdurmadı; "
                            "eksik muayene nedeniyle olası bir boğulmuş kasık fıtığı veya saç turnikesi "
                            "riski gözden kaçırılmış oldu."
                        ),
                        "teaching_point": (
                            "Huzursuz ve ağlayan süt çocuğu tamamen soyulup tepeden tırnağa muayene "
                            "edilmeden asla semptomatik gaz tedavisi veya rektal girişim uygulanmamalıdır."
                        ),
                    },
                    {
                        "text": (
                            "Bebeği tamamen soyarak yaşamsal bulguları ölçmek; kornea, kulak zarı, fontanel, "
                            "ağız içi, kasıklar, skrotum, anal bölge ve tüm parmak boğumlarını sistematik "
                            "biçimde muayene etmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Ağlayan süt çocuğunun acil servisteki değerlendirmesi gizli organik acilleri "
                            "dışlamakla başlar. Bebek tamamen soyularak parmak boğumları, genital bölge, "
                            "kasıklar, kornea ve fontanel dikkatle kontrol edilmelidir."
                        ),
                        "new_finding": (
                            "Yaşamsal bulgular: Ateş 36.8°C, KTA 142/dk, SS 34/dk, SpO2 %99. Ön fontanel "
                            "normal bombelikte, bilateral timpanik membranlar doğal, floresein ile korneal "
                            "boyanma yok. El ve ayak parmaklarında veya peniste saç-ip dolanması saptanmadı. "
                            "Bilateral inguinal herni yok, testisler skrotumda, normal boyutta ve ağrısız. "
                            "Sakinleştiğinde batın yumuşak, kitle veya organomegali yok, anal fissür görülmedi."
                        ),
                    },
                    {
                        "text": (
                            "Ağlama krizinin olası akut batın veya invajinasyon kaynaklı olabileceğini "
                            "düşünerek fizik muayene öncesinde bebeği Sarı Alana devretmek ve acil batın "
                            "ultrasonografisi için radyolojiye yönlendirmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Yaşamsal bulguları stabil olan ve kusması bulunmayan bebek Sarı Alana alındı; "
                            "ancak yapılan ultrasonografide hiçbir patoloji saptanmadı ve ailenin "
                            "anksiyetesi belirgin şekilde arttı."
                        ),
                        "teaching_point": (
                            "Yaşamsal bulguları stabil, safralı kusması veya letarjisi olmayan süt "
                            "çocuğunda fizik muayene tamamlanmadan alan değişikliği ve acil görüntüleme "
                            "yapılmaz."
                        ),
                    },
                    {
                        "text": (
                            "Şiddetli huzursuzluğun gastroözofageal reflü özofajitine bağlı olduğunu "
                            "varsayarak muayeneyi kısa tutmak, bebeği dik pozisyona alıp acil serviste oral "
                            "aljinat ve proton pompa inhibitörü başlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Kusma veya tartı kaybı olmayan bebeğe ampirik asit baskılayıcı tedavi "
                            "verildi; ancak ağlama ataklarında hiçbir gerileme sağlanamadı."
                        ),
                        "teaching_point": (
                            "Tartı alımı iyi olan ve kusma yakınması bulunmayan ağlayan bebeklerde "
                            "ampirik antireflü veya proton pompa inhibitörü tedavisinin etkinliği yoktur."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Görüntüleme Planlaması",
                "question": (
                    "Fizik muayenesi tamamen normal saptanan, ateşsiz ve son bir ayda 900 gram tartı "
                    "alımı olan bu bebekte hangi tetkik yaklaşımı doğrudur?"
                ),
                "options": [
                    {
                        "text": (
                            "Atipik seyirli gizli idrar yolu enfeksiyonunu dışlamak amacıyla mesane "
                            "kateterizasyonu ile idrar tetkiki, idrar kültürü, tam kan sayımı ve "
                            "C-reaktif protein istemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Mesane kateterizasyonu işlemi bebeğin daha şiddetli ağlamasına yol açtı; "
                            "tam idrar tetkiki (lökosit 0, nitrit negatif) ve akut faz reaktanları "
                            "tamamen normal sonuçlandı."
                        ),
                        "teaching_point": (
                            "Ateşi olmayan, tartı alımı mükemmel olan ve atak aralarında tamamen huzurlu "
                            "seyreden sağlıklı süt çocuklarında invaziv idrar sondası ve kan tetkiki "
                            "endikasyonu yoktur."
                        ),
                    },
                    {
                        "text": (
                            "İntestinal malrotasyon veya erken evre ileokolik geçiş patolojisini ekarte "
                            "etmek amacıyla ayakta direkt batın grafisi ve tüm batın ultrasonografisi "
                            "planlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Çekilen ayakta direkt batın grafisinde fizyolojik gaz dağılımı izlendi, "
                            "ultrasonografi normal raporlandı; bebek gereksiz radyasyona maruz kaldı."
                        ),
                        "teaching_point": (
                            "Safralı kusma, batın distansiyonu, kanlı dışkılama veya atak aralarında "
                            "letarji bulgusu olmayan ve muayenesi normal bebekte radyolojik görüntüleme "
                            "önerilmez."
                        ),
                    },
                    {
                        "text": (
                            "Kırmızı bayrak bulgusu ve patolojik muayene verisi bulunmadığından laboratuvar "
                            "testi veya radyolojik görüntüleme istemeden klinik izlem ve aile "
                            "değerlendirmesine geçmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Büyüme-gelişmesi normal olan, kırmızı bayrak bulgusu (ateş, safralı kusma, "
                            "kanlı gaita, letarji) taşımayan ve tepeden tırnağa muayenesi doğal saptanan "
                            "bebekte laboratuvar veya görüntüleme tetkiki yönetimi değiştirmez."
                        ),
                        "new_finding": (
                            "Ek invaziv tetkik istenmedi; bebek loş ve sakin ortamda anne kucağında "
                            "ritmik pışpışlama ile sakinleşti, aktif göz teması kurdu."
                        ),
                    },
                    {
                        "text": (
                            "Besin proteini duyarlılığını ve gizli gastrointestinal kanamayı araştırmak "
                            "üzere gaitada gizli kan, gaita redüktan madde, gaita pH ve spesifik IgE "
                            "paneli çalışmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "İshal, mukuslu-kanlı dışkılama veya atopik egzama bulgusu olmayan bebekte "
                            "tüm gaita ve spesifik IgE testleri negatif sonuçlandı."
                        ),
                        "teaching_point": (
                            "Gaitada mukus/kan, kusma veya büyüme geriliği eşlik etmeyen izole akşam "
                            "ağlama ataklarında rutin alerji ve gaita taraması önerilmez."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı ve Ayırıcı Değerlendirme",
                "question": (
                    "Öyküsü, büyüme eğrisi ve tamamen normal fizik muayene bulgularıyla bu bebekte en "
                    "olası klinik tanınız nedir?"
                ),
                "options": [
                    {
                        "text": "İnek Sütü Proteini Alerjik Proktokoliti",
                        "is_correct": False,
                        "scenario_update": (
                            "Alerjik proktokolitte çizgi şeklinde kanlı ve bol mukuslu gaita beklenir; "
                            "bu bebekte dışkılama paterni ve cilt muayenesi tamamen normaldir."
                        ),
                        "teaching_point": (
                            "İnek sütü proteini alerjisi yalnızca gün boyu süren dirençli huzursuzlukta "
                            "kanlı-mukuslu gaita, kusma, egzama veya tartı alımında duraklama varsa "
                            "düşünülür."
                        ),
                    },
                    {
                        "text": "Komplike Gastroözofageal Reflü Hastalığı",
                        "is_correct": False,
                        "scenario_update": (
                            "Hastada tekrarlayan kusma, beslenmeyi reddetme, opisthotonus postürü veya "
                            "tartı kaybı bulunmadığından reflü özofajiti klinik tabloyla uyumlu değildir."
                        ),
                        "teaching_point": (
                            "Kusması olmayan ve haftalık tartı alımı normal olan bebeklerde sadece akşam "
                            "saatlerinde ortaya çıkan ağlama krizleri reflü hastalığı ile açıklanamaz."
                        ),
                    },
                    {
                        "text": "Korneal Abrazyon veya Saç Turnikesi Sendromu",
                        "is_correct": False,
                        "scenario_update": (
                            "Floresein boyama ve ekstremite/genital bölge muayenesi tamamen normal "
                            "saptanmış olup akut travmatik/iskemik patolojiler dışlanmıştır."
                        ),
                        "teaching_point": (
                            "Korneal abrazyon ve saç turnikesi sendromu günün belirli bir saatinde değil, "
                            "olay geliştiği andan itibaren kesintisiz ağlamaya yol açar."
                        ),
                    },
                    {
                        "text": "İnfantil Kolik (Fonksiyonel Paroksismal Ağlama)",
                        "is_correct": True,
                        "explanation": (
                            "Sağlıklı ve büyümesi normal bir süt çocuğunda özellikle akşam saatlerinde "
                            "yoğunlaşan, organik neden saptanamayan paroksismal ağlama atakları infantil "
                            "kolik (Wessel kriterleri / Roma IV) tanısını koydurur."
                        ),
                        "new_finding": (
                            "Kesin Tanı: İnfantil Kolik. Organik acil patolojiler güvenli biçimde "
                            "dışlandı."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Tedavi, İzlem ve Taburculuk Planı",
                "question": (
                    "İnfantil kolik tanısı koyduğunuz bu bebeğin acil servis yönetimi ve taburculuk "
                    "eğitiminde en uygun yaklaşım hangisidir?"
                ),
                "options": [
                    {
                        "text": (
                            "Tablonun selim ve geçici olduğunu açıklamak, 5S yatıştırma manevralarını "
                            "göstermek, ebeveyn tükenmişliğinde bebeği sarsmama uyarısı ve kırmızı bayrak "
                            "eğitimiyle ilaçsız taburcu etmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "İnfantil kolikte en kanıta dayalı yaklaşım aileyi rahatlatmak, duyusal "
                            "yatıştırma tekniklerini öğretmek ve ebeveyn tükenmişliğine bağlı 'Sarsılmış "
                            "Bebek Sendromu'nu önleyici danışmanlık vermektir."
                        ),
                        "new_finding": (
                            "Ailenin kaygıları giderildi, yatıştırma teknikleri ve acil başvuru "
                            "gerektiren kırmızı bayraklar (ateş, safralı kusma, kanlı gaita, letarji) "
                            "anlatılarak bebek güvenle taburcu edildi."
                        ),
                    },
                    {
                        "text": (
                            "Anne sütünden geçen antijenleri kesmek amacıyla anneye sıkı süt ve süt "
                            "ürünleri eliminasyon diyeti başlamak, bebeğe ise simetikon damla ve oral "
                            "antihistaminik reçete etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Kanıtlanmamış alerji nedeniyle anneye gereksiz kısıtlayıcı diyet uygulandı; "
                            "altı haftalık bebeğe verilen sedatif antihistaminik ise letarji ve apne "
                            "riski yarattı."
                        ),
                        "teaching_point": (
                            "Süt çocuklarında antihistaminik veya sedatif ilaçlar solunum depresyonu "
                            "riski nedeniyle kontrendikedir; simetikonun ise plaseboya üstünlüğü "
                            "gösterilmemiştir."
                        ),
                    },
                    {
                        "text": (
                            "Emzirmeyi geçici olarak durdurup tam hidrolize hipoalerjenik mamaya geçmek "
                            "ve akşam ağlama krizlerini önlemek için günde iki kez oral trimebutin "
                            "süspansiyon başlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Anne sütünün kesilmesi laktasyonu azalttı ve bebeğin beslenme düzenini "
                            "bozdu; spazmolitik ilaç kullanımı ise paralitik ileus riski oluşturdu."
                        ),
                        "teaching_point": (
                            "İnfantil kolikte anne sütü kesinlikle kesilmez ve küçük süt çocuklarında "
                            "intestinal motilite düzenleyici spazmolitik ilaçlar kullanılmaz."
                        ),
                    },
                    {
                        "text": (
                            "Akşam saatlerindeki paroksismal ağrıyı kontrol altına almak için yemeklerden "
                            "önce oral omeprazol süspansiyon başlamak ve sık aralıklarla rektal "
                            "gliserinli lavman uygulanmasını önermek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Uygulanan proton pompa inhibitörü ağlama süresini değiştirmedi, tekrarlayan "
                            "rektal uyarılar ise anal mukozada tahriş ve fissür gelişimine neden oldu."
                        ),
                        "teaching_point": (
                            "Kolik tedavisinde proton pompa inhibitörlerinin yeri yoktur; tekrarlayan "
                            "rektal fitil veya lavman uygulamaları mukozal hasara yol açar."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "id": "G12",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "14 Yaş",
        "gender": "Kız",
        "complaint": "Ayağa kalkınca olan baş dönmesi (dizziness) ve göz kararması",
        "history": (
            "Hasta kendisi anlatıyor: 'Bu sabah kahvaltı yapmadan okula gittim. Okul bahçesinde törende "
            "güneşin altında beklerken ve evde yataktan hızlı kalktığımda bir anda başım döndü, gözlerim "
            "karardı ve kulaklarım uğuldadı. Oturunca 1-2 dakika içinde hemen geçti. Bayılıp yere düşmedim, "
            "kasılma olmadı, kalbimde çarpıntı veya göğüs ağrısı hissetmedim. Son zamanlarda su içmeyi de "
            "çok unutuyorum.'"
        ),
        "final_diagnosis": "Ortostatik Hipotansiyon ve Vazovagal Presenkop (Postüral İntolerans)",
        "disposition": "Yeşil Alandan Oral Hidrasyon/Tuz Dengesi ve Postüral Manevra Eğitimi ile Taburculuk",
        "case_pearl": (
            "Adölesanlarda yatarken veya otururken ayağa kalkmakla ya da uzun süre ayakta kalmakla gelişen, "
            "oturunca hızla düzelen baş dönmesi ve göz kararmasında (presenkop) en sık neden ortostatik "
            "hipotansiyon (ayağa kalktıktan sonraki 3 dakika içinde sistolik TA ≥20 mmHg veya diyastolik "
            "TA ≥10 mmHg düşüş) ve vazovagal mekanizmadır. Kardiyak kırmızı bayraklar (egzersiz sırasında "
            "senkop, yatar pozisyonda senkop, ailede <40 yaş ani kardiyak ölüm, patolojik üfürüm, anormal "
            "EKG) mutlaka dışlanmalıdır."
        ),
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": (
                    "Sabah açken ve ayağa kalktığında başlayan baş dönmesi ile göz kararması tarifleyen "
                    "on dört yaşındaki hastada ilk değerlendirmede ne yapılmalıdır?"
                ),
                "options": [
                    {
                        "text": (
                            "Şikayetin iç kulak kaynaklı periferik vestibüler patolojiye bağlı olduğunu "
                            "düşünerek yatak başında Dix-Hallpike testi ile Epley repozisyon manevrası "
                            "uygulamak ve hastaya oral dimenhidrinat tablet vermek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Dix-Hallpike testinde nistagmus veya rotatuar vertigo tetiklenmedi; verilen "
                            "antihistaminik ise hastada uyku hali ve halsizlik artışına neden oldu."
                        ),
                        "teaching_point": (
                            "Baş dönmesi ile başvuran hastada önce etrafın dönmesi ve nistagmus ile giden "
                            "gerçek vertigo ile ayağa kalkınca göz kararmasıyla seyreden postüral "
                            "sersemlik ayırt edilmelidir."
                        ),
                    },
                    {
                        "text": (
                            "Akut hipovolemi ve dolaşım bozukluğu varsayımıyla postüral kan basıncı ölçümü "
                            "beklemeden hastayı hemen Sarı Alana almak ve hızlı intravenöz izotonik salin "
                            "bolusu tedavisi başlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "İstirahatte yaşamsal bulguları tamamen normal olan ve oral alımı açık hastaya "
                            "gereksiz damar yolu açıldı; postüral kan basıncı değişimi ise kayıt altına "
                            "alınamadı."
                        ),
                        "teaching_point": (
                            "Genel durumu iyi ve istirahat hemodinamisi stabil olan hastada öncelikle "
                            "yatar ve ayakta kan basıncı farkı dökümante edilmelidir."
                        ),
                    },
                    {
                        "text": (
                            "Yatar pozisyonda ve ayağa kalktıktan üç dakika sonra kan basıncı ile nabız "
                            "ölçmek, kardiyak oskültasyon, nörolojik muayene ve kardiyak kırmızı bayrak "
                            "sorgulaması yapmak"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Postüral baş dönmesi ve göz kararması yakınmasında yatarak ve ayakta 3. "
                            "dakika kan basıncı-nabız ölçümü, kardiyak kırmızı bayrak sorgulaması ve "
                            "nörolojik/vestibüler muayene temel basamaktır."
                        ),
                        "new_finding": (
                            "Yatar pozisyonda TA: 106/66 mmHg, KTA: 76/dk; ayağa kalktıktan 3. dakikada "
                            "TA: 84/50 mmHg, KTA: 104/dk ölçüldü ve hasta bu sırada hafif göz kararması "
                            "tarifledi. Kardiyak oskültasyonda ritim düzenli, ek ses veya üfürüm yok. "
                            "Serebellar testler, yürüyüş ve kraniyal sinir muayenesi doğal; nistagmus "
                            "saptanmadı. Egzersizle senkop veya ailede erken yaş ani kardiyak ölüm öyküsü yok."
                        ),
                    },
                    {
                        "text": (
                            "Kısa süreli görsel kararma ve uğuldama tarifini atipik jeneralize nöbet "
                            "eşdeğeri kabul ederek ayrıntılı fundus ve kraniyal sinir muayenesi sonrası "
                            "acil çocuk nöroloji konsültasyonu istemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Nörolojik muayenesi tamamen normal olan ve bilinç kaybı, kasılma veya "
                            "postiktal konfüzyon tariflemeyen hastada nöroloji konsültasyonu patoloji "
                            "saptamadı."
                        ),
                        "teaching_point": (
                            "Ayağa kalkmakla tetiklenen ve oturunca dakikalar içinde düzelen göz "
                            "kararması ile kulak uğuldaması epileptik aura değil, postüral serebral "
                            "hipoperfüzyon bulgusudur."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Görüntüleme Planlaması",
                "question": (
                    "Ayağa kalkmakla sistolik kan basıncında 22 mmHg düşüş saptanan ve nörolojik "
                    "muayenesi normal olan bu adölesan kız hastada hangi tetkikler istenmelidir?"
                ),
                "options": [
                    {
                        "text": (
                            "Aritmi ve iletim bozukluklarını dışlamak için on iki derivasyonlu "
                            "elektrokardiyografi çekmek, parmak ucu kan şekeri ve tam kan sayımı bakmak"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Bayılma veya bayılayazma yakınmasıyla başvuran her çocuk ve ergende 12 "
                            "derivasyonlu EKG ve kan şekeri; adölesan kızlarda ise menstrüel kanamaya "
                            "bağlı demir eksikliği anemisi açısından hemoglobin kontrolü önerilir."
                        ),
                        "new_finding": (
                            "12 Derivasyonlu EKG: Normal sinüs ritmi, hız 78/dk, QTc: 410 ms, PR ve QRS "
                            "süreleri normal, delta dalgası veya ST-T değişikliği yok. Parmak ucu kan "
                            "şekeri: 92 mg/dL. Hemogram: Hb 12.6 g/dL, Hct %38, MCV 84 fL."
                        ),
                    },
                    {
                        "text": (
                            "Serebral hipoperfüzyon ve intrakraniyal patolojiyi dışlamak amacıyla "
                            "kontrastsız beyin bilgisayarlı tomografisi, bilateral karotis-vertebral "
                            "arter Doppler ultrasonografisi ve uyanıklık elektroensefalografisi planlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Çekilen beyin BT, boyun Doppler USG ve EEG tamamen normal sonuçlandı; ancak "
                            "hasta gereksiz radyasyon aldı ve temel ritim değerlendirmesi gecikti."
                        ),
                        "teaching_point": (
                            "Fokal nörolojik defisiti veya kafa travması olmayan postüral baş dönmesi "
                            "olgularında kraniyal görüntüleme, Doppler USG ve EEG endikasyonu yoktur."
                        ),
                    },
                    {
                        "text": (
                            "Yapısal kalp hastalığı ve miyokardit olasılığını acil serviste ekarte etmek "
                            "için yatak başı transtorasik ekokardiyografi, serum troponin-I, D-dimer ve "
                            "tiroid fonksiyon testleri istemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Troponin-I, D-dimer ve TSH düzeyleri ile ekokardiyografi tamamen normal "
                            "bulundu; acil serviste gereksiz tetkik maliyeti ve bekleme süresi oluştu."
                        ),
                        "teaching_point": (
                            "Kardiyak kırmızı bayrağı ve üfürümü olmayan, EKG'si normal saptanan "
                            "hastalarda acil ekokardiyografi ve kardiyak biyobelirteç taraması "
                            "önerilmez."
                        ),
                    },
                    {
                        "text": (
                            "Tipik postüral kan basıncı düşüşü saptandığından elektrokardiyografi ve "
                            "kapiller kan şekeri dahil hiçbir tetkik yapmadan hastayı doğrudan sözlü "
                            "önerilerle taburcu etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Hasta EKG çekilmeden taburcu edildi; oysa konjenital uzun QT veya "
                            "preeksitasyon sendromlarını dışlamak için bazal EKG kaydı kılavuz "
                            "zorunluluğuydu."
                        ),
                        "teaching_point": (
                            "Tablo ne kadar tipik görünürse görünsün, ilk kez başvuran presenkop/senkop "
                            "hastalarında 12 derivasyonlu EKG ve kapiller glukoz ölçümü atlanmamalıdır."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı ve Ayırıcı Değerlendirme",
                "question": (
                    "Postüral kan basıncı düşüşü, normal elektrokardiyografi ve normal hemoglobin "
                    "değerleri ışığında bu hastada en olası tanınız nedir?"
                ),
                "options": [
                    {
                        "text": "Uzun QT Sendromuna Bağlı Kardiyojenik Senkop",
                        "is_correct": False,
                        "scenario_update": (
                            "Hastanın EKG'sinde QTc 410 ms ile normal sınırlardadır ve eforla veya "
                            "ani sesle tetiklenen prodromsuz bayılma öyküsü bulunmamaktadır."
                        ),
                        "teaching_point": (
                            "Kardiyojenik senkop genellikle prodromsuz olarak egzersiz sırasında veya "
                            "yatar pozisyonda gelişir ve patolojik EKG ya da aile öyküsü eşlik eder."
                        ),
                    },
                    {
                        "text": "Ortostatik Hipotansiyon ve Vazovagal Presenkop",
                        "is_correct": True,
                        "explanation": (
                            "Ayağa kalktıktan sonraki 3 dakika içinde sistolik kan basıncında ≥20 mmHg "
                            "veya diyastolik kan basıncında ≥10 mmHg düşüş olması ortostatik "
                            "hipotansiyonu tanımlar; açlık ve yetersiz sıvı alımı vazovagal/ortostatik "
                            "presenkopu kolaylaştırır."
                        ),
                        "new_finding": (
                            "Kesin Tanı: Ortostatik Hipotansiyon ve Vazovagal Presenkop."
                        ),
                    },
                    {
                        "text": "Benign Paroksismal Pozisyonel Vertigo",
                        "is_correct": False,
                        "scenario_update": (
                            "Hastada baş hareketleriyle tetiklenen rotatuar baş dönmesi veya nistagmus "
                            "yoktur; semptomlar yalnızca ayağa kalkınca ve uzun süre ayakta kalınca "
                            "oluşmaktadır."
                        ),
                        "teaching_point": (
                            "Periferik vertigoda kan basıncı düşüşü olmaz, etrafın dönmesi hissi ve "
                            "pozisyonel nistagmus saptanır."
                        ),
                    },
                    {
                        "text": "Postüral Ortostatik Taşikardi Sendromu (POTS)",
                        "is_correct": False,
                        "scenario_update": (
                            "Adölesanlarda POTS tanısı için ortostatik hipotansiyon OLMAKSIZIN kalp "
                            "hızının ≥40/dk artması gerekir; bu hastada ise belirgin kan basıncı düşüşü "
                            "mevcuttur."
                        ),
                        "teaching_point": (
                            "POTS tanısı ancak ilk 3 dakikada klasik ortostatik kan basıncı düşüşü "
                            "(≥20/10 mmHg) dışlandıktan sonra aşırı taşikardi (≥40/dk artış) varlığında "
                            "konulabilir."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Tedavi, İzlem ve Taburculuk Planı",
                "question": (
                    "Ortostatik hipotansiyon ve vazovagal presenkop tanısı alan bu hastanın acil servis "
                    "yönetimi ve taburculuk eğitiminde en doğru yaklaşım hangisidir?"
                ),
                "options": [
                    {
                        "text": (
                            "Kan basıncı düşüşünü hızla düzeltmek için birinci basamak tedavi olarak oral "
                            "fludrokortizon asetat ve midodrin tablet reçete edip iki hafta sıkı tuz "
                            "kısıtlaması önermek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Yaşam tarzı önlemleri denenmeden başlanan mineralokortikoid ve alfa-agonist "
                            "tedavi baş ağrısı ve supin hipertansiyona yol açtı; tuz kısıtlaması ise "
                            "hipovolemiyi derinleştirdi."
                        ),
                        "teaching_point": (
                            "Adölesan ortostatik hipotansiyonunda farmakolojik ajanlar (fludrokortizon, "
                            "midodrin) ilk basamak değildir; ayrıca tuz kısıtlaması değil, tuz desteğinin "
                            "artırılması gerekir."
                        ),
                    },
                    {
                        "text": (
                            "Refleks taşikardiyi baskılamak amacıyla düşük doz oral propranolol tedavisi "
                            "başlamak, okulda beden eğitimi derslerini tamamen yasaklamak ve uzun süreli "
                            "yatak istirahati raporu düzenlemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Verilen beta-bloker kompansatuar kalp hızı yanıtını baskılayarak hastanın "
                            "ayağa kalktığında daha ağır hipotansiyon yaşamasına ve kondisyon kaybına "
                            "neden oldu."
                        ),
                        "teaching_point": (
                            "Hipovolemiye bağlı ortostatik hipotansiyonda beta-blokerler kompansatuar "
                            "taşikardiyi engelleyerek semptomları kötüleştirir; uzun süreli yatak "
                            "istirahati ise ortostatik toleransı daha da bozar."
                        ),
                    },
                    {
                        "text": (
                            "Hastayı monitörize gözlem yatağında yirmi dört saat yatırarak seri kardiyak "
                            "enzim takibi yapmak ve taburculuk öncesi mutlaka eğik masa (tilt-table) "
                            "provokasyon testi uygulamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Kardiyak kırmızı bayrağı olmayan hasta gereksiz yere bir gün hastanede "
                            "tutuldu; tüm seri troponin değerleri normal kaldı."
                        ),
                        "teaching_point": (
                            "Tipik öyküsü ve ortostatik vital bulgusu olan, EKG'si normal hastalarda "
                            "hastaneye yatış veya acil tilt-table testi endikasyonu yoktur."
                        ),
                    },
                    {
                        "text": (
                            "Oral sıvı desteği sağlamak, günlük su ve tuz alımını artırmayı, kahvaltıyı "
                            "atlamamayı, kademeli ayağa kalkmayı ve prodromda izometrik karşı-basınç "
                            "manevralarını öğreterek taburcu etmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Adölesan ortostatik hipotansiyon ve vazovagal presenkopta birinci basamak "
                            "tedavi yeterli hidrasyon (2-2.5 L/gün su), uygun tuz alımı, düzenli "
                            "kahvaltı, yataktan kademeli kalkış ve prodrom anında bacak çaprazlama/çömelme "
                            "gibi izometrik karşı-basınç manevralarıdır."
                        ),
                        "new_finding": (
                            "Acil serviste oral sıvı alımı sonrası semptomları tamamen düzelen hasta, "
                            "postüral önlemler ve kırmızı bayrak eğitimi verilerek taburcu edildi."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "id": "G13",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "20 Aylık",
        "gender": "Erkek",
        "complaint": "Gece aniden başlayan havlar tarzda kaba öksürük ve ses kısıklığı",
        "history": (
            "Annesi ve babası gece 02:00'de getiriyor: 'Gündüz sadece hafif burun akıntısı vardı. Gece "
            "yarısı bir anda köpek havlaması ya da fok balığı sesi gibi çok kaba bir öksürükle uyandı, "
            "ağlarken sesi kalın ve boğuk çıkıyor. Soğuk gece havasında arabaya götürürken biraz rahatladı, "
            "şu an kucağımızda sakin oturuyor, salya akışı veya yutma güçlüğü yok.'"
        ),
        "final_diagnosis": "Hafif Akut Viral Laringotrakeit (Hafif Krup - Westley Skoru 1)",
        "disposition": "Yeşil Alandan Tek Doz Oral Deksametazon ve Aile Eğitimi ile Taburculuk",
        "case_pearl": (
            "İstirahatte stridoru ve göğüs çekilmesi olmayan, yalnızca ağlamakla veya öksürükle kaba sesi "
            "ve stridoru duyulan viral laringotrakeit 'Hafif Krup' (Westley skoru ≤2) olarak "
            "sınıflandırılır. Hafif krupta dahi tek doz (0.15 - 0.6 mg/kg) oral deksametazon semptom "
            "süresini, uyku bölünmesini ve acile tekrar başvuruyu anlamlı biçimde azaltır; istirahatte "
            "stridor yoksa nebülize adrenalin uygulanmaz."
        ),
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": (
                    "Gece aniden başlayan havlar tarzda kaba öksürük ve ses kısıklığı ile getirilen "
                    "yirmi aylık bu çocukta ilk muayene yaklaşımınız nasıl olmalıdır?"
                ),
                "options": [
                    {
                        "text": (
                            "Üst hava yolu ödeminin derecesini doğrudan görmek amacıyla çocuğu muayene "
                            "masasına yatırıp abeslang yardımıyla derin orofarenks ve epiglot muayenesi "
                            "yapmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Zorla yapılan dil basacağı muayenesi çocuğu şiddetli ağlattı; artan "
                            "negatif intratorasik basınç ve türbülan hava akımı nedeniyle inspiratuar "
                            "stridor belirginleşti."
                        ),
                        "teaching_point": (
                            "Akut üst hava yolu darlığı bulguları olan çocuklarda ağlama ve ajitasyon "
                            "türbülan akımı artırarak darlığı ağırlaştırır; zorlu ağız içi muayeneden "
                            "kaçınılmalıdır."
                        ),
                    },
                    {
                        "text": (
                            "Akut üst hava yolu obstrüksiyonu riski nedeniyle muayeneyi beklemeden "
                            "hastayı Sarı Alana devretmek, damar yolu açmak ve hemen nebülize adrenalin "
                            "tedavisi başlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "İstirahatte rahat olan çocuğa damar yolu açılırken gelişen şiddetli ağlama "
                            "solunum iş yükünü artırdı; endikasyon dışı verilen nebülize adrenalin ise "
                            "taşikardiye ve gereksiz dört saatlik gözlem zorunluluğuna yol açtı."
                        ),
                        "teaching_point": (
                            "İstirahatte stridoru ve çekilmesi olmayan, genel durumu iyi çocuklarda "
                            "ağrılı damar yolu girişimi ve nebülize adrenalin endikasyonu yoktur."
                        ),
                    },
                    {
                        "text": (
                            "Gece başlayan kaba öksürüğü alt hava yolu darlığı olarak değerlendirip "
                            "öncelikle kurtarıcı nebülize salbutamol uygulamak ve yirmi dakika sonra "
                            "oskültasyonu tekrarlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Uygulanan nebülize beta-2 agonist üst hava yolundaki mukozal ödem üzerinde "
                            "hiçbir etki göstermedi ve çocukta huzursuzluk ile taşikardi yaptı."
                        ),
                        "teaching_point": (
                            "Havlar tarzda kaba öksürük ve ses kısıklığı alt hava yolu bronkospazmını "
                            "değil, subglottik üst hava yolu ödemini gösterir; bronkodilatörler etkisizdir."
                        ),
                    },
                    {
                        "text": (
                            "Çocuğu ağlatmadan anne kucağında genel görünümünü, istirahatte stridor ve "
                            "çekilme varlığını, akciğer havalanmasını, satürasyonu değerlendirmek ve salya "
                            "akışını dışlamak"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Üst hava yolu darlığı düşünülen çocuklarda değerlendirme çocuğu huzursuz "
                            "etmeden anne kucağında yapılmalı; istirahatte stridor, çekilmeler ve ağır "
                            "bakteriyel üst hava yolu enfeksiyonu kırmızı bayrakları (salya akışı, "
                            "toksik görünüm, tripod pozisyonu) kontrol edilmelidir."
                        ),
                        "new_finding": (
                            "Yaşamsal bulgular: Ateş 37.7°C, KTA 120/dk, SS 26/dk, oda havasında SpO2 "
                            "%99. Çocuk anne kucağında sakin, etrafıyla ilgili ve cilt rengi doğal. "
                            "İstirahat halinde inspiratuar stridor duyulmuyor; yalnızca heyecanlandığında "
                            "veya öksürdüğünde kaba ses ve hafif stridor ortaya çıkıyor. Suprasternal "
                            "veya interkostal çekilme yok, her iki akciğere hava girişi eşit ve doğal. "
                            "Salya akışı, yutma güçlüğü veya toksik görünüm saptanmadı."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Görüntüleme Planlaması",
                "question": (
                    "İstirahatte stridoru, göğüs çekilmesi ve yabancı cisim aspirasyonu kuşkusu "
                    "bulunmayan, genel durumu iyi olan bu çocukta hangi tetkik yaklaşımı doğrudur?"
                ),
                "options": [
                    {
                        "text": (
                            "Subglottik daralmayı radyolojik olarak doğrulamak ve retrolaringeal "
                            "patolojileri dışlamak amacıyla ön-arka ve yan yumuşak doku boyun grafisi "
                            "ile akciğer grafisi çekmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Röntgen odasında pozisyon verilirken ağlayan çocuğun solunum sıkıntısı "
                            "arttı; çekilen grafiler klinik yönetimi hiç değiştirmedi."
                        ),
                        "teaching_point": (
                            "Tipik viral üst hava yolu darlığı tablosunda boyun veya akciğer grafisi "
                            "rutin olarak önerilmez; görüntüleme yalnızca atipik seyir, yabancı cisim "
                            "veya retrofaringeal apse şüphesinde düşünülür."
                        ),
                    },
                    {
                        "text": (
                            "Tipik klinik tablo ve normal oksijenasyon varlığında rutin boyun veya "
                            "akciğer grafisi ile kan tetkiki istemeden doğrudan tedavi planlamasına "
                            "geçmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Tipik gece başlangıçlı kaba öksürük ve ses kısıklığı tablosunda değerlendirme "
                            "tamamen kliniktir; gereksiz kan alma ve radyografi işlemleri çocuğu "
                            "ağlatarak üst hava yolu darlığını kötüleştirir."
                        ),
                        "new_finding": (
                            "Ek laboratuvar veya radyolojik tetkik istenmedi; çocuk anne kucağında sakin "
                            "kalarak tedavi basamağına geçildi."
                        ),
                    },
                    {
                        "text": (
                            "Bakteriyel süperenfeksiyonu ve solunumsal asidozu değerlendirmek üzere tam "
                            "kan sayımı, C-reaktif protein, prokalsitonin, kan kültürü ve kapiller kan "
                            "gazı çalışmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Kan alma işlemi sırasında çocuk katılarak ağladı ve inspiratuar stridoru "
                            "belirginleşti; tüm laboratuvar ve kan gazı parametreleri normal sınırlarda "
                            "geldi."
                        ),
                        "teaching_point": (
                            "Hafif seyirli ve oksijen satürasyonu normal olan hastalarda kan tetkiki "
                            "veya kan gazı alınması endike değildir; ağrılı işlemler hava yolu "
                            "obstrüksiyonunu artırır."
                        ),
                    },
                    {
                        "text": (
                            "Özgül antiviral veya antibiyotik seçimi yapabilmek için nazofaringeal "
                            "sürüntüden çoklu solunum yolu viral polimeraz zincir reaksiyonu paneli ve "
                            "boğaz kültürü istemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Nazofaringeal ve orofaringeal sürüntü işlemi çocuğu ajite etti; test "
                            "sonuçları acil servis tedavisinde hiçbir değişiklik sağlamadı."
                        ),
                        "teaching_point": (
                            "Ayaktan izlenecek hafif olgularda etken virüsü saptamaya yönelik rutin "
                            "moleküler panel veya boğaz kültürü acil yönetimi değiştirmez."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı ve Ayırıcı Değerlendirme",
                "question": (
                    "Mevcut öykü ve fizik muayene bulguları (istirahatte stridor ve çekilme olmaması, "
                    "Westley skoru 1) ile bu hastada tanınız nedir?"
                ),
                "options": [
                    {
                        "text": "Hafif Akut Viral Laringotrakeit (Krup)",
                        "is_correct": True,
                        "explanation": (
                            "Viral prodrom sonrası gece başlayan havlar tarzda öksürük ve ses kısıklığı "
                            "varlığında istirahatte stridor ve göğüs duvarı çekilmesinin olmaması "
                            "(Westley skoru ≤2) Hafif Akut Viral Krup tanısını koydurur."
                        ),
                        "new_finding": "Kesin Tanı: Hafif Akut Viral Laringotrakeit (Westley Skoru: 1).",
                    },
                    {
                        "text": "Orta-Ağır Akut Laringotrakeit (Westley Skoru ≥3)",
                        "is_correct": False,
                        "scenario_update": (
                            "Orta-ağır krup tanısı için istirahat halinde duyulan stridor ve belirgin "
                            "suprasternal/interkostal çekilmeler bulunmalıdır; bu hastada istirahatte "
                            "stridor ve çekilme yoktur."
                        ),
                        "teaching_point": (
                            "Westley skorlamasında istirahatte stridor olmaması ve çekilme bulunmaması "
                            "hastayı hafif krup grubuna sokar."
                        ),
                    },
                    {
                        "text": "Akut Bakteriyel Trakeit veya Epiglottit",
                        "is_correct": False,
                        "scenario_update": (
                            "Hastada yüksek ateş, toksik görünüm, salya akışı, yutma güçlüğü veya "
                            "pürülan hava yolu sekresyonu bulunmamaktadır."
                        ),
                        "teaching_point": (
                            "Epiglottit ve bakteriyel trakeitte yüksek ateş, toksik tablo ve ilerleyici "
                            "ağır solunum sıkıntısı ön plandadır."
                        ),
                    },
                    {
                        "text": "Akut Subglottik Yabancı Cisim Aspirasyonu",
                        "is_correct": False,
                        "scenario_update": (
                            "Öyküde ani boğulma/morarma atağı yoktur; tablo gündüz başlayan burun "
                            "akıntısı ve subfebril ateş prodromu sonrası gelişmiştir."
                        ),
                        "teaching_point": (
                            "Yabancı cisim aspirasyonu viral prodrom olmaksızın yemek veya oyun "
                            "sırasında ani başlayan boğulma ve öksürük krizi ile karakterizedir."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Tedavi, İzlem ve Taburculuk Planı",
                "question": (
                    "Hafif akut viral laringotrakeit (Westley skoru 1) tanısı koyduğunuz bu hastada en "
                    "uygun tedavi ve taburculuk yaklaşımı hangisidir?"
                ),
                "options": [
                    {
                        "text": (
                            "Tek doz oral deksametazon ile birlikte rutin bir doz nebülize L-adrenalin "
                            "uygulamak ve işlemden on beş dakika sonra hastayı doğrudan evine taburcu etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Hafif krupta endikasyon dışı nebülize adrenalin verildi; üstelik adrenalin "
                            "etkisi 2 saatte geçtiği için erken taburculuk sonrası rebound stridor riski "
                            "oluştu."
                        ),
                        "teaching_point": (
                            "Nebülize L-adrenalin yalnızca orta-ağır krupta (istirahatte stridor varlığında) "
                            "endikedir ve uygulanan her hasta rebound stridor açısından en az 2-4 saat "
                            "gözlenmeden taburcu edilemez."
                        ),
                    },
                    {
                        "text": (
                            "Sistemik steroid yan etkilerinden kaçınmak için yalnızca soğuk buhar "
                            "inhalasyonu ve nebülize salbutamol uygulamak, sekonder enfeksiyon "
                            "profilaksisi için oral amoksisilin-klavulanat reçete etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Steroid verilmeyen çocuk aynı gece sabaha karşı artan stridor ve göğüs "
                            "çekilmeleriyle acil servise orta krup tablosunda tekrar başvurdu."
                        ),
                        "teaching_point": (
                            "Hafif krupta dahi tek doz deksametazon acile tekrar başvuruyu ve "
                            "kötüleşmeyi azaltır; salbutamol ve antibiyotiklerin viral krupta yeri yoktur."
                        ),
                    },
                    {
                        "text": (
                            "Tek doz 0.15-0.6 mg/kg oral deksametazon uygulamak, nebülize adrenalin "
                            "vermeden oral alımını gözlemlemek ve istirahatte stridor gelişirse başvuru "
                            "eğitimiyle taburcu etmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Hafif krup tedavisinde altın standart tek doz 0.15-0.6 mg/kg oral "
                            "deksametazondur (oral alamıyorsa İM veya nebülize budesonid). İstirahatte "
                            "stridor olmadığı için nebülize adrenalin ve uzun süreli gözlem gerekmez."
                        ),
                        "new_finding": (
                            "Tek doz oral deksametazon sorunsuz içirildi; aileye nemli/serin hava "
                            "desteği ve kırmızı bayraklar (istirahatte stridor, çekilme, salya akışı, "
                            "morarma) anlatılarak taburcu edildi."
                        ),
                    },
                    {
                        "text": (
                            "İntramüsküler seftriakson ve metilprednizolon enjeksiyonu yaptıktan sonra "
                            "evde yedi gün kullanılmak üzere oral prednizolon şurup ve dekstrometorfan "
                            "içeren öksürük şurubu reçete etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Ağrılı enjeksiyon çocuğu şiddetli ağlatarak stridorunu artırdı; küçük "
                            "çocukta kontrendike olan antitussif şurup ise solunum depresyonu riski "
                            "yarattı."
                        ),
                        "teaching_point": (
                            "Uzun yarı ömürlü tek doz oral deksametazon yeterlidir, 7 günlük steroid "
                            "kürü gerekmez; ayrıca küçük çocuklarda santral öksürük kesiciler "
                            "kontrendikedir."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "id": "G14",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "5 Yaş",
        "gender": "Kız",
        "complaint": "Saçlı deriden ve gövdeden başlayan kaşıntılı, içi su dolu kabarcıklar ve hafif ateş",
        "history": (
            "Annesi anlatıyor: 'Dün hafif ateşi ve halsizliği oldu. Bu sabah saçlarının arasında, yüzünde ve "
            "karnında kırmızı noktalar çıktı, birkaç saat içinde üstleri su damlası gibi kabarcıklara "
            "dönüştü. Çok kaşınıyor. Anaokulunda geçen hafta iki arkadaşında da aynı döküntüler çıkmış. "
            "Aşıları eksik kalmıştı, kronik bir hastalığı yok.'"
        ),
        "final_diagnosis": "Suçiçeği (Varisella - Primer VZV Enfeksiyonu)",
        "disposition": (
            "Yeşil Alandan Semptomatik Tedavi, Aspirin/İbuprofen Yasağı Uyarıları ve İzolasyon Eğitimi "
            "ile Taburculuk"
        ),
        "case_pearl": (
            "Suçiçeğinde saçlı deri ve gövdeden başlayan (sentripetal dağılım), kaşıntılı ve aynı anda "
            "farklı evrelerde (makül, papül, 'gül yaprağı üzerinde çiğ damlası' vezikül, püstül ve krut) "
            "polimorfik lezyonlar tanı koydurucudur. Tedavide Reye sendromu riski nedeniyle Aspirin ve "
            "invaziv Grup A Streptokok / nekrotizan fasiit riskini artırdığı için İbuprofen (NSAİİ) "
            "kesinlikle verilmemeli; antipiretik olarak yalnızca Parasetamol tercih edilmelidir."
        ),
        "steps": [
            {
                "stage_title": "Enfeksiyon Kontrolü ve Fizik Muayene",
                "question": (
                    "Saçlı deriden ve gövdeden başlayan kaşıntılı su dolu kabarcıklar ile getirilen "
                    "beş yaşındaki bu çocukta ilk yaklaşımınız nasıl olmalıdır?"
                ),
                "options": [
                    {
                        "text": (
                            "Hava yolu ve temas izolasyonu önlemleri alarak saçlı deri dahil tüm "
                            "cildi, mukozaları, akciğer oskültasyonunu ve serebellar dengeyi muayene etmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Yüksek bulaştırıcılığa sahip veziküler döküntülü hastalar bekleme salonundan "
                            "derhal izole odaya alınmalı; lezyonların dağılımı/evreleri ile olası "
                            "pulmoner, nörolojik ve sekonder bakteriyel deri komplikasyonları "
                            "değerlendirilmelidir."
                        ),
                        "new_finding": (
                            "Yaşamsal bulgular: Ateş 37.8°C, KTA 98/dk, SS 20/dk, SpO2 %99. Hasta izole "
                            "muayene odasına alındı. Saçlı deri, yüz ve gövdede yoğunlaşan, "
                            "ekstremitelerde daha seyrek dağılım gösteren eritemli maküller, papüller, "
                            "ince duvarlı berrak veziküller ve erken evre krutlanmış lezyonların aynı "
                            "anda bir arada bulunduğu görüldü. Lezyon çevresinde pürülan selülit bulgusu "
                            "yok. Akciğer oskültasyonu ve serebellar denge muayenesi doğal."
                        ),
                    },
                    {
                        "text": (
                            "Döküntülerin alerjik reaksiyon olduğunu düşünerek hastayı genel bekleme "
                            "alanına almak ve muayene öncesinde intramüsküler feniramin ile deksametazon "
                            "enjeksiyonu hemen uygulatmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Bekleme salonundaki immünsüprese hastalar ve gebeler hava yoluyla bulaşan "
                            "etkene maruz kaldı; uygulanan sistemik steroid ise viral replikasyonun "
                            "ağırlaşması riskini doğurdu."
                        ),
                        "teaching_point": (
                            "Ateşli veziküler döküntüyle başvuran çocuklar bulaş riski nedeniyle ortak "
                            "bekleme salonunda tutulmamalı ve viral enfeksiyon dışlanmadan sistemik "
                            "steroid verilmemelidir."
                        ),
                    },
                    {
                        "text": (
                            "İzole lokalize deri enfeksiyonu varsayımıyla ek bulaş önlemi almadan "
                            "lezyonların üstünü steril iğne ile açıp povidon iyot solüsyonu ile pansuman "
                            "yapmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "İğne ile patlatılan veziküller çocukta şiddetli ağrıya yol açtı ve sağlam "
                            "epidermal bariyer bozulduğu için sekonder bakteriyel süperenfeksiyon ile "
                            "skar riski arttı."
                        ),
                        "teaching_point": (
                            "Veziküler döküntüler kesinlikle patlatılmaz; vezikül bütünlüğünün "
                            "korunması sekonder stafilokoksik ve streptokoksik invazyonu önler."
                        ),
                    },
                    {
                        "text": (
                            "Yaygın veziküler döküntüyü ağır sistemik bakteriyel sepsis bulgusu kabul "
                            "ederek çocuğu izolasyonsuz Sarı Alana devretmek ve hemen intravenöz "
                            "antibiyotik tedavisi hazırlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "İzolasyon önlemi alınmadan Sarı Alana alınan hasta diğer kritik hastalar "
                            "için ciddi bulaş kaynağı oluşturdu; genel durumu iyi olan çocukta sepsis "
                            "bulgusu saptanmadı."
                        ),
                        "teaching_point": (
                            "Yaşamsal bulguları stabil olan veziküler döküntülü çocuklarda öncelik "
                            "izolasyon önlemi alarak klinik muayene yapmaktır."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Görüntüleme Planlaması",
                "question": (
                    "Bağışıklığı normal, genel durumu iyi ve fizik muayenede komplikasyon bulgusu "
                    "saptanmayan beş yaşındaki bu hastada hangi tetkik yaklaşımı uygundur?"
                ),
                "options": [
                    {
                        "text": (
                            "Etkeni kesinleştirmek ve sistemik yayılımı taramak amacıyla vezikül "
                            "sıvısından polimeraz zincir reaksiyonu testi, viral seroloji, tam kan "
                            "sayımı ve karaciğer enzimleri istemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Kan alma işlemi çocuğun huzursuzluğunu artırdı; lökosit sayısı hafif "
                            "düşük, transaminazlar normal geldi ve PCR sonucu günler sonra çıkacağı "
                            "için acil yönetime katkı sağlamadı."
                        ),
                        "teaching_point": (
                            "İmmünkompetan çocuklarda tipik polimorfik veziküler döküntü varlığında "
                            "rutin kan tetkiki, seroloji veya PCR doğrulaması gerekmez."
                        ),
                    },
                    {
                        "text": (
                            "Subklinik viral pnömoni ve bakteriyel süperenfeksiyonu dışlamak için "
                            "arka-ön akciğer grafisi, kan kültürü, C-reaktif protein ve eritrosit "
                            "sedimantasyon hızı çalışmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Solunum sıkıntısı olmayan çocuğun radyoloji ünitesine gönderilmesi hastane "
                            "içi bulaş riskine yol açtı; akciğer grafisi ve akut faz reaktanları normal "
                            "bulundu."
                        ),
                        "teaching_point": (
                            "Takipne, öksürük, hipoksi veya dirençli yüksek ateş gibi komplikasyon "
                            "bulguları olmayan vakalarda akciğer grafisi ve kan kültürü istenmez."
                        ),
                    },
                    {
                        "text": (
                            "Veziküler lezyon tabanından Tzanck yayması ve bakteriyel yara kültürü "
                            "alarak sonuçlar çıkana kadar hastayı acil servis gözlem odasında izlemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Pürülan akıntısı olmayan berrak vezikülden alınan kültür üreme göstermedi; "
                            "hastanın acil serviste bekletilmesi bulaş süresini uzattı."
                        ),
                        "teaching_point": (
                            "Sekonder bakteriyel enfeksiyon bulgusu olmayan tipik vakalarda yara kültürü "
                            "veya Tzanck yayması rutin acil pratiğinde endike değildir."
                        ),
                    },
                    {
                        "text": (
                            "Tipik polimorfik veziküler döküntü ve temas öyküsü bulunduğundan ek "
                            "laboratuvar, seroloji veya görüntüleme tetkiki istemeden klinik "
                            "değerlendirme ile ilerlemek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Saçlı deriyi ve gövdeyi tutan, aynı anda farklı evrelerdeki veziküler "
                            "lezyonlarla seyreden klasik tabloda değerlendirme tamamen kliniktir; "
                            "komplikasyonsuz immünkompetan hastada tetkik gerekmez."
                        ),
                        "new_finding": (
                            "Ek laboratuvar veya görüntüleme tetkiki istenmedi; hastane içi bulaş "
                            "önlenerek doğrudan klinik yönetim aşamasına geçildi."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı ve Ayırıcı Değerlendirme",
                "question": (
                    "Saçlı deriyi tutan sentripetal dağılımlı ve aynı anda farklı evrelerdeki (makül, "
                    "papül, vezikül, krut) polimorfik döküntü bulgularıyla tanınız nedir?"
                ),
                "options": [
                    {
                        "text": "El-Ayak-Ağız Hastalığı (Enteroviral Veziküler Ekzantem)",
                        "is_correct": False,
                        "scenario_update": (
                            "El-ayak-ağız hastalığında veziküller ağız mukozası, avuç içi, ayak tabanı "
                            "ve gluteal bölgede yoğunlaşır (akral dağılım); saçlı deriden başlayan "
                            "polimorfik gövde döküntüsü beklenmez."
                        ),
                        "teaching_point": (
                            "Sentripetal (gövde ve saçlı deri ağırlıklı) ve farklı evrelerdeki "
                            "kaşıntılı veziküller el-ayak-ağız hastalığından ayırt ettiricidir."
                        ),
                    },
                    {
                        "text": "Suçiçeği (Primer Varisella Enfeksiyonu)",
                        "is_correct": True,
                        "explanation": (
                            "Kreş temas öyküsü sonrası saçlı deri ve gövdeden başlayan, aynı anda "
                            "makül, papül, berrak vezikül ve krut evrelerinde bulunan kaşıntılı "
                            "polimorfik döküntü Suçiçeği (Varisella) için patognomoniktir."
                        ),
                        "new_finding": "Kesin Tanı: Suçiçeği (Varisella).",
                    },
                    {
                        "text": "Büllöz İmpetigo (Stafilokoksik Deri Enfeksiyonu)",
                        "is_correct": False,
                        "scenario_update": (
                            "Büllöz impetigoda gevşek duvarlı büyük büller ve açıldığında vernik benzeri "
                            "sarı krutlar görülür; saçlı deriden başlayan yaygın simetrik çiğ damlası "
                            "veziküllerle seyretmez."
                        ),
                        "teaching_point": (
                            "Büllöz impetigo lokalize veya asimetrik kümeler halinde başlar; tüm gövde "
                            "ve saçlı deriyi tutan polimorfik veziküler ekzantem varisella lehinedir."
                        ),
                    },
                    {
                        "text": "Papüler Ürtiker ve Yaygın Böcek Isırığı",
                        "is_correct": False,
                        "scenario_update": (
                            "Papüler ürtiker genellikle giysi dışı açık ekstremite bölgelerinde "
                            "gruplaşan ürtikeryal papüllerle seyreder; ateş prodromu, mukoza/saçlı deri "
                            "tutulumu ve kreş salgını öyküsü varisellayı gösterir."
                        ),
                        "teaching_point": (
                            "Saçlı deri tutulumu ve eritemli zeminde ince duvarlı veziküllerin hızlıca "
                            "krutlanması papüler ürtikerden ayrımda en önemli klinik ipucudur."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Tedavi, İlaç Güvenliği ve Taburculuk Planı",
                "question": (
                    "İmmünkompetan beş yaşındaki bu suçiçeği hastasında reçete düzenleme ve taburculuk "
                    "eğitiminde en doğru yaklaşım hangisidir?"
                ),
                "options": [
                    {
                        "text": (
                            "Dirençli ateşi ve inflamasyonu kontrol altına almak için parasetamol ile "
                            "dönüşümlü oral ibuprofen süspansiyon başlamak ve lezyonlara topikal "
                            "betametazon krem sürülmesini önermek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Suçiçeğinde kullanılan ibuprofen ve topikal steroid, lezyon yerlerinde "
                            "invaziv Grup A Streptokok enfeksiyonu ve nekrotizan fasiit gelişme "
                            "riskini ciddi oranda artırdı!"
                        ),
                        "teaching_point": (
                            "Suçiçeğinde İbuprofen ve diğer NSAİİ'ler ağır nekrotizan yumuşak doku "
                            "enfeksiyonu riskini artırdığı için, topikal steroidler ise lokal bağışıklığı "
                            "baskıladığı için kontrendikedir."
                        ),
                    },
                    {
                        "text": (
                            "Ateş için yalnızca parasetamol, kaşıntı için oral antihistaminik vermek; "
                            "aspirin ve ibuprofenden kaçınılmasını, tırnak kesimini ve lezyonlar "
                            "kabuklanana dek izolasyonu anlatmak"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Sağlıklı 12 yaş altı çocuklarda suçiçeği tedavisi semptomatiktir: ateş "
                            "için sadece parasetamol, kaşıntı için oral antihistaminik ve ılık duş "
                            "önerilir. Reye sendromu nedeniyle Aspirin ve nekrotizan fasiit riski "
                            "nedeniyle İbuprofen kesinlikle yasaklanmalı, tüm lezyonlar krutlanana "
                            "kadar okul izolasyonu sağlanmalıdır."
                        ),
                        "new_finding": (
                            "Parasetamol ve oral antihistaminik reçete edildi; ilaç güvenliği, cilt "
                            "hijyeni, izolasyon süresi ve kırmızı bayraklar (ataksi, takipne, lezyon "
                            "çevresinde hızla yayılan kızarıklık/ağrı) anlatılarak taburcu edildi."
                        ),
                    },
                    {
                        "text": (
                            "Sağlıklı her okul öncesi çocukta komplikasyonları önlemek amacıyla rutin "
                            "beş gün yüksek doz oral asiklovir, profilaktik oral sefaleksin ve talk "
                            "pudrası reçete etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Lezyonların üzerine sürülen talk pudrası bakteriyel kolonizasyon için "
                            "zemin oluşturdu; sağlıklı 5 yaş çocukta rutin antiviral ve profilaktik "
                            "antibiyotik gereksiz yan etkilere yol açtı."
                        ),
                        "teaching_point": (
                            "Komplikasyonsuz sağlıklı 12 yaş altı çocuklarda rutin oral asiklovir veya "
                            "profilaktik antibiyotik önerilmez; pudra/talk kullanımı ise sekonder "
                            "bakteriyel enfeksiyon riskini artırır."
                        ),
                    },
                    {
                        "text": (
                            "Ateş kontrolü için asetilsalisilik asit (aspirin) vermek, kaşıntıyı "
                            "azaltmak için veziküllerin üzerine yoğun çinko oksitli pomad kapatmak ve "
                            "ateş düşünce okula dönüşe izin vermek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Verilen aspirin akut ensefalopati ve karaciğer yağlanması (Reye sendromu) "
                            "riskini tetikledi; kabuklanma tamamlanmadan okula dönüş ise salgının "
                            "yayılmasına yol açtı."
                        ),
                        "teaching_point": (
                            "Suçiçeğinde aspirin Reye sendromu nedeniyle mutlak kontrendikedir; "
                            "bulaştırıcılık ise ateşin düşmesiyle değil, tüm veziküllerin kabuklanmasıyla "
                            "sona erer."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "id": "G15",
        "category": "👁️ Göz Şikayetleri",
        "age": "3 Yaş",
        "gender": "Kız",
        "complaint": "Her iki gözde kızarıklık, sulanma, sabah kirpiklerde çapaklanma ve burun akıntısı",
        "history": (
            "Annesi anlatıyor: '2 gündür burnu akıyor ve hafif hapşırıyordu. Dün sağ gözü pembeleşti ve "
            "sulandı, bu sabah uyandığında iki gözünde de sulu-hafif çapaklanma vardı. Göz kapakları şiş "
            "değil, gözünü rahatça hareket ettiriyor, ışığa bakabiliyor ve görmesinde bir sorun yok. Ateşi "
            "37.3°C.'"
        ),
        "final_diagnosis": "Akut Adenoviral (Viral) Konjonktivit",
        "disposition": "Yeşil Alandan Göz Temizliği, Destek Tedavisi ve Hijyen Eğitimi ile Taburculuk",
        "case_pearl": (
            "Çocuklarda burun akıntısı, hapşırık ve preauriküler lenfadenopatinin eşlik ettiği, bir gözden "
            "başlayıp diğerine geçen hiperemi ve sulu-serömüköz akıntı çoğunlukla viral (özellikle "
            "Adenovirus) konjonktivittir. Muayenede orbital selülit (göz kapağı ödemi, proptozis, "
            "ağrılı/kısıtlı göz hareketleri), korneal tutulum/herpes (korneal bulanıklık, şiddetli fotofobi) "
            "ve eşlik edebilecek akut otitis media mutlaka dışlanmalıdır. Topikal anestezik veya steroidli "
            "göz damlaları acil serviste kesinlikle reçete edilmez."
        ),
        "steps": [
            {
                "stage_title": "Oftalmolojik ve Sistemik Fizik Muayene",
                "question": (
                    "Üst solunum yolu semptomları eşlik eden bilateral göz kızarıklığı ve sulanma ile "
                    "getirilen üç yaşındaki çocukta ilk muayenede neleri değerlendirmelisiniz?"
                ),
                "options": [
                    {
                        "text": (
                            "Derin orbital enfeksiyon olasılığını hızla dışlamak amacıyla fizik muayene "
                            "öncesinde hastayı radyolojiye göndererek kontrastlı orbital bilgisayarlı "
                            "tomografi çekmek ve damar yolu açmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Kapak ödemi, proptozisi veya göz hareket kısıtlılığı olmayan üç yaşındaki "
                            "çocukta çekilen orbital BT tamamen normal çıktı ve lens dokusu gereksiz "
                            "radyasyona maruz kaldı."
                        ),
                        "teaching_point": (
                            "Orbital BT yalnızca proptozis, oftalmopleji, ağrılı göz hareketleri, görme "
                            "azalması veya ağır periorbital ödem gibi orbital selülit bulguları varsa "
                            "çekilir."
                        ),
                    },
                    {
                        "text": (
                            "Göz hareketlerinin her yöne açıklığını ve ağrısızlığını, periorbital ödemi, "
                            "kornea saydamlığını, ışık refleksini, preauriküler lenf nodlarını ve kulak "
                            "zarlarını muayene etmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Kırmızı gözle başvuran çocukta görmeyi ve yaşamı tehdit eden durumları "
                            "(orbital selülit, korneal ülser/keratit) ve eşlik edebilecek orta kulak "
                            "enfeksiyonunu dışlamak için göz hareketleri, kornea saydamlığı, preauriküler "
                            "lenf nodu ve otoskopi mutlaka değerlendirilmelidir."
                        ),
                        "new_finding": (
                            "Yaşamsal bulgular: Ateş 37.3°C, KTA 104/dk. Bilateral bulber ve tarsal "
                            "konjonktivada belirgin hiperemi ve sulu-serömüköz sekresyon mevcut. "
                            "Periorbital ödem, kapak endürasyonu veya proptozis yok. Göz küresi "
                            "hareketleri her yöne tam ve ağrısız. Kornea saydam, floresein boyanma "
                            "defekti yok, pupiller izokorik ve ışık refleksi bilateral doğal. Sağ "
                            "preauriküler bölgede 0.8 cm mobil hassas lenf nodu palpe edildi; bilateral "
                            "timpanik membranlar doğal."
                        ),
                    },
                    {
                        "text": (
                            "Kızarıklık ve batma hissini hızla gidermek için kornea muayenesi yapmadan "
                            "acil serviste deksametazon içeren göz damlası ve lokal anestezik damla "
                            "uygulamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Kornea bütünlüğü değerlendirilmeden uygulanan topikal steroid ve anestezik "
                            "damla epitel iyileşmesini baskılayarak korneal ülserasyon riski oluşturdu."
                        ),
                        "teaching_point": (
                            "Korneal epitel defekti ve herpetik keratit dışlanmadan kırmızı göze "
                            "kesinlikle kortikosteroidli damla uygulanmaz."
                        ),
                    },
                    {
                        "text": (
                            "Çocuğu huzursuz etmemek için göz kapaklarını ve kulak zarlarını açmadan "
                            "yalnızca dışarıdan gözlem yapmak ve doğrudan oral geniş spektrumlu "
                            "antibiyotik reçete etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Kornea ve kulak muayenesi atlandı; yüzeyel mukozal tablo için verilen "
                            "sistemik antibiyotik ise ishal dışında hiçbir etki göstermedi."
                        ),
                        "teaching_point": (
                            "Göz kızarıklığı ile başvuran çocuklarda kornea saydamlığı ve eşlik "
                            "edebilecek akut otit açısından otoskopik muayene ihmal edilmemelidir."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Görüntüleme Planlaması",
                "question": (
                    "Korneası saydam, göz hareketleri tam ve ağrısız, otoskopisi normal olan üç "
                    "yaşındaki bu hastada hangi tetkik yaklaşımı doğrudur?"
                ),
                "options": [
                    {
                        "text": (
                            "Etken mikroorganizmayı ve antibiyotik duyarlılığını saptamak amacıyla her "
                            "iki alt forniksten bakteriyel kültür, Gram boyama ve klamidyal antijen "
                            "taraması istemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Alınan oküler sürüntü örneklerinde patojen bakteri üremedi; kültür sonucu "
                            "48 saat sonra çıktığı için acil servis yönetimine hiçbir katkı sağlamadı."
                        ),
                        "teaching_point": (
                            "Yenidoğan dönemi dışında ve hiperakut pürülan (gonokoksik) akıntı şüphesi "
                            "olmayan akut çocukluk çağı olgularında rutin sürüntü kültürü önerilmez."
                        ),
                    },
                    {
                        "text": (
                            "Sistemik inflamatuar yanıtı ve gizli bakteriyemiyi değerlendirmek üzere tam "
                            "kan sayımı, C-reaktif protein, eritrosit sedimantasyon hızı ve kan kültürü "
                            "çalışmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Genel durumu iyi ve ateşsiz çocukta yapılan damar girişimi ağlamaya yol "
                            "açtı; tüm hemogram ve akut faz değerleri normal sınırlarda geldi."
                        ),
                        "teaching_point": (
                            "Komplike olmayan yüzeyel oküler mukozal enfeksiyonlarda sistemik kan "
                            "tahlili ve kan kültürü endikasyonu yoktur."
                        ),
                    },
                    {
                        "text": (
                            "Subklinik derin doku yayılımını ve sinüzit komplikasyonunu dışlamak "
                            "amacıyla paranazal sinüs grafisi ve yüzeyel periorbital yumuşak doku "
                            "ultrasonografisi planlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Periorbital ödemi olmayan üç yaşındaki çocukta çekilen sinüs grafisi ve "
                            "yüzeyel ultrasonografi normal raporlandı."
                        ),
                        "teaching_point": (
                            "Periorbital şişlik, eritem veya göz hareket kısıtlılığı olmayan çocuklarda "
                            "görüntüleme tetkiki yapılmaz."
                        ),
                    },
                    {
                        "text": (
                            "Kırmızı bayrak bulgusu bulunmayan bu tabloda ek kan tahlili, radyolojik "
                            "görüntüleme veya oküler sürüntü kültürü istemeden klinik olarak ilerlemek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Üst solunum yolu enfeksiyonu bulguları ve preauriküler lenfadenopati "
                            "eşliğinde gelişen, korneası saydam ve kapak ödemi olmayan olgularda "
                            "değerlendirme kliniktir; laboratuvar testi gerekmez."
                        ),
                        "new_finding": (
                            "Ek laboratuvar veya kültür tetkiki istenmedi; klinik bulgularla tanı "
                            "aşamasına geçildi."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı ve Ayırıcı Değerlendirme",
                "question": (
                    "Üst solunum yolu enfeksiyonu bulguları, bir gözden diğerine geçen hiperemi, "
                    "serömüköz akıntı ve preauriküler lenfadenopati varlığında en olası tanınız nedir?"
                ),
                "options": [
                    {
                        "text": "Preseptal (Periorbital) Selülit",
                        "is_correct": False,
                        "scenario_update": (
                            "Preseptal selülitte göz kapaklarında belirgin ödem, kızarıklık, ısı artışı "
                            "ve hassasiyet bulunur; bu hastada göz kapakları tamamen doğaldır."
                        ),
                        "teaching_point": (
                            "Kapak ödemi ve periorbital cilt eritemi olmaksızın yalnızca konjonktival "
                            "hiperemi bulunması preseptal selüliti dışlar."
                        ),
                    },
                    {
                        "text": "Herpetik Keratokonjonktivit (Korneal Ülser)",
                        "is_correct": False,
                        "scenario_update": (
                            "Herpetik tutulum genellikle tek taraflıdır, göz kapağında grup veziküller, "
                            "şiddetli fotofobi ve floresein ile dendritik korneal boyanma görülür."
                        ),
                        "teaching_point": (
                            "Saydam kornea, floresein boyanma olmaması ve bilateral serömüköz "
                            "sekresyon herpetik keratitten uzaklaştırır."
                        ),
                    },
                    {
                        "text": "Akut Adenoviral (Viral) Konjonktivit",
                        "is_correct": True,
                        "explanation": (
                            "Rinit semptomları, bir gözden başlayıp 24-48 saatte diğer göze geçen "
                            "konjonktival hiperemi, sulu-serömüköz sekresyon ve hassas preauriküler "
                            "lenfadenopati akut adenoviral konjonktivit için tipiktir."
                        ),
                        "new_finding": "Kesin Tanı: Akut Adenoviral (Viral) Konjonktivit.",
                    },
                    {
                        "text": "Akut Nazolakrimal Kanal Tıkanıklığı ve Dakriyosistit",
                        "is_correct": False,
                        "scenario_update": (
                            "Dakriyosistitte medial kantus ve gözyaşı kesesi üzerinde kızarık, ağrılı "
                            "şişlik ve kese basısıyla punktumdan pürülan reflü saptanır."
                        ),
                        "teaching_point": (
                            "Medial kantusta şişlik olmaması ve tablonun ÜSYE ile birlikte akut "
                            "bilateral başlaması viral konjonktivit lehinedir."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Tedavi, İzlem ve Taburculuk Planı",
                "question": (
                    "Akut adenoviral konjonktivit tanısı koyduğunuz bu çocukta en doğru tedavi, hijyen "
                    "ve taburculuk yaklaşımı hangisidir?"
                ),
                "options": [
                    {
                        "text": (
                            "Steril serum fizyolojik ile kapak temizliği, soğuk kompres ve suni gözyaşı "
                            "önermek, sıkı el-havlu hijyeni ve kırmızı bayrak eğitimiyle taburcu etmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Viral konjonktivitte temel tedavi mekanik sekresyon temizliği, soğuk "
                            "kompres, suni gözyaşı damlaları ve yüksek bulaştırıcılık nedeniyle el, "
                            "havlu ve yastık kılıfı hijyenidir."
                        ),
                        "new_finding": (
                            "Göz temizliği ve temas hijyeni eğitimi verildi; kapak ödemi, şiddetli göz "
                            "ağrısı, fotofobi, yoğun pürülan akıntı veya görme bulanıklığı gelişirse "
                            "başvuru önerisiyle taburcu edildi."
                        ),
                    },
                    {
                        "text": (
                            "Oküler ağrı ve yanmayı evde kesmek için hastaya proparakain içeren topikal "
                            "anestezik göz damlası reçete etmek ve her iki gözü steril gazlı bezle "
                            "kapatmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Evde tekrarlayan topikal anestezik damla kullanımı kornea epitel "
                            "rejenerasyonunu durdurarak toksik keratopatiye, göz kapama bandajı ise "
                            "sekonder bakteriyel üremeye yol açtı!"
                        ),
                        "teaching_point": (
                            "Topikal anestezik göz damlaları korneal erime riski nedeniyle hastaya asla "
                            "reçete edilmez; ayrıca enfeksiyöz konjonktivitlerde göz bandajla kapatılmaz."
                        ),
                    },
                    {
                        "text": (
                            "Hiperemiyi hızla baskılamak amacıyla günde dört kez topikal prednizolon "
                            "asetat göz damlası ve on gün süreyle oral amoksisilin-klavulanat "
                            "süspansiyon tedavisi başlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Topikal steroid viral saçılım süresini uzattı ve göz içi basıncı artışı "
                            "riski yarattı; sistemik antibiyotik ise viral tabloda etkisiz kaldı."
                        ),
                        "teaching_point": (
                            "Acil serviste oftalmolog kontrolü olmadan kırmızı göze topikal steroid "
                            "reçete edilmez; basit konjonktivitte oral antibiyotik endikasyonu yoktur."
                        ),
                    },
                    {
                        "text": (
                            "Viral replikasyonu durdurmak için beş gün süreyle oral asiklovir "
                            "süspansiyon ve günde beş kez topikal gansiklovir oftalmik jel reçete "
                            "ederek gözlem altına almak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Herpes virüslerine etkili olan asiklovir ve gansiklovir adenoviral "
                            "enfeksiyon üzerinde etki göstermedi ve oküler yüzeyde lokal irritasyon "
                            "yaptı."
                        ),
                        "teaching_point": (
                            "Adenoviral konjonktivit kendi kendini sınırlayan bir enfeksiyondur; "
                            "anti-herpetik antivirallerin (asiklovir, gansiklovir) adenovirüse karşı "
                            "klinik etkinliği yoktur."
                        ),
                    },
                ],
            },
        ],
    },
]
