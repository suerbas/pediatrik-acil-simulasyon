import os
import sys

# Windows DLL / PyTorch & PyQt6 çakışma çözümü:
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
# Hugging Face ve sistem uyarılarını sessize al (konsol kirliliğini önler)
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
import warnings
warnings.filterwarnings("ignore")
import logging
logging.getLogger("RapidOCR").setLevel(logging.ERROR)
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("docling").setLevel(logging.WARNING)

try:
    import torch
except Exception as _e:
    pass

import time
from pathlib import Path
from datetime import datetime

# Docling imports
try:
    from docling.document_converter import DocumentConverter, PdfFormatOption
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    DOCLING_AVAILABLE = True
except Exception as _e:
    DOCLING_AVAILABLE = False

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QTableWidget, QTableWidgetItem,
    QProgressBar, QTextEdit, QHeaderView, QCheckBox, QGroupBox,
    QMessageBox, QAbstractItemView, QFrame
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QIcon, QColor


SUPPORTED_EXTENSIONS = {'.pdf', '.docx', '.pptx', '.html', '.htm', '.png', '.jpg', '.jpeg'}


class ConversionWorker(QThread):
    """Docling işlemlerini arka planda yürüten iş parçacığı (UI donmasını önler)."""
    file_started = pyqtSignal(int, str)           # row_idx, file_path
    file_finished = pyqtSignal(int, str, str)     # row_idx, status, output_path
    file_failed = pyqtSignal(int, str, str)       # row_idx, error_msg, file_path
    overall_progress = pyqtSignal(int, int)       # current, total
    log_message = pyqtSignal(str, str)            # level (info/success/error), message
    all_finished = pyqtSignal()

    def __init__(self, file_items, output_folder, same_folder_as_source, add_metadata, fast_mode=True):
        super().__init__()
        self.file_items = file_items  # list of (row_idx, file_path)
        self.output_folder = output_folder
        self.same_folder_as_source = same_folder_as_source
        self.add_metadata = add_metadata
        self.fast_mode = fast_mode
        self._is_cancelled = False

    def cancel(self):
        self._is_cancelled = True

    def run(self):
        if not DOCLING_AVAILABLE:
            self.log_message.emit("error", "HATA: 'docling' kütüphanesi sistemde bulunamadı!")
            return

        mode_str = "⚡ Hızlı Mod (OCR Kapalı)" if self.fast_mode else "🔍 Derin Mod (OCR Açık)"
        self.log_message.emit("info", f"Docling motoru hazırlanıyor... [{mode_str}]")
        try:
            pipeline_options = PdfPipelineOptions()
            pipeline_options.do_ocr = not self.fast_mode

            converter = DocumentConverter(
                format_options={
                    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
                }
            )
            self.log_message.emit("success", f"Docling motoru hazır. [{mode_str}]")
        except Exception as e:
            self.log_message.emit("error", f"Docling başlatılırken hata oluştu: {str(e)}")
            return

        total_files = len(self.file_items)
        for i, (row_idx, file_path) in enumerate(self.file_items):
            if self._is_cancelled:
                self.log_message.emit("warning", "İşlem kullanıcı tarafından durduruldu.")
                break

            p = Path(file_path)
            self.file_started.emit(row_idx, file_path)
            self.log_message.emit("info", f"[{i+1}/{total_files}] İşleniyor: {p.name}")
            start_time = time.time()

            try:
                # Hedef klasörü ve dosya adını belirle
                if self.same_folder_as_source:
                    target_dir = p.parent
                else:
                    target_dir = Path(self.output_folder)
                
                target_dir.mkdir(parents=True, exist_ok=True)
                output_file = target_dir / f"{p.stem}.md"

                # Docling ile dönüştür
                conv_res = converter.convert(file_path)
                md_content = conv_res.document.export_to_markdown()

                # İsteğe bağlı RAG meta bilgisi ekle
                if self.add_metadata:
                    header = (
                        f"<!-- RAG METADATA\n"
                        f"Kaynak Dosya: {p.name}\n"
                        f"Orijinal Format: {p.suffix.upper()}\n"
                        f"Dönüştürülme Tarihi: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                        f"-->\n\n"
                        f"# {p.stem}\n\n"
                    )
                    md_content = header + md_content

                # Dosyaya yaz
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(md_content)

                elapsed = round(time.time() - start_time, 1)
                self.file_finished.emit(row_idx, f"Tamamlandı ({elapsed}s)", str(output_file))
                self.log_message.emit("success", f"✓ Başarılı ({elapsed}s): {p.name} -> {output_file.name}")

            except Exception as e:
                err_msg = str(e)
                self.file_failed.emit(row_idx, err_msg, file_path)
                self.log_message.emit("error", f"✗ Hata ({p.name}): {err_msg}")

            self.overall_progress.emit(i + 1, total_files)

        self.all_finished.emit()


class DoclingConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Docling RAG Markdown Dönüştürücü (Palyatif Bakım Doküman Hazırlama)")
        self.setMinimumSize(960, 720)
        self.setAcceptDrops(True)

        self.worker = None
        self.files_to_convert = []  # list of full paths

        # Varsayılan çıktı klasörü
        default_out = Path.cwd() / "md_cikti"
        self.output_dir = str(default_out)

        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)

        # 1. BAŞLIK VE AÇIKLAMA KARTI
        header_frame = QFrame()
        header_frame.setObjectName("headerFrame")
        header_layout = QVBoxLayout(header_frame)
        
        title_label = QLabel("📚 Docling Doküman -> RAG Markdown (.md) Dönüştürücü")
        title_label.setObjectName("titleLabel")
        desc_label = QLabel("PDF, Word (DOCX), PPTX ve HTML dokümanlarını RAG sistemleri için tabloları ve başlık hiyerarşisini koruyarak Markdown formatına çevirir.")
        desc_label.setObjectName("descLabel")
        desc_label.setWordWrap(True)
        
        header_layout.addWidget(title_label)
        header_layout.addWidget(desc_label)
        main_layout.addWidget(header_frame)

        # 2. ÜST BUTONLAR: DOSYA & KLASÖR EKLEME
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)

        self.btn_add_files = QPushButton("📄 Dosya(lar) Ekle")
        self.btn_add_files.clicked.connect(self.add_files_dialog)
        btn_layout.addWidget(self.btn_add_files)

        self.btn_add_folder = QPushButton("📁 Klasör Ekle (Toplu)")
        self.btn_add_folder.clicked.connect(self.add_folder_dialog)
        btn_layout.addWidget(self.btn_add_folder)

        self.btn_remove_selected = QPushButton("🗑️ Seçilenleri Kaldır")
        self.btn_remove_selected.clicked.connect(self.remove_selected)
        btn_layout.addWidget(self.btn_remove_selected)

        self.btn_clear_all = QPushButton("🧹 Listeyi Temizle")
        self.btn_clear_all.clicked.connect(self.clear_all)
        btn_layout.addWidget(self.btn_clear_all)

        btn_layout.addStretch()
        main_layout.addLayout(btn_layout)

        # 3. DOSYA LİSTESİ TABLOSU
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Dosya Adı", "Boyut", "Tür", "Durum"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setAlternatingRowColors(True)
        main_layout.addWidget(self.table)

        # 4. AYARLAR VE HEDEF KLASÖR KUTUSU
        settings_group = QGroupBox("⚙️ Dönüştürme & Çıktı Ayarları")
        settings_layout = QVBoxLayout(settings_group)

        # Hedef klasör satırı
        out_layout = QHBoxLayout()
        self.chk_same_folder = QCheckBox("Dönüştürülen .md dosyasını orijinal dosyanın yanına kaydet")
        self.chk_same_folder.toggled.connect(self.on_same_folder_toggled)
        out_layout.addWidget(self.chk_same_folder)

        self.lbl_target = QLabel(f"<b>Hedef Klasör:</b> {self.output_dir}")
        self.btn_choose_target = QPushButton("📂 Klasör Seç...")
        self.btn_choose_target.clicked.connect(self.choose_output_dir)
        self.btn_open_target = QPushButton("🔍 Klasörü Aç")
        self.btn_open_target.clicked.connect(self.open_output_dir)

        out_layout.addStretch()
        out_layout.addWidget(self.lbl_target)
        out_layout.addWidget(self.btn_choose_target)
        out_layout.addWidget(self.btn_open_target)
        settings_layout.addLayout(out_layout)

        # Ekstra RAG ve Hız ayarları
        opts_layout = QHBoxLayout()
        self.chk_fast_mode = QCheckBox("⚡ Hızlı Mod (OCR'ı kapat - Dijital PDF ve makaleler için 5-10 kat daha hızlı)")
        self.chk_fast_mode.setChecked(True)
        self.chk_fast_mode.setToolTip("Resmi rehberler ve akademik PDF'ler dijital metin içerdiği için OCR gerektirmez. Bu seçenek işlemi muazzam hızlandırır.")
        opts_layout.addWidget(self.chk_fast_mode)

        self.chk_metadata = QCheckBox("RAG Meta Bilgisi Ekle")
        self.chk_metadata.setChecked(True)
        opts_layout.addWidget(self.chk_metadata)
        opts_layout.addStretch()
        settings_layout.addLayout(opts_layout)

        main_layout.addWidget(settings_group)

        # 5. İLERLEME ÇUBUĞU VE DÖNÜŞTÜR BUTONU
        action_layout = QHBoxLayout()
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        action_layout.addWidget(self.progress_bar, 1)

        self.btn_start = QPushButton("🚀 Dönüştürmeyi Başlat")
        self.btn_start.setObjectName("btnStart")
        self.btn_start.clicked.connect(self.start_conversion)
        action_layout.addWidget(self.btn_start)

        self.btn_stop = QPushButton("🛑 Durdur")
        self.btn_stop.setObjectName("btnStop")
        self.btn_stop.setEnabled(False)
        self.btn_stop.clicked.connect(self.stop_conversion)
        action_layout.addWidget(self.btn_stop)

        main_layout.addLayout(action_layout)

        # 6. LOG PANELİ
        log_group = QGroupBox("📋 İşlem Günlüğü (Canlı Log)")
        log_layout = QVBoxLayout(log_group)
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(140)
        log_layout.addWidget(self.log_text)
        main_layout.addWidget(log_group)

        self.log("info", "Uygulama hazır. Dönüştürmek istediğiniz dosyaları seçin veya sürükleyip bırakın.")

    def apply_styles(self):
        """Modern, temiz ve şık arayüz tasarımı."""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8fafc;
            }
            #headerFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0f172a, stop:1 #1e293b);
                border-radius: 8px;
                padding: 12px;
            }
            #titleLabel {
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
            }
            #descLabel {
                color: #94a3b8;
                font-size: 12px;
            }
            QPushButton {
                background-color: #ffffff;
                border: 1px solid #cbd5e1;
                border-radius: 6px;
                padding: 7px 14px;
                font-weight: 500;
                color: #1e293b;
            }
            QPushButton:hover {
                background-color: #f1f5f9;
                border-color: #94a3b8;
            }
            #btnStart {
                background-color: #0284c7;
                color: #ffffff;
                border: none;
                font-weight: bold;
                padding: 8px 22px;
                font-size: 13px;
            }
            #btnStart:hover {
                background-color: #0369a1;
            }
            #btnStop {
                background-color: #ef4444;
                color: #ffffff;
                border: none;
                font-weight: bold;
                padding: 8px 16px;
            }
            #btnStop:hover {
                background-color: #dc2626;
            }
            QTableWidget {
                background-color: #ffffff;
                border: 1px solid #e2e8f0;
                border-radius: 6px;
                gridline-color: #f1f5f9;
            }
            QHeaderView::section {
                background-color: #e2e8f0;
                color: #334155;
                font-weight: bold;
                border: none;
                padding: 6px;
            }
            QGroupBox {
                background-color: #ffffff;
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                margin-top: 10px;
                font-weight: bold;
                color: #1e293b;
                padding: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 4px;
            }
            QProgressBar {
                border: 1px solid #cbd5e1;
                border-radius: 6px;
                text-align: center;
                background-color: #e2e8f0;
                font-weight: bold;
                color: #0f172a;
                height: 26px;
            }
            QProgressBar::chunk {
                background-color: #0ea5e9;
                border-radius: 5px;
            }
            QTextEdit {
                background-color: #0f172a;
                color: #e2e8f0;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 11px;
                border-radius: 6px;
                border: 1px solid #334155;
            }
        """)

    # DRAG & DROP
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        paths = [url.toLocalFile() for url in event.mimeData().urls()]
        self.add_paths(paths)

    def add_paths(self, paths):
        added_count = 0
        for p in paths:
            path_obj = Path(p)
            if path_obj.is_file() and path_obj.suffix.lower() in SUPPORTED_EXTENSIONS:
                if str(path_obj) not in self.files_to_convert:
                    self.append_file_row(path_obj)
                    self.files_to_convert.append(str(path_obj))
                    added_count += 1
            elif path_obj.is_dir():
                for sub in path_obj.rglob('*'):
                    if sub.is_file() and sub.suffix.lower() in SUPPORTED_EXTENSIONS:
                        if str(sub) not in self.files_to_convert:
                            self.append_file_row(sub)
                            self.files_to_convert.append(str(sub))
                            added_count += 1
        if added_count > 0:
            self.log("info", f"{added_count} adet doküman listeye eklendi.")

    def append_file_row(self, path_obj):
        row = self.table.rowCount()
        self.table.insertRow(row)

        name_item = QTableWidgetItem(path_obj.name)
        name_item.setToolTip(str(path_obj))

        try:
            sz_kb = path_obj.stat().st_size / 1024
            size_str = f"{sz_kb:.1f} KB" if sz_kb < 1024 else f"{(sz_kb/1024):.2f} MB"
        except Exception:
            size_str = "-"

        size_item = QTableWidgetItem(size_str)
        ext_item = QTableWidgetItem(path_obj.suffix.upper().replace('.', ''))
        status_item = QTableWidgetItem("Bekliyor")
        status_item.setForeground(QColor("#64748b"))

        self.table.setItem(row, 0, name_item)
        self.table.setItem(row, 1, size_item)
        self.table.setItem(row, 2, ext_item)
        self.table.setItem(row, 3, status_item)

    def add_files_dialog(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Dönüştürülecek Dokümanları Seçin",
            "",
            "Desteklenen Dosyalar (*.pdf *.docx *.pptx *.html *.htm *.png *.jpg *.jpeg);;Tüm Dosyalar (*.*)"
        )
        if files:
            self.add_paths(files)

    def add_folder_dialog(self):
        folder = QFileDialog.getExistingDirectory(self, "Doküman Klasörü Seçin")
        if folder:
            self.add_paths([folder])

    def remove_selected(self):
        selected_rows = sorted(set(idx.row() for idx in self.table.selectedIndexes()), reverse=True)
        for row in selected_rows:
            if row < len(self.files_to_convert):
                del self.files_to_convert[row]
            self.table.removeRow(row)

    def clear_all(self):
        self.table.setRowCount(0)
        self.files_to_convert.clear()
        self.progress_bar.setValue(0)
        self.log("info", "Liste temizlendi.")

    def on_same_folder_toggled(self, checked):
        self.btn_choose_target.setEnabled(not checked)
        self.btn_open_target.setEnabled(not checked)
        if checked:
            self.lbl_target.setText("<b>Hedef Klasör:</b> <i>Her dosyanın kendi klasörü</i>")
        else:
            self.lbl_target.setText(f"<b>Hedef Klasör:</b> {self.output_dir}")

    def choose_output_dir(self):
        folder = QFileDialog.getExistingDirectory(self, "Çıktı Klasörünü Seçin", self.output_dir)
        if folder:
            self.output_dir = folder
            self.lbl_target.setText(f"<b>Hedef Klasör:</b> {self.output_dir}")

    def open_output_dir(self):
        out_path = Path(self.output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
        os.startfile(str(out_path))

    def log(self, level, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        color_map = {
            "info": "#38bdf8",     # Açık mavi
            "success": "#4ade80",  # Açık yeşil
            "warning": "#facc15",  # Sarı
            "error": "#f87171"     # Kırmızı
        }
        color = color_map.get(level, "#e2e8f0")
        html_msg = f"<span style='color:#64748b;'>[{timestamp}]</span> <span style='color:{color};'>{message}</span>"
        self.log_text.append(html_msg)

    def start_conversion(self):
        if not self.files_to_convert:
            QMessageBox.warning(self, "Uyarı", "Lütfen dönüştürmek için en az bir dosya ekleyin!")
            return

        self.btn_start.setEnabled(False)
        self.btn_stop.setEnabled(True)
        self.btn_add_files.setEnabled(False)
        self.btn_add_folder.setEnabled(False)
        self.btn_clear_all.setEnabled(False)
        self.btn_remove_selected.setEnabled(False)

        self.progress_bar.setValue(0)
        items = list(enumerate(self.files_to_convert))

        self.worker = ConversionWorker(
            items,
            self.output_dir,
            self.chk_same_folder.isChecked(),
            self.chk_metadata.isChecked(),
            fast_mode=self.chk_fast_mode.isChecked()
        )
        self.worker.file_started.connect(self.on_file_started)
        self.worker.file_finished.connect(self.on_file_finished)
        self.worker.file_failed.connect(self.on_file_failed)
        self.worker.overall_progress.connect(self.on_overall_progress)
        self.worker.log_message.connect(self.log)
        self.worker.all_finished.connect(self.on_all_finished)

        self.worker.start()

    def stop_conversion(self):
        if self.worker and self.worker.isRunning():
            self.worker.cancel()
            self.btn_stop.setEnabled(False)
            self.log("warning", "Durdurma sinyali gönderildi, mevcut dosya tamamlanınca duracak...")

    def on_file_started(self, row, path):
        item = self.table.item(row, 3)
        if item:
            item.setText("⏳ İşleniyor...")
            item.setForeground(QColor("#0ea5e9"))

    def on_file_finished(self, row, status_text, out_path):
        item = self.table.item(row, 3)
        if item:
            item.setText(f"✓ {status_text}")
            item.setForeground(QColor("#16a34a"))
            item.setToolTip(f"Kaydedildi:\n{out_path}")

    def on_file_failed(self, row, err_msg, path):
        item = self.table.item(row, 3)
        if item:
            item.setText("✗ Hata")
            item.setForeground(QColor("#dc2626"))
            item.setToolTip(f"Hata detayı:\n{err_msg}")

    def on_overall_progress(self, current, total):
        val = int((current / total) * 100)
        self.progress_bar.setValue(val)

    def on_all_finished(self):
        self.btn_start.setEnabled(True)
        self.btn_stop.setEnabled(False)
        self.btn_add_files.setEnabled(True)
        self.btn_add_folder.setEnabled(True)
        self.btn_clear_all.setEnabled(True)
        self.btn_remove_selected.setEnabled(True)
        self.log("success", "Tüm dönüştürme işlemleri tamamlandı!")
        QMessageBox.information(self, "Tamamlandı", "Tüm dokümanlar başarıyla işlendi!")


def main():
    app = QApplication(sys.argv)
    window = DoclingConverterApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
