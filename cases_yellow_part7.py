# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Sarı Alan Vakaları (Bölüm 7: S61 - S70)
"""

YELLOW_CASES_PART7 = [{'id': 'S61',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '3 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Altı gündür düşmeyen yüksek ateş, gözlerde kızarıklık, dudaklarda çatlama ve boyunda şişlik',
  'history': "Ailesi anlatıyor: 'Altı gündür ateşi 39.5°C'ye kadar çıkıyor, ateş düşürücülerle ancak 38.5°C'ye iniyor. "
             'Üç gün önce farenjit denilerek oral sefalosporin başlandı, ateş hiç gerilemedi. Gözlerinin akı '
             'kıpkırmızı ama çapak yok. Dudakları kurudu, çatladı, kanıyor. Dün gövdesinde kırmızı döküntüler çıktı, '
             "el ve ayakları şişti, kızardı. Çok huzursuz.' Öksürük ve ishal yok. Aşıları tam. Tartı: 15 kg.",
  'final_diagnosis': 'Kawasaki Hastalığı (Tam Form, Koroner Arter Dilatasyonu ile)',
  'disposition': 'Sarı Alanda Ekokardiyografi Sonrası İntravenöz İmmünoglobulin (2 g/kg) ve Aspirin ile Çocuk '
                 'Kardiyoloji Yatışı',
  'case_pearl': 'En az 5 gün ateşle birlikte şu beş bulgudan en az dördü tam form tanısı koydurur: eksüdasız bilateral '
                'konjonktival kızarıklık, dudak-ağız değişiklikleri (çatlak dudak, çilek dili), polimorf döküntü, '
                'el-ayakta ödem-eritem (sonra periungual soyulma) ve genellikle tek taraflı ≥1.5 cm servikal '
                'lenfadenopati. Eksik formda laboratuvar (CRP, ESH, albümin, ALT, trombositoz, steril piyüri) ve '
                'ekokardiyografi yol gösterir. Tedavi ilk 10 gün içinde İVİG 2 g/kg ve aspirindir; amaç koroner '
                'anevrizmayı önlemektir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Antibiyotiğe rağmen altı gündür ateşi süren bu 3 yaşındaki çocukta muayenede neye '
                         'odaklanırsınız?',
             'options': [{'text': 'Perfüzyon ve kalp muayenesini yapmak; göz, dudak-ağız, döküntü, el-ayak '
                                  'değişikliklerini ve boyun lenf nodlarını sistematik olarak değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Uzamış ateşte göz, ağız, deri ve el-ayak bulgularının sistematik sayılması '
                                         'tanıyı belirler. Taşikardi, galo veya şok bulguları miyokardit ya da şok '
                                         'tablosunu düşündürür.',
                          'new_finding': 'Vital Bulgular: Ateş 39.4°C, KTA 142/dk, SS 28/dk, SpO2 %98, TA 94/58 mmHg, '
                                         'KDZ 2 sn. Bilateral eksüdasız konjonktival kızarıklık, limbus korunmuş. '
                                         'Dudaklar kırmızı, çatlak ve kanamalı; çilek dili. Gövdede makülopapüler '
                                         'polimorf döküntü. El ve ayak sırtında sert ödem, avuç içi ve tabanlarda '
                                         'eritem. Solda 2x2 cm tek, hassas servikal lenf nodu. Kalp sesleri ritmik, '
                                         'üfürüm ve galo yok.'},
                         {'text': 'Göz kızarıklığını bakteriyel konjonktivit kabul edip antibiyotikli göz damlası '
                                  'başlamak, döküntüyü sefalosporin alerjisine bağlayıp antihistaminik vermek',
                          'is_correct': False,
                          'scenario_update': 'Göz damlası ve antihistaminik bulguları değiştirmedi; altta yatan tablo '
                                             'tanınmadı.',
                          'teaching_point': 'Bulguları ayrı ayrı açıklamaya çalışmak, onları birleştiren sistemik '
                                            'hastalığın gözden kaçmasına yol açar.'},
                         {'text': 'Viral bir enfeksiyon olduğunu düşünüp antibiyotiği kesmek, ateş düşürücü ve bol '
                                  'sıvı önererek çocuğu evde izleme göndermek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk dördüncü gün yine ateşli getirildi; ekokardiyografide koroner '
                                             'anevrizma saptandı.',
                          'teaching_point': 'Beş günü aşan ateşte bu bulgular varsa tedavi geciktirilmemelidir; '
                                            'koroner hasar riski zamanla artar.'},
                         {'text': 'Ateşin dirençli farenjite bağlı olduğunu düşünüp antibiyotiği intravenöz '
                                  'seftriaksona çevirmek ve iki gün sonra yeniden değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'İki gün seftriaksona rağmen ateş sürdü; tedavi penceresi daralmaya '
                                             'başladı.',
                          'teaching_point': 'Antibiyotiğe yanıtsız uzamış ateşte enfeksiyon dışı nedenler ile deri ve '
                                            'mukoza bulguları sistematik değerlendirilmelidir.'}]},
            {'stage_title': 'Laboratuvar ve Kardiyak Değerlendirme',
             'question': 'Uzamış ateş ve dört deri-mukoza bulgusu olan bu çocukta hangi tetkikler öncelikli olarak '
                         'istenmelidir?',
             'options': [{'text': 'Hemogram, CRP, sedimantasyon, albümin, karaciğer testleri ve tam idrar istemek; '
                                  'acil ekokardiyografiyle koroner arterleri değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Yüksek inflamatuvar belirteçler, hipoalbüminemi, transaminaz artışı ve '
                                         'steril piyüri tanıyı destekler. Ekokardiyografi koroner tutulumu, miyokardit '
                                         've perikardiyal sıvıyı gösterir ve tedavi yoğunluğunu belirler.',
                          'new_finding': 'Lökosit 18.400/mm³ (%78 nötrofil), Hb 10.2 g/dL, trombosit 485.000/mm³, CRP '
                                         '142 mg/L, ESH 88 mm/sa, albümin 2.8 g/dL, ALT 72 U/L. Tam idrarda steril '
                                         'piyüri (15-20 lökosit/saha). Ekokardiyografi: sol ön inen koroner arter Z '
                                         'skoru +2.8 (dilatasyon), sol ventrikül fonksiyonu normal, minimal '
                                         'perikardiyal sıvı.'},
                         {'text': 'Döküntü ve ateş nedeniyle kızamık, EBV ve adenovirüs serolojilerini gönderip '
                                  'sonuçlar gelene kadar ekokardiyografiyi ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Seroloji sonuçları beş gün sürdü; kardiyak değerlendirme gecikti.',
                          'teaching_point': 'Viral tetkikler ayırıcı tanıda yardımcı olabilir ancak kardiyak '
                                            'değerlendirmeyi ve tedaviyi geciktirmemelidir.'},
                         {'text': 'Yalnızca boğaz kültürü ve ASO istemek, streptokok enfeksiyonu dışlanırsa ateşin '
                                  'nedenini araştırmak için çocuğu bir hafta daha izlemek',
                          'is_correct': False,
                          'scenario_update': 'Bekleme süresinde ateşin onuncu günü geçti; tedavinin en etkili olduğu '
                                             'dönem kaçırıldı.',
                          'teaching_point': 'Tedavi ateşin ilk 10 günü içinde verildiğinde koroner anevrizma riski '
                                            'belirgin azalır.'},
                         {'text': 'Menenjiti dışlamak için lomber ponksiyon yapmak ve sonuç gelene kadar intravenöz '
                                  'antibiyotikle izlemek',
                          'is_correct': False,
                          'scenario_update': 'Beyin omurilik sıvısında hafif pleositoz saptandı ancak kültür negatif '
                                             'kaldı; asıl tablo için tetkikler gecikti.',
                          'teaching_point': 'Bu hastalıkta aseptik pleositoz görülebilir; lomber ponksiyon ilk basamak '
                                            'tetkik değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Altı gündür süren ateş, eksüdasız konjonktival kızarıklık, çatlak dudak ve çilek dili, '
                         'polimorf döküntü, el-ayakta ödem, servikal lenfadenopati ve koroner dilatasyonu olan bu '
                         'çocukta tanı nedir?',
             'options': [{'text': 'Sistemik juvenil idiyopatik artrit',
                          'is_correct': False,
                          'scenario_update': 'Artrit yok; mukokutanöz bulgular ve koroner tutulum farklı bir tabloyu '
                                             'gösteriyor.',
                          'teaching_point': "Sistemik JİA'da günlük kotidyen ateş, somon renkli döküntü ve artrit "
                                            'beklenir.'},
                         {'text': 'Kızıl (A grubu streptokok)',
                          'is_correct': False,
                          'scenario_update': 'Döküntü zımpara kâğıdı gibi değil, konjonktival kızarıklık var ve '
                                             'antibiyotiğe yanıt yok.',
                          'teaching_point': 'Kızılda konjonktivit beklenmez ve antibiyotik tedavisine hızlı yanıt '
                                            'alınır.'},
                         {'text': 'Kawasaki hastalığı (tam form)',
                          'is_correct': True,
                          'explanation': 'En az 5 gün ateşle birlikte beş ana bulgunun tamamının varlığı ve koroner '
                                         'dilatasyon tam form Kawasaki hastalığını doğrular.',
                          'new_finding': 'Tanı: Kawasaki Hastalığı (tam form, koroner arter dilatasyonu ile).'},
                         {'text': 'Kızamık (rubeola enfeksiyonu)',
                          'is_correct': False,
                          'scenario_update': 'Aşıları tam; öksürük, burun akıntısı ve Koplik lekeleri yok.',
                          'teaching_point': 'Kızamıkta öksürük, nezle ve konjonktivit üçlüsü ile Koplik lekeleri '
                                            'görülür.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu çocuğun tedavi planı hangisidir?',
             'options': [{'text': 'Ateş altıncı günde olduğu için tedavi için geç kalındığını kabul edip yalnızca '
                                  'düşük doz aspirinle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Tedavi verilmeyen çocukta üçüncü haftada dev koroner anevrizma gelişti.',
                          'teaching_point': 'İVİG ideal olarak ilk 10 günde verilir; 10. günden sonra da ateş veya '
                                            'inflamasyon sürüyorsa önerilir.'},
                         {'text': 'İVİG yerine yüksek doz intravenöz metilprednizolon vermek ve koroner dilatasyon '
                                  'anevrizmaya dönüşürse immünoglobulin eklemek',
                          'is_correct': False,
                          'scenario_update': 'Steroid tek başına verildi; koroner dilatasyon ilerledi.',
                          'teaching_point': "Steroid ilk tedavide yalnızca yüksek riskli hastalarda İVİG'e ek olarak "
                                            'kullanılır, yerine geçmez.'},
                         {'text': 'Yalnızca yüksek doz aspirin başlamak, ateş düşmezse iki gün sonra intravenöz '
                                  'immünoglobulin vermeyi değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Aspirin tek başına koroner tutulumu önlemedi; iki gün sonraki ekoda '
                                             'dilatasyon arttı.',
                          'teaching_point': "Tedavinin temeli İVİG'dir; aspirin tek başına koroner anevrizmayı "
                                            'önlemez.'},
                         {'text': "İntravenöz immünoglobulin 2 g/kg'ı 10-12 saatte vermek, aspirin başlamak ve 2 ile "
                                  '6. haftalarda ekokardiyografi kontrolü planlamak',
                          'is_correct': True,
                          'explanation': 'İVİG koroner anevrizma riskini belirgin azaltır. Aspirin ateş düşene kadar '
                                         'orta-yüksek dozda, sonra 3-5 mg/kg/gün düşük dozda sürdürülür. Koroner '
                                         'dilatasyonu olan yüksek riskli olguda ek steroid düşünülebilir. Canlı aşılar '
                                         'İVİG sonrası 11 ay ertelenir.',
                          'new_finding': 'İVİG ve aspirin başlandı. 36 saatte ateş düştü, CRP geriledi. İkinci hafta '
                                         "ekokardiyografide koroner Z skoru +2.1'e indi; altıncı haftada normaldi. "
                                         'Düşük doz aspirin kardiyoloji önerisiyle kesildi.'}]}]},
 {'id': 'S62',
  'category': '🦴 Kas-İskelet & Eklem / Ortopedik Aciller',
  'age': '2 Yaşında',
  'gender': 'Kız',
  'complaint': 'Sağ dizde hızla artan şişlik, kızarıklık, sıcaklık, yüksek ateş ve bacağa hiç basamama',
  'history': "Ailesi anlatıyor: 'Dün sabah hafif topallıyordu. Gece sağ dizi şişti, kızardı, dokununca yanıyor. Ateşi "
             "39.2°C'ye çıktı. Bacağını hafif bükük tutuyor, hiç basmıyor, dokunmamıza izin vermiyor.' Bir hafta önce "
             'dizinde küçük bir sıyrık olmuş. Travma yok. Kanama hastalığı öyküsü yok. Aşıları tam. Tartı: 12 kg.',
  'final_diagnosis': 'Sağ Diz Septik Artriti (Staphylococcus aureus)',
  'disposition': 'Sarı Alanda Kültür Sonrası İntravenöz Antistafilokokal Antibiyotik ve Acil Ortopedik Eklem Lavajı '
                 'ile Yatış',
  'case_pearl': 'Ateş, basamama ve tek eklemde ağrılı şişlik septik artrit acilidir; kıkırdak hasarı saatler içinde '
                "başlar. En sık etken S. aureus'tur; 4 yaş altında Kingella kingae de sık görülür ve kültürde zor ürer "
                '(PCR yararlıdır). Sinovyal sıvıda lökosit >50.000/mm³ ve nötrofil hakimiyeti tipiktir. Tedavi '
                'kültürler alındıktan sonra ampirik antibiyotik ve cerrahi drenajdır; klinik ve CRP yanıtıyla erken '
                'oral geçiş mümkündür. Komşu kemikte osteomiyelit eşlik edebilir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Ateşli, dizi şiş ve bacağına basamayan bu 2 yaşındaki kızda muayenede neye odaklanırsınız?',
             'options': [{'text': 'Sepsis bulgularını, dizde efüzyon ve hareket ağrısını, komşu kemik hassasiyetini, '
                                  'diğer eklemleri ve deri lezyonlarını değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Ateşli monoartritte sistemik durum aciliyeti belirler. Komşu metafizde '
                                         'hassasiyet osteomiyeliti, birden çok eklem tutulumu farklı nedenleri '
                                         'düşündürür. Deri lezyonu stafilokokal giriş kapısı olabilir.',
                          'new_finding': 'Vital Bulgular: Ateş 39.1°C, KTA 138/dk, SS 26/dk, SpO2 %99, TA 96/60 mmHg, '
                                         'KDZ 2 sn. Sağ diz 30 derece fleksiyonda tutuluyor; belirgin şişlik, patellar '
                                         'ballotman, kızarıklık ve ısı artışı var. En küçük pasif hareket şiddetli '
                                         'ağrıya yol açıyor. Distal femur ve proksimal tibiada belirgin kemik '
                                         'hassasiyeti yok. Diğer eklemler normal. Diz önünde iyileşmekte olan sıyrık.'},
                         {'text': 'Travma olabileceğini düşünüp diz grafisi çekmek, kırık yoksa atel ve ibuprofen '
                                  'önerip üç gün sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Grafide kırık yoktu; atelle eve giden çocuğun ateşi sürdü ve iki gün '
                                             'sonra eklem harabiyetiyle geri getirildi.',
                          'teaching_point': 'Ateşle birlikte tek eklemde ağrılı şişlik enfeksiyon dışlanana kadar acil '
                                            'kabul edilir.'},
                         {'text': 'Huzursuzluğu azaltmak için önce sedasyon verip dizden hemen biyopsi almak üzere '
                                  'ortopediye danışmak',
                          'is_correct': False,
                          'scenario_update': 'Biyopsi bu aşamada gereksizdi; sistemik değerlendirme ve kültürler '
                                             'alınmadan zaman kaybedildi.',
                          'teaching_point': 'İlk adım sistemik değerlendirme, kan tetkikleri ve kültürlerdir; doku '
                                            'biyopsisi atipik olgularda düşünülür.'},
                         {'text': 'Romatizmal bir hastalık düşünüp romatoloji polikliniğine yönlendirmek ve ağrı için '
                                  'oral prednizolon başlamak',
                          'is_correct': False,
                          'scenario_update': 'Steroid ateşi maskeledi; eklem enfeksiyonu ilerledi.',
                          'teaching_point': 'Enfeksiyon dışlanmadan steroid verilmez; akut ateşli monoartrit acil '
                                            'değerlendirilir.'}]},
            {'stage_title': 'Laboratuvar, Görüntüleme ve Sinovyal Sıvı',
             'question': 'Bu çocukta tanıyı doğrulamak için hangi tetkikler yapılmalıdır?',
             'options': [{'text': "Yalnızca hemogram ve CRP istemek, lökosit 20.000/mm³'ün altındaysa enfeksiyonu "
                                  'dışlayıp çocuğu ağrı kesiciyle izlemek',
                          'is_correct': False,
                          'scenario_update': 'Lökosit 19.800/mm³ geldi ve enfeksiyon yok sayıldı; sinovyal sıvı '
                                             'alınmadı.',
                          'teaching_point': 'Normal veya sınırda lökosit sayısı eklem enfeksiyonunu dışlamaz.'},
                         {'text': 'Osteomiyeliti dışlamak için sedasyon altında diz manyetik rezonansını acil çekmek '
                                  've sonuç gelene kadar antibiyotiği ertelemek',
                          'is_correct': False,
                          'scenario_update': 'MR için saatlerce beklendi; eklem enfeksiyonu tedavisiz kaldı.',
                          'teaching_point': 'MR eşlik eden osteomiyelit şüphesinde değerlidir ancak drenaj ve '
                                            'antibiyotiği geciktirmemelidir.'},
                         {'text': 'Hemogram, CRP ve kan kültürü almak; grafi ve ultrason çekip ortopediyle sinovyal '
                                  'sıvıyı hücre sayımı ve kültür için almak',
                          'is_correct': True,
                          'explanation': 'Kan kültürü ve sinovyal sıvı kültürü antibiyotik öncesinde alınmalıdır. '
                                         'Sinovyal lökosit sayısı ve Gram boyama tanıyı hızla destekler. Grafi kırık '
                                         've kemik lezyonunu, ultrason efüzyonu gösterir.',
                          'new_finding': 'Lökosit 19.800/mm³ (%84 nötrofil), CRP 112 mg/L, ESH 74 mm/sa, kan kültürü '
                                         'alındı. Grafide kırık yok, yumuşak doku şişliği var. Ultrasonda yoğun '
                                         'ekojenik efüzyon. Sinovyal sıvı bulanık: lökosit 92.000/mm³ (%88 nötrofil), '
                                         'Gram boyamada küme yapan gram pozitif koklar; kültür ve Kingella PCR '
                                         'gönderildi.'},
                         {'text': 'Sinovyal sıvı almadan hemen intravenöz antibiyotik başlamak ve tanıyı antibiyotik '
                                  'yanıtına göre koymak, eklem sıvısını yalnızca yanıt alınamazsa incelemek',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik sonrası alınan sıvıda kültür negatif kaldı; etken ve '
                                             'duyarlılık belirlenemedi.',
                          'teaching_point': 'Hemodinami stabilse antibiyotik öncesinde eklem sıvısı ve kan kültürü '
                                            'alınmalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Ateş, basamama, dizde ağrılı efüzyon, CRP 112 mg/L ve sinovyal sıvıda 92.000/mm³ lökosit ile '
                         'gram pozitif kok kümeleri olan bu çocukta tanı nedir?',
             'options': [{'text': 'Geçici (toksik) sinovit',
                          'is_correct': False,
                          'scenario_update': 'Yüksek ateş, basamama, yüksek CRP ve pürülan sinovyal sıvı var.',
                          'teaching_point': 'Geçici sinovitte çocuk iyi görünür ve inflamatuvar belirteçler '
                                            'normaldir.'},
                         {'text': 'Hemofiliye bağlı hemartroz',
                          'is_correct': False,
                          'scenario_update': 'Kanama öyküsü yok, kız çocuk ve sinovyal sıvı kanlı değil pürülan.',
                          'teaching_point': 'Hemartrozda eklem sıvısı kanlıdır ve kanama öyküsü bulunur.'},
                         {'text': 'Sağ diz septik artriti',
                          'is_correct': True,
                          'explanation': 'Pürülan sinovyal sıvı, lökosit >50.000/mm³, nötrofil hakimiyeti ve Gram '
                                         'boyamada stafilokok morfolojisi bakteriyel eklem enfeksiyonunu doğrular.',
                          'new_finding': 'Tanı: Sağ Diz Septik Artriti (olası Staphylococcus aureus).'},
                         {'text': 'Oligoartiküler juvenil idiyopatik artrit',
                          'is_correct': False,
                          'scenario_update': 'Akut başlangıç, yüksek ateş ve sinovyal sıvıda bakteri görülmesi bu '
                                             'tanıyla uyumsuz.',
                          'teaching_point': 'Juvenil idiyopatik artrit en az 6 hafta süren, genellikle ateşsiz '
                                            'artritle tanınır.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu çocuğun tedavi planı hangisidir?',
             'options': [{'text': 'Eklemi yıkamadan altı hafta intravenöz antibiyotik vermek ve eklem hareketini '
                                  'tamamen kısıtlamak için alçıya almak',
                          'is_correct': False,
                          'scenario_update': 'Drenaj yapılmayan eklemde pürülan sıvı kaldı ve kıkırdak hasarı gelişti; '
                                             'alçı eklem sertliğine yol açtı.',
                          'teaching_point': 'Drenaj kıkırdağı korur; uzun süreli immobilizasyon önerilmez.'},
                         {'text': 'Eklem içine kortikosteroid ve antibiyotik enjekte etmek, inflamasyonu baskılamak '
                                  'için oral ibuprofeni yüksek dozda sürdürmek',
                          'is_correct': False,
                          'scenario_update': 'Eklem içi steroid enfeksiyonu ağırlaştırdı; ateş ve şişlik arttı.',
                          'teaching_point': 'Eklem enfeksiyonunda eklem içi steroid kontrendikedir; antibiyotik '
                                            'sistemik verilir.'},
                         {'text': 'Oral sefaleksinle ayaktan tedavi başlamak ve 48 saat sonra poliklinikte eklemi '
                                  'yeniden değerlendirmek, ağrı için ibuprofen ve dinlenme önermek',
                          'is_correct': False,
                          'scenario_update': 'Drenajsız oral tedavi yetersiz kaldı; çocuk iki gün sonra eklem '
                                             'harabiyetiyle geri geldi.',
                          'teaching_point': 'Septik artrit başlangıçta intravenöz antibiyotik ve eklem drenajı '
                                            'gerektirir.'},
                         {'text': 'İntravenöz sefazolin başlamak, acil eklem lavajı yapmak; klinik ve CRP düzelince '
                                  'oral tedaviyle toplam 2-3 haftaya tamamlamak',
                          'is_correct': True,
                          'explanation': "Sefazolin S. aureus ve Kingella'yı kapsar; MRSA sıklığı yüksek bölgelerde "
                                         'klindamisin veya vankomisin tercih edilir. Cerrahi lavaj bakteri yükünü ve '
                                         "kıkırdak hasarını azaltır. Ateşi düşen ve CRP'si gerileyen çocukta erken "
                                         'oral geçiş güvenlidir.',
                          'new_finding': 'Sefazolin başlandı, artroskopik lavaj yapıldı. Kültürde metisiline duyarlı '
                                         "S. aureus üredi. 72. saatte ateş düştü, CRP 34 mg/L'ye indi; oral "
                                         'sefaleksine geçildi ve tedavi üç haftaya tamamlandı. Eklem hareketleri '
                                         'normale döndü.'}]}]},
 {'id': 'S63',
  'category': '💧 Sıvı-Elektrolit & Renal / Ürolojik Aciller',
  'age': '8 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Kola renginde idrar, göz kapaklarında ve bacaklarda şişlik, idrar azalması ve şiddetli baş ağrısı',
  'history': "Ailesi anlatıyor: 'Sabahtan beri kola renginde, koyu idrar yapıyor; bugün yalnızca bir kez azıcık yaptı. "
             'Sabah göz kapakları ve yüzü şişti, çorap lastikleri bacağında iz bıraktı. Şiddetli baş ağrısı var, '
             "gözlerinin önünde ışıklar çaktığını söylüyor.' İki hafta önce ateşli boğaz ağrısı geçirmiş, tedavi "
             'almamış. Bilinen böbrek hastalığı yok. Tartı: 28 kg (bir hafta önce 26 kg).',
  'final_diagnosis': 'Akut Poststreptokokal Glomerülonefrit (Hipertansiyon ve Sıvı Yüklenmesi ile)',
  'disposition': 'Sarı Alanda Tuz-Sıvı Kısıtlaması, İntravenöz Furosemid, Antihipertansif Tedavi ve Çocuk Nefroloji '
                 'Yatışı',
  'case_pearl': 'Boğaz enfeksiyonundan 1-3 hafta (deri enfeksiyonundan 3-6 hafta) sonra gelişen kola renkli idrar, '
                'ödem, hipertansiyon ve oligüri nefritik sendromun klasik tablosudur. Düşük C3 ve normal C4, '
                'streptokok antikorlarının yüksekliği ve idrarda dismorfik eritrosit-eritrosit silendirleri tanıyı '
                'destekler. Hipertansiyon çoğunlukla sıvı-tuz tutulumuna bağlıdır; tedavi tuz-sıvı kısıtlaması ve loop '
                'diüretiktir. Baş ağrısı, görme bozukluğu ve nöbet hipertansif ensefalopatiyi düşündürür. C3 6-8 '
                'haftada normale döner; dönmezse başka glomerül hastalıkları araştırılır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Kan Basıncı',
             'question': 'Kola renkli idrar, ödem ve şiddetli baş ağrısıyla gelen bu 8 yaşındaki çocukta ilk '
                         'değerlendirmede neye odaklanırsınız?',
             'options': [{'text': 'İdrar azaldığı için böbrekleri desteklemek amacıyla 20 mL/kg serum fizyolojik '
                                  'bolusu vermek ve idrar çıkışını iki saat boyunca saat başı ölçerek beklemek',
                          'is_correct': False,
                          'scenario_update': "Bolus sonrası solunum hızı arttı, satürasyon %92'ye düştü ve kan basıncı "
                                             "150/100 mmHg'ye yükseldi.",
                          'teaching_point': 'Ödemli ve hipertansif çocukta oligüri sıvı yüklenmesine eşlik eder; bolus '
                                            'tehlikelidir.'},
                         {'text': 'Kan basıncını uygun manşonla ölçmek; sıvı yüklenmesi, kalp yetmezliği ve '
                                  'hipertansif ensefalopati bulgularını aramak, tartıp idrar çıkışını izlemek',
                          'is_correct': True,
                          'explanation': 'Baş ağrısı ve görsel yakınmalar hipertansif ensefalopatinin habercisi '
                                         'olabilir. Ödem, raller, hepatomegali ve galo sıvı yüklenmesini gösterir. '
                                         'Tartı ve idrar çıkışı sıvı dengesinin temelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 88/dk, SS 22/dk, SpO2 %98, TA 138/92 mmHg '
                                         '(evre 2 hipertansiyon). Bilinç açık, oryante; fokal defisit yok, '
                                         'fundoskopide papilödem yok. Belirgin periorbital ödem, pretibial 2+ gode '
                                         'bırakan ödem. Akciğer bazallerinde hafif raller, karaciğer kot kavsini 2 cm '
                                         'geçiyor, galo yok. Tartı 28 kg.'},
                         {'text': 'Şişliği alerjik reaksiyon kabul edip intravenöz antihistaminik ve steroid vermek, '
                                  'baş ağrısı için parasetamol önermek',
                          'is_correct': False,
                          'scenario_update': 'Kan basıncı ölçülmedi; çocuk gözlem sırasında jeneralize nöbet geçirdi.',
                          'teaching_point': 'Ödem ve baş ağrısı olan çocukta kan basıncı ölçümü atlanmamalıdır.'},
                         {'text': 'Baş ağrısı ve görme yakınması nedeniyle önce kontrastsız beyin tomografisi çekmek '
                                  've idrar değerlendirmesini sonrasına bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Tomografi normal geldi; kan basıncı ve idrar değerlendirilmeden bir saat '
                                             'geçti.',
                          'teaching_point': 'Baş ağrısının en olası nedeni yüksek kan basıncıdır; önce ölçülmeli ve '
                                            'tedavi edilmelidir.'}]},
            {'stage_title': 'Laboratuvar ve İdrar Değerlendirmesi',
             'question': 'Hipertansif ve ödemli bu çocukta hangi tetkikler öncelikli olarak istenmelidir?',
             'options': [{'text': 'Tam idrar ve idrar mikroskopisi, BUN-kreatinin, elektrolitler, albümin, C3-C4, ASO '
                                  've anti-DNaz B istemek; solunum sıkıntısı varsa akciğer grafisi çekmek',
                          'is_correct': True,
                          'explanation': 'Dismorfik eritrositler ve eritrosit silendirleri glomerül kaynaklı kanamayı '
                                         'gösterir. Düşük C3 ve normal C4 ile streptokok antikorlarının yüksekliği '
                                         'etiyolojiyi destekler. Potasyum ve kreatinin akut böbrek hasarının '
                                         'derecesini belirler.',
                          'new_finding': 'Tam idrar: kola renginde, dansite 1025, protein 2+, kan 3+. Mikroskopide bol '
                                         'dismorfik eritrosit ve eritrosit silendirleri. BUN 48 mg/dL, kreatinin 0.88 '
                                         'mg/dL, K 4.6 mEq/L, Na 136 mEq/L, albümin 3.4 g/dL. C3 32 mg/dL (düşük), C4 '
                                         'normal, ASO 680 IU/mL. Akciğer grafisinde hafif vasküler belirginleşme.'},
                         {'text': 'Kola renkli idrarı rabdomiyolize bağlayıp kreatin kinaz ve idrarda miyoglobin '
                                  'istemek, sonuç gelene kadar yüksek hızda sıvı başlamak, idrarı alkalileştirmek için '
                                  'bikarbonat eklemek',
                          'is_correct': False,
                          'scenario_update': 'Kreatin kinaz normal geldi; verilen sıvı ödemi ve hipertansiyonu '
                                             'ağırlaştırdı.',
                          'teaching_point': 'Ödem ve hipertansiyonla birlikte koyu idrar glomerül kaynaklı hematüriyi '
                                            'düşündürür.'},
                         {'text': 'Tanıyı kesinleştirmek için acil perkütan böbrek biyopsisi planlamak ve tedaviyi '
                                  'patoloji sonucuna göre başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Biyopsi tipik klinik tabloda gereksizdi; hipertansif çocukta kanama '
                                             'riski taşıdı ve tedavi gecikti.',
                          'teaching_point': "Biyopsi atipik seyir, hızlı ilerleyen böbrek yetmezliği veya C3'ün 8 "
                                            'haftada düzelmemesi durumunda yapılır.'},
                         {'text': 'Yalnızca idrar kültürü göndermek, idrar yolu enfeksiyonu kabul edip oral '
                                  'antibiyotik başlamak ve ödemi gözlemek',
                          'is_correct': False,
                          'scenario_update': 'Kültür negatif geldi; hipertansiyon ve böbrek fonksiyonu '
                                             'değerlendirilmedi.',
                          'teaching_point': 'Hematüri, ödem ve hipertansiyon birlikteliği enfeksiyonla açıklanmaz.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Boğaz enfeksiyonundan iki hafta sonra kola renkli idrar, ödem, hipertansiyon, eritrosit '
                         'silendirleri, düşük C3 ve yüksek ASO olan bu çocukta tanı nedir?',
             'options': [{'text': 'İlk atak nefrotik sendrom',
                          'is_correct': False,
                          'scenario_update': 'Albümin yalnızca hafif düşük, masif proteinüri yok ve hematüri ile '
                                             'hipertansiyon belirgin.',
                          'teaching_point': 'Nefrotik sendromda masif proteinüri ve ağır hipoalbüminemi ön plandadır.'},
                         {'text': 'Hemolitik üremik sendrom',
                          'is_correct': False,
                          'scenario_update': 'Kanlı ishal, anemi ve trombositopeni yok.',
                          'teaching_point': 'Hemolitik üremik sendromda mikroanjiyopatik hemoliz ve trombositopeni '
                                            'böbrek hasarına eşlik eder.'},
                         {'text': 'IgA nefropatisi',
                          'is_correct': False,
                          'scenario_update': 'Hematüri enfeksiyondan iki hafta sonra başladı ve C3 düşük.',
                          'teaching_point': 'IgA nefropatisinde hematüri enfeksiyonla eş zamanlı (1-2 gün içinde) '
                                            'ortaya çıkar ve C3 normaldir.'},
                         {'text': 'Akut poststreptokokal glomerülonefrit',
                          'is_correct': True,
                          'explanation': 'Latent dönem sonrası nefritik sendrom, düşük C3, normal C4 ve yüksek '
                                         'streptokok antikorları akut poststreptokokal glomerülonefriti doğrular.',
                          'new_finding': 'Tanı: Akut Poststreptokokal Glomerülonefrit (hipertansiyon ve sıvı '
                                         'yüklenmesi ile).'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu çocuğun tedavi planı hangisidir?',
             'options': [{'text': 'Tuz ve sıvıyı kısıtlamak, intravenöz furosemid vermek, kan basıncı yüksek kalırsa '
                                  'nifedipin eklemek ve günlük tartıyla izlemek',
                          'is_correct': True,
                          'explanation': 'Hipertansiyon ve ödem sıvı-tuz tutulumuna bağlıdır; diüretik ve kısıtlama '
                                         'temel tedavidir. Kalsiyum kanal blokerleri ek antihipertansif olarak '
                                         'güvenlidir. Süren streptokok enfeksiyonu varsa penisilin verilir ancak '
                                         'böbrek seyrini değiştirmez.',
                          'new_finding': 'Furosemid 1 mg/kg intravenöz verildi, tuz-sıvı kısıtlandı. Dört saatte 450 '
                                         "mL idrar çıktı, kan basıncı 118/76 mmHg'ye indi, baş ağrısı geçti. Üç günde "
                                         'ödem çözüldü. Sekizinci haftada C3 normale döndü.'},
                         {'text': 'Kan basıncı 138/92 mmHg olduğu için hipertansiyonu ciddi kabul etmemek, oral '
                                  'antibiyotik ve tuzsuz diyetle çocuğu taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Evde baş ağrısı arttı; çocuk ertesi gün hipertansif ensefalopati ve '
                                             'nöbetle getirildi.',
                          'teaching_point': 'Semptomatik evre 2 hipertansiyon ve oligüri yatış gerektirir.'},
                         {'text': 'Böbrek perfüzyonunu korumak için idame hızında intravenöz sıvı vermek, kan '
                                  'basıncını düşürmek için ilk seçenek olarak ACE inhibitörü başlamak',
                          'is_correct': False,
                          'scenario_update': "Sıvı yükü arttı; ACE inhibitörü sonrası potasyum 6.1 mEq/L'ye yükseldi "
                                             've kreatinin arttı.',
                          'teaching_point': 'Akut dönemde sıvı kısıtlanır; ACE inhibitörleri hiperkalemi ve böbrek '
                                            'fonksiyonunda bozulma riski nedeniyle ilk seçenek değildir.'},
                         {'text': 'Böbrek hasarını önlemek için yüksek doz intravenöz metilprednizolon ve '
                                  'siklofosfamid başlamak, kan basıncı için yalnızca gözlem yapmak',
                          'is_correct': False,
                          'scenario_update': 'İmmünsüpresif tedavi gereksizdi; tedavi edilmeyen hipertansiyon '
                                             'nedeniyle çocukta nöbet gelişti.',
                          'teaching_point': 'Tipik seyirde immünsüpresyon endike değildir; hipertansiyon acilen tedavi '
                                            'edilmelidir.'}]}]},
 {'id': 'S64',
  'category': '💧 Sıvı-Elektrolit & Renal / Ürolojik Aciller',
  'age': '4 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Göz kapaklarında başlayıp bacaklara, karına ve skrotuma yayılan yaygın şişlik ve köpüklü idrar',
  'history': "Ailesi anlatıyor: 'Beş gün önce sabah göz kapakları şişmişti, alerji sandık. Şişlik bacaklarına, ayak "
             'bileklerine ve testislerine yayıldı. Karnı şişti, pantolonu kapanmıyor. İdrarı azaldı ve köpüklü. Bugün '
             "karnı biraz ağrıyor, halsiz.' Bir hafta önce soğuk algınlığı geçirmiş. Kanlı idrar ve döküntü yok. Su "
             'çiçeği geçirmemiş. Tartı: 18 kg (öncesinde 15.5 kg).',
  'final_diagnosis': 'İlk Atak İdiyopatik Nefrotik Sendrom (Olası Minimal Değişiklik Hastalığı)',
  'disposition': 'Sarı Alanda Damar İçi Hacim Değerlendirmesi, Tuz Kısıtlaması, Oral Prednizolon ve Komplikasyon '
                 'Eğitimi ile Çocuk Nefroloji Yatışı',
  'case_pearl': 'Masif proteinüri (idrar protein/kreatinin >2 mg/mg), hipoalbüminemi (<2.5 g/dL) ve ödem tanı '
                'koydurur; hiperlipidemi eşlik eder. 1-10 yaş arasında hematüri, hipertansiyon ve böbrek yetmezliği '
                "olmayan, C3'ü normal çocukta neden çoğunlukla minimal değişiklik hastalığıdır ve biyopsi yapılmadan "
                'steroid başlanır. Ödemli olmasına karşın damar içi hacim azalmış olabilir (karın ağrısı, taşikardi, '
                'soğuk ekstremite, yüksek hematokrit); bu durumda diüretik tehlikelidir. Başlıca komplikasyonlar '
                'enfeksiyon (peritonit, selülit) ve trombozdur.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Hacim Durumu',
             'question': 'Yaygın ödemi, asiti ve karın ağrısı olan bu 4 yaşındaki çocukta ilk değerlendirmede neye '
                         'odaklanırsınız?',
             'options': [{'text': 'Skrotal şişlik nedeniyle testis torsiyonunu dışlamak için acil skrotal Doppler '
                                  'istemek ve üroloji görüşü gelene kadar muayeneyi bununla sınırlamak',
                          'is_correct': False,
                          'scenario_update': 'Doppler normal geldi; yaygın ödemin nedeni ve hacim durumu '
                                             'değerlendirilmedi.',
                          'teaching_point': 'Yaygın ödemin bir parçası olan skrotal ödem sistemik değerlendirme '
                                            'gerektirir.'},
                         {'text': 'Göz kapağı şişliği nedeniyle alerjik anjiyoödem kabul edip intramüsküler adrenalin '
                                  've antihistaminik vermek',
                          'is_correct': False,
                          'scenario_update': 'Tedaviye yanıt alınmadı; ödemin nedeni değerlendirilmedi.',
                          'teaching_point': 'Günler içinde yerçekimine bağlı yayılan gode bırakan ödem alerjik '
                                            'değildir.'},
                         {'text': 'Ödemi hızla azaltmak için hacim durumunu değerlendirmeden yüksek doz intravenöz '
                                  'furosemid vermek ve idrar çıkışını izlemek',
                          'is_correct': False,
                          'scenario_update': 'Furosemid sonrası çocukta taşikardi, karın ağrısında artış ve soğuk '
                                             'ekstremiteler gelişti.',
                          'teaching_point': 'Hacim azlığı olan nefrotik çocukta diüretik şoka ve tromboza yol '
                                            'açabilir.'},
                         {'text': 'Kan basıncı, nabız, kapiller dolum ve ekstremite ısısıyla hacim durumunu; ödem, '
                                  'asit, solunum, enfeksiyon ve tromboz bulgularını değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Ödemli çocukta damar içi hacim azalmış olabilir; karın ağrısı ve soğuk '
                                         'ekstremite hipovolemiyi düşündürür. Plevral efüzyon solunumu etkiler. Karın '
                                         'ağrısı ayrıca enfeksiyon veya trombozun habercisi olabilir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 98/dk, SS 22/dk, SpO2 %99, TA 96/60 mmHg, '
                                         'KDZ 2 sn, ekstremiteler sıcak. Periorbital ödem, pretibial 3+ gode bırakan '
                                         'ödem, belirgin skrotal ödem. Karın distandü, yer değiştiren matite (asit); '
                                         'hafif yaygın hassasiyet, defans ve rebound yok. Akciğer bazallerinde solunum '
                                         'sesleri hafif azalmış. Tartı 18 kg.'}]},
            {'stage_title': 'Laboratuvar Değerlendirmesi',
             'question': 'Bu çocukta tanı ve tedavi kararı için hangi tetkikler istenmelidir?',
             'options': [{'text': 'Tam idrar, idrar protein/kreatinin oranı, albümin, kolesterol, kreatinin, '
                                  'elektrolit, hemogram ve C3 istemek; enfeksiyon taraması yapmak',
                          'is_correct': True,
                          'explanation': 'Masif proteinüri ve hipoalbüminemi tanıyı doğrular. Hematüri, düşük C3, '
                                         'hipertansiyon ve kreatinin artışı atipik nedenleri düşündürür. Hematokrit '
                                         'yüksekliği hacim azlığını gösterir. Hepatit B, su çiçeği serolojisi ve '
                                         'tüberküloz taraması steroid öncesi önemlidir.',
                          'new_finding': 'Tam idrar: dansite 1030, protein 4+, eritrosit yok. İdrar protein/kreatinin '
                                         '8.4 mg/mg. Albümin 1.6 g/dL, kolesterol 380 mg/dL, kreatinin 0.4 mg/dL, Na '
                                         '133 mEq/L, hematokrit %42, C3 normal. HBsAg negatif, su çiçeği IgG negatif.'},
                         {'text': 'Tedaviye başlamadan önce acil perkütan böbrek biyopsisi planlamak ve histolojik '
                                  'tanıya göre tedavi seçmek',
                          'is_correct': False,
                          'scenario_update': 'Nefroloji, tipik başvuruda biyopsinin gerekmediğini belirtti; tedavi '
                                             'gecikti.',
                          'teaching_point': '1-10 yaş arası tipik başvuruda biyopsi yapılmadan steroid başlanır; '
                                            'biyopsi steroid direncinde düşünülür.'},
                         {'text': 'Asitin nedenini bulmak için kontrastlı batın tomografisi çekmek ve karaciğer '
                                  'hastalığını dışlamak için gastroenterolojiye danışmak',
                          'is_correct': False,
                          'scenario_update': 'Tomografi yaygın asit gösterdi; asıl tanı için idrar tetkiki '
                                             'yapılmamıştı.',
                          'teaching_point': 'Ödem ve asitli çocukta ilk tetkik tam idrardır; proteinüri tanıyı '
                                            'yönlendirir.'},
                         {'text': 'Tedavi kararı için 24 saatlik idrar toplamasını tamamlamak ve sonuç gelene kadar '
                                  'steroid dahil hiçbir tedavi başlamamak',
                          'is_correct': False,
                          'scenario_update': 'Bezli çocukta idrar toplama güvenilir yapılamadı; tedavi bir gün '
                                             'gecikti.',
                          'teaching_point': 'Spot idrar protein/kreatinin oranı küçük çocuklarda yeterli ve '
                                            'pratiktir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Masif proteinüri, albümin 1.6 g/dL, hiperkolesterolemi ve yaygın ödemi olan, hematürisi ve '
                         "hipertansiyonu olmayan, C3'ü normal bu çocukta tanı nedir?",
             'options': [{'text': 'Dilate kardiyomiyopatiye bağlı kalp yetmezliği',
                          'is_correct': False,
                          'scenario_update': 'Kalp muayenesi normal, hepatomegali ve galo yok; idrarda masif protein '
                                             'var.',
                          'teaching_point': 'Kalp yetmezliğine bağlı ödemde proteinüri ve ağır hipoalbüminemi '
                                            'beklenmez.'},
                         {'text': 'İlk atak idiyopatik nefrotik sendrom',
                          'is_correct': True,
                          'explanation': 'Masif proteinüri, hipoalbüminemi, ödem ve hiperlipidemi nefrotik sendromu '
                                         'tanımlar; yaş, hematüri ve hipertansiyon yokluğu ve normal C3 minimal '
                                         'değişiklik hastalığını düşündürür.',
                          'new_finding': 'Tanı: İlk Atak İdiyopatik Nefrotik Sendrom (olası minimal değişiklik '
                                         'hastalığı).'},
                         {'text': 'Akut glomerülonefrit',
                          'is_correct': False,
                          'scenario_update': 'Hematüri, hipertansiyon ve düşük C3 yok; masif proteinüri ön planda.',
                          'teaching_point': 'Glomerülonefritte hematüri, hipertansiyon ve oligüri baskındır.'},
                         {'text': 'Protein kaybettiren enteropati',
                          'is_correct': False,
                          'scenario_update': 'İdrarda masif protein kaybı var; ishal ve gastrointestinal yakınma yok.',
                          'teaching_point': 'Protein kaybettiren enteropatide idrarda protein beklenmez.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Damar içi hacmi korunmuş bu çocuğun tedavi planı hangisidir?',
             'options': [{'text': 'Steroid başlamadan önce proteinürinin kendiliğinden düzelip düzelmediğini görmek '
                                  'için iki hafta yalnızca tuzsuz diyetle izlemek',
                          'is_correct': False,
                          'scenario_update': 'Bekleme süresinde ödem arttı ve çocukta selülit gelişti.',
                          'teaching_point': 'Tipik ilk atakta steroid geciktirilmemelidir.'},
                         {'text': 'Oral prednizolon 60 mg/m²/gün başlamak, tuzu kısıtlamak, hareketi teşvik etmek ve '
                                  'enfeksiyon ile tromboz belirtileri konusunda aileyi eğitmek',
                          'is_correct': True,
                          'explanation': 'Steroid ilk atakta 4-6 hafta günlük, ardından 4-6 hafta gün aşırı verilir; '
                                         'çocukların çoğunda 2 hafta içinde remisyon sağlanır. Tuz kısıtlaması ödemi '
                                         'azaltır. Hareketsizlik tromboz riskini artırır. Ateş, karın ağrısı ve su '
                                         'çiçeği teması acil başvuru nedenidir.',
                          'new_finding': 'Prednizolon ve tuz kısıtlaması başlandı. Onuncu günde idrarda protein '
                                         'negatifleşti, diürez başladı ve ödem çözüldü. Aileye günlük idrar stiki ve '
                                         'uyarı belirtileri öğretildi.'},
                         {'text': 'İlk tedavi olarak siklofosfamid başlamak, steroidi yan etkileri nedeniyle vermemek '
                                  've proteinüri azalana kadar yatak istirahati önermek',
                          'is_correct': False,
                          'scenario_update': 'Siklofosfamid ilk basamak değildi; yatak istirahati sırasında çocukta '
                                             'derin ven trombozu gelişti.',
                          'teaching_point': 'İlk atakta tedavi steroiddir; ikinci basamak ilaçlar steroid bağımlılığı '
                                            'veya direncinde kullanılır.'},
                         {'text': 'Ödemin hızla çözülmesi için her çocukta rutin olarak günde iki kez albümin ve '
                                  'furosemid vermek ve sıvıyı kesin olarak kısıtlamak',
                          'is_correct': False,
                          'scenario_update': 'Rutin albümin-furosemid sonrası çocukta hacim azlığı ve hiponatremi '
                                             'gelişti.',
                          'teaching_point': 'Albümin ve diüretik yalnızca semptomatik ağır ödemde, hacim azlığı yoksa '
                                            've yakın izlemle kullanılır.'}]}]},
 {'id': 'S65',
  'category': '🧠 Nörolojik Aciller',
  'age': '7 Yaşında',
  'gender': 'Kız',
  'complaint': 'Bulantı ilacı sonrası başlayan boyunda kasılma, başın geriye-yana bükülmesi, gözlerin yukarı kayması '
               've konuşma güçlüğü',
  'history': "Ailesi anlatıyor: 'Dün geceden beri kusuyordu. Bugün aile hekimi bulantı için damla reçete etti; kusmaya "
             'devam edince önerilenin iki katı verdik. Yaklaşık iki saat sonra boynu sola kilitlendi, başı geriye '
             "büküldü, gözleri yukarı kaydı, aşağı bakamıyor. Dili kasılıyor, konuşamıyor ama bizi duyuyor, korkuyor.' "
             'Ateş, travma ve bilinç kaybı yok. Daha önce nöbet öyküsü yok. Tartı: 24 kg.',
  'final_diagnosis': 'İlaca Bağlı Akut Distonik Reaksiyon (Metoklopramid; Okülojirik Kriz ve Tortikolis)',
  'disposition': 'Sarı Alanda İntravenöz-İntramüsküler Antikolinerjik Tedavi, İlacın Kesilmesi ve 24-48 Saat Oral '
                 'Antikolinerjikle Taburculuk',
  'case_pearl': 'Dopamin antagonistleri (metoklopramid, proklorperazin, haloperidol) özellikle çocuk ve gençlerde, '
                'sıklıkla doz aşımında saatler içinde akut distoniye yol açar: tortikolis, okülojirik kriz, dil-çene '
                'kasılması ve opistotonus. Bilinç korunur ve bu nöbetten ayıran temel özelliktir. Laringeal distoni '
                'hava yolunu tehdit edebilir. Tedavi intravenöz veya intramüsküler difenhidramin (1 mg/kg) ya da '
                'biperidendir; yanıt dakikalar içindedir. Tekrarı önlemek için 24-48 saat oral antikolinerjik verilir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Bulantı damlası sonrası boynu kilitlenen ve gözleri yukarı kayan bu 7 yaşındaki kızda ilk '
                         'değerlendirmede neye odaklanırsınız?',
             'options': [{'text': 'Ensefalit olasılığı nedeniyle lomber ponksiyon yapmak ve sonuç gelene kadar '
                                  'intravenöz asiklovir başlamak',
                          'is_correct': False,
                          'scenario_update': 'Lomber ponksiyon sırasında çocuk kasılmalar nedeniyle pozisyon alamadı; '
                                             'ateş ve bilinç bozukluğu yoktu.',
                          'teaching_point': 'Ateşsiz, bilinci açık ve ilaç öyküsü belirgin çocukta santral sinir '
                                            'sistemi enfeksiyonu öncelikli düşünülmez.'},
                         {'text': 'Kaygılı görünümü nedeniyle tabloyu psikojenik kabul edip çocuğu sakinleştirmeye '
                                  'çalışmak ve ailesini dışarı çıkarmak',
                          'is_correct': False,
                          'scenario_update': 'Kasılmalar sürdü ve dil kasılması nedeniyle çocuk yutkunmakta zorlanmaya '
                                             'başladı.',
                          'teaching_point': 'Yeni ilaç sonrası gelişen kasılmalar organik bir neden olarak '
                                            'değerlendirilmelidir.'},
                         {'text': 'Gözlerin yukarı kayması nedeniyle tabloyu epileptik nöbet kabul edip intravenöz '
                                  'diazepam ve ardından fenitoin yüklemesi yapmak, nöbet sürerse levetirasetam eklemek',
                          'is_correct': False,
                          'scenario_update': 'Diazepam sonrası çocuk uykuya daldı ancak boyun ve göz kasılması sürdü; '
                                             'fenitoin yanıtsızdı.',
                          'teaching_point': 'Bilinç açıkken süren kasılma epileptik nöbet değildir; antiepileptikler '
                                            'bu tabloda etkisizdir.'},
                         {'text': 'Hava yolunu ve yutmayı değerlendirmek; bilinç, ateş, kas sertliği ve vital '
                                  'bulguları kontrol edip ilacın adını ve dozunu öğrenmek',
                          'is_correct': True,
                          'explanation': 'Laringeal tutulum hava yolunu tehdit edebilir. Korunmuş bilinç epileptik '
                                         'nöbetten ayırır. Ateş, yaygın rijidite ve otonomik bozukluk daha ağır bir '
                                         'ilaç reaksiyonunu düşündürür. İlaç öyküsü tanının anahtarıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 104/dk, SS 20/dk, SpO2 %99, TA 102/64 mmHg. '
                                         'Stridor yok, salyasını yutabiliyor. Bilinç tamamen açık, sorulara baş '
                                         'hareketiyle yanıt veriyor. Sola tortikolis, hafif retrokollis; gözler '
                                         'yukarıda fikse, aşağı bakamıyor. Dilde kasılma. Ekstremitelerde yaygın '
                                         'rijidite yok. Kullanılan damlanın bir dopamin antagonisti antiemetik olduğu '
                                         'öğrenildi.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Bilinci açık, ateşsiz, hava yolu güvenli ve ilaç öyküsü belirgin bu çocukta tetkik '
                         'yaklaşımınız nedir?',
             'options': [{'text': 'Geniş kapsamlı toksikoloji taraması göndermek ve sonuç gelene kadar çocuğu gözlem '
                                  'odasında tedavisiz izlemek',
                          'is_correct': False,
                          'scenario_update': 'Tarama sonucu ertesi güne kaldı; çocuk saatlerce kasılmalarla bekledi.',
                          'teaching_point': 'Öyküyle açıklanan tabloda rutin toksikoloji taraması tedaviyi '
                                            'geciktirmemelidir.'},
                         {'text': 'Kapiller kan şekeri, elektrolitler, kalsiyum ve magnezyum bakmak; ateş ve kas '
                                  'sertliği olmadığını kayda geçirip ek görüntüleme istememek',
                          'is_correct': True,
                          'explanation': 'Hipokalsemi ve hipomagnezemi kas spazmlarını taklit edebilir. Ateş, rijidite '
                                         've otonomik bozukluğun olmaması nöroleptik malign sendromu dışlamaya yardım '
                                         'eder. Tanı öyküye dayanır ve tedaviye hızlı yanıtla doğrulanır.',
                          'new_finding': 'Kan şekeri 98 mg/dL, Na 138, K 4.2 mEq/L, iyonize kalsiyum 1.22 mmol/L, '
                                         'magnezyum 2.0 mg/dL. Kreatin kinaz normal. Önerilen dozun iki katı alındığı '
                                         'doğrulandı.'},
                         {'text': 'Kafa içi patolojiyi dışlamak için acil beyin manyetik rezonansı ve '
                                  'elektroensefalografi istemek, nörolojiye danışıp sonuçlar çıkana kadar hiçbir '
                                  'tedavi vermemek',
                          'is_correct': False,
                          'scenario_update': 'Görüntüleme ve EEG için saatlerce beklendi; kasılmalar sürdü.',
                          'teaching_point': 'Tipik ilaç öyküsü ve korunmuş bilinçte görüntüleme ve EEG gerekmez; '
                                            'tedavi tanısaldır.'},
                         {'text': 'Boyun kasılması nedeniyle servikal omurga grafisi ve tomografi çekmek, ardından '
                                  'ortopediye danışmak',
                          'is_correct': False,
                          'scenario_update': 'Görüntüleme normal geldi; travma öyküsü olmadığı için tetkikler '
                                             'gereksizdi.',
                          'teaching_point': 'Travmasız, ilaçla ilişkili tortikoliste omurga görüntülemesi gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Önerilen dozun iki katı bulantı damlası (metoklopramid) aldıktan sonra bilinci açıkken '
                         'tortikolis, okülojirik kriz ve dil kasılması gelişen bu çocukta tanı nedir?',
             'options': [{'text': 'Fokal epileptik nöbet',
                          'is_correct': False,
                          'scenario_update': 'Bilinç tamamen açık, kasılmalar sürekli ve ilaç alımı sonrası başladı.',
                          'teaching_point': 'Uzun süren fokal nöbetlerde genellikle ritmik kasılmalar ve bilinç '
                                            'değişikliği görülür.'},
                         {'text': 'Nöroleptik malign sendrom',
                          'is_correct': False,
                          'scenario_update': 'Ateş, yaygın kurşun boru rijiditesi, otonomik bozukluk ve kreatin kinaz '
                                             'yüksekliği yok.',
                          'teaching_point': 'Nöroleptik malign sendrom ateş, rijidite, bilinç değişikliği ve otonomik '
                                            'instabiliteyle seyreder.'},
                         {'text': 'Hipokalsemik tetani',
                          'is_correct': False,
                          'scenario_update': 'İyonize kalsiyum ve magnezyum normal; karpopedal spazm yok.',
                          'teaching_point': 'Tetanide el-ayak spazmı, Chvostek ve Trousseau bulguları görülür.'},
                         {'text': 'İlaca bağlı akut distonik reaksiyon',
                          'is_correct': True,
                          'explanation': 'Dopamin antagonisti alımından saatler sonra gelişen, bilincin korunduğu '
                                         'tortikolis, okülojirik kriz ve dil kasılması akut distonik reaksiyonu '
                                         'doğrular.',
                          'new_finding': 'Tanı: İlaca Bağlı Akut Distonik Reaksiyon (metoklopramid).'}]},
            {'stage_title': 'Tedavi ve Taburculuk',
             'question': 'Bu çocuğun tedavisi nasıl olmalıdır?',
             'options': [{'text': 'Kasılmalar kendiliğinden geçeceği için yalnızca intravenöz sıvı ve parasetamol '
                                  'vermek, ilacın bir sonraki dozunu evde yarıya indirerek sürdürmeyi önermek',
                          'is_correct': False,
                          'scenario_update': 'Kasılmalar saatlerce sürdü; yarım dozla yeniden başlanan ilaç reaksiyonu '
                                             'tekrarlattı.',
                          'teaching_point': 'Neden olan ilaç kesilmeli ve antikolinerjikle hızla tedavi edilmelidir.'},
                         {'text': 'Yüksek doz intravenöz midazolam infüzyonu başlamak, kasılma geçmezse kas gevşetici '
                                  'ile entübasyon hazırlığı yapmak',
                          'is_correct': False,
                          'scenario_update': 'Midazolam çocuğu derin sedasyona soktu ancak distoniyi çözmedi; solunum '
                                             'depresyonu gelişti.',
                          'teaching_point': 'Benzodiazepinler ikinci basamak destek tedavidir; ilk seçenek '
                                            'antikolinerjiktir.'},
                         {'text': 'İlacı kesip intravenöz difenhidramin 1 mg/kg veya biperiden vermek, tekrarı önlemek '
                                  'için 24-48 saat oral antikolinerjik reçete etmek',
                          'is_correct': True,
                          'explanation': 'Antikolinerjik ilaçlar dopamin-asetilkolin dengesini düzelterek dakikalar '
                                         'içinde distoniyi çözer. İlacın etkisi sürebileceği için reaksiyon '
                                         'tekrarlayabilir; kısa süreli oral tedavi önerilir. Aileye bu ilacı tekrar '
                                         'kullanmamaları söylenir.',
                          'new_finding': 'İntravenöz difenhidramin sonrası 10 dakikada boyun ve göz kasılması çözüldü, '
                                         'çocuk konuşmaya başladı. İki saat gözlem sonrası oral antikolinerjikle '
                                         'taburcu edildi; kayda ilaç reaksiyonu işlendi.'},
                         {'text': 'Kasılmaları çözmek için intravenöz dantrolen başlamak ve çocuğu yoğun bakım '
                                  'ünitesinde izlemek',
                          'is_correct': False,
                          'scenario_update': 'Dantrolen bu tabloda etkisizdi; çocuk gereksiz yere yoğun bakıma '
                                             'yatırıldı.',
                          'teaching_point': 'Dantrolen malign hipertermi ve seçilmiş nöroleptik malign sendrom '
                                            'olgularında kullanılır.'}]}]},
 {'id': 'S66',
  'category': '🩸 Hematolojik & Onkolojik Aciller',
  'age': '6 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Lösemi tedavisi alan çocukta üşüme-titreme ile başlayan 38.9°C ateş ve halsizlik',
  'history': "Ailesi anlatıyor: 'Akut lenfoblastik lösemi tedavisi alıyor, son kemoterapisini 9 gün önce aldı. "
             'Göğsünde port var. Bir saat önce titreyerek ateşlendi, 38.9°C ölçtük. Halsiz, yemek yemiyor. Port '
             "bölgesinde kızarıklık yok.' Öksürük, ishal ve idrar yakınması yok. Hematoloji ateşlenirse hemen "
             'gelmelerini söylemiş. Penisilin alerjisi yok. Tartı: 20 kg.',
  'final_diagnosis': 'Kemoterapi Sonrası Febril Nötropeni (Yüksek Risk, Santral Venöz Kateterli)',
  'disposition': 'Sarı Alanda İlk 60 Dakikada Kültür Sonrası İntravenöz Antipsödomonal Beta-Laktam ile Çocuk '
                 'Hematoloji-Onkoloji Yatışı',
  'case_pearl': 'Kemoterapi alan çocukta tek ölçümde ≥38.3°C ya da bir saat süren ≥38.0°C ateş ve mutlak nötrofil '
                "sayısı <500/mm³ (veya 48 saatte <500'e düşmesi beklenen) acil durumdur. Nötropenik hastada "
                'enflamasyon bulguları silik olabilir; ilk belirti yalnızca ateştir. Kan kültürü (kateterin tüm '
                'lümenlerinden, mümkünse periferden) alındıktan sonra antipsödomonal beta-laktam monoterapisi '
                '(sefepim, piperasilin-tazobaktam) başvurudan itibaren 60 dakika içinde verilmelidir. Hipotansiyon, '
                'kateter giriş yeri enfeksiyonu veya MRSA kolonizasyonunda vankomisin eklenir. Rektal ölçüm ve rektal '
                'muayene yapılmaz.',
  'steps': [{'stage_title': 'Triaj ve İlk Değerlendirme',
             'question': 'Kemoterapi alan, portu olan ve titreyerek ateşlenen bu çocukta ilk yaklaşımınız nedir?',
             'options': [{'text': 'Ateşin nedenini netleştirmek için önce tam kan sayımı sonucunu beklemek, nötrofil '
                                  'düşükse antibiyotik başlamayı değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Hemogram sonucu 75 dakika sonra çıktı; antibiyotik penceresi kaçırıldı.',
                          'teaching_point': 'Ampirik antibiyotik nötrofil sonucunu beklemeden, başvurudan itibaren 60 '
                                            'dakika içinde verilmelidir.'},
                         {'text': 'Hemen izole odaya almak; perfüzyonu değerlendirmek, port bölgesi, ağız, deri ve '
                                  'perianal bölgeyi rektal muayene yapmadan incelemek',
                          'is_correct': True,
                          'explanation': 'Bağışıklığı baskılanmış çocuk enfeksiyondan korunmalı ve şok açısından hızla '
                                         'değerlendirilmelidir. Mukozit, kateter enfeksiyonu, selülit ve perianal apse '
                                         'sık odaklardır. Rektal girişim bakteriyemi riski nedeniyle yapılmaz.',
                          'new_finding': 'Vital Bulgular: Ateş 38.9°C, KTA 136/dk, SS 24/dk, SpO2 %98, TA 98/58 mmHg, '
                                         'KDZ 2 sn. Bilinç açık, halsiz. Ağızda hafif mukozit, port giriş yeri temiz, '
                                         'kızarıklık ve hassasiyet yok. Akciğer sesleri doğal. Perianal bölgede '
                                         'kızarıklık yok. Deri lezyonu yok.'},
                         {'text': 'Ateşin doğruluğunu kontrol etmek için rektal ölçüm yapmak ve olası perianal odağı '
                                  'aramak için parmakla rektal muayene uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Rektal muayene sonrası mukozada küçük bir kanama oldu; bakteriyemi riski '
                                             'arttı.',
                          'teaching_point': 'Nötropeni olasılığı olan çocukta rektal ölçüm, rektal muayene ve fitil '
                                            'kullanılmaz.'},
                         {'text': 'Bekleme salonunda sıra beklemesine izin vermek, ateş düşürücü verip bir saat sonra '
                                  'ateşi kontrol ederek hekime almak',
                          'is_correct': False,
                          'scenario_update': 'Bekleme salonunda geçen 80 dakikada çocukta taşikardi ve soğuk '
                                             'ekstremiteler gelişti.',
                          'teaching_point': 'Kemoterapi alan ateşli çocuk triajda öncelikli alınır; antibiyotiğe kadar '
                                            'geçen süre sağkalımı etkiler.'}]},
            {'stage_title': 'Kültürler ve Antibiyotik Zamanlaması',
             'question': 'Hemodinamisi şu an stabil olan bu çocukta tetkik ve tedavi sıralaması nasıl olmalıdır?',
             'options': [{'text': 'Ateş kaynağını göstermek için önce akciğer grafisi, batın ultrasonu ve '
                                  'ekokardiyografi yaptırmak, odak bulunursa antibiyotik seçmek',
                          'is_correct': False,
                          'scenario_update': 'Görüntülemeler iki saat sürdü ve odak bulunamadı; antibiyotik gecikti.',
                          'teaching_point': 'Bu hastaların çoğunda odak bulunmaz; ampirik tedavi görüntüleme '
                                            'beklenmeden başlanır.'},
                         {'text': 'Kültür alamadan portu çıkarmak için cerrahiye danışmak ve kateter ucu kültürü '
                                  'gelene kadar antibiyotiği ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Cerrahi görüş saatler aldı; port yerinde enfeksiyon bulgusu yoktu ve '
                                             'çıkarılması gereksizdi.',
                          'teaching_point': 'Kateter çıkarılması tünel enfeksiyonu, septik tromboz veya dirençli '
                                            'bakteriyemide gündeme gelir.'},
                         {'text': 'Port ve periferden kan kültürü, hemogram, CRP ve biyokimya almak; 60 dakika içinde '
                                  'antipsödomonal antibiyotik başlamak',
                          'is_correct': True,
                          'explanation': 'Kültürler antibiyotik öncesinde alınır ancak tedaviyi geciktirmemelidir. '
                                         'İdrar kültürü idrar sondası olmadan alınabiliyorsa gönderilir. Akciğer '
                                         'grafisi solunum bulgusu varsa çekilir.',
                          'new_finding': 'Kültürler alındı, başvurunun 40. dakikasında antibiyotik verildi. Lökosit '
                                         '400/mm³, mutlak nötrofil sayısı 162/mm³, Hb 8.4 g/dL, trombosit 38.000/mm³, '
                                         'CRP 46 mg/L. Laktat 1.6 mmol/L. Kreatinin ve karaciğer testleri normal. Tam '
                                         'idrar normal.'},
                         {'text': 'Ateşli ancak iyi görünen çocuğa oral amoksisilin-klavulanat verip ertesi gün '
                                  'hematoloji polikliniğine kontrole göndermek',
                          'is_correct': False,
                          'scenario_update': 'Gece evde çocuk hipotansif hale geldi ve septik şokla getirildi.',
                          'teaching_point': 'Yüksek riskli hastada ilk tedavi yatırılarak intravenöz yoldan '
                                            'verilir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Kemoterapiden 9 gün sonra 38.9°C ateşi ve mutlak nötrofil sayısı 162/mm³ olan, belirgin '
                         'odağı bulunmayan bu çocukta tanı nedir?',
             'options': [{'text': 'Kateter ilişkili tünel enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Port giriş yeri ve tünel hattında kızarıklık, hassasiyet veya akıntı '
                                             'yok.',
                          'teaching_point': 'Tünel enfeksiyonunda kateter hattı boyunca selülit görülür.'},
                         {'text': 'Kemoterapiye bağlı ilaç ateşi',
                          'is_correct': False,
                          'scenario_update': 'Son kemoterapiden 9 gün geçmiş ve ağır nötropeni var; enfeksiyon '
                                             'dışlanmadan bu tanı konmaz.',
                          'teaching_point': 'Nötropenik hastada ateş, aksi kanıtlanana kadar enfeksiyon kabul edilir.'},
                         {'text': 'Kemoterapi sonrası febril nötropeni',
                          'is_correct': True,
                          'explanation': "Kemoterapi alan çocukta ≥38.3°C ateş ve mutlak nötrofil sayısının 500/mm³'ün "
                                         'altında olması febril nötropeniyi tanımlar.',
                          'new_finding': 'Tanı: Kemoterapi Sonrası Febril Nötropeni (yüksek risk, santral venöz '
                                         'kateterli).'},
                         {'text': 'Tümör lizis sendromu',
                          'is_correct': False,
                          'scenario_update': 'Potasyum, fosfor, ürik asit ve kreatinin normal; tedavinin başlangıç '
                                             'dönemi değil.',
                          'teaching_point': 'Tümör lizis sendromu genellikle tedavinin ilk günlerinde metabolik '
                                            'bozukluklarla ortaya çıkar.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu çocuğun tedavi planı hangisidir?',
             'options': [{'text': 'Nötrofil sayısını hızla artırmak için granülosit transfüzyonu yapmak ve '
                                  'antibiyotiği yalnızca kültür üremesi olursa başlamak',
                          'is_correct': False,
                          'scenario_update': 'Granülosit transfüzyonu bu aşamada endike değildi; antibiyotiksiz kalan '
                                             'çocukta tablo ağırlaştı.',
                          'teaching_point': 'Kültür sonucu beklenmeden ampirik antibiyotik sürdürülmelidir.'},
                         {'text': 'Tek doz intravenöz seftriakson verip çocuğu evde oral siprofloksasinle izlemek ve '
                                  '48 saat sonra yeniden değerlendirmek',
                          'is_correct': False,
                          'scenario_update': "Seftriakson Pseudomonas'ı kapsamadı; evde ateşi süren çocuk yeniden "
                                             'başvurdu.',
                          'teaching_point': 'Ayaktan tedavi yalnızca düşük riskli seçilmiş hastalarda düşünülür; '
                                            'lösemide indüksiyon ve kateter yüksek risktir.'},
                         {'text': 'İlk tedaviye rutin olarak vankomisin, amikasin ve amfoterisin B eklemek ve tüm '
                                  'antibiyotikleri en az üç hafta sürdürmek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz kombinasyon tedavisi sonrası kreatinin yükseldi ve işitme '
                                             'testinde bozulma saptandı.',
                          'teaching_point': 'Stabil hastada monoterapi yeterlidir; rutin kombinasyon toksisiteyi '
                                            'artırır.'},
                         {'text': 'Sefepim veya piperasilin-tazobaktam monoterapisini sürdürüp hematoloji servisine '
                                  'yatırmak; hipotansiyon veya kateter enfeksiyonu gelişirse vankomisin eklemek',
                          'is_correct': True,
                          'explanation': 'Antipsödomonal beta-laktam monoterapisi ilk seçenektir. Rutin vankomisin '
                                         'önerilmez; hemodinamik bozulma, kateter giriş yeri enfeksiyonu, pnömoni veya '
                                         'gram pozitif üreme durumunda eklenir. 96 saati aşan ateşte mantar '
                                         'enfeksiyonu araştırılır.',
                          'new_finding': 'Sefepim ile 48. saatte ateş düştü, kan kültürü negatif kaldı. Nötrofil '
                                         "sayısı 7. günde 600/mm³'ün üzerine çıktı ve antibiyotik kesildi."}]}]},
 {'id': 'S67',
  'category': '🩸 Hematolojik & Onkolojik Aciller',
  'age': '9 Yaşında',
  'gender': 'Kız',
  'complaint': 'Bacaklarda, sırtta ve göğüste dayanılmaz ağrı; evde verilen ağrı kesicilere yanıt yok',
  'history': "Ailesi anlatıyor: 'Kalıtsal bir kan hastalığı var, hidroksiüre kullanıyor. Dün akşam soğuk havada okul "
             'gezisinden döndükten sonra bacaklarında ve belinde ağrı başladı. Evde ibuprofen ve parasetamol verdik, '
             "geçmedi. Ağrısı 10 üzerinden 9 diyor, ağlıyor, yürüyemiyor.' Bugün az su içmiş. Ateş, öksürük ve nefes "
             'darlığı yok. Önceki ağrı ataklarında morfin almış. Bilinen hemoglobin değeri 7.8 g/dL. Tartı: 28 kg.',
  'final_diagnosis': 'Orak Hücre Anemisinde Akut Vazo-Oklüzif Ağrı Krizi',
  'disposition': 'Sarı Alanda 60 Dakika İçinde İntravenöz Opioid, NSAİİ, İdame Sıvı ve Teşvik Spirometrisi ile Çocuk '
                 'Hematoloji Yatışı',
  'case_pearl': 'Orak hücre hastalığında soğuk, dehidratasyon, enfeksiyon ve stres vazo-oklüzyonu tetikler. Ağrı '
                'krizinde hedef, triajdan sonraki 60 dakika içinde (ideal 30 dakika) intravenöz veya intranazal opioid '
                'vermek ve 15-30 dakikada bir yeniden değerlendirmektir. Aşırı sıvı akut göğüs sendromunu '
                'tetikleyebileceği için idame sıvı verilir. Teşvik spirometrisi akut göğüs sendromunu önler. Ateş '
                "fonksiyonel aspleni nedeniyle acil kabul edilir. Hb'nin bazal değerden ≥2 g/dL düşmesi dalak "
                'sekestrasyonu veya aplastik krizi düşündürür.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Ağrı Yönetimi',
             'question': 'Bilinen kalıtsal kan hastalığı olan ve şiddetli ağrıyla gelen bu çocukta ilk yaklaşımınız '
                         'nedir?',
             'options': [{'text': 'Dehidratasyonu düzeltmek için iki kez 20 mL/kg serum fizyolojik bolusu vermek, ağrı '
                                  'kesiciyi sıvı tamamlanıp idrar çıkışı görüldükten sonra başlamak',
                          'is_correct': False,
                          'scenario_update': "Hızlı sıvı yüklemesi sonrası solunum hızı arttı, satürasyon %92'ye "
                                             'düştü; ağrı tedavisi gecikti.',
                          'teaching_point': 'Aşırı sıvı akciğer komplikasyonunu tetikleyebilir; ağrı kesici sıvıyı '
                                            'beklemeden verilir.'},
                         {'text': 'Vital bulgular, ağrı skoru, göğüs ve dalak muayenesini yapıp 30 dakika içinde '
                                  'intravenöz morfin vermek ve sık yeniden değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Şiddetli ağrı hızla opioidle tedavi edilir. Göğüs muayenesi akut göğüs '
                                         'sendromu, dalak boyutu sekestrasyon açısından önemlidir. Ateş ve nörolojik '
                                         'bulgu ayrı aciller gerektirir. NSAİİ böbrek fonksiyonu normalse eklenir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.4°C, KTA 118/dk, SS 22/dk, SpO2 %96 (bazal %97), TA '
                                         '108/66 mmHg. Konjonktivalar soluk, sklerada hafif sarılık. Akciğer sesleri '
                                         'doğal. Dalak ele gelmiyor. Nörolojik muayene normal. Alt ekstremite ve '
                                         'lomber bölgede yaygın hassasiyet, şişlik yok. Ağrı skoru 9/10. Morfin 0.1 '
                                         'mg/kg intravenöz verildi.'},
                         {'text': 'Ağrının gerçekliğini anlamak için bir saat gözlemlemek ve ağrı kesici talebini '
                                  'bağımlılık riski açısından sorgulamak',
                          'is_correct': False,
                          'scenario_update': 'Analjezi gecikti; çocuğun ağrısı arttı ve aile güvenini kaybetti.',
                          'teaching_point': 'Bu hastalarda ağrı öznel bildirime göre tedavi edilir; analjezi gecikmesi '
                                            'sık ve önlenebilir bir hatadır.'},
                         {'text': 'Ağrıyı hafifletmek için ağrılı bölgelere buz uygulamak ve ağrı kesici olarak '
                                  'yalnızca intramüsküler diklofenak yapmak',
                          'is_correct': False,
                          'scenario_update': 'Soğuk uygulama damar daralmasını artırdı ve ağrı kötüleşti; tek başına '
                                             'NSAİİ yetersiz kaldı.',
                          'teaching_point': 'Soğuk uygulama tetikleyicidir; şiddetli ağrıda opioid gerekir ve '
                                            'intramüsküler yol önerilmez.'}]},
            {'stage_title': 'Laboratuvar Değerlendirmesi',
             'question': 'Analjezi başlanan bu çocukta hangi tetkikler öncelikli olarak istenmelidir?',
             'options': [{'text': 'Ağrılı bölgelerin tamamından direkt grafi çekmek ve kırık saptanmazsa analjeziyi '
                                  'azaltarak çocuğu taburcu etmeyi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Grafiler normal geldi; analjezi azaltılınca ağrı yeniden şiddetlendi.',
                          'teaching_point': 'Normal grafi ağrı krizini dışlamaz; analjezi klinik yanıta göre '
                                            'ayarlanır.'},
                         {'text': 'Ağrının nedenini görmek için tüm vücut kemik sintigrafisi ve lomber manyetik '
                                  'rezonans çekmek, sonuçlara göre analjezi dozunu ayarlamak',
                          'is_correct': False,
                          'scenario_update': 'Tetkikler gereksizdi; çocuk saatlerce görüntüleme biriminde bekletildi.',
                          'teaching_point': 'Tipik ağrı ataklarında ileri görüntüleme gerekmez; osteomiyelit '
                                            'şüphesinde seçici kullanılır.'},
                         {'text': 'Yalnızca CRP ve prokalsitonin istemek, değerler yüksekse ağrıyı enfeksiyona '
                                  'bağlayıp geniş spektrumlu antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'Ateşsiz çocukta gereksiz antibiyotik başlandı; hemoglobin ve retikülosit '
                                             'değerlendirilmedi.',
                          'teaching_point': 'Ağrı krizinde inflamatuvar belirteçler yükselebilir; ateş yoksa '
                                            'antibiyotik gerekmez.'},
                         {'text': 'Hemogram ve retikülosit sayısı, biyokimya, bilirubin, LDH ve kan grubu-tarama '
                                  'istemek; bazal değerlerle karşılaştırıp göğüs muayenesini tekrarlamak',
                          'is_correct': True,
                          'explanation': "Hb'nin bazalden belirgin düşmesi sekestrasyon veya aplastik krizi, düşük "
                                         "retikülosit parvovirüs B19'u düşündürür. Kan grubu olası transfüzyon için "
                                         'hazırlıktır. Göğüs ağrısı, ateş veya hipoksi gelişirse akciğer grafisi '
                                         'çekilir.',
                          'new_finding': 'Hb 7.6 g/dL (bazal 7.8), retikülosit %9.2, lökosit 13.800/mm³, trombosit '
                                         '410.000/mm³. Total bilirubin 3.1 mg/dL (indirekt ağırlıklı), LDH 620 U/L, '
                                         'kreatinin 0.4 mg/dL. Kan grubu ve antikor taraması gönderildi. Morfin '
                                         'sonrası ağrı skoru 5/10.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Hidroksiüre kullanan, soğuk ve sıvı azlığı sonrası yaygın kemik ağrısı başlayan, Hb bazale '
                         'yakın, retikülositi yüksek ve göğüs bulgusu olmayan bu çocukta tanı nedir?',
             'options': [{'text': 'Parvovirüs B19 ilişkili aplastik kriz',
                          'is_correct': False,
                          'scenario_update': 'Retikülosit sayısı yüksek ve Hb düşmemiş.',
                          'teaching_point': 'Aplastik krizde retikülosit belirgin düşer ve Hb hızla azalır.'},
                         {'text': 'Akut göğüs sendromu',
                          'is_correct': False,
                          'scenario_update': 'Göğüs ağrısı, ateş, hipoksi ve akciğer bulgusu yok.',
                          'teaching_point': 'Akut göğüs sendromunda grafide yeni infiltrat ile ateş veya solunum '
                                            'bulgusu birlikte bulunur.'},
                         {'text': 'Orak hücre hastalığında vazo-oklüzif ağrı krizi',
                          'is_correct': True,
                          'explanation': 'Tetikleyici sonrası yaygın kemik ağrısı, bazal düzeyde Hb, yüksek '
                                         'retikülosit ve hemoliz bulguları ile göğüs ve dalak bulgusu olmaması akut '
                                         'vazo-oklüzif krizi doğrular.',
                          'new_finding': 'Tanı: Orak Hücre Anemisinde Akut Vazo-Oklüzif Ağrı Krizi.'},
                         {'text': 'Akut dalak sekestrasyonu',
                          'is_correct': False,
                          'scenario_update': 'Dalak ele gelmiyor ve Hb bazal değere yakın.',
                          'teaching_point': 'Dalak sekestrasyonunda dalak hızla büyür ve Hb bazalden ≥2 g/dL düşer.'}]},
            {'stage_title': 'Tedavi ve İzlem',
             'question': 'Ağrısı kısmen gerileyen bu çocuğun yatış tedavisi nasıl olmalıdır?',
             'options': [{'text': 'Oksijen satürasyonu normal olmasına karşın tüm hastalara rutin yüksek akımlı '
                                  'oksijen vermek ve intravenöz sıvıyı iki katı idamede tutmak',
                          'is_correct': False,
                          'scenario_update': 'Fazla sıvı ile çocukta raller ve hipoksi gelişti.',
                          'teaching_point': 'Oksijen yalnızca hipokside verilir; sıvı idame hızını belirgin '
                                            'aşmamalıdır.'},
                         {'text': 'Morfin hasta kontrollü analjezi ve düzenli NSAİİ vermek, idame sıvıyla devam etmek, '
                                  'saatlik teşvik spirometrisi ve satürasyon izlemi uygulamak',
                          'is_correct': True,
                          'explanation': 'Düzenli analjezi ağrıyı kontrol eder. İdame sıvı dehidratasyonu düzeltir '
                                         'ancak akciğer ödemine yol açmaz. Teşvik spirometrisi atelektaziyi ve akut '
                                         'göğüs sendromunu önler. Opioid kullanırken sedasyon ve solunum izlenir.',
                          'new_finding': 'Hasta kontrollü analjezi, ibuprofen ve idame sıvı başlandı, teşvik '
                                         "spirometrisi öğretildi. 48. saatte ağrı skoru 3/10'a indi, oral analjeziye "
                                         'geçildi. Akut göğüs sendromu gelişmedi; dördüncü gün taburcu edildi.'},
                         {'text': 'Solunum depresyonu riski nedeniyle opioidleri kesip yalnızca parasetamol vermek ve '
                                  'hastayı yatakta hareketsiz tutmak',
                          'is_correct': False,
                          'scenario_update': 'Ağrı kontrol edilemedi; hareketsiz kalan çocukta yüzeyel solunum ve '
                                             'atelektazi gelişti.',
                          'teaching_point': 'Yeterli analjezi ve erken mobilizasyon akciğer komplikasyonlarını '
                                            'azaltır.'},
                         {'text': 'Anemiyi düzeltmek için hemen 20 mL/kg eritrosit süspansiyonu vermek ve hemoglobini '
                                  "12 g/dL'nin üzerine çıkarmak",
                          'is_correct': False,
                          'scenario_update': 'Yüksek hemoglobin kan viskozitesini artırdı ve ağrı kötüleşti.',
                          'teaching_point': 'Komplikasyonsuz ağrı krizinde transfüzyon endike değildir; hedef Hb 10 '
                                            "g/dL'yi aşmamalıdır."}]}]},
 {'id': 'S68',
  'category': '👶 Yenidoğan Acilleri',
  'age': '3 Günlük',
  'gender': 'Erkek',
  'complaint': 'Doğumdan sonraki ilk gün başlayan ve hızla koyulaşan sarılık, uykuya meyil ve emmede azalma',
  'history': "Ailesi anlatıyor: 'Miadında, normal doğumla 3400 gram doğdu. Doğumdan yaklaşık 20 saat sonra yüzü "
             'sararmaya başladı, taburcu olurken söylemiştik ama kontrole çağırdılar. Sarılık bugün karnına ve '
             "bacaklarına yayıldı. Daha uykulu, emmesi azaldı.' Sadece anne sütü alıyor, günde 6 ıslak bez. Kaka rengi "
             'sarı. Annenin kan grubu O Rh pozitif, bebeğinki bilinmiyor. Ağabeyi de yenidoğanda ışık tedavisi almış. '
             'Tartı: 3180 g (doğum ağırlığının %6.5 altı).',
  'final_diagnosis': 'ABO Uyuşmazlığına Bağlı Ağır İndirekt Hiperbilirubinemi (Hemolitik Hastalık)',
  'disposition': 'Sarı Alanda Yoğun Fototerapi Başlanarak Kan Değişimi Hazırlığı ile Yenidoğan Yoğun Bakım Yatışı',
  'case_pearl': 'İlk 24 saatte başlayan sarılık her zaman patolojiktir ve en sık hemolitik hastalığa bağlıdır. Anne O, '
                'bebek A veya B grubu olduğunda direkt Coombs pozitifliği ABO uyuşmazlığını destekler. Tedavi eşikleri '
                'AAP 2022 kılavuzunda doğum haftası, saatlik yaş ve nörotoksisite risk faktörlerine (hemoliz, albümin '
                '<3 g/dL, sepsis, letarji) göre belirlenir. Bilirubin kan değişimi eşiğinin 2 mg/dL altına '
                "yaklaştığında 'eskalasyon bakımı' başlar: yoğun fototerapi, kan değişimi hazırlığı ve hemolizde İVİG. "
                'Akut bilirubin ensefalopatisi bulguları (hipertoni, opistotonus, tiz ağlama) varsa acil kan değişimi '
                'yapılır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'İlk gün başlayan ve hızla artan sarılıkla gelen, uykulu bu 3 günlük bebekte ilk '
                         'değerlendirmede neye odaklanırsınız?',
             'options': [{'text': 'Sarılığın derecesini deri rengine bakarak tahmin etmek, karnın altına inmediyse '
                                  'tetkik istemeden kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Görsel değerlendirme düzeyi olduğundan düşük tahmin etti; ölçüm '
                                             'yapılmadı.',
                          'teaching_point': 'Görsel değerlendirme güvenilir değildir; şüphede serum bilirubini '
                                            'ölçülmelidir.'},
                         {'text': 'Uykuya meyil nedeniyle önce menenjiti dışlamak için lomber ponksiyon yapmak ve '
                                  'sarılığın değerlendirmesini ponksiyon sonucu çıktıktan sonraya bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Lomber ponksiyon normal geldi; bu sürede sarılık düzeyi ölçülmedi.',
                          'teaching_point': 'Ağır sarılıklı letarjik yenidoğanda öncelik serum bilirubinini ölçüp '
                                            'tedaviye başlamaktır.'},
                         {'text': 'Sarılığı anne sütüne bağlamak, emzirmeyi iki gün kesip mama vermelerini ve bebeği '
                                  'güneş ışığına çıkarmalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Bebek eve gönderildi; ertesi gün tiz ağlama ve geriye kasılma ile '
                                             'getirildi.',
                          'teaching_point': 'İlk 24 saatte başlayan sarılık fizyolojik veya anne sütüne bağlı '
                                            'değildir; güneş ışığı tedavi değildir.'},
                         {'text': 'Vital bulgular ve hidrasyonu değerlendirmek; tonus, emme ve ağlamayı muayene edip '
                                  'sarılığın yaygınlığını ve hepatosplenomegaliyi incelemek',
                          'is_correct': True,
                          'explanation': 'Uykuya meyil ve emmede azalma bilirubin nörotoksisitesinin erken bulgusu '
                                         'olabilir. Hipertoni, opistotonus ve tiz ağlama ileri evreyi gösterir. '
                                         'Hepatosplenomegali hemolizi, ateş ve kötü görünüm sepsisi düşündürür.',
                          'new_finding': 'Vital Bulgular: Ateş 36.9°C, KTA 148/dk, SS 46/dk, SpO2 %98. Belirgin '
                                         'sarılık ayak tabanlarına kadar yayılmış. Hafif letarjik ancak '
                                         'uyarılabiliyor, emme refleksi zayıf; hipertoni, opistotonus ve tiz ağlama '
                                         'yok. Fontanel normal. Karaciğer 2 cm, dalak kot kavsinde ele geliyor. Sefal '
                                         'hematom yok.'}]},
            {'stage_title': 'Laboratuvar Değerlendirmesi',
             'question': 'Bu bebekte hangi tetkikler öncelikli olarak istenmelidir?',
             'options': [{'text': 'Biliyer atreziyi dışlamak için hepatobiliyer sintigrafi ve karın ultrasonu istemek, '
                                  'sonuç gelene kadar fototerapiyi ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Direkt bilirubin normal çıktı; sintigrafi gereksizdi ve tedavi gecikti.',
                          'teaching_point': 'Kolestaz tetkiki direkt bilirubin yüksekliğinde yapılır; indirekt '
                                            'sarılıkta fototerapi geciktirilmez.'},
                         {'text': 'Total ve direkt bilirubin, bebeğin kan grubu ve direkt Coombs testi, hemogram, '
                                  'retikülosit, yayma, albümin ve G6PD istemek',
                          'is_correct': True,
                          'explanation': 'Total bilirubin saatlik yaşa göre değerlendirilir. Direkt bilirubin '
                                         'kolestazı dışlar. Kan grubu ve Coombs immün hemolizi, yayma ve G6PD diğer '
                                         'hemoliz nedenlerini araştırır. Düşük albümin nörotoksisite riskini artırır.',
                          'new_finding': 'Total serum bilirubini 20.4 mg/dL (68. saat), direkt bilirubin 0.6 mg/dL. '
                                         'Bebek kan grubu A Rh pozitif, direkt Coombs pozitif. Hb 12.8 g/dL, '
                                         'retikülosit %8.6, yaymada sferositler. Albümin 3.2 g/dL, G6PD normal. Kan '
                                         'değişimi eşiği bu yaş ve risk için yaklaşık 21 mg/dL.'},
                         {'text': "Yalnızca transkutanöz bilirubin ölçmek ve değer 15 mg/dL'nin üzerinde çıkarsa 24 "
                                  'saat sonra serum düzeyini tekrar değerlendirmek, bu sürede emzirmeyi sürdürmelerini '
                                  'önermek',
                          'is_correct': False,
                          'scenario_update': 'Transkutanöz ölçüm yüksek düzeyde güvenilmez kaldı; tedavi bir gün '
                                             'gecikti.',
                          'teaching_point': 'Transkutanöz değer yüksekse veya tedavi eşiğine yakınsa serum bilirubini '
                                            'hemen ölçülmelidir.'},
                         {'text': 'Konjenital hipotiroidiyi dışlamak için tiroid fonksiyon testleri göndermek ve sonuç '
                                  'gelene kadar bebeği taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Tiroid testleri normal geldi; evde sarılık arttı.',
                          'teaching_point': 'Hipotiroidi uzamış sarılığın nedenidir; erken başlayan hızlı sarılığı '
                                            'açıklamaz.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'İlk 24 saatte başlayan sarılığı, 68. saatte total bilirubini 20.4 mg/dL, annesi O, kendisi A '
                         'grubu, direkt Coombs testi pozitif ve sferositleri olan bu bebekte tanı nedir?',
             'options': [{'text': 'Anne sütü sarılığı',
                          'is_correct': False,
                          'scenario_update': 'Sarılık ilk 24 saatte başladı ve Coombs pozitif hemoliz var.',
                          'teaching_point': 'Anne sütü sarılığı ilk haftadan sonra ortaya çıkan, iyi görünümlü bebekte '
                                            'uzamış sarılıktır.'},
                         {'text': 'Herediter sferositoz',
                          'is_correct': False,
                          'scenario_update': 'Direkt Coombs pozitif ve anne-bebek kan grubu uyumsuz.',
                          'teaching_point': 'Herediter sferositozda Coombs negatiftir ve aile öyküsünde splenektomi '
                                            'veya anemi bulunur.'},
                         {'text': 'ABO uyuşmazlığına bağlı hemolitik hiperbilirubinemi',
                          'is_correct': True,
                          'explanation': 'O grubu anne, A grubu bebek, pozitif direkt Coombs, retikülositoz, '
                                         'sferositler ve erken başlangıç ABO hemolitik hastalığını doğrular.',
                          'new_finding': 'Tanı: ABO Uyuşmazlığına Bağlı Ağır İndirekt Hiperbilirubinemi.'},
                         {'text': 'G6PD eksikliğine bağlı hemoliz',
                          'is_correct': False,
                          'scenario_update': 'G6PD düzeyi normal ve Coombs testi pozitif.',
                          'teaching_point': 'G6PD eksikliğinde Coombs negatiftir ve enzim düzeyi düşüktür.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bilirubini kan değişimi eşiğine yaklaşan bu bebeğin tedavi planı hangisidir?',
             'options': [{'text': 'Standart fototerapiyi evde vermek, beslenmeyi artırmalarını önermek ve 24 saat '
                                  'sonra bilirubin kontrolüne çağırmak',
                          'is_correct': False,
                          'scenario_update': "Evde bilirubin 25 mg/dL'ye yükseldi; bebek hipertoni ile getirildi.",
                          'teaching_point': 'Hemolizli ve eşiğe yakın bebekte ev fototerapisi uygun değildir.'},
                         {'text': 'Bilirubini düşürmek için fototerapi yerine bol miktarda %5 dekstrozlu su vermek ve '
                                  'fenobarbital başlamak',
                          'is_correct': False,
                          'scenario_update': 'Dekstrozlu su hiponatremiye yol açtı ve bilirubin düşmedi.',
                          'teaching_point': 'Su veya dekstroz takviyesi bilirubini düşürmez; fenobarbital akut '
                                            'tedavide yer almaz.'},
                         {'text': 'Bilirubin eşiğe yaklaştığı için fototerapi denemeden doğrudan acil kan değişimi '
                                  'yapmak ve emzirmeyi kalıcı olarak kesip mamaya geçirmek',
                          'is_correct': False,
                          'scenario_update': 'Ensefalopati bulgusu olmayan bebekte hazırlıksız işlem komplikasyon '
                                             'riskini artırdı.',
                          'teaching_point': 'Ensefalopati yoksa önce yoğun fototerapi ve İVİG uygulanır; emzirme '
                                            'sürdürülür.'},
                         {'text': 'Hemen yoğun fototerapi başlamak, kan değişimi için kan hazırlatmak, İVİG vermek ve '
                                  'bilirubini 2-3 saatte bir ölçmek',
                          'is_correct': True,
                          'explanation': 'Yoğun fototerapi bilirubini hızla düşürür. Kan değişimi eşiğine yaklaşılması '
                                         'eskalasyon bakımını gerektirir. İVİG immün hemolizi azaltarak kan değişimi '
                                         'gereksinimini düşürebilir. Bilirubin eşiği aşar veya ensefalopati bulgusu '
                                         'gelişirse kan değişimi yapılır.',
                          'new_finding': 'Yoğun fototerapi ve İVİG 0.5 g/kg verildi, kan değişimi için kan hazırlandı. '
                                         "Altıncı saatte bilirubin 17.1 mg/dL'ye geriledi ve kan değişimine gerek "
                                         'kalmadı. Bebek 72. saatte fototerapiden çıkarıldı; işitme taraması (ABR) '
                                         'planlandı.'}]}]},
 {'id': 'S69',
  'category': '💊 Toksikoloji & Metabolik / Endokrin Aciller',
  'age': '14 Günlük',
  'gender': 'Kız',
  'complaint': 'Birkaç gündür artan kusma, emmeme, kilo kaybı ve bugün belirgin halsizlik-uyuşukluk',
  'history': "Ailesi anlatıyor: 'Miadında, 3200 gram doğdu. Doğumda dış genital bölgesinin biraz farklı göründüğünü "
             'söylediler, kontrole çağırdılar ama gidemedik. Son üç gündür her beslenmeden sonra kusuyor, emmiyor. '
             "Bugün çok uyuşuk, ağlaması zayıf.' Ateş ve ishal yok. Kusmuk safralı değil. Anne-baba akraba. Tartı: "
             '2850 g (doğum ağırlığının %11 altı).',
  'final_diagnosis': 'Tuz Kaybettiren Konjenital Adrenal Hiperplazi (21-Hidroksilaz Eksikliği) ve Adrenal Kriz',
  'disposition': 'Sarı Alanda Sıvı Resüsitasyonu, İntravenöz Hidrokortizon ve Hiperkalemi Tedavisi ile Yenidoğan Yoğun '
                 'Bakım ve Çocuk Endokrinoloji Yatışı',
  'case_pearl': 'Yaşamın 1-3. haftasında kusma, dehidratasyon, hiponatremi, hiperkalemi ve hipoglisemi tuz kaybettiren '
                '21-hidroksilaz eksikliğini düşündürür; kız bebekte virilize genitalya ipucudur, erkekte genital bulgu '
                'olmayabilir. Tanı için tedavi öncesi kortizol, 17-OH progesteron, ACTH ve renin örneği alınır ancak '
                'tedavi bekletilmez. Hidrokortizon 50-100 mg/m² intravenöz verilir; yüksek dozda mineralokortikoid '
                'etkisi de vardır. Pilor stenozunda ise hipokloremik hipokalemik alkaloz beklenir; hiperkalemi ayırıcı '
                'tanıda anahtardır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Stabilizasyon',
             'question': 'Kusan, emmeyen ve uyuşuk bu 14 günlük bebekte ilk yaklaşımınız nedir?',
             'options': [{'text': 'Reflü olduğunu düşünüp beslenme miktarını azaltmalarını, mamayı koyulaştırmalarını '
                                  'önermek ve iki gün sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Evde bebek tepkisizleşti ve kardiyak arrest ile getirildi.',
                          'teaching_point': 'Kilo kaybı ve letarjisi olan kusan yenidoğan asla reflü kabul edilip '
                                            'gönderilmez.'},
                         {'text': 'Uyuşukluk nedeniyle sepsis kabul edip ampisilin ve sefotaksim vermek, sıvı ve şeker '
                                  'değerlendirmesini kan ve idrar kültürü sonuçlarının sonrasına bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik verildi ancak hipoglisemi ve elektrolit bozukluğu fark '
                                             'edilmedi; bebek nöbet geçirdi.',
                          'teaching_point': 'Sepsis olasılığında da glukoz, perfüzyon ve elektrolitler aynı anda '
                                            'değerlendirilmelidir.'},
                         {'text': 'Kusma nedeniyle pilor darlığını düşünüp önce batın ultrasonu istemek ve sonuç '
                                  'gelene kadar ağızdan beslenmeyi kesmek',
                          'is_correct': False,
                          'scenario_update': 'Ultrason sırasında bebek bradikardik oldu; şok ve elektrolit bozukluğu '
                                             'tedavisiz kaldı.',
                          'teaching_point': 'Şoktaki yenidoğanda önce resüsitasyon yapılır; tanısal görüntüleme '
                                            'stabilizasyonu geciktirmemelidir.'},
                         {'text': 'Perfüzyon ve dehidratasyonu değerlendirmek, kapiller kan şekeri ölçmek, monitörize '
                                  'edip damar yolu açmak ve genital bölgeyi muayene etmek',
                          'is_correct': True,
                          'explanation': 'Şok bulgusu ve hipoglisemi hemen tedavi edilmelidir. Monitör aritmiyi '
                                         'gösterir. Genital muayene etiyoloji için önemli bir ipucudur.',
                          'new_finding': 'Vital Bulgular: Ateş 36.4°C, KTA 186/dk, SS 52/dk, SpO2 %97, TA 58/30 mmHg, '
                                         'KDZ 4 sn, ekstremiteler soğuk ve alacalı. Fontanel çökük, mukozalar kuru. '
                                         'Letarjik. Kapiller kan şekeri 48 mg/dL. Monitörde sivri T dalgaları. '
                                         'Klitoromegali ve labioskrotal füzyon (Prader evre 3), gonad ele gelmiyor. '
                                         'Meme başı ve genital bölgede hiperpigmentasyon.'}]},
            {'stage_title': 'Laboratuvar ve Acil Müdahale',
             'question': 'Şoktaki, hipoglisemik ve monitörde sivri T dalgaları olan bu bebekte tetkik ve ilk müdahale '
                         'nasıl olmalıdır?',
             'options': [{'text': 'Tüm tetkiklerin sonuçlarını bekleyip kesin tanı konunca sıvı ve hormon tedavisine '
                                  'başlamak, bu sürede ağızdan şekerli su verip yakından izlemek',
                          'is_correct': False,
                          'scenario_update': 'Hormon sonuçları günler sürdü; bebek bu sürede kardiyak arrest geçirdi.',
                          'teaching_point': 'Krizde örnek saklanır ve tedavi sonuç beklenmeden hemen başlanır.'},
                         {'text': 'Hiperkalemiyi düzeltmek için önce potasyum bağlayıcı reçine (sodyum polistiren '
                                  'sülfonat) rektal vermek ve etkisini beklemek',
                          'is_correct': False,
                          'scenario_update': 'Reçinenin etkisi saatler aldı; bu sırada bebekte ventriküler aritmi '
                                             'gelişti.',
                          'teaching_point': 'EKG değişikliği olan hiperkalemide önce kalsiyum ile miyokard korunur; '
                                            'reçine yenidoğanda nekrotizan enterokolit riski taşır.'},
                         {'text': "Hiponatremiyi hızla düzeltmek için %3 NaCl ile sodyumu ilk 6 saatte 135 mEq/L'ye "
                                  'yükseltmek',
                          'is_correct': False,
                          'scenario_update': 'Hızlı düzeltme sonrası bebekte nörolojik bozulma görüldü.',
                          'teaching_point': "Kronik hiponatremi 24 saatte 8-10 mEq/L'yi aşmayacak şekilde düzeltilir; "
                                            'hipertonik salin yalnızca nöbette küçük dozlarda verilir.'},
                         {'text': 'Tedavi öncesi kortizol, 17-OH progesteron ve renin için kan saklayıp elektrolit '
                                  'bakmak; 10 mL/kg SF bolusu ve %10 dekstroz vermek',
                          'is_correct': True,
                          'explanation': 'Tedavi öncesi saklanan kan tanıyı tedaviyi geciktirmeden doğrulamayı sağlar. '
                                         'İzotonik sıvı hipovolemi ve hiponatremiyi, dekstroz hipoglisemiyi düzeltir. '
                                         'Yenidoğanda bolus 10 mL/kg ve yeniden değerlendirmeyle tekrarlanır.',
                          'new_finding': 'Kan gazı: pH 7.21, HCO3 14 mEq/L. Na 116 mEq/L, K 7.6 mEq/L, Cl 88 mEq/L, '
                                         'glukoz 48 mg/dL, BUN 42 mg/dL. Tedavi öncesi kan saklandı (17-OH progesteron '
                                         'sonucu 1 hafta sonra 186 ng/mL geldi). İki bolus sonrası KDZ 3 sn, TA 66/38 '
                                         'mmHg; kan şekeri 92 mg/dL.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'İkinci haftada kusma, şok, Na 116, K 7.6 mEq/L, hipoglisemi, metabolik asidoz, virilize '
                         'genitalya ve hiperpigmentasyonu olan bu kız bebekte tanı nedir?',
             'options': [{'text': 'Psödohipoaldosteronizm tip 1',
                          'is_correct': False,
                          'scenario_update': 'Genital virilizasyon ve hipoglisemi bu tabloyla açıklanmıyor.',
                          'teaching_point': 'Psödohipoaldosteronizmde tuz kaybı vardır ancak kortizol eksikliği ve '
                                            'virilizasyon yoktur.'},
                         {'text': 'Tuz kaybettiren konjenital adrenal hiperplazi krizi',
                          'is_correct': True,
                          'explanation': 'Hiponatremi, hiperkalemi, hipoglisemi, şok ile kız bebekte virilizasyon ve '
                                         'hiperpigmentasyon 21-hidroksilaz eksikliğine bağlı tuz kaybettiren krizi '
                                         'gösterir.',
                          'new_finding': 'Tanı: Tuz Kaybettiren Konjenital Adrenal Hiperplazi (21-hidroksilaz '
                                         'eksikliği), adrenal kriz.'},
                         {'text': 'Geç başlangıçlı yenidoğan sepsisi',
                          'is_correct': False,
                          'scenario_update': 'Ateş yok; elektrolit tablosu ve virilizasyon sepsisle açıklanmıyor.',
                          'teaching_point': 'Sepsis hiponatremi yapabilir ancak belirgin hiperkalemi ve genital '
                                            'virilizasyonu açıklamaz.'},
                         {'text': 'Hipertrofik pilor stenozu',
                          'is_correct': False,
                          'scenario_update': 'Hiperkalemi ve asidoz var; pilor darlığında hipokalemik alkaloz '
                                             'beklenir.',
                          'teaching_point': 'Pilor stenozunda hipokloremik hipokalemik metabolik alkaloz görülür ve '
                                            'genital bulgu olmaz.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu bebeğin tedavisi nasıl olmalıdır?',
             'options': [{'text': 'İntravenöz hidrokortizon 50-100 mg/m² vermek; EKG değişikliği için kalsiyum '
                                  'glukonat yapmak, elektrolitleri sık izlemek',
                          'is_correct': True,
                          'explanation': 'Yüksek doz hidrokortizon hem glukokortikoid hem mineralokortikoid etki '
                                         'sağlar. Kalsiyum glukonat miyokardı korur; sıvı ve kortizol potasyumu '
                                         'düşürür. Stabilizasyon sonrası idame hidrokortizon, fludrokortizon ve tuz '
                                         'başlanır; aileye stres dozu eğitimi verilir.',
                          'new_finding': 'Hidrokortizon 25 mg intravenöz ve kalsiyum glukonat verildi. Sivri T '
                                         'dalgaları geriledi. 24 saatte Na 126, K 5.4 mEq/L oldu, kan şekeri stabil '
                                         'kaldı. Fludrokortizon ve tuz eklendi; karyotip 46,XX geldi.'},
                         {'text': 'Hiperkalemi için insülin ve dekstrozu tek tedavi olarak vermek, hormon tedavisini '
                                  'genetik test sonucuna göre planlamak',
                          'is_correct': False,
                          'scenario_update': 'Potasyum geçici düştü ancak hormon eksikliği sürdüğü için yeniden '
                                             'yükseldi ve hipotansiyon tekrarladı.',
                          'teaching_point': 'Altta yatan hormon eksikliği tedavi edilmeden elektrolit düzeltmeleri '
                                            'kalıcı olmaz.'},
                         {'text': 'Deksametazonu tek doz verip hidrokortizon yerine idame tedavisi olarak sürdürmek ve '
                                  'sıvıyı kısıtlamak',
                          'is_correct': False,
                          'scenario_update': 'Deksametazon mineralokortikoid etki sağlamadı; tuz kaybı ve hiperkalemi '
                                             'sürdü.',
                          'teaching_point': 'Deksametazonun mineralokortikoid etkisi yoktur ve yenidoğanda büyümeyi '
                                            'baskılar; tercih hidrokortizondur.'},
                         {'text': 'Yalnızca oral fludrokortizon ve tuz takviyesi başlamak, glukokortikoidi '
                                  'endokrinoloji polikliniği görüşüne bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Kortizol eksikliği tedavi edilmedi; bebekte yeniden hipoglisemi ve '
                                             'hipotansiyon gelişti.',
                          'teaching_point': 'Krizde öncelik intravenöz hidrokortizondur; oral mineralokortikoid '
                                            'stabilizasyon sonrası eklenir.'}]}]},
 {'id': 'S70',
  'category': '💊 Toksikoloji & Metabolik / Endokrin Aciller',
  'age': '11 Yaşında',
  'gender': 'Kız',
  'complaint': 'Sabah uyanınca başlayan şiddetli baş ağrısı, bulantı-kusma, baş dönmesi ve banyoda kısa süreli bayılma',
  'history': "Ailesi anlatıyor: 'Kış tatilinde köydeki evimizdeyiz, odada sobayla ısınıyoruz, gece kapıyı pencereyi "
             'kapattık. Sabah kalkınca başı çok ağrıdı, kustu, banyoda birkaç saniye bayıldı. Bizim de başımız '
             "ağrıyor, küçük oğlum da kustu.' Ateş yok. Travma olmamış, düşerken başını çarpmamış. Kronik hastalığı "
             'yok. Tartı: 36 kg.',
  'final_diagnosis': 'Soba Kaynaklı Karbonmonoksit Zehirlenmesi (Senkop ile, Ağır)',
  'disposition': 'Sarı Alanda Geri Solumasız Maske ile %100 Oksijen, Hiperbarik Oksijen Merkezi ile Görüşme ve Aile '
                 'Bireylerinin Birlikte Değerlendirilmesi',
  'case_pearl': 'Kışın soba, şofben veya mangal kullanılan kapalı ortamda aynı evde birden fazla kişinin baş ağrısı, '
                'bulantı ve baş dönmesi karbonmonoksit zehirlenmesini düşündürür. Standart nabız oksimetresi '
                'karboksihemoglobini oksihemoglobinden ayıramaz ve satürasyon yanıltıcı biçimde normal görünür. Tanı '
                'kooksimetreli kan gazıyla konur. Tedavi hemen %100 oksijendir (yarı ömrü ~5 saatten ~75 dakikaya '
                'iner). Bilinç kaybı-senkop, nörolojik bulgu, miyokard iskemisi, gebelik veya karboksihemoglobin >%25 '
                'hiperbarik oksijen için değerlendirme gerektirir. Gecikmiş nörolojik sekel açısından izlem önerilir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Oksijenizasyon',
             'question': 'Sobalı kapalı odada uyuduktan sonra baş ağrısı, kusma ve bayılma ile gelen bu 11 yaşındaki '
                         'kızda ilk yaklaşımınız nedir?',
             'options': [{'text': 'Satürasyondan bağımsız olarak geri solumasız maskeyle %100 oksijen başlamak; '
                                  'bilinç, nörolojik muayene ve kardiyak ritmi değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Kapalı ortamda yanma ürünlerine maruziyet şüphesinde oksijen hemen başlanır. '
                                         'Nörolojik bulgu, senkop ve miyokard tutulumu ağırlığı belirler. '
                                         'Monitörizasyon iskemi ve aritmiyi yakalar.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 118/dk, SS 24/dk, nabız oksimetresi SpO2 '
                                         '%99, TA 112/70 mmHg. GKS 15, hafif konfüzyon dışında nörolojik muayene '
                                         'normal, fokal defisit yok. Deri rengi normal. Monitörde sinüs taşikardisi. '
                                         '%100 oksijen başlandı.'},
                         {'text': 'Nabız oksimetresi %99 gösterdiği için oksijen gereksinimi olmadığını kabul edip baş '
                                  'ağrısı için intravenöz parasetamol vermek',
                          'is_correct': False,
                          'scenario_update': 'Oksijen verilmeyen çocukta baş ağrısı arttı ve bilinç bulanıklığı '
                                             'gelişti.',
                          'teaching_point': 'Bu tabloda standart oksimetri yanıltıcı biçimde normal görünebilir; '
                                            'satürasyona güvenilmez.'},
                         {'text': 'Bayılma nedeniyle önce kafa travmasını dışlamak için beyin tomografisi çekmek ve '
                                  'oksijeni tomografi sonrasına bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Tomografi normal geldi; oksijen tedavisi bir saat gecikti.',
                          'teaching_point': 'Travma öyküsü olmayan çocukta görüntüleme oksijen tedavisini '
                                            'geciktirmemelidir.'},
                         {'text': 'Bayılmayı vazovagal senkop kabul edip çocuğu sırtüstü yatırmak, sıvı vermek ve '
                                  'ailenin geri kalanını değerlendirmeden taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Aile aynı eve döndü; gece kardeşi bilinç kaybıyla getirildi.',
                          'teaching_point': 'Aynı ortamdaki birden fazla kişide benzer yakınma ortak bir çevresel '
                                            'nedeni düşündürür.'}]},
            {'stage_title': 'Laboratuvar ve Kardiyak Değerlendirme',
             'question': 'Oksijen başlanan bu çocukta hangi tetkikler istenmelidir?',
             'options': [{'text': 'Baş ağrısı ve kusma nedeniyle lomber ponksiyon yapmak ve beyin omurilik sıvısında '
                                  'hücre ve protein bakmak',
                          'is_correct': False,
                          'scenario_update': 'Lomber ponksiyon normal geldi; asıl tanıyı koyduracak kan gazı '
                                             'istenmedi.',
                          'teaching_point': 'Ateşsiz ve ortak maruziyet öyküsü olan çocukta önce toksik neden '
                                            'araştırılmalıdır.'},
                         {'text': 'Kan gazında kooksimetriyle hemoglobin türlerini ölçmek; laktat, elektrolit, '
                                  'troponin ve 12 derivasyonlu EKG istemek',
                          'is_correct': True,
                          'explanation': 'Kooksimetri tanıyı koyar; venöz örnek yeterlidir. Laktat ve asidoz doku '
                                         'hipoksisini, troponin ve EKG miyokard hasarını gösterir. Kapalı yangın '
                                         'ortamında siyanür zehirlenmesi de düşünülmelidir.',
                          'new_finding': 'Venöz kan gazı kooksimetri: COHb %28.4, pH 7.32, HCO3 19 mEq/L, laktat 3.4 '
                                         'mmol/L. Troponin I 0.02 ng/mL (normal), kreatin kinaz normal. EKG sinüs '
                                         'taşikardisi, iskemik değişiklik yok. Gebelik testi negatif.'},
                         {'text': "Yalnızca parmak ucu nabız oksimetresiyle izlemek, değer %95'in üzerinde kaldıkça ek "
                                  'tetkik istememek',
                          'is_correct': False,
                          'scenario_update': 'Satürasyon sürekli normal göründü; zehirlenmenin derecesi belirlenemedi.',
                          'teaching_point': 'Standart nabız oksimetresi bu tabloda zehirlenmenin derecesini '
                                            'göstermez.'},
                         {'text': 'Arteriyel kan gazında yalnızca parsiyel oksijen basıncına bakmak, değer normalse '
                                  'zehirlenmeyi dışlamak',
                          'is_correct': False,
                          'scenario_update': 'PaO2 normal geldi ve tanı dışlandı; çocuk eve gönderilmek üzereydi.',
                          'teaching_point': 'PaO2 çözünmüş oksijeni gösterir ve bu zehirlenmede normal olabilir; '
                                            'kooksimetri gerekir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Sobalı kapalı odada uyuduktan sonra baş ağrısı, kusma, senkop gelişen, aile bireyleri de '
                         "etkilenen, SpO2'si normal ancak kooksimetride karboksihemoglobini %28.4 olan bu çocukta tanı "
                         'nedir?',
             'options': [{'text': 'Migren atağı (auralı)',
                          'is_correct': False,
                          'scenario_update': 'Ailenin diğer bireyleri de etkilenmiş ve kan gazında belirgin anormallik '
                                             'var.',
                          'teaching_point': 'Migren aile bireylerinde aynı anda başlamaz ve laboratuvar anormalliği '
                                            'yapmaz.'},
                         {'text': 'Karbonmonoksit zehirlenmesi',
                          'is_correct': True,
                          'explanation': 'Kapalı ortamda soba kullanımı, ailede ortak yakınmalar ve karboksihemoglobin '
                                         '%28.4 karbonmonoksit zehirlenmesini doğrular; senkop ağır zehirlenmeyi '
                                         'gösterir.',
                          'new_finding': 'Tanı: Soba Kaynaklı Karbonmonoksit Zehirlenmesi (senkop ile, ağır).'},
                         {'text': 'Siyanür zehirlenmesi',
                          'is_correct': False,
                          'scenario_update': 'Yangın veya duman maruziyeti yok; laktat yalnızca hafif yüksek.',
                          'teaching_point': 'Siyanür zehirlenmesi genellikle kapalı alan yangınlarında, belirgin '
                                            'laktik asidozla görülür.'},
                         {'text': 'Viral gastroenterit',
                          'is_correct': False,
                          'scenario_update': 'İshal ve ateş yok; kooksimetride belirgin anormallik var.',
                          'teaching_point': 'Ailede eş zamanlı kusma, baş ağrısı ve kapalı ortam öyküsü toksik '
                                            'maruziyeti düşündürür.'}]},
            {'stage_title': 'Tedavi ve Yönlendirme',
             'question': 'Bu çocuğun tedavi ve izlem planı hangisidir?',
             'options': [{'text': '%100 oksijeni sürdürüp hiperbarik oksijen merkezine danışmak; tüm aileyi '
                                  'değerlendirip kaynak giderilmeden eve dönülmemesini sağlamak',
                          'is_correct': True,
                          'explanation': 'Senkop ve karboksihemoglobin >%25 hiperbarik oksijen için değerlendirme '
                                         'ölçütleridir; amaç gecikmiş nörolojik sekel riskini azaltmaktır. Aynı '
                                         'ortamdaki herkes kooksimetriyle taranmalıdır. Soba ve baca kontrolü ile ev '
                                         'dedektörü önerilir.',
                          'new_finding': 'Hiperbarik merkezle görüşüldü ve bir seans hiperbarik oksijen uygulandı. '
                                         "Dördüncü saatte karboksihemoglobin %3'e indi, baş ağrısı geçti. Diğer aile "
                                         'bireyleri de tedavi aldı. Bir ay sonra nörolojik kontrol planlandı.'},
                         {'text': 'Belirtiler azaldığı için oksijeni kesip çocuğu ailesiyle birlikte aynı eve '
                                  'göndermek ve sobayı daha az yakmalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Aile aynı ortama döndü; ertesi gece yeniden zehirlenme gelişti.',
                          'teaching_point': 'Kaynak giderilmeden ortama dönüş yinelemeye yol açar; aile '
                                            'bilgilendirilmelidir.'},
                         {'text': "Oksijeni nazal kanülle 2 L/dk'ya düşürmek ve karboksihemoglobin normale inene kadar "
                                  'çocuğu serviste yatırarak izlemek',
                          'is_correct': False,
                          'scenario_update': 'Düşük akımlı oksijenle karboksihemoglobin yavaş geriledi; baş ağrısı '
                                             'uzun sürdü.',
                          'teaching_point': 'Eliminasyonu hızlandırmak için en yüksek oksijen konsantrasyonu '
                                            'kullanılmalıdır.'},
                         {'text': 'Zehirlenmeyi bağlamak için intravenöz hidroksokobalamin ve sodyum tiyosülfat '
                                  'vermek, oksijeni kesmek',
                          'is_correct': False,
                          'scenario_update': 'Bu antidotlar bu tablonun tedavisi değildi; oksijen kesilince belirtiler '
                                             'arttı.',
                          'teaching_point': 'Hidroksokobalamin siyanür zehirlenmesinin antidotudur; bu tablonun '
                                            'tedavisi oksijendir.'}]}]}]
