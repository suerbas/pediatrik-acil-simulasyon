# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - Y56-Y60 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "Y56",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "5 Yaşında",
        "gender": "Erkek",
        "complaint": "Hızla şiddetlenen sağ alt karın ağrısı, kusma ve ateş",
        "history": "Ailesi anlatıyor: 'Dün göbeğinin altında ağrı başladı, hızla şiddetlendi, üç kez kustu. Ateşi 38.6°C'ye çıktı. Başka bir hastanede ultrason çektiler, apandisit normal görünüyor deyip ağrı kesiciyle gönderdiler ama ağrısı daha da arttı.' Daha önce birkaç kez nedeni bulunamayan karın ağrısı atakları olmuş. Dışkıda kan görülmemiş. Tartı: 19 kg.",
        "final_diagnosis": "İnflame Meckel Divertikülü (Meckel Divertiküliti)",
        "disposition": "Sarı Alanda Oral Alımın Kesilmesi, İntravenöz Sıvı-Analjezi-Antibiyotik ve Çocuk Cerrahisiyle Acil Laparoskopik Rezeksiyon",
        "case_pearl": "Normal apendiks görüntülenen ancak lokal periton irritasyonu süren çocukta alternatif nedenler aranmalıdır. Meckel divertikülü '2 kuralı' ile anılır: toplumun yaklaşık %2'si, ileoçekal valvden yaklaşık 60 cm proksimalde, çoğunlukla 2 yaş altında semptom verir. Ağrısız masif rektal kanama, obstrüksiyon (invajinasyon, volvulus) veya divertikülit ile başvurabilir. Divertikülit klinik olarak apandisite çok benzer; tedavi cerrahi rezeksiyondur. Teknesyum sintigrafisi kanayan olgularda yararlıdır, inflamasyonda tanısal değeri sınırlıdır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Karın Muayenesi",
                "question": "Dış merkezde apendiksi normal bildirilen ancak ağrısı artan bu ateşli 5 yaşındaki çocukta yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Dış merkez ultrasonunda apendiks normal olduğu için cerrahi tabloyu dışlamak, ağrıyı mezenterik lenfadenite bağlayıp oral analjezikle yeniden taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk evde kötüleşti; 12 saat sonra yaygın karın hassasiyeti ve yüksek ateşle geri getirildi.",
                        "teaching_point": "Normal görüntüleme ile klinik bulgular çeliştiğinde klinik bulgular esas alınır ve yeniden değerlendirme yapılır."
                    },
                    {
                        "text": "Ağrının kabızlığa bağlı olabileceğini düşünüp lavman uygulamak, ardından laksatif reçete edip bir gün sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Lavman sonrası ağrı değişmedi; ateş yükseldi ve peritoneal bulgular belirginleşti.",
                        "teaching_point": "Ateş ve lokal periton irritasyonu olan çocukta lavman uygunsuzdur."
                    },
                    {
                        "text": "Analjezi verip oral alımı kesmek, damar yolu açmak ve karını peritoneal bulgular ile ağrının tam yeri açısından yeniden muayene etmek",
                        "is_correct": True,
                        "explanation": "Önceki normal görüntüleme ilerleyen klinik bulguları geçersiz kılmaz. Lokal peritoneal irritasyon cerrahi bir nedenin sürdüğünü gösterir; olası cerrahi için çocuk aç tutulur.",
                        "new_finding": "Vital Bulgular: Ateş 38.6°C, KTA 132/dk, SS 26/dk, TA 102/64 mmHg, SpO2 %98, KDZ 2 sn. Bacaklarını karnına çekerek yatıyor. Sağ alt kadranda, klasik apendiks noktasının medialinde belirgin hassasiyet, istemsiz defans ve rebound. Diğer kadranlar rahat. Testisler normal, akciğer sesleri eşit."
                    },
                    {
                        "text": "Ateş nedeniyle idrar yolu enfeksiyonu düşünüp idrar tetkiki istemek, sonuç gelene kadar oral antibiyotik başlayıp oral sıvı vermek",
                        "is_correct": False,
                        "scenario_update": "İdrar tetkiki normal geldi; oral sıvı verilen çocuk kustu ve cerrahi değerlendirme gecikti.",
                        "teaching_point": "Karın muayenesi bulgularını açıklamayan tetkiklere odaklanmak tanıyı geciktirir."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar ve Ayrıntılı Görüntüleme",
                "question": "Apendiksi normal bildirilmiş ancak lokal periton irritasyonu olan bu çocukta hangi tetkik yaklaşımı uygundur?",
                "options": [
                    {
                        "text": "Terminal ileumu değerlendirmek için acil kolonoskopi planlamak ve hazırlık için oral barsak temizleme solüsyonu vermek",
                        "is_correct": False,
                        "scenario_update": "Oral solüsyon sonrası çocuk kustu ve ağrısı arttı; işlem güvenli bulunmadı.",
                        "teaching_point": "Akut peritoneal bulgularda kolonoskopi ve oral barsak hazırlığı kontrendikedir."
                    },
                    {
                        "text": "Ultrasonu yinelemek yerine ertesi sabah tekrar muayene etmek üzere çocuğu antibiyotiksiz olarak servise yatırmak",
                        "is_correct": False,
                        "scenario_update": "Gece ateş 39.5°C'ye çıktı ve yaygın hassasiyet gelişti.",
                        "teaching_point": "Peritoneal bulgusu olan ateşli çocukta tanısal değerlendirme ertelenmemelidir."
                    },
                    {
                        "text": "Ektopik mide mukozasını göstermek için teknesyum-99m perteknetat sintigrafisi planlamak ve sonuç gelene kadar çocuğu oral beslenmeyle izlemek",
                        "is_correct": False,
                        "scenario_update": "Sintigrafi ertesi güne planlandı; inflamasyonlu yapıda tanısal değeri sınırlıydı ve tedavi gecikti.",
                        "teaching_point": "Bu sintigrafi ağrısız rektal kanamada değerlidir; akut inflamatuvar tabloda ilk tetkik değildir."
                    },
                    {
                        "text": "Hemogram, CRP ve tam idrar istemek; deneyimli radyologla apendiks dışındaki yapıları da kapsayan ayrıntılı karın ultrasonu yaptırmak",
                        "is_correct": True,
                        "explanation": "Laboratuvar inflamasyonu destekler. Ultrasonun yalnızca apendikse odaklanması diğer nedenlerin atlanmasına yol açabilir; ileum, mezenter ve over-testis gibi yapılar da değerlendirilmelidir.",
                        "new_finding": "Lökosit 17.200/mm³ (%88 nötrofil), CRP 76 mg/L, tam idrar normal. Ultrason: retroçekal yerleşimli, 4 mm, basılabilen normal apendiks. Medialinde terminal ileumun antimezenterik kenarından kaynaklanan, kör sonlanan, 13 mm çaplı, kalın duvarlı, lümeni distandü tübüler yapı ve çevresinde inflamatuvar yağ dokusu."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Normal apendiks, sağ alt kadranda periton irritasyonu ve ultrasonda terminal ileumdan kaynaklanan inflame kör sonlanan yapı olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Crohn hastalığına bağlı terminal ileit",
                        "is_correct": False,
                        "scenario_update": "Kronik ishal, kilo kaybı ve büyüme geriliği yok; ileum duvarında segmenter kalınlaşma değil kör sonlanan yapı var.",
                        "teaching_point": "Crohn hastalığında kronik semptomlar ve uzun segment ileum duvar kalınlaşması beklenir."
                    },
                    {
                        "text": "Meckel divertiküliti",
                        "is_correct": True,
                        "explanation": "Terminal ileumun antimezenterik kenarından kaynaklanan, kör sonlanan inflame yapı Meckel divertikülünün iltihabını gösterir; klinik apandisiti taklit eder.",
                        "new_finding": "Tanı: İnflame Meckel Divertikülü (Meckel Divertiküliti)."
                    },
                    {
                        "text": "Retroçekal akut apandisit",
                        "is_correct": False,
                        "scenario_update": "Apendiks 4 mm, basılabilir ve çevresinde inflamasyon yok.",
                        "teaching_point": "Normal çaplı, basılabilen apendiks apandisit lehine değildir."
                    },
                    {
                        "text": "Omental infarkt",
                        "is_correct": False,
                        "scenario_update": "Ultrasonda hiperekoik omental kitle yok; tübüler inflame yapı ileumla ilişkili.",
                        "teaching_point": "Omental infarkt genellikle obez çocuklarda, ateşsiz ve sağ tarafta lokal ağrıyla seyreder."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Cerrahi",
                "question": "Bu çocuğun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Ektopik mide mukozasına bağlı inflamasyonu azaltmak için intravenöz proton pompası inhibitörü başlamak ve iyileşme olursa cerrahiden kaçınmak",
                        "is_correct": False,
                        "scenario_update": "Proton pompası inhibitörü inflamasyonu geriletmedi; çocuğun ateşi ve hassasiyeti sürdü.",
                        "teaching_point": "Asit baskılama inflame yapının kesin tedavisi değildir."
                    },
                    {
                        "text": "Ateş ve ağrı azaldığı için oral amoksisilin-klavulanat ile taburcu edip iki hafta sonra elektif cerrahi değerlendirme planlamak",
                        "is_correct": False,
                        "scenario_update": "Evde ağrı ve ateş yeniden başladı; çocuk perforasyon bulgularıyla geri geldi.",
                        "teaching_point": "İnflame yapı perforasyon riskini sürdürür; tedavisi cerrahidir."
                    },
                    {
                        "text": "Oral alımı kesip intravenöz sıvı, analjezi ve geniş spektrumlu antibiyotik vermek, çocuk cerrahisiyle acil laparoskopik rezeksiyon planlamak",
                        "is_correct": True,
                        "explanation": "İnflame yapı perforasyon ve obstrüksiyon riski taşır. Antibiyotik ve sıvı cerrahi hazırlığın parçasıdır; laparoskopik veya açık rezeksiyon kesin tedavidir.",
                        "new_finding": "Seftriakson ve metronidazol başlandı. Laparoskopide ileoçekal valvin 60 cm proksimalinde inflame, perforasyon öncesi evrede divertikül saptandı ve rezeke edildi; patolojide ektopik mide mukozası doğrulandı. Çocuk üçüncü gün taburcu edildi."
                    },
                    {
                        "text": "Görüntüleme eşliğinde perkütan drenaj yapıp antibiyotikle altı hafta izlemek ve kontrol ultrasonuna göre karar vermek",
                        "is_correct": False,
                        "scenario_update": "Drene edilecek apse olmadığı için girişim yapılamadı; zaman kaybedildi.",
                        "teaching_point": "Perkütan drenaj apse varlığında uygulanır; inflame yapı rezeksiyon gerektirir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y57",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "18 Aylık",
        "gender": "Kız",
        "complaint": "Üç gündür süren ishal sırasında başlayan uyuklama, kas seyirmeleri ve acil kapısında nöbet",
        "history": "Ailesi anlatıyor: 'Üç gündür sulu ishali ve kusması vardı. Kaybettiği sıvıyı yerine koymak için sürekli kaynamış su ve açık çay içirdik, tuzlu sıvı vermedik. Bugün öğleden sonra çok uyuklamaya başladı, kollarında ve bacaklarında sıçramalar oldu.' Acil kapısında 3 dakika süren, kendiliğinden duran jeneralize tonik-klonik nöbet geçirdi. Ateşi yok, travma yok. Tartı: 11 kg.",
        "final_diagnosis": "Ağır Semptomatik Hiponatremi (Hipotonik Sıvı Alımına Bağlı)",
        "disposition": "Sarı Alanda Hava Yolu Güvenliği, %3 NaCl Bolusu ile Akut Düzeltme ve Kontrollü Sodyum Yükselişi İçin Çocuk Yoğun Bakım Yatışı",
        "case_pearl": "Ishalli çocuğa elektrolitsiz sıvı (su, çay, seyreltilmiş mama) verilmesi sodyumu hızla düşürebilir; akut düşüş beyin ödemi, nöbet ve solunum durmasına yol açar. Nöbet, bilinç bozukluğu veya solunum değişikliği varsa %3 NaCl 2-3 mL/kg 10-15 dakikada verilir, belirtiler sürerse 2-3 kez tekrarlanır; hedef ilk saatlerde 4-6 mEq/L yükseliştir. İlk 24 saatte toplam yükseliş 8-10 mEq/L'yi geçmemelidir (osmotik demiyelinizasyon riski). Önleme için ishalde ORS kullanımı öğretilmelidir.",
        "steps": [
            {
                "stage_title": "Nöbet Yönetimi ve İlk Değerlendirme",
                "question": "Nöbeti kendiliğinden duran, postiktal ve kas seyirmeleri süren bu çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Ateşsiz nöbette santral sinir sistemi enfeksiyonunu dışlamak için lomber ponksiyon yapmak ve sonuç çıkana kadar asiklovir başlamak",
                        "is_correct": False,
                        "scenario_update": "Lomber ponksiyon için hazırlanırken çocuğun seyirmeleri arttı; elektrolitler bakılmamıştı.",
                        "teaching_point": "Ateşsiz ve ishal sonrası nöbette önce metabolik nedenler değerlendirilir."
                    },
                    {
                        "text": "İshale bağlı sıvı kaybı nedeniyle 20 mL/kg %0.45 NaCl ile %5 dekstroz bolusu vermek ve nöbeti dehidratasyona bağlamak",
                        "is_correct": False,
                        "scenario_update": "Hipotonik sıvı sonrası çocukta ikinci nöbet gelişti ve sodyum daha da düştü.",
                        "teaching_point": "Bolus sıvılar izotonik olmalıdır; hipotonik sıvı serbest su yükünü artırır."
                    },
                    {
                        "text": "Hava yolu ve solunumu güvenceye alıp oksijen vermek, damar yolu açmak, kapiller kan şekeri ve yatak başı kan gazında elektrolitlere bakmak",
                        "is_correct": True,
                        "explanation": "Nöbet sonrası hava yolu ve oksijenasyon önceliklidir. Hipoglisemi ve elektrolit bozuklukları ishalli çocukta nöbetin hızla düzeltilebilir nedenleridir; yatak başı kan gazı dakikalar içinde sodyumu gösterir.",
                        "new_finding": "Vital Bulgular: Ateş 36.9°C, KTA 148/dk, SS 28/dk, TA 106/66 mmHg, SpO2 %94 (oksijenle %99). Postiktal konfüze, kollarında seyirmeler sürüyor. Pupiller izokorik, ışık refleksi var; fokal defisit yok. Mukozalar nemli, KDZ 2 sn. Kan şekeri 98 mg/dL. Kan gazı: Na 116 mEq/L, K 3.8 mEq/L, Cl 86 mEq/L, pH 7.34."
                    },
                    {
                        "text": "Nöbet tekrarını önlemek için hemen intravenöz fenitoin yüklemesi yapıp kafa içi patolojiyi dışlamak amacıyla kontrastsız beyin tomografisi çekmek ve elektrolitleri sonrasında istemek",
                        "is_correct": False,
                        "scenario_update": "Fenitoin seyirmeleri durdurmadı; tomografi için beklerken çocuk yeniden nöbet geçirdi.",
                        "teaching_point": "Elektrolit bozukluğuna bağlı nöbette antiepileptikler etkisizdir; neden hızla düzeltilmelidir."
                    }
                ]
            },
            {
                "stage_title": "Acil Düzeltme",
                "question": "Serum sodyumu 116 mEq/L olan, seyirmeleri ve konfüzyonu süren bu çocukta acil tedavi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Sodyumu düzeltmek için 20 mL/kg serum fizyolojik bolusu vermek ve iki saat sonra sodyumu yeniden ölçmek",
                        "is_correct": False,
                        "scenario_update": "Serum fizyolojik sodyumu ancak 1-2 mEq/L yükseltti; seyirmeler sürdü.",
                        "teaching_point": "Nörolojik belirtili akut düşüşte izotonik sıvı yetersizdir; hipertonik salin gerekir."
                    },
                    {
                        "text": "Yalnızca sıvı kısıtlaması yapıp oral yoldan tuz tableti vermek ve sodyumun kendiliğinden yükselmesini beklemek",
                        "is_correct": False,
                        "scenario_update": "Bilinci bulanık çocuk tableti yutamadı; bir saat içinde yeniden nöbet geçirdi.",
                        "teaching_point": "Nörolojik belirti varsa kısıtlama ve oral tedavi yetersizdir; acil hipertonik salin gerekir."
                    },
                    {
                        "text": "%3 NaCl 3 mL/kg dozunu 10-15 dakikada intravenöz vermek, belirtiler sürerse tekrarlamak ve sodyumu yakından ölçmek",
                        "is_correct": True,
                        "explanation": "Hipertonik salin bolusu sodyumu hızla 2-3 mEq/L yükselterek beyin ödemini azaltır ve nöbeti sonlandırır. İlk hedef belirtilerin düzelmesi ve 4-6 mEq/L yükseliştir.",
                        "new_finding": "33 mL %3 NaCl 15 dakikada verildi. Kontrol sodyum 121 mEq/L; seyirmeler ve konfüzyon geriledi, çocuk gözlerini açıp annesini tanıdı."
                    },
                    {
                        "text": "Sodyumu birkaç saat içinde normale getirmek için yüksek hızda sürekli %3 NaCl infüzyonu başlamak ve hedefi 135 mEq/L olarak belirlemek",
                        "is_correct": False,
                        "scenario_update": "Altı saatte sodyum 132 mEq/L'ye yükseldi; çok hızlı düzeltme nedeniyle osmotik demiyelinizasyon riski oluştu.",
                        "teaching_point": "Akut düzeltmenin hedefi belirtilerin kontrolüdür; 24 saatte 8-10 mEq/L'den fazla yükselişten kaçınılır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "İshal sırasında yalnızca su ve çay içirilen, nöbet ve konfüzyonla gelen, serum sodyumu 116 mEq/L olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Viral ensefalit",
                        "is_correct": False,
                        "scenario_update": "Ateş yok; bulgular hipertonik salinle hızla düzeldi.",
                        "teaching_point": "Ensefalitte ateş, ilerleyici bilinç değişikliği ve beyin omurilik sıvısı bulguları beklenir."
                    },
                    {
                        "text": "Basit febril nöbet",
                        "is_correct": False,
                        "scenario_update": "Ateş yok ve serum sodyumu belirgin düşük.",
                        "teaching_point": "Febril nöbet tanısı ateş varlığı ve metabolik nedenlerin dışlanmasıyla konur."
                    },
                    {
                        "text": "Ağır semptomatik hiponatremi",
                        "is_correct": True,
                        "explanation": "Kayıpların elektrolitsiz sıvıyla yerine konması serbest su yükü oluşturarak sodyumu akut düşürür; nöbet ve konfüzyon beyin ödemine bağlı ağır belirtilerdir.",
                        "new_finding": "Tanı: Ağır Semptomatik Hiponatremi (hipotonik sıvı alımına bağlı)."
                    },
                    {
                        "text": "Hipoglisemik nöbet",
                        "is_correct": False,
                        "scenario_update": "Kan şekeri 98 mg/dL.",
                        "teaching_point": "Nöbetli her çocukta kan şekeri bakılmalıdır; burada normaldir."
                    }
                ]
            },
            {
                "stage_title": "İzlem ve Önleme",
                "question": "Belirtileri düzelen bu çocuğun sonraki tedavisi ve izlemi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Belirtiler düzeldiği için birkaç saat gözlem sonrası taburcu etmek ve aileye ishal geçene kadar bol su içirmelerini önermek",
                        "is_correct": False,
                        "scenario_update": "Evde bol su içirilen çocuk ertesi gün yeniden nöbetle getirildi.",
                        "teaching_point": "Sodyum normale yaklaşmadan taburculuk yapılmaz; ishalde sade su yerine ORS önerilir."
                    },
                    {
                        "text": "Yoğun bakımda 2-4 saatte bir sodyum ölçmek, 24 saatte yükselişi 8-10 mEq/L ile sınırlamak, izotonik sıvı vermek ve aileye ishalde ORS kullanımını öğretmek",
                        "is_correct": True,
                        "explanation": "Sık ölçüm aşırı hızlı düzeltmeyi önler. İzotonik idame sıvısı yeni düşüşü engeller. Aile eğitimi tekrarın önlenmesinde temeldir.",
                        "new_finding": "Yoğun bakımda izotonik sıvı sürdürüldü; sodyum 24 saatte 125, 48 saatte 132 mEq/L oldu. Yeni nöbet olmadı. Aileye ORS hazırlama ve kullanımı uygulamalı anlatıldı."
                    },
                    {
                        "text": "Yeni nöbetleri önlemek için sodyum 135 mEq/L olana kadar her saat %3 NaCl bolusunu tekrarlamak ve bu süre boyunca diğer tüm sıvıları tamamen kısıtlamak",
                        "is_correct": False,
                        "scenario_update": "Sodyum 12 saatte 18 mEq/L yükseldi; çocukta osmotik demiyelinizasyon açısından yüksek risk oluştu.",
                        "teaching_point": "Belirtiler düzeldikten sonra hipertonik bolus tekrarlanmaz; yükseliş sınırlandırılır."
                    },
                    {
                        "text": "Nöbet durduğu için sodyum ölçümünü bırakmak, idame sıvısı olarak %0.18 NaCl ve %5 dekstroz başlamak ve çocuğu genel servise yatırmak",
                        "is_correct": False,
                        "scenario_update": "Hipotonik idame sıvısıyla sodyum yeniden 118 mEq/L'ye düştü ve çocukta yeni seyirmeler başladı.",
                        "teaching_point": "Hasta çocuklarda hipotonik idame sıvısı hiponatremiyi ağırlaştırır; izlem sürdürülmelidir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y58",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "3 Yaşında",
        "gender": "Erkek",
        "complaint": "Üç gündür süren ishal ve kusma sonrası 24 saattir hiç idrar yapmama, solukluk ve halsizlik",
        "history": "Ailesi anlatıyor: 'Üç gündür günde on kez sulu ishali ve kusması var, ağızdan sıvı içiremedik. Ateşi için iki gündür ibuprofen şurubu veriyoruz. Son 24 saattir bezi kupkuru, hiç çiş yapmadı. Çok halsiz, gözlerini açmakta zorlanıyor. Böbrekleri iflas mı etti diye çok korkuyoruz.' Dışkıda kan yok. Bilinen böbrek hastalığı yok. Hastalık öncesi tartısı: 14 kg.",
        "final_diagnosis": "Dehidratasyona Bağlı Prerenal Akut Böbrek Hasarı",
        "disposition": "Sarı Alanda İzotonik Sıvı Bolusları, Nefrotoksik İlaçların Kesilmesi, İdrar Çıkışı ve Böbrek Fonksiyon İzlemi ile Servis Yatışı",
        "case_pearl": "Hipovolemide böbrek perfüzyonu azalır; tübüller sağlam olduğundan sodyum ve su tutulur (idrar sodyumu <20 mEq/L, FENa <%1, dansite yüksek, BUN/kreatinin oranı >20). Hızlı ve yeterli hacim replasmanıyla tablo genellikle 24-72 saatte geri döner. Uzarsa akut tübüler nekroza ilerleyebilir. NSAİİ'ler afferent arteriyolü daraltarak hasarı artırır ve kesilmelidir. İdrar çıkışı sıvı tedavisine yanıtın en iyi göstergesidir.",
        "steps": [
            {
                "stage_title": "Hacim Durumu ve Acil Resüsitasyon",
                "question": "24 saattir idrar yapmayan, halsiz bu 3 yaşındaki çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Ondansetron verip oral rehidratasyon solüsyonunu kaşıkla denemek ve çocuk idrar yapana kadar acil serviste beklemek",
                        "is_correct": False,
                        "scenario_update": "Halsiz çocuk sıvıyı yeterli içemedi; iki saat sonra perfüzyonu daha da bozuldu.",
                        "teaching_point": "Dolaşım bozukluğu bulgusu olan çocukta oral deneme yerine intravenöz bolus gerekir."
                    },
                    {
                        "text": "Perfüzyon, kan basıncı ve hidrasyonu değerlendirip mesanenin dolu olup olmadığına bakmak, damar yolu açıp 20 mL/kg izotonik sıvı bolusu vermek",
                        "is_correct": True,
                        "explanation": "İdrar yokluğunun en sık nedeni hipovolemidir; hızlı izotonik bolus perfüzyonu ve böbrek kan akımını düzeltir. Dolu mesane idrar retansiyonunu gösterir ve yaklaşımı değiştirir.",
                        "new_finding": "Vital Bulgular: Ateş 37.3°C, KTA 146/dk, SS 30/dk, TA 80/48 mmHg, SpO2 %98, KDZ 3.5 sn. Gözler çökük, mukozalar kuru, deri turgoru 2.5 sn. Ödem yok, akciğerler temiz. Suprapubik bölgede mesane ele gelmiyor, yatak başı ultrasonda mesane boş. 20 mL/kg serum fizyolojik verildi; KTA 124/dk, KDZ 2.5 sn."
                    },
                    {
                        "text": "Mesane kateteri takıp idrar gelmezse acil nefroloji konsültasyonu istemek ve sıvı tedavisini nefroloji önerisine kadar ertelemek",
                        "is_correct": False,
                        "scenario_update": "Kateterden idrar gelmedi; nefroloji beklenirken bir saat sıvı verilmedi ve taşikardi arttı.",
                        "teaching_point": "Hipovolemi bulgusu varsa sıvı resüsitasyonu konsültasyon beklenmeden başlanır."
                    },
                    {
                        "text": "24 saattir idrar yapmadığı için gelişmiş böbrek yetmezliği kabul edip sıvıyı kısıtlamak ve idrar çıkışını sağlamak için yüksek doz intravenöz furosemid vermek",
                        "is_correct": False,
                        "scenario_update": "Furosemid sonrası idrar gelmedi; kan basıncı daha da düştü ve çocuk letarjikleşti.",
                        "teaching_point": "Hipovolemik çocukta diüretik ve sıvı kısıtlaması perfüzyonu daha da bozar."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar Değerlendirmesi",
                "question": "Bolusa yanıt veren bu çocukta hangi tetkikler istenmelidir?",
                "options": [
                    {
                        "text": "BUN, kreatinin, elektrolitler, kan gazı ve tam idrar istemek; ilk idrarda sodyum, kreatinin ve dansiteye bakarak sodyum atılım fraksiyonunu hesaplamak",
                        "is_correct": True,
                        "explanation": "BUN/kreatinin oranı, düşük idrar sodyumu, FENa <%1 ve yüksek dansite tübül fonksiyonunun korunduğunu, yani hasarın perfüzyona bağlı olduğunu gösterir. Potasyum ve asidoz acil tedavi gerektirebilir.",
                        "new_finding": "BUN 102 mg/dL, kreatinin 1.9 mg/dL (bazal beklenen ~0.4), Na 135, K 5.0 mEq/L, HCO3 17 mmol/L. Bolustan sonraki ikinci saatte 35 mL idrar: dansite 1025, idrar sodyumu 11 mEq/L, FENa %0.4, idrar sedimenti temiz."
                    },
                    {
                        "text": "Glomerülonefrit ve diğer parankim hastalıklarını dışlamak için acil perkütan böbrek biyopsisi planlamak ve sıvı tedavisini biyopsi sonucuna göre ayarlamak",
                        "is_correct": False,
                        "scenario_update": "Biyopsi bu klinik tabloda endike değildi; nefroloji işlemi reddetti ve zaman kaybedildi.",
                        "teaching_point": "Böbrek biyopsisi açıklanamayan veya ilerleyici böbrek hasarında düşünülür."
                    },
                    {
                        "text": "Böbrekleri ayrıntılı görmek için intravenöz kontrastlı batın tomografisi çekmek ve laboratuvarı görüntüleme sonrasına bırakmak",
                        "is_correct": False,
                        "scenario_update": "Kontrast madde zaten bozulmuş böbrek fonksiyonunu daha da kötüleştirdi.",
                        "teaching_point": "Böbrek fonksiyonu bozulmuş çocukta nefrotoksik kontrast maddelerden kaçınılır; gerekirse ultrason yeterlidir."
                    },
                    {
                        "text": "Böbrek skarını değerlendirmek için DMSA sintigrafisi planlamak ve sonuç çıkana kadar çocuğu oral sıvıyla izlemek",
                        "is_correct": False,
                        "scenario_update": "Sintigrafi akut dönemde yönetime katkı sağlamadı; temel laboratuvar tetkikleri gecikti.",
                        "teaching_point": "DMSA sintigrafisi akut tabloda değil, seçilmiş olgularda geç dönemde kullanılır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Dehidratasyon sonrası idrar yokluğu, kreatinin artışı, idrar sodyumu 11 mEq/L, FENa %0.4 ve bolusa idrar çıkışıyla yanıt veren bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Posterior üretral valve bağlı obstrüksiyon",
                        "is_correct": False,
                        "scenario_update": "Mesane boş, idrar akımı bolus sonrası başladı ve bilinen idrar yolu sorunu yok.",
                        "teaching_point": "Postrenal nedenlerde dolu mesane ve hidronefroz beklenir."
                    },
                    {
                        "text": "Akut tübüler nekroz",
                        "is_correct": False,
                        "scenario_update": "FENa %1'in altında, idrar sodyumu düşük, dansite yüksek ve sediment temiz.",
                        "teaching_point": "Akut tübüler nekrozda FENa >%2, idrar sodyumu >40 mEq/L ve granüler silendirler görülür."
                    },
                    {
                        "text": "Dehidratasyona bağlı prerenal akut böbrek hasarı",
                        "is_correct": True,
                        "explanation": "Hipovolemiye bağlı azalmış böbrek perfüzyonunda tübüller sodyumu tutmaya devam eder; düşük idrar sodyumu, FENa <%1 ve sıvıya hızlı yanıt prerenal hasarı doğrular. NSAİİ kullanımı tabloya katkıda bulunmuştur.",
                        "new_finding": "Tanı: Dehidratasyona Bağlı Prerenal Akut Böbrek Hasarı (NSAİİ katkılı)."
                    },
                    {
                        "text": "Hemolitik üremik sendrom",
                        "is_correct": False,
                        "scenario_update": "Kanlı ishal öyküsü yok; anemi ve trombositopeni saptanmadı.",
                        "teaching_point": "Hemolitik üremik sendromda mikroanjiyopatik hemoliz ve trombositopeni böbrek hasarına eşlik eder."
                    }
                ]
            },
            {
                "stage_title": "Sıvı Tedavisi ve İzlem",
                "question": "Bu çocuğun sonraki tedavisi ve izlemi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Kreatinin yüksek olduğu için hemen periton diyalizi başlatmak üzere nefrolojiye devretmek ve sıvıyı idame hızının altında tutmak",
                        "is_correct": False,
                        "scenario_update": "Nefroloji diyaliz endikasyonu olmadığını belirtti; kısıtlı sıvı nedeniyle idrar çıkışı yeniden azaldı.",
                        "teaching_point": "Diyaliz hiperkalemi, sıvı yüklenmesi, ağır asidoz veya üremi gibi endikasyonlarda yapılır."
                    },
                    {
                        "text": "İdrar çıkışı başladığı için ateş için ibuprofene devam ederek çocuğu oral sıvıyla taburcu etmek ve bir hafta sonra kreatinin kontrolü yapmak",
                        "is_correct": False,
                        "scenario_update": "Evde yeterli içemeyen ve ibuprofen almaya devam eden çocuk iki gün sonra yeniden idrarsız getirildi.",
                        "teaching_point": "Kreatinin düşmeden ve oral alım güvenceye alınmadan taburculuk yapılmaz; NSAİİ kesilir."
                    },
                    {
                        "text": "Ibuprofeni kesip izotonik sıvıyla açığı ve idameyi vermek, idrar çıkışını ve sıvı dengesini saatlik izlemek, 12-24 saatte kreatinin ve elektrolitleri tekrarlamak",
                        "is_correct": True,
                        "explanation": "Hacim açığının kapatılması böbrek perfüzyonunu düzeltir. NSAİİ'ler hasarı artırır. Yeterli sıvıya rağmen idrar çıkışı düzelmezse intrinsik böbrek hasarı düşünülür ve nefroloji ile değerlendirilir.",
                        "new_finding": "İbuprofen kesildi, izotonik sıvı sürdürüldü. İdrar çıkışı 1.5-2 mL/kg/saat oldu. Kreatinin 24 saatte 0.9, 72 saatte 0.4 mg/dL'ye geriledi; çocuk dördüncü gün taburcu edildi."
                    },
                    {
                        "text": "İdrar çıkışını artırmak için saatlik 20 mL/kg bolusları idrar dansitesi normale dönene kadar tekrarlamak ve furosemid eklemek",
                        "is_correct": False,
                        "scenario_update": "Tekrarlanan boluslar sonrası çocukta göz kapağı ödemi ve takipne gelişti.",
                        "teaching_point": "Bolus yalnızca perfüzyon bozukluğu sürüyorsa tekrarlanır; sonrasında hesaplanmış açık ve idame verilir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y59",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "5 Yaşında",
        "gender": "Kız",
        "complaint": "Nefrotik sendrom tanılı çocukta aniden başlayan ateş, yaygın şiddetli karın ağrısı ve kusma",
        "history": "Ailesi anlatıyor: 'Bir aydır nefrotik sendrom atağında, günlük yüksek doz prednizolon kullanıyor; karnı ve bacakları şiş. Dün gece aniden ateşi 38.8°C'ye çıktı, karnının her yerinde çok şiddetli ağrı başladı, üç kez kustu. Nefes alırken bile karnının battığını söylüyor, kıpırdamadan yatıyor.' Pnömokok aşıları eksik. Tartı: 20 kg (ödemli; kuru ağırlığı 17 kg).",
        "final_diagnosis": "Nefrotik Sendrom Zemininde Spontan Bakteriyel Peritonit",
        "disposition": "Sarı Alanda Kan Kültürü ve Tanısal Parasentez Sonrası İntravenöz Seftriakson, Dikkatli Hacim Desteği ve Stres Dozu Steroid ile Servis Yatışı",
        "case_pearl": "Nefrotik sendromda idrarla immünoglobulin ve kompleman kaybı, asit ve steroid kullanımı nedeniyle kapsüllü bakterilerle (en sık S. pneumoniae) asit enfeksiyonu gelişebilir. Asit sıvısında nötrofil >250/mm³ tanı koydurur. Tedavi pnömokok ve gram negatifleri kapsayan üçüncü kuşak sefalosporindir. Ödemli olmasına rağmen damar içi hacim azalmış olabilir; hipovolemi ve tromboz açısından dikkatli olunmalıdır. Uzun süreli steroid kullananlarda stres dozu gerekir; asit varlığında steroid bulguları maskeleyebilir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Sepsis Yaklaşımı",
                "question": "Nefrotik sendrom atağında, yüksek doz steroid kullanan, ateşli ve yaygın karın ağrılı bu çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Sepsis ve damar içi hacim azlığı bulgularını değerlendirmek, karını ayrıntılı muayene etmek, damar yolu açıp kan kültürü almak",
                        "is_correct": True,
                        "explanation": "Ödemli çocukta damar içi hacim azalmış olabilir; taşikardi ve soğuk ekstremiteler hipovolemiyi düşündürür. Steroid kullanımı karın bulgularını hafifletebilir. Kan kültürü antibiyotik öncesi alınmalıdır.",
                        "new_finding": "Vital Bulgular: Ateş 38.7°C, KTA 138/dk, SS 32/dk, TA 96/60 mmHg, SpO2 %98, KDZ 3 sn, ekstremiteler soğuk. Periorbital ve pretibial gode bırakan ödem. Karında masif asit, dalgalanma hissi; tüm kadranlarda istemsiz defans ve yaygın rebound. Bağırsak sesleri azalmış. Kan kültürü alındı."
                    },
                    {
                        "text": "Ateşi uzun süreli steroid kullanımının yan etkisine bağlayıp prednizolonu hemen kesmek ve oral antipiretikle çocuğu gözlem odasına almak",
                        "is_correct": False,
                        "scenario_update": "Steroidin ani kesilmesi hipotansiyona katkıda bulundu; enfeksiyon kaynağı aranmadı.",
                        "teaching_point": "Uzun süre steroid kullanan çocukta ilaç aniden kesilmez; stres altında doz artırılabilir."
                    },
                    {
                        "text": "Yaygın karın hassasiyeti nedeniyle perfore apandisit düşünüp doğrudan çocuk cerrahisine laparotomi için yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Cerrahi ekip, nefrotik çocukta asit enfeksiyonunun önce dışlanması gerektiğini belirterek laparotomiyi erteledi.",
                        "teaching_point": "Nefrotik sendromlu çocukta yaygın karın bulguları çoğunlukla cerrahi dışı bir enfeksiyondan kaynaklanır."
                    },
                    {
                        "text": "Karındaki sıvıyı azaltmak için intravenöz albümin ve furosemid vermek, ağrı azalırsa çocuğu nefroloji servisine yatırmak",
                        "is_correct": False,
                        "scenario_update": "Furosemid sonrası kan basıncı düştü ve taşikardi arttı; ateşin nedeni araştırılmadı.",
                        "teaching_point": "Ateşli, hipovolemik ve karın bulguları olan çocukta diüretik tehlikelidir; önce enfeksiyon değerlendirilir."
                    }
                ]
            },
            {
                "stage_title": "Parasentez ve Laboratuvar",
                "question": "Kan kültürü alınan bu çocukta tanıyı kesinleştirmek için hangi tetkik yapılmalıdır?",
                "options": [
                    {
                        "text": "Ultrason eşliğinde tanısal parasentez yapıp asitte hücre sayımı, Gram boyama ve kültür istemek; hemogram, CRP, albümin ve kreatinine bakmak",
                        "is_correct": True,
                        "explanation": "Asit sıvısında nötrofil sayısı >250/mm³ tanı koydurur; Gram boyama ve kan kültürü şişelerine ekilen kültür etkeni belirler. Albümin ve kreatinin hacim durumu ve böbrek fonksiyonunu gösterir.",
                        "new_finding": "Asit sıvısı bulanık: lökosit 1850/mm³ (%86 nötrofil; nötrofil 1590/mm³), Gram boyamada gram pozitif diplokoklar. Kan: lökosit 18.200/mm³, CRP 88 mg/L, albümin 1.8 g/dL, kreatinin 0.5 mg/dL."
                    },
                    {
                        "text": "Parasentezin kanama riski taşıdığını düşünerek yapmamak ve tanıyı kesinleştirmek için tanısal laparoskopi planlamak",
                        "is_correct": False,
                        "scenario_update": "Laparoskopi genel anestezi gerektirdi; hemodinamik olarak hassas çocukta risk ve gecikme oluştu.",
                        "teaching_point": "Ultrason eşliğinde parasentez güvenli ve tanısaldır; cerrahi tanısal yöntem ilk tercih değildir."
                    },
                    {
                        "text": "Karın ağrısının kaynağını göstermek için intravenöz kontrastlı batın tomografisi çekmek ve sonuca göre antibiyotik kararı vermek",
                        "is_correct": False,
                        "scenario_update": "Tomografi yaygın asit gösterdi ancak sıvının enfekte olup olmadığını ayırt edemedi; tedavi gecikti.",
                        "teaching_point": "Asit enfeksiyonunun tanısı görüntülemeyle değil, sıvı analiziyle konur."
                    },
                    {
                        "text": "Yalnızca tam idrar tetkiki ve idrar kültürü göndermek, proteinüri arttıysa ateşi nefrotik atağın alevlenmesine bağlayıp steroid dozunu artırmak",
                        "is_correct": False,
                        "scenario_update": "İdrar tetkiki enfeksiyon kaynağını göstermedi; asit enfeksiyonu tedavisiz kaldı.",
                        "teaching_point": "Nefrotik atak ateş yapmaz; ateşli nefrotik çocukta ciddi enfeksiyon aranmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Nefrotik sendromlu çocukta ateş, yaygın karın hassasiyeti ve asit sıvısında 1590/mm³ nötrofil ile gram pozitif diplokoklar saptanırsa tanı nedir?",
                "options": [
                    {
                        "text": "Akut pankreatit",
                        "is_correct": False,
                        "scenario_update": "Asit sıvısında belirgin nötrofil ve bakteri var; tablo enfeksiyonu gösteriyor.",
                        "teaching_point": "Steroid kullananlarda pankreatit görülebilir ancak asitte bakteri beklenmez."
                    },
                    {
                        "text": "Spontan bakteriyel peritonit",
                        "is_correct": True,
                        "explanation": "Nefrotik zeminde asit sıvısında nötrofil >250/mm³ ve tek tip gram pozitif diplokok (olası pnömokok) cerrahi odak olmadan gelişen spontan bakteriyel peritoniti doğrular.",
                        "new_finding": "Tanı: Nefrotik Sendrom Zemininde Spontan Bakteriyel Peritonit (olası S. pneumoniae)."
                    },
                    {
                        "text": "Perfore apandisite bağlı sekonder peritonit",
                        "is_correct": False,
                        "scenario_update": "Tek bir mikroorganizma görüldü; çoklu bakteri, serbest hava veya lokal odak yok.",
                        "teaching_point": "Sekonder peritonitte asitte çoklu flora, çok yüksek protein ve düşük glukoz beklenir."
                    },
                    {
                        "text": "Renal ven trombozu",
                        "is_correct": False,
                        "scenario_update": "Hematüri ve böğür ağrısı yok; asit enfeksiyonu bulguları tabloyu açıklıyor.",
                        "teaching_point": "Nefrotik sendromda tromboz riski yüksektir ancak burada tablo enfeksiyöz."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu çocuğun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Asiti tamamen boşaltmak için büyük hacimli parasentez yapmak ve enfeksiyonu kontrol etmek için laparotomiyle periton lavajı planlamak",
                        "is_correct": False,
                        "scenario_update": "Büyük hacimli boşaltma sonrası hipotansiyon gelişti; cerrahi ekip laparotomiyi gereksiz buldu.",
                        "teaching_point": "Spontan enfeksiyon antibiyotikle tedavi edilir; cerrahi lavaj gerekmez."
                    },
                    {
                        "text": "Antipiretik sonrası ağrı ve ateş azalınca çocuğu oral amoksisilin ile taburcu etmek ve steroid tedavisini aynı dozda sürdürmesini önermek",
                        "is_correct": False,
                        "scenario_update": "Evde ateş sürdü; çocuk hipotansiyonla geri getirildi.",
                        "teaching_point": "Asit enfeksiyonu parenteral tedavi ve hastane izlemi gerektirir."
                    },
                    {
                        "text": "Enfeksiyonla savaşmak için steroidi tamamen kesip intravenöz immünoglobulin vermek ve antibiyotiği kültür sonucuna kadar ertelemek",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik gecikti ve steroidin ani kesilmesiyle çocukta dirençli hipotansiyon gelişti.",
                        "teaching_point": "Antibiyotik kültür alınır alınmaz başlanır; steroid aniden kesilmez."
                    },
                    {
                        "text": "İntravenöz seftriakson başlamak, hipovolemi varsa albümin ve izotonik sıvı vermek, stres dozu steroid planlamak ve tromboz açısından izlemek",
                        "is_correct": True,
                        "explanation": "Üçüncü kuşak sefalosporin pnömokok ve gram negatifleri kapsar; 7-10 gün verilir. Damar içi hacim azlığında albümin desteği perfüzyonu düzeltir. Uzun süreli steroid kullananlarda adrenal baskılanma olabileceğinden stres dozu düşünülür. İyileşme sonrası aşılar tamamlanır.",
                        "new_finding": "Seftriakson başlandı, albümin ve izotonik sıvıyla perfüzyon düzeldi, stres dozu hidrokortizon planlandı. Kan ve asit kültüründe penisiline duyarlı S. pneumoniae üredi. 72 saatte ateş düştü; tedavi 10 güne tamamlandı ve pnömokok aşıları planlandı."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y60",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "2 Yaşında",
        "gender": "Erkek",
        "complaint": "Oyuncak kumandasındaki yassı yuvarlak pili yuttuktan sonra göğüs ağrısı, salya akıtma ve yutamama",
        "history": "Ailesi anlatıyor: 'Yaklaşık 45 dakika önce oyuncak arabanın kumandasının kapağını açmış, içindeki madeni para büyüklüğündeki yassı yuvarlak lityum pili ağzına atıp yutmuş. O andan beri göğsünün üstünü gösterip ağlıyor, tükürüğünü yutamıyor, salyası akıyor. Su içirmeye çalıştık, hemen öğürüp çıkardı.' Öksürük ve nefes darlığı yok. Bilinen hastalığı yok. Tartı: 12 kg.",
        "final_diagnosis": "Özofagusta Takılı Düğme Pil",
        "disposition": "Sarı Alanda Oral Alımın Kesilmesi, Bal Uygulaması ve İlk 2 Saat İçinde Acil Endoskopik Çıkarma, Sonrasında Gecikmiş Komplikasyon İzlemi",
        "case_pearl": "Özofagusta takılan lityum düğme pil, mukozada hidroksit iyonu oluşturarak 2 saat içinde ciddi yanık yapabilir; perforasyon, trakeoözofageal fistül ve aortoözofageal fistül gelişebilir. Çıkarma süresi saatlerle ölçülür. Çocuk 1 yaşından büyükse ve yutma 12 saat içindeyse endoskopiyi geciktirmeden 10 dakikada bir 10 mL bal verilmesi (en fazla 6 doz) hasarı azaltır. Ön-arka grafide çift halka, yan grafide basamaklanma görülür. Çıkarma sonrası haftalarca gecikmiş komplikasyonlar açısından izlem gerekir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Acil Önlemler",
                "question": "45 dakika önce yassı yuvarlak lityum pil yutan, salya akıtan ve yutamayan bu 2 yaşındaki çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Hava yolunu değerlendirip oral alımı kesmek, işlemi geciktirmeden 10 mL bal vermek, acil grafi çekip endoskopi ekibini çağırmak",
                        "is_correct": True,
                        "explanation": "Salya ve yutamama özofagusta takılmayı düşündürür. 1 yaşından büyük çocukta ilk 12 saat içinde bal, pil yüzeyini kaplayarak mukoza hasarını azaltır; ancak çıkarma işlemi asla geciktirilmez.",
                        "new_finding": "Vital Bulgular: Ateş 37.0°C, KTA 128/dk, SS 26/dk, TA 94/56 mmHg, SpO2 %99. Ajite, göğsünün üstünü gösteriyor, salya akıyor. Stridor ve solunum sıkıntısı yok, akciğer sesleri eşit. Hematemez yok. 10 mL bal verildi; endoskopi ekibi bilgilendirildi."
                    },
                    {
                        "text": "Pili mideye itmek için bol su ve ekmek yedirmek, ardından dışkıyla çıkmasını beklemek üzere aileyi evde izleme yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk suyu ve ekmeği kustu; özofagusta takılı pil yerinde kalmaya devam etti.",
                        "teaching_point": "Özofagusta takılı cisim için zorlama beslenme aspirasyon riskini artırır ve hasarı durdurmaz."
                    },
                    {
                        "text": "Pilin ağızdan çıkması için ipeka şurubu ile kusturmaya çalışmak ve yarım saat içinde kusma olmazsa boyun-göğüs grafisi çekmek",
                        "is_correct": False,
                        "scenario_update": "Kusturma girişimi sonrası çocuk öğürdü ama pil çıkmadı; aspirasyon riski oluştu.",
                        "teaching_point": "Yutulan cisimlerde kusturma kontrendikedir; aspirasyon riskini artırır."
                    },
                    {
                        "text": "Çocuk stabil olduğu için ailenin aç kalma süresini tamamlamasını bekleyip endoskopiyi ertesi sabaha planlamak",
                        "is_correct": False,
                        "scenario_update": "Bekleme süresinde çocukta hematemez gelişti; endoskopide derin özofagus yanığı saptandı.",
                        "teaching_point": "Bu tabloda endoskopi aç kalma süresi beklenmeden acil yapılır; hasar dakikalar-saatler içinde gelişir."
                    }
                ]
            },
            {
                "stage_title": "Görüntüleme",
                "question": "Bal verilen ve endoskopi ekibi bilgilendirilen bu çocukta hangi görüntüleme yapılmalıdır?",
                "options": [
                    {
                        "text": "Özofagus hasarını değerlendirmek için endoskopiden önce intravenöz kontrastlı toraks tomografisi çekmek",
                        "is_correct": False,
                        "scenario_update": "Tomografi endoskopiyi bir saat geciktirdi; bu sürede mukoza hasarı ilerledi.",
                        "teaching_point": "Tomografi gerekirse çıkarma sonrası komplikasyon değerlendirmesi için yapılır; çıkarmayı geciktirmez."
                    },
                    {
                        "text": "Cismin yerini ve özofagus hasarını kesinleştirmek için oral kontrastlı özofagus grafisi çekmek ve kontrastın mideye geçişini izlemek",
                        "is_correct": False,
                        "scenario_update": "Çocuk kontrastı aspire etti ve öksürmeye başladı.",
                        "teaching_point": "Yutamayan çocukta oral kontrast aspirasyon riski taşır ve gereksizdir."
                    },
                    {
                        "text": "Boyun, göğüs ve karını kapsayan ön-arka ve yan grafi çekmek; cismin yerini, şeklini ve kenar özelliklerini değerlendirmek",
                        "is_correct": True,
                        "explanation": "Ön-arka grafide çift halka, yan grafide basamaklanma lityum pili madeni paradan ayırır. Yan grafi negatif kutbun yönünü ve hasarın en çok olacağı tarafı gösterir.",
                        "new_finding": "Ön-arka ve yan grafi: üst özofagusta (C6-T1 düzeyi) 20 mm çaplı yuvarlak metalik opasite; ön-arka görüntüde çift halka, yan görüntüde kenarda basamaklanma. Cilt altı amfizem ve mediastinal hava yok.",
                        "image": "assets/images/adbg_button_battery.png",
                        "image_caption": "Boyun-Göğüs Grafisi (Ön-Arka ve Yan)"
                    },
                    {
                        "text": "Radyasyon riskini azaltmak için grafi çekmeden yalnızca metal dedektörüyle yerini belirlemek ve endoskopiyi buna göre planlamak",
                        "is_correct": False,
                        "scenario_update": "Dedektör cismin şeklini ve türünü göstermedi; madeni para ile pil ayrımı yapılamadı.",
                        "teaching_point": "Grafi cismin türünü, yerini ve komplikasyonları gösterdiği için zorunludur."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Grafide üst özofagusta çift halka ve basamaklanma gösteren 20 mm'lik yuvarlak metalik opasite saptanan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Özofagusta takılı düğme pil",
                        "is_correct": True,
                        "explanation": "Öyküyle birlikte çift halka ve basamaklanma işareti özofagusta takılı lityum düğme pili doğrular; acil endoskopik çıkarma gerektirir.",
                        "new_finding": "Tanı: Özofagusta Takılı Lityum Düğme Pil."
                    },
                    {
                        "text": "Retrofaringeal apse",
                        "is_correct": False,
                        "scenario_update": "Ateş ve boyun hareket kısıtlılığı yok; grafide metalik cisim var.",
                        "teaching_point": "Retrofaringeal apse ateş, boyun sertliği ve prevertebral yumuşak doku genişlemesiyle seyreder."
                    },
                    {
                        "text": "Akut viral krup",
                        "is_correct": False,
                        "scenario_update": "Stridor ve havlar tarzda öksürük yok; yutma öyküsü ve metalik cisim var.",
                        "teaching_point": "Krupta inspiratuvar stridor ve havlar öksürük öne çıkar."
                    },
                    {
                        "text": "Özofagusta takılı madeni para",
                        "is_correct": False,
                        "scenario_update": "Madeni para grafide tek, homojen bir disk olarak görülür; çift halka ve basamaklanma yoktur.",
                        "teaching_point": "Çift halka işareti lityum pili madeni paradan ayırır ve aciliyeti belirler."
                    }
                ]
            },
            {
                "stage_title": "Çıkarma ve İzlem",
                "question": "Bu çocuğun tedavi ve izlem planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "İlk 2 saat içinde genel anestezi altında endoskopik çıkarma yapmak, mukoza hasarını değerlendirmek ve gecikmiş fistül-perforasyon belirtileri için haftalarca izlemek",
                        "is_correct": True,
                        "explanation": "Hasar süreyle orantılı olduğundan çıkarma acil yapılır. Endoskopide yanığın derinliği ve yönü kaydedilir; aortoözofageal fistül gibi hayatı tehdit eden komplikasyonlar haftalar sonra gelişebileceğinden aile hematemez, ateş ve göğüs ağrısı konusunda bilgilendirilir.",
                        "new_finding": "Yutmadan 1 saat 40 dakika sonra endoskopik olarak çıkarıldı; arka duvarda yüzeyel yanık saptandı, asetik asitle yıkandı. Aileye gecikmiş komplikasyon belirtileri anlatıldı; iki hafta sonraki kontrolde yutma normaldi."
                    },
                    {
                        "text": "Mukozayı korumak için intravenöz proton pompası inhibitörü ve sukralfat başlamak, pil mideye geçebileceği için 24 saat sonra kontrol grafisiyle endoskopi gereksinimini değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Bekleme sırasında mukoza hasarı ilerledi; endoskopide derin nekroz saptandı.",
                        "teaching_point": "İlaçlar çıkarmanın yerini tutmaz; pil acilen çıkarılmalıdır."
                    },
                    {
                        "text": "Acil serviste sedasyonsuz Foley kateteriyle körlemesine çekerek pili çıkarmak ve çocuğu hemen taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Girişim sırasında çocuk öğürdü ve pil hava yoluna doğru yer değiştirdi; acil anestezi gerekti.",
                        "teaching_point": "Lityum pil doğrudan görüş altında çıkarılmalı ve mukoza hasarı değerlendirilmelidir."
                    },
                    {
                        "text": "Pilin mideye geçmesi için laksatif vermek ve dışkıyla çıkana kadar günlük grafiyle evde izlemek",
                        "is_correct": False,
                        "scenario_update": "Pil özofagusta kaldı; ikinci gün ateş ve hematemez gelişti.",
                        "teaching_point": "Özofagustaki pil kendiliğinden ilerlemeyi beklemeden acil çıkarılmalıdır."
                    }
                ]
            }
        ]
    }
]
