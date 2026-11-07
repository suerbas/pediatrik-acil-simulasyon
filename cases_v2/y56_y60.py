# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - Y56-Y60 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "Y56",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "7 Yaşında",
        "gender": "Erkek",
        "complaint": "Bir haftadır halsizlik, bulantı ve iştahsızlık; son iki gündür gözlerde sararma ve koyu renkli idrar",
        "history": "Annesi anlatıyor: 'Bir hafta önce hafif ateşi, halsizliği ve bulantısı başladı, hiçbir şey yemek istemedi, karnının sağ üst tarafı ağrıyordu. Ateşi geçti ama iki gündür gözlerinin akı sarardı, çişi çay rengi, kakası açık renkli oldu. Sınıfında üç arkadaşında da benzer şikayet olmuş.' Kan nakli, ilaç veya bitki çayı kullanımı yok. Aşı kartında 18. ay sonrası takvim aşılarının yapılmadığı görüldü (aile göç nedeniyle aşıları kaçırmış). Tartı: 24 kg.",
        "final_diagnosis": "Akut Viral Hepatit A",
        "disposition": "Yeşil Alanda Karaciğer Sentez Fonksiyonunun Doğrulanması, Destek Tedavisi, Temaslı Profilaksisi ve Bildirim ile Ayaktan İzlem",
        "case_pearl": "Okul çağında prodrom (halsizlik, bulantı, sağ üst kadran ağrısı) sonrası ateşin düşüp sarılığın başlaması ve kümelenme hepatit A'yı düşündürür. Tanı anti-HAV IgM ile konur. Prognozu belirleyen transaminaz düzeyi değil, sentez fonksiyonu (INR), kan şekeri ve bilinç durumudur; INR ≥1.5 veya ensefalopati akut karaciğer yetmezliği kriteridir. Tedavi destekleyicidir; parasetamol düşük dozda kısa süre kullanılabilir, hepatotoksik ilaç ve bitkisel ürünlerden kaçınılır. Temaslılara iki hafta içinde aşı ile profilaksi önerilir ve bildirim zorunludur.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Prodrom sonrası sarılık, koyu idrar ve açık renkli dışkısı olan bu 7 yaşındaki çocukta muayenede öncelikle neyi değerlendirirsiniz?",
                "options": [
                    {
                        "text": "Sağ üst kadran ağrısı nedeniyle Murphy bulgusunu aramak ve safra yolu taşı olasılığına karşı muayeneyi karın palpasyonuyla sınırlı tutup cerrahiye danışmak",
                        "is_correct": False,
                        "scenario_update": "Murphy bulgusu negatifti. Bilinç, kanama ve maruziyet değerlendirilmeden cerrahi konsültasyon istendi; cerrahi ekip akut cerrahi tablo düşünmedi.",
                        "teaching_point": "Prodrom ve kümelenme sonrası gelişen sarılıkta öncelik karaciğer fonksiyonunu tehdit eden bulguları aramaktır; safra taşı çocukta nadirdir."
                    },
                    {
                        "text": "Sınıftaki kümelenme nedeniyle izolasyon önlemlerine odaklanıp çocuğu ayrı bir odaya almak ve muayeneyi laboratuvar sonuçları geldikten sonra ayrıntılandırmak",
                        "is_correct": False,
                        "scenario_update": "Çocuk bir saat odada bekletildi; ensefalopati ve kanama bulguları sorgulanmadan zaman geçti.",
                        "teaching_point": "Temas önlemleri gereklidir ancak sistematik muayeneyi geciktirmemelidir."
                    },
                    {
                        "text": "Bulantı ve iştahsızlık nedeniyle önce intravenöz sıvı ve ondansetron başlatmak, sarılığın derecesini değerlendirmek için transkutan bilirubin ölçümü yapmak",
                        "is_correct": False,
                        "scenario_update": "İntravenöz sıvı başlandı; çocuk oral alabildiği halde damar yolu açıldı ve karaciğer yetmezliği bulguları sistematik değerlendirilmedi.",
                        "teaching_point": "Transkutan ölçüm yenidoğan dışında güvenilir değildir; oral alabilen çocukta intravenöz sıvı gerekmez."
                    },
                    {
                        "text": "Bilinç ve davranış değişikliğini, asteriksisi, kanama bulgularını, hidrasyonu ve karaciğer-dalak boyutunu değerlendirip ilaç, bitki ve toksin maruziyetini sorgulamak",
                        "is_correct": True,
                        "explanation": "Sarılıklı çocukta ilk öncelik akut karaciğer yetmezliği bulgularını (ensefalopati, kanama) erkenden tanımaktır. Karaciğer boyutu, hassasiyet, dalak ve ilaç-bitki maruziyeti ayırıcı tanıyı yönlendirir.",
                        "new_finding": "Vital Bulgular: Ateş 37.2°C, KTA 92/dk, SS 20/dk, TA 104/66 mmHg. Bilinç açık, oryante, davranış değişikliği ve asteriksis yok. Skleralar ikterik. Peteşi, ekimoz, burun kanaması yok. Karaciğer kot kavsini 3 cm geçiyor, kenarı yumuşak ve hassas. Dalak ele gelmiyor. Asit yok. Hidrasyonu iyi. İlaç olarak yalnızca iki gün parasetamol kullanılmış (15 mg/kg, günde 3 kez)."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Stratejisi",
                "question": "Bilinci açık, kanama bulgusu olmayan ve hepatomegalisi olan bu sarılıklı çocukta hangi tetkikler öncelikli olarak istenmelidir?",
                "options": [
                    {
                        "text": "Kolestaz paterni nedeniyle önce batın ultrasonografisi ve manyetik rezonans kolanjiyografi isteyip laboratuvar tetkiklerini görüntüleme sonucuna göre planlamak",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografide hepatomegali ve safra kesesi duvar ödemi dışında bulgu yoktu; MR kolanjiyografi için sedasyon gerekecekti.",
                        "teaching_point": "Hepatosellüler hasar paterni olan çocukta ilk basamak laboratuvar ve viral seroloji olmalıdır; ileri görüntüleme seçici kullanılır."
                    },
                    {
                        "text": "AST, ALT ve bilirubin düzeylerini istemek, transaminazlar 1000 U/L'nin üzerindeyse hastayı karaciğer nakil merkezine sevk etmek",
                        "is_correct": False,
                        "scenario_update": "ALT 1840 U/L geldi; sentez fonksiyonu bilinmeden çocuk nakil merkezine sevk edilmek üzereydi.",
                        "teaching_point": "Transaminaz yüksekliği prognozu belirlemez; sentez fonksiyonu (INR), kan şekeri ve bilinç durumu belirleyicidir."
                    },
                    {
                        "text": "Yalnızca total bilirubin ve tam idrar tetkiki isteyip idrarda bilirubin pozitifse ek tetkik yapmadan aile hekimi kontrolü ile taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "İdrarda bilirubin pozitif bulundu; sentez fonksiyonu ve etiyoloji değerlendirilmeden çocuk taburcu edilecekti.",
                        "teaching_point": "Sarılıklı çocukta INR ve kan şekeri bakılmadan güvenli taburculuk kararı verilemez."
                    },
                    {
                        "text": "Transaminazlar, total-direkt bilirubin, INR, kan şekeri, albümin ve tam kan sayımı ile birlikte hepatotropik virüs serolojilerini istemek",
                        "is_correct": True,
                        "explanation": "Akut hepatitte sentez fonksiyonu (INR, albümin) ve kan şekeri yetmezlik riskini gösterir. Akut viral seroloji paneli (A, B ve C tipi belirteçler) etiyolojiyi belirler.",
                        "new_finding": "AST 1420 U/L, ALT 1840 U/L, total bilirubin 5.8 mg/dL, direkt 4.1 mg/dL, INR 1.1, kan şekeri 92 mg/dL, albümin 3.9 g/dL, hemogram normal. Viral seroloji: A tipi IgM antikoru pozitif; B tipi yüzey antijeni ve çekirdek IgM negatif."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Prodrom sonrası sarılık, belirgin transaminaz yüksekliği, normal INR ve A tipi IgM antikoru pozitifliği olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Otoimmün hepatit",
                        "is_correct": False,
                        "scenario_update": "Kümelenme, akut prodrom ve viral seroloji pozitifliği otoimmün süreci düşündürmez.",
                        "teaching_point": "Otoimmün hepatit viral etiyoloji dışlandıktan sonra düşünülür."
                    },
                    {
                        "text": "Parasetamol hepatotoksisitesi",
                        "is_correct": False,
                        "scenario_update": "Terapötik dozda kısa süreli kullanım ve pozitif anti-HAV IgM bu tanıyı desteklemez.",
                        "teaching_point": "Parasetamol toksisitesi aşırı doz öyküsü ve genellikle prodrom olmadan gelişir."
                    },
                    {
                        "text": "Akut hepatit A",
                        "is_correct": True,
                        "explanation": "Okul kümelenmesi, aşısız çocuk, prodrom sonrası sarılık, hepatosellüler hasar ve anti-HAV IgM pozitifliği akut hepatit A'yı doğrular. INR normal olduğundan karaciğer yetmezliği yoktur.",
                        "new_finding": "Tanı: Akut Viral Hepatit A (sentez fonksiyonu korunmuş)."
                    },
                    {
                        "text": "Koledok kisti",
                        "is_correct": False,
                        "scenario_update": "Ultrasonda safra yollarında dilatasyon yok; tablo hepatosellüler.",
                        "teaching_point": "Koledok kistinde kolestatik patern ve safra yolu dilatasyonu beklenir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Oral alabilen, INR'si normal bu çocuğun yönetimi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Akut karaciğer yetmezliği gelişme riskine karşı çocuğu servise yatırıp intravenöz dekstrozlu sıvı başlatmak ve transaminazlar normale dönene kadar hastanede tutmak",
                        "is_correct": False,
                        "scenario_update": "Stabil çocuk iki hafta hastanede kaldı; transaminazlar haftalar içinde yavaş düştüğü için taburculuk gereksiz uzadı.",
                        "teaching_point": "INR normal, bilinci açık ve oral alabilen çocuk ayaktan izlenir; yatış ölçütü transaminaz değil sentez fonksiyonu ve klinik bulgulardır."
                    },
                    {
                        "text": "Ev temaslılarına profilaksi için immünoglobulin yapmak ve çocuğa enfeksiyonu sınırlamak amacıyla antiviral tedavi başlayıp bir hafta sonra kontrol etmek",
                        "is_correct": False,
                        "scenario_update": "Antiviral tedavi için bir endikasyon bulunmadığı belirtildi; sağlıklı okul çağı temaslılarda immünoglobulin yerine aşı tercih edilecekti.",
                        "teaching_point": "Hepatit A için antiviral tedavi yoktur; 12 ay-40 yaş sağlıklı temaslılarda temas sonrası profilakside tercih aşıdır."
                    },
                    {
                        "text": "Karaciğeri korumak için ursodeoksikolik asit ve silimarin başlamak, yağ ve protein kısıtlı diyet önermek ve iki hafta okula gönderilmemesini söylemek",
                        "is_correct": False,
                        "scenario_update": "Kısıtlı diyetle çocuk iştahsızlaşıp kilo kaybetti; ilaçlar seyri değiştirmedi.",
                        "teaching_point": "Akut hepatit A'da spesifik tedavi yoktur; diyet kısıtlaması ve hepatoprotektif ürünlerin yararı gösterilmemiştir."
                    },
                    {
                        "text": "Destek tedavisi, gerekirse kısa süreli düşük doz parasetamol, sarılık başlangıcından bir hafta okula ara, temaslılara aşı profilaksisi, bildirim ve 3-5 günde INR kontrolü",
                        "is_correct": True,
                        "explanation": "Tedavi destekleyicidir; hepatotoksik ilaç ve bitkisel ürünlerden kaçınılır. Bulaştırıcılık sarılık başlangıcından yaklaşık bir hafta sonra azalır. Ev ve sınıf temaslılarına iki hafta içinde aşı uygulanır; INR ve bilinç izlemi karaciğer yetmezliğini erken yakalamak için yapılır.",
                        "new_finding": "Bildirim yapıldı, kardeşe ve sınıf temaslılarına hepatit A aşısı önerildi. Dördüncü gün kontrolünde INR 1.0, bilirubin 4.2 mg/dL; çocuk iştahla yemek yiyordu. Üç haftada sarılık geriledi."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y57",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "15 Aylık",
        "gender": "Kız",
        "complaint": "Geçirilmiş ishal sonrasında süt ve yoğurt alınca tekrarlayan köpüklü sulu dışkılama, şişkinlik ve pişik",
        "history": "Annesi anlatıyor: 'On gün önce ateşli, kusmalı bir ishal geçirdi; ateşi ve kusması geçti. Ama ne zaman inek sütü veya yoğurt versem yarım saat sonra karnından gurultular geliyor, bezine fışkırır gibi köpüklü, sapsarı, ekşi kokulu sulu kaka yapıyor. Popo bölgesi kıpkırmızı oldu. Süt vermediğim günlerde kakası düzeliyor gibi.' İştahı iyi, oyun oynuyor. Kreşe gidiyor. Tartı: 10 kg (hastalık öncesi 10.2 kg).",
        "final_diagnosis": "Sekonder (Postenfeksiyöz) Laktoz İntoleransı",
        "disposition": "Yeşil Alandan 2-4 Hafta Laktozu Azaltılmış Beslenme, Bariyer Krem ve Kademeli Yeniden Başlama Eğitimi ile Taburculuk",
        "case_pearl": "Viral gastroenterit sonrası ince bağırsak fırça kenarı hasarı geçici laktaz eksikliğine yol açabilir. Süt ürünleriyle ilişkili köpüklü, asidik ishal, şişkinlik ve perianal eritem tipiktir; dışkı pH <5.5 ve redüktan madde pozitifliği tanıyı destekler. Tedavi geçici (2-4 hafta) laktozu azaltılmış beslenmedir; yoğurt ve peynir gibi fermente ürünler çoğunlukla tolere edilir. Kalıcı kısıtlama ve rutin laktozsuz mama önerilmez.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Geçirilmiş ishal sonrası belirli gıdalarla tetiklenen köpüklü dışkılaması olan bu bebekte değerlendirmenin odağı nedir?",
                "options": [
                    {
                        "text": "Dışkılamanın tetikleyici gıdalarla zamansal ilişkisini ayrıntılı sorgulayıp hidrasyon, büyüme, karın distansiyonu ve perianal cildi değerlendirmek",
                        "is_correct": True,
                        "explanation": "Postenfeksiyöz dönemde belirli gıdalarla tetiklenen ishalde gıda-semptom ilişkisi tanının anahtarıdır. Hidrasyon ve büyüme klinik ciddiyeti, perianal eritem dışkının asiditesini yansıtır.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 104/dk, SS 22/dk, KDZ 1.5 sn. Hidrasyonu iyi, aktif. Tartı 10 kg (%2 kayıp). Karın hafif distandü, timpanik, yaygın gurultu; hassasiyet yok. Perianal bölgede parlak kırmızı, dışkı temas alanıyla sınırlı eritem; satellit lezyon yok. Annenin tuttuğu bezde köpüklü, sulu, sarı dışkı."
                    },
                    {
                        "text": "Uzayan ishal nedeniyle bakteriyel bir etken olabileceğini düşünüp hidrasyon değerlendirmesi sonrasında dışkı kültürü ve Clostridioides toksin testi istemek",
                        "is_correct": False,
                        "scenario_update": "Kültür negatif geldi; toksin testi pozitif bildirildi ve iki yaş altı çocukta kolonizasyon olabileceği için yorumlanamadı. Aile kaygılandı.",
                        "teaching_point": "Ateşsiz, iyi görünen ve belirli gıdalarla tetiklenen ishalde rutin bakteriyel tetkik yönetimi değiştirmez."
                    },
                    {
                        "text": "Perianal kızarıklığı kandida dermatiti kabul edip antifungal krem önermek, ishal için mevcut beslenmeyi sürdürüp bir hafta sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Antifungal kreme rağmen kızarıklık sürdü; dışkının niteliği değişmediği için cilt iyileşmedi.",
                        "teaching_point": "Satellit lezyonu olmayan, dışkı temas alanıyla sınırlı eritem asidik dışkıya bağlı irritan dermatittir; altta yatan nedene yönelinmelidir."
                    },
                    {
                        "text": "Köpüklü ve yağlı görünümlü dışkı nedeniyle pankreas yetersizliğini düşünüp solunum öyküsünü sorgulamak ve ter testi için yönlendirme planlamak",
                        "is_correct": False,
                        "scenario_update": "Solunum öyküsü yoktu; ter testi randevusu verildi ve gıda-semptom ilişkisi ayrıntılı sorgulanmadı.",
                        "teaching_point": "Akut enfeksiyon sonrası başlayan ve belirli gıdalarla tetiklenen ishal kronik malabsorpsiyon hastalıklarından önce geçici enzim eksikliklerini düşündürür."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Stratejisi",
                "question": "Hidrasyonu iyi, perianal asidik eritemi ve köpüklü dışkısı olan bu bebekte hangi basit tetkik tanıyı destekler?",
                "options": [
                    {
                        "text": "Taze dışkı örneğinde pH ölçümü ve redüktan madde testi yapmak, mikroskopide lökosit ve parazit bakmak; kan tetkiki istememek",
                        "is_correct": True,
                        "explanation": "Fermente edilmemiş karbonhidratların kolonda bakteriyel fermantasyonu asidik (pH <5.5) ve redüktan madde içeren dışkıya yol açar. Bu basit tetkikler kan tetkikine gerek kalmadan tanıyı destekler.",
                        "new_finding": "Taze dışkı: pH 5.0, redüktan madde ++ pozitif. Mikroskopide lökosit, eritrosit, parazit ve kist yok."
                    },
                    {
                        "text": "Tanıyı kesinleştirmek için acil serviste 2 g/kg oral yükleme verip iki saat sonra kan şekeri artışını ve gelişen semptomları gözlemek",
                        "is_correct": False,
                        "scenario_update": "Yükleme sonrası bebekte şiddetli gaz sancısı ve dört kez patlayıcı ishal gelişti; kan şekeri ölçümü güvenilir sonuç vermedi.",
                        "teaching_point": "Provokatif yükleme testleri akut dönemdeki küçük çocukta rahatsızlık verir ve gereksizdir."
                    },
                    {
                        "text": "Hidrojen nefes testi ile karbonhidrat emilimini değerlendirmek amacıyla çocuk gastroenteroloji polikliniğine randevu verip testi yapılana kadar mevcut beslenmeyi sürdürmek",
                        "is_correct": False,
                        "scenario_update": "Randevu üç hafta sonraya verildi; bu sürede ishal ve pişik sürdü.",
                        "teaching_point": "Hidrojen nefes testi küçük çocukta uygulaması güç ve bu klinik tabloda gereksizdir; basit dışkı testleri yeterlidir."
                    },
                    {
                        "text": "Malabsorpsiyonu değerlendirmek için doku transglutaminaz IgA, total IgA, albümin, demir ve çinko düzeylerini isteyip sonuçlara göre diyet planlamak",
                        "is_correct": False,
                        "scenario_update": "Sonuçlar normal geldi; bebek kan alımı sırasında çok ağladı ve diyet önerisi ertelendi.",
                        "teaching_point": "Yeni başlayan, enfeksiyon sonrası, büyümeyi etkilememiş ishalde kronik malabsorpsiyon taraması gerekmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Viral ishal sonrası süt ürünleriyle tetiklenen köpüklü ishal, asidik dışkı ve redüktan madde pozitifliği olan bu bebekte tanı nedir?",
                "options": [
                    {
                        "text": "Giardia duodenalis enfeksiyonu",
                        "is_correct": False,
                        "scenario_update": "Mikroskopide trofozoit veya kist görülmedi ve ishal süt alımıyla tetikleniyor.",
                        "teaching_point": "Protozoon enfeksiyonu belirli gıdayla tetiklenmeyen uzamış ishal yapar."
                    },
                    {
                        "text": "İnek sütü proteini alerjisi",
                        "is_correct": False,
                        "scenario_update": "Yakınma enfeksiyon sonrası başlamış; kanlı dışkı, ürtiker veya egzama yok ve dışkı bulguları karbonhidrat malabsorpsiyonunu gösteriyor.",
                        "teaching_point": "Asidik dışkı ve redüktan madde pozitifliği protein alerjisinden çok karbonhidrat malabsorpsiyonunu düşündürür."
                    },
                    {
                        "text": "Konjenital sukraz-izomaltaz eksikliği",
                        "is_correct": False,
                        "scenario_update": "Konjenital eksiklikte şikayet sükroz içeren gıdalara geçişle başlar; burada belirleyici olan enfeksiyon sonrası süt ürünleri.",
                        "teaching_point": "Konjenital disakkaridaz eksiklikleri enfeksiyon öyküsünden bağımsız ve kalıcıdır."
                    },
                    {
                        "text": "Sekonder (postenfeksiyöz) laktoz intoleransı",
                        "is_correct": True,
                        "explanation": "Viral enterit sonrası fırça kenarı hasarına bağlı geçici laktaz eksikliği süt alımıyla ozmotik-fermentatif ishale neden olur; asidik dışkı ve redüktan madde pozitifliği tanıyı destekler.",
                        "new_finding": "Tanı: Postenfeksiyöz (Sekonder) Laktoz İntoleransı."
                    }
                ]
            },
            {
                "stage_title": "Diyet Yönetimi ve İyileşme Planı",
                "question": "Bu bebeğin beslenme planı nasıl düzenlenmelidir?",
                "options": [
                    {
                        "text": "İnek sütü ve süt ürünlerini kalıcı olarak kesip soya bazlı mamaya geçmek, kalsiyum desteği başlamak ve okul çağında yeniden değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Kalıcı kısıtlama gereksiz yere uygulandı; aile yıllarca süt ürünlerinden kaçındı.",
                        "teaching_point": "Sekonder laktoz intoleransı geçicidir; kalıcı kısıtlama ve soya mamaya geçiş gereksizdir."
                    },
                    {
                        "text": "İki-dört hafta laktozu azaltılmış süt kullanmak, yoğurt ve peynire devam etmek, bariyer krem önermek ve ardından sütü kademeli olarak yeniden başlatmak",
                        "is_correct": True,
                        "explanation": "Fırça kenarının yenilenmesi için 2-4 haftalık laktoz azaltımı yeterlidir. Fermente ürünler daha az laktoz içerdiği için genellikle tolere edilir. Sonrasında süt ürünleri kademeli açılır; perianal bölge bariyer kremle korunur.",
                        "new_finding": "Laktozu azaltılmış süte geçildi, çinko oksitli bariyer krem başlandı. 48 saatte patlayıcı ishal durdu, pişik geriledi. Üç hafta sonra normal süt sorunsuz yeniden başlandı."
                    },
                    {
                        "text": "Bağırsak enzimlerinin hızla yenilenmesi için iki hafta probiyotik ve çinko vermek, süt ürünlerine aynı miktarda devam edip şikayetleri izlemek",
                        "is_correct": False,
                        "scenario_update": "Süt ürünlerine devam edilince ishal ve pişik sürdü; bebeğin tartısı 200 g daha azaldı.",
                        "teaching_point": "Takviyeler tek başına yeterli değildir; semptomların kontrolü için geçici laktoz azaltımı gerekir."
                    },
                    {
                        "text": "İshali durdurmak için 24 saat yalnızca ORS ile beslemek, ardından pirinç lapası ve muzla sınırlı bir diyetle bir hafta devam etmek",
                        "is_correct": False,
                        "scenario_update": "Kısıtlı diyetle bebek huzursuzlaştı ve kilo kaybı derinleşti; süt yeniden başlanınca ishal tekrarladı.",
                        "teaching_point": "Aç bırakma ve kısıtlı diyetler önerilmez; hedef yalnızca laktoz yükünü geçici olarak azaltmaktır."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y58",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "7 Yaşında",
        "gender": "Kız",
        "complaint": "Araba yolculuğu sırasında başlayan bulantı, kusma, solukluk ve soğuk terleme",
        "history": "Ailesi anlatıyor: 'Ailecek bayram için şehir dışına arabayla gidiyorduk. Yolun ilk saatinde arka koltukta tablette çizgi film izlerken esnemeye başladı, rengi soldu, soğuk soğuk terledi ve ardından kustu. Arabayı kenara çekip açık havaya çıkınca 15-20 dakikada toparlandı. Tekrar yola çıkıp virajlara girince yine kustu. Evde hiç şikayeti yok. Baş ağrısı, sabah kusması veya dengesizliği olmadı. Daha önce otobüs yolculuklarında da midesi bulanmıştı. Beyninde bir şey mi var diye çok korktuk.'",
        "final_diagnosis": "Hareket Hastalığı (Taşıt Tutması)",
        "disposition": "Yeşil Alandan Nörolojik Muayenenin Doğrulanması, Davranışsal Önlemler ve Gerekirse Yolculuk Öncesi Profilaksi Eğitimi ile Taburculuk",
        "case_pearl": "Taşıt hareketiyle başlayıp hareket bitince geçen bulantı, solukluk, terleme ve kusma; vestibüler, görsel ve proprioseptif girdiler arasındaki uyumsuzluktan kaynaklanır. Normal nörolojik muayenede görüntüleme gerekmez. Kırmızı bayraklar: sabah kusmaları, uykudan uyandıran baş ağrısı, ataksi, nistagmus, papilödem. Tedavide ön koltukta ufka bakmak, ekran-okuma yasağı, havalandırma ve hafif öğün; gerekirse 2 yaş üstünde yolculuktan 30-60 dakika önce birinci kuşak antihistaminik.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Yolculuk sırasında tekrarlayan kusması olan, ailesi beyinle ilgili bir hastalıktan endişe eden bu çocukta muayenede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Kusma ve solukluk nedeniyle hipoglisemiyi düşünüp kapiller kan şekeri bakmak, normalse ek muayene yapmadan oral sıvı denemesiyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Kan şekeri normal geldi. Nörolojik muayene yapılmadığı için ailenin endişesi giderilemedi ve aile başka bir merkezde tomografi istedi.",
                        "teaching_point": "Ailenin intrakraniyal hastalık kaygısı ancak sistematik nörolojik muayeneyle giderilebilir."
                    },
                    {
                        "text": "Kusmaların gastrointestinal kaynaklı olabileceğini düşünüp karın muayenesine odaklanmak, ardından ondansetron vererek ailenin yolculuğa devam etmesini önermek",
                        "is_correct": False,
                        "scenario_update": "Karın muayenesi normaldi; nörolojik muayene yapılmadan çocuk taburcu edildi ve aile endişesini sürdürdü.",
                        "teaching_point": "Tekrarlayan kusmada nörolojik kırmızı bayraklar mutlaka değerlendirilmelidir."
                    },
                    {
                        "text": "Viraj sırasında kusma olduğu için vestibüler nörit olasılığını değerlendirmek amacıyla Dix-Hallpike manevrası yapıp kulak burun boğaz konsültasyonu istemek",
                        "is_correct": False,
                        "scenario_update": "Dix-Hallpike negatifti; çocuk manevra sırasında yeniden bulantı hissetti. KBB randevusu ertesi güne verildi.",
                        "teaching_point": "Vestibüler nörit sürekli vertigo ve spontan nistagmusla seyreder; yalnız taşıt içinde ortaya çıkan semptomlar bu tabloya uymaz."
                    },
                    {
                        "text": "Baş ağrısı, sabah kusması ve dengesizlik gibi kırmızı bayrakları sorgulayıp fundoskopi, nistagmus, serebellar testler, Romberg ve tandem yürüyüşü içeren nörolojik muayene yapmak",
                        "is_correct": True,
                        "explanation": "Kusan çocukta intrakraniyal basınç artışı ve arka çukur patolojileri kırmızı bayraklar ve ayrıntılı nörolojik muayeneyle dışlanır. Normal muayene ve hareketle ilişkili örüntü aileye güvence vermek için temel dayanaktır.",
                        "new_finding": "Vital Bulgular: Ateş 36.6°C, KTA 86/dk, SS 18/dk, TA 102/64 mmHg. Genel durumu iyi, toparlanmış. Fundoskopide optik disk sınırları keskin. Kraniyal sinirler normal, nistagmus yok, parmak-burun ve topuk-diz testleri normal, Romberg negatif, tandem yürüyüş normal. Kulak zarları doğal. Karın rahat, hidrasyonu iyi."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Nörolojik muayenesi tamamen normal, şikayetleri yalnızca taşıt içinde olan bu çocukta tetkik yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Görüntüleme veya laboratuvar istemeden, şikayetlerin yalnızca taşıt hareketiyle başlayıp durduğunu ve kırmızı bayrak olmadığını aileyle birlikte netleştirmek",
                        "is_correct": True,
                        "explanation": "Tanı öykü ve normal nörolojik muayeneye dayanır. Semptomların taşıt hareketiyle tetiklenip hareket bitince geçmesi tipik örüntüdür; tetkikler yönetimi değiştirmez ve kaygıyı artırabilir.",
                        "new_finding": "Tetkik istenmedi. Ayrıntılı öyküde çocuğun salıncak ve lunaparktaki dönen oyuncaklarda da benzer bulantı yaşadığı, evde hiç şikayeti olmadığı öğrenildi."
                    },
                    {
                        "text": "Paroksismal vertigo atağı olabileceğini düşünüp elektroensefalografi ve odyometri planlamak, sonuçlar çıkana kadar uzun yolculuklardan kaçınmasını önermek",
                        "is_correct": False,
                        "scenario_update": "Tetkik randevuları haftalar sonrasına verildi; aile bayram ziyaretini iptal etti.",
                        "teaching_point": "Benign paroksismal vertigo taşıttan bağımsız, ani başlangıçlı kısa ataklarla seyreder; burada tetkik gerekmez."
                    },
                    {
                        "text": "Ailenin endişesini gidermek ve arka çukur kitlesini kesin olarak dışlamak için kontrastsız beyin tomografisi çekip sonucu aileyle paylaşmak",
                        "is_correct": False,
                        "scenario_update": "Tomografi normal geldi; çocuk gereksiz radyasyona maruz kaldı ve aile bir sonraki yolculukta yeniden görüntüleme istedi.",
                        "teaching_point": "Normal nörolojik muayenede görüntüleme endike değildir; güvence muayene bulgularıyla verilir."
                    },
                    {
                        "text": "Tekrarlayan kusma nedeniyle elektrolit, kan gazı ve tam idrar tetkiki isteyip metabolik bir neden dışlanana kadar oral alımı kısıtlamak",
                        "is_correct": False,
                        "scenario_update": "Sonuçlar normal geldi; toparlanmış ve yemek isteyen çocuk iki saat aç bekletildi.",
                        "teaching_point": "Hidrasyonu iyi ve semptomları geçmiş çocukta laboratuvar tetkikinin katkısı yoktur."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Yalnızca taşıt ve dönen oyuncaklarda başlayan, hareket bitince geçen bulantı-kusma, solukluk ve terlemesi olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Döngüsel kusma sendromu",
                        "is_correct": False,
                        "scenario_update": "Ataklar taşıt hareketiyle tetikleniyor ve dakikalar içinde geçiyor; saatler-günler süren stereotipik ataklar yok.",
                        "teaching_point": "Döngüsel kusma tetikleyiciden bağımsız uzun ataklarla seyreder."
                    },
                    {
                        "text": "Çocukluk çağı benign paroksismal vertigosu",
                        "is_correct": False,
                        "scenario_update": "Ataklar taşıt dışında spontan olmuyor ve kusma ön planda.",
                        "teaching_point": "Benign paroksismal vertigo ani başlangıçlı, kısa süreli ve spontan dengesizlik ataklarıdır."
                    },
                    {
                        "text": "Arka çukur tümörü",
                        "is_correct": False,
                        "scenario_update": "Sabah kusmaları, baş ağrısı, ataksi ve papilödem yok; nörolojik muayene normal.",
                        "teaching_point": "Kafa içi basınç artışı taşıttan bağımsız, ilerleyici bulgularla seyreder."
                    },
                    {
                        "text": "Hareket hastalığı (taşıt tutması)",
                        "is_correct": True,
                        "explanation": "Görsel, vestibüler ve proprioseptif girdiler arasındaki uyumsuzluk taşıt hareketi sırasında bulantı, solukluk, terleme ve kusmaya yol açar; hareket bitince semptomlar geriler.",
                        "new_finding": "Tanı: Hareket Hastalığı (Taşıt Tutması)."
                    }
                ]
            },
            {
                "stage_title": "Önlemler ve Yolculuk Planı",
                "question": "Ailenin dönüş yolculuğu için en uygun öneri hangisidir?",
                "options": [
                    {
                        "text": "Yolculuk öncesinde mideyi boşaltmak için çocuğu aç bırakmak, araba içinde kapalı camla klimayı açık tutmak ve uyuması için hafif sedatif şurup vermek",
                        "is_correct": False,
                        "scenario_update": "Aç bırakılan çocukta bulantı daha erken başladı; sedatif şurup sonrası aşırı uyku hali gelişti.",
                        "teaching_point": "Tamamen aç kalmak bulantıyı artırabilir; hafif öğün ve temiz hava önerilir, rutin sedatif kullanımı uygun değildir."
                    },
                    {
                        "text": "Yolculuk sırasında bulantı başlayınca ağızdan çözünen ondansetron vermek ve çocuğun dikkatini dağıtmak için tablette film izlemeye devam etmesine izin vermek",
                        "is_correct": False,
                        "scenario_update": "Ekran izlemeye devam eden çocuk yine kustu; ondansetron hareketle ilişkili bulantıda sınırlı etki gösterdi.",
                        "teaching_point": "Ekrana bakmak görsel-vestibüler uyumsuzluğu artırır; ondansetronun bu durumda etkinliği düşüktür."
                    },
                    {
                        "text": "Tekrarlayan kusma nedeniyle yolculuk öncesi intramüsküler metoklopramid uygulamak, çocuğu arka koltukta yatırıp gözlerini kapatarak uyumasını sağlamak",
                        "is_correct": False,
                        "scenario_update": "Metoklopramid sonrası çocukta huzursuzluk ve istemsiz kasılmalar gelişti; yolculuk ertelendi.",
                        "teaching_point": "Metoklopramid çocuklarda ekstrapiramidal yan etki riski nedeniyle bu amaçla önerilmez."
                    },
                    {
                        "text": "Ekran ve kitaptan kaçınmasını, mümkünse ön koltukta ufka bakmasını, havalandırmayı ve hafif öğünü önermek; gerekirse yolculuktan 30-60 dakika önce antihistaminik kullanmak",
                        "is_correct": True,
                        "explanation": "Davranışsal önlemler duyusal uyumsuzluğu azaltır. Gerekirse 2 yaş üstünde yolculuk öncesi birinci kuşak antihistaminik (örn. dimenhidrinat) profilaktik kullanılabilir; sedasyon yan etkisi anlatılır.",
                        "new_finding": "Dönüş yolculuğunda çocuk ön koltukta, camı aralık, müzik dinleyerek ve ufka bakarak seyahat etti; ilaca gerek kalmadan kusmadan yolculuğu tamamladı."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y59",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "15 Yaşında",
        "gender": "Kız",
        "complaint": "Beş gündür boğaz ağrısı, ateş ve halsizlik; iki gündür gövdede yaygın kaşıntılı döküntü",
        "history": "Kendisi anlatıyor: 'Beş gündür boğazım çok ağrıyor, yutkunamıyorum, ateşim 39°C'ye çıkıyor. Çok yorgunum, sabahları kalkamıyorum.' Üç gün önce başka bir merkezde boğaz enfeksiyonu denilerek amoksisilin başlanmış. İlacın ikinci gününde gövdede ve kollarda kaşıntılı, kırmızı döküntüler çıkmış. Göz kapaklarında şişlik fark etmiş. Kronik hastalığı ve bilinen ilaç alerjisi yok. Okulda voleybol takımında oynuyor.",
        "final_diagnosis": "Enfeksiyöz Mononükleoz (EBV) ve Aminopenisiline Bağlı Makülopapüler Döküntü",
        "disposition": "Destek Tedavisi, Temas Sporu Kısıtlaması ve Aile Hekimi Takibiyle Yeşil Alandan Taburculuk",
        "case_pearl": "Ergende ateş, eksüdatif tonsillit, posterior servikal lenfadenopati, belirgin yorgunluk ve splenomegali enfeksiyöz mononükleozu düşündürür. Aminopenisilin alan hastaların önemli bir kısmında döküntü gelişir; bu gerçek penisilin alerjisi değildir. Tedavi destekleyicidir. Kortikosteroid yalnızca havayolu daralması, ağır hemoliz veya trombositopeni gibi komplikasyonlarda verilir. Dalak rüptürü riski nedeniyle en az 3-4 hafta temas sporundan kaçınılır.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Antibiyotiğe rağmen ateşi süren ve döküntü gelişen bu ergende muayenede nelere odaklanırsınız?",
                "options": [
                    {
                        "text": "Döküntüyü ilaç alerjisi olarak kabul edip amoksisilini kesmek, antihistaminik başlamak ve tonsillit tedavisini klaritromisinle tamamlamak",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik değiştirildi, ancak ateş ve yorgunluk sürdü; altta yatan tablo değerlendirilmedi.",
                        "teaching_point": "Döküntüyü yalnızca ilaç reaksiyonu olarak ele almak, antibiyotiğe yanıtsız boğaz ağrısının asıl nedenini gözden kaçırır."
                    },
                    {
                        "text": "Havayolu açıklığını, tonsil ve uvula görünümünü, servikal lenf nodlarının yerini, karaciğer ve dalak boyutunu ve döküntünün özelliğini değerlendirmek",
                        "is_correct": True,
                        "explanation": "Lenf nodlarının ön veya arka zincirde olması, organomegali ve tonsil büyüklüğü ayırıcı tanıda ve havayolu riskinin değerlendirilmesinde belirleyicidir.",
                        "new_finding": "Vital Bulgular: Ateş 38.8°C, KTA 104/dk, SS 18/dk, SpO2 %99, TA 108/66 mmHg. Tonsiller 3+ hipertrofik, gri-beyaz eksüdalı, uvula orta hatta, stridor yok, ağzı rahat açıyor. Bilateral posterior servikal zincirde çok sayıda 1.5-2 cm hassas lenf nodu. Bilateral göz kapağı ödemi. Dalak kosta kenarını 3 cm geçiyor, karaciğer 2 cm palpabl. Gövde ve kollarda birleşme eğilimli makülopapüler döküntü, mukoza tutulumu yok."
                    },
                    {
                        "text": "Tonsil eksüdası nedeniyle bakteriyel enfeksiyonun dirençli olduğunu düşünüp intramüsküler benzatin penisilin uygulamak ve 48 saat sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Penisilin uygulandı; döküntü yaygınlaştı ve kaşıntı arttı, ateş ve yorgunluk değişmedi.",
                        "teaching_point": "Antibiyotiğe yanıtsız tonsillitte tedavi değiştirmeden önce lenf nodu dağılımı ve organomegali değerlendirilmelidir."
                    },
                    {
                        "text": "Ateş, döküntü ve göz kapağı şişliği nedeniyle sistemik vaskülit düşünüp ekokardiyografi ve yüksek doz aspirin başlamak için hastayı Sarı Alana almak",
                        "is_correct": False,
                        "scenario_update": "Ekokardiyografi normal bulundu; aspirin başlanması gereksiz kanama ve Reye sendromu riski yarattı.",
                        "teaching_point": "Eksüdatif tonsillit, posterior servikal lenfadenopati ve organomegali bu tablodan uzaklaştırır; önce tam muayene yapılmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Ön tablo değerlendirildikten sonra hangi tetkikleri istersiniz?",
                "options": [
                    {
                        "text": "Döküntü nedeniyle derhal deri biyopsisi planlamak, aynı zamanda serum IgE düzeyi ve ilaç yama testi için dermatolojiye sevk etmek",
                        "is_correct": False,
                        "scenario_update": "Biyopsi nonspesifik perivasküler infiltrasyon gösterdi; asıl hastalık yine aydınlatılmadı.",
                        "teaching_point": "Tipik makülopapüler ilaç döküntüsü biyopsi gerektirmez; ateş ve tonsillitin nedeni kan tetkikleriyle araştırılmalıdır."
                    },
                    {
                        "text": "Yalnızca boğaz kültürü almak ve kültür sonucuna göre antibiyotik seçimini düzenlemek, başka tetkik gerekmediğini söylemek",
                        "is_correct": False,
                        "scenario_update": "Kültürde normal flora üredi; antibiyotik almış hastada sonuç yorumlanamadı ve tablo açıklanamadı.",
                        "teaching_point": "Kültür antibiyotik sonrası yanlış negatif olabilir ve organomegali ile lenfadenopatiyi açıklamaz."
                    },
                    {
                        "text": "Lenfadenopati ve organomegaliyi açıklamak için acil boyun ve batın bilgisayarlı tomografisi istemek, sonuca göre hematolojiye danışmak",
                        "is_correct": False,
                        "scenario_update": "Tomografi lenfadenopati ve splenomegaliyi gösterdi ama nedeni açıklamadı; hasta gereksiz radyasyon aldı.",
                        "teaching_point": "Organomegali ve lenfadenopatide ilk adım periferik yayma dahil kan tetkikleridir; görüntüleme gerekirse ultrasonografi tercih edilir."
                    },
                    {
                        "text": "Periferik yayma ile tam kan sayımı, karaciğer enzimleri ve heterofil antikor testini istemek, gerekirse virüse özgü serolojiyle tamamlamak",
                        "is_correct": True,
                        "explanation": "Lenfositoz, atipik lenfositler ve transaminaz yüksekliği tanıyı destekler; heterofil antikor ergende duyarlı bir hızlı testtir. Negatifse virüse özgü serolojiyle doğrulanır.",
                        "new_finding": "Lökosit 14.200/mm³, lenfosit %62, atipik lenfosit %18, Hb 12.8 g/dL, trombosit 162.000/mm³. ALT 112 U/L, AST 96 U/L, total bilirubin 0.9 mg/dL. Heterofil antikor testi pozitif. Hızlı strep antijen testi negatif."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik ve laboratuvar bulgularına göre en olası tanınız nedir?",
                "options": [
                    {
                        "text": "Enfeksiyöz mononükleoz ve aminopenisilin döküntüsü",
                        "is_correct": True,
                        "explanation": "Eksüdatif tonsillit, posterior servikal lenfadenopati, splenomegali, atipik lenfositoz, transaminaz artışı ve pozitif heterofil antikor EBV enfeksiyonunu gösterir. Amoksisilin sonrası döküntü bu tabloda sık görülür.",
                        "new_finding": "Tanı: EBV enfeksiyöz mononükleozu, amoksisiline bağlı makülopapüler döküntü."
                    },
                    {
                        "text": "Streptokoksik tonsillit ve gerçek penisilin alerjisi",
                        "is_correct": False,
                        "scenario_update": "Hızlı antijen testi negatifti; splenomegali ve atipik lenfositoz streptokoksik tonsillitle açıklanamazdı.",
                        "teaching_point": "Streptokoksik tonsillitte ön servikal lenfadenopati olur; splenomegali ve atipik lenfositoz beklenmez."
                    },
                    {
                        "text": "Sitomegalovirüs mononükleoz sendromu",
                        "is_correct": False,
                        "scenario_update": "Heterofil antikor pozitifti ve belirgin eksüdatif tonsillit vardı.",
                        "teaching_point": "CMV mononükleozunda farenjit ve lenfadenopati hafiftir, heterofil test negatiftir."
                    },
                    {
                        "text": "Akut lösemi ilk başvurusu",
                        "is_correct": False,
                        "scenario_update": "Hb ve trombosit normaldi, yaymada blast yoktu.",
                        "teaching_point": "Lösemide sitopeniler ve yaymada blastlar beklenir; atipik lenfositler reaktif hücrelerdir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu hasta için en doğru tedavi ve taburculuk planı hangisidir?",
                "options": [
                    {
                        "text": "Tonsil ödemini hızla azaltmak ve hastalık süresini kısaltmak için beş gün oral prednizolon başlayıp amoksisilini kesmek ve taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Steroid başlandı; yorgunluk süresi değişmedi ve havayolu sorunu olmayan hastaya gereksiz ilaç verilmiş oldu.",
                        "teaching_point": "Kortikosteroidler komplike olmayan olguda önerilmez; havayolu daralması, ağır hemoliz veya trombositopenide düşünülür."
                    },
                    {
                        "text": "Amoksisilini kesip parasetamol veya ibuprofen, bol sıvı ve istirahat önermek; en az 3-4 hafta temas sporundan uzak durmasını söylemek",
                        "is_correct": True,
                        "explanation": "Tedavi destekleyicidir. Döküntü gerçek alerji değildir ve kayıtlara penisilin alerjisi olarak yazılmamalıdır. Dalak rüptürü riski nedeniyle temas sporu kısıtlanır.",
                        "new_finding": "Hasta destek tedavisiyle taburcu edildi. Döküntü bir haftada soldu, ateş 10. günde geriledi. Dört hafta sonraki kontrolde dalak ele gelmiyordu ve voleybola dönüşüne izin verildi."
                    },
                    {
                        "text": "Döküntü nedeniyle tıbbi kayda kalıcı penisilin alerjisi yazmak, antibiyotiği azitromisinle değiştirip beş gün daha devam ettirmek",
                        "is_correct": False,
                        "scenario_update": "Hasta yanlış biçimde penisilin alerjisi olarak etiketlendi; ileride ilk basamak antibiyotikler kullanılamayacak hale geldi.",
                        "teaching_point": "Bu tablodaki aminopenisilin döküntüsü gerçek alerji değildir; antibiyotik endikasyonu da yoktur."
                    },
                    {
                        "text": "Ateş düşünce bir hafta içinde okula ve spor antrenmanlarına dönebileceğini söylemek, ilaç önermeden aile hekimi kontrolü planlamak",
                        "is_correct": False,
                        "scenario_update": "İkinci haftada voleybol maçında sol üst kadrana darbe alan hasta şiddetli karın ağrısıyla getirildi.",
                        "teaching_point": "Splenomegali olan hastada temas sporu ve ağır egzersiz en az 3-4 hafta kısıtlanmalıdır."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y60",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "6 Yaşında",
        "gender": "Kız",
        "complaint": "Ani başlayan yüksek ateş, yutma güçlüğü, göbek çevresinde karın ağrısı ve kusma",
        "history": "Ailesi anlatıyor: 'Dün aniden 39.2°C ateş başladı, yutkunurken ağladı. Bu sabah iki kez kustu ve göbeğinin etrafında kramp tarzında ağrısı oldu. Öksürüğü, burun akıntısı veya hapşırması yok. Boynunun yanında dokununca acıyan şişlikler fark ettik. Karnı ağrıdığı ve kustuğu için apandisitten korktuk.' Sınıfında son haftalarda benzer hastalık geçiren çocuklar var. Penisilin alerjisi yok. Tartı: 22 kg.",
        "final_diagnosis": "Akut Streptokokal Tonsillofarenjit (Karın Ağrısı ile Seyreden)",
        "disposition": "Yeşil Alandan Hızlı Antijen Testi ile Doğrulama, Oral Amoksisilin ve Okula Dönüş Eğitimi ile Taburculuk",
        "case_pearl": "Okul çağında ani ateş, boğaz ağrısı, tonsiller eksüda, hassas ön servikal lenfadenopati ve öksürük-burun akıntısı yokluğu A grubu streptokok enfeksiyonunu düşündürür; bu çocuklarda karın ağrısı ve kusma sıktır ve akut batını taklit edebilir. Tanı hızlı antijen testi veya kültürle konur. Tedavide amoksisilin 50 mg/kg/gün (tek veya iki dozda, maks 1 g/gün) 10 gün ya da tek doz benzatin penisilin G kullanılır; antibiyotiğin 12-24. saatinden sonra okula dönülebilir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Ani ateş, yutma güçlüğü, karın ağrısı ve kusması olan bu 6 yaşındaki kızda muayeneniz nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Orofarenkste eksüda ve peteşi, ön servikal lenf nodlarını ve öksürük-burun akıntısı varlığını değerlendirmek; karında peritoneal bulgu aramak ve hidrasyonu kontrol etmek",
                        "is_correct": True,
                        "explanation": "Ateşli karın ağrısında sistematik muayene karın dışı odakları ortaya koyar. Tonsiller eksüda, palatal peteşi, hassas ön servikal lenfadenopati ve viral bulguların yokluğu bakteriyel farenjiti düşündürür; peritoneal bulguların yokluğu cerrahi olasılığı azaltır.",
                        "new_finding": "Vital Bulgular: Ateş 39.2°C, KTA 128/dk, SS 22/dk, SpO2 %99, KDZ 2 sn. Konjonktivit, burun akıntısı ve öksürük yok. Tonsiller hipertrofik, hiperemik, üzerinde beyaz-krem eksüda; yumuşak damakta peteşiler, uvula ödemli. Bilateral ön servikal zincirde 2x1.5 cm hassas lenf nodları. Karın yumuşak, periumbilikal hafif hassasiyet; defans ve rebound yok, zıplayabiliyor. Döküntü yok."
                    },
                    {
                        "text": "Ateş ve kusma nedeniyle muayene öncesinde intravenöz parasetamol ve ondansetron yapıp ateş düştükten sonra sistemleri ayrıntılı değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Ateş düştü ve çocuk rahatladı; ilk muayene bulguları kaydedilmeden 45 dakika geçti.",
                        "teaching_point": "Semptomatik tedavi öncesinde vital bulgular ve sistemik muayene kayıt altına alınmalıdır; oral alabilen çocukta intravenöz yol gerekmez."
                    },
                    {
                        "text": "Yutma güçlüğü nedeniyle hava yolu tehlikesini düşünerek orofarenksi dil basacağıyla muayene etmeden çocuğu oturur pozisyonda tutmak ve kulak burun boğaz uzmanını çağırmak",
                        "is_correct": False,
                        "scenario_update": "Çocukta salya akması, stridor ve tripod pozisyon yoktu; KBB uzmanı orofarenks muayenesinin güvenle yapılabileceğini belirtti, zaman kaybedildi.",
                        "teaching_point": "Dil basacağı ile muayeneden kaçınma yalnızca salya akması, stridor ve toksik görünüm gibi epiglottit bulgularında gereklidir."
                    },
                    {
                        "text": "Karın ağrısı ve kusma nedeniyle önce sağ alt kadran, rebound ve zıplama testini değerlendirmek, orofarenks muayenesini batın ultrasonografisinden sonraya bırakmak",
                        "is_correct": False,
                        "scenario_update": "Karında peritoneal bulgu saptanmadı; ultrasonografi beklenirken orofarenks muayenesi yapılmadığından tablonun kaynağı bir saat belirsiz kaldı.",
                        "teaching_point": "Ateşli karın ağrısı olan çocukta orofarenks ve servikal lenf nodu muayenesi atlanmamalıdır; karın dışı nedenler sık görülür."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Stratejisi",
                "question": "Tonsiller eksüda, hassas ön servikal lenfadenopati ve öksürük yokluğu olan, karnı rahat bu çocukta tetkik yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Monomükleoz olasılığına karşı periferik yayma ve heterofil antikor testi isteyip sonuç çıkana kadar antibiyotik vermeden izlemek",
                        "is_correct": False,
                        "scenario_update": "Periferik yaymada atipik lenfosit görülmedi, heterofil antikor negatifti; tanı bir gün gecikti.",
                        "teaching_point": "Monomükleoz arka servikal lenfadenopati, hepatosplenomegali ve yorgunlukla seyreder; burada ilk tetkik boğaz sürüntüsüdür."
                    },
                    {
                        "text": "Klinik bulgular tipik olduğu için hiçbir tetkik istemeden ampirik antibiyotik başlamak ve kusma nedeniyle ilk dozu intramüsküler seftriakson olarak yapmak",
                        "is_correct": False,
                        "scenario_update": "Seftriakson enjeksiyonu ağrılı oldu; mikrobiyolojik doğrulama yapılmadığı için tedavinin gerekliliği belirsiz kaldı.",
                        "teaching_point": "Viral farenjitlerle örtüşme nedeniyle klinik skorlar tek başına antibiyotik kararı için yeterli değildir; geniş spektrumlu parenteral tedavi gereksizdir."
                    },
                    {
                        "text": "Boğaz sürüntüsünden hızlı antijen testi yapmak, negatif olursa kültür göndermek; karın bulguları rahat olduğu için batın görüntülemesi istememek",
                        "is_correct": True,
                        "explanation": "Klinik bulgular tek başına bakteriyel ve viral farenjiti güvenle ayıramaz; tedavi kararı hızlı antijen testi veya kültürle verilir. Çocukta negatif hızlı test kültürle doğrulanmalıdır. Peritoneal bulgu olmadığından görüntüleme gerekmez.",
                        "new_finding": "Boğaz sürüntüsü hızlı antijen testi: POZİTİF. Karında bulgu gerilemesi için görüntüleme istenmedi."
                    },
                    {
                        "text": "Akut batını dışlamak için tam kan sayımı, CRP ve batın ultrasonografisi istemek, sonuçlar normalse boğaz sürüntüsü almadan ampirik antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "Lökosit 15.200/mm³, CRP 38 mg/L geldi; ultrasonografide yalnızca reaktif mezenterik lenf nodları görüldü. Etiyoloji doğrulanmadan antibiyotik başlandı.",
                        "teaching_point": "Lökosit ve CRP viral ve bakteriyel farenjiti ayırmaz; antibiyotik kararı mikrobiyolojik doğrulamaya dayanmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Ani ateş, tonsiller eksüda, palatal peteşi, hassas ön servikal lenfadenopati, karın ağrısı ve pozitif hızlı antijen testi olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Adenoviral faringokonjonktival ateş",
                        "is_correct": False,
                        "scenario_update": "Konjonktivit, öksürük ve burun akıntısı yok.",
                        "teaching_point": "Adenovirüs farenjiti konjonktivit ve diğer viral bulgularla birlikte görülür."
                    },
                    {
                        "text": "Akut apandisit",
                        "is_correct": False,
                        "scenario_update": "Karında defans ve rebound yok, çocuk zıplayabiliyor ve tablo orofarenks bulgularıyla açıklanıyor.",
                        "teaching_point": "Farenjite eşlik eden karın ağrısı mezenterik lenfoid yanıtla ilişkilidir; peritoneal bulgu yoksa cerrahi tablo düşünülmez."
                    },
                    {
                        "text": "Akut streptokokal tonsillofarenjit",
                        "is_correct": True,
                        "explanation": "Pozitif hızlı antijen testi ile birlikte tipik klinik bulgular A grubu streptokok tonsillofarenjitini doğrular; karın ağrısı ve kusma bu enfeksiyonda sık görülür.",
                        "new_finding": "Tanı: Akut A Grubu Streptokok Tonsillofarenjiti (karın ağrısı ve kusma ile)."
                    },
                    {
                        "text": "Enfeksiyöz mononükleoz",
                        "is_correct": False,
                        "scenario_update": "Arka servikal lenfadenopati ve splenomegali yok, hızlı antijen testi pozitif.",
                        "teaching_point": "Mononükleozda eksüdatif farenjit olabilir ancak lenfadenopati yaygın ve organomegali eşlik eder."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Oral alabilen bu 22 kg'lık çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Oral amoksisilin-klavulanat 90 mg/kg/gün dozunu üç gün vermek, ateş düşünce kesmek ve bir hafta sonra kontrol boğaz kültürü almak",
                        "is_correct": False,
                        "scenario_update": "Kısa süreli tedavi sonrası iki hafta içinde semptomlar tekrarladı; kontrol kültürü taşıyıcılığı gösterdi ve aile kafası karıştı.",
                        "teaching_point": "Geniş spektrumlu ve kısa süreli tedavi önerilmez; 10 günlük süre eradikasyon ve romatizmal ateşin önlenmesi için gereklidir. Asemptomatik hastada kontrol kültürü yapılmaz."
                    },
                    {
                        "text": "Karın ağrısı ve kusma nedeniyle yatırıp intravenöz ampisilin başlamak, çocuk cerrahisi ile seri muayene planlamak ve kusma kesilince orale geçmek",
                        "is_correct": False,
                        "scenario_update": "Oral alabilen ve karnı rahat çocuk gereksiz yere yatırıldı; ertesi gün cerrahi ekip izlem gerekmediğini belirtti.",
                        "teaching_point": "Oral tolere eden, peritoneal bulgusu olmayan çocukta yatış ve parenteral tedavi gerekmez."
                    },
                    {
                        "text": "Oral azitromisin 12 mg/kg/gün dozunu beş gün vermek, kısa süreli tedavinin uyumu artıracağını anlatmak ve okula üç gün sonra dönmesini önermek",
                        "is_correct": False,
                        "scenario_update": "Makrolid direnci nedeniyle 72. saatte ateş sürüyordu; tedavi amoksisiline değiştirildi.",
                        "teaching_point": "Makrolidler yalnızca ciddi penisilin alerjisinde alternatiftir; direnç oranları yüksek olabilir."
                    },
                    {
                        "text": "Oral amoksisilin 50 mg/kg/gün dozunu iki dozda 10 gün vermek, ateş ve ağrı için parasetamol önermek, antibiyotiğin ilk gününden sonra okula dönüşe izin vermek",
                        "is_correct": True,
                        "explanation": "A grubu streptokok tonsillofarenjitinde amoksisilin 50 mg/kg/gün (maks 1 g/gün) 10 gün etkin ve iyi tolere edilen ilk seçenektir. Tedavinin tamamlanması akut romatizmal ateşi önler; 12-24 saat antibiyotik sonrası bulaştırıcılık belirgin azalır.",
                        "new_finding": "Oral amoksisilin ve parasetamol başlandı. 24 saat sonra ateşi düştü, yutkunması rahatladı; karın ağrısı ve kusması kayboldu. Aile 10 günlük tedaviyi tamamladı."
                    }
                ]
            }
        ]
    }
]
