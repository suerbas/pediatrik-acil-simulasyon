# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - Y46-Y50 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "Y46",
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
        "id": "Y47",
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
        "id": "Y48",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "13 Yaşında",
        "gender": "Erkek",
        "complaint": "Üç saattir süren ani başlangıçlı sağ alt karın ve kasık ağrısı, bulantı ve iki kez kusma",
        "history": "Kendisi anlatıyor: 'Sabah uykudan ağrıyla uyandım. Ağrı karnımın sağ alt tarafında ve kasığımda, çok şiddetli. İki kez kustum. Yürürken iki büklüm oluyorum.' Triyajda karın ağrısı olarak değerlendirilmiş; genital bölge sorgulanmamış. Ayrıntılı sorgulamada geçen ay benzer ama birkaç dakikada geçen bir ağrısı olduğu öğrenildi. Ateş, idrar yanması ve travma yok. Tartı: 48 kg.",
        "final_diagnosis": "Sağ Testis Torsiyonu",
        "disposition": "Sarı Alanda Oral Alımın Kesilmesi, Analjezi ve Görüntüleme İçin Gecikmeden Acil Skrotal Eksplorasyon (Detorsiyon ve Bilateral Orşiopeksi)",
        "case_pearl": "Karın ağrısı olan her erkek çocukta genital muayene yapılmalıdır; adölesanlar skrotal ağrıyı utanma nedeniyle karın ağrısı olarak tarif edebilir. Ani başlangıç, kusma, yüksek yerleşimli ve yatay duran testis ile kremaster refleksinin kaybı torsiyonu düşündürür. Testis kurtarılma oranı ilk 6 saatte %90'ın üzerindedir. Klinik şüphe yüksekse Doppler ultrason beklenmeden cerrahiye gidilir. Manuel detorsiyon geçici bir önlemdir, cerrahinin yerini tutmaz.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Genital Muayene",
                "question": "Ani başlangıçlı sağ alt karın ve kasık ağrısıyla gelen bu 13 yaşındaki erkek çocukta muayenede neye öncelik verirsiniz?",
                "options": [
                    {
                        "text": "Karın muayenesine ek olarak mahremiyeti sağlayıp skrotumu incelemek; testislerin konumu, duruş ekseni, hassasiyeti, skrotal ödem ve kremaster refleksini değerlendirmek",
                        "is_correct": True,
                        "explanation": "Kasık ve alt karın ağrısının kaynağı skrotum olabilir. Yüksek yerleşimli, yatay duran ve hassas testis ile kremaster refleksinin yokluğu acil cerrahi tabloyu düşündürür.",
                        "new_finding": "Vital Bulgular: Ateş 37.0°C, KTA 108/dk, SS 20/dk, TA 112/70 mmHg. Karında sağ alt kadranda hafif hassasiyet, defans ve rebound yok. Sağ hemiskrotum ödemli ve hafif eritemli; sağ testis yukarı çekilmiş, yatay duruyor ve dokunmakla çok hassas. Sağ kremaster refleksi alınamıyor; testisi kaldırmak ağrıyı azaltmıyor. Sol testis normal."
                    },
                    {
                        "text": "Triyaj notuna dayanarak muayeneyi karınla sınırlı tutmak, sağ alt kadran hassasiyeti nedeniyle batın ultrasonu isteyip cerrahi konsültasyonu sonuca göre planlamak",
                        "is_correct": False,
                        "scenario_update": "Batın ultrasonu normal geldi; genital muayene yapılmadan iki saat geçti.",
                        "teaching_point": "Karın ağrılı erkek çocukta genital muayene atlanmamalıdır; skrotal acil karın ağrısı olarak kendini gösterebilir."
                    },
                    {
                        "text": "İdrar yolu enfeksiyonu veya taş olasılığına karşı önce tam idrar tetkiki ve böbrek ultrasonu istemek, ağrı için intravenöz parasetamol verip sonuçları beklemek",
                        "is_correct": False,
                        "scenario_update": "İdrar ve böbrek ultrasonu normal geldi; skrotal muayene yapılmadan değerli zaman kaybedildi.",
                        "teaching_point": "Normal idrar tetkiki skrotal patolojiyi dışlamaz."
                    },
                    {
                        "text": "Ağrının gaz ve kabızlığa bağlı olduğunu düşünüp lavman uygulamak ve rahatladıktan sonra yeniden muayene etmek",
                        "is_correct": False,
                        "scenario_update": "Lavman sonrası ağrı değişmedi; muayene bir saat ertelendi.",
                        "teaching_point": "Ani başlangıçlı şiddetli ağrı ve kusma fonksiyonel bir nedenle açıklanmamalıdır."
                    }
                ]
            },
            {
                "stage_title": "Acil Karar ve Görüntüleme",
                "question": "Yatay duran, yüksek yerleşimli hassas testisi ve kayıp kremaster refleksi olan bu çocukta sonraki adım nedir?",
                "options": [
                    {
                        "text": "Acil serviste testisi içten dışa çevirerek manuel düzeltme denemek, ağrı geçerse çocuğu taburcu edip elektif cerrahi randevusu vermek",
                        "is_correct": False,
                        "scenario_update": "Manuel girişim sonrası ağrı kısmen azaldı ancak çocuk taburcu edildikten sonra ağrı tekrarladı.",
                        "teaching_point": "Manuel girişim cerrahiye kadar geçici bir önlemdir; başarılı görünse bile acil cerrahi gerekir."
                    },
                    {
                        "text": "Skrotal ödem ve eritem nedeniyle epididimit olasılığını düşünüp idrar kültürü alarak oral antibiyotik başlamak, skrotal destek ve soğuk uygulama önerip 48 saat sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Çocuk eve gönderildi; ağrı sürdü ve ertesi gün başvurduğunda testis kurtarılamadı.",
                        "teaching_point": "Ani başlangıç, kusma ve kayıp kremaster refleksi epididimitten çok iskemik tabloyu düşündürür."
                    },
                    {
                        "text": "Klinik şüphe yüksek olduğu için oral alımı kesip analjezi vermek, çocuk cerrahisi veya ürolojiyi hemen çağırmak; Doppler ultrasonu yalnızca cerrahiyi geciktirmeyecekse yaptırmak",
                        "is_correct": True,
                        "explanation": "Testis canlılığı iskemi süresine bağlıdır. Yüksek klinik şüphede (örneğin yüksek TWIST skoru) görüntüleme beklenmeden eksplorasyon yapılır; Doppler belirsiz olgularda değerlidir.",
                        "new_finding": "Cerrahi ekip hemen bilgilendirildi. Ameliyathane hazırlanırken acil serviste yapılan yatak başı Doppler ultrasonda sağ testiste kan akımı izlenmedi, kordda girdap görünümü vardı; sol testis normaldi."
                    },
                    {
                        "text": "Radyoloji birimi gece çalışmadığı için Doppler ultrasonu sabaha planlamak, analjezi ve soğuk uygulamayla çocuğu serviste izlemek",
                        "is_correct": False,
                        "scenario_update": "Sabah Doppler ultrasona kadar dokuz saat geçti; testis kanlanması geri döndürülemez şekilde bozuldu.",
                        "teaching_point": "Görüntülemeye erişim yoksa klinik tanıyla eksplorasyon yapılır; bekleme organ kaybına yol açar."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Ani başlangıçlı kasık-skrotal ağrı, kusma, yatay duran yüksek testis, kayıp kremaster refleksi ve Doppler'de kanlanma kaybı olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Apendiks testis torsiyonu",
                        "is_correct": False,
                        "scenario_update": "Hassasiyet tüm testiste, mavi nokta işareti yok ve testis kanlanması kaybolmuş.",
                        "teaching_point": "Apendiks testis torsiyonunda hassasiyet üst kutupta lokalizedir ve testis kanlanması normaldir."
                    },
                    {
                        "text": "Sağ testis torsiyonu",
                        "is_correct": True,
                        "explanation": "Ani başlangıçlı ağrı, kusma, yüksek ve yatay testis, kremaster refleks kaybı ve Doppler'de akım yokluğu spermatik kordun dönmesiyle gelişen testis iskemisini gösterir; önceki kısa atak aralıklı dönmeyi düşündürür.",
                        "new_finding": "Tanı: Sağ Testis Torsiyonu."
                    },
                    {
                        "text": "Akut epididimoorşit",
                        "is_correct": False,
                        "scenario_update": "Ateş ve idrar yakınması yok, başlangıç ani ve Doppler'de kanlanma artmamış aksine kaybolmuş.",
                        "teaching_point": "Epididimitte Doppler'de kanlanma artışı görülür ve kremaster refleksi genellikle korunur."
                    },
                    {
                        "text": "Akut apandisit",
                        "is_correct": False,
                        "scenario_update": "Karında peritoneal bulgu yok; patoloji skrotumda gösterildi.",
                        "teaching_point": "Kasığa yayılan ağrıda skrotal muayene ayırıcı tanıyı netleştirir."
                    }
                ]
            },
            {
                "stage_title": "Cerrahi Tedavi",
                "question": "Bu çocuğun cerrahi yönetimi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Testis canlılığından emin olmak için ameliyattan önce skrotal manyetik rezonans çekmek ve sonuca göre orşiektomi kararı vermek",
                        "is_correct": False,
                        "scenario_update": "MR için iki saat beklendi; iskemi süresi uzadı.",
                        "teaching_point": "Canlılık ameliyatta değerlendirilir; ek görüntüleme cerrahiyi geciktirmemelidir."
                    },
                    {
                        "text": "Acil skrotal eksplorasyonla detorsiyon yapmak, canlılığı değerlendirmek; canlıysa her iki testisi sabitlemek, canlı değilse orşiektomi ve karşı tarafa orşiopeksi uygulamak",
                        "is_correct": True,
                        "explanation": "Eksplorasyonda kord çözülür ve testis ılık kompresle değerlendirilir. Anatomik yatkınlık genellikle iki taraflı olduğundan karşı testis de sabitlenir.",
                        "new_finding": "Semptomların dördüncü saatinde eksplorasyon yapıldı; 540 derece dönmüş kord çözüldü, testis ılık kompres sonrası pembeleşti. Bilateral orşiopeksi yapıldı. Üç ay sonraki kontrolde testis boyutları simetrikti."
                    },
                    {
                        "text": "Doppler ultrasonda testis kanlanması tamamen kaybolduğu için detorsiyon denemeden doğrudan orşiektomi yapmak ve sağlam karşı testise herhangi bir girişim yapmamak",
                        "is_correct": False,
                        "scenario_update": "Erken dönemde gelen, kurtarılabilir testis gereksiz yere çıkarıldı; karşı taraf korumasız kaldı.",
                        "teaching_point": "Önce detorsiyon ve canlılık değerlendirmesi yapılır; ilk saatlerde testisler çoğunlukla kurtarılabilir."
                    },
                    {
                        "text": "Detorsiyon sonrası testis canlı göründüğü için yalnızca etkilenen testisi sabitlemek ve karşı taraf için izlem önermek",
                        "is_correct": False,
                        "scenario_update": "İki yıl sonra karşı testiste torsiyon gelişti.",
                        "teaching_point": "Karşı testiste aynı anatomik yatkınlık bulunduğundan orşiopeksi iki taraflı yapılır."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y49",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "6 Yaşında",
        "gender": "Erkek",
        "complaint": "Kıvrandıran şiddetli karın ağrısı, dışkıda kan, dizlerde şişlik ve bacaklarda kabarık kırmızı-mor döküntüler",
        "history": "Ailesi anlatıyor: 'İki hafta önce boğaz ağrısı ve burun akıntısı geçirdi. Dün bacaklarında ve kalçasında, bastırınca solmayan kabarık kırmızı-mor lekeler çıktı. Bu sabah karnını tutup kıvrandıran çok şiddetli ağrısı başladı, bir kez koyu kırmızı kanlı kaka yaptı. İki dizi şişti, basmak istemiyor.' Ateşi yok, genel durumu ağrı dışında iyi. Bilinen hastalığı ve ilaç kullanımı yok. Tartı: 21 kg.",
        "final_diagnosis": "IgA Vasküliti (Henoch-Schönlein Purpurası) - Ciddi Gastrointestinal ve Renal Tutulum",
        "disposition": "Sarı Alanda Analjezi, İntravenöz Sıvı, İnvajinasyonun Dışlanması ve Sistemik Kortikosteroid ile Pediatri Servisine Yatış",
        "case_pearl": "Çocukluk çağının en sık vaskülitidir. Trombositopeni olmadan alt ekstremite ve kalçada palpabl purpura, artrit-artralji, kolik karın ağrısı ve böbrek tutulumu tipiktir. En önemli akut komplikasyon çoğunlukla ileoileal invajinasyondur; şiddetli karın ağrısında ultrasonla dışlanmalıdır. Şiddetli karın ağrısında kortikosteroid yarar sağlar ancak böbrek tutulumunu önlemez. Böbrek tutulumu için en az 6-12 ay idrar ve kan basıncı izlemi gerekir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Döküntünün Niteliği",
                "question": "Solmayan döküntü, şiddetli karın ağrısı, kanlı dışkı ve diz şişliği olan bu çocukta ilk değerlendirmede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Kabarık döküntüyü alerjik ürtiker kabul edip intravenöz antihistaminik ve steroid vermek, karın ağrısı ile kanlı dışkıyı gastroenterite bağlayıp oral sıvı denemesi yapmak",
                        "is_correct": False,
                        "scenario_update": "Döküntünün solmadığı ve ele geldiği fark edilmedi; karın ağrısı ve kanlı dışkı değerlendirilmedi.",
                        "teaching_point": "Solmayan döküntü ürtiker değildir; sistematik değerlendirme gerektirir."
                    },
                    {
                        "text": "Diz şişliği nedeniyle septik artriti dışlamak için iki dizden acil eklem aspirasyonu yapmak ve sinovyal sıvıyı kültüre göndermek",
                        "is_correct": False,
                        "scenario_update": "Ateşsiz, çok eklemli tabloda aspirasyon gereksizdi; çocuk ağrılı işlem yaşadı ve karın değerlendirmesi gecikti.",
                        "teaching_point": "Ateşsiz, simetrik, döküntüyle birlikte olan artrit sistemik bir hastalığı düşündürür."
                    },
                    {
                        "text": "Ateş, perfüzyon ve genel görünümle sepsisi dışlamak; döküntünün dağılımını ve ele gelip gelmediğini, eklemleri, karın, kan basıncı ve testisleri değerlendirmek",
                        "is_correct": True,
                        "explanation": "Solmayan döküntüde ilk görev hayatı tehdit eden sepsisi dışlamaktır. Simetrik, alt ekstremite ve kalçaya yerleşen palpabl purpura vaskülitik bir süreci düşündürür. Karında kitle invajinasyonu, hipertansiyon böbrek tutulumunu gösterebilir.",
                        "new_finding": "Vital Bulgular: Ateş 37.4°C, KTA 116/dk, SS 22/dk, TA 106/64 mmHg, SpO2 %99, KDZ 2 sn. Genel durumu ağrı dışında iyi. Bilateral alt ekstremitelerde ve kalçada simetrik, basmakla solmayan, ele gelen purpurik döküntüler; gövde ve yüz temiz. Her iki dizde şişlik ve hareket ağrısı. Karında yaygın kolik hassasiyet, kitle ve peritonit bulgusu yok. Testisler normal."
                    },
                    {
                        "text": "Kanlı dışkı nedeniyle çocuğu aç bırakıp acil kolonoskopi için gastroenterolojiye danışmak ve muayeneyi endoskopi sonrasına bırakmak",
                        "is_correct": False,
                        "scenario_update": "Endoskopi için hazırlık başlatıldı; döküntü, eklemler ve kan basıncı değerlendirilmedi.",
                        "teaching_point": "Endoskopi bu tabloda ilk adım değildir; tanı çoğunlukla klinik bulgularla konur."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar ve Ultrasonografi",
                "question": "Ateşsiz, palpabl purpura, artrit ve şiddetli karın ağrısı olan bu çocukta hangi tetkikler öncelikli olarak istenmelidir?",
                "options": [
                    {
                        "text": "Lösemi ve aplastik anemiyi dışlamak için acil kemik iliği aspirasyonu planlamak ve periferik yaymayı hematolojiye göndermek",
                        "is_correct": False,
                        "scenario_update": "Kan sayımı normalken kemik iliği incelemesi gereksizdi; çocuk sedasyon riskine maruz kaldı.",
                        "teaching_point": "Normal hemogramda kemik iliği incelemesi gerekmez."
                    },
                    {
                        "text": "Karın ağrısı ve kanlı dışkı nedeniyle intravenöz kontrastlı batın bilgisayarlı tomografisi çekmek ve idrar tetkikini taburculukta istemek",
                        "is_correct": False,
                        "scenario_update": "Tomografi ultrasonla elde edilebilecek bilgiyi verdi; böbrek tutulumu bir gün geç fark edildi.",
                        "teaching_point": "Çocukta karın değerlendirmesinde ultrason ilk tercihtir; idrar tetkiki ilk değerlendirmenin parçasıdır."
                    },
                    {
                        "text": "Tanıyı kesinleştirmek için bacaktaki purpurik lezyondan acil deri biyopsisi yapıp immünfloresan incelemeye göndermek ve sonuç çıkana kadar analjezi dışındaki tedavileri ertelemek",
                        "is_correct": False,
                        "scenario_update": "Biyopsi sonucu günler sürdü; bu sürede karın ağrısı ve kanama tedavisiz kaldı.",
                        "teaching_point": "Biyopsi atipik olgularda değerlidir; tipik klinikte tedaviyi geciktirmemelidir."
                    },
                    {
                        "text": "Tam kan sayımı, koagülasyon, BUN-kreatinin, albümin ve tam idrar ile idrarda protein/kreatinin oranı istemek; invajinasyonu dışlamak için batın ultrasonu yapmak",
                        "is_correct": True,
                        "explanation": "Normal trombosit sayısı ve koagülasyon purpuranın trombositopeni veya koagülopatiye bağlı olmadığını gösterir. İdrar ve böbrek fonksiyonları renal tutulumu belirler. Şiddetli karın ağrısında ultrason invajinasyon ve intramural hematomu gösterir.",
                        "new_finding": "Trombosit 350.000/mm³, lökosit 12.400/mm³, Hb 11.8 g/dL, PT ve aPTT normal, kreatinin 0.4 mg/dL, albümin 3.8 g/dL. İdrarda mikroskopik hematüri, protein/kreatinin oranı 0.6 mg/mg. Batın ultrasonu: ileum duvarında intramural hematomla uyumlu segmenter kalınlaşma; invajinasyon saptanmadı."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Enfeksiyon sonrası trombositopeni olmadan palpabl purpura, artrit, kanlı dışkıyla kolik karın ağrısı ve hematüri-proteinüri olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Akut lenfoblastik lösemi",
                        "is_correct": False,
                        "scenario_update": "Hemogram normal, organomegali ve lenfadenopati yok.",
                        "teaching_point": "Lösemide sitopeniler ve kemik ağrısı beklenir."
                    },
                    {
                        "text": "Meningokoksik sepsis (purpura fulminans)",
                        "is_correct": False,
                        "scenario_update": "Ateş yok, genel durum iyi, perfüzyon normal ve döküntü simetrik alt ekstremite yerleşimli.",
                        "teaching_point": "Meningokoksemide hızlı ilerleyen purpura, ateş ve toksik görünüm vardır."
                    },
                    {
                        "text": "IgA vasküliti (Henoch-Schönlein purpurası)",
                        "is_correct": True,
                        "explanation": "EULAR/PRINTO/PRES kriterlerine göre alt ekstremite baskın palpabl purpura ile birlikte karın ağrısı, artrit ve böbrek tutulumu IgA vaskülitini tanımlar.",
                        "new_finding": "Tanı: IgA Vasküliti (Henoch-Schönlein Purpurası) - ciddi gastrointestinal ve renal tutulum."
                    },
                    {
                        "text": "İmmün trombositopenik purpura",
                        "is_correct": False,
                        "scenario_update": "Trombosit sayısı normal, döküntü palpabl ve artrit eşlik ediyor.",
                        "teaching_point": "İmmün trombositopenide purpura trombositopeniye bağlıdır ve ele gelmez."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Şiddetli karın ağrısı, kanlı dışkı ve böbrek tutulumu olan bu çocuğun tedavisi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Hematüri ve proteinüri nedeniyle böbrek kaybını önlemek için acil siklofosfamid ve plazmaferez başlamak, karın ağrısı için sürekli opioid infüzyonuyla çocuğu yoğun bakımda izlemek",
                        "is_correct": False,
                        "scenario_update": "Hafif böbrek tutulumunda yoğun immünsüpresyon gereksizdi; çocuk ciddi yan etki riskine maruz kaldı.",
                        "teaching_point": "Yoğun immünsüpresyon nefrotik düzeyde proteinüri veya hızla ilerleyen böbrek yetmezliğinde, biyopsi sonrası planlanır."
                    },
                    {
                        "text": "Eklem ve karın ağrısı için yüksek doz ibuprofen başlamak, kanama azaldığı için oral beslenmeye geçip çocuğu idrar izlemi planlamadan taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "İbuprofen sonrası gastrointestinal kanama arttı; böbrek tutulumu izlenmedi.",
                        "teaching_point": "Gastrointestinal kanama ve böbrek tutulumunda NSAİİ'lerden kaçınılır; böbrek izlemi zorunludur."
                    },
                    {
                        "text": "Servise yatırıp intravenöz sıvı ve analjezi vermek, prednizolon 1-2 mg/kg/gün başlamak, invajinasyon bulgularını izlemek ve 6-12 ay idrar ile kan basıncı takibi planlamak",
                        "is_correct": True,
                        "explanation": "Şiddetli karın ağrısında kortikosteroid ağrıyı ve komplikasyon riskini azaltır. İnvajinasyon tedavi sırasında da gelişebilir. Steroid böbrek tutulumunu önlemediğinden uzun süreli idrar ve kan basıncı izlemi gerekir.",
                        "new_finding": "İntravenöz sıvı, parasetamol ve metilprednizolon başlandı. 24 saatte karın ağrısı belirgin geriledi, kanama durdu. Steroid iki haftada azaltılarak kesildi; nefroloji izleminde proteinüri üç ayda kayboldu."
                    },
                    {
                        "text": "Enfeksiyon sonrası başladığı için intravenöz seftriakson başlamak ve kortikosteroidi böbrek tutulumunu önlemek amacıyla üç ay sürdürmek",
                        "is_correct": False,
                        "scenario_update": "Antibiyotiğin rolü yoktu; uzun steroid kullanımı yan etkilere yol açtı ve böbrek tutulumunu önlemedi.",
                        "teaching_point": "Profilaktik uzun süreli steroid böbrek tutulumunu önlemez; antibiyotik endikasyonu yoktur."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y50",
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
