# -*- coding: utf-8 -*-
"""
Kalan gerçek tıbbi görüntüleri Wikimedia thumbnail CDN'i üzerinden indiren betik.
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

REMAINING_FILES = {
    # 1. İnvajinasyon Batın USG (Target Sign)
    "usg_intussusception.png": "File:Ultrasound of target sign in intussusception of the right bowel.png",
    # 2. Korneal Abrazyon (Flöresein Boyama)
    "corneal_abrasion.png": "File:Corneal Abrasion with Fluorescein Staining.jpg",
    # 3. Uzun QT EKG Trasesi
    "ecg_long_qtc.png": "File:Ecgqt.png",
    # 4. Yabancı Cisim / Para / Düğme Pil Özofagus Radyografisi
    "adbg_button_battery.png": "File:Coin esophagus.jpg",
    # 5. Geniş QRS / Ventriküler Taşikardi / TKA EKG
    "ecg_tca.png": "File:Electrocardiogram of Ventricular Tachycardia.png"
}


def get_wikimedia_thumb_url(file_title):
    api_url = (
        "https://commons.wikimedia.org/w/api.php?"
        + urllib.parse.urlencode({
            "action": "query",
            "titles": file_title,
            "prop": "imageinfo",
            "iiprop": "url",
            "iiurlwidth": 800,
            "format": "json"
        })
    )
    headers = {
        "User-Agent": "PediatricMedSimEdu/2.0 (medical emergency simulation; contact: suat.pediatri@gmail.com)",
        "Accept": "application/json"
    }
    req = urllib.request.Request(api_url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get("query", {}).get("pages", {})
            for pid, pdata in pages.items():
                if "imageinfo" in pdata and len(pdata["imageinfo"]) > 0:
                    info = pdata["imageinfo"][0]
                    return info.get("thumburl") or info.get("url")
    except Exception as e:
        print(f"API Hatası ({file_title}): {e}")
    return None


def download_and_save(url, dest_path):
    headers = {
        "User-Agent": "PediatricMedSimEdu/2.0 (medical emergency simulation; contact: suat.pediatri@gmail.com)",
        "Referer": "https://commons.wikimedia.org/",
        "Accept": "image/*"
    }
    req = urllib.request.Request(url, headers=headers)
    temp_path = dest_path + ".tmp"
    with urllib.request.urlopen(req, timeout=15) as resp:
        with open(temp_path, "wb") as f:
            f.write(resp.read())

    with Image.open(temp_path) as im:
        rgb_im = im.convert('RGB')
        if rgb_im.width > 900:
            ratio = 900.0 / rgb_im.width
            new_size = (900, int(rgb_im.height * ratio))
            rgb_im = rgb_im.resize(new_size, Image.Resampling.LANCZOS)
        rgb_im.save(dest_path, "PNG", optimize=True)

    if os.path.exists(temp_path):
        os.remove(temp_path)
    print(f"✓ Başarıyla indirildi ve optimize edildi: {os.path.basename(dest_path)}")


def main():
    print("Kalan 5 gerçek tıbbi görsel Wikimedia CDN üzerinden indiriliyor...")
    for target_name, file_title in REMAINING_FILES.items():
        dest = os.path.join(DEST_DIR, target_name)
        print(f"Sorgulanıyor: {file_title} -> {target_name}")
        time.sleep(2)
        thumb_url = get_wikimedia_thumb_url(file_title)
        if thumb_url:
            print(f"İndiriliyor: {thumb_url}")
            try:
                time.sleep(1)
                download_and_save(thumb_url, dest)
            except Exception as e:
                print(f"İndirme başarısız ({target_name}): {e}")
        else:
            print(f"Thumb URL bulunamadı: {file_title}")

    print("\nTüm kalan dosyalar tamamlandı!")


if __name__ == "__main__":
    main()
