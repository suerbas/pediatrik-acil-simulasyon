import {
  buildClinicalPrompt,
  SAMPLE_CASES,
  summarizeCaliperAndQtc,
} from "./clinicalData.js";

const LLM_TIMEOUT_MS = 120000;

const EXPECTED_STEP_KEYS = [
  "step1_calibration_quality",
  "step2_rate_rhythm",
  "step3_axis",
  "step4_intervals",
  "step5_morphology_st_t",
  "step6_clinical_synthesis",
];

const URGENT_COMPLAINT_KEYWORDS = ["göğüs", "ağrı", "senkop", "bayıl", "nefes", "çarpıntı"];

function extractJsonBlock(rawText) {
  let text = String(rawText || "").trim();
  if (text.startsWith("```")) {
    text = text.replace(/^```(?:json)?\s*/i, "").replace(/\s*```$/, "");
  }
  try {
    return JSON.parse(text);
  } catch {
    const match = text.match(/\{[\s\S]*\}/);
    if (match) {
      return JSON.parse(match[0]);
    }
    throw new Error("Model çıktısı geçerli JSON formatında ayrıştırılamadı.");
  }
}

function loadImageElement(src) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = () => reject(new Error("Görsel tarayıcı tarafından okunamadı."));
    img.src = src;
  });
}

function readFileAsDataUrl(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result);
    reader.onerror = () => reject(new Error("Dosya okunamadı."));
    reader.readAsDataURL(file);
  });
}

function assessImageQuality(rgba, width, height) {
  const step = Math.max(1, Math.floor(Math.min(width, height) / 400));
  let sum = 0;
  let sumSq = 0;
  let count = 0;

  const grayAt = (x, y) => {
    const idx = (y * width + x) * 4;
    return 0.299 * rgba[idx] + 0.587 * rgba[idx + 1] + 0.114 * rgba[idx + 2];
  };

  for (let y = 0; y < height; y += step) {
    for (let x = 0; x < width; x += step) {
      const g = grayAt(x, y);
      sum += g;
      sumSq += g * g;
      count += 1;
    }
  }

  const brightness = count ? sum / count : 128;
  const variance = count ? Math.max(0, sumSq / count - brightness * brightness) : 0;
  const contrast = Math.sqrt(variance);

  // Yaklaşık Laplacian netlik skoru
  let lapSum = 0;
  let lapSq = 0;
  let lapCount = 0;
  // Komşular 1 px uzaklıktan alınır (cv2.Laplacian ile aynı çekirdek); `step` yalnızca örnekleme sıklığıdır.
  // Komşuları da `step` kadar uzaktan almak bulanık fotoğraflarda skoru yapay olarak yükseltiyordu.
  for (let y = 1; y < height - 1; y += step) {
    for (let x = 1; x < width - 1; x += step) {
      const lap =
        grayAt(x - 1, y) +
        grayAt(x + 1, y) +
        grayAt(x, y - 1) +
        grayAt(x, y + 1) -
        4 * grayAt(x, y);
      lapSum += lap;
      lapSq += lap * lap;
      lapCount += 1;
    }
  }
  const lapMean = lapCount ? lapSum / lapCount : 0;
  const sharpnessScore = lapCount ? Math.max(0, lapSq / lapCount - lapMean * lapMean) : 0;

  const warnings = [];
  if (Math.min(width, height) < 600) {
    warnings.push("Düşük çözünürlük: Küçük kareler ve P dalgaları belirsiz olabilir.");
  }
  if (sharpnessScore < 45) {
    warnings.push("Bulanıklık tespit edildi: Netlik skoru düşük, çekimi sabitleyerek yinelemek önerilir.");
  }
  if (brightness < 65) {
    warnings.push("Görüntü karanlık: CLAHE Netleştirilmiş modu kullanmanız önerilir.");
  } else if (brightness > 245 && contrast < 15) {
    warnings.push("Görüntü aşırı parlak / düşük kontrastlı görünüyor.");
  }

  let overallStatus = "POOR";
  if (warnings.length === 0) overallStatus = "GOOD";
  else if (warnings.length === 1 && Math.min(width, height) >= 500) overallStatus = "FAIR";

  return {
    width,
    height,
    sharpness_score: Number(sharpnessScore.toFixed(1)),
    brightness: Number(brightness.toFixed(1)),
    contrast: Number(contrast.toFixed(1)),
    overall_status: overallStatus,
    warnings,
  };
}

function buildEnhancedCanvas(srcCanvas) {
  const { width, height } = srcCanvas;
  const ctx = srcCanvas.getContext("2d");
  const imgData = ctx.getImageData(0, 0, width, height);
  const data = imgData.data;

  // 2% - 98% parlaklık germe ile gölge/kontrast dengeleme
  const hist = new Uint32Array(256);
  const totalPixels = width * height;
  for (let i = 0; i < data.length; i += 4) {
    const lum = Math.round(0.299 * data[i] + 0.587 * data[i + 1] + 0.114 * data[i + 2]);
    hist[lum] += 1;
  }

  let low = 0;
  let high = 255;
  let acc = 0;
  const lowThresh = totalPixels * 0.015;
  const highThresh = totalPixels * 0.985;
  for (let i = 0; i < 256; i++) {
    acc += hist[i];
    if (acc >= lowThresh) {
      low = i;
      break;
    }
  }
  acc = 0;
  for (let i = 0; i < 256; i++) {
    acc += hist[i];
    if (acc >= highThresh) {
      high = i;
      break;
    }
  }
  const span = Math.max(30, high - low);

  const enhCanvas = document.createElement("canvas");
  enhCanvas.width = width;
  enhCanvas.height = height;
  const enhCtx = enhCanvas.getContext("2d");
  const outData = enhCtx.createImageData(width, height);
  const out = outData.data;

  for (let i = 0; i < data.length; i += 4) {
    for (let c = 0; c < 3; c++) {
      const v = ((data[i + c] - low) * 255) / span;
      out[i + c] = v < 0 ? 0 : v > 255 ? 255 : Math.round(v);
    }
    out[i + 3] = 255;
  }
  enhCtx.putImageData(outData, 0, 0);
  return enhCanvas;
}

function buildWaveformCanvas(enhCanvas) {
  const { width, height } = enhCanvas;
  const ctx = enhCanvas.getContext("2d");
  const data = ctx.getImageData(0, 0, width, height).data;

  const wfCanvas = document.createElement("canvas");
  wfCanvas.width = width;
  wfCanvas.height = height;
  const wfCtx = wfCanvas.getContext("2d");
  const outData = wfCtx.createImageData(width, height);
  const out = outData.data;

  for (let i = 0; i < data.length; i += 4) {
    // Pembe/kırmızı ızgarayı baskılamak için R kanalına yüksek ağırlık ver
    const weighted = 0.65 * data[i] + 0.25 * data[i + 1] + 0.1 * data[i + 2];
    const stretched = weighted >= 205 ? 255 : Math.max(0, Math.min(255, Math.round((weighted / 205) * 255)));
    out[i] = stretched;
    out[i + 1] = stretched;
    out[i + 2] = stretched;
    out[i + 3] = 255;
  }
  wfCtx.putImageData(outData, 0, 0);
  return wfCanvas;
}

