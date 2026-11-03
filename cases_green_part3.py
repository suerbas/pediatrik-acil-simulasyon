# -*- coding: utf-8 -*-
GREEN_CASES_PART3 = [{'id': 'G21',
  'category': '👶 Ağlayan, Emmeyen, Huzursuz Bebek',
  'age': '18 Aylık',
  'gender': 'Erkek',
  'complaint': 'Halsizlik, iştahsızlık, solukluk ve yabancı maddeleri yeme isteği',
  'history': "On sekiz aylık erkek çocuğu annesi polikliniğe getiriyor: 'Oğlum son bir aydır eskisi gibi "
             'koşup oynamıyor, çabuk yoruluyor ve sürekli kucak istiyor. İştahı çok azaldı, katı gıdaları '
             'neredeyse hiç yemiyor; günde bir litreden fazla inek sütü biberonla içiyor. Ayrıca son iki '
             'haftadır saksıdaki toprağı ve yerdeki kağıt parçalarını ağzına götürürken yakalıyorum. Ten '
             "rengi de sanki giderek beyazlaştı.'",
  'final_diagnosis': 'Aşırı İnek Sütü Tüketimine Bağlı Demir Eksikliği Anemisi',
  'disposition': 'Yeşil Alandan Oral Demir Tedavisi, Beslenme Düzenlemesi ve Poliklinik Kontrolü ile '
                 'Taburculuk',
  'case_pearl': "Süt çocukluğu döneminde günlük 500 mL'nin üzerinde inek sütü tüketimi hem mikrovasküler "
                'intestinal kanamaya yol açarak gizli kan kaybına neden olur hem de biyoyararlanımı '
                'düşürerek demir eksikliği anemisi gelişimini tetikler. Tedavide oral elementer demir 3-6 '
                'mg/kg/gün bölünmüş dozda başlanmalı, inek sütü günde 400-500 mL ile sınırlandırılmalıdır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Halsizlik, iştahsızlık ve pika öyküsüyle getirilen bu çocukta ilk muayene '
                         'yaklaşımınız hangisi olmalıdır?',
             'options': [{'text': 'Hastayı acilen monitörize alana alıp periferik damar yolu açarak '
                                  'hidrasyon ve parenteral beslenme amacıyla hemen Sarı Alana devretmek',
                          'is_correct': False,
                          'scenario_update': 'Sarı Alanda hastanın vital bulgularının tamamen stabil olduğu '
                                             'görüldü; damar yolu açılması çocuğu aşırı ajite etti.',
                          'teaching_point': 'Genel durumu stabil, dehidratasyon veya dekompansasyon bulgusu '
                                            'olmayan ve aktif kanaması bulunmayan hastalar Yeşil Alanda '
                                            'değerlendirilir.'},
                         {'text': 'Vital bulguları ölçmek, konjonktiva ve derideki solukluğu incelemek, '
                                  'kardiyak üfürüm varlığını mezokardiyak odakta dikkatle oskülte etmek',
                          'is_correct': True,
                          'explanation': 'Kronik hematolojik yetersizliklerde doku hipoksisine bağlı '
                                         'kompansatuar taşikardi ve hiperdinamik sistolik üfürüm '
                                         'gelişebilir; genel perfüzyon dikkatle incelenmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 122/dk, SS 24/dk, SpO2 %99, KB '
                                         '92/58 mmHg. Genel durumu sakin, konjonktivalar ve avuç içleri '
                                         'belirgin soluk. Kalp oskültasyonunda mezokardiyak odakta 2/6 '
                                         'dereceden sistolik üfürüm duyuldu, periferik nabızlar dolgun. '
                                         'Organomegali saptanmadı.'},
                         {'text': 'Ağızdan toprak ve kağıt parçaları yeme davranışı nedeniyle genel fizik '
                                  'muayeneyi kısa tutup hastayı doğrudan çocuk psikiyatrisi polikliniğine '
                                  'sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'Psikiyatri polikliniğine yönlendirilen ailenin fiziksel '
                                             'muayenesi eksik kaldı ve çocuğun belirgin solukluğu ile '
                                             'üfürümü gözden kaçtı.',
                          'teaching_point': 'Küçük çocuklarda yabancı cisim yeme (pika) davranışı öncelikle '
                                            'nutrisyonel eksikliklerin organik bir belirtisi olarak '
                                            'araştırılmalıdır.'},
                         {'text': 'Aşırı süt alımı öyküsü nedeniyle batın muayenesine yoğunlaşıp karın '
                                  'ağrısı veya akut batın bulgularını ekarte etmeyi öncelikli hedef seçmek',
                          'is_correct': False,
                          'scenario_update': 'Batın muayenesinde defans veya hassasiyet saptanmadı; ancak '
                                             'hastanın genel halsizliği ve mukozal solukluğu sistematik '
                                             'olarak değerlendirilmemiş oldu.',
                          'teaching_point': 'Aşırı inek sütü tüketimi tek başına akut batın tablosuna yol '
                                            'açmaz; solukluk ve kardiyovasküler kompansasyon bulguları '
                                            'öncelikle taranmalıdır.'}]},
            {'stage_title': 'Tetkik ve Yaklaşım Kararı',
             'question': 'Fizik muayenesinde belirgin solukluk ve sistolik üfürüm saptanan bu çocukta ilk '
                         'basamakta hangi tetkik istenmelidir?',
             'options': [{'text': 'Pika semptomu ve derin halsizlik nedeniyle ilk basamakta doğrudan kemik '
                                  'iliği aspirasyonu ve kapsamlı genetik enzim paneli tetkiki planlamak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz invaziv işlem önerisi aileyi paniğe sevk etti ve '
                                             'poliklinik şartlarında gereksiz ileri tetkik maliyeti oluştu.',
                          'teaching_point': 'Nutrisyonel kaynaklı şüpheli tablolarda ilk basamakta invaziv '
                                            'tetkikler yerine tam kan sayımı ve eritrosit indeksleri '
                                            'yeterlidir.'},
                         {'text': 'Oskültasyonda sistolik ejeksiyon üfürümü duyulduğu için '
                                  'elektrokardiyografi çekip ileri kardiyak değerlendirme ve ekokardiyografi '
                                  'incelemesi amacıyla hastayı çocuk kardiyolojisine sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'EKG normal sinüs ritmi ve taşikardi gösterdi; kardiyoloji '
                                             'konsültasyonunda üfürümün hiperdinamik akıma bağlı masum '
                                             'üfürüm olduğu belirtildi.',
                          'teaching_point': 'Belirgin solukluğu olan çocuklarda duyulan sistolik fonksiyonel '
                                            'üfürümlerde ilk aşama kardiyak görüntüleme değil hematolojik '
                                            'değerlendirmedir.'},
                         {'text': 'Eritrosit indeksleri, hemoglobin, hematokrit ve eritrosit dağılım '
                                  'genişliğini içeren tam kan sayımı ile periferik yayma tetkiki istemek',
                          'is_correct': True,
                          'explanation': 'Hemoglobin düzeyi, ortalama eritrosit hacmi (MCV) ve eritrosit '
                                         'dağılım genişliği (RDW) tablonun ağırlığını ve morfolojisini '
                                         'ortaya koyar.',
                          'new_finding': 'Laboratuvar Bulguları: Hemoglobin 7.1 g/dL, Hematokrit %22.4, MCV '
                                         '58 fL (düşük), MCH 19 pg, RDW %19.8 (belirgin yüksek), WBC '
                                         '8.400/mm³, Trombosit 460.000/mm³. Periferik yaymada eritrositlerde '
                                         'belirgin hipokromi, anizositoz ve poikilositoz izlendi.'},
                         {'text': 'Toprak yeme öyküsü olduğundan kurşun maruziyetini araştırmak üzere ayakta '
                                  'direkt batın grafisi çekilmesini ve tam idrar tahlili yapılmasını istemek',
                          'is_correct': False,
                          'scenario_update': 'Batın grafisinde radyoopak yabancı cisim görülmedi ve idrar '
                                             'tetkiki doğal çıktı; ancak solukluğun derecesi '
                                             'aydınlatılamadı.',
                          'teaching_point': 'Pika öyküsünde kurşun maruziyeti bir komplikasyon olabilse de '
                                            'hastanın belirgin solukluğu öncelikle tam kan sayımıyla '
                                            'değerlendirilir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Öykü, fizik muayene ve laboratuvar bulguları bir arada değerlendirildiğinde en '
                         'olası klinik tanınız nedir?',
             'options': [{'text': 'Talasemi Minör (Akdeniz Kansızlığı Taşıyıcılığı)',
                          'is_correct': False,
                          'scenario_update': 'Talasemi taşıyıcılığında genellikle RDW normaldir ve Mentzer '
                                             "indeksi 13'ün altındadır; hastamızda ise RDW yüksek ve Mentzer "
                                             'indeksi 15.8 hesaplandı.',
                          'teaching_point': 'Talasemi minörde eritrosit sayısı yüksek, RDW normal veya hafif '
                                            'yüksek ve Mentzer indeksi (MCV/RBC) < 13 iken, demir '
                                            'eksikliğinde RDW belirgin yüksektir ve Mentzer > 13 saptanır.'},
                         {'text': 'Demir Eksikliği Anemisi',
                          'is_correct': True,
                          'explanation': 'Aşırı inek sütü tüketimi, pika, düşük MCV, yüksek RDW ve reaktif '
                                         'trombositoz demir eksikliği anemisini güçlü şekilde destekler.',
                          'new_finding': 'Tanı Demir Eksikliği Anemisi olarak teyit edildi; eşzamanlı '
                                         'bakılan serum ferritin düzeyi 4 ng/mL (çok düşük) olarak '
                                         'sonuçlandı.'},
                         {'text': 'Kronik Hastalık Anemisi',
                          'is_correct': False,
                          'scenario_update': 'Hastanın öyküsünde kronik inflamatuar, romatizmal veya '
                                             'enfeksiyöz bir hastalık bulunmamaktadır; ferritin düzeyi düşük '
                                             'beklenir.',
                          'teaching_point': 'Kronik hastalık anemisinde ferritin normal veya yüksektir ve '
                                            'demir bağlama kapasitesi azalmıştır; hastanın öyküsü besinsel '
                                            'eksiklikle uyumludur.'},
                         {'text': 'Kurşun Zehirlenmesine Bağlı Sideroblastik Anemi',
                          'is_correct': False,
                          'scenario_update': 'Periferik yaymada bazofilik noktalanma izlenmedi ve hastanın '
                                             'tablosunu açıklayan birincil neden nutrisyonel yetersizliktir.',
                          'teaching_point': 'Pikaya sekonder kurşun maruziyeti gelişebilse de süt '
                                            'çocukluğunda mikrositer hipokrom aneminin ezici çoğunluğu '
                                            'nutrisyonel demir eksikliğidir.'}]},
            {'stage_title': 'Tedavi ve Yönetim',
             'question': 'Demir eksikliği anemisi tanısı kesinleşen bu hastada en uygun tedavi ve beslenme '
                         'planı hangisidir?',
             'options': [{'text': 'Hemoglobin değeri sekiz gramın altında saptandığı için acil serviste '
                                  'eritrosit süspansiyonu transfüzyonu uygulayarak hastayı çocuk hematoloji '
                                  'servisine yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Kalp yetmezliği veya dekompansasyon bulgusu olmayan stabil '
                                             'kronik anemide acil transfüzyon volüm yüklenmesi riski '
                                             'oluşturdu.',
                          'teaching_point': 'Kronik demir eksikliği anemisinde hemodinami stabilse '
                                            'hemoglobin 7 g/dL altında olsa dahi öncelikle oral tedavi '
                                            'tercih edilir.'},
                         {'text': 'Oral emilimin yetersiz kalacağı gerekçesiyle acil serviste tek doz yüksek '
                                  'doz intravenöz demir infüzyonu planlayarak hastayı gözleme almak',
                          'is_correct': False,
                          'scenario_update': 'İntravenöz demir infüzyonu sonrası çocukta alerjik reaksiyon '
                                             'gelişti; gereksiz yere invaziv ve maliyetli bir yol seçildi.',
                          'teaching_point': 'Oral tedaviyi tolere edebilen ve malabsorbsiyonu olmayan süt '
                                            'çocuklarında parenteral demir ilk seçenek değildir.'},
                         {'text': 'Diyet kısıtlaması yapmadan sadece profilaktik dozda günde bir miligram '
                                  'bölü kilogram oral demir damlası başlayarak hastayı kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Aşırı süt alımı devam ettiği ve doz yetersiz kaldığı için '
                                             'birinci aydaki kontrolde hemoglobin yükselmedi.',
                          'teaching_point': 'Tedavi edici doz 3-6 mg/kg/gün elementer demirdir ve inek sütü '
                                            "tüketimi mutlaka günlük 500 mL'nin altına indirilmelidir."},
                         {'text': 'Günlük 3-6 mg/kg elementer demir başlamak, inek sütünü kısıtlamak ve '
                                  'ilacı C vitaminiyle aç karnına vermek',
                          'is_correct': True,
                          'explanation': 'Tedavi dozu 3-6 mg/kg/gün elementer demirdir; C vitamini emilimi '
                                         'artırırken kalsiyum emilimi azaltır, inek sütü günlük 500 mL '
                                         'altında tutulmalıdır.',
                          'new_finding': 'Oral demir tedavisi başlandı. Aileye ilacın dişlerde geçici '
                                         'boyanma yapabileceği, gaitayı siyaha boyayacağı anlatıldı ve 1 ay '
                                         'sonraya kontrol planlandı.'}]}]},
 {'id': 'G22',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '6 Yaş',
  'gender': 'Kız',
  'complaint': 'Ağız içinde şiddetli ağrı, yemek yiyememe ve dudakta yaralar',
  'history': "Altı yaşındaki kız çocuğu annesi tarafından ağız içi yaralar nedeniyle getiriliyor: 'Kızım üç "
             'gündür bir şeyler çiğnerken ve su içerken ağzının çok acıdığını söylüyor, katı hiçbir şey '
             'yemedi. Dudağının içinde ve yanağında beyaz renkli küçük yaralar fark ettik. Ateşi hiç olmadı. '
             'Ellerinde veya ayaklarında herhangi bir döküntü yok. Geçen yıl da benzer şekilde dudağında tek '
             "bir yara çıkmış ve yaklaşık on günde kendiliğinden geçmişti.'",
  'final_diagnosis': 'Rekürren Aftöz Stomatit (Minör Aft)',
  'disposition': 'Yeşil Alandan Topikal Tedavi, Oral Hijyen ve Diyet Önerileri ile Taburculuk',
  'case_pearl': 'Rekürren aftöz stomatitte lezyonlar keratinize olmayan mukozada (bukkal mukoza, dudak iç '
                'yüzü, dil altı) yerleşir; etrafı eritemli bir hale ile çevrili, ortası sarı-gri '
                'psödomembranla kaplı ağrılı oval ülserlerdir. Diş etleri ve sert damak tutulmaz; ateş ve '
                'sistemik bulgu eşlik etmez. Viral enfeksiyonlardan (herpetik gingivostomatit, el-ayak-ağız) '
                'bu klinik özelliklerle ayrılır; antibiyotik veya sistemik antiviral gerekmez.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Ağız içinde ağrılı lezyonlar nedeniyle getirilen bu hastada ilk fizik muayene '
                         'yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Vital bulguları almak, ağız mukozası, diş etleri ile el, ayak ve perineal '
                                  'bölgeleri dikkatle muayene etmek',
                          'is_correct': True,
                          'explanation': 'Lezyonların yerleşimi (keratinize vs non-keratinize mukoza) ve '
                                         'ekstraoral döküntülerin taranması ayırıcı tanıda kilit role '
                                         'sahiptir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 88/dk, SS 20/dk, SpO2 %100. Fizik '
                                         'Muayene: Alt dudak mukozasında 4 mm ve sağ bukkal mukozada 5 mm '
                                         'çapında, ortası sarı-gri tabanlı, çevresi parlak eritemli hale ile '
                                         'çevrili 2 adet yuvarlak ülseratif lezyon izlendi. Diş etleri, dil '
                                         'sırtı ve sert damak tamamen doğal; ödem ve kanama yok. El ayası, '
                                         'ayak tabanı ve perianal bölgede döküntü saptanmadı. Servikal '
                                         'lenfadenopati yok.'},
                         {'text': 'Ülser tabanından steril eküvyonla sürüntü alarak hızlı antijen testi ve '
                                  'mikrobiyolojik boğaz kültürü analizi için acilen laboratuvara göndermek',
                          'is_correct': False,
                          'scenario_update': 'Lezyon tabanından sürüntü alınması çocuğa şiddetli ağrı verdi '
                                             've ağlamasına yol açtı; sürüntüde bakteriyel üreme saptanmadı.',
                          'teaching_point': 'Tipik non-keratinize mukozal ülserlerde rutin bakteriyel kültür '
                                            'endike değildir ve invaziv sürüntü gereksiz acı verir.'},
                         {'text': 'Beslenme azlığı öyküsü nedeniyle dehidratasyon gelişebileceğini öngörüp '
                                  'periferik damar yolu açarak rutin kan şekeri ve elektrolit paneli '
                                  'göndermek',
                          'is_correct': False,
                          'scenario_update': 'Damar yolu açılması hastanın anksiyetesini artırdı; bakılan '
                                             'elektrolitler ve kan şekeri tamamen normal sınırlarda geldi.',
                          'teaching_point': 'Mukozaları nemli, turgoru doğal ve idrar çıkışı yeterli olan '
                                            'çocuklarda invaziv damar yolu ve lab tetkiki gereksizdir.'},
                         {'text': 'Ağız içi yaygın enfeksiyon kuşkusuyla hastayı derhal izole edip acil diş '
                                  'hekimliği konsültasyonu ve tedavi amacıyla Sarı Alana devretmek',
                          'is_correct': False,
                          'scenario_update': 'Sarı Alanda hastanın genel durumunun stabil olduğu ve acil '
                                             'invaziv müdahale gereksinimi bulunmadığı teyit edildi.',
                          'teaching_point': 'Ateşi olmayan, vital bulguları stabil ve hava yolu tehdidi '
                                            'bulunmayan oral lezyonlu hastalar Yeşil Alanda '
                                            'yönetilebilir.'}]},
            {'stage_title': 'Tetkik ve Yaklaşım Kararı',
             'question': 'Fizik muayenesinde dudak içi ve yanakta lokalize ülserleri olan, ateşi bulunmayan '
                         'çocukta tetkik stratejiniz ne olmalıdır?',
             'options': [{'text': 'Herpes simpleks virüs enfeksiyonunu dışlamak amacıyla lezyon tabanından '
                                  'Tzanck yayması ve viral polimeraz zincir reaksiyonu tetkikini birlikte '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'Tzanck yaymasında multinükleer dev hücreler izlenmedi; viral '
                                             'tetkikler negatif sonuçlandı ve ek klinik katkı sağlamadı.',
                          'teaching_point': 'Herpetik lezyonlar genellikle keratinize mukozayı (diş eti, '
                                            'sert damak) tutar ve vezikülle başlar; non-keratinize mukoza '
                                            'ülserlerinde rutin önerilmez.'},
                         {'text': 'Tekrarlayan ağız lezyonları öyküsü nedeniyle Behçet hastalığı ve '
                                  'otoimmünite yönünden tam kan, CRP, ANA ve HLA-B51 tetkiklerini göndermek',
                          'is_correct': False,
                          'scenario_update': 'İstenen romatolojik ve genetik testlerin sonuçlanmasının '
                                             'haftalar süreceği belirtildi; akut faz reaktanları tamamen '
                                             'negatif çıktı.',
                          'teaching_point': 'Yılda bir iki kez çıkan, genital ülser veya üveitin eşlik '
                                            'etmediği izole tablolarda ilk başvuruda romatolojik panel '
                                            'istenmez.'},
                         {'text': 'Altta yatan inflamatuar bağırsak hastalığını ekarte etmek için fekal '
                                  'kalprotektin düzeyi bakılmasını ve acil gastroenteroloji konsültasyonu '
                                  'talep etmek',
                          'is_correct': False,
                          'scenario_update': 'Gastroenteroloji konsültan hekimi hastada kilo kaybı, kronik '
                                             'ishal veya rektal kanama olmadığı için endoskopi endikasyonu '
                                             'görmedi.',
                          'teaching_point': 'Gastrointestinal semptomların, büyüme geriliğinin veya anemi '
                                            'bulgularının eşlik etmediği durumlarda ileri tetkik gerekmez.'},
                         {'text': 'Klinik tablo ve lezyonlar tipik olduğundan laboratuvar tetkiki istemeden '
                                  'semptomları rahatlatmaya ve oral alımı desteklemeye odaklanmak',
                          'is_correct': True,
                          'explanation': 'Ateşsiz, izole ve karakteristik lezyonlarda tanı tamamen klinik '
                                         'konur; gereksiz tetkik ve girişimlerden kaçınılmalıdır.',
                          'new_finding': 'Ek laboratuvar tetkiki istenmedi. Hastanın klinik muayene '
                                         'bulgularıyla tanısal değerlendirmeye geçildi.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Öykü ve fizik muayene bulguları dikkate alındığında bu hastada en olası klinik '
                         'tanı hangisidir?',
             'options': [{'text': 'Primer Herpetik Gingivostomatit',
                          'is_correct': False,
                          'scenario_update': 'Herpetik gingivostomatitte yüksek ateş, yaygın diş eti '
                                             'hipertrofisi, kanaması ve perioral veziküller beklenir; bu '
                                             'hastada diş etleri doğaldır.',
                          'teaching_point': 'Herpetik gingivostomatit belirgin ateş, servikal lenfadenopati '
                                            've keratinize mukoza (gingiva) tutulumu ile seyreder.'},
                         {'text': 'El-Ayak-Ağız Hastalığı',
                          'is_correct': False,
                          'scenario_update': 'Hastanın el ayalarında, ayak tabanlarında veya kalçasında '
                                             'döküntü yoktur ve lezyonlar daha çok arka farenksten ziyade ön '
                                             'ağızdadır.',
                          'teaching_point': 'El-ayak-ağız hastalığında el ve ayaklarda papüloveziküler '
                                            'döküntüler ile farenks/damakta enantemler görülür.'},
                         {'text': 'Rekürren Aftöz Stomatit',
                          'is_correct': True,
                          'explanation': 'Non-keratinize mukoza tutulumu, sarı-gri psödomembranlı ağrılı '
                                         'ülserler, eritemli çevre ve ateşsiz seyir aftöz stomatit ile '
                                         'uyumludur.',
                          'new_finding': 'Klinik tanı Rekürren Aftöz Stomatit (Minör Aft) olarak '
                                         'belirlendi.'},
                         {'text': 'Oral Mukozal Kandidiyazis (Pamukçuk)',
                          'is_correct': False,
                          'scenario_update': 'Oral kandidiyaziste mukozaya yapışık, kaldırılınca kanayan '
                                             'beyaz peynirimsi plaklar görülür; sınırları belirgin ülserler '
                                             'oluşmaz.',
                          'teaching_point': 'Pamukçuk lezyonları eritemli tabanlı beyaz plaklar şeklindedir, '
                                            'tipik ağrılı çukurlaşmış ülser morfolojisinde değildir.'}]},
            {'stage_title': 'Tedavi ve Yönetim',
             'question': 'Rekürren aftöz stomatit tanısı konulan bu hastada en uygun tedavi ve taburculuk '
                         'planı hangisidir?',
             'options': [{'text': 'Topikal bariyer veya analjezik jel uygulamak, ılık yumuşak gıdalar '
                                  'önermek ve hidrasyonu yakından takip etmek',
                          'is_correct': True,
                          'explanation': 'Tedavide amaç ağrıyı hafifletmek ve hidrasyonu korumaktır; topikal '
                                         'hyaluronik asit/mukoprotektif jeller ve oral hijyen yeterlidir.',
                          'new_finding': 'Aileye topikal mukoza koruyucu jel tarifi yapıldı. Asitli, tuzlu '
                                         've sert gıdalardan kaçınmaları, hidrasyonu sürdürmeleri '
                                         'anlatıldı.'},
                         {'text': 'Lezyonların hızla gerilemesi amacıyla yedi gün süreli oral asiklovir '
                                  'süspansiyon ve sistemik antibiyotik tedavisi reçete ederek taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Viral veya bakteriyel etken olmadığı için antiviral ve '
                                             'antibiyotik tedavisi klinik gidişatı değiştirmedi ve yan etki '
                                             'riski oluşturdu.',
                          'teaching_point': 'Aftöz lezyonlarda herpes virüsü veya bakteriler rol oynamaz; '
                                            'asiklovir veya antibiyotik kullanımı tamamen gereksizdir.'},
                         {'text': 'Ülserlerin yayılmasını önlemek amacıyla yüksek doz oral prednizolon '
                                  'tedavisi başlayarak hastayı acil serviste yakın gözlem yatağına yatırmak',
                          'is_correct': False,
                          'scenario_update': 'Hafif minör lezyonlarda sistemik kortikosteroid başlanması '
                                             'hiperglisemi, immünsüpresyon ve huzursuzluk gibi yan etkilere '
                                             'yol açtı.',
                          'teaching_point': 'Sistemik steroidler yalnızca çok şiddetli, majör ve tedaviye '
                                            'dirençli vakalarda uzman kontrolünde düşünülür; minör '
                                            'lezyonlarda yeri yoktur.'},
                         {'text': 'Ağrıyı derhal kesmek için poliklinikte lezyon tabanını gümüş nitrat '
                                  'çubuğuyla koterize edip derin kimyasal koterizasyon pansumanı uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Gümüş nitrat uygulaması çocukta dayanılmaz bir yanma ağrısına '
                                             'yol açtı ve çevre dokuda kimyasal hasar oluşturdu.',
                          'teaching_point': 'Küçük çocuklarda kimyasal koterizasyon ağrılıdır, çevre '
                                            'mukozaya zarar verebilir ve doku iyileşmesini '
                                            'geciktirebilir.'}]}]},
 {'id': 'G23',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '9 Yaş',
  'gender': 'Erkek',
  'complaint': 'Gövdede kaşıntılı döküntüler ve göğüste daha önce çıkan büyük leke',
  'history': "Dokuz yaşındaki erkek çocuk annesiyle birlikte polikliniğe başvuruyor: 'Doktor bey/hanım, "
             'yaklaşık on gün önce oğlumun göğsünün üst kısmında madeni para büyüklüğünde, kenarları hafif '
             'kabuklu pembe bir leke fark ettik. Başta mantar sandık ve nemlendirici sürdük ama geçmedi. Son '
             'üç dört gündür ise sırtında, karnında ve göğsünde aynı lekenin daha küçükleri hızla çoğaldı. '
             "Hafif kaşıntısı var ama ateşi, boğaz ağrısı veya halsizliği hiç olmadı.'",
  'final_diagnosis': 'Pitriyazis Rozea',
  'disposition': 'Yeşil Alandan Bilgilendirme, Güvence Verme, Semptomatik Kaşıntı Tedavisi ile Taburculuk',
  'case_pearl': 'Pitriyazis rozea tipik olarak gövdede tek, 2-5 cm çapında, kenarları kalkık ve hafif '
                'skuamlı öncü plakla (herald patch / madalyon plak) başlar; 1-2 hafta sonra gövdede Langer '
                "çizgilerine paralel, 'çam ağacı' dağılımı gösteren daha küçük oval eritematöz skuamlı papül "
                've plaklar belirir. Kendi kendini 6-8 haftada sınırlayan selim bir ekzantemdir; gereksiz '
                'antifungal veya antibiyotik verilmemeli, aileye bulaşıcı olmadığı anlatılarak güvence '
                'verilmelidir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Gövdede yaygın döküntü şikayetiyle getirilen bu okul çağı çocuğunda ilk klinik '
                         'muayene yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Malign deri lezyonlarını ekarte etmek amacıyla döküntülerin dermatoskopik '
                                  'incelemesini yapıp acilen cerrahi eksizyonel deri biyopsisi işlemi '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'İnvaziv biyopsi önerisi aileyi derin bir endişeye sevk etti; '
                                             'selim bir ekzantem için gereksiz doku hasarı riski doğdu.',
                          'teaching_point': 'Simetrik, yüzeyel ve tipik seyirli döküntülerde invaziv deri '
                                            'biyopsisi endike değildir; klinik muayene yeterlidir.'},
                         {'text': 'Tüm vücut cildini tamamen soyup döküntülerin morfolojisini, gövdedeki '
                                  'dizilim paternini, avuç içlerini ve mukozaları dikkatlice incelemek',
                          'is_correct': True,
                          'explanation': 'Döküntünün dağılım paterni (Langer çizgilerine paralellik), skuam '
                                         'özelliği ve mukoza/avuç içi tutulumunun olmaması kritik ipuçları '
                                         'sağlar.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 82/dk, SS 18/dk, SpO2 %99. Cilt '
                                         'Muayenesi: Sternum üzerinde 3.5 cm çapında, hafif kabarık '
                                         'eritematöz kenarlı, iç kenarında yakalık tarzında ince '
                                         'deskuamasyon bulunan oval bir plak saptandı. Sırt ve gövde ön '
                                         "yüzünde kaburga çizgilerine paralel 'çam ağacı' diziliminde "
                                         '0.5-1.5 cm boyutlarında benzer morfolojide çok sayıda oval '
                                         'eritematöz skuamlı lezyon izlendi. Avuç içleri, ayak tabanları ve '
                                         'oral mukoza tamamen temiz. Lenfadenopati yok.'},
                         {'text': 'Vaskülit veya meningokoksemi kuşkusuyla hastayı izole edip acil damar '
                                  'yolu açılması ve monitörizasyon amacıyla Sarı Alana devretmek',
                          'is_correct': False,
                          'scenario_update': 'Sarı Alanda hastanın genel durumunun iyi, döküntülerin '
                                             'peteşi-purpura değil eritematöz skuamlı olduğu ve vitallerin '
                                             'stabil olduğu görüldü.',
                          'teaching_point': 'Basmakla solan, skuamlı ve genel durumu mükemmel olan hastalar '
                                            'vaskülit veya meningokoksemi lehine değildir; Yeşil Alanda '
                                            'incelenir.'},
                         {'text': 'Çocuğu tamamen soymadan sadece göğsündeki ilk lezyonu muayene edip '
                                  'alerjik reaksiyon düşünerek oral antihistaminik şurup verip taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Sırt ve diğer gövde alanları incelenmediği için döküntünün '
                                             'karakteristik dermatom benzeri dağılım paterni gözden '
                                             'kaçırıldı.',
                          'teaching_point': 'Döküntülü çocuklarda tüm vücut derisi mutlaka tamamen açılarak '
                                            'incelenmeli ve lezyonların yayılım paterni '
                                            'haritalandırılmalıdır.'}]},
            {'stage_title': 'Tetkik ve Yaklaşım Kararı',
             'question': 'Gövdede kaburga çizgilerine paralel dağılım gösteren oval skuamlı döküntüleri olan '
                         'bu hastada tetkik kararınız ne olmalıdır?',
             'options': [{'text': 'Mantar enfeksiyonunu kesin olarak dışlamak amacıyla tüm lezyonlardan '
                                  'bistüriyle derin kazıntı alarak potasyum hidroksit mikroskopisi tetkiki '
                                  'istemek',
                          'is_correct': False,
                          'scenario_update': 'Çok sayıda lezyondan yapılan ağrılı kazıntıda mikroskopide '
                                             'mantar hifleri veya sporları görülmedi; lezyonlar irrite oldu.',
                          'teaching_point': 'Tinea korporiste lezyon genellikle tek veya birkaç adettir; tüm '
                                            'gövdeye paralel dağılan döküntülerde yaygın kazıntı gerekmez.'},
                         {'text': 'Alerji ve post-streptokokal reaksiyonları araştırmak amacıyla periferik '
                                  'tam kan sayımı, total IgE, CRP ve ASO düzeylerini birlikte göndermek',
                          'is_correct': False,
                          'scenario_update': 'Kan tahlili sonuçları tamamen normal geldi; damar yolu '
                                             'açılması çocuğun korkmasına ve acilde beklemesine neden oldu.',
                          'teaching_point': 'Klinik görünümü tipik olan, ateş ve sistemik bulgunun eşlik '
                                            'etmediği tablolarda kan tetkiklerinin tanısal değeri yoktur.'},
                         {'text': 'Klinik tablo ve döküntü paterni tanısal olduğundan hastadan herhangi bir '
                                  'invaziv laboratuvar veya görüntüleme tetkiki istememek',
                          'is_correct': True,
                          'explanation': 'Karakteristik öncü lezyon ve gövdedeki dağılım paterni klinik tanı '
                                         'için yeterlidir; rutin laboratuvar tetkiki endike değildir.',
                          'new_finding': 'Tetkik istenmedi; lezyonların klinik özellikleri üzerinden tanı ve '
                                         'hasta eğitimi aşamasına geçildi.'},
                         {'text': 'Viral döküntü etkenlerini aydınlatmak için kanda Epstein-Barr virüsü, '
                                  'sitomegalovirüs ve parvovirüs serolojilerinden oluşan genişletilmiş '
                                  'antikor panelini istemek',
                          'is_correct': False,
                          'scenario_update': 'Seroloji sonuçlarının çıkmasının günler alacağı öğrenildi; '
                                             'hastanın klinik yaklaşımında ve tedavisinde hiçbir değişiklik '
                                             'sağlamadı.',
                          'teaching_point': 'Selim seyirli yüzeyel ekzantemlerde genişletilmiş viral antikor '
                                            'panelleri rutin pratikte maliyet-etkin değildir ve '
                                            'önerilmez.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Öykü ve döküntü morfolojisi birlikte değerlendirildiğinde hastadaki en olası '
                         'klinik tanı hangisidir?',
             'options': [{'text': 'Tinea Korporis (Gövde Mantarı)',
                          'is_correct': False,
                          'scenario_update': 'Tinea korporiste genellikle tek veya az sayıda, santralden '
                                             'iyileşme gösteren anüler plaklar görülür; tüm sırtta çam ağacı '
                                             'dağılımı beklenmez.',
                          'teaching_point': 'Tinea korporis asimetrik ve sınırlı sayıda lezyonla gider; bu '
                                            'hastadaki gibi öncü plak sonrası bilateral simetrik dissemine '
                                            'yayılım göstermez.'},
                         {'text': 'Guttat Psöriyazis (Damla Sedef)',
                          'is_correct': False,
                          'scenario_update': 'Guttat psöriyaziste genellikle streptokokal farenjitten 1-2 '
                                             'hafta sonra kalın gümüşi skuamlı küçük damla şeklinde '
                                             'lezyonlar çıkar; öncü madalyon plak olmaz.',
                          'teaching_point': 'Guttat psöriyazis kalın sedef rengi skuamlarla kaplıdır ve öncü '
                                            'bir büyük plak öyküsü bulunmaz.'},
                         {'text': 'Sekonder Sifiliz Ekzantemi',
                          'is_correct': False,
                          'scenario_update': 'Sekonder sifilizde döküntüler avuç içi ve ayak tabanlarını '
                                             'belirgin tutar, lenfadenopati eşlik eder ve öncü plak '
                                             'görülmez.',
                          'teaching_point': 'Sekonder sifiliz palmar ve plantar tutulumun yanı sıra '
                                            'generalized lenfadenopati ile seyreder.'},
                         {'text': 'Pitriyazis Rozea',
                          'is_correct': True,
                          'explanation': 'Öncü plak (herald patch), bunu izleyen çam ağacı dağılımlı yakalık '
                                         'tarzı skuamlı oval lezyonlar pitriyazis rozea için tipiktir.',
                          'new_finding': 'Klinik tanı Pitriyazis Rozea olarak kesinleştirildi.'}]},
            {'stage_title': 'Tedavi ve Yönetim',
             'question': 'Pitriyazis rozea tanısı kesinleşen bu hastanın tedavisinde ve aile '
                         'bilgilendirmesinde en uygun yaklaşım hangisidir?',
             'options': [{'text': 'Döküntülerin yayılmasını durdurmak amacıyla dört hafta süreli oral '
                                  'terbinafin veya flukonazol antifungal tablet tedavisi reçete ederek '
                                  'taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Antifungal tedavi mantar kaynaklı olmayan bu tabloda etkisiz '
                                             'kaldı ve gereksiz hepatotoksisite takip ihtiyacı doğurdu.',
                          'teaching_point': 'Pitriyazis rozea fungal bir enfeksiyon değildir; sistemik veya '
                                            'topikal antifungallerin tedavide yeri yoktur.'},
                         {'text': 'Hastalığın kendiliğinden iyileşeceğini belirtmek, bulaşıcı olmadığını '
                                  'anlatıp kaşıntı varsa semptomatik antihistaminik veya nemlendirici losyon '
                                  'önermek',
                          'is_correct': True,
                          'explanation': 'Hastalık kendi kendini sınırlayan selim bir tablodur; temel '
                                         'yaklaşım aileye güvence vermek ve varsa semptomatik kaşıntıyı '
                                         'rahatlatmaktır.',
                          'new_finding': 'Aileye hastalığın iz bırakmadan 1-2 ay içinde kendiliğinden '
                                         'geçeceği anlatıldı. Sıcak banyodan kaçınmaları ve hafif kaşıntı '
                                         'için nemlendirici kullanmaları önerildi.'},
                         {'text': 'Hastalığı bulaşıcı kabul ederek çocuğu üç hafta okuldan izole etmek ve '
                                  'taburculukta yüksek doz sistemik kortikosteroid başlamak',
                          'is_correct': False,
                          'scenario_update': 'Okuldan gereksiz yere uzaklaştırılan çocuğun eğitim hayatı '
                                             'aksadı ve sistemik steroid yan etkileri ortaya çıktı.',
                          'teaching_point': 'Pitriyazis rozea bulaşıcı değildir, okula devamı kısıtlanmaz ve '
                                            'rutin sistemik kortikosteroid endikasyonu yoktur.'},
                         {'text': 'Lezyonların derhal solması için hastayı acil serviste ultraviyole '
                                  'fototerapi seansına almak ve yüksek doz intravenöz antiviral infüzyonu '
                                  'uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Hastanede yatış ve fototerapi gereksiz maliyet ve anksiyete '
                                             'yarattı; selim tablonun seyrinde dramatik fark oluşmadı.',
                          'teaching_point': 'Hafif ve orta seyirli pitriyazis rozeada acil fototerapi veya '
                                            'antiviral infüzyon endikasyonu bulunmamaktadır.'}]}]},
 {'id': 'G24',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '4 Yaş',
  'gender': 'Kız',
  'complaint': 'Koltuk altında ve gövdede inci tanesi gibi parlak pütürler çıkması',
  'history': 'Dört yaşındaki kız çocuğu annesi tarafından cildindeki pütürler nedeniyle getiriliyor: '
             "'Kızımın yaklaşık bir ay önce sağ koltuk altında bir iki tane sivilce benzeri kabarcık "
             'çıkmıştı. Zamanla bunların sayısı arttı, göğsüne ve karnına da yayıldı. Kabarcıklar sert, inci '
             'gibi parlıyor ve ortalarında minik bir çukurluk var. Herhangi bir ağrısı veya ateşi yok, bazen '
             "hafif kaşıyor. Kreşe gidiyor ve havuz kursuna katılıyordu.'",
  'final_diagnosis': 'Molluskum Kontagiozum',
  'disposition': 'Yeşil Alandan Aile Eğitimi, Otomanipülasyondan Kaçınma ve İzlem Planı ile Taburculuk',
  'case_pearl': 'Molluskum kontagiozum, poxvirüs ailesinden Molluscum contagiosum virüsünün neden olduğu, '
                'çocuklarda sık görülen selim bir kutanöz enfeksiyondur. Karakteristik lezyonlar 2-5 mm '
                'çapında, kubbe şeklinde, ortası göbekli (umbilike), inci benzeri parlak papüllerdir. Havuz, '
                'doğrudan temas veya havlu paylaşımıyla bulaşır. Çoğu lezyon 6-18 ay içinde nedbesiz '
                'kendiliğinden geriler. Sıkma, kaşıma ve cerrahi küretaj otokoinokülasyona ve skar '
                'gelişimine yol açabileceğinden öncelikle konservatif izlem ve aile eğitimi önerilir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Gövdede parlak kabarcıklar tariflenen bu çocuğun ilk değerlendirmesinde en uygun '
                         'klinik muayene yaklaşımı hangisidir?',
             'options': [{'text': 'Tanıyı doğrulamak amacıyla lezyonlardan birini forsepsle sıkarak içindeki '
                                  'kazeöz materyali aspire edip acil serviste mikroskop altında incelemeyi '
                                  'seçmek',
                          'is_correct': False,
                          'scenario_update': 'Lezyonun sıkılması şiddetli ağrıya, kanamaya ve virüsün çevre '
                                             'deriye yayılmasına zemin hazırladı.',
                          'teaching_point': 'Klinik muayenede tipik kubbe şeklindeki papüller sıkılmamalı '
                                            'veya koparılmamalıdır; bu durum otokoinokülasyona ve skara yol '
                                            'açar.'},
                         {'text': 'Suçiçeği veya dissemine enfeksiyon kuşkusuyla çocuğu negatif basınçlı '
                                  'odaya alıp damar yolu ve izolasyon amacıyla Sarı Alana devretmek',
                          'is_correct': False,
                          'scenario_update': 'Sarı Alanda hastanın ateşi olmadığı, genel durumunun tamamen '
                                             'stabil olduğu ve lezyonların vezikül değil papül olduğu '
                                             'belirlendi.',
                          'teaching_point': 'Sistemik toksisite bulgusu, ateşi veya akut veziküler döküntüsü '
                                            'olmayan stabil deri döküntüleri Yeşil Alanda değerlendirilir.'},
                         {'text': 'Vital bulguları almak, lezyonların morfolojisini, santral '
                                  'umbilikasyonunu, anatomik dağılımını ve sekonder enfeksiyon varlığını '
                                  'dikkatle muayene etmek',
                          'is_correct': True,
                          'explanation': 'Kubbe şeklindeki papüllerin santral umbilikasyonu ve parlak inci '
                                         'görünümü ile çevre derideki egzama veya süperenfeksiyon '
                                         'incelenmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 94/dk, SS 22/dk, SpO2 %100. Cilt '
                                         'Muayenesi: Sağ aksiller bölgede, göğüs yan duvarında ve karında '
                                         '2-4 mm boyutlarında, pembe-ten rengi, kubbe şeklinde, ortasında '
                                         'belirgin göbek benzeri çukurluk (santral umbilikasyon) bulunan '
                                         'yaklaşık 15 adet parlak papül izlendi. Lezyonların çevresinde '
                                         'eritem, ısı artışı veya pürülan akıntı yok. Diğer sistem '
                                         'muayeneleri doğal.'},
                         {'text': 'Cinsel istismar kuşkusu nedeniyle ayrıntılı adli tıp protokolü başlatıp '
                                  'hastayı genel muayene yapmadan doğrudan çocuk izlem merkezine '
                                  'yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Adli süreç başlatılması ailede büyük bir şok yarattı; aksiller '
                                             've gövdedeki lezyonların çocukluk çağında temasla geçtiği '
                                             'sonradan anlaşıldı.',
                          'teaching_point': 'Aksilla ve gövde yerleşimi çocukluk çağında havuz veya oyun '
                                            'temasıyla sık görülen tipik bir kutanöz yayılımdır; izole adli '
                                            'şüphe doğurmaz.'}]},
            {'stage_title': 'Tetkik ve Yaklaşım Kararı',
             'question': 'Fizik muayenesinde gövdede ortası göbekli parlak papülleri saptanan bu çocukta '
                         'tetkik yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Karakteristik klinik bulgular tanı koydurucu olduğundan hastadan herhangi '
                                  'bir invaziv girişim veya laboratuvar tetkiki istememek',
                          'is_correct': True,
                          'explanation': 'Ortası göbekli inci gibi kubbe papüller tanı için patognomoniktir; '
                                         'laboratuvar veya biyopsi gerekmez.',
                          'new_finding': 'Tetkik istenmedi; lezyonların klinik morfolojisinin tanı için tam '
                                         'yeterlilikte olduğu teyit edildi.'},
                         {'text': 'Histopatolojik inceleme için genel anestezi altında lezyonlardan çok '
                                  'odaklı cerrahi punch deri biyopsisi alınmasını planlayıp hastaya gün '
                                  'vermek',
                          'is_correct': False,
                          'scenario_update': 'Deri biyopsisi önerisi çocuğu çok korkuttu ve küçük çocukta '
                                             'genel anestezi riski gereksiz yere gündeme geldi.',
                          'teaching_point': 'Tipik klinik görünüme sahip benign papüler lezyonlarda tanı '
                                            'klinik olarak konur; cerrahi deri biyopsisi endike değildir.'},
                         {'text': 'Altta yatan hücresel immün yetmezlik olasılığını dışlamak amacıyla '
                                  'lenfosit alt grupları ve serum immünglobulin düzeylerini tetkik olarak '
                                  'göndermek',
                          'is_correct': False,
                          'scenario_update': 'Gönderilen immünolojik paneller tamamen normal çıktı; '
                                             'poliklinik bekleme süresi uzadı ve gereksiz maliyet oluştu.',
                          'teaching_point': 'Gelişimi normal, tekrarlayan ağır enfeksiyon öyküsü olmayan '
                                            'immünokompetan çocuklarda yaygın kutanöz lezyonlar için rutin '
                                            'immün panel gerekmez.'},
                         {'text': 'Papüllerin yüzeyini bistüriyle delerek steril eküvyon çubuğuyla '
                                  'bakteriyel ve fungal kültür örnekleri alıp acilen mikrobiyoloji '
                                  'laboratuvarına göndermek',
                          'is_correct': False,
                          'scenario_update': 'Papüllerin delinmesi ağrı ve kanamaya yol açtı; kültürlerde '
                                             'patojen üremedi ve iyileşme gecikti.',
                          'teaching_point': 'Pürülan akıntı veya selülit benzeri süperenfeksiyon bulgusu '
                                            'yoksa lezyonları delmek veya kültür almak kontraendikedir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Öykü ve fizik muayenedeki lezyon morfolojisi dikkate alındığında en olası klinik '
                         'tanı nedir?',
             'options': [{'text': 'Verruka Vulgaris (Yaygın Siğil)',
                          'is_correct': False,
                          'scenario_update': 'Verruka vulgariste hiperkeratotik, pürtüklü karnabahar benzeri '
                                             'lezyonlar görülür; düzgün yüzeyli santral umbilike kubbe '
                                             'papüller olmaz.',
                          'teaching_point': 'Verrukalar HPV kaynaklıdır ve yüzeyi sert, hiperkeratotiktir; '
                                            'ortası göbekli inci benzeri morfoloji göstermez.'},
                         {'text': 'Varisella Zoster (Suçiçeği)',
                          'is_correct': False,
                          'scenario_update': 'Suçiçeğinde lezyonlar hızla polimorfik veziküllere dönüşür, '
                                             'kaşıntılıdır, ateş eşlik eder ve haftalarca aynı papül '
                                             'formunda kalmaz.',
                          'teaching_point': 'Varisella akut başlangıçlı, ateşli ve hızla vezikül-krut '
                                            'evrelerine ilerleyen kaşıntılı bir enfeksiyondur.'},
                         {'text': 'Molluskum Kontagiozum',
                          'is_correct': True,
                          'explanation': 'Kubbe şeklinde, santral umbilike inci parlaklığındaki papüller '
                                         'Molluscum contagiosum virüsü enfeksiyonu için karakteristiktir.',
                          'new_finding': 'Klinik tanı Molluskum Kontagiozum olarak kesinleştirildi.'},
                         {'text': 'Gençlik Ksantogranülomu',
                          'is_correct': False,
                          'scenario_update': 'Ksantogranülomlar sarı-turuncu renkli, umbilikasyon içermeyen '
                                             'soliter veya az sayıda nodüllerdir; lezyon özellikleri '
                                             'uymamaktadır.',
                          'teaching_point': 'Ksantogranülom sarımsı histiyositik proliferasyon olup santral '
                                            'göbekli parlak inci papülleri yapmaz.'}]},
            {'stage_title': 'Tedavi ve Yönetim',
             'question': 'Molluskum kontagiozum tanısı alan bu çocuk ve ailesi için en uygun yönetim '
                         'stratejisi hangisidir?',
             'options': [{'text': 'Acil serviste tüm lezyonları cerrahi küretajla kazımak veya sıvı nitrojen '
                                  'koterizasyonuyla seanslar halinde agresif cerrahi kriyoterapi uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Küretaj ve agresif kriyoterapi çocukta kalıcı '
                                             'hipopigmentasyon, hipertrofik skar ve tedaviye bağlı fobiye '
                                             'yol açtı.',
                          'teaching_point': 'Küçük çocuklarda invaziv girişimler skar bırakabilir ve '
                                            'travmatiktir; lezyonların kendiliğinden gerileyeceği '
                                            'unutulmamalıdır.'},
                         {'text': 'Sistemik yayılımı önlemek için oral asiklovir süspansiyon ve profilaktik '
                                  'geniş spektrumlu oral sefalosporin antibiyotik tedavisi reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Poxvirüslere asiklovir etkisizdir ve bakteriyel '
                                             'süperenfeksiyon yokluğunda antibiyotik sadece bağırsak '
                                             'florasını bozdu.',
                          'teaching_point': 'Molluskum kontagiozum bir poxvirüs enfeksiyonudur; asiklovir '
                                            'veya oral antibiyotikler tedavide kesinlikle etkisizdir.'},
                         {'text': 'Papülleri hızla kurutmak amacıyla tüm lezyonlu deriye sabah akşam yüksek '
                                  'potensli topikal klobetazol kortikosteroid krem reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Güçlü kortikosteroid uygulanması lokal immüniteyi baskılayarak '
                                             'lezyonların hızla çoğalmasına ve büyümesine neden oldu.',
                          'teaching_point': 'Topikal kortikosteroidler virüsün çoğalmasını artırarak '
                                            'molluskum lezyonlarının yayılmasına yol açabilir.'},
                         {'text': 'Lezyonların kendiliğinden gerileyeceğini aileye anlatmak, lezyonları '
                                  'sıkma ve kaşımadan kaçınmayı tembihlemek, ortak havlu kullanımını '
                                  'kesinlikle engellemek',
                          'is_correct': True,
                          'explanation': 'İmmünokompetan çocuklarda lezyonlar 6-18 ayda nedbesiz geriler; '
                                         'otokoinokülasyonu ve bulaşı önlemek için sıkmamak ve havlu '
                                         'paylaşmamak esastır.',
                          'new_finding': 'Aileye lezyonların selim doğası anlatıldı. Tırnakların kısa '
                                         'kesilmesi, banyoda liflenmemesi ve yüzme havuzunda lezyonların su '
                                         'geçirmez bantla kapatılması önerildi.'}]}]},
 {'id': 'G25',
  'category': '👶 Ağlayan, Emmeyen, Huzursuz Bebek',
  'age': '7 Aylık',
  'gender': 'Kız',
  'complaint': 'Alt bez bölgesinde şiddetli kızarıklık, pişik ve huzursuzluk',
  'history': 'Yedi aylık kız bebek annesi tarafından alt bez bölgesindeki döküntüler nedeniyle getiriliyor: '
             "'Kızımın altındaki kızarıklık yaklaşık beş gün önce başladı. Normalde pişik kremi sürünce "
             'geçerdi ama bu sefer hiç fayda etmedi, aksine daha da koyu kırmızı oldu ve bacak kıvrımlarının '
             'içine doğru yayıldı. Kızarıklığın çevresinde küçük sivilce gibi kırmızı noktalar çıkmaya '
             'başladı. Altını her açtığımızda veya ıslattığında canı çok yanıyor ve durmaksızın ağlıyor. İki '
             "hafta önce üst solunum yolu enfeksiyonu nedeniyle bir hafta antibiyotik şurup kullanmıştı.'",
  'final_diagnosis': 'Bebek Bezi Dermatiti ve Sekonder Kandida Süperenfeksiyonu',
  'disposition': 'Yeşil Alandan Topikal Antifungal, Çinko Oksit Bariyer Krem ve Bez Bakımı Eğitimi ile '
                 'Taburculuk',
  'case_pearl': 'Basit irritan bebek bezi dermatitinde inguinal katlantılar korunurken, sekonder Candida '
                'albicans süperenfeksiyonu eklendiğinde parlak kırmızı eritematöz plaklar inguinal '
                'kıvrımları da tutar ve çevreye dağılan noktasal satellit püstüller/papüller görülür. Yakın '
                'zamanda antibiyotik kullanımı önemli bir kolaylaştırıcı faktördür. Tedavide katlantılara '
                'topikal antifungal (klotrimazol veya mikonazol), üzerine çinko oksitli bariyer krem '
                'uygulanmalı ve bölgenin kuru kalması sağlanmalıdır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Alt bez alanında şiddetli kızarıklık ve huzursuzlukla başvuran bu süt çocuğunda '
                         'ilk klinik muayene yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Huzursuzluk ve yaygın cilt bulguları nedeniyle bebeği acil Sarı Alana '
                                  'alıp erken sepsis kuşkusuyla damar yolu açmak',
                          'is_correct': False,
                          'scenario_update': 'Sarı Alanda bebeğin ateşi olmadığı, beslenmesinin iyi ve '
                                             'hemodinamisinin tamamen stabil olduğu görüldü.',
                          'teaching_point': 'Genel durumu iyi, ateşi ve sistemik enfeksiyon belirtisi '
                                            'olmayan lokalize cilt lezyonlu bebekler Yeşil Alanda '
                                            'değerlendirilir.'},
                         {'text': 'Lokal lezyon muayenesini yapmadan önce tüm püstülleri enjektör iğnesiyle '
                                  'patlatarak elde edilen pürülan materyali mikrobiyoloji laboratuvarına '
                                  'ulaştırmak',
                          'is_correct': False,
                          'scenario_update': 'Püstüllerin mekanik olarak boşaltılması bebeğe şiddetli acı '
                                             'verdi ve deride açık erozyonlar oluşturdu.',
                          'teaching_point': 'İntakt lezyonların agresif şekilde patlatılması ağrı ve '
                                            'sekonder bakteriyel giriş kapısı oluşturur; muayene '
                                            'inspeksiyonla yapılmalıdır.'},
                         {'text': 'Vital bulguları almak, perineal bölgeyi, inguinal katlantıları, perianal '
                                  'dokuyu ve oral mukozayı dikkatlice muayene etmek',
                          'is_correct': True,
                          'explanation': 'İnguinal kıvrımların tutulumu, periferik çevre püstüllerin varlığı '
                                         've eşlik edebilecek oral mukoza lezyonları kritik ayırt edici '
                                         'bulgulardır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 114/dk, SS 26/dk, SpO2 %99. Fizik '
                                         'Muayene: Gluteal, perineal ve her iki inguinal katlantıyı içine '
                                         "alan, parlak 'biftek kırmızısı' eritemli, masere plaklar saptandı. "
                                         'Plağın periferinde sağlam deriye saçılmış çok sayıda 1-2 mm '
                                         'boyutunda noktasal eritematöz çevre püstül ve papüller görüldü. '
                                         'Oral mukozada yanak içinde beyaz membranöz lezyonlar saptandı. '
                                         'Sistemik muayeneler doğal.'},
                         {'text': 'Kızarıklığın sınırları belirgin olduğu için öncelikle çocuk istismarı '
                                  'açısından genital yaralanma ve travma odaklı adli muayene gerçekleştirmek',
                          'is_correct': False,
                          'scenario_update': 'Adli şüphe aileyi renside etti; perineal kıvrımları tutan '
                                             'parlak eritemin tipik bir dermatolojik süreç olduğu anlaşıldı.',
                          'teaching_point': 'Katlantıları tutan masere eritem ve periferik püstüller '
                                            'enfeksiyöz dermatolojik süreçlerle uyumludur; travmatik veya '
                                            'adli özellik taşımaz.'}]},
            {'stage_title': 'Tetkik ve Yaklaşım Kararı',
             'question': 'İnguinal katlantıları tutan parlak kızarıklığı ve çevresel püstülleri olan bu '
                         'bebekte tetkik stratejiniz ne olmalıdır?',
             'options': [{'text': 'Sistemik bakteriyemi veya derin doku enfeksiyonu riskini değerlendirmek '
                                  'üzere tam kan sayımı, CRP ve kan kültürünü acilen almak',
                          'is_correct': False,
                          'scenario_update': 'Laboratuvar sonuçlarında lökosit ve CRP normal sınırlarda '
                                             'geldi; kan alınırken bebek uzun süre sakinleşmedi.',
                          'teaching_point': 'Ateş veya toksik görünümün olmadığı yüzeyel perineal tablolarda '
                                            'sistemik enflamatuar belirteçler ve kan kültürü endike '
                                            'değildir.'},
                         {'text': 'Klinik görünüm ve lezyon dağılımı karakteristik olduğundan acil serviste '
                                  'kan tahlili veya radyolojik tetkik istememek',
                          'is_correct': True,
                          'explanation': 'İnguinal kıvrım tutulumu ve periferik lezyonlar klinik tanı için '
                                         'yeterlidir; rutin laboratuvar araştırması gerekmez.',
                          'new_finding': 'Gereksiz laboratuvar tetkiklerinden kaçınıldı; klinik bulgularla '
                                         'doğrudan tanı ve tedavi aşamasına geçildi.'},
                         {'text': 'Langerhans hücreli histiyositoz olasılığını dışlamak amacıyla sedasyon '
                                  'altında acil perineal cerrahi punch deri biyopsisi işlemini planlamak',
                          'is_correct': False,
                          'scenario_update': 'Punch biyopsi önerisi aileyi paniğe sevk etti; invaziv işlem '
                                             'bölgedeki doku maserasyonunu artırma riski taşıdı.',
                          'teaching_point': 'Tipik eritematöz masere döküntülerde histiyositoz gibi nadir '
                                            'antiteler ilk aşamada düşünülmez ve acil biyopsi yapılmaz.'},
                         {'text': 'Perineal döküntülerin idrar yolu enfeksiyonu sekeli olabileceği '
                                  'düşüncesiyle mesane kateterizasyonu uygulayarak steril idrar tahlili ve '
                                  'kültürü göndermek',
                          'is_correct': False,
                          'scenario_update': 'Ağrılı idrar sondası uygulaması eritemli perineal dokuda '
                                             'kanamaya neden oldu; tam idrar tetkiki normal sonuçlandı.',
                          'teaching_point': 'İdrar yolu enfeksiyonu perineal kıvrımlarda biftek kırmızısı '
                                            'lezyon yapmaz; travmatize dokuya gereksiz kateter '
                                            'uygulanmamalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Öykü, antibiyotik kullanımı ve fizik muayene bulguları birlikte ele alındığında en '
                         'olası klinik tanı nedir?',
             'options': [{'text': 'Basit İrritan Bez Dermatiti',
                          'is_correct': False,
                          'scenario_update': 'Basit irritan dermatitte inguinal katlantılar ve kıvrımlar '
                                             'genellikle korunur, satellit lezyonlar ve parlak eritem '
                                             'izlenmez.',
                          'teaching_point': 'Basit irritan kontakt dermatitte dışbükey yüzeyler tutulurken '
                                            'derin kıvrımlar korunur; kıvrım tutulumu süperenfeksiyon '
                                            'lehinedir.'},
                         {'text': 'İnvers Psoriyazis (Ters Sedef)',
                          'is_correct': False,
                          'scenario_update': 'İnvers psoriyaziste parlak kırmızı keskin sınırlı plaklar '
                                             'görülebilse de satellit püstüller ve oral pamukçuk eşliği '
                                             'beklenmez.',
                          'teaching_point': 'İnvers sedefte lezyonlar kıvrımlardadır ancak satellit '
                                            'püstüller bulunmaz ve yakın dönem antibiyotik öyküsüyle '
                                            'ilişkili değildir.'},
                         {'text': 'Bebek Bezi Dermatiti ve Sekonder Kandida Süperenfeksiyonu',
                          'is_correct': True,
                          'explanation': 'İnguinal kıvrımların belirgin tutulumu, parlak biftek kırmızısı '
                                         'maserasyon, satellit püstüller ve oral tutulum tipiktir.',
                          'new_finding': 'Klinik tanı Bebek Bezi Dermatiti ve Sekonder Kandida '
                                         'Süperenfeksiyonu olarak doğrulandı.'},
                         {'text': 'Streptokokal Perianal Selülit',
                          'is_correct': False,
                          'scenario_update': 'Perianal streptokokal enfeksiyonda anüs çevresinde keskin '
                                             'sınırlı parlak eritem ve kanamalı defekasyon görülür; inguinal '
                                             'katlantılar tutulmaz.',
                          'teaching_point': 'Streptokokal hastalıkta anüs çevresi sınırlı tutulur ve '
                                            'satellit püstüller görülmez.'}]},
            {'stage_title': 'Tedavi ve Yönetim',
             'question': 'Kandida süperenfeksiyonlu bebek bezi dermatiti tanısı kesinleşen bu bebek için en '
                         'uygun tedavi yaklaşımı nedir?',
             'options': [{'text': 'Enflamasyonu derhal baskılamak amacıyla günde iki kez yüksek potensli '
                                  'topikal florlu kortikosteroid krem reçete edip taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Güçlü steroid antifungal olmadan uygulandığı için fungal '
                                             'proliferasyon şiddetlendi ve cilt atrofisi gelişti.',
                          'teaching_point': 'Fungal süperenfeksiyon varlığında tek başına güçlü steroid '
                                            'kullanımı mantarın çoğalmasına ve sistemik emilime yol açar.'},
                         {'text': 'Süperenfeksiyonun derin dokulara yayılmasını önlemek amacıyla bebeği '
                                  'yatırıp intravenöz flukonazol infüzyonu ve parenteral geniş spektrumlu '
                                  'antibiyotik başlamak',
                          'is_correct': False,
                          'scenario_update': 'İnvaziv fungal enfeksiyonu olmayan stabil bebekte gereksiz '
                                             'hastane yatışı ve parenteral ilaç toksisite riski doğdu.',
                          'teaching_point': 'Yüzeyel kutanöz fungal enfeksiyonlarda hemodinami stabilse '
                                            'parenteral tedavi endike değildir; topikal tedavi yeterlidir.'},
                         {'text': 'Lezyonlara talk pudrası uygulayarak bölgeyi kurutmak ve eşzamanlı olarak '
                                  'oral yoldan amoksisilin-klavulanat antibiyotik şurup reçete ederek '
                                  'taburculuk planlamak',
                          'is_correct': False,
                          'scenario_update': 'Pudra kullanımı aspirasyon riski yarattı ve ciltte '
                                             'granülasyona neden oldu; antibiyotik ise mantar florasını daha '
                                             'da artırdı.',
                          'teaching_point': 'Pudra solunum yolu için tehlikelidir; antibiyotikler koruyucu '
                                            'bakterileri yok ederek kandida üremesini alevlendirir.'},
                         {'text': 'Topikal klotrimazol krem ile çinko oksit bariyer krem başlamak, altını '
                                  'sık değiştirmek ve kuru tutulmasını sağlamak',
                          'is_correct': True,
                          'explanation': 'Günde 2-3 kez topikal antifungal (klotrimazol veya mikonazol), '
                                         'üzerine bariyer krem sürülmeli ve bölge havalandırılmalıdır.',
                          'new_finding': 'Topikal antifungal ve çinko oksit bariyer krem başlandı. Eşlik '
                                         'eden oral pamukçuk için nistatin damla reçete edildi ve bez bakımı '
                                         'eğitimi verildi.'}]}]},
 {'id': 'G26',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '6 Yaş',
  'gender': 'Erkek',
  'complaint': 'Geceleri uykuda altını ıslatma ve yatağı kirletme şikayeti',
  'history': '6 yaşındaki erkek hasta, annesi tarafından acil polikliniğine getirildi. Annesi, oğlunun '
             'bezden çıktığı 3 yaşından beri hiçbir zaman 6 ay üst üste kuru kalmadığını, son birkaç aydır '
             'ise haftada 3-4 gece uykuda farkında olmadan yatağını ıslattığını anlatıyor. Gündüzleri idrar '
             'kaçırma, ani sıkışma hissi, kesik kesik idrar yapma veya damlatma olmuyor. İdrar yaparken '
             'yanma, ağrı, kabızlık veya aşırı su içme şikayeti yok. Okula yeni başlamış ve ailesi ceza '
             'yöntemi denediğinde tablonun kötüleştiğini ifade ediyor.',
  'final_diagnosis': 'Primer Monosemptomatik Noktürnal Enürezis',
  'disposition': 'Yeşil Alandan Aile Eğitimi, Yaşam Tarzı Önerileri ve Çocuk Nefroloji / Üroloji Poliklinik '
                 'Randevusu ile Taburculuk',
  'case_pearl': 'Beş yaşından büyük çocuklarda, gündüz semptomu veya organik patoloji olmaksızın sadece '
                'uykuda idrar kaçırma primer monosemptomatik noktürnal enürezis olarak adlandırılır. İlk '
                'basamakta tam idrar tahlili ve fizik muayene yeterlidir; invaziv ürolojik tetkik gerekmez. '
                'Tedavide suçlayıcı tutumun bırakılması, akşam sıvı kısıtlaması ve motivasyonel takip ilk '
                'adımdır; medikal (desmopresin) veya alarm tedavisi poliklinik takibinde planlanır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Geceleri uykuda idrar kaçırma şikayetiyle getirilen 6 yaşındaki bu hastada ilk '
                         'fizik muayene yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Acil serviste mesane disfonksiyonunu ve nörolojik kökeni araştırmak '
                                  'amacıyla hastayı hemen Sarı Alana devredip acil spinal manyetik rezonans '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'Sarı Alana devredilen hastanın genel durumu ve vital bulguları '
                                             'tamamen stabildi; acil sedasyonlu spinal görüntüleme '
                                             'endikasyonu bulunmadığı için yeşil alana geri yönlendirildi.',
                          'teaching_point': 'Nörolojik defisiti, lumbosakral anomalisi veya gündüz idrar '
                                            'semptomu olmayan çocuklarda acil nörogörüntüleme gerekmez; '
                                            'değerlendirme ayaktan yapılmalıdır.'},
                         {'text': 'Vital bulgularla birlikte batın muayenesi, lumbosakral omurga '
                                  'inspeksiyonu, alt ekstremite derin tendon refleksleri ve dış genital '
                                  'muayeneyi eksiksiz tamamlamak',
                          'is_correct': True,
                          'explanation': 'Uykuda alt ıslatma yakınmasında spina bifida okülta gibi nöropatik '
                                         'nedenleri dışlamak için lumbosakral bölge, kabızlığı ekarte etmek '
                                         'için batın muayenesi mutlaka yapılmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 86/dk, SS 20/dk, TA 95/60 mmHg. '
                                         'Batın rahat, glob vezikale veya kitle yok. Lumbosakral bölgede '
                                         'çukurcuk, kıllanma veya hiperpigmentasyon yok. Alt ekstremite '
                                         'nörolojik muayenesi ve anal sfinkter tonusu doğal. Genital '
                                         'muayenede mea darlığı veya sineşi izlenmedi.'},
                         {'text': 'Üretral obstrüksiyon veya posterior üretral valv şüphesiyle acil serviste '
                                  'idrar sondası takarak rezidü idrar miktarını ve mesane çıkım anatomisini '
                                  'değerlendirmek',
                          'is_correct': False,
                          'scenario_update': 'İdrar sondası takılması sırasında çocuk yoğun ajitasyon ve '
                                             'ağrı yaşadı; işlem sonrasında üretral travmaya bağlı geçici '
                                             'mikroskopik hematüri gelişti.',
                          'teaching_point': 'Gündüz semptomu olmayan ve işeme akımı normal olan çocukta '
                                            'invaziv üretral kateterizasyon kesinlikle endike değildir, '
                                            'travma ve enfeksiyon riskini artırır.'},
                         {'text': 'Şikayetin yalnızca gece uykuda ortaya çıktığını öğrenip fizik muayene '
                                  'yapmadan hastayı doğrudan çocuk psikiyatri polikliniğine yönlendirerek '
                                  'taburculuk planlamak',
                          'is_correct': False,
                          'scenario_update': 'Fizik muayene yapılmadığı için olası sakral disrafizm, '
                                             'kabızlık fekalomu veya eksternal genital anomaliler klinik '
                                             'olarak dışlanamamış oldu.',
                          'teaching_point': 'Psikolojik faktörler tetikleyici olabilse de lumbosakral ve '
                                            'genital muayene yapılmadan organik patolojiler dışlanamaz; '
                                            'fizik muayene atlanmamalıdır.'}]},
            {'stage_title': 'Laboratuvar ve Tetkik Stratejisi',
             'question': 'Fizik muayenesinde organik patoloji veya nörolojik defisit saptanmayan bu hastada '
                         'tetkik yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Mesane kapasitesini, duvar kalınlığını ve işeme sonrası rezidüel idrar '
                                  'volümünü belirlemek için acil üriner sistem ultrasonografisi ve ürodinami '
                                  'tetkiki istemek',
                          'is_correct': False,
                          'scenario_update': 'Acil şartlarda yapılan ultrasonda böbrek parankimi, toplayıcı '
                                             'sistemler ve mesane duvarı tamamen normal bulundu; invaziv '
                                             'ürodinami ise çocukta anksiyeteye yol açtı.',
                          'teaching_point': 'Monosemptomatik olgularda başlangıçta radyolojik görüntüleme '
                                            'veya ürodinamik çalışma endike değildir; bu tetkikler tedaviye '
                                            'yanıtsız veya komplike vakalara saklanır.'},
                         {'text': 'Kronik böbrek yetmezliği, elektrolit dengesizliği ve diabetes insipidus '
                                  'taraması için serum üre, kreatinin, elektrolitler ve sabah plazma '
                                  'osmolaritesi kanı almak',
                          'is_correct': False,
                          'scenario_update': 'Kan sonuçlarında üre 21 mg/dL, kreatinin 0.42 mg/dL, sodyum '
                                             '139 mEq/L, potasyum 4.3 mEq/L olup tüm biyokimyasal '
                                             'parametreler referans aralıkta geldi.',
                          'teaching_point': 'Büyüme-gelişme geriliği, gündüz polidipsi veya poliürisi '
                                            'bulunmayan stabil çocuklarda rutin venöz kan biyokimyası '
                                            'tetkiki maliyet-etkin değildir ve gereksizdir.'},
                         {'text': 'Glikozüri, proteinüri veya üriner enfeksiyonu dışlamak adına yalnızca tam '
                                  'idrar tahlili isteyip gereksiz ileri tetkiklerden kaçınmak',
                          'is_correct': True,
                          'explanation': 'Sadece uykuda idrar kaçıran, gündüz semptomu ve muayene bulgusu '
                                         'olmayan çocuklarda diabetes mellitus ve enfeksiyonu dışlamak için '
                                         'tam idrar analizi yeterlidir.',
                          'new_finding': 'TAM İDRAR TAHLİLİ: Dansite 1022, pH 6.0, Glukoz negatif, Protein '
                                         'negatif, Nitrit negatif, Lökosit esteraz negatif, Mikroskopi: 1-2 '
                                         'lökosit, eritrosit yok, bakteri görülmedi.'},
                         {'text': 'Mesane ve üretranın yapısal patolojilerini dışlamak amacıyla acil '
                                  'serviste kontrastlı işeme sistoüretrografisi çekilerek vezikoüreteral '
                                  'reflü varlığını araştırmak',
                          'is_correct': False,
                          'scenario_update': 'Kateter eşliğinde çekilen sistoüretrografide darlık veya kaçak '
                                             'saptanmadı ancak çocuk yüksek miktarda radyasyona ve üretral '
                                             'travmaya maruz kaldı.',
                          'teaching_point': 'İdrar yolu enfeksiyonu öyküsü, gündüz inkontinansı veya '
                                            'ultrasonografik anomali bulunmayan monosemptomatik olgularda '
                                            'sistoüretrografi kesinlikle endike değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Anamnez, fizik muayene ve tam idrar tahlili sonuçlarına göre en olası klinik '
                         'tanınız nedir?',
             'options': [{'text': 'Primer Monosemptomatik Noktürnal Enürezis',
                          'is_correct': True,
                          'explanation': 'Doğumdan itibaren 6 aydan uzun kuru döneminin olmaması (primer), '
                                         'gündüz hiçbir alt üriner sistem semptomunun bulunmaması '
                                         "(monosemptomatik) ve TİT'in normal olması primer monosemptomatik "
                                         'noktürnal enürezis tanısını kesinleştirir.',
                          'new_finding': 'Klinik tanı Primer Monosemptomatik Noktürnal Enürezis olarak '
                                         'kesinleştirildi; aileye durumun yaygın ve gelişimsel olduğu '
                                         'açıklandı.'},
                         {'text': 'Non-Monosemptomatik Noktürnal Enürezis',
                          'is_correct': False,
                          'scenario_update': 'Hastada gündüz idrar kaçırma, ani sıkışma, bacakları '
                                             'çaprazlama veya işeme sıklığında artış gibi gündüz semptomları '
                                             'bulunmadığı teyit edildi.',
                          'teaching_point': 'Non-monosemptomatik tanı için gece ıslatmasına gündüz '
                                            'inkontinansı, sıkışma veya disfonksiyonel işeme gibi alt üriner '
                                            'sistem semptomlarının eşlik etmesi gerekir.'},
                         {'text': 'Sekonder Noktürnal Enürezis',
                          'is_correct': False,
                          'scenario_update': 'Anamnez derinleştirildiğinde çocuğun bez bırakmadan sonra '
                                             'hiçbir zaman aralıksız altı ay kuru kalmadığı yeniden '
                                             'doğrulandı.',
                          'teaching_point': 'Sekonder tanı için çocuğun en az 6 ay boyunca tamamen kuru '
                                            'kaldığı bir dönemin ardından alt ıslatmanın yeniden başlamış '
                                            'olması şarttır.'},
                         {'text': 'Nörojenik Mesane Disfonksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Lumbosakral omurga, perineal duyu, anal refleks ve alt '
                                             'ekstremite nörolojik muayenesinde nöropatik mesaneyi '
                                             'düşündürecek patoloji saptanmadı.',
                          'teaching_point': 'Nörojenik mesanede spina bifida, anal sfinkter tonus kaybı, '
                                            'rektal disfonksiyon ve gündüz sürekli damlatma tarzında '
                                            'inkontinans beklenir.'}]},
            {'stage_title': 'Tedavi, Aile Eğitimi ve Taburculuk Planı',
             'question': 'Primer monosemptomatik noktürnal enürezis tanısı alan bu hastada acil servisteki '
                         'en uygun yönetim ve taburculuk planı hangisidir?',
             'options': [{'text': 'Acil servisten taburcu ederken yüksek doz oral desmopresin liyofilize '
                                  'tablet başlayıp sıvı kısıtlaması eğitimi vermeden hastayı kontrole '
                                  'çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Sıvı kısıtlaması eğitimi verilmeden yüksek doz desmopresin '
                                             'kullanan çocukta aşırı su içilmesine bağlı hiponatremi ve baş '
                                             'ağrısı semptomları gelişti.',
                          'teaching_point': 'Desmopresin başlanırken akşam sıvı kısıtlaması mutlaka '
                                            'anlatılmalıdır; ayrıca ilaç tedavisi acil serviste değil '
                                            'poliklinikte aile eğitimi sonrası başlanmalıdır.'},
                         {'text': 'Spesifik olmayan mesane kontraksiyonlarını baskılamak amacıyla acil '
                                  'serviste oral oksibutinin tedavisi başlayarak bir ay sonra kontrole '
                                  'çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Oral antikolinerjik başlanan çocukta belirgin ağız kuruluğu, '
                                             'yüzde kızarıklık ve kabızlık gelişti ancak gece yatak ıslatma '
                                             'sıklığı değişmedi.',
                          'teaching_point': 'Oksibutinin gibi antikolinerjikler gündüz aşırı aktif mesane '
                                            'semptomları olan non-monosemptomatik vakalarda kullanılır, '
                                            'izole monosemptomatik olgularda ilk basamak değildir.'},
                         {'text': 'Uykuda uyanma eşiğini düşürmek amacıyla trisiklik antidepresan olan '
                                  'imipramin tablet reçete edip aileye yakın takip önerisinde bulunmak',
                          'is_correct': False,
                          'scenario_update': 'Kardiyak aritmi ve fatal intoksikasyon riski taşıyan trisiklik '
                                             'antidepresan reçetesi ailede endişe yarattı ve çocukta '
                                             'sabahları aşırı sedasyon gözlendi.',
                          'teaching_point': 'Trisiklik antidepresanlar kardiyotoksisite ve dar terapötik '
                                            'aralıkları nedeniyle ilk seçenek değildir; dirençli vakalarda '
                                            'sadece uzman hekimce kullanılabilir.'},
                         {'text': 'Akşam sıvı alımını kısıtlama, işeme günlüğü tutma, cezalandırıcı '
                                  'yaklaşımdan kaçınma eğitimi vererek elektif çocuk nefroloji polikliniğine '
                                  'yönlendirmek',
                          'is_correct': True,
                          'explanation': 'Tedavinin ilk basamağı ailenin suçlayıcı tutumunun önlenmesi, '
                                         'motivasyonel takvim ve akşam sıvısının sınırlandırılmasıdır; alarm '
                                         'veya desmopresin elektif poliklinikte planlanır.',
                          'new_finding': 'Aileye suçlayıcı tutumdan kaçınmaları ve motivasyon takvimi '
                                         'tutmaları anlatıldı; poliklinik randevusu oluşturularak çocuk '
                                         'taburcu edildi.'}]}]},
 {'id': 'G27',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '5 Yaş',
  'gender': 'Kız',
  'complaint': 'Özellikle geceleri uykudan uyandıran şiddetli makat kaşıntısı ve huzursuzluk',
  'history': '5 yaşındaki kız çocuğu, annesi tarafından acil polikliniğine getirildi. Annesi, kızının '
             'yaklaşık 10 gündür özellikle yatağa yattıktan sonra başlayan perianal bölgede şiddetli '
             'kaşıntıdan yakındığını, sürekli poposunu kaşıdığını ve uykuya dalmakta zorlandığını '
             'belirtiyor. Gece huzursuz uyanmaları oluyormuş. Ateş, karın ağrısı, kusma, ishal veya kilo '
             'kaybı yok. Anaokuluna gittiği ve sınıfta benzer kaşıntı şikayeti olan başka çocukların da '
             'bulunduğu öğrenildi.',
  'final_diagnosis': 'Enterobiyazis (Kıl Kurdu Enfeksiyonu)',
  'disposition': 'Yeşil Alandan Antipareziter Tedavi, Tüm Aile Tedavisi ve Hijyen Eğitimi ile Taburculuk',
  'case_pearl': 'Enterobius vermicularis (kıl kurdu) çocuklarda en sık görülen paraziter enfeksiyondur ve '
                'tipik olarak geceleri perianal bölgeye göç eden dişi parazitlerin yol açtığı kaşıntıyla '
                'başvurur. Tanıda rutin gaita mikroskopisinin duyarlılığı düşüktür (<%10); altın standart '
                'sabah perianal bölgeden alınan selofan bant testidir. Tedavide pirantel pamoat veya '
                'mebendazol tek doz verilir; yumurtalara etkisiz olduğu için tüm aile bireyleri eş zamanlı '
                'tedavi edilmeli ve 2 hafta sonra doz mutlaka tekrarlanmalıdır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Geceleri artan perianal kaşıntı ve uykusuzluk şikayetiyle getirilen 5 yaşındaki '
                         'hastada en uygun klinik muayene yaklaşımı hangisidir?',
             'options': [{'text': 'Perianal kaşıntının derin rektal patolojilerden kaynaklanabileceğini '
                                  'düşünerek hastaya sedasyonsuz acil rektal tuşe ve dijital muayene '
                                  'uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Ağrılı dijital muayene nedeniyle çocuk yoğun korku ve '
                                             'ajitasyon yaşadı; rektal lümende kitle veya palpable kitle '
                                             'saptanmadı.',
                          'teaching_point': 'Yüzeyel perianal kaşıntı yakınmasında rektal kanama veya kitle '
                                            'şüphesi olmadıkça invaziv dijital rektal muayene endike '
                                            'değildir ve çocuğu travmatize eder.'},
                         {'text': 'Kaşıntının sistemik alerjik bir reaksiyona bağlı olduğunu varsayarak '
                                  'fizik muayeneyi yapmadan acil intramüsküler antihistaminik uygulayıp '
                                  'çocuğu gözleme almak',
                          'is_correct': False,
                          'scenario_update': 'Antihistaminik enjeksiyonu sonrası çocukta derin sedasyon '
                                             'gelişti ancak perianal bölge değerlendirilmediği için lokal '
                                             'patolojiler gözden kaçırıldı.',
                          'teaching_point': 'İzole perianal kaşıntıda sistemik anafilaksi veya ürtiker '
                                            'bulgusu yoksa sedatif antihistaminik enjeksiyonu yapılmamalı, '
                                            'öncelikle fizik muayene tamamlanmalıdır.'},
                         {'text': 'Vital bulgular, karın palpasyonu, sistemik cilt bakısı ve perianal '
                                  'bölgenin inspeksiyonunu eksfoliasyon ve eritem yönünden dikkatle '
                                  'değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Perianal kaşıntı olgularında anal fissür, streptokokal perianal '
                                         'dermatit ve kaşıntıya bağlı ekskoriasyonları ayırt etmek için '
                                         'perianal inspeksiyon yapılmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 94/dk, SS 20/dk, SpO2 %99. Batın '
                                         'rahat, defans veya organomegali yok. Perianal inspeksiyonda eritem '
                                         've tırnak izlerine bağlı yüzeyel ekskoriasyonlar görüldü; anal '
                                         'fissür, apse veya pürülan akıntı saptanmadı.'},
                         {'text': 'Perianal eritemi doğrudan idrar yolu enfeksiyonuna bağlayarak genital '
                                  'muayeneyi ertelemek ve çocuğu acil serviste idrar sondasıyla kateterize '
                                  'etmek',
                          'is_correct': False,
                          'scenario_update': 'Kateterizasyon sırasında çocukta şiddetli üretral rahatsızlık '
                                             'oluştu; idrar tahlili tamamen normal geldi ancak perianal '
                                             'patoloji aydınlatılamadı.',
                          'teaching_point': 'Dizüri veya ateş olmaksızın izole gece kaşıntısı olan olguda '
                                            'invaziv üriner kateterizasyon kesinlikle gereksizdir; perianal '
                                            'inspeksiyon önceliklidir.'}]},
            {'stage_title': 'Laboratuvar ve Tetkik Stratejisi',
             'question': 'Anamnezinde gece artan perianal kaşıntısı olan ve muayenede ekskoriasyon saptanan '
                         'bu çocukta en uygun tetkik yöntemi hangisidir?',
             'options': [{'text': 'Sabah uyanınca yıkama yapmadan perianal bölgeye şeffaf yapışkan bant '
                                  'yapıştırılarak hazırlanan lam preparatının mikroskopta incelenmesini '
                                  'planlamak',
                          'is_correct': True,
                          'explanation': 'Parazit yumurtaları perianal deriye bırakıldığından sabah perianal '
                                         'yapışkan bant mikroskopisi tanı koydurucudur; rutin dışkı '
                                         'incelemesinde yumurta saptanma oranı çok düşüktür.',
                          'new_finding': 'Yapışkan bant mikroskobik incelemesinde bir tarafı düz, diğer '
                                         'tarafı konveks karakteristik asimetrik parazit yumurtaları bol '
                                         'miktarda gözlendi.'},
                         {'text': 'Paraziter etkenleri saptamak amacıyla hastadan ardışık üç gün boyunca '
                                  'taze dışkı örneği toplanarak rutin gaita mikroskopisi istemek',
                          'is_correct': False,
                          'scenario_update': 'Gönderilen dışkı mikroskopisinde parazit kisti veya trofozoiti '
                                             'izlenmedi; yanlış negatif sonuç ailenin endişesini artırdı ve '
                                             'tanıyı geciktirdi.',
                          'teaching_point': 'Bu parazitin yumurtaları lümene değil perianal cilde '
                                            'bırakıldığından rutin gaita mikroskopisinin duyarlılığı yüzde '
                                            'beş ile on civarındadır, güvenilmezdir.'},
                         {'text': 'Perianal kaşıntının helmintik invazyona bağlı olup olmadığını anlamak '
                                  'için kanda total IgE ve periferik yaymada eozinofil sayımı istemek',
                          'is_correct': False,
                          'scenario_update': 'Laboratuvar sonucunda lökosit sayısı 6.800/mm³, eozinofil '
                                             'oranı %2, total IgE düzeyi normal sınırlarda geldi ve tanısal '
                                             'katkı sağlamadı.',
                          'teaching_point': 'Yüzeyel lümen içi parazitler doku invazyonu yapmadığından '
                                            'periferik eozinofili veya belirgin IgE yüksekliği oluşturmaz; '
                                            'kan tahlili gereksizdir.'},
                         {'text': 'Perianal derideki eritematöz lezyonlardan bakteriyel ve fungal sürüntü '
                                  'kültürü alarak mikrobiyolojik üreme sonucuna göre tedavi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Sürüntü kültüründe normal cilt florası bakterileri üredi; '
                                             'kültür sonucunu beklemek tanıyı ve tedaviyi en az iki gün '
                                             'gereksiz geciktirdi.',
                          'teaching_point': 'Pürülan akıntı, bül veya bal rengi krut yoksa izole kaşıntılı '
                                            'ekskoriasyonlarda rutin mikrobiyolojik kültür gönderilmesine '
                                            'gerek yoktur.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Anamnez, perianal inspeksiyon ve mikroskobik inceleme bulguları doğrultusunda en '
                         'olası klinik tanınız nedir?',
             'options': [{'text': 'Perianal Streptokokal Selülit',
                          'is_correct': False,
                          'scenario_update': 'Perianal bölgede parlak kırmızı, keskin sınırlı selülitik '
                                             'eritem veya defekasyon sırasında şiddetli kanamalı ağrı '
                                             'saptanmadı.',
                          'teaching_point': 'Streptokokal perianal hastalıkta gece kaşıntısından ziyade '
                                            'defekasyonda şiddetli acı, parlak kırmızı sınırları belirgin '
                                            'eritem ve rektal kanama ön plandadır.'},
                         {'text': 'İntestinal Giardiyazis Enfeksiyonu',
                          'is_correct': False,
                          'scenario_update': 'Hastada sulu, köpüklü veya yağlı ishal, karın krampları, gaz '
                                             've kilo kaybı gibi malabsorptif bağırsak semptomları '
                                             'bulunmadığı görüldü.',
                          'teaching_point': 'Giardiyazis lümen içi protozoon enfeksiyonu olup '
                                            'malabsorpsiyon, kronik ishal ve gaz sancısıyla seyreder; izole '
                                            'gece perianal kaşıntısı yapmaz.'},
                         {'text': 'Atopik Perianal Dermatit',
                          'is_correct': False,
                          'scenario_update': 'Çocukta atopi öyküsü, fleksural egzama lezyonları saptanmadı '
                                             've mikroskopide karakteristik yumurtaların görülmesi tanıyı '
                                             'dışladı.',
                          'teaching_point': 'Atopik dermatit kronik kaşıntı yapsa da mikroskobik parazit '
                                            'yumurtası görülmesi durumunda etken doğrudan spesifik paraziter '
                                            'enfeksiyondur.'},
                         {'text': 'Enterobiyazis (Kıl Kurdu Enfeksiyonu)',
                          'is_correct': True,
                          'explanation': 'Gece artan perianal kaşıntı, okulda benzer şikayet öyküsü ve '
                                         'yapışkan bantta asimetrik yumurtaların görülmesi Enterobius '
                                         'vermicularis (kıl kurdu) enfeksiyonu için patognomoniktir.',
                          'new_finding': 'Klinik tanı Enterobiyazis (Kıl Kurdu Enfeksiyonu) olarak '
                                         'kesinleştirildi.'}]},
            {'stage_title': 'Tedavi ve Profilaksi Planı',
             'question': 'Enterobiyazis tanısı kesinleşen bu hastada en uygun farmakolojik tedavi, aile '
                         'yaklaşımı ve hijyen stratejisi hangisi olmalıdır?',
             'options': [{'text': 'Yalnızca şikayeti olan çocuğa oral metronidazol süspansiyon başlayıp yedi '
                                  'gün süreyle kullanmasını ve aile bireylerine tedavi vermemeyi önermek',
                          'is_correct': False,
                          'scenario_update': 'Kullanılan metronidazol enterobiyazise karşı etkisiz kaldı; '
                                             'ayrıca aile bireyleri tedavi edilmediği için çocukta kısa süre '
                                             'sonra reenfeksiyon gelişti.',
                          'teaching_point': 'Metronidazol protozoonlara etkilidir, kıl kurduna etki etmez; '
                                            'ayrıca aile fertleri asemptomatik taşıyıcı olabileceğinden tüm '
                                            'aile eş zamanlı tedavi edilmelidir.'},
                         {'text': 'Hastaya ve tüm aile bireylerine tek doz pirantel pamoat verip iki hafta '
                                  'sonra dozu mutlaka tekrarlamak',
                          'is_correct': True,
                          'explanation': 'Antihelmintik ilaçlar paraziti öldürür ancak yumurtalara '
                                         'etkisizdir; otoenfeksiyonu önlemek için 2 hafta sonra 2. doz '
                                         'şarttır ve tüm aile eş zamanlı tedavi edilmelidir.',
                          'new_finding': 'Aileye tüm fertlerin tedavi edileceği, 14 gün sonra dozun '
                                         'tekrarlanacağı ve iç çamaşırlarının sıcak suyla yıkanıp '
                                         'ütüleneceği anlatılarak taburculuk sağlandı.'},
                         {'text': 'Sadece çocuğa tek doz oral albendazol vermek, iki hafta sonraki tekrar '
                                  'dozunu ise yalnızca kaşıntı devam ederse uygulamak',
                          'is_correct': False,
                          'scenario_update': 'İki hafta sonraki tekrar dozu verilmediği için hayatta kalan '
                                             'yumurtalardan çıkan yeni larvalar bir ay sonra kaşıntının '
                                             'nüksetmesine yol açtı.',
                          'teaching_point': 'Antihelmintikler yumurtaları yok edemez; yumurtadan çıkacak '
                                            'yeni kurtları öldürmek ve döngüyü kırmak için şikayet olmasa '
                                            'bile 2 hafta sonra ikinci doz şarttır.'},
                         {'text': 'Farmakolojik tedavi vermeden sadece perianal bölgeye topikal çinko oksit '
                                  'krem sürülmesini ve tırnakların kısa kesilmesini klinik olarak yeterli '
                                  'görmek',
                          'is_correct': False,
                          'scenario_update': 'Topikal bariyer krem kaşıntıyı kısmen azaltsa da bağırsak '
                                             'lümenindeki parazit yükü devam etti ve paraziter enfeksiyon '
                                             'kontrol altına alınamadı.',
                          'teaching_point': 'Hijyenik önlemler döngüyü kırmak için vazgeçilmez bir '
                                            'yardımcıdır ancak bağırsak lümenindeki etkeni eradike etmek '
                                            'için medikal antihelmintik tedavi zorunludur.'}]}]},
 {'id': 'G28',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '3.5 Aylık',
  'gender': 'Erkek',
  'complaint': 'Her beslenme sonrası ağızdan taşar tarzda, eforsuz ve ağrısız kusma',
  'history': '3.5 aylık erkek bebek, anne ve babası tarafından acil polikliniğine getirildi. Annesi, bebeğin '
             'son 1 aydır neredeyse her emzirme sonrasında sütün bir kısmını eforsuzca ağzından geri '
             'çıkardığını söylüyor. Kusmaların safrasız, kansız, beyaz süt renginde olduğu, fışkırır tarzda '
             'olmadığı ve bebek kusarken ağlamayıp neşeli kaldığı belirtildi. Doğum ağırlığı 3200 gr olan '
             'bebeğin şu an 6200 gr olduğu (ayda ~850 gr kilo alımı), bezlerinin bol idrarlı olduğu, ateş, '
             'öksürük veya solunum sıkıntısı bulunmadığı öğrenildi.',
  'final_diagnosis': "Fizyolojik Gastroözofageal Reflü ('Mutlu Kusan Bebek' / Happy Spitter)",
  'disposition': 'Yeşil Alandan Beslenme Pozisyonu ve Gaz Çıkarma Eğitimi Verilerek İlaçsız Taburculuk',
  'case_pearl': 'Süt çocuklarında alt özofagus sfinkterinin geçici gevşemelerine bağlı fizyolojik '
                "gastroözofageal reflü çok sıktır ve 'mutlu kusan bebek' (happy spitter) olarak "
                'adlandırılır. Kilo alımı normalse, hematemez, safralı kusma, aspirasyon bulgusu ve '
                'irritabilite yoksa bu durum reflü hastalığı (GÖRH) değil, selim fizyolojik bir süreçtir. '
                'Asit baskılayıcılar (PPI, H2 reseptör blokeri) veya motilite ajanları endike değildir; '
                'besleme sonrası dik tutma, gaz çıkarma ve aşırı beslenmeden kaçınma yeterlidir.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Her beslenme sonrası eforsuz kusma şikayetiyle getirilen 3.5 aylık bebeğin acil '
                         'servisteki ilk fizik muayene yaklaşımı hangisi olmalıdır?',
             'options': [{'text': 'Vital bulgular, tartı ölçümü, büyüme eğrisi, batın muayenesinde zeytin '
                                  'benzeri kitle ve hidrasyon durumunu kapsamlı olarak değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Kusan bebekte öncelikle kilo alımı, hidrasyon, batında pilor '
                                         'stenozu düşündürecek kitle veya distansiyon gibi kırmızı bayraklar '
                                         'dışlanmalıdır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 124/dk, SS 32/dk, SpO2 %99. Kilo '
                                         '6.200 gr (50. persentilde, mükemmel kilo alımı). Ön fontanel '
                                         'normal bombelikte, mukozalar ıslak, turgor doğal. Batın rahat, '
                                         'distansiyon veya palpabl kitle (zeytin kitle) yok. Akciğer sesleri '
                                         'doğal, çekilme yok.'},
                         {'text': 'Kusma şikayetinin intrakraniyal basınç artışına bağlı olabileceğini '
                                  'düşünerek bebeği acil serviste bekletmeden Sarı Alana devredip acil beyin '
                                  'tomografisi istemek',
                          'is_correct': False,
                          'scenario_update': 'Sarı Alana alınan bebeğin nörolojik muayenesi ve fontaneli '
                                             'tamamen normaldi; radyasyona yol açacak acil beyin '
                                             'görüntülemesi endikasyonu bulunmadığı belirtildi.',
                          'teaching_point': 'Genel durumu iyi, fontaneli normal ve nöromotor gelişimi olağan '
                                            'kusan süt çocuklarında kırmızı bayraklar olmadan santral '
                                            'patoloji düşünülüp tomografi istenmez.'},
                         {'text': 'Beslenme sonrası kusmanın akut cerrahi batına işaret edebileceğini '
                                  'öngörerek batın muayenesini derin ve ağrılı palpasyonla tekrarlayıp hemen '
                                  'nazogastrik sonda takmak',
                          'is_correct': False,
                          'scenario_update': 'Nazogastrik sonda takılması bebeği aşırı derecede ajite etti; '
                                             'mideden sadece sindirilmemiş süt geldi ve herhangi bir safra '
                                             'içeriği görülmedi.',
                          'teaching_point': 'Batını rahat, kilo alımı mükemmel ve safrasız kusan bebekte '
                                            'akut cerrahi batın düşünülmez; gereksiz nazogastrik '
                                            'dekompresyon travmaya neden olur.'},
                         {'text': 'Bebeğin neşeli ve aktif olduğunu gözlemleyip tartı ölçümü ve fizik '
                                  'muayene yapmadan anneyi sadece sakinleştirerek taburculuğa yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Tartı ölçümü ve muayene yapılmadığı için bebeğin büyüme eğrisi '
                                             've olası patolojik kusma nedenleri objektif olarak '
                                             'değerlendirilememiş oldu.',
                          'teaching_point': 'Kusan her süt çocuğunda büyüme persentili, tartı takibi ve '
                                            'hidrasyon değerlendirilmesi fizyolojik ve patolojik süreçleri '
                                            'ayırt etmede zorunludur.'}]},
            {'stage_title': 'Laboratuvar ve Tetkik Stratejisi',
             'question': 'Kilo alımı ve hidrasyonu mükemmel, batını rahat olan bu bebekte acil serviste '
                         'tetkik stratejiniz ne olmalıdır?',
             'options': [{'text': 'Pilor stenozu ve intestinal malrotasyonu dışlamak amacıyla bebeğe acil '
                                  'baryumlu üst gastrointestinal sistem pasaj grafisi çektirmek',
                          'is_correct': False,
                          'scenario_update': 'Kontrastlı pasaj grafisinde baryumun mideye ve duodenuma '
                                             'geçişi normal bulundu ancak bebek kontrast madde aspirasyonu '
                                             'riskiyle karşı karşıya kaldı.',
                          'teaching_point': 'Safrasız kusan ve kilo alımı persentil üzerinde olan bebekte '
                                            'intestinal malrotasyon veya pilor stenozu düşünülerek acil '
                                            'kontrastlı grafi çekilmez.'},
                         {'text': 'Kusmaya bağlı gelişebilecek hipokloremi, hipokalemi ve metabolik alkalozu '
                                  'belirlemek için acil kan gazı ve venöz elektrolit paneli çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Kan gazında pH 7.39, pCO2 38 mmHg, HCO3 23 mmol/L, sodyum 138 '
                                             'mEq/L, potasyum 4.4 mEq/L, klor 102 mEq/L normal sınırlarda '
                                             'geldi.',
                          'teaching_point': 'Fışkırır tarzda kusması olmayan, dehidrate bulunmayan ve '
                                            'beslenmesi iyi bebeklerde elektrolit bozukluğu beklenmez; '
                                            'invaziv kan alımı gereksizdir.'},
                         {'text': 'Özofagus lümeninde mikroskopik erozyon ve kanamayı araştırmak için '
                                  'dışkıda gizli kan testi ve acil üst gastrointestinal endoskopi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Dışkıda gizli kan negatif bulundu; çocuk gastroenteroloji '
                                             'konsültanı asemptomatik ve kilo alan bu bebekte endoskopi '
                                             'endikasyonu olmadığını bildirdi.',
                          'teaching_point': 'Hematemez, demir eksikliği anemisi veya belirgin büyüme '
                                            'geriliği bulunmayan kusan bebeklerde invaziv endoskopik biyopsi '
                                            'endikasyonu yoktur.'},
                         {'text': 'Kırmızı bayrak bulgusu ve gelişim geriliği bulunmadığı için herhangi bir '
                                  'laboratuvar veya görüntüleme tetkiki istememek',
                          'is_correct': True,
                          'explanation': 'Kilo alımı çok iyi olan, safrasız, eforsuz kusan ve hidrasyonu '
                                         'normal bebeklerde ileri laboratuvar veya radyolojik inceleme '
                                         'endike değildir.',
                          'new_finding': 'Tetkik istenmedi; aileye bebeğin organ muayenesinin, hidrasyonunun '
                                         've tartı artışının tamamen sağlıklı olduğu bilgisi verildi.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Anamnez, fizik muayene ve mükemmel kilo alımı bulguları ışığında bu bebeğin en '
                         'olası tanısı nedir?',
             'options': [{'text': 'Gastroözofageal Reflü Hastalığı (GÖRH)',
                          'is_correct': False,
                          'scenario_update': 'Bebekte hematemez, beslenmeyi reddetme, kilo alamama, stridor '
                                             'veya apne gibi patolojik reflü hastalığı bulguları saptanmadı.',
                          'teaching_point': 'Reflü hastalığı (GÖRH) tanısı için basit regürjitasyonun '
                                            'ötesinde büyüme geriliği, özofajit, hematemez veya solunumsal '
                                            'komplikasyonlar bulunmalıdır.'},
                         {'text': "Fizyolojik Gastroözofageal Reflü ('Mutlu Kusan Bebek')",
                          'is_correct': True,
                          'explanation': 'Eforsuz kusmalara rağmen kilo alımının mükemmel olması, kusma '
                                         'sırasında ağrı veya irritabilite olmaması fizyolojik '
                                         "gastroözofageal reflü ('mutlu kusan bebek') tablosunu kanıtlar.",
                          'new_finding': "Klinik tanı Fizyolojik Gastroözofageal Reflü ('Mutlu Kusan Bebek') "
                                         'olarak kesinleştirildi; durumun selim olduğu aileye açıklandı.'},
                         {'text': 'İnfantil Hipertrofik Pilor Stenozu',
                          'is_correct': False,
                          'scenario_update': 'Kusmaların fışkırır tarzda olmaması, kilo alımının 50. '
                                             'persentilde seyretmesi ve batında zeytin kitle bulunmaması '
                                             'pilor stenozunu dışladı.',
                          'teaching_point': 'Pilor darlığında tipik olarak 3-6 haftalıkken başlayan fışkırır '
                                            'tarzda safrasız kusma, kilo kaybı ve hipokloremik metabolik '
                                            'alkaloz gelişir.'},
                         {'text': 'İnek Sütü Proteini İlişkili Proktokolit',
                          'is_correct': False,
                          'scenario_update': 'Dışkıda mukus veya taze kan çizgileri bulunmadığı, bebeğin '
                                             'derisinde egzama veya atopik lezyon olmadığı gözlendi.',
                          'teaching_point': 'İnek sütü proktokolitinde temel başvuru bulgusu dışkıda kan ve '
                                            'mukustur; izole kilo alımı iyi olan eforsuz kusma alerjik '
                                            'kolitle uyuşmaz.'}]},
            {'stage_title': 'Tedavi ve Aile Eğitimi Planı',
             'question': "Fizyolojik reflü tanısı alan bu 'mutlu kusan bebek' için en uygun tedavi ve "
                         'taburculuk yaklaşımı hangisidir?',
             'options': [{'text': 'Kusma sıklığını azaltmak amacıyla hemen oral proton pompa inhibitörü '
                                  'süspansiyon ve motilite artırıcı prokinetik şurup tedavisi başlamak',
                          'is_correct': False,
                          'scenario_update': 'Asit baskılayıcı ilaç başlanan bebekte iki hafta sonra '
                                             'nekrotizan enterokolit riski, gastrointestinal disbiyozis ve '
                                             'solunum yolu enfeksiyonu sıklığı arttı.',
                          'teaching_point': 'Kilo alımı iyi olan selim reflüde proton pompa inhibitörleri ve '
                                            'prokinetikler etkisizdir; pnömoni ve bağırsak enfeksiyonu '
                                            'riskini artırdığı için kontrendikedir.'},
                         {'text': 'Anne sütünü derhal keserek bebeği yoğunlaştırılmış pirinçli antireflü '
                                  'formül mamaya ve koyulaştırıcı mama takviyelerine geçirmeyi aileye '
                                  'önermek',
                          'is_correct': False,
                          'scenario_update': 'Anne sütünün kesilmesi bebekte kabızlığa ve annenin süt '
                                             'üretiminin hızla azalmasına neden oldu; ailede belirgin '
                                             'emzirme stresi yaşandı.',
                          'teaching_point': 'Anne sütü koruyucudur ve sindirimi kolaydır; fizyolojik '
                                            'kusmaları olan bebekte anne sütü kesinlikle kesilmemeli ve '
                                            'formül mamaya geçilmemelidir.'},
                         {'text': 'İlaç tedavisi vermeden beslenme sonrası dik tutma, gaz çıkarma ve aşırı '
                                  'beslenmeden kaçınma eğitimiyle bebeği taburcu etmek',
                          'is_correct': True,
                          'explanation': 'Fizyolojik reflüde asit baskılayıcı ilaçlar etkisizdir ve yan etki '
                                         'riskini artırır; dik pozisyon, sık aralıklarla uygun hacimde '
                                         'besleme ve gaz çıkarma yeterlidir.',
                          'new_finding': 'Anneye beslenme sonrası bebeği 20-30 dakika dik tutması, gazını '
                                         'çıkarması ve kırmızı bayraklar (safralı kusma, ateş, kilo '
                                         'duraklaması) anlatılarak taburcu edildi.'},
                         {'text': 'Mide asiditesini nötralize etmek için her beslenmeden önce antiasit '
                                  'magnezyum ve alüminyum hidroksit süspansiyon verilmesini reçete etmek',
                          'is_correct': False,
                          'scenario_update': 'Alüminyum içeren antiasit verilen süt çocuğunda serum '
                                             'alüminyum toksisitesi ve mineral metabolizması bozukluğu riski '
                                             'ortaya çıktı.',
                          'teaching_point': 'Süt çocuklarında magnezyum veya alüminyum içeren antiasitler '
                                            'elektrolit dengesizliği ve sistemik toksisite '
                                            'oluşturabileceğinden kesinlikle kullanılmaz.'}]}]},
 {'id': 'G29',
  'category': '👂 Kulak Ağrısı & KBB',
  'age': '4 Yaş',
  'gender': 'Erkek',
  'complaint': 'Televizyonu yüksek sesle dinleme, seslenildiğinde bakmama ve işitme güçlüğü',
  'history': '4 yaşındaki erkek çocuk, annesi tarafından acil polikliniğine getirildi. Annesi, çocuğun son 3 '
             'haftadır televizyonu çok yakından ve sesini aşırı açarak izlediğini, arkasından '
             'seslenildiğinde çoğu zaman duymadığını veya yanıt vermediğini anlatıyor. Akut kulak ağrısı, '
             'kulaktan akıntı veya ateş tariflenmiyor. Yaklaşık 1 ay önce hafif bir viral üst solunum yolu '
             'enfeksiyonu geçirdiği öğrenildi. Çocuğun genel durumu iyi, beslenmesi ve uykusu düzenli.',
  'final_diagnosis': 'Efüzyonlu Otitis Media (Seröz Otit)',
  'disposition': 'Yeşil Alandan Antibiyotiksiz İzlem, Aile Eğitimi ve 3 Ay Sonra Elektif KBB Kontrolü ile '
                 'Taburculuk',
  'case_pearl': 'Efüzyonlu otitis media (EOM / seröz otit), akut enfeksiyon bulguları (ateş, kulak ağrısı, '
                'zarda belirgin bombeleşme/eritem) olmaksızın timpanik membran arkasında sıvı toplanmasıdır. '
                'Genellikle viral ÜSYE veya AOM atağını takiben gelişir ve en sık başvuru semptomu '
                'hafif-orta derecede iletim tipi işitme kaybıdır (TV sesini açma, seslenince bakmama). '
                "Vakaların %75-90'ı 3 ay içinde kendiliğinden düzelir. Antibiyotikler, oral/nazal "
                'dekonjestanlar ve kortikosteroidler etkisizdir ve önerilmez. 3 aydan uzun süren veya '
                'konuşma geriliği yapan olgularda KBB tarafından tüp takılması planlanır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'İşitme azlığı ve seslenildiğinde yanıt vermeme şikayetiyle getirilen 4 yaşındaki '
                         'çocukta en uygun fizik muayene yaklaşımı hangisidir?',
             'options': [{'text': 'Ani gelişen işitme kaybının intrakraniyal kitleye bağlı olabileceğini '
                                  'düşünerek hastayı acil Sarı Alana devredip acil beyin manyetik rezonansı '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'Sarı Alana yönlendirilen çocuğun nörolojik muayenesi ve '
                                             'kranial sinirleri tamamen intakt bulundu; acil santral '
                                             'görüntüleme endikasyonu olmadığı bildirildi.',
                          'teaching_point': 'Öncesinde nezle öyküsü olan, bilateral ve ağrısız işitme '
                                            'azalmasında nörolojik defisit yoksa acil santral görüntüleme '
                                            'gerekmez; kulak muayenesi önceliklidir.'},
                         {'text': 'Kulak kanalını incelemeden önce işitme kaybının akut mastoidite bağlı '
                                  'olabileceğini varsayarak hastayı acil temporal kemik bilgisayarlı '
                                  'tomografisine göndermek',
                          'is_correct': False,
                          'scenario_update': 'Retroauriküler eritem, ödem veya kulak kepçesinde öne itilme '
                                             'gibi hiçbir mastoidit bulgusu olmayan çocukta gereksiz yüksek '
                                             'doz radyasyon maruziyeti oluştu.',
                          'teaching_point': 'Mastoidit retroauriküler şişlik, kızarıklık ve sistemik ateşle '
                                            'seyreder; bu bulgular olmadan izole işitme güçlüğünde '
                                            'bilgisayarlı tomografi endike değildir.'},
                         {'text': 'Çocuğun seslenince bakmamasını tamamen davranışsal ve psikolojik bir '
                                  'sorun olarak kabul edip otoskopik muayeneyi atlayarak çocuk '
                                  'psikiyatrisine sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'Kulak zarları incelenmediği için orta kulak patolojisi tamamen '
                                             'atlandı ve çocuk gereksiz yere davranışsal değerlendirme '
                                             'sürecine sokuldu.',
                          'teaching_point': 'Seslenince bakmama veya televizyon sesini açma yakınmasında '
                                            'davranışsal tanı düşünülmeden önce mutlaka ayrıntılı otoskopik '
                                            'kulak muayenesi yapılmalıdır.'},
                         {'text': 'Vital bulguları kaydedip pnömatik otoskopi ile timpanik membranın rengi, '
                                  'pozisyonu, saydamlığı ve mobilitesini dikkatle değerlendirmek',
                          'is_correct': True,
                          'explanation': 'İşitme azlığı yakınmasında akut inflamasyon varlığını, zar '
                                         'arkasında sıvı toplanmasını ve zar mobilitesindeki kısıtlılığı '
                                         'saptamak için pnömatik otoskopi esastır.',
                          'new_finding': 'Vital Bulgular: Ateş 36.6°C, KTA 90/dk, SS 22/dk, SpO2 %99. '
                                         'Orofarenks sakin. Otoskopide: Bilateral timpanik membranlar '
                                         'matlaşmış, retrakte görünümde, ışık refleksi silik; zar arkasında '
                                         'sarımsı sıvı birikimi ve hava kabarcıkları izlendi, bombeleşme '
                                         'veya hiperemi yok. Pnömatik otoskopide zar mobilitesi belirgin '
                                         'azalmış.'}]},
            {'stage_title': 'Laboratuvar ve Tetkik Stratejisi',
             'question': 'Otoskopisinde zar arkasında hava-sıvı seviyesi saptanan, ateşi ve kulak ağrısı '
                         'olmayan bu çocukta tetkik yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Orta kulaktaki sıvının bakteriyel enfeksiyon belirteci olup olmadığını '
                                  'netleştirmek amacıyla acil tam kan sayımı ve CRP tetkiki istemek',
                          'is_correct': False,
                          'scenario_update': 'Laboratuvar tetkiklerinde lökosit sayısı 7.200/mm³, CRP 1.1 '
                                             'mg/L olarak tamamen normal sınırlarda geldi ve klinik '
                                             'yaklaşımı değiştirmedi.',
                          'teaching_point': 'Ateş veya akut ağrısı olmayan orta kulak sıvı birikimlerinde '
                                            'sistemik inflamasyon belirteçleri tanısal değer taşımaz ve '
                                            'bakılmamalıdır.'},
                         {'text': 'Acil serviste kan tahlili veya radyoloji istemeyip elektif poliklinikte '
                                  'timpanometri ve odyometrik işitme testi planlamak',
                          'is_correct': True,
                          'explanation': 'Akut inflamasyon bulgusu olmayan olgularda kan veya radyolojik '
                                         'tetkik gerekmez; tanı ve izlemde objektif değerlendirme '
                                         'timpanometri ve odyometri ile yapılır.',
                          'new_finding': 'Acil kan ve radyolojik tetkik istenmedi; hastanın izlemi için '
                                         'kulak burun boğaz polikliniğinde Tip B timpanogram ve işitme '
                                         'değerlendirmesi önerildi.'},
                         {'text': 'Sıvı içeriğinin etken mikrobiyolojisini belirlemek amacıyla acil serviste '
                                  'parasentez ve timpanosentez uygulayarak orta kulak sıvısından kültür '
                                  'almak',
                          'is_correct': False,
                          'scenario_update': 'Acil serviste timpanosentez girişimi sırasında çocuk şiddetli '
                                             'ağrı duydu ve timpanik membranda travmatik mikro-perforasyon '
                                             'gelişti.',
                          'teaching_point': 'Timpanosentez acil serviste elektif sıvı toplanmasında '
                                            'uygulanmaz; yalnızca toksik, dirençli ve bağışıklık yetmezliği '
                                            'olan komplike vakalarda KBB uzmanlarınca yapılır.'},
                         {'text': 'Miringoskleroz ve olası kemikçik zincir anomalilerini değerlendirmek için '
                                  'acil serviste yüksek çözünürlüklü temporal kemik bilgisayarlı tomografisi '
                                  'çekmek',
                          'is_correct': False,
                          'scenario_update': 'Tomografi sonucunda orta kulak boşluklarında aerasyon kaybı '
                                             'dışında kemik destrüksiyonu izlenmedi; çocuk gereksiz '
                                             'radyasyona maruz bırakıldı.',
                          'teaching_point': 'Kolesteatom, intrakraniyal yayılım veya kemik erozyonu şüphesi '
                                            'olmayan olgularda temporal bilgisayarlı tomografi çekilmesi '
                                            'kesinlikle kontrendikedir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Anamnez, fizik muayene ve otoskopik bulgular ışığında bu hastada en olası klinik '
                         'tanınız nedir?',
             'options': [{'text': 'Akut Süpüratif Otitis Media',
                          'is_correct': False,
                          'scenario_update': 'Timpanik membranda belirgin bombeleşme, kızarıklık, akut '
                                             'otalji ve sistemik ateş bulunmadığı yeniden teyit edildi.',
                          'teaching_point': 'Akut otitis media tanısı için timpanik membranda belirgin '
                                            'bombeleşme, akut eritem ve eşlik eden şiddetli kulak ağrısı ya '
                                            'da ateş şarttır.'},
                         {'text': 'Kronik Süpüratif Otitis Media',
                          'is_correct': False,
                          'scenario_update': 'Muayenede timpanik membranda kalıcı delinme veya dış kulak '
                                             'yoluna kronik pürülan akıntı olmadığı görüldü.',
                          'teaching_point': 'Kronik süpüratif otit timpanik membranda kalıcı perforasyon ve '
                                            'en az altı haftadır devam eden pürülan akıntı ile tanımlanır.'},
                         {'text': 'Efüzyonlu Otitis Media (Seröz Otit)',
                          'is_correct': True,
                          'explanation': 'Akut enfeksiyon bulgusu (ateş, ağrı, bombeleşme) olmadan timpanik '
                                         'membran arkasında sıvı ve hava kabarcıkları varlığı efüzyonlu '
                                         'otitis media için tipiktir.',
                          'new_finding': 'Klinik tanı Efüzyonlu Otitis Media (Seröz Otit) olarak '
                                         'netleştirildi.'},
                         {'text': 'Kanal İçi Tıkacı (Serümen Bitişi)',
                          'is_correct': False,
                          'scenario_update': 'Dış kulak yolunun tamamen açık olduğu, zarı kapatan buşon veya '
                                             'yabancı cisim bulunmadığı otoskopide netleştirildi.',
                          'teaching_point': 'Serümen tıkacında işitme kaybı dış kulak yolunun tıkanmasına '
                                            'bağlıdır ve buşon nedeniyle timpanik membran muayene '
                                            'edilemez.'}]},
            {'stage_title': 'Tedavi ve İzlem Planı',
             'question': 'Efüzyonlu otitis media tanısı alan bu çocuk için güncel kılavuzlara göre en uygun '
                         'yönetim planı hangisidir?',
             'options': [{'text': 'Antibiyotik veya dekonjestan vermeden izlem kararı alıp aileyi '
                                  'bilgilendirerek üç ay sonra poliklinik kontrolü önermek',
                          'is_correct': True,
                          'explanation': 'Olguların çoğu 3 ay içinde spontan düzelir; antibiyotikler, '
                                         'antihistaminikler ve dekonjestanlar etkisizdir. 3 ayı aşan '
                                         'efüzyonda KBB değerlendirmesi gerekir.',
                          'new_finding': 'Aileye durumun nezle sonrası geliştiği, çoğu vakada kendiliğinden '
                                         'geçtiği anlatıldı; okulda öğretmene işitme azlığının bildirilmesi '
                                         've 3 ay sonra KBB kontrolü planlandı.'},
                         {'text': 'Orta kulaktaki sıvının rezolüsyonunu hızlandırmak amacıyla yüksek doz '
                                  'oral amoksisilin-klavulanat süspansiyon ve nazal kortikosteroid sprey '
                                  'tedavisi başlamak',
                          'is_correct': False,
                          'scenario_update': 'On günlük antibiyotik kullanımı sonrası çocukta yaygın '
                                             'antibiyotiğe bağlı diyare gelişti ancak orta kulaktaki sıvı '
                                             'varlığı ve işitme kaybı devam etti.',
                          'teaching_point': 'Efüzyonlu otitis mediada bakteriyel eradikasyon '
                                            'hedeflenmediğinden antibiyotikler ve steroidler uzun dönemde '
                                            'sıvıyı rezolve etmez; kılavuzlarca önerilmez.'},
                         {'text': 'Östaki disfonksiyonunu gidermek amacıyla sistemik psödoefedrin şurup ve '
                                  'sedatif birinci kuşak oral antihistaminik kombinasyonunu reçete ederek '
                                  'taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Kombine şurup kullanımı çocukta sinirlilik, uykusuzluk ve '
                                             'taşikardiye yol açtı; östaki tüp fonksiyonlarında veya '
                                             'işitmede hiçbir düzelme sağlanamadı.',
                          'teaching_point': 'Oral dekonjestanlar ve antihistaminikler efüzyonlu otitte '
                                            'klinik iyileşme sağlamadığı gibi çocuklarda belirgin '
                                            'nöropsikiyatrik ve kardiyovasküler yan etki yapar.'},
                         {'text': 'İşitme kaybı saptandığı için çocuğu acil servisten taburcu etmeden aynı '
                                  'gün ameliyathaneye alarak bilateral ventilasyon tüpü tatbik etmek',
                          'is_correct': False,
                          'scenario_update': 'Acil serviste cerrahi girişim endikasyonu olmadığı, olguların '
                                             'çoğunun ilk üç ayda spontan rezolüsyona uğradığı KBB '
                                             'kliniğince hatırlatıldı.',
                          'teaching_point': 'Ventilasyon tüpü tatbiki akut bir acil müdahale değildir; en az '
                                            'üç ay süren bilateral efüzyon ve işitme/konuşma geriliği '
                                            'varlığında elektif olarak planlanır.'}]}]},
 {'id': 'G30',
  'category': '👂 Kulak Ağrısı & KBB',
  'age': '7 Yaş',
  'gender': 'Kız',
  'complaint': 'Sol boyunda 2 haftadır ele gelen ve ağrısız olan küçük şişlik',
  'history': '7 yaşındaki kız çocuğu, annesi tarafından boynundaki şişlik nedeniyle acil servise getirildi. '
             'Annesi, yaklaşık 2 hafta önce çocuğun hafif burun akıntısı ve boğaz ağrısı ile seyreden viral '
             'bir üst solunum yolu enfeksiyonu geçirdiğini, bu enfeksiyondan birkaç gün sonra sol boyun '
             'bölgesinde fındık büyüklüğünde bir beze fark ettiğini söylüyor. Şişlikte belirgin kızarıklık, '
             'sıcaklık artışı veya ağrı olmamış. Son 2 haftada boyutta büyüme veya küçülme gözlenmemiş. '
             'Ateş, gece terlemesi, kilo kaybı, halsizlik veya kemik ağrısı yok.',
  'final_diagnosis': 'Reaktif Servikal Lenfadenopati',
  'disposition': 'Yeşil Alandan Aile Eğitimi, Kırmızı Bayrak Bulguları Bilgilendirmesi ve 3-4 Hafta Sonra '
                 'Poliklinik Kontrolü ile Taburculuk',
  'case_pearl': 'Çocukluk çağında servikal lenfadenopatilerin en sık nedeni geçirilmiş viral üst solunum '
                'yolu enfeksiyonlarına bağlı reaktif lenf bezi hiperplazisidir. Tipik olarak <2 cm, mobil, '
                'yumuşak-elastik kıvamda, ağrısızdır; üzerindeki deride eritem/ısı artışı yoktur ve B '
                'semptomları (ateş, kilo kaybı, gece terlemesi) eşlik etmez. Fiks, sert, konglomere, '
                "supraklaviküler yerleşimli veya 2 cm'den büyük nodüller malignite/granülomatöz hastalık "
                'açısından ileri inceleme gerektirir. Akut süpürasyon ve sistemik bulgu yoksa antibiyotik, '
                'acil biyopsi veya gereksiz kan tetkiki endike değildir; 3-4 hafta gözlem en doğru '
                'yaklaşımdır.',
  'steps': [{'stage_title': 'İlk Değerlendirme ve Fizik Muayene',
             'question': 'Boynunda 2 haftadır ele gelen şişlik şikayetiyle başvuran 7 yaşındaki çocukta ilk '
                         'fizik muayene yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Boyundaki kitlenin olası lenfoma veya nöroblastom metastazı olabileceğini '
                                  'öngörerek hastayı hemen Sarı Alana devredip acil boyun tomografisi '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'Sarı Alana yönlendirilen stabil hastada kitle bulgusu veya '
                                             'hava yolu basısı saptanmadı; acil serviste kontrastlı boyun '
                                             'tomografisi endikasyonu olmadığı bildirildi.',
                          'teaching_point': 'Genel durumu iyi, B semptomu olmayan ve mobil küçük lenf '
                                            'nodlarında acil radyasyonlu tomografi endike değildir; ayaktan '
                                            'benign değerlendirme esastır.'},
                         {'text': 'Vital bulgular, lenf nodunun boyutu, kıvamı, mobilitesi ile '
                                  'supraklaviküler bölge, orofarenks ve hepatosplenomegaliyi dikkatle '
                                  'değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Lenf bezi büyümesiyle gelen çocukta malignite ve sistemik '
                                         'enfeksiyonları dışlamak için lenf bezinin karakteri, diğer lenf '
                                         'istasyonları ve organomegali muayene edilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.7°C, KTA 84/dk, SS 18/dk, SpO2 %100. Sol '
                                         'anterior servikal zincirde yaklaşık 1.5 cm çapında, '
                                         'yumuşak-elastik, çevre dokulara fikse olmayan mobil, hassasiyetsiz '
                                         'lenf nodu palpe edildi. Üzerindeki cilt doğal, ısı artışı veya '
                                         'fluktuasyon yok. Supraklaviküler, aksiller veya inguinal lenf bezi '
                                         'yok. Hepatosplenomegali saptanmadı. Tonsiller ve orofarenks '
                                         'sakin.'},
                         {'text': 'Fluktuasyon veya derin apse varlığını netleştirmek amacıyla acil serviste '
                                  'kalın iğne aspirasyonu uygulayarak lenf nodu içeriğini boşaltmak',
                          'is_correct': False,
                          'scenario_update': 'Aspirasyon girişimi sırasında lenf nodundan pürülan içerik '
                                             'gelmedi; travmaya bağlı lokal hematom ve çocukta yoğun '
                                             'anksiyete oluştu.',
                          'teaching_point': 'Eritem, ısı artışı ve fluktuasyon olmayan küçük lenf nodlarında '
                                            'körlemesine acil iğne aspirasyonu kontrendikedir; enfeksiyon ve '
                                            'hematom riski yaratır.'},
                         {'text': 'Şişliğin sadece sol tarafta olması nedeniyle derin boyun apsesi '
                                  'şüphesiyle çocuğu derhal ameliyathaneye alıp acil açık insizyon ve drenaj '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'Ateşi, trismusu, yutma güçlüğü veya sellüliti olmayan çocukta '
                                             'acil cerrahi drenaj planlanması gereksiz cerrahi invazyon '
                                             'riski oluşturdu.',
                          'teaching_point': 'Süpürasyon veya derin fasyal plan apsesi bulgusu bulunmayan '
                                            'asemptomatik servikal lenf nodlarında acil cerrahi insizyon '
                                            'kesinlikle yapılmaz.'}]},
            {'stage_title': 'Laboratuvar ve Tetkik Stratejisi',
             'question': 'Fizik muayenesinde sol servikalde 1.5 cm mobil, hassasiyetsiz nodül saptanan, '
                         'genel durumu iyi çocukta tetkik stratejiniz ne olmalıdır?',
             'options': [{'text': 'Kırmızı bayrak bulguları ve sistemik semptom bulunmadığı için acil '
                                  'laboratuvar veya invaziv biyopsi yapmadan izlem kararı vermek',
                          'is_correct': True,
                          'explanation': 'Viral enfeksiyon sonrası gelişen, <2 cm, mobil ve hassasiyetsiz '
                                         'lenf bezlerinde B semptomu yoksa rutin laboratuvar veya acil '
                                         'biyopsi gerekmez.',
                          'new_finding': 'Acil tetkik veya biyopsi istenmedi; aileye mevcut bulguların '
                                         'geçirilmiş üst solunum yolu enfeksiyonuna bağlı selim bağışıklık '
                                         'yanıtı olduğu açıklandı.'},
                         {'text': 'Lenfoproliferatif hastalıkları ve lösemiyi ekarte etmek amacıyla acil '
                                  'serviste kemik iliği aspirasyonu ve eksizyonel lenf nodu biyopsisi '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'Hematoloji kliniği sistemik bulgusu, sitopenisi veya '
                                             'hepatosplenomegalisi olmayan hastada invaziv kemik iliği ve '
                                             'biyopsi endikasyonu bulunmadığını bildirdi.',
                          'teaching_point': 'Çocuklarda maligniteyi düşündüren sert/fiks kıvam, '
                                            'supraklaviküler yerleşim veya organomegali yoksa acil serviste '
                                            'biyopsi veya kemik iliği tetkiki istenmez.'},
                         {'text': 'Gizli granülomatöz enfeksiyonları araştırmak amacıyla acil serviste PPD '
                                  'deri testi, tüberküloz kültürü ve toraks bilgisayarlı tomografisi istemek',
                          'is_correct': False,
                          'scenario_update': 'Toraks tomografisinde mediastinal lenfadenopati veya '
                                             'parankimal lezyon izlenmedi; çocuk gereksiz radyasyona maruz '
                                             'bırakıldı.',
                          'teaching_point': 'Kronik süpürasyon, fistülizasyon veya tüberküloz temas öyküsü '
                                            'olmayan izole servikal lenf nodlarında acil toraks tomografisi '
                                            'rutin olarak endike değildir.'},
                         {'text': 'Viral etyolojileri ayrıntılandırmak için EBV, CMV, Toksoplazma, '
                                  'Bartonella ve HIV serolojilerini kapsayan geniş enfeksiyon paneli kanı '
                                  'göndermek',
                          'is_correct': False,
                          'scenario_update': 'Geniş serolojik panel sonuçlarının çıkmasının günler süreceği '
                                             'anlaşıldı; acil şartlarda hastanın klinik yönetimine hiçbir '
                                             'anlık katkı sağlamadı.',
                          'teaching_point': 'Sistemik ateş, hepatosplenomegali veya atipik lenfosit artışı '
                                            'olmayan selim lenf bezi büyümelerinde acil serviste geniş '
                                            'serolojik panel çalışılması maliyet-etkin değildir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Geçirilmiş viral enfeksiyon öyküsü, fizik muayenede mobil yumuşak nodül ve B '
                         'semptomu yokluğuyla en olası klinik tanınız nedir?',
             'options': [{'text': 'Akut Bakteriyel Süpüratif Lenfadenit',
                          'is_correct': False,
                          'scenario_update': 'Lenf nodunda hızlı büyüme, şiddetli hassasiyet, çevre dokuda '
                                             'kızarıklık, ısı artışı veya fluktuasyon saptanmadı.',
                          'teaching_point': 'Akut bakteriyel lenfadenit stafilokok veya streptokoklara bağlı '
                                            'olup eritemli, fluktuasyon veren, aşırı ağrılı ve sıklıkla '
                                            'ateşli seyreder.'},
                         {'text': 'Hodgkin Lenfoma Tutulumu',
                          'is_correct': False,
                          'scenario_update': 'Nodülün sert-lastik kıvamda olmaması, çevreye fikse '
                                             'bulunmaması ve gece terlemesi ile kilo kaybının olmaması '
                                             'maligniteyi dışladı.',
                          'teaching_point': 'Hodgkin lenfomada lenf nodları tipik olarak ağrısız, sert, '
                                            'lastik kıvamında, fikse veya konglomeredir; sıklıkla '
                                            'supraklaviküler yerleşir ve B semptomları eşlik eder.'},
                         {'text': 'Enfeksiyöz Mononükleoz (EBV Enfeksiyonu)',
                          'is_correct': False,
                          'scenario_update': 'Hastada yaygın posterior servikal lenfadenopati, eksüdatif '
                                             'tonsillit, ateş veya splenomegali bulgusu olmadığı görüldü.',
                          'teaching_point': 'EBV enfeksiyonunda tipik olarak belirgin farenjit, tonsiller '
                                            'eksüda, posterior servikal ağırlıklı yaygın adenopati ve '
                                            'hepatosplenomegali bulunur.'},
                         {'text': 'Reaktif Servikal Lenfadenopati',
                          'is_correct': True,
                          'explanation': 'Geçirilmiş viral ÜSYE sonrası soliter, <2 cm, yumuşak-elastik, '
                                         'mobil, ağrısız ve inflamasyon bulgusu olmayan lenf bezi reaktif '
                                         'servikal lenfadenopati ile tam uyumludur.',
                          'new_finding': 'Klinik tanı Reaktif Servikal Lenfadenopati olarak '
                                         'kesinleştirildi.'}]},
            {'stage_title': 'Tedavi ve İzlem Planı',
             'question': 'Reaktif servikal lenfadenopati tanısı alan bu stabil çocukta acil servisteki en '
                         'doğru yönetim ve taburculuk planı hangisidir?',
             'options': [{'text': 'Ampirik olarak iki hafta süreli yüksek doz oral amoksisilin-klavulanat ve '
                                  'parenteral aminoglikozid antibiyotik kombinasyonu reçete ederek hastayı '
                                  'taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz geniş spektrumlu antibiyotik başlanan çocukta ciddi '
                                             'ishal ve gastrointestinal kramplar gelişti ancak lenf nodu '
                                             'boyutunda değişiklik olmadı.',
                          'teaching_point': 'Eritem, ısı artışı, fluktuasyon veya sistemik ateş olmayan '
                                            'reaktif lenfadenopatilerde antibiyotik tedavisi kesinlikle '
                                            'endike değildir ve zararlıdır.'},
                         {'text': 'Lenf nodunun hızlı gerilemesini sağlamak için yüksek doz oral '
                                  'kortikosteroid tedavisi başlayarak hastayı bir hafta sonra kontrole '
                                  'çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Steroid kullanımı olası gizli hematolojik malignitelerde '
                                             'tanısal gecikmeye yol açabileceği gibi çocukta iştah artışı ve '
                                             'geçici hipertansiyon oluşturdu.',
                          'teaching_point': 'Tanısı tam netleşmemiş lenfadenopatilerde kortikosteroid '
                                            'verilmesi histopatolojik değerlendirmeyi bozabileceğinden ve '
                                            'maligniteyi maskeleyebileceğinden kontrendikedir.'},
                         {'text': 'Gereksiz antibiyotik vermeden üç dört hafta sonra poliklinik kontrolü '
                                  'planlamak ve büyüme durumunda erken başvuru önermek',
                          'is_correct': True,
                          'explanation': 'Reaktif lenf nodlarının küçülmesi 4-6 hafta sürebilir. Bakteriyel '
                                         'süpürasyon yoksa antibiyotik endike değildir; kırmızı bayrak '
                                         'eğitimi ve 3-4 hafta sonra takip yeterlidir.',
                          'new_finding': 'Aileye nodülün haftalar içinde küçülebileceği, antibiyotiğe gerek '
                                         'olmadığı, boyutta artış veya ateş halinde hemen başvurmaları '
                                         'anlatılarak taburcu edildi.'},
                         {'text': 'Lenf nodunun maligniteye dönüşüm riskini ekarte etmek amacıyla hastayı '
                                  'acil çocuk cerrahisine yatırarak aynı gün eksizyonel biyopsiye almak',
                          'is_correct': False,
                          'scenario_update': 'Cerrahi ekip stabil, 1.5 cm mobil nodülü olan çocukta acil '
                                             'biyopsi endikasyonu olmadığını, gereksiz skar ve anestezi '
                                             'riski doğuracağını belirtti.',
                          'teaching_point': 'Çocuklarda reaktif lenfadenopatilerde acil cerrahi eksizyon '
                                            'endike değildir; en az 3-4 haftalık izlemde progresyon gösteren '
                                            'nodüllere biyopsi düşünülür.'}]}]}]
