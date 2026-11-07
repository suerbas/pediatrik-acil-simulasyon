# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Yeşil Alan Vakaları (Part 8: Y71 - Y80)
"""

GREEN_CASES_PART8 = [{'id': 'Y71',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '4 Yaşında',
  'gender': 'Erkek',
  'complaint': "Üç gündür 39°C'ye çıkan ateş, boğaz ağrısı ve iki gözde kızarıklık",
  'history': "Annesi anlatıyor: 'Üç gündür ateşi 39°C'ye çıkıyor, ateş düşürücüyle iniyor. Boğazı ağrıyor, yemek yemek "
             "istemiyor. Dün iki gözü de kızardı, sulanıyor ama çapak yok. Burnu akıyor.' Kreşe gidiyor, sınıfta "
             "birkaç çocukta 'göz nezlesi' varmış. Hafta sonu kapalı yüzme havuzuna gitmişler. Döküntü, ishal yok. "
             'Aşıları tam. Tartı: 17 kg.',
  'final_diagnosis': 'Faringokonjonktival Ateş (Adenovirüs Enfeksiyonu)',
  'disposition': 'Destek Tedavisi ve Hijyen Önerileriyle Yeşil Alandan Taburculuk',
  'case_pearl': 'Ateş, farenjit ve bilateral eksüdasız konjonktivitin birlikteliği adenovirüse bağlı '
                'faringokonjonktival ateşi düşündürür; havuz ve kreş salgınları tipiktir. Belirgin viral bulgular '
                '(konjonktivit, burun akıntısı, öksürük) varken AGBHS testi önerilmez. Ateş 5-7 gün sürebilir ve CRP '
                'yüksek olabilir. Ateş 5 günü aşarsa Kawasaki hastalığı yeniden değerlendirilmelidir. Tedavi '
                'destekleyicidir; antibiyotiğin yeri yoktur.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Ateş, boğaz ağrısı ve göz kızarıklığı olan bu çocukta muayenede nelere dikkat edersiniz?',
             'options': [{'text': 'Göz kızarıklığını bakteriyel kabul edip muayeneyi gözle sınırlı tutmak, '
                                  'antibiyotikli göz damlası yazarak boğaz ağrısı için yalnız gargara önermek',
                          'is_correct': False,
                          'scenario_update': 'Göz damlası başlandı; ateş ve boğaz ağrısı sürdü, sistemik değerlendirme '
                                             'yapılmadı.',
                          'teaching_point': 'Ateşli çocukta göz bulgusu sistemik tablonun parçası olabilir; tam '
                                            'muayene yapılmalıdır.'},
                         {'text': 'Hidrasyonu ve genel durumu değerlendirip farenks, tonsiller, konjonktiva, kornea, '
                                  'kulaklar, lenf nodları, deri ve el-ayak bulgularını sistematik muayene etmek',
                          'is_correct': True,
                          'explanation': 'Konjonktivitin eksüdalı olup olmaması, limbusun korunması, lenf nodu '
                                         'dağılımı, döküntü ve el-ayak bulguları viral, bakteriyel ve vaskülitik '
                                         'tabloları ayırır.',
                          'new_finding': 'Vital Bulgular: Ateş 39.1°C, KTA 128/dk, SS 24/dk, SpO2 %99, KDZ 2 sn. '
                                         'Hidrasyonu iyi. Farenks hiperemik, tonsiller 2+ ve ince beyaz eksüdalı. '
                                         'Bilateral foliküler, eksüdasız konjonktivit, kornea saydam, fotofobi yok. '
                                         'Bilateral preaüriküler ve anterior servikal küçük hassas lenf nodları. '
                                         'Berrak burun akıntısı. Dudaklar normal, döküntü ve el-ayak değişikliği yok. '
                                         'Kulak zarları normal.'},
                         {'text': 'Ateş ve konjonktival kızarıklık birlikteliği nedeniyle muayeneyi tamamlamadan '
                                  'çocuğu Sarı Alana alıp ekokardiyografi ve inflamatuvar belirteç istemek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk Sarı Alanda saatlerce bekletildi; ekokardiyografi normal geldi ve '
                                             'tablo henüz üçüncü gündeydi.',
                          'teaching_point': 'Üçüncü gündeki ateş ve eksüdasız konjonktivit tek başına ileri tetkik '
                                            'gerektirmez; muayene bulguları birlikte değerlendirilmelidir.'},
                         {'text': 'Tonsil eksüdası nedeniyle muayeneyi kısa tutup hemen amoksisilin başlamak ve göz '
                                  'bulgusunun antibiyotikle birlikte geçeceğini aileye açıklamak',
                          'is_correct': False,
                          'scenario_update': 'Amoksisilin başlandı; ateş yedinci güne dek sürdü ve aile antibiyotiğin '
                                             'işe yaramadığını düşünerek tekrar başvurdu.',
                          'teaching_point': 'Tonsil eksüdası viral enfeksiyonlarda da görülür; antibiyotik kararı '
                                            'klinik ve test birlikte değerlendirilerek verilmelidir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Bu çocukta hangi tetkik yaklaşımı en uygundur?',
             'options': [{'text': 'Tonsil eksüdası bulunduğu için boğazdan hızlı strep antijen testi ve kültür almak, '
                                  'test sonucu negatif çıkarsa yine de kültürü bekleyip antibiyotiği sürdürmek',
                          'is_correct': False,
                          'scenario_update': 'Hızlı test negatif geldi, kültür 48 saat sürdü; bu sürede çocuk gereksiz '
                                             'antibiyotik aldı.',
                          'teaching_point': 'Konjonktivit, burun akıntısı gibi belirgin viral bulgular varken AGBHS '
                                            'testi önerilmez; taşıyıcılık nedeniyle yanıltıcı olabilir.'},
                         {'text': 'Belirgin viral bulgular nedeniyle strep testi yapmamak; antibiyotik isteyen aileye '
                                  'kanıt sunmak için göz sürüntüsünden hızlı viral antijen testi bakmak',
                          'is_correct': True,
                          'explanation': 'Viral bulgular güçlü olduğunda bakteriyel test yapılmaz. Hızlı viral antijen '
                                         'testi tanıyı destekler ve gereksiz antibiyotik kullanımını azaltır.',
                          'new_finding': 'Konjonktival sürüntüde hızlı viral antijen testi pozitif.'},
                         {'text': 'Ateşin üç gündür sürmesi nedeniyle hemogram, CRP, sedimantasyon ve kan kültürü '
                                  'istemek, CRP yüksekse oral antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'Lökosit 16.800/mm³, CRP 58 mg/L geldi; antibiyotik başlandı, ancak '
                                             'ateşin seyri değişmedi.',
                          'teaching_point': 'Bazı viral enfeksiyonlarda CRP ve lökosit belirgin yüksek olabilir; bu '
                                            'değerler tek başına antibiyotik kararı için yeterli değildir.'},
                         {'text': 'Göz tutulumunu değerlendirmek için acil göz hastalıkları konsültasyonu istemek ve '
                                  'konjonktival kültür sonucuna göre damla tedavisini planlamak',
                          'is_correct': False,
                          'scenario_update': 'Konsültasyon için saatlerce beklendi; kültür birkaç gün sonra normal '
                                             'flora olarak raporlandı.',
                          'teaching_point': 'Kornea tutulumu, görme kaybı veya fotofobi olmadıkça eksüdasız '
                                            'konjonktivitte göz konsültasyonu ve kültür gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Streptokoksik tonsillofarenjit',
                          'is_correct': False,
                          'scenario_update': 'Konjonktivit ve burun akıntısı gibi belirgin viral bulgular vardı.',
                          'teaching_point': 'Streptokoksik farenjitte konjonktivit, burun akıntısı ve öksürük '
                                            'beklenmez.'},
                         {'text': 'Faringokonjonktival ateş',
                          'is_correct': True,
                          'explanation': 'Ateş, eksüdatif farenjit, bilateral foliküler konjonktivit, preaüriküler '
                                         'lenfadenopati, havuz ve kreş teması ile pozitif viral antijen testi '
                                         'adenovirüse bağlı faringokonjonktival ateşi gösterir.',
                          'new_finding': 'Tanı: Faringokonjonktival ateş (adenovirüs).'},
                         {'text': 'Kawasaki hastalığı (erken dönem)',
                          'is_correct': False,
                          'scenario_update': 'Ateş henüz üçüncü gündeydi, dudak, döküntü ve el-ayak bulguları yoktu, '
                                             'konjonktivit foliküler ve preaüriküler lenfadenopatiliydi.',
                          'teaching_point': 'Kawasaki konjonktiviti limbusu koruyan, eksüdasız, foliküler olmayan '
                                            'tiptedir; ateş 5 günü geçerse yeniden değerlendirilmelidir.'},
                         {'text': 'Kızamık prodrom dönemi',
                          'is_correct': False,
                          'scenario_update': 'Aşıları tamdı, Koplik lekesi yoktu ve öksürük belirgin değildi.',
                          'teaching_point': 'Kızamık prodromunda ateş, öksürük, burun akıntısı, konjonktivit ve Koplik '
                                            'lekeleri görülür.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi ve taburculuk planı hangisidir?',
             'options': [{'text': 'Viral olsa da sekonder bakteriyel enfeksiyonu önlemek için 10 gün amoksisilin '
                                  'başlamak ve göz için antibiyotikli damla eklemek',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik sonrası ishal gelişti; hastalığın süresi değişmedi.',
                          'teaching_point': 'Profilaktik antibiyotik viral enfeksiyonda sekonder enfeksiyonu önlemez '
                                            've yan etki riski taşır.'},
                         {'text': 'Göz kızarıklığını hızla geçirmek için kortikosteroid içeren göz damlası başlamak ve '
                                  'ateş için aspirin önermek, bir hafta sonra kontrol planlamak',
                          'is_correct': False,
                          'scenario_update': 'Steroidli damla viral replikasyonu uzattı; aspirin çocukta Reye sendromu '
                                             'riski nedeniyle kesildi.',
                          'teaching_point': 'Viral konjonktivitte rutin steroidli damla ve çocukta ateş için aspirin '
                                            'kullanılmaz.'},
                         {'text': 'Parasetamol 15 mg/kg veya ibuprofen 10 mg/kg, bol sıvı ve el hijyeni önermek; ateş '
                                  '5 günü aşarsa ya da gözde ağrı gelişirse dönmelerini söylemek',
                          'is_correct': True,
                          'explanation': 'Tedavi destekleyicidir. Göz salgıları çok bulaşıcı olduğundan havlu '
                                         'ayrılmalı ve el yıkama vurgulanmalıdır. Ateşin uzaması ayırıcı tanının '
                                         'yeniden değerlendirilmesini gerektirir.',
                          'new_finding': 'Aile bilgilendirildi. Ateş beşinci gün kendiliğinden düştü, göz bulguları '
                                         'ikinci haftada geriledi. Kreşe ateşsiz 24 saat sonra dönmesi önerildi.'},
                         {'text': 'Çocuğun boğaz ağrısı için viskoz lidokain gargarası ve antihistaminik şurup vermek, '
                                  'kreşe ateş düştüğü gün hemen dönebileceğini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk lidokaini yuttu ve uyuşukluk yakınması oldu; kreşte iki çocukta '
                                             'daha konjonktivit gelişti.',
                          'teaching_point': 'Küçük çocukta viskoz lidokain sistemik toksisite riski taşır; bulaşıcılık '
                                            'süresinde hijyen önlemleri önemlidir.'}]}]},
 {'id': 'Y72',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '2 Yaşında (12 kg)',
  'gender': 'Kız',
  'complaint': 'İki gündür ateş, yemek yemeyi reddetme ve salya akması',
  'history': "Annesi anlatıyor: 'Dünden beri ateşi 39°C'ye çıkıyor. Ağzını açınca ağlıyor, hiçbir şey yemiyor, su da "
             "az içiyor. Salyası çok akıyor.' Kreşe gidiyor, yaz aylarında. Kusma, ishal, öksürük yok. Son 12 saatte "
             'iki bez ıslatmış. Döküntü fark edilmemiş. Daha önce benzer şikâyeti olmamış. Aşıları tam.',
  'final_diagnosis': 'Herpanjina (Enterovirus/Coxsackie A)',
  'disposition': 'Ağızdan Sıvı Alımı Gözlendikten Sonra Analjezi ve Sıvı Önerileriyle Yeşil Alandan Taburculuk',
  'case_pearl': 'Herpanjinada ateşle birlikte yumuşak damak, uvula ve ön plikalarda 1-2 mm veziküller ve sığ ülserler '
                'görülür; dişeti ve dudaklar korunur. Herpetik gingivostomatitte ise ön ağız, dişeti ve dudak tutulur. '
                'El-ayak-ağız hastalığında el ve ayakta lezyonlar eşlik eder. Asıl risk ağrıya bağlı sıvı alamamaktır. '
                'Tedavi analjezi ve sıvıdır. Viskoz lidokain küçük çocuklarda önerilmez.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Ateşli ve yemek yemeyen bu çocukta ilk değerlendirmede öncelikli olarak ne yaparsınız?',
             'options': [{'text': 'Hidrasyon durumunu ve son idrar zamanını değerlendirip ağız içini, dişetini, '
                                  'dudakları, farenksi, el ve ayakları ve deriyi ayrıntılı olarak muayene etmek',
                          'is_correct': True,
                          'explanation': 'Ağız içi lezyonların yeri (ön ağız, dişeti, yumuşak damak) ve el-ayak '
                                         'tutulumu ayırıcı tanıyı belirler. Ağrılı ağız lezyonlarında asıl risk '
                                         'dehidratasyondur.',
                          'new_finding': 'Vital Bulgular: Ateş 38.9°C, KTA 136/dk, SS 26/dk, SpO2 %99, KDZ 2 sn. '
                                         'Mukozalar hafif kuru, göz yaşı var, fontanel kapalı. Yumuşak damak, uvula ve '
                                         'ön tonsil plikalarında 6-8 adet gri-beyaz, kırmızı haleli 1-2 mm vezikül ve '
                                         'sığ ülser. Dişeti, dil ucu ve dudaklar normal. El, ayak ve kalçada lezyon '
                                         'yok. Boyunda küçük, hassas olmayan lenf nodları.'},
                         {'text': 'Salya akması ve ağız açmayı reddetme nedeniyle havayolu tıkanıklığı düşünüp ağız '
                                  'muayenesinden kaçınarak çocuğu hemen KBB değerlendirmesine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'KBB konsültasyonu saatler sürdü; çocukta stridor ya da solunum sıkıntısı '
                                             'yoktu ve ağız içi muayene yapılmamıştı.',
                          'teaching_point': 'Solunum sıkıntısı, stridor ve tripod pozisyonu yoksa ağız içi muayene '
                                            'güvenle yapılabilir.'},
                         {'text': 'Ateş ve beslenme reddi nedeniyle muayeneyi kısa tutup tam kan sayımı, CRP ve idrar '
                                  'tetkiki istemek ve sonuçlara göre tedavi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Tetkikler normal geldi; ağız içindeki lezyonlar saatler sonra fark '
                                             'edildi.',
                          'teaching_point': 'Ateşli çocukta tetkik öncesi ağız içi dahil tam muayene, çoğu zaman '
                                            'tanıyı tek başına koydurur.'},
                         {'text': 'Diş çıkarmaya bağlı ateş ve huzursuzluk olarak değerlendirip diş jeli ve ateş '
                                  'düşürücü önermek, ağız içi muayene için ertesi gün kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Evde sıvı alımı daha da azaldı; çocuk ertesi gün belirgin '
                                             'dehidratasyonla getirildi.',
                          'teaching_point': 'Diş çıkarma 38.5°C üzeri ateş ve beslenme reddi yapmaz; ağız içi muayene '
                                            'ertelenmemelidir.'}]},
            {'stage_title': 'Tetkik ve Destek Kararı',
             'question': 'Bu çocukta hangi yaklaşım uygundur?',
             'options': [{'text': 'Ülserlerin bakteriyel olabileceğini düşünerek boğaz kültürü almak ve kültür '
                                  'sonucuna göre antibiyotik başlamayı planlamak',
                          'is_correct': False,
                          'scenario_update': 'Kültürde normal flora üredi; bu sürede analjezi ve sıvı alımı gözden '
                                             'kaçtı.',
                          'teaching_point': 'Tipik viral ağız lezyonlarında kültür gerekmez; öncelik ağrı kontrolü ve '
                                            'hidrasyondur.'},
                         {'text': 'Lezyonlardan virüs PCR ve serolojik testler göndermek, sonuç gelene dek çocuğu Sarı '
                                  'Alanda damar yolu ile izlemek',
                          'is_correct': False,
                          'scenario_update': 'Damar yolu açılırken çocuk çok ağladı; PCR sonucu yönetimi değiştirmeden '
                                             'günler sonra geldi.',
                          'teaching_point': 'Klinik tanının açık olduğu hafif olguda viral PCR ve damar yolu '
                                            'gerekmez.'},
                         {'text': 'Laboratuvar tetkiki yapmadan analjezik vermek, 30-45 dakika sonra soğuk sıvı '
                                  'içirmeyi deneyerek ağızdan alımı acil serviste gözlemlemek',
                          'is_correct': True,
                          'explanation': 'Tanı kliniktir. Analjezi sonrası ağızdan sıvı içebilmesi taburculuk için en '
                                         'önemli ölçüttür; içemezse IV veya nazogastrik sıvı düşünülür.',
                          'new_finding': 'İbuprofen 10 mg/kg verildi. 40 dakika sonra çocuk soğuk ayran ve su içmeye '
                                         'başladı, bir saatte yaklaşık 180 mL aldı, bir kez idrar yaptı.'},
                         {'text': 'Ağız içi ağrısı nedeniyle beklemeden nazogastrik sonda takarak sıvı vermek ve '
                                  'çocuğu bir gece gözleme alıp sabah değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Sonda takılması çocuğu çok rahatsız etti; analjezi sonrası ağızdan '
                                             'içebileceği hiç denenmemişti.',
                          'teaching_point': 'Önce yeterli analjezi verilip ağızdan alım denenmelidir; sonda veya damar '
                                            'yolu yalnızca başarısızlıkta gerekir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Primer herpetik gingivostomatit',
                          'is_correct': False,
                          'scenario_update': 'Dişeti, dil ucu ve dudaklar normaldi; lezyonlar posterior ağızdaydı.',
                          'teaching_point': 'Herpetik gingivostomatitte dişeti kanamalı ve ödemlidir, ön ağız ve '
                                            'dudaklar tutulur.'},
                         {'text': 'El-ayak-ağız hastalığı',
                          'is_correct': False,
                          'scenario_update': 'El, ayak ve kalçada lezyon yoktu.',
                          'teaching_point': 'El-ayak-ağız hastalığında ağız lezyonlarına el, ayak ve kalçada '
                                            'veziküller eşlik eder.'},
                         {'text': 'Herpanjina (enteroviral)',
                          'is_correct': True,
                          'explanation': 'Ateşle birlikte yumuşak damak, uvula ve ön plikalarda veziküller ve sığ '
                                         'ülserler, dişeti ve dudakların korunması herpanjinayı gösterir.',
                          'new_finding': 'Tanı: Herpanjina (enterovirüs).'},
                         {'text': 'Rekürren aftöz stomatit',
                          'is_correct': False,
                          'scenario_update': 'Lezyonlar ateşle birlikte yumuşak damakta küçük veziküllerle başlamıştı '
                                             've daha önce benzer atak yoktu.',
                          'teaching_point': 'Aftlar genellikle ateşsiz, tekrarlayan, daha büyük ve hareketli mukozada '
                                            'yerleşen ülserlerdir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun taburculuk planı hangisidir?',
             'options': [{'text': 'Ağız lezyonlarını hızla iyileştirmek için oral asiklovir 20 mg/kg günde dört kez 7 '
                                  'gün başlamak ve ateş düşürücüyle birlikte taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Asiklovir verildi ancak hastalığın seyrinde hiçbir değişiklik olmadı.',
                          'teaching_point': 'Asiklovir enterovirüslere etkisizdir; herpetik gingivostomatitin erken '
                                            'döneminde düşünülür.'},
                         {'text': 'Ağrıyı azaltmak için her öğünden önce viskoz lidokainli gargara önermek ve olası '
                                  'sekonder enfeksiyon için amoksisilin eklemek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk lidokaini yuttu, ağız ve boğaz uyuşması nedeniyle öğürdü; '
                                             'amoksisilin ishale yol açtı.',
                          'teaching_point': 'Küçük çocuklarda viskoz lidokain nöbet ve aspirasyon riski taşır; '
                                            'antibiyotik gereksizdir.'},
                         {'text': 'Lezyonlar iyileşene kadar katı gıda yasağı koyup yalnızca damar yolu ile sıvı '
                                  'alması için çocuğu servise yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Ağızdan içebilen çocuk gereksiz yere yatırıldı; hastane ortamı '
                                             'enterovirüs bulaşı açısından da risk oluşturdu.',
                          'teaching_point': 'Analjeziyle ağızdan içebilen çocuk evde izlenebilir; yatış yalnızca '
                                            'dehidratasyon veya içememe durumunda gerekir.'},
                         {'text': 'Düzenli parasetamol veya ibuprofen, soğuk ve asitsiz sıvılarla yumuşak gıda '
                                  "önermek; günde 4'ten az bez ıslatırsa veya hiç içemezse dönmelerini söylemek",
                          'is_correct': True,
                          'explanation': 'Hastalık 7-10 günde kendiliğinden geçer. Düzenli analjezi sıvı alımını '
                                         'sağlar. Azalmış idrar dehidratasyonun en pratik uyarı bulgusudur. El hijyeni '
                                         'bulaşı azaltır.',
                          'new_finding': 'Çocuk taburcu edildi. Üçüncü gün ateş düştü, yedinci gün lezyonlar iyileşti; '
                                         'dehidratasyon gelişmedi.'}]}]},
 {'id': 'Y73',
  'category': '👂 Kulak Ağrısı & KBB',
  'age': '7 Yaşında',
  'gender': 'Kız',
  'complaint': 'On iki gündür geçmeyen burun akıntısı, burun tıkanıklığı ve gündüz de süren öksürük',
  'history': "Annesi anlatıyor: 'Nezle ile başladı, iki haftaya yakın oldu, hiç düzelmedi. Burnundan sarı-yeşil koyu "
             "akıntı geliyor, ağzı açık uyuyor, gündüz de öksürüyor. Ateşi ilk iki gün 38°C idi, sonra olmadı.' Baş "
             'ağrısı hafif, göz çevresinde şişlik, görme bozukluğu ve kusma yok. Son bir ayda antibiyotik kullanmamış. '
             'Astım veya alerji öyküsü yok. Tartı: 24 kg.',
  'final_diagnosis': 'Akut Bakteriyel Rinosinüzit (Persistan Seyirli)',
  'disposition': 'Yüksek Doz Amoksisilin ve 72 Saat Sonra Yeniden Değerlendirme Önerisiyle Yeşil Alandan Taburculuk',
  'case_pearl': 'AAP 2013 kılavuzuna göre tanı kliniktir: (1) 10 günü aşan ve düzelmeyen burun akıntısı veya gündüz '
                'öksürüğü, (2) düzelme sonrası kötüleşme ya da (3) en az 3 gün süren ≥39°C ateş ve pürülan akıntı. '
                'Komplike olmayan olguda görüntüleme önerilmez. Persistan seyirde antibiyotik ya da 3 günlük ek gözlem '
                'seçenekleri sunulabilir. Göz çevresinde şişlik, görme değişikliği veya nörolojik bulgu orbital ya da '
                'intrakraniyal komplikasyonu düşündürür ve acil görüntüleme gerektirir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'On iki gündür burun akıntısı ve öksürüğü olan bu çocukta muayenede neye öncelik verirsiniz?',
             'options': [{'text': 'Uzamış öksürük nedeniyle akciğer muayenesine odaklanıp oskültasyon normalse viral '
                                  'üst solunum yolu enfeksiyonu deyip yalnızca serum fizyolojik önermek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk üçüncü haftada hâlâ koyu akıntı ve öksürükle yeniden başvurdu.',
                          'teaching_point': 'On günü aşan, düzelmeyen tabloda klinik seyir değerlendirilmeli; yalnızca '
                                            'akciğer muayenesi yeterli değildir.'},
                         {'text': 'Hastalığın seyrini sorgulayıp burun mukozası, postnazal akıntı, kulak zarları, göz '
                                  'çevresi ve göz hareketleri ile nörolojik bulguları değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Tanının temeli semptom süresi ve seyridir. Göz çevresi, göz hareketleri ve '
                                         'nörolojik muayene komplikasyonları dışlamak için mutlaka yapılmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.9°C, KTA 92/dk, SS 20/dk, SpO2 %99. Burun mukozası '
                                         'ödemli ve hiperemik, orta meada koyu sarı-yeşil akıntı. Arka farenks '
                                         'duvarında pürülan postnazal akıntı. Kulak zarları normal. Göz kapakları '
                                         'ödemsiz, göz hareketleri ağrısız ve tam, görme normal. Nörolojik muayene '
                                         'olağan. Akciğer sesleri temiz.'},
                         {'text': 'Pürülan akıntı nedeniyle burundan kültür alıp muayeneyi kültür sonucu gelene dek '
                                  'ertelemek, bu sürede yalnızca antihistaminik şurup başlamak',
                          'is_correct': False,
                          'scenario_update': 'Burun kültüründe normal flora ve S. aureus üredi; sonuç yönetime katkı '
                                             'sağlamadı.',
                          'teaching_point': 'Burun sürüntüsü kültürü sinüs içindeki etkeni yansıtmaz ve önerilmez.'},
                         {'text': 'Sarı-yeşil akıntıyı bakteriyel enfeksiyonun kesin kanıtı kabul edip ayrıntılı '
                                  'muayeneye gerek görmeden azitromisin reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Azitromisin üç gün kullanıldı; akıntı sürdü ve çocuk tekrar başvurdu.',
                          'teaching_point': 'Akıntının rengi tek başına bakteriyel enfeksiyonu göstermez; tanı semptom '
                                            'süresi ve seyriyle konur.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Komplikasyon bulgusu olmayan bu çocukta hangi tetkik yaklaşımı uygundur?',
             'options': [{'text': 'Tanıyı kesinleştirmek için Waters pozisyonunda sinüs grafisi çekmek ve sinüslerde '
                                  'opasite varsa antibiyotik tedavisi başlamak',
                          'is_correct': False,
                          'scenario_update': 'Grafide maksiller sinüslerde bilateral mukozal kalınlaşma görüldü; bu '
                                             'bulgu viral nezlede de bulunabildiği için yorum değişmedi.',
                          'teaching_point': 'Sinüs grafisi viral ve bakteriyel tabloyu ayıramaz; komplike olmayan '
                                            'olguda önerilmez.'},
                         {'text': 'Görüntüleme veya laboratuvar tetkiki istemeden klinik ölçütlerle tanı koymak ve '
                                  'tedavi seçeneklerini aileyle birlikte değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Komplike olmayan olguda tanı kliniktir. Görüntüleme yalnızca orbital veya '
                                         'intrakraniyal komplikasyon şüphesinde, kontrastlı tomografi veya MR olarak '
                                         'yapılır.',
                          'new_finding': 'Tetkik istenmedi. Semptomlar 10 günü aşmış ve düzelme göstermemiş; ateş yok, '
                                         'komplikasyon bulgusu yok.'},
                         {'text': 'Paranazal sinüs bilgisayarlı tomografisi çekip mukozal kalınlaşma derecesine göre '
                                  'antibiyotik ya da burun spreyi kararını vermek',
                          'is_correct': False,
                          'scenario_update': 'Tomografide yaygın mukozal kalınlaşma saptandı; çocuk gereksiz radyasyon '
                                             'aldı ve tedavi kararı değişmedi.',
                          'teaching_point': 'Tomografi komplikasyon şüphesi veya cerrahi planlaması dışında '
                                            'önerilmez.'},
                         {'text': 'Hemogram, CRP ve sedimantasyon istemek; CRP yüksekse antibiyotik başlamak, normalse '
                                  'viral kabul edip burun spreyi önermek',
                          'is_correct': False,
                          'scenario_update': 'CRP 9 mg/L geldi ve antibiyotik verilmedi; çocuk bir hafta sonra aynı '
                                             'yakınmalarla döndü.',
                          'teaching_point': 'Kan tetkikleri bu tanıda ayırt edici değildir; karar semptomların süresi '
                                            've seyrine göre verilir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bu çocukta en olası tanınız nedir?',
             'options': [{'text': 'Uzamış viral üst solunum yolu enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Semptomlar 10 günü aşmış ve hiç düzelme göstermemişti.',
                          'teaching_point': 'Viral nezle genellikle 5-7. günde zirve yapıp 10 gün içinde belirgin '
                                            'düzelir.'},
                         {'text': 'Akut bakteriyel rinosinüzit',
                          'is_correct': True,
                          'explanation': 'On günü aşan ve düzelmeyen pürülan burun akıntısı ve gündüz öksürüğü '
                                         'persistan akut bakteriyel rinosinüziti gösterir.',
                          'new_finding': 'Tanı: Akut bakteriyel rinosinüzit (persistan seyir).'},
                         {'text': 'Alerjik rinit alevlenmesi',
                          'is_correct': False,
                          'scenario_update': 'Hapşırma, kaşıntı ve sulu akıntı yoktu; akıntı pürülandı ve öncesinde '
                                             'nezle vardı.',
                          'teaching_point': 'Alerjik rinitte sulu akıntı, hapşırma ve burun-göz kaşıntısı baskındır.'},
                         {'text': 'Burunda yabancı cisim',
                          'is_correct': False,
                          'scenario_update': 'Akıntı bilateraldi ve kötü koku yoktu.',
                          'teaching_point': 'Yabancı cisimde tek taraflı, kötü kokulu, bazen kanlı akıntı tipiktir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Amoksisilin 80-90 mg/kg/gün iki dozda başlamak ya da aileyle 3 gün ek gözlem kararı '
                                  'vermek; 72 saatte düzelme yoksa amoksisilin-klavulanata geçmek',
                          'is_correct': True,
                          'explanation': 'Persistan seyirde antibiyotik veya kısa ek gözlem seçenekleri sunulur. '
                                         'Amoksisilin ilk seçenektir. 72 saatte yanıt alınamazsa tedavi genişletilir '
                                         'veya tanı yeniden değerlendirilir.',
                          'new_finding': 'Amoksisilin 2 x 1000 mg başlandı. 72. saatte akıntı azaldı, öksürük '
                                         'geriledi. Tedavi 10 güne tamamlandı.'},
                         {'text': 'Üç gün azitromisin vermek ve tıkanıklık için 7 yaşında olduğundan oral '
                                  'dekonjestan-antihistaminik kombinasyonu eklemek',
                          'is_correct': False,
                          'scenario_update': 'Azitromisine rağmen akıntı sürdü; dekonjestan sonrası çocukta uykusuzluk '
                                             've çarpıntı oldu.',
                          'teaching_point': 'Makrolidlere pnömokok direnci yüksektir; dekonjestan ve '
                                            'antihistaminiklerin bu tabloda yararı yoktur.'},
                         {'text': 'Antibiyotik vermeden yalnızca 14 gün topikal dekonjestan sprey kullanımını önermek '
                                  've bir ay sonra KBB kontrolüne yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Uzun süreli dekonjestan sprey rebound tıkanıklık yaptı; akıntı sürdü.',
                          'teaching_point': 'Topikal dekonjestanlar 3-5 günden uzun kullanılmamalıdır; uzun süreli '
                                            'kullanım rebound etki yapar.'},
                         {'text': 'Seftriakson 50 mg/kg intramüsküler üç gün uygulamak ve tedaviden sonra kontrol için '
                                  'paranazal sinüs tomografisi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Çocuk üç gün iğne için hastaneye getirildi; kontrol tomografisi gereksiz '
                                             'radyasyona neden oldu.',
                          'teaching_point': 'Ağızdan tedavi alabilen çocukta parenteral antibiyotik ve kontrol '
                                            'görüntüleme gerekmez.'}]}]},
 {'id': 'Y74',
  'category': '👂 Kulak Ağrısı & KBB',
  'age': '9 Yaşında',
  'gender': 'Erkek',
  'complaint': 'İki gündür sağ kulakta giderek artan ağrı, dolgunluk hissi ve az miktarda akıntı',
  'history': "Kendisi anlatıyor: 'Kulağım çok ağrıyor, kulak mememe dokununca daha çok acıyor. Çiğnerken de ağrıyor.' "
             'Annesi bir haftadır her gün yüzme kursuna gittiğini, kulağını kulak çubuğuyla temizlediğini anlatıyor. '
             'Ateş, burun akıntısı, öksürük yok. Daha önce kulak ameliyatı veya kulak zarı delinmesi olmamış. Diyabet '
             'veya bağışıklık sorunu yok.',
  'final_diagnosis': 'Akut Otitis Eksterna (Yüzücü Kulağı)',
  'disposition': 'Topikal Antibiyotikli Damla, Analjezi ve Kulağı Kuru Tutma Önerisiyle Yeşil Alandan Taburculuk',
  'case_pearl': 'Tragusa bası ve kulak kepçesinin çekilmesiyle artan ağrı, dış kulak yolunda ödem, eritem ve debris '
                "akut otitis eksternayı düşündürür. Başlıca etkenler P. aeruginosa ve S. aureus'tur. Tedavi topikal "
                'antibiyotik (kinolon ± steroid) damladır. Kulak zarı görülemiyorsa ototoksik olmayan damla seçilir. '
                'Kanal ödemliyse fitil konur. Oral antibiyotik yalnızca kanal dışına yayılım veya bağışıklık '
                'yetmezliğinde gerekir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Kulak ağrısı ve akıntısı olan bu çocukta muayenede neye dikkat edersiniz?',
             'options': [{'text': 'Akıntıyı orta kulak iltihabına bağlı delinme kabul edip otoskopi yapmadan oral '
                                  'amoksisilin başlamak ve iki gün sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Amoksisiline rağmen ağrı arttı, kulak yolu tamamen kapandı.',
                          'teaching_point': 'Kulak akıntısında otoskopi yapılmadan neden ve tedavi belirlenemez.'},
                         {'text': 'Tragus ve kulak kepçesine basıyla ağrıyı, kulak arkasını ve yüz sinirini '
                                  'değerlendirmek; otoskopiyle kulak yolu ve kulak zarını incelemek',
                          'is_correct': True,
                          'explanation': 'Tragus ve kepçe hareketiyle artan ağrı dış kulak yoluna işaret eder. Kulak '
                                         'arkası ve yüz siniri muayenesi yayılım ve komplikasyonları dışlar. Kulak '
                                         'zarının durumu damla seçimini belirler.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 88/dk. Sağ tragusa bası ve kulak kepçesinin '
                                         'çekilmesi belirgin ağrılı. Dış kulak yolu ödemli ve eritemli, lümen yaklaşık '
                                         '%50 daralmış, beyaz-sarı nemli debris var. Debris nazikçe temizlendikten '
                                         'sonra kulak zarı sağlam ve normal görünümde. Kulak arkası normal, kepçede '
                                         'selülit yok, yüz siniri fonksiyonları normal. Periauriküler küçük hassas '
                                         'lenf nodu.'},
                         {'text': 'Akıntının kaynağını görmek için muayene öncesi kulağı şırıngayla ılık suyla yıkayıp '
                                  'temizlemek, ardından kulak zarını değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Yıkama sırasında çocuk şiddetli ağrı duydu ve muayeneye uyum '
                                             'sağlayamadı; kanal ödemi arttı.',
                          'teaching_point': 'Ödemli ve iltihaplı kulak yolunda su ile yıkama ağrıyı ve enfeksiyonu '
                                            'artırır; temizlik nazikçe aspirasyon veya kuru yöntemle yapılır.'},
                         {'text': 'Yüzme öyküsü nedeniyle mantar enfeksiyonu düşünüp muayeneyi kısa tutarak topikal '
                                  'antifungal krem önermek ve yüzmeye devam edebileceğini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Antifungal kremden yarar görülmedi ve yüzmeye devam eden çocuğun ağrısı '
                                             'arttı.',
                          'teaching_point': 'Akut tabloda en sık etken bakteriyeldir; mantar enfeksiyonunda kaşıntı ve '
                                            'tipik hif-spor görünümü baskındır.'}]},
            {'stage_title': 'Tetkik ve İlk Müdahale Kararı',
             'question': 'Kulak zarı sağlam, kanal %50 daralmış bu çocukta bir sonraki adım nedir?',
             'options': [{'text': 'Kulak akıntısından kültür almak ve antibiyogram sonucuna göre tedavi seçmek; sonuç '
                                  'gelene kadar tedaviye başlamamak',
                          'is_correct': False,
                          'scenario_update': 'Kültür 72 saat sürdü; bu sürede çocuk ağrıdan uyuyamadı.',
                          'teaching_point': 'İlk atakta kültür gerekmez; tedaviye yanıtsız veya tekrarlayan olgularda '
                                            'istenir.'},
                         {'text': 'Tamponad ve kulak arkası yayılım şüphesiyle temporal kemik bilgisayarlı tomografisi '
                                  'istemek ve sonucu gelince tedaviye karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi yalnızca yumuşak doku ödemi gösterdi; gereksiz radyasyon ve '
                                             'bekleme süresi oluştu.',
                          'teaching_point': 'Görüntüleme, kafa tabanına yayılım veya mastoid tutulumu şüphesi olan '
                                            'ağır olgularla sınırlıdır.'},
                         {'text': 'Debrisi nazikçe temizleyip kanal ödemi damlanın geçişini engelleyecek düzeyde '
                                  'değilse fitil koymadan, tetkik istemeden topikal tedaviye geçmek',
                          'is_correct': True,
                          'explanation': 'Kanalın temizlenmesi damlanın dokuya ulaşmasını sağlar. Belirgin ödemde '
                                         'fitil konur. Komplike olmayan ilk atakta kültür ve görüntüleme gerekmez.',
                          'new_finding': 'Kanal temizlendi, damla geçişi için yeterli açıklık sağlandı. Kulak zarı '
                                         'sağlam olarak kayda geçti. Tetkik istenmedi.'},
                         {'text': 'Hemogram ve CRP istemek; değerler yüksekse oral antibiyotik ve damlayı birlikte '
                                  'başlamak, normalse yalnızca analjezik önermek',
                          'is_correct': False,
                          'scenario_update': 'Hemogram ve CRP normal geldi, damla başlanmadı; çocuğun ağrısı arttı.',
                          'teaching_point': 'Lokal dış kulak yolu enfeksiyonunda kan tetkiki tanıya katkı sağlamaz.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bu çocukta en olası tanınız nedir?',
             'options': [{'text': 'Perforasyonlu akut otitis media',
                          'is_correct': False,
                          'scenario_update': 'Kulak zarı sağlamdı ve ateş yoktu.',
                          'teaching_point': 'Perforasyonlu otitis mediada kulak zarında delik görülür ve akıntı orta '
                                            'kulaktan gelir.'},
                         {'text': 'Akut otitis eksterna',
                          'is_correct': True,
                          'explanation': 'Yüzme ve kulak çubuğu öyküsü, tragusa bası ile artan ağrı, kanalda ödem, '
                                         'eritem ve debris ile sağlam kulak zarı akut otitis eksternayı gösterir.',
                          'new_finding': 'Tanı: Akut otitis eksterna.'},
                         {'text': 'Dış kulak yolu fronkülü',
                          'is_correct': False,
                          'scenario_update': 'Kanalın tamamında yaygın ödem vardı; lokalize bir pustül veya '
                                             'fluktuasyon yoktu.',
                          'teaching_point': 'Fronkülde kanalın dış kısmında sınırlı, kabarık, püylü bir lezyon '
                                            'görülür.'},
                         {'text': 'Akut mastoidit',
                          'is_correct': False,
                          'scenario_update': 'Kulak arkası normaldi, kulak kepçesi öne itilmemişti ve kulak zarı '
                                             'sağlamdı.',
                          'teaching_point': 'Mastoiditte kulak arkasında şişlik, kızarıklık ve kepçenin öne itilmesi '
                                            'görülür.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Oral amoksisilin-klavulanat 10 gün başlamak, kulağa damla vermemek ve yüzmeye ağrı '
                                  'geçtiğinde hemen devam edebileceğini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Oral antibiyotik kulak yolu dokusuna yeterli düzeyde ulaşmadı; yüzmeye '
                                             'dönen çocukta tablo tekrarladı.',
                          'teaching_point': 'Komplike olmayan olguda oral antibiyotik gereksizdir; topikal tedavi çok '
                                            'daha etkilidir.'},
                         {'text': 'Kulak yolunu evde günde iki kez kulak çubuğu ve oksijenli suyla temizlemelerini, '
                                  'ardından antibiyotiksiz yağlı damla kullanmalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Kulak çubuğu kanal derisini daha da tahriş etti; ağrı ve akıntı arttı.',
                          'teaching_point': 'Kulak çubuğu kullanımı otitis eksterna için risk faktörüdür ve '
                                            'kaçınılmalıdır.'},
                         {'text': 'Kinolon-steroid damlayı 7 gün günde iki kez ve ibuprofen önermek; 7-10 gün yüzmeye '
                                  'ara verip kulağı kuru tutmasını söylemek',
                          'is_correct': True,
                          'explanation': "Topikal kinolon P. aeruginosa ve S. aureus'u kapsar ve ototoksik değildir; "
                                         'steroid ödem ve ağrıyı azaltır. 48-72 saatte düzelme yoksa yeniden '
                                         'değerlendirilmelidir.',
                          'new_finding': 'Siprofloksasin-hidrokortizon damla ve ibuprofen ile taburcu edildi. 72. '
                                         'saatte ağrı belirgin azaldı, yedinci gün kanal normale döndü.'},
                         {'text': 'Aminoglikozid içeren damlayı 14 gün günde dört kez önermek ve ağrıyı kesmek için '
                                  'kulak yoluna topikal anestezikli damla eklemek',
                          'is_correct': False,
                          'scenario_update': 'Uzun süreli aminoglikozid damla kanal derisinde kontakt dermatit yaptı; '
                                             'ağrı ve kaşıntı arttı.',
                          'teaching_point': 'Tedavi süresi genellikle 7 gündür. Uzun süreli kullanım ve neomisin '
                                            'kontakt duyarlılık ile ilişkilidir.'}]}]},
 {'id': 'Y75',
  'category': '🫁 Hırıltı & Solunum Sıkıntısı',
  'age': '7 Yaşında (22 kg)',
  'gender': 'Erkek',
  'complaint': 'İki gündür artan öksürük, hırıltılı solunum ve geceleri öksürükle uyanma',
  'history': "Annesi anlatıyor: 'Üç yıldır astım tanısı var, koruyucu inhaler sprey verilmişti ama iyi olunca "
             'bıraktık. Üç gün önce nezle oldu, sonra öksürük ve hırıltı başladı. Evde mavi spreyi günde 3-4 kez '
             "kullandık, biraz rahatlıyor ama birkaç saat sonra tekrar başlıyor.' Konuşurken nefesi kesilmiyor, "
             'oynuyor. Daha önce yoğun bakım yatışı yok. Son bir yılda bir kez acil başvurusu olmuş. Evde sigara '
             'içiliyor.',
  'final_diagnosis': 'Viral Enfeksiyonla Tetiklenen Hafif-Orta Astım Atağı',
  'disposition': 'Oral Kortikosteroid, Kontrol Edici İnhaler Tedavi ve Yazılı Eylem Planıyla Yeşil Alandan Taburculuk',
  'case_pearl': "GINA'ya göre hafif-orta atakta çocuk cümle kurabilir, ajite değildir, SpO2 ≥%92'dir. Tedavi ilk "
                'saatte 20 dakikada bir 4-10 puf salbutamolün aralayıcıyla verilmesi ve oral prednizolon 1-2 mg/kg (en '
                'fazla 40 mg) 3-5 gündür. Rutin akciğer grafisi, kan gazı ve antibiyotik gerekmez. Taburculukta '
                'kontrol edici tedavinin (inhaler kortikosteroid) başlanması veya basamağının artırılması, inhaler '
                'tekniği, yazılı eylem planı ve 1 hafta içinde kontrol şarttır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Şiddet Belirleme',
             'question': 'Hırıltılı solunumla gelen bu çocukta ilk değerlendirmede hangi yaklaşım doğrudur?',
             'options': [{'text': 'Konuşma, solunum sayısı, yardımcı solunum kası kullanımı, bilinç, SpO2 ve '
                                  'oskültasyonla atak şiddetini belirleyip mümkünse PEF ölçmek',
                          'is_correct': True,
                          'explanation': 'Tedavi şiddete göre belirlenir: cümle kurabilme, ajitasyon, solunum sayısı, '
                                         'yardımcı kas kullanımı, SpO2 ve PEF temel ölçütlerdir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.4°C, KTA 116/dk, SS 30/dk, SpO2 %94 (oda havası), TA '
                                         '104/64 mmHg. Cümleler halinde konuşuyor, ajitasyon yok. Hafif interkostal '
                                         'çekilme. Bilateral ekspiratuvar yaygın hışıltı, ekspiryum uzamış, hava '
                                         "girişi iyi. PEF beklenen değerin %62'si."},
                         {'text': 'Hırıltının nedenini netleştirmek için önce akciğer grafisi ve kan gazı istemek, '
                                  'sonuçlar gelince bronkodilatör tedaviye karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Grafide hafif havalanma artışı dışında bulgu yoktu; bekleme süresinde '
                                             "çocuğun solunum sayısı 36/dk'ya çıktı.",
                          'teaching_point': 'Bilinen astımlı çocukta atak tedavisi tetkik beklenmeden başlar; rutin '
                                            'grafi ve kan gazı gerekmez.'},
                         {'text': 'Ateşi 37.4°C olduğu ve nezle ile başladığı için pnömoni düşünüp muayeneden hemen '
                                  'sonra oral amoksisilin başlamak',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik başlandı; hırıltı ve öksürük bronkodilatör verilmediği için '
                                             'düzelmedi.',
                          'teaching_point': 'Viral enfeksiyonun tetiklediği astım atağında antibiyotik endikasyonu '
                                            'yoktur; bronkodilatör ve steroid gerekir.'},
                         {'text': 'Çocuğun rahat konuştuğunu görüp atağın hafif olduğunu varsaymak, SpO2 ölçümü ve '
                                  'oskültasyon yapmadan evdeki mavi spreyi sık aralıklarla sürdürmesini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk eve gönderildi; gece SpO2 düşüşü ve belirgin çekilmelerle yeniden '
                                             'getirildi.',
                          'teaching_point': 'Atak şiddeti nesnel ölçütlerle (SpO2, solunum sayısı, PEF) belirlenmeden '
                                            'taburculuk kararı verilmez.'}]},
            {'stage_title': 'İlk Tedavi ve Tetkik Kararı',
             'question': 'Bu çocuğa acil serviste hangi tedavi verilmelidir?',
             'options': [{'text': 'Salbutamol nebülünü ipratropium ile birlikte vermek, damar yolu açarak intravenöz '
                                  'metilprednizolon uygulamak ve magnezyum sülfat eklemek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk yoğun tedaviye kısa sürede yanıt verdi; ancak damar yolu ve IV '
                                             'ilaçlar bu atak şiddetinde gereksizdi.',
                          'teaching_point': 'Magnezyum ve IV steroid ağır ataklar içindir; ağızdan alabilen çocukta '
                                            'oral steroid aynı etkinliktedir.'},
                         {'text': 'Aralayıcıyla 20 dakikada bir 6 puf salbutamol (toplam 3 doz) vermek, ilk saatte '
                                  "oral prednizolon 1-2 mg/kg uygulamak ve SpO2'yi izlemek",
                          'is_correct': True,
                          'explanation': 'Aralayıcıyla ölçülü doz inhaler en az nebülizer kadar etkilidir. Erken oral '
                                         'kortikosteroid yatış riskini azaltır. Tedaviye yanıt 1 saat sonra yeniden '
                                         'değerlendirilir.',
                          'new_finding': 'Üç doz salbutamol ve prednizolon 40 mg sonrası 1. saatte: KTA 124/dk, SS '
                                         '22/dk, SpO2 %97 (oda havası), çekilme yok, hışıltı azalmış, PEF %84. Dört '
                                         'saat izlemde semptomlar yeniden artmadı.'},
                         {'text': 'Salbutamolü yalnızca tek doz nebülle vermek, yanıt varsa steroid vermeden çocuğu '
                                  'hemen evdeki inhaleriyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Kısa süre rahatlayan çocuk birkaç saat sonra yeniden hırıltıyla '
                                             'başvurdu.',
                          'teaching_point': 'Tek doz yanıt atağın kontrolü için yeterli değildir; oral steroid tekrar '
                                            'başvuruyu azaltır.'},
                         {'text': 'Montelukast 5 mg ve oral antihistaminik verip bir saat gözlemlemek, iyileşme yoksa '
                                  'salbutamol eklemeyi düşünmek',
                          'is_correct': False,
                          'scenario_update': "Bir saatte hırıltı ve solunum sayısı arttı, SpO2 %92'ye düştü.",
                          'teaching_point': 'Akut atakta ilk tedavi kısa etkili beta-agonist ve sistemik steroiddir; '
                                            'montelukast ve antihistaminik akut tedavide yer almaz.'}]},
            {'stage_title': 'Klinik Tanı ve Atak Şiddeti',
             'question': 'Başlangıç bulgularına göre bu atağı nasıl sınıflandırırsınız?',
             'options': [{'text': 'Ağır astım atağı',
                          'is_correct': False,
                          'scenario_update': "Çocuk cümle kurabiliyordu, ajite değildi ve SpO2 %94'tü.",
                          'teaching_point': 'Ağır atakta kelimelerle konuşma, ajitasyon, belirgin çekilme ve SpO2 <%92 '
                                            'olur.'},
                         {'text': 'Hayatı tehdit eden astım atağı',
                          'is_correct': False,
                          'scenario_update': 'Bilinç açıktı, sessiz akciğer veya siyanoz yoktu.',
                          'teaching_point': 'Sessiz akciğer, siyanoz, bilinç bozukluğu ve bitkinlik hayatı tehdit eden '
                                            'atağı gösterir.'},
                         {'text': 'Viral tetikli hafif-orta astım atağı',
                          'is_correct': True,
                          'explanation': 'Cümle kurabilme, ajitasyon olmaması, SpO2 %94 ve PEF %62 hafif-orta atakla '
                                         'uyumludur. Tetikleyici viral enfeksiyon ve kontrol edici tedavinin '
                                         'bırakılmasıdır.',
                          'new_finding': 'Tanı: Viral tetikli hafif-orta astım atağı.'},
                         {'text': 'Yabancı cisim aspirasyonu',
                          'is_correct': False,
                          'scenario_update': 'Hışıltı bilateral ve simetrikti, bronkodilatöre hızlı yanıt verdi ve '
                                             'öyküde boğulma epizodu yoktu.',
                          'teaching_point': 'Aspirasyonda ani başlangıç, tek taraflı hışıltı ve bronkodilatöre '
                                            'yanıtsızlık beklenir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun taburculuk planı hangisidir?',
             'options': [{'text': 'Evde kullanılmak üzere nebülizatör cihazı reçete etmek, salbutamol nebülünü günde '
                                  'dört kez sürdürmek ve kontrol edici tedaviyi atak bitince değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk nebülle evde sık salbutamol aldı ancak kontrol edici tedavi '
                                             'başlanmadığı için iki ay içinde yeniden atak geçirdi.',
                          'teaching_point': 'Aralayıcıyla inhaler nebülizatör kadar etkilidir; atak sonrası kontrol '
                                            'edici tedavinin başlanması veya artırılması ertelenmemelidir.'},
                         {'text': 'Prednizolonu 3 güne tamamlatmak, düşük doz inhaler kortikosteroidi yeniden '
                                  'başlatmak, aralayıcı tekniği ve yazılı eylem planı vermek',
                          'is_correct': True,
                          'explanation': 'Atak sonrası kontrol edici tedavinin başlanması yeni ataklarını önler. '
                                         'İnhaler tekniği, uyum, tetikleyiciler (evde sigara) ve yazılı plan '
                                         'taburculuğun temel parçalarıdır.',
                          'new_finding': 'Çocuk prednizolon, düşük doz budesonid ve gerektiğinde salbutamol ile '
                                         'taburcu edildi. Aileye sigara dumanından korunma anlatıldı. Bir hafta '
                                         'sonraki kontrolde semptomsuzdu, PEF %95.'},
                         {'text': 'Kontrol edici olarak yalnızca uzun etkili beta-agonist içeren inhaler başlamak ve '
                                  'kortikosteroid kullanımının büyümeyi etkileyeceği için önermemek',
                          'is_correct': False,
                          'scenario_update': 'Steroidsiz uzun etkili beta-agonist kullanımı sonrası çocuk üç hafta '
                                             'içinde daha ağır bir atakla geldi.',
                          'teaching_point': 'Uzun etkili beta-agonist tek başına kullanılmaz; düşük doz inhaler '
                                            'kortikosteroidin büyüme üzerine etkisi klinik açıdan önemsizdir.'},
                         {'text': 'Oral steroid yerine 10 gün antibiyotik ve öksürük şurubu reçete etmek, astım '
                                  'kontrolünü değerlendirmek için 3 ay sonra randevu vermek',
                          'is_correct': False,
                          'scenario_update': 'Öksürük sürdü; çocuk iki hafta sonra aynı yakınmalarla geri geldi.',
                          'teaching_point': 'Antibiyotik ve öksürük şurubu astım atağında yarar sağlamaz; atak sonrası '
                                            'erken kontrol gereklidir.'}]}]},
 {'id': 'Y76',
  'category': '🫁 Hırıltı & Solunum Sıkıntısı',
  'age': '2.5 Yaşında (13 kg)',
  'gender': 'Kız',
  'complaint': 'Nezleden iki gün sonra başlayan öksürük ve hırıltılı solunum',
  'history': "Annesi anlatıyor: 'Bu yıl üçüncü kez oluyor. Her seferinde nezle ile başlıyor, iki gün sonra hırıltı "
             'geliyor, bir hafta sürüyor. Aralarda hiç öksürmüyor, koşup oynarken veya gülerken nefesi daralmıyor, '
             "geceleri rahat uyuyor.' Egzaması ve besin alerjisi yok. Anne ve babada astım yok. Önceki ataklarda "
             "'bronşit' denilerek şurup ve antibiyotik verilmiş. Boğulma veya yabancı cisim öyküsü yok. Ateşi 37.8°C.",
  'final_diagnosis': 'Okul Öncesi Epizodik Viral Hışıltı',
  'disposition': 'Aralayıcı ve Maskeyle Gerektiğinde Salbutamol, Yazılı Plan ve Çocuk Göğüs Hastalıkları/Aile Hekimi '
                 'Takibiyle Taburculuk',
  'case_pearl': "Okul öncesi dönemde yalnızca viral enfeksiyonlarla gelen, ara dönemde semptomsuz hışıltı 'epizodik "
                "viral hışıltı' olarak adlandırılır. Atak tedavisinde aralayıcı ve maskeyle salbutamol kullanılır. "
                'Hafif-orta ataklarda rutin oral steroidin yararı gösterilmemiştir; ağır atak veya yatış gerektiren '
                'durumlarda düşünülür. Sık (yılda ≥3) veya ağır ataklarda 3 aylık düşük doz inhaler kortikosteroid '
                'deneme tedavisi önerilir. Antibiyotik ve öksürük şurubunun yeri yoktur.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Nezle sonrası hırıltıyla gelen bu çocukta ilk değerlendirmenizde hangi yaklaşım doğrudur?',
             'options': [{'text': "Solunum sayısını, çekilmeleri, SpO2'yi, konuşma ve beslenme durumunu, bilinç "
                                  'düzeyini değerlendirip iki taraflı oskültasyonla hışıltının dağılımını belirlemek',
                          'is_correct': True,
                          'explanation': 'Atak şiddeti solunum işi, SpO2, beslenme ve bilinçle belirlenir. Hışıltının '
                                         'iki taraflı ve simetrik olması yabancı cisim gibi lokal nedenlerden '
                                         'uzaklaştırır.',
                          'new_finding': 'Vital Bulgular: Ateş 37.8°C, KTA 132/dk, SS 38/dk, SpO2 %95 (oda havası). '
                                         'Huzursuz değil, annesiyle konuşuyor, su içiyor. Hafif subkostal çekilme. İki '
                                         'taraflı simetrik ekspiratuvar hışıltı, hava girişi iyi, ral yok. Berrak '
                                         'burun akıntısı. Egzema bulgusu yok.'},
                         {'text': 'Ateş ve öksürük nedeniyle pnömoni ayırımı için hemen akciğer grafisi, tam kan '
                                  'sayımı ve CRP istemek, sonuçlara göre tedaviye karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Grafide peribronşiyal kalınlaşma dışında bulgu yoktu; bekleme sırasında '
                                             'hırıltı ve çekilmeler arttı.',
                          'teaching_point': 'Tipik viral tetikli hışıltıda rutin grafi ve kan tetkiki gerekmez; önce '
                                            'şiddet değerlendirilip tedavi başlatılır.'},
                         {'text': 'Önceki ataklar gibi bronşit kabul edip muayeneyi kısa tutarak antibiyotik ve '
                                  'öksürük kesici şurup reçete etmek ve eve göndermek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk evde hırıltıyla geceyi geçirdi ve ertesi gün daha belirgin '
                                             'çekilmeyle getirildi.',
                          'teaching_point': 'Hışıltıda öncelik bronkodilatördür; antibiyotik ve öksürük şurubu '
                                            'yararsız ve iki yaş altında risklidir.'},
                         {'text': 'Tekrarlayan hışıltı nedeniyle yabancı cisim aspirasyonunu dışlamak için muayeneden '
                                  'önce acil bronkoskopi konsültasyonu istemek',
                          'is_correct': False,
                          'scenario_update': 'Konsültasyon saatlerce sürdü; hışıltının iki taraflı ve viral '
                                             'enfeksiyonlarla tekrarlayan bir örüntüsü olduğu anlaşıldı.',
                          'teaching_point': 'Yabancı cisim ani başlangıçlı, genellikle tek taraflı ve boğulma '
                                            'öyküsüyle gelir; önce muayene ve öykü değerlendirilir.'}]},
            {'stage_title': 'İlk Tedavi Kararı',
             'question': 'Hafif-orta solunum sıkıntısı olan bu çocuğa hangi tedaviyi uygularsınız?',
             'options': [{'text': 'Salbutamol ve ipratropiumu nebülle vermek, ardından damar yolu açarak intravenöz '
                                  'metilprednizolon uygulayıp servise yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Çocuk damar yolu açılırken çok ağladı, oksijen ihtiyacı yoktu ve '
                                             'tedaviye ilk dozda yanıt verdi.',
                          'teaching_point': 'Hafif-orta atakta IV steroid ve yatış gerekmez; aralayıcıyla salbutamol '
                                            'yeterlidir.'},
                         {'text': 'Nebül budesonid ve serum fizyolojikle buhar tedavisi vermek, bir saat içinde yanıt '
                                  'olmazsa ancak o zaman salbutamol eklemeyi değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Budesonid nebül sonrası bir saatte hışıltı ve solunum sayısı değişmedi.',
                          'teaching_point': 'İnhaler kortikosteroidin akut bronkodilatör etkisi yoktur; ilk tedavi '
                                            'kısa etkili beta-agonisttir.'},
                         {'text': 'Aralayıcı ve maskeyle 20 dakikada bir 2-6 puf salbutamol vermek, bir saat sonra '
                                  "yanıtı ve SpO2'yi yeniden değerlendirmek",
                          'is_correct': True,
                          'explanation': 'Aralayıcı ve maskeyle verilen ölçülü doz inhaler küçük çocukta nebül kadar '
                                         'etkilidir ve yan etkisi daha azdır. Yanıt bir saat sonunda değerlendirilir.',
                          'new_finding': 'Üç doz 4 puf salbutamol sonrası: SS 28/dk, SpO2 %97, çekilme yok, hışıltı '
                                         'belirgin azalmış. İki saatlik izlemde bulgular stabil kaldı, çocuk oynamaya '
                                         'başladı.'},
                         {'text': 'Montelukast 4 mg granül ve oral antihistaminik vermek, iki saat gözlemledikten '
                                  'sonra yanıt yoksa bronkodilatör başlamak',
                          'is_correct': False,
                          'scenario_update': "İki saatte hışıltı arttı ve SpO2 %93'e düştü.",
                          'teaching_point': 'Montelukast ve antihistaminik akut hışıltı tedavisinde etkili '
                                            'değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Öykü ve tedaviye yanıta göre en olası tanınız nedir?',
             'options': [{'text': 'Çok tetikleyicili hışıltı (erken astım)',
                          'is_correct': False,
                          'scenario_update': 'Ara dönemde koşma, gülme veya gece semptomu yoktu, atopi yoktu.',
                          'teaching_point': 'Viral enfeksiyon dışında da egzersiz, gülme ve alerjenle hışıltı olması '
                                            'çok tetikleyicili hışıltıyı gösterir.'},
                         {'text': 'Akut viral bronşiolit',
                          'is_correct': False,
                          'scenario_update': 'Çocuk 2.5 yaşındaydı ve bu yıl üçüncü hışıltı epizoduydu.',
                          'teaching_point': 'Bronşiolit genellikle iki yaş altında ilk hışıltı epizodudur.'},
                         {'text': 'Okul öncesi epizodik viral hışıltı',
                          'is_correct': True,
                          'explanation': 'Yalnız viral enfeksiyonlarla tekrarlayan, ara dönemde semptomsuz ve '
                                         'bronkodilatöre yanıt veren hışıltı epizodik viral hışıltıyı gösterir.',
                          'new_finding': 'Tanı: Okul öncesi epizodik viral hışıltı.'},
                         {'text': 'Tekrarlayan yabancı cisim aspirasyonu',
                          'is_correct': False,
                          'scenario_update': 'Hışıltı simetrikti, viral enfeksiyonlarla geliyordu ve bronkodilatöre '
                                             'hızla yanıt verdi.',
                          'teaching_point': 'Aspirasyonda tek taraflı bulgu ve tedaviye direnç beklenir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun taburculuk planı hangisidir?',
             'options': [{'text': 'Gerektiğinde aralayıcıyla salbutamol ve yazılı plan vermek; yılda üç atak '
                                  'olduğundan 3 aylık düşük doz inhaler kortikosteroid denemesi başlayıp takip '
                                  'planlamak',
                          'is_correct': True,
                          'explanation': 'Sık ataklarda düşük doz inhaler kortikosteroid deneme tedavisi atak '
                                         'sıklığını azaltabilir ve 3 ay sonra yanıt değerlendirilir. Aileye aralayıcı '
                                         'tekniği ve uyarı bulguları öğretilir.',
                          'new_finding': 'Aileye aralayıcı-maske tekniği gösterildi ve düşük doz budesonid başlandı. '
                                         'Üç ay boyunca bir hafif atak oldu, acil başvurusu gerekmedi.'},
                         {'text': 'Her nezle başlangıcında evde 5 gün oral prednizolon başlamalarını önermek ve '
                                  'salbutamolü yalnızca hırıltı belirginleşirse kullanmalarını söylemek',
                          'is_correct': False,
                          'scenario_update': 'Bir yılda çocuk yedi kür oral steroid aldı; atak sayısı azalmadı, kilo '
                                             'artışı ve uyku sorunları gelişti.',
                          'teaching_point': 'Okul öncesi viral hışıltıda ebeveyn tarafından başlatılan oral steroid '
                                            'atak şiddetini azaltmaz ve tekrarlayan kürler yan etki yapar.'},
                         {'text': 'Ataklar enfeksiyonla tetiklendiği için her atakta 7 gün amoksisilin-klavulanat ve '
                                  'öksürük şurubu kullanmalarını önermek, aralayıcı reçete etmemek',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotiklere rağmen ataklar aynı sıklıkta sürdü ve çocukta ishal '
                                             'gelişti.',
                          'teaching_point': 'Viral tetikli hışıltıda antibiyotik ve öksürük şurubu yararsızdır; '
                                            'bronkodilatör için aralayıcı gereklidir.'},
                         {'text': 'Uzun süreli kontrol için tek başına montelukast başlamak ve sağlık kuruluşuna gerek '
                                  'kalmaması için evde nebülizatör cihazı almalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Montelukast sonrası çocukta kâbus ve uyku bozukluğu gelişti; ataklar '
                                             'azalmadı.',
                          'teaching_point': 'Montelukastın bu grupta etkisi sınırlıdır ve nöropsikiyatrik yan etki '
                                            'uyarısı vardır; aralayıcı nebülizatöre tercih edilir.'}]}]},
 {'id': 'Y77',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '20 Aylık (11 kg)',
  'gender': 'Erkek',
  'complaint': "Dün akşamdan beri 39.5°C'ye çıkan ateş",
  'history': "Annesi çok endişeli: 'Dün akşam başladı, 39.5°C ölçtüm. Parasetamol ve ibuprofeni ikişer saatte bir "
             'dönüşümlü veriyorum, ateş düşünce oynuyor ama yükselince halsizleşiyor. Gece de uyandırıp ilaç verdim. '
             "Ateşten havale geçirmesinden korkuyorum.' Öksürük, burun akıntısı, kusma, ishal, döküntü yok. Su içiyor, "
             'bezleri ıslak. Aşıları (pnömokok ve Hib dahil) tam. Sünnet olmuş. Daha önce idrar yolu enfeksiyonu yok. '
             'Ablası iki gün önce ateşli bir hastalık geçirmiş.',
  'final_diagnosis': 'Odak Saptanmayan Ateş (Olası Viral Enfeksiyon), Düşük Risk',
  'disposition': 'Ateş Yönetimi Eğitimi ve 48 Saat İçinde Yeniden Değerlendirme Önerisiyle Yeşil Alandan Taburculuk',
  'case_pearl': 'Aşıları tam, iyi görünen 3-36 aylık çocukta odak saptanmayan ateşin çoğu viraldir; konjuge aşılar '
                "sonrası gizli bakteriyemi oranı %1'in altına inmiştir. Bu yaşta en sık gizli bakteriyel enfeksiyon "
                'idrar yolu enfeksiyonudur. Kız çocuklarda ve sünnetsiz erkeklerde idrar tetkiki düşük eşikle yapılır; '
                'sünnetli erkekte risk düşüktür ve ateş 48 saati aşarsa yeniden değerlendirilir. Ateş düşürücünün '
                'amacı rahatlatmaktır; dönüşümlü kullanım, uyandırarak ilaç verme ve soğuk-alkollü uygulama önerilmez. '
                'Ateş düşürücüler febril nöbeti önlemez.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Bir gündür ateşi olan bu çocuğun ilk değerlendirmesinde hangi yaklaşım doğrudur?',
             'options': [{'text': 'Ateş düşürücü verip bir saat sonra ateşin düşüp düşmediğine bakmak, ateş düşerse '
                                  'ciddi bir enfeksiyon olmadığını kabul ederek taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Ateş düştü ve çocuk taburcu edildi; ancak hiçbir değerlendirme '
                                             'yapılmadığı için aile ne zaman dönmesi gerektiğini bilmiyordu.',
                          'teaching_point': 'Ateşin antipiretiğe yanıtı bakteriyel ve viral enfeksiyonu ayırt etmez; '
                                            'karar genel görünüm ve muayeneye dayanır.'},
                         {'text': 'Muayeneyi kısa tutup beklemeden tam kan sayımı, CRP, kan kültürü, akciğer grafisi '
                                  've idrar sondası ile tam bir ateş taraması başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Çocuk çok sayıda girişim geçirdi; tüm sonuçlar normal geldi ve yönetim '
                                             'değişmedi.',
                          'teaching_point': 'İyi görünen, aşıları tam çocukta rutin tam tarama gereksizdir; tetkikler '
                                            'risk değerlendirmesine göre seçilir.'},
                         {'text': 'Genel görünüm, uyarılara yanıt, cilt rengi, hidrasyon ve solunumu değerlendirip '
                                  'kulak, boğaz, deri, eklem ve meningeal bulgular dahil odak aramak',
                          'is_correct': True,
                          'explanation': 'Ateşli çocukta risk değerlendirmesi genel görünüm (aktivite, renk, '
                                         'hidrasyon, solunum) ve odak araştırmasına dayanır. Aşı durumu ve sünnet '
                                         'bilgisi risk sınıflamasına katkı sağlar.',
                          'new_finding': 'Vital Bulgular: Ateş 39.2°C, KTA 146/dk, SS 30/dk, SpO2 %99, KDZ 2 sn. '
                                         'Uyanık, gülümsüyor, oyuncağa uzanıyor, ağladığında kolayca susuyor. Cilt '
                                         'pembe, döküntü veya peteşi yok. Mukozalar nemli. Kulak zarları normal, '
                                         'farenks hafif hiperemik, tonsil eksüdası yok. Akciğer sesleri temiz, çekilme '
                                         'yok. Karın rahat. Eklem şişliği yok. Ense sertliği yok. Sünnetli.'},
                         {'text': 'Ateşin yüksekliği nedeniyle olası bir bakteriyemiyi önlemek için muayene sonrası '
                                  'tek doz intramüsküler seftriakson yapıp ertesi gün kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Seftriakson sonrası ateş devam etti; ertesi gün tanı koymak güçleşti ve '
                                             'aile antibiyotiğin işe yaramadığını düşündü.',
                          'teaching_point': 'Ampirik antibiyotik odak bulunamayan ateşli çocukta tanıyı maskeler ve '
                                            'aşılı çocukta önerilmez.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'İyi görünen ve odak saptanmayan bu çocukta hangi tetkik yaklaşımı uygundur?',
             'options': [{'text': 'Gizli bakteriyemiyi dışlamak için tam kan sayımı ve kan kültürü almak; lökosit '
                                  "15.000/mm³'ün üzerindeyse akciğer grafisi de istemek",
                          'is_correct': False,
                          'scenario_update': 'Lökosit 13.400/mm³ geldi, kültür sonucu iki gün sonra negatif '
                                             'bildirildi; yönetim değişmedi.',
                          'teaching_point': 'Konjuge aşılar sonrası gizli bakteriyemi çok nadir olduğundan aşılı ve '
                                            'iyi görünen çocukta rutin kan tetkiki önerilmez.'},
                         {'text': 'Aşıları tam ve sünnetli olduğu için şu an tetkik istememek; ateş 48 saati aşarsa '
                                  'idrar tetkikiyle yeniden değerlendirme planını aileyle paylaşmak',
                          'is_correct': True,
                          'explanation': 'İyi görünen, aşılı çocukta ciddi bakteriyel enfeksiyon olasılığı düşüktür. '
                                         'Sünnetli erkekte idrar yolu enfeksiyonu riski düşüktür; ateş uzarsa idrar '
                                         'tetkiki yapılır. Net bir izlem planı tetkiklerin yerini alır.',
                          'new_finding': 'Tetkik istenmedi. Aileye yeniden değerlendirme için açık ölçütler anlatıldı: '
                                         'ateşin 48 saati aşması, kusma, sıvı alamama, döküntü, uykuya meyil, solunum '
                                         'sıkıntısı.'},
                         {'text': 'Ateşli her çocukta idrar enfeksiyonu dışlanmalı diyerek torba ile idrar toplamak, '
                                  'sonuç normal gelene kadar çocuğu acil serviste saatlerce bekletmek',
                          'is_correct': False,
                          'scenario_update': 'Torba idrarında 8-10 lökosit görüldü ve kontaminasyon nedeniyle kültür '
                                             'gönderildi; aile gereksiz yere antibiyotik talep etti.',
                          'teaching_point': 'Torba idrarı kültür için güvenilir değildir; tetkik kararı risk '
                                            'faktörlerine göre verilmelidir.'},
                         {'text': 'Öksürük olmasa da gizli pnömoniyi dışlamak için akciğer grafisi çekmek ve normalse '
                                  'ek tetkik yapmadan taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Grafi normal geldi; çocuk gereksiz radyasyon aldı.',
                          'teaching_point': 'Solunum bulgusu ve hipoksi olmayan çocukta rutin akciğer grafisi '
                                            'gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bu çocukta en olası tanınız nedir?',
             'options': [{'text': 'Gizli pnömokok bakteriyemisi',
                          'is_correct': False,
                          'scenario_update': 'Pnömokok aşıları tamdı ve çocuk iyi görünüyordu.',
                          'teaching_point': "Konjuge aşı sonrası gizli bakteriyemi oranı %1'in altına inmiştir."},
                         {'text': 'Odak saptanmayan ateş (olası viral)',
                          'is_correct': True,
                          'explanation': 'Kısa süreli ateş, iyi genel görünüm, odak yokluğu, tam aşılama ve evde '
                                         'benzer hastalık öyküsü düşük riskli, büyük olasılıkla viral bir ateşi '
                                         'gösterir.',
                          'new_finding': 'Tanı: Odak saptanmayan ateş, düşük risk (olası viral enfeksiyon).'},
                         {'text': 'Ateşli idrar yolu enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Ateş 24 saatlikti, sünnetliydi ve risk faktörü düşüktü; ateş uzarsa '
                                             'yeniden değerlendirilecekti.',
                          'teaching_point': 'İdrar yolu enfeksiyonu bu yaşta en sık gizli bakteriyel enfeksiyondur; '
                                            'risk sünnetsiz erkek ve kızlarda daha yüksektir.'},
                         {'text': 'Kawasaki hastalığı (erken dönem)',
                          'is_correct': False,
                          'scenario_update': 'Ateş henüz birinci gündeydi ve hiçbir mukokutanöz bulgu yoktu.',
                          'teaching_point': 'Kawasaki için en az 5 gün ateş ve tipik bulgular aranır.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Ateş konusunda çok kaygılı olan bu aileye hangi öneriler verilmelidir?',
             'options': [{'text': 'Ateşin febril nöbete yol açmaması için parasetamol ve ibuprofeni ikişer saat arayla '
                                  'dönüşümlü vermeye ve gece uyandırarak ilaç vermeye devam etmelerini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Aile bir günde önerilenden fazla doz verdi; çocukta karın ağrısı ve '
                                             'kusma gelişti.',
                          'teaching_point': 'Dönüşümlü kullanım doz hatası riskini artırır ve ateş düşürücüler febril '
                                            'nöbeti önlemez; uyuyan çocuk ilaç için uyandırılmaz.'},
                         {'text': 'Parasetamol 15 mg/kg 4-6 saatte veya ibuprofen 10 mg/kg 6-8 saatte, tek ilaçla '
                                  'vermek; amacın rahatlatmak olduğunu ve uyarı bulgularını anlatmak',
                          'is_correct': True,
                          'explanation': 'Ateş düşürücü çocuğu rahatlatmak için verilir, ateşi normale getirmek hedef '
                                         'değildir. Tek ilaç ve doğru doz güvenlidir. Uyarı bulguları ve 48 saatte '
                                         'yeniden değerlendirme aileyi rahatlatır.',
                          'new_finding': 'Aileye 11 kg için parasetamol 165 mg ve ibuprofen 110 mg dozları yazılı '
                                         'olarak verildi. İkinci gün ateş düştü; dördüncü gün gövdede pembe '
                                         'makülopapüler döküntü çıktı, çocuk iyiydi.'},
                         {'text': 'Ateşi hızla düşürmek için çocuğu soğuk suyla yıkamalarını veya alkollü bezle '
                                  "silmelerini önermek ve ateş 38°C'nin altına inene kadar ilaç vermelerini söylemek",
                          'is_correct': False,
                          'scenario_update': 'Alkollü bezle silme sonrası çocuk titredi ve huzursuzlandı; ateş kısa '
                                             'süre sonra yeniden yükseldi.',
                          'teaching_point': 'Soğuk su ve alkolle silme titremeye ve rahatsızlığa yol açar, alkol '
                                            'emilimi toksiktir; önerilmez.'},
                         {'text': 'Ailenin kaygısını gidermek için güvence amaçlı 5 gün amoksisilin reçete etmek ve '
                                  'ateş düşmezse iki gün sonra kontrole gelmelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'Dördüncü gün çıkan döküntü amoksisilin alerjisi sanıldı ve çocuk yanlış '
                                             'biçimde alerjik olarak etiketlendi.',
                          'teaching_point': 'Viral ateşte antibiyotik yararsızdır ve döküntü gibi tabloların yorumunu '
                                            'karıştırır.'}]}]},
 {'id': 'Y78',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '5 Yaşında (19 kg)',
  'gender': 'Kız',
  'complaint': 'İki gündür ateş, boğaz ağrısı ve bugün başlayan kaşıntılı kırmızı döküntü',
  'history': "Annesi anlatıyor: 'Dün aniden ateşlendi, 39°C'ye çıktı, boğazı ağrıdı ve iki kez kustu, karnı ağrıdı. Bu "
             'sabah boynunda ve göğsünde kırmızı, pütür pütür döküntüler çıktı, sonra koltuk altlarına ve kasıklara '
             "yayıldı. Kaşınıyor.' Öksürük ve burun akıntısı yok. Anaokulunda birkaç çocukta benzer döküntü varmış. "
             'Herhangi bir ilaç kullanmamış. Aşıları tam. İlaç alerjisi yok.',
  'final_diagnosis': 'Kızıl (Skarlatina - A Grubu Beta-Hemolitik Streptokok)',
  'disposition': 'On Gün Oral Amoksisilin ve Okula Dönüş Önerileriyle Yeşil Alandan Taburculuk',
  'case_pearl': "Kızıl, eritrojenik toksin üreten AGBHS'ye bağlıdır. Zımpara kâğıdı dokusunda, basmakla solan, kıvrım "
                'yerlerinde yoğunlaşan (Pastia çizgileri) döküntü, çilek dil, perioral solukluk ve farenjit tipiktir. '
                'Hızlı antijen testi veya kültürle doğrulanır. Tedavi 10 gün amoksisilin (50 mg/kg/gün, en çok 1000 '
                'mg) veya penisilindir. Antibiyotiğin ilk 24 saatinden sonra okula dönülebilir. 1-3 hafta sonra '
                'el-ayakta soyulma olabilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Ateş, boğaz ağrısı ve döküntüsü olan bu çocukta muayenede neye dikkat edersiniz?',
             'options': [{'text': 'Döküntünün dokusunu, dağılımını ve basmakla solmasını, ağız içini, dili, farenksi, '
                                  'boyun lenf nodlarını, el-ayakları ve perfüzyonu sistematik olarak değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Döküntünün özellikleri (doku, dağılım, solma) ile ağız-dil bulguları ayırıcı '
                                         'tanının temelidir. Perfüzyon ve genel görünüm toksik tabloları dışlamak için '
                                         'gereklidir.',
                          'new_finding': 'Vital Bulgular: Ateş 38.8°C, KTA 124/dk, SS 22/dk, SpO2 %99, TA 98/60 mmHg, '
                                         'KDZ 2 sn. Boyun, gövde ve kıvrım yerlerinde basmakla solan, zımpara kâğıdı '
                                         'dokusunda ince papüler kırmızı döküntü; koltuk altı ve dirsek kıvrımında '
                                         'koyu kırmızı çizgilenme. Ağız çevresi soluk, yanaklar kızarık. Dil kırmızı, '
                                         'papiller belirgin. Tonsiller 2+ hiperemik, damakta peteşiler. Bilateral '
                                         'hassas anterior servikal lenf nodları. Konjonktivit yok, dudaklar çatlak '
                                         'değil, el-ayakta ödem yok.'},
                         {'text': 'Döküntüyü viral ekzantem olarak kabul edip boğaz muayenesine gerek duymadan '
                                  'antihistaminik ve ateş düşürücüyle taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Döküntü kaşıntısı biraz azaldı ancak ateş ve boğaz ağrısı sürdü; aynı '
                                             'sınıftan iki çocuk daha hastalandı.',
                          'teaching_point': 'Ateşli döküntüde ağız içi ve farenks muayenesi tanı için kritiktir; '
                                            'tedavi edilebilir bakteriyel nedenler atlanmamalıdır.'},
                         {'text': 'Ateş ve yaygın kırmızı döküntü nedeniyle toksik şok olasılığıyla çocuğu Sarı Alana '
                                  'alıp damar yolu açarak sıvı bolusu başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Çocuğun perfüzyonu ve tansiyonu normaldi; gereksiz damar yolu ve bolus '
                                             'uygulandı.',
                          'teaching_point': 'Toksik şokta hipotansiyon ve çoklu organ tutulumu beklenir; iyi görünen, '
                                            'perfüzyonu normal çocukta bu yaklaşım gereksizdir.'},
                         {'text': 'Döküntüyü kızamık olabilir diye çocuğu izole edip yalnızca serolojik testleri '
                                  'göndermek, ağız ve boğaz muayenesini sonuçlara bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Seroloji sonuçları günler sonra negatif geldi; bu sürede tedavi '
                                             'başlanmadı.',
                          'teaching_point': 'Kızamıkta öksürük, burun akıntısı ve konjonktivit prodromu olur; ayırım '
                                            'klinik muayeneyle hemen yapılabilir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Bu çocukta tanıyı doğrulamak için hangi tetkik yaklaşımı uygundur?',
             'options': [{'text': 'Tam kan sayımı, CRP ve ASO istemek; ASO yüksek gelirse bakteriyel enfeksiyon kabul '
                                  'edip antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'ASO normal geldi ve antibiyotik başlanmadı; ancak akut enfeksiyonun ilk '
                                             'günlerinde ASO henüz yükselmemişti.',
                          'teaching_point': 'ASO geçirilmiş enfeksiyonu gösterir ve 1-3 haftada yükselir; akut tanıda '
                                            'kullanılmaz.'},
                         {'text': 'Boğazdan hızlı strep antijen testi yapmak, test negatif çıkarsa boğaz kültürü ile '
                                  'doğrulamak',
                          'is_correct': True,
                          'explanation': 'Tanı farenksten bakterinin gösterilmesiyle doğrulanır. Çocuklarda hızlı test '
                                         'negatifse kültürle doğrulama önerilir.',
                          'new_finding': 'Hızlı strep antijen testi pozitif.'},
                         {'text': 'Döküntü nedeniyle deri biyopsisi planlamak ve dermatoloji görüşü alındıktan sonra '
                                  'tedavi seçeneklerini değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Biyopsi nonspesifik inflamasyon gösterdi; tedavi günlerce gecikti.',
                          'teaching_point': 'Bu döküntüde biyopsinin tanısal değeri yoktur; tanı farenksten bakteri '
                                            'gösterilerek konur.'},
                         {'text': 'Test yapmadan ampirik olarak amoksisilin başlamak, iki gün sonra düzelme yoksa '
                                  'boğaz kültürü almak üzere kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik sonrası alınan kültür yorumlanamadı ve ailenin temaslı '
                                             'çocukları için net bilgi verilemedi.',
                          'teaching_point': 'Antibiyotik öncesi test tanıyı kesinleştirir ve gereksiz antibiyotik '
                                            'kullanımını önler.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Kawasaki hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Ateş ikinci gündeydi, konjonktivit, dudak çatlağı ve el-ayak ödemi '
                                             'yoktu, strep testi pozitifti.',
                          'teaching_point': "Kawasaki'de beş gün ateş ve konjonktivit, dudak, el-ayak bulguları "
                                            'aranır; strep testi negatiftir.'},
                         {'text': 'Stafilokoksik haşlanmış deri sendromu',
                          'is_correct': False,
                          'scenario_update': 'Deride hassasiyet, büller veya soyulma yoktu.',
                          'teaching_point': 'Haşlanmış deri sendromunda deri hassastır, Nikolsky pozitiftir ve yüzeyel '
                                            'soyulma olur.'},
                         {'text': 'Kızıl (skarlatina)',
                          'is_correct': True,
                          'explanation': 'Ateş, farenjit, zımpara dokusunda kıvrım yerlerinde yoğunlaşan döküntü, '
                                         'Pastia çizgileri, çilek dil, perioral solukluk ve pozitif hızlı test kızılı '
                                         'gösterir.',
                          'new_finding': 'Tanı: Kızıl (AGBHS farenjiti ve skarlatiniform döküntü).'},
                         {'text': 'Amoksisiline bağlı ilaç döküntüsü',
                          'is_correct': False,
                          'scenario_update': 'Çocuk döküntü öncesinde hiçbir ilaç kullanmamıştı.',
                          'teaching_point': 'İlaç döküntüsü için zamansal ilaç maruziyeti gerekir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi ve taburculuk planı hangisidir?',
             'options': [{'text': 'Döküntü kaybolunca antibiyotiğin kesilebileceğini söyleyip 5 gün amoksisilin vermek '
                                  've döküntü tamamen geçene dek okula gitmemesini istemek',
                          'is_correct': False,
                          'scenario_update': 'Tedavi beşinci gün kesildi; iki hafta sonra boğaz ağrısı tekrarladı ve '
                                             'çocuk okul kaybı yaşadı.',
                          'teaching_point': 'Amoksisilin 10 gün verilmelidir. Okula dönüş antibiyotiğin ilk 24 '
                                            'saatinden sonra mümkündür.'},
                         {'text': 'Amoksisilin 50 mg/kg/gün (en çok 1000 mg) 10 gün vermek; antibiyotiğin 24. '
                                  'saatinden sonra okula dönebileceğini ve soyulmanın zararsız olduğunu anlatmak',
                          'is_correct': True,
                          'explanation': 'Amoksisilin 10 gün tedavi romatizmal ateşi önler. Antibiyotiğin ilk 24 '
                                         'saatinden sonra bulaştırıcılık belirgin azalır. Sonradan görülen el-ayak '
                                         'soyulması beklenen bir bulgudur.',
                          'new_finding': 'Amoksisilin 950 mg günde tek doz başlandı. Ateş 24 saatte düştü ve çocuk '
                                         'ikinci gün okula döndü. İkinci haftada parmak uçlarında hafif soyulma oldu.'},
                         {'text': 'İlk seçenek olarak 3 gün azitromisin vermek ve tedavi bittikten sonra tedavi '
                                  'başarısını göstermek için kontrol boğaz kültürü almak',
                          'is_correct': False,
                          'scenario_update': 'Azitromisine rağmen ateş sürdü; kontrol kültürü taşıyıcılık nedeniyle '
                                             'pozitif kaldı ve aile gereksiz yere endişelendi.',
                          'teaching_point': 'Makrolidler yalnızca gerçek penisilin alerjisinde seçilir ve direnç '
                                            'sorunu vardır. Rutin kontrol kültürü önerilmez.'},
                         {'text': 'Tek doz intramüsküler seftriakson uygulamak ve kaşıntı için oral kortikosteroid '
                                  'başlayarak ailenin evdeki tüm bireylerine profilaktik antibiyotik yazmak',
                          'is_correct': False,
                          'scenario_update': 'Tek doz seftriakson yeterli tedavi sağlamadı; ev halkına gereksiz '
                                             'antibiyotik verildi.',
                          'teaching_point': 'Tek doz seftriakson AGBHS tedavisinde yeterli değildir. Semptomsuz '
                                            'temaslılara rutin profilaksi önerilmez.'}]}]},
 {'id': 'Y79',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '3 Yaşında (14 kg)',
  'gender': 'Erkek',
  'complaint': 'Beş gündür yüksek ateş, öksürük, gözlerde kızarıklık ve dün yüzden başlayıp gövdeye yayılan döküntü',
  'history': "Annesi anlatıyor: 'Beş gündür ateşi 39.5-40°C. Öksürüyor, burnu akıyor, gözleri kızarık ve ışıktan "
             'rahatsız oluyor. Dün akşam saç diplerinden ve kulak arkasından kırmızı döküntüler başladı, bugün gövdeye '
             "indi.' Aile aşılarını yaptırmamış ('aşı karşıtıyız'). İki hafta önce hastanede ateşli bir çocukla aynı "
             'bekleme salonunda bulunmuşlar. İshal yok, iştahı azalmış ama sıvı alıyor. Evde 8 aylık bir kardeşi var.',
  'final_diagnosis': 'Kızamık (Komplikasyonsuz)',
  'disposition': 'Solunum İzolasyonu, A Vitamini, Halk Sağlığına Bildirim ve Temaslı Taramasıyla Evde İzlem',
  'case_pearl': 'Kızamık ateş, öksürük, burun akıntısı ve konjonktivit prodromuyla başlar. Yanak mukozasında Koplik '
                'lekeleri döküntüden 1-2 gün önce çıkar. Makülopapüler döküntü saç çizgisinden başlayıp aşağı yayılır. '
                'Hava yoluyla bulaşır, bu yüzden hemen solunum izolasyonu gerekir. Döküntü başladıktan sonraki 4 gün '
                'bulaşıcıdır. Tanı IgM serolojisi ve boğaz/idrar PCR ile doğrulanır ve bildirimi zorunludur. Tüm '
                'olgulara iki gün A vitamini verilir (12 ay üzeri 200.000 IU/gün). Temaslılara ilk 72 saatte KKK '
                'aşısı, 6 gün içinde riskli bebek ve bağışıklığı baskılanmışlara immünoglobulin önerilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Aşısız, beş gündür ateşi olan ve döküntüsü başlayan bu çocukta ilk yaklaşımınız nedir?',
             'options': [{'text': 'Çocuğu diğer hastalarla birlikte genel bekleme salonunda tutup sırası gelince '
                                  'muayene etmek, döküntünün dağılımı ve özelliklerini değerlendirerek tanıya karar '
                                  'vermek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk bir saat bekleme salonunda kaldı; sonraki haftalarda aynı '
                                             'salondaki iki aşısız bebekte benzer tablo gelişti.',
                          'teaching_point': 'Aşısız çocukta ateş, öksürük, konjonktivit ve döküntü birlikteliğinde '
                                            'hava yoluyla bulaş riski nedeniyle hemen izolasyon gerekir.'},
                         {'text': 'Çocuğu ve aileyi maskeyle hemen ayrı, kapalı bir odaya almak; hidrasyon, solunum, '
                                  'kulak, ağız içi ve göz bulgularını muayene etmek',
                          'is_correct': True,
                          'explanation': 'Hava yoluyla bulaşan ateşli döküntülü hastalık şüphesinde ilk adım '
                                         'izolasyondur. Muayenede komplikasyonlar (pnömoni, otit, dehidratasyon, '
                                         'ensefalit) ve tanısal ağız bulguları aranır.',
                          'new_finding': 'Vital Bulgular: Ateş 39.8°C, KTA 138/dk, SS 30/dk, SpO2 %97, KDZ 2 sn. '
                                         'Mukozalar hafif kuru, idrar yapıyor. Bilateral eksüdasız konjonktivit ve '
                                         'fotofobi. Yanak mukozasında alt azı dişleri hizasında kırmızı zemin üzerinde '
                                         'beyaz kum tanesi gibi noktalar. Yüz, kulak arkası, boyun ve gövdede birleşme '
                                         'eğilimli makülopapüler döküntü, el ve ayaklarda henüz yok. Akciğerlerde '
                                         'birkaç kaba ral, çekilme yok. Kulak zarları hafif hiperemik, bombe değil. '
                                         'Bilinç açık, ense sertliği yok.'},
                         {'text': 'Beş gündür süren ateş ve konjonktivit nedeniyle muayeneyi kısa tutup '
                                  'ekokardiyografi ve inflamatuvar belirteçler istemek',
                          'is_correct': False,
                          'scenario_update': 'Ekokardiyografi normal geldi; çocuk saatlerce ortak alanlarda bekledi ve '
                                             'izolasyona alınmadı.',
                          'teaching_point': 'Belirgin öksürük, burun akıntısı ve aşısızlık öyküsü başka bir tanıya '
                                            'işaret eder; izolasyon öncelikle düşünülmelidir.'},
                         {'text': 'Ateş ve öksürük nedeniyle önce akciğer grafisi çektirmek için radyoloji bekleme '
                                  'alanına göndermek, sonra döküntüyü değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk radyoloji bekleme alanında 40 dakika kaldı; daha sonra temaslı '
                                             'taraması gereken kişi sayısı arttı.',
                          'teaching_point': 'Bulaş riski olan hasta ortak alanlarda dolaştırılmaz; görüntüleme '
                                            'gerekiyorsa izolasyon önlemleriyle yapılır.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'İzole edilen bu çocukta hangi tetkik yaklaşımı uygundur?',
             'options': [{'text': 'Tanının klinik olduğunu düşünerek hiçbir tetkik istememek ve bildirimin yalnızca '
                                  'laboratuvar doğrulaması gerektiren olgular için yapıldığını kabul etmek',
                          'is_correct': False,
                          'scenario_update': 'Olgu bildirilmedi ve laboratuvarla doğrulanmadı; halk sağlığı birimi '
                                             'temaslıları zamanında taramadı.',
                          'teaching_point': 'Şüpheli olgu bile bildirilmelidir; laboratuvar doğrulaması salgın '
                                            'kontrolü için gereklidir.'},
                         {'text': "Serum IgM serolojisi ile boğaz sürüntüsü ve idrardan virüs PCR'si göndermek ve "
                                  'olguyu laboratuvar sonucunu beklemeden halk sağlığına bildirmek',
                          'is_correct': True,
                          'explanation': 'Laboratuvar doğrulaması IgM ve PCR ile yapılır. Bildirim şüphe aşamasında '
                                         'yapılır, böylece temaslı taraması ve profilaksi zamanında başlar.',
                          'new_finding': 'Serum, boğaz sürüntüsü ve idrar örnekleri gönderildi; olgu aynı gün halk '
                                         'sağlığı birimine bildirildi. İki gün sonra IgM pozitif ve boğaz PCR pozitif '
                                         'bildirildi.'},
                         {'text': 'Ralleri nedeniyle hemogram, CRP, kan kültürü ve akciğer grafisi istemek, lökositoz '
                                  'saptanırsa bakteriyel pnömoni düşünerek hemen IV antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'Lökosit 5.800/mm³ geldi, grafide hafif peribronşiyal kalınlaşma vardı; '
                                             'tanısal test istenmediği için tanı netleşmedi.',
                          'teaching_point': 'Hipoksi ve belirgin solunum sıkıntısı olmayan çocukta rutin grafi ve '
                                            'kültür gerekmez; tanısal test ve bildirim önceliklidir.'},
                         {'text': "Lomber ponksiyon yapıp BOS'ta viral PCR çalışmak ve sonuç gelene kadar çocuğu "
                                  'servise yatırarak asiklovir başlamak',
                          'is_correct': False,
                          'scenario_update': 'BOS normal geldi; nörolojik bulgusu olmayan çocuğa gereksiz invaziv '
                                             'girişim ve tedavi uygulandı.',
                          'teaching_point': 'Nörolojik bulgu yokken BOS incelemesi endike değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Kawasaki hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Belirgin öksürük, burun akıntısı, eksüdasız konjonktivitle fotofobi ve '
                                             'yanak mukozasında beyaz noktalar vardı.',
                          'teaching_point': "Kawasaki'de solunum yolu prodromu belirgin değildir ve yanak mukozası "
                                            'lekeleri görülmez.'},
                         {'text': 'Kızamık (rubeola)',
                          'is_correct': True,
                          'explanation': 'Aşısız çocukta ateş, öksürük, burun akıntısı, konjonktivit, Koplik lekeleri '
                                         've saç çizgisinden aşağı yayılan makülopapüler döküntü kızamığı gösterir.',
                          'new_finding': 'Tanı: Kızamık (komplikasyonsuz).'},
                         {'text': 'Kızamıkçık (rubella)',
                          'is_correct': False,
                          'scenario_update': 'Ateş yüksek ve uzun süreliydi, öksürük ve konjonktivit belirgindi.',
                          'teaching_point': 'Kızamıkçıkta ateş hafif ve kısadır, postaurikuler ve oksipital '
                                            'lenfadenopati belirgindir.'},
                         {'text': 'Roseola infantum',
                          'is_correct': False,
                          'scenario_update': 'Döküntü ateş sürerken çıkmıştı ve 3 yaşındaydı.',
                          'teaching_point': 'Roseolada döküntü ateş düştükten sonra çıkar ve genellikle 2 yaş altında '
                                            'görülür.'}]},
            {'stage_title': 'Tedavi ve İzlem Planı',
             'question': 'Bu çocuk ve ailesi için en uygun plan hangisidir?',
             'options': [{'text': 'İki gün A vitamini 200.000 IU vermek, döküntüden sonra 4 gün evde izolasyon önermek '
                                  've 8 aylık kardeş için profilaksi planlamak',
                          'is_correct': True,
                          'explanation': 'A vitamini komplikasyon ve ölüm riskini azaltır. Döküntüden sonraki 4 gün '
                                         'bulaştırıcıdır. 8 aylık kardeşe temastan sonraki 72 saat içinde KKK aşısı '
                                         'veya 6 gün içinde immünoglobulin önerilir.',
                          'new_finding': 'A vitamini iki gün verildi. Halk sağlığı birimi 8 aylık kardeşe KKK aşısı '
                                         'uyguladı ve diğer temaslıları taradı. Ateş döküntünün üçüncü gününde düştü; '
                                         'komplikasyon gelişmedi.'},
                         {'text': 'Sekonder bakteriyel pnömoniyi önlemek için 10 gün amoksisilin-klavulanat başlamak, '
                                  'ateş düştüğünde kreşe gönderebileceklerini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Ateşi düşen çocuk döküntünün ikinci gününde kreşe gitti; kreşte üç '
                                             'aşısız çocukta hastalık görüldü.',
                          'teaching_point': 'Profilaktik antibiyotik önerilmez; izolasyon ateşin düşmesine değil '
                                            'döküntü başlangıcından itibaren 4 güne göre belirlenir.'},
                         {'text': 'Viral replikasyonu baskılamak için oral ribavirin başlamak ve evdeki 8 aylık '
                                  'kardeşi aşı yaşı gelmediği için takip dışı bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Ribavirin komplikasyonsuz olguda yarar sağlamadı; 8 aylık kardeş 12 gün '
                                             'sonra ağır kızamık pnömonisiyle yatırıldı.',
                          'teaching_point': 'Komplikasyonsuz olguda antiviral önerilmez. 12 aydan küçük temaslılara da '
                                            'profilaksi uygulanır.'},
                         {'text': 'Çocuğu ateş düşene kadar çocuk servisinde ortak odada yatırmak, A vitaminini '
                                  'yalnızca ishali olan olgulara saklamak',
                          'is_correct': False,
                          'scenario_update': 'Ortak odada yatan iki bebek temaslı oldu; A vitamini verilmeyen çocukta '
                                             'komplikasyon riski azaltılmadı.',
                          'teaching_point': 'Yatış gerekiyorsa negatif basınçlı tek kişilik odada izolasyon yapılır. A '
                                            'vitamini tüm olgulara verilmelidir.'}]}]},
 {'id': 'Y80',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '12 Yaşında',
  'gender': 'Erkek',
  'complaint': 'İki gündür her iki kulak önünde ve çene köşesinde ağrılı şişlik, çiğnerken ağrı ve hafif ateş',
  'history': "Kendisi anlatıyor: 'Önce sağ tarafta kulak önü şişti, dün sol taraf da şişti. Limon suyu içince ağrı "
             "artıyor, çiğneyemiyorum.' Ateşi 38.2°C. Okulunda son iki haftada benzer şişliği olan birkaç öğrenci var. "
             'KKK aşısının iki dozunun da yapıldığı aşı kartında görülüyor. Testislerde ağrı, baş ağrısı, kusma ve '
             'karın ağrısı yok. Diş şikâyeti yok.',
  'final_diagnosis': 'Kabakulak (Bilateral Parotit, Komplikasyonsuz)',
  'disposition': 'Destek Tedavisi, 5 Gün Okuldan İzolasyon ve Halk Sağlığına Bildirimle Yeşil Alandan Taburculuk',
  'case_pearl': 'Kabakulak tipik olarak 1-2 gün içinde iki taraflı hale gelen parotis şişliğiyle seyreder; şişlik '
                'kulak memesini yukarı ve dışa iter ve mandibula açısını siler. İki doz aşılılarda da okul ve kampüs '
                'salgınları görülebilir. Tanı bukkal sürüntüde PCR ve IgM ile doğrulanır; bildirim zorunludur. Şişlik '
                'başladıktan sonraki 5 gün izolasyon gerekir. Orşit, menenjit, pankreatit ve işitme kaybı açısından '
                'uyarı bulguları anlatılmalıdır. Tedavi destekleyicidir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Kulak önünde iki taraflı şişliği olan bu ergende muayenede nelere dikkat edersiniz?',
             'options': [{'text': 'Şişliğin bez mi lenf nodu mu olduğunu, kanal ağzını ve dişleri incelemek; testis, '
                                  'ense sertliği ve karın muayenesi yapmak',
                          'is_correct': True,
                          'explanation': 'Şişliğin anatomik yeri tanıyı belirler. Kanal ağzından püy gelmesi '
                                         'bakteriyel enfeksiyonu düşündürür. Testis, meninks ve karın muayenesi '
                                         'komplikasyonları dışlamak için gereklidir.',
                          'new_finding': 'Vital Bulgular: Ateş 38.1°C, KTA 96/dk, SS 18/dk, SpO2 %99. Her iki kulak '
                                         'önünde, kulak memesini yukarı-dışa iten, mandibula açısını silen, hassas, '
                                         'sıcak olmayan hamurumsu şişlik. Bukkal mukozada, ikinci üst azı hizasında '
                                         'kanal ağızları hafif kızarık, masajla berrak tükürük geliyor, püy yok. '
                                         'Dişler sağlam. Servikal lenf nodları ayrıca ele gelmiyor. Testisler normal '
                                         've ağrısız. Ense sertliği yok. Karın rahat.'},
                         {'text': 'Şişliği servikal lenfadenit kabul edip ağız içi ve diğer sistem muayenelerine gerek '
                                  'duymadan amoksisilin-klavulanat başlamak',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotiğe rağmen şişlik bir hafta sürdü; komplikasyon bulguları '
                                             'değerlendirilmedi.',
                          'teaching_point': 'Şişliğin bez kaynaklı mı lenf nodu mu olduğu muayeneyle ayırt '
                                            'edilmelidir; antibiyotik viral bez tutulumunda yararsızdır.'},
                         {'text': 'Şişliğin kitle olabileceğini düşünerek acil boyun bilgisayarlı tomografisi ve ince '
                                  'iğne aspirasyonu planlamak, muayeneyi sonrasına bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Tomografi iki taraflı bez büyümesi gösterdi; aspirasyon gereksiz bir '
                                             'girişim olarak değerlendirildi.',
                          'teaching_point': 'Akut, ateşli, iki taraflı bez şişliğinde invaziv tetkikler gerekmez.'},
                         {'text': 'Aşıları tam olduğu için viral bir enfeksiyonu dışlayıp şişliği diş apsesi olarak '
                                  'değerlendirmek ve diş hekimine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Diş muayenesi normaldi; hasta iki gün sonra okulda başka öğrencilere '
                                             'bulaştırdıktan sonra yeniden başvurdu.',
                          'teaching_point': 'İki doz aşı enfeksiyonu tamamen dışlamaz; okul salgınlarında aşılı '
                                            'çocuklar da hastalanabilir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Bu hastada hangi tetkik yaklaşımı uygundur?',
             'options': [{'text': 'Tam kan sayımı, CRP ve kan kültürü istemek; CRP yüksekse bakteriyel enfeksiyon '
                                  'kabul edip intravenöz antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'CRP 12 mg/L, lökosit normal geldi; tablo açıklanmadı ve bildirim '
                                             'yapılmadı.',
                          'teaching_point': 'Kan tetkikleri viral bez enfeksiyonunu doğrulamaz; tanıya özgü test ve '
                                            'bildirim gerekir.'},
                         {'text': 'Ağız içinden bukkal sürüntü alıp PCR çalışmak, serum IgM göndermek ve olguyu halk '
                                  'sağlığına bildirmek',
                          'is_correct': True,
                          'explanation': 'Bez masajı sonrası alınan bukkal sürüntüde PCR en duyarlı testtir. Aşılı '
                                         'kişilerde IgM negatif olabilir. Olgu bildirimi salgın kontrolü için '
                                         'zorunludur.',
                          'new_finding': 'Bukkal sürüntü ve serum örnekleri gönderildi. İki gün sonra PCR pozitif, IgM '
                                         'negatif bildirildi. Okul halk sağlığı birimine bildirildi.'},
                         {'text': 'Serum amilaz ve lipaz istemek; amilaz yüksekse pankreatit kabul edip hastayı '
                                  'servise yatırarak oral alımı kesmek',
                          'is_correct': False,
                          'scenario_update': 'Amilaz 280 U/L geldi ve hasta yatırıldı; lipaz normaldi, karın bulgusu '
                                             'yoktu ve yüksek amilaz bez kaynaklıydı.',
                          'teaching_point': 'Bez tutulumunda amilaz yükselir; pankreatit tanısı için karın bulguları '
                                            've lipaz gerekir.'},
                         {'text': 'Taş olasılığı nedeniyle sialografi istemek ve tükürük kanalını açmak için limon ve '
                                  'sakız çiğnemesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Sialografi gereksiz bir girişim oldu; limon ağrıyı daha da artırdı.',
                          'teaching_point': 'İki taraflı akut şişlikte taş olasılığı düşüktür; asitli yiyecekler '
                                            'ağrıyı artırdığı için kaçınılmalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Bakteriyel süpüratif parotit',
                          'is_correct': False,
                          'scenario_update': 'Kanal ağzından püy gelmiyordu, şişlik iki taraflıydı ve deride sıcaklık '
                                             'artışı yoktu.',
                          'teaching_point': 'Bakteriyel parotit genellikle tek taraflıdır, kanaldan püy gelir ve '
                                            'ciltte kızarıklık olur.'},
                         {'text': 'Bilateral servikal lenfadenit',
                          'is_correct': False,
                          'scenario_update': 'Şişlik kulak memesini itiyor ve mandibula açısını siliyordu; lenf '
                                             'nodları ayrıca ele gelmiyordu.',
                          'teaching_point': 'Lenf nodları mandibula açısının altında yer alır ve kulak memesini '
                                            'yerinden oynatmaz.'},
                         {'text': 'Kabakulak (bilateral parotit)',
                          'is_correct': True,
                          'explanation': 'Ateşle birlikte iki taraflı, kulak memesini iten, hassas parotis şişliği, '
                                         'okul salgını ve pozitif PCR kabakulağı gösterir.',
                          'new_finding': 'Tanı: Kabakulak (bilateral parotit, komplikasyonsuz).'},
                         {'text': 'Tükürük bezi taşı (sialolitiazis)',
                          'is_correct': False,
                          'scenario_update': 'Şişlik iki taraflıydı, ateş vardı ve yemekle değişken bir öykü yoktu.',
                          'teaching_point': 'Taşta tek taraflı, yemekle artan aralıklı şişlik tipiktir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu hasta için en uygun taburculuk planı hangisidir?',
             'options': [{'text': 'Parasetamol veya ibuprofen, sıcak-soğuk kompres ve yumuşak, asitsiz gıda önermek; '
                                  'şişlik başladıktan sonra 5 gün okula gitmemesini ve uyarı bulgularını anlatmak',
                          'is_correct': True,
                          'explanation': 'Tedavi destekleyicidir. Şişlik başladıktan sonraki 5 gün bulaştırıcılık '
                                         'sürer. Testiste ağrı, şiddetli baş ağrısı, kusma veya karın ağrısı '
                                         'komplikasyonu düşündürür ve başvuru gerektirir.',
                          'new_finding': 'Hasta destek tedavisiyle taburcu edildi. Şişlik 8 günde geriledi; '
                                         'komplikasyon gelişmedi. Okula beşinci günden sonra döndü.'},
                         {'text': 'Şişliği hızla azaltmak için 5 gün oral prednizolon başlamak ve ateşi düştüğü anda '
                                  'okula dönebileceğini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Steroid seyri değiştirmedi; erken okula dönen öğrenci iki sınıf '
                                             'arkadaşına bulaştırdı.',
                          'teaching_point': 'Komplikasyonsuz olguda steroid önerilmez; izolasyon şişlik başlangıcından '
                                            'itibaren 5 gündür.'},
                         {'text': 'Orşiti önlemek için iki hafta yatak istirahati ve skrotal destek önermek, ek olarak '
                                  '7 gün amoksisilin-klavulanat vermek',
                          'is_correct': False,
                          'scenario_update': 'Uzun yatak istirahati ve antibiyotik yarar sağlamadı; hasta ishal oldu '
                                             've okul kaybı yaşadı.',
                          'teaching_point': 'Orşiti önleyen bir tedavi yoktur; antibiyotik gereksizdir. Orşit '
                                            'gelişirse destek tedavisi verilir.'},
                         {'text': 'Aşılı olduğu için ağır bir hastalık beklenmediğini, izolasyon veya bildirim '
                                  'gerekmediğini söyleyip ertesi gün rahatlıkla okula ve spor antrenmanlarına '
                                  'gönderilebileceğini aileye belirtmek',
                          'is_correct': False,
                          'scenario_update': 'Öğrenci ertesi gün okula gitti ve salgın genişledi.',
                          'teaching_point': 'Aşılı kişilerde de bulaştırıcılık sürer; izolasyon ve bildirim '
                                            'gereklidir.'}]}]}]
