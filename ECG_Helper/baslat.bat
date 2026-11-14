@echo off
chcp 65001 > nul
echo ========================================================
echo   ECG_Helper — FastAPI + React EKG Klinik Karar Destek
echo ========================================================
echo.
echo [1/2] FastAPI Backend baslatiliyor (http://127.0.0.1:8000)...
start "ECG_Helper Backend (FastAPI)" cmd /k "cd /d "%~dp0backend" && python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload"

timeout /t 2 /nobreak > nul

echo [2/2] React Frontend baslatiliyor (http://localhost:5173)...
start "ECG_Helper Frontend (Vite)" cmd /k "cd /d "%~dp0frontend" && npm run dev"

timeout /t 3 /nobreak > nul
start "" http://localhost:5173

echo.
echo Her iki servis baslatildi. Tarayicinizda http://localhost:5173 acilacaktir.
pause
