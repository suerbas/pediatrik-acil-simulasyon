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
