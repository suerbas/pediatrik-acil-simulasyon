# -*- coding: utf-8 -*-
"""
cases_v2/ altındaki kaynak vaka dosyalarından uygulamanın okuduğu parça dosyalarını üretir.
  Yeşil alan (Y01…)  -> cases_green_partN.py  (10'ar vaka)  + cases_green.py
  Sarı alan  (S01…)  -> cases_yellow_partN.py (10'ar vaka)  + cases_yellow.py
Var olan parça dosyasının başlık açıklaması (docstring) korunur.
Kullanım: python cases_v2/derle.py
"""
import ast
import importlib.util
import pprint
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
SRC = Path(__file__).resolve().parent

ZONES = {
    "green": {"prefix": "y", "id": "Y", "var": "GREEN_CASES", "title": "Yeşil Alan"},
    "yellow": {"prefix": "s", "id": "S", "var": "YELLOW_CASES", "title": "Sarı Alan"},
}


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CASES


def old_doc(path):
    if not path.exists():
        return None
    try:
        return ast.get_docstring(ast.parse(path.read_text(encoding="utf-8")), clean=False)
    except SyntaxError:
        return None


def build(zone, cfg):
    cases = []
    for f in sorted(SRC.glob(f"{cfg['prefix']}[0-9][0-9]*_{cfg['prefix']}[0-9][0-9]*.py")):
        cases.extend(load(f))
    cases.sort(key=lambda c: int(c["id"][1:]))
    ids = [c["id"] for c in cases]
    expected = [f"{cfg['id']}{i:02d}" for i in range(1, len(cases) + 1)]
    if ids != expected:
        raise SystemExit(f"{zone}: kimlikler ardışık değil: {sorted(set(expected) ^ set(ids))}")

    parts = [cases[i : i + 10] for i in range(0, len(cases), 10)]
    for n, chunk in enumerate(parts, 1):
        path = ROOT / f"cases_{zone}_part{n}.py"
        doc = old_doc(path)
        rng = f"{chunk[0]['id']} - {chunk[-1]['id']}"
        if not doc or rng not in doc:
            doc = f"\nPediatrik Acil Simülasyonu - {cfg['title']} Vakaları (Part {n}: {rng})\n"
        body = pprint.pformat(chunk, width=120, sort_dicts=False)
        path.write_text(
            f'# -*- coding: utf-8 -*-\n"""{doc}"""\n\n{cfg["var"]}_PART{n} = {body}\n', encoding="utf-8"
        )

    # Artık kullanılmayan fazla parça dosyalarını kaldır.
    n = len(parts) + 1
    while (ROOT / f"cases_{zone}_part{n}.py").exists():
        (ROOT / f"cases_{zone}_part{n}.py").unlink()
        n += 1

    imports = "\n".join(
        f"from cases_{zone}_part{i} import {cfg['var']}_PART{i}" for i in range(1, len(parts) + 1)
    )
    joined = "\n    + ".join(f"{cfg['var']}_PART{i}" for i in range(1, len(parts) + 1))
    (ROOT / f"cases_{zone}.py").write_text(
        f'# -*- coding: utf-8 -*-\n"""\n{cfg["title"]} Simülasyon Vakaları ({len(cases)} Vaka)\n'
        "Bu dosya cases_v2/derle.py tarafından üretilir; vakaları cases_v2/ altında düzenleyin.\n"
        f'"""\n\n{imports}\n\n{cfg["var"]} = (\n    {joined}\n)\n',
        encoding="utf-8",
    )
    print(f"{zone}: {len(cases)} vaka, {len(parts)} parça")


if __name__ == "__main__":
    for zone, cfg in ZONES.items():
        build(zone, cfg)
