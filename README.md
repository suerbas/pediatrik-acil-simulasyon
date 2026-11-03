# 📚 Docling RAG Markdown Dönüştürücü (Masaüstü Uygulaması)

Bu uygulama, **"Aile Hekimliğinde Palyatif Bakım"** ve benzeri spesifik alanlardaki klinik protokoller, kılavuzlar ve akademik yayınları (PDF, Word, PPTX, HTML) RAG (Retrieval-Augmented Generation) sistemlerine uygun **Markdown (.md)** formatına dönüştürmek için tasarlanmıştır.

Arka planda IBM'in açık kaynaklı **Docling** kütüphanesini kullanır. Bu sayede:
- İlaç dozaj ve semptom yönetim tabloları bozulmadan Markdown tablolarına (`| İlaç | Doz |`) aktarılır.
- Başlık hiyerarşisi (`#`, `##`, `###`) korunur, böylece RAG metin parçalama (chunking) sırasında bilginin bağlamı kaybolmaz.
- Sayfa numaraları ve altbilgi çöpleri ayıklanır.
- İsteğe bağlı olarak her dosyanın başına kaynak doküman meta bilgisi eklenir.

---

## 🚀 Nasıl Başlatılır?

1. Klasördeki **`baslat.bat`** dosyasına çift tıklayarak doğrudan başlatabilirsiniz.
2. Veya terminalden şu komutu çalıştırabilirsiniz:
   ```bash
   python app.py
   ```

---

## 🛠️ Temel Özellikler

* **Çoklu Dosya & Klasör Seçimi:** PDF, DOCX, PPTX, HTML ve taranmış görüntüleri tek tek veya topluca klasör halinde ekleyebilirsiniz.
* **Sürükle & Bırak (Drag & Drop):** Dosyaları doğrudan pencerenin üzerine bırakabilirsiniz.
* **Donmayan Arayüz (Multi-Threading):** Docling'in yapay zeka modelleri arka planda (`QThread`) çalışır, işlem sırasında masaüstü arayüzü asla donmaz.
* **Çıktı Seçenekleri:** 
  * İster belirlenen bir çıktı klasörüne (`./md_cikti`),
  * İsterseniz her dokümanın orijinal klasörüne `.md` çıktısı kaydedebilirsiniz.
* **Canlı İşlem Günlüğü:** Her dokümanın ayrıştırma sürecini, geçen süreyi ve olası hataları anlık olarak konsoldan takip edebilirsiniz.
