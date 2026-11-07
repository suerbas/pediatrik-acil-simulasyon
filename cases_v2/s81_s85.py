# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - S81-S85 (Toksikoloji, Bölgesel Enfeksiyonlar, Kardiyoloji ve Onkoloji)
"""

SPOILERS = {
    "S81": ["sentetik kannabinoid", "kannabinoid", "bonzai", "jamaika"],
    "S82": ["kkka", "kırım", "kongo", "hemorajik ateş"],
    "S83": ["bruselloz", "brusella", "brucella", "malta humması"],
    "S84": ["uzun qt", "long qt", "lqts"],
    "S85": ["lösemi", "lenfoblastik", "all"],
}

CASES = [
    {
        "id": "S81",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "15 Yaşında (58 kg)",
        "gender": "Erkek",
        "complaint": "Arkadaşlarıyla parkta olduğu sırada başlayan aşırı huzursuzluk, saldırganlık, kusma ve çarpıntı",
        "history": "Arkadaşları 112'yi aramış, olay yerinden ayrılmışlar. Babası hastaneye sonradan geldi: 'Son aylarda okuldan kaçıyor, notları düştü, para istiyor. Bir şey kullanıyor mu bilmiyorum.' Ambulans ekibi çocuğun 'bir şey içtik' dediğini ama ne olduğunu söylemediğini bildiriyor. Bilinen hastalığı ve ilaç kullanımı yok. Kafa travması öyküsü yok. Cebinde kuru ot parçacıkları olan küçük bir paket bulunmuş.",
        "final_diagnosis": "Sentetik Kannabinoid (Bonzai) İntoksikasyonu",
        "disposition": "Benzodiazepinle Ajitasyon Kontrolü, Monitörizasyon ve Rabdomiyoliz-Böbrek İzlemi Sonrası Gözlem; Gizlilik Gözetilerek Ergen Psikiyatrisi ve Bağımlılık Merkezi Yönlendirmesi",
        "case_pearl": "Türkiye'de ergenlerde sık görülen sentetik kannabinoidler doğal esrardan çok daha güçlüdür. Ajitasyon, psikoz, taşikardi, hipertansiyon, kusma, nöbet, hipertermi, rabdomiyoliz, akut böbrek hasarı ve aritmiye yol açabilir. Standart idrar ilaç taramasında saptanmazlar; negatif tarama tanıyı dışlamaz. Ajitasyonda ilk seçenek İV benzodiazepindir; uzun süreli fiziksel kısıtlama hipertermi ve rabdomiyolizi artırır. Kan şekeri, elektrolitler, CK, kreatinin ve EKG değerlendirilir. Ergenle ebeveyn olmadan, gizlilik gözetilerek görüşülür; madde kullanımı için bağımlılık merkezine (ÇEMATEM) yönlendirme yapılır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Ajitasyon Yönetimi",
                "question": "Ajite, terli ve taşikardik bu ergene ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Güvenlik görevlileriyle sedyeye bağlayıp bileklerinden sıkıca sabitlemek ve ilaç vermeden sakinleşene kadar saatlerce fiziksel olarak kısıtlı tutmak",
                        "is_correct": False,
                        "scenario_update": "Kısıtlamaya karşı direnen çocukta vücut ısısı 40.1°C'ye yükseldi, CK 18.000 U/L'ye çıktı.",
                        "teaching_point": "Uzun süreli fiziksel kısıtlama hipertermi ve rabdomiyolizi artırır; kimyasal sedasyon tercih edilir."
                    },
                    {
                        "text": "Sakin bir ortamda monitörize etmek, kan şekeri ve ısıyı ölçmek; ajitasyon için İV midazolam veya diazepam vermek",
                        "is_correct": True,
                        "explanation": "Sempatomimetik bulgular ve ajitasyonda benzodiazepin hem sakinleştirir hem taşikardi, hipertansiyon ve nöbet riskini azaltır. Hipoglisemi ve hipertermi hemen dışlanmalıdır.",
                        "new_finding": "Midazolam öncesi: KTA 142/dk, KB 154/94 mmHg, SS 24/dk, SpO2 %98, ateş 38.1°C, kan şekeri 128 mg/dL. Pupiller normal boyutta, konjonktivalar hiperemik. Cilt terli. Paranoid düşünceler, 'beni öldürecekler' diyor. Midazolam 5 mg İV sonrası sakinleşti; KTA 112/dk, KB 132/80 mmHg."
                    },
                    {
                        "text": "Ajitasyonu psikotik atak kabul edip yüksek doz intramüsküler haloperidol yapmak ve psikiyatri servisine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Haloperidol sonrası QTc uzadı ve çocuk nöbet geçirdi.",
                        "teaching_point": "Zehirlenme şüphesinde ilk seçenek benzodiazepindir; antipsikotikler nöbet eşiğini düşürüp QT'yi uzatabilir."
                    },
                    {
                        "text": "Babası gelene ve onam verene kadar tedaviye başlamamak, çocuğu bekleme salonunda gözetim altında oturtmak",
                        "is_correct": False,
                        "scenario_update": "Bekleme salonunda çocuk jeneralize nöbet geçirdi.",
                        "teaching_point": "Acil durumlarda tedavi onam beklenmeden yapılır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Sakinleşen bu ergende hangi tetkikler en uygundur?",
                "options": [
                    {
                        "text": "Yalnızca idrar ilaç taraması istemek; negatif gelirse zehirlenmeyi dışlayıp çocuğu psikiyatriye göndermek",
                        "is_correct": False,
                        "scenario_update": "İdrar taraması negatif geldi; ölçülmeyen CK ve kreatinin sonradan yüksek bulundu.",
                        "teaching_point": "Bazı yeni maddeler standart idrar taramasında görülmez; negatif sonuç zehirlenmeyi dışlamaz."
                    },
                    {
                        "text": "Acil beyin tomografisi ve lomber ponksiyonla ensefaliti dışlamak, sonra toksikolojik değerlendirmeye geçmek",
                        "is_correct": False,
                        "scenario_update": "Tetkikler normal geldi; asıl organ hasarı belirteçleri geç değerlendirildi.",
                        "teaching_point": "Açık bir zehirlenme öyküsü olan, odak bulgusuz ergende önce toksikolojik değerlendirme yapılır."
                    },
                    {
                        "text": "EKG, elektrolitler, CK, kreatinin, karaciğer testleri ve kan gazı göndermek; parasetamol ve etanol düzeyi istemek",
                        "is_correct": True,
                        "explanation": "Bu tablo aritmi, rabdomiyoliz ve böbrek hasarına yol açabilir. Kasıtlı alımda eşlik eden parasetamol ve alkol rutin olarak araştırılır.",
                        "new_finding": "EKG: sinüs taşikardisi, QTc 440 ms. K 3.3 mmol/L, CK 2.400 U/L, kreatinin 1.1 mg/dL, kan gazı normal. Parasetamol ve etanol saptanmadı. İdrar ilaç taraması (esrar dahil) negatif."
                    },
                    {
                        "text": "Tetkik istemeden çocuğu iki saat izlemek, sakinse babasına teslim edip yalnızca okul rehberlik servisine yönlendirmekle yetinmek",
                        "is_correct": False,
                        "scenario_update": "Evde yeniden ajitasyon ve kas ağrısı başladı; koyu renkli idrar fark edildi.",
                        "teaching_point": "Organ hasarı belirteçleri değerlendirilmeden ve gözlem süresi tamamlanmadan taburculuk yapılmaz."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu ergendeki tablonun en olası nedeni nedir?",
                "options": [
                    {"text": "Sentetik kannabinoid intoksikasyonu", "is_correct": True, "explanation": "Kuru ot içeren paket, sempatomimetik bulgular, paranoid psikoz, kusma, konjonktival hiperemi ve CK yüksekliğine rağmen standart taramanın negatif olması sentetik kannabinoid intoksikasyonunu gösterir.", "new_finding": "Tanı: Sentetik kannabinoid (bonzai) intoksikasyonu."},
                    {"text": "Antikolinerjik zehirlenme", "is_correct": False, "scenario_update": "Cilt terliydi ve pupiller geniş değildi.", "teaching_point": "Antikolinerjik tabloda cilt kuru ve kızarık, pupiller geniş, bağırsak sesleri azalmıştır."},
                    {"text": "Akut psikotik bozukluk", "is_correct": False, "scenario_update": "Belirgin otonom bulgular, ateş ve CK yüksekliği vardı.", "teaching_point": "Primer psikozda otonom instabilite ve kas hasarı beklenmez; önce organik neden dışlanır."},
                    {"text": "Serotonin sendromu", "is_correct": False, "scenario_update": "Serotonerjik ilaç kullanımı, klonus ve hiperrefleksi yoktu.", "teaching_point": "Serotonin sendromunda serotonerjik ilaç öyküsü, klonus ve hiperrefleksi tipiktir."}
                ]
            },
            {
                "stage_title": "Gözlem ve Yönlendirme",
                "question": "Bu ergen için en uygun plan hangisidir?",
                "options": [
                    {
                        "text": "Sakinleştiği için hemen taburcu etmek ve babaya polis bildirimi yapmasını ve çocuğu cezalandırmasını önermek",
                        "is_correct": False,
                        "scenario_update": "Erken taburcu edilen çocuk bağımlılık desteği almadan madde kullanmaya devam etti.",
                        "teaching_point": "Bu yaş grubunda madde kullanımı bir sağlık sorunudur; tedavi ve destek odaklı yaklaşım gerekir."
                    },
                    {
                        "text": "Uzun süreli bağımlılık tedavisi için oral naltrekson reçetesi yazıp aile hekimine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Naltrekson bu madde için etkili değildi; uzman yönlendirmesi yapılmadı.",
                        "teaching_point": "Bu madde grubunda özgül ilaç tedavisi yoktur; ergen bağımlılık merkezine yönlendirme yapılır."
                    },
                    {
                        "text": "Sıvı tedavisiyle CK ve kreatinini izleyerek gözlemlemek; ergenle yalnız görüşüp ÇEMATEM ve psikiyatri yönlendirmesi yapmak",
                        "is_correct": True,
                        "explanation": "Sıvı tedavisi kas hasarının böbreğe etkisini önler. Gizlilik gözetilen görüşme ergenin açık konuşmasını sağlar ve tedaviye yönlendirme başarısını artırır.",
                        "new_finding": "İV sıvıyla 12. saatte CK 1.100 U/L'ye düştü, kreatinin normale döndü. Ergen yalnız görüşmede iki aydır kullandığını anlattı. Psikiyatri konsültasyonu yapıldı ve ÇEMATEM randevusu verildi."
                    },
                    {
                        "text": "Profilaktik olarak levetirasetam başlamak ve nöbet olmasa da bir ay antiepileptik kullanması gerektiğini söylemek",
                        "is_correct": False,
                        "scenario_update": "Gereksiz antiepileptik başlandı; çocukta irritabilite arttı.",
                        "teaching_point": "Zehirlenmeye bağlı akut nöbetlerde uzun süreli antiepileptik gerekmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "S82",
        "category": "🌡️ Ateş & Döküntü / Enfeksiyon",
        "age": "13 Yaşında (45 kg)",
        "gender": "Erkek",
        "complaint": "Dört gündür yüksek ateş, şiddetli kas ağrısı, baş ağrısı ve bugün dişeti kanaması",
        "history": "Tokat'ın bir köyünde yaşıyor, haziran ayı. Babası anlatıyor: 'Bir hafta önce hayvanları otlatırken bacağına kene yapışmış, elimizle çekip çıkardık. Dört gündür ateşi 39-40, her yeri ağrıyor, kustu, karnı ağrıyor. Bugün dişlerini fırçalarken dişetinden kan geldi, kolunda morluklar çıktı.' Köyde son bir ayda iki kişi benzer şikâyetle hastaneye yatmış. Bilinen hastalığı yok.",
        "final_diagnosis": "Kırım-Kongo Kanamalı Ateşi (KKKA)",
        "disposition": "İzolasyon Önlemleriyle Çocuk Enfeksiyon Servisine Yatış, Destek Tedavisi, Kan Ürünü Desteği ve Bildirim",
        "case_pearl": "Türkiye'de özellikle Tokat, Sivas, Çorum, Yozgat ve Kastamonu'da ilkbahar ve yaz aylarında görülür. Kene tutunması veya hasta kanı ile temastan sonra 1-9 gün içinde ani ateş, miyalji, baş ağrısı ve gastrointestinal yakınmalar başlar; ardından kanama dönemi gelir. Trombositopeni, lökopeni, AST, ALT, LDH ve CK yüksekliği ve uzamış PT/aPTT tipiktir. Tanı Halk Sağlığı referans laboratuvarında PCR veya IgM ile konur, olgu bildirilir. Tedavi destekleyicidir: sıvı, kanama varsa trombosit ve taze donmuş plazma. Sağlık çalışanları kan ve vücut sıvılarına karşı temas ve damlacık önlemi almalıdır. Keneler çıplak elle değil, pensle deriye yakın tutularak çıkarılmalıdır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Enfeksiyon Kontrolü",
                "question": "Ateşli, kanaması olan ve kene tutunma öyküsü olan bu çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Tek kişilik odaya almak, eldiven, önlük, maske ve göz koruyucu kullanmak; vital bulgular, perfüzyon ve kanama odaklarını değerlendirmek",
                        "is_correct": True,
                        "explanation": "Bu tablo kan ve vücut sıvılarıyla insandan insana bulaşabilen bir enfeksiyonu düşündürür. Personel korunurken şok ve kanama bulguları hemen değerlendirilir.",
                        "new_finding": "Ateş 39.4°C, KTA 124/dk, KB 98/58 mmHg, SS 22/dk, SpO2 %98, KDZ 2 sn. Yüzde ve göğüste kızarıklık, konjonktivalarda hiperemi. Dişeti kenarında sızıntı tarzında kanama, kollarda ve enjeksiyon yerlerinde ekimozlar, gövdede peteşiler. Karında yaygın hassasiyet, hafif hepatomegali. Bilinç açık, ense sertliği yok."
                    },
                    {
                        "text": "Ateş düşürücü olarak hemen intramüsküler diklofenak yapmak ve kas ağrısı için ibuprofen başlamak",
                        "is_correct": False,
                        "scenario_update": "Kas içi enjeksiyon yerinde büyük hematom gelişti ve dişeti kanaması arttı.",
                        "teaching_point": "Kanama eğilimi olan hastada kas içi enjeksiyon ve trombosit işlevini bozan ilaçlar verilmez."
                    },
                    {
                        "text": "Standart önlemlerle bekleme salonunda değerlendirmek ve kene öyküsünü önemsiz bulup viral enfeksiyon kabul etmek",
                        "is_correct": False,
                        "scenario_update": "Hastanın kanı bulaşan bir hemşire temaslı kabul edildi ve profilaktik izleme alındı.",
                        "teaching_point": "Endemik bölgede kene öyküsü, ateş ve kanama birlikteliği yüksek bulaşıcılık riski taşır."
                    },
                    {
                        "text": "Ağır kanama riskine karşı hemen santral venöz kateter takmak ve arteriyel kan gazı için femoral ponksiyon yapmak",
                        "is_correct": False,
                        "scenario_update": "Femoral ponksiyon yerinden durdurulamayan kanama oldu.",
                        "teaching_point": "Kanama eğiliminde gereksiz invaziv girişimlerden kaçınılır; periferik damar yolu yeterlidir."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar Değerlendirmesi",
                "question": "Hangi laboratuvar bulgu kümesi bu tabloyu en iyi destekler?",
                "options": [
                    {
                        "text": "Lökositoz ve nötrofili, yüksek CRP, normal trombosit sayısı ve normal karaciğer enzimleri ile normal pıhtılaşma testleri",
                        "is_correct": False,
                        "scenario_update": "Hastanın sonuçları bu tabloyla uyumlu değildi.",
                        "teaching_point": "Bu bulgular bakteriyel enfeksiyonu düşündürür; bu hastalıkta lökopeni ve trombositopeni beklenir."
                    },
                    {
                        "text": "Trombositopeni, lökopeni, yüksek AST, ALT, LDH ve CK, uzamış PT ve aPTT ile birlikte düşük fibrinojen",
                        "is_correct": True,
                        "explanation": "Virüs endotel ve karaciğeri tutarak pıhtılaşma bozukluğu ve trombositopeni yapar. Kas enzimleri ve LDH yüksekliği yaygın doku tutulumunu gösterir.",
                        "new_finding": "Lökosit 1.900/mm³, Hb 13.2 g/dL, trombosit 32.000/mm³. AST 486 U/L, ALT 212 U/L, LDH 1.240 U/L, CK 1.680 U/L. PT 17 sn, INR 1.5, aPTT 52 sn, fibrinojen 140 mg/dL. Kreatinin 0.7 mg/dL. Kan örneği PCR için Halk Sağlığı referans laboratuvarına gönderildi."
                    },
                    {
                        "text": "İzole trombositopeni ile normal lökosit, karaciğer enzimleri ve pıhtılaşma testleri, periferik yaymada büyük trombositler",
                        "is_correct": False,
                        "scenario_update": "Hastanın sonuçları bu tabloyla uyumlu değildi.",
                        "teaching_point": "İzole trombositopeni ve büyük trombositler immün trombositopeniyi düşündürür; ateş ve organ tutulumu beklenmez."
                    },
                    {
                        "text": "Anemi, şistositler, trombositopeni ve yüksek kreatinin ile birlikte normal PT ve aPTT, yüksek LDH",
                        "is_correct": False,
                        "scenario_update": "Hastanın sonuçları bu tabloyla uyumlu değildi.",
                        "teaching_point": "Bu kümeler mikroanjiyopatik hemolitik anemiyi düşündürür."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik ve laboratuvar bulgularına göre en olası tanınız nedir?",
                "options": [
                    {"text": "Fulminan meningokoksemi", "is_correct": False, "scenario_update": "Lökopeni vardı ve tablo kene tutunmasından sonra, endemik bölgede ve mevsimde gelişmişti.", "teaching_point": "Meningokoksemide hızla yayılan purpura ve şok tablosu, sıklıkla lökositoz görülür."},
                    {"text": "Akut lösemi", "is_correct": False, "scenario_update": "Akut başlangıç, kene öyküsü ve belirgin enzim yüksekliği vardı.", "teaching_point": "Lösemide haftalar süren solukluk, kemik ağrısı ve periferik yaymada blastlar görülür."},
                    {"text": "Kırım-Kongo kanamalı ateşi", "is_correct": True, "explanation": "Endemik bölgede yaz aylarında kene tutunmasından sonra ani ateş, miyalji, kanama, lökopeni, trombositopeni, transaminaz ve CK yüksekliği ve pıhtılaşma bozukluğu Kırım-Kongo kanamalı ateşini gösterir.", "new_finding": "Tanı: Kırım-Kongo kanamalı ateşi. PCR pozitif geldi."},
                    {"text": "Tularemi (Francisella tularensis)", "is_correct": False, "scenario_update": "Bölgesel lenfadenopati veya ülserli lezyon yoktu, kanama ön plandaydı.", "teaching_point": "Tularemide ülseroglandüler veya orofaringeal tutulum ve lenfadenopati tipiktir."}
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Bakteriyel enfeksiyonu dışlamak için geniş spektrumlu antibiyotik ve yüksek doz kortikosteroid başlayıp genel serviste izlemek",
                        "is_correct": False,
                        "scenario_update": "Tedavi viral tabloyu etkilemedi; izolasyonsuz serviste bir refakatçi kanla temas etti.",
                        "teaching_point": "Tedavi destekleyicidir; izolasyon önlemleri her aşamada sürdürülür."
                    },
                    {
                        "text": "Trombosit sayısı düşük olduğu için kanama olmasa da her gün profilaktik trombosit ve plazma vermek",
                        "is_correct": False,
                        "scenario_update": "Gereksiz ürün kullanımı oldu; transfüzyon reaksiyonu gelişti.",
                        "teaching_point": "Kan ürünleri aktif kanama veya çok düşük değerlerde verilir; rutin profilaksi yapılmaz."
                    },
                    {
                        "text": "İzolasyonda sıvı desteği vermek, kanamaya göre trombosit ve taze donmuş plazma kullanmak, günlük tetkiklerle izleyip bildirmek",
                        "is_correct": True,
                        "explanation": "Destek tedavisi ve kanamanın yakın izlemi sağkalımı belirler. Bildirim ve temaslı izlemi bulaşın kontrolü için gereklidir.",
                        "new_finding": "Dişeti kanaması nedeniyle trombosit ve taze donmuş plazma verildi. Olgu bildirildi, temaslı aile bireyleri 14 gün ateş açısından izlendi. Yedinci günde trombosit 110.000/mm³'e yükseldi ve çocuk sekelsiz iyileşti."
                    },
                    {
                        "text": "Ateş ve kanama yatışana dek evde yatak istirahati önermek, ağrı için aspirin vermek ve günlük kan sayımı yaptırmak",
                        "is_correct": False,
                        "scenario_update": "Aspirin kanamayı artırdı; çocuk evde masif gastrointestinal kanamayla getirildi.",
                        "teaching_point": "Bu hastalar yatırılarak izlenir; aspirin ve NSAİİ kontrendikedir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S83",
        "category": "🦴 Kas-İskelet & Eklem / Ortopedik Aciller",
        "age": "9 Yaşında (28 kg)",
        "gender": "Kız",
        "complaint": "Üç haftadır gelip giden ateş, gece terlemesi ve bir haftadır sağ kalçada ağrı ve topallama",
        "history": "Van'da yaşıyor. Annesi anlatıyor: 'Üç haftadır akşamları ateşleniyor, gece yatağı sırılsıklam oluyor, sabah ateşi düşüyor, yine okula gidiyor. İştahı yok, iki kilo verdi. Bir haftadır sağ kalçası ağrıyor, topallıyor.' Evde inek ve koyun besleniyor. Aile taze, ev yapımı otlu peynir yiyor, süt kaynatılmadan içiliyor. Babasında da birkaç aydır eklem ağrısı ve halsizlik var. Öksürük, ishal, döküntü yok. Daha önce verilen bir haftalık amoksisilin işe yaramamış.",
        "final_diagnosis": "Bruselloz (Sağ Sakroiliit ile Osteoartiküler Tutulum)",
        "disposition": "Doksisiklin ve Rifampisin (6 Hafta) Başlanarak Çocuk Enfeksiyon Servisine Yatış, Bildirim ve Aile Taraması",
        "case_pearl": "Türkiye'de özellikle Doğu ve Güneydoğu Anadolu'da endemiktir. Pastörize edilmemiş süt ve taze peynir tüketimi en sık bulaş yoludur. Gelip giden ateş, gece terlemesi, kilo kaybı, artralji ve hepatosplenomegali tipiktir; çocuklarda en sık osteoartiküler tutulum sakroiliit ve büyük eklem artritidir. Tanıda Rose Bengal tarama testi, standart tüp aglütinasyonu (≥1/160) ve kan kültürü (laboratuvar uyarılmalı) kullanılır. Sekiz yaş ve üzerinde doksisiklin + rifampisin, sekiz yaş altında trimetoprim-sulfametoksazol + rifampisin 6 hafta verilir. Tek ilaç ve kısa tedavi nüks riskini artırır. Olgu bildirilir ve aynı ürünleri tüketen aile bireyleri taranır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Üç haftadır ateşi olan ve topallayan bu çocukta değerlendirmede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Topallama nedeniyle yalnızca kalça grafisi çekip kalça hastalığı olmadığında ateşi viral kabul etmek",
                        "is_correct": False,
                        "scenario_update": "Grafi normal geldi; sistemik bulgular değerlendirilmeden çocuk gönderildi.",
                        "teaching_point": "Uzun süreli ateş sistemik bir hastalığın işaretidir; ayrıntılı öykü ve muayene gerekir."
                    },
                    {
                        "text": "Beslenme ve hayvan teması öyküsünü derinleştirmek, lenf bezleri, karaciğer, dalak ve eklemleri sistemli muayene etmek",
                        "is_correct": True,
                        "explanation": "Uzamış ateşte maruziyet öyküsü ve organomegali, lenfadenopati, eklem bulguları ayırıcı tanıyı daraltır. Pastörize edilmemiş ürün tüketimi önemli bir ipucudur.",
                        "new_finding": "Ateş 38.6°C, KTA 112/dk, KB 102/62 mmHg. Soluk görünümlü. Karaciğer kosta altında 3 cm, dalak 2 cm ele geliyor. Servikal bölgede 1 cm'lik birkaç ağrısız lenf nodu. Sağ sakroiliak eklem üzerinde basmakla hassasiyet, FABER testi sağda ağrılı. Kalça hareketleri tam, diz ve ayak bileği normal. Döküntü yok."
                    },
                    {
                        "text": "Daha önce verilen antibiyotiğin yetersiz kaldığını düşünüp tetkik yapmadan amoksisilin-klavulanat başlamak",
                        "is_correct": False,
                        "scenario_update": "Ateş sürdü ve tanı haftalarca gecikti.",
                        "teaching_point": "Uzamış ateşte nedeni bulmadan yapılan ampirik tedavi tanıyı geciktirir."
                    },
                    {
                        "text": "Ateş, kilo kaybı ve gece terlemesi nedeniyle hemen kemik iliği aspirasyonu planlamak ve onkolojiye sevk etmek",
                        "is_correct": False,
                        "scenario_update": "Daha basit tetkiklerle tanı konabilecekken çocuk invaziv bir girişime maruz kaldı.",
                        "teaching_point": "Malignite akılda tutulur ama önce öykü, muayene ve temel tetkiklerle değerlendirme yapılır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Bu çocukta hangi tetkik grubu tanıya en hızlı ulaştırır?",
                "options": [
                    {
                        "text": "Tam kan sayımı, periferik yayma, karaciğer testleri, Rose Bengal ve tüp aglütinasyon testi; laboratuvarı uyararak kan kültürü göndermek",
                        "is_correct": True,
                        "explanation": "Serolojik testler endemik bölgede hızlı tanı sağlar. Kan kültürü uzun inkübasyon gerektirir ve laboratuvar çalışanları için enfeksiyon riski taşıdığı için önceden bildirilmelidir.",
                        "new_finding": "Lökosit 4.100/mm³ (lenfosit baskın), Hb 10.4 g/dL, trombosit 168.000/mm³, yaymada blast yok. AST 88 U/L, ALT 74 U/L, CRP 38 mg/L. Rose Bengal pozitif, standart tüp aglütinasyonu 1/640. Sakroiliak MR'da sağda kemik iliği ödemi ve eklem sıvısı."
                    },
                    {
                        "text": "Kalça eklemine aspirasyon yapıp eklem sıvısını kültüre göndermek ve sonuca göre tedaviye karar vermek",
                        "is_correct": False,
                        "scenario_update": "Kalça ekleminde sıvı yoktu; girişim gereksiz yere yapıldı.",
                        "teaching_point": "Ağrı sakroiliak kaynaklıydı; kalça hareketleri normaldi."
                    },
                    {
                        "text": "Tüberküloz için tüberkülin deri testi, açlık mide suyu ve toraks tomografisini sıralı olarak planlamak",
                        "is_correct": False,
                        "scenario_update": "Tetkikler negatif geldi ve tanı gecikti.",
                        "teaching_point": "Maruziyet öyküsü olan endemik bölgede daha olası tanılar öncelikle araştırılır."
                    },
                    {
                        "text": "Romatolojik hastalık için ANA, RF ve HLA-B27 istemek ve sonuçlar gelince ateş için yeniden değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Sonuçlar negatif geldi; enfeksiyon tedavisi gecikti.",
                        "teaching_point": "Ateş ve organomegali ile gelen artritte önce enfeksiyonlar dışlanmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "Septik artrit (kalça)", "is_correct": False, "scenario_update": "Kalça hareketleri tamdı ve tutulum sakroiliak eklemdeydi; tablo haftalardır sürüyordu.", "teaching_point": "Septik artritte akut başlangıç, eklem hareketinde belirgin kısıtlılık ve yüksek akut faz görülür."},
                    {"text": "Juvenil idiyopatik artrit (sistemik)", "is_correct": False, "scenario_update": "Somon renkli döküntü yoktu ve seroloji yüksek titrede pozitifti.", "teaching_point": "Sistemik JİA'da günde bir-iki kez yükselen ateş ve somon renkli döküntü tipiktir; enfeksiyonlar dışlandıktan sonra düşünülür."},
                    {"text": "Bruselloz (sakroiliit ile)", "is_correct": True, "explanation": "Endemik bölgede pastörize edilmemiş ürün tüketimi, gelip giden ateş, gece terlemesi, hepatosplenomegali, sakroiliit, Rose Bengal pozitifliği ve 1/640 aglütinasyon titresi brusellozu gösterir.", "new_finding": "Tanı: Bruselloz, sağ sakroiliit."},
                    {"text": "Akut lösemi", "is_correct": False, "scenario_update": "Periferik yaymada blast yoktu ve trombosit sayısı normaldi.", "teaching_point": "Kemik ağrısı ve organomegali lösemide de görülür; yayma ve kan sayımı ayrımda önemlidir."}
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Tek başına oral trimetoprim-sulfametoksazolü iki hafta vermek, ateş ve ağrı geçince kontrol tetkiki yapmadan tedaviyi kesmek",
                        "is_correct": False,
                        "scenario_update": "İki ay sonra ateş ve kalça ağrısı yeniden başladı.",
                        "teaching_point": "Tek ilaç ve kısa süreli tedavi nüks oranını belirgin artırır."
                    },
                    {
                        "text": "Doksisiklin ve rifampisini 6 hafta vermek; olguyu bildirmek, süt ve peyniri kaynatmayı anlatıp aileyi taramak",
                        "is_correct": True,
                        "explanation": "Sekiz yaş üstünde doksisiklin ve rifampisin kombinasyonu standart tedavidir; osteoartiküler tutulumda süre uzatılabilir. Aynı ürünü tüketen aile bireylerinde de enfeksiyon sıktır.",
                        "new_finding": "Tedavi başlandı, olgu bildirildi. Babada da tüp aglütinasyonu 1/320 pozitif çıktı ve tedavi başlandı. Çocuğun ateşi bir haftada düştü, kalça ağrısı dördüncü haftada geçti."
                    },
                    {
                        "text": "İntravenöz vankomisin ve seftriakson başlayıp sakroiliak ekleme cerrahi debridman planlamak",
                        "is_correct": False,
                        "scenario_update": "Seçilen antibiyotikler hücre içi bakteriye yeterli etki göstermedi; gereksiz cerrahi planlandı.",
                        "teaching_point": "Bu hücre içi etkene karşı hücre içine iyi geçen ilaç kombinasyonları kullanılır; cerrahi nadiren gerekir."
                    },
                    {
                        "text": "Eklem ağrısı için naproksen ve yüksek doz prednizolon başlayıp romatoloji polikliniğine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Kortikosteroid enfeksiyonu baskıladı ve tanıyı karmaşıklaştırdı; ateş sürdü.",
                        "teaching_point": "Enfeksiyöz artritte kortikosteroid kullanılmaz; etkene yönelik tedavi gerekir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S84",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "13 Yaşında (44 kg)",
        "gender": "Kız",
        "complaint": "Beden eğitimi dersinde koşarken aniden yere yığılma ve kısa süren kasılma",
        "history": "Öğretmeni getirdi. 'Koşu sırasında hiçbir uyarı vermeden yere düştü, kolları bacakları birkaç saniye kasıldı, morardı. Yaklaşık bir dakikada kendine geldi, bizi tanıdı.' Annesi telefonda: 'Geçen yıl yüzerken de bir kez bayılmıştı, havuz görevlisi çıkarmıştı. Ben de gençken birkaç kez bayıldım, bana epilepsi dediler, ilaç kullanıyorum. Dayısı 24 yaşında denizde boğularak öldü.' Son günlerde hastalık, ishal, kusma yok. İlaç kullanmıyor. Enerji içeceği tüketmemiş.",
        "final_diagnosis": "Konjenital Uzun QT Sendromu (Olası Tip 1, Eforla Tetiklenen Senkop)",
        "disposition": "Sürekli Monitörizasyon, Beta-Bloker Başlanması, QT Uzatan İlaçlardan Kaçınma ve Aile Taramasıyla Çocuk Kardiyoloji Servisine Yatış",
        "case_pearl": "Egzersiz, yüzme, ani ses veya korkuyla tetiklenen, öncesinde uyarı bulgusu olmayan senkop kardiyak kaynaklı kabul edilmelidir. Kısa süreli kasılmalar beyin perfüzyonunun azalmasıyla ortaya çıkar ve epilepsi ile karışabilir. Ailede genç yaşta açıklanamayan ölüm, boğulma veya 'epilepsi' tanısı uyarıcıdır. Her senkopta 12 derivasyonlu EKG çekilmeli, QTc elle (Bazett) hesaplanmalıdır; ergen kızda 460 ms üzeri uzundur. Hipokalemi, hipomagnezemi ve hipokalsemi düzeltilir. Tedavide beta-bloker (propranolol veya nadolol) verilir, QT uzatan ilaçlardan (makrolidler, ondansetron, bazı antihistaminikler, antipsikotikler) kaçınılır. Birinci derece akrabalara EKG taraması yapılır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme",
                "question": "Efor sırasında yere yığılan ve kendine gelmiş bu çocukta ilk değerlendirmeniz nedir?",
                "options": [
                    {
                        "text": "Kasılma olduğu için epileptik nöbet kabul edip annesinin kullandığı ilacın aynısını başlamak üzere nöroloji randevusu vermek",
                        "is_correct": False,
                        "scenario_update": "Kardiyak değerlendirme yapılmadan gönderilen çocuk bir ay sonra koşarken yeniden yığıldı.",
                        "teaching_point": "Efor sırasında prodromsuz yığılma ve kısa kasılma kardiyak senkopu düşündürür."
                    },
                    {
                        "text": "Monitöre bağlayıp 12 derivasyonlu EKG çekmek, kan şekeri, elektrolitler, kalsiyum ve magnezyumu göndermek",
                        "is_correct": True,
                        "explanation": "Eforla ortaya çıkan senkopta ilk ve en değerli tetkik EKG'dir. Elektrolit bozuklukları ritim bozukluğunu tetikleyebileceği için birlikte değerlendirilir.",
                        "new_finding": "KTA 68/dk, KB 108/66 mmHg, SpO2 %99, bilinç tam, nörolojik muayene normal. Kalp sesleri normal, üfürüm yok. Kan şekeri 98 mg/dL, K 4.1 mmol/L, Mg 2.0 mg/dL, iyonize Ca normal. EKG: sinüs ritmi, geniş tabanlı T dalgaları, elle hesaplanan QTc 520 ms.",
                        "image": "assets/images/ecg_long_qtc.png"
                    },
                    {
                        "text": "Vazovagal bayılma kabul edip tuzlu yiyecek ve bol sıvı önermek, yüzme ve koşuya devam etmesini söyleyerek taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk iki hafta sonra yüzme sırasında yeniden bilincini kaybetti.",
                        "teaching_point": "Vazovagal senkop eforla değil, uzun süre ayakta kalma veya ağrı ile, prodromla ortaya çıkar."
                    },
                    {
                        "text": "Acil beyin tomografisi ve EEG istemek, kardiyolojik değerlendirmeyi nöroloji sonuçlarından sonraya bırakmak",
                        "is_correct": False,
                        "scenario_update": "Tomografi ve EEG normal geldi; asıl neden gecikmeyle saptandı.",
                        "teaching_point": "Eforla ortaya çıkan olaylarda önce kardiyak nedenler dışlanır."
                    }
                ]
            },
            {
                "stage_title": "Acil Önlemler",
                "question": "EKG'de QTc 520 ms bulunan bu çocukta acilde hangi yaklaşım uygundur?",
                "options": [
                    {
                        "text": "Bulantısı için ondansetron, olası enfeksiyon için klaritromisin vermek ve sonuçları izlemek",
                        "is_correct": False,
                        "scenario_update": "İlaçlar sonrası monitörde polimorfik ventriküler taşikardi atakları görüldü.",
                        "teaching_point": "Ondansetron ve makrolidler QT'yi uzatır; bu hastalarda kaçınılmalıdır."
                    },
                    {
                        "text": "Sürekli ritim monitörü ve defibrilatörü hazır tutmak, QT uzatan ilaçlardan kaçınmak ve çocuk kardiyolojiye danışmak",
                        "is_correct": True,
                        "explanation": "Bu hastalarda torsades de pointes ani ölüme yol açabilir. Monitör ve defibrilatör hazır olmalı, ritmi bozabilecek ilaçlar verilmemelidir.",
                        "new_finding": "Monitörde ventriküler ektopi görülmedi. Çocuk kardiyoloji konsültasyonunda yatış ve beta-bloker kararı alındı. Ekokardiyografi normal."
                    },
                    {
                        "text": "Profilaktik amiodaron infüzyonu başlamak ve hemen elektrofizyolojik çalışma için başka merkeze sevk etmek",
                        "is_correct": False,
                        "scenario_update": "Amiodaron QT'yi daha da uzattı ve hipotansiyon yaptı.",
                        "teaching_point": "Amiodaron QT'yi uzatır; bu tabloda kullanılmaz."
                    },
                    {
                        "text": "Elektrolitler normal olduğu halde yüksek doz İV magnezyum ve potasyum yükleyerek QT aralığını kısaltmaya çalışmak",
                        "is_correct": False,
                        "scenario_update": "Normal düzeylere ek yükleme hiperkalemiye yol açtı.",
                        "teaching_point": "Elektrolitler düşükse düzeltilir; magnezyum torsades atağında verilir, profilaktik yükleme gerekmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bu çocuktaki olayların en olası nedeni nedir?",
                "options": [
                    {"text": "Hipertrofik kardiyomiyopati", "is_correct": False, "scenario_update": "Üfürüm yoktu ve ekokardiyografi normaldi.", "teaching_point": "Hipertrofik kardiyomiyopatide sol ventrikül hipertrofisi ve EKG'de yüksek voltajlar görülür."},
                    {"text": "Konjenital uzun QT sendromu", "is_correct": True, "explanation": "Egzersiz ve yüzme sırasında prodromsuz senkop, annede 'epilepsi' tanılı bayılmalar, dayıda genç yaşta boğulma, normal elektrolitlerle QTc 520 ms ve geniş tabanlı T dalgaları konjenital uzun QT sendromunu gösterir.", "new_finding": "Tanı: Konjenital uzun QT sendromu (olası tip 1). Annenin EKG'sinde de QTc 490 ms bulundu."},
                    {"text": "Jeneralize epilepsi", "is_correct": False, "scenario_update": "Olaylar eforla tetiklenmişti, kasılma kısa ve bilinç hızla düzelmişti.", "teaching_point": "Epileptik nöbette postiktal dönem uzundur ve olaylar eforla ilişkili değildir."},
                    {"text": "Wolff-Parkinson-White sendromu", "is_correct": False, "scenario_update": "EKG'de kısa PR ve delta dalgası yoktu.", "teaching_point": "WPW'de kısa PR aralığı ve delta dalgası görülür."}
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış Planı",
                "question": "Bu çocuk ve ailesi için en uygun plan hangisidir?",
                "options": [
                    {
                        "text": "Beta-bloker başlayıp yatırmak, QT uzatan ilaç listesi vermek, rekabetçi sporu kısıtlamak ve tüm birinci derece akrabalara EKG çekmek",
                        "is_correct": True,
                        "explanation": "Beta-bloker eforla tetiklenen aritmi riskini azaltır. Ailenin taranması hem annedeki yanlış tanıyı düzeltir hem de diğer risklileri ortaya çıkarır.",
                        "new_finding": "Nadolol başlandı, QT uzatan ilaç listesi verildi. Genetik testte KCNQ1 mutasyonu saptandı. Annenin epilepsi ilacı kesilip beta-bloker başlandı, kardeşin EKG'si normal bulundu."
                    },
                    {
                        "text": "Olay tekrarlamadıkça tedavi gerekmediğini söyleyip yıllık EKG kontrolüyle taburcu etmek ve spora devam ettirmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk bir yarışma sırasında ani kardiyak arrest geçirdi.",
                        "teaching_point": "Senkop geçirmiş bu hastalar yüksek risklidir ve tedavi gerektirir."
                    },
                    {
                        "text": "Tüm hastalarda zorunlu olduğu için hemen implante edilebilir defibrilatör takılmasını planlamak ve beta-bloker vermemek",
                        "is_correct": False,
                        "scenario_update": "İlk basamak tedavi atlandı ve gereksiz bir cerrahi girişim planlandı.",
                        "teaching_point": "İlk tedavi beta-blokerdir; defibrilatör tedaviye rağmen olay geçirenlerde ve çok yüksek riskte düşünülür."
                    },
                    {
                        "text": "Annesinin epilepsi ilacını çocuğa da başlamak ve kardiyolojik izlemi annenin nöroloji kontrollerine bağlamak",
                        "is_correct": False,
                        "scenario_update": "Epilepsi ilacı aritmiyi önlemedi; anne ve çocuk yanlış tedavi almaya devam etti.",
                        "teaching_point": "Annedeki olayların da kardiyak kaynaklı olabileceği akla gelmeli ve aile taranmalıdır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S85",
        "category": "🩸 Hematolojik & Onkolojik Aciller",
        "age": "4 Yaşında (16 kg)",
        "gender": "Erkek",
        "complaint": "Üç haftadır solukluk, halsizlik, bacak ağrısı nedeniyle yürümek istememe ve vücutta morluklar",
        "history": "Annesi anlatıyor: 'Üç haftadır çok soluk, hemen yoruluyor. Geceleri bacaklarım ağrıyor diye uyanıyor, son birkaç gündür yürümek istemiyor, kucak istiyor. Bacaklarında ve sırtında nedensiz morluklar çıktı. Arada ateşlendi, doktor büyüme ağrısı dedi, ibuprofen verdik.' Burun kanaması iki kez olmuş. İştahı azalmış. Travma öyküsü yok. Ailede kan hastalığı yok.",
        "final_diagnosis": "Akut Lenfoblastik Lösemi (Hiperlökositoz ve Tümör Lizis Riski)",
        "disposition": "Tümör Lizisi Önlemleri (Hiperhidrasyon, Allopürinol), Gerekli Kan Ürünleri ve Tanısal Kemik İliği İncelemesi İçin Çocuk Hematoloji-Onkoloji Servisine Yatış",
        "case_pearl": "Solukluk, yorgunluk, kemik ağrısı (özellikle gece uyandıran), morluk, ateş, hepatosplenomegali ve lenfadenopati birlikteliği kemik iliği infiltrasyonunu düşündürür; iki veya üç hücre serisinin birlikte etkilenmesi uyarıcıdır. 'Büyüme ağrısı' gece ağrısı yapar ama sistemik bulgu ve laboratuvar bozukluğu olmaz. Tanı konmadan kortikosteroid verilmemelidir; hem tanıyı gizler hem tümör lizisini tetikler. Tümör lizisi için ürik asit, potasyum, fosfor, kalsiyum ve kreatinin ölçülür; potasyumsuz hiperhidrasyon ve allopürinol (veya yüksek riskte rasburikaz) başlanır. Hiperlökositozda eritrosit transfüzyonu yavaş ve dikkatli verilir. Sedasyon öncesi akciğer grafisiyle mediasten kitlesi dışlanır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Fizik Muayene",
                "question": "Solukluk, kemik ağrısı ve morlukları olan bu çocukta muayenede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Morlukları istismar bulgusu kabul edip ayrıntılı muayene yapmadan hemen sosyal hizmet ve adli bildirim sürecini başlatmak",
                        "is_correct": False,
                        "scenario_update": "Aile büyük travma yaşadı; altta yatan ciddi hastalık değerlendirmesi gecikti.",
                        "teaching_point": "Morluklarda istismar akılda tutulur, ancak önce kanama bozuklukları ve kemik iliği hastalıkları dışlanmalıdır."
                    },
                    {
                        "text": "Ağrıyı büyüme ağrısı kabul edip muayene etmeden kas gevşetici ve D vitamini önermek, bir ay sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Bir hafta sonra çocuk yüksek ateş ve yaygın kanama ile getirildi.",
                        "teaching_point": "Büyüme ağrısında solukluk, morluk, ateş ve yürümeyi reddetme olmaz; bu bulgular ileri değerlendirme gerektirir."
                    },
                    {
                        "text": "Vital bulgular ve perfüzyonu değerlendirmek; lenf bezleri, karaciğer, dalak, testisler, deri ve mukozalarda kanama bulgularını incelemek",
                        "is_correct": True,
                        "explanation": "Sistemik bulgularla gelen kemik ağrısında organomegali, lenfadenopati ve kanama bulguları kemik iliği tutulumunu düşündürür. Testis muayenesi infiltrasyon açısından önemlidir.",
                        "new_finding": "Ateş 38.2°C, KTA 136/dk, KB 98/60 mmHg, SS 26/dk, SpO2 %98. Belirgin soluk. Bacaklarda ve sırtta farklı evrelerde ekimozlar, gövdede peteşiler. Servikal ve aksiller bölgede 1-2 cm'lik, ağrısız, birbirine yapışık olmayan lenf nodları. Karaciğer 4 cm, dalak 5 cm ele geliyor. Tibialarda basmakla hassasiyet. Testisler normal."
                    },
                    {
                        "text": "Kemik ağrısı ve ateş nedeniyle osteomiyelit kabul edip hemen İV sefazolin başlamak ve ortopediye danışmak",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik tabloyu düzeltmedi; asıl tanı gecikti.",
                        "teaching_point": "Çok odaklı kemik ağrısı, organomegali ve kanama bulguları sistemik bir hastalığı düşündürür."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar Değerlendirmesi",
                "question": "Tam kan sayımında lökosit 86.000/mm³, Hb 6.1 g/dL, trombosit 14.000/mm³ bulundu. Sonraki adım nedir?",
                "options": [
                    {
                        "text": "Periferik yayma yapmak; ürik asit, potasyum, fosfor, kalsiyum, kreatinin ve LDH ile pıhtılaşma testleri ve akciğer grafisi istemek",
                        "is_correct": True,
                        "explanation": "Yayma tanıya yönlendirir. Yüksek hücre yükü tümör lizisi riski taşır; metabolik değerler başlangıçta bilinmelidir. Akciğer grafisi mediasten kitlesini dışlar.",
                        "new_finding": "Periferik yaymada lökositlerin %78'i blast (küçük-orta boy, dar sitoplazmalı). Ürik asit 9.8 mg/dL, K 4.9 mmol/L, fosfor 6.4 mg/dL, Ca 8.6 mg/dL, kreatinin 0.6 mg/dL, LDH 2.840 U/L. PT ve aPTT normal. Akciğer grafisinde mediasten genişlemesi yok."
                    },
                    {
                        "text": "Lökositozu ağır bakteriyel enfeksiyon kabul edip kan kültürü alıp geniş spektrumlu antibiyotik başlamak ve yaymayı ertelemek",
                        "is_correct": False,
                        "scenario_update": "Yayma geç yapıldı; tümör lizisi önlemleri saatlerce gecikti.",
                        "teaching_point": "Üç hücre serisinin birlikte bozulduğu tabloda yayma hemen yapılmalıdır."
                    },
                    {
                        "text": "Ağrısı ve ateşi için tanı konmadan yüksek doz İV metilprednizolon başlamak ve tetkikleri ertesi güne bırakmak",
                        "is_correct": False,
                        "scenario_update": "Kortikosteroid sonrası ürik asit ve potasyum hızla yükseldi; kemik iliği tanısı güçleşti.",
                        "teaching_point": "Tanı konmadan kortikosteroid verilmez; tümör lizisini tetikler ve tanıyı gizler."
                    },
                    {
                        "text": "Hemoglobini hızla yükseltmek için 20 mL/kg eritrosit süspansiyonunu bir saatte vermek ve sonra yaymaya bakmak",
                        "is_correct": False,
                        "scenario_update": "Hızlı transfüzyon sonrası kan viskozitesi arttı; çocukta baş ağrısı ve solunum sıkıntısı gelişti.",
                        "teaching_point": "Yüksek lökosit sayısında transfüzyon küçük hacimlerde ve yavaş verilir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {"text": "İmmün trombositopenik purpura", "is_correct": False, "scenario_update": "Anemi, lökositoz, blastlar ve organomegali vardı.", "teaching_point": "İTP'de yalnızca trombositopeni olur; çocuk iyi görünür ve organomegali yoktur."},
                    {"text": "Enfeksiyöz mononükleoz", "is_correct": False, "scenario_update": "Yaymada atipik lenfosit değil blastlar görüldü ve ağır trombositopeni vardı.", "teaching_point": "Mononükleozda atipik lenfositler, tonsillit ve lenfadenopati görülür; ağır sitopeni beklenmez."},
                    {"text": "Aplastik anemi", "is_correct": False, "scenario_update": "Lökosit sayısı düşük değil çok yüksekti ve organomegali vardı.", "teaching_point": "Aplastik anemide pansitopeni olur, organomegali ve lenfadenopati beklenmez."},
                    {"text": "Akut lenfoblastik lösemi", "is_correct": True, "explanation": "Solukluk, kemik ağrısı, kanama bulguları, hepatosplenomegali, lenfadenopati, anemi, trombositopeni, hiperlökositoz ve periferik yaymada blastlar akut lenfoblastik lösemiyi gösterir.", "new_finding": "Tanı: Akut lenfoblastik lösemi (kemik iliği ve akım sitometrisiyle doğrulandı, prekürsör B hücreli)."}
                ]
            },
            {
                "stage_title": "Acil Tedavi ve Yatış",
                "question": "Bu çocuk için en uygun acil yönetim hangisidir?",
                "options": [
                    {
                        "text": "Potasyum içeren idame sıvısını standart hızda başlatmak ve hiperkalemiyi önlemek için yalnızca kalsiyum glukonat vermek",
                        "is_correct": False,
                        "scenario_update": "Sıvıdaki potasyum ve yetersiz hidrasyonla potasyum 6.4 mmol/L'ye yükseldi.",
                        "teaching_point": "Tümör lizisi riskinde potasyumsuz hiperhidrasyon gerekir."
                    },
                    {
                        "text": "Potasyumsuz sıvıyla iki katı idame hızında hidrasyon ve allopürinol başlamak; trombosit vermek, İV antibiyotikle onkolojiye yatırmak",
                        "is_correct": True,
                        "explanation": "Hiperhidrasyon ve allopürinol ürik asit nefropatisini önler. Ateşli ve sitopenik çocukta ampirik antibiyotik başlanır, kanama riskine karşı trombosit verilir.",
                        "new_finding": "Hiperhidrasyon, allopürinol, trombosit süspansiyonu ve sefepim başlandı. Hematoloji-onkoloji servisine yatırıldı; ertesi gün kemik iliği aspirasyonu yapıldı ve tedavi protokolüne başlandı. Tümör lizisi gelişmedi."
                    },
                    {
                        "text": "Ateşi ve kemik ağrısı için ibuprofen vermek ve ayaktan hematoloji polikliniğine bir hafta içinde randevu vermek",
                        "is_correct": False,
                        "scenario_update": "İbuprofen kanamayı artırdı; evde akut böbrek hasarı ve tümör lizisi gelişti.",
                        "teaching_point": "Trombositopenide NSAİİ verilmez; hiperlökositozlu çocuk hemen yatırılmalıdır."
                    },
                    {
                        "text": "Sedasyonla acil kemik iliği aspirasyonu yapmak ve sonuç gelene kadar tümör lizisi önlemlerini beklemek",
                        "is_correct": False,
                        "scenario_update": "Önlemlerin gecikmesiyle ürik asit 13 mg/dL'ye ve kreatinin 1.4 mg/dL'ye yükseldi.",
                        "teaching_point": "Tümör lizisi önlemleri tanısal girişimden önce başlatılır."
                    }
                ]
            }
        ]
    }
]
