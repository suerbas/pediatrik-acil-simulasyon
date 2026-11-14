import erbBenchmarkTrees from "./erb_benchmark_trees.json";

export const ERB_BENCHMARK_TREES = erbBenchmarkTrees;

export const ANATOMICAL_TERRITORIES = {
  Inferior: {
    leads: ["II", "III", "aVF"],
    artery: "RCA (%80) veya LCx (%20)",
    reciprocal: ["I", "aVL"],
    description:
      "Alt duvar miyokard perfüzyonu; RCA tutulumunda sağ ventrikül (V4R) ve posterior (V7-V9) değerlendirme önerilir.",
  },
  Septal: {
    leads: ["V1", "V2"],
    artery: "Proksimal LAD (Septal perforatörler)",
    reciprocal: ["Posterior/Inferior (duruma göre)"],
    description:
      "İnterventriküler septum bölgesi; sağ dal bloğu veya Brugada paterni açısından da dikkatle incelenir.",
  },
  Anterior: {
    leads: ["V3", "V4"],
    artery: "LAD (Sol Ön İnen Arter)",
    reciprocal: ["II", "III", "aVF"],
    description:
      "Ön duvar bölgesi; V1-V4 birlikte tutulduğunda antero-septal, V1-V6 + I/aVL tutulduğunda yaygın anterior.",
  },
  Lateral: {
    leads: ["I", "aVL", "V5", "V6"],
    artery: "LCx (Sirkumfleks) veya LAD Diyagonal dallar",
    reciprocal: ["II", "III", "aVF", "V1"],
    description: "Yüksek lateral (I, aVL) ve apikal-lateral (V5, V6) segmentler.",
  },
  aVR: {
    leads: ["aVR"],
    artery: "Sol Ana Koroner (LMCA), Proksimal LAD veya 3-Damar Hastalığı",
    reciprocal: ["Yaygın ST depresyonu (I, II, V4-V6)"],
    description:
      "aVR'de >= 1 mm ST elevasyonu ile birlikte >= 6 derivasyonda yaygın ST depresyonu kritik LMCA/ağır iskemi uyarısıdır.",
  },
};

