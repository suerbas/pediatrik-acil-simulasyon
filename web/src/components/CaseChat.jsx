import { useEffect, useRef, useState } from 'react'

// Modelin döndürdüğü basit markdown'ı (kalın, madde, satır sonu) güvenli biçimde gösterir.
function Rich({ text }) {
  const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  const html = text
    .split('\n')
    .map((line) => {
      let l = esc(line).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>')
      if (/^\s*[-*•]\s+/.test(line)) l = `<span class="chat-bullet">•</span> ${l.replace(/^\s*[-*•]\s+/, '')}`
      return l
    })
    .join('<br>')
  return <p className="chat-text" dangerouslySetInnerHTML={{ __html: html }} />
}

// Model kimliğini okunur ada çevirir: "google/gemma-4-31b-it:free" -> "Gemma 4 31B", "gemini-3.8-flash" -> "Gemini 3.8 Flash"
const MODEL_NAMES = {
  'google/gemma-4-31b-it': 'Gemma 4 31B',
  'nvidia/nemotron-3-ultra-550b-a55b': 'Nemotron 3 Ultra',
  'nvidia/nemotron-3.5-super-vl': 'Nemotron 3.5 Super VL',
  'baidu/ernie-5.5-flash-preview': 'ERNIE 5.5 Flash',
}
function modelLabel(id) {
  const base = id.replace(/:free$/, '')
  if (MODEL_NAMES[base]) return `${MODEL_NAMES[base]} · OpenRouter`
  if (base.startsWith('gemini-')) return base.split('-').map((w) => (/^\d/.test(w) ? w : w[0].toUpperCase() + w.slice(1))).join(' ')
  return base
}

const SUGGESTIONS = ['Ayırıcı tanıda neleri düşünmeliyim?', 'Bu aşamada hangi kırmızı bayraklara bakmalıyım?']

export default function CaseChat({ caseId, step, finished }) {
  const [open, setOpen] = useState(false)
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')
  const [errorDetail, setErrorDetail] = useState('')
  const listRef = useRef(null)
  const inputRef = useRef(null)

  useEffect(() => {
    listRef.current?.scrollTo({ top: listRef.current.scrollHeight, behavior: 'smooth' })
  }, [messages, busy])

  useEffect(() => {
    if (open) inputRef.current?.focus()
  }, [open])

  const send = async (text) => {
    const q = text.trim()
    if (!q || busy) return
    const next = [...messages, { role: 'user', text: q }]
    setMessages(next)
    setInput('')
    setError('')
    setErrorDetail('')
    setBusy(true)
    try {
      const r = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ caseId, step, messages: next }),
      })
      const data = await r.json().catch(() => ({}))
      if (!r.ok) {
        setErrorDetail(data.detail || '')
        throw new Error(data.error || 'Asistan şu an yanıt veremiyor.')
      }
      setMessages((m) => [...m, { role: 'model', text: data.reply, model: data.model }])
    } catch (e) {
      setError(e.message === 'Failed to fetch' ? 'Bağlantı kurulamadı.' : e.message)
      setMessages((m) => m.slice(0, -1))
      setInput(q)
    } finally {
      setBusy(false)
    }
  }

  const onKey = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      send(input)
    }
  }

  return (
    <section className={`chat${open ? ' is-open' : ''}`}>
      <button className="chat-toggle" onClick={() => setOpen((o) => !o)} aria-expanded={open}>
        <span className="chat-toggle-icon" aria-hidden="true">
          ?
        </span>
        <span>
          <b>Vaka asistanına soru sor</b>
          <small>{finished ? 'Vaka tamamlandı, tanı dahil her şey konuşulabilir' : 'Cevabı söylemez, düşünmene yardım eder'}</small>
        </span>
        <span className="chat-chevron" aria-hidden="true">
          {open ? '▾' : '▸'}
        </span>
      </button>

      {open && (
        <div className="chat-panel">
          <div className="chat-list" ref={listRef} aria-live="polite">
            {messages.length === 0 && (
              <div className="chat-empty">
                <p>Bu vakayla ilgili aklına takılanı sor. Örneğin:</p>
                <div className="chat-suggestions">
                  {SUGGESTIONS.map((s) => (
                    <button key={s} className="chat-chip" onClick={() => send(s)} disabled={busy}>
                      {s}
                    </button>
                  ))}
                </div>
              </div>
            )}
            {messages.map((m, i) => (
              <div key={i} className={`chat-msg chat-${m.role}`}>
                {m.role === 'user' ? (
                  <p className="chat-text">{m.text}</p>
                ) : (
                  <>
                    <Rich text={m.text} />
                    {m.model && <p className="chat-model-tag">({modelLabel(m.model)})</p>}
                  </>
                )}
              </div>
            ))}
            {busy && (
              <div className="chat-msg chat-model chat-typing" aria-label="Yanıt yazılıyor">
                <span />
                <span />
                <span />
              </div>
            )}
          </div>

          {error && (
            <div className="chat-error">
              <p>{error}</p>
              {errorDetail && (
                <details>
                  <summary>Teknik ayrıntı</summary>
                  <p className="chat-error-detail">{errorDetail}</p>
                </details>
              )}
            </div>
          )}

          <form
            className="chat-form"
            onSubmit={(e) => {
              e.preventDefault()
              send(input)
            }}
          >
            <textarea
              ref={inputRef}
              rows={2}
              maxLength={800}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={onKey}
              placeholder="Sorunu yaz… (Enter gönderir, Shift+Enter yeni satır)"
              disabled={busy}
            />
            <button className="btn btn-primary" type="submit" disabled={busy || !input.trim()}>
              Gönder
            </button>
          </form>
          <p className="chat-note">
            Yapay zekâ yanıtları eğitim amaçlıdır ve hatalı olabilir; doz ve klinik kararlar için kılavuzlara başvurun.
            Gerçek hasta bilgisi yazmayın.
          </p>
        </div>
      )}
    </section>
  )
}
