# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - Y31-Y35 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "Y31",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "2 Yaş",
        "gender": "Erkek",
        "complaint": "Bezinde aniden başlayan, ağrısız, yoğun vişne çürüğü ve parlak kırmızı renkli rektal kanama ile solukluk",
        "history": (
            "Ailesi daha önce sağlıklı olan 2 yaşındaki erkek çocuğu bezinde yoğun kanama fark ederek Sarı Alana getiriyor: "
            "'Yaklaşık iki saat önce altını değiştirirken bezinin tamamen taze kırmızı ve vişne çürüğü renkli kanla kaplandığını "
            "gördük. Çocuğun hiçbir karın ağrısı kıvranması, ağlama nöbeti veya kusması olmadı. Bir saat sonra bezinde tekrar "
            "bol miktarda pıhtılı kanama oldu ve ten rengi belirgin şekilde soldu.'"
        ),
        "final_diagnosis": "Meckel Divertikülü Kanaması (Ektopik Gastrik Mukoza Ülserasyonu)",
        "disposition": "Sarı Alanda İV Damar Yolu + İzotonik Sıvı Resüsitasyonu + Kan Grubu ve Çapraz Karşılaştırma + Çocuk Cerrahisi Konsültasyonu ile Cerrahi Rezeksiyon İçin Yatış",
        "case_pearl": (
            "Meckel divertikülü, omfalomezenterik kanalın kapanma kusuru sonucu gelişen en sık konjenital gastrointestinal anomalidir "
            "('2'ler kuralı': toplumun %2'sinde görülür, ileoçekal valvden yaklaşık 2 fit proksimaldedir, 2 inç uzunluğundadır, "
            "sıklıkla 2 yaş altında semptom verir). En yaygın prezantasyon, ektopik mide mukozasından salgılanan aside bağlı komşu "
            "ileum mukozasında gelişen ağrısız, yoğun alt gastrointestinal sistem kanamasıdır (vişne çürüğü veya parlak kırmızı rektal kanama). "
            "Karın muayenesinde defans veya hassasiyet saptanmaz, batın tamamen rahattır. Tanıda altın standart yöntem Tc-99m perteknetat "
            "sintigrafisidir (Meckel sintigrafisi); ektopik gastrik mukoza perteknetatı tutarak sağ alt kadranda fokal aktivite artışı gösterir. "
            "Tedavi cerrahi kama rezeksiyonu veya divertikülektomidir."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Hemodinamik Stabilizasyon",
                "question": "Masif ağrısız rektal kanama, solukluk ve belirgin taşikardisi olan 2 yaşındaki bu hastada ilk yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Cerrahi konsültasyon öncesinde kanama odağını netleştirmek amacıyla hastaya nazogastrik tüp takıp bol miktarda soğuk serum fizyolojikle mide lavajı uygulamak",
                        "is_correct": False,
                        "scenario_update": "Nazogastrik lavajda berrak mide içeriği geldi, kanama izlenmedi ancak lavaj işlemi esnasında çocuk aşırı ajite olarak taşikardisi arttı.",
                        "teaching_point": "Ağrısız masif alt gastrointestinal kanamalı ve taşikardik çocuklarda ilk öncelik invaziv nazogastrik lavaj değil, acil damar yolu açılarak hemodinamik resüsitasyonun sağlanmasıdır.",
                    },
                    {
                        "text": "Geniş iki damar yolu açarak izotonik kristaloid bolusu başlatmak, tam kan sayımı, kan grubu ve çapraz karşılama göndermek",
                        "is_correct": True,
                        "explanation": "Masif kanamalı ve kompanse şok bulguları (taşikardi, solukluk) olan çocukta öncelik damar yolu güvenliği, hacim resüsitasyonu ve acil kan hazırlığıdır.",
                        "new_finding": "Vital bulgular: Ateş 36.8°C, KTA 155/dk, SS 28/dk, TA 88/52 mmHg, SpO2 %98, CRT 3 saniye. Batın muayenesi tamamen rahat, distansiyon, defans veya rebound yok. Rektal tuşede parlak kırmızı kan ve pıhtı izlendi, fissür saptanmadı. 20 mL/kg izotonik sonrası KTA 132/dk'ya geriledi.",
                    },
                    {
                        "text": "Kanamanın anal fissürden kaynaklanıp kaynaklanmadığını ayırt etmek amacıyla hastaya derin sedasyon vererek acil tanısal anoskopi ve rektoskopi yapmak",
                        "is_correct": False,
                        "scenario_update": "Derin sedasyon uygulanan hipovolemik çocukta kan basıncı 75/40 mmHg düzeyine geriledi ve anoskopide yalnızca proksimalden gelen yoğun kan görüldü.",
                        "teaching_point": "Hemodinamik resüsitasyon tamamlanmadan ve damar yolu açılmadan yapılan sedasyon ve endoskopik girişimler hipovolemik şoku derinleştirerek hayati risk oluşturur.",
                    },
                    {
                        "text": "Oral beslenmeyi açık tutarak koagülasyon parametreleri sonuçlanana kadar hastayı monitörize gözlem odasında izlemek ve oral demir damlası başlamak",
                        "is_correct": False,
                        "scenario_update": "Oral hidrasyon verilmeye çalışılırken hasta kustu, takip eden bezinde tekrar yoğun parlak kırmızı kanama oldu ve taşikardi 160/dk'ya yükseldi.",
                        "teaching_point": "Aktif masif gastrointestinal kanaması olan çocuklarda oral alım aspirasyon riski ve acil cerrahi olasılığı nedeniyle derhal kapatılmalı, parenteral hidrasyon verilmelidir.",
                    },
                ],
            },
            {
                "stage_title": "Laboratuvar Tetkikleri ve İleri Görüntüleme Yönteminin Belirlenmesi",
                "question": "Hemodinamisi stabilize edilen, ağrısız alt gastrointestinal kanaması ve rahat batın muayenesi olan çocukta öncelikli görüntüleme yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Kolon lümenindeki olası vasküler lezyonları doğrudan saptamak amacıyla bağırsak temizliği yapmadan acil tanısal ve terapotik kolonoskopi planlamak",
                        "is_correct": False,
                        "scenario_update": "Kolonda yoğun pıhtı ve taze kan bulunması nedeniyle mukozal yüzeyler net değerlendirilemedi ve kanama odağı tespit edilemedi.",
                        "teaching_point": "Masif alt gastrointestinal kanamalarda hazırlıksız acil kolonoskopinin tanısal değeri düşüktür; lümendeki kan mukozal vizualizasyonu engeller.",
                    },
                    {
                        "text": "Batın içi serbest havayı ve olası bağırsak perforasyonunu ekarte etmek amacıyla ayakta direkt batın ve sol lateral grafi çekmek",
                        "is_correct": False,
                        "scenario_update": "Direkt batın grafilerinde serbest hava veya obstrüksiyon bulgusu saptanmadı, tanıya ve klinik yönetime herhangi bir katkı sağlamadı.",
                        "teaching_point": "Ağrısız rektal kanamada perforasyon veya mekanik obstrüksiyon kliniği yoksa direkt grafilerin tanısal duyarlılığı ve yönetime katkısı son derece düşüktür.",
                    },
                    {
                        "text": "Ektopik mide mukozasını görüntülemek amacıyla nükleer tıp ünitesiyle koordine olarak teknesyum doksan dokuz em perteknetat sintigrafisi planlamak",
                        "is_correct": True,
                        "explanation": "Pediatrik yaş grubunda ağrısız masif alt gastrointestinal kanamanın en sık nedeni ektopik gastrik mukoza içeren konjenital anomalilerdir ve sintigrafi altın standarttır.",
                        "new_finding": "Laboratuvar: Hb 7.8 g/dL, Hct %23.8, BK 8.400/mm³, Trombosit 290.000/mm³, Koagülasyon testleri doğal. Sintigrafi: Sağ alt kadranda, mide mukozasıyla eş zamanlı perteknetat tutulumu gösteren fokal radyoaktivite artışı izlendi.",
                    },
                    {
                        "text": "İntususepsiyonu kesin olarak dışlamak amacıyla batın ultrasonografisi çekmek ve işlem esnasında hidrostatik redüksiyon için lavman hazırlığı yapmak",
                        "is_correct": False,
                        "scenario_update": "Batın ultrasonografisinde hedef tahtası görünümü saptanmadı, lavman hazırlığı gereksiz zaman kaybına ve mukozal irritasyona yol açtı.",
                        "teaching_point": "Ağrısız, vişne çürüğü kanamalarda ve rahat batın muayenesinde intususepsiyon ön planda düşünülmez; lavman uygulanması gereksiz ve zararlıdır.",
                    },
                ],
            },
            {
                "stage_title": "Klinik ve Sintigrafik Bulgularla Kesin Tanı",
                "question": "Ağrısız masif rektal kanama, derin anemi ve sintigrafide sağ alt kadranda ektopik mide mukozası saptanan hastada kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Meckel divertikülü kanaması",
                        "is_correct": True,
                        "explanation": "İki yaş altı çocukta ağrısız masif vişne çürüğü rektal kanama ve sintigrafide ektopik gastrik mukoza tespiti Meckel divertikülü kanamasını kesinleştirir.",
                        "new_finding": "Kesin tanı: Meckel divertikülü kanaması (ektopik gastrik mukoza zemininde gelişen ileal ülser kanaması).",
                    },
                    {
                        "text": "İleokolik invajinasyon",
                        "is_correct": False,
                        "scenario_update": "İnvajinasyonda kolik tarzı aralıklı şiddetli karın ağrısı, safralı kusma ve palpabl kitle beklenir; sintigrafide ektopik mukoza tutulumu olmaz.",
                        "teaching_point": "Ağrısız masif vişne çürüğü kanama invajinasyondan ziyade Meckel divertikülü kanaması için karakteristiktir.",
                    },
                    {
                        "text": "Juvenil rektal polip",
                        "is_correct": False,
                        "scenario_update": "Juvenil polipler genellikle dışkılamanın sonunda damlama şeklinde parlak kırmızı kanama yapar ve masif anemiye nadiren yol açar.",
                        "teaching_point": "Rektal polipler masif vişne çürüğü kanama veya ektopik gastrik mukoza sintigrafi pozitifliği göstermez.",
                    },
                    {
                        "text": "Nekrotizan enterokolit",
                        "is_correct": False,
                        "scenario_update": "Nekrotizan enterokolit prematüre yenidoğanlarda distandü batın, safralı kusma ve pnömatozis intestinalis ile seyreder; 2 yaşında beklenmez.",
                        "teaching_point": "Nekrotizan enterokolit yenidoğan dönemine özgü bir tablodur; 2 yaşındaki sağlıklı çocukta ağrısız kanama nedeni değildir.",
                    },
                ],
            },
            {
                "stage_title": "Cerrahi Konsültasyon ve Kesin Tedavi Yönetimi",
                "question": "Meckel divertikülü kanaması tanısı kesinleşen ve anemisi olan 2 yaşındaki bu hastanın acil servisteki nihai yönetim planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Kanama kendiliğinden durduğu için oral proton pompa inhibitörü ve demir damlası reçete ederek hastayı cerrahi poliklinik kontrolüne yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Taburcu edilmesi planlanan hastada üç saat sonra tekrar masif rektal kanama ve derin hipovolemik şok tablosu gelişti.",
                        "teaching_point": "Meckel divertikülü kanamaları aralıklı ve masif tekrarlayabilir; cerrahi rezeksiyon yapılmadan medikal tedaviyle taburcu edilemez.",
                    },
                    {
                        "text": "Cerrahi müdahale öncesinde gastrointestinal kanama odağını elektrokoterle yakmak amacıyla acil terapotik çift balonlu enteroskopi ünitesine derhal sevk etmek",
                        "is_correct": False,
                        "scenario_update": "İnvaziv enteroskopi esnasında ileum lümeni perfore oldu ve hasta acil laparatomiye alınmak zorunda kaldı.",
                        "teaching_point": "Meckel divertikülü kanamasında endoskopik hemostaz endike değildir; standart tedavi cerrahi rezeksiyondur.",
                    },
                    {
                        "text": "Kanamanın tekrarlamasını önlemek amacıyla traneksamik asit infüzyonu başlayarak hastayı çocuk gastroenteroloji servisinde yakın medikal izleme almak",
                        "is_correct": False,
                        "scenario_update": "Antifibrinolitik tedavi kanamayı geçici durdursa da anatomik anomaliyi çözmedi ve hastanede yatarken rekanalizasyonla kanama nüksetti.",
                        "teaching_point": "Ektopik gastrik mukozaya bağlı ülser kanamasında medikal tedaviler kesin çözüm sağlamaz; çocuk cerrahisi tarafından cerrahi eksizyon şarttır.",
                    },
                    {
                        "text": "Çocuk cerrahisi ile konsülte edilerek eritrosit süspansiyonu desteği eşliğinde acil cerrahi rezeksiyon için ameliyathaneye ve servise almak",
                        "is_correct": True,
                        "explanation": "Semptomatik Meckel divertikülünün kesin tedavisi cerrahidir (divertikülektomi veya segmental ileum rezeksiyonu); derin anemi için kan transfüzyonu eşlik etmelidir.",
                        "new_finding": "Eritrosit süspansiyonu transfüzyonu eşliğinde çocuk cerrahisi tarafından laparoskopik Meckel divertikülektomisi başarıyla uygulandı; hasta şifa ile taburcu edildi.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y32",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "12 Yaş",
        "gender": "Kız",
        "complaint": "Aniden başlayan, kıvrandırıcı sol alt kadran karın ağrısı ve tekrarlayan safrasız kusma",
        "history": (
            "12 yaşındaki kız hasta ailesi tarafından şiddetli karın ağrısı nedeniyle Sarı Alana getiriliyor: "
            "'Yaklaşık dört saat önce ders çalışırken sol kasığına bıçak saplanır gibi aniden başlayan çok şiddetli bir ağrı oldu. "
            "Ağrı dalgalar halinde geliyor, iki büklüm kıvranıyor ve arka arkaya üç kez mide içeriği kustu. "
            "Daha önce benzer bir ağrısı hiç olmamıştı, son adeti iki hafta önceydi ve idrar yaparken yanması yok.'"
        ),
        "final_diagnosis": "Akut Sol Over Torsiyonu (Adneksiyal Torsiyon)",
        "disposition": "Sarı Alanda Oral Stop + Damar Yolu + İV Hidrasyon + Analjezi + Acil Çocuk Cerrahisi ve Jinekoloji Konsültasyonu ile Laparoskopik Detorsiyon İçin Ameliyathaneye Yatış",
        "case_pearl": (
            "Over torsiyonu, over ve fallop tüpünün kendi vasküler pedikülü etrafında dönerek venöz staz, ödem ve takiben arteriyel iskemiye yol açtığı "
            "acil jinekolojik-cerrahi bir durumdur. Adölesan kızlarda aniden başlayan tek taraflı, şiddetli, kolik tarzda alt kadran ağrısı ve kusma ile prezante olur. "
            "Tanıda ilk tercih Renkli Doppler ultrasonografidir (stroması ödemli ve büyümüş over, periferik yerleşimli foliküller, vasküler pedikülde 'whirlpool' "
            "burgu işareti ve azalmış/kaybolmuş akım; akım izlenmesi torsiyonu ekarte ettirmez). Zaman over canlılığı için kritiktir; altın standart tedavi "
            "doku nekrotik görünse dahi ooferektomi değil, organ koruyucu acil laparoskopik detorsiyondur."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda Akut Alt Kadran Ağrılı Hastaya İlk Yaklaşım",
                "question": "Aniden başlayan şiddetli sol alt kadran ağrısı ve kusması olan 12 yaşındaki kız hastada ilk muayene ve stabilizasyon yaklaşımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Damar yolu açıp intravenöz hidrasyon ve analjezi sağlamak, batın muayenesinde peritoneal irritasyon ve pelvik kitle bulgularını incelemek",
                        "is_correct": True,
                        "explanation": "Akut batın kliniği olan hastada öncelikle hemodinamik stabilizasyon ve analjezi sağlanmalı, peritoneal bulgular ve pelvik kitle varlığı araştırılmalıdır.",
                        "new_finding": "Vital bulgular: Ateş 37.0°C, KTA 116/dk, SS 20/dk, TA 110/70 mmHg. Karın muayenesinde sol alt kadranda belirgin hassasiyet ve defans mevcut, sağ alt kadran rahat. Pelvik bölgede sol tarafta derin palpasyonla dolgunluk ve hassas kitle hissi alınıyor. İntravenöz parasetamol sonrası ağrının kıvrandırıcı şiddeti devam ediyor.",
                    },
                    {
                        "text": "Gastrointestinal spazmı rahatlatmak amacıyla antispazmodik ve antiemetik uygulayıp ağrı hafifleyene kadar fizik muayeneyi geciktirerek hastayı sakinleştirmek",
                        "is_correct": False,
                        "scenario_update": "Antispazmodik sonrası kusma baskılandı ancak sol alt kadrandaki kıvrandırıcı iskemi ağrısı ve peritonit bulguları hızla şiddetlendi.",
                        "teaching_point": "Akut cerrahi batın şüphesi olan hastalarda tanı konulmadan antispazmodik verilmesi tabloyu maskeleyebilir ve kritik cerrahi zaman penceresinin kaçırılmasına yol açar.",
                    },
                    {
                        "text": "Olası ektopik gebelik veya rüptüre korpus luteumu dışlamak amacıyla analjezik vermeden hastaya acil bimanual vajinal muayene yapmak",
                        "is_correct": False,
                        "scenario_update": "Virgo adölesan hastada gereksiz ve travmatik bimanual muayene girişimi şiddetli anksiyete ve ajitasyona yol açtı, tanısal fayda sağlamadı.",
                        "teaching_point": "Pediatrik ve adölesan grupta pelvik patolojilerin değerlendirilmesinde bimanual vajinal muayene rutin uygulanmaz; rektal veya non-invaziv transabdominal ultrasonografi tercih edilir.",
                    },
                    {
                        "text": "Ağrının renal kolik kaynaklı olduğunu düşünerek yüksek doz intramüsküler nonsteroid antiinflamatuar yapmak ve iki litre oral su içirmek",
                        "is_correct": False,
                        "scenario_update": "Oral sıvı alımı sonrası hasta tekrar safrasız mide içeriği kustu ve oral stop prensibi bozulduğu için anestezi hazırlığı gecikti.",
                        "teaching_point": "Akut batın şüpheli ve kusan hastalarda oral alım kesinlikle kesilmeli, renal kolik varsayımıyla cerrahi patolojiler atlanmamalıdır.",
                    },
                ],
            },
            {
                "stage_title": "Laboratuvar İncelemeleri ve İlk Basamak Radyolojik İnceleme",
                "question": "Sol alt kadranda hassas kitle ve peritoneal irritasyon saptanan adölesan kız hastada öncelikli tanısal görüntüleme yönteminiz ne olmalıdır?",
                "options": [
                    {
                        "text": "Peritoneal kalsifikasyon ve bağırsak obstrüksiyonunu dışlamak için acil ayakta direkt batın grafisi ve sol lateral dekübit grafi çekmek",
                        "is_correct": False,
                        "scenario_update": "Direkt batın grafilerinde sol alt kadranda nonspesifik yumuşak doku gölgesi dışında patoloji izlenmedi ve tanısal gecikme yaşandı.",
                        "teaching_point": "Direkt grafiler pelvik patolojilerin tanısında yetersizdir; yumuşak doku ve vasküler detay vermez.",
                    },
                    {
                        "text": "Pelvik patolojileri ve apandisiti aynı anda kesin olarak dışlamak amacıyla acil intravenöz kontrastlı tüm batın bilgisayarlı tomografisi çekmek",
                        "is_correct": False,
                        "scenario_update": "Bilgisayarlı tomografide sol pelvik bölgede kitle teyit edildi ancak adölesan hasta gereksiz yüksek doz gonadal iyonizan radyasyona maruz kaldı.",
                        "teaching_point": "Adölesan kızlarda akut pelvik ağrının ilk basamak görüntülemesi radyasyon içermeyen ultrasonografidir; BT ancak şüpheli veya komplike olgularda düşünülür.",
                    },
                    {
                        "text": "İnflamasyon belirteçlerini izlemek için tam kan sayımı ve CRP gönderip sonuçlar çıkana kadar radyolojik görüntüleme yapmadan beklemek",
                        "is_correct": False,
                        "scenario_update": "Sonuçlar beklenirken geçen iki saatte hastanın ağrısı dayanılmaz hale geldi ve gonadal dokunun iskemik süresi uzadı.",
                        "teaching_point": "Akut organ iskemisi şüphesinde laboratuvar sonuçları beklenmeden acil ultrasonografik görüntüleme organize edilmelidir; zaman doku canlılığı demektir.",
                    },
                    {
                        "text": "Radyasyon maruziyetinden kaçınarak sol pelvik bölgeyi ve kan akımını değerlendirmek için acil pelvik renkli Doppler ultrasonografi istemek",
                        "is_correct": True,
                        "explanation": "Pediatrik ve adölesan kızlarda akut pelvik kitle ve ağrının altın standart ilk basamak görüntülemesi pelvik renkli Doppler ultrasonografidir.",
                        "new_finding": "Laboratuvar: Lökosit 12.200/mm³, CRP 8 mg/L, beta-hCG negatif, TİT doğal. Renkli Doppler USG: Sol pelvik lojda 48x35 mm boyutlarında, stroması belirgin ödemli ve periferinde küçük kistik yapılar dizilmiş kitle izlendi. Vasküler pedikülde burgu görünümü saptandı ve arteriyel-venöz kan akımında ileri derecede azalma izlendi. Sağ taraf anatomik yapısı tamamen doğal.",
                    },
                ],
            },
            {
                "stage_title": "Klinik ve Doppler Bulguları ile Kesin Tanı",
                "question": "Büyümüş ve ödemli sol gonadal yapı, periferik foliküller ve pedikülde burgu işaretiyle akım kaybı saptanan hastada kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Rüptüre hemorajik over kisti",
                        "is_correct": False,
                        "scenario_update": "Hemorajik kist rüptüründe batında serbest sıvı ve kist kollapsı görülür; vasküler pedikülde burgu ve stromal büyüme izlenmez.",
                        "teaching_point": "Stromal ödem, belirgin büyüme ve vasküler burgu bulgusu kist rüptüründen ziyade torsiyona işaret eder.",
                    },
                    {
                        "text": "Pelvik inflamatuar hastalık",
                        "is_correct": False,
                        "scenario_update": "Pelvik inflamatuar hastalıkta bilateral hassasiyet, vajinal akıntı ve yüksek ateş beklenir; tek taraflı burgu işareti görülmez.",
                        "teaching_point": "Ani başlangıçlı tek taraflı kitle ve akım kaybı enfeksiyondan ziyade vasküler torsiyon ile uyumludur.",
                    },
                    {
                        "text": "Akut sol over torsiyonu",
                        "is_correct": True,
                        "explanation": "Adölesan kızda ani başlangıçlı alt kadran ağrısı, büyümüş ödemli parankim, periferik foliküller ve pedikülde burgu işareti akut over torsiyonu için patognomoniktir.",
                        "new_finding": "Kesin tanı: Akut sol over torsiyonu (sol adneksiyal torsiyon).",
                    },
                    {
                        "text": "Akut sol taraflı apandisit",
                        "is_correct": False,
                        "scenario_update": "Situs inversus veya sol yerleşimli apandisitte USG'de kör sonlanan tübüler yapı izlenir; pelvik kitle ve gonadal iskemi görülmez.",
                        "teaching_point": "Ultrasonografide sol gonadal stromanın büyümesi ve vasküler pedikülün dönmesi apandisit ile uyumlu değildir.",
                    },
                ],
            },
            {
                "stage_title": "Acil Cerrahi Tedavi ve Detorsiyon Yönetimi",
                "question": "Akut sol over torsiyonu tanısı kesinleşen 12 yaşındaki adölesan hastada gonadal rezervi korumaya yönelik en uygun cerrahi yaklaşım nedir?",
                "options": [
                    {
                        "text": "Dokunun iskemik ve nekrotik görünümde olma ihtimali nedeniyle zaman hiç kaybetmeden tek taraflı açık ooferektomi operasyonu planlamak",
                        "is_correct": False,
                        "scenario_update": "Detorsiyon denenmeden doğrudan ooferektomi yapılması adölesan hastanın gelecekteki over rezervini ve fertilitesini geri dönüşsüz olarak azalttı.",
                        "teaching_point": "Pediatrik ve adölesan torsiyonlarda over siyah/nekrotik görünse dahi doku reperfüzyon potansiyeli yüksektir; ilk tercih her zaman detorsiyondur.",
                    },
                    {
                        "text": "Çocuk cerrahisi ve jinekoloji ile acil laparoskopik detorsiyon planlayarak doku görünümünden bağımsız organ koruyucu yaklaşım uygulamak",
                        "is_correct": True,
                        "explanation": "Pediatrik torsiyonlarda altın standart, nekrotik görünümde dahi dokunun korunarak detorsiyon yapılması ve over canlılığının izlenmesidir.",
                        "new_finding": "Acil laparoskopide 720 derece torsiyone ve siyanotik sol over detorsiyone edildi; 15 dakika içinde pembeleşerek kan akımının geri döndüğü görüldü ve organ korundu.",
                    },
                    {
                        "text": "İntravenöz geniş spektrumlu antibiyotik ve antikoagülan başlayarak sol pelvik kitleyi yirmi dört saatlik konservatif takip altına almak",
                        "is_correct": False,
                        "scenario_update": "Konservatif takip altında geçen saatlerde over dokusunda tam hemorajik enfarktüs ve gangren gelişti, over kaybedildi.",
                        "teaching_point": "Torsiyon mekanik bir vasküler tıkanıklıktır; medikal tedavi ile düzelmez, gecikilen her saat over kaybı riskini katlar.",
                    },
                    {
                        "text": "Ağrı kesici infüzyonunu artırıp pelvik kist gerilemesini izlemek üzere hastayı acil servisten elektif jinekoloji polikliniğine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Taburcu edilmeye çalışılan hastada peritonit ve sepsis tablosu gelişti, acil laparatomi ile nekrotik doku rezeke edildi.",
                        "teaching_point": "Over torsiyonu acil cerrahi endikasyonudur; elektif poliklinik takibi yapılamaz.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y33",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "3 Yaş",
        "gender": "Erkek",
        "complaint": "Bir hafta önceki ishal sonrası giderek artan halsizlik, solukluk, açıklanamayan belirgin çarpıntı ve hızlı soluma",
        "history": (
            "3 yaşındaki erkek çocuk ailesi tarafından halsizlik ve hızlı nefes alıp verme şikayetiyle Sarı Alana getiriliyor: "
            "'Yaklaşık bir hafta önce hafif ateş ve sulu ishal geçirmişti, ishali düzeldi ancak son iki gündür yataktan kalkmak istemiyor, "
            "hiçbir şey yemiyor ve göğsü kuş gibi çok hızlı çarpıyor. Vücudunda belirgin bir ateş olmamasına rağmen kalbi durmaksızın "
            "çok hızlı atıyor ve emerken ya da su içerken hemen yorulup terliyor.'"
        ),
        "final_diagnosis": "Akut Viral Enfeksiyon Sonrası Miyokardit (Kardiyak Dekompanzasyon)",
        "disposition": "Sarı Alanda Oksijen + Damar Yolu + Sıvı Kısıtlaması + İnotropik Destek + Çocuk Kardiyoloji ve Çocuk Yoğun Bakım Ünitesine Acil Yatış",
        "case_pearl": (
            "Pediatrik miyokardit, sıklıkla geçirilmiş viral bir enfeksiyonu (enterovirus, adenovirus, parvovirus B19 vb.) takiben gelişen "
            "miyosit hasarı ve miyokard disfonksiyonudur. Ateş olmaksızın açıklanamayan persistan taşikardi, hepatomegali, galo ritmi ve takipne "
            "erken kalp yetersizliğinin kritik kırmızı bayraklarıdır. Telekardiyografide kardiyomegali ve pulmoner venöz konjesyon, EKG'de düşük "
            "voltaj veya ST-T değişiklikleri, Troponin I ve NT-proBNP yüksekliği tipiktir. Erken dönemde aşırı sıvı yüklemesinden kaçınılmalı "
            "(sıvı kısıtlaması), inotropik destek (milrinon, dopamin vb.) ve gerektiğinde mekanik dolaşım desteği (ECMO) için hasta hızla "
            "çocuk kardiyoloji yoğun bakımına yatırılmalıdır."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda Açıklanamayan Taşikardiye İlk Yaklaşım",
                "question": "Ateşi olmamasına rağmen belirgin taşikardisi ve solunum sıkıntısı olan 3 yaşındaki çocukta ilk muayene önceliğiniz ne olmalıdır?",
                "options": [
                    {
                        "text": "Taşikardiyi dehidratasyona bağlayarak hızla yirmi mililitre kilogram izotonik serum fizyolojiği yarım saat içinde intravenöz infüzyonla göndermek",
                        "is_correct": False,
                        "scenario_update": "Hızlı sıvı bolusu sonrası akciğerlerde raller arttı, karaciğer 5 cm'ye büyüdü ve hasta akut pulmoner ödeme girdi.",
                        "teaching_point": "Kardiyak disfonksiyona bağlı taşikardi ve hepatomegalisi olan çocuklara kontrolsüz sıvı bolusu verilmesi akut kalp yetersizliğini ağırlaştırır.",
                    },
                    {
                        "text": "Çocuğun huzursuzluğunu yatıştırmak amacıyla yüksek doz oral sedatif uygulayıp tam sakinleşmesini bekledikten sonra rutin fizik muayeneyi tamamlamak",
                        "is_correct": False,
                        "scenario_update": "Sedasyon uygulanan hastada solunum depresyonu ve hipoksi gelişti, zayıf olan hemodinamik kompanzasyon bozuldu.",
                        "teaching_point": "Açıklanamayan taşikardi ve taşipnesi olan çocukta sedasyon uygulanması solunum ve kardiyovasküler kollapsa zemin hazırlar.",
                    },
                    {
                        "text": "Havayolu ve solunumu destekleyip kalp seslerini, periferik nabızları, galo ritmini ve karaciğer boyutunu dikkatle muayene etmek",
                        "is_correct": True,
                        "explanation": "Ateşle orantısız taşikardisi olan çocukta kalp yetersizliği bulguları (S3 galo, hepatomegali, zayıf nabızlar) öncelikle taranmalıdır.",
                        "new_finding": "Vital bulgular: Ateş 37.1°C, KTA 170/dk (ritmik, zayıf dolgunlukta), SS 48/dk, TA 82/52 mmHg, SpO2 %92 (oda havasında), CRT 3.5 saniye. Kalp seslerinde belirgin taşikardi ve üçüncü kalp sesi (S3 galo ritmi) duyuldu, patolojik üfürüm yok. Solunum seslerinde bilateral bazallerde krepitan raller mevcut. Karaciğer kot kavsi altında 3.5 cm palpabl. Periferik nabızlar filiform.",
                    },
                    {
                        "text": "Solunum sıkıntısını bronkospazma bağlayarak ardışık üç doz nebulize salbutamol ve oral deksametazon başlayıp klinik yanıtı izlemek",
                        "is_correct": False,
                        "scenario_update": "Nebulize beta-agonist uygulaması sonrası hastanın kalp tepe atımı 195/dk'ya fırladı ve kardiyak iş yükü belirgin arttı.",
                        "teaching_point": "Pulmoner konjesyona bağlı ral ve taşipnesi olan olgularda astım tedavisi verilmesi taşikardiyi ve miyokardiyal oksijen tüketimini artırır.",
                    },
                ],
            },
            {
                "stage_title": "Kardiyovasküler İnceleme ve Laboratuvar Tetkik Planı",
                "question": "Galo ritmi, hepatomegali ve persistan taşikardisi saptanan bu hastada tanıya yönelik en uygun ilk tetkik kombinasyonu nedir?",
                "options": [
                    {
                        "text": "Gastrointestinal enfeksiyon odağını saptamak için gaita mikroskopisi, viral antijen paneli ve batın ultrasonografisi ile tetkik sürecini başlatmak",
                        "is_correct": False,
                        "scenario_update": "Gaita tetkikleri normal geldi ancak tetkik sürecinde kardiyak pompa yetersizliği derinleşti ve periferik dolaşım bozuldu.",
                        "teaching_point": "Kardiyak dekompanzasyon bulguları olan hastada geçirilmiş gastroenterite yönelik tetkikler tanısal önceliğe sahip değildir; kardiyovasküler inceleme şarttır.",
                    },
                    {
                        "text": "Oksijen desteği verip on iki derivasyonlu elektrokardiyografi çekmek, telekardiyografi istemek ve natriüretik peptit ile nekroz enzimlerini göndermek",
                        "is_correct": True,
                        "explanation": "Kardiyak disfonksiyon şüphesinde EKG ritim ve iletiyi, telekardiyografi kalp boyutunu, nekroz enzimleri ve natriüretik peptitler miyosit hasarını ve yetersizliği belgeler.",
                        "new_finding": "EKG: Sinüs taşikardisi (172/dk), prekordiyal derivasyonlarda düşük QRS voltajı ve yaygın ST-T değişiklikleri izlendi. Telekardiyografi: Kardiyotorasik indeks 0.64 (belirgin kardiyomegali) ve pulmoner vasküler konjesyon. Laboratuvar: CK-MB 64 U/L (yüksek), NT-proBNP 9.600 pg/mL (belirgin yüksek), Lökosit 10.800/mm³, CRP 12 mg/L.",
                    },
                    {
                        "text": "Yalnızca rutin hemogram ve idrar tahlili isteyerek taşikardinin kendiliğinden düzelmesi için hastayı iki saat kardiyak monitörizasyonsuz bekletmek",
                        "is_correct": False,
                        "scenario_update": "Monitörizasyonsuz bekletilen hastada taşikardi devam etti, bilinci letarjikleşti ve kapiller dolum zamanı beş saniyeye uzadı.",
                        "teaching_point": "Ağır taşikardi ve konjestif yetersizlik bulgusu olan hasta monitörize edilmeli ve acil kardiyolojik tetkikler geciktirilmemelidir.",
                    },
                    {
                        "text": "Olası intoksikasyonları ekarte etmek amacıyla acil kranial bilgisayarlı tomografi ve toksikoloji tarama paneli isteyip diğer tetkikleri ertelemek",
                        "is_correct": False,
                        "scenario_update": "Kranial tomografi normal sonuçlandı ancak hasta tomografi odasında taşipneik ve soğuk terleme içinde kaldı.",
                        "teaching_point": "Nörolojik odak olmaksızın izole taşikardi ve hepatomegalide öncelik santral sinir sistemi görüntülemesi değil kardiyovasküler değerlendirmedir.",
                    },
                ],
            },
            {
                "stage_title": "Klinik ve Laboratuvar Bulguları ile Kesin Tanı",
                "question": "Viral enfeksiyon sonrası gelişen galo ritmi, kardiyomegali ve belirgin nekroz belirteçleri saptanan hastada kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Akut viral miyokardit",
                        "is_correct": True,
                        "explanation": "Geçirilmiş viral enfeksiyon, açıklanamayan taşikardi, galo ritmi, kardiyomegali, düşük voltaj EKG ve belirgin kardiyak enzim yüksekliği miyokardit tanısını kesinleştirir.",
                        "new_finding": "Kesin tanı: Akut viral enfeksiyon sonrası miyokardit (sol ventrikül sistolik disfonksiyonu ve erken kardiyojenik şok tablosu). Troponin I düzeyi 4.2 ng/mL saptandı.",
                    },
                    {
                        "text": "Konjenital uzun QT sendromu",
                        "is_correct": False,
                        "scenario_update": "Uzun QT sendromunda EKG'de QTc uzaması ve polimorfik ventriküler taşikardi atakları görülür; kardiyomegali ve nekroz belirteçleri beklenmez.",
                        "teaching_point": "Kardiyomegali, pulmoner ödem ve enzim yüksekliği primer iyon kanalopatisi değil miyokard doku hasarı bulgusudur.",
                    },
                    {
                        "text": "Ağır bakteriyel bronkopnömoni",
                        "is_correct": False,
                        "scenario_update": "Pnömonide yüksek ateş, pürülan sekresyon ve lober konsolidasyon beklenir; izole kardiyomegali ve NT-proBNP yüksekliği açıklanamaz.",
                        "teaching_point": "Akciğerdeki raller ve takipne primer akciğer enfeksiyonundan ziyade sol kalp yetersizliğine bağlı pulmoner venöz konjesyonu gösterir.",
                    },
                    {
                        "text": "Hipovolemik dehidratasyon şoku",
                        "is_correct": False,
                        "scenario_update": "Hipovolemik şokta kalp gölgesi küçülür ve hepatomegali olmaz; burada kardiyomegali ve hepatomegali hipervolemik/konjestif yetersizliği kanıtlar.",
                        "teaching_point": "Hepatomegali ve kardiyomegali varlığı hipovolemiyi dışlar; tablonun kardiyojenik olduğunu gösterir.",
                    },
                ],
            },
            {
                "stage_title": "Acil Yoğun Bakım Tedavisi ve İnotropik Yönetim",
                "question": "Akut miyokardit ve düşük debili kardiyak pompa yetersizliği saptanan 3 yaşındaki bu hastada en uygun yönetim planı nedir?",
                "options": [
                    {
                        "text": "Kalp debisini artırmak amacıyla bolus intravenöz izotonik serum yükleyip hastayı genel pediatri servisinde takip altına almak",
                        "is_correct": False,
                        "scenario_update": "İzotonik yüklemesi sonrası pulmoner venöz göllenme derinleşti ve hasta entübe edilmek zorunda kaldı.",
                        "teaching_point": "Miyokarditte aşırı ön yük kardiyak yetersizliği dekompanse eder; sıvı kısıtlaması esastır, kontrolsüz bolus kontrendikedir.",
                    },
                    {
                        "text": "Taşikardiyi hızla kırmak amacıyla intravenöz yüksek doz beta bloker bolusu uygulayıp hastayı acil gözlem ünitesinde izlemek",
                        "is_correct": False,
                        "scenario_update": "Negatif inotrop etkili beta bloker miyokard kontraktilitesini tamamen çökerterek ağır kardiyojenik şoka yol açtı.",
                        "teaching_point": "Akut dekompanse miyokarditte beta blokerler negatif inotropik etkileri nedeniyle kesinlikle kontrendikedir.",
                    },
                    {
                        "text": "Ağır klinik tabloyu geriletmek amacıyla acil plazmaferez planlayarak hastayı taburcu edip çocuk kardiyoloji polikliniğine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Taburcu edilmesi düşünülen düşük debili hastada evde kardiyak arrest riski ve mortalite son derece yüksektir.",
                        "teaching_point": "Kardiyojenik şok riski taşıyan akut miyokardit hastaları acil servisten taburcu edilemez; yoğun bakımda sürekli izlem şarttır.",
                    },
                    {
                        "text": "Sıvı kısıtlaması uygulayıp inotropik infüzyon desteği hazırlayarak hastayı çocuk kardiyoloji yoğun bakım ünitesine acilen yatırmak",
                        "is_correct": True,
                        "explanation": "Dekompanse miyokarditte tedavi yaklaşımı sıvı kısıtlaması, kardiyak debiyi artıracak inotropik destek (örn. milrinon, düşük doz epinefrin) ve yoğun bakım takibidir.",
                        "new_finding": "Oksijen, milrinon infüzyonu ve sıvı kısıtlaması altında çocuk kardiyoloji yoğun bakım ünitesine nakledildi; ekokardiyografide EF %35 saptandı ve ECMO hazırlığıyla izleme alındı.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y34",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "8 Yaş",
        "gender": "Kız",
        "complaint": "Aniden başlayan şiddetli çarpıntı, göğüste baskı hissi, hafif baş dönmesi ve halsizlik",
        "history": (
            "8 yaşındaki kız çocuğu okulda beden eğitimi dersinde aniden fenalaşarak ailesiyle birlikte Sarı Alana getiriliyor: "
            "'Kızımız koşarken birdenbire kalbinin göğsünden fırlayacak gibi çarptığını söyledi. Göğsünde sıkışma hissi, halsizlik "
            "ve hafif sersemlik oldu ancak bayılmadı, senkop veya nöbet geçirmedi. Daha önce bilinen bir kalp rahatsızlığı, "
            "ritim bozukluğu veya ilaç maruziyeti bulunmuyor.'"
        ),
        "final_diagnosis": "Ventriküler Taşikardi (Hemodinamik Olarak Stabil Geniş QRS Taşikardi)",
        "disposition": "Sarı Alanda Monitörizasyon + Oksijen + İV Damar Yolu + İV Amiodaron İnfüzyonu + Senkronize Kardiyoversiyon Hazırlığı + Çocuk Kardiyoloji Yoğun Bakımına Yatış",
        "case_pearl": (
            "Pediatrik taşikardilerde QRS süresi (>0.09-0.10 sn) geniş taşiaritmiler aksi kanıtlanmadıkça ventriküler taşikardi kabul edilir. "
            "Ventriküler taşikardilerde yönetim hemodinamik stabiliteye göre belirlenir: Nabızsız veya unstabil (hipotansiyon, bilinç değişikliği, şok) "
            "olgularda acil elektriksel kardiyoversiyon/defibrilasyon gerekirken; bilinci açık ve normotansif stabil olgularda elektriksel kardiyoversiyon "
            "yerine antiaritmik infüzyonu (tercihen İV Amiodaron 5 mg/kg, 20-60 dakikada infüzyon, veya Prokainamid) ilk tercihtir. "
            "Stabil olgularda vagal manevralar veya adenozin primer tedavi değildir (aberran iletili SVT şüphesi dışında ventriküler taşikardiyi "
            "sonlandırmaz ve hemodinamiyi bozabilir). Her zaman senkronize kardiyoversiyon cihazı hazır bulundurulmalıdır."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda Ani Başlayan Çarpıntıya İlk Yaklaşım",
                "question": "Aniden başlayan şiddetli çarpıntı ve göğüste baskı hissi olan 8 yaşındaki bu çocukta ilk muayene ve yaklaşımınız nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Taşikardiyi hızla kırmak amacıyla ritmi ve hemodinamiyi hiç değerlendirmeden bilateral karotis sinüs masajı ve orbital bası uygulamak",
                        "is_correct": False,
                        "scenario_update": "Bilateral karotis ve orbital bası ağrıyı ve ajitasyonu artırdı; taşikardide hiçbir düzelme olmadı ve vagal manevra başarısız kaldı.",
                        "teaching_point": "Pediatrik yaş grubunda orbital bası retina dekolmanı riski nedeniyle kesinlikle kontrendikedir; ritim tipi bilinmeden körlemesine vagal manevra yapılmamalıdır.",
                    },
                    {
                        "text": "Hastayı monitörize edip damar yolu açmak, kan basıncı, bilinç durumu ve periferik perfüzyon ile ritmi değerlendirmek",
                        "is_correct": True,
                        "explanation": "Taşiaritmi ile başvuran hastada ilk adım hastanın hemodinamik stabilitesini (bilinç, tansiyon, perfüzyon) belirlemek ve kardiyak monitörizasyonu sağlamaktır.",
                        "new_finding": "Vital bulgular: Bilinç açık ve koopere, KTA 190/dk (düzenli), SS 22/dk, TA 95/62 mmHg, SpO2 %98, CRT 2 saniye. Periferik nabızlar zayıflamış ancak net alınıyor. Kardiyak muayenede taşikardi dışında üfürüm yok, akciğer sesleri doğal, periferik ödem veya hepatomegali saptanmadı. Hasta normotansif ve hemodinamik olarak stabildir.",
                    },
                    {
                        "text": "Hastanın bilinci açık ve genel durumu iyi olduğu için sakinleştirici oral sedatif vererek karanlık bir odada dinlendirmek",
                        "is_correct": False,
                        "scenario_update": "Dinlenmeyle taşikardi gerilemedi, hasta göğüs ağrısı ve aşırı halsizlik hissetmeye devam etti.",
                        "teaching_point": "Dakikada 190 atımlı taşikardiler primer aritmik patolojilerdir; dinlenme veya sedasyonla düzelmez, acil tanısal elektrokardiyografi gerektirir.",
                    },
                    {
                        "text": "Taşikardik her ritim bozukluğunda ilk basamak olan hızlı intravenöz puşe adenozin uygulaması için defibrilatörsüz acil hazırlık yapmak",
                        "is_correct": False,
                        "scenario_update": "Ritim tipi ve QRS morfolojisi incelenmeden hazırlanan puşe adenozin yaklaşımı, olası ventriküler aritmilerde dekompanzasyon riskini artırdı.",
                        "teaching_point": "Ritim tipi elektrokardiyografi ile analiz edilmeden ve defibrilasyon hazırlığı tamamlanmadan körlemesine adenozin puşesi uygulanması tehlikelidir.",
                    },
                ],
            },
            {
                "stage_title": "On İki Derivasyonlu Elektrokardiyografi ve Ritim Analizi",
                "question": "Hemodinamisi stabil olan ancak belirgin taşikardisi devam eden bu hastada tanısal ritim analizi için ne yapılmalıdır?",
                "options": [
                    {
                        "text": "Acil on iki derivasyonlu elektrokardiyografiyle ventriküler aktivasyon süresini, atriyoventriküler ilişkiyi ve füzyon vuruşlarını analiz etmek",
                        "is_correct": True,
                        "explanation": "Taşiaritmilerde kesin tanı 12 derivasyonlu elektrokardiyografi ile konur; QRS süresi, AV dissosiasyon ve füzyon vuruşları ayırıcı tanıda anahtardır.",
                        "new_finding": "12 Derivasyonlu EKG: Düzenli ritim, kalp tepe atımı 192/dk, QRS süresi 120 milisaniye (yaşa göre uzamış / >0.10 sn), P dalgaları ile QRS arasında bağımsızlık (belirgin atriyoventriküler dissosiasyon), aralarda yakalama ve füzyon vuruları izlendi.",
                    },
                    {
                        "text": "Elektrokardiyografi çekmeden önce ritmi sonlandırmak amacıyla hastaya derin nefes aldırıp ıkındırarak arka arkaya vagal manevralar denemek",
                        "is_correct": False,
                        "scenario_update": "Tekrarlanan vagal manevralar taşikardi hızını veya ritmini değiştirmedi, hastanın göğüs kafesindeki sıkıntı hissi devam etti.",
                        "teaching_point": "Ventriküler kökenli taşiaritmiler atriyoventriküler nodu içermediği için vagal manevralara yanıt vermez; zaman kaybetmeden EKG çekilmelidir.",
                    },
                    {
                        "text": "Yalnızca tek derivasyonlu monitör şeridi izleyerek kardiyak enzim ve elektrolit sonuçları çıkana kadar hiçbir girişim yapmamak",
                        "is_correct": False,
                        "scenario_update": "Tek derivasyonda P dalgaları ve füzyon vuruları ayırt edilemedi, ritmin mekanizması aydınlatılamadığı için tanısal süreç kilitlendi.",
                        "teaching_point": "Taşiaritmilerin ayırıcı tanısında tek derivasyonlu monitör şeridi yetersizdir; AV dissosiasyon ve QRS morfolojisi için tam 12 derivasyonlu EKG şarttır.",
                    },
                    {
                        "text": "Ritim bozukluğunun olası intrakranial nedenlerini dışlamak amacıyla elektrokardiyografiyi erteleyip acil beyin manyetik rezonans görüntüleme istemek",
                        "is_correct": False,
                        "scenario_update": "Radyoloji hazırlığı esnasında EKG çekimi gecikti ve hastanın kardiyak dekompanzasyon riski arttı.",
                        "teaching_point": "Taşikardi ile başvuran hastada ilk ve en acil tanı aracı elektrokardiyografidir; beyin görüntülemelerinin acil ritim tanısında yeri yoktur.",
                    },
                ],
            },
            {
                "stage_title": "Elektrokardiyografik Bulgularla Kesin Tanı",
                "question": "EKG'de QRS süresi >0.10 sn, AV dissosiasyon ve füzyon vuruşları saptanan stabil hastada kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Dar QRS supraventriküler taşikardi",
                        "is_correct": False,
                        "scenario_update": "SVT'de QRS süresi normaldir (<0.09 sn) ve genellikle AV dissosiasyon veya füzyon vuruları görülmez.",
                        "teaching_point": "QRS süresi uzamış taşikardilerde AV dissosiasyon ve füzyon vurularının varlığı SVT'yi dışlar.",
                    },
                    {
                        "text": "Aberran iletili sinüs taşikardisi",
                        "is_correct": False,
                        "scenario_update": "Sinüs taşikardisinde her QRS öncesinde normal P dalgası bulunur ve hız genellikle yaşa bağlı fizyolojik sınırlardadır.",
                        "teaching_point": "Hızın 190/dk olması, AV dissosiasyon bulunması sinüs taşikardisi ile bağdaşmaz.",
                    },
                    {
                        "text": "Ortodromik atriyoventriküler reentran taşikardi",
                        "is_correct": False,
                        "scenario_update": "Ortodromik AVRT'de antegrad ileti AV noddan geçtiği için QRS kompleksi dar ve normal morfolojidedir.",
                        "teaching_point": "Uzamış QRS ve AV dissosiasyon ortodromik AVRT tablosuyla uyumsuzdur.",
                    },
                    {
                        "text": "Hemodinamik stabil ventriküler taşikardi",
                        "is_correct": True,
                        "explanation": "QRS süresinin uzamış olması (>0.10 sn), atriyoventriküler dissosiasyon ve füzyon vuruşları ventriküler taşikardi için tanı koydurucudur; normotansif olması stabil olduğunu gösterir.",
                        "new_finding": "Kesin tanı: Hemodinamik olarak stabil monomorfik ventriküler taşikardi.",
                    },
                ],
            },
            {
                "stage_title": "Stabil Taşiaritminin Farmakolojik Tedavisi ve Yönetimi",
                "question": "Bilinci açık, normotansif ve hemodinamik olarak stabil ventriküler taşikardi saptanan 8 yaşındaki bu hastada en uygun tedavi yaklaşımı nedir?",
                "options": [
                    {
                        "text": "Bilinci açık hastaya yeterli sedoanaljezi uygulamadan derhal iki yüz joule asenkron defibrilasyon şoku vererek ritmi sonlandırmak",
                        "is_correct": False,
                        "scenario_update": "Stabil hastaya sedasyonsuz ve asenkron yüksek doz şok verilmesi ağır miyokardiyal travma, ağrı ve ventriküler fibrilasyon tetikledi.",
                        "teaching_point": "Defibrilasyon yalnızca nabızsız VT veya ventriküler fibrilasyonda uygulanır; stabil hastada acil şok endikasyonu yoktur, antiaritmik infüzyon gerekir.",
                    },
                    {
                        "text": "Ritmi düzeltmek amacıyla arka arkaya üç kez hızlı puşe intravenöz adenozin uygulayıp hastayı servise taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Adenozin ventriküler kaynaklı taşikardiyi sonlandırmadı, geçici bradikardi ve hipotansiyon atağına yol açtı.",
                        "teaching_point": "Adenozin AV nod bağımlı SVT'lerde etkilidir; ventriküler taşikardilerde tedavi edici değildir ve hastayı instabil hale getirebilir.",
                    },
                    {
                        "text": "Senkronize kardiyoversiyon hazırlığı eşliğinde intravenöz amiodaron infüzyonu başlayarak hastayı çocuk kardiyoloji yoğun bakım ünitesinde izlemek",
                        "is_correct": True,
                        "explanation": "Hemodinamik olarak stabil ventriküler taşikardide ilk basamak farmakolojik kardiyoversiyondur (İV amiodaron 5 mg/kg, 20-60 dakikada); olası dekompanzasyon için kardiyoversiyon hazır tutulmalıdır.",
                        "new_finding": "Amiodaron infüzyonunun 35. dakikasında ritim sinüse döndü (KTA 94/dk, dar QRS). Çocuk kardiyoloji yoğun bakım ünitesinde sürekli monitörizasyona alındı.",
                    },
                    {
                        "text": "Hastayı monitörden ayırıp oral digoksin tedavisi başlayarak ertesi gün çocuk kardiyoloji poliklinik kontrolüne gelmek üzere taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Monitörden ayrılan hastada ventriküler taşikardi dekompanse olarak senkop ve hipotansif şok gelişti.",
                        "teaching_point": "Ventriküler taşikardili hiçbir hasta acil servisten oral ilaçla taburcu edilemez; yoğun bakımda sürekli ritim takibi zorunludur.",
                    },
                ],
            },
        ],
    },
    {
        "id": "Y35",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "9 Yaş",
        "gender": "Erkek",
        "complaint": "Gezici eklem ağrısı, diz ve ayak bileğinde şişlik, kızarıklık, subfebril ateş ve halsizlik",
        "history": (
            "9 yaşındaki erkek çocuk ailesi tarafından eklem şişlikleri nedeniyle Sarı Alana getiriliyor: "
            "'Üç hafta önce şiddetli boğaz ağrısı ve yüksek ateşi olmuştu, doktora götürmedik ve kendiliğinden geçmişti. "
            "Dört gün önce sağ dizi aniden şişti, kızardı ve dokununca şiddetli ağrıyordu. İki gün sonra sağ dizi hafiflerken "
            "bu kez sol ayak bileği şişti ve basamaz hale geldi. Çocuğumuz aşırı halsiz ve çabuk yoruluyor.'"
        ),
        "final_diagnosis": "Akut Romatizmal Ateş (Kardit ve Gezici Poliartrit / Jones Kriterleri)",
        "disposition": "Sarı Alanda İV Damar Yolu + Yatak İstirahati + Oral Penisilin V / Benzatin Penisilin G + Antiinflamatuar Tedavi + Çocuk Kardiyoloji ve Romatoloji Servisine Yatış",
        "case_pearl": (
            "Akut romatizmal ateş (ARA), tedavi edilmemiş A Grubu Beta-Hemolitik Streptokok (AGBHS) farenjitinden 2-4 hafta sonra gelişen "
            "sistemik otoimmün bir tablodur. Tanı revize Jones kriterlerine dayanır: Geçirilmiş streptokok enfeksiyonu kanıtı (ASO yüksekliği veya "
            "pozitif boğaz kültürü) eşliğinde 2 majör veya 1 majör + 2 minör kriter gereklidir. Majör kriterler: Gezici poliartrit, kardit "
            "(en sık mitral kapak yetersizliği), Sydenham koresi, eritema marjinatum ve subkutan nodüllerdir. Minör kriterler: Ateş, artralji, "
            "yüksek ESH/CRP ve EKG'de uzamış PR intervalidir (1. derece AV blok). Tedavide streptokok eradikasyonu (benzatin penisilin veya oral penisilin), "
            "kardit ve artrit için antiinflamatuar tedavi (aspirin veya steroid) ve sekonder profilaksi esastır."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda Gezici Artritli Hastaya İlk Yaklaşım",
                "question": "Üç hafta önceki farenjit sonrası gezici eklem tutulumu gelişen 9 yaşındaki çocukta ilk muayene önceliğiniz ne olmalıdır?",
                "options": [
                    {
                        "text": "Eklem şişliğini primer septik artrit kabul ederek eklemi aspire edip acil cerrahi artrotomi için ortopediye devretmek",
                        "is_correct": False,
                        "scenario_update": "Eklem aspirasyonunda pürülan mayi gelmedi; gereksiz invaziv artrotomi girişimi gezici karakterdeki sistemik inflamasyonu aydınlatamadı.",
                        "teaching_point": "Gezici karakterdeki poliartritlerde tek ekleme odaklanıp cerrahi artrotomi yapmak hatalıdır; sistemik ve kardiyovasküler muayene önceliklidir.",
                    },
                    {
                        "text": "Yalnızca eklem ultrasonografisi isteyerek kardiyovasküler oskültasyon yapmadan yüksek doz intramüsküler analjezik uygulayıp hastayı yatakta dinlendirmek",
                        "is_correct": False,
                        "scenario_update": "Analjezik ağrıyı geçici azalttı ancak kardiyak oskültasyon yapılmadığı için apeksteki belirgin pansistolik üfürüm gözden kaçırıldı.",
                        "teaching_point": "Geçirilmiş farenjit ve gezici artrit öyküsünde kardiyak oskültasyon hayatidir; kardit bulguları atlanmamalıdır.",
                    },
                    {
                        "text": "Geçirilmiş farenjit öyküsünü göz ardı edip travmatik bağ yaralanması ön tanısıyla bilateral alt ekstremiteye alçı uygulamak",
                        "is_correct": False,
                        "scenario_update": "Alçı tespiti uygulanan eklemde enflamasyon ve ısı artışı devam etti, sistemik hastalık tablosu ilerledi.",
                        "teaching_point": "Travma öyküsü olmayan, bir eklemden diğerine göç eden artrit tablosunda ortopedik immobilizasyon değil sistemik etiyoloji araştırılmalıdır.",
                    },
                    {
                        "text": "Eklem bulgularını değerlendirirken kalp seslerini dikkatle oskülte ederek apekste pansistolik üfürüm ve kapak disfonksiyonunu araştırmak",
                        "is_correct": True,
                        "explanation": "Geçirilmiş farenjit sonrası gezici poliartrit tablosunda subklinik veya klinik kardit gelişimini saptamak için kardiyak oskültasyon zorunludur.",
                        "new_finding": "Vital bulgular: Ateş 38.3°C, KTA 110/dk, SS 20/dk, TA 105/65 mmHg. Sol ayak bileğinde belirgin eritem, şişlik, sıcaklık artışı ve hareket kısıtlılığı mevcut; sağ dizde hafif hassasiyet izlendi. Kardiyak oskültasyonda apekste aksillaya yayılan 3/6 pansistolik üfürüm duyuldu, S3 veya perikardiyal frotman yok. Ciltte döküntü veya subkutan nodül saptanmadı.",
                    },
                ],
            },
            {
                "stage_title": "Laboratuvar Belirteçleri ve Kardiyak İnceleme",
                "question": "Gezici eklem tutulumu ve mitral üfürüm saptanan bu hastada sistemik tutulumu netleştirecek tetkik planınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Gezici eklem tutulumunu aydınlatmak amacıyla her iki diz ve ayak bileğine kontrastlı manyetik rezonans görüntüleme tetkiki çekmek",
                        "is_correct": False,
                        "scenario_update": "Manyetik rezonansta eklem içi efüzyon ve sinovyal kalınlaşma dışında etiyolojik tanıya katkı sağlayan ek bilgi elde edilemedi.",
                        "teaching_point": "Artrit tanısında eklem MRG rutin tetkik değildir; geçirilmiş streptokok enfeksiyonu ve kardiyak tutulumu göstermez.",
                    },
                    {
                        "text": "Sistemik etiyolojiyi araştırmadan yalnızca serum kan glukozu ve böbrek fonksiyon testleri isteyerek hastayı gözlemde tutmak",
                        "is_correct": False,
                        "scenario_update": "Böbrek testleri normal geldi ancak kardiyak kapak tutulumu ve streptokok belirteçleri araştırılmadığı için tanı gecikti.",
                        "teaching_point": "Gezici artrit ve üfürüm tablosunda ASO, akut faz reaktifleri ve elektrokardiyografi istenmeden hasta bekletilemez.",
                    },
                    {
                        "text": "Streptokok belirteçleri, akut faz reaktifleri ve olası ileti bozukluklarını saptamak amacıyla elektrokardiyografi ile ekokardiyografi planlamak",
                        "is_correct": True,
                        "explanation": "Tanı için geçirilmiş streptokok kanıtı (ASO), minör kriterler (ESH, CRP, uzamış PR) ve kardit kanıtı (ekokardiyografide kapak yetersizliği) gereklidir.",
                        "new_finding": "Laboratuvar: ASO >800 IU/mL (normal <200), CRP 68 mg/L, ESH 75 mm/saat, Lökosit 13.600/mm³, Boğaz kültürü negatif. EKG: Sinüs ritmi, PR intervali 0.20 sn (yaşa göre uzamış, 1. derece AV blok). Ekokardiyografi: Mitral kapakta kalınlaşma, hafif-orta derecede mitral yetersizlik jeti saptandı; sol ventrikül fonksiyonları normal.",
                    },
                    {
                        "text": "Viral artrit düşüncesiyle hiçbir laboratuvar tetkiki istemeden hastaya yalnızca semptomatik lokal buz uygulaması ve istirahat önermek",
                        "is_correct": False,
                        "scenario_update": "Buz uygulamasıyla eklem ağrısı gerilemedi, üfürümün nedeni aydınlatılamadı ve kardiyak tutulum ilerleme riskiyle karşı karşıya kaldı.",
                        "teaching_point": "Üfürüm eşlik eden gezici artritlerde viral etiyoloji varsayımıyla tetkiksiz izlem kabul edilemez; streptokok immünolojik yanıtı araştırılmalıdır.",
                    },
                ],
            },
            {
                "stage_title": "Jones Kriterleri Işığında Kesin Tanı",
                "question": "Belgelenmiş streptokok enfeksiyonu, kardit, gezici poliartrit, yüksek akut faz reaktifleri ve uzamış PR saptanan hastada kesin tanınız nedir?",
                "options": [
                    {
                        "text": "Juvenil idiyopatik artrit",
                        "is_correct": False,
                        "scenario_update": "JİA'da artrit en az altı hafta sebat eder, gezici karakterde değildir ve geçirilmiş streptokok kanıtı veya PR uzaması beklenmez.",
                        "teaching_point": "Kısa sürede eklem değiştiren gezici poliartrit ve kardit tablosu juvenil idiyopatik artritten ziyade akut romatizmal ateşe işaret eder.",
                    },
                    {
                        "text": "Akut romatizmal ateş",
                        "is_correct": True,
                        "explanation": "Yüksek ASO varlığında 2 majör kriter (kardit, gezici poliartrit) ve 2 minör kriter (ateş, uzamış PR, yüksek ESH/CRP) Jones kriterlerine göre kesin akut romatizmal ateş tanısı koydurur.",
                        "new_finding": "Kesin tanı: Akut romatizmal ateş (mitral valvülit/kardit ve gezici poliartrit).",
                    },
                    {
                        "text": "Poststreptokoksik reaktif artrit",
                        "is_correct": False,
                        "scenario_update": "Poststreptokoksik reaktif artritte eklem tutulumu gezici değildir, aspirine dramatik yanıt vermez ve kardit veya EKG'de PR uzaması eşlik etmez.",
                        "teaching_point": "Kardiyak valvülit ve PR uzaması varlığı tabloyu reaktif artritten ayırır, akut romatizmal ateşi kesinleştirir.",
                    },
                    {
                        "text": "Sistemik lupus eritematozus",
                        "is_correct": False,
                        "scenario_update": "SLE'de malar döküntü, fotosensitivite, böbrek tutulumu ve pozitif otoantikorlar (ANA, anti-dsDNA) beklenir; geçirilmiş streptokokla ilişkili değildir.",
                        "teaching_point": "Ateş, kardit ve geçirilmiş streptokok farenjiti SLE'den ziyade romatizmal kardit tablosudur.",
                    },
                ],
            },
            {
                "stage_title": "Eradikasyon, Antiinflamatuar Tedavi ve İzlem Planı",
                "question": "Akut romatizmal ateş tanısı kesinleşen 9 yaşındaki bu hastanın medikal tedavisi ve hospitalizasyon yönetimi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Streptokok eradikasyonu için penisilin başlamak, antiinflamatuar tedavi planlayıp kardit izlemi amacıyla hastayı çocuk servisine yatırmak",
                        "is_correct": True,
                        "explanation": "Akut romatizmal ateşte yaklaşım streptokok eradikasyonu (benzatin penisilin G veya oral penisilin V), kardit/artrit için antiinflamatuar tedavi ve yatak istirahatidir.",
                        "new_finding": "Tek doz intramüskler benzatin penisilin G yapıldı, antiinflamatuar tedavi ve yatak istirahati altında kardit izlemi için çocuk kardiyoloji servisine yatırıldı.",
                    },
                    {
                        "text": "Kapak tutulumu saptandığı için hastayı derhal acil açık kalp ameliyatına alarak mekanik mitral kapak protezi takmak",
                        "is_correct": False,
                        "scenario_update": "Akut enflamasyon evresinde kapak dokuları frajildir; medikal tedavi denenmeden cerrahiye alınması ağır komplikasyonlara yol açar.",
                        "teaching_point": "Akut romatizmal karditte öncelik cerrahi değil medikal antiinflamatuar tedavidir; cerrahi yalnızca dirençli ve medikal tedaviye yanıtsız akut kalp yetersizliğinde düşünülür.",
                    },
                    {
                        "text": "Hiçbir medikal tedavi vermeden yalnızca mutlak yatak istirahati önererek hastayı doğrudan evine taburcu edip kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Tedavi edilmeyen hastada streptokok taşıyıcılığı devam etti, kapak tutulumu ilerleyerek kalıcı kronik romatizmal kapak hastalığına dönüştü.",
                        "teaching_point": "Antibiyotik eradikasyonu ve antiinflamatuar tedavi yapılmaksızın taburculuk kabul edilemez; kalıcı kapak hasarı riski yüksektir.",
                    },
                    {
                        "text": "Akut inflamasyonu baskılamak amacıyla yüksek doz intravenöz immünoglobulin infüzyonu uygulayıp başka hiçbir antibiyotik tedavisi vermemek",
                        "is_correct": False,
                        "scenario_update": "İntravenöz immünoglobulin romatizmal karditte kanıtlanmış etkinliğe sahip değildir ve streptokok eradikasyonunu sağlamadığı için enfeksiyon devam etti.",
                        "teaching_point": "Akut romatizmal ateşte IVIG standart tedavi değildir; penisilin ile streptokok eradikasyonu ve antiinflamatuar tedavi şarttır.",
                    },
                ],
            },
        ],
    },
]
