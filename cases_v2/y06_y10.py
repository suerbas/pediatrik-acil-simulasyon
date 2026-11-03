# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - Y06-Y10 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "Y06",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "10 Yaş",
        "gender": "Kız",
        "complaint": "Karın ağrısı, tekrarlayan kusma, derin ve hızlı nefes alma, belirgin halsizlik",
        "history": (
            "Sarı Alana halsiz ve bitkin halde getiriliyor: 'Dün akşamdan beri karnı çok ağrıyor ve 6 kez "
            "kustu. İshali veya ateşi hiç olmadı ama çok derin ve hızlı nefes alıp veriyor. Son 3 haftadır "
            "çok su içiyordu, geceleri 3-4 kez idrara kalkıyordu ve iştahı açık olmasına rağmen 4 kilo zayıfladı.'"
        ),
        "final_diagnosis": "Diyabetik Ketoasidoz (DKA - Yeni Tanı Tip 1 Diabetes Mellitus)",
        "disposition": (
            "Sarı Alanda İlk Saat İzotonik Sıvı Restorasyonu + Potasyum Destekli Rehidratasyon ve İV Regüler "
            "İnsülin İnfüzyonu -> Çocuk Yoğun Bakım Yatışı"
        ),
        "case_pearl": (
            "Karın ağrısı, kusma ve takipne ile başvuran çocuklarda ishal yoksa ve poliüri, polidipsi, kilo "
            "kaybı eşlik ediyorsa Diyabetik Ketoasidoz (DKA) akut batın veya solunum yolu enfeksiyonu ile sıkça "
            "karışır. ISPAD 2022 kılavuzuna göre İV bolus insülin ve rutin sodyum bikarbonat serebral ödem "
            "riskini artırdığı için kontrendikedir; ilk saat %0.9 NaCl restorasyonu sonrası 0.05-0.1 U/kg/saat "
            "İV regüler insülin infüzyonu başlanır."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Yatak Başı Yaklaşım",
                "question": (
                    "Karın ağrısı, kusma ve derin-hızlı solunumla getirilen 10 yaşındaki bu hastada ilk "
                    "değerlendirmede öncelikli yaklaşımınız ne olmalıdır?"
                ),
                "options": [
                    {
                        "text": (
                            "Solunum sıkıntısı ve takipne ön planda olduğu için hemen geri solumasız maskeyle "
                            "oksijen başlayıp ardışık üç doz nebülize salbutamol ve sistemik metilprednizolon uygulamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Akciğer oskültasyonu tamamen doğal ve SpO2 değeri %100 olan hastada verilen "
                            "beta-agonist ve sistemik kortikosteroid sonrası kan şekeri 610 mg/dL düzeyine "
                            "yükseldi, takipnesi ve letarjisi daha da derinleşti."
                        ),
                        "teaching_point": (
                            "Akciğer oskültasyonu doğal ve satürasyonu normal olan bir çocukta derin ve hızlı "
                            "solunum paterni alt solunum yolu obstrüksiyonunu değil, ağır metabolik asidozun "
                            "solunumsal kompansasyonunu düşündürmelidir."
                        ),
                    },
                    {
                        "text": (
                            "Asidotik tipte derin ve takipneik solunum paternini, dehidratasyon derecesini ve "
                            "bilinç durumunu değerlendirip derhal parmak ucu kan şekeri ile kan ketonu bakmak"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Poliüri, polidipsi, kilo kaybı, kusma ve akciğer bulgusu olmaksızın derin-hızlı "
                            "solunumla başvuran çocukta ağır hiperglisemi ve metabolik asidoz tablosu yatak "
                            "başı kapiller glukoz ve keton ölçümüyle ilk dakikada saptanmalıdır."
                        ),
                        "new_finding": (
                            "Vital Bulgular: Ateş 36.7°C, KTA 132/dk, SS 34/dk, TA 100/65 mmHg, SpO2 %100. "
                            "Solunum asidotik tipte derin ve takipneik paternde; akciğer oskültasyonu bilateral "
                            "doğal. Nefeste belirgin aseton kokusu mevcut. Ağız mukozası kuru, kapiller dolum "
                            "3 saniye, GKS 14. Parmak ucu kan şekeri 465 mg/dL, kapiller kan ketonu 5.8 mmol/L saptandı."
                        ),
                    },
                    {
                        "text": (
                            "Şiddetli karın ağrısı ve tekrarlayan kusma nedeniyle akut cerrahi batın düşünerek "
                            "oral alımı kesmek, nazogastrik dekompresyon yapmak ve acil batın ultrasonografisi "
                            "için radyolojiye göndermek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Yatak başı kan şekeri bakılmadan radyoloji ünitesine gönderilen hastanın "
                            "ultrasonografisinde serbest sıvı veya akut cerrahi patoloji saptanmadı; ancak işlem "
                            "sırasında hastanın uykuya meyili ve dehidratasyonu belirgin şekilde arttı."
                        ),
                        "teaching_point": (
                            "Ağır metabolik asidoz ve ketonemi tablosu şiddetli karın ağrısı ve kusma ile akut "
                            "cerrahi batını taklit edebilir; görüntüleme öncesinde yatak başı kan şekeri ve kan "
                            "gazı mutlaka kontrol edilmelidir."
                        ),
                    },
                    {
                        "text": (
                            "Tekrarlayan kusma ve dehidratasyon nedeniyle damar yolu açıp intravenöz ondansetron "
                            "uygulamak ve kan şekeri bakmadan %5 dekstroz içeren hipotonik sıvıyı hızlı infüzyonla başlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Kan şekeri ölçülmeden verilen dekstrozlu hipotonik sıvı sonrası hastanın mevcut "
                            "hiperglisemisi daha da arttı ve serum efektif osmolaritesindeki ani dalgalanma "
                            "nedeniyle baş ağrısı ile konvülziyon riski ortaya çıktı."
                        ),
                        "teaching_point": (
                            "Hiperglisemi ve dehidratasyon kuşkusu olan hastalarda kapiller glukoz görülmeden "
                            "dekstroz içeren veya hipotonik sıvılar kesinlikle başlanmamalı; ilk hacim "
                            "genişletme yalnız izotonik kristaloid ile yapılmalıdır."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Laboratuvar İncelemesi ve Metabolik Değerlendirme",
                "question": (
                    "Parmak ucu kan şekeri 465 mg/dL ve kan ketonu 5.8 mmol/L saptanan bu hastada ilk "
                    "laboratuvar ve izlem planınız ne olmalıdır?"
                ),
                "options": [
                    {
                        "text": (
                            "Sadece venöz glukoz ve tam idrar tetkiki göndermek, sonuçları beklemeden kan "
                            "şekerini hızla düşürmek için 0.15 U/kg intravenöz puşe regüler insülin uygulamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Serum potasyum düzeyi ve asidoz derecesi görülmeden yapılan intravenöz bolus "
                            "insülin sonrası potasyum hızla hücre içine kaydı; monitörde T dalga düzleşmesi, "
                            "belirgin U dalgaları ve ventriküler ekstrasistoller gelişti."
                        ),
                        "teaching_point": (
                            "Ağır hiperglisemi ve ketonemi yönetiminde intravenöz bolus insülin hem akut "
                            "hipokalemik aritmi hem de hızlı osmolarite düşüşüne bağlı beyin ödemi riskini "
                            "artırdığı için kesinlikle kontrendikedir."
                        ),
                    },
                    {
                        "text": (
                            "Arteriyel kan gazı ve serum elektrolitlerini almak, derin takipneyi azaltmak "
                            "amacıyla kan gazı sonucunu beklemeden 2 mEq/kg intravenöz sodyum bikarbonat infüzyonu başlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Erken uygulanan sodyum bikarbonat infüzyonu sonrası hastada paradoksal santral "
                            "sinir sistemi asidozu, hipokalemi eğilimi ve doku oksijen sunumunda bozulma "
                            "gelişerek bilinç durumu GKS 11 düzeyine geriledi."
                        ),
                        "teaching_point": (
                            "Metabolik asidozlu hiperglisemik krizlerde rutin sodyum bikarbonat uygulaması "
                            "paradoksal serebral asidoz ve beyin ödemi riski taşır; sıvı ve insülin infüzyonu "
                            "ile keton üretimi durduğunda asidoz kendiliğinden düzelir."
                        ),
                    },
                    {
                        "text": (
                            "Venöz kan gazı, biyokimya ve HbA1c istemek, ancak ilk saat sıvı tedavisini "
                            "beklemeden eş zamanlı olarak 0.1 U/kg/saat hızında intravenöz insülin infüzyonunu başlatmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "İlk saat izotonik sıvı restorasyonu tamamlanmadan erken başlanan insülin "
                            "infüzyonu, intravasküler hacim henüz dolmadan glukozun hızla düşmesine ve sistemik "
                            "hipotansiyon ile serebral hipoperfüzyona yol açtı."
                        ),
                        "teaching_point": (
                            "Güncel kılavuzlara göre insülin infüzyonu ilk başvuruda hemen başlanmaz; önce 1 "
                            "saatlik izotonik sıvı restorasyonu yapılmalı ve serum potasyum düzeyi görüldükten "
                            "sonra insülin infüzyonuna geçilmelidir."
                        ),
                    },
                    {
                        "text": (
                            "Venöz kan gazı, serum elektrolitleri, düzeltilmiş sodyum hesabı, üre, kreatinin, "
                            "fosfor, magnezyum, tam idrar tetkiki, HbA1c ve potasyum izlemi için EKG istemek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Venöz pH ve bikarbonat ile metabolik tablonun ağırlığı belirlenir; ölçülen sodyum "
                            "üzerinden düzeltilmiş sodyum hesaplanmalı ve insülin öncesi bazal potasyum düzeyi "
                            "ile EKG mutlaka değerlendirilmelidir."
                        ),
                        "new_finding": (
                            "LABORATUVAR: Venöz Kan Gazı pH 7.12, pCO2 20 mmHg, HCO3 6.4 mmol/L, Baz Açığı -21, "
                            "Laktat 1.8 mmol/L. Glukoz 465 mg/dL, Ölçülen Na 131 mEq/L, Hesaplanan Düzeltilmiş "
                            "Na 137 mEq/L, K 4.6 mEq/L, Cl 96 mEq/L, Fosfor 3.8 mg/dL, Üre 42 mg/dL, Kreatinin "
                            "0.72 mg/dL. TİT: Glukoz +++, Keton +++. HbA1c %11.8. EKG: Sinüs taşikardisi, T dalgaları normal."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": (
                    "Mevcut klinik bulgular ve laboratuvar sonuçları (Glukoz 465 mg/dL, venöz pH 7.12, "
                    "HCO3 6.4 mmol/L, kan ketonu 5.8 mmol/L) doğrultusunda kesin tanınız nedir?"
                ),
                "options": [
                    {
                        "text": "Orta-Ağır Diyabetik Ketoasidoz (Yeni Tanı Tip 1 DM)",
                        "is_correct": True,
                        "explanation": (
                            "ISPAD 2022 kriterlerine göre kan şekeri >200 mg/dL, venöz pH <7.30 veya HCO3 "
                            "<15 mmol/L ve ketonemi ≥3.0 mmol/L varlığı DKA tanısını koydurur; pH 7.12 ve HCO3 "
                            "6.4 mmol/L orta-ağır DKA ile uyumludur."
                        ),
                        "new_finding": "Kesin Tanı: Orta-Ağır Diyabetik Ketoasidoz (Yeni Tanı Tip 1 Diabetes Mellitus).",
                    },
                    {
                        "text": "Ketoasidoz Olmayan Hiperglisemik Hiperosmolar Durum (HHD)",
                        "is_correct": False,
                        "scenario_update": (
                            "Hastada belirgin ketonemi (5.8 mmol/L) ve derin metabolik asidoz (pH 7.12, HCO3 "
                            "6.4 mmol/L) mevcut olup tablo HHD kriterleri ile uyumlu değildir."
                        ),
                        "teaching_point": (
                            "Hiperglisemik Hiperosmolar Durumda kan şekeri >600 mg/dL ve efektif osmolarite "
                            ">320 mOsm/kg iken belirgin ketozis ve ağır asidoz (pH >7.25, HCO3 >15) beklenmez."
                        ),
                    },
                    {
                        "text": "Akut Dekompanse Metabolik Asidoz ve Stres Hiperglisemisi",
                        "is_correct": False,
                        "scenario_update": (
                            "Hastanın 3 haftalık poliüri-polidipsi öyküsü, 465 mg/dL glukoz değeri, 5.8 mmol/L "
                            "ketonemisi ve %11.8 HbA1c düzeyi geçici stres hiperglisemisini dışlamaktadır."
                        ),
                        "teaching_point": (
                            "Stres hiperglisemisinde HbA1c normaldir (<%5.7) ve ağır ketonemi ile derin "
                            "metabolik asidoz görülmez."
                        ),
                    },
                    {
                        "text": "Akut Salisilat İntoksikasyonuna Bağlı Metabolik Asidoz",
                        "is_correct": False,
                        "scenario_update": (
                            "Hastada ilaç alım öyküsü yoktur; üç haftalık ozmotik diürez semptomları, aşikâr "
                            "hiperglisemi ve yüksek HbA1c salisilat zehirlenmesiyle açıklanamaz."
                        ),
                        "teaching_point": (
                            "Salisilat zehirlenmesi solunumsal alkaloz ve yüksek anyon açıklı metabolik asidoz "
                            "yapabilir ancak kan şekeri 465 mg/dL ve HbA1c %11.8 yeni tanı Tip 1 DM göstergesidir."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda İlk Saat Tedavisi ve Serebral Ödemden Korunma",
                "question": (
                    "Orta-ağır DKA tanısı konulan ve serum potasyumu 4.6 mEq/L olan bu hastada beyin ödemi "
                    "riskini en aza indiren tedavi planı hangisidir?"
                ),
                "options": [
                    {
                        "text": (
                            "İlk saatte 20 mL/kg %0.45 NaCl hipotonik sıvı yüklemek, 0.1 U/kg İV puşe insülin "
                            "yapmak ve pH 7.12 olduğu için 1 mEq/kg sodyum bikarbonat vermek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Hipotonik sıvı yüklemesi, İV bolus insülin ve sodyum bikarbonat uygulaması sonrası "
                            "3. saatte hastada şiddetli baş ağrısı, bradikardi, sistemik hipertansiyon ve bilinç "
                            "kaybı ile akut serebral ödem gelişti."
                        ),
                        "teaching_point": (
                            "DKA tedavisinde hipotonik sıvı bolusu, İV puşe insülin ve rutin bikarbonat "
                            "verilmesi serum efektif osmolaritesini hızla düşürerek ölümcül beyin ödemine yol açar."
                        ),
                    },
                    {
                        "text": (
                            "İlk saatte 10 mL/kg %0.9 NaCl vermek, potasyum 4.6 mEq/L olduğu için sıvıya hiç "
                            "potasyum eklemeden 0.2 U/kg/saat yüksek doz İV insülin infüzyonu başlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Potasyum desteği eklenmeden yüksek dozda başlanan insülin infüzyonu sonrası 2. "
                            "saatte serum potasyumu 2.4 mEq/L düzeyine düştü ve hastada ciddi hipokalemik aritmi gelişti."
                        ),
                        "teaching_point": (
                            "İnsülin potasyumu hızla hücre içine sokar; idrar çıkışı olan ve serum K <5.5 mEq/L "
                            "olan her DKA hastasında rehidratasyon sıvısına mutlaka 40 mEq/L potasyum eklenmelidir."
                        ),
                    },
                    {
                        "text": (
                            "İlk saat 10-20 mL/kg %0.9 NaCl verdikten sonra 40 mEq/L potasyum eklenmiş sıvıyla "
                            "defisiti 24-48 saate yaymak ve 0.05-0.1 U/kg/saat İV regüler insülin başlamak"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "ISPAD 2022 kılavuzuna göre ilk saat yalnız izotonik sıvı verilir; 1. saatin "
                            "sonunda potasyum içeren rehidratasyon sıvısı ve 0.05-0.1 U/kg/saat düşük doz İV "
                            "regüler insülin infüzyonu başlanarak hasta yoğun bakıma yatırılır."
                        ),
                        "new_finding": (
                            "İlk saat %0.9 NaCl restorasyonu sonrası potasyum destekli sıvı ve 0.1 U/kg/saat "
                            "İV regüler insülin infüzyonu başlandı; kan şekeri 250 mg/dL altına indiğinde sıvıya "
                            "%5 dekstroz eklenerek Çocuk Yoğun Bakım Ünitesine devredildi."
                        ),
                    },
                    {
                        "text": (
                            "İlk saatte %0.9 NaCl infüzyonu ile birlikte subkütan hızlı etkili insülin lispro "
                            "uygulamak ve kusması durunca hastayı endokrinoloji poliklinik kontrolü önerisiyle taburcu etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Orta-ağır dehidratasyonu ve pH 7.12 asidozu olan hastada subkütan insülin emilimi "
                            "yetersiz kaldı; 4. saatte metabolik asidozu derinleşen hastada bilinç bulanıklığı arttı."
                        ),
                        "teaching_point": (
                            "Orta ve ağır DKA (pH <7.20) hastalarında doku perfüzyonu bozuk olduğundan subkütan "
                            "insülin yerine titre edilebilir İV regüler insülin infüzyonu kullanılmalı ve hasta "
                            "mutlaka yatırılmalıdır."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "id": "Y07",
        "category": "👶 Ağlayan, Emmeyen, Huzursuz Bebek",
        "age": "9 Aylık",
        "gender": "Erkek",
        "complaint": "Aralıklı şiddetli ağlama krizleri, bacaklarını karnına çekme, safralı kusma ve ataklar arasında belirgin uyuklama",
        "history": (
            "Annesi Sarı Alana getiriyor: 'Sabah saatlerinden beri 15-20 dakikada bir aniden çığlık atarak "
            "ağlamaya başlıyor, rengi soluyor ve iki bacağını karnına doğru çekiyor. Kriz 2-3 dakika sürüp "
            "geçince tamamen bitkin düşüp uyukluyor. Az önce 2 kez sarı-yeşil renkli kustu.'"
        ),
        "final_diagnosis": "İleoçekal İnvajinasyon (İntususepsiyon)",
        "disposition": (
            "Sarı Alanda NPO + Nazogastrik Dekompresyon + İV Sıvı Resüsitasyonu -> USG Eşliğinde "
            "Hidrostatik/Pnömatik Redüksiyon ve Çocuk Cerrahisi Yatışı"
        ),
        "case_pearl": (
            "3 ay - 3 yaş arası süt çocuklarında periyodik kıvrandırıcı ağlama atakları, ataklar arasında "
            "belirgin letarji ve safralı kusma İleoçekal İnvajinasyon için tipiktir. Mukuslu-kanlı dışkılama "
            "geç bir bulgudur. Tanıda altın standart Batın USG (transvers kesitte hedef tahtası / target sign) "
            "olup, perforasyon veya peritonit yoksa ilk basamak tedavi hidrostatik veya pnömatik enema redüksiyonudur."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda İlk Değerlendirme ve Fizik Muayene",
                "question": (
                    "Periyodik kıvrandırıcı ağlama atakları, ataklar arası letarji ve safralı kusması olan 9 "
                    "aylık bu bebekte ilk muayenede öncelikli yaklaşımınız ne olmalıdır?"
                ),
                "options": [
                    {
                        "text": (
                            "Ataklar arasındaki belirgin uykuya meyil ve kusmayı santral sinir sistemi "
                            "enfeksiyonu bulgusu kabul ederek batın muayenesini erteleyip acil lomber ponksiyon hazırlığı yapmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Lomber ponksiyon hazırlığı sırasında bebek tekrar bacaklarını karnına çekerek "
                            "şiddetli ağlama krizi geçirdi ve bol miktarda safralı kustu; işlem sonunda BOS "
                            "bulguları tamamen normal saptandı."
                        ),
                        "teaching_point": (
                            "Süt çocuklarında periyodik karın ağrısı atakları arasında gelişen derin letarji, "
                            "endojen opioid salınımına bağlı klasik bir klinik bulgudur; safralı kusma "
                            "varlığında öncelikle akut batın muayenesi yapılmalıdır."
                        ),
                    },
                    {
                        "text": (
                            "Ağlama krizlerini süt çocuğu gaz sancısı olarak değerlendirip simetikon damla ve "
                            "rektal gliserin fitil uyguladıktan sonra bebeği Yeşil Alanda gözleme almak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Uygulanan gliserin fitil sonrası bezde mukuslu ve koyu pembe-kırmızı kanlı dışkı "
                            "görüldü; bebeğin safralı kusmaları devam etti ve taşikardisi derinleşerek kapiller "
                            "dolum zamanı 4 saniyeye uzadı."
                        ),
                        "teaching_point": (
                            "Dokuz aylık bir bebekte yeni başlayan periyodik kıvrandırıcı ağlama krizleri, "
                            "letarji ve safralı kusma asla fonksiyonel gaz sancısı olarak değerlendirilemez; "
                            "mekanik bağırsak tıkanıklığı dışlanmalıdır."
                        ),
                    },
                    {
                        "text": (
                            "Vital bulguları, atak dışı bilinç durumunu, sağ üst kadran palpasyonu ile sağ alt "
                            "kadran boşluğunu ve bezdeki dışkıyı değerlendirmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Kolik tarzda ağlama atakları, safralı kusma ve letarji ile başvuran süt çocuğunda "
                            "batın kadranlarının dikkatli palpasyonu, peritoneal irritasyon kontrolü ve "
                            "rektal/bez muayenesi en kritik ilk adımdır."
                        ),
                        "new_finding": (
                            "Vital Bulgular: Ateş 37.3°C, KTA 148/dk, SS 32/dk, TA 88/52 mmHg, KDZ 2-3 sn. Bebek "
                            "muayene başında uykuya meyilli iken aniden bacaklarını karnına çekerek ağlama atağı "
                            "geçirdi. Sakinleştiğinde sağ üst kadranda 3x2 cm boyutunda silindirik kitle palpe "
                            "edildi, sağ alt kadran boş hissedildi. Bezde mukuslu ve pembe-kırmızı kanlı dışkı "
                            "bulaşı görüldü. Tahta karın bulgusu yok."
                        ),
                    },
                    {
                        "text": (
                            "Kusmayı durdurmak amacıyla hemen intravenöz ondansetron yapıp ağızdan oral "
                            "rehidratasyon sıvısı denemesine başlamak ve iki saat sonra batın muayenesini tekrarlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Ağızdan verilen sıvıyı hemen safralı olarak kusan bebekte batın distansiyonu "
                            "belirginleşti ve 2 saatlik gecikme sonucunda kapiller dolum zamanı uzayarak "
                            "hipovolemi bulguları ağırlaştı."
                        ),
                        "teaching_point": (
                            "Safralı kusma aksi kanıtlanana kadar mekanik intestinal obstrüksiyon göstergesidir; "
                            "bu hastalarda oral alım derhal kesilmeli ve antiemetik verilerek oral besleme "
                            "denemesi yapılmamalıdır."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Stabilizasyon ve Görüntüleme Seçimi",
                "question": (
                    "Safralı kusması, sağ üst kadranda palpe edilen kitlesi ve mukuslu-kanlı dışkısı olan bu "
                    "bebekte ilk stabilizasyon ve görüntüleme planınız ne olmalıdır?"
                ),
                "options": [
                    {
                        "text": (
                            "Oral alımı kesmek, nazogastrik dekompresyon sağlamak, %0.9 NaCl ile intravenöz "
                            "sıvı resüsitasyonu başlamak ve acil batın ultrasonografisi istemek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Akut mekanik bağırsak obstrüksiyonu şüphesinde oral alımın kesilmesi, nazogastrik "
                            "dekompresyon, izotonik sıvı desteği ve yüksek duyarlılığa sahip batın "
                            "ultrasonografisi altın standart yaklaşımdır."
                        ),
                        "new_finding": (
                            "Nazogastrik sondadan safralı mide içeriği drene edildi ve 20 mL/kg %0.9 NaCl bolusu "
                            "sonrası KTA 126/dk düzeyine geriledi. BATIN USG: Sağ üst kadranda transvers kesitte "
                            "iç içe geçmiş konsantrik ekojenik ve hipoekoik bağırsak halkaları (3.2 cm çapında), "
                            "longitudinal kesitte ise tübüler katmanlı bağırsak segmenti izlendi. Batın içinde "
                            "serbest hava saptanmadı."
                        ),
                    },
                    {
                        "text": (
                            "Sadece ayakta direkt batın grafisi çekmek ve grafide hava-sıvı seviyesi görülmezse "
                            "mekanik tıkanıklığı dışlayarak hastaya oral beslenme denemesi yapmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Çekilen direkt batın grafisinde yalnızca sağ alt kadranda gaz azlığı izlendi, "
                            "belirgin hava-sıvı seviyesi görülmedi; ancak oral besleme sonrası bebeğin safralı "
                            "kusması ve letarjisi şiddetlendi."
                        ),
                        "teaching_point": (
                            "Direkt batın grafisi erken dönemde %25-30 oranında tamamen normal olabilir ve "
                            "mekanik obstrüksiyonu dışlamaz; yalnızca perforasyon (serbest hava) şüphesinde ek "
                            "bilgi sağlar."
                        ),
                    },
                    {
                        "text": (
                            "Damar yolu açıp sedasyon uyguladıktan sonra ultrasonografi beklemeksizin kontrastlı "
                            "tüm batın bilgisayarlı tomografisi çekerek bağırsak lümenini ve mezenteri değerlendirmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Dokuz aylık bebek yüksek doz iyonizan radyasyona ve sedasyon riskine maruz kaldı; "
                            "ayrıca kontrast hazırlığı nedeniyle kesin tedavi 2 saat gecikti."
                        ),
                        "teaching_point": (
                            "Süt çocuklarında bu klinik tabloda ultrasonografi %98-100 duyarlılık ve özgüllüğe "
                            "sahiptir; radyasyon ve sedasyon gerektiren bilgisayarlı tomografi ilk basamakta "
                            "endike değildir."
                        ),
                    },
                    {
                        "text": (
                            "Mukuslu ve kanlı dışkılama nedeniyle akut bakteriyel enterokolit düşünerek gaita "
                            "kültürü göndermek, intravenöz seftriakson başlamak ve görüntülemeyi ertesi güne bırakmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Antibiyotik tedavisine rağmen bebeğin kıvrandırıcı ağlama atakları ve safralı "
                            "kusmaları devam etti; 12 saat sonra batın distansiyonu, ateş ve peritoneal "
                            "irritasyon bulguları gelişti."
                        ),
                        "teaching_point": (
                            "Mukuslu-kanlı dışkı bakteriyel dizanteri ile karışabilir; ancak safralı kusma, "
                            "periyodik ağlama krizleri ve sağ üst kadranda kitle varlığında acil ultrasonografi "
                            "geciktirilmemelidir."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": (
                    "Klinik tablo ve batın ultrasonografisinde saptanan iç içe geçmiş konsantrik bağırsak "
                    "halkaları görünümü doğrultusunda kesin tanınız nedir?"
                ),
                "options": [
                    {
                        "text": "İnfantil Hipertrofik Pilor Stenozu",
                        "is_correct": False,
                        "scenario_update": (
                            "Pilor stenozu yaşamın ilk 3-6 haftasında safrasız fışkırır kusma ile seyreder; 9 "
                            "aylık bebekte safralı kusma ve kanlı dışkı pilor stenozu ile uyumsuzdur."
                        ),
                        "teaching_point": (
                            "Hipertrofik pilor stenozunda tıkanıklık pilor düzeyinde olduğu için kusma her "
                            "zaman safrasızdır ve hipokloremik hipokalemik metabolik alkaloz görülür."
                        ),
                    },
                    {
                        "text": "Akut İnvaziv Bakteriyel Gastroenterit (Şigelloz)",
                        "is_correct": False,
                        "scenario_update": (
                            "Ultrasonografide saptanan 3.2 cm çapındaki iç içe geçmiş bağırsak halkaları (hedef "
                            "işareti) enfeksiyöz koliti değil mekanik invajinasyonu göstermektedir."
                        ),
                        "teaching_point": (
                            "Bakteriyel enterokolitte yüksek ateş ve sık sulu-kanlı ishal ön plandadır; USG de "
                            "hedef tahtası (target sign) bulgusu görülmez."
                        ),
                    },
                    {
                        "text": "Meckel Divertikülüne Bağlı Alt GİS Kanaması",
                        "is_correct": False,
                        "scenario_update": (
                            "Meckel divertikülü tipik olarak ağrısız masif rektal kanama yapar; bu hastada ise "
                            "şiddetli kolik ağrı atakları ve USG ile kanıtlanmış invajinasyon mevcuttur."
                        ),
                        "teaching_point": (
                            "Meckel divertikülü süt çocuğunda invajinasyon için bir sürükleyici nokta (lead "
                            "point) olabilir ancak mevcut akut klinik tablo ileoçekal invajinasyondur."
                        ),
                    },
                    {
                        "text": "Akut İleoçekal İnvajinasyon (İntususepsiyon)",
                        "is_correct": True,
                        "explanation": (
                            "Distal ileumun çekum ve çıkan kolon lümeni içine teleskop gibi girmesiyle oluşan "
                            "ileoçekal invajinasyon, USG de transvers kesitte hedef tahtası (target/donut sign) "
                            "ve longitudinal kesitte psödo-böbrek görünümü verir."
                        ),
                        "new_finding": "Kesin Tanı: Akut İleoçekal İnvajinasyon (İntususepsiyon).",
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Tedavi Seçimi ve Yatış Planı",
                "question": (
                    "Perforasyon, peritonit veya dekompanse şok bulgusu olmayan bu ileoçekal invajinasyon "
                    "hastasında en uygun tedavi ve izlem yaklaşımı hangisidir?"
                ),
                "options": [
                    {
                        "text": (
                            "Radyolojik redüksiyon girişimi perforasyon riski taşıdığı için enema denemeden "
                            "hastayı doğrudan acil eksploratris laparotomi ve bağırsak rezeksiyonu için ameliyathaneye almak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Peritonit veya perforasyon bulgusu olmayan hastada ameliyatsız redüksiyon şansı "
                            "kullanılmadan yapılan laparotomi, gereksiz genel anestezi ve cerrahi morbiditeye yol açtı."
                        ),
                        "teaching_point": (
                            "Cerrahi laparotomi yalnızca serbest hava (perforasyon), yaygın peritonit, refrakter "
                            "şok veya radyolojik redüksiyonun başarısız olduğu durumlarda endikedir."
                        ),
                    },
                    {
                        "text": (
                            "Çocuk Cerrahisi konsültasyonu ile ultrasonografi veya skopi eşliğinde hidrostatik "
                            "veya pnömatik enema redüksiyonu uygulamak ve gözlem için yatırmak"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Komplike olmayan ileoçekal invajinasyonda ilk tercih %85-90 başarı oranına sahip "
                            "ultrasonografi eşliğinde hidrostatik (serum fizyolojik) veya skopi eşliğinde "
                            "pnömatik (hava) redüksiyondur; işlem sonrası erken nüks (%5-10) açısından hasta izlenir."
                        ),
                        "new_finding": (
                            "Çocuk Cerrahisi ve Radyoloji işbirliği ile USG kılavuzluğunda hidrostatik "
                            "redüksiyon başarıyla uygulandı; ileoçekal valvden serbest sıvı geçişi doğrulandı "
                            "ve hasta 24 saatlik gözlem için yatırıldı."
                        ),
                    },
                    {
                        "text": (
                            "Ultrasonografi eşliğinde hidrostatik redüksiyon başarıyla tamamlandıktan hemen "
                            "sonra oral beslenmeye geçip hastayı 1. saatte acil servisten eve taburcu etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "İşlemden 1 saat sonra eve gönderilen bebekte 6 saat sonra evde tekrar şiddetli "
                            "ağlama krizleri ve safralı kusma ile erken rekürrens (nüks) gelişti."
                        ),
                        "teaching_point": (
                            "Başarılı hidrostatik veya pnömatik redüksiyon sonrasında vakaların %5-10 unda "
                            "özellikle ilk 24 saat içinde erken nüks görülebileceğinden hastalar yakın gözlem "
                            "altında tutulmalıdır."
                        ),
                    },
                    {
                        "text": (
                            "Bağırsak ansının kendiliğinden açılabileceğini düşünerek enema redüksiyonu yapmadan "
                            "sadece intravenöz sıvı ve spazmolitik ilaç verip 24 saat klinik izlemde beklemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "İleoçekal invajinasyonda sadece sıvı ve spazmolitik ile beklenmesi sonucu bağırsak "
                            "duvarında venöz konjesyon, transmural iskemi, nekroz ve 18. saatte perforasyon gelişti."
                        ),
                        "teaching_point": (
                            "İleoçekal (kolonik) invajinasyonlar kendiliğinden açılmaz ve acil redüksiyon "
                            "gerektirir; yalnız asemptomatik, kısa segment (<2 cm) ince bağırsak (ileo-ileal) "
                            "invajinasyonları yakın USG takibiyle izlenebilir."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "id": "Y08",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "4 Yaş",
        "gender": "Erkek",
        "complaint": "Yüksek ateş (40.1°C), şiddetli baş ağrısı, fışkırır tarzda kusma, ışıktan rahatsız olma ve uykuya meyil",
        "history": (
            "Sarı Alana kucakta getiriliyor: 'Dün akşamdan beri ateşi 40°C'ye çıktı, ateş düşürücülere rağmen "
            "düşmüyor. Başım çok ağrıyor deyip ağlıyor, odanın ışığını açtığımızda gözlerini sıkıca kapatıyor. "
            "Bugün 4 kez fışkırır gibi kustu ve boynunu öne doğru eğmek istemiyor. Son 1 saattir sorularımıza "
            "çok yavaş cevap veriyor.'"
        ),
        "final_diagnosis": "Akut Bakteriyel Menenjit (Pnömokoksik Menenjit - S. pneumoniae)",
        "disposition": (
            "Sarı Alanda Kan Kültürü + Lomber Ponksiyon -> İlk Antibiyotik Dozu Öncesi İV Deksametazon + "
            "Menenjit Dozunda Seftriakson ve Vankomisin -> Çocuk Yoğun Bakım Yatışı"
        ),
        "case_pearl": (
            "Yüksek ateş, baş ağrısı, fışkırır tarzda kusma, fotofobi, letarji ve meninks irritasyon bulguları "
            "(ense sertliği, Kernig ve Brudzinski) Akut Bakteriyel Menenjit için klasiktir. Lomber ponksiyon "
            "kontrendikasyonu (herniasyon bulgusu, fokal nörolojik defisit, kardiyopulmoner instabilite, "
            "koagülopati/purpura) yoksa hızla LP yapılmalı; ilk antibiyotik dozundan hemen önce/eş zamanlı "
            "0.15 mg/kg İV Deksametazon ve ardından menenjit dozunda Seftriakson (100 mg/kg/gün) + Vankomisin "
            "(60 mg/kg/gün) başlanmalıdır."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda Nörolojik ve Sistemik Değerlendirme",
                "question": (
                    "40.1°C ateşi, fotofobisi, fışkırır tarzda kusması ve uykuya meyili olan 4 yaşındaki bu "
                    "çocukta ilk muayenede öncelikli yaklaşımınız ne olmalıdır?"
                ),
                "options": [
                    {
                        "text": (
                            "Vital bulguları, GKS ve pupilleri, fokal nörolojik defisitleri, pasif boyun "
                            "fleksiyonunda direnç ile kalça-diz ekstansiyon manevralarını ve döküntüyü değerlendirmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Akut santral sinir sistemi enfeksiyonu şüphesinde hem spinal zar irritasyon "
                            "bulguları hem de kafa içi basınç artışı bulguları (bradikardi, hipertansiyon, "
                            "anizokori, fokal defisit) ve purpurik döküntü hızla kontrol edilmelidir."
                        ),
                        "new_finding": (
                            "Vital Bulgular: Ateş 40.0°C, KTA 138/dk, SS 28/dk, TA 102/65 mmHg, SpO2 %98, KDZ "
                            "2 sn. GKS 13 (uykuya meyilli, sesli uyaranla göz açıyor). Pasif boyun "
                            "fleksiyonunda belirgin direnç mevcut; boyun öne eğildiğinde kalça ve dizlerde "
                            "refleks fleksiyon gelişiyor ve uyluk fleksiyonda iken bacak ekstansiyonunda "
                            "ağrılı kısıtlılık saptanıyor. Pupiller izokorik, papilödem veya fokal nörolojik "
                            "defisit yok, ciltte peteşi/purpura yok."
                        ),
                    },
                    {
                        "text": (
                            "Şiddetli baş ağrısı, kusma ve ışıktan rahatsız olmayı pediatrik migren atağı olarak "
                            "değerlendirip karanlık odada intravenöz parasetamol ve ondansetron vererek izlemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Yalnızca analjezik ve antiemetik verilerek bekletilen çocukta 1 saat sonra "
                            "jeneralize tonik-klonik konvülziyon gelişti ve bilinç durumu GKS 9 düzeyine geriledi."
                        ),
                        "teaching_point": (
                            "Kırk derece ateş, letarji ve pasif boyun fleksiyonunda direnç bulunan bir çocukta "
                            "tablo asla primer baş ağrısı veya migren olarak açıklanamaz; akut santral sinir "
                            "sistemi enfeksiyonu dışlanmalıdır."
                        ),
                    },
                    {
                        "text": (
                            "Yüksek ateş ve baş ağrısını akut bakteriyel rinosinüzite bağlayarak nörolojik "
                            "muayene yapmadan intravenöz amoksisilin-klavulanat uygulayıp gözlem odasında ateşin düşmesini beklemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Standart dozda verilen amoksisilin-klavulanat kan-beyin bariyerini yeterli düzeyde "
                            "geçemedi; 3 saat içinde hastanın uykuya meyili derinleşti ve periferik dolaşım "
                            "bozukluğu gelişti."
                        ),
                        "teaching_point": (
                            "Fışkırır tarzda kusma, fotofobi, bilinç değişikliği ve boyun hareketlerinde "
                            "kısıtlılık varlığında üst solunum yolu enfeksiyonu düşünülerek standart doz "
                            "antibiyotikle yetinilmesi ağır komplikasyonlara yol açar."
                        ),
                    },
                    {
                        "text": (
                            "Uykuya meyilli çocuğu muayene etmeden ve damar yolu açmadan önce kafa içi kitleyi "
                            "dışlamak amacıyla doğrudan kraniyal manyetik rezonans görüntülemeye göndermek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Stabilizasyon ve ilk değerlendirme yapılmadan uzun süreli MR çekimine gönderilen "
                            "hastada radyoloji ünitesinde ateşli konvülziyon gelişti ve acil müdahale gecikti."
                        ),
                        "teaching_point": (
                            "Akut ateşli ve letarjik çocukta ilk adım yatak başı vital bulguların, dolaşımın ve "
                            "nörolojik muayenenin değerlendirilmesidir; stabilizasyon sağlanmadan hasta uzun "
                            "süreli görüntülemeye gönderilmez."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Laboratuvar ve Beyin Omurilik Sıvısı İnceleme Yaklaşımı",
                "question": (
                    "Hemodinamisi stabil olan, papilödemi, fokal nörolojik defisiti veya cilt döküntüsü "
                    "bulunmayan bu hastada inceleme ve girişim planınız ne olmalıdır?"
                ),
                "options": [
                    {
                        "text": (
                            "Kan kültürü ve lomber ponksiyon yapmadan hemen antibiyotik başlamak, 24 saat sonra "
                            "klinik yanıt alındıktan sonra beyin omurilik sıvısı örneği almak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Kontrendikasyon olmadığı halde ertelenen ve antibiyotik verildikten 24 saat sonra "
                            "yapılan lomber ponksiyonda beyin omurilik sıvısı kültürü steril kaldı; etken ve "
                            "antibiyotik duyarlılığı saptanamadı."
                        ),
                        "teaching_point": (
                            "Herniasyon riski, fokal defisit, şok veya koagülopati gibi bir kontrendikasyon "
                            "yoksa antibiyotik dozundan hemen önce kan kültürü ve lomber ponksiyon yapılarak "
                            "etken izolasyonu sağlanmalıdır."
                        ),
                    },
                    {
                        "text": (
                            "Papilödem ve fokal defisit olmamasına rağmen önce kraniyal bilgisayarlı tomografi "
                            "çekmek ve radyoloji raporu çıkana kadar 3 saat boyunca antibiyotik vermeden beklemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Kraniyal BT tamamen normal raporlandı; ancak 3 saatlik süreçte antibiyotik "
                            "başlanmadığı için hastada septik şok ve ağır nörolojik kötüleşme gelişti."
                        ),
                        "teaching_point": (
                            "Fokal nörolojik defisit, papilödem, koma (GKS <10) veya immünsüpresyon yoksa lomber "
                            "ponksiyon öncesi rutin kraniyal BT endike değildir; görüntüleme yapılacaksa bile "
                            "kan kültürü alınıp ampirik tedavi geciktirilmeden başlanmalıdır."
                        ),
                    },
                    {
                        "text": (
                            "Damar yolu açarak kan kültürü, hemogram, CRP, prokalsitonin ve eş zamanlı glukoz "
                            "alıp kontrendikasyon bulunmadığından steril koşullarda lomber ponksiyon uygulamak"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Hemodinamik instabilite, fokal nörolojik bulgu veya papilödem olmayan hastada kan "
                            "kültürü ve eş zamanlı kan şekeri alınarak derhal lomber ponksiyon yapılmalı ve "
                            "beyin omurilik sıvısı incelenmelidir."
                        ),
                        "new_finding": (
                            "KAN: WBC 24.500/mm³, CRP 165 mg/L, Prokalsitonin 14 ng/mL, Eş zamanlı Kan Şekeri "
                            "100 mg/dL, Koagülasyon normal. BOS BULGULARI: Görünüm bulanık, açılış basıncı "
                            "artmış, hücre sayımı 1.850/mm³ (%92 parçalı çekirdekli lökosit), BOS proteini "
                            "185 mg/dL, BOS glukozu 18 mg/dL (BOS/kan glukoz oranı 0.18). Gram boyamada bol "
                            "lökosit ve Gram pozitif diplokoklar görüldü."
                        ),
                    },
                    {
                        "text": (
                            "Lomber ponksiyon invaziv bir işlem olduğu için yalnızca kan kültürü, tam idrar "
                            "tetkiki ve nazofarengeal viral sürüntü göndererek klinik izleme almak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Nazofarengeal sürüntü ve idrar tetkiki negatif sonuçlandı; beyin omurilik sıvısı "
                            "incelenmediği için santral sinir sistemi enfeksiyonunun şiddeti ve etkeni belirlenemedi."
                        ),
                        "teaching_point": (
                            "Santral sinir sistemi enfeksiyonu şüphesinde kesin etiyolojik ayrım ve uygun tedavi "
                            "süresi yalnızca beyin omurilik sıvısı analizi (hücre, protein, glukoz, Gram boyama "
                            "ve kültür/PCR) ile belirlenebilir."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": (
                    "Bulanık görünümde BOS, 1.850/mm³ nötrofil hakimiyetli pleositoz, yüksek BOS proteini "
                    "(185 mg/dL), düşük BOS glukozu (18 mg/dL) ve Gram (+) diplokok bulgusu ile kesin tanınız nedir?"
                ),
                "options": [
                    {
                        "text": "Akut Enteroviral (Aseptik) Menenjit",
                        "is_correct": False,
                        "scenario_update": (
                            "Viral menenjitlerde BOS genellikle berraktır, hücre sayısı çoğunlukla <500/mm³ "
                            "olup lenfosit hakimiyeti vardır, BOS glukozu normaldir ve Gram boyamada bakteri görülmez."
                        ),
                        "teaching_point": (
                            "Belirgin hipoglikoraji (BOS/kan glukoz oranı <0.4), yüksek protein (>100 mg/dL), "
                            ">1000/mm³ nötrofilik pleositoz ve pozitif Gram boyama bakteriyel menenjiti gösterir."
                        ),
                    },
                    {
                        "text": "Akut Bakteriyel Menenjit (Pnömokoksik Menenjit)",
                        "is_correct": True,
                        "explanation": (
                            "Bulanık BOS, >1000/mm³ PNL hakimiyeti, belirgin hipoglikoraji (18 mg/dL), yüksek "
                            "protein ve Gram boyamada Gram (+) diplokokların görülmesi Streptococcus pneumoniae "
                            "kaynaklı akut bakteriyel menenjit için tanısaldır."
                        ),
                        "new_finding": "Kesin Tanı: Akut Bakteriyel Menenjit (Streptococcus pneumoniae).",
                    },
                    {
                        "text": "Herpes Simpleks Virüs (HSV-1) Ensefaliti",
                        "is_correct": False,
                        "scenario_update": (
                            "HSV ensefalitinde fokal nöbetler, temporal lob bulguları, BOS ta lenfositik "
                            "pleositoz, eritrosit varlığı ve normal/hafif düşük glukoz beklenir; Gram (+) diplokok görülmez."
                        ),
                        "teaching_point": (
                            "Gram boyamada Gram (+) diplokok saptanması ve ağır hipoglikoraji doğrudan "
                            "pnömokoksik bakteriyel menenjiti doğrular."
                        ),
                    },
                    {
                        "text": "Santral Sinir Sistemi Tüberküloz Menenjiti",
                        "is_correct": False,
                        "scenario_update": (
                            "Tüberküloz menenjiti haftalar süren subakut prodromla başlar, BOS ta lenfosit "
                            "hakimiyeti vardır ve Gram boyamada Gram (+) diplokok izlenmez."
                        ),
                        "teaching_point": (
                            "Akut 24 saatlik fulminan başlangıç, nötrofilik pleositoz ve Gram (+) diplokoklar "
                            "akut piyojenik pnömokoksik menenjit tablosudur."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Ampirik Antibiyoterapi, Steroid Zamanlaması ve Yatış",
                "question": (
                    "Akut bakteriyel menenjit tanısı konulan 4 yaşındaki bu hastada kılavuzlara en uygun ilk "
                    "doz tedavi ve yatış protokolü hangisidir?"
                ),
                "options": [
                    {
                        "text": (
                            "Standart enfeksiyon dozunda 50 mg/kg/gün İV seftriakson monoterapisi başlamak, "
                            "vankomisin eklememek ve inflamasyonu baskılamak için deksametazonu antibiyotikten 6 saat sonra uygulamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Düşük doz seftriakson BOS ta yeterli bakterisidal konsantrasyona ulaşamadı, "
                            "sefalosporin dirençli pnömokok olasılığı kapsanmadı ve antibiyotikten saatler sonra "
                            "verilen deksametazon işitme kaybını önlemede etkisiz kaldı."
                        ),
                        "teaching_point": (
                            "Bakteriyel menenjitte seftriakson mutlaka 100 mg/kg/gün (menenjit dozu) verilmeli, "
                            "dirençli S. pneumoniae için vankomisin (60 mg/kg/gün) eklenmeli ve deksametazon ilk "
                            "antibiyotik dozundan önce/eş zamanlı uygulanmalıdır."
                        ),
                    },
                    {
                        "text": (
                            "Kan-beyin bariyerini geçmesi için İV ampisilin ve gentamisin kombinasyonu başlamak, "
                            "enfeksiyonu yayabileceği düşüncesiyle kortikosteroid vermekten kaçınmak ve genel servise yatırmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Yenidoğan döneminden sonra ampisilin + gentamisin kombinasyonu penisilin dirençli "
                            "S. pneumoniae için yetersiz kaldı ve hastada sensorinöral işitme kaybı gelişti."
                        ),
                        "teaching_point": (
                            "Bir aydan büyük çocuklarda ampirik bakteriyel menenjit tedavisinde 3. kuşak "
                            "sefalosporin (seftriakson/sefotaksim) + vankomisin kullanılır; ilk doz öncesi "
                            "deksametazon işitme kaybı ve nörolojik sekeli azaltır."
                        ),
                    },
                    {
                        "text": (
                            "Menenjit dozunda 100 mg/kg/gün İV seftriakson ve 60 mg/kg/gün İV vankomisin "
                            "başlamak, ödemi azaltmak için hastaya günlük %50 fazla hipotonik idame sıvısı vermek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Aşırı ve hipotonik sıvı verilen hastada uygunsuz ADH salınımı sendromu (SIADH) "
                            "zemininde serum sodyumu 124 mEq/L düzeyine düştü ve beyin ödemi ile konvülziyon gelişti."
                        ),
                        "teaching_point": (
                            "Bakteriyel menenjitte SIADH riski yüksek olduğundan aşırı ve hipotonik sıvı "
                            "yüklemesinden kaçınılmalı; övolemiyi koruyacak şekilde izotonik idame sıvısı "
                            "tercih edilerek sodyum yakından izlenmelidir."
                        ),
                    },
                    {
                        "text": (
                            "İlk antibiyotik dozundan önce 0.15 mg/kg İV deksametazon uygulayıp 100 mg/kg/gün "
                            "İV seftriakson ve 60 mg/kg/gün İV vankomisin başlayarak yatırmak"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "IDSA ve AAP kılavuzlarına göre >1 ay çocuklarda ampirik menenjit tedavisi "
                            "Seftriakson (100 mg/kg/gün, 2 dozda) + Vankomisin (60 mg/kg/gün, 4 dozda) "
                            "kombinasyonudur; ilk antibiyotik dozundan hemen önce/eş zamanlı verilen "
                            "Deksametazon (0.15 mg/kg) bakteriyolize bağlı subaraknoid inflamasyonu ve işitme "
                            "kaybını azaltır."
                        ),
                        "new_finding": (
                            "İlk doz öncesi 0.15 mg/kg İV Deksametazon, ardından menenjit dozunda İV Seftriakson "
                            "ve Vankomisin uygulandı; hasta yakın nörolojik izlem ve SIADH/elektrolit takibi "
                            "amacıyla Çocuk Yoğun Bakım Ünitesine yatırıldı."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "id": "Y09",
        "category": "👶 Ağlayan, Emmeyen, Huzursuz Bebek",
        "age": "6 Aylık",
        "gender": "Kız",
        "complaint": "İki gündür düşmeyen 39.8°C ateş, belirgin huzursuzluk, tekrarlayan kusma ve emmede azalma",
        "history": (
            "Annesi Sarı Alana getiriyor: 'İki gündür ateşi 39.8°C'ye kadar çıkıyor, ateş düşürücü verince "
            "38.5°C'ye ancak iniyor ve titreyerek tekrar yükseliyor. Burnu akmıyor, öksürmüyor, ishali de yok "
            "ama bugün 3 kez kustu ve çok huzursuz. Bezini açtığımızda idrarının normalden daha ağır koktuğunu fark ettik.'"
        ),
        "final_diagnosis": "Akut Piyelonefrit (Ateşli Üst İdrar Yolu Enfeksiyonu)",
        "disposition": (
            "Sarı Alanda Steril Mesane Kateterizasyonu ile Kültür + Kan Tetkikleri -> Parenteral Antibiyoterapi "
            "(İV Seftriakson), Üriner USG Planı ve Çocuk Servisi Yatışı"
        ),
        "case_pearl": (
            "2-24 ay arası süt çocuklarında odağı belirsiz ≥39°C ateş varlığında en sık ciddi bakteriyel "
            "enfeksiyon Akut Piyelonefrittir. Tuvalet eğitimi olmayan ateşli bebekte antibiyotik başlanmadan "
            "önce steril mesane kateterizasyonu veya suprapubik aspirasyon ile idrar kültürü alınmalıdır; torba "
            "idrarı yüksek kontaminasyon oranı nedeniyle kültür için kullanılmaz. Kusması olan veya küçük süt "
            "çocuklarında parenteral antibiyoterapi başlanır ve Üriner Sistem USG planlanır."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda Odak Araştırması ve Sistemik Muayene",
                "question": (
                    "İki gündür 39.8°C ateşi, huzursuzluğu ve kusması olan 6 aylık bu kız bebekte ilk "
                    "değerlendirmede yaklaşımınız ne olmalıdır?"
                ),
                "options": [
                    {
                        "text": (
                            "Solunum semptomu olmasa bile yüksek ateş ve kusmayı gizli bakteriyel pnömoni "
                            "bulgusu kabul ederek fizik muayeneyi erteleyip doğrudan arka-ön akciğer grafisi çektirmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Takipnesi, çekilmesi ve öksürüğü olmayan bebekte çekilen akciğer grafisi tamamen "
                            "normal saptandı; bebek gereksiz radyasyona maruz kaldı ve asıl enfeksiyon odağı aydınlatılamadı."
                        ),
                        "teaching_point": (
                            "Solunum sayısı ve akciğer oskültasyonu tamamen normal olan, öksürük veya rinit "
                            "bulgusu bulunmayan ateşli süt çocuklarında rutin akciğer grafisi önerilmez."
                        ),
                    },
                    {
                        "text": (
                            "Altıncı ayda başlayan yüksek ateş ve huzursuzluğu diş çıkarma dönemine bağlayarak "
                            "oral ibuprofen şurup verip bebeği Yeşil Alandan eve taburcu etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Ateş düşürücü verilerek eve gönderilen bebek 18 saat sonra 40.2°C ateş, letarji, "
                            "uzamış kapiller dolum zamanı ve septik şok tablosuyla acil servise tekrar getirildi."
                        ),
                        "teaching_point": (
                            "Diş çıkarma süreci hiçbir zaman ≥38.5°C üzerinde yüksek ateş ve tekrarlayan kusma "
                            "nedeni olarak kabul edilemez; 39.8°C ateşte gizli bakteriyel enfeksiyon odağı "
                            "mutlaka araştırılmalıdır."
                        ),
                    },
                    {
                        "text": (
                            "Ateşi hızla kontrol altına almak ve bakteriyemi riskini önlemek için kültür "
                            "örnekleri almadan hemen intramüsküler 50 mg/kg seftriakson uygulayıp gözleme almak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Örnek alınmadan yapılan seftriakson enjeksiyonu sonrasında bebeğin ateşi kısmen "
                            "geriledi ancak daha sonra alınan kültürlerde üreme olmadığından kesin tanı ve "
                            "antibiyogram duyarlılığı belirlenemedi."
                        ),
                        "teaching_point": (
                            "Hemodinamik olarak stabil olan ateşli süt çocuğunda ampirik antibiyotik verilmeden "
                            "önce mutlaka uygun yöntemle mikrobiyolojik kültür örnekleri alınmalıdır."
                        ),
                    },
                    {
                        "text": (
                            "Vital bulguları, periferik dolaşımı, ön fontanel ve nörolojik durumu, "
                            "kulak-boğaz-akciğer-cilt muayenesini ve suprapubik ile kostovertebral bölge hassasiyetini eksiksiz olarak değerlendirmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Odağı ilk bakışta belli olmayan ≥39°C ateşli süt çocuğunda tüm sistemlerin "
                            "muayenesi yapılmalı, meninks irritasyonu dışlanmalı ve üriner sistem muayenesi "
                            "dahil gizli enfeksiyon odakları taranmalıdır."
                        ),
                        "new_finding": (
                            "Vital Bulgular: Ateş 39.7°C, KTA 160/dk, SS 36/dk, TA 86/50 mmHg, KDZ 2 sn. Bebek "
                            "huzursuz ancak uyanık, ön fontanel normal bombelikte, pasif boyun fleksiyonu "
                            "serbest. Otoskopi, orofarenks ve akciğer oskültasyonu tamamen doğal, ciltte "
                            "döküntü yok. Suprapubik bölge ve kostovertebral açı palpasyonunda bebeğin ağlaması "
                            "ve huzursuzluğu belirgin artıyor."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Uygun Örnek Alma Yöntemi ve Laboratuvar Planı",
                "question": (
                    "Görünür üst solunum yolu odağı saptanmayan, 39.7°C ateşi ve kusması olan 6 aylık bu kız "
                    "bebekte kesin odak tespiti için hangi tetkikleri nasıl istemelisiniz?"
                ),
                "options": [
                    {
                        "text": (
                            "Perine cildine steril olmayan toplama torbası yapıştırarak hem tam idrar tetkiki "
                            "hem de idrar kültürü göndermek ve kan tetkiki almadan sonucu beklemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Torba örneğinde lökosit esteraz pozitif saptandı; ancak aynı torbadan gönderilen "
                            "kültürde perine florası bulaşına bağlı üç farklı mikroorganizma (karışık deri "
                            "florası) ürediği için sonuç geçersiz sayıldı."
                        ),
                        "teaching_point": (
                            "Tuvalet eğitimi olmayan çocuklarda torba örneği %85 e varan yalancı pozitiflik "
                            "(kontaminasyon) oranına sahiptir; torba yalnız taramada negatif çıkarsa dışlama "
                            "sağlar, kültür için asla kullanılmaz."
                        ),
                    },
                    {
                        "text": (
                            "Steril mesane kateterizasyonu ile tam idrar tetkiki, mikroskopi ve idrar kültürü "
                            "almak; hemogram, CRP, prokalsitonin ve kan kültürü göndermek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "AAP kılavuzuna göre tuvalet eğitimi olmayan ateşli süt çocuğunda antibiyotik "
                            "öncesi kültür için altın standart steril mesane kateterizasyonu veya suprapubik "
                            "aspirasyondur; kusması olan bebekte akut faz reaktanları ve kan kültürü de alınmalıdır."
                        ),
                        "new_finding": (
                            "KATETER İDRARI: Görünüm bulanık, Lökosit Esteraz +++, Nitrit Pozitif (+), "
                            "Mikroskopide her sahada 40-50 lökosit ve bol bakteri. KAN TETKİKLERİ: WBC "
                            "19.600/mm³ (%80 nötrofil), CRP 94 mg/L, Prokalsitonin 3.8 ng/mL, Üre 24 mg/dL, "
                            "Kreatinin 0.35 mg/dL. İdrar ve kan kültürleri ekime gönderildi."
                        ),
                    },
                    {
                        "text": (
                            "Yalnızca parmak ucu CRP ve tam kan sayımı bakmak, lökositoz saptanırsa "
                            "kateterizasyon ile bebeği huzursuz etmeden doğrudan oral amoksisilin-klavulanat başlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "İdrar incelemesi ve kültürü alınmadan başlanan oral antibiyotik kusma nedeniyle "
                            "tolere edilemedi; ayrıca enfeksiyon odağı kanıtlanamadığı için uygun görüntüleme "
                            "ve izlem planı yapılamadı."
                        ),
                        "teaching_point": (
                            "Odağı belirsiz yüksek ateşi olan <24 ay süt çocuklarında tek başına hemogram ve "
                            "CRP odak belirlemez; antibiyotik öncesi mutlaka kateter veya suprapubik "
                            "aspirasyonla idrar örneği alınmalıdır."
                        ),
                    },
                    {
                        "text": (
                            "Kateterizasyon yerine bebeğin bezini sıkıp alınan idrarda dipstick testi yapmak ve "
                            "negatif çıkarsa üriner kaynaklı enfeksiyonu tamamen dışlayarak taburcu etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Bezden sıkılarak alınan örnekte bezin emici polimerleri lökositleri tuttuğu ve "
                            "küçük bebeklerde sık mesane boşalması nedeniyle nitrit negatif kaldığı için tanı atlandı."
                        ),
                        "teaching_point": (
                            "Bezden sıkılarak alınan örnek güvenilir değildir; ayrıca süt çocukları sık idrar "
                            "yaptığından mesanede bekleme süresi kısa olur ve nitrit testi %50 den fazla vakada "
                            "yalancı negatif çıkabilir."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": (
                    "39.8°C ateş, kusma, CRP 94 mg/L, Prokalsitonin 3.8 ng/mL ve kateter idrarında belirgin "
                    "piyüri ile nitrit pozitifliği saptanan bu bebekte kesin tanınız nedir?"
                ),
                "options": [
                    {
                        "text": "Ateşsiz Akut Basit Sistit (Alt İYE)",
                        "is_correct": False,
                        "scenario_update": (
                            "Hastada 39.8°C ateş, tekrarlayan kusma ve belirgin akut faz reaktan yüksekliği "
                            "(CRP 94 mg/L, PCT 3.8 ng/mL) mevcut olup tablo alt üriner sistemle sınırlı değildir."
                        ),
                        "teaching_point": (
                            "Süt çocuklarında ≥38.5-39°C ateş ve sistemik inflamasyon bulguları eşlik eden idrar "
                            "yolu enfeksiyonları renal parankim tutulumunu (akut piyelonefrit) gösterir."
                        ),
                    },
                    {
                        "text": "Asemptomatik Bakteriüri ve Viral ÜSYE",
                        "is_correct": False,
                        "scenario_update": (
                            "Hastada viral üst solunum yolu bulgusu yoktur; kateter idrarında her sahada 40-50 "
                            "lökosit (belirgin piyüri) ve yüksek prokalsitonin gerçek doku invazyonunu kanıtlamaktadır."
                        ),
                        "teaching_point": (
                            "Asemptomatik bakteriüride klinik semptom, yüksek akut faz reaktanı ve gerçek "
                            "piyüri bulunmaz; tedavi gerektirmez."
                        ),
                    },
                    {
                        "text": "Akut Piyelonefrit (Ateşli Üst İdrar Yolu Enfeksiyonu)",
                        "is_correct": True,
                        "explanation": (
                            "Yüksek ateş, kusma, CRP ve prokalsitonin yüksekliği ile birlikte kateter idrarında "
                            "piyüri ve nitrit pozitifliği akut renal parankimal enfeksiyonu (Akut Piyelonefrit) doğrular."
                        ),
                        "new_finding": "Kesin Tanı: Akut Piyelonefrit (Ateşli Üst İdrar Yolu Enfeksiyonu).",
                    },
                    {
                        "text": "Akut Poststreptokoksik Glomerülonefrit (APSGN)",
                        "is_correct": False,
                        "scenario_update": (
                            "Altı aylık bebekte APSGN son derece nadirdir; ayrıca yüksek ateş, prokalsitonin "
                            "yüksekliği ve nitrit pozitifliği bakteriyel piyelonefrit için tipiktir."
                        ),
                        "teaching_point": (
                            "APSGN genellikle >2-3 yaş çocuklarda streptokoksik enfeksiyondan 1-3 hafta sonra "
                            "makroskopik hematüri, ödem ve hipertansiyon ile başvurur; nitrit pozitifliği görülmez."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Tedavi, Görüntüleme Zamanlaması ve Yatış Planı",
                "question": (
                    "Tekrarlayan kusması olan 6 aylık bu akut piyelonefrit hastasında kılavuzlara en uygun "
                    "antibiyoterapi, görüntüleme ve izlem planı hangisidir?"
                ),
                "options": [
                    {
                        "text": (
                            "Servise yatırarak İV seftriakson ve sıvı tedavisi başlamak, üriner sistem "
                            "ultrasonografisi planlamak ve toplam antibiyoterapi süresini 10-14 güne tamamlamak"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Kusması/oral intoleransı olan 6 aylık akut piyelonefrit hastası yatırılarak "
                            "parenteral 3. kuşak sefalosporin (örn. Seftriakson 50-75 mg/kg/gün) ile tedavi "
                            "edilir; <2 yaş ilk ateşli İYE de anatomik anomalileri değerlendirmek için Üriner "
                            "USG yapılır ve tedavi 10-14 güne tamamlanır."
                        ),
                        "new_finding": (
                            "Hasta Çocuk Servisine yatırılarak İV Seftriakson ve hidrasyon başlandı. 48. saatte "
                            "ateşi düştü, kusması durdu; kateter kültüründe >100.000 CFU/mL duyarlı E. coli "
                            "üredi. Yapılan Üriner USG normal saptandı ve 10 günlük tedaviye tamamlanmak üzere "
                            "oral sefiksim ile taburcu edildi."
                        ),
                    },
                    {
                        "text": (
                            "Oral nitrofurantoin süspansiyon reçete ederek kusması için ondansetron vermek ve "
                            "poliklinikte kontrol edilmek üzere hastayı acil servisten eve taburcu etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Nitrofurantoin renal parankimde ve kanda terapötik konsantrasyona ulaşamadığı ve "
                            "bebek oral ilacı kustuğu için 24 saat sonra ürosepsis tablosu gelişti."
                        ),
                        "teaching_point": (
                            "Nitrofurantoin ve fosfomisin yalnızca ateşsiz alt İYE (sistit) tedavisinde "
                            "kullanılır; böbrek dokusu düzeyleri yetersiz olduğundan akut piyelonefrit "
                            "tedavisinde kesinlikle kontrendikedir."
                        ),
                    },
                    {
                        "text": (
                            "İntravenöz seftriakson başlamak ve vezikoüreteral reflüyü saptamak amacıyla henüz "
                            "ateşli enfeksiyon devam ederken hemen bugün işeme sistoüretrografisi (VSUG) çekmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Aktif piyelonefrit sırasında yapılan retrograd kontrastlı mesane kateterizasyonu "
                            "bakteriyemiyi tetikledi ve enflamasyona bağlı geçici vezikoüreteral reflü "
                            "nedeniyle yanıltıcı sonuç elde edildi."
                        ),
                        "teaching_point": (
                            "İlk ateşli İYE geçiren <2 yaş çocukta ilk basamak görüntüleme Üriner USG dir; VSUG "
                            "rutin yapılmaz (yalnız USG de hidronefroz/skar bulgusu veya atipik/tekrarlayan İYE "
                            "varsa enfeksiyon düzeldikten sonra çekilir)."
                        ),
                    },
                    {
                        "text": (
                            "Acil serviste tek doz intramüsküler seftriakson uyguladıktan sonra toplam 3 günlük "
                            "kısa süreli oral trimetoprim-sülfametoksazol reçete ederek hastayı taburcu etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Kusması devam eden 6 aylık bebekte 3 günlük kısa süreli ve E. coli direnci yüksek "
                            "olan TMP-SMX tedavisi yetersiz kaldı; enfeksiyon nüks ederek renal skar riski arttı."
                        ),
                        "teaching_point": (
                            "Akut piyelonefritte 3 günlük kısa süreli tedavi yetersizdir (7-14 gün gerekir); "
                            "ayrıca kusması olan süt çocuğunda başlangıç tedavisi parenteral yoldan yapılmalıdır."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "id": "Y10",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "2 Yaş",
        "gender": "Erkek",
        "complaint": "Sakin dururken bile duyulan tiz nefes alma sesi (stridor), kaba öksürük ve boyun çukurunda çekilme",
        "history": (
            "Gece 03:30'da ailesi kucağında Sarı Alana getiriyor: 'Dün akşamdan beri sesi kısıktı ve hafif "
            "nezlesi vardı, gece yarısı havlar gibi kaba bir öksürük başladı. Son 1 saattir hiç ağlamazken, "
            "kucağımızda sakin otururken bile nefes alırken boğazından tiz bir ses çıkıyor ve boynunun çukuru "
            "içeri çöküyor.'"
        ),
        "final_diagnosis": "Orta-Ağır Akut Viral Laringotrakeit (Orta-Ağır Krup)",
        "disposition": (
            "Sarı Alanda Nebülize L-Adrenalin + Tek Doz 0.6 mg/kg Deksametazon -> En Az 3-4 Saat Rebound "
            "Stridor Gözlemi Sonrası Taburculuk"
        ),
        "case_pearl": (
            "İstirahatte (çocuk sakinken) duyulan inspiratuar stridor ve suprasternal/interkostal çekilmeler "
            "Orta-Ağır Krup (Westley skoru ≥3) göstergesidir. Tedavide tek doz Deksametazon (0.6 mg/kg oral/İM) "
            "ile birlikte Nebülize L-Adrenalin (0.5 mL/kg, maks 5 mL, 1:1000) uygulanır. Nebülize adrenalinin "
            "etkisi ~2 saatte sona erip rebound stridor gelişebileceğinden hasta en az 3-4 saat Sarı Alanda "
            "gözlemlenmeden taburcu edilmez."
        ),
        "steps": [
            {
                "stage_title": "Sarı Alanda Sakin Değerlendirme ve Hava Yolu Muayenesi",
                "question": (
                    "Gece yarısı başlayan kaba öksürük, istirahatte inspiratuar stridor ve suprasternal çekilme "
                    "ile getirilen 2 yaşındaki bu çocukta ilk yaklaşımınız ne olmalıdır?"
                ),
                "options": [
                    {
                        "text": (
                            "Hava yolu açıklığını net görmek için çocuğu annesinden ayırıp muayene masasına "
                            "yatırarak abeslang ile zorlu orofarenks muayenesi yapmak ve damar yolu açmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Annesinden ayrılan ve abeslang ile zorlanan çocuğun şiddetli ağlaması dinamik üst "
                            "hava yolu darlığını artırdı; türbülan hava akımı sonucu stridor şiddetlendi ve "
                            "SpO2 %85 düzeyine düştü."
                        ),
                        "teaching_point": (
                            "Akut üst hava yolu obstrüksiyonu ve stridoru olan çocuklarda ağlama ve ajitasyon "
                            "negatif intratorasik basıncı artırarak dinamik darlığı ağırlaştırır; zorlu "
                            "orofarenks muayenesi ve gereksiz ağrılı işlemlerden kaçınılmalıdır."
                        ),
                    },
                    {
                        "text": (
                            "Çocuğu anne kucağında hiç ağlatmadan genel görünümünü, bilinç durumunu, "
                            "istirahatteki stridorunu, suprasternal-interkostal çekilmelerini, akciğer hava girişini ve oksijen satürasyonunu değerlendirmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Akut üst hava yolu darlığı olan çocukta ajitasyonu önlemek temel ilkedir; çocuk "
                            "ebeveyn kucağında sakin tutulurken bilinç, istirahatte stridor, çekilmeler, hava "
                            "girişi ve SpO2 değerlendirilerek klinik ağırlık belirlenir."
                        ),
                        "new_finding": (
                            "Vital Bulgular: Ateş 38.0°C, KTA 144/dk, SS 38/dk, Oda havasında SpO2 %93. Çocuk "
                            "anne kucağında sakin otururken dahi belirgin inspiratuar stridor duyuluyor, "
                            "suprasternal ve interkostal çekilmeleri mevcut, akciğer bazallerinde hava girişi "
                            "hafif azalmış. Bilinci açık, siyanoz yok, toksik görünüm veya ağızdan salya akışı "
                            "(drooling) yok."
                        ),
                    },
                    {
                        "text": (
                            "Sakinleştirmek ve solunum çabasını azaltmak amacıyla hemen 0.1 mg/kg intravenöz "
                            "midazolam uygulayıp çocuğu sırtüstü düz pozisyonda monitörize izleme almak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Verilen sedatif ilaç üst hava yolu kas tonusunu ve solunum dürtüsünü baskıladı; "
                            "düz yatırılan çocukta tam hava yolu obstrüksiyonu ve derin hipoksemi gelişti."
                        ),
                        "teaching_point": (
                            "Üst hava yolu obstrüksiyonu olan çocuklarda sedatif ilaçlar solunum çabasını ve "
                            "hava yolu tonusunu baskılayarak solunum arrestine yol açabileceği için kesinlikle "
                            "kontrendikedir."
                        ),
                    },
                    {
                        "text": (
                            "Subglottik darlık derecesini objektif olarak görüntülemek için tedavi başlamadan "
                            "önce çocuğu radyoloji ünitesine göndererek ön-arka ve yan boyun grafisi çektirmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Tedavi verilmeden radyolojiye gönderilen ve çekim sırasında pozisyon verilmeye "
                            "çalışılan çocukta ağlama ile birlikte stridor ve retraksiyonlar ağırlaşarak "
                            "hipoksemi derinleşti."
                        ),
                        "teaching_point": (
                            "Tipik klinik bulgularla başvuran akut üst hava yolu obstrüksiyonunda boyun grafisi "
                            "rutin olarak endike değildir ve acil medikal tedaviyi geciktirmemelidir."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Sarı Alanda Akut Medikal Müdahale Seçimi",
                "question": (
                    "İstirahatte belirgin inspiratuar stridoru, suprasternal çekilmeleri ve oda havasında %93 "
                    "satürasyonu olan bu çocukta hemen uygulanması gereken tedavi protokolü hangisidir?"
                ),
                "options": [
                    {
                        "text": (
                            "Yalnızca soğuk buhar (mist) uygulaması yapmak ve subglottik mukozal ödemi çözmek "
                            "için 20 dakika arayla üç doz nebülize salbutamol başlamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Soğuk buhar çocuğun yüzünü rahatsız ederek ağlamasını artırdı; verilen nebülize "
                            "salbutamol üst hava yolu ödemini çözmediği gibi taşikardiyi artırdı ve stridor devam etti."
                        ),
                        "teaching_point": (
                            "Soğuk buhar uygulamasının klinik etkinliği kanıtlanmamıştır; beta-2 agonist olan "
                            "salbutamol ise alt hava yolu bronkospazmında etkilidir, subglottik üst hava yolu "
                            "ödeminde kullanılmaz."
                        ),
                    },
                    {
                        "text": (
                            "Tek başına 0.15 mg/kg oral deksametazon verip taşikardi yan etkisinden kaçınmak "
                            "amacıyla nebülize adrenalin uygulamadan stridorun geçmesini 30 dakika beklemek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Kortikosteroidlerin antiinflamatuar etkisi en erken 2-4 saat içinde başladığından, "
                            "nebülize adrenalin verilmeyen hastanın istirahatteki stridoru, çekilmeleri ve "
                            "hipoksemisi ilk saat boyunca devam etti."
                        ),
                        "teaching_point": (
                            "İstirahatte stridor ve belirgin çekilmesi olan orta-ağır vakalarda yalnız "
                            "deksametazon yeterli hızlı rahatlama sağlamaz; dakikalar içinde etki eden nebülize "
                            "L-adrenalin mutlaka eklenmelidir."
                        ),
                    },
                    {
                        "text": (
                            "Nebülize L-adrenalin (0.5 mL/kg, maksimum 5 mL, 1:1000) ile birlikte tek doz "
                            "0.6 mg/kg deksametazon uygulamak ve oksijen sağlamak"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Alfa-adrenerjik vazokonstriksiyon yapan nebülize L-adrenalin subglottik mukozal "
                            "ödemi 10-30 dakikada hızla çözer; eş zamanlı verilen 0.6 mg/kg deksametazon ise "
                            "2-4 saatte devreye girerek kalıcı antiinflamatuar etki sağlar."
                        ),
                        "new_finding": (
                            "5 mL (1:1000) Nebülize L-Adrenalin, 0.6 mg/kg Deksametazon ve oksijen desteği "
                            "uygulandıktan 20 dakika sonra istirahatteki stridor tamamen kayboldu, suprasternal "
                            "çekilmeler geriledi ve oda havasında SpO2 %98 düzeyine yükseldi."
                        ),
                    },
                    {
                        "text": (
                            "Üst hava yolu enfeksiyonunu kontrol altına almak için intravenöz "
                            "ampisilin-sulbaktam ve metilprednizolon yükleyip eş zamanlı intramüsküler feniramin maleat uygulamak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "İntramüsküler enjeksiyon ve damar yolu işlemi çocuğu şiddetle ağlattı; viral "
                            "kaynaklı non-histaminerjik subglottik ödemde antibiyotik ve antihistaminik hiçbir "
                            "akut yarar sağlamadı."
                        ),
                        "teaching_point": (
                            "Viral subglottik ödemde antibiyotiklerin ve H1 antihistaminiklerin yeri yoktur; "
                            "akut hava yolu rahatlaması için nebülize adrenalin ve sistemik deksametazon standart tedavidir."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Klinik Tanı",
                "question": (
                    "Havlar tarzda kaba öksürük, ses kısıklığı, istirahatte inspiratuar stridor ve nebülize "
                    "adrenalin + deksametazon tedavisine hızlı yanıt doğrultusunda kesin tanınız nedir?"
                ),
                "options": [
                    {
                        "text": "Orta-Ağır Akut Viral Laringotrakeit (Orta-Ağır Krup)",
                        "is_correct": True,
                        "explanation": (
                            "Viral prodrom sonrası gece başlayan havlar tarzda öksürük, ses kısıklığı, "
                            "istirahatte inspiratuar stridor, çekilmeler (Westley skoru 5) ve nebülize "
                            "adrenaline hızlı yanıt Orta-Ağır Viral Krup tanısını doğrular."
                        ),
                        "new_finding": "Kesin Tanı: Orta-Ağır Akut Viral Laringotrakeit (Orta-Ağır Krup - Westley Skoru 5).",
                    },
                    {
                        "text": "Sekonder Akut Eksüdatif Bakteriyel Trakeit",
                        "is_correct": False,
                        "scenario_update": (
                            "Bakteriyel trakeitte çok yüksek ateş, toksik görünüm, koyu pürülan trakeal "
                            "sekresyonlar ve nebülize adrenaline yanıtsızlık görülür; bu hasta ise adrenaline "
                            "20 dakikada tam yanıt verdi."
                        ),
                        "teaching_point": (
                            "Nebülize adrenalin ve deksametazona dramatik yanıt veren, toksik görünümü olmayan "
                            "tablo viral laringotrakeittir."
                        ),
                    },
                    {
                        "text": "Akut Bakteriyel Supraglottit (Akut Epiglottit)",
                        "is_correct": False,
                        "scenario_update": (
                            "Akut epiglottitte havlar tarzda öksürük beklenmez; ani başlayan yüksek ateş, "
                            "toksik görünüm, yutma güçlüğü, ağızdan salya akışı (drooling) ve tripod pozisyonu görülür."
                        ),
                        "teaching_point": (
                            "Havlar tarzda öksürük ve ses kısıklığı subglottik bölge (krup) tutulumunu "
                            "gösterir; supraglottitte ise boğuk (hot potato) ses ve salya akışı ön plandadır."
                        ),
                    },
                    {
                        "text": "Konjenital Laringomalazi ve Gastroözofageal Reflü",
                        "is_correct": False,
                        "scenario_update": (
                            "Laringomalazi yaşamın ilk haftalarında başlayan, sırtüstü yatınca ve beslenirken "
                            "artan kronik stridor nedenidir; 2 yaşında akut başlayan ateşli tablo viral kruptur."
                        ),
                        "teaching_point": (
                            "İki yaşında akut viral prodromla başlayan havlar öksürük ve stridor konjenital "
                            "laringomalazi değil akut viral laringotrakeittir."
                        ),
                    },
                ],
            },
            {
                "stage_title": "Sarı Alan Gözlem Süresi (Rebound Stridor İzlemi) ve Taburculuk",
                "question": (
                    "Nebülize L-adrenalin uygulamasından 30 dakika sonra stridoru ve çekilmeleri tamamen "
                    "düzelen çocuk için ailesi eve gitmek istiyor. Doğru yaklaşımınız nedir?"
                ),
                "options": [
                    {
                        "text": (
                            "Çocuğun istirahatte stridoru kalmadığı ve oksijen satürasyonu %98 olduğu için evde "
                            "kullanmak üzere salbutamol şurup reçete ederek hemen taburcu etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Tedaviden 30 dakika sonra taburcu edilen çocukta 90. dakikada nebülize adrenalinin "
                            "vazokonstriktör etkisi sona erdi; evde ağır rebound stridor ve çekilmeler "
                            "tekrarlayarak acil servise geri getirildi."
                        ),
                        "teaching_point": (
                            "Nebülize L-adrenalinin etkisi yaklaşık 2 saat içinde biter ve subglottik ödem "
                            "tekrarlayabilir (rebound fenomeni); bu nedenle hiçbir hasta ilk 1 saat içinde "
                            "taburcu edilmemelidir."
                        ),
                    },
                    {
                        "text": (
                            "Hastayı sadece 1 saat gözlemde tutup stridor tekrarlamazsa evde buhar makinesiyle "
                            "uygulamaları için aileye adrenalin ampul reçete ederek taburcu etmek"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Bir saatlik gözlem rebound stridoru dışlamak için yetersiz kaldı; ayrıca evde "
                            "kontrolsüz dozda uygulanan nebülize adrenalin çocukta ciddi taşikardi ve "
                            "ajitasyona yol açtı."
                        ),
                        "teaching_point": (
                            "Nebülize adrenalin sonrası gözlem süresi en az 3-4 saat olmalıdır ve nebülize "
                            "adrenalin yalnızca hastane ortamında monitörize edilerek uygulanır, eve reçete edilmez."
                        ),
                    },
                    {
                        "text": (
                            "Tek doz nebülize adrenalin alan her krup hastasında entübasyon riski yüksek "
                            "olduğundan klinik yanıt tam olsa bile çocuk yoğun bakıma yatırmak"
                        ),
                        "is_correct": False,
                        "scenario_update": (
                            "Tek doz nebülize adrenalin ve deksametazon sonrası tamamen düzelen ve 4 saat "
                            "boyunca istirahatte stridoru tekrarlamayan hastada gereksiz yoğun bakım yatışı yapıldı."
                        ),
                        "teaching_point": (
                            "Tek doz nebülize adrenalin ve deksametazon sonrası 3-4 saatlik gözlemde "
                            "istirahatte stridoru ve çekilmesi tekrarlamayan hastalar yatış gerekmeden güvenle "
                            "taburcu edilebilir; yatış tekrarlayan adrenalin gereksiniminde endikedir."
                        ),
                    },
                    {
                        "text": (
                            "Rebound stridor riski nedeniyle en az 3-4 saat izlemek; 4. saatte istirahatte "
                            "stridor ve çekilme yoksa kırmızı bayraklarla taburcu etmek"
                        ),
                        "is_correct": True,
                        "explanation": (
                            "Nebülize adrenalinin etkisi ~2 saatte geçerken deksametazonun etkisi 2-4 saatte "
                            "başlar; hasta en az 3-4 saat izlenmeli, bu sürede istirahatte stridor tekrarlamaz, "
                            "SpO2 normal ve oral alımı iyi ise taburcu edilmelidir."
                        ),
                        "new_finding": (
                            "Hasta Sarı Alanda 4 saat boyunca izlendi; rebound stridor veya çekilme gelişmedi, "
                            "oda havasında SpO2 %99 ve sıvı alımı iyi olduğu görülerek aileye kırmızı bayrak "
                            "eğitimi verilip taburcu edildi."
                        ),
                    },
                ],
            },
        ],
    },
]
