# -*- coding: utf-8 -*-
"""
Yeşil Alan Vakaları - Y86-Y90 (GİS, Nörolojik Belirtiler, Kas-İskelet ve Genital)
"""

SPOILERS = {
    "Y86": [
        "şigel",
        "shigella",
        "basilli dizanteri"
    ],
    "Y87": [
        "katılma",
        "nefes tutma",
        "breath-holding"
    ],
    "Y88": [
        "bell",
        "idiyopatik fasiyal"
    ],
    "Y89": [
        "kas kaynaklı tortikolis",
        "postüral tortikolis",
        "muskuler tortikolis"
    ],
    "Y90": [
        "balanopostit",
        "balanit",
        "postit"
    ]
}

CASES = [
    {
        "id": "Y86",
        "category": "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
        "age": "4 Yaşında (16 kg)",
        "gender": "Kız",
        "complaint": "Dünden beri yüksek ateş, kıvrandıran karın ağrısı ve günde on kez az miktarda kanlı-sümüksü dışkılama",
        "history": "Annesi anlatıyor: 'Dün öğlen ateşi 39.5°C'ye çıktı, karnına kramp girer gibi ağrıyor. Sonra çok sık tuvalete gitmeye başladı, her seferinde az miktarda kanlı, sümüklü dışkı yapıyor, ıkınıyor ama çıkmıyor.' Kreşte iki çocukta da ishal varmış. Kusma bir kez olmuş. İdrarını yapıyor. Havale geçirmemiş. Antibiyotik kullanmamış. Çiğ köfte veya az pişmiş et yemesi yok. Aşıları tam.",
        "final_diagnosis": "Şigelloz (Shigella sonnei Dizanterisi)",
        "disposition": "Oral Azitromisin, Ağızdan Rehidratasyon ve Kreş Kısıtlamasıyla Yeşil Alandan Taburculuk",
        "case_pearl": "Ateş, kramp tarzında karın ağrısı, tenezm ve sık, az miktarda kanlı-mukuslu dışkı dizanteriyi düşündürür. Antibiyotik öncesi dışkı kültürü ve Shiga toksin testi gönderilmelidir; STEC enfeksiyonunda antibiyotik HÜS riskini artırabilir. Kanlı ishalde hemogram ve kreatinin HÜS taraması için faydalıdır. Türkiye'de ampisilin ve trimetoprim-sülfametoksazol direnci yüksektir. İlk seçenek azitromisindir (ilk gün 12 mg/kg, ardından 4 gün 6 mg/kg). Antimotilite ajanlardan kaçınılır.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Ateş ve kanlı dışkısı olan bu çocukta ilk değerlendirmede neye odaklanırsınız?",
                "options": [
                    {
                        "text": "Dehidratasyonu, genel görünümü ve karın muayenesini değerlendirmek; solukluk, idrar azlığı, ödem ve nöbet öyküsünü sorgulamak",
                        "is_correct": True,
                        "explanation": "Kanlı ishalde dehidratasyonun yanında karın içi cerrahi nedenler, nörolojik tutulum ve böbrek tutulumunu düşündüren solukluk-idrar azlığı sorgulanmalıdır.",
                        "new_finding": "Vital Bulgular: Ateş 39.2°C, KTA 138/dk, SS 24/dk, TA 96/58 mmHg, KDZ 2 sn. Mukozalar hafif kuru, göz yaşı var. Karında alt kadranlarda yaygın hassasiyet, defans ve kitle yok, bağırsak sesleri artmış. Bezde az miktarda mukuslu, kanlı dışkı. Solukluk, ödem, peteşi yok. Bilinç açık, ense sertliği yok. Son 6 saatte iki kez idrar yapmış."
                    },
                    {
                        "text": "Dışkıdaki kan nedeniyle invajinasyon olasılığıyla muayeneyi kısa tutup acil batın ultrasonografisi ve çocuk cerrahisi konsültasyonu istemek",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografi normal geldi; yüksek ateşli ve sık dışkılamalı çocukta asıl tablo saatler sonra değerlendirilebildi.",
                        "teaching_point": "Yüksek ateş, tenezm ve sık mukuslu dışkılama enfeksiyöz bir tabloyu düşündürür; önce tam klinik değerlendirme yapılmalıdır."
                    },
                    {
                        "text": "İshali azaltmak için hemen loperamid ve probiyotik vermek, karın ağrısı için buscopan yapıp ağrı geçince değerlendirmeye karar vermek",
                        "is_correct": False,
                        "scenario_update": "Loperamid sonrası karında şişlik ve ateşte artış oldu.",
                        "teaching_point": "Kanlı ve ateşli ishalde antimotilite ajanları toksin ve bakteri klirensini azaltır, komplikasyon riskini artırır."
                    },
                    {
                        "text": "Ateşli kanlı ishali olduğu için muayene sonrası tetkik beklemeden ampirik oral trimetoprim-sülfametoksazol başlayıp ertesi gün kontrole çağırmak",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik öncesi kültür alınmadı; ilaca rağmen ateş ve dışkılama sürdü.",
                        "teaching_point": "Antibiyotik öncesi dışkı kültürü ve Shiga toksin testi alınmalıdır; bölgedeki direnç oranları ilaç seçimini belirler."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Bu çocukta hangi tetkikleri istersiniz?",
                "options": [
                    {
                        "text": "Yalnızca dışkıda gizli kan ve rotavirüs-adenovirüs antijeni bakmak, kültür istemeden viral gastroenterit olarak izlemek ve evde izlem önermek",
                        "is_correct": False,
                        "scenario_update": "Gizli kan pozitif, viral antijenler negatif geldi; etken saptanmadı ve tedavi planlanamadı.",
                        "teaching_point": "Kanlı-ateşli ishalde bakteriyel kültür ve Shiga toksin testi gerekir; viral antijenler yeterli değildir."
                    },
                    {
                        "text": "Dışkı mikroskopisi, kültür ve Shiga toksin testi göndermek; kanlı ishal nedeniyle hemogram ve kreatinin istemek",
                        "is_correct": True,
                        "explanation": "Kültür etkeni ve duyarlılığı gösterir. Shiga toksin testi STEC'i dışlar. Hemogram ve kreatinin hemoliz, trombositopeni ve böbrek tutulumu açısından temel değerlendirmeyi sağlar.",
                        "new_finding": "Dışkı mikroskopisi: her alanda bol lökosit ve eritrosit. Shiga toksin PCR negatif. Lökosit 14.800/mm³ (çomak %18), Hb 12.4 g/dL, trombosit 286.000/mm³, kreatinin 0.38 mg/dL, Na 136 mmol/L. 48 saat sonra dışkı kültüründe laktoz fermente etmeyen, hareketsiz gram negatif basil üredi; ampisilin ve trimetoprim-sülfametoksazole dirençli, azitromisine duyarlı."
                    },
                    {
                        "text": "Ağrıyı değerlendirmek için kontrastlı batın bilgisayarlı tomografisi istemek ve sonucuna göre dışkı tetkiklerini planlamak",
                        "is_correct": False,
                        "scenario_update": "Tomografi kalın bağırsak duvarında yaygın kalınlaşma gösterdi; etken ve tedavi seçimi için bilgi vermedi.",
                        "teaching_point": "Enfeksiyöz kolitte görüntüleme etkeni göstermez; dışkı tetkikleri tanının temelidir."
                    },
                    {
                        "text": "Kan kültürü, CRP ve prokalsitonin istemek; prokalsitonin yüksekse intravenöz seftriaksonla servise yatırmak",
                        "is_correct": False,
                        "scenario_update": "Prokalsitonin 1.2 ng/mL geldi ve çocuk yatırıldı; dışkı kültürü alınmadığı için etken bilinmedi.",
                        "teaching_point": "Genel durumu iyi çocukta parenteral tedavi gerekmez; dışkı kültürü atlanmamalıdır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {
                        "text": "STEC enfeksiyonu",
                        "is_correct": False,
                        "scenario_update": "Shiga toksin PCR negatifti ve yüksek ateş vardı.",
                        "teaching_point": "STEC enfeksiyonunda ateş genellikle yoktur veya hafiftir, Shiga toksin pozitiftir."
                    },
                    {
                        "text": "Şigelloz (basilli dizanteri)",
                        "is_correct": True,
                        "explanation": "Yüksek ateş, tenezm, sık az miktarda kanlı-mukuslu dışkı, dışkıda bol lökosit, kreş salgını ve kültürde üreme şigellozu gösterir.",
                        "new_finding": "Tanı: Şigelloz (S. sonnei)."
                    },
                    {
                        "text": "İleokolik invajinasyon",
                        "is_correct": False,
                        "scenario_update": "Ateş yüksekti, karında kitle yoktu ve dışkıda bol lökosit vardı.",
                        "teaching_point": "İnvajinasyonda aralıklı ağlama krizleri, kitle ve çilek jölesi dışkı görülür; yüksek ateş beklenmez."
                    },
                    {
                        "text": "Kampilobakter enteriti",
                        "is_correct": False,
                        "scenario_update": "Kültürde kampilobakter değil şigella üredi, kreş salgını vardı.",
                        "teaching_point": "Kampilobakter sıklıkla az pişmiş tavuk ile ilişkilidir ve kültürle ayırt edilir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Ampirik olarak ampisilin 100 mg/kg/gün 5 gün başlamak ve ishali hızla kesmek için racekadotril ile loperamidi birlikte önermek",
                        "is_correct": False,
                        "scenario_update": "Ampisiline dirençli suşta ateş ve dışkılama sürdü; loperamid karın şişkinliğine neden oldu.",
                        "teaching_point": "Ülkemizde ampisilin direnci yüksektir. Antimotilite ajanları dizanteride kontrendikedir."
                    },
                    {
                        "text": "Antibiyotiğin taşıyıcılığı uzatacağını düşünerek hiç antibiyotik vermeden yalnız sıvı önermek ve ishal geçer geçmez kreşe göndermek",
                        "is_correct": False,
                        "scenario_update": "Ateş ve dizanteri bir hafta sürdü, kreşte üç çocuk daha hastalandı.",
                        "teaching_point": "Şigellozda antibiyotik hastalık süresini ve bulaşı azaltır; kreşe dönüş kurallara göre planlanmalıdır."
                    },
                    {
                        "text": "Azitromisin ilk gün 12 mg/kg, sonra 4 gün 6 mg/kg vermek; ağızdan rehidratasyon ve el hijyeni önermek, ishal geçene dek kreşe göndermemek",
                        "is_correct": True,
                        "explanation": "Azitromisin duyarlı suşlarda etkilidir ve çocuklarda ilk seçenektir. El hijyeni ev içi bulaşı azaltır. Kreşe dönüş için ishalin bitmesi ve yerel kurallara göre kültür kontrolü gerekebilir.",
                        "new_finding": "Azitromisin başlandı. 48. saatte ateş düştü, dışkı sayısı günde üçe indi. Beşinci gün dışkı normale döndü; kreşe dönüş halk sağlığı önerisine göre planlandı."
                    },
                    {
                        "text": "Ateş ve kan olduğu için 10 gün oral siprofloksasin ile birlikte metronidazol vermek ve iki hafta boyunca süt ürünlerini kesmek ve probiyotik eklemek",
                        "is_correct": False,
                        "scenario_update": "Gereksiz geniş kombinasyon ve uzun süre bulantı ve iştahsızlık yaptı; süt kısıtlaması beslenmeyi bozdu.",
                        "teaching_point": "Tek ve uygun ajanla kısa tedavi yeterlidir; rutin laktoz kısıtlaması gerekmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y87",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "15 Aylık (10 kg)",
        "gender": "Erkek",
        "complaint": "Ağlarken morarıp bayılma ve kısa süreli kasılma atakları",
        "history": "Annesi çok korkmuş: 'Bugün oyuncağını aldığımda çok ağladı, ağlarken sesi kesildi, dudakları morardı, sonra gevşeyip yere yığıldı. Birkaç kez kolları kasıldı, bir dakika içinde ağlayarak kendine geldi, sonra biraz uyudu.' Benzer atak son iki ayda üç kez olmuş, hepsi düştüğünde veya kızdığında. Ateş yok. Gelişimi normal. Günde 1 litreden fazla inek sütü içiyor, et ve sebze yemiyor. Ailede ani ölüm veya epilepsi yok.",
        "final_diagnosis": "Siyanotik Katılma Nöbeti (Demir Eksikliği Anemisi Eşlikli)",
        "disposition": "Demir Tedavisi, Beslenme Düzenlemesi ve Aile Eğitimiyle Yeşil Alandan Taburculuk",
        "case_pearl": "Katılma nöbeti genellikle 6-18 ay arasında başlar. Ağlama veya ağrı gibi bir tetikleyicinin ardından ekspiryumda soluk tutma, siyanoz, bilinç kaybı ve bazen kısa kasılmalarla seyreder; nöbet tetikleyiciden önce başlamaz. Tanı öyküyle konur. Demir eksikliği sık eşlik eder ve demir tedavisi atak sıklığını azaltır. Tetikleyicisi belirsiz, solgun tip veya egzersizle gelen ataklarda EKG ile uzun QT dışlanmalıdır. Antiepileptik gerekmez. Ataklar genellikle 5-6 yaşta kaybolur.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Öykü",
                "question": "Ağlarken morarıp bayılan bu çocukta ilk değerlendirmede en önemli adım nedir?",
                "options": [
                    {
                        "text": "Olayın sırasını ayrıntılı sorgulamak; tetikleyici, ağlama, ses kesilmesi, morarma ve bilinç kaybının sırasını ve süresini öğrenip tam fizik muayene yapmak",
                        "is_correct": True,
                        "explanation": "Tanı öyküye dayanır: tetikleyicinin olaydan önce gelmesi ve olayların sırası nöbetten ayırt ettirir. Solukluk ve muayene anemi gibi eşlik eden durumları gösterebilir.",
                        "new_finding": "Vital Bulgular: Ateş 36.7°C, KTA 118/dk, SS 26/dk, SpO2 %99. Çocuk aktif ve oynuyor. Konjonktivalar ve avuç içleri soluk. Kalp sesleri ritmik, üfürüm yok. Nörolojik muayene yaşına uygun, fokal bulgu yok. Annenin telefonundaki videoda: şiddetli ağlama, ekspiryumda sesin kesilmesi, dudaklarda morarma, gevşeme, iki kez kol kasılması ve 50 saniye içinde ağlayarak uyanma görülüyor."
                    },
                    {
                        "text": "Kasılma tarif edildiği için epileptik nöbet kabul edip hemen intravenöz levetirasetam yüklemesi yapmak ve nöroloji konsültasyonu istemek ve gece gözlemde tutmak",
                        "is_correct": False,
                        "scenario_update": "Levetirasetam yüklendi; videoyu izleyen nörolog olayın epileptik olmadığını belirtti.",
                        "teaching_point": "Tetikleyici ile başlayan morarma ve bilinç kaybını izleyen kısa kasılmalar beyin hipoksisine bağlıdır; antiepileptik endikasyonu yoktur."
                    },
                    {
                        "text": "Olayın bitmiş olduğunu ve çocuğun iyi göründüğünü belirterek öykü sorgulamadan ve muayene etmeden aileyi rahatlatıp eve göndermek",
                        "is_correct": False,
                        "scenario_update": "Aile yeniden atak olduğunda panikle 112'yi aradı; anemi saptanmadı ve tedavi edilmedi.",
                        "teaching_point": "Her iyi görünen çocukta bile öykü ve muayene gerekir; eşlik eden anemi ve kardiyak nedenler atlanmamalıdır."
                    },
                    {
                        "text": "Morarma nedeniyle doğuştan kalp hastalığını dışlamak için öyküyü kısa tutup acil ekokardiyografi istemek ve kardiyoloji yatışı planlamak",
                        "is_correct": False,
                        "scenario_update": "Ekokardiyografi normal geldi; çocuk gereksiz yere yatırıldı.",
                        "teaching_point": "Yalnızca ağlama sırasında olan geçici morarmada yapısal kalp hastalığı beklenmez; öykü ve muayene yönlendirir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Bu çocukta hangi tetkikler uygundur?",
                "options": [
                    {
                        "text": "Uyku deprivasyonlu EEG ve kraniyal MR planlamak, sonuçları gelene kadar ailenin evde çocuğun ağlamasını engellemesini önermek ve nörolojiye sevk etmek",
                        "is_correct": False,
                        "scenario_update": "EEG ve MR normal geldi; sedasyon ve bekleme süresi aileyi yordu.",
                        "teaching_point": "Tipik öyküde EEG ve görüntüleme tanıya katkı sağlamaz."
                    },
                    {
                        "text": "Tam kan sayımı, ferritin ve EKG istemek; EKG'de QTc ve ritmi değerlendirip normal ise ek tetkik planlamamak",
                        "is_correct": True,
                        "explanation": "Demir eksikliği sık eşlik eder ve tedavisi atakları azaltır. EKG uzun QT gibi kardiyak senkop nedenlerini dışlamak için basit bir tetkiktir.",
                        "new_finding": "Hb 9.6 g/dL, MCV 62 fL, RDW %18, trombosit 412.000/mm³, ferritin 5 ng/mL. EKG: sinüs ritmi, QTc 410 ms, preeksitasyon yok."
                    },
                    {
                        "text": "Elektrolit, kalsiyum, magnezyum, glukoz, amonyak, laktat ve metabolik tarama testlerini kapsayan geniş bir panel istemek",
                        "is_correct": False,
                        "scenario_update": "Tüm metabolik testler normal geldi; asıl eşlik eden sorun olan demir eksikliği bakılmadı.",
                        "teaching_point": "Tetkikler öykü ve muayeneye göre seçilmelidir; geniş metabolik panel bu tabloda gereksizdir."
                    },
                    {
                        "text": "Lomber ponksiyon yapıp BOS incelemesi ve kültür istemek, sonuç gelene kadar çocuğu gözlem altında tutmak",
                        "is_correct": False,
                        "scenario_update": "BOS normal geldi; ateşsiz ve iyi görünen çocuğa gereksiz invaziv girişim yapıldı.",
                        "teaching_point": "Ateş ve meningeal bulgu olmadan BOS incelemesi endike değildir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Öykü ve tetkiklere göre en olası tanınız nedir?",
                "options": [
                    {
                        "text": "Siyanotik katılma nöbeti",
                        "is_correct": True,
                        "explanation": "Kızgınlık veya düşmeyle tetiklenen ağlama, ekspiryumda soluk kesilmesi, siyanoz, kısa bilinç kaybı ve hızlı düzelme siyanotik katılma nöbetini gösterir. Demir eksikliği anemisi eşlik etmektedir.",
                        "new_finding": "Tanı: Siyanotik katılma nöbeti, demir eksikliği anemisi."
                    },
                    {
                        "text": "Fokal epileptik nöbet",
                        "is_correct": False,
                        "scenario_update": "Olaylar her zaman tetikleyiciyle başlamış, kasılmalar morarma ve bilinç kaybından sonra gelmişti.",
                        "teaching_point": "Epileptik nöbetler tetikleyiciye bağlı değildir ve siyanoz nöbetin sonucudur, nedeni değil."
                    },
                    {
                        "text": "Uzun QT sendromuna bağlı senkop",
                        "is_correct": False,
                        "scenario_update": "EKG'de QTc normaldi ve ailede ani ölüm yoktu.",
                        "teaching_point": "Uzun QT senkopu egzersiz, ani ses veya yüzme ile tetiklenebilir; EKG tanı koydurur."
                    },
                    {
                        "text": "Basit febril konvülziyon",
                        "is_correct": False,
                        "scenario_update": "Ataklar sırasında ateş yoktu.",
                        "teaching_point": "Febril konvülziyon için ateş gerekir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun plan hangisidir?",
                "options": [
                    {
                        "text": "Atakları önlemek için çocuğun her isteğini yerine getirmelerini ve ağlamasına hiç izin vermemelerini önermek, ek tedavi planlamamak",
                        "is_correct": False,
                        "scenario_update": "Ataklar azalmadı ve çocukta davranış sorunları başladı.",
                        "teaching_point": "Ataklardan korkup her isteği yerine getirmek davranışı pekiştirir; tutarlı ebeveyn yaklaşımı önerilir."
                    },
                    {
                        "text": "Atak sırasında çocuğu sarsmalarını, yüzüne soğuk su serpmelerini ve ağızdan suni solunum yapmalarını öğretmek",
                        "is_correct": False,
                        "scenario_update": "Bir atak sırasında çocuk sarsıldı ve başını çarptı.",
                        "teaching_point": "Atak sırasında çocuk güvenli bir yüzeyde yan yatırılır; sarsma ve suni solunum gereksiz ve zararlıdır."
                    },
                    {
                        "text": "Elementer demir 3 mg/kg/gün 3 ay vermek, süt tüketimini 500 mL altına indirip demirden zengin beslenme önermek; atakta yan yatırmayı öğretmek",
                        "is_correct": True,
                        "explanation": "Demir tedavisi hem anemiyi düzeltir hem atak sıklığını azaltır. Ailenin zararsız ve geçici bir durum olduğunu bilmesi ve atakta güvenli pozisyonu öğrenmesi gerekir.",
                        "new_finding": "Demir başlandı, beslenme düzenlendi. Üç ay sonra Hb 11.8 g/dL'ye yükseldi; ataklar ayda bire indi ve sonra kayboldu."
                    },
                    {
                        "text": "Ataklar tekrarladığı için altı ay süreyle oral levetirasetam başlamak ve her atakta rektal diazepam uygulamalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Çocukta huzursuzluk ve uyku sorunları gelişti; ataklar azalmadı.",
                        "teaching_point": "Antiepileptikler ve benzodiazepinler katılma nöbetini önlemez."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y88",
        "category": "🧠 Nörolojik Belirtiler & Konvülziyon",
        "age": "10 Yaşında (32 kg)",
        "gender": "Kız",
        "complaint": "Bu sabah uyandığında yüzünün sağ tarafında kayma, sağ gözünü kapatamama ve ağzından su kaçırma",
        "history": "Annesi anlatıyor: 'Sabah dişlerini fırçalarken ağzından su kaçtı, sağ yanağı düşük, sağ gözünü tam kapatamıyor. Dün akşam sağ kulağının arkasında hafif ağrı olmuş. Yediklerinin tadı farklı geliyormuş.' Bir hafta önce soğuk algınlığı geçirmiş. Kulak akıntısı, kulakta kabarcık, baş ağrısı, kusma, kol veya bacakta güçsüzlük, konuşma bozukluğu yok. Kene ısırığı öyküsü yok.",
        "final_diagnosis": "Bell Paralizisi (Sağ İdiyopatik Periferik Fasiyal Paralizi)",
        "disposition": "Oral Prednizolon, Göz Koruması ve 1-2 Hafta Sonra Kontrolle Yeşil Alandan Taburculuk",
        "case_pearl": "Periferik (alt motor nöron) fasiyal paralizide alın da tutulur; santral paralizide alın korunur. Kulak kanalında ve kulak kepçesinde veziküller Ramsay Hunt sendromunu, akıntılı kulak zarı otitis mediayı, parotis kitlesi tümörü, diğer kranyal sinir veya ekstremite bulguları santral bir nedeni düşündürür. Kan basıncı mutlaka ölçülmelidir. Tipik olguda görüntüleme gerekmez. İlk 72 saatte oral kortikosteroid önerilir. Göz kapağı kapanmıyorsa gündüz yapay gözyaşı, gece göz merhemi ve bantlama ile kornea korunmalıdır. Çocuklarda prognoz çok iyidir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Yüz felci ile gelen bu çocukta muayenede en kritik noktalar nelerdir?",
                "options": [
                    {
                        "text": "Muayeneyi kısa tutup inme olasılığı nedeniyle çocuğu hemen acil kontrastsız beyin tomografisine göndermek ve sonuca göre karar vermek",
                        "is_correct": False,
                        "scenario_update": "Tomografi normal geldi; alın tutulumu ve kulak muayenesi değerlendirilmeden çocuk gereksiz radyasyon aldı.",
                        "teaching_point": "Periferik ve santral paralizi ayrımı fizik muayeneyle yapılır; görüntüleme ancak atipik bulgularda gerekir."
                    },
                    {
                        "text": "Alnın tutulup tutulmadığını, göz kapanmasını, kulak kanalı ve zarını, parotisi, diğer kranyal sinirleri, ekstremite gücünü ve kan basıncını değerlendirmek",
                        "is_correct": True,
                        "explanation": "Alın tutulumu periferik lezyonu gösterir. Kulak, parotis ve diğer nörolojik bulgular ikincil nedenleri, kan basıncı da hipertansiyonu dışlamak için gereklidir.",
                        "new_finding": "Vital Bulgular: Ateş 36.8°C, KTA 84/dk, TA 108/68 mmHg. Sağda alın kırışıklıkları kaybolmuş, kaş kaldıramıyor, göz kapağı tam kapanmıyor, kapamaya çalışınca göz küresi yukarı dönüyor. Sağ nazolabial oluk silik, ağız sola çekiliyor. Kulak kepçesi ve kanalında vezikül yok, kulak zarları normal. Parotis normal. Diğer kranyal sinirler, ekstremite gücü, refleksler ve serebellar testler normal. Kornea saydam."
                    },
                    {
                        "text": "Yüz kaymasını konversiyon bozukluğu kabul edip okul stresini sorgulamak ve psikiyatri polikliniğine yönlendirerek nörolojik muayeneyi atlamak",
                        "is_correct": False,
                        "scenario_update": "Çocuk psikiyatriye yönlendirildi; göz koruması anlatılmadığı için kornea kurudu.",
                        "teaching_point": "Nesnel fasiyal güçsüzlük nörolojik bir bulgudur; ayrıntılı muayene yapılmadan psikojenik tanı konmaz."
                    },
                    {
                        "text": "Soğuk algınlığı sonrası olduğu için viral nedenli kabul edip muayeneyi yüzle sınırlamak ve hemen oral asiklovir başlayarak taburcu etmek",
                        "is_correct": False,
                        "scenario_update": "Kan basıncı ve kulak değerlendirilmedi; tek başına antiviral tedavi iyileşmeyi hızlandırmadı.",
                        "teaching_point": "Muayene ikincil nedenleri dışlamalıdır; antiviral tek başına önerilmez."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Alın tutulumu olan ve başka nörolojik bulgusu olmayan bu çocukta hangi tetkik yaklaşımı uygundur?",
                "options": [
                    {
                        "text": "Acil kraniyal MR ve kontrastlı temporal kemik tomografisi istemek, görüntüleme tamamlanmadan tedaviye başlamamak",
                        "is_correct": False,
                        "scenario_update": "MR için randevu birkaç gün sonraya verildi; tedavi penceresi olan 72 saat kaçırıldı.",
                        "teaching_point": "Tipik periferik paralizide görüntüleme gerekmez; 3 haftada düzelme başlamaz veya atipik bulgu varsa yapılır."
                    },
                    {
                        "text": "Lomber ponksiyon yapıp BOS hücre, protein ve viral PCR çalışmak, sonuçlar gelene dek çocuğu servise yatırmak",
                        "is_correct": False,
                        "scenario_update": "BOS normal geldi; çocuk gereksiz yere yatırıldı ve invaziv girişim geçirdi.",
                        "teaching_point": "İzole periferik paralizide BOS incelemesi endike değildir."
                    },
                    {
                        "text": "Kan basıncı ve kulak muayenesi normal olduğundan görüntüleme ve kan tetkiki istemeden klinik tanıyla tedaviye geçmek",
                        "is_correct": True,
                        "explanation": "Tipik öykü ve muayenede tanı kliniktir. Lyme hastalığı endemik bölgede veya kene öyküsünde, bilateral tutulum ya da atipik seyirde tetkik planlanır.",
                        "new_finding": "Tetkik istenmedi. Bulgular sağ tarafta izole periferik fasiyal sinir tutulumuyla uyumlu; başlangıçtan bu yana yaklaşık 10 saat geçmiş."
                    },
                    {
                        "text": "Elektromiyografi ve sinir iletim çalışması istemek, sonuçlarına göre kortikosteroid tedavisinin gerekip gerekmediğine karar vermek",
                        "is_correct": False,
                        "scenario_update": "Erken dönemde yapılan çalışma bilgi vermedi; steroid başlangıcı gecikti.",
                        "teaching_point": "Elektrofizyolojik testler ilk günlerde anlamlı değildir ve tedavi kararını geciktirmemelidir."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {
                        "text": "Ramsay Hunt sendromu",
                        "is_correct": False,
                        "scenario_update": "Kulak kanalı ve kepçesinde vezikül yoktu.",
                        "teaching_point": "Ramsay Hunt'ta kulakta ağrılı veziküller ve sıklıkla işitme-denge tutulumu olur."
                    },
                    {
                        "text": "Akut iskemik inme",
                        "is_correct": False,
                        "scenario_update": "Alın tutulmuştu ve başka nörolojik bulgu yoktu.",
                        "teaching_point": "Santral yüz felcinde alın korunur ve genellikle kol-bacak bulguları eşlik eder."
                    },
                    {
                        "text": "Bell paralizisi",
                        "is_correct": True,
                        "explanation": "Saatler içinde gelişen, alnı da tutan izole tek taraflı periferik fasiyal paralizi, kulak arkası ağrısı ve tat değişikliği, ikincil nedenler dışlandığında Bell paralizisini gösterir.",
                        "new_finding": "Tanı: Sağ Bell paralizisi."
                    },
                    {
                        "text": "Otitis mediaya bağlı fasiyal paralizi",
                        "is_correct": False,
                        "scenario_update": "Kulak zarları normaldi.",
                        "teaching_point": "Otitis medianın komplikasyonu olan paralizide kulak zarı bombe ve hiperemiktir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Steroid yerine tek başına oral valasiklovir 7 gün başlamak ve göz kapağı kapanmadığı için gece gözü açık bırakıp nemli bezle silmelerini önermek",
                        "is_correct": False,
                        "scenario_update": "Antiviral tek başına yarar sağlamadı; gece açık kalan gözde kornea abrazyonu gelişti.",
                        "teaching_point": "Tek başına antiviral önerilmez. Gece göz merhemi ve bantlama ile kornea korunmalıdır."
                    },
                    {
                        "text": "Oral prednizolon 1 mg/kg/gün 5 gün verip 5 günde azaltmak; gündüz yapay gözyaşı, gece göz merhemi ve bantlama önermek, 1-2 haftada kontrol",
                        "is_correct": True,
                        "explanation": "İlk 72 saatte başlanan kortikosteroid iyileşme olasılığını artırır. Kornea koruması en önemli destek tedavidir. 3 haftada düzelme başlamazsa ileri değerlendirme yapılır.",
                        "new_finding": "Prednizolon 30 mg/gün başlandı, göz bakımı gösterildi. İki hafta sonra göz kapanması tamdı; altıncı haftada yüz hareketleri tamamen normale döndü."
                    },
                    {
                        "text": "Kas zayıflığını önlemek için hemen yoğun elektrik stimülasyonu programı başlatmak, steroidi ancak ikinci haftada düzelme yoksa eklemek",
                        "is_correct": False,
                        "scenario_update": "Steroid tedavi penceresi geçtikten sonra başlandı; elektrik stimülasyonu yüzde sinkinezi riskini artırdı.",
                        "teaching_point": "Elektrik stimülasyonunun yararı gösterilmemiştir; steroid ilk 72 saatte başlanmalıdır."
                    },
                    {
                        "text": "Çocuklarda prognoz çok iyi olduğu için ilaç vermeden yalnızca yüz egzersizleri önermek ve göz bakımına gerek olmadığını söylemek",
                        "is_correct": False,
                        "scenario_update": "Gece kapanmayan gözde kızarıklık ve ağrı gelişti; çocuk göz acile başvurdu.",
                        "teaching_point": "Prognoz iyi olsa da steroid iyileşmeyi destekler ve göz koruması her olguda gereklidir."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y89",
        "category": "🦴 Kas-İskelet & Eklem / Ortopedik Aciller",
        "age": "8 Yaşında (27 kg)",
        "gender": "Erkek",
        "complaint": "Sabah uyandığında başlayan boyun ağrısı ve başını sağa çevirememe",
        "history": "Annesi anlatıyor: 'Dün akşam uzun yolculuk yaptık, arabada başını cama dayayıp uyudu. Bu sabah başı sola eğik kaldı, sağa çevirmeye çalışınca ağlıyor.' Düşme, çarpma, spor yaralanması yok. Ateş, boğaz ağrısı, yutma güçlüğü, salya akması, ses değişikliği, kusma, baş ağrısı, yürümede dengesizlik yok. Son iki haftada ilaç kullanmamış. Daha önce benzer yakınması olmamış.",
        "final_diagnosis": "Kas Kaynaklı (Postüral) Akut Tortikolis",
        "disposition": "Analjezi, Sıcak Uygulama ve Bir Hafta İçinde Düzelme Yoksa Kontrol Önerisiyle Yeşil Alandan Taburculuk",
        "case_pearl": "Çocukta akut tortikolisin en sık nedeni uygunsuz pozisyonda uyku sonrası gelişen kas spazmıdır. Ateş, yutma güçlüğü ve boyun hareketlerinde ağrı retrofarengeal apseyi; yakın zamanda geçirilmiş üst solunum yolu enfeksiyonu veya baş-boyun cerrahisi sonrası düzelmeyen tortikolis atlantoaksiyel rotatuar subluksasyonu; baş ağrısı, kusma veya ataksi posterior fossa kitlesini; ilaç öyküsü distonik reaksiyonu düşündürür. Tipik olguda görüntüleme gerekmez. Bir haftada düzelmeyen olgu yeniden değerlendirilir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Başını çeviremeyen bu çocukta muayenede hangi bulguları özellikle ararsınız?",
                "options": [
                    {
                        "text": "Ateşi, ağız içi ve farenksi, boyun lenf nodlarını, kas spazmının tarafını, nörolojik bulguları, yürüyüşü ve göz hareketlerini değerlendirmek",
                        "is_correct": True,
                        "explanation": "Ateş ve farenks bulguları derin boyun enfeksiyonunu, nörolojik ve serebellar bulgular santral nedenleri dışlar. Kas spazmının tarafı ve hareket kısıtlılığı tabloyu tanımlar.",
                        "new_finding": "Vital Bulgular: Ateş 36.7°C, KTA 88/dk. Baş sola eğik, çene hafif sağa dönük. Sol sternokleidomastoid kasında gerginlik ve hassasiyet. Sağa rotasyon ve sola eğilme ağrılı ve kısıtlı. Farenks normal, uvula orta hatta, salya yok, lenf nodu büyük değil. Nörolojik muayene, göz hareketleri, yürüyüş ve serebellar testler normal. Orta hatta kemik hassasiyeti yok."
                    },
                    {
                        "text": "Boyun yaralanması olasılığıyla hemen boyunluk takıp sırt tahtasına almak ve muayene etmeden servikal tomografi istemek ve ortopediye danışmak",
                        "is_correct": False,
                        "scenario_update": "Tomografi normal geldi; travma öyküsü olmayan çocuk gereksiz immobilizasyon ve radyasyona maruz kaldı.",
                        "teaching_point": "Travma öyküsü olmayan çocukta spinal immobilizasyon ve tomografi gerekmez."
                    },
                    {
                        "text": "Boynu düzeltmek için hızlı bir manevrayla başı orta hatta getirmeye çalışmak, ardından muayeneyi tamamlamak",
                        "is_correct": False,
                        "scenario_update": "Manevra çocukta şiddetli ağrıya neden oldu ve kas spazmı arttı.",
                        "teaching_point": "Zorlayıcı manipülasyon zararlıdır; altta yatan neden belirlenmeden boyun zorla döndürülmez."
                    },
                    {
                        "text": "Ağrıyı ilaca bağlı bir kasılma kabul edip öyküyü sorgulamadan intravenöz biperiden uygulamak ve yanıtı gözlemek",
                        "is_correct": False,
                        "scenario_update": "Biperiden sonrası çocukta ağız kuruluğu ve huzursuzluk oldu, boyun pozisyonu değişmedi.",
                        "teaching_point": "İlaç öyküsü olmadan antikolinerjik tedavi gereksizdir; önce öykü ve muayene yapılmalıdır."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Ateşi ve nörolojik bulgusu olmayan bu çocukta hangi yaklaşım uygundur?",
                "options": [
                    {
                        "text": "Boyun ön-arka ve yan grafisi çekmek, grafi normalse servikal MR ile bağ yaralanmasını dışlamak üzere randevu vermek ve kontrol grafisi planlamak",
                        "is_correct": False,
                        "scenario_update": "Grafide yalnızca kas spazmına bağlı lordoz düzleşmesi görüldü; MR gereksiz bekleme yarattı.",
                        "teaching_point": "Travmasız tipik tortikoliste grafi ve MR yönetimi değiştirmez."
                    },
                    {
                        "text": "Tam kan sayımı, CRP ve sedimantasyon istemek, değerler yüksekse derin boyun enfeksiyonu açısından kontrastlı tomografi planlamak",
                        "is_correct": False,
                        "scenario_update": "Tüm değerler normal geldi; çocuk kan alımıyla gereksiz yere strese girdi.",
                        "teaching_point": "Ateş, yutma güçlüğü ve farenks bulgusu olmadan kan tetkiki gerekmez."
                    },
                    {
                        "text": "Görüntüleme ve kan tetkiki istemeden tedaviye başlamak; ateş, yutma güçlüğü, nörolojik bulgu veya bir haftada düzelmeme olursa yeniden değerlendirmek",
                        "is_correct": True,
                        "explanation": "Tipik öykü ve normal muayenede tanı kliniktir. Uyarı bulguları tanımlanır ve bir haftada düzelmeyen olguda görüntüleme planlanır.",
                        "new_finding": "Tetkik istenmedi. İbuprofen sonrası 45 dakikada ağrı azaldı ve rotasyon açıklığı arttı."
                    },
                    {
                        "text": "Acil kontrastlı boyun ve beyin tomografisini birlikte istemek ve sonuç gelene dek çocuğu ağızdan beslemeden bekletmek",
                        "is_correct": False,
                        "scenario_update": "Tomografiler normal geldi; çocuk saatlerce aç bekletildi ve gereksiz radyasyon aldı.",
                        "teaching_point": "Uyarı bulgusu olmadan ileri görüntüleme önerilmez."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {
                        "text": "Atlantoaksiyel rotatuar subluksasyon",
                        "is_correct": False,
                        "scenario_update": "Yakında üst solunum yolu enfeksiyonu yoktu ve analjeziyle hareket açıklığı arttı.",
                        "teaching_point": "Rotatuar subluksasyonda kafa 'horoz pozisyonunda' sabittir ve analjeziyle düzelmez; BT gerekir."
                    },
                    {
                        "text": "Retrofarengeal apse",
                        "is_correct": False,
                        "scenario_update": "Ateş, yutma güçlüğü, salya ve farenks bulgusu yoktu.",
                        "teaching_point": "Retrofarengeal apsede ateş, boyun ekstansiyonunda ağrı ve yutma güçlüğü olur."
                    },
                    {
                        "text": "Kas kaynaklı (postüral) akut tortikolis",
                        "is_correct": True,
                        "explanation": "Uygunsuz pozisyonda uyku sonrası başlayan, ateşsiz, nörolojik bulgusuz ve analjeziyle hareket açıklığı artan tortikolis kas kaynaklıdır.",
                        "new_finding": "Tanı: Kas kaynaklı (postüral) akut tortikolis."
                    },
                    {
                        "text": "Akut distonik reaksiyon",
                        "is_correct": False,
                        "scenario_update": "Son iki haftada ilaç kullanımı yoktu.",
                        "teaching_point": "Distonik reaksiyon dopamin antagonisti ilaçlardan sonra görülür ve göz, dil tutulumu eşlik edebilir."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun plan hangisidir?",
                "options": [
                    {
                        "text": "Üç hafta sert boyunluk takmasını ve boynunu hiç hareket ettirmemesini önermek, okuldan rapor vermek",
                        "is_correct": False,
                        "scenario_update": "Uzun süre hareketsiz kalan boyunda sertlik arttı ve iyileşme gecikti.",
                        "teaching_point": "Uzun süreli boyunluk kas sertliğini artırır; erken ve nazik hareket önerilir."
                    },
                    {
                        "text": "İbuprofen 10 mg/kg günde üç kez 3-5 gün, sıcak uygulama ve nazik germe egzersizleri önermek; bir haftada düzelmezse kontrole gelmesini söylemek",
                        "is_correct": True,
                        "explanation": "Analjezi ve sıcak uygulama kas spazmını çözer, nazik hareket iyileşmeyi hızlandırır. Bir haftada düzelmeme veya uyarı bulguları yeniden değerlendirme gerektirir.",
                        "new_finding": "Çocuk ibuprofen ve sıcak uygulama önerileriyle taburcu edildi. Üçüncü gün boyun hareketleri tamamen normale döndü."
                    },
                    {
                        "text": "Kas gevşetici olarak oral diazepam başlamak ve boynun hızla düzelmesi için ertesi gün manuel manipülasyon seansı planlamak",
                        "is_correct": False,
                        "scenario_update": "Diazepam çocukta aşırı uyku hali yaptı; manipülasyon önerisi gereksiz risk oluşturdu.",
                        "teaching_point": "Çocuklarda benzodiazepin kas gevşetici olarak önerilmez; boyun manipülasyonu ciddi komplikasyon riski taşır."
                    },
                    {
                        "text": "Altta yatan bir enfeksiyonu önlemek için 7 gün amoksisilin-klavulanat başlamak ve iki gün sonra kontrol grafisi planlamak",
                        "is_correct": False,
                        "scenario_update": "Antibiyotik ishal yaptı ve kontrol grafisi gereksiz radyasyon oldu.",
                        "teaching_point": "Enfeksiyon bulgusu olmayan kas kaynaklı tabloda antibiyotik ve kontrol grafisi gerekmez."
                    }
                ]
            }
        ]
    },
    {
        "id": "Y90",
        "category": "💧 Sıvı-Elektrolit & Renal / Ürolojik Aciller",
        "age": "4 Yaşında (16 kg)",
        "gender": "Erkek",
        "complaint": "İki gündür penis ucunda kızarıklık, şişlik, ağrı ve idrar yaparken yanma",
        "history": "Annesi anlatıyor: 'İki gündür pipisinin ucu kıpkırmızı ve şiş, sarı bir akıntı var. İşerken ağlıyor ama idrarını yapıyor. Sünnetli değil. Derisini temizlemek için geri çekmeye çalıştım ama açılmıyor.' Ateş yok, karın ağrısı ve kusma yok. Bir hafta önce boğaz ağrısı olmuş, kardeşi de boğaz enfeksiyonu geçirmiş. Bebek bezini bırakmış, kendi tuvaletini yapıyor.",
        "final_diagnosis": "Akut Bakteriyel Balanopostit (A Grubu Streptokok)",
        "disposition": "Oral Amoksisilin, Ilık Oturma Banyosu ve Hijyen Eğitimiyle Yeşil Alandan Taburculuk",
        "case_pearl": "Balanopostit sünnetsiz erkek çocuklarda glans ve sünnet derisinin iltihabıdır; sıklıkla hijyen sorunu ve irritasyonla ilişkilidir. Pürülan akıntı ve belirgin eritemde, özellikle yakın zamanda farenjit öyküsü varsa A grubu streptokok düşünülür ve sürüntü kültürü alınır. Sünnet derisi zorla geri çekilmemelidir; çocuklarda fizyolojik yapışıklık normaldir. İdrar retansiyonu ve derinin glansın arkasında sıkışması (parafimozis) acil durumlardır. Tek atak sünnet endikasyonu değildir.",
        "steps": [
            {
                "stage_title": "İlk Klinik Değerlendirme ve Fizik Muayene",
                "question": "Penis ucunda kızarıklık ve akıntı olan bu çocukta muayenede neye dikkat edersiniz?",
                "options": [
                    {
                        "text": "Sünnet derisinin pozisyonunu, glansın görünümünü, akıntının niteliğini, idrar akımını, inguinal bölgeyi ve skrotumu sünnet derisini zorlamadan değerlendirmek",
                        "is_correct": True,
                        "explanation": "Derinin glans arkasında sıkışıp sıkışmadığı ve idrar akımı acil durumları dışlar. Pürülan akıntı enfeksiyon için kültür kararını belirler. Zorla geri çekme travmaya yol açar.",
                        "new_finding": "Ateş 36.9°C, genel durum iyi. Sünnet derisi glansı örtüyor, glans arkasında sıkışma yok. Prepisyum ve görülebilen glans kenarı parlak kırmızı ve ödemli, ağızda sarı pürülan akıntı. Meatus prepisyum açıklığından görülüyor, çocuk muayene sırasında ince ama kesintisiz akımla idrar yaptı. Skrotum ve testisler normal. İnguinal bölgede küçük hassas lenf nodları."
                    },
                    {
                        "text": "Glansı tam görmek ve akıntıyı temizlemek için sünnet derisini muayene sırasında zorlayarak geri çekmek ve altını antiseptikle silmek",
                        "is_correct": False,
                        "scenario_update": "Zorla geri çekilen deri glans arkasında sıkıştı ve çocukta şiddetli ağrı ile ödem gelişti.",
                        "teaching_point": "Küçük çocukta sünnet derisi fizyolojik olarak yapışıktır; zorla geri çekmek travmaya ve parafimozise yol açar."
                    },
                    {
                        "text": "İdrar yaparken yanma olduğu için idrar yolu enfeksiyonu kabul edip penisi muayene etmeden idrar tetkiki ve kültürü istemek",
                        "is_correct": False,
                        "scenario_update": "İdrar örneği akıntıyla kontamine oldu ve sonuç yorumlanamadı; lokal tablo değerlendirilmedi.",
                        "teaching_point": "Lokal iltihapta idrarın iltihaplı alandan geçmesi yanmaya neden olur; önce genital muayene yapılır."
                    },
                    {
                        "text": "Muayene sonrası hemen çocuk cerrahisine sevk edip acil sünnet planlamak, o zamana kadar ağrı kesici vermek",
                        "is_correct": False,
                        "scenario_update": "Akut iltihap döneminde cerrahi planlanması uygun bulunmadı ve aile gereksiz yere sevk edildi.",
                        "teaching_point": "Akut iltihapta sünnet yapılmaz; tek atak sünnet endikasyonu değildir."
                    }
                ]
            },
            {
                "stage_title": "Tetkik Kararı",
                "question": "Pürülan akıntısı olan, idrarını yapabilen bu çocukta hangi yaklaşım uygundur?",
                "options": [
                    {
                        "text": "Tam kan sayımı, CRP ve kan kültürü istemek, değerler yüksekse intravenöz antibiyotikle servise yatırmak ve kültürleri beklemek",
                        "is_correct": False,
                        "scenario_update": "Değerler normal geldi; iyi görünen çocuk gereksiz yere kan alımı geçirdi.",
                        "teaching_point": "Sistemik bulgusu olmayan lokal genital enfeksiyonda kan tetkiki gerekmez."
                    },
                    {
                        "text": "Penis ve skrotum ultrasonografisi istemek ve sonucu gelene kadar çocuğu acil serviste bekletmek",
                        "is_correct": False,
                        "scenario_update": "Ultrasonografi yalnızca yüzeyel ödem gösterdi; tanıya katkı sağlamadı.",
                        "teaching_point": "Yüzeyel iltihapta görüntüleme gerekmez."
                    },
                    {
                        "text": "Akıntıdan sürüntü kültürü almak ve yakın zamanda boğaz enfeksiyonu öyküsü nedeniyle hızlı strep testi uygulamak",
                        "is_correct": True,
                        "explanation": "Pürülan akıntıda etken belirlenmesi tedaviyi yönlendirir. Yakın farenjit öyküsü ve belirgin eritem A grubu streptokoku düşündürür.",
                        "new_finding": "Akıntıdan alınan sürüntüde hızlı strep antijen testi pozitif. Kültür 48 saat sonra A grubu beta-hemolitik streptokok olarak bildirildi."
                    },
                    {
                        "text": "İdrar sondası takıp kateter idrarından kültür almak ve sonuç gelene kadar sondayı yerinde bırakmak",
                        "is_correct": False,
                        "scenario_update": "Sonda takılırken ödemli doku travmatize oldu ve çocuk çok ağladı.",
                        "teaching_point": "İdrar yapabilen çocukta sonda gerekmez ve iltihaplı dokuda travma riski taşır."
                    }
                ]
            },
            {
                "stage_title": "Klinik Tanı",
                "question": "Bulgulara göre en olası tanınız nedir?",
                "options": [
                    {
                        "text": "Parafimozis (sıkışmış prepisyum)",
                        "is_correct": False,
                        "scenario_update": "Sünnet derisi glansı örtüyordu, glans arkasında sıkışma yoktu.",
                        "teaching_point": "Parafimoziste geri çekilmiş deri glans arkasında halka şeklinde sıkışır ve glans ödemlenir."
                    },
                    {
                        "text": "Akut bakteriyel balanopostit",
                        "is_correct": True,
                        "explanation": "Sünnetsiz çocukta glans ve prepisyumda eritem, ödem, pürülan akıntı ve pozitif streptokok testi akut bakteriyel balanopostiti gösterir.",
                        "new_finding": "Tanı: Akut bakteriyel balanopostit (A grubu streptokok)."
                    },
                    {
                        "text": "Fimozise bağlı idrar retansiyonu",
                        "is_correct": False,
                        "scenario_update": "Çocuk muayene sırasında kesintisiz akımla idrar yaptı.",
                        "teaching_point": "Retansiyonda mesane dolgun ve ele gelir, çocuk işeyemez."
                    },
                    {
                        "text": "Kandidiyal balanit",
                        "is_correct": False,
                        "scenario_update": "Satellit lezyonlar ve beyaz plak yoktu, streptokok testi pozitifti.",
                        "teaching_point": "Kandida enfeksiyonunda uydu lezyonlar ve beyaz plaklar görülür."
                    }
                ]
            },
            {
                "stage_title": "Tedavi ve Taburculuk Planı",
                "question": "Bu çocuk için en uygun tedavi planı hangisidir?",
                "options": [
                    {
                        "text": "Yalnızca topikal kortikosteroid krem sürmelerini ve sünnet derisini her gün geri çekip içini sabunla yıkamalarını önermek",
                        "is_correct": False,
                        "scenario_update": "Steroid krem enfeksiyonu ilerletti, zorla geri çekme ağrı ve küçük yırtıklara neden oldu.",
                        "teaching_point": "Bakteriyel enfeksiyonda tek başına steroid uygun değildir ve deri zorla geri çekilmemelidir."
                    },
                    {
                        "text": "Ağızdan amoksisilin 10 gün, günde iki-üç kez ılık oturma banyosu ve analjezi önermek; işeyemezse veya deri geride sıkışırsa hemen dönmelerini söylemek",
                        "is_correct": True,
                        "explanation": "A grubu streptokok enfeksiyonu sistemik antibiyotikle tedavi edilir. Ilık banyo ödemi ve ağrıyı azaltır. İdrar retansiyonu ve parafimozis uyarı bulgularıdır.",
                        "new_finding": "Amoksisilin ve ılık banyo önerisiyle taburcu edildi. Üçüncü gün akıntı kesildi, yedinci gün kızarıklık tamamen geçti."
                    },
                    {
                        "text": "Tek doz intramüsküler seftriakson yapıp tedaviyi tamamlanmış saymak ve aynı hafta içinde elektif sünnet randevusu vermek",
                        "is_correct": False,
                        "scenario_update": "Tek doz yetersiz kaldı ve akıntı tekrarladı; iltihaplı dönemde sünnet planı uygun bulunmadı.",
                        "teaching_point": "Tek doz seftriakson streptokok enfeksiyonunda yeterli değildir; iltihap geçmeden cerrahi planlanmaz."
                    },
                    {
                        "text": "Antibiyotikli göz pomadı ile topikal mupirosin sürmek ve ağrı geçene kadar çocuğun su içmesini kısıtlayarak idrar sayısını azaltmak",
                        "is_correct": False,
                        "scenario_update": "Su kısıtlaması sonrası idrar konsantre hale geldi ve yanma arttı.",
                        "teaching_point": "Sıvı kısıtlaması yanmayı artırır; bol sıvı ve ılık banyo önerilir."
                    }
                ]
            }
        ]
    }
]
