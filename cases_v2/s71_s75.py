# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - S71-S75 (Nöbet ve Solunum Acilleri)
"""

SPOILERS = {
    "S71": ["status epileptikus", "status"],
    "S72": ["provoke olmayan", "ilk afebril nöbet"],
    "S73": ["ağır astım", "ağır akut astım", "status astmatikus"],
    "S74": ["bronşiolit", "bronşiyolit", "rsv"],
    "S75": ["kızamık", "rubeola", "morbilli"],
}

CASES = [
    {
        "id": "S71",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "9 Yaşında (30 kg)",
        "gender": "Erkek",
        "complaint": "Evde başlayan ve hastaneye gelişinde hâlâ süren kasılma",
        "history": "Ambulansla getirildi. Annesi anlatıyor: 'Epilepsisi var, levetirasetam kullanıyor. Bayramda köye gittik, ilacı bitti, üç gündür veremedik. Yarım saat önce kollarını, bacaklarını kasıp titremeye başladı, gözleri yukarı kaydı. Ambulansta burnuna bir ilaç sıktılar, biraz azaldı ama tekrar başladı.' Ambulans ekibi 20 dakika önce intranazal midazolam uyguladığını bildiriyor. Ateş, kusma, baş travması öyküsü yok. Bilinen başka hastalığı yok.",
        "final_diagnosis": "Antiepileptik İlaç Kesilmesine Bağlı Konvülzif Status Epileptikus (Benzodiazepine Dirençli)",
        "disposition": "İkinci Basamak Antiepileptik Yüklemesi Sonrası Çocuk Nörolojisi ile Pediatri Servisine (Gerekirse Yoğun Bakıma) Yatış",
        "case_pearl": "Beş dakikadan uzun süren veya aralarında bilincin düzelmediği nöbetler status epileptikus olarak tedavi edilir. Hava yolu, oksijen ve kan şekeri kontrolünden sonra en fazla iki doz benzodiazepin verilir; hastane öncesi dozlar da sayılır. Nöbet sürerse ikinci basamak ilaç (levetirasetam 40-60 mg/kg, fenitoin/fosfenitoin 20 mg/kg veya valproat 40 mg/kg) gecikmeden yüklenir. Üçüncü doz benzodiazepin solunum depresyonunu artırır ve önerilmez. Bilinen epileptikte en sık neden ilaç uyumsuzluğudur; rutin acil BT gerekmez. Nöbet 40 dakikayı aşarsa anestezi ve entübasyon gündeme gelir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Stabilizasyon",
                "question": "Kasılması süren bu çocuğa gelişinde ilk yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Yan yatırıp hava yolunu açmak, oksijen vermek, monitörize etmek, kan şekerine bakıp damar yolundan ikinci benzodiazepin dozunu yapmak",
                        "is_correct": True,
                        "explanation": "Hava yolu, oksijen ve kan şekeri her nöbette önceliklidir. Hastane öncesi bir doz verilmiş olduğundan acilde yalnızca bir doz benzodiazepin daha uygulanır.",
                        "new_finding": "KTA 142/dk, SS 26/dk, KB 118/72 mmHg, SpO2 %93'ten oksijenle %99'a çıktı, ateş 37.3°C. Kapiller kan şekeri 112 mg/dL. Bilateral jeneralize tonik-klonik kasılmalar sürüyor. İV midazolam 0.1 mg/kg (3 mg) verildi. Beş dakika sonra kasılmalar sürüyor, solunum yeterli."
                    },
                    {
                        "text": "Kasılmayı durdurmak için ağzına dil basacağı yerleştirmek, kollarını tutarak sabitlemek ve damar yolu açılana kadar beklemek",
                        "is_correct": False,
                        "scenario_update": "Dil basacağı dişlerde kırılmaya ve ağızda kanamaya yol açtı; kasılmalar sürdü.",
                        "teaching_point": "Nöbet geçiren çocuğun ağzına cisim konmaz ve hareketleri zorla kısıtlanmaz."
                    },
                    {
                        "text": "Nöbetin nedenini bulmak için kasılma sürerken hemen beyin tomografisine götürmek ve sonrasında tedaviye karar vermek",
                        "is_correct": False,
                        "scenario_update": "Tomografide hava yolu korunamadı, SpO2 %85'e düştü; tedavi gecikti.",
                        "teaching_point": "Önce nöbet durdurulur ve hasta stabilize edilir; görüntüleme gerekiyorsa sonra yapılır."
                    },
                    {
                        "text": "Hastane öncesinde verilen intranazal dozu hesaba katmadan ardışık üç doz intravenöz diazepam uygulayıp her doz sonrası yanıtı beklemek",
                        "is_correct": False,
                        "scenario_update": "Üçüncü doz sonrası solunum yüzeyelleşti, SpO2 %84'e düştü ve balon-maske ventilasyon gerekti.",
                        "teaching_point": "Hastane öncesi doz da sayılarak toplam iki doz benzodiazepinden sonra ikinci basamak ilaca geçilir."
                    }
                ]
            },
            {
                "stage_title": "İkinci Basamak Tedavi",
                "question": "İki doz benzodiazepine rağmen kasılmaları süren bu çocukta bir sonraki adım nedir?",
                "options": [
                    {
                        "text": "Üçüncü doz midazolamı intramüsküler yapmak ve nöbetin kendiliğinden durmasını 15 dakika daha beklemek",
                        "is_correct": False,
                        "scenario_update": "Kasılmalar sürdü, solunum depresyonu gelişti ve nöbet süresi uzadı.",
                        "teaching_point": "Benzodiazepine dirençli nöbette bekleme süresi nöronal hasar ve tedaviye direnci artırır."
                    },
                    {
                        "text": "Hemen entübe edip tiyopental infüzyonu başlamak ve çocuğu yoğun bakıma almak için ikinci basamak ilacı atlamak",
                        "is_correct": False,
                        "scenario_update": "İkinci basamak ilaç verilmeden anestezi başlandı; derin hipotansiyon gelişti.",
                        "teaching_point": "Anestezik infüzyon ikinci basamak ilaçlara yanıtsız dirençli tabloda düşünülür."
                    },
                    {
                        "text": "Levetirasetam 60 mg/kg intravenöz yükleme dozunu 5-10 dakikada vermek; yanıt yoksa fenitoin veya valproat hazırlamak",
                        "is_correct": True,
                        "explanation": "Benzodiazepine dirençli nöbette ikinci basamak ilaç gecikmeden yüklenir. Hasta zaten bu ilacı kullandığından levetirasetam hem etkili hem de güvenli bir seçimdir.",
                        "new_finding": "Levetirasetam 1800 mg İV verildi. İnfüzyonun bitiminden 3 dakika sonra kasılmalar durdu. GKS 9, solunum düzenli, SpO2 %99 (oksijenle). Pupiller izokorik, ışık refleksi var, ense sertliği yok."
                    },
                    {
                        "text": "Rektal parasetamol ve intravenöz %3 NaCl vermek, ardından kalsiyum glukonat uygulayıp yanıtı değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Elektrolit bozukluğu olmayan çocuğa gereksiz tedaviler verildi; nöbet sürdü.",
                        "teaching_point": "Elektrolit tedavisi yalnızca ölçülmüş bozuklukta verilir; burada antiepileptik gerekir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu tablonun en olası tanısı nedir?",
                "options": [
                    {"text": "Komplike febril konvülziyon", "is_correct": False, "scenario_update": "Çocuk 9 yaşındaydı ve ateşi yoktu.", "teaching_point": "Febril konvülziyon 6 ay-5 yaş arasında ateşle olur."},
                    {"text": "Psikojenik non-epileptik nöbet", "is_correct": False, "scenario_update": "Gözler yukarı kaymıştı, SpO2 düşmüştü ve postiktal dönem belirgindi.", "teaching_point": "Psikojenik nöbetlerde gözler sıkıca kapalıdır, hareketler asenkrondur, desatürasyon olmaz."},
                    {"text": "İlaç kesilmesine bağlı konvülzif status epileptikus", "is_correct": True, "explanation": "Bilinen epilepside ilacın üç gün verilmemesi, beş dakikayı aşan ve iki doz benzodiazepine dirençli jeneralize nöbet konvülzif status epileptikusu gösterir.", "new_finding": "Tanı: Antiepileptik ilaç kesilmesine bağlı konvülzif status epileptikus."},
                    {"text": "Akut bakteriyel menenjit", "is_correct": False, "scenario_update": "Ateş ve ense sertliği yoktu, açık bir tetikleyici vardı.", "teaching_point": "Ateş, ense sertliği veya bilincin açıklanamayan bozukluğunda lomber ponksiyon düşünülür."}
                ]
            },
            {
                "stage_title": "Nöbet Sonrası Yönetim ve Yatış",
                "question": "Nöbeti duran bu çocuk için en uygun plan hangisidir?",
                "options": [
                    {
                        "text": "Bilinci düzelmesini beklemeden rutin acil kontrastsız beyin tomografisi çekip normalse acilden taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Tomografi normal geldi; taburculuk sonrası evde yeni bir nöbet oldu.",
                        "teaching_point": "Açık nedeni olan bilinen epileptikte rutin BT gerekmez; status sonrası çocuk yatırılarak izlenir."
                    },
                    {
                        "text": "Elektrolitleri kontrol etmek, idame ilacı yeniden başlatıp servise yatırmak ve aileye evde kurtarıcı ilaç kullanımını öğretmek",
                        "is_correct": True,
                        "explanation": "Status sonrası çocuk bilinci tam düzelene kadar izlenir. İdame tedavinin kesintisiz sürmesi ve evde kurtarıcı ilaç planı tekrarı önler.",
                        "new_finding": "Elektrolitler normal. Levetirasetam idamesi başlandı. Çocuk 4 saat içinde tam bilinçlendi, nörolojik muayenesi normal. Aileye intranazal midazolam eğitimi verildi ve 48 saat sonra taburcu edildi."
                    },
                    {
                        "text": "Levetirasetamın etkisiz olduğunu düşünüp kesmek, yerine fenobarbital idamesi başlamak ve tedaviyi değiştirmek",
                        "is_correct": False,
                        "scenario_update": "Etkili olan ilaç gereksiz yere değiştirildi; fenobarbital çocukta uyuklama ve okul başarısında düşüş yaptı.",
                        "teaching_point": "Nöbet ilacın alınmamasıyla ortaya çıktıysa ilaç etkisiz sayılmaz; uyum sağlanır."
                    },
                    {
                        "text": "Lomber ponksiyon ve EEG yapılmadan yatış verilmemesi gerektiğini düşünüp ikisini acilde hemen planlamak",
                        "is_correct": False,
                        "scenario_update": "Ateşsiz ve ense sertliği olmayan çocukta gereksiz lomber ponksiyon yapıldı.",
                        "teaching_point": "Lomber ponksiyon enfeksiyon şüphesinde yapılır; EEG çoğu zaman acil değildir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S72",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "8 Yaşında",
        "gender": "Kız",
        "complaint": "Sabah uyanırken bir kez olan, iki dakika süren tüm vücutta kasılma ve ardından uyku hali",
        "history": "Annesi anlatıyor: 'Sabah 7'de odasından ses geldi. Yatakta kolları bacakları kasılmış, titriyordu, ağzından köpük geliyordu, altına kaçırmıştı. İki dakika kadar sürdü. Sonra 20 dakika uyudu, şimdi biraz kafası karışık ama bizi tanıyor.' Ateş yok, son günlerde hastalık geçirmemiş. Kafa travması yok. Evde ilaç, alkol veya zehirli madde erişimi yok. Daha önce nöbeti olmamış. Dün gece arkadaşının doğum gününde geç saate kadar uyumamış. Halasında epilepsi var. Okul başarısı iyi.",
        "final_diagnosis": "İlk Provoke Olmayan Jeneralize Tonik-Klonik Nöbet (Uykusuzlukla Tetiklenen)",
        "disposition": "Bazal Duruma Dönüş ve Gözlem Sonrası Ayaktan EEG ve Çocuk Nörolojisi Randevusuyla Taburculuk",
        "case_pearl": "İlk provoke olmayan nöbette çocuk bazal nörolojik durumuna döndüyse ve muayene normalse acil görüntüleme gerekmez. Kan şekeri ölçülür, EKG çekilir (uzun QT gibi kardiyak nedenli konvülzif senkopu dışlamak için). Rutin elektrolit, toksikoloji ve lomber ponksiyon yalnızca öyküye göre yapılır. EEG ve gerekirse MR ayaktan planlanır. İlk nöbetten sonra genellikle antiepileptik başlanmaz; tekrarlama riski yaklaşık %40-50'dir. Aileye nöbet sırasında yapılacaklar, yüzme ve banyoda gözetim ve uyku düzeni anlatılır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Nörolojik Muayene",
                "question": "Nöbeti geçmiş, uykulu ama yanıt veren bu çocukta ilk değerlendirmeniz nedir?",
                "options": [
                    {
                        "text": "Nöbetin yeniden tekrarlamasını önlemek için muayeneden önce intravenöz diazepam ve ardından fenitoin yüklemesi yapmak",
                        "is_correct": False,
                        "scenario_update": "Nöbeti olmayan çocuğa verilen ilaçlar derin uyuklama yaptı ve nörolojik muayene değerlendirilemedi.",
                        "teaching_point": "Duran bir nöbet için benzodiazepin veya yükleme dozu verilmez."
                    },
                    {
                        "text": "Vital bulgular ve kan şekerini ölçmek, menenjit bulgularını aramak, nörolojik muayene yapıp bilincin düzelmesini izlemek",
                        "is_correct": True,
                        "explanation": "Ateş, menenjit bulgusu, odak defisit veya bilincin düzelmemesi farklı bir yaklaşım gerektirir. Hipoglisemi her nöbette dışlanmalıdır.",
                        "new_finding": "Ateş 36.8°C, KTA 92/dk, SS 20/dk, KB 104/66 mmHg, SpO2 %99. Kan şekeri 96 mg/dL. Dilinin yan kenarında ısırık izi. Ense sertliği yok, cilt döküntüsü yok. Pupiller izokorik, kranial sinirler normal, kas gücü ve refleksler simetrik, Babinski negatif. Bir saat içinde bilinci tamamen düzeldi, yürüyüşü normal."
                    },
                    {
                        "text": "Çocuğu hemen sarı alanda entübasyona hazırlayıp yoğun bakım yatağı istemek, ardından nörolojik muayene ve kan şekeri ölçümü yapmak",
                        "is_correct": False,
                        "scenario_update": "Solunumu yeterli ve bilinci düzelen çocukta gereksiz hazırlık yapıldı.",
                        "teaching_point": "Hava yolu yeterli ve bilinci düzelen hastada ileri hava yolu girişimi gerekmez."
                    },
                    {
                        "text": "Olayın bayılma olduğunu düşünüp muayene yapmadan sıvı içirerek taburcu etmek ve aileyi rahatlatmak",
                        "is_correct": False,
                        "scenario_update": "Değerlendirme yapılmadan gönderilen çocuk iki hafta sonra okulda yeniden kasıldı.",
                        "teaching_point": "Dil ısırığı, idrar kaçırma ve uzamış bilinç bulanıklığı nöbeti senkoptan ayırmaya yardımcıdır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Bilinci tamamen düzelen ve nörolojik muayenesi normal olan bu çocukta hangi tetkik yaklaşımı uygundur?",
                "options": [
                    {
                        "text": "Acil kontrastsız beyin tomografisi, lomber ponksiyon ve geniş toksikoloji paneli istemek, sonuçlara göre karar vermek",
                        "is_correct": False,
                        "scenario_update": "Tüm sonuçlar normal geldi; çocuk gereksiz radyasyon ve girişime maruz kaldı.",
                        "teaching_point": "Bazal duruma dönen, normal muayeneli çocukta bu tetkikler rutin değildir."
                    },
                    {
                        "text": "Elektrolitler, kalsiyum ve magnezyumu ölçmek; normalse ek tetkik istemeden aileyi bilgilendirip taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Değerler normal geldi; kardiyak ritim değerlendirmesi ve nöroloji planı yapılmadan gönderildi.",
                        "teaching_point": "Kardiyak nedenli konvülzif senkopu atlamamak için EKG çekilmeli ve ayaktan nöroloji planı yapılmalıdır."
                    },
                    {
                        "text": "Rutin kan tetkiki istememek; 12 derivasyonlu EKG çekmek, EEG ve çocuk nörolojisi randevusunu ayaktan planlamak",
                        "is_correct": True,
                        "explanation": "EKG uzun QT ve diğer aritmileri dışlar. EEG nöbet tipini ve tekrar riskini belirlemeye yardım eder; ayaktan yapılabilir. Acil görüntüleme yalnızca odak bulgu veya bilincin düzelmemesinde gerekir.",
                        "new_finding": "EKG normal sinüs ritmi, QTc 410 ms. Çocuk nörolojisi ile görüşüldü; bir hafta içinde EEG ve poliklinik randevusu verildi."
                    },
                    {
                        "text": "Acil EEG çekilmeden ve beyin MR'ı yapılmadan çocuğun taburcu edilmemesi gerektiği için yatırmak",
                        "is_correct": False,
                        "scenario_update": "Çocuk tetkikler için üç gün yatırıldı; sonuçlar yönetimi değiştirmedi.",
                        "teaching_point": "İyi görünen çocukta EEG ve MR ayaktan planlanabilir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu çocuktaki tablonun en olası tanısı nedir?",
                "options": [
                    {"text": "Uzun QT'ye bağlı konvülzif senkop", "is_correct": False, "scenario_update": "EKG'de QTc normaldi ve olay egzersiz ya da ani ses ile tetiklenmemişti.", "teaching_point": "Kardiyak senkop egzersiz, ani ses veya yüzmeyle tetiklenir ve postiktal dönemi kısadır."},
                    {"text": "Uykusuzlukla tetiklenen ilk provoke olmayan jeneralize nöbet", "is_correct": True, "explanation": "Ateş, travma, metabolik veya toksik neden olmadan ortaya çıkan, dil ısırığı ve postiktal konfüzyonla seyreden ilk jeneralize tonik-klonik nöbet ilk provoke olmayan nöbeti gösterir. Uykusuzluk eşiği düşüren bir faktördür.", "new_finding": "Tanı: İlk provoke olmayan jeneralize tonik-klonik nöbet."},
                    {"text": "Vazovagal senkop", "is_correct": False, "scenario_update": "Olay yatarken başlamıştı ve postiktal dönem 20 dakikadan uzundu.", "teaching_point": "Vazovagal senkop ayakta, bulantı-terleme prodromuyla başlar; bilinç hızla düzelir."},
                    {"text": "Akut viral ensefalit", "is_correct": False, "scenario_update": "Ateş yoktu ve bilinç bir saat içinde tamamen düzeldi.", "teaching_point": "Ensefalitte ateş, uzamış bilinç değişikliği ve davranış bozukluğu olur."}
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk ve ailesi için en uygun plan hangisidir?",
                "options": [
                    {
                        "text": "Antiepileptik başlamadan nöbette yapılacakları, yüzme ve banyoda gözetimi, düzenli uykuyu anlatmak; ayaktan EEG ve nöroloji kontrolüyle taburcu etmek",
                        "is_correct": True,
                        "explanation": "İlk nöbet sonrası çoğu çocukta ilaç başlanmaz; karar EEG ve tekrar riskine göre nörolojide verilir. Güvenlik önerileri tekrar eden bir nöbetin zararını önler.",
                        "new_finding": "Aile eğitildi ve yazılı bilgi verildi. EEG'de jeneralize diken-dalga deşarjları görüldü; nöroloji kontrolünde izlem kararı alındı."
                    },
                    {
                        "text": "Tekrarı önlemek için hemen valproat idamesi başlayıp ömür boyu kullanması gerektiğini söyleyerek taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Erken başlanan ilaç kilo artışı ve bulantı yaptı; aile gereksiz yere kaygılandı.",
                        "teaching_point": "Tek nöbetten sonra ilaç rutin değildir; kararı çocuk nörolojisi verir."
                    },
                    {
                        "text": "Nöbet geçirdiği için okula gitmemesini, spor ve tüm fiziksel etkinlikleri altı ay bırakmasını önermek",
                        "is_correct": False,
                        "scenario_update": "Çocuk okuldan ve arkadaşlarından uzak kaldı; yaşam kalitesi gereksiz yere bozuldu.",
                        "teaching_point": "Gözetimli etkinliklere devam edilir; yalnızca yüzme ve yüksekte durma gibi riskli durumlarda önlem alınır."
                    },
                    {
                        "text": "Ateş olmadan nöbet geçirdiği için evde ateş düşürücü saklamalarını ve nöbet olursa ağzına su dökmelerini önermek",
                        "is_correct": False,
                        "scenario_update": "Aile yanlış ilk yardım bilgileriyle gönderildi; aspirasyon riski oluştu.",
                        "teaching_point": "Nöbet sırasında ağızdan hiçbir şey verilmez; çocuk yan yatırılır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S73",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "11 Yaşında (36 kg)",
        "gender": "Erkek",
        "complaint": "İki gündür artan nefes darlığı, bugün konuşurken nefesinin yetmemesi",
        "history": "Annesi anlatıyor: 'Astımı var, kontrol ilacını yazın havalar düzelince kendimiz kestik. İki gündür nezleydi, öksürüyordu. Dün gece kurtarıcı spreyini 10 kez kullandı, az rahatladı. Sabah tekrar kötüleşti, cümle kuramıyor.' Son bir yılda iki kez acile gelmiş, bir kez serviste yatmış, hiç yoğun bakıma girmemiş. Ateş 37.9°C olmuş. Evde sigara içiliyor.",
        "final_diagnosis": "Ağır Akut Astım Atağı (İlk Basamak Tedaviye Yanıtsız, İV Magnezyum Sülfat Gerektiren)",
        "disposition": "İV Magnezyum Sülfat Sonrası Sürekli Monitörizasyonla Pediatri Servisine, Kötüleşirse Yoğun Bakıma Yatış",
        "case_pearl": "Ağır atakta çocuk tek kelimeyle konuşur, yardımcı solunum kaslarını kullanır, SpO2 %92'nin altındadır ve PEF beklenenin %50'sinin altındadır. Sessiz akciğer, siyanoz, bilinç değişikliği ve normal ya da yükselen pCO2 yaşamı tehdit eden bulgulardır. Tedavi oksijen, ilk saatte üç kez salbutamol ve ipratropiyum, erken sistemik kortikosteroiddir. Yanıt yetersizse İV magnezyum sülfat (40-50 mg/kg, en fazla 2 g, 20 dakikada) verilir. Rutin akciğer grafisi ve antibiyotik gerekmez. Sedatif ilaçlar kontrendikedir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Acil Tedavi",
                "question": "Tek kelimeyle konuşabilen bu çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Huzursuzluğu azaltıp nefesini düzenlemesi için düşük doz intravenöz midazolam vermek, ardından nebül tedavisi planlamak",
                        "is_correct": False,
                        "scenario_update": "Midazolam sonrası solunum yüzeyelleşti, SpO2 %84'e düştü.",
                        "teaching_point": "Astım atağında sedasyon solunum yetmezliğini hızlandırır; kontrendikedir."
                    },
                    {
                        "text": "Akciğer grafisi ve kan sayımı sonucu gelene kadar yalnızca oksijen vermek, sonra tedaviyi seçmek",
                        "is_correct": False,
                        "scenario_update": "Bekleme süresinde çocuk yoruldu, SpO2 %87'ye düştü.",
                        "teaching_point": "Tetkik beklenmeden bronkodilatör ve kortikosteroid tedavisi hemen başlanmalıdır."
                    },
                    {
                        "text": "Oturtup oksijenle SpO2'yi %94 üzerinde tutmak; üç kez salbutamol-ipratropiyum nebülü ve hemen sistemik kortikosteroid vermek",
                        "is_correct": True,
                        "explanation": "Ağır bulgulu çocukta oksijen, art arda bronkodilatör ve erken sistemik kortikosteroid ilk saatin temel tedavisidir. Kortikosteroidin etkisi saatler sonra başladığı için geciktirilmemelidir.",
                        "new_finding": "Başlangıçta: KTA 138/dk, SS 38/dk, SpO2 %89 (oda havası), tek kelimelerle konuşuyor, sternokleidomastoid ve interkostal çekilme, dinlemekle ekspiryum uzamış, yaygın hışıltı, bazallerde ses azalmış. PEF beklenenin %32'si. Oksijen, üç kez salbutamol-ipratropiyum ve İV metilprednizolon 1 mg/kg verildi."
                    },
                    {
                        "text": "Ateşi olduğu için bakteriyel enfeksiyon kabul edip önce kan kültürü alarak intravenöz seftriakson başlamak ve nebülü sonraya bırakmak",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik bronkospazmı düzeltmedi; çocuk yoruldu.",
                        "teaching_point": "Atakların çoğunu viral enfeksiyon tetikler; antibiyotik rutin değildir."
                    }
                ]
            },
            {
                "stage_title": "Yanıt Değerlendirmesi ve Kan Gazı",
                "question": "İlk saatin sonunda SpO2 %91 (oksijenle), SS 34/dk ve hâlâ kısa ifadelerle konuşuyor. Kan gazı sonucu nasıl yorumlanmalıdır?",
                "options": [
                    {
                        "text": "pH 7.38 ve pCO2 42 mmHg normal sınırlarda olduğu için çocuğun iyileştiğini gösterir ve nebül sıklığı azaltılabilir",
                        "is_correct": False,
                        "scenario_update": "Tedavi azaltılınca çocuk yoruldu ve pCO2 52 mmHg'ye yükseldi.",
                        "teaching_point": "Takipneik çocukta pCO2 düşük olmalıdır; normal değer yorgunluğun ve yaklaşan yetmezliğin işaretidir."
                    },
                    {
                        "text": "Takipneye rağmen normal olan pCO2 (42 mmHg), solunum kaslarının yorulduğunu ve yaklaşan yetmezliği gösteren bir alarm bulgusudur",
                        "is_correct": True,
                        "explanation": "Atak sırasında hiperventilasyon pCO2'yi düşürür. Takipneik bir çocukta normale dönen pCO2 solunum kaslarının yorulduğunu gösterir ve tedavi yoğunlaştırılmalıdır.",
                        "new_finding": "Kan gazı: pH 7.38, pCO2 42 mmHg, HCO3 24 mmol/L, laktat 2.6 mmol/L. Potasyum 3.4 mmol/L. Çocuk yorgun görünüyor, hışıltı bazallerde zor duyuluyor."
                    },
                    {
                        "text": "Laktat yüksekliği sepsisi gösterir; kan kültürü alıp geniş spektrumlu antibiyotik başlamak gerekir",
                        "is_correct": False,
                        "scenario_update": "Kültürler negatif geldi; laktat yüksekliği salbutamole bağlıydı.",
                        "teaching_point": "Salbutamol tedavisi laktat yükselmesine ve hipokalemiye yol açabilir."
                    },
                    {
                        "text": "Potasyumun 3.4 mmol/L olması salbutamol tedavisinin hemen kesilmesini ve yerine teofilin başlanmasını gerektirir",
                        "is_correct": False,
                        "scenario_update": "Salbutamol kesilince bronkospazm arttı; teofilin kusma ve taşikardi yaptı.",
                        "teaching_point": "Hafif hipokalemi izlenir ve gerekirse yerine konur; bronkodilatör kesilmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu çocuktaki tablonun en doğru tanımı hangisidir?",
                "options": [
                    {"text": "Hafif-orta astım atağı", "is_correct": False, "scenario_update": "Tek kelimeyle konuşuyor, SpO2 %89 ve PEF %32'ydi.", "teaching_point": "Hafif-orta atakta çocuk cümle kurar, SpO2 ≥%92 ve PEF ≥%50'dir."},
                    {"text": "Toplum kökenli pnömoni", "is_correct": False, "scenario_update": "Bulgular yaygın ve iki taraflıydı, bronkodilatöre kısmi yanıt vardı.", "teaching_point": "Pnömonide lokal raller ve yüksek ateş beklenir."},
                    {"text": "Spontan pnömotoraks", "is_correct": False, "scenario_update": "Solunum sesleri iki tarafta simetrikti, ani göğüs ağrısı yoktu.", "teaching_point": "Asimetrik ses azalması ve ani kötüleşmede pnömotoraks için grafi çekilir."},
                    {"text": "İlk basamak tedaviye yanıtsız ağır akut astım atağı", "is_correct": True, "explanation": "Tek kelimeyle konuşma, SpO2 %89, PEF %32, bir saatlik tedaviye rağmen süren bulgular ve normal pCO2 ilk basamağa yanıtsız ağır akut astım atağını gösterir.", "new_finding": "Tanı: Ağır akut astım atağı (ilk basamak tedaviye yanıtsız)."}
                ]
            },
            {
                "stage_title": "İleri Tedavi ve Yatış",
                "question": "Bu çocukta bir sonraki tedavi adımı ve yatış planı ne olmalıdır?",
                "options": [
                    {
                        "text": "Nebüllere ara verip iki saat sonra yeniden değerlendirmek ve düzelmezse aminofilin infüzyonu başlamak",
                        "is_correct": False,
                        "scenario_update": "Ara verilen sürede çocuk yoruldu ve pCO2 58 mmHg'ye yükseldi.",
                        "teaching_point": "Yanıtsız ağır atakta tedaviye ara verilmez; ilk ileri tedavi seçeneği magnezyum sülfattır."
                    },
                    {
                        "text": "Mevcut tedaviyle kısa sürede iyileşeceğini düşünüp oral prednizolon ve inhaler reçetesiyle aynı gün eve göndermek",
                        "is_correct": False,
                        "scenario_update": "Eve gönderilen çocuk iki saat sonra siyanoz ve bilinç bulanıklığıyla getirildi.",
                        "teaching_point": "Oksijen ihtiyacı süren ağır atakta taburculuk yapılmaz."
                    },
                    {
                        "text": "Yorulmaya başladığı için hemen entübe etmek ve mekanik ventilasyona alarak yoğun bakıma transfer etmek",
                        "is_correct": False,
                        "scenario_update": "Erken entübasyon sonrası barotravma ve hipotansiyon gelişti.",
                        "teaching_point": "Entübasyon yüksek riskli bir işlemdir; bilinç bozukluğu ve tedaviye yanıtsız solunum yetmezliğinde düşünülür."
                    },
                    {
                        "text": "İV magnezyum sülfat 50 mg/kg'ı 20 dakikada vermek, salbutamole devam edip monitörlü yatağa yatırmak",
                        "is_correct": True,
                        "explanation": "Magnezyum düz kas gevşemesi sağlar ve ilk basamağa yanıtsız ağır atakta etkilidir. Hipotansiyon açısından kan basıncı izlenir.",
                        "new_finding": "Magnezyum sülfat 1.8 g İV verildi. Bir saat sonra SS 28/dk, SpO2 %95 (2 L/dk oksijenle), cümleler kurabiliyor. Servise yatırıldı; üçüncü gün taburcu edildi ve kontrol tedavisi yeniden başlandı."
                    }
                ]
            }
        ]
    },
    {
        "id": "S74",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "5 Haftalık (3.9 kg)",
        "gender": "Kız",
        "complaint": "Burun akıntısı ve öksürük sonrası bugün evde iki kez nefesinin durup yüzünün morarması",
        "history": "Annesi anlatıyor: 'Üç gündür burnu akıyor, ablası kreşten hasta geldi. Bugün emerken iki kez nefesi durdu, dudakları morardı, sırtına vurunca düzeldi. Biberonun yarısını bile bitiremiyor.' 35. haftada doğmuş, 4 gün yenidoğan servisinde kalmış. Ateşi 37.6°C olmuş. Öksürük nöbetleri, öksürük sonrası kusma veya öksürük sonunda derin iç çekiş yok. Aşıları yaşına göre tam (yalnızca doğumda hepatit B).",
        "final_diagnosis": "Apne ile Seyreden Ağır Akut Bronşiolit (Prematüre, Genç Süt Çocuğu)",
        "disposition": "Yüksek Akımlı Nazal Kanül, Nazogastrik Beslenme ve Apne Monitörizasyonuyla Pediatri Yoğun Bakım veya Yüksek Bağımlılık Ünitesine Yatış",
        "case_pearl": "Prematüre doğmuş ve 2 aydan küçük süt çocuklarında viral alt solunum yolu enfeksiyonu hışıltı veya raller belirginleşmeden apneyle başlayabilir. Apne, SpO2'nin sürekli %90 altında olması, belirgin solunum işi ve beslenmenin yarıdan aza inmesi yatış ölçütleridir. Tedavi destekleyicidir: oksijen, gerekirse yüksek akımlı nazal kanül (2 L/kg/dk), nazogastrik veya İV sıvı ve apne monitörü. Bronkodilatör, adrenalin, kortikosteroid ve antibiyotik rutin değildir. Öksürük paroksizmi, öksürük sonrası kusma ve belirgin lenfositoz boğmacayı düşündürür.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Stabilizasyon",
                "question": "Evde nefes durması öyküsü olan 5 haftalık bu bebekte ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Bebeği bekleme salonunda annesinin kucağında izlemek ve yeni bir nefes durması olursa sarı alana almak",
                        "is_correct": False,
                        "scenario_update": "Bekleme salonunda bebek yeniden morardı; fark edilmesi gecikti.",
                        "teaching_point": "Apne öyküsü olan genç süt çocuğu hemen monitörize edilmelidir."
                    },
                    {
                        "text": "Sürekli kardiyorespiratuvar monitör ve pulse oksimetreye bağlamak, burnunu aspire edip solunum işini değerlendirmek ve oksijen başlamak",
                        "is_correct": True,
                        "explanation": "Apnenin tekrarını yakalamak için sürekli monitör gerekir. Genç bebekler burundan soluduğundan burun aspirasyonu solunum işini belirgin azaltır.",
                        "new_finding": "Ateş 37.7°C, KTA 172/dk, SS 68/dk, SpO2 %87 (oda havası), KDZ 3 sn. Burun aspirasyonu sonrası belirgin subkostal ve interkostal çekilme, burun kanadı solunumu, başını sallayarak soluma. Dinlemekle iki tarafta yaygın ince raller ve hafif hışıltı. Gözlemde 18 saniyelik bir apne ve SpO2'nin %78'e düşmesi, uyarıyla düzeliyor. Fontanel normal, mukozalar hafif kuru."
                    },
                    {
                        "text": "Hışıltı duyulduğu için monitörize etmeden hemen salbutamol nebül vermek ve yanıt yoksa ardından adrenalin nebülü eklemek",
                        "is_correct": False,
                        "scenario_update": "Nebül sonrası kalp hızı 205/dk'ya çıktı; solunum işinde değişiklik olmadı.",
                        "teaching_point": "Bu yaş grubunda viral alt solunum tablosunda bronkodilatör ve adrenalin rutin önerilmez."
                    },
                    {
                        "text": "Ağzından biberonla mama vermeyi denemek ve ne kadar içebildiğini görmek için bir saat beklemek",
                        "is_correct": False,
                        "scenario_update": "Beslenme sırasında bebek öksürüp mamayı aspire etti ve SpO2 %80'e düştü.",
                        "teaching_point": "Ağır takipneik bebekte ağızdan beslenme aspirasyon riski taşır."
                    }
                ]
            },
            {
                "stage_title": "Solunum Desteği Kararı",
                "question": "Oksijenle SpO2 %91, solunum işi belirgin ve apneleri olan bu bebekte hangi destek uygundur?",
                "options": [
                    {
                        "text": "Yüksek akımlı nazal kanülü 2 L/kg/dk ile başlatmak, oral beslenmeyi kesip nazogastrik veya İV sıvı vermek",
                        "is_correct": True,
                        "explanation": "Yüksek akımlı nazal kanül solunum işini azaltır ve hafif pozitif basınç sağlar. Nazogastrik beslenme veya İV sıvı aspirasyonu önler ve hidrasyonu korur.",
                        "new_finding": "Yüksek akım 8 L/dk, FiO2 %40 ile başlandı. Bir saat sonra SS 52/dk, SpO2 %95, çekilmeler azaldı. Kılcal kan gazı: pH 7.31, pCO2 54 mmHg. Nazogastrik sondadan beslenme başlandı. Yeni apne olmadı."
                    },
                    {
                        "text": "Apne öyküsü nedeniyle hemen entübe edip mekanik ventilasyona almak ve sedasyon başlamak",
                        "is_correct": False,
                        "scenario_update": "Entübasyon sırasında bradikardi gelişti; daha az invaziv destek denenmemişti.",
                        "teaching_point": "Entübasyon, noninvaziv desteğe rağmen tekrarlayan apne veya solunum yetmezliğinde gerekir."
                    },
                    {
                        "text": "Nazal kanülden 0.5 L/dk düşük akım oksijen verip bebeği ağızdan beslemeye devam ederek serviste izlemek",
                        "is_correct": False,
                        "scenario_update": "Düşük akım solunum işini azaltmadı ve beslenme sırasında yeni apne gelişti.",
                        "teaching_point": "Belirgin solunum işi ve apnesi olan bebekte daha güçlü destek ve monitörize ortam gerekir."
                    },
                    {
                        "text": "Sistemik kortikosteroid ve nebülize %3 hipertonik salin ile tedaviyi güçlendirip bebeği acil gözlem odasında yakından izlemek",
                        "is_correct": False,
                        "scenario_update": "Tedavi solunum işini azaltmadı; hipertonik salin öksürüğü artırdı.",
                        "teaching_point": "Kortikosteroid etkisizdir; hipertonik salinin acilde rutin yeri yoktur."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu bebekteki tablonun en olası tanısı nedir?",
                "options": [
                    {"text": "Boğmaca (pertussis)", "is_correct": False, "scenario_update": "Öksürük paroksizmi ve öksürük sonrası kusma yoktu, yaygın raller vardı.", "teaching_point": "Boğmacada öksürük paroksizmleri, öksürük sonrası apne-kusma ve belirgin lenfositoz görülür; akciğer muayenesi çoğu zaman temizdir."},
                    {"text": "Apneli ağır akut bronşiolit", "is_correct": True, "explanation": "Prematüre doğmuş 5 haftalık bebekte viral nezleyi izleyen takipne, yaygın raller ve hışıltı, hipoksemi, apne ve beslenme yetersizliği apneli ağır akut bronşioliti gösterir.", "new_finding": "Tanı: Apne ile seyreden ağır akut bronşiolit."},
                    {"text": "Geç başlangıçlı neonatal sepsis", "is_correct": False, "scenario_update": "Belirgin viral alt solunum yolu bulguları ve hasta bir kardeş vardı.", "teaching_point": "Sepsis kuşkusunda kültür alınır; burada solunum bulguları ön plandadır."},
                    {"text": "Gastroözofageal reflüye bağlı kısa süren açıklanamayan olay", "is_correct": False, "scenario_update": "Olaylar solunum yolu enfeksiyonu ve belirgin solunum sıkıntısı zemininde gelişti.", "teaching_point": "Tanı, iyi görünen ve muayenesi normal bebekte konur."}
                ]
            },
            {
                "stage_title": "Yatış Yeri ve İzlem",
                "question": "Bu bebek için en uygun yatış planı hangisidir?",
                "options": [
                    {
                        "text": "Durumu düzeldiği için yüksek akımı kesip 6 saat gözlem sonrası ağızdan beslenme önerisiyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Hastalığın en ağır dönemi henüz gelmemişti; bebek gece yeniden apneyle getirildi.",
                        "teaching_point": "Bu hastalık 3-5. günde zirve yapar; apneli bebekte taburculuk erkendir."
                    },
                    {
                        "text": "Bakteriyel süperenfeksiyon riski nedeniyle ampisilin ve gentamisin başlayıp genel pediatri servisine yatırmak",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik gereksizdi; monitörsüz serviste gece bir apne geç fark edildi.",
                        "teaching_point": "Rutin antibiyotik gerekmez; apneli bebek sürekli monitörün olduğu bir ünitede izlenmelidir."
                    },
                    {
                        "text": "Yüksek akım, nazogastrik beslenme ve sürekli apne monitörüyle yoğun bakım veya yüksek bağımlılık ünitesine yatırmak; temas izolasyonu uygulamak",
                        "is_correct": True,
                        "explanation": "Apneli ve yüksek akım gereken bebek yakın izlem gerektirir. Kötüleşirse CPAP veya entübasyon hızla yapılabilmelidir. Temas izolasyonu servis içi bulaşı önler.",
                        "new_finding": "Bebek yüksek bağımlılık ünitesine yatırıldı. Dördüncü gün yüksek akım kesildi, altıncı gün tam oral beslenmeye geçti ve sekizinci gün taburcu edildi."
                    },
                    {
                        "text": "Kafeinin apneyi önleyeceğini düşünerek yükleme dozu verip bebeği oral beslenmeyle monitörsüz serviste izlemek",
                        "is_correct": False,
                        "scenario_update": "Kafeine rağmen bebekte beslenme sırasında yeni apne gelişti ve geç fark edildi.",
                        "teaching_point": "Monitör ve solunum desteği bu tabloda vazgeçilmezdir; kafein rutin önerilmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "S75",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "10 Aylık (8.6 kg)",
        "gender": "Erkek",
        "complaint": "Bir haftadır yüksek ateş, üç gündür tüm vücutta döküntü ve bugün hızlı nefes alma",
        "history": "Annesi anlatıyor: 'Bir hafta önce ateşi çıktı, burnu aktı, gözleri kızardı, çok öksürdü. Dört gün sonra kulak arkasından başlayan kırmızı döküntü yüzüne ve tüm vücuduna yayıldı. Döküntü kahverengiye dönüyor ama ateşi düşmedi, bugün hızlı nefes almaya başladı, emmiyor.' Mahallede birkaç çocukta benzer hastalık olmuş. Bebek 12. ay aşılarını henüz olmamış. Ağabeyi 4 yaşında, aile aşı yaptırmayı reddetmiş, o da iki hafta önce benzer bir hastalık geçirmiş.",
        "final_diagnosis": "Kızamık (Rubeola) Pnömonisi ve Hipoksemi",
        "disposition": "Hava Yolu İzolasyonunda Oksijen, A Vitamini, Ampirik Antibiyotik ve Bildirimle Pediatri Servisine Yatış",
        "case_pearl": "Ateş, öksürük, burun akıntısı ve konjonktiviti izleyen, kulak arkasından başlayıp aşağı yayılan makülopapüler döküntü bu hastalığa özgüdür. En sık ölüm nedeni pnömonidir; viral veya ikincil bakteriyel olabilir. Döküntüden sonra ateşin sürmesi komplikasyonu düşündürür. Hasta hava yolu (solunum) izolasyonuna alınır; döküntü başlangıcından sonraki 4 gün bulaştırıcıdır. A vitamini (6-11 ay 100.000 IU, ≥12 ay 200.000 IU, iki gün) ağır hastalık ve ölüm riskini azaltır. Olgu bildirimi zorunludur, temaslılara aşı veya immünglobulin profilaksisi uygulanır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Enfeksiyon Kontrolü",
                "question": "Ateşli, döküntülü ve hızlı soluyan bu bebeğe ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Bebeği diğer hastalarla aynı sarı alan bölmesinde, standart önlemlerle değerlendirmek ve tanı netleşince izolasyonu düşünmek",
                        "is_correct": False,
                        "scenario_update": "Bekleme alanındaki 4 aylık iki bebek temaslı sayıldı ve profilaksi gerekti.",
                        "teaching_point": "Ateş ve makülopapüler döküntüyle gelen aşısız çocuk hemen solunum izolasyonuna alınmalıdır."
                    },
                    {
                        "text": "Ağzından bol sıvı içirmek, ateş için soğuk suyla banyo yaptırmak ve ateş düştükten sonra solunumunu ve SpO2'sini yeniden değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Soğuk banyo bebeği titretti ve oksijen ihtiyacını artırdı; değerlendirme gecikti.",
                        "teaching_point": "Solunum sıkıntısı olan bebekte önce oksijenlenme değerlendirilir; soğuk su banyosu önerilmez."
                    },
                    {
                        "text": "Bebeği hemen tek kişilik odada solunum izolasyonuna almak, personele N95 maske taktırmak; vital bulgular, SpO2 ve hidrasyonu değerlendirmek",
                        "is_correct": True,
                        "explanation": "Bu tablo hava yoluyla bulaşan bir enfeksiyonu düşündürür ve bekleme alanındaki aşısız bebekler için risklidir. Solunum sıkıntısı ve hidrasyon durumu tedavi önceliklerini belirler.",
                        "new_finding": "Ateş 39.4°C, KTA 168/dk, SS 62/dk, SpO2 %89 (oda havası), KDZ 3 sn. İnterkostal çekilme, burun kanadı solunumu. Yüz ve gövdede birleşme eğiliminde, kahverengiye dönen makülopapüler döküntü. Gözler kızarık, çapaklı. Dudaklar kuru, ağız içinde yaygın kızarıklık. Sağ akciğerde ince raller ve bronşiyal ses. Bilinç açık, irritabl."
                    },
                    {
                        "text": "Döküntüyü ilaç reaksiyonu kabul edip intravenöz antihistaminik ve kortikosteroid vermek, ardından ateşi izlemek",
                        "is_correct": False,
                        "scenario_update": "Kortikosteroid enfeksiyonu kötüleştirdi; döküntü değişmedi.",
                        "teaching_point": "Prodrom ve yayılım şekli enfeksiyöz bir döküntüyü gösterir; kortikosteroid viral enfeksiyonu ağırlaştırabilir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Oksijen başlanan bu bebekte hangi tetkikler en uygundur?",
                "options": [
                    {
                        "text": "Tetkik istemeden yalnızca oksijen ve ateş düşürücüyle izlemek; döküntü geçince tanının kendiliğinden netleşeceğini ve hastalığın geçeceğini beklemek",
                        "is_correct": False,
                        "scenario_update": "Tanı doğrulanmadığı için bildirim ve temaslı profilaksisi gecikti.",
                        "teaching_point": "Bildirimi zorunlu hastalıklarda laboratuvar doğrulaması ve erken bildirim gerekir."
                    },
                    {
                        "text": "Akciğer grafisi, tam kan sayımı, CRP ve elektrolitlerle birlikte serum özgül IgM ve virüs PCR'ı göndermek",
                        "is_correct": True,
                        "explanation": "Grafi akciğer tutulumunun yaygınlığını ve komplikasyonları gösterir. Serum IgM ve PCR tanıyı doğrular, bildirim ve temaslı yönetimi için gereklidir.",
                        "new_finding": "Akciğer grafisi: Sağ üst ve orta zonda yamalı konsolidasyon, iki tarafta peribronşiyal kalınlaşma, plevral sıvı yok. Lökosit 4.200/mm³ (lenfosit 900/mm³), CRP 68 mg/L, Na 132 mmol/L. Serum özgül IgM ve PCR sonucu bekleniyor."
                    },
                    {
                        "text": "Döküntünün nedenini anlamak için deri biyopsisi yapmak ve ateş nedeniyle lomber ponksiyon planlamak",
                        "is_correct": False,
                        "scenario_update": "Gereksiz girişimler bebeği yordu ve oksijen ihtiyacını artırdı.",
                        "teaching_point": "Tipik tabloda biyopsi gerekmez; bilinç değişikliği ya da nöbet olmadan lomber ponksiyon yapılmaz."
                    },
                    {
                        "text": "Toraks bilgisayarlı tomografisi ve ekokardiyografi istemek, sonuçlarına göre izolasyon kararı vermek",
                        "is_correct": False,
                        "scenario_update": "Tomografi yönetimi değiştirmedi; izolasyonsuz taşımalarda personel temaslı sayıldı.",
                        "teaching_point": "Tomografi rutin değildir; izolasyon kararı klinik şüpheyle hemen verilir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu bebekteki tablonun en olası tanısı nedir?",
                "options": [
                    {"text": "Kawasaki hastalığı", "is_correct": False, "scenario_update": "Öksürük, burun akıntısı, çapaklı konjonktivit ve kahverengiye dönen döküntü vardı; temaslı vakalar vardı.", "teaching_point": "Kawasaki'de konjonktivit çapaksızdır ve öksürük-nezle prodromu beklenmez."},
                    {"text": "Ekzantem süfit (roseola)", "is_correct": False, "scenario_update": "Döküntü ateş düşmeden çıkmıştı ve ateş sürüyordu.", "teaching_point": "Roseolada döküntü ateş düştükten sonra çıkar ve çocuk iyi görünür."},
                    {"text": "Kızamık pnömonisi", "is_correct": True, "explanation": "Aşısız bebekte öksürük, burun akıntısı ve konjonktivit prodromunu izleyen, kulak arkasından başlayıp yayılan ve kahverengiye dönen döküntü, salgın öyküsü, lenfopeni ve döküntüden sonra süren ateşle birlikte hipoksemik akciğer tutulumu kızamık pnömonisini gösterir.", "new_finding": "Tanı: Kızamık pnömonisi. İki gün sonra serum özgül IgM pozitif geldi."},
                    {"text": "İlaç reaksiyonu (DRESS)", "is_correct": False, "scenario_update": "Yeni başlanmış ilaç ve eozinofili yoktu.", "teaching_point": "DRESS ilaç başlangıcından 2-6 hafta sonra döküntü, eozinofili ve organ tutulumuyla gelir."}
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu bebek için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Oksijen ve sıvıyla iki gün A vitamini vermek, antibiyotik başlamak, hava yolu izolasyonunda yatırıp olguyu hemen bildirmek",
                        "is_correct": True,
                        "explanation": "A vitamini bu hastalıkta ölüm ve komplikasyon riskini azaltır. Döküntüden sonra süren ateş, CRP yüksekliği ve konsolidasyon ikincil bakteriyel pnömoniyi düşündürdüğünden antibiyotik eklenir. Bildirim temaslıların korunması içindir.",
                        "new_finding": "A vitamini, oksijen, İV ampisilin-sulbaktam başlandı, olgu halk sağlığına bildirildi. Temaslı bebeklere immünglobulin uygulandı. Beşinci gün oksijen kesildi, onuncu gün taburcu edildi."
                    },
                    {
                        "text": "Antiviral olarak oral asiklovir başlayıp oksijen ihtiyacı geçince standart serviste izolasyonsuz izlemek",
                        "is_correct": False,
                        "scenario_update": "Asiklovir etkisizdi; izolasyonsuz izlemde servisteki iki bebekte hastalık gelişti.",
                        "teaching_point": "Bu virüse karşı asiklovir etkili değildir ve izolasyon döküntüden sonraki 4 gün sürer."
                    },
                    {
                        "text": "Ateşi ve döküntüsü yatışacağı için oral parasetamol ve antihistaminikle evde izlemek, kardeşini ayrı odada tutmalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Hipoksemik bebek evde kötüleşti ve iki gün sonra solunum yetmezliğiyle getirildi.",
                        "teaching_point": "Hipoksemisi olan bebek mutlaka yatırılarak tedavi edilir."
                    },
                    {
                        "text": "Hastalığın seyrini hafifletmek için hemen KKK aşısı yapmak ve sistemik kortikosteroid başlayıp servise yatırmak",
                        "is_correct": False,
                        "scenario_update": "Hasta bebeğe aşı yapmak tedavi edici değildi; kortikosteroid ikincil enfeksiyonu ağırlaştırdı.",
                        "teaching_point": "Aşı hastalık başladıktan sonra tedavi edici değildir; temaslılarda ilk 72 saat içinde koruyucudur."
                    }
                ]
            }
        ]
    }
]