export const CLINICAL_CRITERIA_KB = [
  {
    id: "stemi",
    title: "Akut STEMI Tanı Kriterleri (ESC/AHA 4. Evrensel Tanım)",
    urgency: "CRITICAL",
    summary: "Anatomik olarak komşu en az 2 derivasyonda J noktasında yeni gelişen ST elevasyonu.",
    criteria: [
      "Genel derivasyonlar (I, II, III, aVL, aVF, V1, V4-V6): >= 1 mm (0.1 mV) ST elevasyonu.",
      "V2 ve V3 derivasyonları için cinsiyet/yaş eşikleri: >= 40 yaş erkek >= 2.0 mm; < 40 yaş erkek >= 2.5 mm; tüm kadınlar >= 1.5 mm.",
      "Resiprokal ST depresyonu (ör. İnferior STEMI'de I ve aVL'de depresyon) tanıyı güçlü şekilde destekler.",
      "V7-V9'da >= 0.5 mm elevasyon (veya V1-V3'te derin ST depresyonu + uzun R) posterior MI lehinedir.",
    ],
  },
  {
    id: "av_blocks",
    title: "Atriyoventriküler (AV) Blok Dereceleri",
    urgency: "URGENT",
    summary: "Atriyal uyarıların ventriküllere iletim gecikmesi veya kesintisi.",
    criteria: [
      "1. Derece AV Blok: PR aralığı sabit ve > 200 ms (> 5 küçük kare), her P dalgasını QRS takip eder.",
      "2. Derece Mobitz Tip I (Wenckebach): PR aralığı progresif olarak uzar ve sonunda bir P dalgası iletilmez (QRS düşer).",
      "2. Derece Mobitz Tip II: Sabit PR aralığı varken aniden iletilmeyen P dalgaları görülür (yüksek tam blok riski).",
      "3. Derece (Tam) AV Blok: P dalgaları ile QRS kompleksleri tamamen bağımsızdır (AV disosiyasyon); atriyal hız > ventriküler hız.",
    ],
  },
  {
    id: "bundle_branch_blocks",
    title: "Dal Blokları (RBBB / LBBB) ve Sgarbossa Kriterleri",
    urgency: "URGENT",
    summary: "QRS süresi >= 120 ms (>= 3 küçük kare) ile karakterize intraventriküler iletim gecikmeleri.",
    criteria: [
      "Sağ Dal Bloğu (RBBB): QRS >= 120 ms; V1-V2'de rSR' ('tavşan kulağı') paterni; I ve V6'da derin/geniş S dalgası.",
      "Sol Dal Bloğu (LBBB): QRS >= 120 ms; I, aVL, V5-V6'da geniş çentikli monofazik R dalgası (Q yok); V1-V3'te derin rS veya QS.",
      "Sgarbossa Kriterleri (LBBB'de Akut MI): (1) Pozitif QRS'li derivasyonda >= 1 mm konkordan ST elevasyonu (5 puan); (2) V1-V3'te >= 1 mm konkordan ST depresyonu (3 puan); (3) Modifiye Smith kuralı: ST/S oranı <= -0.25 olan aşırı diskordan elevasyon.",
    ],
  },
  {
    id: "afib_aflutter",
    title: "Atriyal Fibrilasyon (AF) ve Atriyal Flutter",
    urgency: "URGENT",
    summary: "En sık görülen sürekli supraventriküler aritmiler.",
    criteria: [
      "Atriyal Fibrilasyon: Düzensiz-düzensiz (irregularly irregular) R-R aralıkları, belirgin P dalgası yokluğu, düzensiz f (fibrilasyon) dalgaları.",
      "Hızlı Ventrikül Yanıtlı AF (RVR): Ventriküler hız > 100-110/dk.",
      "Atriyal Flutter: Tipik testere dişi (sawtooth) F dalgaları (en iyi II, III, aVF ve V1'de), atriyal hız ~250-350/dk (genellikle 2:1 blokla 150/dk düzenli ritim).",
    ],
  },
  {
    id: "lvh",
    title: "Sol Ventrikül Hipertrofisi (LVH) Voltaj Kriterleri",
    urgency: "ROUTINE",
    summary: "Artmış sol ventrikül miyokard kütlesine bağlı yüksek QRS voltajı ve sekonder repolarizasyon değişikliği.",
    criteria: [
      "Sokolow-Lyon Kriteri: S(V1) + R(V5 veya V6) >= 35 mm (3.5 mV) veya R(aVL) >= 11 mm.",
      "Cornell Kriteri: Erkeklerde R(aVL) + S(V3) > 28 mm; kadınlarda > 20 mm.",
      "LVH Strain Paterni: Lateral derivasyonlarda (V5-V6, I, aVL) asimetrik ST depresyonu ve T dalgası inversiyonu.",
    ],
  },
  {
    id: "wellens_brugada",
    title: "Yüksek Riskli İskemik ve Kanalopati Paternleri (Wellens & Brugada)",
    urgency: "CRITICAL",
    summary: "Ani kardiyak ölüm veya yakın proksimal LAD tıkanıklığı habercisi kritik paternler.",
    criteria: [
      "Wellens Sendromu (Proksimal LAD kritik darlığı): V2-V3'te ağrısız dönemde bile bifazik (Tip A) veya derin simetrik T negatifliği (Tip B), ST elevasyonu belirgin değildir.",
      "Brugada Tip 1 Paterni: V1-V2'de >= 2 mm kubbeli (coved) ST elevasyonu ve ardından negatif T dalgası (ani aritmik ölüm riski).",
      "De Winter Paterni: V1-V6'da J noktasında yukarı eğimli ST depresyonu + uzun, simetrik hiperakut T dalgaları (LAD tıkanıklığı eşdeğeri).",
    ],
  },
];