function cropLeadRegions(enhCanvas) {
  const { width, height } = enhCanvas;
  const regions = [
    {
      id: "col1_limb",
      title: "I, II, III (Standart Ekstremite)",
      leads: ["I", "II", "III"],
      territory: "Ekstremite / İnferior (II, III) & Yüksek Lateral (I)",
      bbox: [0.04, 0.1, 0.29, 0.74],
    },
    {
      id: "col2_augmented",
      title: "aVR, aVL, aVF (Artırılmış)",
      leads: ["aVR", "aVL", "aVF"],
      territory: "Ana Koroner (aVR) / Yüksek Lateral (aVL) / İnferior (aVF)",
      bbox: [0.27, 0.1, 0.52, 0.74],
    },
    {
      id: "col3_septal_ant",
      title: "V1, V2, V3 (Septal / Anterior)",
      leads: ["V1", "V2", "V3"],
      territory: "Septal (V1-V2) & Anterior (V3) — LAD Alanı",
      bbox: [0.5, 0.1, 0.75, 0.74],
    },
    {
      id: "col4_ant_lat",
      title: "V4, V5, V6 (Anterior / Lateral)",
      leads: ["V4", "V5", "V6"],
      territory: "Anterior (V4) & Apikal-Lateral (V5-V6) — LAD / LCx",
      bbox: [0.73, 0.1, 0.97, 0.74],
    },
    {
      id: "rhythm_strip",
      title: "Ritim Şeridi (Uzun DII)",
      leads: ["II (Ritim)"],
      territory: "Hız, Ritim Düzeni, P Dalgası & AV İletim Analizi",
      bbox: [0.04, 0.72, 0.97, 0.96],
    },
  ];

  const crops = [];
  for (const reg of regions) {
    const [x1n, y1n, x2n, y2n] = reg.bbox;
    const x1 = Math.max(0, Math.floor(x1n * width));
    const y1 = Math.max(0, Math.floor(y1n * height));
    const cw = Math.max(1, Math.min(width - x1, Math.floor((x2n - x1n) * width)));
    const ch = Math.max(1, Math.min(height - y1, Math.floor((y2n - y1n) * height)));

    const cCanvas = document.createElement("canvas");
    cCanvas.width = cw;
    cCanvas.height = ch;
    const cCtx = cCanvas.getContext("2d");
    cCtx.drawImage(enhCanvas, x1, y1, cw, ch, 0, 0, cw, ch);

    crops.push({
      id: reg.id,
      title: reg.title,
      leads: reg.leads,
      territory: reg.territory,
      bbox: reg.bbox,
      image_b64: cCanvas.toDataURL("image/png"),
    });
  }
  return crops;
}

export async function preprocessEcgInBrowser(fileOrDataUrl) {
  const dataUrl =
    typeof fileOrDataUrl === "string" ? fileOrDataUrl : await readFileAsDataUrl(fileOrDataUrl);
  const img = await loadImageElement(dataUrl);

  let width = img.naturalWidth || img.width;
  let height = img.naturalHeight || img.height;
  const maxDim = 2000;
  if (Math.max(width, height) > maxDim) {
    const scale = maxDim / Math.max(width, height);
    width = Math.round(width * scale);
    height = Math.round(height * scale);
  }

  const origCanvas = document.createElement("canvas");
  origCanvas.width = width;
  origCanvas.height = height;
  const origCtx = origCanvas.getContext("2d");
  origCtx.drawImage(img, 0, 0, width, height);

  const origImgData = origCtx.getImageData(0, 0, width, height);
  const quality = assessImageQuality(origImgData.data, width, height);

  const enhCanvas = buildEnhancedCanvas(origCanvas);
  const wfCanvas = buildWaveformCanvas(enhCanvas);
  const leadCrops = cropLeadRegions(enhCanvas);

  return {
    original_b64: origCanvas.toDataURL("image/png"),
    enhanced_b64: enhCanvas.toDataURL("image/png"),
    waveform_b64: wfCanvas.toDataURL("image/png"),
    lead_crops: leadCrops,
    quality,
    dimensions: { width, height },
  };
}

function gaussian(t, center, width, amp) {
  const z = (t - center) / Math.max(width, 1e-4);
  return amp * Math.exp(-0.5 * z * z);
}

function synthesizeBeatMv(phaseSec, lead, caseId) {
  const leadPolarity = {
    I: [0.85, 0.9, 1.0],
    II: [1.1, 1.25, 1.15],
    III: [0.6, 0.75, 0.85],
    aVR: [-1.0, -1.0, -0.9],
    aVL: [0.45, 0.55, 0.6],
    aVF: [0.9, 1.0, 1.0],
    V1: [0.3, -1.1, 0.35],
    V2: [0.4, -0.7, 0.85],
    V3: [0.5, 0.2, 1.1],
    V4: [0.6, 1.3, 1.15],
    V5: [0.6, 1.45, 1.0],
    V6: [0.55, 1.2, 0.85],
  };
  const [pMul, rMul, tMul] = leadPolarity[lead] || [1.0, 1.0, 1.0];
  let val = 0;

  if (caseId !== "afib") {
    val += gaussian(phaseSec, 0.09, 0.022, 0.14 * pMul);
  }

  let qAmp = lead !== "aVR" && lead !== "V1" && lead !== "V2" ? -0.08 : 0.0;
  if (caseId === "inferior_stemi" && (lead === "II" || lead === "III" || lead === "aVF")) {
    qAmp = -0.28;
  }
  val += gaussian(phaseSec, 0.215, 0.008, qAmp);

  if (lead === "V1" || lead === "V2") {
    val += gaussian(phaseSec, 0.232, 0.01, lead === "V1" ? 0.28 : 0.55);
    val += gaussian(phaseSec, 0.252, 0.012, lead === "V1" ? -1.05 : -0.85);
  } else if (lead === "aVR") {
    val += gaussian(phaseSec, 0.242, 0.012, -1.05);
  } else {
    val += gaussian(phaseSec, 0.238, 0.011, 1.15 * Math.max(rMul, 0.35));
    val += gaussian(phaseSec, 0.26, 0.01, -0.22);
  }

  let stShift = 0;
  let tAmp = 0.28 * tMul;
  if (caseId === "inferior_stemi") {
    if (lead === "II" || lead === "III" || lead === "aVF") {
      stShift = lead === "II" ? 0.26 : 0.32;
      tAmp = 0.42;
    } else if (lead === "I" || lead === "aVL") {
      stShift = lead === "aVL" ? -0.18 : -0.14;
      tAmp = -0.22;
    }
  } else if (caseId === "afib") {
    tAmp = 0.16 * tMul;
  }

  // T dalgası zamanlaması: sinüs vakalarında QT ~370 ms (fizyolojik), hızlı AF'de daha kısa (~320 ms)
  const [tCenter, tWidth] = caseId === "afib" ? [0.42, 0.038] : [0.46, 0.041];

  if (phaseSec >= 0.265 && phaseSec <= tCenter + 0.01 && stShift !== 0) {
    const z = (phaseSec - 0.33) / 0.06;
    val += stShift * Math.exp(-0.5 * z * z);
  }
  val += gaussian(phaseSec, tCenter, tWidth, tAmp);
  return val;
}

