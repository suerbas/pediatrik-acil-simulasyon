# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - G31-G35 (v2 Şartnamesine Uygun)
"""

CASES = [
    {
        "id": "G31",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "9 Yaş",
        "gender": "Erkek",
        "complaint": "Bir haftadır geçmeyen kuru öksürük, halsizlik, hafif ateş ve baş ağrısı",
        "history": (
            "Dokuz yaşındaki erkek çocuk, yaklaşık bir haftadır devam eden inatçı, kesik kesik kuru öksürük "
            "şikayetiyle getirildi. Ailesi çocuğun okul performansının belirgin düştüğünü, eşlik eden baş ağrısı, "
            "boğazda gıcıklanma ve hafif ateşinin (en yüksek 37.8°C) olduğunu belirtiyor. Evde verilen parasetamol ve "
            "soğuk algınlığı şuruplarına rağmen öksürük nöbetlerinde gerileme olmamış; nefes darlığı, göğüs ağrısı "
            "ya da dudaklarında morarma tarif edilmiyor."
        ),
        "final_diagnosis": "Toplum Kökenli Atipik Pnömoni (Mycoplasma pneumoniae Enfeksiyonu)",
        "disposition": "Yeşil Alandan Ayaktan Oral Makrolid Tedavisi ve Poliklinik Kontrolü ile Taburculuk",
        "case_pearl": (
            "Okul çağı çocuklarında ve adolesanlarda sinsi başlangıçlı inatçı kuru öksürük, baş ağrısı ve subfebril ateşe "
            "eşlik eden bilateral dağınık raller varlığında atipik pnömoni akla gelmelidir. Fizik muayene ve radyolojik "
            "bulgular hastanın genel klinik tablosuna göre beklenenden çok daha belirgindir (klinik-radyolojik diskordans). "
            "Hücre duvarı bulunmayan bu etkene karşı beta-laktamlar etkisiz olup birinci basamak ampirik tedavide oral "
            "makrolidler (klaritromisin veya azitromisin) ilk seçenektir."
        ),
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Bu hastada ilk değerlendirmede odaklanmanız gereken en uygun klinik muayene yaklaşımı hangisidir?",
                "options": [
                    {
                        "text": "Genel durumu ve vital bulguları hızlıca kontrol edip hastayı beklemeden acil bronkodilatatör nebülizasyonu amacıyla Sarı Alana devretmek",
                        "is_correct": False,
                        "scenario_update": "Nebülize salbutamol inhalasyonu sonrasında hastanın kalp tepe atımı 124/dk'ya yükseldi ancak inatçı kuru öksürüğünde ve dinleme bulgularında hiçbir rahatlama sağlanamadı.",
                        "teaching_point": "Solunum sıkıntısı, çekilme ve belirgin bronkospazmı olmayan stabil hastalarda ayırıcı muayene tamamlanmadan Sarı Alana devir ve ampirik bronkodilatatör uygulaması gereksizdir.",
                    },
                    {
                        "text": "Vital bulguları, solunum sayısını, oksijen satürasyonunu ölçmek ve bilateral tüm akciğer alanlarını derin inspiryumda dikkatle dinlemek",
                        "is_correct": True,
                        "explanation": "Okul çağı çocuğunda uzamış öksürük varlığında solunum iş yükü değerlendirilmeli ve fokal veya yaygın akciğer sesleri eksiksiz oskülte edilmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 37.7°C, KTA 86/dk, Solunum Sayısı 20/dk, SpO2 %98 (oda havasında), Kan Basıncı 105/65 mmHg. Çocuk rahat, dispne veya retraksiyon yok. Orofarenks hafif hiperemik. Akciğer oskültasyonunda bilateral alt zonlarda dağınık ince raller ve hafif bilateral ekspiratuar hışıltı duyuldu; tübüler ses veya fokal sessiz alan saptanmadı.",
                    },
                    {
                        "text": "Üst solunum yolu semptomları ön planda olduğundan orofarenks ve otoskopik muayeneyle yetinip akciğer oskültasyonunu derinleştirmeden semptomatik tedaviye geçmek",
                        "is_correct": False,
                        "scenario_update": "Yalnızca orofarenks incelenerek postnazal akıntı tanısıyla gönderilmek istenen hastada derin oskültasyon yapılmadığı için akciğer parankimindeki yaygın raller atlanmış oldu.",
                        "teaching_point": "Bir haftadır süren inatçı öksürük ve baş ağrısı olan okul çağı çocuğunda alt solunum yolu tutulumunu dışlamak için ayrıntılı akciğer oskültasyonu zorunludur.",
                    },
                    {
                        "text": "Ateş ve uzamış öksürüğü olan hastada kardiyopulmoner muayeneyi öteleyip hızlıca damar yolu açarak kan tetkikleri hazırlığına girişmek",
                        "is_correct": False,
                        "scenario_update": "Genel durumu iyi ve satürasyonu normal olan hastada invaziv damar yolu girişimi çocukta aşırı ajitasyon ve strese yol açtı.",
                        "teaching_point": "Hemodinamisi stabil, oda havasında oksijenasyonu normal çocuklarda invaziv girişimlerden önce ayrıntılı fizik muayene ve klinik değerlendirme tamamlanmalıdır.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Radyolojik Görüntüleme Kararı",
                "question": "Akciğer oskültasyonunda bilateral yaygın ince raller ve hafif hışıltı duyulan hastada en uygun tetkik ve görüntüleme yaklaşımı hangisidir?",
                "options": [
                    {
                        "text": "İnfiltrasyon varlığını ve komplikasyonları acil servis şartlarında en duyarlı şekilde netleştirmek için kontrastlı toraks tomografisi çekilmesini planlamak",
                        "is_correct": False,
                        "scenario_update": "Toraks tomografisi çekilmesi hastanın yüksek dozda iyonizan radyasyona maruz kalmasına yol açtı ve klinik yönetimde beklenen ek faydayı sağlamadı.",
                        "teaching_point": "Çocukluk çağı toplum kökenli alt solunum yolu enfeksiyonlarında bilgisayarlı tomografi rutin tanı aracı değildir; gereksiz radyasyon riski taşır.",
                    },
                    {
                        "text": "Akut enfeksiyon odağını dışlamak amacıyla rutin tam kan sayımı, sedimentasyon, CRP ve prokalsitonin düzeylerini içeren geniş biyokimya paneli istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR: WBC 8.400/mm³ (nötrofil %58, lenfosit %34), Hb 13.1 g/dL, PLT 285.000/mm³, CRP 16 mg/L, Prokalsitonin 0.08 ng/mL. Sonuçlar patognomonik ayrım sağlamadı.",
                        "teaching_point": "Klinik tablosu hafif, genel durumu iyi olan okul çağı çocuklarında kan parametreleri bakteriyel ve viral ayrımında özgül değildir.",
                    },
                    {
                        "text": "Akciğer parankim tutulumunu ve infiltrasyon paternini değerlendirmek amacıyla arka-ön (PA) akciğer grafisi çekilmesini talep etmek",
                        "is_correct": True,
                        "explanation": "Oskültasyonda dinleme bulgusu olan ve uzamış öksürüğü bulunan çocukta PA akciğer grafisi parankimal tutulumun yaygınlığını ve paternini göstermede temel incelemedir.",
                        "new_finding": "PA Akciğer Grafisi: Bilateral perihiler belirginleşme, alt zonlarda yaygın retikülonodüler ve peribronşial interstisyel infiltratlar saptandı; lober konsolidasyon veya plevral sıvı izlenmedi.",
                        "image": "assets/images/cxr_atypical_pneumonia.png",
                        "image_caption": "PA Akciğer Grafisi: Bilateral perihiler ve retikülonodüler infiltratlar",
                    },
                    {
                        "text": "Klinik bulguların viral bronşiolit düşündürdüğünü varsayarak hiçbir görüntüleme veya tetkik yapmadan hastayı doğrudan semptomatik tedavilerle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Görüntüleme yapılmadığı için bilateral belirgin interstisyel infiltrasyon tespit edilemedi ve uygun antimikrobiyal başlanması gecikti.",
                        "teaching_point": "Dokuz yaşındaki bir çocukta bir haftadır süren öksürük ve bilateral raller varlığında görüntüleme yapılmadan alt solunum yolu parankim tutulumu dışlanamaz.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik seyri, fizik muayene bulguları ve akciğer grafisi değerlendirildiğinde bu hastada en olası tanı hangisidir?",
                "options": [
                    {
                        "text": "Toplum Kökenli Atipik Pnömoni",
                        "is_correct": True,
                        "explanation": "Okul çağında sinsi seyirli kuru öksürük, subfebril ateş, baş ağrısı ve bilateral retikülonodüler infiltrasyon Mycoplasma pneumoniae kaynaklı atipik pnömoni ile tipiktir.",
                        "new_finding": "Klinik ve radyolojik bulgularla Atipik Pnömoni tanısı doğrulandı.",
                    },
                    {
                        "text": "Pnömokok Kaynaklı Lober Pnömoni",
                        "is_correct": False,
                        "scenario_update": "Lober pnömonide beklenen ani yüksek ateş, toksik görünüm, takipne ve grafide segmental veya lober yoğun konsolidasyon bulguları hastada saptanmadı.",
                        "teaching_point": "Tipik bakteriyel pnömonilerde ani başlangıç, yüksek ateş, taşipne, inleme ve grafide fokal konsolidasyon ile bronkogram bulguları ön plandadır.",
                    },
                    {
                        "text": "Akut Viral Trakeobronşit",
                        "is_correct": False,
                        "scenario_update": "Grafide saptanan belirgin bilateral retikülonodüler ve peribronşial parankim infiltrasyonu basit trakeobronşit tablosunun çok ötesinde parankimal tutuluma işaret etti.",
                        "teaching_point": "Akut bronşitte akciğer grafisi genellikle doğaldır; parankimal interstisyel ve alveoler infiltratların varlığı pnömoni lehinedir.",
                    },
                    {
                        "text": "Yabancı Cisim Aspirasyonu",
                        "is_correct": False,
                        "scenario_update": "Hastada ani gelişen boğulma öyküsü, tek taraflı lokalize havalanma azlığı, atelektazi veya hava hapsi bulgusu izlenmedi.",
                        "teaching_point": "Yabancı cisim aspirasyonu ani başlangıçlı öksürük ve tek taraflı oskültasyon/grafi bulgularıyla seyreder; bir haftalık sinsi enfeksiyöz prodrom beklenmez.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Atipik pnömoni tanısı konulan genel durumu iyi bu çocuk için en uygun tedavi ve taburculuk protokolü hangisidir?",
                "options": [
                    {
                        "text": "Ampirik olarak oral yüksek doz amoksisilin-klavulanat süspansiyon reçete edip yedi gün sonra çocuk hastalıkları polikliniği kontrolüne çağırmak",
                        "is_correct": False,
                        "scenario_update": "Hücre duvarı sentez inhibitörü olan aminopenisilin başlanan hastanın 72 saat sonraki kontrolünde kuru öksürük ve halsizlik yakınmalarında hiçbir gerileme olmadı.",
                        "teaching_point": "Mycoplasma pneumoniae hücre duvarına sahip olmadığından penisilinler, sefalosporinler ve diğer beta-laktam antibiyotiklere yapısal olarak tamamen dirençlidir.",
                    },
                    {
                        "text": "Çocuğu acil serviste müşahedeye alıp intravenöz seftriakson infüzyonu ve eş zamanlı nebülize kortikosteroid tedavisi uygulayarak pediatri servisine yatırmak",
                        "is_correct": False,
                        "scenario_update": "Solunum sıkıntısı ve hipoksemisi olmayan stabil hasta gereksiz yere hastaneye yatırıldı ve etkisiz bir antibiyotik grubuna maruz bırakıldı.",
                        "teaching_point": "Hafif seyirli, oral alımı tam ve satürasyonu normal atipik pnömoni olguları ayaktan oral makrolid tedavisiyle güvenle yönetilebilir; yatış endikasyonu yoktur.",
                    },
                    {
                        "text": "Antibiyotik başlamaksızın yalnızca oral dekstrometorfan içeren antitussif şurup ve antipiretik parasetamol vererek hastayı semptomatik taburculuk planıyla evine göndermek",
                        "is_correct": False,
                        "scenario_update": "Öksürük kesici şurup sekresyonların atılmasını engelleyerek öksürük krizlerini artırdı ve hastanın klinik semptomları iki gün içinde kötüleşti.",
                        "teaching_point": "Çocukluk çağı pnömonilerinde antitussif şurupların yeri yoktur; etiyolojiye yönelik makrolid başlanması klinik iyileşmeyi hızlandırır ve bulaşıcılığı azaltır.",
                    },
                    {
                        "text": "Ayaktan oral makrolid (klaritromisin veya azitromisin) tedavisi planlayıp, hidrasyon ve kırmızı bayrak eğitimiyle kontrole çağırmak",
                        "is_correct": True,
                        "explanation": "Okul çağı atipik pnömonisinde mikoplazmaya etkili ilk seçenek oral makrolidlerdir; genel durumu iyi hasta ayaktan güvenle izlenebilir.",
                        "new_finding": "Hastaya oral klaritromisin tedavisi planlandı, dinlenme ve hidrasyon önerildi; 48-72 saat içinde kontrol veya nefes darlığında acile başvuru anlatıldı.",
                    },
                ],
            },
        ],
    },
    {
        "id": "G32",
        "category": "👁️ Göz Şikayetleri",
        "age": "7 Yaş",
        "gender": "Kız",
        "complaint": "Her iki gözde yoğun kaşıntı, ovuşturma, sulanma ve göz kapaklarında şişlik",
        "history": (
            "Yedi yaşındaki kız çocuk, ilkbahar aylarının başlamasıyla birlikte her iki gözünde yaklaşık 5 gündür "
            "giderek artan şiddetli kaşıntı, sürekli gözlerini ovuşturma, sulanma ve kızarıklık yakınmasıyla getirildi. "
            "Ailesi sabahları çapaklanma olmadığını, göz kapaklarının hafif şiş göründüğünü ve akıntının berrak su gibi "
            "olduğunu ifade ediyor. Çocuğun daha önce bilinen astım veya besin duyarlılığı öyküsü bulunmuyor; ancak son "
            "günlerde açık havada ve parkta vakit geçirdikten sonra göz şikayetlerinin belirginleştiği belirtiliyor. "
            "Görmede bulanıklık, gözde zonklayıcı ağrı veya ateş bildirilmiyor."
        ),
        "final_diagnosis": "Akut Alerjik Konjonktivit",
        "disposition": "Yeşil Alandan Ayaktan Topikal Antihistaminik/Mast Hücre Stabilizatörü ve Korunma Önlemleriyle Taburculuk",
        "case_pearl": (
            "Alerjik konjonktivitin kardinal semptomu yoğun kaşıntı ve gözleri ovuşturmadır. Genellikle bilateral tutulum, "
            "seröz sulanma, kemozis ve tarsal konjonktivada papiller reaksiyon görülür; pürülan çapaklanma ve görme kaybı "
            "beklenmez. Tedavide birinci basamak yaklaşım alerjenden korunma, soğuk kompres, koruyucusuz suni gözyaşı ve "
            "topikal çift etkili H1-antihistaminik / mast hücre stabilizatörü (örn. olopatadin damla) kombinasyonudur. "
            "Göz hekimi kontrolü olmadan topikal kortikosteroidler asla başlanmamalıdır."
        ),
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Oftalmolojik Muayene",
                "question": "Bu hastada göz semptomlarını değerlendirirken ilk aşamada uygulamanız gereken en uygun muayene yaklaşımı hangisidir?",
                "options": [
                    {
                        "text": "Görme keskinliğini test etmeden doğrudan topikal lokal anestezik damlatıp kornea duyarlılığını pamuk uçlu aplikatörle değerlendirmeye odaklanmak",
                        "is_correct": False,
                        "scenario_update": "Topikal anestezik uygulanması geçici rahatlama sağlasa da görme keskinliği baştan belgelenmedi ve gereksiz kornea manipülasyonu huzursuzluğa yol açtı.",
                        "teaching_point": "Tüm göz başvurularında invaziv veya ağrılı işlemlerden önce görme keskinliği mutlaka değerlendirilmeli; rutin anestezik damla kullanılmamalıdır.",
                    },
                    {
                        "text": "Şikayetlerin yalnızca tek bir gözde yoğunlaştığını varsayıp diğer gözü muayene etmeden doğrudan fundus oftalmoskopik incelemesine geçmek",
                        "is_correct": False,
                        "scenario_update": "Oftalmoskop ışığı çocuğun fotofobisini artırırken, her iki göz kapağı ve konjonktiva karşılaştırmalı olarak yeterince incelenemedi.",
                        "teaching_point": "Kaşıntı ve sulanma yakınmalarında bilateral karşılaştırmalı ön segment muayenesi esastır; arka segment incelemesi ilk basamak muayene önceliği değildir.",
                    },
                    {
                        "text": "Görme keskinliğini değerlendirmek, göz kapaklarını, konjonktival hiperemiyi, akıntı niteliğini ve üst kapak tarsal konjonktivasını dikkatle incelemek",
                        "is_correct": True,
                        "explanation": "Bilateral kaşıntı ve sulanmada görme keskinliği belgelenmeli, tarsal papiller yapılar, hiperemi paterni ve çapak niteliği ayırt edilmelidir.",
                        "new_finding": "Görme keskinliği bilateral tam (Snellen 10/10). Göz kapaklarında hafif ödem, bilateral bulber konjonktivada yaygın soluk pembe hiperemi ve hafif kemozis saptandı. Pürülan çapak yok, sulu berrak sekresyon mevcut. Üst göz kapağı eversiyonunda üst tarsal konjonktivada ince diffüz papiller hipertrofi izlendi. Kornea berrak, pupil ışık refleksleri bilateral doğal.",
                    },
                    {
                        "text": "Göz muayenesini inspeksiyonla sınırlı tutup hastayı hızla sedate ederek acil şartlarda genişletilmiş biyomikroskopik yarık lamba incelemesine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Kooperasyonu tam olan yedi yaşındaki çocukta gereksiz sedasyon planlanması aileyi endişelendirdi ve acil servis işleyişini aksattı.",
                        "teaching_point": "Kooperatif çocuklarda sedasyona gerek olmaksızın basit büyüteç, el lambası ve gerekirse biyomikroskopla ayrıntılı ön segment muayenesi rahatlıkla yapılabilir.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve İleri İnceleme Kararı",
                "question": "Bilateral papiller konjonktival hiperemi, berrak sulanma ve yoğun kaşıntısı olan bu çocukta en uygun tetkik yaklaşımı hangisidir?",
                "options": [
                    {
                        "text": "Klinik bulgular tanı için yeterli olduğundan gereksiz laboratuvar tetkiki veya konjonktival sürüntü kültürü almadan tanıya ilerlemek",
                        "is_correct": True,
                        "explanation": "Mevsimsel özellik gösteren, pürülan olmayan kaşıntılı bilateral tablolarda öykü ve tipik muayene tanı koydurucudur, laboratuvar gerekmez.",
                        "new_finding": "Tetkik istenmedi; hastanın klinik ve muayene bulgularının tipik mevsimsel ön segment inflamasyonuyla örtüştüğü belirlendi.",
                    },
                    {
                        "text": "Bakteriyel veya klamidyal patojenleri ekarte etmek amacıyla bilateral konjonktival kazıntı örneği alarak Giemsa ve Gram boyama yaptırmak",
                        "is_correct": False,
                        "scenario_update": "Konjonktivadan invaziv sürüntü ve kazıntı alınması çocukta yoğun ağrıya, submukozal peteşiyel kanamaya ve belirgin huzursuzluğa yol açtı.",
                        "teaching_point": "Pürülan akıntısı veya neonatal dönem öyküsü olmayan çocuklarda ağrılı konjonktival kazıntı veya yayma endike değildir.",
                    },
                    {
                        "text": "Etiyolojiyi saptamak amacıyla acil serviste geniş inhalan spesifik IgE paneli, total IgE ve periferik yaymada eozinofil sayımı istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR: Total IgE 140 IU/mL, Eozinofil %4, tam kan sayımı normal. Spesifik IgE paneli sonuçlarının ise günler sonra çıkacağı öğrenildi.",
                        "teaching_point": "Akut acil başvurularda spesifik IgE veya alerji panelleri yönetimi değiştirmez; bu testler gerekirse elektif poliklinik şartlarında planlanmalıdır.",
                    },
                    {
                        "text": "Sistemik vaskülit ve otoimmün üveit birlikteliğini dışlamak amacıyla ANA, RF, eritrosit sedimentasyon hızı ve HLA-B27 tarama testleri göndermek",
                        "is_correct": False,
                        "scenario_update": "Gönderilen otoantikor ve romatolojik paneller tamamen negatif sonuçlandı; gereksiz kan alımı ve yüksek maliyet dışında katkı sağlamadı.",
                        "teaching_point": "Görme bozukluğu, siliyer enjeksiyon, pupil düzensizliği veya ön kamara hücresi olmayan saf yüzeyel tablolarda sistemik otoimmün tarama endike değildir.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Anamnez, mevsimsel özellikler ve fizik muayene bulguları ışığında bu hastada en olası klinik tanınız nedir?",
                "options": [
                    {
                        "text": "Akut Bakteriyel Konjonktivit",
                        "is_correct": False,
                        "scenario_update": "Bakteriyel enfeksiyonlarda beklenen sabahları göz kapaklarını yapıştıran kalın pürülan akıntı ve mat hiperemi tablosu hastada bulunmadı.",
                        "teaching_point": "Bakteriyel formlarda pürülan sekresyon ve kirpiklerde kabuklanma belirgindir; yoğun kaşıntı ve seröz sulanma ise tipik değildir.",
                    },
                    {
                        "text": "Epidemik Keratokonjonktivit",
                        "is_correct": False,
                        "scenario_update": "Adenoviral keratokonjonktivitte sık rastlanan preauriküler hassas lenfadenopati, korneal subepitelyal infiltratlar ve yoğun ağrı hastada saptanmadı.",
                        "teaching_point": "Viral epidemik tablolarda preauriküler lenf nodu büyümesi, folliküler hipertrofi ve bulaşıcılık belirginken, kaşıntı ana semptom değildir.",
                    },
                    {
                        "text": "Ön Blefarit ve Meibomian Disfonksiyonu",
                        "is_correct": False,
                        "scenario_update": "Kapak kenarlarında kepeklenme, kirpik diplerinde silendirik manşonlar veya meibomian bezi tıkanıklığı muayenede izlenmedi.",
                        "teaching_point": "Blefaritte inflamasyon göz kapağı kenarında ve kirpik diplerinde lokalizedir; konjonktival papiller hipertrofi ve kemozis ön planda olmaz.",
                    },
                    {
                        "text": "Akut Alerjik Konjonktivit",
                        "is_correct": True,
                        "explanation": "Mevsimsel artış, her iki gözde yoğun kaşıntı, berrak sulanma, kemozis ve üst tarsal papiller hipertrofi alerjik konjonktivit için klasiktir.",
                        "new_finding": "Klinik tanı Akut Alerjik Konjonktivit olarak kesinleşti.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Akut alerjik konjonktivit tanısı kesinleşen bu hastanın tedavisinde en uygun yaklaşım ve aile bilgilendirmesi hangisidir?",
                "options": [
                    {
                        "text": "Enflamasyonu hızla baskılamak amacıyla topikal deksametazon damlayı günde dört kez iki hafta süreyle kullanması talimatıyla reçete etmek",
                        "is_correct": False,
                        "scenario_update": "Göz hekimi kontrolü olmaksızın başlanan topikal steroid damla nedeniyle hastada ilerleyen haftalarda intraoküler basınç artışı riski doğdu.",
                        "teaching_point": "Topikal kortikosteroidler katarakt ve glokom gibi ciddi komplikasyon riskleri nedeniyle oftalmolog takibi olmadan acil servisten asla başlanmamalıdır.",
                    },
                    {
                        "text": "Topikal olopatadin damla, koruyucusuz suni gözyaşı, soğuk kompres uygulaması ve gözleri ovuşturmaktan kaçınma eğitimiyle ayaktan taburcu etmek",
                        "is_correct": True,
                        "explanation": "Çift etkili H1-antihistaminik/mast hücre stabilizatörü (olopatadin), suni gözyaşı ve soğuk uygulama kaşıntıyı hızla dindirir ve güvenlidir.",
                        "new_finding": "Reçetesi düzenlenen hastanın ailesine polen mevsiminde pencereleri kapalı tutma, güneş gözlüğü takma ve ovuşturmama uyarısı yapıldı.",
                    },
                    {
                        "text": "Sekonder enfeksiyon gelişimini önlemek amacıyla profilaktik topikal tobramisin damla ile birlikte sistemik birinci kuşak oral antihistaminik şurup başlamak",
                        "is_correct": False,
                        "scenario_update": "Gereksiz antibiyotik kullanımı oküler florayı bozdu; sedatif oral antihistaminik ise okul çağındaki çocukta belirgin uyuklama ve dikkat dağınıklığı yaptı.",
                        "teaching_point": "Alerjik olgularda profilaktik topikal antibiyotiğin yeri yoktur; sistemik birinci kuşak antihistaminikler ise sedasyon yapar ve göz kuruluğunu artırabilir.",
                    },
                    {
                        "text": "Semptomları hızla geriletmek amacıyla gözleri steril gazlı bezle 48 saat kapatıp (oklüzyon pansumanı) kesin istirahat önermek",
                        "is_correct": False,
                        "scenario_update": "Göz kapama işlemi lokal sıcaklığı ve alerjen temas süresini artırarak kaşıntıyı şiddetlendirdi ve çocukta aşırı tedirginliğe yol açtı.",
                        "teaching_point": "Alerjik veya enfeksiyöz oküler inflamasyonlarda gözün kapatılması lokal ısıyı ve nemi artırarak tabloyu kötüleştirir; oklüzyon kontrendikedir.",
                    },
                ],
            },
        ],
    },
    {
        "id": "G33",
        "category": "👁️ Göz Şikayetleri",
        "age": "2.5 Aylık",
        "gender": "Erkek",
        "complaint": "Doğumdan beri sağ gözde sürekli sulanma ve kirpikte hafif mukoid yapışma",
        "history": (
            "İki buçuk aylık erkek bebek, annesi tarafından sağ gözünde neredeyse doğumdan itibaren devam eden "
            "sürekli sulanma, yaşarma ve özellikle sabahları uyanırken kirpik diplerinde hafif yapışkan sarımsı-beyaz "
            "akıntı şikayetiyle getirildi. Annesi sol gözünde hiçbir sorun olmadığını, sağ gözünü ise günde birkaç kez "
            "temizlemek zorunda kaldığını belirtiyor. Bebeğin gözünde kızarıklık, kapaklarda belirgin şişlik veya morarma "
            "tarif edilmiyor. Emmesi, kilo alımı ve genel gelişimi mükemmel olan bebeğin ateşi hiç olmamış; dış merkezde "
            "daha önce verilen antibiyotikli damlalar kullanıldığı sürece akıntıyı azaltmış ancak kesildikten sonra sulanma "
            "aynen devam etmiş."
        ),
        "final_diagnosis": "Konjenital Nazolakrimal Kanal Tıkanıklığı (Dakriyostenoz)",
        "disposition": "Yeşil Alandan Ayaktan Lakrimal Kese Masajı (Crigler Masajı) ve Aile Eğitimi ile Taburculuk",
        "case_pearl": (
            "Süt çocukluğunda doğumdan itibaren görülen, tek veya çift taraflı persistan sulanma ve mukoid akıntının en sık "
            "nedeni Hasner valvinin açılmamasıyla karakterize konjenital nazolakrimal kanal tıkanıklığıdır (dakriyostenoz). "
            "Sklera beyaz, kornea saydamdır ve konjonktival hiperemi eşlik etmez (akut konjonktivitten temel farkı). "
            "Olguların %90'ından fazlası 1 yaşına kadar konservatif izlem ve doğru uygulanan Crigler masajı ile kendiliğinden "
            "düzelir. Akut dakriyosistit (medial kantusta hiperemi, fluktuasyon, ateş) gelişmedikçe rutin profilaktik antibiyotik "
            "veya erken invaziv sondalama önerilmez."
        ),
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Bu bebekte semptomların kaynağını netleştirmek ve acil patolojileri dışlamak için en uygun fizik muayene yaklaşımı hangisidir?",
                "options": [
                    {
                        "text": "Bilateral kornea saydamlığını, sklera ve konjonktivayı incelemek, medial kantal bölgeye nazik bası uygulayarak reflüyü değerlendirmek",
                        "is_correct": True,
                        "explanation": "Tek taraflı sulanmada kornea saydamlığı kontrol edilmeli (glokom dışlanmalı), konjonktivanın sakinliği görülmeli ve kese basısıyla mukoid reflü aranmalıdır.",
                        "new_finding": "Sağ gözde artmış lakrimal göllenme mevcut. Sklera beyaz, bulber konjonktiva tamamen sakin, kızarıklık veya hiperemi yok. Kornea tamamen saydam ve çapı normal (buftalmus bulgusu yok), ışık refleksi doğal. Sağ medial kantal lakrimal kese üzerine işaret parmağıyla basıldığında punktumdan berrak-mukoid sekresyon reflüsü izlendi; lakrimal kese üzerinde eritem, endurasyon veya fluktuasyon yok. Sol göz muayenesi tamamen doğal.",
                    },
                    {
                        "text": "Bebekte konjenital glokomu kesinleştirmek amacıyla acil serviste lokal anestezik eşliğinde doğrudan tonometri ile göz içi basıncı ölçmek",
                        "is_correct": False,
                        "scenario_update": "Bebek ajite oldu ve ağladı; ağlama sırasında ölçülen göz içi basıncı yalancı yüksek çıktı ve gereksiz yere endişe yarattı.",
                        "teaching_point": "Kornea çapı normal, korneası tamamen saydam olan ve fotofobisi bulunmayan bir süt çocuğunda acil invaziv tonometri endike değildir.",
                    },
                    {
                        "text": "Yalnızca dış inspeksiyonla yetinip göz küresine ve lakrimal bölgeye hiç dokunmadan bebeği hızla göz hastalıkları servisine yatırmak",
                        "is_correct": False,
                        "scenario_update": "Medial kantal bası testi yapılmadığı için sekresyonun lakrimal keseden kaynaklandığı anlaşılamadı ve gereksiz yatış talebi konsültan hekimce reddedildi.",
                        "teaching_point": "İnflamatuar odak veya kitle bulgusu olmayan izole sulanmalarda lakrimal kese palpasyonu yapılmalı, yatış yerine ayaktan yönetim planlanmalıdır.",
                    },
                    {
                        "text": "Göz kapağını forsepsle zorlayarak evert etmek ve konjonktiva fornikslerinde gizli yabancı cisim veya forseps travması aramak",
                        "is_correct": False,
                        "scenario_update": "Forsepsle zorlu eversiyon bebeğin konjonktivasında travmatik mikrohematoma ve yoğun ağlamaya yol açarak muayeneyi imkansız hale getirdi.",
                        "teaching_point": "Doğumdan beri süregelen, kapak lezyonu veya akut batma bulgusu olmayan bebeklerde travmatik forseps uygulamaları kontrendikedir.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Yaklaşım Stratejisi",
                "question": "Kornea ve sklerası doğal, yalnızca kese basısıyla punktumdan mukoid reflü veren bu bebekte en uygun tanısal yaklaşım hangisidir?",
                "options": [
                    {
                        "text": "Akut dakriyosistit ve apse formasyonunu ekarte etmek amacıyla acil intravenöz kontrastlı paranazal ve orbita bilgisayarlı tomografisi çektirmek",
                        "is_correct": False,
                        "scenario_update": "Medial kantusta selülit, ısı artışı veya fluktuasyon olmayan bebeğe yüksek doz radyasyon verilmiş oldu ve tomografi normal raporlandı.",
                        "teaching_point": "Medial kantusta eritem, hassasiyet ve kitle gibi akut inflamasyon bulgusu yoksa görüntüleme (BT/MRG) gereksizdir.",
                    },
                    {
                        "text": "Bakteriyel kolonizasyonu tam tanımlamak için punktumdan gelen mukoid sekresyondan acil aerop-anaerop kültür ve antibiyogram örneği göndermek",
                        "is_correct": False,
                        "scenario_update": "Kültürde normal flora elemanı olan koagülaz negatif stafilokok üredi; bu durum gereksiz geniş spektrumlu antibiyotik başlanması ikilemi yarattı.",
                        "teaching_point": "Konjonktival hiperemi ve sistemik bulgu olmayan izole mukoid göllenmelerde rutin sekresyon kültürü yönetimi değiştirmez.",
                    },
                    {
                        "text": "Drenaj yollarının anatomik açıklığını doğrulamak için genel anestezi altında acil dakriyosistografi ve floroskopik kontrast inceleme planlamak",
                        "is_correct": False,
                        "scenario_update": "İki buçuk aylık asemptomatik bebekte gereksiz genel anestezi riski ve floroskopi maruziyeti gündeme gelerek işlem ertelendi.",
                        "teaching_point": "Süt çocuklarında lakrimal sistem radyolojik kontrast incelemeleri invazivdir; komplikasyonsuz olgularda birinci basamakta yeri yoktur.",
                    },
                    {
                        "text": "Ek bir laboratuvar veya görüntüleme tetkiki istemeden, fizik muayene bulgularıyla klinik tanıya varıp aile eğitimine odaklanmak",
                        "is_correct": True,
                        "explanation": "Öykü ve tipik kese bası bulgusuyla klinik tanı kesinleştirilir; infant döneminde komplikasyonsuz olgularda hiçbir tetkik gerekmez.",
                        "new_finding": "Tetkik istenmedi; lakrimal kese bölgesinde inflamasyon veya selülit bulgusu olmadığı, tablonun selim seyirli konjenital süreçle uyumlu olduğu teyit edildi.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Doğumdan beri tek taraflı sulanma, beyaz sklera ve punktum reflüsü olan bu bebekte en olası tanı hangisidir?",
                "options": [
                    {
                        "text": "Akut Bakteriyel Konjonktivit",
                        "is_correct": False,
                        "scenario_update": "Konjonktivitte beklenen belirgin konjonktival hiperemi, kemozis ve yaygın pürülan eksüda bu bebekte mevcut değildi.",
                        "teaching_point": "Bakteriyel konjonktivitte bulber konjonktiva kırmızıdır; skleranın beyaz ve sakin olması akıntının lakrimal göllenmeye bağlı olduğunu gösterir.",
                    },
                    {
                        "text": "Konjenital Nazolakrimal Kanal Tıkanıklığı",
                        "is_correct": True,
                        "explanation": "Doğumdan itibaren tek taraflı epifora, mukoid göllenme, beyaz sklera ve kese basısıyla punktumdan reflü dakriyostenoz için patognomoniktir.",
                        "new_finding": "Klinik tanı Konjenital Nazolakrimal Kanal Tıkanıklığı (Dakriyostenoz) olarak kesinleşti.",
                    },
                    {
                        "text": "Konjenital İnfantil Glokom",
                        "is_correct": False,
                        "scenario_update": "Glokomda görülen korneal bulanıklık (ödem), kornea çapında genişleme (buftalmus) ve belirgin fotofobi hastada saptanmadı.",
                        "teaching_point": "Konjenital glokomda kornea mat ve büyüktür, bebek ışıktan aşırı rahatsız olur; korneanın berrak ve normal çapta olması bu tanıyı dışlar.",
                    },
                    {
                        "text": "Akut Enfeksiyöz Dakriyosistit",
                        "is_correct": False,
                        "scenario_update": "Dakriyosistitte medial kantusta kızarıklık, gergin şişlik, fluktuasyon, yoğun ağrı ve sistemik ateş bulunur; bu bebekte kese sakindir.",
                        "teaching_point": "Dakriyosistit kanal tıkanıklığının akut pürülan ve flegmonöz bir komplikasyonudur; lokal eritem ve kitle olmadan tanı konulamaz.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Aile Eğitimi",
                "question": "Konjenital nazolakrimal kanal tıkanıklığı tanısı alan 2.5 aylık bebeğin yönetiminde en uygun yaklaşım hangisidir?",
                "options": [
                    {
                        "text": "Kanalı mekanik olarak hemen açmak amacıyla bebeğe acil sedasyon altında genel anesteziyle lakrimal kanal sondalaması (probing) uygulamak",
                        "is_correct": False,
                        "scenario_update": "Erken dönemde gereksiz invaziv girişim planlanması ailede büyük tedirginlik yarattı ve anestezi komplikasyonu riski oluşturdu.",
                        "teaching_point": "Konjenital dakriyostenozda spontan düzelme oranı bir yaşına kadar %90'ın üzerindedir; erken sondalama ilk basamakta önerilmez.",
                    },
                    {
                        "text": "Gözdeki mukoid sekresyonu tamamen baskılamak için günde dört kez topikal tobramisin ve deksametazon kombine damlasını bir ay kullandırmak",
                        "is_correct": False,
                        "scenario_update": "Uzun süreli topikal steroid kullanımı bebekte göz içi basınç artışı riski yaratırken, antibiyotik kesildiğinde göllenme aynen devam etti.",
                        "teaching_point": "Akut enfeksiyon olmaksızın rutin topikal antibiyotik veya steroid kullanımı etkisizdir ve dirençli mikroorganizma ile glokom riski taşır.",
                    },
                    {
                        "text": "Ilık suyla temizlik, nazolakrimal kese üzerine Crigler masajı tekniği eğitimi ve bir yaşına kadar konservatif izlem önermek",
                        "is_correct": True,
                        "explanation": "Hasner membranını açmak için günde 2-3 kez uygulanan Crigler masajı (aşağı hidrostatik bası) ve hijyen birinci basamak standart tedavidir.",
                        "new_finding": "Anneye lakrimal keseden aşağıya burun kanadına doğru hidrostatik masaj tekniği gösterildi; akut dakriyosistit uyarı işaretleri anlatılarak taburcu edildi.",
                    },
                    {
                        "text": "Lakrimal yollara silikon tüp entübasyonu yapılması amacıyla hastayı acilen üçüncü basamak oküloplastik cerrahi kliniğine sevk etmek",
                        "is_correct": False,
                        "scenario_update": "Henüz konservatif yöntemler denenmeden üçüncü basamağa sevk edilmesi ailenin gereksiz sağlık kurumu dolaşmasına yol açtı.",
                        "teaching_point": "Silikon tüp entübasyonu veya cerrahi müdahaleler tekrarlayan başarısız sondalamalar sonrası ileri yaşlarda düşünülen invaziv tedavilerdir.",
                    },
                ],
            },
        ],
    },
    {
        "id": "G34",
        "category": "👁️ Göz Şikayetleri",
        "age": "5 Yaş",
        "gender": "Erkek",
        "complaint": "Sağ gözde ani başlayan batma, yabancı cisim hissi, sulanma ve ışıktan rahatsız olma",
        "history": (
            "Beş yaşındaki erkek çocuk, yaklaşık 2 saat önce parkta kum havuzunda oynarken arkadaşının savurduğu "
            "kum ve tozların yüzüne gelmesi sonrası sağ gözünde aniden gelişen şiddetli ağrı, batma hissi, sürekli "
            "göz kırpma, sulanma ve ışığa bakamama şikayetiyle getirildi. Annesi çocuğun sağ gözünü eliyle sürekli "
            "ovuşturmaya çalıştığını, gözünü açmakta çok zorlandığını ve evde suyla yıkamalarına rağmen batma hissinin "
            "hiç geçmediğini ifade ediyor. Çocuğun delici bir cisim teması, göze darbe veya kimyasal madde maruziyeti "
            "öyküsü bulunmuyor."
        ),
        "final_diagnosis": "Korneal Abrazyon (Yüzeyel Kornea Epitel Defekti)",
        "disposition": "Yeşil Alandan Ayaktan Topikal Profilaktik Antibiyotikli Damla, Analjezi ve Kontrol Randevusu ile Taburculuk",
        "case_pearl": (
            "Çocuklarda yabancı cisim veya sürtünme öyküsü sonrası ani başlayan tek taraflı batma, ağrı, fotofobi ve "
            "blefarospazm varlığında korneal abrazyon ilk akla gelmelidir. Muayenede üst ve alt göz kapakları evert "
            "edilerek fornikslerde saklı yabancı cisim taranmalı, ardından vital boyama stripi ve kobalt mavisi ışıkla "
            "epitel defekti gösterilmelidir. Tedavide profilaktik topikal antibiyotik damla ve oral analjezik yeterlidir. "
            "Gözün kapatılması (oklüzyon) epitel rejenerasyonunu geciktirdiği ve enfeksiyon riskini artırdığı için güncel "
            "kılavuzlarda kontrendikedir. Topikal anestezikler toksik keratit riski nedeniyle asla eve reçete edilmemelidir."
        ),
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Parkta gözüne kum kaçtığı belirtilen ve blefarospazmı olan bu çocukta ilk aşamada en uygun muayene yaklaşımı hangisidir?",
                "options": [
                    {
                        "text": "Blefarospazmı aşmak için göz kapaklarını ekartörle zorlayarak aralamak ve kornea yüzeyini steril kuru gazlı bezle silerek temizlemek",
                        "is_correct": False,
                        "scenario_update": "Kuru gazlı bezle mekanik silme girişimi kornea yüzeyel dokusunda ek mikrotravmaya ve çocuğun şiddetli ağlamasına neden oldu.",
                        "teaching_point": "Göz yüzeyi asla kuru gazlı bezle silinmemelidir; kornea epitel bütünlüğünü korumak için nazik irrigasyon ve dikkatli inspeksiyon esastır.",
                    },
                    {
                        "text": "Ayrıntılı ön segment muayenesini yapmadan önce hastaya ağrıyı kesmesi için eve reçete edilmek üzere topikal proparakain damlatmak",
                        "is_correct": False,
                        "scenario_update": "Muayene tamamlanmadan damla verilmesi semptomları maskeledi; topikal anesteziklerin kontrolsüz kullanımı ciddi toksik keratit riski taşır.",
                        "teaching_point": "Topikal anestezikler yalnızca hekim gözetiminde tanısal amaçla tek doz uygulanabilir; evde analjezik amaçlı kullanımı kesinlikle kontrendikedir.",
                    },
                    {
                        "text": "Göz kapaklarını muayene etmeksizin penetran göz yaralanması şüphesiyle çocuğu hiçbir işlem yapmadan doğrudan cerrahi ameliyathaneye sevk etmek",
                        "is_correct": False,
                        "scenario_update": "Basit kum teması olan çocuk gereksiz cerrahi hazırlığa alındı; ön segment ve kapak değerlendirmesi yapılmadığı için süreç aksadı.",
                        "teaching_point": "Öyküde künt veya penetran delici yaralanma mekanizması yoksa, gereksiz sevk öncesinde standart acil ön segment muayenesi tamamlanmalıdır.",
                    },
                    {
                        "text": "Görme keskinliğini değerlendirmek, tek damla anestezik sonrası kapakları evert ederek fornikslerde saklı partikülleri serum fizyolojikle yıkamak",
                        "is_correct": True,
                        "explanation": "Şiddetli blefarospazmda tek damla anestezik muayeneyi kolaylaştırır; kapak eversiyonu fornikste gizli yabancı cisimleri temizlemek için zorunludur.",
                        "new_finding": "Görme keskinliği sol gözde 10/10, sağ gözde fotofobi nedeniyle 8/10. Sağ gözde siliyer ve konjonktival hiperemi mevcut, ön kamara derinliği normal, hifema yok, pupil ışık refleksleri doğal. Üst ve alt göz kapakları evert edilerek forniksler serum fizyolojikle yıkandı; konjonktivada kalıcı yabancı cisim veya çapak izlenmedi.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve İleri İnceleme Kararı",
                "question": "Forniksleri yıkanan ancak kornea yüzeyinde batması devam eden bu çocukta epitel bütünlüğünü değerlendirmek için en uygun adım hangisidir?",
                "options": [
                    {
                        "text": "Göz küresi bütünlüğünü ve intraoküler yabancı cisim varlığını değerlendirmek amacıyla acil bilgisayarlı orbita ve kafa tomografisi çektirmek",
                        "is_correct": False,
                        "scenario_update": "Yüzeyel toz teması olan hastaya çekilen orbita tomografisi normal sonuçlandı; çocuk gereksiz iyonizan radyasyon almış oldu.",
                        "teaching_point": "Metalik veya yüksek enerjili delici yabancı cisim şüphesi bulunmayan yüzeyel irritasyon olgularında bilgisayarlı tomografi endike değildir.",
                    },
                    {
                        "text": "Vital boyama stripi uygulayarak biyomikroskop veya oftalmoskop altında kobalt mavisi filtreli ışıkla kornea epitel yüzeyini incelemek",
                        "is_correct": True,
                        "explanation": "Kobalt mavisi ışık altında vital boyama epitel defektlerini net olarak görünür kılar ve perforasyon bulgusu olan Seidel testine olanak tanır.",
                        "new_finding": "Kobalt mavisi ışık altında kornea alt-orta kadranda yüzeyel epitel defektiyle uyumlu parlak yeşil boyanma izlendi. Ön kamara derinliği doğal, Seidel testi negatif (aköz sızıntısı yok).",
                        "image": "assets/images/corneal_abrasion.png",
                        "image_caption": "Korneal Flöresein İncelemesi: Kornea yüzeyinde lineer epitel abrazyonu",
                    },
                    {
                        "text": "Olası fungal veya bakteriyel keratitleri erkenden tespit etmek için kornea yüzeyinden bistüri ucuyla kazıntı alıp mikrobiyolojiye göndermek",
                        "is_correct": False,
                        "scenario_update": "Akut travmatik yüzeyel defekti olan çocukta korneal kazıntı uygulanması ağrıyı artırdı ve iyileşme sürecini geciktirerek lezyonu derinleştirdi.",
                        "teaching_point": "İnfiltrat veya ülser tablosu olmayan akut travmatik epitel hasarlarında kornea kazıntısı yapılmaz; epitel rejenerasyonuna zarar verir.",
                    },
                    {
                        "text": "Korneal lezyonu doğrulamak amacıyla ultrasonik pakimetri ile kornea kalınlığını ve endotel hücre yoğunluğunu acil serviste cihazla ölçmek",
                        "is_correct": False,
                        "scenario_update": "Pakimetri probunun korneaya teması çocukta yoğun batmaya ve iritasyona yol açtı, yüzey hasarının genişlemesine sebep oldu.",
                        "teaching_point": "Ultrasonik pakimetri veya endotel mikroskopisi akut yüzey epitel defektlerinin acil yönetiminde yeri olmayan elektif oftalmolojik incelemelerdir.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Vital boyama altında korneada yeşil renkli lineer epitel defekti saptanan bu hastada en olası klinik tanı nedir?",
                "options": [
                    {
                        "text": "Bakteriyel Kornea Ülseri",
                        "is_correct": False,
                        "scenario_update": "Kornea ülserinde (mikrobik keratit) beklenen stromal beyaz infiltrat, ön kamarada hipopiyon ve çevre dokuda yoğun nekroz hastada yoktu.",
                        "teaching_point": "Bakteriyel keratitte stromal infiltrasyon ve pürülan eksüda görülür; akut travmatik yüzeyel abrazyonda ise stroma saydamdır.",
                    },
                    {
                        "text": "Akut Ön Üveit",
                        "is_correct": False,
                        "scenario_update": "Ön üveitte görülen siliyer kızarıklık, ön kamara hücresi (tyndall), miyotik ve düzensiz pupil gibi bulgular hastada mevcut değildi.",
                        "teaching_point": "Ön üveit intraoküler inflamasyondur; kornea epitel defekti ve vital boya tutulumu üveitin primer bir bulgusu değildir.",
                    },
                    {
                        "text": "Korneal Abrazyon",
                        "is_correct": True,
                        "explanation": "Toz kaçması öyküsü, ani batma, fotofobi ve vital boyamada yüzeyel epitel defekti görülmesi korneal abrazyon için tanı koydurucudur.",
                        "new_finding": "Klinik tanı Korneal Abrazyon (Yüzeyel Epitel Defekti) olarak kesinleştirildi.",
                    },
                    {
                        "text": "Akut Açı Kapanması Glokomu",
                        "is_correct": False,
                        "scenario_update": "Glokom krizinde izlenen fikse dilate pupil, sığ ön kamara, tahta sertliğinde göz küresi ve kornea epitel ödemi hastada yoktu.",
                        "teaching_point": "Akut glokom çocuklarda son derece nadirdir ve yüksek göz içi basıncıyla seyreder; yüzeyel lineer epitel defekti oluşturmaz.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Taburculuk Protokolü",
                "question": "Korneal abrazyon tanısı alan bu hastanın acil servis tedavisi ve taburculuk planı aşağıdakilerden hangisi olmalıdır?",
                "options": [
                    {
                        "text": "Topikal profilaktik antibiyotik damla, oral analjezik reçete edip, gözü kesinlikle kapatmayarak ertesi gün kontrole çağırmak",
                        "is_correct": True,
                        "explanation": "Topikal antibiyotik sekonder enfeksiyonu önler; gözün kapatılmaması (oklüzyon yapılmaması) epitelin oksijenlenmesini ve hızla iyileşmesini sağlar.",
                        "new_finding": "Hastaya topikal tobramisin damla ve oral analjezik başlandı; gözün kapatılmaması gerektiği tembihlendi ve ertesi gün kontrolü planlandı.",
                    },
                    {
                        "text": "Ağrıyı dindirmek amacıyla göze kırk sekiz saat sıkı basılı göz bandajı uygulayıp antibiyotiksiz şekilde evine göndermek",
                        "is_correct": False,
                        "scenario_update": "Gözün kapatılması kornea yüzeyinde hipoksiye yol açarak epitel iyileşmesini geciktirdi ve bakteriyel süperenfeksiyon riskini belirgin şekilde artırdı.",
                        "teaching_point": "Güncel rehberlere göre korneal abrazyonlarda gözün kapatılması (patching) iyileşmeyi hızlandırmaz, ağrıyı azaltmaz ve enfeksiyon riskini artırır.",
                    },
                    {
                        "text": "Hastanın göz ağrısı oldukça evde kendi kendine damlatması için topikal proparakain içeren lokal anestezik damlayı reçete etmek",
                        "is_correct": False,
                        "scenario_update": "Evde kontrolsüz anestezik kullanan hastada kornea epitel rejenerasyonu durdu ve toksik keratite bağlı kalıcı korneal opasite gelişti.",
                        "teaching_point": "Topikal anesteziklerin reçete edilmesi kornea epitel hücre toksisitesi, kalıcı erozyon ve korneal perforasyon riski nedeniyle kesinlikle kontrendikedir.",
                    },
                    {
                        "text": "Korneadaki reaktif inflamasyonu hızla baskılamak amacıyla topikal deksametazon içeren kortikosteroidli göz damlasını bir hafta boyunca günde altı kez uygulamak",
                        "is_correct": False,
                        "scenario_update": "Steroid damla lokal immün yanıtı baskılayarak epitel defektinin derinleşmesine ve sekonder bakteriyel keratit gelişmesine yol açtı.",
                        "teaching_point": "Epitel defekti varlığında topikal steroid kullanımı enfeksiyonu alevlendirir, yara iyileşmesini bozar ve korneal erimeye neden olabilir.",
                    },
                ],
            },
        ],
    },
    {
        "id": "G35",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "2 Aylık",
        "gender": "Kız",
        "complaint": "Uykuya dalarken kollarda ve bacaklarda ani sıçrama ve titreme hareketleri",
        "history": (
            "İki aylık kız bebek, anne ve babası tarafından uykuya dalma esnasında kollarında ve bacaklarında "
            "ortaya çıkan tekrarlayıcı, hızlı, sıçrama ve atma benzeri hareketler nedeniyle panik halinde acil servise "
            "getirildi. Ailesi bu hareketlerin yaklaşık bir haftadır özellikle gece uykuya dalarken ve hafif uykuda fark "
            "edildiğini, günde birkaç kez 15-30 saniye sürdüğünü ve nöbet geçirdiğinden korktuklarını ifade ediyor. "
            "Anne, bebeğe dokunup uyandırdıklarında veya sıçrayan kolunu/bacağını nazikçe tuttuklarında hareketlerin "
            "hemen durduğunu fark ettiklerini belirtiyor. Uyanıkken bebeğin hareketleri, etrafa ilgisi, gülümsemesi ve "
            "anne sütüyle emmesi tamamen normaldir; ateş, kusma, kafa travması veya ailede erken yaşta epilepsi öyküsü yoktur."
        ),
        "final_diagnosis": "Yenidoğanın / İnfantın Selim Uyku Miyoklonusu (Benign Sleep Myoclonus)",
        "disposition": "Yeşil Alandan Aileye Ayrıntılı Bilgilendirme ve Güvence Verilerek İlaçsız Taburculuk",
        "case_pearl": (
            "Yenidoğanın ve infantın selim uyku miyoklonusu, yalnızca uyku sırasında (özellikle Non-REM uykusunda) "
            "ortaya çıkan, ritmik veya aritmik hızlı sıçramalarla karakterize tamamen fizyolojik ve geçici bir tablodur. "
            "En kritik tanısal ve ayırt edici özelliği: Bebek uyandırıldığında veya sıçrayan ekstremite nazikçe tutulduğunda "
            "hareketlerin anında sonlanmasıdır (epileptik nöbetlerde ekstremiteyi tutmak veya uyandırmak hareketi durdurmaz). "
            "Uyanıkken nörolojik muayene ve gelişim tamamen normaldir, EEG negatiftir. Antiepileptik tedavi kesinlikle "
            "kontrendikedir (fenobarbital veya benzodiazepinler tabloyu kötüleştirebilir). Genellikle yaşamın ilk 6 ayı "
            "içinde kendiliğinden tamamen kaybolur."
        ),
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Uyku sırasında sıçrama şikayetiyle getirilen bu bebekte patolojiyi aydınlatmak için en uygun ilk klinik yaklaşım hangisidir?",
                "options": [
                    {
                        "text": "Ailenin video kaydını ve öyküyü dinlemeksizin bebeği hızla solunum arresti riskiyle entübasyon hazırlığı yaparak resüsitasyon odasına almak",
                        "is_correct": False,
                        "scenario_update": "Genel durumu mükemmel, pembe ve spontan soluyan bebekte agresif resüsitasyon hazırlığı ailede yoğun panik ve travmaya yol açtı.",
                        "teaching_point": "Uyanıkken tamamen normal, vital bulguları stabil ve aktif sıkıntısı olmayan bebeklerde gereksiz invaziv resüsitatif yaklaşımlardan kaçınılmalıdır.",
                    },
                    {
                        "text": "Vital bulguları, uyanıkken nörolojik muayeneyi, primitif refleksleri değerlendirmek ve uykudaki hareketlerin ekstremiteyi tutmakla durup durmadığını sorgulamak",
                        "is_correct": True,
                        "explanation": "Uyanıkken nörolojik normallik ve hareketlerin ekstremite nazikçe tutulduğunda veya uyandığında anında durması fizyolojik ve epileptik olmayan ayrımında anahtardır.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 128/dk, SS 34/dk, SpO2 %99, Kan Şekeri 94 mg/dL. Genel durum çok iyi, etrafla ilgili, aktif hareketli. Fontanel normal bombelikte, baş çevresi persentili %50. Nörolojik muayenede kas tonusu, derin tendon refleksleri, Moro, yakalama ve emme refleksleri tamamen fizyolojik. Ailenin telefonla çektiği video izlendiğinde uykuya dalarken bilateral kollarda senkron ve asenkron ritmik sıçramalar izlendi; anne kolu tuttuğunda hareketin derhal durduğu görüldü.",
                    },
                    {
                        "text": "Hareketleri epileptik status olarak kabul edip damar yolu dahi açılmadan rektal diazepam uygulayarak nöroloji yoğun bakımına sevki başlatmak",
                        "is_correct": False,
                        "scenario_update": "Uykudan uyandırıldığında tamamen normal olan bebeğe gereksiz benzodiazepin uygulanması solunum depresyonuna ve sedasyona yol açtı.",
                        "teaching_point": "Ekstremite tutulmasıyla duran ve uyanıkken görülmeyen hareketler epileptik değildir; gereksiz antiepileptik uygulanması zararlıdır.",
                    },
                    {
                        "text": "Yalnızca kalp seslerini ve batın muayenesini yapıp nörolojik değerlendirmeyi ve hareketin videosunu incelemeyi sonraya ertelemek",
                        "is_correct": False,
                        "scenario_update": "Video kaydı incelenmediği ve nörolojik muayene yapılmadığı için paroksizmal hareketin karakteri ve epileptik olmayan doğası anlaşılamadı.",
                        "teaching_point": "Paroksizmal motor olaylarda aile tarafından çekilen videolar ve ayrıntılı nörolojik muayene en değerli tanısal araçlardır.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Klinik Yaklaşım Stratejisi",
                "question": "Uyanıkken nörolojik muayenesi tamamen doğal olan ve tutmakla duran sıçramaları bulunan bu bebekte en uygun inceleme yaklaşımı hangisidir?",
                "options": [
                    {
                        "text": "Konvülziyon etiyolojisini ve santral sinir sistemi enfeksiyonlarını ekarte etmek amacıyla acil lomber ponksiyon yaparak beyin omurilik sıvısı incelemek",
                        "is_correct": False,
                        "scenario_update": "Ateşi olmayan, uyanıkken aktif ve fontaneli sakin bebeğe invaziv lomber ponksiyon yapılması gereksiz komplikasyon riski yarattı.",
                        "teaching_point": "Sistemik enfeksiyon bulgusu, ateşi veya nörolojik defisiti olmayan, fizyolojik hareket özellikleri taşıyan bebeklerde lomber ponksiyon endike değildir.",
                    },
                    {
                        "text": "İntrakraniyal yapısal anomali veya kanamayı dışlamak amacıyla acil serviste genel anestezi altında kontrastlı kranial manyetik rezonans görüntüleme istemek",
                        "is_correct": False,
                        "scenario_update": "İki aylık sağlıklı bebeğin sedasyon ve anestezi alarak MRG'ye girmesi solunum sekresyon artışına ve hastanede gereksiz kalışa yol açtı.",
                        "teaching_point": "Fokal nörolojik bulgusu olmayan, baş çevresi ve nöromotor gelişimi normal bebeklerde acil kranial MRG gereksiz bir tetkiktir.",
                    },
                    {
                        "text": "Tipik klinik ve video özellikleri doğrultusunda acil invaziv tetkik veya görüntüleme yapmadan selim tabloyu açıklayıp izleme almak",
                        "is_correct": True,
                        "explanation": "Öykü, tutulunca durma özelliği ve normal nörolojik muayene epileptik olmayan fizyolojik süreci gösterir; acil tetkik gerekmez.",
                        "new_finding": "Tetkik istenmedi; paroksizmal olayın yalnızca uykuda ortaya çıkışı ve dokunmakla sonlanmasının selim fizyolojik bir motor fenomene işaret ettiği belirlendi.",
                    },
                    {
                        "text": "Hemen acil 24 saatlik video-EEG monitorizasyonu başlatmak için bebeği üçüncü basamak epilepsi izlem merkezine yatış amacıyla sevk etmek",
                        "is_correct": False,
                        "scenario_update": "Acil sevk edilen bebeğe yapılan rutin uyanıklık ve uyku kayıtlarında epileptiform deşarj saptanmadı; aile aşırı anksiyeteye sürüklendi.",
                        "teaching_point": "Tipik benign tablolarda acil EEG şart değildir; gerek duyulursa elektif şartlarda poliklinik kontrolünde planlanabilir.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Yalnızca uykuda beliren, tutmakla anında duran sıçramaları ve normal nörolojik muayenesi olan bu infantta en olası tanı nedir?",
                "options": [
                    {
                        "text": "Yenidoğanın Selim Uyku Miyoklonusu",
                        "is_correct": True,
                        "explanation": "Yalnızca uykuda görülen, ekstremite tutulunca veya bebek uyanınca derhal duran ve nörolojik gelişimi etkilemeyen tablo selim uyku miyoklonusudur.",
                        "new_finding": "Klinik tanı Yenidoğanın / İnfantın Selim Uyku Miyoklonusu (Benign Sleep Myoclonus) olarak kesinleşti.",
                    },
                    {
                        "text": "İnfantil Spazm Sendromu",
                        "is_correct": False,
                        "scenario_update": "İnfantil spazmda (West sendromu) uyanırken kümelenen ani fleksiyon/ekstansiyon spazmları, hipsaritmi ve gelişimsel duraklama görülür.",
                        "teaching_point": "İnfantil spazmlar uyanıkken kümeler halinde gelir, tutmakla durmaz ve ağır psikomotor gerileme ile EEG'de hipsaritmi eşlik eder.",
                    },
                    {
                        "text": "Erken İnfantil Epileptik Ensefalopati",
                        "is_correct": False,
                        "scenario_update": "Ağır epileptik ensefalopatilerde bebeğin uyanıklığı bozuktur, hipotoni, emme güçlüğü ve tedaviye dirençli multifokal nöbetler mevcuttur.",
                        "teaching_point": "Epileptik ensefalopatilerde ağır nörolojik bozukluk ve kesintisiz nöbet aktivitesi vardır; bu bebek uyanıkken tamamen sağlıklıdır.",
                    },
                    {
                        "text": "Aşırı İrkilme Hastalığı",
                        "is_correct": False,
                        "scenario_update": "Hiperekplekside (aşırı irkilme) burun ucuna vurulduğunda uyanıkken abartılı irkilme ve yaygın hipertoni saptanır; bu hastada test negatiftir.",
                        "teaching_point": "Hiperekpleksi dokunsal/işitsel uyaranla tetiklenen uyanıkken de olan şiddetli spazmdır; uykuda spontan oluşan izole sıçramalardan farklıdır.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Aile Bilgilendirmesi",
                "question": "Selim uyku miyoklonusu tanısı konulan 2 aylık bebeğin acil servis yönetimi ve taburculuk yaklaşımı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Nöbetlerin tekrarlamasını engellemek amacıyla idame oral fenobarbital şurup tedavisi başlayıp bir ay sonra çocuk nörolojisi polikliniğine kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Başlanan fenobarbital miyoklonik hareketleri baskılamadığı gibi bebekte derin sedasyon, emme tembelliği ve solunum ritim bozukluğuna yol açtı.",
                        "teaching_point": "Selim uyku miyoklonusunda antiepileptikler etkisizdir; hatta benzodiazepin ve fenobarbital hareketlerin sıklığını paradoksal olarak artırabilir.",
                    },
                    {
                        "text": "Bebeğin uyku esnasında hipoksiye girebileceği endişesiyle aileye ev tipi kardiyopulmoner monitör cihazı reçete ederek hastaneye yatış planlamak",
                        "is_correct": False,
                        "scenario_update": "Ev tipi monitör sürekli yalancı alarmlar vererek ailenin anksiyetesini ve tükenmişliğini artırdı; bebeğin uykusu gereksiz yere bölündü.",
                        "teaching_point": "Bu durum solunum durması veya kardiyak aritmi yapmaz; ev monitörü endikasyonu yoktur ve ebeveyn kaygısını artırmaktan başka işe yaramaz.",
                    },
                    {
                        "text": "İstemsiz kas spazmlarını çözmek amacıyla oral baklofen damla reçete ederek bebeği acil servisten herhangi bir takip önermeksizin taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Baklofen kullanımı iki aylık bebekte santral hipotoni ve letarji tablosu oluşturarak acil servise tekrar başvuruya neden oldu.",
                        "teaching_point": "Fizyolojik ve selim olan bu durumda hiçbir kas gevşetici veya santral etkili ilacın yeri yoktur; ciddi yan etki doğurur.",
                    },
                    {
                        "text": "İlaç vermeksizin aileyi tablonun selim ve geçici olduğu konusunda rahatlatıp rutin çocuk polikliniği takibiyle taburcu etmek",
                        "is_correct": True,
                        "explanation": "Tablo fizyolojiktir, 6-12 ayda kendiliğinden geçer; aileye güvence vermek, uyanıkken nöbet veya gelişim geriliği olursa başvurmasını tembihlemek esastır.",
                        "new_finding": "Aileye durumun selim doğası açıklandı, hareketlerin genellikle ilk 6 ayda kaybolacağı anlatıldı ve gereksiz ilaçtan kaçınılarak taburcu edildi.",
                    },
                ],
            },
        ],
    },
]
