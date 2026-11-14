"""OpenCV tabanlı EKG görüntü ön işleme, 12-derivasyon bölge kırpma ve sentetik EKG üreteci."""

import base64
import math
from typing import Dict, Any, List, Tuple

import cv2
import numpy as np


SAMPLE_CASES: Dict[str, Dict[str, Any]] = {
    "nsr": {
        "id": "nsr",
        "title": "Normal Sinüs Ritmi (75/dk)",
        "subtitle": "Sağlıklı tarama EKG'si — Referans Vaka",
        "age": 34,
        "sex": "Erkek",
        "chief_complaint": "Check-up / Spor öncesi rutin değerlendirme",
        "history": "Bilinen kardiyak hastalık yok, asemptomatik.",
        "notes": "Düzenli kalp atımı, normal kardiyak eksen ve normal ST-T segmenti.",
        "expected_hr": 75,
    },
    "inferior_stemi": {
        "id": "inferior_stemi",
        "title": "Akut İnferior STEMI (68/dk)",
        "subtitle": "II, III, aVF ST Elevasyonu + I, aVL Resiprokal Depresyon",
        "age": 62,
        "sex": "Erkek",
        "chief_complaint": "1 saattir süren baskı tarzında retrosternal göğüs ağrısı ve soğuk terleme",
        "history": "Hipertansiyon, 30 paket-yıl sigara öyküsü, hiperlipidemi.",
        "notes": "TA: 105/65 mmHg, bulantı eşlik ediyor. Acil reperfüzyon açısından değerlendirilmeli.",
        "expected_hr": 68,
    },
    "afib": {
        "id": "afib",
        "title": "Hızlı Ventrikül Yanıtlı Atriyal Fibrilasyon (~132/dk)",
        "subtitle": "Düzensiz R-R aralıkları, P dalgası yokluğu, f dalgaları",
        "age": 71,
        "sex": "Kadın",
        "chief_complaint": "3 saattir başlayan çarpıntı, nefes darlığı ve baş dönmesi",
        "history": "Hipertansiyon, hipotiroidi. Antikoagülan kullanmıyor.",
        "notes": "Nabız düzensiz ve hızlı. İnme riski (CHA2DS2-VASc) ve hız kontrolü açısından değerlendirilmeli.",
        "expected_hr": 132,
    },
}


def _encode_png_data_uri(img_bgr: np.ndarray) -> str:
    """OpenCV BGR görüntüsünü base64 PNG data URI formatına dönüştürür."""
    ok, buf = cv2.imencode(".png", img_bgr)
    if not ok:
        raise ValueError("Görüntü PNG olarak kodlanamadı.")
    b64 = base64.b64encode(buf.tobytes()).decode("ascii")
    return f"data:image/png;base64,{b64}"


def encode_image_bytes_to_png_b64(img_bgr: np.ndarray) -> bytes:
    """OpenCV BGR görüntüsünü ham PNG baytlarına çevirir."""
    ok, buf = cv2.imencode(".png", img_bgr)
    if not ok:
        raise ValueError("Görüntü PNG baytlarına çevrilemedi.")
    return buf.tobytes()


def assess_image_quality(img_bgr: np.ndarray) -> Dict[str, Any]:
    """EKG görüntüsünün çözünürlük, netlik (Laplacian) ve parlaklık kalitesini değerlendirir."""
    height, width = img_bgr.shape[:2]
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    sharpness_score = float(cv2.Laplacian(gray, cv2.CV_64F).var())
    brightness = float(np.mean(gray))
    contrast = float(np.std(gray))

    warnings: List[str] = []
    if min(width, height) < 600:
        warnings.append("Düşük çözünürlük: Küçük kareler ve P dalgaları belirsiz olabilir.")
    if sharpness_score < 45.0:
        warnings.append("Bulanıklık tespit edildi: Netlik skoru düşük, çekimi sabitleyerek yinelemek önerilir.")
    if brightness < 65.0:
        warnings.append("Görüntü karanlık: CLAHE netleştirilmiş modu kullanmanız önerilir.")
    elif brightness > 245.0 and contrast < 15.0:
        warnings.append("Görüntü aşırı parlak / düşük kontrastlı görünüyor.")

    if not warnings:
        overall_status = "GOOD"
    elif len(warnings) == 1 and min(width, height) >= 500:
        overall_status = "FAIR"
    else:
        overall_status = "POOR"

    return {
        "width": int(width),
        "height": int(height),
        "sharpness_score": round(sharpness_score, 1),
        "brightness": round(brightness, 1),
        "contrast": round(contrast, 1),
        "overall_status": overall_status,
        "warnings": warnings,
    }