function generateLeadSignal(lead, caseId, durationSec, fs = 250) {
  const n = Math.floor(durationSec * fs);
  const sig = new Float32Array(n);
  const rrList =
    caseId === "inferior_stemi"
      ? [0.88]
      : caseId === "afib"
      ? [0.38, 0.54, 0.35, 0.62, 0.41, 0.48, 0.37, 0.56, 0.42, 0.51, 0.39, 0.58, 0.4, 0.49, 0.36, 0.53]
      : [0.8];

  const beatStarts = [];
  let curr = 0.05;
  let idx = 0;
  while (curr < durationSec + 0.5) {
    beatStarts.push(curr);
    curr += rrList[idx % rrList.length];
    idx += 1;
  }

  if (caseId === "afib") {
    for (let i = 0; i < n; i++) {
      const t = i / fs;
      sig[i] +=
        0.035 * Math.sin(2 * Math.PI * 6.4 * t) +
        0.025 * Math.sin(2 * Math.PI * 8.7 * t + 1.1) +
        0.018 * Math.sin(2 * Math.PI * 11.3 * t + 2.3);
    }
  }

  for (const bStart of beatStarts) {
    const iStart = Math.max(0, Math.floor((bStart - 0.02) * fs));
    const iEnd = Math.min(n, Math.floor((bStart + 0.61) * fs));
    for (let i = iStart; i < iEnd; i++) {
      const phase = i / fs - bStart;
      if (phase >= 0 && phase <= 0.6) {
        sig[i] += synthesizeBeatMv(phase, lead, caseId);
      }
    }
  }
  return sig;
}

export async function generateSyntheticEcgInBrowser(caseId) {
  const meta = SAMPLE_CASES.find((c) => c.id === caseId);
  if (!meta) {
    throw new Error(`Bilinmeyen demo vaka kimliği: ${caseId}`);
  }

  const pxPerMm = 7;
  const width = 1900;
  const height = 1060;
  const canvas = document.createElement("canvas");
  canvas.width = width;
  canvas.height = height;
  const ctx = canvas.getContext("2d");

  ctx.fillStyle = "rgb(255, 252, 252)";
  ctx.fillRect(0, 0, width, height);

  // Milimetrik pembe ızgara
  ctx.lineWidth = 1;
  for (let x = 0; x < width; x += pxPerMm) {
    const isMajor = x % (pxPerMm * 5) === 0;
    ctx.strokeStyle = isMajor ? "rgb(244, 195, 195)" : "rgb(252, 232, 232)";
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, height);
    ctx.stroke();
  }
  for (let y = 0; y < height; y += pxPerMm) {
    const isMajor = y % (pxPerMm * 5) === 0;
    ctx.strokeStyle = isMajor ? "rgb(244, 195, 195)" : "rgb(252, 232, 232)";
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(width, y);
    ctx.stroke();
  }

  // Üst başlık bandı
  ctx.fillStyle = "rgb(255, 250, 250)";
  ctx.fillRect(0, 0, width, 96);
  ctx.strokeStyle = "rgb(210, 160, 160)";
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(0, 96);
  ctx.lineTo(width, 96);
  ctx.stroke();

  ctx.fillStyle = "rgb(40, 35, 35)";
  ctx.font = "bold 24px sans-serif";
  ctx.fillText(
    `ECG_HELPER SENTETİK KAYIT | Vaka: ${meta.title} | Yaş/Cinsiyet: ${meta.age}/${meta.sex} | 25 mm/s  10 mm/mV`,
    40,
    58
  );

  const gridLeft = 105;
  const pxPerSec = 25 * pxPerMm;
  const pxPerMv = 10 * pxPerMm;
  const rowBaselines = [215, 435, 655, 895];
  const leadLayout = [
    ["I", "aVR", "V1", "V4"],
    ["II", "aVL", "V2", "V5"],
    ["III", "aVF", "V3", "V6"],
  ];

  ctx.strokeStyle = "rgb(20, 20, 24)";
  ctx.lineWidth = 2.2;
  const calX0 = 42;
  for (const baseY of rowBaselines) {
    ctx.beginPath();
    ctx.moveTo(calX0, baseY);
    ctx.lineTo(calX0 + 12, baseY);
    ctx.lineTo(calX0 + 12, baseY - pxPerMv);
    ctx.lineTo(calX0 + 42, baseY - pxPerMv);
    ctx.lineTo(calX0 + 42, baseY);
    ctx.lineTo(calX0 + 54, baseY);
    ctx.stroke();
  }

  const fs = 250;
  const colWidthSec = 2.5;
  const colWidthPx = Math.floor(colWidthSec * pxPerSec);

  for (let rIdx = 0; rIdx < leadLayout.length; rIdx++) {
    const baseY = rowBaselines[rIdx];
    const rowLeads = leadLayout[rIdx];
    for (let cIdx = 0; cIdx < rowLeads.length; cIdx++) {
      const leadName = rowLeads[cIdx];
      const xOffset = gridLeft + cIdx * colWidthPx;
      const sig = generateLeadSignal(leadName, caseId, colWidthSec, fs);

      ctx.strokeStyle = "rgb(20, 20, 24)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i = 0; i < sig.length; i++) {
        const px = xOffset + (i / fs) * pxPerSec;
        const py = baseY - sig[i] * pxPerMv;
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = "rgb(110, 25, 25)";
      ctx.font = "bold 22px sans-serif";
      ctx.fillText(leadName, xOffset + 12, baseY - 78);

      if (cIdx > 0) {
        ctx.strokeStyle = "rgb(100, 60, 60)";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(xOffset, baseY - 25);
        ctx.lineTo(xOffset, baseY + 25);
        ctx.stroke();
      }
    }
  }

  // Uzun Ritim Şeridi (II)
  const rhythmBaseY = rowBaselines[3];
  const rhythmSig = generateLeadSignal("II", caseId, 10.0, fs);
  ctx.strokeStyle = "rgb(20, 20, 24)";
  ctx.lineWidth = 2;
  ctx.beginPath();
  for (let i = 0; i < rhythmSig.length; i++) {
    const px = gridLeft + (i / fs) * pxPerSec;
    const py = rhythmBaseY - rhythmSig[i] * pxPerMv;
    if (i === 0) ctx.moveTo(px, py);
    else ctx.lineTo(px, py);
  }
  ctx.stroke();

  ctx.fillStyle = "rgb(110, 25, 25)";
  ctx.font = "bold 22px sans-serif";
  ctx.fillText("II (Ritim Şeridi - 10 sn)", gridLeft + 12, rhythmBaseY - 78);

  const rawDataUrl = canvas.toDataURL("image/png");
  const processed = await preprocessEcgInBrowser(rawDataUrl);
  return {
    case: {
      ...meta,
      calibration: { px_per_mm: pxPerMm, paper_speed_mm_s: 25, gain_mm_mv: 10, width, height },
    },
    ...processed,
  };
}

