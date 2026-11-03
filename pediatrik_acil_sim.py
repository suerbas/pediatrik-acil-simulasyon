# -*- coding: utf-8 -*-
"""
Pediatrik Acil Simülasyon Uygulaması (Yeşil Alan & Sarı Alan)
Öğrenme odaklı, interaktif, dinamik senaryo güncellemeli klinik vaka simülatörü.
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
    page_title="Pediatrik Acil Simülasyonu",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Özel CSS Stilleri (Açık Yeşil ve Açık Sarı Temalar + Modern Kart Tasarımı)
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 2.3rem;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 0.3rem;
    }
    .sub-title {
        text-align: center;
        font-size: 1.1rem;
        color: #475569;
        margin-bottom: 2rem;
    }
    /* Ana Sayfa Seçim Kutuları */
    .green-zone-box {
        background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
        border: 3px solid #22c55e;
        border-radius: 18px;
        padding: 32px 24px;
        text-align: center;
        box-shadow: 0 10px 25px -5px rgba(34, 197, 94, 0.25);
        margin-bottom: 16px;
        min-height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .green-zone-box h2 {
        color: #14532d;
        font-size: 1.8rem;
        font-weight: 800;
        margin-bottom: 12px;
    }
    .green-zone-box p {
        color: #166534;
        font-size: 1.05rem;
        line-height: 1.5;
    }
    .yellow-zone-box {
        background: linear-gradient(135deg, #fef9c3 0%, #fef08a 100%);
        border: 3px solid #eab308;
        border-radius: 18px;
        padding: 32px 24px;
        text-align: center;
        box-shadow: 0 10px 25px -5px rgba(234, 179, 8, 0.25);
        margin-bottom: 16px;
        min-height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .yellow-zone-box h2 {
        color: #713f12;
        font-size: 1.8rem;
        font-weight: 800;
        margin-bottom: 12px;
    }
    .yellow-zone-box p {
        color: #854d0e;
        font-size: 1.05rem;
        line-height: 1.5;
    }
    /* Vaka Başlık Bannerları */
    .banner-green {
        background-color: #dcfce7;
        border-left: 8px solid #16a34a;
        padding: 16px 22px;
        border-radius: 12px;
        color: #14532d;
        margin-bottom: 18px;
    }
    .banner-yellow {
        background-color: #fef9c3;
        border-left: 8px solid #ca8a04;
        padding: 16px 22px;
        border-radius: 12px;
        color: #713f12;
        margin-bottom: 18px;
    }
    .banner-transfer {
        background: linear-gradient(90deg, #dcfce7 0%, #fef08a 50%, #fef9c3 100%);
        border-left: 8px solid #ea580c;
        padding: 16px 22px;
        border-radius: 12px;
        color: #7c2d12;
        margin-bottom: 18px;
        font-weight: 600;
    }
    /* Hasta Kimlik ve Öykü Kartı */
    .patient-card {
        background-color: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 18px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    .patient-badge {
        display: inline-block;
        background-color: #e2e8f0;
        color: #0f172a;
        font-weight: 700;
        padding: 5px 12px;
        border-radius: 8px;
        margin-right: 10px;
        margin-bottom: 8px;
        font-size: 0.95rem;
    }
    /* Dinamik Klinik Güncelleme / Dosya Notları */
    .clinical-log-card {
        background-color: #f0fdf4;
        border: 1px solid #86efac;
        border-radius: 12px;
        padding: 15px 18px;
        margin-bottom: 16px;
        color: #14532d;
    }
    .clinical-log-card-yellow {
        background-color: #fefce8;
        border: 1px solid #fde047;
        border-radius: 12px;
        padding: 15px 18px;
        margin-bottom: 16px;
        color: #713f12;
    }
    /* Soru Kartı */
    .question-box {
        background-color: #ffffff;
        border: 2px solid #94a3b8;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .question-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 8px;
    }
    /* Yanlış Seçim / Senaryo Güncelleme ve Çıkmaz Ekranı */
    .detour-box {
        background-color: #fff1f2;
        border: 2px solid #f43f5e;
        border-radius: 14px;
        padding: 22px;
        margin-top: 12px;
        margin-bottom: 18px;
        color: #881337;
    }
    .scenario-update-box {
        background-color: #fffbeb;
        border-left: 6px solid #f59e0b;
        padding: 15px 18px;
        border-radius: 8px;
        margin-bottom: 14px;
        color: #78350f;
    }
    .teaching-box {
        background-color: #eff6ff;
        border-left: 6px solid #3b82f6;
        padding: 15px 18px;
        border-radius: 8px;
        margin-bottom: 14px;
        color: #1e3a8a;
    }
    iframe[title="scroll-to-top"],
    iframe[title="st.iframe"],
    iframe[title="streamlit.components.v1.html"] {
        position: absolute !important;
        height: 0px !important;
        width: 0px !important;
        border: none !important;
        margin: 0 !important;
        padding: 0 !important;
        visibility: hidden !important;
        pointer-events: none !important;
    }
    div:has(> iframe[title="scroll-to-top"]),
    div:has(> iframe[title="st.iframe"]),
    div:has(> iframe[title="streamlit.components.v1.html"]) {
        height: 0px !important;
        min-height: 0px !important;
        margin: 0 !important;
        padding: 0 !important;
        position: absolute !important;
        visibility: hidden !important;
    }
    /* Klinik Değerler ve İnteraktif Hover Tooltip Rozetleri */
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
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.12);
    }
    .med-val .med-tooltip {
        visibility: hidden;
        opacity: 0;
        position: absolute;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%);
        background-color: #0f172a;
        color: #f8fafc;
        text-align: center;
        padding: 5px 12px;
        border-radius: 6px;
        font-size: 0.86rem;
        font-weight: 500;
        line-height: 1.25;
        white-space: nowrap;
        z-index: 999999;
        box-shadow: 0 8px 20px -3px rgba(0, 0, 0, 0.45);
        pointer-events: none;
        transition: opacity 0.2s ease, transform 0.2s ease;
    }
    .med-val:hover .med-tooltip {
        visibility: visible;
        opacity: 1;
        transform: translateX(-50%) translateY(-3px);
    }
    .med-val .med-tooltip::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -6px;
        border-width: 6px;
        border-style: solid;
        border-color: #0f172a transparent transparent transparent;
    }
    /* Triyaj ve Acil Geliş Vital Bulguları Kartı */
    .triage-vitals-card {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 1.5px solid #cbd5e1;
        border-left: 6px solid #0284c7;
        border-radius: 10px;
        padding: 12px 18px;
        margin-top: 12px;
        margin-bottom: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
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
                    
                    // Önceki tıklanmış butonun focus'unu kaldır (tarayıcının alta kaymasını engeller)
                    if (doc.activeElement && typeof doc.activeElement.blur === 'function') {{
                        doc.activeElement.blur();
                    }}
                    
                    // 1. Üstteki çapa elemente kaydır
                    const anchor = doc.getElementById('page-top-anchor');
                    if (anchor && typeof anchor.scrollIntoView === 'function') {{
                        anchor.scrollIntoView({{ behavior: 'auto', block: 'start' }});
                    }}
                    
                    // 2. Streamlit'in tüm kaydırma konteynırlarını tepeye (0,0) sıfırla
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
            
            // Streamlit re-render ve animasyon gecikmelerine karşı çoklu tetikleme
            scrollToTop();
            setTimeout(scrollToTop, 25);
            setTimeout(scrollToTop, 75);
            setTimeout(scrollToTop, 150);
            setTimeout(scrollToTop, 300);
            setTimeout(scrollToTop, 500);
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

    # Kategori filtresi
    if category and category != "Tüm Semptomlar (Rastgele Vaka)":
        filtered_pool = [c for c in pool if c.get("category") == category]
        if filtered_pool:
            pool = filtered_pool
        else:
            st.toast(f"'{category}' grubunda bu alana ait vaka bulunmadığı için tüm {zone} vakalarından seçildi.", icon="ℹ️")

    available = [c for c in pool if c["id"] not in seen]
    if not available:
        # Havuzdaki tüm vakalar görüldüyse bu havuzu sıfırla
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
    """Ana sayfa: Semptom filtresi, A - Yeşil Alan ve B - Sarı Alan kutuları."""
    st.markdown('<div id="page-top-anchor" style="position:relative;top:0;left:0;width:1px;height:1px;"></div>', unsafe_allow_html=True)
    scroll_to_top()
    st.markdown('<div class="main-title">🩺 Pediatrik Acil Klinik Simülasyon Platformu</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-title">Gerçekçi medikal hasta senaryoları ile adım adım anamnez, muayene, tetkik, triyaj ve tedavi yönetimi (Travma dışı pediatrik aciller)</div>',
        unsafe_allow_html=True,
    )

    # Semptom Kategori Seçici
    cat_col1, cat_col2 = st.columns([3, 1])
    with cat_col1:
        current_cat = st.session_state.get("selected_category", CATEGORIES[0])
        idx = CATEGORIES.index(current_cat) if current_cat in CATEGORIES else 0
        selected = st.selectbox(
            "🎯 Semptom / Klinik Şikayet Grubu Filtresi (Örn: Kulak ağrısı, göz şikayeti, hırıltı, huzursuz bebek):",
            CATEGORIES,
            index=idx,
            key="select_symptom_category",
            help="İstediğiniz bir semptom grubuna odaklanabilir veya tüm vakalar arasından rastgele vaka alabilirsiniz.",
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
            st.info(f"🟢 Yeşil: {len(GREEN_CASES)} | 🟡 Sarı: {len(YELLOW_CASES)}")

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div class="green-zone-box">
                <h2>🟢 A - YEŞİL ALAN SİMÜLASYONU</h2>
                <p>
                    <b>Ayaktan Başvuran Poliklinik / Yeşil Alan Hastaları</b><br><br>
                    Kulak ağrısı, gözde çapaklanma/kızarıklık, hafif hırıltı/öksürük, ağlayan/huzursuz bebek (infantil kolik), döküntü, ateş, kusma ve ishal gibi yakınmalarla başvuran çocuklar.<br><br>
                    <i>Not: Çoğunluğu ayaktan tanı ve tedavi ile taburcu edilir; ancak bazı vakalarda kritik bulgular saptanarak Sarı Alana devir gerekebilir!</i>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("🟢 A - YEŞİL ALAN SİMÜLASYONUNU BAŞLAT", key="btn_home_start_green", use_container_width=True, type="primary"):
            pick_random_case("GREEN", st.session_state.selected_category)
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="yellow-zone-box">
                <h2>🟡 B - SARI ALAN SİMÜLASYONU</h2>
                <p>
                    <b>Acil Gözlem / Sarı Alan Hastaları</b><br><br>
                    Göz kapağında selülit, akut astım atağı, bronşiyolit, toksik yüksek ateş, dirençli kusma/dehidratasyon, nöbet/havale, zehirlenme şüphesi ve emmeyen/huzursuz bebek tabloları.<br><br>
                    <i>Not: Yakın monitörizasyon, hızlı stabilizasyon ve hedefe yönelik tetkik/tedavi gerektirir. Bazı hastalar gözlem sonrası taburcu edilirken bazıları yatış alır.</i>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("🟡 B - SARI ALAN SİMÜLASYONUNU BAŞLAT", key="btn_home_start_yellow", use_container_width=True, type="primary"):
            pick_random_case("YELLOW", st.session_state.selected_category)
            st.rerun()

    st.markdown("---")
    with st.expander("ℹ️ Simülasyon Nasıl Çalışır? (Kısa Rehber)"):
        st.markdown(
            """
            - **Tek Soru ve Çoklu Seçenek:** Her ekranda vakanın o anki aşamasına ait **tek bir klinik soru** ve çoklu seçenekler yer alır.
            - **Dinamik Senaryo Güncellemesi:** Gereksiz bir tahlil istediğinizde veya hatalı bir müdahale seçtiğinizde sistem **senaryoyu o isteminize göre anında günceller** (örneğin istediğiniz gereksiz tetkikin sonucunu veya hastada gelişen durumu gösterir) ve doğrusunun ne olduğunu açıklar.
            - **Öğretici İpucu:** İstediğiniz her aşamada **"💡 Bu Aşamanın Doğru Seçeneğini ve Açıklamasını Gör"** butonuna basarak doğru yaklaşımı öğrenebilirsiniz.
            - **Esnek Navigasyon:** Her sayfada mevcut soruyu/vakayı iptal edip **yeni bir vakaya geçebilir** veya **ana sayfaya dönebilirsiniz**.
            - **Travma Dışı Pediatrik Aciller:** Tüm vakalar pediatrik dahili acillerden derlenmiş olup güncel uluslararası ve ulusal pediatri kılavuzlarına tam uyumludur.
            """
        )


def render_top_navigation():
    """Her vaka sayfasında üstte yer alan kontrol butonları."""
    c1, c2, c3 = st.columns([2, 2, 2])
    with c1:
        if st.button("🏠 Ana Sayfaya Dön", key="top_btn_home", use_container_width=True):
            go_home()
            st.rerun()
    with c2:
        zone_label = "Yeşil Alan" if st.session_state.zone == "GREEN" else "Sarı Alan"
        if st.button(f"🔄 Vakayı İptal Et / Yeni {zone_label} Vakası Al", key="top_btn_new_case", use_container_width=True):
            pick_random_case(st.session_state.zone, st.session_state.get("selected_category"))
            st.rerun()
    with c3:
        other_zone = "YELLOW" if st.session_state.zone == "GREEN" else "GREEN"
        other_label = "🟡 Sarı Alan'a Geç" if other_zone == "YELLOW" else "🟢 Yeşil Alan'a Geç"
        if st.button(other_label, key="top_btn_switch_zone", use_container_width=True):
            pick_random_case(other_zone, st.session_state.get("selected_category"))
            st.rerun()


def render_simulation():
    """Aktif vaka simülasyon ekranını oluşturur."""
    case = st.session_state.current_case
    if not case:
        go_home()
        st.rerun()
        return

    st.markdown('<div id="page-top-anchor" style="position:relative;top:0;left:0;width:1px;height:1px;"></div>', unsafe_allow_html=True)
    scroll_to_top()

    render_top_navigation()

    # Alan Banner'ı
    eff_zone = st.session_state.effective_zone
    steps = case["steps"]
    total_steps = len(steps)
    current_idx = st.session_state.step_idx

    if eff_zone == "GREEN":
        st.markdown(f'<div class="banner-green"><b style="font-size:1.2rem;">🟢 YEŞİL ALAN SİMÜLASYONU</b> &nbsp;|&nbsp; Aşama: <b>{current_idx + 1} / {total_steps}</b></div>', unsafe_allow_html=True)
    elif eff_zone == "YELLOW_TRANSFER":
        st.markdown(f'<div class="banner-transfer"><b style="font-size:1.2rem;">🚨 YEŞİL ALANDAN SARI ALANA DEVREDİLEN HASTA</b> &nbsp;|&nbsp; Sarı Alan Yönetimi Aşama: <b>{current_idx + 1} / {total_steps}</b></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="banner-yellow"><b style="font-size:1.2rem;">🟡 SARI ALAN SİMÜLASYONU</b> &nbsp;|&nbsp; Aşama: <b>{current_idx + 1} / {total_steps}</b></div>', unsafe_allow_html=True)

    # Sabit Hasta Bilgisi Kartı (Yaş, Cinsiyet, Kategori, Başvuru Şikayeti, Triyaj Vitalleri, Kısa Öykü)
    cat_badge = case.get("category", "Genel Acil")
    history_html = annotate_clinical_text(case["history"], case["age"])
    raw_vitals = get_case_vitals(case)
    vitals_html = annotate_clinical_text(raw_vitals, case["age"])

    patient_card_html = (
        f'<div class="patient-card">'
        f'<div>'
        f'<span class="patient-badge">👶 Yaş: {case["age"]}</span>'
        f'<span class="patient-badge">🚻 Cinsiyet: {case["gender"]}</span>'
        f'<span class="patient-badge" style="background-color:#dbeafe; color:#1e40af; border:1px solid #93c5fd;">{cat_badge}</span>'
        f'<span class="patient-badge">📋 Başvuru Şikayeti: {case["complaint"]}</span>'
        f'</div>'
        f'<div class="triage-vitals-card">'
        f'<div style="font-weight:700; color:#0369a1; font-size:0.95rem; margin-bottom:5px;">'
        f'🩺 <b>Acil Triyaj & Geliş Vital Bulguları (Hemşire / Triyaj Kaydı):</b>'
        f'</div>'
        f'<div style="font-size:1.05rem; line-height:1.7;">'
        f'{vitals_html}'
        f'</div>'
        f'</div>'
        f'<div style="margin-top: 10px; font-size: 1.05rem; color: #1e293b; line-height: 1.6;">'
        f'<b>🗣️ Kısa Öykü / Anamnez:</b><br>'
        f'{history_html}'
        f'</div>'
        f'<div style="font-size:0.83rem; color:#64748b; margin-top:10px; border-top:1px dashed #cbd5e1; padding-top:6px;">'
        f'💡 <b>İnteraktif Klinik Değerlendirme:</b> Ölçüm ve laboratuvar verilerinin (KTA, SS, Ateş, SpO2, Kan Gazı, WBC vb.) üzerine mouse ile gelerek yaşa göre <b>Normal / Yüksek / Düşük</b> değerlendirmesini ve referans aralığını inceleyebilirsiniz.'
        f'</div>'
        f'</div>'
    )
    st.markdown(patient_card_html, unsafe_allow_html=True)

    # Şimdiye kadar doğru adımlarla elde edilen klinik bulgular / tetkik sonuçları (Senaryo İlerleyişi)
    if st.session_state.clinical_logs:
        log_css = "clinical-log-card" if eff_zone == "GREEN" else "clinical-log-card-yellow"
        st.markdown(
            f"""
            <div class="{log_css}">
                <b style="font-size:1.05rem;">📂 Hasta Dosyası - Güncel Klinik Bulgular ve İzlem:</b><br><br>
            """,
            unsafe_allow_html=True,
        )
        for item in st.session_state.clinical_logs:
            finding_html = annotate_clinical_text(item["finding"], case["age"])
            st.markdown(f"<b>✓ {item['stage']}:</b> {finding_html}", unsafe_allow_html=True)
            if item.get("image") and os.path.exists(item["image"]):
                st.image(item["image"], caption=item.get("image_caption", "Görüntüleme / Klinik Tetkik"), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Bir önceki doğru adımın açıklaması varsa bilgi olarak göster
    if st.session_state.last_step_feedback:
        st.success(f"**✅ Önceki Adım Değerlendirmesi:** {st.session_state.last_step_feedback}")

    step = steps[current_idx]

    # EĞER KULLANICI YANLIŞ BİR SEÇENEK SEÇTİYSE (SENARYO GÜNCELLEMESİ / ÇIKMAZ EKRANI)
    if st.session_state.active_detour is not None:
        detour = st.session_state.active_detour
        scen_html = annotate_clinical_text(detour["scenario_update"], case["age"])
        teach_html = annotate_clinical_text(detour["teaching_point"], case["age"])
        detour_header_html = (
            f'<div class="detour-box">'
            f'<h4 style="margin-top:0; color:#be123c;">⚠️ Seçiminize Göre Senaryo Güncellemesi ve Klinik Uyarı</h4>'
            f'<p><b>Seçtiğiniz Hamle:</b> {detour["selected_text"]}</p>'
            f'<div class="scenario-update-box">'
            f'<b>🔄 Senaryoda Ne Oldu? (İstem / Müdahale Sonucu):</b><br>'
            f'{scen_html}'
            f'</div>'
        )
        st.markdown(detour_header_html, unsafe_allow_html=True)
        if detour.get("image") and os.path.exists(detour["image"]):
            st.image(detour["image"], caption=detour.get("image_caption", "İstenen Görüntüleme / Tetkik Sonucu"), use_container_width=True)
        detour_teach_html = (
            f'<div class="teaching-box" style="margin-top:10px;">'
            f'<b>🎓 Neden Hatalı / Eksik? Doğru Yaklaşım Nedir?</b><br>'
            f'{teach_html}'
            f'</div>'
            f'</div>'
        )
        st.markdown(detour_teach_html, unsafe_allow_html=True)

        col_d1, col_d2 = st.columns(2)
        with col_d1:
            if st.button("↩️ Anladım, Soruya Dön ve Doğru Yaklaşımı Seç", key="btn_detour_return", use_container_width=True, type="primary"):
                st.session_state.active_detour = None
                st.rerun()
        with col_d2:
            if st.button("💡 Doğru Seçeneği Göstererek Soruya Dön", key="btn_detour_hint", use_container_width=True):
                st.session_state.active_detour = None
                st.session_state.show_hint = True
                st.rerun()
        return

    # AKTİF TEK SORU VE SEÇENEKLER EKRANI
    q_html = annotate_clinical_text(step["question"], case["age"])
    question_box_html = (
        f'<div class="question-box">'
        f'<div style="color:#475569; font-weight:600; font-size:0.95rem; margin-bottom:4px;">'
        f'AŞAMA {current_idx + 1}: {step["stage_title"]}'
        f'</div>'
        f'<div class="question-title">'
        f'❓ {q_html}'
        f'</div>'
        f'</div>'
    )
    st.markdown(question_box_html, unsafe_allow_html=True)

    # İpucu / Doğru Seçeneği Gör Butonu (Her aşamada açık)
    hint_col1, hint_col2 = st.columns([3, 3])
    with hint_col1:
        hint_btn_label = (
            "🙈 Doğru Seçeneği ve Açıklamayı Gizle"
            if st.session_state.show_hint
            else "💡 Bu Aşamanın Doğru Seçeneğini ve Kısa Açıklamasını Gör"
        )
        if st.button(hint_btn_label, key=f"btn_hint_toggle_{current_idx}", use_container_width=True):
            st.session_state.show_hint = not st.session_state.show_hint
            st.rerun()

    if st.session_state.show_hint:
        current_opts = st.session_state.shuffled_options.get(current_idx, step["options"])
        correct_opt = next((o for o in current_opts if o.get("is_correct")), None)
        if correct_opt:
            st.info(
                f"**🎯 Doğru Seçenek:** {correct_opt['text']}\n\n"
                f"**📘 Klinik Açıklama:** {correct_opt['explanation']}"
            )

    st.markdown("### 👇 Seçenekler (Lütfen uygulamak istediğiniz yaklaşımı seçin):")

    current_opts = st.session_state.shuffled_options.get(current_idx, step["options"])
    for idx, opt in enumerate(current_opts):
        btn_label = f"{chr(65 + idx)}) {opt['text']}"
        if st.button(btn_label, key=f"opt_{current_idx}_{idx}", use_container_width=True):
            if opt.get("is_correct"):
                # Doğru seçim!
                st.session_state.active_detour = None
                st.session_state.show_hint = False
                st.session_state.last_step_feedback = opt["explanation"]

                # Varsa bu adımın getirdiği yeni klinik bulguyu hasta dosyasına ekle
                if opt.get("new_finding"):
                    st.session_state.clinical_logs.append(
                        {
                            "stage": step["stage_title"],
                            "finding": opt["new_finding"],
                            "image": opt.get("image"),
                            "image_caption": opt.get("image_caption", "Görüntüleme / Tetkik Bulgusu"),
                        }
                    )

                # Eğer bu adımda hasta Yeşil Alandan Sarı Alana devredildiyse temayı güncelle
                if opt.get("triggers_yellow_transfer"):
                    st.session_state.effective_zone = "YELLOW_TRANSFER"

                # Sonraki adıma geç veya vakayı tamamla
                if current_idx + 1 < total_steps:
                    st.session_state.step_idx += 1
                else:
                    st.session_state.page = "completed"
                st.rerun()
            else:
                # Yanlış seçim! Senaryoyu o isteme göre güncelle ve öğretici çıkmaz ekranını aç
                st.session_state.active_detour = {
                    "selected_text": opt["text"],
                    "scenario_update": opt["scenario_update"],
                    "teaching_point": opt["teaching_point"],
                    "image": opt.get("image"),
                    "image_caption": opt.get("image_caption", "İstenen Görüntüleme / Tetkik"),
                }
                st.rerun()


def render_completed():
    """Vaka başarıyla tamamlandığında gösterilen özet ve tebrik ekranı."""
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
        badge_text = "🚨 Yeşil Alandan Başlayıp Sarı Alana Devredilen Kritik Vaka"
    elif eff_zone == "GREEN":
        badge_text = "🟢 Yeşil Alan Vakası Tamamlandı"
    else:
        badge_text = "🟡 Sarı Alan Vakası Tamamlandı"

    st.balloons()

    completed_card_html = (
        f'<div style="background-color:#ecfdf5; border:3px solid #10b981; border-radius:16px; padding:26px; margin-bottom:20px;">'
        f'<div style="font-weight:700; color:#047857; font-size:1rem; margin-bottom:6px;">{badge_text}</div>'
        f'<h2 style="color:#065f46; margin-top:0;">🎉 Tebrikler! Tanı ve Tedavi Sürecini Doğruladınız</h2>'
        f'<p style="font-size:1.15rem; color:#064e3b;">'
        f'<b>Kesin Tanı:</b> {case["final_diagnosis"]}<br>'
        f'<b>Sonuç / Taburculuk & Yatış Durumu:</b> {case["disposition"]}'
        f'</p>'
        f'</div>'
    )
    st.markdown(completed_card_html, unsafe_allow_html=True)

    if st.session_state.last_step_feedback:
        st.success(f"**✅ Son Aşama Değerlendirmesi:** {st.session_state.last_step_feedback}")

    st.markdown("### 📋 Vaka Boyunca Elde Edilen Klinik Bulgular ve İzlem Özeti")
    for item in st.session_state.clinical_logs:
        finding_html = annotate_clinical_text(item["finding"], case["age"])
        st.markdown(f"- **{item['stage']}:** {finding_html}", unsafe_allow_html=True)
        if item.get("image") and os.path.exists(item["image"]):
            st.image(item["image"], caption=item.get("image_caption", "Görüntüleme / Tetkik Sonucu"), use_container_width=True)

    st.markdown("### 🎓 Vakanın Anahtar Öğrenme Noktaları (Klinik İnciler)")
    st.info(case["case_pearl"])

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        zone_label = "Yeşil Alan" if st.session_state.zone == "GREEN" else "Sarı Alan"
        if st.button(f"▶️ Yeni {zone_label} Vakasına Geç", key="btn_completed_next_case", use_container_width=True, type="primary"):
            pick_random_case(st.session_state.zone, st.session_state.get("selected_category"))
            st.rerun()
    with c2:
        other_zone = "YELLOW" if st.session_state.zone == "GREEN" else "GREEN"
        other_label = "🟡 Sarı Alan Vakası Çöz" if other_zone == "YELLOW" else "🟢 Yeşil Alan Vakası Çöz"
        if st.button(other_label, key="btn_completed_switch_zone", use_container_width=True):
            pick_random_case(other_zone, st.session_state.get("selected_category"))
            st.rerun()
    with c3:
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
