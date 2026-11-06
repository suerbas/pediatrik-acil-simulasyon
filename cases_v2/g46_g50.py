# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - G46-G50 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "G46",
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
        "id": "G47",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "7 Yaşında",
        "gender": "Erkek",
        "complaint": "Üst solunum yolu enfeksiyonundan bir hafta sonra başlayan sağ alt karın ağrısı ve hafif ateş",
        "history": "Ailesi anlatıyor: 'Bir hafta önce ateş, burun akıntısı ve boğaz ağrısı geçirdi, tam iyileşti derken iki gündür karnının sağ alt tarafı sızlıyor. Ateşi evde 37.6°C ölçüldü. Kusması veya ishali yok, iştahı biraz azaldı ama yemek yiyor. Zıplayınca sağ tarafında hafif batma oluyor, yürüyebiliyor.' Daha önce benzer şikayeti olmamış.",
        "final_diagnosis": "Akut Mezenterik Lenfadenit",
        "disposition": "Yeşil Alanda USG ile Cerrahi Nedenlerin Dışlanması, Semptomatik Tedavi ve 24 Saatlik Yeniden Değerlendirme Planıyla Taburculuk",
        "case_pearl": "Viral üst solunum yolu enfeksiyonu sonrası sağ alt kadran ağrısı ve hafif ateşle gelen çocukta mezenterik lenfadenit sık bir nedendir; ancak tanı apandisit dışlanmadan konmamalıdır. Normal kalibrede (<6 mm), komprese edilebilen apendiksin USG ile gösterilmesi ve kümelenmiş, kısa aksı 8 mm'yi aşan mezenterik lenf nodları tanıyı destekler. Tablo destek tedavisiyle düzelir; ağrı artarsa yeniden değerlendirme şarttır.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Yakın zamanda üst solunum yolu enfeksiyonu geçiren, sağ alt kadran ağrısı ve hafif ateşi olan bu çocukta ilk değerlendirmeniz nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Karın ağrısının kabızlığa bağlı olabileceğini düşünüp dışkılama alışkanlığını sorgulamak ve muayene öncesinde gliserinli rektal lavman uygulamak",
                        "is_correct": False,
                        "scenario_update": "Lavman sonrası çocuk az miktarda normal dışkı çıkardı; ağrısı değişmedi ve karın muayenesi gecikti.",
                        "teaching_point": "Ateşli sağ alt kadran ağrısında lavman öncesinde cerrahi patolojiler değerlendirilmelidir."
                    },
                    {
                        "text": "Ağrının zamanla yer değiştirip değiştirmediğini, kusma-iştah değişimini sorgulayıp sağ alt kadran hassasiyeti, defans, rebound, zıplama testi ve skrotal muayene yapmak",
                        "is_correct": True,
                        "explanation": "Sağ alt kadran ağrısında ağrının göçü, anoreksi ve kusma öyküsü ile peritoneal irritasyon bulguları ve zıplama testi cerrahi patolojiyi değerlendirmede temel bileşenlerdir. Erkek çocukta skrotal muayene atlanmamalıdır.",
                        "new_finding": "Vital Bulgular: Ateş 37.5°C, KTA 92/dk, SS 20/dk, SpO2 %99. Ağrı başından beri sağ alt kadranda, göç etmemiş. Kusma yok, iştah hafif azalmış. Orofarenks hafif hiperemik, servikal küçük lenf nodları. Sağ alt kadranda hafif-orta palpasyon hassasiyeti; istemsiz defans ve rebound yok. Tek ayak üzerinde zıplayabiliyor, hafif rahatsızlık tarif ediyor. Testisler doğal."
                    },
                    {
                        "text": "Ateş ve yakın zamandaki enfeksiyon öyküsü nedeniyle akciğer ve orofarenks muayenesini önceleyip karın muayenesini analjezik etkisi geçtikten sonra yapmak",
                        "is_correct": False,
                        "scenario_update": "Akciğer muayenesi normal bulundu. Karın muayenesi bir saat ertelendi ve ağrının karakteri hakkında bilgi alınmadan zaman kaybedildi.",
                        "teaching_point": "Sağ alt kadran ağrılı çocukta karın muayenesi önceliklidir; analjezi muayeneyi maskelemez ancak muayene ertelenmemelidir."
                    },
                    {
                        "text": "Sağ alt kadran ağrısıyla gelen her çocukta olduğu gibi oral alımı kesip intravenöz sıvı başlatmak ve muayeneden önce çocuk cerrahisini çağırmak",
                        "is_correct": False,
                        "scenario_update": "Cerrahi ekip muayeneden önce çağrıldı; peritoneal bulgu saptanmadı ve hasta ön değerlendirme yapılmadan acil konsülte edildiği için süreç uzadı.",
                        "teaching_point": "Konsültasyon kararı klinik değerlendirme ve risk sınıflamasına göre verilir; iyi görünen çocukta önce tam muayene yapılır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Stratejisi",
                "question": "Peritoneal bulgusu olmayan ancak sağ alt kadranda hassasiyeti süren bu çocukta tetkik yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Radyasyon riskine rağmen kesin sonuç almak amacıyla intravenöz kontrastlı batın bilgisayarlı tomografisi çekip cerrahiye konsülte etmek",
                        "is_correct": False,
                        "scenario_update": "Tomografide sağ alt kadranda birkaç lenf nodu görüldü; bulgu ultrasonla da gösterilebilecek düzeydeydi ve çocuk gereksiz radyasyona maruz kaldı.",
                        "teaching_point": "Çocukta sağ alt kadran ağrısında ilk görüntüleme ultrasonografidir; tomografi yalnızca USG tanısal olmadığında ve klinik şüphe sürdüğünde düşünülür."
                    },
                    {
                        "text": "Laboratuvar tetkiki olmadan yalnızca ayakta direkt batın grafisi çekip apendikolit veya gaz-sıvı seviyesi yoksa taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Grafide patolojik bulgu yoktu; ancak grafi apendiksi değerlendiremediği için tablo aydınlatılmadan taburculuk düşünüldü.",
                        "teaching_point": "Direkt grafi sağ alt kadran ağrısında düşük duyarlılığa sahiptir ve tek başına güvence vermez."
                    },
                    {
                        "text": "Ateşli karın ağrısında idrar yolu enfeksiyonunu dışlamak için yalnızca tam idrar tetkiki istemek ve normal gelirse antibiyotiksiz taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Tam idrar tetkiki normal geldi; sağ alt kadran hassasiyeti açıklanmadan çocuk taburcu edilecekti.",
                        "teaching_point": "İdrar tetkiki ayırıcı tanıda yararlıdır ancak lokalize sağ alt kadran hassasiyetinde görüntüleme ve laboratuvar değerlendirmesinin yerini tutmaz."
                    },
                    {
                        "text": "Tam kan sayımı, CRP ve batın ultrasonografisi istemek; ultrasonda apendiksin görüntülenmesini, çapını ve kompresibilitesini özellikle sorgulamak",
                        "is_correct": True,
                        "explanation": "Orta riskli sağ alt kadran ağrısında laboratuvar ve ultrasonografi birlikte risk sınıflamasını belirler. Normal kalibrede ve komprese edilebilen apendiksin gösterilmesi cerrahi patolojiyi büyük ölçüde dışlar.",
                        "new_finding": "Lökosit 8.400/mm³ (%55 nötrofil), CRP 8 mg/L. Batın USG: Apendiks 4.2 mm çapında, komprese edilebilir, periapendiküler yağlanma yok. Sağ alt kadran mezenter kökünde en büyüğü 11x6 mm, oval, ekojen hilusu korunmuş çok sayıda kümelenmiş lenf nodu. Serbest sıvı yok."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Viral enfeksiyon sonrası sağ alt kadran ağrısı, normal apendiks ve kümelenmiş büyük lenf nodları saptanan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Akut mezenterik lenfadenit",
                        "is_correct": True,
                        "explanation": "Üst solunum yolu enfeksiyonunu izleyen sağ alt kadran ağrısı, normal kalibrede komprese edilebilen apendiks ve kısa aksı 8 mm'yi aşan kümelenmiş mezenterik lenf nodları mezenterik lenfaditi destekler.",
                        "new_finding": "Tanı: Akut Mezenterik Lenfadenit (apendiks normal)."
                    },
                    {
                        "text": "Sağ üreter taşına bağlı kolik",
                        "is_correct": False,
                        "scenario_update": "Kolik tarzda ağrı, hematüri ve hidronefroz yok.",
                        "teaching_point": "Renal kolik ani başlangıçlı, dalgalı ağrı ve idrar bulgularıyla seyreder."
                    },
                    {
                        "text": "Meckel divertiküliti",
                        "is_correct": False,
                        "scenario_update": "Ultrasonda kör sonlanan inflame divertiküler yapı veya çevre yağlanması görülmedi.",
                        "teaching_point": "Meckel divertiküliti ultrasonda apendiksten ayrı inflame yapı olarak izlenir."
                    },
                    {
                        "text": "Erken evre akut apandisit",
                        "is_correct": False,
                        "scenario_update": "Apendiks 4.2 mm, komprese edilebilir ve çevresinde inflamasyon yok; laboratuvar normal.",
                        "teaching_point": "Normal apendiksin gösterilmesi apandisiti büyük ölçüde dışlar ancak şikayet ilerlerse yeniden değerlendirme gerekir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuğun tedavi ve izlem planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Cerrahi patolojiyi kesin olarak dışlamak için çocuğu oral alımı kapalı olarak 24 saat çocuk cerrahisi servisinde seri muayeneyle izlemek",
                        "is_correct": False,
                        "scenario_update": "Çocuk 24 saat aç izlendi; şikayetleri hızla gerileyen hastada gereksiz yatış oldu.",
                        "teaching_point": "Genel durumu iyi, ağrısı hafif ve USG'de apendiksi normal çocukta güvenilir bir aileyle ayaktan izlem uygundur."
                    },
                    {
                        "text": "Parasetamol ve hidrasyon önerip, ağrının artması, kusma, yürürken zorlanma veya ateş yükselmesinde dönmeyi anlatarak 24 saat içinde yeniden değerlendirme planlamak",
                        "is_correct": True,
                        "explanation": "Mezenterik lenfadenit kendini sınırlayan bir tablodur; destek tedavisi yeterlidir. Erken apandisitin USG'de gözden kaçabileceği unutulmamalı, net dönüş kriterleri ve 24 saatlik yeniden değerlendirme planlanmalıdır.",
                        "new_finding": "Çocuk parasetamol ile taburcu edildi. 24. saatteki kontrolde ağrısı azalmış, karın muayenesi rahattı; 72 saatte şikayetleri tamamen geçti."
                    },
                    {
                        "text": "Lenf nodlarının boyutu nedeniyle lenfoma olasılığını dışlamak için tam kan sayımı, LDH, ürik asit ve periferik yayma istemek ve onkolojiye yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Tetkikler normal geldi; aile onkoloji yönlendirmesi nedeniyle büyük kaygı yaşadı.",
                        "teaching_point": "Ekojen hilusu korunmuş, oval, kümelenmiş reaktif nodlar enfeksiyon sonrası beklenen bulgulardır; sistemik bulgu yoksa malignite araştırması gerekmez."
                    },
                    {
                        "text": "Bakteriyel süperenfeksiyon olasılığına karşı yedi gün oral amoksisilin-klavulanat başlamak ve ağrı için parasetamol önererek bir hafta sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Antibiyotikle çocukta ishal gelişti; ağrısı zaten 48 saatte geriliyordu.",
                        "teaching_point": "Viral kökenli mezenterik lenfaditte rutin antibiyotik gerekmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "G48",
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
        "id": "G49",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "3 Aylık",
        "gender": "Kız",
        "complaint": "Her beslenme sonrası ağzından kesilmiş süt çıkarması",
        "history": "Annesi anlatıyor: 'Emzirdikten hemen sonra veya gaz çıkarırken günde 5-6 kez ağzından süt ya da yoğurt gibi kesilmiş süt geliyor. Bunu yaparken ağlamıyor, gülümsüyor bile. Boğulur gibi olmuyor, morarmıyor. Kilo alıyor. Ama komşular mutlaka mide ilacı başlamamız gerektiğini söylüyor, bir arkadaşımın bebeğine de şurup verilmiş. Endişelendik.' Term doğum, sadece anne sütü alıyor.",
        "final_diagnosis": "Fizyolojik Gastroözofageal Reflü (Komplikasyonsuz)",
        "disposition": "Yeşil Alandan Aile Eğitimi, Asit Baskılayıcı İlaçtan Kaçınma ve Beslenme Önerileri ile Taburculuk",
        "case_pearl": "Süt çocuklarının yaklaşık yarısında görülen ağrısız, eforsuz, beslenme sonrası kusma; kilo alımı normal, beslenme reddi ve solunum komplikasyonu yoksa fizyolojiktir ve genellikle 12-14 ayda düzelir. Tanı kliniktir; tetkik ve asit baskılayıcı tedavi önerilmez (NASPGHAN/ESPGHAN 2018). Safralı veya fışkırır kusma, kilo kaybı, letarji, fontanel bombeliği, 6 aydan sonra başlangıç kırmızı bayraktır.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Beslenme sonrası sık süt çıkaran, keyfi yerinde 3 aylık bu bebekte değerlendirmenin odağı ne olmalıdır?",
                "options": [
                    {
                        "text": "Kusma sıklığı nedeniyle sağ üst kadranda zeytin benzeri kitle aramak için bebeği beslerken epigastriumu palpe edip acil batın ultrasonografisi planlamak",
                        "is_correct": False,
                        "scenario_update": "Kitle palpe edilmedi; ultrasonografi normal geldi. Kusmaların fışkırır olmadığı ve bebeğin kilo aldığı sorgulanmamıştı.",
                        "teaching_point": "Fışkırır kusma ve kilo alamama olmadan pilor görüntülemesi gerekmez; kusmanın niteliği öyküyle ayırt edilir."
                    },
                    {
                        "text": "Kusmalara bağlı aspirasyon riskini değerlendirmek için muayeneyle birlikte akciğer grafisi çekmek ve uyku sırasında apne monitörizasyonu önermek",
                        "is_correct": False,
                        "scenario_update": "Akciğer grafisi normal geldi; aile apne monitörü almak için kaygıyla arayışa girdi.",
                        "teaching_point": "Solunum belirtisi olmayan bebekte grafi ve monitörizasyon gereksizdir; endişeyi artırır."
                    },
                    {
                        "text": "Komşuların önerisini değerlendirip aileye güvence vermek amacıyla muayeneyi hızlıca yapıp yalnızca tartıya bakmak, kilo alımı iyiyse sonraki aşı kontrolüne yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Tartı normal bulundu ancak kırmızı bayraklar sistematik sorgulanmadığı için aile tam güvence alamadı ve ertesi gün başka merkeze başvurdu.",
                        "teaching_point": "Güvence ancak sistematik öykü ve muayeneyle verilebilir; kırmızı bayrakların yokluğu açıkça belgelenmelidir."
                    },
                    {
                        "text": "Kusmanın safralı veya fışkırır olup olmadığını, beslenme reddini ve solunum belirtilerini sorgulayıp büyüme eğrisi ve fontanel muayenesiyle kırmızı bayrakları aramak",
                        "is_correct": True,
                        "explanation": "Kusan süt çocuğunda ilk görev fizyolojik tabloyu organik nedenlerden ayırmaktır. Safralı veya fışkırır kusma, kilo kaybı, beslenme reddi, fontanel bombeliği ve letarji gibi kırmızı bayraklar yoksa tablo büyük olasılıkla fizyolojiktir.",
                        "new_finding": "Vital Bulgular: Ateş 36.7°C, KTA 122/dk, SS 28/dk, SpO2 %100. Tartı 6.0 kg (doğum 3.2 kg; günlük ortalama 31 g artış, 50. persentil). Muayene masasında gülümsüyor. Fontanel düz, tonus normal. Akciğer sesleri doğal. Karın yumuşak, epigastrik kitle yok. Kusmalar safrasız, fışkırır değil."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Kırmızı bayrağı olmayan, düzenli kilo alan bu bebekte tetkik yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Elektrolit kaybını değerlendirmek amacıyla venöz kan gazı ve serum klor düzeyine bakmak, normalse ilaç başlamadan taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Kan gazı ve elektrolitler normal geldi; bebek kan alımı sırasında uzun süre ağladı.",
                        "teaching_point": "Kilo alan, dehidratasyon bulgusu olmayan bebekte kan tetkiki gerekmez."
                    },
                    {
                        "text": "Tetkik istemeden aileye mekanizmayı anlatmak ve acilde bir beslenmeyi gözlemleyerek beslenme miktarını, sıklığını ve gaz çıkarma tekniğini değerlendirmek",
                        "is_correct": True,
                        "explanation": "Komplikasyonsuz tabloda tanı kliniktir. pH-impedans, endoskopi veya grafi önerilmez. Beslenme gözlemi aşırı besleme veya teknik sorunları ortaya koyabilir.",
                        "new_finding": "Gözlenen emzirmede bebek etkin emdi; ardından gaz çıkarırken az miktarda süt çıkardı, rahatsızlık göstermedi. Annenin bebeği beslenme hemen sonrasında yatırdığı öğrenildi."
                    },
                    {
                        "text": "Mide çıkış yolu ve anatomiyi değerlendirmek için baryumlu üst gastrointestinal pasaj grafisi istemek ve sonuca göre ilaç kararı vermek",
                        "is_correct": False,
                        "scenario_update": "Grafide işlem sırasında birkaç kez geri kaçış görüldü; bulgu yönetimi değiştirmedi ve bebek radyasyona maruz kaldı.",
                        "teaching_point": "Kontrastlı grafi geri kaçışı tanımlamak için uygun değildir; yalnızca anatomik anomali şüphesinde kullanılır."
                    },
                    {
                        "text": "Süt alerjisini dışlamak için kan eozinofil sayısı ve inek sütü spesifik IgE istemek, sonuç gelene dek annenin süt ürünlerini kesmesini önermek",
                        "is_correct": False,
                        "scenario_update": "Testler normal geldi; anne gereksiz diyet kısıtlaması nedeniyle yorgun düştü.",
                        "teaching_point": "Kanlı dışkı, egzama veya kilo alamama yoksa alerji testi önerilmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Ağrısız, eforsuz beslenme sonrası kusmaları olan, gülümseyen ve düzenli kilo alan 3 aylık bebekte tanı nedir?",
                "options": [
                    {
                        "text": "İnfantil hipertrofik pilor stenozu",
                        "is_correct": False,
                        "scenario_update": "Kusmalar fışkırır değil, bebek kilo alıyor ve epigastrik kitle yok.",
                        "teaching_point": "Pilor stenozu fışkırır kusma, açlık ve kilo kaybıyla seyreder."
                    },
                    {
                        "text": "Gastroözofageal reflü hastalığı",
                        "is_correct": False,
                        "scenario_update": "Beslenme reddi, kilo alamama, irritabilite veya solunum komplikasyonu yok.",
                        "teaching_point": "Hastalık tanımı ancak komplikasyon veya rahatsız edici semptomlar varsa kullanılır."
                    },
                    {
                        "text": "İnek sütü proteini alerjisi",
                        "is_correct": False,
                        "scenario_update": "Egzama, kanlı dışkı ve beslenme güçlüğü yok.",
                        "teaching_point": "Alerji tanısı için kusmaya eşlik eden ek bulgular aranmalıdır."
                    },
                    {
                        "text": "Fizyolojik gastroözofageal reflü",
                        "is_correct": True,
                        "explanation": "Kilo alımı normal, kırmızı bayrağı olmayan ve kusarken rahatsızlık göstermeyen süt çocuğunda geri kaçış fizyolojiktir ve kendiliğinden düzelir.",
                        "new_finding": "Tanı: Fizyolojik Gastroözofageal Reflü (komplikasyonsuz)."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu bebeğin ailesine yönelik en uygun plan hangisidir?",
                "options": [
                    {
                        "text": "Emzirmeyi bırakıp geri kaçışı azaltan özel koyulaştırılmış formüle geçmek ve formülün etkisini iki hafta sonra değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Formüle geçişle emzirme sona erdi; geri kaçış yalnızca hafifçe azaldı.",
                        "teaching_point": "Anne sütüyle beslenen bebekte fizyolojik geri kaçış emzirmeyi bırakmak için gerekçe değildir."
                    },
                    {
                        "text": "Tablonun normal olduğunu ve 1 yaş civarında geçeceğini anlatmak, aşırı beslemeden kaçınmayı ve beslenme sonrası dik tutmayı önermek, kırmızı bayrakları öğretmek",
                        "is_correct": True,
                        "explanation": "Fizyolojik geri kaçışta temel yaklaşım güvence ve beslenme önerileridir. Emzirme sürdürülür, ilaç verilmez. Safralı-fışkırır kusma, kilo kaybı veya beslenme reddinde dönüş anlatılır.",
                        "new_finding": "Aileye yazılı bilgi verildi. Bir ay sonraki kontrolde kusmalar azalmış, bebek düzenli kilo almaya devam ediyordu."
                    },
                    {
                        "text": "Mide asidini azaltmak için dört hafta oral omeprazol başlamak, beslenme sonrası dik tutmayı önermek ve ilaç bitiminde kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Kusma sıklığı değişmedi; bebek ikinci haftada akut gastroenterit ile başvurdu.",
                        "teaching_point": "Fizyolojik tabloda asit baskılayıcılar etkisizdir ve enfeksiyon riskini artırabilir."
                    },
                    {
                        "text": "Kusmayı azaltmak için sağılmış anne sütüne pirinç unu ekleyerek koyulaştırmayı ve bebeği gece yüzüstü yatırmayı önerip iki hafta sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Aile pirinç unuyla biberon kullanmaya başladı ve emzirme azaldı; yüzüstü yatış önerisi ani bebek ölümü riski taşıyordu.",
                        "teaching_point": "Yüzüstü yatırma ani bebek ölümü sendromu riski nedeniyle önerilmez; anne sütüyle beslenen bebekte kıvam artırıcı rutin değildir."
                    }
                ]
            }
        ]
    },
    {
        "id": "G50",
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