export function generateDemoResponse(
  patientContext = {},
  caliperMeasurements = {},
  caseHint = null,
  quality = null,
  fallbackReason = null
) {
  const caliperInfo = summarizeCaliperAndQtc(caliperMeasurements, patientContext);
  const caliperUsed = caliperInfo.has_measurements;
  const caliperNote = caliperUsed
    ? " | Dijital pergel ölçümleri: " + caliperInfo.summary_lines.join("; ")
    : "";
  const qStatus = !quality || quality.overall_status !== "POOR" ? "ADEQUATE" : "SUBOPTIMAL";
  const qNotes =
    "Görsel ön işleme uygulandı. " +
    (quality?.warnings?.length ? quality.warnings.join(", ") : "Çözünürlük ve kontrast analiz için uygun.");

  const complaint = String(patientContext.chief_complaint || "").toLocaleLowerCase("tr");
  const urgentComplaint = URGENT_COMPLAINT_KEYWORDS.some((k) => complaint.includes(k));
  let result;

  if (caseHint === "inferior_stemi") {
    result = {
      step1_calibration_quality: {
        status: qStatus,
        paper_speed_and_gain: "25 mm/s hız ve 10 mm/mV kalibrasyon dikdörtgeni doğrulandı.",
        image_quality_notes: qNotes,
        findings: [
          "12 derivasyon + uzun DII ritim şeridi eksiksiz izleniyor.",
          "Izgara çizgileri net, bazal hat artefaktı saptanmadı.",
        ],
      },
      step2_rate_rhythm: {
        heart_rate_bpm: 68,
        rhythm_regularity: "Düzenli",
        p_wave_assessment: "I, II, aVF'de pozitif, aVR'de negatif sinüs P dalgaları seçiliyor.",
        av_relationship: "1:1 AV iletim mevcut (PR sabit). İnferior MI seyrinde AV blok gelişimi açısından yakın takip gerekir.",
        summary: "68/dk hızında düzenli Sinüs Ritmi.",
      },
      step3_axis: {
        axis_classification: "Normal Eksen",
        lead_i_polarity: "Pozitif (QRS ağırlıklı yukarı)",
        lead_avf_polarity: "Pozitif (QRS ağırlıklı yukarı)",
        summary: "I (+) ve aVF (+) olduğundan QRS ekseni normal aralıkta (~ +45° ile +60°).",
      },
      step4_intervals: {
        pr_interval_ms: "160 ms (Normal, 120-200 ms arası)" + caliperNote,
        qrs_duration_ms: "90 ms (Dar QRS, < 120 ms)",
        qt_qtc_ms: caliperInfo.computed_qtc
          ? `Hesaplanan Bazett QTc: ${caliperInfo.computed_qtc.qtc_bazett_ms} ms`
          : "QT ~370 ms, QTc ~395 ms (Normal sınırlarda)",
        caliper_used: caliperUsed,
        summary: "İletim süreleri normal sınırlarda; dal bloğu veya uzamış QT saptanmadı.",
      },
      step5_morphology_st_t: {
        territories: [
          {
            wall: "Inferior (II, III, aVF)",
            st_segment: "II, III ve aVF derivasyonlarında J noktasında 2.5 - 3.2 mm konveks (kubbeli) ST elevasyonu.",
            t_wave: "ST elevasyonu ile birleşen hiperakut/belirgin pozitif T dalgaları.",
            q_wave: "III ve aVF'de gelişmekte olan Q dalgaları.",
            status: "ABNORMAL",
          },
          {
            wall: "Septal & Anterior (V1-V4)",
            st_segment: "İzoelektrik hatta yakın.",
            t_wave: "Normal morfoloji.",
            q_wave: "Patolojik Q yok.",
            status: "NORMAL",
          },
          {
            wall: "Lateral (I, aVL, V5, V6)",
            st_segment: "I ve özellikle aVL'de 1.5 - 2.0 mm belirgin resiprokal ST depresyonu.",
            t_wave: "I ve aVL'de T dalgası negatifliği.",
            q_wave: "Yok.",
            status: "RECIPROCAL",
          },
          { wall: "aVR", st_segment: "İzoelektrik.", t_wave: "Negatif.", q_wave: "Yok.", status: "NORMAL" },
        ],
        summary: "İnferior duvarda (II, III, aVF) akut transmural iskemi ile uyumlu ST elevasyonu ve yüksek lateralde (I, aVL) klasik resiprokal ST depresyonu.",
      },
      step6_clinical_synthesis: {
        primary_diagnosis: "Akut İnferior ST-Elevasyonlu Miyokard İnfarktüsü (İnferior STEMI)",
        urgency: "CRITICAL",
        confidence_score: 95,
        differential_diagnoses: [
          {
            diagnosis: "Akut Perikardit",
            likelihood: "Düşük",
            rationale: "Resiprokal ST depresyonunun (I, aVL) varlığı ve bölgesel dağılım perikarditten uzaklaştırır.",
          },
          {
            diagnosis: "Erken Repolarizasyon",
            likelihood: "Çok Düşük",
            rationale: "Konveks ST morfolojisi ve resiprokal değişikliklerle uyumsuzdur.",
          },
        ],
        red_flags: [
          "ACİL REPERFÜZYON ENDİKASYONU: Primer PKG (PCI) veya trombolitik zaman penceresi aktive edilmeli.",
          "Sağ Ventrikül İnfarktüsü ekartasyonu için mutlaka V4R çekilmeli (RV tutulumunda nitratlar kontrendikedir).",
          "Posterior tutulum için V7-V9 çekilmesi ve bradiaritmi/AV blok açısından monitörizasyon önerilir.",
        ],
        guideline_matches: [
          "ESC/AHA Akut STEMI Kriteri: Komşu >= 2 inferior derivasyonda (II, III, aVF) >= 1 mm ST elevasyonu.",
          "Anatomik Eşleşme: Muhtemel Sağ Koroner Arter (RCA) oklüzyonu.",
        ],
        recommended_actions: [
          "Acil Kardiyoloji / Kateter Laboratuvarı aktivasyonu (Kapı-balon süresi < 90 dk).",
          "Sağ (V4R) ve posterior (V7-V9) derivasyonlarla 18 derivasyonlu EKG kaydı.",
          "Kılavuzlara uygun antiagregan/antikoagülan tedavi ve sürekli ritim monitörizasyonu.",
        ],
      },
      erb_reasoning_chain: {
        target_dx: "inferior_myocardial_infarction",
        steps: [
          {
            criterion_selection: "İnferior derivasyonlarda J-noktasında ST-segment elevasyonu varlığı",
            finding_identification:
              "Evet — II, III ve aVF derivasyonlarında komşu >= 2 derivasyonda > 1 mm ST elevasyonu ve I, aVL'de resiprokal depresyon mevcut.",
            ecg_grounding: {
              lead_grounding: ["Lead II", "Lead III", "Lead aVF"],
              wave_grounding: "QRS sonrası J-noktası ve ST segmenti",
              measurement_grounding: "2.6 - 3.2 mm ST elevasyonu",
            },
            diagnostic_decision: "Doğrulandı",
          },
        ],
      },
    };
  } else if (caseHint === "afib") {
    result = {
      step1_calibration_quality: {
        status: qStatus,
        paper_speed_and_gain: "25 mm/s hız ve 10 mm/mV kalibrasyon doğrulandı.",
        image_quality_notes: qNotes,
        findings: [
          "Uzun DII ritim şeridi ritim düzensizliğini doğrulamak için yeterli netlikte.",
          "Bazal hatta hızlı fibrilasyon osilasyonları görülebiliyor.",
        ],
      },
      step2_rate_rhythm: {
        heart_rate_bpm: 132,
        rhythm_regularity: "Düzensiz-düzensiz (Irregularly irregular)",
        p_wave_assessment: "Organize sinüs P dalgası seçilmiyor; yerine bazal hatta düzensiz fibrilasyon (f) dalgaları mevcut.",
        av_relationship: "AV düğüm üzerinden değişken refrakterlik ile düzensiz ventriküler yanıt.",
        summary: "Ortalama ~132/dk ventrikül hızlı Atriyal Fibrilasyon (AF with RVR).",
      },
      step3_axis: {
        axis_classification: "Normal Eksen",
        lead_i_polarity: "Pozitif",
        lead_avf_polarity: "Pozitif",
        summary: "QRS ekseni normal aralıkta.",
      },
      step4_intervals: {
        pr_interval_ms: "Ölçülemez (P dalgası yok)",
        qrs_duration_ms: "88 ms (Dar QRS — supraventriküler iletim)" + caliperNote,
        qt_qtc_ms: caliperInfo.computed_qtc
          ? `Hesaplanan QTc (Fridericia): ${caliperInfo.computed_qtc.qtc_fridericia_ms} ms`
          : "Düzensiz R-R nedeniyle ortalama QT değerlendirmesi gerekir (~415 ms)",
        caliper_used: caliperUsed,
        summary: "Dar QRS kompleksi supraventriküler kökeni doğrular; aberran iletim saptanmadı.",
      },
      step5_morphology_st_t: {
        territories: [
          { wall: "Inferior (II, III, aVF)", st_segment: "İzoelektrik.", t_wave: "Düşük amplitüdlü pozitif.", q_wave: "Yok.", status: "NORMAL" },
          { wall: "Septal & Anterior (V1-V4)", st_segment: "İzoelektrik.", t_wave: "Normal.", q_wave: "Yok.", status: "NORMAL" },
          { wall: "Lateral (I, aVL, V5, V6)", st_segment: "Belirgin iskemi yok.", t_wave: "Hafif düzleşmiş.", q_wave: "Yok.", status: "NORMAL" },
          { wall: "aVR", st_segment: "İzoelektrik.", t_wave: "Negatif.", q_wave: "Yok.", status: "NORMAL" },
        ],
        summary: "Akut ST elevasyonlu iskemi bulgusu yok; hızlı ventriküler yanıta bağlı hafif repolarizasyon düzleşmesi izleniyor.",
      },
      step6_clinical_synthesis: {
        primary_diagnosis: "Hızlı Ventrikül Yanıtlı Atriyal Fibrilasyon (AFib with RVR)",
        urgency: "URGENT",
        confidence_score: 93,
        differential_diagnoses: [
          { diagnosis: "Değişken Bloklu Atriyal Flutter", likelihood: "Düşük-Orta", rationale: "Tipik düzenli testere dişi F dalgaları izlenmediğinden AF ön plandadır." },
          { diagnosis: "Multifokal Atriyal Taşikardi (MAT)", likelihood: "Düşük", rationale: "Belirgin farklı P dalgaları yerine kaotik f dalgaları mevcut." },
        ],
        red_flags: [
          "Hemodinamik instabilite varsa acil senkronize kardiyoversiyon düşünülmelidir.",
          "Antikoagülan kullanmayan hastada başlangıç süresi (> 48 saat veya belirsiz) tromboembolik risk açısından kritiktir.",
        ],
        guideline_matches: [
          "ESC AF Kılavuzu: Düzensiz R-R aralıkları + belirgin P dalgası yokluğu = Atriyal Fibrilasyon.",
          "CHA2DS2-VASc skoru hesaplanmalı.",
        ],
        recommended_actions: [
          "Hemodinamik durumun ve vital bulguların değerlendirilmesi.",
          "Altta yatan tetikleyicilerin taranması (TSH, elektrolitler, enfeksiyon, anemi).",
          "Hız kontrolü ve CHA2DS2-VASc / HAS-BLED ile antikoagülasyon planlanması.",
        ],
      },
      erb_reasoning_chain: {
        target_dx: "atrial_fibrillation",
        steps: [
          {
            criterion_selection: "R-R aralıklarının düzensizliği (Irregularly irregular RR intervals)",
            finding_identification: "Evet — Uzun DII ritim şeridinde ardışık R-R mesafeleri tamamen düzensiz.",
            ecg_grounding: {
              lead_grounding: ["Lead II (Ritim Şeridi)"],
              wave_grounding: "R-R aralıkları (QRS tepeleri arası)",
              measurement_grounding: "Ortalama ~132/dk",
            },
            diagnostic_decision: "Ek bulgu gerekli",
          },
          {
            criterion_selection: "Organize P dalgalarının yokluğu ve bazal f dalgaları",
            finding_identification: "Evet — Düzenli P dalgası izlenmiyor, bazal hatta fibrilasyon osilasyonları mevcut.",
            ecg_grounding: {
              lead_grounding: ["Lead II", "Lead V1"],
              wave_grounding: "İzoelektrik hat / PR bölgesi",
              measurement_grounding: "P dalgası yok",
            },
            diagnostic_decision: "Doğrulandı",
          },
        ],
      },
    };
  } else if (caseHint === "nsr") {
    result = {
      step1_calibration_quality: {
        status: qStatus,
        paper_speed_and_gain: "25 mm/s hız ve 10 mm/mV kalibrasyon doğrulandı.",
        image_quality_notes: qNotes,
        findings: ["Tüm 12 derivasyon ve ritim şeridi temiz ve artefaktsız."],
      },
      step2_rate_rhythm: {
        heart_rate_bpm: 75,
        rhythm_regularity: "Düzenli",
        p_wave_assessment: "I, II, aVF'de pozitif, aVR'de negatif sinüs P dalgaları.",
        av_relationship: "Sabit PR aralığı ile 1:1 AV iletim.",
        summary: "75/dk hızında Normal Sinüs Ritmi.",
      },
      step3_axis: {
        axis_classification: "Normal Eksen",
        lead_i_polarity: "Pozitif",
        lead_avf_polarity: "Pozitif",
        summary: "Kardiyak eksen normal kadran (-30° ile +90° arası) içerisinde.",
      },
      step4_intervals: {
        pr_interval_ms: "160 ms (Normal)" + caliperNote,
        qrs_duration_ms: "85 ms (Dar, normal)",
        qt_qtc_ms: caliperInfo.computed_qtc
          ? `Hesaplanan Bazett QTc: ${caliperInfo.computed_qtc.qtc_bazett_ms} ms`
          : "QT ~370 ms, QTc ~415 ms (Normal)",
        caliper_used: caliperUsed,
        summary: "PR, QRS ve QTc süreleri normal fizyolojik sınırlarda.",
      },
      step5_morphology_st_t: {
        territories: [
          { wall: "Inferior (II, III, aVF)", st_segment: "İzoelektrik", t_wave: "Pozitif", q_wave: "Yok", status: "NORMAL" },
          { wall: "Septal & Anterior (V1-V4)", st_segment: "İzoelektrik", t_wave: "Normal", q_wave: "Yok", status: "NORMAL" },
          { wall: "Lateral (I, aVL, V5, V6)", st_segment: "İzoelektrik", t_wave: "Pozitif", q_wave: "Fizyolojik q", status: "NORMAL" },
          { wall: "aVR", st_segment: "İzoelektrik", t_wave: "Negatif", q_wave: "Yok", status: "NORMAL" },
        ],
        summary: "Akut iskemi, hipertrofi veya iletim bozukluğu bulgusu izlenmedi.",
      },
      step6_clinical_synthesis: {
        primary_diagnosis: "Normal 12-Derivasyonlu EKG (Normal Sinüs Ritmi)",
        urgency: "ROUTINE",
        confidence_score: 96,
        differential_diagnoses: [],
        red_flags: [],
        guideline_matches: ["Kalp hızı (60-100/dk), PR (120-200 ms), QRS (<120 ms) ve ST-T normal referans aralığındadır."],
        recommended_actions: ["Klinik bulgularla uyumlu ise ek acil EKG girişimi gerekmez.", "Semptom halinde seri EKG takibi önerilir."],
      },
      erb_reasoning_chain: {
        target_dx: "normal_sinus_rhythm",
        steps: [
          {
            criterion_selection: "1:1 AV iletim ve sinüs P dalga ekseni (I, II pozitif; aVR negatif)",
            finding_identification: "Evet — Her P dalgasını sabit PR aralığı ile dar bir QRS kompleksi izliyor.",
            ecg_grounding: {
              lead_grounding: ["Lead I", "Lead II", "Lead aVR"],
              wave_grounding: "P dalgası ve PR segmenti",
              measurement_grounding: "PR ~160 ms, QRS ~85 ms, Hız 75/dk",
            },
            diagnostic_decision: "Doğrulandı",
          },
        ],
      },
    };
  } else {
    const hrFromCaliper = caliperInfo.computed_qtc ? Math.round(caliperInfo.computed_qtc.hr_bpm) : null;
    result = {
      step1_calibration_quality: {
        status: qStatus === "SUBOPTIMAL" ? "SUBOPTIMAL" : "UNASSESSED",
        paper_speed_and_gain: "Görsel üzerindeki kalibrasyon (genellikle 25 mm/s, 10 mm/mV) hekim tarafından doğrulanmalıdır.",
        image_quality_notes: qNotes,
        findings: [
          "Görüntü ön işleme ve 5 anatomik bölge kırpması tamamlandı.",
          "Sağ üstteki 'API Ayarları' bölümünden OpenRouter API anahtarınızı girerek canlı MLLM okuması yapabilirsiniz.",
        ],
      },
      step2_rate_rhythm: {
        heart_rate_bpm: hrFromCaliper,
        rhythm_regularity: "Çevrimdışı Demo Modu — Canlı LLM bağlantısı gerektirir",
        p_wave_assessment: "DII ritim şeridi kırpmasından her QRS öncesi P dalgası varlığını kontrol ediniz.",
        av_relationship: "PR sabitliğini ardışık atımlarda dijital pergel ile doğrulayınız.",
        summary: "Özel fotoğraf yüklendi; canlı görsel ritim çıkarımı için OpenRouter API anahtarı yapılandırılmalıdır.",
      },
      step3_axis: {
        axis_classification: "Görsel Kontrol Bekleniyor",
        lead_i_polarity: "Sol üst sütun (I) kırpmasından kontrol ediniz",
        lead_avf_polarity: "2. sütun alt (aVF) kırpmasından kontrol ediniz",
        summary: "I (+) ve aVF (+) ise normal eksen değerlendirmesi yapılır.",
      },
      step4_intervals: {
        pr_interval_ms: String(caliperInfo.raw?.PR || "Dijital pergel ile ölçülebilir"),
        qrs_duration_ms: String(caliperInfo.raw?.QRS || "Dijital pergel ile ölçülebilir"),
        qt_qtc_ms: caliperInfo.computed_qtc
          ? `Hesaplanan Bazett QTc: ${caliperInfo.computed_qtc.qtc_bazett_ms} ms`
          : "QT ve R-R ölçümü girildiğinde otomatik hesaplanır",
        caliper_used: caliperUsed,
        summary: caliperUsed
          ? "Girdiğiniz pergel ölçümleri kaydedildi" + caliperNote
          : "Tuval üzerindeki 'Dijital Pergel' aracını kullanarak PR, QRS ve QT ölçebilirsiniz.",
      },
      step5_morphology_st_t: {
        territories: [
          { wall: "Inferior (II, III, aVF)", st_segment: "Kırpılmış bölgelerden J noktasını inceleyiniz.", t_wave: "T polaritesi kontrolü.", q_wave: "Patolojik Q kontrolü.", status: "UNASSESSED" },
          { wall: "Septal & Anterior (V1-V4)", st_segment: "V2-V3 ST elevasyon eşiklerine dikkat ediniz.", t_wave: "Wellens Tip A/B kontrolü.", q_wave: "R progresyonu kontrolü.", status: "UNASSESSED" },
        ],
        summary: "Yapılandırılmış 6 adımlı şablon hazır; canlı görsel tanı yorumu için OpenRouter API anahtarı ekleyebilirsiniz.",
      },
      step6_clinical_synthesis: {
        primary_diagnosis: "Canlı LLM Görsel Analizi İçin API Anahtarı Bekleniyor (Ön İşleme Tamamlandı)",
        // Görsel okunmadığı için EKG'ye dayalı aciliyet atanamaz; "ROUTINE" yanlış güvence verir
        urgency: urgentComplaint ? "URGENT" : "UNASSESSED",
        confidence_score: 0,
        differential_diagnoses: [],
        red_flags: urgentComplaint
          ? [`Hasta şikayeti ('${patientContext.chief_complaint}') nedeniyle yüksek klinik öncelik ile hekim değerlendirmesi önerilir.`]
          : ["Bu EKG henüz yorumlanmadı; aşağıdaki şablon bir tanı veya 'normal' sonucu değildir."],
        guideline_matches: ["Görüntü ön işleme ve anatomik derivasyon kırpma adımları başarıyla tamamlandı."],
        recommended_actions: [
          "Sağ üstteki 'API Ayarları' butonundan OpenRouter API anahtarınızı ve modelinizi girerek '6 Adımlı Klinik Analizi Başlat' butonuna basın.",
          "Ya da üst/sol menüden hazır Demo Vakaları yükleyerek tam yapay zekâ muhakemesini test edin.",
        ],
      },
      erb_reasoning_chain: {
        target_dx: "awaiting_live_mllm_grounding",
        steps: [
          {
            criterion_selection: "Jwoo5/ecg-reasoning-benchmark 17 tanı karar ağacı prompta bağlandı",
            finding_identification: "Canlı MLLM çağrısı yapıldığında görsel bulgular otomatik doğrulanacaktır.",
            ecg_grounding: {
              lead_grounding: ["I-III", "aVR-aVF", "V1-V3", "V4-V6", "Ritim Şeridi"],
              wave_grounding: "Tüm derivasyon kırpmaları modele gönderilmeye hazır",
              measurement_grounding: caliperNote.replace(/^ \| /, "") || "Dijital pergel ölçümü bekleniyor",
            },
            diagnostic_decision: "Ek bulgu gerekli",
          },
        ],
      },
    };
  }

  return {
    ...result,
    mode: "demo_simulation",
    model_used: "Klinik Simülasyon Motoru (Çevrimdışı / Tarayıcı Demo)",
    ...(fallbackReason ? { fallback_note: fallbackReason } : {}),
    computed_qtc: caliperInfo.computed_qtc,
    disclaimer:
      "Bu çıktı eğitim ve klinik karar destek amaçlıdır; kesin tanı ve tedavi kararı hekim değerlendirmesi gerektirir.",
  };
}