export const SAMPLE_CASES = [
  {
    id: "nsr",
    title: "Normal Sinüs Ritmi (75/dk)",
    subtitle: "Sağlıklı tarama EKG'si — Referans Vaka",
    age: 34,
    sex: "Erkek",
    chief_complaint: "Check-up / Spor öncesi rutin değerlendirme",
    history: "Bilinen kardiyak hastalık yok, asemptomatik.",
    notes: "Düzenli kalp atımı, normal kardiyak eksen ve normal ST-T segmenti.",
    expected_hr: 75,
  },
  {
    id: "inferior_stemi",
    title: "Akut İnferior STEMI (68/dk)",
    subtitle: "II, III, aVF ST Elevasyonu + I, aVL Resiprokal Depresyon",
    age: 62,
    sex: "Erkek",
    chief_complaint: "1 saattir süren baskı tarzında retrosternal göğüs ağrısı ve soğuk terleme",
    history: "Hipertansiyon, 30 paket-yıl sigara öyküsü, hiperlipidemi.",
    notes: "TA: 105/65 mmHg, bulantı eşlik ediyor. Acil reperfüzyon açısından değerlendirilmeli.",
    expected_hr: 68,
  },
  {
    id: "afib",
    title: "Hızlı Ventrikül Yanıtlı Atriyal Fibrilasyon (~132/dk)",
    subtitle: "Düzensiz R-R aralıkları, P dalgası yokluğu, f dalgaları",
    age: 71,
    sex: "Kadın",
    chief_complaint: "3 saattir başlayan çarpıntı, nefes darlığı ve baş dönmesi",
    history: "Hipertansiyon, hipotiroidi. Antikoagülan kullanmıyor.",
    notes: "Nabız düzensiz ve hızlı. İnme riski (CHA2DS2-VASc) ve hız kontrolü açısından değerlendirilmeli.",
    expected_hr: 132,
  },
];

function normalizeSex(sex) {
  const text = String(sex ?? "").trim().toLocaleLowerCase("tr");
  if (["erkek", "e", "male", "m"].includes(text)) return "male";
  if (["kadın", "kadin", "k", "female", "f"].includes(text)) return "female";
  return null;
}

function parseAge(age) {
  if (age === null || age === undefined || String(age).trim() === "") return null;
  const val = Number(String(age).trim().replace(",", "."));
  return Number.isFinite(val) && val >= 0 && val <= 130 ? val : null;
}

/**
 * Bazett ve Fridericia ile QTc hesaplar; erişkinde cinsiyete özgü eşiklerle sınıflar.
 * Erişkin eşikleri (Goldenberg, Moss & Zareba 2006): Erkek sınırda 431-450, uzamış > 450 ms;
 * Kadın sınırda 451-470, uzamış > 470 ms. backend/clinical_guidelines.py ile birebir aynı tutulmalıdır.
 */
