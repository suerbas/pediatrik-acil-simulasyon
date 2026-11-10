import { useMemo, useState } from 'react'
import { SHIFTS, buildShiftPlan, clock, duration } from './plan.js'

const MAX_PEOPLE = 20
const PART_OPTIONS = [
  { value: 1, label: 'Tek blok' },
  { value: 2, label: "2'ye böl" },
  { value: 3, label: "3'e böl" },
]

function Stepper({ value, onChange, min = 0, max = MAX_PEOPLE }) {
  const set = (v) => onChange(Math.max(min, Math.min(max, v)))
  return (
    <div className="stepper">
      <button type="button" onClick={() => set(value - 1)} disabled={value <= min} aria-label="Azalt">−</button>
      <input
        type="number"
        inputMode="numeric"
        min={min}
        max={max}
        value={value}
        onChange={(e) => set(parseInt(e.target.value, 10) || 0)}
      />
      <button type="button" onClick={() => set(value + 1)} disabled={value >= max} aria-label="Artır">+</button>
    </div>
  )
}

function ShiftSettings({ shift, count, setCount, parts, setParts }) {
  return (
    <div className="setting">
      <div className="setting-head">
        <h2>{shift.label}</h2>
        <span className="muted">{clock(shift.start)} – {clock(shift.end)}</span>
      </div>
      <label className="field">
        <span>Kişi sayısı</span>
        <Stepper value={count} onChange={setCount} />
      </label>
      <div className="field">
        <span>Paylaşım şekli</span>
        <div className="segmented" role="radiogroup">
          {PART_OPTIONS.map((o) => (
            <button
              key={o.value}
              type="button"
              role="radio"
              aria-checked={parts === o.value}
              className={parts === o.value ? 'active' : ''}
              onClick={() => setParts(o.value)}
            >
              {o.label}
            </button>
          ))}
        </div>
      </div>
      {parts > 1 && count >= 2 && (
        <p className="hint">
          {count} kişi, {count * parts} kişilik gibi planlanır. Herkes her alanda {parts} ayrı blok alır.
        </p>
      )}
    </div>
  )
}

function ShiftResult({ plan }) {
  const { shift, slots, summary, error, people } = plan
  if (people.length === 0) return null
  return (
    <section className="card">
      <div className="card-head">
        <h2>{shift.label}</h2>
        <span className="muted">{clock(shift.start)} – {clock(shift.end)} · {people.length} kişi</span>
      </div>

      {error ? (
        <p className="warning">{error}</p>
      ) : (
        <>
          <div className="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Saat</th>
                  <th>Süre</th>
                  <th className="green-h">Yeşil</th>
                  <th className="yellow-h">Sarı</th>
                </tr>
              </thead>
              <tbody>
                {slots.map((s, i) => (
                  <tr key={i}>
                    <td className="nowrap">{clock(s.start)} – {clock(s.end)}</td>
                    <td className="muted small">{duration(s.minutes)}</td>
                    <td><span className="pill green">{s.green}</span></td>
                    <td><span className="pill yellow">{s.yellow}</span></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <h3>Kişi bazında</h3>
          <div className="people">
            {summary.map((p) => (
              <div key={p.name} className="person">
                <div className="person-head">
                  <span className="badge">{p.name}</span>
                  <span className="muted small">Toplam {duration(p.totalMin)}</span>
                </div>
                <ul>
                  {[...p.green.map((s) => ({ ...s, area: 'green' })), ...p.yellow.map((s) => ({ ...s, area: 'yellow' }))]
                    .sort((a, b) => a.start - b.start)
                    .map((s, i) => (
                      <li key={i}>
                        <span className={`dot ${s.area}`} />
                        <span className="area">{s.area === 'green' ? 'Yeşil' : 'Sarı'}</span>
                        <span className="nowrap">{clock(s.start)} – {clock(s.end)}</span>
                      </li>
                    ))}
                </ul>
              </div>
            ))}
          </div>
        </>
      )}
    </section>
  )
}

export default function App() {
  const [morning, setMorning] = useState(4)
  const [evening, setEvening] = useState(3)
  const [morningParts, setMorningParts] = useState(1)
  const [eveningParts, setEveningParts] = useState(1)

  const morningPlan = useMemo(
    () => buildShiftPlan(SHIFTS.sabah, morning, morningParts, 0),
    [morning, morningParts],
  )
  const eveningPlan = useMemo(
    () => buildShiftPlan(SHIFTS.aksam, evening, eveningParts, morning),
    [evening, eveningParts, morning],
  )

  return (
    <div className="app">
      <header>
        <h1>Mesai Planlayıcı</h1>
        <p className="muted">
          Yeşil ve sarı alan için eşit, çakışmasız mesai paylaşımı. Harfler, paylaşım sonrası kişiler arasında seçilir.
        </p>
      </header>

      <section className="card settings">
        <ShiftSettings shift={SHIFTS.sabah} count={morning} setCount={setMorning} parts={morningParts} setParts={setMorningParts} />
        <ShiftSettings shift={SHIFTS.aksam} count={evening} setCount={setEvening} parts={eveningParts} setParts={setEveningParts} />
      </section>

      <ShiftResult plan={morningPlan} />
      <ShiftResult plan={eveningPlan} />

      {morning === 0 && evening === 0 && <p className="muted center">Plan oluşturmak için kişi sayısı girin.</p>}
    </div>
  )
}
