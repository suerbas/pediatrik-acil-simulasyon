# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Yeşil Alan Vakaları (Part 10: Y91 - Y100)
"""

GREEN_CASES_PART10 = [{'id': 'Y91',
  'category': '💧 Sıvı-Elektrolit & Renal / Ürolojik Aciller',
  'age': '5 Yaşında',
  'gender': 'Kız',
  'complaint': 'Bir haftadır genital bölgede kaşıntı, kızarıklık, idrar yaparken yanma ve iç çamaşırında hafif sarımsı '
               'leke',
  'history': "Annesi anlatıyor: 'Bir haftadır sürekli kaşınıyor, kızarmış. Çişini yaparken yanıyor diyor. Külotunda "
             "biraz sarı leke oluyor ama kötü koku yok.' Her gün köpük banyosu yapıyor, tuvaletten sonra kendisi "
             'siliyor. Son iki ayda antibiyotik kullanmamış. Gece makat kaşıntısı fark edilmemiş. Kan, kötü kokulu '
             'akıntı yok. Ateş, karın ağrısı yok. Çocuk ve annesiyle ayrı ayrı yapılan görüşmede istismarı düşündüren '
             'bir öykü yok.',
  'final_diagnosis': 'Prepubertal Nonspesifik (İrritan) Vulvovajinit',
  'disposition': 'Hijyen ve Davranış Önerileriyle Yeşil Alandan Taburculuk',
  'case_pearl': 'Prepubertal kızlarda vulvovajinitin en sık nedeni nonspesifiktir: ince ve östrojensiz mukoza, yakın '
                'anatomik komşuluk, arkadan öne silme, köpüklü banyo ve sabun irritasyonu. Muayene kurbağa '
                'pozisyonunda dış inspeksiyonla yapılır, spekulum kullanılmaz. Kanlı ve kötü kokulu akıntı yabancı '
                'cismi, gece kaşıntısı kıl kurdunu, porselen beyazı atrofik deri liken sklerozu düşündürür. Cinsel '
                'istismar her olguda dikkatle değerlendirilmelidir. Tedavi hijyen önlemleridir. Kandida enfeksiyonu bu '
                'yaşta nadirdir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Genital kaşıntı ve akıntısı olan bu çocukta muayeneye nasıl yaklaşırsınız?',
             'options': [{'text': 'Annenin yanında, kurbağa pozisyonunda dış genital bölgeyi incelemek; akıntının '
                                  'niteliğini, deri değişikliklerini, yabancı cisim ve travma bulgularını '
                                  'değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Bu yaşta dış inspeksiyon yeterlidir. Akıntının rengi ve kokusu, deri '
                                         'görünümü ve travma bulguları yabancı cisim, enfeksiyon, dermatolojik '
                                         'hastalık ve istismar ayırımında yol gösterir.',
                          'new_finding': 'Ateş 36.7°C, genel durum iyi. Labia majora ve minora iç yüzlerinde hafif '
                                         'eritem ve ödem, vulvada kaşıntı izleri. Introitusta az miktarda kokusuz, '
                                         'sarı-beyaz akıntı. Himen ve perianal bölge olağan, travma bulgusu yok. '
                                         'Porselen beyazı deri değişikliği yok. Görünür yabancı cisim yok.'},
                         {'text': 'Vajinal akıntının kaynağını görmek için küçük boy spekulumla muayene yapmak ve '
                                  'servikal bölgeden sürüntü almak',
                          'is_correct': False,
                          'scenario_update': 'Çocuk muayene sırasında çok korktu ve ağladı; muayene yarıda kaldı ve '
                                             'bir sonraki muayeneyi reddetti.',
                          'teaching_point': 'Prepubertal çocukta spekulum muayenesi yapılmaz; gerekirse anestezi '
                                            'altında vajinoskopi uygulanır.'},
                         {'text': 'Genital muayene yapmadan idrar yolu enfeksiyonu kabul edip yanma nedeniyle torbayla '
                                  'idrar kültürü göndermek ve ampirik oral antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'İdrar kültürü steril geldi; antibiyotik sonrası çocukta pişik ve '
                                             'kaşıntıda artış oldu.',
                          'teaching_point': 'Vulvar irritasyonda idrarın iltihaplı deriye temasıyla yanma olur; önce '
                                            'genital muayene yapılmalıdır.'},
                         {'text': 'Akıntı nedeniyle muayene yapmadan cinsel istismar kabul edip adli bildirimde '
                                  'bulunmak ve çocuğu adli tıbba yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Muayene ve görüşme yapılmadan süreç başlatıldı; aile büyük travma yaşadı '
                                             've sonradan istismar bulgusu saptanmadı.',
                          'teaching_point': 'İstismar her zaman akılda tutulmalı, ancak değerlendirme öykü ve '
                                            'muayeneyle dikkatlice yapılmalıdır.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Bulguları hafif olan bu çocukta hangi yaklaşım uygundur?',
             'options': [{'text': 'Mantar enfeksiyonu olasılığına karşı vajinal sürüntüden mantar kültürü istemek ve '
                                  'sonuç gelene dek antifungal krem başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Kültür negatif geldi; antifungal kremle tahriş arttı.',
                          'teaching_point': 'Bu yaşta kandida enfeksiyonu nadirdir; antibiyotik kullanımı, bez veya '
                                            'diyabet olmadan düşünülmez.'},
                         {'text': 'Hafif ve kokusuz akıntıda rutin tetkik istememek; akıntı pürülan veya inatçı olursa '
                                  'vajinal girişten sürüntü kültürü planlamak',
                          'is_correct': True,
                          'explanation': 'Nonspesifik irritasyonda tetkik gerekmez. Pürülan, kanlı veya tedaviye '
                                         'dirençli akıntıda kültür ve gerekirse ileri değerlendirme yapılır.',
                          'new_finding': 'Tetkik istenmedi. Risk faktörleri: köpük banyosu, arkadan öne silme, dar '
                                         'sentetik iç çamaşırı.'},
                         {'text': 'Pelvik ultrasonografi istemek ve yabancı cisim olasılığını dışlamak için sonucuna '
                                  'göre vajinoskopi randevusu planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografi normal geldi; kanlı veya kötü kokulu akıntı olmadığı için '
                                             'tetkik gereksizdi.',
                          'teaching_point': 'Yabancı cisim kanlı, kötü kokulu ve inatçı akıntıyla gelir; bu tabloda '
                                            'görüntüleme gerekmez.'},
                         {'text': 'Tam kan sayımı, CRP ve kan şekeri istemek; değerler normalse cinsel yolla bulaşan '
                                  'enfeksiyon testlerini de eklemek',
                          'is_correct': False,
                          'scenario_update': 'Tüm testler normal geldi; çocuk gereksiz kan alımı yaşadı ve aile '
                                             'kaygılandı.',
                          'teaching_point': 'Tetkikler öykü ve bulgulara göre seçilir; istismar şüphesi yoksa rutin '
                                            'CYBE testi gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Vajinal yabancı cisim',
                          'is_correct': False,
                          'scenario_update': 'Akıntı kokusuz ve kansızdı.',
                          'teaching_point': 'Yabancı cisimde (sıklıkla tuvalet kâğıdı) kötü kokulu, kanlı akıntı '
                                            'tipiktir.'},
                         {'text': 'Liken skleroz',
                          'is_correct': False,
                          'scenario_update': 'Porselen beyazı atrofik deri ve sekiz şeklinde tutulum yoktu.',
                          'teaching_point': 'Liken sklerozda vulva ve perianal bölgede beyaz, ince, kırışık deri '
                                            'görülür.'},
                         {'text': 'Kıl kurduna bağlı vulvit',
                          'is_correct': False,
                          'scenario_update': 'Gece makat kaşıntısı yoktu.',
                          'teaching_point': 'Kıl kurdunda gece artan perianal kaşıntı belirgindir; selofan bant testi '
                                            'tanı koydurur.'},
                         {'text': 'Nonspesifik (irritan) vulvovajinit',
                          'is_correct': True,
                          'explanation': 'Köpük banyosu ve hatalı silme öyküsü, hafif eritem ve kokusuz az akıntı, '
                                         'diğer nedenlerin bulgusu olmaması nonspesifik vulvovajiniti gösterir.',
                          'new_finding': 'Tanı: Prepubertal nonspesifik vulvovajinit.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Köpük banyosu ve sabunu bırakmak, önden arkaya silmek, pamuklu iç çamaşırı ve sade '
                                  'ılık su oturma banyosu önermek',
                          'is_correct': True,
                          'explanation': 'Hijyen ve irritanlardan kaçınma çoğu olguda 2-3 haftada iyileşme sağlar. '
                                         'Yanıt alınamazsa kültür ve diğer nedenler yeniden değerlendirilir.',
                          'new_finding': 'Önerilerle taburcu edildi. İki hafta sonraki kontrolde kaşıntı ve akıntı '
                                         'tamamen geçmişti.'},
                         {'text': 'Topikal klotrimazol kremini günde iki kez iki hafta sürmelerini ve kaşıntı için '
                                  'oral antihistaminik kullanmalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Antifungal krem kaşıntıyı azaltmadı ve bölgede tahriş yaptı.',
                          'teaching_point': 'Bu yaşta mantar enfeksiyonu nadirdir; irritasyon tablosunda antifungal '
                                            'yarar sağlamaz.'},
                         {'text': 'Akıntıya karşı 7 gün oral amoksisilin-klavulanat ve günde birkaç kez antiseptik '
                                  'solüsyonla bölgeyi silmelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'Antiseptik solüsyon tahrişi artırdı; antibiyotik sonrası ishal ve pişik '
                                             'gelişti.',
                          'teaching_point': 'Nonspesifik tabloda antibiyotik ve antiseptik gereksizdir, irritasyonu '
                                            'artırır.'},
                         {'text': 'Mukozayı güçlendirmek için topikal östrojen kremi iki hafta sürmek ve yanıt yoksa '
                                  'çocuk jinekolojiye sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'Östrojen krem sonrası meme tomurcuklanması ve labiyalarda '
                                             'hiperpigmentasyon gelişti.',
                          'teaching_point': 'Östrojen krem labial yapışıklık gibi seçilmiş durumlarda kısa süre '
                                            'kullanılır; bu tabloda endike değildir.'}]}]},
 {'id': 'Y92',
  'category': '👶 Ağlayan, Emmeyen, Huzursuz Bebek',
  'age': '6 Haftalık (4.6 kg)',
  'gender': 'Erkek',
  'complaint': 'Son birkaç gündür memeyi tutup ağlayarak bırakma ve ağız içinde beyaz lekeler',
  'history': "Annesi anlatıyor: 'Birkaç gündür memeyi alıyor, birkaç saniye emip ağlayarak bırakıyor. Dilinde ve "
             'yanaklarının içinde beyaz lekeler var, silmeye çalıştım çıkmadı. Bez bölgesinde de kırmızılık var. Benim '
             "meme uçlarım da çok acıyor, emzirirken yanma ve batma oluyor.' Ateş yok. Bezleri günde 6-7 kez "
             'ıslanıyor. Bir ay önce annenin meme iltihabı için antibiyotik kullandığı öğreniliyor. Bebek emzik '
             'kullanıyor. Kilo alımı düzenli.',
  'final_diagnosis': 'Oral Kandidiyazis (Pamukçuk), Bez Bölgesi Kandidiyazisi ve Annede Meme Ucu Kandidiyazisi',
  'disposition': 'Bebeğe Oral Nistatin, Anneye Topikal Antifungal ve Emzirmeye Devam Önerisiyle Yeşil Alandan '
                 'Taburculuk',
  'case_pearl': 'Süt çocuğunda dil, yanak ve damakta silinmeyen, kazındığında altında kırmızı kanamalı zemin bırakan '
                'beyaz plaklar oral kandidiyazisi gösterir; süt artığı kolayca silinir. Anneye yakın zamanda '
                'antibiyotik verilmesi, emzik kullanımı ve annede meme ucu ağrısı risk faktörüdür. Bebek ve anne '
                'birlikte tedavi edilir. 4 aydan küçük bebeklerde oral nistatin süspansiyonu tercih edilir, tedavi '
                'lezyonlar geçtikten sonra 48 saat sürdürülür. Emzik ve biberon uçları kaynatılmalıdır. Emzirme '
                'kesilmez. Sağlıklı süt çocuğunda immün yetmezlik araştırması gerekmez.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Memeyi ağlayarak bırakan ve ağzında beyaz lekeler olan bu bebekte ilk değerlendirmeniz '
                         'nedir?',
             'options': [{'text': 'Lekelerin süt artığı olduğunu düşünüp bakmadan aileyi rahatlatmak ve beslenme '
                                  'sonrası ağzı gazlı bezle sertçe silmelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'Sert silme mukozada kanamalı alanlara ve beslenmenin daha da ağrılı hale '
                                             'gelmesine yol açtı.',
                          'teaching_point': 'Lekelerin niteliği muayeneyle belirlenmelidir; mukozayı sertçe silmek '
                                            'zararlıdır.'},
                         {'text': 'Tartı ve hidrasyonu değerlendirip ağız içinde lekelerin silinip silinmediğine '
                                  'bakmak; bez bölgesini ve annenin meme uçlarını da incelemek',
                          'is_correct': True,
                          'explanation': 'Beslenme güçlüğünde hidrasyon ve kilo alımı önce değerlendirilir. Silinmeyen '
                                         'plaklar süt artığından ayırt edilir. Bez bölgesi ve anne memesi birlikte '
                                         'tedavi gerektirebilecek odaklardır.',
                          'new_finding': 'Ateş 36.8°C, tartı 4600 g (doğum ağırlığı 3300 g), mukozalar nemli, fontanel '
                                         'normal. Dil sırtı, yanak iç yüzleri ve damakta, dil basacağıyla silinmeyen, '
                                         'kazındığında altında kırmızı kanamalı zemin bırakan beyaz plaklar. Bez '
                                         'bölgesinde parlak kırmızı, kıvrımları da tutan plak ve çevresinde uydu papül '
                                         've püstüller. Annenin her iki meme ucu kırmızı ve parlak, çatlak yok.'},
                         {'text': 'Beslenme reddi nedeniyle bebeği hemen Sarı Alana alıp tam kan sayımı, CRP ve idrar '
                                  'tetkiki ile sepsis taraması başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Ateşsiz, kilo alan ve iyi görünen bebekte tüm sonuçlar normal geldi; '
                                             'ağız muayenesi saatler sonra yapıldı.',
                          'teaching_point': 'Genel durumu iyi, ateşsiz bebekte önce ayrıntılı muayene yapılır; sepsis '
                                            'taraması klinik bulgulara göre planlanır.'},
                         {'text': 'Ağız içi lekeler nedeniyle doğrudan çocuk immünoloji polikliniğine sevk etmek ve '
                                  'sevk tarihine kadar emzirmeye ara vermelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'Emzirmeye ara verilince annenin sütü azaldı; sevk için haftalarca '
                                             'beklendi.',
                          'teaching_point': 'Sağlıklı süt çocuğunda bu tablo sıktır ve tek başına immün yetmezlik '
                                            'düşündürmez; emzirme kesilmez.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'İyi görünen ve kilo alan bu bebekte hangi tetkik yaklaşımı uygundur?',
             'options': [{'text': 'Ağız plaklarından kültür almak ve tür tayini ile duyarlılık sonucu gelene kadar '
                                  'tedaviyi ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Kültür sonucu bir hafta sürdü; bu sürede bebek beslenmede zorlanmaya '
                                             'devam etti.',
                          'teaching_point': 'Tipik görünümde tanı kliniktir; kültür tedaviye dirençli olgularda '
                                            'istenir.'},
                         {'text': 'Tetkik istememek; tipik görünüm, risk faktörleri ve annedeki bulgularla klinik tanı '
                                  'koyup tedaviye geçmek',
                          'is_correct': True,
                          'explanation': 'Sağlıklı süt çocuğunda tanı kliniktir. Tekrarlayan, tedaviye dirençli veya 1 '
                                         'yaş üzerinde açıklanamayan olgularda ileri değerlendirme düşünülür.',
                          'new_finding': 'Tetkik istenmedi. Risk faktörleri: annede yakın zamanda antibiyotik '
                                         'kullanımı, emzik kullanımı ve annede meme ucu ağrısı.'},
                         {'text': 'İmmün yetmezliği dışlamak için tam kan sayımı, immünoglobulin düzeyleri, lenfosit '
                                  'alt grupları ve HIV testi istemek',
                          'is_correct': False,
                          'scenario_update': 'Tüm sonuçlar normal geldi; aile gereksiz yere büyük kaygı yaşadı.',
                          'teaching_point': 'İlk ve tipik atakta immün yetmezlik araştırması gerekmez.'},
                         {'text': 'Beslenme sırasında ağrı nedeniyle özofagusu değerlendirmek için kontrastlı üst '
                                  'gastrointestinal sistem grafisi istemek',
                          'is_correct': False,
                          'scenario_update': 'Grafi normal geldi ve bebek gereksiz radyasyon aldı.',
                          'teaching_point': 'Ağız içi lezyonu belirgin, iyi görünen bebekte görüntülemenin yeri '
                                            'yoktur.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Süt artığı ve fizyolojik dil beyazlığı',
                          'is_correct': False,
                          'scenario_update': 'Plaklar silinmiyor ve kazındığında kanamalı zemin bırakıyordu.',
                          'teaching_point': 'Süt artığı kolayca silinir ve yalnızca dil sırtında görülür.'},
                         {'text': 'Primer herpetik gingivostomatit',
                          'is_correct': False,
                          'scenario_update': 'Ateş, vezikül ve dişeti ödemi yoktu.',
                          'teaching_point': 'Herpetik stomatitte ateş, veziküller ve kanamalı dişeti görülür.'},
                         {'text': 'Oral kandidiyazis (pamukçuk)',
                          'is_correct': True,
                          'explanation': 'Silinmeyen, kanamalı zemin bırakan beyaz plaklar, bez bölgesinde uydu '
                                         'lezyonlu dermatit ve annede meme ucu yanması oral kandidiyazisi gösterir.',
                          'new_finding': 'Tanı: Oral kandidiyazis, bez bölgesi kandidiyazisi ve annede meme ucu '
                                         'kandidiyazisi.'},
                         {'text': 'Coğrafik dil',
                          'is_correct': False,
                          'scenario_update': 'Lezyonlar yanak ve damağı da tutuyordu ve beslenme ağrılıydı.',
                          'teaching_point': 'Coğrafik dil yalnızca dilde, yeri değişen haritalı alanlarla seyreder ve '
                                            'genellikle belirtisizdir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu bebek ve annesi için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Bebeğe ağızdan flukonazol başlayıp annenin emzirmeyi tedavi bitene dek bırakmasını '
                                  've sütünü sağıp dökmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Emzirme bırakıldı, süt azaldı; anne tedavi edilmediği için bebekte '
                                             'enfeksiyon tekrarladı.',
                          'teaching_point': 'Emzirme kesilmez; ilk seçenek topikal tedavidir ve anne birlikte tedavi '
                                            'edilmelidir.'},
                         {'text': 'Bebeğe günde dört kez nistatin süspansiyonu vermek ve lezyonlar geçtikten 48 saat '
                                  'sonra kesmek; anneye meme ucu kremi önerip emzikleri kaynatmak',
                          'is_correct': True,
                          'explanation': 'Nistatin bu yaşta güvenli ve etkilidir. Anne ve bebeğin birlikte tedavisi ve '
                                         'emzik-biberon uçlarının kaynatılması tekrarı önler. Bez bölgesine topikal '
                                         'antifungal krem eklenir.',
                          'new_finding': 'Bebeğe nistatin süspansiyonu ve bez bölgesine nistatin krem, anneye '
                                         'mikonazol krem başlandı. Bir hafta sonra plaklar kayboldu, emzirme ağrısız '
                                         'hale geldi.'},
                         {'text': 'Yalnızca bez bölgesine çinko oksitli krem sürmelerini önermek, ağızdaki lezyonlar '
                                  'için bir hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Ağız lezyonları yaygınlaştı ve bebek beslenmeyi büyük ölçüde reddetti.',
                          'teaching_point': 'Ağız içi lezyonlar beslenmeyi etkiliyorsa tedavi edilmelidir; bez bölgesi '
                                            'için de antifungal gerekir.'},
                         {'text': 'Beyaz plakları her beslenmeden sonra karbonatlı suya batırılmış gazlı bezle sertçe '
                                  'kazıyarak temizlemelerini ve emziği sürdürmelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'Kazıma mukozada kanamaya neden oldu ve bebek daha da huzursuzlandı.',
                          'teaching_point': 'Plaklar kazınmaz; antifungal tedavi ve emzik hijyeni yeterlidir.'}]}]},
 {'id': 'Y93',
  'category': '👶 Yenidoğan Acilleri',
  'age': '5 Günlük (3050 g)',
  'gender': 'Erkek',
  'complaint': "Annenin 'sütüm yetmiyor, bebek sürekli ağlıyor ve sarardı' yakınmasıyla başvuru",
  'history': "Annesi anlatıyor: 'İlk bebeğim. Memeye veriyorum ama sadece ucunu tutuyor, 10 dakika emip uyuyor, sonra "
             'bir saat içinde ağlayarak uyanıyor. Göğüslerim yeni dolmaya başladı. Bugün dört bez ıslattı, dışkısı '
             "kahverengi-yeşil.' 39. haftada normal doğum, doğum ağırlığı 3350 g, ikinci gün taburcu. Ateş, kusma, "
             'letarji yok. Yüzü ve göğsü sararmış. Anne ve bebek kan grupları uyumlu. Annenin meme uçları çatlak ve '
             'kanamalı.',
  'final_diagnosis': 'Yetersiz Anne Sütü Alımı (Hatalı Emzirme Tekniği, %9 Kilo Kaybı), Sodyumu Normal',
  'disposition': 'Emzirme Danışmanlığı, Sağılmış Süt Desteği ve 24-48 Saat İçinde Tartı Kontrolüyle Yeşil Alandan '
                 'Taburculuk',
  'case_pearl': "Yalnız anne sütü alan yenidoğanda doğum ağırlığının %7'sini aşan kayıp emzirme değerlendirmesi, %10'u "
                'aşan kayıp ise serum sodyumu ve bilirubin ölçümü ile yakın izlem gerektirir. Etkin emmenin '
                'göstergeleri yeterli ıslak bez (5. günden sonra ≥6), sarı dışkıya geçiş ve memede ritmik yutkunmadır. '
                'Tedavi emzirme tekniğinin düzeltilmesi, günde 8-12 kez besleme ve gerekirse sağılmış süt veya mama '
                'ile desteklemedir. Su ve şekerli su verilmez. 24-48 saat içinde tartı kontrolü yapılır.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Annesi sütünün yetmediğinden yakınan 5 günlük bu bebekte ilk değerlendirmeniz nedir?',
             'options': [{'text': 'Bebeği çıplak tartıp yüzde kilo kaybını hesaplamak, hidrasyon, sarılık ve genel '
                                  'durumu değerlendirmek ve bir emzirme seansını gözlemlemek',
                          'is_correct': True,
                          'explanation': 'Kilo kaybı yüzdesi ve hidrasyon durumu yönetimi belirler. Emzirme gözlemi '
                                         'sorunun kaynağını gösterir. Letarji ve sarılık ek değerlendirme '
                                         'gerektirebilir.',
                          'new_finding': 'Ateş 36.9°C, KTA 148/dk, SS 44/dk, KDZ 2 sn. Tartı 3050 g (doğum ağırlığının '
                                         '%9 altında). Mukozalar nemli, fontanel normal, uyarılınca canlı ağlıyor. Yüz '
                                         've göğüste sarılık. Emzirme gözleminde bebek yalnızca meme ucunu tutuyor, '
                                         'ağzı dar açık, alt dudak içe dönük, yanaklar çökük, ritmik yutkunma '
                                         'duyulmuyor. Annenin meme uçları çatlak.'},
                         {'text': 'Annenin sütünün az olduğunu kabul edip tartı, muayene ve emzirme gözlemi yapmadan '
                                  'bebeği hemen ve tamamen formül mamaya geçirmelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'Anne emzirmeyi bıraktı; meme dolgunluğu ve ağrısı arttı, emzirme fırsatı '
                                             'kaybedildi.',
                          'teaching_point': 'Süt yetersizliği algısı çoğu zaman hatalı teknikten kaynaklanır; emzirme '
                                            'gözlemlenmeden mamaya geçilmez.'},
                         {'text': 'Sarılık nedeniyle bebeği hemen yenidoğan servisine yatırıp bilirubin sonucunu '
                                  'beklemeden fototerapi ve intravenöz sıvı başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Bebek anneden ayrıldı, emzirme kesintiye uğradı; bilirubin fototerapi '
                                             'eşiğinin altında çıktı.',
                          'teaching_point': 'Fototerapi ve sıvı kararı ölçülen değerlere ve klinik duruma göre '
                                            'verilir.'},
                         {'text': 'Bebeğin sık ağlamasını kolik olarak değerlendirip simetikon damla önermek ve bir '
                                  'hafta sonra rutin kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Bebek bir hafta sonra %14 kilo kaybı ve belirgin sarılıkla getirildi.',
                          'teaching_point': 'İlk haftada sık ağlama çoğu zaman açlığa bağlıdır; kilo ve emzirme '
                                            'değerlendirilmelidir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': "Doğum ağırlığının %9'unu kaybetmiş, sarılığı olan bu bebekte hangi tetkikler uygundur?",
             'options': [{'text': 'Serum total bilirubin ile serum sodyumunu ölçmek ve bilirubini saat-yaşa göre '
                                  'fototerapi eşiğiyle karşılaştırmak',
                          'is_correct': True,
                          'explanation': 'Sarılığın düzeyi saat-yaşa göre yorumlanır. Belirgin kilo kaybında sodyum '
                                         'ölçümü hipernatremik dehidratasyonu dışlar.',
                          'new_finding': 'Total bilirubin 13.2 mg/dL (118. saat; fototerapi eşiğinin altında), direkt '
                                         'bilirubin 0.5 mg/dL. Serum sodyum 143 mmol/L, glukoz 72 mg/dL.'},
                         {'text': 'Sepsis olasılığı nedeniyle tam kan sayımı, CRP, kan kültürü ve idrar kültürü '
                                  'göndermek, sonuçlar gelene kadar antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'Ateşsiz ve iyi görünen bebek antibiyotikle yatırıldı; kültürler negatif '
                                             'geldi.',
                          'teaching_point': 'Ateş ve klinik sepsis bulgusu olmayan bebekte rutin sepsis taraması '
                                            'gerekmez.'},
                         {'text': 'Herhangi bir tetkik istemeden emzirme önerisiyle taburcu etmek ve iki hafta sonraki '
                                  'rutin aşı kontrolünde tartmak',
                          'is_correct': False,
                          'scenario_update': 'Sodyum ve bilirubin bilinmeden gönderilen bebeğin kilo kaybı bir hafta '
                                             "içinde %13'e ulaştı.",
                          'teaching_point': 'Belirgin kilo kaybı ve sarılık olan bebekte değerler ölçülmeli ve 24-48 '
                                            'saat içinde kontrol yapılmalıdır.'},
                         {'text': 'Tiroid fonksiyon testleri, idrarda metabolik tarama ve batın ultrasonografisi '
                                  'isteyip sonuçlara göre beslenme planı yapmak',
                          'is_correct': False,
                          'scenario_update': 'Sonuçlar normal geldi; asıl sorun olan emzirme tekniği bu sürede '
                                             'düzeltilmedi.',
                          'teaching_point': 'Tetkikler klinik soruya göre seçilir; emzirme sorunu gözlemle tanınır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik ve laboratuvar bulgularına göre en olası tanınız nedir?',
             'options': [{'text': 'Hipernatremik dehidratasyon',
                          'is_correct': False,
                          'scenario_update': 'Serum sodyumu 143 mmol/L ile normaldi ve hidrasyon bulguları korunmuştu.',
                          'teaching_point': 'Hipernatremik dehidratasyonda sodyum 145-150 mmol/L üzerindedir; '
                                            "genellikle kayıp %10'u aşar."},
                         {'text': 'Geç başlangıçlı neonatal sepsis',
                          'is_correct': False,
                          'scenario_update': 'Ateş, letarji ve perfüzyon bozukluğu yoktu.',
                          'teaching_point': 'Sepsiste ateş veya hipotermi, letarji ve beslenmenin tamamen azalması '
                                            'beklenir.'},
                         {'text': 'Hatalı tekniğe bağlı yetersiz anne sütü alımı',
                          'is_correct': True,
                          'explanation': 'Hatalı kavrama, ritmik yutkunmanın olmaması, %9 kilo kaybı, sınırda ıslak '
                                         'bez sayısı ve normal sodyum yetersiz anne sütü alımını gösterir.',
                          'new_finding': 'Tanı: Hatalı emzirme tekniğine bağlı yetersiz anne sütü alımı.'},
                         {'text': 'Konjenital hipotiroidi',
                          'is_correct': False,
                          'scenario_update': 'Letarji, makroglossi, kabızlık ve geniş fontanel yoktu, tarama normaldi.',
                          'teaching_point': 'Hipotiroidide uzamış sarılık, letarji ve kabızlık olur; tarama tanıyı '
                                            'koydurur.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu bebek ve annesi için en uygun plan hangisidir?',
             'options': [{'text': 'Sarılığı azaltmak için öğün aralarında su veya şekerli su vermelerini ve emzirmeyi '
                                  'üç saatte bir 10 dakikayla sınırlamalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Su verilen bebek memeye daha az talip oldu; kilo kaybı ve sarılık arttı.',
                          'teaching_point': 'Yenidoğana su ve şekerli su verilmez; emzirme süresi sınırlandırılmaz.'},
                         {'text': 'Doğru kavrama ve pozisyonu göstermek, günde 8-12 kez emzirmek ve sağılmış sütle '
                                  'desteklemek; meme ucu bakımı önerip 24-48 saatte tartı kontrolü yapmak',
                          'is_correct': True,
                          'explanation': 'Kavrama düzeltilince süt transferi artar ve meme ucu yaraları iyileşir. '
                                         'Sağılmış süt desteği kilo kaybını durdurur. Yakın tartı kontrolü etkinliği '
                                         'gösterir.',
                          'new_finding': 'Emzirme danışmanı kavramayı düzeltti, sağma gösterildi. 48. saat kontrolünde '
                                         "tartı 3120 g'a yükseldi, günde 7 bez ıslanıyordu, dışkı sarıya döndü."},
                         {'text': 'Emzirmeyi tamamen bırakıp mamaya geçmelerini, annenin sütünü kurutmak için ilaç '
                                  'almasını önermek ve bir hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Anne emzirme fırsatını kaybetti; mama ile beslenmede de gaz sancısı ve '
                                             'kabızlık başladı.',
                          'teaching_point': 'Teknik sorunlar düzeltilebilir; emzirmeyi bırakmak ilk seçenek değildir.'},
                         {'text': 'Bebeği fototerapi ve intravenöz dekstrozlu sıvı için yenidoğan servisine yatırıp '
                                  'emzirmeyi yatış süresince durdurmak',
                          'is_correct': False,
                          'scenario_update': 'Fototerapi eşiğinin altındaki bebek gereksiz yere yatırıldı ve emzirme '
                                             'kesintiye uğradı.',
                          'teaching_point': 'Bilirubin eşiğin altında ve sodyum normalken yatış gerekmez; emzirme '
                                            'desteklenmelidir.'}]}]},
 {'id': 'Y94',
  'category': '👶 Yenidoğan Acilleri',
  'age': '3 Haftalık',
  'gender': 'Erkek',
  'complaint': 'Göbek kordonu düştükten sonra kurumayan, nemli kalan ve bezde lekelenme yapan göbek',
  'history': "Annesi anlatıyor: 'Göbeği 10. gün düştü. O günden beri hep ıslak, bezin üstünde sarımsı-pembe lekeler "
             "oluyor. İçinde kırmızı, et gibi küçük bir şey var.' Bebek iyi emiyor, kilo alıyor, ateşi yok. Göbekten "
             'idrar ya da dışkı geldiği fark edilmemiş. Annesi her gün alkollü pamukla silmiş. Göbek çevresinde '
             'kızarıklık veya kötü koku yok.',
  'final_diagnosis': 'Göbek (Umbilikal) Granülomu',
  'disposition': 'Gümüş Nitrat Koterizasyonu ve Bir Hafta Sonra Kontrolle Yeşil Alandan Taburculuk',
  'case_pearl': 'Kordon düştükten sonra göbek tabanında kalan, nemli, pembe-kırmızı, yumuşak, ağrısız doku göbek '
                'granülomudur ve en sık göbek sorunudur. Göbek çevresinde yayılan kızarıklık, sertlik ve kötü koku '
                'omfaliti, göbekten idrar gelmesi patent urakusu, dışkı veya safra gelmesi omfalomezenterik kanal '
                'kalıntısını düşündürür. Granülom gümüş nitrat koterizasyonu (çevre deri vazelinle korunarak) veya '
                'sofra tuzu uygulamasıyla tedavi edilir. 2-3 uygulamaya yanıt vermeyen veya parlak kırmızı, sert '
                'lezyonlar cerrahiye yönlendirilir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Göbeği kurumayan bu bebekte muayenede neye dikkat edersiniz?',
             'options': [{'text': 'Göbek çevresindeki deriyi kızarıklık, sertlik ve koku açısından değerlendirmek; '
                                  'göbek tabanındaki dokuyu incelemek ve akıntının niteliğini belirlemek',
                          'is_correct': True,
                          'explanation': 'Göbek çevresindeki yayılan kızarıklık enfeksiyonu, idrar veya dışkı akıntısı '
                                         'embriyolojik kanal kalıntılarını gösterir. Bu ayrım tedaviyi tamamen '
                                         'değiştirir.',
                          'new_finding': 'Ateş 36.8°C, genel durum iyi, tartı uygun artmış. Göbek tabanında 4 mm '
                                         'çaplı, nemli, pembe-kırmızı, yumuşak, granüler yüzeyli, saplı olmayan doku; '
                                         'dokunmakla ağrı yok, az miktarda seröz akıntı. Göbek çevresinde kızarıklık, '
                                         'sertlik ve koku yok. İdrar veya dışkı gelmiyor. Göbek fıtığı yok.'},
                         {'text': 'Göbek akıntısını enfeksiyon kabul edip muayene etmeden ağızdan antibiyotik başlamak '
                                  've göbeği günde birkaç kez alkolle silmeye devam etmek',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotiğe rağmen göbek nemli kalmaya devam etti; bebekte ishal '
                                             'gelişti.',
                          'teaching_point': 'Göbek çevresinde enfeksiyon bulgusu olmadan antibiyotik gerekmez; göbek '
                                            'tabanındaki doku muayene edilmelidir.'},
                         {'text': 'Göbekteki dokuyu tümör olarak değerlendirip muayeneyi kısa tutarak acil batın '
                                  'ultrasonografisi ve tomografi istemek',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografi normal geldi; tomografi gereksiz radyasyon yaratacağı '
                                             'için iptal edildi.',
                          'teaching_point': 'Bu yaşta göbekteki yumuşak, nemli doku sık görülen selim bir durumdur; '
                                            'görüntüleme ancak idrar veya dışkı gelmesi durumunda gerekir.'},
                         {'text': 'Ateş olmadığı için sepsis olasılığını dışlamak amacıyla tam kan sayımı ve CRP '
                                  'istemek, değerler normalse aileyi rahatlatıp göndermek',
                          'is_correct': False,
                          'scenario_update': 'Kan tetkikleri normal geldi; göbekteki sorun tedavi edilmeden bebek '
                                             'gönderildi.',
                          'teaching_point': 'Lokal ve sistemik enfeksiyon bulgusu olmayan bebekte kan tetkiki tanıya '
                                            'katkı sağlamaz.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Enfeksiyon bulgusu olmayan ve idrar-dışkı akıntısı bulunmayan bu bebekte hangi yaklaşım '
                         'uygundur?',
             'options': [{'text': 'Göbek akıntısından bakteri kültürü almak ve kültürde üreme olursa topikal ve '
                                  'sistemik antibiyotik planlamak',
                          'is_correct': False,
                          'scenario_update': 'Kültürde deri florası üredi ve gereksiz antibiyotik başlandı.',
                          'teaching_point': 'Kolonizasyonla enfeksiyon ayırt edilmelidir; enfeksiyon bulgusu yoksa '
                                            'kültür gerekmez.'},
                         {'text': 'Tetkik istemeden klinik tanıyla tedaviye geçmek; idrar veya dışkı akıntısı olsaydı '
                                  'ultrasonografi planlanacağını not etmek',
                          'is_correct': True,
                          'explanation': 'Tipik görünümde tanı kliniktir. Görüntüleme yalnızca kanal kalıntısını '
                                         'düşündüren akıntı veya tedaviye yanıtsızlık durumunda gerekir.',
                          'new_finding': 'Tetkik istenmedi. Lezyon tipik görünümde ve tek.'},
                         {'text': 'Göbekten kanala kontrast madde verip fistülografi istemek ve sonuca göre çocuk '
                                  'cerrahisi konsültasyonu planlamak',
                          'is_correct': False,
                          'scenario_update': 'Fistülografide kanal saptanmadı; girişim bebeği huzursuz etti.',
                          'teaching_point': 'Fistülografi yalnızca kanal kalıntısı şüphesinde düşünülür.'},
                         {'text': 'Göbek fıtığı olasılığına karşı ayakta direkt batın grafisi çekmek ve fıtık '
                                  'dışlanınca tedaviye karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Grafi normal geldi; fıtık muayeneyle zaten dışlanmıştı.',
                          'teaching_point': 'Göbek fıtığı muayeneyle tanınır; grafi gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Göbek granülomu',
                          'is_correct': True,
                          'explanation': 'Kordon düştükten sonra göbek tabanında kalan nemli, pembe, yumuşak, ağrısız '
                                         'doku ve enfeksiyon ya da kanal bulgusunun olmaması göbek granülomunu '
                                         'gösterir.',
                          'new_finding': 'Tanı: Göbek granülomu.'},
                         {'text': 'Omfalit (göbek çevresi enfeksiyonu)',
                          'is_correct': False,
                          'scenario_update': 'Göbek çevresinde kızarıklık, sertlik ve koku yoktu.',
                          'teaching_point': 'Omfalitte göbek çevresine yayılan eritem, ödem ve pürülan kötü kokulu '
                                            'akıntı olur.'},
                         {'text': 'Patent urakus',
                          'is_correct': False,
                          'scenario_update': 'Göbekten idrar gelmiyordu.',
                          'teaching_point': 'Patent urakusta göbekten berrak idrar sızar, ağlarken artar.'},
                         {'text': 'Umbilikal polip',
                          'is_correct': False,
                          'scenario_update': 'Lezyon yumuşak ve granüler yüzeyliydi, parlak kırmızı ve sert değildi.',
                          'teaching_point': 'Umbilikal polip parlak kırmızı, sert, mukozal bir dokudur ve '
                                            'koterizasyona yanıt vermez; cerrahi gerekir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu bebek için en uygun tedavi hangisidir?',
             'options': [{'text': 'Lezyonu ipek iple tabanından bağlamak için hemen çocuk cerrahisine yatış planlamak '
                                  've ameliyata kadar göbeği kapatmak',
                          'is_correct': False,
                          'scenario_update': 'Bebek gereksiz yere cerrahi süreç için bekletildi; basit bir poliklinik '
                                             'işlemi yeterliydi.',
                          'teaching_point': 'Granülomun ilk tedavisi koterizasyon veya tuz uygulamasıdır; cerrahi '
                                            'yalnız yanıtsız olgularda düşünülür.'},
                         {'text': 'Çevre deriyi vazelinle koruyup gümüş nitrat çubuğuyla koterize etmek, bölgeyi kuru '
                                  'tutmak ve bir hafta sonra kontrol etmek',
                          'is_correct': True,
                          'explanation': 'Gümüş nitrat granülomu kurutur. Çevre deri korunmazsa kimyasal yanık '
                                         'olabilir. Gerekirse işlem 2-3 kez haftalık tekrarlanır; yanıt yoksa cerrahi '
                                         'değerlendirme yapılır.',
                          'new_finding': 'Gümüş nitrat uygulandı. Bir hafta sonra granülom küçülmüş, ikinci uygulama '
                                         'sonrası göbek tamamen kurudu.'},
                         {'text': 'Göbek bölgesine iki hafta günde iki kez antibiyotikli ve kortikosteroidli krem '
                                  'sürmelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'Krem ile göbek daha da nemli kaldı ve granülom büyüdü.',
                          'teaching_point': 'Kremler nemli ortamı sürdürür ve granülomu tedavi etmez.'},
                         {'text': 'Göbeği günde beş kez alkollü pamukla silmeye devam etmelerini ve bebeği göbek '
                                  'tamamen kuruyana dek yıkamamalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Alkolle silme granülomu küçültmedi ve bebek bir ay boyunca yıkanmadı.',
                          'teaching_point': 'Alkol granülomu tedavi etmez; bebek normal şekilde yıkanabilir, göbek '
                                            'kurulanır.'}]}]},
 {'id': 'Y95',
  'category': '👶 Yenidoğan Acilleri',
  'age': '3 Günlük',
  'gender': 'Kız',
  'complaint': 'Dünden beri göğüs, sırt ve kollarda çıkan kırmızı lekeler ve ortalarında sarı-beyaz sivilceler',
  'history': "Ailesi çok endişeli: 'Dün göğsünde kırmızı lekeler çıktı, bugün sırtına ve kollarına yayıldı. "
             'Ortalarında sarı beyaz sivilceler var, iltihap mı diye korktuk. Bir yerde kayboluyor, başka yerde '
             "çıkıyor.' 40. haftada normal doğum, doğum ağırlığı 3500 g. Bebek iyi emiyor, ateşi yok, uykusu normal. "
             'Annenin genital uçuk öyküsü yok, doğumda erken su gelmesi veya ateş olmamış. Avuç içi ve ayak tabanında '
             'lezyon yok.',
  'final_diagnosis': 'Eritema Toksikum Neonatorum',
  'disposition': 'Aile Bilgilendirmesi ve Uyarı Bulgularıyla Yeşil Alandan Taburculuk',
  'case_pearl': 'Eritema toksikum neonatorum term yenidoğanların yaklaşık yarısında ilk 1-3 günde başlayan, kırmızı '
                'makül ve ortasında sarı-beyaz papül veya püstüllerden oluşan, yeri değişen zararsız bir döküntüdür. '
                'Avuç içi ve ayak tabanı tutulmaz. Bebek iyi görünür. Kuşkuda püstül içeriğinin yaymasında '
                'eozinofiller görülür. Gruplaşmış veziküller, letarji veya ateş neonatal HSV enfeksiyonunu, yaymada '
                'nötrofil ve gram pozitif kok stafilokoksik püstülozu düşündürür. Tedavi gerekmez, 1-2 haftada '
                'kendiliğinden geçer.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Döküntüsü olan 3 günlük bu bebekte ilk değerlendirmeniz nedir?',
             'options': [{'text': 'Genel görünümü, ateşi, beslenmeyi ve hidrasyonu değerlendirip döküntünün '
                                  'dağılımını, lezyon tipini ve avuç içi-taban tutulumunu incelemek',
                          'is_correct': True,
                          'explanation': 'Yenidoğanda döküntünün zararsız mı ciddi mi olduğu genel görünüm, ateş, '
                                         'beslenme ve lezyonların niteliğine göre ayırt edilir. Gruplaşmış veziküller '
                                         'ayrıca aranmalıdır.',
                          'new_finding': 'Ateş 36.9°C, KTA 138/dk, SS 42/dk, KDZ 2 sn. Bebek uyanık, canlı, iyi '
                                         'emiyor. Göğüs, sırt, uyluk ve kollarda 1-3 cm çaplı, düzensiz sınırlı '
                                         'eritemli maküller; çoğunun ortasında 1-2 mm sarı-beyaz papül veya püstül. '
                                         'Gruplaşmış vezikül, erozyon veya kabuk yok. Avuç içi ve ayak tabanı temiz. '
                                         'Ağız içi ve gözler normal. Göbek temiz.'},
                         {'text': 'Püstüller nedeniyle bebeği hemen yenidoğan yoğun bakıma yatırıp kan kültürü, lomber '
                                  'ponksiyon ve ampirik antibiyotik ile asiklovir başlatmak',
                          'is_correct': False,
                          'scenario_update': 'İyi görünen bebek invaziv girişimler geçirdi ve anneden ayrıldı; tüm '
                                             'kültürler negatif geldi.',
                          'teaching_point': 'İyi görünen, ateşsiz ve tipik lezyonlu bebekte sepsis taraması gerekmez; '
                                            'önce lezyonların niteliği değerlendirilmelidir.'},
                         {'text': 'Döküntüyü annenin kullandığı kremlere ve deterjana bağlayıp muayene etmeden aileye '
                                  'çamaşır deterjanını değiştirmelerini söylemek',
                          'is_correct': False,
                          'scenario_update': 'Deterjan değiştirildi; bebeğin genel durumu ve lezyonları '
                                             'değerlendirilmeden gönderildi.',
                          'teaching_point': 'Yenidoğanda döküntü muayene edilmeden değerlendirilemez; ciddi '
                                            'enfeksiyonlar atlanabilir.'},
                         {'text': 'Püstülleri iğneyle açıp içini boşaltmak ve bölgeleri antiseptik solüsyonla silmek, '
                                  'ardından bebeği muayene etmek',
                          'is_correct': False,
                          'scenario_update': 'İşlem bebeği çok rahatsız etti ve deride gereksiz yaralar oluştu.',
                          'teaching_point': 'Lezyonlar boşaltılmaz; tanı için gerekirse yalnızca yayma amacıyla içerik '
                                            'alınabilir.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Genel durumu iyi olan bu bebekte ailenin kaygısını gidermek için hangi yaklaşım uygundur?',
             'options': [{'text': 'Tam kan sayımı, CRP ve kan kültürü istemek ve sonuçlar normal gelene kadar bebeği '
                                  'gözlemde tutmak',
                          'is_correct': False,
                          'scenario_update': 'Sonuçlar normal geldi; bebek gereksiz kan alımı ve uzun bekleme yaşadı.',
                          'teaching_point': 'İyi görünen bebekte tipik döküntü için kan tetkiki gerekmez.'},
                         {'text': 'Tipik görünümde tetkik gerekmediğini açıklamak; kuşku duyulursa bir püstül '
                                  'içeriğinden yayma yapıp hücre tipini incelemek',
                          'is_correct': True,
                          'explanation': 'Tanı genellikle kliniktir. Yaymada eozinofil baskınlığı tanıyı doğrular ve '
                                         'aileyi rahatlatır; nötrofil ve bakteri görülmesi farklı bir tanıya işaret '
                                         'eder.',
                          'new_finding': 'Ailenin isteğiyle bir püstülden alınan yaymada bol eozinofil görüldü, '
                                         'nötrofil ve bakteri yoktu.'},
                         {'text': 'Lezyonlardan virüs PCR çalışmak ve sonuç gelene kadar bebeği izole ederek annenin '
                                  'emzirmesini durdurmak',
                          'is_correct': False,
                          'scenario_update': 'PCR negatif geldi; emzirme gereksiz yere kesildi.',
                          'teaching_point': 'Gruplaşmış vezikül ve risk faktörü olmayan iyi görünen bebekte bu '
                                            'yaklaşım gereksizdir.'},
                         {'text': 'Deri biyopsisi için dermatolojiye yönlendirmek ve biyopsi sonucu gelene dek bebeği '
                                  'yıkamamalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Biyopsi gereksiz bir girişim oldu ve sonucu çıkmadan döküntü '
                                             'kendiliğinden geriledi.',
                          'teaching_point': 'Tipik yenidoğan döküntülerinde biyopsi gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Neonatal herpes simpleks deri enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Gruplaşmış vezikül yoktu, bebek iyi görünüyordu ve yaymada eozinofil '
                                             'vardı.',
                          'teaching_point': "Neonatal HSV'de eritemli zemin üzerinde gruplaşmış veziküller ve sıklıkla "
                                            '1-3. haftada başlangıç görülür.'},
                         {'text': 'Stafilokoksik püstüloz',
                          'is_correct': False,
                          'scenario_update': 'Yaymada nötrofil ve bakteri görülmedi.',
                          'teaching_point': 'Stafilokoksik püstülozda püstüller daha çok kıvrım yerlerinde ve bez '
                                            'bölgesindedir, yaymada nötrofil ve gram pozitif kok görülür.'},
                         {'text': 'Geçici neonatal püstüler melanozis',
                          'is_correct': False,
                          'scenario_update': 'Lezyonlar doğumda yoktu ve kırmızı zemin üzerindeydi.',
                          'teaching_point': 'Püstüler melanozis doğumda vardır, eritemsizdir ve hiperpigmente maküller '
                                            'bırakır.'},
                         {'text': 'Eritema toksikum neonatorum',
                          'is_correct': True,
                          'explanation': 'İyi görünen term bebekte ilk günlerde başlayan, yeri değişen eritemli '
                                         'maküller ve ortalarında sarı-beyaz papül-püstüller, avuç içi-taban '
                                         'tutulmaması ve yaymada eozinofil eritema toksikum neonatorumu gösterir.',
                          'new_finding': 'Tanı: Eritema toksikum neonatorum.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu aileye hangi öneriler verilmelidir?',
             'options': [{'text': 'Zararsız olduğunu ve 1-2 haftada kendiliğinden geçeceğini açıklamak, krem '
                                  'gerekmediğini söylemek; ateş, beslenme sorunu veya vezikül olursa başvurmalarını '
                                  'önermek',
                          'is_correct': True,
                          'explanation': 'Tedavi gerekmez. Aileye zararsız seyrin anlatılması ve gerçek uyarı '
                                         'bulgularının öğretilmesi gereksiz başvuruları azaltır.',
                          'new_finding': 'Aile bilgilendirildi. Kontrolde döküntü 10. günde tamamen kaybolmuştu; bebek '
                                         'iyi kilo alıyordu.'},
                         {'text': 'Olası bir enfeksiyona karşı lezyonlara günde üç kez mupirosin krem sürmelerini ve '
                                  'bebeği iki hafta yıkamamalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Krem gereksiz yere kullanıldı ve yıkanmayan bebekte pişik gelişti.',
                          'teaching_point': 'Bu döküntü enfeksiyon değildir; topikal antibiyotik gerekmez, normal '
                                            'bakım sürdürülür.'},
                         {'text': 'Ampirik oral asiklovir başlamak ve tedavi süresince bebeği diğer çocuklardan ayrı '
                                  'tutmalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Asiklovir gereksiz yere verildi ve böbrek fonksiyonu izlemi gerekti.',
                          'teaching_point': 'HSV bulgusu olmayan bebekte antiviral endikasyonu yoktur.'},
                         {'text': 'Döküntünün inek sütü alerjisi olabileceğini söyleyip annenin diyetinden süt '
                                  'ürünlerini çıkarmasını ve bebeğe hidrolize mama başlamasını önermek',
                          'is_correct': False,
                          'scenario_update': 'Anne süt ürünlerini kesti ve emzirme azaldı; döküntü diyetten bağımsız '
                                             'olarak kendiliğinden geçti.',
                          'teaching_point': 'Bu döküntü besin alerjisiyle ilişkili değildir; diyet değişikliği '
                                            'gerekmez.'}]}]},
 {'id': 'Y96',
  'category': '👁️ Göz Şikayetleri',
  'age': '7 Yaşında',
  'gender': 'Erkek',
  'complaint': 'İki gündür sağ üst göz kapağının kenarında ağrılı şişlik ve kızarıklık',
  'history': "Annesi anlatıyor: 'Dün sabah göz kapağının kenarında küçük, kırmızı, ağrılı bir şişlik çıktı. Bugün "
             "biraz büyüdü, üstünde sarı bir nokta oluştu. Gözünü sık sık ovuşturuyor.' Ateş yok. Görmede bulanıklık, "
             'gözü hareket ettirirken ağrı yok. Gözde çapaklanma az. Daha önce benzer bir şişlik olmamış. Son günlerde '
             'nezle geçirmemiş. Aşıları tam.',
  'final_diagnosis': 'Eksternal Hordeolum (Arpacık)',
  'disposition': 'Sıcak Kompres ve Kapak Hijyeni Önerisiyle Yeşil Alandan Taburculuk',
  'case_pearl': 'Hordeolum, kapak kenarındaki bezlerin (Zeis/Moll: eksternal, Meibom: internal) akut, ağrılı, '
                'çoğunlukla stafilokoksik enfeksiyonudur. Tedavi günde 3-4 kez 10-15 dakika sıcak kompres ve kapak '
                'hijyenidir; sıkılmaz. Rutin sistemik antibiyotik gerekmez. Ağrısız, kapak içinde kalıcı lastik '
                'kıvamında nodül şalazyondur. Kapak ödemi yaygınlaşırsa preseptal selülit, göz hareketlerinde ağrı, '
                'proptozis veya görme kaybı orbital selülit düşündürür ve acil değerlendirme gerektirir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Göz kapağında ağrılı şişliği olan bu çocukta muayenede öncelikle neyi değerlendirirsiniz?',
             'options': [{'text': 'Görme keskinliği, göz hareketleri ve ağrısını, proptozisi ve kapak ödeminin '
                                  'yaygınlığını değerlendirmek; lezyonun yerini ve kıvamını incelemek',
                          'is_correct': True,
                          'explanation': 'Kapak şişliğinde ilk hedef orbital tutulumu dışlamaktır. Lezyonun kapak '
                                         'kenarında sınırlı olması ve kıvamı ayırıcı tanıyı belirler.',
                          'new_finding': 'Ateş 36.8°C. Görme keskinliği iki gözde 10/10, göz hareketleri serbest ve '
                                         'ağrısız, proptozis yok. Sağ üst kapak kenarında kirpik dibinde 4 mm çaplı, '
                                         'kızarık, hassas, ortasında sarı püstül olan nodül. Kapak ödemi lezyon '
                                         'çevresinde sınırlı, periorbital deride yayılan kızarıklık yok. Konjonktiva '
                                         'hafif hiperemik.'},
                         {'text': 'Püstülü görür görmez steril iğneyle açıp içeriğini sıkarak boşaltmak ve ardından '
                                  'gözü antibiyotikli pomadla kapamak',
                          'is_correct': False,
                          'scenario_update': 'Sıkma sonrası kapakta ödem ve kızarıklık arttı; çocuk ertesi gün yaygın '
                                             'kapak şişliğiyle getirildi.',
                          'teaching_point': 'Kapak lezyonları sıkılmaz; enfeksiyon çevre dokulara yayılabilir.'},
                         {'text': 'Orbital tutulum olasılığına karşı muayeneyi kısa tutup hemen kontrastlı orbita '
                                  'tomografisi istemek ve göz konsültasyonu beklemek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi normal geldi; çocuk gereksiz radyasyon ve kontrast maddeye '
                                             'maruz kaldı.',
                          'teaching_point': 'Görme, göz hareketleri ve proptozis normalse görüntüleme gerekmez; tanı '
                                            'muayeneyle konur.'},
                         {'text': 'Kızarıklık nedeniyle viral konjonktivit kabul edip muayene etmeden suni gözyaşı '
                                  'vermek ve okuldan bir hafta uzak tutmak',
                          'is_correct': False,
                          'scenario_update': 'Kapaktaki lezyon değerlendirilmedi; çocuk okuldan gereksiz yere uzak '
                                             'kaldı.',
                          'teaching_point': 'Kapak kenarındaki ağrılı nodül konjonktivitten ayrı bir durumdur; muayene '
                                            'şarttır.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Orbital tutulum bulgusu olmayan bu çocukta hangi yaklaşım uygundur?',
             'options': [{'text': 'Tam kan sayımı ve CRP istemek; lökositoz varsa ağızdan antibiyotik başlayıp üç gün '
                                  'sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Kan değerleri normal geldi; çocuk gereksiz kan alımı yaşadı.',
                          'teaching_point': 'Sınırlı kapak lezyonunda kan tetkiki tanı veya tedaviye katkı sağlamaz.'},
                         {'text': 'Püstül içeriğinden bakteri kültürü almak ve duyarlılık sonucuna göre topikal '
                                  'antibiyotiği seçmek için sonucu beklemek',
                          'is_correct': False,
                          'scenario_update': 'Kültürde deri florası üredi; sonuç tedaviyi değiştirmedi.',
                          'teaching_point': 'Tipik kapak lezyonunda kültür gerekmez.'},
                         {'text': 'Tetkik istememek; tanının muayeneyle konduğunu açıklamak ve yayılma bulgusu olursa '
                                  'yeniden değerlendirmeyi planlamak',
                          'is_correct': True,
                          'explanation': 'Kapak kenarında sınırlı, ağrılı, püstüllü lezyonda tanı kliniktir. Tetkik '
                                         'ancak yayılma veya sistemik bulgu olursa gerekir.',
                          'new_finding': 'Tetkik istenmedi. Lezyon tek, kapak kenarında ve kirpik dibinde.'},
                         {'text': 'Kapak lezyonunun derinliğini görmek için orbita ultrasonografisi istemek ve sonuca '
                                  'göre tedavi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografi yalnızca yüzeyel bir lezyon gösterdi ve yönetimi '
                                             'değiştirmedi.',
                          'teaching_point': 'Yüzeyel kapak lezyonları görüntüleme gerektirmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Şalazyon (meibom bezi kisti)',
                          'is_correct': False,
                          'scenario_update': 'Lezyon akut, ağrılı ve kapak kenarında püstüllüydü.',
                          'teaching_point': 'Şalazyon kapak içinde, ağrısız, lastik kıvamında ve haftalarca süren bir '
                                            'nodüldür.'},
                         {'text': 'Preseptal (periorbital) selülit',
                          'is_correct': False,
                          'scenario_update': 'Kapak ödemi lezyon çevresinde sınırlıydı, yaygın kızarıklık yoktu.',
                          'teaching_point': 'Preseptal selülitte kapağın tamamında ödem ve eritem olur.'},
                         {'text': 'Eksternal hordeolum (arpacık)',
                          'is_correct': True,
                          'explanation': 'Kirpik dibinde akut başlayan, ağrılı, kızarık, ortasında püstül olan sınırlı '
                                         'nodül ve orbital bulgu olmaması eksternal hordeolumu gösterir.',
                          'new_finding': 'Tanı: Eksternal hordeolum.'},
                         {'text': 'Akut dakriyosistit',
                          'is_correct': False,
                          'scenario_update': 'Şişlik iç kantusta değil, kapak kenarındaydı.',
                          'teaching_point': 'Dakriyosistitte iç kantusta, gözyaşı kesesi üzerinde ağrılı şişlik '
                                            'olur.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Günde 3-4 kez 10-15 dakika sıcak kompres, kapak kenarını bebek şampuanıyla '
                                  'temizleme ve ovuşturmamayı önermek',
                          'is_correct': True,
                          'explanation': 'Sıcak kompres bezin drenajını hızlandırır ve çoğu lezyon bir hafta içinde '
                                         'kendiliğinden boşalıp geçer. Kapak hijyeni tekrarı azaltır.',
                          'new_finding': 'Sıcak kompres önerildi. Üç gün sonra lezyon kendiliğinden boşalmış, bir '
                                         'haftada tamamen geçmişti.'},
                         {'text': 'Yedi gün ağızdan amoksisilin-klavulanat ve topikal kortikosteroidli göz damlası '
                                  'başlamak, iki gün sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik ishal yaptı; steroid damla gereksiz yere göz içi basınç '
                                             'riskine yol açtı.',
                          'teaching_point': 'Sınırlı lezyonda sistemik antibiyotik gerekmez; steroid damla göz doktoru '
                                            'önerisi olmadan verilmez.'},
                         {'text': 'Lezyonun cerrahi olarak boşaltılması için ertesi gün göz hastalıkları polikliniğine '
                                  'ameliyat randevusu vermek',
                          'is_correct': False,
                          'scenario_update': 'Lezyon randevu tarihinden önce kendiliğinden boşaldı; girişim '
                                             'gereksizdi.',
                          'teaching_point': 'Cerrahi drenaj yalnızca kompresle geçmeyen veya şalazyona dönüşen '
                                            'lezyonlarda düşünülür.'},
                         {'text': 'Soğuk buz uygulaması yapmalarını, lezyonu her gün bastırarak içini boşaltmalarını '
                                  've okuldan bir hafta uzak durmasını önermek',
                          'is_correct': False,
                          'scenario_update': 'Bastırma sonrası kapakta yaygın şişlik ve kızarıklık gelişti.',
                          'teaching_point': 'Soğuk değil sıcak kompres önerilir; lezyon bastırılmaz, okul kısıtlaması '
                                            'gerekmez.'}]}]},
 {'id': 'Y97',
  'category': '👂 Kulak Ağrısı & KBB',
  'age': '3 Yaşında',
  'gender': 'Kız',
  'complaint': 'Dün gece şiddetli kulak ağrısından sonra bu sabah sol kulaktan sarı akıntı gelmesi',
  'history': "Annesi anlatıyor: 'Üç gündür burnu akıyordu. Dün gece kulağını tutup saatlerce ağladı, ateşi 38.9 oldu. "
             "Sabaha karşı birden rahatladı, uyudu. Uyandığında yastığında sarı, yapışkan akıntı vardı.' Kulağına bir "
             'şey sokulmamış, havuza girmemiş. Daha önce kulak akıntısı olmamış. Aşıları tam. Kulak arkasında şişlik '
             'fark edilmemiş.',
  'final_diagnosis': 'Timpanik Membran Perforasyonlu Akut Otitis Media (Otore)',
  'disposition': 'Yüksek Doz Oral Amoksisilin, Kulağı Kuru Tutma Önerisi ve 2-3 Hafta Sonra Kulak Kontrolüyle Yeşil '
                 'Alandan Taburculuk',
  'case_pearl': 'Akut otitis mediada orta kulakta biriken pürülan sıvının basıncı zarı yırtabilir; ağrının aniden '
                'azalmasının ardından akıntı başlaması tipiktir. Kulak kanalı ağrısız ve kulak kepçesi çekme ile '
                'hassas değilse kaynak orta kulaktır. Tedavi yüksek doz oral amoksisilindir (80-90 mg/kg/gün). Topikal '
                'kinolon damlası eklenebilir; aminoglikozitli damlalar perfore zarda ototoksik olabileceği için '
                'kullanılmaz. Kulak kuru tutulur. Perforasyonların çoğu 2-6 haftada kapanır; kontrol muayenesi zarın '
                'kapandığını doğrulamak için gereklidir. Kulak arkası şişlik ve kulak kepçesinin öne itilmesi '
                'mastoiditi düşündürür.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Kulak ağrısı geçtikten sonra akıntısı başlayan bu çocukta muayenede neyi değerlendirirsiniz?',
             'options': [{'text': 'Kulak arkasını şişlik ve hassasiyet açısından incelemek, kulak kepçesini çekerek '
                                  'ağrıyı değerlendirmek, kanalı temizleyip zarı görmeye çalışmak',
                          'is_correct': True,
                          'explanation': 'Kulak kepçesini çekmekle ağrı dış kulak yolu kaynaklı akıntıyı, kulak arkası '
                                         'bulguları komplikasyonu gösterir. Akıntı silinince zar değerlendirilebilir.',
                          'new_finding': 'Ateş 37.9°C, genel durum iyi. Sol kulak yolunda kokusuz, sarı mukopürülan '
                                         'akıntı; kepçe çekilince ağrı yok, kanal derisi ödemsiz. Akıntı silindikten '
                                         'sonra zarın arka-alt kadranında küçük delik ve pulsatil akıntı görülüyor. '
                                         'Sağ zar bombe ve hiperemik. Kulak arkası normal, kepçe öne itilmemiş. Boyun '
                                         'hareketleri serbest.'},
                         {'text': 'Akıntıyı dış kulak yolu enfeksiyonu kabul edip kulağı muayene etmeden antibiyotikli '
                                  've kortikosteroidli kulak damlası yazmak',
                          'is_correct': False,
                          'scenario_update': 'Orta kulaktaki enfeksiyon tedavi edilmedi; ateş sürdü ve iki gün sonra '
                                             'tekrar başvurdu.',
                          'teaching_point': 'Akıntının kaynağı muayeneyle belirlenmelidir; orta kulak kaynaklı akıntı '
                                            'sistemik tedavi gerektirir.'},
                         {'text': 'Akıntıyı kulak yolundan basınçlı su ile yıkayarak temizlemek ve zarı daha iyi '
                                  'görmek için işlemi birkaç kez tekrarlamak',
                          'is_correct': False,
                          'scenario_update': 'Yıkama sırasında çocuk şiddetli ağrı ve baş dönmesi yaşadı; orta kulağa '
                                             'su kaçtı.',
                          'teaching_point': 'Zar bütünlüğü bilinmeyen kulakta su ile yıkama yapılmaz; akıntı kuru '
                                            'pamukla silinir.'},
                         {'text': 'Akıntının beyin omurilik sıvısı olabileceğini düşünüp çocuğu hemen sarı alana '
                                  'alarak beyin tomografisi istemek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi normal geldi; travma ve nörolojik bulgu olmayan çocukta '
                                             'gereksizdi.',
                          'teaching_point': 'Travma öyküsü olmadan, enfeksiyon tablosunda gelen kulak akıntısında BOS '
                                            'kaçağı düşünülmez.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Kulak arkası normal, genel durumu iyi olan bu çocukta hangi yaklaşım uygundur?',
             'options': [{'text': 'Mastoiditi dışlamak için temporal kemik tomografisi istemek ve sonuç gelene kadar '
                                  'intravenöz antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'Tomografi normal geldi; çocuk gereksiz radyasyon ve damar yolu girişimi '
                                             'yaşadı.',
                          'teaching_point': 'Kulak arkası bulgusu yoksa görüntüleme gerekmez.'},
                         {'text': 'Tetkik istememek; tanıyı otoskopik bulgulara dayandırmak ve akıntı tedaviye rağmen '
                                  'sürerse kültür planlamak',
                          'is_correct': True,
                          'explanation': 'İlk atakta tanı kliniktir. Kültür, tedaviye rağmen 7-10 günden uzun süren '
                                         'veya tekrarlayan akıntıda istenir.',
                          'new_finding': "Tetkik istenmedi. Ateş antipiretikle 37.2°C'ye düştü, çocuk oyun oynuyor."},
                         {'text': 'Tam kan sayımı, CRP ve kan kültürü göndermek; değerler yüksekse çocuğu servise '
                                  'yatırmak',
                          'is_correct': False,
                          'scenario_update': 'CRP hafif yüksek geldi ve iyi görünen çocuk gereksiz yere yatırıldı.',
                          'teaching_point': 'Komplike olmayan orta kulak enfeksiyonunda kan tetkiki gerekmez.'},
                         {'text': 'Odyometri ve timpanometri istemek, işitme kaybı derecesine göre tedavi planını '
                                  'belirlemek',
                          'is_correct': False,
                          'scenario_update': 'Akut dönemde yapılan testler güvenilir olmadı ve tedaviyi geciktirdi.',
                          'teaching_point': 'İşitme değerlendirmesi akut dönemde değil, iyileşme sonrası kontrolde '
                                            'yapılır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Akut otitis eksterna',
                          'is_correct': False,
                          'scenario_update': 'Kepçe çekilince ağrı yoktu ve kanal derisi ödemsizdi.',
                          'teaching_point': 'Otitis eksternada kepçe çekme ve tragus basısıyla ağrı, kanal ödemi '
                                            'belirgindir.'},
                         {'text': 'Akut mastoidit',
                          'is_correct': False,
                          'scenario_update': 'Kulak arkasında şişlik, kızarıklık ve kepçe yer değişikliği yoktu.',
                          'teaching_point': 'Mastoiditte kulak arkası hassas, şiş ve kepçe öne-aşağı itilmiştir.'},
                         {'text': 'Edinsel kolesteatom',
                          'is_correct': False,
                          'scenario_update': 'Akut başlangıçlı ve ilk akıntıydı, kötü koku yoktu.',
                          'teaching_point': 'Kolesteatomda kronik, kötü kokulu, ağrısız akıntı ve zarda beyaz kitle '
                                            'görülür.'},
                         {'text': 'Zar perforasyonlu akut otitis media',
                          'is_correct': True,
                          'explanation': 'Üst solunum yolu enfeksiyonu sonrası şiddetli ağrı ve ateş, ağrının aniden '
                                         'geçip mukopürülan akıntı başlaması, zarda delik ve karşı kulakta bombe zar '
                                         'perforasyonlu akut otitis mediayı gösterir.',
                          'new_finding': 'Tanı: Timpanik membran perforasyonlu akut otitis media.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Akıntı kendiliğinden geçeceği için antibiyotik vermemek ve kulağı her gün su ile '
                                  'yıkayıp ardından kulak çubuğuyla kurulamalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Yıkama sonrası akıntı arttı ve enfeksiyon sürdü.',
                          'teaching_point': 'Perfore zarda kulak kuru tutulur; bu yaşta ve bilateral tutulumda '
                                            'antibiyotik önerilir.'},
                         {'text': 'Gentamisinli kulak damlasını günde dört kez damlatmak ve oral antibiyotik vermeden '
                                  'akıntının geçmesini beklemek',
                          'is_correct': False,
                          'scenario_update': 'Aminoglikozitli damla perfore zardan orta kulağa geçti; ototoksisite '
                                             'riski oluştu.',
                          'teaching_point': 'Perfore zarda aminoglikozitli damlalar kullanılmaz; güvenli seçenek '
                                            'kinolon damlalardır.'},
                         {'text': 'Yüksek doz oral amoksisilin, analjezi ve kulağı kuru tutmayı önermek; zarın '
                                  'kapanması için 2-3 hafta sonra kontrol planlamak',
                          'is_correct': True,
                          'explanation': 'Yüksek doz amoksisilin pnömokok direncini aşar. Kulağın kuru tutulması '
                                         'iyileşmeyi destekler. Kontrol muayenesinde zarın kapanması ve işitme '
                                         'değerlendirilir.',
                          'new_finding': 'Amoksisilin 90 mg/kg/gün ve ibuprofen başlandı. Akıntı üç günde kesildi; üç '
                                         'hafta sonraki kontrolde zar kapanmıştı.'},
                         {'text': 'İntravenöz seftriakson için servise yatırmak ve zar onarımı için kulak burun boğaz '
                                  'servisinde ameliyat planlamak',
                          'is_correct': False,
                          'scenario_update': 'İyi görünen çocuk gereksiz yere yatırıldı; perforasyon kendiliğinden '
                                             'kapandı.',
                          'teaching_point': 'Komplike olmayan perforasyon ayaktan tedavi edilir; çoğu birkaç haftada '
                                            'kendiliğinden kapanır.'}]}]},
 {'id': 'Y98',
  'category': '🫁 Hırıltı & Solunum Sıkıntısı',
  'age': '7 Aylık (8.2 kg)',
  'gender': 'Erkek',
  'complaint': 'Üç gündür burun akıntısı, iki gündür öksürük ve göğüsten hırıltı sesi',
  'history': "Annesi anlatıyor: 'Ablası kreşten nezle getirdi. Üç gündür burnu akıyor, iki gündür öksürüyor, göğsünden "
             'hırıltı geliyor. Burnu tıkalıyken emerken biraz zorlanıyor ama yine de her seferinde biberonunun çoğunu '
             "bitiriyor. Altı bez ıslattı.' Ateşi 37.8°C olmuş. Daha önce hırıltı atağı yok. Term doğmuş, kalp "
             'hastalığı yok. Evde sigara içiliyor. Morarma, nefes durması olmamış.',
  'final_diagnosis': 'Hafif Akut Bronşiolit (Evde İzlenebilir)',
  'disposition': 'Nazal Lavaj, Destek Tedavisi, Uyarı Bulguları Eğitimi ve 24-48 Saat Sonra Kontrolle Yeşil Alandan '
                 'Taburculuk',
  'case_pearl': 'Bronşiolit klinik bir tanıdır: iki yaş altında viral üst solunum yolu belirtilerini izleyen öksürük, '
                'takipne, raller ve hışıltı. Hafif olguda (SpO2 ≥%92, hafif çekilme, beslenme normalin yarısından '
                'fazla) evde destek tedavisi yeterlidir. Rutin akciğer grafisi, kan tetkiki, viral test, salbutamol, '
                'kortikosteroid, nebülize adrenalin ve antibiyotik önerilmez. Burun temizliği ve sık-az beslenme '
                'önerilir. Hastalık 3-5. günde en ağır hale gelebileceği için aileye uyarı bulguları (inleme, belirgin '
                'çekilme, beslenmenin yarıya düşmesi, apne, morarma) öğretilir. Evde sigara içilmemesi önemlidir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Hırıltısı olan bu süt çocuğunda ilk değerlendirmeniz nedir?',
             'options': [{'text': "Burun temizlendikten sonra solunum sayısı, çekilmeler, inleme ve SpO2'yi "
                                  'değerlendirmek; beslenme miktarını ve ıslak bez sayısını sorgulamak',
                          'is_correct': True,
                          'explanation': 'Hastalığın şiddeti solunum işi, oksijenlenme ve beslenme ile belirlenir. '
                                         'Burun tıkanıklığı sayımları yanıltabileceği için değerlendirme burun '
                                         'temizliğinden sonra yapılmalıdır.',
                          'new_finding': 'Ateş 37.7°C, KTA 132/dk, SS 46/dk, SpO2 %97 (oda havası), KDZ 2 sn. Burun '
                                         'aspirasyonu sonrası bebek sakin, inleme ve burun kanadı solunumu yok, hafif '
                                         'subkostal çekilme. Dinlemekle iki tarafta yaygın ince raller ve ekspiratuvar '
                                         'hışıltı. Mukozalar nemli. Biberonu muayene sırasında rahatça emdi.'},
                         {'text': 'Hışıltı nedeniyle muayene yapmadan hemen salbutamol nebül başlamak ve ilk dozdan '
                                  'sonra yanıtı değerlendirmek',
                          'is_correct': False,
                          'scenario_update': "Salbutamol sonrası kalp hızı 175/dk'ya çıktı, bebek huzursuzlandı; "
                                             'solunumunda değişiklik olmadı.',
                          'teaching_point': 'Bu yaş grubundaki viral alt solunum yolu tablosunda bronkodilatörler '
                                            'rutin olarak önerilmez.'},
                         {'text': 'Hışıltının yabancı cisim kaynaklı olabileceğini düşünerek muayeneyi kısa tutup acil '
                                  'bronkoskopi için konsültasyon istemek',
                          'is_correct': False,
                          'scenario_update': 'Bilateral bulgular ve nezle öyküsü olan bebekte gereksiz konsültasyon '
                                             'istendi.',
                          'teaching_point': 'Yabancı cisim ani boğulma öyküsü ve tek taraflı bulgularla gelir; bu '
                                            'tabloda düşünülmez.'},
                         {'text': 'Bebeği değerlendirmeden hemen sarı alana alıp damar yolu açmak, intravenöz sıvı '
                                  'başlamak ve yüz maskesiyle oksijen vermek',
                          'is_correct': False,
                          'scenario_update': 'Oksijen ihtiyacı ve dehidratasyonu olmayan bebek gereksiz girişimler '
                                             'yaşadı.',
                          'teaching_point': "Tedavi şiddet değerlendirmesine göre seçilir; iyi beslenen ve SpO2'si "
                                            'normal bebekte girişim gerekmez.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': "SpO2'si %97, beslenmesi korunmuş bu bebekte hangi tetkik yaklaşımı uygundur?",
             'options': [{'text': 'Akciğer grafisi çekmek ve bakteriyel enfeksiyonu dışlamak için tam kan sayımı ve '
                                  'CRP istemek',
                          'is_correct': False,
                          'scenario_update': 'Grafide peribronşiyal kalınlaşma ve atelektazi alanı görüldü, gereksiz '
                                             'antibiyotik başlandı.',
                          'teaching_point': 'Tipik hafif tabloda grafi atelektaziyi pnömoni gibi gösterebilir ve '
                                            'gereksiz antibiyotiğe yol açar.'},
                         {'text': 'Nazofaringeal sürüntüden solunum yolu virüs panelini çalışmak ve sonuca göre izlem '
                                  'planını belirlemek',
                          'is_correct': False,
                          'scenario_update': 'Test sonucu iki gün sonra geldi ve yönetimi değiştirmedi.',
                          'teaching_point': 'Viral etken tespiti hafif ayaktan hastada tedaviyi değiştirmez.'},
                         {'text': 'Tetkik istememek; tanıyı öykü ve muayeneye dayandırmak ve gerekirse beslenme '
                                  "sonrası SpO2'yi yeniden ölçmek",
                          'is_correct': True,
                          'explanation': 'Tanı kliniktir. Hafif olguda tetkikler yönetimi değiştirmez; gereksiz '
                                         'tedaviye ve yatışa yol açabilir.',
                          'new_finding': 'Beslenme sonrası tekrar ölçümde SpO2 %96, SS 44/dk. Bebek ağız yoluyla rahat '
                                         'besleniyor.'},
                         {'text': 'Kan gazı ve elektrolitleri ölçmek, değerler normalse aileyi rahatlatıp göndermek',
                          'is_correct': False,
                          'scenario_update': 'Kan gazı normal geldi; işlem bebeği ağlattı ve solunumunu geçici olarak '
                                             'zorlaştırdı.',
                          'teaching_point': 'Oksijenlenmesi normal ve iyi görünen bebekte kan gazı gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Toplum kökenli bakteriyel pnömoni',
                          'is_correct': False,
                          'scenario_update': 'Ateş düşük, bulgular yaygın ve bilateral, genel durum iyiydi.',
                          'teaching_point': 'Bakteriyel pnömonide yüksek ateş, lokal bulgular ve toksik görünüm daha '
                                            'olasıdır.'},
                         {'text': 'Hafif akut bronşiolit',
                          'is_correct': True,
                          'explanation': 'İki yaş altında viral nezleyi izleyen öksürük, yaygın raller ve hışıltı, '
                                         'normal SpO2, hafif çekilme ve korunmuş beslenme hafif akut bronşioliti '
                                         'gösterir.',
                          'new_finding': 'Tanı: Hafif akut bronşiolit.'},
                         {'text': 'İlk astım atağı',
                          'is_correct': False,
                          'scenario_update': 'Yaşı küçük, ilk hırıltı atağıydı ve yaygın ince raller vardı.',
                          'teaching_point': 'Bir yaş altında ilk viral hırıltı atağı astım olarak değerlendirilmez.'},
                         {'text': 'Konjenital kalp hastalığına bağlı kalp yetersizliği',
                          'is_correct': False,
                          'scenario_update': 'Üfürüm, hepatomegali ve kilo alma sorunu yoktu.',
                          'teaching_point': 'Kalp yetersizliğinde beslenirken terleme, hepatomegali ve kilo alamama '
                                            'görülür.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu bebek için en uygun taburculuk planı hangisidir?',
             'options': [{'text': 'Evde günde üç kez salbutamol ve budesonid nebül kullanmalarını, beş gün oral '
                                  'kortikosteroid vermelerini önermek',
                          'is_correct': False,
                          'scenario_update': 'İlaçlar hastalık süresini kısaltmadı; bebekte huzursuzluk ve taşikardi '
                                             'oldu.',
                          'teaching_point': 'Bu tabloda bronkodilatör, inhaler veya sistemik kortikosteroid '
                                            'önerilmez.'},
                         {'text': 'Serum fizyolojikle burun temizliği, sık-az beslenme ve sigarasız ev önermek; '
                                  'inleme, belirgin çekilme, beslenmenin yarıya düşmesinde başvurmalarını öğretmek',
                          'is_correct': True,
                          'explanation': 'Hafif olguda destek tedavisi yeterlidir. Hastalığın birkaç gün daha '
                                         'ağırlaşabileceği anlatılır ve aileye yatış gerektirecek bulgular öğretilir.',
                          'new_finding': 'Aile eğitildi, 48 saat sonra kontrol planlandı. Kontrolde SpO2 %97, beslenme '
                                         'iyi; öksürük iki hafta içinde azalarak geçti.'},
                         {'text': 'Bakteriyel süperenfeksiyonu önlemek için yedi gün oral amoksisilin başlamak ve '
                                  'öksürük şurubu vermek',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik ishal yaptı; öksürük şurubu bebekte uyuklamaya yol açtı.',
                          'teaching_point': 'Viral tabloda antibiyotik ve iki yaş altında öksürük şurubu önerilmez.'},
                         {'text': 'Hastalığın ilerleyebileceği düşüncesiyle bebeği oksijen ihtiyacı olmasa da pediatri '
                                  'servisine yatırarak birkaç gün nazal aspirasyon ve monitörle izlemek',
                          'is_correct': False,
                          'scenario_update': 'Bebek gereksiz yere yatırıldı ve hastanede ek bir enfeksiyon kaptı.',
                          'teaching_point': 'Hafif olgu ayaktan izlenir; yatış için oksijen ihtiyacı, beslenme '
                                            'yetersizliği veya risk faktörü gerekir.'}]}]},
 {'id': 'Y99',
  'category': '🫁 Hırıltı & Solunum Sıkıntısı',
  'age': '4 Yaşında (17 kg)',
  'gender': 'Erkek',
  'complaint': 'Üç gündür yüksek ateş, öksürük ve bugün başlayan sağ yan ağrısı',
  'history': "Babası anlatıyor: 'Üç gündür ateşi 39'a çıkıyor, ateş düşürücüyle düşüyor ama tekrar yükseliyor. "
             "Öksürüğü arttı. Bugün öksürünce sağ yanım ağrıyor dedi. İştahı azaldı ama su içiyor, tuvalete gidiyor.' "
             'Kusma, ishal yok. Daha önce hastaneye yatışı olmamış. Aşıları tam (pnömokok aşısı dahil). Astım yok. '
             'Kardeşi bir hafta önce nezle geçirmiş.',
  'final_diagnosis': 'Komplike Olmayan, Ayaktan Tedavi Edilebilir Toplum Kökenli Bakteriyel Pnömoni (Sağ Alt Lob)',
  'disposition': 'Yüksek Doz Oral Amoksisilin ve 48 Saat Sonra Kontrolle Yeşil Alandan Taburculuk',
  'case_pearl': 'Okul öncesi çocukta yüksek ateş, takipne ve lokal ince raller bakteriyel pnömoniyi düşündürür. '
                'Hipoksemi (SpO2 <%92), belirgin solunum sıkıntısı, oral alamama, dehidratasyon, 6 aydan küçük yaş, '
                'toksik görünüm veya komplikasyon (efüzyon, ampiyem) yoksa ayaktan tedavi edilir. Ayaktan hastada '
                'rutin kan tetkiki gerekmez; grafi tanı belirsizse veya ağır olguda çekilir. İlk seçenek yüksek doz '
                'amoksisilindir (90 mg/kg/gün, 2 doz, 5-7 gün). Makrolid ilk sırada değildir. 48-72 saatte ateşte '
                'düzelme olmaması komplikasyon araştırmasını gerektirir.',
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Ateşli, öksürüklü ve yan ağrısı olan bu çocukta ilk değerlendirmeniz nedir?',
             'options': [{'text': "Genel görünüm, solunum sayısı, çekilmeler ve SpO2'yi ölçmek; akciğerleri iki "
                                  'taraflı dinleyip perküte etmek ve hidrasyonu değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Ateşli öksürükte takipne ve SpO2 alt solunum yolu tutulumunun ve şiddetin '
                                         'göstergesidir. Lokal bulgular ve hidrasyon, yatış veya ayaktan tedavi '
                                         'kararını belirler.',
                          'new_finding': 'Ateş 38.9°C, KTA 128/dk, SS 36/dk (yaşına göre yüksek), SpO2 %95 (oda '
                                         'havası), KDZ 2 sn. Genel durum orta, konuşabiliyor, içebiliyor. Hafif '
                                         'interkostal çekilme. Sağ alt zonda solunum sesleri azalmış, ince raller ve '
                                         'bronşiyal ses, perküsyonda hafif matite. Sol akciğer temiz. Mukozalar nemli. '
                                         'Ense sertliği yok.'},
                         {'text': 'Öksürüğü viral üst solunum yolu enfeksiyonu kabul edip akciğerleri dinlemeden '
                                  'öksürük şurubu ve ateş düşürücü önermek, üç gün sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Akciğer bulguları atlandı; çocuk iki gün sonra solunum sıkıntısı ve SpO2 '
                                             '%90 ile getirildi.',
                          'teaching_point': 'Yüksek ateş ve yan ağrısı olan çocukta akciğer muayenesi şarttır.'},
                         {'text': 'Yan ağrısı nedeniyle karın kaynaklı nedenleri öncelemek, apandisit için akciğeri '
                                  'dinlemeden batın ultrasonografisi istemek',
                          'is_correct': False,
                          'scenario_update': 'Ultrasonografi normal geldi ve akciğer muayenesi saatler sonra yapıldı.',
                          'teaching_point': 'Alt lob tutulumu karın veya yan ağrısı yapabilir; ateşli öksürükte önce '
                                            'akciğer muayenesi yapılmalıdır.'},
                         {'text': 'Ateş ve öksürük nedeniyle hemen damar yolu açıp intravenöz sıvı ve antibiyotik '
                                  'başlayarak servise yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Hipoksemi ve dehidratasyonu olmayan çocuk değerlendirme yapılmadan '
                                             'yatırıldı.',
                          'teaching_point': 'Yatış kararı şiddet ölçütlerine göre verilir; önce değerlendirme '
                                            'yapılmalıdır.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': "Sağ alt zonda lokal bulguları olan, SpO2'si %95 olan bu çocukta hangi tetkik yaklaşımı "
                         'uygundur?',
             'options': [{'text': 'Matite ve yan ağrısı nedeniyle sıvıyı dışlamak için akciğer grafisi çekmek; kan '
                                  'tetkiki ve kültür istememek',
                          'is_correct': True,
                          'explanation': 'Ayaktan tedavi edilecek hastada rutin kan tetkiki gerekmez. Matite ve yan '
                                         'ağrısı plevral sıvı kuşkusu doğurduğu için grafi tedavi kararını etkiler.',
                          'new_finding': 'PA akciğer grafisinde sağ alt lobu dolduran hava bronkogramlı homojen '
                                         'konsolidasyon. Kostofrenik açılar açık, plevral sıvı yok.',
                          'image': 'assets/images/cxr_lobar_pneumonia.png'},
                         {'text': 'Tam kan sayımı, CRP, prokalsitonin ve kan kültürü istemek; sonuçlar gelip '
                                  'değerlendirilmeden antibiyotik ve taburculuk kararını vermemek',
                          'is_correct': False,
                          'scenario_update': 'Saatler süren bekleme sonrası sonuçlar ayaktan tedavi kararını '
                                             'değiştirmedi.',
                          'teaching_point': 'Ayaktan tedavi edilecek komplike olmayan olguda kan tetkiki ve kültür '
                                            'önerilmez.'},
                         {'text': 'Toraks bilgisayarlı tomografisi istemek ve konsolidasyonun yaygınlığına göre tedavi '
                                  'planını belirlemek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi yönetimi değiştirmedi ve çocuk yüksek doz radyasyona maruz '
                                             'kaldı.',
                          'teaching_point': 'Komplike olmayan olguda tomografinin yeri yoktur.'},
                         {'text': 'Solunum yolu virüs paneli ve mikoplazma serolojisi istemek; sonuçlara göre '
                                  'antibiyotik seçimini yapmak',
                          'is_correct': False,
                          'scenario_update': 'Sonuçlar günler sonra geldi ve tedavi gecikti.',
                          'teaching_point': 'Ayaktan tedavide etken tayini gerekmez; tedavi ampiriktir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik ve radyolojik bulgulara göre en olası tanınız nedir?',
             'options': [{'text': 'Parapnömonik efüzyon veya ampiyem',
                          'is_correct': False,
                          'scenario_update': 'Kostofrenik açılar açıktı, sıvı yoktu.',
                          'teaching_point': 'Efüzyonda kostofrenik açı kapanır, menisküs işareti görülür ve solunum '
                                            'sesleri belirgin azalır.'},
                         {'text': 'Akut bronşiolit',
                          'is_correct': False,
                          'scenario_update': 'Çocuk 4 yaşındaydı ve bulgular tek taraflı, lokaldi.',
                          'teaching_point': 'Bronşiolit iki yaş altında, yaygın raller ve hışıltıyla seyreder.'},
                         {'text': 'Yabancı cisme bağlı atelektazi',
                          'is_correct': False,
                          'scenario_update': 'Boğulma öyküsü yoktu, yüksek ateş ve hava bronkogramlı konsolidasyon '
                                             'vardı.',
                          'teaching_point': 'Yabancı cisim ani öksürük öyküsüyle gelir; grafide hava hapsi veya volüm '
                                            'kaybı görülür.'},
                         {'text': 'Komplike olmayan toplum kökenli bakteriyel pnömoni',
                          'is_correct': True,
                          'explanation': 'Yüksek ateş, takipne, sağ alt zonda lokal bulgular ve grafide lober '
                                         'konsolidasyon; sıvı ve hipoksemi olmaması komplike olmayan toplum kökenli '
                                         'bakteriyel pnömoniyi gösterir.',
                          'new_finding': 'Tanı: Komplike olmayan toplum kökenli bakteriyel pnömoni (sağ alt lob).'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi planı hangisidir?',
             'options': [{'text': 'Oral klaritromisin 7 gün başlamak ve öksürük için kodeinli şurup vermek, iki hafta '
                                  'sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Pnömokokta makrolid direnci nedeniyle ateş düşmedi; kodein çocuklarda '
                                             'güvenli değildir.',
                          'teaching_point': 'Bu yaşta tipik bakteriyel tabloda ilk seçenek amoksisilindir; kodein '
                                            'çocuklarda kullanılmaz.'},
                         {'text': 'Pediatri servisine yatırıp intravenöz ampisilin ve oksijen başlamak, grafi düzelene '
                                  'kadar yatışı sürdürmek',
                          'is_correct': False,
                          'scenario_update': 'Oksijen ihtiyacı olmayan çocuk gereksiz yere yatırıldı; grafi düzelmesi '
                                             'haftalar sürdüğü için yatış uzadı.',
                          'teaching_point': 'Hipoksemi ve ağır bulgusu olmayan çocuk ayaktan tedavi edilir; grafi '
                                            'düzelmesi beklenmez.'},
                         {'text': 'Günde iki doza bölünmüş 90 mg/kg/gün oral amoksisilin, antipiretik ve sıvı alımı '
                                  'önermek; 48 saatte kontrol ve uyarı bulgularını öğretmek',
                          'is_correct': True,
                          'explanation': 'Yüksek doz amoksisilin pnömokoku etkili şekilde kapsar. 48-72 saatte ateşte '
                                         'düzelme beklenir; düzelme olmazsa efüzyon gibi komplikasyonlar araştırılır.',
                          'new_finding': 'Amoksisilin 2 x 765 mg başlandı. 48. saat kontrolünde ateş düşmüş, SS 28/dk, '
                                         'SpO2 %97; tedavi 7 güne tamamlandı.'},
                         {'text': 'Tek doz intramüsküler seftriakson yapmak ve ardından antibiyotik vermeden ateşin '
                                  'seyrine göre bir hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Tek doz yetersiz kaldı; çocuk üç gün sonra süren ateş ve artan öksürükle '
                                             'getirildi.',
                          'teaching_point': 'Tek doz parenteral antibiyotik yeterli tedavi değildir; oral alabilen '
                                            'çocukta tam kür oral tedavi verilir.'}]}]},
 {'id': 'Y100',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '8 Yaşında (26 kg)',
  'gender': 'Kız',
  'complaint': 'Bir saat önce bahçede taşı kaldırırken sağ el parmağından sokulma, şiddetli yanıcı ağrı ve uyuşma',
  'history': "Şanlıurfa'da yaşayan aile anlatıyor: 'Temmuz akşamı bahçede taşı kaldırırken bir şey soktu, sarımsı "
             "küçük bir hayvan gördük, kaçtı. Parmağı çok yanıyor, uyuşuyor diyor.' Bir saattir ağrı sürüyor. Kusma, "
             'terleme, salya akması, nefes darlığı yok. Göz hareketlerinde bir tuhaflık fark edilmemiş. Aile parmağa '
             'bez bağlamış ve sokulan yeri jiletle çizip emmeye çalışmış. Tetanos aşıları güncel. Bilinen hastalığı '
             'yok.',
  'final_diagnosis': 'Akrep Sokması, Evre 1 (Yalnız Lokal Bulgular)',
  'disposition': 'Lokal Bakım, Analjezi ve En Az 6 Saatlik Gözlemden Sonra Sistemik Bulgu Gelişmezse Yeşil Alandan '
                 'Taburculuk',
  'case_pearl': "Türkiye'de akrep sokmaları özellikle Güneydoğu Anadolu'da yaz aylarında sıktır; çocuklarda ağır seyir "
                "riski yetişkinlerden yüksektir. Evre 1'de yalnızca lokal ağrı ve parestezi vardır. Evre 2'de uzak "
                "bölgede ağrı ve parestezi, evre 3'te kranial sinir veya iskelet kası bulguları (huzursuzluk, göz "
                "hareketlerinde bozukluk, istemsiz hareketler) ya da otonom bulgular, evre 4'te ikisi birlikte "
                'bulunur. Ciddi bulgular sokmadan sonraki ilk saatlerde ortaya çıkar; bu nedenle çocuklar en az 6 saat '
                "gözlenir. Turnike, kesme ve emme zararlıdır. Evre 1 ve 2'de antivenom gerekmez. Ağrı soğuk uygulama, "
                "analjezik ve gerekirse lokal anestezikle giderilir. UZEM 114'ten danışmanlık alınabilir.",
  'steps': [{'stage_title': 'İlk Klinik Değerlendirme ve Fizik Muayene',
             'question': 'Parmağından sokulan ve şiddetli ağrısı olan bu çocukta ilk değerlendirmeniz nedir?',
             'options': [{'text': 'Bağı çözmek, vital bulguları almak; uzak bölgede ağrı, göz hareketleri, istemsiz '
                                  'hareketler, terleme, salivasyon ve solunumu sistemli değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Bağ dolaşımı bozar ve yarar sağlamaz. Sistemik bulguların, özellikle kranial '
                                         'sinir, iskelet kası ve otonom bulguların aranması evreyi ve tedaviyi '
                                         'belirler.',
                          'new_finding': 'Ateş 36.8°C, KTA 104/dk, SS 22/dk, KB 108/68 mmHg, SpO2 %99. Sağ işaret '
                                         'parmağı pulpasında küçük delinme izi, çevresinde hafif kızarıklık, jiletle '
                                         'yapılmış yüzeyel çizikler. Dokunmakla artan şiddetli yanıcı ağrı ve parmakta '
                                         'karıncalanma; el bileğinin yukarısına yayılım yok. Göz hareketleri normal, '
                                         'istemsiz hareket, terleme, salivasyon, kusma yok. Akciğerler temiz, bilinç '
                                         'açık.'},
                         {'text': 'Zehrin yayılmasını önlemek için parmaktaki bezi daha sıkı bağlamak, sokulma yerini '
                                  'tekrar kesip zehri emmek ve sonra muayeneye geçmek',
                          'is_correct': False,
                          'scenario_update': 'Parmakta ödem ve morarma gelişti; kesi yeri enfekte oldu.',
                          'teaching_point': 'Turnike, kesme ve emme zehrin uzaklaştırılmasında etkisizdir ve doku '
                                            'hasarına yol açar.'},
                         {'text': 'Sokulma öyküsü nedeniyle evrelemeyi beklemeden hemen intravenöz antivenom ve '
                                  'kortikosteroid uygulayıp ardından nörolojik muayene yapmak',
                          'is_correct': False,
                          'scenario_update': 'Antivenom sonrası çocukta yaygın ürtiker ve kusma gelişti; sistemik '
                                             'bulgusu olmayan çocukta gereksizdi.',
                          'teaching_point': 'Antivenom evreye göre verilir; yalnız lokal bulgularda yan etkisi '
                                            'yararından fazladır.'},
                         {'text': 'Ağrının hafiflemesini beklemek için çocuğu bir saat bekleme salonunda oturtmak, '
                                  'ardından vitalleri alıp muayene etmek',
                          'is_correct': False,
                          'scenario_update': 'Bekleme süresince çocuk değerlendirilmedi ve ağrısı giderilmedi.',
                          'teaching_point': 'Sokma sonrası çocuklar hızla değerlendirilmeli ve sistemik bulgular '
                                            'aranmalıdır.'}]},
            {'stage_title': 'Tetkik Kararı',
             'question': 'Yalnız lokal bulguları olan bu çocukta hangi yaklaşım uygundur?',
             'options': [{'text': 'Tam kan sayımı, biyokimya, kreatin kinaz, troponin ve EKG istemek; sonuçlar gelene '
                                  'kadar antivenom bekletmek',
                          'is_correct': False,
                          'scenario_update': 'Tüm sonuçlar normal geldi; çocuk gereksiz kan alımı yaşadı.',
                          'teaching_point': 'Lokal bulgularla sınırlı tabloda rutin tetkik gerekmez; sistemik bulgu '
                                            'gelişirse tetkik planlanır.'},
                         {'text': 'Tetkik istememek; ilk saatlerde ortaya çıkabilecek sistemik bulgular için çocuğu '
                                  'vital takibiyle gözlemde tutmak',
                          'is_correct': True,
                          'explanation': 'Ciddi bulgular genellikle sokmadan sonraki ilk saatlerde gelişir. Gözlem '
                                         'süresince göz hareketleri, motor huzursuzluk, otonom bulgular ve vitaller '
                                         'izlenir.',
                          'new_finding': 'Gözlem başlatıldı. Saatlik muayenelerde sistemik bulgu gelişmedi, vital '
                                         'bulgular stabil seyretti.'},
                         {'text': 'Sokulma yerine yabancı cisim kalıp kalmadığını görmek için el grafisi çekmek ve '
                                  'sonuca göre karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Grafi normal geldi; bu tür sokmalarda deride yapı kalmaz.',
                          'teaching_point': 'Bu tür sokmalarda iğne deride kalmaz; grafi gereksizdir.'},
                         {'text': 'Ağrı şiddetli olduğu için hemen taburcu edip evde gözlemelerini ve bulgu olursa '
                                  'başvurmalarını önermek',
                          'is_correct': False,
                          'scenario_update': 'Çocuk evde birkaç saat içinde huzursuzlanabilirdi; erken taburculuk '
                                             'risklidir.',
                          'teaching_point': 'Çocuklarda sistemik bulgular saatler içinde gelişebileceği için hastanede '
                                            'gözlem gerekir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bulgulara göre en olası tanınız ve evresi nedir?',
             'options': [{'text': 'Akrep sokması, evre 1 (yalnız lokal bulgular)',
                          'is_correct': True,
                          'explanation': 'Sokulma öyküsü, sokulma yerinde şiddetli ağrı ve parestezi olması; uzak '
                                         'bölge, kranial sinir, iskelet kası ve otonom bulguların bulunmaması evre 1 '
                                         'akrep sokmasını gösterir.',
                          'new_finding': 'Tanı: Akrep sokması, evre 1.'},
                         {'text': 'Akrep sokması, evre 3 (nöromüsküler tutulum)',
                          'is_correct': False,
                          'scenario_update': 'Göz hareketleri normaldi ve istemsiz hareket yoktu.',
                          'teaching_point': "Evre 3'te göz hareketlerinde bozukluk, huzursuzluk, istemsiz kasılmalar "
                                            'veya otonom bulgular olur.'},
                         {'text': 'Arı sokmasına bağlı lokal alerjik reaksiyon',
                          'is_correct': False,
                          'scenario_update': 'Sokulma yerinde iğne yoktu ve belirgin şişlik yerine yanıcı ağrı-uyuşma '
                                             'baskındı.',
                          'teaching_point': 'Arı sokmasında iğne çoğu kez deride kalır ve lokal şişlik-kaşıntı '
                                            'belirgindir.'},
                         {'text': 'Örümcek ısırığı (siyah dul)',
                          'is_correct': False,
                          'scenario_update': 'Kas krampları, karın sertliği ve terleme yoktu.',
                          'teaching_point': 'Siyah dul örümceği ısırığında kas krampları ve karın kaslarında sertlik '
                                            'tipiktir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu çocuk için en uygun tedavi ve taburculuk planı hangisidir?',
             'options': [{'text': 'Şiddetli ağrı için morfin infüzyonu başlayıp çocuğu pediatri yoğun bakımına '
                                  'yatırmak ve iki gün monitörde izlemek',
                          'is_correct': False,
                          'scenario_update': 'Opioid sonrası çocukta uyuklama ve solunum depresyonu riski oluştu; '
                                             'yoğun bakım yatağı gereksiz kullanıldı.',
                          'teaching_point': "Evre 1'de basit analjezikler ve lokal anestezik yeterlidir; yoğun bakım "
                                            'gerekmez.'},
                         {'text': 'Soğuk uygulama, parasetamol, gerekirse lokal anestezik ve yara bakımı; en az 6 saat '
                                  'gözlemde sistemik bulgu yoksa taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Ağrı kontrolü evre 1 tedavisinin temelidir. Altı saat boyunca sistemik bulgu '
                                         'gelişmeyen çocuk güvenle taburcu edilir; aileye uyarı bulguları öğretilir.',
                          'new_finding': 'Soğuk uygulama, parasetamol ve dijital blok ile ağrı belirgin azaldı. Yedi '
                                         'saatlik gözlemde sistemik bulgu gelişmedi; çocuk taburcu edildi.'},
                         {'text': 'Profilaktik olarak antivenom, antihistaminik ve kortikosteroid uygulayıp bir saat '
                                  'gözledikten sonra aileyi bilgilendirerek taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Antivenom sonrası serum hastalığı gelişti; gözlem süresi tamamlanmadan '
                                             'taburcu edildi.',
                          'teaching_point': 'Profilaktik antivenom önerilmez; erken taburculuk geç gelişen bulguları '
                                            'atlatır.'},
                         {'text': 'Sokulma yerine sıcak kompres uygulayıp oral antibiyotik ve tetanos aşısı yapmak, '
                                  'ardından hemen taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Sıcak uygulama ağrıyı artırdı; aşıları güncel çocuğa gereksiz tetanos '
                                             'aşısı yapıldı.',
                          'teaching_point': 'Soğuk uygulama tercih edilir; tetanos durumu kontrol edilir ve rutin '
                                            'antibiyotik gerekmez.'}]}]}]
