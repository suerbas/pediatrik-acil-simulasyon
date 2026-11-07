# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - Y61-Y65 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "Y61",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "4 Yaşında",
        "gender": "Erkek",
        "complaint": "Bu sabah aniden başlayan sağ bacağa basamama ve topallama",
        "history": "Babası anlatıyor: 'Bir hafta önce hafif burun akıntısı ve öksürüğü olmuştu, ilaçsız geçti. Bu sabah uyanınca sağ bacağının üstüne basınca acıdığını söyleyip ağladı, topallayarak yürüyor. Ateşi hiç çıkmadı. Düşme ya da çarpma olmadı. İştahı ve neşesi yerinde.' Bilinen hastalığı yok. Tartı: 17 kg.",
        "final_diagnosis": "Geçici (Toksik) Sinovit",
        "disposition": "Yeşil Alandan Oral NSAİİ, Kısa Süreli İstirahat, Alarm Bulguları Eğitimi ve 48-72 Saat Sonra Kontrol ile Taburculuk",
        "case_pearl": "3-8 yaş erkek çocukta viral enfeksiyon sonrası ani başlayan, ateşsiz, iyi görünümlü topallama geçici sinovitin tipik tablosudur. Asıl hedef septik artriti kaçırmamaktır: Kocher kriterleri (ateş >38.5°C, basamama, ESH >40 mm/sa, lökosit >12.000/mm³) ve CRP >2 mg/dL riski artırır. Ultrasonda efüzyon iki durumda da görülebilir; ayrım klinik ve laboratuvarla yapılır. Tedavi NSAİİ ve istirahattir; yakınmalar genellikle 1-2 haftada geçer.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Ateşsiz, travmasız, aniden topallamaya başlayan bu 4 yaşındaki çocukta muayenede neyi değerlendirirsiniz?",
                "options": [
                    {
                        "text": "Ateşi ve genel görünümü, yürüyüşü, kalça iç rotasyon-abdüksiyonunu, diğer eklemleri, omurga, karın, testis ve cildi sistematik olarak değerlendirmek",
                        "is_correct": True,
                        "explanation": "Çocukta topallamanın kaynağı kalça dışında diz, omurga, karın veya testis olabilir. Ateş, toksik görünüm ve hareket kısıtlılığının derecesi septik artriti diğer nedenlerden ayırmada ilk ipuçlarıdır.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 94/dk, SS 20/dk, SpO2 %99. Masada otururken neşeli, oyuncakla oynuyor. Sağ bacağa kısmen basarak antaljik yürüyüş. Sağ kalçada iç rotasyon ve abdüksiyonun son derecelerinde hafif ağrı; pasif hareket büyük ölçüde serbest. Isı artışı, kızarıklık, şişlik yok. Diz, ayak bileği, omurga, karın ve testis muayenesi normal. Peteşi veya döküntü yok."
                    },
                    {
                        "text": "Bacağını kullanmak istemediği için çocuğu tekerlekli sandalyeye alıp ortopedi konsültasyonu istemek, sistemik muayeneyi ortopedi değerlendirmesinden sonraya bırakmak",
                        "is_correct": False,
                        "scenario_update": "Ortopedi ekibi iki saat sonra geldi; bu sürede ateş, diğer eklemler ve karın değerlendirilmemişti.",
                        "teaching_point": "Topallayan çocuğun ilk değerlendirmesi acil hekiminin sorumluluğundadır; konsültasyon sistematik muayeneden sonra gerekirse istenir."
                    },
                    {
                        "text": "Topallamanın kaynağının kalça olduğunu kabul edip yalnızca kalça eklemini muayene etmek ve ağrı kontrolü için hemen intramüsküler diklofenak uygulamak",
                        "is_correct": False,
                        "scenario_update": "Enjeksiyon sonrası çocuk ağlayarak muayeneye direnç gösterdi; diz, omurga ve karın muayenesi yapılmadan zaman geçti.",
                        "teaching_point": "Küçük çocuk ağrının yerini doğru tarif edemez; topallamada tüm alt ekstremite, omurga, karın ve genital bölge muayene edilmelidir."
                    },
                    {
                        "text": "Çocuğun travma öyküsünü saklıyor olabileceğini düşünüp istismar şüphesiyle sosyal hizmet bildirimi yapmak ve kemik taraması planlamak",
                        "is_correct": False,
                        "scenario_update": "Ciltte morluk, kırık bulgusu veya öyküde tutarsızlık yoktu; aile yersiz şüpheden incindi ve muayene ertelendi.",
                        "teaching_point": "İstismar şüphesi tutarsız öykü, uygunsuz yaralanma bulguları veya gecikmiş başvuru gibi somut ipuçlarına dayanmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Stratejisi",
                "question": "Ateşsiz, iyi görünümlü ve kalça hareketleri hafif ağrılı bu çocukta hangi tetkik yaklaşımı uygundur?",
                "options": [
                    {
                        "text": "Kalça patolojilerini en iyi gösteren yöntem olduğu için sedasyon altında kontrastlı kalça manyetik rezonans görüntülemesi planlamak",
                        "is_correct": False,
                        "scenario_update": "MR için sedasyon ve saatlerce bekleme gerekti; temel laboratuvar tetkikleri istenmemişti.",
                        "teaching_point": "MR, atipik seyir veya osteomiyelit şüphesinde değerlidir; ilk basamak tetkik değildir."
                    },
                    {
                        "text": "Yalnızca ön-arka pelvis grafisi çekmek, kırık ve kemik lezyonu görülmezse laboratuvar istemeden taburcu edip bir hafta sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Grafi normal geldi; inflamatuvar belirteçler bakılmadan taburcu edilmek üzereydi ve septik artrit dışlanmamıştı.",
                        "teaching_point": "Normal grafi eklem enfeksiyonunu dışlamaz; basamayan çocukta laboratuvar ve ultrason değerlendirmesi gerekir."
                    },
                    {
                        "text": "Ortopedi ile birlikte acil kalça eklem aspirasyonu yapmak, sinovyal sıvıyı hücre sayımı ve kültür için gönderip sonuç gelene kadar intravenöz antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "Sedasyonla aspirasyon yapıldı; az miktarda berrak sıvıda düşük hücre sayısı saptandı. Çocuk gereksiz yere invaziv işlem ve antibiyotiğe maruz kaldı.",
                        "teaching_point": "Eklem aspirasyonu ateş, basamama ve yüksek inflamatuvar belirteçlerle septik artrit riski arttığında endikedir."
                    },
                    {
                        "text": "Tam kan sayımı, CRP ve sedimantasyon istemek, bilateral kalça ultrasonografisiyle efüzyonu değerlendirmek ve sonuçları septik artrit risk kriterleriyle yorumlamak",
                        "is_correct": True,
                        "explanation": "Lökosit, ESH ve CRP Kocher ve CRP kriterlerinin bileşenleridir. Ultrason efüzyonu gösterir ancak septik artriti ayırmaz; karar klinik ve laboratuvar birlikte değerlendirilerek verilir.",
                        "new_finding": "Lökosit 7.800/mm³, CRP 0.2 mg/dL, ESH 12 mm/sa. Kalça ultrasonu: sağda 4 mm anekoik efüzyon, sinovyal kalınlaşma yok; sol kalça normal. Kocher kriterlerinin hiçbiri yok."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Viral enfeksiyon sonrası ateşsiz topallama, normal inflamatuvar belirteçler ve kalçada az miktarda efüzyonu olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Septik artrit",
                        "is_correct": False,
                        "scenario_update": "Ateş yok, lökosit, CRP ve ESH normal, çocuk kısmen basabiliyor.",
                        "teaching_point": "Septik artritte ateş, şiddetli ağrı, basamama ve yüksek inflamatuvar belirteçler beklenir."
                    },
                    {
                        "text": "Juvenil idiyopatik artrit",
                        "is_correct": False,
                        "scenario_update": "Sabah tutukluğu ve 6 haftayı aşan eklem şişliği öyküsü yok.",
                        "teaching_point": "Juvenil idiyopatik artrit tanısı için en az 6 hafta süren artrit gerekir."
                    },
                    {
                        "text": "Geçici (toksik) sinovit",
                        "is_correct": True,
                        "explanation": "İyi görünüm, ateşsizlik, normal lökosit-CRP-ESH ve küçük efüzyon geçici sinovitle uyumludur; Kocher kriterlerinin hiçbirinin olmaması septik artrit olasılığını çok düşük kılar.",
                        "new_finding": "Tanı: Geçici (Toksik) Sinovit."
                    },
                    {
                        "text": "Legg-Calvé-Perthes hastalığı",
                        "is_correct": False,
                        "scenario_update": "Yakınma aniden ve viral enfeksiyon sonrası başladı; haftalar süren sinsi topallama öyküsü yok.",
                        "teaching_point": "Perthes hastalığı sinsi başlangıçlıdır; topallama 2 haftayı aşarsa grafi tekrarlanmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuğun tedavi ve izlem planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Sinovyal inflamasyonu hızla baskılamak için üç gün oral prednizolon vermek ve iki hafta sonra kalça manyetik rezonansı ile kontrol etmek",
                        "is_correct": False,
                        "scenario_update": "Steroid sonrası iştah artışı ve uyku bozukluğu gelişti; kontrol MR'ı gereksizdi.",
                        "teaching_point": "Geçici sinovitte sistemik steroid ve rutin ileri görüntüleme önerilmez."
                    },
                    {
                        "text": "Çocuğu servise yatırıp cilt traksiyonu uygulamak, intravenöz sıvı başlamak ve günlük CRP ile ultrason kontrolü yaparak efüzyon kaybolana kadar izlemek",
                        "is_correct": False,
                        "scenario_update": "Yatışın üçüncü gününde çocuk iyileşmişti; traksiyon ve tekrarlanan tetkikler sonucu değiştirmedi.",
                        "teaching_point": "Geçici sinovitte traksiyon ve yatış gerekmez; seri ultrason efüzyonun takibinde kullanılmaz."
                    },
                    {
                        "text": "Ibuprofen 10 mg/kg 8 saatte bir, kısa süreli istirahat, ateş veya basamama gelişirse hemen başvuru eğitimi ve 48-72 saat sonra kontrol",
                        "is_correct": True,
                        "explanation": "NSAİİ ağrı ve sinovyal inflamasyonu azaltır ve iyileşmeyi hızlandırır. Ateş, kötüleşen ağrı veya basamama septik artrit olasılığını yeniden gündeme getirir; bu nedenle kısa süreli kontrol önemlidir.",
                        "new_finding": "İbuprofen başlandı, alarm bulguları anlatıldı. 72. saat kontrolünde çocuk topallamadan koşuyordu; kalça hareketleri ağrısızdı."
                    },
                    {
                        "text": "Olası erken bakteriyel enfeksiyonu önlemek için 10 gün oral sefaleksin başlamak ve topallama tamamen geçene kadar çocuğun yürümesini yasaklamak",
                        "is_correct": False,
                        "scenario_update": "Gereksiz antibiyotik sonrası çocukta ishal gelişti; yürüme yasağı ailenin günlük yaşamını zorlaştırdı.",
                        "teaching_point": "Bu tabloda antibiyotik endikasyonu yoktur; çocuk tolere ettiği ölçüde hareket edebilir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y62",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "9 Yaşında",
        "gender": "Kız",
        "complaint": "Dört saattir süren şiddetli, zonklayıcı baş ağrısı, bulantı, ışık ve sesten rahatsızlık",
        "history": "Annesi anlatıyor: 'Öğleden sonra okulda başının sağ tarafında zonklayıcı, çok şiddetli bir ağrı başladı. Eve gelince iki kez kustu. Işık ve ses ağrısını artırıyor, karanlık odaya kapanmak istiyor. Son bir yılda ayda bir-iki kez benzer, daha hafif ağrıları oldu, uyuyunca geçiyordu. Bende de gençliğimden beri böyle baş ağrıları var.' Ateş, travma, sabah kusması veya uykudan uyandıran baş ağrısı yok. Tartı: 30 kg.",
        "final_diagnosis": "Aurasız Migren Atağı",
        "disposition": "Yeşil Alanda Erken Analjezi, Antiemetik ve Karanlık-Sessiz Ortamda Dinlendirme Sonrası Baş Ağrısı Günlüğü Eğitimi ile Taburculuk",
        "case_pearl": "Çocuklarda migren erişkinden daha kısa (2-72 saat) ve sıklıkla bilateral olabilir; bulantı-kusma, fotofobi-fonofobi ve aile öyküsü tanıyı destekler. Normal nörolojik ve fundoskopik muayenede, kırmızı bayrak yoksa görüntüleme gerekmez. Akut tedavide ilk seçenek erken alınan ibuprofen 10 mg/kg'dır; yanıt yoksa intravenöz sıvı ve dopamin antagonisti eklenir. Opioidlerden kaçınılır; ayda 10-15 günden fazla analjezik kullanımı ilaç aşırı kullanım baş ağrısına yol açar.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Şiddetli baş ağrısı ve kusması olan bu 9 yaşındaki kızda değerlendirmenin odağı nedir?",
                "options": [
                    {
                        "text": "Ailede benzer baş ağrısı olduğu için tanıyı öyküye dayanarak koymak, muayeneyi vital bulgularla sınırlı tutup oral analjezik vererek taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Fundoskopi ve nörolojik muayene yapılmadan taburcu edildi; kırmızı bayraklar dışlanmadığı için aile ertesi gün başka bir merkeze başvurdu.",
                        "teaching_point": "Aile öyküsü destekleyicidir ancak sekonder nedenleri dışlamak için ayrıntılı muayene şarttır."
                    },
                    {
                        "text": "Kan basıncı, ateş ve bilinç düzeyini değerlendirmek; fundoskopi, meninks irritasyon bulguları, kraniyal sinirler, motor-duyu ve serebellar muayeneyi yapmak",
                        "is_correct": True,
                        "explanation": "Baş ağrılı çocukta sekonder nedenler (menenjit, kafa içi basınç artışı, hipertansiyon, kitle) ancak sistematik nörolojik muayene ve fundoskopiyle dışlanabilir. Normal muayene görüntüleme ihtiyacını belirleyen en önemli unsurdur.",
                        "new_finding": "Vital Bulgular: Ateş 36.6°C, KTA 82/dk, SS 18/dk, SpO2 %99, TA 102/64 mmHg. Işıktan gözlerini kısıyor. Bilinç açık, oryante. Ense sertliği, Kernig ve Brudzinski negatif. Kraniyal sinirler, motor-duyu muayenesi ve serebellar testler normal. Fundoskopide optik disk sınırları keskin, venöz pulsasyon var."
                    },
                    {
                        "text": "Kusma ve tek taraflı ağrı nedeniyle kafa içi kanama düşünüp çocuğu sedyede yatırmak ve muayene etmeden acil beyin tomografisi istemek",
                        "is_correct": False,
                        "scenario_update": "Tomografi için sıra beklenirken muayene yapılmadı; nörolojik muayene sonradan tamamen normal bulundu.",
                        "teaching_point": "Görüntüleme kararı öykü ve muayene bulgularına göre verilir; muayeneden önce rutin tomografi istenmez."
                    },
                    {
                        "text": "Çocuğun ağrısını hızla azaltmak için muayeneden önce intravenöz tramadol uygulamak ve rahatladıktan sonra kısa bir nörolojik değerlendirme yapmak",
                        "is_correct": False,
                        "scenario_update": "Tramadol sonrası bulantısı arttı ve uykuya daldı; nörolojik muayene güvenilir yapılamadı.",
                        "teaching_point": "Opioidler çocukta baş ağrısı tedavisinde önerilmez; ayrıca muayeneyi maskeleyebilir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Nörolojik ve fundoskopik muayenesi normal olan bu çocukta tetkik yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Ataklar arasında tamamen iyi olduğu için epileptik bir süreci dışlamak amacıyla acil elektroensefalografi istemek ve sonucu nöroloji ile değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "EEG acil koşullarda yapılamadı; randevu haftalar sonrasına verildi ve tanıya katkısı olmadı.",
                        "teaching_point": "EEG baş ağrısının rutin değerlendirmesinde yer almaz; bilinç kaybı veya nöbet şüphesinde düşünülür."
                    },
                    {
                        "text": "Menenjit olasılığını dışlamak için tam kan sayımı ve CRP istemek, yüksek çıkarsa lomber ponksiyon yapmak üzere hazırlık yapmak",
                        "is_correct": False,
                        "scenario_update": "Lökosit ve CRP normal geldi; ateş ve meninks bulgusu olmadığı halde çocuk kan alımı sırasında daha da kötüleşti.",
                        "teaching_point": "Ateşsiz, meninks irritasyon bulgusu olmayan çocukta menenjit için kan tetkiki ve lomber ponksiyon endike değildir."
                    },
                    {
                        "text": "Kırmızı bayrakları (ani gök gürültüsü ağrı, uykudan uyandırma, sabah kusması, nörolojik bulgu, kişilik değişikliği) aileyle gözden geçirip görüntüleme istememek",
                        "is_correct": True,
                        "explanation": "Kırmızı bayrak olmayan, tekrarlayan benzer atakları ve normal muayenesi olan çocukta tanı kliniktir. Görüntüleme ve laboratuvar yönetimi değiştirmez; aileye hangi durumda yeniden değerlendirme gerektiği anlatılır.",
                        "new_finding": "Kırmızı bayrak saptanmadı. Ataklar son bir yılda benzer nitelikte, aralarda çocuk tamamen iyi. Tetkik istenmedi."
                    },
                    {
                        "text": "Kusmayla seyreden ilk şiddetli atak olduğu için kontrastsız beyin tomografisi çekmek ve normalse aileyi rahatlatarak taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Tomografi normal geldi; çocuk gereksiz radyasyona maruz kaldı ve ağrısı tedavi edilmeden bir saat geçti.",
                        "teaching_point": "Tekrarlayan benzer ataklar, aile öyküsü ve normal muayenede görüntüleme tanıya katkı sağlamaz."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Tekrarlayan, zonklayıcı, bulantı-kusma ve ışık-ses hassasiyetiyle seyreden, aile öyküsü olan ve muayenesi normal bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Gerilim tipi baş ağrısı",
                        "is_correct": False,
                        "scenario_update": "Ağrı zonklayıcı, şiddetli ve kusmayla birlikte; gerilim tipi baş ağrısında bunlar beklenmez.",
                        "teaching_point": "Gerilim tipi baş ağrısı bası tarzında, hafif-orta şiddette ve bulantısızdır."
                    },
                    {
                        "text": "Akut bakteriyel rinosinüzit",
                        "is_correct": False,
                        "scenario_update": "Burun akıntısı, ateş veya yüz ağrısı yok; ağrı epizodik.",
                        "teaching_point": "Sinüzit tekrarlayan epizodik baş ağrısının nadir nedenidir."
                    },
                    {
                        "text": "Aurasız migren atağı",
                        "is_correct": True,
                        "explanation": "Tekrarlayan, orta-şiddetli, zonklayıcı ağrı; bulantı-kusma ve fotofobi-fonofobi ile birlikte normal muayene ve aile öyküsü ICHD-3 aurasız migren kriterlerini karşılar.",
                        "new_finding": "Tanı: Aurasız Migren Atağı."
                    },
                    {
                        "text": "İdiyopatik intrakraniyal hipertansiyon",
                        "is_correct": False,
                        "scenario_update": "Papilödem ve görme yakınması yok, ataklar arasında çocuk tamamen iyi.",
                        "teaching_point": "İdiyopatik intrakraniyal hipertansiyonda sürekli baş ağrısı ve papilödem beklenir."
                    }
                ]
            },
            {
                "stage_title": "Akut Tedavi ve Taburculuk Planı",
                "question": "Bu çocuğun acil serviste akut tedavisi ve taburculuk önerileri nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Oral ibuprofen 10 mg/kg ve ondansetron verip karanlık-sessiz odada dinlendirmek; atak başında erken ilaç alımını, uyku düzenini ve baş ağrısı günlüğünü anlatmak",
                        "is_correct": True,
                        "explanation": "Atağın erken döneminde alınan ibuprofen çocuk migreninde en kanıtlı ilk basamaktır; antiemetik bulantıyı giderir. Günlük, tetikleyicileri ve sıklığı izlemeye yardım eder; analjezikleri ayda 10-15 günden fazla kullanmamak ilaç aşırı kullanım baş ağrısını önler.",
                        "new_finding": "İbuprofen ve ondansetron sonrası karanlık odada bir saat uyudu; uyandığında ağrısı ve bulantısı geçmişti. Aileye günlük ve analjezik kullanım sınırları anlatıldı."
                    },
                    {
                        "text": "Atağı sonlandırmak için intravenöz deksametazon uygulamak ve tekrarları önlemek amacıyla acil serviste günlük topiramat proflaksisi başlatıp bir ay sonra kontrol önermek",
                        "is_correct": False,
                        "scenario_update": "Steroid ilk basamak tedavi değildi; ayda bir-iki atağı olan çocukta proflaksi endikasyonu yoktu ve ilaç yan etki riski taşıyordu.",
                        "teaching_point": "Proflaksi sık ve yeti yitimine yol açan ataklarda, poliklinik değerlendirmesiyle planlanır."
                    },
                    {
                        "text": "Ağrının şiddeti nedeniyle oral kodeinli parasetamol reçete etmek ve ataklar sırasında günde üç kez, en az beş gün düzenli kullanmasını önermek",
                        "is_correct": False,
                        "scenario_update": "Kodein 12 yaş altında solunum depresyonu riski nedeniyle kontrendikedir; düzenli kullanım önerisi ilaç aşırı kullanımına zemin hazırlar.",
                        "teaching_point": "Kodein ve diğer opioidler çocuklarda baş ağrısı tedavisinde kullanılmamalıdır."
                    },
                    {
                        "text": "Analjeziği yalnızca ağrı en şiddetli düzeye ulaştığında vermek, çocuğun okul ve ekran kullanımını tamamen yasaklayıp bir ay ev istirahati önermek",
                        "is_correct": False,
                        "scenario_update": "Geç alınan ilaç etkisiz kaldı; okuldan uzaklaştırma çocuğun kaygısını artırdı.",
                        "teaching_point": "Analjezik atak başında alınmalıdır; okula devam ve düzenli yaşam desteklenir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y63",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "6 Yaşında",
        "gender": "Kız",
        "complaint": "İki gündür idrar yaparken yanma, sık idrara çıkma ve altını ıslatma",
        "history": "Annesi anlatıyor: 'İki gündür çiş yaparken yandığını söyleyip ağlıyor. Günde on beş kez tuvalete koşuyor ama birkaç damla yapıyor. Dün okulda iki kez altına kaçırdı. Ateşi olmadı, böğrü ağrımıyor, kusmadı.' Ayrıntılı sorgulamada üç-dört günde bir, sert dışkı yaptığı ve okulda tuvalete gitmekten kaçındığı öğrenildi. Daha önce benzer yakınması olmamış. Tartı: 20 kg.",
        "final_diagnosis": "Akut Sistit (Ateşsiz İdrar Yolu Enfeksiyonu), Eşlik Eden Mesane-Bağırsak Disfonksiyonu",
        "disposition": "Yeşil Alandan Kültür Sonrası Kısa Süreli Oral Antibiyotik, Kabızlık Tedavisi ve Tuvalet Alışkanlığı Eğitimi ile Taburculuk",
        "case_pearl": "Okul çağındaki kız çocukta ateşsiz dizüri, sık idrara çıkma ve suprapubik hassasiyet alt üriner sistem enfeksiyonunu düşündürür. Tanı orta akım temiz idrarda piyüri ile birlikte anlamlı üremeyle konur; idrar torbası kültür için uygun değildir. Ateşsiz enfeksiyonda 3-5 günlük oral tedavi yeterlidir ve ilk atakta rutin görüntüleme gerekmez. Kabızlık ve işeme ertelemesi (mesane-bağırsak disfonksiyonu) tekrarların en sık değiştirilebilir nedenidir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Ateşsiz idrar yakınmaları olan bu 6 yaşındaki kızda muayenede neye dikkat edersiniz?",
                "options": [
                    {
                        "text": "Ateş ve kostovertebral açı hassasiyetine bakmak, suprapubik bölgeyi ve dış genitali vulvovajinit ve yapışıklık açısından incelemek, lumbosakral omurga ve kabızlığı değerlendirmek",
                        "is_correct": True,
                        "explanation": "Ateş ve böğür hassasiyeti üst üriner sistem tutulumunu düşündürür. Genital muayene vulvovajinit, labial yapışıklık ve kıl kurdu gibi taklitçileri ayırır. Lumbosakral anomali ve kabızlık işeme bozukluğuna katkıda bulunur.",
                        "new_finding": "Vital Bulgular: Ateş 36.7°C, KTA 86/dk, SS 18/dk, TA 98/62 mmHg. Genel durumu iyi. Suprapubik hafif hassasiyet; kostovertebral açı hassasiyeti yok. Sol alt kadranda dışkı kitlesi palpe ediliyor. Dış genital normal, vulvit, akıntı veya yapışıklık yok. Lumbosakral bölgede gamze veya kıl tutamı yok."
                    },
                    {
                        "text": "Altını ıslatma yakınması nedeniyle psikolojik bir sorun olabileceğini düşünüp okul stresini sorgulamak ve çocuk psikiyatrisine yönlendirme yapmak",
                        "is_correct": False,
                        "scenario_update": "Fizik muayene ve idrar değerlendirmesi yapılmadan yönlendirme yapıldı; dizüri sürdü.",
                        "teaching_point": "Yeni başlayan gündüz ıslatması öncelikle organik nedenlerle değerlendirilmelidir."
                    },
                    {
                        "text": "Havuz ve banyo öyküsünü sorgulayıp vulvovajinit kabul etmek, oturma banyosu önermek ve idrar tetkiki yapmadan semptomlar sürerse kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Genital muayene yapılmadan vulvovajinit kabul edildi; idrar tetkiki yapılmadığı için olası enfeksiyon tedavisiz kaldı.",
                        "teaching_point": "Dizüri ve sık idrara çıkma idrar tetkikiyle değerlendirilmeli; vulvovajinit tanısı muayeneyle konmalıdır."
                    },
                    {
                        "text": "Muayeneyi yalnızca karın palpasyonuyla sınırlı tutup ampirik oral antibiyotik reçete etmek ve idrar örneğini tedaviden üç gün sonra kontrol amaçlı istemek",
                        "is_correct": False,
                        "scenario_update": "Kültür alınmadan başlanan antibiyotik nedeniyle tanı doğrulanamadı ve direnç durumu öğrenilemedi.",
                        "teaching_point": "Antibiyotik öncesi uygun yöntemle alınmış idrar kültürü tanı ve tedavi seçimi için zorunludur."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Stratejisi",
                "question": "Ateşsiz, böğür hassasiyeti olmayan ve tuvalet eğitimini tamamlamış bu çocukta hangi tetkik yaklaşımı uygundur?",
                "options": [
                    {
                        "text": "Böbrek tutulumunu dışlamak amacıyla tam kan sayımı, CRP, kan kültürü ve böbrek fonksiyon testleri isteyip idrar tetkikini sonuçlara göre planlamak",
                        "is_correct": False,
                        "scenario_update": "Kan tetkikleri normal geldi; çocuk gereksiz damar yolu girişimine maruz kaldı ve asıl tanısal tetkik gecikti.",
                        "teaching_point": "Ateşsiz ve iyi görünümlü çocukta kan tetkikleri ve kan kültürü gerekmez."
                    },
                    {
                        "text": "Çocuğun bezine idrar torbası yapıştırıp toplanan örnekten hem tam idrar tetkiki hem de kültür göndermek ve sonuca göre tedavi başlamak",
                        "is_correct": False,
                        "scenario_update": "Torba örneğinin kültüründe karışık flora üredi; sonuç yorumlanamadı ve tetkik tekrarlandı.",
                        "teaching_point": "Torba idrarı kontaminasyon riski nedeniyle kültür için uygun değildir; tuvalet eğitimli çocukta orta akım temiz idrar alınır."
                    },
                    {
                        "text": "Genital temizlik sonrası orta akım idrar örneğinden tam idrar tetkiki ve mikroskopi yapmak, aynı örneği antibiyotik öncesinde kültüre göndermek",
                        "is_correct": True,
                        "explanation": "Tuvalet eğitimli çocukta temiz orta akım idrarı güvenilir bir örnektir. Lökosit esteraz, nitrit ve mikroskopik piyüri ön tanıyı destekler; kesin tanı ve antibiyotik seçimi kültürle yapılır.",
                        "new_finding": "Tam idrar: dansite 1020, lökosit esteraz +++, nitrit pozitif, mikroskopide her sahada 35-40 lökosit, bol bakteri, 1-2 eritrosit. Kültür antibiyotik öncesi gönderildi."
                    },
                    {
                        "text": "Altta yatan anatomik bir sorunu dışlamak için aynı gün böbrek-mesane ultrasonu ve işeme sistoüretrografisi planlamak, ardından idrar kültürü göndermek",
                        "is_correct": False,
                        "scenario_update": "İşeme sistoüretrografisi aktif enfeksiyon döneminde ve gereksiz yere planlandı; aile kateterizasyon nedeniyle çok kaygılandı.",
                        "teaching_point": "Ateşsiz ilk enfeksiyonda rutin görüntüleme gerekmez; işeme sistoüretrografisi seçilmiş olgularda yapılır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Ateşsiz dizüri, sık idrara çıkma, suprapubik hassasiyet, piyüri ve nitrit pozitifliği olan, kabız bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Akut sistit ve mesane-bağırsak disfonksiyonu",
                        "is_correct": True,
                        "explanation": "Ateşsiz alt üriner sistem yakınmaları, piyüri ve nitrit pozitifliği akut sistiti düşündürür; kültür doğrular. Kabızlık ve işeme ertelemesi eşlik eden ve tekrar riskini artıran mesane-bağırsak disfonksiyonunu gösterir.",
                        "new_finding": "Tanı: Akut Sistit (ateşsiz idrar yolu enfeksiyonu), eşlik eden mesane-bağırsak disfonksiyonu."
                    },
                    {
                        "text": "Kimyasal irritan üretrit",
                        "is_correct": False,
                        "scenario_update": "Köpük banyosu veya sabun maruziyeti öyküsü yok; nitrit pozitifliği bakteriyel enfeksiyonu düşündürüyor.",
                        "teaching_point": "İrritan üretritte idrar tetkiki genellikle normaldir."
                    },
                    {
                        "text": "Akut piyelonefrit",
                        "is_correct": False,
                        "scenario_update": "Ateş, böğür ağrısı, kostovertebral açı hassasiyeti ve sistemik bulgu yok.",
                        "teaching_point": "Piyelonefritte ateş ve böğür hassasiyeti beklenir; tedavi süresi ve yaklaşım farklıdır."
                    },
                    {
                        "text": "Nonspesifik vulvovajinit",
                        "is_correct": False,
                        "scenario_update": "Genital muayene normal; idrarda nitrit pozitif ve belirgin piyüri var.",
                        "teaching_point": "Vulvovajinitte dış genital eritem ve akıntı görülür; nitrit pozitifliği beklenmez."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuğun tedavi ve izlem planı hangisidir?",
                "options": [
                    {
                        "text": "Çocuğu servise yatırıp intravenöz seftriakson başlamak, ateşsiz geçen ilk 48 saatten sonra orale geçerek toplam 14 gün tedaviyi tamamlamak",
                        "is_correct": False,
                        "scenario_update": "İyi görünümlü, ateşsiz çocuk gereksiz yere yatırıldı ve geniş spektrumlu parenteral tedavi aldı.",
                        "teaching_point": "Ateşsiz alt üriner sistem enfeksiyonu oral ve kısa süreli tedavi edilir."
                    },
                    {
                        "text": "Oral sefaleksin 50 mg/kg/gün dört dozda 3-5 gün vermek, kültür sonucunu kontrol etmek, kabızlığı tedavi edip düzenli tuvalet alışkanlığını anlatmak",
                        "is_correct": True,
                        "explanation": "Ateşsiz enfeksiyonda yerel dirence uygun oral ajanla 3-5 günlük tedavi yeterlidir; kültüre göre gerekirse değiştirilir. Kabızlığın tedavisi, 2-3 saatte bir tuvalete gitme ve yeterli sıvı tekrarları önler; ilk atakta görüntüleme gerekmez.",
                        "new_finding": "Sefaleksin ve polietilen glikol başlandı, tuvalet programı anlatıldı. Kültürde 100.000 cfu/mL sefaleksine duyarlı E. coli üredi. 48 saatte yakınmaları geçti; bir ay sonra dışkılaması düzenliydi ve yeni atak olmadı."
                    },
                    {
                        "text": "Ondört gün amoksisilin-klavulanat vermek, tekrarları önlemek için altı ay düşük doz trimetoprim-sülfametoksazol proflaksisi başlamak ve işeme sistoüretrografisi planlamak",
                        "is_correct": False,
                        "scenario_update": "İlk ateşsiz atakta uzun tedavi, proflaksi ve invaziv görüntüleme gereksizdi; çocukta proflaksi sırasında döküntü gelişti.",
                        "teaching_point": "Proflaksi ve işeme sistoüretrografisi ilk ateşsiz enfeksiyonda rutin önerilmez."
                    },
                    {
                        "text": "Kültür sonucu gelene kadar antibiyotik vermeyip bol su içmesini önermek, kızılcık suyu ve idrar alkalileştirici şurup ile semptomları gidermeye çalışmak",
                        "is_correct": False,
                        "scenario_update": "İki gün tedavisiz kalan çocuğun yakınmaları arttı ve ateşi çıktı.",
                        "teaching_point": "Semptomatik ve piyürisi olan çocukta kültür alındıktan sonra ampirik tedavi geciktirilmemelidir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y64",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "11 Yaşında",
        "gender": "Erkek",
        "complaint": "Temmuz öğleden sonrası açık sahada futbol oynadıktan sonra başlayan baş dönmesi, halsizlik, bulantı ve aşırı terleme",
        "history": "Antrenörü anlatıyor: 'Saat 14:00'te güneş altında iki saattir maç yapıyorlardı. Sona doğru başı döndü, dizleri boşaldı ve yere oturdu. Çok terliyor, forması sırılsıklam. Bir şişe su içince bir kez kustu. Bizi tanıyor, sorulara doğru cevap veriyor. Bayılmadı, kasılmadı.' Bilinen hastalığı ve düzenli ilacı yok. Tartı: 38 kg.",
        "final_diagnosis": "Sıcak Bitkinliği (Isıya Bağlı Hastalık, Santral Sinir Sistemi Tutulumu Olmayan)",
        "disposition": "Yeşil Alanda Serin Ortamda Soğutma, Oral Elektrolitli Sıvı ve Sıcakta Egzersiz Eğitimi ile Taburculuk",
        "case_pearl": "Isıya bağlı hastalıkta en kritik ayrım santral sinir sistemi tutulumudur: sıcak çarpmasında vücut iç ısısı genellikle >40°C'dir ve bilinç değişikliği, konfüzyon, ataksi veya nöbet görülür; acil soğuk suya daldırma gerekir. Sıcak bitkinliğinde bilinç normaldir, iç ısı genellikle <40°C'dir; serin ortam, soyma, evaporatif soğutma ve oral elektrolitli sıvı yeterlidir. Aksiller ölçüm güvenilmez, rektal ölçüm tercih edilir. Antipiretikler etkisizdir. Aşırı sade su hiponatremiye yol açabilir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Sıcakta egzersiz sonrası baş dönmesi ve kusması olan bu çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Çocuğu hemen serin bir odaya alıp formasını çıkarmak, rektal ısı ölçmek, bilinç-davranış, nörolojik bulgular, vital bulgular ve kan şekerini değerlendirmek",
                        "is_correct": True,
                        "explanation": "Isıya bağlı hastalıkta soğutmaya başlamak ve iç ısıyı doğru ölçmek eş zamanlı yapılır. Bilinç değişikliği, konfüzyon veya ataksi santral sinir sistemi tutulumunu gösterir ve yaklaşımı tamamen değiştirir.",
                        "new_finding": "Vital Bulgular: Rektal ısı 38.9°C, KTA 112/dk, SS 22/dk, SpO2 %99, TA 100/62 mmHg, kapiller kan şekeri 92 mg/dL. Bilinç açık, oryante, konuşması akıcı. Yürüyüşü dengeli, nörolojik muayene normal. Cilt nemli ve terli, mukozalar hafif kuru, KDZ 2.5 sn."
                    },
                    {
                        "text": "Kusma nedeniyle önce intravenöz yol açıp 20 mL/kg serum fizyolojik bolus başlatmak ve sıvı bitene kadar çocuğu sedyede sıcak bekleme alanında tutmak",
                        "is_correct": False,
                        "scenario_update": "Sıvı verilirken çocuk sıcak ortamda kaldı; iç ısı ölçülmedi ve soğutma gecikti.",
                        "teaching_point": "İlk öncelik serin ortama alma ve soğutmadır; oral alabilen çocukta intravenöz sıvı zorunlu değildir."
                    },
                    {
                        "text": "Baş dönmesi ve kusma nedeniyle kafa travması olasılığını düşünüp boyunluk takmak ve nörolojik değerlendirme için çocuğu sırtüstü sabitlemek",
                        "is_correct": False,
                        "scenario_update": "Öyküde travma yoktu; boyunluk ve sabitleme sırasında çocuk terlemeye devam etti ve soğutma başlamadı.",
                        "teaching_point": "Travma öyküsü olmayan çocukta omurga immobilizasyonu gereksizdir ve tedaviyi geciktirir."
                    },
                    {
                        "text": "Aksiller ısı 38.2°C olduğu için ateşi düşürmek amacıyla oral parasetamol vermek, yarım saat bekleyip ısı düşmezse ibuprofen eklemek",
                        "is_correct": False,
                        "scenario_update": "Antipiretik ısıyı düşürmedi; iç ısı ölçülmeden ve soğutma başlanmadan yarım saat geçti.",
                        "teaching_point": "Isıya bağlı hastalıkta yükseklik hipotalamik ayar noktasından kaynaklanmaz; antipiretikler etkisizdir, fiziksel soğutma gerekir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Stratejisi",
                "question": "Bilinci tamamen açık, rektal ısısı 38.9°C ve hafif dehidrate olan bu çocukta tetkik yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Kan şekeri, sodyum-potasyum, böbrek fonksiyonları ve kreatin kinaz ile idrar dansitesi bakmak; soğutmayı sürdürüp ısıyı 15-30 dakikada bir izlemek",
                        "is_correct": True,
                        "explanation": "Kusma ve aşırı terlemeyle sodyum değişikliği, prerenal azotemi ve rabdomiyoliz gelişebilir. Seri ısı ölçümü soğutmaya yanıtı ve kötüleşmeyi gösterir.",
                        "new_finding": "Glukoz 88 mg/dL, Na 137 mEq/L, K 4.1 mEq/L, BUN 16 mg/dL, kreatinin 0.6 mg/dL, CK 210 U/L. İdrar dansitesi 1028, miyoglobin negatif. 30. dakikada rektal ısı 38.1°C."
                    },
                    {
                        "text": "Ateş nedeniyle enfeksiyon odağı aramak amacıyla kan kültürü, CRP ve akciğer grafisi istemek, sonuç gelene kadar ampirik antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "Tetkikler normal geldi; gereksiz antibiyotik başlandı ve tablo egzersiz-ısı ilişkisi göz ardı edildi.",
                        "teaching_point": "Sıcakta egzersizle başlayan ve soğutmaya yanıt veren tabloda enfeksiyon tetkiki rutin değildir."
                    },
                    {
                        "text": "Tetkik istemeden çocuğu yarım saat gölgede dinlendirip baş dönmesi geçince antrenmana dönmesine izin vermek",
                        "is_correct": False,
                        "scenario_update": "Elektrolit ve hidrasyon durumu değerlendirilmeden antrenmana dönen çocuk yeniden baş dönmesi yaşadı.",
                        "teaching_point": "Isıya bağlı hastalık sonrası aynı gün egzersize dönüş önerilmez."
                    },
                    {
                        "text": "Baş dönmesi ve kusma birlikteliği nedeniyle kontrastsız beyin tomografisi çekmek, ardından ateş ve kusma için lomber ponksiyon planlamak",
                        "is_correct": False,
                        "scenario_update": "Bilinci açık, nörolojik muayenesi normal çocuğa gereksiz görüntüleme ve invaziv işlem planlandı.",
                        "teaching_point": "Normal nörolojik muayenesi olan çocukta görüntüleme ve lomber ponksiyon endike değildir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Sıcakta uzun egzersiz sonrası baş dönmesi, bulantı, aşırı terleme, bilinci açık ve rektal ısısı 38.9°C olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Sıcak bitkinliği",
                        "is_correct": True,
                        "explanation": "Sıcakta egzersiz sonrası halsizlik, baş dönmesi, bulantı-kusma, terleme ve hafif dehidratasyon ile birlikte normal bilinç ve 40°C altı iç ısı sıcak bitkinliğini tanımlar.",
                        "new_finding": "Tanı: Sıcak Bitkinliği."
                    },
                    {
                        "text": "Sıcak çarpması",
                        "is_correct": False,
                        "scenario_update": "Bilinç ve nörolojik muayene normal, iç ısı 40°C'nin altında.",
                        "teaching_point": "Sıcak çarpmasında santral sinir sistemi bulguları vardır ve hayatı tehdit eder."
                    },
                    {
                        "text": "Akut viral gastroenterit",
                        "is_correct": False,
                        "scenario_update": "Yakınmalar sıcakta egzersizle başladı, ishal yok ve soğutmayla hızla düzeliyor.",
                        "teaching_point": "Bağlamın (ısı, egzersiz) değerlendirilmesi tanının anahtarıdır."
                    },
                    {
                        "text": "Egzersize bağlı hiponatremi",
                        "is_correct": False,
                        "scenario_update": "Serum sodyumu 137 mEq/L, normal.",
                        "teaching_point": "Egzersize bağlı hiponatremi genellikle aşırı sade su alımıyla gelişir ve sodyum <135 mEq/L'dir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuğun tedavisi ve taburculuk önerileri nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Kaybedilen sıvıyı hızla yerine koymak için çocuğa yarım saat içinde iki litre sade su içirmek ve terleme geçince aynı gün maça dönmesine izin vermek",
                        "is_correct": False,
                        "scenario_update": "Hızlı sade su alımı sonrası bulantı arttı ve yeniden kustu; aynı gün egzersize dönüş riskliydi.",
                        "teaching_point": "Kısa sürede aşırı sade su hiponatremi riski taşır; elektrolitli sıvı azar azar verilmelidir."
                    },
                    {
                        "text": "Serin ortamda nemli bez ve fanla soğutmak, azar azar soğuk oral elektrolitli sıvı vermek; sıcakta egzersiz saatleri, sıvı molaları ve uyarı belirtilerini anlatmak",
                        "is_correct": True,
                        "explanation": "Evaporatif soğutma ve oral rehidratasyon sıcak bitkinliğinde yeterlidir. Günün sıcak saatlerinden kaçınma, düzenli sıvı molası, açık renkli giysi ve kademeli alışma tekrarları önler; konfüzyon gelişirse acil başvuru gerekir.",
                        "new_finding": "Bir saatte rektal ısı 37.4°C'ye, nabız 82/dk'ya geriledi; baş dönmesi geçti, iki bardak elektrolitli sıvıyı kusmadan içti. Antrenöre ve aileye öneriler yazılı verildi."
                    },
                    {
                        "text": "Aktif soğutma için çocuğu buzlu suya daldırıp titreme başlayana kadar tutmak ve ardından intravenöz parasetamol ile ısıyı kontrol altında tutmak",
                        "is_correct": False,
                        "scenario_update": "Bilinci açık çocuk buzlu suda şiddetli titreme ve huzursuzluk yaşadı; parasetamol ısıyı etkilemedi.",
                        "teaching_point": "Soğuk suya daldırma sıcak çarpmasında hayat kurtarıcıdır; sıcak bitkinliğinde evaporatif soğutma yeterlidir ve antipiretikler etkisizdir."
                    },
                    {
                        "text": "Çocuğu 24 saat gözlem için yatırıp intravenöz idame sıvısı başlamak, ertesi gün tekrar elektrolit ve böbrek fonksiyon testleri istemek",
                        "is_correct": False,
                        "scenario_update": "Bir saatte tamamen düzelen çocuk gereksiz yere yatırıldı ve tetkikler tekrarlandı.",
                        "teaching_point": "Soğutma ve oral sıvıyla düzelen, laboratuvarı normal çocuk taburcu edilebilir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y65",
        "category": "👁️ Göz Şikayetleri",
        "age": "5 Yaşında",
        "gender": "Kız",
        "complaint": "Sağ göz kapaklarında iki gündür giderek artan kızarıklık, şişlik ve dokunmakla hassasiyet",
        "history": "Annesi anlatıyor: 'Üç gün önce sağ kaşının kenarını sivrisinek ısırdı, çok kaşıdı. Dünden beri sağ üst ve alt göz kapağı kızardı, şişti, gözü biraz kapandı. Gözünün akı kızarık değil, akıntısı yok. Çizgi filmi net gördüğünü söylüyor, gözünü oynatınca acımıyor. Ateşi 37.4°C oldu.' Burun akıntısı veya sinüzit öyküsü yok. Aşıları tam. Tartı: 19 kg.",
        "final_diagnosis": "Preseptal Selülit (Cilt Bütünlüğü Bozulmasına Sekonder)",
        "disposition": "Yeşil Alandan Oral Antibiyotik, Alarm Bulguları Eğitimi ve 24-48 Saat Sonra Kontrol ile Taburculuk",
        "case_pearl": "Göz kapağı selülitinde asıl görev orbital tutulumu dışlamaktır: proptozis, ağrılı veya kısıtlı göz hareketleri, görme azalması, RAPD ve kemozis orbital selülit bulgularıdır ve kontrastlı orbita BT ile acil yatış gerektirir. Bu bulgular yoksa ve çocuk iyi görünümlüyse görüntüleme gerekmez. Cilt kaynaklı olgularda S. aureus ve A grubu streptokoku kapsayan oral tedavi (sefaleksin veya amoksisilin-klavulanat; MRSA riskinde klindamisin veya TMP-SMX) 7-10 gün verilir ve 24-48 saatte kontrol edilir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Göz kapaklarında kızarıklık ve şişliği olan bu 5 yaşındaki kızda muayenede öncelikle neyi değerlendirirsiniz?",
                "options": [
                    {
                        "text": "Ateşli kapak şişliğinde menenjit riskini dışlamak amacıyla önce ense sertliği ve Kernig-Brudzinski bulgularına odaklanmak, göz muayenesini oftalmolojiye bırakmak",
                        "is_correct": False,
                        "scenario_update": "Meninks bulguları negatifti; görme ve göz hareketleri değerlendirilmeden göz konsültasyonu için saatlerce beklendi.",
                        "teaching_point": "Göz kapağı enfeksiyonunun ilk değerlendirmesinde orbital bulgular acil hekimi tarafından kontrol edilmelidir."
                    },
                    {
                        "text": "Görme keskinliği, pupilla refleksleri ve RAPD, göz hareketlerinde ağrı veya kısıtlılık, proptozis ve kemoziyi değerlendirip cilt giriş kapısını ve sinüs bulgularını aramak",
                        "is_correct": True,
                        "explanation": "Göz kapağı enfeksiyonunda hayatı ve görmeyi tehdit eden durum septum arkasına yayılımdır. Görme, pupilla, göz hareketleri, proptozis ve kemozi bu ayrımın temelidir; giriş kapısı olası etkeni ve tedavi seçimini belirler.",
                        "new_finding": "Vital Bulgular: Ateş 37.3°C, KTA 92/dk, SS 20/dk, SpO2 %99. Genel durumu iyi. Sağ üst ve alt kapakta eritem, ödem ve hafif hassasiyet; kaş kenarında kaşıntıya bağlı ekskoriasyon. Göz hareketleri her yöne tam ve ağrısız, proptozis yok, kemozis yok. Görme keskinliği her iki gözde tam, pupillalar izokorik, RAPD yok. Burun akıntısı ve sinüs hassasiyeti yok."
                    },
                    {
                        "text": "Kapaklar şiş ve çocuk huzursuz olduğu için gözü açmaya zorlamadan sıcak kompres uygulamak, ödem azaldıktan sonra yarın ayrıntılı göz muayenesi için göz polikliniğine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Görme, pupilla ve göz hareketleri değerlendirilmeden çocuk gönderilecekti; orbital tutulum dışlanmamıştı.",
                        "teaching_point": "Şiş kapak muayeneyi zorlaştırsa da kapak nazikçe açılarak görme ve göz hareketleri mutlaka değerlendirilmelidir."
                    },
                    {
                        "text": "Sivrisinek ısırığı öyküsü nedeniyle tabloyu alerjik reaksiyon kabul edip oral antihistaminik vermek ve göz muayenesine gerek görmeden taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Hassasiyet ve ateş göz ardı edildi; enfeksiyon olasılığı ve orbital bulgular değerlendirilmedi.",
                        "teaching_point": "Alerjik ödem genellikle kaşıntılı ve ağrısızdır; hassasiyet ve ateş enfeksiyonu düşündürür."
                    }
                ]
            },
            {
                "stage_title": "Tetkik ve Görüntüleme Kararı",
                "question": "Orbital bulgusu olmayan, iyi görünümlü bu çocukta tetkik yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Göz kapağı ödemi ve ateşi olan her çocukta septum arkasına yayılımı kesin olarak dışlamak için acil kontrastlı orbita ve sinüs bilgisayarlı tomografisi çekmek",
                        "is_correct": False,
                        "scenario_update": "Tomografi normal geldi; çocuk gereksiz radyasyon ve kontrast maddeye maruz kaldı.",
                        "teaching_point": "Orbita BT orbital bulgu varlığında, muayene yapılamadığında veya 24-48 saatte yanıt alınamadığında endikedir."
                    },
                    {
                        "text": "Kan kültürü, tam kan sayımı ve CRP almak, değerler yüksekse çocuğu yatırıp intravenöz antibiyotik başlamak üzere planlama yapmak",
                        "is_correct": False,
                        "scenario_update": "Lökosit 8.400/mm³, CRP hafif yüksek geldi; kan kültürü negatifti ve tetkikler yönetimi değiştirmedi.",
                        "teaching_point": "İyi görünümlü çocukta kan kültürünün verimi çok düşüktür; yatış kararı klinik bulgulara dayanır."
                    },
                    {
                        "text": "Sedasyon altında orbita manyetik rezonansı ve göz içi basıncı ölçümü yaptırmak, sonuçlar normalse oral tedaviyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Sedasyon için çocuğun aç kalması gerekti ve tedavi saatlerce gecikti.",
                        "teaching_point": "MR ve göz içi basıncı ölçümü bu klinik tabloda gereksizdir."
                    },
                    {
                        "text": "Görüntüleme veya kan tetkiki istemeden klinik tanıyla tedaviyi planlamak, orbital bulguların yokluğunu kayıt altına almak ve kontrol zamanını belirlemek",
                        "is_correct": True,
                        "explanation": "Orbital bulgusu olmayan, sistemik olarak iyi ve muayenesi güvenilir çocukta tanı kliniktir. Tetkikler yönetimi değiştirmez; asıl güvenlik önlemi yakın klinik izlemdir.",
                        "new_finding": "Tetkik istenmedi. Muayene bulguları ve kapak eritem sınırı kalemle işaretlenerek kayda geçirildi."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Böcek ısırığı ve kaşıma sonrası göz kapaklarında hassas eritem-ödem, ağrısız ve tam göz hareketleri, normal görme ve proptozis yokluğu olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Preseptal selülit",
                        "is_correct": True,
                        "explanation": "Cilt bütünlüğü bozulması sonrası gelişen, septum önüyle sınırlı hassas eritem-ödem ve normal orbital muayene preseptal selülitle uyumludur.",
                        "new_finding": "Tanı: Preseptal Selülit (cilt kaynaklı)."
                    },
                    {
                        "text": "Böcek ısırığına lokal alerjik reaksiyon",
                        "is_correct": False,
                        "scenario_update": "Lezyon hassas, ateş var ve eritem giderek yayılıyor.",
                        "teaching_point": "Alerjik reaksiyon kaşıntılı, hassasiyetsiz ve ateşsizdir."
                    },
                    {
                        "text": "Akut dakriyosistit",
                        "is_correct": False,
                        "scenario_update": "Şişlik iç kantusta lokalize değil ve gözyaşı kesesinden akıntı yok.",
                        "teaching_point": "Dakriyosistit medial kantusta, gözyaşı kesesi üzerinde hassas şişlikle seyreder."
                    },
                    {
                        "text": "Orbital selülit",
                        "is_correct": False,
                        "scenario_update": "Proptozis, ağrılı veya kısıtlı göz hareketi, görme kaybı ve kemozis yok.",
                        "teaching_point": "Orbital selülit septum arkasına yayılımdır ve orbital bulgularla kendini gösterir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuğun tedavi ve izlem planı hangisidir?",
                "options": [
                    {
                        "text": "Yalnızca antibiyotikli göz damlası ve göz merhemi reçete etmek, kapağa günde birkaç kez soğuk kompres önermek ve şişlik geçmezse bir hafta sonra kontrole gelmesini söylemek",
                        "is_correct": False,
                        "scenario_update": "Topikal tedavi yumuşak doku enfeksiyonuna ulaşmadı; iki gün sonra eritem yanağa doğru yayıldı.",
                        "teaching_point": "Preseptal selülit yumuşak doku enfeksiyonudur ve sistemik antibiyotik gerektirir."
                    },
                    {
                        "text": "Oral sefaleksin veya amoksisilin-klavulanat ile 7-10 gün tedavi, eritem sınırını izlemek, görme bozukluğu veya ağrılı göz hareketinde acil başvuru ve 24-48 saatte kontrol",
                        "is_correct": True,
                        "explanation": "Cilt kaynaklı preseptal selülitte S. aureus ve A grubu streptokoku kapsayan oral tedavi yeterlidir. Alarm bulguları ve 24-48 saatlik kontrol orbital yayılımı erken yakalamayı sağlar; yanıt yoksa görüntüleme ve yatış düşünülür.",
                        "new_finding": "Oral sefaleksin başlandı, alarm bulguları anlatıldı. 48. saat kontrolünde eritem işaretli sınırın gerisine çekilmişti, göz kolayca açılıyordu; tedavi 7 güne tamamlandı."
                    },
                    {
                        "text": "Ödemi hızla azaltmak için oral prednizolon ve antihistaminik başlamak, antibiyotiği ancak ateş 38.5°C'yi geçerse vermek üzere aileye reçete etmek",
                        "is_correct": False,
                        "scenario_update": "Steroid ödemi kısa süre azalttı ancak enfeksiyon ilerledi; ertesi gün kapak eritemi belirgin şekilde genişledi.",
                        "teaching_point": "Bakteriyel yumuşak doku enfeksiyonunda tedavinin temeli antibiyotiktir; steroidlerin yeri yoktur."
                    },
                    {
                        "text": "Çocuğu servise yatırıp intravenöz seftriakson ve vankomisin başlamak, orbita BT ile izlemek ve en az beş gün intravenöz tedaviyi sürdürmek",
                        "is_correct": False,
                        "scenario_update": "İyi görünümlü çocuk gereksiz yere yatırıldı ve geniş spektrumlu parenteral tedavi aldı.",
                        "teaching_point": "Yatış küçük bebeklerde, toksik görünümde, oral tolere edemeyende veya ayaktan tedaviye yanıtsızlıkta gerekir."
                    }
                ]
            }
        ]
    }
]
