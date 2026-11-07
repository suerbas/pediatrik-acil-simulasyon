# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - S26-S30 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "S26",
        "category": "👂 Kulak Ağrısı & KBB",
        "age": "11 Yaş",
        "gender": "Erkek",
        "complaint": "Tek taraflı şiddetli boğaz ağrısı, yutkunamama, çene açmada zorluk ve boğuk konuşma",
        "history": (
            "11 yaşındaki erkek çocuk (38 kg), dört gündür süren boğaz ağrısı ve ateşle getirildi. İki gün önce "
            "amoksisilin başlanmış ancak son yirmi dört saatte sol taraflı boğaz ve kulak ağrısı dramatik artmış. "
            "Hasta tükürüğünü yutamıyor, ağzını açarken şiddetli ağrı çekiyor ve sanki ağzında sıcak patates varmış "
            "gibi boğuk sesle güçlükle konuşuyor."
        ),
        "final_diagnosis": "Sol Peritonsiller Abse (Quinsy)",
        "disposition": "Acil KBB Konsültasyonu ile İğne Aspirasyonu / İnsizyon Drenajı + İntravenöz Ampisilin-Sulbaktam ve Yatış",
        "case_pearl": (
            "Peritonsiller abse (quinsy), adölesan ve büyük çocuklarda akut tonsillitin en sık derin boyun komplikasyonudur. "
            "En sık etkenler Streptococcus pyogenes ve anaerop mikroorganizmalardır (Fusobacterium necrophorum). "
            "Tek taraflı şiddetli boğaz ağrısı, odinofaji, kulağa yansıyan ağrı, trismus (internal pterigoid kas irritasyonuna bağlı) "
            "ve sıcak patates sesi tipiktir. Fizik muayenede etkilenen tarafta tonsil ön plikasında asimetrik şişlik ve uvulanın "
            "karşı tarafa deviasyonu görülür. Tanı genellikle kliniktir; şüpheli olgularda kontrastlı boyun BT yardımcıdır. "
            "Yönetimde acil KBB konsültasyonu ile iğne aspirasyonu veya insizyon-drenaj, intravenöz ampisilin-sulbaktam "
            "(veya klindamisin), hidrasyon, analjezi ve sistemik kortikosteroid uygulaması esastır."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Fizik Muayene",
                "question": "Tek taraflı şiddetli boğaz ağrısı, yutma güçlüğü ve çene kısıtlılığı olan hastada orofarenks değerlendirmesinde ilk yaklaşım nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Çene açıklığı kısıtlı olan hastanın dil kökünü metal basacakla kuvvetlice bastırarak orofarenks ve arka duvarını zorlayarak ayrıntılı şekilde incelemek",
                        "is_correct": False,
                        "scenario_update": "Zorlu dil basacağı uygulaması hastada şiddetli öğürme refleksini tetikledi ve geçici laringospazm ile oksijen satürasyonu %91 düzeyine düştü.",
                        "teaching_point": "Çene açması kısıtlı ve hava yolu daralmış çocuklarda orofarenks zorlanmamalıdır; agresif muayene laringospazm ve akut havayolu tıkanıklığına yol açabilir."
                    },
                    {
                        "text": "Hastayı zorlamadan ışık kaynağıyla ağız boşluğunu incelemek, tonsiller asimetriyi, uvula deviasyonunu ve havayolu açıklığını sakince değerlendirmek",
                        "is_correct": True,
                        "explanation": "Ağız açmada kısıtlılık ve havayolu darlığı kuşkusu olan hastalarda orofarenks nazikçe ve aydınlatılarak incelenmeli, gereksiz mekanik travmadan kaçınılmalıdır.",
                        "new_finding": "Vital Bulgular: Ateş 38.8°C, KTA 110/dk, SS 20/dk, SpO2 %98. Muayene: Sol tonsil ön plikası ileri derecede şiş ve eritemli, sol bademcik öne-orta hatta itilmiş, küçük dil belirgin şekilde sağa devie, çene açıklığı 1.5 cm."
                    },
                    {
                        "text": "Muayene yapmadan hastayı sakinleştirmek için hemen oral analjezik şurup içirmek ve sedyede tam supin pozisyonda yatırarak gözleme almak",
                        "is_correct": False,
                        "scenario_update": "Yutma güçlüğü belirgin olan hasta oral şurubu yutamayarak aspire etme tehlikesi yaşadı ve sırtüstü pozisyonda solunum eforu belirgin arttı.",
                        "teaching_point": "Ciddi odinofajisi ve salya akışı olan hastalara oral ilaç verilmemelidir; supin pozisyon farengeal havayolunu daraltarak solunum sıkıntısını artırır."
                    },
                    {
                        "text": "Fizik muayeneyi tamamen erteleyerek hastayı genel anestezi eşliğinde acil orotrakeal entübasyon yapmak amacıyla derhal ameliyathane koşullarına hızla nakletmek",
                        "is_correct": False,
                        "scenario_update": "Stabil solunumu olan hastada gereksiz genel anestezi ve entübasyon hazırlığı nedeniyle acil klinik değerlendirme ve tedavi süreci gecikti.",
                        "teaching_point": "Solunumu stabil olan, dinlenme halinde dispnesi bulunmayan hastalarda orotrakeal entübasyon endikasyonu yoktur; öncelik sakin ortamda klinik değerlendirmedir."
                    }
                ]
            },
            {
                "stage_title": "Acil Girişimsel ve Klinik İnceleme",
                "question": "Muayenesinde sol tonsil plikasında tek taraflı belirgin kabarıklık ve küçük dilde karşıya deviasyon saptanan hastada öncelikli yaklaşım nedir?",
                "options": [
                    {
                        "text": "Klinik bulgular tanıya yettiğinden radyolojik gecikme yaratmadan acil kulak burun boğaz konsültasyonuyla iğne aspirasyonu veya drenaj planlamak",
                        "is_correct": True,
                        "explanation": "Tipik klinik bulguları olan stabil kooperatif adölesanlarda görüntüleme şart değildir; KBB tarafından yapılan tanısal ve terapötik aspirasyon ilk seçenektir.",
                        "new_finding": "KBB hekimi tarafından sol tonsil üst kutbundan 18G iğne ile lokal anestezi altında yapılan aspirasyonda 4 mL pürülan sıvı boşaltıldı; hastanın ağrısı ve çene hareketleri belirgin rahatladı."
                    },
                    {
                        "text": "Herhangi bir cerrahi konsültasyon istemeden hastaya yalnızca oral tek doz sefaleksin reçete ederek ertesi gün kontrole gelmesini önermek",
                        "is_correct": False,
                        "scenario_update": "Lokalize pürülan sıvı drene edilmediği için enfeksiyon derin parafarengeal dokulara ilerledi, ateş 39.5°C oldu ve hastada dispne gelişti.",
                        "teaching_point": "Lokal pürülan sıvı birikimlerinde tek başına antibiyotik tedavisi yetersizdir; cerrahi drenaj yapılmadığında derin boyun enfeksiyonlarına ilerleme riski yüksektir."
                    },
                    {
                        "text": "Aspirasyon girişiminden önce mutlaka kontrastlı boyun manyetik rezonans görüntülemesi planlayıp hasta çekimden çıkana kadar hiçbir medikal tedavi başlamamak",
                        "is_correct": False,
                        "scenario_update": "MR randevusu ve çekimi için kaybedilen üç saatlik sürede hastanın ağrısı dayanılmaz hale geldi ve yutkunma güçlüğü daha da kötüleşti.",
                        "teaching_point": "Tipik klinik tablolarda manyetik rezonans görüntüleme gibi zaman alıcı tetkikler acil drenajı ve antibiyotik tedavisini gereksiz yere geciktirir."
                    },
                    {
                        "text": "Tanıyı doğrulamak amacıyla yalnızca boğaz kültürü ve rutin tam kan sayımı isteyerek sonuçlar çıkana kadar hastayı tedavisiz gözlemek",
                        "is_correct": False,
                        "scenario_update": "Laboratuvar sonuçlarının beklenmesi sırasında hastanın orofaringeal darlığı ilerledi ve hastada belirgin solunum güçlüğü belirtileri ortaya çıktı.",
                        "teaching_point": "Akut pürülan farengeal koleksiyonlarda tanı kliniktir; laboratuvar sonuçlarını beklemek hava yolu obstrüksiyonu riskini artırır ve tedaviyi geciktirir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Tek taraflı boğaz ağrısı, yutkunamama, sıcak patates sesi, çene kısıtlılığı, uvula deviasyonu ve pürülan aspirasyon ile kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Akut Eksüdatif Tonsillofarenjit",
                        "is_correct": False,
                        "scenario_update": "Tonsillofarenjitte uvula karşı tarafa itilmez, trismus ve asimetrik ön plika şişliği bulunmaz.",
                        "teaching_point": "Akut tonsillofarenjit simetrik tutulum yapar; tek taraflı şişlik, uvula deviasyonu ve trismus peritonsiller abseyi işaret eder."
                    },
                    {
                        "text": "Akut İnflamatuar Epiglottit",
                        "is_correct": False,
                        "scenario_update": "Epiglottitte tonsiller asimetri ve uvula deviasyonu olmaz; stridor, nefes darlığı ve oturur pozisyonda öne eğilme ön plandadır.",
                        "teaching_point": "Epiglottit supraglottik yapıların diffüz inflamasyonudur; tek taraflı tonsil flegmonu ve uvula itilmesi peritonsiller kompartman patolojisidir."
                    },
                    {
                        "text": "Sol Peritonsiller Abse",
                        "is_correct": True,
                        "explanation": "Tek taraflı tonsil plikası şişliği, uvulanın karşıya deviasyonu, trismus ve pürülan mayi aspirasyonu peritonsiller abse tanısını doğrular.",
                        "new_finding": "Kesin tanı: Sol Peritonsiller Abse (Quinsy). Cerrahi aspirasyon sonrası hava yolu açıklığı rahatladı."
                    },
                    {
                        "text": "Parafarengeal Boşluk Enfeksiyonu",
                        "is_correct": False,
                        "scenario_update": "Parafarengeal enfeksiyonlarda tonsil itilmesinden ziyade boyun lateralinde derin şişlik ve sistemik toksisite baskındır.",
                        "teaching_point": "Parafarengeal tutulumda karotis kılıfı komşuluğu ve boyun dış üçgeninde şişlik ön plandadır; intraoral asimetri peritonsiller alana işaret eder."
                    }
                ]
            },
            {
                "stage_title": "Acil Tedavi Yönetimi ve Konsültasyon",
                "question": "İğne aspirasyonu ile pürülan drenaj sağlanan 11 yaşındaki hastanın servis yatışında medikal tedavi ve takip planı nasıl düzenlenmelidir?",
                "options": [
                    {
                        "text": "Drenaj sonrasında şikayetleri gerilediği için hastaya antibiyotik vermeden yalnızca evde tuzlu su gargarası ve oral parasetamol önererek taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Parenteral antibakteriyel tedavi verilmeden gönderilen hastada yirmi dört saat sonra pürülan koleksiyon yeniden toplandı ve ateşle acile döndü.",
                        "teaching_point": "Drenaj sonrası rezidüel enfeksiyonu ve nüksü önlemek için geniş spektrumlu parenteral antibiyoterapi başlanması ve hastanın yatırılarak izlenmesi zorunludur."
                    },
                    {
                        "text": "Oral alımı hemen açarak hastayı yüksek doz oral siprofloksasin tedavisiyle evine göndermek ve üç gün sonra poliklinik kontrolüne çağırmak",
                        "is_correct": False,
                        "scenario_update": "Oral kinolon tedavisi adölesanlarda uygun birinci basamak tercih değildir ve hasta devam eden ağrı nedeniyle oral tableti içemedi.",
                        "teaching_point": "Çocuklarda derin enfeksiyonlarda florokinolonlar ilk seçenek değildir; erken dönemde oral uyumsuzluk riski nedeniyle intravenöz tedavi tercih edilir."
                    },
                    {
                        "text": "Hastaya parenteral kortikosteroid veya antibiyotik uygulamadan doğrudan acil genel anestezi altında elektif cerrahi tonsillektomi operasyonuna derhal almak",
                        "is_correct": False,
                        "scenario_update": "Akut aktif enfeksiyon ve inflamasyon zemininde yapılan acil tonsillektomi sırasında şiddetli orofaringeal kanama ve operasyon komplikasyonları gelişti.",
                        "teaching_point": "Akut enfeksiyon evresinde rutin tonsillektomi kanama riskini artırır; drenaj ve medikal tedaviye yanıt vermeyen seçilmiş olgularda düşünülür."
                    },
                    {
                        "text": "Hastaneye yatırılarak intravenöz ampisilin-sulbaktam, hidrasyon, analjezi, tek doz deksametazon ve hava yolu açısından yakın takip planlamak",
                        "is_correct": True,
                        "explanation": "En sık etken olan GAS ve oral anaeropları kapsayan ampisilin-sulbaktam, analjezi, ödemi azaltıcı steroid ve hospitalizasyon standart tedavidir.",
                        "new_finding": "Hasta servise yatırıldı; intravenöz ampisilin-sulbaktam (200 mg/kg/gün) ve tek doz deksametazon sonrası 24. saatte oral alımı açıldı, ateşi düştü."
                    }
                ]
            }
        ]
    },
    {
        "id": "S27",
        "category": "👂 Kulak Ağrısı & KBB",
        "age": "3 Yaş",
        "gender": "Kız",
        "complaint": "Kulak arkasında kızarıklık, şişlik, hassasiyet ve kulak kepçesinin öne doğru itilmesi",
        "history": (
            "3 yaşındaki kız çocuğu (14 kg), beş gün önce sol orta kulak iltihabı tanısıyla oral amoksisilin başlanmış "
            "bir hastadır. İlacını düzenli almasına karşın ateşi düşmemiş; son yirmi dört saatte sol kulak arkasında "
            "belirgin kızarıklık ve ağrılı şişlik gelişmiş, sol kulak kepçesi öne-aşağı doğru açılanmıştır."
        ),
        "final_diagnosis": "Sol Akut Koalesan Mastoidit",
        "disposition": "Acil KBB ve Pediatri Yatışı + İntravenöz Seftriakson ve Vankomisin Tedavisi + Terapötik Miringotomi / Tüp Uygulaması İçin Takip",
        "case_pearl": (
            "Akut koalesan mastoidit, akut otitis medianın en sık görülen intratemporal komplikasyonudur. "
            "Enfeksiyonun mastoid hava hücrelerine yayılması, pürülan eksüdanın basınç artışı yapması ve kemik trabeküllerin "
            "erimesi (osteit/koalesans) ile karakterizedir. Tipik fizik muayene bulguları kulak arkasında (retroauriküler) "
            "ödem, eritem, retroauriküler sulkusun silinmesi ve kulak kepçesinin öne-aşağı doğru itilmesidir (aurikular proptozis). "
            "Kemik destrüksiyonu, subperiosteal abse veya intrakraniyal yayılım şüphesinde kontrastlı temporal kemik BT çekilmelidir. "
            "Tedavide intravenöz geniş spektrumlu antibiyoterapi (seftriakson +/- vankomisin), orta kulak dekompresyonu için "
            "miringotomi ve medikal tedaviye yanıtsız olgularda kortikal mastoidektomi uygulanır."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Kulak Muayenesi",
                "question": "Kulak arkasında şişlik, kızarıklık ve kulak kepçesi öne itilmiş olan 3 yaşındaki çocukta ilk muayene yaklaşımı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Otoskopiyle timpanik membranı değerlendirmek, kulak arkasındaki kemik çıkıntıda ödem, eritem, hassasiyet ve sulkus silinmesini dikkatlice muayene etmek",
                        "is_correct": True,
                        "explanation": "Kulak arkası enfeksiyon bulguları ve kepçe protrüzyonu olan çocukta orta kulak zarı ve retroauriküler kemik çıkıntı eş zamanlı incelenmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 39.2°C, KTA 134/dk, SS 26/dk, SpO2 %98. Muayene: Sol kulak kepçesi öne-aşağı itilmiş, kulak arkasında eritemli ve aşırı hassas ödem mevcut, sulkus silinmiş; sol kulak zarı bombe ve hiperemik."
                    },
                    {
                        "text": "Kulak arkasındaki şişliği basit bir böcek ısırığı reaksiyonu olarak kabul edip topikal antihistaminik krem sürerek çocuğu evine göndermek",
                        "is_correct": False,
                        "scenario_update": "Topikal tedaviyle evine gönderilen hastada saatler içinde kulak arkasındaki eritem yayıldı, ateş 40°C oldu ve subperiosteal yayılım ilerledi.",
                        "teaching_point": "Kulak arkası kemik çıkıntıda kızarıklık, ödem ve aurikula protrüzyonu derin kemik enfeksiyonu işaretidir; basit cilt lezyonlarıyla karıştırılmamalıdır."
                    },
                    {
                        "text": "Kulak zarını görmeye çalışmadan önce dış kulak yoluna yüksek basınçlı çeşme suyu sıkarak kontrolsüz şekilde lavaj uygulamaya çalışmak",
                        "is_correct": False,
                        "scenario_update": "Akut enfekte ve gergin kulak zarına uygulanan basınçlı lavaj hastada şiddetli ağrı krizine ve kulak zarında perforasyona neden oldu.",
                        "teaching_point": "Akut süpüratif kulak enfeksiyonlarında basınçlı lavaj kontrendikedir; şiddetli ağrıya, timpanik membran rüptürüne ve enfeksiyonun yayılmasına yol açabilir."
                    },
                    {
                        "text": "Mevcut klinik tabloyu önemsemeyip hastanın oral amoksisilin tedavisini aynı dozda sürdürerek bir hafta sonra rutin poliklinik kontrolüne çağırmak",
                        "is_correct": False,
                        "scenario_update": "Oral amoksisiline yanıtsız devam eden enfeksiyon nedeniyle retroauriküler kemik korteksi erozyona uğradı ve çocuk toksik görünümle acile döndü.",
                        "teaching_point": "Oral antibiyotik altında ilerleyen kulak arkası kemik tutulumu acil hastane yatışı ve parenteral tedavi gerektiren ciddi bir komplikasyondur."
                    }
                ]
            },
            {
                "stage_title": "Acil Radyolojik ve Laboratuvar İncelemesi",
                "question": "Kulak arkasında ödem, kızarıklık, hassasiyet ve aurikula deviasyonu saptanan 3 yaşındaki çocukta en uygun ileri tetkik yaklaşımı nedir?",
                "options": [
                    {
                        "text": "Kafatasını değerlendirmek amacıyla yalnızca iki yönlü akciğer grafisi çekip herhangi bir kan tahlili veya ek inceleme istemeden beklemek",
                        "is_correct": False,
                        "scenario_update": "Akciğer grafisi normal geldi ancak kulak arkasındaki kemik erozyonu ve pürülan koleksiyon saptanamadığı için uygun tedavi planlanamadı.",
                        "teaching_point": "Akciğer grafisi temporal kemik patolojilerini göstermez; kemik destrüksiyonu ve intrakraniyal yayılım riskini değerlendirmek için hedefe yönelik inceleme gerekir."
                    },
                    {
                        "text": "Radyolojik inceleme yapmadan kulak arkasındaki gergin cilt alanına poliklinik şartlarında cerrahi bistüriyle körlemesine derin bir insizyon uygulamak",
                        "is_correct": False,
                        "scenario_update": "Anatomik planlar görüntülenmeden yapılan kör insizyon sırasında retroauriküler damar yaralanması ve kontrolsüz kanama meydana geldi.",
                        "teaching_point": "Görüntüleme ile kemik destrüksiyonu, vasküler yapılar ve sinüs ilişkisi ortaya konmadan kulak arkasına körlemesine cerrahi kesi yapılmamalıdır."
                    },
                    {
                        "text": "Hastadan yalnızca rutin tam idrar tetkiki ve gaita mikroskopisi isteyerek sonuçlar çıkana kadar hastayı tedavisiz acilde bekletmeye almak",
                        "is_correct": False,
                        "scenario_update": "İdrar ve gaita tetkikleri normal sonuçlandı; bu süreçte kaybedilen saatler nedeniyle retroauriküler subperiosteal sıvı birikimi belirginleşti.",
                        "teaching_point": "Kulak arkası komplikasyonlarında idrar veya gaita tahlilinin tanısal değeri yoktur; zaman kaybetmeden temporal kemik görüntülemesi yapılmalıdır."
                    },
                    {
                        "text": "Kemik trabekül yıkımını ve komplikasyonları belirlemek için kontrastlı temporal kemik tomografisi ve inflamasyon belirteçlerini istemek",
                        "is_correct": True,
                        "explanation": "Temporal kemik BT, kemik trabekül destrüksiyonunu, subperiosteal koleksiyonu ve intrakraniyal yayılımı net gösteren altın standart yöntemdir.",
                        "new_finding": "Temporal Kemik BT: Sol timpanik kavite ve hava hücrelerinde yaygın sıvı dansitesi, kemik septalarda destrüksiyon (koalesans) ve kortikal kemik erozyonu izlendi. Lökosit 19.500/mm³, CRP 105 mg/L."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Kulak enfeksiyonu zemininde retroauriküler eritem, sulkus silinmesi, aurikula protrüzyonu ve tomografide kemik koalesansı saptanan hastada kesin tanı nedir?",
                "options": [
                    {
                        "text": "Akut Süpüratif Otitis Eksterna",
                        "is_correct": False,
                        "scenario_update": "Dış kulak yolu enfeksiyonlarında tragus hassasiyeti belirgindir ancak temporal kemik tomografisinde trabeküler destrüksiyon görülmez.",
                        "teaching_point": "Otitis eksternada tragus basısıyla ağrı olur ve dış kulak yolu ödemlidir; retroauriküler kemik erozyonu ve sulkus silinmesi mastoid tutulumunu gösterir."
                    },
                    {
                        "text": "Sol Akut Koalesan Mastoidit",
                        "is_correct": True,
                        "explanation": "Tedaviye dirençli orta kulak enfeksiyonu, retroauriküler sulkus silinmesi, kepçe protrüzyonu ve BT'de kemik septa erimesi koalesan mastoidit tanısı koydurur.",
                        "new_finding": "Kesin tanı: Sol Akut Koalesan Mastoidit. Kemik trabekül destrüksiyonu ve subperiosteal yayılım doğrulandı."
                    },
                    {
                        "text": "Akut Bakteriyel Enfeksiyöz Parotit",
                        "is_correct": False,
                        "scenario_update": "Parotitte şişlik mandibula köşesi ve yanak önündedir; retroauriküler sulkusu silmez ve aurikulayı öne itmez.",
                        "teaching_point": "Parotit lezyonları kulağın ön ve alt kısımlarındadır; retroauriküler kemik hassasiyeti ve otoskopik orta kulak bulguları mastoiditi işaret eder."
                    },
                    {
                        "text": "Retroauriküler Enfekte Aterom Kisti",
                        "is_correct": False,
                        "scenario_update": "Aterom kisti cilt altı lokalize kistik lezyondur; orta kulak patolojisi ve temporal kemikte trabeküler destrüksiyon yapmaz.",
                        "teaching_point": "Enfekte sebase kistler yüzeyeldir; otoskopik orta kulak inflamasyonu ve BT'de kemik erozyonu bulunması sistemik mastoidit tablosunu doğrular."
                    }
                ]
            },
            {
                "stage_title": "Acil Tedavi Yönetimi ve Konsültasyon",
                "question": "Kemik trabekül yıkımı ve subperiosteal kortikal erozyon saptanan 3 yaşındaki bu hastanın acil medikal ve cerrahi yönetimi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Hastayı oral amoksisilin-klavulanat reçete ederek ayaktan takibe almak ve herhangi bir cerrahi branşa danışmadan beş gün sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Oral antibiyotik kemik yıkımı olan dokuda yeterli konsantrasyona ulaşamadı ve hastada subperiosteal pürülan koleksiyon ciltten fistülize oldu.",
                        "teaching_point": "Kemik erozyonu ve koalesans gelişen olgularda oral tedavi yetersizdir; acil hospitalizasyon, intravenöz tedavi ve cerrahi müdahale şarttır."
                    },
                    {
                        "text": "Sistemik hiçbir antibiyotik vermeden sadece dış kulak yoluna gentamisin damla damlatıp hastayı doğrudan evine göndererek yakın gözlem önermek",
                        "is_correct": False,
                        "scenario_update": "Topikal damlalar orta kulak arkasındaki kemik trabeküllere ulaşamaz; enfeksiyon hızla sigmoid sinüs trombozuna doğru ilerledi.",
                        "teaching_point": "Topikal kulak damlaları derin kemik tutulumunda tamamen etkisizdir; sistemik yayılımı ve intrakraniyal komplikasyonları önleyemez."
                    },
                    {
                        "text": "Hastaneye yatırarak intravenöz seftriakson ve vankomisin başlamak, kulak burun boğaz konsültasyonuyla miringotomi ve cerrahi drenaj planlamak",
                        "is_correct": True,
                        "explanation": "Streptococcus pneumoniae ve anaeropları kapsayan intravenöz geniş spektrumlu antibiyoterapi ve KBB tarafından orta kulak dekompresyonu/miringotomi esastır.",
                        "new_finding": "Hasta KBB servisine yatırıldı; intravenöz antibiyotikler başlandı ve genel anestezi altında sol miringotomi ile ventilasyon tüpü takılarak pürülan drenaj sağlandı."
                    },
                    {
                        "text": "Hastayı çocuk cerrahisi servisine devrederek genel anestezi altında tanısal acil laparotomi yapmak üzere ameliyathane hazırlığı derhal başlatmak",
                        "is_correct": False,
                        "scenario_update": "Kulak ve baş boyun patolojisinde ilgisiz şekilde batın cerrahisi hazırlığı yapılması hem zaman kaybına hem de malpraktis riskine yol açtı.",
                        "teaching_point": "Temporal kemik patolojileri KBB uzmanlık alanıdır; alakasız cerrahi konsültasyonlar ve girişimler hastanın yönetimini ciddi şekilde aksatır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S28",
        "category": "👂 Kulak Ağrısı & KBB",
        "age": "2.5 Yaş",
        "gender": "Erkek",
        "complaint": "Yüksek ateş, boynunu geriye atma, ağzını açamama, yutkunamama ve hırıltılı solunum",
        "history": (
            "2.5 yaşındaki erkek çocuk (13 kg), üç gündür süren yüksek ateş, huzursuzluk ve boynunu geriye doğru "
            "hiperekstansiyonda tutma yakınmasıyla getirildi. Ailesi çocuğun dünden beri ağzını hiç açmak istemediğini, "
            "salyasının aktığını, katı gıdayı tamamen reddettiğini ve nefes alırken kaba bir hırıltı çıkardığını ifade ediyor."
        ),
        "final_diagnosis": "Akut Retrofarengeal Abse",
        "disposition": "Acil KBB ve Pediatrik Yoğun Bakım Konsültasyonu + Havayolu Güvenliğinin Sağlanması + Cerrahi İnsizyon ve Drenaj + İntravenöz Antibiyotik İçin Yatış",
        "case_pearl": (
            "Retrofarengeal abse, genellikle beş yaşından küçük çocuklarda (özellikle 2-4 yaş) retrofarengeal lenf nodlarının "
            "(Rouvière nodları) süpürasyonu sonucu gelişir; bu nodlar yaşla birlikte atrofiye uğrar. Polimikrobiyaldir "
            "(A grubu streptokok, S. aureus, solunum yolu anaeropları). Belirtiler yüksek ateş, boyun hiperekstansiyonu "
            "(menenjizmi taklit eden rijidite), tortikolis, odinofaji, salya akması, kaba ses ve inspiratuar stridordur. "
            "Radyolojik olarak boyun ekstansiyonda ve inspiryumda çekilen lateral boyun grafisinde servikal omurga önü yumuşak "
            "doku kalınlaşması (C2 düzeyinde >7 mm veya vertebra korpus genişliğinden fazla, C6 düzeyinde >14 mm) karakteristiktir. "
            "Kontrastlı boyun BT altın standarttır. Acil hava yolu kontrolü, KBB tarafından cerrahi drenaj ve intravenöz "
            "ampisilin-sulbaktam (veya seftriakson + klindamisin/vankomisin) standart tedavidir."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Havayolu Muayenesi",
                "question": "Yüksek ateş, salya akması, boyun hiperekstansiyonu ve inspiratuar stridoru olan 2.5 yaşındaki çocukta ilk muayene yaklaşımı ne olmalıdır?",
                "options": [
                    {
                        "text": "Çocuğun boynunu kuvvetle öne bükmeye zorlayarak meningeal irritasyon bulgularını ortaya çıkarmak için tekrarlayan fleksiyon manevraları uygulamaya çalışmak",
                        "is_correct": False,
                        "scenario_update": "Boynun zorla fleksiyona getirilmesi faringeal kabarıklığı hava yoluna doğru itti ve çocukta ani akut respiratuar arrest gelişti.",
                        "teaching_point": "Derin boyun patolojisi olan çocukta boyun zorlanmamalıdır; fleksiyon manevraları laringeal basıyı artırarak ani havayolu kollapsına yol açabilir."
                    },
                    {
                        "text": "Solunum yolunu açmak için hastayı derhal supin yatırıp metal dil basacağı ile dil kökünü kuvvetlice bastırarak muayene etmek",
                        "is_correct": False,
                        "scenario_update": "Dil köküne uygulanan mekanik baskı spazm ve öğürmeyi tetikledi, kitle rüptürü riski ve ağır laringeal daralma oluştu.",
                        "teaching_point": "Hava yolu tehlikede olan çocukta zorlu orofarenks alet muayenesi kontrendikedir; refleks laringospazma veya kitle rüptürüne neden olabilir."
                    },
                    {
                        "text": "Çocuğu ajite etmeden, boynunu zorlamadan havayolu açıklığını, solunum eforunu ve vital parametrelerini sakin ortamda değerlendirmek",
                        "is_correct": True,
                        "explanation": "Üst hava yolu obstrüksiyonu riski taşıyan çocuklarda ajitasyon stridoru artırır; hasta en rahat ettiği pozisyonda, sakin ortamda değerlendirilmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 39.3°C, KTA 146/dk, SS 34/dk, SpO2 %94. Fizik Muayene: Baş hiperekstansiyonda, boyun fleksiyonu ağrılı, sürekli salya akıyor, orofarenks arka duvarında tek taraflı belirgin kabarıklık izleniyor."
                    },
                    {
                        "text": "Solunum sıkıntısını hiç önemsemeyip hastaya intramusküler tek doz kristalize penisilin enjekte ederek reçetesiz şekilde doğrudan evine göndermek",
                        "is_correct": False,
                        "scenario_update": "İntramusküler enjeksiyon sonrası eve gönderilen hastada iki saat içinde tam hava yolu tıkanması ve siyanoz gelişti.",
                        "teaching_point": "Stridor, salya akması ve boyun rijiditesi olan çocukta havayolu acildir; hastayı taburcu etmek ölümcül asfiksiye zemin hazırlar."
                    }
                ]
            },
            {
                "stage_title": "Acil Radyolojik Görüntüleme ve İnceleme",
                "question": "Hava yolunu tehdit eden derin servikal patoloji şüphesinde ilk basamakta istenmesi gereken hızlı radyolojik görüntüleme yöntemi nedir?",
                "options": [
                    {
                        "text": "Boyun ekstansiyonda ve inspiryumda lateral boyun grafisi çekerek servikal omurga önü yumuşak doku kalınlığını radyolojik incelemek",
                        "is_correct": True,
                        "image": "assets/images/neck_retropharyngeal.png",
                        "image_caption": "Lateral Boyun Grafisi: Prevertebral yumuşak doku gölgesinde ileri derecede kalınlaşma",
                        "explanation": "İnspiryumda ve boyun ekstansiyondayken çekilen lateral boyun grafisi servikal yumuşak doku genişlemesini hızlıca gösteren ilk tercihtir.",
                        "new_finding": "Lateral Boyun Grafisi: Servikal omurga önündeki yumuşak doku mesafesinde ileri derecede patolojik genişleme (C2-C4 seviyesinde komşu korpus kalınlığının iki katından fazla), farengeal hava sütununda öne doğru yer değiştirme izlendi."
                    },
                    {
                        "text": "Radyasyon riskinden kaçınmak amacıyla görüntüleme yapmayıp sadece tam idrar tahlili ve gaita mikroskopisi isteyerek hastayı izleme almak",
                        "is_correct": False,
                        "scenario_update": "Laboratuvar tetkikleri normal sonuçlandı ancak derin dokudaki bası ilerleyerek hastada belirgin hipoksi ve hava yolu stridoru derinleşti.",
                        "teaching_point": "Stridor ve boyun hiperekstansiyonu olan olgularda radyolojik görüntüleme esastır; idrar tahlili gibi ilgisiz tetkikler tanıyı tehlikeli şekilde geciktirir."
                    },
                    {
                        "text": "Birincil basamak tetkiki olarak derhal yüksek doz kontrastlı tüm vücut anjiyografisi çekerek olası vasküler malformasyonları taramaya çalışmak",
                        "is_correct": False,
                        "scenario_update": "Tüm vücut anjiyografisi hazırlığı ve kontrast uygulaması sırasında solunum sıkıntısı ağırlaştı ve kardiyopulmoner instabilite yaşandı.",
                        "teaching_point": "Tüm vücut anjiyografisi endike değildir; invazivdir, gereksiz yüksek radyasyon ve kontrast yükü taşır ve acil süreci aksatır."
                    },
                    {
                        "text": "Görüntüleme tetkiki istemeden hastayı sakinleştirmek için genel anestezi altında acil diagnostik bronkoskopi planlayarak ameliyathane koşullarına hızla nakletmek",
                        "is_correct": False,
                        "scenario_update": "Görüntüleme olmadan girilen bronkoskopi sırasında kitleye temas edilerek kanama ve pürülan içeriğin bronşlara aspirasyonu meydana geldi.",
                        "teaching_point": "Anatomik lokalizasyon radyolojik olarak belirlenmeden körlemesine bronkoskopi yapılması kitle rüptürüne ve trakeobronşiyal aspirasyona neden olabilir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Boyun hiperekstansiyonu, salya akması, stridor ve lateral grafide servikal omurga önü doku kalınlaşması saptanan hastada kesin tanı nedir?",
                "options": [
                    {
                        "text": "Akut Viral Krup Sendromu",
                        "is_correct": False,
                        "scenario_update": "Krup sendromunda havlayan öksürük ve subglottik daralma olur; salya akması, boyun hiperekstansiyonu ve servikal doku kalınlaşması görülmez.",
                        "teaching_point": "Krup subglottik trakeayı tutar; salya akışı, disfaji ve boyun rijiditesi derin servikal abse patolojilerini işaret eder."
                    },
                    {
                        "text": "Akut Bakteriyel Trakeit Tablosu",
                        "is_correct": False,
                        "scenario_update": "Bakteriyel trakeitte pürülan psödomembranlar trakea lümenini tıkar; lateral grafide farenks arkası yumuşak dokuda kalınlaşma izlenmez.",
                        "teaching_point": "Bakteriyel trakeit endotrakeal pürülan eksüda ile seyreder; lateral boyun grafisinde servikal yumuşak doku genişlemesi retrofarengeal tutulumu gösterir."
                    },
                    {
                        "text": "Akut İnflamatuar Epiglottit Enfeksiyonu",
                        "is_correct": False,
                        "scenario_update": "Epiglottitte lateral grafide belirgin başparmak belirtisi (ödemli epiglottis) görülür; farenks arkası doku mesafesi normal sınırlardadır.",
                        "teaching_point": "Epiglottit supraglottik laringeal yapıları tutar; retrofarengeal abse ise vertebra önü potansiyel boşlukta koleksiyonla karakterizedir."
                    },
                    {
                        "text": "Akut Servikal Retrofarengeal Abse",
                        "is_correct": True,
                        "explanation": "Küçük çocukta ateş, salya akması, boyun hiperekstansiyonu, stridor ve lateral grafide yumuşak doku kalınlaşması retrofarengeal abse için patognomoniktir.",
                        "new_finding": "Kesin tanı: Akut Servikal Retrofarengeal Abse. Hava yolu obstrüksiyonu riski nedeniyle acil cerrahi drenaj planlandı."
                    }
                ]
            },
            {
                "stage_title": "Acil Tedavi Yönetimi ve Konsültasyon",
                "question": "Lateral boyun grafisinde derin enfeksiyon odağı saptanan 2.5 yaşındaki bu hastanın kesin tedavi ve takip stratejisi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Hastaya oral sefuroksim reçete ederek ayaktan izlem planlamak ve genel durumu bozulursa iki gün sonra getirilmesini söylemek",
                        "is_correct": False,
                        "scenario_update": "Oral sefalosporin alan hastada gece saatlerinde kitle büyüyerek havayolunu tamamen kapattı ve arrest tablosuyla acile getirildi.",
                        "teaching_point": "Havayolunu tehdit eden derin boyun koleksiyonlarında ayaktan oral tedavi kesinlikle kabul edilemez; cerrahi drenaj ve hospitalizasyon şarttır."
                    },
                    {
                        "text": "Acil KBB konsültasyonuyla ameliyathanede cerrahi drenaj planlamak, hastanın havayolu güvenliğini sağlamak ve intravenöz ampisilin-sulbaktam başlamak",
                        "is_correct": True,
                        "explanation": "Havayolu emniyeti sağlandıktan sonra KBB tarafından cerrahi drenaj yapılması ve polimikrobiyal floraya yönelik ampisilin-sulbaktam verilmesi esastır.",
                        "new_finding": "Hasta ameliyathaneye alındı; KBB ekibi transoral insizyon ve drenajla 6 mL pürülan mayi boşalttı; çocuk yoğun bakımda İV antibiyoterapiyle izleme alındı."
                    },
                    {
                        "text": "Cerrahi yaklaşımı tamamen reddederek hastaya yalnızca soğuk buhar inhalasyonu ve nebulize budesonid vermek, acilde iki saat gözlemek",
                        "is_correct": False,
                        "scenario_update": "Nebulize tedaviler derin farengeal pürülan odağı etkilemedi ve solunum eforu dakikalar içinde daha da kötüleşti.",
                        "teaching_point": "Krup benzeri nebulize tedaviler retrofarengeal pürülan koleksiyonlarda etkisizdir; mekanik basıyı ortadan kaldıracak cerrahi drenaj gereklidir."
                    },
                    {
                        "text": "Boyun bölgesine lokal sıcak kompres uygulayıp hastayı çocuk enfeksiyon polikliniğine haftalık elektif poliklinik randevusu için sevk etmek",
                        "is_correct": False,
                        "scenario_update": "Sıcak uygulama ve gecikme nedeniyle lokal hiperemi arttı ve koleksiyon spontan rüptürle trakeobronşiyal ağaca boşalma tehlikesi oluşturdu.",
                        "teaching_point": "Derin boyun patolojilerinde sıcak kompres ve elektif poliklinik sevki kontrendikedir; acil cerrahi drenaj ve hava yolu emniyeti gerekir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S29",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "1.5 Yaş",
        "gender": "Kız",
        "complaint": "Aniden başlayan tükürüğünü yutamama, öğürme, retrosternal huzursuzluk ve besini reddetme",
        "history": (
            "1.5 yaşındaki kız çocuğu (11 kg), evde oyuncak uzaktan kumandasıyla oynadıktan hemen sonra aniden öğürmeye "
            "ve ağlamaya başlamış. Ailesi çocuğun dakikalar içinde tükürüğünü yutamaz hale geldiğini, sürekli salyasının "
            "aktığını, göğsünü göstererek kıvrandığını ve hiçbir şey içemediğini belirtiyor."
        ),
        "final_diagnosis": "Özofagus Üst Darlıkta Düğme Pil İmpaksiyonu",
        "disposition": "Acil Çocuk Cerrahisi / Pediatrik Gastroenteroloji Konsültasyonu + İlk 2 Saat İçinde Acil Rijit Endoskopik Çıkarma + Yoğun Bakım Takibi",
        "case_pearl": (
            "Özofagusta düğme pil (button battery) sıkışması, çocuk acil pratiğinde en kritik zamana duyarlı durumlardan biridir. "
            "Düğme piller elektrik akımı oluşturarak hidroksit iyonu üretir, alkali likefaksiyon nekrozu ve bası nekrozu ile "
            "2 saat kadar kısa sürede mukozal hasar ve özofagus perforasyonu yapabilir; trakeoözofageal veya aortoözofageal fistül "
            "gibi ölümcül komplikasyonlara yol açabilir. Ön-arka radyografide karakteristik çift halka (double ring / halo) "
            "belirtisi ve yan grafide basamak (step-off) belirtisi görülmesi madeni paralardan ayırt ettirir. Tanı anında oral stop "
            "yapılmalı ve genel anestezi altında ilk 2 saat içinde acil rijit endoskopiyle çıkarılmalıdır. Bir yaşından büyük "
            "çocuklarda endoskopiye kadar mukozal hasarı azaltmak için bal verilmesi önerilse de endoskopiyi asla geciktirmemelidir."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Triyaj",
                "question": "Ani başlayan yutma güçlüğü, tükürüğünü yutamama ve göğüs huzursuzluğu olan 1.5 yaşındaki bebekte ilk yaklaşım ne olmalıdır?",
                "options": [
                    {
                        "text": "Yutamadığı tükürüğü temizlemek için ağzına parmak sokarak kuvvetlice öğürtmek ve kusmasını sağlayarak lümeni temizlemeye hemen gayret etmek",
                        "is_correct": False,
                        "scenario_update": "Ağza parmak sokulması öğürme spazmına, mukozal abrazyona ve tükürüğün trakeobronşiyal ağaca aspire edilmesine neden oldu.",
                        "teaching_point": "Özofagus patolojisi şüphesinde körlemesine parmak manevraları ve kusturma kontrendikedir; lümen perforasyonu ve aspirasyon riskini artırır."
                    },
                    {
                        "text": "Lümeni mekanik olarak temizlemek amacıyla bebeğe zorla bol miktarda katı ekmek içi yedirmek ve su içirmeye çalışmak",
                        "is_correct": False,
                        "scenario_update": "Katı gıda takılan diskin üzerine bası yaparak mukozal hasarı artırdı ve çocukta tam solunum sıkıntısı tetiklendi.",
                        "teaching_point": "Özofagusta takılma şüphesi olan hastaya katı gıda veya sıvı verilmemelidir; perforasyon riskini ve aspirasyon tehlikesini tetikler."
                    },
                    {
                        "text": "Tablonun hafif bir boğaz enfeksiyonu olabileceğini düşünerek ağızdan parasetamol şurup içirmek ve evde dinlenmeye göndermek üzere reçetelemek",
                        "is_correct": False,
                        "scenario_update": "Oral şurup yutulamayıp aspire edildi; eve gönderilmek istenen çocukta göğüs ağrısı ve huzursuzluk şiddetlenerek devam etti.",
                        "teaching_point": "Ani başlayan disfaji ve tükürük yutamama tablosu akut cerrahi acildir; basit farenjit kabul edilip analjezikle evine gönderilemez."
                    },
                    {
                        "text": "Havayolu açıklığını ve aspirasyon riskini değerlendirmek, oral alımı derhal durdurup damar yolu açarak monitörize takibe almak",
                        "is_correct": True,
                        "explanation": "Ani disfaji ve tükürük yutamayan çocuklarda aspirasyonu önlemek için oral alım kesilmeli, havayolu güvenceye alınmalı ve İV erişim sağlanmalıdır.",
                        "new_finding": "Vital Bulgular: KTA 126/dk, SS 24/dk, TA 92/58 mmHg, SpO2 %98. Muayene: Sürekli tükürük akışı var, çocuk göğsünü tutarak ağlıyor, solunum sesleri kaba ancak stridor yok, orofarenkste travma izlenmedi."
                    }
                ]
            },
            {
                "stage_title": "Acil Radyolojik Görüntüleme ve İnceleme",
                "question": "Özofagusta şüpheli radyoopak disk alımı kuşkusu bulunan bu çocukta tanısal yerleşimi belirlemek için hangi radyolojik inceleme yapılmalıdır?",
                "options": [
                    {
                        "text": "Radyasyon almaması için düz film çekmeyip yalnızca baryumlu sindirim pasaj grafisi planlayarak bebeğe kontrast madde içirmeye kalkışmak",
                        "is_correct": False,
                        "scenario_update": "Olası perforasyon zemininde verilen baryumlu kontrast madde mediastene sızarak kimyasal mediastinit tehlikesi yarattı ve endoskopiyi zorlaştırdı.",
                        "teaching_point": "Perforasyon riski olan şüpheli lümen patolojilerinde baryum kontrendikedir; mediastene sızıntı ölümcül kimyasal mediastinite yol açabilir."
                    },
                    {
                        "text": "Boyun, göğüs ve batını içeren iki yönlü grafiler çekerek radyoopak diskin anatomik morfolojisini dikkatlice incelemek",
                        "is_correct": True,
                        "image": "assets/images/adbg_button_battery.png",
                        "image_caption": "Radyografi: Üst özofagus hizasında çift halka (double ring / halo) belirtisi veren radyoopak disk",
                        "explanation": "Ön-arka ve yan grafilerde diskin karakteristik kenar yapısı (çift kontur/halo ve basamak belirtisi) radyolojik tanıyı kesinleştirir.",
                        "new_finding": "Radyografi: Servikal özofagus C6-T1 hizasında yaklaşık 20 mm çapında, ön-arka grafide kenarında belirgin çift halka (halo) görünümü, yan grafide basamak belirtisi veren radyoopak disk saptandı."
                    },
                    {
                        "text": "Birincil basamakta derhal genel anestezi altında tüm vücut manyetik rezonans görüntülemesi planlayıp hastayı radyoloji ünitesine hızla göndermek",
                        "is_correct": False,
                        "scenario_update": "Metalik ferromanyetik materyal varlığında MR çekilmeye çalışılması doku ısınması ve cismin yer değiştirmesi riskini doğurdu.",
                        "teaching_point": "Vücutta metalik iletken disk şüphesi varken MR görüntüleme kesinlikle kontrendikedir; termal yanık ve doku hasarına neden olur."
                    },
                    {
                        "text": "Herhangi bir radyolojik film çekmeden çocuğu doğrudan çocuk cerrahisi polikliniğine sonraki haftalık rutin randevu sırasına yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Radyografik inceleme yapılmadığı için özofagustaki doku hasarı fark edilemedi ve duvarda saatler içinde tam kat nekroz gelişti.",
                        "teaching_point": "Akut yutma güçlüğü olan çocukta acil radyografi zorunludur; gecikme durumunda dokuda likefaksiyon nekrozu ve ölümcül perforasyon gelişir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Özofagus proksimalinde çift halka ve basamak belirtisi veren metalik disk saptanan hastada kesin tanı nedir?",
                "options": [
                    {
                        "text": "Özofagusta Düğme Pil İmpaksiyonu",
                        "is_correct": True,
                        "explanation": "Ön-arka grafide çift halka (halo) ve yan grafide basamak (step-off) belirtisi düğme pil için patognomoniktir; madeni paralardan ayırır.",
                        "new_finding": "Kesin tanı: Özofagusta Düğme Pil İmpaksiyonu. İki saat içinde perforasyon ve doku nekrozu riski nedeniyle acil endoskopi gerekir."
                    },
                    {
                        "text": "Özofagusta Madeni Para Sıkışması",
                        "is_correct": False,
                        "scenario_update": "Madeni paralar tek katmanlı homojen radyoopasite verir; çift halka (halo) veya basamak belirtisi göstermezler.",
                        "teaching_point": "Madeni para homojen radyoopaktır; çift kontur (halo) ve basamak görünümü iki kutuplu düğme pil yapısına özgüdür."
                    },
                    {
                        "text": "Akut Özofageal Kostik Yanık",
                        "is_correct": False,
                        "scenario_update": "Kostik sıvı alımlarında düz radyografide lümende sınırları keskin dairesel radyoopak metalik gölge izlenmez.",
                        "teaching_point": "Sıvı kostik madde alımları yaygın kimyasal yanık yapar ancak grafide disk şeklinde sınırları belirgin opasite oluşturmaz."
                    },
                    {
                        "text": "Konjenital Vasküler Halka Basısı",
                        "is_correct": False,
                        "scenario_update": "Vasküler halka basısı kronik stridor ve beslenme güçlüğü yapar; aniden başlayan metalik radyoopak gölge ile ilişkisizdir.",
                        "teaching_point": "Vasküler halka basısı kronik konjenital malformasyondur; ani başlayan disfaji ve radyografide disk gölgesi pil yutulmasını gösterir."
                    }
                ]
            },
            {
                "stage_title": "Acil Tedavi Yönetimi ve Konsültasyon",
                "question": "Özofagusta iki saat içinde likefaksiyon nekrozu ve fistül riski taşıyan bu hastada acil yönetim nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Kendiliğinden mideye geçmesini beklemek amacıyla oral laksatif şurup başlayıp çocuğu kırk sekiz saat sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Özofagusta bekletilen disk iki saat içinde özofagus duvarını eriterek trakeoözofageal fistül ve ağır mediastinit tablosuna yol açtı.",
                        "teaching_point": "Özofagustaki düğme pil kendiliğinden geçiş için asla bekletilemez; iki saat içinde tam kat nekroz ve trakeoözofageal fistül yapabilir."
                    },
                    {
                        "text": "Çocuğa bol lifli katı gıdalar yedirerek diski mekanik olarak aşağı itmeyi denemek ve ayaktan güvenle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Verilen katı gıdalar nekroze olan duvardan mediastene döküldü ve çocukta septik şok tablosu gelişti.",
                        "teaching_point": "Katı gıdayla itmeye çalışmak perforasyonu hızlandırır ve mediastinal kontaminasyona yol açar; oral alım kesinlikle durdurulmalıdır."
                    },
                    {
                        "text": "Çocuk cerrahisi veya gastroenteroloji konsültasyonuyla ilk iki saat içinde acil rijit endoskopi planlayıp ameliyathaneye nakletmek",
                        "is_correct": True,
                        "explanation": "Özofagus düğme pillerinde altın standart ilk 2 saat içinde genel anestezi altında rijit/fleksibl endoskopik acil çıkarmadır.",
                        "new_finding": "Hasta acilen ameliyathaneye alındı; çocuk cerrahisi tarafından rijit özofagoskopiyle lityum pil çıkarıldı, mukozal nekroz görüldü, perforasyon saptanmadı."
                    },
                    {
                        "text": "Acil girişim yapmadan çocuğu evine gönderip haftalık seri karın grafileriyle diskin dışkıdan spontan çıkışını uzun süre bekletmek",
                        "is_correct": False,
                        "scenario_update": "Müdahale edilmeyen çocukta aortoözofageal fistül ve masif gastrointestinal kanama nedeniyle ölümcül kardiyovasküler kollaps gelişti.",
                        "teaching_point": "Özofagus düğme pilleri acil cerrahi acildir; seri grafilerle haftalık takip yaklaşımı yalnızca mideyi geçmiş asemptomatik piller içindir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S30",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "3 Yaş",
        "gender": "Erkek",
        "complaint": "Safralı koyu yeşil fışkırır kusma, karında ileri derecede şişlik ve gaz-gaita çıkışının durması",
        "history": (
            "3 yaşındaki erkek çocuk (14 kg), on sekiz ay önce perfore apandisit nedeniyle açık operasyon geçirmiştir. "
            "On iki saat önce aniden başlayan safralı, koyu yeşil fışkırır kusma ve kıvrandırıcı karın ağrısıyla getirildi. "
            "Ailesi dünden beri hiç gaz ve gaita çıkarmadığını, karnının davul gibi gerginleştiğini ifade ediyor."
        ),
        "final_diagnosis": "Adezyona Bağlı Mekanik Bağırsak Obstrüksiyonu (Akut İleus)",
        "disposition": "Oral Stop (NPO) + Nazogastrik Dekompresyon + İntravenöz Kristaloid Sıvı Resüsitasyonu + Acil Çocuk Cerrahisi Konsültasyonu ve Yatış",
        "case_pearl": (
            "Pediatrik yaş grubunda safralı (koyu yeşil) kusma, aksi kanıtlanana kadar cerrahi mekanik bağırsak obstrüksiyonu olarak kabul edilmelidir. "
            "Daha önce geçirilmiş batın cerrahisi (örneğin perfore apandisit) öyküsü olan çocuklarda postoperatif adezyonlar (bridler) "
            "en sık mekanik obstrüksiyon nedenidir. Klinik bulgular safralı kusma, karın distansiyonu, kolik karın ağrısı, "
            "obstipasyon (gaz-gaita çıkaramama) ve metalik çınlama tarzında hiperaktif veya kaybolmuş barsak sesleridir. "
            "Ayakta direkt batın grafisinde (ADBG) dilate ince bağırsak ansları, merdiven basamağı şeklinde yaygın hava-sıvı seviyeleri "
            "ve kolonda gaz yokluğu tipiktir. Tedavide acil oral stop (NPO), geniş lümenli nazogastrik sonda ile sürekli dekompresyon, "
            "üçüncü boşluğa kaçan sıvıyı yerine koymak için agresif izotonik İV kristaloid sıvı resüsitasyonu, elektrolit takibi "
            "ve acil çocuk cerrahisi konsültasyonu esastır."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Resüsitasyon",
                "question": "Safralı kusma, karın distansiyonu ve gaz-gaita çıkışı olmayan 3 yaşındaki çocukta ilk acil yaklaşım ne olmalıdır?",
                "options": [
                    {
                        "text": "Dehidratasyonu hızla düzeltmek amacıyla bol miktarda oral rehidratasyon sıvısını zorlayarak içirmek ve kusmanın kendiliğinden kesilmesini sabırla beklemek",
                        "is_correct": False,
                        "scenario_update": "Oral sıvı alımı mide ve bağırsak içi basıncı dramatik artırarak masif safralı kusmaya ve akciğer aspirasyonuna neden oldu.",
                        "teaching_point": "Safralı kusan ve distandü batını olan çocukta oral alım derhal durdurulmalıdır; enteral sıvı verilmesi aspirasyon ve perforasyon riskini artırır."
                    },
                    {
                        "text": "Oral alımı durdurmak, nazogastrik sonda ile gastrointestinal dekompresyon sağlamak ve damar yolundan izotonik sıvı başlamak",
                        "is_correct": True,
                        "explanation": "Safralı kusma cerrahi mekanik engel göstergesidir; aspirasyonu önlemek için nazogastrik dekompresyon ve kayıplar için İV sıvı zorunludur.",
                        "new_finding": "Vital Bulgular: KTA 136/dk, SS 28/dk, TA 88/54 mmHg, SpO2 %98, KDZ 3 saniye. Muayene: Batın belirgin distandü, timpanik, sağ altta eski cerrahi skar mevcut; nazogastrik sondadan 140 mL koyu yeşil safralı mayi drene oldu."
                    },
                    {
                        "text": "Kusmayı durdurmak için hastaya yüksek doz oral antiemetik şurup içirip ayaktan izlemek üzere reçete düzenleyerek taburculuk planlamak",
                        "is_correct": False,
                        "scenario_update": "Antiemetik verilmesine rağmen bağırsak lümenindeki aşırı basınç nedeniyle kusma sürdü ve çocukta uykuya meyil gelişti.",
                        "teaching_point": "Safralı kusmalarda antiemetik verilmesi klinik tabloyu maskeler ve cerrahi tanıyı geciktirir; mekanik patolojide temel yaklaşım dekompresyondur."
                    },
                    {
                        "text": "Bağırsak pasajını açmak düşüncesiyle yüksek basınçlı hipertonik rektal lavman uygulayarak çocuğu derhal evine göndermek ve yakın izlem önermek",
                        "is_correct": False,
                        "scenario_update": "İnce bağırsak düzeyindeki mekanik geçiş durmasında rektal lavman distansiyonu artırdı ve hastada şiddetli hipotansiyon gelişti.",
                        "teaching_point": "İnce bağırsak düzeyindeki mekanik patolojilerde rektal lavman etkisizdir; hipotansiyon, perforasyon ve elektrolit bozukluğuna yol açabilir."
                    }
                ]
            },
            {
                "stage_title": "Acil Radyolojik Görüntüleme ve İnceleme",
                "question": "Safralı kusma ve batın distansiyonu olan bu hastada bağırsak lümen içi hava-sıvı dağılımını gösteren ilk radyolojik tetkik nedir?",
                "options": [
                    {
                        "text": "Radyasyon almaması için görüntüleme yapmayıp sadece tam idrar tahlili ve dışkıda parazit incelemesiyle yetinerek hastayı acilde izlemek",
                        "is_correct": False,
                        "scenario_update": "İdrar ve gaita tetkikleri normal sonuçlandı ancak batın içi distansiyon ilerleyerek solunum sıkıntısına ve şoka neden oldu.",
                        "teaching_point": "Safralı kusma ve akut cerrahi batın tablosunda acil radyolojik görüntüleme zorunludur; idrar veya gaita tahlili cerrahi patolojiyi dışlayamaz."
                    },
                    {
                        "text": "Birincil basamakta derhal genel anestezi altında acil kolonoskopi planlayarak kalın bağırsak mukozasını endoskopik olarak ayrıntılı biçimde incelemek",
                        "is_correct": False,
                        "scenario_update": "Akut distandü ince bağırsak patolojisinde kolonoskopi hiçbir tanısal katkı sağlamadı, aksine bağırsak perforasyonu riski yarattı.",
                        "teaching_point": "İnce bağırsak düzeyindeki tablolarda kolonoskopi endike değildir; aşırı distandü lümende perforasyon tehlikesi oluşturur."
                    },
                    {
                        "text": "Ayakta direkt batın grafisi çekerek bağırsak anslarındaki patolojik genişlemeyi ve hava-sıvı seviyelerini radyolojik olarak incelemek",
                        "is_correct": True,
                        "image": "assets/images/adbg_air_fluid.png",
                        "image_caption": "ADBG: İnce bağırsak anslarında dilatasyon ve merdiven basamağı şeklinde yaygın hava-sıvı seviyeleri",
                        "explanation": "Ayakta direkt batın grafisi, dilate bağırsak anslarını ve basamak tarzı hava-sıvı seviyelerini göstererek mekanik geçiş bozukluğunu doğrular.",
                        "new_finding": "Ayakta Direkt Batın Grafisi: İnce bağırsak anslarında belirgin lümen dilatasyonu, orta batında merdiven basamağı şeklinde çok sayıda hava-sıvı seviyesi, kolonda gaz yokluğu izlendi; diyafram altı serbest hava saptanmadı."
                    },
                    {
                        "text": "Görüntüleme istemeden doğrudan oral yoldan yoğun baryum sülfat içirerek sindirim sistemi pasaj grafisi çekmeye derhal acilde kalkışmak",
                        "is_correct": False,
                        "scenario_update": "Mekanik tıkanma zemininde verilen baryum lümende taşlaşarak impaksiyona yol açtı ve olası cerrahi girişimi zorlaştırdı.",
                        "teaching_point": "Akut lümen obstrüksiyonu şüphesinde oral baryum verilmesi kontrendikedir; lümende sertleşir ve perforasyon riskini artırır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Geçirilmiş batın cerrahisi, safralı kusma, karın distansiyonu ve grafide merdiven basamağı hava-sıvı seviyeleriyle kesin tanı nedir?",
                "options": [
                    {
                        "text": "Akut Viral Gastroenterit",
                        "is_correct": False,
                        "scenario_update": "Gastroenteritte sulu ishal ve kramp ağrıları olur; safralı fışkırır kusma ve yaygın hava-sıvı seviyeleri görülmez.",
                        "teaching_point": "Gastroenteritte ishal ön plandadır; safralı kusma ve grafide basamak hava-sıvı seviyeleri mekanik bağırsak obstrüksiyonunu gösterir."
                    },
                    {
                        "text": "Kronik Fonksiyonel Konstipasyon",
                        "is_correct": False,
                        "scenario_update": "Konstipasyonda safralı fışkırır kusma görülmez; grafide rektumda yoğun dışkı birikimi saptanır.",
                        "teaching_point": "Fonksiyonel kabızlıkta safralı kusma beklenmez; safralı kusma cerrahi mekanik patolojinin kardinal belirtisidir."
                    },
                    {
                        "text": "Pediatrik Siklik Kusma",
                        "is_correct": False,
                        "scenario_update": "Siklik kusmada tekrarlayan kusma atakları olur ancak batında masif distansiyon ve merdiven basamağı seviyeleri izlenmez.",
                        "teaching_point": "Siklik kusma santral kökenli benign bir tablodur; karın distansiyonu ve mekanik hava-sıvı seviyeleri cerrahi ileus bulgusudur."
                    },
                    {
                        "text": "Mekanik Bağırsak Obstrüksiyonu",
                        "is_correct": True,
                        "explanation": "Geçirilmiş cerrahi öyküsü, safralı kusma, distansiyon, obstipasyon ve ADBG'de merdiven basamağı hava-sıvı seviyeleri mekanik obstrüksiyonu (ileus) doğrular.",
                        "new_finding": "Kesin tanı: Adezyona Bağlı Mekanik Bağırsak Obstrüksiyonu (Brid İleus). Acil cerrahi eksplorasyon kararı alındı."
                    }
                ]
            },
            {
                "stage_title": "Acil Tedavi Yönetimi ve Konsültasyon",
                "question": "Nazogastrik dekompresyon sağlanan ve grafisinde multipl hava-sıvı seviyeleri saptanan bu hastanın kesin tedavi ve takip stratejisi ne olmalıdır?",
                "options": [
                    {
                        "text": "Nazogastrik dekompresyon ve intravenöz hidrasyona devam ederek acil çocuk cerrahisi konsültasyonuyla operasyon kararı açısından yatırmak",
                        "is_correct": True,
                        "explanation": "Postoperatif adezyona bağlı mekanik obstrüksiyonda sürekli NPO, NG dekompresyon, İV kristaloid ve cerrahi değerlendirme standart yönetimdir.",
                        "new_finding": "Çocuk cerrahisi hastayı servise devraldı; intravenöz sıvı resüsitasyonu ve nazogastrik dekompresyon sonrası acil eksploratris laparotomiyle brid ligasyonu yapıldı."
                    },
                    {
                        "text": "Hastanın nazogastrik sondasını çekip tam yağlı sütle beslemeye başlamak ve çocuk polikliniğine elektif randevu vererek hemen göndermek",
                        "is_correct": False,
                        "scenario_update": "Sondası çekilip beslenen çocukta masif safralı aspirasyon ve solunum durması gelişti, acil resüsitasyon gerekti.",
                        "teaching_point": "Mekanik obstrüksiyonda besleme yapılamaz; nazogastrik sonda çekilirse masif aspirasyon ve fatal komplikasyonlar kaçınılmazdır."
                    },
                    {
                        "text": "Tablonun kendiliğinden geçeceğini öngörerek oral laksatif ilaç reçete edip acil servisten taburculuk kararı alarak evine hızla yollamak",
                        "is_correct": False,
                        "scenario_update": "Mekanik adezyon varlığında verilen laksatifler lümen içi basıncı artırarak ince bağırsak perforasyonu ve fekal peritonit yaptı.",
                        "teaching_point": "Mekanik obstrüksiyonda oral laksatifler kesinlikle kontrendikedir; proksimalde basıncı artırarak bağırsak gangreni ve perforasyona yol açar."
                    },
                    {
                        "text": "Damar yolunu çekerek hastayı sedatize etmek ve yirmi dört saat boyunca hiçbir medikal destek vermeden evde gözlemek",
                        "is_correct": False,
                        "scenario_update": "Sıvı desteği kesilen ve evde izlenen çocukta üçüncü boşluk kayıplarına bağlı derin hipovolemik şok ve nekroz gelişti.",
                        "teaching_point": "Mekanik obstrüksiyonlu çocuklarda masif sıvı kayıpları hipovolemik şoka götürür; agresif İV sıvı desteği ve cerrahi izlem hayatidir."
                    }
                ]
            }
        ]
    }
]
