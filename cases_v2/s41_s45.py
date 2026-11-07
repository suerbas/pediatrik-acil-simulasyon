# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - S41-S45 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "S41",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "2.5 Yaşında (12 kg)",
        "gender": "Erkek",
        "complaint": "Sabah uyandırılmakta zorlanılan, gevşek ve terli çocuk; dünden beri kusma",
        "history": "Annesi anlatıyor: 'Dün öğleden sonra ateşsiz kusmaya başladı, akşam yemeğini hiç yemedi, üç kez kustu. Gece su içip uyudu. Sabah uyandırmaya çalıştım, gözlerini açıp tekrar kapattı, çok terliydi, bana tepki vermedi.' Ateş, ishal, ilaç veya zehirli madde teması yok. Benzer bir atak bir yıl önce gastroenterit sırasında 'şekeri düşmüş' denilerek serum verilip taburcu edilmiş, ileri tetkik yapılmamış. Zayıf yapılı, 12 kg (3. persentil). Gelişimi yaşıtlarıyla uyumlu.",
        "final_diagnosis": "Ketotik Hipoglisemi (Açlık ve Kusmayla Tetiklenen)",
        "disposition": "Dekstrozlu İntravenöz Sıvı ile Sarı Alanda İzlem ve Hastalık Günü Planıyla Çocuk Endokrinoloji Takibine Taburculuk",
        "case_pearl": "Bilinç değişikliği olan her çocukta parmak ucu kan şekeri ölçülmelidir. Hipoglisemi anında 'kritik örnek' (glukoz, beta-hidroksibutirat, insülin, C-peptid, kortizol, büyüme hormonu, laktat, amonyak, serbest yağ asidi, açil-karnitin profili, idrar ketonu) alınması nedeni bulmayı sağlar. Ardından %10 dekstroz 2 mL/kg IV verilir. Ketotik hipoglisemi zayıf yapılı küçük çocuklarda açlık ve hastalıkla ortaya çıkan, dışlama ile konan bir tanıdır. Ketonların düşük olması yağ asidi oksidasyon kusuru veya hiperinsülinizmi düşündürür.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Stabilizasyon",
                "question": "Uyandırılmakta zorlanan bu çocukta ilk dakikalardaki yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Bilinç bozukluğu nedeniyle kafa içi bir olayı dışlamak için hastayı hemen acil kontrastsız beyin tomografisine göndermek ve sonuca göre karar vermek",
                        "is_correct": False,
                        "scenario_update": "Tomografiye gidiş sırasında çocuk kısa bir jeneralize nöbet geçirdi; tomografi normal geldi, ölçülen kan şekeri 32 mg/dL idi.",
                        "teaching_point": "Bilinç değişikliğinde görüntülemeden önce havayolu, solunum, dolaşım ve parmak ucu glukozu değerlendirilmelidir."
                    },
                    {
                        "text": "Ateşsiz bilinç bozukluğunda menenjit ve ensefaliti dışlamak için tetkik beklemeden lomber ponksiyon yapmak ve ampirik antibiyotik ile asiklovir başlamak",
                        "is_correct": False,
                        "scenario_update": "Ponksiyon girişimi sırasında çocuk hipoglisemik kaldı ve terlemesi arttı; BOS normal geldi.",
                        "teaching_point": "Kolayca düzeltilebilir metabolik nedenler dışlanmadan invaziv girişime geçilmemelidir."
                    },
                    {
                        "text": "Havayolu, solunum ve dolaşımı değerlendirip damar yolu açmak, parmak ucu glukozunu hemen ölçmek ve kan örneklerini tedaviden önce ayırmayı planlamak",
                        "is_correct": True,
                        "explanation": "Bilinç değişikliğinde ABC ile birlikte glukoz ölçümü ilk dakikalarda yapılmalıdır. Düşük bulunursa düzeltmeden hemen önce alınan örnek nedeni aydınlatır.",
                        "new_finding": "Vital Bulgular: Ateş 36.6°C, KTA 138/dk, SS 26/dk, SpO2 %98, TA 92/58 mmHg, KDZ 2 sn. AVPU: Ağrıya yanıt veriyor. Pupiller izokorik, ışık refleksi var, ense sertliği yok, lateralizan bulgu yok. Ciltte terleme, mukozalar kuru. Parmak ucu glukoz: 36 mg/dL."
                    },
                    {
                        "text": "Çocuğu yan yatırıp oksijen vermek, ailenin anlattığı kusmayı izlemek ve laboratuvar sonuçları gelene kadar herhangi bir tedavi vermeden gözlemde tutmak",
                        "is_correct": False,
                        "scenario_update": "Bir saatlik beklemede bilinç daha da kötüleşti ve çocuk nöbet geçirdi.",
                        "teaching_point": "Ağır hipoglisemi dakikalar içinde düzeltilmesi gereken bir acildir; sonuç beklemek nörolojik hasar riskini artırır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik ve Acil Tedavi",
                "question": "Parmak ucu glukozu 36 mg/dL. Hangi yaklaşım en doğrudur?",
                "options": [
                    {
                        "text": "Damar yolundan hemen %50 dekstroz 1 mL/kg puşe yapmak, glukoz yükseldiğinde ileri tetkik gerekmediğini kabul edip örnek almamak",
                        "is_correct": False,
                        "scenario_update": "Glukoz yükseldi ancak periferik damar yolunda flebit gelişti; neden araştırılacak örnek kaybedildi.",
                        "teaching_point": "Çocuklarda yüksek konsantrasyonlu dekstroz hiperozmolar olup damar hasarı yapar; %10 dekstroz 2 mL/kg tercih edilir ve kritik örnek atlanmamalıdır."
                    },
                    {
                        "text": "Kan şekerini yükseltmek için önce intramüsküler glukagon 0.5 mg uygulamak, ardından damar yolu açılınca serum fizyolojik infüzyonuyla izlemek",
                        "is_correct": False,
                        "scenario_update": "Glukagona rağmen glukoz 15 dakika sonra 40 mg/dL'de kaldı; damar yolu zaten açıktı ve zaman kaybedildi.",
                        "teaching_point": "Glukagon glikojen deposu dolu hastada etkilidir; uzamış açlık ve kusmada depolar boş olabilir. Damar yolu varken ilk tedavi IV dekstrozdur."
                    },
                    {
                        "text": "Kritik örneği ayırıp idrar ketonuna bakmak, ardından %10 dekstroz 2 mL/kg IV vermek ve dekstrozlu idame sıvısını başlatarak glukozu sık izlemek",
                        "is_correct": True,
                        "explanation": "Hipoglisemi anındaki örnekte insülin, keton ve karşı düzenleyici hormonlar nedeni ayırır. %10 dekstroz bolusu güvenli ve etkilidir; ardından dekstrozlu idame sıvısı tekrarı önler.",
                        "new_finding": "Kritik örnek: glukoz 34 mg/dL, beta-hidroksibutirat 4.6 mmol/L, insülin <2 µIU/mL, C-peptid baskılı, kortizol 26 µg/dL, büyüme hormonu 11 ng/mL, laktat 1.3 mmol/L, amonyak 38 µg/dL. İdrar ketonu +++. Bolus sonrası glukoz 118 mg/dL, çocuk gözlerini açıp annesini tanıdı. Kan gazında hafif metabolik asidoz (pH 7.32, HCO3 17 mmol/L)."
                    },
                    {
                        "text": "Çocuk biraz uyandığı için ağızdan şekerli meyve suyu içirmeye çalışmak, kusarsa damar yolundan dekstrozsuz serum fizyolojik başlamak",
                        "is_correct": False,
                        "scenario_update": "Uykulu çocuk sıvıyı öksürerek aspire etme riski taşıdı ve kustu; dekstrozsuz sıvıyla glukoz yeniden düştü.",
                        "teaching_point": "Bilinci bozuk çocuğa ağızdan sıvı verilmez; ağır hipoglisemide IV dekstroz ve ardından dekstrozlu idame gerekir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Kritik örnek sonuçlarına göre en olası tanınız nedir?",
                "options": [
                    {
                        "text": "Konjenital hiperinsülinizm",
                        "is_correct": False,
                        "scenario_update": "Hipoglisemi anında insülin ve C-peptid baskılıydı, ketonlar belirgin yüksekti.",
                        "teaching_point": "Hiperinsülinizmde insülin uygunsuz şekilde ölçülebilir ve ketonlar baskılıdır."
                    },
                    {
                        "text": "Orta zincirli açil-KoA dehidrogenaz eksikliği",
                        "is_correct": False,
                        "scenario_update": "Beta-hidroksibutirat 4.6 mmol/L ile yüksekti; açil-karnitin profili sonradan normal geldi.",
                        "teaching_point": "Yağ asidi oksidasyon kusurlarında hipoglisemi hipoketotiktir."
                    },
                    {
                        "text": "Ketotik hipoglisemi",
                        "is_correct": True,
                        "explanation": "Açlık ve kusma sırasında gelişen, ketonların yüksek, insülinin baskılı, kortizol ve büyüme hormonunun yeterli olduğu hipoglisemi, zayıf yapılı küçük çocukta ketotik hipoglisemiyi düşündürür.",
                        "new_finding": "Tanı: Ketotik hipoglisemi."
                    },
                    {
                        "text": "Primer adrenal yetmezlik",
                        "is_correct": False,
                        "scenario_update": "Hipoglisemi anında kortizol 26 µg/dL ile yeterliydi, sodyum ve potasyum normaldi.",
                        "teaching_point": "Adrenal yetmezlikte stres anında kortizol düşüktür; hiponatremi ve hiperkalemi eşlik edebilir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Glukozu düzelen bu çocuk için en uygun izlem ve taburculuk planı hangisidir?",
                "options": [
                    {
                        "text": "Bolus sonrası glukoz normale döndüğü ve çocuk uyandığı için damar yolunu çıkarıp yarım saat sonra ek izlem yapmadan taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Evde kusma sürdü; dört saat sonra çocuk yeniden uykulu halde getirildi, glukoz 41 mg/dL.",
                        "teaching_point": "Ağızdan yeterli alım sağlanana ve glukoz dekstrozsuz dönemde stabil kalana dek dekstrozlu sıvı ve izlem sürdürülmelidir."
                    },
                    {
                        "text": "Dekstrozlu idame sıvısıyla ağızdan beslenme ve keton temizlenene dek izlemek; hastalık günlerinde sık karbonhidrat ve gece atıştırmalığı planıyla taburcu etmek",
                        "is_correct": True,
                        "explanation": "Tedavi açlığı önlemeye dayanır: hastalık sırasında sık karbonhidratlı öğün, uzun açlıktan kaçınma ve evde idrar keton izlemi. Kusma ağızdan alımı engellerse erken başvuru gerekir. Tekrarlayan ataklar endokrinoloji tarafından izlenir.",
                        "new_finding": "On iki saat dekstrozlu sıvı sonrası çocuk yemek yedi, keton temizlendi, açlıkta glukoz 82 mg/dL. Aileye yazılı hastalık günü planı verildi ve endokrinoloji poliklinik randevusu ayarlandı."
                    },
                    {
                        "text": "Tekrarlayan hipoglisemi nedeniyle uzun süreli oral diazoksit başlamak ve glukozu evde günde dört kez ölçecek şekilde aileyi eğitip taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Diazoksit sıvı tutulumu ve kıllanma yaptı; insülin zaten baskılı olduğu için hiçbir yararı olmadı.",
                        "teaching_point": "Diazoksit hiperinsülinizmde kullanılır; insülinin baskılı olduğu bu tabloda endikasyonu yoktur."
                    },
                    {
                        "text": "Ataklar stres sırasında olduğu için idame hidrokortizon başlamak ve hastalık günlerinde dozu üç katına çıkaracak şekilde stres dozu eğitimi vermek",
                        "is_correct": False,
                        "scenario_update": "Kortizol yanıtı normal olan çocuğa gereksiz glukokortikoid başlandı; büyüme ve kemik sağlığı açısından risk oluştu.",
                        "teaching_point": "Hipoglisemi anında kortizol yeterliyse adrenal yetmezlik yoktur ve steroid tedavisi gerekmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "S42",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "9 Yaşında (30 kg)",
        "gender": "Kız",
        "complaint": "Ormandan toplanan mantarlarla hazırlanan yemekten saatler sonra başlayan şiddetli kusma, sulu ishal ve karın krampları",
        "history": "Babası anlatıyor: 'Dün akşam saat 19.00'da köyde ormandan topladığımız mantarları kavurup yedik. Gece 05.00 gibi kızım kusmaya başladı, sonra su gibi ishal oldu. Annesi de az yemişti, onda da ishal başladı.' Yemekten hemen sonra hiçbir yakınması olmamış. Şu ana dek sekiz kez kusmuş, on kez sulu ishal olmuş, kan yok. Ateş yok. Daha önce sağlıklı. Bir kısım çiğ mantar poşette getirilmiş.",
        "final_diagnosis": "Geç Başlangıçlı (Amatoksin İçeren) Mantar Zehirlenmesi",
        "disposition": "Agresif Sıvı, Tekrarlayan Doz Aktif Kömür ve Silibinin Tedavisiyle Çocuk Yoğun Bakım/Gastroenteroloji Yatışı ve Transplant Merkezinin Bilgilendirilmesi",
        "case_pearl": "Mantar yeme sonrası ilk 6 saatte başlayan gastrointestinal yakınmalar genellikle zararsız türlere bağlıdır. 6 saatten sonra başlayan şiddetli kusma-ishal ise aksi kanıtlanana dek amatoksin zehirlenmesidir. Gastrointestinal yakınmaların 24-48. saatte azaldığı 'yalancı iyilik' dönemi hepatotoksisiteyi gizler. Tedavi: agresif sıvı, tekrarlayan doz aktif kömür, silibinin (yoksa yüksek doz penisilin G), N-asetilsistein, 12 saatte bir ALT, INR ve glukoz izlemi ve erken transplant konsültasyonu. Aynı yemeği yiyen herkes değerlendirilir; Ulusal Zehir Danışma Merkezi (114) aranır.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Mantar yedikten sonra kusma ve ishal ile gelen bu çocukta ilk değerlendirmede neye özellikle odaklanırsınız?",
                "options": [
                    {
                        "text": "Dehidratasyon derecesini ve perfüzyonu değerlendirip yemek ile yakınmaların başlaması arasındaki süreyi, yiyen diğer kişileri ve mantar örneğini kayıt altına almak",
                        "is_correct": True,
                        "explanation": "Yemek ile semptom başlangıcı arasındaki süre, mantar zehirlenmesinde riskin en önemli belirleyicisidir. Aynı yemeği yiyen herkes değerlendirilmeli, örnek saklanmalıdır.",
                        "new_finding": "Vital Bulgular: Ateş 36.9°C, KTA 136/dk, SS 24/dk, SpO2 %99, TA 94/56 mmHg, KDZ 3 sn. Mukozalar kuru, gözler çökük, göz yaşı azalmış, bilinç açık. Karında yaygın hafif hassasiyet, defans yok, karaciğer ele gelmiyor, sarılık yok. Semptomlar yemekten yaklaşık 10 saat sonra başlamış. Anne de benzer yakınmalarla erişkin acile yönlendirildi."
                    },
                    {
                        "text": "Akut gastroenterit tablosu olarak değerlendirip ağızdan rehidratasyon solüsyonu ve ondansetron vererek kusma durunca ev izlemi önermek",
                        "is_correct": False,
                        "scenario_update": "Çocuk taburcu edildi; 36 saat sonra ishal azalmışken sarılık, uykuya meyil ve burun kanaması ile geri getirildi.",
                        "teaching_point": "Yabani mantar sonrası gecikmiş gastrointestinal yakınmalar sıradan gastroenterit gibi yönetilmemelidir; gecikmiş karaciğer hasarı ilk gün belirgin değildir."
                    },
                    {
                        "text": "Toksini midede kalan mantardan uzaklaştırmak için önce ağızdan bol su içirip kusturmak ve ardından mide lavajı uygulamayı planlamak",
                        "is_correct": False,
                        "scenario_update": "Zaten sekiz kez kusan çocukta kusturma dehidratasyonu ağırlaştırdı; mide lavajında mantar parçası gelmedi.",
                        "teaching_point": "Saatler sonra başvuruda kusturma ve lavajın yararı yoktur, aspirasyon ve sıvı kaybı riskini artırır."
                    },
                    {
                        "text": "İshali kesmek için loperamid ve probiyotik başlamak, sıvı kaybını önlemek amacıyla katı gıdaya kısa süre ara verip hastayı gözlemde tutmak",
                        "is_correct": False,
                        "scenario_update": "Loperamid barsak geçişini yavaşlattı ve karın şişkinliği gelişti; toksin emilimi açısından risk arttı.",
                        "teaching_point": "Zehirlenmelerde antimotilite ajanları toksin klirensini azaltır; çocuklarda loperamid ayrıca ileus riski taşır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik ve İlk Tedavi Kararı",
                "question": "Yemekten 10 saat sonra başlayan yakınmaları olan bu çocukta hangi yaklaşım doğrudur?",
                "options": [
                    {
                        "text": "Yalnızca elektrolit, kan gazı ve böbrek fonksiyonu bakıp intravenöz sıvı başlamak; karaciğer testlerinin ve INR'nin ilk 24 saatte anlamlı olmayacağını düşünerek istememek",
                        "is_correct": False,
                        "scenario_update": "Sıvı tedavisi verildi; ertesi gün bakılan ALT 1840 U/L ve INR 2.4 çıktı, başlangıç değeri bilinmediği için seyir yorumlanamadı.",
                        "teaching_point": "Başlangıç ALT, INR ve glukoz değerleri seyrin izlenmesi ve transplant ölçütlerinin değerlendirilmesi için gereklidir."
                    },
                    {
                        "text": "IV sıvıyla rehidratasyon başlatıp ALT, AST, INR, glukoz, böbrek fonksiyonu ve kan gazını istemek; aktif kömür vermek ve zehir danışma merkezini aramak",
                        "is_correct": True,
                        "explanation": "Geç başlangıçlı mantar zehirlenmesinde agresif sıvı, karaciğer ve pıhtılaşma izlemi ve enterohepatik dolaşımı kesmek için aktif kömür tedavinin temelidir. Ulusal Zehir Danışma Merkezi (114) tür tanımlama ve tedavi için yardımcı olur.",
                        "new_finding": "ALT 92 U/L, AST 110 U/L, INR 1.2, glukoz 74 mg/dL, kreatinin 0.7 mg/dL, BUN 28 mg/dL, Na 134 mmol/L, K 3.3 mmol/L, pH 7.31, HCO3 16 mmol/L. 1 g/kg aktif kömür verildi, 20 mL/kg serum fizyolojik bolus ardından idame sıvısı başlandı. UZEM ile görüşüldü; mikolog örneği değerlendirmeye aldı."
                    },
                    {
                        "text": "Toksini kandan uzaklaştırmak amacıyla acil hemodiyaliz kateteri takıp diyalize başlamak, sıvıyı diyaliz ekibinin belirleyeceği şekilde ayarlamak",
                        "is_correct": False,
                        "scenario_update": "Kateter takılırken kanama oldu; diyaliz toksin düzeylerini anlamlı biçimde düşürmedi.",
                        "teaching_point": "Hemodiyalizin bu toksin için kanıtlanmış yararı yoktur; erken dönemde temel tedavi sıvı ve gastrointestinal dekontaminasyondur."
                    },
                    {
                        "text": "Karaciğer hasarını önlemek için yalnızca oral N-asetilsistein başlayıp hemogram ve CRP istemek, sonuçlar normalse ayaktan izlem planlamak",
                        "is_correct": False,
                        "scenario_update": "Hemogram ve CRP normal geldi; çocuk taburcu edilmek üzereyken hipotansiyon gelişti.",
                        "teaching_point": "Hemogram ve CRP karaciğer hasarını göstermez; bu tabloda yatış, sıvı ve yakın karaciğer izlemi gerekir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik tablo ve zamanlamaya göre en olası tanınız nedir?",
                "options": [
                    {
                        "text": "Erken başlangıçlı gastrointestinal mantar zehirlenmesi",
                        "is_correct": False,
                        "scenario_update": "Semptomlar 6 saatten sonra, yaklaşık 10. saatte başlamıştı.",
                        "teaching_point": "Zararsız türlere bağlı gastrointestinal tablo genellikle ilk 6 saatte başlar ve kendini sınırlar."
                    },
                    {
                        "text": "Stafilokoksik enterotoksin besin zehirlenmesi",
                        "is_correct": False,
                        "scenario_update": "Ateşsiz kusma vardı ancak belirgin sulu ishal, yabani mantar öyküsü ve gecikmiş başlangıç bu tanıyı desteklemiyordu.",
                        "teaching_point": "Enterotoksin zehirlenmesi 1-6 saatte ani kusmayla başlar ve 24 saatte geriler."
                    },
                    {
                        "text": "Geç başlangıçlı amatoksin içeren mantar zehirlenmesi",
                        "is_correct": True,
                        "explanation": "Yabani mantar sonrası 6 saati aşan gecikmeyle başlayan şiddetli kusma ve sulu ishal amatoksin zehirlenmesini düşündürür; hafif transaminaz artışı erken hepatotoksisitenin işaretidir.",
                        "new_finding": "Tanı: Geç başlangıçlı amatoksin zehirlenmesi."
                    },
                    {
                        "text": "Norovirüs akut gastroenteriti",
                        "is_correct": False,
                        "scenario_update": "Aile içi eş zamanlı tablo ortak yemekle ilişkiliydi ve transaminazlar yükselmeye başlamıştı.",
                        "teaching_point": "Viral gastroenterit tanısı ortak besin ve gecikmiş başlangıç varken dışlama tanısı olmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve İzlem Planı",
                "question": "Bu çocuk için en uygun tedavi ve izlem planı hangisidir?",
                "options": [
                    {
                        "text": "İkinci gün kusma ve ishal azalıp çocuk ağızdan beslenmeye başlayınca, transaminazlar yalnızca hafif yüksek olduğundan aile hekimi kontrolüyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Taburculuktan bir gün sonra ALT 3200 U/L, INR 3.1 ve hipoglisemiyle geri döndü.",
                        "teaching_point": "Gastrointestinal yakınmaların azaldığı dönem yalancı iyilik dönemidir; karaciğer hasarı 48-72. saatte zirve yapar."
                    },
                    {
                        "text": "Furosemid ve yüksek hacimli sıvıyla zorlu diürez uygulayıp toksinin idrarla atılmasını hızlandırmak, karaciğer testlerini günde bir kez izlemek",
                        "is_correct": False,
                        "scenario_update": "Zorlu diürez elektrolit bozukluğu ve hipokalemi yaptı; karaciğer testleri izlem aralığı uzun kaldı.",
                        "teaching_point": "Yeterli idrar akımı hedeflenir ancak furosemidle zorlu diürez önerilmez; karaciğer ve INR izlemi 12 saatte bir yapılmalıdır."
                    },
                    {
                        "text": "Yatırarak sıvıyı sürdürmek, tekrarlayan doz aktif kömür ve IV silibinin vermek; ALT, INR ve glukozu 12 saatte bir izleyip transplant merkezini erkenden bilgilendirmek",
                        "is_correct": True,
                        "explanation": "Silibinin hepatosit toksin alımını azaltır; yoksa yüksek doz penisilin G kullanılabilir. N-asetilsistein de eklenebilir. INR yükselişi, hipoglisemi ve ensefalopati transplant değerlendirmesi gerektirir.",
                        "new_finding": "Silibinin 20 mg/kg/gün IV, tekrarlayan doz aktif kömür ve N-asetilsistein başlandı. 48. saatte ALT 1240 U/L ile zirve yapıp INR 1.6'da kaldı, ensefalopati gelişmedi. Beşinci gün transaminazlar gerilemeye başladı."
                    },
                    {
                        "text": "Antidot olarak atropin infüzyonunu başlatıp sekresyonlar kuruyana dek titre etmek, kusma kontrol altına alınınca çocuk servisine yatırmak",
                        "is_correct": False,
                        "scenario_update": "Atropin taşikardi ve huzursuzluk yaptı; karaciğer hasarı üzerinde hiçbir etkisi olmadı.",
                        "teaching_point": "Atropin muskarinik belirtilerle seyreden türlerde kullanılır; bu tabloda hepatotoksisiteye yönelik tedavi gerekir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S43",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "5 Haftalık",
        "gender": "Erkek",
        "complaint": "On gündür her beslenme sonrası fışkırır tarzda safrasız kusma, sürekli açlık ve kilo kaybı",
        "history": "Annesi anlatıyor: 'İlk çocuğum. On gündür emdikten hemen sonra sütün hepsini fışkırtarak, metrelerce ileri kusuyor. Kusmukta yeşil yok, ekşimiş süt geliyor. Kustuktan hemen sonra yine iştahla emmek istiyor. Son bir haftadır bezleri hafifledi, daha az ıslatıyor.' Term doğmuş, doğum ağırlığı 3.4 kg. Ateş ve ishal yok. Tartı: 3.6 kg (bir hafta önce 3.9 kg).",
        "final_diagnosis": "İnfantil Hipertrofik Pilor Stenozu",
        "disposition": "Sarı Alanda Oral Alımın Kesilmesi, Sıvı-Elektrolit ve Alkaloz Düzeltilmesi Sonrası Elektif Piloromiyotomi İçin Çocuk Cerrahisine Yatış",
        "case_pearl": "2-8 haftalık, özellikle ilk çocuk erkek bebekte giderek artan fışkırır tarzda safrasız kusma ve kusma sonrası açlık tipiktir. Tekrarlayan mide asidi kaybı hipokloremik hipokalemik metabolik alkaloza yol açar. Tanıda ultrason ile kas kalınlığı ≥3-4 mm ve kanal uzunluğu ≥15-16 mm aranır. Piloromiyotomi acil değildir: alkaloz düzelmeden (HCO3 <30, Cl >100 mEq/L) anestezi verilmez, aksi halde postoperatif apne riski artar.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Hidrasyon",
                "question": "Fışkırır tarzda safrasız kusan ve kilo kaybeden bu 5 haftalık bebekte ilk değerlendirmede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Kusmanın sepsise bağlı olabileceğini düşünerek hidrasyonu değerlendirmeden lomber ponksiyon, kan ve idrar kültürü alıp ampirik antibiyotik başlamak",
                        "is_correct": False,
                        "scenario_update": "Ateşsiz, iştahlı bebeğe invaziv tetkikler yapıldı; dehidratasyonu ve karın bulguları değerlendirilmedi.",
                        "teaching_point": "İyi görünümlü, ateşsiz ve aç bebekte sepsis taraması ilk adım değildir; muayene obstrüksiyonu gösterebilir."
                    },
                    {
                        "text": "Dehidratasyon derecesini, perfüzyonu ve kan şekerini değerlendirmek; karında görülebilen peristaltik dalgaları ve beslenme sonrası epigastrik kitleyi aramak",
                        "is_correct": True,
                        "explanation": "Kusan küçük bebekte hidrasyon ve kan şekeri önceliklidir. Sol üstten sağa ilerleyen peristaltik dalgalar ve epigastriumda zeytin büyüklüğünde sert kitle mide çıkış obstrüksiyonunu düşündürür; kitle en iyi kusma sonrası, gevşemiş karında palpe edilir.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 152/dk, SS 34/dk, TA 82/48 mmHg, KDZ 3 sn, kapiller kan şekeri 74 mg/dL. Ön fontanel çökük, mukozalar kuru, deri turgoru azalmış. Beslenme sonrası epigastriumda soldan sağa ilerleyen peristaltik dalgalar; kusmadan sonra sağ rektus kenarında hareketli, sert, zeytin büyüklüğünde kitle palpe edildi. Sarılık yok."
                    },
                    {
                        "text": "Kusmayı reflüye bağlayıp anneye daha sık ve az miktarda emzirmesini, emzirme sonrası bebeği dik tutmasını önermek ve iki hafta sonra kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Bebek eve gönderilmek üzereyken muayenede belirgin dehidratasyon fark edildi.",
                        "teaching_point": "Fizyolojik reflü kilo kaybına ve dehidratasyona yol açmaz; ilerleyici fışkırır kusma obstrüksiyonu düşündürür."
                    },
                    {
                        "text": "İnek sütü alerjisi olasılığı nedeniyle annenin süt ürünlerini kesmesini önermek ve bebeğe aminoasit bazlı mamaya geçişi planlamak",
                        "is_correct": False,
                        "scenario_update": "Mamaya geçildi ancak bebek mamayı da fışkırtarak kustu; hidrasyonu değerlendirilmedi.",
                        "teaching_point": "Kanıt olmadan beslenmeyi değiştirmek altta yatan obstrüktif nedeni geciktirir."
                    }
                ]
            },
            {
                "stage_title": "Biyokimya ve Ultrasonografi",
                "question": "Dehidrate, epigastrik kitlesi olan bu bebekte hangi tetkikler öncelikli olarak istenmelidir?",
                "options": [
                    {
                        "text": "Yalnızca tam kan sayımı ve CRP istemek, normal gelirse ampirik proton pompası inhibitörü başlayıp bebeği gözlem odasında beslemek",
                        "is_correct": False,
                        "scenario_update": "Kan sayımı ve CRP normal geldi; beslenen bebek kusmaya devam etti ve alkaloz derinleşti.",
                        "teaching_point": "Bu tabloda elektrolit ve kan gazı temel tetkiklerdir; PPI obstrüksiyonu düzeltmez."
                    },
                    {
                        "text": "Kontrastlı üst gastrointestinal sistem grafisi çekip sonucu bekleyene kadar bebeği beslemeye devam etmek ve elektrolitleri ertesi gün istemek",
                        "is_correct": False,
                        "scenario_update": "Bebek baryumu kustu ve aspirasyon riski oluştu; elektrolit bozukluğu bir gün geç fark edildi.",
                        "teaching_point": "Ultrason tanıda ilk seçenektir; kontrastlı grafi ultrason tanısal değilse kullanılır."
                    },
                    {
                        "text": "Venöz kan gazı, sodyum, potasyum, klor, BUN-kreatinin ve kan şekeri istemek; mide çıkışını değerlendirmek için batın ultrasonografisi yapmak",
                        "is_correct": True,
                        "explanation": "Tekrarlayan asit kaybı hipokloremi, hipokalemi ve metabolik alkaloz yapar; düzeltilmesi cerrahi öncesi zorunludur. Ultrasonda kas kalınlığı ve kanal uzunluğu tanıyı koyar.",
                        "new_finding": "Venöz kan gazı: pH 7.54, pCO2 48 mmHg, HCO3 36 mmol/L. Na 132, K 3.1, Cl 86 mEq/L, BUN 36 mg/dL, kreatinin 0.4 mg/dL, glukoz 76 mg/dL. Ultrason: mide çıkış kanalında kas kalınlığı 4.3 mm, kanal uzunluğu 17 mm; gerçek zamanlı incelemede mide içeriği kanaldan geçmiyor.",
                        "image": "assets/images/usg_pyloric_stenosis.png",
                        "image_caption": "Batın Ultrasonografisi (Mide Çıkışı)"
                    },
                    {
                        "text": "Kafa içi basınç artışını dışlamak için transfontanel ultrason ve beyin tomografisi istemek, ardından metabolik tarama için amonyak ve laktat bakmak",
                        "is_correct": False,
                        "scenario_update": "Nörolojik tetkikler normal geldi; çökük fontaneli olan bebekte elektrolitler bakılmadan saatler geçti.",
                        "teaching_point": "Normal nörolojik muayene ve çökük fontanel kafa içi basınç artışını düşündürmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Safrasız fışkırır kusma, epigastrik zeytin benzeri kitle, hipokloremik hipokalemik metabolik alkaloz ve ultrasonda kalınlaşmış uzun mide çıkış kanalı olan bu bebekte tanı nedir?",
                "options": [
                    {
                        "text": "Gastroözofageal reflü hastalığı",
                        "is_correct": False,
                        "scenario_update": "Reflü kitle, belirgin metabolik alkaloz ve ultrasonda kalınlaşmış kanal yapmaz.",
                        "teaching_point": "Reflü hastalığında kusma daha az zorlu, kilo kaybı ve elektrolit bozukluğu nadirdir."
                    },
                    {
                        "text": "İnfantil hipertrofik pilor stenozu",
                        "is_correct": True,
                        "explanation": "Mide çıkış kanalında kas kalınlığının ≥3-4 mm ve uzunluğunun ≥15-16 mm olması, tipik klinik ve hipokloremik hipokalemik metabolik alkaloz tanıyı doğrular.",
                        "new_finding": "Tanı: İnfantil Hipertrofik Pilor Stenozu."
                    },
                    {
                        "text": "Duodenal atrezi",
                        "is_correct": False,
                        "scenario_update": "Duodenal atrezi doğumdan itibaren ve çoğunlukla safralı kusmayla başlar.",
                        "teaching_point": "Duodenal atrezide direkt grafide çift balon görünümü saptanır."
                    },
                    {
                        "text": "Tuz kaybettiren konjenital adrenal hiperplazi",
                        "is_correct": False,
                        "scenario_update": "Potasyum düşük ve alkaloz var; tuz kaybında hiperkalemi ve asidoz beklenir.",
                        "teaching_point": "Kusan bebekte hiperkalemi ve hiponatremi adrenal yetmezliği düşündürür."
                    }
                ]
            },
            {
                "stage_title": "Metabolik Düzeltme ve Cerrahi Zamanlaması",
                "question": "Bu bebeğin acil servis tedavisi ve cerrahi zamanlaması nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Oral alımı kesmek, 10-20 mL/kg serum fizyolojik bolus vermek, ardından dekstrozlu izotonik idame sıvısına idrar çıkışı sonrası potasyum eklemek; alkaloz düzelince ameliyat planlamak",
                        "is_correct": True,
                        "explanation": "Dehidratasyon izotonik bolusla düzeltilir; klor yerine konmadan alkaloz düzelmez. Potasyum idrar çıkışı sağlandıktan sonra eklenir. HCO3 <30 ve Cl >100 mEq/L olunca piloromiyotomi güvenle yapılır.",
                        "new_finding": "Bolus sonrası perfüzyon düzeldi, idrar çıkışı başladı; potasyumlu dekstrozlu izotonik sıvı sürdürüldü. 24 saatte Cl 104 mEq/L, K 4.0 mEq/L, HCO3 26 mmol/L oldu. Laparoskopik piloromiyotomi sonrası 6. saatte beslenme başlandı."
                    },
                    {
                        "text": "Hipokalemiyi hızla düzeltmek için potasyum klorürü intravenöz bolus olarak vermek ve alkaloz için asetazolamid başlayıp ertesi sabah ameliyata almak",
                        "is_correct": False,
                        "scenario_update": "Potasyum bolusu ciddi aritmi riski taşıdı ve uygulama durduruldu; asetazolamid sıvı açığını derinleştirdi.",
                        "teaching_point": "Potasyum asla bolus olarak verilmez; alkaloz klor ve sıvı replasmanıyla düzelir."
                    },
                    {
                        "text": "Obstrüksiyon nedeniyle bebeği hemen ameliyathaneye almak, sıvı ve elektrolit düzeltmesini anestezi sırasında ve postoperatif dönemde yapmak",
                        "is_correct": False,
                        "scenario_update": "Anestezist alkaloz düzelmeden ameliyata izin vermedi; postoperatif apne riski konusunda uyardı.",
                        "teaching_point": "Bu cerrahi acil değil elektiftir; önce metabolik denge sağlanır."
                    },
                    {
                        "text": "Ameliyattan kaçınmak için oral atropin tedavisi başlamak, sık ve az beslemeyle bebeği servise yatırıp kusma azalana kadar izlemek",
                        "is_correct": False,
                        "scenario_update": "Atropinle kusma kısmen azaldı ancak tedavi haftalar sürdü ve yan etkiler gelişti; aile cerrahiye yönlendirildi.",
                        "teaching_point": "Atropin bazı merkezlerde alternatif olsa da standart tedavi metabolik düzeltme sonrası piloromiyotomidir."
                    }
                ]
            }
        ]
    },
    {
        "id": "S44",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "14 Aylık",
        "gender": "Kız",
        "complaint": "İki gündür günde 12 kez sulu dışkılama, ağızdan verilen her şeyi kusma, uykuya meyil ve idrar yapmama",
        "history": "Ailesi anlatıyor: 'İki gündür su gibi kakası var, bu sabahtan beri bir kaşık su versem bile kusuyor. Son 12 saattir bezi hiç ıslanmadı. Çok uyuyor, ağlarken gözyaşı gelmiyor, bize eskisi gibi tepki vermiyor.' Kreşte benzer ishalli çocuklar var. Dışkıda kan yok. Bilinen hastalığı yok, aşıları tam (rotavirüs aşısı yapılmamış). Hastalık öncesi tartısı: 10 kg.",
        "final_diagnosis": "Akut Gastroenterite Bağlı Ağır Dehidratasyon ve Kompanse Hipovolemik Şok",
        "disposition": "Sarı Alanda İzotonik Sıvı Bolusu, Elektrolit ve Glukoz İzlemi, Defisit-İdame Tedavisi ve Erken Oral Geçiş ile Gözlem Yatışı",
        "case_pearl": "Uzamış kapiller dolum, taşikardi, zayıf periferik nabız, letarji ve oligüri ağır sıvı kaybını ve kompanse şoku gösterir; hipotansiyon geç bulgudur. Tedavi 20 mL/kg izotonik kristaloid bolusu ve her bolus sonrası yeniden değerlendirmedir. Kan şekeri mutlaka bakılır. Sonrasında dekstrozlu izotonik sıvıyla defisit ve idame verilir; hipotonik sıvı hiponatremi riskini artırır. Kusma kontrol altına alınınca ondansetron desteğiyle ORS'ye erken geçilir.",
        "steps": [
            {
                "stage_title": "Triyaj ve Acil Resüsitasyon",
                "question": "Letarjik, gözyaşı gelmeyen ve 12 saattir idrar yapmayan bu 14 aylık çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Perfüzyon bulgularını hızla değerlendirip damar yolu (gerekirse intraosseöz) açmak, kapiller kan şekeri bakmak ve 20 mL/kg izotonik kristaloidi 5-20 dakikada vermek",
                        "is_correct": True,
                        "explanation": "Uzamış kapiller dolum, taşikardi, zayıf nabız ve letarji dolaşım yetmezliğini gösterir; hızlı vasküler erişim ve izotonik bolus gerekir. Uzun süren kusmada hipoglisemi sık görülür ve atlanmamalıdır.",
                        "new_finding": "Vital Bulgular: Ateş 38.2°C, KTA 168/dk, SS 38/dk, TA 78/46 mmHg, SpO2 %97, KDZ 4 sn, periferik nabızlar zayıf. Letarjik, gözler çökük, mukozalar kuru, cilt turgoru 3 sn. Kapiller kan şekeri 64 mg/dL. 20 mL/kg serum fizyolojik 15 dakikada verildi; ardından KTA 138/dk, KDZ 2.5 sn, nabızlar güçlendi, çocuk gözlerini açıp ağladı. Hipoglisemi için 2 mL/kg %10 dekstroz verildi."
                    },
                    {
                        "text": "Kusmayı durdurmak için önce ağızdan çözünen ondansetron vermek, yarım saat sonra nazogastrik sonda takıp sürekli ORS infüzyonu başlatmak ve çocuğun yanıtını iki saat izlemek",
                        "is_correct": False,
                        "scenario_update": "Bu sürede taşikardi arttı ve kapiller dolum 5 saniyeye uzadı; dolaşım yetmezliği için intravenöz tedavi gecikti.",
                        "teaching_point": "Nazogastrik ORS orta dereceli kayıpta seçenektir; dolaşım yetmezliği bulgusu olan çocukta intravenöz bolus gerekir."
                    },
                    {
                        "text": "Ateş ve letarji nedeniyle önce lomber ponksiyon yapıp menenjiti dışlamak, ardından sıvı tedavisini beyin omurilik sıvısı sonucuna göre planlamak",
                        "is_correct": False,
                        "scenario_update": "Lomber ponksiyon hazırlığı sırasında çocuğun perfüzyonu kötüleşti; resüsitasyon gecikti.",
                        "teaching_point": "Hemodinamik olarak stabil olmayan çocukta önce dolaşım desteklenir; invaziv tanısal işlemler ertelenir."
                    },
                    {
                        "text": "Damar yolu açıp idame hızında %0.18 NaCl ve %5 dekstroz başlamak, çocuğun idrar yapmasını beklerken laboratuvar sonuçlarını istemek",
                        "is_correct": False,
                        "scenario_update": "İdame hızında hipotonik sıvı perfüzyonu düzeltmedi; çocuk daha da letarjikleşti.",
                        "teaching_point": "Şok tablosunda hızlı izotonik bolus gerekir; hipotonik sıvılar resüsitasyonda kullanılmaz."
                    }
                ]
            },
            {
                "stage_title": "Yeniden Değerlendirme ve Laboratuvar",
                "question": "İlk bolusa yanıt veren bu çocukta sonraki adım nedir?",
                "options": [
                    {
                        "text": "Çocuk uyandığı için laboratuvar istemeden hemen bardakla ORS vermeye başlamak ve kusmazsa iki saat sonra taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Çocuk ORS'yi kustu; elektrolit ve böbrek fonksiyonları bilinmeden taburculuk planlanmıştı.",
                        "teaching_point": "Şok tablosuyla gelen çocuk tek bolus sonrası taburcu edilmez; laboratuvar ve gözlem gerekir."
                    },
                    {
                        "text": "Karın ağrısı ve kusma nedeniyle invajinasyon ve cerrahi tabloları dışlamak için öncelikle kontrastlı batın tomografisi istemek",
                        "is_correct": False,
                        "scenario_update": "Karın muayenesi rahat olan çocuğa gereksiz tomografi istendi; elektrolit ve asit-baz durumu değerlendirilmedi.",
                        "teaching_point": "Rahat karın ve sulu ishalde görüntüleme gerekmez; öncelik metabolik değerlendirmedir."
                    },
                    {
                        "text": "Elektrolitler, BUN-kreatinin, venöz kan gazı ve kan şekeri bakmak; perfüzyonu ve bilinci yeniden değerlendirip gerekirse ikinci bolusu vermek",
                        "is_correct": True,
                        "explanation": "Ağır kayıpta sodyum bozuklukları, prerenal azotemi ve metabolik asidoz sıktır; sonuçlar sıvı türünü ve hızını belirler. Her bolustan sonra klinik yeniden değerlendirme yapılır.",
                        "new_finding": "Na 136 mEq/L, K 3.6 mEq/L, Cl 108 mEq/L, BUN 58 mg/dL, kreatinin 0.8 mg/dL, venöz pH 7.29, HCO3 15 mmol/L. Kontrol kan şekeri 108 mg/dL. Klinik yeniden değerlendirmede KDZ 2.5 sn sürdüğü için ikinci 10 mL/kg bolus verildi; sonrasında KDZ 2 sn."
                    },
                    {
                        "text": "Ateşli ishalin bakteriyel olabileceğini düşünüp gaita kültürü, kan kültürü ve CRP almak, sonuçları beklemeden ampirik intravenöz seftriakson başlayıp elektrolitleri ertesi güne bırakmak",
                        "is_correct": False,
                        "scenario_update": "Dışkıda kan olmayan, kreşte salgın öyküsü olan çocuğa gereksiz antibiyotik başlandı; elektrolitler bakılmadı.",
                        "teaching_point": "Sulu ishal çoğunlukla viraldir; antibiyotik kanlı ishal, sepsis bulgusu veya seçilmiş patojenlerde düşünülür."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Sulu ishal ve kusma sonrası letarji, uzamış kapiller dolum, zayıf nabız, oligüri ve bolusa yanıt veren bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Hemolitik üremik sendrom",
                        "is_correct": False,
                        "scenario_update": "Dışkıda kan yok; böbrek fonksiyon bozukluğu prerenal ve sıvıyla düzeliyor.",
                        "teaching_point": "Bu sendrom genellikle kanlı ishal sonrası anemi, trombositopeni ve böbrek hasarıyla seyreder."
                    },
                    {
                        "text": "Bakteriyel sepsise bağlı septik şok",
                        "is_correct": False,
                        "scenario_update": "Tablo belirgin sıvı kaybıyla açıklanıyor ve sıvıya hızla yanıt verdi; döküntü veya odak yok.",
                        "teaching_point": "Sıvı yanıtı sınırlı, ateşli ve toksik görünümlü çocukta septik şok düşünülür."
                    },
                    {
                        "text": "Akut gastroenterite bağlı ağır dehidratasyon ve kompanse hipovolemik şok",
                        "is_correct": True,
                        "explanation": "Sıvı kaybı öyküsü, letarji, uzamış kapiller dolum, zayıf nabız, oligüri ve izotonik bolusa hızlı yanıt hipovolemik nedenli kompanse şoku doğrular; kan basıncı henüz korunmuştur.",
                        "new_finding": "Tanı: Akut Gastroenterite Bağlı Ağır Dehidratasyon ve Kompanse Hipovolemik Şok."
                    },
                    {
                        "text": "Ağır diyabetik asidoz tablosu",
                        "is_correct": False,
                        "scenario_update": "Kan şekeri başlangıçta düşük; asidoz ishalle bikarbonat kaybına bağlı.",
                        "teaching_point": "Hiperglisemi ve ketonüri olmadan diyabete bağlı asidoz düşünülmez."
                    }
                ]
            },
            {
                "stage_title": "Defisit-İdame Tedavisi ve İzlem",
                "question": "Perfüzyonu düzelen bu çocuğun sonraki sıvı tedavisi ve izlemi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Ondansetron 0.15 mg/kg verip dekstrozlu izotonik sıvıyla defisit ve idameyi 24 saate yaymak, idrar çıkışını ve elektrolitleri izlemek ve kusma geçince ORS'ye geçmek",
                        "is_correct": True,
                        "explanation": "İzotonik ve dekstrozlu sıvı hiponatremi ve hipoglisemi riskini azaltır. Ondansetron kusmayı azaltarak oral rehidratasyona geçişi hızlandırır. İdrar çıkışı perfüzyonun en iyi göstergelerindendir.",
                        "new_finding": "Dekstrozlu izotonik sıvıya idrar çıkışı sonrası potasyum eklendi. Dördüncü saatte idrar çıkışı 1.8 mL/kg/saat oldu. Kusma durdu; altıncı saatte ORS ve ardından normal beslenme başlandı. 24 saat sonra Na 138 mEq/L, BUN 18 mg/dL idi."
                    },
                    {
                        "text": "Bikarbonat 1 mEq/kg vererek asidozu düzeltmek ve perfüzyon düzelmiş olsa bile toplam 60 mL/kg olana kadar serum fizyolojik bolusunu 20 mL/kg olarak tekrarlamaya devam etmek",
                        "is_correct": False,
                        "scenario_update": "Gereksiz boluslar sonrası göz kapaklarında ödem gelişti; bikarbonat sonrası potasyum düştü.",
                        "teaching_point": "Hafif metabolik asidoz sıvı ile düzelir; bolus yalnızca perfüzyon bozukluğu sürüyorsa tekrarlanır."
                    },
                    {
                        "text": "Elektrolit kaybını yerine koymak için idame hızında %0.18 NaCl ve %5 dekstroz vermek ve oral beslenmeyi ishal tamamen kesilene kadar ertelemek",
                        "is_correct": False,
                        "scenario_update": "Hipotonik sıvı sonrası sodyum 129 mEq/L'ye düştü; çocuk uzun süre aç kaldı.",
                        "teaching_point": "Hasta çocuklarda hipotonik idame sıvısı hiponatremi riski taşır; beslenme erken başlatılmalıdır."
                    },
                    {
                        "text": "İshali hızla azaltmak için oral loperamid başlamak, laktozsuz mamaya geçmek, intravenöz sıvıyı kesip çocuğu yeterli idrar yaptığında aynı gün taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Loperamid sonrası karında distansiyon ve uykuya meyil gelişti; laktozsuz mamanın gerekliliği yoktu.",
                        "teaching_point": "Antimotilite ajanlar küçük çocuklarda kontrendikedir; rutin laktozsuz beslenme önerilmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "S45",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "4 Yaşında (16 kg)",
        "gender": "Erkek",
        "complaint": "Bahçede bulunan bir şişeden içtikten sonra kusma, aşırı terleme, salya akması ve hırıltılı solunum",
        "history": "Annesi anlatıyor: 'Bir saat önce bahçede oynarken depodaki etiketsiz bir pet şişeden içmiş. Dedesi şişeye bahçe ağaçları için ilaç koymuş. Şişeyi yanımızda getirdik, keskin, sarımsak gibi bir kokusu var. Kustu, her yeri ter içinde, ağzından sürekli salya akıyor, nefesi hırıltılı.' Daha önce sağlıklı. Çocuğun kıyafetleri ve elleri sıvıyla ıslanmış.",
        "final_diagnosis": "Organofosfat (Kolinesteraz İnhibitörü Pestisit) Zehirlenmesi",
        "disposition": "Atropin ve Pralidoksim İnfüzyonuyla Çocuk Yoğun Bakım Ünitesine Yatış",
        "case_pearl": "Muskarinik bulgular salya, bronkore, bronkospazm, kusma, ishal, terleme, miyozis ve bradikardidir. Nikotinik bulgular fasikülasyon, kas güçsüzlüğü ve taşikardidir. Çocuklarda santral bulgular (letarji, nöbet) erişkinden daha belirgindir. Önce sağlık çalışanını koruyarak dekontaminasyon yapılır. Atropin 0.02-0.05 mg/kg IV verilir ve akciğer sekresyonları kuruyana dek 5 dakikada bir doz ikiye katlanır; hedef pupil genişlemesi değildir. Pralidoksim 25-50 mg/kg yükleme ardından infüzyon olarak verilir. Süksinilkolinden kaçınılır.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Stabilizasyon",
                "question": "Bu çocuğun acil serviste ilk değerlendirmesinde hangi yaklaşım doğrudur?",
                "options": [
                    {
                        "text": "Koruyucu eldiven ve önlükle ıslak kıyafetleri çıkarıp cildi su ve sabunla yıkamak; havayolu, sekresyonlar, solunum, nabız, pupiller ve kas seğirmesini hızla değerlendirmek",
                        "is_correct": True,
                        "explanation": "Cilt ve kıyafetle temas devam ettikçe emilim sürer ve sağlık çalışanı da etkilenebilir. Sekresyon yükü ve solunum durumu acil tedavi ihtiyacını belirler.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 82/dk, SS 36/dk, SpO2 %90 (oda havası), TA 88/50 mmHg. Bol salya ve ağızda köpüklü sekresyon. Bilateral yaygın raller ve ekspiratuvar hışıltı. Pupiller 1 mm, ışığa yanıt zayıf. Gövde ve kollarda belirgin terleme, baldırlarda kas seğirmeleri. Bir kez sulu ishal. AVPU: Sese yanıt veriyor, uykulu."
                    },
                    {
                        "text": "Hasta bir saat önce içtiği için toksini uzaklaştırmak amacıyla önce burundan mide sondası takıp bol sıvıyla mide lavajı yapmak, sonra muayeneye geçmek",
                        "is_correct": False,
                        "scenario_update": "Lavaj sırasında çocuk öğürüp aspirasyon yaptı ve satürasyonu %84'e düştü; ekipten bir hemşirede baş ağrısı ve bulantı başladı.",
                        "teaching_point": "Bilinci bozulmaya başlayan, bol sekresyonlu hastada lavaj aspirasyon riskini artırır; önce stabilizasyon ve cilt dekontaminasyonu yapılır."
                    },
                    {
                        "text": "Hışıltı ve satürasyon düşüklüğü nedeniyle hemen salbutamol nebülü ve oksijen başlamak, kıyafetleri ve cildi tedaviden sonra temizlemeyi planlamak",
                        "is_correct": False,
                        "scenario_update": "Salbutamol sekresyonları azaltmadı, satürasyon %88'de kaldı; ıslak kıyafetlerden emilim sürdü.",
                        "teaching_point": "Bu hışıltının nedeni bronkore ve bronkospazmdır; beta-agonist yetersiz kalır, dekontaminasyon ertelenmemelidir."
                    },
                    {
                        "text": "Bilinç bulanıklığı nedeniyle önce parmak ucu glukozu ve beyin tomografisi planlamak, vital bulgular stabil kaldığı sürece dekontaminasyonu ertelemek",
                        "is_correct": False,
                        "scenario_update": "Tomografi için beklerken çocuğun sekresyonları arttı ve solunum yetmezliğine ilerledi.",
                        "teaching_point": "Glukoz ölçülmeli ancak görüntüleme beklenmeden dekontaminasyon ve solunum desteği önceliklidir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik ve Destek Kararı",
                "question": "Oksijen başlandı, kıyafetler çıkarıldı. Bir sonraki tetkik ve destek adımınız ne olmalıdır?",
                "options": [
                    {
                        "text": "Tanıyı kesinleştirmek için kan kolinesteraz düzeyini istemek ve sonuç laboratuvardan gelinceye dek ilaç tedavisine başlamamak",
                        "is_correct": False,
                        "scenario_update": "Sonuç saatler sonra geldi; bu sürede çocuk solunum yetmezliğine girdi.",
                        "teaching_point": "Tedavi klinik tabloya göre hemen başlatılır; laboratuvar sonucu beklenmez."
                    },
                    {
                        "text": "Kan gazı, glukoz, elektrolitler ve EKG'yi alırken kolinesteraz düzeyini göndermek, beklemeden yüksek akım oksijen ve aspirasyonla sekresyonları temizlemek",
                        "is_correct": True,
                        "explanation": "Kolinesteraz düzeyi tanıyı destekler ve izlemde kullanılır ancak tedavi geciktirilmez. EKG'de bradikardi, QT uzaması ve aritmiler izlenmelidir.",
                        "new_finding": "Kapiller kan gazı: pH 7.26, pCO2 52 mmHg, HCO3 20 mmol/L, laktat 3.4 mmol/L. Glukoz 168 mg/dL, K 3.6 mmol/L. EKG: Sinüs ritmi 80/dk, QTc 470 ms. Plazma kolinesteraz düzeyi 720 U/L (normal 5300-12900 U/L)."
                    },
                    {
                        "text": "Sekresyonları azaltmak için furosemid 1 mg/kg IV vermek ve akciğer ödemini değerlendirmek için portabl akciğer grafisi istemek",
                        "is_correct": False,
                        "scenario_update": "Furosemid hipotansiyonu ağırlaştırdı; akciğer grafisinde yaygın infiltrasyon görüldü ama sekresyonlar azalmadı.",
                        "teaching_point": "Bu tablodaki akciğer sekresyonları kardiyojenik ödem değil bronkoredir; diüretik zararlıdır."
                    },
                    {
                        "text": "Ajitasyonu ve kas seğirmelerini kontrol altına almak için sedasyon amaçlı yüksek doz fenobarbital yüklemesi yapmak ve monitörize izlemek",
                        "is_correct": False,
                        "scenario_update": "Fenobarbital solunumu baskıladı ve pCO2 68 mmHg'ya yükseldi.",
                        "teaching_point": "Kas seğirmesi nikotinik etkidir, sedasyonla düzelmez; nöbet olursa benzodiazepin tercih edilir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Klinik ve laboratuvar bulgularına göre tanınız nedir?",
                "options": [
                    {
                        "text": "Organofosfat zehirlenmesi",
                        "is_correct": True,
                        "explanation": "Pestisit öyküsü, muskarinik (salya, bronkore, miyozis, terleme, bradikardi) ve nikotinik (fasikülasyon) bulgular ile çok düşük kolinesteraz organofosfat zehirlenmesini gösterir.",
                        "new_finding": "Tanı: Organofosfat zehirlenmesi."
                    },
                    {
                        "text": "Opioid zehirlenmesi",
                        "is_correct": False,
                        "scenario_update": "Miyozis vardı ancak bol sekresyon, terleme ve fasikülasyon opioidle açıklanamazdı.",
                        "teaching_point": "Opioid zehirlenmesinde miyozis ve solunum depresyonu olur, sekresyonlar ve terleme artmaz."
                    },
                    {
                        "text": "Nikotin likidi zehirlenmesi",
                        "is_correct": False,
                        "scenario_update": "Kolinesteraz belirgin düşüktü ve tabloya muskarinik bulgular hakimdi.",
                        "teaching_point": "Nikotin zehirlenmesinde kolinesteraz normaldir; erken kusma, taşikardi ve hipertansiyon belirgindir."
                    },
                    {
                        "text": "Klonidin zehirlenmesi",
                        "is_correct": False,
                        "scenario_update": "Bradikardi ve miyozis vardı ancak sekresyon artışı ve terleme klonidin tablosuna uymuyordu.",
                        "teaching_point": "Klonidin zehirlenmesinde miyozis, bradikardi ve letarji olur fakat ciltte terleme ve bronkore beklenmez."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış Planı",
                "question": "Bu çocuğun tedavisinde en doğru yaklaşım hangisidir?",
                "options": [
                    {
                        "text": "Atropini pupiller genişleyene kadar titre etmek, pupiller orta boya geldiğinde dozu sabit tutup pralidoksim gerekmeden izlemek",
                        "is_correct": False,
                        "scenario_update": "Pupiller genişledi ancak akciğer sekresyonları sürüyordu; kas güçsüzlüğü ilerledi ve solunum desteği gerekti.",
                        "teaching_point": "Atropin titrasyon hedefi akciğer sekresyonlarının kurumasıdır; pupil boyutu güvenilir değildir. Nikotinik etkiler için pralidoksim eklenir."
                    },
                    {
                        "text": "Atropin 0.02-0.05 mg/kg IV verip sekresyonlar kuruyana dek 5 dakikada bir dozu ikiye katlamak, pralidoksim yükleyip infüzyona geçmek ve yoğun bakıma yatırmak",
                        "is_correct": True,
                        "explanation": "Atropin muskarinik etkileri, pralidoksim nikotinik etkileri ve kas güçsüzlüğünü düzeltir. Entübasyon gerekirse süksinilkolinden kaçınılır. Ara sendrom riski nedeniyle yoğun bakım izlemi gerekir.",
                        "new_finding": "Üç doz atropin sonrası akciğerler temizlendi, SpO2 %97, KTA 118/dk. Pralidoksim 40 mg/kg yükleme ardından 15 mg/kg/saat infüzyon başlandı. Fasikülasyonlar azaldı, bilinç düzeldi. Çocuk yoğun bakıma devredildi."
                    },
                    {
                        "text": "Tek doz atropin 0.02 mg/kg verip kalp hızı yükseldiyse ek doz vermemek, sekresyonlar için aralıklı aspirasyonla çocuk servisinde izlemek",
                        "is_correct": False,
                        "scenario_update": "Tek doz sonrası sekresyonlar yeniden arttı ve servise çıktıktan iki saat sonra çocuk solunum yetmezliğine girdi.",
                        "teaching_point": "Ağır zehirlenmede çok sayıda ve artan dozda atropin gerekebilir; taşikardi tek başına atropin kontrendikasyonu değildir."
                    },
                    {
                        "text": "Solunum yükünü azaltmak için süksinilkolin ile hızlı ardışık entübasyon yapmak, ardından atropin ve pralidoksimi yoğun bakımda başlatmak",
                        "is_correct": False,
                        "scenario_update": "Süksinilkolin sonrası paralizi saatlerce uzadı; antidotların gecikmesi hipoksiyi derinleştirdi.",
                        "teaching_point": "Kolinesteraz inhibisyonunda süksinilkolin etkisi çok uzar; gerekirse rokuronyum kullanılır ve antidotlar hemen başlanır."
                    }
                ]
            }
        ]
    }
]
