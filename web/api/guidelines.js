// Vaka asistanının dayandığı kılavuz kartları.
// Her kart, kaynağı belirtilmiş KISA bir özettir (kılavuz metni kopyalanmaz).
// "teyit" alanı: hangi bilginin birincil/ikincil kaynakla doğrulandığını ve hekim incelemesinde
// özellikle bakılması gerekenleri not eder (modele gönderilmez).
//
// cases: kartın doğrudan ilgili olduğu vaka kimlikleri (vaka açıkken öncelikli seçilir)
// keywords: soru metninde aranan, Türkçe karakterleri sadeleştirilmiş anahtar kelimeler

export const GUIDELINES = [
  {
    id: 'status-epileptikus',
    title: 'Konvülzif status epileptikus (çocuk)',
    sources: 'AES 2016 (Glauser ve ark., Epilepsy Currents); ENLS; Türkiye uygulama notları',
    cases: ['S03', 'S71', 'S72', 'S49', 'S80', 'S76'],
    keywords: ['status', 'nobet', 'konvulziyon', 'kasilma', 'epilep', 'benzodiazepin', 'midazolam', 'diazepam', 'lorazepam', 'levetirasetam', 'fenitoin', 'fosfenitoin', 'valproat', 'fenobarbital', 'antiepileptik'],
    body: [
      'Tanım: 5 dakika veya daha uzun süren nöbet ya da arada bilinç düzelmeden tekrarlayan nöbetler.',
      '0-5 dk (stabilizasyon): hava yolu, O2, monitör, kan şekeri (hipoglisemiyi düzelt), damar yolu aç.',
      '5-20 dk, 1. basamak (benzodiazepin): IM midazolam 13-40 kg 5 mg, >40 kg 10 mg (tek doz) VEYA IV diazepam 0,15-0,2 mg/kg (maks 10 mg) VEYA IV lorazepam 0,1 mg/kg (maks 4 mg; IV formu Türkiye\'de çoğu merkezde bulunmaz).',
      'Damar yolu yoksa: IM/intranazal/bukkal midazolam ya da rektal diazepam 0,2-0,5 mg/kg (maks 20 mg) (yerel protokolden teyit et).',
      'Benzodiazepin hastane öncesi dozlar dahil en fazla 2 kez verilir; ikinci doz ilk dozdan yaklaşık 5 dk sonra.',
      '20-40 dk, 2. basamak (aralarında üstünlük gösterilmemiş): IV fosfenitoin 20 mg FE/kg (maks 1500 mg FE) VEYA IV valproat 40 mg/kg (maks 3000 mg) VEYA IV levetirasetam 60 mg/kg (maks 4500 mg). Bunlar yoksa IV fenobarbital 15 mg/kg (yerel protokolden teyit et).',
      'Valproat: karaciğer hastalığı veya metabolik/mitokondriyal hastalık şüphesinde kaçınılır. Fenitoin/fosfenitoin: kardiyak monitör, hız sınırına uy.',
      '40 dk sonrası (refrakter): yoğun bakım, entübasyon, anestezik infüzyon (midazolam, tiyopental/pentobarbital, propofol), mümkünse sürekli EEG.',
      'Nedeni araştır: ateş/enfeksiyon, ilaç kesilmesi veya düşük düzey, elektrolit (Na, Ca, Mg), glukoz, toksik madde, kafa içi patoloji.',
    ],
    teyit:
      'IM midazolam ağırlık bantları ve diazepam 0,15-0,2 mg/kg AES özetinden; levetirasetam 60 (maks 4500), valproat 40, fosfenitoin 20 mg FE/kg ENLS\'ten doğrulandı. Valproat yükleme dozu kaynaklar arasında 20-40 mg/kg değişiyor. Fenobarbital 15 mg/kg ve intranazal/bukkal midazolam dozu kaynakla doğrulanamadı.',
  },
  {
    id: 'febril-nobet',
    title: 'Febril nöbet',
    sources: 'AAP 2011 basit febril nöbet kılavuzu',
    cases: ['S02', 'S03'],
    keywords: ['febril', 'ates', 'nobet', 'konvulziyon', 'kasilma', 'lomber', 'ponksiyon', 'eeg', 'goruntuleme'],
    body: [
      'Basit febril nöbet: 6-60 ay, ateşle birlikte, jeneralize, 15 dakikadan kısa, 24 saatte bir kez, SSS enfeksiyonu yok. Fokal, 15 dakika veya daha uzun ya da 24 saatte tekrarlayan nöbet komplike sayılır.',
      'Nörolojik olarak sağlıklı çocukta basit febril nöbette rutin EEG, nörogörüntüleme ve kan tetkiki önerilmez; tetkik ateşin odağına göre planlanır.',
      'Lomber ponksiyon: menenjit bulgusu varsa yapılmalı. 6-12 ayda Hib veya pnömokok aşısı eksik/bilinmiyorsa ya da önceden antibiyotik almışsa seçenek olarak düşünülür.',
      'Ateş düşürücüler nöbet tekrarını önlemez; basit febril nöbette profilaktik antiepileptik önerilmez.',
      '5 dakikayı aşan nöbet status epileptikus gibi tedavi edilir (benzodiazepin).',
      'Aileye eğitim: nöbet sırasında yan yatırma, ağza bir şey sokmama, süreyi ölçme.',
    ],
    teyit: 'EEG, görüntüleme, kan tetkiki ve LP önerileri AAP 2011 özetlerinden doğrulandı.',
  },
  {
    id: 'akut-gastroenterit',
    title: 'Akut gastroenterit ve dehidratasyon',
    sources: 'ESPGHAN/ESPID 2014; NICE CG84',
    cases: ['S01', 'S44', 'S48', 'S58', 'Y04', 'Y41', 'Y42', 'S49'],
    keywords: ['gastroenterit', 'ishal', 'diyare', 'kusma', 'dehidratasyon', 'ors', 'rehidratasyon', 'sivi', 'ondansetron', 'metoklopramid', 'domperidon', 'antiemetik', 'probiyotik', 'nazogastrik'],
    body: [
      'Temel tedavi: düşük osmolar oral rehidratasyon solüsyonu (ORS), mümkün olan en erken zamanda.',
      'NICE: klinik dehidratasyonda 4 saatte 50 ml/kg ORS + idame sıvı; her sulu dışkı/kusma sonrası ek sıvı.',
      'Oral alım başarısızsa nazogastrik ORS; enteral rehidratasyon IV\'ye eşdeğer veya üstün kabul edilir.',
      'Şok bulgusu (veya şüphesi) varsa IV izotonik kristaloid bolus ve yeniden değerlendirme; dozu yerel protokole göre (sepsis/şok kartına bak).',
      'Beslenme: emzirme kesilmez, yaşa uygun normal diyet sürdürülür; rutin laktozsuz/sulandırılmış mama gerekmez.',
      'Antiemetik: ondansetron kusmayı azaltır ve oral rehidratasyon başarısını artırır; ESPGHAN rutin kullanım için kardiyak (QT) güvenlik uyarısı belirtir. Metoklopramid ve domperidon rutin önerilmez.',
      'Probiyotik: yalnızca kanıtı olan belirli suşlar (ör. Lactobacillus rhamnosus GG, Saccharomyces boulardii) süreyi kısaltabilir.',
      'Antibiyotik rutin önerilmez.',
    ],
    teyit:
      'ORS, beslenme, NG rehidratasyon, ondansetron uyarısı ve probiyotik bilgisi ESPGHAN 2014 özetlerinden; 50 ml/kg/4 saat NICE\'ın ikincil özetinden. Ondansetron dozu ve şok bolus hacmi bu kartta bilerek verilmedi.',
  },
  {
    id: 'bronsiolit',
    title: 'Akut bronşiolit',
    sources: 'AAP 2014; NICE NG9 (2021 güncellemesi)',
    cases: ['S12', 'S74', 'Y19', 'Y98'],
    keywords: ['bronsiolit', 'rsv', 'hisilti', 'wheezing', 'salbutamol', 'hipertonik', 'nebul', 'adrenalin', 'oksijen', 'satur', 'yuksek akim', 'hfnc', 'apne'],
    body: [
      'Tanı klinik; rutin akciğer grafisi, viral test ve kan tetkiki önerilmez.',
      'Önerilmeyenler: salbutamol, nebül adrenalin, sistemik veya inhale steroid, bakteriyel enfeksiyon yoksa antibiyotik, göğüs fizyoterapisi. Hipertonik salin acil serviste önerilmez (AAP yatan hastada seçenek sayar, NICE hiç önermez).',
      'Oksijen eşiği: AAP SpO2 <%90. NICE: 6 hafta ve üzeri <%90; 6 haftadan küçük veya altta yatan hastalığı olanlarda <%92.',
      'Destek: beslenmeyi bozuyorsa burun aspirasyonu; yetersiz oral alımda nazogastrik veya IV sıvı; ağır solunum sıkıntısında yüksek akımlı nazal kanül/CPAP.',
      'Ağır seyir riski: prematürite, küçük süt çocuğu (özellikle <3 ay), konjenital kalp/kronik akciğer hastalığı, immün yetmezlik.',
      'Yatış/acil sevk bulguları: apne, ağır solunum sıkıntısı (inleme, belirgin çekilme), eşik altında SpO2, belirgin azalmış oral alım veya dehidratasyon.',
    ],
    teyit: 'Önerilmeyen tedaviler ve SpO2 eşikleri AAP 2014 ve NICE NG9 metinlerinden doğrulandı.',
  },
  {
    id: 'astim-atagi',
    title: 'Akut astım atağı (çocuk)',
    sources: 'GINA 2024/2025; BTS/SIGN',
    cases: ['S04', 'S73', 'Y75', 'Y76'],
    keywords: ['astim', 'atak', 'hisilti', 'salbutamol', 'ipratropium', 'steroid', 'prednizolon', 'deksametazon', 'magnezyum', 'mgso4', 'bronkodilator', 'inhaler', 'spacer'],
    body: [
      'Şiddeti değerlendir: konuşma, solunum sayısı, çekilmeler, SpO2, bilinç. Kırmızı bayrak: konuşamama, sessiz akciğer, siyanoz, bilinç değişikliği.',
      'Oksijen: SpO2 hedefi %94-98.',
      'Kısa etkili beta-2 agonist (salbutamol) ölçülü doz inhaler + spacer ile (veya nebül), ilk saatte 20 dakika arayla tekrarlanır.',
      'Orta-ağır atakta ilk saatte ipratropium bromür eklenir.',
      'Sistemik steroid erken verilir: oral prednizolon 1-2 mg/kg/gün (6-11 yaşta maks 40 mg), 3-5 gün (yerel protokolden teyit et). Yutamıyor/kusuyorsa parenteral steroid.',
      'Ağır veya ilk tedaviye yanıtsız atakta IV magnezyum sülfat düşünülür (dozu yerel protokole göre teyit et).',
      'Rutin akciğer grafisi ve antibiyotik önerilmez.',
    ],
    teyit:
      'SpO2 %94-98 ve ipratropium önerisi GINA tabanlı ikincil kaynaklardan doğrulandı. Prednizolon 1-2 mg/kg (maks 40 mg) ve MgSO4 dozu bu aramada birincil kaynakla doğrulanamadı; salbutamol puf/nebül dozu karta bilerek yazılmadı.',
  },
  {
    id: 'anafilaksi',
    title: 'Anafilaksi',
    sources: 'EAACI 2021; Resuscitation Council UK 2021; WAO',
    cases: ['S16', 'Y20', 'Y06'],
    keywords: ['anafilaksi', 'alerji', 'adrenalin', 'epinefrin', 'urtiker', 'anjioodem', 'otoenjektor', 'antihistaminik', 'bifazik'],
    body: [
      'İlk ve en önemli tedavi: IM adrenalin, uyluk anterolateraline, 1 mg/mL (1:1000) solüsyondan 0,01 mg/kg (maks 0,5 mg) (yerel protokolden teyit et). Yanıt yoksa yaklaşık 5 dakikada bir tekrarlanır.',
      'Pozisyon: sırtüstü, bacaklar yukarıda; solunum sıkıntısında oturur pozisyon. Ani ayağa kaldırma.',
      'O2, damar yolu; hipotansiyon veya şokta IV kristaloid bolus ve yeniden değerlendirme.',
      'İki doz IM adrenaline yanıtsızlık refrakter anafilaksidir: IV adrenalin infüzyonu (uzman/yoğun bakım).',
      'Antihistaminik ve steroid ikinci plandadır, adrenalinin yerini tutmaz.',
      'Bifazik reaksiyon riski nedeniyle gözlem; taburculukta adrenalin otoenjektörü, yazılı eylem planı ve alerji polikliniğine sevk.',
    ],
    teyit:
      'IM adrenalinin birinci basamak olduğu ve 5 dakikada tekrar EAACI/RCUK özetlerinden doğrulandı. 0,01 mg/kg (maks 0,5 mg) birincil kaynakla doğrulanamadı; RCUK yaş bantları (150/300/500 mcg), otoenjektör ağırlık bantları ve gözlem süresi karta bilerek yazılmadı.',
  },
  {
    id: 'krup',
    title: 'Krup (viral laringotrakeit)',
    sources: 'Kanada Pediatri Derneği (CPS); TREKK',
    cases: ['S10', 'Y13'],
    keywords: ['krup', 'stridor', 'havlar', 'laringotrakeit', 'deksametazon', 'westley', 'adrenalin', 'epinefrin', 'nebul'],
    body: [
      'Şiddet Westley skoruyla değerlendirilir. Çocuğu ajite etme, gereksiz boğaz muayenesinden kaçın.',
      'Tüm şiddetlerde tek doz oral deksametazon: kanıt 0,15-0,6 mg/kg aralığını destekler; en yaygın kullanılan 0,6 mg/kg (TREKK: maks 12 mg).',
      'Orta-ağır krupta nebül adrenalin; etkisi geçici olduğundan sonrasında 2-4 saat gözlem (istirahatte stridor ve çekilme kaybolana kadar).',
      'Hipoksemide oksijen.',
      'Kırmızı bayrak: salya, toksik görünüm, tripod pozisyonu, yüksek ateş; epiglottit, bakteriyel trakeit veya retrofarengeal apse düşün.',
      'Taburculuk: istirahatte stridor ve çekilme yok, oral alım iyi, aile güvenli.',
    ],
    teyit:
      'Deksametazon 0,6 mg/kg (CPS) ve 0,15-0,6 aralığı/maks 12 mg (TREKK), gözlem süresi doğrulandı. Nebül adrenalin dozu kaynaklar arasında değiştiği için karta yazılmadı.',
  },
  {
    id: 'dka',
    title: 'Diyabetik ketoasidoz (DKA)',
    sources: 'ISPAD 2022; BSPED',
    cases: ['S06', 'S79', 'Y39'],
    keywords: ['dka', 'ketoasidoz', 'diyabet', 'insulin', 'keton', 'serebral odem', 'beyin odemi', 'mannitol', 'hipertonik', 'potasyum', 'bikarbonat', 'glukoz'],
    body: [
      'Tanı: hiperglisemi, venöz pH <7,3 veya bikarbonat <18 mmol/L, ketonemi/ketonüri.',
      'Sıvı: başlangıç bolusu(ları) 20-30 dakikada; BSPED 10 ml/kg\'lık bolusları her birinden sonra yeniden değerlendirerek kullanır. Kalan sıvı açığı yavaş, saatler içinde (24-48 saat) yerine konur.',
      'İnsülin: sıvı tedavisinden sonra başlanır (ISPAD tabanlı protokoller: ilk sıvıdan 60-120 dakika sonra); insülin bolusu yapılmaz.',
      'Potasyum: K <3,0 mmol/L ise insülini ertele, önce potasyum ver (en fazla 0,5 mEq/kg/saat).',
      'Bikarbonat rutin kullanılmaz.',
      'Serebral ödem uyarı bulguları: tedavi başladıktan sonra başlayan veya artan baş ağrısı, bilinç değişikliği, bradikardi, kan basıncı yükselmesi, nörolojik bulgu. Şüphede hemen ozmotik tedavi (mannitol veya hipertonik salin) ve sıvı hızını azaltma; dozları yerel protokolden teyit et.',
      'İzlem: saatlik glukoz ve nörolojik değerlendirme, düzenli elektrolit ve kan gazı.',
    ],
    teyit:
      'Bikarbonat <18, bolusun 20-30 dakikada verilmesi, K <3 kuralı ISPAD 2022; 10 ml/kg aliquot BSPED; insülin zamanlaması BC Children\'s/ISPAD. İnsülin infüzyon hızı (0,05-0,1 ü/kg/saat) ve mannitol/hipertonik salin dozları doğrulanamadığı için karta yazılmadı.',
  },
  {
    id: 'ates-kucuk-bebek',
    title: 'İyi görünen ateşli küçük bebek (8-60 gün)',
    sources: 'AAP 2021 (Pantell ve ark., Pediatrics)',
    cases: ['S60', 'Y77'],
    keywords: ['ates', 'bebek', 'yenidogan', 'sepsis', 'prokalsitonin', 'crp', 'lomber', 'ponksiyon', 'bos', 'idrar', 'kultur', 'gunluk'],
    body: [
      'Kapsam: iyi görünen, term doğmuş, 8-60 günlük, son 24 saatte 38,0 °C veya üzeri ateşi olan bebek. Kötü görünen bebek, prematüre ve 8 günden küçükler kapsam dışıdır (tam sepsis değerlendirmesi).',
      '8-21 gün: idrar, kan ve BOS incelemesi; parenteral antibiyotik ve yatış.',
      '22-28 gün: idrar, kan kültürü ve inflamatuvar belirteçler (ateş yüksekliği, prokalsitonin, mutlak nötrofil sayısı, CRP). Belirteçlerden biri anormalse BOS alınır; hepsi normalse ve bebek yatırılıp kültürleri alındıysa BOS isteğe bağlıdır.',
      '29-60 gün: idrar ve inflamatuvar belirteçler normalse lomber ponksiyon gerekmez; belirteçler anormalse aileyle ortak karar.',
      'Anormal belirteç eşikleri için kılavuz tablosunu teyit et.',
    ],
    teyit:
      'Yaş grupları, 38,0 °C eşiği ve LP kararları AAP 2021 özetlerinden doğrulandı. Belirteç eşikleri (prokalsitonin, CRP, MNS, ateş) bu aramada doğrulanamadığı için karta yazılmadı.',
  },
  {
    id: 'sepsis-septik-sok',
    title: 'Sepsis ve septik şok (çocuk)',
    sources: 'Surviving Sepsis Campaign Çocuk Kılavuzu 2020',
    cases: ['S24', 'S77', 'Y18', 'S66', 'S96', 'S08', 'S62', 'S93'],
    keywords: ['sepsis', 'septik', 'sok', 'bolus', 'kristaloid', 'antibiyotik', 'adrenalin', 'noradrenalin', 'vazoaktif', 'laktat', 'perfuzyon', 'hipotansiyon'],
    body: [
      'Şok bulguları: kapiller dolum uzaması, soğuk ya da beneklenmiş ekstremite, bilinç değişikliği, oligüri, laktat yüksekliği; hipotansiyon geç bulgudur.',
      'Antibiyotik: septik şokta tanıdan sonra ilk 1 saat içinde; kültürleri al ama antibiyotiği geciktirme.',
      'Sıvı (yoğun bakım imkânı varsa): 10-20 ml/kg bolus, her bolustan sonra yeniden değerlendirme; şok düzelene veya sıvı yüklenmesi bulgusu çıkana kadar. Albümin yerine kristaloid; mümkünse dengeli kristaloid.',
      'Yoğun bakım imkânı yoksa: hipotansiyon yoksa bolus verilmez.',
      'Sıvıya yanıtsız şokta vazoaktif ajan: adrenalin veya noradrenalin (dopamin yerine).',
    ],
    teyit:
      '10-20 ml/kg bolus, yoğun bakım yoksa bolus kısıtlaması, kristaloid/dengeli kristaloid, adrenalin/noradrenalin ve 1 saat antibiyotik SSC 2020 kaynaklarından doğrulandı. "İlk saatte 40-60 ml/kg" ve şoksuz sepsiste 3 saat kuralı doğrulanamadığı için karta yazılmadı.',
  },
]

