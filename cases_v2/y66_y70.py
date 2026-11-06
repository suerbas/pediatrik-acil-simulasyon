# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - Y66-Y70 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "Y66",
        "category": "🩸 Hematolojik & Onkolojik Aciller",
        "age": "6 Yaşında",
        "gender": "Erkek",
        "complaint": "Lösemi tedavisi alan çocukta üşüme-titreme ile başlayan 38.9°C ateş ve halsizlik",
        "history": "Ailesi anlatıyor: 'Akut lenfoblastik lösemi tedavisi alıyor, son kemoterapisini 9 gün önce aldı. Göğsünde port var. Bir saat önce titreyerek ateşlendi, 38.9°C ölçtük. Halsiz, yemek yemiyor. Port bölgesinde kızarıklık yok.' Öksürük, ishal ve idrar yakınması yok. Hematoloji ateşlenirse hemen gelmelerini söylemiş. Penisilin alerjisi yok. Tartı: 20 kg.",
        "final_diagnosis": "Kemoterapi Sonrası Febril Nötropeni (Yüksek Risk, Santral Venöz Kateterli)",
        "disposition": "Sarı Alanda İlk 60 Dakikada Kültür Sonrası İntravenöz Antipsödomonal Beta-Laktam ile Çocuk Hematoloji-Onkoloji Yatışı",
        "case_pearl": "Kemoterapi alan çocukta tek ölçümde ≥38.3°C ya da bir saat süren ≥38.0°C ateş ve mutlak nötrofil sayısı <500/mm³ (veya 48 saatte <500'e düşmesi beklenen) acil durumdur. Nötropenik hastada enflamasyon bulguları silik olabilir; ilk belirti yalnızca ateştir. Kan kültürü (kateterin tüm lümenlerinden, mümkünse periferden) alındıktan sonra antipsödomonal beta-laktam monoterapisi (sefepim, piperasilin-tazobaktam) başvurudan itibaren 60 dakika içinde verilmelidir. Hipotansiyon, kateter giriş yeri enfeksiyonu veya MRSA kolonizasyonunda vankomisin eklenir. Rektal ölçüm ve rektal muayene yapılmaz.",
        "steps": [
            {
                "stage_title": "Triaj ve İlk Değerlendirme",
                "question": "Kemoterapi alan, portu olan ve titreyerek ateşlenen bu çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Ateşin nedenini netleştirmek için önce tam kan sayımı sonucunu beklemek, nötrofil düşükse antibiyotik başlamayı değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Hemogram sonucu 75 dakika sonra çıktı; antibiyotik penceresi kaçırıldı.",
                        "teaching_point": "Ampirik antibiyotik nötrofil sonucunu beklemeden, başvurudan itibaren 60 dakika içinde verilmelidir."
                    },
                    {
                        "text": "Hemen izole odaya almak; perfüzyonu değerlendirmek, port bölgesi, ağız, deri ve perianal bölgeyi rektal muayene yapmadan incelemek",
                        "is_correct": True,
                        "explanation": "Bağışıklığı baskılanmış çocuk enfeksiyondan korunmalı ve şok açısından hızla değerlendirilmelidir. Mukozit, kateter enfeksiyonu, selülit ve perianal apse sık odaklardır. Rektal girişim bakteriyemi riski nedeniyle yapılmaz.",
                        "new_finding": "Vital Bulgular: Ateş 38.9°C, KTA 136/dk, SS 24/dk, SpO2 %98, TA 98/58 mmHg, KDZ 2 sn. Bilinç açık, halsiz. Ağızda hafif mukozit, port giriş yeri temiz, kızarıklık ve hassasiyet yok. Akciğer sesleri doğal. Perianal bölgede kızarıklık yok. Deri lezyonu yok."
                    },
                    {
                        "text": "Ateşin doğruluğunu kontrol etmek için rektal ölçüm yapmak ve olası perianal odağı aramak için parmakla rektal muayene uygulamak",
                        "is_correct": False,
                        "scenario_update": "Rektal muayene sonrası mukozada küçük bir kanama oldu; bakteriyemi riski arttı.",
                        "teaching_point": "Nötropeni olasılığı olan çocukta rektal ölçüm, rektal muayene ve fitil kullanılmaz."
                    },
                    {
                        "text": "Bekleme salonunda sıra beklemesine izin vermek, ateş düşürücü verip bir saat sonra ateşi kontrol ederek hekime almak",
                        "is_correct": False,
                        "scenario_update": "Bekleme salonunda geçen 80 dakikada çocukta taşikardi ve soğuk ekstremiteler gelişti.",
                        "teaching_point": "Kemoterapi alan ateşli çocuk triajda öncelikli alınır; antibiyotiğe kadar geçen süre sağkalımı etkiler."
                    }
                ]
            },
            {
                "stage_title": "Kültürler ve Antibiyotik Zamanlaması",
                "question": "Hemodinamisi şu an stabil olan bu çocukta tetkik ve tedavi sıralaması nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Ateş kaynağını göstermek için önce akciğer grafisi, batın ultrasonu ve ekokardiyografi yaptırmak, odak bulunursa antibiyotik seçmek",
                        "is_correct": False,
                        "scenario_update": "Görüntülemeler iki saat sürdü ve odak bulunamadı; antibiyotik gecikti.",
                        "teaching_point": "Bu hastaların çoğunda odak bulunmaz; ampirik tedavi görüntüleme beklenmeden başlanır."
                    },
                    {
                        "text": "Kültür alamadan portu çıkarmak için cerrahiye danışmak ve kateter ucu kültürü gelene kadar antibiyotiği ertelemek",
                        "is_correct": False,
                        "scenario_update": "Cerrahi görüş saatler aldı; port yerinde enfeksiyon bulgusu yoktu ve çıkarılması gereksizdi.",
                        "teaching_point": "Kateter çıkarılması tünel enfeksiyonu, septik tromboz veya dirençli bakteriyemide gündeme gelir."
                    },
                    {
                        "text": "Port ve periferden kan kültürü, hemogram, CRP ve biyokimya almak; 60 dakika içinde antipsödomonal antibiyotik başlamak",
                        "is_correct": True,
                        "explanation": "Kültürler antibiyotik öncesinde alınır ancak tedaviyi geciktirmemelidir. İdrar kültürü idrar sondası olmadan alınabiliyorsa gönderilir. Akciğer grafisi solunum bulgusu varsa çekilir.",
                        "new_finding": "Kültürler alındı, başvurunun 40. dakikasında antibiyotik verildi. Lökosit 400/mm³, mutlak nötrofil sayısı 162/mm³, Hb 8.4 g/dL, trombosit 38.000/mm³, CRP 46 mg/L. Laktat 1.6 mmol/L. Kreatinin ve karaciğer testleri normal. Tam idrar normal."
                    },
                    {
                        "text": "Ateşli ancak iyi görünen çocuğa oral amoksisilin-klavulanat verip ertesi gün hematoloji polikliniğine kontrole göndermek",
                        "is_correct": False,
                        "scenario_update": "Gece evde çocuk hipotansif hale geldi ve septik şokla getirildi.",
                        "teaching_point": "Yüksek riskli hastada ilk tedavi yatırılarak intravenöz yoldan verilir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Kemoterapiden 9 gün sonra 38.9°C ateşi ve mutlak nötrofil sayısı 162/mm³ olan, belirgin odağı bulunmayan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Kateter ilişkili tünel enfeksiyonu",
                        "is_correct": False,
                        "scenario_update": "Port giriş yeri ve tünel hattında kızarıklık, hassasiyet veya akıntı yok.",
                        "teaching_point": "Tünel enfeksiyonunda kateter hattı boyunca selülit görülür."
                    },
                    {
                        "text": "Kemoterapiye bağlı ilaç ateşi",
                        "is_correct": False,
                        "scenario_update": "Son kemoterapiden 9 gün geçmiş ve ağır nötropeni var; enfeksiyon dışlanmadan bu tanı konmaz.",
                        "teaching_point": "Nötropenik hastada ateş, aksi kanıtlanana kadar enfeksiyon kabul edilir."
                    },
                    {
                        "text": "Kemoterapi sonrası febril nötropeni",
                        "is_correct": True,
                        "explanation": "Kemoterapi alan çocukta ≥38.3°C ateş ve mutlak nötrofil sayısının 500/mm³'ün altında olması febril nötropeniyi tanımlar.",
                        "new_finding": "Tanı: Kemoterapi Sonrası Febril Nötropeni (yüksek risk, santral venöz kateterli)."
                    },
                    {
                        "text": "Tümör lizis sendromu",
                        "is_correct": False,
                        "scenario_update": "Potasyum, fosfor, ürik asit ve kreatinin normal; tedavinin başlangıç dönemi değil.",
                        "teaching_point": "Tümör lizis sendromu genellikle tedavinin ilk günlerinde metabolik bozukluklarla ortaya çıkar."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu çocuğun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Nötrofil sayısını hızla artırmak için granülosit transfüzyonu yapmak ve antibiyotiği yalnızca kültür üremesi olursa başlamak",
                        "is_correct": False,
                        "scenario_update": "Granülosit transfüzyonu bu aşamada endike değildi; antibiyotiksiz kalan çocukta tablo ağırlaştı.",
                        "teaching_point": "Kültür sonucu beklenmeden ampirik antibiyotik sürdürülmelidir."
                    },
                    {
                        "text": "Tek doz intravenöz seftriakson verip çocuğu evde oral siprofloksasinle izlemek ve 48 saat sonra yeniden değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Seftriakson Pseudomonas'ı kapsamadı; evde ateşi süren çocuk yeniden başvurdu.",
                        "teaching_point": "Ayaktan tedavi yalnızca düşük riskli seçilmiş hastalarda düşünülür; lösemide indüksiyon ve kateter yüksek risktir."
                    },
                    {
                        "text": "İlk tedaviye rutin olarak vankomisin, amikasin ve amfoterisin B eklemek ve tüm antibiyotikleri en az üç hafta sürdürmek",
                        "is_correct": False,
                        "scenario_update": "Gereksiz kombinasyon tedavisi sonrası kreatinin yükseldi ve işitme testinde bozulma saptandı.",
                        "teaching_point": "Stabil hastada monoterapi yeterlidir; rutin kombinasyon toksisiteyi artırır."
                    },
                    {
                        "text": "Sefepim veya piperasilin-tazobaktam monoterapisini sürdürüp hematoloji servisine yatırmak; hipotansiyon veya kateter enfeksiyonu gelişirse vankomisin eklemek",
                        "is_correct": True,
                        "explanation": "Antipsödomonal beta-laktam monoterapisi ilk seçenektir. Rutin vankomisin önerilmez; hemodinamik bozulma, kateter giriş yeri enfeksiyonu, pnömoni veya gram pozitif üreme durumunda eklenir. 96 saati aşan ateşte mantar enfeksiyonu araştırılır.",
                        "new_finding": "Sefepim ile 48. saatte ateş düştü, kan kültürü negatif kaldı. Nötrofil sayısı 7. günde 600/mm³'ün üzerine çıktı ve antibiyotik kesildi."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y67",
        "category": "🩸 Hematolojik & Onkolojik Aciller",
        "age": "9 Yaşında",
        "gender": "Kız",
        "complaint": "Bacaklarda, sırtta ve göğüste dayanılmaz ağrı; evde verilen ağrı kesicilere yanıt yok",
        "history": "Ailesi anlatıyor: 'Kalıtsal bir kan hastalığı var, hidroksiüre kullanıyor. Dün akşam soğuk havada okul gezisinden döndükten sonra bacaklarında ve belinde ağrı başladı. Evde ibuprofen ve parasetamol verdik, geçmedi. Ağrısı 10 üzerinden 9 diyor, ağlıyor, yürüyemiyor.' Bugün az su içmiş. Ateş, öksürük ve nefes darlığı yok. Önceki ağrı ataklarında morfin almış. Bilinen hemoglobin değeri 7.8 g/dL. Tartı: 28 kg.",
        "final_diagnosis": "Orak Hücre Anemisinde Akut Vazo-Oklüzif Ağrı Krizi",
        "disposition": "Sarı Alanda 60 Dakika İçinde İntravenöz Opioid, NSAİİ, İdame Sıvı ve Teşvik Spirometrisi ile Çocuk Hematoloji Yatışı",
        "case_pearl": "Orak hücre hastalığında soğuk, dehidratasyon, enfeksiyon ve stres vazo-oklüzyonu tetikler. Ağrı krizinde hedef, triajdan sonraki 60 dakika içinde (ideal 30 dakika) intravenöz veya intranazal opioid vermek ve 15-30 dakikada bir yeniden değerlendirmektir. Aşırı sıvı akut göğüs sendromunu tetikleyebileceği için idame sıvı verilir. Teşvik spirometrisi akut göğüs sendromunu önler. Ateş fonksiyonel aspleni nedeniyle acil kabul edilir. Hb'nin bazal değerden ≥2 g/dL düşmesi dalak sekestrasyonu veya aplastik krizi düşündürür.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Ağrı Yönetimi",
                "question": "Bilinen kalıtsal kan hastalığı olan ve şiddetli ağrıyla gelen bu çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Dehidratasyonu düzeltmek için iki kez 20 mL/kg serum fizyolojik bolusu vermek, ağrı kesiciyi sıvı tamamlanıp idrar çıkışı görüldükten sonra başlamak",
                        "is_correct": False,
                        "scenario_update": "Hızlı sıvı yüklemesi sonrası solunum hızı arttı, satürasyon %92'ye düştü; ağrı tedavisi gecikti.",
                        "teaching_point": "Aşırı sıvı akciğer komplikasyonunu tetikleyebilir; ağrı kesici sıvıyı beklemeden verilir."
                    },
                    {
                        "text": "Vital bulgular, ağrı skoru, göğüs ve dalak muayenesini yapıp 30 dakika içinde intravenöz morfin vermek ve sık yeniden değerlendirmek",
                        "is_correct": True,
                        "explanation": "Şiddetli ağrı hızla opioidle tedavi edilir. Göğüs muayenesi akut göğüs sendromu, dalak boyutu sekestrasyon açısından önemlidir. Ateş ve nörolojik bulgu ayrı aciller gerektirir. NSAİİ böbrek fonksiyonu normalse eklenir.",
                        "new_finding": "Vital Bulgular: Ateş 37.4°C, KTA 118/dk, SS 22/dk, SpO2 %96 (bazal %97), TA 108/66 mmHg. Konjonktivalar soluk, sklerada hafif sarılık. Akciğer sesleri doğal. Dalak ele gelmiyor. Nörolojik muayene normal. Alt ekstremite ve lomber bölgede yaygın hassasiyet, şişlik yok. Ağrı skoru 9/10. Morfin 0.1 mg/kg intravenöz verildi."
                    },
                    {
                        "text": "Ağrının gerçekliğini anlamak için bir saat gözlemlemek ve ağrı kesici talebini bağımlılık riski açısından sorgulamak",
                        "is_correct": False,
                        "scenario_update": "Analjezi gecikti; çocuğun ağrısı arttı ve aile güvenini kaybetti.",
                        "teaching_point": "Bu hastalarda ağrı öznel bildirime göre tedavi edilir; analjezi gecikmesi sık ve önlenebilir bir hatadır."
                    },
                    {
                        "text": "Ağrıyı hafifletmek için ağrılı bölgelere buz uygulamak ve ağrı kesici olarak yalnızca intramüsküler diklofenak yapmak",
                        "is_correct": False,
                        "scenario_update": "Soğuk uygulama damar daralmasını artırdı ve ağrı kötüleşti; tek başına NSAİİ yetersiz kaldı.",
                        "teaching_point": "Soğuk uygulama tetikleyicidir; şiddetli ağrıda opioid gerekir ve intramüsküler yol önerilmez."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar Değerlendirmesi",
                "question": "Analjezi başlanan bu çocukta hangi tetkikler öncelikli olarak istenmelidir?",
                "options": [
                    {
                        "text": "Ağrılı bölgelerin tamamından direkt grafi çekmek ve kırık saptanmazsa analjeziyi azaltarak çocuğu taburcu etmeyi planlamak",
                        "is_correct": False,
                        "scenario_update": "Grafiler normal geldi; analjezi azaltılınca ağrı yeniden şiddetlendi.",
                        "teaching_point": "Normal grafi ağrı krizini dışlamaz; analjezi klinik yanıta göre ayarlanır."
                    },
                    {
                        "text": "Ağrının nedenini görmek için tüm vücut kemik sintigrafisi ve lomber manyetik rezonans çekmek, sonuçlara göre analjezi dozunu ayarlamak",
                        "is_correct": False,
                        "scenario_update": "Tetkikler gereksizdi; çocuk saatlerce görüntüleme biriminde bekletildi.",
                        "teaching_point": "Tipik ağrı ataklarında ileri görüntüleme gerekmez; osteomiyelit şüphesinde seçici kullanılır."
                    },
                    {
                        "text": "Yalnızca CRP ve prokalsitonin istemek, değerler yüksekse ağrıyı enfeksiyona bağlayıp geniş spektrumlu antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "Ateşsiz çocukta gereksiz antibiyotik başlandı; hemoglobin ve retikülosit değerlendirilmedi.",
                        "teaching_point": "Ağrı krizinde inflamatuvar belirteçler yükselebilir; ateş yoksa antibiyotik gerekmez."
                    },
                    {
                        "text": "Hemogram ve retikülosit sayısı, biyokimya, bilirubin, LDH ve kan grubu-tarama istemek; bazal değerlerle karşılaştırıp göğüs muayenesini tekrarlamak",
                        "is_correct": True,
                        "explanation": "Hb'nin bazalden belirgin düşmesi sekestrasyon veya aplastik krizi, düşük retikülosit parvovirüs B19'u düşündürür. Kan grubu olası transfüzyon için hazırlıktır. Göğüs ağrısı, ateş veya hipoksi gelişirse akciğer grafisi çekilir.",
                        "new_finding": "Hb 7.6 g/dL (bazal 7.8), retikülosit %9.2, lökosit 13.800/mm³, trombosit 410.000/mm³. Total bilirubin 3.1 mg/dL (indirekt ağırlıklı), LDH 620 U/L, kreatinin 0.4 mg/dL. Kan grubu ve antikor taraması gönderildi. Morfin sonrası ağrı skoru 5/10."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Hidroksiüre kullanan, soğuk ve sıvı azlığı sonrası yaygın kemik ağrısı başlayan, Hb bazale yakın, retikülositi yüksek ve göğüs bulgusu olmayan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Parvovirüs B19 ilişkili aplastik kriz",
                        "is_correct": False,
                        "scenario_update": "Retikülosit sayısı yüksek ve Hb düşmemiş.",
                        "teaching_point": "Aplastik krizde retikülosit belirgin düşer ve Hb hızla azalır."
                    },
                    {
                        "text": "Akut göğüs sendromu",
                        "is_correct": False,
                        "scenario_update": "Göğüs ağrısı, ateş, hipoksi ve akciğer bulgusu yok.",
                        "teaching_point": "Akut göğüs sendromunda grafide yeni infiltrat ile ateş veya solunum bulgusu birlikte bulunur."
                    },
                    {
                        "text": "Orak hücre hastalığında vazo-oklüzif ağrı krizi",
                        "is_correct": True,
                        "explanation": "Tetikleyici sonrası yaygın kemik ağrısı, bazal düzeyde Hb, yüksek retikülosit ve hemoliz bulguları ile göğüs ve dalak bulgusu olmaması akut vazo-oklüzif krizi doğrular.",
                        "new_finding": "Tanı: Orak Hücre Anemisinde Akut Vazo-Oklüzif Ağrı Krizi."
                    },
                    {
                        "text": "Akut dalak sekestrasyonu",
                        "is_correct": False,
                        "scenario_update": "Dalak ele gelmiyor ve Hb bazal değere yakın.",
                        "teaching_point": "Dalak sekestrasyonunda dalak hızla büyür ve Hb bazalden ≥2 g/dL düşer."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve İzlem",
                "question": "Ağrısı kısmen gerileyen bu çocuğun yatış tedavisi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Oksijen satürasyonu normal olmasına karşın tüm hastalara rutin yüksek akımlı oksijen vermek ve intravenöz sıvıyı iki katı idamede tutmak",
                        "is_correct": False,
                        "scenario_update": "Fazla sıvı ile çocukta raller ve hipoksi gelişti.",
                        "teaching_point": "Oksijen yalnızca hipokside verilir; sıvı idame hızını belirgin aşmamalıdır."
                    },
                    {
                        "text": "Morfin hasta kontrollü analjezi ve düzenli NSAİİ vermek, idame sıvıyla devam etmek, saatlik teşvik spirometrisi ve satürasyon izlemi uygulamak",
                        "is_correct": True,
                        "explanation": "Düzenli analjezi ağrıyı kontrol eder. İdame sıvı dehidratasyonu düzeltir ancak akciğer ödemine yol açmaz. Teşvik spirometrisi atelektaziyi ve akut göğüs sendromunu önler. Opioid kullanırken sedasyon ve solunum izlenir.",
                        "new_finding": "Hasta kontrollü analjezi, ibuprofen ve idame sıvı başlandı, teşvik spirometrisi öğretildi. 48. saatte ağrı skoru 3/10'a indi, oral analjeziye geçildi. Akut göğüs sendromu gelişmedi; dördüncü gün taburcu edildi."
                    },
                    {
                        "text": "Solunum depresyonu riski nedeniyle opioidleri kesip yalnızca parasetamol vermek ve hastayı yatakta hareketsiz tutmak",
                        "is_correct": False,
                        "scenario_update": "Ağrı kontrol edilemedi; hareketsiz kalan çocukta yüzeyel solunum ve atelektazi gelişti.",
                        "teaching_point": "Yeterli analjezi ve erken mobilizasyon akciğer komplikasyonlarını azaltır."
                    },
                    {
                        "text": "Anemiyi düzeltmek için hemen 20 mL/kg eritrosit süspansiyonu vermek ve hemoglobini 12 g/dL'nin üzerine çıkarmak",
                        "is_correct": False,
                        "scenario_update": "Yüksek hemoglobin kan viskozitesini artırdı ve ağrı kötüleşti.",
                        "teaching_point": "Komplikasyonsuz ağrı krizinde transfüzyon endike değildir; hedef Hb 10 g/dL'yi aşmamalıdır."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y68",
        "category": "👶 Yenidoğan Acilleri",
        "age": "3 Günlük",
        "gender": "Erkek",
        "complaint": "Doğumdan sonraki ilk gün başlayan ve hızla koyulaşan sarılık, uykuya meyil ve emmede azalma",
        "history": "Ailesi anlatıyor: 'Miadında, normal doğumla 3400 gram doğdu. Doğumdan yaklaşık 20 saat sonra yüzü sararmaya başladı, taburcu olurken söylemiştik ama kontrole çağırdılar. Sarılık bugün karnına ve bacaklarına yayıldı. Daha uykulu, emmesi azaldı.' Sadece anne sütü alıyor, günde 6 ıslak bez. Kaka rengi sarı. Annenin kan grubu O Rh pozitif, bebeğinki bilinmiyor. Ağabeyi de yenidoğanda ışık tedavisi almış. Tartı: 3180 g (doğum ağırlığının %6.5 altı).",
        "final_diagnosis": "ABO Uyuşmazlığına Bağlı Ağır İndirekt Hiperbilirubinemi (Hemolitik Hastalık)",
        "disposition": "Sarı Alanda Yoğun Fototerapi Başlanarak Kan Değişimi Hazırlığı ile Yenidoğan Yoğun Bakım Yatışı",
        "case_pearl": "İlk 24 saatte başlayan sarılık her zaman patolojiktir ve en sık hemolitik hastalığa bağlıdır. Anne O, bebek A veya B grubu olduğunda direkt Coombs pozitifliği ABO uyuşmazlığını destekler. Tedavi eşikleri AAP 2022 kılavuzunda doğum haftası, saatlik yaş ve nörotoksisite risk faktörlerine (hemoliz, albümin <3 g/dL, sepsis, letarji) göre belirlenir. Bilirubin kan değişimi eşiğinin 2 mg/dL altına yaklaştığında 'eskalasyon bakımı' başlar: yoğun fototerapi, kan değişimi hazırlığı ve hemolizde İVİG. Akut bilirubin ensefalopatisi bulguları (hipertoni, opistotonus, tiz ağlama) varsa acil kan değişimi yapılır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "İlk gün başlayan ve hızla artan sarılıkla gelen, uykulu bu 3 günlük bebekte ilk değerlendirmede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Sarılığın derecesini deri rengine bakarak tahmin etmek, karnın altına inmediyse tetkik istemeden kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Görsel değerlendirme düzeyi olduğundan düşük tahmin etti; ölçüm yapılmadı.",
                        "teaching_point": "Görsel değerlendirme güvenilir değildir; şüphede serum bilirubini ölçülmelidir."
                    },
                    {
                        "text": "Uykuya meyil nedeniyle önce menenjiti dışlamak için lomber ponksiyon yapmak ve sarılığın değerlendirmesini ponksiyon sonucu çıktıktan sonraya bırakmak",
                        "is_correct": False,
                        "scenario_update": "Lomber ponksiyon normal geldi; bu sürede sarılık düzeyi ölçülmedi.",
                        "teaching_point": "Ağır sarılıklı letarjik yenidoğanda öncelik serum bilirubinini ölçüp tedaviye başlamaktır."
                    },
                    {
                        "text": "Sarılığı anne sütüne bağlamak, emzirmeyi iki gün kesip mama vermelerini ve bebeği güneş ışığına çıkarmalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Bebek eve gönderildi; ertesi gün tiz ağlama ve geriye kasılma ile getirildi.",
                        "teaching_point": "İlk 24 saatte başlayan sarılık fizyolojik veya anne sütüne bağlı değildir; güneş ışığı tedavi değildir."
                    },
                    {
                        "text": "Vital bulgular ve hidrasyonu değerlendirmek; tonus, emme ve ağlamayı muayene edip sarılığın yaygınlığını ve hepatosplenomegaliyi incelemek",
                        "is_correct": True,
                        "explanation": "Uykuya meyil ve emmede azalma bilirubin nörotoksisitesinin erken bulgusu olabilir. Hipertoni, opistotonus ve tiz ağlama ileri evreyi gösterir. Hepatosplenomegali hemolizi, ateş ve kötü görünüm sepsisi düşündürür.",
                        "new_finding": "Vital Bulgular: Ateş 36.9°C, KTA 148/dk, SS 46/dk, SpO2 %98. Belirgin sarılık ayak tabanlarına kadar yayılmış. Hafif letarjik ancak uyarılabiliyor, emme refleksi zayıf; hipertoni, opistotonus ve tiz ağlama yok. Fontanel normal. Karaciğer 2 cm, dalak kot kavsinde ele geliyor. Sefal hematom yok."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar Değerlendirmesi",
                "question": "Bu bebekte hangi tetkikler öncelikli olarak istenmelidir?",
                "options": [
                    {
                        "text": "Biliyer atreziyi dışlamak için hepatobiliyer sintigrafi ve karın ultrasonu istemek, sonuç gelene kadar fototerapiyi ertelemek",
                        "is_correct": False,
                        "scenario_update": "Direkt bilirubin normal çıktı; sintigrafi gereksizdi ve tedavi gecikti.",
                        "teaching_point": "Kolestaz tetkiki direkt bilirubin yüksekliğinde yapılır; indirekt sarılıkta fototerapi geciktirilmez."
                    },
                    {
                        "text": "Total ve direkt bilirubin, bebeğin kan grubu ve direkt Coombs testi, hemogram, retikülosit, yayma, albümin ve G6PD istemek",
                        "is_correct": True,
                        "explanation": "Total bilirubin saatlik yaşa göre değerlendirilir. Direkt bilirubin kolestazı dışlar. Kan grubu ve Coombs immün hemolizi, yayma ve G6PD diğer hemoliz nedenlerini araştırır. Düşük albümin nörotoksisite riskini artırır.",
                        "new_finding": "Total serum bilirubini 20.4 mg/dL (68. saat), direkt bilirubin 0.6 mg/dL. Bebek kan grubu A Rh pozitif, direkt Coombs pozitif. Hb 12.8 g/dL, retikülosit %8.6, yaymada sferositler. Albümin 3.2 g/dL, G6PD normal. Kan değişimi eşiği bu yaş ve risk için yaklaşık 21 mg/dL."
                    },
                    {
                        "text": "Yalnızca transkutanöz bilirubin ölçmek ve değer 15 mg/dL'nin üzerinde çıkarsa 24 saat sonra serum düzeyini tekrar değerlendirmek, bu sürede emzirmeyi sürdürmelerini önermek",
                        "is_correct": False,
                        "scenario_update": "Transkutanöz ölçüm yüksek düzeyde güvenilmez kaldı; tedavi bir gün gecikti.",
                        "teaching_point": "Transkutanöz değer yüksekse veya tedavi eşiğine yakınsa serum bilirubini hemen ölçülmelidir."
                    },
                    {
                        "text": "Konjenital hipotiroidiyi dışlamak için tiroid fonksiyon testleri göndermek ve sonuç gelene kadar bebeği taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Tiroid testleri normal geldi; evde sarılık arttı.",
                        "teaching_point": "Hipotiroidi uzamış sarılığın nedenidir; erken başlayan hızlı sarılığı açıklamaz."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "İlk 24 saatte başlayan sarılığı, 68. saatte total bilirubini 20.4 mg/dL, annesi O, kendisi A grubu, direkt Coombs testi pozitif ve sferositleri olan bu bebekte tanı nedir?",
                "options": [
                    {
                        "text": "Anne sütü sarılığı",
                        "is_correct": False,
                        "scenario_update": "Sarılık ilk 24 saatte başladı ve Coombs pozitif hemoliz var.",
                        "teaching_point": "Anne sütü sarılığı ilk haftadan sonra ortaya çıkan, iyi görünümlü bebekte uzamış sarılıktır."
                    },
                    {
                        "text": "Herediter sferositoz",
                        "is_correct": False,
                        "scenario_update": "Direkt Coombs pozitif ve anne-bebek kan grubu uyumsuz.",
                        "teaching_point": "Herediter sferositozda Coombs negatiftir ve aile öyküsünde splenektomi veya anemi bulunur."
                    },
                    {
                        "text": "ABO uyuşmazlığına bağlı hemolitik hiperbilirubinemi",
                        "is_correct": True,
                        "explanation": "O grubu anne, A grubu bebek, pozitif direkt Coombs, retikülositoz, sferositler ve erken başlangıç ABO hemolitik hastalığını doğrular.",
                        "new_finding": "Tanı: ABO Uyuşmazlığına Bağlı Ağır İndirekt Hiperbilirubinemi."
                    },
                    {
                        "text": "G6PD eksikliğine bağlı hemoliz",
                        "is_correct": False,
                        "scenario_update": "G6PD düzeyi normal ve Coombs testi pozitif.",
                        "teaching_point": "G6PD eksikliğinde Coombs negatiftir ve enzim düzeyi düşüktür."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bilirubini kan değişimi eşiğine yaklaşan bu bebeğin tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Standart fototerapiyi evde vermek, beslenmeyi artırmalarını önermek ve 24 saat sonra bilirubin kontrolüne çağırmak",
                        "is_correct": False,
                        "scenario_update": "Evde bilirubin 25 mg/dL'ye yükseldi; bebek hipertoni ile getirildi.",
                        "teaching_point": "Hemolizli ve eşiğe yakın bebekte ev fototerapisi uygun değildir."
                    },
                    {
                        "text": "Bilirubini düşürmek için fototerapi yerine bol miktarda %5 dekstrozlu su vermek ve fenobarbital başlamak",
                        "is_correct": False,
                        "scenario_update": "Dekstrozlu su hiponatremiye yol açtı ve bilirubin düşmedi.",
                        "teaching_point": "Su veya dekstroz takviyesi bilirubini düşürmez; fenobarbital akut tedavide yer almaz."
                    },
                    {
                        "text": "Bilirubin eşiğe yaklaştığı için fototerapi denemeden doğrudan acil kan değişimi yapmak ve emzirmeyi kalıcı olarak kesip mamaya geçirmek",
                        "is_correct": False,
                        "scenario_update": "Ensefalopati bulgusu olmayan bebekte hazırlıksız işlem komplikasyon riskini artırdı.",
                        "teaching_point": "Ensefalopati yoksa önce yoğun fototerapi ve İVİG uygulanır; emzirme sürdürülür."
                    },
                    {
                        "text": "Hemen yoğun fototerapi başlamak, kan değişimi için kan hazırlatmak, İVİG vermek ve bilirubini 2-3 saatte bir ölçmek",
                        "is_correct": True,
                        "explanation": "Yoğun fototerapi bilirubini hızla düşürür. Kan değişimi eşiğine yaklaşılması eskalasyon bakımını gerektirir. İVİG immün hemolizi azaltarak kan değişimi gereksinimini düşürebilir. Bilirubin eşiği aşar veya ensefalopati bulgusu gelişirse kan değişimi yapılır.",
                        "new_finding": "Yoğun fototerapi ve İVİG 0.5 g/kg verildi, kan değişimi için kan hazırlandı. Altıncı saatte bilirubin 17.1 mg/dL'ye geriledi ve kan değişimine gerek kalmadı. Bebek 72. saatte fototerapiden çıkarıldı; işitme taraması (ABR) planlandı."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y69",
        "category": "💊 Toksikoloji & Metabolik / Endokrin Aciller",
        "age": "14 Günlük",
        "gender": "Kız",
        "complaint": "Birkaç gündür artan kusma, emmeme, kilo kaybı ve bugün belirgin halsizlik-uyuşukluk",
        "history": "Ailesi anlatıyor: 'Miadında, 3200 gram doğdu. Doğumda dış genital bölgesinin biraz farklı göründüğünü söylediler, kontrole çağırdılar ama gidemedik. Son üç gündür her beslenmeden sonra kusuyor, emmiyor. Bugün çok uyuşuk, ağlaması zayıf.' Ateş ve ishal yok. Kusmuk safralı değil. Anne-baba akraba. Tartı: 2850 g (doğum ağırlığının %11 altı).",
        "final_diagnosis": "Tuz Kaybettiren Konjenital Adrenal Hiperplazi (21-Hidroksilaz Eksikliği) ve Adrenal Kriz",
        "disposition": "Sarı Alanda Sıvı Resüsitasyonu, İntravenöz Hidrokortizon ve Hiperkalemi Tedavisi ile Yenidoğan Yoğun Bakım ve Çocuk Endokrinoloji Yatışı",
        "case_pearl": "Yaşamın 1-3. haftasında kusma, dehidratasyon, hiponatremi, hiperkalemi ve hipoglisemi tuz kaybettiren 21-hidroksilaz eksikliğini düşündürür; kız bebekte virilize genitalya ipucudur, erkekte genital bulgu olmayabilir. Tanı için tedavi öncesi kortizol, 17-OH progesteron, ACTH ve renin örneği alınır ancak tedavi bekletilmez. Hidrokortizon 50-100 mg/m² intravenöz verilir; yüksek dozda mineralokortikoid etkisi de vardır. Pilor stenozunda ise hipokloremik hipokalemik alkaloz beklenir; hiperkalemi ayırıcı tanıda anahtardır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Stabilizasyon",
                "question": "Kusan, emmeyen ve uyuşuk bu 14 günlük bebekte ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Reflü olduğunu düşünüp beslenme miktarını azaltmalarını, mamayı koyulaştırmalarını önermek ve iki gün sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Evde bebek tepkisizleşti ve kardiyak arrest ile getirildi.",
                        "teaching_point": "Kilo kaybı ve letarjisi olan kusan yenidoğan asla reflü kabul edilip gönderilmez."
                    },
                    {
                        "text": "Uyuşukluk nedeniyle sepsis kabul edip ampisilin ve sefotaksim vermek, sıvı ve şeker değerlendirmesini kan ve idrar kültürü sonuçlarının sonrasına bırakmak",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik verildi ancak hipoglisemi ve elektrolit bozukluğu fark edilmedi; bebek nöbet geçirdi.",
                        "teaching_point": "Sepsis olasılığında da glukoz, perfüzyon ve elektrolitler aynı anda değerlendirilmelidir."
                    },
                    {
                        "text": "Kusma nedeniyle pilor darlığını düşünüp önce batın ultrasonu istemek ve sonuç gelene kadar ağızdan beslenmeyi kesmek",
                        "is_correct": False,
                        "scenario_update": "Ultrason sırasında bebek bradikardik oldu; şok ve elektrolit bozukluğu tedavisiz kaldı.",
                        "teaching_point": "Şoktaki yenidoğanda önce resüsitasyon yapılır; tanısal görüntüleme stabilizasyonu geciktirmemelidir."
                    },
                    {
                        "text": "Perfüzyon ve dehidratasyonu değerlendirmek, kapiller kan şekeri ölçmek, monitörize edip damar yolu açmak ve genital bölgeyi muayene etmek",
                        "is_correct": True,
                        "explanation": "Şok bulgusu ve hipoglisemi hemen tedavi edilmelidir. Monitör aritmiyi gösterir. Genital muayene etiyoloji için önemli bir ipucudur.",
                        "new_finding": "Vital Bulgular: Ateş 36.4°C, KTA 186/dk, SS 52/dk, SpO2 %97, TA 58/30 mmHg, KDZ 4 sn, ekstremiteler soğuk ve alacalı. Fontanel çökük, mukozalar kuru. Letarjik. Kapiller kan şekeri 48 mg/dL. Monitörde sivri T dalgaları. Klitoromegali ve labioskrotal füzyon (Prader evre 3), gonad ele gelmiyor. Meme başı ve genital bölgede hiperpigmentasyon."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar ve Acil Müdahale",
                "question": "Şoktaki, hipoglisemik ve monitörde sivri T dalgaları olan bu bebekte tetkik ve ilk müdahale nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Tüm tetkiklerin sonuçlarını bekleyip kesin tanı konunca sıvı ve hormon tedavisine başlamak, bu sürede ağızdan şekerli su verip yakından izlemek",
                        "is_correct": False,
                        "scenario_update": "Hormon sonuçları günler sürdü; bebek bu sürede kardiyak arrest geçirdi.",
                        "teaching_point": "Krizde örnek saklanır ve tedavi sonuç beklenmeden hemen başlanır."
                    },
                    {
                        "text": "Hiperkalemiyi düzeltmek için önce potasyum bağlayıcı reçine (sodyum polistiren sülfonat) rektal vermek ve etkisini beklemek",
                        "is_correct": False,
                        "scenario_update": "Reçinenin etkisi saatler aldı; bu sırada bebekte ventriküler aritmi gelişti.",
                        "teaching_point": "EKG değişikliği olan hiperkalemide önce kalsiyum ile miyokard korunur; reçine yenidoğanda nekrotizan enterokolit riski taşır."
                    },
                    {
                        "text": "Hiponatremiyi hızla düzeltmek için %3 NaCl ile sodyumu ilk 6 saatte 135 mEq/L'ye yükseltmek",
                        "is_correct": False,
                        "scenario_update": "Hızlı düzeltme sonrası bebekte nörolojik bozulma görüldü.",
                        "teaching_point": "Kronik hiponatremi 24 saatte 8-10 mEq/L'yi aşmayacak şekilde düzeltilir; hipertonik salin yalnızca nöbette küçük dozlarda verilir."
                    },
                    {
                        "text": "Tedavi öncesi kortizol, 17-OH progesteron ve renin için kan saklayıp elektrolit bakmak; 10 mL/kg SF bolusu ve %10 dekstroz vermek",
                        "is_correct": True,
                        "explanation": "Tedavi öncesi saklanan kan tanıyı tedaviyi geciktirmeden doğrulamayı sağlar. İzotonik sıvı hipovolemi ve hiponatremiyi, dekstroz hipoglisemiyi düzeltir. Yenidoğanda bolus 10 mL/kg ve yeniden değerlendirmeyle tekrarlanır.",
                        "new_finding": "Kan gazı: pH 7.21, HCO3 14 mEq/L. Na 116 mEq/L, K 7.6 mEq/L, Cl 88 mEq/L, glukoz 48 mg/dL, BUN 42 mg/dL. Tedavi öncesi kan saklandı (17-OH progesteron sonucu 1 hafta sonra 186 ng/mL geldi). İki bolus sonrası KDZ 3 sn, TA 66/38 mmHg; kan şekeri 92 mg/dL."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "İkinci haftada kusma, şok, Na 116, K 7.6 mEq/L, hipoglisemi, metabolik asidoz, virilize genitalya ve hiperpigmentasyonu olan bu kız bebekte tanı nedir?",
                "options": [
                    {
                        "text": "Psödohipoaldosteronizm tip 1",
                        "is_correct": False,
                        "scenario_update": "Genital virilizasyon ve hipoglisemi bu tabloyla açıklanmıyor.",
                        "teaching_point": "Psödohipoaldosteronizmde tuz kaybı vardır ancak kortizol eksikliği ve virilizasyon yoktur."
                    },
                    {
                        "text": "Tuz kaybettiren konjenital adrenal hiperplazi krizi",
                        "is_correct": True,
                        "explanation": "Hiponatremi, hiperkalemi, hipoglisemi, şok ile kız bebekte virilizasyon ve hiperpigmentasyon 21-hidroksilaz eksikliğine bağlı tuz kaybettiren krizi gösterir.",
                        "new_finding": "Tanı: Tuz Kaybettiren Konjenital Adrenal Hiperplazi (21-hidroksilaz eksikliği), adrenal kriz."
                    },
                    {
                        "text": "Geç başlangıçlı yenidoğan sepsisi",
                        "is_correct": False,
                        "scenario_update": "Ateş yok; elektrolit tablosu ve virilizasyon sepsisle açıklanmıyor.",
                        "teaching_point": "Sepsis hiponatremi yapabilir ancak belirgin hiperkalemi ve genital virilizasyonu açıklamaz."
                    },
                    {
                        "text": "Hipertrofik pilor stenozu",
                        "is_correct": False,
                        "scenario_update": "Hiperkalemi ve asidoz var; pilor darlığında hipokalemik alkaloz beklenir.",
                        "teaching_point": "Pilor stenozunda hipokloremik hipokalemik metabolik alkaloz görülür ve genital bulgu olmaz."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu bebeğin tedavisi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "İntravenöz hidrokortizon 50-100 mg/m² vermek; EKG değişikliği için kalsiyum glukonat yapmak, elektrolitleri sık izlemek",
                        "is_correct": True,
                        "explanation": "Yüksek doz hidrokortizon hem glukokortikoid hem mineralokortikoid etki sağlar. Kalsiyum glukonat miyokardı korur; sıvı ve kortizol potasyumu düşürür. Stabilizasyon sonrası idame hidrokortizon, fludrokortizon ve tuz başlanır; aileye stres dozu eğitimi verilir.",
                        "new_finding": "Hidrokortizon 25 mg intravenöz ve kalsiyum glukonat verildi. Sivri T dalgaları geriledi. 24 saatte Na 126, K 5.4 mEq/L oldu, kan şekeri stabil kaldı. Fludrokortizon ve tuz eklendi; karyotip 46,XX geldi."
                    },
                    {
                        "text": "Hiperkalemi için insülin ve dekstrozu tek tedavi olarak vermek, hormon tedavisini genetik test sonucuna göre planlamak",
                        "is_correct": False,
                        "scenario_update": "Potasyum geçici düştü ancak hormon eksikliği sürdüğü için yeniden yükseldi ve hipotansiyon tekrarladı.",
                        "teaching_point": "Altta yatan hormon eksikliği tedavi edilmeden elektrolit düzeltmeleri kalıcı olmaz."
                    },
                    {
                        "text": "Deksametazonu tek doz verip hidrokortizon yerine idame tedavisi olarak sürdürmek ve sıvıyı kısıtlamak",
                        "is_correct": False,
                        "scenario_update": "Deksametazon mineralokortikoid etki sağlamadı; tuz kaybı ve hiperkalemi sürdü.",
                        "teaching_point": "Deksametazonun mineralokortikoid etkisi yoktur ve yenidoğanda büyümeyi baskılar; tercih hidrokortizondur."
                    },
                    {
                        "text": "Yalnızca oral fludrokortizon ve tuz takviyesi başlamak, glukokortikoidi endokrinoloji polikliniği görüşüne bırakmak",
                        "is_correct": False,
                        "scenario_update": "Kortizol eksikliği tedavi edilmedi; bebekte yeniden hipoglisemi ve hipotansiyon gelişti.",
                        "teaching_point": "Krizde öncelik intravenöz hidrokortizondur; oral mineralokortikoid stabilizasyon sonrası eklenir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y70",
        "category": "💊 Toksikoloji & Metabolik / Endokrin Aciller",
        "age": "11 Yaşında",
        "gender": "Kız",
        "complaint": "Sabah uyanınca başlayan şiddetli baş ağrısı, bulantı-kusma, baş dönmesi ve banyoda kısa süreli bayılma",
        "history": "Ailesi anlatıyor: 'Kış tatilinde köydeki evimizdeyiz, odada sobayla ısınıyoruz, gece kapıyı pencereyi kapattık. Sabah kalkınca başı çok ağrıdı, kustu, banyoda birkaç saniye bayıldı. Bizim de başımız ağrıyor, küçük oğlum da kustu.' Ateş yok. Travma olmamış, düşerken başını çarpmamış. Kronik hastalığı yok. Tartı: 36 kg.",
        "final_diagnosis": "Soba Kaynaklı Karbonmonoksit Zehirlenmesi (Senkop ile, Ağır)",
        "disposition": "Sarı Alanda Geri Solumasız Maske ile %100 Oksijen, Hiperbarik Oksijen Merkezi ile Görüşme ve Aile Bireylerinin Birlikte Değerlendirilmesi",
        "case_pearl": "Kışın soba, şofben veya mangal kullanılan kapalı ortamda aynı evde birden fazla kişinin baş ağrısı, bulantı ve baş dönmesi karbonmonoksit zehirlenmesini düşündürür. Standart nabız oksimetresi karboksihemoglobini oksihemoglobinden ayıramaz ve satürasyon yanıltıcı biçimde normal görünür. Tanı kooksimetreli kan gazıyla konur. Tedavi hemen %100 oksijendir (yarı ömrü ~5 saatten ~75 dakikaya iner). Bilinç kaybı-senkop, nörolojik bulgu, miyokard iskemisi, gebelik veya karboksihemoglobin >%25 hiperbarik oksijen için değerlendirme gerektirir. Gecikmiş nörolojik sekel açısından izlem önerilir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Oksijenizasyon",
                "question": "Sobalı kapalı odada uyuduktan sonra baş ağrısı, kusma ve bayılma ile gelen bu 11 yaşındaki kızda ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Satürasyondan bağımsız olarak geri solumasız maskeyle %100 oksijen başlamak; bilinç, nörolojik muayene ve kardiyak ritmi değerlendirmek",
                        "is_correct": True,
                        "explanation": "Kapalı ortamda yanma ürünlerine maruziyet şüphesinde oksijen hemen başlanır. Nörolojik bulgu, senkop ve miyokard tutulumu ağırlığı belirler. Monitörizasyon iskemi ve aritmiyi yakalar.",
                        "new_finding": "Vital Bulgular: Ateş 36.7°C, KTA 118/dk, SS 24/dk, nabız oksimetresi SpO2 %99, TA 112/70 mmHg. GKS 15, hafif konfüzyon dışında nörolojik muayene normal, fokal defisit yok. Deri rengi normal. Monitörde sinüs taşikardisi. %100 oksijen başlandı."
                    },
                    {
                        "text": "Nabız oksimetresi %99 gösterdiği için oksijen gereksinimi olmadığını kabul edip baş ağrısı için intravenöz parasetamol vermek",
                        "is_correct": False,
                        "scenario_update": "Oksijen verilmeyen çocukta baş ağrısı arttı ve bilinç bulanıklığı gelişti.",
                        "teaching_point": "Bu tabloda standart oksimetri yanıltıcı biçimde normal görünebilir; satürasyona güvenilmez."
                    },
                    {
                        "text": "Bayılma nedeniyle önce kafa travmasını dışlamak için beyin tomografisi çekmek ve oksijeni tomografi sonrasına bırakmak",
                        "is_correct": False,
                        "scenario_update": "Tomografi normal geldi; oksijen tedavisi bir saat gecikti.",
                        "teaching_point": "Travma öyküsü olmayan çocukta görüntüleme oksijen tedavisini geciktirmemelidir."
                    },
                    {
                        "text": "Bayılmayı vazovagal senkop kabul edip çocuğu sırtüstü yatırmak, sıvı vermek ve ailenin geri kalanını değerlendirmeden taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Aile aynı eve döndü; gece kardeşi bilinç kaybıyla getirildi.",
                        "teaching_point": "Aynı ortamdaki birden fazla kişide benzer yakınma ortak bir çevresel nedeni düşündürür."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar ve Kardiyak Değerlendirme",
                "question": "Oksijen başlanan bu çocukta hangi tetkikler istenmelidir?",
                "options": [
                    {
                        "text": "Baş ağrısı ve kusma nedeniyle lomber ponksiyon yapmak ve beyin omurilik sıvısında hücre ve protein bakmak",
                        "is_correct": False,
                        "scenario_update": "Lomber ponksiyon normal geldi; asıl tanıyı koyduracak kan gazı istenmedi.",
                        "teaching_point": "Ateşsiz ve ortak maruziyet öyküsü olan çocukta önce toksik neden araştırılmalıdır."
                    },
                    {
                        "text": "Kan gazında kooksimetriyle hemoglobin türlerini ölçmek; laktat, elektrolit, troponin ve 12 derivasyonlu EKG istemek",
                        "is_correct": True,
                        "explanation": "Kooksimetri tanıyı koyar; venöz örnek yeterlidir. Laktat ve asidoz doku hipoksisini, troponin ve EKG miyokard hasarını gösterir. Kapalı yangın ortamında siyanür zehirlenmesi de düşünülmelidir.",
                        "new_finding": "Venöz kan gazı kooksimetri: COHb %28.4, pH 7.32, HCO3 19 mEq/L, laktat 3.4 mmol/L. Troponin I 0.02 ng/mL (normal), kreatin kinaz normal. EKG sinüs taşikardisi, iskemik değişiklik yok. Gebelik testi negatif."
                    },
                    {
                        "text": "Yalnızca parmak ucu nabız oksimetresiyle izlemek, değer %95'in üzerinde kaldıkça ek tetkik istememek",
                        "is_correct": False,
                        "scenario_update": "Satürasyon sürekli normal göründü; zehirlenmenin derecesi belirlenemedi.",
                        "teaching_point": "Standart nabız oksimetresi bu tabloda zehirlenmenin derecesini göstermez."
                    },
                    {
                        "text": "Arteriyel kan gazında yalnızca parsiyel oksijen basıncına bakmak, değer normalse zehirlenmeyi dışlamak",
                        "is_correct": False,
                        "scenario_update": "PaO2 normal geldi ve tanı dışlandı; çocuk eve gönderilmek üzereydi.",
                        "teaching_point": "PaO2 çözünmüş oksijeni gösterir ve bu zehirlenmede normal olabilir; kooksimetri gerekir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Sobalı kapalı odada uyuduktan sonra baş ağrısı, kusma, senkop gelişen, aile bireyleri de etkilenen, SpO2'si normal ancak kooksimetride karboksihemoglobini %28.4 olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Migren atağı (auralı)",
                        "is_correct": False,
                        "scenario_update": "Ailenin diğer bireyleri de etkilenmiş ve kan gazında belirgin anormallik var.",
                        "teaching_point": "Migren aile bireylerinde aynı anda başlamaz ve laboratuvar anormalliği yapmaz."
                    },
                    {
                        "text": "Karbonmonoksit zehirlenmesi",
                        "is_correct": True,
                        "explanation": "Kapalı ortamda soba kullanımı, ailede ortak yakınmalar ve karboksihemoglobin %28.4 karbonmonoksit zehirlenmesini doğrular; senkop ağır zehirlenmeyi gösterir.",
                        "new_finding": "Tanı: Soba Kaynaklı Karbonmonoksit Zehirlenmesi (senkop ile, ağır)."
                    },
                    {
                        "text": "Siyanür zehirlenmesi",
                        "is_correct": False,
                        "scenario_update": "Yangın veya duman maruziyeti yok; laktat yalnızca hafif yüksek.",
                        "teaching_point": "Siyanür zehirlenmesi genellikle kapalı alan yangınlarında, belirgin laktik asidozla görülür."
                    },
                    {
                        "text": "Viral gastroenterit",
                        "is_correct": False,
                        "scenario_update": "İshal ve ateş yok; kooksimetride belirgin anormallik var.",
                        "teaching_point": "Ailede eş zamanlı kusma, baş ağrısı ve kapalı ortam öyküsü toksik maruziyeti düşündürür."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yönlendirme",
                "question": "Bu çocuğun tedavi ve izlem planı hangisidir?",
                "options": [
                    {
                        "text": "%100 oksijeni sürdürüp hiperbarik oksijen merkezine danışmak; tüm aileyi değerlendirip kaynak giderilmeden eve dönülmemesini sağlamak",
                        "is_correct": True,
                        "explanation": "Senkop ve karboksihemoglobin >%25 hiperbarik oksijen için değerlendirme ölçütleridir; amaç gecikmiş nörolojik sekel riskini azaltmaktır. Aynı ortamdaki herkes kooksimetriyle taranmalıdır. Soba ve baca kontrolü ile ev dedektörü önerilir.",
                        "new_finding": "Hiperbarik merkezle görüşüldü ve bir seans hiperbarik oksijen uygulandı. Dördüncü saatte karboksihemoglobin %3'e indi, baş ağrısı geçti. Diğer aile bireyleri de tedavi aldı. Bir ay sonra nörolojik kontrol planlandı."
                    },
                    {
                        "text": "Belirtiler azaldığı için oksijeni kesip çocuğu ailesiyle birlikte aynı eve göndermek ve sobayı daha az yakmalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Aile aynı ortama döndü; ertesi gece yeniden zehirlenme gelişti.",
                        "teaching_point": "Kaynak giderilmeden ortama dönüş yinelemeye yol açar; aile bilgilendirilmelidir."
                    },
                    {
                        "text": "Oksijeni nazal kanülle 2 L/dk'ya düşürmek ve karboksihemoglobin normale inene kadar çocuğu serviste yatırarak izlemek",
                        "is_correct": False,
                        "scenario_update": "Düşük akımlı oksijenle karboksihemoglobin yavaş geriledi; baş ağrısı uzun sürdü.",
                        "teaching_point": "Eliminasyonu hızlandırmak için en yüksek oksijen konsantrasyonu kullanılmalıdır."
                    },
                    {
                        "text": "Zehirlenmeyi bağlamak için intravenöz hidroksokobalamin ve sodyum tiyosülfat vermek, oksijeni kesmek",
                        "is_correct": False,
                        "scenario_update": "Bu antidotlar bu tablonun tedavisi değildi; oksijen kesilince belirtiler arttı.",
                        "teaching_point": "Hidroksokobalamin siyanür zehirlenmesinin antidotudur; bu tablonun tedavisi oksijendir."
                    }
                ]
            }
        ]
    }
]
