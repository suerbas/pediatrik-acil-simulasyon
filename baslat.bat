@echo off
chcp 65001 > nul
set KMP_DUPLICATE_LIB_OK=TRUE
echo Docling RAG Markdown Donusturucu Baslatiliyor...
python app.py
pause
