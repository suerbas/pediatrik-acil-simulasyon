# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - S76-S80 (Nörolojik, Enfeksiyon ve Metabolik Aciller)
"""

SPOILERS = {
    "S76": ["herpes", "hsv", "ensefalit"],
    "S77": ["septik şok", "ürosepsis"],
    "S78": ["hipoglisemi"],
    "S79": ["serebral ödem", "beyin ödemi"],
    "S80": ["d vitamini eksikliği", "raşitizm", "rikets", "hipokalsemi"],
}

CASES = [
    {
        "id": "S76",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "3 Yaşında (14 kg)",
        "gender": "Kız",
        "complaint": "Üç gündür ateş, dünden beri tuhaf davranışlar ve bugün sağ kolda başlayıp yayılan kasılma",
        "history": "Annesi anlatıyor: 'Üç gündür ateşi var, nezle sandık. Dün akşamdan beri bizi tanımıyormuş gibi bakıyor, anlamsız konuşuyor, sebepsiz ağlıyor. Bu sabah sağ kolu ve yüzünün sağ tarafı seğirmeye başladı, sonra tüm vücudu kasıldı, beş dakika sürdü.' Kusma bir kez olmuş. Döküntü yok. Kafa travması, ilaç veya zehirli madde erişimi yok. Aşıları tam. Daha önce nöbet geçirmemiş.",
        "final_diagnosis": "Herpes Simpleks Virüs (HSV-1) Ensefaliti",
        "disposition": "Yüksek Doz İV Asiklovir (21 Gün), Antiepileptik Tedavi ve Nörolojik İzlem İçin Çocuk Yoğun Bakım Yatışı",
        "case_pearl": "Ateş, davranış değişikliği, bilinç bulanıklığı ve fokal nöbet birlikteliği temporal lob tutulumlu viral ensefaliti düşündürür; en sık ve en ağır seyreden etken HSV-1'dir. Asiklovir (3 ay-12 yaş için 20 mg/kg/doz, 8 saatte bir) şüphe anında, görüntüleme veya lomber ponksiyon beklenmeden başlanır; gecikme ölüm ve sekel riskini artırır. Odak bulgu veya bilinç bozukluğunda lomber ponksiyondan önce görüntüleme yapılır. BOS'ta lenfositik pleositoz, eritrosit ve hafif protein artışı görülür; PCR ilk 72 saatte negatif olabilir. MR'da temporal lob tutulumu, EEG'de periyodik lateralize deşarjlar tipiktir. Böbrek toksisitesine karşı hidrasyon sağlanır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Stabilizasyon",
                "question": "Gelişinde uykulu ve sağ tarafı hafif güçsüz olan bu ateşli çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Ateş düşürücü verip ateşi düşünce bilincinin düzelip düzelmediğini görmek için iki saat gözlemlemek ve sonra karar vermek",
                        "is_correct": False,
                        "scenario_update": "Ateş düştü ama çocuk düzelmedi; bekleme sırasında yeni bir fokal nöbet geçirdi ve tedavi gecikti.",
                        "teaching_point": "Ateşle birlikte davranış değişikliği ve fokal nöbet merkezi sinir sistemi enfeksiyonunu düşündürür; beklenmez."
                    },
                    {
                        "text": "Hava yolu, oksijen ve kan şekerini kontrol etmek; GKS, pupil ve fokal nörolojik muayeneyle menenjit ve döküntü bulgularını değerlendirmek",
                        "is_correct": True,
                        "explanation": "Bilinç değişikliği olan ateşli çocukta önce hava yolu ve kan şekeri güvenceye alınır. Fokal bulgular ve bilinç düzeyi lomber ponksiyon öncesi görüntüleme gereksinimini belirler.",
                        "new_finding": "Ateş 39.2°C, KTA 148/dk, SS 28/dk, KB 102/64 mmHg, SpO2 %98. Kan şekeri 104 mg/dL. GKS 12 (G3 S4 M5). Pupiller izokorik. Sağ kol ve bacakta hafif güçsüzlük, sağda refleksler canlı. Ense sertliği şüpheli. Döküntü yok. Fundus muayenesi yapılamadı."
                    },
                    {
                        "text": "Ateşli nöbet geçirdiği için basit febril konvülziyon kabul edip ateş düşürücü ve ağızdan sıvıyla taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Eve gönderilen çocuk aynı gece tekrarlayan nöbetler ve koma ile getirildi.",
                        "teaching_point": "Fokal başlangıç, uzamış süre ve öncesinde davranış değişikliği basit febril nöbetle bağdaşmaz."
                    },
                    {
                        "text": "Bilinci bulanık olduğu için muayene etmeden hemen entübe edip sedasyon başlamak ve ardından yoğun bakıma aktarmak",
                        "is_correct": False,
                        "scenario_update": "Hava yolu yeterli olan çocuk entübe edildi; sedasyon nedeniyle nörolojik izlem yapılamadı.",
                        "teaching_point": "Entübasyon için GKS ≤8, hava yolunu koruyamama veya solunum yetmezliği gerekir."
                    }
                ]
            },
            {
                "stage_title": "Ampirik Tedavi ve Tetkik Sıralaması",
                "question": "Fokal nörolojik bulgusu olan bu çocukta tetkik ve tedavi sıralaması nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Önce lomber ponksiyon yapmak, BOS sonuçları ve PCR gelene kadar antibiyotik ve antiviral tedaviyi ertelemek",
                        "is_correct": False,
                        "scenario_update": "Fokal bulgulu çocukta görüntülemesiz ponksiyon riskliydi; PCR sonucu 48 saat sürdü ve tedavi gecikti.",
                        "teaching_point": "Fokal bulgu varsa ponksiyon öncesi görüntüleme gerekir; ampirik tedavi tetkik için ertelenmez."
                    },
                    {
                        "text": "Kan kültürü alıp hemen İV seftriakson ve asiklovir başlamak; görüntüleme sonrası güvenliyse lomber ponksiyon yapmak",
                        "is_correct": True,
                        "explanation": "Ampirik tedavi tetkikler için geciktirilmez. Fokal bulgu nedeniyle ponksiyondan önce görüntüleme yapılır; BOS PCR tedavi başladıktan sonra da pozitif bulunur.",
                        "new_finding": "Seftriakson ve asiklovir 20 mg/kg başlandı. Kontrastsız BT'de kitle veya kanama yok, sol temporal bölgede silik hipodansite. BOS: lökosit 85/mm³ (%90 lenfosit), eritrosit 240/mm³, protein 78 mg/dL, glukoz 58 mg/dL (kan 104). Gram boyamada bakteri yok."
                    },
                    {
                        "text": "Beyin MR ve EEG yapılmadan tedaviye başlanmamasını, iki tetkikin de acilde aynı gün tamamlanmasını beklemek",
                        "is_correct": False,
                        "scenario_update": "MR ve EEG için saatlerce beklendi; çocuk yeniden nöbet geçirdi ve bilinci kötüleşti.",
                        "teaching_point": "MR ve EEG tanıyı destekler ama ampirik tedaviyi geciktirmemelidir."
                    },
                    {
                        "text": "Yalnızca İV seftriakson başlamak; antiviral tedaviyi BOS'ta virüs saptanırsa eklemek ve ponksiyonu hemen yapmak",
                        "is_correct": False,
                        "scenario_update": "Antiviral iki gün gecikti; çocukta kalıcı konuşma bozukluğu gelişti.",
                        "teaching_point": "Ateş, ensefalopati ve fokal bulguda antiviral tedavi şüphe anında başlanmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik ve BOS bulgularına göre en olası tanınız nedir?",
                "options": [
                    {"text": "Akut bakteriyel menenjit", "is_correct": False, "scenario_update": "BOS'ta lenfosit hakimiyeti vardı, glukoz normaldi ve bakteri görülmedi.", "teaching_point": "Bakteriyel menenjitte nötrofil hakimiyeti, düşük glukoz ve yüksek protein beklenir."},
                    {"text": "Akut dissemine ensefalomiyelit (ADEM)", "is_correct": False, "scenario_update": "Yakın zamanda geçirilmiş enfeksiyon veya aşı sonrası latent dönem yoktu, tutulum tek taraflı ve temporaldi.", "teaching_point": "ADEM enfeksiyondan 1-3 hafta sonra çok odaklı beyaz cevher tutulumuyla gelir."},
                    {"text": "Herpes simpleks ensefaliti", "is_correct": True, "explanation": "Ateş, davranış değişikliği, fokal nöbet ve hemiparezi; lenfositik pleositoz, BOS'ta eritrosit ve temporal hipodansite herpes simpleks ensefalitini gösterir.", "new_finding": "Tanı: HSV-1 ensefaliti. BOS HSV-1 PCR pozitif geldi; MR'da sol temporal lob ve insulada T2 hiperintensite."},
                    {"text": "Tümöre bağlı fokal nöbet", "is_correct": False, "scenario_update": "Akut ateşli tablo ve inflamatuvar BOS vardı, BT'de kitle yoktu.", "teaching_point": "Tümörde haftalar süren baş ağrısı, kusma ve ilerleyici nörolojik bulgu beklenir."}
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış Planı",
                "question": "Bu çocuğun tedavisi nasıl sürdürülmelidir?",
                "options": [
                    {
                        "text": "Durumu düzelirse asikloviri yedinci günde ağızdan valasiklovire geçip servise almak ve taburculuğu planlamak",
                        "is_correct": False,
                        "scenario_update": "Kısa tedavi sonrası iki hafta içinde nüks gelişti ve çocuk yeniden yatırıldı.",
                        "teaching_point": "Bu enfeksiyonda İV tedavi 21 gün sürer; kısa veya oral tedavi nüks riskini artırır."
                    },
                    {
                        "text": "Asikloviri 21 gün İV sürdürmek, hidrasyonla böbrek fonksiyonunu izlemek, nöbet tedavisi verip yoğun bakımda izlemek",
                        "is_correct": True,
                        "explanation": "Tam süreli İV tedavi nüksü ve sekel riskini azaltır. Asiklovir kristalüriye bağlı böbrek hasarı yapabileceğinden hidrasyon ve kreatinin izlemi gerekir.",
                        "new_finding": "Levetirasetam başlandı. Asiklovir 21 gün verildi, kreatinin normal seyretti. Tedavi sonunda BOS PCR negatifti. Hafif konuşma güçlüğüyle taburcu edildi, rehabilitasyon planlandı."
                    },
                    {
                        "text": "Beyindeki inflamasyonu azaltmak için yüksek doz İV deksametazon eklemek ve antivirali BOS PCR negatifleşince kesmek",
                        "is_correct": False,
                        "scenario_update": "Kortikosteroidin yararı gösterilmedi; PCR erken negatifleşince tedavi kısa kesildi ve nüks gelişti.",
                        "teaching_point": "Kortikosteroid rutin önerilmez; tedavi süresi PCR'a değil klinik protokole göre belirlenir."
                    },
                    {
                        "text": "Nöbet geçtiğine göre antiepileptik vermeden asiklovir ile genel pediatri servisinde rutin aralıklarla izlemek",
                        "is_correct": False,
                        "scenario_update": "Serviste fark edilmeyen nonkonvülzif nöbetler bilinç bulanıklığını uzattı.",
                        "teaching_point": "Bu hastalarda nöbetler sıktır; antiepileptik tedavi ve yakın nörolojik izlem gerekir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S77",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "10 Yaşında (32 kg)",
        "gender": "Kız",
        "complaint": "İki gündür yüksek titremeli ateş, sol böğür ağrısı, kusma ve bugün aşırı halsizlik ve ellerinin buz gibi olması",
        "history": "Annesi anlatıyor: 'İki gündür 40'a çıkan titremeli ateşi var, sol yanı ağrıyor, iki kez kustu. Bu sabah kalkamadı, çok soluk, elleri ayakları buz gibi, sabahtan beri tuvalete gitmedi.' Bir yıl önce sık sık sol yan ağrısı olmuş, 'böbrekte genişleme var, takip edelim' denmiş ama kontrole gidilmemiş. Bilinen başka hastalığı yok. Aşıları tam.",
        "final_diagnosis": "Üreteropelvik Bileşke Darlığı Zemininde Piyonefrozdan Kaynaklanan Septik Şok (Ürosepsis)",
        "disposition": "Sıvı Resüsitasyonu, İnotrop/Vazopresör Desteği, Geniş Spektrumlu Antibiyotik ve Acil Perkütan Nefrostomi ile Çocuk Yoğun Bakım Yatışı",
        "case_pearl": "Septik şok tanısında hipotansiyon geç bulgudur; taşikardi, uzamış kapiller dolum, soğuk ekstremiteler, oligüri ve bilinç değişikliği daha erken bulgulardır. İlk saatte iki damar yolu (veya intraosseöz), kültürler, laktat ve bir saat içinde geniş spektrumlu antibiyotik verilir. Sıvı 10-20 mL/kg dengeli kristaloid bolusları halinde, her bolus sonrası karaciğer ve akciğer muayenesiyle yeniden değerlendirilerek verilir. 40-60 mL/kg'a yanıtsız şokta adrenalin veya noradrenalin periferden başlanabilir. Tıkalı enfekte böbrek gibi bir odak varsa kaynak kontrolü (drenaj) antibiyotik kadar önemlidir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Resüsitasyon",
                "question": "Ateşli, soluk ve soğuk ekstremiteli bu çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Oksijen, monitör ve iki damar yolu; kültür ve laktat alıp 10-20 mL/kg dengeli kristaloid bolusu vermek ve yeniden değerlendirmek",
                        "is_correct": True,
                        "explanation": "Perfüzyon bozukluğu olan ateşli çocukta resüsitasyon hemen başlar. Bolusların küçük porsiyonlarla verilip her seferinde sıvı yüklenmesi bulgularının aranması güvenliği artırır.",
                        "new_finding": "Ateş 39.6°C, KTA 164/dk, SS 32/dk, KB 78/42 mmHg, SpO2 %95, KDZ 5 sn, el ve ayaklar soğuk ve alacalı, nabızlar zayıf. Uykulu, uyarana yanıt veriyor. Sol kostovertebral açı hassas. Laktat 5.8 mmol/L. Kan şekeri 92 mg/dL. Mesane kateterinden 15 mL koyu idrar."
                    },
                    {
                        "text": "Ateşini düşürmek için önce parasetamol verip bir saat sonra perfüzyonu ve kan basıncını yeniden değerlendirmek, düzelmezse sıvıya başlamak",
                        "is_correct": False,
                        "scenario_update": "Bir saat içinde kan basıncı 64/34 mmHg'ye düştü, bilinç kötüleşti.",
                        "teaching_point": "Perfüzyon bozukluğu ateş düşmesiyle düzelmez; resüsitasyon geciktirilmemelidir."
                    },
                    {
                        "text": "Damar yolu açılana kadar beklemek, tek seferde 60 mL/kg serum fizyolojiği hızlıca verip sonra yeniden değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Hızlı ve yüksek hacimli sıvı sonrası akciğerlerde raller ve hepatomegali gelişti, SpO2 %88'e düştü.",
                        "teaching_point": "Sıvılar küçük boluslarla, her biri sonrası yüklenme bulguları aranarak verilir; damar yolu gecikirse intraosseöz yol kullanılır."
                    },
                    {
                        "text": "Antibiyotiği kültür sonuçlarına göre seçmek için ilk değerlendirmede vermemek ve tetkik sonuçlarını beklemek",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik dört saat gecikti; çocuk çoklu organ yetmezliğine ilerledi.",
                        "teaching_point": "Şoktaki çocukta antibiyotik ilk saat içinde, kültür alınır alınmaz verilmelidir."
                    }
                ]
            },
            {
                "stage_title": "Sıvıya Yanıtsız Dolaşım Bozukluğu",
                "question": "Seftriakson verildi. Toplam 40 mL/kg sıvıya rağmen KB 76/40 mmHg, KDZ 5 sn ve ekstremiteler soğuk. Sıradaki adım nedir?",
                "options": [
                    {
                        "text": "Kan basıncı normale dönene kadar 20 mL/kg serum fizyolojik boluslarını toplam 100 mL/kg'a ulaşana dek hızla vermeyi sürdürmek",
                        "is_correct": False,
                        "scenario_update": "Akciğer ödemi gelişti; SpO2 %85'e düştü ve çocuk entübe edilmek zorunda kalındı.",
                        "teaching_point": "Sıvıya yanıtsız şokta sıvıya ısrar edilmez; vazoaktif tedaviye geçilir."
                    },
                    {
                        "text": "Periferik damar yolundan adrenalin infüzyonu başlamak, yanıta göre doz artırmak ve yoğun bakımla merkezi kateter planlamak",
                        "is_correct": True,
                        "explanation": "Soğuk şok tablosunda adrenalin hem kalp debisini hem kan basıncını artırır. Merkezi kateter beklenirken periferden başlamak gecikmeyi önler.",
                        "new_finding": "Adrenalin 0.1 mcg/kg/dk başlandı, 0.2'ye çıkıldı. Otuz dakika sonra KB 94/56 mmHg, KTA 142/dk, KDZ 3 sn. Lökosit 24.800/mm³, CRP 286 mg/L, prokalsitonin 42 ng/mL, kreatinin 1.4 mg/dL. İdrarda bol lökosit ve nitrit pozitif."
                    },
                    {
                        "text": "Dopaminin böbrek kan akımını koruyacağını düşünüp düşük doz dopamin infüzyonunu tek başına başlatmak",
                        "is_correct": False,
                        "scenario_update": "Düşük doz dopamin şoku düzeltmedi ve taşikardi arttı.",
                        "teaching_point": "Böbrek koruyucu düşük doz dopamin kavramı geçerli değildir; ilk tercih adrenalin veya noradrenalindir."
                    },
                    {
                        "text": "Hemen hidrokortizon başlayıp vazoaktif tedaviyi steroide yanıt alınamazsa düşünmek üzere bir saat beklemek",
                        "is_correct": False,
                        "scenario_update": "Steroid tek başına dolaşımı düzeltmedi; hipoperfüzyon bir saat daha sürdü.",
                        "teaching_point": "Hidrokortizon vazoaktife dirençli şokta veya adrenal yetmezlik riskinde eklenir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik ve laboratuvar bulgularına göre en olası tanınız nedir?",
                "options": [
                    {"text": "Hipovolemik şok (gastroenterit)", "is_correct": False, "scenario_update": "İshal yoktu, sıvı kaybı sınırlıydı ve belirgin enfeksiyon odağı vardı.", "teaching_point": "Hipovolemik şok sıvı replasmanına hızlı yanıt verir."},
                    {"text": "İdrar kaynaklı septik şok", "is_correct": True, "explanation": "Titremeli ateş, böğür ağrısı, piyüri ve nitrit pozitifliği ile birlikte sıvıya yanıtsız, vazoaktif ilaç gerektiren dolaşım bozukluğu idrar kaynaklı septik şoku gösterir.", "new_finding": "Tanı: Ürosepsis ve septik şok."},
                    {"text": "Toksik şok sendromu", "is_correct": False, "scenario_update": "Yaygın eritrodermi, tampon veya yara odağı yoktu, net bir idrar odağı vardı.", "teaching_point": "Toksik şokta eritrodermi, mukozal hiperemi ve sonradan soyulma görülür."},
                    {"text": "Akut miyokardit ve kardiyojenik şok", "is_correct": False, "scenario_update": "Ateş ve odaklı enfeksiyon bulguları belirgindi; hepatomegali ve galo ritmi yoktu.", "teaching_point": "Kardiyojenik şokta sıvı ile kötüleşme, hepatomegali ve galo ritmi tipiktir."}
                ]
            },
            {
                "stage_title": "Kaynak Kontrolü ve Yatış",
                "question": "Yatak başı ultrasonografide sol böbrekte ileri pelvikaliektazi ve toplayıcı sistemde ekojen içerik görüldü. En uygun plan hangisidir?",
                "options": [
                    {
                        "text": "Antibiyotiğin tek başına yeterli olacağını düşünüp drenajı iki hafta sonraki elektif ameliyata bırakmak",
                        "is_correct": False,
                        "scenario_update": "Tıkalı ve enfekte böbrekte antibiyotik yeterli olmadı; şok derinleşti.",
                        "teaching_point": "Tıkanıklığa bağlı enfeksiyonda acil drenaj gerekir."
                    },
                    {
                        "text": "Durumu stabil olduğunda kontrastlı tomografi ve sintigrafi çektirip sonuçlara göre çocuk ürolojisine ayaktan danışmak",
                        "is_correct": False,
                        "scenario_update": "Tetkik beklenirken drenaj gecikti ve böbrek fonksiyonu kötüleşti.",
                        "teaching_point": "Ultrasonografi drenaj kararı için yeterlidir; ileri görüntüleme sonra yapılır."
                    },
                    {
                        "text": "Seftriaksonu sürdürmek, girişimsel radyoloji veya çocuk ürolojisiyle acil perkütan nefrostomi yapıp yoğun bakıma yatırmak",
                        "is_correct": True,
                        "explanation": "Enfekte ve tıkalı toplayıcı sistemin drenajı septik kaynağı ortadan kaldırır. Hasta vazoaktif destek gerektirdiği için yoğun bakımda izlenir.",
                        "new_finding": "Acil perkütan nefrostomiyle pürülan idrar boşaltıldı; kültürde E. coli üredi. Yirmi dört saatte adrenalin kesildi. Altı hafta sonra üreteropelvik bileşke darlığı için piyeloplasti yapıldı."
                    },
                    {
                        "text": "Mesaneye konan kateterin üst idrar yolunu da boşaltacağını düşünüp yalnızca kateter ve antibiyotikle servise yatırmak",
                        "is_correct": False,
                        "scenario_update": "Mesane kateteri tıkalı böbreği boşaltmadı; çocuk yoğun bakıma geç aktarıldı.",
                        "teaching_point": "Üreteropelvik düzeyde tıkanıklıkta mesane kateteri böbreği drene etmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "S78",
        "category": "💊 Toksikoloji & Metabolik / Endokrin Aciller",
        "age": "12 Yaşında (40 kg)",
        "gender": "Erkek",
        "complaint": "Futbol maçından sonra terleme, titreme, anlamsız konuşma ve uykuya meyil",
        "history": "Antrenörü getirdi, annesi telefonla ulaşıldı. Antrenör anlatıyor: 'İki saatlik turnuvadan sonra soyunma odasında terliyor, titriyordu. Saçma sapan konuşmaya başladı, sonra uyuklamaya başladı.' Annesi: 'İki yıldır tip 1 diyabeti var, insülin kalemleri kullanıyor. Sabah her zamanki dozunu yaptı ama geç kaldığı için kahvaltısını yarım bıraktı. Maç sırasında bir şey yemedi.' Kafa travması yok. Alkol veya madde kullanımı bilinmiyor.",
        "final_diagnosis": "Tip 1 Diyabetli Çocukta Egzersiz ve Yetersiz Beslenmeyle Tetiklenen Ağır Hipoglisemi",
        "disposition": "İV Glukoz ile Düzelme, Uzun Etkili Karbonhidrat ve Gözlem Sonrası Glukagon Reçetesi ve Diyabet Eğitimiyle Sarı Alandan Taburculuk",
        "case_pearl": "Bilinen diyabetli çocukta terleme, titreme, davranış değişikliği ve bilinç bulanıklığı düşük kan şekerinin klasik bulgularıdır; her bilinç değişikliğinde kan şekeri ilk ölçülendir. Yutabilen çocukta 0.3 g/kg hızlı emilen karbonhidrat verilir. Bilinci bozuk veya yutamayan çocukta İV %10 dekstroz 2 mL/kg (0.2 g/kg) verilir; damar yolu yoksa glukagon (25 kg altında 0.5 mg, üstünde 1 mg İM) veya intranazal glukagon kullanılır. Hipertonik %50 dekstroz damar hasarı ve rebound nedeniyle çocuklarda önerilmez. Düzelmeden sonra uzun etkili karbonhidrat verilir, 15 dakikada bir kan şekeri ölçülür. Egzersiz geç başlangıçlı düşük şekere yol açabileceği için gece izlemi önerilir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme",
                "question": "Bilinci bulanık olan bu çocuğa ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Madde kullanımı şüphesiyle idrarda toksikoloji taraması istemek ve sonuç gelene kadar gözlem odasında yatırmak",
                        "is_correct": False,
                        "scenario_update": "Bekleme sırasında çocuğun bilinci daha da kötüleşti ve nöbet geçirdi.",
                        "teaching_point": "Bilinç bulanıklığında kan şekeri hemen ölçülmeli ve geri döndürülebilir nedenler önce düzeltilmelidir."
                    },
                    {
                        "text": "Diyabetik ketoasidoz kabul edip kan şekerine bakmadan İV insülin infüzyonu ve serum fizyolojik bolusu başlamak",
                        "is_correct": False,
                        "scenario_update": "İnsülin başlanmak üzereyken ölçülen şeker çok düşük çıktı; ciddi bir hata son anda önlendi.",
                        "teaching_point": "Diyabetli çocukta bilinç değişikliğinin nedeni şeker ölçülmeden bilinemez."
                    },
                    {
                        "text": "Hava yolunu ve solunumu değerlendirip hemen kapiller kan şekerini ölçmek, damar yolu açmak ve kan şekeri için venöz örnek almak",
                        "is_correct": True,
                        "explanation": "Bilinç değişikliğinde ABC'den hemen sonra kapiller kan şekeri ölçülür. Damar yolu hem tedavi hem doğrulama örneği için gereklidir.",
                        "new_finding": "KTA 118/dk, SS 20/dk, KB 112/70 mmHg, SpO2 %99, ateş 36.4°C. Terli, soluk. GKS 12 (G3 S4 M5), komutlara yavaş uyuyor, yutma refleksi zayıf. Pupiller izokorik. Kapiller kan şekeri 36 mg/dL. Ketonemi 0.3 mmol/L."
                    },
                    {
                        "text": "Bilinci bulanık olduğu halde ağzına şekerli meyve suyu dökmek ve kendine gelmesi için yüzüne soğuk su çarpmak",
                        "is_correct": False,
                        "scenario_update": "Yutma refleksi zayıf olan çocuk meyve suyunu aspire etti ve öksürük krizine girdi.",
                        "teaching_point": "Bilinci bozuk veya yutamayan çocuğa ağızdan bir şey verilmez."
                    }
                ]
            },
            {
                "stage_title": "Acil Tedavi",
                "question": "Kan şekeri 36 mg/dL olan ve güvenle yutamayan bu çocukta en uygun tedavi nedir?",
                "options": [
                    {
                        "text": "İV %10 dekstroz 2 mL/kg vermek; 10-15 dakika sonra kan şekerini yeniden ölçüp gerekirse dozu tekrarlamak",
                        "is_correct": True,
                        "explanation": "%10 dekstroz 0.2 g/kg glukoz sağlar ve damar için güvenlidir. Kan şekeri düzelmezse doz tekrarlanır ve ardından idame glukoz başlanır.",
                        "new_finding": "80 mL %10 dekstroz verildi. Onbeş dakika sonra kan şekeri 118 mg/dL, GKS 15, çocuk ne olduğunu soruyor. Ağızdan sandviç ve süt verildi."
                    },
                    {
                        "text": "Periferik damar yolundan hızla 1 mL/kg %50 dekstroz itmek ve kan şekeri düzelince insülin dozunu atlamak",
                        "is_correct": False,
                        "scenario_update": "Hipertonik dekstroz damar yolunda flebite ve sonrasında yeniden düşüşe neden oldu.",
                        "teaching_point": "Çocuklarda %50 dekstroz önerilmez; %10 dekstroz tercih edilir."
                    },
                    {
                        "text": "Damar yolu açık olmasına rağmen yalnızca intramüsküler glukagon yapıp etkisini görmek için yarım saat beklemek",
                        "is_correct": False,
                        "scenario_update": "Glukagon etkisi gecikti ve uzun süre kusma yaptı; şeker 30 dakika boyunca düşük kaldı.",
                        "teaching_point": "Glukagon damar yolu olmadığında veya hastane öncesinde tercih edilir; İV yol varsa dekstroz verilir."
                    },
                    {
                        "text": "Diyabet hemşiresi gelene kadar tedaviyi ertelemek, bu sürede kan şekerini her yarım saatte ölçmek",
                        "is_correct": False,
                        "scenario_update": "Erteleme sırasında çocuk nöbet geçirdi.",
                        "teaching_point": "Bilinç bulanıklığıyla seyreden düşük kan şekeri acil tedavi gerektirir; hiçbir nedenle ertelenmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu tablonun en doğru tanımı hangisidir?",
                "options": [
                    {"text": "Diyabetik ketoasidoz", "is_correct": False, "scenario_update": "Kan şekeri çok düşüktü ve ketonemi yoktu.", "teaching_point": "Ketoasidozda kan şekeri yüksek, ketonemi ve metabolik asidoz vardır."},
                    {"text": "Egzersiz ve yetersiz beslenmeyle tetiklenen ağır hipoglisemi", "is_correct": True, "explanation": "İnsülin kullanan çocukta öğün atlanması ve uzun egzersiz sonrası terleme, titreme, bilinç bulanıklığı ve 36 mg/dL kan şekeri, glukozla hızla düzelme ağır hipoglisemiyi gösterir.", "new_finding": "Tanı: Tip 1 diyabette egzersiz ve yetersiz beslenmeyle tetiklenen ağır hipoglisemi."},
                    {"text": "Eforla ısı çarpması", "is_correct": False, "scenario_update": "Vücut ısısı normaldi ve glukozla tamamen düzeldi.", "teaching_point": "Isı çarpmasında vücut ısısı 40°C üzerindedir ve bilinç değişikliği eşlik eder."},
                    {"text": "Postiktal konfüzyon", "is_correct": False, "scenario_update": "Kasılma gözlenmemişti ve bilinç glukozla hemen düzeldi.", "teaching_point": "Postiktal dönem glukoz verilmesinden bağımsız olarak yavaş düzelir."}
                ]
            },
            {
                "stage_title": "Gözlem ve Taburculuk Planı",
                "question": "Bilinci düzelen bu çocuk için en uygun plan hangisidir?",
                "options": [
                    {
                        "text": "Tekrar düşüşü önlemek için o akşamki uzun etkili insülin dozunu tamamen atlamasını ve ertesi gün yeniden başlamasını önermek",
                        "is_correct": False,
                        "scenario_update": "İnsülin atlanınca ertesi gün ketoz ve kan şekeri yüksekliği gelişti.",
                        "teaching_point": "Bazal insülin tamamen kesilmez; dozu diyabet ekibinin önerisiyle azaltılabilir."
                    },
                    {
                        "text": "Diyabetin kontrolsüz olduğunu söyleyip spor yapmasını yasaklamak ve insülin pompasına geçmeden taburcu etmemek",
                        "is_correct": False,
                        "scenario_update": "Çocuk spordan uzaklaştırıldı ve gereksiz yere yatırıldı.",
                        "teaching_point": "Egzersiz yasaklanmaz; öncesinde karbonhidrat ve insülin dozu ayarlaması öğretilir."
                    },
                    {
                        "text": "Birkaç saat gözlemleyip şeker izlemi yapmak; glukagon reçete etmek, egzersiz öncesi beslenme ve gece şeker ölçümünü öğretmek",
                        "is_correct": True,
                        "explanation": "Egzersizden saatler sonra da şeker düşebilir. Evde glukagon ve aile eğitimi bir sonraki atağın güvenle yönetilmesini sağlar.",
                        "new_finding": "Dört saatlik gözlemde kan şekerleri 110-160 mg/dL seyretti. Glukagon reçete edildi, aile ve antrenör eğitildi. Diyabet polikliniğinde insülin dozu düzenlendi."
                    },
                    {
                        "text": "Kan şekeri düzeldiği için hemen eve göndermek ve bir sonraki rutin diyabet poliklinik kontrolüne kadar değişiklik yapmamak",
                        "is_correct": False,
                        "scenario_update": "Çocuk gece yeniden düşük şeker atağı geçirdi ve evde glukagon bulunmadı.",
                        "teaching_point": "Ağır atak sonrası gözlem, glukagon reçetesi ve tetikleyiciye yönelik eğitim gerekir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S79",
        "category": "💊 Toksikoloji & Metabolik / Endokrin Aciller",
        "age": "6 Yaşında (19 kg)",
        "gender": "Kız",
        "complaint": "Ketoasidoz tedavisinin beşinci saatinde yeni başlayan baş ağrısı, kusma ve uykuya meyil",
        "history": "Çocuk bu sabah yeni tanı diyabet ve ketoasidozla (pH 6.98, HCO3 4 mmol/L, kan şekeri 620 mg/dL, düzeltilmiş Na 138 mmol/L, BUN 32 mg/dL) acile alınmış. Dış merkezde iki kez 20 mL/kg serum fizyolojik verilmiş, bikarbonat yapılmış. Acilde insülin infüzyonu 0.1 Ü/kg/saat ve sıvı başlanmış. Beşinci saatte hemşire 'baş ağrısından şikâyet etti, kustu, şimdi uyandırınca zor açıyor gözlerini' diyor. Kan şekeri 260 mg/dL'ye düşmüş, son ölçülen Na 133 mmol/L.",
        "final_diagnosis": "Diyabetik Ketoasidoz Tedavisi Sırasında Gelişen Serebral Ödem",
        "disposition": "Hiperosmolar Tedavi, Sıvı Kısıtlaması ve Yakın Nörolojik İzlemle Çocuk Yoğun Bakım Yatışı",
        "case_pearl": "Ketoasidozlu çocukların yaklaşık %0.5-1'inde tedavinin genellikle ilk 4-12 saatinde beyin ödemi gelişir. Risk faktörleri: küçük yaş, yeni tanı, ağır asidoz, düşük pCO2, yüksek BUN, bikarbonat tedavisi, hızlı sıvı verilmesi ve tedavi sırasında sodyumun yükselmemesi veya düşmesidir. Baş ağrısı, kusma, bilinç değişikliği, bradikardi ve hipertansiyon, inkontinans uyarı bulgularıdır. Tedavi görüntüleme beklenmeden başlanır: mannitol 0.5-1 g/kg veya %3 NaCl 2.5-5 mL/kg, başın 30° kaldırılması ve sıvı hızının azaltılması. Entübasyon gerekirse hiperventilasyondan kaçınılır. BT stabilizasyondan sonra kanama ve tromboz dışlamak için çekilir.",
        "steps": [
            {
                "stage_title": "Yatak Başı Değerlendirme",
                "question": "Ketoasidoz tedavisi sırasında baş ağrısı ve uykuya meyil gelişen bu çocukta ilk değerlendirmeniz nedir?",
                "options": [
                    {
                        "text": "Uykuya meyli ketoasidozun beklenen yorgunluğu kabul edip saatlik izlemi sürdürmek ve baş ağrısı için parasetamol vermek",
                        "is_correct": False,
                        "scenario_update": "Bir saat sonra çocuk yanıtsızlaştı, pupilleri eşitsizleşti.",
                        "teaching_point": "Tedavi sırasında kötüleşen bilinç ve baş ağrısı acil değerlendirme gerektirir."
                    },
                    {
                        "text": "GKS, pupiller ve vital bulguları değerlendirip bradikardi ve hipertansiyonu aramak; kan şekeri, sodyum ve sıvı dengesini gözden geçirmek",
                        "is_correct": True,
                        "explanation": "Nörolojik kötüleşmede kafa içi basınç artışının bulguları aranır. Kan şekerinin hızlı düşüşü, sodyumun düşmesi ve fazla sıvı yüklemesi risk değerlendirmesinde önemlidir.",
                        "new_finding": "KTA 64/dk (bir saat önce 128/dk), KB 132/86 mmHg, SS 18/dk düzensiz, SpO2 %97. GKS 10 (G2 S3 M5). Sağ pupil sola göre hafif geniş, ışık yanıtı tembel. Altına idrar kaçırdı. Kan şekeri 260 mg/dL, Na 133 mmol/L. İlk 5 saatte toplam 62 mL/kg sıvı almış."
                    },
                    {
                        "text": "Kan şekeri yüksek olduğu için insülin infüzyonunu 0.2 Ü/kg/saate çıkarmak ve dekstrozlu sıvıyı kesmek",
                        "is_correct": False,
                        "scenario_update": "Kan şekeri hızla 120 mg/dL'ye düştü ve osmolalite değişimi bilinç durumunu kötüleştirdi.",
                        "teaching_point": "Kan şekerinin hızlı düşürülmesi bu tabloda zararlıdır; insülin artırılmaz."
                    },
                    {
                        "text": "Kusma nedeniyle ketoasidozun kötüleştiğini düşünüp ek 20 mL/kg serum fizyolojik bolusu ve bikarbonat vermek",
                        "is_correct": False,
                        "scenario_update": "Ek sıvı ve bikarbonat sonrası bilinç daha da kötüleşti, GKS 7'ye düştü.",
                        "teaching_point": "Bu tabloda ek sıvı bolusu ve bikarbonat kafa içi basıncı artırabilir."
                    }
                ]
            },
            {
                "stage_title": "Acil Müdahale",
                "question": "Bradikardi, hipertansiyon ve pupil asimetrisi olan bu çocukta hemen ne yapılmalıdır?",
                "options": [
                    {
                        "text": "Tanıyı kesinleştirmek için önce acil kontrastsız beyin tomografisi çekmek ve radyoloji raporuna göre tedaviye karar vermek",
                        "is_correct": False,
                        "scenario_update": "Tomografiye götürülürken çocuk apneik oldu; tedavi 40 dakika gecikti.",
                        "teaching_point": "Klinik bulgular varsa tedavi görüntüleme beklenmeden başlanmalıdır."
                    },
                    {
                        "text": "Entübe edip pCO2'yi 25 mmHg'nin altına indirecek şekilde agresif hiperventilasyon uygulamak",
                        "is_correct": False,
                        "scenario_update": "Aşırı hiperventilasyon serebral kan akımını azalttı ve iskemik hasar riskini artırdı.",
                        "teaching_point": "Entübasyon gerekirse normokapni hedeflenir; agresif hiperventilasyon kötü sonuçla ilişkilidir."
                    },
                    {
                        "text": "Mannitol 0.5-1 g/kg'ı 10-15 dakikada vermek, başı 30° kaldırmak ve sıvı hızını üçte bir azaltmak",
                        "is_correct": True,
                        "explanation": "Hiperosmolar tedavi beyin dokusundan su çeker ve kafa içi basıncı düşürür. Yanıt alınamazsa %3 NaCl verilebilir. Sıvı kısıtlaması ödemin artmasını önler.",
                        "new_finding": "Mannitol 15 g verildi, baş 30° kaldırıldı, sıvı hızı azaltıldı. Yirmi dakika sonra KTA 104/dk, KB 112/70 mmHg, GKS 13, pupiller eşit ve reaktif."
                    },
                    {
                        "text": "İnsülin infüzyonunu tamamen durdurup deksametazon vermek ve bir saat sonra yeniden değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "İnsülin kesilince ketoasidoz derinleşti; deksametazon kafa içi basıncı düşürmedi.",
                        "teaching_point": "İnsülin tamamen kesilmez; deksametazonun bu tabloda yeri yoktur."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu çocuktaki kötüleşmenin en olası nedeni nedir?",
                "options": [
                    {"text": "Ketoasidoz tedavisi sırasında serebral ödem", "is_correct": True, "explanation": "Yeni tanı, ağır asidoz, yüksek BUN, bikarbonat ve fazla sıvı verilmesi zemininde tedavinin beşinci saatinde baş ağrısı, kusma, bilinç kötüleşmesi, bradikardi, hipertansiyon ve inkontinans, hiperosmolar tedaviye hızlı yanıt serebral ödemi gösterir.", "new_finding": "Tanı: Ketoasidoz tedavisi sırasında serebral ödem."},
                    {"text": "Tedaviye bağlı düşük kan şekeri", "is_correct": False, "scenario_update": "Kan şekeri 260 mg/dL'ydi.", "teaching_point": "Ketoasidoz tedavisinde kan şekeri 250-300 mg/dL'ye inince dekstroz eklenir."},
                    {"text": "Serebral venöz sinüs trombozu", "is_correct": False, "scenario_update": "Tablo hiperosmolar tedaviye hızla yanıt verdi; BT'de tromboz bulgusu yoktu.", "teaching_point": "Tromboz dehidratasyonlu ketoasidozda görülebilir ve görüntülemeyle tanınır; stabilizasyondan sonra araştırılır."},
                    {"text": "Bakteriyel menenjit", "is_correct": False, "scenario_update": "Ateş ve ense sertliği yoktu, tablo tedavinin beşinci saatinde başlamıştı.", "teaching_point": "Ketoasidozda enfeksiyon tetikleyici olabilir ama bu tablo tedaviyle zamansal ilişkilidir."}
                ]
            },
            {
                "stage_title": "İzlem ve Yatış Planı",
                "question": "Durumu düzelen bu çocuğun sonraki yönetimi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Çocuk düzeldiğine göre ketoasidoz protokolünü değiştirmeden serviste rutin saatlik takiple sürdürmek",
                        "is_correct": False,
                        "scenario_update": "İki saat sonra bulgular tekrarladı ve geç fark edildi.",
                        "teaching_point": "Ödem tekrarlayabilir; yoğun bakımda sık nörolojik izlem gerekir."
                    },
                    {
                        "text": "Yoğun bakıma almak, stabilken BT çekmek, sıvıyı kısıtlayıp sodyumu izlemek ve gerekirse hiperosmolar tedaviyi tekrarlamak",
                        "is_correct": True,
                        "explanation": "Stabilizasyon sonrası BT kanama ve trombozu dışlar. Sodyumun yükselmesini sağlamak ve sıvı kısıtlaması ödemin tekrarını önler.",
                        "new_finding": "BT'de yaygın serebral ödem bulguları, kanama ve tromboz yok. Yoğun bakımda Na kademeli olarak 140 mmol/L'ye yükseldi. Asidoz 30. saatte düzeldi ve çocuk nörolojik sekelsiz taburcu edildi."
                    },
                    {
                        "text": "Asidozun daha hızlı düzelmesi için ek bikarbonat infüzyonu başlamak ve sıvı hızını iki katına çıkarmak",
                        "is_correct": False,
                        "scenario_update": "Bikarbonat ve fazla sıvı sonrası bilinç yeniden kötüleşti.",
                        "teaching_point": "Bikarbonat ve fazla sıvı bu komplikasyonun risk faktörleridir."
                    },
                    {
                        "text": "İnsülini subkutan uygulamaya geçip ağızdan beslenmeye başlatmak ve ertesi gün taburculuğu planlamak",
                        "is_correct": False,
                        "scenario_update": "Asidozu sürerken subkutan insüline geçilince ketoasidoz derinleşti.",
                        "teaching_point": "Subkutan insüline asidoz düzelip çocuk beslenebildiğinde geçilir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S80",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "6 Aylık (7.2 kg)",
        "gender": "Erkek",
        "complaint": "Ateşsiz, bir dakika süren iki kez kasılma ve sonrasında ellerinin tuhaf şekilde bükülmesi",
        "history": "Annesi anlatıyor: 'Bugün iki kez gözleri dalıp kolları bacakları kasıldı, ateşi yoktu. Arada ellerini bilekten büküp parmaklarını birleştiriyor. Bir haftadır çok huzursuz, uyurken çok terliyor.' Sadece anne sütüyle besleniyor, ek gıdaya başlanmamış. Kış aylarında doğmuş, aile apartmanın bodrum katında oturuyor, annesi kapalı giyiniyor. Doğumdan sonra verilen D vitamini damlasını 'ağzı tadını sevmedi' diye iki aylıkken bırakmışlar. Annenin gebelikte vitamin kullanımı düzensizmiş. Kusma, ishal, kafa travması yok.",
        "final_diagnosis": "D Vitamini Eksikliğine Bağlı Hipokalsemik Konvülziyon (Nutrisyonel Raşitizm)",
        "disposition": "İV Kalsiyum, Ardından Oral Kalsiyum ve D Vitamini Tedavisiyle Pediatri Servisine Yatış; Annenin D Vitamini Düzeyinin Değerlendirilmesi",
        "case_pearl": "Türkiye'de bebeklere ilk yıl boyunca günde 400 IU D vitamini önerilir ve ücretsiz verilir. Yalnızca anne sütü alan, profilaksi almayan, güneş görmeyen ve annesi kapalı giyinen bebekler risk altındadır. Düşük kalsiyum nöbet, karpopedal spazm, laringospazm ve kardiyomiyopatiye yol açabilir. Tetkiklerde düşük kalsiyum, düşük-normal fosfor, yüksek ALP ve PTH, düşük 25-OH-D görülür; magnezyum da ölçülür. Semptomatik olguda %10 kalsiyum glukonat 0.5 mL/kg (en fazla 20 mL) EKG monitörü altında 10 dakikada verilir; ekstravazasyon ağır doku nekrozu yapar. Sonra İV veya oral kalsiyum sürdürülür ve D vitamini başlanır. Kalsiyum yerine konmadan tek başına yüksek doz D vitamini verilmesi kalsiyumu daha da düşürebilir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme",
                "question": "Ateşsiz nöbet geçiren ve el bileklerinde bükülme olan bu bebekte ilk değerlendirmeniz nedir?",
                "options": [
                    {
                        "text": "Ateşsiz nöbet nedeniyle hemen beyin MR'ı ve EEG istemek, sonuçlar gelene kadar fenobarbital yükleyip beklemek",
                        "is_correct": False,
                        "scenario_update": "Metabolik neden araştırılmadan fenobarbital verildi; bebekte laringospazm gelişti.",
                        "teaching_point": "Bebekte ateşsiz nöbette önce kan şekeri ve elektrolitler gibi düzeltilebilir nedenler araştırılır."
                    },
                    {
                        "text": "Ateşsiz kasılmanın kafa travmasıyla ilişkili olduğunu kabul edip istismar şüphesiyle sosyal hizmet ve adli bildirim yapmak",
                        "is_correct": False,
                        "scenario_update": "Metabolik değerlendirme gecikti; travma bulgusu saptanmadı.",
                        "teaching_point": "İstismar akılda tutulur ama öncelikle düzeltilebilir metabolik nedenler hızla dışlanmalıdır."
                    },
                    {
                        "text": "ABC ve kan şekerini değerlendirmek; kalsiyum, magnezyum, fosfor, sodyum, ALP ve kan gazı göndermek, monitörize edip EKG çekmek",
                        "is_correct": True,
                        "explanation": "Bu yaşta ateşsiz nöbetin en sık düzeltilebilir nedenleri şeker, sodyum, kalsiyum ve magnezyum bozukluklarıdır. Karpopedal spazm kalsiyum düşüklüğünü düşündürür; EKG'de QT uzaması aranır.",
                        "new_finding": "KTA 138/dk, SS 34/dk, SpO2 %98, ateş 36.9°C, kan şekeri 88 mg/dL. Fontanel geniş (3x3 cm), kafatası kemikleri basmakla esniyor, kostokondral bileşkelerde tespih gibi şişlikler, el bileklerinde genişleme. Karpopedal spazm. EKG'de QTc 510 ms. Total kalsiyum 5.9 mg/dL, iyonize Ca 0.72 mmol/L, fosfor 3.2 mg/dL, ALP 1240 U/L, magnezyum 1.9 mg/dL, Na 138 mmol/L."
                    },
                    {
                        "text": "Nöbet geçtiği için tetkik yapmadan aileyi bilgilendirmek ve bir hafta sonra çocuk nörolojisi polikliniğine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Bebek eve giderken arabada laringospazm ve morarma geçirdi.",
                        "teaching_point": "Ateşsiz nöbet geçiren süt çocuğu acil metabolik değerlendirme gerektirir."
                    }
                ]
            },
            {
                "stage_title": "Acil Tedavi",
                "question": "İyonize kalsiyumu 0.72 mmol/L ve QTc'si uzun olan bu bebekte en uygun acil tedavi nedir?",
                "options": [
                    {
                        "text": "Tek seferde 300.000 IU oral D vitamini (stoss) vermek ve kalsiyumun birkaç gün içinde kendiliğinden yükselmesini beklemek",
                        "is_correct": False,
                        "scenario_update": "Kalsiyum verilmediği için bebek yeniden nöbet geçirdi; kalsiyum daha da düştü.",
                        "teaching_point": "Semptomatik düşük kalsiyumda önce kalsiyum verilir; yüksek doz D vitamini bu yaşta önerilmez."
                    },
                    {
                        "text": "%10 kalsiyum glukonat 0.5 mL/kg'ı seyreltip EKG monitörüyle 10 dakikada vermek ve damar yolunu sık kontrol etmek",
                        "is_correct": True,
                        "explanation": "Yavaş İV kalsiyum aritmi riskini azaltır. Ekstravazasyon ağır doku nekrozuna yol açabileceğinden damar yolu sık kontrol edilir.",
                        "new_finding": "3.6 mL kalsiyum glukonat seyreltilerek verildi. Karpopedal spazm geçti, QTc 450 ms'ye kısaldı. Ardından İV kalsiyum infüzyonu başlandı. 25-OH-D <4 ng/mL, PTH 410 pg/mL. El bileği grafisinde metafizlerde fırçamsı görünüm."
                    },
                    {
                        "text": "Kalsiyum klorürü küçük bir el sırtı damar yolundan hızla itmek ve damar yolunu izlemeden servise göndermek",
                        "is_correct": False,
                        "scenario_update": "Kalsiyum ekstravazasyonu el sırtında ağır doku nekrozuna yol açtı; hızlı verilişte bradikardi oldu.",
                        "teaching_point": "Kalsiyum yavaş verilir; kalsiyum klorür periferik yolda kullanılmaz."
                    },
                    {
                        "text": "Önce magnezyum sülfat yüklemek ve kalsiyumun ardından gelecek kontrol tetkike göre verilmesini planlamak",
                        "is_correct": False,
                        "scenario_update": "Magnezyumu normal olan bebeğe gereksiz tedavi verildi ve kalsiyum tedavisi gecikti.",
                        "teaching_point": "Magnezyum yalnızca düşükse yerine konur; semptomatik bebekte kalsiyum geciktirilmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik, laboratuvar ve radyolojik bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Primer hipoparatiroidi", "is_correct": False, "scenario_update": "PTH düşük değil belirgin yüksekti ve fosfor yüksek değildi.", "teaching_point": "Hipoparatiroidide PTH düşük, fosfor yüksektir."},
                    {"text": "Febril olmayan idiyopatik epilepsi", "is_correct": False, "scenario_update": "Belirgin metabolik bozukluk ve kemik bulguları vardı.", "teaching_point": "Metabolik neden saptanan nöbet akut semptomatik nöbettir."},
                    {"text": "Psödohipoparatiroidi (PTH direnci)", "is_correct": False, "scenario_update": "25-OH-D çok düşüktü ve kemik bulguları beslenme kaynaklıydı.", "teaching_point": "Psödohipoparatiroidide D vitamini normal, PTH yüksek, fosfor yüksektir."},
                    {"text": "D vitamini eksikliğine bağlı hipokalsemik konvülziyon", "is_correct": True, "explanation": "Profilaksi almayan, güneş görmeyen anne sütüyle beslenen bebekte düşük kalsiyum, yüksek ALP ve PTH, çok düşük 25-OH-D, geniş fontanel, raşitik tespih ve metafiz değişiklikleri D vitamini eksikliğine bağlı hipokalsemik konvülziyonu gösterir.", "new_finding": "Tanı: Nutrisyonel D vitamini eksikliğine bağlı hipokalsemik konvülziyon."}
                ]
            },
            {
                "stage_title": "İdame Tedavi ve Yatış",
                "question": "Bu bebek için en uygun idame tedavi ve plan hangisidir?",
                "options": [
                    {
                        "text": "Kalsiyumu düzelince D vitamini vermeden taburcu etmek ve yalnızca ek gıdaya başlamalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Altta yatan eksiklik tedavi edilmedi; iki hafta sonra yeniden nöbet geçirdi.",
                        "teaching_point": "Kalsiyumun geçici düzelmesi yeterli değildir; D vitamini eksikliği tedavi edilmelidir."
                    },
                    {
                        "text": "Servise yatırıp oral kalsiyum ve günlük 2000 IU D vitamini başlamak; kalsiyumu izleyip anneyi de değerlendirmeye almak",
                        "is_correct": True,
                        "explanation": "Günlük D vitamini ve kalsiyum birlikte verildiğinde kemik mineralizasyonu düzelir. Annede de eksiklik sık olduğundan anne de değerlendirilir.",
                        "new_finding": "Üç gün sonra kalsiyum 8.9 mg/dL'ye yükseldi, İV kalsiyum kesildi. Oral tedaviyle taburcu edildi. Annenin 25-OH-D düzeyi 6 ng/mL çıktı ve tedavi başlandı. Üç ay sonra ALP normale yaklaştı."
                    },
                    {
                        "text": "Ömür boyu antiepileptik gerektiğini düşünüp levetirasetam başlamak ve D vitaminini nöroloji önerisine bırakmak",
                        "is_correct": False,
                        "scenario_update": "Gereksiz antiepileptik başlandı; altta yatan eksiklik tedavisi gecikti.",
                        "teaching_point": "Metabolik bozukluğa bağlı nöbette neden düzeltilir; uzun süreli antiepileptik gerekmez."
                    },
                    {
                        "text": "Anne sütünün yetersiz olduğunu söyleyerek emzirmeyi hemen kesmelerini ve bebeği yalnızca tam yağlı inek sütüyle beslemelerini önermek",
                        "is_correct": False,
                        "scenario_update": "İnek sütü demir eksikliği anemisine ve gastrointestinal kanamaya yol açtı.",
                        "teaching_point": "Emzirme sürdürülür, D vitamini takviyesi eklenir; bir yaştan önce inek sütü önerilmez."
                    }
                ]
            }
        ]
    }
]
