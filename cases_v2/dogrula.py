# -*- coding: utf-8 -*-
"""
Vaka doğrulama betiği (v2).
Kullanım: python cases_v2/dogrula.py <dosya_yolu>
"""
import importlib.util
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

REQUIRED_CASE_KEYS = {
    "id",
    "category",
    "age",
    "gender",
    "complaint",
    "history",
    "final_diagnosis",
    "disposition",
    "case_pearl",
    "steps",
}

SPOILER_KEYWORDS_BY_ID = {
    "G01": ["nazofarenjit", "soğuk algınlığı", "nezle"],
    "G02": ["streptokok", "agbhs", "centor", "mcisaac", "strep-a", "strep a"],
    "G03": ["otitis media", "aom", "orta kulak iltihabı"],
    "G04": ["gastroenterit", "age"],
    "G05": ["fonksiyonel kabızlık", "konstipasyon", "roma iv", "hirschsprung"],
    "G06": ["ürtiker", "kurdeşen"],
    "G07": ["eritema infeksiyozum", "beşinci hastalık", "5. hastalık", "parvovirus", "tokatlanmış"],
    "G08": ["roseola", "altıncı hastalık", "6. hastalık", "ekzantema subitum", "hhv-6", "hhv6", "nagayama"],
    "G09": ["el-ayak-ağız", "el ayak ağız", "coxsackie", "enterovirus", "enteroviral"],
    "G10": ["alerjik rinit", "postnazal akıntı sendromu", "üst hava yolu öksürük sendromu"],
    "G11": ["infantil kolik", "wessel", "3'ler kuralı", "üçler kuralı"],
    "G12": ["ortostatik hipotansiyon", "vazovagal"],
    "G13": ["krup", "laringotrakeit", "westley"],
    "G14": ["suçiçeği", "varisella", "vzv"],
    "G15": ["konjonktivit", "adenoviral", "adenovirus"],
    "G16": ["impetigo", "ssss", "haşlanmış deri"],
    "G17": ["apandisit", "mcburney", "rovsing", "apendiks", "apendikolit"],
    "G18": ["meningokok", "meningokoksemi", "waterhouse"],
    "G19": ["bronşiolit", "bronşiyolit"],
    "G20": ["anafilaksi", "anafilaktik"],
    "G21": ["demir eksikliği", "ferritin", "mikrositer"],
    "G22": ["aft", "aftöz", "stomatit"],
    "G23": ["pitriyazis", "rozea", "herald patch", "madalyon"],
    "G24": ["molluskum", "molluscum", "kontagiozum"],
    "G25": ["bebek bezi dermatiti", "diaper", "kandida", "kandidiyazis", "satellit"],
    "G26": ["enürezis", "noktürnal"],
    "G27": ["kıl kurdu", "enterobiyazis", "oksiyüriyazis", "selofan"],
    "G28": ["reflü", "happy spitter", "gastroözofageal"],
    "G29": ["efüzyonlu", "seröz otit", "som"],
    "G30": ["reaktif lenfadenit", "reaktif lenfadenopati"],
    "G31": ["mikoplazma", "mycoplasma", "atipik pnömoni"],
    "G32": ["alerjik konjonktivit", "vernal"],
    "G33": ["dakriyostenoz", "nazolakrimal", "kanal tıkanıklığı"],
    "G34": ["korneal abrazyon", "abrazyon", "flöresein"],
    "G35": ["miyoklonus", "uyku miyoklonusu"],
    "G36": ["büyüme ağrısı", "büyüme ağrıları"],
    "G37": ["mezenterik lenfadenit"],
    "G38": ["ürolitiyazis", "böbrek taşı", "üreter taşı", "renal kolik"],
    "G39": ["diyabet", "diabetes", "hiperglisemi"],
    "G40": ["inguinal fıtık", "inkarsere", "fıtık"],
    "Y01": ["gastroenterit", "hipovolemik şok", "orta-ağır dehidratasyon"],
    "Y02": ["basit febril", "febril konvülziyon", "ateşli havale"],
    "Y03": ["status epileptikus", "febril status", "komplike febril"],
    "Y04": ["astım", "status astmatikus"],
    "Y05": ["rumack", "n-asetilsistein", "nac", "hepatotoksisite çizgisi"],
    "Y06": ["diyabetik ketoasidoz", "dka", "ketoasidoz", "kussmaul", "tip 1 diyabet", "diabetes mellitus"],
    "Y07": ["invajinasyon", "intususepsiyon", "çilek jölesi", "hedef işareti", "target sign", "psödo-böbrek"],
    "Y08": ["bakteriyel menenjit", "menenjit", "kernig", "brudzinski"],
    "Y09": ["piyelonefrit", "idrar yolu enfeksiyonu", "iye"],
    "Y10": ["krup", "laringotrakeit", "westley"],
    "Y11": ["apandisit", "mcburney", "rovsing", "apendiks", "apendikolit", "pas skoru"],
    "Y12": ["bronşiolit", "bronşiyolit", "rsv"],
    "Y13": ["henoch-schönlein", "henoch schönlein", "iga vasküliti", "hsp"],
    "Y14": ["supraventriküler taşikardi", "svt", "adenozin", "vagal manevra"],
    "Y15": ["yabancı cisim aspirasyonu", "rijit bronkoskopi"],
    "Y16": ["anafilaksi", "anafilaktik"],
    "Y17": ["testis torsiyonu", "torsiyon", "prehn", "bell clapper"],
    "Y18": ["immün trombositopenik", "itp", "trombositopenik purpura"],
    "Y19": ["kalsiyum kanal blokeri", "amlodipin", "hiperinsülinemi-öglisemi"],
    "Y20": ["orbital selülit", "postseptal selülit", "preseptal selülit", "subperiosteal"],
    "Y21": ["lober pnömoni", "konsolidasyon"],
    "Y22": ["ampiyem", "parapnömonik", "efüzyon"],
    "Y23": ["pnömotoraks", "viseral plevra"],
    "Y24": ["toksik şok", "tşs", "tss"],
    "Y25": ["ssss", "haşlanmış deri", "ritter"],
    "Y26": ["peritonsiller", "abse", "quinsy", "trismus"],
    "Y27": ["mastoidit", "mastoid"],
    "Y28": ["retrofarengeal", "prevertebral"],
    "Y29": ["düğme pil", "button battery", "yabancı cisim"],
    "Y30": ["ileus", "mekanik obstrüksiyon", "bağırsak tıkanıklığı"],
    "Y31": ["mekkel", "meckel", "divertikül"],
    "Y32": ["over torsiyonu", "adneksiyal", "over"],
    "Y33": ["miyokardit", "troponin", "kardit"],
    "Y34": ["ventriküler taşikardi", "vt", "geniş qrs"],
    "Y35": ["romatizmal ateş", "ara", "sydenham", "kore"],
    "Y36": ["guillain", "barre", "gbs", "albüminositolojik"],
    "Y37": ["serebellar ataksi", "ataksi"],
    "Y38": ["demir zehirlenmesi", "demir intoksikasyonu", "deferoksamin"],
    "Y39": ["trisiklik", "tka", "amitriptilin"],
    "Y40": ["üre döngüsü", "hiperamonyemi", "amonyak"],
    "G41": ["gastroenterit", "rotavirüs", "norovirüs", "espghan"],
    "G42": ["besin zehirlenmesi", "enterotoksin", "stafilokok"],
    "G43": ["fonksiyonel kabızlık", "enkoprezis", "fekal impaksiyon", "taşma ishali", "overflow"],
    "G44": ["infantil kolik", "wessel", "üçler kuralı", "3'ler kuralı"],
    "G45": ["proktokolit", "fpiap", "inek sütü proteini alerjisi", "süt proteini alerjisi"],
    "G46": ["giardia", "giardiazis", "lamblia"],
    "G47": ["mezenterik lenfadenit", "lenfoid hiperplazi"],
    "G48": ["toddler", "non-spesifik diyare", "nonspesifik diyare"],
    "G49": ["reflü", "happy spitter", "mutlu kusan", "gastroözofageal"],
    "G50": ["gastrit"],
    "G51": ["asetonemik", "açlık ketozu", "ketotik kusma"],
    "G52": ["piyelonefrit", "idrar yolu enfeksiyonu", "iye"],
    "G53": ["fonksiyonel karın ağrısı", "roma iv", "okul kaygısı"],
    "G54": ["çölyak", "gluten enteropati"],
    "G55": ["pnömoni", "plörit", "konsolidasyon"],
    "G56": ["hepatit a", "hav", "viral hepatit"],
    "G57": ["laktoz", "laktaz"],
    "G58": ["hareket hastalığı", "taşıt tutması", "kinetoz", "motion"],
    "G59": ["kıl kurdu", "enterobi", "oksiyür", "selofan"],
    "G60": ["streptokok", "agbhs", "tonsillofarenjit", "centor", "mcisaac"],
    "G61": ["toksik sinovit", "transient sinovit", "geçici sinovit"],
    "G62": ["migren", "aurasız migren"],
    "G63": ["sistit", "alt idrar yolu"],
    "G64": ["sıcak bitkinliği", "heat exhaustion"],
    "G65": ["preseptal", "periorbital selülit"],
    "G66": ["diskezi", "infant diskezi"],
    "G67": ["labial füzyon", "sinekşi"],
    "G68": ["gerilim tipi", "gerilim baş ağrısı"],
    "G69": ["epistaksis", "kiesselbach"],
    "G70": ["tinea", "korporis"],
    "Y41": ["apandisit", "mcburney", "rovsing", "apendiks", "apendikolit", "pas skoru"],
    "Y42": ["invajinasyon", "intususepsiyon", "intussusepsiyon", "çilek jölesi", "hedef işareti", "target sign", "psödo-böbrek"],
    "Y43": ["pilor", "pilorik"],
    "Y44": ["gastroenterit", "hipovolemik şok", "ağır dehidratasyon"],
    "Y45": ["diyabetik ketoasidoz", "dka", "ketoasidoz", "kussmaul", "tip 1 diyabet", "diabetes mellitus"],
    "Y46": ["hemolitik üremik", "hüs", "stec", "o157", "shiga"],
    "Y47": ["malrotasyon", "volvulus", "ladd", "corkscrew", "tirbüşon"],
    "Y48": ["testis torsiyonu", "torsiyon", "prehn", "bell clapper"],
    "Y49": ["henoch-schönlein", "henoch schönlein", "iga vasküliti", "hsp"],
    "Y50": ["inkarsere", "fıtık", "herni", "taksis"],
    "Y51": ["ileus", "adezyon", "bağırsak tıkanıklığı", "mekanik obstrüksiyon"],
    "Y52": ["difficile", "psödomembran", "pseudomembran", "cdi"],
    "Y53": ["pankreatit"],
    "Y54": ["hirschsprung", "enterokolit", "haec", "aganglion"],
    "Y55": ["karaciğer yetmezliği", "palf", "hepatik ensefalopati"],
    "Y56": ["meckel", "divertikül"],
    "Y57": ["hiponatremi", "su intoksikasyonu"],
    "Y58": ["prerenal", "akut böbrek hasarı", "abh", "azotemi"],
    "Y59": ["spontan bakteriyel peritonit", "sbp", "peritonit"],
    "Y60": ["düğme pil", "button battery", "yabancı cisim"],
    "Y61": ["kawasaki", "mukokutanöz"],
    "Y62": ["septik artrit", "eklem aspirasyonu"],
    "Y63": ["poststreptokoksik", "apsgn", "glomerülonefrit"],
    "Y64": ["nefrotik sendrom", "minimal değişiklik"],
    "Y65": ["distoni", "distonik", "metoklopramid", "biperiden", "akineton"],
    "Y66": ["febril nötropeni", "nötropenik"],
    "Y67": ["orak hücre", "vazo-oklüzif", "daktilit"],
    "Y68": ["hiperbilirubinemi", "bhutani"],
    "Y69": ["konjenital adrenal", "adrenal kriz", "kah"],
    "Y70": ["karbonmonoksit", "karboksihemoglobin"],
}


