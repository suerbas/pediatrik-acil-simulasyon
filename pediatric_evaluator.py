# -*- coding: utf-8 -*-
"""
Pediatrik Klinik Değer Değerlendirici ve Mouse-Over (Tooltip) Motoru
APLS (Advanced Paediatric Life Support) ve PALS (Pediatric Advanced Life Support)
referanslarına göre yaşa duyarlı vital ve laboratuvar parametrelerini değerlendirir.
"""

import re


def parse_age_in_months(age_str: str) -> float:
    """Yaş dizesini ay (month) cinsine dönüştürür."""
    if not age_str:
        return 24.0  # Varsayılan 2 yaş
    
    age_str = age_str.lower().strip()
    
    # Günlük kontrolü
    gun_match = re.search(r'(\d+)\s*(?:gün|gun)', age_str)
    if gun_match:
        return float(gun_match.group(1)) / 30.0
    
    # Haftalık kontrolü
    hf_match = re.search(r'(\d+)\s*(?:hafta)', age_str)
    if hf_match:
        return float(hf_match.group(1)) * 0.23
        
    # Aylık kontrolü
    ay_match = re.search(r'(\d+)\s*(?:ay|aylık|aylik)', age_str)
    if ay_match:
        return float(ay_match.group(1))
        
    # Yaş kontrolü (örn. "3 yaş", "2.5 yaşında")
    yas_match = re.search(r'(\d+(?:[.,]\d+)?)\s*(?:yaş|yas)', age_str)
    if yas_match:
        num = float(yas_match.group(1).replace(',', '.'))
        return num * 12.0
        
    # Sayı varsa doğrudan al
    digits = re.search(r'(\d+)', age_str)
    if digits:
        return float(digits.group(1)) * 12.0
        
    return 24.0


def eval_kta(val: float, age_m: float) -> dict:
    """Kalp Tepe Atımı (/dk) değerlendirmesi."""
    if age_m < 1:  # Yenidoğan
        ref = "100 - 160 /dk"
        low_t, high_t = 100, 160
    elif age_m < 12:  # Süt çocuğu (1-12 ay)
        ref = "100 - 150 /dk"
        low_t, high_t = 100, 150
    elif age_m < 36:  # 1-3 yaş
        ref = "90 - 130 /dk"
        low_t, high_t = 90, 130
    elif age_m < 72:  # 3-5 yaş
        ref = "80 - 120 /dk"
        low_t, high_t = 80, 120
    elif age_m < 144:  # 6-12 yaş
        ref = "70 - 110 /dk"
        low_t, high_t = 70, 110
    else:  # >12 yaş
        ref = "60 - 100 /dk"
        low_t, high_t = 60, 100
        
    if val < low_t:
        return {"status": "low", "icon": "🔵", "label": "Düşük (Bradikardi)", "ref": ref}
    elif val > high_t:
        if (age_m < 12 and val >= 220) or (age_m >= 12 and val >= 180):
            return {"status": "high", "icon": "🚨", "label": "Kritik Taşikardi (SVT?)", "ref": ref}
        return {"status": "high", "icon": "🔴", "label": "Yüksek (Taşikardi)", "ref": ref}
    return {"status": "normal", "icon": "🟢", "label": "Normal KTA", "ref": ref}


def eval_ss(val: float, age_m: float) -> dict:
    """Solunum Sayısı (/dk) değerlendirmesi."""
    if age_m < 1:
        ref = "30 - 60 /dk"
        low_t, high_t = 30, 60
    elif age_m < 12:
        ref = "25 - 45 /dk"
        low_t, high_t = 25, 45
    elif age_m < 36:
        ref = "20 - 30 /dk"
        low_t, high_t = 20, 30
    elif age_m < 72:
        ref = "20 - 25 /dk"
        low_t, high_t = 18, 25
    elif age_m < 144:
        ref = "14 - 22 /dk"
        low_t, high_t = 12, 22
    else:
        ref = "12 - 18 /dk"
        low_t, high_t = 10, 18
        
    if val < low_t:
        return {"status": "low", "icon": "🔵", "label": "Düşük (Bradipne)", "ref": ref}
    elif val > high_t:
        return {"status": "high", "icon": "🔴", "label": "Yüksek (Takipne)", "ref": ref}
    return {"status": "normal", "icon": "🟢", "label": "Normal Solunum", "ref": ref}