async function fetchWithTimeout(url, options) {
  try {
    return await fetch(url, { ...options, signal: AbortSignal.timeout(LLM_TIMEOUT_MS) });
  } catch (err) {
    if (err?.name === "TimeoutError" || err?.name === "AbortError") {
      throw new Error(`Model ${LLM_TIMEOUT_MS / 1000} sn içinde yanıt vermedi (zaman aşımı).`);
    }
    throw err;
  }
}

function validateLlmPayload(parsed) {
  if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) {
    throw new Error("Model çıktısı bir JSON nesnesi değil.");
  }
  const hasStep = EXPECTED_STEP_KEYS.some((k) => parsed[k] && typeof parsed[k] === "object");
  if (!hasStep) {
    throw new Error("Model çıktısında beklenen 6 adımlı şema alanları bulunamadı.");
  }
  return parsed;
}

/** Tam görüntü + bölge kırpmalarını, modele gönderilecek açıklayıcı etiketleriyle eşler. */
function buildLabeledImages(enhancedB64, leadCrops) {
  const images = [];
  if (enhancedB64) {
    images.push({
      label: "GÖRSEL 1 — Tam 12 derivasyonlu EKG görüntüsü (kontrastı iyileştirilmiş).",
      uri: enhancedB64,
    });
  }
  for (const crop of (leadCrops || []).slice(0, 5)) {
    if (!crop?.image_b64) continue;
    images.push({
      label:
        `GÖRSEL ${images.length + 1} — Yakınlaştırılmış bölge kırpması (beklenen içerik: ${crop.title || crop.id}). ` +
        "Kırpma standart 3x4 + ritim şeridi düzeni varsayılarak sabit oranlarla alınmıştır; " +
        "derivasyon kimliğini kağıt üzerindeki yazılı etiketlerden doğrula.",
      uri: crop.image_b64,
    });
  }
  return images;
}

