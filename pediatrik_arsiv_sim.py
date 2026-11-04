# -*- coding: utf-8 -*-
"""
Pediatrik Acil Vaka Arşivi (The Pediatric Emergency Archive)
The Story Archive modeline tam sadık:
- 3 Kolonlu sabit kart gridi (kartın her yerine tıklanabilir)
- Sağdan kayan sabit çekmece (Fixed Slide-Over Drawer - scroll gerektirmez, layout bozmaz)
- Siyah telemetri kutusu yerine krem/arşiv kağıt estetiğinde vitaller
- %100 zoom'da taşmayan, çok satırlı esnek seçenek butonları
"""

import os
import random
import time
import importlib
import re
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
    from pediatric_evaluator import annotate_clinical_text, parse_age_in_months

    def get_case_vitals(case: dict) -> str:
        if case.get('vitals'):
            return case['vitals']
        pattern = r'(?:Vital Bulgular|Vitalleri|vital bulgular)[:]?\s*([^\n]+?)(?=\.\s+[A-ZĞÜŞİÖÇ]|\.\s*$|\n|$)'
        hist = case.get('history', '')
        m = re.search(pattern, hist, re.IGNORECASE)
        if m:
            return m.group(0).strip()
        age_m = parse_age_in_months(case.get('age', ''))
        return 'Vital Bulgular: Ateş 36.7°C, KTA 110/dk, SS 24/dk, SpO2 %99'

