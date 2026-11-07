# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Yeşil Alan Vakaları (Part 9: Y81 - Y90)
"""

GREEN_CASES_PART9 = [{'id': 'Y81',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '3 Yaşında',
  'gender': 'Kız',
  'complaint': 'Kollarında, dizlerinin arkasında ve boynunda kaşıntılı, pullu kızarıklıklar; geceleri kaşınmaktan '
               'uyuyamama',
  'history': "Annesi anlatıyor: 'Bebekliğinden beri yanaklarında ara ara kuruluk oluyordu. Bu kış çok arttı, dirsek ve "
             'diz içleri kıpkırmızı, geceleri kanatana kadar kaşıyor. Her gün köpüklü banyo yaptırıyorum, kremi seyrek '
             "sürüyorum. Kortizonlu krem verilmişti ama zararlı diye kullanmadım.' Ateş, sulu yara, içi su dolu "
             "kabarcık yok. Ailede babada astım ve saman nezlesi var. Komşu 'süt ve yumurtayı kesin' demiş.",
  'final_diagnosis': 'Atopik Dermatit Alevlenmesi (Orta Şiddet, Enfeksiyonsuz)',
  'disposition': 'Nemlendirici, Topikal Kortikosteroid ve Cilt Bakım Eğitimiyle Yeşil Alandan Taburculuk',
  'case_pearl': 'Atopik dermatit tanısı kliniktir. Kaşıntı, yaşa özgü dağılım (küçük çocukta yüz ve ekstansör yüzler, '
                'büyüklerde fleksural bölgeler), kronik-tekrarlayıcı seyir ve atopi öyküsü aranır. Rutin besin alerji '
                'testleri ve eliminasyon diyeti önerilmez. Tedavinin temeli bol nemlendiricidir. Alevlenmede gövdede '
                'orta potensli, yüzde düşük potensli topikal kortikosteroid günde bir kez 1-2 hafta, ardından haftada '
                'iki gün koruyucu kullanılır. Sarı kabuklanma, delinmiş görünümlü erozyonlar veya ateş enfeksiyonu '
                'düşündürür.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Kaşıntılı kızarıklıklarla gelen bu çocukta muayenede nelere dikkat edersiniz?',
             'options': [{'text': 'Lezyonların dağılımını, yaygınlığını ve kaşıntının uykuya etkisini değerlendirip '
                                  'sarı kabuk, delinmiş erozyon, vezikül ve ateş gibi enfeksiyon bulgularını aramak',
                          'is_correct': True,
                          'explanation': 'Dağılım ve yaygınlık şiddeti belirler. Bakteriyel veya viral süperenfeksiyon '
                                         'tedaviyi tamamen değiştirdiği için mutlaka aranmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, genel durum iyi. Dirsek ve diz fleksural '
                                         'yüzlerinde, boyun önünde ve el bileklerinde sınırları belirsiz, eritemli, '
                                         'kepeklenen, yer yer likenifiye plaklar ve kaşıntı izleri. Yüzde hafif '
                                         "kuruluk. Vücut yüzeyinin yaklaşık %15'i tutulmuş. Sarı kabuk, delinmiş "
                                         'görünümlü erozyon veya vezikül yok. Parmak araları ve el ayasında lezyon '
                                         'yok. Lenf nodları küçük.'},
                         {'text': 'Kızarıklıkları besin alerjisine bağlayıp muayeneyi kısa tutmak ve aileye süt ile '
                                  'yumurtayı hemen diyetten çıkarmalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Aile süt ve yumurtayı kesti; lezyonlar değişmedi, çocuğun kalsiyum alımı '
                                             'azaldı.',
                          'teaching_point': 'Kanıtlanmış bir besin alerjisi olmadan eliminasyon diyeti önerilmez; '
                                            'beslenme eksikliği riski taşır.'},
                         {'text': 'Kaşıntılı papüller nedeniyle tüm ailede kaşıntı olup olmadığını sormadan bulaşıcı '
                                  'bir parazit enfeksiyonu kabul edip tüm aileyi tedavi etmek',
                          'is_correct': False,
                          'scenario_update': 'Ailedeki kimsede kaşıntı yoktu; uygulanan tedavi cildi daha da tahriş '
                                             'etti.',
                          'teaching_point': 'Dağılım, parmak arası tutulumu ve ailede kaşıntı sorgulanmadan bu tanıya '
                                            'gidilmemelidir.'},
                         {'text': 'Lezyonların mantar olabileceğini düşünüp muayene sırasında yalnızca en belirgin '
                                  'plağa bakarak topikal antifungal krem önermek',
                          'is_correct': False,
                          'scenario_update': 'Antifungal krem kaşıntıyı azaltmadı; plaklar yaygınlaşmaya devam etti.',
                          'teaching_point': 'Simetrik fleksural tutulum ve kronik seyir mantar enfeksiyonundan '
                                            'farklıdır; tüm deri muayene edilmelidir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Enfeksiyon bulgusu olmayan bu çocukta hangi tetkik yaklaşımı uygundur?',
             'options': [{'text': 'Besin alerjenlerine karşı spesifik IgE paneli istemek ve pozitif çıkan tüm '
                                  'besinleri diyetten çıkarmak üzere aileyi bilgilendirmek',
                          'is_correct': False,
                          'scenario_update': 'Panelde süt ve yumurtaya düşük düzeyde IgE pozitifliği çıktı; klinik '
                                             'reaksiyon olmamasına rağmen besinler kesildi.',
                          'teaching_point': 'Duyarlılık klinik alerji demek değildir; rutin IgE paneli gereksiz diyet '
                                            'kısıtlamalarına yol açar.'},
                         {'text': 'Tüm lezyonlardan bakteri kültürü almak ve kültürde üreme olursa oral antibiyotik '
                                  'başlamak üzere kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Kültürde S. aureus üredi; enfeksiyon bulgusu olmayan çocukta gereksiz '
                                             'antibiyotik başlandı.',
                          'teaching_point': 'Bu cilt S. aureus ile sık kolonizedir; klinik enfeksiyon yoksa kültür ve '
                                            'antibiyotik gerekmez.'},
                         {'text': 'Tanının klinik olduğunu kabul edip tetkik istememek, şiddet ve tetikleyicileri '
                                  'belirleyerek tedavi planına geçmek',
                          'is_correct': True,
                          'explanation': 'Tanı öykü ve muayeneyle konur. Tetkik ancak tedaviye dirençli, atipik veya '
                                         'besinle açık ilişki gösteren olgularda düşünülür.',
                          'new_finding': 'Tetkik istenmedi. Tetikleyiciler: sık köpüklü banyo, yetersiz nemlendirici '
                                         'kullanımı, kışın kuru ortam ve yünlü giysiler.'},
                         {'text': 'Tam kan sayımı, eozinofil sayısı ve total IgE istemek; değerler yüksekse sistemik '
                                  'antihistaminik ve oral steroid başlamak',
                          'is_correct': False,
                          'scenario_update': 'Eozinofil ve total IgE hafif yüksek geldi; oral steroid sonrası '
                                             'lezyonlar kısa süre gerileyip kesince rebound alevlendi.',
                          'teaching_point': 'Kan tetkikleri tedaviyi yönlendirmez; sistemik steroid rebound '
                                            'alevlenmeye yol açtığı için önerilmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bu çocukta en olası tanınız nedir?',
             'options': [{'text': 'Atopik dermatit alevlenmesi',
                          'is_correct': True,
                          'explanation': 'Kaşıntı, fleksural dağılım, bebeklikten beri tekrarlayan seyir ve ailede '
                                         'atopi atopik dermatiti gösterir. Enfeksiyon bulgusu yoktur.',
                          'new_finding': 'Tanı: Atopik dermatit alevlenmesi (orta şiddet, enfeksiyonsuz).'},
                         {'text': 'Seboreik dermatit',
                          'is_correct': False,
                          'scenario_update': 'Saçlı deri ve kıvrım yerlerinde yağlı sarı kepek yoktu, kaşıntı çok '
                                             'belirgindi.',
                          'teaching_point': 'Seboreik dermatit daha az kaşıntılıdır ve saçlı deri, kaş ve nazolabial '
                                            'bölgeyi tutar.'},
                         {'text': 'Allerjik kontakt dermatit',
                          'is_correct': False,
                          'scenario_update': 'Lezyonlar bir temas alanıyla sınırlı değil, simetrik ve kronikti.',
                          'teaching_point': 'Kontakt dermatit temas alanıyla sınırlı, keskin sınırlı lezyonlar yapar.'},
                         {'text': 'Psoriazis vulgaris',
                          'is_correct': False,
                          'scenario_update': 'Plaklar ekstansör değil fleksural yüzlerdeydi ve keskin sınırlı gümüşi '
                                             'pul yoktu.',
                          'teaching_point': 'Psoriazis genellikle ekstansör yüzlerde keskin sınırlı kalın gümüşi pullu '
                                            'plaklar yapar.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Ailenin kortizon kaygısına saygı göstererek steroidsiz yalnızca nemlendirici '
                                  'önermek ve kaşıntı için düzenli sedatif antihistaminik başlamak',
                          'is_correct': False,
                          'scenario_update': 'İki hafta sonra lezyonlar yaygınlaştı ve kaşıntı nedeniyle sekonder '
                                             'enfeksiyon gelişti.',
                          'teaching_point': 'Alevlenmede topikal kortikosteroid tedavinin temelidir; doğru potens ve '
                                            'sürede güvenlidir. Kaygı bilgilendirmeyle giderilmelidir.'},
                         {'text': 'Günde 2-3 kez bol nemlendirici, gövdeye orta potensli steroidi 1-2 hafta günde bir '
                                  'kez sürmek; kısa ılık banyo önermek ve kaygıyı gidermek',
                          'is_correct': True,
                          'explanation': 'Nemlendirici deri bariyerini onarır. Orta potensli steroid alevlenmeyi '
                                         'kontrol eder; ardından haftada iki gün koruyucu kullanım yeni alevlenmeleri '
                                         'azaltır. Parmak ucu birimiyle doz eğitimi uyumu artırır.',
                          'new_finding': 'Metilprednizolon aseponat krem ve nemlendirici ile taburcu edildi, parmak '
                                         'ucu birimi gösterildi. İkinci hafta kontrolünde lezyonlar %80 geriledi, '
                                         'çocuk geceleri uyuyordu.'},
                         {'text': 'Hızlı etki için yüze ve gövdeye çok yüksek potensli klobetazol kremi günde iki kez '
                                  'bir ay sürmelerini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Bir ay sonra yüzde atrofi ve telenjiektazi gelişti.',
                          'teaching_point': 'Küçük çocukta, özellikle yüzde çok yüksek potensli steroid uzun süre '
                                            'kullanılmaz; potens bölgeye göre seçilir.'},
                         {'text': 'Beş gün oral prednizolon başlamak, banyoyu haftada bire indirip cildin kurumasını '
                                  'önlemek için evde bebek yağı kullanmalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Oral steroid kesilince lezyonlar daha ağır alevlendi; bebek yağı yeterli '
                                             'nem sağlamadı.',
                          'teaching_point': 'Sistemik steroid rebound yaptığı için önerilmez; kısa ılık banyo sonrası '
                                            'nemlendirici uygulaması faydalıdır.'}]}]},
 {'id': 'Y82',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '7 Yaşında (24 kg)',
  'gender': 'Erkek',
  'complaint': 'Üç haftadır özellikle geceleri artan, uykudan uyandıran şiddetli kaşıntı ve elde, bilekte, belde '
               'kabarcıklar',
  'history': "Annesi anlatıyor: 'Üç haftadır geceleri kaşınmaktan uyuyamıyor. Önce parmak aralarında küçük kabarcıklar "
             "çıktı, sonra bileklere, karna, kasığa yayıldı. Ben de ve küçük kardeşi de son bir haftadır kaşınıyoruz.' "
             'Kalabalık bir apartman dairesinde yaşıyorlar, bir ay önce yurt dışından gelen akrabaları evde kalmış. '
             'Daha önce verilen antihistaminik ve kortizonlu krem kaşıntıyı azaltmamış. Ateş yok.',
  'final_diagnosis': 'Skabiyez (Uyuz)',
  'disposition': 'Tüm Ev Halkının Eş Zamanlı Permetrin Tedavisi ve Çevresel Önlemlerle Yeşil Alandan Taburculuk',
  'case_pearl': 'Geceleri artan kaşıntı, ailede benzer yakınma ve parmak araları, el bileği, bel, aksiller ön kıvrım, '
                'genital bölge ve meme başı çevresindeki papül ve tüneller skabiyezi düşündürür. Tanı kliniktir, '
                'dermoskopi doğrulamaya yardımcı olur. Permetrin %5 krem boyundan aşağı tüm vücuda (2 yaş altında '
                'saçlı deri ve yüz dahil) sürülür, 8-12 saat sonra yıkanır ve 7 gün sonra tekrarlanır. Tüm ev halkı '
                'aynı gün tedavi edilmelidir. Kaşıntı tedaviden sonra 2-4 hafta sürebilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Geceleri artan kaşıntısı olan bu çocukta muayenede nelere dikkat edersiniz?',
             'options': [{'text': 'Yalnızca annenin gösterdiği el bölgesine bakıp lezyonları kontakt dermatit kabul '
                                  'ederek daha güçlü bir kortizonlu krem yazmak',
                          'is_correct': False,
                          'scenario_update': 'Güçlü steroid kaşıntıyı kısa süre bastırdı, lezyonlar yaygınlaştı ve '
                                             'kardeşte de tablo ağırlaştı.',
                          'teaching_point': 'Topikal steroid altta yatan nedeni tedavi etmez, tabloyu maskeleyerek '
                                            'yaygınlaşmasına yol açabilir.'},
                         {'text': 'Tüm deriyi muayene edip parmak araları, el bilekleri, bel, aksilla, genital '
                                  'bölgedeki papül ve tünelleri aramak; ev halkında kaşıntıyı sorgulamak',
                          'is_correct': True,
                          'explanation': 'Tipik dağılım, tüneller ve ailede kaşıntı birlikteliği tanıya en çok katkı '
                                         'sağlayan bulgulardır. Genital bölgedeki nodüller sık atlanır.',
                          'new_finding': 'Genel durum iyi, ateş yok. Parmak aralarında, el bileklerinin iç yüzünde ve '
                                         "bel çevresinde yaygın eritemli papüller, ekskoriasyonlar ve 3-5 mm'lik ince, "
                                         'kıvrımlı gri çizgiler. Penis gövdesinde ve skrotumda birkaç kaşıntılı nodül. '
                                         'Aksilla ön kıvrımında papüller. Yüz ve saçlı deri temiz. Sekonder enfeksiyon '
                                         'bulgusu yok.'},
                         {'text': 'Kaşıntıyı stres ve kuru cilde bağlayarak muayeneyi kısa tutmak, nemlendirici ve '
                                  'gece için sedatif antihistaminik önermek',
                          'is_correct': False,
                          'scenario_update': 'Kaşıntı sürdü; iki hafta sonra okul arkadaşlarında da benzer yakınma '
                                             'başladı.',
                          'teaching_point': 'Ailede eş zamanlı kaşıntı bulaşıcı bir nedene işaret eder; tüm deri '
                                            'muayenesi atlanmamalıdır.'},
                         {'text': 'Ateş olmamasına rağmen yaygın papüller nedeniyle suçiçeği kabul edip çocuğu okuldan '
                                  'izole etmek ve asiklovir başlamak',
                          'is_correct': False,
                          'scenario_update': 'Asiklovir etkisiz kaldı; lezyonların üç haftalık süresi ve dağılımı bu '
                                             'tanıyla uyuşmadı.',
                          'teaching_point': 'Suçiçeği ateşle, farklı evrelerde veziküllerle, gövdeden başlayarak ve '
                                            'birkaç gün içinde seyreder.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Tanıyı desteklemek için hangi yaklaşım en uygundur?',
             'options': [{'text': 'Tam kan sayımında eozinofil sayısı ve total IgE istemek, değerler yüksekse alerjik '
                                  'bir tablo kabul edip alerji polikliniğine sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'Eozinofil hafif yüksek geldi ve çocuk alerji polikliniğine '
                                             'yönlendirildi; tedavi haftalarca gecikti.',
                          'teaching_point': 'Eozinofili nonspesifiktir; tanıyı koydurmaz ve bulaşıcı tabloyu '
                                            'geciktirir.'},
                         {'text': 'Lezyonlardan mantar kültürü ve KOH incelemesi istemek, sonuçlar çıkana dek topikal '
                                  'antifungal tedavi başlatmak',
                          'is_correct': False,
                          'scenario_update': 'KOH negatif geldi, antifungal tedavi yararsız kaldı.',
                          'teaching_point': 'Dağılım ve tüneller mantar enfeksiyonuyla uyumlu değildir.'},
                         {'text': 'Tanıyı kliniğe dayandırmak; mümkünse tünel ucundan dermoskopi yapmak, gerekirse '
                                  'kazıma örneğini mikroskopta incelemek',
                          'is_correct': True,
                          'explanation': 'Tanı genellikle klinik bulgularla konur. Dermoskopi ve kazıma doğrulamaya '
                                         'yardımcıdır ancak negatif sonuç tanıyı dışlamaz.',
                          'new_finding': 'Dermoskopide tünel ucunda koyu üçgen bir yapı ve arkasında ince bir iz '
                                         'görüldü. Kazıma mikroskopisinde akar ve yumurtalar saptandı.'},
                         {'text': 'Nodüler lezyonlar nedeniyle genital bölgedeki nodülden punch biyopsi almak ve '
                                  'patoloji sonucuna göre tedavi planı yapmak',
                          'is_correct': False,
                          'scenario_update': 'Biyopsi sonucu iki hafta sürdü; bu sürede ev halkının yakınmaları arttı.',
                          'teaching_point': 'Tipik tabloda biyopsi gereksizdir ve tedaviyi geciktirir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Papüler ürtiker',
                          'is_correct': False,
                          'scenario_update': 'Lezyonlar parmak arası, bilek ve genital bölgedeydi ve tüneller vardı.',
                          'teaching_point': 'Papüler ürtiker açık bölgelerde gruplaşan ısırık papülleridir; tünel ve '
                                            'genital tutulum yoktur.'},
                         {'text': 'Atopik dermatit',
                          'is_correct': False,
                          'scenario_update': 'Daha önce cilt hastalığı yoktu, ev halkında aynı anda başlayan kaşıntı '
                                             'vardı.',
                          'teaching_point': 'Atopik dermatit kronik seyirlidir ve ailede eş zamanlı başlamaz.'},
                         {'text': 'Skabiyez (uyuz)',
                          'is_correct': True,
                          'explanation': 'Geceleri artan kaşıntı, ev halkında benzer yakınma, tipik dağılım, tüneller, '
                                         'genital nodüller ve mikroskopide akar skabiyezi gösterir.',
                          'new_finding': 'Tanı: Skabiyez.'},
                         {'text': 'Tinea korporis',
                          'is_correct': False,
                          'scenario_update': 'Halka şeklinde aktif kenarlı plak yoktu ve KOH incelemesine gerek '
                                             'kalmadan akar gösterildi.',
                          'teaching_point': 'Tinea halka şeklinde, ortası açılan, kenarı aktif plaklar yapar.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk ve ailesi için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Yalnızca çocuğa permetrin kremi bir kez uygulamak, kaşıntısı olan anne ve kardeşi '
                                  'kendi hekimlerine başvurmaları için yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk iki hafta sonra yeniden enfekte oldu; tedavi edilmeyen ev halkı '
                                             'bulaşı sürdürdü.',
                          'teaching_point': 'Tüm ev halkı belirti olsun olmasın aynı gün tedavi edilmeli ve tedavi 7 '
                                            'gün sonra tekrarlanmalıdır.'},
                         {'text': 'Permetrini boyundan aşağı tüm vücuda sürüp 8-12 saat sonra yıkamak, 7 gün sonra '
                                  'tekrarlamak ve tüm ev halkını aynı gün tedavi etmek',
                          'is_correct': True,
                          'explanation': 'Eş zamanlı ev halkı tedavisi ve tekrar doz yeniden enfeksiyonu önler. '
                                         "Çamaşırlar 60°C'de yıkanmalı ya da 72 saat kapalı poşette bekletilmelidir. "
                                         'Kaşıntının 2-4 hafta sürmesi tedavi başarısızlığı değildir.',
                          'new_finding': 'Tüm aile aynı gece tedavi edildi ve tedavi bir hafta sonra tekrarlandı. '
                                         'Dördüncü haftada kaşıntı tamamen geçti, yeni lezyon çıkmadı.'},
                         {'text': 'Kaşıntıyı hızla azaltmak için yüksek potensli topikal steroid ve oral '
                                  'antihistaminik başlamak, lezyonlar iki hafta sonra hâlâ sürerse ancak o zaman '
                                  'yeniden değerlendirip antiparaziter tedaviyi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Steroid altında lezyonlar yaygınlaştı ve kabuklanma arttı.',
                          'teaching_point': 'Topikal steroid bu tabloda tedavi değildir; önce antiparaziter tedavi '
                                            'yapılmalıdır.'},
                         {'text': 'Permetrin kremini yalnızca lezyonlu bölgelere günde iki kez bir hafta sürmelerini '
                                  've kaşıntı geçene dek tedaviyi sürdürmelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'Lezyonsuz bölgelerdeki akarlar tedavi edilmedi; kaşıntı nedeniyle krem '
                                             'gereksiz uzun kullanıldı ve irritasyon gelişti.',
                          'teaching_point': 'Krem tüm vücuda uygulanır; kaşıntının sürmesi tedavinin uzatılmasını '
                                            'gerektirmez.'}]}]},
 {'id': 'Y83',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '5 Yaşında (18 kg)',
  'gender': 'Kız',
  'complaint': 'Sağ bacakta dün akşam başlayıp sabah büyüyen kırmızı, şiş ve kaşıntılı alan',
  'history': "Annesi anlatıyor: 'Yazlıktayız, akşam bahçede çok sivrisinek vardı. Gece kaşındı, sabah baldırında avuç "
             "içi büyüklüğünde kırmızı ve şiş bir alan vardı. Ortasında küçük bir sivrisinek ısırığı izi var.' Ateş, "
             'kusma, nefes darlığı, dudak ve göz şişliği yok. Daha önceki yazlarda da ısırıklar çok şişiyormuş. '
             'Bilinen ilaç alerjisi yok. Çocuk oyun oynuyor ve basabiliyor.',
  'final_diagnosis': 'Sivrisinek Isırığına Büyük Lokal Reaksiyon',
  'disposition': 'Soğuk Uygulama, Oral Antihistaminik ve Isırıktan Korunma Önerileriyle Yeşil Alandan Taburculuk',
  'case_pearl': 'Isırıktan sonraki saatler içinde başlayan, kaşıntının ağrıdan baskın olduğu, ateşsiz ve sistemik '
                'bulgusuz büyük, kızarık ve şiş alan büyük lokal reaksiyondur ve sıklıkla selülitle karıştırılır. '
                'Selülit genellikle ısırıktan 1-3 gün sonra başlar, ağrılıdır, yayılır ve ateş eşlik edebilir. Büyük '
                'lokal reaksiyon 24-48 saatte zirve yapıp 3-10 günde geriler. Antibiyotik gerekmez. Sistemik reaksiyon '
                'olmadığı için adrenalin oto-enjektörü veya alerji testi gerekmez.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Bacağında kızarık ve şiş alan olan bu çocukta muayenede neye odaklanırsınız?',
             'options': [{'text': 'Bacaktaki kızarıklığı enfeksiyon kabul ederek yalnızca lezyonu değerlendirmek ve '
                                  'sistemik bulguları sorgulamadan oral antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik başlandı; reaksiyon üç günde kendiliğinden geriledi ve aile '
                                             'her ısırıkta antibiyotik istemeye başladı.',
                          'teaching_point': 'Başlangıç zamanı, kaşıntı-ağrı dengesi ve sistemik bulgular sorgulanmadan '
                                            'antibiyotik kararı verilmemelidir.'},
                         {'text': 'Havayolu, solunum ve deri muayenesiyle sistemik reaksiyonu dışlamak; alanın '
                                  'sıcaklığını, hassasiyetini, sınırını, ısırık izini ve lenfanjiti değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Önce sistemik alerjik reaksiyon dışlanır. Lezyonun başlangıç zamanı, '
                                         'kaşıntının ağrıya baskınlığı, hassasiyet ve lenfanjit alerjik-inflamatuvar '
                                         'bir yanıtı bakteriyel enfeksiyondan ayırmada yol gösterir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 98/dk, SS 20/dk, SpO2 %99. Ürtiker, '
                                         'anjiyoödem, hışıltı yok. Sağ baldırda 8x6 cm, ortasında ısırık noktası olan, '
                                         'açık kırmızı, ödemli, hafif ılık, çok kaşıntılı ancak az hassas alan. '
                                         'Lenfanjit çizgisi ve fluktuasyon yok. Popliteal ve inguinal lenf nodları ele '
                                         'gelmiyor. Diğer bacakta birkaç küçük ısırık papülü.'},
                         {'text': 'Şişlik nedeniyle anafilaksi riskini düşünüp muayeneyi tamamlamadan intramüsküler '
                                  'adrenalin uygulamak ve çocuğu Sarı Alanda 6 saat izlemek',
                          'is_correct': False,
                          'scenario_update': 'Adrenalin sonrası çocukta çarpıntı ve solukluk gelişti; sistemik tutulum '
                                             'bulgusu yoktu.',
                          'teaching_point': 'Adrenalin sistemik reaksiyon için verilir; yalnız lokal şişlikte '
                                            'endikasyonu yoktur.'},
                         {'text': 'Derin ven trombozunu dışlamak için muayeneyi kısa tutup acil alt ekstremite venöz '
                                  'Doppler ultrasonografisi ve D-dimer istemek',
                          'is_correct': False,
                          'scenario_update': 'Doppler normal geldi, D-dimer hafif yüksekti; çocuk saatlerce gereksiz '
                                             'tetkikle bekletildi.',
                          'teaching_point': 'Risk faktörü olmayan çocukta ısırık sonrası lokal şişlik tromboz '
                                            'düşündürmez; görüntüleme gereksizdir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Sistemik bulgusu olmayan bu çocukta hangi yaklaşım uygundur?',
             'options': [{'text': 'Tam kan sayımı, CRP ve kan kültürü istemek; lökosit ve CRP yüksekse intravenöz '
                                  'antibiyotikle yatış planlamak',
                          'is_correct': False,
                          'scenario_update': 'CRP 8 mg/L, lökosit normal geldi; kan alımı çocuğu çok korkuttu ve '
                                             'yönetim değişmedi.',
                          'teaching_point': 'Lokal reaksiyon ile basit cilt enfeksiyonunun ayrımı kliniktir; kan '
                                            'tetkikleri katkı sağlamaz.'},
                         {'text': 'Lezyon altında apse olup olmadığını görmek için yumuşak doku ultrasonografisi '
                                  'istemek ve sonucuna göre drenaj planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografide yalnızca cilt altı ödemi görüldü, sıvı koleksiyonu '
                                             'yoktu.',
                          'teaching_point': 'Fluktuasyon ve püy yokken ultrasonografi yönetimi değiştirmez.'},
                         {'text': 'Tetkik istemeden lezyon sınırını kalemle çizip fotoğraflamak, saati not etmek ve '
                                  'ilerleme olursa yeniden değerlendirme planlamak',
                          'is_correct': True,
                          'explanation': 'Klinik tanı yeterlidir. Sınırın işaretlenmesi seyrin nesnel izlenmesini '
                                         'sağlar ve aile için yeniden başvuru ölçütü oluşturur.',
                          'new_finding': 'Lezyon sınırı işaretlendi ve fotoğraflandı. Bir saatlik gözlemde sınır '
                                         'değişmedi, çocuk iyi görünüyordu.'},
                         {'text': 'Sivrisinek alerjisini doğrulamak için spesifik IgE testi ve deri prick testi '
                                  'planlayıp sonuç gelene kadar ısırıklardan korunmayı önermek',
                          'is_correct': False,
                          'scenario_update': 'Testler pahalı ve yorumu belirsiz oldu; acil yönetimi değiştirmedi.',
                          'teaching_point': 'Yalnız ısırık bölgesiyle sınırlı reaksiyonda rutin alerji testi '
                                            'önerilmez; sistemik reaksiyon riski düşüktür.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Sivrisinek ısırığına büyük lokal reaksiyon',
                          'is_correct': True,
                          'explanation': 'Isırıktan saatler sonra başlayan, kaşıntının baskın olduğu, ateşsiz ve '
                                         'sistemik bulgusuz, ortasında ısırık noktası olan geniş şişlik ve önceki '
                                         'yazlarda benzer öykü büyük lokal reaksiyonu gösterir.',
                          'new_finding': 'Tanı: Sivrisinek ısırığına büyük lokal reaksiyon.'},
                         {'text': 'Nonpürülan selülit',
                          'is_correct': False,
                          'scenario_update': 'Lezyon ısırıktan saatler sonra başlamıştı, çok kaşıntılıydı, az hassastı '
                                             've ateş yoktu.',
                          'teaching_point': 'Selülit genellikle 1-3 gün sonra, ağrılı ve ilerleyici biçimde gelişir.'},
                         {'text': 'Sistemik alerjik reaksiyon',
                          'is_correct': False,
                          'scenario_update': 'Ürtiker, anjiyoödem, solunum veya dolaşım bulgusu yoktu.',
                          'teaching_point': 'Sistemik reaksiyonda ısırık alanı dışında deri, solunum veya dolaşım '
                                            'tutulumu olur.'},
                         {'text': 'Kontakt dermatit',
                          'is_correct': False,
                          'scenario_update': 'Lezyonun ortasında ısırık noktası vardı ve bir temas maddesi öyküsü '
                                             'yoktu.',
                          'teaching_point': 'Kontakt dermatitte temas alanına uyan, sıklıkla veziküler, keskin sınırlı '
                                            'lezyon olur.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun taburculuk planı hangisidir?',
             'options': [{'text': 'Olası enfeksiyona karşı oral sefaleksin 5 gün başlamak ve lezyon tamamen geçene '
                                  'kadar bacağı sargıyla kapatmalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik sonrası çocukta ishal gelişti; sargı altında kaşıntı arttı.',
                          'teaching_point': 'Büyük lokal reaksiyonda antibiyotik gerekmez.'},
                         {'text': 'Soğuk kompres ve oral setirizin önermek, gerekirse kısa süre orta potensli steroid '
                                  'krem sürmek; sivrisinek kovucu ve cibinlik önerip uyarı bulgularını anlatmak',
                          'is_correct': True,
                          'explanation': 'Semptomatik tedavi yeterlidir. Çocuklara uygun kovucular (DEET ≤%30 veya '
                                         'ikaridin) ve fiziksel korunma yeni ısırıkları önler. Ateş, artan ağrı, '
                                         'kırmızı çizgi veya sınırın yayılması başvuru nedenidir.',
                          'new_finding': 'Setirizin ve soğuk uygulama ile taburcu edildi. Şişlik ikinci gün azalmaya '
                                         'başladı ve beşinci gün tamamen geçti.'},
                         {'text': 'Sonraki ısırıklarda anafilaksi gelişebileceğini söyleyip adrenalin oto-enjektörü '
                                  'reçete etmek ve çocuk alerji polikliniğine sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'Aile her ısırıkta panikle oto-enjektör kullanmayı düşündü; alerji '
                                             'polikliniği ek bir risk saptamadı.',
                          'teaching_point': 'Büyük lokal reaksiyon sonrası sistemik reaksiyon riski düşüktür; '
                                            'oto-enjektör gerekmez.'},
                         {'text': 'Beş gün yüksek doz oral prednizolon başlamak ve şişliğin geçmesini hızlandırmak '
                                  'için lezyon bölgesine sıcak kompres uygulamalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Sıcak uygulama kaşıntı ve şişliği artırdı; sistemik steroid gereksiz yan '
                                             'etki riski oluşturdu.',
                          'teaching_point': 'Soğuk uygulama ödemi ve kaşıntıyı azaltır; rutin sistemik steroid '
                                            'önerilmez.'}]}]},
 {'id': 'Y84',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '8 Yaşında (26 kg)',
  'gender': 'Erkek',
  'complaint': 'Sol bacakta iki gündür giderek büyüyen ağrılı kızarıklık, şişlik ve bugün başlayan ateş',
  'history': "Annesi anlatıyor: 'Dört gün önce böcek ısırdı, çok kaşıdı, yara oldu. İki gün önce etrafı kızardı, her "
             "gün biraz daha büyüyor, dokununca çok acıyor. Bu sabah ateşi 38.3°C oldu.' Basmakta zorlanıyor ama "
             'yürüyebiliyor. İçinde cerahat birikmesi fark etmemişler. Kronik hastalık, diyabet veya bağışıklık sorunu '
             'yok. Aşıları tam. İlaç alerjisi yok.',
  'final_diagnosis': 'Nonpürülan Selülit (Alt Ekstremite)',
  'disposition': 'Oral Sefaleksin ve 48 Saat Sonra Kontrolle Yeşil Alandan Taburculuk',
  'case_pearl': 'Nonpürülan selülit sınırları belirsiz, sıcak, ağrılı ve yayılan eritemle seyreder. Etken çoğunlukla A '
                "grubu streptokok ve S. aureus'tur. Genel durumu iyi çocukta kan tetkiki ve kültür gerekmez. "
                'Fluktuasyon şüphesi varsa ultrasonografi apseyi gösterir. Ağızdan sefaleksin 5 gün yeterlidir ve '
                'yanıta göre uzatılır. Ekstremite yükseltilir, sınır işaretlenir ve 48 saatte kontrol edilir. Ağrının '
                'bulgularla orantısız olması, hızlı yayılım, bül veya toksik görünüm nekrotizan fasiiti düşündürür.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Bacağında yayılan ağrılı kızarıklık ve ateşi olan bu çocukta muayenede neye dikkat '
                         'edersiniz?',
             'options': [{'text': 'Genel görünümü ve vitalleri değerlendirip eritemin sınırlarını, fluktuasyonu, '
                                  'lenfanjiti, krepitasyonu, eklem hareketini ve ağrının bulgularla orantısını '
                                  'incelemek',
                          'is_correct': True,
                          'explanation': 'Fluktuasyon apseyi, krepitasyon ve orantısız ağrı derin enfeksiyonu, eklem '
                                         'hareket kısıtlılığı eklem tutulumunu düşündürür. Genel durum yatış kararını '
                                         'belirler.',
                          'new_finding': 'Vital Bulgular: Ateş 38.2°C, KTA 108/dk, SS 20/dk, TA 104/66 mmHg, KDZ 2 sn. '
                                         'Genel durum iyi. Sol baldır ön yüzünde 10x7 cm, sınırları belirsiz, parlak '
                                         'kırmızı, sıcak, ödemli ve hassas alan; merkezde kabuklu küçük bir yara. '
                                         'Fluktuasyon, bül ve krepitasyon yok. Diz ve ayak bileği hareketleri ağrısız '
                                         've tam. Sol inguinal bölgede 1.5 cm hassas lenf nodu. Lenfanjit çizgisi '
                                         'yok.'},
                         {'text': 'Kızarıklığı böcek ısırığının lokal reaksiyonu kabul edip yalnız lezyona bakmak, '
                                  'antihistaminik ve soğuk uygulamayla aileyi rahatlatmak',
                          'is_correct': False,
                          'scenario_update': "İki gün sonra kızarıklık uyluğa yayıldı ve ateş 39°C'ye çıktı.",
                          'teaching_point': 'Isırıktan günler sonra başlayan, ağrılı, yayılan kızarıklık ve ateş '
                                            'bakteriyel enfeksiyonu düşündürür.'},
                         {'text': 'Ateş nedeniyle hemen Sarı Alana alıp damar yolu açmak ve muayene tamamlanmadan '
                                  'intravenöz geniş spektrumlu antibiyotik başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Genel durumu iyi olan çocuk gereksiz yere damar yolu ve yatış sürecine '
                                             'alındı.',
                          'teaching_point': 'Genel durumu iyi, sistemik toksisitesi olmayan çocukta ağızdan tedavi '
                                            'yeterlidir.'},
                         {'text': 'Kızarıklığın ortasındaki yarayı bistüriyle açıp drene etmek ve içinden kültür '
                                  'almak, sonra muayeneyi tamamlamak',
                          'is_correct': False,
                          'scenario_update': 'Kesiden püy gelmedi; gereksiz bir yara oluşturuldu.',
                          'teaching_point': 'Fluktuasyon olmayan lezyonda kesi yapılmaz; drenaj yalnızca apse '
                                            'varlığında yapılır.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Genel durumu iyi ve fluktuasyonu olmayan bu çocukta hangi tetkik yaklaşımı uygundur?',
             'options': [{'text': 'Kemik tutulumunu dışlamak için acil alt ekstremite MR görüntülemesi istemek ve '
                                  'sonucu gelene kadar antibiyotiği ertelemek',
                          'is_correct': False,
                          'scenario_update': 'MR için sedasyon gerekti ve tedavi saatlerce gecikti; kemik tutulumu '
                                             'yoktu.',
                          'teaching_point': 'Kemik ağrısı veya eklem kısıtlılığı olmadan MR gerekmez; antibiyotik '
                                            'geciktirilmemelidir.'},
                         {'text': 'Kan tetkiki ve kültür istemeden eritem sınırlarını kalemle işaretleyip '
                                  'fotoğraflamak ve tedaviye yanıtı izleme planı yapmak',
                          'is_correct': True,
                          'explanation': 'Genel durumu iyi, komplike olmayan olguda kan kültürü çok nadir pozitiftir '
                                         've yönetimi değiştirmez. Sınırın işaretlenmesi yanıtın değerlendirilmesini '
                                         'sağlar.',
                          'new_finding': 'Eritem sınırı işaretlendi ve fotoğraflandı. Tetkik istenmedi.'},
                         {'text': "Tam kan sayımı, CRP, sedimantasyon ve kan kültürü istemek; CRP 40 mg/L'nin "
                                  'üzerindeyse intravenöz tedavi için yatış planlamak',
                          'is_correct': False,
                          'scenario_update': 'CRP 46 mg/L geldi ve çocuk yatırıldı; genel durumu iyi olduğu için yatış '
                                             'gereksiz oldu.',
                          'teaching_point': 'CRP tek başına yatış ölçütü değildir; karar genel duruma ve ağızdan '
                                            'tedaviyi tolere etmeye göre verilir.'},
                         {'text': 'Lezyon yüzeyinden sürüntü kültürü alıp antibiyogram sonucuna göre tedavi seçmek ve '
                                  'o zamana dek yalnızca topikal antibiyotik vermek',
                          'is_correct': False,
                          'scenario_update': 'Yüzey kültüründe deri florası üredi; topikal tedavi derin dokuya etki '
                                             'etmedi ve kızarıklık yayıldı.',
                          'teaching_point': 'Yüzey kültürü derin dokudaki etkeni yansıtmaz; topikal antibiyotik derin '
                                            'deri enfeksiyonunda etkisizdir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Deri apsesi',
                          'is_correct': False,
                          'scenario_update': 'Fluktuasyon ve püy yoktu.',
                          'teaching_point': 'Apsede fluktuan, sınırlı koleksiyon bulunur ve tedavinin esası '
                                            'drenajdır.'},
                         {'text': 'Nonpürülan selülit',
                          'is_correct': True,
                          'explanation': 'Isırık sonrası gelişen, sınırları belirsiz, sıcak, ağrılı, yayılan eritem, '
                                         'hafif ateş ve bölgesel lenfadenopati, fluktuasyon olmadan nonpürülan '
                                         'selüliti gösterir.',
                          'new_finding': 'Tanı: Nonpürülan selülit.'},
                         {'text': 'Nekrotizan fasiit',
                          'is_correct': False,
                          'scenario_update': 'Genel durum iyiydi, ağrı bulgularla orantılıydı, bül ve krepitasyon '
                                             'yoktu.',
                          'teaching_point': 'Nekrotizan fasiitte toksik görünüm, orantısız ağrı, hızlı yayılım, bül ve '
                                            'krepitasyon görülür.'},
                         {'text': 'Büyük lokal ısırık reaksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Kızarıklık ısırıktan iki gün sonra başlamış, ağrılı ve yayılıcıydı ve '
                                             'ateş vardı.',
                          'teaching_point': 'Lokal reaksiyon saatler içinde başlar, kaşıntılıdır ve ateş yapmaz.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Ağızdan tek başına trimetoprim-sülfametoksazol 7 gün başlamak, bacağı '
                                  'dinlendirmeden günlük aktivitelerine devam etmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'İki gün sonra kızarıklık yayılmaya devam etti; tedavi streptokokları '
                                             'yeterince kapsamadı.',
                          'teaching_point': 'Nonpürülan selülitte streptokok kapsamı gerekir; tek başına '
                                            'trimetoprim-sülfametoksazol yeterli değildir.'},
                         {'text': 'Ağızdan sefaleksin 5 gün, bacağı yükseltmek ve analjezi önermek; 48 saat sonra '
                                  'işaretli sınırla kontrol yapıp yanıt yoksa tedaviyi uzatmak',
                          'is_correct': True,
                          'explanation': "Sefaleksin streptokok ve metisiline duyarlı S. aureus'u kapsar. 5 gün çoğu "
                                         'olguda yeterlidir. İlk 24-48 saatte kızarıklığın hafif artması beklenebilir.',
                          'new_finding': 'Sefaleksin 50 mg/kg/gün dört dozda başlandı. 48. saat kontrolünde ateş yoktu '
                                         've kızarıklık işaretli sınırın içine çekilmişti. Beşinci gün tamamen '
                                         'düzeldi.'},
                         {'text': 'Ateş olduğu için intravenöz klindamisinle servise yatırmak, ateş tamamen düşene '
                                  'kadar en az 72 saat parenteral tedaviyi sürdürmek',
                          'is_correct': False,
                          'scenario_update': 'Genel durumu iyi çocuk üç gün gereksiz yere hastanede yattı.',
                          'teaching_point': 'Hafif ateş tek başına yatış endikasyonu değildir; toksik görünüm veya '
                                            'ağızdan alamama yatış gerektirir.'},
                         {'text': 'Topikal mupirosin ve sıcak kompresle izlemek, kızarıklık bir hafta içinde '
                                  'gerilemezse oral antibiyotik başlamak üzere kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Kızarıklık üç günde uyluğa yayıldı ve çocuk yüksek ateşle geri geldi.',
                          'teaching_point': 'Selülit sistemik antibiyotik gerektirir; topikal tedavi yalnızca yüzeyel '
                                            'enfeksiyonlarda kullanılır.'}]}]},
 {'id': 'Y85',
  'category': '🦴 Kas-İskelet & Eklem / Ortopedik Aciller',
  'age': '10 Yaşında',
  'gender': 'Kız',
  'complaint': 'Sağ işaret parmağında tırnak kenarında iki gündür artan zonklayıcı ağrı ve şişlik',
  'history': "Kendisi anlatıyor: 'Tırnaklarımı ve etlerini yiyorum. İki gün önce tırnağımın yanı kızardı, şimdi şişti, "
             "zonkluyor, gece uyutmadı.' Ateş yok. Annesi sıcak su ile pansuman yapmış. Parmakta kabarcık, su toplama "
             'veya ağız çevresinde uçuk öyküsü yok. Parmak ucunun ön yüzü (pulpa) ağrılı değil. Diyabet yok.',
  'final_diagnosis': 'Apseleşmiş Akut Paronişi',
  'disposition': 'Lokal Anestezi Altında Drenaj ve Ilık Pansuman Önerileriyle Yeşil Alandan Taburculuk',
  'case_pearl': 'Akut paronişi tırnak kıvrımının, çoğunlukla S. aureus ve streptokoklara bağlı enfeksiyonudur ve '
                'tırnak yeme ile tetiklenir. Fluktuasyon yoksa ılık su banyosu yeterlidir. Apse varsa tırnak '
                'kıvrımının künt bir aletle ya da bistüriyle kaldırılarak drenajı esastır. Drenajdan sonra yayılan '
                'selülit yoksa rutin antibiyotik gerekmez. Herpetik dolamada (veziküller, ağrının orantısız olması) '
                'kesi yapılmaz. Pulpada gerginlik ve ağrı felonu düşündürür.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Tırnak kenarında ağrılı şişliği olan bu çocukta muayenede neye dikkat edersiniz?',
             'options': [{'text': 'Şişliğin yerini ve fluktuasyonu, tırnak altına uzanımı, pulpada gerginliği, vezikül '
                                  'varlığını, yayılan kızarıklık ve lenfanjiti değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Fluktuasyon drenaj ihtiyacını, pulpa tutulumu derin enfeksiyonu, veziküller '
                                         'viral nedeni gösterir. Bu ayrım yanlış kesiden korur.',
                          'new_finding': 'Ateş 36.8°C. Sağ işaret parmağında radiyal tırnak kıvrımı ve eponişiyumda '
                                         'kırmızı, gergin şişlik; derinin altından sarı-beyaz bir koleksiyon '
                                         'seçiliyor, fluktuasyon pozitif. Tırnak altına uzanım yok. Pulpa yumuşak ve '
                                         'ağrısız. Vezikül yok. Kızarıklık parmağın proksimaline yayılmıyor, lenfanjit '
                                         'yok. Eklem hareketleri tam.'},
                         {'text': 'Ağrıyı kemik enfeksiyonuna bağlayıp muayeneyi kısa tutarak el grafisi istemek ve '
                                  'grafi sonucuna göre ortopedi konsültasyonu planlamak',
                          'is_correct': False,
                          'scenario_update': 'Grafi normal geldi; ortopedi beklenirken çocuk saatlerce ağrı çekti.',
                          'teaching_point': 'İki günlük lokal tırnak kıvrımı şişliğinde kemik tutulumu beklenmez; '
                                            'grafi gerekmez.'},
                         {'text': 'Şişliği uçuk virüsüne bağlı kabul edip muayeneye gerek duymadan oral asiklovir '
                                  'başlamak ve ağrı kesici önermek',
                          'is_correct': False,
                          'scenario_update': 'Asiklovir verildi; apse büyüdü ve ağrı arttı.',
                          'teaching_point': 'Viral parmak enfeksiyonunda veziküller görülür; püy dolu koleksiyon '
                                            'bakteriyel apseyi gösterir.'},
                         {'text': 'Parmaktaki şişliği ilk günlerde sık görülen basit bir kızarıklık kabul edip muayene '
                                  'etmeden yalnız sıcak su pansumanına devam etmelerini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Koleksiyon tırnak altına uzandı ve tedavi daha karmaşık hale geldi.',
                          'teaching_point': 'Fluktuasyon varsa ılık banyo tek başına yeterli değildir; drenaj '
                                            'gerekir.'}]},
            {'stage_title': 'Girişim Kararı',
             'question': 'Fluktuasyonu olan bu lezyonda bir sonraki adımınız nedir?',
             'options': [{'text': 'Drenaj yapmadan ağızdan amoksisilin-klavulanat başlamak ve bir hafta içinde '
                                  'kendiliğinden açılmasını beklemek üzere aileyi bilgilendirmek',
                          'is_correct': False,
                          'scenario_update': 'Bir hafta antibiyotiğe rağmen apse sürdü ve tırnak altına yayıldı.',
                          'teaching_point': 'Apsede antibiyotik drenajın yerini tutmaz; fluktuan koleksiyon '
                                            'boşaltılmalıdır.'},
                         {'text': 'Dijital blok yapıp tırnak kıvrımını künt bir aletle veya bistüri sırtıyla tırnaktan '
                                  'kaldırarak koleksiyonu boşaltmak',
                          'is_correct': True,
                          'explanation': 'Tırnak kıvrımının kaldırılması çoğu zaman cilt kesisi gerektirmeden drenaj '
                                         'sağlar. Dijital blok işlemi ağrısız yapar.',
                          'new_finding': 'Dijital blok sonrası radiyal tırnak kıvrımı kaldırıldı, yaklaşık 0.5 mL koyu '
                                         'sarı püy boşaltıldı. Bölge serum fizyolojikle yıkandı. Ağrı belirgin '
                                         'azaldı.'},
                         {'text': 'Tırnağın tamamını çekmek için ortopedi veya el cerrahisine sevk etmek, işlem '
                                  'sonrasına kadar parmağa atel uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Tırnak çekimi gereksiz yere yapıldı; iyileşme süresi uzadı.',
                          'teaching_point': 'Tırnak kıvrımı apsesinde tırnak çekimi gerekmez; yalnızca tırnak altına '
                                            'uzanan apsede kısmi çıkarım düşünülür.'},
                         {'text': 'Koleksiyonu ince iğneyle birkaç kez aspire etmek ve kalan kısmın antibiyotikli '
                                  'kremle emilmesini beklemek',
                          'is_correct': False,
                          'scenario_update': 'Aspirasyon yetersiz kaldı; koleksiyon iki gün içinde yeniden doldu.',
                          'teaching_point': 'Yetersiz drenaj nüksle sonuçlanır; tırnak kıvrımı kaldırılarak tam '
                                            'boşaltım yapılmalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Herpetik dolama',
                          'is_correct': False,
                          'scenario_update': 'Vezikül yoktu ve drenajda püy geldi.',
                          'teaching_point': 'Herpetik dolamada gruplaşmış veziküller ve berrak sıvı vardır; kesi '
                                            'kontrendikedir.'},
                         {'text': 'Felon (pulpa apsesi)',
                          'is_correct': False,
                          'scenario_update': 'Pulpa yumuşak ve ağrısızdı.',
                          'teaching_point': 'Felonda parmak ucunun ön yüzünde gergin, şiddetli ağrılı şişlik olur.'},
                         {'text': 'Kronik paronişi',
                          'is_correct': False,
                          'scenario_update': 'Yakınma iki gündür vardı ve akut apse gelişmişti.',
                          'teaching_point': 'Kronik paronişi 6 haftayı aşan, sıklıkla ıslak işle ilişkili, birden '
                                            'fazla parmağı tutan tablodur.'},
                         {'text': 'Apseleşmiş akut paronişi',
                          'is_correct': True,
                          'explanation': 'Tırnak yeme öyküsü, tırnak kıvrımında akut, fluktuan ve püylü şişlik akut '
                                         'apseleşmiş paronişiyi gösterir.',
                          'new_finding': 'Tanı: Apseleşmiş akut paronişi.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Drenaj sonrası en uygun taburculuk planı hangisidir?',
             'options': [{'text': 'Günde 3-4 kez ılık su banyosu ve analjezi önermek, yayılan kızarıklık olmadığı için '
                                  'antibiyotik vermemek ve tırnak yemeyi bırakmasını desteklemek',
                          'is_correct': True,
                          'explanation': 'Yeterli drenaj sonrası ılık banyo iyileşmeyi hızlandırır. Selülit yoksa '
                                         'antibiyotik gerekmez. Tırnak yeme tekrarın en önemli nedenidir.',
                          'new_finding': 'Çocuk ılık banyo önerisiyle taburcu edildi. 48 saat sonraki kontrolde şişlik '
                                         've ağrı belirgin azalmıştı.'},
                         {'text': 'Drenaj sonrası enfeksiyonun tekrar etmemesi için iki hafta oral '
                                  'amoksisilin-klavulanat ve topikal steroidli antibiyotik krem önermek',
                          'is_correct': False,
                          'scenario_update': 'Uzun antibiyotik ishale neden oldu; steroidli krem iyileşmeye katkı '
                                             'sağlamadı.',
                          'teaching_point': 'Yeterli drenaj sonrası rutin uzun antibiyotik önerilmez; steroid enfekte '
                                            'alanda iyileşmeyi geciktirebilir.'},
                         {'text': 'Yarayı sıkı kapalı pansumanla kapatıp bir hafta ıslatmamasını ve pansumanı '
                                  'açmamasını söylemek, kontrol planlamamak',
                          'is_correct': False,
                          'scenario_update': 'Kapalı pansuman altında yara nemli kaldı ve yeniden püy birikti.',
                          'teaching_point': 'Drenaj sonrası ılık banyo ve açık iyileşme önerilir; kontrol '
                                            'planlanmalıdır.'},
                         {'text': 'Tekrarı önlemek için tırnak kıvrımına haftalık steroid enjeksiyonu planlamak ve '
                                  'parmağı birkaç gün tamamen hareketsiz tutmasını istemek',
                          'is_correct': False,
                          'scenario_update': 'Enjeksiyon gereksiz ağrıya neden oldu, hareketsizlik parmakta sertlik '
                                             'yaptı.',
                          'teaching_point': 'Akut paronişide steroid enjeksiyonunun yeri yoktur; tekrar önlemenin yolu '
                                            'tırnak yemeyi bırakmaktır.'}]}]},
 {'id': 'Y86',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '4 Yaşında (16 kg)',
  'gender': 'Kız',
  'complaint': 'Dünden beri yüksek ateş, kıvrandıran karın ağrısı ve günde on kez az miktarda kanlı-sümüksü dışkılama',
  'history': "Annesi anlatıyor: 'Dün öğlen ateşi 39.5°C'ye çıktı, karnına kramp girer gibi ağrıyor. Sonra çok sık "
             'tuvalete gitmeye başladı, her seferinde az miktarda kanlı, sümüklü dışkı yapıyor, ıkınıyor ama '
             "çıkmıyor.' Kreşte iki çocukta da ishal varmış. Kusma bir kez olmuş. İdrarını yapıyor. Havale geçirmemiş. "
             'Antibiyotik kullanmamış. Çiğ köfte veya az pişmiş et yemesi yok. Aşıları tam.',
  'final_diagnosis': 'Şigelloz (Shigella sonnei Dizanterisi)',
  'disposition': 'Oral Azitromisin, Ağızdan Rehidratasyon ve Kreş Kısıtlamasıyla Yeşil Alandan Taburculuk',
  'case_pearl': 'Ateş, kramp tarzında karın ağrısı, tenezm ve sık, az miktarda kanlı-mukuslu dışkı dizanteriyi '
                'düşündürür. Antibiyotik öncesi dışkı kültürü ve Shiga toksin testi gönderilmelidir; STEC '
                'enfeksiyonunda antibiyotik HÜS riskini artırabilir. Kanlı ishalde hemogram ve kreatinin HÜS taraması '
                "için faydalıdır. Türkiye'de ampisilin ve trimetoprim-sülfametoksazol direnci yüksektir. İlk seçenek "
                'azitromisindir (ilk gün 12 mg/kg, ardından 4 gün 6 mg/kg). Antimotilite ajanlardan kaçınılır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Ateş ve kanlı dışkısı olan bu çocukta ilk değerlendirmede neye odaklanırsınız?',
             'options': [{'text': 'Dehidratasyonu, genel görünümü ve karın muayenesini değerlendirmek; solukluk, idrar '
                                  'azlığı, ödem ve nöbet öyküsünü sorgulamak',
                          'is_correct': True,
                          'explanation': 'Kanlı ishalde dehidratasyonun yanında karın içi cerrahi nedenler, nörolojik '
                                         'tutulum ve böbrek tutulumunu düşündüren solukluk-idrar azlığı '
                                         'sorgulanmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 39.2°C, KTA 138/dk, SS 24/dk, TA 96/58 mmHg, KDZ 2 sn. '
                                         'Mukozalar hafif kuru, göz yaşı var. Karında alt kadranlarda yaygın '
                                         'hassasiyet, defans ve kitle yok, bağırsak sesleri artmış. Bezde az miktarda '
                                         'mukuslu, kanlı dışkı. Solukluk, ödem, peteşi yok. Bilinç açık, ense sertliği '
                                         'yok. Son 6 saatte iki kez idrar yapmış.'},
                         {'text': 'Dışkıdaki kan nedeniyle invajinasyon olasılığıyla muayeneyi kısa tutup acil batın '
                                  'ultrasonografisi ve çocuk cerrahisi konsültasyonu istemek',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografi normal geldi; yüksek ateşli ve sık dışkılamalı çocukta '
                                             'asıl tablo saatler sonra değerlendirilebildi.',
                          'teaching_point': 'Yüksek ateş, tenezm ve sık mukuslu dışkılama enfeksiyöz bir tabloyu '
                                            'düşündürür; önce tam klinik değerlendirme yapılmalıdır.'},
                         {'text': 'İshali azaltmak için hemen loperamid ve probiyotik vermek, karın ağrısı için '
                                  'buscopan yapıp ağrı geçince değerlendirmeye karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Loperamid sonrası karında şişlik ve ateşte artış oldu.',
                          'teaching_point': 'Kanlı ve ateşli ishalde antimotilite ajanları toksin ve bakteri '
                                            'klirensini azaltır, komplikasyon riskini artırır.'},
                         {'text': 'Ateşli kanlı ishali olduğu için muayene sonrası tetkik beklemeden ampirik oral '
                                  'trimetoprim-sülfametoksazol başlayıp ertesi gün kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik öncesi kültür alınmadı; ilaca rağmen ateş ve dışkılama '
                                             'sürdü.',
                          'teaching_point': 'Antibiyotik öncesi dışkı kültürü ve Shiga toksin testi alınmalıdır; '
                                            'bölgedeki direnç oranları ilaç seçimini belirler.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Bu çocukta hangi tetkikleri istersiniz?',
             'options': [{'text': 'Yalnızca dışkıda gizli kan ve rotavirüs-adenovirüs antijeni bakmak, kültür '
                                  'istemeden viral gastroenterit olarak izlemek ve evde izlem önermek',
                          'is_correct': False,
                          'scenario_update': 'Gizli kan pozitif, viral antijenler negatif geldi; etken saptanmadı ve '
                                             'tedavi planlanamadı.',
                          'teaching_point': 'Kanlı-ateşli ishalde bakteriyel kültür ve Shiga toksin testi gerekir; '
                                            'viral antijenler yeterli değildir.'},
                         {'text': 'Dışkı mikroskopisi, kültür ve Shiga toksin testi göndermek; kanlı ishal nedeniyle '
                                  'hemogram ve kreatinin istemek',
                          'is_correct': True,
                          'explanation': "Kültür etkeni ve duyarlılığı gösterir. Shiga toksin testi STEC'i dışlar. "
                                         'Hemogram ve kreatinin hemoliz, trombositopeni ve böbrek tutulumu açısından '
                                         'temel değerlendirmeyi sağlar.',
                          'new_finding': 'Dışkı mikroskopisi: her alanda bol lökosit ve eritrosit. Shiga toksin PCR '
                                         'negatif. Lökosit 14.800/mm³ (çomak %18), Hb 12.4 g/dL, trombosit '
                                         '286.000/mm³, kreatinin 0.38 mg/dL, Na 136 mmol/L. 48 saat sonra dışkı '
                                         'kültüründe laktoz fermente etmeyen, hareketsiz gram negatif basil üredi; '
                                         'ampisilin ve trimetoprim-sülfametoksazole dirençli, azitromisine duyarlı.'},
                         {'text': 'Ağrıyı değerlendirmek için kontrastlı batın bilgisayarlı tomografisi istemek ve '
                                  'sonucuna göre dışkı tetkiklerini planlamak',
                          'is_correct': False,
                          'scenario_update': 'Tomografi kalın bağırsak duvarında yaygın kalınlaşma gösterdi; etken ve '
                                             'tedavi seçimi için bilgi vermedi.',
                          'teaching_point': 'Enfeksiyöz kolitte görüntüleme etkeni göstermez; dışkı tetkikleri tanının '
                                            'temelidir.'},
                         {'text': 'Kan kültürü, CRP ve prokalsitonin istemek; prokalsitonin yüksekse intravenöz '
                                  'seftriaksonla servise yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Prokalsitonin 1.2 ng/mL geldi ve çocuk yatırıldı; dışkı kültürü '
                                             'alınmadığı için etken bilinmedi.',
                          'teaching_point': 'Genel durumu iyi çocukta parenteral tedavi gerekmez; dışkı kültürü '
                                            'atlanmamalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'STEC enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Shiga toksin PCR negatifti ve yüksek ateş vardı.',
                          'teaching_point': 'STEC enfeksiyonunda ateş genellikle yoktur veya hafiftir, Shiga toksin '
                                            'pozitiftir.'},
                         {'text': 'Şigelloz (basilli dizanteri)',
                          'is_correct': True,
                          'explanation': 'Yüksek ateş, tenezm, sık az miktarda kanlı-mukuslu dışkı, dışkıda bol '
                                         'lökosit, kreş salgını ve kültürde üreme şigellozu gösterir.',
                          'new_finding': 'Tanı: Şigelloz (S. sonnei).'},
                         {'text': 'İleokolik invajinasyon',
                          'is_correct': False,
                          'scenario_update': 'Ateş yüksekti, karında kitle yoktu ve dışkıda bol lökosit vardı.',
                          'teaching_point': 'İnvajinasyonda aralıklı ağlama krizleri, kitle ve çilek jölesi dışkı '
                                            'görülür; yüksek ateş beklenmez.'},
                         {'text': 'Kampilobakter enteriti',
                          'is_correct': False,
                          'scenario_update': 'Kültürde kampilobakter değil şigella üredi, kreş salgını vardı.',
                          'teaching_point': 'Kampilobakter sıklıkla az pişmiş tavuk ile ilişkilidir ve kültürle ayırt '
                                            'edilir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Ampirik olarak ampisilin 100 mg/kg/gün 5 gün başlamak ve ishali hızla kesmek için '
                                  'racekadotril ile loperamidi birlikte önermek',
                          'is_correct': False,
                          'scenario_update': 'Ampisiline dirençli suşta ateş ve dışkılama sürdü; loperamid karın '
                                             'şişkinliğine neden oldu.',
                          'teaching_point': 'Ülkemizde ampisilin direnci yüksektir. Antimotilite ajanları dizanteride '
                                            'kontrendikedir.'},
                         {'text': 'Antibiyotiğin taşıyıcılığı uzatacağını düşünerek hiç antibiyotik vermeden yalnız '
                                  'sıvı önermek ve ishal geçer geçmez kreşe göndermek',
                          'is_correct': False,
                          'scenario_update': 'Ateş ve dizanteri bir hafta sürdü, kreşte üç çocuk daha hastalandı.',
                          'teaching_point': 'Şigellozda antibiyotik hastalık süresini ve bulaşı azaltır; kreşe dönüş '
                                            'kurallara göre planlanmalıdır.'},
                         {'text': 'Azitromisin ilk gün 12 mg/kg, sonra 4 gün 6 mg/kg vermek; ağızdan rehidratasyon ve '
                                  'el hijyeni önermek, ishal geçene dek kreşe göndermemek',
                          'is_correct': True,
                          'explanation': 'Azitromisin duyarlı suşlarda etkilidir ve çocuklarda ilk seçenektir. El '
                                         'hijyeni ev içi bulaşı azaltır. Kreşe dönüş için ishalin bitmesi ve yerel '
                                         'kurallara göre kültür kontrolü gerekebilir.',
                          'new_finding': 'Azitromisin başlandı. 48. saatte ateş düştü, dışkı sayısı günde üçe indi. '
                                         'Beşinci gün dışkı normale döndü; kreşe dönüş halk sağlığı önerisine göre '
                                         'planlandı.'},
                         {'text': 'Ateş ve kan olduğu için 10 gün oral siprofloksasin ile birlikte metronidazol vermek '
                                  've iki hafta boyunca süt ürünlerini kesmek ve probiyotik eklemek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz geniş kombinasyon ve uzun süre bulantı ve iştahsızlık yaptı; '
                                             'süt kısıtlaması beslenmeyi bozdu.',
                          'teaching_point': 'Tek ve uygun ajanla kısa tedavi yeterlidir; rutin laktoz kısıtlaması '
                                            'gerekmez.'}]}]},
 {'id': 'Y87',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '15 Aylık (10 kg)',
  'gender': 'Erkek',
  'complaint': 'Ağlarken morarıp bayılma ve kısa süreli kasılma atakları',
  'history': "Annesi çok korkmuş: 'Bugün oyuncağını aldığımda çok ağladı, ağlarken sesi kesildi, dudakları morardı, "
             'sonra gevşeyip yere yığıldı. Birkaç kez kolları kasıldı, bir dakika içinde ağlayarak kendine geldi, '
             "sonra biraz uyudu.' Benzer atak son iki ayda üç kez olmuş, hepsi düştüğünde veya kızdığında. Ateş yok. "
             'Gelişimi normal. Günde 1 litreden fazla inek sütü içiyor, et ve sebze yemiyor. Ailede ani ölüm veya '
             'epilepsi yok.',
  'final_diagnosis': 'Siyanotik Katılma Nöbeti (Demir Eksikliği Anemisi Eşlikli)',
  'disposition': 'Demir Tedavisi, Beslenme Düzenlemesi ve Aile Eğitimiyle Yeşil Alandan Taburculuk',
  'case_pearl': 'Katılma nöbeti genellikle 6-18 ay arasında başlar. Ağlama veya ağrı gibi bir tetikleyicinin ardından '
                'ekspiryumda soluk tutma, siyanoz, bilinç kaybı ve bazen kısa kasılmalarla seyreder; nöbet '
                'tetikleyiciden önce başlamaz. Tanı öyküyle konur. Demir eksikliği sık eşlik eder ve demir tedavisi '
                'atak sıklığını azaltır. Tetikleyicisi belirsiz, solgun tip veya egzersizle gelen ataklarda EKG ile '
                'uzun QT dışlanmalıdır. Antiepileptik gerekmez. Ataklar genellikle 5-6 yaşta kaybolur.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Öykü',
             'question': 'Ağlarken morarıp bayılan bu çocukta ilk değerlendirmede en önemli adım nedir?',
             'options': [{'text': 'Olayın sırasını ayrıntılı sorgulamak; tetikleyici, ağlama, ses kesilmesi, morarma '
                                  've bilinç kaybının sırasını ve süresini öğrenip tam fizik muayene yapmak',
                          'is_correct': True,
                          'explanation': 'Tanı öyküye dayanır: tetikleyicinin olaydan önce gelmesi ve olayların sırası '
                                         'nöbetten ayırt ettirir. Solukluk ve muayene anemi gibi eşlik eden durumları '
                                         'gösterebilir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 118/dk, SS 26/dk, SpO2 %99. Çocuk aktif ve '
                                         'oynuyor. Konjonktivalar ve avuç içleri soluk. Kalp sesleri ritmik, üfürüm '
                                         'yok. Nörolojik muayene yaşına uygun, fokal bulgu yok. Annenin telefonundaki '
                                         'videoda: şiddetli ağlama, ekspiryumda sesin kesilmesi, dudaklarda morarma, '
                                         'gevşeme, iki kez kol kasılması ve 50 saniye içinde ağlayarak uyanma '
                                         'görülüyor.'},
                         {'text': 'Kasılma tarif edildiği için epileptik nöbet kabul edip hemen intravenöz '
                                  'levetirasetam yüklemesi yapmak ve nöroloji konsültasyonu istemek ve gece gözlemde '
                                  'tutmak',
                          'is_correct': False,
                          'scenario_update': 'Levetirasetam yüklendi; videoyu izleyen nörolog olayın epileptik '
                                             'olmadığını belirtti.',
                          'teaching_point': 'Tetikleyici ile başlayan morarma ve bilinç kaybını izleyen kısa '
                                            'kasılmalar beyin hipoksisine bağlıdır; antiepileptik endikasyonu yoktur.'},
                         {'text': 'Olayın bitmiş olduğunu ve çocuğun iyi göründüğünü belirterek öykü sorgulamadan ve '
                                  'muayene etmeden aileyi rahatlatıp eve göndermek',
                          'is_correct': False,
                          'scenario_update': "Aile yeniden atak olduğunda panikle 112'yi aradı; anemi saptanmadı ve "
                                             'tedavi edilmedi.',
                          'teaching_point': 'Her iyi görünen çocukta bile öykü ve muayene gerekir; eşlik eden anemi ve '
                                            'kardiyak nedenler atlanmamalıdır.'},
                         {'text': 'Morarma nedeniyle doğuştan kalp hastalığını dışlamak için öyküyü kısa tutup acil '
                                  'ekokardiyografi istemek ve kardiyoloji yatışı planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ekokardiyografi normal geldi; çocuk gereksiz yere yatırıldı.',
                          'teaching_point': 'Yalnızca ağlama sırasında olan geçici morarmada yapısal kalp hastalığı '
                                            'beklenmez; öykü ve muayene yönlendirir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Bu çocukta hangi tetkikler uygundur?',
             'options': [{'text': 'Uyku deprivasyonlu EEG ve kraniyal MR planlamak, sonuçları gelene kadar ailenin '
                                  'evde çocuğun ağlamasını engellemesini önermek ve nörolojiye sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'EEG ve MR normal geldi; sedasyon ve bekleme süresi aileyi yordu.',
                          'teaching_point': 'Tipik öyküde EEG ve görüntüleme tanıya katkı sağlamaz.'},
                         {'text': "Tam kan sayımı, ferritin ve EKG istemek; EKG'de QTc ve ritmi değerlendirip normal "
                                  'ise ek tetkik planlamamak',
                          'is_correct': True,
                          'explanation': 'Demir eksikliği sık eşlik eder ve tedavisi atakları azaltır. EKG uzun QT '
                                         'gibi kardiyak senkop nedenlerini dışlamak için basit bir tetkiktir.',
                          'new_finding': 'Hb 9.6 g/dL, MCV 62 fL, RDW %18, trombosit 412.000/mm³, ferritin 5 ng/mL. '
                                         'EKG: sinüs ritmi, QTc 410 ms, preeksitasyon yok.'},
                         {'text': 'Elektrolit, kalsiyum, magnezyum, glukoz, amonyak, laktat ve metabolik tarama '
                                  'testlerini kapsayan geniş bir panel istemek',
                          'is_correct': False,
                          'scenario_update': 'Tüm metabolik testler normal geldi; asıl eşlik eden sorun olan demir '
                                             'eksikliği bakılmadı.',
                          'teaching_point': 'Tetkikler öykü ve muayeneye göre seçilmelidir; geniş metabolik panel bu '
                                            'tabloda gereksizdir.'},
                         {'text': 'Lomber ponksiyon yapıp BOS incelemesi ve kültür istemek, sonuç gelene kadar çocuğu '
                                  'gözlem altında tutmak',
                          'is_correct': False,
                          'scenario_update': 'BOS normal geldi; ateşsiz ve iyi görünen çocuğa gereksiz invaziv girişim '
                                             'yapıldı.',
                          'teaching_point': 'Ateş ve meningeal bulgu olmadan BOS incelemesi endike değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Öykü ve tetkiklere göre en olası tanınız nedir?',
             'options': [{'text': 'Siyanotik katılma nöbeti',
                          'is_correct': True,
                          'explanation': 'Kızgınlık veya düşmeyle tetiklenen ağlama, ekspiryumda soluk kesilmesi, '
                                         'siyanoz, kısa bilinç kaybı ve hızlı düzelme siyanotik katılma nöbetini '
                                         'gösterir. Demir eksikliği anemisi eşlik etmektedir.',
                          'new_finding': 'Tanı: Siyanotik katılma nöbeti, demir eksikliği anemisi.'},
                         {'text': 'Fokal epileptik nöbet',
                          'is_correct': False,
                          'scenario_update': 'Olaylar her zaman tetikleyiciyle başlamış, kasılmalar morarma ve bilinç '
                                             'kaybından sonra gelmişti.',
                          'teaching_point': 'Epileptik nöbetler tetikleyiciye bağlı değildir ve siyanoz nöbetin '
                                            'sonucudur, nedeni değil.'},
                         {'text': 'Uzun QT sendromuna bağlı senkop',
                          'is_correct': False,
                          'scenario_update': "EKG'de QTc normaldi ve ailede ani ölüm yoktu.",
                          'teaching_point': 'Uzun QT senkopu egzersiz, ani ses veya yüzme ile tetiklenebilir; EKG tanı '
                                            'koydurur.'},
                         {'text': 'Basit febril konvülziyon',
                          'is_correct': False,
                          'scenario_update': 'Ataklar sırasında ateş yoktu.',
                          'teaching_point': 'Febril konvülziyon için ateş gerekir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun plan hangisidir?',
             'options': [{'text': 'Atakları önlemek için çocuğun her isteğini yerine getirmelerini ve ağlamasına hiç '
                                  'izin vermemelerini önermek, ek tedavi planlamamak',
                          'is_correct': False,
                          'scenario_update': 'Ataklar azalmadı ve çocukta davranış sorunları başladı.',
                          'teaching_point': 'Ataklardan korkup her isteği yerine getirmek davranışı pekiştirir; '
                                            'tutarlı ebeveyn yaklaşımı önerilir.'},
                         {'text': 'Atak sırasında çocuğu sarsmalarını, yüzüne soğuk su serpmelerini ve ağızdan suni '
                                  'solunum yapmalarını öğretmek',
                          'is_correct': False,
                          'scenario_update': 'Bir atak sırasında çocuk sarsıldı ve başını çarptı.',
                          'teaching_point': 'Atak sırasında çocuk güvenli bir yüzeyde yan yatırılır; sarsma ve suni '
                                            'solunum gereksiz ve zararlıdır.'},
                         {'text': 'Elementer demir 3 mg/kg/gün 3 ay vermek, süt tüketimini 500 mL altına indirip '
                                  'demirden zengin beslenme önermek; atakta yan yatırmayı öğretmek',
                          'is_correct': True,
                          'explanation': 'Demir tedavisi hem anemiyi düzeltir hem atak sıklığını azaltır. Ailenin '
                                         'zararsız ve geçici bir durum olduğunu bilmesi ve atakta güvenli pozisyonu '
                                         'öğrenmesi gerekir.',
                          'new_finding': "Demir başlandı, beslenme düzenlendi. Üç ay sonra Hb 11.8 g/dL'ye yükseldi; "
                                         'ataklar ayda bire indi ve sonra kayboldu.'},
                         {'text': 'Ataklar tekrarladığı için altı ay süreyle oral levetirasetam başlamak ve her atakta '
                                  'rektal diazepam uygulamalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Çocukta huzursuzluk ve uyku sorunları gelişti; ataklar azalmadı.',
                          'teaching_point': 'Antiepileptikler ve benzodiazepinler katılma nöbetini önlemez.'}]}]},
 {'id': 'Y88',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '10 Yaşında (32 kg)',
  'gender': 'Kız',
  'complaint': 'Bu sabah uyandığında yüzünün sağ tarafında kayma, sağ gözünü kapatamama ve ağzından su kaçırma',
  'history': "Annesi anlatıyor: 'Sabah dişlerini fırçalarken ağzından su kaçtı, sağ yanağı düşük, sağ gözünü tam "
             "kapatamıyor. Dün akşam sağ kulağının arkasında hafif ağrı olmuş. Yediklerinin tadı farklı geliyormuş.' "
             'Bir hafta önce soğuk algınlığı geçirmiş. Kulak akıntısı, kulakta kabarcık, baş ağrısı, kusma, kol veya '
             'bacakta güçsüzlük, konuşma bozukluğu yok. Kene ısırığı öyküsü yok.',
  'final_diagnosis': 'Bell Paralizisi (Sağ İdiyopatik Periferik Fasiyal Paralizi)',
  'disposition': 'Oral Prednizolon, Göz Koruması ve 1-2 Hafta Sonra Kontrolle Yeşil Alandan Taburculuk',
  'case_pearl': 'Periferik (alt motor nöron) fasiyal paralizide alın da tutulur; santral paralizide alın korunur. '
                'Kulak kanalında ve kulak kepçesinde veziküller Ramsay Hunt sendromunu, akıntılı kulak zarı otitis '
                'mediayı, parotis kitlesi tümörü, diğer kranyal sinir veya ekstremite bulguları santral bir nedeni '
                'düşündürür. Kan basıncı mutlaka ölçülmelidir. Tipik olguda görüntüleme gerekmez. İlk 72 saatte oral '
                'kortikosteroid önerilir. Göz kapağı kapanmıyorsa gündüz yapay gözyaşı, gece göz merhemi ve bantlama '
                'ile kornea korunmalıdır. Çocuklarda prognoz çok iyidir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Yüz felci ile gelen bu çocukta muayenede en kritik noktalar nelerdir?',
             'options': [{'text': 'Muayeneyi kısa tutup inme olasılığı nedeniyle çocuğu hemen acil kontrastsız beyin '
                                  'tomografisine göndermek ve sonuca göre karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi normal geldi; alın tutulumu ve kulak muayenesi '
                                             'değerlendirilmeden çocuk gereksiz radyasyon aldı.',
                          'teaching_point': 'Periferik ve santral paralizi ayrımı fizik muayeneyle yapılır; '
                                            'görüntüleme ancak atipik bulgularda gerekir.'},
                         {'text': 'Alnın tutulup tutulmadığını, göz kapanmasını, kulak kanalı ve zarını, parotisi, '
                                  'diğer kranyal sinirleri, ekstremite gücünü ve kan basıncını değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Alın tutulumu periferik lezyonu gösterir. Kulak, parotis ve diğer nörolojik '
                                         'bulgular ikincil nedenleri, kan basıncı da hipertansiyonu dışlamak için '
                                         'gereklidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 84/dk, TA 108/68 mmHg. Sağda alın '
                                         'kırışıklıkları kaybolmuş, kaş kaldıramıyor, göz kapağı tam kapanmıyor, '
                                         'kapamaya çalışınca göz küresi yukarı dönüyor. Sağ nazolabial oluk silik, '
                                         'ağız sola çekiliyor. Kulak kepçesi ve kanalında vezikül yok, kulak zarları '
                                         'normal. Parotis normal. Diğer kranyal sinirler, ekstremite gücü, refleksler '
                                         've serebellar testler normal. Kornea saydam.'},
                         {'text': 'Yüz kaymasını konversiyon bozukluğu kabul edip okul stresini sorgulamak ve '
                                  'psikiyatri polikliniğine yönlendirerek nörolojik muayeneyi atlamak',
                          'is_correct': False,
                          'scenario_update': 'Çocuk psikiyatriye yönlendirildi; göz koruması anlatılmadığı için kornea '
                                             'kurudu.',
                          'teaching_point': 'Nesnel fasiyal güçsüzlük nörolojik bir bulgudur; ayrıntılı muayene '
                                            'yapılmadan psikojenik tanı konmaz.'},
                         {'text': 'Soğuk algınlığı sonrası olduğu için viral nedenli kabul edip muayeneyi yüzle '
                                  'sınırlamak ve hemen oral asiklovir başlayarak taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Kan basıncı ve kulak değerlendirilmedi; tek başına antiviral tedavi '
                                             'iyileşmeyi hızlandırmadı.',
                          'teaching_point': 'Muayene ikincil nedenleri dışlamalıdır; antiviral tek başına '
                                            'önerilmez.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Alın tutulumu olan ve başka nörolojik bulgusu olmayan bu çocukta hangi tetkik yaklaşımı '
                         'uygundur?',
             'options': [{'text': 'Acil kraniyal MR ve kontrastlı temporal kemik tomografisi istemek, görüntüleme '
                                  'tamamlanmadan tedaviye başlamamak',
                          'is_correct': False,
                          'scenario_update': 'MR için randevu birkaç gün sonraya verildi; tedavi penceresi olan 72 '
                                             'saat kaçırıldı.',
                          'teaching_point': 'Tipik periferik paralizide görüntüleme gerekmez; 3 haftada düzelme '
                                            'başlamaz veya atipik bulgu varsa yapılır.'},
                         {'text': 'Lomber ponksiyon yapıp BOS hücre, protein ve viral PCR çalışmak, sonuçlar gelene '
                                  'dek çocuğu servise yatırmak',
                          'is_correct': False,
                          'scenario_update': 'BOS normal geldi; çocuk gereksiz yere yatırıldı ve invaziv girişim '
                                             'geçirdi.',
                          'teaching_point': 'İzole periferik paralizide BOS incelemesi endike değildir.'},
                         {'text': 'Kan basıncı ve kulak muayenesi normal olduğundan görüntüleme ve kan tetkiki '
                                  'istemeden klinik tanıyla tedaviye geçmek',
                          'is_correct': True,
                          'explanation': 'Tipik öykü ve muayenede tanı kliniktir. Lyme hastalığı endemik bölgede veya '
                                         'kene öyküsünde, bilateral tutulum ya da atipik seyirde tetkik planlanır.',
                          'new_finding': 'Tetkik istenmedi. Bulgular sağ tarafta izole periferik fasiyal sinir '
                                         'tutulumuyla uyumlu; başlangıçtan bu yana yaklaşık 10 saat geçmiş.'},
                         {'text': 'Elektromiyografi ve sinir iletim çalışması istemek, sonuçlarına göre kortikosteroid '
                                  'tedavisinin gerekip gerekmediğine karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Erken dönemde yapılan çalışma bilgi vermedi; steroid başlangıcı gecikti.',
                          'teaching_point': 'Elektrofizyolojik testler ilk günlerde anlamlı değildir ve tedavi '
                                            'kararını geciktirmemelidir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Ramsay Hunt sendromu',
                          'is_correct': False,
                          'scenario_update': 'Kulak kanalı ve kepçesinde vezikül yoktu.',
                          'teaching_point': "Ramsay Hunt'ta kulakta ağrılı veziküller ve sıklıkla işitme-denge "
                                            'tutulumu olur.'},
                         {'text': 'Akut iskemik inme',
                          'is_correct': False,
                          'scenario_update': 'Alın tutulmuştu ve başka nörolojik bulgu yoktu.',
                          'teaching_point': 'Santral yüz felcinde alın korunur ve genellikle kol-bacak bulguları eşlik '
                                            'eder.'},
                         {'text': 'Bell paralizisi',
                          'is_correct': True,
                          'explanation': 'Saatler içinde gelişen, alnı da tutan izole tek taraflı periferik fasiyal '
                                         'paralizi, kulak arkası ağrısı ve tat değişikliği, ikincil nedenler '
                                         'dışlandığında Bell paralizisini gösterir.',
                          'new_finding': 'Tanı: Sağ Bell paralizisi.'},
                         {'text': 'Otitis mediaya bağlı fasiyal paralizi',
                          'is_correct': False,
                          'scenario_update': 'Kulak zarları normaldi.',
                          'teaching_point': 'Otitis medianın komplikasyonu olan paralizide kulak zarı bombe ve '
                                            'hiperemiktir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Steroid yerine tek başına oral valasiklovir 7 gün başlamak ve göz kapağı '
                                  'kapanmadığı için gece gözü açık bırakıp nemli bezle silmelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'Antiviral tek başına yarar sağlamadı; gece açık kalan gözde kornea '
                                             'abrazyonu gelişti.',
                          'teaching_point': 'Tek başına antiviral önerilmez. Gece göz merhemi ve bantlama ile kornea '
                                            'korunmalıdır.'},
                         {'text': 'Oral prednizolon 1 mg/kg/gün 5 gün verip 5 günde azaltmak; gündüz yapay gözyaşı, '
                                  'gece göz merhemi ve bantlama önermek, 1-2 haftada kontrol',
                          'is_correct': True,
                          'explanation': 'İlk 72 saatte başlanan kortikosteroid iyileşme olasılığını artırır. Kornea '
                                         'koruması en önemli destek tedavidir. 3 haftada düzelme başlamazsa ileri '
                                         'değerlendirme yapılır.',
                          'new_finding': 'Prednizolon 30 mg/gün başlandı, göz bakımı gösterildi. İki hafta sonra göz '
                                         'kapanması tamdı; altıncı haftada yüz hareketleri tamamen normale döndü.'},
                         {'text': 'Kas zayıflığını önlemek için hemen yoğun elektrik stimülasyonu programı başlatmak, '
                                  'steroidi ancak ikinci haftada düzelme yoksa eklemek',
                          'is_correct': False,
                          'scenario_update': 'Steroid tedavi penceresi geçtikten sonra başlandı; elektrik stimülasyonu '
                                             'yüzde sinkinezi riskini artırdı.',
                          'teaching_point': 'Elektrik stimülasyonunun yararı gösterilmemiştir; steroid ilk 72 saatte '
                                            'başlanmalıdır.'},
                         {'text': 'Çocuklarda prognoz çok iyi olduğu için ilaç vermeden yalnızca yüz egzersizleri '
                                  'önermek ve göz bakımına gerek olmadığını söylemek',
                          'is_correct': False,
                          'scenario_update': 'Gece kapanmayan gözde kızarıklık ve ağrı gelişti; çocuk göz acile '
                                             'başvurdu.',
                          'teaching_point': 'Prognoz iyi olsa da steroid iyileşmeyi destekler ve göz koruması her '
                                            'olguda gereklidir.'}]}]},
 {'id': 'Y89',
  'category': '🦴 Kas-İskelet & Eklem / Ortopedik Aciller',
  'age': '8 Yaşında (27 kg)',
  'gender': 'Erkek',
  'complaint': 'Sabah uyandığında başlayan boyun ağrısı ve başını sağa çevirememe',
  'history': "Annesi anlatıyor: 'Dün akşam uzun yolculuk yaptık, arabada başını cama dayayıp uyudu. Bu sabah başı sola "
             "eğik kaldı, sağa çevirmeye çalışınca ağlıyor.' Düşme, çarpma, spor yaralanması yok. Ateş, boğaz ağrısı, "
             'yutma güçlüğü, salya akması, ses değişikliği, kusma, baş ağrısı, yürümede dengesizlik yok. Son iki '
             'haftada ilaç kullanmamış. Daha önce benzer yakınması olmamış.',
  'final_diagnosis': 'Kas Kaynaklı (Postüral) Akut Tortikolis',
  'disposition': 'Analjezi, Sıcak Uygulama ve Bir Hafta İçinde Düzelme Yoksa Kontrol Önerisiyle Yeşil Alandan '
                 'Taburculuk',
  'case_pearl': 'Çocukta akut tortikolisin en sık nedeni uygunsuz pozisyonda uyku sonrası gelişen kas spazmıdır. Ateş, '
                'yutma güçlüğü ve boyun hareketlerinde ağrı retrofarengeal apseyi; yakın zamanda geçirilmiş üst '
                'solunum yolu enfeksiyonu veya baş-boyun cerrahisi sonrası düzelmeyen tortikolis atlantoaksiyel '
                'rotatuar subluksasyonu; baş ağrısı, kusma veya ataksi posterior fossa kitlesini; ilaç öyküsü distonik '
                'reaksiyonu düşündürür. Tipik olguda görüntüleme gerekmez. Bir haftada düzelmeyen olgu yeniden '
                'değerlendirilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Başını çeviremeyen bu çocukta muayenede hangi bulguları özellikle ararsınız?',
             'options': [{'text': 'Ateşi, ağız içi ve farenksi, boyun lenf nodlarını, kas spazmının tarafını, '
                                  'nörolojik bulguları, yürüyüşü ve göz hareketlerini değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Ateş ve farenks bulguları derin boyun enfeksiyonunu, nörolojik ve serebellar '
                                         'bulgular santral nedenleri dışlar. Kas spazmının tarafı ve hareket '
                                         'kısıtlılığı tabloyu tanımlar.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 88/dk. Baş sola eğik, çene hafif sağa '
                                         'dönük. Sol sternokleidomastoid kasında gerginlik ve hassasiyet. Sağa '
                                         'rotasyon ve sola eğilme ağrılı ve kısıtlı. Farenks normal, uvula orta hatta, '
                                         'salya yok, lenf nodu büyük değil. Nörolojik muayene, göz hareketleri, '
                                         'yürüyüş ve serebellar testler normal. Orta hatta kemik hassasiyeti yok.'},
                         {'text': 'Boyun yaralanması olasılığıyla hemen boyunluk takıp sırt tahtasına almak ve muayene '
                                  'etmeden servikal tomografi istemek ve ortopediye danışmak',
                          'is_correct': False,
                          'scenario_update': 'Tomografi normal geldi; travma öyküsü olmayan çocuk gereksiz '
                                             'immobilizasyon ve radyasyona maruz kaldı.',
                          'teaching_point': 'Travma öyküsü olmayan çocukta spinal immobilizasyon ve tomografi '
                                            'gerekmez.'},
                         {'text': 'Boynu düzeltmek için hızlı bir manevrayla başı orta hatta getirmeye çalışmak, '
                                  'ardından muayeneyi tamamlamak',
                          'is_correct': False,
                          'scenario_update': 'Manevra çocukta şiddetli ağrıya neden oldu ve kas spazmı arttı.',
                          'teaching_point': 'Zorlayıcı manipülasyon zararlıdır; altta yatan neden belirlenmeden boyun '
                                            'zorla döndürülmez.'},
                         {'text': 'Ağrıyı ilaca bağlı bir kasılma kabul edip öyküyü sorgulamadan intravenöz biperiden '
                                  'uygulamak ve yanıtı gözlemek',
                          'is_correct': False,
                          'scenario_update': 'Biperiden sonrası çocukta ağız kuruluğu ve huzursuzluk oldu, boyun '
                                             'pozisyonu değişmedi.',
                          'teaching_point': 'İlaç öyküsü olmadan antikolinerjik tedavi gereksizdir; önce öykü ve '
                                            'muayene yapılmalıdır.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Ateşi ve nörolojik bulgusu olmayan bu çocukta hangi yaklaşım uygundur?',
             'options': [{'text': 'Boyun ön-arka ve yan grafisi çekmek, grafi normalse servikal MR ile bağ '
                                  'yaralanmasını dışlamak üzere randevu vermek ve kontrol grafisi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Grafide yalnızca kas spazmına bağlı lordoz düzleşmesi görüldü; MR '
                                             'gereksiz bekleme yarattı.',
                          'teaching_point': 'Travmasız tipik tortikoliste grafi ve MR yönetimi değiştirmez.'},
                         {'text': 'Tam kan sayımı, CRP ve sedimantasyon istemek, değerler yüksekse derin boyun '
                                  'enfeksiyonu açısından kontrastlı tomografi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Tüm değerler normal geldi; çocuk kan alımıyla gereksiz yere strese '
                                             'girdi.',
                          'teaching_point': 'Ateş, yutma güçlüğü ve farenks bulgusu olmadan kan tetkiki gerekmez.'},
                         {'text': 'Görüntüleme ve kan tetkiki istemeden tedaviye başlamak; ateş, yutma güçlüğü, '
                                  'nörolojik bulgu veya bir haftada düzelmeme olursa yeniden değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Tipik öykü ve normal muayenede tanı kliniktir. Uyarı bulguları tanımlanır ve '
                                         'bir haftada düzelmeyen olguda görüntüleme planlanır.',
                          'new_finding': 'Tetkik istenmedi. İbuprofen sonrası 45 dakikada ağrı azaldı ve rotasyon '
                                         'açıklığı arttı.'},
                         {'text': 'Acil kontrastlı boyun ve beyin tomografisini birlikte istemek ve sonuç gelene dek '
                                  'çocuğu ağızdan beslemeden bekletmek',
                          'is_correct': False,
                          'scenario_update': 'Tomografiler normal geldi; çocuk saatlerce aç bekletildi ve gereksiz '
                                             'radyasyon aldı.',
                          'teaching_point': 'Uyarı bulgusu olmadan ileri görüntüleme önerilmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Atlantoaksiyel rotatuar subluksasyon',
                          'is_correct': False,
                          'scenario_update': 'Yakında üst solunum yolu enfeksiyonu yoktu ve analjeziyle hareket '
                                             'açıklığı arttı.',
                          'teaching_point': "Rotatuar subluksasyonda kafa 'horoz pozisyonunda' sabittir ve analjeziyle "
                                            'düzelmez; BT gerekir.'},
                         {'text': 'Retrofarengeal apse',
                          'is_correct': False,
                          'scenario_update': 'Ateş, yutma güçlüğü, salya ve farenks bulgusu yoktu.',
                          'teaching_point': 'Retrofarengeal apsede ateş, boyun ekstansiyonunda ağrı ve yutma güçlüğü '
                                            'olur.'},
                         {'text': 'Kas kaynaklı (postüral) akut tortikolis',
                          'is_correct': True,
                          'explanation': 'Uygunsuz pozisyonda uyku sonrası başlayan, ateşsiz, nörolojik bulgusuz ve '
                                         'analjeziyle hareket açıklığı artan tortikolis kas kaynaklıdır.',
                          'new_finding': 'Tanı: Kas kaynaklı (postüral) akut tortikolis.'},
                         {'text': 'Akut distonik reaksiyon',
                          'is_correct': False,
                          'scenario_update': 'Son iki haftada ilaç kullanımı yoktu.',
                          'teaching_point': 'Distonik reaksiyon dopamin antagonisti ilaçlardan sonra görülür ve göz, '
                                            'dil tutulumu eşlik edebilir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun plan hangisidir?',
             'options': [{'text': 'Üç hafta sert boyunluk takmasını ve boynunu hiç hareket ettirmemesini önermek, '
                                  'okuldan rapor vermek',
                          'is_correct': False,
                          'scenario_update': 'Uzun süre hareketsiz kalan boyunda sertlik arttı ve iyileşme gecikti.',
                          'teaching_point': 'Uzun süreli boyunluk kas sertliğini artırır; erken ve nazik hareket '
                                            'önerilir.'},
                         {'text': 'İbuprofen 10 mg/kg günde üç kez 3-5 gün, sıcak uygulama ve nazik germe egzersizleri '
                                  'önermek; bir haftada düzelmezse kontrole gelmesini söylemek',
                          'is_correct': True,
                          'explanation': 'Analjezi ve sıcak uygulama kas spazmını çözer, nazik hareket iyileşmeyi '
                                         'hızlandırır. Bir haftada düzelmeme veya uyarı bulguları yeniden '
                                         'değerlendirme gerektirir.',
                          'new_finding': 'Çocuk ibuprofen ve sıcak uygulama önerileriyle taburcu edildi. Üçüncü gün '
                                         'boyun hareketleri tamamen normale döndü.'},
                         {'text': 'Kas gevşetici olarak oral diazepam başlamak ve boynun hızla düzelmesi için ertesi '
                                  'gün manuel manipülasyon seansı planlamak',
                          'is_correct': False,
                          'scenario_update': 'Diazepam çocukta aşırı uyku hali yaptı; manipülasyon önerisi gereksiz '
                                             'risk oluşturdu.',
                          'teaching_point': 'Çocuklarda benzodiazepin kas gevşetici olarak önerilmez; boyun '
                                            'manipülasyonu ciddi komplikasyon riski taşır.'},
                         {'text': 'Altta yatan bir enfeksiyonu önlemek için 7 gün amoksisilin-klavulanat başlamak ve '
                                  'iki gün sonra kontrol grafisi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik ishal yaptı ve kontrol grafisi gereksiz radyasyon oldu.',
                          'teaching_point': 'Enfeksiyon bulgusu olmayan kas kaynaklı tabloda antibiyotik ve kontrol '
                                            'grafisi gerekmez.'}]}]},
 {'id': 'Y90',
  'category': '💧 Sıvı-Elektrolit & Renal / Ürolojik Aciller',
  'age': '4 Yaşında (16 kg)',
  'gender': 'Erkek',
  'complaint': 'İki gündür penis ucunda kızarıklık, şişlik, ağrı ve idrar yaparken yanma',
  'history': "Annesi anlatıyor: 'İki gündür pipisinin ucu kıpkırmızı ve şiş, sarı bir akıntı var. İşerken ağlıyor ama "
             "idrarını yapıyor. Sünnetli değil. Derisini temizlemek için geri çekmeye çalıştım ama açılmıyor.' Ateş "
             'yok, karın ağrısı ve kusma yok. Bir hafta önce boğaz ağrısı olmuş, kardeşi de boğaz enfeksiyonu '
             'geçirmiş. Bebek bezini bırakmış, kendi tuvaletini yapıyor.',
  'final_diagnosis': 'Akut Bakteriyel Balanopostit (A Grubu Streptokok)',
  'disposition': 'Oral Amoksisilin, Ilık Oturma Banyosu ve Hijyen Eğitimiyle Yeşil Alandan Taburculuk',
  'case_pearl': 'Balanopostit sünnetsiz erkek çocuklarda glans ve sünnet derisinin iltihabıdır; sıklıkla hijyen sorunu '
                've irritasyonla ilişkilidir. Pürülan akıntı ve belirgin eritemde, özellikle yakın zamanda farenjit '
                'öyküsü varsa A grubu streptokok düşünülür ve sürüntü kültürü alınır. Sünnet derisi zorla geri '
                'çekilmemelidir; çocuklarda fizyolojik yapışıklık normaldir. İdrar retansiyonu ve derinin glansın '
                'arkasında sıkışması (parafimozis) acil durumlardır. Tek atak sünnet endikasyonu değildir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Penis ucunda kızarıklık ve akıntı olan bu çocukta muayenede neye dikkat edersiniz?',
             'options': [{'text': 'Sünnet derisinin pozisyonunu, glansın görünümünü, akıntının niteliğini, idrar '
                                  'akımını, inguinal bölgeyi ve skrotumu sünnet derisini zorlamadan değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Derinin glans arkasında sıkışıp sıkışmadığı ve idrar akımı acil durumları '
                                         'dışlar. Pürülan akıntı enfeksiyon için kültür kararını belirler. Zorla geri '
                                         'çekme travmaya yol açar.',
                          'new_finding': 'Ateş 36.9°C, genel durum iyi. Sünnet derisi glansı örtüyor, glans arkasında '
                                         'sıkışma yok. Prepisyum ve görülebilen glans kenarı parlak kırmızı ve ödemli, '
                                         'ağızda sarı pürülan akıntı. Meatus prepisyum açıklığından görülüyor, çocuk '
                                         'muayene sırasında ince ama kesintisiz akımla idrar yaptı. Skrotum ve '
                                         'testisler normal. İnguinal bölgede küçük hassas lenf nodları.'},
                         {'text': 'Glansı tam görmek ve akıntıyı temizlemek için sünnet derisini muayene sırasında '
                                  'zorlayarak geri çekmek ve altını antiseptikle silmek',
                          'is_correct': False,
                          'scenario_update': 'Zorla geri çekilen deri glans arkasında sıkıştı ve çocukta şiddetli ağrı '
                                             'ile ödem gelişti.',
                          'teaching_point': 'Küçük çocukta sünnet derisi fizyolojik olarak yapışıktır; zorla geri '
                                            'çekmek travmaya ve parafimozise yol açar.'},
                         {'text': 'İdrar yaparken yanma olduğu için idrar yolu enfeksiyonu kabul edip penisi muayene '
                                  'etmeden idrar tetkiki ve kültürü istemek',
                          'is_correct': False,
                          'scenario_update': 'İdrar örneği akıntıyla kontamine oldu ve sonuç yorumlanamadı; lokal '
                                             'tablo değerlendirilmedi.',
                          'teaching_point': 'Lokal iltihapta idrarın iltihaplı alandan geçmesi yanmaya neden olur; '
                                            'önce genital muayene yapılır.'},
                         {'text': 'Muayene sonrası hemen çocuk cerrahisine sevk edip acil sünnet planlamak, o zamana '
                                  'kadar ağrı kesici vermek',
                          'is_correct': False,
                          'scenario_update': 'Akut iltihap döneminde cerrahi planlanması uygun bulunmadı ve aile '
                                             'gereksiz yere sevk edildi.',
                          'teaching_point': 'Akut iltihapta sünnet yapılmaz; tek atak sünnet endikasyonu değildir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Pürülan akıntısı olan, idrarını yapabilen bu çocukta hangi yaklaşım uygundur?',
             'options': [{'text': 'Tam kan sayımı, CRP ve kan kültürü istemek, değerler yüksekse intravenöz '
                                  'antibiyotikle servise yatırmak ve kültürleri beklemek',
                          'is_correct': False,
                          'scenario_update': 'Değerler normal geldi; iyi görünen çocuk gereksiz yere kan alımı '
                                             'geçirdi.',
                          'teaching_point': 'Sistemik bulgusu olmayan lokal genital enfeksiyonda kan tetkiki '
                                            'gerekmez.'},
                         {'text': 'Penis ve skrotum ultrasonografisi istemek ve sonucu gelene kadar çocuğu acil '
                                  'serviste bekletmek',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografi yalnızca yüzeyel ödem gösterdi; tanıya katkı sağlamadı.',
                          'teaching_point': 'Yüzeyel iltihapta görüntüleme gerekmez.'},
                         {'text': 'Akıntıdan sürüntü kültürü almak ve yakın zamanda boğaz enfeksiyonu öyküsü nedeniyle '
                                  'hızlı strep testi uygulamak',
                          'is_correct': True,
                          'explanation': 'Pürülan akıntıda etken belirlenmesi tedaviyi yönlendirir. Yakın farenjit '
                                         'öyküsü ve belirgin eritem A grubu streptokoku düşündürür.',
                          'new_finding': 'Akıntıdan alınan sürüntüde hızlı strep antijen testi pozitif. Kültür 48 saat '
                                         'sonra A grubu beta-hemolitik streptokok olarak bildirildi.'},
                         {'text': 'İdrar sondası takıp kateter idrarından kültür almak ve sonuç gelene kadar sondayı '
                                  'yerinde bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Sonda takılırken ödemli doku travmatize oldu ve çocuk çok ağladı.',
                          'teaching_point': 'İdrar yapabilen çocukta sonda gerekmez ve iltihaplı dokuda travma riski '
                                            'taşır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Parafimozis (sıkışmış prepisyum)',
                          'is_correct': False,
                          'scenario_update': 'Sünnet derisi glansı örtüyordu, glans arkasında sıkışma yoktu.',
                          'teaching_point': 'Parafimoziste geri çekilmiş deri glans arkasında halka şeklinde sıkışır '
                                            've glans ödemlenir.'},
                         {'text': 'Akut bakteriyel balanopostit',
                          'is_correct': True,
                          'explanation': 'Sünnetsiz çocukta glans ve prepisyumda eritem, ödem, pürülan akıntı ve '
                                         'pozitif streptokok testi akut bakteriyel balanopostiti gösterir.',
                          'new_finding': 'Tanı: Akut bakteriyel balanopostit (A grubu streptokok).'},
                         {'text': 'Fimozise bağlı idrar retansiyonu',
                          'is_correct': False,
                          'scenario_update': 'Çocuk muayene sırasında kesintisiz akımla idrar yaptı.',
                          'teaching_point': 'Retansiyonda mesane dolgun ve ele gelir, çocuk işeyemez.'},
                         {'text': 'Kandidiyal balanit',
                          'is_correct': False,
                          'scenario_update': 'Satellit lezyonlar ve beyaz plak yoktu, streptokok testi pozitifti.',
                          'teaching_point': 'Kandida enfeksiyonunda uydu lezyonlar ve beyaz plaklar görülür.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Yalnızca topikal kortikosteroid krem sürmelerini ve sünnet derisini her gün geri '
                                  'çekip içini sabunla yıkamalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Steroid krem enfeksiyonu ilerletti, zorla geri çekme ağrı ve küçük '
                                             'yırtıklara neden oldu.',
                          'teaching_point': 'Bakteriyel enfeksiyonda tek başına steroid uygun değildir ve deri zorla '
                                            'geri çekilmemelidir.'},
                         {'text': 'Ağızdan amoksisilin 10 gün, günde iki-üç kez ılık oturma banyosu ve analjezi '
                                  'önermek; işeyemezse veya deri geride sıkışırsa hemen dönmelerini söylemek',
                          'is_correct': True,
                          'explanation': 'A grubu streptokok enfeksiyonu sistemik antibiyotikle tedavi edilir. Ilık '
                                         'banyo ödemi ve ağrıyı azaltır. İdrar retansiyonu ve parafimozis uyarı '
                                         'bulgularıdır.',
                          'new_finding': 'Amoksisilin ve ılık banyo önerisiyle taburcu edildi. Üçüncü gün akıntı '
                                         'kesildi, yedinci gün kızarıklık tamamen geçti.'},
                         {'text': 'Tek doz intramüsküler seftriakson yapıp tedaviyi tamamlanmış saymak ve aynı hafta '
                                  'içinde elektif sünnet randevusu vermek',
                          'is_correct': False,
                          'scenario_update': 'Tek doz yetersiz kaldı ve akıntı tekrarladı; iltihaplı dönemde sünnet '
                                             'planı uygun bulunmadı.',
                          'teaching_point': 'Tek doz seftriakson streptokok enfeksiyonunda yeterli değildir; iltihap '
                                            'geçmeden cerrahi planlanmaz.'},
                         {'text': 'Antibiyotikli göz pomadı ile topikal mupirosin sürmek ve ağrı geçene kadar çocuğun '
                                  'su içmesini kısıtlayarak idrar sayısını azaltmak',
                          'is_correct': False,
                          'scenario_update': 'Su kısıtlaması sonrası idrar konsantre hale geldi ve yanma arttı.',
                          'teaching_point': 'Sıvı kısıtlaması yanmayı artırır; bol sıvı ve ılık banyo önerilir.'}]}]}]
