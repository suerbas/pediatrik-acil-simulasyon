# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - S16 - S20 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "S16",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "7 Yaş",
        "gender": "Erkek",
        "complaint": "Fındıklı çikolata yedikten 15 dakika sonra vücutta yaygın kaşıntılı kabarıklıklar, dudaklarda şişlik, ses kısıklığı ve kıvrandırıcı karın ağrısı",
        "history": "Ailesi 7 yaşındaki (25 kg) erkek çocuğu kucaklarında Sarı Alana getiriyor: 'Okuldan gelince arkadaşının ikram ettiği fındıklı çikolatadan iki ısırık aldı. Yaklaşık 10-15 dakika içinde boynu ve gövdesi kıpkırmızı olup kabardı, dudakları şişti. Şimdi boğazım düğümleniyor diyor, sesi boğuklaştı, hafif hırıltısı başladı ve karnım çok ağrıyor diyerek iki büklüm kıvranıyor.'",
        "final_diagnosis": "Akut Sistemik Anafilaksi (Besin Kaynaklı IgE Aracılı Tip 1 Hipersensitivite Reaksiyonu)",
        "disposition": "Sarı Alanda Acil İntramusküler Adrenalin (0.01 mg/kg) + Oksijen + İV Kristaloid Desteği + En Az 6-8 Saatlik Bifazik Reaksiyon Monitörizasyonu ve Otoenjektör Reçetesi ile Taburculuk",
        "case_pearl": "Anafilaksi, alerjen maruziyeti sonrası dakikalar içinde cilt/mukoza bulgularına (ürtiker, anjiyoödem) ek olarak solunum (stridor, bronkospazm, dispne), dolaşım (hipotansiyon, taşikardi, hipoperfüzyon) veya şiddetli gastrointestinal semptomların (kıvrandırıcı kolik karın ağrısı, tekrarlayan kusma) eşlik ettiği yaşamı tehdit eden sistemik reaksiyondur. Tek birinci basamak hayat kurtarıcı ilaç uyluk anterolateral (vastus lateralis) kasına uygulanan İNTRAMUSKÜLER ADRENALİNDİR (1:1000, 0.01 mg/kg, çocukta maks 0.3-0.5 mg). Hasta sırtüstü yatırılıp bacakları yükseltilmeli, boş ventrikül sendromu riski nedeniyle aniden dik oturtulmamalı veya ayağa kaldırılmamalıdır. Bifazik reaksiyon riskine karşı en az 6-8 saat izlenmeli ve adrenalin otoenjektörü eğitimiyle taburcu edilmelidir.",
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Hasta Pozisyonu",
                "question": "Şüpheli besin alımı sonrası cilt bulguları, ses kısıklığı ve karın ağrısı ile başvuran 7 yaşındaki (25 kg) çocukta ilk değerlendirme ve pozisyonlandırma yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Hastayı solunumunu rahatlatmak amacıyla sedyede tam dik oturtmak, vital bulgularını ölçmek ve ağızdan hızlı etkili setirizin şurubu içirerek gözleme almak",
                        "is_correct": False,
                        "scenario_update": "Dik oturtulan çocukta venöz dönüşün aniden azalmasıyla baş dönmesi ve hipotansiyon gelişti; ayrıca yutma güçlüğü nedeniyle oral şurubu aspire etme tehlikesi yaşandı.",
                        "teaching_point": "Sistemik aşırı duyarlılık tablolarında hasta aniden dik oturtulmamalı veya ayağa kaldırılmamalıdır; üst hava yolu ödemi bulgusu varken oral ilaç verilmesi aspirasyon riski taşır."
                    },
                    {
                        "text": "Hastayı hızla sırtüstü yatırıp alt ekstremitelerini yükseltmek, havayolu açıklığını, solunum seslerini, periferik perfüzyonu ve kan basıncını değerlendirerek monitörize oksijen başlamak",
                        "is_correct": True,
                        "explanation": "Çoklu sistem tutulumu düşündüren akut aşırı duyarlılık tablolarında venöz dönüşü korumak için hasta supin pozisyona alınmalı ve hızla ABCDE değerlendirmesi yapılmalıdır.",
                        "new_finding": "Vital Bulgular: KTA 142/dk, SS 30/dk, TA 84/50 mmHg, SpO2 %93, KDZ 3 saniye. Fizik Muayene: Alt ve üst dudakta belirgin ödem, uvula ödemli, gövdede yaygın eritematöz plaklar, inspiratuar kaba ses ve ses kısıklığı, oskültasyonda bilateral ekspiratuar hışıltı, batında yaygın hassasiyet mevcut."
                    },
                    {
                        "text": "Öncelikle alerjen spesifik IgE ve triptaz düzeyi için kan örneği alıp damar yolu açmak, laboratuvar sonuçları çıkana kadar ilaç uygulamadan izlemek",
                        "is_correct": False,
                        "scenario_update": "Damar yolu açılması ve kan alınması sürecinde geçen dakikalar içinde üst hava yolu ödemi ilerledi, inspiratuar ses belirginleşti ve oksijen satürasyonu %88 düzeyine geriledi.",
                        "teaching_point": "Akut solunum ve dolaşım tutulumu olan aşırı duyarlılık reaksiyonlarında tanı tamamen klinik bulgulara dayanır; laboratuvar tetkikleri acil müdahaleyi asla geciktirmemelidir."
                    },
                    {
                        "text": "Solunum sıkıntısını gidermek için öncelikle soğuk buhar ve nebulize salbutamol uygulamak, cilt döküntüleri için topikal kortikosteroid losyon sürerek yanıtı beklemek",
                        "is_correct": False,
                        "scenario_update": "Nebulize salbutamol uygulamasına rağmen hastanın ses kısıklığı ve üst hava yolu obstrüksiyon bulguları gerilemedi, arteriyel kan basıncı 76/42 mmHg düzeyine düştü.",
                        "teaching_point": "Nebulize bronkodilatörler üst hava yolu ödemini ve sistemik vasküler permeabilite artışını düzeltmez; yalnızca birincil parenteral tedaviye ek destek olarak kullanılabilir."
                    }
                ]
            },
            {
                "stage_title": "Acil Farmakolojik Müdahale ve Uygulama Yolu",
                "question": "Üst hava yolu ödemi, bronkospazm ve sınırda hipotansiyonu saptanan 25 kg ağırlığındaki bu hastada derhal uygulanması gereken ilk basamak ilaç ve uygulama şekli hangisidir?",
                "options": [
                    {
                        "text": "Damar yolundan 1 mg/kg metilprednizolon ve 1 mg/kg feniramin maleat yavaş puşe olarak uygulamak, klinik yanıt olmazsa ikinci basamakta vazopresör eklemek",
                        "is_correct": False,
                        "scenario_update": "İntravenöz antihistaminik ve kortikosteroid uygulamasından 10 dakika sonra hastanın stridoru şiddetlendi, siyanoz gelişti ve kan basıncı 68/35 mmHg düzeyine geriledi.",
                        "teaching_point": "H1-antihistaminikler yalnızca cilt semptomlarını hafifletir, kortikosteroidlerin etkisi ise saatler sonra başlar; her iki ilaç da akut laringeal ödemi ve şoku önleyemez."
                    },
                    {
                        "text": "1:1000 konsantrasyondaki adrenalinden 0.25 mg çekerek sulandırmadan doğrudan periferik damar yolundan hızlı intravenöz bolus şeklinde puşe etmek ve sıvı yüklemek",
                        "is_correct": False,
                        "scenario_update": "Konsantre intravenöz adrenalin bolusu sonrasında hastada şiddetli hipertansif atak, göğüs ağrısı ve monitörde polimorfik ventriküler ekstrasistoller ile taşiaritmi gelişti.",
                        "teaching_point": "1:1000 konsantrasyondaki adrenalin yalnızca intramusküler kullanım içindir; doğrudan intravenöz bolus uygulanması ölümcül ventriküler aritmilere ve intrakraniyal kanamaya yol açabilir."
                    },
                    {
                        "text": "1:1000 konsantrasyondaki adrenalinden 0.25 mg dozunda uyluk anterolateral vastus lateralis kasına intramusküler uygulamak ve izotonik kristaloid desteği başlamak",
                        "is_correct": True,
                        "explanation": "Alfa-1 vazokonstriktör etkisiyle mukozal ödemi azaltan, beta-2 etkisiyle bronkodilatasyon sağlayan ve mast hücre degranülasyonunu durduran tek birinci basamak tedavi intramusküler adrenalindir.",
                        "new_finding": "Sol vastus lateralis kasına 0.25 mg intramusküler adrenalin uygulandı ve 20 mL/kg %0.9 NaCl infüzyonu başlandı. 5 dakika içinde ses kısıklığı ve stridor geriledi, SpO2 %98, TA 102/64 mmHg, KTA 116/dk ölçüldü, döküntüler solmaya başladı."
                    },
                    {
                        "text": "1:1000 konsantrasyondaki adrenalinden 0.25 mg dozunda kolun deltoid bölgesine cilt altına enjekte etmek ve eş zamanlı nebulize budesonid tedavisi başlamak",
                        "is_correct": False,
                        "scenario_update": "Subkutan enjeksiyon sonrası ciltteki vazokonstriksiyon nedeniyle ilacın sistemik emilimi gecikti, 15 dakika geçmesine rağmen solunum sıkıntısı ve hipotansiyon düzelmedi.",
                        "teaching_point": "Uyluk anterolateral (vastus lateralis) kasına intramusküler uygulama, subkutan veya deltoid kası uygulamasına göre çok daha hızlı ve yüksek zirve plazma konsantrasyonu sağlar."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Alerjen besin teması sonrası dakikalar içinde cilt-mukoza, solunum ve gastrointestinal sistem bulgularının birlikte geliştiği bu tablonun kesin tanısı nedir?",
                "options": [
                    {
                        "text": "Besin Kaynaklı Akut Sistemik Anafilaksi",
                        "is_correct": True,
                        "explanation": "Bilinen veya olası bir alerjen maruziyeti sonrası dakikalar içinde cilt/mukoza tutulumuna solunum ve persistan gastrointestinal bulguların eşlik etmesi WAO/EAACI kriterlerine göre kesin anafilaksi tanısı koydurur.",
                        "new_finding": "Kesin tanı: Besin Kaynaklı Akut Sistemik Anafilaksi. İlk doz İM adrenalin ile havayolu ve dolaşım stabilizasyonu sağlandı."
                    },
                    {
                        "text": "Akut Jeneralize Ürtiker ve Anjiyoödem",
                        "is_correct": False,
                        "scenario_update": "İzole ürtiker ve anjiyoödemde laringeal stridor, bronkospazm, hipotansiyon veya şiddetli gastrointestinal sistem tutulumu bulunmaz.",
                        "teaching_point": "Cilt ve mukoza bulgularına solunum, dolaşım veya şiddetli gastrointestinal semptomlardan en az birinin eşlik etmesi tabloyu izole ürtikerden çıkarıp anafilaksiye taşır."
                    },
                    {
                        "text": "Herediter Anjiyoödem Akut Laringeal Atağı",
                        "is_correct": False,
                        "scenario_update": "Herediter anjiyoödem bradikinin aracılıdır; kaşıntılı ürtiker plakları eşlik etmez ve adrenalin tedavisine yanıt vermez.",
                        "teaching_point": "Herediter anjiyoödemde C1 esteraz inhibitör eksikliğine bağlı ürtikersiz, kaşıntısız ödem görülür; bu hastada yaygın kaşıntılı ürtiker ve adrenaline hızlı yanıt mevcuttur."
                    },
                    {
                        "text": "Besin Proteini İlişkili Enterokolit Sendromu",
                        "is_correct": False,
                        "scenario_update": "Besin proteini ilişkili enterokolit sendromu (FPIES) IgE aracılı değildir; alımdan 1-4 saat sonra gecikmiş inatçı kusma ile seyreder, ürtiker ve stridor yapmaz.",
                        "teaching_point": "Dakikalar içinde gelişen ürtiker, anjiyoödem ve laringeal ödem IgE aracılı Tip 1 aşırı duyarlılık reaksiyonunu (anafilaksi) gösterir."
                    }
                ]
            },
            {
                "stage_title": "Sarı Alan Gözlem Süresi ve Taburculuk Planı",
                "question": "İlk doz intramusküler adrenalin sonrası klinik bulguları tamamen düzelen 25 kg ağırlığındaki bu hastanın izlem ve taburculuk yönetimi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Semptomları tamamen gerilediği için 1 saatlik gözlem sonunda oral antihistaminik reçete ederek taburcu etmek ve 1 hafta sonra alerji polikliniğine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Erken taburcu edilen çocukta ilk ataktan 5 saat sonra evde tekrar alerjen teması olmaksızın şiddetli stridor ve hipotansiyonla seyreden bifazik reaksiyon gelişti.",
                        "teaching_point": "Anafilaksi olgularının %5-20 kadarında ilk semptomlar düzeldikten saatler sonra bifazik reaksiyon gelişebildiğinden hastalar en az 6-8 saat gözlem altında tutulmalıdır."
                    },
                    {
                        "text": "Hastayı 2 saat gözlemde tuttuktan sonra yalnızca oral metilprednizolon ve desloratadin şurup reçete ederek, adrenalin otoenjektörü yazmadan aileye diyet listesiyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Adrenalin otoenjektörü reçete edilmeyen hasta birkaç hafta sonra okulda gelişen kazara maruziyette ilk müdahale yapılamadığı için ağır solunum yetmezliği ile acile getirildi.",
                        "teaching_point": "Besin anafilaksisi geçiren her çocuğa taburculukta mutlaka ağırlığına uygun adrenalin otoenjektörü reçete edilmeli ve aileye yazılı acil eylem planı verilmelidir."
                    },
                    {
                        "text": "Bifazik reaksiyonu kesin olarak engellemek amacıyla 6 saatlik gözlem süresince her 2 saatte bir profilaktik düşük doz intramusküler adrenalin enjeksiyonu tekrarlamak",
                        "is_correct": False,
                        "scenario_update": "Semptomu kalmayan hastaya yapılan tekrarlayan gereksiz adrenalin enjeksiyonları şiddetli taşikardi, hipertansiyon, tremor ve anksiyeteye yol açtı.",
                        "teaching_point": "Adrenalin yalnızca aktif semptom varlığında (ilk doza 5-15 dakikada yanıt alınamazsa veya semptomlar nüksederse) tekrarlanır; asemptomatik hastaya profilaktik tekrar doz yapılmaz."
                    },
                    {
                        "text": "Bifazik reaksiyon riski açısından en az 6-8 saat monitörize gözlemde tutmak, taburculukta adrenalin otoenjektörü reçete ederek aileye uygulamalı eğitim vermek",
                        "is_correct": True,
                        "explanation": "Solunum tutulumu olan anafilaksi hastaları bifazik reaksiyon açısından en az 6-8 saat izlenmeli, taburculukta adrenalin otoenjektörü reçete edilerek çocuk alerji bölümüne yönlendirilmelidir.",
                        "new_finding": "Hasta Sarı Alanda 8 saat boyunca monitörize izlendi ve bifazik reaksiyon gelişmedi. Aileye adrenalin otoenjektörü kullanımı maket üzerinde uygulamalı olarak öğretildi, yazılı eylem planı ve Çocuk Alerji randevusu verilerek güvenle taburcu edildi."
                    }
                ]
            }
        ]
    },
    {
        "id": "S17",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "13 Yaş",
        "gender": "Erkek",
        "complaint": "Gece uykudan uyandıran sol kasık ve skrotumda ani başlayan şiddetli ağrı, şişlik, kızarıklık ve iki kez kusma",
        "history": "13 yaşındaki erkek hasta babası tarafından sabah 06:00'da Sarı Alana getiriliyor: 'Gece saat 03:00 civarında sol kasığımda ve torbamda bıçak saplanır gibi çok şiddetli bir ağrıyla uyandım. Ağrının şiddetinden iki kez kustum. Sol tarafım şişti ve kızardı, yürürken bacağımı hareket ettiremiyorum. Ateşim, üşümem veya idrar yaparken yanmam olmadı.'",
        "final_diagnosis": "Akut Sol Testis Torsiyonu (Spermatik Kord Torsiyonu ve Akut Testiküler İskemi)",
        "disposition": "Sarı Alanda Acil Renkli Doppler USG + Eş Zamanlı Çocuk Cerrahisi / Üroloji Konsültasyonu ile Altın 6 Saat İçinde Acil Cerrahi Detorsiyon ve Bilateral Orşiopeksi",
        "case_pearl": "Akut skrotal ağrı ve kusma ile başvuran her çocuk ve adölesanda aksi kanıtlanana kadar testis torsiyonu düşünülmelidir. Fizik muayenede en duyarlı bulgu ipsilateral kremasterik refleks kaybıdır; testisin skrotumda yüksek ve transvers (yatay) yerleşimi ile skrotal elevasyonla ağrının azalmaması (negatif Prehn bulgusu) tanıyı destekler. Organın kurtarılabilmesi için altın pencere ilk 6 saattir (>%90 kurtarılma oranı). Renkli Doppler USG'de parankimal kan akımının izlenmemesi ve spermatik kordda girdap (whirlpool) görünümü tipiktir. Zemininde sıklıkla bilateral çan tokmağı (bell-clapper) deformitesi bulunduğundan cerrahi eksplorasyonda detorsiyon sonrası mutlaka her iki testise bilateral orşiopeksi yapılmalıdır.",
        "steps": [
            {
                "stage_title": "Sarı Alanda Akut Skrotal ve Genital Muayene",
                "question": "Gece uykudan uyandıran ani sol skrotal ağrı ve kusma ile başvuran 13 yaşındaki erkek hastada ilk fizik muayene yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Her iki gonadı pozisyon, aks ve hassasiyet açısından muayene etmek, kremasterik refleksi ve skrotal elevasyon yanıtını değerlendirmek",
                        "is_correct": True,
                        "explanation": "Akut skrotal ağrıda gonadın yerleşim aksı, elevasyonla ağrının değişimi ve kremasterik refleks varlığı vasküler acilleri inflamatuar süreçlerden ayırt etmede en değerli muayene bulgularıdır.",
                        "new_finding": "Vital Bulgular: TA 124/78 mmHg, KTA 110/dk, Ateş 36.7°C. Fizik Muayene: Sol hemiskrotum hiperemik ve ödemli; sol gonad skrotum üst polünde yüksek ve transvers yerleşimli, palpasyonla ileri derecede hassas. Skrotal elevasyonla ağrıda azalma olmadı. Sol kremasterik refleks alınamadı. Sağ gonad ve sağ kremasterik refleks doğal, batın muayenesi rahat."
                    },
                    {
                        "text": "Şiddetli ağrı nedeniyle genital palpasyonu erteleyip öncelikle İV metamizol sodyum ve skrotuma sıcak kompres uygulayarak 1 saat sonra muayene etmek",
                        "is_correct": False,
                        "scenario_update": "Muayene edilmeden uygulanan sıcak kompres ve bekleme süresi, dokunun metabolik oksijen tüketimini artırarak geri dönüşsüz parankimal iskemi süresini kısaltmış oldu.",
                        "teaching_point": "Akut skrotal ağrıda fizik muayene asla ertelenmemeli ve vasküler perfüzyon bozukluğu dışlanmadan lokal sıcak uygulama kesinlikle yapılmamalıdır."
                    },
                    {
                        "text": "İdrar yolu enfeksiyonu ve epididimit ön tanısıyla skrotal refleks bakmadan orta akım idrar örneği alıp ampirik İV seftriakson tedavisi başlamak",
                        "is_correct": False,
                        "scenario_update": "İdrar tetkiki beklenen ve antibiyotik başlanan hastada geçen saatler içinde sol skrotumdaki ödem arttı ve ağrı narkotik analjeziklere bile yanıtsız hale geldi.",
                        "teaching_point": "Dizüri ve ateşi olmayan akut başlangıçlı skrotal ağrıda genital muayene ve vasküler değerlendirme yapılmadan enfeksiyon tedavisiyle vakit kaybedilmemelidir."
                    },
                    {
                        "text": "Yansıyan renal kolik ve üreter taşını dışlamak amacıyla skrotal muayene öncesinde hastaya hızlıca intravenöz hidrasyon başlayıp kontrastsız tüm batın tomografisi çekmek",
                        "is_correct": False,
                        "scenario_update": "Tomografi çekimi ve raporlanması için geçen sürede renal taş saptanmadı ancak skrotal patolojiye yönelik kritik müdahale penceresi daraldı.",
                        "teaching_point": "Skrotuma vuran ağrıda öncelik her zaman dikkatli bir genital muayenedir; muayene yapılmadan radyasyon içeren batın görüntülemelerine yönelinmemelidir."
                    }
                ]
            },
            {
                "stage_title": "Radyolojik Görüntüleme ve Zamanlama Stratejisi",
                "question": "Kremasterik refleks kaybı, sol gonadda yüksek-transvers yerleşim ve elevasyonla ağrının azalmaması saptanan 3. saatindeki hastada bir sonraki adımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Öncelikle tam kan sayımı, CRP, sedimantasyon ve idrar kültürü sonuçlarını beklemek, inflamatuar belirteçler normal gelirse radyolojik görüntüleme ve konsültasyon istemek",
                        "is_correct": False,
                        "scenario_update": "Laboratuvar sonuçlarının çıkması için geçen 90 dakika sonunda lökosit ve CRP hafif yüksek saptandı, bu sırada iskemi süresi 4.5 saati aştı.",
                        "teaching_point": "Akut vasküler skrotal patolojilerde akut faz reaktanları normal veya hafif yüksek olabilir; laboratuvar beklemek organ kaybına yol açan tehlikeli bir gecikmedir."
                    },
                    {
                        "text": "Semptomların başlangıcından itibaren henüz 3 saat geçtiği için sabah mesai saatinde elektif skrotal manyetik rezonans görüntüleme planlayarak hastayı gözlemde tutmak",
                        "is_correct": False,
                        "scenario_update": "Sabah mesai saatine kadar bekletilen hastada toplam iskemi süresi 8 saati geçti ve sol parankimde kalıcı koagülasyon nekrozu gelişti.",
                        "teaching_point": "Akut skrotal perfüzyon bozukluğunda organın kurtarılabilmesi için altın pencere ilk 6 saattir; elektif görüntüleme için asla beklenemez."
                    },
                    {
                        "text": "Radyolojik görüntüleme veya cerrahi konsültasyon istemeden önce acil serviste sedasyon altında dışarıdan zorlu manuel rotasyon manevrasını defalarca tekrarlayarak uygulamaya çalışmak",
                        "is_correct": False,
                        "scenario_update": "Körlemesine yapılan zorlu manuel manevra korddaki dolanmayı daha da sıkılaştırarak ağrıyı şiddetlendirdi ve cerrahi ekip çağrılmadığı için zaman kaybedildi.",
                        "teaching_point": "Manuel müdahale asla acil cerrahi konsültasyonun ve ameliyathane hazırlığının yerini tutmaz; kontrolsüz manevralar rotasyon derecesini artırabilir."
                    },
                    {
                        "text": "Oral alımı durdurup İV analjezi başlamak, derhal Çocuk Cerrahisi/Üroloji konsültasyonu isteyerek gecikmeden acil skrotal Renkli Doppler USG yaptırmak",
                        "is_correct": True,
                        "explanation": "Yüksek klinik şüphede hasta derhal ameliyata hazırlanmalı, cerrahi ekip eş zamanlı çağrılmalı ve ameliyatı geciktirmeyecek şekilde hızlıca Renkli Doppler USG ile kan akımı değerlendirilmelidir.",
                        "new_finding": "Tam İdrar Tetkiki: Lökosit ve eritrosit yok. Acil Skrotal Renkli Doppler USG: Sol gonad boyutları sağa göre artmış, parankim ekojenitesi heterojen görünümde; sol parankimde arteriyel ve venöz kan akımının tamamen izlenmemesi ve kord yapılarında girdap görünümü saptandı. Sağ gonadda kanlanmanın doğal olduğu raporlandı."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Kremasterik refleks kaybı, yüksek-transvers gonad yerleşimi ve Renkli Doppler USG bulguları ışığında bu hastanın kesin tanısı nedir?",
                "options": [
                    {
                        "text": "Akut Bakteriyel Epididimo-Orşit",
                        "is_correct": False,
                        "scenario_update": "Akut epididimo-orşitte kremasterik refleks genellikle korunmuştur ve Renkli Doppler USG incelemesinde parankim ve epididimde kan akımı belirgin artmıştır.",
                        "teaching_point": "Epididimo-orşitte inflamasyona bağlı hipervaskülarite görülürken, bu hastada arteriyel ve venöz kan akımı tamamen kesilmiştir."
                    },
                    {
                        "text": "Akut Sol Testis Torsiyonu",
                        "is_correct": True,
                        "explanation": "Ani başlayan skrotal ağrı, kusma, ipsilateral kremasterik refleks kaybı, yüksek-transvers yerleşim ve Doppler USG'de kan akımının izlenmemesi ile kordda girdap görünümü akut testis torsiyonunu kesinleştirir.",
                        "new_finding": "Kesin tanı: Akut Sol Testis Torsiyonu. Semptom süresi 3.5 saat olup altın 6 saatlik cerrahi pencere içindedir."
                    },
                    {
                        "text": "Testiküler Apendiks (Morgagni Hidatidi) Torsiyonu",
                        "is_correct": False,
                        "scenario_update": "Apendiks testis torsiyonunda ağrı daha hafif seyreder, testis üst polünde mavi nokta (blue dot) bulgusu görülür ve testisin kendi parankim kanlanması normaldir.",
                        "teaching_point": "Morgagni hidatidi torsiyonunda Doppler USG'de testis parankim kan akımı korunmuştur; tam akım kaybı ve kordda girdap işareti spermatik kord torsiyonunu gösterir."
                    },
                    {
                        "text": "İnkarsere İnguinal Herni ve Reaktif Hidrosel",
                        "is_correct": False,
                        "scenario_update": "Hastanın inguinal kanalında uzanan barsak ansı saptanmamış olup Doppler USG'de spermatik kordda girdap görünümü ve testiküler avaskülarite mevcuttur.",
                        "teaching_point": "İnguinal hernide kasık kanalından skrotuma uzanan kitle ve barsak sesleri saptanır; bu vakada primer patoloji spermatik kord torsiyonudur."
                    }
                ]
            },
            {
                "stage_title": "Acil Cerrahi Yönetim ve Operasyon İlkeleri",
                "question": "Semptomların 3.5 saatinde akut sol testis torsiyonu tanısı kesinleşen bu hastada uygulanması gereken doğru cerrahi yönetim hangisidir?",
                "options": [
                    {
                        "text": "İntravenöz fraksiyone olmayan heparin antikoagülasyonu ve vazodilatatör ilaç infüzyonu başlayarak 6 saat izlemek, kontrol görüntülemede akım dönmezse ameliyata almak",
                        "is_correct": False,
                        "scenario_update": "Mekanik olarak kendi etrafında dönmüş olan spermatik kord antikoagülan tedaviyle açılmadı ve 6 saatlik kritik süre aşılarak sol testis nekroze oldu.",
                        "teaching_point": "Testis torsiyonu mekanik bir rotasyon sonucu gelişir; trombolitik veya antikoagülan tedavinin yeri yoktur, tek tedavi acil cerrahi detorsiyondur."
                    },
                    {
                        "text": "Acil cerrahi eksplorasyona alarak sol spermatik kord detorsiyonu ve sol orşiopeksi yapmak, sağlam olan sağ testise ise hiçbir cerrahi işlem uygulamamak",
                        "is_correct": False,
                        "scenario_update": "Sol testis kurtarıldı ancak anatomik yatkınlığı devam eden karşı testise fiksasyon yapılmadığı için 8 ay sonra sağ testis torsiyonu gelişti.",
                        "teaching_point": "İntravajinal testis torsiyonunun temel nedeni olan çan tokmağı (bell-clapper) deformitesi olguların çoğunda bilateraldir; bu nedenle karşı testise de profilaktik orşiopeksi yapılması zorunludur."
                    },
                    {
                        "text": "Altın 6 saat dolmadan acil cerrahi eksplorasyona almak, sol detorsiyon ve reperfüzyon sonrası her iki testise bilateral orşiopeksi uygulamak",
                        "is_correct": True,
                        "explanation": "İlk 6 saat içinde yapılan acil cerrahi eksplorasyon ve detorsiyon ile testisin kurtarılma şansı %90'ın üzerindedir; karşı testisteki anatomik anomali riski nedeniyle bilateral orşiopeksi standart yaklaşımdır.",
                        "new_finding": "Hasta 4. saatinde acil ameliyathaneye alındı; 540 derece dönmüş olan sol spermatik kord detorsiyone edildi. Ilık serum fizyolojik uygulaması sonrası sol testis hızla pembeleşti ve kanlanması geri döndü. Her iki testise bilateral orşiopeksi uygulanarak organ kaybı olmadan taburcu edildi."
                    },
                    {
                        "text": "Doppler USG incelemesinde arteriyel kan akımı hiç izlenmediği için testisin nekroze olduğunu kabul ederek detorsiyon denemeden doğrudan sol orşiektomi yapmak",
                        "is_correct": False,
                        "scenario_update": "Henüz 3.5 saatlik iskemisi olan ve detorsiyonla kurtarılabilecek canlılıktaki sol testis, reperfüzyon yanıtı beklenmeden gereksiz yere çıkarılmış oldu.",
                        "teaching_point": "Doppler USG'de akım olmaması testisin öldüğünü değil torsiyone olduğunu gösterir; ameliyatta detorsiyon ve ılık kompres sonrası canlılık mutlaka değerlendirilmelidir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S18",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "3.5 Yaş",
        "gender": "Kız",
        "complaint": "Vücutta aniden ortaya çıkan çok sayıda toplu iğne başı büyüklüğünde kırmızı-mor döküntüler, bacaklarda morluklar ve diş eti kanaması",
        "history": "Annesi 3.5 yaşındaki kızını Sarı Alana getiriyor: 'Yaklaşık iki hafta önce hafif bir üst solunum yolu enfeksiyonu geçirmişti ve tamamen iyileşmişti. Dün akşam banyo yaptırırken cildinde hiçbir şey yoktu; bu sabah uyandığında bacaklarında, kollarında ve gövdesinde yüzlerce minik kırmızı nokta ve birkaç büyük morluk fark ettim. Sabah dişini fırçalarken diş etleri kanadı ve ağız içinde kanlı kabarcıklar gördüm. Ateşi yok, iştahı ve neşesi yerinde.'",
        "final_diagnosis": "Akut İmmün Trombositopenik Purpura (Primer Akut Pediatrik İTP - Mukozal Kanamalı)",
        "disposition": "Sarı Alanda Tam Kan Sayımı ve Periferik Yayma Doğrulaması + Aktif Mukozal Kanama (Islak Purpura) ve Derin Trombositopeni Nedeniyle IVIG (0.8-1 g/kg) Tedavisi ve Servis Yatışı",
        "case_pearl": "Pediatrik akut İTP, sıklıkla viral bir enfeksiyondan 1-4 hafta sonra genel durumu iyi olan çocukta aniden gelişen peteşi, ekimoz ve izole trombositopeni tablosudur. Tanıda altın kural: Fizik muayenede hepatosplenomegali veya patolojik lenfadenopati olmamalı, hemogramda diğer seriler (Hb, WBC) normal olmalı ve periferik yaymada blast veya şistosit bulunmadığı teyit edilmelidir. Ağız içi hemorajik büller ve diş eti kanaması ('ıslak purpura') ile PLT <10.000-20.000/mm³ varlığında intrakraniyal kanama riskini önlemek için IVIG (0.8-1 g/kg tek doz) veya kortikosteroid başlanır. Hayatı tehdit eden masif kanama olmadıkça trombosit transfüzyonu, İM enjeksiyon ve NSAİİ/aspirin kontrendikedir.",
        "steps": [
            {
                "stage_title": "Sarı Alanda Fizik Muayene ve Kanama Değerlendirmesi",
                "question": "Yaygın peteşi, ekimoz ve diş eti kanaması ile başvuran ancak genel durumu iyi olan 3.5 yaşındaki çocukta ilk muayene ve yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Koagülopati olasılığına karşı kan tetkiki öncesinde uyluk kasından intramusküler 5 mg K vitamini uygulamak ve diş eti ağrısı için oral ibuprofen vermek",
                        "is_correct": False,
                        "scenario_update": "İntramusküler enjeksiyon yapılan uyluk bölgesinde kısa sürede derin doku içi hematom gelişti ve verilen ibuprofen sonrası diş eti kanaması şiddetlendi.",
                        "teaching_point": "Kanama diyatezi veya peteşiyal döküntüsü olan hastalarda kas içi enjeksiyonlar derin hematom riski nedeniyle, NSAİİ grubu ilaçlar ise agregasyon bozukluğu nedeniyle kontrendikedir."
                    },
                    {
                        "text": "Vital bulguları ve nörolojik durumu değerlendirmek, ağız mukozasında hemorajik bülleri, lenfadenopati ve hepatosplenomegali varlığını kontrol ederek travmadan korumak",
                        "is_correct": True,
                        "explanation": "Peteşi ve ekimozla başvuran çocukta mukozal kanama varlığı intrakraniyal kanama riskini belirlerken, organomegali ve lenfadenopati kontrolü malign infiltratif süreçleri dışlamak için kritiktir.",
                        "new_finding": "Vital Bulgular: Ateş 36.6°C, KTA 96/dk, SS 20/dk, TA 94/58 mmHg. Genel durumu iyi, bilinci açık, aktif. Ciltte yaygın basmakla solmayan peteşiler ve alt ekstremitelerde 2-3 cm çapında ekimozlar mevcut. Bukkal mukozada iki adet hemorajik bül ve diş eti kenarında sızıntı tarzında kanama izlendi. Servikal/aksiller patolojik lenfadenopati yok, karaciğer ve dalak kot altında ele gelmiyor, nörolojik muayene doğal."
                    },
                    {
                        "text": "Basmakla solmayan döküntüleri invaziv bakteriyel enfeksiyon kabul ederek fizik muayeneyi tamamlamadan lomber ponksiyon yapmak ve yüksek doz seftriakson başlamak",
                        "is_correct": False,
                        "scenario_update": "Hemodinamik olarak stabil ve ateşsiz olan hastada trombosit düzeyi görülmeden yapılan lomber ponksiyon spinal epidural hematom riskini ciddi ölçüde artırdı.",
                        "teaching_point": "Ateşi olmayan ve genel durumu iyi olan peteşili çocukta öncelikle kanama diyatezi değerlendirilmelidir; hemostaz teyit edilmeden lomber ponksiyon yapılması spinal hematom açısından kontrendikedir."
                    },
                    {
                        "text": "Ağız içi hemorajik bülleri lokal travmaya bağlayıp kanama odaklarını povidon iyotlu gazlı bezle sertçe kazıyarak temizlemek ve gargara önermek",
                        "is_correct": False,
                        "scenario_update": "Mukozal hemorajik büllerin mekanik olarak kazınması durdurulamayan yaygın mukozal sızıntı kanamasına ve çocuğun kanı yutarak kusmasına yol açtı.",
                        "teaching_point": "Ağız mukozasındaki hemorajik büller ciddi mukozal kanama göstergesidir; kesinlikle mekanik olarak patlatılmamalı veya travmatize edilmemelidir."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar Tetkikleri ve Morfolojik İnceleme",
                "question": "Organomegalisi olmayan ancak yaygın peteşi ve oral mukozal hemorajik bülleri saptanan bu çocukta doğrulama için hangi tetkikleri istemelisiniz?",
                "options": [
                    {
                        "text": "Tam kan sayımı, retikülosit, koagülasyon parametreleri (PT, aPTT) ve mutlaka periferik kan yayması isteyerek diğer hücre serilerini ve morfolojiyi değerlendirmek",
                        "is_correct": True,
                        "explanation": "Edinsel izole kanama diyatezlerinde hemogramda hemoglobin ve lökosit serisinin normal olduğunun görülmesi ve periferik yaymada atipik hücre, blast veya şistosit bulunmadığının doğrulanması şarttır.",
                        "new_finding": "Laboratuvar: WBC 7.600/mm³, Hb 12.6 g/dL, MCV 79 fL, PLT 6.000/mm³, Retikülosit %1.1, PT 12.1 sn, aPTT 28 sn, Fibrinojen 260 mg/dL. Periferik Yayma: Eritrosit normokrom normositer, şistosit veya fragmente eritrosit yok; lökosit dağılımı normal, blast veya atipik hücre izlenmedi; trombositler her alanda tekli ve nadir, yer yer iri trombositler görüldü."
                    },
                    {
                        "text": "Periferik kan yayması değerlendirmesi yapmadan doğrudan acil ameliyathane koşullarında genel sedasyon altında kemik iliği aspirasyonu ve trepan biyopsisi işlemi planlamak",
                        "is_correct": False,
                        "scenario_update": "Tipik öyküsü ve normal fizik muayenesi olan küçük çocukta periferik yayma görülmeden yapılan invaziv kemik iliği girişimi işlem yerinde ciddi kanamaya neden oldu.",
                        "teaching_point": "ASH ve uluslararası pediatrik hematoloji kılavuzlarına göre, fizik muayenesi ve periferik yayması tipik olan çocuklarda tanı için rutin kemik iliği aspirasyonu önerilmez."
                    },
                    {
                        "text": "Yalnızca cilt kanama zamanı, sedimantasyon ve CRP testleri isteyerek periferik yayma bakmadan hastaya acil taze donmuş plazma infüzyonu uygulamaya başlamak",
                        "is_correct": False,
                        "scenario_update": "Koagülasyon faktör eksikliği olmayan hastaya verilen taze donmuş plazma kanamayı durdurmadı ve periferik yayma bakılmadığı için ayırıcı tanı eksik kaldı.",
                        "teaching_point": "Peteşiyal ve mukozal kanamalarda birincil hemostaz bozukluğu ön plandadır; tanı için tam kan sayımı ve periferik yayma incelemesi zorunludur."
                    },
                    {
                        "text": "Henüz hiçbir kan örneği almadan önce olası iç kanamaları taramak amacıyla sedasyon vererek kontrastlı beyin tomografisi ve batın ultrasonografisi çektirmek",
                        "is_correct": False,
                        "scenario_update": "Nörolojik muayenesi tamamen normal olan çocukta laboratuvar tetkiki yapılmadan radyoloji ünitesinde vakit kaybedildi ve sedasyon işlemi ek risk oluşturdu.",
                        "teaching_point": "Nörolojik semptom veya bulgusu olmayan hastalarda rutin kraniyal görüntüleme endike değildir; öncelik hızlıca tam kan sayımı ve periferik yayma değerlendirmesidir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Viral enfeksiyon sonrası gelişen peteşi, oral mukozal hemorajik büller, PLT 6.000/mm³ ve normal periferik yayma bulgularıyla kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Pediatrik Akut Lenfoblastik Lösemi (ALL)",
                        "is_correct": False,
                        "scenario_update": "Akut lösemide genellikle anemi/nötropeni gibi diğer serilerin tutulumu, hepatosplenomegali, lenfadenopati ve periferik yaymada blast hücreleri görülür.",
                        "teaching_point": "Bu hastada organomegali yoktur, hemoglobin ve lökosit değerleri normaldir ve periferik yaymada blast izlenmemiştir."
                    },
                    {
                        "text": "Edinsel Trombotik Trombositopenik Purpura (TTP)",
                        "is_correct": False,
                        "scenario_update": "Trombotik mikroanjiyopatilerde hemolitik anemi, retikülositoz ve periferik yaymada parçalanmış eritrositler (şistositler) bulunur.",
                        "teaching_point": "Hastanın hemoglobini normal olup periferik yaymasında şistosit ve mikroanjiyopatik hemoliz bulgusu yoktur."
                    },
                    {
                        "text": "Akut İmmün Trombositopenik Purpura (İTP)",
                        "is_correct": True,
                        "explanation": "Viral enfeksiyon sonrası sağlıklı görünümde çocukta gelişen izole derin trombositopeni, normal eritrosit/lökosit serisi ve iri trombositler içeren normal periferik yayma akut primer İTP için tanısaldır.",
                        "new_finding": "Kesin tanı: Akut İmmün Trombositopenik Purpura (Primer Akut İTP). Ağız içi ıslak purpura ve diş eti kanaması mevcut."
                    },
                    {
                        "text": "Kalıtsal Von Willebrand Hastalığı Tip 1",
                        "is_correct": False,
                        "scenario_update": "Von Willebrand hastalığı Tip 1'de trombosit sayısı tamamen normaldir; trombosit fonksiyon bozukluğuna bağlı mukozal kanama görülür.",
                        "teaching_point": "PLT 6.000/mm³ düzeyinde derin trombositopeni Von Willebrand Tip 1 ile açıklanamaz; tablo edinsel immün yıkıma bağlı akut İTP'dir."
                    }
                ]
            },
            {
                "stage_title": "Sarı Alanda Tedavi Seçimi ve Kanama Yönetimi",
                "question": "Trombosit sayısı 6.000/mm³ olan ve ağız mukozasında aktif hemorajik bülleri (ıslak purpura) bulunan 3.5 yaşındaki İTP hastasında en uygun tedavi yaklaşımı hangisidir?",
                "options": [
                    {
                        "text": "Trombosit sayısını hızla normale getirmek amacıyla acilen 2 ünite aferez trombosit süspansiyonu transfüze etmek ve 4 saat sonra taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Transfüze edilen trombositler dolaşımdaki anti-trombosit otoantikorlar tarafından kısa sürede yıkıma uğradı, kontrol trombosit sayısı 8.000/mm³ kaldı ve mukozal kanama sürdü.",
                        "teaching_point": "İTP patofizyolojisinde otoantikor aracılı periferik yıkım olduğundan, yaşamı tehdit eden masif kanama olmadıkça tek başına trombosit transfüzyonu etkisizdir ve önerilmez."
                    },
                    {
                        "text": "Aktif mukozal kanama ve derin trombositopeni nedeniyle 0.8-1 g/kg tek doz IVIG infüzyonu (veya prednizolon) başlayarak hastayı servise yatırmak",
                        "is_correct": True,
                        "explanation": "Ağız içi ıslak purpura ve diş eti kanaması varlığında intrakraniyal ve majör kanama riskini azaltmak için trombosit sayısını en hızlı yükselten IVIG (0.8-1 g/kg) veya kortikosteroid tedavisiyle yatış endikedir.",
                        "new_finding": "Hastaya 0.8 g/kg dozunda IVIG infüzyonu uygulandı ve travma önlemleri alınarak pediatri servisine yatırıldı. 24. saatte yapılan kontrol hemogramda trombosit sayısı 52.000/mm³ düzeyine yükseldi, mukozal kanama tamamen durdu."
                    },
                    {
                        "text": "Genel durumu iyi olduğu için aktif mukozal kanamaya rağmen hiçbir ilaç vermeden 3 ay sonra kontrole gelmek üzere eve göndermek",
                        "is_correct": False,
                        "scenario_update": "Tedavisiz eve gönderilen çocukta gece şiddetli epistaksis ve gastrointestinal sistem kanaması gelişerek acil servise hipovolemik tabloda tekrar başvuru gerçekleşti.",
                        "teaching_point": "Sadece cilt bulgusu (kuru purpura) olan hafif olgularda yakın izlem seçilebilir; ancak ıslak purpura (aktif mukozal kanama) ve PLT <10.000/mm³ varlığında farmakolojik tedavi ve yatış gerekir."
                    },
                    {
                        "text": "Birinci basamak acil tedavi olarak hastayı çocuk cerrahisine danışıp acil splenektomi ameliyatına hazırlamak ve profilaktik intravenöz antibiyotik tedavisi başlamak",
                        "is_correct": False,
                        "scenario_update": "Akut yeni tanı pediatrik olguda medikal tedavi denenmeden cerrahi planlanması hematoloji konsültasyonu ile durdurularak gereksiz organ kaybı önlendi.",
                        "teaching_point": "Çocukluk çağı akut İTP olgularının %80-85 kadarı 6-12 ay içinde kendiliğinden tam remisyona girer; splenektomi yalnızca 12 aydan uzun süren dirençli kronik olgularda son basamakta düşünülür."
                    }
                ]
            }
        ]
    },
    {
        "id": "S19",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "2 Yaş",
        "gender": "Erkek",
        "complaint": "Büyükannesinin komodinin üzerindeki antihipertansif ilaç kutusundaki tabletlerden yutma; 2 saat sonra başlayan halsizlik, uyuklama, baş dönmesi ve soğuk terleme",
        "history": "Ailesi 2 yaşındaki (12 kg) erkek çocuğu Sarı Alana getiriyor: 'Yaklaşık 1.5 saat önce büyükannesinin komodinin üzerindeki antihipertansif ilaç kutusunu açmış. Yerde üzerinde isim yazmayan yırtılmış boş blister folyolar bulduk, 10 mg'lık yuvarlak beyaz tabletlerden en az 5-6 tanesini çiğneyip yuttuğunu düşünüyoruz. İlk saatte hareketliydi ancak son yarım saattir rengi soldu, soğuk terliyor, ayakta duramıyor ve uykuya meyilli hale geldi.'",
        "final_diagnosis": "Kalsiyum Kanal Blokeri (Amlodipin) İntoksikasyonu (Vazoplejik Şok, Metabolik Laktik Asidoz ve Hiperglisemi)",
        "disposition": "Sarı Alanda Aktif Kömür + Kristaloid Bolusu + İV %10 Kalsiyum Glukonat + Yüksek Doz İnsülin-Öglisemi Tedavisi (HIET) ve Norepinefrin İnfüzyonu ile Çocuk Yoğun Bakım Ünitesine Yatış",
        "case_pearl": "Kalsiyum Kanal Blokerleri (KKB - özellikle amlodipin, verapamil, diltiazem) küçük çocuklarda tek bir tabletle bile ölümcül olabilen ('One Pill Can Kill') kardiyovasküler toksinlerdir. Diğer antihipertansiflerden (beta-bloker, klonidin, ACEİ) en önemli ayırıcı özelliği: Pankreas beta hücrelerindeki L-tipi kalsiyum kanallarını bloke ederek insülin salınımını baskılaması ve HİPERGLİSEMİ + LAKTİK ASİDOZ + DİRENÇLİ HİPOTANSİYON yapmasıdır (beta-blokerler hipoglisemi ve bradikardi, klonidin ise miyozis ve solunum depresyonu yapar). Dihidropiridin grubu (amlodipin) erken dönemde refleks sinüs taşikardisi ile derin vazopleji yapar. Tedavide aktif kömür, izotonik sıvı, İV kalsiyum glukonat, norepinefrin ve en kritik metabolik antidot olarak Yüksek Doz İnsülin-Öglisemi Tedavisi (HIET: 1 Ü/kg bolus + 0.5-1 Ü/kg/saat infüzyon ve dekstroz desteği) uygulanır.",
        "steps": [
            {
                "stage_title": "Sarı Alanda Toksikolojik Değerlendirme ve Monitörizasyon",
                "question": "Ne olduğu bilinmeyen antihipertansif tabletlerden çoklu miktarda yutma sonrası perfüzyon bozukluğu ve letarji ile başvuran 2 yaşındaki çocukta ilk değerlendirme yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Midedeki tabletleri hızla uzaklaştırmak amacıyla çocuğa acil serviste hipertonik tuzlu su içirerek veya farenksi uyararak zorla kusturma işlemi uygulamak",
                        "is_correct": False,
                        "scenario_update": "Uykuya meyilli olan çocukta zorla kusturma girişimi sırasında öğürme refleksi yetersiz kaldığı için mide içeriği akciğerlere aspire edildi ve hipoksi gelişti.",
                        "teaching_point": "Akut zehirlenmelerde mekanik uyarıyla veya tuzlu su/ipeka ile kusturma girişimi aspirasyon pnömonisi ve hipernatremi riski nedeniyle kesinlikle kontrendikedir."
                    },
                    {
                        "text": "Kan basıncı ölçümü ve kan şekeri kontrolü yapmadan önce toksik ilacın böbreklerden atılımını hızlandırmak için intravenöz furosemid uygulayarak diürezi zorlamak",
                        "is_correct": False,
                        "scenario_update": "Zaten periferik vazodilatasyon ve hipotansiyonu olan hastada uygulanan loop diüretik intravasküler hacmi daha da azaltarak derin kardiyovasküler kollapsa yol açtı.",
                        "teaching_point": "Antihipertansif ilaç zehirlenmelerinde zorlu diürezin yeri yoktur; diüretik verilmesi hipovolemiyi ve şok tablosunu ağırlaştırır."
                    },
                    {
                        "text": "Pupil çaplarına bakarak opioid/alfa-2 agonist zehirlenmesi varsaymak ve vital bulguları görmeden doğrudan intravenöz yüksek doz nalokson bolusu puşe etmek",
                        "is_correct": False,
                        "scenario_update": "Pupilleri izokorik olan ve solunum depresyonu bulunmayan hastada ampirik nalokson uygulamasına rağmen hipotansiyon ve perfüzyon bozukluğu hiç düzelmedi.",
                        "teaching_point": "Farklı antihipertansif sınıflarını ayırt etmek için öncelikle kan basıncı, kalp hızı, EKG, kapiller kan şekeri ve kan gazı parametreleri bütünsel değerlendirilmelidir."
                    },
                    {
                        "text": "Kardiyak monitörizasyon, 12 derivasyonlu EKG, kan basıncı, kapiller dolum zamanı, kan şekeri ve kan gazı/laktat ölçümünü hızla yapmak",
                        "is_correct": True,
                        "explanation": "Bilinmeyen antihipertansif zehirlenmelerinde hipotansiyon derecesi, kalp hızı/ritmi, laktik asidoz ve özellikle glukoz düzeyi etken ilaç grubunu ayırt etmede en önemli klinik ipuçlarıdır.",
                        "new_finding": "Vital Bulgular: TA 64/34 mmHg, KTA 142/dk, SS 28/dk, SpO2 %97, KDZ 4 saniye, ekstremiteler soğuk, pupiller izokorik ve miyozis yok. EKG: Sinüs taşikardisi, PR 130 ms, QRS 80 ms. Parmak ucu kan şekeri: 246 mg/dL. Venöz Kan Gazı: pH 7.24, HCO3 15 mmol/L, Baz Açığı -11, Laktat 4.8 mmol/L, K+ 3.9 mEq/L."
                    }
                ]
            },
            {
                "stage_title": "Gastrointestinal Dekontaminasyon ve İlk Resüsitasyon",
                "question": "Alımdan 1.5 saat sonra başvuran, derin hipotansiyonu (64/34 mmHg), metabolik laktik asidozu ve belirgin hiperglisemisi (246 mg/dL) olan 12 kg çocukta ilk basamak müdahaleniz ne olmalıdır?",
                "options": [
                    {
                        "text": "Hava yolunu koruyarak 1 g/kg aktif kömür vermek, 20 mL/kg izotonik kristaloid bolusu ve İV %10 kalsiyum glukonat (0.6 mL/kg) uygulamak",
                        "is_correct": True,
                        "explanation": "Erken dönemde aktif kömür gastrointestinal emilimi azaltır; izotonik sıvı bolusu damar içi hacmi desteklerken intravenöz kalsiyum tuzu miyokardiyal kontraktiliteyi ve vasküler tonusu artırır.",
                        "new_finding": "12 gram aktif kömür uygulandı, 20 mL/kg %0.9 NaCl bolusu ve 0.6 mL/kg %10 kalsiyum glukonat yavaş intravenöz infüzyonla verildi. Müdahale sonrası kan basıncı 72/40 mmHg, KTA 136/dk, kan şekeri 258 mg/dL, kontrol laktat 4.5 mmol/L ölçüldü; hipoperfüzyon bulguları devam ediyor."
                    },
                    {
                        "text": "Kan şekeri 246 mg/dL olduğu için diyabetik ketoasidoz protokolü başlatarak sadece 0.05 Ü/kg/saat düşük doz insülin ve hipotonik sıvı infüzyonu vermek",
                        "is_correct": False,
                        "scenario_update": "İdrarda ketonu negatif olan ve ilaç kaynaklı pankreatik insülin salınım baskılanması yaşayan hastada hipotonik sıvı uygulaması hipotansiyonu daha da derinleştirdi.",
                        "teaching_point": "Vazoplejik şoktaki zehirlenme hastasında hiperglisemi primer diyabete değil, pankreas beta hücrelerindeki iyon kanalı blokajına bağlıdır; hipotonik sıvı verilmemelidir."
                    },
                    {
                        "text": "Derin hipotansiyonu düzeltmek amacıyla kristaloid sıvı veya kalsiyum desteği vermeden doğrudan periferik damardan beta-agonist izoproterenol ve sodyum nitroprusid infüzyonu başlatmak",
                        "is_correct": False,
                        "scenario_update": "Periferik vazodilatatör etki mekanizmasına sahip bu ilaçların verilmesi sistemik vasküler direnci tamamen düşürerek kan basıncını ölçülemeyecek düzeye indirdi.",
                        "teaching_point": "Periferik vazodilatasyonun ön planda olduğu antihipertansif toksisitelerinde vazodilatatör ajanlar ve saf beta-2 agonistler hipotansiyonu ağırlaştırır."
                    },
                    {
                        "text": "Alımdan 1.5 saat geçtiği için çok geniş çaplı orogastrik tüp takarak 3 litre musluk suyu ile mide lavajı yapmak ve aktif kömür vermemek",
                        "is_correct": False,
                        "scenario_update": "Küçük çocukta musluk suyu ile yapılan yüksek hacimli gastrik lavaj hiponatremiye, hipotermiye ve mide mukozası travmasına yol açarken emilimi engellemedi.",
                        "teaching_point": "Çocuklarda rutin mide lavajı önerilmez ve musluk suyu su zehirlenmesine yol açar; uygun vakalarda 1 g/kg aktif kömür tercih edilmelidir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı ve Toksidrom Ayrımı",
                "question": "Antihipertansif alımı sonrası derin hipotansiyon, refleks taşikardi, metabolik laktik asidoz ve belirgin hiperglisemi (258 mg/dL) birlikteliği hangi ilaç grubu zehirlenmesini gösterir?",
                "options": [
                    {
                        "text": "Beta-Bloker (Propranolol) Akut İntoksikasyonu",
                        "is_correct": False,
                        "scenario_update": "Beta-bloker zehirlenmesinde belirgin bradikardi ve glukoneogenez/glikojenoliz baskılanmasına bağlı hipoglisemi görülür; bu hastada refleks taşikardi ve belirgin hiperglisemi mevcuttur.",
                        "teaching_point": "Antihipertansif zehirlenmesinde hiperglisemi kalsiyum kanal blokerlerini, hipoglisemi ise beta-blokerleri işaret eden en önemli metabolik ayırıcı bulgudur."
                    },
                    {
                        "text": "Santral Alfa-2 Agonist (Klonidin) İntoksikasyonu",
                        "is_correct": False,
                        "scenario_update": "Klonidin zehirlenmesinde opioid benzeri toksidrom (toplu iğne başı miyozis, bradikardi, apne/solunum depresyonu ve koma) görülür; belirgin hiperglisemi beklenmez.",
                        "teaching_point": "Hastada miyozis ve solunum depresyonu olmaması, aksine hiperglisemi ve laktik asidozla giden vazoplejik şok bulunması klonidin toksisitesini dışlar."
                    },
                    {
                        "text": "Kalsiyum Kanal Blokeri (Amlodipin) İntoksikasyonu",
                        "is_correct": True,
                        "explanation": "L-tipi kalsiyum kanallarının blokajı vasküler düz kasta gevşeme (derin hipotansiyon ve refleks taşikardi), doku hipoperfüzyonu (laktik asidoz) ve pankreas beta hücrelerinden insülin salınımının durmasıyla karakteristik hiperglisemiye yol açar.",
                        "new_finding": "Kesin tanı: Kalsiyum Kanal Blokeri (Amlodipin) İntoksikasyonu. Ailenin evden getirdiği ilaç kutusu da Amlodipin 10 mg olarak doğrulandı."
                    },
                    {
                        "text": "Anjiyotensin Dönüştürücü Enzim İnhibitörü İntoksikasyonu",
                        "is_correct": False,
                        "scenario_update": "ACE inhibitörü alımları çocuklarda genellikle hafif-orta hipotansiyon ve hiperkalemi ile seyreder; erken dönemde ağır laktik asidoz ve 258 mg/dL düzeyinde hiperglisemi yapmaz.",
                        "teaching_point": "Dirençli vazoplejik şok, laktik asidoz ve pankreatik insülin blokajına bağlı hiperglisemi triadı ACE inhibitörlerinden ziyade kalsiyum kanal blokeri toksisitesine özgüdür."
                    }
                ]
            },
            {
                "stage_title": "Spesifik Antidot (HIET) ve Yoğun Bakım Yönetimi",
                "question": "Sıvı ve İV kalsiyum glukonata rağmen hipotansiyonu (72/40 mmHg) ve laktik asidozu süren Kalsiyum Kanal Blokeri zehirlenmeli bu çocukta en etkili spesifik tedavi nedir?",
                "options": [
                    {
                        "text": "Yalnızca intravenöz glukagon (0.05 mg/kg) tek doz puşe uygulayıp Dekstroz veya insülin vermeden hastayı 6 saat sonra pediatri servisine çıkarmak",
                        "is_correct": False,
                        "scenario_update": "Tek doz glukagon uygulaması kusmayı tetikledi ve kalsiyum kanal blokajına bağlı vazoplejik şoku düzeltmekte yetersiz kalarak hipotansiyonun derinleşmesine yol açtı.",
                        "teaching_point": "Glukagon beta-bloker zehirlenmelerinde cAMP artışıyla yardımcı olabilir ancak ağır kalsiyum kanal blokeri şokunda tek başına yetersizdir; temel metabolik antidot yüksek doz insülindir."
                    },
                    {
                        "text": "Yüksek doz insülin-öglisemi protokolü (1 Ü/kg bolus, 0.5-1 Ü/kg/saat infüzyon + dekstroz) ve norepinefrin başlayarak Çocuk Yoğun Bakıma yatırmak",
                        "is_correct": True,
                        "explanation": "Kalsiyum kanal blokeri toksisitesinde yüksek doz insülin-öglisemi tedavisi (HIET) miyokardın karbonhidrat kullanımını sağlayarak güçlü inotropik etki gösterir; vazopleji için norepinefrin eklenerek yoğun bakımda izlenir.",
                        "new_finding": "Yüksek doz insülin (1 Ü/kg bolus ardından 1 Ü/kg/saat infüzyon), %10 Dekstroz ve norepinefrin infüzyonu başlatıldı. Saatlik glukoz ve potasyum takibiyle Çocuk Yoğun Bakım Ünitesine alınan hastanın 3. saatte kan basıncı 94/56 mmHg düzeyine ulaştı ve laktat 1.6 mmol/L değerine geriledi."
                    },
                    {
                        "text": "İdrar pH değerini 7.5-8.0 aralığında tutacak şekilde yüksek doz intravenöz sodyum bikarbonat alkalinizasyonu ve acil aralıklı hemodiyaliz işlemi başlatmak",
                        "is_correct": False,
                        "scenario_update": "Plazma proteinlerine yüksek oranda (%95 üzerinde) bağlanan ve dağılım hacmi geniş olan ilaç hemodiyalizle temizlenemedi ve hemodinamik instabilite sürdü.",
                        "teaching_point": "Amlodipin gibi kalsiyum kanal blokerleri proteine yüksek oranda bağlandığı ve geniş dağılım hacmine sahip olduğu için hemodiyaliz veya idrar alkalinizasyonu ile uzaklaştırılamaz."
                    },
                    {
                        "text": "Kalsiyum kanal blokajını geri döndürmek amacıyla intravenöz fizostigmin salisilat ve pridostigmin vererek kolinerjik uyarıyı artırmak ve genel serviste izlemek",
                        "is_correct": False,
                        "scenario_update": "Kolinerjik ajanların uygulanması miyokardiyal iletimi baskılayarak hastada ağır bradikardi, atriyoventriküler blok ve bronkore gelişmesine neden oldu.",
                        "teaching_point": "Antikolinesteraz ilaçların kalsiyum kanal blokeri zehirlenmesinde yeri yoktur; ağır bradikardi ve AV blok yaparak kardiyovasküler kollapsı hızlandırırlar."
                    }
                ]
            }
        ]
    },
    {
        "id": "S20",
        "category": "👁️ Göz Şikayetleri",
        "age": "4 Yaş",
        "gender": "Erkek",
        "complaint": "Sol göz kapaklarında kızarıklık, şiddetli şişlik, gözünü açamama, göz hareketleriyle artan ağrı ve yüksek ateş",
        "history": "Ailesi 4 yaşındaki erkek çocuğu Sarı Alana getiriyor: 'Dört gündür koyu kıvamlı burun akıntısı ve hafif ateşi vardı. Dün sabah sol gözünün iç köşesinde ve kapaklarında kızarıklık başladı; bu sabah ise göz kapakları tamamen şişti, morumsu-kırmızı bir renk aldı ve ateşi 39.2°C'ye yükseldi. Sağa sola bakmasını istediğimizde sol gözünü ettiremiyor ve gözünün arkasında çok şiddetli ağrı olduğunu söyleyerek ağlıyor.'",
        "final_diagnosis": "Akut Orbital Selülit ve Medial Subperiosteal Abse (Akut Etmoid Sinüzit Komplikasyonu)",
        "disposition": "Sarı Alanda Acil Kontrastlı Orbital ve Paranazal Sinüs BT + İV Geniş Spektrumlu Antibiyotik (Seftriakson + Vankomisin) + Oftalmoloji ve KBB Konsültasyonu ile Yatış",
        "case_pearl": "Göz kapağında kızarıklık ve şişlikle başvuran çocukta en kritik adım yüzeyel (preseptal) enfeksiyonu derin (orbital/postseptal) enfeksiyondan ayırt etmektir. Orbital selülit en sık akut etmoid sinüzitin ince lamina papyracea kemiğinden orbita içine yayılmasıyla gelişir. Klinik kırmızı bayraklar: 1) Ekstraoküler göz hareketlerinde kısıtlılık (oftalmopleji), 2) Göz hareketleriyle şiddetli ağrı, 3) Proptozis (globun öne yer değiştirmesi), 4) Kemozis (konjonktival ödem), 5) Görme azalması veya aferent pupil defektidir (RAPD). Bu bulgulardan biri bile varsa acil İV kontrastlı Orbital ve Paranazal BT çekilmeli, subperiosteal abse araştırılmalı, İV Seftriakson + Vankomisin (veya Ampisilin-Sulbaktam) başlanarak KBB ve Göz konsültasyonu ile yatırılmalıdır.",
        "steps": [
            {
                "stage_title": "Sarı Alanda Oftalmolojik Muayene ve Kırmızı Bayraklar",
                "question": "Akut rinosinüzit öyküsü sonrası tek taraflı göz kapağı ödemi, eritem ve yüksek ateşle başvuran 4 yaşındaki çocukta ilk fizik muayenede neleri değerlendirmelisiniz?",
                "options": [
                    {
                        "text": "Göz kapakları çok ödemli olduğu için kapakları hiç aralamadan dıştan inspeksiyonla yetinmek ve topikal tobramisin damla başlayıp 48 saat sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Göz küresi ve ekstraoküler hareketler değerlendirilmeden eve gönderilen hastada 12 saat içinde sol gözde aferent pupil defekti ve kalıcı görme kaybı gelişti.",
                        "teaching_point": "Ateşli periorbital ödem ve eritemle başvuran her çocukta göz kapakları nazikçe aralanarak göz küresi pozisyonu, göz hareketleri ve pupil refleksleri mutlaka değerlendirilmelidir."
                    },
                    {
                        "text": "Şişliği indirmek amacıyla sol göz üzerine sıcak nemli kompres uygulamak ve ağrısını kesmek için topikal tetrakain anestezik göz damlası damlatmak",
                        "is_correct": False,
                        "scenario_update": "Yüzeyel anestezik damla derin oküler ağrıyı geçirmediği gibi kornea epitel toksisitesine yol açtı ve sıcak uygulama derin dokulardaki ödemi artırdı.",
                        "teaching_point": "Derin orbita dokularını ilgilendiren akut bakteriyel enfeksiyon şüphesinde sıcak kompres ve topikal anestezik damlalar tanısal süreci geciktirir ve kontrendikedir."
                    },
                    {
                        "text": "Vital bulgularla birlikte görme keskinliğini, ekstraoküler göz hareketlerini, globun öne yer değiştirmesini, konjonktival ödemi ve aferent pupil defektini değerlendirmek",
                        "is_correct": True,
                        "explanation": "Göz kapağı enfeksiyonlarında derin orbita yapıların etkilenip etkilenmediğini belirleyen temel bulgular ekstraoküler hareket kısıtlılığı, ağrılı göz hareketleri, proptozis, kemozis ve pupil reaksiyonlarıdır.",
                        "new_finding": "Vital Bulgular: Ateş 39.2°C, KTA 132/dk, SS 24/dk, TA 100/62 mmHg. Oftalmolojik Muayene: Sol alt ve üst göz kapağında şiddetli eritem, ısı artışı ve ödem; sol gözde öne doğru yer değiştirme (proptozis), yukarı ve dışa bakışta ağrılı hareket kısıtlılığı, konjonktival ödem (kemozis) saptandı. Pupiller izokorik, direkt ve indirekt ışık refleksleri pozitif, rölatif aferent pupil defekti yok."
                    },
                    {
                        "text": "Böcek ısırığına bağlı lokal alerjik reaksiyon düşünerek göz muayenesini tamamlamadan intramusküler feniramin ve deksametazon uygulayıp hastayı 2 saat gözleme almak",
                        "is_correct": False,
                        "scenario_update": "Antihistaminik ve tek doz steroid uygulamasına rağmen hastanın yüksek ateşi, göz ağrısı ve göz hareket kısıtlılığı ilerlemeye devam etti.",
                        "teaching_point": "Yüksek ateş, pürülan rinit öyküsü ve tek taraflı ağrılı göz kapağı şişliğinde alerjik anjiyoödemden önce akut bakteriyel enfeksiyon ve derin doku yayılımı dışlanmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Radyolojik Görüntüleme ve Laboratuvar Planı",
                "question": "Sol gözde proptozis, yukarı ve dışa bakışta ağrılı hareket kısıtlılığı ve kemozis saptanan bu hastada en uygun tetkik yaklaşımı hangisidir?",
                "options": [
                    {
                        "text": "Yalnızca iki yönlü direkt Waters ve Caldwell paranazal sinüs grafisi çekmek, hemogram alarak radyasyon riski nedeniyle kesitsel görüntülemeden kaçınmak",
                        "is_correct": False,
                        "scenario_update": "Direkt sinüs grafisinde etmoid sinüslerde bulanıklık görülse de orbita içi yumuşak dokular ve kemik duvar komşuluğundaki koleksiyon değerlendirilemedi.",
                        "teaching_point": "Proptozis ve ekstraoküler hareket kısıtlılığı varlığında direkt grafiler orbita içi yayılımı ve abse formasyonunu göstermede tamamen yetersizdir."
                    },
                    {
                        "text": "Damar yolu açıp hemogram, CRP ve kan kültürü almak; acil intravenöz kontrastlı orbital ve paranazal sinüs BT çekmek",
                        "is_correct": True,
                        "explanation": "Proptozis, kemozis ve ağrılı göz hareket kısıtlılığı derin intraorbital tutulumu gösterir; koleksiyon veya abse varlığını saptamak için altın standart ilk görüntüleme kontrastlı orbital ve paranazal BT çekimidir.",
                        "new_finding": "Laboratuvar: WBC 19.200/mm³ (%85 nötrofil), CRP 112 mg/L, kan kültürü alındı. İV Kontrastlı Orbital ve Paranazal Sinüs BT: Sol etmoid ve maksiller sinüste tam opasifikasyon, lamina papyracea komşuluğunda orbita medial duvarında 12x5 mm boyutunda periferik kontrastlanan koleksiyon, sol medial rektus kasında ödem ve globda anterolateral yer değiştirme saptandı. Kavernöz sinüs yapıları doğal izlendi."
                    },
                    {
                        "text": "Radyolojik görüntüleme yapmadan önce olası intrakraniyal yayılımı dışlamak amacıyla acil serviste lomber ponksiyon yapmak ve konjonktival sürüntü kültürü sonucunu beklemek",
                        "is_correct": False,
                        "scenario_update": "Meninks irritasyon bulgusu olmayan hastada kesitsel görüntüleme öncesi lomber ponksiyon planlanması asıl anatomik odağın ve koleksiyonun saptanmasını geciktirdi.",
                        "teaching_point": "Fokal intraorbital bulguları olan hastada öncelikli tanı aracı kontrastlı orbital ve paranazal BT incelemesidir; konjonktival sürüntü kültürü derin doku etkenini yansıtmaz."
                    },
                    {
                        "text": "Herhangi bir radyolojik görüntüleme yapmadan doğrudan acil serviste lokal anestezi altında üst göz kapağı oluğundan enjektörle ponksiyon ve aspirasyon denemek",
                        "is_correct": False,
                        "scenario_update": "Körlemesine yapılan iğne aspirasyonu girişimi sırasında derin koleksiyona ulaşılamadığı gibi ekstraoküler kas ve glob perforasyonu tehlikesi yaşandı.",
                        "teaching_point": "Orbita içi koleksiyonlar anatomik olarak kemik duvar ile periorbita arasında derin yerleşimlidir; kesitsel görüntüleme olmadan acil serviste körlemesine iğne girişimi kesinlikle kontrendikedir."
                    }
                ]
            },
            {
                "stage_title": "Klinik ve Radyolojik Kesin Tanı",
                "question": "Proptozis, ağrılı oftalmopleji, kemozis ve BT incelemesinde sol orbita medial duvarında 12x5 mm koleksiyon saptanan hastanın kesin tanısı nedir?",
                "options": [
                    {
                        "text": "Komplike Olmayan Akut Preseptal (Periorbital) Selülit",
                        "is_correct": False,
                        "scenario_update": "Preseptal selülitte enfeksiyon septum orbitale önündeki cilt ve cilt altı dokuyla sınırlıdır; proptozis, ağrılı hareket kısıtlılığı ve intraorbital koleksiyon görülmez.",
                        "teaching_point": "Proptozis, kemozis ve ekstraoküler hareket kısıtlılığı varlığı preseptal selüliti dışlar ve postseptal (orbital) tutulumu kanıtlar."
                    },
                    {
                        "text": "Akut Bakteriyel Dakriyosistit ve Pürülan Konjonktivit",
                        "is_correct": False,
                        "scenario_update": "Dakriyosistit lakrimal kese bölgesinde lokalize şişlik yapar; globda öne itilme, ekstraoküler kas ödemi ve medial duvar koleksiyonu oluşturmaz.",
                        "teaching_point": "Hastadaki bulgular lakrimal kese ile sınırlı olmayıp etmoid sinüzite sekonder postseptal orbita boşluğu tutulumunu göstermektedir."
                    },
                    {
                        "text": "Steril İdiyopatik Orbital İnflamatuar Psödotümör Sendromu",
                        "is_correct": False,
                        "scenario_update": "Orbital psödotümör enfeksiyöz olmayan steril bir inflamasyondur; akut pürülan rinosinüzit, yüksek ateş, belirgin lökositoz ve etmoid komşuluğunda abse ile seyretmez.",
                        "teaching_point": "Akut rinosinüzit zemininde yüksek ateş, CRP yüksekliği ve lamina papyracea komşuluğunda koleksiyon varlığı bakteriyel orbital selüliti doğrular."
                    },
                    {
                        "text": "Akut Orbital Selülit ve Subperiosteal Abse",
                        "is_correct": True,
                        "explanation": "Proptozis, ağrılı oftalmopleji ve kemozis kliniğine BT'de etmoid sinüzit ve lamina papyracea komşuluğunda periferik kontrastlanan koleksiyon eşlik etmesi akut orbital selülit ve subperiosteal abse tanısını kesinleştirir.",
                        "new_finding": "Kesin tanı: Akut Orbital Selülit ve Sol Medial Subperiosteal Abse (Chandler Evre III - Etmoid Sinüzit Komplikasyonu)."
                    }
                ]
            },
            {
                "stage_title": "Multidisipliner Konsültasyon ve Tedavi Yönetimi",
                "question": "Etmoid sinüzite sekonder akut orbital selülit ve 12x5 mm medial subperiosteal abse tanısı alan 4 yaşındaki hastada doğru yönetim planı hangisidir?",
                "options": [
                    {
                        "text": "İV Seftriakson ve Vankomisin (veya Ampisilin-Sulbaktam) başlayarak hastayı yatırmak, acil Göz ve KBB konsültasyonu ile cerrahi drenaj açısından değerlendirmek",
                        "is_correct": True,
                        "explanation": "Orbital selülit ve subperiosteal abse varlığında S. pneumoniae, S. aureus (MRSA dahil), H. influenzae ve anaeropları kapsayan geniş spektrumlu parenteral antibiyotik başlanmalı, >10 mm abse veya görme tehdidinde KBB/Oftalmoloji ile endoskopik drenaj planlanmalıdır.",
                        "new_finding": "Hastaya İV Seftriakson (100 mg/kg/gün) ve İV Vankomisin (60 mg/kg/gün) başlanarak yatışı yapıldı. KBB ve Göz Hastalıkları konsültasyonu ile endoskopik etmoidektomi ve subperiosteal abse drenajı gerçekleştirildi; hasta görme kaybı gelişmeden şifayla taburcu edildi."
                    },
                    {
                        "text": "Yüksek doz oral amoksisilin-klavulanat (90 mg/kg/gün) şurup ve nazal dekonjestan sprey reçete ederek günlük poliklinik kontrolü şartıyla hastayı taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Ayaktan oral antibiyotikle eve gönderilen hastada subperiosteal abse genişleyerek optik sinir basısına ve kavernöz sinüs trombozuna ilerledi.",
                        "teaching_point": "Oral antibiyotik tedavisi yalnızca komplike olmayan hafif preseptal selülitte düşünülebilir; orbital selülit ve subperiosteal abse mutlak hastane yatışı ve İV tedavi endikasyonudur."
                    },
                    {
                        "text": "Parenteral antibiyotik tedavisi başlamadan önce 48 saat süreyle yalnızca intravenöz yüksek doz metilprednizolon uygulayarak intraorbital doku ödeminin gerilemesini beklemek",
                        "is_correct": False,
                        "scenario_update": "Etkin antimikrobiyal koruma olmadan tek başına verilen yüksek doz sistemik steroid bakteriyel enfeksiyonun intrakraniyal boşluğa hızla yayılmasına neden oldu.",
                        "teaching_point": "Bakteriyel orbital selülitte uygun intravenöz antibiyotik tedavisi başlanmadan tek başına sistemik kortikosteroid uygulanması enfeksiyonun yayılımını hızlandırır."
                    },
                    {
                        "text": "Yalnızca topikal moksifloksasin göz damlası ve düşük doz intramusküler sefazolin uygulayarak KBB veya Göz konsültasyonu istemeden acil gözlemde izlemek",
                        "is_correct": False,
                        "scenario_update": "Kan-beyin ve orbita geçişi yetersiz olan birinci kuşak sefalosporin ve topikal damla altında abse boyutu büyüdü ve görme keskinliği azaldı.",
                        "teaching_point": "Subperiosteal abseli orbital selülitte santral sinir sistemi geçişi yüksek geniş spektrumlu İV antibiyotikler ve acil Oftalmoloji/KBB değerlendirmesi şarttır."
                    }
                ]
            }
        ]
    }
]
