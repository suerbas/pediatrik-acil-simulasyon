# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - Y71-Y75 (Üst Solunum Yolu, KBB ve Hışıltı)
"""

SPOILERS = {
    "Y71": ["faringokonjonktival", "adenovir"],
    "Y72": ["herpanjina", "coxsackie", "koksaki"],
    "Y73": ["sinüzit", "rinosinüzit"],
    "Y74": ["otitis eksterna", "yüzücü kulağı", "eksterna"],
    "Y75": ["hafif-orta astım atağı", "hafif atak"],
}

CASES = [
    {
        "id": "Y71",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "4 Yaşında",
        "gender": "Erkek",
        "complaint": "Üç gündür 39°C'ye çıkan ateş, boğaz ağrısı ve iki gözde kızarıklık",
        "history": "Annesi anlatıyor: 'Üç gündür ateşi 39°C'ye çıkıyor, ateş düşürücüyle iniyor. Boğazı ağrıyor, yemek yemek istemiyor. Dün iki gözü de kızardı, sulanıyor ama çapak yok. Burnu akıyor.' Kreşe gidiyor, sınıfta birkaç çocukta 'göz nezlesi' varmış. Hafta sonu kapalı yüzme havuzuna gitmişler. Döküntü, ishal yok. Aşıları tam. Tartı: 17 kg.",
        "final_diagnosis": "Faringokonjonktival Ateş (Adenovirüs Enfeksiyonu)",
        "disposition": "Destek Tedavisi ve Hijyen Önerileriyle Yeşil Alandan Taburculuk",
        "case_pearl": "Ateş, farenjit ve bilateral eksüdasız konjonktivitin birlikteliği adenovirüse bağlı faringokonjonktival ateşi düşündürür; havuz ve kreş salgınları tipiktir. Belirgin viral bulgular (konjonktivit, burun akıntısı, öksürük) varken AGBHS testi önerilmez. Ateş 5-7 gün sürebilir ve CRP yüksek olabilir. Ateş 5 günü aşarsa Kawasaki hastalığı yeniden değerlendirilmelidir. Tedavi destekleyicidir; antibiyotiğin yeri yoktur.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Ateş, boğaz ağrısı ve göz kızarıklığı olan bu çocukta muayenede nelere dikkat edersiniz?",
                "options": [
                    {
                        "text": "Göz kızarıklığını bakteriyel kabul edip muayeneyi gözle sınırlı tutmak, antibiyotikli göz damlası yazarak boğaz ağrısı için yalnız gargara önermek",
                        "is_correct": False,
                        "scenario_update": "Göz damlası başlandı; ateş ve boğaz ağrısı sürdü, sistemik değerlendirme yapılmadı.",
                        "teaching_point": "Ateşli çocukta göz bulgusu sistemik tablonun parçası olabilir; tam muayene yapılmalıdır."
                    },
                    {
                        "text": "Hidrasyonu ve genel durumu değerlendirip farenks, tonsiller, konjonktiva, kornea, kulaklar, lenf nodları, deri ve el-ayak bulgularını sistematik muayene etmek",
                        "is_correct": True,
                        "explanation": "Konjonktivitin eksüdalı olup olmaması, limbusun korunması, lenf nodu dağılımı, döküntü ve el-ayak bulguları viral, bakteriyel ve vaskülitik tabloları ayırır.",
                        "new_finding": "Vital Bulgular: Ateş 39.1°C, KTA 128/dk, SS 24/dk, SpO2 %99, KDZ 2 sn. Hidrasyonu iyi. Farenks hiperemik, tonsiller 2+ ve ince beyaz eksüdalı. Bilateral foliküler, eksüdasız konjonktivit, kornea saydam, fotofobi yok. Bilateral preaüriküler ve anterior servikal küçük hassas lenf nodları. Berrak burun akıntısı. Dudaklar normal, döküntü ve el-ayak değişikliği yok. Kulak zarları normal."
                    },
                    {
                        "text": "Ateş ve konjonktival kızarıklık birlikteliği nedeniyle muayeneyi tamamlamadan çocuğu Sarı Alana alıp ekokardiyografi ve inflamatuvar belirteç istemek",
                        "is_correct": False,
                        "scenario_update": "Çocuk Sarı Alanda saatlerce bekletildi; ekokardiyografi normal geldi ve tablo henüz üçüncü gündeydi.",
                        "teaching_point": "Üçüncü gündeki ateş ve eksüdasız konjonktivit tek başına ileri tetkik gerektirmez; muayene bulguları birlikte değerlendirilmelidir."
                    },
                    {
                        "text": "Tonsil eksüdası nedeniyle muayeneyi kısa tutup hemen amoksisilin başlamak ve göz bulgusunun antibiyotikle birlikte geçeceğini aileye açıklamak",
                        "is_correct": False,
                        "scenario_update": "Amoksisilin başlandı; ateş yedinci güne dek sürdü ve aile antibiyotiğin işe yaramadığını düşünerek tekrar başvurdu.",
                        "teaching_point": "Tonsil eksüdası viral enfeksiyonlarda da görülür; antibiyotik kararı klinik ve test birlikte değerlendirilerek verilmelidir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Bu çocukta hangi tetkik yaklaşımı en uygundur?",
                "options": [
                    {
                        "text": "Tonsil eksüdası bulunduğu için boğazdan hızlı strep antijen testi ve kültür almak, test sonucu negatif çıkarsa yine de kültürü bekleyip antibiyotiği sürdürmek",
                        "is_correct": False,
                        "scenario_update": "Hızlı test negatif geldi, kültür 48 saat sürdü; bu sürede çocuk gereksiz antibiyotik aldı.",
                        "teaching_point": "Konjonktivit, burun akıntısı gibi belirgin viral bulgular varken AGBHS testi önerilmez; taşıyıcılık nedeniyle yanıltıcı olabilir."
                    },
                    {
                        "text": "Belirgin viral bulgular nedeniyle strep testi yapmamak; antibiyotik isteyen aileye kanıt sunmak için göz sürüntüsünden hızlı viral antijen testi bakmak",
                        "is_correct": True,
                        "explanation": "Viral bulgular güçlü olduğunda bakteriyel test yapılmaz. Hızlı viral antijen testi tanıyı destekler ve gereksiz antibiyotik kullanımını azaltır.",
                        "new_finding": "Konjonktival sürüntüde hızlı viral antijen testi pozitif."
                    },
                    {
                        "text": "Ateşin üç gündür sürmesi nedeniyle hemogram, CRP, sedimantasyon ve kan kültürü istemek, CRP yüksekse oral antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "Lökosit 16.800/mm³, CRP 58 mg/L geldi; antibiyotik başlandı, ancak ateşin seyri değişmedi.",
                        "teaching_point": "Bazı viral enfeksiyonlarda CRP ve lökosit belirgin yüksek olabilir; bu değerler tek başına antibiyotik kararı için yeterli değildir."
                    },
                    {
                        "text": "Göz tutulumunu değerlendirmek için acil göz hastalıkları konsültasyonu istemek ve konjonktival kültür sonucuna göre damla tedavisini planlamak",
                        "is_correct": False,
                        "scenario_update": "Konsültasyon için saatlerce beklendi; kültür birkaç gün sonra normal flora olarak raporlandı.",
                        "teaching_point": "Kornea tutulumu, görme kaybı veya fotofobi olmadıkça eksüdasız konjonktivitte göz konsültasyonu ve kültür gerekmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Streptokoksik tonsillofarenjit", "is_correct": False, "scenario_update": "Konjonktivit ve burun akıntısı gibi belirgin viral bulgular vardı.", "teaching_point": "Streptokoksik farenjitte konjonktivit, burun akıntısı ve öksürük beklenmez."},
                    {"text": "Faringokonjonktival ateş", "is_correct": True, "explanation": "Ateş, eksüdatif farenjit, bilateral foliküler konjonktivit, preaüriküler lenfadenopati, havuz ve kreş teması ile pozitif viral antijen testi adenovirüse bağlı faringokonjonktival ateşi gösterir.", "new_finding": "Tanı: Faringokonjonktival ateş (adenovirüs)."},
                    {"text": "Kawasaki hastalığı (erken dönem)", "is_correct": False, "scenario_update": "Ateş henüz üçüncü gündeydi, dudak, döküntü ve el-ayak bulguları yoktu, konjonktivit foliküler ve preaüriküler lenfadenopatiliydi.", "teaching_point": "Kawasaki konjonktiviti limbusu koruyan, eksüdasız, foliküler olmayan tiptedir; ateş 5 günü geçerse yeniden değerlendirilmelidir."},
                    {"text": "Kızamık prodrom dönemi", "is_correct": False, "scenario_update": "Aşıları tamdı, Koplik lekesi yoktu ve öksürük belirgin değildi.", "teaching_point": "Kızamık prodromunda ateş, öksürük, burun akıntısı, konjonktivit ve Koplik lekeleri görülür."}
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun tedavi ve taburculuk planı hangisidir?",
                "options": [
                    {
                        "text": "Viral olsa da sekonder bakteriyel enfeksiyonu önlemek için 10 gün amoksisilin başlamak ve göz için antibiyotikli damla eklemek",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik sonrası ishal gelişti; hastalığın süresi değişmedi.",
                        "teaching_point": "Profilaktik antibiyotik viral enfeksiyonda sekonder enfeksiyonu önlemez ve yan etki riski taşır."
                    },
                    {
                        "text": "Göz kızarıklığını hızla geçirmek için kortikosteroid içeren göz damlası başlamak ve ateş için aspirin önermek, bir hafta sonra kontrol planlamak",
                        "is_correct": False,
                        "scenario_update": "Steroidli damla viral replikasyonu uzattı; aspirin çocukta Reye sendromu riski nedeniyle kesildi.",
                        "teaching_point": "Viral konjonktivitte rutin steroidli damla ve çocukta ateş için aspirin kullanılmaz."
                    },
                    {
                        "text": "Parasetamol 15 mg/kg veya ibuprofen 10 mg/kg, bol sıvı ve el hijyeni önermek; ateş 5 günü aşarsa ya da gözde ağrı gelişirse dönmelerini söylemek",
                        "is_correct": True,
                        "explanation": "Tedavi destekleyicidir. Göz salgıları çok bulaşıcı olduğundan havlu ayrılmalı ve el yıkama vurgulanmalıdır. Ateşin uzaması ayırıcı tanının yeniden değerlendirilmesini gerektirir.",
                        "new_finding": "Aile bilgilendirildi. Ateş beşinci gün kendiliğinden düştü, göz bulguları ikinci haftada geriledi. Kreşe ateşsiz 24 saat sonra dönmesi önerildi."
                    },
                    {
                        "text": "Çocuğun boğaz ağrısı için viskoz lidokain gargarası ve antihistaminik şurup vermek, kreşe ateş düştüğü gün hemen dönebileceğini söylemek",
                        "is_correct": False,
                        "scenario_update": "Çocuk lidokaini yuttu ve uyuşukluk yakınması oldu; kreşte iki çocukta daha konjonktivit gelişti.",
                        "teaching_point": "Küçük çocukta viskoz lidokain sistemik toksisite riski taşır; bulaşıcılık süresinde hijyen önlemleri önemlidir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y72",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "2 Yaşında (12 kg)",
        "gender": "Kız",
        "complaint": "İki gündür ateş, yemek yemeyi reddetme ve salya akması",
        "history": "Annesi anlatıyor: 'Dünden beri ateşi 39°C'ye çıkıyor. Ağzını açınca ağlıyor, hiçbir şey yemiyor, su da az içiyor. Salyası çok akıyor.' Kreşe gidiyor, yaz aylarında. Kusma, ishal, öksürük yok. Son 12 saatte iki bez ıslatmış. Döküntü fark edilmemiş. Daha önce benzer şikâyeti olmamış. Aşıları tam.",
        "final_diagnosis": "Herpanjina (Enterovirus/Coxsackie A)",
        "disposition": "Ağızdan Sıvı Alımı Gözlendikten Sonra Analjezi ve Sıvı Önerileriyle Yeşil Alandan Taburculuk",
        "case_pearl": "Herpanjinada ateşle birlikte yumuşak damak, uvula ve ön plikalarda 1-2 mm veziküller ve sığ ülserler görülür; dişeti ve dudaklar korunur. Herpetik gingivostomatitte ise ön ağız, dişeti ve dudak tutulur. El-ayak-ağız hastalığında el ve ayakta lezyonlar eşlik eder. Asıl risk ağrıya bağlı sıvı alamamaktır. Tedavi analjezi ve sıvıdır. Viskoz lidokain küçük çocuklarda önerilmez.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Ateşli ve yemek yemeyen bu çocukta ilk değerlendirmede öncelikli olarak ne yaparsınız?",
                "options": [
                    {
                        "text": "Hidrasyon durumunu ve son idrar zamanını değerlendirip ağız içini, dişetini, dudakları, farenksi, el ve ayakları ve deriyi ayrıntılı olarak muayene etmek",
                        "is_correct": True,
                        "explanation": "Ağız içi lezyonların yeri (ön ağız, dişeti, yumuşak damak) ve el-ayak tutulumu ayırıcı tanıyı belirler. Ağrılı ağız lezyonlarında asıl risk dehidratasyondur.",
                        "new_finding": "Vital Bulgular: Ateş 38.9°C, KTA 136/dk, SS 26/dk, SpO2 %99, KDZ 2 sn. Mukozalar hafif kuru, göz yaşı var, fontanel kapalı. Yumuşak damak, uvula ve ön tonsil plikalarında 6-8 adet gri-beyaz, kırmızı haleli 1-2 mm vezikül ve sığ ülser. Dişeti, dil ucu ve dudaklar normal. El, ayak ve kalçada lezyon yok. Boyunda küçük, hassas olmayan lenf nodları."
                    },
                    {
                        "text": "Salya akması ve ağız açmayı reddetme nedeniyle havayolu tıkanıklığı düşünüp ağız muayenesinden kaçınarak çocuğu hemen KBB değerlendirmesine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "KBB konsültasyonu saatler sürdü; çocukta stridor ya da solunum sıkıntısı yoktu ve ağız içi muayene yapılmamıştı.",
                        "teaching_point": "Solunum sıkıntısı, stridor ve tripod pozisyonu yoksa ağız içi muayene güvenle yapılabilir."
                    },
                    {
                        "text": "Ateş ve beslenme reddi nedeniyle muayeneyi kısa tutup tam kan sayımı, CRP ve idrar tetkiki istemek ve sonuçlara göre tedavi planlamak",
                        "is_correct": False,
                        "scenario_update": "Tetkikler normal geldi; ağız içindeki lezyonlar saatler sonra fark edildi.",
                        "teaching_point": "Ateşli çocukta tetkik öncesi ağız içi dahil tam muayene, çoğu zaman tanıyı tek başına koydurur."
                    },
                    {
                        "text": "Diş çıkarmaya bağlı ateş ve huzursuzluk olarak değerlendirip diş jeli ve ateş düşürücü önermek, ağız içi muayene için ertesi gün kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Evde sıvı alımı daha da azaldı; çocuk ertesi gün belirgin dehidratasyonla getirildi.",
                        "teaching_point": "Diş çıkarma 38.5°C üzeri ateş ve beslenme reddi yapmaz; ağız içi muayene ertelenmemelidir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik ve Destek Kararı",
                "question": "Bu çocukta hangi yaklaşım uygundur?",
                "options": [
                    {
                        "text": "Ülserlerin bakteriyel olabileceğini düşünerek boğaz kültürü almak ve kültür sonucuna göre antibiyotik başlamayı planlamak",
                        "is_correct": False,
                        "scenario_update": "Kültürde normal flora üredi; bu sürede analjezi ve sıvı alımı gözden kaçtı.",
                        "teaching_point": "Tipik viral ağız lezyonlarında kültür gerekmez; öncelik ağrı kontrolü ve hidrasyondur."
                    },
                    {
                        "text": "Lezyonlardan virüs PCR ve serolojik testler göndermek, sonuç gelene dek çocuğu Sarı Alanda damar yolu ile izlemek",
                        "is_correct": False,
                        "scenario_update": "Damar yolu açılırken çocuk çok ağladı; PCR sonucu yönetimi değiştirmeden günler sonra geldi.",
                        "teaching_point": "Klinik tanının açık olduğu hafif olguda viral PCR ve damar yolu gerekmez."
                    },
                    {
                        "text": "Laboratuvar tetkiki yapmadan analjezik vermek, 30-45 dakika sonra soğuk sıvı içirmeyi deneyerek ağızdan alımı acil serviste gözlemlemek",
                        "is_correct": True,
                        "explanation": "Tanı kliniktir. Analjezi sonrası ağızdan sıvı içebilmesi taburculuk için en önemli ölçüttür; içemezse IV veya nazogastrik sıvı düşünülür.",
                        "new_finding": "İbuprofen 10 mg/kg verildi. 40 dakika sonra çocuk soğuk ayran ve su içmeye başladı, bir saatte yaklaşık 180 mL aldı, bir kez idrar yaptı."
                    },
                    {
                        "text": "Ağız içi ağrısı nedeniyle beklemeden nazogastrik sonda takarak sıvı vermek ve çocuğu bir gece gözleme alıp sabah değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Sonda takılması çocuğu çok rahatsız etti; analjezi sonrası ağızdan içebileceği hiç denenmemişti.",
                        "teaching_point": "Önce yeterli analjezi verilip ağızdan alım denenmelidir; sonda veya damar yolu yalnızca başarısızlıkta gerekir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Primer herpetik gingivostomatit", "is_correct": False, "scenario_update": "Dişeti, dil ucu ve dudaklar normaldi; lezyonlar posterior ağızdaydı.", "teaching_point": "Herpetik gingivostomatitte dişeti kanamalı ve ödemlidir, ön ağız ve dudaklar tutulur."},
                    {"text": "El-ayak-ağız hastalığı", "is_correct": False, "scenario_update": "El, ayak ve kalçada lezyon yoktu.", "teaching_point": "El-ayak-ağız hastalığında ağız lezyonlarına el, ayak ve kalçada veziküller eşlik eder."},
                    {"text": "Herpanjina (enteroviral)", "is_correct": True, "explanation": "Ateşle birlikte yumuşak damak, uvula ve ön plikalarda veziküller ve sığ ülserler, dişeti ve dudakların korunması herpanjinayı gösterir.", "new_finding": "Tanı: Herpanjina (enterovirüs)."},
                    {"text": "Rekürren aftöz stomatit", "is_correct": False, "scenario_update": "Lezyonlar ateşle birlikte yumuşak damakta küçük veziküllerle başlamıştı ve daha önce benzer atak yoktu.", "teaching_point": "Aftlar genellikle ateşsiz, tekrarlayan, daha büyük ve hareketli mukozada yerleşen ülserlerdir."}
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun taburculuk planı hangisidir?",
                "options": [
                    {
                        "text": "Ağız lezyonlarını hızla iyileştirmek için oral asiklovir 20 mg/kg günde dört kez 7 gün başlamak ve ateş düşürücüyle birlikte taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Asiklovir verildi ancak hastalığın seyrinde hiçbir değişiklik olmadı.",
                        "teaching_point": "Asiklovir enterovirüslere etkisizdir; herpetik gingivostomatitin erken döneminde düşünülür."
                    },
                    {
                        "text": "Ağrıyı azaltmak için her öğünden önce viskoz lidokainli gargara önermek ve olası sekonder enfeksiyon için amoksisilin eklemek",
                        "is_correct": False,
                        "scenario_update": "Çocuk lidokaini yuttu, ağız ve boğaz uyuşması nedeniyle öğürdü; amoksisilin ishale yol açtı.",
                        "teaching_point": "Küçük çocuklarda viskoz lidokain nöbet ve aspirasyon riski taşır; antibiyotik gereksizdir."
                    },
                    {
                        "text": "Lezyonlar iyileşene kadar katı gıda yasağı koyup yalnızca damar yolu ile sıvı alması için çocuğu servise yatırmak",
                        "is_correct": False,
                        "scenario_update": "Ağızdan içebilen çocuk gereksiz yere yatırıldı; hastane ortamı enterovirüs bulaşı açısından da risk oluşturdu.",
                        "teaching_point": "Analjeziyle ağızdan içebilen çocuk evde izlenebilir; yatış yalnızca dehidratasyon veya içememe durumunda gerekir."
                    },
                    {
                        "text": "Düzenli parasetamol veya ibuprofen, soğuk ve asitsiz sıvılarla yumuşak gıda önermek; günde 4'ten az bez ıslatırsa veya hiç içemezse dönmelerini söylemek",
                        "is_correct": True,
                        "explanation": "Hastalık 7-10 günde kendiliğinden geçer. Düzenli analjezi sıvı alımını sağlar. Azalmış idrar dehidratasyonun en pratik uyarı bulgusudur. El hijyeni bulaşı azaltır.",
                        "new_finding": "Çocuk taburcu edildi. Üçüncü gün ateş düştü, yedinci gün lezyonlar iyileşti; dehidratasyon gelişmedi."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y73",
        "category": "👂 Kulak Ağrısı & KBB",
        "age": "7 Yaşında",
        "gender": "Kız",
        "complaint": "On iki gündür geçmeyen burun akıntısı, burun tıkanıklığı ve gündüz de süren öksürük",
        "history": "Annesi anlatıyor: 'Nezle ile başladı, iki haftaya yakın oldu, hiç düzelmedi. Burnundan sarı-yeşil koyu akıntı geliyor, ağzı açık uyuyor, gündüz de öksürüyor. Ateşi ilk iki gün 38°C idi, sonra olmadı.' Baş ağrısı hafif, göz çevresinde şişlik, görme bozukluğu ve kusma yok. Son bir ayda antibiyotik kullanmamış. Astım veya alerji öyküsü yok. Tartı: 24 kg.",
        "final_diagnosis": "Akut Bakteriyel Rinosinüzit (Persistan Seyirli)",
        "disposition": "Yüksek Doz Amoksisilin ve 72 Saat Sonra Yeniden Değerlendirme Önerisiyle Yeşil Alandan Taburculuk",
        "case_pearl": "AAP 2013 kılavuzuna göre tanı kliniktir: (1) 10 günü aşan ve düzelmeyen burun akıntısı veya gündüz öksürüğü, (2) düzelme sonrası kötüleşme ya da (3) en az 3 gün süren ≥39°C ateş ve pürülan akıntı. Komplike olmayan olguda görüntüleme önerilmez. Persistan seyirde antibiyotik ya da 3 günlük ek gözlem seçenekleri sunulabilir. Göz çevresinde şişlik, görme değişikliği veya nörolojik bulgu orbital ya da intrakraniyal komplikasyonu düşündürür ve acil görüntüleme gerektirir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "On iki gündür burun akıntısı ve öksürüğü olan bu çocukta muayenede neye öncelik verirsiniz?",
                "options": [
                    {
                        "text": "Uzamış öksürük nedeniyle akciğer muayenesine odaklanıp oskültasyon normalse viral üst solunum yolu enfeksiyonu deyip yalnızca serum fizyolojik önermek",
                        "is_correct": False,
                        "scenario_update": "Çocuk üçüncü haftada hâlâ koyu akıntı ve öksürükle yeniden başvurdu.",
                        "teaching_point": "On günü aşan, düzelmeyen tabloda klinik seyir değerlendirilmeli; yalnızca akciğer muayenesi yeterli değildir."
                    },
                    {
                        "text": "Hastalığın seyrini sorgulayıp burun mukozası, postnazal akıntı, kulak zarları, göz çevresi ve göz hareketleri ile nörolojik bulguları değerlendirmek",
                        "is_correct": True,
                        "explanation": "Tanının temeli semptom süresi ve seyridir. Göz çevresi, göz hareketleri ve nörolojik muayene komplikasyonları dışlamak için mutlaka yapılmalıdır.",
                        "new_finding": "Vital Bulgular: Ateş 36.9°C, KTA 92/dk, SS 20/dk, SpO2 %99. Burun mukozası ödemli ve hiperemik, orta meada koyu sarı-yeşil akıntı. Arka farenks duvarında pürülan postnazal akıntı. Kulak zarları normal. Göz kapakları ödemsiz, göz hareketleri ağrısız ve tam, görme normal. Nörolojik muayene olağan. Akciğer sesleri temiz."
                    },
                    {
                        "text": "Pürülan akıntı nedeniyle burundan kültür alıp muayeneyi kültür sonucu gelene dek ertelemek, bu sürede yalnızca antihistaminik şurup başlamak",
                        "is_correct": False,
                        "scenario_update": "Burun kültüründe normal flora ve S. aureus üredi; sonuç yönetime katkı sağlamadı.",
                        "teaching_point": "Burun sürüntüsü kültürü sinüs içindeki etkeni yansıtmaz ve önerilmez."
                    },
                    {
                        "text": "Sarı-yeşil akıntıyı bakteriyel enfeksiyonun kesin kanıtı kabul edip ayrıntılı muayeneye gerek görmeden azitromisin reçete etmek",
                        "is_correct": False,
                        "scenario_update": "Azitromisin üç gün kullanıldı; akıntı sürdü ve çocuk tekrar başvurdu.",
                        "teaching_point": "Akıntının rengi tek başına bakteriyel enfeksiyonu göstermez; tanı semptom süresi ve seyriyle konur."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Komplikasyon bulgusu olmayan bu çocukta hangi tetkik yaklaşımı uygundur?",
                "options": [
                    {
                        "text": "Tanıyı kesinleştirmek için Waters pozisyonunda sinüs grafisi çekmek ve sinüslerde opasite varsa antibiyotik tedavisi başlamak",
                        "is_correct": False,
                        "scenario_update": "Grafide maksiller sinüslerde bilateral mukozal kalınlaşma görüldü; bu bulgu viral nezlede de bulunabildiği için yorum değişmedi.",
                        "teaching_point": "Sinüs grafisi viral ve bakteriyel tabloyu ayıramaz; komplike olmayan olguda önerilmez."
                    },
                    {
                        "text": "Görüntüleme veya laboratuvar tetkiki istemeden klinik ölçütlerle tanı koymak ve tedavi seçeneklerini aileyle birlikte değerlendirmek",
                        "is_correct": True,
                        "explanation": "Komplike olmayan olguda tanı kliniktir. Görüntüleme yalnızca orbital veya intrakraniyal komplikasyon şüphesinde, kontrastlı tomografi veya MR olarak yapılır.",
                        "new_finding": "Tetkik istenmedi. Semptomlar 10 günü aşmış ve düzelme göstermemiş; ateş yok, komplikasyon bulgusu yok."
                    },
                    {
                        "text": "Paranazal sinüs bilgisayarlı tomografisi çekip mukozal kalınlaşma derecesine göre antibiyotik ya da burun spreyi kararını vermek",
                        "is_correct": False,
                        "scenario_update": "Tomografide yaygın mukozal kalınlaşma saptandı; çocuk gereksiz radyasyon aldı ve tedavi kararı değişmedi.",
                        "teaching_point": "Tomografi komplikasyon şüphesi veya cerrahi planlaması dışında önerilmez."
                    },
                    {
                        "text": "Hemogram, CRP ve sedimantasyon istemek; CRP yüksekse antibiyotik başlamak, normalse viral kabul edip burun spreyi önermek",
                        "is_correct": False,
                        "scenario_update": "CRP 9 mg/L geldi ve antibiyotik verilmedi; çocuk bir hafta sonra aynı yakınmalarla döndü.",
                        "teaching_point": "Kan tetkikleri bu tanıda ayırt edici değildir; karar semptomların süresi ve seyrine göre verilir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu çocukta en olası tanınız nedir?",
                "options": [
                    {"text": "Uzamış viral üst solunum yolu enfeksiyonu", "is_correct": False, "scenario_update": "Semptomlar 10 günü aşmış ve hiç düzelme göstermemişti.", "teaching_point": "Viral nezle genellikle 5-7. günde zirve yapıp 10 gün içinde belirgin düzelir."},
                    {"text": "Akut bakteriyel rinosinüzit", "is_correct": True, "explanation": "On günü aşan ve düzelmeyen pürülan burun akıntısı ve gündüz öksürüğü persistan akut bakteriyel rinosinüziti gösterir.", "new_finding": "Tanı: Akut bakteriyel rinosinüzit (persistan seyir)."},
                    {"text": "Alerjik rinit alevlenmesi", "is_correct": False, "scenario_update": "Hapşırma, kaşıntı ve sulu akıntı yoktu; akıntı pürülandı ve öncesinde nezle vardı.", "teaching_point": "Alerjik rinitte sulu akıntı, hapşırma ve burun-göz kaşıntısı baskındır."},
                    {"text": "Burunda yabancı cisim", "is_correct": False, "scenario_update": "Akıntı bilateraldi ve kötü koku yoktu.", "teaching_point": "Yabancı cisimde tek taraflı, kötü kokulu, bazen kanlı akıntı tipiktir."}
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Amoksisilin 80-90 mg/kg/gün iki dozda başlamak ya da aileyle 3 gün ek gözlem kararı vermek; 72 saatte düzelme yoksa amoksisilin-klavulanata geçmek",
                        "is_correct": True,
                        "explanation": "Persistan seyirde antibiyotik veya kısa ek gözlem seçenekleri sunulur. Amoksisilin ilk seçenektir. 72 saatte yanıt alınamazsa tedavi genişletilir veya tanı yeniden değerlendirilir.",
                        "new_finding": "Amoksisilin 2 x 1000 mg başlandı. 72. saatte akıntı azaldı, öksürük geriledi. Tedavi 10 güne tamamlandı."
                    },
                    {
                        "text": "Üç gün azitromisin vermek ve tıkanıklık için 7 yaşında olduğundan oral dekonjestan-antihistaminik kombinasyonu eklemek",
                        "is_correct": False,
                        "scenario_update": "Azitromisine rağmen akıntı sürdü; dekonjestan sonrası çocukta uykusuzluk ve çarpıntı oldu.",
                        "teaching_point": "Makrolidlere pnömokok direnci yüksektir; dekonjestan ve antihistaminiklerin bu tabloda yararı yoktur."
                    },
                    {
                        "text": "Antibiyotik vermeden yalnızca 14 gün topikal dekonjestan sprey kullanımını önermek ve bir ay sonra KBB kontrolüne yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Uzun süreli dekonjestan sprey rebound tıkanıklık yaptı; akıntı sürdü.",
                        "teaching_point": "Topikal dekonjestanlar 3-5 günden uzun kullanılmamalıdır; uzun süreli kullanım rebound etki yapar."
                    },
                    {
                        "text": "Seftriakson 50 mg/kg intramüsküler üç gün uygulamak ve tedaviden sonra kontrol için paranazal sinüs tomografisi planlamak",
                        "is_correct": False,
                        "scenario_update": "Çocuk üç gün iğne için hastaneye getirildi; kontrol tomografisi gereksiz radyasyona neden oldu.",
                        "teaching_point": "Ağızdan tedavi alabilen çocukta parenteral antibiyotik ve kontrol görüntüleme gerekmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y74",
        "category": "👂 Kulak Ağrısı & KBB",
        "age": "9 Yaşında",
        "gender": "Erkek",
        "complaint": "İki gündür sağ kulakta giderek artan ağrı, dolgunluk hissi ve az miktarda akıntı",
        "history": "Kendisi anlatıyor: 'Kulağım çok ağrıyor, kulak mememe dokununca daha çok acıyor. Çiğnerken de ağrıyor.' Annesi bir haftadır her gün yüzme kursuna gittiğini, kulağını kulak çubuğuyla temizlediğini anlatıyor. Ateş, burun akıntısı, öksürük yok. Daha önce kulak ameliyatı veya kulak zarı delinmesi olmamış. Diyabet veya bağışıklık sorunu yok.",
        "final_diagnosis": "Akut Otitis Eksterna (Yüzücü Kulağı)",
        "disposition": "Topikal Antibiyotikli Damla, Analjezi ve Kulağı Kuru Tutma Önerisiyle Yeşil Alandan Taburculuk",
        "case_pearl": "Tragusa bası ve kulak kepçesinin çekilmesiyle artan ağrı, dış kulak yolunda ödem, eritem ve debris akut otitis eksternayı düşündürür. Başlıca etkenler P. aeruginosa ve S. aureus'tur. Tedavi topikal antibiyotik (kinolon ± steroid) damladır. Kulak zarı görülemiyorsa ototoksik olmayan damla seçilir. Kanal ödemliyse fitil konur. Oral antibiyotik yalnızca kanal dışına yayılım veya bağışıklık yetmezliğinde gerekir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Kulak ağrısı ve akıntısı olan bu çocukta muayenede neye dikkat edersiniz?",
                "options": [
                    {
                        "text": "Akıntıyı orta kulak iltihabına bağlı delinme kabul edip otoskopi yapmadan oral amoksisilin başlamak ve iki gün sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Amoksisiline rağmen ağrı arttı, kulak yolu tamamen kapandı.",
                        "teaching_point": "Kulak akıntısında otoskopi yapılmadan neden ve tedavi belirlenemez."
                    },
                    {
                        "text": "Tragus ve kulak kepçesine basıyla ağrıyı, kulak arkasını ve yüz sinirini değerlendirmek; otoskopiyle kulak yolu ve kulak zarını incelemek",
                        "is_correct": True,
                        "explanation": "Tragus ve kepçe hareketiyle artan ağrı dış kulak yoluna işaret eder. Kulak arkası ve yüz siniri muayenesi yayılım ve komplikasyonları dışlar. Kulak zarının durumu damla seçimini belirler.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 88/dk. Sağ tragusa bası ve kulak kepçesinin çekilmesi belirgin ağrılı. Dış kulak yolu ödemli ve eritemli, lümen yaklaşık %50 daralmış, beyaz-sarı nemli debris var. Debris nazikçe temizlendikten sonra kulak zarı sağlam ve normal görünümde. Kulak arkası normal, kepçede selülit yok, yüz siniri fonksiyonları normal. Periauriküler küçük hassas lenf nodu."
                    },
                    {
                        "text": "Akıntının kaynağını görmek için muayene öncesi kulağı şırıngayla ılık suyla yıkayıp temizlemek, ardından kulak zarını değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Yıkama sırasında çocuk şiddetli ağrı duydu ve muayeneye uyum sağlayamadı; kanal ödemi arttı.",
                        "teaching_point": "Ödemli ve iltihaplı kulak yolunda su ile yıkama ağrıyı ve enfeksiyonu artırır; temizlik nazikçe aspirasyon veya kuru yöntemle yapılır."
                    },
                    {
                        "text": "Yüzme öyküsü nedeniyle mantar enfeksiyonu düşünüp muayeneyi kısa tutarak topikal antifungal krem önermek ve yüzmeye devam edebileceğini söylemek",
                        "is_correct": False,
                        "scenario_update": "Antifungal kremden yarar görülmedi ve yüzmeye devam eden çocuğun ağrısı arttı.",
                        "teaching_point": "Akut tabloda en sık etken bakteriyeldir; mantar enfeksiyonunda kaşıntı ve tipik hif-spor görünümü baskındır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik ve İlk Müdahale Kararı",
                "question": "Kulak zarı sağlam, kanal %50 daralmış bu çocukta bir sonraki adım nedir?",
                "options": [
                    {
                        "text": "Kulak akıntısından kültür almak ve antibiyogram sonucuna göre tedavi seçmek; sonuç gelene kadar tedaviye başlamamak",
                        "is_correct": False,
                        "scenario_update": "Kültür 72 saat sürdü; bu sürede çocuk ağrıdan uyuyamadı.",
                        "teaching_point": "İlk atakta kültür gerekmez; tedaviye yanıtsız veya tekrarlayan olgularda istenir."
                    },
                    {
                        "text": "Tamponad ve kulak arkası yayılım şüphesiyle temporal kemik bilgisayarlı tomografisi istemek ve sonucu gelince tedaviye karar vermek",
                        "is_correct": False,
                        "scenario_update": "Tomografi yalnızca yumuşak doku ödemi gösterdi; gereksiz radyasyon ve bekleme süresi oluştu.",
                        "teaching_point": "Görüntüleme, kafa tabanına yayılım veya mastoid tutulumu şüphesi olan ağır olgularla sınırlıdır."
                    },
                    {
                        "text": "Debrisi nazikçe temizleyip kanal ödemi damlanın geçişini engelleyecek düzeyde değilse fitil koymadan, tetkik istemeden topikal tedaviye geçmek",
                        "is_correct": True,
                        "explanation": "Kanalın temizlenmesi damlanın dokuya ulaşmasını sağlar. Belirgin ödemde fitil konur. Komplike olmayan ilk atakta kültür ve görüntüleme gerekmez.",
                        "new_finding": "Kanal temizlendi, damla geçişi için yeterli açıklık sağlandı. Kulak zarı sağlam olarak kayda geçti. Tetkik istenmedi."
                    },
                    {
                        "text": "Hemogram ve CRP istemek; değerler yüksekse oral antibiyotik ve damlayı birlikte başlamak, normalse yalnızca analjezik önermek",
                        "is_correct": False,
                        "scenario_update": "Hemogram ve CRP normal geldi, damla başlanmadı; çocuğun ağrısı arttı.",
                        "teaching_point": "Lokal dış kulak yolu enfeksiyonunda kan tetkiki tanıya katkı sağlamaz."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu çocukta en olası tanınız nedir?",
                "options": [
                    {"text": "Perforasyonlu akut otitis media", "is_correct": False, "scenario_update": "Kulak zarı sağlamdı ve ateş yoktu.", "teaching_point": "Perforasyonlu otitis mediada kulak zarında delik görülür ve akıntı orta kulaktan gelir."},
                    {"text": "Akut otitis eksterna", "is_correct": True, "explanation": "Yüzme ve kulak çubuğu öyküsü, tragusa bası ile artan ağrı, kanalda ödem, eritem ve debris ile sağlam kulak zarı akut otitis eksternayı gösterir.", "new_finding": "Tanı: Akut otitis eksterna."},
                    {"text": "Dış kulak yolu fronkülü", "is_correct": False, "scenario_update": "Kanalın tamamında yaygın ödem vardı; lokalize bir pustül veya fluktuasyon yoktu.", "teaching_point": "Fronkülde kanalın dış kısmında sınırlı, kabarık, püylü bir lezyon görülür."},
                    {"text": "Akut mastoidit", "is_correct": False, "scenario_update": "Kulak arkası normaldi, kulak kepçesi öne itilmemişti ve kulak zarı sağlamdı.", "teaching_point": "Mastoiditte kulak arkasında şişlik, kızarıklık ve kepçenin öne itilmesi görülür."}
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Oral amoksisilin-klavulanat 10 gün başlamak, kulağa damla vermemek ve yüzmeye ağrı geçtiğinde hemen devam edebileceğini söylemek",
                        "is_correct": False,
                        "scenario_update": "Oral antibiyotik kulak yolu dokusuna yeterli düzeyde ulaşmadı; yüzmeye dönen çocukta tablo tekrarladı.",
                        "teaching_point": "Komplike olmayan olguda oral antibiyotik gereksizdir; topikal tedavi çok daha etkilidir."
                    },
                    {
                        "text": "Kulak yolunu evde günde iki kez kulak çubuğu ve oksijenli suyla temizlemelerini, ardından antibiyotiksiz yağlı damla kullanmalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Kulak çubuğu kanal derisini daha da tahriş etti; ağrı ve akıntı arttı.",
                        "teaching_point": "Kulak çubuğu kullanımı otitis eksterna için risk faktörüdür ve kaçınılmalıdır."
                    },
                    {
                        "text": "Kinolon-steroid damlayı 7 gün günde iki kez ve ibuprofen önermek; 7-10 gün yüzmeye ara verip kulağı kuru tutmasını söylemek",
                        "is_correct": True,
                        "explanation": "Topikal kinolon P. aeruginosa ve S. aureus'u kapsar ve ototoksik değildir; steroid ödem ve ağrıyı azaltır. 48-72 saatte düzelme yoksa yeniden değerlendirilmelidir.",
                        "new_finding": "Siprofloksasin-hidrokortizon damla ve ibuprofen ile taburcu edildi. 72. saatte ağrı belirgin azaldı, yedinci gün kanal normale döndü."
                    },
                    {
                        "text": "Aminoglikozid içeren damlayı 14 gün günde dört kez önermek ve ağrıyı kesmek için kulak yoluna topikal anestezikli damla eklemek",
                        "is_correct": False,
                        "scenario_update": "Uzun süreli aminoglikozid damla kanal derisinde kontakt dermatit yaptı; ağrı ve kaşıntı arttı.",
                        "teaching_point": "Tedavi süresi genellikle 7 gündür. Uzun süreli kullanım ve neomisin kontakt duyarlılık ile ilişkilidir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y75",
        "category": "🫁 Hırıltı & Solunum Sıkıntısı",
        "age": "7 Yaşında (22 kg)",
        "gender": "Erkek",
        "complaint": "İki gündür artan öksürük, hırıltılı solunum ve geceleri öksürükle uyanma",
        "history": "Annesi anlatıyor: 'Üç yıldır astım tanısı var, koruyucu inhaler sprey verilmişti ama iyi olunca bıraktık. Üç gün önce nezle oldu, sonra öksürük ve hırıltı başladı. Evde mavi spreyi günde 3-4 kez kullandık, biraz rahatlıyor ama birkaç saat sonra tekrar başlıyor.' Konuşurken nefesi kesilmiyor, oynuyor. Daha önce yoğun bakım yatışı yok. Son bir yılda bir kez acil başvurusu olmuş. Evde sigara içiliyor.",
        "final_diagnosis": "Viral Enfeksiyonla Tetiklenen Hafif-Orta Astım Atağı",
        "disposition": "Oral Kortikosteroid, Kontrol Edici İnhaler Tedavi ve Yazılı Eylem Planıyla Yeşil Alandan Taburculuk",
        "case_pearl": "GINA'ya göre hafif-orta atakta çocuk cümle kurabilir, ajite değildir, SpO2 ≥%92'dir. Tedavi ilk saatte 20 dakikada bir 4-10 puf salbutamolün aralayıcıyla verilmesi ve oral prednizolon 1-2 mg/kg (en fazla 40 mg) 3-5 gündür. Rutin akciğer grafisi, kan gazı ve antibiyotik gerekmez. Taburculukta kontrol edici tedavinin (inhaler kortikosteroid) başlanması veya basamağının artırılması, inhaler tekniği, yazılı eylem planı ve 1 hafta içinde kontrol şarttır.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Şiddet Belirleme",
                "question": "Hırıltılı solunumla gelen bu çocukta ilk değerlendirmede hangi yaklaşım doğrudur?",
                "options": [
                    {
                        "text": "Konuşma, solunum sayısı, yardımcı solunum kası kullanımı, bilinç, SpO2 ve oskültasyonla atak şiddetini belirleyip mümkünse PEF ölçmek",
                        "is_correct": True,
                        "explanation": "Tedavi şiddete göre belirlenir: cümle kurabilme, ajitasyon, solunum sayısı, yardımcı kas kullanımı, SpO2 ve PEF temel ölçütlerdir.",
                        "new_finding": "Vital Bulgular: Ateş 37.4°C, KTA 116/dk, SS 30/dk, SpO2 %94 (oda havası), TA 104/64 mmHg. Cümleler halinde konuşuyor, ajitasyon yok. Hafif interkostal çekilme. Bilateral ekspiratuvar yaygın hışıltı, ekspiryum uzamış, hava girişi iyi. PEF beklenen değerin %62'si."
                    },
                    {
                        "text": "Hırıltının nedenini netleştirmek için önce akciğer grafisi ve kan gazı istemek, sonuçlar gelince bronkodilatör tedaviye karar vermek",
                        "is_correct": False,
                        "scenario_update": "Grafide hafif havalanma artışı dışında bulgu yoktu; bekleme süresinde çocuğun solunum sayısı 36/dk'ya çıktı.",
                        "teaching_point": "Bilinen astımlı çocukta atak tedavisi tetkik beklenmeden başlar; rutin grafi ve kan gazı gerekmez."
                    },
                    {
                        "text": "Ateşi 37.4°C olduğu ve nezle ile başladığı için pnömoni düşünüp muayeneden hemen sonra oral amoksisilin başlamak",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik başlandı; hırıltı ve öksürük bronkodilatör verilmediği için düzelmedi.",
                        "teaching_point": "Viral enfeksiyonun tetiklediği astım atağında antibiyotik endikasyonu yoktur; bronkodilatör ve steroid gerekir."
                    },
                    {
                        "text": "Çocuğun rahat konuştuğunu görüp atağın hafif olduğunu varsaymak, SpO2 ölçümü ve oskültasyon yapmadan evdeki mavi spreyi sık aralıklarla sürdürmesini söylemek",
                        "is_correct": False,
                        "scenario_update": "Çocuk eve gönderildi; gece SpO2 düşüşü ve belirgin çekilmelerle yeniden getirildi.",
                        "teaching_point": "Atak şiddeti nesnel ölçütlerle (SpO2, solunum sayısı, PEF) belirlenmeden taburculuk kararı verilmez."
                    }
                ]
            },
            {
                "stage_title": "İlk Tedavi ve Tetkik Kararı",
                "question": "Bu çocuğa acil serviste hangi tedavi verilmelidir?",
                "options": [
                    {
                        "text": "Salbutamol nebülünü ipratropium ile birlikte vermek, damar yolu açarak intravenöz metilprednizolon uygulamak ve magnezyum sülfat eklemek",
                        "is_correct": False,
                        "scenario_update": "Çocuk yoğun tedaviye kısa sürede yanıt verdi; ancak damar yolu ve IV ilaçlar bu atak şiddetinde gereksizdi.",
                        "teaching_point": "Magnezyum ve IV steroid ağır ataklar içindir; ağızdan alabilen çocukta oral steroid aynı etkinliktedir."
                    },
                    {
                        "text": "Aralayıcıyla 20 dakikada bir 6 puf salbutamol (toplam 3 doz) vermek, ilk saatte oral prednizolon 1-2 mg/kg uygulamak ve SpO2'yi izlemek",
                        "is_correct": True,
                        "explanation": "Aralayıcıyla ölçülü doz inhaler en az nebülizer kadar etkilidir. Erken oral kortikosteroid yatış riskini azaltır. Tedaviye yanıt 1 saat sonra yeniden değerlendirilir.",
                        "new_finding": "Üç doz salbutamol ve prednizolon 40 mg sonrası 1. saatte: KTA 124/dk, SS 22/dk, SpO2 %97 (oda havası), çekilme yok, hışıltı azalmış, PEF %84. Dört saat izlemde semptomlar yeniden artmadı."
                    },
                    {
                        "text": "Salbutamolü yalnızca tek doz nebülle vermek, yanıt varsa steroid vermeden çocuğu hemen evdeki inhaleriyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Kısa süre rahatlayan çocuk birkaç saat sonra yeniden hırıltıyla başvurdu.",
                        "teaching_point": "Tek doz yanıt atağın kontrolü için yeterli değildir; oral steroid tekrar başvuruyu azaltır."
                    },
                    {
                        "text": "Montelukast 5 mg ve oral antihistaminik verip bir saat gözlemlemek, iyileşme yoksa salbutamol eklemeyi düşünmek",
                        "is_correct": False,
                        "scenario_update": "Bir saatte hırıltı ve solunum sayısı arttı, SpO2 %92'ye düştü.",
                        "teaching_point": "Akut atakta ilk tedavi kısa etkili beta-agonist ve sistemik steroiddir; montelukast ve antihistaminik akut tedavide yer almaz."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı ve Atak Şiddeti",
                "question": "Başlangıç bulgularına göre bu atağı nasıl sınıflandırırsınız?",
                "options": [
                    {"text": "Ağır astım atağı", "is_correct": False, "scenario_update": "Çocuk cümle kurabiliyordu, ajite değildi ve SpO2 %94'tü.", "teaching_point": "Ağır atakta kelimelerle konuşma, ajitasyon, belirgin çekilme ve SpO2 <%92 olur."},
                    {"text": "Hayatı tehdit eden astım atağı", "is_correct": False, "scenario_update": "Bilinç açıktı, sessiz akciğer veya siyanoz yoktu.", "teaching_point": "Sessiz akciğer, siyanoz, bilinç bozukluğu ve bitkinlik hayatı tehdit eden atağı gösterir."},
                    {"text": "Viral tetikli hafif-orta astım atağı", "is_correct": True, "explanation": "Cümle kurabilme, ajitasyon olmaması, SpO2 %94 ve PEF %62 hafif-orta atakla uyumludur. Tetikleyici viral enfeksiyon ve kontrol edici tedavinin bırakılmasıdır.", "new_finding": "Tanı: Viral tetikli hafif-orta astım atağı."},
                    {"text": "Yabancı cisim aspirasyonu", "is_correct": False, "scenario_update": "Hışıltı bilateral ve simetrikti, bronkodilatöre hızlı yanıt verdi ve öyküde boğulma epizodu yoktu.", "teaching_point": "Aspirasyonda ani başlangıç, tek taraflı hışıltı ve bronkodilatöre yanıtsızlık beklenir."}
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun taburculuk planı hangisidir?",
                "options": [
                    {
                        "text": "Evde kullanılmak üzere nebülizatör cihazı reçete etmek, salbutamol nebülünü günde dört kez sürdürmek ve kontrol edici tedaviyi atak bitince değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk nebülle evde sık salbutamol aldı ancak kontrol edici tedavi başlanmadığı için iki ay içinde yeniden atak geçirdi.",
                        "teaching_point": "Aralayıcıyla inhaler nebülizatör kadar etkilidir; atak sonrası kontrol edici tedavinin başlanması veya artırılması ertelenmemelidir."
                    },
                    {
                        "text": "Prednizolonu 3 güne tamamlatmak, düşük doz inhaler kortikosteroidi yeniden başlatmak, aralayıcı tekniği ve yazılı eylem planı vermek",
                        "is_correct": True,
                        "explanation": "Atak sonrası kontrol edici tedavinin başlanması yeni ataklarını önler. İnhaler tekniği, uyum, tetikleyiciler (evde sigara) ve yazılı plan taburculuğun temel parçalarıdır.",
                        "new_finding": "Çocuk prednizolon, düşük doz budesonid ve gerektiğinde salbutamol ile taburcu edildi. Aileye sigara dumanından korunma anlatıldı. Bir hafta sonraki kontrolde semptomsuzdu, PEF %95."
                    },
                    {
                        "text": "Kontrol edici olarak yalnızca uzun etkili beta-agonist içeren inhaler başlamak ve kortikosteroid kullanımının büyümeyi etkileyeceği için önermemek",
                        "is_correct": False,
                        "scenario_update": "Steroidsiz uzun etkili beta-agonist kullanımı sonrası çocuk üç hafta içinde daha ağır bir atakla geldi.",
                        "teaching_point": "Uzun etkili beta-agonist tek başına kullanılmaz; düşük doz inhaler kortikosteroidin büyüme üzerine etkisi klinik açıdan önemsizdir."
                    },
                    {
                        "text": "Oral steroid yerine 10 gün antibiyotik ve öksürük şurubu reçete etmek, astım kontrolünü değerlendirmek için 3 ay sonra randevu vermek",
                        "is_correct": False,
                        "scenario_update": "Öksürük sürdü; çocuk iki hafta sonra aynı yakınmalarla geri geldi.",
                        "teaching_point": "Antibiyotik ve öksürük şurubu astım atağında yarar sağlamaz; atak sonrası erken kontrol gereklidir."
                    }
                ]
            }
        ]
    }
]