def load_cases(filepath):
    spec = importlib.util.spec_from_file_location("mod", filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for attr in (
        "CASES",
        "GREEN_CASES_PART1",
        "GREEN_CASES_PART2",
        "GREEN_CASES_PART3",
        "GREEN_CASES_PART4",
        "GREEN_CASES_PART5",
        "GREEN_CASES_PART6",
        "GREEN_CASES_PART7",
        "YELLOW_CASES_PART1",
        "YELLOW_CASES_PART2",
        "YELLOW_CASES_PART3",
        "YELLOW_CASES_PART4",
        "YELLOW_CASES_PART5",
        "YELLOW_CASES_PART6",
        "YELLOW_CASES_PART7",
    ):
        if hasattr(mod, attr):
            return getattr(mod, attr)
    raise ValueError(f"{filepath} içinde CASES listesi bulunamadı!")


def has_spoiler(text_low: str, kw: str) -> bool:
    if len(kw) <= 4:
        return bool(re.search(rf"\b{re.escape(kw)}\b", text_low))
    return kw in text_low


def word_count(s):
    return len(re.findall(r"\S+", s or ""))


def validate_file(filepath):
    cases = load_cases(filepath)
    errors = []
    warnings = []

    for c in cases:
        cid = c.get("id", "UNKNOWN")
        missing = REQUIRED_CASE_KEYS - set(c.keys())
        if missing:
            errors.append(f"[{cid}] Eksik anahtarlar: {missing}")
            continue

        steps = c["steps"]
        if len(steps) < 4:
            errors.append(f"[{cid}] En az 4 aşama olmalı, mevcut: {len(steps)}")

        # Find diagnosis step index (usually index 2)
        diag_step_idx = 2
        for idx, stp in enumerate(steps):
            if "tanı" in stp.get("stage_title", "").lower() or "tanınız nedir" in stp.get("question", "").lower():
                diag_step_idx = idx
                break

        spoiler_words = SPOILER_KEYWORDS_BY_ID.get(cid, [])
        if not spoiler_words:
            errors.append(f"[{cid}] SPOILER_KEYWORDS_BY_ID içinde bu vaka için anahtar kelime tanımlı değil")

        # Doğru seçenek konumu ve uzunluk ipucu (tanı adımı hariç)
        non_diag = [stp for i, stp in enumerate(steps) if i != diag_step_idx and len(stp.get("options", [])) == 4]
        correct_idx = [next((i for i, o in enumerate(stp["options"]) if o.get("is_correct")), -1) for stp in steps]
        if len(set(correct_idx)) == 1:
            errors.append(f"[{cid}] Ham veride doğru seçenek her adımda aynı indekste ({correct_idx[0]}); çeşitlendirin")
        longest_hits = 0
        for stp in non_diag:
            L = [word_count(o["text"]) for o in stp["options"]]
            ci = next((i for i, o in enumerate(stp["options"]) if o.get("is_correct")), -1)
            if ci >= 0 and L[ci] == max(L) and L.count(max(L)) == 1:
                longest_hits += 1
        if non_diag and longest_hits > len(non_diag) // 2:
            errors.append(f"[{cid}] Tanı dışı {len(non_diag)} adımın {longest_hits}'inde doğru seçenek tek başına en uzun")

        # Check complaint and history for spoilers (except when complaint itself is a general symptom)
        for field_name in ("complaint", "history"):
            val_low = c[field_name].lower()
            for sw in spoiler_words:
                if has_spoiler(val_low, sw):
                    errors.append(f"[{cid}] '{field_name}' içinde tanı ipucu (spoiler) bulundu: '{sw}'")

        for s_idx, stp in enumerate(steps):
            opts = stp.get("options", [])
            if len(opts) != 4:
                errors.append(f"[{cid} - Adım {s_idx+1}] Tam 4 seçenek olmalı, mevcut: {len(opts)}")
                continue

            correct_opts = [o for o in opts if o.get("is_correct") is True]
            wrong_opts = [o for o in opts if not o.get("is_correct")]
            if len(correct_opts) != 1:
                errors.append(f"[{cid} - Adım {s_idx+1}] Tam 1 doğru seçenek olmalı, mevcut: {len(correct_opts)}")
                continue

            co = correct_opts[0]
            for k in ("text", "explanation", "new_finding"):
                if not co.get(k) or not str(co.get(k)).strip():
                    errors.append(f"[{cid} - Adım {s_idx+1}] Doğru seçenekte '{k}' boş!")

            if cid in ("G17", "G18", "G19", "G20", "G37", "G38", "G39", "G40") and s_idx == 0:
                if not co.get("triggers_yellow_transfer"):
                    errors.append(f"[{cid} - Adım 1] Doğru seçenekte 'triggers_yellow_transfer': True olmalı!")

            for w_idx, wo in enumerate(wrong_opts):
                for k in ("text", "scenario_update", "teaching_point"):
                    if not wo.get(k) or not str(wo.get(k)).strip():
                        errors.append(f"[{cid} - Adım {s_idx+1} - Yanlış {w_idx+1}] '{k}' boş!")

            # Check option lengths
            lengths = [word_count(o["text"]) for o in opts]
            min_len, max_len = min(lengths), max(lengths)
            co_len = word_count(co["text"])
            avg_wrong = sum(word_count(wo["text"]) for wo in wrong_opts) / 3.0

            is_diag_step = (s_idx == diag_step_idx)
            if not is_diag_step:
                if min_len < 9:
                    errors.append(
                        f"[{cid} - Adım {s_idx+1}] Çok kısa seçenek var ({min_len} kelime). En az 10 kelime olmalı. Uzunluklar: {lengths}"
                    )
                if max_len / max(min_len, 1) > 1.85:
                    errors.append(
                        f"[{cid} - Adım {s_idx+1}] Seçenek uzunlukları dengesiz (min={min_len}, max={max_len}, oran={max_len/max(min_len,1):.2f} > 1.85). Uzunluklar: {lengths}"
                    )
                if co_len > avg_wrong * 1.35:
                    errors.append(
                        f"[{cid} - Adım {s_idx+1}] Doğru seçenek yanlışların ortalamasından çok uzun ({co_len} vs ort {avg_wrong:.1f}). Uzunluklar: {lengths}"
                    )
            else:
                if min_len < 2:
                    errors.append(f"[{cid} - Adım {s_idx+1} (Tanı)] Çok kısa tanı seçeneği ({min_len} kelime). Uzunluklar: {lengths}")
                if max_len / max(min_len, 1) > 2.5 and max_len - min_len > 6:
                    errors.append(
                        f"[{cid} - Adım {s_idx+1} (Tanı)] Tanı seçenek uzunlukları dengesiz: {lengths}"
                    )

            # Check spoilers in steps BEFORE diagnosis step
            if s_idx < diag_step_idx:
                texts_to_check = [
                    ("stage_title", stp.get("stage_title", "")),
                    ("question", stp.get("question", "")),
                ]
                for o_i, o in enumerate(opts):
                    texts_to_check.append((f"opt[{o_i}].text", o.get("text", "")))
                    if o.get("is_correct"):
                        texts_to_check.append((f"opt[{o_i}].explanation", o.get("explanation", "")))
                        texts_to_check.append((f"opt[{o_i}].new_finding", o.get("new_finding", "")))
                    else:
                        texts_to_check.append((f"opt[{o_i}].scenario_update", o.get("scenario_update", "")))
                        texts_to_check.append((f"opt[{o_i}].teaching_point", o.get("teaching_point", "")))

                for label, txt in texts_to_check:
                    txt_low = txt.lower()
                    for sw in spoiler_words:
                        if has_spoiler(txt_low, sw):
                            errors.append(
                                f"[{cid} - Adım {s_idx+1} ({label})] Tanı öncesi SPOILER yakalandı: '{sw}'"
                            )

    return len(cases), errors, warnings


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python cases_v2/dogrula.py <dosya1.py> [dosya2.py ...]")
        sys.exit(1)

    total_errors = 0
    for fp in sys.argv[1:]:
        try:
            cnt, errs, warns = validate_file(fp)
            print(f"=== {fp} ({cnt} vaka) ===")
            if not errs:
                print("  ✅ TÜM KONTROLLER BAŞARILI (0 hata)")
            else:
                print(f"  ❌ {len(errs)} HATA BULUNDU:")
                for e in errs:
                    print("   -", e)
                total_errors += len(errs)
        except Exception as ex:
            print(f"=== {fp} ===\n  ❌ İSTİSNA: {ex}")
            total_errors += 1

    sys.exit(1 if total_errors > 0 else 0)