export function calculateQtc(qtMs, hrBpm, { sex = null, age = null } = {}) {
  const qt = Number(qtMs);
  const hr = Number(hrBpm);
  if (!Number.isFinite(qt) || !Number.isFinite(hr) || !(qt > 0) || !(hr > 0)) {
    throw new Error("QT süresi (ms) ve kalp hızı (bpm) pozitif değerler olmalıdır.");
  }
  const rrSec = 60.0 / hr;
  const bazett = qt / Math.sqrt(rrSec);
  const fridericia = qt / Math.cbrt(rrSec);
  // Bazett taşikardide fazla, bradikardide eksik düzeltir; 60-100/dk dışında Fridericia esas alınır
  const useBazett = hr >= 60 && hr <= 100;
  const refQtc = useBazett ? bazett : fridericia;

  const sexNorm = normalizeSex(sex);
  const ageVal = parseAge(age);
  let borderlineGt = 450;
  let prolongedGt = 470;
  let basis = "Cinsiyet belirtilmedi: erkekte > 450 ms, kadında > 470 ms uzamış kabul edilir";
  if (ageVal !== null && ageVal < 16) {
    basis = "< 16 yaş: erişkin eşikleri doğrudan uygulanamaz, pediatrik değerlendirme gerekir";
  } else if (sexNorm === "male") {
    borderlineGt = 430;
    prolongedGt = 450;
    basis = "Erkek eşiği: sınırda 431-450 ms, uzamış > 450 ms";
  } else if (sexNorm === "female") {
    basis = "Kadın eşiği: sınırda 451-470 ms, uzamış > 470 ms";
  }

  let interpretation = `NORMAL (${basis})`;
  let level = "NORMAL";
  if (refQtc >= 500) {
    interpretation = "KRİTİK UZAMIŞ (>= 500 ms — Torsades de Pointes riski)";
    level = "CRITICAL";
  } else if (refQtc > prolongedGt) {
    interpretation = `UZAMIŞ (${basis})`;
    level = "URGENT";
  } else if (refQtc > borderlineGt) {
    interpretation = `SINIRDA (${basis})`;
    level = "BORDERLINE";
  } else if (refQtc < 350) {
    interpretation = "KISA QT (< 350 ms)";
    level = "URGENT";
  }

  return {
    qt_ms: Number(qt.toFixed(1)),
    hr_bpm: Number(hr.toFixed(1)),
    rr_sec: Number(rrSec.toFixed(3)),
    qtc_bazett_ms: Number(bazett.toFixed(1)),
    qtc_fridericia_ms: Number(fridericia.toFixed(1)),
    reference_qtc_ms: Number(refQtc.toFixed(1)),
    recommended_formula: useBazett ? "Bazett" : "Fridericia (HR 60-100 dışı)",
    threshold_basis: basis,
    interpretation,
    level,
  };
}

export function summarizeCaliperAndQtc(caliperMeasurements, patientContext = {}) {
  if (!caliperMeasurements || Object.keys(caliperMeasurements).length === 0) {
    return { has_measurements: false, computed_qtc: null, summary_lines: [], raw: {} };
  }

  const lines = [];
  for (const [key, val] of Object.entries(caliperMeasurements)) {
    if (val !== null && val !== undefined && val !== "") {
      lines.push(`- ${key}: ${val}`);
    }
  }

  const parseNum = (raw) => {
    if (typeof raw === "number") return raw;
    if (typeof raw === "string") {
      const m = raw.match(/(\d+(?:\.\d+)?)/);
      if (m) return Number(m[1]);
    }
    return null;
  };

  const qtCandidate = parseNum(caliperMeasurements.QT) ?? parseNum(caliperMeasurements.qt_ms);
  const rrCandidate = parseNum(caliperMeasurements["R-R"]) ?? parseNum(caliperMeasurements.rr_ms);
  let hrCandidate = parseNum(caliperMeasurements.HR) ?? parseNum(caliperMeasurements.hr_bpm);
  if (rrCandidate && rrCandidate > 150 && !hrCandidate) {
    hrCandidate = Number((60000.0 / rrCandidate).toFixed(1));
  }

  let computedQtc = null;
  if (qtCandidate > 0 && hrCandidate > 0) {
    try {
      computedQtc = calculateQtc(qtCandidate, hrCandidate, {
        sex: patientContext?.sex,
        age: patientContext?.age,
      });
      lines.push(
        `- Uygulama Tarafından Hesaplanan QTc (Bazett): ${computedQtc.qtc_bazett_ms} ms | Fridericia: ${computedQtc.qtc_fridericia_ms} ms | Esas alınan: ${computedQtc.recommended_formula} = ${computedQtc.reference_qtc_ms} ms -> ${computedQtc.interpretation}`
      );
    } catch {
      computedQtc = null;
    }
  }

  return {
    has_measurements: lines.length > 0,
    computed_qtc: computedQtc,
    summary_lines: lines,
    raw: caliperMeasurements,
  };
}

