# -*- coding: utf-8 -*-
"""
Sarı Alan Vakaları - S51-S55 (v2 Şartnamesine Uygun Yeniden Yazım)
"""

CASES = [
    {
        "id": "S51",
        "category": "⚡ Alerji, Zehirlenme & Diğer Aciller",
        "age": "2 Yaşında (12 kg)",
        "gender": "Erkek",
        "complaint": "Bir saat önce su şişesine konmuş lavabo açıcı sıvıdan içtikten sonra ağlama, salya akması ve su içmeyi reddetme",
        "history": "Annesi anlatıyor: 'Mutfak lavabosunu açmak için kullandığımız sıvıyı su şişesine boşaltmıştım, tezgâhta kalmış. Oğlum bir yudum alıp çığlık attı, hemen ağzını yıkadım ve süt içirmeye çalıştım ama içmedi.' Bir kez kusmuş, kusmukta kan yok. Öksürük, ses kısıklığı veya nefes darlığı yok. Ürün şişesi yanında; etikette 'sodyum hidroksit içerir' yazıyor. Daha önce sağlıklı.",
        "final_diagnosis": "Alkali Korozif Madde (Lavabo Açıcı) Yutmasına Bağlı Zargar Evre 2b Özofagus Yanığı",
        "disposition": "Ağızdan Beslenme Kesilerek IV Sıvı, PPİ ve Darlık İzlemi Planıyla Çocuk Gastroenteroloji Yatışı",
        "case_pearl": "Korozif madde yutmada kusturma, nötralize etme, mide lavajı ve aktif kömür kontrendikedir. Ağız içinde lezyon olmaması özofagus hasarını dışlamaz. Semptomatik çocukta (salya, kusma, yutamama, stridor) özofagus hasarı yüksek olasılıktır. Endoskopi ilk 24 saatte (perforasyon riski nedeniyle 5. günden sonra değil) yapılmalıdır. Zargar sınıflaması prognozu belirler: evre 2b ve üzerinde darlık riski yüksektir. Darlık için 3. haftada kontrastlı grafi ile izlem yapılır.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Lavabo açıcı içtikten sonra salyası akan bu çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Maddeyi nötralize etmek için seyreltik sirke veya limon suyu içirmek, ardından bol süt vererek midedeki maddeyi seyreltmeye çalışmak",
                        "is_correct": False,
                        "scenario_update": "Sıvı verildikten sonra çocuk kustu; korozif madde özofagusa yeniden temas etti ve ağlaması arttı.",
                        "teaching_point": "Nötralizasyon ısı açığa çıkarır ve kusmayı tetikler; korozif yutmada ağızdan hiçbir şey verilmez."
                    },
                    {
                        "text": "Mide sondası takıp lavaj yapmak ve ardından toksini bağlamak için aktif kömür vermek, sonra muayeneyi tamamlamak",
                        "is_correct": False,
                        "scenario_update": "Sonda yerleştirme sırasında çocuk öğürdü ve kustu; aktif kömür endoskopik görüşü engelleyecek şekilde mukozayı kapladı.",
                        "teaching_point": "Korozif maddelerde lavaj ve aktif kömür kontrendikedir; perforasyon riski taşır ve endoskopiyi zorlaştırır."
                    },
                    {
                        "text": "Havayolunu stridor, ses değişikliği ve solunum sıkıntısı açısından değerlendirip ağızdan alımı kesmek, ağız içini incelemek ve damar yolu açmak",
                        "is_correct": True,
                        "explanation": "Laringeal ödem havayolunu tehdit edebilir. Ağızdan alım kesilir; ağız içi bulgular kaydedilir ancak lezyon olmaması özofagus hasarını dışlamaz.",
                        "new_finding": "Vital Bulgular: Ateş 36.9°C, KTA 132/dk, SS 26/dk, SpO2 %99. Stridor ve ses kısıklığı yok, solunum rahat. Dilin ucu ve sağ yanak mukozasında beyazımsı, hassas ödemli alanlar; dudak köşesinde eritem. Sürekli salya akıyor, yutkunmayı reddediyor. Göğüs ve karın muayenesi olağan, deri altı amfizemi yok."
                    },
                    {
                        "text": "Ağız içinde belirgin yara olmadığını varsayarak yalnızca ağzı yıkamak, bir saat gözlemde su içebiliyorsa aileyi evden izlem önerisiyle göndermek",
                        "is_correct": False,
                        "scenario_update": "Çocuk sıvıyı yine reddetti; ertesi gün ateş ve göğüs ağrısıyla getirildi.",
                        "teaching_point": "Semptomatik çocukta özofagus hasarı olasılığı yüksektir; ağız bulgusu olmasa bile ileri değerlendirme gerekir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik ve Endoskopi Kararı",
                "question": "Havayolu güvende olan bu çocukta hangi tetkik ve zamanlama doğrudur?",
                "options": [
                    {
                        "text": "Hasarı göstermek için hemen baryumlu özofagus grafisi çekmek ve grafi normalse endoskopi yapmadan beslenmeye başlamak",
                        "is_correct": False,
                        "scenario_update": "Erken baryum grafisi mukozal hasarı göstermedi; baryum ayrıca sonraki endoskopik değerlendirmeyi zorlaştırdı.",
                        "teaching_point": "Akut dönemde kontrastlı grafi hasarın derinliğini göstermez; ilk değerlendirme endoskopidir, kontrast grafi darlık izleminde kullanılır."
                    },
                    {
                        "text": "Kesin bilgi için yutmadan sonraki ilk saat içinde, çocuk aç olmasa bile hemen acil endoskopi yaptırmak ve sonucuna göre plan yapmak",
                        "is_correct": False,
                        "scenario_update": "Çok erken yapılan endoskopi hasarın tam sınırlarını göstermedi; tam mide nedeniyle aspirasyon riski yüksekti.",
                        "teaching_point": "Endoskopi hasar sınırlarının belirginleştiği 12-24. saatlerde, uygun açlık sonrası yapılmalıdır."
                    },
                    {
                        "text": "Akciğer grafisi ve kan gazını alıp ağızdan alımı kesmek, IV sıvı ve PPİ başlamak; endoskopiyi ilk 24 saat içinde planlamak",
                        "is_correct": True,
                        "explanation": "Akciğer grafisi mediastinit ve perforasyon için ilk taramadır. Endoskopi yaralanmanın derecesini ve tedavi planını belirler; 24 saat içinde yapılmalı, 5. günden sonra perforasyon riski nedeniyle ertelenmemelidir.",
                        "new_finding": "Akciğer grafisi normal, serbest hava veya mediastinal genişleme yok. Kan gazı normal. 16. saatte yapılan endoskopi: Orta ve distal özofagusta çevresel, eksüdalı, beyaz plaklı derin ülserasyonlar; midede yaygın hiperemi, perforasyon yok."
                    },
                    {
                        "text": "Endoskopiye gerek olmadığını düşünüp toraks ve batın bilgisayarlı tomografisi çekmek ve özofagus duvar kalınlığına göre karar vermek",
                        "is_correct": False,
                        "scenario_update": "Tomografide özofagus duvarında hafif kalınlaşma görüldü; mukozal hasarın derecesi değerlendirilemedi.",
                        "teaching_point": "Tomografi perforasyon şüphesinde yararlıdır, ancak mukozal hasarın sınıflaması için endoskopinin yerini tutmaz."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Endoskopi bulgularına göre yaralanmanın sınıflaması nedir?",
                "options": [
                    {
                        "text": "Zargar evre 1 (yalnız ödem ve hiperemi)",
                        "is_correct": False,
                        "scenario_update": "Endoskopide ödem ve hiperemiden öte, derin ve çevresel ülserler vardı.",
                        "teaching_point": "Evre 1 yalnızca ödem ve hiperemidir; darlık riski çok düşüktür."
                    },
                    {
                        "text": "Zargar evre 2a (yüzeyel ülserler)",
                        "is_correct": False,
                        "scenario_update": "Ülserler yüzeyel değil, derin ve çevreseldi.",
                        "teaching_point": "Evre 2a yüzeyel ülser, erozyon ve eksüda ile sınırlıdır."
                    },
                    {
                        "text": "Zargar evre 3a (fokal nekroz)",
                        "is_correct": False,
                        "scenario_update": "Kahverengi-siyah nekroz alanı görülmedi.",
                        "teaching_point": "Evre 3 nekrozla karakterizedir; 3a fokal, 3b yaygın nekrozdur."
                    },
                    {
                        "text": "Zargar evre 2b (derin veya çevresel ülserler)",
                        "is_correct": True,
                        "explanation": "Çevresel, eksüdalı derin ülserasyonlar Zargar evre 2b özofagus yanığını gösterir; bu evrede darlık riski yüksektir.",
                        "new_finding": "Tanı: Alkali korozif yutmaya bağlı Zargar evre 2b özofagus yanığı."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve İzlem Planı",
                "question": "Evre 2b özofagus yanığı olan bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Ağızdan beslenmeyi kesip IV sıvı, PPİ ve analjezi vermek; tolere edince sıvı gıdaya geçmek ve 3. haftada darlık için kontrastlı grafi planlamak",
                        "is_correct": True,
                        "explanation": "Destek tedavisi ve beslenme planı esastır. Ekip, kısa süreli yüksek doz metilprednizolonu evre 2b için değerlendirebilir. Antibiyotik rutin değildir. Darlık riski nedeniyle kontrastlı grafi ile izlem yapılır.",
                        "new_finding": "Yedinci gün salya geriledi ve sıvı gıdaya geçildi. Üçüncü hafta kontrastlı grafide distal özofagusta 2 cm'lik hafif daralma saptandı ve dilatasyon programına alındı."
                    },
                    {
                        "text": "Çocuk salya akıtmayı bıraktığında ağız lezyonları iyileşiyor kabul edip ikinci gün normal diyetle taburcu etmek, darlık izlemi planlamamak",
                        "is_correct": False,
                        "scenario_update": "Altı hafta sonra çocuk katı gıdaları yutamama ve kilo kaybıyla getirildi; ileri derecede darlık saptandı.",
                        "teaching_point": "Evre 2b yanıkta darlık sık gelişir; semptomlar düzelse de kontrastlı grafiyle izlem gerekir."
                    },
                    {
                        "text": "Enfeksiyonu önlemek için iki hafta geniş spektrumlu IV antibiyotik başlamak ve beslenmeyi yalnızca total parenteral beslenmeyle sürdürmek",
                        "is_correct": False,
                        "scenario_update": "Uzun süreli antibiyotik ishale neden oldu; santral kateter enfeksiyonu gelişti.",
                        "teaching_point": "Rutin antibiyotik önerilmez; mümkün olan en kısa sürede enteral beslenmeye geçilmelidir."
                    },
                    {
                        "text": "Darlığı önlemek için ilk hafta içinde endoskopik balon dilatasyonu yapmak ve ardından haftalık dilatasyon seanslarına başlamak",
                        "is_correct": False,
                        "scenario_update": "Erken dilatasyon sırasında özofagus duvarında perforasyon gelişti.",
                        "teaching_point": "Akut dönemde (ilk 3-4 hafta) dilatasyon perforasyon riski taşır; darlık geliştikten sonra yapılır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S52",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "8 Yaşında",
        "gender": "Erkek",
        "complaint": "Antibiyotik tedavisi sonrası başlayan şiddetli kanlı-mukuslu ishal, yüksek ateş ve karında şişlik",
        "history": "Ailesi anlatıyor: 'On gün önce sinüzit nedeniyle önce amoksisilin-klavulanat, sonra sefiksim kullandı. İlaçlar bittikten üç gün sonra günde 10-12 kez çok kötü kokulu, mukuslu, kanlı ishal başladı. Karın ağrısı çok şiddetli, ateşi 39.1°C'ye çıktı, son 12 saatte karnı belirgin şişti.' Yakın zamanda seyahat veya çiğ gıda öyküsü yok. Tartı: 26 kg.",
        "final_diagnosis": "Ağır Clostridioides difficile Koliti (Psödomembranöz Kolit)",
        "disposition": "Sarı Alanda Temas İzolasyonu, Gereksiz Antibiyotiklerin Kesilmesi, Oral Vankomisin ve Toksik Megakolon İzlemi ile Yatış",
        "case_pearl": "Antibiyotik kullanımı sırasında veya sonrasındaki 8-12 hafta içinde başlayan ishalde bu etken düşünülmelidir. Test yalnızca şekilsiz dışkıda yapılır; 1 yaş altında kolonizasyon sık olduğu için test önerilmez. Lökositoz >15.000/mm³, kreatinin artışı ve hipoalbüminemi ağır hastalığı, hipotansiyon, ileus veya megakolon fulminan hastalığı gösterir. Tedavide oral vankomisin (veya fidaksomisin) kullanılır; fulminan olguda intravenöz metronidazol eklenir. Sporlar alkole dirençli olduğundan el hijyeni su ve sabunla yapılır.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Toksik Tablo",
                "question": "Antibiyotik sonrası kanlı ishal, yüksek ateş ve karın şişliği olan bu çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Hemodinamiyi, hidrasyonu ve toksik görünümü değerlendirmek; karın distansiyonu ve periton irritasyonunu aramak, damar yolu açıp temas izolasyonu başlatmak",
                        "is_correct": True,
                        "explanation": "Toksik görünüm, distansiyon ve periton bulguları megakolon veya perforasyon gibi fulminan seyri düşündürür. Hastane içi bulaşı önlemek için temas izolasyonu tanı konmadan başlanır.",
                        "new_finding": "Vital Bulgular: Ateş 38.9°C, KTA 128/dk, SS 24/dk, TA 102/62 mmHg, SpO2 %98, KDZ 2.5 sn. Toksik ve bitkin görünüyor. Karın distandü, timpanik, kolon trasesi boyunca yaygın hassasiyet ve istemli defans; belirgin rebound yok. Bezde kötü kokulu, mukuslu, kanlı sulu dışkı. Temas izolasyonu başlandı, damar yolu açıldı."
                    },
                    {
                        "text": "Sık dışkılamayı azaltmak için oral loperamid başlamak, oral rehidratasyon solüsyonu önermek ve dışkı sayısı azalırsa çocuğu evde izleme almak",
                        "is_correct": False,
                        "scenario_update": "Loperamid sonrası dışkı sayısı azaldı ancak karın daha da gerildi ve ateş yükseldi.",
                        "teaching_point": "Kanlı ve toksik kolitte antimotilite ajanlar megakolon riskini artırır."
                    },
                    {
                        "text": "Sinüzit tedavisinin yetersiz kaldığını düşünüp intravenöz seftriakson başlamak ve ishali ilaç yan etkisi olarak kabul etmek",
                        "is_correct": False,
                        "scenario_update": "Yeni geniş spektrumlu antibiyotik ishali daha da ağırlaştırdı.",
                        "teaching_point": "Gereksiz antibiyotikler kesilmeli; yeni antibiyotik ancak spesifik endikasyonla verilmelidir."
                    },
                    {
                        "text": "Kanlı ishal nedeniyle hemen ampirik siprofloksasin başlamak ve izolasyon önlemlerini dışkı kültürü sonucuna göre planlamak",
                        "is_correct": False,
                        "scenario_update": "Ampirik kinolon tabloyu düzeltmedi; izolasyon gecikince oda arkadaşı çocukta da ishal başladı.",
                        "teaching_point": "Temas izolasyonu şüphe anında başlanır; bu tabloda ampirik kinolon yararsızdır."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar ve Görüntüleme",
                "question": "Toksik görünümlü, karnı distandü bu çocukta hangi tetkikler öncelikli olarak istenmelidir?",
                "options": [
                    {
                        "text": "Hemogram, CRP, kreatinin, albümin ve elektrolitler istemek; şekilsiz dışkıda GDH antijeni ve toksin testi yapmak, direkt batın grafisi çekmek",
                        "is_correct": True,
                        "explanation": "Lökosit, kreatinin ve albümin hastalık şiddetini belirler. İki basamaklı dışkı testi (GDH ve toksin) tanıyı doğrular. Direkt grafi kolon dilatasyonunu ve perforasyonu gösterir.",
                        "new_finding": "Lökosit 24.800/mm³ (%86 nötrofil), CRP 94 mg/L, albümin 2.6 g/dL, kreatinin 0.7 mg/dL, Na 133 mEq/L. Dışkıda GDH antijeni ve toksin A/B pozitif; dışkı kültüründe Salmonella, Shigella ve Campylobacter üremedi. Direkt grafi: transvers kolon 5.2 cm genişlemiş, serbest hava yok."
                    },
                    {
                        "text": "Şiddetli karın ağrısı nedeniyle mezenterik iskemiyi dışlamak için acil BT anjiyografi çekmek ve böbrek fonksiyonlarını kontrast sonrası değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "BT kolit bulgularını gösterdi ancak dışkı testleri ve temel laboratuvar gecikti.",
                        "teaching_point": "BT seçilmiş olgularda komplikasyon değerlendirmesi için kullanılır; ilk basamak değildir."
                    },
                    {
                        "text": "Kanlı ishalde amip ve diğer parazitleri dışlamak için üç ayrı gün dışkı örneği toplamak, sonuçlar gelene kadar tedaviyi ertelemek",
                        "is_correct": False,
                        "scenario_update": "Örnekler toplanırken çocuğun karnı daha da gerildi; asıl etken araştırılmadı.",
                        "teaching_point": "Antibiyotik sonrası kanlı ishalde öncelikli olarak toksijenik bakteri araştırılmalıdır."
                    },
                    {
                        "text": "Mukozayı doğrudan görmek ve biyopsi almak için aynı gün sedasyonla tam kolonoskopi planlamak ve dışkı tetkiklerini sonrasına bırakmak",
                        "is_correct": False,
                        "scenario_update": "Gastroenteroloji, distandü ve toksik kolitte kolonoskopinin perforasyon riski taşıdığını belirterek işlemi reddetti.",
                        "teaching_point": "Ağır kolitte tam kolonoskopi perforasyon riski nedeniyle kaçınılır; tanı dışkı testleriyle konur."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Antibiyotik sonrası kanlı ishal, ateş, belirgin lökositoz, hipoalbüminemi, kolon dilatasyonu ve dışkıda GDH-toksin pozitifliği olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Shigella dizanterisi",
                        "is_correct": False,
                        "scenario_update": "Dışkı kültürü negatif ve tablo antibiyotik sonrası gelişti.",
                        "teaching_point": "Shigella dizanterisi salgın veya temas öyküsüyle birlikte kültürle doğrulanır."
                    },
                    {
                        "text": "Ülseratif kolit atağı",
                        "is_correct": False,
                        "scenario_update": "Öncesinde kronik bağırsak yakınması yok; tablo antibiyotik sonrası başladı ve toksin pozitif.",
                        "teaching_point": "İnflamatuvar bağırsak hastalığında da bu enfeksiyon gelişebilir; ancak öykü ve toksin pozitifliği burada enfeksiyonu gösteriyor."
                    },
                    {
                        "text": "Salmonella enterokoliti",
                        "is_correct": False,
                        "scenario_update": "Dışkı kültürü negatif, çiğ gıda öyküsü yok ve toksin pozitif.",
                        "teaching_point": "Salmonella enteritinde gıda öyküsü ve kültür pozitifliği beklenir."
                    },
                    {
                        "text": "Ağır Clostridioides difficile koliti",
                        "is_correct": True,
                        "explanation": "Antibiyotik maruziyeti, kanlı ishal, lökosit >15.000/mm³, hipoalbüminemi, kolon dilatasyonu ve toksin pozitifliği ağır psödomembranöz koliti doğrular; megakolon gelişimi açısından yakın izlem gerekir.",
                        "new_finding": "Tanı: Ağır Clostridioides difficile Koliti (psödomembranöz kolit)."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve İzlem",
                "question": "Bu çocuğun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Ağır tabloda kolona yeterli düzeyde ulaşacağını düşünerek vankomisini intravenöz yoldan başlamak ve ateş düşünce oral metronidazole geçerek tedaviyi tamamlamak",
                        "is_correct": False,
                        "scenario_update": "İntravenöz vankomisin kolon lümenine ulaşmadı; ateş ve ishal sürdü.",
                        "teaching_point": "Bu enfeksiyonda vankomisin yalnızca oral veya rektal yoldan etkilidir."
                    },
                    {
                        "text": "Diğer antibiyotikleri kesmek, oral vankomisin başlamak, sıvı-elektrolit desteği vermek, cerrahiyi bilgilendirip seri grafiyle izlemek ve su-sabunla el hijyenini anlatmak",
                        "is_correct": True,
                        "explanation": "Ağır hastalıkta ilk seçenek oral vankomisin 10 mg/kg dozunda günde dört kez (maks 125 mg) 10 gündür; fulminan tabloda doz artırılır ve intravenöz metronidazol eklenir. Megakolon ve perforasyon açısından cerrahi bilgilendirilir. Sporlar alkole dirençlidir.",
                        "new_finding": "Oral vankomisin ve sıvı tedavisi başlandı; cerrahi ekip bilgilendirildi. 72. saatte ateş düştü, dışkı sayısı azaldı ve kontrol grafide kolon çapı 4 cm'ye geriledi. Tedavi 10 güne tamamlandı."
                    },
                    {
                        "text": "Antibiyotik kullanmadan yüksek doz probiyotik başlamak, ishal kendiliğinden geçene kadar sıvı desteğiyle izlemek",
                        "is_correct": False,
                        "scenario_update": "Tedavisiz izlemde kolon çapı 6.5 cm'ye ulaştı ve fulminan tablo gelişti.",
                        "teaching_point": "Ağır hastalık mutlaka spesifik antibiyotikle tedavi edilir; probiyotikler tedavi yerine geçmez."
                    },
                    {
                        "text": "Oral metronidazol başlamak ve el hijyeni için alkol bazlı dezenfektanın yeterli olduğunu söyleyerek çocuğu ertesi gün taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Ağır hastalıkta yanıt yetersiz kaldı; kardeşte de benzer ishal başladı.",
                        "teaching_point": "Metronidazol ağır olmayan olgularda seçenektir; ağır hastalıkta oral vankomisin tercih edilir. Alkol sporları etkisizleştirmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "S53",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "11 Yaşında",
        "gender": "Kız",
        "complaint": "Göbeğin üst kısmında başlayıp sırta kuşak tarzında yayılan şiddetli karın ağrısı ve inatçı kusma",
        "history": "Kendisi anlatıyor: 'Dün akşam göbeğimin üstünde, sırtıma doğru bıçak gibi saplanan çok şiddetli bir ağrı başladı. Öne eğilip dizlerimi göğsüme çekince biraz hafifliyor, sırtüstü yatınca dayanamıyorum.' Annesi beş kez safrasız kustuğunu söylüyor. İki gün önce bir doğum günü partisinde çok yağlı yemek yemiş. Travma, ilaç kullanımı ve ailede benzer hastalık yok. Tartı: 38 kg.",
        "final_diagnosis": "Akut Pankreatit (Ödematöz İnterstisyel)",
        "disposition": "Sarı Alanda Hedefe Yönelik Sıvı Tedavisi, İntravenöz Analjezi ve Erken Enteral Beslenme Planıyla Pediatri Servisine Yatış",
        "case_pearl": "INSPPIRE kriterlerine göre tanı için şu üç bulgudan ikisi yeterlidir: uyumlu karın ağrısı, lipaz veya amilazın normalin üst sınırının en az 3 katı olması ve görüntüleme bulgusu. Çocukta en sık nedenler safra yolu hastalığı, ilaçlar, travma, sistemik hastalıklar ve genetik yatkınlıktır. Tedavinin temeli hedefe yönelik sıvı (tercihen Ringer laktat), yeterli analjezi (gerekirse opioid) ve ilk 48-72 saatte enteral beslenmedir. Profilaktik antibiyotik önerilmez; erken kontrastlı BT rutin değildir.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Analjezi",
                "question": "Sırta yayılan şiddetli epigastrik ağrısı ve inatçı kusması olan bu 11 yaşındaki kızda ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Opioidlerin safra yolu spazmı yapacağını düşünerek analjezi vermemek ve ağrının seyrini izlemek için çocuğu aç bekletmek",
                        "is_correct": False,
                        "scenario_update": "Analjezi verilmeyen çocuk saatlerce şiddetli ağrı çekti; muayene güvenilir yapılamadı.",
                        "teaching_point": "Opioidlerin bu tabloyu kötüleştirdiğine dair kanıt yoktur; yeterli analjezi verilmelidir."
                    },
                    {
                        "text": "Ağrıyı psikojenik kabul edip çocuğu sakinleştirmek için oral benzodiazepin vermek ve aileye stres yönetimi önermek",
                        "is_correct": False,
                        "scenario_update": "Sedasyon sonrası çocuk uykuya meyilli oldu; kusma ve ağrı sürdü.",
                        "teaching_point": "Organik nedenler dışlanmadan karın ağrısı psikojenik kabul edilmez."
                    },
                    {
                        "text": "Vital bulgular ve hidrasyonu değerlendirip damar yolu açmak, intravenöz analjezi vermek; karında hassasiyet, defans, sarılık ve böğürde-göbekte morarma bulgularını aramak",
                        "is_correct": True,
                        "explanation": "Şiddetli ağrı ve kusma sıvı kaybına yol açar; erken analjezi ve sıvı tedavinin temelidir. Sarılık safra yolu tıkanıklığını, böğür ve göbek çevresinde morarma hemorajik ağır tabloyu düşündürür.",
                        "new_finding": "Vital Bulgular: Ateş 37.7°C, KTA 122/dk, SS 24/dk, TA 108/68 mmHg, SpO2 %99, KDZ 2.5 sn. Öne eğilmiş oturuyor. Epigastriumda belirgin hassasiyet ve istemsiz defans; yaygın rebound yok. Bağırsak sesleri azalmış. Sarılık ve ciltte morarma yok. İntravenöz morfin sonrası ağrı skoru 9'dan 4'e indi."
                    },
                    {
                        "text": "Yağlı yemek öyküsü nedeniyle ağrıyı akut gastrite bağlayıp antiasit süspansiyon ve oral proton pompası inhibitörü vermek, ağrı azalırsa çocuğu taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Antiasit sonrası ağrı değişmedi ve çocuk yeniden kustu; tanı gecikti.",
                        "teaching_point": "Sırta yayılan, kusmayla seyreden şiddetli epigastrik ağrı basit gastritle açıklanmamalıdır."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar ve Görüntüleme",
                "question": "Analjezi ve sıvı başlanan bu çocukta hangi tetkikler öncelikli olarak istenmelidir?",
                "options": [
                    {
                        "text": "Maliyeti azaltmak için yalnızca serum amilazı istemek, değer normalin iki katından düşükse ciddi bir sorunu dışlayıp çocuğu oral beslenmeyle taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Amilaz erken dönemde normalin iki katı bulundu; lipaz bakılmadan tanı dışlanmak üzereydi.",
                        "teaching_point": "Amilaz daha az duyarlı ve özgüldür; lipaz tercih edilir."
                    },
                    {
                        "text": "Safra yolu taşını dışlamak için acil endoskopik retrograd kolanjiyopankreatografi planlamak ve kan tetkiklerini işlem sonrasına bırakmak",
                        "is_correct": False,
                        "scenario_update": "Endoskopist, safra yolu tıkanıklığı bulgusu olmadan girişimin endike olmadığını belirtti.",
                        "teaching_point": "ERCP yalnızca safra yolu tıkanıklığı veya kolanjit varlığında endikedir."
                    },
                    {
                        "text": "Ciddi bir komplikasyonu kaçırmamak için ilk saatlerde intravenöz kontrastlı batın bilgisayarlı tomografisi çekmek",
                        "is_correct": False,
                        "scenario_update": "Erken BT nekrozu güvenilir göstermedi; çocuk gereksiz radyasyon ve kontrasta maruz kaldı.",
                        "teaching_point": "Erken kontrastlı BT rutin değildir; tanı belirsizse veya 72 saat sonra komplikasyon şüphesinde kullanılır."
                    },
                    {
                        "text": "Lipaz, amilaz, karaciğer testleri, kalsiyum, trigliserit, glukoz, böbrek fonksiyonları, hemogram ve CRP istemek; batın ultrasonu yapmak",
                        "is_correct": True,
                        "explanation": "Lipaz duyarlı ve özgül belirteçtir. Kalsiyum, trigliserit ve karaciğer testleri etiyolojiye, BUN ve hemokonsantrasyon şiddete ışık tutar. Ultrason safra taşı ve safra yolu dilatasyonunu radyasyonsuz gösterir.",
                        "new_finding": "Lipaz 1380 U/L (normalin 23 katı), amilaz 860 U/L, ALT 32 U/L, AST 38 U/L, total bilirubin 0.8 mg/dL, kalsiyum 8.9 mg/dL, trigliserit 110 mg/dL, glukoz 128 mg/dL, BUN 18 mg/dL, lökosit 13.400/mm³, CRP 36 mg/L. Ultrason: pankreas gövde ve kuyruğunda ödematöz hipoekoik büyüme, minimal peripankreatik sıvı; safra kesesi ve yolları normal."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Sırta yayılan epigastrik ağrı, lipazın normalin 23 katı olması ve ultrasonda ödematöz pankreas görülen bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Akut taşlı kolesistit",
                        "is_correct": False,
                        "scenario_update": "Ultrasonda safra kesesi ve yolları normal.",
                        "teaching_point": "Kolesistitte sağ üst kadran ağrısı, Murphy bulgusu ve kese duvarı kalınlaşması görülür."
                    },
                    {
                        "text": "Akut ödematöz pankreatit",
                        "is_correct": True,
                        "explanation": "Tipik ağrı, lipazın normalin üst sınırının 3 katından fazla olması ve görüntüleme bulgusu INSPPIRE kriterlerinin üçünü de karşılar; nekroz bulgusu olmadığından ödematöz interstisyel formdur.",
                        "new_finding": "Tanı: Akut Pankreatit (ödematöz interstisyel)."
                    },
                    {
                        "text": "Perfore peptik ülser",
                        "is_correct": False,
                        "scenario_update": "Yaygın periton irritasyonu ve serbest hava yok; lipaz belirgin yüksek.",
                        "teaching_point": "Perfore ülserde ani yaygın ağrı ve diyafram altında serbest hava beklenir."
                    },
                    {
                        "text": "Diyabetik ketoasidoz",
                        "is_correct": False,
                        "scenario_update": "Glukoz 128 mg/dL, asidoz ve ketonemi yok.",
                        "teaching_point": "Karın ağrısı ve kusma metabolik nedenlerle de gelişebilir; kan şekeri ve kan gazı ayırıcı tanıda yardımcıdır."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu çocuğun tedavi planı nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Ağrı kontrol altına alındığı için sıvı tedavisini kesip çocuğu normal diyetle aynı gün taburcu etmek ve lipaz normale dönene kadar haftalık kontrol önermek",
                        "is_correct": False,
                        "scenario_update": "Evde ağrı ve kusma yeniden başladı; çocuk dehidrate olarak ertesi gün geri geldi.",
                        "teaching_point": "Lipaz düzeyi izlem kararını belirlemez; klinik iyileşme ve oral tolerans esastır."
                    },
                    {
                        "text": "Pankreası tamamen dinlendirmek için en az bir hafta oral ve nazogastrik alımı kesmek, santral kateterden total parenteral beslenme başlamak ve sıvıyı yalnızca idame hızında vermek",
                        "is_correct": False,
                        "scenario_update": "Uzun açlık ve santral kateter sonrası kateter ilişkili enfeksiyon gelişti; hastanede kalış uzadı.",
                        "teaching_point": "Uzun süreli açlık önerilmez; erken enteral beslenme daha güvenlidir."
                    },
                    {
                        "text": "Komplikasyonları önlemek için profilaktik imipenem başlamak, enzim salınımını azaltmak amacıyla oktreotid infüzyonu eklemek ve çocuğu en az bir hafta aç tutmak",
                        "is_correct": False,
                        "scenario_update": "Bu tedaviler seyri değiştirmedi; çocuk gereksiz geniş spektrumlu antibiyotiğe maruz kaldı.",
                        "teaching_point": "Profilaktik antibiyotik ve oktreotidin çocuklarda yararı gösterilmemiştir."
                    },
                    {
                        "text": "Ringer laktatla 1.5-2 kat idame hızında hedefe yönelik sıvı vermek, düzenli analjezi sürdürmek, kusma azalınca ilk 48-72 saatte enteral beslenmeye geçmek ve antibiyotik vermemek",
                        "is_correct": True,
                        "explanation": "Hedefe yönelik sıvı tedavisi pankreas perfüzyonunu korur. Erken enteral beslenme bağırsak bariyerini destekler ve hastanede kalış süresini kısaltır. Profilaktik antibiyotik enfekte nekroz riskini azaltmaz.",
                        "new_finding": "Ringer laktat ve morfin sürdürüldü. İkinci gün ağrı azaldı, düşük yağlı diyetle oral beslenme başlandı. Etiyoloji araştırması için poliklinik izlemi planlandı; çocuk beşinci gün taburcu edildi."
                    }
                ]
            }
        ]
    },
    {
        "id": "S54",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "2 Aylık",
        "gender": "Erkek",
        "complaint": "Ateş, karında aşırı şişlik, yeşil kusma, patlayıcı kötü kokulu ishal ve solukluk",
        "history": "Ailesi anlatıyor: 'Doğumdan sonra ilk kakasını ancak üçüncü gün yaptı. O günden beri hep kabız, fitille kaka yapıyordu ve karnı şişkindi. Dün aniden ateşi 38.8°C'ye çıktı, karnı balon gibi şişti. Bugün yeşil kustu, sonra bezine fışkırır gibi çok kötü kokulu, sulu kaka geldi. Emmiyor, inliyor.' Term doğmuş. Büyüme yavaş. Tartı: 4.8 kg.",
        "final_diagnosis": "Hirschsprung Hastalığı İlişkili Enterokolit",
        "disposition": "Sarı Alanda Sıvı Resüsitasyonu, Nazogastrik Dekompresyon, Geniş Spektrumlu İntravenöz Antibiyotik ve Rektal İrrigasyon ile Çocuk Yoğun Bakım ve Cerrahi İzlemi",
        "case_pearl": "Mekonyumun 48 saatten geç çıkması ve doğumdan beri süren kabızlık, distal kolonda ganglion hücresi yokluğunu düşündürür. Bu hastalarda gelişen ateş, distansiyon, patlayıcı kötü kokulu ishal ve letarji hayatı tehdit eden enterokolittir; ölümün en sık nedenidir. Tedavi resüsitasyon, dekompresyon, ampisilin-gentamisin-metronidazol gibi geniş spektrumlu antibiyotik ve serum fizyolojikle rektal irrigasyondur. Akut dönemde kontrastlı lavman yapılmaz; tanı sonradan rektal emme biyopsisiyle konur.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Resüsitasyon",
                "question": "Ateşli, distandü, safralı kusan ve patlayıcı ishali olan bu 2 aylık bebekte ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Sulu ishal nedeniyle biberonla oral rehidratasyon solüsyonu vermek, ateş için parasetamol önermek ve bebeği acil gözlem odasında iki saat izlemek",
                        "is_correct": False,
                        "scenario_update": "Bebek ORS'yi safralı kustu; gözlem sırasında perfüzyonu belirgin bozuldu.",
                        "teaching_point": "Safralı kusma, distansiyon ve letarji acil resüsitasyon gerektirir; oral deneme yapılmaz."
                    },
                    {
                        "text": "Doğumdan beri süren kabızlık öyküsü nedeniyle karın şişliğini azaltmak için yetişkin dozunda fosfatlı lavman uygulamak ve dışkılama sonrası bebeği yeniden değerlendirmek",
                        "is_correct": False,
                        "scenario_update": "Fosfatlı lavman sonrası bebekte ciddi elektrolit bozukluğu gelişti ve tablo ağırlaştı.",
                        "teaching_point": "Küçük bebekte fosfatlı lavman kontrendikedir; dekompresyon serum fizyolojikle yapılır."
                    },
                    {
                        "text": "İshali durdurmak için antimotilite damla başlamak ve karın şişliği için simetikon vermek, aileyi beslenme konusunda bilgilendirip taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Antimotilite ajan sonrası distansiyon arttı; bebek saatler sonra şokta geri getirildi.",
                        "teaching_point": "Ateşli, distandü bebekte antimotilite ajanlar tehlikelidir."
                    },
                    {
                        "text": "Havayolu, solunum ve perfüzyonu değerlendirip damar yolu açmak, izotonik sıvı bolusu vermek, kan şekeri bakmak, oral alımı kesip nazogastrik dekompresyon yapmak",
                        "is_correct": True,
                        "explanation": "Letarji, taşikardi ve uzamış kapiller dolum sepsis ve şoku düşündürür; hızlı sıvı ve dekompresyon gereklidir. Küçük bebekte hipoglisemi sık görülür.",
                        "new_finding": "Vital Bulgular: Ateş 38.7°C, KTA 164/dk, SS 46/dk, TA 74/42 mmHg, SpO2 %96, KDZ 3 sn. İniltili, soluk, letarjik. Karın ileri derecede distandü, parlak, venöz dolgunluk belirgin. Rektal muayenede anal kanal dar ve sıkı; parmak çıkarılınca patlayıcı şekilde kötü kokulu gaz ve sıvı dışkı fışkırdı. Kan şekeri 68 mg/dL. 20 mL/kg serum fizyolojik sonrası KDZ 2 sn'ye indi."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar, Görüntüleme ve Antibiyotik",
                "question": "Resüsitasyona kısmi yanıt veren bu bebekte sonraki adım nedir?",
                "options": [
                    {
                        "text": "Altta yatan yapısal nedeni göstermek için acil serviste hemen kontrastlı kolon grafisi çekmek ve antibiyotiği tanı kesinleştikten sonra başlamak",
                        "is_correct": False,
                        "scenario_update": "Radyolog, akut inflamasyonda kontrastlı lavmanın perforasyon riski taşıdığını belirterek işlemi erteledi; antibiyotik gecikti.",
                        "teaching_point": "Akut ağır kolitte kontrastlı lavman yapılmaz; antibiyotik geciktirilmez."
                    },
                    {
                        "text": "Kan kültürü, hemogram, CRP, kan gazı, laktat ve elektrolitler alıp hemen geniş spektrumlu intravenöz antibiyotik başlamak ve direkt grafi çekmek",
                        "is_correct": True,
                        "explanation": "Sepsis bulgusu olan bebekte antibiyotik kültür alındıktan sonra geciktirilmez. Anaerop ve gram negatifleri kapsayan ampisilin, gentamisin ve metronidazol uygundur. Direkt grafi dilatasyonu, geçiş noktasını ve perforasyonu gösterir.",
                        "new_finding": "Lökosit 21.400/mm³ (%20 çomak), CRP 92 mg/L, pH 7.24, laktat 3.8 mmol/L, Na 132, K 3.4 mEq/L. Ampisilin, gentamisin ve metronidazol başlandı. Direkt grafi: kolonda yaygın gaz distansiyonu, rektosigmoid bölgede gazın aniden kesilmesi, bağırsak duvarında ödem; serbest hava yok."
                    },
                    {
                        "text": "Yalnızca dışkı kültürü ve rotavirüs antijeni göndermek, viral etken olasılığı yüksek olduğu için antibiyotik vermeden sıvı tedavisiyle bebeği izlemek",
                        "is_correct": False,
                        "scenario_update": "Antibiyotiksiz izlemde laktat 5.6 mmol/L'ye yükseldi ve bebek inotrop ihtiyacıyla yoğun bakıma alındı.",
                        "teaching_point": "Ateşli, toksik ve distandü bebekte bakteriyel translokasyon ve sepsis riski yüksektir."
                    },
                    {
                        "text": "Ateşli küçük bebekte tam sepsis değerlendirmesi için önce lomber ponksiyon yapmak ve işlem tamamlanana kadar antibiyotik başlamamak",
                        "is_correct": False,
                        "scenario_update": "Lomber ponksiyon hemodinamik instabilite nedeniyle yapılamadı; antibiyotik bir saat gecikti.",
                        "teaching_point": "Stabil olmayan bebekte lomber ponksiyon ertelenir; antibiyotik beklemeden başlanır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Gecikmiş mekonyum ve doğumdan beri kabızlık öyküsü olan, ateş, distansiyon, patlayıcı kötü kokulu ishal ve rektosigmoidde geçiş noktası saptanan bu bebekte tanı nedir?",
                "options": [
                    {
                        "text": "Hirschsprung ilişkili enterokolit",
                        "is_correct": True,
                        "explanation": "Gecikmiş mekonyum, kronik kabızlık, rektal muayenede patlayıcı boşalma ve rektosigmoidde geçiş noktası altta yatan aganglionozu; ateş, distansiyon ve kötü kokulu ishal ise hayatı tehdit eden enterokoliti gösterir.",
                        "new_finding": "Tanı: Hirschsprung Hastalığı İlişkili Enterokolit."
                    },
                    {
                        "text": "Salmonella sepsisi",
                        "is_correct": False,
                        "scenario_update": "Kronik kabızlık, gecikmiş mekonyum ve rektosigmoidde geçiş noktası enfeksiyonla açıklanmaz.",
                        "teaching_point": "Altta yatan yapısal sorun tekrarlayan ağır tabloların nedenidir ve atlanmamalıdır."
                    },
                    {
                        "text": "Nekrotizan enterokolit",
                        "is_correct": False,
                        "scenario_update": "Term ve 2 aylık bebek; grafide pnömatozis yok ve öykü doğumdan beri süren kabızlığı gösteriyor.",
                        "teaching_point": "Nekrotizan enterokolit çoğunlukla prematürelerde, ilk haftalarda görülür."
                    },
                    {
                        "text": "Malrotasyon ve orta bağırsak volvulusu",
                        "is_correct": False,
                        "scenario_update": "Distal kolon tutulumu ve kronik kabızlık öyküsü var; proksimal duodenal tıkanıklık bulgusu yok.",
                        "teaching_point": "Volvulus ani başlangıçlı safralı kusmayla seyreder ve kronik kabızlık öyküsü beklenmez."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Yatış",
                "question": "Bu bebeğin acil tedavisi nasıl sürdürülmelidir?",
                "options": [
                    {
                        "text": "Antibiyotik ve sıvıyı sürdürüp rektal tüple serum fizyolojik irrigasyonu yapmak, dekompresyona devam etmek ve yoğun bakım-cerrahi izlemine almak",
                        "is_correct": True,
                        "explanation": "Rektal irrigasyon kolonun dekompresyonunu ve bakteri yükünün azalmasını sağlar. Yanıt alınamazsa saptırıcı kolostomi gerekir. Akut dönem sonrasında rektal emme biyopsisiyle tanı doğrulanır ve kesin cerrahi planlanır.",
                        "new_finding": "Günde iki kez 10-20 mL/kg serum fizyolojikle rektal irrigasyon yapıldı. 48 saatte ateş düştü, distansiyon azaldı. Rektal emme biyopsisinde ganglion hücresi saptanmadı; çocuk cerrahisi düzeltici ameliyat planladı."
                    },
                    {
                        "text": "Ateş düşünce intravenöz antibiyotiği oral metronidazole çevirip bebeği evde fitil uygulamasıyla izleme almak",
                        "is_correct": False,
                        "scenario_update": "Evde distansiyon yeniden arttı; bebek iki gün sonra tekrar enterokolitle başvurdu.",
                        "teaching_point": "Enterokolit atakları tekrarlayabilir; dekompresyon ve kesin tanı yapılmadan taburculuk uygun değildir."
                    },
                    {
                        "text": "Kolonu hızla boşaltmak için yüksek hacimli fosfatlı lavmanları günde birkaç kez tekrarlamak ve ateş düşünce antibiyotiği kesmek",
                        "is_correct": False,
                        "scenario_update": "Fosfatlı lavmanlar sonrası ciddi hiperfosfatemi ve hipokalsemi gelişti.",
                        "teaching_point": "İrrigasyon izotonik serum fizyolojikle yapılır; fosfatlı lavman bebekte toksiktir."
                    },
                    {
                        "text": "Kesin çözüm için bebeği aynı gün düzeltici ameliyata almak, hasarlı kolon segmentini çıkarıp tek seansta primer anastomoz yapmak",
                        "is_correct": False,
                        "scenario_update": "Aktif enterokolit ve sepsis sırasında yapılan cerrahi yüksek komplikasyon riski taşıdı; cerrahi ekip ameliyatı erteledi.",
                        "teaching_point": "Kesin cerrahi akut enterokolit tedavi edildikten sonra planlanır."
                    }
                ]
            }
        ]
    },
    {
        "id": "S55",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "4 Yaşında",
        "gender": "Kız",
        "complaint": "Gözlerde ve ciltte sararma, sürekli uyuklama, kusma, diş eti kanaması ve vücutta morluklar",
        "history": "Ailesi anlatıyor: 'Bir hafta önce halsizlik ve bulantı başladı. İki gündür gözlerinin akı ve cildi sarardı, idrarı çay rengi oldu. Bu sabahtan beri sürekli uyumak istiyor, uyandırınca anlamsız bakıyor, beni zor tanıyor. Dişlerini fırçalarken diş eti kanadı, bacaklarında kendiliğinden morluklar çıktı.' Evde parasetamol şurubunu önerilen dozda yalnızca iki kez vermişler. Mantar yeme veya bitkisel ürün öyküsü yok. Tartı: 16 kg.",
        "final_diagnosis": "Pediatrik Akut Karaciğer Yetmezliği (Evre 2 Ensefalopati)",
        "disposition": "Sarı Alanda Hipoglisemi Tedavisi, İntravenöz K Vitamini, Sedatiflerden Kaçınma ve Karaciğer Nakil Merkezi Olan Çocuk Yoğun Bakıma Acil Sevk",
        "case_pearl": "Tanım: bilinen kronik karaciğer hastalığı olmayan çocukta akut karaciğer hasarı ile birlikte K vitaminine yanıtsız INR ≥1.5 ve ensefalopati, ya da ensefalopati olmasa bile INR ≥2. Çocuklarda ensefalopati sinsi ve geç bulgu olabilir. Hipoglisemi sıktır ve sık izlenmelidir. Taze donmuş plazma yalnızca kanama veya girişim için verilir; INR'yi rutin düzeltmek prognostik değerini bozar. Sedatiflerden kaçınılır. Nakil merkeziyle erken iletişim sağkalımı belirler.",
        "steps": [
            {
                "stage_title": "İlk Değerlendirme ve Acil Müdahale",
                "question": "Sarılık, bilinç bulanıklığı ve kanama bulguları olan bu 4 yaşındaki çocukta ilk yaklaşımınız nedir?",
                "options": [
                    {
                        "text": "Havayolu ve solunumu değerlendirip kapiller kan şekeri bakmak, damar yolu açmak, bilinç düzeyini kaydetmek, kanama bulgularını ve ilaç-toksin maruziyetini sorgulamak",
                        "is_correct": True,
                        "explanation": "Bilinç bulanıklığında hipoglisemi hızla düzeltilebilir bir nedendir. Başlangıç bilinç düzeyi kötüleşmeyi izlemek için referanstır. Parasetamol, mantar ve bitkisel ürünler etiyolojiyi ve özgül tedaviyi belirler.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 110/dk, SS 22/dk, TA 98/58 mmHg, SpO2 %99. Kapiller kan şekeri 56 mg/dL; 2 mL/kg %10 dekstroz verildi. Derin sarılık. Sesli uyaranla gözlerini açıyor, konfüze, annesini zor tanıyor; asteriksis var. Karaciğer kot kavsini 4 cm geçiyor ve hassas. Bacaklarda ekimozlar, diş etinde sızıntı tarzında kanama. Dalak ele gelmiyor, asit yok."
                    },
                    {
                        "text": "Sarılığı basit viral hepatite bağlayıp evde oral sıvı ve yatak istirahati önermek, kanama bulgularını trombositopeniye bağlayıp çocuğu hematoloji polikliniğine yönlendirmek",
                        "is_correct": False,
                        "scenario_update": "Hipoglisemi ve bilinç değişikliği atlandı; çocuk konvülziyon geçirerek geri getirildi.",
                        "teaching_point": "Sarılıkla birlikte bilinç değişikliği ve kanama ağır karaciğer hasarının işaretidir."
                    },
                    {
                        "text": "Diş eti kanaması ve ekimozlar nedeniyle tetkik sonuçlarını beklemeden hemen 20 mL/kg taze donmuş plazma ve trombosit süspansiyonu vermek",
                        "is_correct": False,
                        "scenario_update": "Plazma sonrası INR düzeldi ancak sevk merkezinde prognostik değerlendirme güçleşti; çocukta sıvı yüklenmesi gelişti.",
                        "teaching_point": "Taze donmuş plazma ciddi kanama veya girişim için verilir; rutin INR düzeltmesi önerilmez."
                    },
                    {
                        "text": "Huzursuzluk ve konfüzyon nedeniyle muayeneyi kolaylaştırmak için çocuğu intravenöz midazolam ile sakinleştirmek ve ardından ayrıntılı sistemik muayene yapmak",
                        "is_correct": False,
                        "scenario_update": "Midazolam sonrası çocuk derin uykuya daldı; nörolojik değerlendirme yapılamadı ve solunumu yüzeyelleşti.",
                        "teaching_point": "Bilinç bulanıklığı olan karaciğer hastasında sedatifler ensefalopatiyi ağırlaştırır ve izlemi engeller."
                    }
                ]
            },
            {
                "stage_title": "Laboratuvar ve Sentez Fonksiyonu",
                "question": "Hipoglisemisi düzeltilen bu çocukta hangi tetkikler öncelikli olarak istenmelidir?",
                "options": [
                    {
                        "text": "Bilinç değişikliği nedeniyle kafa içi kanamayı dışlamak için önce kontrastsız beyin tomografisi çekmek, ardından karaciğer testlerini istemek",
                        "is_correct": False,
                        "scenario_update": "Tomografi normal geldi; sentez fonksiyonu ve amonyak bir saat geç değerlendirildi.",
                        "teaching_point": "Sarılıklı çocukta bilinç değişikliğinin en olası nedeni metabolik olup ilk tetkikler laboratuvardır."
                    },
                    {
                        "text": "INR, transaminazlar, bilirubin, glukoz, amonyak, elektrolitler, kan gazı, laktat, kreatinin, kan grubu ve parasetamol düzeyi istemek; INR'yi K vitamini sonrası tekrarlamak",
                        "is_correct": True,
                        "explanation": "K vitaminine yanıtsız koagülopati sentez yetersizliğini gösterir. Amonyak, laktat ve kreatinin prognozu ve yoğun bakım ihtiyacını belirler. Kan grubu olası nakil ve transfüzyon için, parasetamol düzeyi özgül tedavi için gereklidir.",
                        "new_finding": "ALT 2460 U/L, AST 3100 U/L, total bilirubin 9.6 mg/dL, direkt 6.8 mg/dL, INR 2.6 (10 mg intravenöz K vitamini sonrası 2.5), amonyak 118 µmol/L, laktat 3.1 mmol/L, kreatinin 0.4 mg/dL, trombosit 142.000/mm³. Parasetamol düzeyi saptanamayacak kadar düşük. Viral seroloji ve otoimmün belirteçler gönderildi."
                    },
                    {
                        "text": "Yalnızca bilirubin ve transaminazları isteyip ALT 1000 U/L'nin üzerindeyse ursodeoksikolik asit ve silimarin gibi hepatoprotektif tedavi başlayarak çocuğu servise yatırmak",
                        "is_correct": False,
                        "scenario_update": "Sentez fonksiyonu bakılmadı; çocuk serviste izlenirken bilinci daha da bozuldu.",
                        "teaching_point": "Prognozu transaminaz değil INR, bilinç düzeyi ve glukoz belirler."
                    },
                    {
                        "text": "Etiyolojiyi kesinleştirmek için aynı gün acil perkütan karaciğer biyopsisi planlamak ve tüm tedavi kararlarını biyopsi sonucuna göre vermek",
                        "is_correct": False,
                        "scenario_update": "Koagülopatisi olan çocukta biyopsi ciddi kanama riski taşıdığı için işlem iptal edildi.",
                        "teaching_point": "Koagülopatide perkütan biyopsi kontrendikedir; gerekirse transjuguler yol seçilir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Kronik karaciğer hastalığı olmayan, K vitaminine yanıtsız INR 2.5, konfüzyon ve asteriksis, hipoglisemi ve yüksek amonyağı olan bu çocukta tanı nedir?",
                "options": [
                    {
                        "text": "Ağır seyirli akut viral hepatit",
                        "is_correct": False,
                        "scenario_update": "Hepatit tablosunun ötesinde, K vitaminine yanıtsız koagülopati ve ensefalopati var.",
                        "teaching_point": "Sentez yetersizliği ve ensefalopati eklendiğinde tablo yetmezlik olarak tanımlanır."
                    },
                    {
                        "text": "Reye sendromu",
                        "is_correct": False,
                        "scenario_update": "Salisilat maruziyeti yok ve belirgin sarılık var; Reye sendromunda sarılık genellikle yoktur.",
                        "teaching_point": "Reye sendromu viral enfeksiyon sırasında aspirin kullanımı sonrası ensefalopati ve mikroveziküler yağlanmayla seyreder."
                    },
                    {
                        "text": "Akut karaciğer yetmezliği (evre 2 ensefalopati)",
                        "is_correct": True,
                        "explanation": "Kronik hastalığı olmayan çocukta akut hepatosellüler hasar, K vitaminine yanıtsız INR ≥1.5 ve ensefalopati pediatrik akut karaciğer yetmezliği tanımını karşılar; konfüzyon ve asteriksis evre 2 ensefalopatiyle uyumludur.",
                        "new_finding": "Tanı: Pediatrik Akut Karaciğer Yetmezliği (evre 2 hepatik ensefalopati)."
                    },
                    {
                        "text": "Sepsise bağlı yaygın damar içi pıhtılaşma",
                        "is_correct": False,
                        "scenario_update": "Ateş ve enfeksiyon odağı yok; trombosit sayısı korunmuş ve tablo karaciğer kaynaklı.",
                        "teaching_point": "Yaygın damar içi pıhtılaşmada trombositopeni ve fibrinojen tüketimi ön plandadır."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Sevk",
                "question": "Bu çocuğun acil serviste tedavisi ve yönlendirmesi nasıl olmalıdır?",
                "options": [
                    {
                        "text": "Laktüloz başlamak, proteini tamamen kısıtlamak ve çocuğu genel pediatri servisinde günlük INR takibiyle izleyip kötüleşirse sevk etmek",
                        "is_correct": False,
                        "scenario_update": "Serviste ensefalopati evre 3'e ilerledi; sevk için entübasyon gerekti ve nakil değerlendirmesi gecikti.",
                        "teaching_point": "Ensefalopatili akut yetmezlikte sevk kötüleşmeyi beklemeden yapılır; protein tamamen kısıtlanmaz."
                    },
                    {
                        "text": "Karaciğer hücrelerini korumak için N-asetilsistein ve yüksek doz metilprednizolon başlamak, INR'yi taze donmuş plazmayla normal düzeye getirip sevki ertelemek",
                        "is_correct": False,
                        "scenario_update": "Plazma ile düzeltilen INR sevk kararını geciktirdi; steroid ve N-asetilsistein seyri değiştirmedi.",
                        "teaching_point": "Parasetamol dışı nedenlerde N-asetilsisteinin çocukta yararı gösterilmemiştir; INR'nin rutin düzeltilmesi önerilmez."
                    },
                    {
                        "text": "Ensefalopati nedeniyle hava yolunu güvenceye almak için hemen entübe edip derin sedasyon başlamak ve beyin ödemini önlemek için rutin mannitol infüzyonu vermek",
                        "is_correct": False,
                        "scenario_update": "Hava yolunu koruyabilen çocuk gereksiz yere entübe edildi; derin sedasyon nörolojik izlemi engelledi.",
                        "teaching_point": "Entübasyon evre 3-4 ensefalopati veya hava yolu korunamadığında yapılır; mannitol kafa içi basınç artışı bulgusunda verilir."
                    },
                    {
                        "text": "Dekstrozlu sıvıyla kan şekerini 70 mg/dL üstünde tutmak, K vitamini vermek, sedatiflerden kaçınmak, başı yükseltmek ve nakil merkezine acil sevk etmek",
                        "is_correct": True,
                        "explanation": "Hipoglisemi sıktır ve sürekli dekstroz gerekir. Sedatifler ensefalopatiyi maskeler. Baş yükseltme kafa içi basıncı azaltır. Ensefalopatili akut yetmezlikte nakil merkezinin erken katılımı sağkalımı belirler.",
                        "new_finding": "%10 dekstrozlu izotonik sıvı, intravenöz K vitamini ve pantoprazol başlandı; saatlik kan şekeri ve nörolojik izlem yapıldı. Nakil merkeziyle görüşülerek çocuk yoğun bakım ambulansıyla sevk edildi; orada nakil listesine alındı."
                    }
                ]
            }
        ]
    }
]
