"""Klinik EKG kılavuzları (ESC/AHA referans kriterleri), anatomik derivasyon eşleşmeleri ve QTc hesaplayıcısı."""

import json
import math
from functools import lru_cache
from pathlib import Path
from typing import Dict, Any, List, Optional


ERB_TREES_PATH = Path(__file__).resolve().parent / "erb_benchmark_trees.json"


@lru_cache(maxsize=1)
def load_erb_benchmark_trees() -> Dict[str, Any]:
    """Jwoo5/ecg-reasoning-benchmark reposundan çıkarılan 17 temel tanı karar ağacını yükler."""
    if not ERB_TREES_PATH.exists():
        return {"source_repo": "https://github.com/Jwoo5/ecg-reasoning-benchmark", "diagnosis_count": 0, "diagnoses": {}}
    try:
        return json.loads(ERB_TREES_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {"source_repo": "https://github.com/Jwoo5/ecg-reasoning-benchmark", "diagnosis_count": 0, "diagnoses": {}}


ANATOMICAL_TERRITORIES: Dict[str, Dict[str, Any]] = {
    "Inferior": {
        "leads": ["II", "III", "aVF"],
        "artery": "RCA (%80) veya LCx (%20)",
        "reciprocal": ["I", "aVL"],
        "description": "Alt duvar miyokard perfüzyonu; RCA tutulumunda sağ ventrikül (V4R) ve posterior (V7-V9) değerlendirme önerilir.",
    },
    "Septal": {
        "leads": ["V1", "V2"],
        "artery": "Proksimal LAD (Septal perforatörler)",
        "reciprocal": ["Posterior/Inferior (duruma göre)"],
        "description": "İnterventriküler septum bölgesi; sağ dal bloğu veya Brugada paterni açısından da dikkatle incelenir.",
    },
    "Anterior": {
        "leads": ["V3", "V4"],
        "artery": "LAD (Sol Ön İnen Arter)",
        "reciprocal": ["II", "III", "aVF"],
        "description": "Ön duvar bölgesi; V1-V4 birlikte tutulduğunda antero-septal, V1-V6 + I/aVL tutulduğunda yaygın anterior.",
    },
    "Lateral": {
        "leads": ["I", "aVL", "V5", "V6"],
        "artery": "LCx (Sirkumfleks) veya LAD Diyagonal dallar",
        "reciprocal": ["II", "III", "aVF", "V1"],
        "description": "Yüksek lateral (I, aVL) ve apikal-lateral (V5, V6) segmentler.",
    },
    "aVR": {
        "leads": ["aVR"],
        "artery": "Sol Ana Koroner (LMCA), Proksimal LAD veya 3-Damar Hastalığı",
        "reciprocal": ["Yaygın ST depresyonu (I, II, V4-V6)"],
        "description": "aVR'de >= 1 mm ST elevasyonu ile birlikte >= 6 derivasyonda yaygın ST depresyonu kritik LMCA/ağır iskemi uyarısıdır.",
    },
}


CLINICAL_CRITERIA_KB: List[Dict[str, Any]] = [
    {
        "id": "stemi",
        "title": "Akut STEMI Tanı Kriterleri (ESC/AHA 4. Evrensel Tanım)",
        "urgency": "CRITICAL",
        "summary": "Anatomik olarak komşu en az 2 derivasyonda J noktasında yeni gelişen ST elevasyonu.",
        "criteria": [
            "Genel derivasyonlar (I, II, III, aVL, aVF, V1, V4-V6): >= 1 mm (0.1 mV) ST elevasyonu.",
            "V2 ve V3 derivasyonları için cinsiyet/yaş eşikleri: >= 40 yaş erkek >= 2.0 mm; < 40 yaş erkek >= 2.5 mm; tüm kadınlar >= 1.5 mm.",
            "Resiprokal ST depresyonu (ör. İnferior STEMI'de I ve aVL'de depresyon) tanıyı güçlü şekilde destekler.",
            "V7-V9'da >= 0.5 mm elevasyon (veya V1-V3'te derin ST depresyonu + uzun R) posterior MI lehinedir.",
        ],
    },
    {
        "id": "av_blocks",
        "title": "Atriyoventriküler (AV) Blok Dereceleri",
        "urgency": "URGENT",
        "summary": "Atriyal uyarıların ventriküllere iletim gecikmesi veya kesintisi.",
        "criteria": [
            "1. Derece AV Blok: PR aralığı sabit ve > 200 ms (> 5 küçük kare), her P dalgasını QRS takip eder.",
            "2. Derece Mobitz Tip I (Wenckebach): PR aralığı progresif olarak uzar ve sonunda bir P dalgası iletilmez (QRS düşer).",
            "2. Derece Mobitz Tip II: Sabit PR aralığı varken aniden iletilmeyen P dalgaları görülür (yüksek tam blok riski).",
            "3. Derece (Tam) AV Blok: P dalgaları ile QRS kompleksleri tamamen bağımsızdır (AV disosiyasyon); atriyal hız > ventriküler hız.",
        ],
    },
    {
        "id": "bundle_branch_blocks",
        "title": "Dal Blokları (RBBB / LBBB) ve Sgarbossa Kriterleri",
        "urgency": "URGENT",
        "summary": "QRS süresi >= 120 ms (>= 3 küçük kare) ile karakterize intraventriküler iletim gecikmeleri.",
        "criteria": [
            "Sağ Dal Bloğu (RBBB): QRS >= 120 ms; V1-V2'de rSR' ('tavşan kulağı') paterni; I ve V6'da derin/geniş S dalgası.",
            "Sol Dal Bloğu (LBBB): QRS >= 120 ms; I, aVL, V5-V6'da geniş çentikli monofazik R dalgası (Q yok); V1-V3'te derin rS veya QS.",
            "Sgarbossa Kriterleri (LBBB'de Akut MI): (1) Pozitif QRS'li derivasyonda >= 1 mm konkordan ST elevasyonu (5 puan); (2) V1-V3'te >= 1 mm konkordan ST depresyonu (3 puan); (3) Modifiye Smith kuralı: ST/S oranı <= -0.25 olan aşırı diskordan elevasyon.",
        ],
    },
    {
        "id": "afib_aflutter",
        "title": "Atriyal Fibrilasyon (AF) ve Atriyal Flutter",
        "urgency": "URGENT",
        "summary": "En sık görülen sürekli supraventriküler aritmiler.",
        "criteria": [
            "Atriyal Fibrilasyon: Düzensiz-düzensiz (irregularly irregular) R-R aralıkları, belirgin P dalgası yokluğu, düzensiz f (fibrilasyon) dalgaları.",
            "Hızlı Ventrikül Yanıtlı AF (RVR): Ventriküler hız > 100-110/dk.",
            "Atriyal Flutter: Tipik testere dişi (sawtooth) F dalgaları (en iyi II, III, aVF ve V1'de), atriyal hız ~250-350/dk (genellikle 2:1 blokla 150/dk düzenli ritim).",
        ],
    },
    {
        "id": "lvh",
        "title": "Sol Ventrikül Hipertrofisi (LVH) Voltaj Kriterleri",
        "urgency": "ROUTINE",
        "summary": "Artmış sol ventrikül miyokard kütlesine bağlı yüksek QRS voltajı ve sekonder repolarizasyon değişikliği.",
        "criteria": [
            "Sokolow-Lyon Kriteri: S(V1) + R(V5 veya V6) >= 35 mm (3.5 mV) veya R(aVL) >= 11 mm.",
            "Cornell Kriteri: Erkeklerde R(aVL) + S(V3) > 28 mm; kadınlarda > 20 mm.",
            "LVH Strain Paterni: Lateral derivasyonlarda (V5-V6, I, aVL) asimetrik ST depresyonu ve T dalgası inversiyonu.",
        ],
    },
    {
        "id": "wellens_brugada",
        "title": "Yüksek Riskli İskemik ve Kanalopati Paternleri (Wellens & Brugada)",
        "urgency": "CRITICAL",
        "summary": "Ani kardiyak ölüm veya yakın proksimal LAD tıkanıklığı habercisi kritik paternler.",
        "criteria": [
            "Wellens Sendromu (Proksimal LAD kritik darlığı): V2-V3'te ağrısız dönemde bile bifazik (Tip A) veya derin simetrik T negatifliği (Tip B), ST elevasyonu belirgin değildir.",
            "Brugada Tip 1 Paterni: V1-V2'de >= 2 mm kubbeli (coved) ST elevasyonu ve ardından negatif T dalgası (ani aritmik ölüm riski).",
            "De Winter Paterni: V1-V6'da J noktasında yukarı eğimli ST depresyonu + uzun, simetrik hiperakut T dalgaları (LAD tıkanıklığı eşdeğeri).",
        ],
    },
]


def _normalize_sex(sex: Any) -> Optional[str]:
    """Serbest metin cinsiyet bilgisini 'male' / 'female' / None değerine indirger."""
    text = str(sex or "").strip().lower()
    if text in ("erkek", "e", "male", "m"):
        return "male"
    if text in ("kadın", "kadin", "k", "female", "f"):
        return "female"
    return None


def _parse_age(age: Any) -> Optional[float]:
    """Yaş alanını (sayı veya metin) güvenli biçimde sayıya çevirir."""
    try:
        val = float(str(age).strip().replace(",", "."))
    except (TypeError, ValueError):
        return None
    return val if 0 <= val <= 130 else None


def calculate_qtc(qt_ms: float, hr_bpm: float, sex: Any = None, age: Any = None) -> Dict[str, Any]:
    """Bazett ve Fridericia formülleriyle QTc hesaplar; erişkinde cinsiyete özgü eşiklerle sınıflar.

    Erişkin eşikleri (Goldenberg, Moss & Zareba 2006): Erkek sınırda 431-450 ms, uzamış > 450 ms;
    Kadın sınırda 451-470 ms, uzamış > 470 ms. Cinsiyet bilinmiyorsa veya hasta < 16 yaş ise
    cinsiyetten bağımsız 451-470 / > 470 ms bandı kullanılır ve bu durum yorumda belirtilir.
    """
    if not (math.isfinite(qt_ms) and math.isfinite(hr_bpm)) or qt_ms <= 0 or hr_bpm <= 0:
        raise ValueError("QT süresi (ms) ve kalp hızı (bpm) pozitif değerler olmalıdır.")

    rr_sec = 60.0 / hr_bpm
    bazett = qt_ms / math.sqrt(rr_sec)
    fridericia = qt_ms / (rr_sec ** (1.0 / 3.0))

    # Bazett taşikardide fazla, bradikardide eksik düzeltir; 60-100/dk dışında Fridericia esas alınır
    use_bazett = 60 <= hr_bpm <= 100
    ref_qtc = bazett if use_bazett else fridericia
    formula = "Bazett" if use_bazett else "Fridericia (HR 60-100 dışı)"

    sex_norm = _normalize_sex(sex)
    age_val = _parse_age(age)
    is_pediatric = age_val is not None and age_val < 16

    if is_pediatric:
        borderline_gt, prolonged_gt = 450.0, 470.0
        basis = "< 16 yaş: erişkin eşikleri doğrudan uygulanamaz, pediatrik değerlendirme gerekir"
    elif sex_norm == "male":
        borderline_gt, prolonged_gt = 430.0, 450.0
        basis = "Erkek eşiği: sınırda 431-450 ms, uzamış > 450 ms"
    elif sex_norm == "female":
        borderline_gt, prolonged_gt = 450.0, 470.0
        basis = "Kadın eşiği: sınırda 451-470 ms, uzamış > 470 ms"
    else:
        borderline_gt, prolonged_gt = 450.0, 470.0
        basis = "Cinsiyet belirtilmedi: erkekte > 450 ms, kadında > 470 ms uzamış kabul edilir"

    if ref_qtc >= 500:
        status = "KRİTİK UZAMIŞ (>= 500 ms — Torsades de Pointes riski)"
        level = "CRITICAL"
    elif ref_qtc > prolonged_gt:
        status = f"UZAMIŞ ({basis})"
        level = "URGENT"
    elif ref_qtc > borderline_gt:
        status = f"SINIRDA ({basis})"
        level = "BORDERLINE"
    elif ref_qtc < 350:
        status = "KISA QT (< 350 ms)"
        level = "URGENT"
    else:
        status = f"NORMAL ({basis})"
        level = "NORMAL"

    return {
        "qt_ms": round(qt_ms, 1),
        "hr_bpm": round(hr_bpm, 1),
        "rr_sec": round(rr_sec, 3),
        "qtc_bazett_ms": round(bazett, 1),
        "qtc_fridericia_ms": round(fridericia, 1),
        "reference_qtc_ms": round(ref_qtc, 1),
        "recommended_formula": formula,
        "threshold_basis": basis,
        "interpretation": status,
        "level": level,
    }


def format_guidelines_for_prompt() -> str:
    """Klinik kriterleri LLM promptuna enjekte edilmek üzere özet metin haline getirir."""
    lines = ["=== ESC/AHA KLİNİK TANI KRİTERLERİ REFERANS BİLGİ BANKASI ==="]
    for item in CLINICAL_CRITERIA_KB:
        lines.append(f"\n[{item['title']}] (Öncelik: {item['urgency']})")
        for c in item["criteria"]:
            lines.append(f"  - {c}")
    lines.append("\n[Anatomik Duvarlar ve Derivasyon Eşleşmesi]")
    for wall, info in ANATOMICAL_TERRITORIES.items():
        leads_str = ", ".join(info["leads"])
        lines.append(f"  - {wall}: {leads_str} -> {info['artery']}")

    erb_data = load_erb_benchmark_trees()
    diagnoses = erb_data.get("diagnoses", {})
    if diagnoses:
        lines.append("\n=== Jwoo5/ECG-Reasoning-Benchmark 17 TANI KARAR VE GÖRSEL DOĞRULAMA (GROUNDING) ZİNCİRLERİ ===")
        for dx_key, dx_info in diagnoses.items():
            criteria_chain = " -> ".join(
                f"{s['criterion']} ({', '.join(g['question_type'] for g in s.get('grounding_steps', [])) or 'kriter kontrolü'})"
                for s in dx_info.get("steps", [])
            )
            lines.append(f"  - {dx_key} ({dx_info.get('display_name', dx_key)}): {criteria_chain}")
    return "\n".join(lines)
