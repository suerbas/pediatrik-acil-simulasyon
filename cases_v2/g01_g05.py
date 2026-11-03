# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - G01-G05 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "G01",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "16 Aylık",
        "gender": "Erkek",
        "complaint": "Burun tıkanıklığı, huzursuzluk, hafif ateş ve öksürük",
        "history": (
            "Annesi kucağında getiriyor: 'Doktor bey/hanım, oğlum 2 gündür çok huysuz. Burnu sürekli berrak şekilde "
            "akıyor ve tıkanıyor, gece memeyi tutmakta zorlandı, ağzından nefes alıyor. Dün akşam ateşi evde 38.1°C "
            "çıktı, ateş düşürücü verince rahatladı. Ara sıra özellikle sırtüstü yatınca öksürüyor ama nefes darlığı "
            "veya morarması olmadı. Kreşe giden ablasında da geçen hafta benzer burun akıntısı ve hapşırık şikayetleri vardı.'"
        ),
        "final_diagnosis": "Akut Viral Nazofarenjit (Soğuk Algınlığı)",
        "disposition": "Yeşil Alandan Ayaktan Semptomatik Tedavi ve Aile Eğitimi ile Taburculuk",
        "case_pearl": (
            "Süt çocuğu ve küçük çocuklarda viral üst solunum yolu enfeksiyonlarında en sık huzursuzluk ve beslenme "
            "güçlüğü nedeni burun tıkanıklığıdır. Rutin hemogram, CRP veya akciğer grafisi endike değildir; "
            "antibiyotiklerin ve 6 yaş altında sistemik dekongestan/antihistaminik kombinasyonlarının tedavide yeri yoktur."
        ),
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Bu hastada ilk değerlendirmede odaklanmanız gereken en uygun klinik muayene yaklaşımı hangisidir?",
                "options": [
                    {
                        "text": "Orofarenks ve burun mukozasını inceleyip, otoskopik muayeneyi çocuğun huzursuzluğunu artırmamak adına erteleyerek doğrudan semptomatik burun açıcı damla uygulamasına geçmek",
                        "is_correct": False,
                        "scenario_update": "Burun damlası sonrası bebek kısmen rahatlasa da kulak zarları değerlendirilmediği için eşlik edebilecek orta kulak kaynaklı odak olasılığı dışlanamamış oldu.",
                        "teaching_point": "Ateş ve huzursuzluk ile başvuran iki yaş altı çocuklarda kulak semptomu tarif edilmese bile otoskopik muayene fizik muayenenin vazgeçilmez bir parçasıdır.",
                    },
                    {
                        "text": "Pediatrik Değerlendirme Üçgeni, vital bulgular, göğüs duvarı çekilmeleri, akciğer oskültasyonu, hidrasyon durumu ve bilateral otoskopik muayeneyi eksiksiz şekilde tamamlamak",
                        "is_correct": True,
                        "explanation": "Küçük çocuklarda üst solunum yolu semptomlarıyla başvuruda takipne ve çekilme gibi alt solunum yolu bulguları ile orta kulak tutulumu dışlanmalı, hidrasyon değerlendirilmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 37.8°C, KTA 118/dk, SS 28/dk, SpO2 %99. Genel görünüm stabil. Burun mukozası ödemli ve seröz sekresyonlu, orofarenks hafif hiperemik, tonsillerde eksüda yok. Bilateral timpanik membranlar doğal. Akciğer oskültasyonunda ral veya ronküs yok, çekilme yok, mukozalar ıslak.",
                    },
                    {
                        "text": "Vital bulguları ve solunum seslerini değerlendirdikten sonra gece öksürüğü tarif edildiği için acil serviste kurtarıcı nebülize salbutamol tedavisi uygulayıp yanıtı gözlemlemek",
                        "is_correct": False,
                        "scenario_update": "Nebülize bronkodilatatör uygulaması sonrası bebeğin kalp tepe atımı 152/dk'ya yükseldi ve huzursuzluğu arttı; oskültasyonda zaten bronkospazm bulgusu olmadığı görüldü.",
                        "teaching_point": "Yatarken artan öksürük genellikle postnazal sekresyon akıntısına bağlıdır; oskültasyonda hışıltı veya ekspiryum uzaması olmadan ampirik bronkodilatatör verilmemelidir.",
                    },
                    {
                        "text": "Ateş ve emme güçlüğü öyküsü nedeniyle fizik muayeneyi kısa tutup hastayı monitörizasyon ve damar yolu açılması için Sarı Alana devretmek",
                        "is_correct": False,
                        "scenario_update": "Sarı alana alınan bebeğin genel görünümü, perfüzyonu ve oksijen satürasyonu tamamen normal seyretti; acil gözlem yatağı gereksiz yere meşgul edildi.",
                        "teaching_point": "Genel durumu iyi, yaşa göre solunum sayısı normal ve dehidratasyon bulgusu olmayan hastalar Yeşil Alanda değerlendirilmelidir.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Yaklaşım Kararı",
                "question": "Fizik muayenesinde takipnesi, çekilmesi ve ek odak bulgusu saptanmayan bu bebekte tetkik kararınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Gizli bakteriyemi ve bakteriyel süperenfeksiyon olasılığını dışlamak amacıyla tam kan sayımı, CRP ve prokalsitonin tetkiklerini birlikte istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: WBC 9.800/mm³ (lenfosit ağırlıklı), Hb 11.8 g/dL, PLT 290.000/mm³, CRP 4.2 mg/L, Prokalsitonin 0.04 ng/mL. Kan alınırken bebek ciddi şekilde huzursuzlandı.",
                        "teaching_point": "Genel durumu iyi, ateşi 38.5°C altında ve muayenesi doğal olan üst solunum yolu enfeksiyonlarında akut faz reaktanları yönetimi değiştirmez.",
                    },
                    {
                        "text": "Gece öksürüğü ve burun akıntısını değerlendirmek için arka-ön akciğer grafisi ile birlikte paranazal sinüs grafisi çekilmesini planlamak",
                        "is_correct": False,
                        "scenario_update": "RADYOLOJİ SONUCU: Akciğer parankiminde infiltrasyon izlenmedi. On altı aylık bebekte sinüs boşlukları henüz yeterince pnömatize olmadığından sinüs grafisi tanısal bilgi sağlamadı.",
                        "teaching_point": "Takipne, hipoksemi veya patolojik oskültasyon bulgusu olmadıkça akciğer grafisi endike değildir; ayrıca küçük çocuklarda rutin sinüs grafisi çekilmez.",
                    },
                    {
                        "text": "Herhangi bir laboratuvar veya radyolojik görüntüleme tetkiki istemeden, mevcut klinik bulgularla Yeşil Alanda tanı ve tedaviye ilerlemek",
                        "is_correct": True,
                        "explanation": "Klinik olarak üst solunum yoluyla sınırlı, vital bulguları stabil ve genel durumu iyi olan çocukta laboratuvar veya görüntüleme tetkiki gerekmez.",
                        "new_finding": "Tetkik istenmedi; aileye bebeğin akciğer dinleme bulgularının ve kulak zarlarının tamamen doğal olduğu açıklandı.",
                    },
                    {
                        "text": "Nazofarengeal sürüntüden genişletilmiş solunum yolu viral multipleks PCR paneli ve eş zamanlı boğaz kültürü göndererek sonucu beklemek",
                        "is_correct": False,
                        "scenario_update": "Mikrobiyoloji laboratuvarından multipleks PCR sonucunun ertesi gün, kültür sonucunun ise 48 saat sonra çıkacağı bildirildi; acil yönetiminde hiçbir değişiklik olmadı.",
                        "teaching_point": "Ayaktan takip edilecek hafif üst solunum yolu tablolarında multipleks viral panel maliyet-etkin değildir; 3 yaş altında bakteriyel boğaz kültürü de rutin önerilmez.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Mevcut anamnez ve fizik muayene bulgularıyla en olası klinik tanınız nedir?",
                "options": [
                    {
                        "text": "Akut Viral Nazofarenjit (Soğuk Algınlığı)",
                        "is_correct": True,
                        "explanation": "Ev içi temas öyküsü, seröz rinit, hafif ateş ve normal kulak ile akciğer muayenesi akut viral nazofarenjit ile uyumludur.",
                        "new_finding": "Klinik tanı Akut Viral Nazofarenjit olarak kesinleştirildi.",
                    },
                    {
                        "text": "Akut Bakteriyel Rinosinüzit",
                        "is_correct": False,
                        "scenario_update": "Semptomların henüz ikinci gününde olması nedeniyle bakteriyel sinüzit tanı kriterleri olan on günü aşan semptom veya ağır başlangıç karşılanmadı.",
                        "teaching_point": "Akut bakteriyel rinosinüzit tanısı için semptomların 10 günü aşması, iyileşirken tekrar kötüleşme veya en az 3-4 gün süren ≥39°C ateş ve pürülan akıntı gerekir.",
                    },
                    {
                        "text": "Erken Evre Akut Bronşiolit",
                        "is_correct": False,
                        "scenario_update": "Tekrarlanan solunum muayenesinde takipne, ekspiratuar uzama, sibilan ronküs veya krepitan ral saptanmadı.",
                        "teaching_point": "Alt solunum yolu obstrüksiyon bulguları olan hışıltı, raller, takipne veya çekilme bulunmadan yalnızca postnazal öksürükle bronşiolit tanısı konulmaz.",
                    },
                    {
                        "text": "Mevsimsel Alerjik Rinit Atağı",
                        "is_correct": False,
                        "scenario_update": "Akut başlayan ateş, aile içi enfeksiyon teması ve 16 aylık yaş grubu tek başına mevsimsel alerjik reaksiyon tablosuyla uyumlu bulunmadı.",
                        "teaching_point": "Alerjik rinit ateş yapmaz ve süt çocuğu döneminde nadirdir; akut ateşli seröz rinit tablosunda öncelikle viral enfeksiyonlar düşünülmelidir.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu hastanın reçete, evde bakım ve taburculuk planı aşağıdakilerden hangisi olmalıdır?",
                "options": [
                    {
                        "text": "Sekonder bakteriyel enfeksiyonu önlemek amacıyla oral amoksisilin-klavulanat süspansiyon ve burun akıntısını kesmek için psödoefedrin-klorfeniramin kombinasyonu içeren şurup reçete etmek",
                        "is_correct": False,
                        "scenario_update": "Ertesi gün bebekte antibiyotiğe bağlı sulu dışkılama ve kombine soğuk algınlığı şurubuna bağlı belirgin huzursuzluk ile taşikardi gelişti.",
                        "teaching_point": "Viral nazofarenjitte antibiyotik komplikasyonları önlemez; ayrıca 6 yaş altında sistemik dekongestan ve antihistaminik kombinasyonları ciddi toksisite nedeniyle kontrendikedir.",
                    },
                    {
                        "text": "Beslenme öncesinde topikal oksimetazolin burun spreyini günde 4 kez 7 gün süreyle ve gece öksürüğü için dekstrometorfan şurup başlamak",
                        "is_correct": False,
                        "scenario_update": "Beşinci günden sonra bebekte ilaca bağlı gelişen rebaund mukozal ödem nedeniyle burun tıkanıklığı daha da şiddetlendi ve letarji eğilimi görüldü.",
                        "teaching_point": "Küçük çocuklarda topikal sempatomimetik dekongestanlar sistemik emilim ve rhinitis medicamentosa riski, santral antitussifler ise solunum depresyonu riski nedeniyle önerilmez.",
                    },
                    {
                        "text": "Düzenli ateş düşürücü şurup reçete edip mukolitik olarak oral asetilsistein ve birinci kuşak sedatif antihistaminik damla ile taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Mukolitik şurup sonrası bronşiyal sekresyonları efektif öksüremeyen bebekte hırıltı arttı, sedatif antihistaminik ise emme performansını düşürdü.",
                        "teaching_point": "İki yaş altı çocuklarda mukolitik ajanlar sekresyon göllenmesine yol açabileceği için, birinci kuşak antihistaminikler ise sedasyon ve antikolinerjik yan etkileri nedeniyle kullanılmaz.",
                    },
                    {
                        "text": "Emzirme ve uyku öncesi serum fizyolojikle nazal aspirasyon, gerektiğinde parasetamol, sık emzirme ve uyarı bulguları eğitimiyle taburcu etmek",
                        "is_correct": True,
                        "explanation": "Küçük çocuklarda viral nazofarenjit tedavisinin temel taşı burun açıklığının izotonik tuzlu su ile sağlanması, uygun hidrasyon ve gerektiğinde antipiretiktir.",
                        "new_finding": "Tedavi düzenlendi; aileye hızlı nefes alma, göğüste çekilme, sıvı alamama veya 3-4 günü aşan ateş durumunda tekrar başvuru eğitimi verilerek taburcu edildi.",
                    },
                ],
            },
        ],
    },
    {
        "id": "G02",
        "category": "👂 Kulak Ağrısı & KBB",
        "age": "8 Yaş",
        "gender": "Kız",
        "complaint": "Boğaz ağrısı, yutkunma güçlüğü ve yüksek ateş",
        "history": (
            "Hasta kendisi anlatıyor: 'Dün sabah okuldayken boğazım çok acımaya başladı, yutkunurken batıyor. "
            "Başım ve karnım da biraz ağrıyor ama burnum hiç akmıyor, öksürüğüm de yok.' Annesi ekliyor: "
            "'Dün geceden beri ateşi 38.8°C'ye kadar çıkıyor, boynunun yan taraflarında da dokununca hassasiyet var.'"
        ),
        "final_diagnosis": "Akut Streptokoksik Tonsillofarenjit (AGBHS)",
        "disposition": "Yeşil Alandan Uygun Antibiyoterapi ve Destek Tedavisi ile Taburculuk",
        "case_pearl": (
            "Öksürük ve rinit olmadan ani başlayan boğaz ağrısı, ateş, tonsiller eksüda, yumuşak damak peteşileri ve "
            "hassas ön servikal lenfadenopati bakteriyel tonsillofarenjit olasılığını (Modifiye Centor / McIsaac skoru) "
            "yükseltir. Tanı hızlı antijen testi veya boğaz kültürü ile doğrulanmalı, ilk tercih olarak dar spektrumlu "
            "oral Penisilin V / Amoksisilin (10 gün) veya tek doz İM Benzatin Penisilin G seçilmelidir."
        ),
        "steps": [
            {
                "stage_title": "Fizik Muayene ve Klinik Değerlendirme",
                "question": "Bu hastada fizik muayenede öncelikle neyi değerlendirmeli ve klinik yaklaşımı nasıl belirlemelisiniz?",
                "options": [
                    {
                        "text": "Boyunda hassasiyet tarif edildiği için ağız içi muayeneyi zorlamadan derin boyun enfeksiyonu açısından öncelikle acil yüzeyel boyun ultrasonografisi istemek",
                        "is_correct": False,
                        "scenario_update": "Radyoloji bölümünde yapılan boyun ultrasonografisinde bilateral 15 mm reaktif servikal lenf nodları raporlandı ancak birincil farengeal odak değerlendirmesi gecikti.",
                        "teaching_point": "Akut farengeal enfeksiyonlara ikincil hassas ön servikal lenfadenopati beklenen bir muayene bulgusudur; trismus veya boyun asimetrisi yoksa ultrasonografi endike değildir.",
                    },
                    {
                        "text": "Karın ağrısı ve yüksek ateş birlikteliği nedeniyle boğaz muayenesini erteleyip akut cerrahi batın açısından çocuk cerrahisi konsültasyonu talep etmek",
                        "is_correct": False,
                        "scenario_update": "Yapılan batın muayenesinde defans ve rebound saptanmadı; hastanın karın ağrısının üst solunum yolu enfeksiyonuna eşlik eden mezenterik lenfadenite bağlı olduğu anlaşıldı.",
                        "teaching_point": "Okul çağı çocuklarında bakteriyel tonsillofarenjit tablolarına baş ağrısı, bulantı ve yansıyan karın ağrısı oldukça sık eşlik edebilir.",
                    },
                    {
                        "text": "Orofarenkste tonsil eksüdası, uvula konumu ve damak peteşilerini, ön servikal lenf nodlarını, döküntüyü ve hepatosplenomegali varlığını muayene etmek",
                        "is_correct": True,
                        "explanation": "Bakteriyel ve viral etkenleri ayırt etmek, derin boyun komplikasyonlarını dışlamak ve klinik olasılığı belirlemek için tam orofarenks, lenf nodu ve batın muayenesi gereklidir.",
                        "new_finding": "Vital Bulgular: Ateş 38.9°C, KTA 104/dk, SS 20/dk. Orofarenkste bilateral tonsiller hipertrofik ve hiperemik, üzerlerinde sarı-beyaz kriptik eksüdalar mevcut, yumuşak damakta peteşiler görülüyor, uvula orta hatta. Bilateral ön servikal bölgede 1.5 cm ağrılı hareketli lenfadenopati mevcut. Hepatosplenomegali ve döküntü yok.",
                    },
                    {
                        "text": "Eksüdatif görünümü yeterli kabul ederek mikrobiyolojik doğrulama planlamadan doğrudan acil serviste tek doz intramüsküler seftriakson enjeksiyonu uygulayıp hastayı göndermek",
                        "is_correct": False,
                        "scenario_update": "Mikrobiyolojik kanıt alınmadan yapılan geniş spektrumlu parenteral antibiyotik enjeksiyonu ağrılı oldu ve kılavuzların önerdiği tanı-tedavi basamaklarına uymadı.",
                        "teaching_point": "Tonsiller üzerindeki eksüda tek başına bakteriyel ve viral ayrımı yaptıramaz; ampirik geniş spektrumlu parenteral sefalosporin kullanımı uygun değildir.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik İstem Kararı",
                "question": "Öksürük olmadan ateş, tonsiller eksüda ve hassas ön servikal lenfadenopatisi olan bu hastada tanıyı doğrulamak için en uygun yaklaşım nedir?",
                "options": [
                    {
                        "text": "Orofarengeal sürüntüden hızlı bakteriyel antijen tarama testi istemek ve negatif çıkması halinde standart boğaz kültürü ile doğrulamak",
                        "is_correct": True,
                        "explanation": "Klinik olarak bakteriyel tonsillofarenjit olasılığı yüksek olan çocuklarda mikrobiyolojik doğrulama için hızlı antijen tarama testi ve gerekirse boğaz kültürü altın standarttır.",
                        "new_finding": "Orofarengeal sürüntüden çalışılan hızlı bakteriyel antijen tarama testi POZİTİF sonuçlandı.",
                    },
                    {
                        "text": "Venöz kan örneği alarak geçirilmiş enfeksiyon antikor titresi, C-reaktif protein ve eritrosit sedimentasyon hızı düzeylerini birlikte çalışmak",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: Antikor titresi 85 IU/mL (Normal <200), CRP 28 mg/L, Sedimentasyon 22 mm/saat. Normal çıkan antikor sonucu akut etkeni doğrulamadı.",
                        "teaching_point": "Serolojik antikor titreleri akut enfeksiyondan 1-3 hafta sonra yükselmeye başlar; akut tonsillofarenjit tanısında hiçbir yeri yoktur, yalnızca geçirilmiş enfeksiyonu gösterir.",
                    },
                    {
                        "text": "Herhangi bir sürüntü veya laboratuvar testi istemeden yalnızca fizik muayene bulgularına dayanarak doğrudan ampirik geniş spektrumlu oral antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "Mikrobiyolojik doğrulama yapılmadığı için hastanın gerçekten 10 günlük antibiyotik tedavisine ve akut romatizmal ateş profilaksisine ihtiyacı olup olmadığı belirsiz kaldı.",
                        "teaching_point": "Klinik bulgular bakteriyel olasılığı artırsa da eksüdatif farenjitlerin önemli bir kısmı viraldir; antibiyotik öncesi hızlı antijen testi veya kültürle doğrulama önerilir.",
                    },
                    {
                        "text": "Tam kan sayımı, periferik yayma, karaciğer fonksiyon testleri ve geniş viral seroloji paneli isteyerek sonuçlar çıkana kadar beklemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: WBC 13.600/mm³ (nötrofil hakimiyeti), atipik lenfosit görülmedi, AST 22 U/L, ALT 18 U/L. Gereksiz venöz kan alımı ve bekleme yaşandı.",
                        "teaching_point": "Jeneralize lenfadenopati, splenomegali veya uzamış semptomlar olmadıkça tipik akut tonsillofarenjit başvurularında ilk basamakta periferik yayma ve viral seroloji gerekmez.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik bulgular ve pozitif hızlı antijen testi doğrultusunda kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Enfeksiyöz Mononükleoz (EBV Tonsillofarenjiti)",
                        "is_correct": False,
                        "scenario_update": "Hastada arka servikal ve jeneralize lenfadenopati, splenomegali veya periorbital ödem bulunmamakta olup hızlı bakteriyel antijen testi pozitiftir.",
                        "teaching_point": "Enfeksiyöz mononükleozda yaygın lenfadenopati, splenomegali ve uzamış semptomlar ön plandadır; bu hastada klinik ve test sonucu AGBHS ile uyumludur.",
                    },
                    {
                        "text": "Akut Streptokoksik (AGBHS) Tonsillofarenjit",
                        "is_correct": True,
                        "explanation": "Ateş, öksürük olmaması, yumuşak damak peteşileri, eksüdatif tonsillit, ön servikal lenfadenopati ve pozitif hızlı antijen testi AGBHS tonsillofarenjitini doğrular.",
                        "new_finding": "Tanı: Akut Streptokoksik Tonsillofarenjit (AGBHS) olarak kesinleştirildi.",
                    },
                    {
                        "text": "Sol Tek Taraflı Peritonsiller Apse",
                        "is_correct": False,
                        "scenario_update": "Muayenede trismus, uvulada karşı tarafa deviasyon, tek taraflı asimetrik yumuşak damak bombeleşmesi veya boğuk ses saptanmadı.",
                        "teaching_point": "Peritonsiller apsede şiddetli trismus, uvula deviasyonu, salya akması ve tek taraflı fluktuasyon veren yumuşak damak şişliği görülür.",
                    },
                    {
                        "text": "Akut Adenoviral Eksüdatif Farenjit",
                        "is_correct": False,
                        "scenario_update": "Hastada eşlik eden konjonktivit, belirgin seröz rinit veya öksürük yok; ayrıca bakteriyel hızlı antijen testi pozitif saptandı.",
                        "teaching_point": "Adenoviral farenjit eksüda yapabilse de genellikle rinit, öksürük ve foliküler konjonktivit (faringokonjonktival ateş) ile birlikte seyreder.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve İzlem Planı",
                "question": "Bu hastada akut romatizmal ateş (ARA) ve süpüratif komplikasyonları önlemek için en uygun tedavi seçeneği hangisidir?",
                "options": [
                    {
                        "text": "Oral Trimetoprim-Sulfametoksazol süspansiyonu günde iki doz 10 gün süreyle reçete etmek ve semptomatik analjezik başlayarak hastayı eve taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Reçete edilen antibiyotik farengeal AGBHS eradikasyonu sağlamadı; hastanın ateşi gerilemedi ve Akut Romatizmal Ateş gelişme riski devam etti.",
                        "teaching_point": "Trimetoprim-sulfametoksazol, tetrasiklinler ve florokinolonlar AGBHS tonsillofarenjitinde bakteriyel eradikasyon sağlamaz ve akut romatizmal ateşi önlemez; kesinlikle kullanılmamalıdır.",
                    },
                    {
                        "text": "Oral Amoksisilin-Klavulanat (90 mg/kg/gün) tedavisiyle birlikte 3 gün oral deksametazon başlamak ve tedavi bitiminde kontrol boğaz kültürü istemek",
                        "is_correct": False,
                        "scenario_update": "Geniş spektrumlu antibiyotik ve sistemik steroid gereksiz yan etkilere yol açtı; asemptomatik hastada tedavi sonrası kontrol kültürü de kılavuzlara aykırıydı.",
                        "teaching_point": "AGBHS'de beta-laktamaz üretimi olmadığından klavulanat eklenmesi gereksizdir; ayrıca rutin sistemik kortikosteroid ve semptomsuz hastada tedavi sonrası kontrol kültürü önerilmez.",
                    },
                    {
                        "text": "Oral Azitromisin süspansiyonu (10 mg/kg/gün, 3 gün) ilk tercih olarak reçete etmek ve bulaş nedeniyle 7 gün okuldan uzak tutmak",
                        "is_correct": False,
                        "scenario_update": "Bölgesel makrolid direnci nedeniyle bakteriyel eradikasyon başarısız oldu; ayrıca 24 saatlik uygun tedavi sonrası okula dönüş gereksiz yere geciktirildi.",
                        "teaching_point": "Makrolidler artan direnç oranları nedeniyle yalnızca penisilin alerjisi olan hastalarda alternatif olarak seçilir; uygun antibiyotiğin 24. saatinden sonra bulaştırıcılık sona erer.",
                    },
                    {
                        "text": "On gün oral Amoksisilin (50 mg/kg/gün) veya tek doz İM Benzatin Penisilin G, parasetamol ve 24. saatte okula dönüş",
                        "is_correct": True,
                        "explanation": "AGBHS'de penisilin direnci yoktur; ilk tercih 10 gün oral Penisilin V / Amoksisilin veya uyum sorunu varsa tek doz İM Benzatin Penisilin G'dir.",
                        "new_finding": "On günlük oral amoksisilin ve parasetamol reçete edildi; antibiyotiğin 24. saatinden itibaren bulaştırıcılığın biteceği ve okula dönebileceği anlatılarak taburcu edildi.",
                    },
                ],
            },
        ],
    },
    {
        "id": "G03",
        "category": "👂 Kulak Ağrısı & KBB",
        "age": "22 Aylık",
        "gender": "Erkek",
        "complaint": "Sağ kulağını çekiştirme, ağlama krizleri ve ateş",
        "history": (
            "Babası anlatıyor: 'Hocam, 3-4 gündür hafif burun akıntısı vardı ama dün gece sabaha kadar hiç uyumadı, "
            "sürekli ağladı ve sağ kulağını tutup çekiştirdi. Sabah ateşi 39.1°C ölçüldü. Kulağından herhangi bir "
            "akıntı gelmedi ama kulağının çevresine dokundurtmuyor.'"
        ),
        "final_diagnosis": "Akut Otitis Media (AOM)",
        "disposition": "Yeşil Alandan Uygun Doz Amoksisilin ve Analjezik Tedavisi ile Taburculuk",
        "case_pearl": (
            "2 yaş altı çocuklarda veya şiddetli semptomu (≥39°C ateş, orta-ağır otalji) olan Akut Otitis Media "
            "vakalarında yüksek doz Amoksisilin (80-90 mg/kg/gün, 10 gün) ve özellikle ilk 24-48 saatte düzenli "
            "sistemik analjezi (parasetamol veya ibuprofen) başlanmalıdır."
        ),
        "steps": [
            {
                "stage_title": "Otoskopik ve Sistemik Muayene",
                "question": "Bu hastada tanıyı kesinleştirmek ve olası komplikasyonları değerlendirmek için fizik muayenede nasıl bir yaklaşım izlemelisiniz?",
                "options": [
                    {
                        "text": "Otoskop ile timpanik membranın bombeleşme, hiperemi ve ışık refleksini incelemek, postauriküler bölgeyi ve meninks irritasyon bulgularını kontrol etmek",
                        "is_correct": True,
                        "explanation": "Orta kulak patolojilerinde en spesifik muayene bulgusu timpanik membranda bombeleşmedir; ayrıca kulak arkası şişlik/hassasiyet ve meninks irritasyon bulguları mutlaka kontrol edilmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 39.0°C, KTA 130/dk, SS 28/dk. Sağ timpanik membran ileri derecede hiperemik, opak ve dışa doğru belirgin bombeleşmiş; ışık refleksi kaybolmuş, perforasyon veya otore yok. Sol kulak zarı doğal. Postauriküler eritem, ödem veya fluktuasyon yok, kulak kepçesi normal konumda, ense sertliği yok.",
                    },
                    {
                        "text": "Çocuk ağladığında kulak zarında fizyolojik kızarıklık olabileceği için otoskopiyi atlayıp yalnızca tragus ve aurikula traksiyonu hassasiyetiyle klinik karar vermek",
                        "is_correct": False,
                        "scenario_update": "Tragus basısı dış kulak yolu kaynaklı ağrılar için anlamlı olup huzursuz çocukta yanıltıcı bulundu; kulak zarının bombeleşmesi ve bütünlüğü değerlendirilemedi.",
                        "teaching_point": "Kulak ağrısı ve ateşle başvuran çocukta otoskopik muayene yapılmadan tanı konulamaz; zarın bombeleşmesi ve perforasyon varlığı tedaviyi doğrudan belirler.",
                    },
                    {
                        "text": "Yüksek ateş ve kulak çevresi hassasiyeti nedeniyle fizik muayeneyi bekletmeden derin doku yayılımını görmek için acil temporal kemik tomografisi istemek",
                        "is_correct": False,
                        "scenario_update": "Yirmi iki aylık çocuğa tomografi çekilebilmesi için sedasyon hazırlığı gündeme geldi; oysa fizik muayenede kulak arkası ödem veya nörolojik bulgu yoktu.",
                        "teaching_point": "Kulak kepçesinde öne-aşağı itilme, postauriküler fluktuasyon veya fokal nörolojik defisit gibi komplikasyon bulguları olmadan kesitsel görüntüleme istenmez.",
                    },
                    {
                        "text": "Dış kulak yoluna topikal lidokainli damla damlatıp otoskopik muayene yapmadan doğrudan kulak burun boğaz hastalıkları acil konsültasyonu talep etmek",
                        "is_correct": False,
                        "scenario_update": "Zar bütünlüğü görülmeden damlatılan anestezik damla perforasyon olasılığı açısından risk oluşturdu ve birinci basamak acil değerlendirmesi eksik kaldı.",
                        "teaching_point": "Timpanik membran bütünlüğü otoskop ile doğrulanmadan dış kulak yoluna topikal ajan uygulanmamalı ve komplike olmayan vakalar doğrudan konsülte edilmemelidir.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik ve Yaklaşım Kararı",
                "question": "Otoskopide sağ timpanik membranda belirgin bombeleşme ve hiperemi saptanan, genel durumu iyi olan bu 22 aylık çocukta ek tetkik gerekir mi?",
                "options": [
                    {
                        "text": "Etken mikroorganizmayı ve antibiyotik duyarlılığını saptamak amacıyla sağ dış kulak yolundan steril eküvyonla sürüntü kültürü alıp laboratuvara göndermek",
                        "is_correct": False,
                        "scenario_update": "KÜLTÜR SONUCU: Dış kulak yolu normal deri florası olan koagülaz negatif stafilokok üredi; zarın arkasındaki gerçek patojeni yansıtmadı.",
                        "teaching_point": "Perfore olmayan sağlam kulak zarında dış kulak yolundan alınan sürüntü kültürü orta kulak boşluğundaki bakteriyel etkenleri kesinlikle göstermez.",
                    },
                    {
                        "text": "Ek laboratuvar veya radyolojik görüntüleme tetkiki istemeden, mevcut otoskopik ve klinik muayene bulgularıyla doğrudan tedavi planına geçmek",
                        "is_correct": True,
                        "explanation": "Net otoskopik bulguları olan, toksik görünmeyen ve komplikasyon saptanmayan çocukta kan tetkiki veya görüntüleme tanı ve tedaviyi değiştirmez.",
                        "new_finding": "Ek tetkik istenmeden mevcut klinik ve otoskopik bulgularla tanı aşamasına geçildi.",
                    },
                    {
                        "text": "Ateşi 39°C üzerinde ölçüldüğü için tam kan sayımı, C-reaktif protein, biyokimya paneli ve periferik kan kültürü istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: WBC 13.400/mm³, CRP 18 mg/L, biyokimya normal. Kan kültüründe üreme olmadı ve sonuçlar tedavi seçimini değiştirmedi.",
                        "teaching_point": "Ateş odağı otoskopik muayene ile net olarak saptanmış, aşılı ve genel durumu iyi olan çocukta rutin kan tahlili ve kan kültürü endike değildir.",
                    },
                    {
                        "text": "Orta kulak boşluğundaki sıvıyı doğrulamak amacıyla acil serviste akustik timpanometri ve iki yönlü konvansiyonel mastoid grafisi istemek",
                        "is_correct": False,
                        "scenario_update": "Ağlayan çocukta timpanometri uyumsuzluğu yaşandı ve düz mastoid grafisi akut mukozal bulanıklık dışında klinik yönetimi değiştiren bir bilgi sağlamadı.",
                        "teaching_point": "Otoskopide belirgin bombeleşmiş ve hiperemik zar görüldüğünde tanı nettir; acil serviste rutin timpanometri veya konvansiyonel mastoid grafisi gerekmez.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Hastanın mevcut öykü ve otoskopik muayene bulgularıyla en olası tanınız nedir?",
                "options": [
                    {
                        "text": "Sağ Efüzyonlu Otitis Media",
                        "is_correct": False,
                        "scenario_update": "Hastada 39.1°C ateş, şiddetli akut kulak ağrısı ve timpanik membranda belirgin akut inflamasyon ile bombeleşme mevcuttur.",
                        "teaching_point": "Efüzyonlu otitis mediada orta kulakta sıvı veya hava-sıvı seviyesi vardır ancak akut ateş, şiddetli otalji ve belirgin bombeleşme bulunmaz.",
                    },
                    {
                        "text": "Sağ Akut Otitis Eksterna",
                        "is_correct": False,
                        "scenario_update": "Dış kulak yolu ödemli veya eritemli olmayıp inflamasyon ve bombeleşme doğrudan timpanik membran ile orta kulak kaynaklıdır.",
                        "teaching_point": "Akut otitis eksterna dış kulak yolu enfeksiyonudur; dış kulak yolu ödemli ve döküntülüdür, tragus basısı belirgin ağrılıdır.",
                    },
                    {
                        "text": "Sağ Akut Otitis Media",
                        "is_correct": True,
                        "explanation": "Üst solunum yolu enfeksiyonu sonrası akut başlayan otalji, yüksek ateş ve timpanik membranda belirgin bombeleşme Akut Otitis Media tanısını koydurur.",
                        "new_finding": "Tanı: Sağ Akut Otitis Media (AOM) olarak kesinleştirildi.",
                    },
                    {
                        "text": "Sağ Akut Koalesan Mastoidit",
                        "is_correct": False,
                        "scenario_update": "Muayenede kulak kepçesinin öne ve aşağı itilmesi, postauriküler sulkusun silinmesi veya mastoid üzerinde fluktuasyon saptanmadı.",
                        "teaching_point": "Akut mastoidit tanısı için otitis media bulgularına ek olarak postauriküler eritem, ödem, hassasiyet ve aurikulanın öne-aşağı yer değiştirmesi gerekir.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Son 30 günde antibiyotik kullanımı ve eşlik eden pürülan konjonktiviti olmayan 22 aylık bu hastada ilk basamak tedavi ne olmalıdır?",
                "options": [
                    {
                        "text": "Yüksek doz oral Amoksisilin (80-90 mg/kg/gün, 10 gün), düzenli sistemik parasetamol veya ibuprofen ve 48-72 saatte kontrol önerisiyle taburculuk",
                        "is_correct": True,
                        "explanation": "AAP kılavuzuna göre 2 yaş altı veya şiddetli semptomlu (≥39°C ateş, orta-ağır otalji) AOM'de penisilin dirençli pnömokokları kapsamak için 80-90 mg/kg/gün amoksisilin (10 gün) ve etkin sistemik analjezi ilk tercihtir.",
                        "new_finding": "Yüksek doz oral amoksisilin ve düzenli ibuprofen/parasetamol başlandı; 48-72 saat içinde ateş veya ağrıda gerileme olmazsa tekrar başvuru eğitimi verilerek taburcu edildi.",
                    },
                    {
                        "text": "Standart doz oral Amoksisilin (40-45 mg/kg/gün, 5 gün) ile birlikte östaki ödemini çözmek amacıyla oral psödoefedrin ve setirizin şurup başlamak",
                        "is_correct": False,
                        "scenario_update": "Düşük doz ve kısa süreli antibiyotik tedavisiyle 48. saatte ateş ve kulak ağrısı gerilemedi; dekongestan ve antihistaminik ise huzursuzluğu artırdı.",
                        "teaching_point": "İki yaş altı ve ağır semptomlu AOM'de standart doz ve 5 günlük süre yetersizdir; ayrıca antihistaminik ve dekongestanların AOM iyileşmesinde hiçbir faydası yoktur.",
                    },
                    {
                        "text": "Antibiyotik başlamadan 48-72 saatlik tedbirsiz bekle-gör izlemi uygulamak ve ağrı için yalnızca dış kulak yoluna topikal siprofloksasin-deksametazon damla reçete etmek",
                        "is_correct": False,
                        "scenario_update": "Sağlam timpanik membrandan topikal damla orta kulağa geçemedi; 39.1°C ateşi ve şiddetli ağrısı olan 22 aylık çocukta klinik tablo ağırlaştı.",
                        "teaching_point": "Ateşi ≥39°C veya şiddetli otaljisi olan çocuklarda bekle-gör yaklaşımı uygulanmaz, hemen antibiyotik başlanır; sağlam zarda topikal antibiyotikli damlalar etkisizdir.",
                    },
                    {
                        "text": "H. influenzae ve M. catarrhalis olasılığı nedeniyle ilk basamakta doğrudan 3 gün intramüsküler Seftriakson (50 mg/kg/gün) enjeksiyonu ve antihistaminik başlamak",
                        "is_correct": False,
                        "scenario_update": "Oral alımı iyi olan ve son bir ayda antibiyotik kullanmayan çocukta gereksiz yere ağrılı parenteral geniş spektrumlu sefalosporin uygulanmış oldu.",
                        "teaching_point": "Parenteral seftriakson yalnızca kusma nedeniyle oral tedaviyi tolere edemeyen veya amoksisilin-klavulanat tedavisine 48-72 saatte yanıt vermeyen AOM vakalarında endikedir.",
                    },
                ],
            },
        ],
    },
    {
        "id": "G04",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "4 Yaş",
        "gender": "Kız",
        "complaint": "İshal, bulantı ve 2 kez kusma",
        "history": (
            "Annesi anlatıyor: 'Dün akşamdan beri 2 kez kustu, bugün de 4 kez sulu, kötü kokulu ama kansız "
            "dışkılaması oldu. Karnım ağrıyor diyor, tuvalete çıkınca biraz rahatlıyor. Su ve ayran içebiliyor, "
            "en son 2 saat önce çişini yaptı. Ateşi 37.6°C civarında.'"
        ),
        "final_diagnosis": "Dehidratasyonsuz / Hafif Akut Gastroenterit (AGE)",
        "disposition": "Yeşil Alandan Oral Rehidratasyon, Uygun Beslenme ve Çinko Desteği ile Taburculuk",
        "case_pearl": (
            "Kanlı dışkılama, yüksek ateş, uzamış seyir veya orta-ağır dehidratasyon bulgusu olmayan akut "
            "gastroenteritlerde rutin gaita mikroskopisi/kültürü veya kan biyokimyası gerekmez. Tedavinin temeli her "
            "kayıp sonrası oral rehidratasyon sıvısı (ORS), erken yaşa uygun beslenme ve çinko desteğidir; "
            "antimotilite ilaçları (loperamid vb.) çocuklarda kontrendikedir."
        ),
        "steps": [
            {
                "stage_title": "Hidrasyon ve Fizik Muayene Değerlendirmesi",
                "question": "Akut kusma ve sulu dışkılaması olan bu çocukta ilk aşamada en kritik klinik değerlendirme hangisidir?",
                "options": [
                    {
                        "text": "Dehidratasyon gelişmesini beklemeksizin hemen periferik damar yolu açarak 20 mL/kg izotonik sodyum klorür solüsyonunu 30 dakikada hızlı infüzyonla vermek",
                        "is_correct": False,
                        "scenario_update": "Klinik olarak sıvı açığı bulunmayan ve ağızdan sıvı alabilen çocukta gereksiz invaziv kateterizasyon ve parenteral izotonik sıvı yüklemesi yapıldı.",
                        "teaching_point": "Yirmi mL/kg izotonik kristaloid bolusu yalnızca hipovolemik şok, ağır dehidratasyon veya oral rehidratasyonu tolere edemeyen orta-ağır dehidratasyon tablolarında uygulanır.",
                    },
                    {
                        "text": "Karın ağrısı tarif edildiği için fizik muayene öncesinde intestinal obstrüksiyonu değerlendirmek amacıyla ayakta direkt batın grafisi ve ultrasonografi istemek",
                        "is_correct": False,
                        "scenario_update": "Görüntülemede non-spesifik ince bağırsak gaz-sıvı seviyeleri dışında patoloji saptanmadı; çocuk gereksiz radyasyona maruz kaldı ve değerlendirme süresi uzadı.",
                        "teaching_point": "Safralı kusma, batın distansiyonu, kanlı dışkılama veya peritonit bulgusu olmayan tipik kusma-ishal başvurularında radyolojik görüntüleme endike değildir.",
                    },
                    {
                        "text": "Ağızdan sıvı alımını değerlendirmeden bulantıyı hızla kesmek amacıyla ilk basamakta intramüsküler metoklopramid enjeksiyonu uygulayıp hastayı acil gözlem odasına almak",
                        "is_correct": False,
                        "scenario_update": "Enjeksiyon sonrası çocukta boyun kaslarında istemsiz kasılma ve bakış kayması ile karakterize akut distonik reaksiyon gelişme riski ortaya çıktı.",
                        "teaching_point": "Çocuklarda metoklopramid gibi dopamin antagonistleri ekstrapiramidal yan etkiler nedeniyle önerilmez; kusması hafif ve oral alabilen hastada rutin antiemetik gerekmez.",
                    },
                    {
                        "text": "Klinik Dehidratasyon Ölçeği kapsamında genel görünüm, göz küreleri, mukoza ıslaklığı, gözyaşı, deri turgoru, kapiller dolum ve batın muayenesini yapmak",
                        "is_correct": True,
                        "explanation": "Akut kusma ve ishal yönetiminde tetkik ve tedavi kararlarını belirleyen en önemli basamak dehidratasyon derecesinin ve cerrahi batının klinik olarak değerlendirilmesidir.",
                        "new_finding": "Vital Bulgular: Ateş 37.5°C, KTA 102/dk, SS 22/dk, TA 95/60 mmHg. Çocuk aktif, etrafla ilgili. Göz küreleri normal, ağız mukozası nemli, ağlarken gözyaşı var. Deri turgoru normal, kapiller dolum <2 saniye. Batın yumuşak, bağırsak sesleri hafif artmış, defans veya rebound yok.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik İstem Kararı",
                "question": "Dehidratasyon bulgusu olmayan, kansız-mukussuz dışkılaması olan ve oral sıvı alabilen bu hastada hangi tetkikler istenmelidir?",
                "options": [
                    {
                        "text": "Taze dışkı örneğinden direkt mikroskopi, gaita kültürü, parazit incelemesi ve Clostridium difficile toksin A/B tarama testlerini birlikte istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: Gaita mikroskopisinde lökosit veya eritrosit görülmedi, parazit kist/trofozoiti saptanmadı; kültür sonucunun ise 72 saat sonra çıkacağı bildirildi.",
                        "teaching_point": "Gaita mikroskopisi ve kültürü yalnızca kanlı-mukuslu dışkılama, yüksek ateşli toksik görünüm, immün yetmezlik veya uzamış ishal varlığında endikedir.",
                    },
                    {
                        "text": "Herhangi bir kan veya dışkı tetkiki istemeden, acil serviste ağızdan sıvı toleransını gözlemleyerek klinik tanı ile ilerlemek",
                        "is_correct": True,
                        "explanation": "Dehidratasyon bulgusu, yüksek ateşi ve kanlı dışkılaması olmayan akut sulu ishal tablolarında kan biyokimyası veya dışkı tetkiki yönetimi değiştirmez.",
                        "new_finding": "Tetkik istenmedi; çocuğa acil serviste deneme amaçlı küçük yudumlarla oral rehidratasyon sıvısı verildi ve kusmadan rahatça tolere ettiği görüldü.",
                    },
                    {
                        "text": "Gizli elektrolit dengesizliğini ve metabolik asidozu saptamak için venöz kan gazı, üre, kreatinin, sodyum, potasyum ve hemogram istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: Na 138 mEq/L, K 4.3 mEq/L, Üre 22 mg/dL, Kreatinin 0.4 mg/dL, pH 7.39, HCO3 22 mmol/L. Tüm değerler normal geldi.",
                        "teaching_point": "Serum elektrolitleri, böbrek fonksiyonları ve kan gazı yalnızca orta-ağır dehidratasyon, intravenöz sıvı gereksinimi veya hipernatremi/hiponatremi şüphesinde istenir.",
                    },
                    {
                        "text": "Gaita rotavirüs ve adenovirüs hızlı antijen testi ile birlikte akut faz reaktanlarını göndererek viral etkeni kesinleştirmek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: Rotavirüs antijeni negatif, adenovirüs antijeni zayıf pozitif, CRP 6.4 mg/L saptandı; ancak sonuçlar rehidratasyon ve beslenme planını değiştirmedi.",
                        "teaching_point": "Ayaktan izlenecek hafif sulu ishalde viral antijen testleri ve akut faz reaktanları tedavi yaklaşımını değiştirmediğinden rutin olarak önerilmez.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu hastada mevcut anamnez ve fizik muayene bulgularıyla en uygun klinik tanı nedir?",
                "options": [
                    {
                        "text": "Akut Bakteriyel Dizanteri (Shigelloz)",
                        "is_correct": False,
                        "scenario_update": "Hastada yüksek ateş, tenezm, şiddetli sol alt kadran hassasiyeti veya kanlı-mukuslu dışkılama bulunmamaktadır.",
                        "teaching_point": "Bakteriyel dizanteri tablosunda yüksek ateş, kramp tarzı şiddetli karın ağrısı, tenezm ve küçük hacimli kanlı-mukuslu dışkılama görülür.",
                    },
                    {
                        "text": "Akut Gastroenterit ve Ağır Dehidratasyon",
                        "is_correct": False,
                        "scenario_update": "Hastanın bilinci açık, göz küreleri ve deri turgoru normal, mukozaları ıslak ve kapiller dolum zamanı 2 saniyenin altındadır.",
                        "teaching_point": "Ağır dehidratasyonda letarji, çökük göz küreleri, gözyaşı yokluğu, çadırlaşan deri turgoru, taşikardi ve uzamış kapiller dolum zamanı saptanır.",
                    },
                    {
                        "text": "Dehidratasyonsuz Akut Viral Gastroenterit",
                        "is_correct": True,
                        "explanation": "Kansız sulu dışkılama, subfebril ateş, korunmuş oral alım ve normal hidrasyon muayenesi dehidratasyonsuz akut viral gastroenterit ile uyumludur.",
                        "new_finding": "Tanı: Dehidratasyonsuz Akut Gastroenterit (AGE) olarak kesinleştirildi.",
                    },
                    {
                        "text": "Akut Apandisit (Pelvik Yerleşimli)",
                        "is_correct": False,
                        "scenario_update": "Pelvik apandisit irritatif ishal yapabilse de hastada sürekli ilerleyen karın ağrısı, ateş yüksekliği, iştahsızlık ve lokalize defans/rebound yoktur.",
                        "teaching_point": "Pelvik yerleşimli apandisitte dışkılama sonrası rahatlamayan persistan ağrı, yüksek ateş ve suprapubik/sağ alt kadran hassasiyeti ön plandadır.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Beslenme Planı",
                "question": "Bu hastanın evdeki tedavi ve beslenme planı için güncel kılavuzlara göre en doğru yaklaşım hangisidir?",
                "options": [
                    {
                        "text": "Her sulu dışkılama sonrası düşük osmolariteli Oral Rehidratasyon Sıvısı (10 mL/kg), yaşa uygun normal beslenme, çinko desteği ve aile eğitimi",
                        "is_correct": True,
                        "explanation": "ESPGHAN ve WHO rehberlerine göre temel yaklaşım devam eden kayıpların düşük osmolariteli ORS ile yerine konması, katı diyet kısıtlaması yapılmadan yaşa uygun beslenmenin sürdürülmesi ve çinko/probiyotik desteğidir.",
                        "new_finding": "ORS kullanım şeması, yaşa uygun beslenme önerileri ve tekrar başvuru kriterleri (dirençli kusma, idrar azalması, kanlı dışkı, uykuya meyil) anlatılarak taburcu edildi.",
                    },
                    {
                        "text": "Dışkılama sayısını hızla azaltmak için oral loperamid damla ve ampirik metronidazol süspansiyon başlamak, bağırsağı dinlendirmek için 24 saat katı gıdayı kesmek",
                        "is_correct": False,
                        "scenario_update": "Loperamid verilen çocukta bağırsak motilitesi durarak paralitik ileus ve batın distansiyonu gelişti; aç bırakılması ise enterosit yenilenmesini geciktirdi.",
                        "teaching_point": "Çocuklarda loperamid gibi antimotilite ilaçları paralitik ileus, toksik megakolon ve bakteriyel translokasyon riski nedeniyle kesinlikle kontrendikedir; ayrıca bağırsak dinlendirme diyeti önerilmez.",
                    },
                    {
                        "text": "Sıvı ve enerji kaybını karşılamak amacıyla hazır meyve suları veya gazlı içecekler önermek ve yalnızca haşlanmış patates-pirinç lapası diyeti uygulamak",
                        "is_correct": False,
                        "scenario_update": "Yüksek karbonhidrat ve osmolarite içeren meyve suları lümen içine su çekerek ozmotik ishali şiddetlendirdi; kısıtlı diyet ise kalori açığına yol açtı.",
                        "teaching_point": "Hazır meyve suları ve gazlı içecekler yüksek osmolarite ve düşük sodyum içerdiğinden ozmotik ishali artırır; kısıtlayıcı BRAT diyeti de artık önerilmemektedir.",
                    },
                    {
                        "text": "Oral alımı tamamen kesip 12 saat acil gözlemde %5 Dekstroz + %0.2 NaCl (1/5 izotonik) idame sıvısı ve siprofloksasin başlamak",
                        "is_correct": False,
                        "scenario_update": "Oral alabilen hastada gereksiz yatış yapıldı; hipotonik sıvı infüzyonu hiponatremi riskini artırdı ve viral tabloda florokinolon kullanımı uygunsuz oldu.",
                        "teaching_point": "Dehidratasyonsuz hastada parenteral sıvı verilmez; İV sıvı gerektiğinde de hiponatremi riski nedeniyle %0.2 NaCl gibi aşırı hipotonik sıvılar tercih edilmemelidir.",
                    },
                ],
            },
        ],
    },
    {
        "id": "G05",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "5 Yaş",
        "gender": "Erkek",
        "complaint": "Aralıklı karın ağrısı ve dışkılama güçlüğü",
        "history": (
            "Annesi anlatıyor: '2 gündür ara sıra karnını tutup ağrıyor diyor, özellikle yemeklerden sonra kramp gibi "
            "gelip 5-10 dakika içinde geçiyor, sonra oyununa devam ediyor. Ateşi ve kusması hiç olmadı. Anaokuluna "
            "başladığından beri okul tuvaletine gitmek istemiyor, 4-5 günde bir çok sert ve kalın kaka yapıyor, bazen "
            "kakasını tutmak için bacaklarını çaprazlıyor.'"
        ),
        "final_diagnosis": "Fonksiyonel Kabızlık (Konstipasyon) ve Buna Bağlı Kolik Karın Ağrısı",
        "disposition": "Yeşil Alandan Fekal İmpaksiyon Çözümü / Osmotik Laksatif ve Tuvalet Eğitimi ile Taburculuk",
        "case_pearl": (
            "Çocuk acile akut veya tekrarlayan karın ağrısı ile başvuran hastaların en sık nedenlerinden biri "
            "fonksiyonel kabızlıktır. Organik kırmızı bayraklar (ilk 48 saatte mekonyum çıkaramama, büyüme geriliği, "
            "safralı kusma, perianal fistül, sakral/nörolojik bulgu) yoksa Roma IV kriterleriyle klinik tanı konur; "
            "polietilen glikol veya laktüloz ile davranışsal tuvalet eğitimi başlanır."
        ),
        "steps": [
            {
                "stage_title": "Öykü ve Fizik Muayene",
                "question": "Bu hastada organik nedenleri ve cerrahi akut batını dışlamak için fizik muayenede nasıl bir yaklaşım izlemelisiniz?",
                "options": [
                    {
                        "text": "Ağrılı muayeneden kaçınmak amacıyla dış perianal inspeksiyon yapmadan her çocukta rutin rektal tuşe uygulamak ve organik patoloji için rektal biyopsi planlamak",
                        "is_correct": False,
                        "scenario_update": "Beş yaşındaki çocukta ilk basamakta yapılan rutin rektal tuşe ciddi korku ve travmaya yol açarak dışkı tutma davranışını daha da pekiştirdi.",
                        "teaching_point": "Tipik dışkı tutma öyküsü ve palpabl fekal kitlesi olan çocuklarda rutin rektal tuşe önerilmez; öncelikle atravmatik dış perianal ve sakral inspeksiyon yapılmalıdır.",
                    },
                    {
                        "text": "Karın ağrısı nedeniyle fizik muayeneyi beklemeden hastanın oral alımını kesip cerrahi akut batın ön tanısıyla acil çocuk cerrahisi konsültasyonu istemek",
                        "is_correct": False,
                        "scenario_update": "Ateşi, kusması ve peritonit bulgusu olmayan, ağrı atakları dışında aktif oyun oynayan çocukta cerrahi ekip tarafından akut batın düşünülmedi.",
                        "teaching_point": "Yemek sonrası gastrokolik refleksle tetiklenen, kısa süren ve aralarında çocuğun tamamen iyi olduğu kramp tarzı ağrılarda öncelikle dikkatli batın palpasyonu yapılmalıdır.",
                    },
                    {
                        "text": "Büyüme persentillerini, batın palpasyonuyla fekal kitle ve defans/rebound varlığını, lumbosakral bölgeyi, alt ekstremite reflekslerini ve perianal dış inspeksiyonu değerlendirmek",
                        "is_correct": True,
                        "explanation": "Dışkılama güçlüğü ve karın ağrısında cerrahi batın dışlanmalı, sol alt kadranda fekal kitle, perianal fissür ve nörojenik nedenler için lumbosakral bölge kontrol edilmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 36.7°C, KTA 92/dk. Tartı ve boy 50. persentilde. Batın yumuşak, defans veya rebound yok; sol alt kadranda ve suprapubik bölgede palpasyonla hareketli sert fekal kitleler ele geliyor. Perianal dış inspeksiyonda saat 6 hizasında yüzeyel anal fissür mevcut. Lumbosakral bölge ve alt ekstremite nörolojik muayenesi doğal.",
                    },
                    {
                        "text": "Batın ve perianal bölge muayenesini atlayıp ağrıyı hızla kesmek amacıyla doğrudan acil serviste yüksek basınçlı rektal sodyum fosfat lavmanı uygulamak",
                        "is_correct": False,
                        "scenario_update": "Anal fissür varlığı görülmeden yapılan rektal lavman işlemi sırasında çocuk şiddetli ağrı duydu ve işlem tamamlanamadan rektal mukozal tahriş gelişti.",
                        "teaching_point": "Fizik muayene ve perianal inspeksiyon tamamlanmadan körlemesine rektal müdahale yapılmamalıdır; anal fissür varlığında rektal işlemler ağrı-tutma döngüsünü ağırlaştırır.",
                    },
                ],
            },
            {
                "stage_title": "Tetkik İstem Kararı",
                "question": "Okulda dışkı tutma öyküsü olan, muayenede sol alt kadranda fekalom ve anal fissür saptanan, kırmızı bayrak bulgusu bulunmayan bu çocukta tetkik yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Kolondaki dışkı yükünü objektif olarak derecelendirmek için rutin ayakta direkt batın grafisi ve tüm batın ultrasonografisi birlikte istemek",
                        "is_correct": False,
                        "scenario_update": "RADYOLOJİ SONUCU: Direkt grafide kolon çerçevesi boyunca yoğun fekal materyal izlendi, serbest hava yok. Çocuğa tanı değiştirmeyen iyonize radyasyon verildi.",
                        "teaching_point": "Öykü ve fizik muayene ile fekal birikim net olarak saptandığında rutin direkt batın grafisi tanısal ek katkı sağlamaz ve gereksiz radyasyon maruziyetidir.",
                    },
                    {
                        "text": "Sekonder metabolik ve endokrin nedenleri acil serviste taramak amacıyla serbest T4, TSH, çölyak serolojisi, kalsiyum ve ter testi istemek",
                        "is_correct": False,
                        "scenario_update": "LABORATUVAR SONUCU: Kalsiyum 9.6 mg/dL, TSH 2.1 mIU/L, sT4 normal; çölyak antikorlarının ise günler sonra çıkacağı bildirildi. Acil yönetimi değişmedi.",
                        "teaching_point": "Büyüme gelişmesi normal olan ve okula başlama sonrası dışkı tutma davranışıyla ortaya çıkan tablolarda acil serviste rutin endokrin veya çölyak taraması önerilmez.",
                    },
                    {
                        "text": "Distal kolondaki geçiş zonunu ve aganglionik segmenti dışlamak amacıyla acil baryumlu kolon grafisi ve anorektal manometri tetkiki planlamak",
                        "is_correct": False,
                        "scenario_update": "Doğumdan sonraki ilk 24 saatte mekonyum çıkaran ve 5 yaşına kadar normal dışkılayan çocukta ileri invaziv tetkik istemi uygun bulunmadı.",
                        "teaching_point": "Baryumlu kolon grafisi ve manometri yalnızca yenidoğan döneminden beri süren dirençli dışkılama güçlüğü, büyüme geriliği veya kırmızı bayrak varlığında düşünülür.",
                    },
                    {
                        "text": "Herhangi bir radyolojik görüntüleme veya laboratuvar tetkiki istemeden, mevcut öykü ve fizik muayene bulgularıyla klinik tanı koymak",
                        "is_correct": True,
                        "explanation": "Uluslararası pediatrik gastroenteroloji rehberlerine göre tipik dışkı tutma öyküsü ve muayene bulgusu olan, kırmızı bayrağı bulunmayan çocuklarda rutin radyografi veya kan tetkiki önerilmez.",
                        "new_finding": "Gereksiz radyasyon ve kan alımından kaçınılarak klinik tanı ile doğrudan tedavi planlamasına geçildi.",
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu hastada mevcut anamnez ve fizik muayene bulgularıyla en olası tanınız nedir?",
                "options": [
                    {
                        "text": "Fonksiyonel Kabızlık ve Anal Fissür",
                        "is_correct": True,
                        "explanation": "Okulda tuvalet erteleme, ağrılı sert dışkılama, anal fissür gelişimi ve ağrı korkusuyla dışkı tutma kısır döngüsü Roma IV kriterlerine göre fonksiyonel kabızlık tanısını koydurur.",
                        "new_finding": "Tanı: Fonksiyonel Kabızlık (Konstipasyon) ve Sekonder Anal Fissür olarak kesinleştirildi.",
                    },
                    {
                        "text": "Hirschsprung Hastalığı (Konjenital Aganglionik Megakolon)",
                        "is_correct": False,
                        "scenario_update": "Anamnezde bebeğin doğumdan sonraki ilk 24 saatte mekonyum çıkardığı, büyümesinin normal olduğu ve büyük kalibreli dışkıladığı görüldü.",
                        "teaching_point": "Hirschsprung hastalığı yenidoğan döneminde başlar, ilk 48 saatte mekonyum çıkışı gecikir, dışkı tutma davranışı yoktur ve rektum genellikle boştur.",
                    },
                    {
                        "text": "İleokolik İnvajinasyon (İntususepsiyon)",
                        "is_correct": False,
                        "scenario_update": "Hastada letarji atakları, safralı kusma, kanlı-mukuslu dışkılama veya sağ üst kadranda sucukvari kitle bulunmamaktadır.",
                        "teaching_point": "İnvajinasyon çoğunlukla 3 ay - 3 yaş arasında görülür ve şiddetli kıvrandırıcı ağrı-letarji periyotları ile seyreder.",
                    },
                    {
                        "text": "İnek Sütü Proteini Alerjisi",
                        "is_correct": False,
                        "scenario_update": "Beş yaşına kadar süt ürünlerini sorunsuz tüketen, atopi öyküsü olmayan ve anaokuluna başlayınca tuvalet tutan çocukta alerjik proktokolit düşünülmedi.",
                        "teaching_point": "İnek sütü proteini alerjisine bağlı kabızlık daha çok süt çocukluğu ve erken çocukluk döneminde, diğer atopik bulgularla veya standart tedaviye dirençli vakalarda görülür.",
                    },
                ],
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu hastada ağrılı dışkılama-tutma kısır döngüsünü kırmak ve tekrarı önlemek için en doğru tedavi planı nedir?",
                "options": [
                    {
                        "text": "Acil serviste tek seferlik rektal fosfat lavmanı uygulayıp bağırsağı boşaltmak ve idame laksatif başlamadan yalnızca posalı diyet önerisiyle eve göndermek",
                        "is_correct": False,
                        "scenario_update": "İdame osmotik laksatif ve fissür bakımı verilmediği için çocuk 4 gün sonra tekrar dışkısını tuttu ve şiddetli karın ağrısıyla acile geri başvurdu.",
                        "teaching_point": "Fonksiyonel kabızlıkta yalnızca rektumu bir kez boşaltmak yetmez; rektum tonusu ve ağrısız dışkılama alışkanlığı yerleşene kadar en az 2 ay idame osmotik laksatif şarttır.",
                    },
                    {
                        "text": "Oral osmotik laksatif (Polietilen glikol veya Laktüloz), anal fissür için sıcak oturma banyosu ve bariyer krem, yemek sonrası tuvalet oturuşu",
                        "is_correct": True,
                        "explanation": "ESPGHAN/NASPGHAN kılavuzlarına göre hem fekal impaksiyonun çözümü hem de idame tedavide ilk tercih oral Polietilen Glikol (PEG) veya yoksa Laktüloz, fissür bakımı ve yemek sonrası 5-10 dakika tuvalet oturuşu eğitimidir.",
                        "new_finding": "Oral osmotik laksatif, anal fissür için sıcak oturma banyosu/topikal bakım ve gastrokolik refleksten yararlanan davranışsal tuvalet takvimi anlatılarak hasta taburcu edildi.",
                    },
                    {
                        "text": "Kolik karın ağrısını hızla kesmek için oral trimebutin veya antikolinerjik spazmolitik şurup başlamak ve haftada iki kez senna çayı önermek",
                        "is_correct": False,
                        "scenario_update": "Verilen antikolinerjik spazmolitik ilaç bağırsak motilitesini daha da yavaşlatarak fekal retansiyonu ve karın ağrısı ataklarını şiddetlendirdi.",
                        "teaching_point": "Kabızlığa bağlı kolik karın ağrısında antikolinerjik spazmolitikler motiliteyi azaltarak tabloyu kötüleştirir; ilk basamakta uyarıcı bitkisel laksatifler de tercih edilmez.",
                    },
                    {
                        "text": "Ağızdan sıvı parafin (mineral yağ) ve gliserin fitil başlayıp, okul döneminde tuvalet eğitimini erteleyerek çocuğun bez bağlamasına geri dönmesini önermek",
                        "is_correct": False,
                        "scenario_update": "Beş yaşındaki çocukta bez bağlamaya geri dönülmesi psikolojik regresyona yol açtı ve düzenli tuvalet oturuşu alışkanlığı kazanılamadı.",
                        "teaching_point": "Beş yaşındaki çocukta amaç ağrısız yumuşak dışkılama sağlayarak yemeklerden 20-30 dakika sonra ayakları destekli şekilde klozete oturma alışkanlığı kazandırmaktır.",
                    },
                ],
            },
        ],
    },
]