st.set_page_config(
    page_title="Pediatrik Acil Vaka Arşivi",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom Styling: The Story Archive Exact Aesthetic + Fixed Slide-Over Drawer
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap');

    /* Genel Sayfa Stili */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background-color: #faf9f6;
        color: #1a1a1a;
    }

    /* Üst Başlık */
    .archive-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px 0 10px 0;
        border-bottom: 1.5px solid #1a1a1a;
        margin-bottom: 12px;
    }
    .archive-logo {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.6rem;
        font-weight: 700;
        letter-spacing: -0.03em;
        color: #1a1a1a;
    }
    .archive-icons {
        display: flex;
        gap: 16px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.88rem;
        color: #4a4a4a;
    }

    /* Kart Izgarası Stilleri */
    .card-wrapper {
        position: relative;
        margin-bottom: 18px;
    }
    .archive-card {
        background: #ffffff;
        border: 1.5px solid #10b981;
        border-radius: 8px;
        padding: 16px 18px;
        box-shadow: 2px 2px 0px rgba(0, 0, 0, 0.08);
        transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 245px;
        cursor: pointer;
    }
    .archive-card-yellow {
        border-color: #b45309 !important;
    }
    .card-wrapper:hover .archive-card {
        transform: translateY(-2px);
        box-shadow: 4px 5px 0px rgba(0, 0, 0, 0.16);
        border-color: #1a1a1a !important;
    }

    .card-top {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 8px;
    }
    .card-title {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.02rem;
        font-weight: 700;
        color: #0f172a;
        line-height: 1.35;
        flex: 1;
        margin-right: 8px;
    }
    .card-category-pill {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        font-weight: 600;
        padding: 3px 8px;
        border-radius: 12px;
        white-space: nowrap;
        background: #047857;
        color: #ffffff;
    }
    .pill-yellow {
        background: #b45309 !important;
    }

    .card-meta {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.76rem;
        color: #64748b;
        margin-bottom: 10px;
    }
    .card-complaint {
        font-size: 0.88rem;
        line-height: 1.45;
        color: #334155;
        margin-bottom: 12px;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    /* Etiket Çipleri (The Story Archive Tags) */
    .card-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-top: auto;
        padding-top: 8px;
    }
    .tag-chip {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        padding: 2px 7px;
        border-radius: 10px;
        background: #fbf8f3;
        border: 1px solid #d4a373;
        color: #7f4f24;
    }

    .card-click-hint {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        font-weight: 600;
        color: #0369a1;
        margin-top: 10px;
        border-top: 1px dashed #e2e8f0;
        padding-top: 6px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    /* Kart Sarmalayıcısı ve Tıklanabilir Şeffaf Buton Overlay */
    div[class*="st-key-card_box_"] {
        position: relative !important;
        margin-bottom: 18px !important;
    }
    div[class*="st-key-card_box_"] div[class*="st-key-btn_overlay_"],
    div[class*="st-key-btn_overlay_"] {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        z-index: 50 !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    div[class*="st-key-btn_overlay_"] div[data-testid="stButton"],
    div[class*="st-key-btn_overlay_"] button {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        z-index: 50 !important;
        margin: 0 !important;
        padding: 0 !important;
        opacity: 0 !important;
        cursor: pointer !important;
        background: transparent !important;
        border: none !important;
    }
    div[class*="st-key-card_box_"]:hover .archive-card {
        transform: translateY(-2px);
        box-shadow: 4px 6px 0px rgba(0, 0, 0, 0.16);
        border-color: #1a1a1a !important;
    }

    /* ======================================================== */
    /* SABİT KAYAN ÇEKMECE (FIXED SLIDE-OVER DRAWER)              */
    /* Sayfada nerede olursanız olun ekranın sağında sabit açılır  */
    /* Layout'u bozmaz, yukarı scroll gerektirmez               */
    /* ======================================================== */
    div[class*="st-key-slide_over_drawer"] {
        position: fixed !important;
        top: 0 !important;
        right: 0 !important;
        bottom: 0 !important;
        width: 540px !important;
        max-width: 92vw !important;
        height: 100vh !important;
        background: #faf9f6 !important;
        border-left: 2px solid #1a1a1a !important;
        box-shadow: -12px 0 40px rgba(0, 0, 0, 0.22) !important;
        z-index: 999999 !important;
        overflow-y: auto !important;
        padding: 24px 22px !important;
        display: flex !important;
        flex-direction: column !important;
        animation: drawerSlideIn 0.24s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    @keyframes drawerSlideIn {
        from { transform: translateX(100%); }
        to { transform: translateX(0); }
    }

    .story-backdrop {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        background: rgba(0, 0, 0, 0.22) !important;
        z-index: 999990 !important;
        backdrop-filter: blur(1.5px) !important;
        pointer-events: none !important;
    }

    .drawer-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        border-bottom: 1.5px solid #1a1a1a;
        padding-bottom: 12px;
        margin-bottom: 14px;
    }
    .drawer-title {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.25rem;
        font-weight: 800;
        color: #0f172a;
        line-height: 1.3;
    }
    .drawer-meta {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        color: #64748b;
        margin-top: 4px;
    }

    /* YENİLENEN VİTAL KARTI (SİYAH KUTU KALDIRILDI - KREM / ARŞİV KAĞIT TEMASI) */
    .drawer-vitals-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #059669;
        border-radius: 8px;
        padding: 12px 14px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.86rem;
        line-height: 1.65;
        margin-bottom: 14px;
        box-shadow: 1px 1px 0px rgba(0, 0, 0, 0.04);
    }
    .vitals-card-yellow {
        border-left-color: #b45309 !important;
    }
    .vitals-header {
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        color: #475569;
        text-transform: uppercase;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Anamnez ve Metin Kutuları */
    .drawer-box {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 12px 14px;
        font-size: 0.92rem;
        line-height: 1.55;
        color: #1e293b;
        margin-bottom: 14px;
        box-shadow: 1px 1px 0px rgba(0, 0, 0, 0.03);
    }

    .drawer-stepper {
        display: flex;
        gap: 6px;
        align-items: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.76rem;
        color: #64748b;
        margin-bottom: 14px;
        padding: 8px 12px;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
    }
    .drawer-stepper-active {
        font-weight: 700;
        color: #0284c7;
    }

    .drawer-alert {
        background: #fff1f2;
        border: 1.5px solid #fecdd3;
        border-radius: 8px;
        padding: 14px;
        margin-bottom: 14px;
        font-size: 0.88rem;
        line-height: 1.5;
    }

    /* Çekmece İçindeki Butonlar: Çok Satırlı Sarma & Tam Metin (%100 Zoom Uyumlu) */
    div[class*="st-key-slide_over_drawer"] div[data-testid="stButton"] button {
        opacity: 1 !important;
        position: static !important;
        background: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 8px !important;
        padding: 11px 14px !important;
        text-align: left !important;
        white-space: normal !important;
        word-break: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.45 !important;
        width: 100% !important;
        height: auto !important;
        min-height: 48px !important;
        margin-bottom: 8px !important;
        display: flex !important;
        align-items: center !important;
    }
    div[class*="st-key-slide_over_drawer"] div[data-testid="stButton"] button div,
    div[class*="st-key-slide_over_drawer"] div[data-testid="stButton"] button p {
        white-space: normal !important;
        word-break: break-word !important;
        overflow-wrap: break-word !important;
        text-align: left !important;
        display: block !important;
        line-height: 1.45 !important;
        text-overflow: clip !important;
        overflow: visible !important;
    }
    div[class*="st-key-slide_over_drawer"] div[data-testid="stButton"] button:hover {
        border-color: #1a1a1a !important;
        background: #f8fafc !important;
        transform: translateY(-1px) !important;
    }
    div[class*="st-key-slide_over_drawer"] div[data-testid="stButton"] button[kind="primary"] {
        background: #1a1a1a !important;
        border-color: #1a1a1a !important;
        color: #ffffff !important;
    }

    /* Tooltip Stilleri (Arşiv Kağıdı ile Uyumlu) */
    .med-val {
        position: relative;
        display: inline-block;
        font-weight: 700;
        padding: 1px 6px;
        margin: 0 2px;
        border-radius: 4px;
        cursor: help;
        border-bottom: 1.5px dashed;
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
        padding: 5px 10px;
        border-radius: 6px;
        font-size: 0.78rem;
        font-weight: 500;
        white-space: nowrap;
        z-index: 9999999;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
        pointer-events: none;
        transition: opacity 0.2s ease;
    }
    .med-val:hover .med-tooltip {
        visibility: visible;
        opacity: 1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def init_state():
    """Arşiv durum değişkenleri."""
    defaults = {
        "active_tab": "ALL",
        "search_query": "",
        "selected_case_id": None,
        "drawer_step_idx": 0,
        "drawer_logs": [],
        "drawer_detour": None,
        "drawer_show_hint": False,
        "drawer_last_feedback": None,
        "drawer_shuffled_opts": {},
        "solved_case_ids": set(),
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def get_all_cases():
    return GREEN_CASES + YELLOW_CASES


def extract_card_tags(case: dict) -> list:
    tags = []
    comp = case.get("complaint", "").lower()
    age_str = case.get("age", "")
    if "gün" in age_str.lower():
        tags.append("Yenidoğan")
    elif "ay" in age_str.lower():
        tags.append("Süt Çocuğu")
    elif any(x in age_str for x in ["2 Yaş", "3 Yaş", "4 Yaş", "5 Yaş"]):
        tags.append("Oyun Çağı")
    else:
        tags.append("Okul / Ergen")

    keyword_map = [
        ("ateş", "Ateş"),
        ("kusma", "Kusma"),
        ("ishal", "İshal"),
        ("karın ağrı", "Karın Ağrısı"),
        ("öksürük", "Öksürük"),
        ("hırıltı", "Hırıltı"),
        ("dispne", "Dispne"),
        ("döküntü", "Döküntü"),
        ("baş ağrı", "Baş Ağrısı"),
        ("nöbet", "Konvülziyon"),
        ("şişlik", "Ödem"),
        ("sarılık", "Sarılık"),
        ("idrar", "Üriner"),
        ("ağlama", "Huzursuz Bebek"),
        ("eklem", "Artralji"),
        ("zehirlen", "Toksikoloji"),
    ]
    for kw, label in keyword_map:
        if kw in comp and label not in tags:
            tags.append(label)
        if len(tags) >= 4:
            break

    cat = case.get("category", "")
    if "GİS" in cat and "Gastroenteroloji" not in tags:
        tags.append("GİS")
    elif "Solunum" in cat and "Solunum" not in tags:
        tags.append("Respiratuar")
    elif "Nörolojik" in cat and "Nöroloji" not in tags:
        tags.append("Nöroloji")
    elif "Enfeksiyon" in cat and "Enfeksiyon" not in tags:
        tags.append("Enfeksiyon")

    return tags[:4]


def open_case(case_id: str):
    cases_dict = {c["id"]: c for c in get_all_cases()}
    chosen = cases_dict.get(case_id)
    if not chosen:
        return
    st.session_state.selected_case_id = case_id
    st.session_state.drawer_step_idx = 0
    st.session_state.drawer_logs = []
    st.session_state.drawer_detour = None
    st.session_state.drawer_show_hint = False
    st.session_state.drawer_last_feedback = None
    st.session_state.drawer_shuffled_opts = {
        s_idx: random.sample(s["options"], len(s["options"]))
        for s_idx, s in enumerate(chosen["steps"])
    }


def close_case():
    st.session_state.selected_case_id = None
    st.session_state.drawer_detour = None
    st.session_state.drawer_show_hint = False
    st.session_state.drawer_last_feedback = None


def render_archive_header():
    st.markdown(
        """
        <div class="archive-header">
            <div class="archive-logo">The Pediatric Emergency Archive</div>
            <div class="archive-icons">
                <span>140 Cases Online</span>
                <span>•</span>
                <span>Evidence-Based</span>
                <span>•</span>
                <span>AAP / PALS</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns([1.5, 1.5, 1.5, 5])
    with c1:
        if st.button("Tüm Vakalar (140)", key="tab_all", use_container_width=True,
                     type="primary" if st.session_state.active_tab == "ALL" else "secondary"):
            st.session_state.active_tab = "ALL"
            st.rerun()
    with c2:
        if st.button("🟢 Yeşil Alan (70)", key="tab_green", use_container_width=True,
                     type="primary" if st.session_state.active_tab == "GREEN" else "secondary"):
            st.session_state.active_tab = "GREEN"
            st.rerun()
    with c3:
        if st.button("🟡 Sarı Alan (70)", key="tab_yellow", use_container_width=True,
                     type="primary" if st.session_state.active_tab == "YELLOW" else "secondary"):
            st.session_state.active_tab = "YELLOW"
            st.rerun()
    with c4:
        st.session_state.search_query = st.text_input(
            "Arşivde Ara:",
            placeholder="🔍 Semptom, yaş, şikayet veya vaka kodu ara... (örn: ateş, öksürük, G54, Y12)",
            label_visibility="collapsed",
            key="search_input_field",
        )


def render_case_card(case: dict):
    """
    Kullanıcının kartın her yerine tıklayarak doğrudan sağ çekmeceyi açabileceği
    tam entegre indeks kartı.
    """
    cid = case["id"]
    is_yellow = cid.startswith("Y")
    card_class = "archive-card archive-card-yellow" if is_yellow else "archive-card"
    pill_class = "pill-yellow" if is_yellow else ""
    zone_label = "Sarı Alan" if is_yellow else "Yeşil Alan"
    is_solved = cid in st.session_state.solved_case_ids

    tags = extract_card_tags(case)
    tags_html = "".join([f'<span class="tag-chip">{t}</span>' for t in tags])
    solved_badge = " ✓ Çözüldü" if is_solved else ""
    card_title = f"{case['age']} {case['gender']}"

    # Kart ve tıklama butonu için kapsayıcı container
    with st.container(key=f"card_box_{cid}"):
        st.markdown(
            f"""
            <div class="card-wrapper">
                <div class="{card_class}">
                    <div>
                        <div class="card-top">
                            <div class="card-title">{cid} • {card_title}{solved_badge}</div>
                            <span class="card-category-pill {pill_class}">{zone_label}</span>
                        </div>
                        <div class="card-meta">
                            {case.get('category', 'Klinik Acil')} • 4 Aşama
                        </div>
                        <div class="card-complaint">
                            <b>Şikayet:</b> {case['complaint']}
                        </div>
                    </div>
                    <div>
                        <div class="card-tags">
                            {tags_html}
                        </div>
                        <div class="card-click-hint">
                            <span>📖 İncele & Çöz</span>
                            <span>➔</span>
                        </div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Kartın üzerini tamamen kaplayan şeffaf buton (tüm kart tıklanabilir)
        if st.button(f"Aç_{cid}", key=f"btn_overlay_{cid}", use_container_width=True):
            open_case(cid)
            st.rerun()


def render_drawer(case: dict):
    """
    Ekranın sağına sabitlenmiş (Fixed Viewport) Slide-Over Çekmece.
    Sayfanın neresinde olursanız olun anında sağda açılır; yukarı scroll gerektirmez,
    ana 3 kolonlu ızgara düzenini bozmaz.
    """
    cid = case["id"]
    steps = case["steps"]
    total_steps = len(steps)
    current_idx = st.session_state.drawer_step_idx
    is_yellow = cid.startswith("Y")
    zone_label = "🟡 Sarı Alan (Acil Gözlem)" if is_yellow else "🟢 Yeşil Alan (Poliklinik)"

    # Üst Başlık (Sol) ve Kapat Butonu (Sağ - The Story Archive düzeni)
    title_c, close_c = st.columns([4.2, 1.3])
    with title_c:
        st.markdown(
            f"""
            <div style="font-family:'JetBrains Mono', monospace; font-size:1.22rem; font-weight:800; color:#0f172a; line-height:1.25;">
                {cid} • {case['age']} {case['gender']}
            </div>
            <div style="font-family:'JetBrains Mono', monospace; font-size:0.78rem; color:#64748b; margin-top:3px;">
                {zone_label} • {case.get('category', 'Klinik Acil')}
            </div>
            """,
            unsafe_allow_html=True,
        )
    with close_c:
        if st.button("✕ Kapat", key="btn_close_drawer", use_container_width=True):
            close_case()
            st.rerun()

    st.markdown("<hr style='margin:10px 0 14px 0; border:none; border-top:1.5px solid #1a1a1a;'>", unsafe_allow_html=True)

    # Başvuru Şikayeti
    st.markdown(
        f"""
        <div class="drawer-box">
            <b>Başvuru Şikayeti:</b> {case['complaint']}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # YENİLENEN VİTALLER (SİYAH KUTU KALDIRILDI - KREM/ARŞİV KAĞIT KARTI)
    raw_vitals = get_case_vitals(case)
    vitals_html = annotate_clinical_text(raw_vitals, case["age"])
    vitals_class = "drawer-vitals-card vitals-card-yellow" if is_yellow else "drawer-vitals-card"
    st.markdown(
        f"""
        <div class="{vitals_class}">
            <div class="vitals-header">
                <span>📋 ACİL GELİŞ VİTAL BULGULARI (TRİYAJ KAYDI):</span>
            </div>
            <div>
                {vitals_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Anamnez Öyküsü
    hist_html = annotate_clinical_text(case["history"], case["age"])
    with st.expander("🗣️ Hasta Öyküsü / Anamnez Detayı", expanded=True):
        st.markdown(hist_html, unsafe_allow_html=True)

    # Şimdiye kadar elde edilen klinik bulgular
    if st.session_state.drawer_logs:
        st.markdown("<p style='font-family:JetBrains Mono; font-size:0.78rem; font-weight:700; margin-bottom:6px; color:#475569;'>DOSYA NOTLARI & TETKİK SONUÇLARI:</p>", unsafe_allow_html=True)
        for log in st.session_state.drawer_logs:
            f_html = annotate_clinical_text(log["finding"], case["age"])
            st.markdown(
                f"""
                <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:3px solid #0284c7; border-radius:6px; padding:8px 12px; margin-bottom:8px; font-size:0.86rem; line-height:1.45;">
                    <b>✓ {log['stage']}:</b> {f_html}
                </div>
                """,
                unsafe_allow_html=True,
            )
            if log.get("image") and os.path.exists(log["image"]):
                st.image(log["image"], caption=log.get("image_caption", "Görüntüleme"), use_container_width=True)

    # Vaka Tamamlandı Ekranı
    if current_idx >= total_steps:
        st.session_state.solved_case_ids.add(cid)
        st.markdown(
            f"""
            <div style="background:#ecfdf5; border:1.5px solid #10b981; border-radius:8px; padding:16px; margin-bottom:14px;">
                <h4 style="color:#065f46; margin-top:0;">🎉 Tebrikler! Teşhis ve Tedavi Doğrulandı</h4>
                <p><b>Kesin Tanı:</b> {case['final_diagnosis']}</p>
                <p><b>Taburculuk / Yatış:</b> {case['disposition']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.info(f"**🎓 Klinik İnciler (Case Pearls):**\n\n{case['case_pearl']}")

        if st.button("Arşive Dön", key="btn_completed_close_drawer", use_container_width=True, type="primary"):
            close_case()
            st.rerun()
        return

    # Stepper Göstergesi
    st.markdown(
        f"""
        <div class="drawer-stepper">
            <span class="drawer-stepper-active">AŞAMA {current_idx + 1}/{total_steps}</span>
            <span>•</span>
            <span>{steps[current_idx]['stage_title']}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Yanlış Seçim Detour / Senaryo Güncellemesi
    if st.session_state.drawer_detour is not None:
        detour = st.session_state.drawer_detour
        scen_html = annotate_clinical_text(detour["scenario_update"], case["age"])
        teach_html = annotate_clinical_text(detour["teaching_point"], case["age"])

        st.markdown(
            f"""
            <div class="drawer-alert">
                <div style="font-family:JetBrains Mono; color:#be123c; font-weight:700; font-size:0.8rem; margin-bottom:6px;">
                    ⚠️ KLİNİK SENARYO GÜNCELLEMESİ
                </div>
                <div><b>Seçiminiz:</b> <i>{detour['selected_text']}</i></div>
                <div style="background:#ffffff; border-left:3px solid #f59e0b; padding:8px 10px; margin:8px 0; border-radius:4px;">
                    <b>🔄 Ne Oldu?</b><br>{scen_html}
                </div>
                <div style="background:#eff6ff; border-left:3px solid #3b82f6; padding:8px 10px; margin:8px 0; border-radius:4px;">
                    <b>🎓 Rehber Noktası:</b><br>{teach_html}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("↩️ Kararı Değiştir ve Soruya Dön", key="btn_drawer_return", use_container_width=True, type="primary"):
            st.session_state.drawer_detour = None
            st.rerun()
        return

    # Soru ve Çok Seçenekli Karar
    step = steps[current_idx]
    q_html = annotate_clinical_text(step["question"], case["age"])
    st.markdown(f"**❓ {q_html}**", unsafe_allow_html=True)

    if st.session_state.drawer_last_feedback:
        st.success(f"✓ {st.session_state.drawer_last_feedback}")

    current_opts = st.session_state.drawer_shuffled_opts.get(current_idx, step["options"])
    for idx, opt in enumerate(current_opts):
        letter = chr(65 + idx)
        btn_label = f"[{letter}]  {opt['text']}"
        if st.button(btn_label, key=f"d_opt_{current_idx}_{idx}", use_container_width=True):
            if opt.get("is_correct"):
                st.session_state.drawer_detour = None
                st.session_state.drawer_show_hint = False
                st.session_state.drawer_last_feedback = opt["explanation"]
                if opt.get("new_finding"):
                    st.session_state.drawer_logs.append({
                        "stage": step["stage_title"],
                        "finding": opt["new_finding"],
                        "image": opt.get("image"),
                        "image_caption": opt.get("image_caption", "Tetkik Bulgusu"),
                    })
                st.session_state.drawer_step_idx += 1
                st.rerun()
            else:
                st.session_state.drawer_detour = {
                    "selected_text": opt["text"],
                    "scenario_update": opt["scenario_update"],
                    "teaching_point": opt["teaching_point"],
                }
                st.rerun()

    # İpucu Alanı
    st.write("")
    h_label = "🙈 İpucunu Gizle" if st.session_state.drawer_show_hint else "💡 Klinik İpucu Al"
    if st.button(h_label, key=f"btn_drawer_hint_{current_idx}", use_container_width=True):
        st.session_state.drawer_show_hint = not st.session_state.drawer_show_hint
        st.rerun()

    if st.session_state.drawer_show_hint:
        co = next((o for o in current_opts if o.get("is_correct")), None)
        if co:
            st.info(f"**🎯 Doğru Yaklaşım:** {co['text']}\n\n**Gerekçe:** {co['explanation']}")


def main():
    init_state()
    render_archive_header()

    all_cases = get_all_cases()

    # Filtreleme
    filtered = all_cases
    tab = st.session_state.active_tab
    if tab == "GREEN":
        filtered = [c for c in filtered if c["id"].startswith("G")]
    elif tab == "YELLOW":
        filtered = [c for c in filtered if c["id"].startswith("Y")]

    query = st.session_state.search_query.strip().lower()
    if query:
        filtered = [
            c for c in filtered
            if query in c["id"].lower()
            or query in c.get("complaint", "").lower()
            or query in c.get("age", "").lower()
            or query in c.get("category", "").lower()
        ]

    st.caption(f"Arşivde toplam **{len(filtered)}** vaka listeleniyor.")

    # 3 Kolonlu Sabit Sayfa Gridi (The Story Archive görünümü)
    # Drawer açılsa dahi grid genişliği ve kolonları asla değişmez / bozulmaz!
    cols = st.columns(3)
    for idx, c in enumerate(filtered):
        with cols[idx % 3]:
            render_case_card(c)

    # EĞER ÇEKMECE AÇIKSA:
    # Sayfada nerede olursanız olun ekranın sağına sabitlenen (fixed) çekmece
    drawer_id = st.session_state.selected_case_id
    cases_dict = {c["id"]: c for c in all_cases}

    if drawer_id and drawer_id in cases_dict:
        # Karartıcı / Odaklayıcı Arka Plan
        st.markdown('<div class="story-backdrop"></div>', unsafe_allow_html=True)
        # Sağdan Kayan Sabit Çekmece Konteyneri
        with st.container(key="slide_over_drawer"):
            render_drawer(cases_dict[drawer_id])


if __name__ == "__main__":
    main()
