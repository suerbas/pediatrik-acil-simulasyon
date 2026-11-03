import os
import sys
import json
import re
import webbrowser
from pathlib import Path

# Windows OpenMP & PyTorch/PyQt6 DLL çakışma önleyici
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
try:
    import torch
except Exception:
    pass

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QTextBrowser, QComboBox,
    QGroupBox, QListWidget, QSplitter, QProgressBar, QMessageBox,
    QFrame, QSizePolicy
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QIcon, QColor

from rag_engine import PalliativeRAGEngine


class IndexWorker(QThread):
    finished_signal = pyqtSignal(int, int)
    error_signal = pyqtSignal(str)

    def __init__(self, engine: PalliativeRAGEngine):
        super().__init__()
        self.engine = engine

    def run(self):
        try:
            docs, chunks = self.engine.index_markdown_files("md_cikti")
            self.finished_signal.emit(docs, chunks)
        except Exception as e:
            self.error_signal.emit(str(e))


class QueryWorker(QThread):
    response_signal = pyqtSignal(dict)
    error_signal = pyqtSignal(str)

    def __init__(self, engine: PalliativeRAGEngine, question: str):
        super().__init__()
        self.engine = engine
        self.question = question

    def run(self):
        try:
            result = self.engine.ask(self.question)
            self.response_signal.emit(result)
        except Exception as e:
            self.error_signal.emit(str(e))


class PalliativeRAGApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🏥 Aile Hekimliği Palyatif Bakım Klinik Karar Destek Asistanı")
        self.setMinimumSize(1050, 750)

        self.engine = PalliativeRAGEngine()
        self.init_ui()
        self.apply_styles()
        self.refresh_stats()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(14, 14, 14, 14)
        main_layout.setSpacing(10)

        # 1. ÜST PANEL: BAŞLIK & AI SAĞLAYICI AYARLARI
        header_frame = QFrame()
        header_frame.setObjectName("headerFrame")
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(12, 10, 12, 10)

        title_box = QVBoxLayout()
        title_lbl = QLabel("🩺 Palyatif Bakım Klinik Karar Destek Asistanı (RAG)")
        title_lbl.setObjectName("titleLbl")
        subtitle_lbl = QLabel("Sağlık Bakanlığı & Hakemli Tıp Kılavuzlarına Dayalı Kanıta Dayalı Soru-Cevap")
        subtitle_lbl.setObjectName("subtitleLbl")
        title_box.addWidget(title_lbl)
        title_box.addWidget(subtitle_lbl)
        header_layout.addLayout(title_box, 1)

        # AI Sağlayıcı Seçimi & API Key
        prov_box = QHBoxLayout()
        prov_box.setSpacing(8)

        self.lbl_prov = QLabel("AI Beyni:")
        self.combo_provider = QComboBox()
        self.combo_provider.addItems([
            "Google Gemini 3.6 Flash (Önerilen - Ücretsiz)",
            "Google Gemini Flash (En Güncel)",
            "Groq (Llama-3.3-70B - Çok Hızlı)",
            "Yerel Ollama (Lokal AI / Çevrimdışı)"
        ])
        # Mevcut ayarı yükle
        cur_prov = self.engine.config.get("provider", "gemini")
        if cur_prov == "gemini":
            cur_model = self.engine.config.get("gemini_model", "gemini-3.6-flash")
            self.combo_provider.setCurrentIndex(1 if "latest" in cur_model else 0)
        elif cur_prov == "groq":
            self.combo_provider.setCurrentIndex(2)
        elif cur_prov == "ollama":
            self.combo_provider.setCurrentIndex(3)
        self.combo_provider.currentIndexChanged.connect(self.on_provider_changed)

        self.txt_api_key = QLineEdit()
        self.txt_api_key.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_api_key.setPlaceholderText("API Anahtarınızı Yapıştırın...")
        self.txt_api_key.setMaximumWidth(220)

        self.btn_save_key = QPushButton("💾 Kaydet")
        self.btn_save_key.clicked.connect(self.save_api_settings)

        self.btn_get_key = QPushButton("🔑 Ücretsiz Key Al")
        self.btn_get_key.setObjectName("btnGetKey")
        self.btn_get_key.clicked.connect(self.open_get_key_url)

        self.update_api_key_field()

        prov_box.addWidget(self.lbl_prov)
        prov_box.addWidget(self.combo_provider)
        prov_box.addWidget(self.txt_api_key)
        prov_box.addWidget(self.btn_save_key)
        prov_box.addWidget(self.btn_get_key)

        header_layout.addLayout(prov_box)
        main_layout.addWidget(header_frame)

        # 2. ORTA PANEL: SPLITTER (SOL: KÜTÜPHANE / SAĞ: SOHBET & CEVAPLAR)
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # SOL: KILAVUZ KÜTÜPHANESİ
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(8)

        kb_group = QGroupBox("📚 İndekslenmiş Kılavuzlar")
        kb_layout = QVBoxLayout(kb_group)

        self.lbl_stats = QLabel("İndeks Durumu: Yükleniyor...")
        self.lbl_stats.setObjectName("statsLbl")
        kb_layout.addWidget(self.lbl_stats)

        self.doc_list = QListWidget()
        kb_layout.addWidget(self.doc_list)

        self.btn_reindex = QPushButton("🔄 Yeni Markdown'ları İndeksle")
        self.btn_reindex.clicked.connect(self.start_reindex)
        kb_layout.addWidget(self.btn_reindex)

        left_layout.addWidget(kb_group)
        left_widget.setMaximumWidth(280)
        splitter.addWidget(left_widget)

        # SAĞ: SOHBET & KLİNİK SORU-CEVAP
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(8)

        # Hızlı Sorular Çubuğu
        quick_layout = QHBoxLayout()
        quick_layout.setSpacing(6)
        lbl_quick = QLabel("⚡ Hızlı Klinik Sorular:")
        lbl_quick.setStyleSheet("font-weight: bold; color: #475569;")
        quick_layout.addWidget(lbl_quick)

        q1 = QPushButton("💊 Parasetamol & Morfin Dozları")
        q1.clicked.connect(lambda: self.ask_predefined("Çocuk palyatif bakımda parasetamol, ibuprofen ve morfin dozları ve uygulama aralıkları nelerdir?"))
        quick_layout.addWidget(q1)

        q2 = QPushButton("💉 Fentanil Transdermal Geçiş")
        q2.clicked.connect(lambda: self.ask_predefined("Oral morfinden transdermal fentanil flasterine geçiş kuralları ve başlangıç şartları nelerdir?"))
        quick_layout.addWidget(q2)

        q3 = QPushButton("🌬️ Terminal Dispne Yönetimi")
        q3.clicked.connect(lambda: self.ask_predefined("Palyatif bakımda nefes darlığı (dispne) yönetiminde opioid kullanımı ve pozisyonlama önerileri nelerdir?"))
        quick_layout.addWidget(q3)

        quick_layout.addStretch()
        right_layout.addLayout(quick_layout)

        # Sohbet Ekranı (Chat Display)
        self.chat_display = QTextBrowser()
        self.chat_display.setOpenExternalLinks(True)
        right_layout.addWidget(self.chat_display, 1)

        # Alıntılanan Kaynak Kutusu
        self.sources_box = QGroupBox("📌 Yanıtın Alındığı Klinik Kaynak Parçaları (Kanıt Dayanağı)")
        sources_layout = QVBoxLayout(self.sources_box)
        self.sources_display = QTextBrowser()
        self.sources_display.setMaximumHeight(150)
        sources_layout.addWidget(self.sources_display)
        right_layout.addWidget(self.sources_box)

        # İlerleme / Yükleniyor Çubuğu
        self.query_progress = QProgressBar()
        self.query_progress.setRange(0, 0)  # Sonsuz dönen animasyon
        self.query_progress.setVisible(False)
        self.query_progress.setFixedHeight(4)
        right_layout.addWidget(self.query_progress)

        # Soru Giriş Satırı
        input_layout = QHBoxLayout()
        self.txt_query = QLineEdit()
        self.txt_query.setPlaceholderText("Palyatif bakım ile ilgili klinik sorunuzu buraya yazın (Örn: Bası yarası evrelemesi ve pansumanı)...")
        self.txt_query.returnPressed.connect(self.send_query)
        input_layout.addWidget(self.txt_query, 1)

        self.btn_send = QPushButton("🚀 Sor / Gönder")
        self.btn_send.setObjectName("btnSend")
        self.btn_send.clicked.connect(self.send_query)
        input_layout.addWidget(self.btn_send)

        right_layout.addLayout(input_layout)
        splitter.addWidget(right_widget)
        main_layout.addWidget(splitter, 1)

        # 3. ALT BİLGİ & DİSCLAİMER
        footer_layout = QHBoxLayout()
        disclaimer_lbl = QLabel("⚠️ Sorumluluk Reddi: Bu yapay zeka asistanı, sisteme yüklenen Sağlık Bakanlığı ve hakemli tıp kılavuzlarına dayanarak hekime karar desteği sunar. Nihai klinik karar ve uygulama yetkisi sorumlu hekime aittir.")
        disclaimer_lbl.setObjectName("disclaimerLbl")
        footer_layout.addWidget(disclaimer_lbl)
        main_layout.addLayout(footer_layout)

        # Hoşgeldiniz Mesajı
        self.add_assistant_message(
            "Merhaba Doktorum! 🩺\n\n"
            "Ben **Aile Hekimliği Palyatif Bakım Klinik Karar Destek Asistanı**'yım.\n\n"
            "Sol taraftaki kılavuz kütüphanenizde yer alan Sağlık Bakanlığı ve bilimsel yayınlardan derlediğim bilgilerle sorularınızı yanıtlamaya hazırım.\n\n"
            "Yukarıdaki **Hızlı Klinik Sorular** butonlarından birini deneyebilir ya da aklınızdaki spesifik bir tedavi protokolünü aşağıdan doğrudan sorabilirsiniz!"
        )

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8fafc;
            }
            #headerFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0f172a, stop:1 #1e293b);
                border-radius: 8px;
            }
            #titleLbl {
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
            }
            #subtitleLbl {
                color: #94a3b8;
                font-size: 12px;
            }
            #lbl_prov {
                color: #cbd5e1;
                font-weight: bold;
            }
            QPushButton {
                background-color: #ffffff;
                border: 1px solid #cbd5e1;
                border-radius: 6px;
                padding: 6px 12px;
                color: #1e293b;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #f1f5f9;
                border-color: #94a3b8;
            }
            #btnSend {
                background-color: #0284c7;
                color: #ffffff;
                font-weight: bold;
                border: none;
                padding: 8px 18px;
            }
            #btnSend:hover {
                background-color: #0369a1;
            }
            #btnGetKey {
                background-color: #10b981;
                color: #ffffff;
                border: none;
                font-weight: bold;
            }
            #btnGetKey:hover {
                background-color: #059669;
            }
            QGroupBox {
                background-color: #ffffff;
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                margin-top: 8px;
                font-weight: bold;
                color: #1e293b;
                padding: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 4px;
            }
            QTextBrowser {
                background-color: #ffffff;
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                padding: 12px;
                font-size: 13px;
                line-height: 1.5;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #cbd5e1;
                border-radius: 6px;
                padding: 7px 10px;
                font-size: 13px;
            }
            #disclaimerLbl {
                color: #64748b;
                font-size: 11px;
                font-style: italic;
            }
            #statsLbl {
                color: #0369a1;
                font-weight: bold;
                font-size: 12px;
                padding-bottom: 4px;
            }
        """)

    def update_api_key_field(self):
        idx = self.combo_provider.currentIndex()
        if idx in (0, 1):
            key = self.engine.config.get("gemini_api_key", "")
            self.txt_api_key.setText(key)
            self.txt_api_key.setEnabled(True)
            self.btn_get_key.setEnabled(True)
        elif idx == 2:
            key = self.engine.config.get("groq_api_key", "")
            self.txt_api_key.setText(key)
            self.txt_api_key.setEnabled(True)
            self.btn_get_key.setEnabled(True)
        else:
            self.txt_api_key.setText("Yerel Ollama (Key Gerekmez)")
            self.txt_api_key.setEnabled(False)
            self.btn_get_key.setEnabled(False)

    def on_provider_changed(self, idx):
        self.update_api_key_field()

    def save_api_settings(self):
        idx = self.combo_provider.currentIndex()
        new_key = self.txt_api_key.text().strip()

        if idx == 0:
            self.engine.save_config({
                "provider": "gemini",
                "gemini_model": "gemini-3.6-flash",
                "gemini_api_key": new_key
            })
        elif idx == 1:
            self.engine.save_config({
                "provider": "gemini",
                "gemini_model": "gemini-flash-latest",
                "gemini_api_key": new_key
            })
        elif idx == 2:
            self.engine.save_config({
                "provider": "groq",
                "groq_api_key": new_key
            })
        elif idx == 3:
            self.engine.save_config({
                "provider": "ollama"
            })

        QMessageBox.information(self, "Kaydedildi", "AI Sağlayıcı ayarları başarıyla kaydedildi!")

    def open_get_key_url(self):
        idx = self.combo_provider.currentIndex()
        if idx in (0, 1):
            webbrowser.open("https://aistudio.google.com/app/apikey")
        elif idx == 2:
            webbrowser.open("https://console.groq.com/keys")

    def refresh_stats(self):
        stats = self.engine.get_indexed_stats()
        chunks = stats["total_chunks"]
        sources = stats["sources"]

        self.lbl_stats.setText(f"🟢 {len(sources)} Kılavuz ({chunks} Bölüm İndeksli)")
        self.doc_list.clear()
        for s in sources:
            self.doc_list.addItem(f"📄 {s}")

    def start_reindex(self):
        self.btn_reindex.setEnabled(False)
        self.lbl_stats.setText("⏳ Yeni dökümanlar indeksleniyor...")
        self.index_worker = IndexWorker(self.engine)
        self.index_worker.finished_signal.connect(self.on_reindex_finished)
        self.index_worker.error_signal.connect(self.on_reindex_error)
        self.index_worker.start()

    def on_reindex_finished(self, docs, chunks):
        self.btn_reindex.setEnabled(True)
        self.refresh_stats()
        QMessageBox.information(self, "İndeksleme Tamamlandı", f"{docs} dosya ve {chunks} yeni bölüm veritabanına eklendi!")

    def on_reindex_error(self, err):
        self.btn_reindex.setEnabled(True)
        self.refresh_stats()
        QMessageBox.critical(self, "Hata", f"İndeksleme sırasında hata oluştu: {err}")

    def add_user_message(self, text):
        html = f"""
        <div style="margin: 10px 0; text-align: right;">
            <div style="display: inline-block; background-color: #0284c7; color: #ffffff; padding: 8px 14px; border-radius: 12px 12px 2px 12px; max-width: 80%; text-align: left;">
                <b>👨‍⚕️ Siz:</b><br>{text}
            </div>
        </div>
        """
        self.chat_display.append(html)

    def add_assistant_message(self, text):
        lines = text.split('\n')
        html_lines = []
        in_list = False

        for line in lines:
            line_s = line.strip()
            if not line_s:
                if in_list:
                    html_lines.append("</ul>")
                    in_list = False
                html_lines.append("<div style='height: 4px;'></div>")
                continue

            if line_s.startswith("### "):
                if in_list:
                    html_lines.append("</ul>")
                    in_list = False
                title = line_s[4:]
                html_lines.append(f"<h4 style='color:#0284c7; margin:10px 0 4px; font-size:13px;'>{title}</h4>")
            elif line_s.startswith("## "):
                if in_list:
                    html_lines.append("</ul>")
                    in_list = False
                title = line_s[3:]
                html_lines.append(f"<h3 style='color:#0f172a; margin:12px 0 6px; font-size:14px;'>{title}</h3>")
            elif line_s.startswith("# "):
                if in_list:
                    html_lines.append("</ul>")
                    in_list = False
                title = line_s[2:]
                html_lines.append(f"<h2 style='color:#0f172a; margin:14px 0 8px; font-size:15px;'>{title}</h2>")
            elif line_s.startswith("---"):
                if in_list:
                    html_lines.append("</ul>")
                    in_list = False
                html_lines.append("<hr style='border: 0; border-top: 1px solid #e2e8f0; margin: 8px 0;'>")
            elif line_s.startswith("* ") or line_s.startswith("- "):
                if not in_list:
                    html_lines.append("<ul style='margin:4px 0; padding-left:18px;'>")
                    in_list = True
                item_text = line_s[2:]
                item_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', item_text)
                item_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', item_text)
                html_lines.append(f"<li style='margin-bottom: 3px;'>{item_text}</li>")
            else:
                if in_list:
                    html_lines.append("</ul>")
                    in_list = False
                t = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
                t = re.sub(r'\*(.*?)\*', r'<i>\1</i>', t)
                html_lines.append(f"<p style='margin: 3px 0;'>{t}</p>")

        if in_list:
            html_lines.append("</ul>")

        inner_html = "".join(html_lines)
        html = f"""
        <div style="margin: 10px 0; text-align: left;">
            <div style="display: inline-block; background-color: #ffffff; color: #0f172a; padding: 12px 18px; border-radius: 12px 12px 12px 2px; border: 1px solid #cbd5e1; max-width: 95%;">
                <div style="color: #0284c7; font-weight: bold; margin-bottom: 6px;">🩺 Palyatif Karar Destek Asistanı:</div>
                {inner_html}
            </div>
        </div>
        """
        self.chat_display.append(html)
        # Otomatik olarak en aşağı kaydır
        self.chat_display.verticalScrollBar().setValue(self.chat_display.verticalScrollBar().maximum())

    def ask_predefined(self, question):
        self.txt_query.setText(question)
        self.send_query()

    def send_query(self):
        q = self.txt_query.text().strip()
        if not q:
            return

        self.txt_query.clear()
        self.add_user_message(q)

        self.btn_send.setEnabled(False)
        self.query_progress.setVisible(True)

        self.query_worker = QueryWorker(self.engine, q)
        self.query_worker.response_signal.connect(self.on_query_response)
        self.query_worker.error_signal.connect(self.on_query_error)
        self.query_worker.start()

    def on_query_response(self, result):
        self.btn_send.setEnabled(True)
        self.query_progress.setVisible(False)

        answer = result.get("answer", "")
        self.add_assistant_message(answer)

        # Kaynakları göster
        sources = result.get("sources", [])
        src_html = ""
        for i, s in enumerate(sources, 1):
            content_preview = s['content'][:300].replace('\n', ' ')
            src_html += f"<b>[{i}] {s['source']}</b> &gt; <i>{s['header']}</i><br><span style='color:#64748b;'>{content_preview}...</span><br><br>"

        self.sources_display.setHtml(src_html if src_html else "Kaynak bilgisi bulunamadı.")

    def on_query_error(self, err):
        self.btn_send.setEnabled(True)
        self.query_progress.setVisible(False)
        self.add_assistant_message(f"❌ Bir hata oluştu: {err}")


def main():
    app = QApplication(sys.argv)
    window = PalliativeRAGApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
