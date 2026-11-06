# -*- coding: utf-8 -*-
"""
Yeşil Alan Simülasyon Vakaları - Bölüm 7 (G61 - G70)
"""

GREEN_CASES_PART7 = [{'id': 'G61',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '4 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Bu sabah aniden başlayan sağ bacağa basamama ve topallama',
  'history': "Babası anlatıyor: 'Bir hafta önce hafif burun akıntısı ve öksürüğü olmuştu, ilaçsız geçti. Bu sabah "
             'uyanınca sağ bacağının üstüne basınca acıdığını söyleyip ağladı, topallayarak yürüyor. Ateşi hiç '
             "çıkmadı. Düşme ya da çarpma olmadı. İştahı ve neşesi yerinde.' Bilinen hastalığı yok. Tartı: 17 kg.",
  'final_diagnosis': 'Geçici (Toksik) Sinovit',
  'disposition': 'Yeşil Alandan Oral NSAİİ, Kısa Süreli İstirahat, Alarm Bulguları Eğitimi ve 48-72 Saat Sonra Kontrol '
                 'ile Taburculuk',
  'case_pearl': '3-8 yaş erkek çocukta viral enfeksiyon sonrası ani başlayan, ateşsiz, iyi görünümlü topallama geçici '
                'sinovitin tipik tablosudur. Asıl hedef septik artriti kaçırmamaktır: Kocher kriterleri (ateş >38.5°C, '
                'basamama, ESH >40 mm/sa, lökosit >12.000/mm³) ve CRP >2 mg/dL riski artırır. Ultrasonda efüzyon iki '
                'durumda da görülebilir; ayrım klinik ve laboratuvarla yapılır. Tedavi NSAİİ ve istirahattir; '
                'yakınmalar genellikle 1-2 haftada geçer.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Ateşsiz, travmasız, aniden topallamaya başlayan bu 4 yaşındaki çocukta muayenede neyi '
                         'değerlendirirsiniz?',
             'options': [{'text': 'Ateşi ve genel görünümü, yürüyüşü, kalça iç rotasyon-abdüksiyonunu, diğer '
                                  'eklemleri, omurga, karın, testis ve cildi sistematik olarak değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Çocukta topallamanın kaynağı kalça dışında diz, omurga, karın veya testis '
                                         'olabilir. Ateş, toksik görünüm ve hareket kısıtlılığının derecesi septik '
                                         'artriti diğer nedenlerden ayırmada ilk ipuçlarıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 94/dk, SS 20/dk, SpO2 %99. Masada otururken '
                                         'neşeli, oyuncakla oynuyor. Sağ bacağa kısmen basarak antaljik yürüyüş. Sağ '
                                         'kalçada iç rotasyon ve abdüksiyonun son derecelerinde hafif ağrı; pasif '
                                         'hareket büyük ölçüde serbest. Isı artışı, kızarıklık, şişlik yok. Diz, ayak '
                                         'bileği, omurga, karın ve testis muayenesi normal. Peteşi veya döküntü yok.'},
                         {'text': 'Bacağını kullanmak istemediği için çocuğu tekerlekli sandalyeye alıp ortopedi '
                                  'konsültasyonu istemek, sistemik muayeneyi ortopedi değerlendirmesinden sonraya '
                                  'bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Ortopedi ekibi iki saat sonra geldi; bu sürede ateş, diğer eklemler ve '
                                             'karın değerlendirilmemişti.',
                          'teaching_point': 'Topallayan çocuğun ilk değerlendirmesi acil hekiminin sorumluluğundadır; '
                                            'konsültasyon sistematik muayeneden sonra gerekirse istenir.'},
                         {'text': 'Topallamanın kaynağının kalça olduğunu kabul edip yalnızca kalça eklemini muayene '
                                  'etmek ve ağrı kontrolü için hemen intramüsküler diklofenak uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Enjeksiyon sonrası çocuk ağlayarak muayeneye direnç gösterdi; diz, '
                                             'omurga ve karın muayenesi yapılmadan zaman geçti.',
                          'teaching_point': 'Küçük çocuk ağrının yerini doğru tarif edemez; topallamada tüm alt '
                                            'ekstremite, omurga, karın ve genital bölge muayene edilmelidir.'},
                         {'text': 'Çocuğun travma öyküsünü saklıyor olabileceğini düşünüp istismar şüphesiyle sosyal '
                                  'hizmet bildirimi yapmak ve kemik taraması planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ciltte morluk, kırık bulgusu veya öyküde tutarsızlık yoktu; aile yersiz '
                                             'şüpheden incindi ve muayene ertelendi.',
                          'teaching_point': 'İstismar şüphesi tutarsız öykü, uygunsuz yaralanma bulguları veya '
                                            'gecikmiş başvuru gibi somut ipuçlarına dayanmalıdır.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Ateşsiz, iyi görünümlü ve kalça hareketleri hafif ağrılı bu çocukta hangi tetkik yaklaşımı '
                         'uygundur?',
             'options': [{'text': 'Kalça patolojilerini en iyi gösteren yöntem olduğu için sedasyon altında kontrastlı '
                                  'kalça manyetik rezonans görüntülemesi planlamak',
                          'is_correct': False,
                          'scenario_update': 'MR için sedasyon ve saatlerce bekleme gerekti; temel laboratuvar '
                                             'tetkikleri istenmemişti.',
                          'teaching_point': 'MR, atipik seyir veya osteomiyelit şüphesinde değerlidir; ilk basamak '
                                            'tetkik değildir.'},
                         {'text': 'Yalnızca ön-arka pelvis grafisi çekmek, kırık ve kemik lezyonu görülmezse '
                                  'laboratuvar istemeden taburcu edip bir hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Grafi normal geldi; inflamatuvar belirteçler bakılmadan taburcu edilmek '
                                             'üzereydi ve septik artrit dışlanmamıştı.',
                          'teaching_point': 'Normal grafi eklem enfeksiyonunu dışlamaz; basamayan çocukta laboratuvar '
                                            've ultrason değerlendirmesi gerekir.'},
                         {'text': 'Ortopedi ile birlikte acil kalça eklem aspirasyonu yapmak, sinovyal sıvıyı hücre '
                                  'sayımı ve kültür için gönderip sonuç gelene kadar intravenöz antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'Sedasyonla aspirasyon yapıldı; az miktarda berrak sıvıda düşük hücre '
                                             'sayısı saptandı. Çocuk gereksiz yere invaziv işlem ve antibiyotiğe maruz '
                                             'kaldı.',
                          'teaching_point': 'Eklem aspirasyonu ateş, basamama ve yüksek inflamatuvar belirteçlerle '
                                            'septik artrit riski arttığında endikedir.'},
                         {'text': 'Tam kan sayımı, CRP ve sedimantasyon istemek, bilateral kalça ultrasonografisiyle '
                                  'efüzyonu değerlendirmek ve sonuçları septik artrit risk kriterleriyle yorumlamak',
                          'is_correct': True,
                          'explanation': 'Lökosit, ESH ve CRP Kocher ve CRP kriterlerinin bileşenleridir. Ultrason '
                                         'efüzyonu gösterir ancak septik artriti ayırmaz; karar klinik ve laboratuvar '
                                         'birlikte değerlendirilerek verilir.',
                          'new_finding': 'Lökosit 7.800/mm³, CRP 0.2 mg/dL, ESH 12 mm/sa. Kalça ultrasonu: sağda 4 mm '
                                         'anekoik efüzyon, sinovyal kalınlaşma yok; sol kalça normal. Kocher '
                                         'kriterlerinin hiçbiri yok.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Viral enfeksiyon sonrası ateşsiz topallama, normal inflamatuvar belirteçler ve kalçada az '
                         'miktarda efüzyonu olan bu çocukta tanı nedir?',
             'options': [{'text': 'Septik artrit',
                          'is_correct': False,
                          'scenario_update': 'Ateş yok, lökosit, CRP ve ESH normal, çocuk kısmen basabiliyor.',
                          'teaching_point': 'Septik artritte ateş, şiddetli ağrı, basamama ve yüksek inflamatuvar '
                                            'belirteçler beklenir.'},
                         {'text': 'Juvenil idiyopatik artrit',
                          'is_correct': False,
                          'scenario_update': 'Sabah tutukluğu ve 6 haftayı aşan eklem şişliği öyküsü yok.',
                          'teaching_point': 'Juvenil idiyopatik artrit tanısı için en az 6 hafta süren artrit '
                                            'gerekir.'},
                         {'text': 'Geçici (toksik) sinovit',
                          'is_correct': True,
                          'explanation': 'İyi görünüm, ateşsizlik, normal lökosit-CRP-ESH ve küçük efüzyon geçici '
                                         'sinovitle uyumludur; Kocher kriterlerinin hiçbirinin olmaması septik artrit '
                                         'olasılığını çok düşük kılar.',
                          'new_finding': 'Tanı: Geçici (Toksik) Sinovit.'},
                         {'text': 'Legg-Calvé-Perthes hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Yakınma aniden ve viral enfeksiyon sonrası başladı; haftalar süren sinsi '
                                             'topallama öyküsü yok.',
                          'teaching_point': 'Perthes hastalığı sinsi başlangıçlıdır; topallama 2 haftayı aşarsa grafi '
                                            'tekrarlanmalıdır.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuğun tedavi ve izlem planı nasıl olmalıdır?',
             'options': [{'text': 'Sinovyal inflamasyonu hızla baskılamak için üç gün oral prednizolon vermek ve iki '
                                  'hafta sonra kalça manyetik rezonansı ile kontrol etmek',
                          'is_correct': False,
                          'scenario_update': "Steroid sonrası iştah artışı ve uyku bozukluğu gelişti; kontrol MR'ı "
                                             'gereksizdi.',
                          'teaching_point': 'Geçici sinovitte sistemik steroid ve rutin ileri görüntüleme önerilmez.'},
                         {'text': 'Çocuğu servise yatırıp cilt traksiyonu uygulamak, intravenöz sıvı başlamak ve '
                                  'günlük CRP ile ultrason kontrolü yaparak efüzyon kaybolana kadar izlemek',
                          'is_correct': False,
                          'scenario_update': 'Yatışın üçüncü gününde çocuk iyileşmişti; traksiyon ve tekrarlanan '
                                             'tetkikler sonucu değiştirmedi.',
                          'teaching_point': 'Geçici sinovitte traksiyon ve yatış gerekmez; seri ultrason efüzyonun '
                                            'takibinde kullanılmaz.'},
                         {'text': 'Ibuprofen 10 mg/kg 8 saatte bir, kısa süreli istirahat, ateş veya basamama '
                                  'gelişirse hemen başvuru eğitimi ve 48-72 saat sonra kontrol',
                          'is_correct': True,
                          'explanation': 'NSAİİ ağrı ve sinovyal inflamasyonu azaltır ve iyileşmeyi hızlandırır. Ateş, '
                                         'kötüleşen ağrı veya basamama septik artrit olasılığını yeniden gündeme '
                                         'getirir; bu nedenle kısa süreli kontrol önemlidir.',
                          'new_finding': 'İbuprofen başlandı, alarm bulguları anlatıldı. 72. saat kontrolünde çocuk '
                                         'topallamadan koşuyordu; kalça hareketleri ağrısızdı.'},
                         {'text': 'Olası erken bakteriyel enfeksiyonu önlemek için 10 gün oral sefaleksin başlamak ve '
                                  'topallama tamamen geçene kadar çocuğun yürümesini yasaklamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz antibiyotik sonrası çocukta ishal gelişti; yürüme yasağı '
                                             'ailenin günlük yaşamını zorlaştırdı.',
                          'teaching_point': 'Bu tabloda antibiyotik endikasyonu yoktur; çocuk tolere ettiği ölçüde '
                                            'hareket edebilir.'}]}]},
 {'id': 'G62',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '9 Yaşında',
  'gender': 'Kız',
  'complaint': 'Dört saattir süren şiddetli, zonklayıcı baş ağrısı, bulantı, ışık ve sesten rahatsızlık',
  'history': "Annesi anlatıyor: 'Öğleden sonra okulda başının sağ tarafında zonklayıcı, çok şiddetli bir ağrı başladı. "
             'Eve gelince iki kez kustu. Işık ve ses ağrısını artırıyor, karanlık odaya kapanmak istiyor. Son bir '
             'yılda ayda bir-iki kez benzer, daha hafif ağrıları oldu, uyuyunca geçiyordu. Bende de gençliğimden beri '
             "böyle baş ağrıları var.' Ateş, travma, sabah kusması veya uykudan uyandıran baş ağrısı yok. Tartı: 30 "
             'kg.',
  'final_diagnosis': 'Aurasız Migren Atağı',
  'disposition': 'Yeşil Alanda Erken Analjezi, Antiemetik ve Karanlık-Sessiz Ortamda Dinlendirme Sonrası Baş Ağrısı '
                 'Günlüğü Eğitimi ile Taburculuk',
  'case_pearl': 'Çocuklarda migren erişkinden daha kısa (2-72 saat) ve sıklıkla bilateral olabilir; bulantı-kusma, '
                'fotofobi-fonofobi ve aile öyküsü tanıyı destekler. Normal nörolojik ve fundoskopik muayenede, kırmızı '
                "bayrak yoksa görüntüleme gerekmez. Akut tedavide ilk seçenek erken alınan ibuprofen 10 mg/kg'dır; "
                'yanıt yoksa intravenöz sıvı ve dopamin antagonisti eklenir. Opioidlerden kaçınılır; ayda 10-15 günden '
                'fazla analjezik kullanımı ilaç aşırı kullanım baş ağrısına yol açar.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Şiddetli baş ağrısı ve kusması olan bu 9 yaşındaki kızda değerlendirmenin odağı nedir?',
             'options': [{'text': 'Ailede benzer baş ağrısı olduğu için tanıyı öyküye dayanarak koymak, muayeneyi '
                                  'vital bulgularla sınırlı tutup oral analjezik vererek taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Fundoskopi ve nörolojik muayene yapılmadan taburcu edildi; kırmızı '
                                             'bayraklar dışlanmadığı için aile ertesi gün başka bir merkeze başvurdu.',
                          'teaching_point': 'Aile öyküsü destekleyicidir ancak sekonder nedenleri dışlamak için '
                                            'ayrıntılı muayene şarttır.'},
                         {'text': 'Kan basıncı, ateş ve bilinç düzeyini değerlendirmek; fundoskopi, meninks irritasyon '
                                  'bulguları, kraniyal sinirler, motor-duyu ve serebellar muayeneyi yapmak',
                          'is_correct': True,
                          'explanation': 'Baş ağrılı çocukta sekonder nedenler (menenjit, kafa içi basınç artışı, '
                                         'hipertansiyon, kitle) ancak sistematik nörolojik muayene ve fundoskopiyle '
                                         'dışlanabilir. Normal muayene görüntüleme ihtiyacını belirleyen en önemli '
                                         'unsurdur.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 82/dk, SS 18/dk, SpO2 %99, TA 102/64 mmHg. '
                                         'Işıktan gözlerini kısıyor. Bilinç açık, oryante. Ense sertliği, Kernig ve '
                                         'Brudzinski negatif. Kraniyal sinirler, motor-duyu muayenesi ve serebellar '
                                         'testler normal. Fundoskopide optik disk sınırları keskin, venöz pulsasyon '
                                         'var.'},
                         {'text': 'Kusma ve tek taraflı ağrı nedeniyle kafa içi kanama düşünüp çocuğu sedyede yatırmak '
                                  've muayene etmeden acil beyin tomografisi istemek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi için sıra beklenirken muayene yapılmadı; nörolojik muayene '
                                             'sonradan tamamen normal bulundu.',
                          'teaching_point': 'Görüntüleme kararı öykü ve muayene bulgularına göre verilir; muayeneden '
                                            'önce rutin tomografi istenmez.'},
                         {'text': 'Çocuğun ağrısını hızla azaltmak için muayeneden önce intravenöz tramadol uygulamak '
                                  've rahatladıktan sonra kısa bir nörolojik değerlendirme yapmak',
                          'is_correct': False,
                          'scenario_update': 'Tramadol sonrası bulantısı arttı ve uykuya daldı; nörolojik muayene '
                                             'güvenilir yapılamadı.',
                          'teaching_point': 'Opioidler çocukta baş ağrısı tedavisinde önerilmez; ayrıca muayeneyi '
                                            'maskeleyebilir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Nörolojik ve fundoskopik muayenesi normal olan bu çocukta tetkik yaklaşımınız nedir?',
             'options': [{'text': 'Ataklar arasında tamamen iyi olduğu için epileptik bir süreci dışlamak amacıyla '
                                  'acil elektroensefalografi istemek ve sonucu nöroloji ile değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'EEG acil koşullarda yapılamadı; randevu haftalar sonrasına verildi ve '
                                             'tanıya katkısı olmadı.',
                          'teaching_point': 'EEG baş ağrısının rutin değerlendirmesinde yer almaz; bilinç kaybı veya '
                                            'nöbet şüphesinde düşünülür.'},
                         {'text': 'Menenjit olasılığını dışlamak için tam kan sayımı ve CRP istemek, yüksek çıkarsa '
                                  'lomber ponksiyon yapmak üzere hazırlık yapmak',
                          'is_correct': False,
                          'scenario_update': 'Lökosit ve CRP normal geldi; ateş ve meninks bulgusu olmadığı halde '
                                             'çocuk kan alımı sırasında daha da kötüleşti.',
                          'teaching_point': 'Ateşsiz, meninks irritasyon bulgusu olmayan çocukta menenjit için kan '
                                            'tetkiki ve lomber ponksiyon endike değildir.'},
                         {'text': 'Kırmızı bayrakları (ani gök gürültüsü ağrı, uykudan uyandırma, sabah kusması, '
                                  'nörolojik bulgu, kişilik değişikliği) aileyle gözden geçirip görüntüleme istememek',
                          'is_correct': True,
                          'explanation': 'Kırmızı bayrak olmayan, tekrarlayan benzer atakları ve normal muayenesi olan '
                                         'çocukta tanı kliniktir. Görüntüleme ve laboratuvar yönetimi değiştirmez; '
                                         'aileye hangi durumda yeniden değerlendirme gerektiği anlatılır.',
                          'new_finding': 'Kırmızı bayrak saptanmadı. Ataklar son bir yılda benzer nitelikte, aralarda '
                                         'çocuk tamamen iyi. Tetkik istenmedi.'},
                         {'text': 'Kusmayla seyreden ilk şiddetli atak olduğu için kontrastsız beyin tomografisi '
                                  'çekmek ve normalse aileyi rahatlatarak taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi normal geldi; çocuk gereksiz radyasyona maruz kaldı ve ağrısı '
                                             'tedavi edilmeden bir saat geçti.',
                          'teaching_point': 'Tekrarlayan benzer ataklar, aile öyküsü ve normal muayenede görüntüleme '
                                            'tanıya katkı sağlamaz.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Tekrarlayan, zonklayıcı, bulantı-kusma ve ışık-ses hassasiyetiyle seyreden, aile öyküsü olan '
                         've muayenesi normal bu çocukta tanı nedir?',
             'options': [{'text': 'Gerilim tipi baş ağrısı',
                          'is_correct': False,
                          'scenario_update': 'Ağrı zonklayıcı, şiddetli ve kusmayla birlikte; gerilim tipi baş '
                                             'ağrısında bunlar beklenmez.',
                          'teaching_point': 'Gerilim tipi baş ağrısı bası tarzında, hafif-orta şiddette ve '
                                            'bulantısızdır.'},
                         {'text': 'Akut bakteriyel rinosinüzit',
                          'is_correct': False,
                          'scenario_update': 'Burun akıntısı, ateş veya yüz ağrısı yok; ağrı epizodik.',
                          'teaching_point': 'Sinüzit tekrarlayan epizodik baş ağrısının nadir nedenidir.'},
                         {'text': 'Aurasız migren atağı',
                          'is_correct': True,
                          'explanation': 'Tekrarlayan, orta-şiddetli, zonklayıcı ağrı; bulantı-kusma ve '
                                         'fotofobi-fonofobi ile birlikte normal muayene ve aile öyküsü ICHD-3 aurasız '
                                         'migren kriterlerini karşılar.',
                          'new_finding': 'Tanı: Aurasız Migren Atağı.'},
                         {'text': 'İdiyopatik intrakraniyal hipertansiyon',
                          'is_correct': False,
                          'scenario_update': 'Papilödem ve görme yakınması yok, ataklar arasında çocuk tamamen iyi.',
                          'teaching_point': 'İdiyopatik intrakraniyal hipertansiyonda sürekli baş ağrısı ve papilödem '
                                            'beklenir.'}]},
            {'stage_title': 'Akut Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuğun acil serviste akut tedavisi ve taburculuk önerileri nasıl olmalıdır?',
             'options': [{'text': 'Oral ibuprofen 10 mg/kg ve ondansetron verip karanlık-sessiz odada dinlendirmek; '
                                  'atak başında erken ilaç alımını, uyku düzenini ve baş ağrısı günlüğünü anlatmak',
                          'is_correct': True,
                          'explanation': 'Atağın erken döneminde alınan ibuprofen çocuk migreninde en kanıtlı ilk '
                                         'basamaktır; antiemetik bulantıyı giderir. Günlük, tetikleyicileri ve sıklığı '
                                         'izlemeye yardım eder; analjezikleri ayda 10-15 günden fazla kullanmamak ilaç '
                                         'aşırı kullanım baş ağrısını önler.',
                          'new_finding': 'İbuprofen ve ondansetron sonrası karanlık odada bir saat uyudu; uyandığında '
                                         'ağrısı ve bulantısı geçmişti. Aileye günlük ve analjezik kullanım sınırları '
                                         'anlatıldı.'},
                         {'text': 'Atağı sonlandırmak için intravenöz deksametazon uygulamak ve tekrarları önlemek '
                                  'amacıyla acil serviste günlük topiramat proflaksisi başlatıp bir ay sonra kontrol '
                                  'önermek',
                          'is_correct': False,
                          'scenario_update': 'Steroid ilk basamak tedavi değildi; ayda bir-iki atağı olan çocukta '
                                             'proflaksi endikasyonu yoktu ve ilaç yan etki riski taşıyordu.',
                          'teaching_point': 'Proflaksi sık ve yeti yitimine yol açan ataklarda, poliklinik '
                                            'değerlendirmesiyle planlanır.'},
                         {'text': 'Ağrının şiddeti nedeniyle oral kodeinli parasetamol reçete etmek ve ataklar '
                                  'sırasında günde üç kez, en az beş gün düzenli kullanmasını önermek',
                          'is_correct': False,
                          'scenario_update': 'Kodein 12 yaş altında solunum depresyonu riski nedeniyle kontrendikedir; '
                                             'düzenli kullanım önerisi ilaç aşırı kullanımına zemin hazırlar.',
                          'teaching_point': 'Kodein ve diğer opioidler çocuklarda baş ağrısı tedavisinde '
                                            'kullanılmamalıdır.'},
                         {'text': 'Analjeziği yalnızca ağrı en şiddetli düzeye ulaştığında vermek, çocuğun okul ve '
                                  'ekran kullanımını tamamen yasaklayıp bir ay ev istirahati önermek',
                          'is_correct': False,
                          'scenario_update': 'Geç alınan ilaç etkisiz kaldı; okuldan uzaklaştırma çocuğun kaygısını '
                                             'artırdı.',
                          'teaching_point': 'Analjezik atak başında alınmalıdır; okula devam ve düzenli yaşam '
                                            'desteklenir.'}]}]},
 {'id': 'G63',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '6 Yaşında',
  'gender': 'Kız',
  'complaint': 'İki gündür idrar yaparken yanma, sık idrara çıkma ve altını ıslatma',
  'history': "Annesi anlatıyor: 'İki gündür çiş yaparken yandığını söyleyip ağlıyor. Günde on beş kez tuvalete koşuyor "
             "ama birkaç damla yapıyor. Dün okulda iki kez altına kaçırdı. Ateşi olmadı, böğrü ağrımıyor, kusmadı.' "
             'Ayrıntılı sorgulamada üç-dört günde bir, sert dışkı yaptığı ve okulda tuvalete gitmekten kaçındığı '
             'öğrenildi. Daha önce benzer yakınması olmamış. Tartı: 20 kg.',
  'final_diagnosis': 'Akut Sistit (Ateşsiz İdrar Yolu Enfeksiyonu), Eşlik Eden Mesane-Bağırsak Disfonksiyonu',
  'disposition': 'Yeşil Alandan Kültür Sonrası Kısa Süreli Oral Antibiyotik, Kabızlık Tedavisi ve Tuvalet Alışkanlığı '
                 'Eğitimi ile Taburculuk',
  'case_pearl': 'Okul çağındaki kız çocukta ateşsiz dizüri, sık idrara çıkma ve suprapubik hassasiyet alt üriner '
                'sistem enfeksiyonunu düşündürür. Tanı orta akım temiz idrarda piyüri ile birlikte anlamlı üremeyle '
                'konur; idrar torbası kültür için uygun değildir. Ateşsiz enfeksiyonda 3-5 günlük oral tedavi '
                'yeterlidir ve ilk atakta rutin görüntüleme gerekmez. Kabızlık ve işeme ertelemesi (mesane-bağırsak '
                'disfonksiyonu) tekrarların en sık değiştirilebilir nedenidir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Ateşsiz idrar yakınmaları olan bu 6 yaşındaki kızda muayenede neye dikkat edersiniz?',
             'options': [{'text': 'Ateş ve kostovertebral açı hassasiyetine bakmak, suprapubik bölgeyi ve dış genitali '
                                  'vulvovajinit ve yapışıklık açısından incelemek, lumbosakral omurga ve kabızlığı '
                                  'değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Ateş ve böğür hassasiyeti üst üriner sistem tutulumunu düşündürür. Genital '
                                         'muayene vulvovajinit, labial yapışıklık ve kıl kurdu gibi taklitçileri '
                                         'ayırır. Lumbosakral anomali ve kabızlık işeme bozukluğuna katkıda bulunur.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 86/dk, SS 18/dk, TA 98/62 mmHg. Genel '
                                         'durumu iyi. Suprapubik hafif hassasiyet; kostovertebral açı hassasiyeti yok. '
                                         'Sol alt kadranda dışkı kitlesi palpe ediliyor. Dış genital normal, vulvit, '
                                         'akıntı veya yapışıklık yok. Lumbosakral bölgede gamze veya kıl tutamı yok.'},
                         {'text': 'Altını ıslatma yakınması nedeniyle psikolojik bir sorun olabileceğini düşünüp okul '
                                  'stresini sorgulamak ve çocuk psikiyatrisine yönlendirme yapmak',
                          'is_correct': False,
                          'scenario_update': 'Fizik muayene ve idrar değerlendirmesi yapılmadan yönlendirme yapıldı; '
                                             'dizüri sürdü.',
                          'teaching_point': 'Yeni başlayan gündüz ıslatması öncelikle organik nedenlerle '
                                            'değerlendirilmelidir.'},
                         {'text': 'Havuz ve banyo öyküsünü sorgulayıp vulvovajinit kabul etmek, oturma banyosu önermek '
                                  've idrar tetkiki yapmadan semptomlar sürerse kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Genital muayene yapılmadan vulvovajinit kabul edildi; idrar tetkiki '
                                             'yapılmadığı için olası enfeksiyon tedavisiz kaldı.',
                          'teaching_point': 'Dizüri ve sık idrara çıkma idrar tetkikiyle değerlendirilmeli; '
                                            'vulvovajinit tanısı muayeneyle konmalıdır.'},
                         {'text': 'Muayeneyi yalnızca karın palpasyonuyla sınırlı tutup ampirik oral antibiyotik '
                                  'reçete etmek ve idrar örneğini tedaviden üç gün sonra kontrol amaçlı istemek',
                          'is_correct': False,
                          'scenario_update': 'Kültür alınmadan başlanan antibiyotik nedeniyle tanı doğrulanamadı ve '
                                             'direnç durumu öğrenilemedi.',
                          'teaching_point': 'Antibiyotik öncesi uygun yöntemle alınmış idrar kültürü tanı ve tedavi '
                                            'seçimi için zorunludur.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Ateşsiz, böğür hassasiyeti olmayan ve tuvalet eğitimini tamamlamış bu çocukta hangi tetkik '
                         'yaklaşımı uygundur?',
             'options': [{'text': 'Böbrek tutulumunu dışlamak amacıyla tam kan sayımı, CRP, kan kültürü ve böbrek '
                                  'fonksiyon testleri isteyip idrar tetkikini sonuçlara göre planlamak',
                          'is_correct': False,
                          'scenario_update': 'Kan tetkikleri normal geldi; çocuk gereksiz damar yolu girişimine maruz '
                                             'kaldı ve asıl tanısal tetkik gecikti.',
                          'teaching_point': 'Ateşsiz ve iyi görünümlü çocukta kan tetkikleri ve kan kültürü gerekmez.'},
                         {'text': 'Çocuğun bezine idrar torbası yapıştırıp toplanan örnekten hem tam idrar tetkiki hem '
                                  'de kültür göndermek ve sonuca göre tedavi başlamak',
                          'is_correct': False,
                          'scenario_update': 'Torba örneğinin kültüründe karışık flora üredi; sonuç yorumlanamadı ve '
                                             'tetkik tekrarlandı.',
                          'teaching_point': 'Torba idrarı kontaminasyon riski nedeniyle kültür için uygun değildir; '
                                            'tuvalet eğitimli çocukta orta akım temiz idrar alınır.'},
                         {'text': 'Genital temizlik sonrası orta akım idrar örneğinden tam idrar tetkiki ve mikroskopi '
                                  'yapmak, aynı örneği antibiyotik öncesinde kültüre göndermek',
                          'is_correct': True,
                          'explanation': 'Tuvalet eğitimli çocukta temiz orta akım idrarı güvenilir bir örnektir. '
                                         'Lökosit esteraz, nitrit ve mikroskopik piyüri ön tanıyı destekler; kesin '
                                         'tanı ve antibiyotik seçimi kültürle yapılır.',
                          'new_finding': 'Tam idrar: dansite 1020, lökosit esteraz +++, nitrit pozitif, mikroskopide '
                                         'her sahada 35-40 lökosit, bol bakteri, 1-2 eritrosit. Kültür antibiyotik '
                                         'öncesi gönderildi.'},
                         {'text': 'Altta yatan anatomik bir sorunu dışlamak için aynı gün böbrek-mesane ultrasonu ve '
                                  'işeme sistoüretrografisi planlamak, ardından idrar kültürü göndermek',
                          'is_correct': False,
                          'scenario_update': 'İşeme sistoüretrografisi aktif enfeksiyon döneminde ve gereksiz yere '
                                             'planlandı; aile kateterizasyon nedeniyle çok kaygılandı.',
                          'teaching_point': 'Ateşsiz ilk enfeksiyonda rutin görüntüleme gerekmez; işeme '
                                            'sistoüretrografisi seçilmiş olgularda yapılır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Ateşsiz dizüri, sık idrara çıkma, suprapubik hassasiyet, piyüri ve nitrit pozitifliği olan, '
                         'kabız bu çocukta tanı nedir?',
             'options': [{'text': 'Akut sistit ve mesane-bağırsak disfonksiyonu',
                          'is_correct': True,
                          'explanation': 'Ateşsiz alt üriner sistem yakınmaları, piyüri ve nitrit pozitifliği akut '
                                         'sistiti düşündürür; kültür doğrular. Kabızlık ve işeme ertelemesi eşlik eden '
                                         've tekrar riskini artıran mesane-bağırsak disfonksiyonunu gösterir.',
                          'new_finding': 'Tanı: Akut Sistit (ateşsiz idrar yolu enfeksiyonu), eşlik eden '
                                         'mesane-bağırsak disfonksiyonu.'},
                         {'text': 'Kimyasal irritan üretrit',
                          'is_correct': False,
                          'scenario_update': 'Köpük banyosu veya sabun maruziyeti öyküsü yok; nitrit pozitifliği '
                                             'bakteriyel enfeksiyonu düşündürüyor.',
                          'teaching_point': 'İrritan üretritte idrar tetkiki genellikle normaldir.'},
                         {'text': 'Akut piyelonefrit',
                          'is_correct': False,
                          'scenario_update': 'Ateş, böğür ağrısı, kostovertebral açı hassasiyeti ve sistemik bulgu '
                                             'yok.',
                          'teaching_point': 'Piyelonefritte ateş ve böğür hassasiyeti beklenir; tedavi süresi ve '
                                            'yaklaşım farklıdır.'},
                         {'text': 'Nonspesifik vulvovajinit',
                          'is_correct': False,
                          'scenario_update': 'Genital muayene normal; idrarda nitrit pozitif ve belirgin piyüri var.',
                          'teaching_point': 'Vulvovajinitte dış genital eritem ve akıntı görülür; nitrit pozitifliği '
                                            'beklenmez.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuğun tedavi ve izlem planı hangisidir?',
             'options': [{'text': 'Çocuğu servise yatırıp intravenöz seftriakson başlamak, ateşsiz geçen ilk 48 '
                                  'saatten sonra orale geçerek toplam 14 gün tedaviyi tamamlamak',
                          'is_correct': False,
                          'scenario_update': 'İyi görünümlü, ateşsiz çocuk gereksiz yere yatırıldı ve geniş spektrumlu '
                                             'parenteral tedavi aldı.',
                          'teaching_point': 'Ateşsiz alt üriner sistem enfeksiyonu oral ve kısa süreli tedavi edilir.'},
                         {'text': 'Oral sefaleksin 50 mg/kg/gün dört dozda 3-5 gün vermek, kültür sonucunu kontrol '
                                  'etmek, kabızlığı tedavi edip düzenli tuvalet alışkanlığını anlatmak',
                          'is_correct': True,
                          'explanation': 'Ateşsiz enfeksiyonda yerel dirence uygun oral ajanla 3-5 günlük tedavi '
                                         'yeterlidir; kültüre göre gerekirse değiştirilir. Kabızlığın tedavisi, 2-3 '
                                         'saatte bir tuvalete gitme ve yeterli sıvı tekrarları önler; ilk atakta '
                                         'görüntüleme gerekmez.',
                          'new_finding': 'Sefaleksin ve polietilen glikol başlandı, tuvalet programı anlatıldı. '
                                         'Kültürde 100.000 cfu/mL sefaleksine duyarlı E. coli üredi. 48 saatte '
                                         'yakınmaları geçti; bir ay sonra dışkılaması düzenliydi ve yeni atak olmadı.'},
                         {'text': 'Ondört gün amoksisilin-klavulanat vermek, tekrarları önlemek için altı ay düşük doz '
                                  'trimetoprim-sülfametoksazol proflaksisi başlamak ve işeme sistoüretrografisi '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'İlk ateşsiz atakta uzun tedavi, proflaksi ve invaziv görüntüleme '
                                             'gereksizdi; çocukta proflaksi sırasında döküntü gelişti.',
                          'teaching_point': 'Proflaksi ve işeme sistoüretrografisi ilk ateşsiz enfeksiyonda rutin '
                                            'önerilmez.'},
                         {'text': 'Kültür sonucu gelene kadar antibiyotik vermeyip bol su içmesini önermek, kızılcık '
                                  'suyu ve idrar alkalileştirici şurup ile semptomları gidermeye çalışmak',
                          'is_correct': False,
                          'scenario_update': 'İki gün tedavisiz kalan çocuğun yakınmaları arttı ve ateşi çıktı.',
                          'teaching_point': 'Semptomatik ve piyürisi olan çocukta kültür alındıktan sonra ampirik '
                                            'tedavi geciktirilmemelidir.'}]}]},
 {'id': 'G64',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '11 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Temmuz öğleden sonrası açık sahada futbol oynadıktan sonra başlayan baş dönmesi, halsizlik, bulantı ve '
               'aşırı terleme',
  'history': "Antrenörü anlatıyor: 'Saat 14:00'te güneş altında iki saattir maç yapıyorlardı. Sona doğru başı döndü, "
             'dizleri boşaldı ve yere oturdu. Çok terliyor, forması sırılsıklam. Bir şişe su içince bir kez kustu. '
             "Bizi tanıyor, sorulara doğru cevap veriyor. Bayılmadı, kasılmadı.' Bilinen hastalığı ve düzenli ilacı "
             'yok. Tartı: 38 kg.',
  'final_diagnosis': 'Sıcak Bitkinliği (Isıya Bağlı Hastalık, Santral Sinir Sistemi Tutulumu Olmayan)',
  'disposition': 'Yeşil Alanda Serin Ortamda Soğutma, Oral Elektrolitli Sıvı ve Sıcakta Egzersiz Eğitimi ile '
                 'Taburculuk',
  'case_pearl': 'Isıya bağlı hastalıkta en kritik ayrım santral sinir sistemi tutulumudur: sıcak çarpmasında vücut iç '
                "ısısı genellikle >40°C'dir ve bilinç değişikliği, konfüzyon, ataksi veya nöbet görülür; acil soğuk "
                "suya daldırma gerekir. Sıcak bitkinliğinde bilinç normaldir, iç ısı genellikle <40°C'dir; serin "
                'ortam, soyma, evaporatif soğutma ve oral elektrolitli sıvı yeterlidir. Aksiller ölçüm güvenilmez, '
                'rektal ölçüm tercih edilir. Antipiretikler etkisizdir. Aşırı sade su hiponatremiye yol açabilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Sıcakta egzersiz sonrası baş dönmesi ve kusması olan bu çocukta ilk yaklaşımınız nedir?',
             'options': [{'text': 'Çocuğu hemen serin bir odaya alıp formasını çıkarmak, rektal ısı ölçmek, '
                                  'bilinç-davranış, nörolojik bulgular, vital bulgular ve kan şekerini değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Isıya bağlı hastalıkta soğutmaya başlamak ve iç ısıyı doğru ölçmek eş '
                                         'zamanlı yapılır. Bilinç değişikliği, konfüzyon veya ataksi santral sinir '
                                         'sistemi tutulumunu gösterir ve yaklaşımı tamamen değiştirir.',
                          'new_finding': 'Vital Bulgular: Rektal ısı 38.9°C, KTA 112/dk, SS 22/dk, SpO2 %99, TA 100/62 '
                                         'mmHg, kapiller kan şekeri 92 mg/dL. Bilinç açık, oryante, konuşması akıcı. '
                                         'Yürüyüşü dengeli, nörolojik muayene normal. Cilt nemli ve terli, mukozalar '
                                         'hafif kuru, KDZ 2.5 sn.'},
                         {'text': 'Kusma nedeniyle önce intravenöz yol açıp 20 mL/kg serum fizyolojik bolus başlatmak '
                                  've sıvı bitene kadar çocuğu sedyede sıcak bekleme alanında tutmak',
                          'is_correct': False,
                          'scenario_update': 'Sıvı verilirken çocuk sıcak ortamda kaldı; iç ısı ölçülmedi ve soğutma '
                                             'gecikti.',
                          'teaching_point': 'İlk öncelik serin ortama alma ve soğutmadır; oral alabilen çocukta '
                                            'intravenöz sıvı zorunlu değildir.'},
                         {'text': 'Baş dönmesi ve kusma nedeniyle kafa travması olasılığını düşünüp boyunluk takmak ve '
                                  'nörolojik değerlendirme için çocuğu sırtüstü sabitlemek',
                          'is_correct': False,
                          'scenario_update': 'Öyküde travma yoktu; boyunluk ve sabitleme sırasında çocuk terlemeye '
                                             'devam etti ve soğutma başlamadı.',
                          'teaching_point': 'Travma öyküsü olmayan çocukta omurga immobilizasyonu gereksizdir ve '
                                            'tedaviyi geciktirir.'},
                         {'text': 'Aksiller ısı 38.2°C olduğu için ateşi düşürmek amacıyla oral parasetamol vermek, '
                                  'yarım saat bekleyip ısı düşmezse ibuprofen eklemek',
                          'is_correct': False,
                          'scenario_update': 'Antipiretik ısıyı düşürmedi; iç ısı ölçülmeden ve soğutma başlanmadan '
                                             'yarım saat geçti.',
                          'teaching_point': 'Isıya bağlı hastalıkta yükseklik hipotalamik ayar noktasından '
                                            'kaynaklanmaz; antipiretikler etkisizdir, fiziksel soğutma gerekir.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Bilinci tamamen açık, rektal ısısı 38.9°C ve hafif dehidrate olan bu çocukta tetkik '
                         'yaklaşımınız nedir?',
             'options': [{'text': 'Kan şekeri, sodyum-potasyum, böbrek fonksiyonları ve kreatin kinaz ile idrar '
                                  'dansitesi bakmak; soğutmayı sürdürüp ısıyı 15-30 dakikada bir izlemek',
                          'is_correct': True,
                          'explanation': 'Kusma ve aşırı terlemeyle sodyum değişikliği, prerenal azotemi ve '
                                         'rabdomiyoliz gelişebilir. Seri ısı ölçümü soğutmaya yanıtı ve kötüleşmeyi '
                                         'gösterir.',
                          'new_finding': 'Glukoz 88 mg/dL, Na 137 mEq/L, K 4.1 mEq/L, BUN 16 mg/dL, kreatinin 0.6 '
                                         'mg/dL, CK 210 U/L. İdrar dansitesi 1028, miyoglobin negatif. 30. dakikada '
                                         'rektal ısı 38.1°C.'},
                         {'text': 'Ateş nedeniyle enfeksiyon odağı aramak amacıyla kan kültürü, CRP ve akciğer grafisi '
                                  'istemek, sonuç gelene kadar ampirik antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'Tetkikler normal geldi; gereksiz antibiyotik başlandı ve tablo '
                                             'egzersiz-ısı ilişkisi göz ardı edildi.',
                          'teaching_point': 'Sıcakta egzersizle başlayan ve soğutmaya yanıt veren tabloda enfeksiyon '
                                            'tetkiki rutin değildir.'},
                         {'text': 'Tetkik istemeden çocuğu yarım saat gölgede dinlendirip baş dönmesi geçince '
                                  'antrenmana dönmesine izin vermek',
                          'is_correct': False,
                          'scenario_update': 'Elektrolit ve hidrasyon durumu değerlendirilmeden antrenmana dönen çocuk '
                                             'yeniden baş dönmesi yaşadı.',
                          'teaching_point': 'Isıya bağlı hastalık sonrası aynı gün egzersize dönüş önerilmez.'},
                         {'text': 'Baş dönmesi ve kusma birlikteliği nedeniyle kontrastsız beyin tomografisi çekmek, '
                                  'ardından ateş ve kusma için lomber ponksiyon planlamak',
                          'is_correct': False,
                          'scenario_update': 'Bilinci açık, nörolojik muayenesi normal çocuğa gereksiz görüntüleme ve '
                                             'invaziv işlem planlandı.',
                          'teaching_point': 'Normal nörolojik muayenesi olan çocukta görüntüleme ve lomber ponksiyon '
                                            'endike değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Sıcakta uzun egzersiz sonrası baş dönmesi, bulantı, aşırı terleme, bilinci açık ve rektal '
                         'ısısı 38.9°C olan bu çocukta tanı nedir?',
             'options': [{'text': 'Sıcak bitkinliği',
                          'is_correct': True,
                          'explanation': 'Sıcakta egzersiz sonrası halsizlik, baş dönmesi, bulantı-kusma, terleme ve '
                                         'hafif dehidratasyon ile birlikte normal bilinç ve 40°C altı iç ısı sıcak '
                                         'bitkinliğini tanımlar.',
                          'new_finding': 'Tanı: Sıcak Bitkinliği.'},
                         {'text': 'Sıcak çarpması',
                          'is_correct': False,
                          'scenario_update': "Bilinç ve nörolojik muayene normal, iç ısı 40°C'nin altında.",
                          'teaching_point': 'Sıcak çarpmasında santral sinir sistemi bulguları vardır ve hayatı tehdit '
                                            'eder.'},
                         {'text': 'Akut viral gastroenterit',
                          'is_correct': False,
                          'scenario_update': 'Yakınmalar sıcakta egzersizle başladı, ishal yok ve soğutmayla hızla '
                                             'düzeliyor.',
                          'teaching_point': 'Bağlamın (ısı, egzersiz) değerlendirilmesi tanının anahtarıdır.'},
                         {'text': 'Egzersize bağlı hiponatremi',
                          'is_correct': False,
                          'scenario_update': 'Serum sodyumu 137 mEq/L, normal.',
                          'teaching_point': 'Egzersize bağlı hiponatremi genellikle aşırı sade su alımıyla gelişir ve '
                                            "sodyum <135 mEq/L'dir."}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuğun tedavisi ve taburculuk önerileri nasıl olmalıdır?',
             'options': [{'text': 'Kaybedilen sıvıyı hızla yerine koymak için çocuğa yarım saat içinde iki litre sade '
                                  'su içirmek ve terleme geçince aynı gün maça dönmesine izin vermek',
                          'is_correct': False,
                          'scenario_update': 'Hızlı sade su alımı sonrası bulantı arttı ve yeniden kustu; aynı gün '
                                             'egzersize dönüş riskliydi.',
                          'teaching_point': 'Kısa sürede aşırı sade su hiponatremi riski taşır; elektrolitli sıvı azar '
                                            'azar verilmelidir.'},
                         {'text': 'Serin ortamda nemli bez ve fanla soğutmak, azar azar soğuk oral elektrolitli sıvı '
                                  'vermek; sıcakta egzersiz saatleri, sıvı molaları ve uyarı belirtilerini anlatmak',
                          'is_correct': True,
                          'explanation': 'Evaporatif soğutma ve oral rehidratasyon sıcak bitkinliğinde yeterlidir. '
                                         'Günün sıcak saatlerinden kaçınma, düzenli sıvı molası, açık renkli giysi ve '
                                         'kademeli alışma tekrarları önler; konfüzyon gelişirse acil başvuru gerekir.',
                          'new_finding': "Bir saatte rektal ısı 37.4°C'ye, nabız 82/dk'ya geriledi; baş dönmesi geçti, "
                                         'iki bardak elektrolitli sıvıyı kusmadan içti. Antrenöre ve aileye öneriler '
                                         'yazılı verildi.'},
                         {'text': 'Aktif soğutma için çocuğu buzlu suya daldırıp titreme başlayana kadar tutmak ve '
                                  'ardından intravenöz parasetamol ile ısıyı kontrol altında tutmak',
                          'is_correct': False,
                          'scenario_update': 'Bilinci açık çocuk buzlu suda şiddetli titreme ve huzursuzluk yaşadı; '
                                             'parasetamol ısıyı etkilemedi.',
                          'teaching_point': 'Soğuk suya daldırma sıcak çarpmasında hayat kurtarıcıdır; sıcak '
                                            'bitkinliğinde evaporatif soğutma yeterlidir ve antipiretikler '
                                            'etkisizdir.'},
                         {'text': 'Çocuğu 24 saat gözlem için yatırıp intravenöz idame sıvısı başlamak, ertesi gün '
                                  'tekrar elektrolit ve böbrek fonksiyon testleri istemek',
                          'is_correct': False,
                          'scenario_update': 'Bir saatte tamamen düzelen çocuk gereksiz yere yatırıldı ve tetkikler '
                                             'tekrarlandı.',
                          'teaching_point': 'Soğutma ve oral sıvıyla düzelen, laboratuvarı normal çocuk taburcu '
                                            'edilebilir.'}]}]},
 {'id': 'G65',
  'category': '👁️ Göz Şikayetleri',
  'age': '5 Yaşında',
  'gender': 'Kız',
  'complaint': 'Sağ göz kapaklarında iki gündür giderek artan kızarıklık, şişlik ve dokunmakla hassasiyet',
  'history': "Annesi anlatıyor: 'Üç gün önce sağ kaşının kenarını sivrisinek ısırdı, çok kaşıdı. Dünden beri sağ üst "
             've alt göz kapağı kızardı, şişti, gözü biraz kapandı. Gözünün akı kızarık değil, akıntısı yok. Çizgi '
             "filmi net gördüğünü söylüyor, gözünü oynatınca acımıyor. Ateşi 37.4°C oldu.' Burun akıntısı veya sinüzit "
             'öyküsü yok. Aşıları tam. Tartı: 19 kg.',
  'final_diagnosis': 'Preseptal Selülit (Cilt Bütünlüğü Bozulmasına Sekonder)',
  'disposition': 'Yeşil Alandan Oral Antibiyotik, Alarm Bulguları Eğitimi ve 24-48 Saat Sonra Kontrol ile Taburculuk',
  'case_pearl': 'Göz kapağı selülitinde asıl görev orbital tutulumu dışlamaktır: proptozis, ağrılı veya kısıtlı göz '
                'hareketleri, görme azalması, RAPD ve kemozis orbital selülit bulgularıdır ve kontrastlı orbita BT ile '
                'acil yatış gerektirir. Bu bulgular yoksa ve çocuk iyi görünümlüyse görüntüleme gerekmez. Cilt '
                'kaynaklı olgularda S. aureus ve A grubu streptokoku kapsayan oral tedavi (sefaleksin veya '
                'amoksisilin-klavulanat; MRSA riskinde klindamisin veya TMP-SMX) 7-10 gün verilir ve 24-48 saatte '
                'kontrol edilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Göz kapaklarında kızarıklık ve şişliği olan bu 5 yaşındaki kızda muayenede öncelikle neyi '
                         'değerlendirirsiniz?',
             'options': [{'text': 'Ateşli kapak şişliğinde menenjit riskini dışlamak amacıyla önce ense sertliği ve '
                                  'Kernig-Brudzinski bulgularına odaklanmak, göz muayenesini oftalmolojiye bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Meninks bulguları negatifti; görme ve göz hareketleri değerlendirilmeden '
                                             'göz konsültasyonu için saatlerce beklendi.',
                          'teaching_point': 'Göz kapağı enfeksiyonunun ilk değerlendirmesinde orbital bulgular acil '
                                            'hekimi tarafından kontrol edilmelidir.'},
                         {'text': 'Görme keskinliği, pupilla refleksleri ve RAPD, göz hareketlerinde ağrı veya '
                                  'kısıtlılık, proptozis ve kemoziyi değerlendirip cilt giriş kapısını ve sinüs '
                                  'bulgularını aramak',
                          'is_correct': True,
                          'explanation': 'Göz kapağı enfeksiyonunda hayatı ve görmeyi tehdit eden durum septum '
                                         'arkasına yayılımdır. Görme, pupilla, göz hareketleri, proptozis ve kemozi bu '
                                         'ayrımın temelidir; giriş kapısı olası etkeni ve tedavi seçimini belirler.',
                          'new_finding': 'Vital Bulgular: Ateş 37.3°C, KTA 92/dk, SS 20/dk, SpO2 %99. Genel durumu '
                                         'iyi. Sağ üst ve alt kapakta eritem, ödem ve hafif hassasiyet; kaş kenarında '
                                         'kaşıntıya bağlı ekskoriasyon. Göz hareketleri her yöne tam ve ağrısız, '
                                         'proptozis yok, kemozis yok. Görme keskinliği her iki gözde tam, pupillalar '
                                         'izokorik, RAPD yok. Burun akıntısı ve sinüs hassasiyeti yok.'},
                         {'text': 'Kapaklar şiş ve çocuk huzursuz olduğu için gözü açmaya zorlamadan sıcak kompres '
                                  'uygulamak, ödem azaldıktan sonra yarın ayrıntılı göz muayenesi için göz '
                                  'polikliniğine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Görme, pupilla ve göz hareketleri değerlendirilmeden çocuk '
                                             'gönderilecekti; orbital tutulum dışlanmamıştı.',
                          'teaching_point': 'Şiş kapak muayeneyi zorlaştırsa da kapak nazikçe açılarak görme ve göz '
                                            'hareketleri mutlaka değerlendirilmelidir.'},
                         {'text': 'Sivrisinek ısırığı öyküsü nedeniyle tabloyu alerjik reaksiyon kabul edip oral '
                                  'antihistaminik vermek ve göz muayenesine gerek görmeden taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Hassasiyet ve ateş göz ardı edildi; enfeksiyon olasılığı ve orbital '
                                             'bulgular değerlendirilmedi.',
                          'teaching_point': 'Alerjik ödem genellikle kaşıntılı ve ağrısızdır; hassasiyet ve ateş '
                                            'enfeksiyonu düşündürür.'}]},
            {'stage_title': 'Tetkik ve Görüntüleme Kararı',
             'question': 'Orbital bulgusu olmayan, iyi görünümlü bu çocukta tetkik yaklaşımınız nedir?',
             'options': [{'text': 'Göz kapağı ödemi ve ateşi olan her çocukta septum arkasına yayılımı kesin olarak '
                                  'dışlamak için acil kontrastlı orbita ve sinüs bilgisayarlı tomografisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi normal geldi; çocuk gereksiz radyasyon ve kontrast maddeye '
                                             'maruz kaldı.',
                          'teaching_point': 'Orbita BT orbital bulgu varlığında, muayene yapılamadığında veya 24-48 '
                                            'saatte yanıt alınamadığında endikedir.'},
                         {'text': 'Kan kültürü, tam kan sayımı ve CRP almak, değerler yüksekse çocuğu yatırıp '
                                  'intravenöz antibiyotik başlamak üzere planlama yapmak',
                          'is_correct': False,
                          'scenario_update': 'Lökosit 8.400/mm³, CRP hafif yüksek geldi; kan kültürü negatifti ve '
                                             'tetkikler yönetimi değiştirmedi.',
                          'teaching_point': 'İyi görünümlü çocukta kan kültürünün verimi çok düşüktür; yatış kararı '
                                            'klinik bulgulara dayanır.'},
                         {'text': 'Sedasyon altında orbita manyetik rezonansı ve göz içi basıncı ölçümü yaptırmak, '
                                  'sonuçlar normalse oral tedaviyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Sedasyon için çocuğun aç kalması gerekti ve tedavi saatlerce gecikti.',
                          'teaching_point': 'MR ve göz içi basıncı ölçümü bu klinik tabloda gereksizdir.'},
                         {'text': 'Görüntüleme veya kan tetkiki istemeden klinik tanıyla tedaviyi planlamak, orbital '
                                  'bulguların yokluğunu kayıt altına almak ve kontrol zamanını belirlemek',
                          'is_correct': True,
                          'explanation': 'Orbital bulgusu olmayan, sistemik olarak iyi ve muayenesi güvenilir çocukta '
                                         'tanı kliniktir. Tetkikler yönetimi değiştirmez; asıl güvenlik önlemi yakın '
                                         'klinik izlemdir.',
                          'new_finding': 'Tetkik istenmedi. Muayene bulguları ve kapak eritem sınırı kalemle '
                                         'işaretlenerek kayda geçirildi.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Böcek ısırığı ve kaşıma sonrası göz kapaklarında hassas eritem-ödem, ağrısız ve tam göz '
                         'hareketleri, normal görme ve proptozis yokluğu olan bu çocukta tanı nedir?',
             'options': [{'text': 'Preseptal selülit',
                          'is_correct': True,
                          'explanation': 'Cilt bütünlüğü bozulması sonrası gelişen, septum önüyle sınırlı hassas '
                                         'eritem-ödem ve normal orbital muayene preseptal selülitle uyumludur.',
                          'new_finding': 'Tanı: Preseptal Selülit (cilt kaynaklı).'},
                         {'text': 'Böcek ısırığına lokal alerjik reaksiyon',
                          'is_correct': False,
                          'scenario_update': 'Lezyon hassas, ateş var ve eritem giderek yayılıyor.',
                          'teaching_point': 'Alerjik reaksiyon kaşıntılı, hassasiyetsiz ve ateşsizdir.'},
                         {'text': 'Akut dakriyosistit',
                          'is_correct': False,
                          'scenario_update': 'Şişlik iç kantusta lokalize değil ve gözyaşı kesesinden akıntı yok.',
                          'teaching_point': 'Dakriyosistit medial kantusta, gözyaşı kesesi üzerinde hassas şişlikle '
                                            'seyreder.'},
                         {'text': 'Orbital selülit',
                          'is_correct': False,
                          'scenario_update': 'Proptozis, ağrılı veya kısıtlı göz hareketi, görme kaybı ve kemozis yok.',
                          'teaching_point': 'Orbital selülit septum arkasına yayılımdır ve orbital bulgularla kendini '
                                            'gösterir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuğun tedavi ve izlem planı hangisidir?',
             'options': [{'text': 'Yalnızca antibiyotikli göz damlası ve göz merhemi reçete etmek, kapağa günde birkaç '
                                  'kez soğuk kompres önermek ve şişlik geçmezse bir hafta sonra kontrole gelmesini '
                                  'söylemek',
                          'is_correct': False,
                          'scenario_update': 'Topikal tedavi yumuşak doku enfeksiyonuna ulaşmadı; iki gün sonra eritem '
                                             'yanağa doğru yayıldı.',
                          'teaching_point': 'Preseptal selülit yumuşak doku enfeksiyonudur ve sistemik antibiyotik '
                                            'gerektirir.'},
                         {'text': 'Oral sefaleksin veya amoksisilin-klavulanat ile 7-10 gün tedavi, eritem sınırını '
                                  'izlemek, görme bozukluğu veya ağrılı göz hareketinde acil başvuru ve 24-48 saatte '
                                  'kontrol',
                          'is_correct': True,
                          'explanation': 'Cilt kaynaklı preseptal selülitte S. aureus ve A grubu streptokoku kapsayan '
                                         'oral tedavi yeterlidir. Alarm bulguları ve 24-48 saatlik kontrol orbital '
                                         'yayılımı erken yakalamayı sağlar; yanıt yoksa görüntüleme ve yatış '
                                         'düşünülür.',
                          'new_finding': 'Oral sefaleksin başlandı, alarm bulguları anlatıldı. 48. saat kontrolünde '
                                         'eritem işaretli sınırın gerisine çekilmişti, göz kolayca açılıyordu; tedavi '
                                         '7 güne tamamlandı.'},
                         {'text': 'Ödemi hızla azaltmak için oral prednizolon ve antihistaminik başlamak, antibiyotiği '
                                  "ancak ateş 38.5°C'yi geçerse vermek üzere aileye reçete etmek",
                          'is_correct': False,
                          'scenario_update': 'Steroid ödemi kısa süre azalttı ancak enfeksiyon ilerledi; ertesi gün '
                                             'kapak eritemi belirgin şekilde genişledi.',
                          'teaching_point': 'Bakteriyel yumuşak doku enfeksiyonunda tedavinin temeli antibiyotiktir; '
                                            'steroidlerin yeri yoktur.'},
                         {'text': 'Çocuğu servise yatırıp intravenöz seftriakson ve vankomisin başlamak, orbita BT ile '
                                  'izlemek ve en az beş gün intravenöz tedaviyi sürdürmek',
                          'is_correct': False,
                          'scenario_update': 'İyi görünümlü çocuk gereksiz yere yatırıldı ve geniş spektrumlu '
                                             'parenteral tedavi aldı.',
                          'teaching_point': 'Yatış küçük bebeklerde, toksik görünümde, oral tolere edemeyende veya '
                                            'ayaktan tedaviye yanıtsızlıkta gerekir.'}]}]},
 {'id': 'G66',
  'category': '👶 Ağlayan, Emmeyen, Huzursuz Bebek',
  'age': '2 Aylık',
  'gender': 'Erkek',
  'complaint': 'Her dışkılama öncesi 15-20 dakika yüzü kızararak ıkınma, ağlama ve bacaklarını karnına çekme',
  'history': "Ebeveynleri anlatıyor: 'Yalnızca anne sütü alıyor. İki haftadır kaka yapmadan önce yüzü kıpkırmızı olana "
             'kadar ıkınıyor, 15-20 dakika ağlıyor. Sonunda yaptığı kaka yumuşacık, hardal sarısı. Yapınca hemen '
             'sakinleşiyor. Kabız diye makatına yağlı kulak çubuğu soktuk, gliserinli fitil verdik ama her seferinde '
             "aynı şey oluyor.' Doğumdan sonraki ilk gün mekonyum çıkarmış. Kusma ve ateş yok. Ayda 900 g alıyor. "
             'Tartı: 5.4 kg.',
  'final_diagnosis': 'İnfant Diskezi (Roma IV)',
  'disposition': 'Yeşil Alandan Fizyolojik Sürecin Açıklanması ve Rektal Uyarıların Bırakılması Eğitimi ile Taburculuk',
  'case_pearl': '9 aylıktan küçük, sağlıklı bebekte yumuşak dışkı çıkarmadan önce en az 10 dakika süren ıkınma ve '
                'ağlama, karın içi basınç artışı ile pelvik taban gevşemesinin henüz koordine olmamasından kaynaklanır '
                '(Roma IV). Dışkının yumuşak olması kabızlığı dışlar. Mekonyumun gecikmemesi, normal büyüme ve normal '
                'muayene güvence verir. Rektal uyarı (çubuk, termometre, fitil) bebeği dışkılama için dış uyarıya '
                'koşullandırabileceğinden bırakılmalıdır; laksatif gerekmez.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Dışkılama öncesi uzun süre ıkınan ve ağlayan bu 2 aylık bebekte öykü ve muayenede neye '
                         'odaklanırsınız?',
             'options': [{'text': 'Mekonyum çıkış zamanını, büyüme eğrisini ve dışkı kıvamını sorgulamak; karın '
                                  'distansiyonu, anüs yeri ve çapı, fissür, anal refleks ve lumbosakral bölgeyi '
                                  'muayene etmek',
                          'is_correct': True,
                          'explanation': 'Mekonyum gecikmesi, büyüme geriliği, distansiyon ve anal anomali organik '
                                         'nedenleri (Hirschsprung, anorektal malformasyon, spinal disrafizm) '
                                         'düşündürür. Dışkının yumuşak olması gerçek kabızlığı dışlar.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 128/dk, SS 34/dk. Tartı 5.4 kg (50. '
                                         'persentil). Bebek sakin, gülümsüyor. Karın yumuşak, distansiyon ve kitle '
                                         'yok. Anüs normal yerleşimli ve normal çaplı, fissür yok; anal refleks canlı. '
                                         'Lumbosakral bölgede gamze, kıl tutamı veya leke yok.'},
                         {'text': 'Ikınmayı kabızlık kabul edip ayrıntılı muayeneye gerek görmeden laktüloz şurubu '
                                  'başlamak, gliserinli fitili her dışkılamada sürdürmelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'Laktüloz sonrası dışkı sulandı, gaz ve huzursuzluk arttı; ıkınma süresi '
                                             'değişmedi.',
                          'teaching_point': 'Yumuşak dışkı kabızlık değildir; laksatif ve rektal uyarı gereksizdir.'},
                         {'text': 'Ağlama atakları ve bacaklarını karnına çekmesi nedeniyle invajinasyonu düşünüp acil '
                                  'karın ultrasonografisi istemek ve sonuç gelene kadar emzirmeye ara verip bebeği aç '
                                  'bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografi normal geldi; iyi görünümlü bebek iki saat aç bekletildi.',
                          'teaching_point': 'Yalnızca dışkılamayla ilişkili, dışkı çıkınca geçen yakınmada '
                                            'invajinasyon düşünülmez; 2 aylık bebekte de nadirdir.'},
                         {'text': 'Annenin beslenmesinin bebekte gaz yaptığını düşünüp anneye süt, baklagil ve sebze '
                                  'içermeyen kısıtlı diyet önermek ve bir hafta sonra kontrol etmek',
                          'is_correct': False,
                          'scenario_update': 'Annenin kısıtlı diyeti emzirmeyi zorlaştırdı; bebeğin yakınmaları '
                                             'değişmedi.',
                          'teaching_point': 'Kanıt olmadan annenin diyetini kısıtlamak emzirmeyi tehlikeye atar.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Büyümesi normal, mekonyumu zamanında çıkmış, muayenesi normal ve dışkısı yumuşak olan bu '
                         'bebekte tetkik yaklaşımınız nedir?',
             'options': [{'text': 'Tiroid fonksiyon testleri, serum kalsiyum, elektrolitler ve çölyak serolojisi '
                                  'isteyip normal çıkarsa fonksiyonel bir sorun olduğunu söylemek',
                          'is_correct': False,
                          'scenario_update': 'Tetkikler normal geldi; yenidoğan taraması zaten normaldi ve kan alımı '
                                             'bebeği çok huzursuz etti.',
                          'teaching_point': 'Yalnızca anne sütü alan 2 aylık bebekte çölyak serolojisi anlamsızdır; '
                                            'metabolik tetkikler bu tabloda gereksizdir.'},
                         {'text': 'Hirschsprung hastalığını dışlamak için kontrastlı kolon grafisi ve rektal emme '
                                  'biyopsisi planlamak, sonuçlara göre aileye bilgi vermek',
                          'is_correct': False,
                          'scenario_update': 'Kolon grafisi normal geldi; biyopsi ailenin onayıyla iptal edildi ancak '
                                             'bebek gereksiz radyasyona maruz kaldı.',
                          'teaching_point': 'Zamanında mekonyum, yumuşak dışkı ve normal büyüme Hirschsprung '
                                            'olasılığını çok düşürür.'},
                         {'text': 'Anorektal manometri ile sfinkter fonksiyonunu değerlendirmek için çocuk '
                                  'gastroenterolojisine sevk etmek ve bu sürede fitile devam etmelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'Sevk randevusu haftalar sonrasına verildi; fitil uygulamasına devam '
                                             'edildi.',
                          'teaching_point': 'Manometri bu tabloda endike değildir; rektal uyarı bırakılmalıdır.'},
                         {'text': 'Kırmızı bayrakların yokluğunu aileyle gözden geçirip herhangi bir tetkik istememek '
                                  've yakınmaların fizyolojik nedenini açıklamaya hazırlanmak',
                          'is_correct': True,
                          'explanation': 'Safralı kusma, distansiyon, mekonyum gecikmesi, büyüme geriliği, kanlı dışkı '
                                         've anal anomali yokluğunda tanı kliniktir. Tetkik yönetimi değiştirmez ve '
                                         'aile kaygısını artırabilir.',
                          'new_finding': 'Kırmızı bayrak saptanmadı. Tetkik istenmedi; ebeveynler gözlem sırasında '
                                         'bebeğin ıkınma sonrası yumuşak dışkı yaptığını ve hemen rahatladığını '
                                         'gördü.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Sağlıklı, iyi büyüyen 2 aylık bebekte yumuşak dışkı çıkarmadan önce 10 dakikadan uzun ıkınma '
                         've ağlama varsa tanı nedir?',
             'options': [{'text': 'Hirschsprung hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Mekonyum ilk gün çıkmış, distansiyon yok, büyüme normal.',
                          'teaching_point': 'Hirschsprung hastalığı gecikmiş mekonyum, distansiyon ve kusmayla '
                                            'seyreder.'},
                         {'text': 'Fonksiyonel kabızlık',
                          'is_correct': False,
                          'scenario_update': 'Dışkı yumuşak ve kıvamı normal; sert, ağrılı dışkılama yok.',
                          'teaching_point': 'Kabızlık tanısı sert ve seyrek dışkılama gerektirir.'},
                         {'text': 'Akut anal fissür',
                          'is_correct': False,
                          'scenario_update': 'Perianal muayenede fissür yok, dışkıda kan yok.',
                          'teaching_point': 'Fissürde ağrılı dışkılama ve dışkı üzerinde parlak kırmızı kan görülür.'},
                         {'text': 'İnfant diskezi',
                          'is_correct': True,
                          'explanation': "Roma IV'e göre 9 aydan küçük, sağlıklı bebekte yumuşak dışkı çıkarmadan önce "
                                         'en az 10 dakika süren ıkınma ve ağlama infant diskezisidir.',
                          'new_finding': 'Tanı: İnfant Diskezi.'}]},
            {'stage_title': 'Aile Eğitimi ve Taburculuk',
             'question': 'Bu bebeğin ailesine hangi öneriyi verirsiniz?',
             'options': [{'text': 'Simetikon damla ve probiyotik başlamak, karın masajını her öğünden sonra '
                                  'yapmalarını önermek ve yakınma sürerse iki hafta sonra laktüloza geçmek',
                          'is_correct': False,
                          'scenario_update': 'Damla ve probiyotik yakınmayı değiştirmedi; aile laktüloz için yeniden '
                                             'başvurdu.',
                          'teaching_point': 'Bu tabloda ilaç tedavisinin yararı yoktur; güvence verme ve eğitim '
                                            'yeterlidir.'},
                         {'text': 'Dışkılamayı kolaylaştırmak için her ağlama ataklarında makata termometre ucu ile '
                                  'nazikçe uyarı vermelerini ve günde bir kez gliserinli fitil kullanmalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Bebek her dışkılama için uyarıya ihtiyaç duyar hale geldi; yakınmalar '
                                             'uzadı.',
                          'teaching_point': 'Rektal uyarı bebeğin doğal dışkılama koordinasyonunu öğrenmesini '
                                            'geciktirir.'},
                         {'text': 'Durumun birkaç haftada kendiliğinden geçeceğini açıklamak, çubuk-fitil gibi rektal '
                                  'uyarıları bırakmalarını ve emzirmeye aynı şekilde devam etmelerini önermek',
                          'is_correct': True,
                          'explanation': 'Bebek zamanla karın içi basıncını artırırken pelvik tabanı gevşetmeyi '
                                         'öğrenir. Rektal uyarılar bu öğrenmeyi geciktirir ve bebeği dış uyarıya '
                                         'koşullandırabilir; laksatif ve diyet değişikliği gerekmez.',
                          'new_finding': 'Rektal uyarılar bırakıldı. Üç hafta sonraki kontrolde bebek ağlamadan, kısa '
                                         'sürede yumuşak dışkı yapıyordu.'},
                         {'text': 'Anne sütünün yetersiz olabileceğini düşünüp hidrolize formül mamaya geçmelerini ve '
                                  'dışkıyı yumuşatmak için günde iki kez meyve suyu vermelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'Emzirme azaldı, bebek mamayı reddetti ve 2 aylık bebeğe meyve suyu '
                                             'verildi.',
                          'teaching_point': 'Emzirme sürdürülmeli; 6 aydan küçük bebeğe meyve suyu önerilmez.'}]}]},
 {'id': 'G67',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '18 Aylık',
  'gender': 'Kız',
  'complaint': 'Bez değişiminde vajina girişinin kapalı göründüğünün fark edilmesi ve idrarın ince bir çizgi halinde '
               'öne doğru fışkırması',
  'history': "Annesi anlatıyor: 'Dün akşam bezini değiştirirken vajina girişi sanki yokmuş gibi, kapanmış gördüm. "
             'Çişini yaparken idrar ince bir çizgi gibi öne doğru fışkırıyor, bazen bezi idrardan sonra da damlıyor. '
             'Ateşi yok, ağlamadan çiş yapıyor. Bez bölgesinde sık sık pişik oluyordu. Doğduğunda her şey normaldi, '
             "sonradan mı kapandı, ameliyat mı gerekecek çok korktuk.' Büyüme gelişmesi normal. Tartı: 11 kg.",
  'final_diagnosis': 'Labial Yapışıklık (Sinekşi)',
  'disposition': 'Yeşil Alandan Topikal Östrojen ve Nazik Uygulama Eğitimi, Sonrasında Bariyer Merhem ile Taburculuk',
  'case_pearl': 'Bebeklik ve erken çocuklukta düşük östrojen düzeyi ve pişik gibi kronik irritasyonlar labia '
                'minoraların orta hatta ince, avasküler bir zarla yapışmasına yol açabilir. Klitoris ve diğer genital '
                'yapılar normaldir; bu ayrım konjenital anomalilerden ve cinsel gelişim bozukluklarından ayırmada '
                'temeldir. Asemptomatik olgularda tedavi gerekmez. İdrar akımı bozuluyorsa veya enfeksiyon varsa 2-6 '
                'hafta topikal östrojen ilk seçenektir; zorla ayırma ağrılıdır ve tekrar riskini artırır. Ayrılma '
                'sonrası bariyer merhem tekrarları azaltır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Vajina girişinin kapalı göründüğü ve idrar akımı değişen bu 18 aylık kızda muayenede neye '
                         'dikkat edersiniz?',
             'options': [{'text': 'Kapalı vajina girişinin cinsel istismara bağlı skar dokusu olduğunu varsayıp adli '
                                  'bildirimi yapmak ve genital muayeneyi adli tıp uzmanına bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Adli muayenede travma bulgusu saptanmadı; aile yersiz şüphe nedeniyle '
                                             'ağır bir süreç yaşadı.',
                          'teaching_point': 'İnce, avasküler orta hat zarı tipik olarak edinsel benign bir durumdur; '
                                            'istismar şüphesi somut bulgulara dayanmalıdır.'},
                         {'text': 'Labiaları nazikçe yanlara çekerek yapının niteliğini, idrar çıkış açıklığını, '
                                  'klitoris boyutunu, enfeksiyon veya travma bulgularını değerlendirmek ve istismar '
                                  'açısından öyküyü sorgulamak',
                          'is_correct': True,
                          'explanation': 'Nazik lateral traksiyonla zarın inceliği, saydamlığı ve yerleşimi görülür. '
                                         'Klitoris boyutu cinsel gelişim bozukluklarını ayırır; enfeksiyon ve travma '
                                         'bulguları ile öykü istismar şüphesini değerlendirmek için gereklidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 98/dk, SS 22/dk. Sakin. Labia minoralar '
                                         'forşetten klitorise doğru orta hatta ince, yarı saydam, avasküler bir zarla '
                                         "birleşik; en üstte 2-3 mm'lik bir açıklık var. Klitoris normal boyutta. "
                                         'Labia majoralar normal, gonad ele gelmiyor. Vulvit, akıntı, ekimoz veya '
                                         'yırtık yok.'},
                         {'text': 'Ambigus genitalya olasılığı nedeniyle muayeneyi yapmadan çocuk endokrinolojisine '
                                  'acil konsültasyon istemek ve kromozom analizi göndermek',
                          'is_correct': False,
                          'scenario_update': 'Konsültan muayenede klitorisin normal olduğunu ve endokrin tetkik '
                                             'gerekmediğini belirtti; aile gereksiz kaygı yaşadı.',
                          'teaching_point': 'Muayene yapılmadan endokrinolojik tetkik istenmez; normal klitoris ve '
                                            'gonad yokluğu kız iç genitalyasıyla uyumludur.'},
                         {'text': 'Muayeneyi kısa tutup kapalı görünen yapıyı açmak için acil serviste pamuklu çubukla '
                                  'bastırarak zarı ayırmak ve ayrılan kenarlara antibiyotikli merhem sürmek',
                          'is_correct': False,
                          'scenario_update': 'İşlem çocukta yoğun ağrı ve kanamaya neden oldu; çocuk sonraki '
                                             'muayenelerde çok korktu.',
                          'teaching_point': 'Zorla ayırma travmatiktir, ağrılıdır ve yeniden yapışma riski '
                                            'yüksektir.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'İdrar akımı değişmiş, ateşsiz ve klitorisi normal olan bu çocukta hangi tetkik uygundur?',
             'options': [{'text': 'Bozulan idrar akımı nedeniyle uygun yöntemle alınan idrardan tam idrar tetkiki '
                                  'yapmak, başka tetkik istememek',
                          'is_correct': True,
                          'explanation': 'İdrar akımının engellenmesi ve vajinal göllenme idrar yolu enfeksiyonu '
                                         'riskini artırır. Tam idrar tetkiki eşlik eden enfeksiyonu gösterir; genital '
                                         'yapılar normal olduğu için endokrin veya görüntüleme tetkiki gerekmez.',
                          'new_finding': 'Tam idrar: dansite 1018, lökosit esteraz ve nitrit negatif, mikroskopide 1-2 '
                                         'lökosit. Enfeksiyon bulgusu yok.'},
                         {'text': 'Cinsel gelişim bozukluğunu dışlamak için kromozom analizi, 17-OH progesteron, '
                                  'elektrolitler ve testosteron düzeyi istemek, sonuçlar çıkana kadar tedavi kararını '
                                  'ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Tetkikler normal geldi; çocuk birkaç hafta tedavisiz kaldı ve idrar '
                                             'akımı sorunu sürdü.',
                          'teaching_point': 'Klitoris ve labia majoraları normal çocukta cinsel gelişim bozukluğu '
                                            'tetkiki gerekmez.'},
                         {'text': 'Herhangi bir tetkik istemeden zarın kendiliğinden açılacağını söyleyip çocuğu '
                                  'ergenliğe kadar izlem için aile hekimine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'İdrar akımı bozuk olduğu halde enfeksiyon değerlendirilmedi ve tedavi '
                                             'önerilmedi.',
                          'teaching_point': 'Asemptomatik olgu izlenebilir; idrar akımı bozulmuşsa değerlendirme ve '
                                            'tedavi gerekir.'},
                         {'text': 'Pelvik ultrasonografi ile uterus ve overleri, işeme sistoüretrografisi ile üretrayı '
                                  'değerlendirmek ve sonuçlara göre çocuk cerrahisi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografi normal iç genitalya gösterdi; işeme sistoüretrografisi '
                                             'gereksiz kateterizasyon ve radyasyon içeriyordu.',
                          'teaching_point': 'Genital yapıları normal çocukta iç genital ve üriner görüntüleme '
                                            'gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Labia minoraların orta hatta ince, avasküler bir zarla birleştiği, klitorisi normal ve idrar '
                         'akımı değişen bu çocukta tanı nedir?',
             'options': [{'text': 'İmperfore himen',
                          'is_correct': False,
                          'scenario_update': 'Labia minoralar birbirine yapışık; himen düzeyinde bombeleşen bir zar '
                                             'yok.',
                          'teaching_point': 'İmperfore himen genellikle yenidoğanda veya menarş döneminde bombeleşen '
                                            'zarla saptanır.'},
                         {'text': 'Vulvar liken skleroz',
                          'is_correct': False,
                          'scenario_update': 'Vulvada beyaz, atrofik, sekiz şeklinde plak ve kaşıntı yok.',
                          'teaching_point': 'Liken skleroz kaşıntılı, porselen beyazı atrofik plaklarla seyreder.'},
                         {'text': 'Labial yapışıklık (sinekşi)',
                          'is_correct': True,
                          'explanation': 'Düşük östrojen düzeyi ve kronik irritasyon zemininde labia minoraların orta '
                                         'hatta ince avasküler zarla birleşmesi edinsel labial yapışıklıktır.',
                          'new_finding': 'Tanı: Labial Yapışıklık (Sinekşi), idrar akımını etkileyen.'},
                         {'text': 'Konjenital adrenal hiperplazi',
                          'is_correct': False,
                          'scenario_update': 'Klitoris normal, labioskrotal füzyon ve hiperpigmentasyon yok; doğumda '
                                             'genital yapı normalmiş.',
                          'teaching_point': 'Konjenital adrenal hiperplazide doğumdan itibaren klitoromegali ve '
                                            'labioskrotal füzyon görülür.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'İdrar akımı bozulan bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Topikal östrojenli kremi 2-6 hafta, günde 1-2 kez zar hattına pamuklu çubukla hafif '
                                  'bastırarak sürmek; açıldıktan sonra vazelinle bariyer sağlamak',
                          'is_correct': True,
                          'explanation': 'Topikal östrojen zarın incelmesini ve kendiliğinden ayrılmasını sağlar; '
                                         'hafif bası etkinliği artırır. Ayrılma sonrası bariyer merhem ve pişik bakımı '
                                         'tekrarı azaltır. Uzun kullanımda geçici meme tomurcuklanması ve labial '
                                         'pigmentasyon olabileceği anlatılır.',
                          'new_finding': 'Topikal östrojen ve uygulama tekniği anlatıldı. Üç hafta sonra zarın tamamen '
                                         'ayrıldığı, idrar akımının normale döndüğü görüldü; bariyer merhemle izleme '
                                         'alındı.'},
                         {'text': 'İdrar yolu enfeksiyonunu önlemek için üç ay düşük doz oral antibiyotik proflaksisi '
                                  'başlamak ve zarın kendiliğinden açılmasını beklemek',
                          'is_correct': False,
                          'scenario_update': 'Proflaksi zarı etkilemedi; idrar akımı bozukluğu sürdü ve çocukta '
                                             'gereksiz antibiyotik maruziyeti oldu.',
                          'teaching_point': 'Antibiyotik proflaksisi labial yapışmanın tedavisi değildir.'},
                         {'text': 'Ailenin evde her bez değişiminde labiaları parmaklarıyla kuvvetle yanlara çekerek '
                                  'zarı yavaş yavaş açmasını ve sonrasında antiseptik solüsyonla silmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Ev içi zorlamalar çocukta ağrı, kanama ve bez değişiminden korku '
                                             'oluşturdu; yeniden yapışma gelişti.',
                          'teaching_point': 'Zorlayıcı manipülasyon ve antiseptikler irritasyonu artırarak tekrarı '
                                            'kolaylaştırır.'},
                         {'text': 'Ağrısız ve hızlı çözüm için genel anestezi altında cerrahi olarak zarı ayırmak ve '
                                  'ardından ayrılan kenarları birkaç gün dikişle açık tutmak',
                          'is_correct': False,
                          'scenario_update': 'Cerrahi ilk basamak tedavi değildi; çocuk gereksiz anestezi riskine '
                                             'maruz kaldı.',
                          'teaching_point': 'Cerrahi ayırma yalnızca topikal tedaviye dirençli ve semptomatik '
                                            'olgularda düşünülür.'}]}]},
 {'id': 'G68',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '12 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Üç haftadır okul günleri öğleden sonra başlayan, başın çevresini saran sıkıştırıcı ağrı',
  'history': "Ailesi anlatıyor: 'Üç haftadır hafta içi okuldan çıkınca bütün başını saran, sanki sıkı bir şapka takmış "
             'gibi künt bir ağrıdan yakınıyor. Zonklamıyor, bulantısı yok, ışıktan kaçmıyor. Ağrısına rağmen '
             'oynayabiliyor. Hafta sonları ve tatilde ağrısı olmuyor. Bu dönemde sınav hazırlığı yoğunlaştı; günde 5-6 '
             "saat telefon ve tablet başında, geceleri geç yatıyor, kahvaltı yapmıyor.' Sabah kusması, uykudan "
             'uyandıran ağrı veya görme yakınması yok. Tartı: 42 kg.',
  'final_diagnosis': 'Epizodik Gerilim Tipi Baş Ağrısı',
  'disposition': 'Yeşil Alandan Nörolojik Muayenenin Doğrulanması, Yaşam Tarzı Düzenlemesi, Sınırlı Analjezik ve Baş '
                 'Ağrısı Günlüğü Eğitimi ile Taburculuk',
  'case_pearl': 'Bilateral, bası-sıkıştırma tarzında, hafif-orta şiddetli, günlük aktiviteyle artmayan, bulantısız '
                'ağrı gerilim tipi baş ağrısını düşündürür. Normal nörolojik muayene ve fundoskopide görüntüleme '
                'gerekmez. Tedavinin temeli tetikleyicilerin (uyku düzensizliği, öğün atlama, yetersiz sıvı, uzun '
                'ekran süresi, stres) düzenlenmesidir. Analjezikler (ibuprofen, parasetamol) haftada 2-3 günü '
                'geçmemelidir; aksi halde ilaç aşırı kullanım baş ağrısı gelişir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Üç haftadır tekrarlayan baş ağrısı olan bu 12 yaşındaki çocukta muayenede neyi '
                         'değerlendirirsiniz?',
             'options': [{'text': 'Uzun ekran kullanımının gözleri yorduğunu varsayarak yalnızca görme keskinliği ve '
                                  'göz muayenesine odaklanmak, gözlük reçetesi için çocuğu aynı gün göz polikliniğine '
                                  'yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Nörolojik muayene ve kan basıncı ölçümü yapılmadı; göz muayenesi normal '
                                             'çıktı ve ağrı sürdü.',
                          'teaching_point': 'Kırma kusuru baş ağrısının nadir nedenidir; nörolojik muayene '
                                            'atlanmamalıdır.'},
                         {'text': 'Ağrı okul günleriyle ilişkili olduğu için okul kaçınmasını düşünüp muayeneyi kısa '
                                  'tutmak ve çocuk psikiyatrisine yönlendirme yapmak',
                          'is_correct': False,
                          'scenario_update': 'Nörolojik muayene ve fundoskopi yapılmadan yönlendirme yapıldı; aile '
                                             'çocuğun ağrısının ciddiye alınmadığını düşündü.',
                          'teaching_point': 'Psikososyal etkenler önemlidir ancak önce sekonder nedenler muayeneyle '
                                            'dışlanmalıdır.'},
                         {'text': 'Üç haftadır süren baş ağrısı nedeniyle muayeneden önce kontrastsız beyin '
                                  'tomografisi isteyip sonucu normalse göz doktoruna yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi normal geldi; çocuk gereksiz radyasyona maruz kaldı ve '
                                             'nörolojik muayene yapılmamıştı.',
                          'teaching_point': 'Görüntüleme kararı muayene sonrasında, kırmızı bayraklara göre verilir.'},
                         {'text': 'Kan basıncını ölçmek, görme keskinliğine ve fundoskopiye bakmak, kraniyal sinir, '
                                  'motor, serebellar ve yürüyüş muayenesi yapmak ve perikraniyal kas hassasiyetini '
                                  'değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Hipertansiyon, papilödem, görme ve nörolojik bulgular sekonder nedenleri '
                                         'düşündürür. Perikraniyal kas hassasiyeti birincil baş ağrısı tipini '
                                         'destekleyen bir bulgudur.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 76/dk, TA 105/68 mmHg. Görme keskinliği her '
                                         'iki gözde 10/10. Fundoskopide optik disk sınırları keskin, venöz pulsasyon '
                                         'var. Kraniyal sinirler, motor-duyu, serebellar testler ve tandem yürüyüş '
                                         'normal. Trapez ve boyun arka kaslarında palpasyonla hassasiyet.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Nörolojik muayenesi, fundoskopisi ve kan basıncı normal olan bu çocukta tetkik yaklaşımınız '
                         'nedir?',
             'options': [{'text': 'Ağrının nöbet eşdeğeri olabileceğini düşünüp elektroensefalografi istemek ve sonuç '
                                  'çıkana kadar ekran kullanımını tamamen yasaklamak',
                          'is_correct': False,
                          'scenario_update': 'EEG normal geldi; tanıya katkısı olmadı ve ani yasak aile içi çatışmaya '
                                             'yol açtı.',
                          'teaching_point': 'EEG baş ağrısı değerlendirmesinde rutin değildir.'},
                         {'text': 'Tam kan sayımı, demir parametreleri, tiroid fonksiyonları, D vitamini ve '
                                  'sedimantasyon isteyip sonuçlara göre tedavi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Tetkikler normal geldi; yönetimi değiştirmedi ve çocuk yaşam tarzı '
                                             'önerileri almadan gönderildi.',
                          'teaching_point': 'Birincil baş ağrısı tablosunda rutin laboratuvar tetkiki tanıya katkı '
                                            'sağlamaz.'},
                         {'text': 'Kırmızı bayrakların yokluğunu kayda geçirip tetkik istememek; uyku, öğün, sıvı, '
                                  'ekran süresi ve stres etkenlerini ayrıntılı sorgulamak',
                          'is_correct': True,
                          'explanation': 'Normal muayene ve kırmızı bayrak yokluğunda tanı kliniktir. Tetikleyicilerin '
                                         'ayrıntılı sorgulanması tedavinin temelini oluşturur.',
                          'new_finding': "Tetkik istenmedi. Çocuğun gece 01:00'de yattığı, kahvaltı yapmadığı, okulda "
                                         'neredeyse hiç su içmediği ve sınav kaygısı yaşadığı öğrenildi.'},
                         {'text': 'Arka çukur kitlesini dışlamak için sedasyonsuz beyin manyetik rezonans '
                                  'görüntülemesi planlamak ve sonuç gelene kadar okula gitmemesini önermek',
                          'is_correct': False,
                          'scenario_update': 'MR randevusu haftalar sonrasına verildi; çocuk okuldan uzak kaldı ve '
                                             'kaygısı arttı.',
                          'teaching_point': 'Kırmızı bayrak yoksa görüntüleme yapılmaz; okula devam '
                                            'desteklenmelidir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bilateral, sıkıştırıcı, hafif-orta şiddetli, bulantısız, okul günleri tekrarlayan ve '
                         'muayenesi normal olan bu çocukta tanı nedir?',
             'options': [{'text': 'İdiyopatik intrakraniyal hipertansiyon',
                          'is_correct': False,
                          'scenario_update': 'Papilödem ve görme yakınması yok; ağrı hafta sonları kayboluyor.',
                          'teaching_point': 'İdiyopatik intrakraniyal hipertansiyonda papilödem tanının temelidir.'},
                         {'text': 'Arka çukur tümörü',
                          'is_correct': False,
                          'scenario_update': 'Sabah kusması, uykudan uyandıran ağrı, ataksi veya papilödem yok.',
                          'teaching_point': 'Kafa içi kitlede ilerleyici ağrı ve nörolojik bulgular beklenir.'},
                         {'text': 'Epizodik gerilim tipi baş ağrısı',
                          'is_correct': True,
                          'explanation': 'Bilateral, bası tarzında, hafif-orta şiddetli, aktiviteyle artmayan ve '
                                         'bulantısız ağrı ile normal muayene ICHD-3 gerilim tipi baş ağrısı '
                                         'kriterlerini karşılar.',
                          'new_finding': 'Tanı: Epizodik Gerilim Tipi Baş Ağrısı.'},
                         {'text': 'Aurasız migren',
                          'is_correct': False,
                          'scenario_update': 'Ağrı zonklayıcı değil; bulantı, fotofobi ve fonofobi yok, aktivite ile '
                                             'artmıyor.',
                          'teaching_point': 'Migren genellikle zonklayıcı, orta-şiddetli ve bulantı veya ışık-ses '
                                            'hassasiyetiyle birliktedir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuğun tedavi ve izlem planı hangisidir?',
             'options': [{'text': 'Düzenli uyku, kahvaltı, sıvı alımı ve ekran molaları önermek; ağrıda ibuprofen veya '
                                  'parasetamolü haftada en fazla 2-3 gün kullanmak ve baş ağrısı günlüğü tutmak',
                          'is_correct': True,
                          'explanation': 'Yaşam tarzı düzenlemesi tedavinin temelidir. Analjeziklerin sınırlı '
                                         'kullanımı ilaç aşırı kullanım baş ağrısını önler; günlük, tetikleyicileri ve '
                                         'tedavi yanıtını izlemeyi sağlar. Stres yönetimi gerekirse okul rehberliğiyle '
                                         'desteklenir.',
                          'new_finding': 'Aileye yazılı öneriler verildi. İki hafta sonraki kontrolde uyku ve öğün '
                                         'düzeni oturmuş, ekran süresi azalmıştı; çocuk haftada yalnızca bir kez hafif '
                                         'ağrı tanımlıyordu.'},
                         {'text': 'Boyun kaslarındaki hassasiyet için servikal grafi çekmek, fizik tedaviye '
                                  'yönlendirmek ve okulda ağrı olursa eve gönderilmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Grafi normal geldi; okulda ağrı nedeniyle sık eve gönderilmek okul '
                                             'kaçınmasını pekiştirdi.',
                          'teaching_point': 'Görüntüleme gerekmez; ağrı sırasında okulda kalmak ve kısa mola '
                                            'desteklenmelidir.'},
                         {'text': 'Ağrının tekrarlamasını önlemek için her gün düzenli olarak sabah ve akşam ibuprofen '
                                  'kullanmasını ve ağrı tamamen geçene kadar devam etmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Bir ay düzenli analjezik kullanımı sonrası ağrı neredeyse her gün olmaya '
                                             'başladı.',
                          'teaching_point': 'Haftada 2-3 günden sık analjezik kullanımı ilaç aşırı kullanım baş '
                                            'ağrısına yol açar.'},
                         {'text': 'Ağrıların sıklığı nedeniyle acil serviste koruyucu tedavi olarak gece amitriptilin '
                                  'başlamak, kas gevşetici eklemek ve iki ay sonraki kontrolde yanıta göre dozları '
                                  'artırmayı planlamak',
                          'is_correct': False,
                          'scenario_update': 'İlaç sonrası gündüz uykululuk ve okul başarısında düşme gelişti; '
                                             'tetikleyiciler değiştirilmemişti.',
                          'teaching_point': 'Profilaktik ilaçlar sık ve yaşam kalitesini bozan ağrılarda, yaşam tarzı '
                                            'düzenlemesinden sonra poliklinikte planlanır.'}]}]},
 {'id': 'G69',
  'category': '👂 Kulak Ağrısı & KBB',
  'age': '7 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Burun karıştırma sonrası sağ burun deliğinden yarım saattir süren taze kanama',
  'history': "Annesi anlatıyor: 'Televizyon izlerken parmağıyla burnunu karıştırdı, sağ burnundan kan akmaya başladı. "
             'Panikle başını arkaya yatırdım, kanı yutup öğürdü ve pıhtılı kan çıkardı. Ensesine buz koyduk, kanama '
             "azaldı ama durmadı.' Kış aylarında evde kalorifer açık ve hava kuru. Daha önce birkaç kez kısa süreli "
             'burun kanaması olmuş. Vücutta morluk, diş eti kanaması yok. Ailede kanama hastalığı yok. İlaç '
             'kullanmıyor. Tartı: 24 kg.',
  'final_diagnosis': 'Anterior Epistaksis (Kiesselbach Pleksusu, Dijital Travma)',
  'disposition': 'Yeşil Alanda Doğru Bası Tekniğiyle Kanama Kontrolü, Mukoza Nemlendirme ve Önleme Eğitimi ile '
                 'Taburculuk',
  'case_pearl': 'Çocuklarda burun kanamalarının büyük çoğunluğu septumun ön kısmındaki Kiesselbach pleksusundan '
                'kaynaklanır; burun karıştırma ve kuru hava en sık nedenlerdir. Doğru teknik: oturur pozisyonda, baş '
                'hafif öne eğik, burnun yumuşak kısmına 10-15 dakika kesintisiz bası. Baş geriye yatırılmaz. Kanama '
                'sürerse topikal vazokonstriktör, görünür damarda gümüş nitrat koterizasyonu, son seçenek olarak '
                'anterior tampon uygulanır. Kişisel ve ailesel kanama öyküsü yoksa koagülasyon tetkiki gerekmez.',
  'steps': [{'stage_title': 'İlk Müdahale ve Fizik Muayene',
             'question': 'Yarım saattir burnu kanayan bu 7 yaşındaki çocukta ilk yapılacak müdahale nedir?',
             'options': [{'text': 'Çocuğun başını geriye yatırıp burun kökünü sıkmak, enseye buz koymaya devam etmek '
                                  've kanama durana kadar her iki dakikada bir basıyı kaldırıp kontrol etmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk kanı yutmaya devam etti ve kustu; sık kontrol nedeniyle pıhtı '
                                             'oluşamadı ve kanama sürdü.',
                          'teaching_point': 'Baş geriye yatırılmaz; bası burnun yumuşak kısmına uygulanmalı ve 10-15 '
                                            'dakika kesintisiz sürdürülmelidir.'},
                         {'text': 'Kanama yarım saattir sürdüğü için öncelikle kan grubu, tam kan sayımı ve '
                                  'koagülasyon paneli almak ve damar yolu açarak sıvı başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Tetkik ve damar yolu işlemleri sırasında kimse burna bası yapmadı; '
                                             'kanama sürdü ve çocuk huzursuzlaştı.',
                          'teaching_point': 'Hemodinamisi stabil çocukta ilk adım doğrudan bası ile kanamayı '
                                            'durdurmaktır.'},
                         {'text': 'Bası denemeden hemen her iki burun deliğine vazelinli gazlı bez ile anterior tampon '
                                  'yerleştirmek ve 48 saat sonra çıkarılmak üzere taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Tampon işlemi çocuk için çok ağrılı oldu ve mukozada ek travmaya neden '
                                             'oldu.',
                          'teaching_point': 'Tampon, basıya ve topikal tedaviye yanıt vermeyen kanamalarda son '
                                            'seçenektir.'},
                         {'text': 'Çocuğu oturtup başını hafif öne eğdirmek, burnun yumuşak kısmına 10-15 dakika '
                                  'kesintisiz bası yapmak ve bu sırada vital bulguları ve kanama miktarını '
                                  'değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Öne eğilme kanın yutulmasını ve aspirasyonu önler. Burun kanatlarına sürekli '
                                         'bası ön septumdaki kanama odağını doğrudan sıkıştırır. Vital bulgular '
                                         'kanamanın hemodinamik etkisini gösterir.',
                          'new_finding': 'Vital Bulgular: KTA 88/dk, SS 18/dk, SpO2 %100, TA 98/62 mmHg. Çocuk korkmuş '
                                         'ama stabil. 15 dakikalık kesintisiz bası sonrası kanama durdu. Anterior '
                                         'rinoskopide sağ septum ön kısmında küçük mukozal erozyon ve üzerinde pıhtı; '
                                         'mukoza kuru. Orofarinks arka duvarında akan kan yok. Ciltte peteşi, ekimoz '
                                         'yok; hepatosplenomegali yok.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Basıyla kanaması duran, ön septumda erozyon görülen ve kanama öyküsü olmayan bu çocukta '
                         'tetkik yaklaşımınız nedir?',
             'options': [{'text': 'Kişisel ve ailesel kanama öyküsünün, ilaç kullanımının ve sistemik kanama '
                                  'bulgularının yokluğunu kayda geçirip laboratuvar tetkiki istememek',
                          'is_correct': True,
                          'explanation': 'Lokal nedeni açık, basıyla kontrol edilen ve diğer kanama bulguları (morluk, '
                                         'diş eti kanaması, ailede kanama hastalığı) olmayan anterior kanamada '
                                         'koagülasyon tetkikinin tanısal değeri düşüktür.',
                          'new_finding': 'Kanama bulgusu ve aile öyküsü yok; tetkik istenmedi. 20 dakikalık gözlemde '
                                         'kanama tekrarlamadı.'},
                         {'text': 'Kan yutup kustuğu için gizli kanamayı değerlendirmek amacıyla hemoglobin takibi ve '
                                  'gaitada gizli kan testi istemek',
                          'is_correct': False,
                          'scenario_update': 'Hemoglobin 12.6 g/dL geldi; gaitada gizli kan yutulan kan nedeniyle '
                                             'pozitif bulundu ve aile yanlış yönlendirildi.',
                          'teaching_point': 'Yutulan burun kanı gaitada gizli kan testini pozitifleştirir; bu durumda '
                                            'test yanıltıcıdır.'},
                         {'text': 'Altta yatan kitle veya yabancı cismi dışlamak için paranazal sinüs tomografisi '
                                  'çekmek ve kulak burun boğaz konsültasyonu istemek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi normal geldi; kanama odağı rinoskopiyle zaten görülmüştü.',
                          'teaching_point': 'Tek taraflı kötü kokulu akıntı veya tekrarlayan şiddetli kanama yoksa '
                                            'görüntüleme gerekmez.'},
                         {'text': 'Tekrarlayan kanama öyküsü nedeniyle tam kan sayımı, PT, aPTT ve von Willebrand '
                                  'paneli istemek ve sonuç gelene kadar çocuğu gözlemde tutmak',
                          'is_correct': False,
                          'scenario_update': 'Tüm sonuçlar normal geldi; çocuk saatlerce bekletildi ve aile gereksiz '
                                             'kaygı yaşadı.',
                          'teaching_point': 'Kanama odağı belli, kısa süreli ve basıyla duran kanamada, diğer kanama '
                                            'bulguları yoksa tetkik gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Burun karıştırma sonrası tek taraflı, basıyla duran, ön septumda erozyon görülen ve kanama '
                         'bozukluğu bulgusu olmayan bu çocukta tanı nedir?',
             'options': [{'text': 'Posterior epistaksis',
                          'is_correct': False,
                          'scenario_update': 'Kanama odağı ön septumda görüldü, farinks arka duvarından akış yok ve '
                                             'kanama basıyla durdu.',
                          'teaching_point': 'Posterior kanama çocukta nadirdir, genellikle şiddetlidir ve anterior '
                                            'basıyla durmaz.'},
                         {'text': 'Von Willebrand hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Kişisel ve ailesel kanama öyküsü yok, morluk ve diş eti kanaması yok.',
                          'teaching_point': 'Kanama bozukluğu uzun süren, iki taraflı veya diğer bölgelerde kanamayla '
                                            'birlikte seyreden kanamalarda düşünülür.'},
                         {'text': 'Anterior epistaksis (Kiesselbach pleksusu)',
                          'is_correct': True,
                          'explanation': 'Ön septumdaki Kiesselbach pleksusu çocuklarda burun kanamalarının en sık '
                                         'kaynağıdır; dijital travma ve kuru mukoza tipik tetikleyicilerdir.',
                          'new_finding': 'Tanı: Anterior Epistaksis (Kiesselbach Pleksusu, dijital travma ve kuru '
                                         'mukoza zemininde).'},
                         {'text': 'Juvenil nazofarenks anjiyofibromu',
                          'is_correct': False,
                          'scenario_update': 'Burun tıkanıklığı yok, kanama burun karıştırma ile tetiklenmiş ve ön '
                                             'septumdan kaynaklanıyor.',
                          'teaching_point': 'Anjiyofibrom ergen erkeklerde tek taraflı burun tıkanıklığı ve '
                                            'tekrarlayan şiddetli kanamayla seyreder.'}]},
            {'stage_title': 'Taburculuk ve Önleme Planı',
             'question': 'Kanaması duran bu çocuğun taburculuk önerileri hangisidir?',
             'options': [{'text': 'Tekrarlayan kanamaları önlemek için acil serviste her iki septum ön kısmına gümüş '
                                  'nitratla koterizasyon uygulamak ve bir hafta burun spreyi kullanmak',
                          'is_correct': False,
                          'scenario_update': 'İki taraflı koterizasyon septum perforasyonu riski taşır; kanama durmuş '
                                             've aktif damar görülmüyordu.',
                          'teaching_point': 'Koterizasyon görünür damar veya basıya dirençli kanamada, tek taraflı ve '
                                            'uygun koşullarda yapılır.'},
                         {'text': 'Kanama tekrarlarsa evde başını geriye yatırıp burun köküne buz uygulamalarını ve '
                                  'iki gün süreyle burnunu sümkürmemesini, sıcak içecekten kaçınmasını önermek',
                          'is_correct': False,
                          'scenario_update': 'Bir sonraki kanamada aile yine başı geriye yatırdı; çocuk kanı yutup '
                                             'kustu ve kanama uzadı.',
                          'teaching_point': 'Yanlış tekniğin düzeltilmesi taburculuk eğitiminin en önemli parçasıdır.'},
                         {'text': 'Burun mukozasına günde iki kez vazelin sürmek, oda havasını nemlendirmek, '
                                  'tırnakları kısa tutup burun karıştırmamak ve doğru bası tekniğini aileye göstermek',
                          'is_correct': True,
                          'explanation': 'Mukozanın nemlendirilmesi ve dijital travmadan kaçınma tekrarı önlemede en '
                                         'etkili yöntemlerdir. Aile doğru bası tekniğini öğrendiğinde sonraki '
                                         'kanamaları evde durdurabilir; 20 dakikalık basıya yanıt vermeyen kanamada '
                                         'başvuru gerekir.',
                          'new_finding': 'Aileye bası tekniği uygulamalı gösterildi ve nemlendirme önerildi. Bir ay '
                                         'sonraki kontrolde yalnızca bir kez kısa süreli kanama olmuş ve evde basıyla '
                                         'durdurulmuştu.'},
                         {'text': 'Tekrarı önlemek için anterior tamponu 48 saat yerinde bırakmak, tampon süresince '
                                  'oral amoksisilin-klavulanat vermek ve çıkarmak için kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Kanaması durmuş çocuğa gereksiz tampon ve antibiyotik uygulandı; tampon '
                                             'nedeniyle ağız solunumu ve uyku sorunu yaşadı.',
                          'teaching_point': 'Kanaması duran çocukta tampon ve antibiyotik gerekmez.'}]}]},
 {'id': 'G70',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '8 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Sağ kolunda ve boynunda iki haftadır genişleyen, kenarları kabarık, hafif kaşıntılı kırmızı halka '
               'şeklinde lezyonlar',
  'history': "Annesi anlatıyor: 'İki hafta önce sağ kolunda küçük kırmızı bir sivilce gibi başladı, gün geçtikçe "
             'madeni para büyüklüğünde bir halkaya dönüştü. Ortası soldu, kenarı kırmızı, kabarık ve pul pul. Şimdi '
             'boynunda da benzeri çıktı. Hafif kaşıntılı. Bir ay önce sokakta bulduğumuz yavru kediyi eve aldık, onun '
             'da kulak arkasında tüysüz bir yer var. Eczaneden aldığımız kortizonlu kremi sürünce kızarıklık azaldı '
             "ama halka büyümeye devam etti.' Ateş, eklem ağrısı veya kene ısırığı yok. Tartı: 26 kg.",
  'final_diagnosis': 'Tinea Korporis (Zoofilik Dermatofit Enfeksiyonu)',
  'disposition': 'Yeşil Alandan Topikal Antifungal, Kortizonlu Kremin Bırakılması ve Evcil Hayvanın Tedavisi Eğitimi '
                 'ile Taburculuk',
  'case_pearl': 'Kenarı kabarık, pullu ve aktif, ortası soluk ve santrifüj genişleyen halka lezyon dermatofit '
                'enfeksiyonunu düşündürür; yavru kedi veya köpek sık bir kaynaktır (Microsporum canis). Tanı lezyon '
                'kenarından alınan kazıntının KOH incelemesiyle desteklenir. Topikal steroid kullanımı tabloyu '
                'maskeleyip yaygınlaştırabilir. Sınırlı lezyonlarda topikal terbinafin veya azol, lezyonun 1-2 cm '
                'ötesine kadar, temizlendikten sonra 1-2 hafta daha uygulanır. Saçlı deri tutulumu oral tedavi '
                'gerektirir; bu yüzden muayeneye mutlaka dahil edilmelidir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Genişleyen halka şeklinde lezyonları olan bu 8 yaşındaki çocukta muayenede neye dikkat '
                         'edersiniz?',
             'options': [{'text': 'Kortizonlu kreme kısmi yanıt verdiği için lezyonu egzama kabul edip daha güçlü bir '
                                  'topikal steroid reçete etmek ve iki hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Güçlü steroidle kızarıklık geçici azaldı ancak lezyonlar genişledi ve '
                                             'yenileri çıktı.',
                          'teaching_point': 'Topikal steroid mantar enfeksiyonunu maskeler ve yayılımını '
                                            'kolaylaştırır.'},
                         {'text': 'Lezyonların sınırını, pul yapısını ve dağılımını incelemek, saçlı deriyi, '
                                  'tırnakları ve kasık bölgesini muayene etmek ve sistemik bulguları sorgulamak',
                          'is_correct': True,
                          'explanation': 'Kenarın aktif ve pullu, ortanın soluk olması ayırıcı tanıda belirleyicidir. '
                                         'Saçlı deri ve tırnak tutulumu topikal tedaviyle iyileşmez; varlığı tedavi '
                                         'seçimini değiştirir. Sistemik bulgular eritema migrans gibi diğer halka '
                                         'lezyonları ayırır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 80/dk. Genel durumu iyi. Sağ ön kolda 3 cm '
                                         'çaplı, keskin sınırlı, kenarı kabarık, eritemli ve ince pullu, ortası soluk '
                                         'halka lezyon; boyun yan yüzünde 1.5 cm benzeri. Saçlı deride saç kaybı, '
                                         'pullanma veya kırık kıl yok. Tırnaklar ve kasık normal. Lenfadenopati, eklem '
                                         'bulgusu yok.'},
                         {'text': 'Halka şeklindeki lezyonu Lyme hastalığı ile ilişkili kabul edip kene ısırığını '
                                  'yeniden sorgulamak ve muayene etmeden ampirik oral doksisiklin başlamak',
                          'is_correct': False,
                          'scenario_update': 'Lezyonlar muayene edilmeden antibiyotik başlandı; pullu kenar ve kedi '
                                             'teması göz ardı edildi.',
                          'teaching_point': 'Eritema migransta pullanma beklenmez; halka lezyonlar ayrıntılı '
                                            'dermatolojik muayeneyle ayrılmalıdır.'},
                         {'text': 'Kedideki tüysüz alan nedeniyle zoonotik bir enfeksiyon olabileceğini düşünüp çocuğu '
                                  'okuldan uzaklaştırmak ve kedinin evden çıkarılmasını önermek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk muayene edilmeden okuldan uzaklaştırıldı; aile kediden ayrılmak '
                                             'zorunda kaldı.',
                          'teaching_point': 'Bu tabloda okul kısıtlaması gerekmez; evcil hayvan veteriner tarafından '
                                            'tedavi edilebilir.'}]},
            {'stage_title': 'Tetkik Stratejisi',
             'question': 'Saçlı deri ve tırnakları normal, kenarı pullu halka lezyonları olan bu çocukta tanıyı '
                         'desteklemek için hangi tetkiki yaparsınız?',
             'options': [{'text': 'Kesin tanı için lezyonun ortasından 4 mm punch biyopsi alıp histopatoloji ve fungal '
                                  'kültüre göndermek, sonuç gelene kadar tedavi başlamamak',
                          'is_correct': False,
                          'scenario_update': 'Biyopsi sonucu iki hafta sonra çıktı; bu sürede lezyonlar genişledi.',
                          'teaching_point': 'Biyopsi tipik halka lezyonlarda gerekmez; kazıntı ve KOH yeterlidir. '
                                            'Lezyonun ortası en az verimli bölgedir.'},
                         {'text': 'Halka şeklinde lezyonlarda Lyme serolojisi ve antinükleer antikor göndermek, '
                                  'sonuçlar negatifse dermatolojiye yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Seroloji negatif geldi; tanıyı destekleyen basit yatak başı tetkik '
                                             'yapılmamıştı.',
                          'teaching_point': 'Pullu kenarlı halka lezyonlarda ilk tetkik kazıntı ve KOH incelemesidir.'},
                         {'text': 'Lezyonun kabarık kenarından lam veya bistüri sırtıyla kazıntı alıp yüzde 10-20 KOH '
                                  'ile hazırlanan preparatı mikroskopta incelemek',
                          'is_correct': True,
                          'explanation': 'Fungal elemanlar en yoğun olarak aktif kenarda bulunur. KOH keratini '
                                         'eriterek dallanan septalı hiflerin görülmesini sağlar; basit, hızlı ve ucuz '
                                         'bir yatak başı tetkiktir.',
                          'new_finding': 'Kenar kazıntısının KOH incelemesinde dallanan, septalı hifler ve artrokonidi '
                                         'zincirleri görüldü.'},
                         {'text': 'Lezyondan eküvyonla sürüntü alıp bakteriyel kültür ve antibiyogram göndermek, '
                                  'üreyen etkene göre topikal antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'Kültürde deri florası üredi; topikal antibiyotik lezyonları etkilemedi.',
                          'teaching_point': 'Bakteriyel kültür bu tabloda tanıya katkı sağlamaz.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Kedi teması sonrası kenarı kabarık ve pullu, ortası soluk, genişleyen halka lezyonları ve '
                         "KOH'da septalı hifleri olan bu çocukta tanı nedir?",
             'options': [{'text': 'Pitriyazis rozea',
                          'is_correct': False,
                          'scenario_update': 'Gövdede çam ağacı dağılımı ve öncü madalyon plak yok; KOH pozitif.',
                          'teaching_point': 'Pitriyazis rozeada pullanma kenarın iç tarafında yaka şeklindedir ve KOH '
                                            'negatiftir.'},
                         {'text': 'Granuloma anülare',
                          'is_correct': False,
                          'scenario_update': 'Lezyonlar pullu ve kaşıntılı; granuloma anülarede pullanma olmaz.',
                          'teaching_point': 'Granuloma anülare pullanmayan, ten renginde papüllerden oluşan halkalarla '
                                            'seyreder.'},
                         {'text': 'Tinea korporis',
                          'is_correct': True,
                          'explanation': 'Santrifüj genişleyen, aktif pullu kenarlı halka lezyonlar, evcil hayvan '
                                         "teması ve KOH'da septalı hifler gövde-ekstremite dermatofit enfeksiyonunu "
                                         'doğrular.',
                          'new_finding': 'Tanı: Tinea Korporis (zoofilik, olası Microsporum canis).'},
                         {'text': 'Nummüler egzama',
                          'is_correct': False,
                          'scenario_update': "Lezyonların ortası soluk, kenarı aktif ve KOH'da hif görüldü.",
                          'teaching_point': 'Nummüler egzamada lezyonun tamamı homojen eritemli ve sızıntılıdır.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuğun tedavi planı hangisidir?',
             'options': [{'text': 'Topikal nistatin kremini günde üç kez bir hafta sürmek, lezyon geçmezse topikal '
                                  'mupirosin eklemek ve kedi ile temasın tamamen kesilmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Nistatin dermatofitlere etkisiz olduğu için lezyonlar genişlemeye devam '
                                             'etti.',
                          'teaching_point': "Nistatin yalnızca Candida'ya etkilidir; dermatofitlerde terbinafin veya "
                                            'azol kullanılır.'},
                         {'text': 'Topikal terbinafin veya azolü lezyonun 1-2 cm ötesine kadar günde 1-2 kez sürmek, '
                                  'temizlendikten sonra 1-2 hafta sürdürmek, kortizonlu kremi bırakmak ve kediyi '
                                  'veterinere götürmek',
                          'is_correct': True,
                          'explanation': 'Sınırlı tutulumda topikal antifungal yeterlidir; klinik iyileşme sonrası '
                                         'devam etmek nüksü önler. Steroid enfeksiyonu yaygınlaştırır. Kaynak hayvan '
                                         'tedavi edilmezse yeniden bulaş olur; okul kısıtlaması gerekmez.',
                          'new_finding': 'Topikal terbinafin başlandı, steroid krem bırakıldı, kedi veterinerde tedavi '
                                         'edildi. Üç hafta sonraki kontrolde lezyonlar solmuş, pullanma kaybolmuştu.'},
                         {'text': 'Kaşıntı ve kızarıklığı hızla azaltmak için steroid-antifungal kombine krem önermek '
                                  've iyileşme görüldüğünde kremi hemen bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Kombine krem lezyonu baskıladı ancak erken bırakılınca halkalar yeniden '
                                             'genişledi.',
                          'teaching_point': 'Steroid içeren kombinasyonlar dermatofit enfeksiyonlarında önerilmez; '
                                            'tedavi iyileşmeden sonra da sürdürülmelidir.'},
                         {'text': 'Lezyonlar birden fazla olduğu için oral griseofulvin 20-25 mg/kg/gün dozunu 8 hafta '
                                  'vermek, karaciğer fonksiyon testleriyle izlemek ve tedavi bitene kadar okula '
                                  'gitmemesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Sınırlı cilt lezyonu için uzun süreli sistemik tedavi gereksizdi; çocuk '
                                             'okuldan uzak kaldı.',
                          'teaching_point': 'Oral tedavi saçlı deri, tırnak veya yaygın-dirençli tutulumda '
                                            'gereklidir.'}]}]}]
