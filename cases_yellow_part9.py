# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Sarı Alan Vakaları (Part 9: S81 - S90)
"""

YELLOW_CASES_PART9 = [{'id': 'S81',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '15 Yaşında (58 kg)',
  'gender': 'Erkek',
  'complaint': 'Arkadaşlarıyla parkta olduğu sırada başlayan aşırı huzursuzluk, saldırganlık, kusma ve çarpıntı',
  'history': "Arkadaşları 112'yi aramış, olay yerinden ayrılmışlar. Babası hastaneye sonradan geldi: 'Son aylarda "
             "okuldan kaçıyor, notları düştü, para istiyor. Bir şey kullanıyor mu bilmiyorum.' Ambulans ekibi çocuğun "
             "'bir şey içtik' dediğini ama ne olduğunu söylemediğini bildiriyor. Bilinen hastalığı ve ilaç kullanımı "
             'yok. Kafa travması öyküsü yok. Cebinde kuru ot parçacıkları olan küçük bir paket bulunmuş.',
  'final_diagnosis': 'Sentetik Kannabinoid (Bonzai) İntoksikasyonu',
  'disposition': 'Benzodiazepinle Ajitasyon Kontrolü, Monitörizasyon ve Rabdomiyoliz-Böbrek İzlemi Sonrası Gözlem; '
                 'Gizlilik Gözetilerek Ergen Psikiyatrisi ve Bağımlılık Merkezi Yönlendirmesi',
  'case_pearl': "Türkiye'de ergenlerde sık görülen sentetik kannabinoidler doğal esrardan çok daha güçlüdür. "
                'Ajitasyon, psikoz, taşikardi, hipertansiyon, kusma, nöbet, hipertermi, rabdomiyoliz, akut böbrek '
                'hasarı ve aritmiye yol açabilir. Standart idrar ilaç taramasında saptanmazlar; negatif tarama tanıyı '
                'dışlamaz. Ajitasyonda ilk seçenek İV benzodiazepindir; uzun süreli fiziksel kısıtlama hipertermi ve '
                'rabdomiyolizi artırır. Kan şekeri, elektrolitler, CK, kreatinin ve EKG değerlendirilir. Ergenle '
                'ebeveyn olmadan, gizlilik gözetilerek görüşülür; madde kullanımı için bağımlılık merkezine (ÇEMATEM) '
                'yönlendirme yapılır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Ajitasyon Yönetimi',
             'question': 'Ajite, terli ve taşikardik bu ergene ilk yaklaşımınız nedir?',
             'options': [{'text': 'Güvenlik görevlileriyle sedyeye bağlayıp bileklerinden sıkıca sabitlemek ve ilaç '
                                  'vermeden sakinleşene kadar saatlerce fiziksel olarak kısıtlı tutmak',
                          'is_correct': False,
                          'scenario_update': "Kısıtlamaya karşı direnen çocukta vücut ısısı 40.1°C'ye yükseldi, CK "
                                             "18.000 U/L'ye çıktı.",
                          'teaching_point': 'Uzun süreli fiziksel kısıtlama hipertermi ve rabdomiyolizi artırır; '
                                            'kimyasal sedasyon tercih edilir.'},
                         {'text': 'Sakin bir ortamda monitörize etmek, kan şekeri ve ısıyı ölçmek; ajitasyon için İV '
                                  'midazolam veya diazepam vermek',
                          'is_correct': True,
                          'explanation': 'Sempatomimetik bulgular ve ajitasyonda benzodiazepin hem sakinleştirir hem '
                                         'taşikardi, hipertansiyon ve nöbet riskini azaltır. Hipoglisemi ve hipertermi '
                                         'hemen dışlanmalıdır.',
                          'new_finding': 'Midazolam öncesi: KTA 142/dk, KB 154/94 mmHg, SS 24/dk, SpO2 %98, ateş '
                                         '38.1°C, kan şekeri 128 mg/dL. Pupiller normal boyutta, konjonktivalar '
                                         "hiperemik. Cilt terli. Paranoid düşünceler, 'beni öldürecekler' diyor. "
                                         'Midazolam 5 mg İV sonrası sakinleşti; KTA 112/dk, KB 132/80 mmHg.'},
                         {'text': 'Ajitasyonu psikotik atak kabul edip yüksek doz intramüsküler haloperidol yapmak ve '
                                  'psikiyatri servisine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Haloperidol sonrası QTc uzadı ve çocuk nöbet geçirdi.',
                          'teaching_point': 'Zehirlenme şüphesinde ilk seçenek benzodiazepindir; antipsikotikler nöbet '
                                            "eşiğini düşürüp QT'yi uzatabilir."},
                         {'text': 'Babası gelene ve onam verene kadar tedaviye başlamamak, çocuğu bekleme salonunda '
                                  'gözetim altında oturtmak',
                          'is_correct': False,
                          'scenario_update': 'Bekleme salonunda çocuk jeneralize nöbet geçirdi.',
                          'teaching_point': 'Acil durumlarda tedavi onam beklenmeden yapılır.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Sakinleşen bu ergende hangi tetkikler en uygundur?',
             'options': [{'text': 'Yalnızca idrar ilaç taraması istemek; negatif gelirse zehirlenmeyi dışlayıp çocuğu '
                                  'psikiyatriye göndermek',
                          'is_correct': False,
                          'scenario_update': 'İdrar taraması negatif geldi; ölçülmeyen CK ve kreatinin sonradan yüksek '
                                             'bulundu.',
                          'teaching_point': 'Bazı yeni maddeler standart idrar taramasında görülmez; negatif sonuç '
                                            'zehirlenmeyi dışlamaz.'},
                         {'text': 'Acil beyin tomografisi ve lomber ponksiyonla ensefaliti dışlamak, sonra '
                                  'toksikolojik değerlendirmeye geçmek',
                          'is_correct': False,
                          'scenario_update': 'Tetkikler normal geldi; asıl organ hasarı belirteçleri geç '
                                             'değerlendirildi.',
                          'teaching_point': 'Açık bir zehirlenme öyküsü olan, odak bulgusuz ergende önce toksikolojik '
                                            'değerlendirme yapılır.'},
                         {'text': 'EKG, elektrolitler, CK, kreatinin, karaciğer testleri ve kan gazı göndermek; '
                                  'parasetamol ve etanol düzeyi istemek',
                          'is_correct': True,
                          'explanation': 'Bu tablo aritmi, rabdomiyoliz ve böbrek hasarına yol açabilir. Kasıtlı '
                                         'alımda eşlik eden parasetamol ve alkol rutin olarak araştırılır.',
                          'new_finding': 'EKG: sinüs taşikardisi, QTc 440 ms. K 3.3 mmol/L, CK 2.400 U/L, kreatinin '
                                         '1.1 mg/dL, kan gazı normal. Parasetamol ve etanol saptanmadı. İdrar ilaç '
                                         'taraması (esrar dahil) negatif.'},
                         {'text': 'Tetkik istemeden çocuğu iki saat izlemek, sakinse babasına teslim edip yalnızca '
                                  'okul rehberlik servisine yönlendirmekle yetinmek',
                          'is_correct': False,
                          'scenario_update': 'Evde yeniden ajitasyon ve kas ağrısı başladı; koyu renkli idrar fark '
                                             'edildi.',
                          'teaching_point': 'Organ hasarı belirteçleri değerlendirilmeden ve gözlem süresi '
                                            'tamamlanmadan taburculuk yapılmaz.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bu ergendeki tablonun en olası nedeni nedir?',
             'options': [{'text': 'Sentetik kannabinoid intoksikasyonu',
                          'is_correct': True,
                          'explanation': 'Kuru ot içeren paket, sempatomimetik bulgular, paranoid psikoz, kusma, '
                                         'konjonktival hiperemi ve CK yüksekliğine rağmen standart taramanın negatif '
                                         'olması sentetik kannabinoid intoksikasyonunu gösterir.',
                          'new_finding': 'Tanı: Sentetik kannabinoid (bonzai) intoksikasyonu.'},
                         {'text': 'Antikolinerjik zehirlenme',
                          'is_correct': False,
                          'scenario_update': 'Cilt terliydi ve pupiller geniş değildi.',
                          'teaching_point': 'Antikolinerjik tabloda cilt kuru ve kızarık, pupiller geniş, bağırsak '
                                            'sesleri azalmıştır.'},
                         {'text': 'Akut psikotik bozukluk',
                          'is_correct': False,
                          'scenario_update': 'Belirgin otonom bulgular, ateş ve CK yüksekliği vardı.',
                          'teaching_point': 'Primer psikozda otonom instabilite ve kas hasarı beklenmez; önce organik '
                                            'neden dışlanır.'},
                         {'text': 'Serotonin sendromu',
                          'is_correct': False,
                          'scenario_update': 'Serotonerjik ilaç kullanımı, klonus ve hiperrefleksi yoktu.',
                          'teaching_point': 'Serotonin sendromunda serotonerjik ilaç öyküsü, klonus ve hiperrefleksi '
                                            'tipiktir.'}]},
            {'stage_title': 'Gözlem ve Yönlendirme',
             'question': 'Bu ergen için en uygun plan hangisidir?',
             'options': [{'text': 'Sakinleştiği için hemen taburcu etmek ve babaya polis bildirimi yapmasını ve çocuğu '
                                  'cezalandırmasını önermek',
                          'is_correct': False,
                          'scenario_update': 'Erken taburcu edilen çocuk bağımlılık desteği almadan madde kullanmaya '
                                             'devam etti.',
                          'teaching_point': 'Bu yaş grubunda madde kullanımı bir sağlık sorunudur; tedavi ve destek '
                                            'odaklı yaklaşım gerekir.'},
                         {'text': 'Uzun süreli bağımlılık tedavisi için oral naltrekson reçetesi yazıp aile hekimine '
                                  'yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Naltrekson bu madde için etkili değildi; uzman yönlendirmesi yapılmadı.',
                          'teaching_point': 'Bu madde grubunda özgül ilaç tedavisi yoktur; ergen bağımlılık merkezine '
                                            'yönlendirme yapılır.'},
                         {'text': 'Sıvı tedavisiyle CK ve kreatinini izleyerek gözlemlemek; ergenle yalnız görüşüp '
                                  'ÇEMATEM ve psikiyatri yönlendirmesi yapmak',
                          'is_correct': True,
                          'explanation': 'Sıvı tedavisi kas hasarının böbreğe etkisini önler. Gizlilik gözetilen '
                                         'görüşme ergenin açık konuşmasını sağlar ve tedaviye yönlendirme başarısını '
                                         'artırır.',
                          'new_finding': "İV sıvıyla 12. saatte CK 1.100 U/L'ye düştü, kreatinin normale döndü. Ergen "
                                         'yalnız görüşmede iki aydır kullandığını anlattı. Psikiyatri konsültasyonu '
                                         'yapıldı ve ÇEMATEM randevusu verildi.'},
                         {'text': 'Profilaktik olarak levetirasetam başlamak ve nöbet olmasa da bir ay antiepileptik '
                                  'kullanması gerektiğini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz antiepileptik başlandı; çocukta irritabilite arttı.',
                          'teaching_point': 'Zehirlenmeye bağlı akut nöbetlerde uzun süreli antiepileptik '
                                            'gerekmez.'}]}]},
 {'id': 'S82',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '13 Yaşında (45 kg)',
  'gender': 'Erkek',
  'complaint': 'Dört gündür yüksek ateş, şiddetli kas ağrısı, baş ağrısı ve bugün dişeti kanaması',
  'history': "Tokat'ın bir köyünde yaşıyor, haziran ayı. Babası anlatıyor: 'Bir hafta önce hayvanları otlatırken "
             'bacağına kene yapışmış, elimizle çekip çıkardık. Dört gündür ateşi 39-40, her yeri ağrıyor, kustu, karnı '
             "ağrıyor. Bugün dişlerini fırçalarken dişetinden kan geldi, kolunda morluklar çıktı.' Köyde son bir ayda "
             'iki kişi benzer şikâyetle hastaneye yatmış. Bilinen hastalığı yok.',
  'final_diagnosis': 'Kırım-Kongo Kanamalı Ateşi (KKKA)',
  'disposition': 'İzolasyon Önlemleriyle Çocuk Enfeksiyon Servisine Yatış, Destek Tedavisi, Kan Ürünü Desteği ve '
                 'Bildirim',
  'case_pearl': "Türkiye'de özellikle Tokat, Sivas, Çorum, Yozgat ve Kastamonu'da ilkbahar ve yaz aylarında görülür. "
                'Kene tutunması veya hasta kanı ile temastan sonra 1-9 gün içinde ani ateş, miyalji, baş ağrısı ve '
                'gastrointestinal yakınmalar başlar; ardından kanama dönemi gelir. Trombositopeni, lökopeni, AST, ALT, '
                'LDH ve CK yüksekliği ve uzamış PT/aPTT tipiktir. Tanı Halk Sağlığı referans laboratuvarında PCR veya '
                'IgM ile konur, olgu bildirilir. Tedavi destekleyicidir: sıvı, kanama varsa trombosit ve taze donmuş '
                'plazma. Sağlık çalışanları kan ve vücut sıvılarına karşı temas ve damlacık önlemi almalıdır. Keneler '
                'çıplak elle değil, pensle deriye yakın tutularak çıkarılmalıdır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Enfeksiyon Kontrolü',
             'question': 'Ateşli, kanaması olan ve kene tutunma öyküsü olan bu çocukta ilk yaklaşımınız nedir?',
             'options': [{'text': 'Tek kişilik odaya almak, eldiven, önlük, maske ve göz koruyucu kullanmak; vital '
                                  'bulgular, perfüzyon ve kanama odaklarını değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Bu tablo kan ve vücut sıvılarıyla insandan insana bulaşabilen bir '
                                         'enfeksiyonu düşündürür. Personel korunurken şok ve kanama bulguları hemen '
                                         'değerlendirilir.',
                          'new_finding': 'Ateş 39.4°C, KTA 124/dk, KB 98/58 mmHg, SS 22/dk, SpO2 %98, KDZ 2 sn. Yüzde '
                                         've göğüste kızarıklık, konjonktivalarda hiperemi. Dişeti kenarında sızıntı '
                                         'tarzında kanama, kollarda ve enjeksiyon yerlerinde ekimozlar, gövdede '
                                         'peteşiler. Karında yaygın hassasiyet, hafif hepatomegali. Bilinç açık, ense '
                                         'sertliği yok.'},
                         {'text': 'Ateş düşürücü olarak hemen intramüsküler diklofenak yapmak ve kas ağrısı için '
                                  'ibuprofen başlamak',
                          'is_correct': False,
                          'scenario_update': 'Kas içi enjeksiyon yerinde büyük hematom gelişti ve dişeti kanaması '
                                             'arttı.',
                          'teaching_point': 'Kanama eğilimi olan hastada kas içi enjeksiyon ve trombosit işlevini '
                                            'bozan ilaçlar verilmez.'},
                         {'text': 'Standart önlemlerle bekleme salonunda değerlendirmek ve kene öyküsünü önemsiz bulup '
                                  'viral enfeksiyon kabul etmek',
                          'is_correct': False,
                          'scenario_update': 'Hastanın kanı bulaşan bir hemşire temaslı kabul edildi ve profilaktik '
                                             'izleme alındı.',
                          'teaching_point': 'Endemik bölgede kene öyküsü, ateş ve kanama birlikteliği yüksek '
                                            'bulaşıcılık riski taşır.'},
                         {'text': 'Ağır kanama riskine karşı hemen santral venöz kateter takmak ve arteriyel kan gazı '
                                  'için femoral ponksiyon yapmak',
                          'is_correct': False,
                          'scenario_update': 'Femoral ponksiyon yerinden durdurulamayan kanama oldu.',
                          'teaching_point': 'Kanama eğiliminde gereksiz invaziv girişimlerden kaçınılır; periferik '
                                            'damar yolu yeterlidir.'}]},
            {'stage_title': 'Laboratuvar Değerlendirmesi',
             'question': 'Hangi laboratuvar bulgu kümesi bu tabloyu en iyi destekler?',
             'options': [{'text': 'Lökositoz ve nötrofili, yüksek CRP, normal trombosit sayısı ve normal karaciğer '
                                  'enzimleri ile normal pıhtılaşma testleri',
                          'is_correct': False,
                          'scenario_update': 'Hastanın sonuçları bu tabloyla uyumlu değildi.',
                          'teaching_point': 'Bu bulgular bakteriyel enfeksiyonu düşündürür; bu hastalıkta lökopeni ve '
                                            'trombositopeni beklenir.'},
                         {'text': 'Trombositopeni, lökopeni, yüksek AST, ALT, LDH ve CK, uzamış PT ve aPTT ile '
                                  'birlikte düşük fibrinojen',
                          'is_correct': True,
                          'explanation': 'Virüs endotel ve karaciğeri tutarak pıhtılaşma bozukluğu ve trombositopeni '
                                         'yapar. Kas enzimleri ve LDH yüksekliği yaygın doku tutulumunu gösterir.',
                          'new_finding': 'Lökosit 1.900/mm³, Hb 13.2 g/dL, trombosit 32.000/mm³. AST 486 U/L, ALT 212 '
                                         'U/L, LDH 1.240 U/L, CK 1.680 U/L. PT 17 sn, INR 1.5, aPTT 52 sn, fibrinojen '
                                         '140 mg/dL. Kreatinin 0.7 mg/dL. Kan örneği PCR için Halk Sağlığı referans '
                                         'laboratuvarına gönderildi.'},
                         {'text': 'İzole trombositopeni ile normal lökosit, karaciğer enzimleri ve pıhtılaşma '
                                  'testleri, periferik yaymada büyük trombositler',
                          'is_correct': False,
                          'scenario_update': 'Hastanın sonuçları bu tabloyla uyumlu değildi.',
                          'teaching_point': 'İzole trombositopeni ve büyük trombositler immün trombositopeniyi '
                                            'düşündürür; ateş ve organ tutulumu beklenmez.'},
                         {'text': 'Anemi, şistositler, trombositopeni ve yüksek kreatinin ile birlikte normal PT ve '
                                  'aPTT, yüksek LDH',
                          'is_correct': False,
                          'scenario_update': 'Hastanın sonuçları bu tabloyla uyumlu değildi.',
                          'teaching_point': 'Bu kümeler mikroanjiyopatik hemolitik anemiyi düşündürür.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik ve laboratuvar bulgularına göre en olası tanınız nedir?',
             'options': [{'text': 'Fulminan meningokoksemi',
                          'is_correct': False,
                          'scenario_update': 'Lökopeni vardı ve tablo kene tutunmasından sonra, endemik bölgede ve '
                                             'mevsimde gelişmişti.',
                          'teaching_point': 'Meningokoksemide hızla yayılan purpura ve şok tablosu, sıklıkla lökositoz '
                                            'görülür.'},
                         {'text': 'Akut lösemi',
                          'is_correct': False,
                          'scenario_update': 'Akut başlangıç, kene öyküsü ve belirgin enzim yüksekliği vardı.',
                          'teaching_point': 'Lösemide haftalar süren solukluk, kemik ağrısı ve periferik yaymada '
                                            'blastlar görülür.'},
                         {'text': 'Kırım-Kongo kanamalı ateşi',
                          'is_correct': True,
                          'explanation': 'Endemik bölgede yaz aylarında kene tutunmasından sonra ani ateş, miyalji, '
                                         'kanama, lökopeni, trombositopeni, transaminaz ve CK yüksekliği ve pıhtılaşma '
                                         'bozukluğu Kırım-Kongo kanamalı ateşini gösterir.',
                          'new_finding': 'Tanı: Kırım-Kongo kanamalı ateşi. PCR pozitif geldi.'},
                         {'text': 'Tularemi (Francisella tularensis)',
                          'is_correct': False,
                          'scenario_update': 'Bölgesel lenfadenopati veya ülserli lezyon yoktu, kanama ön plandaydı.',
                          'teaching_point': 'Tularemide ülseroglandüler veya orofaringeal tutulum ve lenfadenopati '
                                            'tipiktir.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Bakteriyel enfeksiyonu dışlamak için geniş spektrumlu antibiyotik ve yüksek doz '
                                  'kortikosteroid başlayıp genel serviste izlemek',
                          'is_correct': False,
                          'scenario_update': 'Tedavi viral tabloyu etkilemedi; izolasyonsuz serviste bir refakatçi '
                                             'kanla temas etti.',
                          'teaching_point': 'Tedavi destekleyicidir; izolasyon önlemleri her aşamada sürdürülür.'},
                         {'text': 'Trombosit sayısı düşük olduğu için kanama olmasa da her gün profilaktik trombosit '
                                  've plazma vermek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz ürün kullanımı oldu; transfüzyon reaksiyonu gelişti.',
                          'teaching_point': 'Kan ürünleri aktif kanama veya çok düşük değerlerde verilir; rutin '
                                            'profilaksi yapılmaz.'},
                         {'text': 'İzolasyonda sıvı desteği vermek, kanamaya göre trombosit ve taze donmuş plazma '
                                  'kullanmak, günlük tetkiklerle izleyip bildirmek',
                          'is_correct': True,
                          'explanation': 'Destek tedavisi ve kanamanın yakın izlemi sağkalımı belirler. Bildirim ve '
                                         'temaslı izlemi bulaşın kontrolü için gereklidir.',
                          'new_finding': 'Dişeti kanaması nedeniyle trombosit ve taze donmuş plazma verildi. Olgu '
                                         'bildirildi, temaslı aile bireyleri 14 gün ateş açısından izlendi. Yedinci '
                                         "günde trombosit 110.000/mm³'e yükseldi ve çocuk sekelsiz iyileşti."},
                         {'text': 'Ateş ve kanama yatışana dek evde yatak istirahati önermek, ağrı için aspirin vermek '
                                  've günlük kan sayımı yaptırmak',
                          'is_correct': False,
                          'scenario_update': 'Aspirin kanamayı artırdı; çocuk evde masif gastrointestinal kanamayla '
                                             'getirildi.',
                          'teaching_point': 'Bu hastalar yatırılarak izlenir; aspirin ve NSAİİ kontrendikedir.'}]}]},
 {'id': 'S83',
  'category': '🦴 Kas-İskelet & Eklem / Ortopedik Aciller',
  'age': '9 Yaşında (28 kg)',
  'gender': 'Kız',
  'complaint': 'Üç haftadır gelip giden ateş, gece terlemesi ve bir haftadır sağ kalçada ağrı ve topallama',
  'history': "Van'da yaşıyor. Annesi anlatıyor: 'Üç haftadır akşamları ateşleniyor, gece yatağı sırılsıklam oluyor, "
             'sabah ateşi düşüyor, yine okula gidiyor. İştahı yok, iki kilo verdi. Bir haftadır sağ kalçası ağrıyor, '
             "topallıyor.' Evde inek ve koyun besleniyor. Aile taze, ev yapımı otlu peynir yiyor, süt kaynatılmadan "
             'içiliyor. Babasında da birkaç aydır eklem ağrısı ve halsizlik var. Öksürük, ishal, döküntü yok. Daha '
             'önce verilen bir haftalık amoksisilin işe yaramamış.',
  'final_diagnosis': 'Bruselloz (Sağ Sakroiliit ile Osteoartiküler Tutulum)',
  'disposition': 'Doksisiklin ve Rifampisin (6 Hafta) Başlanarak Çocuk Enfeksiyon Servisine Yatış, Bildirim ve Aile '
                 'Taraması',
  'case_pearl': "Türkiye'de özellikle Doğu ve Güneydoğu Anadolu'da endemiktir. Pastörize edilmemiş süt ve taze peynir "
                'tüketimi en sık bulaş yoludur. Gelip giden ateş, gece terlemesi, kilo kaybı, artralji ve '
                'hepatosplenomegali tipiktir; çocuklarda en sık osteoartiküler tutulum sakroiliit ve büyük eklem '
                'artritidir. Tanıda Rose Bengal tarama testi, standart tüp aglütinasyonu (≥1/160) ve kan kültürü '
                '(laboratuvar uyarılmalı) kullanılır. Sekiz yaş ve üzerinde doksisiklin + rifampisin, sekiz yaş '
                'altında trimetoprim-sulfametoksazol + rifampisin 6 hafta verilir. Tek ilaç ve kısa tedavi nüks '
                'riskini artırır. Olgu bildirilir ve aynı ürünleri tüketen aile bireyleri taranır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Üç haftadır ateşi olan ve topallayan bu çocukta değerlendirmede neye odaklanırsınız?',
             'options': [{'text': 'Topallama nedeniyle yalnızca kalça grafisi çekip kalça hastalığı olmadığında ateşi '
                                  'viral kabul etmek',
                          'is_correct': False,
                          'scenario_update': 'Grafi normal geldi; sistemik bulgular değerlendirilmeden çocuk '
                                             'gönderildi.',
                          'teaching_point': 'Uzun süreli ateş sistemik bir hastalığın işaretidir; ayrıntılı öykü ve '
                                            'muayene gerekir.'},
                         {'text': 'Beslenme ve hayvan teması öyküsünü derinleştirmek, lenf bezleri, karaciğer, dalak '
                                  've eklemleri sistemli muayene etmek',
                          'is_correct': True,
                          'explanation': 'Uzamış ateşte maruziyet öyküsü ve organomegali, lenfadenopati, eklem '
                                         'bulguları ayırıcı tanıyı daraltır. Pastörize edilmemiş ürün tüketimi önemli '
                                         'bir ipucudur.',
                          'new_finding': 'Ateş 38.6°C, KTA 112/dk, KB 102/62 mmHg. Soluk görünümlü. Karaciğer kosta '
                                         "altında 3 cm, dalak 2 cm ele geliyor. Servikal bölgede 1 cm'lik birkaç "
                                         'ağrısız lenf nodu. Sağ sakroiliak eklem üzerinde basmakla hassasiyet, FABER '
                                         'testi sağda ağrılı. Kalça hareketleri tam, diz ve ayak bileği normal. '
                                         'Döküntü yok.'},
                         {'text': 'Daha önce verilen antibiyotiğin yetersiz kaldığını düşünüp tetkik yapmadan '
                                  'amoksisilin-klavulanat başlamak',
                          'is_correct': False,
                          'scenario_update': 'Ateş sürdü ve tanı haftalarca gecikti.',
                          'teaching_point': 'Uzamış ateşte nedeni bulmadan yapılan ampirik tedavi tanıyı geciktirir.'},
                         {'text': 'Ateş, kilo kaybı ve gece terlemesi nedeniyle hemen kemik iliği aspirasyonu '
                                  'planlamak ve onkolojiye sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'Daha basit tetkiklerle tanı konabilecekken çocuk invaziv bir girişime '
                                             'maruz kaldı.',
                          'teaching_point': 'Malignite akılda tutulur ama önce öykü, muayene ve temel tetkiklerle '
                                            'değerlendirme yapılır.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Bu çocukta hangi tetkik grubu tanıya en hızlı ulaştırır?',
             'options': [{'text': 'Tam kan sayımı, periferik yayma, karaciğer testleri, Rose Bengal ve tüp '
                                  'aglütinasyon testi; laboratuvarı uyararak kan kültürü göndermek',
                          'is_correct': True,
                          'explanation': 'Serolojik testler endemik bölgede hızlı tanı sağlar. Kan kültürü uzun '
                                         'inkübasyon gerektirir ve laboratuvar çalışanları için enfeksiyon riski '
                                         'taşıdığı için önceden bildirilmelidir.',
                          'new_finding': 'Lökosit 4.100/mm³ (lenfosit baskın), Hb 10.4 g/dL, trombosit 168.000/mm³, '
                                         'yaymada blast yok. AST 88 U/L, ALT 74 U/L, CRP 38 mg/L. Rose Bengal pozitif, '
                                         "standart tüp aglütinasyonu 1/640. Sakroiliak MR'da sağda kemik iliği ödemi "
                                         've eklem sıvısı.'},
                         {'text': 'Kalça eklemine aspirasyon yapıp eklem sıvısını kültüre göndermek ve sonuca göre '
                                  'tedaviye karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Kalça ekleminde sıvı yoktu; girişim gereksiz yere yapıldı.',
                          'teaching_point': 'Ağrı sakroiliak kaynaklıydı; kalça hareketleri normaldi.'},
                         {'text': 'Tüberküloz için tüberkülin deri testi, açlık mide suyu ve toraks tomografisini '
                                  'sıralı olarak planlamak',
                          'is_correct': False,
                          'scenario_update': 'Tetkikler negatif geldi ve tanı gecikti.',
                          'teaching_point': 'Maruziyet öyküsü olan endemik bölgede daha olası tanılar öncelikle '
                                            'araştırılır.'},
                         {'text': 'Romatolojik hastalık için ANA, RF ve HLA-B27 istemek ve sonuçlar gelince ateş için '
                                  'yeniden değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Sonuçlar negatif geldi; enfeksiyon tedavisi gecikti.',
                          'teaching_point': 'Ateş ve organomegali ile gelen artritte önce enfeksiyonlar '
                                            'dışlanmalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Septik artrit (kalça)',
                          'is_correct': False,
                          'scenario_update': 'Kalça hareketleri tamdı ve tutulum sakroiliak eklemdeydi; tablo '
                                             'haftalardır sürüyordu.',
                          'teaching_point': 'Septik artritte akut başlangıç, eklem hareketinde belirgin kısıtlılık ve '
                                            'yüksek akut faz görülür.'},
                         {'text': 'Juvenil idiyopatik artrit (sistemik)',
                          'is_correct': False,
                          'scenario_update': 'Somon renkli döküntü yoktu ve seroloji yüksek titrede pozitifti.',
                          'teaching_point': "Sistemik JİA'da günde bir-iki kez yükselen ateş ve somon renkli döküntü "
                                            'tipiktir; enfeksiyonlar dışlandıktan sonra düşünülür.'},
                         {'text': 'Bruselloz (sakroiliit ile)',
                          'is_correct': True,
                          'explanation': 'Endemik bölgede pastörize edilmemiş ürün tüketimi, gelip giden ateş, gece '
                                         'terlemesi, hepatosplenomegali, sakroiliit, Rose Bengal pozitifliği ve 1/640 '
                                         'aglütinasyon titresi brusellozu gösterir.',
                          'new_finding': 'Tanı: Bruselloz, sağ sakroiliit.'},
                         {'text': 'Akut lösemi',
                          'is_correct': False,
                          'scenario_update': 'Periferik yaymada blast yoktu ve trombosit sayısı normaldi.',
                          'teaching_point': 'Kemik ağrısı ve organomegali lösemide de görülür; yayma ve kan sayımı '
                                            'ayrımda önemlidir.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Tek başına oral trimetoprim-sulfametoksazolü iki hafta vermek, ateş ve ağrı geçince '
                                  'kontrol tetkiki yapmadan tedaviyi kesmek',
                          'is_correct': False,
                          'scenario_update': 'İki ay sonra ateş ve kalça ağrısı yeniden başladı.',
                          'teaching_point': 'Tek ilaç ve kısa süreli tedavi nüks oranını belirgin artırır.'},
                         {'text': 'Doksisiklin ve rifampisini 6 hafta vermek; olguyu bildirmek, süt ve peyniri '
                                  'kaynatmayı anlatıp aileyi taramak',
                          'is_correct': True,
                          'explanation': 'Sekiz yaş üstünde doksisiklin ve rifampisin kombinasyonu standart tedavidir; '
                                         'osteoartiküler tutulumda süre uzatılabilir. Aynı ürünü tüketen aile '
                                         'bireylerinde de enfeksiyon sıktır.',
                          'new_finding': 'Tedavi başlandı, olgu bildirildi. Babada da tüp aglütinasyonu 1/320 pozitif '
                                         'çıktı ve tedavi başlandı. Çocuğun ateşi bir haftada düştü, kalça ağrısı '
                                         'dördüncü haftada geçti.'},
                         {'text': 'İntravenöz vankomisin ve seftriakson başlayıp sakroiliak ekleme cerrahi debridman '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'Seçilen antibiyotikler hücre içi bakteriye yeterli etki göstermedi; '
                                             'gereksiz cerrahi planlandı.',
                          'teaching_point': 'Bu hücre içi etkene karşı hücre içine iyi geçen ilaç kombinasyonları '
                                            'kullanılır; cerrahi nadiren gerekir.'},
                         {'text': 'Eklem ağrısı için naproksen ve yüksek doz prednizolon başlayıp romatoloji '
                                  'polikliniğine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Kortikosteroid enfeksiyonu baskıladı ve tanıyı karmaşıklaştırdı; ateş '
                                             'sürdü.',
                          'teaching_point': 'Enfeksiyöz artritte kortikosteroid kullanılmaz; etkene yönelik tedavi '
                                            'gerekir.'}]}]},
 {'id': 'S84',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '13 Yaşında (44 kg)',
  'gender': 'Kız',
  'complaint': 'Beden eğitimi dersinde koşarken aniden yere yığılma ve kısa süren kasılma',
  'history': "Öğretmeni getirdi. 'Koşu sırasında hiçbir uyarı vermeden yere düştü, kolları bacakları birkaç saniye "
             "kasıldı, morardı. Yaklaşık bir dakikada kendine geldi, bizi tanıdı.' Annesi telefonda: 'Geçen yıl "
             'yüzerken de bir kez bayılmıştı, havuz görevlisi çıkarmıştı. Ben de gençken birkaç kez bayıldım, bana '
             "epilepsi dediler, ilaç kullanıyorum. Dayısı 24 yaşında denizde boğularak öldü.' Son günlerde hastalık, "
             'ishal, kusma yok. İlaç kullanmıyor. Enerji içeceği tüketmemiş.',
  'final_diagnosis': 'Konjenital Uzun QT Sendromu (Olası Tip 1, Eforla Tetiklenen Senkop)',
  'disposition': 'Sürekli Monitörizasyon, Beta-Bloker Başlanması, QT Uzatan İlaçlardan Kaçınma ve Aile Taramasıyla '
                 'Çocuk Kardiyoloji Servisine Yatış',
  'case_pearl': 'Egzersiz, yüzme, ani ses veya korkuyla tetiklenen, öncesinde uyarı bulgusu olmayan senkop kardiyak '
                'kaynaklı kabul edilmelidir. Kısa süreli kasılmalar beyin perfüzyonunun azalmasıyla ortaya çıkar ve '
                "epilepsi ile karışabilir. Ailede genç yaşta açıklanamayan ölüm, boğulma veya 'epilepsi' tanısı "
                'uyarıcıdır. Her senkopta 12 derivasyonlu EKG çekilmeli, QTc elle (Bazett) hesaplanmalıdır; ergen '
                'kızda 460 ms üzeri uzundur. Hipokalemi, hipomagnezemi ve hipokalsemi düzeltilir. Tedavide beta-bloker '
                '(propranolol veya nadolol) verilir, QT uzatan ilaçlardan (makrolidler, ondansetron, bazı '
                'antihistaminikler, antipsikotikler) kaçınılır. Birinci derece akrabalara EKG taraması yapılır.',
  'steps': [{'stage_title': 'İlk Değerlendirme',
             'question': 'Efor sırasında yere yığılan ve kendine gelmiş bu çocukta ilk değerlendirmeniz nedir?',
             'options': [{'text': 'Kasılma olduğu için epileptik nöbet kabul edip annesinin kullandığı ilacın aynısını '
                                  'başlamak üzere nöroloji randevusu vermek',
                          'is_correct': False,
                          'scenario_update': 'Kardiyak değerlendirme yapılmadan gönderilen çocuk bir ay sonra koşarken '
                                             'yeniden yığıldı.',
                          'teaching_point': 'Efor sırasında prodromsuz yığılma ve kısa kasılma kardiyak senkopu '
                                            'düşündürür.'},
                         {'text': 'Monitöre bağlayıp 12 derivasyonlu EKG çekmek, kan şekeri, elektrolitler, kalsiyum '
                                  've magnezyumu göndermek',
                          'is_correct': True,
                          'explanation': "Eforla ortaya çıkan senkopta ilk ve en değerli tetkik EKG'dir. Elektrolit "
                                         'bozuklukları ritim bozukluğunu tetikleyebileceği için birlikte '
                                         'değerlendirilir.',
                          'new_finding': 'KTA 68/dk, KB 108/66 mmHg, SpO2 %99, bilinç tam, nörolojik muayene normal. '
                                         'Kalp sesleri normal, üfürüm yok. Kan şekeri 98 mg/dL, K 4.1 mmol/L, Mg 2.0 '
                                         'mg/dL, iyonize Ca normal. EKG: sinüs ritmi, geniş tabanlı T dalgaları, elle '
                                         'hesaplanan QTc 520 ms.',
                          'image': 'assets/images/ecg_long_qtc.png'},
                         {'text': 'Vazovagal bayılma kabul edip tuzlu yiyecek ve bol sıvı önermek, yüzme ve koşuya '
                                  'devam etmesini söyleyerek taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk iki hafta sonra yüzme sırasında yeniden bilincini kaybetti.',
                          'teaching_point': 'Vazovagal senkop eforla değil, uzun süre ayakta kalma veya ağrı ile, '
                                            'prodromla ortaya çıkar.'},
                         {'text': 'Acil beyin tomografisi ve EEG istemek, kardiyolojik değerlendirmeyi nöroloji '
                                  'sonuçlarından sonraya bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Tomografi ve EEG normal geldi; asıl neden gecikmeyle saptandı.',
                          'teaching_point': 'Eforla ortaya çıkan olaylarda önce kardiyak nedenler dışlanır.'}]},
            {'stage_title': 'Acil Önlemler',
             'question': "EKG'de QTc 520 ms bulunan bu çocukta acilde hangi yaklaşım uygundur?",
             'options': [{'text': 'Bulantısı için ondansetron, olası enfeksiyon için klaritromisin vermek ve sonuçları '
                                  'izlemek',
                          'is_correct': False,
                          'scenario_update': 'İlaçlar sonrası monitörde polimorfik ventriküler taşikardi atakları '
                                             'görüldü.',
                          'teaching_point': "Ondansetron ve makrolidler QT'yi uzatır; bu hastalarda kaçınılmalıdır."},
                         {'text': 'Sürekli ritim monitörü ve defibrilatörü hazır tutmak, QT uzatan ilaçlardan kaçınmak '
                                  've çocuk kardiyolojiye danışmak',
                          'is_correct': True,
                          'explanation': 'Bu hastalarda torsades de pointes ani ölüme yol açabilir. Monitör ve '
                                         'defibrilatör hazır olmalı, ritmi bozabilecek ilaçlar verilmemelidir.',
                          'new_finding': 'Monitörde ventriküler ektopi görülmedi. Çocuk kardiyoloji konsültasyonunda '
                                         'yatış ve beta-bloker kararı alındı. Ekokardiyografi normal.'},
                         {'text': 'Profilaktik amiodaron infüzyonu başlamak ve hemen elektrofizyolojik çalışma için '
                                  'başka merkeze sevk etmek',
                          'is_correct': False,
                          'scenario_update': "Amiodaron QT'yi daha da uzattı ve hipotansiyon yaptı.",
                          'teaching_point': "Amiodaron QT'yi uzatır; bu tabloda kullanılmaz."},
                         {'text': 'Elektrolitler normal olduğu halde yüksek doz İV magnezyum ve potasyum yükleyerek QT '
                                  'aralığını kısaltmaya çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Normal düzeylere ek yükleme hiperkalemiye yol açtı.',
                          'teaching_point': 'Elektrolitler düşükse düzeltilir; magnezyum torsades atağında verilir, '
                                            'profilaktik yükleme gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bu çocuktaki olayların en olası nedeni nedir?',
             'options': [{'text': 'Hipertrofik kardiyomiyopati',
                          'is_correct': False,
                          'scenario_update': 'Üfürüm yoktu ve ekokardiyografi normaldi.',
                          'teaching_point': "Hipertrofik kardiyomiyopatide sol ventrikül hipertrofisi ve EKG'de yüksek "
                                            'voltajlar görülür.'},
                         {'text': 'Konjenital uzun QT sendromu',
                          'is_correct': True,
                          'explanation': "Egzersiz ve yüzme sırasında prodromsuz senkop, annede 'epilepsi' tanılı "
                                         'bayılmalar, dayıda genç yaşta boğulma, normal elektrolitlerle QTc 520 ms ve '
                                         'geniş tabanlı T dalgaları konjenital uzun QT sendromunu gösterir.',
                          'new_finding': "Tanı: Konjenital uzun QT sendromu (olası tip 1). Annenin EKG'sinde de QTc "
                                         '490 ms bulundu.'},
                         {'text': 'Jeneralize epilepsi',
                          'is_correct': False,
                          'scenario_update': 'Olaylar eforla tetiklenmişti, kasılma kısa ve bilinç hızla düzelmişti.',
                          'teaching_point': 'Epileptik nöbette postiktal dönem uzundur ve olaylar eforla ilişkili '
                                            'değildir.'},
                         {'text': 'Wolff-Parkinson-White sendromu',
                          'is_correct': False,
                          'scenario_update': "EKG'de kısa PR ve delta dalgası yoktu.",
                          'teaching_point': "WPW'de kısa PR aralığı ve delta dalgası görülür."}]},
            {'stage_title': 'Tedavi ve Yatış Planı',
             'question': 'Bu çocuk ve ailesi için en uygun plan hangisidir?',
             'options': [{'text': 'Beta-bloker başlayıp yatırmak, QT uzatan ilaç listesi vermek, rekabetçi sporu '
                                  'kısıtlamak ve tüm birinci derece akrabalara EKG çekmek',
                          'is_correct': True,
                          'explanation': 'Beta-bloker eforla tetiklenen aritmi riskini azaltır. Ailenin taranması hem '
                                         'annedeki yanlış tanıyı düzeltir hem de diğer risklileri ortaya çıkarır.',
                          'new_finding': 'Nadolol başlandı, QT uzatan ilaç listesi verildi. Genetik testte KCNQ1 '
                                         'mutasyonu saptandı. Annenin epilepsi ilacı kesilip beta-bloker başlandı, '
                                         "kardeşin EKG'si normal bulundu."},
                         {'text': 'Olay tekrarlamadıkça tedavi gerekmediğini söyleyip yıllık EKG kontrolüyle taburcu '
                                  'etmek ve spora devam ettirmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk bir yarışma sırasında ani kardiyak arrest geçirdi.',
                          'teaching_point': 'Senkop geçirmiş bu hastalar yüksek risklidir ve tedavi gerektirir.'},
                         {'text': 'Tüm hastalarda zorunlu olduğu için hemen implante edilebilir defibrilatör '
                                  'takılmasını planlamak ve beta-bloker vermemek',
                          'is_correct': False,
                          'scenario_update': 'İlk basamak tedavi atlandı ve gereksiz bir cerrahi girişim planlandı.',
                          'teaching_point': 'İlk tedavi beta-blokerdir; defibrilatör tedaviye rağmen olay geçirenlerde '
                                            've çok yüksek riskte düşünülür.'},
                         {'text': 'Annesinin epilepsi ilacını çocuğa da başlamak ve kardiyolojik izlemi annenin '
                                  'nöroloji kontrollerine bağlamak',
                          'is_correct': False,
                          'scenario_update': 'Epilepsi ilacı aritmiyi önlemedi; anne ve çocuk yanlış tedavi almaya '
                                             'devam etti.',
                          'teaching_point': 'Annedeki olayların da kardiyak kaynaklı olabileceği akla gelmeli ve aile '
                                            'taranmalıdır.'}]}]},
 {'id': 'S85',
  'category': '🩸 Hematolojik & Onkolojik Aciller',
  'age': '4 Yaşında (16 kg)',
  'gender': 'Erkek',
  'complaint': 'Üç haftadır solukluk, halsizlik, bacak ağrısı nedeniyle yürümek istememe ve vücutta morluklar',
  'history': "Annesi anlatıyor: 'Üç haftadır çok soluk, hemen yoruluyor. Geceleri bacaklarım ağrıyor diye uyanıyor, "
             'son birkaç gündür yürümek istemiyor, kucak istiyor. Bacaklarında ve sırtında nedensiz morluklar çıktı. '
             "Arada ateşlendi, doktor büyüme ağrısı dedi, ibuprofen verdik.' Burun kanaması iki kez olmuş. İştahı "
             'azalmış. Travma öyküsü yok. Ailede kan hastalığı yok.',
  'final_diagnosis': 'Akut Lenfoblastik Lösemi (Hiperlökositoz ve Tümör Lizis Riski)',
  'disposition': 'Tümör Lizisi Önlemleri (Hiperhidrasyon, Allopürinol), Gerekli Kan Ürünleri ve Tanısal Kemik İliği '
                 'İncelemesi İçin Çocuk Hematoloji-Onkoloji Servisine Yatış',
  'case_pearl': 'Solukluk, yorgunluk, kemik ağrısı (özellikle gece uyandıran), morluk, ateş, hepatosplenomegali ve '
                'lenfadenopati birlikteliği kemik iliği infiltrasyonunu düşündürür; iki veya üç hücre serisinin '
                "birlikte etkilenmesi uyarıcıdır. 'Büyüme ağrısı' gece ağrısı yapar ama sistemik bulgu ve laboratuvar "
                'bozukluğu olmaz. Tanı konmadan kortikosteroid verilmemelidir; hem tanıyı gizler hem tümör lizisini '
                'tetikler. Tümör lizisi için ürik asit, potasyum, fosfor, kalsiyum ve kreatinin ölçülür; potasyumsuz '
                'hiperhidrasyon ve allopürinol (veya yüksek riskte rasburikaz) başlanır. Hiperlökositozda eritrosit '
                'transfüzyonu yavaş ve dikkatli verilir. Sedasyon öncesi akciğer grafisiyle mediasten kitlesi '
                'dışlanır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Solukluk, kemik ağrısı ve morlukları olan bu çocukta muayenede neye odaklanırsınız?',
             'options': [{'text': 'Morlukları istismar bulgusu kabul edip ayrıntılı muayene yapmadan hemen sosyal '
                                  'hizmet ve adli bildirim sürecini başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Aile büyük travma yaşadı; altta yatan ciddi hastalık değerlendirmesi '
                                             'gecikti.',
                          'teaching_point': 'Morluklarda istismar akılda tutulur, ancak önce kanama bozuklukları ve '
                                            'kemik iliği hastalıkları dışlanmalıdır.'},
                         {'text': 'Ağrıyı büyüme ağrısı kabul edip muayene etmeden kas gevşetici ve D vitamini '
                                  'önermek, bir ay sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Bir hafta sonra çocuk yüksek ateş ve yaygın kanama ile getirildi.',
                          'teaching_point': 'Büyüme ağrısında solukluk, morluk, ateş ve yürümeyi reddetme olmaz; bu '
                                            'bulgular ileri değerlendirme gerektirir.'},
                         {'text': 'Vital bulgular ve perfüzyonu değerlendirmek; lenf bezleri, karaciğer, dalak, '
                                  'testisler, deri ve mukozalarda kanama bulgularını incelemek',
                          'is_correct': True,
                          'explanation': 'Sistemik bulgularla gelen kemik ağrısında organomegali, lenfadenopati ve '
                                         'kanama bulguları kemik iliği tutulumunu düşündürür. Testis muayenesi '
                                         'infiltrasyon açısından önemlidir.',
                          'new_finding': 'Ateş 38.2°C, KTA 136/dk, KB 98/60 mmHg, SS 26/dk, SpO2 %98. Belirgin soluk. '
                                         'Bacaklarda ve sırtta farklı evrelerde ekimozlar, gövdede peteşiler. Servikal '
                                         "ve aksiller bölgede 1-2 cm'lik, ağrısız, birbirine yapışık olmayan lenf "
                                         'nodları. Karaciğer 4 cm, dalak 5 cm ele geliyor. Tibialarda basmakla '
                                         'hassasiyet. Testisler normal.'},
                         {'text': 'Kemik ağrısı ve ateş nedeniyle osteomiyelit kabul edip hemen İV sefazolin başlamak '
                                  've ortopediye danışmak',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik tabloyu düzeltmedi; asıl tanı gecikti.',
                          'teaching_point': 'Çok odaklı kemik ağrısı, organomegali ve kanama bulguları sistemik bir '
                                            'hastalığı düşündürür.'}]},
            {'stage_title': 'Laboratuvar Değerlendirmesi',
             'question': 'Tam kan sayımında lökosit 86.000/mm³, Hb 6.1 g/dL, trombosit 14.000/mm³ bulundu. Sonraki '
                         'adım nedir?',
             'options': [{'text': 'Periferik yayma yapmak; ürik asit, potasyum, fosfor, kalsiyum, kreatinin ve LDH ile '
                                  'pıhtılaşma testleri ve akciğer grafisi istemek',
                          'is_correct': True,
                          'explanation': 'Yayma tanıya yönlendirir. Yüksek hücre yükü tümör lizisi riski taşır; '
                                         'metabolik değerler başlangıçta bilinmelidir. Akciğer grafisi mediasten '
                                         'kitlesini dışlar.',
                          'new_finding': "Periferik yaymada lökositlerin %78'i blast (küçük-orta boy, dar "
                                         'sitoplazmalı). Ürik asit 9.8 mg/dL, K 4.9 mmol/L, fosfor 6.4 mg/dL, Ca 8.6 '
                                         'mg/dL, kreatinin 0.6 mg/dL, LDH 2.840 U/L. PT ve aPTT normal. Akciğer '
                                         'grafisinde mediasten genişlemesi yok.'},
                         {'text': 'Lökositozu ağır bakteriyel enfeksiyon kabul edip kan kültürü alıp geniş spektrumlu '
                                  'antibiyotik başlamak ve yaymayı ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Yayma geç yapıldı; tümör lizisi önlemleri saatlerce gecikti.',
                          'teaching_point': 'Üç hücre serisinin birlikte bozulduğu tabloda yayma hemen yapılmalıdır.'},
                         {'text': 'Ağrısı ve ateşi için tanı konmadan yüksek doz İV metilprednizolon başlamak ve '
                                  'tetkikleri ertesi güne bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Kortikosteroid sonrası ürik asit ve potasyum hızla yükseldi; kemik iliği '
                                             'tanısı güçleşti.',
                          'teaching_point': 'Tanı konmadan kortikosteroid verilmez; tümör lizisini tetikler ve tanıyı '
                                            'gizler.'},
                         {'text': 'Hemoglobini hızla yükseltmek için 20 mL/kg eritrosit süspansiyonunu bir saatte '
                                  'vermek ve sonra yaymaya bakmak',
                          'is_correct': False,
                          'scenario_update': 'Hızlı transfüzyon sonrası kan viskozitesi arttı; çocukta baş ağrısı ve '
                                             'solunum sıkıntısı gelişti.',
                          'teaching_point': 'Yüksek lökosit sayısında transfüzyon küçük hacimlerde ve yavaş '
                                            'verilir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'İmmün trombositopenik purpura',
                          'is_correct': False,
                          'scenario_update': 'Anemi, lökositoz, blastlar ve organomegali vardı.',
                          'teaching_point': "İTP'de yalnızca trombositopeni olur; çocuk iyi görünür ve organomegali "
                                            'yoktur.'},
                         {'text': 'Enfeksiyöz mononükleoz',
                          'is_correct': False,
                          'scenario_update': 'Yaymada atipik lenfosit değil blastlar görüldü ve ağır trombositopeni '
                                             'vardı.',
                          'teaching_point': 'Mononükleozda atipik lenfositler, tonsillit ve lenfadenopati görülür; '
                                            'ağır sitopeni beklenmez.'},
                         {'text': 'Aplastik anemi',
                          'is_correct': False,
                          'scenario_update': 'Lökosit sayısı düşük değil çok yüksekti ve organomegali vardı.',
                          'teaching_point': 'Aplastik anemide pansitopeni olur, organomegali ve lenfadenopati '
                                            'beklenmez.'},
                         {'text': 'Akut lenfoblastik lösemi',
                          'is_correct': True,
                          'explanation': 'Solukluk, kemik ağrısı, kanama bulguları, hepatosplenomegali, lenfadenopati, '
                                         'anemi, trombositopeni, hiperlökositoz ve periferik yaymada blastlar akut '
                                         'lenfoblastik lösemiyi gösterir.',
                          'new_finding': 'Tanı: Akut lenfoblastik lösemi (kemik iliği ve akım sitometrisiyle '
                                         'doğrulandı, prekürsör B hücreli).'}]},
            {'stage_title': 'Acil Tedavi ve Yatış',
             'question': 'Bu çocuk için en uygun acil yönetim hangisidir?',
             'options': [{'text': 'Potasyum içeren idame sıvısını standart hızda başlatmak ve hiperkalemiyi önlemek '
                                  'için yalnızca kalsiyum glukonat vermek',
                          'is_correct': False,
                          'scenario_update': "Sıvıdaki potasyum ve yetersiz hidrasyonla potasyum 6.4 mmol/L'ye "
                                             'yükseldi.',
                          'teaching_point': 'Tümör lizisi riskinde potasyumsuz hiperhidrasyon gerekir.'},
                         {'text': 'Potasyumsuz sıvıyla iki katı idame hızında hidrasyon ve allopürinol başlamak; '
                                  'trombosit vermek, İV antibiyotikle onkolojiye yatırmak',
                          'is_correct': True,
                          'explanation': 'Hiperhidrasyon ve allopürinol ürik asit nefropatisini önler. Ateşli ve '
                                         'sitopenik çocukta ampirik antibiyotik başlanır, kanama riskine karşı '
                                         'trombosit verilir.',
                          'new_finding': 'Hiperhidrasyon, allopürinol, trombosit süspansiyonu ve sefepim başlandı. '
                                         'Hematoloji-onkoloji servisine yatırıldı; ertesi gün kemik iliği aspirasyonu '
                                         'yapıldı ve tedavi protokolüne başlandı. Tümör lizisi gelişmedi.'},
                         {'text': 'Ateşi ve kemik ağrısı için ibuprofen vermek ve ayaktan hematoloji polikliniğine bir '
                                  'hafta içinde randevu vermek',
                          'is_correct': False,
                          'scenario_update': 'İbuprofen kanamayı artırdı; evde akut böbrek hasarı ve tümör lizisi '
                                             'gelişti.',
                          'teaching_point': 'Trombositopenide NSAİİ verilmez; hiperlökositozlu çocuk hemen '
                                            'yatırılmalıdır.'},
                         {'text': 'Sedasyonla acil kemik iliği aspirasyonu yapmak ve sonuç gelene kadar tümör lizisi '
                                  'önlemlerini beklemek',
                          'is_correct': False,
                          'scenario_update': "Önlemlerin gecikmesiyle ürik asit 13 mg/dL'ye ve kreatinin 1.4 mg/dL'ye "
                                             'yükseldi.',
                          'teaching_point': 'Tümör lizisi önlemleri tanısal girişimden önce başlatılır.'}]}]},
 {'id': 'S86',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '6 Yaşında (20 kg)',
  'gender': 'Erkek',
  'complaint': 'Altı haftadır sabahları olan baş ağrısı ve kusma, son bir haftadır yürürken sendeleme ve çift görme',
  'history': "Annesi anlatıyor: 'Bir buçuk aydır sabah uyanınca başım ağrıyor diyor, kahvaltıdan önce kusuyor, sonra "
             'rahatlıyor. Mide üşütmesi dediler, iki kez ilaç verdiler. Bir haftadır sarhoş gibi yürüyor, düşüyor. Dün '
             "televizyonu iki tane görüyorum dedi.' Son iki haftadır okulda yazısı bozulmuş, öğretmeni dikkatsizlikten "
             'şikâyet etmiş. Ateş, yakın zamanda geçirilmiş enfeksiyon veya suçiçeği yok. Kafa travması yok.',
  'final_diagnosis': 'Posterior Fossa Tümörü (Olası Medulloblastom) ve Obstrüktif Hidrosefali',
  'disposition': 'Deksametazon ve Kafa İçi Basınç Önlemleriyle Acil Beyin Cerrahisi Konsültasyonu ve Yatış',
  'case_pearl': 'Çocuklarda beyin tümörlerinin çoğu posterior fossadadır. Sabah baş ağrısı, bulantısız kusma, uykudan '
                'uyandıran ağrı ve haftalar içinde ilerleyen yakınmalar kafa içi basınç artışını düşündürür. Gövde '
                'ataksisi, nistagmus, altıncı sinir felcine bağlı çift görme ve papilödem eşlik edebilir. Tekrarlayan '
                "'gastroenterit' tanısı alan çocuklarda nörolojik muayene atlanmamalıdır. Kafa içi basınç artışı "
                'şüphesinde lomber ponksiyon yapılmaz. Tanı acil görüntülemeyle konur; MR tercih edilir, '
                'ulaşılamıyorsa BT çekilir. Ödem için deksametazon başlanır ve beyin cerrahisine danışılır. Akut '
                'ataksi, enfeksiyon sonrası günler içinde başlayıp kafa içi basınç bulgusu olmadan seyrederse '
                'serebelliti düşündürür.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Nörolojik Muayene',
             'question': 'Sabah baş ağrısı, kusma ve sendelemesi olan bu çocukta muayenede neye odaklanırsınız?',
             'options': [{'text': 'Kusma nedeniyle gastroenterit kabul edip ondansetron ve ağızdan sıvı tedavisi '
                                  'vermek, iyi görünürse taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk iki gün sonra bilinç bulanıklığı ve şiddetli baş ağrısıyla '
                                             'getirildi.',
                          'teaching_point': 'Sabahları olan, haftalardır süren kusma ve baş ağrısı gastroenteritle '
                                            'açıklanmaz; nörolojik muayene şarttır.'},
                         {'text': 'Bilinç, pupiller ve fundus muayenesiyle kranial sinirleri, yürüyüşü, serebellar '
                                  'testleri ve vital bulguları değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Fundus muayenesi papilödemi, kranial sinir muayenesi altıncı sinir '
                                         'tutulumunu, serebellar testler arka beyin yapılarının etkilenmesini '
                                         'gösterir. Bradikardi ve hipertansiyon ileri basınç artışının işaretidir.',
                          'new_finding': 'Ateş 36.8°C, KTA 84/dk, KB 112/70 mmHg, SS 20/dk. Bilinç açık, GKS 15. '
                                         'Bilateral papilödem. Sağ gözde dışa bakış kısıtlı. Horizontal nistagmus. '
                                         'Geniş tabanlı, sendeleyen yürüyüş, tandem yürüyemiyor, oturur pozisyonda '
                                         'gövde salınımı var. Sağ elde dismetri. Kas gücü normal. Ense sertliği yok.'},
                         {'text': 'Çift görme nedeniyle göz doktoruna yönlendirip gözlük muayenesi sonrası nörolojik '
                                  'değerlendirme planlamak',
                          'is_correct': False,
                          'scenario_update': 'Göz polikliniği randevusu bir hafta sonraya verildi; çocuk bu sürede '
                                             'kötüleşti.',
                          'teaching_point': 'Ataksi ve kusmayla birlikte yeni çift görme acil nörolojik değerlendirme '
                                            'gerektirir.'},
                         {'text': 'Yazının bozulması ve dikkatsizlik nedeniyle dikkat eksikliği düşünüp çocuk '
                                  'psikiyatrisine ayaktan yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Nörolojik muayene yapılmadan gönderilen çocuk birkaç gün sonra yanıtsız '
                                             'getirildi.',
                          'teaching_point': 'Yeni başlayan okul başarısı bozulması ve motor yakınmalar organik '
                                            'nedenleri dışlamayı gerektirir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Papilödem ve serebellar bulguları olan bu çocukta hangi yaklaşım uygundur?',
             'options': [{'text': 'Ensefalit ve menenjiti dışlamak için hemen lomber ponksiyon yapmak ve BOS basıncını '
                                  'ölçmek',
                          'is_correct': False,
                          'scenario_update': 'Ponksiyon sonrası çocukta bilinç bozuldu, pupiller eşitsizleşti; '
                                             'herniasyon gelişti.',
                          'teaching_point': 'Papilödem ve fokal bulgularda lomber ponksiyon herniasyona yol açabilir; '
                                            'kontrendikedir.'},
                         {'text': 'Acil beyin görüntülemesi istemek, tercihen kontrastlı MR, ulaşılamıyorsa hemen BT; '
                                  'bu sürede nörolojik izlemi sürdürmek',
                          'is_correct': True,
                          'explanation': 'Kafa içi basınç artışı ve serebellar bulgularda yapısal neden acil olarak '
                                         'görüntülenmelidir. MR arka beyin yapılarını daha iyi gösterir.',
                          'new_finding': 'BT ve ardından MR: Dördüncü ventrikülü dolduran, 4.5 cm çaplı, kontrast '
                                         'tutan, orta hatta yerleşimli kitle; lateral ve üçüncü ventriküllerde '
                                         'belirgin genişleme, periventriküler ödem.'},
                         {'text': 'Elektroensefalografi ve elektrolitler istemek; sonuçlar normalse çocuk nörolojisi '
                                  'polikliniğine ayaktan yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'EEG normal geldi; görüntüleme yapılmadan gönderildi.',
                          'teaching_point': 'EEG yapısal lezyonları göstermez; bu bulgularda acil görüntüleme '
                                            'gerekir.'},
                         {'text': 'Enfeksiyon sonrası ataksi olabileceğini düşünüp bir hafta izleyerek bulgular '
                                  'sürerse görüntüleme planlamak',
                          'is_correct': False,
                          'scenario_update': 'İzlem sırasında çocuk ani bilinç kaybı geçirdi.',
                          'teaching_point': 'Papilödem ve haftalardır süren yakınmalar enfeksiyon sonrası ataksiyle '
                                            'uyumlu değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik ve görüntüleme bulgularına göre en olası tanınız nedir?',
             'options': [{'text': 'Akut serebellar ataksi (postenfeksiyöz)',
                          'is_correct': False,
                          'scenario_update': 'Yakın zamanda enfeksiyon yoktu, yakınmalar haftalardır sürüyordu ve '
                                             'papilödem vardı.',
                          'teaching_point': 'Postenfeksiyöz ataksi viral hastalıktan sonra ani başlar, kafa içi basınç '
                                            'artışı yapmaz.'},
                         {'text': 'İdiyopatik intrakraniyal hipertansiyon',
                          'is_correct': False,
                          'scenario_update': 'Görüntülemede ventriküller genişti ve kitle vardı.',
                          'teaching_point': 'Bu tanıda görüntüleme normaldir, ventriküller dar veya normaldir.'},
                         {'text': 'Serebellar apse',
                          'is_correct': False,
                          'scenario_update': 'Ateş, kulak veya sinüs enfeksiyonu ve halka şeklinde kontrastlanma '
                                             'yoktu.',
                          'teaching_point': 'Apsede ateş, enfeksiyon odağı ve halka tarzında kontrastlanma beklenir.'},
                         {'text': 'Posterior fossa tümörü ve obstrüktif hidrosefali',
                          'is_correct': True,
                          'explanation': 'Haftalar içinde ilerleyen sabah baş ağrısı ve kusma, papilödem, altıncı '
                                         'sinir felci, gövde ataksisi, dördüncü ventrikülü dolduran kitle ve ventrikül '
                                         'genişlemesi posterior fossa tümörü ve obstrüktif hidrosefaliyi gösterir.',
                          'new_finding': 'Tanı: Posterior fossa tümörü (olası medulloblastom) ve obstrüktif '
                                         'hidrosefali.'}]},
            {'stage_title': 'Acil Yönetim ve Yatış',
             'question': 'Bu çocuk için en uygun acil yönetim hangisidir?',
             'options': [{'text': 'Deksametazon başlamak, başı 30° kaldırmak, nörolojik izlemi sürdürmek ve beyin '
                                  'cerrahisine acil danışıp yatırmak',
                          'is_correct': True,
                          'explanation': 'Deksametazon tümör çevresi ödemi azaltır. Hidrosefali için ventriküler '
                                         'drenaj veya erken cerrahi kararı beyin cerrahisi tarafından verilir.',
                          'new_finding': 'Deksametazon başlandı, baş ağrısı ve kusma azaldı. Beyin cerrahisi '
                                         'tarafından ertesi gün tümör çıkarıldı; patoloji medulloblastom geldi. Spinal '
                                         'MR ile yayılım değerlendirildi ve onkoloji tedavisi planlandı.'},
                         {'text': 'Kusma nedeniyle büyük hacimli hipotonik sıvı başlamak ve cerrahiyi birkaç gün '
                                  'sonraki elektif listeye almak',
                          'is_correct': False,
                          'scenario_update': 'Hipotonik sıvı ödemi artırdı; çocuk gece bradikardi ve bilinç kaybı '
                                             'geçirdi.',
                          'teaching_point': 'Kafa içi basınç artışında hipotonik sıvıdan kaçınılır; hidrosefali acil '
                                            'değerlendirilir.'},
                         {'text': 'Ağrısını gidermek için morfin ve sakinleşmesi için midazolam vermek, ardından genel '
                                  'pediatri servisine yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Sedasyon sonrası solunum yüzeyelleşti, pCO2 yükseldi ve kafa içi basınç '
                                             'daha da arttı.',
                          'teaching_point': 'Sedasyon nörolojik izlemi engeller ve hipoventilasyonla basıncı artırır.'},
                         {'text': 'Tümör tanısıyla doğrudan kemoterapi başlamak için onkoloji servisine yatırmak ve '
                                  'cerrahi görüşü sonraya bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Hidrosefali tedavi edilmeden bekleyen çocuk kötüleşti.',
                          'teaching_point': 'Önce hidrosefali ve kitle etkisi cerrahi olarak yönetilir; doku tanısı '
                                            'tedaviyi belirler.'}]}]},
 {'id': 'S87',
  'category': '🩸 Hematolojik & Onkolojik Aciller',
  'age': '3 Yaşında (14 kg)',
  'gender': 'Erkek',
  'complaint': 'Dünden beri aşırı solukluk, gözlerde sararma, halsizlik ve kola renginde idrar',
  'history': "Annesi anlatıyor: 'Dün sabahtan beri bembeyaz oldu, gözlerinin akı sarardı, çişi koyu kahverengi, kola "
             "gibi. Çok halsiz, sürekli uyumak istiyor.' Ailesi Aydın'da yaşıyor. Üç gün önce bahçeden toplanan taze "
             'baklayı çiğ ve pişmiş olarak bolca yemiş. Son günlerde ilaç kullanmamış, naftalin teması bilinmiyor. '
             'Ateş yok. İki yaşındayken de benzer daha hafif bir sararma olmuş, kendiliğinden geçmiş. Dayısında da '
             "'kansızlık nöbetleri' varmış.",
  'final_diagnosis': 'G6PD Eksikliğinde Bakla Tüketimine Bağlı Akut İntravasküler Hemoliz (Favizm)',
  'disposition': 'Eritrosit Transfüzyonu, Hidrasyon ve Böbrek İzlemiyle Pediatri Servisine Yatış; Tetikleyicilerden '
                 'Kaçınma Eğitimi',
  'case_pearl': "X'e bağlı kalıtılan bu enzim eksikliği Türkiye'de özellikle Akdeniz ve Ege bölgelerinde sıktır. "
                'Bakla, naftalin, bazı ilaçlar (primakin, dapson, sülfonamidler, nitrofurantoin, rasburikaz, metilen '
                'mavisi) ve enfeksiyonlar oksidatif stresle akut intravasküler hemolize yol açar. Ani solukluk, '
                'sarılık, koyu idrar (hemoglobinüri), taşikardi görülür. Coombs negatif, indirekt bilirubin ve LDH '
                'yüksek, haptoglobin düşüktür; yaymada ısırılmış hücreler ve Heinz cisimcikleri görülür. Hemoliz '
                'sırasında genç eritrositlerin enzimi yüksek olduğundan ölçüm yanlış normal çıkabilir; test 2-3 ay '
                'sonra tekrarlanır. Ağır anemi ve süren hemolizde transfüzyon verilir; hemoglobinüride hidrasyonla '
                'böbrek korunur.',
  'steps': [{'stage_title': 'İlk Değerlendirme',
             'question': 'Ani solukluk, sararma ve koyu idrarı olan bu çocukta ilk değerlendirmeniz nedir?',
             'options': [{'text': 'Sarılık nedeniyle hepatit kabul edip karaciğer testlerini istemek ve evde istirahat '
                                  'önerisiyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Hemoglobin ölçülmeden gönderilen çocuk ertesi gün nefes darlığı ve '
                                             'taşikardiyle getirildi.',
                          'teaching_point': 'Ani solukluk ve sarılık birlikteliği hemolizi düşündürür; hemoglobin '
                                            'hemen ölçülmelidir.'},
                         {'text': 'Koyu idrar nedeniyle glomerülonefrit kabul edip sıvı kısıtlaması ve diüretik '
                                  'başlayarak böbrek testlerini beklemek',
                          'is_correct': False,
                          'scenario_update': 'Sıvı kısıtlaması sonrası kreatinin yükseldi ve idrar çıkışı azaldı.',
                          'teaching_point': 'Kola renkli idrar hemoglobinüriden de kaynaklanabilir; bu durumda '
                                            'hidrasyon böbreği korur.'},
                         {'text': 'Perfüzyonu ve kalp yetersizliği bulgularını değerlendirip tam kan sayımı, '
                                  'retikülosit, bilirubin, LDH, direkt Coombs ve idrar tetkiki istemek',
                          'is_correct': True,
                          'explanation': 'Ağır anemide kalp yetersizliği gelişebilir. Retikülosit, indirekt bilirubin, '
                                         'LDH ve Coombs hemolizin varlığını ve immün kaynaklı olup olmadığını '
                                         'gösterir.',
                          'new_finding': 'KTA 152/dk, SS 30/dk, KB 94/56 mmHg, SpO2 %98, KDZ 2 sn, ateş 36.9°C. '
                                         'Belirgin soluk ve ikterik, hafif hepatomegali, dalak ele gelmiyor. Galo '
                                         'ritmi yok. Hb 5.4 g/dL, MCV 84 fL, retikülosit %8, lökosit 13.200/mm³, '
                                         'trombosit 312.000/mm³. İndirekt bilirubin 5.6 mg/dL, LDH 1.680 U/L, '
                                         'haptoglobin <10 mg/dL. Direkt Coombs negatif. İdrar: kan pozitif, '
                                         'mikroskopide eritrosit yok.'},
                         {'text': 'Demir eksikliği anemisi kabul edip yüksek doz oral demir başlamak ve bir ay sonra '
                                  'kan sayımı kontrolü planlamak',
                          'is_correct': False,
                          'scenario_update': 'Demir tedavisi akut tabloyu düzeltmedi; çocuk iki gün sonra Hb 4.1 g/dL '
                                             'ile getirildi.',
                          'teaching_point': 'Ani gelişen, sarılıklı ve normositer anemi demir eksikliğiyle '
                                            'açıklanmaz.'}]},
            {'stage_title': 'Periferik Yayma Yorumu',
             'question': 'Periferik yaymada hangi bulgu bu tabloyu en çok destekler?',
             'options': [{'text': 'Isırılmış hücreler (bite cell), kabarcıklı hücreler ve özel boyamayla '
                                  'eritrositlerde Heinz cisimcikleri',
                          'is_correct': True,
                          'explanation': 'Oksidatif hasarla çökmüş hemoglobin Heinz cisimciklerini oluşturur; dalak '
                                         'bunları uzaklaştırırken ısırılmış görünüm meydana gelir.',
                          'new_finding': 'Yaymada çok sayıda ısırılmış ve kabarcıklı eritrosit, polikromazi. '
                                         'Supravital boyamada Heinz cisimcikleri. Şistosit ve sferosit yok. Enzim '
                                         'düzeyi gönderildi.'},
                         {'text': 'Çok sayıda mikrosferosit ve osmotik frajilite artışı ile birlikte pozitif aile '
                                  'öyküsü ve belirgin splenomegali',
                          'is_correct': False,
                          'scenario_update': 'Yaymada sferosit yoktu ve dalak ele gelmiyordu.',
                          'teaching_point': 'Kalıtsal sferositozda sferositler, splenomegali ve kronik hemoliz '
                                            'bulguları görülür.'},
                         {'text': 'Şistositler (parçalanmış eritrositler), trombositopeni ve yüksek kreatininle '
                                  'birlikte kanlı ishal öyküsü',
                          'is_correct': False,
                          'scenario_update': 'Şistosit yoktu, trombosit sayısı ve kreatinin normaldi.',
                          'teaching_point': 'Şistositler ve trombositopeni mikroanjiyopatik hemolizi düşündürür.'},
                         {'text': 'Hipokrom mikrositer eritrositler, hedef hücreler ve bazofilik noktalanma ile düşük '
                                  'MCV ve yüksek RDW',
                          'is_correct': False,
                          'scenario_update': 'MCV normaldi ve hedef hücre yoktu.',
                          'teaching_point': 'Bu bulgular talasemi veya kurşun zehirlenmesini düşündürür.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Otoimmün hemolitik anemi',
                          'is_correct': False,
                          'scenario_update': 'Direkt Coombs negatifti ve sferosit yoktu.',
                          'teaching_point': 'Otoimmün hemolizde direkt Coombs pozitiftir ve sferositler görülür.'},
                         {'text': 'G6PD eksikliğinde baklaya bağlı akut hemoliz (favizm)',
                          'is_correct': True,
                          'explanation': 'Erkek çocukta bakla tüketiminden sonra gelişen ani intravasküler hemoliz, '
                                         'hemoglobinüri, Coombs negatifliği, ısırılmış hücreler ve Heinz cisimcikleri, '
                                         'önceki benzer atak ve anne tarafında benzer öykü G6PD eksikliğine bağlı '
                                         'favizmi gösterir.',
                          'new_finding': 'Tanı: G6PD eksikliğinde bakla tüketimine bağlı akut hemoliz (favizm).'},
                         {'text': 'Hemolitik üremik sendrom',
                          'is_correct': False,
                          'scenario_update': 'Kanlı ishal, trombositopeni ve böbrek yetmezliği yoktu.',
                          'teaching_point': "HÜS'te şistositler, trombositopeni ve akut böbrek hasarı birlikte "
                                            'görülür.'},
                         {'text': 'Akut viral hepatit',
                          'is_correct': False,
                          'scenario_update': 'Bilirubin indirekt baskındı ve belirgin anemi vardı.',
                          'teaching_point': 'Hepatitte direkt bilirubin ve transaminazlar yükselir, ağır anemi '
                                            'beklenmez.'}]},
            {'stage_title': 'Tedavi ve Yatış',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Hemolizi durdurmak için yüksek doz İV metilprednizolon ve intravenöz immünglobulin '
                                  'vermek',
                          'is_correct': False,
                          'scenario_update': 'Tedavi hemolizi etkilemedi; transfüzyon gecikti.',
                          'teaching_point': 'Bu hemoliz immün kaynaklı değildir; kortikosteroid ve İVİG etkisizdir.'},
                         {'text': 'Eritrosit süspansiyonu 10 mL/kg vermek, hidrasyonla idrar çıkışını korumak, servise '
                                  'yatırıp tetikleyici listesini öğretmek',
                          'is_correct': True,
                          'explanation': 'Ağır ve süren hemolizde transfüzyon doku oksijenlenmesini korur. Hidrasyon '
                                         'hemoglobinüriye bağlı böbrek hasarını önler. Aile bakla, naftalin ve riskli '
                                         'ilaçlardan kaçınmalıdır.',
                          'new_finding': 'Transfüzyon sonrası Hb 8.6 g/dL, kalp hızı 118/dk. İdrar üçüncü günde '
                                         'açıldı. Tetikleyici listesi verildi. Üç ay sonra enzim düzeyi belirgin düşük '
                                         'bulundu; anne taşıyıcı çıktı.'},
                         {'text': 'Hemoliz kendiliğinden duracağı için transfüzyon yapmadan folik asit başlayıp ertesi '
                                  'gün poliklinik kontrolüyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Evde hemoliz sürdü; çocuk Hb 3.8 g/dL ve kalp yetersizliği bulgularıyla '
                                             'getirildi.',
                          'teaching_point': 'Hb 6 g/dL altında ve süren hemolizde çocuk yatırılmalı, transfüzyon '
                                            'değerlendirilmelidir.'},
                         {'text': 'Splenektomi için çocuk cerrahisine danışmak ve tekrarlayan atakları önlemek için '
                                  'cerrahiyi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Dalak bu hemolizde temel rol oynamadığı için cerrahi yarar sağlamazdı.',
                          'teaching_point': 'Bu hastalıkta splenektominin yeri yoktur; tetikleyicilerden kaçınmak '
                                            'esastır.'}]}]},
 {'id': 'S88',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '7 Yaşında (23 kg)',
  'gender': 'Kız',
  'complaint': 'Dünden beri yüksek ateş ve tüm karına yayılan şiddetli karın ağrısı',
  'history': "Annesi anlatıyor: 'Dün öğleden sonra 39.5 ateşle birlikte karnı ağrımaya başladı, kıvranıyor, yürürken "
             "öne eğiliyor. Bir kez kustu, ishali yok.' Son iki yılda yılda 5-6 kez, 2-3 gün süren ateşli karın ağrısı "
             "atakları olmuş; her seferinde 'mide virüsü' denmiş, iki kez de apandisit şüphesiyle cerrahiye "
             'danışılmış. Ataklar arasında tamamen iyi. Bir kez de ateşle birlikte dizi şişmiş. Ailesi Sivaslı, akraba '
             'evliliği var. Amcası genç yaşta böbrek yetmezliğinden diyalize girmiş.',
  'final_diagnosis': 'Ailevi Akdeniz Ateşi (FMF) Atağı (Peritonit)',
  'disposition': 'Analjezi ve Gözlem Sonrası Kolşisin Başlanarak, Amiloidoz Taraması ve Çocuk Romatoloji Kontrolüyle '
                 'Taburculuk',
  'case_pearl': "Türkiye'de sık görülen bu otoinflamatuvar hastalık 1-3 gün süren, kendiliğinden geçen ateş ve seröz "
                'zar inflamasyonu (peritonit, plörit, artrit) ataklarıyla seyreder. Atak sırasında akut batın '
                'bulguları apandisiti taklit edebilir ve gereksiz laparotomilere yol açabilir. Ataklar arası tam '
                'iyilik hali, aile öyküsü ve akraba evliliği önemli ipuçlarıdır. Atakta CRP, sedimantasyon ve serum '
                'amiloid A yükselir, ataklar arasında normale döner. Tanı klinik kriterlerle konur, MEFV gen analizi '
                'destekler. Tedavi ömür boyu kolşisindir; ataklar ve en önemlisi amiloidoz önlenir. Amiloidozun ilk '
                'bulgusu proteinüridir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Karın Muayenesi',
             'question': 'Ateşli ve yaygın karın ağrısı olan bu çocukta ilk değerlendirmeniz nedir?',
             'options': [{'text': 'Yaygın hassasiyet olduğu için apandisit perforasyonu kabul edip görüntüleme '
                                  'yapmadan acil laparotomi için cerrahiye yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Laparotomide apendiks normal bulundu, yalnızca az miktarda seröz sıvı '
                                             'vardı.',
                          'teaching_point': 'Tekrarlayan benzer ataklar öyküsü olan çocukta görüntüleme ve öykü '
                                            'değerlendirilmeden cerrahi karar verilmez.'},
                         {'text': 'Vital bulgular ve hidrasyonu değerlendirip ayrıntılı karın muayenesi yapmak, '
                                  'tekrarlayan atakların özelliklerini ve aile öyküsünü derinleştirmek',
                          'is_correct': True,
                          'explanation': 'Ataklar arası tam iyilik, kısa süreli kendiliğinden geçen ateşli ataklar, '
                                         'artrit ve aile öyküsü ayırıcı tanıyı belirgin şekilde daraltır.',
                          'new_finding': 'Ateş 39.3°C, KTA 132/dk, KB 104/66 mmHg, SS 24/dk. Mukozalar hafif kuru. '
                                         'Karında yaygın hassasiyet ve hafif defans, belirgin lokalize hassasiyet yok, '
                                         'rebound şüpheli. Bağırsak sesleri azalmış. Akciğer ve eklem muayenesi '
                                         'normal. Döküntü yok.'},
                         {'text': 'Ağrı muayeneyi zorlaştırmasın diye hiçbir analjezik vermeden çocuğu saatlerce aç '
                                  'izleyip seri muayene yapmak',
                          'is_correct': False,
                          'scenario_update': 'Analjezi verilmeyen çocuk saatlerce kıvrandı ve aile büyük sıkıntı '
                                             'yaşadı.',
                          'teaching_point': 'Analjezi muayene bulgularını gizlemez; akut karın ağrısında güvenle '
                                            'verilmelidir.'},
                         {'text': 'Mide virüsü kabul edip ağızdan sıvı ve antiemetik vererek taburcu etmek ve ateş '
                                  'düşmezse kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Tekrarlayan ataklar yine değerlendirilmeden geçiştirildi ve tanı '
                                             'yıllarca gecikti.',
                          'teaching_point': 'Tekrarlayan ateşli karın ağrısı atakları her seferinde gastroenterit '
                                            'olarak açıklanmamalıdır.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Analjezi sonrası ağrısı azalan bu çocukta hangi tetkikler en uygundur?',
             'options': [{'text': 'Batın tomografisi çekmek ve ardından bağırsak duvarını görmek için kolonoskopi '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'Tomografi yönetimi değiştirmedi; çocuk gereksiz radyasyon aldı.',
                          'teaching_point': 'Çocuklarda karın ağrısında ilk görüntüleme ultrasonografidir.'},
                         {'text': 'Tam kan sayımı, CRP, sedimantasyon, serum amiloid A, idrar tetkiki ve proteinüri '
                                  'ile karın ultrasonografisi istemek',
                          'is_correct': True,
                          'explanation': 'Ultrasonografi apandisiti değerlendirir. Akut faz belirteçleri atak '
                                         'sırasında belirgin yükselir. İdrarda protein amiloidozun ilk bulgusudur.',
                          'new_finding': 'Lökosit 15.800/mm³ (nötrofil %84), CRP 148 mg/L, sedimantasyon 62 mm/sa, '
                                         'serum amiloid A çok yüksek. İdrar normal, proteinüri yok. Ultrasonografide '
                                         'apendiks 4 mm, kompresyonla daralıyor, çevresinde inflamasyon yok; '
                                         "Douglas'ta az miktarda serbest sıvı."},
                         {'text': 'Tetkik yapmadan antibiyotik başlayıp ateş düşene kadar beklemek ve sonraki atakta '
                                  'değerlendirme yapmak',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik etkisizdi; atak kendi süresinde geçti ve tanı yine konmadı.',
                          'teaching_point': 'Bu ataklar antibiyotikten bağımsız olarak 1-3 günde kendiliğinden geçer.'},
                         {'text': 'Lomber ponksiyon ve kan kültürü yapıp menenjit ve sepsisi dışlamak için sonuçları '
                                  'beklemek',
                          'is_correct': False,
                          'scenario_update': 'Menenjit bulgusu olmayan çocukta gereksiz girişim yapıldı.',
                          'teaching_point': 'Tetkikler klinik bulgulara göre seçilmelidir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Akut apandisit',
                          'is_correct': False,
                          'scenario_update': 'Apendiks ultrasonografide normaldi ve benzer ataklar kendiliğinden '
                                             'geçmişti.',
                          'teaching_point': 'Apandisitte apendiks çapı 6 mm üzerinde, kompresyonla daralmaz ve '
                                            'çevresinde inflamasyon görülür.'},
                         {'text': 'Ailevi Akdeniz ateşi atağı (peritonit)',
                          'is_correct': True,
                          'explanation': 'Akraba evliliği ve amiloidoz düşündüren aile öyküsü olan çocukta 2-3 gün '
                                         'süren tekrarlayan ateşli peritonit ve artrit atakları, ataklar arası tam '
                                         'iyilik, belirgin akut faz yanıtı ve normal apendiks ailevi Akdeniz ateşi '
                                         'atağını gösterir.',
                          'new_finding': 'Tanı: Ailevi Akdeniz ateşi atağı (peritonit). MEFV gen analizinde M694V '
                                         'homozigot mutasyon saptandı.'},
                         {'text': 'Henoch-Schönlein purpurası',
                          'is_correct': False,
                          'scenario_update': 'Palpabl purpura yoktu ve ataklar tekrarlayıcıydı.',
                          'teaching_point': "HSP'de alt ekstremitelerde palpabl purpura, artrit ve karın ağrısı "
                                            'görülür.'},
                         {'text': 'Primer bakteriyel peritonit',
                          'is_correct': False,
                          'scenario_update': 'Nefrotik sendrom veya asit yoktu; benzer ataklar kendiliğinden geçmişti.',
                          'teaching_point': 'Primer peritonit çoğunlukla nefrotik sendrom veya sirozla ilişkilidir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun uzun dönem plan hangisidir?',
             'options': [{'text': 'Yalnızca ataklar sırasında kolşisin kullanmalarını ve ataklar arasında ilacı '
                                  'tamamen bırakmalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Ataklar sürdü ve yıllar içinde proteinüri gelişti.',
                          'teaching_point': 'İlaç her gün, ömür boyu kullanılır; amaç atakları ve amiloidozu '
                                            'önlemektir.'},
                         {'text': 'Ataklar seyrek olduğu için tedavi gerekmediğini söyleyip yalnızca ağrı kesiciyle '
                                  'izlemeyi önermek',
                          'is_correct': False,
                          'scenario_update': 'Tedavisiz izlenen çocukta ilerleyen yıllarda nefrotik düzeyde proteinüri '
                                             'gelişti.',
                          'teaching_point': 'Tedavisiz hastalarda amiloidoz riski yüksektir; tanı konan her hastaya '
                                            'tedavi başlanır.'},
                         {'text': 'Analjeziyle atak geçince her gün kolşisin başlamak, aileye ömür boyu kullanımı '
                                  'anlatmak ve proteinüri izlemi planlamak',
                          'is_correct': True,
                          'explanation': 'Günlük kolşisin atak sıklığını azaltır ve amiloidozu önler. Düzenli idrar '
                                         'protein izlemi böbrek tutulumunu erken yakalar.',
                          'new_finding': 'Atak 48 saatte kendiliğinden geriledi. Kolşisin başlandı, aile '
                                         'bilgilendirildi. Romatoloji kontrolünde atak sıklığı belirgin azaldı; '
                                         'proteinüri gelişmedi. Kardeşleri de değerlendirmeye çağrıldı.'},
                         {'text': 'Ataklar sırasında uzun süreli yüksek doz oral kortikosteroid başlamak ve ataklar '
                                  'belirgin şekilde seyrekleşince dozu yavaşça azaltmak',
                          'is_correct': False,
                          'scenario_update': 'Kortikosteroid atakları önlemedi; çocukta kilo artışı ve büyüme '
                                             'yavaşlaması oldu.',
                          'teaching_point': 'Bu hastalıkta kortikosteroidin yeri yoktur; temel tedavi '
                                            'kolşisindir.'}]}]},
 {'id': 'S89',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '16 Yaşında (54 kg)',
  'gender': 'Kız',
  'complaint': 'Bugün aniden başlayan sağ alt karın ağrısı, baş dönmesi ve bir kez bayılma',
  'history': "Annesiyle geldi. Annesi: 'Okulda karnım ağrıyor dedi, tuvalette bayılmış. Apandisit mi?' Hasta ilk "
             'görüşmede adet düzensizliği dışında bir şey söylemedi. Anne odadan çıkarıldıktan sonra yapılan gizlilik '
             'gözetilen görüşmede son adetinin yedi hafta önce olduğunu, bir aydır erkek arkadaşıyla cinsel ilişkisi '
             'olduğunu, iki gündür hafif lekelenme tarzında kanaması olduğunu anlatıyor. Bir yıl önce pelvik '
             'enfeksiyon nedeniyle antibiyotik kullanmış. Ağrı sağ omzuna da vuruyor.',
  'final_diagnosis': 'Rüptüre Ektopik (Tubal) Gebelik ve Hemoperitoneum',
  'disposition': 'Resüsitasyon, Kan Hazırlığı ve Acil Laparoskopi İçin Kadın Hastalıkları ve Doğum Kliniğine Yatış',
  'case_pearl': 'Doğurganlık çağındaki her ergen kızda karın ağrısı, bayılma veya vajinal kanamada gebelik testi '
                'yapılmalıdır. Öykü ergenle yalnız ve gizlilik gözetilerek alınmalıdır. Pelvik enfeksiyon öyküsü tubal '
                "hasar yoluyla risk faktörüdür. Pozitif test, boş uterus, adneksiyal kitle ve Douglas'ta serbest sıvı "
                'tanıyı düşündürür. Omuz ağrısı diyafram irritasyonuna bağlı karın içi kanamanın işaretidir. '
                'Hemodinamik bozuklukta iki geniş damar yolu, kan grubu ve çapraz karşılaştırma yapılır, Rh negatif '
                'hastalara anti-D verilir ve acil cerrahi uygulanır. Hemodinamisi stabil, rüptür olmayan erken '
                'olgularda metotreksat seçilebilir. On sekiz yaş altı gebelikte yasal bildirim yükümlülükleri '
                'gözetilir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Öykü',
             'question': 'Sağ alt karın ağrısı ve bayılması olan bu ergende ilk yaklaşımınız nedir?',
             'options': [{'text': 'Apandisit kabul edip annenin yanında kısa öykü almak ve doğrudan çocuk cerrahisine '
                                  'yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Ergen annesinin yanında cinsel öyküsünü paylaşmadı; asıl neden gözden '
                                             'kaçtı ve kanama sürdü.',
                          'teaching_point': 'Ergenle gizlilik gözetilerek yalnız görüşülmeli ve gebelik olasılığı her '
                                            'zaman sorgulanmalıdır.'},
                         {'text': 'Vital bulguları değerlendirip iki geniş damar yolu açmak, gebelik testi ve kan '
                                  'grubu göndermek',
                          'is_correct': True,
                          'explanation': 'Bayılma ve omuz ağrısı karın içi kanamayı düşündürür; damar yolu ve kan '
                                         'hazırlığı erkenden yapılmalıdır. Gebelik testi ayırıcı tanının '
                                         'merkezindedir.',
                          'new_finding': 'KTA 128/dk, KB 88/54 mmHg, SS 22/dk, SpO2 %99, ateş 36.7°C, KDZ 3 sn. Soluk '
                                         've terli. Sağ alt kadranda belirgin hassasiyet, rebound ve defans; karında '
                                         'yaygın hassasiyet. İdrar gebelik testi pozitif, serum β-hCG 3.850 mIU/mL. Hb '
                                         '9.2 g/dL. Kan grubu A Rh negatif.'},
                         {'text': 'Bayılmayı vazovagal kabul edip ağızdan sıvı vermek, ağrı kesiciyle izleyip ağrı '
                                  'geçerse taburcu etmek',
                          'is_correct': False,
                          'scenario_update': "Bekleme sırasında kan basıncı 70/40 mmHg'ye düştü ve bilinç "
                                             'bulanıklaştı.',
                          'teaching_point': 'Karın ağrısıyla birlikte bayılma karın içi kanama açısından '
                                            'değerlendirilmelidir.'},
                         {'text': 'Pelvik enfeksiyon öyküsü nedeniyle tekrarlayan pelvik inflamatuvar hastalık kabul '
                                  'edip ayaktan antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'Gebelik testi yapılmadan antibiyotikle gönderilen hasta şok tablosuyla '
                                             'geri geldi.',
                          'teaching_point': 'Pelvik enfeksiyon öyküsü tüp hasarı yoluyla uterus dışı gebelik için risk '
                                            'faktörüdür; önce gebelik dışlanmalıdır.'}]},
            {'stage_title': 'Görüntüleme Kararı',
             'question': 'Gebelik testi pozitif ve hipotansif olan bu ergende hangi görüntüleme uygundur?',
             'options': [{'text': 'Kontrastlı batın tomografisi çekip apandisiti dışlamak ve sonra kadın doğum '
                                  'konsültasyonu istemek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi için harcanan sürede hasta şoka girdi; gebelikte gereksiz '
                                             'radyasyon verildi.',
                          'teaching_point': 'Gebelikte ve instabil hastada tomografi yerine yatak başı ultrasonografi '
                                            'tercih edilir.'},
                         {'text': 'Yatak başı ultrasonografiyle karın içi serbest sıvıyı aramak, uterus içinde gebelik '
                                  'kesesini ve adneksleri değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Yatak başı ultrasonografi hızlıdır ve hastayı yerinden kaldırmadan karın içi '
                                         'kanamayı gösterir. Uterus içinde gebelik görülmemesi ve adneksiyal kitle '
                                         'tanıyı destekler.',
                          'new_finding': "Uterus boş, endometrium kalın. Sağ adnekste 3 cm'lik heterojen kitle. "
                                         'Douglas boşluğunda ve Morison poşunda pıhtı içeren yaygın serbest sıvı.'},
                         {'text': 'β-hCG düzeyinin 48 saat sonraki artışını görmek için tekrar ölçüm planlamak ve '
                                  'hastayı serviste izlemek',
                          'is_correct': False,
                          'scenario_update': "İzlem sırasında hemoglobin 6.8 g/dL'ye düştü ve hasta şoka girdi.",
                          'teaching_point': 'Seri β-hCG izlemi yalnızca stabil ve kanaması olmayan hastalarda '
                                            'uygundur.'},
                         {'text': 'Pelvik MR istemek ve kitlenin niteliğini belirledikten sonra tedavi kararını vermek',
                          'is_correct': False,
                          'scenario_update': 'MR için beklenirken hasta hemodinamik olarak kötüleşti.',
                          'teaching_point': 'İnstabil hastada uzun süren görüntülemelerden kaçınılır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Rüptüre over kisti',
                          'is_correct': False,
                          'scenario_update': 'Gebelik testi pozitifti ve uterus boştu.',
                          'teaching_point': 'Over kisti rüptüründe gebelik testi negatiftir.'},
                         {'text': 'Akut apandisit',
                          'is_correct': False,
                          'scenario_update': 'Gebelik testi pozitifti, karında pıhtılı yaygın sıvı ve adneksiyal kitle '
                                             'vardı.',
                          'teaching_point': 'Apandisitte hipotansiyon ve hemoperitoneum beklenmez.'},
                         {'text': 'Over torsiyonu',
                          'is_correct': False,
                          'scenario_update': 'Gebelik testi pozitifti ve yaygın kanamalı serbest sıvı vardı.',
                          'teaching_point': 'Over torsiyonunda büyümüş over ve azalmış akım görülür; kanama tipik '
                                            'değildir.'},
                         {'text': 'Rüptüre ektopik gebelik ve hemoperitoneum',
                          'is_correct': True,
                          'explanation': 'Pozitif gebelik testi, boş uterus, adneksiyal kitle, pıhtılı serbest sıvı, '
                                         'hipotansiyon, bayılma ve omuz ağrısı rüptüre ektopik gebelik ve '
                                         'hemoperitoneumu gösterir.',
                          'new_finding': 'Tanı: Rüptüre sağ tubal (ektopik) gebelik ve hemoperitoneum.'}]},
            {'stage_title': 'Acil Tedavi',
             'question': 'Bu hasta için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Kristaloid ve kan ürünleriyle resüsitasyon yapıp anti-D vermek ve kadın doğumla '
                                  'acil laparoskopiye almak',
                          'is_correct': True,
                          'explanation': 'Rüptür ve hemodinamik bozuklukta cerrahi tek seçenektir. Rh negatif hastada '
                                         'anti-D ilerideki gebelikleri korur.',
                          'new_finding': 'Bir ünite eritrosit verildi, anti-D yapıldı. Laparoskopide sağ tüpte rüptüre '
                                         'gebelik ve 800 mL hemoperitoneum saptandı, salpenjektomi yapıldı. Hasta ve '
                                         'ailesiyle psikososyal destek planlandı, yasal süreç sosyal hizmetle '
                                         'yürütüldü.'},
                         {'text': 'Ağızdan ilk dozu verilen metotreksat ile medikal tedavi başlayıp hastayı serviste '
                                  'seri β-hCG ile izlemek',
                          'is_correct': False,
                          'scenario_update': 'Medikal tedavi kanamayı durdurmadı; hasta derin şoka girdi.',
                          'teaching_point': 'Metotreksat yalnızca hemodinamisi stabil, rüptür olmayan olgularda '
                                            'seçilir.'},
                         {'text': 'Hastanın isteği üzerine durumu ailesinden tamamen gizlemek ve onam almadan '
                                  'cerrahiye göndermeden izlemek',
                          'is_correct': False,
                          'scenario_update': 'Hayati girişim gecikti ve yasal süreçler yürütülmedi.',
                          'teaching_point': 'Gizlilik önemlidir ancak hayati tehlikede ve yasal bildirim gerektiren '
                                            'durumlarda sınırları vardır; süreç hasta ile birlikte yönetilir.'},
                         {'text': 'Kanamanın kendiliğinden durmasını beklemek için traneksamik asit verip hastayı '
                                  'yoğun bakımda gözlemek',
                          'is_correct': False,
                          'scenario_update': 'Kanama durmadı ve hasta masif transfüzyon gerektirdi.',
                          'teaching_point': 'Kanayan bir tüp cerrahi olarak kontrol altına alınmalıdır.'}]}]},
 {'id': 'S90',
  'category': '💧 Sıvı-Elektrolit & Renal / Ürolojik Aciller',
  'age': '10 Yaşında',
  'gender': 'Erkek',
  'complaint': 'Dünden beri giderek artan sol testis ağrısı ve hafif şişlik',
  'history': "Babası anlatıyor: 'Dün öğleden sonra sol yumurtalığım ağrıyor dedi, gece biraz arttı. Yürürken ağrıyor "
             "ama uyuyabildi. Kusma yok.' Ağrı aniden değil yavaş yavaş başlamış. Travma, ateş, idrar yaparken yanma "
             'yok. Cinsel aktivite yok. Kabakulak geçirmemiş, aşıları tam. Daha önce benzer ağrı olmamış.',
  'final_diagnosis': 'Appendiks Testis (Morgagni Hidatiği) Torsiyonu',
  'disposition': 'NSAİİ, İstirahat ve Skrotal Destekle Sarı Alandan Taburculuk; Ağrı Artarsa Hemen Başvuru Önerisi',
  'case_pearl': 'Prepubertal erkek çocukta akut skrotumun en sık nedeni testis eklerinin torsiyonudur. Ağrı genellikle '
                'daha yavaş başlar, testisin üst kutbunda lokalize hassasiyet vardır ve bazen deri altında mavi-siyah '
                'bir nokta görülür. Kremaster refleksi korunur, testis normal pozisyondadır. Testis torsiyonunda ise '
                'ani şiddetli ağrı, kusma, yüksek yerleşimli ve yatay duran testis, kremaster refleksinin kaybı '
                'tipiktir. Kuşkuda renkli Doppler ultrasonografi testis kan akımını değerlendirir; ancak klinik olarak '
                'testis torsiyonu düşünülüyorsa görüntüleme beklenmeden cerrahiye danışılır. Ek torsiyonu NSAİİ ve '
                'istirahatle 5-10 günde geçer.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Testis ağrısı olan bu çocuğun muayenesinde neye dikkat edersiniz?',
             'options': [{'text': 'Ağrı bir günü geçtiği için testisin kurtarılamayacağını düşünüp muayene etmeden '
                                  'ağrı kesiciyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Muayene edilmeden gönderilen çocuğun tanısı belirsiz kaldı.',
                          'teaching_point': 'Her akut skrotumda ayrıntılı muayene yapılmalıdır; süre tek başına karar '
                                            'vermez.'},
                         {'text': 'Testisin pozisyonunu ve duruşunu, hassasiyetin yerini, kremaster refleksini ve '
                                  'skrotal deriyi iki taraflı karşılaştırarak değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Testis pozisyonu, hassasiyetin yeri ve kremaster refleksi testis torsiyonunu '
                                         'diğer nedenlerden ayırmada en değerli muayene bulgularıdır.',
                          'new_finding': 'Ateş 36.8°C, genel durum iyi, KTA 96/dk. Sol hemiskrotumda hafif ödem ve '
                                         'kızarıklık. Sol testis normal yerleşimli, dikey duruşlu, testis gövdesi '
                                         "hassas değil. Üst kutupta 3-4 mm'lik çok hassas nodül ve üzerinde deri "
                                         'altında mavi-siyah renk değişikliği. Kremaster refleksi iki tarafta var. '
                                         'Karın muayenesi normal.'},
                         {'text': 'Testis ağrısını kabakulak orşiti kabul edip muayeneyi kısa tutarak tükürük '
                                  'bezlerini değerlendirmek ve evde izlem önermek',
                          'is_correct': False,
                          'scenario_update': 'Parotis şişliği yoktu; testis muayenesi ayrıntılı yapılmadı ve ayırıcı '
                                             'tanı eksik kaldı.',
                          'teaching_point': 'Orşit genellikle parotitten sonra, ergenlik sonrası görülür; aşılı '
                                            'prepubertal çocukta olası değildir.'},
                         {'text': 'İdrar yolu enfeksiyonu kabul edip yalnızca idrar tetkiki istemek ve sonuç gelene '
                                  'kadar ampirik antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'İdrar tetkiki normal geldi; skrotal muayene ve görüntüleme gecikti.',
                          'teaching_point': 'Akut skrotumda önce testis muayenesi yapılmalıdır.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Bu muayene bulgularıyla hangi yaklaşım uygundur?',
             'options': [{'text': 'Görüntüleme yapmadan doğrudan acil skrotal eksplorasyon için çocuk ürolojisine '
                                  'ameliyathane hazırlığı istemek',
                          'is_correct': False,
                          'scenario_update': 'Testis torsiyonu bulgusu olmayan çocuk gereksiz bir cerrahi girişimle '
                                             'karşı karşıya kaldı.',
                          'teaching_point': 'Klinik testis torsiyonunu düşündürmüyorsa Doppler ile değerlendirme '
                                            'yapılabilir.'},
                         {'text': 'Tam kan sayımı, CRP ve kan kültürü göndermek; sonuç gelene kadar İV antibiyotik '
                                  'başlayıp servise yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Sonuçlar normal geldi ve çocuk gereksiz yere yatırıldı.',
                          'teaching_point': 'Ateşsiz, lokalize hassasiyeti olan çocukta enfeksiyon belirteçleri tanıya '
                                            'katkı sağlamaz.'},
                         {'text': 'Testis kan akımını göstermek için iki taraflı renkli Doppler ultrasonografi istemek '
                                  've idrar tetkiki yapmak',
                          'is_correct': True,
                          'explanation': 'Doppler testis akımının korunduğunu göstererek testis torsiyonunu dışlar ve '
                                         'eklerdeki değişikliği gösterebilir. İdrar tetkiki epididimiti '
                                         'değerlendirmeye yardımcı olur.',
                          'new_finding': 'Doppler: Her iki testiste kan akımı simetrik ve normal. Sol testis üst '
                                         "kutbunda 5 mm'lik, akım izlenmeyen, hipoekoik-heterojen oval yapı; "
                                         'çevresinde hafif reaktif hidrosel. Epididim normal boyut ve akımda. İdrar '
                                         'tetkiki normal.'},
                         {'text': 'Skrotal manüel detorsiyon yapmak için testisi dışa doğru çevirmek ve ardından '
                                  'ağrının azalıp azalmadığına bakmak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz manipülasyon çocukta şiddetli ağrıya neden oldu.',
                          'teaching_point': 'Manüel detorsiyon yalnızca testis torsiyonunda ve cerrahi gecikecekse '
                                            'geçici bir önlemdir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik ve Doppler bulgularına göre en olası tanınız nedir?',
             'options': [{'text': 'Testis (spermatik kord) torsiyonu',
                          'is_correct': False,
                          'scenario_update': 'Testis akımı normaldi, kremaster refleksi vardı ve testis normal '
                                             'pozisyondaydı.',
                          'teaching_point': 'Testis torsiyonunda akım azalmış veya yoktur ve testis yüksek, yatay '
                                            'yerleşimlidir.'},
                         {'text': 'Akut epididimit',
                          'is_correct': False,
                          'scenario_update': 'Epididim normaldi ve idrar tetkiki temizdi.',
                          'teaching_point': 'Epididimitte epididim büyük ve hiperemiktir; sıklıkla idrar bulguları '
                                            'eşlik eder.'},
                         {'text': 'Appendiks testis torsiyonu',
                          'is_correct': True,
                          'explanation': 'Yavaş başlayan ağrı, üst kutupta lokalize hassas nodül ve mavi-siyah renk '
                                         'değişikliği, korunmuş kremaster refleksi, normal testis akımı ve akımsız ek '
                                         'yapısı appendiks testis torsiyonunu gösterir.',
                          'new_finding': 'Tanı: Appendiks testis torsiyonu.'},
                         {'text': 'İnkarsere inguinal herni',
                          'is_correct': False,
                          'scenario_update': 'Kasık kanalında kitle yoktu ve barsak bulgusu saptanmadı.',
                          'teaching_point': 'İnkarsere hernide kasıktan skrotuma uzanan, redükte edilemeyen kitle '
                                            'olur.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'İbuprofen, birkaç gün istirahat ve skrotal destek önermek; ağrı ani artarsa veya '
                                  'kusma olursa hemen başvurmalarını söylemek',
                          'is_correct': True,
                          'explanation': 'Ek torsiyonu kendiliğinden geçer; tedavi ağrı kontrolüdür. Uyarı bulguları '
                                         'öğretilerek nadir görülen testis torsiyonunun atlanması önlenir.',
                          'new_finding': 'İbuprofen başlandı. Bir hafta sonraki kontrolde ağrı tamamen geçmişti, '
                                         'muayene normaldi.'},
                         {'text': 'Aynı durumun tekrarlamaması için iki taraflı testis fiksasyonu amacıyla elektif '
                                  'ameliyat listesine almak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz bir cerrahi planlandı; ek torsiyonunda fiksasyon gerekmez.',
                          'teaching_point': 'Ek torsiyonunda cerrahi yalnızca ağrısı geçmeyen nadir olgularda '
                                            'düşünülür.'},
                         {'text': 'Enfeksiyon olasılığına karşı iki hafta oral siprofloksasin vermek ve kontrol '
                                  'ultrasonografisiyle izlemek',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik gereksizdi ve çocukta bulantı yaptı.',
                          'teaching_point': 'Bu tabloda enfeksiyon yoktur; antibiyotik gerekmez.'},
                         {'text': 'Çocuğu bir hafta okula göndermemek, sıcak su torbası uygulamak ve ağrı için '
                                  'kodeinli şurup vermek',
                          'is_correct': False,
                          'scenario_update': 'Kodein çocuklarda solunum depresyonu riski nedeniyle önerilmez; sıcak '
                                             'uygulama ödemi artırdı.',
                          'teaching_point': 'NSAİİ yeterlidir; kodein bu yaş grubunda kullanılmaz.'}]}]}]
