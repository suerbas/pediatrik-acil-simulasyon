# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Yeşil Alan Vakaları (Part 11: Y101 - Y102)
"""

GREEN_CASES_PART11 = [{'id': 'Y101',
  'category': '👶 Yenidoğan Acilleri',
  'age': '5 Haftalık (3.9 kg)',
  'gender': 'Kız',
  'complaint': 'Doğumdan beri geçmeyen sarılık, son günlerde açık renkli kaka ve bezi boyayan koyu sarı idrar',
  'history': "Annesi anlatıyor: 'Doğumdan sonra ikinci günde sarardı, aile hekimimiz anne sütü sarılığı olabilir, "
             'geçer dedi. Ama bir aydır geçmedi. Son on gündür kakası açık sarı, bazen kirli beyaz gibi; çişi koyu, '
             "bezi sarıya boyuyor. Gayet iyi emiyor, huzursuz değil.' 39 haftalık, 3.250 g normal doğumla doğmuş; "
             'yenidoğan döneminde ışık tedavisi almamış. Yalnızca anne sütü alıyor. K vitamini doğumda yapılmış. '
             'Ailede karaciğer hastalığı bilinmiyor. Yeşil Alana sarılık kontrolü için getirildi.',
  'final_diagnosis': 'Biliyer Atrezi (Neonatal Kolestaz)',
  'disposition': 'Aynı Gün Çocuk Gastroenteroloji ve Çocuk Cerrahisi Merkezine Sevk (Kasai Portoenterostomisi Planı)',
  'case_pearl': 'İki haftadan uzun süren sarılıkta (iyi beslenen, muayenesi normal anne sütüyle beslenen bebekte en '
                'geç üç haftada) total ve direkt (konjuge) bilirubin mutlaka ölçülmelidir. NASPGHAN/ESPGHAN 2017 '
                'kılavuzuna göre direkt veya konjuge bilirubinin 1.0 mg/dL üzerinde olması patolojiktir ve hızlı '
                'değerlendirme gerektirir. Akolik (açık renkli, kil rengi) dışkı ve bezi boyayan koyu idrar kolestazın '
                'en önemli ipuçlarıdır; bebeğin iyi emmesi ve kilo alması tanıyı dışlamaz. Biliyer atrezi neonatal '
                'kolestazın en sık cerrahi nedenidir ve zaman kritiktir: Kasai portoenterostomisi erken yapıldığında '
                '(60 günden önce) kendi karaciğeriyle yaşam olasılığı daha yüksektir. Anne sütü sarılığı indirekt '
                'hiperbilirubinemidir, dışkı rengini değiştirmez. Konjuge hiperbilirubinemide fototerapi tedavi '
                'değildir. Kolestatik bebekte yağda eriyen vitamin emilimi bozulduğundan K vitamini eksikliğine bağlı '
                'kanama riski vardır; koagülasyon değerlendirilmeli ve gerekirse parenteral K vitamini uygulanmalıdır. '
                'Kesin tanı ve tedavi çocuk gastroenteroloji ve çocuk cerrahisi bulunan bir merkezde yapılır.',
  'steps': [{'stage_title': 'Öykü ve Fizik Muayene',
             'question': 'Beş haftalık, iyi emen ve sarılığı doğumdan beri geçmeyen bu bebekte ilk değerlendirmede en '
                         'çok neye odaklanmalısınız?',
             'options': [{'text': 'Bebek iyi emdiği ve huzursuz olmadığı için anne sütü sarılığı kabul etmek, '
                                  'emzirmeye devam önerip iki hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Bebek iki hafta sonra daha belirgin sarılık, kil rengi dışkı ve büyümüş '
                                             'karaciğerle getirildi; değerlendirme yedinci haftaya kaldı.',
                          'teaching_point': 'İki-üç haftadan uzun süren sarılıkta direkt bilirubin ölçülmeden anne '
                                            'sütü sarılığı tanısı konmamalıdır; iyi emmek ve kilo almak kolestazı '
                                            'dışlamaz.'},
                         {'text': 'Sarılığın yoğunluğunu deri rengine göre tahmin etmek, transkutan bilirubin ölçerek '
                                  'değer düşükse ek tetkik yapmadan izleme almak',
                          'is_correct': False,
                          'scenario_update': 'Transkutan ölçüm orta düzeyde çıktı ve bebek izleme alındı; total ve '
                                             'direkt bilirubin ayrımı yapılmadığından kolestaz fark edilmedi.',
                          'teaching_point': 'Transkutan bilirubin yalnızca toplam düzeyi tahmin eder, direkt (konjuge) '
                                            'bileşeni göstermez; uzamış sarılıkta serum total ve direkt bilirubin '
                                            'gerekir.'},
                         {'text': 'Dışkı ve idrar rengini anneye renk kartıyla doğrulatmak, bezi kendiniz görmek; '
                                  'karaciğer, dalak, büyüme eğrisi ve kanama bulgularını muayene etmek',
                          'is_correct': True,
                          'explanation': 'Uzamış sarılıkta akolik dışkı ve koyu idrar kolestazın en değerli '
                                         'ipuçlarıdır; dışkı rengi bizzat görülmeli veya renk kartıyla '
                                         'doğrulanmalıdır. Hepatomegali, splenomegali, büyüme ve kanama bulguları '
                                         'kolestazın nedenini ve aciliyetini değerlendirmeye yardımcı olur.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, Nabız 142/dk, SS 40/dk, SpO2 %99. Genel durumu '
                                         'iyi, aktif, iyi emiyor. Deri ve skleralar belirgin sarı, yeşilimsi tonda. '
                                         'Getirilen bezdeki dışkı soluk, kirli beyaz-açık bej renkte; idrar bezi koyu '
                                         'sarıya boyamış. Karaciğer kot kenarını 3 cm geçiyor, sert kıvamlı; dalak kot '
                                         'kenarında ele geliyor. Ağırlık doğumdan bu yana 650 g artmış. Peteşi, ekimoz '
                                         'veya göbek kanaması yok. Kalp sesleri doğal, üfürüm yok.'},
                         {'text': 'Sarılığın hemolizden kaynaklanabileceğini düşünüp yalnızca kan grubu uyuşmazlığı ve '
                                  'direkt Coombs testine odaklanmak, karın muayenesini ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Kan grupları uyumlu ve Coombs negatif bulundu; karın muayenesi ve dışkı '
                                             'rengi değerlendirilmediği için asıl ipuçları gözden kaçtı.',
                          'teaching_point': 'Hemoliz erken dönem indirekt hiperbilirubinemiye yol açar; beşinci '
                                            'haftada süren sarılıkta öncelikle direkt bilirubin ve kolestaz bulguları '
                                            'değerlendirilmelidir.'}]},
            {'stage_title': 'Laboratuvar ve Görüntüleme',
             'question': 'Soluk dışkı, koyu idrar ve sert hepatomegali saptanan bu bebekte hangi tetkik yaklaşımı en '
                         'uygundur?',
             'options': [{'text': 'Total ve direkt bilirubin, karaciğer enzimleri, GGT, albümin, glukoz, protrombin '
                                  'zamanı ve INR ile tam idrar tetkiki istemek; açlıkta karın ultrasonografisi '
                                  'planlamak',
                          'is_correct': True,
                          'explanation': 'Direkt bilirubin kolestazı doğrular; GGT, transaminazlar ve albümin '
                                         'karaciğer hasarını, protrombin zamanı ve INR K vitamini eksikliğine bağlı '
                                         'kanama riskini gösterir. Açlıkta yapılan ultrasonografi safra kesesini ve '
                                         'diğer anatomik nedenleri değerlendirir.',
                          'new_finding': 'Total bilirubin 9.8 mg/dL, direkt bilirubin 7.1 mg/dL. AST 186 U/L, ALT 142 '
                                         'U/L, GGT 640 U/L, albümin 3.6 g/dL, glukoz 88 mg/dL. Protrombin zamanı 16.8 '
                                         'sn, INR 1.5. Hemogram doğal. Açlık ultrasonografisi: Karaciğer büyük, safra '
                                         'kesesi küçük ve düzensiz duvarlı, porta hepatiste ekojen üçgen şeklinde '
                                         'bant; intrahepatik safra yollarında genişleme yok.'},
                         {'text': 'Yalnızca total bilirubin istemek; değer fototerapi sınırının altındaysa güneş ışığı '
                                  'önerip anne sütüne 48 saat ara vererek yanıtı izlemek',
                          'is_correct': False,
                          'scenario_update': 'Total bilirubin fototerapi sınırının altında bulundu, emzirmeye ara '
                                             'verildi; sarılık geçmedi ve anne sütü üretimi azaldı.',
                          'teaching_point': 'Uzamış sarılıkta toplam bilirubin tek başına yetersizdir; direkt '
                                            'bilirubin ölçülmeden kolestaz atlanır. Emzirmeye ara vermek ve güneş '
                                            'ışığı önerisi bu bebekte yanlış yönlendirir.'},
                         {'text': 'Tiroid fonksiyon testleri ve galaktozemi taramasını istemek, sonuçlar gelene kadar '
                                  'diğer tetkikleri bekletip bebeği bir hafta sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Tiroid testleri normal geldi ve galaktozemi taraması negatif bulundu; '
                                             'bir haftalık bekleme sonunda bebek yedinci haftaya ulaştı.',
                          'teaching_point': 'Hipotiroidi ve metabolik hastalıklar araştırılabilir, ancak akolik '
                                            'dışkılı bebekte direkt bilirubin ve görüntüleme geciktirilmemelidir; '
                                            'zaman cerrahi sonucu belirler.'},
                         {'text': 'Viral hepatit serolojisi ve TORCH paneli istemek, sonuçlar çıkana kadar '
                                  'ursodeoksikolik asit başlayıp iki hafta sonra dışkı rengine ve yanıta göre sevk '
                                  'kararı vermek',
                          'is_correct': False,
                          'scenario_update': 'Seroloji sonuçlarını beklerken başlanan ilaçla dışkı rengi değişmedi; '
                                             'uzman değerlendirmesi iki hafta gecikti.',
                          'teaching_point': 'Ampirik ilaçla izlem cerrahi gerektiren nedenlerin tanısını geciktirir; '
                                            'akolik dışkılı bebek tetkiklerle birlikte gecikmeden uzman merkeze '
                                            'yönlendirilmelidir.'}]},
            {'stage_title': 'Tanı Koyma',
             'question': 'Direkt bilirubin 7.1 mg/dL, GGT 640 U/L, akolik dışkı, sert hepatomegali ve ultrasonografide '
                         'küçük düzensiz safra kesesi saptanan beş haftalık bebekte en olası tanı nedir?',
             'options': [{'text': 'Anne sütü sarılığı',
                          'is_correct': False,
                          'scenario_update': 'Anne sütü sarılığı indirekt hiperbilirubinemidir; dışkı rengi normaldir '
                                             've karaciğer büyümez.',
                          'teaching_point': 'Direkt bilirubin yüksekliği anne sütü sarılığıyla açıklanamaz.'},
                         {'text': 'Konjenital hipotiroidi',
                          'is_correct': False,
                          'scenario_update': 'Hipotiroidi uzamış sarılık yapabilir, ancak genellikle indirekt '
                                             'hiperbilirubinemiyle birliktedir ve akolik dışkı beklenmez.',
                          'teaching_point': 'Uzamış sarılıkta tiroid testi istenir, fakat bu tablo kolestaz ve safra '
                                            'yolu tıkanıklığını düşündürür.'},
                         {'text': 'Biliyer atrezi',
                          'is_correct': True,
                          'explanation': 'Akolik dışkı, koyu idrar, belirgin direkt hiperbilirubinemi, yüksek GGT, '
                                         'sert hepatomegali ve ultrasonografide küçük düzensiz safra kesesiyle porta '
                                         'hepatiste üçgen kordon bulgusu biliyer atreziyi kuvvetle düşündürür. Kesin '
                                         'tanı uzman merkezde intraoperatif kolanjiyografiyle konur.',
                          'new_finding': 'Ön tanı: Biliyer atrezi. Direkt bilirubin 1.0 mg/dL eşiğinin belirgin '
                                         'üzerinde; INR 1.5 ile K vitamini eksikliğine bağlı kanama riski mevcut.'},
                         {'text': 'Koledok kisti',
                          'is_correct': False,
                          'scenario_update': 'Koledok kisti de kolestaz yapabilir, ancak ultrasonografide safra '
                                             'yolunda kistik genişleme görülür; bu bebekte safra yolları genişlememiş.',
                          'teaching_point': 'Ultrasonografide kistik yapı yokluğu, küçük safra kesesi ve üçgen kordon '
                                            'bulgusu ayırımda yol gösterir.'}]},
            {'stage_title': 'Yönetim ve Sevk',
             'question': 'Biliyer atrezi düşünülen beş haftalık bu bebekte en uygun yaklaşım hangisidir?',
             'options': [{'text': 'Bilirubin yüksek olduğu için hastaneye yatırıp çift ünite yoğun fototerapi '
                                  'başlamak, bilirubin düzeyi düştükten sonra çocuk gastroenteroloji polikliniğinden '
                                  'ayaktan randevu almak',
                          'is_correct': False,
                          'scenario_update': 'Fototerapiye rağmen direkt bilirubin düşmedi ve bebekte bronz renk '
                                             'değişimi gelişti; uzman değerlendirmesi gecikti.',
                          'teaching_point': 'Konjuge hiperbilirubinemide fototerapi tedavi değildir ve gereksiz yere '
                                            'zaman kaybettirir.'},
                         {'text': 'Ursodeoksikolik asit ve yağda eriyen vitamin desteği başlayıp ayaktan izlemek, iki '
                                  'hafta sonra dışkı rengine göre sevk kararı vermek',
                          'is_correct': False,
                          'scenario_update': 'İki haftalık ilaç tedavisinde dışkı rengi değişmedi; bebek sevk '
                                             'edildiğinde ameliyat için uygun zaman aralığı daralmıştı.',
                          'teaching_point': 'Biliyer atrezi ilaçla tedavi edilmez; destek tedavisi uzman '
                                            'değerlendirmesini ve cerrahiyi geciktirmemelidir.'},
                         {'text': 'Aynı gün çocuk gastroenteroloji ve çocuk cerrahisi bulunan merkeze sevk etmek; INR '
                                  'yüksekliği için parenteral K vitamini planlamak ve fototerapi vermemek',
                          'is_correct': True,
                          'explanation': 'Kasai portoenterostomisi erken yapıldığında kendi karaciğeriyle yaşam '
                                         'olasılığı daha yüksektir; bu nedenle sevk aynı gün yapılmalıdır. Kolestaz '
                                         'nedeniyle K vitamini emilimi bozulduğundan uzamış INR parenteral K '
                                         'vitaminiyle düzeltilmelidir. Fototerapi konjuge hiperbilirubinemide '
                                         'etkisizdir.',
                          'new_finding': 'Bebek aynı gün çocuk gastroenteroloji ve çocuk cerrahisi merkezine sevk '
                                         'edildi; K vitamini uygulandıktan sonra INR düzeldi. Merkezde intraoperatif '
                                         'kolanjiyografiyle biliyer atrezi doğrulandı ve 38. günde Kasai '
                                         'portoenterostomisi yapıldı.'},
                         {'text': 'Karaciğer biyopsisini kendi hastanenizde planlamak, sonuç çıkana kadar bebeği '
                                  'taburcu edip haftalık bilirubin takibiyle izlemek',
                          'is_correct': False,
                          'scenario_update': 'Biyopsi için sıra beklenirken INR yüksekliği düzeltilmediğinden işlem '
                                             'ertelendi; bebek uzman merkeze ancak dokuzuncu haftada ulaştı.',
                          'teaching_point': 'Tanısal işlemler deneyimli merkezde ve kanama riski düzeltildikten sonra '
                                            'yapılmalıdır; amaç cerrahiyi mümkün olan en erken zamanda '
                                            'yapabilmektir.'}]}]},
 {'id': 'Y102',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '4 Yaşında (16 kg)',
  'gender': 'Erkek',
  'complaint': 'Sabah uyanınca başlayan kusma, baş ağrısı ve halsizlik; anne ve babasında da sabahtan beri baş ağrısı',
  'history': "Ocak ayı, sabah saat 09:30. Annesi anlatıyor: 'Sabah uyandığında başım ağrıyor dedi, iki kez kustu, çok "
             'uyuşuk. İshali yok, ateşi ölçmedim. Kreşte mide virüsü varmış, bizden de geçti herhalde; eşimle benim de '
             'sabahtan beri başımız ağrıyor, ben biraz mideme fena oldum. Dün gece eve döndüğümüzde kombimiz biraz ses '
             "yapıyordu.' Çocuk dün akşam iyiymiş, birlikte akşam yemeği yemişler. Kronik hastalığı ve düzenli "
             "kullandığı ilaç yok. Annesi yeşil alanda 'gastroenterit olabilir mi' diye soruyor.",
  'final_diagnosis': 'Hafif-Orta Karbonmonoksit Zehirlenmesi (Kombi Kaynaklı, Ailesel Maruziyet)',
  'disposition': 'Acil Serviste Normobarik %100 Oksijen Tedavisi ve İzlem, Semptomlar Gerileyince Taburculuk; Ailenin '
                 'Değerlendirilmesi ve Kombi Denetimi Tamamlanmadan Eve Dönülmemesi',
  'case_pearl': 'Karbonmonoksit (CO) zehirlenmesi kış aylarında gastroenterit veya viral enfeksiyon gibi görünebilir; '
                'aynı evde birden fazla kişinin sabah baş ağrısı, bulantı ve halsizlikle başvurması, belirtilerin '
                'evden uzaklaşınca azalması ve ateş ile ishal olmaması en önemli ipuçlarıdır. Çocuklar atipik '
                'bulgularla, örneğin yalnızca kusmayla başvurabilir. Standart nabız oksimetresi karboksihemoglobini '
                'oksihemoglobinden ayırt edemez; SpO2 yanıltıcı biçimde normal görünür. Tanı kooksimetreli kan gazıyla '
                '(venöz örnek yeterlidir) konur; düzeyin klinikle her zaman uyumlu olmadığı ve maruziyetten sonra '
                "geçen süre ve alınan oksijenle düştüğü unutulmamalıdır. Şüphe anında, SpO2'den bağımsız olarak, "
                'maskeyle %100 oksijen başlanır: karboksihemoglobinin yarılanma ömrü oda havasında yaklaşık 320 '
                'dakikadan %100 oksijenle 90 dakikanın altına iner. Hiperbarik oksijen bilinç kaybı, belirgin '
                'nörolojik bulgu, ağır asidoz, kardiyak iskemi veya yüksek karboksihemoglobin düzeyinde konsültasyonla '
                'değerlendirilir; kanıt düzeyi tartışmalıdır. Tedavi kadar önemli olan, aynı ortamdaki herkesin '
                "değerlendirilmesi ve kaynak denetlenmeden eve dönülmemesidir. Türkiye'de doğal gaz kaçağı ve cihaz "
                'arızaları için 187 Doğal Gaz Acil hattı aranabilir.',
  'steps': [{'stage_title': 'Öykü ve İlk Müdahale',
             'question': 'Sabah uyanınca kusma, baş ağrısı ve uyuşuklukla getirilen, anne ve babasında da baş ağrısı '
                         'olan dört yaşındaki çocukta ilk yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Kreşteki salgını göz önüne alıp viral gastroenterit kabul etmek, ondansetron verip '
                                  'ağızdan sıvı denemesi yapmak ve tolere ederse taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Kusması duran çocuk taburcu edildi; aile aynı eve döndü ve akşam '
                                             'saatlerinde çocuk daha uyuşuk, babası ise bayılma hissiyle yeniden '
                                             'başvurdu.',
                          'teaching_point': 'Ateş ve ishal olmadan aynı evde birden fazla kişinin sabah başlayan baş '
                                            'ağrısı ve bulantısı ortak bir çevresel maruziyeti düşündürmelidir; '
                                            'antiemetik tanıyı gizleyebilir.'},
                         {'text': 'Isınma kaynağını, belirtilerin evden çıkınca değişip değişmediğini ve evcil '
                                  'hayvanları sormak; SpO2 normal olsa da maskeyle %100 oksijen başlayıp nörolojik '
                                  'muayene yapmak',
                          'is_correct': True,
                          'explanation': 'Kış aylarında ailesel baş ağrısı, bulantı ve halsizlik, ısınma cihazıyla '
                                         'ilişkili zehirlenme açısından sorgulanmalıdır. Nabız oksimetresi bu durumda '
                                         "yanıltıcı olabileceğinden şüphe anında SpO2'den bağımsız olarak %100 oksijen "
                                         'başlanır; nörolojik muayene ağırlığı değerlendirmede temeldir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.9°C, Nabız 128/dk, SS 26/dk, TA 98/62 mmHg, SpO2 %99 '
                                         '(oda havası). Uyuşuk ama sözlü uyaranla kolayca uyanıyor, oryante, GKS 15; '
                                         'ataksi, nöbet veya fokal bulgu yok. Deri pembe, karın yumuşak, bağırsak '
                                         'sesleri normoaktif. Aile kombinin banyoda olduğunu, bacasının kış başında '
                                         'temizlenmediğini ve evdeki kedinin de sabahtan beri halsiz yattığını '
                                         'belirtiyor. Hastaneye geldikten sonra annenin baş ağrısı biraz hafiflemiş. '
                                         'Non-rebreather maskeyle %100 oksijen başlandı.'},
                         {'text': 'Uyuşukluk nedeniyle santral sinir sistemi enfeksiyonunu öncelikle düşünüp lomber '
                                  'ponksiyon planlamak ve ampirik seftriakson başlamak',
                          'is_correct': False,
                          'scenario_update': 'Ateşi ve meningeal irritasyon bulgusu olmayan çocuğa lomber ponksiyon '
                                             'yapıldı ve beyin omurilik sıvısı normal geldi; oksijen tedavisi bu '
                                             'sürede başlanmamıştı.',
                          'teaching_point': 'Ateşsiz, meningeal bulgusu olmayan ve ailesinde benzer belirtiler bulunan '
                                            'çocukta önce çevresel bir neden düşünülmelidir.'},
                         {'text': 'SpO2 %99 olduğu için oksijen vermeden kan şekeri ve elektrolitlerle başlamak, '
                                  'sonuçlar normal çıkarsa sıvı tedavisiyle gözlem odasında izleyip öğleden sonra '
                                  'yeniden değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Kan şekeri ve elektrolitler normal bulundu; oksijen verilmeden geçen '
                                             'saatlerde çocuğun uyuşukluğu sürdü ve ailenin diğer üyeleri '
                                             'değerlendirilmedi.',
                          'teaching_point': 'Nabız oksimetresi bu gazın hemoglobine bağlı formunu oksihemoglobinden '
                                            'ayırt edemez; normal SpO2 bu zehirlenmeyi dışlamaz.'}]},
            {'stage_title': 'Doğrulayıcı Tetkikler',
             'question': 'Isınma cihazına maruziyet öyküsü olan ve %100 oksijen başlanan bu çocukta hangi tetkik '
                         'yaklaşımı en uygundur?',
             'options': [{'text': 'Arter kan gazında oksijen kısmi basıncına bakmak; değer normal çıkarsa doku '
                                  'oksijenlenmesinin yeterli olduğunu kabul edip oksijeni kesmek',
                          'is_correct': False,
                          'scenario_update': 'Oksijen alırken bakılan kan gazında PaO2 yüksek bulundu ve oksijen '
                                             'kesildi; çocuğun baş ağrısı ve bulantısı yeniden arttı.',
                          'teaching_point': 'PaO2 plazmada çözünmüş oksijeni yansıtır, hemoglobine bağlı zehirli gazı '
                                            'göstermez; normal PaO2 zehirlenmeyi dışlamaz.'},
                         {'text': 'Beyin hasarını göstermek için hemen kranial manyetik rezonans görüntüleme planlamak '
                                  've görüntüleme bitene kadar oksijeni ara vermek',
                          'is_correct': False,
                          'scenario_update': 'Görüntüleme için oksijene ara verildi ve işlem bir saat sürdü; nörolojik '
                                             'muayenesi normal olan çocukta görüntüleme tedaviyi değiştirmedi.',
                          'teaching_point': 'Nörolojik muayenesi normal çocukta acil beyin görüntülemesi gerekli '
                                            'değildir; oksijen tedavisine ara verilmemelidir.'},
                         {'text': 'Kooksimetreli venöz kan gazı, laktat, glukoz ve elektrolitlerle EKG istemek; anne, '
                                  'baba ve evdeki diğer kişileri de değerlendirmeye çağırmak',
                          'is_correct': True,
                          'explanation': 'Kooksimetre hemoglobine bağlı anormal türevleri ölçer ve venöz örnek '
                                         'yeterlidir. Laktat ve asidoz ağırlığı, EKG kardiyak etkilenmeyi '
                                         'değerlendirir. Aynı ortamdaki herkes maruz kaldığından ailenin de '
                                         'değerlendirilmesi gerekir.',
                          'new_finding': 'Oksijen başlandıktan yaklaşık 30 dakika sonra alınan kooksimetreli venöz kan '
                                         'gazı: pH 7.36, HCO3 21 mEq/L, laktat 2.1 mmol/L, COHb %14.6, MetHb %0.8. '
                                         'Glukoz 96 mg/dL, elektrolitler doğal. EKG: Sinüs taşikardisi, iskemik '
                                         'değişiklik yok. Annede COHb %11, babada %9 (sigara içmiyor) bulundu; her '
                                         'ikisi de %100 oksijene alındı.'},
                         {'text': 'Kandaki zehirli maddeleri araştırmak için geniş idrar toksikoloji taraması '
                                  'göndermek, sonuç gelene kadar oksijen yerine damar yolundan sıvı vermek',
                          'is_correct': False,
                          'scenario_update': 'Toksikoloji taraması negatif geldi; bu tetkik zehirlenmeyi göstermediği '
                                             'gibi oksijen tedavisi de gereksiz yere ertelendi.',
                          'teaching_point': 'Rutin idrar toksikoloji taramaları bu gazı saptamaz; tanı kooksimetreyle '
                                            'konur ve oksijen tedavisi beklemeden sürdürülür.'}]},
            {'stage_title': 'Tanı',
             'question': 'Ailesel sabah baş ağrısı, kusma, normal SpO2 ve kooksimetride COHb %14.6 saptanan bu çocukta '
                         'tanınız nedir?',
             'options': [{'text': 'Viral gastroenterit',
                          'is_correct': False,
                          'scenario_update': 'Gastroenterit ishalle seyreder, aile bireylerinin aynı anda baş '
                                             'ağrısıyla başvurmasını ve COHb yüksekliğini açıklamaz.',
                          'teaching_point': "Kış aylarında 'aile boyu gastroenterit' tablosunda ısınma kaynağı mutlaka "
                                            'sorgulanmalıdır.'},
                         {'text': 'Karbonmonoksit zehirlenmesi',
                          'is_correct': True,
                          'explanation': 'Kombi maruziyeti, ailesel belirtiler, evcil hayvanın etkilenmesi, normal '
                                         'SpO2 ve yüksek COHb düzeyi karbonmonoksit zehirlenmesi tanısını doğrular. '
                                         'Düzey, oksijen başlandıktan sonra ölçüldüğü için gerçek maruziyetten daha '
                                         'düşük olabilir.',
                          'new_finding': 'Tanı: Kombi kaynaklı karbonmonoksit zehirlenmesi. Bilinç kaybı öyküsü, '
                                         'nörolojik bulgu, ağır asidoz ve iskemik EKG değişikliği yok.'},
                         {'text': 'Gıda zehirlenmesi',
                          'is_correct': False,
                          'scenario_update': 'Ortak yemek öyküsü dikkat çekici olsa da gıda zehirlenmesi COHb '
                                             'yüksekliğini açıklamaz ve belirtiler evden uzaklaşınca azalmaz.',
                          'teaching_point': 'Ortak besin öyküsü yanıltıcı olabilir; kooksimetre sonucu tanıyı '
                                            'belirler.'},
                         {'text': 'Migren atağı',
                          'is_correct': False,
                          'scenario_update': 'Migren aile bireylerinde eş zamanlı başlamaz ve COHb düzeyini '
                                             'yükseltmez.',
                          'teaching_point': 'Ailede eş zamanlı baş ağrısı, ortak bir çevresel neden '
                                            'düşündürmelidir.'}]},
            {'stage_title': 'Tedavi, İzlem ve Taburculuk',
             'question': "COHb %14.6, nörolojik muayenesi normal ve EKG'si doğal olan bu çocukta en uygun tedavi ve "
                         'taburculuk planı hangisidir?',
             'options': [{'text': 'Kusma geçtiyse oksijeni kesip çocuğu taburcu etmek, aileye evde kombiyi kapatıp '
                                  'pencereleri açık bırakarak dinlenmelerini ve ertesi gün kontrole gelmelerini '
                                  'önermek',
                          'is_correct': False,
                          'scenario_update': 'Aile denetlenmemiş kombinin bulunduğu eve döndü; gece yeniden maruz '
                                             'kalan çocuk sabaha karşı bilinç bulanıklığıyla 112 tarafından getirildi.',
                          'teaching_point': 'Kaynak denetlenip giderilmeden eve dönüş yeniden maruziyete yol açar; '
                                            'pencere açmak güvenli bir çözüm değildir.'},
                         {'text': 'Belirtiler geçip COHb normale inene kadar %100 oksijeni sürdürmek; aileyi de tedavi '
                                  "edip kombi denetlenmeden eve dönmemelerini ve 187'yi aramalarını söylemek",
                          'is_correct': True,
                          'explanation': 'Normobarik %100 oksijen COHb yarılanma ömrünü belirgin kısaltır; tedavi '
                                         'belirtiler düzelip düzey normale inene kadar sürdürülür. Bu çocukta bilinç '
                                         'kaybı, nörolojik bulgu, ağır asidoz veya kardiyak iskemi olmadığından '
                                         'hiperbarik oksijen öncelikli değildir. Kaynağın denetlenmesi ve ailenin '
                                         'korunması tedavinin parçasıdır.',
                          'new_finding': "Dört saatlik %100 oksijen tedavisi sonrası COHb %2'ye indi; baş ağrısı ve "
                                         'bulantı geçti, nörolojik muayene doğal. Anne ve baba da tedavi edildi. Aile '
                                         '187 Doğal Gaz Acil hattını aradı; kombinin baca bağlantısında sızıntı '
                                         'saptandı ve cihaz kullanım dışı bırakıldı. Aile akrabalarında kaldı; '
                                         'gecikmiş nörolojik belirtiler (bellek, dikkat, davranış değişikliği) '
                                         'açısından bilgilendirilip kontrol randevusu verildi.'},
                         {'text': 'COHb %14.6 olduğu için ailenin tamamını hemen hiperbarik oksijen merkezine sevk '
                                  'etmek, sevk sırasında oksijen yerine oda havasıyla taşımak',
                          'is_correct': False,
                          'scenario_update': 'Sevk süresince oksijen verilmedi; hiperbarik merkezde ailenin hiçbir '
                                             'bireyinde hiperbarik tedavi ölçütü saptanmadı ve aile normobarik '
                                             'oksijenle geri yönlendirildi.',
                          'teaching_point': 'Hiperbarik oksijen bilinç kaybı, nörolojik bulgu, ağır asidoz, kardiyak '
                                            'iskemi veya yüksek düzey gibi durumlarda konsültasyonla değerlendirilir; '
                                            'sevk sırasında %100 oksijen kesintisiz sürdürülmelidir.'},
                         {'text': 'Kusması olduğu için çocuğu servise yatırıp İV sıvı ve antiemetik başlamak, oksijeni '
                                  "yalnızca SpO2 %94'ün altına düşerse vermek",
                          'is_correct': False,
                          'scenario_update': 'SpO2 normal seyrettiği için oksijen verilmedi; COHb yavaş düştü ve '
                                             'çocuğun baş ağrısı saatlerce sürdü.',
                          'teaching_point': "Bu zehirlenmede oksijen SpO2'ye göre titre edilmez; COHb'nin "
                                            'uzaklaştırılması için %100 oksijen gerekir.'}]}]}]