def eval_ates(val: float, age_m: float = 999) -> dict:
    """Ateş (°C) değerlendirmesi, yaşa göre (koltuk altı ölçümü esas alınır).

    3 aydan küçük bebeklerde normal aralık dardır (36.5-37.4 °C): 36.0-36.4 °C hafif
    hipotermi (DSÖ), 37.5-37.9 °C subfebril, >= 38.0 °C ise sepsis açısından ateştir.
    """
    young = age_m < 3
    ref = "36.5 - 37.4 °C (3 ay altı)" if young else "36.0 - 37.4 °C"
    if val < 36.0:
        return {"status": "low", "icon": "🔵", "label": "Düşük (Hipotermi)", "ref": ref}
    if val < 36.5 and young:
        return {"status": "low", "icon": "🔵", "label": "Hafif Hipotermi", "ref": ref}
    if val < 37.5:
        return {"status": "normal", "icon": "🟢", "label": "Normal Sıcaklık", "ref": ref}
    if val < 38.0:
        label = "Subfebril (Yakın Takip)" if young else "Hafif Yüksek (Subfebril)"
        return {"status": "high", "icon": "🟡", "label": label, "ref": ref}
    if young:
        return {"status": "high", "icon": "🔴", "label": "Ateş (Sepsis Açısından Değerlendir)", "ref": ref}
    if val < 39.0:
        return {"status": "high", "icon": "🔴", "label": "Yüksek (Ateş)", "ref": ref}
    return {"status": "high", "icon": "🔥", "label": "Belirgin Yüksek Ateş", "ref": ref}


def eval_spo2(val: float) -> dict:
    """SpO2 (%) değerlendirmesi."""
    ref = "≥ %95 (Oda Havasında)"
    if val >= 95:
        return {"status": "normal", "icon": "🟢", "label": "Normal Oksijenasyon", "ref": ref}
    elif 92 <= val < 95:
        return {"status": "low", "icon": "🟡", "label": "Sınırda / Hafif Hipoksemi", "ref": ref}
    elif 90 <= val < 92:
        return {"status": "low", "icon": "🔵", "label": "Düşük (Hipoksemi)", "ref": ref}
    else:
        return {"status": "low", "icon": "🚨", "label": "Kritik Düşük (Ciddi Hipoksi)", "ref": ref}


def eval_ta(sys: float, dia: float, age_m: float) -> dict:
    """Kan Basıncı / TA (mmHg) değerlendirmesi."""
    age_y = age_m / 12.0
    if age_m < 1:
        hypo = 60
        ref = "Sistolik > 60 mmHg"
    elif age_m < 12:
        hypo = 70
        ref = "Sistolik > 70 mmHg"
    elif age_y <= 10:
        hypo = 70 + (2 * age_y)
        ref = f"Sistolik > {int(hypo)} mmHg"
    else:
        hypo = 90
        ref = "Sistolik > 90 mmHg"
        
    if sys < hypo:
        return {"status": "low", "icon": "🚨", "label": "Düşük (Hipotansiyon / Şok!)", "ref": ref}
    elif sys > 135 or dia > 88:
        return {"status": "high", "icon": "🔴", "label": "Yüksek (Hipertansiyon)", "ref": ref}
    return {"status": "normal", "icon": "🟢", "label": "Normal Tansiyon", "ref": ref}


def eval_kdz(val: float) -> dict:
    """Kılcal Dolum Zamanı (saniye)."""
    ref = "≤ 2 saniye"
    if val <= 2.0:
        return {"status": "normal", "icon": "🟢", "label": "Normal Doku Perfüzyonu", "ref": ref}
    return {"status": "high", "icon": "🔴", "label": "Uzamış (Bozulmuş Perfüzyon)", "ref": ref}


def eval_ph(val: float) -> dict:
    """Kan Gazı pH değerlendirmesi."""
    ref = "7.35 - 7.45"
    if val < 7.35:
        return {"status": "low", "icon": "🔵", "label": "Düşük (Asidemi / Asidoz)", "ref": ref}
    elif val > 7.45:
        return {"status": "high", "icon": "🔴", "label": "Yüksek (Alkalemi / Alkaloz)", "ref": ref}
    return {"status": "normal", "icon": "🟢", "label": "Normal pH", "ref": ref}


