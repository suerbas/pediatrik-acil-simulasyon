# -*- coding: utf-8 -*-
GREEN_CASES_PART2 = [{'id': 'G11',
  'category': '👶 Ağlayan, Emmeyen, Huzursuz Bebek',
  'age': '6 Haftalık',
  'gender': 'Erkek',
  'complaint': "Her akşamüstü saat 18:00'den sonra başlayan, saatlerce süren durdurulamayan şiddetli ağlama "
               'krizleri, bacaklarını karnına çekme ve yüzünde kızarma',
  'history': "Genç anne-baba 6 haftalık ilk bebeklerini akşam saat 20:30'da büyük bir panik içinde Yeşil "
             "Alana getiriyor: 'Doktor bey/hanım, bebeğimiz son 10 gündür her akşam aynı saatlerde aralıksız "
             'çığlık atarak ağlıyor! Ne kucağımıza alınca susuyor ne memeyi verince. Karnı taş gibi '
             'sertleşiyor, bacaklarını karnına çekiyor, ellerini yumruk yapıyor ve kıpkırmızı oluyor. Gazını '
             'çıkarmaya çalıştık ama hiç fayda etmedi. Acaba bir yeri mi kırıldı, bağırsakları mı '
             "düğümlendi? Ne olur yardım edin!' Anne bebeğin gündüzleri huzurlu uyuduğunu, yalnız anne sütü "
             'aldığını, kilo alımının çok iyi olduğunu (son ayda 900 gram almış), kusma, kanlı kaka veya '
             'ateşinin olmadığını belirtiyor.',
  'final_diagnosis': "İnfantil Kolik (Wessel '3'ler Kuralı' ile Uyumlu Paroksismal Aşırı Ağlama)",
  'disposition': "Yeşil Alanda Kapsamlı 'Tepeden Tırnağa' Muayene (Organik Patolojilerin Dışlanması), Aile "
                 'Eğitimi, 5S Yatıştırma Teknikleri ve Kırmızı Bayraklarla Taburculuk',
  'case_pearl': 'İnfantil kolik sağlıklı, büyüme-gelişmesi mükemmel süt çocuklarında yaşamın 2-3. haftasında '
                'başlayıp 3-4. ayda kendiliğinden sonlanan, genellikle akşam saatlerinde tekrarlayan '
                "paroksismal ağlama nöbetleridir (Wessel '3'ler Kuralı': Günde >3 saat, haftada >3 gün, en "
                'az 3 hafta süren sebepsiz ağlama). Acil hekiminin EN KRİTİK GÖREVİ bebeği tamamen soyup '
                'tepeden tırnağa muayene ederek ağlamaya yol açabilecek organik patolojileri dışlamaktır: 1) '
                'Korneal abrazyon (floresein boyama), 2) Parmak veya peniste saç-ip turnikesi, 3) İnkarsere '
                'inguinal fıtık / testis torsiyonu, 4) Akut otit, 5) İdrar yolu enfeksiyonu, 6) '
                'Non-aksidental travma. Muayenesi normal olan bebekte gereksiz lavman, batın grafisi, proton '
                'pompa inhibitörü veya antibiyotik uygulanmaz. Aileye durumun iyi huylu ve geçici olduğu '
                "anlatılmalı, tükenmişlik hissine karşı destek olunmalı ve 'Sarsılmış Bebek Sendromu'na "
                'karşı mutlaka uyarı yapılmalıdır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Durdurulamayan şiddetli akşam ağlama atakları ile getirilen altı haftalık bu '
                         'bebekte ilk klinik yaklaşımınız nasıl olmalıdır?',
             'options': [{'text': 'Genel görünümü iyi ve emmesi aktif olduğundan bebeği soymadan yalnızca '
                                  'karın oskültasyonu yapmak, gaz sancısı düşünerek acil serviste simetikon '
                                  'damla ve rektal gliserin fitil uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Bebek soyulmadan uygulanan rektal fitil ve gaz damlası '
                                             'ağlamayı durdurmadı; eksik muayene nedeniyle olası bir '
                                             'boğulmuş kasık fıtığı veya saç turnikesi riski gözden '
                                             'kaçırılmış oldu.',
                          'teaching_point': 'Huzursuz ve ağlayan süt çocuğu tamamen soyulup tepeden tırnağa '
                                            'muayene edilmeden asla semptomatik gaz tedavisi veya rektal '
                                            'girişim uygulanmamalıdır.'},
                         {'text': 'Bebeği tamamen soyarak yaşamsal bulguları ölçmek; kornea, kulak zarı, '
                                  'fontanel, ağız içi, kasıklar, skrotum, anal bölge ve tüm parmak '
                                  'boğumlarını sistematik biçimde muayene etmek',
                          'is_correct': True,
                          'explanation': 'Ağlayan süt çocuğunun acil servisteki değerlendirmesi gizli '
                                         'organik acilleri dışlamakla başlar. Bebek tamamen soyularak parmak '
                                         'boğumları, genital bölge, kasıklar, kornea ve fontanel dikkatle '
                                         'kontrol edilmelidir.',
                          'new_finding': 'Yaşamsal bulgular: Ateş 36.8°C, KTA 142/dk, SS 34/dk, SpO2 %99. Ön '
                                         'fontanel normal bombelikte, bilateral timpanik membranlar doğal, '
                                         'floresein ile korneal boyanma yok. El ve ayak parmaklarında veya '
                                         'peniste saç-ip dolanması saptanmadı. Bilateral inguinal herni yok, '
                                         'testisler skrotumda, normal boyutta ve ağrısız. Sakinleştiğinde '
                                         'batın yumuşak, kitle veya organomegali yok, anal fissür '
                                         'görülmedi.'},
                         {'text': 'Ağlama krizinin olası akut batın veya invajinasyon kaynaklı olabileceğini '
                                  'düşünerek fizik muayene öncesinde bebeği Sarı Alana devretmek ve acil '
                                  'batın ultrasonografisi için radyolojiye yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Yaşamsal bulguları stabil olan ve kusması bulunmayan bebek '
                                             'Sarı Alana alındı; ancak yapılan ultrasonografide hiçbir '
                                             'patoloji saptanmadı ve ailenin anksiyetesi belirgin şekilde '
                                             'arttı.',
                          'teaching_point': 'Yaşamsal bulguları stabil, safralı kusması veya letarjisi '
                                            'olmayan süt çocuğunda fizik muayene tamamlanmadan alan '
                                            'değişikliği ve acil görüntüleme yapılmaz.'},
                         {'text': 'Şiddetli huzursuzluğun gastroözofageal reflü özofajitine bağlı olduğunu '
                                  'varsayarak muayeneyi kısa tutmak, bebeği dik pozisyona alıp acil serviste '
                                  'oral aljinat ve proton pompa inhibitörü başlamak',
                          'is_correct': False,
                          'scenario_update': 'Kusma veya tartı kaybı olmayan bebeğe ampirik asit baskılayıcı '
                                             'tedavi verildi; ancak ağlama ataklarında hiçbir gerileme '
                                             'sağlanamadı.',
                          'teaching_point': 'Tartı alımı iyi olan ve kusma yakınması bulunmayan ağlayan '
                                            'bebeklerde ampirik antireflü veya proton pompa inhibitörü '
                                            'tedavisinin etkinliği yoktur.'}]},
            {'stage_title': 'Tetkik ve Görüntüleme Planlaması',
             'question': 'Fizik muayenesi tamamen normal saptanan, ateşsiz ve son bir ayda 900 gram tartı '
                         'alımı olan bu bebekte hangi tetkik yaklaşımı doğrudur?',
             'options': [{'text': 'Atipik seyirli gizli idrar yolu enfeksiyonunu dışlamak amacıyla mesane '
                                  'kateterizasyonu ile idrar tetkiki, idrar kültürü, tam kan sayımı ve '
                                  'C-reaktif protein istemek',
                          'is_correct': False,
                          'scenario_update': 'Mesane kateterizasyonu işlemi bebeğin daha şiddetli ağlamasına '
                                             'yol açtı; tam idrar tetkiki (lökosit 0, nitrit negatif) ve '
                                             'akut faz reaktanları tamamen normal sonuçlandı.',
                          'teaching_point': 'Ateşi olmayan, tartı alımı mükemmel olan ve atak aralarında '
                                            'tamamen huzurlu seyreden sağlıklı süt çocuklarında invaziv '
                                            'idrar sondası ve kan tetkiki endikasyonu yoktur.'},
                         {'text': 'İntestinal malrotasyon veya erken evre ileokolik geçiş patolojisini '
                                  'ekarte etmek amacıyla ayakta direkt batın grafisi ve tüm batın '
                                  'ultrasonografisi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Çekilen ayakta direkt batın grafisinde fizyolojik gaz dağılımı '
                                             'izlendi, ultrasonografi normal raporlandı; bebek gereksiz '
                                             'radyasyona maruz kaldı.',
                          'teaching_point': 'Safralı kusma, batın distansiyonu, kanlı dışkılama veya atak '
                                            'aralarında letarji bulgusu olmayan ve muayenesi normal bebekte '
                                            'radyolojik görüntüleme önerilmez.'},
                         {'text': 'Kırmızı bayrak bulgusu ve patolojik muayene verisi bulunmadığından '
                                  'laboratuvar testi veya radyolojik görüntüleme istemeden klinik izlem ve '
                                  'aile değerlendirmesine geçmek',
                          'is_correct': True,
                          'explanation': 'Büyüme-gelişmesi normal olan, kırmızı bayrak bulgusu (ateş, '
                                         'safralı kusma, kanlı gaita, letarji) taşımayan ve tepeden tırnağa '
                                         'muayenesi doğal saptanan bebekte laboratuvar veya görüntüleme '
                                         'tetkiki yönetimi değiştirmez.',
                          'new_finding': 'Ek invaziv tetkik istenmedi; bebek loş ve sakin ortamda anne '
                                         'kucağında ritmik pışpışlama ile sakinleşti, aktif göz teması '
                                         'kurdu.'},
                         {'text': 'Besin proteini duyarlılığını ve gizli gastrointestinal kanamayı '
                                  'araştırmak üzere gaitada gizli kan, gaita redüktan madde, gaita pH ve '
                                  'spesifik IgE paneli çalışmak',
                          'is_correct': False,
                          'scenario_update': 'İshal, mukuslu-kanlı dışkılama veya атоpik egzama bulgusu '
                                             'olmayan bebekte tüm gaita ve spesifik IgE testleri negatif '
                                             'sonuçlandı.',
                          'teaching_point': 'Gaitada mukus/kan, kusma veya büyüme geriliği eşlik etmeyen '
                                            'izole akşam ağlama ataklarında rutin alerji ve gaita taraması '
                                            'önerilmez.'}]},
            {'stage_title': 'Klinik Tanı ve Ayırıcı Değerlendirme',
             'question': 'Öyküsü, büyüme eğrisi ve tamamen normal fizik muayene bulgularıyla bu bebekte en '
                         'olası klinik tanınız nedir?',
             'options': [{'text': 'İnek Sütü Proteini Alerjik Proktokoliti',
                          'is_correct': False,
                          'scenario_update': 'Alerjik proktokolitte çizgi şeklinde kanlı ve bol mukuslu '
                                             'gaita beklenir; bu bebekte dışkılama paterni ve cilt muayenesi '
                                             'tamamen normaldir.',
                          'teaching_point': 'İnek sütü proteini alerjisi yalnızca gün boyu süren dirençli '
                                            'huzursuzlukta kanlı-mukuslu gaita, kusma, egzama veya tartı '
                                            'alımında duraklama varsa düşünülür.'},
                         {'text': 'Komplike Gastroözofageal Reflü Hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Hastada tekrarlayan kusma, beslenmeyi reddetme, opisthotonus '
                                             'postürü veya tartı kaybı bulunmadığından reflü özofajiti '
                                             'klinik tabloyla uyumlu değildir.',
                          'teaching_point': 'Kusması olmayan ve haftalık tartı alımı normal olan bebeklerde '
                                            'sadece akşam saatlerinde ortaya çıkan ağlama krizleri reflü '
                                            'hastalığı ile açıklanamaz.'},
                         {'text': 'Korneal Abrazyon veya Saç Turnikesi Sendromu',
                          'is_correct': False,
                          'scenario_update': 'Floresein boyama ve ekstremite/genital bölge muayenesi tamamen '
                                             'normal saptanmış olup akut travmatik/iskemik patolojiler '
                                             'dışlanmıştır.',
                          'teaching_point': 'Korneal abrazyon ve saç turnikesi sendromu günün belirli bir '
                                            'saatinde değil, olay geliştiği andan itibaren kesintisiz '
                                            'ağlamaya yol açar.'},
                         {'text': 'İnfantil Kolik (Fonksiyonel Paroksismal Ağlama)',
                          'is_correct': True,
                          'explanation': 'Sağlıklı ve büyümesi normal bir süt çocuğunda özellikle akşam '
                                         'saatlerinde yoğunlaşan, organik neden saptanamayan paroksismal '
                                         'ağlama atakları infantil kolik (Wessel kriterleri / Roma IV) '
                                         'tanısını koydurur.',
                          'new_finding': 'Kesin Tanı: İnfantil Kolik. Organik acil patolojiler güvenli '
                                         'biçimde dışlandı.'}]},
            {'stage_title': 'Tedavi, İzlem ve Taburculuk Planı',
             'question': 'İnfantil kolik tanısı koyduğunuz bu bebeğin acil servis yönetimi ve taburculuk '
                         'eğitiminde en uygun yaklaşım hangisidir?',
             'options': [{'text': 'Tablonun selim ve geçici olduğunu açıklamak, 5S yatıştırma manevralarını '
                                  'göstermek, ebeveyn tükenmişliğinde bebeği sarsmama uyarısı ve kırmızı '
                                  'bayrak eğitimiyle ilaçsız taburcu etmek',
                          'is_correct': True,
                          'explanation': 'İnfantil kolikte en kanıta dayalı yaklaşım aileyi rahatlatmak, '
                                         'duyusal yatıştırma tekniklerini öğretmek ve ebeveyn tükenmişliğine '
                                         "bağlı 'Sarsılmış Bebek Sendromu'nu önleyici danışmanlık vermektir.",
                          'new_finding': 'Ailenin kaygıları giderildi, yatıştırma teknikleri ve acil başvuru '
                                         'gerektiren kırmızı bayraklar (ateş, safralı kusma, kanlı gaita, '
                                         'letarji) anlatılarak bebek güvenle taburcu edildi.'},
                         {'text': 'Anne sütünden geçen antijenleri kesmek amacıyla anneye sıkı süt ve süt '
                                  'ürünleri eliminasyon diyeti başlamak, bebeğe ise simetikon damla ve oral '
                                  'antihistaminik reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Kanıtlanmamış alerji nedeniyle anneye gereksiz kısıtlayıcı '
                                             'diyet uygulandı; altı haftalık bebeğe verilen sedatif '
                                             'antihistaminik ise letarji ve apne riski yarattı.',
                          'teaching_point': 'Süt çocuklarında antihistaminik veya sedatif ilaçlar solunum '
                                            'depresyonu riski nedeniyle kontrendikedir; simetikonun ise '
                                            'plaseboya üstünlüğü gösterilmemiştir.'},
                         {'text': 'Emzirmeyi geçici olarak durdurup tam hidrolize hipoalerjenik mamaya '
                                  'geçmek ve akşam ağlama krizlerini önlemek için günde iki kez oral '
                                  'trimebutin süspansiyon başlamak',
                          'is_correct': False,
                          'scenario_update': 'Anne sütünün kesilmesi laktasyonu azalttı ve bebeğin beslenme '
                                             'düzenini bozdu; spazmolitik ilaç kullanımı ise paralitik ileus '
                                             'riski oluşturdu.',
                          'teaching_point': 'İnfantil kolikte anne sütü kesinlikle kesilmez ve küçük süt '
                                            'çocuklarında intestinal motilite düzenleyici spazmolitik '
                                            'ilaçlar kullanılmaz.'},
                         {'text': 'Akşam saatlerindeki paroksismal ağrıyı kontrol altına almak için '
                                  'yemeklerden önce oral omeprazol süspansiyon başlamak ve sık aralıklarla '
                                  'rektal gliserinli lavman uygulanmasını önermek',
                          'is_correct': False,
                          'scenario_update': 'Uygulanan proton pompa inhibitörü ağlama süresini '
                                             'değiştirmedi, tekrarlayan rektal uyarılar ise anal mukozada '
                                             'tahriş ve fissür gelişimine neden oldu.',
                          'teaching_point': 'Kolik tedavisinde proton pompa inhibitörlerinin yeri yoktur; '
                                            'tekrarlayan rektal fitil veya lavman uygulamaları mukozal '
                                            'hasara yol açar.'}]}]},
 {'id': 'G12',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '14 Yaş',
  'gender': 'Kız',
  'complaint': 'Ayağa kalkınca olan baş dönmesi (dizziness) ve göz kararması',
  'history': "Hasta kendisi anlatıyor: 'Bu sabah kahvaltı yapmadan okula gittim. Okul bahçesinde törende "
             'güneşin altında beklerken ve evde yataktan hızlı kalktığımda bir anda başım döndü, gözlerim '
             'karardı ve kulaklarım uğuldadı. Oturunca 1-2 dakika içinde hemen geçti. Bayılıp yere düşmedim, '
             'kasılma olmadı, kalbimde çarpıntı veya göğüs ağrısı hissetmedim. Son zamanlarda su içmeyi de '
             "çok unutuyorum.'",
  'final_diagnosis': 'Ortostatik Hipotansiyon ve Vazovagal Presenkop (Postüral İntolerans)',
  'disposition': 'Yeşil Alandan Oral Hidrasyon/Tuz Dengesi ve Postüral Manevra Eğitimi ile Taburculuk',
  'case_pearl': 'Adölesanlarda yatarken veya otururken ayağa kalkmakla ya da uzun süre ayakta kalmakla '
                'gelişen, oturunca hızla düzelen baş dönmesi ve göz kararmasında (presenkop) en sık neden '
                'ortostatik hipotansiyon (ayağa kalktıktan sonraki 3 dakika içinde sistolik TA ≥20 mmHg veya '
                'diyastolik TA ≥10 mmHg düşüş) ve vazovagal mekanizmadır. Kardiyak kırmızı bayraklar '
                '(egzersiz sırasında senkop, yatar pozisyonda senkop, ailede <40 yaş ani kardiyak ölüm, '
                'patolojik üfürüm, anormal EKG) mutlaka dışlanmalıdır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Sabah açken ve ayağa kalktığında başlayan baş dönmesi ile göz kararması tarifleyen '
                         'on dört yaşındaki hastada ilk değerlendirmede ne yapılmalıdır?',
             'options': [{'text': 'Şikayetin iç kulak kaynaklı periferik vestibüler patolojiye bağlı '
                                  'olduğunu düşünerek yatak başında Dix-Hallpike testi ile Epley repozisyon '
                                  'manevrası uygulamak ve hastaya oral dimenhidrinat tablet vermek',
                          'is_correct': False,
                          'scenario_update': 'Dix-Hallpike testinde nistagmus veya rotatuar vertigo '
                                             'tetiklenmedi; verilen antihistaminik ise hastada uyku hali ve '
                                             'halsizlik artışına neden oldu.',
                          'teaching_point': 'Baş dönmesi ile başvuran hastada önce etrafın dönmesi ve '
                                            'nistagmus ile giden gerçek vertigo ile ayağa kalkınca göz '
                                            'kararmasıyla seyreden postüral sersemlik ayırt edilmelidir.'},
                         {'text': 'Akut hipovolemi ve dolaşım bozukluğu varsayımıyla postüral kan basıncı '
                                  'ölçümü beklemeden hastayı hemen Sarı Alana almak ve hızlı intravenöz '
                                  'izotonik salin bolusu tedavisi başlamak',
                          'is_correct': False,
                          'scenario_update': 'İstirahatte yaşamsal bulguları tamamen normal olan ve oral '
                                             'alımı açık hastaya gereksiz damar yolu açıldı; postüral kan '
                                             'basıncı değişimi ise kayıt altına alınamadı.',
                          'teaching_point': 'Genel durumu iyi ve istirahat hemodinamisi stabil olan hastada '
                                            'öncelikle yatar ve ayakta kan basıncı farkı dökümante '
                                            'edilmelidir.'},
                         {'text': 'Yatar pozisyonda ve ayağa kalktıktan üç dakika sonra kan basıncı ile '
                                  'nabız ölçmek, kardiyak oskültasyon, nörolojik muayene ve kardiyak kırmızı '
                                  'bayrak sorgulaması yapmak',
                          'is_correct': True,
                          'explanation': 'Postüral baş dönmesi ve göz kararması yakınmasında yatarak ve '
                                         'ayakta 3. dakika kan basıncı-nabız ölçümü, kardiyak kırmızı bayrak '
                                         'sorgulaması ve nörolojik/vestibüler muayene temel basamaktır.',
                          'new_finding': 'Yatar pozisyonda TA: 106/66 mmHg, KTA: 76/dk; ayağa kalktıktan 3. '
                                         'dakikada TA: 84/50 mmHg, KTA: 104/dk ölçüldü ve hasta bu sırada '
                                         'hafif göz kararması tarifledi. Kardiyak oskültasyonda ritim '
                                         'düzenli, ek ses veya üfürüm yok. Serebellar testler, yürüyüş ve '
                                         'kraniyal sinir muayenesi doğal; nistagmus saptanmadı. Egzersizle '
                                         'senkop veya ailede erken yaş ani kardiyak ölüm öyküsü yok.'},
                         {'text': 'Kısa süreli görsel kararma ve uğuldama tarifini atipik jeneralize nöbet '
                                  'eşdeğeri kabul ederek ayrıntılı fundus ve kraniyal sinir muayenesi '
                                  'sonrası acil çocuk nöroloji konsültasyonu istemek',
                          'is_correct': False,
                          'scenario_update': 'Nörolojik muayenesi tamamen normal olan ve bilinç kaybı, '
                                             'kasılma veya postiktal konfüzyon tariflemeyen hastada nöroloji '
                                             'konsültasyonu patoloji saptamadı.',
                          'teaching_point': 'Ayağa kalkmakla tetiklenen ve oturunca dakikalar içinde düzelen '
                                            'göz kararması ile kulak uğuldaması epileptik aura değil, '
                                            'postüral serebral hipoperfüzyon bulgusudur.'}]},
            {'stage_title': 'Tetkik ve Görüntüleme Planlaması',
             'question': 'Ayağa kalkmakla sistolik kan basıncında 22 mmHg düşüş saptanan ve nörolojik '
                         'muayenesi normal olan bu adölesan kız hastada hangi tetkikler istenmelidir?',
             'options': [{'text': 'Aritmi ve iletim bozukluklarını dışlamak için on iki derivasyonlu '
                                  'elektrokardiyografi çekmek, parmak ucu kan şekeri ve tam kan sayımı '
                                  'bakmak',
                          'is_correct': True,
                          'explanation': 'Bayılma veya bayılayazma yakınmasıyla başvuran her çocuk ve '
                                         'ergende 12 derivasyonlu EKG ve kan şekeri; adölesan kızlarda ise '
                                         'menstrüel kanamaya bağlı demir eksikliği anemisi açısından '
                                         'hemoglobin kontrolü önerilir.',
                          'new_finding': '12 Derivasyonlu EKG: Normal sinüs ritmi, hız 78/dk, QTc: 410 ms, '
                                         'PR ve QRS süreleri normal, delta dalgası veya ST-T değişikliği '
                                         'yok. Parmak ucu kan şekeri: 92 mg/dL. Hemogram: Hb 12.6 g/dL, Hct '
                                         '%38, MCV 84 fL.',
                          'image': 'assets/images/ecg_normal.png',
                          'image_caption': '12 Derivasyonlu EKG: Normal Pediatrik Sinüs Ritmi'},
                         {'text': 'Serebral hipoperfüzyon ve intrakraniyal patolojiyi dışlamak amacıyla '
                                  'kontrastsız beyin bilgisayarlı tomografisi, bilateral karotis-vertebral '
                                  'arter Doppler ultrasonografisi ve uyanıklık elektroensefalografisi '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'Çekilen beyin BT, boyun Doppler USG ve EEG tamamen normal '
                                             'sonuçlandı; ancak hasta gereksiz radyasyon aldı ve temel ritim '
                                             'değerlendirmesi gecikti.',
                          'teaching_point': 'Fokal nörolojik defisiti veya kafa travması olmayan postüral '
                                            'baş dönmesi olgularında kraniyal görüntüleme, Doppler USG ve '
                                            'EEG endikasyonu yoktur.'},
                         {'text': 'Yapısal kalp hastalığı ve miyokardit olasılığını acil serviste ekarte '
                                  'etmek için yatak başı transtorasik ekokardiyografi, serum troponin-I, '
                                  'D-dimer ve tiroid fonksiyon testleri istemek',
                          'is_correct': False,
                          'scenario_update': 'Troponin-I, D-dimer ve TSH düzeyleri ile ekokardiyografi '
                                             'tamamen normal bulundu; acil serviste gereksiz tetkik maliyeti '
                                             've bekleme süresi oluştu.',
                          'teaching_point': "Kardiyak kırmızı bayrağı ve üfürümü olmayan, EKG'si normal "
                                            'saptanan hastalarda acil ekokardiyografi ve kardiyak '
                                            'biyobelirteç taraması önerilmez.'},
                         {'text': 'Tipik postüral kan basıncı düşüşü saptandığından elektrokardiyografi ve '
                                  'kapiller kan şekeri dahil hiçbir tetkik yapmadan hastayı doğrudan sözlü '
                                  'önerilerle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Hasta EKG çekilmeden taburcu edildi; oysa konjenital uzun QT '
                                             'veya preeksitasyon sendromlarını dışlamak için bazal EKG kaydı '
                                             'kılavuz zorunluluğuydu.',
                          'teaching_point': 'Tablo ne kadar tipik görünürse görünsün, ilk kez başvuran '
                                            'presenkop/senkop hastalarında 12 derivasyonlu EKG ve kapiller '
                                            'glukoz ölçümü atlanmamalıdır.'}]},
            {'stage_title': 'Klinik Tanı ve Ayırıcı Değerlendirme',
             'question': 'Postüral kan basıncı düşüşü, normal elektrokardiyografi ve normal hemoglobin '
                         'değerleri ışığında bu hastada en olası tanınız nedir?',
             'options': [{'text': 'Uzun QT Sendromuna Bağlı Kardiyojenik Senkop',
                          'is_correct': False,
                          'scenario_update': "Hastanın EKG'sinde QTc 410 ms ile normal sınırlardadır ve "
                                             'eforla veya ani sesle tetiklenen prodromsuz bayılma öyküsü '
                                             'bulunmamaktadır.',
                          'teaching_point': 'Kardiyojenik senkop genellikle prodromsuz olarak egzersiz '
                                            'sırasında veya yatar pozisyonda gelişir ve patolojik EKG ya da '
                                            'aile öyküsü eşlik eder.'},
                         {'text': 'Ortostatik Hipotansiyon ve Vazovagal Presenkop',
                          'is_correct': True,
                          'explanation': 'Ayağa kalktıktan sonraki 3 dakika içinde sistolik kan basıncında '
                                         '≥20 mmHg veya diyastolik kan basıncında ≥10 mmHg düşüş olması '
                                         'ortostatik hipotansiyonu tanımlar; açlık ve yetersiz sıvı alımı '
                                         'vazovagal/ortostatik presenkopu kolaylaştırır.',
                          'new_finding': 'Kesin Tanı: Ortostatik Hipotansiyon ve Vazovagal Presenkop.'},
                         {'text': 'Benign Paroksismal Pozisyonel Vertigo',
                          'is_correct': False,
                          'scenario_update': 'Hastada baş hareketleriyle tetiklenen rotatuar baş dönmesi '
                                             'veya nistagmus yoktur; semptomlar yalnızca ayağa kalkınca ve '
                                             'uzun süre ayakta kalınca oluşmaktadır.',
                          'teaching_point': 'Periferik vertigoda kan basıncı düşüşü olmaz, etrafın dönmesi '
                                            'hissi ve pozisyonel nistagmus saptanır.'},
                         {'text': 'Postüral Ortostatik Taşikardi Sendromu (POTS)',
                          'is_correct': False,
                          'scenario_update': 'Adölesanlarda POTS tanısı için ortostatik hipotansiyon '
                                             'OLMAKSIZIN kalp hızının ≥40/dk artması gerekir; bu hastada ise '
                                             'belirgin kan basıncı düşüşü mevcuttur.',
                          'teaching_point': 'POTS tanısı ancak ilk 3 dakikada klasik ortostatik kan basıncı '
                                            'düşüşü (≥20/10 mmHg) dışlandıktan sonra aşırı taşikardi (≥40/dk '
                                            'artış) varlığında konulabilir.'}]},
            {'stage_title': 'Tedavi, İzlem ve Taburculuk Planı',
             'question': 'Ortostatik hipotansiyon ve vazovagal presenkop tanısı alan bu hastanın acil servis '
                         'yönetimi ve taburculuk eğitiminde en doğru yaklaşım hangisidir?',
             'options': [{'text': 'Kan basıncı düşüşünü hızla düzeltmek için birinci basamak tedavi olarak '
                                  'oral fludrokortizon asetat ve midodrin tablet reçete edip iki hafta sıkı '
                                  'tuz kısıtlaması önermek',
                          'is_correct': False,
                          'scenario_update': 'Yaşam tarzı önlemleri denenmeden başlanan mineralokortikoid ve '
                                             'alfa-agonist tedavi baş ağrısı ve supin hipertansiyona yol '
                                             'açtı; tuz kısıtlaması ise hipovolemiyi derinleştirdi.',
                          'teaching_point': 'Adölesan ortostatik hipotansiyonunda farmakolojik ajanlar '
                                            '(fludrokortizon, midodrin) ilk basamak değildir; ayrıca tuz '
                                            'kısıtlaması değil, tuz desteğinin artırılması gerekir.'},
                         {'text': 'Refleks taşikardiyi baskılamak amacıyla düşük doz oral propranolol '
                                  'tedavisi başlamak, okulda beden eğitimi derslerini tamamen yasaklamak ve '
                                  'uzun süreli yatak istirahati raporu düzenlemek',
                          'is_correct': False,
                          'scenario_update': 'Verilen beta-bloker kompansatuar kalp hızı yanıtını '
                                             'baskılayarak hastanın ayağa kalktığında daha ağır hipotansiyon '
                                             'yaşamasına ve kondisyon kaybına neden oldu.',
                          'teaching_point': 'Hipovolemiye bağlı ortostatik hipotansiyonda beta-blokerler '
                                            'kompansatuar taşikardiyi engelleyerek semptomları kötüleştirir; '
                                            'uzun süreli yatak istirahati ise ortostatik toleransı daha da '
                                            'bozar.'},
                         {'text': 'Hastayı monitörize gözlem yatağında yirmi dört saat yatırarak seri '
                                  'kardiyak enzim takibi yapmak ve taburculuk öncesi mutlaka eğik masa '
                                  '(tilt-table) provokasyon testi uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Kardiyak kırmızı bayrağı olmayan hasta gereksiz yere bir gün '
                                             'hastanede tutuldu; tüm seri troponin değerleri normal kaldı.',
                          'teaching_point': "Tipik öyküsü ve ortostatik vital bulgusu olan, EKG'si normal "
                                            'hastalarda hastaneye yatış veya acil tilt-table testi '
                                            'endikasyonu yoktur.'},
                         {'text': 'Oral sıvı desteği sağlamak, günlük su ve tuz alımını artırmayı, '
                                  'kahvaltıyı atlamamayı, kademeli ayağa kalkmayı ve prodromda izometrik '
                                  'karşı-basınç manevralarını öğreterek taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Adölesan ortostatik hipotansiyon ve vazovagal presenkopta birinci '
                                         'basamak tedavi yeterli hidrasyon (2-2.5 L/gün su), uygun tuz '
                                         'alımı, düzenli kahvaltı, yataktan kademeli kalkış ve prodrom '
                                         'anında bacak çaprazlama/çömelme gibi izometrik karşı-basınç '
                                         'manevralarıdır.',
                          'new_finding': 'Acil serviste oral sıvı alımı sonrası semptomları tamamen düzelen '
                                         'hasta, postüral önlemler ve kırmızı bayrak eğitimi verilerek '
                                         'taburcu edildi.'}]}]},
 {'id': 'G13',
  'category': '🫁 Hırıltı & Solunum Sıkıntısı',
  'age': '20 Aylık',
  'gender': 'Erkek',
  'complaint': 'Gece aniden başlayan havlar tarzda kaba öksürük ve ses kısıklığı',
  'history': "Annesi ve babası gece 02:00'de getiriyor: 'Gündüz sadece hafif burun akıntısı vardı. Gece "
             'yarısı bir anda köpek havlaması ya da fok balığı sesi gibi çok kaba bir öksürükle uyandı, '
             'ağlarken sesi kalın ve boğuk çıkıyor. Soğuk gece havasında arabaya götürürken biraz rahatladı, '
             "şu an kucağımızda sakin oturuyor, salya akışı veya yutma güçlüğü yok.'",
  'final_diagnosis': 'Hafif Akut Viral Laringotrakeit (Hafif Krup - Westley Skoru 1)',
  'disposition': 'Yeşil Alandan Tek Doz Oral Deksametazon ve Aile Eğitimi ile Taburculuk',
  'case_pearl': 'İstirahatte stridoru ve göğüs çekilmesi olmayan, yalnızca ağlamakla veya öksürükle kaba '
                "sesi ve stridoru duyulan viral laringotrakeit 'Hafif Krup' (Westley skoru ≤2) olarak "
                'sınıflandırılır. Hafif krupta dahi tek doz (0.15 - 0.6 mg/kg) oral deksametazon semptom '
                'süresini, uyku bölünmesini ve acile tekrar başvuruyu anlamlı biçimde azaltır; istirahatte '
                'stridor yoksa nebülize adrenalin uygulanmaz.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Gece aniden başlayan havlar tarzda kaba öksürük ve ses kısıklığı ile getirilen '
                         'yirmi aylık bu çocukta ilk muayene yaklaşımınız nasıl olmalıdır?',
             'options': [{'text': 'Üst hava yolu ödeminin derecesini doğrudan görmek amacıyla çocuğu muayene '
                                  'masasına yatırıp abeslang yardımıyla derin orofarenks ve epiglot '
                                  'muayenesi yapmak',
                          'is_correct': False,
                          'scenario_update': 'Zorla yapılan dil basacağı muayenesi çocuğu şiddetli ağlattı; '
                                             'artan negatif intratorasik basınç ve türbülan hava akımı '
                                             'nedeniyle inspiratuar stridor belirginleşti.',
                          'teaching_point': 'Akut üst hava yolu darlığı bulguları olan çocuklarda ağlama ve '
                                            'ajitasyon türbülan akımı artırarak darlığı ağırlaştırır; zorlu '
                                            'ağız içi muayeneden kaçınılmalıdır.'},
                         {'text': 'Akut üst hava yolu obstrüksiyonu riski nedeniyle muayeneyi beklemeden '
                                  'hastayı Sarı Alana devretmek, damar yolu açmak ve hemen nebülize '
                                  'adrenalin tedavisi başlamak',
                          'is_correct': False,
                          'scenario_update': 'İstirahatte rahat olan çocuğa damar yolu açılırken gelişen '
                                             'şiddetli ağlama solunum iş yükünü artırdı; endikasyon dışı '
                                             'verilen nebülize adrenalin ise taşikardiye ve gereksiz dört '
                                             'saatlik gözlem zorunluluğuna yol açtı.',
                          'teaching_point': 'İstirahatte stridoru ve çekilmesi olmayan, genel durumu iyi '
                                            'çocuklarda ağrılı damar yolu girişimi ve nebülize adrenalin '
                                            'endikasyonu yoktur.'},
                         {'text': 'Gece başlayan kaba öksürüğü alt hava yolu darlığı olarak değerlendirip '
                                  'öncelikle kurtarıcı nebülize salbutamol uygulamak ve yirmi dakika sonra '
                                  'oskültasyonu tekrarlamak',
                          'is_correct': False,
                          'scenario_update': 'Uygulanan nebülize beta-2 agonist üst hava yolundaki mukozal '
                                             'ödem üzerinde hiçbir etki göstermedi ve çocukta huzursuzluk '
                                             'ile taşikardi yaptı.',
                          'teaching_point': 'Havlar tarzda kaba öksürük ve ses kısıklığı alt hava yolu '
                                            'bronkospazmını değil, subglottik üst hava yolu ödemini '
                                            'gösterir; bronkodilatörler etkisizdir.'},
                         {'text': 'Çocuğu ağlatmadan anne kucağında genel görünümünü, istirahatte stridor ve '
                                  'çekilme varlığını, akciğer havalanmasını, satürasyonu değerlendirmek ve '
                                  'salya akışını dışlamak',
                          'is_correct': True,
                          'explanation': 'Üst hava yolu darlığı düşünülen çocuklarda değerlendirme çocuğu '
                                         'huzursuz etmeden anne kucağında yapılmalı; istirahatte stridor, '
                                         'çekilmeler ve ağır bakteriyel üst hava yolu enfeksiyonu kırmızı '
                                         'bayrakları (salya akışı, toksik görünüm, tripod pozisyonu) kontrol '
                                         'edilmelidir.',
                          'new_finding': 'Yaşamsal bulgular: Ateş 37.7°C, KTA 120/dk, SS 26/dk, oda '
                                         'havasında SpO2 %99. Çocuk anne kucağında sakin, etrafıyla ilgili '
                                         've cilt rengi doğal. İstirahat halinde inspiratuar stridor '
                                         'duyulmuyor; yalnızca heyecanlandığında veya öksürdüğünde kaba ses '
                                         've hafif stridor ortaya çıkıyor. Suprasternal veya interkostal '
                                         'çekilme yok, her iki akciğere hava girişi eşit ve doğal. Salya '
                                         'akışı, yutma güçlüğü veya toksik görünüm saptanmadı.'}]},
            {'stage_title': 'Tetkik ve Görüntüleme Planlaması',
             'question': 'İstirahatte stridoru, göğüs çekilmesi ve yabancı cisim aspirasyonu kuşkusu '
                         'bulunmayan, genel durumu iyi olan bu çocukta hangi tetkik yaklaşımı doğrudur?',
             'options': [{'text': 'Subglottik daralmayı radyolojik olarak doğrulamak ve retrolaringeal '
                                  'patolojileri dışlamak amacıyla ön-arka ve yan yumuşak doku boyun grafisi '
                                  'ile akciğer grafisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Röntgen odasında pozisyon verilirken ağlayan çocuğun solunum '
                                             'sıkıntısı arttı; çekilen grafiler klinik yönetimi hiç '
                                             'değiştirmedi.',
                          'teaching_point': 'Tipik viral üst hava yolu darlığı tablosunda boyun veya akciğer '
                                            'grafisi rutin olarak önerilmez; görüntüleme yalnızca atipik '
                                            'seyir, yabancı cisim veya retrofaringeal apse şüphesinde '
                                            'düşünülür.'},
                         {'text': 'Tipik klinik tablo ve normal oksijenasyon varlığında rutin boyun veya '
                                  'akciğer grafisi ile kan tetkiki istemeden doğrudan tedavi planlamasına '
                                  'geçmek',
                          'is_correct': True,
                          'explanation': 'Tipik gece başlangıçlı kaba öksürük ve ses kısıklığı tablosunda '
                                         'değerlendirme tamamen kliniktir; gereksiz kan alma ve radyografi '
                                         'işlemleri çocuğu ağlatarak üst hava yolu darlığını kötüleştirir.',
                          'new_finding': 'Ek laboratuvar veya radyolojik tetkik istenmedi; çocuk anne '
                                         'kucağında sakin kalarak tedavi basamağına geçildi.'},
                         {'text': 'Bakteriyel süperenfeksiyonu ve solunumsal asidozu değerlendirmek üzere '
                                  'tam kan sayımı, C-reaktif protein, prokalsitonin, kan kültürü ve kapiller '
                                  'kan gazı çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Kan alma işlemi sırasında çocuk katılarak ağladı ve '
                                             'inspiratuar stridoru belirginleşti; tüm laboratuvar ve kan '
                                             'gazı parametreleri normal sınırlarda geldi.',
                          'teaching_point': 'Hafif seyirli ve oksijen satürasyonu normal olan hastalarda kan '
                                            'tetkiki veya kan gazı alınması endike değildir; ağrılı işlemler '
                                            'hava yolu obstrüksiyonunu artırır.'},
                         {'text': 'Özgül antiviral veya antibiyotik seçimi yapabilmek için nazofaringeal '
                                  'sürüntüden çoklu solunum yolu viral polimeraz zincir reaksiyonu paneli ve '
                                  'boğaz kültürü istemek',
                          'is_correct': False,
                          'scenario_update': 'Nazofaringeal ve orofaringeal sürüntü işlemi çocuğu ajite '
                                             'etti; test sonuçları acil servis tedavisinde hiçbir değişiklik '
                                             'sağlamadı.',
                          'teaching_point': 'Ayaktan izlenecek hafif olgularda etken virüsü saptamaya '
                                            'yönelik rutin moleküler panel veya boğaz kültürü acil yönetimi '
                                            'değiştirmez.'}]},
            {'stage_title': 'Klinik Tanı ve Ayırıcı Değerlendirme',
             'question': 'Mevcut öykü ve fizik muayene bulguları (istirahatte stridor ve çekilme olmaması, '
                         'Westley skoru 1) ile bu hastada tanınız nedir?',
             'options': [{'text': 'Hafif Akut Viral Laringotrakeit (Krup)',
                          'is_correct': True,
                          'explanation': 'Viral prodrom sonrası gece başlayan havlar tarzda öksürük ve ses '
                                         'kısıklığı varlığında istirahatte stridor ve göğüs duvarı '
                                         'çekilmesinin olmaması (Westley skoru ≤2) Hafif Akut Viral Krup '
                                         'tanısını koydurur.',
                          'new_finding': 'Kesin Tanı: Hafif Akut Viral Laringotrakeit (Westley Skoru: 1).'},
                         {'text': 'Orta-Ağır Akut Laringotrakeit (Westley Skoru ≥3)',
                          'is_correct': False,
                          'scenario_update': 'Orta-ağır krup tanısı için istirahat halinde duyulan stridor '
                                             've belirgin suprasternal/interkostal çekilmeler bulunmalıdır; '
                                             'bu hastada istirahatte stridor ve çekilme yoktur.',
                          'teaching_point': 'Westley skorlamasında istirahatte stridor olmaması ve çekilme '
                                            'bulunmaması hastayı hafif krup grubuna sokar.'},
                         {'text': 'Akut Bakteriyel Trakeit veya Epiglottit',
                          'is_correct': False,
                          'scenario_update': 'Hastada yüksek ateş, toksik görünüm, salya akışı, yutma '
                                             'güçlüğü veya pürülan hava yolu sekresyonu bulunmamaktadır.',
                          'teaching_point': 'Epiglottit ve bakteriyel trakeitte yüksek ateş, toksik tablo ve '
                                            'ilerleyici ağır solunum sıkıntısı ön plandadır.'},
                         {'text': 'Akut Subglottik Yabancı Cisim Aspirasyonu',
                          'is_correct': False,
                          'scenario_update': 'Öyküde ani boğulma/morarma atağı yoktur; tablo gündüz başlayan '
                                             'burun akıntısı ve subfebril ateş prodromu sonrası gelişmiştir.',
                          'teaching_point': 'Yabancı cisim aspirasyonu viral prodrom olmaksızın yemek veya '
                                            'oyun sırasında ani başlayan boğulma ve öksürük krizi ile '
                                            'karakterizedir.'}]},
            {'stage_title': 'Tedavi, İzlem ve Taburculuk Planı',
             'question': 'Hafif akut viral laringotrakeit (Westley skoru 1) tanısı koyduğunuz bu hastada en '
                         'uygun tedavi ve taburculuk yaklaşımı hangisidir?',
             'options': [{'text': 'Tek doz oral deksametazon ile birlikte rutin bir doz nebülize L-adrenalin '
                                  'uygulamak ve işlemden on beş dakika sonra hastayı doğrudan evine taburcu '
                                  'etmek',
                          'is_correct': False,
                          'scenario_update': 'Hafif krupta endikasyon dışı nebülize adrenalin verildi; '
                                             'üstelik adrenalin etkisi 2 saatte geçtiği için erken '
                                             'taburculuk sonrası rebound stridor riski oluştu.',
                          'teaching_point': 'Nebülize L-adrenalin yalnızca orta-ağır krupta (istirahatte '
                                            'stridor varlığında) endikedir ve uygulanan her hasta rebound '
                                            'stridor açısından en az 2-4 saat gözlenmeden taburcu edilemez.'},
                         {'text': 'Sistemik steroid yan etkilerinden kaçınmak için yalnızca soğuk buhar '
                                  'inhalasyonu ve nebülize salbutamol uygulamak, sekonder enfeksiyon '
                                  'profilaksisi için oral amoksisilin-klavulanat reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Steroid verilmeyen çocuk aynı gece sabaha karşı artan stridor '
                                             've göğüs çekilmeleriyle acil servise orta krup tablosunda '
                                             'tekrar başvurdu.',
                          'teaching_point': 'Hafif krupta dahi tek doz deksametazon acile tekrar başvuruyu '
                                            've kötüleşmeyi azaltır; salbutamol ve antibiyotiklerin viral '
                                            'krupta yeri yoktur.'},
                         {'text': 'Tek doz 0.15-0.6 mg/kg oral deksametazon uygulamak, nebülize adrenalin '
                                  'vermeden oral alımını gözlemlemek ve istirahatte stridor gelişirse '
                                  'başvuru eğitimiyle taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Hafif krup tedavisinde altın standart tek doz 0.15-0.6 mg/kg oral '
                                         'deksametazondur (oral alamıyorsa İM veya nebülize budesonid). '
                                         'İstirahatte stridor olmadığı için nebülize adrenalin ve uzun '
                                         'süreli gözlem gerekmez.',
                          'new_finding': 'Tek doz oral deksametazon sorunsuz içirildi; aileye nemli/serin '
                                         'hava desteği ve kırmızı bayraklar (istirahatte stridor, çekilme, '
                                         'salya akışı, morarma) anlatılarak taburcu edildi.'},
                         {'text': 'İntramüsküler seftriakson ve metilprednizolon enjeksiyonu yaptıktan sonra '
                                  'evde yedi gün kullanılmak üzere oral prednizolon şurup ve dekstrometorfan '
                                  'içeren öksürük şurubu reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Ağrılı enjeksiyon çocuğu şiddetli ağlatarak stridorunu '
                                             'artırdı; küçük çocukta kontrendike olan antitussif şurup ise '
                                             'solunum depresyonu riski yarattı.',
                          'teaching_point': 'Uzun yarı ömürlü tek doz oral deksametazon yeterlidir, 7 günlük '
                                            'steroid kürü gerekmez; ayrıca küçük çocuklarda santral öksürük '
                                            'kesiciler kontrendikedir.'}]}]},
 {'id': 'G14',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '5 Yaş',
  'gender': 'Kız',
  'complaint': 'Saçlı deriden ve gövdeden başlayan kaşıntılı, içi su dolu kabarcıklar ve hafif ateş',
  'history': "Annesi anlatıyor: 'Dün hafif ateşi ve halsizliği oldu. Bu sabah saçlarının arasında, yüzünde "
             've karnında kırmızı noktalar çıktı, birkaç saat içinde üstleri su damlası gibi kabarcıklara '
             'dönüştü. Çok kaşınıyor. Anaokulunda geçen hafta iki arkadaşında da aynı döküntüler çıkmış. '
             "Aşıları eksik kalmıştı, kronik bir hastalığı yok.'",
  'final_diagnosis': 'Suçiçeği (Varisella - Primer VZV Enfeksiyonu)',
  'disposition': 'Yeşil Alandan Semptomatik Tedavi, Aspirin/İbuprofen Yasağı Uyarıları ve İzolasyon Eğitimi '
                 'ile Taburculuk',
  'case_pearl': 'Suçiçeğinde saçlı deri ve gövdeden başlayan (sentripetal dağılım), kaşıntılı ve aynı anda '
                "farklı evrelerde (makül, papül, 'gül yaprağı üzerinde çiğ damlası' vezikül, püstül ve krut) "
                'polimorfik lezyonlar tanı koydurucudur. Tedavide Reye sendromu riski nedeniyle Aspirin ve '
                'invaziv Grup A Streptokok / nekrotizan fasiit riskini artırdığı için İbuprofen (NSAİİ) '
                'kesinlikle verilmemeli; antipiretik olarak yalnızca Parasetamol tercih edilmelidir.',
  'steps': [{'stage_title': 'Enfeksiyon Kontrolü ve Fizik Muayene',
             'question': 'Saçlı deriden ve gövdeden başlayan kaşıntılı su dolu kabarcıklar ile getirilen beş '
                         'yaşındaki bu çocukta ilk yaklaşımınız nasıl olmalıdır?',
             'options': [{'text': 'Hava yolu ve temas izolasyonu önlemleri alarak saçlı deri dahil tüm '
                                  'cildi, mukozaları, akciğer oskültasyonunu ve serebellar dengeyi muayene '
                                  'etmek',
                          'is_correct': True,
                          'explanation': 'Yüksek bulaştırıcılığa sahip veziküler döküntülü hastalar bekleme '
                                         'salonundan derhal izole odaya alınmalı; lezyonların '
                                         'dağılımı/evreleri ile olası pulmoner, nörolojik ve sekonder '
                                         'bakteriyel deri komplikasyonları değerlendirilmelidir.',
                          'new_finding': 'Yaşamsal bulgular: Ateş 37.8°C, KTA 98/dk, SS 20/dk, SpO2 %99. '
                                         'Hasta izole muayene odasına alındı. Saçlı deri, yüz ve gövdede '
                                         'yoğunlaşan, ekstremitelerde daha seyrek dağılım gösteren eritemli '
                                         'maküller, papüller, ince duvarlı berrak veziküller ve erken evre '
                                         'krutlanmış lezyonların aynı anda bir arada bulunduğu görüldü. '
                                         'Lezyon çevresinde pürülan selülit bulgusu yok. Akciğer '
                                         'oskültasyonu ve serebellar denge muayenesi doğal.'},
                         {'text': 'Döküntülerin alerjik reaksiyon olduğunu düşünerek hastayı genel bekleme '
                                  'alanına almak ve muayene öncesinde intramüsküler feniramin ile '
                                  'deksametazon enjeksiyonu hemen uygulatmak',
                          'is_correct': False,
                          'scenario_update': 'Bekleme salonundaki immünsüprese hastalar ve gebeler hava '
                                             'yoluyla bulaşan etkene maruz kaldı; uygulanan sistemik steroid '
                                             'ise viral replikasyonun ağırlaşması riskini doğurdu.',
                          'teaching_point': 'Ateşli veziküler döküntüyle başvuran çocuklar bulaş riski '
                                            'nedeniyle ortak bekleme salonunda tutulmamalı ve viral '
                                            'enfeksiyon dışlanmadan sistemik steroid verilmemelidir.'},
                         {'text': 'İzole lokalize deri enfeksiyonu varsayımıyla ek bulaş önlemi almadan '
                                  'lezyonların üstünü steril iğne ile açıp povidon iyot solüsyonu ile '
                                  'pansuman yapmak',
                          'is_correct': False,
                          'scenario_update': 'İğne ile patlatılan veziküller çocukta şiddetli ağrıya yol '
                                             'açtı ve sağlam epidermal bariyer bozulduğu için sekonder '
                                             'bakteriyel süperenfeksiyon ile skar riski arttı.',
                          'teaching_point': 'Veziküler döküntüler kesinlikle patlatılmaz; vezikül '
                                            'bütünlüğünün korunması sekonder stafilokoksik ve streptokoksik '
                                            'invazyonu önler.'},
                         {'text': 'Yaygın veziküler döküntüyü ağır sistemik bakteriyel sepsis bulgusu kabul '
                                  'ederek çocuğu izolasyonsuz Sarı Alana devretmek ve hemen intravenöz '
                                  'antibiyotik tedavisi hazırlamak',
                          'is_correct': False,
                          'scenario_update': 'İzolasyon önlemi alınmadan Sarı Alana alınan hasta diğer '
                                             'kritik hastalar için ciddi bulaş kaynağı oluşturdu; genel '
                                             'durumu iyi olan çocukta sepsis bulgusu saptanmadı.',
                          'teaching_point': 'Yaşamsal bulguları stabil olan veziküler döküntülü çocuklarda '
                                            'öncelik izolasyon önlemi alarak klinik muayene yapmaktır.'}]},
            {'stage_title': 'Tetkik ve Görüntüleme Planlaması',
             'question': 'Bağışıklığı normal, genel durumu iyi ve fizik muayenede komplikasyon bulgusu '
                         'saptanmayan beş yaşındaki bu hastada hangi tetkik yaklaşımı uygundur?',
             'options': [{'text': 'Etkeni kesinleştirmek ve sistemik yayılımı taramak amacıyla vezikül '
                                  'sıvısından polimeraz zincir reaksiyonu testi, viral seroloji, tam kan '
                                  'sayımı ve karaciğer enzimleri istemek',
                          'is_correct': False,
                          'scenario_update': 'Kan alma işlemi çocuğun huzursuzluğunu artırdı; lökosit sayısı '
                                             'hafif düşük, transaminazlar normal geldi ve PCR sonucu günler '
                                             'sonra çıkacağı için acil yönetime katkı sağlamadı.',
                          'teaching_point': 'İmmünkompetan çocuklarda tipik polimorfik veziküler döküntü '
                                            'varlığında rutin kan tetkiki, seroloji veya PCR doğrulaması '
                                            'gerekmez.'},
                         {'text': 'Subklinik viral pnömoni ve bakteriyel süperenfeksiyonu dışlamak için '
                                  'arka-ön akciğer grafisi, kan kültürü, C-reaktif protein ve eritrosit '
                                  'sedimantasyon hızı çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Solunum sıkıntısı olmayan çocuğun radyoloji ünitesine '
                                             'gönderilmesi hastane içi bulaş riskine yol açtı; akciğer '
                                             'grafisi ve akut faz reaktanları normal bulundu.',
                          'teaching_point': 'Takipne, öksürük, hipoksi veya dirençli yüksek ateş gibi '
                                            'komplikasyon bulguları olmayan vakalarda akciğer grafisi ve kan '
                                            'kültürü istenmez.'},
                         {'text': 'Veziküler lezyon tabanından Tzanck yayması ve bakteriyel yara kültürü '
                                  'alarak sonuçlar çıkana kadar hastayı acil servis gözlem odasında izlemek',
                          'is_correct': False,
                          'scenario_update': 'Pürülan akıntısı olmayan berrak vezikülden alınan kültür üreme '
                                             'göstermedi; hastanın acil serviste bekletilmesi bulaş süresini '
                                             'uzattı.',
                          'teaching_point': 'Sekonder bakteriyel enfeksiyon bulgusu olmayan tipik vakalarda '
                                            'yara kültürü veya Tzanck yayması rutin acil pratiğinde endike '
                                            'değildir.'},
                         {'text': 'Tipik polimorfik veziküler döküntü ve temas öyküsü bulunduğundan ek '
                                  'laboratuvar, seroloji veya görüntüleme tetkiki istemeden klinik '
                                  'değerlendirme ile ilerlemek',
                          'is_correct': True,
                          'explanation': 'Saçlı deriyi ve gövdeyi tutan, aynı anda farklı evrelerdeki '
                                         'veziküler lezyonlarla seyreden klasik tabloda değerlendirme '
                                         'tamamen kliniktir; komplikasyonsuz immünkompetan hastada tetkik '
                                         'gerekmez.',
                          'new_finding': 'Ek laboratuvar veya görüntüleme tetkiki istenmedi; hastane içi '
                                         'bulaş önlenerek doğrudan klinik yönetim aşamasına geçildi.'}]},
            {'stage_title': 'Klinik Tanı ve Ayırıcı Değerlendirme',
             'question': 'Saçlı deriyi tutan sentripetal dağılımlı ve aynı anda farklı evrelerdeki (makül, '
                         'papül, vezikül, krut) polimorfik döküntü bulgularıyla tanınız nedir?',
             'options': [{'text': 'El-Ayak-Ağız Hastalığı (Enteroviral Veziküler Ekzantem)',
                          'is_correct': False,
                          'scenario_update': 'El-ayak-ağız hastalığında veziküller ağız mukozası, avuç içi, '
                                             'ayak tabanı ve gluteal bölgede yoğunlaşır (akral dağılım); '
                                             'saçlı deriden başlayan polimorfik gövde döküntüsü beklenmez.',
                          'teaching_point': 'Sentripetal (gövde ve saçlı deri ağırlıklı) ve farklı '
                                            'evrelerdeki kaşıntılı veziküller el-ayak-ağız hastalığından '
                                            'ayırt ettiricidir.'},
                         {'text': 'Suçiçeği (Primer Varisella Enfeksiyonu)',
                          'is_correct': True,
                          'explanation': 'Kreş temas öyküsü sonrası saçlı deri ve gövdeden başlayan, aynı '
                                         'anda makül, papül, berrak vezikül ve krut evrelerinde bulunan '
                                         'kaşıntılı polimorfik döküntü Suçiçeği (Varisella) için '
                                         'patognomoniktir.',
                          'new_finding': 'Kesin Tanı: Suçiçeği (Varisella).'},
                         {'text': 'Büllöz İmpetigo (Stafilokoksik Deri Enfeksiyonu)',
                          'is_correct': False,
                          'scenario_update': 'Büllöz impetigoda gevşek duvarlı büyük büller ve açıldığında '
                                             'vernik benzeri sarı krutlar görülür; saçlı deriden başlayan '
                                             'yaygın simetrik çiğ damlası veziküllerle seyretmez.',
                          'teaching_point': 'Büllöz impetigo lokalize veya asimetrik kümeler halinde başlar; '
                                            'tüm gövde ve saçlı deriyi tutan polimorfik veziküler ekzantem '
                                            'varisella lehinedir.'},
                         {'text': 'Papüler Ürtiker ve Yaygın Böcek Isırığı',
                          'is_correct': False,
                          'scenario_update': 'Papüler ürtiker genellikle giysi dışı açık ekstremite '
                                             'bölgelerinde gruplaşan ürtikeryal papüllerle seyreder; ateş '
                                             'prodromu, mukoza/saçlı deri tutulumu ve kreş salgını öyküsü '
                                             'varisellayı gösterir.',
                          'teaching_point': 'Saçlı deri tutulumu ve eritemli zeminde ince duvarlı '
                                            'veziküllerin hızlıca krutlanması papüler ürtikerden ayrımda en '
                                            'önemli klinik ipucudur.'}]},
            {'stage_title': 'Tedavi, İlaç Güvenliği ve Taburculuk Planı',
             'question': 'İmmünkompetan beş yaşındaki bu suçiçeği hastasında reçete düzenleme ve taburculuk '
                         'eğitiminde en doğru yaklaşım hangisidir?',
             'options': [{'text': 'Dirençli ateşi ve inflamasyonu kontrol altına almak için parasetamol ile '
                                  'dönüşümlü oral ibuprofen süspansiyon başlamak ve lezyonlara topikal '
                                  'betametazon krem sürülmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Suçiçeğinde kullanılan ibuprofen ve topikal steroid, lezyon '
                                             'yerlerinde invaziv Grup A Streptokok enfeksiyonu ve nekrotizan '
                                             'fasiit gelişme riskini ciddi oranda artırdı!',
                          'teaching_point': "Suçiçeğinde İbuprofen ve diğer NSAİİ'ler ağır nekrotizan "
                                            'yumuşak doku enfeksiyonu riskini artırdığı için, topikal '
                                            'steroidler ise lokal bağışıklığı baskıladığı için '
                                            'kontrendikedir.'},
                         {'text': 'Ateş için yalnızca parasetamol, kaşıntı için oral antihistaminik vermek; '
                                  'aspirin ve ibuprofenden kaçınılmasını, tırnak kesimini ve lezyonlar '
                                  'kabuklanana dek izolasyonu anlatmak',
                          'is_correct': True,
                          'explanation': 'Sağlıklı 12 yaş altı çocuklarda suçiçeği tedavisi semptomatiktir: '
                                         'ateş için sadece parasetamol, kaşıntı için oral antihistaminik ve '
                                         'ılık duş önerilir. Reye sendromu nedeniyle Aspirin ve nekrotizan '
                                         'fasiit riski nedeniyle İbuprofen kesinlikle yasaklanmalı, tüm '
                                         'lezyonlar krutlanana kadar okul izolasyonu sağlanmalıdır.',
                          'new_finding': 'Parasetamol ve oral antihistaminik reçete edildi; ilaç güvenliği, '
                                         'cilt hijyeni, izolasyon süresi ve kırmızı bayraklar (ataksi, '
                                         'takipne, lezyon çevresinde hızla yayılan kızarıklık/ağrı) '
                                         'anlatılarak taburcu edildi.'},
                         {'text': 'Sağlıklı her okul öncesi çocukta komplikasyonları önlemek amacıyla rutin '
                                  'beş gün yüksek doz oral asiklovir, profilaktik oral sefaleksin ve talk '
                                  'pudrası reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Lezyonların üzerine sürülen talk pudrası bakteriyel '
                                             'kolonizasyon için zemin oluşturdu; sağlıklı 5 yaş çocukta '
                                             'rutin antiviral ve profilaktik antibiyotik gereksiz yan '
                                             'etkilere yol açtı.',
                          'teaching_point': 'Komplikasyonsuz sağlıklı 12 yaş altı çocuklarda rutin oral '
                                            'asiklovir veya profilaktik antibiyotik önerilmez; pudra/talk '
                                            'kullanımı ise sekonder bakteriyel enfeksiyon riskini artırır.'},
                         {'text': 'Ateş kontrolü için asetilsalisilik asit (aspirin) vermek, kaşıntıyı '
                                  'azaltmak için veziküllerin üzerine yoğun çinko oksitli pomad kapatmak ve '
                                  'ateş düşünce okula dönüşe izin vermek',
                          'is_correct': False,
                          'scenario_update': 'Verilen aspirin akut ensefalopati ve karaciğer yağlanması '
                                             '(Reye sendromu) riskini tetikledi; kabuklanma tamamlanmadan '
                                             'okula dönüş ise salgının yayılmasına yol açtı.',
                          'teaching_point': 'Suçiçeğinde aspirin Reye sendromu nedeniyle mutlak '
                                            'kontrendikedir; bulaştırıcılık ise ateşin düşmesiyle değil, tüm '
                                            'veziküllerin kabuklanmasıyla sona erer.'}]}]},
 {'id': 'G15',
  'category': '👁️ Göz Şikayetleri',
  'age': '3 Yaş',
  'gender': 'Kız',
  'complaint': 'Her iki gözde kızarıklık, sulanma, sabah kirpiklerde çapaklanma ve burun akıntısı',
  'history': "Annesi anlatıyor: '2 gündür burnu akıyor ve hafif hapşırıyordu. Dün sağ gözü pembeleşti ve "
             'sulandı, bu sabah uyandığında iki gözünde de sulu-hafif çapaklanma vardı. Göz kapakları şiş '
             'değil, gözünü rahatça hareket ettiriyor, ışığa bakabiliyor ve görmesinde bir sorun yok. Ateşi '
             "37.3°C.'",
  'final_diagnosis': 'Akut Adenoviral (Viral) Konjonktivit',
  'disposition': 'Yeşil Alandan Göz Temizliği, Destek Tedavisi ve Hijyen Eğitimi ile Taburculuk',
  'case_pearl': 'Çocuklarda burun akıntısı, hapşırık ve preauriküler lenfadenopatinin eşlik ettiği, bir '
                'gözden başlayıp diğerine geçen hiperemi ve sulu-serömüköz akıntı çoğunlukla viral '
                '(özellikle Adenovirus) konjonktivittir. Muayenede orbital selülit (göz kapağı ödemi, '
                'proptozis, ağrılı/kısıtlı göz hareketleri), korneal tutulum/herpes (korneal bulanıklık, '
                'şiddetli fotofobi) ve eşlik edebilecek akut otitis media mutlaka dışlanmalıdır. Topikal '
                'anestezik veya steroidli göz damlaları acil serviste kesinlikle reçete edilmez.',
  'steps': [{'stage_title': 'Oftalmolojik ve Sistemik Fizik Muayene',
             'question': 'Üst solunum yolu semptomları eşlik eden bilateral göz kızarıklığı ve sulanma ile '
                         'getirilen üç yaşındaki çocukta ilk muayenede neleri değerlendirmelisiniz?',
             'options': [{'text': 'Derin orbital enfeksiyon olasılığını hızla dışlamak amacıyla fizik '
                                  'muayene öncesinde hastayı radyolojiye göndererek kontrastlı orbital '
                                  'bilgisayarlı tomografi çekmek ve damar yolu açmak',
                          'is_correct': False,
                          'scenario_update': 'Kapak ödemi, proptozisi veya göz hareket kısıtlılığı olmayan '
                                             'üç yaşındaki çocukta çekilen orbital BT tamamen normal çıktı '
                                             've lens dokusu gereksiz radyasyona maruz kaldı.',
                          'teaching_point': 'Orbital BT yalnızca proptozis, oftalmopleji, ağrılı göz '
                                            'hareketleri, görme azalması veya ağır periorbital ödem gibi '
                                            'orbital selülit bulguları varsa çekilir.'},
                         {'text': 'Göz hareketlerinin her yöne açıklığını ve ağrısızlığını, periorbital '
                                  'ödemi, kornea saydamlığını, ışık refleksini, preauriküler lenf nodlarını '
                                  've kulak zarlarını muayene etmek',
                          'is_correct': True,
                          'explanation': 'Kırmızı gözle başvuran çocukta görmeyi ve yaşamı tehdit eden '
                                         'durumları (orbital selülit, korneal ülser/keratit) ve eşlik '
                                         'edebilecek orta kulak enfeksiyonunu dışlamak için göz hareketleri, '
                                         'kornea saydamlığı, preauriküler lenf nodu ve otoskopi mutlaka '
                                         'değerlendirilmelidir.',
                          'new_finding': 'Yaşamsal bulgular: Ateş 37.3°C, KTA 104/dk. Bilateral bulber ve '
                                         'tarsal konjonktivada belirgin hiperemi ve sulu-serömüköz sekresyon '
                                         'mevcut. Periorbital ödem, kapak endürasyonu veya proptozis yok. '
                                         'Göz küresi hareketleri her yöne tam ve ağrısız. Kornea saydam, '
                                         'floresein boyanma defekti yok, pupiller izokorik ve ışık refleksi '
                                         'bilateral doğal. Sağ preauriküler bölgede 0.8 cm mobil hassas lenf '
                                         'nodu palpe edildi; bilateral timpanik membranlar doğal.'},
                         {'text': 'Kızarıklık ve batma hissini hızla gidermek için kornea muayenesi yapmadan '
                                  'acil serviste deksametazon içeren göz damlası ve lokal anestezik damla '
                                  'uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Kornea bütünlüğü değerlendirilmeden uygulanan topikal steroid '
                                             've anestezik damla epitel iyileşmesini baskılayarak korneal '
                                             'ülserasyon riski oluşturdu.',
                          'teaching_point': 'Korneal epitel defekti ve herpetik keratit dışlanmadan kırmızı '
                                            'göze kesinlikle kortikosteroidli damla uygulanmaz.'},
                         {'text': 'Çocuğu huzursuz etmemek için göz kapaklarını ve kulak zarlarını açmadan '
                                  'yalnızca dışarıdan gözlem yapmak ve doğrudan oral geniş spektrumlu '
                                  'antibiyotik reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Kornea ve kulak muayenesi atlandı; yüzeyel mukozal tablo için '
                                             'verilen sistemik antibiyotik ise ishal dışında hiçbir etki '
                                             'göstermedi.',
                          'teaching_point': 'Göz kızarıklığı ile başvuran çocuklarda kornea saydamlığı ve '
                                            'eşlik edebilecek akut otit açısından otoskopik muayene ihmal '
                                            'edilmemelidir.'}]},
            {'stage_title': 'Tetkik ve Görüntüleme Planlaması',
             'question': 'Korneası saydam, göz hareketleri tam ve ağrısız, otoskopisi normal olan üç '
                         'yaşındaki bu hastada hangi tetkik yaklaşımı doğrudur?',
             'options': [{'text': 'Etken mikroorganizmayı ve antibiyotik duyarlılığını saptamak amacıyla her '
                                  'iki alt forniksten bakteriyel kültür, Gram boyama ve klamidyal antijen '
                                  'taraması istemek',
                          'is_correct': False,
                          'scenario_update': 'Alınan oküler sürüntü örneklerinde patojen bakteri üremedi; '
                                             'kültür sonucu 48 saat sonra çıktığı için acil servis '
                                             'yönetimine hiçbir katkı sağlamadı.',
                          'teaching_point': 'Yenidoğan dönemi dışında ve hiperakut pürülan (gonokoksik) '
                                            'akıntı şüphesi olmayan akut çocukluk çağı olgularında rutin '
                                            'sürüntü kültürü önerilmez.'},
                         {'text': 'Sistemik inflamatuar yanıtı ve gizli bakteriyemiyi değerlendirmek üzere '
                                  'tam kan sayımı, C-reaktif protein, eritrosit sedimantasyon hızı ve kan '
                                  'kültürü çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Genel durumu iyi ve ateşsiz çocukta yapılan damar girişimi '
                                             'ağlamaya yol açtı; tüm hemogram ve akut faz değerleri normal '
                                             'sınırlarda geldi.',
                          'teaching_point': 'Komplike olmayan yüzeyel oküler mukozal enfeksiyonlarda '
                                            'sistemik kan tahlili ve kan kültürü endikasyonu yoktur.'},
                         {'text': 'Subklinik derin doku yayılımını ve sinüzit komplikasyonunu dışlamak '
                                  'amacıyla paranazal sinüs grafisi ve yüzeyel periorbital yumuşak doku '
                                  'ultrasonografisi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Periorbital ödemi olmayan üç yaşındaki çocukta çekilen sinüs '
                                             'grafisi ve yüzeyel ultrasonografi normal raporlandı.',
                          'teaching_point': 'Periorbital şişlik, eritem veya göz hareket kısıtlılığı olmayan '
                                            'çocuklarda görüntüleme tetkiki yapılmaz.'},
                         {'text': 'Kırmızı bayrak bulgusu bulunmayan bu tabloda ek kan tahlili, radyolojik '
                                  'görüntüleme veya oküler sürüntü kültürü istemeden klinik olarak ilerlemek',
                          'is_correct': True,
                          'explanation': 'Üst solunum yolu enfeksiyonu bulguları ve preauriküler '
                                         'lenfadenopati eşliğinde gelişen, korneası saydam ve kapak ödemi '
                                         'olmayan olgularda değerlendirme kliniktir; laboratuvar testi '
                                         'gerekmez.',
                          'new_finding': 'Ek laboratuvar veya kültür tetkiki istenmedi; klinik bulgularla '
                                         'tanı aşamasına geçildi.'}]},
            {'stage_title': 'Klinik Tanı ve Ayırıcı Değerlendirme',
             'question': 'Üst solunum yolu enfeksiyonu bulguları, bir gözden diğerine geçen hiperemi, '
                         'serömüköz akıntı ve preauriküler lenfadenopati varlığında en olası tanınız nedir?',
             'options': [{'text': 'Preseptal (Periorbital) Selülit',
                          'is_correct': False,
                          'scenario_update': 'Preseptal selülitte göz kapaklarında belirgin ödem, '
                                             'kızarıklık, ısı artışı ve hassasiyet bulunur; bu hastada göz '
                                             'kapakları tamamen doğaldır.',
                          'teaching_point': 'Kapak ödemi ve periorbital cilt eritemi olmaksızın yalnızca '
                                            'konjonktival hiperemi bulunması preseptal selüliti dışlar.'},
                         {'text': 'Herpetik Keratokonjonktivit (Korneal Ülser)',
                          'is_correct': False,
                          'scenario_update': 'Herpetik tutulum genellikle tek taraflıdır, göz kapağında grup '
                                             'veziküller, şiddetli fotofobi ve floresein ile dendritik '
                                             'korneal boyanma görülür.',
                          'teaching_point': 'Saydam kornea, floresein boyanma olmaması ve bilateral '
                                            'serömüköz sekresyon herpetik keratitten uzaklaştırır.'},
                         {'text': 'Akut Adenoviral (Viral) Konjonktivit',
                          'is_correct': True,
                          'explanation': 'Rinit semptomları, bir gözden başlayıp 24-48 saatte diğer göze '
                                         'geçen konjonktival hiperemi, sulu-serömüköz sekresyon ve hassas '
                                         'preauriküler lenfadenopati akut adenoviral konjonktivit için '
                                         'tipiktir.',
                          'new_finding': 'Kesin Tanı: Akut Adenoviral (Viral) Konjonktivit.'},
                         {'text': 'Akut Nazolakrimal Kanal Tıkanıklığı ve Dakriyosistit',
                          'is_correct': False,
                          'scenario_update': 'Dakriyosistitte medial kantus ve gözyaşı kesesi üzerinde '
                                             'kızarık, ağrılı şişlik ve kese basısıyla punktumdan pürülan '
                                             'reflü saptanır.',
                          'teaching_point': 'Medial kantusta şişlik olmaması ve tablonun ÜSYE ile birlikte '
                                            'akut bilateral başlaması viral konjonktivit lehinedir.'}]},
            {'stage_title': 'Tedavi, İzlem ve Taburculuk Planı',
             'question': 'Akut adenoviral konjonktivit tanısı koyduğunuz bu çocukta en doğru tedavi, hijyen '
                         've taburculuk yaklaşımı hangisidir?',
             'options': [{'text': 'Steril serum fizyolojik ile kapak temizliği, soğuk kompres ve suni '
                                  'gözyaşı önermek, sıkı el-havlu hijyeni ve kırmızı bayrak eğitimiyle '
                                  'taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Viral konjonktivitte temel tedavi mekanik sekresyon temizliği, '
                                         'soğuk kompres, suni gözyaşı damlaları ve yüksek bulaştırıcılık '
                                         'nedeniyle el, havlu ve yastık kılıfı hijyenidir.',
                          'new_finding': 'Göz temizliği ve temas hijyeni eğitimi verildi; kapak ödemi, '
                                         'şiddetli göz ağrısı, fotofobi, yoğun pürülan akıntı veya görme '
                                         'bulanıklığı gelişirse başvuru önerisiyle taburcu edildi.'},
                         {'text': 'Oküler ağrı ve yanmayı evde kesmek için hastaya proparakain içeren '
                                  'topikal anestezik göz damlası reçete etmek ve her iki gözü steril gazlı '
                                  'bezle kapatmak',
                          'is_correct': False,
                          'scenario_update': 'Evde tekrarlayan topikal anestezik damla kullanımı kornea '
                                             'epitel rejenerasyonunu durdurarak toksik keratopatiye, göz '
                                             'kapama bandajı ise sekonder bakteriyel üremeye yol açtı!',
                          'teaching_point': 'Topikal anestezik göz damlaları korneal erime riski nedeniyle '
                                            'hastaya asla reçete edilmez; ayrıca enfeksiyöz '
                                            'konjonktivitlerde göz bandajla kapatılmaz.'},
                         {'text': 'Hiperemiyi hızla baskılamak amacıyla günde dört kez topikal prednizolon '
                                  'asetat göz damlası ve on gün süreyle oral amoksisilin-klavulanat '
                                  'süspansiyon tedavisi başlamak',
                          'is_correct': False,
                          'scenario_update': 'Topikal steroid viral saçılım süresini uzattı ve göz içi '
                                             'basıncı artışı riski yarattı; sistemik antibiyotik ise viral '
                                             'tabloda etkisiz kaldı.',
                          'teaching_point': 'Acil serviste oftalmolog kontrolü olmadan kırmızı göze topikal '
                                            'steroid reçete edilmez; basit konjonktivitte oral antibiyotik '
                                            'endikasyonu yoktur.'},
                         {'text': 'Viral replikasyonu durdurmak için beş gün süreyle oral asiklovir '
                                  'süspansiyon ve günde beş kez topikal gansiklovir oftalmik jel reçete '
                                  'ederek gözlem altına almak',
                          'is_correct': False,
                          'scenario_update': 'Herpes virüslerine etkili olan asiklovir ve gansiklovir '
                                             'adenoviral enfeksiyon üzerinde etki göstermedi ve oküler '
                                             'yüzeyde lokal irritasyon yaptı.',
                          'teaching_point': 'Adenoviral konjonktivit kendi kendini sınırlayan bir '
                                            'enfeksiyondur; anti-herpetik antivirallerin (asiklovir, '
                                            'gansiklovir) adenovirüse karşı klinik etkinliği yoktur.'}]}]},
 {'id': 'G16',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '4 Yaş',
  'gender': 'Erkek',
  'complaint': 'Burun delikleri ve ağız çevresinde kaşıntılı, sarı-kehribar rengi kabuklu yaralar',
  'history': "Annesi anlatıyor: '4-5 gün önce burnunun altında sinek ısırığı gibi küçük bir kızarıklık "
             'vardı, kaşıdıkça yayıldı. Şimdi burun kenarında ve çenesinde üzeri sarı bal kurumuş gibi '
             "kabuklu 3-4 tane yara oldu. Ateşi yok, keyfi ve iştahı yerinde.'",
  'final_diagnosis': 'Büllöz Olmayan İmpetigo (Non-büllöz İmpetigo - S. aureus / S. pyogenes)',
  'disposition': 'Yeşil Alandan Topikal Antibiyotik (Mupirosin/Fusidik Asit) ve Hijyen Eğitimi ile '
                 'Taburculuk',
  'case_pearl': 'Çocuklarda en sık bakteriyel deri enfeksiyonu olan non-büllöz impetigoda burun ve ağız '
                "çevresinde eritemli zeminde 'bal rengi krutlar' (honey-colored crusts) tipiktir. Sınırlı ve "
                'az sayıda lezyonu olan, sistemik bulgusu bulunmayan vakalarda ilk tercih tedavi kabukların '
                'ılık sabunlu suyla yumuşatılarak temizlenmesi ve topikal Mupirosin veya Fusidik asit '
                'uygulanmasıdır.',
  'steps': [{'stage_title': 'Dermatolojik ve Sistemik Fizik Muayene',
             'question': 'Perioral ve perinazal kabuklu lezyonlarla başvuran bu çocukta fizik muayenede '
                         'öncelikle neleri değerlendirmelisiniz?',
             'options': [{'text': 'Lezyon zeminindeki bakteriyel yükü hızla azaltmak amacıyla kabukları kuru '
                                  'gazlı bezle kazıyarak tamamen kaldırmak ve kanayan zemine povidon iyot '
                                  'solüsyonu sürerek sıkı kapalı pansuman yapmak',
                          'is_correct': False,
                          'scenario_update': 'Kuru halde zorla kaldırılan kabuklar yüzeyel dermiste '
                                             'kanamaya, şiddetli ağrıya ve çevre sağlam deriye '
                                             'oto-inokülasyon riskine yol açtı.',
                          'teaching_point': 'Yüzeyel epidermal kabuklar asla kuru kuruya kazınarak '
                                            'koparılmamalı; ılık su veya serum fizyolojikli kompresle '
                                            'yumuşatılarak nazikçe temizlenmelidir.'},
                         {'text': 'Lezyonların sayısını ve dağılımını, sarı-kehribar rengi krut yapısını, '
                                  'çevre deride basmakla soyulma veya derin endürasyon varlığını ve bölgesel '
                                  'lenf nodlarını muayene etmek',
                          'is_correct': True,
                          'explanation': 'Yüzeyel sınırlı epidermal enfeksiyonu yaygın büllöz tablolardan, '
                                         'eksfoliyatif toksin aracılı soyulmalardan veya derin yumuşak doku '
                                         'enfeksiyonundan ayırt etmek tedavi yolunu belirler.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 95/dk. Perioral ve perinazal '
                                         'bölgede toplam 4 adet, 0.5-1 cm çapında, eritemli zeminde sarı-bal '
                                         'rengi krutlu plaklar mevcut. Yaygın bül yok, basmakla epidermis '
                                         'soyulması negatif, derin doku endürasyonu veya ısı artışı yok. '
                                         'Submandibuler 0.8 cm mobil reaktif lenf nodu dışında sistemik '
                                         'muayene doğal.'},
                         {'text': 'Yüzün orta hattındaki deri enfeksiyonlarının kavernöz sinüs komşuluğu '
                                  'taşıması nedeniyle hastayı acil gözleme yatırarak damar yolu açmak ve '
                                  'kraniyal-oftalmolojik konsültasyon istemek',
                          'is_correct': False,
                          'scenario_update': 'Ateşi, periorbital ödemi veya derin selülit bulgusu olmayan '
                                             'tamamen yüzeyel 4 adet lezyon için gereksiz invaziv girişim ve '
                                             'konsültasyon planlandı.',
                          'teaching_point': 'Kavernöz sinüs trombozu riski fasiyal üçgendeki derin fronkül '
                                            'veya ağır selülitlerde söz konusudur; epidermise sınırlı '
                                            'yüzeyel krutlu lezyonlarda yatış gerekmez.'},
                         {'text': 'Fizik muayeneyi yalnızca burun çevresiyle sınırlı tutup vezikül-krut '
                                  'ayrımı veya tüm vücut deri kontrolü yapmadan doğrudan geniş spektrumlu '
                                  'ampirik oral antibiyotik reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Gövde ve ekstremiteler kontrol edilmediği için lezyonların '
                                             'gerçekten sınırlı olup olmadığı ve büllöz tutulum varlığı '
                                             'doğrulanamadı.',
                          'teaching_point': 'Deri enfeksiyonlarında tedavi seçimi lezyonların toplam '
                                            'yaygınlığına ve bül varlığına göre yapıldığından tüm deri '
                                            'yüzeyi incelenmelidir.'}]},
            {'stage_title': 'Tetkik İstem Kararı',
             'question': 'Sınırlı sayıda (4 adet) perioral krutlu lezyonu olan, ateşi ve derin doku bulgusu '
                         'bulunmayan bu çocukta hangi tetkikler istenmelidir?',
             'options': [{'text': 'Topikal veya sistemik tedaviye başlamadan önce krut altından '
                                  'bakteriyolojik yara sürüntü kültürü ve antibiyogram alarak üreme sonucuna '
                                  'göre hedefe yönelik antibiyotik planlamak',
                          'is_correct': False,
                          'scenario_update': 'Kültür sonucu 48-72 saat sonra S. aureus olarak raporlandı; bu '
                                             'sürede tedavisiz bekleyen çocukta oto-inokülasyonla yeni '
                                             'lezyonlar çıktı.',
                          'teaching_point': 'Tipik ve sınırlı yüzeyel piyodermilerde rutin yara kültürü '
                                            'önerilmez; kültür yalnızca tedaviye dirençli, tekrarlayan veya '
                                            'MRSA salgını şüphesi olan vakalarda alınır.'},
                         {'text': 'Bakteriyel deri enfeksiyonu sonrası akut böbrek tutulumu riskini erken '
                                  'saptamak amacıyla tam idrar tetkiki, serum ASO titresi, kompleman C3 '
                                  'düzeyi ve renal fonksiyon testleri istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR: TİT normal, ASO 80 IU/mL, C3 125 mg/dL, Kreatinin '
                                             '0.35 mg/dL. Sonuçlar klinik yönetimi hiçbir şekilde '
                                             'değiştirmedi.',
                          'teaching_point': 'Akut poststreptokoksik glomerülonefrit deri enfeksiyonundan 2-6 '
                                            'hafta sonra gelişebilir; aktif, asemptomatik yüzeyel lezyon '
                                            'aşamasında rutin C3 veya idrar taraması endike değildir.'},
                         {'text': 'Klinik görünüm yüzeyel epidermise sınırlı olduğu ve sistemik enfeksiyon '
                                  'bulgusu saptanmadığı için ek kan tetkiki veya sürüntü kültürü istemeden '
                                  'tanıya yönelmek',
                          'is_correct': True,
                          'explanation': 'Genel durumu iyi, ateşi olmayan ve sınırlı sayıda tipik yüzeyel '
                                         'krutlu lezyonu bulunan çocuklarda tanı kliniktir; laboratuvar veya '
                                         'kültür tetkiki gerekmez.',
                          'new_finding': 'Ek laboratuvar veya kültür tetkiki istenmedi; klinik bulgularla '
                                         'tanı ve tedavi aşamasına geçildi.'},
                         {'text': 'Enfeksiyonun derin yumuşak dokuya yayılımını ve sistemik inflamatuar '
                                  'yanıtı değerlendirmek amacıyla tam kan sayımı, CRP, prokalsitonin ve '
                                  'periferik kan kültürü tetkikleri istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR: WBC 8.400/mm³, CRP 2.1 mg/L, Prokalsitonin 0.04 '
                                             'ng/mL. Ateşsiz çocukta gereksiz kan alma işlemi yapıldı.',
                          'teaching_point': 'Ateş, bölgesel selülit veya toksik görünüm eşlik etmeyen '
                                            'lokalize yüzeyel deri enfeksiyonlarında sistemik akut faz '
                                            'reaktanları ve kan kültürü istenmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik öykü ve fizik muayene bulgularıyla bu hastada en doğru tanı hangisidir?',
             'options': [{'text': 'Non-büllöz İmpetigo',
                          'is_correct': True,
                          'explanation': 'Burun ve ağız çevresinde kaşıma/mikrotravma sonrası gelişen, '
                                         'eritemli zeminde bal rengi kalın krutlarla karakterize yüzeyel '
                                         'lezyonlar non-büllöz impetigo için tipiktir.',
                          'new_finding': 'Kesin Tanı: Lokalize Non-büllöz İmpetigo.'},
                         {'text': 'Eksfoliyatif Büllöz İmpetigo',
                          'is_correct': False,
                          'scenario_update': "Hastada eksfoliyatif toksin A'ya bağlı gevşek, şeffaf-sarı "
                                             'sıvı dolu intakt büller veya bül yırtılması sonrası ince '
                                             'vernik benzeri yakalık (collarette) görünümü yoktur.',
                          'teaching_point': 'Büllöz impetigoda sağlam deride gelişen gevşek büller ve '
                                            'açıldığında çevresinde kalan ince skuamlı halka görülür; kalın '
                                            'bal rengi krutlar non-büllöz formun özelliğidir.'},
                         {'text': 'Sekonder Enfekte Perioral Atopik Dermatit',
                          'is_correct': False,
                          'scenario_update': 'Çocuğun özgeçmişinde kronik tekrarlayan kuruluk, fleksüral '
                                             'egzama veya atopi öyküsü olmayıp lezyonlar sağlıklı deride '
                                             'sinek ısırığı sonrası akut başlamıştır.',
                          'teaching_point': 'Kronik kserozis ve egzamatöz zemin olmadan sağlıklı deride akut '
                                            'başlayan bal rengi krutlu plaklar primer non-büllöz '
                                            'impetigodur.'},
                         {'text': 'Rekürren Herpes Simpleks Labialis',
                          'is_correct': False,
                          'scenario_update': 'Lezyonlar dudak vermilion sınırında ağrılı-yanmalı prodromla '
                                             'çıkan grup halinde milimetrik veziküller değil, burun altı ve '
                                             'çene derisinde kaşıntılı bal rengi krutlu plaklardır.',
                          'teaching_point': 'Herpes labialis dudak mukokutanöz birleşiminde eritemli zeminde '
                                            'küme yapmış ağrılı küçük veziküllerle seyreder.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Sınırlı sayıda (4 adet) lokalize non-büllöz impetigo lezyonu olan bu çocukta '
                         'kılavuzlara göre ilk basamak tedavi ne olmalıdır?',
             'options': [{'text': 'Krutları ılık sabunlu suyla yumuşatarak temizlemek, günde 3 kez topikal '
                                  '%2 mupirosin krem sürmek ve 24 saat sonra kreşe dönebileceği bilgisiyle '
                                  'taburcu etmek',
                          'is_correct': True,
                          'explanation': 'IDSA ve pediatrik dermatoloji rehberlerine göre sınırlı ve '
                                         'komplike olmayan non-büllöz impetigoda topikal mupirosin veya '
                                         'fusidik asit ilk tercihtir; oral antibiyotik kadar etkilidir ve '
                                         'yan etkisi daha azdır.',
                          'new_finding': 'Topikal %2 mupirosin krem, tırnakların kısa kesilmesi ve havlu '
                                         'ayrımı eğitimi verilerek hasta şifayla taburcu edildi.'},
                         {'text': 'Topikal tedavinin yüz bölgesinde yetersiz kalacağı düşüncesiyle doğrudan '
                                  '10 gün süreyle oral amoksisilin-klavulanat (45 mg/kg/gün) reçete edip '
                                  'lezyonlar tamamen iyileşene dek kreşi yasaklamak',
                          'is_correct': False,
                          'scenario_update': 'Sınırlı 4 lezyon için verilen 10 günlük sistemik geniş '
                                             'spektrumlu antibiyotik çocukta antibiyotik ilişkili ishale yol '
                                             'açtı.',
                          'teaching_point': 'Oral antibiyotik (sefaleksin veya amoksisilin-klavulanat) '
                                            'yalnızca çok sayıda/yaygın lezyon varlığında, büllöz impetigoda '
                                            'veya kreş salgınlarında tercih edilir; kreş izolasyonu etkili '
                                            'tedavinin 24. saatine kadardır.'},
                         {'text': 'Kaşıntı ve eritemi hızla baskılamak amacıyla günde 2 kez topikal '
                                  'mometazon furoat krem ile topikal ketokonazol kremi birlikte reçete '
                                  'ederek 1 hafta sonra poliklinik kontrolüne çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Bakteriyel piyodermiye uygulanan topikal kortikosteroid lokal '
                                             'bağışıklığı baskılayarak lezyonların tüm yanaklara yayılmasına '
                                             'neden oldu.',
                          'teaching_point': 'İmpetigo S. aureus ve S. pyogenes kaynaklı bakteriyel bir '
                                            'enfeksiyondur; topikal steroid ve antifungal kremler tabloyu '
                                            'ağırlaştırır.'},
                         {'text': 'Poststreptokoksik nefriti önlemek amacıyla tek doz intramüsküler benzatin '
                                  'penisilin G uygulamak ve lezyonların üzerini hava almayacak şekilde '
                                  'steril oklüzif sargıyla kapatarak evde izlemek',
                          'is_correct': False,
                          'scenario_update': 'Non-büllöz impetigoda en sık etken beta-laktamaz salgılayan S. '
                                             'aureus olduğu için penisilin G etkisiz kaldı ve lezyonlar '
                                             'gerilemedi.',
                          'teaching_point': 'Non-büllöz impetigoda başat etken S. aureus olduğundan dar '
                                            'spektrumlu penisilinler etkisizdir; ayrıca antibiyotik tedavisi '
                                            'poststreptokoksik glomerülonefrit gelişimini engellemez.'}]}]},
 {'id': 'G17',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '9 Yaş',
  'gender': 'Erkek',
  'complaint': 'Karın ağrısı, iştahsızlık ve 2 kez kusma',
  'history': "Annesi Yeşil Alan polikliniğine 'üşüttü, midesini bozdu' diyerek getiriyor: 'Dün akşam "
             'göbeğinin etrafında başlayan bir karın ağrısı vardı, gece 2 kez kustu. Bu sabah ağrısı '
             'karnının sağ alt tarafına indi. Çok sevdiği börekten bile bir lokma yemedi. Arabayla hastaneye '
             'gelirken kasislere girdikçe karnını tutup inledi ve muayene odasına hafif öne eğilerek yavaş '
             "yavaş yürüdü.'",
  'final_diagnosis': 'Akut Apandisit (Yeşil Alandan Sarı Alana Devir ve Cerrahi Yatış)',
  'disposition': 'Yeşil Alanda Saptanıp Sarı Alana Devir -> İV Sıvı/Analjezi/USG Doğrulaması -> Çocuk '
                 'Cerrahisi Yatışı',
  'case_pearl': 'Göbek çevresinden (periumbilikal) başlayıp sağ alt kadrana (McBurney) göç eden ağrı, '
                'iştahsızlık (anoreksi), ağrıdan sonra başlayan kusma ve sarsıntıyla/yürümekle artan ağrı '
                '(topuk testi / kasis belirtisi) akut apandisit için çok güçlü ipuçlarıdır. Yeşil alana '
                "'basit karın ağrısı/gastroenterit' diye başvuran bu hastalar muayene ile yakalanıp Sarı "
                'Alana devredilmelidir.',
  'steps': [{'stage_title': 'Yeşil Alanda Fizik Muayene ve Alan Kararı',
             'question': 'Yeşil alana mide üşütmesi düşüncesiyle getirilen bu 9 yaşındaki çocukta ilk '
                         'muayene ve alan kararınız ne olmalıdır?',
             'options': [{'text': 'Kusma ve karın ağrısını viral mide-bağırsak enfeksiyonu olarak '
                                  'değerlendirip Yeşil Alanda intramüsküler ondansetron uygulamak, oral '
                                  'rehidratasyon sıvısı başlayarak 2 saat sonra ağızdan beslenme toleransını '
                                  'kontrol etmek',
                          'is_correct': False,
                          'scenario_update': 'İshali olmayan ve sağ alt kadran peritoneal irritasyon bulgusu '
                                             'bulunan çocukta oral sıvı verilmesi kusmayı artırdı ve cerrahi '
                                             'tanı gecikti.',
                          'teaching_point': 'Ağrının kusmadan önce başladığı, ishali olmayan ve '
                                            'yürümekle/sarsıntıyla sağ alt kadran ağrısı tarifleyen çocukta '
                                            'batın muayenesi yapılmadan viral enfeksiyon tedavisi '
                                            'başlanmaz.'},
                         {'text': 'Sağ alt kadrandaki ağrıyı dışkı stazına bağlı kolik olarak yorumlayıp '
                                  'Yeşil Alanda rektal sodyum fosfat lavman uygulamak ve defekasyon sonrası '
                                  'ağrının tamamen gerileyip gerilemediğini gözlemlemek',
                          'is_correct': False,
                          'scenario_update': 'Akut peritoneal irritasyon bulgusu olan hastaya yapılan rektal '
                                             'lavman intraluminal basıncı ve karın ağrısını şiddetlendirdi.',
                          'teaching_point': 'Ateş, anoreksi, göç eden karın ağrısı ve peritoneal duyarlılığı '
                                            'olan çocuklarda akut cerrahi batın dışlanmadan rektal lavman '
                                            'uygulanmaz.'},
                         {'text': 'Sağ alt kadranda spina iliaka anterior superior ile umblikus hattının dış '
                                  'üçte birlik noktasında lokalize defans ve geri çekme hassasiyetini '
                                  'değerlendirip hastayı Sarı Alana devretmek',
                          'is_correct': True,
                          'triggers_yellow_transfer': True,
                          'explanation': 'Göbek çevresinden sağ alt kadrana göç eden ağrı, anoreksi, '
                                         'kasislerde artan ağrı ve lokalize peritoneal irritasyon bulguları '
                                         'akut cerrahi batını gösterir; hasta derhal Sarı Alana alınmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 38.2°C, KTA 112/dk. Batın muayenesinde sağ '
                                         'alt kadranda spina iliaka anterior superior ile umblikus hattının '
                                         'dış üçte birlik noktasında lokalize defans ve geri çekme '
                                         'hassasiyeti pozitif; sol alt kadran palpasyonuyla sağ alt kadranda '
                                         'ağrı ve topuk sarsıntı testi pozitif. Hasta Sarı Alana '
                                         'devredildi!'},
                         {'text': 'Hastayı Yeşil Alanda tutarak önce ayakta direkt batın grafisi ve tam '
                                  'idrar tetkiki istemek, sonuçlar çıkana kadar oral parasetamol süspansiyon '
                                  'içirerek bekleme salonunda klinik seyri izlemek',
                          'is_correct': False,
                          'scenario_update': 'Olası cerrahi girişim gerektiren hastaya ağızdan ilaç/sıvı '
                                             'verilmesi anestezi açlık süresini bozdu ve direkt batın '
                                             'grafisi tanısal katkı sağlamadı.',
                          'teaching_point': 'Akut cerrahi batın şüphesi saptanan hastada oral alım derhal '
                                            'kesilmeli, hasta Sarı Alana devredilmeli ve gereksiz direkt '
                                            'batın grafisi yerine ultrasonografi planlanmalıdır.'}]},
            {'stage_title': 'Sarı Alanda İlk Yaklaşım ve Görüntüleme Kararı',
             'question': 'Hastayı Sarı Alana devraldınız. Bu aşamada ilk yönetim ve tetkik isteminiz nasıl '
                         'olmalıdır?',
             'options': [{'text': 'Ağızdan alımı kesmek, damar yolu açıp izotonik sıvı ve intravenöz '
                                  'analjezi başlamak; hemogram, CRP, tam idrar tetkiki ve kademeli '
                                  'kompresyonlu batın ultrasonografisi istemek',
                          'is_correct': True,
                          'explanation': 'Cerrahi akut batın şüphesinde ağızdan alımın kesilmesi, intravenöz '
                                         'hidrasyon, muayene bulgularını maskelemeyen uygun doz analjezi ve '
                                         'radyasyon içermeyen ilk basamak görüntüleme olarak ultrasonografi '
                                         'altın standarttır.',
                          'new_finding': 'LABORATUVAR: WBC 16.800/mm³ (%84 nötrofil), CRP 46 mg/L, TİT '
                                         'normal. BATIN USG: Sağ alt kadranda peristaltizmi olmayan, '
                                         'kompresyonla basılanamayan 9.5 mm çapında kör sonlanan tübüler '
                                         'lümen ve içinde 6 mm akustik gölgelenme veren kalsifiye odak ile '
                                         'çevre mezenterik yağ dokuda ekojenite artışı izlendi.'},
                         {'text': 'Fizik muayene bulgularını ve peritoneal irritasyonu maskelememek adına '
                                  'cerrahi konsültasyon tamamlanana kadar hiçbir analjezik ilaç vermemek, '
                                  'doğrudan oral ve intravenöz kontrastlı tüm batın bilgisayarlı tomografisi '
                                  'çekmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk saatlerce şiddetli ağrı çekti ve ultrasonografi ile '
                                             'radyasyonsuz tanı konulabilecekken yüksek doz karın BT '
                                             'radyasyonuna maruz kaldı.',
                          'teaching_point': 'Güncel pediatrik cerrahi kılavuzlarına göre uygun doz '
                                            'intravenöz analjezi fizik muayene bulgularını maskelemez; ilk '
                                            'görüntüleme seçeneği ise BT değil ultrasonografidir.'},
                         {'text': 'Ağızdan alımı kesip damar yolu açmak, yalnızca ayakta direkt batın '
                                  'grafisi ve tam kan sayımı isteyerek görüntüleme yapmadan doğrudan ampirik '
                                  'intravenöz seftriakson ve metronidazol tedavisi başlamak',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografik doğrulama ve cerrahi değerlendirme yapılmadan '
                                             'başlanan geniş spektrumlu antibiyotik klinik tabloyu kısmen '
                                             'baskılayarak kesin cerrahi kararı geciktirdi.',
                          'teaching_point': 'Sepsis veya yaygın peritonit bulgusu olmayan stabil hastada '
                                            'antibiyotik profilaksisi ultrasonografi ile tanı '
                                            'kesinleştirilip cerrahi karar verildikten sonra başlanır.'},
                         {'text': 'Sağ alt kadran ağrısının mezenterik lenfadenit veya idrar yolu '
                                  'enfeksiyonuna bağlı olabileceği düşüncesiyle ultrasonografiyi erteleyip '
                                  'idrar kültürü, gaita mikroskopisi ve viral antijen testleri sonuçlanana '
                                  'dek gözlemlemek',
                          'is_correct': False,
                          'scenario_update': 'Görüntüleme ertelendiği için geçen 8 saat sonunda hastanın '
                                             "ateşi 39.1°C'ye yükseldi ve sağ alt kadrandaki defans tüm alt "
                                             'batına yayıldı.',
                          'teaching_point': 'Lokalize sağ alt kadran defansı ve geri çekme hassasiyeti olan '
                                            'çocukta ultrasonografi geciktirilmemelidir; lümende kalsifiye '
                                            'taş varlığında perforasyon riski saatler içinde artar.'}]},
            {'stage_title': 'Sarı Alanda Kesin Tanı',
             'question': 'Klinik tablo, nötrofilik lökositoz ve ultrasonografi bulguları eşliğinde kesin '
                         'tanınız nedir?',
             'options': [{'text': 'Akut Mezenterik Lenfadenit Sendromu',
                          'is_correct': False,
                          'scenario_update': "Ultrasonografide çapı 9.5 mm'ye ulaşmış, basılanamayan ve "
                                             'içinde 6 mm apendikolit bulunan inflame apendiks doğrudan '
                                             'görüntülendi.',
                          'teaching_point': 'Mezenterik lenfadenitte apendiks normal çapta (<6 mm) ve '
                                            'kompresyonla basılanabilir özellikte olup sağ alt kadranda '
                                            'büyümüş reaktif lenf nodları izlenir.'},
                         {'text': 'Akut Süpüratif Apandisit',
                          'is_correct': True,
                          'explanation': 'Yüksek klinik skor (PAS ≥7), nötrofilik lökositoz ve '
                                         'ultrasonografide >6 mm basılanamayan kör sonlanan apendiks ile '
                                         'lümende apendikolit saptanması Akut Apandisit tanısını '
                                         'kesinleştirir.',
                          'new_finding': 'Kesin Tanı: Akut Apandisit.'},
                         {'text': 'Akut İleokolik İntususepsiyon (İnvajinasyon)',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografide iç içe geçmiş bağırsak ansına ait hedef '
                                             'işareti (target sign) değil, kör sonlanan 9.5 mm çapında '
                                             'tübüler apendiks ve apendikolit saptandı.',
                          'teaching_point': 'İnvajinasyon genellikle 3-36 ay arası çocuklarda kolik tarzı '
                                            'ağrı atakları ve ultrasonografide hedef/psödo-böbrek işareti '
                                            'ile seyreder.'},
                         {'text': 'Sağ Distal Üreterolitiazis (Renal Kolik)',
                          'is_correct': False,
                          'scenario_update': 'Tam idrar tetkikinde hematüri saptanmadı, üriner sistem '
                                             'toplayıcı yapıları doğal bulundu ve kalsifiye odak üreterde '
                                             'değil apendiks lümeninde izlendi.',
                          'teaching_point': 'Normal idrar tetkiki, peritoneal irritasyon bulguları ve '
                                            'kalsifiye taşın kör sonlanan apendiks lümeninde yer alması '
                                            'üreter taşını dışlar.'}]},
            {'stage_title': 'Sarı Alanda Tedavi ve Yatış Planı',
             'question': 'Apendikolit eşlikli akut apandisit tanısı kesinleşen bu 9 yaşındaki hastada en '
                         'doğru yönetim hangisidir?',
             'options': [{'text': 'Lümende apendikolit bulunmasına rağmen perforasyon gelişmediği için '
                                  'ameliyatsız yönetim (non-operatif tedavi) amacıyla 10 gün oral '
                                  'amoksisilin-klavulanat reçete edip poliklinik kontrolüyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Apendikolit varlığında ayaktan oral antibiyotikle eve '
                                             'gönderilen hasta 18 saat sonra perfore apandisit ve yaygın '
                                             'peritonit tablosuyla acile tekrar başvurdu.',
                          'teaching_point': 'Apendikolit (fekalit) varlığı ameliyatsız (non-operatif) '
                                            'antibiyotik tedavisinde yüksek başarısızlık ve erken '
                                            'perforasyon kriteridir; kesinlikle ayaktan taburcu edilmez.'},
                         {'text': 'Perforasyon bulgusu olmadığı için cerrahi konsültasyonu ertesi sabah '
                                  'poliklinik şartlarına bırakmak, acil serviste tek doz intramüsküler '
                                  'seftriakson uygulayarak ağrı kesici şurupla hastayı eve göndermek',
                          'is_correct': False,
                          'scenario_update': 'Gece boyunca evde ağrısı ve ateşi artan hastada apendiks '
                                             'lümenindeki taş zemininde nekroz ve lokalize perforasyon '
                                             'gelişti.',
                          'teaching_point': 'Akut apandisit tanısı konulan her çocuk acil servisten Çocuk '
                                            'Cerrahisi konsültasyonu ile yatırılarak izlenmelidir.'},
                         {'text': 'Cerrahi girişim öncesinde kalın bağırsak temizliği sağlamak amacıyla '
                                  'yüksek hacimli rektal lavman ve oral polietilen glikol solüsyonu '
                                  'uygulayıp 24 saat sonra elektif cerrahi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Akut inflame apendiks ve apendikolit varlığında verilen oral '
                                             'laksatif ve lavman intraluminal basıncı artırarak iyatrojenik '
                                             'perforasyona zemin hazırladı.',
                          'teaching_point': 'Akut apandisitte preoperatif mekanik bağırsak temizliği veya '
                                            'lavman kesinlikle kontrendikedir; hasta NPO tutulur.'},
                         {'text': 'Ağızdan aç izlemi sürdürerek intravenöz idame sıvı ve preoperatif '
                                  'profilaktik antibiyotik başlamak, acil Çocuk Cerrahisi konsültasyonu ile '
                                  'apendektomi için cerrahi servise yatırmak',
                          'is_correct': True,
                          'explanation': 'Apendikolit eşlikli akut apandisitte standart yaklaşım NPO, '
                                         'intravenöz hidrasyon, preoperatif profilaktik antibiyotik ve '
                                         'laparoskopik/açık apendektomi için Çocuk Cerrahisi servisine '
                                         'yatıştır.',
                          'new_finding': 'Çocuk Cerrahisi tarafından değerlendirilen hasta preoperatif '
                                         'hazırlıkları tamamlanarak laparoskopik apendektomi yapılmak üzere '
                                         'servise yatırıldı.'}]}]},
 {'id': 'G18',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '15 Aylık',
  'gender': 'Kız',
  'complaint': 'Ateş, halsizlik ve bacaklarda yeni fark edilen küçük kırmızı-mor lekeler',
  'history': "Annesi Yeşil Alana 'ateşi var ve isilik gibi birkaç döküntüsü çıktı' diyerek başvuruyor: "
             "'Öğleden beri 39.2°C ateşi var, bir kez kustu. Normalde çok hareketli bir çocuktur ama son 2 "
             'saattir omzuma başını koyup yatıyor, bacakları da biraz soğuk geldi. Bezini değiştirirken '
             "uyluğunda ve bacağında toplu iğne başı gibi koyu kırmızı-mor 5-6 tane leke gördüm.'",
  'final_diagnosis': 'Meningokoksemi (Ateş + Peteşiyal/Purpurik Döküntü ve Kompanse Septik Şok)',
  'disposition': 'Yeşil Alanda Saptanıp Derhal Sarı/Kırmızı Alana Devir -> Acil İV Seftriakson & Sıvı '
                 'Resüsitasyonu -> Çocuk Yoğun Bakım Yatışı',
  'case_pearl': 'Ateşli bir çocukta BASMAKLA SOLMAYAN (cam bardak / vitropresyon testi pozitif) peteşi veya '
                'purpura varlığı aksi kanıtlanana kadar Meningokoksemi / İnvaziv Bakteriyel Enfeksiyon '
                'acilidir! Özellikle letarji, ekstremite soğukluğu ve kapiller dolum uzaması eşlik ediyorsa '
                'dakikalar hayati önem taşır; LP veya görüntüleme beklenmeden kan kültürü alınıp ilk 1 saat '
                'içinde İV 3. kuşak sefalosporin (Seftriakson/Sefotaksim) ve sıvı resüsitasyonu '
                'başlanmalıdır.',
  'steps': [{'stage_title': 'Yeşil Alanda İlk Değerlendirme ve Alan Kararı',
             'question': 'Yeşil alana ateş, halsizlik ve bacaklarda yeni başlayan döküntü ile getirilen bu '
                         '15 aylık bebekte ilk muayene ve alan kararınız ne olmalıdır?',
             'options': [{'text': 'Çocuğu tamamen soyarak lezyonlara cam bardakla bası testi uygulamak; '
                                  'kapiller dolum zamanı, bilinç durumu ve periferik nabızları değerlendirip '
                                  'hastayı derhal Sarı Alana devretmek',
                          'is_correct': True,
                          'triggers_yellow_transfer': True,
                          'explanation': 'Yüksek ateş, basmakla solmayan peteşi/purpura, letarji ve uzamış '
                                         'kapiller dolum zamanı fulminan seyirli invaziv bakteriyel '
                                         'enfeksiyon ve kompanse şokun alarm bulgularıdır; hasta saniyeler '
                                         'içinde Sarı/Kırmızı Alana alınmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 39.4°C, KTA 178/dk, SS 42/dk, TA 82/45 mmHg, '
                                         'SpO2 %95. Alt ekstremitelerde ve gövde altında basmakla solmayan '
                                         '2-4 mm peteşi ve erken ekimotik purpurik lezyonlar mevcut! '
                                         'Ekstremiteler soğuk, kapiller dolum zamanı 4 saniye, çocuk uykuya '
                                         'meyilli. Hasta derhal Sarı Alana devredildi!'},
                         {'text': 'Ateşi düşürüp taşikardi ve halsizliğin gerileyip gerilemediğini görmek '
                                  'amacıyla Yeşil Alanda oral parasetamol süspansiyon verip ılık uygulama '
                                  'yapmak ve 1 saat sonra yeniden değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Kritik 1 saatlik bekleme süresinde bacaklardaki mor lekeler '
                                             'hızla tüm gövdeye yayıldı, kapiller dolum 6 saniyeye çıktı ve '
                                             'hipotansif şok gelişti!',
                          'teaching_point': 'Ateşli bir çocukta basmakla solmayan peteşi/purpura ve '
                                            'perfüzyon bozukluğu varlığında antipiretik yanıtı beklenmez; '
                                            'dakikalar içinde resüsitasyon başlatılmalıdır.'},
                         {'text': 'Bacaklardaki döküntüleri viral ekzantem veya kusmaya bağlı mekanik peteşi '
                                  'olarak değerlendirip Yeşil Alanda tam kan sayımı ve idrar tetkiki '
                                  'isteyerek bekleme salonunda sonuçları beklemek',
                          'is_correct': False,
                          'scenario_update': 'Bekleme salonunda geçen 45 dakika içinde purpuralar birleşerek '
                                             'ekimotik plaklara dönüştü ve çocukta bilinç kaybı gelişti.',
                          'teaching_point': 'Kusmaya bağlı mekanik peteşiler yalnızca üst kaval kemiği '
                                            'hattının üzerinde, baş-boyun bölgesinde görülür; alt '
                                            'ekstremitedeki ateşli peteşi/purpura invaziv sepsis '
                                            'göstergesidir.'},
                         {'text': 'Yüksek ateş ve uykuya meyil öyküsü nedeniyle santral sinir sistemi '
                                  'enfeksiyonunu doğrulamak üzere Yeşil Alanda sedasyon hazırlığı yaparak '
                                  'öncelikle tanısal lomber ponksiyon işlemi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Dolaşım bozukluğu ve olası koagülopatisi olan hastada '
                                             'resüsitasyon yapılmadan denenen lomber ponksiyon '
                                             'kardiyorespiratuar kollapsı tetikledi.',
                          'teaching_point': 'Perfüzyon bozukluğu (soğuk ekstremite, uzamış KDZ, letarji) ve '
                                            'yaygın purpura varlığında lomber ponksiyon kontrendikedir; önce '
                                            'ABC stabilizasyonu ve antibiyotik uygulanır.'}]},
            {'stage_title': 'Sarı Alanda İlk Saat Resüsitasyon ve Tetkik Yaklaşımı',
             'question': 'Hastayı Sarı Alana aldınız ve monitörize ettiniz. İlk 15-30 dakikadaki en doğru '
                         'müdahale ve tetkik sırası nedir?',
             'options': [{'text': 'Beyin omurilik sıvısı kültürünün steril kalmasını önlemek amacıyla '
                                  'antibiyotik ve sıvı bolusu vermeden önce acil lomber ponksiyon uygulamak, '
                                  'ardından kraniyal bilgisayarlı tomografi görüntülemesine göndermek',
                          'is_correct': False,
                          'scenario_update': 'Hemodinamisi unstabil ve trombositopenisi/koagülopatisi olan '
                                             'hastada LP ve BT için antibiyotiğin geciktirilmesi şoku '
                                             'derinleştirdi ve spinal hematom riski yarattı!',
                          'teaching_point': 'Şok bulguları ve purpura/koagülopati varlığında lomber '
                                            'ponksiyon kesinlikle yapılmaz; parenteral antibiyotik tedavisi '
                                            'LP veya görüntüleme için geciktirilemez.'},
                         {'text': 'Oksijen başlayıp damar yolu açarak kan kültürü, hemogram, koagülasyon, '
                                  'prokalsitonin ve kan gazı almak; beklemeksizin intravenöz seftriakson ve '
                                  '20 mL/kg izotonik kristaloid bolusu uygulamak',
                          'is_correct': True,
                          'explanation': 'Pediatrik sepsis kılavuzlarına göre damar yolu açılır açılmaz kan '
                                         'kültürü alınır, lomber ponksiyon beklenmeden ilk saat içinde '
                                         'intravenöz seftriakson (100 mg/kg/gün dozunda) ve 20 mL/kg %0.9 '
                                         'NaCl bolusu verilir.',
                          'new_finding': 'Damar yolu açıldı, kan kültürü alındı ve ilk doz intravenöz '
                                         'seftriakson + 20 mL/kg %0.9 NaCl bolusu uygulandı. LABORATUVAR: '
                                         'WBC 21.400/mm³, PLT 88.000/mm³, CRP 115 mg/L, Prokalsitonin 18 '
                                         "ng/mL, Laktat 4.1 mmol/L, INR 1.6. Bolus sonrası KTA 145/dk'ya, "
                                         'KDZ 2 saniyeye geriledi.'},
                         {'text': 'Kan basıncı henüz 82/45 mmHg düzeyinde korunduğu için intravenöz sıvı '
                                  'bolusu vermekten kaçınmak; yalnızca idame hızında sıvı başlayıp kültür ve '
                                  'koagülasyon sonuçları çıkınca antibiyotik seçmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuklarda hipotansiyon şokun çok geç bir bulgusudur; bolus '
                                             'verilmeyen ve antibiyotiği bekletilen hastada 30 dakika içinde '
                                             'dekompanse hipotansif şok gelişti.',
                          'teaching_point': 'Pediatrik kompanse şokta taşikardi, uzamış kapiller dolum ve '
                                            'soğuk ekstremite varlığında hipotansiyon gelişmesi beklenmeden '
                                            'derhal 20 mL/kg izotonik sıvı bolusu ve ampirik seftriakson '
                                            'başlanmalıdır.'},
                         {'text': 'Trombositopeni ve purpurik döküntülerin immün aracılı olabileceği '
                                  'düşüncesiyle antibiyotik başlamadan önce intravenöz immünglobulin ve '
                                  'yüksek doz metilprednizolon infüzyonu hazırlayarak acil çocuk hematoloji '
                                  'konsültasyonu istemek',
                          'is_correct': False,
                          'scenario_update': 'Akut bakteriyel sepsis ve dissemine intravasküler koagülasyon '
                                             'tablosunda antibiyotik yerine immünsüpresif steroid verilmesi '
                                             'bakteriyemiyi hızlandırdı.',
                          'teaching_point': 'Yüksek ateş, letarji ve şok bulguları eşliğindeki akut purpura '
                                            've trombositopeni aksi kanıtlanana kadar invaziv bakteriyel '
                                            'sepsis ve DİK olarak yönetilir.'}]},
            {'stage_title': 'Sarı Alanda Kesin Tanı',
             'question': 'Klinik tablo ve laboratuvar bulguları (lökositoz, trombositopeni, yüksek '
                         'prokalsitonin/laktat, INR uzaması ve ateşli purpura) ile kesin tanınız nedir?',
             'options': [{'text': 'Henoch-Schönlein Purpurası (IgA Vasküliti)',
                          'is_correct': False,
                          'scenario_update': 'IgA vaskülitinde çocuk toksik görünmez, septik şok gelişmez ve '
                                             'trombosit sayısı ile koagülasyon parametreleri tamamen '
                                             'normaldir.',
                          'teaching_point': 'Yüksek ateş, şok bulguları, yüksek prokalsitonin ve '
                                            'trombositopeni/koagülopati varlığında purpura vaskülit değil '
                                            'meningokoksemi ve DİK lehinedir.'},
                         {'text': 'Akut İmmün Trombositopenik Purpura (İTP)',
                          'is_correct': False,
                          'scenario_update': "İTP'de genel durumu çok iyi olan afebril çocukta izole "
                                             'trombositopeni görülür; lökositoz, INR uzaması, laktat '
                                             'yüksekliği ve şok bulunmaz.',
                          'teaching_point': 'Toksik görünüm, 39.4°C ateş, yüksek akut faz reaktanları ve '
                                            'koagülopati İTP tanısını kesin olarak dışlar.'},
                         {'text': 'Meningokoksemi ve Septik Şok',
                          'is_correct': True,
                          'explanation': 'Akut yüksek ateş, alt ekstremitelerden hızla yayılan basmakla '
                                         'solmayan peteşi/purpura, taşikardi, uzamış KDZ, hiperlaktatemi ve '
                                         'tüketim koagülopatisi Meningokoksemi ve kompanse septik şok için '
                                         'tanısaldır.',
                          'new_finding': 'Kesin Tanı: Meningokoksemi (İnvaziv Meningokokal Hastalık) ve '
                                         'Kompanse Septik Şok.'},
                         {'text': 'Tipik Hemolitik Üremik Sendrom (HÜS)',
                          'is_correct': False,
                          'scenario_update': 'Öyküde kanlı ishal prodromu olmayıp birkaç saat içinde '
                                             'hiperakut başlayan yüksek ateş, yaygın purpura ve septik şok '
                                             'tablosu mevcuttur.',
                          'teaching_point': 'HÜS genellikle kanlı ishal sonrası solukluk, oligo-anüri ve '
                                            'normal koagülasyon (INR normal) ile seyreder; hiperakut ateşli '
                                            'purpura ve şok meningokoksemidir.'}]},
            {'stage_title': 'İzlem, İzolasyon ve Temaslı Kemoprofilaksisi',
             'question': 'İlk resüsitasyonu yapılan bu meningokoksemi hastasında yatış, izolasyon ve halk '
                         'sağlığı yönetimi nasıl olmalıdır?',
             'options': [{'text': 'Sıvı bolusu sonrası kapiller dolum zamanı düzeldiği için hastayı '
                                  'izolasyonsuz genel pediatri servisine yatırmak ve yalnızca ateş gelişen '
                                  'aile bireylerine oral amoksisilin profilaksisi önermek',
                          'is_correct': False,
                          'scenario_update': 'Genel serviste izlenen hastada 4. saatte dirençli hipotansiyon '
                                             've adrenal yetmezlik gelişti; ayrıca amoksisilin nazofaringeal '
                                             'meningokok taşıyıcılığını eradike edemedi.',
                          'teaching_point': 'Meningokoksemi hastaları Çocuk Yoğun Bakım Ünitesinde damlacık '
                                            'izolasyonu altında izlenmeli ve tüm ev içi temaslılara '
                                            'asemptomatik olsalar dahi rifampisin, seftriakson veya '
                                            'siprofloksasin ile kemoprofilaksi verilmelidir.'},
                         {'text': 'İlk doz intravenöz seftriakson ve sıvı resüsitasyonu sonrası vital '
                                  'bulguları stabilize olan hastayı 6 saat acil gözlemde tutup günlük '
                                  'intramüsküler seftriakson tedavisiyle ayaktan kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Meningokoksemi ve erken DİK tablosundaki hastanın taburcu '
                                             'edilmesi saatler içinde gelişebilecek Waterhouse-Friderichsen '
                                             'sendromu nedeniyle ölümcül risk oluşturdu.',
                          'teaching_point': 'Meningokoksemi şüphesi veya tanısı olan hiçbir hasta acil '
                                            'servisten taburcu edilemez; yoğun bakım şartlarında yakın '
                                            'monitörizasyon zorunludur.'},
                         {'text': 'Hava yolu (negatif basınçlı oda) izolasyonu altında Çocuk Yoğun Bakım '
                                  'Ünitesine yatırmak ve hastanın kreş ile ev içi temaslılarına 10 gün '
                                  'süreyle oral trimetoprim-sülfametoksazol profilaksisi başlamak',
                          'is_correct': False,
                          'scenario_update': 'Neisseria meningitidis hava yoluyla değil büyük damlacıklarla '
                                             'bulaşır ve trimetoprim-sülfametoksazol meningokok '
                                             'kemoprofilaksisinde önerilen bir ajan değildir.',
                          'teaching_point': 'Meningokok enfeksiyonlarında etkili antibiyotik tedavisinin ilk '
                                            '24 saati boyunca damlacık izolasyonu uygulanır; '
                                            'kemoprofilakside rifampisin (2 gün), tek doz İM seftriakson '
                                            'veya erişkinde tek doz siprofloksasin kullanılır.'},
                         {'text': 'Damlacık izolasyonuyla Çocuk Yoğun Bakım Ünitesine yatırmak, hemodinamik '
                                  've DİK izlemi yapmak, zorunlu bildirimde bulunup ev içi temaslılara '
                                  'rifampisin veya seftriakson kemoprofilaksisi planlamak',
                          'is_correct': True,
                          'explanation': 'Meningokoksemi hastası ilk 24 saat damlacık izolasyonu ile Çocuk '
                                         'Yoğun Bakım Ünitesinde izlenmeli, Sağlık Bakanlığı bildirimi '
                                         'yapılmalı ve yakın temaslılara en kısa sürede (tercihen ilk 24 '
                                         'saatte) kemoprofilaksi başlanmalıdır.',
                          'new_finding': 'Hasta damlacık izolasyonu altında Çocuk Yoğun Bakım Ünitesine '
                                         'yatırıldı ve ev içi yakın temaslılara kemoprofilaksi '
                                         'düzenlendi.'}]}]},
 {'id': 'G19',
  'category': '🫁 Hırıltı & Solunum Sıkıntısı',
  'age': '4.5 Aylık',
  'gender': 'Erkek',
  'complaint': 'Burun tıkanıklığı, öksürük ve bugün başlayan hızlı nefes alıp verme',
  'history': "Annesi Yeşil Alana 'nezlesi ve öksürüğü var, şurup yazdırmak istiyorum' diyerek getiriyor: '3 "
             'gündür burnu akıyordu ve hapşırıyordu. Ama bu sabahtan beri nefes alırken karnı ve '
             'kaburgalarının arası içeri çöküyor, memeyi ağzına alıp 2-3 kez çekip nefes alamadığı için '
             "bırakıyor. Bez sayısı da bugün yarıya düştü.'",
  'final_diagnosis': 'Orta-Ağır Akut Bronşiolit (Hipoksemik ve Beslenme Güçlüğü Olan Süt Çocuğu)',
  'disposition': 'Yeşil Alanda Saptanıp Sarı Alana Devir -> Oksijen, Nazal Aspirasyon ve Hidrasyon -> '
                 'Pediatri Servis Yatışı',
  'case_pearl': '<2 yaş (özellikle <6 ay) bebeklerde viral ÜSYE prodromu sonrası gelişen ilk hışıltı '
                "(wheezing), takipne ve çekilme Akut Bronşiolittir. Yeşil alana 'öksürük/nezle' diye "
                'başvuran süt çocuklarında göğüs duvarı soyularak solunum sayısı, çekilmeler ve SpO2 mutlaka '
                'ölçülmelidir. SpO2 <%90-92, belirgin çekilme, takipne (>60/dk) ve beslenememe Sarı Alana '
                'devir ve yatış endikasyonudur.',
  'steps': [{'stage_title': 'Yeşil Alanda Solunum Değerlendirmesi ve Alan Kararı',
             'question': 'Yeşil alana öksürük ve burun tıkanıklığı ile getirilen bu 4.5 aylık bebekte ilk '
                         'muayene ve alan kararınız ne olmalıdır?',
             'options': [{'text': 'Üst solunum yolu enfeksiyonuna bağlı burun tıkanıklığı düşünerek Yeşil '
                                  'Alanda serum fizyolojik burun damlası uygulamak ve oksijen satürasyonu '
                                  'ölçmeden anneye bebeği emzirmesini söyleyerek bekletmek',
                          'is_correct': False,
                          'scenario_update': 'Göğsü açılmayan ve SpO2 ölçümü yapılmayan bebekte emzirme '
                                             'sırasında şiddetli desatürasyon ve morarma gelişti.',
                          'teaching_point': 'Öksürük, emmeme ve hızlı nefes alma öyküsü olan her süt '
                                            'çocuğunda göğüs tamamen açılarak çekilmeler değerlendirilmeli '
                                            've pulse oksimetre ile SpO2 ölçülmelidir.'},
                         {'text': 'Bebeğin göğüs duvarını açarak solunum sayısını, interkostal-subkostal '
                                  'çekilmeleri, oskültasyon bulgularını ve oda havasında SpO2 değerini ölçüp '
                                  'hastayı Sarı Alana devretmek',
                          'is_correct': True,
                          'triggers_yellow_transfer': True,
                          'explanation': 'Süt çocuğunda takipne (>60/dk), interkostal/subkostal çekilme, '
                                         'beslenememe ve hipoksemi akut alt solunum yolu obstrüksiyonunun '
                                         'ağırlaştığını gösterir; hasta derhal Sarı Alana devredilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.9°C, KTA 156/dk, Solunum Sayısı 64/dk, Oda '
                                         'havasında SpO2 %89. Belirgin subkostal ve interkostal çekilmeler '
                                         'ile burun kanadı solunumu mevcut. Oskültasyonda ekspiryum uzun, '
                                         'bilateral yaygın sibilan ronküsler ve ince krepitan raller '
                                         'duyuluyor. Hasta Sarı Alana devredildi!'},
                         {'text': 'Oskültasyonda duyulan sibilan ronküsler nedeniyle hastayı Yeşil Alanda '
                                  'tutarak 20 dakika arayla 3 doz nebülize salbutamol uygulamak ve oral '
                                  'prednizolon şurup vererek yanıtı beklemek',
                          'is_correct': False,
                          'scenario_update': 'Oksijen desteği verilmeden Yeşil Alanda uygulanan ardışık '
                                             "salbutamol nebülleri bebeğin taşikardisini 190/dk'ya çıkardı, "
                                             "SpO2 %88'de kaldı ve solunum iş yükü azalmadı.",
                          'teaching_point': 'Hipoksemik (SpO2 <%90) süt çocuğu Yeşil Alanda tutulamaz; '
                                            'ayrıca küçük süt çocuklarının ilk viral alt solunum yolu '
                                            'hışıltısında rutin bronkodilatör ve steroid önerilmez.'},
                         {'text': 'Öksürük ve hızlı solunumu bakteriyel pnömoni başlangıcı kabul ederek '
                                  'Yeşil Alanda PA akciğer grafisi istemek ve oral amoksisilin-klavulanat '
                                  'ile dekstrometorfan şurup reçete edip eve göndermek',
                          'is_correct': False,
                          'scenario_update': 'Hipoksemik ve beslenemeyen 4.5 aylık bebekte solunum '
                                             'yetmezliği riski atlandı ve süt çocuklarında kontrendike olan '
                                             'antitussif şurup reçete edildi.',
                          'teaching_point': 'Süt çocuklarında öksürük kesici (antitussif/mukolitik) ilaçlar '
                                            'kesinlikle kontrendikedir; hipoksemik bebek acil gözleme '
                                            'alınmalıdır.'}]},
            {'stage_title': 'Sarı Alanda Stabilizasyon ve Tedavi Yaklaşımı',
             'question': 'Sarı Alana devraldığınız (SpO2 %89, SS 64/dk, çekilmeleri olan ve ememeyen) bu 4.5 '
                         'aylık bebekte kanıta dayalı ilk müdahale ne olmalıdır?',
             'options': [{'text': 'Rutin olarak tam kan sayımı, CRP ve akciğer grafisi çekmek; intravenöz '
                                  'metilprednizolon, ampisilin-sulbaktam ve sekresyon mobilizasyonu için '
                                  'agresif göğüs fizyoterapisi (tapotman) uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Agresif göğüs perküsyonu/tapotman bebeğin ağlamasını ve '
                                             'oksijen tüketimini artırarak desatürasyonu derinleştirdi; '
                                             'steroid ve antibiyotik klinik fayda sağlamadı.',
                          'teaching_point': 'Güncel uluslararası kılavuzlarda viral alt hava yolu '
                                            'obstrüksiyonunda rutin akciğer grafisi, kan tetkiki, '
                                            'sistemik/inhale kortikosteroidler, antibiyotikler ve göğüs '
                                            'fizyoterapisi önerilmemektedir.'},
                         {'text': 'Solunum sayısı 64/dk iken dehidratasyonu önlemek amacıyla bebeği '
                                  'biberonla beslemeye devam etmek ve eş zamanlı ardışık nebülize '
                                  'ipratropium bromür ile salbutamol kombinasyonu uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Dakikada 64 kez nefes alan bebekte emme-yutma-solunum '
                                             'koordinasyonu bozulduğu için mama aspirasyonu ve akut '
                                             'desatürasyon gelişti!',
                          'teaching_point': 'Solunum sayısı >60/dk olan süt çocuklarında aspirasyon riski '
                                            'çok yüksektir; takipne gerileyene kadar ağızdan beslenme '
                                            'kesilerek intravenöz veya nazogastrik hidrasyon sağlanmalıdır.'},
                         {'text': 'Başı 30 derece yükseltip nazal aspirasyon yapmak, SpO2 >%92 tutacak '
                                  'şekilde oksijen başlamak ve aspirasyon riski nedeniyle oral beslenmeyi '
                                  'kesip intravenöz hidrasyon sağlamak',
                          'is_correct': True,
                          'explanation': 'Zorunlu burun solunumu yapan süt çocuklarında yüzeyel nazal '
                                         'aspirasyon üst hava yolu direncini düşürür; SpO2 <%90-92 olduğunda '
                                         'oksijen desteği ve SS >60/dk iken intravenöz/NG hidrasyon '
                                         'tedavinin kanıtlanmış temel taşlarıdır.',
                          'new_finding': 'Yüzeyel nazal aspirasyon ve 2 L/dk nemlendirilmiş oksijen desteği '
                                         "sonrası bebeğin SpO2 değeri %96'ya yükseldi, solunum sayısı "
                                         "54/dk'ya geriledi. Damar yolu açılarak izotonik idame sıvı "
                                         'tedavisi başlandı.'},
                         {'text': 'Nazal aspirasyon yapmadan doğrudan derin endotrakeal aspirasyon '
                                  'uygulamak, rutin arteriyel kan gazı almak ve solunum iş yükünü baskılamak '
                                  'amacıyla düşük doz intravenöz midazolam sedasyonu başlamak',
                          'is_correct': False,
                          'scenario_update': 'Derin aspirasyon mukozal ödeme ve laringospazma yol açarken, '
                                             'verilen sedatif solunum dürtüsünü baskılayarak apne atağı '
                                             'tetikledi!',
                          'teaching_point': 'Derin nazofaringeal/trakeal aspirasyon mukozal travma ve '
                                            'refleks bradikardi/apne yaptığı için önerilmez; entübe olmayan '
                                            'solunum sıkıntılı süt çocuğuna sedatif verilmez.'}]},
            {'stage_title': 'Sarı Alanda Kesin Tanı',
             'question': 'Mevcut anamnez ve fizik muayene bulgularıyla bu 4.5 aylık bebekte kesin tanınız '
                         'nedir?',
             'options': [{'text': 'Orta-Ağır Akut Bronşiolit',
                          'is_correct': True,
                          'explanation': '4.5 aylık süt çocuğunda 3 günlük viral ÜSYE prodromu sonrası '
                                         'gelişen ilk wheezing/ince ral atağı, takipne (64/dk), çekilmeler, '
                                         'hipoksemi (SpO2 %89) ve beslenme güçlüğü Orta-Ağır Akut Bronşiolit '
                                         'tanısını koydurur.',
                          'new_finding': 'Kesin Tanı: Orta-Ağır Akut Bronşiolit.'},
                         {'text': 'Akut Viral Laringotrakeit (Krup)',
                          'is_correct': False,
                          'scenario_update': 'Hastada inspiratuar stridor ve havlar tarzda kaba öksürük '
                                             'değil, ekspiryum uzaması, yaygın sibilan ronküsler ve ince '
                                             'krepitan raller mevcuttur.',
                          'teaching_point': 'Krup üst hava yolu (subglottik) darlığıdır ve inspiratuar '
                                            'stridorla seyreder; bronşiolit ise alt solunum yollarının '
                                            '(bronşiollerin) obstrüksiyonudur.'},
                         {'text': 'Bronşiyal Yabancı Cisim Aspirasyonu',
                          'is_correct': False,
                          'scenario_update': 'Henüz ek gıdaya geçmemiş 4.5 aylık bebekte ani başlayan '
                                             'boğulma/öksürük krizi öyküsü olmayıp 3 günlük rinit prodromu '
                                             've bilateral simetrik oskültasyon bulguları vardır.',
                          'teaching_point': 'Viral prodrom ve bilateral simetrik sibilan ronküs/ince raller '
                                            'akut bronşiolit lehinedir; yabancı cisim aspirasyonunda ani '
                                            'başlangıç ve asimetrik solunum sesleri beklenir.'},
                         {'text': 'Akut Bakteriyel Lober Pnömoni',
                          'is_correct': False,
                          'scenario_update': 'Bebekte toksik görünüm, yüksek ateş veya fokal konsolidasyon '
                                             '(bronşiyal solunum sesi/matite) yerine yaygın bilateral '
                                             'sibilan ronküsler ve ekspiryum uzaması ön plandadır.',
                          'teaching_point': 'Subfebril ateş ve yaygın bilateral wheezing/ince raller süt '
                                            'çocuğunda viral bronşiolit için tipiktir.'}]},
            {'stage_title': 'Sarı Alanda Yatış ve İzlem Kararı',
             'question': 'Oda havasında hipoksemisi (SpO2 %89), takipnesi ve beslenme güçlüğü olan 4.5 aylık '
                         'bu bebekte son kararınız ne olmalıdır?',
             'options': [{'text': "Oksijen altında SpO2 değeri %96'ya yükseldiği için oksijen desteğini "
                                  'kesip evde kullanmak üzere nebülize salbutamol ve budesonid reçete ederek '
                                  '24 saat sonra poliklinik kontrolüyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Oksijen kesildikten 20 dakika sonra bebeğin SpO2 değeri tekrar '
                                             "%88'e düştü, subkostal çekilmeleri arttı ve emmeyi reddetti.",
                          'teaching_point': 'Oda havasında SpO2 <%90-92 olan ve oral alımı yarıdan fazla '
                                            'azalmış küçük süt çocuğu acil servisten taburcu edilemez.'},
                         {'text': 'Acil gözlemde tek doz intramüsküler deksametazon ve seftriakson '
                                  'uyguladıktan sonra 2 saat izleyip solunum sayısı 54/dk düzeyindeyken oral '
                                  'beslenmeye geçerek hastayı eve göndermek',
                          'is_correct': False,
                          'scenario_update': 'Etkisiz medikal tedavilerle eve gönderilen bebek gece solunum '
                                             'yorgunluğu ve dehidratasyon nedeniyle acil servise yeniden '
                                             'getirildi.',
                          'teaching_point': 'Orta-ağır bronşiolitte parenteral steroid veya antibiyotik '
                                            'yatış ihtiyacını ortadan kaldırmaz; hasta oksijen ve hidrasyon '
                                            'desteği için yatırılmalıdır.'},
                         {'text': 'Rutin olarak tüm orta-ağır bronşiolit hastalarına uygulanan erken '
                                  'endotrakeal entübasyon ve mekanik ventilasyon amacıyla bebeği doğrudan '
                                  'üçüncü basamak yoğun bakım ünitesine entübe ederek nakletmek',
                          'is_correct': False,
                          'scenario_update': "Nazal aspirasyon ve düşük akımlı oksijenle SpO2'si %96'ya "
                                             'çıkan ve apnesi olmayan bebekte gereksiz invaziv mekanik '
                                             'ventilasyon girişimi planlandı.',
                          'teaching_point': 'Düşük akımlı oksijen veya HFNC ile stabilize olan, apnesi ve '
                                            'hiperkapnik solunum yetmezliği bulunmayan orta-ağır bronşiolit '
                                            'vakaları genel pediatri servisinde izlenir.'},
                         {'text': 'Oda havasında hipoksemisi, takipnesi ve beslenme güçlüğü süren 4.5 aylık '
                                  'bebeği oksijen desteği, hidrasyon ve yakın solunum/apne izlemi amacıyla '
                                  'Pediatri servisine yatırmak',
                          'is_correct': True,
                          'explanation': 'Oda havasında SpO2 <%90-92 olması, orta-ağır solunum sıkıntısı '
                                         '(belirgin çekilmeler, takipne) ve oral beslenmenin yarıdan fazla '
                                         'azalması kesin hastane yatış endikasyonudur.',
                          'new_finding': 'Bebek nemlendirilmiş oksijen ve intravenöz hidrasyon desteği '
                                         'altında Çocuk Sağlığı ve Hastalıkları servisine yatırıldı.'}]}]},
 {'id': 'G20',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '7 Yaş',
  'gender': 'Erkek',
  'complaint': 'Kaşıntı, kızarıklık ve yeni başlayan öksürük / kusma',
  'history': "Babası Yeşil Alana 'alerji oldu, kaşınıyor' diyerek getiriyor: 'Yarım saat önce doğum günü "
             'partisinde fıstıklı pasta yemişti. Önce boynunda ve kollarında kaşıntılı kabarıklıklar çıktı. '
             'Yeşil alan sırasında beklerken 2 kez kustu, şimdi de boğazım daralıyor diyor, sesi biraz '
             "çatallı çıkıyor ve kuru kuru öksürmeye başladı.'",
  'final_diagnosis': 'Anafilaksi (Besin Alerjeni Tetikli Çoklu Sistem Tutulumu)',
  'disposition': 'Yeşil Alanda Saptanıp Derhal Sarı/Kırmızı Alana Devir -> Acil İM Adrenalin -> Gözlem ve '
                 'Adrenalin Oto-enjektör Reçetesi',
  'case_pearl': 'Bilinen veya olası bir alerjen maruziyeti sonrası dakikalar-saatler içinde başlayan '
                'deri/mukoza bulgularına (ürtiker, anjiyoödem, kaşıntı) SOLUNUM (stridor, ses kısıklığı, '
                'wheezing, dispne), DOLAŞIM (hipotansiyon, taşikardi, senkop) veya GİS (dirençli kusma, '
                'kramp tarzı karın ağrısı) bulgularından en az birinin eşlik etmesi ANAFİLAKSİDİR! İlk ve '
                'hayat kurtarıcı tedavi uyluk anterolateraline (vastus lateralis) İM Adrenalin (0.01 mg/kg, '
                '1:1000) uygulanmasıdır.',
  'steps': [{'stage_title': 'Yeşil Alanda Değerlendirme ve Acil Müdahale Kararı',
             'question': 'Yeşil alana kaşıntı ve döküntü şikayetiyle giren ancak kusma, ses boğukluğu ve '
                         'öksürük eklenen bu 7 yaşındaki çocukta ilk kararınız ne olmalıdır?',
             'options': [{'text': 'Hastayı Sarı Alana devredip periferik damar yolu açarak öncelikle '
                                  'intravenöz feniramin ve 1-2 mg/kg metilprednizolon uygulamak, yalnızca '
                                  'arteriyel hipotansiyon gelişirse intramüsküler adrenalin planlamak',
                          'is_correct': False,
                          'scenario_update': 'Antihistaminik ve etkisi saatler sonra başlayan kortikosteroid '
                                             'laringeal ödemi durduramadı; hastanın stridoru artarak SpO2 '
                                             "değeri %84'e geriledi!",
                          'teaching_point': 'Çoklu sistem tutulumu ve hava yolu obstrüksiyonu bulgularında '
                                            'adrenalin için hipotansiyon gelişmesi beklenmez; antihistaminik '
                                            've steroidler adrenalinin yerini asla tutmaz.'},
                         {'text': 'Yeşil Alanda oral setirizin şurup ve soğuk buhar uygulayarak 30 dakika '
                                  'beklemek, kusması devam ederse intramüsküler ondansetron yapıp klinik '
                                  'semptomların gerileyip gerilemediğini kontrol etmek',
                          'is_correct': False,
                          'scenario_update': 'Oral antihistaminik ve antiemetik ile Yeşil Alanda bekletilen '
                                             'çocukta dakikalar içinde tam üst hava yolu obstrüksiyonu ve '
                                             'hipoksik bradikardi gelişti!',
                          'teaching_point': 'Alerjen maruziyeti sonrası deri bulgularına solunum ve '
                                            'gastrointestinal semptomların eklenmesi hayatı tehdit eden '
                                            'sistemik reaksiyonu gösterir; Yeşil Alanda bekletilemez.'},
                         {'text': 'Çoklu sistem tutulumu (deri-mukoza, gastrointestinal ve akut solunum '
                                  'obstrüksiyonu) saptayarak hastayı Sarı/Kırmızı Alana devretmek ve vastus '
                                  'lateralis kas içine 0.01 mg/kg adrenalin uygulamak',
                          'is_correct': True,
                          'triggers_yellow_transfer': True,
                          'explanation': 'Şüpheli besin alımı sonrası dakikalar içinde gelişen ürtiker + '
                                         'tekrarlayan kusma + laringeal/bronşiyal obstrüksiyon bulgularında '
                                         'ilk ve hayat kurtarıcı basamak uyluk üst-dış yanından (vastus '
                                         'lateralis) intramüsküler 0.01 mg/kg (1:1000) adrenalin uygulanması '
                                         've Sarı/Kırmızı Alana devirdir.',
                          'new_finding': 'Vital Bulgular: KTA 142/dk, SS 32/dk, TA 88/52 mmHg, SpO2 %92. '
                                         'Yaygın ürtiker plakları, alt dudakta ödem, seste boğukluk, '
                                         'inspiratuar stridor ve bilateral ekspiratuar wheezing mevcut. '
                                         'Hasta derhal Sarı Alana alındı ve sol uyluk anterolateralinden '
                                         '0.25 mg intramüsküler adrenalin uygulandı!'},
                         {'text': 'Solunum seslerindeki boğukluk ve hışıltıyı akut bronkospazm olarak '
                                  'değerlendirip Yeşil Alanda yalnızca ardışık nebülize salbutamol ve inhale '
                                  'budesonid uygulayarak hastayı oturur pozisyonda yakından izlemek',
                          'is_correct': False,
                          'scenario_update': 'Nebülize salbutamol üst hava yolundaki (laringeal) anjiyoödemi '
                                             've sistemik mediyatör salınımını engelleyemediği için stridor '
                                             've dolaşım bozukluğu ilerledi.',
                          'teaching_point': 'İnhale beta-2 agonistler laringeal ödemi ve mukozal kapiller '
                                            'sızıntıyı düzeltmez; birincil tedavi alfa-1 ve beta-2 agonisti '
                                            'olan intramüsküler adrenalindir.'}]},
            {'stage_title': 'Sarı Alanda İkincil Destek ve Resüsitasyon Yönetimi',
             'question': 'Sarı Alanda ilk doz intramüsküler adrenalin uygulandı. Bu aşamada eş zamanlı '
                         'yapılması gereken doğru destek tedavileri nelerdir?',
             'options': [{'text': 'Uygun pozisyon verip oksijen başlamak, damar yolu açarak 20 mL/kg '
                                  'izotonik kristaloid, bronkospazm için nebülize salbutamol ve yardımcı '
                                  'olarak H1-antihistaminik ile metilprednizolon uygulamak',
                          'is_correct': True,
                          'explanation': 'İntramüsküler adrenalin sonrası hava yolu/oksijen desteği, damar '
                                         'yolu açılarak intravasküler hacim desteği (%0.9 NaCl), alt hava '
                                         'yolu obstrüksiyonu için nebülize salbutamol ve ikincil ilaçlar '
                                         'uygulanır; 5-15 dakikada yanıt değerlendirilir.',
                          'new_finding': 'İntramüsküler adrenalin, oksijen, izotonik sıvı desteği ve '
                                         'nebülize salbutamol sonrası 8. dakikada ses boğukluğu ve wheezing '
                                         'düzeldi; SpO2 %99, TA 105/68 mmHg, KTA 110/dk ölçüldü.'},
                         {'text': 'İlk doz intramüsküler adrenalinden hemen 2 dakika sonra tam yanıt '
                                  'alınamadığı düşüncesiyle 1:1000 konsantrasyondaki adrenalini '
                                  'sulandırmadan 0.25 mg dozunda hızlı intravenöz puşe olarak uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Sulandırılmamış (1:1000) adrenalinin hızlı intravenöz puşe '
                                             'yapılması şiddetli hipertansif kriz ve ventriküler taşikardi '
                                             'atağı tetikledi!',
                          'teaching_point': 'Adrenalin 5-15 dakika arayla intramüsküler olarak '
                                            'tekrarlanabilir; sulandırılmamış (1:1000) intravenöz puşe '
                                            'adrenalin ölümcül kardiyak aritmi ve miyokardiyal iskemiye yol '
                                            'açar.'},
                         {'text': 'Solunumunun rahatlaması ve kusmasının geçmesi için çocuğu sedyeden '
                                  'kaldırarak acil servis koridorunda yürütmek ve ağızdan bol su içirerek '
                                  'alerjenin mideden hızla temizlenmesini sağlamak',
                          'is_correct': False,
                          'scenario_update': 'Vazodilatasyon ve kapiller sızıntısı olan hastanın aniden '
                                             'ayağa kaldırılması venöz dönüşü düşürerek senkop ve hipotansif '
                                             'kollapsa neden oldu!',
                          'teaching_point': 'Akut sistemik alerjik reaksiyon sırasında hasta kesinlikle '
                                            'ayağa kaldırılmaz veya yürütülmez (boş ventrikül sendromu / ani '
                                            'kardiyak arrest riski); sırtüstü bacaklar yükseltilmiş veya '
                                            'solunum sıkıntısı varsa bacaklar uzatılarak yarı oturur '
                                            'pozisyonda tutulur.'},
                         {'text': 'Stridor ve wheezing bulguları devam ederken oksijen veya sıvı desteği '
                                  'vermeden önce kesin tanı koymak amacıyla serum triptaz düzeyi ve spesifik '
                                  'IgE sonuçları çıkana dek beklemek',
                          'is_correct': False,
                          'scenario_update': 'Laboratuvar sonucu beklenirken oksijen ve sıvı desteği '
                                             'geciktirildiği için hipoksemi ve taşikardi derinleşti.',
                          'teaching_point': 'Serum triptaz düzeyi tanıyı retrospektif desteklemek için '
                                            'alınabilir ancak sonuçları saatler-günler sürer; acil '
                                            'stabilizasyon hiçbir laboratuvar testi için bekletilmez.'}]},
            {'stage_title': 'Sarı Alanda Kesin Tanı',
             'question': 'Öykü, fizik muayene ve tedavi yanıtı birlikte değerlendirildiğinde bu hastada '
                         'kesin tanınız nedir?',
             'options': [{'text': 'İzole Akut Ürtiker ve Anjiyoödem',
                          'is_correct': False,
                          'scenario_update': 'Hastada yalnızca deri-mukoza bulguları değil, eş zamanlı ses '
                                             'boğukluğu/stridor, bilateral wheezing, hipoksemi ve '
                                             'tekrarlayan kusma mevcuttur.',
                          'teaching_point': 'Deri-mukoza bulgularına solunum, dolaşım veya şiddetli '
                                            'gastrointestinal sistem bulgularından en az birinin eşlik '
                                            'etmesi izole ürtiker değil anafilaksidir.'},
                         {'text': 'Akut Trakeobronşiyal Yabancı Cisim Aspirasyonu',
                          'is_correct': False,
                          'scenario_update': 'Fıstıklı pasta yedikten 30 dakika sonra yaygın ürtiker, dudak '
                                             'ödemi ve kusma ile başlayan ve intramüsküler adrenaline hızla '
                                             'yanıt veren tablo mevcuttur.',
                          'teaching_point': 'Yaygın ürtiker-anjiyoödem, kusma ve intramüsküler adrenaline '
                                            'dramatik yanıt mekanik obstrüksiyonu değil sistemik IgE aracılı '
                                            'anafilaksiyi gösterir.'},
                         {'text': 'Besin Kaynaklı Akut Bakteriyel Gastroenterit',
                          'is_correct': False,
                          'scenario_update': 'Enterotoksin kaynaklı besin zehirlenmesinde yaygın ürtiker, '
                                             'dudak anjiyoödemi, laringeal stridor ve bronkospazm görülmez.',
                          'teaching_point': 'Alerjen besin alımı sonrası dakikalar içinde gelişen kusmaya '
                                            'deri ve solunum yolu obstrüksiyonunun eşlik etmesi anafilaksi '
                                            'tanı kriteridir.'},
                         {'text': 'Besin Tetikli Akut Anafilaksi',
                          'is_correct': True,
                          'explanation': 'WAO/EAACI kriterlerine göre olası alerjen (yer fıstığı) maruziyeti '
                                         'sonrası dakikalar içinde başlayan deri/mukoza tutulumuna (ürtiker, '
                                         'dudak ödemi) solunum (stridor, wheezing, hipoksemi) ve GİS (kusma) '
                                         'bulgularının eşlik etmesi kesin Anafilaksi tanısı koydurur.',
                          'new_finding': 'Kesin Tanı: Besin (Yer Fıstığı) Tetikli Anafilaksi.'}]},
            {'stage_title': 'Gözlem Süresi ve Taburculuk Planı',
             'question': 'Tedavi sonrası semptomları tamamen düzelen bu anafilaksi hastasında gözlem süresi '
                         've taburculuk planı nasıl olmalıdır?',
             'options': [{'text': 'İntramüsküler adrenalin sonrası 15. dakikada tüm bulgular ve vital '
                                  'değerler tamamen normale döndüğü için oral antihistaminik reçete ederek '
                                  'hastayı 1. saatin sonunda eve taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Erken taburcu edilen hastada 5 saat sonra evde alerjenle yeni '
                                             'temas olmaksızın bifazik anafilaksi atağı gelişti ve evde '
                                             'oto-enjektör bulunmadığı için hayati tehlike yaşandı!',
                          'teaching_point': "Anafilaksi hastalarının %5-20'sinde ilk ataktan 4-24 saat sonra "
                                            'bifazik reaksiyon gelişebildiğinden hastalar en az 6-12 saat '
                                            '(ağır solunum/hipotansiyon varsa daha uzun) gözlemlenmelidir.'},
                         {'text': 'Bifazik reaksiyon riski nedeniyle hastayı en az 6-12 saat gözlemlemek; '
                                  'taburculukta adrenalin oto-enjektör reçete edip kullanım eğitimi, fıstık '
                                  'eliminasyonu ve Çocuk Alerji randevusu vermek',
                          'is_correct': True,
                          'explanation': 'Bifazik anafilaksi riski nedeniyle özellikle solunum/dolaşım '
                                         'tutulumu olan vakalar en az 6-12 saat izlenmeli; taburculukta 0.15 '
                                         'mg/0.30 mg kiloya uygun Adrenalin oto-enjektör reçetesi, yazılı '
                                         'eylem planı ve Çocuk Alerji yönlendirmesi mutlaka yapılmalıdır.',
                          'new_finding': 'Hasta Sarı Alanda 8 saat sorunsuz izlendi; Adrenalin oto-enjektör '
                                         'kullanım eğitimi, yazılı anafilaksi eylem planı ve Çocuk Alerji '
                                         'randevusu verilerek güvenle taburcu edildi.'},
                         {'text': 'Hastayı 8 saat gözlemledikten sonra sadece oral prednizolon ve '
                                  'desloratadin şurup reçete etmek, adrenalin oto-enjektör kararını 1 ay '
                                  'sonraki Çocuk Alerji poliklinik kontrolüne bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Poliklinik randevusunu bekleyen çocuk 10 gün sonra eser '
                                             'miktarda fıstık içeren bir bisküvi yedikten sonra evde tekrar '
                                             'anafilaksi geçirdi ve oto-enjektörü olmadığı için müdahale '
                                             'gecikti.',
                          'teaching_point': 'Besin tetikli anafilaksi geçiren her hastaya Adrenalin '
                                            'oto-enjektör acil servisten taburcu edilirken reçete edilmeli '
                                            've aileye uygulama pratiği gösterilmelidir.'},
                         {'text': 'Reaksiyonun gerçekten yer fıstığına bağlı olup olmadığını kesinleştirmek '
                                  'amacıyla taburculuk öncesinde acil gözlem odasında doktor gözetiminde '
                                  'düşük doz oral besin yükleme (provokasyon) testi yapmak',
                          'is_correct': False,
                          'scenario_update': 'Akut anafilaksi atağından hemen sonra acil serviste tekrar '
                                             'alerjen verilmesi şiddetli ve dirençli ikinci bir anafilaktik '
                                             'şok tablosunu tetikledi!',
                          'teaching_point': 'Acil serviste besin provokasyon testi kesinlikle yapılmaz; '
                                            'şüpheli besin diyetten tamamen çıkarılır ve tanısal testler '
                                            'ataktan en az 4-6 hafta sonra Çocuk Alerji kliniğinde '
                                            'planlanır.'}]}]}]
