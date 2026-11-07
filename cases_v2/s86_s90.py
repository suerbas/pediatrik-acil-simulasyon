# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - S86-S90 (Nöro-onkoloji, Hematoloji, Romatoloji, Jinekoloji ve Ürolojik Aciller)
"""

SPOILERS = {
    "S86": ["medulloblastom", "posterior fossa tümörü", "arka çukur"],
    "S87": ["g6pd", "favizm"],
    "S88": ["ailevi akdeniz", "akdeniz ateşi", "fmf"],
    "S89": ["ektopik", "dış gebelik", "tubal"],
    "S90": ["appendiks testis", "apendiks testis", "morgagni", "testis eki"],
}

CASES = [
    {
        "id": "S86",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "6 Yaşında (20 kg)",
        "gender": "Erkek",
        "complaint": "Altı haftadır sabahları olan baş ağrısı ve kusma, son bir haftadır yürürken sendeleme ve çift görme",
        "history": "Annesi anlatıyor: 'Bir buçuk aydır sabah uyanınca başım ağrıyor diyor, kahvaltıdan önce kusuyor, sonra rahatlıyor. Mide üşütmesi dediler, iki kez ilaç verdiler. Bir haftadır sarhoş gibi yürüyor, düşüyor. Dün televizyonu iki tane görüyorum dedi.' Son iki haftadır okulda yazısı bozulmuş, öğretmeni dikkatsizlikten şikâyet etmiş. Ateş, yakın zamanda geçirilmiş enfeksiyon veya suçiçeği yok. Kafa travması yok.",
        "final_diagnosis": "Posterior Fossa Tümörü (Olası Medulloblastom) ve Obstrüktif Hidrosefali",
        "disposition": "Deksametazon ve Kafa İçi Basınç Önlemleriyle Acil Beyin Cerrahisi Konsültasyonu ve Yatış",
        "case_pearl": "Çocuklarda beyin tümörlerinin çoğu posterior fossadadır. Sabah baş ağrısı, bulantısız kusma, uykudan uyandıran ağrı ve haftalar içinde ilerleyen yakınmalar kafa içi basınç artışını düşündürür. Gövde ataksisi, nistagmus, altıncı sinir felcine bağlı çift görme ve papilödem eşlik edebilir. Tekrarlayan 'gastroenterit' tanısı alan çocuklarda nörolojik muayene atlanmamalıdır. Kafa içi basınç artışı şüphesinde lomber ponksiyon yapılmaz. Tanı acil görüntülemeyle konur; MR tercih edilir, ulaşılamıyorsa BT çekilir. Ödem için deksametazon başlanır ve beyin cerrahisine danışılır. Akut ataksi, enfeksiyon sonrası günler içinde başlayıp kafa içi basınç bulgusu olmadan seyrederse serebelliti düşündürür.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Nörolojik Muayene",
                "question": "Sabah baş ağrısı, kusma ve sendelemesi olan bu çocukta muayenede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Kusma nedeniyle gastroenterit kabul edip ondansetron ve ağızdan sıvı tedavisi vermek, iyi görünürse taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk iki gün sonra bilinç bulanıklığı ve şiddetli baş ağrısıyla getirildi.",
                        "teaching_point": "Sabahları olan, haftalardır süren kusma ve baş ağrısı gastroenteritle açıklanmaz; nörolojik muayene şarttır."
                    },
                    {
                        "text": "Bilinç, pupiller ve fundus muayenesiyle kranial sinirleri, yürüyüşü, serebellar testleri ve vital bulguları değerlendirmek",
                        "is_correct": True,
                        "explanation": "Fundus muayenesi papilödemi, kranial sinir muayenesi altıncı sinir tutulumunu, serebellar testler arka beyin yapılarının etkilenmesini gösterir. Bradikardi ve hipertansiyon ileri basınç artışının işaretidir.",
                        "new_finding": "Ateş 36.8°C, KTA 84/dk, KB 112/70 mmHg, SS 20/dk. Bilinç açık, GKS 15. Bilateral papilödem. Sağ gözde dışa bakış kısıtlı. Horizontal nistagmus. Geniş tabanlı, sendeleyen yürüyüş, tandem yürüyemiyor, oturur pozisyonda gövde salınımı var. Sağ elde dismetri. Kas gücü normal. Ense sertliği yok."
                    },
                    {
                        "text": "Çift görme nedeniyle göz doktoruna yönlendirip gözlük muayenesi sonrası nörolojik değerlendirme planlamak",
                        "is_correct": False,
                        "scenario_update": "Göz polikliniği randevusu bir hafta sonraya verildi; çocuk bu sürede kötüleşti.",
                        "teaching_point": "Ataksi ve kusmayla birlikte yeni çift görme acil nörolojik değerlendirme gerektirir."
                    },
                    {
                        "text": "Yazının bozulması ve dikkatsizlik nedeniyle dikkat eksikliği düşünüp çocuk psikiyatrisine ayaktan yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Nörolojik muayene yapılmadan gönderilen çocuk birkaç gün sonra yanıtsız getirildi.",
                        "teaching_point": "Yeni başlayan okul başarısı bozulması ve motor yakınmalar organik nedenleri dışlamayı gerektirir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Papilödem ve serebellar bulguları olan bu çocukta hangi yaklaşım uygundur?",
                "options": [
                    {
                        "text": "Ensefalit ve menenjiti dışlamak için hemen lomber ponksiyon yapmak ve BOS basıncını ölçmek",
                        "is_correct": False,
                        "scenario_update": "Ponksiyon sonrası çocukta bilinç bozuldu, pupiller eşitsizleşti; herniasyon gelişti.",
                        "teaching_point": "Papilödem ve fokal bulgularda lomber ponksiyon herniasyona yol açabilir; kontrendikedir."
                    },
                    {
                        "text": "Acil beyin görüntülemesi istemek, tercihen kontrastlı MR, ulaşılamıyorsa hemen BT; bu sürede nörolojik izlemi sürdürmek",
                        "is_correct": True,
                        "explanation": "Kafa içi basınç artışı ve serebellar bulgularda yapısal neden acil olarak görüntülenmelidir. MR arka beyin yapılarını daha iyi gösterir.",
                        "new_finding": "BT ve ardından MR: Dördüncü ventrikülü dolduran, 4.5 cm çaplı, kontrast tutan, orta hatta yerleşimli kitle; lateral ve üçüncü ventriküllerde belirgin genişleme, periventriküler ödem."
                    },
                    {
                        "text": "Elektroensefalografi ve elektrolitler istemek; sonuçlar normalse çocuk nörolojisi polikliniğine ayaktan yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "EEG normal geldi; görüntüleme yapılmadan gönderildi.",
                        "teaching_point": "EEG yapısal lezyonları göstermez; bu bulgularda acil görüntüleme gerekir."
                    },
                    {
                        "text": "Enfeksiyon sonrası ataksi olabileceğini düşünüp bir hafta izleyerek bulgular sürerse görüntüleme planlamak",
                        "is_correct": False,
                        "scenario_update": "İzlem sırasında çocuk ani bilinç kaybı geçirdi.",
                        "teaching_point": "Papilödem ve haftalardır süren yakınmalar enfeksiyon sonrası ataksiyle uyumlu değildir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik ve görüntüleme bulgularına göre en olası tanınız nedir?",
                "options": [
                    {"text": "Akut serebellar ataksi (postenfeksiyöz)", "is_correct": False, "scenario_update": "Yakın zamanda enfeksiyon yoktu, yakınmalar haftalardır sürüyordu ve papilödem vardı.", "teaching_point": "Postenfeksiyöz ataksi viral hastalıktan sonra ani başlar, kafa içi basınç artışı yapmaz."},
                    {"text": "İdiyopatik intrakraniyal hipertansiyon", "is_correct": False, "scenario_update": "Görüntülemede ventriküller genişti ve kitle vardı.", "teaching_point": "Bu tanıda görüntüleme normaldir, ventriküller dar veya normaldir."},
                    {"text": "Serebellar apse", "is_correct": False, "scenario_update": "Ateş, kulak veya sinüs enfeksiyonu ve halka şeklinde kontrastlanma yoktu.", "teaching_point": "Apsede ateş, enfeksiyon odağı ve halka tarzında kontrastlanma beklenir."},
                    {"text": "Posterior fossa tümörü ve obstrüktif hidrosefali", "is_correct": True, "explanation": "Haftalar içinde ilerleyen sabah baş ağrısı ve kusma, papilödem, altıncı sinir felci, gövde ataksisi, dördüncü ventrikülü dolduran kitle ve ventrikül genişlemesi posterior fossa tümörü ve obstrüktif hidrosefaliyi gösterir.", "new_finding": "Tanı: Posterior fossa tümörü (olası medulloblastom) ve obstrüktif hidrosefali."}
                ]
            },
            {
                "stage_title": "Acil Yönetim ve Yatış",
                "question": "Bu çocuk için en uygun acil yönetim hangisidir?",
                "options": [
                    {
                        "text": "Deksametazon başlamak, başı 30° kaldırmak, nörolojik izlemi sürdürmek ve beyin cerrahisine acil danışıp yatırmak",
                        "is_correct": True,
                        "explanation": "Deksametazon tümör çevresi ödemi azaltır. Hidrosefali için ventriküler drenaj veya erken cerrahi kararı beyin cerrahisi tarafından verilir.",
                        "new_finding": "Deksametazon başlandı, baş ağrısı ve kusma azaldı. Beyin cerrahisi tarafından ertesi gün tümör çıkarıldı; patoloji medulloblastom geldi. Spinal MR ile yayılım değerlendirildi ve onkoloji tedavisi planlandı."
                    },
                    {
                        "text": "Kusma nedeniyle büyük hacimli hipotonik sıvı başlamak ve cerrahiyi birkaç gün sonraki elektif listeye almak",
                        "is_correct": False,
                        "scenario_update": "Hipotonik sıvı ödemi artırdı; çocuk gece bradikardi ve bilinç kaybı geçirdi.",
                        "teaching_point": "Kafa içi basınç artışında hipotonik sıvıdan kaçınılır; hidrosefali acil değerlendirilir."
                    },
                    {
                        "text": "Ağrısını gidermek için morfin ve sakinleşmesi için midazolam vermek, ardından genel pediatri servisine yatırmak",
                        "is_correct": False,
                        "scenario_update": "Sedasyon sonrası solunum yüzeyelleşti, pCO2 yükseldi ve kafa içi basınç daha da arttı.",
                        "teaching_point": "Sedasyon nörolojik izlemi engeller ve hipoventilasyonla basıncı artırır."
                    },
                    {
                        "text": "Tümör tanısıyla doğrudan kemoterapi başlamak için onkoloji servisine yatırmak ve cerrahi görüşü sonraya bırakmak",
                        "is_correct": False,
                        "scenario_update": "Hidrosefali tedavi edilmeden bekleyen çocuk kötüleşti.",
                        "teaching_point": "Önce hidrosefali ve kitle etkisi cerrahi olarak yönetilir; doku tanısı tedaviyi belirler."
                    }
                ]
            }
        ]
    },
    {
        "id": "S87",
        "category": "🩸 Hematolojik & Onkolojik Aciller",
        "age": "3 Yaşında (14 kg)",
        "gender": "Erkek",
        "complaint": "Dünden beri aşırı solukluk, gözlerde sararma, halsizlik ve kola renginde idrar",
        "history": "Annesi anlatıyor: 'Dün sabahtan beri bembeyaz oldu, gözlerinin akı sarardı, çişi koyu kahverengi, kola gibi. Çok halsiz, sürekli uyumak istiyor.' Ailesi Aydın'da yaşıyor. Üç gün önce bahçeden toplanan taze baklayı çiğ ve pişmiş olarak bolca yemiş. Son günlerde ilaç kullanmamış, naftalin teması bilinmiyor. Ateş yok. İki yaşındayken de benzer daha hafif bir sararma olmuş, kendiliğinden geçmiş. Dayısında da 'kansızlık nöbetleri' varmış.",
        "final_diagnosis": "G6PD Eksikliğinde Bakla Tüketimine Bağlı Akut İntravasküler Hemoliz (Favizm)",
        "disposition": "Eritrosit Transfüzyonu, Hidrasyon ve Böbrek İzlemiyle Pediatri Servisine Yatış; Tetikleyicilerden Kaçınma Eğitimi",
        "case_pearl": "X'e bağlı kalıtılan bu enzim eksikliği Türkiye'de özellikle Akdeniz ve Ege bölgelerinde sıktır. Bakla, naftalin, bazı ilaçlar (primakin, dapson, sülfonamidler, nitrofurantoin, rasburikaz, metilen mavisi) ve enfeksiyonlar oksidatif stresle akut intravasküler hemolize yol açar. Ani solukluk, sarılık, koyu idrar (hemoglobinüri), taşikardi görülür. Coombs negatif, indirekt bilirubin ve LDH yüksek, haptoglobin düşüktür; yaymada ısırılmış hücreler ve Heinz cisimcikleri görülür. Hemoliz sırasında genç eritrositlerin enzimi yüksek olduğundan ölçüm yanlış normal çıkabilir; test 2-3 ay sonra tekrarlanır. Ağır anemi ve süren hemolizde transfüzyon verilir; hemoglobinüride hidrasyonla böbrek korunur.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme",
                "question": "Ani solukluk, sararma ve koyu idrarı olan bu çocukta ilk değerlendirmeniz nedir?",
                "options": [
                    {
                        "text": "Sarılık nedeniyle hepatit kabul edip karaciğer testlerini istemek ve evde istirahat önerisiyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Hemoglobin ölçülmeden gönderilen çocuk ertesi gün nefes darlığı ve taşikardiyle getirildi.",
                        "teaching_point": "Ani solukluk ve sarılık birlikteliği hemolizi düşündürür; hemoglobin hemen ölçülmelidir."
                    },
                    {
                        "text": "Koyu idrar nedeniyle glomerülonefrit kabul edip sıvı kısıtlaması ve diüretik başlayarak böbrek testlerini beklemek",
                        "is_correct": False,
                        "scenario_update": "Sıvı kısıtlaması sonrası kreatinin yükseldi ve idrar çıkışı azaldı.",
                        "teaching_point": "Kola renkli idrar hemoglobinüriden de kaynaklanabilir; bu durumda hidrasyon böbreği korur."
                    },
                    {
                        "text": "Perfüzyonu ve kalp yetersizliği bulgularını değerlendirip tam kan sayımı, retikülosit, bilirubin, LDH, direkt Coombs ve idrar tetkiki istemek",
                        "is_correct": True,
                        "explanation": "Ağır anemide kalp yetersizliği gelişebilir. Retikülosit, indirekt bilirubin, LDH ve Coombs hemolizin varlığını ve immün kaynaklı olup olmadığını gösterir.",
                        "new_finding": "KTA 152/dk, SS 30/dk, KB 94/56 mmHg, SpO2 %98, KDZ 2 sn, ateş 36.9°C. Belirgin soluk ve ikterik, hafif hepatomegali, dalak ele gelmiyor. Galo ritmi yok. Hb 5.4 g/dL, MCV 84 fL, retikülosit %8, lökosit 13.200/mm³, trombosit 312.000/mm³. İndirekt bilirubin 5.6 mg/dL, LDH 1.680 U/L, haptoglobin <10 mg/dL. Direkt Coombs negatif. İdrar: kan pozitif, mikroskopide eritrosit yok."
                    },
                    {
                        "text": "Demir eksikliği anemisi kabul edip yüksek doz oral demir başlamak ve bir ay sonra kan sayımı kontrolü planlamak",
                        "is_correct": False,
                        "scenario_update": "Demir tedavisi akut tabloyu düzeltmedi; çocuk iki gün sonra Hb 4.1 g/dL ile getirildi.",
                        "teaching_point": "Ani gelişen, sarılıklı ve normositer anemi demir eksikliğiyle açıklanmaz."
                    }
                ]
            },
            {
                "stage_title": "Periferik Yayma Yorumu",
                "question": "Periferik yaymada hangi bulgu bu tabloyu en çok destekler?",
                "options": [
                    {
                        "text": "Isırılmış hücreler (bite cell), kabarcıklı hücreler ve özel boyamayla eritrositlerde Heinz cisimcikleri",
                        "is_correct": True,
                        "explanation": "Oksidatif hasarla çökmüş hemoglobin Heinz cisimciklerini oluşturur; dalak bunları uzaklaştırırken ısırılmış görünüm meydana gelir.",
                        "new_finding": "Yaymada çok sayıda ısırılmış ve kabarcıklı eritrosit, polikromazi. Supravital boyamada Heinz cisimcikleri. Şistosit ve sferosit yok. Enzim düzeyi gönderildi."
                    },
                    {
                        "text": "Çok sayıda mikrosferosit ve osmotik frajilite artışı ile birlikte pozitif aile öyküsü ve belirgin splenomegali",
                        "is_correct": False,
                        "scenario_update": "Yaymada sferosit yoktu ve dalak ele gelmiyordu.",
                        "teaching_point": "Kalıtsal sferositozda sferositler, splenomegali ve kronik hemoliz bulguları görülür."
                    },
                    {
                        "text": "Şistositler (parçalanmış eritrositler), trombositopeni ve yüksek kreatininle birlikte kanlı ishal öyküsü",
                        "is_correct": False,
                        "scenario_update": "Şistosit yoktu, trombosit sayısı ve kreatinin normaldi.",
                        "teaching_point": "Şistositler ve trombositopeni mikroanjiyopatik hemolizi düşündürür."
                    },
                    {
                        "text": "Hipokrom mikrositer eritrositler, hedef hücreler ve bazofilik noktalanma ile düşük MCV ve yüksek RDW",
                        "is_correct": False,
                        "scenario_update": "MCV normaldi ve hedef hücre yoktu.",
                        "teaching_point": "Bu bulgular talasemi veya kurşun zehirlenmesini düşündürür."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Otoimmün hemolitik anemi", "is_correct": False, "scenario_update": "Direkt Coombs negatifti ve sferosit yoktu.", "teaching_point": "Otoimmün hemolizde direkt Coombs pozitiftir ve sferositler görülür."},
                    {"text": "G6PD eksikliğinde baklaya bağlı akut hemoliz (favizm)", "is_correct": True, "explanation": "Erkek çocukta bakla tüketiminden sonra gelişen ani intravasküler hemoliz, hemoglobinüri, Coombs negatifliği, ısırılmış hücreler ve Heinz cisimcikleri, önceki benzer atak ve anne tarafında benzer öykü G6PD eksikliğine bağlı favizmi gösterir.", "new_finding": "Tanı: G6PD eksikliğinde bakla tüketimine bağlı akut hemoliz (favizm)."},
                    {"text": "Hemolitik üremik sendrom", "is_correct": False, "scenario_update": "Kanlı ishal, trombositopeni ve böbrek yetmezliği yoktu.", "teaching_point": "HÜS'te şistositler, trombositopeni ve akut böbrek hasarı birlikte görülür."},
                    {"text": "Akut viral hepatit", "is_correct": False, "scenario_update": "Bilirubin indirekt baskındı ve belirgin anemi vardı.", "teaching_point": "Hepatitte direkt bilirubin ve transaminazlar yükselir, ağır anemi beklenmez."}
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Hemolizi durdurmak için yüksek doz İV metilprednizolon ve intravenöz immünglobulin vermek",
                        "is_correct": False,
                        "scenario_update": "Tedavi hemolizi etkilemedi; transfüzyon gecikti.",
                        "teaching_point": "Bu hemoliz immün kaynaklı değildir; kortikosteroid ve İVİG etkisizdir."
                    },
                    {
                        "text": "Eritrosit süspansiyonu 10 mL/kg vermek, hidrasyonla idrar çıkışını korumak, servise yatırıp tetikleyici listesini öğretmek",
                        "is_correct": True,
                        "explanation": "Ağır ve süren hemolizde transfüzyon doku oksijenlenmesini korur. Hidrasyon hemoglobinüriye bağlı böbrek hasarını önler. Aile bakla, naftalin ve riskli ilaçlardan kaçınmalıdır.",
                        "new_finding": "Transfüzyon sonrası Hb 8.6 g/dL, kalp hızı 118/dk. İdrar üçüncü günde açıldı. Tetikleyici listesi verildi. Üç ay sonra enzim düzeyi belirgin düşük bulundu; anne taşıyıcı çıktı."
                    },
                    {
                        "text": "Hemoliz kendiliğinden duracağı için transfüzyon yapmadan folik asit başlayıp ertesi gün poliklinik kontrolüyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Evde hemoliz sürdü; çocuk Hb 3.8 g/dL ve kalp yetersizliği bulgularıyla getirildi.",
                        "teaching_point": "Hb 6 g/dL altında ve süren hemolizde çocuk yatırılmalı, transfüzyon değerlendirilmelidir."
                    },
                    {
                        "text": "Splenektomi için çocuk cerrahisine danışmak ve tekrarlayan atakları önlemek için cerrahiyi planlamak",
                        "is_correct": False,
                        "scenario_update": "Dalak bu hemolizde temel rol oynamadığı için cerrahi yarar sağlamazdı.",
                        "teaching_point": "Bu hastalıkta splenektominin yeri yoktur; tetikleyicilerden kaçınmak esastır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S88",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "7 Yaşında (23 kg)",
        "gender": "Kız",
        "complaint": "Dünden beri yüksek ateş ve tüm karına yayılan şiddetli karın ağrısı",
        "history": "Annesi anlatıyor: 'Dün öğleden sonra 39.5 ateşle birlikte karnı ağrımaya başladı, kıvranıyor, yürürken öne eğiliyor. Bir kez kustu, ishali yok.' Son iki yılda yılda 5-6 kez, 2-3 gün süren ateşli karın ağrısı atakları olmuş; her seferinde 'mide virüsü' denmiş, iki kez de apandisit şüphesiyle cerrahiye danışılmış. Ataklar arasında tamamen iyi. Bir kez de ateşle birlikte dizi şişmiş. Ailesi Sivaslı, akraba evliliği var. Amcası genç yaşta böbrek yetmezliğinden diyalize girmiş.",
        "final_diagnosis": "Ailevi Akdeniz Ateşi (FMF) Atağı (Peritonit)",
        "disposition": "Analjezi ve Gözlem Sonrası Kolşisin Başlanarak, Amiloidoz Taraması ve Çocuk Romatoloji Kontrolüyle Taburculuk",
        "case_pearl": "Türkiye'de sık görülen bu otoinflamatuvar hastalık 1-3 gün süren, kendiliğinden geçen ateş ve seröz zar inflamasyonu (peritonit, plörit, artrit) ataklarıyla seyreder. Atak sırasında akut batın bulguları apandisiti taklit edebilir ve gereksiz laparotomilere yol açabilir. Ataklar arası tam iyilik hali, aile öyküsü ve akraba evliliği önemli ipuçlarıdır. Atakta CRP, sedimantasyon ve serum amiloid A yükselir, ataklar arasında normale döner. Tanı klinik kriterlerle konur, MEFV gen analizi destekler. Tedavi ömür boyu kolşisindir; ataklar ve en önemlisi amiloidoz önlenir. Amiloidozun ilk bulgusu proteinüridir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Karın Muayenesi",
                "question": "Ateşli ve yaygın karın ağrısı olan bu çocukta ilk değerlendirmeniz nedir?",
                "options": [
                    {
                        "text": "Yaygın hassasiyet olduğu için apandisit perforasyonu kabul edip görüntüleme yapmadan acil laparotomi için cerrahiye yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Laparotomide apendiks normal bulundu, yalnızca az miktarda seröz sıvı vardı.",
                        "teaching_point": "Tekrarlayan benzer ataklar öyküsü olan çocukta görüntüleme ve öykü değerlendirilmeden cerrahi karar verilmez."
                    },
                    {
                        "text": "Vital bulgular ve hidrasyonu değerlendirip ayrıntılı karın muayenesi yapmak, tekrarlayan atakların özelliklerini ve aile öyküsünü derinleştirmek",
                        "is_correct": True,
                        "explanation": "Ataklar arası tam iyilik, kısa süreli kendiliğinden geçen ateşli ataklar, artrit ve aile öyküsü ayırıcı tanıyı belirgin şekilde daraltır.",
                        "new_finding": "Ateş 39.3°C, KTA 132/dk, KB 104/66 mmHg, SS 24/dk. Mukozalar hafif kuru. Karında yaygın hassasiyet ve hafif defans, belirgin lokalize hassasiyet yok, rebound şüpheli. Bağırsak sesleri azalmış. Akciğer ve eklem muayenesi normal. Döküntü yok."
                    },
                    {
                        "text": "Ağrı muayeneyi zorlaştırmasın diye hiçbir analjezik vermeden çocuğu saatlerce aç izleyip seri muayene yapmak",
                        "is_correct": False,
                        "scenario_update": "Analjezi verilmeyen çocuk saatlerce kıvrandı ve aile büyük sıkıntı yaşadı.",
                        "teaching_point": "Analjezi muayene bulgularını gizlemez; akut karın ağrısında güvenle verilmelidir."
                    },
                    {
                        "text": "Mide virüsü kabul edip ağızdan sıvı ve antiemetik vererek taburcu etmek ve ateş düşmezse kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Tekrarlayan ataklar yine değerlendirilmeden geçiştirildi ve tanı yıllarca gecikti.",
                        "teaching_point": "Tekrarlayan ateşli karın ağrısı atakları her seferinde gastroenterit olarak açıklanmamalıdır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Analjezi sonrası ağrısı azalan bu çocukta hangi tetkikler en uygundur?",
                "options": [
                    {
                        "text": "Batın tomografisi çekmek ve ardından bağırsak duvarını görmek için kolonoskopi planlamak",
                        "is_correct": False,
                        "scenario_update": "Tomografi yönetimi değiştirmedi; çocuk gereksiz radyasyon aldı.",
                        "teaching_point": "Çocuklarda karın ağrısında ilk görüntüleme ultrasonografidir."
                    },
                    {
                        "text": "Tam kan sayımı, CRP, sedimantasyon, serum amiloid A, idrar tetkiki ve proteinüri ile karın ultrasonografisi istemek",
                        "is_correct": True,
                        "explanation": "Ultrasonografi apandisiti değerlendirir. Akut faz belirteçleri atak sırasında belirgin yükselir. İdrarda protein amiloidozun ilk bulgusudur.",
                        "new_finding": "Lökosit 15.800/mm³ (nötrofil %84), CRP 148 mg/L, sedimantasyon 62 mm/sa, serum amiloid A çok yüksek. İdrar normal, proteinüri yok. Ultrasonografide apendiks 4 mm, kompresyonla daralıyor, çevresinde inflamasyon yok; Douglas'ta az miktarda serbest sıvı."
                    },
                    {
                        "text": "Tetkik yapmadan antibiyotik başlayıp ateş düşene kadar beklemek ve sonraki atakta değerlendirme yapmak",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik etkisizdi; atak kendi süresinde geçti ve tanı yine konmadı.",
                        "teaching_point": "Bu ataklar antibiyotikten bağımsız olarak 1-3 günde kendiliğinden geçer."
                    },
                    {
                        "text": "Lomber ponksiyon ve kan kültürü yapıp menenjit ve sepsisi dışlamak için sonuçları beklemek",
                        "is_correct": False,
                        "scenario_update": "Menenjit bulgusu olmayan çocukta gereksiz girişim yapıldı.",
                        "teaching_point": "Tetkikler klinik bulgulara göre seçilmelidir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Akut apandisit", "is_correct": False, "scenario_update": "Apendiks ultrasonografide normaldi ve benzer ataklar kendiliğinden geçmişti.", "teaching_point": "Apandisitte apendiks çapı 6 mm üzerinde, kompresyonla daralmaz ve çevresinde inflamasyon görülür."},
                    {"text": "Ailevi Akdeniz ateşi atağı (peritonit)", "is_correct": True, "explanation": "Akraba evliliği ve amiloidoz düşündüren aile öyküsü olan çocukta 2-3 gün süren tekrarlayan ateşli peritonit ve artrit atakları, ataklar arası tam iyilik, belirgin akut faz yanıtı ve normal apendiks ailevi Akdeniz ateşi atağını gösterir.", "new_finding": "Tanı: Ailevi Akdeniz ateşi atağı (peritonit). MEFV gen analizinde M694V homozigot mutasyon saptandı."},
                    {"text": "Henoch-Schönlein purpurası", "is_correct": False, "scenario_update": "Palpabl purpura yoktu ve ataklar tekrarlayıcıydı.", "teaching_point": "HSP'de alt ekstremitelerde palpabl purpura, artrit ve karın ağrısı görülür."},
                    {"text": "Primer bakteriyel peritonit", "is_correct": False, "scenario_update": "Nefrotik sendrom veya asit yoktu; benzer ataklar kendiliğinden geçmişti.", "teaching_point": "Primer peritonit çoğunlukla nefrotik sendrom veya sirozla ilişkilidir."}
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun uzun dönem plan hangisidir?",
                "options": [
                    {
                        "text": "Yalnızca ataklar sırasında kolşisin kullanmalarını ve ataklar arasında ilacı tamamen bırakmalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Ataklar sürdü ve yıllar içinde proteinüri gelişti.",
                        "teaching_point": "İlaç her gün, ömür boyu kullanılır; amaç atakları ve amiloidozu önlemektir."
                    },
                    {
                        "text": "Ataklar seyrek olduğu için tedavi gerekmediğini söyleyip yalnızca ağrı kesiciyle izlemeyi önermek",
                        "is_correct": False,
                        "scenario_update": "Tedavisiz izlenen çocukta ilerleyen yıllarda nefrotik düzeyde proteinüri gelişti.",
                        "teaching_point": "Tedavisiz hastalarda amiloidoz riski yüksektir; tanı konan her hastaya tedavi başlanır."
                    },
                    {
                        "text": "Analjeziyle atak geçince her gün kolşisin başlamak, aileye ömür boyu kullanımı anlatmak ve proteinüri izlemi planlamak",
                        "is_correct": True,
                        "explanation": "Günlük kolşisin atak sıklığını azaltır ve amiloidozu önler. Düzenli idrar protein izlemi böbrek tutulumunu erken yakalar.",
                        "new_finding": "Atak 48 saatte kendiliğinden geriledi. Kolşisin başlandı, aile bilgilendirildi. Romatoloji kontrolünde atak sıklığı belirgin azaldı; proteinüri gelişmedi. Kardeşleri de değerlendirmeye çağrıldı."
                    },
                    {
                        "text": "Ataklar sırasında uzun süreli yüksek doz oral kortikosteroid başlamak ve ataklar belirgin şekilde seyrekleşince dozu yavaşça azaltmak",
                        "is_correct": False,
                        "scenario_update": "Kortikosteroid atakları önlemedi; çocukta kilo artışı ve büyüme yavaşlaması oldu.",
                        "teaching_point": "Bu hastalıkta kortikosteroidin yeri yoktur; temel tedavi kolşisindir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S89",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "16 Yaşında (54 kg)",
        "gender": "Kız",
        "complaint": "Bugün aniden başlayan sağ alt karın ağrısı, baş dönmesi ve bir kez bayılma",
        "history": "Annesiyle geldi. Annesi: 'Okulda karnım ağrıyor dedi, tuvalette bayılmış. Apandisit mi?' Hasta ilk görüşmede adet düzensizliği dışında bir şey söylemedi. Anne odadan çıkarıldıktan sonra yapılan gizlilik gözetilen görüşmede son adetinin yedi hafta önce olduğunu, bir aydır erkek arkadaşıyla cinsel ilişkisi olduğunu, iki gündür hafif lekelenme tarzında kanaması olduğunu anlatıyor. Bir yıl önce pelvik enfeksiyon nedeniyle antibiyotik kullanmış. Ağrı sağ omzuna da vuruyor.",
        "final_diagnosis": "Rüptüre Ektopik (Tubal) Gebelik ve Hemoperitoneum",
        "disposition": "Resüsitasyon, Kan Hazırlığı ve Acil Laparoskopi İçin Kadın Hastalıkları ve Doğum Kliniğine Yatış",
        "case_pearl": "Doğurganlık çağındaki her ergen kızda karın ağrısı, bayılma veya vajinal kanamada gebelik testi yapılmalıdır. Öykü ergenle yalnız ve gizlilik gözetilerek alınmalıdır. Pelvik enfeksiyon öyküsü tubal hasar yoluyla risk faktörüdür. Pozitif test, boş uterus, adneksiyal kitle ve Douglas'ta serbest sıvı tanıyı düşündürür. Omuz ağrısı diyafram irritasyonuna bağlı karın içi kanamanın işaretidir. Hemodinamik bozuklukta iki geniş damar yolu, kan grubu ve çapraz karşılaştırma yapılır, Rh negatif hastalara anti-D verilir ve acil cerrahi uygulanır. Hemodinamisi stabil, rüptür olmayan erken olgularda metotreksat seçilebilir. On sekiz yaş altı gebelikte yasal bildirim yükümlülükleri gözetilir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Öykü",
                "question": "Sağ alt karın ağrısı ve bayılması olan bu ergende ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Apandisit kabul edip annenin yanında kısa öykü almak ve doğrudan çocuk cerrahisine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Ergen annesinin yanında cinsel öyküsünü paylaşmadı; asıl neden gözden kaçtı ve kanama sürdü.",
                        "teaching_point": "Ergenle gizlilik gözetilerek yalnız görüşülmeli ve gebelik olasılığı her zaman sorgulanmalıdır."
                    },
                    {
                        "text": "Vital bulguları değerlendirip iki geniş damar yolu açmak, gebelik testi ve kan grubu göndermek",
                        "is_correct": True,
                        "explanation": "Bayılma ve omuz ağrısı karın içi kanamayı düşündürür; damar yolu ve kan hazırlığı erkenden yapılmalıdır. Gebelik testi ayırıcı tanının merkezindedir.",
                        "new_finding": "KTA 128/dk, KB 88/54 mmHg, SS 22/dk, SpO2 %99, ateş 36.7°C, KDZ 3 sn. Soluk ve terli. Sağ alt kadranda belirgin hassasiyet, rebound ve defans; karında yaygın hassasiyet. İdrar gebelik testi pozitif, serum β-hCG 3.850 mIU/mL. Hb 9.2 g/dL. Kan grubu A Rh negatif."
                    },
                    {
                        "text": "Bayılmayı vazovagal kabul edip ağızdan sıvı vermek, ağrı kesiciyle izleyip ağrı geçerse taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Bekleme sırasında kan basıncı 70/40 mmHg'ye düştü ve bilinç bulanıklaştı.",
                        "teaching_point": "Karın ağrısıyla birlikte bayılma karın içi kanama açısından değerlendirilmelidir."
                    },
                    {
                        "text": "Pelvik enfeksiyon öyküsü nedeniyle tekrarlayan pelvik inflamatuvar hastalık kabul edip ayaktan antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "Gebelik testi yapılmadan antibiyotikle gönderilen hasta şok tablosuyla geri geldi.",
                        "teaching_point": "Pelvik enfeksiyon öyküsü tüp hasarı yoluyla uterus dışı gebelik için risk faktörüdür; önce gebelik dışlanmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Görüntüleme Kararı",
                "question": "Gebelik testi pozitif ve hipotansif olan bu ergende hangi görüntüleme uygundur?",
                "options": [
                    {
                        "text": "Kontrastlı batın tomografisi çekip apandisiti dışlamak ve sonra kadın doğum konsültasyonu istemek",
                        "is_correct": False,
                        "scenario_update": "Tomografi için harcanan sürede hasta şoka girdi; gebelikte gereksiz radyasyon verildi.",
                        "teaching_point": "Gebelikte ve instabil hastada tomografi yerine yatak başı ultrasonografi tercih edilir."
                    },
                    {
                        "text": "Yatak başı ultrasonografiyle karın içi serbest sıvıyı aramak, uterus içinde gebelik kesesini ve adneksleri değerlendirmek",
                        "is_correct": True,
                        "explanation": "Yatak başı ultrasonografi hızlıdır ve hastayı yerinden kaldırmadan karın içi kanamayı gösterir. Uterus içinde gebelik görülmemesi ve adneksiyal kitle tanıyı destekler.",
                        "new_finding": "Uterus boş, endometrium kalın. Sağ adnekste 3 cm'lik heterojen kitle. Douglas boşluğunda ve Morison poşunda pıhtı içeren yaygın serbest sıvı."
                    },
                    {
                        "text": "β-hCG düzeyinin 48 saat sonraki artışını görmek için tekrar ölçüm planlamak ve hastayı serviste izlemek",
                        "is_correct": False,
                        "scenario_update": "İzlem sırasında hemoglobin 6.8 g/dL'ye düştü ve hasta şoka girdi.",
                        "teaching_point": "Seri β-hCG izlemi yalnızca stabil ve kanaması olmayan hastalarda uygundur."
                    },
                    {
                        "text": "Pelvik MR istemek ve kitlenin niteliğini belirledikten sonra tedavi kararını vermek",
                        "is_correct": False,
                        "scenario_update": "MR için beklenirken hasta hemodinamik olarak kötüleşti.",
                        "teaching_point": "İnstabil hastada uzun süren görüntülemelerden kaçınılır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Rüptüre over kisti", "is_correct": False, "scenario_update": "Gebelik testi pozitifti ve uterus boştu.", "teaching_point": "Over kisti rüptüründe gebelik testi negatiftir."},
                    {"text": "Akut apandisit", "is_correct": False, "scenario_update": "Gebelik testi pozitifti, karında pıhtılı yaygın sıvı ve adneksiyal kitle vardı.", "teaching_point": "Apandisitte hipotansiyon ve hemoperitoneum beklenmez."},
                    {"text": "Over torsiyonu", "is_correct": False, "scenario_update": "Gebelik testi pozitifti ve yaygın kanamalı serbest sıvı vardı.", "teaching_point": "Over torsiyonunda büyümüş over ve azalmış akım görülür; kanama tipik değildir."},
                    {"text": "Rüptüre ektopik gebelik ve hemoperitoneum", "is_correct": True, "explanation": "Pozitif gebelik testi, boş uterus, adneksiyal kitle, pıhtılı serbest sıvı, hipotansiyon, bayılma ve omuz ağrısı rüptüre ektopik gebelik ve hemoperitoneumu gösterir.", "new_finding": "Tanı: Rüptüre sağ tubal (ektopik) gebelik ve hemoperitoneum."}
                ]
            },
            {
                "stage_title": "Acil Tedavi",
                "question": "Bu hasta için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Kristaloid ve kan ürünleriyle resüsitasyon yapıp anti-D vermek ve kadın doğumla acil laparoskopiye almak",
                        "is_correct": True,
                        "explanation": "Rüptür ve hemodinamik bozuklukta cerrahi tek seçenektir. Rh negatif hastada anti-D ilerideki gebelikleri korur.",
                        "new_finding": "Bir ünite eritrosit verildi, anti-D yapıldı. Laparoskopide sağ tüpte rüptüre gebelik ve 800 mL hemoperitoneum saptandı, salpenjektomi yapıldı. Hasta ve ailesiyle psikososyal destek planlandı, yasal süreç sosyal hizmetle yürütüldü."
                    },
                    {
                        "text": "Ağızdan ilk dozu verilen metotreksat ile medikal tedavi başlayıp hastayı serviste seri β-hCG ile izlemek",
                        "is_correct": False,
                        "scenario_update": "Medikal tedavi kanamayı durdurmadı; hasta derin şoka girdi.",
                        "teaching_point": "Metotreksat yalnızca hemodinamisi stabil, rüptür olmayan olgularda seçilir."
                    },
                    {
                        "text": "Hastanın isteği üzerine durumu ailesinden tamamen gizlemek ve onam almadan cerrahiye göndermeden izlemek",
                        "is_correct": False,
                        "scenario_update": "Hayati girişim gecikti ve yasal süreçler yürütülmedi.",
                        "teaching_point": "Gizlilik önemlidir ancak hayati tehlikede ve yasal bildirim gerektiren durumlarda sınırları vardır; süreç hasta ile birlikte yönetilir."
                    },
                    {
                        "text": "Kanamanın kendiliğinden durmasını beklemek için traneksamik asit verip hastayı yoğun bakımda gözlemek",
                        "is_correct": False,
                        "scenario_update": "Kanama durmadı ve hasta masif transfüzyon gerektirdi.",
                        "teaching_point": "Kanayan bir tüp cerrahi olarak kontrol altına alınmalıdır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S90",
        "category": "💧 Sıvı-Elektrolit & Renal / Ürolojik Aciller",
        "age": "10 Yaşında",
        "gender": "Erkek",
        "complaint": "Dünden beri giderek artan sol testis ağrısı ve hafif şişlik",
        "history": "Babası anlatıyor: 'Dün öğleden sonra sol yumurtalığım ağrıyor dedi, gece biraz arttı. Yürürken ağrıyor ama uyuyabildi. Kusma yok.' Ağrı aniden değil yavaş yavaş başlamış. Travma, ateş, idrar yaparken yanma yok. Cinsel aktivite yok. Kabakulak geçirmemiş, aşıları tam. Daha önce benzer ağrı olmamış.",
        "final_diagnosis": "Appendiks Testis (Morgagni Hidatiği) Torsiyonu",
        "disposition": "NSAİİ, İstirahat ve Skrotal Destekle Sarı Alandan Taburculuk; Ağrı Artarsa Hemen Başvuru Önerisi",
        "case_pearl": "Prepubertal erkek çocukta akut skrotumun en sık nedeni testis eklerinin torsiyonudur. Ağrı genellikle daha yavaş başlar, testisin üst kutbunda lokalize hassasiyet vardır ve bazen deri altında mavi-siyah bir nokta görülür. Kremaster refleksi korunur, testis normal pozisyondadır. Testis torsiyonunda ise ani şiddetli ağrı, kusma, yüksek yerleşimli ve yatay duran testis, kremaster refleksinin kaybı tipiktir. Kuşkuda renkli Doppler ultrasonografi testis kan akımını değerlendirir; ancak klinik olarak testis torsiyonu düşünülüyorsa görüntüleme beklenmeden cerrahiye danışılır. Ek torsiyonu NSAİİ ve istirahatle 5-10 günde geçer.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Testis ağrısı olan bu çocuğun muayenesinde neye dikkat edersiniz?",
                "options": [
                    {
                        "text": "Ağrı bir günü geçtiği için testisin kurtarılamayacağını düşünüp muayene etmeden ağrı kesiciyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Muayene edilmeden gönderilen çocuğun tanısı belirsiz kaldı.",
                        "teaching_point": "Her akut skrotumda ayrıntılı muayene yapılmalıdır; süre tek başına karar vermez."
                    },
                    {
                        "text": "Testisin pozisyonunu ve duruşunu, hassasiyetin yerini, kremaster refleksini ve skrotal deriyi iki taraflı karşılaştırarak değerlendirmek",
                        "is_correct": True,
                        "explanation": "Testis pozisyonu, hassasiyetin yeri ve kremaster refleksi testis torsiyonunu diğer nedenlerden ayırmada en değerli muayene bulgularıdır.",
                        "new_finding": "Ateş 36.8°C, genel durum iyi, KTA 96/dk. Sol hemiskrotumda hafif ödem ve kızarıklık. Sol testis normal yerleşimli, dikey duruşlu, testis gövdesi hassas değil. Üst kutupta 3-4 mm'lik çok hassas nodül ve üzerinde deri altında mavi-siyah renk değişikliği. Kremaster refleksi iki tarafta var. Karın muayenesi normal."
                    },
                    {
                        "text": "Testis ağrısını kabakulak orşiti kabul edip muayeneyi kısa tutarak tükürük bezlerini değerlendirmek ve evde izlem önermek",
                        "is_correct": False,
                        "scenario_update": "Parotis şişliği yoktu; testis muayenesi ayrıntılı yapılmadı ve ayırıcı tanı eksik kaldı.",
                        "teaching_point": "Orşit genellikle parotitten sonra, ergenlik sonrası görülür; aşılı prepubertal çocukta olası değildir."
                    },
                    {
                        "text": "İdrar yolu enfeksiyonu kabul edip yalnızca idrar tetkiki istemek ve sonuç gelene kadar ampirik antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "İdrar tetkiki normal geldi; skrotal muayene ve görüntüleme gecikti.",
                        "teaching_point": "Akut skrotumda önce testis muayenesi yapılmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Bu muayene bulgularıyla hangi yaklaşım uygundur?",
                "options": [
                    {
                        "text": "Görüntüleme yapmadan doğrudan acil skrotal eksplorasyon için çocuk ürolojisine ameliyathane hazırlığı istemek",
                        "is_correct": False,
                        "scenario_update": "Testis torsiyonu bulgusu olmayan çocuk gereksiz bir cerrahi girişimle karşı karşıya kaldı.",
                        "teaching_point": "Klinik testis torsiyonunu düşündürmüyorsa Doppler ile değerlendirme yapılabilir."
                    },
                    {
                        "text": "Tam kan sayımı, CRP ve kan kültürü göndermek; sonuç gelene kadar İV antibiyotik başlayıp servise yatırmak",
                        "is_correct": False,
                        "scenario_update": "Sonuçlar normal geldi ve çocuk gereksiz yere yatırıldı.",
                        "teaching_point": "Ateşsiz, lokalize hassasiyeti olan çocukta enfeksiyon belirteçleri tanıya katkı sağlamaz."
                    },
                    {
                        "text": "Testis kan akımını göstermek için iki taraflı renkli Doppler ultrasonografi istemek ve idrar tetkiki yapmak",
                        "is_correct": True,
                        "explanation": "Doppler testis akımının korunduğunu göstererek testis torsiyonunu dışlar ve eklerdeki değişikliği gösterebilir. İdrar tetkiki epididimiti değerlendirmeye yardımcı olur.",
                        "new_finding": "Doppler: Her iki testiste kan akımı simetrik ve normal. Sol testis üst kutbunda 5 mm'lik, akım izlenmeyen, hipoekoik-heterojen oval yapı; çevresinde hafif reaktif hidrosel. Epididim normal boyut ve akımda. İdrar tetkiki normal."
                    },
                    {
                        "text": "Skrotal manüel detorsiyon yapmak için testisi dışa doğru çevirmek ve ardından ağrının azalıp azalmadığına bakmak",
                        "is_correct": False,
                        "scenario_update": "Gereksiz manipülasyon çocukta şiddetli ağrıya neden oldu.",
                        "teaching_point": "Manüel detorsiyon yalnızca testis torsiyonunda ve cerrahi gecikecekse geçici bir önlemdir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik ve Doppler bulgularına göre en olası tanınız nedir?",
                "options": [
                    {"text": "Testis (spermatik kord) torsiyonu", "is_correct": False, "scenario_update": "Testis akımı normaldi, kremaster refleksi vardı ve testis normal pozisyondaydı.", "teaching_point": "Testis torsiyonunda akım azalmış veya yoktur ve testis yüksek, yatay yerleşimlidir."},
                    {"text": "Akut epididimit", "is_correct": False, "scenario_update": "Epididim normaldi ve idrar tetkiki temizdi.", "teaching_point": "Epididimitte epididim büyük ve hiperemiktir; sıklıkla idrar bulguları eşlik eder."},
                    {"text": "Appendiks testis torsiyonu", "is_correct": True, "explanation": "Yavaş başlayan ağrı, üst kutupta lokalize hassas nodül ve mavi-siyah renk değişikliği, korunmuş kremaster refleksi, normal testis akımı ve akımsız ek yapısı appendiks testis torsiyonunu gösterir.", "new_finding": "Tanı: Appendiks testis torsiyonu."},
                    {"text": "İnkarsere inguinal herni", "is_correct": False, "scenario_update": "Kasık kanalında kitle yoktu ve barsak bulgusu saptanmadı.", "teaching_point": "İnkarsere hernide kasıktan skrotuma uzanan, redükte edilemeyen kitle olur."}
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "İbuprofen, birkaç gün istirahat ve skrotal destek önermek; ağrı ani artarsa veya kusma olursa hemen başvurmalarını söylemek",
                        "is_correct": True,
                        "explanation": "Ek torsiyonu kendiliğinden geçer; tedavi ağrı kontrolüdür. Uyarı bulguları öğretilerek nadir görülen testis torsiyonunun atlanması önlenir.",
                        "new_finding": "İbuprofen başlandı. Bir hafta sonraki kontrolde ağrı tamamen geçmişti, muayene normaldi."
                    },
                    {
                        "text": "Aynı durumun tekrarlamaması için iki taraflı testis fiksasyonu amacıyla elektif ameliyat listesine almak",
                        "is_correct": False,
                        "scenario_update": "Gereksiz bir cerrahi planlandı; ek torsiyonunda fiksasyon gerekmez.",
                        "teaching_point": "Ek torsiyonunda cerrahi yalnızca ağrısı geçmeyen nadir olgularda düşünülür."
                    },
                    {
                        "text": "Enfeksiyon olasılığına karşı iki hafta oral siprofloksasin vermek ve kontrol ultrasonografisiyle izlemek",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik gereksizdi ve çocukta bulantı yaptı.",
                        "teaching_point": "Bu tabloda enfeksiyon yoktur; antibiyotik gerekmez."
                    },
                    {
                        "text": "Çocuğu bir hafta okula göndermemek, sıcak su torbası uygulamak ve ağrı için kodeinli şurup vermek",
                        "is_correct": False,
                        "scenario_update": "Kodein çocuklarda solunum depresyonu riski nedeniyle önerilmez; sıcak uygulama ödemi artırdı.",
                        "teaching_point": "NSAİİ yeterlidir; kodein bu yaş grubunda kullanılmaz."
                    }
                ]
            }
        ]
    }
]