def _enhance_clahe(img_bgr: np.ndarray) -> np.ndarray:
    """LAB renk uzayında L kanalına CLAHE uygulayarak gölgeleri dengeler ve dalgaları belirginleştirir."""
    lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
    l_chan, a_chan, b_chan = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.4, tileGridSize=(8, 8))
    l_eq = clahe.apply(l_chan)
    merged = cv2.merge((l_eq, a_chan, b_chan))
    return cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)


def _extract_high_contrast_waveform(img_bgr: np.ndarray) -> np.ndarray:
    """Pembe/kırmızı EKG ızgarasını baskılayıp siyah dalga formunu yüksek kontrastla öne çıkarır."""
    b_chan, g_chan, r_chan = cv2.split(img_bgr)
    # Pembe/kırmızı ızgaralar R kanalında parlak (beyaza yakın), siyah çizgi ise tüm kanallarda koyudur.
    weighted = cv2.addWeighted(r_chan, 0.65, g_chan, 0.25, 0.0)
    weighted = cv2.addWeighted(weighted, 0.90, b_chan, 0.10, 0.0)

    # Gölgeleri ve düzensiz aydınlatmayı gidermek için arka plan bölmesi
    kernel_size = max(31, (min(img_bgr.shape[:2]) // 18) | 1)
    background = cv2.GaussianBlur(weighted, (kernel_size, kernel_size), 0)
    background = np.clip(background, 1, 255)
    normalized = np.clip((weighted.astype(np.float32) / background.astype(np.float32)) * 245.0, 0, 255).astype(
        np.uint8
    )

    # Kontrast germe: koyu çizgileri siyah, açık ızgarayı beyaza yaklaştır
    _, thresh = cv2.threshold(normalized, 215, 255, cv2.THRESH_TRUNC)
    stretched = cv2.normalize(thresh, None, 0, 255, cv2.NORM_MINMAX)

    # Hafif morfolojik temizleme (ince kesintileri kapatmadan gürültüyü azalt)
    denoised = cv2.medianBlur(stretched, 3) if min(img_bgr.shape[:2]) >= 800 else stretched
    return cv2.cvtColor(denoised, cv2.COLOR_GRAY2BGR)


def crop_standard_leads(img_bgr: np.ndarray) -> List[Dict[str, Any]]:
    """Standart 4x3 + alt ritim şeridi EKG düzenine göre bölgesel yakınlaştırılmış kırpmalar üretir."""
    h, w = img_bgr.shape[:2]

    # Standart 12-derivasyon kağıdında üst %10 başlık, sol %5 kalibrasyon payı varsayılır
    regions = [
        {
            "id": "col1_limb",
            "title": "I, II, III (Standart Ekstremite)",
            "leads": ["I", "II", "III"],
            "territory": "Ekstremite / İnferior (II, III) & Yüksek Lateral (I)",
            "bbox": [0.04, 0.10, 0.29, 0.74],
        },
        {
            "id": "col2_augmented",
            "title": "aVR, aVL, aVF (Artırılmış)",
            "leads": ["aVR", "aVL", "aVF"],
            "territory": "Ana Koroner (aVR) / Yüksek Lateral (aVL) / İnferior (aVF)",
            "bbox": [0.27, 0.10, 0.52, 0.74],
        },
        {
            "id": "col3_septal_ant",
            "title": "V1, V2, V3 (Septal / Anterior)",
            "leads": ["V1", "V2", "V3"],
            "territory": "Septal (V1-V2) & Anterior (V3) — LAD Alanı",
            "bbox": [0.50, 0.10, 0.75, 0.74],
        },
        {
            "id": "col4_ant_lat",
            "title": "V4, V5, V6 (Anterior / Lateral)",
            "leads": ["V4", "V5", "V6"],
            "territory": "Anterior (V4) & Apikal-Lateral (V5-V6) — LAD / LCx",
            "bbox": [0.73, 0.10, 0.97, 0.74],
        },
        {
            "id": "rhythm_strip",
            "title": "Ritim Şeridi (Uzun DII)",
            "leads": ["II (Ritim)"],
            "territory": "Hız, Ritim Düzeni, P Dalgası & AV İletim Analizi",
            "bbox": [0.04, 0.72, 0.97, 0.96],
        },
    ]

    crops: List[Dict[str, Any]] = []
    for reg in regions:
        x1_n, y1_n, x2_n, y2_n = reg["bbox"]
        x1 = max(0, int(x1_n * w))
        y1 = max(0, int(y1_n * h))
        x2 = min(w, int(x2_n * w))
        y2 = min(h, int(y2_n * h))
        if x2 <= x1 or y2 <= y1:
            continue
        crop_img = img_bgr[y1:y2, x1:x2]
        crops.append(
            {
                "id": reg["id"],
                "title": reg["title"],
                "leads": reg["leads"],
                "territory": reg["territory"],
                "bbox": reg["bbox"],
                "image_b64": _encode_png_data_uri(crop_img),
            }
        )
    return crops


def preprocess_ecg_image(image_bytes: bytes) -> Dict[str, Any]:
    """Yüklenen EKG görüntüsünü decode eder, netleştirir, ızgarayı baskılar ve derivasyon kırpmalarını üretir."""
    arr = np.frombuffer(image_bytes, dtype=np.uint8)
    img_bgr = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img_bgr is None:
        raise ValueError("Geçersiz görsel dosyası: Görüntü OpenCV tarafından okunamadı.")

    # Çok büyük fotoğrafları performansı korumak için maksimum 2400px genişliğe orantılı ölçekle
    h, w = img_bgr.shape[:2]
    max_dim = 2400
    if max(w, h) > max_dim:
        scale = max_dim / float(max(w, h))
        img_bgr = cv2.resize(img_bgr, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)

    quality = assess_image_quality(img_bgr)
    enhanced_bgr = _enhance_clahe(img_bgr)
    waveform_bgr = _extract_high_contrast_waveform(enhanced_bgr)
    lead_crops = crop_standard_leads(enhanced_bgr)

    return {
        "original_b64": _encode_png_data_uri(img_bgr),
        "enhanced_b64": _encode_png_data_uri(enhanced_bgr),
        "waveform_b64": _encode_png_data_uri(waveform_bgr),
        "enhanced_bytes": encode_image_bytes_to_png_b64(enhanced_bgr),
        "lead_crops": lead_crops,
        "quality": quality,
        "dimensions": {"width": quality["width"], "height": quality["height"]},
    }


def _gaussian_wave(t: np.ndarray, center: float, width: float, amp: float) -> np.ndarray:
    """Belirli merkez, genişlik ve genlikte Gauss dalga bileşeni üretir."""
    return amp * np.exp(-0.5 * ((t - center) / max(width, 1e-4)) ** 2)


def _synthesize_beat_mv(
    phase_sec: float,
    lead: str,
    case_id: str,
) -> float:
    """Tek bir kalp atımı fazı (saniye cinsinden) için derivasyona özgü mV değeri üretir."""
    # Derivasyon yönelimi ve bazal amplitüd çarpanları
    lead_polarity = {
        "I": (0.85, 0.9, 1.0, 0.9),
        "II": (1.1, 1.25, 1.15, 1.1),
        "III": (0.6, 0.75, 0.85, 0.65),
        "aVR": (-1.0, -1.0, -0.9, -0.9),
        "aVL": (0.45, 0.55, 0.6, 0.5),
        "aVF": (0.9, 1.0, 1.0, 0.9),
        "V1": (0.3, -1.1, 0.35, -0.35),
        "V2": (0.4, -0.7, 0.85, 0.6),
        "V3": (0.5, 0.2, 1.1, 0.9),
        "V4": (0.6, 1.3, 1.15, 1.0),
        "V5": (0.6, 1.45, 1.0, 0.95),
        "V6": (0.55, 1.2, 0.85, 0.85),
    }
    p_mul, r_mul, t_mul, _ = lead_polarity.get(lead, (1.0, 1.0, 1.0, 1.0))

    val = 0.0
    t_arr = np.array([phase_sec], dtype=np.float32)

    # P dalgası (AF'de yok)
    if case_id != "afib":
        val += float(_gaussian_wave(t_arr, 0.09, 0.022, 0.14 * p_mul)[0])

    # Q dalgası
    q_amp = -0.08 if lead not in ("aVR", "V1", "V2") else 0.0
    if case_id == "inferior_stemi" and lead in ("II", "III", "aVF"):
        q_amp = -0.28  # Patolojik Q başlangıcı
    val += float(_gaussian_wave(t_arr, 0.215, 0.008, q_amp)[0])

    # R ve S dalgaları
    if lead in ("V1", "V2"):
        r_pos = 0.28 if lead == "V1" else 0.55
        s_neg = -1.05 if lead == "V1" else -0.85
        val += float(_gaussian_wave(t_arr, 0.232, 0.010, r_pos)[0])
        val += float(_gaussian_wave(t_arr, 0.252, 0.012, s_neg)[0])
    elif lead == "aVR":
        val += float(_gaussian_wave(t_arr, 0.242, 0.012, -1.05)[0])
    else:
        val += float(_gaussian_wave(t_arr, 0.238, 0.011, 1.15 * max(r_mul, 0.35))[0])
        val += float(_gaussian_wave(t_arr, 0.260, 0.010, -0.22)[0])

    # ST segmenti & T dalgası
    st_shift = 0.0
    t_amp = 0.28 * t_mul
    if case_id == "inferior_stemi":
        if lead in ("II", "III", "aVF"):
            st_shift = 0.32 if lead != "II" else 0.26  # 2.6 - 3.2 mm ST elevasyonu
            t_amp = 0.42  # Hiperakut/elevasyonlu T ile birleşen kubbeli ST
        elif lead in ("I", "aVL"):
            st_shift = -0.18 if lead == "aVL" else -0.14  # Resiprokal ST depresyonu
            t_amp = -0.22  # Resiprokal T negatifliği
    elif case_id == "afib":
        t_amp = 0.16 * t_mul

    # T dalgası zamanlaması: sinüs vakalarında QT ~370 ms (fizyolojik), hızlı AF'de daha kısa (~320 ms)
    t_center, t_width = (0.42, 0.038) if case_id == "afib" else (0.46, 0.041)

    # ST elevasyonu/depresyonu J noktasından (0.27s) T tepesine uzanan plato
    if 0.265 <= phase_sec <= t_center + 0.01 and st_shift != 0.0:
        plat = math.exp(-0.5 * ((phase_sec - 0.33) / 0.06) ** 2)
        val += st_shift * plat

    val += float(_gaussian_wave(t_arr, t_center, t_width, t_amp)[0])
    return val


def _generate_lead_signal(lead: str, case_id: str, duration_sec: float, fs: int = 250) -> np.ndarray:
    """Belirli bir süre (saniye) için derivasyon sinyalini (mV) üretir."""
    n_samples = int(duration_sec * fs)
    signal = np.zeros(n_samples, dtype=np.float32)

    if case_id == "nsr":
        rr_list = [0.80] * 20  # 75 bpm
    elif case_id == "inferior_stemi":
        rr_list = [0.88] * 20  # 68 bpm
    elif case_id == "afib":
        # Düzensiz-düzensiz R-R aralıkları (~132 bpm ortalama)
        rr_list = [0.38, 0.54, 0.35, 0.62, 0.41, 0.48, 0.37, 0.56, 0.42, 0.51, 0.39, 0.58, 0.40, 0.49, 0.36, 0.53] * 2
    else:
        rr_list = [0.80] * 20

    beat_starts: List[float] = []
    curr = 0.05
    idx = 0
    while curr < duration_sec + 0.5:
        beat_starts.append(curr)
        curr += rr_list[idx % len(rr_list)]
        idx += 1

    # AF için bazal fibrilasyon (f) dalgaları ekle
    t_axis = np.arange(n_samples, dtype=np.float32) / float(fs)
    if case_id == "afib":
        signal += (
            0.035 * np.sin(2 * np.pi * 6.4 * t_axis)
            + 0.025 * np.sin(2 * np.pi * 8.7 * t_axis + 1.1)
            + 0.018 * np.sin(2 * np.pi * 11.3 * t_axis + 2.3)
        )

    for b_start in beat_starts:
        i_start = max(0, int((b_start - 0.02) * fs))
        i_end = min(n_samples, int((b_start + 0.61) * fs))
        for i in range(i_start, i_end):
            phase = (i / float(fs)) - b_start
            if 0.0 <= phase <= 0.60:
                signal[i] += _synthesize_beat_mv(phase, lead, case_id)

    return signal


def _to_ascii(text: str) -> str:
    """OpenCV Hershey fontu için Türkçe karakterleri ASCII karşılıklarına dönüştürür."""
    trans = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
    return text.translate(trans)


def generate_synthetic_ecg(case_id: str) -> Tuple[bytes, Dict[str, Any]]:
    """Milimetrik pembe EKG kağıdı üzerinde 12-derivasyon + ritim şeridi sentetik EKG PNG üretir."""
    if case_id not in SAMPLE_CASES:
        raise ValueError(f"Bilinmeyen demo vaka kimliği: {case_id}")

    meta = SAMPLE_CASES[case_id]
    px_per_mm = 7
    width = 1900
    height = 1060

    # Açık krem/beyaz EKG kağıdı arka planı
    canvas = np.full((height, width, 3), (252, 252, 255), dtype=np.uint8)

    # Milimetrik 1 mm ve 5 mm pembe ızgara çizgileri
    minor_color = (232, 232, 252)
    major_color = (195, 195, 244)
    for x in range(0, width, px_per_mm):
        is_major = (x % (px_per_mm * 5)) == 0
        cv2.line(canvas, (x, 0), (x, height), major_color if is_major else minor_color, 1)
    for y in range(0, height, px_per_mm):
        is_major = (y % (px_per_mm * 5)) == 0
        cv2.line(canvas, (0, y), (width, y), major_color if is_major else minor_color, 1)

    # Üst başlık bandı
    cv2.rectangle(canvas, (0, 0), (width, 96), (250, 250, 255), -1)
    cv2.line(canvas, (0, 96), (width, 96), (160, 160, 210), 2)
    header_text = _to_ascii(
        f"ECG_HELPER SENTETIK TEST KAYDI  |  Vaka: {meta['title']}  |  "
        f"Yas/Cinsiyet: {meta['age']}/{meta['sex']}  |  25 mm/s   10 mm/mV"
    )
    cv2.putText(canvas, header_text, (40, 58), cv2.FONT_HERSHEY_SIMPLEX, 0.85, (35, 35, 60), 2, cv2.LINE_AA)

    # 4 satır yerleşimi: 3 standart satır (4x3) + 1 alt ritim şeridi (II)
    grid_left = 105
    grid_right = 1855  # 1750 px = 250 mm = 10.0 saniye (25 mm/s -> 175 px/s)
    px_per_sec = 25.0 * px_per_mm  # 175 px/s
    px_per_mv = 10.0 * px_per_mm   # 70 px/mV

    row_baselines = [215, 435, 655, 895]
    lead_layout = [
        ["I", "aVR", "V1", "V4"],
        ["II", "aVL", "V2", "V5"],
        ["III", "aVF", "V3", "V6"],
    ]

    trace_color = (20, 20, 24)
    col_width_sec = 2.5
    col_width_px = int(col_width_sec * px_per_sec)

    # Her satırın soluna 10 mm/mV kalibrasyon dikdörtgeni çiz
    cal_x0 = 42
    for base_y in row_baselines:
        cal_pts = np.array(
            [
                [cal_x0, base_y],
                [cal_x0 + 12, base_y],
                [cal_x0 + 12, base_y - px_per_mv],
                [cal_x0 + 42, base_y - px_per_mv],
                [cal_x0 + 42, base_y],
                [cal_x0 + 54, base_y],
            ],
            dtype=np.int32,
        )
        cv2.polylines(canvas, [cal_pts], False, trace_color, 2, cv2.LINE_AA)

    fs = 250
    # İlk 3 satır: 4 sütun x 2.5 sn
    for row_idx, leads_in_row in enumerate(lead_layout):
        base_y = row_baselines[row_idx]
        for col_idx, lead_name in enumerate(leads_in_row):
            x_offset = grid_left + col_idx * col_width_px
            sig = _generate_lead_signal(lead_name, case_id, col_width_sec, fs=fs)
            xs = (x_offset + (np.arange(len(sig)) / float(fs)) * px_per_sec).astype(np.int32)
            ys = (base_y - sig * px_per_mv).astype(np.int32)
            pts = np.column_stack((xs, ys)).reshape((-1, 1, 2))
            cv2.polylines(canvas, [pts], False, trace_color, 2, cv2.LINE_AA)

            # Derivasyon etiketi
            cv2.putText(
                canvas,
                lead_name,
                (x_offset + 12, base_y - 78),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.78,
                (15, 25, 110),
                2,
                cv2.LINE_AA,
            )
            # Sütun ayırıcı küçük işaret
            if col_idx > 0:
                cv2.line(canvas, (x_offset, base_y - 25), (x_offset, base_y + 25), (60, 60, 100), 2)

    # 4. satır: Uzun 10 saniyelik Ritim Şeridi (II)
    rhythm_base_y = row_baselines[3]
    rhythm_sig = _generate_lead_signal("II", case_id, 10.0, fs=fs)
    r_xs = (grid_left + (np.arange(len(rhythm_sig)) / float(fs)) * px_per_sec).astype(np.int32)
    r_ys = (rhythm_base_y - rhythm_sig * px_per_mv).astype(np.int32)
    r_pts = np.column_stack((r_xs, r_ys)).reshape((-1, 1, 2))
    cv2.polylines(canvas, [r_pts], False, trace_color, 2, cv2.LINE_AA)
    cv2.putText(
        canvas,
        "II (Ritim Seridi - 10 sn)",
        (grid_left + 12, rhythm_base_y - 78),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.78,
        (15, 25, 110),
        2,
        cv2.LINE_AA,
    )

    png_bytes = encode_image_bytes_to_png_b64(canvas)
    calibration_info = {
        "px_per_mm": px_per_mm,
        "paper_speed_mm_s": 25.0,
        "gain_mm_mv": 10.0,
        "width": width,
        "height": height,
    }
    return png_bytes, {**meta, "calibration": calibration_info}