export function formatGuidelinesForPrompt() {
  const lines = ["=== ESC/AHA KLİNİK TANI KRİTERLERİ REFERANS BİLGİ BANKASI ==="];
  for (const item of CLINICAL_CRITERIA_KB) {
    lines.push(`\n[${item.title}] (Öncelik: ${item.urgency})`);
    for (const c of item.criteria) {
      lines.push(`  - ${c}`);
    }
  }
  lines.push("\n[Anatomik Duvarlar ve Derivasyon Eşleşmesi]");
  for (const [wall, info] of Object.entries(ANATOMICAL_TERRITORIES)) {
    lines.push(`  - ${wall}: ${info.leads.join(", ")} -> ${info.artery}`);
  }

  const diagnoses = ERB_BENCHMARK_TREES?.diagnoses || {};
  if (Object.keys(diagnoses).length > 0) {
    lines.push("\n=== Jwoo5/ECG-Reasoning-Benchmark 17 TANI KARAR VE GÖRSEL DOĞRULAMA (GROUNDING) ZİNCİRLERİ ===");
    for (const [dxKey, dxInfo] of Object.entries(diagnoses)) {
      const chain = (dxInfo.steps || [])
        .map((s) => {
          const gTypes = (s.grounding_steps || []).map((g) => g.question_type).join(", ");
          return `${s.criterion} (${gTypes || "kriter kontrolü"})`;
        })
        .join(" -> ");
      lines.push(`  - ${dxKey} (${dxInfo.display_name || dxKey}): ${chain}`);
    }
  }
  return lines.join("\n");
}