async function callOpenAiCompatibleBrowser({ apiKey, modelName, baseUrl, prompt, images, isOpenRouter }) {
  const contentParts = [{ type: "text", text: prompt }];
  for (const img of images) {
    contentParts.push({ type: "text", text: img.label });
    contentParts.push({ type: "image_url", image_url: { url: img.uri, detail: "high" } });
  }

  const headers = {
    "Content-Type": "application/json",
    Authorization: `Bearer ${apiKey}`,
  };
  if (isOpenRouter) {
    headers["HTTP-Referer"] = window.location.origin;
    headers["X-Title"] = "ECG_Helper";
  }

  const endpoint = `${baseUrl.replace(/\/+$/, "")}/chat/completions`;
  const baseBody = {
    model: modelName,
    messages: [{ role: "user", content: contentParts }],
  };

  let res = await fetchWithTimeout(endpoint, {
    method: "POST",
    headers,
    body: JSON.stringify({ ...baseBody, temperature: 0.15, response_format: { type: "json_object" } }),
  });

  // Yalnızca "parametre desteklenmiyor" türü hatalarda (400/422) yalın istekle yinele.
  // 401/402/429 gibi hatalarda aynı isteği tekrarlamak kota tüketmekten başka işe yaramaz.
  if (res.status === 400 || res.status === 422) {
    res = await fetchWithTimeout(endpoint, {
      method: "POST",
      headers,
      body: JSON.stringify(baseBody),
    });
  }

  if (!res.ok) {
    const errText = await res.text();
    throw new Error(`API Hatası (${res.status}): ${errText.slice(0, 220)}`);
  }

  const data = await res.json();
  const content = data?.choices?.[0]?.message?.content;
  if (!content) {
    throw new Error("Model boş yanıt döndürdü.");
  }
  return extractJsonBlock(content);
}