def eval_pco2(val: float) -> dict:
    """Kan Gazı pCO2 (mmHg)."""
    ref = "35 - 45 mmHg"
    if val < 35:
        return {"status": "low", "icon": "🔵", "label": "Düşük (Hipokapni)", "ref": ref}
    elif val > 45:
        return {"status": "high", "icon": "🔴", "label": "Yüksek (Hiperkapni / Asidoz)", "ref": ref}
    return {"status": "normal", "icon": "🟢", "label": "Normal pCO2", "ref": ref}


def eval_hco3(val: float) -> dict:
    """Kan Gazı HCO3 (mmol/L)."""
    ref = "22 - 26 mmol/L"
    if val < 22:
        return {"status": "low", "icon": "🔵", "label": "Düşük (Metabolik Asidoz)", "ref": ref}
    elif val > 26:
        return {"status": "high", "icon": "🔴", "label": "Yüksek (Metabolik Alkaloz)", "ref": ref}
    return {"status": "normal", "icon": "🟢", "label": "Normal Bikarbonat", "ref": ref}


def eval_laktat(val: float) -> dict:
    """Laktat (mmol/L)."""
    ref = "0.5 - 2.0 mmol/L"
    if val <= 2.0:
        return {"status": "normal", "icon": "🟢", "label": "Normal Laktat", "ref": ref}
    elif val <= 4.0:
        return {"status": "high", "icon": "🔴", "label": "Yüksek (Doku Hipoksisi)", "ref": ref}
    return {"status": "high", "icon": "🚨", "label": "Kritik Yüksek (Şok Bulgusu)", "ref": ref}


def eval_be(val: float) -> dict:
    """Baz Açığı (mmol/L)."""
    ref = "-3 ila +3 mmol/L"
    if val < -3.0:
        return {"status": "low", "icon": "🔵", "label": "Belirgin Baz Açığı (Asidoz)", "ref": ref}
    elif val > 3.0:
        return {"status": "high", "icon": "🔴", "label": "Pozitif Baz Fazlalığı", "ref": ref}
    return {"status": "normal", "icon": "🟢", "label": "Normal Baz Durumu", "ref": ref}


def eval_crp(val: float) -> dict:
    """CRP (mg/L)."""
    ref = "< 5.0 mg/L"
    if val <= 5.0:
        return {"status": "normal", "icon": "🟢", "label": "Normal (Negatif)", "ref": ref}
    elif val <= 20.0:
        return {"status": "high", "icon": "🟡", "label": "Hafif Yüksek", "ref": ref}
    elif val <= 50.0:
        return {"status": "high", "icon": "🔴", "label": "Yüksek (Akut Faz Yanıtı)", "ref": ref}
    return {"status": "high", "icon": "🔥", "label": "Belirgin Yüksek (Ciddi Enfeksiyon)", "ref": ref}


def eval_procalcitonin(val: float) -> dict:
    """Prokalsitonin (ng/mL)."""
    ref = "< 0.5 ng/mL"
    if val < 0.5:
        return {"status": "normal", "icon": "🟢", "label": "Normal (Düşük Bakteriyel Risk)", "ref": ref}
    elif val < 2.0:
        return {"status": "high", "icon": "🟡", "label": "Yüksek (Bakteriyel Enfeksiyon Olası)", "ref": ref}
    return {"status": "high", "icon": "🚨", "label": "Kritik Yüksek (İnvaziv Bakteriyel / Sepsis)", "ref": ref}


def eval_wbc(val: float, age_m: float) -> dict:
    """Lökosit / WBC (/mm³)."""
    if age_m < 12:
        ref = "6.000 - 17.500 /mm³"
        low_t, high_t = 5000, 17500
    else:
        ref = "5.000 - 14.500 /mm³"
        low_t, high_t = 4500, 14500
        
    if val < low_t:
        return {"status": "low", "icon": "🔵", "label": "Düşük (Lökopeni)", "ref": ref}
    elif val > high_t:
        return {"status": "high", "icon": "🔴", "label": "Yüksek (Lökositoz)", "ref": ref}
    return {"status": "normal", "icon": "🟢", "label": "Normal Lökosit", "ref": ref}


