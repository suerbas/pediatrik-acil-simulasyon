# -*- coding: utf-8 -*-
"""
Wikimedia Commons'tan gerçek, anonim, telifsiz / açık lisanslı tıbbi radyoloji,
ultrasonografi, EKG ve klinik fotoğrafları indiren betik.
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

DEST_DIR = os.path.join(os.path.dirname(__file__), 'assets', 'images')
os.makedirs(DEST_DIR, exist_ok=True)

# Wikimedia Commons Dosya Adı -> Yerel Dosya Adı Eşleştirmesi
COMMONS_FILES = {
    # 1. Lober Pnömoni (Konsolidasyon) PA Akciğer Grafisi
    "cxr_lobar_pneumonia.png": [
        "File:X-ray of lobar pneumonia.jpg",
        "File:RLL pneumoniaM.jpg",
        "File:Pneumonia x ray.jpg"
    ],
    # 2. Plevral Efüzyon / Küntleşme PA Akciğer Grafisi
    "cxr_pleural_effusion.png": [
        "File:Pleural effusion.jpg",
        "File:Effusionhalf.PNG"
    ],
    # 3. Pnömotoraks PA Akciğer Grafisi
    "cxr_pneumothorax.png": [
        "File:Pneumothorax CXR.jpg",
        "File:Chest X-ray of pneumothorax.png",
        "File:Pneumothorax.jpg"
    ],
    # 4. Atipik / Bronkopnömoni PA Akciğer Grafisi
    "cxr_atypical_pneumonia.png": [
        "File:X-ray of bronchopneumonia.png",
        "File:Pneumonia x ray.jpg"
    ],
    # 5. Normal Akciğer Grafisi
    "cxr_normal.png": [
        "File:Normal PA chest X-ray.jpg",
        "File:Chest Xray PA 3-8-2010.png",
        "File:Chest X-ray.jpg"
    ],
    # 6. ADBG: İleus ve Hava-Sıvı Seviyeleri
    "adbg_air_fluid.png": [
        "File:Upright X-ray demonstrating small bowel obstruction.jpg",
        "File:Small bowel obstruction.jpg",
        "File:LargeBowelObsUp2008.jpg"
    ],
    # 7. ADBG: Masif Fekal İmpaksiyon / Kolon Doluluğu
    "adbg_fecal_impaction.png": [
        "File:Severe fecal impaction.jpg",
        "File:Fecal impaction x-ray.jpg",
        "File:LargeBowelObsUp2008.jpg",
        "File:Constipation xray.jpg"
    ],
    # 8. Krup: Steeple Sign (Subglottik Sivrilme) AP Boyun Grafisi
    "neck_steeple_sign.png": [
        "File:Croup steeple sign.jpg",
        "File:Steeple sign croup.jpg"
    ],
    # 9. Retrofarengeal Abse: Lateral Boyun Grafisi
    "neck_retropharyngeal.png": [
        "File:Retroabscess10.JPG",
        "File:Retropharyngeal abscess x ray.jpg"
    ],
    # 10. İnvajinasyon: Batın USG Target Sign (Konsantrik Halkalar)
    "usg_intussusception.png": [
        "File:Ultrasound of target sign in intussusception of the right bowel.png",
        "File:Ultrasound of target sign in intussusception.jpg",
        "File:Ultrasound of pseudokidney sign in intussusception.jpg"
    ],
    # 11. Akut Apandisit: Batın USG
    "usg_appendicitis.png": [
        "File:Appendicitis ultrasound.png",
        "File:Appendicitis US.jpg"
    ],
    # 12. Korneal Abrazyon: Flöresein Boyama
    "corneal_abrasion.png": [
        "File:Corneal Abrasion with Fluorescein Staining.jpg",
        "File:Human cornea with abrasion highlighted by fluorescein staining.jpg"
    ],
    # 13. SVT: Supraventriküler Taşikardi EKG Trasesi
    "ecg_svt.png": [
        "File:SVT Lead II-2.JPG",
        "File:SVT Lead II.jpg",
        "File:Supraventricular tachycardia ECG.png"
    ],
    # 14. Normal EKG
    "ecg_normal.png": [
        "File:Normal ECG with 12 leads.jpg",
        "File:Normal ECG 17yrs old.jpg"
    ],
    # 15. Uzun QT EKG
    "ecg_long_qtc.png": [
        "File:Ecgqt.png",
        "File:Long QT subtypes.jpg"
    ],
    # 16. Düğme Pil Radyografisi (Halo / Çift Halka)
    "adbg_button_battery.png": [
        "File:Button battery ingestion.jpg",
        "File:Foreign body x ray.jpg",
        "File:Button battery halo sign.jpg"
    ],
    # 17. TKA / Geniş QRS EKG
    "ecg_tca.png": [
        "File:TCA toxicity ECG.jpg",
        "File:Wide QRS tachycardia.jpg",
        "File:Ventricular tachycardia ECG.jpg"
    ]
}


def get_wikimedia_image_url(file_title):
    """MediaWiki API'sini sorgulayarak doğrudan indirme bağlantısını alır."""
    api_url = (
        "https://commons.wikimedia.org/w/api.php?"
        + urllib.parse.urlencode({
            "action": "query",
            "titles": file_title,
            "prop": "imageinfo",
            "iiprop": "url",
            "format": "json"
        })
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json"
    }
    req = urllib.request.Request(api_url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get("query", {}).get("pages", {})
            for pid, pdata in pages.items():
                if "imageinfo" in pdata and len(pdata["imageinfo"]) > 0:
                    raw_url = pdata["imageinfo"][0]["url"]
                    # Strip query parameters if any
                    clean_url = raw_url.split("?")[0]
                    return clean_url
    except Exception as e:
        print(f"Hata ({file_title}): {e}")
    return None


def download_and_optimize(url, dest_path):
    """Verilen URL'den görseli indirir, optimize eder ve PNG olarak kaydeder."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://commons.wikimedia.org/",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8"
    }
    req = urllib.request.Request(url, headers=headers)
    temp_path = dest_path + ".tmp"
    with urllib.request.urlopen(req, timeout=15) as resp:
        with open(temp_path, "wb") as f:
            f.write(resp.read())

    # PIL ile aç ve standart boyutta PNG olarak dönüştür
    with Image.open(temp_path) as im:
        rgb_im = im.convert('RGB')
        # Çok büyükse en fazla 1000px genişliğe küçült
        if rgb_im.width > 1000:
            ratio = 1000.0 / rgb_im.width
            new_size = (1000, int(rgb_im.height * ratio))
            rgb_im = rgb_im.resize(new_size, Image.Resampling.LANCZOS)
        rgb_im.save(dest_path, "PNG", optimize=True)

    if os.path.exists(temp_path):
        os.remove(temp_path)
    print(f"✓ Başarıyla indirildi ve kaydedildi: {os.path.basename(dest_path)}")


def main():
    print("Gerçek tıbbi görüntüler Wikimedia Commons arşivinden taranıyor...")
    success_count = 0
    # İndirilmiş olanları kontrol et ve kalanları 2.5 sn bekleyerek indir
    ALREADY_DONE = {
        "cxr_lobar_pneumonia.png",
        "cxr_pleural_effusion.png",
        "cxr_pneumothorax.png",
        "cxr_atypical_pneumonia.png",
        "adbg_fecal_impaction.png"
    }

    for target_name, candidates in COMMONS_FILES.items():
        dest = os.path.join(DEST_DIR, target_name)
        if target_name in ALREADY_DONE and os.path.exists(dest) and os.path.getsize(dest) > 20000:
            print(f"⏩ {target_name} zaten gerçek tıbbi görüntü olarak mevcut, atlanıyor.")
            success_count += 1
            continue

        downloaded = False
        for title in candidates:
            print(f"Sorgulanıyor: {title} -> {target_name}")
            time.sleep(2.5)  # Rate limit koruması
            direct_url = get_wikimedia_image_url(title)
            if direct_url:
                print(f"Bağlantı bulundu: {direct_url}")
                try:
                    time.sleep(1.5)
                    download_and_optimize(direct_url, dest)
                    downloaded = True
                    success_count += 1
                    break
                except Exception as ex:
                    print(f"İndirme hatası: {ex}")
        if not downloaded:
            print(f"⚠️ {target_name} için uygun görsel bulunamadı veya indirilemedi.")

    print(f"\nİşlem tamamlandı! {success_count}/{len(COMMONS_FILES)} gerçek tıbbi görüntü arşivlendi.")


if __name__ == "__main__":
    main()
