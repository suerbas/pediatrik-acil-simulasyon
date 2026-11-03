@echo off
chcp 65001 > nul
set KMP_DUPLICATE_LIB_OK=TRUE
echo Palyatif Bakim RAG Asistani Baslatiliyor...
python rag_asistan.py
pause
