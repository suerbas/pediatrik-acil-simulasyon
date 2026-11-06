import { useCallback, useDeferredValue, useEffect, useMemo, useState } from 'react'
import INDEX from './data/index.json'
import CaseCard from './components/CaseCard.jsx'
import Drawer from './components/Drawer.jsx'
import { loadCase, loadSearchIndex, normalize, readSolved, readUrlState, writeSolved, writeUrlState } from './lib.js'

const COUNTS = {
  all: INDEX.length,
  green: INDEX.filter((c) => c.zone === 'green').length,
  yellow: INDEX.filter((c) => c.zone === 'yellow').length,
}
const IDS = new Set(INDEX.map((c) => c.id))

export default function App() {
  const initial = useMemo(readUrlState, [])
  const [zone, setZone] = useState(initial.zone)
  const [tag, setTag] = useState(initial.tag)
  const [query, setQuery] = useState(initial.query)
  const [caseId, setCaseId] = useState(IDS.has(initial.caseId) ? initial.caseId : '')
  const [solved, setSolved] = useState(readSolved)
  const [searchIndex, setSearchIndex] = useState(null)

  const deferredQuery = useDeferredValue(query.trim())

  useEffect(() => {
    writeUrlState({ zone, tag, query: query.trim(), caseId })
  }, [zone, tag, query, caseId])

  useEffect(() => {
    if (deferredQuery && !searchIndex) loadSearchIndex().then(setSearchIndex).catch(() => {})
  }, [deferredQuery, searchIndex])

  const filtered = useMemo(() => {
    let list = INDEX
    if (zone !== 'all') list = list.filter((c) => c.zone === zone)
    if (tag) {
      const t = normalize(tag)
      list = list.filter(
        (c) =>
          c.tags.some((x) => normalize(x).includes(t)) ||
          normalize(c.complaint).includes(t) ||
          normalize(c.category).includes(t),
      )
    }
    if (deferredQuery) {
      const q = normalize(deferredQuery)
      list = list.filter((c) =>
        searchIndex
          ? searchIndex[c.id]?.includes(q)
          : normalize(`${c.id} ${c.age} ${c.gender} ${c.category} ${c.complaint} ${c.tags.join(' ')}`).includes(q),
      )
    }
    return list
  }, [zone, tag, deferredQuery, searchIndex])

  const markSolved = useCallback((id) => {
    setSolved((prev) => {
      if (prev.has(id)) return prev
      const next = new Set(prev)
      next.add(id)
      writeSolved(next)
      return next
    })
  }, [])

  const pickTag = useCallback((t) => {
    setTag(t)
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }, [])

  const clearFilters = () => {
    setTag('')
    setQuery('')
  }

  const solvedCount = INDEX.filter((c) => solved.has(c.id)).length

  return (
    <div className="page">
      <header className="masthead">
        <div className="masthead-row">
          <h1 className="wordmark">
            The Pediatric
            <br />
            Emergency Archive
          </h1>
          <dl className="masthead-stats">
            <div>
              <dt>Vaka</dt>
              <dd>{COUNTS.all}</dd>
            </div>
            <div>
              <dt>Çözülen</dt>
              <dd>
                {solvedCount}
                <span className="muted">/{COUNTS.all}</span>
              </dd>
            </div>
          </dl>
        </div>
        <p className="masthead-sub">
          Adım adım karar verdiren pediatrik acil vaka simülasyonları · Kanıta dayalı · AAP / PALS / ESPGHAN / ISPAD
        </p>
      </header>

      <div className="toolbar">
        <div className="zone-tabs" role="tablist" aria-label="Alan">
          {[
            ['all', 'Tüm Vakalar'],
            ['green', 'Yeşil Alan'],
            ['yellow', 'Sarı Alan'],
          ].map(([key, label]) => (
            <button
              key={key}
              role="tab"
              aria-selected={zone === key}
              className={`zone-tab zone-tab-${key}`}
              onClick={() => setZone(key)}
            >
              {key !== 'all' && <span className={`dot dot-${key}`} aria-hidden="true" />}
              {label}
              <span className="zone-count">{COUNTS[key]}</span>
            </button>
          ))}
        </div>
        <label className="search">
          <span className="visually-hidden">Arşivde ara</span>
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true">
            <circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" strokeWidth="2" />
            <path d="M20 20l-4-4" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
          </svg>
          <input
            type="search"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onFocus={() => loadSearchIndex().then(setSearchIndex).catch(() => {})}
            placeholder="Tüm arşivde ara: menenjit, yoğun bakım, kusma, G14…"
          />
        </label>
      </div>

      <div className="result-line">
        <span>
          <b>{filtered.length}</b> vaka listeleniyor
        </span>
        {tag && (
          <button className="filter-pill" onClick={() => setTag('')}>
            Etiket: <b>{tag}</b> <span aria-hidden="true">✕</span>
          </button>
        )}
        {query.trim() && (
          <button className="filter-pill filter-pill-search" onClick={() => setQuery('')}>
            Arama: <b>“{query.trim()}”</b> <span aria-hidden="true">✕</span>
          </button>
        )}
        {(tag || query.trim()) && (
          <button className="link-button" onClick={clearFilters}>
            Filtreleri temizle
          </button>
        )}
      </div>

      {filtered.length === 0 ? (
        <div className="empty">
          <p>Bu filtrelerle eşleşen vaka yok.</p>
          <button className="btn btn-primary" onClick={clearFilters}>
            Filtreleri temizle
          </button>
        </div>
      ) : (
        <main className="grid">
          {filtered.map((c) => (
            <CaseCard
              key={c.id}
              item={c}
              solved={solved.has(c.id)}
              onOpen={setCaseId}
              onTag={pickTag}
              onPrefetch={loadCase}
            />
          ))}
        </main>
      )}

      <footer className="colophon">
        <span>The Pediatric Emergency Archive</span>
        <span>Eğitim amaçlıdır; klinik kararın yerini tutmaz.</span>
      </footer>

      {caseId && <Drawer key={caseId} caseId={caseId} onClose={() => setCaseId('')} onSolved={markSolved} />}
    </div>
  )
}
