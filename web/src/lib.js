// Python arşivindeki normalize_search_text ile aynı: Türkçe harfleri sadeleştirir.
export function normalize(text) {
  if (!text) return ''
  return text
    .replace(/İ/g, 'i')
    .replace(/I/g, 'ı')
    .toLowerCase()
    .replace(/ğ/g, 'g')
    .replace(/ü/g, 'u')
    .replace(/ş/g, 's')
    .replace(/ı/g, 'i')
    .replace(/ö/g, 'o')
    .replace(/ç/g, 'c')
}

// Eş anlamlı / farklı yazım grupları (sadeleştirilmiş, kelime başı biçiminde).
// Bir arama kelimesi gruptaki bir üyeyle başlıyorsa (ya da üyenin başıysa) grubun tümü aranır.
const SYNONYMS = [
  ['serebell', 'cerebell', 'beyincik'],
  ['ataksi', 'ataxi'],
  ['menenjit', 'meningit'],
  ['ensefalit', 'encephalit'],
  ['ensefalopati', 'encephalopath'],
  ['krup', 'croup', 'laringotrakeit'],
  ['bronsiolit', 'bronsiyolit', 'bronchiolit'],
  ['apandisit', 'appendicit', 'apendisit'],
  ['pnomoni', 'pneumoni', 'zaturre'],
  ['astim', 'asthma'],
  ['salbutamol', 'albuterol', 'ventolin'],
  ['adrenalin', 'epinefrin', 'epinephrin'],
  ['parasetamol', 'asetaminofen', 'acetaminophen', 'paracetamol'],
  ['invajinasyon', 'intususepsiyon', 'intussuscept'],
  ['nobet', 'konvulziyon', 'convulsion', 'seizure'],
  ['epilepsi', 'epilepsy'],
  ['ketoasidoz', 'dka', 'ketoacidosis'],
  ['diyabet', 'diabet'],
  ['anafilaksi', 'anaphyla'],
  ['hipoglisemi', 'hypoglycem'],
  ['dehidratasyon', 'dehydrat'],
  ['gastroenterit', 'gastroenteritis'],
  ['ishal', 'diyare', 'diarrh'],
  ['kusma', 'vomit'],
  ['dokuntu', 'ekzantem', 'rash'],
  ['siyanoz', 'cyanosis', 'morarma'],
  ['hisilti', 'hirilti', 'wheez'],
  ['henoch', 'hsp', 'iga vaskulit'],
  ['itp', 'trombositopenik purpura'],
  ['migren', 'migraine'],
  ['torsiyon', 'torsion'],
  ['ondansetron', 'zofran'],
  ['deksametazon', 'dexamethason'],
  ['prednizolon', 'prednisolon'],
  ['idrar yolu enfeksiyon', 'iye'],
  ['kizamik', 'measles', 'rubeola'],
  ['sucicegi', 'varisella', 'varicella'],
  ['bogmaca', 'pertussis'],
  ['kabakulak', 'parotit', 'mumps'],
  ['gks', 'glasgow'],
  ['tasikardi', 'tachycard'],
  ['bradikardi', 'bradycard'],
  ['hipotansiyon', 'hypotension'],
  ['entubasyon', 'intubat'],
  ['antibiyotik', 'antibiotic'],
  ['yogun bakim', 'icu', 'picu'],
]

const escapeRe = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')

// Latince/İngilizce yazımı Türkçe okunuşa yaklaştırır: cerebellum -> serebellum, hypoglycemia -> hipoglisemia
function transliterate(w) {
  return w
    .replace(/ph/g, 'f')
    .replace(/th/g, 't')
    .replace(/ch/g, 'k')
    .replace(/c(?=[eiy])/g, 's')
    .replace(/c/g, 'k')
    .replace(/x/g, 'ks')
    .replace(/q/g, 'k')
    .replace(/w/g, 'v')
    .replace(/y(?![aeiou])/g, 'i')
}

// Ek farkını tolere et: serebellum/serebellar -> serebell, ataksik -> ataks
function stem(w) {
  if (w.length < 7) return w
  const s = w.replace(/(um|us|ar|al|ik|ic|is|ia|ya|ler|lar|leri|lari)$/, '')
  return s.length >= 5 ? s : w
}

function variants(word) {
  const out = new Set([word])
  // Kısa kelimeler (qt, iv, y14…) olduğu gibi aranır; yazım dönüşümü yalnızca uzun kelimelerde
  const t = word.length >= 5 ? transliterate(word) : word
  out.add(t)
  out.add(stem(word))
  out.add(stem(t))
  for (const group of SYNONYMS) {
    const hit = group.some((m) => [...out].some((v) => v.startsWith(m) || (v.length >= 4 && m.startsWith(v))))
    if (hit) group.forEach((m) => out.add(m))
  }
  return [...out].filter(Boolean)
}

// Arama sorgusunu eşleştiriciye çevirir: her kelime (veya varyantı) metinde KELİME BAŞINDA geçmeli.
// Örn. "hsp" artık "hirschsprung" içinde eşleşmez; "cerebellum" "serebellar"ı bulur.
export function makeMatcher(query) {
  const words = normalize(query).split(/\s+/).filter(Boolean)
  const regs = words.map(
    (w) => new RegExp(`(?:^|[^a-z0-9])(?:${variants(w).map(escapeRe).join('|')})`),
  )
  return regs.length ? (text) => regs.every((r) => r.test(text)) : null
}

const caseCache = new Map()

export function loadCase(id) {
  if (!caseCache.has(id)) {
    const p = fetch(`/cases/${id}.json`).then((r) => {
      if (!r.ok) throw new Error(`Vaka yüklenemedi: ${id}`)
      return r.json()
    })
    p.catch(() => caseCache.delete(id))
    caseCache.set(id, p)
  }
  return caseCache.get(id)
}

let searchPromise = null

export function loadSearchIndex() {
  if (!searchPromise) {
    searchPromise = fetch('/search.json').then((r) => r.json())
    searchPromise.catch(() => {
      searchPromise = null
    })
  }
  return searchPromise
}

export function shuffle(list) {
  const a = list.slice()
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

const SOLVED_KEY = 'pea-solved-v1'

export function readSolved() {
  try {
    return new Set(JSON.parse(localStorage.getItem(SOLVED_KEY) || '[]'))
  } catch {
    return new Set()
  }
}

export function writeSolved(set) {
  try {
    localStorage.setItem(SOLVED_KEY, JSON.stringify([...set]))
  } catch {
    // Gizli pencere vb. durumlarda ilerleme yalnızca bu oturumda tutulur.
  }
}

export function readUrlState() {
  const p = new URLSearchParams(window.location.search)
  const zone = p.get('alan')
  return {
    zone: zone === 'yesil' ? 'green' : zone === 'sari' ? 'yellow' : 'all',
    tags: [...new Set(p.getAll('etiket').filter(Boolean))],
    query: p.get('ara') || '',
    caseId: p.get('vaka') || '',
  }
}

export function writeUrlState({ zone, tags, query, caseId }) {
  const p = new URLSearchParams()
  if (zone === 'green') p.set('alan', 'yesil')
  if (zone === 'yellow') p.set('alan', 'sari')
  for (const t of tags) p.append('etiket', t)
  if (query) p.set('ara', query)
  if (caseId) p.set('vaka', caseId)
  const qs = p.toString()
  const url = qs ? `?${qs}` : window.location.pathname
  window.history.replaceState(null, '', url)
}