def eval_hb(val: float, age_m: float) -> dict:
    """Hemoglobin (g/dL)."""
    ref = "≥ 11.0 g/dL" if age_m >= 6 else "≥ 10.0 g/dL"
    threshold = 11.0 if age_m >= 6 else 10.0
    if val < threshold:
        return {"status": "low", "icon": "🔵", "label": "Düşük (Anemi)", "ref": ref}
    return {"status": "normal", "icon": "🟢", "label": "Normal Hemoglobin", "ref": ref}


def eval_plt(val: float) -> dict:
    """Trombosit / PLT (/mm³)."""
    ref = "150.000 - 450.000 /mm³"
    if val < 150000:
        return {"status": "low", "icon": "🔵", "label": "Düşük (Trombositopeni)", "ref": ref}
    elif val > 450000:
        return {"status": "high", "icon": "🔴", "label": "Yüksek (Trombositoz)", "ref": ref}
    return {"status": "normal", "icon": "🟢", "label": "Normal Trombosit", "ref": ref}


def eval_glukoz(val: float) -> dict:
    """Kan Şekeri (mg/dL)."""
    ref = "70 - 140 mg/dL"
    if val < 60:
        return {"status": "low", "icon": "🚨", "label": "Düşük (Hipoglisemi!)", "ref": ref}
    elif val <= 140:
        return {"status": "normal", "icon": "🟢", "label": "Normal Glukoz", "ref": ref}
    elif val <= 200:
        return {"status": "high", "icon": "🟡", "label": "Hafif Hiperglisemi", "ref": ref}
    return {"status": "high", "icon": "🚨", "label": "Belirgin Yüksek (DKA Şüphesi)", "ref": ref}


def eval_na(val: float) -> dict:
    """Sodyum / Na (mEq/L)."""
    ref = "135 - 145 mEq/L"
    if val < 135:
        return {"status": "low", "icon": "🔵", "label": "Düşük (Hiponatremi)", "ref": ref}
    elif val > 145:
        return {"status": "high", "icon": "🔴", "label": "Yüksek (Hipernatremi)", "ref": ref}
    return {"status": "normal", "icon": "🟢", "label": "Normal Sodyum", "ref": ref}


def eval_k(val: float) -> dict:
    """Potasyum / K (mEq/L)."""
    ref = "3.5 - 5.2 mEq/L"
    if val < 3.5:
        return {"status": "low", "icon": "🔵", "label": "Düşük (Hipokalemi)", "ref": ref}
    elif val > 5.2:
        return {"status": "high", "icon": "🔴", "label": "Yüksek (Hiperkalemi)", "ref": ref}
    return {"status": "normal", "icon": "🟢", "label": "Normal Potasyum", "ref": ref}


def eval_kreatinin(val: float, age_m: float) -> dict:
    """Kreatinin (mg/dL) değerlendirmesi."""
    ref = "0.2 - 0.6 mg/dL" if age_m < 36 else "0.3 - 0.8 mg/dL"
    threshold = 0.6 if age_m < 36 else 0.8
    if val <= threshold:
        return {"status": "normal", "icon": "🟢", "label": "Normal Kreatinin", "ref": ref}
    return {"status": "high", "icon": "🔴", "label": "Yüksek (Böbrek Fonksiyon Bozukluğu?)", "ref": ref}


def build_tooltip_html(matched_text: str, res: dict) -> str:
    """Klinik değer için şık HTML rozeti ve hover tooltip çıktısı üretir."""
    status = res.get("status", "normal")
    icon = res.get("icon", "🟢")
    label = res.get("label", "Normal")
    ref = res.get("ref", "")
    
    # HTML tooltip yapısı (saf CSS tabanlı tek satır hover baloncuğu, native title yok)
    return (
        f'<span class="med-val med-val-{status}">'
        f'{matched_text}'
        f'<span class="med-tooltip">'
        f'<b style="color:#ffffff;">{icon} {label}</b> &nbsp;|&nbsp; <span style="color:#cbd5e1;">Normal: {ref}</span>'
        f'</span>'
        f'</span>'
    )


