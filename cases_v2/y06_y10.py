# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - Bölüm 2 (Y06 - Y10)
Şartname v2 kurallarına göre yeniden yazılmış klinik simülasyon vakaları.
"""

CASES = [
    {
        "id": "Y06",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "6 Yaş",
        "gender": "Kız",
        "complaint": "Vücutta aniden çıkan kaşıntılı kızarıklıklar ve kabarıklıklar",
        "history": (
            "Çocuk kollarını kaşıyarak diyor ki: 'Doktor abla/abi, her yerim çok kaşınıyor!' Annesi anlatıyor: "
            "'İki saat önce sırtında ve kollarında sivrisinek ısırığı gibi kabarık, etrafı kızarık döküntüler "
            "çıktı. Bir yerdekiler solarken başka yerde yenileri beliriyor. Nefes darlığı, ses kısıklığı, dudak "
            "şişmesi veya kusması olmadı. Üç gün önce hafif burun akıntısı vardı, bugün de ilk kez çilekli "
            "paketli bir atıştırmalık yedi.'"
        ),
        "final_diagnosis": "Akut Ürtiker (Anafilaksi Bulgusu Olmayan)",
        "disposition": "Yeşil Alandan İkinci Kuşak H1 Antihistaminik Tedavisi ve Anafilaksi Uyarı Eğitimi ile Taburculuk",
        "case_pearl": (
            "Ani gelişen eritematöz-ödematöz plaklarla başvuran her çocukta ilk adım sistemik tutulumu (solunum, "
            "kardiyovasküler, gastrointestinal -> Anafilaksi) dışlamaktır. İzole akut ürtikerde ilk tercih tedavi "
            "sedasyon yapmayan 2. kuşak H1-antihistaminiklerdir; rutin laboratuvar veya alerji paneli acil serviste istenmez."
        ),
        "steps": [
            {
                "stage_title": "Sistemik Tarama ve Fizik Muayene",
                "question": "Kaşıntılı döküntülerle başvuran bu çocukta ilk klinik değerlendirmede en öncelikli yaklaşım hangisidir?",
                "options": [
                    {
                        "text": "Hava yolu ödemi, solunum sesleri, tansiyon ve gastrointestinal bulguları sorgulayıp lezyonların basmakla solup solmadığını muayene etmek",
                        "is_correct": True,
                        "explanation": "Akut başlayan kaşıntılı ödematöz plaklar sistemik alerjik reaksiyonun ilk bulgusu olabileceğinden hava yolu, solunum, dolaşım ve mukoza tutulumu mutlaka değerlendirilmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 96/dk, SS 20/dk, TA 100/65 mmHg, SpO2 %99. Dudak, dil ve uvulada ödem yok. Akciğer oskültasyonu doğal, stridor veya wheezing yok. Gövde ve ekstremitelerde basmakla solan, sınırları belirgin eritematöz-ödematöz gezici plaklar mevcut.",
                    },
                    {
                        "text": "Kütanöz lezyonların yaygınlığını dikkate alarak sistemik reaksiyon gelişimini önlemek amacıyla uyluk anterolateralinden intramüsküler adrenalin uygulayıp hastayı monitörize etmek",
                        "is_correct": False,
                        "scenario_update": "Solunum ve dolaşım bulgusu olmayan çocukta intramüsküler adrenalin uygulaması sonrası taşikardi (158/dk), titreme, solukluk ve belirgin anksiyete gelişti.",
                        "teaching_point": "İntramüsküler adrenalin yalnızca mukokütanöz bulgulara solunum, kardiyovasküler veya şiddetli gastrointestinal sistem tutulumunun eşlik ettiği sistemik reaksiyonlarda endikedir; izole deri tutulumunda uygulanmaz.",
                    },
                    {
                        "text": "Damar yolu açarak parenteral birinci kuşak H1-antihistaminik ve metilprednizolon uygulamak üzere hastayı doğrudan Sarı Alana devretmek",
                        "is_correct": False,
                        "scenario_update": "Sarı Alana alınan hastanın tüm yaşamsal bulguları stabil seyretti; parenteral birinci kuşak antihistaminik sonrasında çocukta belirgin sedasyon gelişti.",
                        "teaching_point": "Sistemik tutulumu ve anjiyoödemi olmayan, yaşamsal bulguları stabil hastalarda parenteral sedatif antihistaminik veya rutin intravenöz steroid uygulaması yerine oral tedavi tercih edilir.",
                    },
                    {
                        "text": "Lezyonların vaskülitik veya enfeksiyöz etiyolojisini ayırt etmek için deri lezyonlarının kenarlarını işaretleyip öncelikle dermatoskopik inceleme ve punch biyopsi planlamak",
                        "is_correct": False,
                        "scenario_update": "Sağlık personeli hazırlık yaparken çocuğun sırtındaki ilk plakların kendiliğinden solduğu, buna karşın ön kolda yeni plakların çıktığı gözlendi.",
                        "teaching_point": "Yirmi dört saatten kısa sürede yer değiştirip iz bırakmadan solan akut gezici plaklarda deri biyopsisi endike değildir; biyopsi yalnızca 24-48 saatten uzun süren sabit, purpurik veya ağrılı lezyonlarda düşünülür.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik İstem Kararı",
                "question": "Sistemik tutulumu olmayan ve genel durumu iyi olan bu hastada acil serviste hangi tetkik yaklaşımı seçilmelidir?",
                "options": [
                    {
                        "text": "Besin tetikleyicisini netleştirmek amacıyla acil serviste total IgE ve çilek dahil spesifik IgE paneli istemek",
                        "is_correct": False,
                        "scenario_update": "Kan alma işlemi çocuğu huzursuz etti; laboratuvar spesifik IgE sonuçlarının bir hafta sonra çıkacağını bildirdi ve acil yönetim değişmedi.",
                        "teaching_point": "İlk kez gelişen ve sistemik bulgu içermeyen akut mukokütanöz ataklarda acil serviste spesifik IgE veya geniş alerji taraması yapılması kılavuzlarda önerilmez.",
                    },
                    {
                        "text": "Hiçbir laboratuvar veya alerji testi istemeden mevcut öykü ve fizik muayene bulgularıyla klinik tanı koymak",
                        "is_correct": True,
                        "explanation": "Uluslararası rehberlere göre sistemik reaksiyon bulgusu taşımayan akut olgularda rutin kan veya alerji tetkiki önerilmez; çocuklarda en sık tetikleyici yakın zamanlı viral enfeksiyonlardır.",
                        "new_finding": "Tetkik istenmedi; hastanın genel durumu, orofarenks muayenesi ve solunum bulguları tamamen stabil seyretti.",
                    },
                    {
                        "text": "Enfeksiyöz tetikleyicileri ve gizli inflamasyonu değerlendirmek için tam kan sayımı, CRP, sedimentasyon ve boğaz kültürü istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: WBC 8.900/mm³, eozinofil %3, CRP 3.1 mg/L, sedimentasyon 11 mm/saat. Sonuçlar tedavi planında hiçbir değişiklik sağlamadı.",
                        "teaching_point": "Ateşi ve odak bulgusu olmayan akut kütanöz plaklarda rutin akut faz reaktanları veya kültür tetkikleri tanı ve tedaviyi değiştirmez.",
                    },
                    {
                        "text": "Kompleman aracılı veya otoimmün süreçleri dışlamak üzere serum C3, C4, CH50, ANA ve tiroid otoantikorlarını istemek",
                        "is_correct": False,
                        "scenario_update": "İstenen kompleman ve otoantikor tetkikleri normal sınırlarda raporlandı ve gereksiz maliyet ile bekleme süresine yol açtı.",
                        "teaching_point": "Otoimmün ve kompleman incelemeleri yalnızca altı haftadan uzun süren kronik olgularda veya vaskülit şüphesi varlığında poliklinik koşullarında planlanır.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Mevcut anamnez ve fizik muayene bulgularıyla en olası klinik tanınız nedir?",
                "options": [
                    {
                        "text": "Eritema Multiforme Minör",
                        "is_correct": False,
                        "scenario_update": "Lezyonların üç halkalı sabit hedef tahtası görünümünde olmadığı ve saatler içinde yer değiştirip solduğu yeniden doğrulandı.",
                        "teaching_point": "Eritema multiformede lezyonlar simetrik, sabit (günlerce aynı yerde kalan) ve tipik santral koyu halkalı hedef görünümündedir.",
                    },
                    {
                        "text": "Henoch-Schönlein Purpurası (IgA Vasküliti)",
                        "is_correct": False,
                        "scenario_update": "Lezyonların basmakla tamamen solduğu, alt ekstremite ağırlıklı palpabl purpura niteliği taşımadığı ve artralji bulunmadığı görüldü.",
                        "teaching_point": "IgA vaskülitinde döküntüler basmakla solmayan palpabl purpura karakterindedir; nadiren başlangıçta ödematöz görünse de kısa sürede purpurik hal alır.",
                    },
                    {
                        "text": "İzole Akut Ürtiker",
                        "is_correct": True,
                        "explanation": "Basmakla solan, kaşıntılı, 24 saatten kısa sürede yer değiştiren eritematöz-ödematöz plaklar ve sistemik bulgu olmaması izole akut ürtiker tanısını doğrular.",
                        "new_finding": "Tanı: Akut Ürtiker (anafilaksi bulgusu olmaksızın).",
                    },
                    {
                        "text": "Viral Makülopapüler Ekzantem",
                        "is_correct": False,
                        "scenario_update": "Döküntülerin günlerce sabit kalan makülopapüler elemanlar değil, saatler içinde yer değiştiren belirgin dermal ödem plakları olduğu görüldü.",
                        "teaching_point": "Viral makülopapüler ekzantemler basmakla solabilir ancak saatler içinde kaybolup başka bölgede çıkan gezici dermal ödem plakları oluşturmaz.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu hastada semptom kontrolü ve güvenli taburculuk için en uygun tedavi yaklaşımı hangisidir?",
                "options": [
                    {
                        "text": "Birinci kuşak oral hidroksizin şurup ve 7 günlük oral prednizolon başlayıp şüpheli tüm meyveleri diyetten kalıcı olarak çıkarmak",
                        "is_correct": False,
                        "scenario_update": "Hidroksizin kullanan çocukta ertesi gün okulda ağır uyku hali ve dikkat dağınıklığı gelişti; uzun süreli steroide bağlı huzursuzluk ortaya çıktı.",
                        "teaching_point": "Akut ürtikerde birinci basamak tedavi sedasyon yapmayan ikinci kuşak H1-antihistaminiklerdir; komplike olmayan vakalarda rutin sistemik kortikosteroid ve kanıtlanmamış kalıcı diyet kısıtlaması önerilmez.",
                    },
                    {
                        "text": "Viral prodrom öyküsü nedeniyle oral amoksisilin-klavulanat ve kaşıntı/inflamasyon kontrolü için düzenli ibuprofen süspansiyon reçete ederek taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "İbuprofen dozundan iki saat sonra çocuğun gövdesindeki ürtiker plakları hızla arttı ve üst dudakta hafif anjiyoödem gelişti.",
                        "teaching_point": "Akut ürtikerde non-steroid antiinflamatuar ilaçlar (ibuprofen vb.) lökotrien sentezini artırarak ürtiker ve anjiyoödemi alevlendirebilir; ateş/ağrı durumunda parasetamol tercih edilmelidir.",
                    },
                    {
                        "text": "Yalnızca kalamin losyon ve soğuk uygulama önerip sistemik antihistaminik vermeden 24 saat acil gözlem odasında yatırmak",
                        "is_correct": False,
                        "scenario_update": "Sistemik H1-antihistaminik verilmeyen çocuğun gece boyunca şiddetli kaşıntısı devam etti ve uyuyamadı; yaşamsal bulguları ise tamamen normal kaldı.",
                        "teaching_point": "İzole akut ürtikerde 24 saatlik hastane yatışı gerekmez; oral ikinci kuşak H1-antihistaminik semptomları etkin biçimde kontrol eder.",
                    },
                    {
                        "text": "İkinci kuşak oral H1-antihistaminik başlamak, non-steroid antiinflamatuarlardan kaçınmayı önermek ve sistemik alerji uyarılarını anlatarak taburcu etmek",
                        "is_correct": True,
                        "explanation": "EAACI/GA²LEN/EDF/WAO rehberlerine göre akut ürtikerde ilk tercih standart doz 2. kuşak oral H1-antihistaminiktir; aileye lezyonların birkaç gün dalgalanabileceği ve anafilaksi kırmızı bayrakları anlatılmalıdır.",
                        "new_finding": "Oral setirizin/desloratadin tedavisi düzenlendi; nefes darlığı, ses kısıklığı, dil-dudak şişmesi veya tekrarlayan kusma olursa derhal acile başvuru eğitimi verilerek taburcu edildi.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y07",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "7 Yaş",
        "gender": "Erkek",
        "complaint": "Yanaklarda belirgin kızarıklık ve kollarında dantel gibi döküntü",
        "history": (
            "Çocuk gayet neşeli bir şekilde muayene masasında oturuyor: 'Arkadaşlarım yanaklarıma boya mı sürdün "
            "veya güneşte mi yandın diye sordu ama hiç acımıyor, sadece kollarımdaki kızarıklıklar sıcakta biraz "
            "belli oluyor.' Annesi anlatıyor: 'Bir hafta önce hafif bir kırgınlığı ve burun akıntısı olmuştu, "
            "geçti sanmıştık. Dün iki yanağı parlak kırmızı oldu, bugün de kollarının dış yüzünde ve gövdesinde "
            "kafes veya dantel gibi pembe döküntüler fark ettik. Genel durumu ve iştahı çok iyi.'"
        ),
        "final_diagnosis": "Eritema İnfeksiyozum (Beşinci Hastalık - Parvovirus B19)",
        "disposition": "Yeşil Alandan Semptomatik İzlem ve Bulaştırıcılık/Gebe Teması Bilgilendirmesi ile Taburculuk",
        "case_pearl": (
            "Parvovirus B19'un neden olduğu Eritema İnfeksiyozum'da (Beşinci Hastalık) yanaklarda parlak malar "
            "eritem ('tokatlanmış yüz') ve ekstremitelerde retiküler (dantelvari) döküntü tipiktir. Döküntü "
            "çıktığında hasta artık bulaştırıcı değildir ve okula gidebilir; ancak kronik hemolitik anemili "
            "bireylerde aplastik kriz ve gebelerde fetal hidrops riski unutulmamalıdır."
        ),
        "steps": [
            {
                "stage_title": "Fizik Muayene ve Risk Faktörü Sorgulama",
                "question": "Bu hastada ilk fizik muayene ve anamnez derinleştirmesinde öncelikle neyi değerlendirmelisiniz?",
                "options": [
                    {
                        "text": "Yanaklardaki malar eritemi, ağız çevresi solukluğunu ve ekstremitelerdeki retiküler döküntüyü inceleyip bilinen hemolitik anemi veya gebe temasını sorgulamak",
                        "is_correct": True,
                        "explanation": "Karakteristik iki evreli döküntü paterni klinik tanıyı yönlendirir; etkenin eritroid öncüllere tropizmi nedeniyle kronik hemolitik anemi ve ev içi gebelik teması mutlaka sorgulanmalıdır.",
                        "new_finding": "Vital Bulgular: Ateş 36.6°C, KTA 88/dk, SS 18/dk. Genel durum çok iyi. Her iki yanakta parlak kırmızı malar eritem, perioral solukluk ve ekstremite ekstansör yüzlerinde dantelvari (retiküler) makülopapüler döküntü mevcut. Orofarenks doğal, lenfadenopati veya organomegali yok. Bilinen kan hastalığı ve evde gebe teması yok.",
                    },
                    {
                        "text": "Yüzdeki malar eritem nedeniyle akut fotosensitif bağ dokusu hastalığı düşünerek eklem muayenesi yapıp hastayı acil gözlemde monitörize etmek",
                        "is_correct": False,
                        "scenario_update": "Eklem muayenesinde artrit bulgusu saptanmadı; 1 hafta önceki viral prodrom ve ekstremitelerdeki tipik dantelvari patern göz ardı edilmiş oldu.",
                        "teaching_point": "Kısa viral prodromu izleyen akut çift taraflı malar eritem, perioral solukluk ve ekstremitelerde retiküler döküntü okul çağı çocuklarında öncelikle karakteristik viral ekzantemi düşündürür.",
                    },
                    {
                        "text": "Yüksek bulaştırıcılıklı solunum yolu ekzantemi şüphesiyle hastayı derhal negatif basınçlı izolasyon odasına alıp ağız içinde Koplik lekesi aramak",
                        "is_correct": False,
                        "scenario_update": "İzolasyon odasına alınan çocuğun ateşinin olmadığı, öksürük/koriza/konjonktivit bulgusu taşımadığı ve bukkal mukozasının tamamen doğal olduğu görüldü.",
                        "teaching_point": "Ateşsiz, genel durumu çok iyi olan ve 3C bulgusu (öksürük, koriza, konjonktivit) bulunmayan retiküler döküntülü çocukta kızamık izolasyonu endike değildir.",
                    },
                    {
                        "text": "Yanaklardaki eritem ve perioral solukluğu bakteriyel toksin aracılı döküntü lehine yorumlayıp öncelikle tonsiller eksüda ve Pastia çizgilerini aramak",
                        "is_correct": False,
                        "scenario_update": "Orofarenks muayenesinde tonsiller doğal bulundu, çilek dili saptanmadı ve döküntünün zımpara kağıdı dokusunda değil düz-retiküler yapıda olduğu görüldü.",
                        "teaching_point": "Bakteriyel ekzotoksin kaynaklı döküntülerde akut yüksek ateş, eksüdatif tonsillofarenjit ve deride pütürlü zımpara kağıdı hissi veren yaygın noktasal papüller beklenir.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik İstem Kararı",
                "question": "Bilinen kronik hastalığı olmayan ve muayene bulguları tipik olan bu çocukta hangi tetkik yaklaşımı uygundur?",
                "options": [
                    {
                        "text": "Tanıyı mikrobiyolojik olarak kesinleştirmek için acil serviste viral spesifik IgM/IgG serolojisi ve kantitatif kan PCR testi istemek",
                        "is_correct": False,
                        "scenario_update": "Damar yolu açılırken çocuk ağladı; dış laboratuvara gönderilen seroloji ve PCR sonuçlarının 4 gün sonra çıkacağı öğrenildi.",
                        "teaching_point": "İmmünkompetan ve hematolojik hastalığı bulunmayan çocuklarda karakteristik retiküler ekzantem evresinde serolojik veya moleküler doğrulama testlerine gerek yoktur.",
                    },
                    {
                        "text": "Eritroid seri baskılanmasını ve olası aplastik krizi taramak amacıyla tam kan sayımı, retikülosit yüzdesi ve periferik yayma istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: Hb 12.8 g/dL, Hct %38, Retikülosit %1.1, WBC 7.200/mm³, PLT 265.000/mm³. Tüm hematolojik parametreler normal saptandı.",
                        "teaching_point": "Sağlıklı çocuklarda eritropoezdeki geçici duraklama klinik anemiye yol açmaz; tam kan sayımı ve retikülosit yalnızca kronik hemolitik anemisi (orak hücre, sferositoz vb.) olanlarda endikedir.",
                    },
                    {
                        "text": "Hiçbir laboratuvar veya görüntüleme tetkiki istemeden mevcut karakteristik öykü ve fizik muayene bulgularıyla klinik tanı koymak",
                        "is_correct": True,
                        "explanation": "Sağlıklı çocuklarda tipik malar eritem ve ekstremitelerde dantelvari döküntü varlığında tanı tamamen kliniktir; ek kan tetkiki yönetimi değiştirmez.",
                        "new_finding": "Tetkik istenmedi; tanı klinik bulgularla netleştirildi ve aile bilgilendirme aşamasına geçildi.",
                    },
                    {
                        "text": "Atipik bakteriyel farenjit ve streptokoksik ekzantemi dışlamak için hızlı antijen testi, boğaz kültürü ve ASO titresi istemek",
                        "is_correct": False,
                        "scenario_update": "Hızlı antijen testi negatif sonuçlandı, ASO 90 IU/mL geldi; farenjit bulgusu olmayan çocukta gereksiz sürüntü ve kan işlemi yapıldı.",
                        "teaching_point": "Ateş ve boğaz ağrısı olmayan, orofarenksi doğal saptanan retiküler döküntülü hastada boğaz kültürü veya ASO istemenin tanısal değeri yoktur.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu hastada mevcut bulgularla kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Kızıl (Akut Streptokoksik Ekzantem)",
                        "is_correct": False,
                        "scenario_update": "Orofarenkste eksüda/hiperemi olmadığı, ateşin bulunmadığı ve döküntünün zımpara kağıdı karakteri taşımadığı tekrar değerlendirildi.",
                        "teaching_point": "Kızılda perioral solukluk görülebilse de yüksek ateş, akut tonsillofarenjit, çilek dili ve kıvrım yerlerinde koyulaşan noktasal pütürlü döküntü eşlik eder.",
                    },
                    {
                        "text": "Eritema İnfeksiyozum (Beşinci Hastalık)",
                        "is_correct": True,
                        "explanation": "Hafif prodromdan 1 hafta sonra gelişen parlak malar eritem ('tokatlanmış yüz') ve ekstremitelerde retiküler (dantelvari) döküntü Parvovirus B19 enfeksiyonunun patognomonik bulgusudur.",
                        "new_finding": "Tanı: Eritema İnfeksiyozum (Beşinci Hastalık - Parvovirus B19).",
                    },
                    {
                        "text": "Kızamıkçık (Akut Rubella Enfeksiyonu)",
                        "is_correct": False,
                        "scenario_update": "Muayenede retroauriküler, posterior servikal veya suboksipital ağrılı lenfadenopati saptanmadı ve döküntü dantelvari karakterdeydi.",
                        "teaching_point": "Rubellada belirgin retroauriküler/suboksipital lenfadenopati ve yüzden başlayıp hızla gövdeye yayılan pembe makülopapüler döküntü görülür; retiküler patern tipik değildir.",
                    },
                    {
                        "text": "Roseola İnfantum (Altıncı Hastalık)",
                        "is_correct": False,
                        "scenario_update": "Hasta 7 yaşında olup 3-4 gün süren yüksek ateşin aniden düşmesiyle gövdeden başlayan döküntü öyküsü bulunmamaktadır.",
                        "teaching_point": "Roseola İnfantum tipik olarak 6 ay - 2 yaş arasında görülür ve birkaç gün süren yüksek ateşin krizle düşmesini takiben gövdede makülopapüler döküntü yapar.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi, İzlem ve Okula Dönüş Kararı",
                "question": "Aile çocuğun tedavisi ve yarın okula gidip gidemeyeceği konusunda bilgi istiyor. En doğru yaklaşım hangisidir?",
                "options": [
                    {
                        "text": "Döküntü solana kadar 7 gün ev izolasyonu raporu düzenlemek, kaşıntı olmasa da oral antihistaminik ve topikal steroid krem başlamak",
                        "is_correct": False,
                        "scenario_update": "Bulaştırıcılığı sona ermiş olan çocuk gereksiz yere bir hafta okuldan geri kaldı ve semptomsuz lezyonlara gereksiz topikal steroid uygulandı.",
                        "teaching_point": "Eritema İnfeksiyozum'da döküntü immün kompleks aracılıdır; döküntü çıktığında viremi ve bulaştırıcılık bitmiştir, bu nedenle okuldan izolasyon önerilmez.",
                    },
                    {
                        "text": "İlaç gerekmediğini, döküntü çıktığında bulaştırıcılığın bittiğini, okula gidebileceğini ve döküntünün sıcakla birkaç hafta tekrarlayabileceğini anlatıp taburcu etmek",
                        "is_correct": True,
                        "explanation": "Parvovirus B19 enfeksiyonunda bulaştırıcılık döküntü öncesi prodromal dönemdedir; ekzantem evresinde çocuk bulaştırıcı değildir. Sıcak banyo, egzersiz ve güneşle döküntünün 1-3 hafta dalgalanabileceği aileye açıklanmalıdır.",
                        "new_finding": "Aileye bulaştırıcılığın geçtiği, okula devam edebileceği ve döküntünün sıcak/egzersizle geçici olarak belirginleşebileceği anlatılarak hasta taburcu edildi.",
                    },
                    {
                        "text": "Viral replikasyonu baskılamak ve eklem komplikasyonlarını önlemek amacıyla 5 gün oral asiklovir süspansiyon başlayıp evde istirahat önermek",
                        "is_correct": False,
                        "scenario_update": "Başlanan asiklovir tedavisi tek sarmallı DNA virüsü olan Parvovirus B19 üzerinde hiçbir etki göstermedi ve gereksiz ilaç maruziyeti oluşturdu.",
                        "teaching_point": "Asiklovir yalnızca herpesvirüs ailesine (HSV, VZV) etkilidir; Parvovirus B19 enfeksiyonunda antiviral tedavinin yeri yoktur.",
                    },
                    {
                        "text": "Çocuğun okula dönüşüne izin vermek ancak sınıfındaki tüm çocuklara ve öğretmenlere profilaktik oral antibiyotik başlanmasını yazılı olarak önermek",
                        "is_correct": False,
                        "scenario_update": "Okul yönetimi ve veliler arasında gereksiz panik oluştu; viral bir etken için uygunsuz antibiyotik profilaksisi gündeme geldi.",
                        "teaching_point": "Parvovirus B19 için temaslılara antibiyotik profilaksisi uygulanmaz; yalnızca temaslılar arasında gebe veya kronik hemolitik anemili birey varsa kendi hekimine yönlendirilir.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y08",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "10 Aylık",
        "gender": "Kız",
        "complaint": "Üç gün süren yüksek ateşin düşmesiyle birlikte gövdede çıkan döküntü",
        "history": (
            "Annesi endişeyle anlatıyor: 'Doktor hanım/bey, kızımın 3 gün boyunca 39.5°C'ye varan ateşi oldu, "
            "ateş düşürücüyle düşüp tekrar çıkıyordu ama keyfi ve emmesi fena değildi. Bu sabah ateşi tamamen "
            "düştü, rahatladık; fakat öğleden sonra karnında, göğsünde ve sırtında pembe-kırmızı lekeler çıktı! "
            "Dün verdiğimiz ateş düşürücü şuruptan alerji mi oldu diye çok korktuk.'"
        ),
        "final_diagnosis": "Roseola İnfantum (Altıncı Hastalık / Ekzantema Subitum - HHV-6)",
        "disposition": "Yeşil Alandan İlaç Alerjisi Olmadığının Anlatılması ve Destek Önerileri ile Taburculuk",
        "case_pearl": (
            "Altı ay - 2 yaş arası süt çocuklarında 3-4 gün süren yüksek ateşin aniden (kriz şeklinde) düşmesiyle "
            "gövdeden başlayan, kaşıntısız, basmakla solan gül pembesi makülopapüler döküntü Roseola İnfantum "
            "(HHV-6/7) için klasiktir. Sıklıkla ateş döneminde kullanılan antipiretik veya antibiyotik alerjisi ile "
            "karıştırılır; çocuğa yanlışlıkla 'ilaç alerjisi' etiketi konulmamalıdır."
        ),
        "steps": [
            {
                "stage_title": "Fizik Muayene",
                "question": "Ateşi düştükten sonra gövdede döküntüsü çıkan bu 10 aylık bebekte ilk muayenede neyi değerlendirmelisiniz?",
                "options": [
                    {
                        "text": "Ateş düşürücüye bağlı erken sistemik alerjik reaksiyon düşünerek hızla uyluktan intramüsküler adrenalin uygulayıp damar yolu açmak",
                        "is_correct": False,
                        "scenario_update": "Yaşamsal bulguları normal, kaşıntısı veya solunum sıkıntısı olmayan bebekte adrenalin enjeksiyonu sonrası ciddi taşikardi ve huzursuzluk gelişti.",
                        "teaching_point": "Ateş düştükten sonra ortaya çıkan, kaşıntısız, ödematöz plak içermeyen ve sistemik bulgunun eşlik etmediği makülopapüler döküntülerde adrenalin endikasyonu yoktur.",
                    },
                    {
                        "text": "Yaşamsal bulgular, genel görünüm, ön fontanel, yumuşak damaktaki eritematöz papüller ve gövdedeki döküntünün basmakla solma özelliğini değerlendirmek",
                        "is_correct": True,
                        "explanation": "Üç günlük yüksek ateşin kriz şeklinde düşmesi, bebeğin aktif/huzurlu görünümü ve gövdeden başlayan basmakla solan makülopapüler döküntü karakteristik viral ekzantem seyrini gösterir.",
                        "new_finding": "Vital Bulgular: Ateş 36.5°C, KTA 115/dk, SS 26/dk. Bebek etrafa gülümsüyor, aktif. Ön fontanel normal bombelikte. Gövde, boyun ve sırt ağırlıklı, basmakla solan 2-5 mm çaplı gül pembesi makülopapüler döküntüler mevcut; peteşi/purpura ve kaşıntı yok. Yumuşak damakta hafif eritematöz papüller izlendi.",
                    },
                    {
                        "text": "Üç gün süren yüksek ateş ve yeni başlayan döküntüyü santral sinir sistemi enfeksiyonu bulgusu kabul ederek acil lomber ponksiyon hazırlığı yapmak",
                        "is_correct": False,
                        "scenario_update": "Ateşi tamamen düşmüş, ön fontaneli normal ve gülümseyerek oyun oynayan bebekte invaziv girişim hazırlığı aileyi çok endişelendirdi.",
                        "teaching_point": "Ateşi krizle düşmüş, genel durumu çok iyi, ön fontaneli normal ve döküntüsü basmakla solan süt çocuğunda lomber ponksiyon endike değildir.",
                    },
                    {
                        "text": "Döküntülerin olası bakteriyel sepsis kaynağı olabileceğini düşünerek bebeği Sarı Alana devredip geniş spektrumlu intravenöz antibiyotik hazırlamak",
                        "is_correct": False,
                        "scenario_update": "Sarı Alana alınan bebeğin kapiller dolumu 1 saniye, ateşi 36.5°C ve aktivitesi tam olarak izlendi; toksik görünüm saptanmadı.",
                        "teaching_point": "Basmakla solan pembe makülopapüler döküntüsü olan, ateşi düşmüş ve perfüzyonu normal bir süt çocuğunda meningokoksemi veya bakteriyel sepsis düşünülmez.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik İstem Kararı",
                "question": "Genel durumu çok iyi, ateşi düşmüş ve tipik gövde döküntüsü saptanmış bu bebekte hangi tetkik yaklaşımı doğrudur?",
                "options": [
                    {
                        "text": "Geçirilmiş üç günlük yüksek ateşin gizli bakteriyel odağını dışlamak için tam kan sayımı, CRP, kan kültürü ve mesane sondası ile idrar kültürü almak",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: WBC 5.200/mm³ (%70 lenfosit), CRP 1.9 mg/L, tam idrar tetkiki normal. İyileşme evresindeki bebekte gereksiz invaziv kateterizasyon yapıldı.",
                        "teaching_point": "Odağı belirsiz ateş döneminde idrar tetkiki önemli olsa da, ateş tamamen düşüp karakteristik viral ekzantem ortaya çıktığında tanı netleşmiştir ve invaziv sepsis taraması yapılmaz.",
                    },
                    {
                        "text": "Antipiretik ilaç duyarlılığını doğrulamak amacıyla acil serviste parasetamol spesifik IgE, triptaz düzeyi ve oral ilaç provokasyon testi planlamak",
                        "is_correct": False,
                        "scenario_update": "Laboratuvarda parasetamol için rutin spesifik IgE kiti bulunmadığı bildirildi; akut dönemde provokasyon girişimi ise gereksiz zaman kaybına yol açtı.",
                        "teaching_point": "Ateşin düşmesiyle başlayan kaşıntısız makülopapüler döküntü ilaç reaksiyonu değil, viral enfeksiyonun doğal iyileşme evresi olan ekzantem dönemidir.",
                    },
                    {
                        "text": "Hiçbir laboratuvar veya görüntüleme tetkiki istemeden tipik klinik seyir ve fizik muayene bulgularıyla tanı koymak",
                        "is_correct": True,
                        "explanation": "Üç gün yüksek ateş sonrası ateşin düşmesiyle çıkan karakteristik makülopapüler döküntü evresinde tanı tamamen kliniktir; laboratuvar tetkiki gerekmez.",
                        "new_finding": "Ek tetkik istenmedi; klinik değerlendirme tanı için yeterli görülerek aile eğitimi aşamasına geçildi.",
                    },
                    {
                        "text": "Kızamık ve kızamıkçık serolojisi (IgM/IgG) ile boğaz sürüntüsünden solunum yolu viral PCR paneli göndererek sonuç çıkana kadar gözlemde tutmak",
                        "is_correct": False,
                        "scenario_update": "Seroloji sonuçlarının ertesi gün çıkacağı öğrenildi; bebek acil gözlem odasında gereksiz yere saatlerce bekletildi.",
                        "teaching_point": "Öksürük, koriza, konjonktivit ve ateş olmadan ateşin düşmesini takiben gövdeden başlayan döküntüde kızamık serolojisi veya acil gözlem yatışı endike değildir.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu hastada mevcut öykü ve muayene bulgularıyla kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Roseola İnfantum (Ekzantema Subitum)",
                        "is_correct": True,
                        "explanation": "Altı ay - 2 yaş arası bebekte 3-4 gün süren yüksek ateşin aniden düşmesi ve hemen ardından gövdeden başlayan kaşıntısız gül pembesi makülopapüler döküntü Roseola İnfantum'un klasik tablosudur.",
                        "new_finding": "Tanı: Roseola İnfantum (HHV-6 / Altıncı Hastalık).",
                    },
                    {
                        "text": "Parasetamole Bağlı Makülopapüler İlaç Erüpsiyonu",
                        "is_correct": False,
                        "scenario_update": "Döküntüde kaşıntı veya eozinofili bulgusu olmadığı, tablonun ateşin krizle düşmesini izleyen klasik viral seyir olduğu doğrulandı.",
                        "teaching_point": "İlaç erüpsiyonları genellikle kaşıntılıdır, ilacın ilk dozlarından ziyade günler süren duyarlanma sonrası gelişir ve ateşin kriz şeklinde düşmesiyle eş zamanlı tipik viral dizilim göstermez.",
                    },
                    {
                        "text": "Kızamık (Akut Morbilli Enfeksiyonu)",
                        "is_correct": False,
                        "scenario_update": "Bebekte döküntü çıktığında ateşin tamamen düştüğü, döküntünün saç çizgisi/kulak arkasından değil gövdeden başladığı ve 3C bulgusunun olmadığı görüldü.",
                        "teaching_point": "Kızamıkta döküntü çıktığında ateş en yüksek seviyesindedir, çocuk düşkün görünür ve döküntü kulak arkasından başlayıp aşağı yayılır.",
                    },
                    {
                        "text": "Akut İnvaziv Meningokoksemi Tablosu",
                        "is_correct": False,
                        "scenario_update": "Döküntülerin basmakla tamamen solduğu (peteşiyal/purpurik olmadığı), bebeğin ateşsiz ve gayet neşeli olduğu teyit edildi.",
                        "teaching_point": "Meningokoksemide toksik görünüm, dolaşım bozukluğu ve basmakla solmayan peteşiyal/purpurik lezyonlar görülür.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Aile Bilgilendirmesi",
                "question": "Bu aşamada bebeğin tedavisi ve ailenin ilaç alerjisi endişesi için en doğru yaklaşım hangisidir?",
                "options": [
                    {
                        "text": "İlaç gerekmediğini, tablonun ateş düşürücü alerjisi olmadığını ve döküntülerin birkaç gün içinde iz bırakmadan solacağını anlatarak taburcu etmek",
                        "is_correct": True,
                        "explanation": "Roseola İnfantum'da döküntü çıkışı iyileşme evresini gösterir; hekimin en kritik görevi gereksiz ilaçları önlemek ve çocuğa yanlış 'parasetamol alerjisi' etiketi konulmasının önüne geçmektir.",
                        "new_finding": "Ailenin ilaç alerjisi endişesi giderildi, ileride parasetamol kullanabilecekleri ve döküntünün 1-3 günde kendiliğinden geçeceği anlatılarak bebek taburcu edildi.",
                    },
                    {
                        "text": "Çocuğun elektronik sağlık kaydına 'Parasetamol Alerjisi' işlemek, beş gün oral setirizin damla ve kısa süreli oral prednizolon reçete etmek",
                        "is_correct": False,
                        "scenario_update": "Yanlış ilaç alerjisi kaydı nedeniyle bebeğin sonraki ateşli hastalıklarında antipiretik kullanımı kısıtlandı ve gereksiz steroid maruziyeti oluştu.",
                        "teaching_point": "Roseola İnfantum döküntüsünü ilaç alerjisi sanarak çocuğu temel antipiretiklerden mahrum bırakmak sık yapılan bir hatadır; kaşıntısız viral ekzantemde antihistaminik ve steroid verilmez.",
                    },
                    {
                        "text": "Human Herpesvirus-6 viremisini baskılamak ve febril nöbet riskini önlemek amacıyla 7 gün oral asiklovir veya valasiklovir süspansiyon başlamak",
                        "is_correct": False,
                        "scenario_update": "Ateşi zaten düşmüş ve iyileşme fazına girmiş olan bebekte etkisiz ve gereksiz antiviral tedavi kullanılmış oldu.",
                        "teaching_point": "İmmünkompetan çocuklarda Roseola İnfantum kendi kendini sınırlar; hem asiklovir HHV-6'ya karşı etkisizdir hem de döküntü evresinde hastalık zaten iyileşmiştir.",
                    },
                    {
                        "text": "Döküntülerin sekonder bakteriyel enfeksiyonunu önlemek için topikal mupirosin krem ve 5 gün oral amoksisilin süspansiyon reçete ederek kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Sağlam derideki makülopapüler viral döküntü için verilen oral antibiyotik bebekte antibiyotik ilişkili ishale neden oldu.",
                        "teaching_point": "Bütünlüğü bozulmamış, vezikül veya krut içermeyen viral makülopapüler döküntülerde topikal veya sistemik antibiyotiklerin hiçbir yeri yoktur.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y09",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "2.5 Yaş",
        "gender": "Erkek",
        "complaint": "Ağız içinde ağrılı yaralar, yemek yemeyi reddetme, avuç içi ve ayak tabanında döküntü",
        "history": (
            "Annesi anlatıyor: 'İki gündür ağzından salyası akıyor, çok sevdiği yemekleri bile ağzına götürüp "
            "ağlayarak bırakıyor. Dün 38.2°C ateşi oldu. Bugün de avuç içlerinde, ayak tabanlarında ve bez "
            "bölgesinde kırmızı küçük su toplamış döküntüler fark ettik. Su ve soğuk sütü azar azar içebiliyor, "
            "bezini normal ıslatıyor.'"
        ),
        "final_diagnosis": "El-Ayak-Ağız Hastalığı (Enterovirus / Coxsackievirus A16 - A6)",
        "disposition": "Yeşil Alandan Ağrı Kontrolü, Soğuk/Yumuşak Gıda-Sıvı Desteği ve İzlem ile Taburculuk",
        "case_pearl": (
            "Oral mukozada ağrılı vezikül/ülserler ve avuç içi, ayak tabanı ile gluteal bölgede eritemli zeminde "
            "eliptik veziküller El-Ayak-Ağız hastalığı için tipiktir. En sık komplikasyonu ağrılı oral lezyonlara "
            "bağlı yutma güçlüğü ve dehidratasyondur; tedavide sistemik analjezi ve soğuk/asitsiz sıvılarla "
            "hidrasyonun sürdürülmesi esastır."
        ),
        "steps": [
            {
                "stage_title": "Fizik Muayene ve Hidrasyon Kontrolü",
                "question": "Bu hastada ilk fizik muayenede öncelikle hangi bulguları değerlendirmelisiniz?",
                "options": [
                    {
                        "text": "Ağız içindeki vezikülleri abeslangla kazıyarak psödomembran varlığını kontrol etmek ve avuç içindeki lezyonları steril iğneyle drene etmek",
                        "is_correct": False,
                        "scenario_update": "Ağrılı oral ülserlere yapılan mekanik müdahale mukozal kanamaya ve çocuğun şiddetli ağlayarak ağızdan sıvı alımını tamamen reddetmesine yol açtı.",
                        "teaching_point": "Oral mukozadaki viral vezikül ve ülserler kesinlikle kazınmaz, akral derideki veziküller ise sekonder bakteriyel enfeksiyon riski nedeniyle patlatılmaz.",
                    },
                    {
                        "text": "Akral yerleşimli lezyonları bakteriyel septik emboli veya invaziv döküntü kabul ederek hastayı hızla Sarı Alana devredip damar yolu açmak",
                        "is_correct": False,
                        "scenario_update": "Sarı Alana alınan çocuğun yaşamsal bulguları ve kapiller dolumu tamamen normal bulundu; lezyonların purpurik değil gri-beyaz veziküller olduğu görüldü.",
                        "teaching_point": "Genel durumu iyi olan çocukta oral ülserlere eşlik eden avuç içi, ayak tabanı ve gluteal eliptik veziküller tipik viral enantem-ekzantem kompleksidir.",
                    },
                    {
                        "text": "Orofarenks ve bukkal mukozadaki ülserleri, avuç içi-ayak tabanı-gluteal vezikülleri, hidrasyon durumunu ve miyokloni/ataksi gibi nörolojik bulguları değerlendirmek",
                        "is_correct": True,
                        "explanation": "Karakteristik oral ve akral vezikül dağılımı tanıyı yönlendirir; ağrılı yutma nedeniyle hidrasyon durumu ve nadir santral sinir sistemi tutulumu bulguları mutlaka kontrol edilmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 37.9°C, KTA 116/dk, SS 24/dk. Dil, bukkal mukoza ve yumuşak damakta eritemli haleli 3-4 mm ağrılı vezikül ve ülserler mevcut. Avuç içlerinde, ayak tabanlarında ve gluteal bölgede eliptik gri-beyaz vezikülopapüler lezyonlar var. Ağız mukozası nemli, gözyaşı var, dehidratasyon yok. Nörolojik muayene doğal.",
                    },
                    {
                        "text": "Ağız içi muayeneyi çocuğun ağlamasını artırmamak için tamamen atlayıp yalnızca sırt ve gövde derisinde polimorfik döküntü aramak",
                        "is_correct": False,
                        "scenario_update": "Sırt ve göğüste döküntü saptanmadı; ağız içi ve mukoza ıslaklığı değerlendirilmediği için beslenme reddi nedeni ve hidrasyon durumu eksik kaldı.",
                        "teaching_point": "Salya artışı ve beslenme reddi ile başvuran küçük çocukta orofarenks lezyonlarının ve mukoza nemliliğinin görülmesi temel muayene basamağıdır.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik İstem Kararı",
                "question": "Dehidratasyonu ve nörolojik bulgusu olmayan, tipik oral-akral vezikülleri saptanan bu çocukta hangi tetkik yaklaşımı seçilmelidir?",
                "options": [
                    {
                        "text": "Avuç içindeki vezikül tabanından kazıntı alarak Tzanck yayması, Herpes Simpleks PCR ve Varisella Zoster IgM serolojisi istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: Tzanck yaymasında multinükleer dev hücre görülmedi, HSV ve VZV testleri negatif sonuçlandı; işlem çocuğu gereksiz travmatize etti.",
                        "teaching_point": "Oral ülser ve avuç içi/ayak tabanı/gluteal eliptik vezikül birlikteliği klinik olarak tanı koydurucudur; rutin Tzanck yayması veya herpes serolojisi istenmez.",
                    },
                    {
                        "text": "Orofarenksteki lezyonlar nedeniyle bakteriyel tonsillofarenjiti dışlamak üzere hızlı streptokok antijen testi ve boğaz kültürü almak",
                        "is_correct": False,
                        "scenario_update": "Hızlı antijen testi negatif çıktı; ülserli bukkal mukoza ve dile sürüntü çubuğu değdirilmesi şiddetli ağrıya neden oldu.",
                        "teaching_point": "Ön oral kavitede (dil, bukkal mukoza) vezikül-ülserler ve el-ayak lezyonları ile seyreden tabloda bakteriyel boğaz kültürü endikasyonu yoktur.",
                    },
                    {
                        "text": "Yemek yemeyi reddettiği için klinik dehidratasyon bulgusu olmasa bile rutin kan gazı, serum elektrolitleri, üre ve kreatinin istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: Na 137 mEq/L, K 4.2 mEq/L, Glukoz 86 mg/dL, Üre 19 mg/dL, pH 7.40. Tüm değerler normal geldi.",
                        "teaching_point": "Sıvı alabilen, idrar çıkışı normal olan ve fizik muayenede dehidratasyon bulgusu saptanmayan çocukta rutin venöz biyokimya tetkiki gerekmez.",
                    },
                    {
                        "text": "Ek laboratuvar tetkiki istemeden tipik anatomik lezyon dağılımı ve normal hidrasyon bulgularıyla klinik tanı koymak",
                        "is_correct": True,
                        "explanation": "Oral mukozada vezikül/ülserler ve akral-gluteal vezikülopapüler döküntü karakteristik bir klinik sendromdur; komplike olmayan vakalarda laboratuvar testi önerilmez.",
                        "new_finding": "Tetkik istenmedi; acil serviste çocuğun soğuk sütü yudumlayarak kusmadan tolere edebildiği gözlendi.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu hastada mevcut bulgularla kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Primer Herpetik Gingivostomatit",
                        "is_correct": False,
                        "scenario_update": "Hastanın diş etlerinde yaygın hiperemi, şişlik veya kolay kanama (gingivit) olmadığı; buna karşın el, ayak ve gluteal veziküllerin bulunduğu görüldü.",
                        "teaching_point": "Herpetik gingivostomatitte yüksek ateş, belirgin diş eti ödemi/kanaması ve perioral veziküller ön plandadır; avuç içi, ayak tabanı ve gluteal vezikül beklenmez.",
                    },
                    {
                        "text": "Suçiçeği (Varisella Enfeksiyonu)",
                        "is_correct": False,
                        "scenario_update": "Saçlı deri ve gövdede farklı evrelerde (makül, papül, vezikül, krut bir arada) kaşıntılı santripetal döküntü saptanmadı.",
                        "teaching_point": "Suçiçeğinde döküntü saçlı deri ve gövdeden başlar (merkezden perifere yayılır) ve polimorfiktir; avuç içi ve ayak tabanı tutulumu nadirdir.",
                    },
                    {
                        "text": "El-Ayak-Ağız Hastalığı",
                        "is_correct": True,
                        "explanation": "Oral vezikül/ülserler ile avuç içi, ayak tabanı ve gluteal bölgedeki eliptik veziküller enteroviral El-Ayak-Ağız hastalığını doğrular.",
                        "new_finding": "Tanı: El-Ayak-Ağız Hastalığı (Enteroviral veziküler stomatit ve ekzantem).",
                    },
                    {
                        "text": "Akut Herpangina (İzole Faringeal Enantem)",
                        "is_correct": False,
                        "scenario_update": "Hastada yalnızca arka farenks/tonsiller plikada sınırlı lezyonlar değil, aynı zamanda el ayası, ayak tabanı ve gluteal bölgede veziküller mevcut.",
                        "teaching_point": "Yine enterovirüslerin neden olduğu herpanginada vezikül ve ülserler yalnızca yumuşak damak, uvula ve ön tonsiller plikalarda yer alır; el ve ayak döküntüsü bulunmaz.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu hastada ağrı yönetimi, beslenme ve taburculuk için en doğru yaklaşım hangisidir?",
                "options": [
                    {
                        "text": "Beslenmeden 30 dakika önce sistemik analjezik, soğuk-yumuşak-asitsiz gıdalar, bol sıvı desteği ve kırmızı bayrak eğitimi ile taburcu etmek",
                        "is_correct": True,
                        "explanation": "El-Ayak-Ağız hastalığında spesifik antiviral yoktur; öğün öncesi sistemik analjezi ve soğuk/nötr gıdalar (yoğurt, soğuk süt, püre) oral ağrıyı azaltarak dehidratasyonu önler.",
                        "new_finding": "Sistemik analjezik ve soğuk/yumuşak beslenme planı düzenlendi; idrar azalması, uykuya meyil veya sıçrama/dengesizlik olursa başvuru eğitimi ve haftalar sonra tırnak değişimi (onikomadezis) olabileceği bilgisi verilerek taburcu edildi.",
                    },
                    {
                        "text": "Oral asiklovir süspansiyon ve sekonder enfeksiyon profilaksisi için amoksisilin başlamak, yemeklerden önce ağız içine yoğun topikal lidokain sprey sıkmak",
                        "is_correct": False,
                        "scenario_update": "Asiklovir ve antibiyotik enterovirüslere etki etmedi; 2.5 yaşındaki çocukta yutulan topikal lidokain öğürme refleksini baskıladı ve sistemik toksisite riski yarattı.",
                        "teaching_point": "Enterovirüslere asiklovir veya antibiyotik etki etmez; küçük çocuklarda oral topikal lidokain (konvülziyon, aritmi ve aspirasyon riski nedeniyle) kesinlikle önerilmez.",
                    },
                    {
                        "text": "Bağışıklığı güçlendirmek amacıyla bol taze sıkılmış portakal-limon suyu ve sıcak kemik suyu çorbası içirilmesini önerip analjezik vermeden taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Asitli narenciye suları ve sıcak çorba ülserli oral mukozada şiddetli yanma yaptığı için çocuk ağızdan sıvı alımını tamamen kesti.",
                        "teaching_point": "Oral mukoza ülserlerinde asitli, tuzlu, baharatlı ve sıcak gıda/içecekler ağrıyı şiddetlendirir; soğuk veya oda ısısında nötr sıvılar tercih edilmelidir.",
                    },
                    {
                        "text": "Oral ülserlerin iyileşmesini hızlandırmak için 5 gün oral prednizolon şurup başlamak ve el-ayak veziküllerine potasyum permanganatlı sıcak banyo uygulamak",
                        "is_correct": False,
                        "scenario_update": "Kortikosteroid kullanımı akut enteroviral enfeksiyon seyrinde mukozal iyileşmeyi sağlamadığı gibi viral replikasyon açısından risk oluşturdu.",
                        "teaching_point": "Komplike olmayan El-Ayak-Ağız hastalığında sistemik kortikosteroidler kontrendikedir; veziküller kendi kendine kuruyup iyileşir.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y10",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "10 Yaş",
        "gender": "Erkek",
        "complaint": "Üç haftadır özellikle gece yatınca ve sabah kalkınca artan öksürük, burun tıkanıklığı ve geniz akıntısı",
        "history": (
            "Hasta kendisi anlatıyor: 'Doktor bey/hanım, gündüz okulda pek öksürmüyorum ama akşam yastığa başımı "
            "koyunca ve sabah uyanınca boğazımda bir şey gıdıklanıyor gibi öksürüyorum, sürekli boğazımı "
            "temizleme ihtiyacı hissediyorum. Burnum da çok kaşınıyor ve sabahları üst üste hapşırıyorum. Ateşim "
            "hiç çıkmadı, beden eğitimi dersinde koşarken nefesim daralmıyor veya göğsümden ıslık sesi gelmiyor.'"
        ),
        "final_diagnosis": "Alerjik Rinit ve Postnazal Akıntı Sendromuna (Üst Hava Yolu Öksürük Sendromu) Bağlı Öksürük",
        "disposition": "Yeşil Alandan İntranazal Kortikosteroid / Antihistaminik ve Alerjen Önlemleri ile Taburculuk",
        "case_pearl": (
            "Ateşsiz, özellikle yatınca ve sabah kalkınca belirginleşen, boğaz temizleme hareketi, burun kaşıntısı "
            "ve hapşırığın eşlik ettiği öksürüklerde en sık neden Alerjik Rinit ve buna bağlı Postnazal Akıntıdır. "
            "Orta-ağır veya persistan semptomlarda en etkili birinci basamak antiinflamatuar tedavi intranazal "
            "kortikosteroid spreylerdir."
        ),
        "steps": [
            {
                "stage_title": "Odaklı Fizik Muayene",
                "question": "Pozisyonel öksürük ve burun semptomları ile başvuran bu çocukta fizik muayenede öncelikle hangi bulguları aramalısınız?",
                "options": [
                    {
                        "text": "Üç haftayı bulan öksürük nedeniyle üst hava yolu muayenesini atlayıp yalnızca bazal akciğer oskültasyonu ve parmaklarda çomaklaşma kontrolü yapmak",
                        "is_correct": False,
                        "scenario_update": "Akciğer oskültasyonu tamamen normal saptandı; ancak burun boşluğu ve orofarenks arka duvarı incelenmediği için öksürüğün asıl anatomik kaynağı gözden kaçtı.",
                        "teaching_point": "Yatınca ve sabah uyanınca artan, boğaz temizleme ile karakterize öksürüklerde rinoskopik muayene ve arka farenks duvarı değerlendirmesi atlanmamalıdır.",
                    },
                    {
                        "text": "Nazal konkalarda soluk-mavimsi ödem, burun sırtında yatay çizgi, arka farenkste kaldırım taşı görünümü ve akciğer seslerini değerlendirmek",
                        "is_correct": True,
                        "explanation": "Kronik burun kaşıntısı ve geniz akıntısı yakınmalarında soluk-ödemli nazal konkalar ve arka farenks duvarında lenfoid folikül hipertrofisi (kaldırım taşı görünümü) tanısal anahtardır.",
                        "new_finding": "Vital Bulgular: Ateş 36.6°C, KTA 82/dk, SS 16/dk, SpO2 %99. Burun sırtında enine katlantı izi, rinoskopide bilateral alt konkalar soluk-mavimsi ve ödemli, berrak sekresyon mevcut. Orofarenks arka duvarında mukoid akıntı ve lenfoid folikül hipertrofisi (kaldırım taşı görünümü) var. Akciğer oskültasyonu tamamen doğal, ral/ronküs/wheezing yok.",
                    },
                    {
                        "text": "Gece öksürüğünü alt hava yolu obstrüksiyonu kabul ederek muayene öncesinde 3 doz nebülize salbutamol verip oskültasyon yanıtını değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Bronkodilatör nebülizasyon sonrası hastada taşikardi ve el titremesi gelişti; hışıltısı olmayan hastanın geniz akıntısı ve boğaz gıdıklanması hissinde değişiklik olmadı.",
                        "teaching_point": "Efor dispnesi, hışıltı veya ekspiratuar uzaması olmayan, yalnızca yatınca geniz akıntısıyla öksüren hastada ampirik bronkodilatör yüklemesi uygun değildir.",
                    },
                    {
                        "text": "Yabancı cisim aspirasyonu veya endobronşiyal kitleyi dışlamak için hastayı aç bırakıp acil fleksibl bronkoskopi açısından çocuk göğüs hastalıklarına danışmak",
                        "is_correct": False,
                        "scenario_update": "Ani boğulma öyküsü olmayan, bilateral solunum sesleri eşit ve doğal saptanan çocukta invaziv bronkoskopi endikasyonu bulunmadı.",
                        "teaching_point": "Ani başlangıçlı boğulma öyküsü, asimetrik solunum sesi veya fokal oskültasyon bulgusu olmayan üst hava yolu kaynaklı öksürükte bronkoskopi düşünülmez.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik İstem Kararı",
                "question": "Rinoskopi ve orofarenks bulguları tipik, akciğer oskültasyonu tamamen doğal olan bu hastada acil serviste hangi tetkik gerekir?",
                "options": [
                    {
                        "text": "Paranazal sinüslerin durumunu ve akciğer parankimini görüntülemek amacıyla Waters sinüs grafisi, PA akciğer grafisi ve sinüs BT istemek",
                        "is_correct": False,
                        "scenario_update": "GÖRÜNTÜLEME SONUCU: PA akciğer grafisi normal; sinüs görüntülemesinde yalnızca bilateral alt konka hipertrofisi ve hafif mukozal kalınlaşma izlendi.",
                        "teaching_point": "Pürülan akıntı, ateş veya yüz ağrısı olmayan berrak sekresyonlu mukozal ödem tablosunda rutin radyografi veya sinüs tomografisi endike değildir; gereksiz radyasyon verir.",
                    },
                    {
                        "text": "Atipik bakteriyel enfeksiyon ve boğmaca olasılığını dışlamak için tam kan sayımı, CRP, Mycoplasma IgM ve nazofaringeal Bordetella PCR istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: WBC 6.800/mm³, CRP 0.8 mg/L; seroloji ve PCR sonuçlarının günler sonra çıkacağı bildirildi.",
                        "teaching_point": "Boğulur tarzda paroksismal öksürük nöbeti, inspiratuar 'whoop' sesi, kusma veya ateş olmayan, tipik nazal kaşıntı/hapşırıkla seyreden tabloda enfeksiyon tetkiki istenmez.",
                    },
                    {
                        "text": "Acil serviste solunum fonksiyon testi (spirometri), fraksiyone ekshale nitrik oksit (FeNO) ve geniş aeroalerjen deri prick testi uygulamak",
                        "is_correct": False,
                        "scenario_update": "Acil servis koşullarında spirometri ve deri prick testi yapılamadı; hastanın taburculuğu gereksiz yere gecikti.",
                        "teaching_point": "İleri alerji deri testleri ve solunum fonksiyon ölçümleri acil servis tetkiki değildir; gerektiğinde çocuk alerji polikliniğinde planlanır.",
                    },
                    {
                        "text": "Acil serviste ek laboratuvar veya görüntüleme tetkiki istemeden mevcut öykü ve rinoskopik muayene bulgularıyla klinik tanı koymak",
                        "is_correct": True,
                        "explanation": "Tipik pozisyonel öksürük, burun kaşıntısı, soluk-ödemli nazal konkalar ve normal akciğer oskültasyonu varlığında tanı kliniktir; acil serviste ek tetkik gerekmez.",
                        "new_finding": "Gereksiz radyasyon ve kan tetkikinden kaçınılarak klinik bulgularla tanı ve tedavi planına geçildi.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu hastada mevcut anamnez ve fizik muayene bulgularıyla en doğru klinik tanı nedir?",
                "options": [
                    {
                        "text": "Alerjik Rinit ve Postnazal Akıntı",
                        "is_correct": True,
                        "explanation": "Sabah hapşırıkları, burun kaşıntısı, soluk-mavimsi ödemli konkalar, arka farenkste kaldırım taşı görünümü ve yatınca artan öksürük Alerjik Rinit ve Postnazal Akıntı Sendromunu (Üst Hava Yolu Öksürük Sendromu) doğrular.",
                        "new_finding": "Tanı: Alerjik Rinit ve Postnazal Akıntıya Bağlı Öksürük.",
                    },
                    {
                        "text": "Öksürük Varyant Bronşiyal Astım Tablosu",
                        "is_correct": False,
                        "scenario_update": "Hastanın öksürüğünün kuru/egzersizle tetiklenen karakterde olmadığı, belirgin burun tıkanıklığı ve görünür postnazal mukoid akıntıya sekonder geliştiği değerlendirildi.",
                        "teaching_point": "Öksürük varyant astımda egzersiz, soğuk hava veya gülme ile tetiklenen kuru öksürük ön plandadır; belirgin postnazal sekresyon ve faringeal kaldırım taşı görünümü üst hava yolu kaynağını gösterir.",
                    },
                    {
                        "text": "Akut Bakteriyel Rinosinüzit Enfeksiyonu",
                        "is_correct": False,
                        "scenario_update": "Hastada pürülan sarı-yeşil burun akıntısı, ateş, yüz/diş ağrısı veya 'çift hastalanma' öyküsü bulunmamaktadır.",
                        "teaching_point": "Akut bakteriyel rinosinüzitte 10 günü aşan pürülan nazal akıntı, yüksek ateş (≥39°C) veya başlangıçtaki iyileşmeyi izleyen klinik kötüleşme görülür.",
                    },
                    {
                        "text": "Uzamış Bakteriyel Bronşit Tablosu",
                        "is_correct": False,
                        "scenario_update": "Hastanın öksürüğünün 4 haftayı aşan sürekli balgamlı (ıslak) karakterde olmadığı, gündüzleri olmayıp yalnızca yatınca geniz akıntısıyla tetiklendiği doğrulandı.",
                        "teaching_point": "Uzamış bakteriyel bronşitte >4 hafta süren, pozisyondan bağımsız devamlı ıslak/prodüktif öksürük vardır ve 2 haftalık uygun antibiyoterapiye yanıt verir.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu hastada semptomları kontrol altına almak için en uygun tedavi ve izlem planı hangisidir?",
                "options": [
                    {
                        "text": "İki hafta boyunca günde 3 kez topikal oksimetazolin nazal sprey ve gece öksürüğü için dekstrometorfan şurup reçete ederek taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Beş günden uzun süre topikal oksimetazolin kullanan çocukta şiddetli rebound burun tıkanıklığı (rinitis medikamentoza) gelişti ve öksürük kesilmedi.",
                        "teaching_point": "Topikal alfa-adrenerjik nazal dekongestanlar 3-5 günden uzun kullanıldığında rinitis medikamentozaya yol açar; alerjik rinitin idame tedavisinde yeri yoktur.",
                    },
                    {
                        "text": "İntranazal kortikosteroid sprey, ikinci kuşak oral antihistaminik, serum fizyolojik nazal yıkama ve alerjen önlemleri ile taburcu etmek",
                        "is_correct": True,
                        "explanation": "ARIA kılavuzuna göre orta-ağır veya persistan alerjik rinit ve postnazal akıntıda en etkili tedavi intranazal kortikosteroid sprey (örn. mometazon/flutikazon), nazal serum fizyolojik lavajı ve ikinci kuşak oral H1-antihistaminiktir.",
                        "new_finding": "Doğru intranazal sprey kullanım tekniği (nazal septuma değil lateral duvara/aynı taraf kulak yönüne doğru) uygulamalı gösterilerek ve reçetesi düzenlenerek hasta taburcu edildi.",
                    },
                    {
                        "text": "Geniz akıntısını kurutmak amacıyla 14 gün oral amoksisilin-klavulanat ve birinci kuşak sedatif antihistaminik (klorfeniramin) kombinasyonu başlamak",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik alerjik mukozal ödemi düzeltmedi; birinci kuşak antihistaminik ise gündüz okul başarısını düşüren sedasyon ve sekresyonlarda koyulaşma yaptı.",
                        "teaching_point": "Alerjik rinit ve postnazal akıntıda antibiyotik endikasyonu yoktur; birinci kuşak antihistaminikler antikolinerjik etkileriyle sekresyonu koyulaştırıp sedasyon yaptığı için tercih edilmez.",
                    },
                    {
                        "text": "İntranazal tedavi vermeden doğrudan yüksek doz inhale flutikazon ve gerektiğinde salbutamol inhaler başlayıp üç ay sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Alt hava yoluna yönelik inhaler tedavi burun mukozasındaki alerjik inflamasyonu etkilemediği için hastanın burun tıkanıklığı ve geniz akıntısı devam etti.",
                        "teaching_point": "Astım bulgusu olmayan izole üst hava yolu öksürük sendromunda ağızdan kullanılan bronşiyal inhalerler değil, nazal mukozaya yönelik intranazal kortikosteroid sprey kullanılmalıdır.",
                    },
                ],
            },
        ],
    },
]
