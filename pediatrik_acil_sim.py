# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyon Uygulaması (Yeşil Alan & Sarı Alan)
Modern Klinik Çalışma İstasyonu (EMR Cockpit & Digital Telemetry) Mimarisi.
"""

import os
import random
import time
import importlib
import streamlit as st
from cases_green import GREEN_CASES
from cases_yellow import YELLOW_CASES

import pediatric_evaluator
try:
    importlib.reload(pediatric_evaluator)
except Exception:
    pass

try:
    from pediatric_evaluator import annotate_clinical_text, get_case_vitals
except ImportError:
    import re
    from pediatric_evaluator import annotate_clinical_text, parse_age_in_months

    def get_case_vitals(case: dict) -> str:
        if case.get('vitals'):
            return case['vitals']
        pattern = r'(?:Vital Bulgular|Vitalleri|vital bulgular)[:]?\s*([^\n]+?)(?=\.\s+[A-ZĞÜŞİÖÇ]|\.\s*$|\n|$)'
        hist = case.get('history', '')
        m = re.search(pattern, hist, re.IGNORECASE)
        if m:
            return m.group(0).strip()
        if case.get('steps') and len(case['steps']) > 0:
            for opt in case['steps'][0].get('options', []):
                finding = opt.get('new_finding', '')
                m = re.search(pattern, finding, re.IGNORECASE)
                if m:
                    return m.group(0).strip()
                parts = re.findall(r'(?:Ateş\s*[:]?\s*[\d.,]+°?C|KTA\s*[:]?\s*[\d/]+(?:dk)?|SS\s*[:]?\s*[\d/]+(?:dk)?|SpO2\s*[:]?\s*[%]?[\d]+%?|TA\s*[:]?\s*[\d/]+(?:mmHg)?|KDZ\s*[:]?\s*[\d.,]+s?n?)', finding)
                if len(parts) >= 2:
                    return 'Vital Bulgular: ' + ', '.join(parts)
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

st.set_page_config(
    page_title="Pediatrik Acil Klinik Kokpiti",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom Styling: Modern Hospital Workstation Aesthetic (Clinical Cockpit)
st.markdown(
    """
    <style>
    /* Google Font Inter */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        color: #0f172a;
    }

    /* Ana Başlık ve Alt Başlık */
    .hero-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #0f172a;
        letter-spacing: -0.025em;
        margin-bottom: 0.25rem;
    }
    .hero-subtitle {
        text-align: center;
        font-size: 1.05rem;
        color: #64748b;
        margin-bottom: 1.8rem;
        font-weight: 400;
    }

    /* Ana Sayfa Alan Kartları */
    .portal-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 30px 24px;
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.05);
        transition: all 0.25s ease;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 320px;
        position: relative;
        overflow: hidden;
    }
    .portal-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 30px -4px rgba(0, 0, 0, 0.1);
    }
    .portal-card-green {
        border-top: 6px solid #10b981;
    }
    .portal-card-yellow {
        border-top: 6px solid #f59e0b;
    }
    .portal-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        padding: 4px 10px;
        border-radius: 20px;
        width: fit-content;
        margin-bottom: 14px;
    }
    .badge-green {
        background: #ecfdf5;
        color: #065f46;
        border: 1px solid #a7f3d0;
    }
    .badge-yellow {
        background: #fffbeb;
        color: #92400e;
        border: 1px solid #fde68a;
    }
    .portal-title {
        font-size: 1.5rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 8px;
    }
    .portal-desc {
        color: #475569;
        font-size: 0.95rem;
        line-height: 1.55;
        margin-bottom: 20px;
    }

    /* Üst Klinik Navigasyon Çubuğu */
    .clinical-topbar {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 10px 18px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
    }

    /* İnteraktif Klinik İlerleme Çubuğu (Stepper) */
    .stepper-wrapper {
        display: flex;
        align-items: center;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 10px 18px;
        margin-bottom: 16px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
    }
    .step-node {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 0.82rem;
        font-weight: 600;
        color: #94a3b8;
    }
    .step-node.active {
        color: #0f172a;
        font-weight: 700;
    }
    .step-node.completed {
        color: #059669;
    }
    .step-pill {
        width: 24px;
        height: 24px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75rem;
        font-weight: 700;
        background: #f1f5f9;
        color: #64748b;
        border: 1px solid #cbd5e1;
    }
    .step-node.active .step-pill {
        background: #0284c7;
        color: #ffffff;
        border-color: #0284c7;
        box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.2);
    }
    .step-node.completed .step-pill {
        background: #059669;
        color: #ffffff;
        border-color: #059669;
    }
    .step-divider {
        flex: 1;
        height: 2px;
        background: #e2e8f0;
        margin: 0 8px;
    }
    .step-divider.completed {
        background: #059669;
    }

    /* Sol Kolon: Hasta Dosyası & Klinik İzlem Kartı */
    .emr-panel {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 4px 16px -2px rgba(0, 0, 0, 0.04);
        margin-bottom: 16px;
    }
    .emr-panel-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #f1f5f9;
        padding-bottom: 10px;
        margin-bottom: 12px;
    }
    .emr-title {
        font-size: 0.88rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #475569;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Dijital Hasta Telemetri & Vital Monitörü */
    .telemetry-card {
        background: #090d16;
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 14px 16px;
        margin-bottom: 14px;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.6), 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    .telemetry-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #1e293b;
        padding-bottom: 6px;
        margin-bottom: 8px;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        color: #38bdf8;
        text-transform: uppercase;
    }
    .telemetry-pulse {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #22c55e;
        box-shadow: 0 0 8px #22c55e;
        margin-right: 6px;
        animation: pulse 1.8s infinite;
    }
    @keyframes pulse {
        0% { opacity: 0.4; }
        50% { opacity: 1; }
        100% { opacity: 0.4; }
    }
    .telemetry-content {
        font-size: 0.95rem;
        line-height: 1.6;
        color: #f8fafc;
    }

    /* Hasta Kimlik Etiketleri */
    .patient-demographics {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-bottom: 12px;
    }
    .demo-tag {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 4px 10px;
        font-size: 0.85rem;
        font-weight: 600;
        color: #1e293b;
    }
    .demo-tag-accent {
        background: #f0fdf4;
        border-color: #86efac;
        color: #166534;
    }
    .demo-tag-yellow {
        background: #fefce8;
        border-color: #fde047;
        color: #854d0e;
    }

    /* Anamnez Kartı */
    .anamnesis-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 12px 14px;
        font-size: 0.92rem;
        line-height: 1.55;
        color: #334155;
        margin-bottom: 14px;
    }

    /* Klinik Seyir & Dosya Notları Zaman Tüneli (Scrollable Timeline) */
    .timeline-container {
        max-height: 340px;
        overflow-y: auto;
        padding-right: 6px;
        margin-top: 6px;
    }
    .timeline-container::-webkit-scrollbar {
        width: 5px;
    }
    .timeline-container::-webkit-scrollbar-thumb {
        background: #cbd5e1;
        border-radius: 10px;
    }
    .timeline-node {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #0284c7;
        border-radius: 10px;
        padding: 10px 14px;
        margin-bottom: 10px;
        font-size: 0.9rem;
        line-height: 1.5;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
    }
    .timeline-node-title {
        font-weight: 700;
        color: #0f172a;
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 4px;
    }

    /* Sağ Kolon: Klinik Karar Masası */
    .decision-panel {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 22px;
        box-shadow: 0 4px 16px -2px rgba(0, 0, 0, 0.04);
        margin-bottom: 16px;
    }
    .stage-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #0369a1;
        background: #e0f2fe;
        border: 1px solid #bae6fd;
        padding: 4px 10px;
        border-radius: 20px;
        margin-bottom: 10px;
    }
    .question-headline {
        font-size: 1.22rem;
        font-weight: 700;
        color: #0f172a;
        line-height: 1.45;
        margin-bottom: 18px;
    }

    /* Yanlış Seçim Detour / Senaryo Güncelleme Kartı */
    .alert-detour {
        background: #fff1f2;
        border: 1.5px solid #fecdd3;
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 16px;
    }
    .detour-tag {
        display: inline-block;
        background: #ffe4e6;
        color: #be123c;
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        padding: 3px 8px;
        border-radius: 6px;
        margin-bottom: 8px;
    }
    .detour-outcome {
        background: #ffffff;
        border-left: 4px solid #f59e0b;
        border-radius: 8px;
        padding: 12px 14px;
        margin: 10px 0;
        font-size: 0.92rem;
        line-height: 1.5;
        color: #78350f;
    }
    .detour-rationale {
        background: #eff6ff;
        border-left: 4px solid #3b82f6;
        border-radius: 8px;
        padding: 12px 14px;
        margin: 10px 0;
        font-size: 0.92rem;
        line-height: 1.5;
        color: #1e3a8a;
    }

    /* İnteraktif Tıbbi Hover Tooltip Rozetleri */
    .med-val {
        position: relative;
        display: inline-block;
        font-weight: 700;
        padding: 2px 7px;
        margin: 0 2px;
        border-radius: 6px;
        cursor: help;
        transition: all 0.2s ease;
        border-bottom: 2px dashed;
        line-height: 1.35;
    }
    .med-val-normal {
        background-color: #dcfce7 !important;
        color: #14532d !important;
        border-bottom-color: #22c55e !important;
    }
    .med-val-high {
        background-color: #fee2e2 !important;
        color: #991b1b !important;
        border-bottom-color: #ef4444 !important;
    }
    .med-val-low {
        background-color: #e0f2fe !important;
        color: #0369a1 !important;
        border-bottom-color: #0284c7 !important;
    }
    .med-val:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    .med-val .med-tooltip {
        visibility: hidden;
        opacity: 0;
        position: absolute;
        bottom: 130%;
        left: 50%;
        transform: translateX(-50%);
        background-color: #0f172a;
        color: #f8fafc;
        text-align: center;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 0.82rem;
        font-weight: 500;
        line-height: 1.3;
        white-space: nowrap;
        z-index: 999999;
        box-shadow: 0 8px 24px -2px rgba(0, 0, 0, 0.4);
        pointer-events: none;
        transition: opacity 0.2s ease, transform 0.2s ease;
    }
    .med-val:hover .med-tooltip {
        visibility: visible;
        opacity: 1;
        transform: translateX(-50%) translateY(-2px);
    }
    .med-val .med-tooltip::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: #0f172a transparent transparent transparent;
    }

    /* Streamlit Buton Özelleştirmeleri */
    div[data-testid="stButton"] button {
        border-radius: 10px !important;
        font-weight: 500 !important;
        padding: 12px 16px !important;
        line-height: 1.45 !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        border: 1px solid #cbd5e1 !important;
        white-space: normal !important;
        height: auto !important;
        min-height: 48px !important;
        text-align: left !important;
        display: flex !important;
        align-items: center !important;
    }
    div[data-testid="stButton"] button div,
    div[data-testid="stButton"] button p {
        white-space: normal !important;
        word-break: break-word !important;
        overflow-wrap: break-word !important;
        text-align: left !important;
        display: block !important;
        line-height: 1.45 !important;
        text-overflow: clip !important;
        overflow: visible !important;
    }
    div[data-testid="stButton"] button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
        border-color: #0284c7 !important;
    }
    div[data-testid="stButton"] button[kind="primary"] {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%) !important;
        border: none !important;
        color: #ffffff !important;
    }

    /* Scroll iframe gizleme */
    iframe[title="scroll-to-top"],
    iframe[title="st.iframe"],
    iframe[title="streamlit.components.v1.html"] {
        position: absolute !important;
        height: 0px !important;
        width: 0px !important;
        border: none !important;
        visibility: hidden !important;
        pointer-events: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def scroll_to_top():
    """Yeni aşama veya vakaya geçildiğinde ekranı sayfa başına kaydırır."""
    ts = time.time()
    js = f"""
    <div id="scroll-trigger-{ts}" style="display:none;"></div>
    <script>
        (function() {{
            function scrollToTop() {{
                try {{
                    const p = window.parent;
                    const doc = p.document;
                    if (doc.activeElement && typeof doc.activeElement.blur === 'function') {{
                        doc.activeElement.blur();
                    }}
                    const anchor = doc.getElementById('page-top-anchor');
                    if (anchor && typeof anchor.scrollIntoView === 'function') {{
                        anchor.scrollIntoView({{ behavior: 'auto', block: 'start' }});
                    }}
                    const targets = [
                        doc.querySelector('[data-testid="stAppViewContainer"]'),
                        doc.querySelector('[data-testid="stMain"]'),
                        doc.querySelector('section.main'),
                        doc.querySelector('.main'),
                        doc.documentElement,
                        doc.body,
                        p
                    ];
                    targets.forEach(t => {{
                        if (t) {{
                            if (typeof t.scrollTo === 'function') {{
                                t.scrollTo({{ top: 0, left: 0, behavior: 'auto' }});
                            }}
                            t.scrollTop = 0;
                        }}
                    }});
                }} catch (e) {{
                    try {{
                        window.scrollTo(0, 0);
                    }} catch (err) {{}}
                }}
            }}
            scrollToTop();
            setTimeout(scrollToTop, 25);
            setTimeout(scrollToTop, 75);
            setTimeout(scrollToTop, 150);
            setTimeout(scrollToTop, 300);
        }})();
    </script>
    """
    if hasattr(st, "iframe"):
        st.iframe(src=js, height=1, width=1, alt="scroll-to-top")
    else:
        import streamlit.components.v1 as components
        components.html(js, height=0, width=0)


CATEGORIES = [
    "Tüm Semptomlar (Rastgele Vaka)",
    "👂 Kulak Ağrısı & KBB",
    "👁️ Göz Şikayetleri",
    "🫁 Hırıltı & Solunum Sıkıntısı",
    "👶 Ağlayan, Emmeyen, Huzursuz Bebek",
    "🌡️ Ateş & Döküntü / Enfeksiyon",
    "🤢 Karın Ağrısı, Kusma & İshal (GİS)",
    "🧠 Nörolojik Belirtiler & Konvülziyon",
    "⚡ Alerji, Zehirlenme & Diğer Aciller",
]


def init_state():
    """Session state değişkenlerini başlatır."""
    defaults = {
        "page": "home",              # "home", "simulation", "completed"
        "zone": None,                # "GREEN" veya "YELLOW"
        "effective_zone": None,      # Yeşil'den Sarı'ya devir olduğunda "YELLOW_TRANSFER" olur
        "current_case": None,        # Aktif vaka sözlüğü
        "selected_category": "Tüm Semptomlar (Rastgele Vaka)",
        "step_idx": 0,               # Aktif soru aşaması (0, 1, 2, 3...)
        "clinical_logs": [],         # Doğru adımlarla biriken muayene/tetkik bulguları
        "active_detour": None,       # Yanlış seçim yapıldığında tetiklenen senaryo güncellemesi
        "show_hint": False,          # Mevcut aşamanın doğru cevabını ve açıklamasını göster
        "seen_green_ids": set(),     # Çözülen yeşil alan vakaları
        "seen_yellow_ids": set(),    # Çözülen sarı alan vakaları
        "last_step_feedback": None,  # Doğru adım sonrası gösterilecek kısa klinik açıklama
        "shuffled_options": {},      # Her aşama için karıştırılmış seçenek dizilimi
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def pick_random_case(zone: str, category: str = None):
    """Belirtilen alandan ve isteğe bağlı kategoriden henüz çözülmemiş rastgele bir vaka seçer."""
    if category is None:
        category = st.session_state.get("selected_category", "Tüm Semptomlar (Rastgele Vaka)")
    st.session_state.selected_category = category

    if zone == "GREEN":
        pool = GREEN_CASES
        seen = st.session_state.seen_green_ids
    else:
        pool = YELLOW_CASES
        seen = st.session_state.seen_yellow_ids

    if category and category != "Tüm Semptomlar (Rastgele Vaka)":
        filtered_pool = [c for c in pool if c.get("category") == category]
        if filtered_pool:
            pool = filtered_pool
        else:
            st.toast(f"'{category}' grubunda bu alana ait vaka bulunmadığı için tüm {zone} vakalarından seçildi.", icon="ℹ️")

    available = [c for c in pool if c["id"] not in seen]
    if not available:
        for c in pool:
            seen.discard(c["id"])
        available = list(pool)

    chosen = random.choice(available)
    seen.add(chosen["id"])

    st.session_state.zone = zone
    st.session_state.effective_zone = zone
    st.session_state.current_case = chosen
    st.session_state.step_idx = 0
    st.session_state.clinical_logs = []
    st.session_state.active_detour = None
    st.session_state.show_hint = False
    st.session_state.last_step_feedback = None
    st.session_state.shuffled_options = {
        s_idx: random.sample(s["options"], len(s["options"]))
        for s_idx, s in enumerate(chosen["steps"])
    }
    st.session_state.page = "simulation"


def go_home():
    """Ana sayfaya döner."""
    st.session_state.page = "home"
    st.session_state.current_case = None
    st.session_state.active_detour = None
    st.session_state.show_hint = False
    st.session_state.last_step_feedback = None


def render_home():
    """Ana sayfa: Modern portal tasarımı, filtreler ve istatistikler."""
    st.markdown('<div id="page-top-anchor" style="position:relative;top:0;left:0;width:1px;height:1px;"></div>', unsafe_allow_html=True)
    scroll_to_top()

    st.markdown('<div class="hero-title">Pediatrik Acil Klinik Simülasyon Kokpiti</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">Kanıta dayalı pediatrik acil yönetimi (AAP, ESPGHAN, PALS) • 140 Gerçekçi Vaka • İki Kolonlu Klinik Karar İstasyonu</div>',
        unsafe_allow_html=True,
    )

    # Semptom Kategori Seçici & Metrikler
    cat_col1, cat_col2 = st.columns([3, 1])
    with cat_col1:
        current_cat = st.session_state.get("selected_category", CATEGORIES[0])
        idx = CATEGORIES.index(current_cat) if current_cat in CATEGORIES else 0
        selected = st.selectbox(
            "🎯 Klinik Başvuru / Semptom Filtresi:",
            CATEGORIES,
            index=idx,
            key="select_symptom_category",
            help="İstediğiniz bir şikayet grubuna odaklanabilir veya 140 vakanın tamamından rastgele vaka alabilirsiniz.",
        )
        st.session_state.selected_category = selected
    with cat_col2:
        st.write("")
        st.write("")
        if selected != "Tüm Semptomlar (Rastgele Vaka)":
            green_cnt = len([c for c in GREEN_CASES if c.get("category") == selected])
            yellow_cnt = len([c for c in YELLOW_CASES if c.get("category") == selected])
            st.info(f"🟢 Yeşil: {green_cnt} | 🟡 Sarı: {yellow_cnt}")
        else:
            st.info(f"Toplam 140 Vaka (🟢 70 Yeşil + 🟡 70 Sarı)")

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div class="portal-card portal-card-green">
                <div>
                    <span class="portal-badge badge-green">🟢 Triyaj: Düşük / Orta Risk</span>
                    <div class="portal-title">A - YEŞİL ALAN SİMÜLASYONU</div>
                    <div class="portal-desc">
                        <b>Ayaktan Poliklinik & Yeşil Alan Yönetimi (70 Vaka)</b><br>
                        Akut farenjit, basit otit, gastroenterit, hafif dehidratasyon, geçici sinovit, süt alerjisi, krup, migren ve epistaksis gibi yaygın acil başvuruları.<br><br>
                        <i>Önemli: Çoğunluğu ayaktan çözülürken, gizli kırmızı bayraklar (örneğin dehidratasyon derinleşmesi veya respiratuar bozulma) Sarı Alana acil devir gerektirebilir!</i>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("🟢 YEŞİL ALAN SİMÜLASYONUNU BAŞLAT", key="btn_home_start_green", use_container_width=True, type="primary"):
            pick_random_case("GREEN", st.session_state.selected_category)
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="portal-card portal-card-yellow">
                <div>
                    <span class="portal-badge badge-yellow">🟡 Triyaj: Acil Gözlem & Stabilizasyon</span>
                    <div class="portal-title">B - SARI ALAN SİMÜLASYONU</div>
                    <div class="portal-desc">
                        <b>Acil Gözlem & Yatış Kararı Yönetimi (70 Vaka)</b><br>
                        Kawasaki vasküliti, septik artrit, nefritik/nefrotik sendrom, febril nötropeni, orak hücreli ağrı krizi, ağır sarılık, adrenal kriz ve karbonmonoksit intoksikasyonu gibi kritik tablolar.<br><br>
                        <i>Önemli: Yakın hemodinamik telemetri, acil parenteral tedavi ve hedefe yönelik yatış/taburculuk kararı gerektirir.</i>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("🟡 SARI ALAN SİMÜLASYONUNU BAŞLAT", key="btn_home_start_yellow", use_container_width=True, type="primary"):
            pick_random_case("YELLOW", st.session_state.selected_category)
            st.rerun()

    st.markdown("<br><hr>", unsafe_allow_html=True)
    with st.expander("📖 Simülasyon ve Klinik Kokpit Nasıl Çalışır?"):
        st.markdown(
            """
            - **İki Kolonlu Klinik Kokpit:** Sol kolonda hastanın demografisi, dijital telemetri monitörü ve zaman tüneli; sağ kolonda ise o anki aşamanın karar masası bulunur.
            - **Sayfa Şişmesini Önleyen Mimari:** İlerleyen aşamalarda elde edilen tetkik ve muayene bulguları sol kolondaki kompakt zaman tünelinde saklanır, ekran gereksiz aşağı uzamaz.
            - **Dinamik Senaryo Güncellemesi (Detour):** Hatalı veya gereksiz bir tetkik/tedavi seçildiğinde senaryo o kararın sonucuna göre anında güncellenir ve kanıta dayalı pedagojik geri bildirim verilir.
            - **İnteraktif Yaşa Duyarlı Vitaller:** Ateş, KTA, SS, SpO2, TA gibi vital bulguların üzerine mouse ile geldiğinizde yaş grubuna göre Normal / Yüksek / Düşük değerlendirmesi açılır.
            """
        )


def render_top_navigation():
    """Klinik kokpit üst navigasyon ve acil alan eylemleri."""
    c1, c2, c3 = st.columns([2, 3, 2])
    with c1:
        if st.button("🏠 Ana Sayfaya Dön", key="top_btn_home", use_container_width=True):
            go_home()
            st.rerun()
    with c2:
        zone_label = "Yeşil Alan" if st.session_state.zone == "GREEN" else "Sarı Alan"
        if st.button(f"🔄 Bu Vakayı Değiştir (Yeni {zone_label} Vakası Al)", key="top_btn_new_case", use_container_width=True):
            pick_random_case(st.session_state.zone, st.session_state.get("selected_category"))
            st.rerun()
    with c3:
        other_zone = "YELLOW" if st.session_state.zone == "GREEN" else "GREEN"
        other_label = "🟡 Sarı Alan'a Geç" if other_zone == "YELLOW" else "🟢 Yeşil Alan'a Geç"
        if st.button(other_label, key="top_btn_switch_zone", use_container_width=True):
            pick_random_case(other_zone, st.session_state.get("selected_category"))
            st.rerun()


def render_stepper(current_idx: int, total_steps: int):
    """4 aşamalı klinik süreç akışını gösteren interaktif stepper."""
    step_titles = [
        "1. İlk Değerlendirme & Muayene",
        "2. İleri Tetkikler & İnceleme",
        "3. Ayırıcı & Kesin Tanı",
        "4. Tedavi & Triyaj Kararı",
    ]
    html = ['<div class="stepper-wrapper">']
    for idx in range(total_steps):
        title = step_titles[idx] if idx < len(step_titles) else f"{idx+1}. Aşama"
        if idx < current_idx:
            status_class = "completed"
            pill_content = "✓"
        elif idx == current_idx:
            status_class = "active"
            pill_content = str(idx + 1)
        else:
            status_class = ""
            pill_content = str(idx + 1)

        html.append(f'<div class="step-node {status_class}"><div class="step-pill">{pill_content}</div><span>{title}</span></div>')
        if idx < total_steps - 1:
            div_class = "completed" if idx < current_idx else ""
            html.append(f'<div class="step-divider {div_class}"></div>')
    html.append('</div>')
    st.markdown("".join(html), unsafe_allow_html=True)


def render_simulation():
    """İki Kolonlu Modern Klinik Kokpit / Acil Çalışma İstasyonu Ekranı."""
    case = st.session_state.current_case
    if not case:
        go_home()
        st.rerun()
        return

    st.markdown('<div id="page-top-anchor" style="position:relative;top:0;left:0;width:1px;height:1px;"></div>', unsafe_allow_html=True)
    scroll_to_top()

    # 1. Üst Navigasyon
    render_top_navigation()

    steps = case["steps"]
    total_steps = len(steps)
    current_idx = st.session_state.step_idx
    eff_zone = st.session_state.effective_zone

    # 2. İnteraktif Klinik İlerleme Stepper'ı
    render_stepper(current_idx, total_steps)

    # 3. İki Kolonlu Split-Screen Yerleşim
    col_left, col_right = st.columns([4.8, 5.2], gap="large")

    # ==========================================
    # SOL KOLON: HASTA DOSYASI & KLİNİK İZLEM
    # ==========================================
    with col_left:
        st.markdown(
            """
            <div class="emr-panel">
                <div class="emr-panel-header">
                    <span class="emr-title">📋 HASTA DOSYASI & KLİNİK BİLGİLER</span>
                    <span style="font-size:0.8rem; font-weight:700; color:#64748b;">KAYIT NO: """ + case["id"] + """</span>
                </div>
            """,
            unsafe_allow_html=True,
        )

        # Hasta Demografisi Rozetleri
        cat_badge = case.get("category", "Genel Acil")
        zone_badge = "🟢 YEŞİL ALAN" if eff_zone == "GREEN" else ("🚨 SARI ALANA DEVİR" if eff_zone == "YELLOW_TRANSFER" else "🟡 SARI ALAN")
        zone_class = "demo-tag-accent" if eff_zone == "GREEN" else "demo-tag-yellow"

        st.markdown(
            f"""
            <div class="patient-demographics">
                <span class="demo-tag">👶 Yaş: <b>{case["age"]}</b></span>
                <span class="demo-tag">🚻 Cinsiyet: <b>{case["gender"]}</b></span>
                <span class="demo-tag {zone_class}"><b>{zone_badge}</b></span>
                <span class="demo-tag" style="background:#eff6ff; border-color:#bfdbfe; color:#1d4ed8;">{cat_badge}</span>
            </div>
            <div style="font-size:0.92rem; color:#1e293b; margin-bottom:12px;">
                <b>Başvuru Şikayeti:</b> <span style="color:#0369a1; font-weight:600;">{case["complaint"]}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Dijital Hasta Telemetri & Vital Monitörü (Beside Emergency Monitor)
        raw_vitals = get_case_vitals(case)
        vitals_html = annotate_clinical_text(raw_vitals, case["age"])
        st.markdown(
            f"""
            <div class="telemetry-card">
                <div class="telemetry-header">
                    <span><span class="telemetry-pulse"></span>ACİL GELİŞ TELEMETRİ & VİTAL MONİTÖRÜ</span>
                    <span>ONLINE • LIVE</span>
                </div>
                <div class="telemetry-content">
                    {vitals_html}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Anamnez / Kısa Öykü
        history_html = annotate_clinical_text(case["history"], case["age"])
        st.markdown(
            f"""
            <div class="anamnesis-box">
                <div style="font-weight:700; color:#0f172a; font-size:0.83rem; text-transform:uppercase; margin-bottom:4px;">
                    🗣️ Anamnez & Hasta Öyküsü:
                </div>
                {history_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Zaman Tüneli: Bu Vakada Şimdiye Kadar Elde Edilen Klinik Bulgular (Scrollable Timeline)
        if st.session_state.clinical_logs:
            st.markdown(
                """
                <div style="font-weight:700; color:#0f172a; font-size:0.83rem; text-transform:uppercase; margin-top:14px; margin-bottom:6px; display:flex; justify-content:space-between; align-items:center;">
                    <span>📂 KLİNİK BULGULAR & İZLEM NOTLARI:</span>
                    <span style="font-size:0.75rem; color:#64748b; font-weight:500;">(Kronolojik Akış)</span>
                </div>
                <div class="timeline-container">
                """,
                unsafe_allow_html=True,
            )
            for item in st.session_state.clinical_logs:
                finding_html = annotate_clinical_text(item["finding"], case["age"])
                st.markdown(
                    f"""
                    <div class="timeline-node">
                        <div class="timeline-node-title">✓ {item['stage']}</div>
                        <div>{finding_html}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if item.get("image") and os.path.exists(item["image"]):
                    st.image(item["image"], caption=item.get("image_caption", "Görüntüleme / Tetkik Bulgusu"), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # SAĞ KOLON: KLİNİK KARAR MASASI
    # ==========================================
    with col_right:
        step = steps[current_idx]

        st.markdown(
            f"""
            <div class="decision-panel">
                <span class="stage-badge">AŞAMA {current_idx + 1} / {total_steps} • {step["stage_title"]}</span>
            """,
            unsafe_allow_html=True,
        )

        # Önceki Adım Değerlendirmesi Varsa Bilgi Olarak Ver
        if st.session_state.last_step_feedback and st.session_state.active_detour is None:
            st.success(f"**✓ Önceki Aşama Kararınız:** {st.session_state.last_step_feedback}")

        # EĞER YANLIŞ SEÇİM YAPILDIYSA (DETOUR / SENARYO GÜNCELLEMESİ)
        if st.session_state.active_detour is not None:
            detour = st.session_state.active_detour
            scen_html = annotate_clinical_text(detour["scenario_update"], case["age"])
            teach_html = annotate_clinical_text(detour["teaching_point"], case["age"])

            st.markdown(
                f"""
                <div class="alert-detour">
                    <span class="detour-tag">⚠️ KLİNİK SENARYO GÜNCELLEMESİ</span>
                    <div style="font-size:0.95rem; font-weight:600; color:#881337; margin-bottom:8px;">
                        Seçilen Karar: <i>"{detour["selected_text"]}"</i>
                    </div>
                    <div class="detour-outcome">
                        <b>🔄 Ne Oldu? (İstem / Müdahale Sonucu):</b><br>
                        {scen_html}
                    </div>
                """,
                unsafe_allow_html=True,
            )

            if detour.get("image") and os.path.exists(detour["image"]):
                st.image(detour["image"], caption=detour.get("image_caption", "İstenen Görüntüleme"), use_container_width=True)

            st.markdown(
                f"""
                    <div class="detour-rationale">
                        <b>🎓 Kanıta Dayalı Klinik Rehber Noktası:</b><br>
                        {teach_html}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                if st.button("↩️ Kararı Değiştir (Soruya Dön)", key="btn_detour_return", use_container_width=True, type="primary"):
                    st.session_state.active_detour = None
                    st.rerun()
            with btn_col2:
                if st.button("💡 İpucu Al ve Soruya Dön", key="btn_detour_hint", use_container_width=True):
                    st.session_state.active_detour = None
                    st.session_state.show_hint = True
                    st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)
            return

        # NORMAL KARAR VERME DURUMU: SORU VE SEÇENEKLER
        q_html = annotate_clinical_text(step["question"], case["age"])
        st.markdown(
            f"""
            <div class="question-headline">
                ❓ {q_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # İpucu Alanı
        if st.session_state.show_hint:
            current_opts = st.session_state.shuffled_options.get(current_idx, step["options"])
            correct_opt = next((o for o in current_opts if o.get("is_correct")), None)
            if correct_opt:
                st.info(
                    f"**🎯 Önerilen Kanıta Dayalı Yaklaşım:** {correct_opt['text']}\n\n"
                    f"**📘 Rehber Gerekçesi:** {correct_opt['explanation']}"
                )

        st.markdown("<p style='font-size:0.86rem; font-weight:700; color:#64748b; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:10px;'>Klinik Karar Seçenekleri:</p>", unsafe_allow_html=True)

        current_opts = st.session_state.shuffled_options.get(current_idx, step["options"])
        for idx, opt in enumerate(current_opts):
            letter = chr(65 + idx)
            btn_label = f"[{letter}]  {opt['text']}"
            if st.button(btn_label, key=f"opt_{current_idx}_{idx}", use_container_width=True):
                if opt.get("is_correct"):
                    st.session_state.active_detour = None
                    st.session_state.show_hint = False
                    st.session_state.last_step_feedback = opt["explanation"]

                    if opt.get("new_finding"):
                        st.session_state.clinical_logs.append(
                            {
                                "stage": step["stage_title"],
                                "finding": opt["new_finding"],
                                "image": opt.get("image"),
                                "image_caption": opt.get("image_caption", "Görüntüleme / Tetkik Bulgusu"),
                            }
                        )

                    if opt.get("triggers_yellow_transfer"):
                        st.session_state.effective_zone = "YELLOW_TRANSFER"

                    if current_idx + 1 < total_steps:
                        st.session_state.step_idx += 1
                    else:
                        st.session_state.page = "completed"
                    st.rerun()
                else:
                    st.session_state.active_detour = {
                        "selected_text": opt["text"],
                        "scenario_update": opt["scenario_update"],
                        "teaching_point": opt["teaching_point"],
                        "image": opt.get("image"),
                        "image_caption": opt.get("image_caption", "İstenen Görüntüleme / Tetkik"),
                    }
                    st.rerun()

        # Alt Bölüm: İpucu Butonu
        st.markdown("<br>", unsafe_allow_html=True)
        hint_label = "🙈 İpucunu Kapat" if st.session_state.show_hint else "💡 Bu Aşama İçin Klinik İpucu Göster"
        if st.button(hint_label, key=f"btn_hint_toggle_{current_idx}", use_container_width=True):
            st.session_state.show_hint = not st.session_state.show_hint
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)


def render_completed():
    """Vaka başarıyla tamamlandığında iki kolonlu profesyonel epikriz ve klinik inciler ekranı."""
    case = st.session_state.current_case
    if not case:
        go_home()
        st.rerun()
        return

    st.markdown('<div id="page-top-anchor" style="position:relative;top:0;left:0;width:1px;height:1px;"></div>', unsafe_allow_html=True)
    scroll_to_top()

    render_top_navigation()

    eff_zone = st.session_state.effective_zone
    if eff_zone == "YELLOW_TRANSFER":
        badge_text = "🚨 YEŞİL ALANDAN BAŞLAYIP SARI ALANA DEVREDİLEN VAKA TAMAMLANDI"
        badge_style = "background:#ffedd5; color:#9a3412; border:1px solid #fdba74;"
    elif eff_zone == "GREEN":
        badge_text = "🟢 YEŞİL ALAN POLİKLİNİK VAKASI TAMAMLANDI"
        badge_style = "background:#ecfdf5; color:#065f46; border:1px solid #a7f3d0;"
    else:
        badge_text = "🟡 SARI ALAN ACİL GÖZLEM VAKASI TAMAMLANDI"
        badge_style = "background:#fefce8; color:#854d0e; border:1px solid #fde047;"

    st.balloons()

    # İki Kolonlu Epikriz & Değerlendirme
    comp_col1, comp_col2 = st.columns([5, 5], gap="large")

    with comp_col1:
        st.markdown(
            f"""
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:16px; padding:22px; box-shadow:0 4px 16px -2px rgba(0,0,0,0.04);">
                <span style="display:inline-block; font-size:0.75rem; font-weight:700; padding:4px 10px; border-radius:20px; {badge_style} margin-bottom:10px;">
                    {badge_text}
                </span>
                <h2 style="color:#0f172a; margin-top:0; font-size:1.45rem; font-weight:800;">
                    ✓ Teşhis ve Tedavi Protokolü Doğrulandı
                </h2>
                <div style="background:#f8fafc; border-left:4px solid #059669; border-radius:8px; padding:14px; margin-bottom:14px;">
                    <div style="font-size:0.8rem; font-weight:700; color:#475569; text-transform:uppercase;">Kesin Klinik Tanı:</div>
                    <div style="font-size:1.15rem; font-weight:800; color:#065f46; margin-top:2px;">{case["final_diagnosis"]}</div>
                </div>
                <div style="background:#f8fafc; border-left:4px solid #0284c7; border-radius:8px; padding:14px;">
                    <div style="font-size:0.8rem; font-weight:700; color:#475569; text-transform:uppercase;">Taburculuk / Yatış Kararı (Disposition):</div>
                    <div style="font-size:1.05rem; font-weight:600; color:#0f172a; margin-top:2px;">{case["disposition"]}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:16px; padding:20px; margin-top:16px; box-shadow:0 4px 16px -2px rgba(0,0,0,0.04);">
                <div style="font-weight:700; color:#0f172a; font-size:0.85rem; text-transform:uppercase; margin-bottom:10px;">
                    📋 Vaka Boyunca Elde Edilen Epikriz Özeti:
                </div>
            """,
            unsafe_allow_html=True,
        )
        for item in st.session_state.clinical_logs:
            finding_html = annotate_clinical_text(item["finding"], case["age"])
            st.markdown(f"<b>✓ {item['stage']}:</b> {finding_html}", unsafe_allow_html=True)
            if item.get("image") and os.path.exists(item["image"]):
                st.image(item["image"], caption=item.get("image_caption", "Görüntüleme Sonucu"), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with comp_col2:
        st.markdown(
            """
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:16px; padding:22px; box-shadow:0 4px 16px -2px rgba(0,0,0,0.04);">
                <div style="display:flex; align-items:center; gap:6px; font-weight:800; color:#0369a1; font-size:0.95rem; text-transform:uppercase; margin-bottom:12px;">
                    🎓 KLİNİK İNCİLER & KANITA DAYALI ÖĞRENME NOKTALARI
                </div>
            """,
            unsafe_allow_html=True,
        )
        st.info(case["case_pearl"])
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        zone_label = "Yeşil Alan" if st.session_state.zone == "GREEN" else "Sarı Alan"
        if st.button(f"▶️ Yeni {zone_label} Vakasına Geç", key="btn_completed_next_case", use_container_width=True, type="primary"):
            pick_random_case(st.session_state.zone, st.session_state.get("selected_category"))
            st.rerun()

        other_zone = "YELLOW" if st.session_state.zone == "GREEN" else "GREEN"
        other_label = "🟡 Sarı Alan Vakası Çöz" if other_zone == "YELLOW" else "🟢 Yeşil Alan Vakası Çöz"
        if st.button(other_label, key="btn_completed_switch_zone", use_container_width=True):
            pick_random_case(other_zone, st.session_state.get("selected_category"))
            st.rerun()

        if st.button("🏠 Ana Sayfaya Dön", key="btn_completed_home", use_container_width=True):
            go_home()
            st.rerun()


def main():
    init_state()
    if st.session_state.page == "home":
        render_home()
    elif st.session_state.page == "simulation":
        render_simulation()
    elif st.session_state.page == "completed":
        render_completed()


if __name__ == "__main__":
    main()
