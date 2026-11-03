@echo off
chcp 65001 > nul
echo ========================================================
echo   Pediatrik Acil Vaka Arşivi (The Story Archive Modeli)
echo ========================================================
echo.
python -m streamlit run pediatrik_arsiv_sim.py
pause
