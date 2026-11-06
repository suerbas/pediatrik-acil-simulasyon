# -*- coding: utf-8 -*-
"""
Python vaka dosyalarını (cases_green/cases_yellow) web uygulamasının okuyacağı
JSON'a dönüştürür. Vakaların tek doğru kaynağı Python part dosyalarıdır; vaka
değiştiğinde bu betik yeniden çalıştırılır:

    python web/scripts/export_cases.py

Çıktılar:
    web/src/data/index.json      -> kart listesi (pakete gömülür)
    web/public/search.json       -> arama havuzu (ilk aramada indirilir)
    web/public/cases/<ID>.json   -> vaka detayı (vaka açılınca indirilir)
    web/public/assets/images/    -> görüntüleme dosyaları
"""

import json
import os
import re
import shutil
import sys
import warnings

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
WEB = os.path.join(ROOT, "web")
sys.path.insert(0, ROOT)

warnings.filterwarnings("ignore")
import logging  # noqa: E402

logging.disable(logging.CRITICAL)

from cases_green import GREEN_CASES  # noqa: E402
from cases_yellow import YELLOW_CASES  # noqa: E402
from pediatric_evaluator import annotate_clinical_text, get_case_vitals  # noqa: E402

# Etiket ve arama mantığı Streamlit arşiviyle birebir aynı kalsın diye oradan alınır.
import pediatrik_arsiv_sim as arsiv  # noqa: E402

VITALS_PREFIX = re.compile(r"^(?:Vital Bulgular|Vitalleri|vital bulgular)[:]?\s*", re.IGNORECASE)


def vitals_chips(case: dict) -> list:
    cleaned = VITALS_PREFIX.sub("", get_case_vitals(case)).strip()
    parts = [p.strip().rstrip(",") for p in cleaned.split(",") if p.strip()]
    return [annotate_clinical_text(p, case["age"]) for p in parts]


def export_case(case: dict) -> dict:
    age = case["age"]
    steps = []
    for step in case["steps"]:
        options = []
        for opt in step["options"]:
            if opt.get("is_correct"):
                o = {
                    "text": opt["text"],
                    "correct": True,
                    "explanation": opt.get("explanation", ""),
                    "finding": annotate_clinical_text(opt.get("new_finding", ""), age),
                }
                if opt.get("image"):
                    o["image"] = opt["image"]
                    o["imageCaption"] = opt.get("image_caption", "Tetkik Bulgusu")
            else:
                o = {
                    "text": opt["text"],
                    "correct": False,
                    "scenario": annotate_clinical_text(opt.get("scenario_update", ""), age),
                    "teaching": annotate_clinical_text(opt.get("teaching_point", ""), age),
                }
            options.append(o)
        steps.append({
            "title": step["stage_title"],
            "question": annotate_clinical_text(step["question"], age),
            "options": options,
        })
    return {
        "id": case["id"],
        "zone": "yellow" if case["id"].startswith("Y") else "green",
        "age": age,
        "gender": case["gender"],
        "category": case["category"],
        "complaint": case["complaint"],
        "history": annotate_clinical_text(case["history"], age),
        "vitals": vitals_chips(case),
        "diagnosis": case["final_diagnosis"],
        "disposition": case["disposition"],
        "pearl": case["case_pearl"],
        "steps": steps,
    }


def main():
    all_cases = GREEN_CASES + YELLOW_CASES
    ids = [c["id"] for c in all_cases]
    assert len(ids) == len(set(ids)), "Yinelenen vaka kimliği var"

    cases_dir = os.path.join(WEB, "public", "cases")
    shutil.rmtree(cases_dir, ignore_errors=True)
    os.makedirs(cases_dir)
    os.makedirs(os.path.join(WEB, "src", "data"), exist_ok=True)

    index = []
    search = {}
    for case in all_cases:
        with open(os.path.join(cases_dir, f"{case['id']}.json"), "w", encoding="utf-8") as f:
            json.dump(export_case(case), f, ensure_ascii=False, separators=(",", ":"))
        index.append({
            "id": case["id"],
            "zone": "yellow" if case["id"].startswith("Y") else "green",
            "age": case["age"],
            "gender": case["gender"],
            "category": case["category"],
            "complaint": case["complaint"],
            "tags": arsiv.extract_card_tags(case),
        })
        search[case["id"]] = arsiv.build_case_search_corpus(case)

    with open(os.path.join(WEB, "src", "data", "index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(WEB, "public", "search.json"), "w", encoding="utf-8") as f:
        json.dump(search, f, ensure_ascii=False, separators=(",", ":"))

    img_src = os.path.join(ROOT, "assets", "images")
    img_dst = os.path.join(WEB, "public", "assets", "images")
    shutil.rmtree(img_dst, ignore_errors=True)
    shutil.copytree(img_src, img_dst)

    print(f"{len(index)} vaka dışa aktarıldı -> web/src/data/index.json, web/public/cases/")


if __name__ == "__main__":
    main()
