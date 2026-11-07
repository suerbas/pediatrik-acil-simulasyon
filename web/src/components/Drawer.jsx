import { useEffect, useRef, useState } from 'react'
import { loadCase, shuffle } from '../lib.js'

const Html = ({ html, as: Tag = 'span', className }) => (
  <Tag className={className} dangerouslySetInnerHTML={{ __html: html }} />
)

export default function Drawer({ caseId, onClose, onSolved }) {
  const [data, setData] = useState(null)
  const [error, setError] = useState('')
  const [stepIdx, setStepIdx] = useState(0)
  const [logs, setLogs] = useState([])
  const [detour, setDetour] = useState(null)
  const [feedback, setFeedback] = useState('')
  const [showHint, setShowHint] = useState(false)
  const [options, setOptions] = useState([])
  const closeRef = useRef(null)
  const bodyRef = useRef(null)
  const questionRef = useRef(null)

  useEffect(() => {
    let alive = true
    loadCase(caseId)
      .then((c) => {
        if (!alive) return
        setData(c)
        setOptions(c.steps.map((s) => shuffle(s.options)))
      })
      .catch((e) => alive && setError(e.message))
    return () => {
      alive = false
    }
  }, [caseId])

  useEffect(() => {
    closeRef.current?.focus()
    const onKey = (e) => e.key === 'Escape' && onClose()
    document.addEventListener('keydown', onKey)
    document.body.classList.add('no-scroll')
    return () => {
      document.removeEventListener('keydown', onKey)
      document.body.classList.remove('no-scroll')
    }
  }, [onClose])

  const total = data?.steps.length ?? 0
  const finished = data && stepIdx >= total

  useEffect(() => {
    if (finished) onSolved(caseId)
  }, [finished, caseId, onSolved])

  // Vital/lab baloncuğunu panelin içinde tut: sağa/sola taşarsa kaydır, üstte yer yoksa alta aç.
  useEffect(() => {
    const body = bodyRef.current
    if (!body) return
    const place = (e) => {
      const val = e.target.closest?.('.med-val')
      const tip = val?.querySelector('.med-tooltip')
      if (!tip) return
      tip.style.left = '0px'
      tip.style.top = ''
      tip.style.bottom = ''
      requestAnimationFrame(() => {
        const box = body.getBoundingClientRect()
        const t = tip.getBoundingClientRect()
        const v = val.getBoundingClientRect()
        const pad = 8
        let shift = 0
        if (t.right > box.right - pad) shift = box.right - pad - t.right
        if (t.left + shift < box.left + pad) shift = box.left + pad - t.left
        tip.style.left = `${shift}px`
        if (t.top < box.top + pad) {
          tip.style.bottom = 'auto'
          tip.style.top = `${v.height + 6}px`
        }
      })
    }
    body.addEventListener('pointerover', place)
    body.addEventListener('focusin', place)
    return () => {
      body.removeEventListener('pointerover', place)
      body.removeEventListener('focusin', place)
    }
  }, [data])

  // Yeni aşamaya geçince soruyu görünür alana getir.
  useEffect(() => {
    if (stepIdx > 0) questionRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }, [stepIdx])

  const choose = (opt) => {
    const step = data.steps[stepIdx]
    setShowHint(false)
    if (opt.correct) {
      setDetour(null)
      setFeedback(opt.explanation)
      if (opt.finding) {
        setLogs((l) => [...l, { stage: step.title, finding: opt.finding, image: opt.image, caption: opt.imageCaption }])
      }
      setStepIdx((i) => i + 1)
    } else {
      setDetour(opt)
      bodyRef.current?.scrollTo({ top: bodyRef.current.scrollHeight, behavior: 'smooth' })
    }
  }

  const restart = () => {
    setStepIdx(0)
    setLogs([])
    setDetour(null)
    setFeedback('')
    setShowHint(false)
    setOptions(data.steps.map((s) => shuffle(s.options)))
    bodyRef.current?.scrollTo({ top: 0 })
  }

  const zone = data?.zone ?? (caseId.startsWith('S') ? 'yellow' : 'green')

  return (
    <div className="drawer-layer">
      <div className="backdrop" onClick={onClose} aria-hidden="true" />
      <aside className={`drawer drawer-${zone}`} role="dialog" aria-modal="true" aria-labelledby="drawer-title">
        <div className="drawer-head">
          <div>
            <div className="drawer-kicker">
              <span className={`zone-pill zone-pill-${zone}`}>
                {zone === 'yellow' ? 'Sarı Alan · Acil Gözlem' : 'Yeşil Alan · Poliklinik'}
              </span>
              {data && <span className="drawer-category">{data.category}</span>}
            </div>
            <h2 id="drawer-title" className="drawer-title">
              {caseId}
              {data && (
                <>
                  {' '}
                  · {data.age} {data.gender}
                </>
              )}
            </h2>
          </div>
          <button ref={closeRef} className="icon-button" onClick={onClose} aria-label="Kapat">
            ✕
          </button>
        </div>

        {total > 0 && (
          <div className="progress" aria-hidden="true">
            {data.steps.map((s, i) => (
              <span key={i} className={i < stepIdx ? 'done' : i === stepIdx ? 'current' : ''} />
            ))}
          </div>
        )}

        <div className="drawer-body" ref={bodyRef}>
          {error && <p className="error">{error}</p>}
          {!data && !error && <p className="loading">Vaka dosyası açılıyor…</p>}

          {data && (
            <>
              <section className="sheet">
                <p className="sheet-label">Başvuru şikayeti</p>
                <p className="complaint">{data.complaint}</p>
              </section>

              <section className="sheet sheet-vitals">
                <p className="sheet-label">Triyaj kaydı · Geliş vital bulguları</p>
                <div className="vitals">
                  {data.vitals.map((v, i) => (
                    <Html key={i} html={v} className="vital" />
                  ))}
                </div>
              </section>

              <details className="sheet history" open>
                <summary className="sheet-label">Hasta öyküsü / anamnez</summary>
                <Html as="p" html={data.history} />
              </details>

              {logs.length > 0 && (
                <section className="logs">
                  <p className="section-label">Dosya notları & tetkik sonuçları</p>
                  {logs.map((log, i) => (
                    <div key={i} className="log">
                      <p className="log-stage">✓ {log.stage}</p>
                      <Html as="p" html={log.finding} />
                      {log.image && (
                        <figure className="log-figure">
                          <img src={`/${log.image}`} alt={log.caption} loading="lazy" />
                          <figcaption>{log.caption}</figcaption>
                        </figure>
                      )}
                    </div>
                  ))}
                </section>
              )}

              {finished ? (
                <section className="finale">
                  <p className="finale-kicker">Vaka tamamlandı</p>
                  <dl>
                    <dt>Kesin tanı</dt>
                    <dd>{data.diagnosis}</dd>
                    <dt>Taburculuk / yatış</dt>
                    <dd>{data.disposition}</dd>
                  </dl>
                  <div className="pearl">
                    <p className="sheet-label">Klinik inci</p>
                    <p>{data.pearl}</p>
                  </div>
                  <div className="finale-actions">
                    <button className="btn btn-primary" onClick={onClose}>
                      Arşive dön
                    </button>
                    <button className="btn" onClick={restart}>
                      Vakayı yeniden çöz
                    </button>
                  </div>
                </section>
              ) : (
                <section className="stage" ref={questionRef}>
                  <p className="stepper">
                    <span className="stepper-count">
                      Aşama {stepIdx + 1}/{total}
                    </span>
                    {data.steps[stepIdx].title}
                  </p>

                  {feedback && !detour && (
                    <div className="feedback">
                      <b>Doğru karar.</b> {feedback}
                    </div>
                  )}

                  <Html as="h3" className="question" html={data.steps[stepIdx].question} />

                  {detour ? (
                    <div className="detour">
                      <p className="detour-kicker">Klinik senaryo güncellemesi</p>
                      <p className="detour-choice">
                        Seçiminiz: <i>{detour.text}</i>
                      </p>
                      <div className="detour-box detour-what">
                        <b>Ne oldu?</b>
                        <Html as="p" html={detour.scenario} />
                      </div>
                      <div className="detour-box detour-teach">
                        <b>Rehber noktası</b>
                        <Html as="p" html={detour.teaching} />
                      </div>
                      <button className="btn btn-primary btn-block" onClick={() => setDetour(null)}>
                        ↩ Kararı değiştir ve soruya dön
                      </button>
                    </div>
                  ) : (
                    <>
                      <ol className="options">
                        {options[stepIdx].map((opt, i) => (
                          <li key={opt.text}>
                            <button className="option" onClick={() => choose(opt)}>
                              <span className="option-letter">{String.fromCharCode(65 + i)}</span>
                              <span>{opt.text}</span>
                            </button>
                          </li>
                        ))}
                      </ol>
                      <button className="link-button hint-toggle" onClick={() => setShowHint((h) => !h)}>
                        {showHint ? 'İpucunu gizle' : 'Klinik ipucu al'}
                      </button>
                      {showHint && (
                        <div className="hint">
                          {(() => {
                            const co = options[stepIdx].find((o) => o.correct)
                            return (
                              <>
                                <p>
                                  <b>Doğru yaklaşım:</b> {co.text}
                                </p>
                                <p>
                                  <b>Gerekçe:</b> {co.explanation}
                                </p>
                              </>
                            )
                          })()}
                        </div>
                      )}
                    </>
                  )}
                </section>
              )}
            </>
          )}
        </div>
      </aside>
    </div>
  )
}
