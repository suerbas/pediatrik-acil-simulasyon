@echo off
chcp 65001 > nul
echo Pediatrik Acil Simülasyonu (Yeşil & Sarı Alan) Başlatılıyor...
python -m streamlit run pediatrik_acil_sim.py
pause
