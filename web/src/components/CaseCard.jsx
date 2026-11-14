import { memo } from 'react'

function CaseCard({ item, solved, onOpen, onTag, onPrefetch, activeTags }) {
  const zoneLabel = item.zone === 'yellow' ? 'Sarı Alan' : 'Yeşil Alan'
  const open = () => onOpen(item.id)

  return (
    <article
      className={`card card-${item.zone}${solved ? ' card-solved' : ''}`}
      onPointerEnter={() => onPrefetch(item.id)}
    >
      <button className="card-hit" onClick={open} aria-label={`${item.id} vakasını aç: ${item.complaint}`} />
      <div className="card-top">
        <span className="card-id">{item.id}</span>
        <span className={`zone-pill zone-pill-${item.zone}`}>{zoneLabel}</span>
      </div>
      <h2 className="card-title">
        {item.age} {item.gender}
        {solved && <span className="solved-mark" title="Çözüldü">✓</span>}
      </h2>
      <p className="card-category">{item.category}</p>
      <p className="card-complaint">{item.complaint}</p>
      <div className="card-tags">
        {(solved ? [...item.tags, ...item.systemTags] : item.tags).map((t) => {
          const active = activeTags.includes(t)
          return (
            <button
              key={t}
              className={`tag${active ? ' is-active' : ''}`}
              aria-pressed={active}
              title={active ? 'Filtreden çıkar' : 'Filtreye ekle'}
              onClick={() => onTag(t)}
            >
              {t}
            </button>
          )
        })}
      </div>
      <div className="card-foot" aria-hidden="true">
        <span>{solved ? 'Yeniden çöz' : 'İncele & çöz'}</span>
        <span className="arrow">→</span>
      </div>
    </article>
  )
}

export default memo(CaseCard)
