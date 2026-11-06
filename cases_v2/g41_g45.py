# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - G41-G45 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "G41",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "2 Yaşında",
        "gender": "Erkek",
        "complaint": "Dün başlayan sulu ishal, günde 5-6 kez dışkılama ve hafif ateş",
        "history": "Annesi anlatıyor: 'Dün sabah kreşten geldikten sonra sulu, mukussuz, kansız dışkılamaya başladı. Ateşi evde 37.8°C ölçüldü. Dün iki kez kustu ama bugün kusması yok. Su ve çorba içebiliyor, bezini günde 3-4 kez ıslatıyor. Kreşteki birkaç arkadaşında da benzer şikayet varmış. Komşumuz pirinç lapası ve muz dışında bir şey vermememi söyledi.' Tartı: 12.4 kg.",
        "final_diagnosis": "Akut Viral Gastroenterit (Hafif Dehidratasyon)",
        "disposition": "Yeşil Alandan ORS Eğitimi, Yaşa Uygun Beslenme ve Kırmızı Bayrak Eğitimi ile Ayaktan Taburculuk",
        "case_pearl": "Akut viral gastroenteritte dehidratasyon derecesi klinik olarak (genel durum, gözler, mukozalar, turgor, KDZ, idrar çıkışı) belirlenir; hafif dehidratasyonda kan tetkiki ve dışkı kültürü gerekmez. ESPGHAN önerisi düşük osmolariteli ORS ile her sulu dışkı sonrası 10 mL/kg kayıp replasmanı ve kısıtlamasız yaşa uygun beslenmedir; BRAT diyeti, laktozsuz formül rutini ve antidiyareik ilaçlar önerilmez.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Bir gündür sulu dışkılaması olan, oral alımı kısmen korunmuş bu 2 yaşındaki çocukta muayenede önceliğiniz ne olmalıdır?",
                "options": [
                    {
                        "text": "Genel durum, göz küreleri, gözyaşı, mukoza nemi, deri turgoru, kapiller dolum zamanı ve tartıyı değerlendirip batını palpe etmek",
                        "is_correct": True,
                        "explanation": "Sulu ishalli çocukta dehidratasyon derecesi standart klinik bulgularla belirlenir ve tüm yönetim (oral, nazogastrik veya intravenöz sıvı) bu sınıflamaya göre planlanır. Batın muayenesi cerrahi patolojiyi dışlamak için gereklidir.",
                        "new_finding": "Vital Bulgular: Ateş 37.5°C, KTA 112/dk, SS 24/dk, SpO2 %99, KDZ 1.5 sn. Tartı 12.0 kg (2 hafta önceki aşı kontrolünde 12.4 kg). Aktif, oyuncakla ilgileniyor. Göz küreleri normal, ağlarken gözyaşı var, ağız mukozası hafif kuru, turgor anında dönüyor. Karın yumuşak, hassasiyet yok, bağırsak sesleri hiperaktif."
                    },
                    {
                        "text": "Ateş ve kreş öyküsü nedeniyle önce kulak zarları ile orofarenksi detaylı incelemek, hidrasyon değerlendirmesini oral sıvı denemesi sonrasına bırakmak",
                        "is_correct": False,
                        "scenario_update": "Kulak zarları ve orofarenks doğal bulundu. Hidrasyon değerlendirmesi ertelendiği için çocuğun sıvı açığı ve oral tolerans planı ilk saatte netleşmedi.",
                        "teaching_point": "İshalli çocukta ilk hedef sıvı açığının klinik olarak derecelendirilmesidir; odak taraması önemlidir ama hidrasyon değerlendirmesinin yerine geçmez."
                    },
                    {
                        "text": "Kusma öyküsü nedeniyle muayene öncesinde intravenöz ondansetron yapıp ardından sıvı açığını hesaplamak için tartı almak ve batını değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Bugün hiç kusması olmayan çocuğa gereksiz damar yolu açıldı; muayene ve hidrasyon sınıflaması 30 dakika gecikti.",
                        "teaching_point": "Antiemetik yalnızca oral alımı engelleyen aktif kusmada düşünülür ve oral form yeterlidir; önce dehidratasyon derecesi belirlenmelidir."
                    },
                    {
                        "text": "Ateşli ishalde bakteriyemi olasılığını değerlendirmek için muayeneyle eş zamanlı damar yolu açıp hemogram, CRP ve kan kültürü almak",
                        "is_correct": False,
                        "scenario_update": "Damar yolu iki denemede açılabildi; çocuk ajite oldu ve sonrasında sıvı içmeyi reddetti. Hemogram ve CRP sınırda normal geldi, yönetimi değiştirmedi.",
                        "teaching_point": "Genel durumu iyi, kanlı dışkısı olmayan ishalli çocukta rutin kan tetkiki önerilmez; invaziv girişim oral rehidratasyon başarısını da azaltabilir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Tartısında yaklaşık %3 kayıp olan, aktif ve hafif mukozal kuruluğu bulunan bu çocukta hangi tetkik yaklaşımı uygundur?",
                "options": [
                    {
                        "text": "Karın ağrısı ve hiperaktif bağırsak seslerini değerlendirmek için ayakta direkt batın grafisi ve batın ultrasonografisi isteyip cerrahi patolojiyi dışlamak",
                        "is_correct": False,
                        "scenario_update": "Grafide yaygın gaz-sıvı içerikli ince bağırsak ansları görüldü; bulgu non-spesifik olarak raporlandı ve aile kaygılandı.",
                        "teaching_point": "Yumuşak, hassasiyetsiz karın ve sulu ishal tablosunda görüntüleme endike değildir; non-spesifik bulgular gereksiz endişe ve tetkik zincirine yol açar."
                    },
                    {
                        "text": "Ek tetkik istemeden acilde gözetimli oral sıvı denemesi yapmak, kusmadan içebildiğini ve idrar çıkışının sürdüğünü teyit etmek",
                        "is_correct": True,
                        "explanation": "Hafif sıvı kaybı olan, genel durumu iyi ve kanlı dışkısı olmayan çocukta tanı kliniktir. En değerli 'tetkik' gözetimli oral tolerans denemesidir; kan ve dışkı incelemeleri yönetimi değiştirmez.",
                        "new_finding": "Çocuk 1 saat içinde kaşıkla ve bardakla toplam 150 mL düşük osmolariteli ORS içti, kusmadı. Bezini bir kez ıslattı. Gözlem sırasında bir kez sulu, kansız dışkılama oldu."
                    },
                    {
                        "text": "Kreşte benzer olgular bulunduğu için etkenin belirlenmesi amacıyla dışkı kültürü ve viral antijen paneli gönderip sonuca göre tedaviyi düzenlemek",
                        "is_correct": False,
                        "scenario_update": "Dışkı viral antijen testi 2 gün sonra pozitif geldi; sonuç tedaviyi değiştirmedi ve aile kontrol için gereksiz yere tekrar başvurdu.",
                        "teaching_point": "Etken tespiti salgın araştırması veya kanlı ishal dışında bireysel tedaviyi değiştirmez; rutin dışkı tetkiki önerilmez."
                    },
                    {
                        "text": "Hafif sıvı kaybı nedeniyle elektrolit bozukluğu olabileceğini düşünerek venöz kan gazı, sodyum, potasyum ve kan şekeri ölçümü istemek",
                        "is_correct": False,
                        "scenario_update": "Venöz kan gazında HCO3 20 mmol/L, sodyum 137 mEq/L, potasyum 3.9 mEq/L bulundu; sonuçlar normal sınırlarda olup yönetimi değiştirmedi.",
                        "teaching_point": "Elektrolit ölçümü orta-ağır dehidratasyonda, intravenöz sıvı planlanan veya öykü ve muayenesi uyumsuz çocuklarda gereklidir; hafif olguda katkısı yoktur."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Kreş temaslı, akut başlangıçlı sulu ishal, hafif ateş, %3 kilo kaybı ve oral toleransı korunmuş bu çocuktaki en olası tanı nedir?",
                "options": [
                    {
                        "text": "Akut giardiyaz",
                        "is_correct": False,
                        "scenario_update": "Giardiyazda tablo genellikle sinsi başlar; yağlı, kötü kokulu dışkı, şişkinlik ve haftalarca süren şikayetler beklenir.",
                        "teaching_point": "Bir günlük akut sulu ishal ve ateş, protozoon enfeksiyonundan çok viral etiyolojiye uyar."
                    },
                    {
                        "text": "Akut invaziv bakteriyel enterokolit",
                        "is_correct": False,
                        "scenario_update": "İnvaziv bakteriyel enterokolitte genellikle yüksek ateş, kanlı-mukuslu dışkı ve tenezm beklenir; bu çocukta bu bulgular yok.",
                        "teaching_point": "Kansız sulu ishal ve hafif ateş invaziv bakteriyel enfeksiyondan çok viral etkenleri düşündürür."
                    },
                    {
                        "text": "Antibiyotik ilişkili ishal",
                        "is_correct": False,
                        "scenario_update": "Öyküde son 8 haftada antibiyotik kullanımı yok; kreş kümelenmesi bulaşıcı bir etkeni destekliyor.",
                        "teaching_point": "Antibiyotik ilişkili ishal tanısı yakın dönem antibiyotik kullanımı öyküsü gerektirir."
                    },
                    {
                        "text": "Akut viral gastroenterit, hafif dehidratasyon",
                        "is_correct": True,
                        "explanation": "Kreş kümelenmesi, akut sulu kansız ishal ve hafif ateş viral etiyolojiyi düşündürür. %3-5 kilo kaybı, aktif genel durum ve hafif mukozal kuruluk hafif dehidratasyonla uyumludur.",
                        "new_finding": "Tanı: Akut Viral Gastroenterit - Hafif Dehidratasyon (<%5)."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Oral sıvıyı tolere eden bu 12 kg'lık çocuk için en uygun taburculuk önerisi hangisidir?",
                "options": [
                    {
                        "text": "Her sulu dışkı sonrası yaklaşık 120 mL düşük osmolariteli ORS, yaşa uygun normal beslenmeye devam ve dehidratasyon bulguları için dönüş eğitimi vermek",
                        "is_correct": True,
                        "explanation": "ESPGHAN önerisine göre devam eden kayıplar her sulu dışkı sonrası 10 mL/kg ORS ile karşılanır, diyet kısıtlanmaz. Azalan idrar, uykuya meyil, kanlı dışkı veya inatçı kusmada dönüş anlatılır.",
                        "new_finding": "Aileye ORS hazırlanışı gösterildi, yazılı dönüş kriterleri verildi. 48. saatteki telefon kontrolünde ishal sıklığı günde 2'ye indi, çocuk normal besleniyordu."
                    },
                    {
                        "text": "Ateş ve kreş kümelenmesi nedeniyle beş gün oral azitromisin başlamak, ORS ve normal beslenmeyi sürdürmek ve kreşe ara verdirmek",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik başlanan çocukta ikinci gün kusma ve ishal sıklığı arttı; tablo kendi seyrinde dördüncü günde düzeldi.",
                        "teaching_point": "Kansız sulu ishalde ampirik antibiyotik endikasyonu yoktur; yan etki ve direnç riskini artırır."
                    },
                    {
                        "text": "Dışkı sayısını azaltmak için yaşa uygun dozda oral loperamid başlamak, ORS ve normal beslenmeyi sürdürüp üç gün sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Loperamid sonrası çocukta karın şişliği ve uyku hali gelişti; aile acile geri getirdi.",
                        "teaching_point": "Loperamid çocuklarda ileus ve santral sinir sistemi depresyonu riski nedeniyle akut gastroenteritte önerilmez."
                    },
                    {
                        "text": "Barsağı dinlendirmek için 24 saat yalnızca ORS ve pirinç lapası vermek, süt ürünlerini bir hafta kesmek, sonra normal diyete geçmek",
                        "is_correct": False,
                        "scenario_update": "Kısıtlı diyetle çocuk 3 gün sonra halsiz ve iştahsız başvurdu; ishal süresi kısalmadı, kilo kaybı derinleşti.",
                        "teaching_point": "Hafif-orta dehidratasyonda rehidratasyonla birlikte yaşa uygun normal beslenmeye hemen devam edilir; BRAT diyeti ve rutin süt kısıtlaması önerilmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "G42",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "6 Yaşında",
        "gender": "Kız",
        "complaint": "Bir doğum günü partisinden 3 saat sonra başlayan ani, tekrarlayan kusma ve kramp tarzı karın ağrısı",
        "history": "Ailesi anlatıyor: 'Öğleden sonra bir doğum günü partisinde kremalı pasta ve tavuklu sandviç yedi. Eve geldikten kısa süre sonra aniden fışkırır tarzda kusmaya başladı; son 2 saatte 6 kez kustu, su bile içemiyor. Partideki 3 çocukta da aynı saatlerde kusma başlamış. Ateşi yok, henüz ishali olmadı.' Kusmuk safralı veya kanlı değil. Tartı: 20 kg.",
        "final_diagnosis": "Besin Zehirlenmesi (Stafilokoksik Enterotoksin Kaynaklı)",
        "disposition": "Yeşil Alanda Tek Doz Oral Ondansetron + ORS ile Rehidrasyon ve Ayaktan Taburculuk",
        "case_pearl": "Yemekten 1-6 saat sonra başlayan ani şiddetli kusma, kramp ve aynı yemeği yiyenlerde kümelenme S. aureus veya B. cereus kaynaklı hazır toksin aracılı besin zehirlenmesini düşündürür. Tablo 24 saat içinde kendiliğinden geriler; tetkik ve antibiyotik gerekmez. Tek doz oral ondansetron (8-15 kg: 2 mg, 15-30 kg: 4 mg, >30 kg: 8 mg) oral rehidratasyon başarısını artırır. Toplu olgular halk sağlığına bildirilmelidir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Ani başlangıçlı tekrarlayan kusması olan, partideki diğer çocuklarda da benzer şikayet bulunan bu kız çocuğunda ilk değerlendirmede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Kusmuk niteliğini sorgulayıp vital bulguları, hidrasyon durumunu, bilinç düzeyini ve karın muayenesini değerlendirerek cerrahi ve sistemik kırmızı bayrakları dışlamak",
                        "is_correct": True,
                        "explanation": "Akut kusmada safralı veya kanlı kusma, peritoneal irritasyon, bilinç değişikliği ve ağır dehidratasyon gibi kırmızı bayraklar ilk muayenede aranmalıdır; yönetim hidrasyon durumuna göre planlanır.",
                        "new_finding": "Vital Bulgular: Ateş 36.7°C, KTA 108/dk, SS 20/dk, SpO2 %99, TA 98/62 mmHg, KDZ 1.5 sn. Bilinç açık, bulantılı ve halsiz. Ağız mukozası hafif kuru, gözyaşı var. Karın yumuşak, epigastriumda hafif hassasiyet; defans, rebound ve kitle yok. Meningeal irritasyon bulgusu yok."
                    },
                    {
                        "text": "Kusmanın hızla durdurulması için muayeneden önce intramüsküler metoklopramid yapıp bulantı geçtikten sonra karın ve hidrasyon muayenesini tamamlamak",
                        "is_correct": False,
                        "scenario_update": "Metoklopramid sonrası çocukta huzursuzluk ve boyunda istemsiz kasılma gelişti; biperiden gerekti, muayene gecikti.",
                        "teaching_point": "Metoklopramid çocuklarda ekstrapiramidal yan etki riski taşır; antiemetik gerekiyorsa tercih ondansetrondur ve önce muayene yapılmalıdır."
                    },
                    {
                        "text": "Epigastrik ağrı ve kusma nedeniyle muayeneden önce damar yolu açıp tam kan sayımı, amilaz, lipaz ve karaciğer enzimlerini göndermek",
                        "is_correct": False,
                        "scenario_update": "Kan alımı sırasında çocuk iki kez daha kustu. Amilaz, lipaz ve karaciğer enzimleri normal geldi; tetkikler yönetimi değiştirmedi.",
                        "teaching_point": "Öykü ve muayene uyumluyken rutin biyokimya gerekmez; tetkik kararı muayene bulgularına göre verilmelidir."
                    },
                    {
                        "text": "Toplu başvuru nedeniyle olası kimyasal maruziyeti düşünerek önce pupilla, salivasyon ve terleme muayenesi yapıp zehir danışma merkezini aramak",
                        "is_correct": False,
                        "scenario_update": "Pupillalar normal, salivasyon ve terleme artışı yok. Zehir danışma görüşmesi kolinerjik tablo olmadığını teyit etti; hidrasyon değerlendirmesi 20 dakika gecikti.",
                        "teaching_point": "Kolinerjik bulgu olmayan, yemekle zaman ilişkisi net kusmada ilk öncelik hidrasyon ve akut batın değerlendirmesidir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik ve İlk Destek Kararı",
                "question": "Hafif sıvı kaybı olan, karın muayenesi rahat ve ateşsiz bu çocukta tetkik ve ilk destek yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Karın ağrısının cerrahi nedenlerini ekarte etmek için batın ultrasonografisi isteyip sonuç çıkana kadar oral alımı tamamen kapalı tutmak",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografi 2 saat sonra çekildi ve normaldi. Bu sürede oral alımı kapatılan çocuğun ağız kuruluğu belirginleşti.",
                        "teaching_point": "Yumuşak karın ve kısa süreli kramp tarzı ağrıda görüntüleme gerekmez; oral alımın gereksiz kesilmesi dehidratasyonu derinleştirir."
                    },
                    {
                        "text": "Kan tetkiki istemeden kiloya uygun tek doz oral ondansetron vermek ve yarım saat sonra küçük yudumlarla ORS denemesi başlatmak",
                        "is_correct": True,
                        "explanation": "Hafif dehidratasyonlu ve kırmızı bayrağı olmayan kusmada laboratuvar tetkiki gerekmez. Tek doz oral ondansetron kusmayı azaltır, oral rehidratasyon başarısını artırır ve intravenöz sıvı ihtiyacını düşürür.",
                        "new_finding": "20 kg için 4 mg oral dağılan ondansetron verildi. 30 dakika sonra 5 dakikada bir 10-15 mL ORS başlandı; 1 saatte 200 mL içti, kusmadı. Bir kez sulu dışkılama oldu."
                    },
                    {
                        "text": "Altı kez kusma nedeniyle damar yolu açıp elektrolitleri göndermek ve 20 mL/kg serum fizyolojik bolusunu ardından idame sıvıyla sürdürmek",
                        "is_correct": False,
                        "scenario_update": "Elektrolitler normal geldi. İntravenöz sıvı sırasında çocuk 3 saat acilde kaldı; oral alım hiç denenmediği için taburculuk gecikti.",
                        "teaching_point": "Hafif dehidratasyonda ilk seçenek oral rehidratasyondur; intravenöz sıvı oral tedavinin başarısız olduğu veya ağır dehidratasyonda gerekir."
                    },
                    {
                        "text": "Partideki diğer çocuklarla kümelenme olduğu için dışkı kültürü ve kusmuk örneğinden toksin analizi isteyip sonuçlar gelene dek gözlemde tutmak",
                        "is_correct": False,
                        "scenario_update": "Çocuğun ishali olmadığından dışkı örneği alınamadı; kusmuk örneği laboratuvarca kabul edilmedi ve gözlem süresi gereksiz uzadı.",
                        "teaching_point": "Örnekleme salgın araştırmasında halk sağlığı birimince planlanır; bireysel hastanın acil yönetimini değiştirmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Yemekten 1-3 saat sonra başlayan ani kusma, kramp, ateş yokluğu ve aynı yemeği yiyenlerde kümelenme varlığında en olası tanı nedir?",
                "options": [
                    {
                        "text": "Stafilokok enterotoksini kaynaklı besin zehirlenmesi",
                        "is_correct": True,
                        "explanation": "Kremalı tatlı ve tavuklu sandviç gibi oda ısısında bekleyen gıdalarda S. aureus'un ürettiği ısıya dayanıklı enterotoksin 1-6 saat içinde ani kusma ve kramp yapar; ateş genellikle yoktur ve tablo 24 saatte geriler.",
                        "new_finding": "Tanı: Stafilokokal Enterotoksin Kaynaklı Akut Besin Zehirlenmesi. Toplu olgu nedeniyle İl Sağlık Müdürlüğüne bildirim yapıldı."
                    },
                    {
                        "text": "Salmonella gastroenteriti",
                        "is_correct": False,
                        "scenario_update": "Salmonella enfeksiyonunda kuluçka süresi 6-72 saattir ve tabloya genellikle ateş ile ishal hakimdir.",
                        "teaching_point": "Ateşsiz, birkaç saat içinde başlayan kusma baskın tablo invaziv bakteriyel enfeksiyondan çok toksin aracılıdır."
                    },
                    {
                        "text": "Diyabetik ketoasidoz",
                        "is_correct": False,
                        "scenario_update": "Poliüri-polidipsi öyküsü, Kussmaul solunumu ve hiperglisemi yok; kümelenen olgular metabolik bir nedenle açıklanamaz.",
                        "teaching_point": "Kusan çocukta ketoasidoz akılda tutulmalıdır ancak toplu ve zamanla ilişkili başvuru ortak maruziyeti gösterir."
                    },
                    {
                        "text": "Akut viral gastroenterit",
                        "is_correct": False,
                        "scenario_update": "Viral gastroenterit de kümelenebilir ancak kuluçka süresi genellikle 12-48 saattir; tüm çocukların aynı saatlerde başlaması ortak gıda maruziyetini düşündürür.",
                        "teaching_point": "Birkaç saatlik kısa kuluçka ve ortak yemek, bulaşıcı virüsten çok hazır toksin aracılı tabloyu düşündürür."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Ondansetron sonrası ORS'yi tolere eden bu çocuğun taburculuk planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Ortak gıda kaynağı ve kümelenme nedeniyle ampirik beş günlük oral siprofloksasin başlayıp ORS ve normal beslenme ile taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik toksin aracılı tabloya etki etmedi; çocuk ikinci gün antibiyotiğe bağlı bulantı ile tekrar başvurdu.",
                        "teaching_point": "Hazır toksinle oluşan besin zehirlenmesinde bakteri invazyonu yoktur; antibiyotik endikasyonu bulunmaz."
                    },
                    {
                        "text": "Evde kullanmak üzere üç gün boyunca günde iki kez oral ondansetron reçete edip ORS ile normal beslenmeyi sürdürmesini önermek",
                        "is_correct": False,
                        "scenario_update": "Kusması zaten 12 saatte duran çocuğa verilen tekrarlayan dozlar sonrası ishal sıklığı arttı.",
                        "teaching_point": "Ondansetronun kanıtı acilde tek doz kullanım içindir; evde çoklu doz rutin önerilmez ve ishali artırabilir."
                    },
                    {
                        "text": "Sıvı açığını güvenceye almak için tolere etse de 6 saat intravenöz idame sıvı vererek gözlemlemek ve sabah taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Oral alımı iyi olan çocuk gereksiz yere gece boyunca acilde kaldı; serum yerinde flebit gelişti.",
                        "teaching_point": "Oral toleransı sağlanmış hafif dehidratasyonlu çocuk ayaktan izlenir; gereksiz intravenöz sıvı ve uzun gözlem komplikasyon riskini artırır."
                    },
                    {
                        "text": "ORS ve yaşa uygun beslenmeye devam, kusma tekrarlarsa küçük yudumlar, kırmızı bayrak eğitimi ve toplu olgu nedeniyle halk sağlığına bildirim yapmak",
                        "is_correct": True,
                        "explanation": "Tablo kendini sınırlar; destek tedavi yeterlidir. Safralı veya kanlı kusma, uykuya meyil, idrar azalması ya da 24 saati aşan şikayetlerde dönüş anlatılır. Ortak kaynaklı toplu olgular bildirimi zorunlu durumlardır.",
                        "new_finding": "Çocuk ayaktan taburcu edildi. Ertesi gün aile ile yapılan görüşmede kusmasının gece kesildiği, sabah kahvaltı yaptığı öğrenildi. Partideki diğer çocuklar da 24 saat içinde iyileşti."
                    }
                ]
            }
        ]
    },
    {
        "id": "G43",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "5 Yaşında",
        "gender": "Erkek",
        "complaint": "Bir aydır iç çamaşırını sık sık kirletme, karın şişliği ve tuvalete gitmek istememe",
        "history": "Annesi anlatıyor: 'Yaklaşık 1 aydır külodunu kirletiyor, çamur kıvamında lekeler buluyorum, ishal mi diye düşündük. Ama tuvalette haftada bir kez kalın, sert dışkı yapıyor, bazen tuvaleti tıkıyor. Tuvalete oturmak istemiyor, bacaklarını çaprazlayıp parmak ucunda kasılarak bekliyor. Ara ara karnı ağrıyor, iştahı azaldı. Kreşte arkadaşları kokudan dolayı onunla dalga geçiyor.' Yenidoğan döneminde mekonyumunu ilk gün çıkarmış. Kilo-boy gelişimi persentilinde.",
        "final_diagnosis": "Fonksiyonel Kabızlık, Fekal İmpaksiyon ve Taşma Tipi Fekal İnkontinans (Enkoprezis)",
        "disposition": "Yeşil Alandan Oral PEG Disimpaksiyon, İdame Laksatif ve Davranışsal Tuvalet Eğitimi ile Taburculuk",
        "case_pearl": "Çamaşır kirletmesi olan çocukta 'ishal' yakınması sıklıkla rektumdaki sert kitlenin etrafından sızan sıvı dışkıdır. Fonksiyonel kabızlıkta tanı Roma IV kriterleri ve muayeneye dayanır; alarm bulgusu yoksa rutin batın grafisi ve kan tetkiki gerekmez. ESPGHAN/NASPGHAN'a göre ilk seçenek oral PEG ile disimpaksiyon (1-1.5 g/kg/gün, 3-6 gün), ardından en az 2 ay idame (0.4-0.8 g/kg/gün) ve davranışsal tuvalet eğitimidir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Çamaşır kirletmesi, seyrek sert dışkılama ve tutma davranışı tarif edilen bu çocukta muayenede neyi mutlaka değerlendirmelisiniz?",
                "options": [
                    {
                        "text": "Karın ağrısı ve iştahsızlık nedeniyle sağ alt kadran hassasiyeti, rebound ve psoas bulgularını değerlendirip cerrahi konsültasyon gerekliliğine karar vermek",
                        "is_correct": False,
                        "scenario_update": "Sağ alt kadran hassasiyeti ve peritoneal bulgu saptanmadı. Sol alt kadrandaki kitle ve perianal bulgular bu odakla değerlendirilmedi.",
                        "teaching_point": "Bir aylık seyrek-sert dışkılama ve tutma davranışında öncelik peritonit aramak değil, dışkı kitlesi ve organik neden alarm bulgularını değerlendirmektir."
                    },
                    {
                        "text": "Davranışsal bir sorun olduğunu düşünüp çocuğun tuvalet alışkanlıklarını ve okul stresini sorgulamak, fizik muayene sonrasında çocuk psikiyatrisine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Psikiyatri randevusu 3 ay sonraya verildi; bu sürede çamaşır kirletmesi ve karın ağrısı arttı.",
                        "teaching_point": "Tutma davranışı ve sosyal sorunlar sonuçtur; altta yatan dışkı birikimi tedavi edilmeden psikososyal destek tek başına yetersiz kalır."
                    },
                    {
                        "text": "Karın palpasyonunda kitle aramak, lumbosakral bölgeyi ve alt ekstremite nörolojik muayenesini değerlendirmek, perianal inspeksiyon ve gerekirse rektal muayene yapmak",
                        "is_correct": True,
                        "explanation": "Kabızlıkta abdominal fekal kitle, perianal fissür ve sfinkter değerlendirmesi tanıyı destekler. Lumbosakral gamze, kıl yumağı, alt ekstremite refleks ve kuvvet kaybı spinal disrafizm gibi organik nedenler için alarm bulgularıdır.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 94/dk, SS 20/dk, TA 96/60 mmHg. Sol alt kadrandan göbek altına uzanan, sert, hareketli, ağrısız kitle palpe edildi. Lumbosakral bölge doğal, gamze veya kıl yumağı yok. Alt ekstremite refleks ve kas gücü normal. Perianal bölgede dışkı bulaşı ve saat 6 hizasında küçük fissür; anal açıklıkta sert dışkı görülüyor."
                    },
                    {
                        "text": "Dışkı sızıntısını ishal kabul edip hidrasyon bulgularını, perianal cildi ve karın muayenesini değerlendirmek, dışkı mikroskopisi için örnek istemek",
                        "is_correct": False,
                        "scenario_update": "Hidrasyon normal bulundu. Dışkı mikroskopisinde parazit görülmedi; şikayetin nedeni hakkında yol gösterici bilgi elde edilmedi.",
                        "teaching_point": "Sert ve seyrek dışkılama ile birlikte olan çamaşır kirletmesinde sızıntının kaynağı rektumdaki dışkı kitlesi olabilir; bu ayrım muayeneyle yapılır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Alarm bulgusu olmayan, abdominal kitle ve anal fissür saptanan bu çocukta tetkik yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Organik nedenleri dışlamak için tam kan sayımı, tiroid fonksiyon testleri, kalsiyum, çölyak serolojisi ve kurşun düzeyi istemek",
                        "is_correct": False,
                        "scenario_update": "Tüm sonuçlar normal geldi; çocuk 4 tüp kan için iki kez venöz girişime maruz kaldı ve aile tedaviyi sonuçlar gelene kadar erteledi.",
                        "teaching_point": "Büyüme gelişmesi normal ve alarm bulgusu olmayan çocukta rutin laboratuvar taraması gerekmez; tedavi gecikmemelidir."
                    },
                    {
                        "text": "Ek tetkik yapmadan klinik tanıyla tedaviye başlamak; büyüme, nörolojik muayene ve mekonyum öyküsü normal olduğundan organik neden aramamak",
                        "is_correct": True,
                        "explanation": "Roma IV kriterlerini karşılayan ve alarm bulgusu olmayan çocukta tanı kliniktir. Normal büyüme, ilk gün mekonyum çıkışı ve normal nörolojik muayene organik nedenleri büyük ölçüde dışlar; tetkikler yönetimi değiştirmez.",
                        "new_finding": "Laboratuvar veya görüntüleme istenmedi. Aileye şikayetlerin kaynağı muayene bulguları üzerinden görsel bir çizimle anlatıldı; sızıntının ishal olmadığı açıklandı."
                    },
                    {
                        "text": "Mekonyum öyküsü normal olsa da hastalığı dışlamak için baryumlu kolon grafisi ve rektal emme biyopsisi planlamak üzere gastroenterolojiye yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Kontrast grafide rektumda dilatasyon ve dışkı görüldü, geçiş zonu yoktu. Biyopsi randevusu beklenirken tedavi başlanmadı.",
                        "teaching_point": "İlk 48 saatte mekonyum çıkışı, geç başlangıç ve tutma davranışı organik aganglionozis olasılığını düşürür; invaziv tetkik alarm bulgusuna göre planlanır."
                    },
                    {
                        "text": "Kitlenin niteliğini ve kolondaki dışkı yükünü belgelemek amacıyla ayakta direkt batın grafisi çekip tedavi planını grafi bulgusuna göre yapmak",
                        "is_correct": False,
                        "scenario_update": "Grafide kolonda yoğun dışkı görüldü; muayenede zaten belirlenen bulguyu doğruladı ve yönetimi değiştirmedi, çocuk radyasyona maruz kaldı.",
                        "teaching_point": "ESPGHAN/NASPGHAN rutin batın grafisini önermez; rektal muayene yapılamayan veya öykü güvenilmeyen seçilmiş olgularda düşünülebilir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Tutma davranışı, haftada bir sert dışkılama, abdominal fekal kitle ve çamaşır kirletmesi olan bu çocuktaki tanı nedir?",
                "options": [
                    {
                        "text": "Fonksiyonel kabızlık, fekal impaksiyon ve taşma inkontinansı",
                        "is_correct": True,
                        "explanation": "Tutma davranışı, seyrek iri sert dışkı, palpabl fekal kitle ve sıvı dışkı sızıntısı Roma IV fonksiyonel kabızlık ve impaksiyona bağlı taşma inkontinansını gösterir.",
                        "new_finding": "Tanı: Fonksiyonel Kabızlık, Fekal İmpaksiyon ve Retentif Fekal İnkontinans (Enkoprezis)."
                    },
                    {
                        "text": "Hirschsprung hastalığı",
                        "is_correct": False,
                        "scenario_update": "İlk gün mekonyum çıkışı, geç başlangıç ve rektumda dışkı bulunması bu tanıyla uyumlu değildir.",
                        "teaching_point": "Aganglionoziste rektum genellikle boştur ve şikayetler yenidoğan döneminde başlar; çamaşır kirletmesi nadirdir."
                    },
                    {
                        "text": "Akut infeksiyöz ishal",
                        "is_correct": False,
                        "scenario_update": "Bir aylık seyir, sert seyrek dışkılama ve ateş yokluğu enfeksiyöz ishalle açıklanamaz.",
                        "teaching_point": "Çamaşırdaki sıvı dışkı, sert kitle etrafından sızan taşma ishali olabilir."
                    },
                    {
                        "text": "Hipotiroidiye bağlı kabızlık",
                        "is_correct": False,
                        "scenario_update": "Büyüme hızı normal, yorgunluk, soğuk intoleransı veya kuru cilt gibi bulgular yok.",
                        "teaching_point": "Endokrin nedenler büyüme geriliği ve sistemik bulgularla birlikte düşünülür."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu 18 kg'lık çocukta ilk tedavi planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Acilde iki gün üst üste fosfatlı rektal lavman uygulayıp dışkı boşaldıktan sonra lif ağırlıklı diyet ve bol sıvı önererek ilaçsız izlemek",
                        "is_correct": False,
                        "scenario_update": "Lavman sonrası çocuk tuvaletten korkmaya başladı; idame tedavi verilmediği için 3 hafta içinde impaksiyon tekrarladı.",
                        "teaching_point": "Oral PEG disimpaksiyonda lavman kadar etkilidir ve daha az travmatiktir; idame laksatif verilmeden yalnız diyetle nüks kaçınılmazdır."
                    },
                    {
                        "text": "Uyarıcı laksatif olarak her gece oral senna başlamak, yanına simetikon eklemek ve sızıntı için çocuğa gece bezi kullandırmak",
                        "is_correct": False,
                        "scenario_update": "Senna ile karın krampları arttı; çocuk ağrılı dışkılamadan daha çok korkarak tutma davranışını sürdürdü.",
                        "teaching_point": "Uyarıcı laksatifler ilk basamak değildir; ozmotik laksatif ve davranışsal tedavi temel yaklaşımdır."
                    },
                    {
                        "text": "Günlük oral laktüloz 1 mL/kg ile başlamak, dışkı yumuşadığında bir hafta içinde kesmek ve tuvalet eğitimini kreşe bırakmak",
                        "is_correct": False,
                        "scenario_update": "Mevcut impaksiyon çözülmeden başlanan düşük doz laktüloz şişkinlik ve sızıntıyı artırdı; erken kesilince şikayetler tekrarladı.",
                        "teaching_point": "Önce impaksiyon temizlenmeli, ardından idame tedavi en az 2 ay ve düzenli dışkılama sağlandıktan sonra kademeli azaltılmalıdır."
                    },
                    {
                        "text": "Oral PEG ile 1-1.5 g/kg/gün dozda 3-6 gün disimpaksiyon, ardından en az iki ay idame dozu, yemek sonrası tuvalet oturuşu ve ödül çizelgesi",
                        "is_correct": True,
                        "explanation": "ESPGHAN/NASPGHAN önerisi oral PEG ile disimpaksiyon, ardından 0.4-0.8 g/kg/gün idame ve en az 2 ay sürdürülen davranışsal tedavidir. Fissür için oturma banyosu ve bariyer krem eklenir.",
                        "new_finding": "PEG 3350 ile 3 gün disimpaksiyon yapıldı, karındaki kitle kayboldu. İdame doza geçildi; 2 hafta sonraki kontrolde günlük yumuşak dışkılama başladı, çamaşır kirletmesi durdu."
                    }
                ]
            }
        ]
    },
    {
        "id": "G44",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "6 Haftalık",
        "gender": "Kız",
        "complaint": "Üç haftadır her akşam saatlerce süren, susturulamayan ağlama nöbetleri",
        "history": "Ailesi anlatıyor: 'Üç haftadır her akşam saat 18:00 civarında başlıyor. Yüzü kızarıyor, bacaklarını karnına çekiyor, ellerini yumruk yapıp 3-4 saat çığlık atarak ağlıyor. Gaz çıkarınca biraz rahatlıyor gibi, sonra yine başlıyor. Gün içinde neşeli, emmesi iyi. Ateşi veya kusması olmadı. Bu akşam her zamankinden farklı olarak kucakta da hiç susmadı, bu yüzden geldik. Biz uykusuzluktan tükendik.' Term doğum, sadece anne sütü alıyor.",
        "final_diagnosis": "İnfantil Kolik (Roma IV Kriterleri)",
        "disposition": "Yeşil Alandan Aileye Güvence, Yatıştırma Teknikleri ve Ebeveyn Tükenmişliği Danışmanlığı ile Taburculuk",
        "case_pearl": "Beş aydan küçük, sağlıklı büyüyen bebekte açıklanamayan uzun ağlama nöbetleri infantil koliği düşündürür; ancak tanı tam soyarak yapılan muayeneyle organik nedenler (saç turnikesi, korneal abrazyon, fıtık, otitis, fraktür, idrar yolu enfeksiyonu) dışlandıktan sonra konur. Simetikon, antispazmodikler ve asit baskılayıcılar etkisizdir. Ebeveyn tükenmişliği sorgulanmalı ve sarsılmış bebek sendromu açısından önleyici danışmanlık verilmelidir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Akşamları uzun süre ağlayan, bu akşam kucakta da susmayan 6 haftalık bu bebekte muayenede öncelikli yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Ağlama sırasında bacakları karnına çekmesini karın kaynaklı kabul edip batın palpasyonu ve oskültasyonu yaparak gaz giderici damla vermek",
                        "is_correct": False,
                        "scenario_update": "Batın muayenesi normal bulundu. Simetikon sonrası ağlama değişmedi; diğer sistemler muayene edilmeden bebek gözleme alındı.",
                        "teaching_point": "Bacakları karna çekme spesifik değildir; gaz giderici damlaların etkinliği gösterilmemiştir ve kapsamlı muayenenin yerine geçemez."
                    },
                    {
                        "text": "Bebeği tamamen soyarak el-ayak parmaklarında saç turnikesi, korneada çizik, kasık fıtığı, kulak zarları ve uzun kemiklerde hassasiyet dahil baştan ayağa muayene etmek",
                        "is_correct": True,
                        "explanation": "Susturulamayan ağlama ile başvuran süt çocuğunda organik nedenler sistematik ve tam soyulmuş muayeneyle aranmalıdır. Saç turnikesi, korneal abrazyon, inkarsere fıtık ve istismara bağlı fraktürler yalnızca bu şekilde fark edilir.",
                        "new_finding": "Vital Bulgular: Ateş 36.9°C, KTA 138/dk, SS 36/dk, SpO2 %99. Tartı 4.9 kg (doğum 3.4 kg; günlük ortalama 35 g artış). Saç turnikesi yok. Flöresein ile kornealar temiz. Kulak zarları doğal. Kasık kanallarında fıtık yok, dış genitalya doğal. Fontanel düz, tonus normal. Kemiklerde hassasiyet ve ciltte morluk yok. Muayene sırasında bebek emzik ile sakinleşti."
                    },
                    {
                        "text": "Susmayan ağlama nedeniyle muayeneden önce idrar sondası ile tam idrar tetkiki ve kültür almak, sonra bebeği giyinik halde muayene etmek",
                        "is_correct": False,
                        "scenario_update": "İdrar tetkiki normal geldi. Giyinik muayenede sistemik bir sorun bulunmadı ancak ayak parmakları ve kornealar değerlendirilmedi.",
                        "teaching_point": "Ateşsiz ve iyi görünen bebekte ilk adım tam soyulmuş fizik muayenedir; tetkikler muayene bulgularına göre seçilir."
                    },
                    {
                        "text": "Ailenin tükenmişliğini fark edip önce onlarla görüşmek, bebeğin vitallerini ve tartısını alarak muayeneyi bebek sakinleştikten sonraki bir zamana bırakmak",
                        "is_correct": False,
                        "scenario_update": "Bebek bir saat sonra uyudu ve muayene yüzeysel yapıldı; aile bebeğin neden ağladığına dair bir açıklama almadan bekledi.",
                        "teaching_point": "Ebeveyn desteği önemlidir ancak organik nedenleri dışlayan tam muayene geciktirilmemelidir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Muayenesi tamamen normal olan, iyi kilo alan ve emzikle sakinleşen bu bebekte tetkik yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Tetkik istemeden aileyle ağlama günlüğünü gözden geçirmek, bebeğin acilde bir beslenmesini ve sakinleşmesini gözlemleyip kırmızı bayrakları sorgulamak",
                        "is_correct": True,
                        "explanation": "Normal muayene, iyi kilo alımı ve tipik ağlama paterni olan bebekte laboratuvar tetkiki tanıya katkı sağlamaz. Beslenme gözlemi ve kırmızı bayrak sorgusu (kusma, ateş, letarji, kilo kaybı) yeterlidir.",
                        "new_finding": "Bebek acilde etkin emdi, kusmadı, gaz çıkardıktan sonra uyudu. Ağlama günlüğünde günde ortalama 3.5 saat, haftada 6 gün, akşam saatlerinde yoğunlaşan nöbetler kaydedildi. Ateş, kusma veya dışkıda kan yok."
                    },
                    {
                        "text": "Reflüye bağlı ağrıyı dışlamak için batın ultrasonografisi ve özofagus pH monitorizasyonu planlamak üzere bebeği gastroenteroloji polikliniğine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografi normal bulundu; pH monitorizasyonu için randevu 2 ay sonraya verildi ve aile kaygıyla beklemeye başladı.",
                        "teaching_point": "Kusma, beslenme reddi veya kilo kaybı olmayan ağlayan bebekte reflü araştırması önerilmez; ağlama tek başına reflü göstergesi değildir."
                    },
                    {
                        "text": "Süt alerjisini dışlamak için kan eozinofil sayısı ve inek sütü spesifik IgE düzeyi istemek, sonuç gelene kadar annenin süt tüketimini kesmek",
                        "is_correct": False,
                        "scenario_update": "Spesifik IgE negatif geldi. Bu sürede anneye gereksiz diyet kısıtlaması uygulandı ve emzirme motivasyonu azaldı.",
                        "teaching_point": "Kanlı dışkı, egzama veya kusma gibi destekleyici bulgu yoksa alerji testleri önerilmez; diyet kısıtlaması rutin değildir."
                    },
                    {
                        "text": "Uzun ağlama nöbetleri nedeniyle olası nöbet aktivitesini değerlendirmek için kan şekeri, elektrolitler ve elektroensefalografi planlamak",
                        "is_correct": False,
                        "scenario_update": "Kan şekeri ve elektrolitler normal geldi; EEG randevusu verildi ve aile bebekte nörolojik bir hastalık olduğu endişesine kapıldı.",
                        "teaching_point": "Nöbet düşündüren stereotipik hareket, göz deviasyonu veya bilinç değişikliği yoksa nörolojik tetkik gerekmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Sağlıklı büyüyen, muayenesi normal 6 haftalık bebekte haftada 6 gün, günde 3 saati aşan akşam ağlama nöbetlerinin en olası nedeni nedir?",
                "options": [
                    {
                        "text": "İnek sütü proteini alerjisi",
                        "is_correct": False,
                        "scenario_update": "Kanlı-mukuslu dışkı, egzama, kusma veya kilo alımında duraklama yok.",
                        "teaching_point": "İzole ağlama, alerji tanısı için yeterli değildir."
                    },
                    {
                        "text": "İnfantil diskezi",
                        "is_correct": False,
                        "scenario_update": "Diskezide ağlama ve ıkınma yumuşak dışkılama öncesinde kısa sürelidir; akşam saatlerinde uzun nöbetler beklenmez.",
                        "teaching_point": "Diskezi dışkılama ile zamansal ilişkili ve dakikalarla sınırlı bir tablodur."
                    },
                    {
                        "text": "İnfantil kolik",
                        "is_correct": True,
                        "explanation": "Beş aydan küçük, sağlıklı büyüyen bebekte belirgin bir neden olmadan tekrarlayan, uzun süreli, yatıştırılması güç ağlama nöbetleri ve normal muayene Roma IV infantil kolik tanısını karşılar.",
                        "new_finding": "Tanı: İnfantil Kolik (Roma IV kriterleri, organik nedenler dışlandı)."
                    },
                    {
                        "text": "Gastroözofageal reflü hastalığı",
                        "is_correct": False,
                        "scenario_update": "Kusma, beslenme reddi, kilo kaybı veya ark yapma yok; ağlama beslenmeyle ilişkili değil.",
                        "teaching_point": "Reflü hastalığı tanısı için kusmaya eşlik eden komplikasyon bulguları gerekir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu bebeğin ailesine yönelik en uygun taburculuk planı hangisidir?",
                "options": [
                    {
                        "text": "Ağlama nöbetlerinde kullanılmak üzere simetikon damla ve rezene çayı önermek, anneye süt ve kafein kısıtlaması yaparak taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "İki hafta sonra ağlama süresinde değişiklik olmadı; annenin kısıtlı diyeti nedeniyle süt miktarı azaldı.",
                        "teaching_point": "Simetikonun etkinliği gösterilmemiştir, bitki çayları süt çocuğunda önerilmez ve rutin anne diyeti kısıtlaması gereksizdir."
                    },
                    {
                        "text": "Ağrıyı azaltmak amacıyla anne sütünü kesip hidrolize formüle geçmek ve bir hafta sonra kontrolde formülün etkisini değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Formüle geçişle ağlama değişmedi; emzirme sonlandı ve anne bu karardan pişmanlık duydu.",
                        "teaching_point": "Alerji bulgusu olmayan bebekte anne sütünü kesmek önerilmez; hidrolize formül yalnızca seçilmiş olgularda düşünülür."
                    },
                    {
                        "text": "Tablonun selim olduğunu anlatıp yatıştırma tekniklerini göstermek, tükenince bebeği güvenle bırakıp ara vermeyi ve asla sarsmamayı öğretmek",
                        "is_correct": True,
                        "explanation": "Tedavinin temeli aileye güvence, kundaklama, beyaz gürültü, ritmik sallama gibi yatıştırma teknikleri ve ebeveyn tükenmişliğine yönelik danışmanlıktır. Sarsılmış bebek sendromunu önleyici eğitim ve sosyal destek planı mutlaka verilmelidir.",
                        "new_finding": "Ebeveynlere yatıştırma teknikleri uygulamalı gösterildi, dönüşümlü dinlenme planı yapıldı ve aile hekimine 1 hafta sonra kontrol yazıldı. Kontrolde ailenin baş etme becerisinin arttığı, ağlama süresinin azalmaya başladığı görüldü."
                    },
                    {
                        "text": "Ağlama nöbetlerinde kullanılmak üzere düşük doz oral antispazmodik damla başlamak ve bebeğin uykusunu düzenlemek için akşam emzirme aralığını uzatmak",
                        "is_correct": False,
                        "scenario_update": "Antispazmodik sonrası bebekte uyku hali ve beslenme isteksizliği gelişti; aile ilacı kendisi kesti.",
                        "teaching_point": "Antikolinerjik antispazmodikler 6 aydan küçük bebeklerde apne ve konvülziyon riski nedeniyle kontrendikedir."
                    }
                ]
            }
        ]
    },
    {
        "id": "G45",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "2 Aylık",
        "gender": "Erkek",
        "complaint": "Son birkaç gündür bezinde dışkıyla karışık ince kırmızı kan çizgileri ve mukus",
        "history": "Annesi anlatıyor: 'Sadece anne sütü alıyor. Son 4-5 gündür hardal sarısı dışkısının içinde ince iplik şeklinde kırmızı kan çizgileri ve sümük gibi mukus görüyorum. Ateşi, kusması veya karın şişliği yok. Emmesi iyi, keyfi yerinde, kilo alıyor.' Doğumda K vitamini yapılmış. Aile öyküsünde atopi var. Anne son zamanlarda günde 3-4 bardak süt içtiğini söylüyor.",
        "final_diagnosis": "Besin Proteini İlişkili Alerjik Proktokolit (İnek Sütü Proteini Kaynaklı)",
        "disposition": "Yeşil Alandan Emzirmeye Devam, Anne Diyetinden İnek Sütü Eliminasyonu ve Pediatri Kontrolü ile Taburculuk",
        "case_pearl": "Sağlıklı görünen, iyi kilo alan, yalnız anne sütü ile beslenen süt çocuğunda dışkıda kan çizgileri ve mukusun en sık nedeni anne diyetindeki inek sütü proteinine bağlı alerjik proktokolittir. Anal fissür, enfeksiyon ve cerrahi nedenler muayeneyle dışlanır; tanı kliniktir ve anne diyetinden 2-4 hafta süt eliminasyonu ile kanamanın kaybolmasıyla desteklenir. Emzirme kesilmez, anneye kalsiyum-D vitamini desteği verilir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Dışkısında kan çizgileri ve mukus görülen, genel durumu iyi 2 aylık bu bebekte muayenede neye odaklanmalısınız?",
                "options": [
                    {
                        "text": "Dışkıdaki kanın gerçekten kan olup olmadığını anlamak için bezi inceleyip muayeneyi büyüme eğrisi değerlendirmesi ve hızlı batın palpasyonuyla sınırlı tutmak",
                        "is_correct": False,
                        "scenario_update": "Bezde kan çizgileri doğrulandı ancak perianal bölge, cilt ve genel sistemik muayene yapılmadığı için kanamanın kaynağı değerlendirilmedi.",
                        "teaching_point": "Rektal kanamada perianal inspeksiyon ve tam sistemik muayene fissür, enfeksiyon ve kanama diyatezini ayırt etmek için zorunludur."
                    },
                    {
                        "text": "Karın muayenesini yapıp sağ üst kadranda kitle aramak ve bebeği kucakta sallayarak ağlama nöbeti olup olmadığını izlemek için bir saat gözleme almak",
                        "is_correct": False,
                        "scenario_update": "Kitle palpe edilmedi; bir saatlik gözlemde ağlama nöbeti olmadı. Cilt ve perianal muayene yapılmadığı için tablo netleşmedi.",
                        "teaching_point": "Kanlı dışkıda cerrahi neden aranmalıdır ancak bu bebekte kolik ağlama, kusma ve letarji yok; muayene sistemik olarak tamamlanmalıdır."
                    },
                    {
                        "text": "Kanamanın üst gastrointestinal kaynaklı olabileceğini düşünerek nazogastrik sonda takıp mide içeriğini aspire etmek, ardından batını muayene etmek",
                        "is_correct": False,
                        "scenario_update": "Nazogastrik aspiratta kan yoktu; bebek işlem sırasında öğürüp kustu ve aile ciddi biçimde endişelendi.",
                        "teaching_point": "Dışkıyla karışık taze kan çizgileri alt gastrointestinal kaynağı gösterir; stabil bebekte nazogastrik aspirasyon gereksizdir."
                    },
                    {
                        "text": "Vitalleri, büyüme eğrisini, ciltte peteşi ve egzamayı, batında distansiyon ve kitleyi değerlendirip perianal bölgede fissür ve perianal dermatit aramak",
                        "is_correct": True,
                        "explanation": "Kanlı dışkılı süt çocuğunda genel durum, büyüme, karın muayenesi (obstrüksiyon, invajinasyon), cilt (kanama diyatezi, atopik dermatit) ve perianal bölge (fissür) sistematik değerlendirilmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 128/dk, SS 30/dk, SpO2 %100. Tartı 5.4 kg (50. persentil, düzenli artış). Genel durumu çok iyi, güleryüzlü. Yanaklarda hafif kuru egzamatöz alanlar. Peteşi veya ekimoz yok. Karın yumuşak, distansiyon ve kitle yok. Perianal inspeksiyonda fissür veya hemoroid yok. Bezde mukuslu sarı dışkı içinde kılcal kan çizgileri."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Genel durumu çok iyi, büyümesi normal, fissürü olmayan ve yanaklarında hafif egzaması bulunan bu bebekte tetkik planınız nedir?",
                "options": [
                    {
                        "text": "Kolonda polip veya vasküler malformasyonu dışlamak için batın ultrasonografisi isteyip çocuk gastroenterolojisine kolonoskopi değerlendirmesi için yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografi normal geldi; kolonoskopi için anestezi gerektiği belirtilince aile çok endişelendi.",
                        "teaching_point": "İyi görünen süt çocuğunda hafif rektal kanama için endoskopi ilk basamak değildir; seçilmiş, eliminasyona yanıtsız olgularda düşünülür."
                    },
                    {
                        "text": "Ek tetkik istemeden klinik değerlendirmeyle yetinmek; yalnızca annenin diyet öyküsünü ayrıntılı almak ve kanamanın seyrini izlemeyi planlamak",
                        "is_correct": True,
                        "explanation": "İyi görünen, normal büyüyen, fissürü ve sistemik bulgusu olmayan bebekte tanı kliniktir. Hemogram, dışkı tetkikleri ve görüntüleme yönetimi değiştirmez; annenin diyet öyküsü tanıya en çok katkı sağlayan bilgidir.",
                        "new_finding": "Annenin son 3 haftadır kalsiyum alması için günde 3-4 bardak süt, yoğurt ve peynir tükettiği öğrenildi. Bebekte anemi bulgusu yok. Tetkik istenmedi."
                    },
                    {
                        "text": "Kanama nedeniyle tam kan sayımı, protrombin zamanı ve aPTT ile birlikte inek sütü spesifik IgE ve deri prick testini planlamak",
                        "is_correct": False,
                        "scenario_update": "Hemogram ve koagülasyon normal geldi. Spesifik IgE ve deri testi negatif bulundu; aile alerji olmadığı sonucuna vararak diyet önerisine uymadı.",
                        "teaching_point": "Bu tablo IgE aracılı değildir; spesifik IgE ve deri testleri negatiftir ve tanıyı dışlamaz, yanlış güvence verir."
                    },
                    {
                        "text": "Enfeksiyöz kolit olasılığını dışlamak için dışkı kültürü, parazit incelemesi ve Clostridioides toksin testi göndermek ve sonuca göre tedaviyi düzenlemek",
                        "is_correct": False,
                        "scenario_update": "Dışkı kültürü negatif geldi; toksin testi pozitif bulundu ve aile yanlışlıkla enfeksiyon olduğu düşüncesiyle kaygılandı.",
                        "teaching_point": "Bir yaş altı bebeklerde Clostridioides kolonizasyonu sıktır ve test sonucu yanıltıcıdır; ateşsiz, iyi görünen bebekte rutin dışkı tetkiki önerilmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Yalnız anne sütü alan, iyi büyüyen, mukuslu dışkıda kan çizgileri olan ve annesi bol süt ürünü tüketen bu bebekte en olası tanı nedir?",
                "options": [
                    {
                        "text": "İleokolik invajinasyon",
                        "is_correct": False,
                        "scenario_update": "Kolik ağlama nöbetleri, kusma, letarji veya palpabl kitle yok; bebek neşeli.",
                        "teaching_point": "Cerrahi nedenli kanamada genel durum bozulur ve obstrüksiyon bulguları eşlik eder."
                    },
                    {
                        "text": "Yenidoğanın hemorajik hastalığı",
                        "is_correct": False,
                        "scenario_update": "Doğumda K vitamini yapılmış, peteşi-ekimoz veya başka odaktan kanama yok.",
                        "teaching_point": "K vitamini eksikliği kanaması genellikle çoklu odaktan ve profilaksi almamış bebeklerde görülür."
                    },
                    {
                        "text": "İnek sütü proteini ilişkili alerjik proktokolit",
                        "is_correct": True,
                        "explanation": "Sağlıklı görünen, yalnız anne sütü alan süt çocuğunda mukuslu dışkıda kan çizgileri ve annenin süt ürünü tüketimi, anne sütüne geçen inek sütü proteinine bağlı alerjik proktokoliti düşündürür.",
                        "new_finding": "Tanı: Besin Proteini İlişkili Alerjik Proktokolit (İnek Sütü Proteini)."
                    },
                    {
                        "text": "Anal fissür",
                        "is_correct": False,
                        "scenario_update": "Perianal inspeksiyonda fissür saptanmadı; dışkı sert değil, mukuslu ve yumuşak.",
                        "teaching_point": "Fissür kanaması genellikle sert dışkı yüzeyinde ve ağrılı dışkılamayla birliktedir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu bebeğin tedavi ve izlem planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Emzirmeye devam, anne diyetinden tüm inek sütü ürünlerini 2-4 hafta çıkarmak, anneye kalsiyum-D vitamini desteği ve kanama seyri için kontrol planlamak",
                        "is_correct": True,
                        "explanation": "Annenin diyetinden süt proteini çıkarıldığında kanama çoğunlukla 72 saat-2 hafta içinde azalır. Emzirme sürdürülür, anneye günlük kalsiyum ve D vitamini desteği verilir. Tablo genellikle 1 yaşında tolerans gelişmesiyle düzelir; yeniden maruziyet testi pediatri kontrolünde planlanır.",
                        "new_finding": "Anneye süt içeren gizli ürünler listesi verildi, kalsiyum-D vitamini reçete edildi. İkinci haftadaki kontrolde bebeğin dışkısında kan görülmediği, kilo alımının sürdüğü belirlendi."
                    },
                    {
                        "text": "Emzirmeye devam etmek ancak annenin diyetinden süt, yumurta, buğday, soya, fındık ve balığı birlikte çıkarıp altı hafta sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Anne kısıtlı diyete uyum sağlayamadı ve kilo kaybetti; emzirmeyi bırakmayı düşünmeye başladı.",
                        "teaching_point": "Çoklu besin eliminasyonu ilk basamak değildir; çoğu olgu yalnız süt eliminasyonuna yanıt verir. Yanıt yoksa kademeli olarak soya veya yumurta değerlendirilir."
                    },
                    {
                        "text": "Anne sütünü kesip aminoasit bazlı formüle geçmek ve formül sonrası kanama düzeldiğinde altı ay boyunca aynı mamayla devam etmek",
                        "is_correct": False,
                        "scenario_update": "Emzirme sonlandırıldı; aile pahalı formülü temin etmekte zorlandı. Kanama bir haftada geriledi ancak anne sütünün yararları kaybedildi.",
                        "teaching_point": "Anne sütüyle beslenen bebekte ilk basamak emzirmeyi sürdürmek ve anne diyetinden süt eliminasyonu yapmaktır."
                    },
                    {
                        "text": "Diyette değişiklik yapmadan mukozal iyileşmeyi hızlandırmak için oral demir ve probiyotik başlamak, kanama sürerse bir ay sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Bir ay boyunca kanama devam etti; kontrolde hafif anemi gelişmeye başladığı görüldü.",
                        "teaching_point": "Alerjik proktokolitte nedensel tedavi alerjen eliminasyonudur; probiyotikler tek başına yeterli değildir."
                    }
                ]
            }
        ]
    }
]
