# -*- coding: utf-8 -*-
"""
Vaka dosyasındaki seçenek sırasını vaka/adım kimliğine bağlı deterministik olarak karıştırır
ve dosyayı tek tip biçimde yeniden yazar.
Kullanım: python cases_v2/karistir.py <dosya.py> [<dosya2.py> ...]
"""
import importlib.util
import json
import random
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")


def load(path):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CASES, (mod.__doc__ or "").strip()


def shuffle_options(cases):
    for c in cases:
        # Doğru seçenek tüm adımlarda aynı konuma düşerse farklı tohumla yeniden karıştır
        for salt in range(20):
            for s_idx, step in enumerate(c["steps"]):
                rng = random.Random(f"{c['id']}-{s_idx}-{salt}")
                rng.shuffle(step["options"])
            correct_idx = {
                next(i for i, o in enumerate(step["options"]) if o.get("is_correct"))
                for step in c["steps"]
            }
            if len(correct_idx) > 1:
                break


def dump(cases, doc):
    body = json.dumps(cases, ensure_ascii=False, indent=4)
    body = re.sub(r'": true\b', '": True', body)
    body = re.sub(r'": false\b', '": False', body)
    return f'# -*- coding: utf-8 -*-\n"""\n{doc}\n"""\n\nCASES = {body}\n'


if __name__ == "__main__":
    for path in sys.argv[1:]:
        cases, doc = load(path)
        shuffle_options(cases)
        with open(path, "w", encoding="utf-8") as f:
            f.write(dump(cases, doc))
        print(f"{path}: {len(cases)} vaka karıştırıldı")
