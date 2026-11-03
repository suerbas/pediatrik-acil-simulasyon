# -*- coding: utf-8 -*-
GREEN_CASES_PART1 = [{'id': 'G01',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '16 Aylık',
  'gender': 'Erkek',
  'complaint': 'Burun tıkanıklığı, huzursuzluk, hafif ateş ve öksürük',
  'history': "Annesi kucağında getiriyor: 'Doktor bey/hanım, oğlum 2 gündür çok huysuz. Burnu sürekli berrak "
             'şekilde akıyor ve tıkanıyor, gece memeyi tutmakta zorlandı, ağzından nefes alıyor. Dün akşam '
             'ateşi evde 38.1°C çıktı, ateş düşürücü verince rahatladı. Ara sıra özellikle sırtüstü yatınca '
             'öksürüyor ama nefes darlığı veya morarması olmadı. Kreşe giden ablasında da geçen hafta benzer '
             "burun akıntısı ve hapşırık şikayetleri vardı.'",
  'final_diagnosis': 'Akut Viral Nazofarenjit (Soğuk Algınlığı)',
  'disposition': 'Yeşil Alandan Ayaktan Semptomatik Tedavi ve Aile Eğitimi ile Taburculuk',
  'case_pearl': 'Süt çocuğu ve küçük çocuklarda viral üst solunum yolu enfeksiyonlarında en sık huzursuzluk '
                've beslenme güçlüğü nedeni burun tıkanıklığıdır. Rutin hemogram, CRP veya akciğer grafisi '
                'endike değildir; antibiyotiklerin ve 6 yaş altında sistemik dekongestan/antihistaminik '
                'kombinasyonlarının tedavide yeri yoktur.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Bu hastada ilk değerlendirmede odaklanmanız gereken en uygun klinik muayene '
                         'yaklaşımı hangisidir?',
             'options': [{'text': 'Orofarenks ve burun mukozasını inceleyip, otoskopik muayeneyi çocuğun '
                                  'huzursuzluğunu artırmamak adına erteleyerek doğrudan semptomatik burun '
                                  'açıcı damla uygulamasına geçmek',
                          'is_correct': False,
                          'scenario_update': 'Burun damlası sonrası bebek kısmen rahatlasa da kulak zarları '
                                             'değerlendirilmediği için eşlik edebilecek orta kulak kaynaklı '
                                             'odak olasılığı dışlanamamış oldu.',
                          'teaching_point': 'Ateş ve huzursuzluk ile başvuran iki yaş altı çocuklarda kulak '
                                            'semptomu tarif edilmese bile otoskopik muayene fizik muayenenin '
                                            'vazgeçilmez bir parçasıdır.'},
                         {'text': 'Pediatrik Değerlendirme Üçgeni, vital bulgular, göğüs duvarı çekilmeleri, '
                                  'akciğer oskültasyonu, hidrasyon durumu ve bilateral otoskopik muayeneyi '
                                  'eksiksiz şekilde tamamlamak',
                          'is_correct': True,
                          'explanation': 'Küçük çocuklarda üst solunum yolu semptomlarıyla başvuruda takipne '
                                         've çekilme gibi alt solunum yolu bulguları ile orta kulak tutulumu '
                                         'dışlanmalı, hidrasyon değerlendirilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.8°C, KTA 118/dk, SS 28/dk, SpO2 %99. Genel '
                                         'görünüm stabil. Burun mukozası ödemli ve seröz sekresyonlu, '
                                         'orofarenks hafif hiperemik, tonsillerde eksüda yok. Bilateral '
                                         'timpanik membranlar doğal. Akciğer oskültasyonunda ral veya ronküs '
                                         'yok, çekilme yok, mukozalar ıslak.'},
                         {'text': 'Vital bulguları ve solunum seslerini değerlendirdikten sonra gece '
                                  'öksürüğü tarif edildiği için acil serviste kurtarıcı nebülize salbutamol '
                                  'tedavisi uygulayıp yanıtı gözlemlemek',
                          'is_correct': False,
                          'scenario_update': 'Nebülize bronkodilatatör uygulaması sonrası bebeğin kalp tepe '
                                             "atımı 152/dk'ya yükseldi ve huzursuzluğu arttı; oskültasyonda "
                                             'zaten bronkospazm bulgusu olmadığı görüldü.',
                          'teaching_point': 'Yatarken artan öksürük genellikle postnazal sekresyon '
                                            'akıntısına bağlıdır; oskültasyonda hışıltı veya ekspiryum '
                                            'uzaması olmadan ampirik bronkodilatatör verilmemelidir.'},
                         {'text': 'Ateş ve emme güçlüğü öyküsü nedeniyle fizik muayeneyi kısa tutup hastayı '
                                  'monitörizasyon ve damar yolu açılması için Sarı Alana devretmek',
                          'is_correct': False,
                          'scenario_update': 'Sarı alana alınan bebeğin genel görünümü, perfüzyonu ve '
                                             'oksijen satürasyonu tamamen normal seyretti; acil gözlem '
                                             'yatağı gereksiz yere meşgul edildi.',
                          'teaching_point': 'Genel durumu iyi, yaşa göre solunum sayısı normal ve '
                                            'dehidratasyon bulgusu olmayan hastalar Yeşil Alanda '
                                            'değerlendirilmelidir.'}]},
            {'stage_title': 'Tetkik ve Yaklaşım Kararı',
             'question': 'Fizik muayenesinde takipnesi, çekilmesi ve ek odak bulgusu saptanmayan bu bebekte '
                         'tetkik kararınız ne olmalıdır?',
             'options': [{'text': 'Gizli bakteriyemi ve bakteriyel süperenfeksiyon olasılığını dışlamak '
                                  'amacıyla tam kan sayımı, CRP ve prokalsitonin tetkiklerini birlikte '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: WBC 9.800/mm³ (lenfosit ağırlıklı), Hb '
                                             '11.8 g/dL, PLT 290.000/mm³, CRP 4.2 mg/L, Prokalsitonin 0.04 '
                                             'ng/mL. Kan alınırken bebek ciddi şekilde huzursuzlandı.',
                          'teaching_point': 'Genel durumu iyi, ateşi 38.5°C altında ve muayenesi doğal olan '
                                            'üst solunum yolu enfeksiyonlarında akut faz reaktanları '
                                            'yönetimi değiştirmez.'},
                         {'text': 'Gece öksürüğü ve burun akıntısını değerlendirmek için arka-ön akciğer '
                                  'grafisi ile birlikte paranazal sinüs grafisi çekilmesini planlamak',
                          'is_correct': False,
                          'scenario_update': 'RADYOLOJİ SONUCU: Akciğer parankiminde infiltrasyon izlenmedi. '
                                             'On altı aylık bebekte sinüs boşlukları henüz yeterince '
                                             'pnömatize olmadığından sinüs grafisi tanısal bilgi sağlamadı.',
                          'teaching_point': 'Takipne, hipoksemi veya patolojik oskültasyon bulgusu olmadıkça '
                                            'akciğer grafisi endike değildir; ayrıca küçük çocuklarda rutin '
                                            'sinüs grafisi çekilmez.'},
                         {'text': 'Herhangi bir laboratuvar veya radyolojik görüntüleme tetkiki istemeden, '
                                  'mevcut klinik bulgularla Yeşil Alanda tanı ve tedaviye ilerlemek',
                          'is_correct': True,
                          'explanation': 'Klinik olarak üst solunum yoluyla sınırlı, vital bulguları stabil '
                                         've genel durumu iyi olan çocukta laboratuvar veya görüntüleme '
                                         'tetkiki gerekmez.',
                          'new_finding': 'Tetkik istenmedi; aileye bebeğin akciğer dinleme bulgularının ve '
                                         'kulak zarlarının tamamen doğal olduğu açıklandı.'},
                         {'text': 'Nazofarengeal sürüntüden genişletilmiş solunum yolu viral multipleks PCR '
                                  'paneli ve eş zamanlı boğaz kültürü göndererek sonucu beklemek',
                          'is_correct': False,
                          'scenario_update': 'Mikrobiyoloji laboratuvarından multipleks PCR sonucunun ertesi '
                                             'gün, kültür sonucunun ise 48 saat sonra çıkacağı bildirildi; '
                                             'acil yönetiminde hiçbir değişiklik olmadı.',
                          'teaching_point': 'Ayaktan takip edilecek hafif üst solunum yolu tablolarında '
                                            'multipleks viral panel maliyet-etkin değildir; 3 yaş altında '
                                            'bakteriyel boğaz kültürü de rutin önerilmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Mevcut anamnez ve fizik muayene bulgularıyla en olası klinik tanınız nedir?',
             'options': [{'text': 'Akut Viral Nazofarenjit (Soğuk Algınlığı)',
                          'is_correct': True,
                          'explanation': 'Ev içi temas öyküsü, seröz rinit, hafif ateş ve normal kulak ile '
                                         'akciğer muayenesi akut viral nazofarenjit ile uyumludur.',
                          'new_finding': 'Klinik tanı Akut Viral Nazofarenjit olarak kesinleştirildi.'},
                         {'text': 'Akut Bakteriyel Rinosinüzit',
                          'is_correct': False,
                          'scenario_update': 'Semptomların henüz ikinci gününde olması nedeniyle bakteriyel '
                                             'sinüzit tanı kriterleri olan on günü aşan semptom veya ağır '
                                             'başlangıç karşılanmadı.',
                          'teaching_point': 'Akut bakteriyel rinosinüzit tanısı için semptomların 10 günü '
                                            'aşması, iyileşirken tekrar kötüleşme veya en az 3-4 gün süren '
                                            '≥39°C ateş ve pürülan akıntı gerekir.'},
                         {'text': 'Erken Evre Akut Bronşiolit',
                          'is_correct': False,
                          'scenario_update': 'Tekrarlanan solunum muayenesinde takipne, ekspiratuar uzama, '
                                             'sibilan ronküs veya krepitan ral saptanmadı.',
                          'teaching_point': 'Alt solunum yolu obstrüksiyon bulguları olan hışıltı, raller, '
                                            'takipne veya çekilme bulunmadan yalnızca postnazal öksürükle '
                                            'bronşiolit tanısı konulmaz.'},
                         {'text': 'Mevsimsel Alerjik Rinit Atağı',
                          'is_correct': False,
                          'scenario_update': 'Akut başlayan ateş, aile içi enfeksiyon teması ve 16 aylık yaş '
                                             'grubu tek başına mevsimsel alerjik reaksiyon tablosuyla uyumlu '
                                             'bulunmadı.',
                          'teaching_point': 'Alerjik rinit ateş yapmaz ve süt çocuğu döneminde nadirdir; '
                                            'akut ateşli seröz rinit tablosunda öncelikle viral '
                                            'enfeksiyonlar düşünülmelidir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu hastanın reçete, evde bakım ve taburculuk planı aşağıdakilerden hangisi '
                         'olmalıdır?',
             'options': [{'text': 'Sekonder bakteriyel enfeksiyonu önlemek amacıyla oral '
                                  'amoksisilin-klavulanat süspansiyon ve burun akıntısını kesmek için '
                                  'psödoefedrin-klorfeniramin kombinasyonu içeren şurup reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Ertesi gün bebekte antibiyotiğe bağlı sulu dışkılama ve '
                                             'kombine soğuk algınlığı şurubuna bağlı belirgin huzursuzluk '
                                             'ile taşikardi gelişti.',
                          'teaching_point': 'Viral nazofarenjitte antibiyotik komplikasyonları önlemez; '
                                            'ayrıca 6 yaş altında sistemik dekongestan ve antihistaminik '
                                            'kombinasyonları ciddi toksisite nedeniyle kontrendikedir.'},
                         {'text': 'Beslenme öncesinde topikal oksimetazolin burun spreyini günde 4 kez 7 gün '
                                  'süreyle ve gece öksürüğü için dekstrometorfan şurup başlamak',
                          'is_correct': False,
                          'scenario_update': 'Beşinci günden sonra bebekte ilaca bağlı gelişen rebaund '
                                             'mukozal ödem nedeniyle burun tıkanıklığı daha da şiddetlendi '
                                             've letarji eğilimi görüldü.',
                          'teaching_point': 'Küçük çocuklarda topikal sempatomimetik dekongestanlar sistemik '
                                            'emilim ve rhinitis medicamentosa riski, santral antitussifler '
                                            'ise solunum depresyonu riski nedeniyle önerilmez.'},
                         {'text': 'Düzenli ateş düşürücü şurup reçete edip mukolitik olarak oral '
                                  'asetilsistein ve birinci kuşak sedatif antihistaminik damla ile taburcu '
                                  'etmek',
                          'is_correct': False,
                          'scenario_update': 'Mukolitik şurup sonrası bronşiyal sekresyonları efektif '
                                             'öksüremeyen bebekte hırıltı arttı, sedatif antihistaminik ise '
                                             'emme performansını düşürdü.',
                          'teaching_point': 'İki yaş altı çocuklarda mukolitik ajanlar sekresyon '
                                            'göllenmesine yol açabileceği için, birinci kuşak '
                                            'antihistaminikler ise sedasyon ve antikolinerjik yan etkileri '
                                            'nedeniyle kullanılmaz.'},
                         {'text': 'Emzirme ve uyku öncesi serum fizyolojikle nazal aspirasyon, gerektiğinde '
                                  'parasetamol, sık emzirme ve uyarı bulguları eğitimiyle taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Küçük çocuklarda viral nazofarenjit tedavisinin temel taşı burun '
                                         'açıklığının izotonik tuzlu su ile sağlanması, uygun hidrasyon ve '
                                         'gerektiğinde antipiretiktir.',
                          'new_finding': 'Tedavi düzenlendi; aileye hızlı nefes alma, göğüste çekilme, sıvı '
                                         'alamama veya 3-4 günü aşan ateş durumunda tekrar başvuru eğitimi '
                                         'verilerek taburcu edildi.'}]}]},
 {'id': 'G02',
  'category': '👂 Kulak Ağrısı & KBB',
  'age': '8 Yaş',
  'gender': 'Kız',
  'complaint': 'Boğaz ağrısı, yutkunma güçlüğü ve yüksek ateş',
  'history': "Hasta kendisi anlatıyor: 'Dün sabah okuldayken boğazım çok acımaya başladı, yutkunurken "
             "batıyor. Başım ve karnım da biraz ağrıyor ama burnum hiç akmıyor, öksürüğüm de yok.' Annesi "
             "ekliyor: 'Dün geceden beri ateşi 38.8°C'ye kadar çıkıyor, boynunun yan taraflarında da "
             "dokununca hassasiyet var.'",
  'final_diagnosis': 'Akut Streptokoksik Tonsillofarenjit (AGBHS)',
  'disposition': 'Yeşil Alandan Uygun Antibiyoterapi ve Destek Tedavisi ile Taburculuk',
  'case_pearl': 'Öksürük ve rinit olmadan ani başlayan boğaz ağrısı, ateş, tonsiller eksüda, yumuşak damak '
                'peteşileri ve hassas ön servikal lenfadenopati bakteriyel tonsillofarenjit olasılığını '
                '(Modifiye Centor / McIsaac skoru) yükseltir. Tanı hızlı antijen testi veya boğaz kültürü '
                'ile doğrulanmalı, ilk tercih olarak dar spektrumlu oral Penisilin V / Amoksisilin (10 gün) '
                'veya tek doz İM Benzatin Penisilin G seçilmelidir.',
  'steps': [{'stage_title': 'Fizik Muayene ve Klinik Değerlendirme',
             'question': 'Bu hastada fizik muayenede öncelikle neyi değerlendirmeli ve klinik yaklaşımı '
                         'nasıl belirlemelisiniz?',
             'options': [{'text': 'Boyunda hassasiyet tarif edildiği için ağız içi muayeneyi zorlamadan '
                                  'derin boyun enfeksiyonu açısından öncelikle acil yüzeyel boyun '
                                  'ultrasonografisi istemek',
                          'is_correct': False,
                          'scenario_update': 'Radyoloji bölümünde yapılan boyun ultrasonografisinde '
                                             'bilateral 15 mm reaktif servikal lenf nodları raporlandı ancak '
                                             'birincil farengeal odak değerlendirmesi gecikti.',
                          'teaching_point': 'Akut farengeal enfeksiyonlara ikincil hassas ön servikal '
                                            'lenfadenopati beklenen bir muayene bulgusudur; trismus veya '
                                            'boyun asimetrisi yoksa ultrasonografi endike değildir.'},
                         {'text': 'Karın ağrısı ve yüksek ateş birlikteliği nedeniyle boğaz muayenesini '
                                  'erteleyip akut cerrahi batın açısından çocuk cerrahisi konsültasyonu '
                                  'talep etmek',
                          'is_correct': False,
                          'scenario_update': 'Yapılan batın muayenesinde defans ve rebound saptanmadı; '
                                             'hastanın karın ağrısının üst solunum yolu enfeksiyonuna eşlik '
                                             'eden mezenterik lenfadenite bağlı olduğu anlaşıldı.',
                          'teaching_point': 'Okul çağı çocuklarında bakteriyel tonsillofarenjit tablolarına '
                                            'baş ağrısı, bulantı ve yansıyan karın ağrısı oldukça sık eşlik '
                                            'edebilir.'},
                         {'text': 'Orofarenkste tonsil eksüdası, uvula konumu ve damak peteşilerini, ön '
                                  'servikal lenf nodlarını, döküntüyü ve hepatosplenomegali varlığını '
                                  'muayene etmek',
                          'is_correct': True,
                          'explanation': 'Bakteriyel ve viral etkenleri ayırt etmek, derin boyun '
                                         'komplikasyonlarını dışlamak ve klinik olasılığı belirlemek için '
                                         'tam orofarenks, lenf nodu ve batın muayenesi gereklidir.',
                          'new_finding': 'Vital Bulgular: Ateş 38.9°C, KTA 104/dk, SS 20/dk. Orofarenkste '
                                         'bilateral tonsiller hipertrofik ve hiperemik, üzerlerinde '
                                         'sarı-beyaz kriptik eksüdalar mevcut, yumuşak damakta peteşiler '
                                         'görülüyor, uvula orta hatta. Bilateral ön servikal bölgede 1.5 cm '
                                         'ağrılı hareketli lenfadenopati mevcut. Hepatosplenomegali ve '
                                         'döküntü yok.'},
                         {'text': 'Eksüdatif görünümü yeterli kabul ederek mikrobiyolojik doğrulama '
                                  'planlamadan doğrudan acil serviste tek doz intramüsküler seftriakson '
                                  'enjeksiyonu uygulayıp hastayı göndermek',
                          'is_correct': False,
                          'scenario_update': 'Mikrobiyolojik kanıt alınmadan yapılan geniş spektrumlu '
                                             'parenteral antibiyotik enjeksiyonu ağrılı oldu ve kılavuzların '
                                             'önerdiği tanı-tedavi basamaklarına uymadı.',
                          'teaching_point': 'Tonsiller üzerindeki eksüda tek başına bakteriyel ve viral '
                                            'ayrımı yaptıramaz; ampirik geniş spektrumlu parenteral '
                                            'sefalosporin kullanımı uygun değildir.'}]},
            {'stage_title': 'Tetkik İstem Kararı',
             'question': 'Öksürük olmadan ateş, tonsiller eksüda ve hassas ön servikal lenfadenopatisi olan '
                         'bu hastada tanıyı doğrulamak için en uygun yaklaşım nedir?',
             'options': [{'text': 'Orofarengeal sürüntüden hızlı bakteriyel antijen tarama testi istemek ve '
                                  'negatif çıkması halinde standart boğaz kültürü ile doğrulamak',
                          'is_correct': True,
                          'explanation': 'Klinik olarak bakteriyel tonsillofarenjit olasılığı yüksek olan '
                                         'çocuklarda mikrobiyolojik doğrulama için hızlı antijen tarama '
                                         'testi ve gerekirse boğaz kültürü altın standarttır.',
                          'new_finding': 'Orofarengeal sürüntüden çalışılan hızlı bakteriyel antijen tarama '
                                         'testi POZİTİF sonuçlandı.'},
                         {'text': 'Venöz kan örneği alarak geçirilmiş enfeksiyon antikor titresi, C-reaktif '
                                  'protein ve eritrosit sedimentasyon hızı düzeylerini birlikte çalışmak',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: Antikor titresi 85 IU/mL (Normal <200), '
                                             'CRP 28 mg/L, Sedimentasyon 22 mm/saat. Normal çıkan antikor '
                                             'sonucu akut etkeni doğrulamadı.',
                          'teaching_point': 'Serolojik antikor titreleri akut enfeksiyondan 1-3 hafta sonra '
                                            'yükselmeye başlar; akut tonsillofarenjit tanısında hiçbir yeri '
                                            'yoktur, yalnızca geçirilmiş enfeksiyonu gösterir.'},
                         {'text': 'Herhangi bir sürüntü veya laboratuvar testi istemeden yalnızca fizik '
                                  'muayene bulgularına dayanarak doğrudan ampirik geniş spektrumlu oral '
                                  'antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'Mikrobiyolojik doğrulama yapılmadığı için hastanın gerçekten '
                                             '10 günlük antibiyotik tedavisine ve akut romatizmal ateş '
                                             'profilaksisine ihtiyacı olup olmadığı belirsiz kaldı.',
                          'teaching_point': 'Klinik bulgular bakteriyel olasılığı artırsa da eksüdatif '
                                            'farenjitlerin önemli bir kısmı viraldir; antibiyotik öncesi '
                                            'hızlı antijen testi veya kültürle doğrulama önerilir.'},
                         {'text': 'Tam kan sayımı, periferik yayma, karaciğer fonksiyon testleri ve geniş '
                                  'viral seroloji paneli isteyerek sonuçlar çıkana kadar beklemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: WBC 13.600/mm³ (nötrofil hakimiyeti), '
                                             'atipik lenfosit görülmedi, AST 22 U/L, ALT 18 U/L. Gereksiz '
                                             'venöz kan alımı ve bekleme yaşandı.',
                          'teaching_point': 'Jeneralize lenfadenopati, splenomegali veya uzamış semptomlar '
                                            'olmadıkça tipik akut tonsillofarenjit başvurularında ilk '
                                            'basamakta periferik yayma ve viral seroloji gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Klinik bulgular ve pozitif hızlı antijen testi doğrultusunda kesin tanınız nedir?',
             'options': [{'text': 'Enfeksiyöz Mononükleoz (EBV Tonsillofarenjiti)',
                          'is_correct': False,
                          'scenario_update': 'Hastada arka servikal ve jeneralize lenfadenopati, '
                                             'splenomegali veya periorbital ödem bulunmamakta olup hızlı '
                                             'bakteriyel antijen testi pozitiftir.',
                          'teaching_point': 'Enfeksiyöz mononükleozda yaygın lenfadenopati, splenomegali ve '
                                            'uzamış semptomlar ön plandadır; bu hastada klinik ve test '
                                            'sonucu AGBHS ile uyumludur.'},
                         {'text': 'Akut Streptokoksik (AGBHS) Tonsillofarenjit',
                          'is_correct': True,
                          'explanation': 'Ateş, öksürük olmaması, yumuşak damak peteşileri, eksüdatif '
                                         'tonsillit, ön servikal lenfadenopati ve pozitif hızlı antijen '
                                         'testi AGBHS tonsillofarenjitini doğrular.',
                          'new_finding': 'Tanı: Akut Streptokoksik Tonsillofarenjit (AGBHS) olarak '
                                         'kesinleştirildi.'},
                         {'text': 'Sol Tek Taraflı Peritonsiller Apse',
                          'is_correct': False,
                          'scenario_update': 'Muayenede trismus, uvulada karşı tarafa deviasyon, tek taraflı '
                                             'asimetrik yumuşak damak bombeleşmesi veya boğuk ses '
                                             'saptanmadı.',
                          'teaching_point': 'Peritonsiller apsede şiddetli trismus, uvula deviasyonu, salya '
                                            'akması ve tek taraflı fluktuasyon veren yumuşak damak şişliği '
                                            'görülür.'},
                         {'text': 'Akut Adenoviral Eksüdatif Farenjit',
                          'is_correct': False,
                          'scenario_update': 'Hastada eşlik eden konjonktivit, belirgin seröz rinit veya '
                                             'öksürük yok; ayrıca bakteriyel hızlı antijen testi pozitif '
                                             'saptandı.',
                          'teaching_point': 'Adenoviral farenjit eksüda yapabilse de genellikle rinit, '
                                            'öksürük ve foliküler konjonktivit (faringokonjonktival ateş) '
                                            'ile birlikte seyreder.'}]},
            {'stage_title': 'Tedavi ve İzlem Planı',
             'question': 'Bu hastada akut romatizmal ateş (ARA) ve süpüratif komplikasyonları önlemek için '
                         'en uygun tedavi seçeneği hangisidir?',
             'options': [{'text': 'Oral Trimetoprim-Sulfametoksazol süspansiyonu günde iki doz 10 gün '
                                  'süreyle reçete etmek ve semptomatik analjezik başlayarak hastayı eve '
                                  'taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Reçete edilen antibiyotik farengeal AGBHS eradikasyonu '
                                             'sağlamadı; hastanın ateşi gerilemedi ve Akut Romatizmal Ateş '
                                             'gelişme riski devam etti.',
                          'teaching_point': 'Trimetoprim-sulfametoksazol, tetrasiklinler ve florokinolonlar '
                                            'AGBHS tonsillofarenjitinde bakteriyel eradikasyon sağlamaz ve '
                                            'akut romatizmal ateşi önlemez; kesinlikle kullanılmamalıdır.'},
                         {'text': 'Oral Amoksisilin-Klavulanat (90 mg/kg/gün) tedavisiyle birlikte 3 gün '
                                  'oral deksametazon başlamak ve tedavi bitiminde kontrol boğaz kültürü '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'Geniş spektrumlu antibiyotik ve sistemik steroid gereksiz yan '
                                             'etkilere yol açtı; asemptomatik hastada tedavi sonrası kontrol '
                                             'kültürü de kılavuzlara aykırıydı.',
                          'teaching_point': "AGBHS'de beta-laktamaz üretimi olmadığından klavulanat "
                                            'eklenmesi gereksizdir; ayrıca rutin sistemik kortikosteroid ve '
                                            'semptomsuz hastada tedavi sonrası kontrol kültürü önerilmez.'},
                         {'text': 'Oral Azitromisin süspansiyonu (10 mg/kg/gün, 3 gün) ilk tercih olarak '
                                  'reçete etmek ve bulaş nedeniyle 7 gün okuldan uzak tutmak',
                          'is_correct': False,
                          'scenario_update': 'Bölgesel makrolid direnci nedeniyle bakteriyel eradikasyon '
                                             'başarısız oldu; ayrıca 24 saatlik uygun tedavi sonrası okula '
                                             'dönüş gereksiz yere geciktirildi.',
                          'teaching_point': 'Makrolidler artan direnç oranları nedeniyle yalnızca penisilin '
                                            'alerjisi olan hastalarda alternatif olarak seçilir; uygun '
                                            'antibiyotiğin 24. saatinden sonra bulaştırıcılık sona erer.'},
                         {'text': 'On gün oral Amoksisilin (50 mg/kg/gün) veya tek doz İM Benzatin Penisilin '
                                  'G, parasetamol ve 24. saatte okula dönüş',
                          'is_correct': True,
                          'explanation': "AGBHS'de penisilin direnci yoktur; ilk tercih 10 gün oral "
                                         'Penisilin V / Amoksisilin veya uyum sorunu varsa tek doz İM '
                                         "Benzatin Penisilin G'dir.",
                          'new_finding': 'On günlük oral amoksisilin ve parasetamol reçete edildi; '
                                         'antibiyotiğin 24. saatinden itibaren bulaştırıcılığın biteceği ve '
                                         'okula dönebileceği anlatılarak taburcu edildi.'}]}]},
 {'id': 'G03',
  'category': '👂 Kulak Ağrısı & KBB',
  'age': '22 Aylık',
  'gender': 'Erkek',
  'complaint': 'Sağ kulağını çekiştirme, ağlama krizleri ve ateş',
  'history': "Babası anlatıyor: 'Hocam, 3-4 gündür hafif burun akıntısı vardı ama dün gece sabaha kadar hiç "
             'uyumadı, sürekli ağladı ve sağ kulağını tutup çekiştirdi. Sabah ateşi 39.1°C ölçüldü. '
             "Kulağından herhangi bir akıntı gelmedi ama kulağının çevresine dokundurtmuyor.'",
  'final_diagnosis': 'Akut Otitis Media (AOM)',
  'disposition': 'Yeşil Alandan Uygun Doz Amoksisilin ve Analjezik Tedavisi ile Taburculuk',
  'case_pearl': '2 yaş altı çocuklarda veya şiddetli semptomu (≥39°C ateş, orta-ağır otalji) olan Akut '
                'Otitis Media vakalarında yüksek doz Amoksisilin (80-90 mg/kg/gün, 10 gün) ve özellikle ilk '
                '24-48 saatte düzenli sistemik analjezi (parasetamol veya ibuprofen) başlanmalıdır.',
  'steps': [{'stage_title': 'Otoskopik ve Sistemik Muayene',
             'question': 'Bu hastada tanıyı kesinleştirmek ve olası komplikasyonları değerlendirmek için '
                         'fizik muayenede nasıl bir yaklaşım izlemelisiniz?',
             'options': [{'text': 'Otoskop ile timpanik membranın bombeleşme, hiperemi ve ışık refleksini '
                                  'incelemek, postauriküler bölgeyi ve meninks irritasyon bulgularını '
                                  'kontrol etmek',
                          'is_correct': True,
                          'explanation': 'Orta kulak patolojilerinde en spesifik muayene bulgusu timpanik '
                                         'membranda bombeleşmedir; ayrıca kulak arkası şişlik/hassasiyet ve '
                                         'meninks irritasyon bulguları mutlaka kontrol edilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 39.0°C, KTA 130/dk, SS 28/dk. Sağ timpanik '
                                         'membran ileri derecede hiperemik, opak ve dışa doğru belirgin '
                                         'bombeleşmiş; ışık refleksi kaybolmuş, perforasyon veya otore yok. '
                                         'Sol kulak zarı doğal. Postauriküler eritem, ödem veya fluktuasyon '
                                         'yok, kulak kepçesi normal konumda, ense sertliği yok.'},
                         {'text': 'Çocuk ağladığında kulak zarında fizyolojik kızarıklık olabileceği için '
                                  'otoskopiyi atlayıp yalnızca tragus ve aurikula traksiyonu hassasiyetiyle '
                                  'klinik karar vermek',
                          'is_correct': False,
                          'scenario_update': 'Tragus basısı dış kulak yolu kaynaklı ağrılar için anlamlı '
                                             'olup huzursuz çocukta yanıltıcı bulundu; kulak zarının '
                                             'bombeleşmesi ve bütünlüğü değerlendirilemedi.',
                          'teaching_point': 'Kulak ağrısı ve ateşle başvuran çocukta otoskopik muayene '
                                            'yapılmadan tanı konulamaz; zarın bombeleşmesi ve perforasyon '
                                            'varlığı tedaviyi doğrudan belirler.'},
                         {'text': 'Yüksek ateş ve kulak çevresi hassasiyeti nedeniyle fizik muayeneyi '
                                  'bekletmeden derin doku yayılımını görmek için acil temporal kemik '
                                  'tomografisi istemek',
                          'is_correct': False,
                          'scenario_update': 'Yirmi iki aylık çocuğa tomografi çekilebilmesi için sedasyon '
                                             'hazırlığı gündeme geldi; oysa fizik muayenede kulak arkası '
                                             'ödem veya nörolojik bulgu yoktu.',
                          'teaching_point': 'Kulak kepçesinde öne-aşağı itilme, postauriküler fluktuasyon '
                                            'veya fokal nörolojik defisit gibi komplikasyon bulguları '
                                            'olmadan kesitsel görüntüleme istenmez.'},
                         {'text': 'Dış kulak yoluna topikal lidokainli damla damlatıp otoskopik muayene '
                                  'yapmadan doğrudan kulak burun boğaz hastalıkları acil konsültasyonu talep '
                                  'etmek',
                          'is_correct': False,
                          'scenario_update': 'Zar bütünlüğü görülmeden damlatılan anestezik damla '
                                             'perforasyon olasılığı açısından risk oluşturdu ve birinci '
                                             'basamak acil değerlendirmesi eksik kaldı.',
                          'teaching_point': 'Timpanik membran bütünlüğü otoskop ile doğrulanmadan dış kulak '
                                            'yoluna topikal ajan uygulanmamalı ve komplike olmayan vakalar '
                                            'doğrudan konsülte edilmemelidir.'}]},
            {'stage_title': 'Tetkik ve Yaklaşım Kararı',
             'question': 'Otoskopide sağ timpanik membranda belirgin bombeleşme ve hiperemi saptanan, genel '
                         'durumu iyi olan bu 22 aylık çocukta ek tetkik gerekir mi?',
             'options': [{'text': 'Etken mikroorganizmayı ve antibiyotik duyarlılığını saptamak amacıyla sağ '
                                  'dış kulak yolundan steril eküvyonla sürüntü kültürü alıp laboratuvara '
                                  'göndermek',
                          'is_correct': False,
                          'scenario_update': 'KÜLTÜR SONUCU: Dış kulak yolu normal deri florası olan '
                                             'koagülaz negatif stafilokok üredi; zarın arkasındaki gerçek '
                                             'patojeni yansıtmadı.',
                          'teaching_point': 'Perfore olmayan sağlam kulak zarında dış kulak yolundan alınan '
                                            'sürüntü kültürü orta kulak boşluğundaki bakteriyel etkenleri '
                                            'kesinlikle göstermez.'},
                         {'text': 'Ek laboratuvar veya radyolojik görüntüleme tetkiki istemeden, mevcut '
                                  'otoskopik ve klinik muayene bulgularıyla doğrudan tedavi planına geçmek',
                          'is_correct': True,
                          'explanation': 'Net otoskopik bulguları olan, toksik görünmeyen ve komplikasyon '
                                         'saptanmayan çocukta kan tetkiki veya görüntüleme tanı ve tedaviyi '
                                         'değiştirmez.',
                          'new_finding': 'Ek tetkik istenmeden mevcut klinik ve otoskopik bulgularla tanı '
                                         'aşamasına geçildi.'},
                         {'text': 'Ateşi 39°C üzerinde ölçüldüğü için tam kan sayımı, C-reaktif protein, '
                                  'biyokimya paneli ve periferik kan kültürü istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: WBC 13.400/mm³, CRP 18 mg/L, biyokimya '
                                             'normal. Kan kültüründe üreme olmadı ve sonuçlar tedavi '
                                             'seçimini değiştirmedi.',
                          'teaching_point': 'Ateş odağı otoskopik muayene ile net olarak saptanmış, aşılı ve '
                                            'genel durumu iyi olan çocukta rutin kan tahlili ve kan kültürü '
                                            'endike değildir.'},
                         {'text': 'Orta kulak boşluğundaki sıvıyı doğrulamak amacıyla acil serviste akustik '
                                  'timpanometri ve iki yönlü konvansiyonel mastoid grafisi istemek',
                          'is_correct': False,
                          'scenario_update': 'Ağlayan çocukta timpanometri uyumsuzluğu yaşandı ve düz '
                                             'mastoid grafisi akut mukozal bulanıklık dışında klinik '
                                             'yönetimi değiştiren bir bilgi sağlamadı.',
                          'teaching_point': 'Otoskopide belirgin bombeleşmiş ve hiperemik zar görüldüğünde '
                                            'tanı nettir; acil serviste rutin timpanometri veya '
                                            'konvansiyonel mastoid grafisi gerekmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Hastanın mevcut öykü ve otoskopik muayene bulgularıyla en olası tanınız nedir?',
             'options': [{'text': 'Sağ Efüzyonlu Otitis Media',
                          'is_correct': False,
                          'scenario_update': 'Hastada 39.1°C ateş, şiddetli akut kulak ağrısı ve timpanik '
                                             'membranda belirgin akut inflamasyon ile bombeleşme mevcuttur.',
                          'teaching_point': 'Efüzyonlu otitis mediada orta kulakta sıvı veya hava-sıvı '
                                            'seviyesi vardır ancak akut ateş, şiddetli otalji ve belirgin '
                                            'bombeleşme bulunmaz.'},
                         {'text': 'Sağ Akut Otitis Eksterna',
                          'is_correct': False,
                          'scenario_update': 'Dış kulak yolu ödemli veya eritemli olmayıp inflamasyon ve '
                                             'bombeleşme doğrudan timpanik membran ile orta kulak '
                                             'kaynaklıdır.',
                          'teaching_point': 'Akut otitis eksterna dış kulak yolu enfeksiyonudur; dış kulak '
                                            'yolu ödemli ve döküntülüdür, tragus basısı belirgin ağrılıdır.'},
                         {'text': 'Sağ Akut Otitis Media',
                          'is_correct': True,
                          'explanation': 'Üst solunum yolu enfeksiyonu sonrası akut başlayan otalji, yüksek '
                                         'ateş ve timpanik membranda belirgin bombeleşme Akut Otitis Media '
                                         'tanısını koydurur.',
                          'new_finding': 'Tanı: Sağ Akut Otitis Media (AOM) olarak kesinleştirildi.'},
                         {'text': 'Sağ Akut Koalesan Mastoidit',
                          'is_correct': False,
                          'scenario_update': 'Muayenede kulak kepçesinin öne ve aşağı itilmesi, '
                                             'postauriküler sulkusun silinmesi veya mastoid üzerinde '
                                             'fluktuasyon saptanmadı.',
                          'teaching_point': 'Akut mastoidit tanısı için otitis media bulgularına ek olarak '
                                            'postauriküler eritem, ödem, hassasiyet ve aurikulanın öne-aşağı '
                                            'yer değiştirmesi gerekir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Son 30 günde antibiyotik kullanımı ve eşlik eden pürülan konjonktiviti olmayan 22 '
                         'aylık bu hastada ilk basamak tedavi ne olmalıdır?',
             'options': [{'text': 'Yüksek doz oral Amoksisilin (80-90 mg/kg/gün, 10 gün), düzenli sistemik '
                                  'parasetamol veya ibuprofen ve 48-72 saatte kontrol önerisiyle taburculuk',
                          'is_correct': True,
                          'explanation': 'AAP kılavuzuna göre 2 yaş altı veya şiddetli semptomlu (≥39°C '
                                         "ateş, orta-ağır otalji) AOM'de penisilin dirençli pnömokokları "
                                         'kapsamak için 80-90 mg/kg/gün amoksisilin (10 gün) ve etkin '
                                         'sistemik analjezi ilk tercihtir.',
                          'new_finding': 'Yüksek doz oral amoksisilin ve düzenli ibuprofen/parasetamol '
                                         'başlandı; 48-72 saat içinde ateş veya ağrıda gerileme olmazsa '
                                         'tekrar başvuru eğitimi verilerek taburcu edildi.'},
                         {'text': 'Standart doz oral Amoksisilin (40-45 mg/kg/gün, 5 gün) ile birlikte '
                                  'östaki ödemini çözmek amacıyla oral psödoefedrin ve setirizin şurup '
                                  'başlamak',
                          'is_correct': False,
                          'scenario_update': 'Düşük doz ve kısa süreli antibiyotik tedavisiyle 48. saatte '
                                             'ateş ve kulak ağrısı gerilemedi; dekongestan ve antihistaminik '
                                             'ise huzursuzluğu artırdı.',
                          'teaching_point': "İki yaş altı ve ağır semptomlu AOM'de standart doz ve 5 günlük "
                                            'süre yetersizdir; ayrıca antihistaminik ve dekongestanların AOM '
                                            'iyileşmesinde hiçbir faydası yoktur.'},
                         {'text': 'Antibiyotik başlamadan 48-72 saatlik tedbirsiz bekle-gör izlemi uygulamak '
                                  've ağrı için yalnızca dış kulak yoluna topikal '
                                  'siprofloksasin-deksametazon damla reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Sağlam timpanik membrandan topikal damla orta kulağa geçemedi; '
                                             '39.1°C ateşi ve şiddetli ağrısı olan 22 aylık çocukta klinik '
                                             'tablo ağırlaştı.',
                          'teaching_point': 'Ateşi ≥39°C veya şiddetli otaljisi olan çocuklarda bekle-gör '
                                            'yaklaşımı uygulanmaz, hemen antibiyotik başlanır; sağlam zarda '
                                            'topikal antibiyotikli damlalar etkisizdir.'},
                         {'text': 'H. influenzae ve M. catarrhalis olasılığı nedeniyle ilk basamakta '
                                  'doğrudan 3 gün intramüsküler Seftriakson (50 mg/kg/gün) enjeksiyonu ve '
                                  'antihistaminik başlamak',
                          'is_correct': False,
                          'scenario_update': 'Oral alımı iyi olan ve son bir ayda antibiyotik kullanmayan '
                                             'çocukta gereksiz yere ağrılı parenteral geniş spektrumlu '
                                             'sefalosporin uygulanmış oldu.',
                          'teaching_point': 'Parenteral seftriakson yalnızca kusma nedeniyle oral tedaviyi '
                                            'tolere edemeyen veya amoksisilin-klavulanat tedavisine 48-72 '
                                            'saatte yanıt vermeyen AOM vakalarında endikedir.'}]}]},
 {'id': 'G04',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '4 Yaş',
  'gender': 'Kız',
  'complaint': 'İshal, bulantı ve 2 kez kusma',
  'history': "Annesi anlatıyor: 'Dün akşamdan beri 2 kez kustu, bugün de 4 kez sulu, kötü kokulu ama kansız "
             'dışkılaması oldu. Karnım ağrıyor diyor, tuvalete çıkınca biraz rahatlıyor. Su ve ayran '
             "içebiliyor, en son 2 saat önce çişini yaptı. Ateşi 37.6°C civarında.'",
  'final_diagnosis': 'Dehidratasyonsuz / Hafif Akut Gastroenterit (AGE)',
  'disposition': 'Yeşil Alandan Oral Rehidratasyon, Uygun Beslenme ve Çinko Desteği ile Taburculuk',
  'case_pearl': 'Kanlı dışkılama, yüksek ateş, uzamış seyir veya orta-ağır dehidratasyon bulgusu olmayan '
                'akut gastroenteritlerde rutin gaita mikroskopisi/kültürü veya kan biyokimyası gerekmez. '
                'Tedavinin temeli her kayıp sonrası oral rehidratasyon sıvısı (ORS), erken yaşa uygun '
                'beslenme ve çinko desteğidir; antimotilite ilaçları (loperamid vb.) çocuklarda '
                'kontrendikedir.',
  'steps': [{'stage_title': 'Hidrasyon ve Fizik Muayene Değerlendirmesi',
             'question': 'Akut kusma ve sulu dışkılaması olan bu çocukta ilk aşamada en kritik klinik '
                         'değerlendirme hangisidir?',
             'options': [{'text': 'Dehidratasyon gelişmesini beklemeksizin hemen periferik damar yolu açarak '
                                  '20 mL/kg izotonik sodyum klorür solüsyonunu 30 dakikada hızlı infüzyonla '
                                  'vermek',
                          'is_correct': False,
                          'scenario_update': 'Klinik olarak sıvı açığı bulunmayan ve ağızdan sıvı alabilen '
                                             'çocukta gereksiz invaziv kateterizasyon ve parenteral izotonik '
                                             'sıvı yüklemesi yapıldı.',
                          'teaching_point': 'Yirmi mL/kg izotonik kristaloid bolusu yalnızca hipovolemik '
                                            'şok, ağır dehidratasyon veya oral rehidratasyonu tolere '
                                            'edemeyen orta-ağır dehidratasyon tablolarında uygulanır.'},
                         {'text': 'Karın ağrısı tarif edildiği için fizik muayene öncesinde intestinal '
                                  'obstrüksiyonu değerlendirmek amacıyla ayakta direkt batın grafisi ve '
                                  'ultrasonografi istemek',
                          'is_correct': False,
                          'scenario_update': 'Görüntülemede non-spesifik ince bağırsak gaz-sıvı seviyeleri '
                                             'dışında patoloji saptanmadı; çocuk gereksiz radyasyona maruz '
                                             'kaldı ve değerlendirme süresi uzadı.',
                          'teaching_point': 'Safralı kusma, batın distansiyonu, kanlı dışkılama veya '
                                            'peritonit bulgusu olmayan tipik kusma-ishal başvurularında '
                                            'radyolojik görüntüleme endike değildir.'},
                         {'text': 'Ağızdan sıvı alımını değerlendirmeden bulantıyı hızla kesmek amacıyla ilk '
                                  'basamakta intramüsküler metoklopramid enjeksiyonu uygulayıp hastayı acil '
                                  'gözlem odasına almak',
                          'is_correct': False,
                          'scenario_update': 'Enjeksiyon sonrası çocukta boyun kaslarında istemsiz kasılma '
                                             've bakış kayması ile karakterize akut distonik reaksiyon '
                                             'gelişme riski ortaya çıktı.',
                          'teaching_point': 'Çocuklarda metoklopramid gibi dopamin antagonistleri '
                                            'ekstrapiramidal yan etkiler nedeniyle önerilmez; kusması hafif '
                                            've oral alabilen hastada rutin antiemetik gerekmez.'},
                         {'text': 'Klinik Dehidratasyon Ölçeği kapsamında genel görünüm, göz küreleri, '
                                  'mukoza ıslaklığı, gözyaşı, deri turgoru, kapiller dolum ve batın '
                                  'muayenesini yapmak',
                          'is_correct': True,
                          'explanation': 'Akut kusma ve ishal yönetiminde tetkik ve tedavi kararlarını '
                                         'belirleyen en önemli basamak dehidratasyon derecesinin ve cerrahi '
                                         'batının klinik olarak değerlendirilmesidir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.5°C, KTA 102/dk, SS 22/dk, TA 95/60 mmHg. '
                                         'Çocuk aktif, etrafla ilgili. Göz küreleri normal, ağız mukozası '
                                         'nemli, ağlarken gözyaşı var. Deri turgoru normal, kapiller dolum '
                                         '<2 saniye. Batın yumuşak, bağırsak sesleri hafif artmış, defans '
                                         'veya rebound yok.'}]},
            {'stage_title': 'Tetkik İstem Kararı',
             'question': 'Dehidratasyon bulgusu olmayan, kansız-mukussuz dışkılaması olan ve oral sıvı '
                         'alabilen bu hastada hangi tetkikler istenmelidir?',
             'options': [{'text': 'Taze dışkı örneğinden direkt mikroskopi, gaita kültürü, parazit '
                                  'incelemesi ve Clostridium difficile toksin A/B tarama testlerini birlikte '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: Gaita mikroskopisinde lökosit veya '
                                             'eritrosit görülmedi, parazit kist/trofozoiti saptanmadı; '
                                             'kültür sonucunun ise 72 saat sonra çıkacağı bildirildi.',
                          'teaching_point': 'Gaita mikroskopisi ve kültürü yalnızca kanlı-mukuslu dışkılama, '
                                            'yüksek ateşli toksik görünüm, immün yetmezlik veya uzamış ishal '
                                            'varlığında endikedir.'},
                         {'text': 'Herhangi bir kan veya dışkı tetkiki istemeden, acil serviste ağızdan sıvı '
                                  'toleransını gözlemleyerek klinik tanı ile ilerlemek',
                          'is_correct': True,
                          'explanation': 'Dehidratasyon bulgusu, yüksek ateşi ve kanlı dışkılaması olmayan '
                                         'akut sulu ishal tablolarında kan biyokimyası veya dışkı tetkiki '
                                         'yönetimi değiştirmez.',
                          'new_finding': 'Tetkik istenmedi; çocuğa acil serviste deneme amaçlı küçük '
                                         'yudumlarla oral rehidratasyon sıvısı verildi ve kusmadan rahatça '
                                         'tolere ettiği görüldü.'},
                         {'text': 'Gizli elektrolit dengesizliğini ve metabolik asidozu saptamak için venöz '
                                  'kan gazı, üre, kreatinin, sodyum, potasyum ve hemogram istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: Na 138 mEq/L, K 4.3 mEq/L, Üre 22 mg/dL, '
                                             'Kreatinin 0.4 mg/dL, pH 7.39, HCO3 22 mmol/L. Tüm değerler '
                                             'normal geldi.',
                          'teaching_point': 'Serum elektrolitleri, böbrek fonksiyonları ve kan gazı yalnızca '
                                            'orta-ağır dehidratasyon, intravenöz sıvı gereksinimi veya '
                                            'hipernatremi/hiponatremi şüphesinde istenir.'},
                         {'text': 'Gaita rotavirüs ve adenovirüs hızlı antijen testi ile birlikte akut faz '
                                  'reaktanlarını göndererek viral etkeni kesinleştirmek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: Rotavirüs antijeni negatif, adenovirüs '
                                             'antijeni zayıf pozitif, CRP 6.4 mg/L saptandı; ancak sonuçlar '
                                             'rehidratasyon ve beslenme planını değiştirmedi.',
                          'teaching_point': 'Ayaktan izlenecek hafif sulu ishalde viral antijen testleri ve '
                                            'akut faz reaktanları tedavi yaklaşımını değiştirmediğinden '
                                            'rutin olarak önerilmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bu hastada mevcut anamnez ve fizik muayene bulgularıyla en uygun klinik tanı '
                         'nedir?',
             'options': [{'text': 'Akut Bakteriyel Dizanteri (Shigelloz)',
                          'is_correct': False,
                          'scenario_update': 'Hastada yüksek ateş, tenezm, şiddetli sol alt kadran '
                                             'hassasiyeti veya kanlı-mukuslu dışkılama bulunmamaktadır.',
                          'teaching_point': 'Bakteriyel dizanteri tablosunda yüksek ateş, kramp tarzı '
                                            'şiddetli karın ağrısı, tenezm ve küçük hacimli kanlı-mukuslu '
                                            'dışkılama görülür.'},
                         {'text': 'Akut Gastroenterit ve Ağır Dehidratasyon',
                          'is_correct': False,
                          'scenario_update': 'Hastanın bilinci açık, göz küreleri ve deri turgoru normal, '
                                             'mukozaları ıslak ve kapiller dolum zamanı 2 saniyenin '
                                             'altındadır.',
                          'teaching_point': 'Ağır dehidratasyonda letarji, çökük göz küreleri, gözyaşı '
                                            'yokluğu, çadırlaşan deri turgoru, taşikardi ve uzamış kapiller '
                                            'dolum zamanı saptanır.'},
                         {'text': 'Dehidratasyonsuz Akut Viral Gastroenterit',
                          'is_correct': True,
                          'explanation': 'Kansız sulu dışkılama, subfebril ateş, korunmuş oral alım ve '
                                         'normal hidrasyon muayenesi dehidratasyonsuz akut viral '
                                         'gastroenterit ile uyumludur.',
                          'new_finding': 'Tanı: Dehidratasyonsuz Akut Gastroenterit (AGE) olarak '
                                         'kesinleştirildi.'},
                         {'text': 'Akut Apandisit (Pelvik Yerleşimli)',
                          'is_correct': False,
                          'scenario_update': 'Pelvik apandisit irritatif ishal yapabilse de hastada sürekli '
                                             'ilerleyen karın ağrısı, ateş yüksekliği, iştahsızlık ve '
                                             'lokalize defans/rebound yoktur.',
                          'teaching_point': 'Pelvik yerleşimli apandisitte dışkılama sonrası rahatlamayan '
                                            'persistan ağrı, yüksek ateş ve suprapubik/sağ alt kadran '
                                            'hassasiyeti ön plandadır.'}]},
            {'stage_title': 'Tedavi ve Beslenme Planı',
             'question': 'Bu hastanın evdeki tedavi ve beslenme planı için güncel kılavuzlara göre en doğru '
                         'yaklaşım hangisidir?',
             'options': [{'text': 'Her sulu dışkılama sonrası düşük osmolariteli Oral Rehidratasyon Sıvısı '
                                  '(10 mL/kg), yaşa uygun normal beslenme, çinko desteği ve aile eğitimi',
                          'is_correct': True,
                          'explanation': 'ESPGHAN ve WHO rehberlerine göre temel yaklaşım devam eden '
                                         'kayıpların düşük osmolariteli ORS ile yerine konması, katı diyet '
                                         'kısıtlaması yapılmadan yaşa uygun beslenmenin sürdürülmesi ve '
                                         'çinko/probiyotik desteğidir.',
                          'new_finding': 'ORS kullanım şeması, yaşa uygun beslenme önerileri ve tekrar '
                                         'başvuru kriterleri (dirençli kusma, idrar azalması, kanlı dışkı, '
                                         'uykuya meyil) anlatılarak taburcu edildi.'},
                         {'text': 'Dışkılama sayısını hızla azaltmak için oral loperamid damla ve ampirik '
                                  'metronidazol süspansiyon başlamak, bağırsağı dinlendirmek için 24 saat '
                                  'katı gıdayı kesmek',
                          'is_correct': False,
                          'scenario_update': 'Loperamid verilen çocukta bağırsak motilitesi durarak '
                                             'paralitik ileus ve batın distansiyonu gelişti; aç bırakılması '
                                             'ise enterosit yenilenmesini geciktirdi.',
                          'teaching_point': 'Çocuklarda loperamid gibi antimotilite ilaçları paralitik '
                                            'ileus, toksik megakolon ve bakteriyel translokasyon riski '
                                            'nedeniyle kesinlikle kontrendikedir; ayrıca bağırsak '
                                            'dinlendirme diyeti önerilmez.'},
                         {'text': 'Sıvı ve enerji kaybını karşılamak amacıyla hazır meyve suları veya gazlı '
                                  'içecekler önermek ve yalnızca haşlanmış patates-pirinç lapası diyeti '
                                  'uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Yüksek karbonhidrat ve osmolarite içeren meyve suları lümen '
                                             'içine su çekerek ozmotik ishali şiddetlendirdi; kısıtlı diyet '
                                             'ise kalori açığına yol açtı.',
                          'teaching_point': 'Hazır meyve suları ve gazlı içecekler yüksek osmolarite ve '
                                            'düşük sodyum içerdiğinden ozmotik ishali artırır; kısıtlayıcı '
                                            'BRAT diyeti de artık önerilmemektedir.'},
                         {'text': 'Oral alımı tamamen kesip 12 saat acil gözlemde %5 Dekstroz + %0.2 NaCl '
                                  '(1/5 izotonik) idame sıvısı ve siprofloksasin başlamak',
                          'is_correct': False,
                          'scenario_update': 'Oral alabilen hastada gereksiz yatış yapıldı; hipotonik sıvı '
                                             'infüzyonu hiponatremi riskini artırdı ve viral tabloda '
                                             'florokinolon kullanımı uygunsuz oldu.',
                          'teaching_point': 'Dehidratasyonsuz hastada parenteral sıvı verilmez; İV sıvı '
                                            'gerektiğinde de hiponatremi riski nedeniyle %0.2 NaCl gibi '
                                            'aşırı hipotonik sıvılar tercih edilmemelidir.'}]}]},
 {'id': 'G05',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '5 Yaş',
  'gender': 'Erkek',
  'complaint': 'Aralıklı karın ağrısı ve dışkılama güçlüğü',
  'history': "Annesi anlatıyor: '2 gündür ara sıra karnını tutup ağrıyor diyor, özellikle yemeklerden sonra "
             'kramp gibi gelip 5-10 dakika içinde geçiyor, sonra oyununa devam ediyor. Ateşi ve kusması hiç '
             'olmadı. Anaokuluna başladığından beri okul tuvaletine gitmek istemiyor, 4-5 günde bir çok sert '
             "ve kalın kaka yapıyor, bazen kakasını tutmak için bacaklarını çaprazlıyor.'",
  'final_diagnosis': 'Fonksiyonel Kabızlık (Konstipasyon) ve Buna Bağlı Kolik Karın Ağrısı',
  'disposition': 'Yeşil Alandan Fekal İmpaksiyon Çözümü / Osmotik Laksatif ve Tuvalet Eğitimi ile Taburculuk',
  'case_pearl': 'Çocuk acile akut veya tekrarlayan karın ağrısı ile başvuran hastaların en sık nedenlerinden '
                'biri fonksiyonel kabızlıktır. Organik kırmızı bayraklar (ilk 48 saatte mekonyum çıkaramama, '
                'büyüme geriliği, safralı kusma, perianal fistül, sakral/nörolojik bulgu) yoksa Roma IV '
                'kriterleriyle klinik tanı konur; polietilen glikol veya laktüloz ile davranışsal tuvalet '
                'eğitimi başlanır.',
  'steps': [{'stage_title': 'Öykü ve Fizik Muayene',
             'question': 'Bu hastada organik nedenleri ve cerrahi akut batını dışlamak için fizik muayenede '
                         'nasıl bir yaklaşım izlemelisiniz?',
             'options': [{'text': 'Ağrılı muayeneden kaçınmak amacıyla dış perianal inspeksiyon yapmadan her '
                                  'çocukta rutin rektal tuşe uygulamak ve organik patoloji için rektal '
                                  'biyopsi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Beş yaşındaki çocukta ilk basamakta yapılan rutin rektal tuşe '
                                             'ciddi korku ve travmaya yol açarak dışkı tutma davranışını '
                                             'daha da pekiştirdi.',
                          'teaching_point': 'Tipik dışkı tutma öyküsü ve palpabl fekal kitlesi olan '
                                            'çocuklarda rutin rektal tuşe önerilmez; öncelikle atravmatik '
                                            'dış perianal ve sakral inspeksiyon yapılmalıdır.'},
                         {'text': 'Karın ağrısı nedeniyle fizik muayeneyi beklemeden hastanın oral alımını '
                                  'kesip cerrahi akut batın ön tanısıyla acil çocuk cerrahisi konsültasyonu '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'Ateşi, kusması ve peritonit bulgusu olmayan, ağrı atakları '
                                             'dışında aktif oyun oynayan çocukta cerrahi ekip tarafından '
                                             'akut batın düşünülmedi.',
                          'teaching_point': 'Yemek sonrası gastrokolik refleksle tetiklenen, kısa süren ve '
                                            'aralarında çocuğun tamamen iyi olduğu kramp tarzı ağrılarda '
                                            'öncelikle dikkatli batın palpasyonu yapılmalıdır.'},
                         {'text': 'Büyüme persentillerini, batın palpasyonuyla fekal kitle ve defans/rebound '
                                  'varlığını, lumbosakral bölgeyi, alt ekstremite reflekslerini ve perianal '
                                  'dış inspeksiyonu değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Dışkılama güçlüğü ve karın ağrısında cerrahi batın dışlanmalı, sol '
                                         'alt kadranda fekal kitle, perianal fissür ve nörojenik nedenler '
                                         'için lumbosakral bölge kontrol edilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 92/dk. Tartı ve boy 50. '
                                         'persentilde. Batın yumuşak, defans veya rebound yok; sol alt '
                                         'kadranda ve suprapubik bölgede palpasyonla hareketli sert fekal '
                                         'kitleler ele geliyor. Perianal dış inspeksiyonda saat 6 hizasında '
                                         'yüzeyel anal fissür mevcut. Lumbosakral bölge ve alt ekstremite '
                                         'nörolojik muayenesi doğal.'},
                         {'text': 'Batın ve perianal bölge muayenesini atlayıp ağrıyı hızla kesmek amacıyla '
                                  'doğrudan acil serviste yüksek basınçlı rektal sodyum fosfat lavmanı '
                                  'uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Anal fissür varlığı görülmeden yapılan rektal lavman işlemi '
                                             'sırasında çocuk şiddetli ağrı duydu ve işlem tamamlanamadan '
                                             'rektal mukozal tahriş gelişti.',
                          'teaching_point': 'Fizik muayene ve perianal inspeksiyon tamamlanmadan körlemesine '
                                            'rektal müdahale yapılmamalıdır; anal fissür varlığında rektal '
                                            'işlemler ağrı-tutma döngüsünü ağırlaştırır.'}]},
            {'stage_title': 'Tetkik İstem Kararı',
             'question': 'Okulda dışkı tutma öyküsü olan, muayenede sol alt kadranda fekalom ve anal fissür '
                         'saptanan, kırmızı bayrak bulgusu bulunmayan bu çocukta tetkik yaklaşımınız ne '
                         'olmalıdır?',
             'options': [{'text': 'Kolondaki dışkı yükünü objektif olarak derecelendirmek için rutin ayakta '
                                  'direkt batın grafisi ve tüm batın ultrasonografisi birlikte istemek',
                          'is_correct': False,
                          'scenario_update': 'RADYOLOJİ SONUCU: Direkt grafide kolon çerçevesi boyunca yoğun '
                                             'fekal materyal izlendi, serbest hava yok. Çocuğa tanı '
                                             'değiştirmeyen iyonize radyasyon verildi.',
                          'teaching_point': 'Öykü ve fizik muayene ile fekal birikim net olarak '
                                            'saptandığında rutin direkt batın grafisi tanısal ek katkı '
                                            'sağlamaz ve gereksiz radyasyon maruziyetidir.',
                          'image': 'assets/images/adbg_fecal_impaction.png',
                          'image_caption': 'ADBG: İnen kolonda belirgin fekal gölgelenme'},
                         {'text': 'Sekonder metabolik ve endokrin nedenleri acil serviste taramak amacıyla '
                                  'serbest T4, TSH, çölyak serolojisi, kalsiyum ve ter testi istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: Kalsiyum 9.6 mg/dL, TSH 2.1 mIU/L, sT4 '
                                             'normal; çölyak antikorlarının ise günler sonra çıkacağı '
                                             'bildirildi. Acil yönetimi değişmedi.',
                          'teaching_point': 'Büyüme gelişmesi normal olan ve okula başlama sonrası dışkı '
                                            'tutma davranışıyla ortaya çıkan tablolarda acil serviste rutin '
                                            'endokrin veya çölyak taraması önerilmez.'},
                         {'text': 'Distal kolondaki geçiş zonunu ve aganglionik segmenti dışlamak amacıyla '
                                  'acil baryumlu kolon grafisi ve anorektal manometri tetkiki planlamak',
                          'is_correct': False,
                          'scenario_update': 'Doğumdan sonraki ilk 24 saatte mekonyum çıkaran ve 5 yaşına '
                                             'kadar normal dışkılayan çocukta ileri invaziv tetkik istemi '
                                             'uygun bulunmadı.',
                          'teaching_point': 'Baryumlu kolon grafisi ve manometri yalnızca yenidoğan '
                                            'döneminden beri süren dirençli dışkılama güçlüğü, büyüme '
                                            'geriliği veya kırmızı bayrak varlığında düşünülür.',
                          'image': 'assets/images/adbg_fecal_impaction.png',
                          'image_caption': 'ADBG: İnen kolonda belirgin fekal gölgelenme'},
                         {'text': 'Herhangi bir radyolojik görüntüleme veya laboratuvar tetkiki istemeden, '
                                  'mevcut öykü ve fizik muayene bulgularıyla klinik tanı koymak',
                          'is_correct': True,
                          'explanation': 'Uluslararası pediatrik gastroenteroloji rehberlerine göre tipik '
                                         'dışkı tutma öyküsü ve muayene bulgusu olan, kırmızı bayrağı '
                                         'bulunmayan çocuklarda rutin radyografi veya kan tetkiki önerilmez.',
                          'new_finding': 'Gereksiz radyasyon ve kan alımından kaçınılarak klinik tanı ile '
                                         'doğrudan tedavi planlamasına geçildi.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bu hastada mevcut anamnez ve fizik muayene bulgularıyla en olası tanınız nedir?',
             'options': [{'text': 'Fonksiyonel Kabızlık ve Anal Fissür',
                          'is_correct': True,
                          'explanation': 'Okulda tuvalet erteleme, ağrılı sert dışkılama, anal fissür '
                                         'gelişimi ve ağrı korkusuyla dışkı tutma kısır döngüsü Roma IV '
                                         'kriterlerine göre fonksiyonel kabızlık tanısını koydurur.',
                          'new_finding': 'Tanı: Fonksiyonel Kabızlık (Konstipasyon) ve Sekonder Anal Fissür '
                                         'olarak kesinleştirildi.'},
                         {'text': 'Hirschsprung Hastalığı (Konjenital Aganglionik Megakolon)',
                          'is_correct': False,
                          'scenario_update': 'Anamnezde bebeğin doğumdan sonraki ilk 24 saatte mekonyum '
                                             'çıkardığı, büyümesinin normal olduğu ve büyük kalibreli '
                                             'dışkıladığı görüldü.',
                          'teaching_point': 'Hirschsprung hastalığı yenidoğan döneminde başlar, ilk 48 '
                                            'saatte mekonyum çıkışı gecikir, dışkı tutma davranışı yoktur ve '
                                            'rektum genellikle boştur.'},
                         {'text': 'İleokolik İnvajinasyon (İntususepsiyon)',
                          'is_correct': False,
                          'scenario_update': 'Hastada letarji atakları, safralı kusma, kanlı-mukuslu '
                                             'dışkılama veya sağ üst kadranda sucukvari kitle '
                                             'bulunmamaktadır.',
                          'teaching_point': 'İnvajinasyon çoğunlukla 3 ay - 3 yaş arasında görülür ve '
                                            'şiddetli kıvrandırıcı ağrı-letarji periyotları ile seyreder.'},
                         {'text': 'İnek Sütü Proteini Alerjisi',
                          'is_correct': False,
                          'scenario_update': 'Beş yaşına kadar süt ürünlerini sorunsuz tüketen, atopi öyküsü '
                                             'olmayan ve anaokuluna başlayınca tuvalet tutan çocukta alerjik '
                                             'proktokolit düşünülmedi.',
                          'teaching_point': 'İnek sütü proteini alerjisine bağlı kabızlık daha çok süt '
                                            'çocukluğu ve erken çocukluk döneminde, diğer atopik bulgularla '
                                            'veya standart tedaviye dirençli vakalarda görülür.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu hastada ağrılı dışkılama-tutma kısır döngüsünü kırmak ve tekrarı önlemek için '
                         'en doğru tedavi planı nedir?',
             'options': [{'text': 'Acil serviste tek seferlik rektal fosfat lavmanı uygulayıp bağırsağı '
                                  'boşaltmak ve idame laksatif başlamadan yalnızca posalı diyet önerisiyle '
                                  'eve göndermek',
                          'is_correct': False,
                          'scenario_update': 'İdame osmotik laksatif ve fissür bakımı verilmediği için çocuk '
                                             '4 gün sonra tekrar dışkısını tuttu ve şiddetli karın ağrısıyla '
                                             'acile geri başvurdu.',
                          'teaching_point': 'Fonksiyonel kabızlıkta yalnızca rektumu bir kez boşaltmak '
                                            'yetmez; rektum tonusu ve ağrısız dışkılama alışkanlığı '
                                            'yerleşene kadar en az 2 ay idame osmotik laksatif şarttır.'},
                         {'text': 'Oral osmotik laksatif (Polietilen glikol veya Laktüloz), anal fissür için '
                                  'sıcak oturma banyosu ve bariyer krem, yemek sonrası tuvalet oturuşu',
                          'is_correct': True,
                          'explanation': 'ESPGHAN/NASPGHAN kılavuzlarına göre hem fekal impaksiyonun çözümü '
                                         'hem de idame tedavide ilk tercih oral Polietilen Glikol (PEG) veya '
                                         'yoksa Laktüloz, fissür bakımı ve yemek sonrası 5-10 dakika tuvalet '
                                         'oturuşu eğitimidir.',
                          'new_finding': 'Oral osmotik laksatif, anal fissür için sıcak oturma '
                                         'banyosu/topikal bakım ve gastrokolik refleksten yararlanan '
                                         'davranışsal tuvalet takvimi anlatılarak hasta taburcu edildi.'},
                         {'text': 'Kolik karın ağrısını hızla kesmek için oral trimebutin veya '
                                  'antikolinerjik spazmolitik şurup başlamak ve haftada iki kez senna çayı '
                                  'önermek',
                          'is_correct': False,
                          'scenario_update': 'Verilen antikolinerjik spazmolitik ilaç bağırsak motilitesini '
                                             'daha da yavaşlatarak fekal retansiyonu ve karın ağrısı '
                                             'ataklarını şiddetlendirdi.',
                          'teaching_point': 'Kabızlığa bağlı kolik karın ağrısında antikolinerjik '
                                            'spazmolitikler motiliteyi azaltarak tabloyu kötüleştirir; ilk '
                                            'basamakta uyarıcı bitkisel laksatifler de tercih edilmez.'},
                         {'text': 'Ağızdan sıvı parafin (mineral yağ) ve gliserin fitil başlayıp, okul '
                                  'döneminde tuvalet eğitimini erteleyerek çocuğun bez bağlamasına geri '
                                  'dönmesini önermek',
                          'is_correct': False,
                          'scenario_update': 'Beş yaşındaki çocukta bez bağlamaya geri dönülmesi psikolojik '
                                             'regresyona yol açtı ve düzenli tuvalet oturuşu alışkanlığı '
                                             'kazanılamadı.',
                          'teaching_point': 'Beş yaşındaki çocukta amaç ağrısız yumuşak dışkılama sağlayarak '
                                            'yemeklerden 20-30 dakika sonra ayakları destekli şekilde '
                                            'klozete oturma alışkanlığı kazandırmaktır.'}]}]},
 {'id': 'G06',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '6 Yaş',
  'gender': 'Kız',
  'complaint': 'Vücutta aniden çıkan kaşıntılı kızarıklıklar ve kabarıklıklar',
  'history': "Çocuk kollarını kaşıyarak diyor ki: 'Doktor abla/abi, her yerim çok kaşınıyor!' Annesi "
             "anlatıyor: 'İki saat önce sırtında ve kollarında sivrisinek ısırığı gibi kabarık, etrafı "
             'kızarık döküntüler çıktı. Bir yerdekiler solarken başka yerde yenileri beliriyor. Nefes '
             'darlığı, ses kısıklığı, dudak şişmesi veya kusması olmadı. Üç gün önce hafif burun akıntısı '
             "vardı, bugün de ilk kez çilekli paketli bir atıştırmalık yedi.'",
  'final_diagnosis': 'Akut Ürtiker (Anafilaksi Bulgusu Olmayan)',
  'disposition': 'Yeşil Alandan İkinci Kuşak H1 Antihistaminik Tedavisi ve Anafilaksi Uyarı Eğitimi ile '
                 'Taburculuk',
  'case_pearl': 'Ani gelişen eritematöz-ödematöz plaklarla başvuran her çocukta ilk adım sistemik tutulumu '
                '(solunum, kardiyovasküler, gastrointestinal -> Anafilaksi) dışlamaktır. İzole akut '
                'ürtikerde ilk tercih tedavi sedasyon yapmayan 2. kuşak H1-antihistaminiklerdir; rutin '
                'laboratuvar veya alerji paneli acil serviste istenmez.',
  'steps': [{'stage_title': 'Sistemik Tarama ve Fizik Muayene',
             'question': 'Kaşıntılı döküntülerle başvuran bu çocukta ilk klinik değerlendirmede en öncelikli '
                         'yaklaşım hangisidir?',
             'options': [{'text': 'Hava yolu ödemi, solunum sesleri, tansiyon ve gastrointestinal bulguları '
                                  'sorgulayıp lezyonların basmakla solup solmadığını muayene etmek',
                          'is_correct': True,
                          'explanation': 'Akut başlayan kaşıntılı ödematöz plaklar sistemik alerjik '
                                         'reaksiyonun ilk bulgusu olabileceğinden hava yolu, solunum, '
                                         'dolaşım ve mukoza tutulumu mutlaka değerlendirilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 96/dk, SS 20/dk, TA 100/65 mmHg, '
                                         'SpO2 %99. Dudak, dil ve uvulada ödem yok. Akciğer oskültasyonu '
                                         'doğal, stridor veya wheezing yok. Gövde ve ekstremitelerde '
                                         'basmakla solan, sınırları belirgin eritematöz-ödematöz gezici '
                                         'plaklar mevcut.'},
                         {'text': 'Kütanöz lezyonların yaygınlığını dikkate alarak sistemik reaksiyon '
                                  'gelişimini önlemek amacıyla uyluk anterolateralinden intramüsküler '
                                  'adrenalin uygulayıp hastayı monitörize etmek',
                          'is_correct': False,
                          'scenario_update': 'Solunum ve dolaşım bulgusu olmayan çocukta intramüsküler '
                                             'adrenalin uygulaması sonrası taşikardi (158/dk), titreme, '
                                             'solukluk ve belirgin anksiyete gelişti.',
                          'teaching_point': 'İntramüsküler adrenalin yalnızca mukokütanöz bulgulara solunum, '
                                            'kardiyovasküler veya şiddetli gastrointestinal sistem '
                                            'tutulumunun eşlik ettiği sistemik reaksiyonlarda endikedir; '
                                            'izole deri tutulumunda uygulanmaz.'},
                         {'text': 'Damar yolu açarak parenteral birinci kuşak H1-antihistaminik ve '
                                  'metilprednizolon uygulamak üzere hastayı doğrudan Sarı Alana devretmek',
                          'is_correct': False,
                          'scenario_update': 'Sarı Alana alınan hastanın tüm yaşamsal bulguları stabil '
                                             'seyretti; parenteral birinci kuşak antihistaminik sonrasında '
                                             'çocukta belirgin sedasyon gelişti.',
                          'teaching_point': 'Sistemik tutulumu ve anjiyoödemi olmayan, yaşamsal bulguları '
                                            'stabil hastalarda parenteral sedatif antihistaminik veya rutin '
                                            'intravenöz steroid uygulaması yerine oral tedavi tercih '
                                            'edilir.'},
                         {'text': 'Lezyonların vaskülitik veya enfeksiyöz etiyolojisini ayırt etmek için '
                                  'deri lezyonlarının kenarlarını işaretleyip öncelikle dermatoskopik '
                                  'inceleme ve punch biyopsi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Sağlık personeli hazırlık yaparken çocuğun sırtındaki ilk '
                                             'plakların kendiliğinden solduğu, buna karşın ön kolda yeni '
                                             'plakların çıktığı gözlendi.',
                          'teaching_point': 'Yirmi dört saatten kısa sürede yer değiştirip iz bırakmadan '
                                            'solan akut gezici plaklarda deri biyopsisi endike değildir; '
                                            'biyopsi yalnızca 24-48 saatten uzun süren sabit, purpurik veya '
                                            'ağrılı lezyonlarda düşünülür.'}]},
            {'stage_title': 'Tetkik İstem Kararı',
             'question': 'Sistemik tutulumu olmayan ve genel durumu iyi olan bu hastada acil serviste hangi '
                         'tetkik yaklaşımı seçilmelidir?',
             'options': [{'text': 'Besin tetikleyicisini netleştirmek amacıyla acil serviste total IgE ve '
                                  'çilek dahil spesifik IgE paneli istemek',
                          'is_correct': False,
                          'scenario_update': 'Kan alma işlemi çocuğu huzursuz etti; laboratuvar spesifik IgE '
                                             'sonuçlarının bir hafta sonra çıkacağını bildirdi ve acil '
                                             'yönetim değişmedi.',
                          'teaching_point': 'İlk kez gelişen ve sistemik bulgu içermeyen akut mukokütanöz '
                                            'ataklarda acil serviste spesifik IgE veya geniş alerji taraması '
                                            'yapılması kılavuzlarda önerilmez.'},
                         {'text': 'Hiçbir laboratuvar veya alerji testi istemeden mevcut öykü ve fizik '
                                  'muayene bulgularıyla klinik tanı koymak',
                          'is_correct': True,
                          'explanation': 'Uluslararası rehberlere göre sistemik reaksiyon bulgusu taşımayan '
                                         'akut olgularda rutin kan veya alerji tetkiki önerilmez; çocuklarda '
                                         'en sık tetikleyici yakın zamanlı viral enfeksiyonlardır.',
                          'new_finding': 'Tetkik istenmedi; hastanın genel durumu, orofarenks muayenesi ve '
                                         'solunum bulguları tamamen stabil seyretti.'},
                         {'text': 'Enfeksiyöz tetikleyicileri ve gizli inflamasyonu değerlendirmek için tam '
                                  'kan sayımı, CRP, sedimentasyon ve boğaz kültürü istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: WBC 8.900/mm³, eozinofil %3, CRP 3.1 mg/L, '
                                             'sedimentasyon 11 mm/saat. Sonuçlar tedavi planında hiçbir '
                                             'değişiklik sağlamadı.',
                          'teaching_point': 'Ateşi ve odak bulgusu olmayan akut kütanöz plaklarda rutin akut '
                                            'faz reaktanları veya kültür tetkikleri tanı ve tedaviyi '
                                            'değiştirmez.'},
                         {'text': 'Kompleman aracılı veya otoimmün süreçleri dışlamak üzere serum C3, C4, '
                                  'CH50, ANA ve tiroid otoantikorlarını istemek',
                          'is_correct': False,
                          'scenario_update': 'İstenen kompleman ve otoantikor tetkikleri normal sınırlarda '
                                             'raporlandı ve gereksiz maliyet ile bekleme süresine yol açtı.',
                          'teaching_point': 'Otoimmün ve kompleman incelemeleri yalnızca altı haftadan uzun '
                                            'süren kronik olgularda veya vaskülit şüphesi varlığında '
                                            'poliklinik koşullarında planlanır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Mevcut anamnez ve fizik muayene bulgularıyla en olası klinik tanınız nedir?',
             'options': [{'text': 'Eritema Multiforme Minör',
                          'is_correct': False,
                          'scenario_update': 'Lezyonların üç halkalı sabit hedef tahtası görünümünde '
                                             'olmadığı ve saatler içinde yer değiştirip solduğu yeniden '
                                             'doğrulandı.',
                          'teaching_point': 'Eritema multiformede lezyonlar simetrik, sabit (günlerce aynı '
                                            'yerde kalan) ve tipik santral koyu halkalı hedef '
                                            'görünümündedir.'},
                         {'text': 'Henoch-Schönlein Purpurası (IgA Vasküliti)',
                          'is_correct': False,
                          'scenario_update': 'Lezyonların basmakla tamamen solduğu, alt ekstremite ağırlıklı '
                                             'palpabl purpura niteliği taşımadığı ve artralji bulunmadığı '
                                             'görüldü.',
                          'teaching_point': 'IgA vaskülitinde döküntüler basmakla solmayan palpabl purpura '
                                            'karakterindedir; nadiren başlangıçta ödematöz görünse de kısa '
                                            'sürede purpurik hal alır.'},
                         {'text': 'İzole Akut Ürtiker',
                          'is_correct': True,
                          'explanation': 'Basmakla solan, kaşıntılı, 24 saatten kısa sürede yer değiştiren '
                                         'eritematöz-ödematöz plaklar ve sistemik bulgu olmaması izole akut '
                                         'ürtiker tanısını doğrular.',
                          'new_finding': 'Tanı: Akut Ürtiker (anafilaksi bulgusu olmaksızın).'},
                         {'text': 'Viral Makülopapüler Ekzantem',
                          'is_correct': False,
                          'scenario_update': 'Döküntülerin günlerce sabit kalan makülopapüler elemanlar '
                                             'değil, saatler içinde yer değiştiren belirgin dermal ödem '
                                             'plakları olduğu görüldü.',
                          'teaching_point': 'Viral makülopapüler ekzantemler basmakla solabilir ancak '
                                            'saatler içinde kaybolup başka bölgede çıkan gezici dermal ödem '
                                            'plakları oluşturmaz.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu hastada semptom kontrolü ve güvenli taburculuk için en uygun tedavi yaklaşımı '
                         'hangisidir?',
             'options': [{'text': 'Birinci kuşak oral hidroksizin şurup ve 7 günlük oral prednizolon '
                                  'başlayıp şüpheli tüm meyveleri diyetten kalıcı olarak çıkarmak',
                          'is_correct': False,
                          'scenario_update': 'Hidroksizin kullanan çocukta ertesi gün okulda ağır uyku hali '
                                             've dikkat dağınıklığı gelişti; uzun süreli steroide bağlı '
                                             'huzursuzluk ortaya çıktı.',
                          'teaching_point': 'Akut ürtikerde birinci basamak tedavi sedasyon yapmayan ikinci '
                                            'kuşak H1-antihistaminiklerdir; komplike olmayan vakalarda rutin '
                                            'sistemik kortikosteroid ve kanıtlanmamış kalıcı diyet '
                                            'kısıtlaması önerilmez.'},
                         {'text': 'Viral prodrom öyküsü nedeniyle oral amoksisilin-klavulanat ve '
                                  'kaşıntı/inflamasyon kontrolü için düzenli ibuprofen süspansiyon reçete '
                                  'ederek taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'İbuprofen dozundan iki saat sonra çocuğun gövdesindeki ürtiker '
                                             'plakları hızla arttı ve üst dudakta hafif anjiyoödem gelişti.',
                          'teaching_point': 'Akut ürtikerde non-steroid antiinflamatuar ilaçlar (ibuprofen '
                                            'vb.) lökotrien sentezini artırarak ürtiker ve anjiyoödemi '
                                            'alevlendirebilir; ateş/ağrı durumunda parasetamol tercih '
                                            'edilmelidir.'},
                         {'text': 'Yalnızca kalamin losyon ve soğuk uygulama önerip sistemik antihistaminik '
                                  'vermeden 24 saat acil gözlem odasında yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Sistemik H1-antihistaminik verilmeyen çocuğun gece boyunca '
                                             'şiddetli kaşıntısı devam etti ve uyuyamadı; yaşamsal bulguları '
                                             'ise tamamen normal kaldı.',
                          'teaching_point': 'İzole akut ürtikerde 24 saatlik hastane yatışı gerekmez; oral '
                                            'ikinci kuşak H1-antihistaminik semptomları etkin biçimde '
                                            'kontrol eder.'},
                         {'text': 'İkinci kuşak oral H1-antihistaminik başlamak, non-steroid '
                                  'antiinflamatuarlardan kaçınmayı önermek ve sistemik alerji uyarılarını '
                                  'anlatarak taburcu etmek',
                          'is_correct': True,
                          'explanation': 'EAACI/GA²LEN/EDF/WAO rehberlerine göre akut ürtikerde ilk tercih '
                                         'standart doz 2. kuşak oral H1-antihistaminiktir; aileye '
                                         'lezyonların birkaç gün dalgalanabileceği ve anafilaksi kırmızı '
                                         'bayrakları anlatılmalıdır.',
                          'new_finding': 'Oral setirizin/desloratadin tedavisi düzenlendi; nefes darlığı, '
                                         'ses kısıklığı, dil-dudak şişmesi veya tekrarlayan kusma olursa '
                                         'derhal acile başvuru eğitimi verilerek taburcu edildi.'}]}]},
 {'id': 'G07',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '7 Yaş',
  'gender': 'Erkek',
  'complaint': 'Yanaklarda belirgin kızarıklık ve kollarında dantel gibi döküntü',
  'history': "Çocuk gayet neşeli bir şekilde muayene masasında oturuyor: 'Arkadaşlarım yanaklarıma boya mı "
             'sürdün veya güneşte mi yandın diye sordu ama hiç acımıyor, sadece kollarımdaki kızarıklıklar '
             "sıcakta biraz belli oluyor.' Annesi anlatıyor: 'Bir hafta önce hafif bir kırgınlığı ve burun "
             'akıntısı olmuştu, geçti sanmıştık. Dün iki yanağı parlak kırmızı oldu, bugün de kollarının dış '
             'yüzünde ve gövdesinde kafes veya dantel gibi pembe döküntüler fark ettik. Genel durumu ve '
             "iştahı çok iyi.'",
  'final_diagnosis': 'Eritema İnfeksiyozum (Beşinci Hastalık - Parvovirus B19)',
  'disposition': 'Yeşil Alandan Semptomatik İzlem ve Bulaştırıcılık/Gebe Teması Bilgilendirmesi ile '
                 'Taburculuk',
  'case_pearl': "Parvovirus B19'un neden olduğu Eritema İnfeksiyozum'da (Beşinci Hastalık) yanaklarda parlak "
                "malar eritem ('tokatlanmış yüz') ve ekstremitelerde retiküler (dantelvari) döküntü "
                'tipiktir. Döküntü çıktığında hasta artık bulaştırıcı değildir ve okula gidebilir; ancak '
                'kronik hemolitik anemili bireylerde aplastik kriz ve gebelerde fetal hidrops riski '
                'unutulmamalıdır.',
  'steps': [{'stage_title': 'Fizik Muayene ve Risk Faktörü Sorgulama',
             'question': 'Bu hastada ilk fizik muayene ve anamnez derinleştirmesinde öncelikle neyi '
                         'değerlendirmelisiniz?',
             'options': [{'text': 'Yanaklardaki malar eritemi, ağız çevresi solukluğunu ve ekstremitelerdeki '
                                  'retiküler döküntüyü inceleyip bilinen hemolitik anemi veya gebe temasını '
                                  'sorgulamak',
                          'is_correct': True,
                          'explanation': 'Karakteristik iki evreli döküntü paterni klinik tanıyı '
                                         'yönlendirir; etkenin eritroid öncüllere tropizmi nedeniyle kronik '
                                         'hemolitik anemi ve ev içi gebelik teması mutlaka sorgulanmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 88/dk, SS 18/dk. Genel durum çok '
                                         'iyi. Her iki yanakta parlak kırmızı malar eritem, perioral '
                                         'solukluk ve ekstremite ekstansör yüzlerinde dantelvari (retiküler) '
                                         'makülopapüler döküntü mevcut. Orofarenks doğal, lenfadenopati veya '
                                         'organomegali yok. Bilinen kan hastalığı ve evde gebe teması yok.'},
                         {'text': 'Yüzdeki malar eritem nedeniyle akut fotosensitif bağ dokusu hastalığı '
                                  'düşünerek eklem muayenesi yapıp hastayı acil gözlemde monitörize etmek',
                          'is_correct': False,
                          'scenario_update': 'Eklem muayenesinde artrit bulgusu saptanmadı; 1 hafta önceki '
                                             'viral prodrom ve ekstremitelerdeki tipik dantelvari patern göz '
                                             'ardı edilmiş oldu.',
                          'teaching_point': 'Kısa viral prodromu izleyen akut çift taraflı malar eritem, '
                                            'perioral solukluk ve ekstremitelerde retiküler döküntü okul '
                                            'çağı çocuklarında öncelikle karakteristik viral ekzantemi '
                                            'düşündürür.'},
                         {'text': 'Yüksek bulaştırıcılıklı solunum yolu ekzantemi şüphesiyle hastayı derhal '
                                  'negatif basınçlı izolasyon odasına alıp ağız içinde Koplik lekesi aramak',
                          'is_correct': False,
                          'scenario_update': 'İzolasyon odasına alınan çocuğun ateşinin olmadığı, '
                                             'öksürük/koriza/konjonktivit bulgusu taşımadığı ve bukkal '
                                             'mukozasının tamamen doğal olduğu görüldü.',
                          'teaching_point': 'Ateşsiz, genel durumu çok iyi olan ve 3C bulgusu (öksürük, '
                                            'koriza, konjonktivit) bulunmayan retiküler döküntülü çocukta '
                                            'kızamık izolasyonu endike değildir.'},
                         {'text': 'Yanaklardaki eritem ve perioral solukluğu bakteriyel toksin aracılı '
                                  'döküntü lehine yorumlayıp öncelikle tonsiller eksüda ve Pastia '
                                  'çizgilerini aramak',
                          'is_correct': False,
                          'scenario_update': 'Orofarenks muayenesinde tonsiller doğal bulundu, çilek dili '
                                             'saptanmadı ve döküntünün zımpara kağıdı dokusunda değil '
                                             'düz-retiküler yapıda olduğu görüldü.',
                          'teaching_point': 'Bakteriyel ekzotoksin kaynaklı döküntülerde akut yüksek ateş, '
                                            'eksüdatif tonsillofarenjit ve deride pütürlü zımpara kağıdı '
                                            'hissi veren yaygın noktasal papüller beklenir.'}]},
            {'stage_title': 'Tetkik İstem Kararı',
             'question': 'Bilinen kronik hastalığı olmayan ve muayene bulguları tipik olan bu çocukta hangi '
                         'tetkik yaklaşımı uygundur?',
             'options': [{'text': 'Tanıyı mikrobiyolojik olarak kesinleştirmek için acil serviste viral '
                                  'spesifik IgM/IgG serolojisi ve kantitatif kan PCR testi istemek',
                          'is_correct': False,
                          'scenario_update': 'Damar yolu açılırken çocuk ağladı; dış laboratuvara gönderilen '
                                             'seroloji ve PCR sonuçlarının 4 gün sonra çıkacağı öğrenildi.',
                          'teaching_point': 'İmmünkompetan ve hematolojik hastalığı bulunmayan çocuklarda '
                                            'karakteristik retiküler ekzantem evresinde serolojik veya '
                                            'moleküler doğrulama testlerine gerek yoktur.'},
                         {'text': 'Eritroid seri baskılanmasını ve olası aplastik krizi taramak amacıyla tam '
                                  'kan sayımı, retikülosit yüzdesi ve periferik yayma istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: Hb 12.8 g/dL, Hct %38, Retikülosit %1.1, '
                                             'WBC 7.200/mm³, PLT 265.000/mm³. Tüm hematolojik parametreler '
                                             'normal saptandı.',
                          'teaching_point': 'Sağlıklı çocuklarda eritropoezdeki geçici duraklama klinik '
                                            'anemiye yol açmaz; tam kan sayımı ve retikülosit yalnızca '
                                            'kronik hemolitik anemisi (orak hücre, sferositoz vb.) olanlarda '
                                            'endikedir.'},
                         {'text': 'Hiçbir laboratuvar veya görüntüleme tetkiki istemeden mevcut '
                                  'karakteristik öykü ve fizik muayene bulgularıyla klinik tanı koymak',
                          'is_correct': True,
                          'explanation': 'Sağlıklı çocuklarda tipik malar eritem ve ekstremitelerde '
                                         'dantelvari döküntü varlığında tanı tamamen kliniktir; ek kan '
                                         'tetkiki yönetimi değiştirmez.',
                          'new_finding': 'Tetkik istenmedi; tanı klinik bulgularla netleştirildi ve aile '
                                         'bilgilendirme aşamasına geçildi.'},
                         {'text': 'Atipik bakteriyel farenjit ve streptokoksik ekzantemi dışlamak için hızlı '
                                  'antijen testi, boğaz kültürü ve ASO titresi istemek',
                          'is_correct': False,
                          'scenario_update': 'Hızlı antijen testi negatif sonuçlandı, ASO 90 IU/mL geldi; '
                                             'farenjit bulgusu olmayan çocukta gereksiz sürüntü ve kan '
                                             'işlemi yapıldı.',
                          'teaching_point': 'Ateş ve boğaz ağrısı olmayan, orofarenksi doğal saptanan '
                                            'retiküler döküntülü hastada boğaz kültürü veya ASO istemenin '
                                            'tanısal değeri yoktur.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bu hastada mevcut bulgularla kesin tanınız nedir?',
             'options': [{'text': 'Kızıl (Akut Streptokoksik Ekzantem)',
                          'is_correct': False,
                          'scenario_update': 'Orofarenkste eksüda/hiperemi olmadığı, ateşin bulunmadığı ve '
                                             'döküntünün zımpara kağıdı karakteri taşımadığı tekrar '
                                             'değerlendirildi.',
                          'teaching_point': 'Kızılda perioral solukluk görülebilse de yüksek ateş, akut '
                                            'tonsillofarenjit, çilek dili ve kıvrım yerlerinde koyulaşan '
                                            'noktasal pütürlü döküntü eşlik eder.'},
                         {'text': 'Eritema İnfeksiyozum (Beşinci Hastalık)',
                          'is_correct': True,
                          'explanation': 'Hafif prodromdan 1 hafta sonra gelişen parlak malar eritem '
                                         "('tokatlanmış yüz') ve ekstremitelerde retiküler (dantelvari) "
                                         'döküntü Parvovirus B19 enfeksiyonunun patognomonik bulgusudur.',
                          'new_finding': 'Tanı: Eritema İnfeksiyozum (Beşinci Hastalık - Parvovirus B19).'},
                         {'text': 'Kızamıkçık (Akut Rubella Enfeksiyonu)',
                          'is_correct': False,
                          'scenario_update': 'Muayenede retroauriküler, posterior servikal veya suboksipital '
                                             'ağrılı lenfadenopati saptanmadı ve döküntü dantelvari '
                                             'karakterdeydi.',
                          'teaching_point': 'Rubellada belirgin retroauriküler/suboksipital lenfadenopati ve '
                                            'yüzden başlayıp hızla gövdeye yayılan pembe makülopapüler '
                                            'döküntü görülür; retiküler patern tipik değildir.'},
                         {'text': 'Roseola İnfantum (Altıncı Hastalık)',
                          'is_correct': False,
                          'scenario_update': 'Hasta 7 yaşında olup 3-4 gün süren yüksek ateşin aniden '
                                             'düşmesiyle gövdeden başlayan döküntü öyküsü bulunmamaktadır.',
                          'teaching_point': 'Roseola İnfantum tipik olarak 6 ay - 2 yaş arasında görülür ve '
                                            'birkaç gün süren yüksek ateşin krizle düşmesini takiben gövdede '
                                            'makülopapüler döküntü yapar.'}]},
            {'stage_title': 'Tedavi, İzlem ve Okula Dönüş Kararı',
             'question': 'Aile çocuğun tedavisi ve yarın okula gidip gidemeyeceği konusunda bilgi istiyor. '
                         'En doğru yaklaşım hangisidir?',
             'options': [{'text': 'Döküntü solana kadar 7 gün ev izolasyonu raporu düzenlemek, kaşıntı '
                                  'olmasa da oral antihistaminik ve topikal steroid krem başlamak',
                          'is_correct': False,
                          'scenario_update': 'Bulaştırıcılığı sona ermiş olan çocuk gereksiz yere bir hafta '
                                             'okuldan geri kaldı ve semptomsuz lezyonlara gereksiz topikal '
                                             'steroid uygulandı.',
                          'teaching_point': "Eritema İnfeksiyozum'da döküntü immün kompleks aracılıdır; "
                                            'döküntü çıktığında viremi ve bulaştırıcılık bitmiştir, bu '
                                            'nedenle okuldan izolasyon önerilmez.'},
                         {'text': 'İlaç gerekmediğini, döküntü çıktığında bulaştırıcılığın bittiğini, okula '
                                  'gidebileceğini ve döküntünün sıcakla birkaç hafta tekrarlayabileceğini '
                                  'anlatıp taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Parvovirus B19 enfeksiyonunda bulaştırıcılık döküntü öncesi '
                                         'prodromal dönemdedir; ekzantem evresinde çocuk bulaştırıcı '
                                         'değildir. Sıcak banyo, egzersiz ve güneşle döküntünün 1-3 hafta '
                                         'dalgalanabileceği aileye açıklanmalıdır.',
                          'new_finding': 'Aileye bulaştırıcılığın geçtiği, okula devam edebileceği ve '
                                         'döküntünün sıcak/egzersizle geçici olarak belirginleşebileceği '
                                         'anlatılarak hasta taburcu edildi.'},
                         {'text': 'Viral replikasyonu baskılamak ve eklem komplikasyonlarını önlemek '
                                  'amacıyla 5 gün oral asiklovir süspansiyon başlayıp evde istirahat önermek',
                          'is_correct': False,
                          'scenario_update': 'Başlanan asiklovir tedavisi tek sarmallı DNA virüsü olan '
                                             'Parvovirus B19 üzerinde hiçbir etki göstermedi ve gereksiz '
                                             'ilaç maruziyeti oluşturdu.',
                          'teaching_point': 'Asiklovir yalnızca herpesvirüs ailesine (HSV, VZV) etkilidir; '
                                            'Parvovirus B19 enfeksiyonunda antiviral tedavinin yeri yoktur.'},
                         {'text': 'Çocuğun okula dönüşüne izin vermek ancak sınıfındaki tüm çocuklara ve '
                                  'öğretmenlere profilaktik oral antibiyotik başlanmasını yazılı olarak '
                                  'önermek',
                          'is_correct': False,
                          'scenario_update': 'Okul yönetimi ve veliler arasında gereksiz panik oluştu; viral '
                                             'bir etken için uygunsuz antibiyotik profilaksisi gündeme '
                                             'geldi.',
                          'teaching_point': 'Parvovirus B19 için temaslılara antibiyotik profilaksisi '
                                            'uygulanmaz; yalnızca temaslılar arasında gebe veya kronik '
                                            'hemolitik anemili birey varsa kendi hekimine '
                                            'yönlendirilir.'}]}]},
 {'id': 'G08',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '10 Aylık',
  'gender': 'Kız',
  'complaint': 'Üç gün süren yüksek ateşin düşmesiyle birlikte gövdede çıkan döküntü',
  'history': "Annesi endişeyle anlatıyor: 'Doktor hanım/bey, kızımın 3 gün boyunca 39.5°C'ye varan ateşi "
             'oldu, ateş düşürücüyle düşüp tekrar çıkıyordu ama keyfi ve emmesi fena değildi. Bu sabah ateşi '
             'tamamen düştü, rahatladık; fakat öğleden sonra karnında, göğsünde ve sırtında pembe-kırmızı '
             "lekeler çıktı! Dün verdiğimiz ateş düşürücü şuruptan alerji mi oldu diye çok korktuk.'",
  'final_diagnosis': 'Roseola İnfantum (Altıncı Hastalık / Ekzantema Subitum - HHV-6)',
  'disposition': 'Yeşil Alandan İlaç Alerjisi Olmadığının Anlatılması ve Destek Önerileri ile Taburculuk',
  'case_pearl': 'Altı ay - 2 yaş arası süt çocuklarında 3-4 gün süren yüksek ateşin aniden (kriz şeklinde) '
                'düşmesiyle gövdeden başlayan, kaşıntısız, basmakla solan gül pembesi makülopapüler döküntü '
                'Roseola İnfantum (HHV-6/7) için klasiktir. Sıklıkla ateş döneminde kullanılan antipiretik '
                "veya antibiyotik alerjisi ile karıştırılır; çocuğa yanlışlıkla 'ilaç alerjisi' etiketi "
                'konulmamalıdır.',
  'steps': [{'stage_title': 'Fizik Muayene',
             'question': 'Ateşi düştükten sonra gövdede döküntüsü çıkan bu 10 aylık bebekte ilk muayenede '
                         'neyi değerlendirmelisiniz?',
             'options': [{'text': 'Ateş düşürücüye bağlı erken sistemik alerjik reaksiyon düşünerek hızla '
                                  'uyluktan intramüsküler adrenalin uygulayıp damar yolu açmak',
                          'is_correct': False,
                          'scenario_update': 'Yaşamsal bulguları normal, kaşıntısı veya solunum sıkıntısı '
                                             'olmayan bebekte adrenalin enjeksiyonu sonrası ciddi taşikardi '
                                             've huzursuzluk gelişti.',
                          'teaching_point': 'Ateş düştükten sonra ortaya çıkan, kaşıntısız, ödematöz plak '
                                            'içermeyen ve sistemik bulgunun eşlik etmediği makülopapüler '
                                            'döküntülerde adrenalin endikasyonu yoktur.'},
                         {'text': 'Yaşamsal bulgular, genel görünüm, ön fontanel, yumuşak damaktaki '
                                  'eritematöz papüller ve gövdedeki döküntünün basmakla solma özelliğini '
                                  'değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Üç günlük yüksek ateşin kriz şeklinde düşmesi, bebeğin '
                                         'aktif/huzurlu görünümü ve gövdeden başlayan basmakla solan '
                                         'makülopapüler döküntü karakteristik viral ekzantem seyrini '
                                         'gösterir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.5°C, KTA 115/dk, SS 26/dk. Bebek etrafa '
                                         'gülümsüyor, aktif. Ön fontanel normal bombelikte. Gövde, boyun ve '
                                         'sırt ağırlıklı, basmakla solan 2-5 mm çaplı gül pembesi '
                                         'makülopapüler döküntüler mevcut; peteşi/purpura ve kaşıntı yok. '
                                         'Yumuşak damakta hafif eritematöz papüller izlendi.'},
                         {'text': 'Üç gün süren yüksek ateş ve yeni başlayan döküntüyü santral sinir sistemi '
                                  'enfeksiyonu bulgusu kabul ederek acil lomber ponksiyon hazırlığı yapmak',
                          'is_correct': False,
                          'scenario_update': 'Ateşi tamamen düşmüş, ön fontaneli normal ve gülümseyerek oyun '
                                             'oynayan bebekte invaziv girişim hazırlığı aileyi çok '
                                             'endişelendirdi.',
                          'teaching_point': 'Ateşi krizle düşmüş, genel durumu çok iyi, ön fontaneli normal '
                                            've döküntüsü basmakla solan süt çocuğunda lomber ponksiyon '
                                            'endike değildir.'},
                         {'text': 'Döküntülerin olası bakteriyel sepsis kaynağı olabileceğini düşünerek '
                                  'bebeği Sarı Alana devredip geniş spektrumlu intravenöz antibiyotik '
                                  'hazırlamak',
                          'is_correct': False,
                          'scenario_update': 'Sarı Alana alınan bebeğin kapiller dolumu 1 saniye, ateşi '
                                             '36.5°C ve aktivitesi tam olarak izlendi; toksik görünüm '
                                             'saptanmadı.',
                          'teaching_point': 'Basmakla solan pembe makülopapüler döküntüsü olan, ateşi düşmüş '
                                            've perfüzyonu normal bir süt çocuğunda meningokoksemi veya '
                                            'bakteriyel sepsis düşünülmez.'}]},
            {'stage_title': 'Tetkik İstem Kararı',
             'question': 'Genel durumu çok iyi, ateşi düşmüş ve tipik gövde döküntüsü saptanmış bu bebekte '
                         'hangi tetkik yaklaşımı doğrudur?',
             'options': [{'text': 'Geçirilmiş üç günlük yüksek ateşin gizli bakteriyel odağını dışlamak için '
                                  'tam kan sayımı, CRP, kan kültürü ve mesane sondası ile idrar kültürü '
                                  'almak',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: WBC 5.200/mm³ (%70 lenfosit), CRP 1.9 '
                                             'mg/L, tam idrar tetkiki normal. İyileşme evresindeki bebekte '
                                             'gereksiz invaziv kateterizasyon yapıldı.',
                          'teaching_point': 'Odağı belirsiz ateş döneminde idrar tetkiki önemli olsa da, '
                                            'ateş tamamen düşüp karakteristik viral ekzantem ortaya '
                                            'çıktığında tanı netleşmiştir ve invaziv sepsis taraması '
                                            'yapılmaz.'},
                         {'text': 'Antipiretik ilaç duyarlılığını doğrulamak amacıyla acil serviste '
                                  'parasetamol spesifik IgE, triptaz düzeyi ve oral ilaç provokasyon testi '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'Laboratuvarda parasetamol için rutin spesifik IgE kiti '
                                             'bulunmadığı bildirildi; akut dönemde provokasyon girişimi ise '
                                             'gereksiz zaman kaybına yol açtı.',
                          'teaching_point': 'Ateşin düşmesiyle başlayan kaşıntısız makülopapüler döküntü '
                                            'ilaç reaksiyonu değil, viral enfeksiyonun doğal iyileşme evresi '
                                            'olan ekzantem dönemidir.'},
                         {'text': 'Hiçbir laboratuvar veya görüntüleme tetkiki istemeden tipik klinik seyir '
                                  've fizik muayene bulgularıyla tanı koymak',
                          'is_correct': True,
                          'explanation': 'Üç gün yüksek ateş sonrası ateşin düşmesiyle çıkan karakteristik '
                                         'makülopapüler döküntü evresinde tanı tamamen kliniktir; '
                                         'laboratuvar tetkiki gerekmez.',
                          'new_finding': 'Ek tetkik istenmedi; klinik değerlendirme tanı için yeterli '
                                         'görülerek aile eğitimi aşamasına geçildi.'},
                         {'text': 'Kızamık ve kızamıkçık serolojisi (IgM/IgG) ile boğaz sürüntüsünden '
                                  'solunum yolu viral PCR paneli göndererek sonuç çıkana kadar gözlemde '
                                  'tutmak',
                          'is_correct': False,
                          'scenario_update': 'Seroloji sonuçlarının ertesi gün çıkacağı öğrenildi; bebek '
                                             'acil gözlem odasında gereksiz yere saatlerce bekletildi.',
                          'teaching_point': 'Öksürük, koriza, konjonktivit ve ateş olmadan ateşin düşmesini '
                                            'takiben gövdeden başlayan döküntüde kızamık serolojisi veya '
                                            'acil gözlem yatışı endike değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bu hastada mevcut öykü ve muayene bulgularıyla kesin tanınız nedir?',
             'options': [{'text': 'Roseola İnfantum (Ekzantema Subitum)',
                          'is_correct': True,
                          'explanation': 'Altı ay - 2 yaş arası bebekte 3-4 gün süren yüksek ateşin aniden '
                                         'düşmesi ve hemen ardından gövdeden başlayan kaşıntısız gül pembesi '
                                         "makülopapüler döküntü Roseola İnfantum'un klasik tablosudur.",
                          'new_finding': 'Tanı: Roseola İnfantum (HHV-6 / Altıncı Hastalık).'},
                         {'text': 'Parasetamole Bağlı Makülopapüler İlaç Erüpsiyonu',
                          'is_correct': False,
                          'scenario_update': 'Döküntüde kaşıntı veya eozinofili bulgusu olmadığı, tablonun '
                                             'ateşin krizle düşmesini izleyen klasik viral seyir olduğu '
                                             'doğrulandı.',
                          'teaching_point': 'İlaç erüpsiyonları genellikle kaşıntılıdır, ilacın ilk '
                                            'dozlarından ziyade günler süren duyarlanma sonrası gelişir ve '
                                            'ateşin kriz şeklinde düşmesiyle eş zamanlı tipik viral dizilim '
                                            'göstermez.'},
                         {'text': 'Kızamık (Akut Morbilli Enfeksiyonu)',
                          'is_correct': False,
                          'scenario_update': 'Bebekte döküntü çıktığında ateşin tamamen düştüğü, döküntünün '
                                             'saç çizgisi/kulak arkasından değil gövdeden başladığı ve 3C '
                                             'bulgusunun olmadığı görüldü.',
                          'teaching_point': 'Kızamıkta döküntü çıktığında ateş en yüksek seviyesindedir, '
                                            'çocuk düşkün görünür ve döküntü kulak arkasından başlayıp aşağı '
                                            'yayılır.'},
                         {'text': 'Akut İnvaziv Meningokoksemi Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Döküntülerin basmakla tamamen solduğu (peteşiyal/purpurik '
                                             'olmadığı), bebeğin ateşsiz ve gayet neşeli olduğu teyit '
                                             'edildi.',
                          'teaching_point': 'Meningokoksemide toksik görünüm, dolaşım bozukluğu ve basmakla '
                                            'solmayan peteşiyal/purpurik lezyonlar görülür.'}]},
            {'stage_title': 'Tedavi ve Aile Bilgilendirmesi',
             'question': 'Bu aşamada bebeğin tedavisi ve ailenin ilaç alerjisi endişesi için en doğru '
                         'yaklaşım hangisidir?',
             'options': [{'text': 'İlaç gerekmediğini, tablonun ateş düşürücü alerjisi olmadığını ve '
                                  'döküntülerin birkaç gün içinde iz bırakmadan solacağını anlatarak taburcu '
                                  'etmek',
                          'is_correct': True,
                          'explanation': "Roseola İnfantum'da döküntü çıkışı iyileşme evresini gösterir; "
                                         'hekimin en kritik görevi gereksiz ilaçları önlemek ve çocuğa '
                                         "yanlış 'parasetamol alerjisi' etiketi konulmasının önüne "
                                         'geçmektir.',
                          'new_finding': 'Ailenin ilaç alerjisi endişesi giderildi, ileride parasetamol '
                                         'kullanabilecekleri ve döküntünün 1-3 günde kendiliğinden geçeceği '
                                         'anlatılarak bebek taburcu edildi.'},
                         {'text': "Çocuğun elektronik sağlık kaydına 'Parasetamol Alerjisi' işlemek, beş gün "
                                  'oral setirizin damla ve kısa süreli oral prednizolon reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Yanlış ilaç alerjisi kaydı nedeniyle bebeğin sonraki ateşli '
                                             'hastalıklarında antipiretik kullanımı kısıtlandı ve gereksiz '
                                             'steroid maruziyeti oluştu.',
                          'teaching_point': 'Roseola İnfantum döküntüsünü ilaç alerjisi sanarak çocuğu temel '
                                            'antipiretiklerden mahrum bırakmak sık yapılan bir hatadır; '
                                            'kaşıntısız viral ekzantemde antihistaminik ve steroid '
                                            'verilmez.'},
                         {'text': 'Human Herpesvirus-6 viremisini baskılamak ve febril nöbet riskini önlemek '
                                  'amacıyla 7 gün oral asiklovir veya valasiklovir süspansiyon başlamak',
                          'is_correct': False,
                          'scenario_update': 'Ateşi zaten düşmüş ve iyileşme fazına girmiş olan bebekte '
                                             'etkisiz ve gereksiz antiviral tedavi kullanılmış oldu.',
                          'teaching_point': 'İmmünkompetan çocuklarda Roseola İnfantum kendi kendini '
                                            "sınırlar; hem asiklovir HHV-6'ya karşı etkisizdir hem de "
                                            'döküntü evresinde hastalık zaten iyileşmiştir.'},
                         {'text': 'Döküntülerin sekonder bakteriyel enfeksiyonunu önlemek için topikal '
                                  'mupirosin krem ve 5 gün oral amoksisilin süspansiyon reçete ederek '
                                  'kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Sağlam derideki makülopapüler viral döküntü için verilen oral '
                                             'antibiyotik bebekte antibiyotik ilişkili ishale neden oldu.',
                          'teaching_point': 'Bütünlüğü bozulmamış, vezikül veya krut içermeyen viral '
                                            'makülopapüler döküntülerde topikal veya sistemik '
                                            'antibiyotiklerin hiçbir yeri yoktur.'}]}]},
 {'id': 'G09',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '2.5 Yaş',
  'gender': 'Erkek',
  'complaint': 'Ağız içinde ağrılı yaralar, yemek yemeyi reddetme, avuç içi ve ayak tabanında döküntü',
  'history': "Annesi anlatıyor: 'İki gündür ağzından salyası akıyor, çok sevdiği yemekleri bile ağzına "
             'götürüp ağlayarak bırakıyor. Dün 38.2°C ateşi oldu. Bugün de avuç içlerinde, ayak tabanlarında '
             've bez bölgesinde kırmızı küçük su toplamış döküntüler fark ettik. Su ve soğuk sütü azar azar '
             "içebiliyor, bezini normal ıslatıyor.'",
  'final_diagnosis': 'El-Ayak-Ağız Hastalığı (Enterovirus / Coxsackievirus A16 - A6)',
  'disposition': 'Yeşil Alandan Ağrı Kontrolü, Soğuk/Yumuşak Gıda-Sıvı Desteği ve İzlem ile Taburculuk',
  'case_pearl': 'Oral mukozada ağrılı vezikül/ülserler ve avuç içi, ayak tabanı ile gluteal bölgede eritemli '
                'zeminde eliptik veziküller El-Ayak-Ağız hastalığı için tipiktir. En sık komplikasyonu '
                'ağrılı oral lezyonlara bağlı yutma güçlüğü ve dehidratasyondur; tedavide sistemik analjezi '
                've soğuk/asitsiz sıvılarla hidrasyonun sürdürülmesi esastır.',
  'steps': [{'stage_title': 'Fizik Muayene ve Hidrasyon Kontrolü',
             'question': 'Bu hastada ilk fizik muayenede öncelikle hangi bulguları değerlendirmelisiniz?',
             'options': [{'text': 'Ağız içindeki vezikülleri abeslangla kazıyarak psödomembran varlığını '
                                  'kontrol etmek ve avuç içindeki lezyonları steril iğneyle drene etmek',
                          'is_correct': False,
                          'scenario_update': 'Ağrılı oral ülserlere yapılan mekanik müdahale mukozal '
                                             'kanamaya ve çocuğun şiddetli ağlayarak ağızdan sıvı alımını '
                                             'tamamen reddetmesine yol açtı.',
                          'teaching_point': 'Oral mukozadaki viral vezikül ve ülserler kesinlikle kazınmaz, '
                                            'akral derideki veziküller ise sekonder bakteriyel enfeksiyon '
                                            'riski nedeniyle patlatılmaz.'},
                         {'text': 'Akral yerleşimli lezyonları bakteriyel septik emboli veya invaziv döküntü '
                                  'kabul ederek hastayı hızla Sarı Alana devredip damar yolu açmak',
                          'is_correct': False,
                          'scenario_update': 'Sarı Alana alınan çocuğun yaşamsal bulguları ve kapiller '
                                             'dolumu tamamen normal bulundu; lezyonların purpurik değil '
                                             'gri-beyaz veziküller olduğu görüldü.',
                          'teaching_point': 'Genel durumu iyi olan çocukta oral ülserlere eşlik eden avuç '
                                            'içi, ayak tabanı ve gluteal eliptik veziküller tipik viral '
                                            'enantem-ekzantem kompleksidir.'},
                         {'text': 'Orofarenks ve bukkal mukozadaki ülserleri, avuç içi-ayak tabanı-gluteal '
                                  'vezikülleri, hidrasyon durumunu ve miyokloni/ataksi gibi nörolojik '
                                  'bulguları değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Karakteristik oral ve akral vezikül dağılımı tanıyı yönlendirir; '
                                         'ağrılı yutma nedeniyle hidrasyon durumu ve nadir santral sinir '
                                         'sistemi tutulumu bulguları mutlaka kontrol edilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 37.9°C, KTA 116/dk, SS 24/dk. Dil, bukkal '
                                         'mukoza ve yumuşak damakta eritemli haleli 3-4 mm ağrılı vezikül ve '
                                         'ülserler mevcut. Avuç içlerinde, ayak tabanlarında ve gluteal '
                                         'bölgede eliptik gri-beyaz vezikülopapüler lezyonlar var. Ağız '
                                         'mukozası nemli, gözyaşı var, dehidratasyon yok. Nörolojik muayene '
                                         'doğal.'},
                         {'text': 'Ağız içi muayeneyi çocuğun ağlamasını artırmamak için tamamen atlayıp '
                                  'yalnızca sırt ve gövde derisinde polimorfik döküntü aramak',
                          'is_correct': False,
                          'scenario_update': 'Sırt ve göğüste döküntü saptanmadı; ağız içi ve mukoza '
                                             'ıslaklığı değerlendirilmediği için beslenme reddi nedeni ve '
                                             'hidrasyon durumu eksik kaldı.',
                          'teaching_point': 'Salya artışı ve beslenme reddi ile başvuran küçük çocukta '
                                            'orofarenks lezyonlarının ve mukoza nemliliğinin görülmesi temel '
                                            'muayene basamağıdır.'}]},
            {'stage_title': 'Tetkik İstem Kararı',
             'question': 'Dehidratasyonu ve nörolojik bulgusu olmayan, tipik oral-akral vezikülleri saptanan '
                         'bu çocukta hangi tetkik yaklaşımı seçilmelidir?',
             'options': [{'text': 'Avuç içindeki vezikül tabanından kazıntı alarak Tzanck yayması, Herpes '
                                  'Simpleks PCR ve Varisella Zoster IgM serolojisi istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: Tzanck yaymasında multinükleer dev hücre '
                                             'görülmedi, HSV ve VZV testleri negatif sonuçlandı; işlem '
                                             'çocuğu gereksiz travmatize etti.',
                          'teaching_point': 'Oral ülser ve avuç içi/ayak tabanı/gluteal eliptik vezikül '
                                            'birlikteliği klinik olarak tanı koydurucudur; rutin Tzanck '
                                            'yayması veya herpes serolojisi istenmez.'},
                         {'text': 'Orofarenksteki lezyonlar nedeniyle bakteriyel tonsillofarenjiti dışlamak '
                                  'üzere hızlı streptokok antijen testi ve boğaz kültürü almak',
                          'is_correct': False,
                          'scenario_update': 'Hızlı antijen testi negatif çıktı; ülserli bukkal mukoza ve '
                                             'dile sürüntü çubuğu değdirilmesi şiddetli ağrıya neden oldu.',
                          'teaching_point': 'Ön oral kavitede (dil, bukkal mukoza) vezikül-ülserler ve '
                                            'el-ayak lezyonları ile seyreden tabloda bakteriyel boğaz '
                                            'kültürü endikasyonu yoktur.'},
                         {'text': 'Yemek yemeyi reddettiği için klinik dehidratasyon bulgusu olmasa bile '
                                  'rutin kan gazı, serum elektrolitleri, üre ve kreatinin istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: Na 137 mEq/L, K 4.2 mEq/L, Glukoz 86 '
                                             'mg/dL, Üre 19 mg/dL, pH 7.40. Tüm değerler normal geldi.',
                          'teaching_point': 'Sıvı alabilen, idrar çıkışı normal olan ve fizik muayenede '
                                            'dehidratasyon bulgusu saptanmayan çocukta rutin venöz biyokimya '
                                            'tetkiki gerekmez.'},
                         {'text': 'Ek laboratuvar tetkiki istemeden tipik anatomik lezyon dağılımı ve normal '
                                  'hidrasyon bulgularıyla klinik tanı koymak',
                          'is_correct': True,
                          'explanation': 'Oral mukozada vezikül/ülserler ve akral-gluteal vezikülopapüler '
                                         'döküntü karakteristik bir klinik sendromdur; komplike olmayan '
                                         'vakalarda laboratuvar testi önerilmez.',
                          'new_finding': 'Tetkik istenmedi; acil serviste çocuğun soğuk sütü yudumlayarak '
                                         'kusmadan tolere edebildiği gözlendi.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bu hastada mevcut bulgularla kesin tanınız nedir?',
             'options': [{'text': 'Primer Herpetik Gingivostomatit',
                          'is_correct': False,
                          'scenario_update': 'Hastanın diş etlerinde yaygın hiperemi, şişlik veya kolay '
                                             'kanama (gingivit) olmadığı; buna karşın el, ayak ve gluteal '
                                             'veziküllerin bulunduğu görüldü.',
                          'teaching_point': 'Herpetik gingivostomatitte yüksek ateş, belirgin diş eti '
                                            'ödemi/kanaması ve perioral veziküller ön plandadır; avuç içi, '
                                            'ayak tabanı ve gluteal vezikül beklenmez.'},
                         {'text': 'Suçiçeği (Varisella Enfeksiyonu)',
                          'is_correct': False,
                          'scenario_update': 'Saçlı deri ve gövdede farklı evrelerde (makül, papül, vezikül, '
                                             'krut bir arada) kaşıntılı santripetal döküntü saptanmadı.',
                          'teaching_point': 'Suçiçeğinde döküntü saçlı deri ve gövdeden başlar (merkezden '
                                            'perifere yayılır) ve polimorfiktir; avuç içi ve ayak tabanı '
                                            'tutulumu nadirdir.'},
                         {'text': 'El-Ayak-Ağız Hastalığı',
                          'is_correct': True,
                          'explanation': 'Oral vezikül/ülserler ile avuç içi, ayak tabanı ve gluteal '
                                         'bölgedeki eliptik veziküller enteroviral El-Ayak-Ağız hastalığını '
                                         'doğrular.',
                          'new_finding': 'Tanı: El-Ayak-Ağız Hastalığı (Enteroviral veziküler stomatit ve '
                                         'ekzantem).'},
                         {'text': 'Akut Herpangina (İzole Faringeal Enantem)',
                          'is_correct': False,
                          'scenario_update': 'Hastada yalnızca arka farenks/tonsiller plikada sınırlı '
                                             'lezyonlar değil, aynı zamanda el ayası, ayak tabanı ve gluteal '
                                             'bölgede veziküller mevcut.',
                          'teaching_point': 'Yine enterovirüslerin neden olduğu herpanginada vezikül ve '
                                            'ülserler yalnızca yumuşak damak, uvula ve ön tonsiller '
                                            'plikalarda yer alır; el ve ayak döküntüsü bulunmaz.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu hastada ağrı yönetimi, beslenme ve taburculuk için en doğru yaklaşım '
                         'hangisidir?',
             'options': [{'text': 'Beslenmeden 30 dakika önce sistemik analjezik, soğuk-yumuşak-asitsiz '
                                  'gıdalar, bol sıvı desteği ve kırmızı bayrak eğitimi ile taburcu etmek',
                          'is_correct': True,
                          'explanation': 'El-Ayak-Ağız hastalığında spesifik antiviral yoktur; öğün öncesi '
                                         'sistemik analjezi ve soğuk/nötr gıdalar (yoğurt, soğuk süt, püre) '
                                         'oral ağrıyı azaltarak dehidratasyonu önler.',
                          'new_finding': 'Sistemik analjezik ve soğuk/yumuşak beslenme planı düzenlendi; '
                                         'idrar azalması, uykuya meyil veya sıçrama/dengesizlik olursa '
                                         'başvuru eğitimi ve haftalar sonra tırnak değişimi (onikomadezis) '
                                         'olabileceği bilgisi verilerek taburcu edildi.'},
                         {'text': 'Oral asiklovir süspansiyon ve sekonder enfeksiyon profilaksisi için '
                                  'amoksisilin başlamak, yemeklerden önce ağız içine yoğun topikal lidokain '
                                  'sprey sıkmak',
                          'is_correct': False,
                          'scenario_update': 'Asiklovir ve antibiyotik enterovirüslere etki etmedi; 2.5 '
                                             'yaşındaki çocukta yutulan topikal lidokain öğürme refleksini '
                                             'baskıladı ve sistemik toksisite riski yarattı.',
                          'teaching_point': 'Enterovirüslere asiklovir veya antibiyotik etki etmez; küçük '
                                            'çocuklarda oral topikal lidokain (konvülziyon, aritmi ve '
                                            'aspirasyon riski nedeniyle) kesinlikle önerilmez.'},
                         {'text': 'Bağışıklığı güçlendirmek amacıyla bol taze sıkılmış portakal-limon suyu '
                                  've sıcak kemik suyu çorbası içirilmesini önerip analjezik vermeden '
                                  'taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Asitli narenciye suları ve sıcak çorba ülserli oral mukozada '
                                             'şiddetli yanma yaptığı için çocuk ağızdan sıvı alımını tamamen '
                                             'kesti.',
                          'teaching_point': 'Oral mukoza ülserlerinde asitli, tuzlu, baharatlı ve sıcak '
                                            'gıda/içecekler ağrıyı şiddetlendirir; soğuk veya oda ısısında '
                                            'nötr sıvılar tercih edilmelidir.'},
                         {'text': 'Oral ülserlerin iyileşmesini hızlandırmak için 5 gün oral prednizolon '
                                  'şurup başlamak ve el-ayak veziküllerine potasyum permanganatlı sıcak '
                                  'banyo uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Kortikosteroid kullanımı akut enteroviral enfeksiyon seyrinde '
                                             'mukozal iyileşmeyi sağlamadığı gibi viral replikasyon '
                                             'açısından risk oluşturdu.',
                          'teaching_point': 'Komplike olmayan El-Ayak-Ağız hastalığında sistemik '
                                            'kortikosteroidler kontrendikedir; veziküller kendi kendine '
                                            'kuruyup iyileşir.'}]}]},
 {'id': 'G10',
  'category': '🫁 Hırıltı & Solunum Sıkıntısı',
  'age': '10 Yaş',
  'gender': 'Erkek',
  'complaint': 'Üç haftadır özellikle gece yatınca ve sabah kalkınca artan öksürük, burun tıkanıklığı ve '
               'geniz akıntısı',
  'history': "Hasta kendisi anlatıyor: 'Doktor bey/hanım, gündüz okulda pek öksürmüyorum ama akşam yastığa "
             'başımı koyunca ve sabah uyanınca boğazımda bir şey gıdıklanıyor gibi öksürüyorum, sürekli '
             'boğazımı temizleme ihtiyacı hissediyorum. Burnum da çok kaşınıyor ve sabahları üst üste '
             'hapşırıyorum. Ateşim hiç çıkmadı, beden eğitimi dersinde koşarken nefesim daralmıyor veya '
             "göğsümden ıslık sesi gelmiyor.'",
  'final_diagnosis': 'Alerjik Rinit ve Postnazal Akıntı Sendromuna (Üst Hava Yolu Öksürük Sendromu) Bağlı '
                     'Öksürük',
  'disposition': 'Yeşil Alandan İntranazal Kortikosteroid / Antihistaminik ve Alerjen Önlemleri ile '
                 'Taburculuk',
  'case_pearl': 'Ateşsiz, özellikle yatınca ve sabah kalkınca belirginleşen, boğaz temizleme hareketi, burun '
                'kaşıntısı ve hapşırığın eşlik ettiği öksürüklerde en sık neden Alerjik Rinit ve buna bağlı '
                'Postnazal Akıntıdır. Orta-ağır veya persistan semptomlarda en etkili birinci basamak '
                'antiinflamatuar tedavi intranazal kortikosteroid spreylerdir.',
  'steps': [{'stage_title': 'Odaklı Fizik Muayene',
             'question': 'Pozisyonel öksürük ve burun semptomları ile başvuran bu çocukta fizik muayenede '
                         'öncelikle hangi bulguları aramalısınız?',
             'options': [{'text': 'Üç haftayı bulan öksürük nedeniyle üst hava yolu muayenesini atlayıp '
                                  'yalnızca bazal akciğer oskültasyonu ve parmaklarda çomaklaşma kontrolü '
                                  'yapmak',
                          'is_correct': False,
                          'scenario_update': 'Akciğer oskültasyonu tamamen normal saptandı; ancak burun '
                                             'boşluğu ve orofarenks arka duvarı incelenmediği için öksürüğün '
                                             'asıl anatomik kaynağı gözden kaçtı.',
                          'teaching_point': 'Yatınca ve sabah uyanınca artan, boğaz temizleme ile '
                                            'karakterize öksürüklerde rinoskopik muayene ve arka farenks '
                                            'duvarı değerlendirmesi atlanmamalıdır.'},
                         {'text': 'Nazal konkalarda soluk-mavimsi ödem, burun sırtında yatay çizgi, arka '
                                  'farenkste kaldırım taşı görünümü ve akciğer seslerini değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Kronik burun kaşıntısı ve geniz akıntısı yakınmalarında '
                                         'soluk-ödemli nazal konkalar ve arka farenks duvarında lenfoid '
                                         'folikül hipertrofisi (kaldırım taşı görünümü) tanısal anahtardır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 82/dk, SS 16/dk, SpO2 %99. Burun '
                                         'sırtında enine katlantı izi, rinoskopide bilateral alt konkalar '
                                         'soluk-mavimsi ve ödemli, berrak sekresyon mevcut. Orofarenks arka '
                                         'duvarında mukoid akıntı ve lenfoid folikül hipertrofisi (kaldırım '
                                         'taşı görünümü) var. Akciğer oskültasyonu tamamen doğal, '
                                         'ral/ronküs/wheezing yok.'},
                         {'text': 'Gece öksürüğünü alt hava yolu obstrüksiyonu kabul ederek muayene '
                                  'öncesinde 3 doz nebülize salbutamol verip oskültasyon yanıtını '
                                  'değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Bronkodilatör nebülizasyon sonrası hastada taşikardi ve el '
                                             'titremesi gelişti; hışıltısı olmayan hastanın geniz akıntısı '
                                             've boğaz gıdıklanması hissinde değişiklik olmadı.',
                          'teaching_point': 'Efor dispnesi, hışıltı veya ekspiratuar uzaması olmayan, '
                                            'yalnızca yatınca geniz akıntısıyla öksüren hastada ampirik '
                                            'bronkodilatör yüklemesi uygun değildir.'},
                         {'text': 'Yabancı cisim aspirasyonu veya endobronşiyal kitleyi dışlamak için '
                                  'hastayı aç bırakıp acil fleksibl bronkoskopi açısından çocuk göğüs '
                                  'hastalıklarına danışmak',
                          'is_correct': False,
                          'scenario_update': 'Ani boğulma öyküsü olmayan, bilateral solunum sesleri eşit ve '
                                             'doğal saptanan çocukta invaziv bronkoskopi endikasyonu '
                                             'bulunmadı.',
                          'teaching_point': 'Ani başlangıçlı boğulma öyküsü, asimetrik solunum sesi veya '
                                            'fokal oskültasyon bulgusu olmayan üst hava yolu kaynaklı '
                                            'öksürükte bronkoskopi düşünülmez.'}]},
            {'stage_title': 'Tetkik İstem Kararı',
             'question': 'Rinoskopi ve orofarenks bulguları tipik, akciğer oskültasyonu tamamen doğal olan '
                         'bu hastada acil serviste hangi tetkik gerekir?',
             'options': [{'text': 'Paranazal sinüslerin durumunu ve akciğer parankimini görüntülemek '
                                  'amacıyla Waters sinüs grafisi, PA akciğer grafisi ve sinüs BT istemek',
                          'is_correct': False,
                          'scenario_update': 'GÖRÜNTÜLEME SONUCU: PA akciğer grafisi normal; sinüs '
                                             'görüntülemesinde yalnızca bilateral alt konka hipertrofisi ve '
                                             'hafif mukozal kalınlaşma izlendi.',
                          'teaching_point': 'Pürülan akıntı, ateş veya yüz ağrısı olmayan berrak sekresyonlu '
                                            'mukozal ödem tablosunda rutin radyografi veya sinüs tomografisi '
                                            'endike değildir; gereksiz radyasyon verir.'},
                         {'text': 'Atipik bakteriyel enfeksiyon ve boğmaca olasılığını dışlamak için tam kan '
                                  'sayımı, CRP, Mycoplasma IgM ve nazofaringeal Bordetella PCR istemek',
                          'is_correct': False,
                          'scenario_update': 'LABORATUVAR SONUCU: WBC 6.800/mm³, CRP 0.8 mg/L; seroloji ve '
                                             'PCR sonuçlarının günler sonra çıkacağı bildirildi.',
                          'teaching_point': "Boğulur tarzda paroksismal öksürük nöbeti, inspiratuar 'whoop' "
                                            'sesi, kusma veya ateş olmayan, tipik nazal kaşıntı/hapşırıkla '
                                            'seyreden tabloda enfeksiyon tetkiki istenmez.'},
                         {'text': 'Acil serviste solunum fonksiyon testi (spirometri), fraksiyone ekshale '
                                  'nitrik oksit (FeNO) ve geniş aeroalerjen deri prick testi uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Acil servis koşullarında spirometri ve deri prick testi '
                                             'yapılamadı; hastanın taburculuğu gereksiz yere gecikti.',
                          'teaching_point': 'İleri alerji deri testleri ve solunum fonksiyon ölçümleri acil '
                                            'servis tetkiki değildir; gerektiğinde çocuk alerji '
                                            'polikliniğinde planlanır.'},
                         {'text': 'Acil serviste ek laboratuvar veya görüntüleme tetkiki istemeden mevcut '
                                  'öykü ve rinoskopik muayene bulgularıyla klinik tanı koymak',
                          'is_correct': True,
                          'explanation': 'Tipik pozisyonel öksürük, burun kaşıntısı, soluk-ödemli nazal '
                                         'konkalar ve normal akciğer oskültasyonu varlığında tanı kliniktir; '
                                         'acil serviste ek tetkik gerekmez.',
                          'new_finding': 'Gereksiz radyasyon ve kan tetkikinden kaçınılarak klinik '
                                         'bulgularla tanı ve tedavi planına geçildi.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Bu hastada mevcut anamnez ve fizik muayene bulgularıyla en doğru klinik tanı '
                         'nedir?',
             'options': [{'text': 'Alerjik Rinit ve Postnazal Akıntı',
                          'is_correct': True,
                          'explanation': 'Sabah hapşırıkları, burun kaşıntısı, soluk-mavimsi ödemli '
                                         'konkalar, arka farenkste kaldırım taşı görünümü ve yatınca artan '
                                         'öksürük Alerjik Rinit ve Postnazal Akıntı Sendromunu (Üst Hava '
                                         'Yolu Öksürük Sendromu) doğrular.',
                          'new_finding': 'Tanı: Alerjik Rinit ve Postnazal Akıntıya Bağlı Öksürük.'},
                         {'text': 'Öksürük Varyant Bronşiyal Astım Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Hastanın öksürüğünün kuru/egzersizle tetiklenen karakterde '
                                             'olmadığı, belirgin burun tıkanıklığı ve görünür postnazal '
                                             'mukoid akıntıya sekonder geliştiği değerlendirildi.',
                          'teaching_point': 'Öksürük varyant astımda egzersiz, soğuk hava veya gülme ile '
                                            'tetiklenen kuru öksürük ön plandadır; belirgin postnazal '
                                            'sekresyon ve faringeal kaldırım taşı görünümü üst hava yolu '
                                            'kaynağını gösterir.'},
                         {'text': 'Akut Bakteriyel Rinosinüzit Enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Hastada pürülan sarı-yeşil burun akıntısı, ateş, yüz/diş '
                                             "ağrısı veya 'çift hastalanma' öyküsü bulunmamaktadır.",
                          'teaching_point': 'Akut bakteriyel rinosinüzitte 10 günü aşan pürülan nazal '
                                            'akıntı, yüksek ateş (≥39°C) veya başlangıçtaki iyileşmeyi '
                                            'izleyen klinik kötüleşme görülür.'},
                         {'text': 'Uzamış Bakteriyel Bronşit Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Hastanın öksürüğünün 4 haftayı aşan sürekli balgamlı (ıslak) '
                                             'karakterde olmadığı, gündüzleri olmayıp yalnızca yatınca geniz '
                                             'akıntısıyla tetiklendiği doğrulandı.',
                          'teaching_point': 'Uzamış bakteriyel bronşitte >4 hafta süren, pozisyondan '
                                            'bağımsız devamlı ıslak/prodüktif öksürük vardır ve 2 haftalık '
                                            'uygun antibiyoterapiye yanıt verir.'}]},
            {'stage_title': 'Tedavi ve Taburculuk Planı',
             'question': 'Bu hastada semptomları kontrol altına almak için en uygun tedavi ve izlem planı '
                         'hangisidir?',
             'options': [{'text': 'İki hafta boyunca günde 3 kez topikal oksimetazolin nazal sprey ve gece '
                                  'öksürüğü için dekstrometorfan şurup reçete ederek taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Beş günden uzun süre topikal oksimetazolin kullanan çocukta '
                                             'şiddetli rebound burun tıkanıklığı (rinitis medikamentoza) '
                                             'gelişti ve öksürük kesilmedi.',
                          'teaching_point': 'Topikal alfa-adrenerjik nazal dekongestanlar 3-5 günden uzun '
                                            'kullanıldığında rinitis medikamentozaya yol açar; alerjik '
                                            'rinitin idame tedavisinde yeri yoktur.'},
                         {'text': 'İntranazal kortikosteroid sprey, ikinci kuşak oral antihistaminik, serum '
                                  'fizyolojik nazal yıkama ve alerjen önlemleri ile taburcu etmek',
                          'is_correct': True,
                          'explanation': 'ARIA kılavuzuna göre orta-ağır veya persistan alerjik rinit ve '
                                         'postnazal akıntıda en etkili tedavi intranazal kortikosteroid '
                                         'sprey (örn. mometazon/flutikazon), nazal serum fizyolojik lavajı '
                                         've ikinci kuşak oral H1-antihistaminiktir.',
                          'new_finding': 'Doğru intranazal sprey kullanım tekniği (nazal septuma değil '
                                         'lateral duvara/aynı taraf kulak yönüne doğru) uygulamalı '
                                         'gösterilerek ve reçetesi düzenlenerek hasta taburcu edildi.'},
                         {'text': 'Geniz akıntısını kurutmak amacıyla 14 gün oral amoksisilin-klavulanat ve '
                                  'birinci kuşak sedatif antihistaminik (klorfeniramin) kombinasyonu '
                                  'başlamak',
                          'is_correct': False,
                          'scenario_update': 'Antibiyotik alerjik mukozal ödemi düzeltmedi; birinci kuşak '
                                             'antihistaminik ise gündüz okul başarısını düşüren sedasyon ve '
                                             'sekresyonlarda koyulaşma yaptı.',
                          'teaching_point': 'Alerjik rinit ve postnazal akıntıda antibiyotik endikasyonu '
                                            'yoktur; birinci kuşak antihistaminikler antikolinerjik '
                                            'etkileriyle sekresyonu koyulaştırıp sedasyon yaptığı için '
                                            'tercih edilmez.'},
                         {'text': 'İntranazal tedavi vermeden doğrudan yüksek doz inhale flutikazon ve '
                                  'gerektiğinde salbutamol inhaler başlayıp üç ay sonra kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Alt hava yoluna yönelik inhaler tedavi burun mukozasındaki '
                                             'alerjik inflamasyonu etkilemediği için hastanın burun '
                                             'tıkanıklığı ve geniz akıntısı devam etti.',
                          'teaching_point': 'Astım bulgusu olmayan izole üst hava yolu öksürük sendromunda '
                                            'ağızdan kullanılan bronşiyal inhalerler değil, nazal mukozaya '
                                            'yönelik intranazal kortikosteroid sprey kullanılmalıdır.'}]}]}]
