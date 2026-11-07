# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyonu - Sarı Alan Vakaları (Part 4: S31 - S40)
"""

YELLOW_CASES_PART4 = [{'id': 'S31',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '2 Yaş',
  'gender': 'Erkek',
  'complaint': 'Bezinde aniden başlayan, ağrısız, yoğun vişne çürüğü ve parlak kırmızı renkli rektal kanama ile '
               'solukluk',
  'history': 'Ailesi daha önce sağlıklı olan 2 yaşındaki erkek çocuğu bezinde yoğun kanama fark ederek Sarı Alana '
             "getiriyor: 'Yaklaşık iki saat önce altını değiştirirken bezinin tamamen taze kırmızı ve vişne çürüğü "
             'renkli kanla kaplandığını gördük. Çocuğun hiçbir karın ağrısı kıvranması, ağlama nöbeti veya kusması '
             'olmadı. Bir saat sonra bezinde tekrar bol miktarda pıhtılı kanama oldu ve ten rengi belirgin şekilde '
             "soldu.'",
  'final_diagnosis': 'Meckel Divertikülü Kanaması (Ektopik Gastrik Mukoza Ülserasyonu)',
  'disposition': 'Sarı Alanda İV Damar Yolu + İzotonik Sıvı Resüsitasyonu + Kan Grubu ve Çapraz Karşılaştırma + Çocuk '
                 'Cerrahisi Konsültasyonu ile Cerrahi Rezeksiyon İçin Yatış',
  'case_pearl': 'Meckel divertikülü, omfalomezenterik kanalın kapanma kusuru sonucu gelişen en sık konjenital '
                "gastrointestinal anomalidir ('2'ler kuralı': toplumun %2'sinde görülür, ileoçekal valvden yaklaşık 2 "
                'fit proksimaldedir, 2 inç uzunluğundadır, sıklıkla 2 yaş altında semptom verir). En yaygın '
                'prezantasyon, ektopik mide mukozasından salgılanan aside bağlı komşu ileum mukozasında gelişen '
                'ağrısız, yoğun alt gastrointestinal sistem kanamasıdır (vişne çürüğü veya parlak kırmızı rektal '
                'kanama). Karın muayenesinde defans veya hassasiyet saptanmaz, batın tamamen rahattır. Tanıda altın '
                'standart yöntem Tc-99m perteknetat sintigrafisidir (Meckel sintigrafisi); ektopik gastrik mukoza '
                'perteknetatı tutarak sağ alt kadranda fokal aktivite artışı gösterir. Tedavi cerrahi kama rezeksiyonu '
                'veya divertikülektomidir.',
  'steps': [{'stage_title': 'Sarı Alanda İlk Değerlendirme ve Hemodinamik Stabilizasyon',
             'question': 'Masif ağrısız rektal kanama, solukluk ve belirgin taşikardisi olan 2 yaşındaki bu hastada '
                         'ilk yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Cerrahi konsültasyon öncesinde kanama odağını netleştirmek amacıyla hastaya '
                                  'nazogastrik tüp takıp bol miktarda soğuk serum fizyolojikle mide lavajı uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Nazogastrik lavajda berrak mide içeriği geldi, kanama izlenmedi ancak '
                                             'lavaj işlemi esnasında çocuk aşırı ajite olarak taşikardisi arttı.',
                          'teaching_point': 'Ağrısız masif alt gastrointestinal kanamalı ve taşikardik çocuklarda ilk '
                                            'öncelik invaziv nazogastrik lavaj değil, acil damar yolu açılarak '
                                            'hemodinamik resüsitasyonun sağlanmasıdır.'},
                         {'text': 'Geniş iki damar yolu açarak izotonik kristaloid bolusu başlatmak, tam kan sayımı, '
                                  'kan grubu ve çapraz karşılama göndermek',
                          'is_correct': True,
                          'explanation': 'Masif kanamalı ve kompanse şok bulguları (taşikardi, solukluk) olan çocukta '
                                         'öncelik damar yolu güvenliği, hacim resüsitasyonu ve acil kan hazırlığıdır.',
                          'new_finding': 'Vital bulgular: Ateş 36.8°C, KTA 155/dk, SS 28/dk, TA 88/52 mmHg, SpO2 %98, '
                                         'CRT 3 saniye. Batın muayenesi tamamen rahat, distansiyon, defans veya '
                                         'rebound yok. Rektal tuşede parlak kırmızı kan ve pıhtı izlendi, fissür '
                                         "saptanmadı. 20 mL/kg izotonik sonrası KTA 132/dk'ya geriledi."},
                         {'text': 'Kanamanın anal fissürden kaynaklanıp kaynaklanmadığını ayırt etmek amacıyla hastaya '
                                  'derin sedasyon vererek acil tanısal anoskopi ve rektoskopi yapmak',
                          'is_correct': False,
                          'scenario_update': 'Derin sedasyon uygulanan hipovolemik çocukta kan basıncı 75/40 mmHg '
                                             'düzeyine geriledi ve anoskopide yalnızca proksimalden gelen yoğun kan '
                                             'görüldü.',
                          'teaching_point': 'Hemodinamik resüsitasyon tamamlanmadan ve damar yolu açılmadan yapılan '
                                            'sedasyon ve endoskopik girişimler hipovolemik şoku derinleştirerek hayati '
                                            'risk oluşturur.'},
                         {'text': 'Oral beslenmeyi açık tutarak koagülasyon parametreleri sonuçlanana kadar hastayı '
                                  'monitörize gözlem odasında izlemek ve oral demir damlası başlamak',
                          'is_correct': False,
                          'scenario_update': 'Oral hidrasyon verilmeye çalışılırken hasta kustu, takip eden bezinde '
                                             "tekrar yoğun parlak kırmızı kanama oldu ve taşikardi 160/dk'ya yükseldi.",
                          'teaching_point': 'Aktif masif gastrointestinal kanaması olan çocuklarda oral alım '
                                            'aspirasyon riski ve acil cerrahi olasılığı nedeniyle derhal kapatılmalı, '
                                            'parenteral hidrasyon verilmelidir.'}]},
            {'stage_title': 'Laboratuvar Tetkikleri ve İleri Görüntüleme Yönteminin Belirlenmesi',
             'question': 'Hemodinamisi stabilize edilen, ağrısız alt gastrointestinal kanaması ve rahat batın '
                         'muayenesi olan çocukta öncelikli görüntüleme yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Kolon lümenindeki olası vasküler lezyonları doğrudan saptamak amacıyla bağırsak '
                                  'temizliği yapmadan acil tanısal ve terapotik kolonoskopi planlamak',
                          'is_correct': False,
                          'scenario_update': 'Kolonda yoğun pıhtı ve taze kan bulunması nedeniyle mukozal yüzeyler net '
                                             'değerlendirilemedi ve kanama odağı tespit edilemedi.',
                          'teaching_point': 'Masif alt gastrointestinal kanamalarda hazırlıksız acil kolonoskopinin '
                                            'tanısal değeri düşüktür; lümendeki kan mukozal vizualizasyonu engeller.'},
                         {'text': 'Batın içi serbest havayı ve olası bağırsak perforasyonunu ekarte etmek amacıyla '
                                  'ayakta direkt batın ve sol lateral grafi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Direkt batın grafilerinde serbest hava veya obstrüksiyon bulgusu '
                                             'saptanmadı, tanıya ve klinik yönetime herhangi bir katkı sağlamadı.',
                          'teaching_point': 'Ağrısız rektal kanamada perforasyon veya mekanik obstrüksiyon kliniği '
                                            'yoksa direkt grafilerin tanısal duyarlılığı ve yönetime katkısı son '
                                            'derece düşüktür.'},
                         {'text': 'Ektopik mide mukozasını görüntülemek amacıyla nükleer tıp ünitesiyle koordine '
                                  'olarak teknesyum doksan dokuz em perteknetat sintigrafisi planlamak',
                          'is_correct': True,
                          'explanation': 'Pediatrik yaş grubunda ağrısız masif alt gastrointestinal kanamanın en sık '
                                         'nedeni ektopik gastrik mukoza içeren konjenital anomalilerdir ve sintigrafi '
                                         'altın standarttır.',
                          'new_finding': 'Laboratuvar: Hb 7.8 g/dL, Hct %23.8, BK 8.400/mm³, Trombosit 290.000/mm³, '
                                         'Koagülasyon testleri doğal. Sintigrafi: Sağ alt kadranda, mide mukozasıyla '
                                         'eş zamanlı perteknetat tutulumu gösteren fokal radyoaktivite artışı '
                                         'izlendi.'},
                         {'text': 'İntususepsiyonu kesin olarak dışlamak amacıyla batın ultrasonografisi çekmek ve '
                                  'işlem esnasında hidrostatik redüksiyon için lavman hazırlığı yapmak',
                          'is_correct': False,
                          'scenario_update': 'Batın ultrasonografisinde hedef tahtası görünümü saptanmadı, lavman '
                                             'hazırlığı gereksiz zaman kaybına ve mukozal irritasyona yol açtı.',
                          'teaching_point': 'Ağrısız, vişne çürüğü kanamalarda ve rahat batın muayenesinde '
                                            'intususepsiyon ön planda düşünülmez; lavman uygulanması gereksiz ve '
                                            'zararlıdır.'}]},
            {'stage_title': 'Klinik ve Sintigrafik Bulgularla Kesin Tanı',
             'question': 'Ağrısız masif rektal kanama, derin anemi ve sintigrafide sağ alt kadranda ektopik mide '
                         'mukozası saptanan hastada kesin tanınız nedir?',
             'options': [{'text': 'Meckel divertikülü kanaması',
                          'is_correct': True,
                          'explanation': 'İki yaş altı çocukta ağrısız masif vişne çürüğü rektal kanama ve '
                                         'sintigrafide ektopik gastrik mukoza tespiti Meckel divertikülü kanamasını '
                                         'kesinleştirir.',
                          'new_finding': 'Kesin tanı: Meckel divertikülü kanaması (ektopik gastrik mukoza zemininde '
                                         'gelişen ileal ülser kanaması).'},
                         {'text': 'İleokolik invajinasyon',
                          'is_correct': False,
                          'scenario_update': 'İnvajinasyonda kolik tarzı aralıklı şiddetli karın ağrısı, safralı kusma '
                                             've palpabl kitle beklenir; sintigrafide ektopik mukoza tutulumu olmaz.',
                          'teaching_point': 'Ağrısız masif vişne çürüğü kanama invajinasyondan ziyade Meckel '
                                            'divertikülü kanaması için karakteristiktir.'},
                         {'text': 'Juvenil rektal polip',
                          'is_correct': False,
                          'scenario_update': 'Juvenil polipler genellikle dışkılamanın sonunda damlama şeklinde parlak '
                                             'kırmızı kanama yapar ve masif anemiye nadiren yol açar.',
                          'teaching_point': 'Rektal polipler masif vişne çürüğü kanama veya ektopik gastrik mukoza '
                                            'sintigrafi pozitifliği göstermez.'},
                         {'text': 'Nekrotizan enterokolit',
                          'is_correct': False,
                          'scenario_update': 'Nekrotizan enterokolit prematüre yenidoğanlarda distandü batın, safralı '
                                             'kusma ve pnömatozis intestinalis ile seyreder; 2 yaşında beklenmez.',
                          'teaching_point': 'Nekrotizan enterokolit yenidoğan dönemine özgü bir tablodur; 2 yaşındaki '
                                            'sağlıklı çocukta ağrısız kanama nedeni değildir.'}]},
            {'stage_title': 'Cerrahi Konsültasyon ve Kesin Tedavi Yönetimi',
             'question': 'Meckel divertikülü kanaması tanısı kesinleşen ve anemisi olan 2 yaşındaki bu hastanın acil '
                         'servisteki nihai yönetim planı nasıl olmalıdır?',
             'options': [{'text': 'Kanama kendiliğinden durduğu için oral proton pompa inhibitörü ve demir damlası '
                                  'reçete ederek hastayı cerrahi poliklinik kontrolüne yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Taburcu edilmesi planlanan hastada üç saat sonra tekrar masif rektal '
                                             'kanama ve derin hipovolemik şok tablosu gelişti.',
                          'teaching_point': 'Meckel divertikülü kanamaları aralıklı ve masif tekrarlayabilir; cerrahi '
                                            'rezeksiyon yapılmadan medikal tedaviyle taburcu edilemez.'},
                         {'text': 'Cerrahi müdahale öncesinde gastrointestinal kanama odağını elektrokoterle yakmak '
                                  'amacıyla acil terapotik çift balonlu enteroskopi ünitesine derhal sevk etmek',
                          'is_correct': False,
                          'scenario_update': 'İnvaziv enteroskopi esnasında ileum lümeni perfore oldu ve hasta acil '
                                             'laparatomiye alınmak zorunda kaldı.',
                          'teaching_point': 'Meckel divertikülü kanamasında endoskopik hemostaz endike değildir; '
                                            'standart tedavi cerrahi rezeksiyondur.'},
                         {'text': 'Kanamanın tekrarlamasını önlemek amacıyla traneksamik asit infüzyonu başlayarak '
                                  'hastayı çocuk gastroenteroloji servisinde yakın medikal izleme almak',
                          'is_correct': False,
                          'scenario_update': 'Antifibrinolitik tedavi kanamayı geçici durdursa da anatomik anomaliyi '
                                             'çözmedi ve hastanede yatarken rekanalizasyonla kanama nüksetti.',
                          'teaching_point': 'Ektopik gastrik mukozaya bağlı ülser kanamasında medikal tedaviler kesin '
                                            'çözüm sağlamaz; çocuk cerrahisi tarafından cerrahi eksizyon şarttır.'},
                         {'text': 'Çocuk cerrahisi ile konsülte edilerek eritrosit süspansiyonu desteği eşliğinde acil '
                                  'cerrahi rezeksiyon için ameliyathaneye ve servise almak',
                          'is_correct': True,
                          'explanation': 'Semptomatik Meckel divertikülünün kesin tedavisi cerrahidir '
                                         '(divertikülektomi veya segmental ileum rezeksiyonu); derin anemi için kan '
                                         'transfüzyonu eşlik etmelidir.',
                          'new_finding': 'Eritrosit süspansiyonu transfüzyonu eşliğinde çocuk cerrahisi tarafından '
                                         'laparoskopik Meckel divertikülektomisi başarıyla uygulandı; hasta şifa ile '
                                         'taburcu edildi.'}]}]},
 {'id': 'S32',
  'category': '🤢 Karın Ağrısı, Kusma & İshal (GİS)',
  'age': '12 Yaş',
  'gender': 'Kız',
  'complaint': 'Aniden başlayan, kıvrandırıcı sol alt kadran karın ağrısı ve tekrarlayan safrasız kusma',
  'history': '12 yaşındaki kız hasta ailesi tarafından şiddetli karın ağrısı nedeniyle Sarı Alana getiriliyor: '
             "'Yaklaşık dört saat önce ders çalışırken sol kasığına bıçak saplanır gibi aniden başlayan çok şiddetli "
             'bir ağrı oldu. Ağrı dalgalar halinde geliyor, iki büklüm kıvranıyor ve arka arkaya üç kez mide içeriği '
             'kustu. Daha önce benzer bir ağrısı hiç olmamıştı, son adeti iki hafta önceydi ve idrar yaparken yanması '
             "yok.'",
  'final_diagnosis': 'Akut Sol Over Torsiyonu (Adneksiyal Torsiyon)',
  'disposition': 'Sarı Alanda Oral Stop + Damar Yolu + İV Hidrasyon + Analjezi + Acil Çocuk Cerrahisi ve Jinekoloji '
                 'Konsültasyonu ile Laparoskopik Detorsiyon İçin Ameliyathaneye Yatış',
  'case_pearl': 'Over torsiyonu, over ve fallop tüpünün kendi vasküler pedikülü etrafında dönerek venöz staz, ödem ve '
                'takiben arteriyel iskemiye yol açtığı acil jinekolojik-cerrahi bir durumdur. Adölesan kızlarda aniden '
                'başlayan tek taraflı, şiddetli, kolik tarzda alt kadran ağrısı ve kusma ile prezante olur. Tanıda ilk '
                'tercih Renkli Doppler ultrasonografidir (stroması ödemli ve büyümüş over, periferik yerleşimli '
                "foliküller, vasküler pedikülde 'whirlpool' burgu işareti ve azalmış/kaybolmuş akım; akım izlenmesi "
                'torsiyonu ekarte ettirmez). Zaman over canlılığı için kritiktir; altın standart tedavi doku nekrotik '
                'görünse dahi ooferektomi değil, organ koruyucu acil laparoskopik detorsiyondur.',
  'steps': [{'stage_title': 'Sarı Alanda Akut Alt Kadran Ağrılı Hastaya İlk Yaklaşım',
             'question': 'Aniden başlayan şiddetli sol alt kadran ağrısı ve kusması olan 12 yaşındaki kız hastada ilk '
                         'muayene ve stabilizasyon yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Damar yolu açıp intravenöz hidrasyon ve analjezi sağlamak, batın muayenesinde '
                                  'peritoneal irritasyon ve pelvik kitle bulgularını incelemek',
                          'is_correct': True,
                          'explanation': 'Akut batın kliniği olan hastada öncelikle hemodinamik stabilizasyon ve '
                                         'analjezi sağlanmalı, peritoneal bulgular ve pelvik kitle varlığı '
                                         'araştırılmalıdır.',
                          'new_finding': 'Vital bulgular: Ateş 37.0°C, KTA 116/dk, SS 20/dk, TA 110/70 mmHg. Karın '
                                         'muayenesinde sol alt kadranda belirgin hassasiyet ve defans mevcut, sağ alt '
                                         'kadran rahat. Pelvik bölgede sol tarafta derin palpasyonla dolgunluk ve '
                                         'hassas kitle hissi alınıyor. İntravenöz parasetamol sonrası ağrının '
                                         'kıvrandırıcı şiddeti devam ediyor.'},
                         {'text': 'Gastrointestinal spazmı rahatlatmak amacıyla antispazmodik ve antiemetik uygulayıp '
                                  'ağrı hafifleyene kadar fizik muayeneyi geciktirerek hastayı sakinleştirmek',
                          'is_correct': False,
                          'scenario_update': 'Antispazmodik sonrası kusma baskılandı ancak sol alt kadrandaki '
                                             'kıvrandırıcı iskemi ağrısı ve peritonit bulguları hızla şiddetlendi.',
                          'teaching_point': 'Akut cerrahi batın şüphesi olan hastalarda tanı konulmadan antispazmodik '
                                            'verilmesi tabloyu maskeleyebilir ve kritik cerrahi zaman penceresinin '
                                            'kaçırılmasına yol açar.'},
                         {'text': 'Olası ektopik gebelik veya rüptüre korpus luteumu dışlamak amacıyla analjezik '
                                  'vermeden hastaya acil bimanual vajinal muayene yapmak',
                          'is_correct': False,
                          'scenario_update': 'Virgo adölesan hastada gereksiz ve travmatik bimanual muayene girişimi '
                                             'şiddetli anksiyete ve ajitasyona yol açtı, tanısal fayda sağlamadı.',
                          'teaching_point': 'Pediatrik ve adölesan grupta pelvik patolojilerin değerlendirilmesinde '
                                            'bimanual vajinal muayene rutin uygulanmaz; rektal veya non-invaziv '
                                            'transabdominal ultrasonografi tercih edilir.'},
                         {'text': 'Ağrının renal kolik kaynaklı olduğunu düşünerek yüksek doz intramüsküler nonsteroid '
                                  'antiinflamatuar yapmak ve iki litre oral su içirmek',
                          'is_correct': False,
                          'scenario_update': 'Oral sıvı alımı sonrası hasta tekrar safrasız mide içeriği kustu ve oral '
                                             'stop prensibi bozulduğu için anestezi hazırlığı gecikti.',
                          'teaching_point': 'Akut batın şüpheli ve kusan hastalarda oral alım kesinlikle kesilmeli, '
                                            'renal kolik varsayımıyla cerrahi patolojiler atlanmamalıdır.'}]},
            {'stage_title': 'Laboratuvar İncelemeleri ve İlk Basamak Radyolojik İnceleme',
             'question': 'Sol alt kadranda hassas kitle ve peritoneal irritasyon saptanan adölesan kız hastada '
                         'öncelikli tanısal görüntüleme yönteminiz ne olmalıdır?',
             'options': [{'text': 'Peritoneal kalsifikasyon ve bağırsak obstrüksiyonunu dışlamak için acil ayakta '
                                  'direkt batın grafisi ve sol lateral dekübit grafi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Direkt batın grafilerinde sol alt kadranda nonspesifik yumuşak doku '
                                             'gölgesi dışında patoloji izlenmedi ve tanısal gecikme yaşandı.',
                          'teaching_point': 'Direkt grafiler pelvik patolojilerin tanısında yetersizdir; yumuşak doku '
                                            've vasküler detay vermez.'},
                         {'text': 'Pelvik patolojileri ve apandisiti aynı anda kesin olarak dışlamak amacıyla acil '
                                  'intravenöz kontrastlı tüm batın bilgisayarlı tomografisi çekmek',
                          'is_correct': False,
                          'scenario_update': 'Bilgisayarlı tomografide sol pelvik bölgede kitle teyit edildi ancak '
                                             'adölesan hasta gereksiz yüksek doz gonadal iyonizan radyasyona maruz '
                                             'kaldı.',
                          'teaching_point': 'Adölesan kızlarda akut pelvik ağrının ilk basamak görüntülemesi radyasyon '
                                            'içermeyen ultrasonografidir; BT ancak şüpheli veya komplike olgularda '
                                            'düşünülür.'},
                         {'text': 'İnflamasyon belirteçlerini izlemek için tam kan sayımı ve CRP gönderip sonuçlar '
                                  'çıkana kadar radyolojik görüntüleme yapmadan beklemek',
                          'is_correct': False,
                          'scenario_update': 'Sonuçlar beklenirken geçen iki saatte hastanın ağrısı dayanılmaz hale '
                                             'geldi ve gonadal dokunun iskemik süresi uzadı.',
                          'teaching_point': 'Akut organ iskemisi şüphesinde laboratuvar sonuçları beklenmeden acil '
                                            'ultrasonografik görüntüleme organize edilmelidir; zaman doku canlılığı '
                                            'demektir.'},
                         {'text': 'Radyasyon maruziyetinden kaçınarak sol pelvik bölgeyi ve kan akımını değerlendirmek '
                                  'için acil pelvik renkli Doppler ultrasonografi istemek',
                          'is_correct': True,
                          'explanation': 'Pediatrik ve adölesan kızlarda akut pelvik kitle ve ağrının altın standart '
                                         'ilk basamak görüntülemesi pelvik renkli Doppler ultrasonografidir.',
                          'new_finding': 'Laboratuvar: Lökosit 12.200/mm³, CRP 8 mg/L, beta-hCG negatif, TİT doğal. '
                                         'Renkli Doppler USG: Sol pelvik lojda 48x35 mm boyutlarında, stroması '
                                         'belirgin ödemli ve periferinde küçük kistik yapılar dizilmiş kitle izlendi. '
                                         'Vasküler pedikülde burgu görünümü saptandı ve arteriyel-venöz kan akımında '
                                         'ileri derecede azalma izlendi. Sağ taraf anatomik yapısı tamamen doğal.'}]},
            {'stage_title': 'Klinik ve Doppler Bulguları ile Kesin Tanı',
             'question': 'Büyümüş ve ödemli sol gonadal yapı, periferik foliküller ve pedikülde burgu işaretiyle akım '
                         'kaybı saptanan hastada kesin tanınız nedir?',
             'options': [{'text': 'Rüptüre hemorajik over kisti',
                          'is_correct': False,
                          'scenario_update': 'Hemorajik kist rüptüründe batında serbest sıvı ve kist kollapsı görülür; '
                                             'vasküler pedikülde burgu ve stromal büyüme izlenmez.',
                          'teaching_point': 'Stromal ödem, belirgin büyüme ve vasküler burgu bulgusu kist rüptüründen '
                                            'ziyade torsiyona işaret eder.'},
                         {'text': 'Pelvik inflamatuar hastalık',
                          'is_correct': False,
                          'scenario_update': 'Pelvik inflamatuar hastalıkta bilateral hassasiyet, vajinal akıntı ve '
                                             'yüksek ateş beklenir; tek taraflı burgu işareti görülmez.',
                          'teaching_point': 'Ani başlangıçlı tek taraflı kitle ve akım kaybı enfeksiyondan ziyade '
                                            'vasküler torsiyon ile uyumludur.'},
                         {'text': 'Akut sol over torsiyonu',
                          'is_correct': True,
                          'explanation': 'Adölesan kızda ani başlangıçlı alt kadran ağrısı, büyümüş ödemli parankim, '
                                         'periferik foliküller ve pedikülde burgu işareti akut over torsiyonu için '
                                         'patognomoniktir.',
                          'new_finding': 'Kesin tanı: Akut sol over torsiyonu (sol adneksiyal torsiyon).'},
                         {'text': 'Akut sol taraflı apandisit',
                          'is_correct': False,
                          'scenario_update': "Situs inversus veya sol yerleşimli apandisitte USG'de kör sonlanan "
                                             'tübüler yapı izlenir; pelvik kitle ve gonadal iskemi görülmez.',
                          'teaching_point': 'Ultrasonografide sol gonadal stromanın büyümesi ve vasküler pedikülün '
                                            'dönmesi apandisit ile uyumlu değildir.'}]},
            {'stage_title': 'Acil Cerrahi Tedavi ve Detorsiyon Yönetimi',
             'question': 'Akut sol over torsiyonu tanısı kesinleşen 12 yaşındaki adölesan hastada gonadal rezervi '
                         'korumaya yönelik en uygun cerrahi yaklaşım nedir?',
             'options': [{'text': 'Dokunun iskemik ve nekrotik görünümde olma ihtimali nedeniyle zaman hiç kaybetmeden '
                                  'tek taraflı açık ooferektomi operasyonu planlamak',
                          'is_correct': False,
                          'scenario_update': 'Detorsiyon denenmeden doğrudan ooferektomi yapılması adölesan hastanın '
                                             'gelecekteki over rezervini ve fertilitesini geri dönüşsüz olarak '
                                             'azalttı.',
                          'teaching_point': 'Pediatrik ve adölesan torsiyonlarda over siyah/nekrotik görünse dahi doku '
                                            'reperfüzyon potansiyeli yüksektir; ilk tercih her zaman detorsiyondur.'},
                         {'text': 'Çocuk cerrahisi ve jinekoloji ile acil laparoskopik detorsiyon planlayarak doku '
                                  'görünümünden bağımsız organ koruyucu yaklaşım uygulamak',
                          'is_correct': True,
                          'explanation': 'Pediatrik torsiyonlarda altın standart, nekrotik görünümde dahi dokunun '
                                         'korunarak detorsiyon yapılması ve over canlılığının izlenmesidir.',
                          'new_finding': 'Acil laparoskopide 720 derece torsiyone ve siyanotik sol over detorsiyone '
                                         'edildi; 15 dakika içinde pembeleşerek kan akımının geri döndüğü görüldü ve '
                                         'organ korundu.'},
                         {'text': 'İntravenöz geniş spektrumlu antibiyotik ve antikoagülan başlayarak sol pelvik '
                                  'kitleyi yirmi dört saatlik konservatif takip altına almak',
                          'is_correct': False,
                          'scenario_update': 'Konservatif takip altında geçen saatlerde over dokusunda tam hemorajik '
                                             'enfarktüs ve gangren gelişti, over kaybedildi.',
                          'teaching_point': 'Torsiyon mekanik bir vasküler tıkanıklıktır; medikal tedavi ile düzelmez, '
                                            'gecikilen her saat over kaybı riskini katlar.'},
                         {'text': 'Ağrı kesici infüzyonunu artırıp pelvik kist gerilemesini izlemek üzere hastayı acil '
                                  'servisten elektif jinekoloji polikliniğine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Taburcu edilmeye çalışılan hastada peritonit ve sepsis tablosu gelişti, '
                                             'acil laparatomi ile nekrotik doku rezeke edildi.',
                          'teaching_point': 'Over torsiyonu acil cerrahi endikasyonudur; elektif poliklinik takibi '
                                            'yapılamaz.'}]}]},
 {'id': 'S33',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '3 Yaş',
  'gender': 'Erkek',
  'complaint': 'Bir hafta önceki ishal sonrası giderek artan halsizlik, solukluk, açıklanamayan belirgin çarpıntı ve '
               'hızlı soluma',
  'history': '3 yaşındaki erkek çocuk ailesi tarafından halsizlik ve hızlı nefes alıp verme şikayetiyle Sarı Alana '
             "getiriliyor: 'Yaklaşık bir hafta önce hafif ateş ve sulu ishal geçirmişti, ishali düzeldi ancak son iki "
             'gündür yataktan kalkmak istemiyor, hiçbir şey yemiyor ve göğsü kuş gibi çok hızlı çarpıyor. Vücudunda '
             'belirgin bir ateş olmamasına rağmen kalbi durmaksızın çok hızlı atıyor ve emerken ya da su içerken hemen '
             "yorulup terliyor.'",
  'final_diagnosis': 'Akut Viral Enfeksiyon Sonrası Miyokardit (Kardiyak Dekompanzasyon)',
  'disposition': 'Sarı Alanda Oksijen + Damar Yolu + Sıvı Kısıtlaması + İnotropik Destek + Çocuk Kardiyoloji ve Çocuk '
                 'Yoğun Bakım Ünitesine Acil Yatış',
  'case_pearl': 'Pediatrik miyokardit, sıklıkla geçirilmiş viral bir enfeksiyonu (enterovirus, adenovirus, parvovirus '
                'B19 vb.) takiben gelişen miyosit hasarı ve miyokard disfonksiyonudur. Ateş olmaksızın açıklanamayan '
                'persistan taşikardi, hepatomegali, galo ritmi ve takipne erken kalp yetersizliğinin kritik kırmızı '
                "bayraklarıdır. Telekardiyografide kardiyomegali ve pulmoner venöz konjesyon, EKG'de düşük voltaj veya "
                'ST-T değişiklikleri, Troponin I ve NT-proBNP yüksekliği tipiktir. Erken dönemde aşırı sıvı '
                'yüklemesinden kaçınılmalı (sıvı kısıtlaması), inotropik destek (milrinon, dopamin vb.) ve '
                'gerektiğinde mekanik dolaşım desteği (ECMO) için hasta hızla çocuk kardiyoloji yoğun bakımına '
                'yatırılmalıdır.',
  'steps': [{'stage_title': 'Sarı Alanda Açıklanamayan Taşikardiye İlk Yaklaşım',
             'question': 'Ateşi olmamasına rağmen belirgin taşikardisi ve solunum sıkıntısı olan 3 yaşındaki çocukta '
                         'ilk muayene önceliğiniz ne olmalıdır?',
             'options': [{'text': 'Taşikardiyi dehidratasyona bağlayarak hızla yirmi mililitre kilogram izotonik serum '
                                  'fizyolojiği yarım saat içinde intravenöz infüzyonla göndermek',
                          'is_correct': False,
                          'scenario_update': "Hızlı sıvı bolusu sonrası akciğerlerde raller arttı, karaciğer 5 cm'ye "
                                             'büyüdü ve hasta akut pulmoner ödeme girdi.',
                          'teaching_point': 'Kardiyak disfonksiyona bağlı taşikardi ve hepatomegalisi olan çocuklara '
                                            'kontrolsüz sıvı bolusu verilmesi akut kalp yetersizliğini ağırlaştırır.'},
                         {'text': 'Çocuğun huzursuzluğunu yatıştırmak amacıyla yüksek doz oral sedatif uygulayıp tam '
                                  'sakinleşmesini bekledikten sonra rutin fizik muayeneyi tamamlamak',
                          'is_correct': False,
                          'scenario_update': 'Sedasyon uygulanan hastada solunum depresyonu ve hipoksi gelişti, zayıf '
                                             'olan hemodinamik kompanzasyon bozuldu.',
                          'teaching_point': 'Açıklanamayan taşikardi ve taşipnesi olan çocukta sedasyon uygulanması '
                                            'solunum ve kardiyovasküler kollapsa zemin hazırlar.'},
                         {'text': 'Havayolu ve solunumu destekleyip kalp seslerini, periferik nabızları, galo ritmini '
                                  've karaciğer boyutunu dikkatle muayene etmek',
                          'is_correct': True,
                          'explanation': 'Ateşle orantısız taşikardisi olan çocukta kalp yetersizliği bulguları (S3 '
                                         'galo, hepatomegali, zayıf nabızlar) öncelikle taranmalıdır.',
                          'new_finding': 'Vital bulgular: Ateş 37.1°C, KTA 170/dk (ritmik, zayıf dolgunlukta), SS '
                                         '48/dk, TA 82/52 mmHg, SpO2 %92 (oda havasında), CRT 3.5 saniye. Kalp '
                                         'seslerinde belirgin taşikardi ve üçüncü kalp sesi (S3 galo ritmi) duyuldu, '
                                         'patolojik üfürüm yok. Solunum seslerinde bilateral bazallerde krepitan '
                                         'raller mevcut. Karaciğer kot kavsi altında 3.5 cm palpabl. Periferik '
                                         'nabızlar filiform.'},
                         {'text': 'Solunum sıkıntısını bronkospazma bağlayarak ardışık üç doz nebulize salbutamol ve '
                                  'oral deksametazon başlayıp klinik yanıtı izlemek',
                          'is_correct': False,
                          'scenario_update': 'Nebulize beta-agonist uygulaması sonrası hastanın kalp tepe atımı '
                                             "195/dk'ya fırladı ve kardiyak iş yükü belirgin arttı.",
                          'teaching_point': 'Pulmoner konjesyona bağlı ral ve taşipnesi olan olgularda astım tedavisi '
                                            'verilmesi taşikardiyi ve miyokardiyal oksijen tüketimini artırır.'}]},
            {'stage_title': 'Kardiyovasküler İnceleme ve Laboratuvar Tetkik Planı',
             'question': 'Galo ritmi, hepatomegali ve persistan taşikardisi saptanan bu hastada tanıya yönelik en '
                         'uygun ilk tetkik kombinasyonu nedir?',
             'options': [{'text': 'Gastrointestinal enfeksiyon odağını saptamak için gaita mikroskopisi, viral antijen '
                                  'paneli ve batın ultrasonografisi ile tetkik sürecini başlatmak',
                          'is_correct': False,
                          'scenario_update': 'Gaita tetkikleri normal geldi ancak tetkik sürecinde kardiyak pompa '
                                             'yetersizliği derinleşti ve periferik dolaşım bozuldu.',
                          'teaching_point': 'Kardiyak dekompanzasyon bulguları olan hastada geçirilmiş gastroenterite '
                                            'yönelik tetkikler tanısal önceliğe sahip değildir; kardiyovasküler '
                                            'inceleme şarttır.'},
                         {'text': 'Oksijen desteği verip on iki derivasyonlu elektrokardiyografi çekmek, '
                                  'telekardiyografi istemek ve natriüretik peptit ile nekroz enzimlerini göndermek',
                          'is_correct': True,
                          'explanation': 'Kardiyak disfonksiyon şüphesinde EKG ritim ve iletiyi, telekardiyografi kalp '
                                         'boyutunu, nekroz enzimleri ve natriüretik peptitler miyosit hasarını ve '
                                         'yetersizliği belgeler.',
                          'new_finding': 'EKG: Sinüs taşikardisi (172/dk), prekordiyal derivasyonlarda düşük QRS '
                                         'voltajı ve yaygın ST-T değişiklikleri izlendi. Telekardiyografi: '
                                         'Kardiyotorasik indeks 0.64 (belirgin kardiyomegali) ve pulmoner vasküler '
                                         'konjesyon. Laboratuvar: CK-MB 64 U/L (yüksek), NT-proBNP 9.600 pg/mL '
                                         '(belirgin yüksek), Lökosit 10.800/mm³, CRP 12 mg/L.'},
                         {'text': 'Yalnızca rutin hemogram ve idrar tahlili isteyerek taşikardinin kendiliğinden '
                                  'düzelmesi için hastayı iki saat kardiyak monitörizasyonsuz bekletmek',
                          'is_correct': False,
                          'scenario_update': 'Monitörizasyonsuz bekletilen hastada taşikardi devam etti, bilinci '
                                             'letarjikleşti ve kapiller dolum zamanı beş saniyeye uzadı.',
                          'teaching_point': 'Ağır taşikardi ve konjestif yetersizlik bulgusu olan hasta monitörize '
                                            'edilmeli ve acil kardiyolojik tetkikler geciktirilmemelidir.'},
                         {'text': 'Olası intoksikasyonları ekarte etmek amacıyla acil kranial bilgisayarlı tomografi '
                                  've toksikoloji tarama paneli isteyip diğer tetkikleri ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Kranial tomografi normal sonuçlandı ancak hasta tomografi odasında '
                                             'taşipneik ve soğuk terleme içinde kaldı.',
                          'teaching_point': 'Nörolojik odak olmaksızın izole taşikardi ve hepatomegalide öncelik '
                                            'santral sinir sistemi görüntülemesi değil kardiyovasküler '
                                            'değerlendirmedir.'}]},
            {'stage_title': 'Klinik ve Laboratuvar Bulguları ile Kesin Tanı',
             'question': 'Viral enfeksiyon sonrası gelişen galo ritmi, kardiyomegali ve belirgin nekroz belirteçleri '
                         'saptanan hastada kesin tanınız nedir?',
             'options': [{'text': 'Akut viral miyokardit',
                          'is_correct': True,
                          'explanation': 'Geçirilmiş viral enfeksiyon, açıklanamayan taşikardi, galo ritmi, '
                                         'kardiyomegali, düşük voltaj EKG ve belirgin kardiyak enzim yüksekliği '
                                         'miyokardit tanısını kesinleştirir.',
                          'new_finding': 'Kesin tanı: Akut viral enfeksiyon sonrası miyokardit (sol ventrikül sistolik '
                                         'disfonksiyonu ve erken kardiyojenik şok tablosu). Troponin I düzeyi 4.2 '
                                         'ng/mL saptandı.'},
                         {'text': 'Konjenital uzun QT sendromu',
                          'is_correct': False,
                          'scenario_update': "Uzun QT sendromunda EKG'de QTc uzaması ve polimorfik ventriküler "
                                             'taşikardi atakları görülür; kardiyomegali ve nekroz belirteçleri '
                                             'beklenmez.',
                          'teaching_point': 'Kardiyomegali, pulmoner ödem ve enzim yüksekliği primer iyon kanalopatisi '
                                            'değil miyokard doku hasarı bulgusudur.'},
                         {'text': 'Ağır bakteriyel bronkopnömoni',
                          'is_correct': False,
                          'scenario_update': 'Pnömonide yüksek ateş, pürülan sekresyon ve lober konsolidasyon '
                                             'beklenir; izole kardiyomegali ve NT-proBNP yüksekliği açıklanamaz.',
                          'teaching_point': 'Akciğerdeki raller ve takipne primer akciğer enfeksiyonundan ziyade sol '
                                            'kalp yetersizliğine bağlı pulmoner venöz konjesyonu gösterir.'},
                         {'text': 'Hipovolemik dehidratasyon şoku',
                          'is_correct': False,
                          'scenario_update': 'Hipovolemik şokta kalp gölgesi küçülür ve hepatomegali olmaz; burada '
                                             'kardiyomegali ve hepatomegali hipervolemik/konjestif yetersizliği '
                                             'kanıtlar.',
                          'teaching_point': 'Hepatomegali ve kardiyomegali varlığı hipovolemiyi dışlar; tablonun '
                                            'kardiyojenik olduğunu gösterir.'}]},
            {'stage_title': 'Acil Yoğun Bakım Tedavisi ve İnotropik Yönetim',
             'question': 'Akut miyokardit ve düşük debili kardiyak pompa yetersizliği saptanan 3 yaşındaki bu hastada '
                         'en uygun yönetim planı nedir?',
             'options': [{'text': 'Kalp debisini artırmak amacıyla bolus intravenöz izotonik serum yükleyip hastayı '
                                  'genel pediatri servisinde takip altına almak',
                          'is_correct': False,
                          'scenario_update': 'İzotonik yüklemesi sonrası pulmoner venöz göllenme derinleşti ve hasta '
                                             'entübe edilmek zorunda kaldı.',
                          'teaching_point': 'Miyokarditte aşırı ön yük kardiyak yetersizliği dekompanse eder; sıvı '
                                            'kısıtlaması esastır, kontrolsüz bolus kontrendikedir.'},
                         {'text': 'Taşikardiyi hızla kırmak amacıyla intravenöz yüksek doz beta bloker bolusu '
                                  'uygulayıp hastayı acil gözlem ünitesinde izlemek',
                          'is_correct': False,
                          'scenario_update': 'Negatif inotrop etkili beta bloker miyokard kontraktilitesini tamamen '
                                             'çökerterek ağır kardiyojenik şoka yol açtı.',
                          'teaching_point': 'Akut dekompanse miyokarditte beta blokerler negatif inotropik etkileri '
                                            'nedeniyle kesinlikle kontrendikedir.'},
                         {'text': 'Ağır klinik tabloyu geriletmek amacıyla acil plazmaferez planlayarak hastayı '
                                  'taburcu edip çocuk kardiyoloji polikliniğine yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Taburcu edilmesi düşünülen düşük debili hastada evde kardiyak arrest '
                                             'riski ve mortalite son derece yüksektir.',
                          'teaching_point': 'Kardiyojenik şok riski taşıyan akut miyokardit hastaları acil servisten '
                                            'taburcu edilemez; yoğun bakımda sürekli izlem şarttır.'},
                         {'text': 'Sıvı kısıtlaması uygulayıp inotropik infüzyon desteği hazırlayarak hastayı çocuk '
                                  'kardiyoloji yoğun bakım ünitesine acilen yatırmak',
                          'is_correct': True,
                          'explanation': 'Dekompanse miyokarditte tedavi yaklaşımı sıvı kısıtlaması, kardiyak debiyi '
                                         'artıracak inotropik destek (örn. milrinon, düşük doz epinefrin) ve yoğun '
                                         'bakım takibidir.',
                          'new_finding': 'Oksijen, milrinon infüzyonu ve sıvı kısıtlaması altında çocuk kardiyoloji '
                                         'yoğun bakım ünitesine nakledildi; ekokardiyografide EF %35 saptandı ve ECMO '
                                         'hazırlığıyla izleme alındı.'}]}]},
 {'id': 'S34',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '8 Yaş',
  'gender': 'Kız',
  'complaint': 'Aniden başlayan şiddetli çarpıntı, göğüste baskı hissi, hafif baş dönmesi ve halsizlik',
  'history': '8 yaşındaki kız çocuğu okulda beden eğitimi dersinde aniden fenalaşarak ailesiyle birlikte Sarı Alana '
             "getiriliyor: 'Kızımız koşarken birdenbire kalbinin göğsünden fırlayacak gibi çarptığını söyledi. "
             'Göğsünde sıkışma hissi, halsizlik ve hafif sersemlik oldu ancak bayılmadı, senkop veya nöbet geçirmedi. '
             "Daha önce bilinen bir kalp rahatsızlığı, ritim bozukluğu veya ilaç maruziyeti bulunmuyor.'",
  'final_diagnosis': 'Ventriküler Taşikardi (Hemodinamik Olarak Stabil Geniş QRS Taşikardi)',
  'disposition': 'Sarı Alanda Monitörizasyon + Oksijen + İV Damar Yolu + İV Amiodaron İnfüzyonu + Senkronize '
                 'Kardiyoversiyon Hazırlığı + Çocuk Kardiyoloji Yoğun Bakımına Yatış',
  'case_pearl': 'Pediatrik taşikardilerde QRS süresi (>0.09-0.10 sn) geniş taşiaritmiler aksi kanıtlanmadıkça '
                'ventriküler taşikardi kabul edilir. Ventriküler taşikardilerde yönetim hemodinamik stabiliteye göre '
                'belirlenir: Nabızsız veya unstabil (hipotansiyon, bilinç değişikliği, şok) olgularda acil elektriksel '
                'kardiyoversiyon/defibrilasyon gerekirken; bilinci açık ve normotansif stabil olgularda elektriksel '
                'kardiyoversiyon yerine antiaritmik infüzyonu (tercihen İV Amiodaron 5 mg/kg, 20-60 dakikada infüzyon, '
                'veya Prokainamid) ilk tercihtir. Stabil olgularda vagal manevralar veya adenozin primer tedavi '
                'değildir (aberran iletili SVT şüphesi dışında ventriküler taşikardiyi sonlandırmaz ve hemodinamiyi '
                'bozabilir). Her zaman senkronize kardiyoversiyon cihazı hazır bulundurulmalıdır.',
  'steps': [{'stage_title': 'Sarı Alanda Ani Başlayan Çarpıntıya İlk Yaklaşım',
             'question': 'Aniden başlayan şiddetli çarpıntı ve göğüste baskı hissi olan 8 yaşındaki bu çocukta ilk '
                         'muayene ve yaklaşımınız nasıl olmalıdır?',
             'options': [{'text': 'Taşikardiyi hızla kırmak amacıyla ritmi ve hemodinamiyi hiç değerlendirmeden '
                                  'bilateral karotis sinüs masajı ve orbital bası uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Bilateral karotis ve orbital bası ağrıyı ve ajitasyonu artırdı; '
                                             'taşikardide hiçbir düzelme olmadı ve vagal manevra başarısız kaldı.',
                          'teaching_point': 'Pediatrik yaş grubunda orbital bası retina dekolmanı riski nedeniyle '
                                            'kesinlikle kontrendikedir; ritim tipi bilinmeden körlemesine vagal '
                                            'manevra yapılmamalıdır.'},
                         {'text': 'Hastayı monitörize edip damar yolu açmak, kan basıncı, bilinç durumu ve periferik '
                                  'perfüzyon ile ritmi değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Taşiaritmi ile başvuran hastada ilk adım hastanın hemodinamik stabilitesini '
                                         '(bilinç, tansiyon, perfüzyon) belirlemek ve kardiyak monitörizasyonu '
                                         'sağlamaktır.',
                          'new_finding': 'Vital bulgular: Bilinç açık ve koopere, KTA 190/dk (düzenli), SS 22/dk, TA '
                                         '95/62 mmHg, SpO2 %98, CRT 2 saniye. Periferik nabızlar zayıflamış ancak net '
                                         'alınıyor. Kardiyak muayenede taşikardi dışında üfürüm yok, akciğer sesleri '
                                         'doğal, periferik ödem veya hepatomegali saptanmadı. Hasta normotansif ve '
                                         'hemodinamik olarak stabildir.'},
                         {'text': 'Hastanın bilinci açık ve genel durumu iyi olduğu için sakinleştirici oral sedatif '
                                  'vererek karanlık bir odada dinlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Dinlenmeyle taşikardi gerilemedi, hasta göğüs ağrısı ve aşırı halsizlik '
                                             'hissetmeye devam etti.',
                          'teaching_point': 'Dakikada 190 atımlı taşikardiler primer aritmik patolojilerdir; dinlenme '
                                            'veya sedasyonla düzelmez, acil tanısal elektrokardiyografi gerektirir.'},
                         {'text': 'Taşikardik her ritim bozukluğunda ilk basamak olan hızlı intravenöz puşe adenozin '
                                  'uygulaması için defibrilatörsüz acil hazırlık yapmak',
                          'is_correct': False,
                          'scenario_update': 'Ritim tipi ve QRS morfolojisi incelenmeden hazırlanan puşe adenozin '
                                             'yaklaşımı, olası ventriküler aritmilerde dekompanzasyon riskini artırdı.',
                          'teaching_point': 'Ritim tipi elektrokardiyografi ile analiz edilmeden ve defibrilasyon '
                                            'hazırlığı tamamlanmadan körlemesine adenozin puşesi uygulanması '
                                            'tehlikelidir.'}]},
            {'stage_title': 'On İki Derivasyonlu Elektrokardiyografi ve Ritim Analizi',
             'question': 'Hemodinamisi stabil olan ancak belirgin taşikardisi devam eden bu hastada tanısal ritim '
                         'analizi için ne yapılmalıdır?',
             'options': [{'text': 'Acil on iki derivasyonlu elektrokardiyografiyle ventriküler aktivasyon süresini, '
                                  'atriyoventriküler ilişkiyi ve füzyon vuruşlarını analiz etmek',
                          'is_correct': True,
                          'explanation': 'Taşiaritmilerde kesin tanı 12 derivasyonlu elektrokardiyografi ile konur; '
                                         'QRS süresi, AV dissosiasyon ve füzyon vuruşları ayırıcı tanıda anahtardır.',
                          'new_finding': '12 Derivasyonlu EKG: Düzenli ritim, kalp tepe atımı 192/dk, QRS süresi 120 '
                                         'milisaniye (yaşa göre uzamış / >0.10 sn), P dalgaları ile QRS arasında '
                                         'bağımsızlık (belirgin atriyoventriküler dissosiasyon), aralarda yakalama ve '
                                         'füzyon vuruları izlendi.'},
                         {'text': 'Elektrokardiyografi çekmeden önce ritmi sonlandırmak amacıyla hastaya derin nefes '
                                  'aldırıp ıkındırarak arka arkaya vagal manevralar denemek',
                          'is_correct': False,
                          'scenario_update': 'Tekrarlanan vagal manevralar taşikardi hızını veya ritmini değiştirmedi, '
                                             'hastanın göğüs kafesindeki sıkıntı hissi devam etti.',
                          'teaching_point': 'Ventriküler kökenli taşiaritmiler atriyoventriküler nodu içermediği için '
                                            'vagal manevralara yanıt vermez; zaman kaybetmeden EKG çekilmelidir.'},
                         {'text': 'Yalnızca tek derivasyonlu monitör şeridi izleyerek kardiyak enzim ve elektrolit '
                                  'sonuçları çıkana kadar hiçbir girişim yapmamak',
                          'is_correct': False,
                          'scenario_update': 'Tek derivasyonda P dalgaları ve füzyon vuruları ayırt edilemedi, ritmin '
                                             'mekanizması aydınlatılamadığı için tanısal süreç kilitlendi.',
                          'teaching_point': 'Taşiaritmilerin ayırıcı tanısında tek derivasyonlu monitör şeridi '
                                            'yetersizdir; AV dissosiasyon ve QRS morfolojisi için tam 12 derivasyonlu '
                                            'EKG şarttır.'},
                         {'text': 'Ritim bozukluğunun olası intrakranial nedenlerini dışlamak amacıyla '
                                  'elektrokardiyografiyi erteleyip acil beyin manyetik rezonans görüntüleme istemek',
                          'is_correct': False,
                          'scenario_update': 'Radyoloji hazırlığı esnasında EKG çekimi gecikti ve hastanın kardiyak '
                                             'dekompanzasyon riski arttı.',
                          'teaching_point': 'Taşikardi ile başvuran hastada ilk ve en acil tanı aracı '
                                            'elektrokardiyografidir; beyin görüntülemelerinin acil ritim tanısında '
                                            'yeri yoktur.'}]},
            {'stage_title': 'Elektrokardiyografik Bulgularla Kesin Tanı',
             'question': "EKG'de QRS süresi >0.10 sn, AV dissosiasyon ve füzyon vuruşları saptanan stabil hastada "
                         'kesin tanınız nedir?',
             'options': [{'text': 'Dar QRS supraventriküler taşikardi',
                          'is_correct': False,
                          'scenario_update': "SVT'de QRS süresi normaldir (<0.09 sn) ve genellikle AV dissosiasyon "
                                             'veya füzyon vuruları görülmez.',
                          'teaching_point': 'QRS süresi uzamış taşikardilerde AV dissosiasyon ve füzyon vurularının '
                                            "varlığı SVT'yi dışlar."},
                         {'text': 'Aberran iletili sinüs taşikardisi',
                          'is_correct': False,
                          'scenario_update': 'Sinüs taşikardisinde her QRS öncesinde normal P dalgası bulunur ve hız '
                                             'genellikle yaşa bağlı fizyolojik sınırlardadır.',
                          'teaching_point': 'Hızın 190/dk olması, AV dissosiasyon bulunması sinüs taşikardisi ile '
                                            'bağdaşmaz.'},
                         {'text': 'Ortodromik atriyoventriküler reentran taşikardi',
                          'is_correct': False,
                          'scenario_update': "Ortodromik AVRT'de antegrad ileti AV noddan geçtiği için QRS kompleksi "
                                             'dar ve normal morfolojidedir.',
                          'teaching_point': 'Uzamış QRS ve AV dissosiasyon ortodromik AVRT tablosuyla uyumsuzdur.'},
                         {'text': 'Hemodinamik stabil ventriküler taşikardi',
                          'is_correct': True,
                          'explanation': 'QRS süresinin uzamış olması (>0.10 sn), atriyoventriküler dissosiasyon ve '
                                         'füzyon vuruşları ventriküler taşikardi için tanı koydurucudur; normotansif '
                                         'olması stabil olduğunu gösterir.',
                          'new_finding': 'Kesin tanı: Hemodinamik olarak stabil monomorfik ventriküler taşikardi.'}]},
            {'stage_title': 'Stabil Taşiaritminin Farmakolojik Tedavisi ve Yönetimi',
             'question': 'Bilinci açık, normotansif ve hemodinamik olarak stabil ventriküler taşikardi saptanan 8 '
                         'yaşındaki bu hastada en uygun tedavi yaklaşımı nedir?',
             'options': [{'text': 'Bilinci açık hastaya yeterli sedoanaljezi uygulamadan derhal iki yüz joule asenkron '
                                  'defibrilasyon şoku vererek ritmi sonlandırmak',
                          'is_correct': False,
                          'scenario_update': 'Stabil hastaya sedasyonsuz ve asenkron yüksek doz şok verilmesi ağır '
                                             'miyokardiyal travma, ağrı ve ventriküler fibrilasyon tetikledi.',
                          'teaching_point': 'Defibrilasyon yalnızca nabızsız VT veya ventriküler fibrilasyonda '
                                            'uygulanır; stabil hastada acil şok endikasyonu yoktur, antiaritmik '
                                            'infüzyon gerekir.'},
                         {'text': 'Ritmi düzeltmek amacıyla arka arkaya üç kez hızlı puşe intravenöz adenozin '
                                  'uygulayıp hastayı servise taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Adenozin ventriküler kaynaklı taşikardiyi sonlandırmadı, geçici '
                                             'bradikardi ve hipotansiyon atağına yol açtı.',
                          'teaching_point': "Adenozin AV nod bağımlı SVT'lerde etkilidir; ventriküler taşikardilerde "
                                            'tedavi edici değildir ve hastayı instabil hale getirebilir.'},
                         {'text': 'Senkronize kardiyoversiyon hazırlığı eşliğinde intravenöz amiodaron infüzyonu '
                                  'başlayarak hastayı çocuk kardiyoloji yoğun bakım ünitesinde izlemek',
                          'is_correct': True,
                          'explanation': 'Hemodinamik olarak stabil ventriküler taşikardide ilk basamak farmakolojik '
                                         'kardiyoversiyondur (İV amiodaron 5 mg/kg, 20-60 dakikada); olası '
                                         'dekompanzasyon için kardiyoversiyon hazır tutulmalıdır.',
                          'new_finding': 'Amiodaron infüzyonunun 35. dakikasında ritim sinüse döndü (KTA 94/dk, dar '
                                         'QRS). Çocuk kardiyoloji yoğun bakım ünitesinde sürekli monitörizasyona '
                                         'alındı.'},
                         {'text': 'Hastayı monitörden ayırıp oral digoksin tedavisi başlayarak ertesi gün çocuk '
                                  'kardiyoloji poliklinik kontrolüne gelmek üzere taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Monitörden ayrılan hastada ventriküler taşikardi dekompanse olarak '
                                             'senkop ve hipotansif şok gelişti.',
                          'teaching_point': 'Ventriküler taşikardili hiçbir hasta acil servisten oral ilaçla taburcu '
                                            'edilemez; yoğun bakımda sürekli ritim takibi zorunludur.'}]}]},
 {'id': 'S35',
  'category': '🌡️ Ateş & Döküntü / Enfeksiyon',
  'age': '9 Yaş',
  'gender': 'Erkek',
  'complaint': 'Gezici eklem ağrısı, diz ve ayak bileğinde şişlik, kızarıklık, subfebril ateş ve halsizlik',
  'history': "9 yaşındaki erkek çocuk ailesi tarafından eklem şişlikleri nedeniyle Sarı Alana getiriliyor: 'Üç hafta "
             'önce şiddetli boğaz ağrısı ve yüksek ateşi olmuştu, doktora götürmedik ve kendiliğinden geçmişti. Dört '
             'gün önce sağ dizi aniden şişti, kızardı ve dokununca şiddetli ağrıyordu. İki gün sonra sağ dizi '
             'hafiflerken bu kez sol ayak bileği şişti ve basamaz hale geldi. Çocuğumuz aşırı halsiz ve çabuk '
             "yoruluyor.'",
  'final_diagnosis': 'Akut Romatizmal Ateş (Kardit ve Gezici Poliartrit / Jones Kriterleri)',
  'disposition': 'Sarı Alanda İV Damar Yolu + Yatak İstirahati + Oral Penisilin V / Benzatin Penisilin G + '
                 'Antiinflamatuar Tedavi + Çocuk Kardiyoloji ve Romatoloji Servisine Yatış',
  'case_pearl': 'Akut romatizmal ateş (ARA), tedavi edilmemiş A Grubu Beta-Hemolitik Streptokok (AGBHS) farenjitinden '
                '2-4 hafta sonra gelişen sistemik otoimmün bir tablodur. Tanı revize Jones kriterlerine dayanır: '
                'Geçirilmiş streptokok enfeksiyonu kanıtı (ASO yüksekliği veya pozitif boğaz kültürü) eşliğinde 2 '
                'majör veya 1 majör + 2 minör kriter gereklidir. Majör kriterler: Gezici poliartrit, kardit (en sık '
                'mitral kapak yetersizliği), Sydenham koresi, eritema marjinatum ve subkutan nodüllerdir. Minör '
                "kriterler: Ateş, artralji, yüksek ESH/CRP ve EKG'de uzamış PR intervalidir (1. derece AV blok). "
                'Tedavide streptokok eradikasyonu (benzatin penisilin veya oral penisilin), kardit ve artrit için '
                'antiinflamatuar tedavi (aspirin veya steroid) ve sekonder profilaksi esastır.',
  'steps': [{'stage_title': 'Sarı Alanda Gezici Artritli Hastaya İlk Yaklaşım',
             'question': 'Üç hafta önceki farenjit sonrası gezici eklem tutulumu gelişen 9 yaşındaki çocukta ilk '
                         'muayene önceliğiniz ne olmalıdır?',
             'options': [{'text': 'Eklem şişliğini primer septik artrit kabul ederek eklemi aspire edip acil cerrahi '
                                  'artrotomi için ortopediye devretmek',
                          'is_correct': False,
                          'scenario_update': 'Eklem aspirasyonunda pürülan mayi gelmedi; gereksiz invaziv artrotomi '
                                             'girişimi gezici karakterdeki sistemik inflamasyonu aydınlatamadı.',
                          'teaching_point': 'Gezici karakterdeki poliartritlerde tek ekleme odaklanıp cerrahi '
                                            'artrotomi yapmak hatalıdır; sistemik ve kardiyovasküler muayene '
                                            'önceliklidir.'},
                         {'text': 'Yalnızca eklem ultrasonografisi isteyerek kardiyovasküler oskültasyon yapmadan '
                                  'yüksek doz intramüsküler analjezik uygulayıp hastayı yatakta dinlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Analjezik ağrıyı geçici azalttı ancak kardiyak oskültasyon yapılmadığı '
                                             'için apeksteki belirgin pansistolik üfürüm gözden kaçırıldı.',
                          'teaching_point': 'Geçirilmiş farenjit ve gezici artrit öyküsünde kardiyak oskültasyon '
                                            'hayatidir; kardit bulguları atlanmamalıdır.'},
                         {'text': 'Geçirilmiş farenjit öyküsünü göz ardı edip travmatik bağ yaralanması ön tanısıyla '
                                  'bilateral alt ekstremiteye alçı uygulamak',
                          'is_correct': False,
                          'scenario_update': 'Alçı tespiti uygulanan eklemde enflamasyon ve ısı artışı devam etti, '
                                             'sistemik hastalık tablosu ilerledi.',
                          'teaching_point': 'Travma öyküsü olmayan, bir eklemden diğerine göç eden artrit tablosunda '
                                            'ortopedik immobilizasyon değil sistemik etiyoloji araştırılmalıdır.'},
                         {'text': 'Eklem bulgularını değerlendirirken kalp seslerini dikkatle oskülte ederek apekste '
                                  'pansistolik üfürüm ve kapak disfonksiyonunu araştırmak',
                          'is_correct': True,
                          'explanation': 'Geçirilmiş farenjit sonrası gezici poliartrit tablosunda subklinik veya '
                                         'klinik kardit gelişimini saptamak için kardiyak oskültasyon zorunludur.',
                          'new_finding': 'Vital bulgular: Ateş 38.3°C, KTA 110/dk, SS 20/dk, TA 105/65 mmHg. Sol ayak '
                                         'bileğinde belirgin eritem, şişlik, sıcaklık artışı ve hareket kısıtlılığı '
                                         'mevcut; sağ dizde hafif hassasiyet izlendi. Kardiyak oskültasyonda apekste '
                                         'aksillaya yayılan 3/6 pansistolik üfürüm duyuldu, S3 veya perikardiyal '
                                         'frotman yok. Ciltte döküntü veya subkutan nodül saptanmadı.'}]},
            {'stage_title': 'Laboratuvar Belirteçleri ve Kardiyak İnceleme',
             'question': 'Gezici eklem tutulumu ve mitral üfürüm saptanan bu hastada sistemik tutulumu netleştirecek '
                         'tetkik planınız ne olmalıdır?',
             'options': [{'text': 'Gezici eklem tutulumunu aydınlatmak amacıyla her iki diz ve ayak bileğine '
                                  'kontrastlı manyetik rezonans görüntüleme tetkiki çekmek',
                          'is_correct': False,
                          'scenario_update': 'Manyetik rezonansta eklem içi efüzyon ve sinovyal kalınlaşma dışında '
                                             'etiyolojik tanıya katkı sağlayan ek bilgi elde edilemedi.',
                          'teaching_point': 'Artrit tanısında eklem MRG rutin tetkik değildir; geçirilmiş streptokok '
                                            'enfeksiyonu ve kardiyak tutulumu göstermez.'},
                         {'text': 'Sistemik etiyolojiyi araştırmadan yalnızca serum kan glukozu ve böbrek fonksiyon '
                                  'testleri isteyerek hastayı gözlemde tutmak',
                          'is_correct': False,
                          'scenario_update': 'Böbrek testleri normal geldi ancak kardiyak kapak tutulumu ve streptokok '
                                             'belirteçleri araştırılmadığı için tanı gecikti.',
                          'teaching_point': 'Gezici artrit ve üfürüm tablosunda ASO, akut faz reaktifleri ve '
                                            'elektrokardiyografi istenmeden hasta bekletilemez.'},
                         {'text': 'Streptokok belirteçleri, akut faz reaktifleri ve olası ileti bozukluklarını '
                                  'saptamak amacıyla elektrokardiyografi ile ekokardiyografi planlamak',
                          'is_correct': True,
                          'explanation': 'Tanı için geçirilmiş streptokok kanıtı (ASO), minör kriterler (ESH, CRP, '
                                         'uzamış PR) ve kardit kanıtı (ekokardiyografide kapak yetersizliği) '
                                         'gereklidir.',
                          'new_finding': 'Laboratuvar: ASO >800 IU/mL (normal <200), CRP 68 mg/L, ESH 75 mm/saat, '
                                         'Lökosit 13.600/mm³, Boğaz kültürü negatif. EKG: Sinüs ritmi, PR intervali '
                                         '0.20 sn (yaşa göre uzamış, 1. derece AV blok). Ekokardiyografi: Mitral '
                                         'kapakta kalınlaşma, hafif-orta derecede mitral yetersizlik jeti saptandı; '
                                         'sol ventrikül fonksiyonları normal.'},
                         {'text': 'Viral artrit düşüncesiyle hiçbir laboratuvar tetkiki istemeden hastaya yalnızca '
                                  'semptomatik lokal buz uygulaması ve istirahat önermek',
                          'is_correct': False,
                          'scenario_update': 'Buz uygulamasıyla eklem ağrısı gerilemedi, üfürümün nedeni '
                                             'aydınlatılamadı ve kardiyak tutulum ilerleme riskiyle karşı karşıya '
                                             'kaldı.',
                          'teaching_point': 'Üfürüm eşlik eden gezici artritlerde viral etiyoloji varsayımıyla '
                                            'tetkiksiz izlem kabul edilemez; streptokok immünolojik yanıtı '
                                            'araştırılmalıdır.'}]},
            {'stage_title': 'Jones Kriterleri Işığında Kesin Tanı',
             'question': 'Belgelenmiş streptokok enfeksiyonu, kardit, gezici poliartrit, yüksek akut faz reaktifleri '
                         've uzamış PR saptanan hastada kesin tanınız nedir?',
             'options': [{'text': 'Juvenil idiyopatik artrit',
                          'is_correct': False,
                          'scenario_update': "JİA'da artrit en az altı hafta sebat eder, gezici karakterde değildir ve "
                                             'geçirilmiş streptokok kanıtı veya PR uzaması beklenmez.',
                          'teaching_point': 'Kısa sürede eklem değiştiren gezici poliartrit ve kardit tablosu juvenil '
                                            'idiyopatik artritten ziyade akut romatizmal ateşe işaret eder.'},
                         {'text': 'Akut romatizmal ateş',
                          'is_correct': True,
                          'explanation': 'Yüksek ASO varlığında 2 majör kriter (kardit, gezici poliartrit) ve 2 minör '
                                         'kriter (ateş, uzamış PR, yüksek ESH/CRP) Jones kriterlerine göre kesin akut '
                                         'romatizmal ateş tanısı koydurur.',
                          'new_finding': 'Kesin tanı: Akut romatizmal ateş (mitral valvülit/kardit ve gezici '
                                         'poliartrit).'},
                         {'text': 'Poststreptokoksik reaktif artrit',
                          'is_correct': False,
                          'scenario_update': 'Poststreptokoksik reaktif artritte eklem tutulumu gezici değildir, '
                                             "aspirine dramatik yanıt vermez ve kardit veya EKG'de PR uzaması eşlik "
                                             'etmez.',
                          'teaching_point': 'Kardiyak valvülit ve PR uzaması varlığı tabloyu reaktif artritten ayırır, '
                                            'akut romatizmal ateşi kesinleştirir.'},
                         {'text': 'Sistemik lupus eritematozus',
                          'is_correct': False,
                          'scenario_update': "SLE'de malar döküntü, fotosensitivite, böbrek tutulumu ve pozitif "
                                             'otoantikorlar (ANA, anti-dsDNA) beklenir; geçirilmiş streptokokla '
                                             'ilişkili değildir.',
                          'teaching_point': "Ateş, kardit ve geçirilmiş streptokok farenjiti SLE'den ziyade romatizmal "
                                            'kardit tablosudur.'}]},
            {'stage_title': 'Eradikasyon, Antiinflamatuar Tedavi ve İzlem Planı',
             'question': 'Akut romatizmal ateş tanısı kesinleşen 9 yaşındaki bu hastanın medikal tedavisi ve '
                         'hospitalizasyon yönetimi nasıl olmalıdır?',
             'options': [{'text': 'Streptokok eradikasyonu için penisilin başlamak, antiinflamatuar tedavi planlayıp '
                                  'kardit izlemi amacıyla hastayı çocuk servisine yatırmak',
                          'is_correct': True,
                          'explanation': 'Akut romatizmal ateşte yaklaşım streptokok eradikasyonu (benzatin penisilin '
                                         'G veya oral penisilin V), kardit/artrit için antiinflamatuar tedavi ve yatak '
                                         'istirahatidir.',
                          'new_finding': 'Tek doz intramüskler benzatin penisilin G yapıldı, antiinflamatuar tedavi ve '
                                         'yatak istirahati altında kardit izlemi için çocuk kardiyoloji servisine '
                                         'yatırıldı.'},
                         {'text': 'Kapak tutulumu saptandığı için hastayı derhal acil açık kalp ameliyatına alarak '
                                  'mekanik mitral kapak protezi takmak',
                          'is_correct': False,
                          'scenario_update': 'Akut enflamasyon evresinde kapak dokuları frajildir; medikal tedavi '
                                             'denenmeden cerrahiye alınması ağır komplikasyonlara yol açar.',
                          'teaching_point': 'Akut romatizmal karditte öncelik cerrahi değil medikal antiinflamatuar '
                                            'tedavidir; cerrahi yalnızca dirençli ve medikal tedaviye yanıtsız akut '
                                            'kalp yetersizliğinde düşünülür.'},
                         {'text': 'Hiçbir medikal tedavi vermeden yalnızca mutlak yatak istirahati önererek hastayı '
                                  'doğrudan evine taburcu edip kontrole çağırmak',
                          'is_correct': False,
                          'scenario_update': 'Tedavi edilmeyen hastada streptokok taşıyıcılığı devam etti, kapak '
                                             'tutulumu ilerleyerek kalıcı kronik romatizmal kapak hastalığına dönüştü.',
                          'teaching_point': 'Antibiyotik eradikasyonu ve antiinflamatuar tedavi yapılmaksızın '
                                            'taburculuk kabul edilemez; kalıcı kapak hasarı riski yüksektir.'},
                         {'text': 'Akut inflamasyonu baskılamak amacıyla yüksek doz intravenöz immünoglobulin '
                                  'infüzyonu uygulayıp başka hiçbir antibiyotik tedavisi vermemek',
                          'is_correct': False,
                          'scenario_update': 'İntravenöz immünoglobulin romatizmal karditte kanıtlanmış etkinliğe '
                                             'sahip değildir ve streptokok eradikasyonunu sağlamadığı için enfeksiyon '
                                             'devam etti.',
                          'teaching_point': 'Akut romatizmal ateşte IVIG standart tedavi değildir; penisilin ile '
                                            'streptokok eradikasyonu ve antiinflamatuar tedavi şarttır.'}]}]},
 {'id': 'S36',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '7 Yaş',
  'gender': 'Kız',
  'complaint': 'İki hafta önceki ishalin ardından ayak parmaklarında başlayan uyuşma, bacaklardan yukarı yayılan kas '
               'güçsüzlüğü ve ayağa kalkamama',
  'history': "7 yaşındaki kız çocuğu annesi tarafından Sarı Alana getiriliyor: 'Yaklaşık on gün önce geçirdiği sulu "
             'ishal ve karın ağrısı tamamen düzelmişti. Üç gün önce önce ayak parmaklarında karıncalanma hissettiğini '
             'söyledi, ardından yürürken sendelemeye ve merdiven çıkamamaya başladı. Bugün sabahtan beri bacaklarını '
             'hiç kaldıramıyor, yataktan tek başına kalkamıyor ve kollarını kaldırırken de güçsüzlük hissettiğini '
             "söylüyor. İdrar veya dışkı kaçırması olmadı.'",
  'final_diagnosis': 'Guillain-Barré Sendromu (Akut İnflamatuar Demiyelinizan Polinöropati - AIDP)',
  'disposition': 'Çocuk Yoğun Bakım Ünitesine Yatış + İntravenöz İmmünglobulin (IVIG, 2 g/kg) İnfüzyonu + Seri Vital '
                 'Kapasite ve Solunum / Otonomik Monitörizasyon',
  'case_pearl': 'Guillain-Barré Sendromu (GBS), sıklıkla geçirilmiş gastrointestinal (Campylobacter jejuni vb.) veya '
                'üst solunum yolu enfeksiyonunu izleyen, simetrik, asendan (aşağıdan yukarı ilerleyen) flask paralizi '
                've arefleksi ile karakterize post-enfeksiyöz otoimmün periferik polinöropatidir. En kritik hayatı '
                'tehdit edici riskler diyafram ve interkostal solunum kası tutulumuna bağlı solunum yetmezliği ile '
                'otonom disfonksiyondur (ani kardiyak aritmiler, labil kan basıncı). Lomber ponksiyonda protein '
                'yüksekliği ve lökosit sayısının normal olması (albüminositolojik dissosiasyon) tanıyı destekler ancak '
                'erken dönemde protein düzeyi normal çıkabilir. Birinci basamak immünomodülatör tedavi İVİG (2 g/kg, '
                '2-5 günde) veya plazmaferezdir; kortikosteroidlerin tek başına plaseboya üstünlüğü gösterilmemiştir '
                've önerilmez.',
  'steps': [{'stage_title': 'Sarı Alanda İlk Değerlendirme ve Nöromusküler Solunum Muayenesi',
             'question': 'İlerleyici simetrik kas güçsüzlüğü ve yürüme kaybı ile başvuran 7 yaşındaki çocukta ilk '
                         'muayene ve güvenlik yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Sadece kaba kas gücünü değerlendirip periferik nöropati şüphesiyle çocuğu servise '
                                  'yatırmak, solunum seslerini ve diyafram hareketlerini izlem dışı bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Solunum fonksiyonları izlenmeyen hastada saatler içinde sinsi diyafram '
                                             'parezisi gelişti, takipne ve hipoksemi fark edilmeyerek akut solunum '
                                             'arresti tablosu ortaya çıktı.',
                          'teaching_point': 'İlerleyici flask paralizilerde diyafram ve interkostal solunum kası '
                                            'tutulumu hayatı tehdit eder; hastanın solunum paternı, vital kapasitesi '
                                            've periferik oksijenasyonu sürekli değerlendirilmelidir.'},
                         {'text': 'Ekstremite motor gücünü, derin tendon reflekslerini ve solunum paternini inceleyip '
                                  'zorlu vital kapasite takibi amacıyla monitörize alana almak',
                          'is_correct': True,
                          'explanation': 'Asendan kas güçsüzlüklerinde solunum yetmezliği ve kardiyovasküler '
                                         'instabilite riski nedeniyle motor güç, refleksler ve vital kapasite '
                                         'öncelikli olarak değerlendirilmeli ve monitörize edilmelidir.',
                          'new_finding': 'Vital Bulgular: KTA 98/dk, SS 22/dk, TA 108/66 mmHg, SpO2 %98, Ateş 36.6°C. '
                                         'Fizik Muayene: Bilinç açık, kooperasyonu tam, kranial sinir muayenesi doğal. '
                                         'Kas gücü alt ekstremite distalde 2/5, proksimalde 3/5, üst ekstremitede 4/5 '
                                         'düzeyinde simetrik azalmış. Bilateral patella ve aşil refleksleri alınamadı '
                                         '(arefleksi), üst ekstremitede hiporefleksi saptandı. Patolojik refleks yok. '
                                         "Tek nefeste 25'e kadar sayabiliyor, yüzeyel duyular korunmuş."},
                         {'text': 'Kas güçsüzlüğünü histerik konversiyon reaksiyonu kabul ederek psikiyatri '
                                  'konsültasyonu istemek ve sedasyon uygulayarak motor fonksiyonların uykuda '
                                  'düzelmesini izlemek',
                          'is_correct': False,
                          'scenario_update': 'Organik flask paralizisi olan hastaya uygulanan sedatif ajan solunum '
                                             'eforunu daha da baskılayarak derin hipoventilasyon ve hiperkapni '
                                             'gelişimine zemin hazırladı.',
                          'teaching_point': 'Derin tendon reflekslerinin kaybı (arefleksi) ve simetrik flask kas '
                                            'zayıflığı kesin organik periferik nöropati göstergesidir; bu tablo asla '
                                            'psikosomatik reaksiyon olarak yorumlanamaz.'},
                         {'text': 'Dengesizlik ve güç kaybının santral vestibüler kökenli olduğunu varsayıp oral '
                                  'dimenhidrinat tedavisi başlamak ve semptomların ayaktan gerilemesini beklemek',
                          'is_correct': False,
                          'scenario_update': 'Vestibüler supresan verilen hastada nörolojik kayıplar saatler içinde '
                                             'yukarı doğru ilerledi, üst ekstremitelerde tam güç kaybı ve yutma '
                                             'güçlüğü eklendi.',
                          'teaching_point': 'Bilateral arefleksi ve asendan güç kaybı periferik sinir lezyonunu işaret '
                                            'eder; vestibüler patolojiler flask kas güçsüzlüğü ve derin tendon '
                                            'refleksi kaybı yapmaz.'}]},
            {'stage_title': 'Laboratuvar İncelemeleri ve Lomber Ponksiyon Analizi',
             'question': 'İlerleyici asendan flask parezi ve arefleksi saptanan bu hastada ayırıcı klinik tabloyu '
                         'netleştirmek için en uygun tetkik yaklaşımı nedir?',
             'options': [{'text': 'Yalnızca kan elektrolitleri ve tam idrar tetkiki göndermek, lomber ponksiyon '
                                  'girişimini lüzumsuz bularak ileri nörolojik tetkik planlamadan izlem yapmak',
                          'is_correct': False,
                          'scenario_update': 'Elektrolitleri ve idrarı normal çıkan hastanın patolojisi '
                                             'aydınlatılamadı; tanı ve hedefe yönelik immünomodülatör tedavi geciktiği '
                                             'için kas zayıflığı göğüs kafesine yayıldı.',
                          'teaching_point': 'Akut simetrik flask polinöropatilerde BOS incelemesi ve nörogörüntüleme '
                                            'kilit rol oynar; yalnızca rutin biyokimya ile tanı konulamaz ve tedavi '
                                            'geciktirilmemelidir.'},
                         {'text': 'Tüm omurgayı kapsayan acil direkt röntgen grafileri çekmek ve kalsiyum yüksekliğini '
                                  'dışlamak amacıyla parathormon ile idrar kalsiyum düzeylerini incelemek',
                          'is_correct': False,
                          'scenario_update': 'Direkt kemik grafileri ve kalsiyum metabolizması tetkikleri tamamen '
                                             'normal geldi; çekimler esnasında zaman kaybedilerek hastanın solunum '
                                             'kası rezervi azaldı.',
                          'teaching_point': 'Direkt radyografiler nöral dokuları ve periferik sinir inflamasyonunu '
                                            'göstermez; akut nöromusküler güçsüzlükte radyografik kemik grafilerinin '
                                            'yeri yoktur.'},
                         {'text': 'Öncelikle periferik sinir biyopsisi için cerrahi hazırlık yapmak ve histopatolojik '
                                  'teyit gelene kadar lomber ponksiyon uygulamasını kesinlikle ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz invaziv biyopsi hazırlığı saatler sürdü ve cerrahi stres '
                                             'altında hastanın hemodinamik stabilitesi bozularak taşiaritmi atakları '
                                             'tetiklendi.',
                          'teaching_point': 'Akut periferik polinöropati tanısında sinir biyopsisi kesinlikle endike '
                                            'değildir; tanı BOS incelemesi, klinik bulgular ve gerekirse '
                                            'elektrofizyoloji ile konulur.'},
                         {'text': 'Acil beyin-omurilik manyetik rezonans görüntüleme ile basıyı dışlamak ve beyin '
                                  'omurilik sıvısı biyokimya-hücre analizini gerçekleştirmek',
                          'is_correct': True,
                          'explanation': 'Miyelopati ve spinal kord basısını dışlamak için MRG, periferik sinir kök '
                                         'tutulumu ve protein artışını göstermek için BOS analizi altın standart '
                                         'adımlardır.',
                          'new_finding': 'Spinal ve Kraniyal MRG: Akut kord basısı, miyelit veya kitle lezyonu '
                                         'saptanmadı; lomber sinir köklerinde ve kauda ekinada kontrast tutulumu '
                                         'izlendi. Lomber Ponksiyon Analizi: BOS berrak, açılış basıncı 130 mmH2O '
                                         '(normal). Mikroskopi: 1 lökosit/mm³ (hücresel artış yok). BOS Proteini: 148 '
                                         'mg/dL (belirgin yüksek, normal: 15-45 mg/dL), BOS Glukozu: 64 mg/dL (eş '
                                         'zamanlı kan şekeri 98 mg/dL). Serum elektrolitleri, kreatin kinaz (CK) ve '
                                         'tiroid fonksiyonları normal.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': "Gastroenterit öyküsü sonrası simetrik asendan flask paralizi, arefleksi ve BOS'ta hücre "
                         'artışı olmaksızın izole protein yüksekliği saptanan hastada öncelikli klinik tanınız nedir?',
             'options': [{'text': 'Guillain-Barré Sendromu (Akut Polinöropati)',
                          'is_correct': True,
                          'explanation': 'Geçirilmiş enfeksiyonu takiben simetrik ilerleyici asendan kas zayıflığı, '
                                         "arefleksi ve BOS'ta albüminositolojik dissosiasyon varlığı tipik "
                                         'Guillain-Barré sendromu (AIDP) tablosudur.',
                          'new_finding': 'Kesin Tanı: Guillain-Barré Sendromu (Akut İnflamatuar Demiyelinizan '
                                         'Polinöropati). Solunum kası yorgunluğu ve otonom disfonksiyon riski '
                                         'açısından ileri tedavi planlandı.'},
                         {'text': 'Akut Transvers Miyelit',
                          'is_correct': False,
                          'scenario_update': 'Akut transvers miyelitte belirgin duyusal seviye, erken sfinkter '
                                             "disfonksiyonu (idrar retansiyonu), patolojik refleksler ve MRG'de "
                                             'intramedüller hiperintens lezyon bulunur.',
                          'teaching_point': 'Transvers miyelit üst motor nöron bulguları, belirgin duyusal düzey ve '
                                            'mesane tutulumuyla seyreder; bu hastada duyusal düzey yokluğu ve '
                                            'arefleksi periferik patolojiyi gösterir.'},
                         {'text': 'Akut Spinal Epidural Apse',
                          'is_correct': False,
                          'scenario_update': 'Spinal epidural apse lokal şiddetli sırt ağrısı, perküsyon hassasiyeti, '
                                             "sistemik toksisite, kord basısı ve MRG'de epidural kitle görünümü ile "
                                             'seyreder.',
                          'teaching_point': "Epidural apse akut spinal kord kompresyonuna yol açar; omurilik MRG'de "
                                            'epidural alanın tamamen temiz olması bu tanıyı kesin olarak ekarte '
                                            'ettirir.'},
                         {'text': 'Besin Kaynaklı Botulizm İntoksikasyonu',
                          'is_correct': False,
                          'scenario_update': 'Botulizmde kas güçsüzlüğü aşağıdan yukarı değil, kranial sinirlerden '
                                             '(ptozis, diplopi, midriyazis, disfoni) başlayıp desendan (yukarıdan '
                                             'aşağı) yayılım gösterir.',
                          'teaching_point': 'Botulizm bulber ve kranial sinir tutulumuyla başlayıp aşağı doğru iner; '
                                            'Guillain-Barré sendromunda ise güçsüzlük tipik olarak alt '
                                            'ekstremitelerden yukarıya doğru yükselir.'}]},
            {'stage_title': 'Yoğun Bakım Takibi ve İmmünomodülatör Tedavi',
             'question': 'Tanısı kesinleşen ve solunum kas tutulumu riski bulunan 7 yaşındaki hastada en uygun yatış '
                         've farmakolojik tedavi stratejisi nedir?',
             'options': [{'text': 'Genel pediatri servisinde izleme almak ve tek başına yüksek doz intravenöz '
                                  'metilprednizolon tedavisi uygulayarak motor gücün toparlanmasını beklemek',
                          'is_correct': False,
                          'scenario_update': 'Tek başına kortikosteroid verilen hastada motor toparlanma hızlanmadı, '
                                             'aksine solunum kas gücü daha da zayıflayarak entübasyon gereksinimi '
                                             'doğdu.',
                          'teaching_point': 'Guillain-Barré sendromunda tek başına kortikosteroidlerin etkinliği '
                                            'yoktur ve önerilmez; kanıtlanmış birinci basamak tedavi İVİG veya '
                                            'plazmaferezdir.'},
                         {'text': 'Solunum şikayeti henüz belirginleşmediği için hastayı evde istirahate göndermek ve '
                                  'haftalık fizik tedavi seansları ile poliklinikten takip etmek',
                          'is_correct': False,
                          'scenario_update': 'Eve gönderilen hasta gece saatlerinde ani solunum arresti ve otonomik '
                                             'aritmi nedeniyle acile arrest tablosunda geri getirildi.',
                          'teaching_point': 'GBS olgularında vital kapasite aniden düşebilir ve ölümcül otonom '
                                            'instabilite gelişebilir; hastalar mutlaka yoğun bakım koşullarında '
                                            'monitörize edilmelidir.'},
                         {'text': 'Çocuk Yoğun Bakımda vital kapasiteyi izlemek ve toplam iki gram bölü kilogram '
                                  'intravenöz immünglobulin infüzyonu başlamak',
                          'is_correct': True,
                          'explanation': 'GBS tedavisinde toplam 2 g/kg İVİG (genellikle 2 veya 5 güne bölünerek) '
                                         'standart birinci basamak tedavidir; solunum yetmezliği riski nedeniyle yoğun '
                                         'bakım izlemi şarttır.',
                          'new_finding': 'Hasta Çocuk Yoğun Bakım Ünitesine yatırıldı. Toplam 2 g/kg dozundaki İVİG '
                                         'infüzyonu (günde 0.4 g/kg, 5 gün) başlandı. Sürekli vital kapasite, pik '
                                         'ekspiratuar akım ve kardiyak monitörizasyon yapıldı. 48. saatten itibaren '
                                         'motor güç ilerlemesi durdu, mekanik ventilasyon gereksinimi olmadan 7. günde '
                                         'yürüme egzersizlerine başlandı.'},
                         {'text': 'Oral asetilsalisilik asit ve periferik kas gevşetici reçete ederek serviste '
                                  'izlemek, mekanik ventilatör desteği veya immünomodülatör tedavi planlamamak',
                          'is_correct': False,
                          'scenario_update': 'Antienflamatuar ve kas gevşetici verilen hastanın flask paralizisi hızla '
                                             'interkostal kaslara yayılarak akut hiperkapnik solunum yetmezliği '
                                             'tablosuna yol açtı.',
                          'teaching_point': 'Periferik kas gevşeticiler solunum kas paralizisini şiddetlendirir; '
                                            "GBS'de immünomodülasyon (İVİG/plazmaferez) ve solunum desteği dışındaki "
                                            'tedaviler yetersiz ve tehlikelidir.'}]}]},
 {'id': 'S37',
  'category': '🧠 Nörolojik Belirtiler & Konvülziyon',
  'age': '4 Yaş',
  'gender': 'Erkek',
  'complaint': 'İki hafta önceki döküntülü viral enfeksiyon sonrası aniden başlayan sendeleme, sarhoşvari yürüme, '
               'eşyaları tutamama ve gözlerde titreme',
  'history': "4 yaşındaki erkek çocuğun ebeveynleri çocuklarını kucaklarında Sarı Alana getiriyor: 'Yaklaşık on gün "
             'önce vücudunda döküntüler ve hafif ateşi olmuştu, tamamen iyileşmişti. Dün akşamdan beri yürürken '
             'bacaklarını çok açıyor, sarhoş gibi sağa sola sendeliyor ve düşüyor. Su bardağına uzandığında eli '
             'titriyor ve bardağı deviriyor. Gözlerinde de bazen sağa sola hızlı titremeler fark ettik. Ateşi, '
             "kusması, baş ağrısı veya nöbeti olmadı.'",
  'final_diagnosis': 'Akut Serebellar Ataksi (Post-enfeksiyöz Akut Serebellit)',
  'disposition': 'Sarı Alanda Acil Kraniyal Görüntüleme ile Kitle / Kanamanın Dışlanması + Çocuk Nörolojisi / Servis '
                 'Yatışı ile Düşme Önlemleri ve Destek Tedavisi',
  'case_pearl': 'Akut serebellar ataksi, çocukluk çağında ani başlangıçlı yürüme bozukluğunun ve koordinasyon kaybının '
                'en sık nedenidir. Genellikle suçiçeği, EBV, koksaki veya diğer viral enfeksiyonlardan 1-3 hafta sonra '
                'otoimmün serebellar inflamasyon (akut serebellit) sonucu ortaya çıkar. En karakteristik bulguları '
                'geniş tabanlı dengesiz yürüyüş, dismetri (hedefi tutturamama), disdiadokokinez (ardışık hareket '
                'bozukluğu), intansiyonel tremor ve horizontal nistagmustur. Ateş, kafa içi basınç artışı bulgusu ve '
                'ense sertliği beklenmez. Acil serviste öncelikle beyin görüntülemesi (MRG/BT) yapılarak posterior '
                'fossa kitleleri, kanama veya inme dışlanmalıdır. Selim seyirlidir; olguların büyük çoğunluğu haftalar '
                'veya aylar içinde sekelsiz kendiliğinden düzelir, rutin steroid veya immünosüpresif tedavi '
                'gerektirmez.',
  'steps': [{'stage_title': 'Sarı Alanda Nörolojik Değerlendirme ve Koordinasyon Muayenesi',
             'question': 'Ani başlayan sendeleme, sarhoşvari dengesiz yürüme ve hedefi tutturamama şikayetiyle '
                         'getirilen 4 yaşındaki çocukta ilk muayene yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Sadece kaba ekstremite kas gücünü ve eklem hareket açıklığını değerlendirmek, '
                                  'koordinasyon testlerini ve göz hareketlerini muayene etmeden beklemek',
                          'is_correct': False,
                          'scenario_update': 'Yalnızca kaba motor muayene yapılan çocukta serebellar korteks '
                                             'bulguları, nistagmus ve dismetri atlanarak santral patolojinin yeri '
                                             'tespit edilemedi.',
                          'teaching_point': 'Ani denge kaybıyla başvuran çocuklarda ekstremite kas gücü çoğunlukla '
                                            'normaldir; tanı için dismetri, nistagmus ve yürüyüş paterni mutlaka '
                                            'incelenmelidir.'},
                         {'text': 'Gözlerdeki titremeyi konvülziyon eşdeğeri kabul ederek acil rektal diazepam '
                                  'uygulamak ve hastayı derin sedasyonda izleyerek yürütmeyi denememek',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz sedatif uygulanan çocuk derin uykuya daldı; nörolojik muayene '
                                             'yapılamaz hale geldi ve hava yolu güvenliği riske girdi.',
                          'teaching_point': 'Horizontal nistagmus ve tremor nöbet bulgusu değildir; sedasyon '
                                            'uygulanması bilinci baskılar ve altta yatan koordinasyon muayenesini '
                                            'imkansız kılar.'},
                         {'text': 'Bilinç, kranial sinirler, nistagmus, parmak-burun testi, ardışık hareketler ve '
                                  'geniş tabanlı yürüyüş paternini detaylı serebellar muayeneyle değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Ani denge ve koordinasyon kayıplarında bilinç, nistagmus, dismetri, '
                                         'disdiadokokinez ve yürüyüş paterni incelenerek serebellar sistem işlevleri '
                                         'analiz edilmelidir.',
                          'new_finding': 'Vital Bulgular: Ateş 36.8°C, KTA 104/dk, SS 20/dk, TA 96/60 mmHg, SpO2 %99. '
                                         'Bilinç tam açık, koopere ve oryante, ense sertliği yok. Göz dibi '
                                         'muayenesinde papilödem saptanmadı. Her iki yana bakışta belirgin bilateral '
                                         'horizontal nistagmus mevcut. Parmak-burun ve diz-topuk testinde belirgin '
                                         'dismetri ve intansiyonel tremor var; ardışık el hareketlerinde '
                                         'disdiadokokinez pozitif. Çocuk desteksiz durmakta zorlanıyor, adımlarını '
                                         'geniş açarak sendeleyerek sarhoşvari yürüyor. Kas gücü 5/5 tam, derin tendon '
                                         'refleksleri normoaktif, Babinski negatif.'},
                         {'text': 'Dengesizliği iç kulak patolojisine bağlayarak yalnızca otoskopik kulak muayenesi '
                                  'yapmak ve semptomların düzelmesi için antihistaminik şurup verip taburculuk '
                                  'planlamak',
                          'is_correct': False,
                          'scenario_update': 'Sadece otoskopi yapılıp eve gönderilen çocukta intansiyonel tremor ve '
                                             'dismetri ilerledi, su içerken boğulma tehlikesiyle acil servise tekrar '
                                             'getirildi.',
                          'teaching_point': 'Bilateral nistagmus, intansiyonel tremor ve dismetri periferik vestibüler '
                                            'değil santral serebellar kökeni gösterir; kapsamlı nörolojik '
                                            'değerlendirme zorunludur.'}]},
            {'stage_title': 'Acil Nörogörüntüleme ve İntrakraniyal Acilleri Dışlama',
             'question': 'Akut koordinasyon bozukluğu, dismetri ve nistagmus saptanan 4 yaşındaki hastada hayatı '
                         'tehdit eden patolojileri dışlamak için en doğru tetkik nedir?',
             'options': [{'text': 'Acil beyin görüntülemesi ile arka çukur kitle, kanama ve akut enfarktüs '
                                  'lezyonlarını güvenle ekarte etmek',
                          'is_correct': True,
                          'explanation': 'Ani başlangıçlı serebellar bulgularda posterior fossa tümörleri, serebellar '
                                         'hemoraji, abse ve akut hidrosefali gibi cerrahi aciller acil görüntülemeyle '
                                         'dışlanmalıdır.',
                          'new_finding': 'Kraniyal MRG: Arka çukur, serebellar hemisferler, dördüncü ventrikül ve '
                                         'beyin sapı doğal formdadır; kitle, akut kanama, iskemi, fokal herniasyon '
                                         'veya hidrosefali saptanmadı; serebellar folialarda hafif silinme ve '
                                         'post-enfeksiyöz hafif hiperintens sinyal artışı izlendi. Rutin Kan Analizi: '
                                         'Hemogram normal (WBC 7.800/mm³), CRP 1.2 mg/L, sedimantasyon normal, serum '
                                         'elektrolitleri, glukoz ve karaciğer-böbrek testleri tamamen normal.'},
                         {'text': 'Öncelikle elektroensefalografi çekmek ve görüntüleme yapmadan önce iki hafta '
                                  'boyunca evde yatak istirahati vererek semptomların gidişatını izlemek',
                          'is_correct': False,
                          'scenario_update': 'Görüntüleme yapılmadığı için arka çukur patolojileri dışlanamadı ve '
                                             'ailede şiddetli kaygı gelişti; klinik şüphe giderilemeyerek gereksiz EEG '
                                             'ile zaman kaybedildi.',
                          'teaching_point': 'Ani koordinasyon bozukluklarında primer patoloji beyinciktedir; EEG '
                                            'epileptik olmayan fokal serebellar sendromları aydınlatamaz ve '
                                            'görüntülemenin yerini tutamaz.'},
                         {'text': 'Kranial görüntüleme tetkiki istemeden doğrudan acil lomber ponksiyon yaparak BOS '
                                  'basıncını ölçmek ve hücresel artışı mikroskopta incelemek',
                          'is_correct': False,
                          'scenario_update': 'Görüntüleme yapılmadan lomber ponksiyon planlanması, dışlanmamış olası '
                                             'posterior fossa kitlelerinde ölümcül serebellar tonsiller herniasyon '
                                             'riski doğurur.',
                          'teaching_point': 'Yeni gelişen fokal serebellar bulgularda kafa içi kitle ekarte edilmeden '
                                            'lomber ponksiyon yapılması tonsiller herniasyon (foramen magnum '
                                            'fıtıklaşması) riski taşır.'},
                         {'text': 'Yalnızca tam idrar tahlili ve dışkı mikroskopisi göndermek, santral görüntüleme '
                                  'planlamadan olası paraziter enfeksiyon tedavisi ampirik başlamak',
                          'is_correct': False,
                          'scenario_update': 'İdrar ve gaita testleri temiz geldi; santral sinir sistemi görüntülemesi '
                                             'yapılmadığı için intrakraniyal lezyon şüphesi aydınlatılamadı.',
                          'teaching_point': 'Ani başlangıçlı yürüyüş ve hedefi tutturma bozuklukları primer '
                                            'intrakraniyal acil patolojilerle ilişkilidir; rutin idrar ve gaita '
                                            'testleri hedef dışıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'Geçirilmiş viral döküntü sonrası gelişen, görüntülemede kitle saptanmayan ani koordinasyon '
                         'bozukluğunda öncelikli klinik tanınız nedir?',
             'options': [{'text': 'Posterior Fossa Medulloblastomu',
                          'is_correct': False,
                          'scenario_update': 'Medulloblastom genellikle sinsi ilerleyen kafa içi basınç artışı (sabah '
                                             "baş ağrısı, fışkırır kusma) yapar ve MRG'de dördüncü ventrikülü dolduran "
                                             'solid kitle olarak izlenir.',
                          'teaching_point': "Beyin MRG'de kitle, ventrikül basısı ve hidrosefali bulunmaması primer "
                                            'arka çukur tümörlerini kesin olarak dışlar.'},
                         {'text': 'Akut Vestibüler Nörit',
                          'is_correct': False,
                          'scenario_update': 'Vestibüler nöritte şiddetli vertigo, bulantı ve kusma ön plandadır; '
                                             'ancak ekstremitelerde belirgin dismetri, intansiyonel tremor ve '
                                             'disdiadokokinez görülmez.',
                          'teaching_point': 'Periferik vestibüler hastalıklarda intansiyonel tremor, dismetri ve '
                                            'disdiadokokinez gibi serebellar hemisfer disfonksiyonu bulguları '
                                            'bulunmaz.'},
                         {'text': 'Akut Fenitoin Toksisitesi',
                          'is_correct': False,
                          'scenario_update': 'Fenitoin toksisitesi benzer nörolojik bulgular yapabilir ancak bilinen '
                                             'antiepileptik kullanımı veya kazara ilaç maruziyeti öyküsü yoktur.',
                          'teaching_point': 'İlaç intoksikasyonlarında maruziyet öyküsü ve sıklıkla bilinç değişikliği '
                                            'eşlik eder; viral enfeksiyon sonrası izole bulgular post-enfeksiyöz '
                                            'süreci destekler.'},
                         {'text': 'Post-enfeksiyöz Akut Serebellar Ataksi',
                          'is_correct': True,
                          'explanation': 'Çocukluk çağında geçirilmiş viral ekzantem sonrası aniden ortaya çıkan '
                                         'dismetri, nistagmus ve geniş tabanlı yürüyüş kitle ekarte edildiğinde '
                                         'post-enfeksiyöz akut serebellar ataksi tanısını koydurur.',
                          'new_finding': 'Kesin Tanı: Post-enfeksiyöz Akut Serebellar Ataksi (Akut Serebellit). Kitle, '
                                         'kanama ve intoksikasyon dışlandı, selim seyir öngörüldü.'}]},
            {'stage_title': 'İzlem ve Destek Tedavisi Stratejisi',
             'question': 'Akut post-enfeksiyöz serebellar ataksi tanısı alan ve genel durumu stabil olan 4 yaşındaki '
                         'çocuğun en uygun yönetim planı ne olmalıdır?',
             'options': [{'text': 'Serebellar hasarı durdurmak amacıyla derhal yüksek doz intravenöz metilprednizolon '
                                  've eş zamanlı terapötik plazmaferez seansları uygulamaya koymak',
                          'is_correct': False,
                          'scenario_update': 'Gereksiz immünsüpresif tedavi uygulanan çocukta hipertansiyon, '
                                             'hiperglisemi ve immünsüpresyona bağlı sekonder bakteriyel enfeksiyon '
                                             'tablosu gelişti.',
                          'teaching_point': 'Post-enfeksiyöz akut serebellar ataksi selim seyirlidir; rutin '
                                            'kortikosteroid veya plazmaferez gerekmez, bu tedaviler yalnızca fulminan '
                                            'ensefalopatik olgularda düşünülür.'},
                         {'text': 'Servise yatırarak düşme önlemleri almak, destek tedavisi vermek ve aileyi '
                                  'bilgilendirerek spontan klinik iyileşmeyi izlemek',
                          'is_correct': True,
                          'explanation': "Post-enfeksiyöz akut serebellar ataksi olgularının %80-90'ı 2-8 hafta içinde "
                                         'kendiliğinden sekelsiz iyileşir; yönetimde en kritik nokta düşme ve kafa '
                                         'travması önlemleridir.',
                          'new_finding': 'Hasta çocuk servisine yatırıldı. Yatak kenarlıkları kaldırıldı, yumuşak '
                                         'zemin oluşturuldu, düşme önlemleri alındı ve hidrasyon sağlandı. Aileye '
                                         'hastalığın kendini sınırlayan selim doğası anlatıldı. Takiplerinde nörolojik '
                                         'kötüleşme olmadı, 2. haftada yürümesi belirgin düzeldi ve 6. haftada tamamen '
                                         'sekelsiz iyileşti.'},
                         {'text': 'Kalıcı nörolojik hasarı engellemek amacıyla acil cerrahi posterior fossa '
                                  'dekompresyonu ve ventriküloperitoneal şant yerleştirme ameliyatı planlamak',
                          'is_correct': False,
                          'scenario_update': 'Kitle veya obstrüktif hidrosefali bulunmayan hastaya cerrahi girişim '
                                             'yapılması menenjit, BOS kaçağı ve kalıcı morbiditeye yol açtı.',
                          'teaching_point': 'Akut serebellar atakside intrakraniyal kitle veya obstrüktif hidrosefali '
                                            'yoktur; cerrahi dekompresyon veya şant uygulaması kesinlikle endike '
                                            'değildir.'},
                         {'text': 'Hastanede yatışa gerek olmadığını belirterek hemen taburcu etmek ve yürüyemeyen '
                                  'çocuğu evde hiçbir tedbir almadan desteksiz bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Evde tedbirsiz bırakılan dengesiz çocuk ayağa kalkmaya çalışırken '
                                             'merdivenden düşerek travmatik kafa içi kanama tablosuyla acile döndü.',
                          'teaching_point': 'Akut dönemde çocuklar ciddi düşme ve travma riski altındadır; bu nedenle '
                                            'düşme önlemleri alınarak güvenli ortamda ve yakın gözlemle takip '
                                            'edilmelidirler.'}]}]},
 {'id': 'S38',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '2 Yaş (12 kg)',
  'gender': 'Erkek',
  'complaint': 'Evde annesinin şeker kaplı kırmızı kan ilaçlarından çok sayıda yutma sonrası şiddetli karın ağrısı ve '
               'kanlı kahve telvesi kusma',
  'history': "2 yaşındaki (12 kg) erkek çocuk annesi tarafından Sarı Alana getiriliyor: 'Yaklaşık bir saat önce yatak "
             'odasında çekmecede duran kırmızı kaplı kan hapı kutusunu elinde boşalmış buldum; kutuda en az 15-20 '
             'tablet vardı, hepsini çiğneyip yutmuş. Yarım saat sonra çok şiddetli karın ağrısıyla ağlamaya başladı, '
             "ardı ardına kahve telvesi gibi siyahımsı ve kanlı kustu. Çok halsizleşti, baygın gibi bakıyor.'",
  'final_diagnosis': 'Akut Şiddetli Demir İntoksikasyonu (Hap Toksisitesi ve Hemorajik Gastroenterit)',
  'disposition': 'Sarı Alanda Acil İV Sıvı Resüsitasyonu + İntravenöz Deferoksamin Şelasyon İnfüzyonu + Çocuk Yoğun '
                 'Bakım Ünitesine Yatış',
  'case_pearl': 'Akut demir zehirlenmesi pediatrik toksikolojideki en ölümcül maruziyetlerden biridir. Elementer demir '
                'dozu hesaplanmalıdır (örneğin demir sülfat %20 elementer demir içerir; 65 mg elementer demir/tablet x '
                '15-20 tablet = 975-1300 mg -> 12 kg çocukta >80-100 mg/kg elementer demir; >60 mg/kg potansiyel '
                'olarak öldürücüdür). Demir gastrointestinal mukozaya doğrudan koroziftir (evre 1: hematemez, melena, '
                'karın ağrısı), ardından yalancı iyileşme (evre 2), mitokondriyal elektron taşıma zinciri '
                'inhibisyonuna bağlı derin laktik asidoz, şok ve çoklu organ yetmezliği (evre 3), fulminan karaciğer '
                "yetmezliği (evre 4) ve geç pilorik stenoz/skar (evre 5) gelişebilir. Demir radyoopaktır, ADBG'de "
                'midede radyoopak tablet kümeleri görülebilir. Aktif kömür demiri BAĞLAMAZ. Şelasyon tedavisi '
                'endikasyonları: serum demiri >500 mcg/dL, ağır klinik semptomlar (hematemez, laktik asidoz, şok) veya '
                'grafide çok sayıda radyoopak tablet bulunmasıdır. Antidotu İV DEFEROKSAMİNDİR (15 mg/kg/saat sürekli '
                'infüzyon; ferrioksamin kompleksine bağlı vin rosé / pembe idrar rengi izlenir).',
  'steps': [{'stage_title': 'Sarı Alanda İlk Değerlendirme ve Dekontaminasyon Yaklaşımı',
             'question': 'Yüksek miktarda kan yapıcı kırmızı tablet yutan ve hematemezi olan 12 kg çocukta ilk acil '
                         'stabilizasyon yaklaşımınız ne olmalıdır?',
             'options': [{'text': 'Toksinin gastrointestinal emilimini engellemek amacıyla derhal standart bir gram '
                                  'bölü kilogram dozunda oral aktif kömür süspansiyonu içirmek',
                          'is_correct': False,
                          'scenario_update': 'Aktif kömür verilen çocukta kusma şiddetlendi, kömürlü mide içeriği '
                                             'aspire edildi ve endoskopik değerlendirme imkansız hale geldi.',
                          'teaching_point': 'Ağır metaller, demir, lityum ve alkoller aktif kömüre bağlanmaz; korozif '
                                            'mukozal hasarı olan hematemezli hastalarda aktif kömür kesinlikle '
                                            'önerilmez.'},
                         {'text': 'Midedeki toksik tabletleri zorla boşaltmak amacıyla tuzlu su veya ipeka şurubu '
                                  'içirerek çocuğu yatak başında kusturmaya çalışmak',
                          'is_correct': False,
                          'scenario_update': 'Kusturma çabası sırasında hematemez şiddetlendi, özofagus mukozasında '
                                             'laserasyon ve hava yoluna kanlı içerik aspirasyonu meydana geldi.',
                          'teaching_point': 'Korozif gastrointestinal hasara yol açan metal maruziyetlerinde mekanik '
                                            'veya kimyasal kusturma işlemleri aspirasyon ve perforasyon riski '
                                            'nedeniyle kesinlikle kontrendikedir.'},
                         {'text': 'Çocuğun bilincini açık bularak hiçbir damar yolu açmadan sadece oral antiasit şurup '
                                  'içirmek ve evde gözleme bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Eve gönderilmek istenen çocukta hipovolemik şok, bilinç kaybı ve '
                                             'şiddetli gastrointestinal kanamaya bağlı kardiyovasküler kollaps '
                                             'gelişti.',
                          'teaching_point': 'Yüksek doz toksik mineral alımlarında erken evredeki gastrointestinal '
                                            'kanama hızla hipovolemik şoka ilerler; acil damar yolu ve sıvı '
                                            'resüsitasyonu zorunludur.'},
                         {'text': 'Damar yolu açarak izotonik kristaloid infüzyonu başlamak, vital bulguları '
                                  'monitörize etmek ve gastrointestinal kanamayı acilen stabilize etmek',
                          'is_correct': True,
                          'explanation': 'Aşındırıcı gastrointestinal kanamaya yol açan toksik alımlarda hipovolemiyi '
                                         'önlemek için damar yolu açılmalı, izotonik sıvı başlanmalı ve hemodinami '
                                         'yakından monitörize edilmelidir.',
                          'new_finding': 'Vital Bulgular: KTA 152/dk (taşikardik), SS 32/dk, TA 82/46 mmHg (düşük), '
                                         'SpO2 %96, KDZ 3.5 saniye, halsiz ve letarjik görünümde. Fizik Muayene: Cilt '
                                         'soluk, batında yaygın hassasiyet ve defans benzeri istemli kasılma var. '
                                         'Nazogastrik tüpten kahve telvesi ve taze kanlı sıvı drene oldu. 20 mL/kg '
                                         'izotonik kristaloid bolusu başlandı.'}]},
            {'stage_title': 'Radyolojik ve Biyokimyasal Toksisite Taraması',
             'question': 'Yaklaşık 15-20 adet kan yapıcı draje yutan bu hastada toksisite şiddetini ve mide yükünü '
                         'belirlemede en öncelikli tetkikler hangileridir?',
             'options': [{'text': 'Yalnızca idrarda toksik madde taraması ve gaita tahlili isteyerek acil radyolojik '
                                  'görüntüleme çekilmesini bütünüyle lüzumsuz bularak ertelemek',
                          'is_correct': False,
                          'scenario_update': 'İdrar taraması ağır metalleri göstermedi; mide içindeki çözünmemiş '
                                             'toksik tablet kitlesi ve sistemik toksisite şiddeti tespit edilemedi.',
                          'teaching_point': 'Standart idrar uyuşturucu panelleri metalik toksinleri saptamaz; tanı '
                                            'için kantitatif serum düzeyi ve midedeki radyoopak yükün grafisi '
                                            'şarttır.'},
                         {'text': 'Ayakta direkt batın grafisi çekerek radyoopak tabletleri aramak ve kantitatif '
                                  'dördüncü saat serum demir konsantrasyonu göndermek',
                          'is_correct': True,
                          'explanation': "Bu mineral molekülleri radyoopak olduğundan ADBG'de net izlenir; toksisite "
                                         'derecesi ve şelasyon kararı alımdan sonraki serum konsantrasyonuyla '
                                         'belirlenir.',
                          'new_finding': 'Ayakta Direkt Batın Grafisi (ADBG): Mide projeksiyonunda ve proksimal '
                                         'duodenumda çok sayıda kümeleşmiş radyoopak (beyaz dansiteli) tablet görünümü '
                                         'saptandı, serbest hava izlenmedi. Laboratuvar Bulguları: Serum demir düzeyi: '
                                         '650 mcg/dL (ağır toksik sınır, normal: 50-120 mcg/dL), total demir bağlama '
                                         'kapasitesi aşılmış. Kan Gazı: pH 7.22, pCO2 28 mmHg, HCO3 12 mmol/L, Laktat '
                                         '5.8 mmol/L (derin anyon açıklı metabolik laktik asidoz). Hemogram: Lökositoz '
                                         '(WBC 21.400/mm³), Hb 10.2 g/dL, Trombosit 340.000/mm³.'},
                         {'text': 'Mide perforasyonunu ekarte etmek amacıyla sadece baryumlu kontrastlı '
                                  'gastrointestinal pasaj grafisi çekerek bağırsak pasaj süresini detaylıca incelemek',
                          'is_correct': False,
                          'scenario_update': 'Hematemezi ve mukozal hasarı olan hastaya baryum verilmesi kusmayı '
                                             'şiddetlendirdi, peritonit ve mediastinit riskini kritik biçimde '
                                             'yükseltti.',
                          'teaching_point': 'Akut korozif mukozal hasarda ve kanamada baryumlu kontrastlı incelemeler '
                                            'perforasyon riski ve şelasyonu engellemesi nedeniyle kesinlikle '
                                            'kontrendikedir.'},
                         {'text': 'Hiçbir kan tahlili almadan acil batın bilgisayarlı tomografisi çekmek ve verilen '
                                  'kontrast maddenin böbreklerden atılımını yatakta beklemek',
                          'is_correct': False,
                          'scenario_update': 'İntravenöz kontrast madde hipovolemik ve asidotik çocukta akut tübüler '
                                             'nekroz ve anürik böbrek yetmezliğini tetikledi.',
                          'teaching_point': 'Akut metal toksisitesinde ilk basamak basit direkt grafi ve serum '
                                            'düzeyidir; kontrastlı BT gereksiz radyasyon ve nefrotoksisite riski '
                                            'taşır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': "Yüksek miktarda kan ilacı yutma öyküsü, hematemez, ADBG'de radyoopak tabletler ve serum "
                         'düzeyi 650 mcg/dL olan hastada kesin tanınız nedir?',
             'options': [{'text': 'Akut Kurşun Ensefalopatisi Toksisitesi',
                          'is_correct': False,
                          'scenario_update': 'Kurşun zehirlenmesi kronik maruziyetle ensefalopati, anemi ve nöropati '
                                             "yapar; akut hematemez ve ADBG'de radyoopak mide tabletleri oluşturmaz.",
                          'teaching_point': 'Kurşun toksisitesi akut masif hematemez ve erken laktik asidoz tablosuyla '
                                            'seyretmez; demir spesifik gastrointestinal ve hücresel toksisiteye yol '
                                            'açar.'},
                         {'text': 'Akut Kostik Madde Alımı',
                          'is_correct': False,
                          'scenario_update': 'Kostik madde alımlarında orofarenkste yanıklar ve salya akması ön '
                                             'plandadır; kanda anyon açıklı laktik asidoz ve radyoopak tabletler '
                                             'görülmez.',
                          'teaching_point': 'Kostik alımlarda orofarengeal mukozal lezyonlar baskındır ve radyografide '
                                            'radyoopak tablet kümeleri izlenmez.'},
                         {'text': 'Akut Şiddetli Demir Zehirlenmesi',
                          'is_correct': True,
                          'explanation': "Yüksek doz alım (>60 mg/kg), hematemez, ADBG'de radyoopak tablet kümeleri, "
                                         '>500 mcg/dL serum düzeyi ve laktik asidoz kesin şiddetli demir '
                                         'intoksikasyonudur.',
                          'new_finding': 'Kesin Tanı: Akut Şiddetli Demir Zehirlenmesi (Hemorajik Korozif Evre). Mide '
                                         'yükü yüksek ve serum düzeyi şelasyon endikasyon sınırını aşmıştır.'},
                         {'text': 'Kanama Diyatezi ve Trombositopeni',
                          'is_correct': False,
                          'scenario_update': 'Kanama diyatezinde trombositopeni veya koagülopati saptanır; '
                                             'radyografide radyoopak tabletler ve yüksek demir konsantrasyonu '
                                             'açıklanamaz.',
                          'teaching_point': 'Hemogramda trombosit sayısı ve pıhtılaşma testleri başlangıçta normaldir; '
                                            'hematemezin nedeni primer hemostaz kusuru değil direkt toksik '
                                            'erozyondur.'}]},
            {'stage_title': 'Acil Şelasyon Tedavisi ve Yoğun Bakım Yönetimi',
             'question': 'Serum düzeyi 650 mcg/dL olan ve laktik asidozu bulunan 12 kg çocukta en uygun antidot '
                         'tedavisi ve yatış yaklaşımı nedir?',
             'options': [{'text': 'Çocuk Yoğun Bakıma yatırarak intravenöz deferoksamin infüzyonu başlamak, '
                                  'hemodinami, idrar rengi ve asidoz tablosunu yakından izlemek',
                          'is_correct': True,
                          'explanation': 'Serum düzeyi >500 mcg/dL, sistemik semptom ve laktik asidoz varlığında '
                                         'spesifik şelatör İV deferoksamindir (15 mg/kg/saat infüzyon, vin rosé idrar '
                                         'takibi).',
                          'new_finding': 'Hasta Çocuk Yoğun Bakım Ünitesine yatırıldı. İntravenöz deferoksamin '
                                         'infüzyonu 15 mg/kg/saat dozunda başlandı. İdrarın karakteristik vin rosé '
                                         '(pembe-kızıl) renk aldığı gözlendi. Sıvı resüsitasyonuyla hemodinamik '
                                         'stabilite sağlandı, 24. saatte serum demir düzeyi 140 mcg/dL düzeyine '
                                         'geriledi ve metabolik asidoz tamamen düzeldi.'},
                         {'text': 'Oral penisilamin kapsül reçete ederek hastayı çocuk servisine yatırmak ve idrar '
                                  'rengini takip etmeden spontan atılımı beklemek',
                          'is_correct': False,
                          'scenario_update': 'Penisilamin demiri bağlamada etkisizdir; şelasyon yapılmayan çocukta '
                                             'mitokondriyal hasar ilerleyerek fulminan karaciğer yetmezliği ve '
                                             'kardiyotoksisite gelişti.',
                          'teaching_point': 'Akut demir zehirlenmesinde penisilamin veya dimerkaprol (BAL) etkisizdir; '
                                            'tek spesifik ve hayat kurtarıcı şelatör intravenöz deferoksamindir.'},
                         {'text': 'Yalnızca yüksek doz oral C vitamini vererek gastrointestinal emilimi nötralize '
                                  'etmeye çalışmak ve antidot vermeden gözlemlemek',
                          'is_correct': False,
                          'scenario_update': 'C vitamini demirin ferrik formdan ferröz forma dönüşümünü artırarak '
                                             'serbest radikal hasarını ve miyokardiyal toksisiteyi daha da '
                                             'ölümcülleştirdi.',
                          'teaching_point': 'Akut fazda askorbik asit (C vitamini) verilmesi serbest demir '
                                            'toksisitesini ve fatal aritmileri artırabileceğinden akut dönemde '
                                            'kesinlikle kontrendikedir.'},
                         {'text': 'Midedeki tabletlerin doğal yolla atılmasını beklemek amacıyla laksatif şurup içirip '
                                  'hastayı ayaktan eve taburcu etmek',
                          'is_correct': False,
                          'scenario_update': 'Taburcu edilen çocukta alımdan 8 saat sonra evde derin koma, kontrolsüz '
                                             'koagülopati ve irreversibl kardiyovasküler kollaps gelişti.',
                          'teaching_point': "Serum düzeyi 500 mcg/dL'yi aşan ve asidozu olan demir intoksikasyonları "
                                            "yoğun bakımda agresif parenteral şelasyon yapılmazsa %50'ye varan "
                                            'mortalite taşır.'}]}]},
 {'id': 'S39',
  'category': '⚡ Alerji, Zehirlenme & Diğer Aciller',
  'age': '3 Yaş (14 kg)',
  'gender': 'Kız',
  'complaint': 'Evde açıkta bırakılan reçeteli antidepresan kutusundan tablet yutma sonrası uykuya meyil, yüzde '
               'kızarıklık, ağız kuruluğu ve çarpıntı',
  'history': "3 yaşındaki (14 kg) kız çocuğun babası panikle Sarı Alana başvuruyor: 'Yaklaşık bir saat önce evde sehpa "
             'üzerinde duran annesine ait kırmızı renkli depresyon hapı kutusundaki tabletleri eksilmiş bulduk; en az '
             '6-8 tablet yutmuş olabilir. Çocuğun göz bebekleri kocaman oldu, cildi kuruyup alev gibi kızardı, kalbi '
             "göğsünden fırlayacak gibi hızlı çarpıyor ve sürekli sayıklayarak uyukluyor.'",
  'final_diagnosis': 'Trisiklik Antidepresan (TKA / Amitriptilin) Zehirlenmesi ve Akut Kardiyotoksisitesi',
  'disposition': 'Sarı Alanda Acil EKG + İV Sodyum Bikarbonat Bolusu (1-2 mEq/kg) + Çocuk Yoğun Bakım Ünitesine Yatış '
                 've Sürekli Kardiyak Monitörizasyon',
  'case_pearl': 'Trisiklik antidepresanlar (TKA - örn. amitriptilin, imipramin), kardiyak voltaj bağımlı hızlı sodyum '
                'kanallarını bloke ederek, periferik alfa-1 adrenerjik reseptörleri antagonize ederek ve '
                'merkezi/periferik muskarinik asetilkolin reseptörlerini baskılayarak çoklu toksisiteye yol açar. '
                'Antikolinerjik toksidrom bulguları: midriyazis, kuru sıcak eritemli cilt, mukozal kuruluk, taşikardi, '
                'bağırsak seslerinde azalma ve üriner retansiyondur. En ölümcül etkisi miyokardiyal sodyum kanal '
                'blokajına bağlı intraventriküler ileti gecikmesi ve malign ventriküler aritmilerdir (VT/VF, torsades '
                "de pointes). 12 derivasyonlu EKG'de QRS >100 ms olması konvülziyon riskini, >160 ms olması "
                'ventriküler aritmi riskini gösterir; aVR derivasyonunda terminal R dalgası yüksekliği (R >3 mm veya '
                'R/S >0.7) TKA kardiyotoksisitesinin patognomonik belirtecidir. Birinci basamak hayat kurtarıcı tedavi '
                'İNTRAVENÖZ SODYUM BİKARBONATTIR (1-2 mEq/kg İV bolus; hedef kan pH 7.45-7.55, serum sodyumu 150-155 '
                'mEq/L). Sodyum yükü kompetitif blokajı çözer, alkaloza kayma ilacın reseptörden ayrılmasını '
                'hızlandırır. Sınıf 1A ve 1C antiaritmikler ile fizostigmin KONTRENDİKEDİR (asistoliye yol açabilir).',
  'steps': [{'stage_title': 'Sarı Alanda Antikolinerjik Toksidrom ve Kardiyak Güvenlik',
             'question': 'Açıkta kalan reçeteli antidepresan tabletlerinden yutan, letarjik ve taşikardik olan 14 kg '
                         'çocukta ilk acil yaklaşım ne olmalıdır?',
             'options': [{'text': 'Hava yolunu güvenceye almak, damar yolu açarak kardiyak monitörizasyon başlatmak ve '
                                  'vital parametreleri acilen değerlendirmek',
                          'is_correct': True,
                          'explanation': 'Bilinç baskılanması ve kardiyotoksisite riski taşıyan antidepresan '
                                         'alımlarında acil hava yolu kontrolü, damar yolu ve sürekli kardiyak '
                                         'monitörizasyon esastır.',
                          'new_finding': 'Vital Bulgular: KTA 154/dk (sinüs taşikardisi), SS 24/dk, TA 86/52 mmHg, '
                                         'SpO2 %98, Ateş 37.8°C, GKS 12. Fizik Muayene: Cilt kuru, sıcak ve yaygın '
                                         'flushed (kırmızı); ağız mukozası kupkuru; pupiller bilateral 6 mm midriyatik '
                                         've ışık refleksi tembel. Batında bağırsak sesleri hipoaktif, mesane glob '
                                         'vezikale formunda palpe ediliyor.'},
                         {'text': 'Bilinç bulanıklığı olan çocuğa derhal ağızdan tuzlu su içirerek kusturmaya çalışmak '
                                  've ardından ev gözlemine göndermek',
                          'is_correct': False,
                          'scenario_update': 'Zorla kusturulan çocukta letarji derinleşti, mide içeriği hava yoluna '
                                             'kaçarak akut aspirasyon pnömonisi ve hipoksi tablosu gelişti.',
                          'teaching_point': 'Bilinci baskılanmış ve kardiyotoksik ilaç almış hastalarda kusturma '
                                            'işlemi hava yolu koruyucu refleksleri zayıfladığı için kesinlikle '
                                            'kontrendikedir.'},
                         {'text': 'Taşikardiyi düşürmek amacıyla hemen intravenöz kısa etkili beta bloker esmolol puşe '
                                  'etmek ve EKG çekimini ertelemek',
                          'is_correct': False,
                          'scenario_update': 'Beta bloker uygulanan hastada miyokardiyal kontraktilite aniden çöktü, '
                                             'şiddetli hipotansiyon ve derin bradikardik kardiyovasküler kollaps '
                                             'meydana geldi.',
                          'teaching_point': 'Toksik taşikardilerde EKG ile ileti anomalileri aydınlatılmadan beta '
                                            'bloker verilmesi kardiyojenik şok ve ölümcül bradiaritmilere yol '
                                            'açabilir.'},
                         {'text': 'Hastanın ajitasyonunu yatıştırmak amacıyla yüksek doz santral etkili intramusküler '
                                  'klorpromazin enjekte ederek serviste tek başına bırakmak',
                          'is_correct': False,
                          'scenario_update': 'Fenotiyazin verilen çocukta ek antikolinerjik ve sodyum kanal blokajı '
                                             'etkisiyle derin koma ve genel tonik klonik nöbet tetiklendi.',
                          'teaching_point': 'Antipsikotikler antikolinerjik yükü artırır, nöbet eşiğini düşürür ve '
                                            'kardiyotoksisiteyi derinleştirir; bu olgularda kesinlikle '
                                            'kullanılmamalıdır.'}]},
            {'stage_title': 'Kardiyak İleti Analizi ve 12 Derivasyonlu Elektrokardiyografi',
             'question': 'Bilinç değişikliği, belirgin taşikardi ve antikolinerjik bulguları olan bu çocukta '
                         'kardiyotoksisiteyi saptamak için en kritik tetkik adımı nedir?',
             'options': [{'text': 'Yalnızca rutin serum elektrolitleri ve kalsiyum düzeyi göndererek kardiyak '
                                  'elektrofizyolojik ritim analizi yapmadan servis yatağında beklemek',
                          'is_correct': False,
                          'scenario_update': 'Elektrolit sonuçları çıkana kadar EKG çekilmediği için ilerleyen '
                                             'intraventriküler ileti gecikmesi fark edilemedi ve hasta ventriküler '
                                             'fibrilasyona girdi.',
                          'teaching_point': 'Kardiyotoksik ilaç alımlarında en acil ve hayat kurtarıcı tanısal tetkik '
                                            "12 derivasyonlu EKG'dir; biyokimya sonuçları beklenerek zaman "
                                            'kaybedilemez.'},
                         {'text': 'Ritim bozukluğunu değerlendirmek için sadece yirmi dört saatlik ritim Holter cihazı '
                                  'takarak hastayı acilden poliklinik kontrolüne yönlendirmek',
                          'is_correct': False,
                          'scenario_update': 'Acil serviste EKG çekilmeden taburcu edilen çocuk yolda malign '
                                             'polimorfik ventriküler taşikardi ve kardiyak arrest geliştirdi.',
                          'teaching_point': 'Akut taşikardik zehirlenmelerde ambulatuvar Holter değil, anlık 12 '
                                            'derivasyonlu acil EKG çekilmeli ve sodyum kanal blokajı hemen '
                                            'saptanmalıdır.'},
                         {'text': "Acilen on iki derivasyonlu elektrokardiyografi çekerek QRS süresini ve aVR'deki "
                                  'terminal R dalgasını analiz etmek',
                          'image': 'assets/images/ecg_tca.png',
                          'image_caption': 'EKG: QRS süresinde genişleme (>100 ms) ve aVR derivasyonunda terminal '
                                           'belirgin R dalgası (>3 mm)',
                          'is_correct': True,
                          'explanation': 'Miyokardiyal sodyum kanalı blokajı QRS genişlemesine (>100 ms) ve aVR '
                                         'derivasyonunda karakteristik yüksek terminal R dalgasına (>3 mm) yol açar.',
                          'new_finding': '12 Derivasyonlu EKG Analizi: Sinüs taşikardisi (KTA 152/dk), QRS süresi 124 '
                                         'ms (belirgin genişleme, >100 ms), QT/QTc aralığı 490 ms (uzamış). aVR '
                                         'derivasyonunda terminal R dalgası yüksekliği 4.2 mm (patolojik >3 mm) ve R/S '
                                         'oranı 1.1 (>0.7). Kan Gazı: pH 7.31, pCO2 38 mmHg, HCO3 19 mmol/L, Laktat '
                                         '2.8 mmol/L. Serum glukozu 108 mg/dL, elektrolitler: Na 137 mEq/L, K 4.1 '
                                         'mEq/L.'},
                         {'text': 'Sadece transtorasik ekokardiyografi ile sol ventrikül ejeksiyon fraksiyonunu ölçmek '
                                  've elektrokardiyografik ileti aralıklarını incelemeyi tamamen ihmal etmek',
                          'is_correct': False,
                          'scenario_update': 'Ekokardiyografi ile ventrikül ileti gecikmesi ve malign aritmi riski '
                                             'değerlendirilemedi; hastada ani QRS genişlemesi ve asistoli gelişti.',
                          'teaching_point': 'Ekokardiyografi elektriksel ileti bloklarını göstermez; akut '
                                            'kardiyotoksisitenin derecesi ve nöbet/aritmi riski yalnızca 12 '
                                            'derivasyonlu EKG ile izlenir.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': "Antikolinerjik bulgular, letarji, EKG'de QRS >100 ms ve aVR'de belirgin R dalgası saptanan "
                         'hastada öncelikli kesin tanınız nedir?',
             'options': [{'text': 'Akut Selektif Serotonin Geri Alım Toksisitesi',
                          'is_correct': False,
                          'scenario_update': 'SSRI zehirlenmesinde tremor, hiperrefleksi, klonus ve terleme görülür; '
                                             "belirgin sodyum kanal blokajı (QRS >100 ms, aVR'de R >3 mm) beklenmez.",
                          'teaching_point': 'SSRI toksisitesi nöromusküler uyarılabilirlik ve klonusla seyreder; '
                                            'klasik QRS genişlemesi ve aVR bulguları TKA kardiyotoksisitesine '
                                            'özgüdür.'},
                         {'text': 'Trisiklik Antidepresan Kardiyotoksisitesi Zehirlenmesi',
                          'is_correct': True,
                          'explanation': "Antikolinerjik toksidrom bulguları ile birlikte EKG'de QRS genişlemesi (>100 "
                                         "ms) ve aVR'de patolojik terminal R dalgası (>3 mm) tipik TKA "
                                         'kardiyotoksisitesidir.',
                          'new_finding': 'Kesin Tanı: Trisiklik Antidepresan (Amitriptilin) Zehirlenmesi ve Akut '
                                         'Kardiyotoksisitesi. QRS >100 ms olduğu için malign aritmi ve nöbet riski '
                                         'yüksektir.'},
                         {'text': 'Atropin ve Belladon Alkaloidi İntoksikasyonu',
                          'is_correct': False,
                          'scenario_update': 'Atropin izole periferik/santral antikolinerjik bulgular yapar ancak '
                                             'ventriküler kardiyak sodyum kanallarını bloke ederek QRS genişletmez.',
                          'teaching_point': "Atropin sinüs taşikardisi ve midriyazis yapsa da aVR'de patolojik "
                                            'terminal R dalgası ve QRS süresinde genişleme (sodyum kanal blokajı) '
                                            'yapmaz.'},
                         {'text': 'Akut Organofosfat İntoksikasyonu Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Organofosfat zehirlenmesinde kolinerjik kriz (miyozis, aşırı bronkore, '
                                             'bronkospazm, bradikardi, aşırı tükürük ve ishal) görülür; kuru cilt ve '
                                             'midriyazis olmaz.',
                          'teaching_point': 'Organofosfatlar kolinerjik fazlalık yaparak ıslak sekresyonlara yol açar; '
                                            'bu hastada kuru sıcak cilt ve midriyazis ile antikolinerjik toksidrom '
                                            'vardır.'}]},
            {'stage_title': 'Spesifik Tedavi ve Kardiyovasküler Stabilizasyon',
             'question': "EKG'de QRS süresi 124 ms ve aVR terminal R dalgası 4.2 mm olan bu hastada derhal uygulanması "
                         'gereken spesifik antidot tedavisi nedir?',
             'options': [{'text': 'Antikolinerjik bulguları tersine çevirmek amacıyla derhal bir miligram intravenöz '
                                  'fizostigmin puşe ederek kardiyak ritim yanıtını monitörden beklemek',
                          'is_correct': False,
                          'scenario_update': 'Fizostigmin uygulanan hastada ileti gecikmesi derinleşti, tam '
                                             'atriyoventriküler blok ve dirençli asistolik kardiyak arrest gelişti.',
                          'teaching_point': 'TKA zehirlenmelerinde fizostigmin uygulanması asistoli ve refrakter '
                                            'kardiyak arrest riskini dramatik artırdığından kesinlikle '
                                            'kontrendikedir.'},
                         {'text': 'QRS genişlemesini düzeltmek için Sınıf 1A antiaritmik prokainamid veya Sınıf 1C '
                                  'flekainid infüzyonu başlayarak hastayı serviste izlemek',
                          'is_correct': False,
                          'scenario_update': 'Sodyum kanal blokeri antiaritmik alan hastada sodyum kanalları tamamen '
                                             'kilitlendi, ventriküler taşikardi ve irreversibl kardiyovasküler kollaps '
                                             'gelişti.',
                          'teaching_point': 'Sınıf 1A ve 1C antiaritmikler sodyum kanal blokajını daha da '
                                            'şiddetlendirir; TKA kardiyotoksisitesinde kullanımları kesinlikle '
                                            'yasaktır.'},
                         {'text': 'Yalnızca intravenöz magnezyum sülfat infüzyonu başlayıp başka hiçbir sistemik '
                                  'alkalinizasyon ajanı vermeden hastayı genel serviste takip etmek',
                          'is_correct': False,
                          'scenario_update': 'Magnezyum sodyum kanal blokajını çözemedi; QRS süresi 160 ms üzerine '
                                             'çıkarak hastada generalize tonik-klonik konvülziyon gelişti.',
                          'teaching_point': 'Magnezyum Torsades de Pointes tedavisinde yardımcıdır ancak sodyum kanal '
                                            'blokajını ve asidozu düzeltemez; primer birinci basamak tedavi değildir.'},
                         {'text': 'Bir ila iki miliequivalan bölü kilogram intravenöz sodyum bikarbonat bolusu '
                                  'uygulayıp QRS daralmasını elektrokardiyografiyle izlemek',
                          'is_correct': True,
                          'explanation': 'İV sodyum bikarbonat, hem sodyum yükü sağlayarak kanalları açar hem de serum '
                                         "pH'sını yükselterek ilacın kanallardan ayrılmasını sağlar (hedef pH "
                                         '7.45-7.55).',
                          'new_finding': 'Hastaya 1.5 mEq/kg (21 mEq) İV Sodyum Bikarbonat bolus uygulandı. 10 dakika '
                                         "sonra tekrarlanan EKG'de QRS süresi 88 ms'ye daraldı, aVR'deki R dalgası 1.8 "
                                         "mm'ye geriledi. Kan gazında pH 7.48 ölçüldü. Çocuk Yoğun Bakım Ünitesine "
                                         'yatırıldı; sürekli sodyum bikarbonat infüzyonu (hedef pH 7.45-7.55) ve '
                                         'kardiyak monitörizasyon ile takip edildi, sekelsiz toparladı.'}]}]},
 {'id': 'S40',
  'category': '👶 Ağlayan, Emmeyen, Huzursuz Bebek',
  'age': '4 Günlük (3.2 kg)',
  'gender': 'Erkek',
  'complaint': 'Doğumun dördüncü gününde beslenememe, giderek derinleşen uyku hali, kaslarda gevşeklik, hızlı nefes '
               'alıp verme ve kol-bacaklarda sıçrama nöbetleri',
  'history': "Zamanında 3200 gram doğan erkek bebeğin ailesi yaşamın dördüncü gününde Sarı Alana başvuruyor: 'İlk iki "
             'gün anne sütünü iştahla emiyordu, hiçbir sıkıntısı yoktu. Üçüncü günden itibaren giderek emmeyi bıraktı, '
             'uyandıramamaya başladık, vücudu pelte gibi gevşedi. Bugün sabah nefes alıp vermesi çok hızlandı, karnı '
             "şişti ve kollarında, bacaklarında ritmik titreme ve sıçrama kasılmaları başladı.'",
  'final_diagnosis': 'Akut Yenidoğan Hiperamonyemisi ve Üre Döngüsü Bozukluğu (Enzimatik Azot Metabolizması Defekti)',
  'disposition': 'Acil Protein Alımının Kesilmesi + %10 Dekstroz İnfüzyonu + İntravenöz Nitrojen Bağlayıcı Ajanlar + '
                 'Acil Hemodiyaliz Hazırlığı ile Çocuk Yoğun Bakım Yatışı',
  'case_pearl': 'Yenidoğan döneminde ilk günlerde tamamen sağlıklı (semptomsuz) bir aralıktan sonra proteinli '
                'beslenmenin (anne sütü veya formül mama) başlamasıyla ortaya çıkan letarji, beslenememe, hipotoni, '
                'santral hiperventilasyona bağlı respiratuar alkaloz ve konvülziyon aksi kanıtlanana kadar Üre Döngüsü '
                'Bozukluğu (UCD - örn. Ornitin Transkarbamilaz / OTC eksikliği vb.) tablosudur. Katabolizma ve protein '
                'yıkımı sonucu kanda aşırı düzeyde biriken serbest amonyak kan-beyin bariyerini geçerek astrositlerde '
                'glutamin birikimine, serebral ödeme ve ensefalopatiye yol açar. Kilit laboratuvar bulguları: normal '
                'kan şekeri, belirgin metabolik asidoz veya ketonüri olmaksızın solunum merkezinin uyarılmasına bağlı '
                'RESPİRATUAR ALKALOZ (pH >7.45, pCO2 düşük) ve aşırı yüksek plazma amonyak düzeyidir (>150-200 mcmol/L '
                'toksik, >400-500 mcmol/L acil diyaliz endikasyonu). Acil tedavi: 1) Ekzojen protein alımının DERHAL '
                'durdurulması, 2) Katabolizmayı baskılamak için yüksek glukoz infüzyonu (%10 Dekstroz, glukoz infüzyon '
                'hızı 8-10 mg/kg/dk), 3) İntravenöz amonyak bağlayıcı ajanlar (Sodyum benzoat ve sodyum fenilasetat), '
                '4) Düzey >400-500 mcmol/L veya nörolojik kötüleşme varsa vakit kaybetmeden acil hemodiyaliz / sürekli '
                'venö-venöz hemodiyafiltrasyon (CVVHDF).',
  'steps': [{'stage_title': 'Yenidoğanda Ani Bozulma ve İlk Resüsitasyon Yaklaşımı',
             'question': 'İlk iki gün sağlıklı olup protein alımıyla hızla letarji, takipne ve kasılma geliştiren 4 '
                         'günlük bebekte ilk adımınız ne olmalıdır?',
             'options': [{'text': 'Bebekteki derin uyku halini normal yenidoğan yorgunluğu kabul ederek beslenmesini '
                                  'zorlamak ve anne sütü vermeye ısrarla devam ettirmek',
                          'is_correct': False,
                          'scenario_update': 'Anne sütü verilmeye devam edilen bebekte protein yükü arttı; '
                                             'ensefalopati tablosu hızla derinleşerek solunum arresti gelişti.',
                          'teaching_point': 'Semptomsuz aralıktan sonra hızla bozulan yenidoğanda protein alımına '
                                            'devam edilmesi toksik metabolit birikimini ve serebral hasarı katlayarak '
                                            'artırır.'},
                         {'text': 'Sadece intravenöz kalsiyum glukonat infüzyonu yaparak nörolojik bulguların '
                                  'hipokalsemiye bağlı olduğunu varsaymak ve metabolik tetkik planlamamak',
                          'is_correct': False,
                          'scenario_update': 'Kalsiyum infüzyonuna rağmen konvülziyonlar durmadı; derinleşen serebral '
                                             'ödem ve letarji nedeniyle hasta entübe edilmek zorunda kalındı.',
                          'teaching_point': 'Yenidoğan dönemindeki ensefalopati ve nöbetlerde tek bir elektrolite '
                                            'odaklanmak ölümcül doğumsal metabolizma hastalıklarının atlanmasına yol '
                                            'açar.'},
                         {'text': 'Hava yolunu sağlamak, damar yolu açıp vital parametreleri monitörize etmek ve '
                                  'enteral beslenmeyi derhal durdurarak hidrasyon planlamak',
                          'is_correct': True,
                          'explanation': 'Yenidoğanda protein maruziyetiyle aniden gelişen letarji ve nöbetlerde hava '
                                         'yolu emniyete alınmalı, protein girişi acilen kesilmeli ve damar yolu '
                                         'açılmalıdır.',
                          'new_finding': 'Vital Bulgular: KTA 168/dk, SS 68/dk (belirgin takipneik, derin solunum), TA '
                                         '64/38 mmHg, SpO2 %96, Ateş 36.5°C. Fizik Muayene: Ağrılı uyarana yanıt '
                                         "zayıf, ileri derecede letarjik ve hipotonik ('kurbağa pozisyonunda'); emme "
                                         've moro refleksleri alınamadı. Ekstremitelerde multifokal miyoklonik '
                                         'sıçramalar ve bisiklet çevirme benzeri nöbet hareketleri izlendi. Karaciğer '
                                         'kot kavsini 1 cm geçiyor, splenomegali yok.'},
                         {'text': 'Mevcut takipneyi hafif geçici taşipne kabul ederek bebeğe nazal oksijen vermek ve '
                                  'tetkik yapmadan serviste anne yanında izlemek',
                          'is_correct': False,
                          'scenario_update': 'Takipnesi derinleşen bebekte koma hali gelişti; oksijen verilmesine '
                                             'rağmen santral hiperventilasyonun altta yatan metabolik nedeni '
                                             'anlaşılamadı.',
                          'teaching_point': 'Bilinç kaybı ve konvülziyonun eşlik ettiği takipne basit akciğer '
                                            'patolojisi değil, beyin sapının toksik metabolitlerce uyarılmasına bağlı '
                                            'santral hiperventilasyondur.'}]},
            {'stage_title': 'Kritik Metabolik Değerlendirme ve Toksik Katabolit Taraması',
             'question': 'Takipne, letarji ve konvülziyonu olan bu yenidoğanda altta yatan metabolik felaketi ortaya '
                         'koymak için en uygun acil tetkik paneli nedir?',
             'options': [{'text': 'Kan gazı, kan şekeri, idrar ketonu, plazma azotlu toksik atık düzeyleri ve tandem '
                                  'spektrometrisi istemek',
                          'is_correct': True,
                          'explanation': 'Yenidoğanda ketonüri ve hipoglisemi olmaksızın gelişen solunumsal alkaloz '
                                         'tablolarında azot metabolizması yıkım ürünleri ve organik asit paneli acilen '
                                         'analiz edilmelidir.',
                          'new_finding': 'Kan Gazı: pH 7.52, pCO2 24 mmHg, HCO3 19 mmol/L, BE -1.2 mmol/L (santral '
                                         'hiperventilasyona sekonder belirgin respiratuar alkaloz). Kan Şekeri: 90 '
                                         'mg/dL (normal). Tam İdrar Tetkiki: Keton negatif, glukoz negatif. Serum '
                                         'Laktatı: 1.9 mmol/L (normal). Plazma toksik nitrojenöz katabolit düzeyi: 485 '
                                         'mcmol/L (ağır toksik yüksek, normal: <60-80 mcmol/L). Karaciğer ve böbrek '
                                         'fonksiyonları normal. Hemogram: Lökosit 9.200/mm³, CRP 0.8 mg/L (enfeksiyon '
                                         'belirteçleri negatif).'},
                         {'text': 'Yalnızca lomber ponksiyon yaparak BOS kültürünü beklemek, kan gazı ve plazma '
                                  'biyokimyasal metabolit analizlerini lüzumsuz bularak ertelemek',
                          'is_correct': False,
                          'scenario_update': 'BOS incelemesi temiz geldi; metabolik tarama ve azot atık düzeyleri '
                                             'gönderilmediği için ensefalopatinin gerçek nedeni anlaşılamadı ve beyin '
                                             'ödemi gelişti.',
                          'teaching_point': 'Yenidoğanda sepsis benzeri tablolarda enfeksiyon dışlanırken eş zamanlı '
                                            'metabolik acil paneli (kan gazı, kan şekeri, toksik azot metabolitleri) '
                                            'mutlaka çalışılmalıdır.'},
                         {'text': 'Sadece kranial ultrasonografi çekerek intraventriküler kanama aramak ve '
                                  'biyokimyasal acil kan tetkiklerini sonraki günlere bırakarak beklemek',
                          'is_correct': False,
                          'scenario_update': 'Kranial ultrasonda kanama görülmedi; ancak metabolik tetkikler '
                                             'yapılmadığı için geri dönüşsüz nörolojik hasar ve beyin sapı basısı '
                                             'ortaya çıktı.',
                          'teaching_point': 'Görüntüleme kaba yapısal lezyonları gösterir ancak hücresel metabolik '
                                            'krizleri ve toksik metabolit birikimini aydınlatamaz; acil biyokimya '
                                            'paneli ertelenemez.'},
                         {'text': 'Bebeğe hiçbir tahlil yapmadan ampirik antiviral asiklovir başlamak ve kalorisini '
                                  'arttırmak amacıyla ek formül mamayla devam etmek',
                          'is_correct': False,
                          'scenario_update': 'Formül mama verilmesiyle ekzojen protein yükü tavan yaptı; toksik '
                                             'metabolitler hızla katlanarak derin koma ve kardiyovasküler '
                                             'instabiliteye neden oldu.',
                          'teaching_point': 'Doğumsal metabolizma bozukluğundan şüphelenilen yenidoğana protein '
                                            'içerikli mama verilmesi felakete yol açar; kesinlikle protein alımı '
                                            'durdurulmalıdır.'}]},
            {'stage_title': 'Klinik Tanı',
             'question': 'İlk beslenme sonrası letarji, respiratuar alkaloz, normal glukoz, ketonüri yokluğu ve aşırı '
                         'yüksek azot kataboliti saptanan yenidoğanda kesin tanınız nedir?',
             'options': [{'text': 'Yenidoğan Erken Sepsisi ve Menenjit',
                          'is_correct': False,
                          'scenario_update': 'Yenidoğan sepsisi tipik olarak metabolik asidoz, yüksek CRP ve '
                                             'enfeksiyon bulguları ile seyreder; respiratuar alkaloz ve izole aşırı '
                                             'azot yüksekliği yapmaz.',
                          'teaching_point': 'Sepsis klinik olarak benzer görünse de kan gazında derin laktik/metabolik '
                                            'asidoz oluşturur; belirgin respiratuar alkaloz üre döngüsü defektlerini '
                                            'işaret eder.'},
                         {'text': 'Propiyonik Asidemi Akut Metabolik Dekompanzasyonu',
                          'is_correct': False,
                          'scenario_update': 'Organik asidemilerde belirgin anyon açıklı metabolik asidoz, idrarda '
                                             'ağır ketonüri ve sıklıkla hipoglisemi ile nötropeni saptanır.',
                          'teaching_point': 'Organik asidemilerde respiratuar alkaloz değil şiddetli metabolik asidoz '
                                            've idrarda keton görülür; bu hastada keton negatiftir ve alkaloz vardır.'},
                         {'text': 'Hipoksik İskemik Ensefalopati Tablosu',
                          'is_correct': False,
                          'scenario_update': 'Hipoksik iskemik ensefalopati doğum anında asfiksi, düşük Apgar skoru ve '
                                             'ilk saatlerde nörolojik bulgu verir; iki günlük normal aralık olmaz.',
                          'teaching_point': 'HİE doğum anında bulgu verirken, üre döngüsü defektlerinde bebek ilk '
                                            '24-48 saat beslenene kadar tamamen sağlıklı ve semptomsuzdur.'},
                         {'text': 'Akut Hiperamonyemi ve Üre Döngüsü Bozukluğu',
                          'is_correct': True,
                          'explanation': 'Proteinli beslenme sonrası letarji, solunumsal alkaloz (santral '
                                         'hiperventilasyon), normal glukoz, ketonüri yokluğu ve aşırı amonyak '
                                         'yüksekliği üre döngüsü bozukluğunu kanıtlar.',
                          'new_finding': 'Kesin Tanı: Akut Yenidoğan Hiperamonyemisi ve Üre Döngüsü Bozukluğu. Plazma '
                                         'düzeyi 485 mcmol/L (>400 mcmol/L) olup acil diyaliz ve şelatör endikasyonu '
                                         'mevcuttur.'}]},
            {'stage_title': 'Acil Metabolik Yönetim ve Yoğun Bakım Tedavisi',
             'question': 'Plazma düzeyi 485 mcmol/L olan ve nöbet geçiren 3.2 kg yenidoğanda en uygun acil tedavi ve '
                         'yatış protokolü nedir?',
             'options': [{'text': 'Protein alımını azaltarak standart idame serum fizyolojik takmak ve düzeyin '
                                  'kendiliğinden düşmesini beklemek amacıyla yenidoğan servisinde izlemek',
                          'is_correct': False,
                          'scenario_update': 'Dekstroz verilmediği için endojen protein katabolizması sürdü; toksik '
                                             'metabolitler 800 mcmol/L üzerine çıkarak irreversibl beyin hasarı ve '
                                             'herniasyona yol açtı.',
                          'teaching_point': 'Yetersiz kalori endojen kas yıkımını artırır; protein kesilmesinin '
                                            'yanında yüksek glukoz infüzyonu ve azot bağlayıcılar derhal '
                                            'başlanmalıdır.'},
                         {'text': 'Tüm proteini kesip yüksek glukoz infüzyonu ve intravenöz sodyum benzoat başlamak, '
                                  'yoğun bakımda hemodiyaliz hazırlığı yapmak',
                          'is_correct': True,
                          'explanation': 'Tedavide ekzojen protein derhal kesilir, katabolizmayı durdurmak için %10 '
                                         'Dekstroz başlanır, nitrojen bağlayıcılar verilir ve >400 mcmol/L için '
                                         'hemodiyaliz hazırlanır.',
                          'new_finding': 'Hasta Çocuk Yoğun Bakım Ünitesine yatırıldı. Enteral beslenme kesildi, '
                                         'katabolizmayı durdurmak için 8-10 mg/kg/dk glukoz infüzyonu (%10 Dekstroz) '
                                         'başlandı. İntravenöz Sodyum Benzoat ve Fenilasetat yüklemesi yapıldı. '
                                         'Amonyak düzeyi 485 mcmol/L olduğundan acil hemodiyaliz/hemofiltrasyon '
                                         'kateteri yerleştirildi. Seans sonrası amonyak <100 mcmol/L düzeyine '
                                         'düşürüldü, nörolojik sekelsiz taburculuk sağlandı.'},
                         {'text': 'Sadece fenobarbital yüklemesi yaparak nöbetleri durdurmak ve hiçbir metabolik ajan '
                                  'vermeden genel pediatri servisinde takibe almak',
                          'is_correct': False,
                          'scenario_update': 'Fenobarbital nöbeti baskılasa da altta yatan toksik metabolit birikimi '
                                             'sürdü; hiperamonyemik koma derinleşerek beyin ölümü gelişti.',
                          'teaching_point': 'Nöbetler toksik ensefalopatinin sonucudur; nöbet önleyici ilaçlar '
                                            'metabolit düzeyini düşürmez, hayat kurtarıcı olan agresif amonyak '
                                            'temizliğidir.'},
                         {'text': 'Bebeğin enerji ihtiyacını karşılamak için yüksek proteinli amino asit solüsyonu '
                                  'infüzyonuna başlayıp diyaliz hazırlığı yapmadan gözlemlemek',
                          'is_correct': False,
                          'scenario_update': 'Amino asit infüzyonu ekzojen azot yükünü patlattı; amonyak 1000 mcmol/L '
                                             'değerini aşarak masif beyin ödemi ve ani arrest oluşturdu.',
                          'teaching_point': 'Üre döngüsü defektlerinde amino asit veya protein verilmesi intihar '
                                            'gibidir; ilk 24-48 saatte tüm proteinler kesilerek sadece glukoz ve lipit '
                                            'verilmelidir.'}]}]}]
