# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - G66-G70 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "G66",
        "category": "👶 Ağlayan, Emmeyen, Huzursuz Bebek",
        "age": "2 Aylık",
        "gender": "Erkek",
        "complaint": "Her dışkılama öncesi 15-20 dakika yüzü kızararak ıkınma, ağlama ve bacaklarını karnına çekme",
        "history": "Ebeveynleri anlatıyor: 'Yalnızca anne sütü alıyor. İki haftadır kaka yapmadan önce yüzü kıpkırmızı olana kadar ıkınıyor, 15-20 dakika ağlıyor. Sonunda yaptığı kaka yumuşacık, hardal sarısı. Yapınca hemen sakinleşiyor. Kabız diye makatına yağlı kulak çubuğu soktuk, gliserinli fitil verdik ama her seferinde aynı şey oluyor.' Doğumdan sonraki ilk gün mekonyum çıkarmış. Kusma ve ateş yok. Ayda 900 g alıyor. Tartı: 5.4 kg.",
        "final_diagnosis": "İnfant Diskezi (Roma IV)",
        "disposition": "Yeşil Alandan Fizyolojik Sürecin Açıklanması ve Rektal Uyarıların Bırakılması Eğitimi ile Taburculuk",
        "case_pearl": "9 aylıktan küçük, sağlıklı bebekte yumuşak dışkı çıkarmadan önce en az 10 dakika süren ıkınma ve ağlama, karın içi basınç artışı ile pelvik taban gevşemesinin henüz koordine olmamasından kaynaklanır (Roma IV). Dışkının yumuşak olması kabızlığı dışlar. Mekonyumun gecikmemesi, normal büyüme ve normal muayene güvence verir. Rektal uyarı (çubuk, termometre, fitil) bebeği dışkılama için dış uyarıya koşullandırabileceğinden bırakılmalıdır; laksatif gerekmez.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Dışkılama öncesi uzun süre ıkınan ve ağlayan bu 2 aylık bebekte öykü ve muayenede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Mekonyum çıkış zamanını, büyüme eğrisini ve dışkı kıvamını sorgulamak; karın distansiyonu, anüs yeri ve çapı, fissür, anal refleks ve lumbosakral bölgeyi muayene etmek",
                        "is_correct": True,
                        "explanation": "Mekonyum gecikmesi, büyüme geriliği, distansiyon ve anal anomali organik nedenleri (Hirschsprung, anorektal malformasyon, spinal disrafizm) düşündürür. Dışkının yumuşak olması gerçek kabızlığı dışlar.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 128/dk, SS 34/dk. Tartı 5.4 kg (50. persentil). Bebek sakin, gülümsüyor. Karın yumuşak, distansiyon ve kitle yok. Anüs normal yerleşimli ve normal çaplı, fissür yok; anal refleks canlı. Lumbosakral bölgede gamze, kıl tutamı veya leke yok."
                    },
                    {
                        "text": "Ikınmayı kabızlık kabul edip ayrıntılı muayeneye gerek görmeden laktüloz şurubu başlamak, gliserinli fitili her dışkılamada sürdürmelerini önermek",
                        "is_correct": False,
                        "scenario_update": "Laktüloz sonrası dışkı sulandı, gaz ve huzursuzluk arttı; ıkınma süresi değişmedi.",
                        "teaching_point": "Yumuşak dışkı kabızlık değildir; laksatif ve rektal uyarı gereksizdir."
                    },
                    {
                        "text": "Ağlama atakları ve bacaklarını karnına çekmesi nedeniyle invajinasyonu düşünüp acil karın ultrasonografisi istemek ve sonuç gelene kadar emzirmeye ara verip bebeği aç bırakmak",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografi normal geldi; iyi görünümlü bebek iki saat aç bekletildi.",
                        "teaching_point": "Yalnızca dışkılamayla ilişkili, dışkı çıkınca geçen yakınmada invajinasyon düşünülmez; 2 aylık bebekte de nadirdir."
                    },
                    {
                        "text": "Annenin beslenmesinin bebekte gaz yaptığını düşünüp anneye süt, baklagil ve sebze içermeyen kısıtlı diyet önermek ve bir hafta sonra kontrol etmek",
                        "is_correct": False,
                        "scenario_update": "Annenin kısıtlı diyeti emzirmeyi zorlaştırdı; bebeğin yakınmaları değişmedi.",
                        "teaching_point": "Kanıt olmadan annenin diyetini kısıtlamak emzirmeyi tehlikeye atar."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Büyümesi normal, mekonyumu zamanında çıkmış, muayenesi normal ve dışkısı yumuşak olan bu bebekte tetkik yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Tiroid fonksiyon testleri, serum kalsiyum, elektrolitler ve çölyak serolojisi isteyip normal çıkarsa fonksiyonel bir sorun olduğunu söylemek",
                        "is_correct": False,
                        "scenario_update": "Tetkikler normal geldi; yenidoğan taraması zaten normaldi ve kan alımı bebeği çok huzursuz etti.",
                        "teaching_point": "Yalnızca anne sütü alan 2 aylık bebekte çölyak serolojisi anlamsızdır; metabolik tetkikler bu tabloda gereksizdir."
                    },
                    {
                        "text": "Hirschsprung hastalığını dışlamak için kontrastlı kolon grafisi ve rektal emme biyopsisi planlamak, sonuçlara göre aileye bilgi vermek",
                        "is_correct": False,
                        "scenario_update": "Kolon grafisi normal geldi; biyopsi ailenin onayıyla iptal edildi ancak bebek gereksiz radyasyona maruz kaldı.",
                        "teaching_point": "Zamanında mekonyum, yumuşak dışkı ve normal büyüme Hirschsprung olasılığını çok düşürür."
                    },
                    {
                        "text": "Anorektal manometri ile sfinkter fonksiyonunu değerlendirmek için çocuk gastroenterolojisine sevk etmek ve bu sürede fitile devam etmelerini önermek",
                        "is_correct": False,
                        "scenario_update": "Sevk randevusu haftalar sonrasına verildi; fitil uygulamasına devam edildi.",
                        "teaching_point": "Manometri bu tabloda endike değildir; rektal uyarı bırakılmalıdır."
                    },
                    {
                        "text": "Kırmızı bayrakların yokluğunu aileyle gözden geçirip herhangi bir tetkik istememek ve yakınmaların fizyolojik nedenini açıklamaya hazırlanmak",
                        "is_correct": True,
                        "explanation": "Safralı kusma, distansiyon, mekonyum gecikmesi, büyüme geriliği, kanlı dışkı ve anal anomali yokluğunda tanı kliniktir. Tetkik yönetimi değiştirmez ve aile kaygısını artırabilir.",
                        "new_finding": "Kırmızı bayrak saptanmadı. Tetkik istenmedi; ebeveynler gözlem sırasında bebeğin ıkınma sonrası yumuşak dışkı yaptığını ve hemen rahatladığını gördü."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Sağlıklı, iyi büyüyen 2 aylık bebekte yumuşak dışkı çıkarmadan önce 10 dakikadan uzun ıkınma ve ağlama varsa tanı nedir?",
                "options": [
                    {
                        "text": "Hirschsprung hastalığı",
                        "is_correct": False,
                        "scenario_update": "Mekonyum ilk gün çıkmış, distansiyon yok, büyüme normal.",
                        "teaching_point": "Hirschsprung hastalığı gecikmiş mekonyum, distansiyon ve kusmayla seyreder."
                    },
                    {
                        "text": "Fonksiyonel kabızlık",
                        "is_correct": False,
                        "scenario_update": "Dışkı yumuşak ve kıvamı normal; sert, ağrılı dışkılama yok.",
                        "teaching_point": "Kabızlık tanısı sert ve seyrek dışkılama gerektirir."
                    },
                    {
                        "text": "Akut anal fissür",
                        "is_correct": False,
                        "scenario_update": "Perianal muayenede fissür yok, dışkıda kan yok.",
                        "teaching_point": "Fissürde ağrılı dışkılama ve dışkı üzerinde parlak kırmızı kan görülür."
                    },
                    {
                        "text": "İnfant diskezi",
                        "is_correct": True,
                        "explanation": "Roma IV'e göre 9 aydan küçük, sağlıklı bebekte yumuşak dışkı çıkarmadan önce en az 10 dakika süren ıkınma ve ağlama infant diskezisidir.",
                        "new_finding": "Tanı: İnfant Diskezi."
                    }
                ]
            },
            {
                "stage_title": "Aile Eğitimi ve Taburculuk",
                "question": "Bu bebeğin ailesine hangi öneriyi verirsiniz?",
                "options": [
                    {
                        "text": "Simetikon damla ve probiyotik başlamak, karın masajını her öğünden sonra yapmalarını önermek ve yakınma sürerse iki hafta sonra laktüloza geçmek",
                        "is_correct": False,
                        "scenario_update": "Damla ve probiyotik yakınmayı değiştirmedi; aile laktüloz için yeniden başvurdu.",
                        "teaching_point": "Bu tabloda ilaç tedavisinin yararı yoktur; güvence verme ve eğitim yeterlidir."
                    },
                    {
                        "text": "Dışkılamayı kolaylaştırmak için her ağlama ataklarında makata termometre ucu ile nazikçe uyarı vermelerini ve günde bir kez gliserinli fitil kullanmalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Bebek her dışkılama için uyarıya ihtiyaç duyar hale geldi; yakınmalar uzadı.",
                        "teaching_point": "Rektal uyarı bebeğin doğal dışkılama koordinasyonunu öğrenmesini geciktirir."
                    },
                    {
                        "text": "Durumun birkaç haftada kendiliğinden geçeceğini açıklamak, çubuk-fitil gibi rektal uyarıları bırakmalarını ve emzirmeye aynı şekilde devam etmelerini önermek",
                        "is_correct": True,
                        "explanation": "Bebek zamanla karın içi basıncını artırırken pelvik tabanı gevşetmeyi öğrenir. Rektal uyarılar bu öğrenmeyi geciktirir ve bebeği dış uyarıya koşullandırabilir; laksatif ve diyet değişikliği gerekmez.",
                        "new_finding": "Rektal uyarılar bırakıldı. Üç hafta sonraki kontrolde bebek ağlamadan, kısa sürede yumuşak dışkı yapıyordu."
                    },
                    {
                        "text": "Anne sütünün yetersiz olabileceğini düşünüp hidrolize formül mamaya geçmelerini ve dışkıyı yumuşatmak için günde iki kez meyve suyu vermelerini önermek",
                        "is_correct": False,
                        "scenario_update": "Emzirme azaldı, bebek mamayı reddetti ve 2 aylık bebeğe meyve suyu verildi.",
                        "teaching_point": "Emzirme sürdürülmeli; 6 aydan küçük bebeğe meyve suyu önerilmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "G67",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "18 Aylık",
        "gender": "Kız",
        "complaint": "Bez değişiminde vajina girişinin kapalı göründüğünün fark edilmesi ve idrarın ince bir çizgi halinde öne doğru fışkırması",
        "history": "Annesi anlatıyor: 'Dün akşam bezini değiştirirken vajina girişi sanki yokmuş gibi, kapanmış gördüm. Çişini yaparken idrar ince bir çizgi gibi öne doğru fışkırıyor, bazen bezi idrardan sonra da damlıyor. Ateşi yok, ağlamadan çiş yapıyor. Bez bölgesinde sık sık pişik oluyordu. Doğduğunda her şey normaldi, sonradan mı kapandı, ameliyat mı gerekecek çok korktuk.' Büyüme gelişmesi normal. Tartı: 11 kg.",
        "final_diagnosis": "Labial Yapışıklık (Sinekşi)",
        "disposition": "Yeşil Alandan Topikal Östrojen ve Nazik Uygulama Eğitimi, Sonrasında Bariyer Merhem ile Taburculuk",
        "case_pearl": "Bebeklik ve erken çocuklukta düşük östrojen düzeyi ve pişik gibi kronik irritasyonlar labia minoraların orta hatta ince, avasküler bir zarla yapışmasına yol açabilir. Klitoris ve diğer genital yapılar normaldir; bu ayrım konjenital anomalilerden ve cinsel gelişim bozukluklarından ayırmada temeldir. Asemptomatik olgularda tedavi gerekmez. İdrar akımı bozuluyorsa veya enfeksiyon varsa 2-6 hafta topikal östrojen ilk seçenektir; zorla ayırma ağrılıdır ve tekrar riskini artırır. Ayrılma sonrası bariyer merhem tekrarları azaltır.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Vajina girişinin kapalı göründüğü ve idrar akımı değişen bu 18 aylık kızda muayenede neye dikkat edersiniz?",
                "options": [
                    {
                        "text": "Kapalı vajina girişinin cinsel istismara bağlı skar dokusu olduğunu varsayıp adli bildirimi yapmak ve genital muayeneyi adli tıp uzmanına bırakmak",
                        "is_correct": False,
                        "scenario_update": "Adli muayenede travma bulgusu saptanmadı; aile yersiz şüphe nedeniyle ağır bir süreç yaşadı.",
                        "teaching_point": "İnce, avasküler orta hat zarı tipik olarak edinsel benign bir durumdur; istismar şüphesi somut bulgulara dayanmalıdır."
                    },
                    {
                        "text": "Labiaları nazikçe yanlara çekerek yapının niteliğini, idrar çıkış açıklığını, klitoris boyutunu, enfeksiyon veya travma bulgularını değerlendirmek ve istismar açısından öyküyü sorgulamak",
                        "is_correct": True,
                        "explanation": "Nazik lateral traksiyonla zarın inceliği, saydamlığı ve yerleşimi görülür. Klitoris boyutu cinsel gelişim bozukluklarını ayırır; enfeksiyon ve travma bulguları ile öykü istismar şüphesini değerlendirmek için gereklidir.",
                        "new_finding": "Vital Bulgular: Ateş 36.6°C, KTA 98/dk, SS 22/dk. Sakin. Labia minoralar forşetten klitorise doğru orta hatta ince, yarı saydam, avasküler bir zarla birleşik; en üstte 2-3 mm'lik bir açıklık var. Klitoris normal boyutta. Labia majoralar normal, gonad ele gelmiyor. Vulvit, akıntı, ekimoz veya yırtık yok."
                    },
                    {
                        "text": "Ambigus genitalya olasılığı nedeniyle muayeneyi yapmadan çocuk endokrinolojisine acil konsültasyon istemek ve kromozom analizi göndermek",
                        "is_correct": False,
                        "scenario_update": "Konsültan muayenede klitorisin normal olduğunu ve endokrin tetkik gerekmediğini belirtti; aile gereksiz kaygı yaşadı.",
                        "teaching_point": "Muayene yapılmadan endokrinolojik tetkik istenmez; normal klitoris ve gonad yokluğu kız iç genitalyasıyla uyumludur."
                    },
                    {
                        "text": "Muayeneyi kısa tutup kapalı görünen yapıyı açmak için acil serviste pamuklu çubukla bastırarak zarı ayırmak ve ayrılan kenarlara antibiyotikli merhem sürmek",
                        "is_correct": False,
                        "scenario_update": "İşlem çocukta yoğun ağrı ve kanamaya neden oldu; çocuk sonraki muayenelerde çok korktu.",
                        "teaching_point": "Zorla ayırma travmatiktir, ağrılıdır ve yeniden yapışma riski yüksektir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Stratejisi",
                "question": "İdrar akımı değişmiş, ateşsiz ve klitorisi normal olan bu çocukta hangi tetkik uygundur?",
                "options": [
                    {
                        "text": "Bozulan idrar akımı nedeniyle uygun yöntemle alınan idrardan tam idrar tetkiki yapmak, başka tetkik istememek",
                        "is_correct": True,
                        "explanation": "İdrar akımının engellenmesi ve vajinal göllenme idrar yolu enfeksiyonu riskini artırır. Tam idrar tetkiki eşlik eden enfeksiyonu gösterir; genital yapılar normal olduğu için endokrin veya görüntüleme tetkiki gerekmez.",
                        "new_finding": "Tam idrar: dansite 1018, lökosit esteraz ve nitrit negatif, mikroskopide 1-2 lökosit. Enfeksiyon bulgusu yok."
                    },
                    {
                        "text": "Cinsel gelişim bozukluğunu dışlamak için kromozom analizi, 17-OH progesteron, elektrolitler ve testosteron düzeyi istemek, sonuçlar çıkana kadar tedavi kararını ertelemek",
                        "is_correct": False,
                        "scenario_update": "Tetkikler normal geldi; çocuk birkaç hafta tedavisiz kaldı ve idrar akımı sorunu sürdü.",
                        "teaching_point": "Klitoris ve labia majoraları normal çocukta cinsel gelişim bozukluğu tetkiki gerekmez."
                    },
                    {
                        "text": "Herhangi bir tetkik istemeden zarın kendiliğinden açılacağını söyleyip çocuğu ergenliğe kadar izlem için aile hekimine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "İdrar akımı bozuk olduğu halde enfeksiyon değerlendirilmedi ve tedavi önerilmedi.",
                        "teaching_point": "Asemptomatik olgu izlenebilir; idrar akımı bozulmuşsa değerlendirme ve tedavi gerekir."
                    },
                    {
                        "text": "Pelvik ultrasonografi ile uterus ve overleri, işeme sistoüretrografisi ile üretrayı değerlendirmek ve sonuçlara göre çocuk cerrahisi planlamak",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografi normal iç genitalya gösterdi; işeme sistoüretrografisi gereksiz kateterizasyon ve radyasyon içeriyordu.",
                        "teaching_point": "Genital yapıları normal çocukta iç genital ve üriner görüntüleme gerekmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Labia minoraların orta hatta ince, avasküler bir zarla birleştiği, klitorisi normal ve idrar akımı değişen bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "İmperfore himen",
                        "is_correct": False,
                        "scenario_update": "Labia minoralar birbirine yapışık; himen düzeyinde bombeleşen bir zar yok.",
                        "teaching_point": "İmperfore himen genellikle yenidoğanda veya menarş döneminde bombeleşen zarla saptanır."
                    },
                    {
                        "text": "Vulvar liken skleroz",
                        "is_correct": False,
                        "scenario_update": "Vulvada beyaz, atrofik, sekiz şeklinde plak ve kaşıntı yok.",
                        "teaching_point": "Liken skleroz kaşıntılı, porselen beyazı atrofik plaklarla seyreder."
                    },
                    {
                        "text": "Labial yapışıklık (sinekşi)",
                        "is_correct": True,
                        "explanation": "Düşük östrojen düzeyi ve kronik irritasyon zemininde labia minoraların orta hatta ince avasküler zarla birleşmesi edinsel labial yapışıklıktır.",
                        "new_finding": "Tanı: Labial Yapışıklık (Sinekşi), idrar akımını etkileyen."
                    },
                    {
                        "text": "Konjenital adrenal hiperplazi",
                        "is_correct": False,
                        "scenario_update": "Klitoris normal, labioskrotal füzyon ve hiperpigmentasyon yok; doğumda genital yapı normalmiş.",
                        "teaching_point": "Konjenital adrenal hiperplazide doğumdan itibaren klitoromegali ve labioskrotal füzyon görülür."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "İdrar akımı bozulan bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Topikal östrojenli kremi 2-6 hafta, günde 1-2 kez zar hattına pamuklu çubukla hafif bastırarak sürmek; açıldıktan sonra vazelinle bariyer sağlamak",
                        "is_correct": True,
                        "explanation": "Topikal östrojen zarın incelmesini ve kendiliğinden ayrılmasını sağlar; hafif bası etkinliği artırır. Ayrılma sonrası bariyer merhem ve pişik bakımı tekrarı azaltır. Uzun kullanımda geçici meme tomurcuklanması ve labial pigmentasyon olabileceği anlatılır.",
                        "new_finding": "Topikal östrojen ve uygulama tekniği anlatıldı. Üç hafta sonra zarın tamamen ayrıldığı, idrar akımının normale döndüğü görüldü; bariyer merhemle izleme alındı."
                    },
                    {
                        "text": "İdrar yolu enfeksiyonunu önlemek için üç ay düşük doz oral antibiyotik proflaksisi başlamak ve zarın kendiliğinden açılmasını beklemek",
                        "is_correct": False,
                        "scenario_update": "Proflaksi zarı etkilemedi; idrar akımı bozukluğu sürdü ve çocukta gereksiz antibiyotik maruziyeti oldu.",
                        "teaching_point": "Antibiyotik proflaksisi labial yapışmanın tedavisi değildir."
                    },
                    {
                        "text": "Ailenin evde her bez değişiminde labiaları parmaklarıyla kuvvetle yanlara çekerek zarı yavaş yavaş açmasını ve sonrasında antiseptik solüsyonla silmesini önermek",
                        "is_correct": False,
                        "scenario_update": "Ev içi zorlamalar çocukta ağrı, kanama ve bez değişiminden korku oluşturdu; yeniden yapışma gelişti.",
                        "teaching_point": "Zorlayıcı manipülasyon ve antiseptikler irritasyonu artırarak tekrarı kolaylaştırır."
                    },
                    {
                        "text": "Ağrısız ve hızlı çözüm için genel anestezi altında cerrahi olarak zarı ayırmak ve ardından ayrılan kenarları birkaç gün dikişle açık tutmak",
                        "is_correct": False,
                        "scenario_update": "Cerrahi ilk basamak tedavi değildi; çocuk gereksiz anestezi riskine maruz kaldı.",
                        "teaching_point": "Cerrahi ayırma yalnızca topikal tedaviye dirençli ve semptomatik olgularda düşünülür."
                    }
                ]
            }
        ]
    },
    {
        "id": "G68",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "12 Yaşında",
        "gender": "Erkek",
        "complaint": "Üç haftadır okul günleri öğleden sonra başlayan, başın çevresini saran sıkıştırıcı ağrı",
        "history": "Ailesi anlatıyor: 'Üç haftadır hafta içi okuldan çıkınca bütün başını saran, sanki sıkı bir şapka takmış gibi künt bir ağrıdan yakınıyor. Zonklamıyor, bulantısı yok, ışıktan kaçmıyor. Ağrısına rağmen oynayabiliyor. Hafta sonları ve tatilde ağrısı olmuyor. Bu dönemde sınav hazırlığı yoğunlaştı; günde 5-6 saat telefon ve tablet başında, geceleri geç yatıyor, kahvaltı yapmıyor.' Sabah kusması, uykudan uyandıran ağrı veya görme yakınması yok. Tartı: 42 kg.",
        "final_diagnosis": "Epizodik Gerilim Tipi Baş Ağrısı",
        "disposition": "Yeşil Alandan Nörolojik Muayenenin Doğrulanması, Yaşam Tarzı Düzenlemesi, Sınırlı Analjezik ve Baş Ağrısı Günlüğü Eğitimi ile Taburculuk",
        "case_pearl": "Bilateral, bası-sıkıştırma tarzında, hafif-orta şiddetli, günlük aktiviteyle artmayan, bulantısız ağrı gerilim tipi baş ağrısını düşündürür. Normal nörolojik muayene ve fundoskopide görüntüleme gerekmez. Tedavinin temeli tetikleyicilerin (uyku düzensizliği, öğün atlama, yetersiz sıvı, uzun ekran süresi, stres) düzenlenmesidir. Analjezikler (ibuprofen, parasetamol) haftada 2-3 günü geçmemelidir; aksi halde ilaç aşırı kullanım baş ağrısı gelişir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Üç haftadır tekrarlayan baş ağrısı olan bu 12 yaşındaki çocukta muayenede neyi değerlendirirsiniz?",
                "options": [
                    {
                        "text": "Uzun ekran kullanımının gözleri yorduğunu varsayarak yalnızca görme keskinliği ve göz muayenesine odaklanmak, gözlük reçetesi için çocuğu aynı gün göz polikliniğine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Nörolojik muayene ve kan basıncı ölçümü yapılmadı; göz muayenesi normal çıktı ve ağrı sürdü.",
                        "teaching_point": "Kırma kusuru baş ağrısının nadir nedenidir; nörolojik muayene atlanmamalıdır."
                    },
                    {
                        "text": "Ağrı okul günleriyle ilişkili olduğu için okul kaçınmasını düşünüp muayeneyi kısa tutmak ve çocuk psikiyatrisine yönlendirme yapmak",
                        "is_correct": False,
                        "scenario_update": "Nörolojik muayene ve fundoskopi yapılmadan yönlendirme yapıldı; aile çocuğun ağrısının ciddiye alınmadığını düşündü.",
                        "teaching_point": "Psikososyal etkenler önemlidir ancak önce sekonder nedenler muayeneyle dışlanmalıdır."
                    },
                    {
                        "text": "Üç haftadır süren baş ağrısı nedeniyle muayeneden önce kontrastsız beyin tomografisi isteyip sonucu normalse göz doktoruna yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Tomografi normal geldi; çocuk gereksiz radyasyona maruz kaldı ve nörolojik muayene yapılmamıştı.",
                        "teaching_point": "Görüntüleme kararı muayene sonrasında, kırmızı bayraklara göre verilir."
                    },
                    {
                        "text": "Kan basıncını ölçmek, görme keskinliğine ve fundoskopiye bakmak, kraniyal sinir, motor, serebellar ve yürüyüş muayenesi yapmak ve perikraniyal kas hassasiyetini değerlendirmek",
                        "is_correct": True,
                        "explanation": "Hipertansiyon, papilödem, görme ve nörolojik bulgular sekonder nedenleri düşündürür. Perikraniyal kas hassasiyeti birincil baş ağrısı tipini destekleyen bir bulgudur.",
                        "new_finding": "Vital Bulgular: Ateş 36.6°C, KTA 76/dk, TA 105/68 mmHg. Görme keskinliği her iki gözde 10/10. Fundoskopide optik disk sınırları keskin, venöz pulsasyon var. Kraniyal sinirler, motor-duyu, serebellar testler ve tandem yürüyüş normal. Trapez ve boyun arka kaslarında palpasyonla hassasiyet."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Nörolojik muayenesi, fundoskopisi ve kan basıncı normal olan bu çocukta tetkik yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Ağrının nöbet eşdeğeri olabileceğini düşünüp elektroensefalografi istemek ve sonuç çıkana kadar ekran kullanımını tamamen yasaklamak",
                        "is_correct": False,
                        "scenario_update": "EEG normal geldi; tanıya katkısı olmadı ve ani yasak aile içi çatışmaya yol açtı.",
                        "teaching_point": "EEG baş ağrısı değerlendirmesinde rutin değildir."
                    },
                    {
                        "text": "Tam kan sayımı, demir parametreleri, tiroid fonksiyonları, D vitamini ve sedimantasyon isteyip sonuçlara göre tedavi planlamak",
                        "is_correct": False,
                        "scenario_update": "Tetkikler normal geldi; yönetimi değiştirmedi ve çocuk yaşam tarzı önerileri almadan gönderildi.",
                        "teaching_point": "Birincil baş ağrısı tablosunda rutin laboratuvar tetkiki tanıya katkı sağlamaz."
                    },
                    {
                        "text": "Kırmızı bayrakların yokluğunu kayda geçirip tetkik istememek; uyku, öğün, sıvı, ekran süresi ve stres etkenlerini ayrıntılı sorgulamak",
                        "is_correct": True,
                        "explanation": "Normal muayene ve kırmızı bayrak yokluğunda tanı kliniktir. Tetikleyicilerin ayrıntılı sorgulanması tedavinin temelini oluşturur.",
                        "new_finding": "Tetkik istenmedi. Çocuğun gece 01:00'de yattığı, kahvaltı yapmadığı, okulda neredeyse hiç su içmediği ve sınav kaygısı yaşadığı öğrenildi."
                    },
                    {
                        "text": "Arka çukur kitlesini dışlamak için sedasyonsuz beyin manyetik rezonans görüntülemesi planlamak ve sonuç gelene kadar okula gitmemesini önermek",
                        "is_correct": False,
                        "scenario_update": "MR randevusu haftalar sonrasına verildi; çocuk okuldan uzak kaldı ve kaygısı arttı.",
                        "teaching_point": "Kırmızı bayrak yoksa görüntüleme yapılmaz; okula devam desteklenmelidir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bilateral, sıkıştırıcı, hafif-orta şiddetli, bulantısız, okul günleri tekrarlayan ve muayenesi normal olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "İdiyopatik intrakraniyal hipertansiyon",
                        "is_correct": False,
                        "scenario_update": "Papilödem ve görme yakınması yok; ağrı hafta sonları kayboluyor.",
                        "teaching_point": "İdiyopatik intrakraniyal hipertansiyonda papilödem tanının temelidir."
                    },
                    {
                        "text": "Arka çukur tümörü",
                        "is_correct": False,
                        "scenario_update": "Sabah kusması, uykudan uyandıran ağrı, ataksi veya papilödem yok.",
                        "teaching_point": "Kafa içi kitlede ilerleyici ağrı ve nörolojik bulgular beklenir."
                    },
                    {
                        "text": "Epizodik gerilim tipi baş ağrısı",
                        "is_correct": True,
                        "explanation": "Bilateral, bası tarzında, hafif-orta şiddetli, aktiviteyle artmayan ve bulantısız ağrı ile normal muayene ICHD-3 gerilim tipi baş ağrısı kriterlerini karşılar.",
                        "new_finding": "Tanı: Epizodik Gerilim Tipi Baş Ağrısı."
                    },
                    {
                        "text": "Aurasız migren",
                        "is_correct": False,
                        "scenario_update": "Ağrı zonklayıcı değil; bulantı, fotofobi ve fonofobi yok, aktivite ile artmıyor.",
                        "teaching_point": "Migren genellikle zonklayıcı, orta-şiddetli ve bulantı veya ışık-ses hassasiyetiyle birliktedir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuğun tedavi ve izlem planı hangisidir?",
                "options": [
                    {
                        "text": "Düzenli uyku, kahvaltı, sıvı alımı ve ekran molaları önermek; ağrıda ibuprofen veya parasetamolü haftada en fazla 2-3 gün kullanmak ve baş ağrısı günlüğü tutmak",
                        "is_correct": True,
                        "explanation": "Yaşam tarzı düzenlemesi tedavinin temelidir. Analjeziklerin sınırlı kullanımı ilaç aşırı kullanım baş ağrısını önler; günlük, tetikleyicileri ve tedavi yanıtını izlemeyi sağlar. Stres yönetimi gerekirse okul rehberliğiyle desteklenir.",
                        "new_finding": "Aileye yazılı öneriler verildi. İki hafta sonraki kontrolde uyku ve öğün düzeni oturmuş, ekran süresi azalmıştı; çocuk haftada yalnızca bir kez hafif ağrı tanımlıyordu."
                    },
                    {
                        "text": "Boyun kaslarındaki hassasiyet için servikal grafi çekmek, fizik tedaviye yönlendirmek ve okulda ağrı olursa eve gönderilmesini önermek",
                        "is_correct": False,
                        "scenario_update": "Grafi normal geldi; okulda ağrı nedeniyle sık eve gönderilmek okul kaçınmasını pekiştirdi.",
                        "teaching_point": "Görüntüleme gerekmez; ağrı sırasında okulda kalmak ve kısa mola desteklenmelidir."
                    },
                    {
                        "text": "Ağrının tekrarlamasını önlemek için her gün düzenli olarak sabah ve akşam ibuprofen kullanmasını ve ağrı tamamen geçene kadar devam etmesini önermek",
                        "is_correct": False,
                        "scenario_update": "Bir ay düzenli analjezik kullanımı sonrası ağrı neredeyse her gün olmaya başladı.",
                        "teaching_point": "Haftada 2-3 günden sık analjezik kullanımı ilaç aşırı kullanım baş ağrısına yol açar."
                    },
                    {
                        "text": "Ağrıların sıklığı nedeniyle acil serviste koruyucu tedavi olarak gece amitriptilin başlamak, kas gevşetici eklemek ve iki ay sonraki kontrolde yanıta göre dozları artırmayı planlamak",
                        "is_correct": False,
                        "scenario_update": "İlaç sonrası gündüz uykululuk ve okul başarısında düşme gelişti; tetikleyiciler değiştirilmemişti.",
                        "teaching_point": "Profilaktik ilaçlar sık ve yaşam kalitesini bozan ağrılarda, yaşam tarzı düzenlemesinden sonra poliklinikte planlanır."
                    }
                ]
            }
        ]
    },
    {
        "id": "G69",
        "category": "👂 Kulak Ağrısı & KBB",
        "age": "7 Yaşında",
        "gender": "Erkek",
        "complaint": "Burun karıştırma sonrası sağ burun deliğinden yarım saattir süren taze kanama",
        "history": "Annesi anlatıyor: 'Televizyon izlerken parmağıyla burnunu karıştırdı, sağ burnundan kan akmaya başladı. Panikle başını arkaya yatırdım, kanı yutup öğürdü ve pıhtılı kan çıkardı. Ensesine buz koyduk, kanama azaldı ama durmadı.' Kış aylarında evde kalorifer açık ve hava kuru. Daha önce birkaç kez kısa süreli burun kanaması olmuş. Vücutta morluk, diş eti kanaması yok. Ailede kanama hastalığı yok. İlaç kullanmıyor. Tartı: 24 kg.",
        "final_diagnosis": "Anterior Epistaksis (Kiesselbach Pleksusu, Dijital Travma)",
        "disposition": "Yeşil Alanda Doğru Bası Tekniğiyle Kanama Kontrolü, Mukoza Nemlendirme ve Önleme Eğitimi ile Taburculuk",
        "case_pearl": "Çocuklarda burun kanamalarının büyük çoğunluğu septumun ön kısmındaki Kiesselbach pleksusundan kaynaklanır; burun karıştırma ve kuru hava en sık nedenlerdir. Doğru teknik: oturur pozisyonda, baş hafif öne eğik, burnun yumuşak kısmına 10-15 dakika kesintisiz bası. Baş geriye yatırılmaz. Kanama sürerse topikal vazokonstriktör, görünür damarda gümüş nitrat koterizasyonu, son seçenek olarak anterior tampon uygulanır. Kişisel ve ailesel kanama öyküsü yoksa koagülasyon tetkiki gerekmez.",
        "steps": [
            {
                "stage_title": "İlk Müdahale ve Fizik Muayene",
                "question": "Yarım saattir burnu kanayan bu 7 yaşındaki çocukta ilk yapılacak müdahale nedir?",
                "options": [
                    {
                        "text": "Çocuğun başını geriye yatırıp burun kökünü sıkmak, enseye buz koymaya devam etmek ve kanama durana kadar her iki dakikada bir basıyı kaldırıp kontrol etmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk kanı yutmaya devam etti ve kustu; sık kontrol nedeniyle pıhtı oluşamadı ve kanama sürdü.",
                        "teaching_point": "Baş geriye yatırılmaz; bası burnun yumuşak kısmına uygulanmalı ve 10-15 dakika kesintisiz sürdürülmelidir."
                    },
                    {
                        "text": "Kanama yarım saattir sürdüğü için öncelikle kan grubu, tam kan sayımı ve koagülasyon paneli almak ve damar yolu açarak sıvı başlatmak",
                        "is_correct": False,
                        "scenario_update": "Tetkik ve damar yolu işlemleri sırasında kimse burna bası yapmadı; kanama sürdü ve çocuk huzursuzlaştı.",
                        "teaching_point": "Hemodinamisi stabil çocukta ilk adım doğrudan bası ile kanamayı durdurmaktır."
                    },
                    {
                        "text": "Bası denemeden hemen her iki burun deliğine vazelinli gazlı bez ile anterior tampon yerleştirmek ve 48 saat sonra çıkarılmak üzere taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Tampon işlemi çocuk için çok ağrılı oldu ve mukozada ek travmaya neden oldu.",
                        "teaching_point": "Tampon, basıya ve topikal tedaviye yanıt vermeyen kanamalarda son seçenektir."
                    },
                    {
                        "text": "Çocuğu oturtup başını hafif öne eğdirmek, burnun yumuşak kısmına 10-15 dakika kesintisiz bası yapmak ve bu sırada vital bulguları ve kanama miktarını değerlendirmek",
                        "is_correct": True,
                        "explanation": "Öne eğilme kanın yutulmasını ve aspirasyonu önler. Burun kanatlarına sürekli bası ön septumdaki kanama odağını doğrudan sıkıştırır. Vital bulgular kanamanın hemodinamik etkisini gösterir.",
                        "new_finding": "Vital Bulgular: KTA 88/dk, SS 18/dk, SpO2 %100, TA 98/62 mmHg. Çocuk korkmuş ama stabil. 15 dakikalık kesintisiz bası sonrası kanama durdu. Anterior rinoskopide sağ septum ön kısmında küçük mukozal erozyon ve üzerinde pıhtı; mukoza kuru. Orofarinks arka duvarında akan kan yok. Ciltte peteşi, ekimoz yok; hepatosplenomegali yok."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Basıyla kanaması duran, ön septumda erozyon görülen ve kanama öyküsü olmayan bu çocukta tetkik yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Kişisel ve ailesel kanama öyküsünün, ilaç kullanımının ve sistemik kanama bulgularının yokluğunu kayda geçirip laboratuvar tetkiki istememek",
                        "is_correct": True,
                        "explanation": "Lokal nedeni açık, basıyla kontrol edilen ve diğer kanama bulguları (morluk, diş eti kanaması, ailede kanama hastalığı) olmayan anterior kanamada koagülasyon tetkikinin tanısal değeri düşüktür.",
                        "new_finding": "Kanama bulgusu ve aile öyküsü yok; tetkik istenmedi. 20 dakikalık gözlemde kanama tekrarlamadı."
                    },
                    {
                        "text": "Kan yutup kustuğu için gizli kanamayı değerlendirmek amacıyla hemoglobin takibi ve gaitada gizli kan testi istemek",
                        "is_correct": False,
                        "scenario_update": "Hemoglobin 12.6 g/dL geldi; gaitada gizli kan yutulan kan nedeniyle pozitif bulundu ve aile yanlış yönlendirildi.",
                        "teaching_point": "Yutulan burun kanı gaitada gizli kan testini pozitifleştirir; bu durumda test yanıltıcıdır."
                    },
                    {
                        "text": "Altta yatan kitle veya yabancı cismi dışlamak için paranazal sinüs tomografisi çekmek ve kulak burun boğaz konsültasyonu istemek",
                        "is_correct": False,
                        "scenario_update": "Tomografi normal geldi; kanama odağı rinoskopiyle zaten görülmüştü.",
                        "teaching_point": "Tek taraflı kötü kokulu akıntı veya tekrarlayan şiddetli kanama yoksa görüntüleme gerekmez."
                    },
                    {
                        "text": "Tekrarlayan kanama öyküsü nedeniyle tam kan sayımı, PT, aPTT ve von Willebrand paneli istemek ve sonuç gelene kadar çocuğu gözlemde tutmak",
                        "is_correct": False,
                        "scenario_update": "Tüm sonuçlar normal geldi; çocuk saatlerce bekletildi ve aile gereksiz kaygı yaşadı.",
                        "teaching_point": "Kanama odağı belli, kısa süreli ve basıyla duran kanamada, diğer kanama bulguları yoksa tetkik gerekmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Burun karıştırma sonrası tek taraflı, basıyla duran, ön septumda erozyon görülen ve kanama bozukluğu bulgusu olmayan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Posterior epistaksis",
                        "is_correct": False,
                        "scenario_update": "Kanama odağı ön septumda görüldü, farinks arka duvarından akış yok ve kanama basıyla durdu.",
                        "teaching_point": "Posterior kanama çocukta nadirdir, genellikle şiddetlidir ve anterior basıyla durmaz."
                    },
                    {
                        "text": "Von Willebrand hastalığı",
                        "is_correct": False,
                        "scenario_update": "Kişisel ve ailesel kanama öyküsü yok, morluk ve diş eti kanaması yok.",
                        "teaching_point": "Kanama bozukluğu uzun süren, iki taraflı veya diğer bölgelerde kanamayla birlikte seyreden kanamalarda düşünülür."
                    },
                    {
                        "text": "Anterior epistaksis (Kiesselbach pleksusu)",
                        "is_correct": True,
                        "explanation": "Ön septumdaki Kiesselbach pleksusu çocuklarda burun kanamalarının en sık kaynağıdır; dijital travma ve kuru mukoza tipik tetikleyicilerdir.",
                        "new_finding": "Tanı: Anterior Epistaksis (Kiesselbach Pleksusu, dijital travma ve kuru mukoza zemininde)."
                    },
                    {
                        "text": "Juvenil nazofarenks anjiyofibromu",
                        "is_correct": False,
                        "scenario_update": "Burun tıkanıklığı yok, kanama burun karıştırma ile tetiklenmiş ve ön septumdan kaynaklanıyor.",
                        "teaching_point": "Anjiyofibrom ergen erkeklerde tek taraflı burun tıkanıklığı ve tekrarlayan şiddetli kanamayla seyreder."
                    }
                ]
            },
            {
                "stage_title": "Taburculuk ve Önleme Planı",
                "question": "Kanaması duran bu çocuğun taburculuk önerileri hangisidir?",
                "options": [
                    {
                        "text": "Tekrarlayan kanamaları önlemek için acil serviste her iki septum ön kısmına gümüş nitratla koterizasyon uygulamak ve bir hafta burun spreyi kullanmak",
                        "is_correct": False,
                        "scenario_update": "İki taraflı koterizasyon septum perforasyonu riski taşır; kanama durmuş ve aktif damar görülmüyordu.",
                        "teaching_point": "Koterizasyon görünür damar veya basıya dirençli kanamada, tek taraflı ve uygun koşullarda yapılır."
                    },
                    {
                        "text": "Kanama tekrarlarsa evde başını geriye yatırıp burun köküne buz uygulamalarını ve iki gün süreyle burnunu sümkürmemesini, sıcak içecekten kaçınmasını önermek",
                        "is_correct": False,
                        "scenario_update": "Bir sonraki kanamada aile yine başı geriye yatırdı; çocuk kanı yutup kustu ve kanama uzadı.",
                        "teaching_point": "Yanlış tekniğin düzeltilmesi taburculuk eğitiminin en önemli parçasıdır."
                    },
                    {
                        "text": "Burun mukozasına günde iki kez vazelin sürmek, oda havasını nemlendirmek, tırnakları kısa tutup burun karıştırmamak ve doğru bası tekniğini aileye göstermek",
                        "is_correct": True,
                        "explanation": "Mukozanın nemlendirilmesi ve dijital travmadan kaçınma tekrarı önlemede en etkili yöntemlerdir. Aile doğru bası tekniğini öğrendiğinde sonraki kanamaları evde durdurabilir; 20 dakikalık basıya yanıt vermeyen kanamada başvuru gerekir.",
                        "new_finding": "Aileye bası tekniği uygulamalı gösterildi ve nemlendirme önerildi. Bir ay sonraki kontrolde yalnızca bir kez kısa süreli kanama olmuş ve evde basıyla durdurulmuştu."
                    },
                    {
                        "text": "Tekrarı önlemek için anterior tamponu 48 saat yerinde bırakmak, tampon süresince oral amoksisilin-klavulanat vermek ve çıkarmak için kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Kanaması durmuş çocuğa gereksiz tampon ve antibiyotik uygulandı; tampon nedeniyle ağız solunumu ve uyku sorunu yaşadı.",
                        "teaching_point": "Kanaması duran çocukta tampon ve antibiyotik gerekmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "G70",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "8 Yaşında",
        "gender": "Erkek",
        "complaint": "Sağ kolunda ve boynunda iki haftadır genişleyen, kenarları kabarık, hafif kaşıntılı kırmızı halka şeklinde lezyonlar",
        "history": "Annesi anlatıyor: 'İki hafta önce sağ kolunda küçük kırmızı bir sivilce gibi başladı, gün geçtikçe madeni para büyüklüğünde bir halkaya dönüştü. Ortası soldu, kenarı kırmızı, kabarık ve pul pul. Şimdi boynunda da benzeri çıktı. Hafif kaşıntılı. Bir ay önce sokakta bulduğumuz yavru kediyi eve aldık, onun da kulak arkasında tüysüz bir yer var. Eczaneden aldığımız kortizonlu kremi sürünce kızarıklık azaldı ama halka büyümeye devam etti.' Ateş, eklem ağrısı veya kene ısırığı yok. Tartı: 26 kg.",
        "final_diagnosis": "Tinea Korporis (Zoofilik Dermatofit Enfeksiyonu)",
        "disposition": "Yeşil Alandan Topikal Antifungal, Kortizonlu Kremin Bırakılması ve Evcil Hayvanın Tedavisi Eğitimi ile Taburculuk",
        "case_pearl": "Kenarı kabarık, pullu ve aktif, ortası soluk ve santrifüj genişleyen halka lezyon dermatofit enfeksiyonunu düşündürür; yavru kedi veya köpek sık bir kaynaktır (Microsporum canis). Tanı lezyon kenarından alınan kazıntının KOH incelemesiyle desteklenir. Topikal steroid kullanımı tabloyu maskeleyip yaygınlaştırabilir. Sınırlı lezyonlarda topikal terbinafin veya azol, lezyonun 1-2 cm ötesine kadar, temizlendikten sonra 1-2 hafta daha uygulanır. Saçlı deri tutulumu oral tedavi gerektirir; bu yüzden muayeneye mutlaka dahil edilmelidir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Genişleyen halka şeklinde lezyonları olan bu 8 yaşındaki çocukta muayenede neye dikkat edersiniz?",
                "options": [
                    {
                        "text": "Kortizonlu kreme kısmi yanıt verdiği için lezyonu egzama kabul edip daha güçlü bir topikal steroid reçete etmek ve iki hafta sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Güçlü steroidle kızarıklık geçici azaldı ancak lezyonlar genişledi ve yenileri çıktı.",
                        "teaching_point": "Topikal steroid mantar enfeksiyonunu maskeler ve yayılımını kolaylaştırır."
                    },
                    {
                        "text": "Lezyonların sınırını, pul yapısını ve dağılımını incelemek, saçlı deriyi, tırnakları ve kasık bölgesini muayene etmek ve sistemik bulguları sorgulamak",
                        "is_correct": True,
                        "explanation": "Kenarın aktif ve pullu, ortanın soluk olması ayırıcı tanıda belirleyicidir. Saçlı deri ve tırnak tutulumu topikal tedaviyle iyileşmez; varlığı tedavi seçimini değiştirir. Sistemik bulgular eritema migrans gibi diğer halka lezyonları ayırır.",
                        "new_finding": "Vital Bulgular: Ateş 36.6°C, KTA 80/dk. Genel durumu iyi. Sağ ön kolda 3 cm çaplı, keskin sınırlı, kenarı kabarık, eritemli ve ince pullu, ortası soluk halka lezyon; boyun yan yüzünde 1.5 cm benzeri. Saçlı deride saç kaybı, pullanma veya kırık kıl yok. Tırnaklar ve kasık normal. Lenfadenopati, eklem bulgusu yok."
                    },
                    {
                        "text": "Halka şeklindeki lezyonu Lyme hastalığı ile ilişkili kabul edip kene ısırığını yeniden sorgulamak ve muayene etmeden ampirik oral doksisiklin başlamak",
                        "is_correct": False,
                        "scenario_update": "Lezyonlar muayene edilmeden antibiyotik başlandı; pullu kenar ve kedi teması göz ardı edildi.",
                        "teaching_point": "Eritema migransta pullanma beklenmez; halka lezyonlar ayrıntılı dermatolojik muayeneyle ayrılmalıdır."
                    },
                    {
                        "text": "Kedideki tüysüz alan nedeniyle zoonotik bir enfeksiyon olabileceğini düşünüp çocuğu okuldan uzaklaştırmak ve kedinin evden çıkarılmasını önermek",
                        "is_correct": False,
                        "scenario_update": "Çocuk muayene edilmeden okuldan uzaklaştırıldı; aile kediden ayrılmak zorunda kaldı.",
                        "teaching_point": "Bu tabloda okul kısıtlaması gerekmez; evcil hayvan veteriner tarafından tedavi edilebilir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Stratejisi",
                "question": "Saçlı deri ve tırnakları normal, kenarı pullu halka lezyonları olan bu çocukta tanıyı desteklemek için hangi tetkiki yaparsınız?",
                "options": [
                    {
                        "text": "Kesin tanı için lezyonun ortasından 4 mm punch biyopsi alıp histopatoloji ve fungal kültüre göndermek, sonuç gelene kadar tedavi başlamamak",
                        "is_correct": False,
                        "scenario_update": "Biyopsi sonucu iki hafta sonra çıktı; bu sürede lezyonlar genişledi.",
                        "teaching_point": "Biyopsi tipik halka lezyonlarda gerekmez; kazıntı ve KOH yeterlidir. Lezyonun ortası en az verimli bölgedir."
                    },
                    {
                        "text": "Halka şeklinde lezyonlarda Lyme serolojisi ve antinükleer antikor göndermek, sonuçlar negatifse dermatolojiye yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Seroloji negatif geldi; tanıyı destekleyen basit yatak başı tetkik yapılmamıştı.",
                        "teaching_point": "Pullu kenarlı halka lezyonlarda ilk tetkik kazıntı ve KOH incelemesidir."
                    },
                    {
                        "text": "Lezyonun kabarık kenarından lam veya bistüri sırtıyla kazıntı alıp yüzde 10-20 KOH ile hazırlanan preparatı mikroskopta incelemek",
                        "is_correct": True,
                        "explanation": "Fungal elemanlar en yoğun olarak aktif kenarda bulunur. KOH keratini eriterek dallanan septalı hiflerin görülmesini sağlar; basit, hızlı ve ucuz bir yatak başı tetkiktir.",
                        "new_finding": "Kenar kazıntısının KOH incelemesinde dallanan, septalı hifler ve artrokonidi zincirleri görüldü."
                    },
                    {
                        "text": "Lezyondan eküvyonla sürüntü alıp bakteriyel kültür ve antibiyogram göndermek, üreyen etkene göre topikal antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "Kültürde deri florası üredi; topikal antibiyotik lezyonları etkilemedi.",
                        "teaching_point": "Bakteriyel kültür bu tabloda tanıya katkı sağlamaz."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Kedi teması sonrası kenarı kabarık ve pullu, ortası soluk, genişleyen halka lezyonları ve KOH'da septalı hifleri olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Pitriyazis rozea",
                        "is_correct": False,
                        "scenario_update": "Gövdede çam ağacı dağılımı ve öncü madalyon plak yok; KOH pozitif.",
                        "teaching_point": "Pitriyazis rozeada pullanma kenarın iç tarafında yaka şeklindedir ve KOH negatiftir."
                    },
                    {
                        "text": "Granuloma anülare",
                        "is_correct": False,
                        "scenario_update": "Lezyonlar pullu ve kaşıntılı; granuloma anülarede pullanma olmaz.",
                        "teaching_point": "Granuloma anülare pullanmayan, ten renginde papüllerden oluşan halkalarla seyreder."
                    },
                    {
                        "text": "Tinea korporis",
                        "is_correct": True,
                        "explanation": "Santrifüj genişleyen, aktif pullu kenarlı halka lezyonlar, evcil hayvan teması ve KOH'da septalı hifler gövde-ekstremite dermatofit enfeksiyonunu doğrular.",
                        "new_finding": "Tanı: Tinea Korporis (zoofilik, olası Microsporum canis)."
                    },
                    {
                        "text": "Nummüler egzama",
                        "is_correct": False,
                        "scenario_update": "Lezyonların ortası soluk, kenarı aktif ve KOH'da hif görüldü.",
                        "teaching_point": "Nummüler egzamada lezyonun tamamı homojen eritemli ve sızıntılıdır."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuğun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Topikal nistatin kremini günde üç kez bir hafta sürmek, lezyon geçmezse topikal mupirosin eklemek ve kedi ile temasın tamamen kesilmesini önermek",
                        "is_correct": False,
                        "scenario_update": "Nistatin dermatofitlere etkisiz olduğu için lezyonlar genişlemeye devam etti.",
                        "teaching_point": "Nistatin yalnızca Candida'ya etkilidir; dermatofitlerde terbinafin veya azol kullanılır."
                    },
                    {
                        "text": "Topikal terbinafin veya azolü lezyonun 1-2 cm ötesine kadar günde 1-2 kez sürmek, temizlendikten sonra 1-2 hafta sürdürmek, kortizonlu kremi bırakmak ve kediyi veterinere götürmek",
                        "is_correct": True,
                        "explanation": "Sınırlı tutulumda topikal antifungal yeterlidir; klinik iyileşme sonrası devam etmek nüksü önler. Steroid enfeksiyonu yaygınlaştırır. Kaynak hayvan tedavi edilmezse yeniden bulaş olur; okul kısıtlaması gerekmez.",
                        "new_finding": "Topikal terbinafin başlandı, steroid krem bırakıldı, kedi veterinerde tedavi edildi. Üç hafta sonraki kontrolde lezyonlar solmuş, pullanma kaybolmuştu."
                    },
                    {
                        "text": "Kaşıntı ve kızarıklığı hızla azaltmak için steroid-antifungal kombine krem önermek ve iyileşme görüldüğünde kremi hemen bırakmak",
                        "is_correct": False,
                        "scenario_update": "Kombine krem lezyonu baskıladı ancak erken bırakılınca halkalar yeniden genişledi.",
                        "teaching_point": "Steroid içeren kombinasyonlar dermatofit enfeksiyonlarında önerilmez; tedavi iyileşmeden sonra da sürdürülmelidir."
                    },
                    {
                        "text": "Lezyonlar birden fazla olduğu için oral griseofulvin 20-25 mg/kg/gün dozunu 8 hafta vermek, karaciğer fonksiyon testleriyle izlemek ve tedavi bitene kadar okula gitmemesini önermek",
                        "is_correct": False,
                        "scenario_update": "Sınırlı cilt lezyonu için uzun süreli sistemik tedavi gereksizdi; çocuk okuldan uzak kaldı.",
                        "teaching_point": "Oral tedavi saçlı deri, tırnak veya yaygın-dirençli tutulumda gereklidir."
                    }
                ]
            }
        ]
    }
]