export function buildClinicalPrompt(patientContext = {}, caliperMeasurements = {}) {
  const caliperInfo = summarizeCaliperAndQtc(caliperMeasurements, patientContext);
  const age = patientContext.age || "Belirtilmedi";
  const sex = patientContext.sex || "Belirtilmedi";
  const complaint = patientContext.chief_complaint || "Belirtilmedi";
  const history = patientContext.history || "Belirtilmedi";
  const notes = patientContext.notes || "Yok";

  const caliperBlock = caliperInfo.has_measurements
    ? caliperInfo.summary_lines.join("\n")
    : "Kullanıcı dijital pergel ölçümü girmedi; görseldeki kalibrasyon ve karelerden tahmin yapın.";

  return `Sen kıdemli bir kardiyoloji uzmanısın. Sana verilen tam 12 derivasyonlu EKG görüntüsünü ve yakınlaştırılmış bölgesel derivasyon kırpmalarını (I-III, aVR-aVF, V1-V3, V4-V6 ve Ritim Şeridi) inceleyerek adım adım klinik akıl yürütme (ECG-Reasoning-Benchmark protokolü) yapacaksın.

ÖNEMLİ KURALLAR:
1. Görüntüde gerçekten görmediğin hiçbir dalga değişikliğini varsayma (görsel doğrulama zorunludur).
2. Eğer kullanıcı dijital pergel (caliper) ölçümleri sağladıysa, aralık ve hız hesaplarında bu ölçümleri kesin referans olarak kullan. "Uygulama Tarafından Hesaplanan QTc" satırı varsa QTc'yi yeniden hesaplama; verilen değeri ve yorumu aynen kullan.
3. Doğrudan tanıya atlama; aşağıdaki 6 adımı ve erb_reasoning_chain alanını sırasıyla doldur ve SADECE geçerli bir JSON objesi döndür.
4. Dil tamamen Türkçe, tıbbi terminoloji ise uluslararası kardiyoloji standardında olmalıdır.
5. Bölge kırpmaları standart 3x4 + ritim şeridi düzeni varsayılarak sabit oranlarla alınmıştır. Kağıt düzeni farklıysa kırpma etiketlerine güvenme; derivasyonları görseldeki yazılı etiketlerden tanı ve emin olamadığın derivasyonu belirt.
6. Görüntü kalitesi bir bulguyu değerlendirmeye yetmiyorsa tahmin yürütme; ilgili alana "Değerlendirilemedi" yaz ve duvar durumunu "UNASSESSED" olarak işaretle.

=== HASTA KLİNİK BİLGİLERİ ===
- Yaş / Cinsiyet: ${age} / ${sex}
- Başvuru Şikayeti: ${complaint}
- Özgeçmiş / Risk Faktörleri: ${history}
- Ek Klinik Notlar: ${notes}

=== DİJİTAL PERGEL (CALIPER) ÖLÇÜMLERİ ===
${caliperBlock}

${formatGuidelinesForPrompt()}

=== İSTENEN ÇIKTI JSON ŞEMASI ===
{
  "step1_calibration_quality": {
    "status": "ADEQUATE" | "SUBOPTIMAL",
    "paper_speed_and_gain": "25 mm/s ve 10 mm/mV kalibrasyon durumu",
    "image_quality_notes": "Görüntü netliği, bazal hat kayması veya artefakt değerlendirmesi",
    "findings": ["Gözlem 1", "Gözlem 2"]
  },
  "step2_rate_rhythm": {
    "heart_rate_bpm": 75,
    "rhythm_regularity": "Düzenli" | "Düzensiz-düzensiz" | "Düzenli düzensiz",
    "p_wave_assessment": "P dalgası varlığı, morfolojisi ve ekseni",
    "av_relationship": "Her P'yi QRS takip ediyor mu?",
    "summary": "Adım 2 klinik özeti"
  },
  "step3_axis": {
    "axis_classification": "Normal Eksen" | "Sol Aks Deviasyonu" | "Sağ Aks Deviasyonu" | "Aşırı Sağ Aks",
    "lead_i_polarity": "Pozitif / Bifazik / Negatif",
    "lead_avf_polarity": "Pozitif / Bifazik / Negatif",
    "summary": "Adım 3 eksen açıklaması"
  },
  "step4_intervals": {
    "pr_interval_ms": "PR değeri ve yorumu",
    "qrs_duration_ms": "QRS değeri ve dar/geniş yorumu",
    "qt_qtc_ms": "QT / QTc değerlendirmesi",
    "caliper_used": ${caliperInfo.has_measurements},
    "summary": "Adım 4 aralık analizi özeti"
  },
  "step5_morphology_st_t": {
    "territories": [
      { "wall": "Inferior (II, III, aVF)", "st_segment": "...", "t_wave": "...", "q_wave": "...", "status": "NORMAL" | "ABNORMAL" | "RECIPROCAL" | "UNASSESSED" },
      { "wall": "Septal & Anterior (V1-V4)", "st_segment": "...", "t_wave": "...", "q_wave": "...", "status": "NORMAL" | "ABNORMAL" | "RECIPROCAL" | "UNASSESSED" },
      { "wall": "Lateral (I, aVL, V5, V6)", "st_segment": "...", "t_wave": "...", "q_wave": "...", "status": "NORMAL" | "ABNORMAL" | "RECIPROCAL" | "UNASSESSED" },
      { "wall": "aVR", "st_segment": "...", "t_wave": "...", "q_wave": "...", "status": "NORMAL" | "ABNORMAL" | "RECIPROCAL" | "UNASSESSED" }
    ],
    "summary": "Morfoloji ve anatomik duvar tutulum özeti"
  },
  "step6_clinical_synthesis": {
    "primary_diagnosis": "En olası ana EKG tanısı",
    "urgency": "CRITICAL" | "URGENT" | "ROUTINE",
    "confidence_score": 85,
    "differential_diagnoses": [{ "diagnosis": "...", "likelihood": "...", "rationale": "..." }],
    "red_flags": ["Acil bulgular (yoksa boş liste)"],
    "guideline_matches": ["Eşleşen ESC/AHA kılavuz kriteri"],
    "recommended_actions": ["Somut sonraki klinik/tanısal adımlar"]
  },
  "erb_reasoning_chain": {
    "target_dx": "17 benchmark tanısından en uygunu; hiçbiri uymuyorsa normal_sinus_rhythm, atrial_fibrillation veya other",
    "steps": [
      {
        "criterion_selection": "Seçilen klinik kriter",
        "finding_identification": "Kriterin görselde karşılanıp karşılanmadığı",
        "ecg_grounding": {
          "lead_grounding": ["Lead II", "Lead III"],
          "wave_grounding": "Dalga/segment",
          "measurement_grounding": "Ölçüm değeri"
        },
        "diagnostic_decision": "Doğrulandı" | "Ek bulgu gerekli" | "Dışlandı"
      }
    ]
  }
}`;
}