async function callGeminiBrowser({ apiKey, modelName, prompt, images }) {
  const parts = [{ text: prompt }];
  for (const img of images) {
    const match = /^data:(image\/[a-zA-Z0-9.+-]+);base64,(.+)$/s.exec(img.uri || "");
    if (!match) continue;
    parts.push({ text: img.label });
    parts.push({ inline_data: { mime_type: match[1], data: match[2] } });
  }

  // Anahtar URL sorgu dizesi yerine başlıkta gönderilir (URL'ler geçmişe ve günlüklere yazılır)
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(
    modelName
  )}:generateContent`;

  const res = await fetchWithTimeout(url, {
    method: "POST",
    headers: { "Content-Type": "application/json", "x-goog-api-key": apiKey },
    body: JSON.stringify({
      contents: [{ parts }],
      generationConfig: { responseMimeType: "application/json", temperature: 0.15 },
    }),
  });

  if (!res.ok) {
    const errText = await res.text();
    throw new Error(`Gemini API Hatası (${res.status}): ${errText.slice(0, 220)}`);
  }

  const data = await res.json();
  const text = (data?.candidates?.[0]?.content?.parts || [])
    .map((part) => part?.text || "")
    .join("");
  if (!text) {
    const reason = data?.promptFeedback?.blockReason || data?.candidates?.[0]?.finishReason;
    throw new Error(`Gemini boş yanıt döndürdü${reason ? ` (${reason})` : ""}.`);
  }
  return extractJsonBlock(text);
}

/** Vercel sunucusuz fonksiyonunda ortam değişkeniyle tanımlı bir anahtar olup olmadığını sorgular. */
export async function fetchServerlessStatus() {
  try {
    const res = await fetch("/api/analyze", { method: "GET" });
    const contentType = res.headers.get("content-type") || "";
    if (!res.ok || !contentType.includes("application/json")) return null;
    const data = await res.json();
    return data?.service === "ECG_Helper_Serverless" ? data : null;
  } catch {
    return null;
  }
}

export async function analyzeEcgClientOrServer({
  enhanced_b64,
  lead_crops = [],
  quality = null,
  patient_context = {},
  caliper_measurements = {},
  case_hint = null,
  localConfig = null,
  hasLocalFastApi = false,
}) {
  const caliperInfo = summarizeCaliperAndQtc(caliper_measurements, patient_context);
  const finalizeLive = (parsed, label) => ({
    ...validateLlmPayload(parsed),
    mode: "live_llm",
    model_used: label,
    computed_qtc: caliperInfo.computed_qtc,
    disclaimer:
      "Bu çıktı yapay zekâ klinik karar destek analizidir; kesin tanı ve tedavi kararı hekim değerlendirmesi gerektirir.",
  });
  const demoFallback = (reason = null) =>
    generateDemoResponse(patient_context, caliper_measurements, case_hint, quality, reason);

  // 1) Yerel FastAPI sunucusu aktifse sunucu üzerinden çalıştır
  if (hasLocalFastApi) {
    const res = await fetch("/api/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        enhanced_b64,
        lead_crops,
        quality,
        patient_context,
        caliper_measurements,
        case_hint,
      }),
    });
    if (!res.ok) {
      const errBody = await res.json().catch(() => ({}));
      const detail = typeof errBody.detail === "string" ? errBody.detail : "";
      throw new Error(detail || `Klinik analiz başarısız oldu (${res.status}).`);
    }
    return res.json();
  }

  // 2) Tarayıcıda (localStorage) kullanıcı anahtarı tanımlıysa sağlayıcıyı doğrudan çağır
  const provider = localConfig?.provider || "openrouter";
  const images = buildLabeledImages(enhanced_b64, lead_crops);
  const prompt = buildClinicalPrompt(patient_context, caliper_measurements);

  const liveCalls = {
    openrouter: {
      key: localConfig?.openrouter_api_key,
      label: "OpenRouter",
      model: localConfig?.openrouter_model || "google/gemini-3.8-flash",
      run: (apiKey, modelName) =>
        callOpenAiCompatibleBrowser({
          apiKey,
          modelName,
          baseUrl: localConfig?.openrouter_base_url || "https://openrouter.ai/api/v1",
          prompt,
          images,
          isOpenRouter: true,
        }),
    },
    gemini: {
      key: localConfig?.gemini_api_key,
      label: "Gemini",
      model: localConfig?.gemini_model || "gemini-2.0-flash",
      run: (apiKey, modelName) => callGeminiBrowser({ apiKey, modelName, prompt, images }),
    },
    openai: {
      key: localConfig?.openai_api_key,
      label: "OpenAI",
      model: localConfig?.openai_model || "gpt-4o",
      run: (apiKey, modelName) =>
        callOpenAiCompatibleBrowser({
          apiKey,
          modelName,
          baseUrl: "https://api.openai.com/v1",
          prompt,
          images,
          isOpenRouter: false,
        }),
    },
  };

  const active = liveCalls[provider];
  if (active?.key) {
    try {
      const parsed = await active.run(active.key, active.model);
      return finalizeLive(parsed, `${active.label} (${active.model})`);
    } catch (err) {
      return demoFallback(`${active.label} çağrısı başarısız oldu (${err.message}); demo simülasyona düşüldü.`);
    }
  }

  // 3) Vercel Serverless (/api/analyze): sunucu ortam değişkeninde anahtar tanımlıysa onu kullan
  let serverFailure = null;
  try {
    const res = await fetchWithTimeout("/api/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        prompt,
        image_uris: images.map((img) => img.uri),
        image_labels: images.map((img) => img.label),
        provider,
        model: active?.model || "",
      }),
    });
    const contentType = res.headers.get("content-type") || "";
    if (contentType.includes("application/json")) {
      const serverData = await res.json();
      if (res.ok && serverData?.mode === "live_llm") {
        return {
          ...validateLlmPayload(serverData),
          computed_qtc: caliperInfo.computed_qtc,
        };
      }
      if (serverData?.mode === "server_error") {
        serverFailure = serverData.error || `HTTP ${res.status}`;
      }
    }
  } catch (err) {
    // Sunucusuz endpoint yoksa (yerel `npm run dev`) sessizce demo simülasyona düş;
    // zaman aşımı veya şema hatası ise kullanıcıya bildir.
    if (/zaman aşımı|JSON|şema/i.test(err?.message || "")) {
      serverFailure = err.message;
    }
  }

  // 4) Canlı model kullanılamıyorsa tarayıcı içi demo simülasyonu döndür
  return demoFallback(
    serverFailure ? `Sunucu tarafı model çağrısı başarısız oldu (${serverFailure}); demo simülasyona düşüldü.` : null
  );
}