def annotate_clinical_text(text: str, age_str: str) -> str:
    """
    Verilen metin içerisindeki vital bulguları ve laboratuvar sonuçlarını tespit eder,
    yaşa göre değerlendirip hover-tooltip rozetlerine dönüştürür.
    """
    if not text or not isinstance(text, str):
        return text
    
    # Zaten dönüştürülmüş metni tekrar dönüştürme (idempotence)
    if 'class="med-val' in text:
        return text
        
    age_m = parse_age_in_months(age_str)
    
    # Sırayla tespit edip değiştireceğimiz kurallar (Regex -> Değerlendirici fonksiyon)
    
    # 1. Ateş: "Ateş 38.5°C", "ateşi 39.1 °C", "38.2°C", "39°C"
    def repl_ates(m):
        raw = m.group(0)
        val = float(m.group(1).replace(',', '.'))
        res = eval_ates(val, age_m)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:(?:Ateş|ateş|Ateşi|ateşi)\s*[:]?\s*)?(\d{2}(?:[.,]\d+)?)\s*°?\s*C\b', repl_ates, text)
    
    # 2. KTA / Nabız: "KTA 130/dk", "KTA: 165/dk", "Nabız 140/dk", "nabzı 110/dk"
    def repl_kta(m):
        raw = m.group(0)
        val = float(m.group(1))
        res = eval_kta(val, age_m)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:KTA|Nabız|nabız|Kta|Nabzı|nabzı|kta)\s*[:]?\s*(\d{2,3})\s*(?:/dk|/dakika|bpm)?\b', repl_kta, text)
    
    # 3. Solunum Sayısı: "SS 45/dk", "SS: 28/dk", "Solunum Sayısı 64/dk", "solunum sayısı 50/dk", "Solunum hızı 40/dk"
    def repl_ss(m):
        raw = m.group(0)
        val = float(m.group(1))
        res = eval_ss(val, age_m)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:SS|Solunum\s+[Ss]ay[ıi]s[ıi]|solunum\s+[Ss]ay[ıi]s[ıi]|Solunum\s+[Hh][ıi]z[ıi]|solunum\s+[Hh][ıi]z[ıi]|Solunumu|solunumu|Solunum|solunum)\s*[:]?\s*(\d{1,2})\s*(?:/dk|/dakika)?\b', repl_ss, text)
    
    # 4. SpO2: "SpO2 %91", "SpO2: %98", "SpO2 94%"
    def repl_spo2(m):
        raw = m.group(0)
        val = float(m.group(1))
        res = eval_spo2(val)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:SpO2|spo2|SPO2)\s*[:]?\s*[%]?\s*(\d{2})\s*%?\b', repl_spo2, text)
    
    # 5. Tansiyon / TA: "TA 80/50 mmHg", "TA: 90/60", "Tansiyon 70/40 mmHg"
    def repl_ta(m):
        raw = m.group(0)
        sys_val = float(m.group(1))
        dia_val = float(m.group(2))
        res = eval_ta(sys_val, dia_val, age_m)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:TA|Tansiyon|tansiyon)\s*[:]?\s*(\d{2,3})\s*/\s*(\d{2,3})\s*(?:mmHg)?\b', repl_ta, text)
    
    # 6. Kılcal Dolum Zamanı: "KDZ 3 sn", "Kılcal dolum zamanı 4 sn"
    def repl_kdz(m):
        raw = m.group(0)
        val = float(m.group(1).replace(',', '.'))
        res = eval_kdz(val)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:KDZ|kdz|Kılcal dolum zamanı|kılcal dolum zamanı)\s*[:]?\s*(\d+(?:[.,]\d+)?)\s*s(?:n|aniye)?\b', repl_kdz, text)
    
    # 7. Kan Gazı pH: "pH 7.18", "pH: 7.42"
    def repl_ph(m):
        raw = m.group(0)
        val = float(m.group(1).replace(',', '.'))
        res = eval_ph(val)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\bpH\s*[:]?\s*(\d[.,]\d{2})\b', repl_ph, text)
    
    # 8. Kan Gazı pCO2: "pCO2 55 mmHg", "pCO2: 28"
    def repl_pco2(m):
        raw = m.group(0)
        val = float(m.group(1).replace(',', '.'))
        res = eval_pco2(val)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\bpCO2\s*[:]?\s*(\d{2}(?:[.,]\d+)?)\s*(?:mmHg)?\b', repl_pco2, text)
    
    # 9. Kan Gazı HCO3: "HCO3 12 mmol/L", "HCO3: 24"
    def repl_hco3(m):
        raw = m.group(0)
        val = float(m.group(1).replace(',', '.'))
        res = eval_hco3(val)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\bHCO3\s*[:]?\s*(\d{1,2}(?:[.,]\d+)?)\s*(?:mmol/L|mEq/L)?\b', repl_hco3, text)
    
    # 10. Laktat: "Laktat 3.8 mmol/L", "laktat: 1.2"
    def repl_laktat(m):
        raw = m.group(0)
        val = float(m.group(1).replace(',', '.'))
        res = eval_laktat(val)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:Laktat|laktat)\s*[:]?\s*(\d+(?:[.,]\d+)?)\s*(?:mmol/L)?\b', repl_laktat, text)
    
    # 11. Baz Açığı / BE: "BE -12", "Baz açığı -8"
    def repl_be(m):
        raw = m.group(0)
        val = float(m.group(1).replace(',', '.'))
        res = eval_be(val)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:BE|Baz açığı|baz açığı)\s*[:]?\s*([+-]?\d+(?:[.,]\d+)?)\b', repl_be, text)
    
    # 12. CRP: "CRP 42 mg/L", "CRP: 4.2 mg/L"
    def repl_crp(m):
        raw = m.group(0)
        val = float(m.group(1).replace(',', '.'))
        res = eval_crp(val)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\bCRP\s*[:]?\s*(\d+(?:[.,]\d+)?)\s*(?:mg/L|mg/dL)?\b', repl_crp, text)
    
    # 13. Prokalsitonin: "Prokalsitonin 2.5 ng/mL", "prokalsitonin 0.04"
    def repl_pct(m):
        raw = m.group(0)
        val = float(m.group(1).replace(',', '.'))
        res = eval_procalcitonin(val)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:Prokalsitonin|prokalsitonin)\s*[:]?\s*(\d+(?:[.,]\d+)?)\s*(?:ng/mL)?\b', repl_pct, text)
    
    # 14. Lökosit / WBC: "WBC 18.500/mm³", "Lökosit: 4.200"
    def repl_wbc(m):
        raw = m.group(0)
        clean_num = m.group(1).replace('.', '').replace(',', '')
        val = float(clean_num)
        res = eval_wbc(val, age_m)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:WBC|Lökosit|lökosit)\s*[:]?\s*(\d{1,2}[.,]?\d{3})\s*(?:/mm³|/uL|/µL)?\b', repl_wbc, text)
    
    # 15. Hemoglobin / Hb: "Hb 7.8 g/dL", "Hemoglobin 12.2 g/dL"
    def repl_hb(m):
        raw = m.group(0)
        val = float(m.group(1).replace(',', '.'))
        res = eval_hb(val, age_m)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:Hb|Hemoglobin|hemoglobin)\s*[:]?\s*(\d{1,2}(?:[.,]\d+)?)\s*(?:g/dL)?\b', repl_hb, text)
    
    # 16. Trombosit / PLT: "PLT 290.000/mm³", "Trombosit: 85.000"
    def repl_plt(m):
        raw = m.group(0)
        clean_num = m.group(1).replace('.', '').replace(',', '')
        val = float(clean_num)
        res = eval_plt(val)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:PLT|Plt|Trombosit|trombosit)\s*[:]?\s*(\d{2,3}[.,]?\d{3})\s*(?:/mm³|/uL|/µL)?\b', repl_plt, text)
    
    # 17. Kan Şekeri / Glukoz: "Kan şekeri 45 mg/dL", "Glukoz 240 mg/dL", "KŞ 110 mg/dL"
    def repl_glukoz(m):
        raw = m.group(0)
        val = float(m.group(1))
        res = eval_glukoz(val)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:Kan şekeri|kan şekeri|Glukoz|glukoz|KŞ|kş)\s*[:]?\s*(\d{2,3})\s*(?:mg/dL)?\b', repl_glukoz, text)
    
    # 18. Sodyum / Na: "Na 128 mEq/L", "Sodyum: 138"
    def repl_na(m):
        raw = m.group(0)
        val = float(m.group(1).replace(',', '.'))
        res = eval_na(val)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:Sodyum|sodyum|Na)\s*[:]?\s*(\d{3}(?:[.,]\d+)?)\s*(?:mEq/L|mmol/L)?\b', repl_na, text)
    
    # 19. Potasyum / K: "K 3.1 mEq/L", "Potasyum: 5.8"
    def repl_k(m):
        raw = m.group(0)
        val = float(m.group(1).replace(',', '.'))
        res = eval_k(val)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:Potasyum|potasyum|K)\s*[:]?\s*(\d[.,]\d+)\s*(?:mEq/L|mmol/L)?\b', repl_k, text)
    
    # 20. Kreatinin: "Kreatinin 1.2 mg/dL", "kreatinin: 0.4"
    def repl_kreatinin(m):
        raw = m.group(0)
        val = float(m.group(1).replace(',', '.'))
        res = eval_kreatinin(val, age_m)
        return build_tooltip_html(raw, res)
    text = re.sub(r'\b(?:Kreatinin|kreatinin)\s*[:]?\s*(\d+(?:[.,]\d+)?)\s*(?:mg/dL)?\b', repl_kreatinin, text)
    
    return text


