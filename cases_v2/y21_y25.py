# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - Y21-Y25 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "Y21",
        "category": "👶 Ağlayan, Emmeyen, Huzursuz Bebek",
        "age": "18 Aylık",
        "gender": "Erkek",
        "complaint": "Halsizlik, iştahsızlık, solukluk ve yabancı maddeleri yeme isteği",
        "history": (
            "On sekiz aylık erkek çocuğu annesi polikliniğe getiriyor: 'Oğlum son bir aydır eskisi gibi koşup oynamıyor, "
            "çabuk yoruluyor ve sürekli kucak istiyor. İştahı çok azaldı, katı gıdaları neredeyse hiç yemiyor; günde bir "
            "litreden fazla inek sütü biberonla içiyor. Ayrıca son iki haftadır saksıdaki toprağı ve yerdeki kağıt "
            "parçalarını ağzına götürürken yakalıyorum. Ten rengi de sanki giderek beyazlaştı.'"
        ),
        "final_diagnosis": "Aşırı İnek Sütü Tüketimine Bağlı Demir Eksikliği Anemisi",
        "disposition": "Yeşil Alandan Oral Demir Tedavisi, Beslenme Düzenlemesi ve Poliklinik Kontrolü ile Taburculuk",
        "case_pearl": (
            "Süt çocukluğu döneminde günlük 500 mL'nin üzerinde inek sütü tüketimi hem mikrovasküler intestinal kanamaya "
            "yol açarak gizli kan kaybına neden olur hem de biyoyararlanımı düşürerek demir eksikliği anemisi gelişimini "
            "tetikler. Tedavide oral elementer demir 3-6 mg/kg/gün bölünmüş dozda başlanmalı, inek sütü günde 400-500 mL "
            "ile sınırlandırılmalıdır."
        ),
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Halsizlik, iştahsızlık ve pika öyküsüyle getirilen bu çocukta ilk muayene yaklaşımınız hangisi olmalıdır?",
                "options": [
                    {
                        "text": "Hastayı acilen monitörize alana alıp periferik damar yolu açarak hidrasyon ve parenteral beslenme amacıyla hemen Sarı Alana devretmek",
                        "is_correct": False,
                        "scenario_update": "Sarı Alanda hastanın vital bulgularının tamamen stabil olduğu görüldü; damar yolu açılması çocuğu aşırı ajite etti.",
                        "teaching_point": "Genel durumu stabil, dehidratasyon veya dekompansasyon bulgusu olmayan ve aktif kanaması bulunmayan hastalar Yeşil Alanda değerlendirilir.",
                    },
                    {
                        "text": "Vital bulguları ölçmek, konjonktiva ve derideki solukluğu incelemek, kardiyak üfürüm varlığını mezokardiyak odakta dikkatle oskülte etmek",
                        "is_correct": True,
                        "explanation": "Kronik hematolojik yetersizliklerde doku hipoksisine bağlı kompansatuar taşikardi ve hiperdinamik sistolik üfürüm gelişebilir; genel perfüzyon dikkatle incelenmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 36.6°C, KTA 122/dk, SS 24/dk, SpO2 %99, KB 92/58 mmHg. Genel durumu sakin, konjonktivalar ve avuç içleri belirgin soluk. Kalp oskültasyonunda mezokardiyak odakta 2/6 dereceden sistolik üfürüm duyuldu, periferik nabızlar dolgun. Organomegali saptanmadı.",
                    },
                    {
                        "text": "Ağızdan toprak ve kağıt parçaları yeme davranışı nedeniyle genel fizik muayeneyi kısa tutup hastayı doğrudan çocuk psikiyatrisi polikliniğine sevk etmek",
                        "is_correct": False,
                        "scenario_update": "Psikiyatri polikliniğine yönlendirilen ailenin fiziksel muayenesi eksik kaldı ve çocuğun belirgin solukluğu ile üfürümü gözden kaçtı.",
                        "teaching_point": "Küçük çocuklarda yabancı cisim yeme (pika) davranışı öncelikle nutrisyonel eksikliklerin organik bir belirtisi olarak araştırılmalıdır.",
                    },
                    {
                        "text": "Aşırı süt alımı öyküsü nedeniyle batın muayenesine yoğunlaşıp karın ağrısı veya akut batın bulgularını ekarte etmeyi öncelikli hedef seçmek",
                        "is_correct": False,
                        "scenario_update": "Batın muayenesinde defans veya hassasiyet saptanmadı; ancak hastanın genel halsizliği ve mukozal solukluğu sistematik olarak değerlendirilmemiş oldu.",
                        "teaching_point": "Aşırı inek sütü tüketimi tek başına akut batın tablosuna yol açmaz; solukluk ve kardiyovasküler kompansasyon bulguları öncelikle taranmalıdır.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Yaklaşım Kararı",
                "question": "Fizik muayenesinde belirgin solukluk ve sistolik üfürüm saptanan bu çocukta ilk basamakta hangi tetkik istenmelidir?",
                "options": [
                    {
                        "text": "Pika semptomu ve derin halsizlik nedeniyle ilk basamakta doğrudan kemik iliği aspirasyonu ve kapsamlı genetik enzim paneli tetkiki planlamak",
                        "is_correct": False,
                        "scenario_update": "Gereksiz invaziv işlem önerisi aileyi paniğe sevk etti ve poliklinik şartlarında gereksiz ileri tetkik maliyeti oluştu.",
                        "teaching_point": "Nutrisyonel kaynaklı şüpheli tablolarda ilk basamakta invaziv tetkikler yerine tam kan sayımı ve eritrosit indeksleri yeterlidir.",
                    },
                    {
                        "text": "Oskültasyonda sistolik ejeksiyon üfürümü duyulduğu için elektrokardiyografi çekip ileri kardiyak değerlendirme ve ekokardiyografi incelemesi amacıyla hastayı çocuk kardiyolojisine sevk etmek",
                        "is_correct": False,
                        "scenario_update": "EKG normal sinüs ritmi ve taşikardi gösterdi; kardiyoloji konsültasyonunda üfürümün hiperdinamik akıma bağlı masum üfürüm olduğu belirtildi.",
                        "teaching_point": "Belirgin solukluğu olan çocuklarda duyulan sistolik fonksiyonel üfürümlerde ilk aşama kardiyak görüntüleme değil hematolojik değerlendirmedir.",
                    },
                    {
                        "text": "Eritrosit indeksleri, hemoglobin, hematokrit ve eritrosit dağılım genişliğini içeren tam kan sayımı ile periferik yayma tetkiki istemek",
                        "is_correct": True,
                        "explanation": "Hemoglobin düzeyi, ortalama eritrosit hacmi (MCV) ve eritrosit dağılım genişliği (RDW) tablonun ağırlığını ve morfolojisini ortaya koyar.",
                        "new_finding": "Laboratuvar Bulguları: Hemoglobin 7.1 g/dL, Hematokrit %22.4, MCV 58 fL (düşük), MCH 19 pg, RDW %19.8 (belirgin yüksek), WBC 8.400/mm³, Trombosit 460.000/mm³. Periferik yaymada eritrositlerde belirgin hipokromi, anizositoz ve poikilositoz izlendi.",
                    },
                    {
                        "text": "Toprak yeme öyküsü olduğundan kurşun maruziyetini araştırmak üzere ayakta direkt batın grafisi çekilmesini ve tam idrar tahlili yapılmasını istemek",
                        "is_correct": False,
                        "scenario_update": "Batın grafisinde radyoopak yabancı cisim görülmedi ve idrar tetkiki doğal çıktı; ancak solukluğun derecesi aydınlatılamadı.",
                        "teaching_point": "Pika öyküsünde kurşun maruziyeti bir komplikasyon olabilse de hastanın belirgin solukluğu öncelikle tam kan sayımıyla değerlendirilir.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Öykü, fizik muayene ve laboratuvar bulguları bir arada değerlendirildiğinde en olası klinik tanınız nedir?",
                "options": [
                    {
                        "text": "Talasemi Minör (Akdeniz Kansızlığı Taşıyıcılığı)",
                        "is_correct": False,
                        "scenario_update": "Talasemi taşıyıcılığında genellikle RDW normaldir ve Mentzer indeksi 13'ün altındadır; hastamızda ise RDW yüksek ve Mentzer indeksi 15.8 hesaplandı.",
                        "teaching_point": "Talasemi minörde eritrosit sayısı yüksek, RDW normal veya hafif yüksek ve Mentzer indeksi (MCV/RBC) < 13 iken, demir eksikliğinde RDW belirgin yüksektir ve Mentzer > 13 saptanır.",
                    },
                    {
                        "text": "Demir Eksikliği Anemisi",
                        "is_correct": True,
                        "explanation": "Aşırı inek sütü tüketimi, pika, düşük MCV, yüksek RDW ve reaktif trombositoz demir eksikliği anemisini güçlü şekilde destekler.",
                        "new_finding": "Tanı Demir Eksikliği Anemisi olarak teyit edildi; eşzamanlı bakılan serum ferritin düzeyi 4 ng/mL (çok düşük) olarak sonuçlandı.",
                    },
                    {
                        "text": "Kronik Hastalık Anemisi",
                        "is_correct": False,
                        "scenario_update": "Hastanın öyküsünde kronik inflamatuar, romatizmal veya enfeksiyöz bir hastalık bulunmamaktadır; ferritin düzeyi düşük beklenir.",
                        "teaching_point": "Kronik hastalık anemisinde ferritin normal veya yüksektir ve demir bağlama kapasitesi azalmıştır; hastanın öyküsü besinsel eksiklikle uyumludur.",
                    },
                    {
                        "text": "Kurşun Zehirlenmesine Bağlı Sideroblastik Anemi",
                        "is_correct": False,
                        "scenario_update": "Periferik yaymada bazofilik noktalanma izlenmedi ve hastanın tablosunu açıklayan birincil neden nutrisyonel yetersizliktir.",
                        "teaching_point": "Pikaya sekonder kurşun maruziyeti gelişebilse de süt çocukluğunda mikrositer hipokrom aneminin ezici çoğunluğu nutrisyonel demir eksikliğidir.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Yönetim",
                "question": "Demir eksikliği anemisi tanısı kesinleşen bu hastada en uygun tedavi ve beslenme planı hangisidir?",
                "options": [
                    {
                        "text": "Hemoglobin değeri sekiz gramın altında saptandığı için acil serviste eritrosit süspansiyonu transfüzyonu uygulayarak hastayı çocuk hematoloji servisine yatırmak",
                        "is_correct": False,
                        "scenario_update": "Kalp yetmezliği veya dekompansasyon bulgusu olmayan stabil kronik anemide acil transfüzyon volüm yüklenmesi riski oluşturdu.",
                        "teaching_point": "Kronik demir eksikliği anemisinde hemodinami stabilse hemoglobin 7 g/dL altında olsa dahi öncelikle oral tedavi tercih edilir.",
                    },
                    {
                        "text": "Oral emilimin yetersiz kalacağı gerekçesiyle acil serviste tek doz yüksek doz intravenöz demir infüzyonu planlayarak hastayı gözleme almak",
                        "is_correct": False,
                        "scenario_update": "İntravenöz demir infüzyonu sonrası çocukta alerjik reaksiyon gelişti; gereksiz yere invaziv ve maliyetli bir yol seçildi.",
                        "teaching_point": "Oral tedaviyi tolere edebilen ve malabsorbsiyonu olmayan süt çocuklarında parenteral demir ilk seçenek değildir.",
                    },
                    {
                        "text": "Diyet kısıtlaması yapmadan sadece profilaktik dozda günde bir miligram bölü kilogram oral demir damlası başlayarak hastayı kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Aşırı süt alımı devam ettiği ve doz yetersiz kaldığı için birinci aydaki kontrolde hemoglobin yükselmedi.",
                        "teaching_point": "Tedavi edici doz 3-6 mg/kg/gün elementer demirdir ve inek sütü tüketimi mutlaka günlük 500 mL'nin altına indirilmelidir.",
                    },
                    {
                        "text": "Günlük 3-6 mg/kg elementer demir başlamak, inek sütünü kısıtlamak ve ilacı C vitaminiyle aç karnına vermek",
                        "is_correct": True,
                        "explanation": "Tedavi dozu 3-6 mg/kg/gün elementer demirdir; C vitamini emilimi artırırken kalsiyum emilimi azaltır, inek sütü günlük 500 mL altında tutulmalıdır.",
                        "new_finding": "Oral demir tedavisi başlandı. Aileye ilacın dişlerde geçici boyanma yapabileceği, gaitayı siyaha boyayacağı anlatıldı ve 1 ay sonraya kontrol planlandı.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y22",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "6 Yaş",
        "gender": "Kız",
        "complaint": "Ağız içinde şiddetli ağrı, yemek yiyememe ve dudakta yaralar",
        "history": (
            "Altı yaşındaki kız çocuğu annesi tarafından ağız içi yaralar nedeniyle getiriliyor: 'Kızım üç gündür bir şeyler "
            "çiğnerken ve su içerken ağzının çok acıdığını söylüyor, katı hiçbir şey yemedi. Dudağının içinde ve yanağında "
            "beyaz renkli küçük yaralar fark ettik. Ateşi hiç olmadı. Ellerinde veya ayaklarında herhangi bir döküntü yok. "
            "Geçen yıl da benzer şekilde dudağında tek bir yara çıkmış ve yaklaşık on günde kendiliğinden geçmişti.'"
        ),
        "final_diagnosis": "Rekürren Aftöz Stomatit (Minör Aft)",
        "disposition": "Yeşil Alandan Topikal Tedavi, Oral Hijyen ve Diyet Önerileri ile Taburculuk",
        "case_pearl": (
            "Rekürren aftöz stomatitte lezyonlar keratinize olmayan mukozada (bukkal mukoza, dudak iç yüzü, dil altı) "
            "yerleşir; etrafı eritemli bir hale ile çevrili, ortası sarı-gri psödomembranla kaplı ağrılı oval ülserlerdir. "
            "Diş etleri ve sert damak tutulmaz; ateş ve sistemik bulgu eşlik etmez. Viral enfeksiyonlardan (herpetik "
            "gingivostomatit, el-ayak-ağız) bu klinik özelliklerle ayrılır; antibiyotik veya sistemik antiviral gerekmez."
        ),
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Ağız içinde ağrılı lezyonlar nedeniyle getirilen bu hastada ilk fizik muayene yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Vital bulguları almak, ağız mukozası, diş etleri ile el, ayak ve perineal bölgeleri dikkatle muayene etmek",
                        "is_correct": True,
                        "explanation": "Lezyonların yerleşimi (keratinize vs non-keratinize mukoza) ve ekstraoral döküntülerin taranması ayırıcı tanıda kilit role sahiptir.",
                        "new_finding": "Vital Bulgular: Ateş 36.7°C, KTA 88/dk, SS 20/dk, SpO2 %100. Fizik Muayene: Alt dudak mukozasında 4 mm ve sağ bukkal mukozada 5 mm çapında, ortası sarı-gri tabanlı, çevresi parlak eritemli hale ile çevrili 2 adet yuvarlak ülseratif lezyon izlendi. Diş etleri, dil sırtı ve sert damak tamamen doğal; ödem ve kanama yok. El ayası, ayak tabanı ve perianal bölgede döküntü saptanmadı. Servikal lenfadenopati yok.",
                    },
                    {
                        "text": "Ülser tabanından steril eküvyonla sürüntü alarak hızlı antijen testi ve mikrobiyolojik boğaz kültürü analizi için acilen laboratuvara göndermek",
                        "is_correct": False,
                        "scenario_update": "Lezyon tabanından sürüntü alınması çocuğa şiddetli ağrı verdi ve ağlamasına yol açtı; sürüntüde bakteriyel üreme saptanmadı.",
                        "teaching_point": "Tipik non-keratinize mukozal ülserlerde rutin bakteriyel kültür endike değildir ve invaziv sürüntü gereksiz acı verir.",
                    },
                    {
                        "text": "Beslenme azlığı öyküsü nedeniyle dehidratasyon gelişebileceğini öngörüp periferik damar yolu açarak rutin kan şekeri ve elektrolit paneli göndermek",
                        "is_correct": False,
                        "scenario_update": "Damar yolu açılması hastanın anksiyetesini artırdı; bakılan elektrolitler ve kan şekeri tamamen normal sınırlarda geldi.",
                        "teaching_point": "Mukozaları nemli, turgoru doğal ve idrar çıkışı yeterli olan çocuklarda invaziv damar yolu ve lab tetkiki gereksizdir.",
                    },
                    {
                        "text": "Ağız içi yaygın enfeksiyon kuşkusuyla hastayı derhal izole edip acil diş hekimliği konsültasyonu ve tedavi amacıyla Sarı Alana devretmek",
                        "is_correct": False,
                        "scenario_update": "Sarı Alanda hastanın genel durumunun stabil olduğu ve acil invaziv müdahale gereksinimi bulunmadığı teyit edildi.",
                        "teaching_point": "Ateşi olmayan, vital bulguları stabil ve hava yolu tehdidi bulunmayan oral lezyonlu hastalar Yeşil Alanda yönetilebilir.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Yaklaşım Kararı",
                "question": "Fizik muayenesinde dudak içi ve yanakta lokalize ülserleri olan, ateşi bulunmayan çocukta tetkik stratejiniz ne olmalıdır?",
                "options": [
                    {
                        "text": "Herpes simpleks virüs enfeksiyonunu dışlamak amacıyla lezyon tabanından Tzanck yayması ve viral polimeraz zincir reaksiyonu tetkikini birlikte istemek",
                        "is_correct": False,
                        "scenario_update": "Tzanck yaymasında multinükleer dev hücreler izlenmedi; viral tetkikler negatif sonuçlandı ve ek klinik katkı sağlamadı.",
                        "teaching_point": "Herpetik lezyonlar genellikle keratinize mukozayı (diş eti, sert damak) tutar ve vezikülle başlar; non-keratinize mukoza ülserlerinde rutin önerilmez.",
                    },
                    {
                        "text": "Tekrarlayan ağız lezyonları öyküsü nedeniyle Behçet hastalığı ve otoimmünite yönünden tam kan, CRP, ANA ve HLA-B51 tetkiklerini göndermek",
                        "is_correct": False,
                        "scenario_update": "İstenen romatolojik ve genetik testlerin sonuçlanmasının haftalar süreceği belirtildi; akut faz reaktanları tamamen negatif çıktı.",
                        "teaching_point": "Yılda bir iki kez çıkan, genital ülser veya üveitin eşlik etmediği izole tablolarda ilk başvuruda romatolojik panel istenmez.",
                    },
                    {
                        "text": "Altta yatan inflamatuar bağırsak hastalığını ekarte etmek için fekal kalprotektin düzeyi bakılmasını ve acil gastroenteroloji konsültasyonu talep etmek",
                        "is_correct": False,
                        "scenario_update": "Gastroenteroloji konsültan hekimi hastada kilo kaybı, kronik ishal veya rektal kanama olmadığı için endoskopi endikasyonu görmedi.",
                        "teaching_point": "Gastrointestinal semptomların, büyüme geriliğinin veya anemi bulgularının eşlik etmediği durumlarda ileri tetkik gerekmez.",
                    },
                    {
                        "text": "Klinik tablo ve lezyonlar tipik olduğundan laboratuvar tetkiki istemeden semptomları rahatlatmaya ve oral alımı desteklemeye odaklanmak",
                        "is_correct": True,
                        "explanation": "Ateşsiz, izole ve karakteristik lezyonlarda tanı tamamen klinik konur; gereksiz tetkik ve girişimlerden kaçınılmalıdır.",
                        "new_finding": "Ek laboratuvar tetkiki istenmedi. Hastanın klinik muayene bulgularıyla tanısal değerlendirmeye geçildi.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Öykü ve fizik muayene bulguları dikkate alındığında bu hastada en olası klinik tanı hangisidir?",
                "options": [
                    {
                        "text": "Primer Herpetik Gingivostomatit",
                        "is_correct": False,
                        "scenario_update": "Herpetik gingivostomatitte yüksek ateş, yaygın diş eti hipertrofisi, kanaması ve perioral veziküller beklenir; bu hastada diş etleri doğaldır.",
                        "teaching_point": "Herpetik gingivostomatit belirgin ateş, servikal lenfadenopati ve keratinize mukoza (gingiva) tutulumu ile seyreder.",
                    },
                    {
                        "text": "El-Ayak-Ağız Hastalığı",
                        "is_correct": False,
                        "scenario_update": "Hastanın el ayalarında, ayak tabanlarında veya kalçasında döküntü yoktur ve lezyonlar daha çok arka farenksten ziyade ön ağızdadır.",
                        "teaching_point": "El-ayak-ağız hastalığında el ve ayaklarda papüloveziküler döküntüler ile farenks/damakta enantemler görülür.",
                    },
                    {
                        "text": "Rekürren Aftöz Stomatit",
                        "is_correct": True,
                        "explanation": "Non-keratinize mukoza tutulumu, sarı-gri psödomembranlı ağrılı ülserler, eritemli çevre ve ateşsiz seyir aftöz stomatit ile uyumludur.",
                        "new_finding": "Klinik tanı Rekürren Aftöz Stomatit (Minör Aft) olarak belirlendi.",
                    },
                    {
                        "text": "Oral Mukozal Kandidiyazis (Pamukçuk)",
                        "is_correct": False,
                        "scenario_update": "Oral kandidiyaziste mukozaya yapışık, kaldırılınca kanayan beyaz peynirimsi plaklar görülür; sınırları belirgin ülserler oluşmaz.",
                        "teaching_point": "Pamukçuk lezyonları eritemli tabanlı beyaz plaklar şeklindedir, tipik ağrılı çukurlaşmış ülser morfolojisinde değildir.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Yönetim",
                "question": "Rekürren aftöz stomatit tanısı konulan bu hastada en uygun tedavi ve taburculuk planı hangisidir?",
                "options": [
                    {
                        "text": "Topikal bariyer veya analjezik jel uygulamak, ılık yumuşak gıdalar önermek ve hidrasyonu yakından takip etmek",
                        "is_correct": True,
                        "explanation": "Tedavide amaç ağrıyı hafifletmek ve hidrasyonu korumaktır; topikal hyaluronik asit/mukoprotektif jeller ve oral hijyen yeterlidir.",
                        "new_finding": "Aileye topikal mukoza koruyucu jel tarifi yapıldı. Asitli, tuzlu ve sert gıdalardan kaçınmaları, hidrasyonu sürdürmeleri anlatıldı.",
                    },
                    {
                        "text": "Lezyonların hızla gerilemesi amacıyla yedi gün süreli oral asiklovir süspansiyon ve sistemik antibiyotik tedavisi reçete ederek taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Viral veya bakteriyel etken olmadığı için antiviral ve antibiyotik tedavisi klinik gidişatı değiştirmedi ve yan etki riski oluşturdu.",
                        "teaching_point": "Aftöz lezyonlarda herpes virüsü veya bakteriler rol oynamaz; asiklovir veya antibiyotik kullanımı tamamen gereksizdir.",
                    },
                    {
                        "text": "Ülserlerin yayılmasını önlemek amacıyla yüksek doz oral prednizolon tedavisi başlayarak hastayı acil serviste yakın gözlem yatağına yatırmak",
                        "is_correct": False,
                        "scenario_update": "Hafif minör lezyonlarda sistemik kortikosteroid başlanması hiperglisemi, immünsüpresyon ve huzursuzluk gibi yan etkilere yol açtı.",
                        "teaching_point": "Sistemik steroidler yalnızca çok şiddetli, majör ve tedaviye dirençli vakalarda uzman kontrolünde düşünülür; minör lezyonlarda yeri yoktur.",
                    },
                    {
                        "text": "Ağrıyı derhal kesmek için poliklinikte lezyon tabanını gümüş nitrat çubuğuyla koterize edip derin kimyasal koterizasyon pansumanı uygulamak",
                        "is_correct": False,
                        "scenario_update": "Gümüş nitrat uygulaması çocukta dayanılmaz bir yanma ağrısına yol açtı ve çevre dokuda kimyasal hasar oluşturdu.",
                        "teaching_point": "Küçük çocuklarda kimyasal koterizasyon ağrılıdır, çevre mukozaya zarar verebilir ve doku iyileşmesini geciktirebilir.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y23",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "9 Yaş",
        "gender": "Erkek",
        "complaint": "Gövdede kaşıntılı döküntüler ve göğüste daha önce çıkan büyük leke",
        "history": (
            "Dokuz yaşındaki erkek çocuk annesiyle birlikte polikliniğe başvuruyor: 'Doktor bey/hanım, yaklaşık on gün önce "
            "oğlumun göğsünün üst kısmında madeni para büyüklüğünde, kenarları hafif kabuklu pembe bir leke fark ettik. Başta "
            "mantar sandık ve nemlendirici sürdük ama geçmedi. Son üç dört gündür ise sırtında, karnında ve göğsünde aynı "
            "lekenin daha küçükleri hızla çoğaldı. Hafif kaşıntısı var ama ateşi, boğaz ağrısı veya halsizliği hiç olmadı.'"
        ),
        "final_diagnosis": "Pitriyazis Rozea",
        "disposition": "Yeşil Alandan Bilgilendirme, Güvence Verme, Semptomatik Kaşıntı Tedavisi ile Taburculuk",
        "case_pearl": (
            "Pitriyazis rozea tipik olarak gövdede tek, 2-5 cm çapında, kenarları kalkık ve hafif skuamlı öncü plakla "
            "(herald patch / madalyon plak) başlar; 1-2 hafta sonra gövdede Langer çizgilerine paralel, 'çam ağacı' dağılımı "
            "gösteren daha küçük oval eritematöz skuamlı papül ve plaklar belirir. Kendi kendini 6-8 haftada sınırlayan selim "
            "bir ekzantemdir; gereksiz antifungal veya antibiyotik verilmemeli, aileye bulaşıcı olmadığı anlatılarak güvence verilmelidir."
        ),
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Gövdede yaygın döküntü şikayetiyle getirilen bu okul çağı çocuğunda ilk klinik muayene yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Malign deri lezyonlarını ekarte etmek amacıyla döküntülerin dermatoskopik incelemesini yapıp acilen cerrahi eksizyonel deri biyopsisi işlemi planlamak",
                        "is_correct": False,
                        "scenario_update": "İnvaziv biyopsi önerisi aileyi derin bir endişeye sevk etti; selim bir ekzantem için gereksiz doku hasarı riski doğdu.",
                        "teaching_point": "Simetrik, yüzeyel ve tipik seyirli döküntülerde invaziv deri biyopsisi endike değildir; klinik muayene yeterlidir.",
                    },
                    {
                        "text": "Tüm vücut cildini tamamen soyup döküntülerin morfolojisini, gövdedeki dizilim paternini, avuç içlerini ve mukozaları dikkatlice incelemek",
                        "is_correct": True,
                        "explanation": "Döküntünün dağılım paterni (Langer çizgilerine paralellik), skuam özelliği ve mukoza/avuç içi tutulumunun olmaması kritik ipuçları sağlar.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 82/dk, SS 18/dk, SpO2 %99. Cilt Muayenesi: Sternum üzerinde 3.5 cm çapında, hafif kabarık eritematöz kenarlı, iç kenarında yakalık tarzında ince deskuamasyon bulunan oval bir plak saptandı. Sırt ve gövde ön yüzünde kaburga çizgilerine paralel 'çam ağacı' diziliminde 0.5-1.5 cm boyutlarında benzer morfolojide çok sayıda oval eritematöz skuamlı lezyon izlendi. Avuç içleri, ayak tabanları ve oral mukoza tamamen temiz. Lenfadenopati yok.",
                    },
                    {
                        "text": "Vaskülit veya meningokoksemi kuşkusuyla hastayı izole edip acil damar yolu açılması ve monitörizasyon amacıyla Sarı Alana devretmek",
                        "is_correct": False,
                        "scenario_update": "Sarı Alanda hastanın genel durumunun iyi, döküntülerin peteşi-purpura değil eritematöz skuamlı olduğu ve vitallerin stabil olduğu görüldü.",
                        "teaching_point": "Basmakla solan, skuamlı ve genel durumu mükemmel olan hastalar vaskülit veya meningokoksemi lehine değildir; Yeşil Alanda incelenir.",
                    },
                    {
                        "text": "Çocuğu tamamen soymadan sadece göğsündeki ilk lezyonu muayene edip alerjik reaksiyon düşünerek oral antihistaminik şurup verip taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Sırt ve diğer gövde alanları incelenmediği için döküntünün karakteristik dermatom benzeri dağılım paterni gözden kaçırıldı.",
                        "teaching_point": "Döküntülü çocuklarda tüm vücut derisi mutlaka tamamen açılarak incelenmeli ve lezyonların yayılım paterni haritalandırılmalıdır.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Yaklaşım Kararı",
                "question": "Gövdede kaburga çizgilerine paralel dağılım gösteren oval skuamlı döküntüleri olan bu hastada tetkik kararınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Mantar enfeksiyonunu kesin olarak dışlamak amacıyla tüm lezyonlardan bistüriyle derin kazıntı alarak potasyum hidroksit mikroskopisi tetkiki istemek",
                        "is_correct": False,
                        "scenario_update": "Çok sayıda lezyondan yapılan ağrılı kazıntıda mikroskopide mantar hifleri veya sporları görülmedi; lezyonlar irrite oldu.",
                        "teaching_point": "Tinea korporiste lezyon genellikle tek veya birkaç adettir; tüm gövdeye paralel dağılan döküntülerde yaygın kazıntı gerekmez.",
                    },
                    {
                        "text": "Alerji ve post-streptokokal reaksiyonları araştırmak amacıyla periferik tam kan sayımı, total IgE, CRP ve ASO düzeylerini birlikte göndermek",
                        "is_correct": False,
                        "scenario_update": "Kan tahlili sonuçları tamamen normal geldi; damar yolu açılması çocuğun korkmasına ve acilde beklemesine neden oldu.",
                        "teaching_point": "Klinik görünümü tipik olan, ateş ve sistemik bulgunun eşlik etmediği tablolarda kan tetkiklerinin tanısal değeri yoktur.",
                    },
                    {
                        "text": "Klinik tablo ve döküntü paterni tanısal olduğundan hastadan herhangi bir invaziv laboratuvar veya görüntüleme tetkiki istememek",
                        "is_correct": True,
                        "explanation": "Karakteristik öncü lezyon ve gövdedeki dağılım paterni klinik tanı için yeterlidir; rutin laboratuvar tetkiki endike değildir.",
                        "new_finding": "Tetkik istenmedi; lezyonların klinik özellikleri üzerinden tanı ve hasta eğitimi aşamasına geçildi.",
                    },
                    {
                        "text": "Viral döküntü etkenlerini aydınlatmak için kanda Epstein-Barr virüsü, sitomegalovirüs ve parvovirüs serolojilerinden oluşan genişletilmiş antikor panelini istemek",
                        "is_correct": False,
                        "scenario_update": "Seroloji sonuçlarının çıkmasının günler alacağı öğrenildi; hastanın klinik yaklaşımında ve tedavisinde hiçbir değişiklik sağlamadı.",
                        "teaching_point": "Selim seyirli yüzeyel ekzantemlerde genişletilmiş viral antikor panelleri rutin pratikte maliyet-etkin değildir ve önerilmez.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Öykü ve döküntü morfolojisi birlikte değerlendirildiğinde hastadaki en olası klinik tanı hangisidir?",
                "options": [
                    {
                        "text": "Tinea Korporis (Gövde Mantarı)",
                        "is_correct": False,
                        "scenario_update": "Tinea korporiste genellikle tek veya az sayıda, santralden iyileşme gösteren anüler plaklar görülür; tüm sırtta çam ağacı dağılımı beklenmez.",
                        "teaching_point": "Tinea korporis asimetrik ve sınırlı sayıda lezyonla gider; bu hastadaki gibi öncü plak sonrası bilateral simetrik dissemine yayılım göstermez.",
                    },
                    {
                        "text": "Guttat Psöriyazis (Damla Sedef)",
                        "is_correct": False,
                        "scenario_update": "Guttat psöriyaziste genellikle streptokokal farenjitten 1-2 hafta sonra kalın gümüşi skuamlı küçük damla şeklinde lezyonlar çıkar; öncü madalyon plak olmaz.",
                        "teaching_point": "Guttat psöriyazis kalın sedef rengi skuamlarla kaplıdır ve öncü bir büyük plak öyküsü bulunmaz.",
                    },
                    {
                        "text": "Sekonder Sifiliz Ekzantemi",
                        "is_correct": False,
                        "scenario_update": "Sekonder sifilizde döküntüler avuç içi ve ayak tabanlarını belirgin tutar, lenfadenopati eşlik eder ve öncü plak görülmez.",
                        "teaching_point": "Sekonder sifiliz palmar ve plantar tutulumun yanı sıra generalized lenfadenopati ile seyreder.",
                    },
                    {
                        "text": "Pitriyazis Rozea",
                        "is_correct": True,
                        "explanation": "Öncü plak (herald patch), bunu izleyen çam ağacı dağılımlı yakalık tarzı skuamlı oval lezyonlar pitriyazis rozea için tipiktir.",
                        "new_finding": "Klinik tanı Pitriyazis Rozea olarak kesinleştirildi.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Yönetim",
                "question": "Pitriyazis rozea tanısı kesinleşen bu hastanın tedavisinde ve aile bilgilendirmesinde en uygun yaklaşım hangisidir?",
                "options": [
                    {
                        "text": "Döküntülerin yayılmasını durdurmak amacıyla dört hafta süreli oral terbinafin veya flukonazol antifungal tablet tedavisi reçete ederek taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Antifungal tedavi mantar kaynaklı olmayan bu tabloda etkisiz kaldı ve gereksiz hepatotoksisite takip ihtiyacı doğurdu.",
                        "teaching_point": "Pitriyazis rozea fungal bir enfeksiyon değildir; sistemik veya topikal antifungallerin tedavide yeri yoktur.",
                    },
                    {
                        "text": "Hastalığın kendiliğinden iyileşeceğini belirtmek, bulaşıcı olmadığını anlatıp kaşıntı varsa semptomatik antihistaminik veya nemlendirici losyon önermek",
                        "is_correct": True,
                        "explanation": "Hastalık kendi kendini sınırlayan selim bir tablodur; temel yaklaşım aileye güvence vermek ve varsa semptomatik kaşıntıyı rahatlatmaktır.",
                        "new_finding": "Aileye hastalığın iz bırakmadan 1-2 ay içinde kendiliğinden geçeceği anlatıldı. Sıcak banyodan kaçınmaları ve hafif kaşıntı için nemlendirici kullanmaları önerildi.",
                    },
                    {
                        "text": "Hastalığı bulaşıcı kabul ederek çocuğu üç hafta okuldan izole etmek ve taburculukta yüksek doz sistemik kortikosteroid başlamak",
                        "is_correct": False,
                        "scenario_update": "Okuldan gereksiz yere uzaklaştırılan çocuğun eğitim hayatı aksadı ve sistemik steroid yan etkileri ortaya çıktı.",
                        "teaching_point": "Pitriyazis rozea bulaşıcı değildir, okula devamı kısıtlanmaz ve rutin sistemik kortikosteroid endikasyonu yoktur.",
                    },
                    {
                        "text": "Lezyonların derhal solması için hastayı acil serviste ultraviyole fototerapi seansına almak ve yüksek doz intravenöz antiviral infüzyonu uygulamak",
                        "is_correct": False,
                        "scenario_update": "Hastanede yatış ve fototerapi gereksiz maliyet ve anksiyete yarattı; selim tablonun seyrinde dramatik fark oluşmadı.",
                        "teaching_point": "Hafif ve orta seyirli pitriyazis rozeada acil fototerapi veya antiviral infüzyon endikasyonu bulunmamaktadır.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y24",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "4 Yaş",
        "gender": "Kız",
        "complaint": "Koltuk altında ve gövdede inci tanesi gibi parlak pütürler çıkması",
        "history": (
            "Dört yaşındaki kız çocuğu annesi tarafından cildindeki pütürler nedeniyle getiriliyor: 'Kızımın yaklaşık bir ay "
            "önce sağ koltuk altında bir iki tane sivilce benzeri kabarcık çıkmıştı. Zamanla bunların sayısı arttı, göğsüne "
            "ve karnına da yayıldı. Kabarcıklar sert, inci gibi parlıyor ve ortalarında minik bir çukurluk var. Herhangi bir "
            "ağrısı veya ateşi yok, bazen hafif kaşıyor. Kreşe gidiyor ve havuz kursuna katılıyordu.'"
        ),
        "final_diagnosis": "Molluskum Kontagiozum",
        "disposition": "Yeşil Alandan Aile Eğitimi, Otomanipülasyondan Kaçınma ve İzlem Planı ile Taburculuk",
        "case_pearl": (
            "Molluskum kontagiozum, poxvirüs ailesinden Molluscum contagiosum virüsünün neden olduğu, çocuklarda sık görülen "
            "selim bir kutanöz enfeksiyondur. Karakteristik lezyonlar 2-5 mm çapında, kubbe şeklinde, ortası göbekli "
            "(umbilike), inci benzeri parlak papüllerdir. Havuz, doğrudan temas veya havlu paylaşımıyla bulaşır. Çoğu lezyon "
            "6-18 ay içinde nedbesiz kendiliğinden geriler. Sıkma, kaşıma ve cerrahi küretaj otokoinokülasyona ve skar "
            "gelişimine yol açabileceğinden öncelikle konservatif izlem ve aile eğitimi önerilir."
        ),
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Gövdede parlak kabarcıklar tariflenen bu çocuğun ilk değerlendirmesinde en uygun klinik muayene yaklaşımı hangisidir?",
                "options": [
                    {
                        "text": "Tanıyı doğrulamak amacıyla lezyonlardan birini forsepsle sıkarak içindeki kazeöz materyali aspire edip acil serviste mikroskop altında incelemeyi seçmek",
                        "is_correct": False,
                        "scenario_update": "Lezyonun sıkılması şiddetli ağrıya, kanamaya ve virüsün çevre deriye yayılmasına zemin hazırladı.",
                        "teaching_point": "Klinik muayenede tipik kubbe şeklindeki papüller sıkılmamalı veya koparılmamalıdır; bu durum otokoinokülasyona ve skara yol açar.",
                    },
                    {
                        "text": "Suçiçeği veya dissemine enfeksiyon kuşkusuyla çocuğu negatif basınçlı odaya alıp damar yolu ve izolasyon amacıyla Sarı Alana devretmek",
                        "is_correct": False,
                        "scenario_update": "Sarı Alanda hastanın ateşi olmadığı, genel durumunun tamamen stabil olduğu ve lezyonların vezikül değil papül olduğu belirlendi.",
                        "teaching_point": "Sistemik toksisite bulgusu, ateşi veya akut veziküler döküntüsü olmayan stabil deri döküntüleri Yeşil Alanda değerlendirilir.",
                    },
                    {
                        "text": "Vital bulguları almak, lezyonların morfolojisini, santral umbilikasyonunu, anatomik dağılımını ve sekonder enfeksiyon varlığını dikkatle muayene etmek",
                        "is_correct": True,
                        "explanation": "Kubbe şeklindeki papüllerin santral umbilikasyonu ve parlak inci görünümü ile çevre derideki egzama veya süperenfeksiyon incelenmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 36.6°C, KTA 94/dk, SS 22/dk, SpO2 %100. Cilt Muayenesi: Sağ aksiller bölgede, göğüs yan duvarında ve karında 2-4 mm boyutlarında, pembe-ten rengi, kubbe şeklinde, ortasında belirgin göbek benzeri çukurluk (santral umbilikasyon) bulunan yaklaşık 15 adet parlak papül izlendi. Lezyonların çevresinde eritem, ısı artışı veya pürülan akıntı yok. Diğer sistem muayeneleri doğal.",
                    },
                    {
                        "text": "Cinsel istismar kuşkusu nedeniyle ayrıntılı adli tıp protokolü başlatıp hastayı genel muayene yapmadan doğrudan çocuk izlem merkezine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Adli süreç başlatılması ailede büyük bir şok yarattı; aksiller ve gövdedeki lezyonların çocukluk çağında temasla geçtiği sonradan anlaşıldı.",
                        "teaching_point": "Aksilla ve gövde yerleşimi çocukluk çağında havuz veya oyun temasıyla sık görülen tipik bir kutanöz yayılımdır; izole adli şüphe doğurmaz.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Yaklaşım Kararı",
                "question": "Fizik muayenesinde gövdede ortası göbekli parlak papülleri saptanan bu çocukta tetkik yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Karakteristik klinik bulgular tanı koydurucu olduğundan hastadan herhangi bir invaziv girişim veya laboratuvar tetkiki istememek",
                        "is_correct": True,
                        "explanation": "Ortası göbekli inci gibi kubbe papüller tanı için patognomoniktir; laboratuvar veya biyopsi gerekmez.",
                        "new_finding": "Tetkik istenmedi; lezyonların klinik morfolojisinin tanı için tam yeterlilikte olduğu teyit edildi.",
                    },
                    {
                        "text": "Histopatolojik inceleme için genel anestezi altında lezyonlardan çok odaklı cerrahi punch deri biyopsisi alınmasını planlayıp hastaya gün vermek",
                        "is_correct": False,
                        "scenario_update": "Deri biyopsisi önerisi çocuğu çok korkuttu ve küçük çocukta genel anestezi riski gereksiz yere gündeme geldi.",
                        "teaching_point": "Tipik klinik görünüme sahip benign papüler lezyonlarda tanı klinik olarak konur; cerrahi deri biyopsisi endike değildir.",
                    },
                    {
                        "text": "Altta yatan hücresel immün yetmezlik olasılığını dışlamak amacıyla lenfosit alt grupları ve serum immünglobulin düzeylerini tetkik olarak göndermek",
                        "is_correct": False,
                        "scenario_update": "Gönderilen immünolojik paneller tamamen normal çıktı; poliklinik bekleme süresi uzadı ve gereksiz maliyet oluştu.",
                        "teaching_point": "Gelişimi normal, tekrarlayan ağır enfeksiyon öyküsü olmayan immünokompetan çocuklarda yaygın kutanöz lezyonlar için rutin immün panel gerekmez.",
                    },
                    {
                        "text": "Papüllerin yüzeyini bistüriyle delerek steril eküvyon çubuğuyla bakteriyel ve fungal kültür örnekleri alıp acilen mikrobiyoloji laboratuvarına göndermek",
                        "is_correct": False,
                        "scenario_update": "Papüllerin delinmesi ağrı ve kanamaya yol açtı; kültürlerde patojen üremedi ve iyileşme gecikti.",
                        "teaching_point": "Pürülan akıntı veya selülit benzeri süperenfeksiyon bulgusu yoksa lezyonları delmek veya kültür almak kontraendikedir.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Öykü ve fizik muayenedeki lezyon morfolojisi dikkate alındığında en olası klinik tanı nedir?",
                "options": [
                    {
                        "text": "Verruka Vulgaris (Yaygın Siğil)",
                        "is_correct": False,
                        "scenario_update": "Verruka vulgariste hiperkeratotik, pürtüklü karnabahar benzeri lezyonlar görülür; düzgün yüzeyli santral umbilike kubbe papüller olmaz.",
                        "teaching_point": "Verrukalar HPV kaynaklıdır ve yüzeyi sert, hiperkeratotiktir; ortası göbekli inci benzeri morfoloji göstermez.",
                    },
                    {
                        "text": "Varisella Zoster (Suçiçeği)",
                        "is_correct": False,
                        "scenario_update": "Suçiçeğinde lezyonlar hızla polimorfik veziküllere dönüşür, kaşıntılıdır, ateş eşlik eder ve haftalarca aynı papül formunda kalmaz.",
                        "teaching_point": "Varisella akut başlangıçlı, ateşli ve hızla vezikül-krut evrelerine ilerleyen kaşıntılı bir enfeksiyondur.",
                    },
                    {
                        "text": "Molluskum Kontagiozum",
                        "is_correct": True,
                        "explanation": "Kubbe şeklinde, santral umbilike inci parlaklığındaki papüller Molluscum contagiosum virüsü enfeksiyonu için karakteristiktir.",
                        "new_finding": "Klinik tanı Molluskum Kontagiozum olarak kesinleştirildi.",
                    },
                    {
                        "text": "Gençlik Ksantogranülomu",
                        "is_correct": False,
                        "scenario_update": "Ksantogranülomlar sarı-turuncu renkli, umbilikasyon içermeyen soliter veya az sayıda nodüllerdir; lezyon özellikleri uymamaktadır.",
                        "teaching_point": "Ksantogranülom sarımsı histiyositik proliferasyon olup santral göbekli parlak inci papülleri yapmaz.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Yönetim",
                "question": "Molluskum kontagiozum tanısı alan bu çocuk ve ailesi için en uygun yönetim stratejisi hangisidir?",
                "options": [
                    {
                        "text": "Acil serviste tüm lezyonları cerrahi küretajla kazımak veya sıvı nitrojen koterizasyonuyla seanslar halinde agresif cerrahi kriyoterapi uygulamak",
                        "is_correct": False,
                        "scenario_update": "Küretaj ve agresif kriyoterapi çocukta kalıcı hipopigmentasyon, hipertrofik skar ve tedaviye bağlı fobiye yol açtı.",
                        "teaching_point": "Küçük çocuklarda invaziv girişimler skar bırakabilir ve travmatiktir; lezyonların kendiliğinden gerileyeceği unutulmamalıdır.",
                    },
                    {
                        "text": "Sistemik yayılımı önlemek için oral asiklovir süspansiyon ve profilaktik geniş spektrumlu oral sefalosporin antibiyotik tedavisi reçete etmek",
                        "is_correct": False,
                        "scenario_update": "Poxvirüslere asiklovir etkisizdir ve bakteriyel süperenfeksiyon yokluğunda antibiyotik sadece bağırsak florasını bozdu.",
                        "teaching_point": "Molluskum kontagiozum bir poxvirüs enfeksiyonudur; asiklovir veya oral antibiyotikler tedavide kesinlikle etkisizdir.",
                    },
                    {
                        "text": "Papülleri hızla kurutmak amacıyla tüm lezyonlu deriye sabah akşam yüksek potensli topikal klobetazol kortikosteroid krem reçete etmek",
                        "is_correct": False,
                        "scenario_update": "Güçlü kortikosteroid uygulanması lokal immüniteyi baskılayarak lezyonların hızla çoğalmasına ve büyümesine neden oldu.",
                        "teaching_point": "Topikal kortikosteroidler virüsün çoğalmasını artırarak molluskum lezyonlarının yayılmasına yol açabilir.",
                    },
                    {
                        "text": "Lezyonların kendiliğinden gerileyeceğini aileye anlatmak, lezyonları sıkma ve kaşımadan kaçınmayı tembihlemek, ortak havlu kullanımını kesinlikle engellemek",
                        "is_correct": True,
                        "explanation": "İmmünokompetan çocuklarda lezyonlar 6-18 ayda nedbesiz geriler; otokoinokülasyonu ve bulaşı önlemek için sıkmamak ve havlu paylaşmamak esastır.",
                        "new_finding": "Aileye lezyonların selim doğası anlatıldı. Tırnakların kısa kesilmesi, banyoda liflenmemesi ve yüzme havuzunda lezyonların su geçirmez bantla kapatılması önerildi.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y25",
        "category": "👶 Ağlayan, Emmeyen, Huzursuz Bebek",
        "age": "7 Aylık",
        "gender": "Kız",
        "complaint": "Alt bez bölgesinde şiddetli kızarıklık, pişik ve huzursuzluk",
        "history": (
            "Yedi aylık kız bebek annesi tarafından alt bez bölgesindeki döküntüler nedeniyle getiriliyor: 'Kızımın altındaki "
            "kızarıklık yaklaşık beş gün önce başladı. Normalde pişik kremi sürünce geçerdi ama bu sefer hiç fayda etmedi, "
            "aksine daha da koyu kırmızı oldu ve bacak kıvrımlarının içine doğru yayıldı. Kızarıklığın çevresinde küçük sivilce "
            "gibi kırmızı noktalar çıkmaya başladı. Altını her açtığımızda veya ıslattığında canı çok yanıyor ve durmaksızın "
            "ağlıyor. İki hafta önce üst solunum yolu enfeksiyonu nedeniyle bir hafta antibiyotik şurup kullanmıştı.'"
        ),
        "final_diagnosis": "Bebek Bezi Dermatiti ve Sekonder Kandida Süperenfeksiyonu",
        "disposition": "Yeşil Alandan Topikal Antifungal, Çinko Oksit Bariyer Krem ve Bez Bakımı Eğitimi ile Taburculuk",
        "case_pearl": (
            "Basit irritan bebek bezi dermatitinde inguinal katlantılar korunurken, sekonder Candida albicans süperenfeksiyonu "
            "eklendiğinde parlak kırmızı eritematöz plaklar inguinal kıvrımları da tutar ve çevreye dağılan noktasal satellit "
            "püstüller/papüller görülür. Yakın zamanda antibiyotik kullanımı önemli bir kolaylaştırıcı faktördür. Tedavide "
            "katlantılara topikal antifungal (klotrimazol veya mikonazol), üzerine çinko oksitli bariyer krem uygulanmalı ve "
            "bölgenin kuru kalması sağlanmalıdır."
        ),
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Alt bez alanında şiddetli kızarıklık ve huzursuzlukla başvuran bu süt çocuğunda ilk klinik muayene yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Huzursuzluk ve yaygın cilt bulguları nedeniyle bebeği acil Sarı Alana alıp erken sepsis kuşkusuyla damar yolu açmak",
                        "is_correct": False,
                        "scenario_update": "Sarı Alanda bebeğin ateşi olmadığı, beslenmesinin iyi ve hemodinamisinin tamamen stabil olduğu görüldü.",
                        "teaching_point": "Genel durumu iyi, ateşi ve sistemik enfeksiyon belirtisi olmayan lokalize cilt lezyonlu bebekler Yeşil Alanda değerlendirilir.",
                    },
                    {
                        "text": "Lokal lezyon muayenesini yapmadan önce tüm püstülleri enjektör iğnesiyle patlatarak elde edilen pürülan materyali mikrobiyoloji laboratuvarına ulaştırmak",
                        "is_correct": False,
                        "scenario_update": "Püstüllerin mekanik olarak boşaltılması bebeğe şiddetli acı verdi ve deride açık erozyonlar oluşturdu.",
                        "teaching_point": "İntakt lezyonların agresif şekilde patlatılması ağrı ve sekonder bakteriyel giriş kapısı oluşturur; muayene inspeksiyonla yapılmalıdır.",
                    },
                    {
                        "text": "Vital bulguları almak, perineal bölgeyi, inguinal katlantıları, perianal dokuyu ve oral mukozayı dikkatlice muayene etmek",
                        "is_correct": True,
                        "explanation": "İnguinal kıvrımların tutulumu, periferik çevre püstüllerin varlığı ve eşlik edebilecek oral mukoza lezyonları kritik ayırt edici bulgulardır.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 114/dk, SS 26/dk, SpO2 %99. Fizik Muayene: Gluteal, perineal ve her iki inguinal katlantıyı içine alan, parlak 'biftek kırmızısı' eritemli, masere plaklar saptandı. Plağın periferinde sağlam deriye saçılmış çok sayıda 1-2 mm boyutunda noktasal eritematöz çevre püstül ve papüller görüldü. Oral mukozada yanak içinde beyaz membranöz lezyonlar saptandı. Sistemik muayeneler doğal.",
                    },
                    {
                        "text": "Kızarıklığın sınırları belirgin olduğu için öncelikle çocuk istismarı açısından genital yaralanma ve travma odaklı adli muayene gerçekleştirmek",
                        "is_correct": False,
                        "scenario_update": "Adli şüphe aileyi renside etti; perineal kıvrımları tutan parlak eritemin tipik bir dermatolojik süreç olduğu anlaşıldı.",
                        "teaching_point": "Katlantıları tutan masere eritem ve periferik püstüller enfeksiyöz dermatolojik süreçlerle uyumludur; travmatik veya adli özellik taşımaz.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Yaklaşım Kararı",
                "question": "İnguinal katlantıları tutan parlak kızarıklığı ve çevresel püstülleri olan bu bebekte tetkik stratejiniz ne olmalıdır?",
                "options": [
                    {
                        "text": "Sistemik bakteriyemi veya derin doku enfeksiyonu riskini değerlendirmek üzere tam kan sayımı, CRP ve kan kültürünü acilen almak",
                        "is_correct": False,
                        "scenario_update": "Laboratuvar sonuçlarında lökosit ve CRP normal sınırlarda geldi; kan alınırken bebek uzun süre sakinleşmedi.",
                        "teaching_point": "Ateş veya toksik görünümün olmadığı yüzeyel perineal tablolarda sistemik enflamatuar belirteçler ve kan kültürü endike değildir.",
                    },
                    {
                        "text": "Klinik görünüm ve lezyon dağılımı karakteristik olduğundan acil serviste kan tahlili veya radyolojik tetkik istememek",
                        "is_correct": True,
                        "explanation": "İnguinal kıvrım tutulumu ve periferik lezyonlar klinik tanı için yeterlidir; rutin laboratuvar araştırması gerekmez.",
                        "new_finding": "Gereksiz laboratuvar tetkiklerinden kaçınıldı; klinik bulgularla doğrudan tanı ve tedavi aşamasına geçildi.",
                    },
                    {
                        "text": "Langerhans hücreli histiyositoz olasılığını dışlamak amacıyla sedasyon altında acil perineal cerrahi punch deri biyopsisi işlemini planlamak",
                        "is_correct": False,
                        "scenario_update": "Punch biyopsi önerisi aileyi paniğe sevk etti; invaziv işlem bölgedeki doku maserasyonunu artırma riski taşıdı.",
                        "teaching_point": "Tipik eritematöz masere döküntülerde histiyositoz gibi nadir antiteler ilk aşamada düşünülmez ve acil biyopsi yapılmaz.",
                    },
                    {
                        "text": "Perineal döküntülerin idrar yolu enfeksiyonu sekeli olabileceği düşüncesiyle mesane kateterizasyonu uygulayarak steril idrar tahlili ve kültürü göndermek",
                        "is_correct": False,
                        "scenario_update": "Ağrılı idrar sondası uygulaması eritemli perineal dokuda kanamaya neden oldu; tam idrar tetkiki normal sonuçlandı.",
                        "teaching_point": "İdrar yolu enfeksiyonu perineal kıvrımlarda biftek kırmızısı lezyon yapmaz; travmatize dokuya gereksiz kateter uygulanmamalıdır.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Öykü, antibiyotik kullanımı ve fizik muayene bulguları birlikte ele alındığında en olası klinik tanı nedir?",
                "options": [
                    {
                        "text": "Basit İrritan Bez Dermatiti",
                        "is_correct": False,
                        "scenario_update": "Basit irritan dermatitte inguinal katlantılar ve kıvrımlar genellikle korunur, satellit lezyonlar ve parlak eritem izlenmez.",
                        "teaching_point": "Basit irritan kontakt dermatitte dışbükey yüzeyler tutulurken derin kıvrımlar korunur; kıvrım tutulumu süperenfeksiyon lehinedir.",
                    },
                    {
                        "text": "İnvers Psoriyazis (Ters Sedef)",
                        "is_correct": False,
                        "scenario_update": "İnvers psoriyaziste parlak kırmızı keskin sınırlı plaklar görülebilse de satellit püstüller ve oral pamukçuk eşliği beklenmez.",
                        "teaching_point": "İnvers sedefte lezyonlar kıvrımlardadır ancak satellit püstüller bulunmaz ve yakın dönem antibiyotik öyküsüyle ilişkili değildir.",
                    },
                    {
                        "text": "Bebek Bezi Dermatiti ve Sekonder Kandida Süperenfeksiyonu",
                        "is_correct": True,
                        "explanation": "İnguinal kıvrımların belirgin tutulumu, parlak biftek kırmızısı maserasyon, satellit püstüller ve oral tutulum tipiktir.",
                        "new_finding": "Klinik tanı Bebek Bezi Dermatiti ve Sekonder Kandida Süperenfeksiyonu olarak doğrulandı.",
                    },
                    {
                        "text": "Streptokokal Perianal Selülit",
                        "is_correct": False,
                        "scenario_update": "Perianal streptokokal enfeksiyonda anüs çevresinde keskin sınırlı parlak eritem ve kanamalı defekasyon görülür; inguinal katlantılar tutulmaz.",
                        "teaching_point": "Streptokokal hastalıkta anüs çevresi sınırlı tutulur ve satellit püstüller görülmez.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Yönetim",
                "question": "Kandida süperenfeksiyonlu bebek bezi dermatiti tanısı kesinleşen bu bebek için en uygun tedavi yaklaşımı nedir?",
                "options": [
                    {
                        "text": "Enflamasyonu derhal baskılamak amacıyla günde iki kez yüksek potensli topikal florlu kortikosteroid krem reçete edip taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Güçlü steroid antifungal olmadan uygulandığı için fungal proliferasyon şiddetlendi ve cilt atrofisi gelişti.",
                        "teaching_point": "Fungal süperenfeksiyon varlığında tek başına güçlü steroid kullanımı mantarın çoğalmasına ve sistemik emilime yol açar.",
                    },
                    {
                        "text": "Süperenfeksiyonun derin dokulara yayılmasını önlemek amacıyla bebeği yatırıp intravenöz flukonazol infüzyonu ve parenteral geniş spektrumlu antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "İnvaziv fungal enfeksiyonu olmayan stabil bebekte gereksiz hastane yatışı ve parenteral ilaç toksisite riski doğdu.",
                        "teaching_point": "Yüzeyel kutanöz fungal enfeksiyonlarda hemodinami stabilse parenteral tedavi endike değildir; topikal tedavi yeterlidir.",
                    },
                    {
                        "text": "Lezyonlara talk pudrası uygulayarak bölgeyi kurutmak ve eşzamanlı olarak oral yoldan amoksisilin-klavulanat antibiyotik şurup reçete ederek taburculuk planlamak",
                        "is_correct": False,
                        "scenario_update": "Pudra kullanımı aspirasyon riski yarattı ve ciltte granülasyona neden oldu; antibiyotik ise mantar florasını daha da artırdı.",
                        "teaching_point": "Pudra solunum yolu için tehlikelidir; antibiyotikler koruyucu bakterileri yok ederek kandida üremesini alevlendirir.",
                    },
                    {
                        "text": "Topikal klotrimazol krem ile çinko oksit bariyer krem başlamak, altını sık değiştirmek ve kuru tutulmasını sağlamak",
                        "is_correct": True,
                        "explanation": "Günde 2-3 kez topikal antifungal (klotrimazol veya mikonazol), üzerine bariyer krem sürülmeli ve bölge havalandırılmalıdır.",
                        "new_finding": "Topikal antifungal ve çinko oksit bariyer krem başlandı. Eşlik eden oral pamukçuk için nistatin damla reçete edildi ve bez bakımı eğitimi verildi.",
                    },
                ],
            },
        ],
    },
]
