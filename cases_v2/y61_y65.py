# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - Y61-Y65 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "Y61",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "3 Yaşında",
        "gender": "Erkek",
        "complaint": "Altı gündür düşmeyen yüksek ateş, gözlerde kızarıklık, dudaklarda çatlama ve boyunda şişlik",
        "history": "Ailesi anlatıyor: 'Altı gündür ateşi 39.5°C'ye kadar çıkıyor, ateş düşürücülerle ancak 38.5°C'ye iniyor. Üç gün önce farenjit denilerek oral sefalosporin başlandı, ateş hiç gerilemedi. Gözlerinin akı kıpkırmızı ama çapak yok. Dudakları kurudu, çatladı, kanıyor. Dün gövdesinde kırmızı döküntüler çıktı, el ve ayakları şişti, kızardı. Çok huzursuz.' Öksürük ve ishal yok. Aşıları tam. Tartı: 15 kg.",
        "final_diagnosis": "Kawasaki Hastalığı (Tam Form, Koroner Arter Dilatasyonu ile)",
        "disposition": "Sarı Alanda Ekokardiyografi Sonrası İntravenöz İmmünoglobulin (2 g/kg) ve Aspirin ile Çocuk Kardiyoloji Yatışı",
        "case_pearl": "En az 5 gün ateşle birlikte şu beş bulgudan en az dördü tam form tanısı koydurur: eksüdasız bilateral konjonktival kızarıklık, dudak-ağız değişiklikleri (çatlak dudak, çilek dili), polimorf döküntü, el-ayakta ödem-eritem (sonra periungual soyulma) ve genellikle tek taraflı ≥1.5 cm servikal lenfadenopati. Eksik formda laboratuvar (CRP, ESH, albümin, ALT, trombositoz, steril piyüri) ve ekokardiyografi yol gösterir. Tedavi ilk 10 gün içinde İVİG 2 g/kg ve aspirindir; amaç koroner anevrizmayı önlemektir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Antibiyotiğe rağmen altı gündür ateşi süren bu 3 yaşındaki çocukta muayenede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Perfüzyon ve kalp muayenesini yapmak; göz, dudak-ağız, döküntü, el-ayak değişikliklerini ve boyun lenf nodlarını sistematik olarak değerlendirmek",
                        "is_correct": True,
                        "explanation": "Uzamış ateşte göz, ağız, deri ve el-ayak bulgularının sistematik sayılması tanıyı belirler. Taşikardi, galo veya şok bulguları miyokardit ya da şok tablosunu düşündürür.",
                        "new_finding": "Vital Bulgular: Ateş 39.4°C, KTA 142/dk, SS 28/dk, SpO2 %98, TA 94/58 mmHg, KDZ 2 sn. Bilateral eksüdasız konjonktival kızarıklık, limbus korunmuş. Dudaklar kırmızı, çatlak ve kanamalı; çilek dili. Gövdede makülopapüler polimorf döküntü. El ve ayak sırtında sert ödem, avuç içi ve tabanlarda eritem. Solda 2x2 cm tek, hassas servikal lenf nodu. Kalp sesleri ritmik, üfürüm ve galo yok."
                    },
                    {
                        "text": "Göz kızarıklığını bakteriyel konjonktivit kabul edip antibiyotikli göz damlası başlamak, döküntüyü sefalosporin alerjisine bağlayıp antihistaminik vermek",
                        "is_correct": False,
                        "scenario_update": "Göz damlası ve antihistaminik bulguları değiştirmedi; altta yatan tablo tanınmadı.",
                        "teaching_point": "Bulguları ayrı ayrı açıklamaya çalışmak, onları birleştiren sistemik hastalığın gözden kaçmasına yol açar."
                    },
                    {
                        "text": "Viral bir enfeksiyon olduğunu düşünüp antibiyotiği kesmek, ateş düşürücü ve bol sıvı önererek çocuğu evde izleme göndermek",
                        "is_correct": False,
                        "scenario_update": "Çocuk dördüncü gün yine ateşli getirildi; ekokardiyografide koroner anevrizma saptandı.",
                        "teaching_point": "Beş günü aşan ateşte bu bulgular varsa tedavi geciktirilmemelidir; koroner hasar riski zamanla artar."
                    },
                    {
                        "text": "Ateşin dirençli farenjite bağlı olduğunu düşünüp antibiyotiği intravenöz seftriaksona çevirmek ve iki gün sonra yeniden değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "İki gün seftriaksona rağmen ateş sürdü; tedavi penceresi daralmaya başladı.",
                        "teaching_point": "Antibiyotiğe yanıtsız uzamış ateşte enfeksiyon dışı nedenler ile deri ve mukoza bulguları sistematik değerlendirilmelidir."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar ve Kardiyak Değerlendirme",
                "question": "Uzamış ateş ve dört deri-mukoza bulgusu olan bu çocukta hangi tetkikler öncelikli olarak istenmelidir?",
                "options": [
                    {
                        "text": "Hemogram, CRP, sedimantasyon, albümin, karaciğer testleri ve tam idrar istemek; acil ekokardiyografiyle koroner arterleri değerlendirmek",
                        "is_correct": True,
                        "explanation": "Yüksek inflamatuvar belirteçler, hipoalbüminemi, transaminaz artışı ve steril piyüri tanıyı destekler. Ekokardiyografi koroner tutulumu, miyokardit ve perikardiyal sıvıyı gösterir ve tedavi yoğunluğunu belirler.",
                        "new_finding": "Lökosit 18.400/mm³ (%78 nötrofil), Hb 10.2 g/dL, trombosit 485.000/mm³, CRP 142 mg/L, ESH 88 mm/sa, albümin 2.8 g/dL, ALT 72 U/L. Tam idrarda steril piyüri (15-20 lökosit/saha). Ekokardiyografi: sol ön inen koroner arter Z skoru +2.8 (dilatasyon), sol ventrikül fonksiyonu normal, minimal perikardiyal sıvı."
                    },
                    {
                        "text": "Döküntü ve ateş nedeniyle kızamık, EBV ve adenovirüs serolojilerini gönderip sonuçlar gelene kadar ekokardiyografiyi ertelemek",
                        "is_correct": False,
                        "scenario_update": "Seroloji sonuçları beş gün sürdü; kardiyak değerlendirme gecikti.",
                        "teaching_point": "Viral tetkikler ayırıcı tanıda yardımcı olabilir ancak kardiyak değerlendirmeyi ve tedaviyi geciktirmemelidir."
                    },
                    {
                        "text": "Yalnızca boğaz kültürü ve ASO istemek, streptokok enfeksiyonu dışlanırsa ateşin nedenini araştırmak için çocuğu bir hafta daha izlemek",
                        "is_correct": False,
                        "scenario_update": "Bekleme süresinde ateşin onuncu günü geçti; tedavinin en etkili olduğu dönem kaçırıldı.",
                        "teaching_point": "Tedavi ateşin ilk 10 günü içinde verildiğinde koroner anevrizma riski belirgin azalır."
                    },
                    {
                        "text": "Menenjiti dışlamak için lomber ponksiyon yapmak ve sonuç gelene kadar intravenöz antibiyotikle izlemek",
                        "is_correct": False,
                        "scenario_update": "Beyin omurilik sıvısında hafif pleositoz saptandı ancak kültür negatif kaldı; asıl tablo için tetkikler gecikti.",
                        "teaching_point": "Bu hastalıkta aseptik pleositoz görülebilir; lomber ponksiyon ilk basamak tetkik değildir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Altı gündür süren ateş, eksüdasız konjonktival kızarıklık, çatlak dudak ve çilek dili, polimorf döküntü, el-ayakta ödem, servikal lenfadenopati ve koroner dilatasyonu olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Sistemik juvenil idiyopatik artrit",
                        "is_correct": False,
                        "scenario_update": "Artrit yok; mukokutanöz bulgular ve koroner tutulum farklı bir tabloyu gösteriyor.",
                        "teaching_point": "Sistemik JİA'da günlük kotidyen ateş, somon renkli döküntü ve artrit beklenir."
                    },
                    {
                        "text": "Kızıl (A grubu streptokok)",
                        "is_correct": False,
                        "scenario_update": "Döküntü zımpara kâğıdı gibi değil, konjonktival kızarıklık var ve antibiyotiğe yanıt yok.",
                        "teaching_point": "Kızılda konjonktivit beklenmez ve antibiyotik tedavisine hızlı yanıt alınır."
                    },
                    {
                        "text": "Kawasaki hastalığı (tam form)",
                        "is_correct": True,
                        "explanation": "En az 5 gün ateşle birlikte beş ana bulgunun tamamının varlığı ve koroner dilatasyon tam form Kawasaki hastalığını doğrular.",
                        "new_finding": "Tanı: Kawasaki Hastalığı (tam form, koroner arter dilatasyonu ile)."
                    },
                    {
                        "text": "Kızamık (rubeola enfeksiyonu)",
                        "is_correct": False,
                        "scenario_update": "Aşıları tam; öksürük, burun akıntısı ve Koplik lekeleri yok.",
                        "teaching_point": "Kızamıkta öksürük, nezle ve konjonktivit üçlüsü ile Koplik lekeleri görülür."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu çocuğun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Ateş altıncı günde olduğu için tedavi için geç kalındığını kabul edip yalnızca düşük doz aspirinle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Tedavi verilmeyen çocukta üçüncü haftada dev koroner anevrizma gelişti.",
                        "teaching_point": "İVİG ideal olarak ilk 10 günde verilir; 10. günden sonra da ateş veya inflamasyon sürüyorsa önerilir."
                    },
                    {
                        "text": "İVİG yerine yüksek doz intravenöz metilprednizolon vermek ve koroner dilatasyon anevrizmaya dönüşürse immünoglobulin eklemek",
                        "is_correct": False,
                        "scenario_update": "Steroid tek başına verildi; koroner dilatasyon ilerledi.",
                        "teaching_point": "Steroid ilk tedavide yalnızca yüksek riskli hastalarda İVİG'e ek olarak kullanılır, yerine geçmez."
                    },
                    {
                        "text": "Yalnızca yüksek doz aspirin başlamak, ateş düşmezse iki gün sonra intravenöz immünoglobulin vermeyi değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Aspirin tek başına koroner tutulumu önlemedi; iki gün sonraki ekoda dilatasyon arttı.",
                        "teaching_point": "Tedavinin temeli İVİG'dir; aspirin tek başına koroner anevrizmayı önlemez."
                    },
                    {
                        "text": "İntravenöz immünoglobulin 2 g/kg'ı 10-12 saatte vermek, aspirin başlamak ve 2 ile 6. haftalarda ekokardiyografi kontrolü planlamak",
                        "is_correct": True,
                        "explanation": "İVİG koroner anevrizma riskini belirgin azaltır. Aspirin ateş düşene kadar orta-yüksek dozda, sonra 3-5 mg/kg/gün düşük dozda sürdürülür. Koroner dilatasyonu olan yüksek riskli olguda ek steroid düşünülebilir. Canlı aşılar İVİG sonrası 11 ay ertelenir.",
                        "new_finding": "İVİG ve aspirin başlandı. 36 saatte ateş düştü, CRP geriledi. İkinci hafta ekokardiyografide koroner Z skoru +2.1'e indi; altıncı haftada normaldi. Düşük doz aspirin kardiyoloji önerisiyle kesildi."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y62",
        "category": "🦴 Kas-İskelet & Eklem / Ortopedik Aciller",
        "age": "2 Yaşında",
        "gender": "Kız",
        "complaint": "Sağ dizde hızla artan şişlik, kızarıklık, sıcaklık, yüksek ateş ve bacağa hiç basamama",
        "history": "Ailesi anlatıyor: 'Dün sabah hafif topallıyordu. Gece sağ dizi şişti, kızardı, dokununca yanıyor. Ateşi 39.2°C'ye çıktı. Bacağını hafif bükük tutuyor, hiç basmıyor, dokunmamıza izin vermiyor.' Bir hafta önce dizinde küçük bir sıyrık olmuş. Travma yok. Kanama hastalığı öyküsü yok. Aşıları tam. Tartı: 12 kg.",
        "final_diagnosis": "Sağ Diz Septik Artriti (Staphylococcus aureus)",
        "disposition": "Sarı Alanda Kültür Sonrası İntravenöz Antistafilokokal Antibiyotik ve Acil Ortopedik Eklem Lavajı ile Yatış",
        "case_pearl": "Ateş, basamama ve tek eklemde ağrılı şişlik septik artrit acilidir; kıkırdak hasarı saatler içinde başlar. En sık etken S. aureus'tur; 4 yaş altında Kingella kingae de sık görülür ve kültürde zor ürer (PCR yararlıdır). Sinovyal sıvıda lökosit >50.000/mm³ ve nötrofil hakimiyeti tipiktir. Tedavi kültürler alındıktan sonra ampirik antibiyotik ve cerrahi drenajdır; klinik ve CRP yanıtıyla erken oral geçiş mümkündür. Komşu kemikte osteomiyelit eşlik edebilir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Ateşli, dizi şiş ve bacağına basamayan bu 2 yaşındaki kızda muayenede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Sepsis bulgularını, dizde efüzyon ve hareket ağrısını, komşu kemik hassasiyetini, diğer eklemleri ve deri lezyonlarını değerlendirmek",
                        "is_correct": True,
                        "explanation": "Ateşli monoartritte sistemik durum aciliyeti belirler. Komşu metafizde hassasiyet osteomiyeliti, birden çok eklem tutulumu farklı nedenleri düşündürür. Deri lezyonu stafilokokal giriş kapısı olabilir.",
                        "new_finding": "Vital Bulgular: Ateş 39.1°C, KTA 138/dk, SS 26/dk, SpO2 %99, TA 96/60 mmHg, KDZ 2 sn. Sağ diz 30 derece fleksiyonda tutuluyor; belirgin şişlik, patellar ballotman, kızarıklık ve ısı artışı var. En küçük pasif hareket şiddetli ağrıya yol açıyor. Distal femur ve proksimal tibiada belirgin kemik hassasiyeti yok. Diğer eklemler normal. Diz önünde iyileşmekte olan sıyrık."
                    },
                    {
                        "text": "Travma olabileceğini düşünüp diz grafisi çekmek, kırık yoksa atel ve ibuprofen önerip üç gün sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Grafide kırık yoktu; atelle eve giden çocuğun ateşi sürdü ve iki gün sonra eklem harabiyetiyle geri getirildi.",
                        "teaching_point": "Ateşle birlikte tek eklemde ağrılı şişlik enfeksiyon dışlanana kadar acil kabul edilir."
                    },
                    {
                        "text": "Huzursuzluğu azaltmak için önce sedasyon verip dizden hemen biyopsi almak üzere ortopediye danışmak",
                        "is_correct": False,
                        "scenario_update": "Biyopsi bu aşamada gereksizdi; sistemik değerlendirme ve kültürler alınmadan zaman kaybedildi.",
                        "teaching_point": "İlk adım sistemik değerlendirme, kan tetkikleri ve kültürlerdir; doku biyopsisi atipik olgularda düşünülür."
                    },
                    {
                        "text": "Romatizmal bir hastalık düşünüp romatoloji polikliniğine yönlendirmek ve ağrı için oral prednizolon başlamak",
                        "is_correct": False,
                        "scenario_update": "Steroid ateşi maskeledi; eklem enfeksiyonu ilerledi.",
                        "teaching_point": "Enfeksiyon dışlanmadan steroid verilmez; akut ateşli monoartrit acil değerlendirilir."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar, Görüntüleme ve Sinovyal Sıvı",
                "question": "Bu çocukta tanıyı doğrulamak için hangi tetkikler yapılmalıdır?",
                "options": [
                    {
                        "text": "Yalnızca hemogram ve CRP istemek, lökosit 20.000/mm³'ün altındaysa enfeksiyonu dışlayıp çocuğu ağrı kesiciyle izlemek",
                        "is_correct": False,
                        "scenario_update": "Lökosit 19.800/mm³ geldi ve enfeksiyon yok sayıldı; sinovyal sıvı alınmadı.",
                        "teaching_point": "Normal veya sınırda lökosit sayısı eklem enfeksiyonunu dışlamaz."
                    },
                    {
                        "text": "Osteomiyeliti dışlamak için sedasyon altında diz manyetik rezonansını acil çekmek ve sonuç gelene kadar antibiyotiği ertelemek",
                        "is_correct": False,
                        "scenario_update": "MR için saatlerce beklendi; eklem enfeksiyonu tedavisiz kaldı.",
                        "teaching_point": "MR eşlik eden osteomiyelit şüphesinde değerlidir ancak drenaj ve antibiyotiği geciktirmemelidir."
                    },
                    {
                        "text": "Hemogram, CRP ve kan kültürü almak; grafi ve ultrason çekip ortopediyle sinovyal sıvıyı hücre sayımı ve kültür için almak",
                        "is_correct": True,
                        "explanation": "Kan kültürü ve sinovyal sıvı kültürü antibiyotik öncesinde alınmalıdır. Sinovyal lökosit sayısı ve Gram boyama tanıyı hızla destekler. Grafi kırık ve kemik lezyonunu, ultrason efüzyonu gösterir.",
                        "new_finding": "Lökosit 19.800/mm³ (%84 nötrofil), CRP 112 mg/L, ESH 74 mm/sa, kan kültürü alındı. Grafide kırık yok, yumuşak doku şişliği var. Ultrasonda yoğun ekojenik efüzyon. Sinovyal sıvı bulanık: lökosit 92.000/mm³ (%88 nötrofil), Gram boyamada küme yapan gram pozitif koklar; kültür ve Kingella PCR gönderildi."
                    },
                    {
                        "text": "Sinovyal sıvı almadan hemen intravenöz antibiyotik başlamak ve tanıyı antibiyotik yanıtına göre koymak, eklem sıvısını yalnızca yanıt alınamazsa incelemek",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik sonrası alınan sıvıda kültür negatif kaldı; etken ve duyarlılık belirlenemedi.",
                        "teaching_point": "Hemodinami stabilse antibiyotik öncesinde eklem sıvısı ve kan kültürü alınmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Ateş, basamama, dizde ağrılı efüzyon, CRP 112 mg/L ve sinovyal sıvıda 92.000/mm³ lökosit ile gram pozitif kok kümeleri olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Geçici (toksik) sinovit",
                        "is_correct": False,
                        "scenario_update": "Yüksek ateş, basamama, yüksek CRP ve pürülan sinovyal sıvı var.",
                        "teaching_point": "Geçici sinovitte çocuk iyi görünür ve inflamatuvar belirteçler normaldir."
                    },
                    {
                        "text": "Hemofiliye bağlı hemartroz",
                        "is_correct": False,
                        "scenario_update": "Kanama öyküsü yok, kız çocuk ve sinovyal sıvı kanlı değil pürülan.",
                        "teaching_point": "Hemartrozda eklem sıvısı kanlıdır ve kanama öyküsü bulunur."
                    },
                    {
                        "text": "Sağ diz septik artriti",
                        "is_correct": True,
                        "explanation": "Pürülan sinovyal sıvı, lökosit >50.000/mm³, nötrofil hakimiyeti ve Gram boyamada stafilokok morfolojisi bakteriyel eklem enfeksiyonunu doğrular.",
                        "new_finding": "Tanı: Sağ Diz Septik Artriti (olası Staphylococcus aureus)."
                    },
                    {
                        "text": "Oligoartiküler juvenil idiyopatik artrit",
                        "is_correct": False,
                        "scenario_update": "Akut başlangıç, yüksek ateş ve sinovyal sıvıda bakteri görülmesi bu tanıyla uyumsuz.",
                        "teaching_point": "Juvenil idiyopatik artrit en az 6 hafta süren, genellikle ateşsiz artritle tanınır."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu çocuğun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Eklemi yıkamadan altı hafta intravenöz antibiyotik vermek ve eklem hareketini tamamen kısıtlamak için alçıya almak",
                        "is_correct": False,
                        "scenario_update": "Drenaj yapılmayan eklemde pürülan sıvı kaldı ve kıkırdak hasarı gelişti; alçı eklem sertliğine yol açtı.",
                        "teaching_point": "Drenaj kıkırdağı korur; uzun süreli immobilizasyon önerilmez."
                    },
                    {
                        "text": "Eklem içine kortikosteroid ve antibiyotik enjekte etmek, inflamasyonu baskılamak için oral ibuprofeni yüksek dozda sürdürmek",
                        "is_correct": False,
                        "scenario_update": "Eklem içi steroid enfeksiyonu ağırlaştırdı; ateş ve şişlik arttı.",
                        "teaching_point": "Eklem enfeksiyonunda eklem içi steroid kontrendikedir; antibiyotik sistemik verilir."
                    },
                    {
                        "text": "Oral sefaleksinle ayaktan tedavi başlamak ve 48 saat sonra poliklinikte eklemi yeniden değerlendirmek, ağrı için ibuprofen ve dinlenme önermek",
                        "is_correct": False,
                        "scenario_update": "Drenajsız oral tedavi yetersiz kaldı; çocuk iki gün sonra eklem harabiyetiyle geri geldi.",
                        "teaching_point": "Septik artrit başlangıçta intravenöz antibiyotik ve eklem drenajı gerektirir."
                    },
                    {
                        "text": "İntravenöz sefazolin başlamak, acil eklem lavajı yapmak; klinik ve CRP düzelince oral tedaviyle toplam 2-3 haftaya tamamlamak",
                        "is_correct": True,
                        "explanation": "Sefazolin S. aureus ve Kingella'yı kapsar; MRSA sıklığı yüksek bölgelerde klindamisin veya vankomisin tercih edilir. Cerrahi lavaj bakteri yükünü ve kıkırdak hasarını azaltır. Ateşi düşen ve CRP'si gerileyen çocukta erken oral geçiş güvenlidir.",
                        "new_finding": "Sefazolin başlandı, artroskopik lavaj yapıldı. Kültürde metisiline duyarlı S. aureus üredi. 72. saatte ateş düştü, CRP 34 mg/L'ye indi; oral sefaleksine geçildi ve tedavi üç haftaya tamamlandı. Eklem hareketleri normale döndü."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y63",
        "category": "💧 Sıvı-Elektrolit & Renal / Ürolojik Aciller",
        "age": "8 Yaşında",
        "gender": "Erkek",
        "complaint": "Kola renginde idrar, göz kapaklarında ve bacaklarda şişlik, idrar azalması ve şiddetli baş ağrısı",
        "history": "Ailesi anlatıyor: 'Sabahtan beri kola renginde, koyu idrar yapıyor; bugün yalnızca bir kez azıcık yaptı. Sabah göz kapakları ve yüzü şişti, çorap lastikleri bacağında iz bıraktı. Şiddetli baş ağrısı var, gözlerinin önünde ışıklar çaktığını söylüyor.' İki hafta önce ateşli boğaz ağrısı geçirmiş, tedavi almamış. Bilinen böbrek hastalığı yok. Tartı: 28 kg (bir hafta önce 26 kg).",
        "final_diagnosis": "Akut Poststreptokokal Glomerülonefrit (Hipertansiyon ve Sıvı Yüklenmesi ile)",
        "disposition": "Sarı Alanda Tuz-Sıvı Kısıtlaması, İntravenöz Furosemid, Antihipertansif Tedavi ve Çocuk Nefroloji Yatışı",
        "case_pearl": "Boğaz enfeksiyonundan 1-3 hafta (deri enfeksiyonundan 3-6 hafta) sonra gelişen kola renkli idrar, ödem, hipertansiyon ve oligüri nefritik sendromun klasik tablosudur. Düşük C3 ve normal C4, streptokok antikorlarının yüksekliği ve idrarda dismorfik eritrosit-eritrosit silendirleri tanıyı destekler. Hipertansiyon çoğunlukla sıvı-tuz tutulumuna bağlıdır; tedavi tuz-sıvı kısıtlaması ve loop diüretiktir. Baş ağrısı, görme bozukluğu ve nöbet hipertansif ensefalopatiyi düşündürür. C3 6-8 haftada normale döner; dönmezse başka glomerül hastalıkları araştırılır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Kan Basıncı",
                "question": "Kola renkli idrar, ödem ve şiddetli baş ağrısıyla gelen bu 8 yaşındaki çocukta ilk değerlendirmede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "İdrar azaldığı için böbrekleri desteklemek amacıyla 20 mL/kg serum fizyolojik bolusu vermek ve idrar çıkışını iki saat boyunca saat başı ölçerek beklemek",
                        "is_correct": False,
                        "scenario_update": "Bolus sonrası solunum hızı arttı, satürasyon %92'ye düştü ve kan basıncı 150/100 mmHg'ye yükseldi.",
                        "teaching_point": "Ödemli ve hipertansif çocukta oligüri sıvı yüklenmesine eşlik eder; bolus tehlikelidir."
                    },
                    {
                        "text": "Kan basıncını uygun manşonla ölçmek; sıvı yüklenmesi, kalp yetmezliği ve hipertansif ensefalopati bulgularını aramak, tartıp idrar çıkışını izlemek",
                        "is_correct": True,
                        "explanation": "Baş ağrısı ve görsel yakınmalar hipertansif ensefalopatinin habercisi olabilir. Ödem, raller, hepatomegali ve galo sıvı yüklenmesini gösterir. Tartı ve idrar çıkışı sıvı dengesinin temelidir.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 88/dk, SS 22/dk, SpO2 %98, TA 138/92 mmHg (evre 2 hipertansiyon). Bilinç açık, oryante; fokal defisit yok, fundoskopide papilödem yok. Belirgin periorbital ödem, pretibial 2+ gode bırakan ödem. Akciğer bazallerinde hafif raller, karaciğer kot kavsini 2 cm geçiyor, galo yok. Tartı 28 kg."
                    },
                    {
                        "text": "Şişliği alerjik reaksiyon kabul edip intravenöz antihistaminik ve steroid vermek, baş ağrısı için parasetamol önermek",
                        "is_correct": False,
                        "scenario_update": "Kan basıncı ölçülmedi; çocuk gözlem sırasında jeneralize nöbet geçirdi.",
                        "teaching_point": "Ödem ve baş ağrısı olan çocukta kan basıncı ölçümü atlanmamalıdır."
                    },
                    {
                        "text": "Baş ağrısı ve görme yakınması nedeniyle önce kontrastsız beyin tomografisi çekmek ve idrar değerlendirmesini sonrasına bırakmak",
                        "is_correct": False,
                        "scenario_update": "Tomografi normal geldi; kan basıncı ve idrar değerlendirilmeden bir saat geçti.",
                        "teaching_point": "Baş ağrısının en olası nedeni yüksek kan basıncıdır; önce ölçülmeli ve tedavi edilmelidir."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar ve İdrar Değerlendirmesi",
                "question": "Hipertansif ve ödemli bu çocukta hangi tetkikler öncelikli olarak istenmelidir?",
                "options": [
                    {
                        "text": "Tam idrar ve idrar mikroskopisi, BUN-kreatinin, elektrolitler, albümin, C3-C4, ASO ve anti-DNaz B istemek; solunum sıkıntısı varsa akciğer grafisi çekmek",
                        "is_correct": True,
                        "explanation": "Dismorfik eritrositler ve eritrosit silendirleri glomerül kaynaklı kanamayı gösterir. Düşük C3 ve normal C4 ile streptokok antikorlarının yüksekliği etiyolojiyi destekler. Potasyum ve kreatinin akut böbrek hasarının derecesini belirler.",
                        "new_finding": "Tam idrar: kola renginde, dansite 1025, protein 2+, kan 3+. Mikroskopide bol dismorfik eritrosit ve eritrosit silendirleri. BUN 48 mg/dL, kreatinin 0.88 mg/dL, K 4.6 mEq/L, Na 136 mEq/L, albümin 3.4 g/dL. C3 32 mg/dL (düşük), C4 normal, ASO 680 IU/mL. Akciğer grafisinde hafif vasküler belirginleşme."
                    },
                    {
                        "text": "Kola renkli idrarı rabdomiyolize bağlayıp kreatin kinaz ve idrarda miyoglobin istemek, sonuç gelene kadar yüksek hızda sıvı başlamak, idrarı alkalileştirmek için bikarbonat eklemek",
                        "is_correct": False,
                        "scenario_update": "Kreatin kinaz normal geldi; verilen sıvı ödemi ve hipertansiyonu ağırlaştırdı.",
                        "teaching_point": "Ödem ve hipertansiyonla birlikte koyu idrar glomerül kaynaklı hematüriyi düşündürür."
                    },
                    {
                        "text": "Tanıyı kesinleştirmek için acil perkütan böbrek biyopsisi planlamak ve tedaviyi patoloji sonucuna göre başlatmak",
                        "is_correct": False,
                        "scenario_update": "Biyopsi tipik klinik tabloda gereksizdi; hipertansif çocukta kanama riski taşıdı ve tedavi gecikti.",
                        "teaching_point": "Biyopsi atipik seyir, hızlı ilerleyen böbrek yetmezliği veya C3'ün 8 haftada düzelmemesi durumunda yapılır."
                    },
                    {
                        "text": "Yalnızca idrar kültürü göndermek, idrar yolu enfeksiyonu kabul edip oral antibiyotik başlamak ve ödemi gözlemek",
                        "is_correct": False,
                        "scenario_update": "Kültür negatif geldi; hipertansiyon ve böbrek fonksiyonu değerlendirilmedi.",
                        "teaching_point": "Hematüri, ödem ve hipertansiyon birlikteliği enfeksiyonla açıklanmaz."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Boğaz enfeksiyonundan iki hafta sonra kola renkli idrar, ödem, hipertansiyon, eritrosit silendirleri, düşük C3 ve yüksek ASO olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "İlk atak nefrotik sendrom",
                        "is_correct": False,
                        "scenario_update": "Albümin yalnızca hafif düşük, masif proteinüri yok ve hematüri ile hipertansiyon belirgin.",
                        "teaching_point": "Nefrotik sendromda masif proteinüri ve ağır hipoalbüminemi ön plandadır."
                    },
                    {
                        "text": "Hemolitik üremik sendrom",
                        "is_correct": False,
                        "scenario_update": "Kanlı ishal, anemi ve trombositopeni yok.",
                        "teaching_point": "Hemolitik üremik sendromda mikroanjiyopatik hemoliz ve trombositopeni böbrek hasarına eşlik eder."
                    },
                    {
                        "text": "IgA nefropatisi",
                        "is_correct": False,
                        "scenario_update": "Hematüri enfeksiyondan iki hafta sonra başladı ve C3 düşük.",
                        "teaching_point": "IgA nefropatisinde hematüri enfeksiyonla eş zamanlı (1-2 gün içinde) ortaya çıkar ve C3 normaldir."
                    },
                    {
                        "text": "Akut poststreptokokal glomerülonefrit",
                        "is_correct": True,
                        "explanation": "Latent dönem sonrası nefritik sendrom, düşük C3, normal C4 ve yüksek streptokok antikorları akut poststreptokokal glomerülonefriti doğrular.",
                        "new_finding": "Tanı: Akut Poststreptokokal Glomerülonefrit (hipertansiyon ve sıvı yüklenmesi ile)."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu çocuğun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Tuz ve sıvıyı kısıtlamak, intravenöz furosemid vermek, kan basıncı yüksek kalırsa nifedipin eklemek ve günlük tartıyla izlemek",
                        "is_correct": True,
                        "explanation": "Hipertansiyon ve ödem sıvı-tuz tutulumuna bağlıdır; diüretik ve kısıtlama temel tedavidir. Kalsiyum kanal blokerleri ek antihipertansif olarak güvenlidir. Süren streptokok enfeksiyonu varsa penisilin verilir ancak böbrek seyrini değiştirmez.",
                        "new_finding": "Furosemid 1 mg/kg intravenöz verildi, tuz-sıvı kısıtlandı. Dört saatte 450 mL idrar çıktı, kan basıncı 118/76 mmHg'ye indi, baş ağrısı geçti. Üç günde ödem çözüldü. Sekizinci haftada C3 normale döndü."
                    },
                    {
                        "text": "Kan basıncı 138/92 mmHg olduğu için hipertansiyonu ciddi kabul etmemek, oral antibiyotik ve tuzsuz diyetle çocuğu taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Evde baş ağrısı arttı; çocuk ertesi gün hipertansif ensefalopati ve nöbetle getirildi.",
                        "teaching_point": "Semptomatik evre 2 hipertansiyon ve oligüri yatış gerektirir."
                    },
                    {
                        "text": "Böbrek perfüzyonunu korumak için idame hızında intravenöz sıvı vermek, kan basıncını düşürmek için ilk seçenek olarak ACE inhibitörü başlamak",
                        "is_correct": False,
                        "scenario_update": "Sıvı yükü arttı; ACE inhibitörü sonrası potasyum 6.1 mEq/L'ye yükseldi ve kreatinin arttı.",
                        "teaching_point": "Akut dönemde sıvı kısıtlanır; ACE inhibitörleri hiperkalemi ve böbrek fonksiyonunda bozulma riski nedeniyle ilk seçenek değildir."
                    },
                    {
                        "text": "Böbrek hasarını önlemek için yüksek doz intravenöz metilprednizolon ve siklofosfamid başlamak, kan basıncı için yalnızca gözlem yapmak",
                        "is_correct": False,
                        "scenario_update": "İmmünsüpresif tedavi gereksizdi; tedavi edilmeyen hipertansiyon nedeniyle çocukta nöbet gelişti.",
                        "teaching_point": "Tipik seyirde immünsüpresyon endike değildir; hipertansiyon acilen tedavi edilmelidir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y64",
        "category": "💧 Sıvı-Elektrolit & Renal / Ürolojik Aciller",
        "age": "4 Yaşında",
        "gender": "Erkek",
        "complaint": "Göz kapaklarında başlayıp bacaklara, karına ve skrotuma yayılan yaygın şişlik ve köpüklü idrar",
        "history": "Ailesi anlatıyor: 'Beş gün önce sabah göz kapakları şişmişti, alerji sandık. Şişlik bacaklarına, ayak bileklerine ve testislerine yayıldı. Karnı şişti, pantolonu kapanmıyor. İdrarı azaldı ve köpüklü. Bugün karnı biraz ağrıyor, halsiz.' Bir hafta önce soğuk algınlığı geçirmiş. Kanlı idrar ve döküntü yok. Su çiçeği geçirmemiş. Tartı: 18 kg (öncesinde 15.5 kg).",
        "final_diagnosis": "İlk Atak İdiyopatik Nefrotik Sendrom (Olası Minimal Değişiklik Hastalığı)",
        "disposition": "Sarı Alanda Damar İçi Hacim Değerlendirmesi, Tuz Kısıtlaması, Oral Prednizolon ve Komplikasyon Eğitimi ile Çocuk Nefroloji Yatışı",
        "case_pearl": "Masif proteinüri (idrar protein/kreatinin >2 mg/mg), hipoalbüminemi (<2.5 g/dL) ve ödem tanı koydurur; hiperlipidemi eşlik eder. 1-10 yaş arasında hematüri, hipertansiyon ve böbrek yetmezliği olmayan, C3'ü normal çocukta neden çoğunlukla minimal değişiklik hastalığıdır ve biyopsi yapılmadan steroid başlanır. Ödemli olmasına karşın damar içi hacim azalmış olabilir (karın ağrısı, taşikardi, soğuk ekstremite, yüksek hematokrit); bu durumda diüretik tehlikelidir. Başlıca komplikasyonlar enfeksiyon (peritonit, selülit) ve trombozdur.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Hacim Durumu",
                "question": "Yaygın ödemi, asiti ve karın ağrısı olan bu 4 yaşındaki çocukta ilk değerlendirmede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Skrotal şişlik nedeniyle testis torsiyonunu dışlamak için acil skrotal Doppler istemek ve üroloji görüşü gelene kadar muayeneyi bununla sınırlamak",
                        "is_correct": False,
                        "scenario_update": "Doppler normal geldi; yaygın ödemin nedeni ve hacim durumu değerlendirilmedi.",
                        "teaching_point": "Yaygın ödemin bir parçası olan skrotal ödem sistemik değerlendirme gerektirir."
                    },
                    {
                        "text": "Göz kapağı şişliği nedeniyle alerjik anjiyoödem kabul edip intramüsküler adrenalin ve antihistaminik vermek",
                        "is_correct": False,
                        "scenario_update": "Tedaviye yanıt alınmadı; ödemin nedeni değerlendirilmedi.",
                        "teaching_point": "Günler içinde yerçekimine bağlı yayılan gode bırakan ödem alerjik değildir."
                    },
                    {
                        "text": "Ödemi hızla azaltmak için hacim durumunu değerlendirmeden yüksek doz intravenöz furosemid vermek ve idrar çıkışını izlemek",
                        "is_correct": False,
                        "scenario_update": "Furosemid sonrası çocukta taşikardi, karın ağrısında artış ve soğuk ekstremiteler gelişti.",
                        "teaching_point": "Hacim azlığı olan nefrotik çocukta diüretik şoka ve tromboza yol açabilir."
                    },
                    {
                        "text": "Kan basıncı, nabız, kapiller dolum ve ekstremite ısısıyla hacim durumunu; ödem, asit, solunum, enfeksiyon ve tromboz bulgularını değerlendirmek",
                        "is_correct": True,
                        "explanation": "Ödemli çocukta damar içi hacim azalmış olabilir; karın ağrısı ve soğuk ekstremite hipovolemiyi düşündürür. Plevral efüzyon solunumu etkiler. Karın ağrısı ayrıca enfeksiyon veya trombozun habercisi olabilir.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 98/dk, SS 22/dk, SpO2 %99, TA 96/60 mmHg, KDZ 2 sn, ekstremiteler sıcak. Periorbital ödem, pretibial 3+ gode bırakan ödem, belirgin skrotal ödem. Karın distandü, yer değiştiren matite (asit); hafif yaygın hassasiyet, defans ve rebound yok. Akciğer bazallerinde solunum sesleri hafif azalmış. Tartı 18 kg."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar Değerlendirmesi",
                "question": "Bu çocukta tanı ve tedavi kararı için hangi tetkikler istenmelidir?",
                "options": [
                    {
                        "text": "Tam idrar, idrar protein/kreatinin oranı, albümin, kolesterol, kreatinin, elektrolit, hemogram ve C3 istemek; enfeksiyon taraması yapmak",
                        "is_correct": True,
                        "explanation": "Masif proteinüri ve hipoalbüminemi tanıyı doğrular. Hematüri, düşük C3, hipertansiyon ve kreatinin artışı atipik nedenleri düşündürür. Hematokrit yüksekliği hacim azlığını gösterir. Hepatit B, su çiçeği serolojisi ve tüberküloz taraması steroid öncesi önemlidir.",
                        "new_finding": "Tam idrar: dansite 1030, protein 4+, eritrosit yok. İdrar protein/kreatinin 8.4 mg/mg. Albümin 1.6 g/dL, kolesterol 380 mg/dL, kreatinin 0.4 mg/dL, Na 133 mEq/L, hematokrit %42, C3 normal. HBsAg negatif, su çiçeği IgG negatif."
                    },
                    {
                        "text": "Tedaviye başlamadan önce acil perkütan böbrek biyopsisi planlamak ve histolojik tanıya göre tedavi seçmek",
                        "is_correct": False,
                        "scenario_update": "Nefroloji, tipik başvuruda biyopsinin gerekmediğini belirtti; tedavi gecikti.",
                        "teaching_point": "1-10 yaş arası tipik başvuruda biyopsi yapılmadan steroid başlanır; biyopsi steroid direncinde düşünülür."
                    },
                    {
                        "text": "Asitin nedenini bulmak için kontrastlı batın tomografisi çekmek ve karaciğer hastalığını dışlamak için gastroenterolojiye danışmak",
                        "is_correct": False,
                        "scenario_update": "Tomografi yaygın asit gösterdi; asıl tanı için idrar tetkiki yapılmamıştı.",
                        "teaching_point": "Ödem ve asitli çocukta ilk tetkik tam idrardır; proteinüri tanıyı yönlendirir."
                    },
                    {
                        "text": "Tedavi kararı için 24 saatlik idrar toplamasını tamamlamak ve sonuç gelene kadar steroid dahil hiçbir tedavi başlamamak",
                        "is_correct": False,
                        "scenario_update": "Bezli çocukta idrar toplama güvenilir yapılamadı; tedavi bir gün gecikti.",
                        "teaching_point": "Spot idrar protein/kreatinin oranı küçük çocuklarda yeterli ve pratiktir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Masif proteinüri, albümin 1.6 g/dL, hiperkolesterolemi ve yaygın ödemi olan, hematürisi ve hipertansiyonu olmayan, C3'ü normal bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Dilate kardiyomiyopatiye bağlı kalp yetmezliği",
                        "is_correct": False,
                        "scenario_update": "Kalp muayenesi normal, hepatomegali ve galo yok; idrarda masif protein var.",
                        "teaching_point": "Kalp yetmezliğine bağlı ödemde proteinüri ve ağır hipoalbüminemi beklenmez."
                    },
                    {
                        "text": "İlk atak idiyopatik nefrotik sendrom",
                        "is_correct": True,
                        "explanation": "Masif proteinüri, hipoalbüminemi, ödem ve hiperlipidemi nefrotik sendromu tanımlar; yaş, hematüri ve hipertansiyon yokluğu ve normal C3 minimal değişiklik hastalığını düşündürür.",
                        "new_finding": "Tanı: İlk Atak İdiyopatik Nefrotik Sendrom (olası minimal değişiklik hastalığı)."
                    },
                    {
                        "text": "Akut glomerülonefrit",
                        "is_correct": False,
                        "scenario_update": "Hematüri, hipertansiyon ve düşük C3 yok; masif proteinüri ön planda.",
                        "teaching_point": "Glomerülonefritte hematüri, hipertansiyon ve oligüri baskındır."
                    },
                    {
                        "text": "Protein kaybettiren enteropati",
                        "is_correct": False,
                        "scenario_update": "İdrarda masif protein kaybı var; ishal ve gastrointestinal yakınma yok.",
                        "teaching_point": "Protein kaybettiren enteropatide idrarda protein beklenmez."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Damar içi hacmi korunmuş bu çocuğun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Steroid başlamadan önce proteinürinin kendiliğinden düzelip düzelmediğini görmek için iki hafta yalnızca tuzsuz diyetle izlemek",
                        "is_correct": False,
                        "scenario_update": "Bekleme süresinde ödem arttı ve çocukta selülit gelişti.",
                        "teaching_point": "Tipik ilk atakta steroid geciktirilmemelidir."
                    },
                    {
                        "text": "Oral prednizolon 60 mg/m²/gün başlamak, tuzu kısıtlamak, hareketi teşvik etmek ve enfeksiyon ile tromboz belirtileri konusunda aileyi eğitmek",
                        "is_correct": True,
                        "explanation": "Steroid ilk atakta 4-6 hafta günlük, ardından 4-6 hafta gün aşırı verilir; çocukların çoğunda 2 hafta içinde remisyon sağlanır. Tuz kısıtlaması ödemi azaltır. Hareketsizlik tromboz riskini artırır. Ateş, karın ağrısı ve su çiçeği teması acil başvuru nedenidir.",
                        "new_finding": "Prednizolon ve tuz kısıtlaması başlandı. Onuncu günde idrarda protein negatifleşti, diürez başladı ve ödem çözüldü. Aileye günlük idrar stiki ve uyarı belirtileri öğretildi."
                    },
                    {
                        "text": "İlk tedavi olarak siklofosfamid başlamak, steroidi yan etkileri nedeniyle vermemek ve proteinüri azalana kadar yatak istirahati önermek",
                        "is_correct": False,
                        "scenario_update": "Siklofosfamid ilk basamak değildi; yatak istirahati sırasında çocukta derin ven trombozu gelişti.",
                        "teaching_point": "İlk atakta tedavi steroiddir; ikinci basamak ilaçlar steroid bağımlılığı veya direncinde kullanılır."
                    },
                    {
                        "text": "Ödemin hızla çözülmesi için her çocukta rutin olarak günde iki kez albümin ve furosemid vermek ve sıvıyı kesin olarak kısıtlamak",
                        "is_correct": False,
                        "scenario_update": "Rutin albümin-furosemid sonrası çocukta hacim azlığı ve hiponatremi gelişti.",
                        "teaching_point": "Albümin ve diüretik yalnızca semptomatik ağır ödemde, hacim azlığı yoksa ve yakın izlemle kullanılır."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y65",
        "category": "🧠 Nörolojik Aciller",
        "age": "7 Yaşında",
        "gender": "Kız",
        "complaint": "Bulantı ilacı sonrası başlayan boyunda kasılma, başın geriye-yana bükülmesi, gözlerin yukarı kayması ve konuşma güçlüğü",
        "history": "Ailesi anlatıyor: 'Dün geceden beri kusuyordu. Bugün aile hekimi bulantı için damla reçete etti; kusmaya devam edince önerilenin iki katı verdik. Yaklaşık iki saat sonra boynu sola kilitlendi, başı geriye büküldü, gözleri yukarı kaydı, aşağı bakamıyor. Dili kasılıyor, konuşamıyor ama bizi duyuyor, korkuyor.' Ateş, travma ve bilinç kaybı yok. Daha önce nöbet öyküsü yok. Tartı: 24 kg.",
        "final_diagnosis": "İlaca Bağlı Akut Distonik Reaksiyon (Metoklopramid; Okülojirik Kriz ve Tortikolis)",
        "disposition": "Sarı Alanda İntravenöz-İntramüsküler Antikolinerjik Tedavi, İlacın Kesilmesi ve 24-48 Saat Oral Antikolinerjikle Taburculuk",
        "case_pearl": "Dopamin antagonistleri (metoklopramid, proklorperazin, haloperidol) özellikle çocuk ve gençlerde, sıklıkla doz aşımında saatler içinde akut distoniye yol açar: tortikolis, okülojirik kriz, dil-çene kasılması ve opistotonus. Bilinç korunur ve bu nöbetten ayıran temel özelliktir. Laringeal distoni hava yolunu tehdit edebilir. Tedavi intravenöz veya intramüsküler difenhidramin (1 mg/kg) ya da biperidendir; yanıt dakikalar içindedir. Tekrarı önlemek için 24-48 saat oral antikolinerjik verilir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Bulantı damlası sonrası boynu kilitlenen ve gözleri yukarı kayan bu 7 yaşındaki kızda ilk değerlendirmede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Ensefalit olasılığı nedeniyle lomber ponksiyon yapmak ve sonuç gelene kadar intravenöz asiklovir başlamak",
                        "is_correct": False,
                        "scenario_update": "Lomber ponksiyon sırasında çocuk kasılmalar nedeniyle pozisyon alamadı; ateş ve bilinç bozukluğu yoktu.",
                        "teaching_point": "Ateşsiz, bilinci açık ve ilaç öyküsü belirgin çocukta santral sinir sistemi enfeksiyonu öncelikli düşünülmez."
                    },
                    {
                        "text": "Kaygılı görünümü nedeniyle tabloyu psikojenik kabul edip çocuğu sakinleştirmeye çalışmak ve ailesini dışarı çıkarmak",
                        "is_correct": False,
                        "scenario_update": "Kasılmalar sürdü ve dil kasılması nedeniyle çocuk yutkunmakta zorlanmaya başladı.",
                        "teaching_point": "Yeni ilaç sonrası gelişen kasılmalar organik bir neden olarak değerlendirilmelidir."
                    },
                    {
                        "text": "Gözlerin yukarı kayması nedeniyle tabloyu epileptik nöbet kabul edip intravenöz diazepam ve ardından fenitoin yüklemesi yapmak, nöbet sürerse levetirasetam eklemek",
                        "is_correct": False,
                        "scenario_update": "Diazepam sonrası çocuk uykuya daldı ancak boyun ve göz kasılması sürdü; fenitoin yanıtsızdı.",
                        "teaching_point": "Bilinç açıkken süren kasılma epileptik nöbet değildir; antiepileptikler bu tabloda etkisizdir."
                    },
                    {
                        "text": "Hava yolunu ve yutmayı değerlendirmek; bilinç, ateş, kas sertliği ve vital bulguları kontrol edip ilacın adını ve dozunu öğrenmek",
                        "is_correct": True,
                        "explanation": "Laringeal tutulum hava yolunu tehdit edebilir. Korunmuş bilinç epileptik nöbetten ayırır. Ateş, yaygın rijidite ve otonomik bozukluk daha ağır bir ilaç reaksiyonunu düşündürür. İlaç öyküsü tanının anahtarıdır.",
                        "new_finding": "Vital Bulgular: Ateş 36.6°C, KTA 104/dk, SS 20/dk, SpO2 %99, TA 102/64 mmHg. Stridor yok, salyasını yutabiliyor. Bilinç tamamen açık, sorulara baş hareketiyle yanıt veriyor. Sola tortikolis, hafif retrokollis; gözler yukarıda fikse, aşağı bakamıyor. Dilde kasılma. Ekstremitelerde yaygın rijidite yok. Kullanılan damlanın bir dopamin antagonisti antiemetik olduğu öğrenildi."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Bilinci açık, ateşsiz, hava yolu güvenli ve ilaç öyküsü belirgin bu çocukta tetkik yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Geniş kapsamlı toksikoloji taraması göndermek ve sonuç gelene kadar çocuğu gözlem odasında tedavisiz izlemek",
                        "is_correct": False,
                        "scenario_update": "Tarama sonucu ertesi güne kaldı; çocuk saatlerce kasılmalarla bekledi.",
                        "teaching_point": "Öyküyle açıklanan tabloda rutin toksikoloji taraması tedaviyi geciktirmemelidir."
                    },
                    {
                        "text": "Kapiller kan şekeri, elektrolitler, kalsiyum ve magnezyum bakmak; ateş ve kas sertliği olmadığını kayda geçirip ek görüntüleme istememek",
                        "is_correct": True,
                        "explanation": "Hipokalsemi ve hipomagnezemi kas spazmlarını taklit edebilir. Ateş, rijidite ve otonomik bozukluğun olmaması nöroleptik malign sendromu dışlamaya yardım eder. Tanı öyküye dayanır ve tedaviye hızlı yanıtla doğrulanır.",
                        "new_finding": "Kan şekeri 98 mg/dL, Na 138, K 4.2 mEq/L, iyonize kalsiyum 1.22 mmol/L, magnezyum 2.0 mg/dL. Kreatin kinaz normal. Önerilen dozun iki katı alındığı doğrulandı."
                    },
                    {
                        "text": "Kafa içi patolojiyi dışlamak için acil beyin manyetik rezonansı ve elektroensefalografi istemek, nörolojiye danışıp sonuçlar çıkana kadar hiçbir tedavi vermemek",
                        "is_correct": False,
                        "scenario_update": "Görüntüleme ve EEG için saatlerce beklendi; kasılmalar sürdü.",
                        "teaching_point": "Tipik ilaç öyküsü ve korunmuş bilinçte görüntüleme ve EEG gerekmez; tedavi tanısaldır."
                    },
                    {
                        "text": "Boyun kasılması nedeniyle servikal omurga grafisi ve tomografi çekmek, ardından ortopediye danışmak",
                        "is_correct": False,
                        "scenario_update": "Görüntüleme normal geldi; travma öyküsü olmadığı için tetkikler gereksizdi.",
                        "teaching_point": "Travmasız, ilaçla ilişkili tortikoliste omurga görüntülemesi gerekmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Önerilen dozun iki katı bulantı damlası (metoklopramid) aldıktan sonra bilinci açıkken tortikolis, okülojirik kriz ve dil kasılması gelişen bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Fokal epileptik nöbet",
                        "is_correct": False,
                        "scenario_update": "Bilinç tamamen açık, kasılmalar sürekli ve ilaç alımı sonrası başladı.",
                        "teaching_point": "Uzun süren fokal nöbetlerde genellikle ritmik kasılmalar ve bilinç değişikliği görülür."
                    },
                    {
                        "text": "Nöroleptik malign sendrom",
                        "is_correct": False,
                        "scenario_update": "Ateş, yaygın kurşun boru rijiditesi, otonomik bozukluk ve kreatin kinaz yüksekliği yok.",
                        "teaching_point": "Nöroleptik malign sendrom ateş, rijidite, bilinç değişikliği ve otonomik instabiliteyle seyreder."
                    },
                    {
                        "text": "Hipokalsemik tetani",
                        "is_correct": False,
                        "scenario_update": "İyonize kalsiyum ve magnezyum normal; karpopedal spazm yok.",
                        "teaching_point": "Tetanide el-ayak spazmı, Chvostek ve Trousseau bulguları görülür."
                    },
                    {
                        "text": "İlaca bağlı akut distonik reaksiyon",
                        "is_correct": True,
                        "explanation": "Dopamin antagonisti alımından saatler sonra gelişen, bilincin korunduğu tortikolis, okülojirik kriz ve dil kasılması akut distonik reaksiyonu doğrular.",
                        "new_finding": "Tanı: İlaca Bağlı Akut Distonik Reaksiyon (metoklopramid)."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk",
                "question": "Bu çocuğun tedavisi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Kasılmalar kendiliğinden geçeceği için yalnızca intravenöz sıvı ve parasetamol vermek, ilacın bir sonraki dozunu evde yarıya indirerek sürdürmeyi önermek",
                        "is_correct": False,
                        "scenario_update": "Kasılmalar saatlerce sürdü; yarım dozla yeniden başlanan ilaç reaksiyonu tekrarlattı.",
                        "teaching_point": "Neden olan ilaç kesilmeli ve antikolinerjikle hızla tedavi edilmelidir."
                    },
                    {
                        "text": "Yüksek doz intravenöz midazolam infüzyonu başlamak, kasılma geçmezse kas gevşetici ile entübasyon hazırlığı yapmak",
                        "is_correct": False,
                        "scenario_update": "Midazolam çocuğu derin sedasyona soktu ancak distoniyi çözmedi; solunum depresyonu gelişti.",
                        "teaching_point": "Benzodiazepinler ikinci basamak destek tedavidir; ilk seçenek antikolinerjiktir."
                    },
                    {
                        "text": "İlacı kesip intravenöz difenhidramin 1 mg/kg veya biperiden vermek, tekrarı önlemek için 24-48 saat oral antikolinerjik reçete etmek",
                        "is_correct": True,
                        "explanation": "Antikolinerjik ilaçlar dopamin-asetilkolin dengesini düzelterek dakikalar içinde distoniyi çözer. İlacın etkisi sürebileceği için reaksiyon tekrarlayabilir; kısa süreli oral tedavi önerilir. Aileye bu ilacı tekrar kullanmamaları söylenir.",
                        "new_finding": "İntravenöz difenhidramin sonrası 10 dakikada boyun ve göz kasılması çözüldü, çocuk konuşmaya başladı. İki saat gözlem sonrası oral antikolinerjikle taburcu edildi; kayda ilaç reaksiyonu işlendi."
                    },
                    {
                        "text": "Kasılmaları çözmek için intravenöz dantrolen başlamak ve çocuğu yoğun bakım ünitesinde izlemek",
                        "is_correct": False,
                        "scenario_update": "Dantrolen bu tabloda etkisizdi; çocuk gereksiz yere yoğun bakıma yatırıldı.",
                        "teaching_point": "Dantrolen malign hipertermi ve seçilmiş nöroleptik malign sendrom olgularında kullanılır."
                    }
                ]
            }
        ]
    }
]