def get_case_vitals(case: dict) -> str:
    """
    Vakaya ait geliş/triyaj vital bulgularını çıkarır.
    Önceden tanımlı vitaller, anamnez veya 1. aşama bulgularından otomatik derler.
    """
    if case.get('vitals'):
        return case['vitals']
        
    pattern = r'(?:Vital Bulgular|Vitalleri|vital bulgular)[:]?\s*([^\n]+?)(?=\.\s+[A-ZĞÜŞİÖÇ]|\.\s*$|\n|$)'
    
    # 1. Anamnez içinde ara
    hist = case.get('history', '')
    m = re.search(pattern, hist, re.IGNORECASE)
    if m:
        return m.group(0).strip()
        
    # 2. 1. Adımın seçenek bulgularında ara
    if case.get('steps') and len(case['steps']) > 0:
        for opt in case['steps'][0].get('options', []):
            finding = opt.get('new_finding', '')
            m = re.search(pattern, finding, re.IGNORECASE)
            if m:
                return m.group(0).strip()
            parts = re.findall(r'(?:Ateş\s*[:]?\s*[\d.,]+°?C|KTA\s*[:]?\s*[\d/]+(?:dk)?|SS\s*[:]?\s*[\d/]+(?:dk)?|SpO2\s*[:]?\s*[%]?[\d]+%?|TA\s*[:]?\s*[\d/]+(?:mmHg)?|KDZ\s*[:]?\s*[\d.,]+s?n?)', finding)
            if len(parts) >= 2:
                return 'Vital Bulgular: ' + ', '.join(parts)
                
        for opt in case['steps'][0].get('options', []):
            for text in [opt.get('scenario_update', ''), opt.get('text', '')]:
                parts = re.findall(r'(?:Ateş\s*[:]?\s*[\d.,]+°?C|KTA\s*[:]?\s*[\d/]+(?:dk)?|SS\s*[:]?\s*[\d/]+(?:dk)?|SpO2\s*[:]?\s*[%]?[\d]+%?|TA\s*[:]?\s*[\d/]+(?:mmHg)?)', text)
                if len(parts) >= 2:
                    return 'Vital Bulgular: ' + ', '.join(parts)
                    
    # 3. Eğer hiçbiri yoksa (stabil göz/KBB vakaları) yaşa uygun stabil normal vitaller
    age_m = parse_age_in_months(case.get('age', ''))
    if age_m < 1:
        return 'Vital Bulgular: Ateş 36.8°C, KTA 136/dk, SS 38/dk, SpO2 %99'
    elif age_m < 12:
        return 'Vital Bulgular: Ateş 36.7°C, KTA 124/dk, SS 30/dk, SpO2 %99'
    elif age_m < 36:
        return 'Vital Bulgular: Ateş 36.6°C, KTA 110/dk, SS 24/dk, SpO2 %99'
    elif age_m < 72:
        return 'Vital Bulgular: Ateş 36.6°C, KTA 98/dk, SS 20/dk, SpO2 %99'
    elif age_m < 144:
        return 'Vital Bulgular: Ateş 36.6°C, KTA 86/dk, SS 18/dk, SpO2 %99'
    else:
        return 'Vital Bulgular: Ateş 36.6°C, KTA 74/dk, SS 16/dk, SpO2 %99'

