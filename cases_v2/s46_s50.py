# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - S46-S50 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "S46",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "3 Yaşında",
        "gender": "Kız",
        "complaint": "Kanlı ishalin ardından başlayan aşırı halsizlik, solukluk, bacaklarda kırmızı noktalar ve idrar miktarında azalma",
        "history": "Ailesi anlatıyor: 'Bir hafta önce kramp tarzında karın ağrısı ve kanlı ishali başladı, ateşi pek olmadı. Başka bir yerde oral antibiyotik verdiler. İki gündür ishali azaldı ama dünden beri bembeyaz oldu, bacaklarında küçük kırmızı-mor noktalar çıktı, gözlerinin çevresi şişti. Son 18 saattir bezi neredeyse kuru.' İshal başlamadan önce bir çiftlik ziyaretinde çiğ süt içmiş. Tartı: 14 kg.",
        "final_diagnosis": "Tipik (STEC İlişkili) Hemolitik Üremik Sendrom",
        "disposition": "Sarı Alanda Sıkı Sıvı Dengesi, Gereksiz Trombosit Transfüzyonundan Kaçınma, Antihipertansif Tedavi ve Diyaliz Hazırlığıyla Çocuk Nefroloji-Yoğun Bakım Yatışı",
        "case_pearl": "Kanlı ishalden 5-10 gün sonra mikroanjiyopatik hemolitik anemi (şistositler, LDH artışı, Coombs negatif), trombositopeni ve akut böbrek hasarı tipik tablodur. Tedavi destekleyicidir: sıvı dengesi (insensibl kayıp + çıkış), hipertansiyon ve elektrolit kontrolü, gerekirse diyaliz. Trombosit transfüzyonu yalnızca aktif kanama veya invaziv işlem için yapılır. Antibiyotik, antimotilite ajanlar ve NSAİİ'lerden kaçınılır. Nörolojik tutulum yakından izlenir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Sıvı Durumu",
                "question": "Kanlı ishal sonrası solukluk, peteşi, ödem ve idrar azalması olan bu 3 yaşındaki çocukta ilk değerlendirmede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "İdrar azlığını dehidratasyona bağlayıp kan basıncını ölçmeden 20 mL/kg serum fizyolojik bolusunu iki kez vermek ve idrar çıkışını beklemek",
                        "is_correct": False,
                        "scenario_update": "İkinci bolus sonrası solunum hızı 40/dk'ya çıktı, oksijen satürasyonu %92'ye düştü; akciğerlerde yaygın raller duyuldu.",
                        "teaching_point": "Ödemli, hipertansif ve oligürik çocukta sıvı yüklenmesi vardır; bolus tedavisi pulmoner ödeme yol açabilir."
                    },
                    {
                        "text": "Bacaklardaki peteşiler nedeniyle olası beyin içi kanama riskini önlemek için tetkik sonuçlarını beklemeden trombosit süspansiyonu istemek ve başlanan oral antibiyotiğe devam etmek",
                        "is_correct": False,
                        "scenario_update": "Kanaması olmayan çocuğa trombosit verilmek üzereydi; değerlendirme yapılmadan transfüzyon istemi hematoloji tarafından durduruldu.",
                        "teaching_point": "Peteşi tek başına transfüzyon endikasyonu değildir; önce tanı ve klinik değerlendirme gerekir."
                    },
                    {
                        "text": "Kan basıncını, ödem ve akciğer sesleriyle sıvı yükünü, perfüzyonu, bilinci ve kanama bulgularını değerlendirip kan şekeri ve idrar çıkışını izlemek",
                        "is_correct": True,
                        "explanation": "Oligürik akut böbrek hasarında çocuk dehidrate değil sıvı yüklü olabilir; sıvı tedavisi bu ayrıma göre belirlenir. Hipertansiyon ve bilinç değişikliği ciddi tutulum bulgularıdır.",
                        "new_finding": "Vital Bulgular: Ateş 37.2°C, KTA 136/dk, SS 26/dk, TA 118/76 mmHg (yaşına göre yüksek), SpO2 %98, KDZ 2 sn. İleri derecede soluk, skleralar hafif ikterik. Göz kapaklarında ve pretibial bölgede gode bırakan ödem. Akciğerlerde bazalde hafif raller. Alt ekstremitelerde peteşiler, aktif kanama yok. Bilinç açık, irritabl. Kapiller kan şekeri 98 mg/dL. Mesane kateterinden 10 mL idrar geldi."
                    },
                    {
                        "text": "İshalin sürmemesi için loperamid başlamak, karın ağrısı için ibuprofen vermek ve ödem nedeniyle albümin infüzyonu planlamak",
                        "is_correct": False,
                        "scenario_update": "İbuprofen böbrek fonksiyonunu daha da bozdu; antimotilite ajan ve albümin tabloyu kötüleştirdi.",
                        "teaching_point": "Bu tabloda antimotilite ajanlar ve NSAİİ'ler kontrendikedir."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar Değerlendirmesi",
                "question": "Hipertansif, ödemli ve oligürik bu çocukta hangi tetkikler öncelikli olarak istenmelidir?",
                "options": [
                    {
                        "text": "Menenjit ve sepsisi dışlamak için kan kültürü alıp lomber ponksiyon yapmak, sonuçlar gelene kadar geniş spektrumlu antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "Trombositopenik çocukta lomber ponksiyon kanama riski taşıdı ve ertelendi; temel hematolojik ve renal tetkikler gecikti.",
                        "teaching_point": "Bu tabloda öncelik hemoliz, trombositopeni ve böbrek fonksiyonunun değerlendirilmesidir."
                    },
                    {
                        "text": "Hemogram, periferik yayma, LDH, direkt Coombs, böbrek fonksiyonları, elektrolitler, kan gazı, tam idrar ve dışkıda enterohemorajik E. coli tetkiki istemek",
                        "is_correct": True,
                        "explanation": "Periferik yaymada şistositler, LDH artışı ve Coombs negatifliği mikroanjiyopatik hemolizi gösterir. Potasyum, asidoz ve üre diyaliz kararını etkiler. Dışkı kültürü ve toksin tetkiki etiyolojiyi doğrular.",
                        "new_finding": "Hb 6.4 g/dL, lökosit 14.200/mm³, trombosit 36.000/mm³. Periferik yaymada bol şistosit, polikromazi. Retikülosit %6, LDH 1820 U/L, indirekt bilirubin 2.4 mg/dL, direkt Coombs negatif. BUN 138 mg/dL, kreatinin 2.7 mg/dL, K 5.9 mEq/L, Na 131 mEq/L, pH 7.28, HCO3 15 mmol/L. İdrarda hematüri ve proteinüri. Dışkı toksin PCR pozitif. PT ve aPTT normal."
                    },
                    {
                        "text": "Solukluk ve peteşiler nedeniyle akut lösemi olasılığını düşünüp acil kemik iliği aspirasyonu planlamak ve sonuç çıkana kadar sıvı ve transfüzyon kararlarını ertelemek",
                        "is_correct": False,
                        "scenario_update": "Aspirasyon için sedasyon gerekti; bu sürede potasyum yükseldi ve sıvı dengesi yönetilmedi.",
                        "teaching_point": "Periferik yayma çoğu zaman tanıyı yönlendirir; kemik iliği incelemesi atipik bulgularda düşünülür."
                    },
                    {
                        "text": "Kanlı ishal sonrası karın ağrısı nedeniyle kontrastlı batın bilgisayarlı tomografisi çekmek ve kolit komplikasyonlarını değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Kontrast madde zaten bozulmuş böbrek fonksiyonunu daha da kötüleştirdi.",
                        "teaching_point": "Akut böbrek hasarında nefrotoksik kontrast maddeden kaçınılmalıdır; karın bulgusu yoksa görüntüleme gerekmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Kanlı ishal sonrası Coombs negatif hemolitik anemi, şistositler, trombositopeni ve akut böbrek hasarı olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Otoimmün hemolitik anemi",
                        "is_correct": False,
                        "scenario_update": "Direkt Coombs negatif, şistositler var ve böbrek hasarı eşlik ediyor.",
                        "teaching_point": "Otoimmün hemolizde Coombs pozitiftir ve sferositler görülür."
                    },
                    {
                        "text": "Tipik hemolitik üremik sendrom (STEC)",
                        "is_correct": True,
                        "explanation": "Kanlı ishal sonrası mikroanjiyopatik hemolitik anemi, trombositopeni ve akut böbrek hasarı üçlüsü ile dışkıda toksin pozitifliği Shiga toksini üreten E. coli ilişkili tipik hemolitik üremik sendromu doğrular.",
                        "new_finding": "Tanı: Tipik (STEC İlişkili) Hemolitik Üremik Sendrom."
                    },
                    {
                        "text": "Trombotik trombositopenik purpura",
                        "is_correct": False,
                        "scenario_update": "Bu yaşta nadirdir; kanlı ishal öyküsü ve toksin pozitifliği tipik tabloyu destekliyor.",
                        "teaching_point": "TTP'de ADAMTS13 aktivitesi ileri derecede düşüktür; nörolojik bulgular ön plandadır."
                    },
                    {
                        "text": "Sepsise bağlı yaygın damar içi pıhtılaşma",
                        "is_correct": False,
                        "scenario_update": "PT ve aPTT normal, fibrinojen tüketimi yok, çocuk septik görünmüyor.",
                        "teaching_point": "Yaygın damar içi pıhtılaşmada koagülasyon testleri bozulur."
                    }
                ]
            },
            {
                "stage_title": "Destek Tedavisi ve Yatış",
                "question": "Bu çocuğun acil serviste tedavi planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Ödemi gidermek ve böbreği zorlamak için yüksek doz intravenöz furosemid ile birlikte 20 mL/kg serum fizyolojik bolusu vermek, idrar çıkışı başlarsa çocuğu genel serviste izlemek",
                        "is_correct": False,
                        "scenario_update": "Bolus sonrası pulmoner ödem gelişti; furosemide yanıt alınamadı ve acil diyaliz gerekti.",
                        "teaching_point": "Oligürik akut böbrek hasarında bolus sıvı yükü artırır; diüretik yanıtı sınırlıdır."
                    },
                    {
                        "text": "İlk basamak tedavi olarak acil plazmaferez ve eculizumab başlamak, sıvı dengesini yoğun bakımda sonradan düzenlemek",
                        "is_correct": False,
                        "scenario_update": "Plazmaferez için santral kateter ve uzun hazırlık gerekti; hiperkalemi ve hipertansiyon bu sürede tedavisiz kaldı.",
                        "teaching_point": "Tipik tabloda destek tedavisi esastır; plazmaferez ve eculizumab atipik veya ağır nörolojik tutulumlu olgularda düşünülür."
                    },
                    {
                        "text": "Trombositopeniyi düzeltmek için trombosit süspansiyonu vermek, enfeksiyonun sürmemesi için antibiyotiği intravenöz seftriaksonla değiştirmek ve idame sıvısı başlamak",
                        "is_correct": False,
                        "scenario_update": "Trombosit sonrası çocukta bilinç değişikliği gelişti; antibiyotik ve idame sıvısı sıvı yükünü artırdı.",
                        "teaching_point": "Gereksiz trombosit transfüzyonu mikroanjiyopatiyi ağırlaştırabilir; antibiyotik önerilmez."
                    },
                    {
                        "text": "Antibiyotiği kesmek, sıvıyı insensibl kayıp artı idrar çıkışıyla sınırlamak, hiperkalemiyi ve hipertansiyonu tedavi etmek, kanama yoksa trombosit vermemek ve diyaliz hazırlığıyla yatırmak",
                        "is_correct": True,
                        "explanation": "Sıvı yüklü oligürik çocukta sıvı kısıtlanır. Antibiyotikler toksin salınımını artırabilir. Trombosit transfüzyonu mikrotrombüsleri artırabileceğinden yalnızca kanama veya işlem için yapılır. Hiperkalemi, sıvı yüklenmesi, ağır asidoz ve üremi diyaliz endikasyonlarıdır.",
                        "new_finding": "Antibiyotik kesildi, sıvı kısıtlandı, hiperkalemi için salbutamol ve kalsiyum glukonat verildi, nifedipin ile kan basıncı kontrol edildi. Hb 6 g/dL'nin altına inince yavaş eritrosit transfüzyonu yapıldı. Çocuk nefrolojisi periton diyalizi başlattı; üç haftada böbrek fonksiyonu düzeldi."
                    }
                ]
            }
        ]
    },
    {
        "id": "S47",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "3 Haftalık",
        "gender": "Erkek",
        "complaint": "Aniden başlayan koyu yeşil kusma, karında şişlik ve beslenmeyi reddetme",
        "history": "Ailesi anlatıyor: 'Doğumdan beri sorunsuz emiyordu. Üç saat önce aniden koyu yeşil renkte kustu, sonra iki kez daha kustu. Emmeyi bıraktı, inliyor, karnı şişmeye başladı. Son birkaç saattir gaz ve kaka çıkarmadı.' Term doğmuş, mekonyumu ilk gün çıkmış. Ateş yok. Tartı: 3.8 kg.",
        "final_diagnosis": "İntestinal Malrotasyon ve Orta Bağırsak Volvulusu",
        "disposition": "Sarı Alanda Nazogastrik Dekompresyon, Damar Yolu, Sıvı Resüsitasyonu ve Geniş Spektrumlu Antibiyotik Sonrası Acil Çocuk Cerrahisi (Ladd Prosedürü)",
        "case_pearl": "Yenidoğan ve küçük bebekte safralı (yeşil) kusma, aksi kanıtlanana kadar cerrahi acildir. Orta bağırsak volvulusu saatler içinde tüm ince bağırsağın iskemisine yol açabilir. Stabil bebekte tanı acil üst gastrointestinal kontrastlı grafiyle konur; peritonit veya şok varsa görüntüleme beklenmeden ameliyata alınır. Tedavi resüsitasyon, dekompresyon, antibiyotik ve acil Ladd prosedürüdür.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Stabilizasyon",
                "question": "Koyu yeşil kusma, karın şişliği ve inlemesi olan bu 3 haftalık bebekte ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Kusmanın mama intoleransına bağlı olduğunu düşünüp hidrolize mamaya geçmek, küçük hacimlerle besleyerek iki saat gözlemlemek",
                        "is_correct": False,
                        "scenario_update": "Beslenen bebek yeniden yeşil kustu ve aspirasyon gelişti; perfüzyonu kötüleşti.",
                        "teaching_point": "Safralı kusması olan bebek beslenmez; mama değişikliği yaklaşımı yoktur."
                    },
                    {
                        "text": "Sepsis olasılığı nedeniyle önce lomber ponksiyon, kan ve idrar kültürü alıp antibiyotik başlamak, cerrahi değerlendirmeyi kültür sonuçlarından sonra planlamak",
                        "is_correct": False,
                        "scenario_update": "Lomber ponksiyon sırasında bebek yeniden kustu; cerrahi bildirim saatlerce gecikti.",
                        "teaching_point": "Safralı kusmada cerrahi değerlendirme ertelenmemelidir; sepsis tetkikleri cerrahi süreci geciktirmeden yapılır."
                    },
                    {
                        "text": "Havayolu, solunum ve perfüzyonu değerlendirip oral alımı kesmek, nazogastrik sondayla mideyi boşaltmak, damar yolu açıp sıvı vermek ve çocuk cerrahisini hemen çağırmak",
                        "is_correct": True,
                        "explanation": "Safralı kusma Treitz bağı distalinde obstrüksiyonu gösterir ve cerrahi acildir. Dekompresyon aspirasyonu önler; resüsitasyon ve erken cerrahi bildirim bağırsak canlılığı için zaman kazandırır.",
                        "new_finding": "Vital Bulgular: Ateş 37.1°C, KTA 166/dk, SS 44/dk, TA 72/42 mmHg, SpO2 %97, KDZ 3.5 sn. Bebek soluk ve inliyor. Karın distandü, epigastriumda hassasiyet; belirgin defans yok. Nazogastrik sondadan 30 mL koyu yeşil sıvı geldi. 10 mL/kg serum fizyolojik sonrası KDZ 2.5 sn. Kapiller kan şekeri 82 mg/dL. Çocuk cerrahisine haber verildi."
                    },
                    {
                        "text": "Gaz ve dışkı çıkışı olmadığı için rektal uyarı ve gliserinli fitil uygulamak, dışkılama sonrası karın şişliğinin azalmasını beklemek",
                        "is_correct": False,
                        "scenario_update": "Rektal uyarı sonrası az miktarda kanlı mukus geldi; zaman kaybedildi ve bebeğin durumu ağırlaştı.",
                        "teaching_point": "Rektal kanama bağırsak iskemisinin geç bulgusu olabilir; obstrüksiyon şüphesinde lavman veya fitil uygulanmaz."
                    }
                ]
            },
            {
                "stage_title": "Görüntüleme Kararı",
                "question": "Resüsitasyona yanıt veren, peritonit bulgusu olmayan bu bebekte hangi görüntüleme yöntemi tercih edilmelidir?",
                "options": [
                    {
                        "text": "Acil üst gastrointestinal kontrastlı grafi çekmek ve duodenojejunal bileşkenin yerini ve kontrast geçişini değerlendirmek",
                        "is_correct": True,
                        "explanation": "Stabil bebekte üst gastrointestinal kontrastlı grafi altın standarttır; duodenojejunal bileşkenin konumu ve duodenumdaki obstrüksiyon paterni tanıyı koyar. Ultrason deneyimli ellerde destekleyicidir ancak normal olması tanıyı dışlamaz.",
                        "new_finding": "Üst gastrointestinal grafi: duodenojejunal bileşke omurganın sağında yerleşmiş; kontrast duodenumun üçüncü kısmında spiral şekilde dönerek ilerliyor ve daralıyor, distale geçiş çok az."
                    },
                    {
                        "text": "Ayakta direkt batın grafisi çekmek, distal gaz görülürse obstrüksiyonu dışlayıp bebeği gözlem odasında izlemek",
                        "is_correct": False,
                        "scenario_update": "Grafide distal gaz vardı ve bebek gözleme alındı; iki saat sonra karın daha da gerildi.",
                        "teaching_point": "Direkt grafi normal veya nonspesifik olabilir; distal gaz bu tabloyu dışlamaz."
                    },
                    {
                        "text": "Bağırsak duvarını ayrıntılı değerlendirmek için intravenöz ve oral kontrastlı batın bilgisayarlı tomografisi istemek ve sonuca göre cerrahiyi çağırmak",
                        "is_correct": False,
                        "scenario_update": "Oral kontrast verilen bebek kustu ve tomografi için sedasyon gerekti; cerrahi bir saat gecikti.",
                        "teaching_point": "BT bu yaşta ilk tercih değildir ve cerrahiyi geciktirmemelidir."
                    },
                    {
                        "text": "Kolonu değerlendirmek için baryumlu kolon grafisi çekmek ve geçiş bozukluğu saptanırsa rektal biyopsi planlamak",
                        "is_correct": False,
                        "scenario_update": "Kolon grafisi çekumun yerini dolaylı gösterdi ancak duodenal obstrüksiyonu değerlendirmedi; tanı gecikti.",
                        "teaching_point": "Kolon grafisi distal obstrüksiyonlarda kullanılır; proksimal safralı kusmada üst grafi tercih edilir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Ani safralı kusma, karın distansiyonu ve üst gastrointestinal grafide sağda yerleşmiş duodenojejunal bileşke ile spiral daralma olan bu bebekte tanı nedir?",
                "options": [
                    {
                        "text": "Malrotasyon ve orta bağırsak volvulusu",
                        "is_correct": True,
                        "explanation": "Duodenojejunal bileşkenin orta hattın sağında olması rotasyon bozukluğunu, kontrastın spiral daralması ise mezenter çevresinde dönmeyi gösterir.",
                        "new_finding": "Tanı: İntestinal Malrotasyon ve Orta Bağırsak Volvulusu."
                    },
                    {
                        "text": "Nekrotizan enterokolit",
                        "is_correct": False,
                        "scenario_update": "Term ve önceden sağlıklı bebek; grafide pnömatozis yok, bulgular duodenal düzeyde.",
                        "teaching_point": "Nekrotizan enterokolit çoğunlukla prematürelerde ve beslenme sonrası görülür."
                    },
                    {
                        "text": "Duodenal web",
                        "is_correct": False,
                        "scenario_update": "Duodenojejunal bileşke yer değiştirmiş ve spiral daralma var; web sabit bir daralma yapar.",
                        "teaching_point": "Duodenal web genellikle daha erken veya daha sinsi bulgu verir ve rotasyon bozukluğu içermez."
                    },
                    {
                        "text": "Hirschsprung enterokoliti",
                        "is_correct": False,
                        "scenario_update": "Mekonyum ilk gün çıkmış ve obstrüksiyon proksimal duodenal düzeyde.",
                        "teaching_point": "Hirschsprung hastalığında distal obstrüksiyon ve mekonyum gecikmesi beklenir."
                    }
                ]
            },
            {
                "stage_title": "Cerrahi Tedavi",
                "question": "Bu bebeğin tedavisi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Bebeğin perfüzyonu tamamen normale dönene kadar 48 saat yoğun bakımda stabilize etmek, ardından laparoskopik cerrahiyi planlamak",
                        "is_correct": False,
                        "scenario_update": "Bekleme sırasında laktat yükseldi ve perfüzyon yeniden bozuldu; iskemi ilerledi.",
                        "teaching_point": "Resüsitasyon cerrahiyle eş zamanlı yürütülür; bağırsak iskemisi stabilizasyon için beklemez."
                    },
                    {
                        "text": "Görüntüleme eşliğinde kontrastlı lavmanla bağırsak dönüşünü düzeltmeye çalışmak ve başarılı olursa cerrahiden kaçınmak",
                        "is_correct": False,
                        "scenario_update": "Lavman dönmüş mezenteri etkilemedi; cerrahi gereksiz yere gecikti.",
                        "teaching_point": "Rotasyon bozukluğu ve dönme cerrahi olarak düzeltilir; görüntüleme eşliğinde redüksiyon yöntemi yoktur."
                    },
                    {
                        "text": "Nazogastrik dekompresyon ve sıvı tedavisiyle 24 saat izlemek, kusma azalırsa bebeği beslemeye başlayıp elektif cerrahiyi birkaç hafta sonraya planlamak",
                        "is_correct": False,
                        "scenario_update": "İzlemin altıncı saatinde bebekte kanlı dışkı ve şok gelişti; ameliyatta geniş bağırsak nekrozu saptandı.",
                        "teaching_point": "Bu tablo saatlerle yarışan bir cerrahi acildir; konservatif izlem kabul edilemez."
                    },
                    {
                        "text": "Resüsitasyonu sürdürüp geniş spektrumlu antibiyotik başlamak ve bebeği gecikmeden acil laparotomiye almak; detorsiyon ve Ladd prosedürünü planlamak",
                        "is_correct": True,
                        "explanation": "Acil laparotomide bağırsak saat yönünün tersine çevrilerek detorsiyon yapılır, Ladd bantları kesilir, mezenter genişletilir ve apendektomi eklenir. Erken cerrahi bağırsak kaybını ve kısa bağırsak sendromunu önler.",
                        "new_finding": "Ampisilin, gentamisin ve metronidazol başlandı. Acil laparotomide 360 derece dönmüş mezenter detorse edildi; ılık kompres sonrası bağırsaklar pembeleşti. Ladd prosedürü tamamlandı, rezeksiyon gerekmedi."
                    }
                ]
            }
        ]
    },
    {
        "id": "S48",
        "category": "👶 Yenidoğan Acilleri",
        "age": "9 Günlük",
        "gender": "Kız",
        "complaint": "Son iki gündür emmeyi bırakan, uykulu, idrarı azalan ve sararan bebek",
        "history": "Annesi anlatıyor: 'İlk bebeğim. Sadece emziriyorum ama memem çok dolmadı sanırım, bebek memeye 40-50 dakika asılı kalıyor, bırakınca ağlıyor. Son iki gündür çok uyuyor, emmek için uyandıramıyorum. Bezini günde iki kez ıslatıyor, idrarı koyu turuncu. Dün akşam biraz ateşi çıktı.' 39. haftada sezaryenle doğmuş, doğum ağırlığı 3200 g, ikinci gün taburcu edilmiş. Taburculuk sonrası hiç tartılmamış. Kusma ve ishal yok.",
        "final_diagnosis": "Yetersiz Anne Sütü Alımına Bağlı Hipernatremik Dehidratasyon",
        "disposition": "Kontrollü Sodyum Düzeltmesi ve Emzirme Desteğiyle Yenidoğan Yoğun Bakım/Servis Yatışı",
        "case_pearl": "Yalnız anne sütüyle beslenen yenidoğanda doğum ağırlığının %10'undan fazla kayıp, azalmış idrar ve letarji hipernatremik dehidratasyonu düşündürür. Hipernatremide hücre dışı hacim korunduğu için dehidratasyon derecesi olduğundan hafif görünür. Şok varsa %0.9 NaCl 10-20 mL/kg bolus verilir. Sonra serum sodyumu 48 saatte, saatte 0.5 mmol/L'yi (günde 10-12 mmol/L) aşmayacak hızda düşürülür ve sodyum 2-4 saatte bir ölçülür. Hızlı düzeltme beyin ödemi ve nöbete yol açar. Ateşli yenidoğanda sepsis de dışlanmalıdır. Anneye emzirme desteği verilir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Uykulu, az idrar yapan ve beslenme sorunu olan bu 9 günlük bebeğin ilk değerlendirmesinde ne yaparsınız?",
                "options": [
                    {
                        "text": "Sarılık nedeniyle transkutan bilirubin ölçmek ve değer fototerapi eşiğinin altındaysa emzirme sıklığını artırmalarını söyleyip ertesi gün kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Bebek taburcu edildi; gece nöbet geçirerek geri getirildi.",
                        "teaching_point": "Letarji, azalmış idrar ve emme güçlüğü olan yenidoğanda tartı, perfüzyon ve elektrolit değerlendirmesi atlanmamalıdır."
                    },
                    {
                        "text": "Havayolu, solunum ve perfüzyonu değerlendirip bebeği çıplak tartarak doğum ağırlığıyla karşılaştırmak; fontanel, cilt turgoru, glukoz ve ateşi kontrol etmek",
                        "is_correct": True,
                        "explanation": "Yenidoğanda yüzde kilo kaybı dehidratasyonun en nesnel göstergesidir. Ateş, letarji ve perfüzyon bozukluğu hem sıvı açığını hem de olası enfeksiyonu düşündürür.",
                        "new_finding": "Vital Bulgular: Ateş 37.9°C, KTA 182/dk, SS 52/dk, SpO2 %98, KDZ 3 sn. Tartı 2720 g (doğum ağırlığının %15 altında). Ön fontanel çökük, mukozalar kuru. Cilt hamurumsu kıvamda, turgor azalmış. Yüz, gövde ve uylukta sarılık. Bebek uyarana huzursuz ve tiz sesle ağlıyor, kas tonusu hafif artmış. Glukoz 62 mg/dL."
                    },
                    {
                        "text": "Ateşli yenidoğan olduğu için tartı ve ayrıntılı muayeneyi atlayıp hemen lomber ponksiyon yaparak ampisilin ve gentamisin başlamak",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik başlandı ancak sıvı açığı ve elektrolit bozukluğu fark edilmedi; bebek giderek uykulu hale geldi.",
                        "teaching_point": "Sepsis değerlendirmesi gerekir, ancak perfüzyon, kilo kaybı ve elektrolitler aynı anda değerlendirilmeden yönetim eksik kalır."
                    },
                    {
                        "text": "Bebeği hemen memeye vermesini istemek ve emme gözlemi yapmak, yeterli emerse ek tetkik gerekmeden mama takviyesiyle evden izlemeyi planlamak",
                        "is_correct": False,
                        "scenario_update": "Bebek memeyi zayıf emdi ve uyuyakaldı; yarım saat sonra bilinç düzeyi daha da azaldı.",
                        "teaching_point": "Letarjik ve perfüzyonu bozuk bebekte ağızdan beslenme denemesi ilk adım olamaz; önce stabilizasyon ve tetkik gerekir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Bu bebekte hangi tetkikler öncelikli olarak istenmelidir?",
                "options": [
                    {
                        "text": "Serum elektrolitleri, glukoz, üre, kreatinin, kan gazı ve bilirubin düzeyini istemek; ateş nedeniyle kan ve kateter idrar kültürünü de almak",
                        "is_correct": True,
                        "explanation": "Elektrolitler sıvı tedavisinin türünü ve hızını belirler. Ateşli yenidoğanda dehidratasyon ateşi olsa bile kültürler alınmalı ve klinik duruma göre sepsis tedavisi değerlendirilmelidir.",
                        "new_finding": "Na 163 mmol/L, K 4.9 mmol/L, Cl 129 mmol/L, glukoz 64 mg/dL, üre 96 mg/dL, kreatinin 1.2 mg/dL. Kan gazı: pH 7.29, HCO3 17 mmol/L. Total bilirubin 17.6 mg/dL, direkt 0.6 mg/dL. Tam idrar dansitesi 1.030, lökosit yok, nitrit negatif. Kan ve idrar kültürü gönderildi."
                    },
                    {
                        "text": "Yalnız tam kan sayımı, CRP ve kan kültürü istemek; sonuçlar normalse sorunun yetersiz emzirme olduğunu kabul edip mamayla beslemeye başlamak",
                        "is_correct": False,
                        "scenario_update": "Hemogram ve CRP normal geldi; elektrolitler bakılmadığı için ağır bozukluk fark edilmedi ve mama yeterli sıvıyı sağlamadı.",
                        "teaching_point": "Dehidratasyonlu yenidoğanda serum sodyumu bilinmeden güvenli sıvı tedavisi planlanamaz."
                    },
                    {
                        "text": "Bilirubin yüksekliği ön planda olduğundan yalnızca total ve direkt bilirubin, kan grubu ve direkt Coombs istemek ve fototerapiye başlamak",
                        "is_correct": False,
                        "scenario_update": "Fototerapi başlandı; buharlaşma kayıpları arttı ve bebeğin idrar çıkışı daha da azaldı.",
                        "teaching_point": "Sarılık bu tabloda yetersiz alımın sonucudur; fototerapi gerekse bile önce sıvı-elektrolit durumu belirlenmelidir."
                    },
                    {
                        "text": "Nöbet riski nedeniyle önce kraniyal ultrasonografi ve elektroensefalografi istemek, sonuçları gelene dek ağızdan beslenmeyi sürdürmek",
                        "is_correct": False,
                        "scenario_update": "Kraniyal ultrasonografi normaldi; laboratuvar beklenmeden yapılan görüntüleme süresince bebek beslenemedi.",
                        "teaching_point": "Huzursuzluk ve tonus artışı metabolik bir bozukluğun bulgusu olabilir; önce elektrolit ve glukoz değerlendirilir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik ve laboratuvar bulgularına göre en olası tanınız nedir?",
                "options": [
                    {
                        "text": "Tuz kaybettiren konjenital adrenal hiperplazi",
                        "is_correct": False,
                        "scenario_update": "Sodyum yüksek, potasyum normaldi ve genital yapı normaldi.",
                        "teaching_point": "Tuz kaybında hiponatremi ve hiperkalemi beklenir."
                    },
                    {
                        "text": "Santral diabetes insipidus",
                        "is_correct": False,
                        "scenario_update": "İdrar yoğun (dansite 1.030) ve azdı.",
                        "teaching_point": "Diabetes insipidusta hipernatremiye rağmen idrar dilüe ve boldur."
                    },
                    {
                        "text": "Geç başlangıçlı neonatal sepsis",
                        "is_correct": False,
                        "scenario_update": "Kültürler sonradan negatif geldi; tabloyu kilo kaybı ve yetersiz alım açıklıyordu.",
                        "teaching_point": "Sepsis dışlanırken, %15 kilo kaybı ve hipernatremi yetersiz beslenmeyi gösterir."
                    },
                    {
                        "text": "Yetersiz anne sütü alımına bağlı hipernatremik dehidratasyon",
                        "is_correct": True,
                        "explanation": "Yalnız anne sütüyle beslenen bebekte %15 kilo kaybı, azalmış idrar, yoğun idrar ve serum sodyumunun 163 mmol/L olması yetersiz alıma bağlı hipernatremik dehidratasyonu gösterir.",
                        "new_finding": "Tanı: Yetersiz anne sütü alımına bağlı hipernatremik dehidratasyon."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış Planı",
                "question": "Sodyum 163 mmol/L olan bu bebekte sıvı tedavisi nasıl planlanmalıdır?",
                "options": [
                    {
                        "text": "Sodyumu hızla normale döndürmek için açığın tamamını ilk 24 saatte %5 dekstroz veya %0.2 NaCl ile yerine koymak ve ertesi sabah kontrol etmek",
                        "is_correct": False,
                        "scenario_update": "Sodyum 12 saatte 147 mmol/L'ye indi; bebek nöbet geçirdi ve beyin ödemi gelişti.",
                        "teaching_point": "Hipotonik sıvıyla hızlı düzeltme beyin ödemine neden olur; sodyum düşüşü saatte 0.5 mmol/L'yi aşmamalı ve sık izlenmelidir."
                    },
                    {
                        "text": "Sodyumu hızla düşürmek için %3 NaCl yerine yalnızca ağızdan bol su verilmesini önermek, emzirmeyi sürdürüp 12 saat sonra sodyum ölçmek",
                        "is_correct": False,
                        "scenario_update": "Ağızdan verilen su yenidoğanda kontrolsüz sodyum düşüşü ve kusmaya yol açtı.",
                        "teaching_point": "Yenidoğana saf su verilmez; letarjik bebekte kontrollü intravenöz düzeltme gerekir."
                    },
                    {
                        "text": "Bebeği yalnızca mamayla beslemeye geçirip anne sütünü kesmek ve sıvıyı ağızdan vererek servis izlemiyle günlük elektrolit bakmak",
                        "is_correct": False,
                        "scenario_update": "Letarjik bebek mamayı yeterince alamadı ve günlük ölçüm sodyumdaki değişimi yakalamakta yetersiz kaldı.",
                        "teaching_point": "Emzirmenin kesilmesi gerekmez, anne desteklenmelidir; bu ağırlıkta IV tedavi ve 2-4 saatte bir sodyum izlemi gerekir."
                    },
                    {
                        "text": "Perfüzyon bozukluğu için %0.9 NaCl 10-20 mL/kg bolus vermek, ardından açığı 48 saate yayarak sodyumu 2-4 saatte bir ölçüp emzirme desteği planlamak",
                        "is_correct": True,
                        "explanation": "Önce dolaşım düzeltilir, ardından sodyumun yavaş düşmesi sağlanır. Emzirme danışmanlığı, gerekirse sağılmış süt veya ek gıdayla beslenme yeniden düzenlenir.",
                        "new_finding": "Bolus sonrası KDZ 2 sn'ye indi. 48 saatte sodyum 163'ten 141 mmol/L'ye kontrollü biçimde düştü, nöbet olmadı. Kültürler negatif geldi. Emzirme desteğiyle bebek günde 40 g almaya başladı ve beşinci gün taburcu edildi."
                    }
                ]
            }
        ]
    },
    {
        "id": "S49",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "20 Aylık",
        "gender": "Kız",
        "complaint": "İki gündür ishal ve kusma; son üç saatte ateşsiz iki kez kasılma nöbeti",
        "history": "Annesi anlatıyor: 'İki gündür günde 5-6 kez sulu ishal oluyor, dün üç kez kustu, bugün kusması azaldı. Ateşi hiç olmadı. Bugün öğlen ve az önce iki kez gözleri kaydı, kolları bacakları kasılıp titredi, bir dakika kadar sürdü. Arada kendine geldi, beni tanıdı, oyuncağıyla oynadı.' Kreşte birkaç çocukta ishal varmış. Daha önce nöbet öyküsü yok. Gelişimi normal. Aile öyküsünde epilepsi yok. Evde ilaç, kimyasal veya düşme öyküsü yok.",
        "final_diagnosis": "Hafif Gastroenteritle İlişkili Benign Afebril Konvülziyon (Norovirüs)",
        "disposition": "Sarı Alanda 24 Saatlik Gözlem ve Ağızdan Rehidratasyon Sonrası Antiepileptiksiz Taburculuk",
        "case_pearl": "Daha önce sağlıklı, 6 ay-3 yaş arası çocukta hafif gastroenteritin 1-5. günlerinde ortaya çıkan, ateşsiz, kısa ve kümelenme eğilimli jeneralize nöbetler benign bir tablodur. En sık rotavirüs ve norovirüs sorumludur. Elektrolitler, glukoz ve nörolojik muayene normaldir; BOS ve görüntüleme gerekmez. Nöbetler 24 saat içinde tekrarlayabilir. Uzun süreli antiepileptik gerekmez, prognoz mükemmeldir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "İshal sırasında iki kez ateşsiz nöbet geçiren ve şu an uyanık olan bu çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Nöbet tekrar riskini azaltmak için muayeneden önce rektal diazepam uygulamak ve çocuğu sakinleştikten sonra değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Nöbet geçirmeyen çocuğa diazepam verildi; uykulu hale geldi ve nörolojik muayene yapılamadı.",
                        "teaching_point": "Aktif nöbet yokken benzodiazepin verilmez; profilaktik doz nörolojik değerlendirmeyi bozar."
                    },
                    {
                        "text": "Havayolu ve vital bulguları değerlendirip parmak ucu glukozu ölçmek, dehidratasyon derecesini belirlemek ve ayrıntılı nörolojik muayene yapmak",
                        "is_correct": True,
                        "explanation": "Ateşsiz nöbette glukoz ve elektrolit bozuklukları düzeltilebilir nedenlerdir. Dehidratasyon ve nörolojik muayene ileri tetkik ihtiyacını belirler.",
                        "new_finding": "Vital Bulgular: Ateş 36.9°C, KTA 124/dk, SS 26/dk, SpO2 %99, TA 94/58 mmHg, KDZ 2 sn. Bilinç açık, annesini tanıyor, oyuncağa uzanıyor. Mukozalar hafif kuru, göz yaşı var. Fontanel kapalı, ense sertliği yok, pupiller izokorik, lateralizan bulgu yok, tonus ve refleksler normal. Karın yumuşak, bağırsak sesleri artmış. Glukoz 92 mg/dL."
                    },
                    {
                        "text": "Ateşsiz ilk nöbet olduğu için hemen nöroloji konsültasyonu istemek ve konsültan gelene kadar çocuğu aç bırakıp herhangi bir sıvı vermemek",
                        "is_correct": False,
                        "scenario_update": "Konsültasyon iki saat sürdü; aç bırakılan çocuk huzursuzlandı ve dehidratasyonu arttı.",
                        "teaching_point": "Konsültasyon beklenirken temel acil değerlendirme ve sıvı ihtiyacı ihmal edilmemelidir."
                    },
                    {
                        "text": "Nöbetler ishal sırasında olduğu için tabloyu dehidratasyona bağlayıp muayene etmeden 20 mL/kg serum fizyolojik bolus başlatmak",
                        "is_correct": False,
                        "scenario_update": "Bolus verildi ancak çocuğun dolaşımı zaten iyiydi; glukoz ve nörolojik durum değerlendirilmeden tedavi başlanmış oldu.",
                        "teaching_point": "Perfüzyonu normal ve hafif dehidrate çocukta bolus gerekmez; önce değerlendirme yapılır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Bilinci açık ve nörolojik muayenesi normal olan bu çocukta hangi tetkik yaklaşımı uygundur?",
                "options": [
                    {
                        "text": "Ateşsiz tekrarlayan nöbet nedeniyle santral sinir sistemi enfeksiyonunu dışlamak için lomber ponksiyon yapmak ve BOS sonuçlarını beklemek",
                        "is_correct": False,
                        "scenario_update": "BOS normal geldi; ponksiyon sonrası çocuk uzun süre ağladı ve kustu.",
                        "teaching_point": "Ateşsiz, bilinci açık, meningeal bulgusu olmayan çocukta lomber ponksiyon endike değildir."
                    },
                    {
                        "text": "Serum sodyum, kalsiyum, magnezyum, glukoz ve kan gazı istemek; dışkıda viral antijen bakmak, görüntüleme veya BOS planlamamak",
                        "is_correct": True,
                        "explanation": "Elektrolit ve glukoz bozuklukları dışlanmalıdır. Normal muayenede görüntüleme ve BOS yönetimi değiştirmez. Dışkıda viral etkenin gösterilmesi tanıyı destekler.",
                        "new_finding": "Na 138 mmol/L, K 4.1 mmol/L, Ca 9.5 mg/dL, Mg 2.0 mg/dL, glukoz 90 mg/dL, kan gazı pH 7.36, HCO3 21 mmol/L. Dışkıda norovirüs antijeni pozitif, rotavirüs negatif."
                    },
                    {
                        "text": "İkinci nöbet nedeniyle yapısal lezyonu dışlamak için acil kontrastsız beyin tomografisi çekmek, normalse elektrolitleri istemek",
                        "is_correct": False,
                        "scenario_update": "Tomografi normal geldi; çocuk gereksiz radyasyon aldı ve sedasyon gerekti.",
                        "teaching_point": "Nörolojik muayenesi normal, nöbet sonrası tam düzelen çocukta acil görüntüleme önerilmez."
                    },
                    {
                        "text": "Acil elektroensefalografi istemek ve epileptiform aktivite saptanırsa beklemeden uzun süreli antiepileptik tedavi planlamak",
                        "is_correct": False,
                        "scenario_update": "Acil EEG normal geldi; ilerleyen saatlerde yapılan EEG yönetimi değiştirmedi.",
                        "teaching_point": "Bu tabloda acil EEG yönetimi değiştirmez; elektrolit ve glukoz değerlendirmesi önceliklidir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik ve laboratuvar bulgularına göre en olası tanınız nedir?",
                "options": [
                    {
                        "text": "Hiponatremik nöbet",
                        "is_correct": False,
                        "scenario_update": "Serum sodyumu 138 mmol/L ile normaldi.",
                        "teaching_point": "Hiponatremik nöbet genellikle sodyum 125 mmol/L'nin altında görülür."
                    },
                    {
                        "text": "Basit febril konvülziyon",
                        "is_correct": False,
                        "scenario_update": "Hastalık boyunca ateş hiç ölçülmemişti.",
                        "teaching_point": "Febril konvülziyon tanısı için nöbet sırasında veya öncesinde ateş olmalıdır."
                    },
                    {
                        "text": "Hafif gastroenteritle ilişkili benign afebril konvülziyon",
                        "is_correct": True,
                        "explanation": "Hafif viral gastroenterit sırasında ateşsiz, kısa, kümelenen jeneralize nöbetler, normal elektrolitler ve normal nörolojik muayene bu tanıyı gösterir.",
                        "new_finding": "Tanı: Hafif gastroenteritle ilişkili benign afebril konvülziyon (norovirüs)."
                    },
                    {
                        "text": "Viral ensefalit",
                        "is_correct": False,
                        "scenario_update": "Ateş, bilinç değişikliği ve fokal bulgu yoktu; nöbetler arasında çocuk tamamen normaldi.",
                        "teaching_point": "Ensefalitte ateş, uzamış bilinç değişikliği ve fokal bulgular beklenir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve İzlem Planı",
                "question": "Bu çocuk için en uygun tedavi ve izlem planı hangisidir?",
                "options": [
                    {
                        "text": "İki nöbet geçirdiği için levetirasetam yüklemesi yapıp altı ay süreyle idame tedaviyle taburcu etmek ve çocuk nörolojiye yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk gereksiz yere uzun süreli antiepileptik aldı; ilaçla davranış değişiklikleri gelişti.",
                        "teaching_point": "Bu benign tabloda uzun süreli antiepileptik endikasyonu yoktur."
                    },
                    {
                        "text": "Ağızdan rehidratasyonla 24 saat gözlemde tutmak; 5 dakikayı aşan nöbette benzodiazepin vermek ve uzun süreli antiepileptik başlamadan taburcu etmek",
                        "is_correct": True,
                        "explanation": "Nöbetler genellikle ilk 24 saat içinde kümelenir; gözlem bu dönemi kapsamalıdır. Nöbetler kısa sürer ve genellikle tedavi gerekmez. Prognoz mükemmeldir ve epilepsi riski artmaz.",
                        "new_finding": "Gözlemde gece bir kez 40 saniye süren kendiliğinden geçen nöbet oldu. Ağızdan rehidratasyon başarılıydı. 24. saatte nöbetsiz, iyi beslenen çocuk ailesine bilgi verilerek taburcu edildi."
                    },
                    {
                        "text": "Nöbetler kendiliğinden geçtiği ve elektrolitler normal olduğu için gözlem gerekmeden ağızdan rehidratasyon önerileriyle hemen taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk eve gittikten dört saat sonra arka arkaya iki nöbet geçirdi ve aile panikle yeniden başvurdu.",
                        "teaching_point": "Nöbetler 24 saat içinde kümelenme eğilimindedir; bu dönemde gözlem ailenin güvenliği açısından önerilir."
                    },
                    {
                        "text": "Her nöbetten sonra fenobarbital 20 mg/kg yükleme yapmak ve nöbetler kesilene kadar intravenöz idame dozla yoğun bakımda izlemek",
                        "is_correct": False,
                        "scenario_update": "Fenobarbital sonrası çocuk derin uykuya daldı, solunum izlemi gerekti ve beslenme gecikti.",
                        "teaching_point": "Kısa süreli kendiliğinden geçen nöbetler yükleme dozu antiepileptik gerektirmez; sedasyon riski yararından fazladır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S50",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "4 Aylık",
        "gender": "Erkek",
        "complaint": "Sağ kasıkta aniden beliren, içeri girmeyen sert şişlik ve durdurulamayan ağlama",
        "history": "Ailesi anlatıyor: 'İki saat önce bezini değiştirirken sağ kasığında ceviz büyüklüğünde sert bir şişlik fark ettik. Doğduğundan beri ağladığında kasığında çıkıp yatınca kaybolan bir kabarıklık oluyordu, doktora göstermeyi düşünüyorduk. Bu kez geri gitmedi. Elle bastırınca çok ağlıyor. Yarım saattir sakinleşmiyor, bir kez süt kustu.' 34. haftada prematüre doğmuş. Ateş yok. Tartı: 6.5 kg.",
        "final_diagnosis": "İnkarsere Sağ İndirekt İnguinal Herni (Strangülasyon Bulgusu Olmayan)",
        "disposition": "Sarı Alanda Analjezi ve Sedasyonla Nazik Manuel Redüksiyon, Başarı Sonrası 24-48 Saat İçinde Cerrahi Onarım İçin Çocuk Cerrahisine Yatış",
        "case_pearl": "Bebeklerde, özellikle prematürelerde inguinal kanalın kapanmaması nedeniyle bağırsak sıkışma riski yüksektir. Ağrılı, sert, geri itilemeyen kasık şişliği inkarserasyonu düşündürür. Strangülasyon bulguları (cilt renk değişikliği, ödem, peritonit, kanlı dışkı, sepsis) yoksa analjezi ve sedasyon altında nazik manuel redüksiyon ilk tedavidir ve çoğunlukla başarılıdır. Başarılı redüksiyon sonrası doku ödemi gerilediğinde, nüks riski nedeniyle 24-48 saat içinde cerrahi onarım yapılır. Başarısız redüksiyon veya strangülasyon acil cerrahi gerektirir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Kasık Muayenesi",
                "question": "Sağ kasıkta içeri girmeyen ağrılı şişliği olan bu 4 aylık bebekte muayenede neyi değerlendirirsiniz?",
                "options": [
                    {
                        "text": "Durdurulamayan ağlamanın infantil kolik olabileceğini düşünüp bebeği kucakta sakinleştirmek, şişlik bir saat içinde kendiliğinden kaybolursa aileye poliklinik randevusu vermek",
                        "is_correct": False,
                        "scenario_update": "Bir saat sonra şişlik hâlâ yerindeydi ve bebek ikinci kez kustu.",
                        "teaching_point": "Ağrılı, geri gitmeyen kasık şişliği acil değerlendirme gerektirir; beklemek iskemi riskini artırır."
                    },
                    {
                        "text": "Analjezi vermeden ve muayene etmeden şişliği hemen güçlü elle bastırarak içeri itmeye çalışmak ve birkaç kez yinelemek",
                        "is_correct": False,
                        "scenario_update": "Zorlamayla bebek çok ağladı, karın içi basınç arttı ve şişlik daha da gerildi.",
                        "teaching_point": "Redüksiyon öncesi değerlendirme, analjezi ve sedasyon gerekir; kaba ve tekrarlayan girişim doku hasarına yol açar."
                    },
                    {
                        "text": "Şişliği sıvı birikimi kabul edip steril iğneyle aspirasyon yapmak ve aspirasyon sonrası şişlik küçülürse bebeği taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Aspirasyon planlanırken transilüminasyonun negatif olduğu fark edildi; iğneyle bağırsak yaralanması riski doğdu.",
                        "teaching_point": "Kasık şişliğine asla iğneyle girilmez; transilüminasyon pozitifliği bile bağırsak içeriğini tam dışlamaz."
                    },
                    {
                        "text": "Vital bulgular ve perfüzyonu değerlendirmek; şişliğin kıvamını, hassasiyetini, üzerindeki cilt rengini, testisin konumunu, transilüminasyonu ve karında obstrüksiyon bulgularını incelemek",
                        "is_correct": True,
                        "explanation": "Cilt renk değişikliği, ödem ve toksik görünüm iskemiyi düşündürür. Testis konumu ve transilüminasyon kordon kisti, hidrosel ve inmemiş testis torsiyonunu ayırır. Distansiyon ve safralı kusma obstrüksiyonu gösterir.",
                        "new_finding": "Vital Bulgular: Ateş 37.3°C, KTA 162/dk, SS 40/dk, SpO2 %99, KDZ 2 sn. Bebek huzursuz ama iyi görünümlü. Sağ inguinal kanaldan skrotuma uzanan 3x2 cm, sert, hassas, geri itilemeyen şişlik; üzerindeki cilt rengi normal, ödemsiz. Transilüminasyon negatif. Sağ testis skrotumda ayrı olarak palpe ediliyor. Karın hafif distandü, yumuşak; bağırsak sesleri normal. Bezde kan yok."
                    }
                ]
            },
            {
                "stage_title": "Hazırlık ve Görüntüleme Kararı",
                "question": "Cilt rengi normal, iyi görünümlü, peritonit bulgusu olmayan bu bebekte sonraki adım nedir?",
                "options": [
                    {
                        "text": "Bağırsak tıkanıklığını değerlendirmek için kontrastlı batın bilgisayarlı tomografisi istemek ve sonuç gelene kadar bebeği beslemeye devam etmek",
                        "is_correct": False,
                        "scenario_update": "Tomografi için sedasyon gerekti ve beslenen bebek kustu; işlemler gecikti.",
                        "teaching_point": "Kasık şişliğinde BT gereksizdir; olası girişim için bebek aç tutulur."
                    },
                    {
                        "text": "Ayakta direkt batın grafisi çekmek, hava-sıvı seviyesi yoksa redüksiyon denemeden bebeği servise yatırıp izlemek",
                        "is_correct": False,
                        "scenario_update": "Grafi nonspesifikti; redüksiyon ertelendikçe kasıktaki şişlik gerginleşti.",
                        "teaching_point": "Normal grafi sıkışmayı dışlamaz; kontrendikasyon yoksa redüksiyon geciktirilmemelidir."
                    },
                    {
                        "text": "Cilt rengi normal ve strangülasyon bulgusu olmadığı için bebeği redüksiyon denemeden aileyle birlikte taburcu edip birkaç hafta içinde elektif cerrahi randevusu vermek",
                        "is_correct": False,
                        "scenario_update": "Eve gönderilmek üzere olan bebekte sıkışma sürüyordu; iskemi riski göz ardı edildi.",
                        "teaching_point": "Sıkışmış bağırsak redükte edilmeden bebek taburcu edilmez."
                    },
                    {
                        "text": "Oral alımı kesip damar yolu açmak, analjezi ve sedasyon hazırlığı yapıp çocuk cerrahisine haber vermek; tanı net değilse ultrason yaptırmak",
                        "is_correct": True,
                        "explanation": "Analjezi ve sedasyon kas gevşemesini sağlayarak redüksiyon başarısını artırır. Olası cerrahi için aç tutulur. Muayene tanısal değilse ultrason kanal içindeki içeriği ve kanlanmayı gösterir.",
                        "new_finding": "Damar yolu açıldı, intranazal fentanil ve ardından intravenöz midazolam verildi. Çocuk cerrahisi bilgilendirildi. Yatak başı ultrasonda sağ inguinal kanalda peristaltizmi azalmış bağırsak ansı, duvarında kanlanma korunmuş; serbest sıvı yok."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Doğumdan beri ağlayınca çıkan, şimdi sert, hassas ve geri itilemeyen, transilüminasyon negatif, testisi ayrı palpe edilen ve cilt bulgusu olmayan kasık şişliği olan bu bebekte tanı nedir?",
                "options": [
                    {
                        "text": "İnguinal lenfadenit",
                        "is_correct": False,
                        "scenario_update": "Şişlik inguinal kanal boyunca skrotuma uzanıyor ve bağırsak içeriyor; ateş ve cilt bulgusu yok.",
                        "teaching_point": "Lenfadenit kanal dışında, yüzeyel ve hareketli bir kitle olarak ele gelir."
                    },
                    {
                        "text": "İnmemiş testis torsiyonu",
                        "is_correct": False,
                        "scenario_update": "Sağ testis skrotumda ayrı olarak palpe ediliyor.",
                        "teaching_point": "Boş skrotumla birlikte kasıkta hassas kitle inmemiş testis torsiyonunu düşündürür."
                    },
                    {
                        "text": "İnkarsere sağ indirekt inguinal herni",
                        "is_correct": True,
                        "explanation": "Daha önce redükte olan kasık şişliğinin geri itilememesi, hassasiyet ve ultrasonda kanalda bağırsak ansı inkarserasyonu gösterir. Cilt bulgusu olmaması ve korunmuş kanlanma strangülasyon lehine değildir.",
                        "new_finding": "Tanı: İnkarsere Sağ İndirekt İnguinal Herni (strangülasyon bulgusu yok)."
                    },
                    {
                        "text": "Akut kordon kisti (hidrosel)",
                        "is_correct": False,
                        "scenario_update": "Transilüminasyon negatif, şişlik ağrılı ve ultrasonda bağırsak ansı izlendi.",
                        "teaching_point": "Hidrosel ve kordon kisti genellikle ağrısız ve transilüminasyon pozitiftir."
                    }
                ]
            },
            {
                "stage_title": "Redüksiyon ve Cerrahi Zamanlaması",
                "question": "Analjezi ve sedasyon altındaki bu bebekte tedavi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Redüksiyon sonrası bebeği aynı gün taburcu edip onarımı bebek bir yaşına gelince planlamak, aileye bandaj kullanmasını önermek",
                        "is_correct": False,
                        "scenario_update": "Üç hafta sonra yeniden sıkışma gelişti; bu kez cilt renk değişikliğiyle başvurdu.",
                        "teaching_point": "Sıkışma öyküsü olan bebekte nüks riski yüksektir; onarım birkaç gün içinde yapılır ve bandaj önerilmez."
                    },
                    {
                        "text": "Bebeğin bacaklarını fleksiyona alıp kanal girişini sabitleyerek nazik ve sürekli basıyla manuel redüksiyon yapmak; başarılıysa gözleyip 24-48 saat içinde cerrahi onarım planlamak",
                        "is_correct": True,
                        "explanation": "Sedasyon altında nazik ve sürekli bası çoğu olguda başarılıdır. Redüksiyon sonrası kusma, distansiyon ve peritonit izlenir. Doku ödemi gerilediğinde, nüks ve yeniden sıkışma riski nedeniyle onarım ertelenmeden yapılır. Başarısızlıkta acil cerrahi gerekir.",
                        "new_finding": "Nazik sürekli bası ile bağırsak ansı hafif bir kayma hissiyle karın içine döndü. Bebek sakinleşti ve uykuya daldı. Gözlemde kusma ve distansiyon olmadı; 36. saatte açık herniotomi yapıldı ve ertesi gün taburcu edildi."
                    },
                    {
                        "text": "Prematüre bebekte nüks riski yüksek olduğu için redüksiyon denemeden doğrudan acil cerrahiye almak, ödemli dokuda onarım yapmak ve karşı tarafı rutin olarak eksplore etmek",
                        "is_correct": False,
                        "scenario_update": "Ödemli dokuda acil cerrahi komplikasyon riskini artırdı; redüksiyon büyük olasılıkla başarılı olacaktı.",
                        "teaching_point": "Strangülasyon yoksa önce redüksiyon denenir; ödem gerilediğinde yapılan cerrahi daha güvenlidir."
                    },
                    {
                        "text": "Redüksiyonu kolaylaştırmak için bebeği Trendelenburg pozisyonunda bırakıp şişliğe buz uygulamak ve dört saat kendiliğinden gerilemesini beklemek",
                        "is_correct": False,
                        "scenario_update": "Dört saatlik beklemede şişlik gerilemedi; buz uygulaması bebekte soğuk hasarı riski yarattı ve iskemi süresi uzadı.",
                        "teaching_point": "Kendiliğinden gerileme beklenmez; analjezi-sedasyon altında aktif redüksiyon yapılır. Bebekte buz uygulaması önerilmez."
                    }
                ]
            }
        ]
    }
]