// Arama için Türkçe karakterleri sadeleştir (web/src/lib.js normalize ile aynı mantık).
export function fold(text = '') {
  return String(text)
    .replace(/İ/g, 'i')
    .replace(/I/g, 'ı')
    .toLowerCase()
    .replace(/ğ/g, 'g')
    .replace(/ü/g, 'u')
    .replace(/ş/g, 's')
    .replace(/ı/g, 'i')
    .replace(/ö/g, 'o')
    .replace(/ç/g, 'c')
}

// Vaka ve soruya göre en ilgili kartları seç (en fazla `limit` kart).
// Vaka bitmeden, yalnızca vaka kimliğine bağlı kart seçilmez (kart başlığı tanıyı ele verebilir);
// vaka bağı sadece soruda eşleşen anahtar kelime varken sıralamayı güçlendirir.
export function pickGuidelines(caseId, question, { finished = false, limit = 3 } = {}) {
  // Kelime başından eşleştir: "sok" -> "sok, soku" evet; "kosok" hayır
  const q = ` ${fold(question).replace(/[^a-z0-9]+/g, ' ')}`
  const scored = GUIDELINES.map((g) => {
    let score = 0
    for (const k of g.keywords) if (q.includes(` ${k}`)) score += 2
    if (g.cases.includes(caseId) && (finished || score > 0)) score += 5
    return { g, score }
  })
    .filter((x) => x.score > 0)
    .sort((a, b) => b.score - a.score)
  return scored.slice(0, limit).map((x) => x.g)
}

export function formatGuidelines(cards) {
  return cards
    .map((g) => [`### ${g.title}  [Kaynak: ${g.sources}]`, ...g.body.map((l) => `- ${l}`)].join('\n'))
    .join('\n\n')
}
