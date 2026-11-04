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
import urllib.parse
import streamlit as st
import streamlit.components.v1 as components

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
        font-size: 0.68rem;
        font-weight: 700;
        padding: 2.5px 8px;
        border-radius: 12px;
        white-space: nowrap;
        background: #059669;
        border: 1.5px solid #047857;
        color: #ffffff;
        display: inline-block;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }
    .card-category-pill.pill-yellow,
    .pill-yellow {
        background: #facc15 !important;
        border: 1.5px solid #ca8a04 !important;
        color: #000000 !important;
        font-weight: 700 !important;
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

    /* Etiket Çipleri (The Story Archive Tags - Tıklanabilir Keyword Filtresi) */
    .card-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-top: auto;
        padding-top: 8px;
        position: relative !important;
        z-index: 60 !important;
    }
    .tag-chip {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        padding: 2px 8px;
        border-radius: 10px;
        background: #fbf8f3;
        border: 1px solid #d4a373;
        color: #7f4f24 !important;
        text-decoration: none !important;
        display: inline-block;
        position: relative !important;
        z-index: 60 !important;
        cursor: pointer !important;
        transition: all 0.16s ease;
    }
    .tag-chip:hover {
        background: #0f172a !important;
        color: #ffffff !important;
        border-color: #0f172a !important;
        transform: translateY(-1px) scale(1.05);
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
    }


    /* ======================================================== */
    /* 4-KOLONLU SABİT VE EŞİT BOYUTLU KART TASARIMI           */
    /* (The Story Archive Birebir Klonu - %100 Hizalı & Eşit)   */
    /* ======================================================== */
    div[class*="st-key-card_box_"] {
        background: #ffffff !important;
        border: 1.5px solid #059669 !important;
        border-radius: 10px !important;
        padding: 12px 14px 8px 14px !important;
        box-shadow: 1px 2px 0px rgba(0, 0, 0, 0.06) !important;
        margin-bottom: 16px !important;
        position: relative !important;
        height: 236px !important;
        min-height: 236px !important;
        max-height: 236px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        box-sizing: border-box !important;
        transition: transform 0.16s ease, box-shadow 0.16s ease !important;
    }
    div[class*="st-key-card_box_"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 3px 5px 0px rgba(0, 0, 0, 0.12) !important;
    }
    div[class*="st-key-card_box_"]:hover {
        border-color: #047857 !important;
    }
    div[class*="st-key-card_box_yellow_"] {
        border-color: #ca8a04 !important;
    }
    div[class*="st-key-card_box_yellow_"]:hover {
        border-color: #a16207 !important;
    }

    .card-top-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 4px;
    }
    .card-title-text {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.94rem;
        font-weight: 700;
        color: #0f172a;
        line-height: 1.25;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        flex: 1;
        margin-right: 6px;
    }
    .card-category-pill {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.66rem;
        font-weight: 700;
        padding: 2px 7px;
        border-radius: 10px;
        white-space: nowrap;
        background: #059669;
        border: 1.5px solid #047857;
        color: #ffffff;
        display: inline-block;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }
    .card-category-pill.pill-yellow,
    .pill-yellow {
        background: #facc15 !important;
        border: 1.5px solid #ca8a04 !important;
        color: #000000 !important;
        font-weight: 700 !important;
    }
    .card-meta-text {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        color: #64748b;
        margin-bottom: 6px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .card-complaint-text {
        font-size: 0.82rem;
        line-height: 1.38;
        color: #334155;
        height: 42px;
        min-height: 42px;
        max-height: 42px;
        overflow: hidden;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        text-overflow: ellipsis;
    }

    /* Etiket Satırı: Sütunları Doğal Genişliğe ve Sarmaya Ayarlama (Asla metin kesilmez!) */
    div[class*="st-key-card_box_"] div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 4px 5px !important;
        margin-top: 4px !important;
        margin-bottom: 2px !important;
        height: 58px !important;
        min-height: 58px !important;
        max-height: 58px !important;
        overflow: hidden !important;
        width: 100% !important;
        align-content: flex-start !important;
    }
    div[class*="st-key-card_box_"] div[data-testid="stColumn"] {
        flex: 0 0 auto !important;
        width: auto !important;
        min-width: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        height: 24px !important;
    }

    /* Kart İçi Etiket Butonları (The Story Archive Pill Teması) */
    div[class*="st-key-tag_"] {
        margin: 0 !important;
        padding: 0 !important;
        height: 24px !important;
    }
    div[class*="st-key-tag_"] div[data-testid="stButton"] {
        margin: 0 !important;
        padding: 0 !important;
        height: 24px !important;
    }
    div[class*="st-key-tag_"] button {
        background: #fbf8f3 !important;
        border: 1px solid #d4a373 !important;
        color: #7f4f24 !important;
        border-radius: 10px !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.65rem !important;
        font-weight: 500 !important;
        height: 22px !important;
        min-height: 22px !important;
        max-height: 22px !important;
        padding: 0 8px !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: nowrap !important;
        box-shadow: none !important;
        transition: all 0.15s ease !important;
    }
    div[class*="st-key-tag_"] button * {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1 !important;
    }
    div[class*="st-key-tag_"] button p {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 0.65rem !important;
        line-height: 1 !important;
        margin: 0 !important;
        padding: 0 !important;
        color: #7f4f24 !important;
        height: 100% !important;
        transform: translateY(-0.5px) !important;
    }
    div[class*="st-key-tag_"] button:hover {
        background: #0f172a !important;
        border-color: #0f172a !important;
        color: #ffffff !important;
        transform: translateY(-1px) scale(1.03);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15) !important;
    }
    div[class*="st-key-tag_"] button:hover p {
        color: #ffffff !important;
    }

    /* Üst Filtre Sekme Butonları (Yeşil Alan / Sarı Alan Teması) */
    div[class*="st-key-tab_green"] button {
        border: 1.5px solid #059669 !important;
        color: #047857 !important;
    }
    div[class*="st-key-tab_green"] button[kind="primary"],
    div[class*="st-key-tab_green"] button[data-testid="baseButton-primary"] {
        background-color: #059669 !important;
        border: 1.5px solid #047857 !important;
        color: #ffffff !important;
    }
    div[class*="st-key-tab_yellow"] button {
        border: 1.5px solid #ca8a04 !important;
        color: #854d0e !important;
    }
    div[class*="st-key-tab_yellow"] button[kind="primary"],
    div[class*="st-key-tab_yellow"] button[data-testid="baseButton-primary"] {
        background-color: #facc15 !important;
        border: 1.5px solid #ca8a04 !important;
        color: #000000 !important;
    }

    /* Alt İncele & Çöz Butonu (Kartın En Altında Kesikli Çizgiyle Yer Alır) */
    div[class*="st-key-btn_hint_"] {
        margin-top: 4px !important;
        margin-bottom: 0 !important;
    }
    div[class*="st-key-btn_hint_"] button {
        background: transparent !important;
        border: none !important;
        border-top: 1px dashed #e2e8f0 !important;
        border-radius: 0 !important;
        color: #0369a1 !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.70rem !important;
        font-weight: 600 !important;
        height: 26px !important;
        min-height: 26px !important;
        padding: 4px 2px 0 2px !important;
        display: flex !important;
        justify-content: space-between !important;
        box-shadow: none !important;
    }
    div[class*="st-key-btn_hint_"] button:hover {
        background: #f0f9ff !important;
        color: #0284c7 !important;
    }

    /* Kart Üst Gövde Şeffaf Tıklama Alanı (Vaka Açar) */
    div[class*="st-key-btn_overlay_"],
    div[class*="st-key-btn_overlay_"] div[data-testid="stButton"],
    div[class*="st-key-btn_overlay_"] button {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 110px !important;
        z-index: 5 !important;
        margin: 0 !important;
        padding: 0 !important;
        opacity: 0 !important;
        cursor: pointer !important;
        background: transparent !important;
        border: none !important;
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
        overflow-x: hidden !important;
        padding: 24px 22px !important;
        display: flex !important;
        flex-direction: column !important;
        animation: drawerSlideIn 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }

    /* YATAY SCROLLBAR'I VE TAŞMALARI KESİN OLARAK ENGELLEME */
    div[class*="st-key-slide_over_drawer"],
    div[class*="st-key-slide_over_drawer"] div[data-testid="stVerticalBlock"],
    div[class*="st-key-slide_over_drawer"] div[data-testid="stVerticalBlockBorderWrapper"],
    div[class*="st-key-slide_over_drawer"] div[data-testid="element-container"],
    div[class*="st-key-slide_over_drawer"] [data-testid="stExpander"],
    div[class*="st-key-slide_over_drawer"] details {
        overflow-x: hidden !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }
    div[class*="st-key-slide_over_drawer"]::-webkit-scrollbar:horizontal,
    div[class*="st-key-slide_over_drawer"] *::-webkit-scrollbar:horizontal {
        display: none !important;
        height: 0px !important;
        width: 0px !important;
    }
    @keyframes drawerSlideIn {
        from { transform: translateX(100%); }
        to { transform: translateX(0); }
    }
    @keyframes drawerSlideOut {
        from { transform: translateX(0); }
        to { transform: translateX(100%); }
    }
    @keyframes backdropFadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes backdropFadeOut {
        from { opacity: 1; }
        to { opacity: 0; }
    }

    /* Kapanış (Slide-Out Soldan Sağa ve Arka Plan Fade-Out) Animasyon Sınıfları */
    div[class*="st-key-slide_over_drawer"].drawer-slide-out {
        animation: drawerSlideOut 0.3s cubic-bezier(0.32, 0, 0.67, 0) forwards !important;
    }
    div[class*="st-key-backdrop_container"].backdrop-fade-out {
        animation: backdropFadeOut 0.28s ease forwards !important;
    }

    /* Tıklanabilir Karartıcı Arka Plan (Click outside to close) */
    div[class*="st-key-backdrop_container"] {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        background: rgba(0, 0, 0, 0.26) !important;
        backdrop-filter: blur(2.5px) !important;
        z-index: 999980 !important;
        margin: 0 !important;
        padding: 0 !important;
        cursor: pointer !important;
        animation: backdropFadeIn 0.22s ease !important;
    }

    div[class*="st-key-backdrop_container"] div[class*="st-key-btn_backdrop_close"],
    div[class*="st-key-backdrop_container"] div[data-testid="stButton"],
    div[class*="st-key-backdrop_container"] button {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        opacity: 0 !important;
        cursor: pointer !important;
        z-index: 999980 !important;
        margin: 0 !important;
        padding: 0 !important;
        border: none !important;
        background: transparent !important;
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
        position: relative;
    }
    .vitals-chips-container {
        display: flex;
        flex-wrap: wrap;
        gap: 6px 8px;
        align-items: center;
        margin-top: 6px;
    }
    .vital-chip-item {
        display: inline-flex;
        align-items: center;
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

    /* Kibar & Minimalist Dairesel Kapat Butonu (The Story Archive Stili) */
    div[class*="st-key-slide_over_drawer"] div[class*="st-key-btn_close_drawer"] {
        display: flex !important;
        justify-content: flex-end !important;
        align-items: center !important;
    }
    div[class*="st-key-slide_over_drawer"] div[class*="st-key-btn_close_drawer"] div[data-testid="stButton"] {
        width: auto !important;
    }
    div[class*="st-key-slide_over_drawer"] div[class*="st-key-btn_close_drawer"] div[data-testid="stButton"] button {
        width: 32px !important;
        height: 32px !important;
        min-height: 32px !important;
        max-height: 32px !important;
        border-radius: 50% !important;
        border: 1px solid #cbd5e1 !important;
        background: #ffffff !important;
        color: #475569 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 !important;
        margin: 0 0 0 auto !important;
        cursor: pointer !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
        transition: all 0.16s ease !important;
    }
    div[class*="st-key-slide_over_drawer"] div[class*="st-key-btn_close_drawer"] div[data-testid="stButton"] button div,
    div[class*="st-key-slide_over_drawer"] div[class*="st-key-btn_close_drawer"] div[data-testid="stButton"] button span {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
        height: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        text-align: center !important;
    }
    div[class*="st-key-slide_over_drawer"] div[class*="st-key-btn_close_drawer"] div[data-testid="stButton"] button p {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        font-size: 1rem !important;
        font-weight: 400 !important;
        line-height: 1 !important;
        margin: 0 !important;
        padding: 0 !important;
        color: #475569 !important;
        text-align: center !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
    }
    div[class*="st-key-slide_over_drawer"] div[class*="st-key-btn_close_drawer"] div[data-testid="stButton"] button:hover {
        background: #0f172a !important;
        border-color: #0f172a !important;
        color: #ffffff !important;
        transform: scale(1.08) !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15) !important;
    }
    div[class*="st-key-slide_over_drawer"] div[class*="st-key-btn_close_drawer"] div[data-testid="stButton"] button:hover p {
        color: #ffffff !important;
    }

    /* Tooltip Stilleri (Arşiv Kağıdı ile Uyumlu - Asla Kırpılmaz, Asla Taşmaz) */
    .med-val {
        position: relative;
        display: inline-block;
        font-weight: 700;
        padding: 2px 7px;
        margin: 1px 2px;
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
        display: none !important;
        position: absolute !important;
        bottom: calc(100% + 6px) !important;
        left: 0 !important;
        transform: none !important;
        background-color: #0f172a !important;
        color: #f8fafc !important;
        text-align: left !important;
        padding: 6px 12px !important;
        border-radius: 6px !important;
        font-size: 0.78rem !important;
        font-weight: 500 !important;
        max-width: 320px !important;
        white-space: normal !important;
        width: max-content !important;
        box-sizing: border-box !important;
        line-height: 1.35 !important;
        z-index: 9999999 !important;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4) !important;
        pointer-events: none !important;
    }
    .med-val:hover .med-tooltip {
        display: block !important;
        animation: tooltipFadeIn 0.15s ease !important;
    }
    @keyframes tooltipFadeIn {
        from { opacity: 0; transform: translateY(3px); }
        to { opacity: 1; transform: translateY(0); }
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


def get_age_group(age_str: str) -> str:
    age_lower = age_str.lower()
    if "gün" in age_lower or "gun" in age_lower:
        return "Yenidoğan"
    if "hafta" in age_lower:
        m = re.search(r'(\d+)', age_lower)
        if m and int(m.group(1)) <= 4:
            return "Yenidoğan"
        return "Süt Çocuğu"
    if "ay" in age_lower:
        return "Süt Çocuğu"
    m = re.search(r'(\d+(?:\.\d+)?)', age_lower)
    if m:
        val = float(m.group(1))
        if val < 1.0:
            return "Süt Çocuğu"
        elif val < 6.0:
            return "Oyun Çağı"
        elif val < 12.0:
            return "Okul Çocuğu"
        else:
            return "Adölesan"
    return "Pediatrik"


def extract_card_tags(case: dict) -> list:
    """
    Tüm arşiv vakalarındaki ortak klinik noktaları, semptomları ve yaş gruplarını
    kapsamlı bir şekilde tarayarak her vaka için 3-5 adet zengin anahtar kelime üretir.
    """
    tags = [get_age_group(case.get("age", ""))]

    comp = case.get("complaint", "").lower()
    cat = case.get("category", "").lower()
    diag = case.get("final_diagnosis", "").lower()

    # 1. Öncü Klinik Semptomlar (Öncelikli! Kullanıcılar semptomlara tıklar)
    symptom_map = [
        (["ateş", "febril", "sıcaklık"], "Ateş"),
        (["kusma", "regürjit"], "Kusma"),
        (["ishal", "diyare", "dışkılama"], "İshal"),
        (["karın ağrı", "batın ağrı", "kolik"], "Karın Ağrısı"),
        (["öksürük", "boğmaca"], "Öksürük"),
        (["hırıltı", "wheezing", "hışıltı"], "Hırıltı"),
        (["dispne", "nefes darlığı", "solunum sıkıntısı", "takipne", "stridor"], "Dispne"),
        (["döküntü", "kızarıklık", "ürtiker", "peteşi", "purpura", "aft", "yara"], "Döküntü"),
        (["nöbet", "konvülziyon", "kasılma"], "Konvülziyon"),
        (["baş ağrı"], "Baş Ağrısı"),
        (["baş dönmesi", "göz kararması", "senkop", "presenkop", "bayılma"], "Senkop / Baş Dönmesi"),
        (["huzursuz", "ağlama", "katılma"], "Huzursuz Bebek"),
        (["kulak ağrı", "kulak akınt", "otalji"], "Kulak Ağrısı"),
        (["şişlik", "ödem", "lenfaden"], "Ödem"),
        (["sarılık", "ikter"], "Sarılık"),
        (["solukluk", "anemi", "halsizlik"], "Anemi / Solukluk"),
        (["idrar", "işeme", "enürezis", "dizüri"], "Üriner / İdrar"),
        (["kabız", "konstipasyon", "kaka yapamama"], "Konstipasyon"),
        (["zehirlen", "toksik", "intoks", "ilaç alım"], "Zehirlenme"),
        (["travma", "düşme", "çarpma", "burkulma", "kırık"], "Travma"),
        (["dehidrat", "sıvı kaybı", "ağız kuruluğu"], "Dehidratasyon"),
    ]

    for keywords, label in symptom_map:
        if any(k in comp or k in diag for k in keywords):
            if label not in tags:
                tags.append(label)

    # 2. Sistem & Uzmanlık Alanı (GİS, Respiratuar, Enfeksiyon, Nöroloji, vb.)
    system_map = [
        (["gastro", "gi̇s", "apandisit", "invajinasyon", "reflü", "hepat", "karın"], "GİS"),
        (["solunum", "respiratuar", "bronşiolit", "krup", "astım", "pnömoni"], "Respiratuar"),
        (["enfeksiyon", "sepsis", "menenjit", "viral", "bakteriyel"], "Enfeksiyon"),
        (["nöroloj", "epilep", "menenjit", "ensefalit"], "Nöroloji"),
        (["alerji", "anafilaksi", "atopik", "anjioödem"], "Alerji"),
        (["kbb", "otit", "tonsil", "boğaz", "rinit", "farenjit"], "KBB"),
        (["göz", "oftalm", "konjonktiv"], "Göz"),
        (["renal", "ürolo", "nefrit", "piyelonefrit", "torsiyon"], "Nefro / Üro"),
        (["toksik", "zehirlen", "intoks"], "Toksikoloji"),
        (["eklem", "artrit", "sinovit", "ortopedi", "dadı dirseği"], "Ortopedi"),
        (["hematol", "itp", "anemi", "lösemi", "trombosit"], "Hematoloji"),
    ]

    for keywords, label in system_map:
        if any(k in cat or k in diag or k in comp for k in keywords):
            if label not in tags:
                tags.append(label)

    return tags[:5]


def normalize_search_text(text: str) -> str:
    """Türkçe karakterleri ve büyük/küçük harfleri hatasız arama için normalize eder."""
    if not text:
        return ""
    t = text.replace("İ", "i").replace("I", "ı").lower()
    t = t.replace("ğ", "g").replace("ü", "u").replace("ş", "s").replace("ı", "i").replace("ö", "o").replace("ç", "c")
    return t


def build_case_search_corpus(case: dict) -> str:
    """
    Vakanın aranabilir tüm metin havuzunu (vaka kodu, yaş, tanı, şikayet, öykü,
    vitaller, taburculuk/yatış, inci notları, aşama soruları ve seçenekleri) derler.
    Kullanıcı 'yoğun bakım', 'Guillain', 'menenjit', 'aspirin' gibi herhangi bir klinik
    ifade aradığında tüm içeriği kapsar.
    """
    parts = [
        case.get("id", ""),
        case.get("age", ""),
        case.get("gender", ""),
        case.get("category", ""),
        case.get("complaint", ""),
        case.get("history", ""),
        case.get("vitals", ""),
        case.get("final_diagnosis", ""),
        case.get("disposition", ""),
        case.get("case_pearl", ""),
    ]
    parts.extend(extract_card_tags(case))

    for step in case.get("steps", []):
        parts.append(step.get("stage_title", ""))
        parts.append(step.get("question", ""))
        for opt in step.get("options", []):
            parts.append(opt.get("text", ""))
            parts.append(opt.get("explanation", ""))
            parts.append(opt.get("new_finding", ""))
            parts.append(opt.get("scenario_update", ""))
            parts.append(opt.get("teaching_point", ""))

    raw_text = " ".join(p for p in parts if p)
    return normalize_search_text(raw_text)


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



    # Üst Filtre & Arama Satırı: Sekmeler + Serbest Arama Çubuğu + Ara Butonu
    c1, c2, c3, c_search, c_btn = st.columns([1.3, 1.3, 1.3, 4.4, 1.1])
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
    with c_search:
        st.text_input(
            "Arşivde Ara:",
            placeholder="🔍 Tüm arşivde serbest ara (örn: Guillain, yoğun bakım, menenjit, kusma, G14...)",
            label_visibility="collapsed",
            key="search_input_box",
        )
    with c_btn:
        if st.button("🔍 Ara", key="btn_do_search", use_container_width=True, type="primary"):
            st.rerun()


def render_case_card(case: dict):
    cid = case["id"]
    is_yellow = cid.startswith("Y")
    zone_label = "Sarı Alan" if is_yellow else "Yeşil Alan"
    pill_class = "pill-yellow" if is_yellow else ""
    is_solved = cid in st.session_state.solved_case_ids

    tags = extract_card_tags(case)
    solved_badge = " ✓ Çözüldü" if is_solved else ""
    card_title = f"{case['age']} {case['gender']}"
    container_key = f"card_box_yellow_{cid}" if is_yellow else f"card_box_{cid}"

    with st.container(key=container_key):
        # 1. Kart Başlığı, Kategori Rozeti ve Şikayet (Birebir Eşit Yükseklik)
        st.markdown(
            f'''
            <div class="card-top-row">
                <div class="card-title-text" title="{cid} • {card_title}{solved_badge}">
                    {cid} • {card_title}{solved_badge}
                </div>
                <span class="card-category-pill {pill_class}">
                    {zone_label}
                </span>
            </div>
            <div class="card-meta-text" title="{case.get('category', 'Klinik Acil')}">
                {case.get('category', 'Klinik Acil')}
            </div>
            <div class="card-complaint-text" title="{case['complaint']}">
                <b>Şikayet:</b> {case['complaint']}
            </div>
            ''',
            unsafe_allow_html=True,
        )

        # Kart gövdesini kaplayan şeffaf buton (vaka açar)
        if st.button(f"Aç_{cid}", key=f"btn_overlay_{cid}", use_container_width=True):
            open_case(cid)
            st.rerun()

        # 2. Kart İçi Etiket Butonları (Doğal Sarma & Taşma Önleme)
        t_cols = st.columns(len(tags))
        for idx, t in enumerate(tags):
            with t_cols[idx]:
                def make_tag_handler(selected_t=t):
                    st.query_params["tag"] = selected_t

                st.button(t, key=f"tag_{cid}_{idx}", on_click=make_tag_handler, use_container_width=True)

        # 3. Kartın Altındaki Kesikli Çizgili "İncele & Çöz" Butonu
        if st.button("📖 İncele & Çöz ➔", key=f"btn_hint_{cid}", use_container_width=True):
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
    pill_class = "pill-yellow" if is_yellow else ""

    # Üst Başlık (Sol) ve Zarif Kapat Butonu (Sağ - The Story Archive düzeni)
    title_c, close_c = st.columns([5, 0.8])
    with title_c:
        st.markdown(
            f"""
            <div style="font-family:'JetBrains Mono', monospace; font-size:1.22rem; font-weight:800; color:#0f172a; line-height:1.25;">
                {cid} • {case['age']} {case['gender']}
            </div>
            <div style="font-family:'JetBrains Mono', monospace; font-size:0.78rem; color:#64748b; margin-top:5px; display:flex; align-items:center; gap:8px;">
                <span class="card-category-pill {pill_class}">
                    {zone_label}
                </span>
                <span>• {case.get('category', 'Klinik Acil')}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with close_c:
        if st.button("✕", key="btn_close_drawer", help="Kapat (veya sol alana tıkla)"):
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
    cleaned_v = re.sub(r'^(?:Vital Bulgular|Vitalleri|vital bulgular)[:]?\s*', '', raw_vitals, flags=re.IGNORECASE).strip()
    raw_parts = [p.strip().rstrip(',') for p in cleaned_v.split(',') if p.strip()]
    chips = []
    for p in raw_parts:
        chips.append(f'<span class="vital-chip-item">{annotate_clinical_text(p, case["age"])}</span>')
    vitals_chips_html = "".join(chips)
    vitals_class = "drawer-vitals-card vitals-card-yellow" if is_yellow else "drawer-vitals-card"
    st.markdown(
        f"""
        <div class="{vitals_class}">
            <div class="vitals-header">
                <span>📋 ACİL GELİŞ VİTAL BULGULARI (TRİYAJ KAYDI):</span>
            </div>
            <div class="vitals-chips-container">
                {vitals_chips_html}
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

    # 1. Alan Sekmesi Filtresi
    filtered = all_cases
    tab = st.session_state.active_tab
    if tab == "GREEN":
        filtered = [c for c in filtered if c["id"].startswith("G")]
    elif tab == "YELLOW":
        filtered = [c for c in filtered if c["id"].startswith("Y")]

    # 2. Anahtar Kelime Filtresi (Karttaki etiketlere tıklandığında anında devreye girer, arama çubuğunu kirletmez)
    active_tag = st.query_params.get("tag", "").strip()
    if active_tag:
        norm_tag = normalize_search_text(active_tag)
        filtered = [
            c for c in filtered
            if any(norm_tag in normalize_search_text(t) for t in extract_card_tags(c))
            or norm_tag in normalize_search_text(c.get("complaint", ""))
            or norm_tag in normalize_search_text(c.get("final_diagnosis", ""))
            or norm_tag in normalize_search_text(c.get("category", ""))
        ]

    # 3. Serbest Metin Arama Filtresi (Tüm vaka havuzunda derinlemesine arar: Guillain, yoğun bakım, vb.)
    search_query = st.session_state.get("search_input_box", "").strip()
    if search_query:
        norm_q = normalize_search_text(search_query)
        filtered = [
            c for c in filtered
            if norm_q in build_case_search_corpus(c)
        ]

    # 4. Aktif Filtre Rozetleri & Çalışan Temizleme Butonları
    if active_tag or search_query:
        col_badge, col_clear = st.columns([5, 1.4])
        with col_badge:
            pills = []
            if active_tag:
                pills.append(f'<span>🏷️ Etiket: <b style="background:#0f172a; color:#fff; padding:2px 8px; border-radius:10px;">{active_tag}</b></span>')
            if search_query:
                pills.append(f'<span>🔍 Arama: <b style="background:#0369a1; color:#fff; padding:2px 8px; border-radius:10px;">"{search_query}"</b></span>')

            pills_html = " &nbsp;&bull;&nbsp; ".join(pills)
            st.markdown(
                f'''
                <div style="font-family:'JetBrains Mono', monospace; font-size:0.84rem; margin:4px 0 10px 0; display:flex; align-items:center; gap:8px;">
                    {pills_html}
                    <span style="color:#64748b; font-size:0.78rem;">({len(filtered)} vaka eşleşti)</span>
                </div>
                ''',
                unsafe_allow_html=True
            )
        with col_clear:
            def clear_all_filters():
                st.session_state["search_input_box"] = ""
                if "tag" in st.query_params:
                    del st.query_params["tag"]

            st.button("✕ Filtreyi Kaldır", key="btn_clear_filter", on_click=clear_all_filters, use_container_width=True)

    st.caption(f"Arşivde toplam **{len(filtered)}** vaka listeleniyor.")

    # 4 Kolonlu Sabit Sayfa Gridi (The Story Archive orijinal görünümü)
    # Drawer açılsa dahi grid genişliği ve kolonları asla değişmez / bozulmaz!
    cols = st.columns(4)
    for idx, c in enumerate(filtered):
        with cols[idx % 4]:
            render_case_card(c)

    # EĞER ÇEKMECE AÇIKSA:
    # Sayfada nerede olursanız olun ekranın sağına sabitlenen (fixed) çekmece
    drawer_id = st.session_state.selected_case_id
    cases_dict = {c["id"]: c for c in all_cases}

    if drawer_id and drawer_id in cases_dict:
        # Tıklanabilir Karartıcı Arka Plan (Sol alana tıklandığında çekmeceyi kapatır)
        with st.container(key="backdrop_container"):
            if st.button("close_backdrop", key="btn_backdrop_close"):
                close_case()
                st.rerun()

        # Sağdan Kayan Sabit Çekmece Konteyneri
        with st.container(key="slide_over_drawer"):
            render_drawer(cases_dict[drawer_id])

if __name__ == "__main__":
    main()
