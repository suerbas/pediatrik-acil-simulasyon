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
    "Y01": ["nazofarenjit", "soğuk algınlığı", "nezle"],
    "Y02": ["streptokok", "agbhs", "centor", "mcisaac", "strep-a", "strep a"],
    "Y03": ["otitis media", "aom", "orta kulak iltihabı"],
    "Y04": ["gastroenterit", "age"],
    "Y05": ["fonksiyonel kabızlık", "konstipasyon", "roma iv", "hirschsprung"],
    "Y06": ["ürtiker", "kurdeşen"],
    "Y07": ["eritema infeksiyozum", "beşinci hastalık", "5. hastalık", "parvovirus", "tokatlanmış"],
    "Y08": ["roseola", "altıncı hastalık", "6. hastalık", "ekzantema subitum", "hhv-6", "hhv6", "nagayama"],
    "Y09": ["el-ayak-ağız", "el ayak ağız", "coxsackie", "enterovirus", "enteroviral"],
    "Y10": ["alerjik rinit", "postnazal akıntı sendromu", "üst hava yolu öksürük sendromu"],
    "Y11": ["infantil kolik", "wessel", "3'ler kuralı", "üçler kuralı"],
    "Y12": ["ortostatik hipotansiyon", "vazovagal"],
    "Y13": ["krup", "laringotrakeit", "westley"],
    "Y14": ["suçiçeği", "varisella", "vzv"],
    "Y15": ["konjonktivit", "adenoviral", "adenovirus"],
    "Y16": ["impetigo", "ssss", "haşlanmış deri"],
    "Y17": ["apandisit", "mcburney", "rovsing", "apendiks", "apendikolit"],
    "Y18": ["meningokok", "meningokoksemi", "waterhouse"],
    "Y19": ["bronşiolit", "bronşiyolit"],
    "Y20": ["anafilaksi", "anafilaktik"],
    "Y21": ["demir eksikliği", "ferritin", "mikrositer"],
    "Y22": ["aft", "aftöz", "stomatit"],
    "Y23": ["pitriyazis", "rozea", "herald patch", "madalyon"],
    "Y24": ["molluskum", "molluscum", "kontagiozum"],
    "Y25": ["bebek bezi dermatiti", "diaper", "kandida", "kandidiyazis", "satellit"],
    "Y26": ["enürezis", "noktürnal"],
    "Y27": ["kıl kurdu", "enterobiyazis", "oksiyüriyazis", "selofan"],
    "Y28": ["reflü", "happy spitter", "gastroözofageal"],
    "Y29": ["efüzyonlu", "seröz otit", "som"],
    "Y30": ["reaktif lenfadenit", "reaktif lenfadenopati"],
    "Y31": ["mikoplazma", "mycoplasma", "atipik pnömoni"],
    "Y32": ["alerjik konjonktivit", "vernal"],
    "Y33": ["dakriyostenoz", "nazolakrimal", "kanal tıkanıklığı"],
    "Y34": ["korneal abrazyon", "abrazyon", "flöresein"],
    "Y35": ["miyoklonus", "uyku miyoklonusu"],
    "Y36": ["büyüme ağrısı", "büyüme ağrıları"],
    "Y37": ["mezenterik lenfadenit"],
    "Y38": ["ürolitiyazis", "böbrek taşı", "üreter taşı", "renal kolik"],
    "Y39": ["diyabet", "diabetes", "hiperglisemi"],
    "Y40": ["inguinal fıtık", "inkarsere", "fıtık"],
    "S01": ["gastroenterit", "hipovolemik şok", "orta-ağır dehidratasyon"],
    "S02": ["basit febril", "febril konvülziyon", "ateşli havale"],
    "S03": ["status epileptikus", "febril status", "komplike febril"],
    "S04": ["astım", "status astmatikus"],
    "S05": ["rumack", "n-asetilsistein", "nac", "hepatotoksisite çizgisi"],
    "S06": ["diyabetik ketoasidoz", "dka", "ketoasidoz", "kussmaul", "tip 1 diyabet", "diabetes mellitus"],
    "S07": ["invajinasyon", "intususepsiyon", "çilek jölesi", "hedef işareti", "target sign", "psödo-böbrek"],
    "S08": ["bakteriyel menenjit", "menenjit", "kernig", "brudzinski"],
    "S09": ["piyelonefrit", "idrar yolu enfeksiyonu", "iye"],
    "S10": ["krup", "laringotrakeit", "westley"],
    "S11": ["apandisit", "mcburney", "rovsing", "apendiks", "apendikolit", "pas skoru"],
    "S12": ["bronşiolit", "bronşiyolit", "rsv"],
    "S13": ["henoch-schönlein", "henoch schönlein", "iga vasküliti", "hsp"],
    "S14": ["supraventriküler taşikardi", "svt", "adenozin", "vagal manevra"],
    "S15": ["yabancı cisim aspirasyonu", "rijit bronkoskopi"],
    "S16": ["anafilaksi", "anafilaktik"],
    "S17": ["testis torsiyonu", "torsiyon", "prehn", "bell clapper"],
    "S18": ["immün trombositopenik", "itp", "trombositopenik purpura"],
    "S19": ["kalsiyum kanal blokeri", "amlodipin", "hiperinsülinemi-öglisemi"],
    "S20": ["orbital selülit", "postseptal selülit", "preseptal selülit", "subperiosteal"],
    "S21": ["lober pnömoni", "konsolidasyon"],
    "S22": ["ampiyem", "parapnömonik", "efüzyon"],
    "S23": ["pnömotoraks", "viseral plevra"],
    "S24": ["toksik şok", "tşs", "tss"],
    "S25": ["ssss", "haşlanmış deri", "ritter"],
    "S26": ["peritonsiller", "abse", "quinsy", "trismus"],
    "S27": ["mastoidit", "mastoid"],
    "S28": ["retrofarengeal", "prevertebral"],
    "S29": ["düğme pil", "button battery", "yabancı cisim"],
    "S30": ["ileus", "mekanik obstrüksiyon", "bağırsak tıkanıklığı"],
    "S31": ["mekkel", "meckel", "divertikül"],
    "S32": ["over torsiyonu", "adneksiyal", "over"],
    "S33": ["miyokardit", "troponin", "kardit"],
    "S34": ["ventriküler taşikardi", "vt", "geniş qrs"],
    "S35": ["romatizmal ateş", "ara", "sydenham", "kore"],
    "S36": ["guillain", "barre", "gbs", "albüminositolojik"],
    "S37": ["serebellar ataksi", "ataksi"],
    "S38": ["demir zehirlenmesi", "demir intoksikasyonu", "deferoksamin"],
    "S39": ["trisiklik", "tka", "amitriptilin"],
    "S40": ["üre döngüsü", "hiperamonyemi", "amonyak"],
    "Y41": ["gastroenterit", "rotavirüs", "norovirüs", "espghan"],
    "Y42": ["besin zehirlenmesi", "enterotoksin", "stafilokok"],
    "Y43": ["fonksiyonel kabızlık", "enkoprezis", "fekal impaksiyon", "taşma ishali", "overflow"],
    "Y44": ["turnike", "saç teli", "kıl turnike"],
    "Y45": ["proktokolit", "fpiap", "inek sütü proteini alerjisi", "süt proteini alerjisi"],
    "Y46": ["giardia", "giardiazis", "lamblia"],
    "Y47": ["midede", "mide içinde", "gastrik"],
    "Y48": ["toddler", "non-spesifik diyare", "nonspesifik diyare"],
    "Y49": ["anne sütü sarılığı", "breast milk"],
    "Y50": ["gastrit"],
    "Y51": ["asetonemik", "açlık ketozu", "ketotik kusma"],
    "Y52": ["piyelonefrit", "idrar yolu enfeksiyonu", "iye"],
    "Y53": ["fonksiyonel karın ağrısı", "roma iv", "okul kaygısı"],
    "Y54": ["çölyak", "gluten enteropati"],
    "Y55": ["pnömoni", "plörit", "konsolidasyon"],
    "Y56": ["hepatit a", "hav", "viral hepatit"],
    "Y57": ["laktoz", "laktaz"],
    "Y58": ["hareket hastalığı", "taşıt tutması", "kinetoz", "motion"],
    "Y59": ["mononükleoz", "ebv", "epstein", "öpücük hastalığı"],
    "Y60": ["streptokok", "agbhs", "tonsillofarenjit", "centor", "mcisaac"],
    "Y61": ["toksik sinovit", "transient sinovit", "geçici sinovit"],
    "Y62": ["migren", "aurasız migren"],
    "Y63": ["sistit", "alt idrar yolu"],
    "Y64": ["sıcak bitkinliği", "heat exhaustion"],
    "Y65": ["preseptal", "periorbital selülit"],
    "Y66": ["diskezi", "infant diskezi"],
    "Y67": ["labial füzyon", "sinekşi"],
    "Y68": ["gerilim tipi", "gerilim baş ağrısı"],
    "Y69": ["epistaksis", "kiesselbach"],
    "Y70": ["tinea", "korporis"],
    "S41": ["ketotik hipoglisemi", "ketotik"],
    "S42": ["amatoksin", "amanita", "silibinin", "falloidin"],
    "S43": ["pilor", "pilorik"],
    "S44": ["gastroenterit", "hipovolemik şok", "ağır dehidratasyon"],
    "S45": ["organofosfat", "pralidoksim", "kolinerjik kriz"],
    "S46": ["hemolitik üremik", "hüs", "stec", "o157", "shiga"],
    "S47": ["malrotasyon", "volvulus", "ladd", "corkscrew", "tirbüşon"],
    "S48": ["hipernatremi", "hipernatremik"],
    "S49": ["benign afebril konvülziyon", "gastroenteritle ilişkili", "cwg"],
    "S50": ["inkarsere", "fıtık", "herni", "taksis"],
    "S51": ["zargar", "2b"],
    "S52": ["difficile", "psödomembran", "pseudomembran", "cdi"],
    "S53": ["pankreatit"],
    "S54": ["hirschsprung", "enterokolit", "haec", "aganglion"],
    "S55": ["karaciğer yetmezliği", "palf", "hepatik ensefalopati"],
    "S56": ["meckel", "divertikül"],
    "S57": ["hiponatremi", "su intoksikasyonu"],
    "S58": ["prerenal", "akut böbrek hasarı", "abh", "azotemi"],
    "S59": ["spontan bakteriyel peritonit", "sbp", "peritonit"],
    "S60": ["idrar yolu enfeksiyonu", "iye", "piyelonefrit", "ürosepsis"],
    "S61": ["kawasaki", "mukokutanöz"],
    "S62": ["septik artrit", "eklem aspirasyonu"],
    "S63": ["poststreptokoksik", "apsgn", "glomerülonefrit"],
    "S64": ["nefrotik sendrom", "minimal değişiklik"],
    "S65": ["distoni", "distonik", "metoklopramid", "biperiden", "akineton"],
    "S66": ["febril nötropeni", "nötropenik"],
    "S67": ["orak hücre", "vazo-oklüzif", "daktilit"],
    "S68": ["hiperbilirubinemi", "bhutani"],
    "S69": ["konjenital adrenal", "adrenal kriz", "kah"],
    "S70": ["karbonmonoksit", "karboksihemoglobin"],
    "Y71": ["faringokonjonktival", "adenovir"],
    "Y72": ["herpanjina", "coxsackie", "koksaki"],
    "Y73": ["sinüzit", "rinosinüzit"],
    "Y74": ["otitis eksterna", "yüzücü kulağı", "eksterna"],
    "Y75": ["hafif-orta astım atağı", "hafif atak"],
    "Y76": ["epizodik viral hışıltı", "viral hışıltı", "viral wheeze"],
    "Y77": ["odak saptanmayan ateş", "kaynağı belirsiz ateş"],
    "Y78": ["kızıl", "skarlatin", "scarlet"],
    "Y79": ["kızamık", "koplik", "morbilli", "rubeola"],
    "Y80": ["kabakulak", "parotit", "mumps"],
    "Y81": ["atopik dermatit", "egzama", "ekzema"],
    "Y82": ["skabiyez", "uyuz", "sarcoptes", "permetrin"],
    "Y83": ["büyük lokal reaksiyon", "skeeter"],
    "Y84": ["selülit", "erizipel"],
    "Y85": ["paronişi", "dolama"],
    "Y86": ["şigel", "shigella", "basilli dizanteri"],
    "Y87": ["katılma", "nefes tutma", "breath-holding"],
    "Y88": ["bell", "idiyopatik fasiyal"],
    "Y89": ["kas kaynaklı tortikolis", "postüral tortikolis", "muskuler tortikolis"],
    "Y90": ["balanopostit", "balanit", "postit"],
    "Y91": ["vulvovajinit", "nonspesifik vulvovajinit", "irritan vulvovajinit"],
    "Y92": ["kandid", "pamukçuk", "mantar"],
    "Y93": ["yetersiz anne sütü alımı", "emzirme yetersizliği"],
    "Y94": ["granülom"],
    "Y95": ["eritema toksikum", "toksikum"],
    "Y96": ["hordeolum", "arpacık", "itdirseği", "it dirseği"],
    "Y97": ["perforasyon", "perfore", "perforasyonlu"],
    "Y98": ["bronşiolit", "bronşiyolit", "rsv"],
    "Y99": ["pnömoni", "zatürre", "lober"],
    "Y100": ["akrep"],
    "S71": ["status epileptikus", "status"],
    "S72": ["provoke olmayan", "ilk afebril nöbet"],
    "S73": ["ağır astım", "ağır akut astım", "status astmatikus"],
    "S74": ["bronşiolit", "bronşiyolit", "rsv"],
    "S75": ["kızamık", "rubeola", "morbilli"],
    "S76": ["herpes", "hsv", "ensefalit"],
    "S77": ["septik şok", "ürosepsis"],
    "S78": ["hipoglisemi"],
    "S79": ["serebral ödem", "beyin ödemi"],
    "S80": ["d vitamini eksikliği", "raşitizm", "rikets", "hipokalsemi"],
    "S81": ["sentetik kannabinoid", "kannabinoid", "bonzai", "jamaika"],
    "S82": ["kkka", "kırım", "kongo", "hemorajik ateş"],
    "S83": ["bruselloz", "brusella", "brucella", "malta humması"],
    "S84": ["uzun qt", "long qt", "lqts"],
    "S85": ["lösemi", "lenfoblastik", "all"],
    "S86": ["medulloblastom", "posterior fossa tümörü", "arka çukur"],
    "S87": ["g6pd", "favizm"],
    "S88": ["ailevi akdeniz", "akdeniz ateşi", "fmf"],
    "S89": ["ektopik", "dış gebelik", "tubal"],
    "S90": ["appendiks testis", "apendiks testis", "morgagni", "testis eki"],
    "S91": ["boğmaca", "pertussis", "bordetella"],
    "S92": ["tüberküloz", "tbc", "verem", "tüberküloz menenjit"],
    "S93": ["osteomiyelit"],
    "S94": ["stevens", "johnson", "sjs", "toksik epidermal"],
    "S95": ["herpetikum", "kaposi", "variselliform"],
    "S96": ["nekrotizan", "fasiit"],
    "S97": ["ısı çarpması", "sıcak çarpması"],
    "S98": ["serotonin", "serotonerjik"],
    "S99": ["opiat", "opioid", "haşhaş", "morfin"],
    "S100": ["datura", "tatula", "boru çiçeği", "antikolinerjik"],
    "S101": ["süpüratif", "bakteriyel parotit", "parotit", "parotis", "sialadenit", "stensen"],
    "S102": ["septik artrit", "kocher", "caird", "artrosentez", "eklem aspirasyonu"],
    "Y101": ["biliyer atrezi", "kasai", "portoenterostomi"],
    "Y102": ["karbonmonoksit", "karboksihemoglobin"],
}


def load_cases(filepath):
    spec = importlib.util.spec_from_file_location("mod", filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, "CASES"):
        return mod.CASES
    for attr in dir(mod):
        if re.fullmatch(r"(GREEN|YELLOW)_CASES_PART\d+", attr):
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

            if cid in ("Y17", "Y18", "Y19", "Y20", "Y37", "Y38", "Y39", "Y40") and s_idx == 0:
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
