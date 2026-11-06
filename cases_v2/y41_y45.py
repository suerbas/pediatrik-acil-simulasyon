# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - Y41-Y45 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "Y41",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "9 Yaşında",
        "gender": "Erkek",
        "complaint": "Dün göbek çevresinde başlayıp sağ alt kadrana yerleşen şiddetli karın ağrısı, bulantı ve iştahsızlık",
        "history": "Ailesi anlatıyor: 'Dün sabah göbeğinin çevresinde künt bir ağrı başladı. Akşama doğru ağrı sağ alt tarafa kaydı ve adım attıkça batmaya başladı. İki kez safrasız kustu, hiçbir şey yemek istemiyor. Arabayla gelirken tümseklerde karnı sarsılınca çığlık attı.' İshal, idrar yakınması, öksürük yok. Bilinen hastalığı yok. Tartı: 30 kg.",
        "final_diagnosis": "Akut Non-perfore Apandisit (Apendikolitli)",
        "disposition": "Sarı Alanda Damar Yolu, İntravenöz Sıvı, Analjezi ve Preoperatif Antibiyotik Sonrası Çocuk Cerrahisi ile Laparoskopik Apendektomi İçin Yatış",
        "case_pearl": "Göbek çevresinden sağ alt kadrana göç eden ağrı, iştahsızlık, kusma ve sarsıntıyla artan ağrı klasik tablodur. Erken analjezi (opioid dahil) tanıyı maskelemez ve verilmelidir. Pediatrik Apandisit Skoru veya Alvarado gibi klinik skorlar laboratuvarla birlikte risk sınıflaması sağlar; çocukta ilk görüntüleme ultrasonografidir, BT tanısal belirsizlikte kullanılır. Apendikolit varlığı antibiyotikle konservatif tedavide başarısızlık riskini artırır; bu nedenle cerrahi tercih edilir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme, Analjezi ve Karın Muayenesi",
                "question": "Sağ alt kadrana yerleşen şiddetli karın ağrısıyla gelen bu 9 yaşındaki çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Kabızlığa bağlı ağrı olabileceğini düşünüp lavman uygulamak ve dışkılama sonrası ağrının gerilemesini bekleyerek yeniden muayene etmek",
                        "is_correct": False,
                        "scenario_update": "Lavman sonrası az miktarda dışkı çıktı ancak ağrı ve ateş sürdü; muayene bir saat ertelendi.",
                        "teaching_point": "Ateş ve peritoneal bulgu olan çocukta lavman uygunsuzdur ve tanıyı geciktirir."
                    },
                    {
                        "text": "Vital bulgular ve hidrasyonu değerlendirip intravenöz analjezi vermek; karında lokal hassasiyet, defans, rebound ve zıplama ağrısını, testis ve akciğer muayenesini yapmak",
                        "is_correct": True,
                        "explanation": "Erken ve yeterli analjezi tanısal doğruluğu bozmaz, muayeneyi kolaylaştırır. Peritoneal irritasyon bulguları cerrahi olasılığı artırır; testis torsiyonu ve alt lob pnömonisi sağ alt kadran ağrısını taklit edebileceği için muayene edilmelidir.",
                        "new_finding": "Vital Bulgular: Ateş 38.3°C, KTA 118/dk, SS 22/dk, TA 106/66 mmHg, SpO2 %99, KDZ 2 sn. İntravenöz morfin 0.1 mg/kg sonrası ağrı skoru 9'dan 4'e indi. Sağ alt kadranda belirgin hassasiyet, istemsiz defans ve rebound; zıplayamıyor, öksürünce ağrı artıyor. Sol alt kadrana basınca sağda ağrı. Testisler normal, akciğer sesleri eşit."
                    },
                    {
                        "text": "Ateş ve kusma nedeniyle önce antipiretik ve ondansetron verip ağrının azalmasını beklemek, karın muayenesini tetkik sonuçları geldikten sonra ayrıntılandırmak",
                        "is_correct": False,
                        "scenario_update": "Ateş düştü ancak ağrı sürdü; karın muayenesi yapılmadan bir saat geçti ve analjezi gecikti.",
                        "teaching_point": "Karın ağrılı çocukta sistematik muayene ilk değerlendirmenin parçasıdır; semptomatik tedavi ağrı kontrolünün yerini tutmaz."
                    },
                    {
                        "text": "Ağrı kesicinin bulguları maskeleyeceğini düşünerek çocuk cerrahisi muayene edene kadar analjezi vermemek ve bu süre içinde oral sıvı alımına izin vermek",
                        "is_correct": False,
                        "scenario_update": "Cerrah iki saat sonra geldi; çocuk bu sürede şiddetli ağrı çekti ve içtiği sıvıyı kustu. Olası anestezi için aç kalma süresi de bozuldu.",
                        "teaching_point": "Analjezinin akut karın tanısını geciktirdiğine dair kanıt yoktur; cerrahi olasılığı olan çocuk oral alıma kapatılır."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar ve Görüntüleme",
                "question": "Peritoneal irritasyon bulguları olan, ateşli bu çocukta hangi tetkik yaklaşımı uygundur?",
                "options": [
                    {
                        "text": "Radyasyon riskini düşünmeden doğrudan intravenöz kontrastlı batın bilgisayarlı tomografisi çekmek ve laboratuvar tetkiklerini sonuca göre istemek",
                        "is_correct": False,
                        "scenario_update": "Tomografi tanısal oldu ancak ultrasonla gösterilebilecek bulgu için çocuk gereksiz radyasyon ve kontrast maddeye maruz kaldı.",
                        "teaching_point": "Çocukta ilk görüntüleme ultrasonografidir; BT, ultrason tanısal değilse ve klinik şüphe sürüyorsa kullanılır."
                    },
                    {
                        "text": "Sedasyon altında batın manyetik rezonans görüntülemesi planlamak ve sonucu beklerken çocuğu oral sıvıyla gözlem odasında izlemek",
                        "is_correct": False,
                        "scenario_update": "MR için birkaç saat beklendi; bu sürede çocuğun ateşi yükseldi ve oral alım nedeniyle anestezi gecikti.",
                        "teaching_point": "MR bazı merkezlerde ikinci basamak seçenektir; ilk tetkik değildir ve tedaviyi geciktirmemelidir."
                    },
                    {
                        "text": "Ayakta direkt batın grafisi çekmek, hava-sıvı seviyesi yoksa cerrahi bir sorun olmadığını kabul edip çocuğu oral antibiyotikle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Grafide spesifik bulgu yoktu; peritoneal bulguları olan çocuk taburcu edilmek üzereydi.",
                        "teaching_point": "Direkt grafinin sağ alt kadran ağrısında tanısal değeri düşüktür; normal grafi akut cerrahi tabloyu dışlamaz."
                    },
                    {
                        "text": "Tam kan sayımı, CRP ve tam idrar tetkiki istemek, klinik risk skorunu hesaplamak ve deneyimli bir operatörle batın ultrasonografisi yaptırmak",
                        "is_correct": True,
                        "explanation": "Lökosit, nötrofil ve CRP klinik skorlarla birlikte risk sınıflaması sağlar. İdrar tetkiki üriner nedenleri ayırır. Ultrason radyasyonsuzdur ve deneyimli ellerde yüksek duyarlılıklıdır.",
                        "new_finding": "Lökosit 15.600/mm³ (%84 nötrofil), CRP 46 mg/L, tam idrar normal. Batın ultrasonu: sağ alt kadranda kör sonlanan, kompresyonla basılmayan, 8.4 mm çaplı aperistaltik tübüler yapı; çevre yağ dokusunda ekojenite artışı ve lümende akustik gölge veren 6 mm ekojen odak. Serbest sıvı veya apse yok.",
                        "image": "assets/images/usg_appendicitis.png",
                        "image_caption": "Batın Ultrasonografisi (Sağ Alt Kadran)"
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Göç eden sağ alt kadran ağrısı, peritoneal bulgular, lökositoz ve ultrasonda lümeninde ekojen odak bulunan 8.4 mm'lik basılmayan tübüler yapı olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Meckel divertiküliti",
                        "is_correct": False,
                        "scenario_update": "Ultrasonda kör sonlanan yapı çekumla ilişkili; Meckel divertikülü ileumdan kaynaklanır.",
                        "teaching_point": "Meckel divertiküliti klinikte benzer olabilir ancak genellikle ameliyatta ayırt edilir."
                    },
                    {
                        "text": "Akut mezenterik lenfadenit",
                        "is_correct": False,
                        "scenario_update": "Ultrasonda basılmayan genişlemiş tübüler yapı ve peritoneal irritasyon bulguları var.",
                        "teaching_point": "Mezenterik lenfadenit tanısı ancak cerrahi patoloji görüntülemeyle dışlandıktan sonra konur."
                    },
                    {
                        "text": "Sağ alt lob pnömonisi",
                        "is_correct": False,
                        "scenario_update": "Solunum bulguları ve takipne yok, akciğer sesleri eşit.",
                        "teaching_point": "Alt lob pnömonisi ateş, takipne ve oskültasyon bulgusuyla birlikte karın ağrısı yapabilir."
                    },
                    {
                        "text": "Akut non-perfore apandisit (apendikolitli)",
                        "is_correct": True,
                        "explanation": "Klasik klinik seyir, lokal peritoneal bulgular, lökositoz ve ultrasonda 6 mm'den kalın, basılmayan, apendikolitli tübüler yapı akut apandisiti doğrular; apse ve serbest sıvı olmaması perforasyon lehine değildir.",
                        "new_finding": "Tanı: Akut Non-perfore Apandisit (apendikolitli)."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Cerrahi Hazırlık",
                "question": "Bu çocuğun acil serviste tedavi ve yönlendirme planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Oral alıma kapatmak, intravenöz izotonik sıvı ve düzenli analjezi sürdürmek, preoperatif antibiyotik başlayıp çocuk cerrahisiyle erken laparoskopik apendektomi planlamak",
                        "is_correct": True,
                        "explanation": "Preoperatif antibiyotik yara yeri ve intraabdominal enfeksiyon riskini azaltır. Apendikolit varlığında konservatif tedavinin başarısızlık oranı yüksek olduğundan erken cerrahi tercih edilir.",
                        "new_finding": "Seftriakson ve metronidazol başlandı, sıvı ve analjezi sürdürüldü. Çocuk cerrahisi aynı gece laparoskopik apendektomi yaptı; patolojide flegmonöz inflamasyon ve apendikolit doğrulandı. Çocuk ikinci gün taburcu edildi."
                    },
                    {
                        "text": "Antibiyotik başlamadan çocuğu servise yatırıp 24 saat seri karın muayenesiyle izlemek ve ertesi gün ultrasonu tekrarlayarak cerrahi kararı vermek",
                        "is_correct": False,
                        "scenario_update": "İzlem sırasında ateş 39.4°C'ye yükseldi; tekrar ultrasonda periapendiküler sıvı koleksiyonu gelişti.",
                        "teaching_point": "Görüntülemeyle doğrulanmış tabloda gereksiz bekleme perforasyon riskini artırır."
                    },
                    {
                        "text": "Tablo komplike olmadığı için çocuğu tek doz intravenöz seftriakson sonrasında 10 günlük oral amoksisilin-klavulanat ile taburcu edip 48 saat sonra poliklinik kontrolüne çağırmak",
                        "is_correct": False,
                        "scenario_update": "Evde ağrı ve ateş arttı; 36. saatte perforasyon ve yaygın peritonitle geri başvurdu.",
                        "teaching_point": "Antibiyotikle konservatif tedavi seçilmiş, apendikolitsiz olgularda hastanede izlemle düşünülebilir; ayaktan taburculuk uygun değildir."
                    },
                    {
                        "text": "Ağrı kontrolü sağlandığı için analjeziyi kesmek, oral sıvı denemesi yapmak ve tolere ederse ameliyatı elektif olarak birkaç hafta sonrasına planlamak",
                        "is_correct": False,
                        "scenario_update": "Analjezi kesilince ağrı yeniden şiddetlendi; oral sıvı sonrası kustu.",
                        "teaching_point": "Akut tabloda elektif erteleme uygun değildir; çocuk aç tutulur ve analjezi sürdürülür."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y42",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "8 Aylık",
        "gender": "Erkek",
        "complaint": "Aralıklı bacaklarını karnına çekerek şiddetli ağlama nöbetleri, kusma ve bezde kanlı-mukuslu dışkı",
        "history": "Ailesi anlatıyor: 'Bu sabah aniden 15-20 dakikada bir bacaklarını karnına çekip çığlık çığlığa ağlamaya başladı. Ataklar arasında bitkin, uykuya meyilli. Önce süt, sonra iki kez yeşil renkte kustu. Son bezinde koyu kırmızı, jöle kıvamında mukuslu kan gördük.' Bir hafta önce burun akıntısı ve hafif ishali olmuş. Daha önce sağlıklı. Tartı: 8.5 kg.",
        "final_diagnosis": "İleokolik İnvajinasyon",
        "disposition": "Sarı Alanda Damar Yolu, Sıvı Resüsitasyonu ve Ultrason Eşliğinde Hidrostatik Redüksiyon Sonrası Gözlem Yatışı",
        "case_pearl": "6-36 ay arasında aralıklı kolik ağrı, ataklar arası letarji, kusma ve kanlı mukuslu dışkı klasik tablodur; ancak tam triad olguların azında görülür ve letarji tek bulgu olabilir. Tanıda ilk seçenek yüksek duyarlılıklı ultrasonografidir. Peritonit, perforasyon veya düzeltilemeyen şok yoksa tedavi ultrason veya floroskopi eşliğinde hidrostatik ya da pnömatik redüksiyondur. Başarılı redüksiyon sonrası nüks %10 civarındadır; aile bilgilendirilir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Stabilizasyon",
                "question": "Aralıklı ağlama nöbetleri, yeşil kusma ve ataklar arası letarjisi olan bu bebekte ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Kusma nedeniyle ağızdan oral rehidratasyon solüsyonu denemesi yapmak, bebeği iki saat gözlemleyip ataklar sürerse kanlı dışkı için gaita kültürü göndermek",
                        "is_correct": False,
                        "scenario_update": "Bebek ORS'yi kustu; iki saatlik gözlem sonunda perfüzyonu bozuldu ve tanı gecikti.",
                        "teaching_point": "Safralı kusması ve letarjisi olan bebekte oral deneme yapılmaz; obstrüksiyon dışlanmalıdır."
                    },
                    {
                        "text": "Ataklar arasında bebeğin sakinleştiğini görüp tabloyu infantil kolik kabul etmek, damla simetikon vermek ve bezdeki kanı anal fissüre bağlayıp aileye evde izlem önermek",
                        "is_correct": False,
                        "scenario_update": "Bebek eve gönderilmek üzereyken yeniden safralı kustu ve letarjisi belirginleşti.",
                        "teaching_point": "Kolik sağlıklı genç bebekte görülür; letarji, safralı kusma ve kanlı dışkı acil cerrahi tabloyu düşündürür."
                    },
                    {
                        "text": "Kitleyi doğrulamak için hemen rektal tüp yerleştirip ılık su ile lavman uygulamak ve ardından karın muayenesini yinelemek",
                        "is_correct": False,
                        "scenario_update": "Lavman görüntüleme eşliğinde olmadığından ne tanısal ne tedavi edici oldu; bebek huzursuzlaştı.",
                        "teaching_point": "Redüksiyon yalnızca görüntüleme eşliğinde, perforasyon riskine karşı hazırlıklı ekip tarafından yapılır."
                    },
                    {
                        "text": "Havayolu, solunum ve perfüzyonu değerlendirmek, damar yolu açıp 20 mL/kg izotonik sıvı vermek, oral alımı kesmek ve karında kitle ve peritonit bulgusu aramak",
                        "is_correct": True,
                        "explanation": "Kusma ve üçüncü boşluğa sıvı kaybı perfüzyonu bozar; redüksiyon veya cerrahi öncesi resüsitasyon gerekir. Safralı kusma ve letarji obstrüksiyonu düşündürür; peritonit bulgusu redüksiyonu kontrendike kılar.",
                        "new_finding": "Vital Bulgular: Ateş 37.4°C, KTA 156/dk, SS 32/dk, TA 84/52 mmHg, SpO2 %98, KDZ 3 sn. Ataklar arası letarjik. Sağ üst kadranda transvers uzanan, sosis şeklinde, düzgün sınırlı kitle; sağ alt kadranda boşluk hissi. Defans ve rebound yok. 20 mL/kg serum fizyolojik sonrası KTA 132/dk, KDZ 2 sn. Bezde koyu kırmızı mukuslu kan."
                    }
                ]
            },
            {
                "stage_title": "Görüntüleme Kararı",
                "question": "Resüsitasyona yanıt veren, sağ üst kadranda kitle palpe edilen bu bebekte hangi görüntüleme yöntemi tercih edilmelidir?",
                "options": [
                    {
                        "text": "Tanıyı kesinleştirmek ve perforasyonu dışlamak için intravenöz kontrastlı batın bilgisayarlı tomografisi çekmek",
                        "is_correct": False,
                        "scenario_update": "Tomografi tanıyı gösterdi ancak bebek gereksiz radyasyon, kontrast ve sedasyona maruz kaldı.",
                        "teaching_point": "Bu tabloda BT ilk seçenek değildir; ultrason yüksek duyarlılıkla tanı koyar."
                    },
                    {
                        "text": "Batın ultrasonografisi yapmak; iç içe geçmiş bağırsak segmentlerini, serbest sıvıyı, kanlanmayı ve olası öncü noktayı değerlendirmek",
                        "is_correct": True,
                        "explanation": "Ultrasonografi radyasyonsuz, hızlı ve yüksek duyarlılık ve özgüllüğe sahip ilk basamak tetkiktir. Serbest sıvı, kanlanma kaybı ve öncü nokta redüksiyon kararını etkiler.",
                        "new_finding": "Batın ultrasonu: sağ subhepatik alanda transvers kesitte iç içe konsantrik hipo-hiperekojen halkalardan oluşan 3.2 cm'lik kitle, longitudinal kesitte böbreği andıran görünüm. Duvarda kanlanma korunmuş, serbest hava ve belirgin serbest sıvı yok; öncü nokta izlenmedi.",
                        "image": "assets/images/usg_intussusception.png",
                        "image_caption": "Batın Ultrasonografisi (Sağ Subhepatik Alan)"
                    },
                    {
                        "text": "Kanlı dışkı nedeniyle önce teknesyum sintigrafisi ile ektopik mide mukozası aramak ve sonuç normalse kolonoskopi planlamak",
                        "is_correct": False,
                        "scenario_update": "Sintigrafi için saatler gerekti; akut obstrüktif tablo gözden kaçtı.",
                        "teaching_point": "Ağrısız masif rektal kanamada sintigrafi düşünülür; kolik ağrı ve kitle başka bir tabloyu gösterir."
                    },
                    {
                        "text": "Yalnızca ayakta direkt batın grafisi çekmek, sağ alt kadranda gaz görülürse tanıyı dışlayıp bebeği gözlem odasında izlemek",
                        "is_correct": False,
                        "scenario_update": "Grafi nonspesifik bulgular gösterdi; tanı ve tedavi birkaç saat gecikti.",
                        "teaching_point": "Direkt grafi duyarsızdır; yalnızca perforasyon şüphesinde serbest hava için değerlidir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Aralıklı kolik ağrı, letarji, kanlı mukuslu dışkı, sağ üst kadranda kitle ve ultrasonda konsantrik halkalar olan bu bebekte tanı nedir?",
                "options": [
                    {
                        "text": "Salmonella enteriti",
                        "is_correct": False,
                        "scenario_update": "Ateş ve sulu ishal yok; palpabl kitle ve ultrason bulgusu enfeksiyonla açıklanmaz.",
                        "teaching_point": "Enfeksiyöz kanlı ishal kolik ağrı ve kitle ile seyretmez."
                    },
                    {
                        "text": "Meckel divertikülü kanaması",
                        "is_correct": False,
                        "scenario_update": "Kanama ağrılı ataklar ve kitleyle birlikte; ultrasonda iç içe geçmiş segmentler var.",
                        "teaching_point": "Meckel kanaması tipik olarak ağrısız ve masiftir; ancak divertikül öncü nokta da olabilir."
                    },
                    {
                        "text": "Orta bağırsak volvulusu",
                        "is_correct": False,
                        "scenario_update": "Ultrasonda mezenterik damarların dönmesi yok; iç içe geçmiş segmentler görülüyor.",
                        "teaching_point": "Volvulus genellikle yenidoğan döneminde safralı kusmayla başlar ve acil cerrahi gerektirir."
                    },
                    {
                        "text": "İleokolik invajinasyon",
                        "is_correct": True,
                        "explanation": "Klinik tablo ve ultrasonda konsantrik halka ve böbreği andıran görünüm ileumun kolona girmesiyle oluşan ileokolik invajinasyonu doğrular; bu yaşta çoğunlukla viral enfeksiyon sonrası lenfoid hiperplazi öncü rol oynar.",
                        "new_finding": "Tanı: İleokolik İnvajinasyon."
                    }
                ]
            },
            {
                "stage_title": "Redüksiyon ve İzlem",
                "question": "Perfüzyonu düzelen, peritonit ve serbest hava bulgusu olmayan bu bebekte tedavi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Başarılı redüksiyon sonrası bebeği hemen taburcu etmek ve tekrar olasılığına karşı iki hafta oral steroid ile profilaksi önermek",
                        "is_correct": False,
                        "scenario_update": "Steroid profilaksisi için yeterli kanıt yoktu; gözlem yapılmadan taburculuk erken nükslerin kaçırılmasına yol açabilirdi.",
                        "teaching_point": "Redüksiyon sonrası kısa gözlem önerilir; nüksü önlemek için rutin ilaç tedavisi önerilmez."
                    },
                    {
                        "text": "Doğrudan çocuk cerrahisine acil laparotomi için yönlendirmek, manuel redüksiyon yapmak ve aynı seansta apendektomi eklemek",
                        "is_correct": False,
                        "scenario_update": "Redüksiyon denenmeden cerrahiye gidildi; bebek gereksiz yere laparotomi ve anesteziye maruz kaldı.",
                        "teaching_point": "Kontrendikasyon yoksa ilk tedavi görüntüleme eşliğinde redüksiyondur; cerrahi başarısızlık, perforasyon veya peritonitte yapılır."
                    },
                    {
                        "text": "Ultrason veya floroskopi eşliğinde hidrostatik ya da pnömatik redüksiyon yapmak, cerrahiyi hazır tutmak ve sonrasında birkaç saat gözlemleyip beslenmeyi başlatmak",
                        "is_correct": True,
                        "explanation": "Görüntüleme eşliğinde redüksiyonun başarısı %80-90'dır. Perforasyon riskine karşı cerrahi ekip bilgilendirilir. Başarılı redüksiyon sonrası gözlem ve beslenme toleransı izlenir; aile nüks belirtileri konusunda bilgilendirilir.",
                        "new_finding": "Ultrason eşliğinde ılık serum fizyolojik ile hidrostatik redüksiyon yapıldı; sıvının terminal ileuma serbestçe geçtiği görüldü. Bebek rahatladı, uykuya daldı. Dört saat sonra emmeye başladı ve ertesi gün taburcu edildi."
                    },
                    {
                        "text": "Kendiliğinden düzelme olasılığı nedeniyle intravenöz antibiyotik başlayıp bebeği servise yatırmak, 24 saat aç bırakarak izlemek ve kontrol ultrasonuna göre karar vermek",
                        "is_correct": False,
                        "scenario_update": "İzlem sırasında bebeğin ataklar arası letarjisi arttı ve kontrol ultrasonda kanlanma azaldı.",
                        "teaching_point": "İleokolik invajinasyon nadiren kendiliğinden düzelir; gecikme iskemi ve perforasyon riskini artırır."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y43",
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
        "id": "Y44",
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
        "id": "Y45",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "7 Yaşında",
        "gender": "Erkek",
        "complaint": "Şiddetli karın ağrısı, inatçı kusma, derin ve hızlı soluk alıp verme ve dalgınlık",
        "history": "Ailesi anlatıyor: 'İki gündür karnı ağrıyor ve kusuyor. Mide üşütmesi sandık. Bugün çok halsizleşti, konuşurken saçmalamaya başladı, nefesi çok derin ve hızlı. Son birkaç haftadır çok su içiyordu, sık tuvalete gidiyordu, geceleri altını ıslatmaya başladı. Kilo da verdi.' Bilinen hastalığı yok. Tartı: 22 kg (bir ay önce 24 kg).",
        "final_diagnosis": "Yeni Tanı Tip 1 Diyabet ve Ağır Diyabetik Ketoasidoz",
        "disposition": "Sarı Alanda İki Damar Yolu, Kontrollü İzotonik Sıvı, Sıvıdan Bir Saat Sonra İntravenöz Düşük Doz İnsülin İnfüzyonu ve Çocuk Yoğun Bakım Yatışı",
        "case_pearl": "Poliüri, polidipsi, kilo kaybı ve sekonder enürezisten sonra gelişen karın ağrısı, kusma ve derin-hızlı solunum ağır asidozu düşündürür; karın bulguları akut batını taklit edebilir. ISPAD önerisi: dolaşım bozuksa 10 mL/kg izotonik bolus, ardından açığın 24-48 saatte kontrollü kapatılması; insülin sıvıdan 1 saat sonra, bolus yapılmadan 0.05-0.1 Ü/kg/saat başlanır. Potasyum insülinle birlikte eklenir. Bikarbonat rutin kullanılmaz. Baş ağrısı, bradikardi, hipertansiyon ve bilinç bozulması beyin ödemini düşündürür; mannitol veya %3 NaCl hazır tutulur.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Solunum Paterni",
                "question": "Karın ağrısı, kusma, derin-hızlı solunum ve bilinç bulanıklığı olan bu 7 yaşındaki çocukta ilk değerlendirmeniz nedir?",
                "options": [
                    {
                        "text": "Havayolu, solunum ve dolaşımı değerlendirip Glasgow skorunu kaydetmek, kapiller kan şekeri ve keton bakmak, tartmak ve iki damar yolu açmak",
                        "is_correct": True,
                        "explanation": "Derin-hızlı solunum metabolik asidozun solunumsal kompanzasyonudur. Kan şekeri ve keton tanıyı dakikalar içinde yönlendirir. Başlangıç bilinç düzeyi beyin ödemini erken tanımak için referanstır; doğru tartı sıvı ve insülin dozları için gereklidir.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 142/dk, SS 36/dk (derin, düzenli), TA 102/64 mmHg, SpO2 %99, KDZ 3 sn. Nefeste aseton kokusu. GKS 13 (konfüze). Karında yaygın hassasiyet, defans ve rebound yok. Kapiller kan şekeri 460 mg/dL, kan ketonu 5.8 mmol/L. Tartı 22 kg. İki damar yolu açıldı."
                    },
                    {
                        "text": "Hızlı solunumu kaygıya bağlayıp çocuğu kese kağıdına soluyarak sakinleştirmeye çalışmak ve ardından anksiyolitik vermeyi düşünmek",
                        "is_correct": False,
                        "scenario_update": "Kese kağıdıyla solunum kompanzasyonu bozdu ve asidoz derinleşti; çocuk uykuya meyilli hale geldi.",
                        "teaching_point": "Derin-hızlı solunum metabolik asidozun kompanzasyonu olabilir; baskılanması tehlikelidir."
                    },
                    {
                        "text": "Bilinç bulanıklığı nedeniyle menenjit ve ensefalit düşünüp önce kontrastsız beyin tomografisi çekmek ve ardından lomber ponksiyon yapmak",
                        "is_correct": False,
                        "scenario_update": "Tomografi için sedasyon gündeme geldi; kan şekeri ve asit-baz durumu değerlendirilmeden zaman kaybedildi.",
                        "teaching_point": "Bilinç değişikliğinde ilk adımlar havayolu-dolaşım ve yatak başı kan şekeridir."
                    },
                    {
                        "text": "Karın ağrısı ve kusma nedeniyle akut batın düşünüp çocuğu aç bırakmak, batın ultrasonu istemek ve çocuk cerrahisi konsültasyonu beklemek",
                        "is_correct": False,
                        "scenario_update": "Ultrason beklenirken kan şekeri bakılmadı; çocuğun bilinci daha da bulandı.",
                        "teaching_point": "Kusan, derin solunumlu ve bilinç değişikliği olan her çocukta hemen kapiller kan şekeri bakılmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Acil Biyokimya ve Başlangıç Sıvı Tedavisi",
                "question": "Kan şekeri 460 mg/dL ve kan ketonu yüksek olan bu çocukta tetkik ve başlangıç sıvı yaklaşımı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Venöz kan gazı, elektrolitler, BUN-kreatinin ve ozmolalite göndermek; 10 mL/kg serum fizyolojiği bir saatte verip kalan açığı 24-48 saate yaymak",
                        "is_correct": True,
                        "explanation": "Asidozun derinliği, düzeltilmiş sodyum ve potasyum tedavi planını belirler. ISPAD'a göre dolaşım bozukluğu olan çocukta 10-20 mL/kg izotonik sıvı verilir, açık 24-48 saatte kontrollü olarak kapatılır.",
                        "new_finding": "Venöz kan gazı: pH 7.10, pCO2 18 mmHg, HCO3 5.8 mmol/L. Na 129 mEq/L (düzeltilmiş 135), K 4.9 mEq/L, Cl 97 mEq/L, anyon açığı 26, BUN 48 mg/dL, kreatinin 0.9 mg/dL. İlk saatte 10 mL/kg serum fizyolojik verildi; KDZ 2 sn'ye indi."
                    },
                    {
                        "text": "Kan şekerini en kısa sürede düşürmek için sıvı başlamadan 0.1 Ü/kg intravenöz insülin bolusu yapmak ve ardından laboratuvar sonuçlarını beklemek",
                        "is_correct": False,
                        "scenario_update": "Sıvı verilmeden yapılan insülin bolusu sonrası potasyum düştü ve dolaşım bozuldu.",
                        "teaching_point": "İnsülin bolusu yapılmaz; infüzyon sıvı tedavisinden yaklaşık bir saat sonra başlatılır."
                    },
                    {
                        "text": "pH 7.10 olduğu için asidozu hızla düzeltmek amacıyla 2 mEq/kg sodyum bikarbonat infüzyonu vermek ve sıvıyı kan gazına göre ayarlamak",
                        "is_correct": False,
                        "scenario_update": "Bikarbonat sonrası potasyum hızla düştü; paradoksal santral sinir sistemi asidozu ve beyin ödemi riski arttı.",
                        "teaching_point": "Bikarbonat rutin kullanılmaz; yalnızca hayatı tehdit eden hiperkalemi veya kardiyak instabilitede düşünülür."
                    },
                    {
                        "text": "Dehidratasyonu hızla düzeltmek için 20 mL/kg serum fizyolojiği üç kez art arda vermek ve ardından idame hızında %0.45 NaCl ile devam etmek",
                        "is_correct": False,
                        "scenario_update": "Toplam 60 mL/kg hızlı sıvı sonrası çocukta baş ağrısı ve bradikardi gelişti; beyin ödemi açısından acil tedavi gerekti.",
                        "teaching_point": "Bu tabloda sıvı kontrollü verilir; tekrarlanan hızlı bolus ancak gerçek şokta gerekir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Poliüri, polidipsi, kilo kaybı, kan şekeri 460 mg/dL, kan ketonu 5.8 mmol/L, pH 7.10 ve HCO3 5.8 mmol/L olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Hiperozmolar hiperglisemik durum",
                        "is_correct": False,
                        "scenario_update": "Kan şekeri 600 mg/dL'nin altında, belirgin ketozis ve ağır asidoz var.",
                        "teaching_point": "Hiperozmolar durumda kan şekeri >600 mg/dL, ozmolalite >320 mOsm/kg'dır ve ketoz-asidoz belirgin değildir."
                    },
                    {
                        "text": "Salisilat zehirlenmesi",
                        "is_correct": False,
                        "scenario_update": "İlaç alım öyküsü yok; belirgin hiperglisemi ve ketonemi tabloyu açıklıyor.",
                        "teaching_point": "Salisilat zehirlenmesi solunumsal alkaloz ve metabolik asidoz karışımıyla seyreder."
                    },
                    {
                        "text": "Ağır diyabetik ketoasidoz",
                        "is_correct": True,
                        "explanation": "Hiperglisemi, ketonemi ve pH <7.1 veya HCO3 <5 mmol/L ağır diyabetik ketoasidozu tanımlar; öykü yeni başlangıçlı tip 1 diyabeti gösterir.",
                        "new_finding": "Tanı: Yeni Tanı Tip 1 Diyabet ve Ağır Diyabetik Ketoasidoz."
                    },
                    {
                        "text": "Perfore akut apandisit",
                        "is_correct": False,
                        "scenario_update": "Karında defans ve rebound yok; karın ağrısı metabolik tabloyla açıklanıyor.",
                        "teaching_point": "Ağır asidozda karın ağrısı sıktır ve tedaviyle geriler; cerrahi tablo ancak bulgular sürerse düşünülür."
                    }
                ]
            },
            {
                "stage_title": "İnsülin, Potasyum ve Yoğun Bakım İzlemi",
                "question": "Sıvı tedavisinin birinci saatini tamamlayan bu çocukta tedaviye nasıl devam edilmelidir?",
                "options": [
                    {
                        "text": "Kan şekeri hızla düşsün diye insülini 0.2 Ü/kg/saat başlatmak, dekstroz eklemeden saatlik 100 mg/dL düşüş hedeflemek ve beyin ödemine karşı sıvıyı tamamen kesmek",
                        "is_correct": False,
                        "scenario_update": "Kan şekeri çok hızlı düştü, sıvı kesildiği için perfüzyon bozuldu; çocukta baş ağrısı ve huzursuzluk gelişti.",
                        "teaching_point": "Kan şekeri ve ozmolalitedeki hızlı düşüş beyin ödemi riskini artırır; dekstroz eklenir, insülin dozu artırılmaz."
                    },
                    {
                        "text": "Subkutan hızlı etkili insülini saatte bir uygulayarak çocuğu genel pediatri servisine yatırmak ve potasyumu oral yoldan sabah vermek",
                        "is_correct": False,
                        "scenario_update": "Bilinci bulanık çocukta servis izlemi yetersiz kaldı; potasyum gece 2.9 mEq/L'ye düştü.",
                        "teaching_point": "Ağır tablo intravenöz insülin, parenteral potasyum ve yoğun bakım düzeyinde izlem gerektirir."
                    },
                    {
                        "text": "Bolus yapmadan 0.05-0.1 Ü/kg/saat intravenöz insülin başlamak, potasyumu sıvıya eklemek, kan şekeri düşünce dekstroz eklemek ve saatlik nörolojik izlemle yoğun bakıma yatırmak",
                        "is_correct": True,
                        "explanation": "Düşük doz insülin infüzyonu ketozu güvenle çözer. İnsülin potasyumu hücre içine sokar; idrar çıkışı varsa sıvıya potasyum eklenir. Kan şekeri 250-300 mg/dL'ye inince dekstroz eklenir. Saatlik nörolojik değerlendirme beyin ödemini erken yakalar.",
                        "new_finding": "0.05 Ü/kg/saat insülin infüzyonu ve 40 mmol/L potasyum başlandı; kan şekeri 280 mg/dL olunca %5 dekstroz eklendi. Saatlik kan şekeri ve nörolojik izlemle yoğun bakıma alındı. Asidoz 18 saatte düzeldi, beyin ödemi gelişmedi."
                    },
                    {
                        "text": "Potasyum 4.9 mEq/L olduğu için tedavi boyunca potasyum eklememek, insülini kan şekeri normale gelince kesmek ve ketonları izlememek",
                        "is_correct": False,
                        "scenario_update": "İnsülin sonrası potasyum hızla düşerek aritmi riski oluştu; insülin erken kesilince ketoz yeniden derinleşti.",
                        "teaching_point": "Vücut potasyum deposu boşalmıştır; insülinle potasyum eklenir. İnsülin asidoz düzelene kadar dekstrozla birlikte sürdürülür."
                    }
                ]
            }
        ]
    }
]
