import React from "react";
import {
  AlertTriangle,
  CheckCircle2,
  ClipboardCheck,
  Compass,
  HeartPulse,
  ShieldAlert,
  Stethoscope,
  Timer,
} from "lucide-react";

const URGENCY_LABELS = {
  CRITICAL: { label: "KRİTİK / ACİL MÜDAHALE", badgeClass: "badge-rose" },
  URGENT: { label: "ÖNCELİKLİ DEĞERLENDİRME", badgeClass: "badge-amber" },
  ROUTINE: { label: "RUTİN / STABİL", badgeClass: "badge-emerald" },
  UNASSESSED: { label: "EKG HENÜZ YORUMLANMADI", badgeClass: "badge-muted" },
};
// Model beklenmeyen/eksik bir aciliyet döndürürse "RUTİN" varsaymak yanlış güvence verir
const URGENCY_UNKNOWN = { label: "ACİLİYET BELİRTİLMEDİ — HEKİM DEĞERLENDİRMELİ", badgeClass: "badge-amber" };

const TERRITORY_STATUS = {
  ABNORMAL: { label: "ANORMAL", cls: "badge-rose" },
  RECIPROCAL: { label: "RESİPROKAL", cls: "badge-amber" },
  NORMAL: { label: "NORMAL", cls: "badge-emerald" },
  UNASSESSED: { label: "DEĞERLENDİRİLMEDİ", cls: "badge-muted" },
};

const CALIBRATION_STATUS = {
  ADEQUATE: { label: "YETERLİ", cls: "badge-emerald" },
  SUBOPTIMAL: { label: "SUBOPTİMAL", cls: "badge-amber" },
  UNASSESSED: { label: "DOĞRULANMADI", cls: "badge-muted" },
};

const upper = (v) => String(v ?? "").trim().toUpperCase();

// LLM çıktısı şemaya her zaman uymaz (metin yerine nesne/dizi gelebilir). React nesneleri doğrudan
// çizemediği için tüm rapor çökmesin diye her değer güvenli metne çevrilir.
function fmt(value) {
  if (value === null || value === undefined || value === "") return "—";
  if (typeof value === "string" || typeof value === "number") return value;
  if (typeof value === "boolean") return value ? "Evet" : "Hayır";
  if (Array.isArray(value)) return value.map(fmt).join(", ");
  try {
    return Object.entries(value)
      .map(([k, v]) => `${k}: ${fmt(v)}`)
      .join("; ");
  } catch {
    return String(value);
  }
}

const asList = (value) =>
  Array.isArray(value) ? value.filter((v) => v !== null && v !== undefined && v !== "") : value ? [value] : [];

const asObjects = (value, textKey) =>
  asList(value).map((item) => (item && typeof item === "object" ? item : { [textKey]: item }));

export default function ReasoningStepper({ analysis }) {
  if (!analysis) {
    return (
      <div className="panel">
        <div className="panel-header">
          <h2 className="panel-title">
            <Stethoscope size={16} color="#22d3ee" />
            6 Adımlı Klinik Muhakeme Raporu (ECG-Reasoning Protokolü)
          </h2>
          <span className="badge badge-muted">Analiz Bekleniyor</span>
        </div>
        <div style={{ fontSize: "0.84rem", color: "#94a3b8", lineHeight: 1.55 }}>
          EKG görüntüsünü yükleyip (isteğe bağlı olarak dijital pergelle PR/QRS/QT ölçümü
          ekledikten sonra) <strong>&quot;6 Adımlı Klinik Analizi Başlat&quot;</strong> butonuna
          tıklayın. Sistem kalibrasyon, ritim, eksen, aralıklar, anatomik ST-T morfolojisi ve
          kılavuz eşleştirmesini adım adım raporlayacaktır.
        </div>
      </div>
    );
  }

  const s1 = analysis.step1_calibration_quality || {};
  const s2 = analysis.step2_rate_rhythm || {};
  const s3 = analysis.step3_axis || {};
  const s4 = analysis.step4_intervals || {};
  const s5 = analysis.step5_morphology_st_t || {};
  const s6 = analysis.step6_clinical_synthesis || {};
  const qtc = analysis.computed_qtc;

  const urgencyKey = upper(s6.urgency);
  const urgencyInfo = URGENCY_LABELS[urgencyKey] || URGENCY_UNKNOWN;
  const urgencyClass = URGENCY_LABELS[urgencyKey] ? urgencyKey : "URGENT";
  const calibInfo = CALIBRATION_STATUS[upper(s1.status)] || CALIBRATION_STATUS.UNASSESSED;
  const confidence = Number(s6.confidence_score);

  const redFlags = asList(s6.red_flags);
  const findings = asList(s1.findings);
  const territories = asObjects(s5.territories, "wall");
  const actions = asList(s6.recommended_actions);
  const guidelineMatches = asList(s6.guideline_matches);
  const differentials = asObjects(s6.differential_diagnoses, "diagnosis");
  const erbSteps = asObjects(analysis.erb_reasoning_chain?.steps, "criterion_selection");

  return (
    <div className="panel">
      <div className="panel-header">
        <h2 className="panel-title">
          <Stethoscope size={16} color="#22d3ee" />
          6 Adımlı Klinik Muhakeme Raporu
        </h2>
        <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
          <span
            className={`badge ${
              analysis.mode === "live_llm" ? "badge-emerald" : "badge-amber"
            }`}
          >
            {analysis.mode === "live_llm" ? "Canlı LLM Görsel Analiz" : "Demo / Simülasyon Modu"}
          </span>
          {analysis.model_used && <span className="badge badge-muted">{analysis.model_used}</span>}
        </div>
      </div>

      {analysis.fallback_note && (
        <div
          style={{
            marginBottom: 12,
            padding: "9px 12px",
            borderRadius: 8,
            background: "rgba(245, 158, 11, 0.12)",
            border: "1px solid rgba(245, 158, 11, 0.35)",
            fontSize: "0.78rem",
            color: "#fbbf24",
          }}
        >
          {analysis.fallback_note}
        </div>
      )}

      {/* Üst Tanı Özeti */}
      <div className={`diagnosis-hero urgency-${urgencyClass}`}>
        <div
          style={{
            display: "flex",
            alignItems: "flex-start",
            justifyContent: "space-between",
            gap: 12,
            flexWrap: "wrap",
          }}
        >
          <div>
            <div style={{ fontSize: "0.74rem", color: "#94a3b8", marginBottom: 4 }}>
              BİRİNCİL KLİNİK SENTEZ
            </div>
            <div style={{ fontSize: "1.18rem", fontWeight: 700, color: "#f8fafc" }}>
              {s6.primary_diagnosis ? fmt(s6.primary_diagnosis) : "Tanı sentezi üretilmedi"}
            </div>
          </div>

          <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
            <span className={`badge ${urgencyInfo.badgeClass}`}>{urgencyInfo.label}</span>
            {Number.isFinite(confidence) && confidence > 0 && (
              <span className="badge badge-cyan mono">Güven: %{Math.round(confidence)}</span>
            )}
          </div>
        </div>
      </div>

      {/* Kırmızı Bayraklar */}
      {redFlags.length > 0 && (
        <div className="red-flag-box">
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 7,
              fontWeight: 700,
              fontSize: "0.84rem",
              color: "#fb7185",
              marginBottom: 5,
            }}
          >
            <ShieldAlert size={16} />
            Kırmızı Bayraklar & Acil Uyarılar
          </div>
          <ul className="list-clean" style={{ color: "#ffe4e6" }}>
            {redFlags.map((rf, i) => (
              <li key={i}>{fmt(rf)}</li>
            ))}
          </ul>
        </div>
      )}

      {/* 6 Adımlı Kart Gridi */}
      <div className="steps-grid">
        {/* Adım 1 */}
        <div className="step-card">
          <div className="step-head">
            <span className="step-num">Adım 1 — Kalibrasyon & Kalite</span>
            <span className={`badge ${calibInfo.cls}`}>{calibInfo.label}</span>
          </div>
          <div className="kv-list">
            <div className="kv-row">
              <span className="kv-key">Hız / Kazanç</span>
              <span className="kv-val">{fmt(s1.paper_speed_and_gain)}</span>
            </div>
            <div className="kv-row">
              <span className="kv-key">Görüntü Notu</span>
              <span className="kv-val">{fmt(s1.image_quality_notes)}</span>
            </div>
          </div>
          {findings.length > 0 && (
            <ul className="list-clean" style={{ color: "#cbd5e1" }}>
              {findings.map((f, i) => (
                <li key={i}>{fmt(f)}</li>
              ))}
            </ul>
          )}
        </div>

        {/* Adım 2 */}
        <div className="step-card">
          <div className="step-head">
            <span className="step-num">Adım 2 — Hız & Ritim</span>
            <HeartPulse size={15} color="#22d3ee" />
          </div>
          <div className="kv-list">
            <div className="kv-row">
              <span className="kv-key">Kalp Hızı</span>
              <span className="kv-val mono">
                {s2.heart_rate_bpm ? `${fmt(s2.heart_rate_bpm)} atım/dk` : "Belirtilmedi"}
              </span>
            </div>
            <div className="kv-row">
              <span className="kv-key">Ritim Düzeni</span>
              <span className="kv-val">{fmt(s2.rhythm_regularity)}</span>
            </div>
            <div className="kv-row">
              <span className="kv-key">P Dalgası</span>
              <span className="kv-val">{fmt(s2.p_wave_assessment)}</span>
            </div>
            <div className="kv-row">
              <span className="kv-key">AV İlişki</span>
              <span className="kv-val">{fmt(s2.av_relationship)}</span>
            </div>
          </div>
          {s2.summary && (
            <div style={{ marginTop: 8, fontSize: "0.8rem", color: "#38bdf8" }}>{fmt(s2.summary)}</div>
          )}
        </div>

        {/* Adım 3 */}
        <div className="step-card">
          <div className="step-head">
            <span className="step-num">Adım 3 — Kardiyak Eksen</span>
            <Compass size={15} color="#22d3ee" />
          </div>
          <div className="kv-list">
            <div className="kv-row">
              <span className="kv-key">Eksen</span>
              <span className="kv-val" style={{ fontWeight: 600 }}>
                {fmt(s3.axis_classification)}
              </span>
            </div>
            <div className="kv-row">
              <span className="kv-key">Derivasyon I</span>
              <span className="kv-val">{fmt(s3.lead_i_polarity)}</span>
            </div>
            <div className="kv-row">
              <span className="kv-key">Derivasyon aVF</span>
              <span className="kv-val">{fmt(s3.lead_avf_polarity)}</span>
            </div>
          </div>
          {s3.summary && (
            <div style={{ marginTop: 8, fontSize: "0.8rem", color: "#cbd5e1" }}>{fmt(s3.summary)}</div>
          )}
        </div>

        {/* Adım 4 */}
        <div className="step-card">
          <div className="step-head">
            <span className="step-num">Adım 4 — İletim Aralıkları</span>
            <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
              {s4.caliper_used === true && <span className="badge badge-cyan">Pergel Referanslı</span>}
              <Timer size={15} color="#22d3ee" />
            </div>
          </div>
          <div className="kv-list">
            <div className="kv-row">
              <span className="kv-key">PR Aralığı</span>
              <span className="kv-val mono">{fmt(s4.pr_interval_ms)}</span>
            </div>
            <div className="kv-row">
              <span className="kv-key">QRS Süresi</span>
              <span className="kv-val mono">{fmt(s4.qrs_duration_ms)}</span>
            </div>
            <div className="kv-row">
              <span className="kv-key">QT / QTc</span>
              <span className="kv-val mono">{fmt(s4.qt_qtc_ms)}</span>
            </div>
          </div>
          {qtc && (
            <div
              className="mono"
              style={{
                marginTop: 8,
                padding: "6px 9px",
                borderRadius: 7,
                background: "rgba(16, 185, 129, 0.1)",
                border: "1px solid rgba(16, 185, 129, 0.3)",
                fontSize: "0.75rem",
                color: "#6ee7b7",
              }}
            >
              QTc (uygulama hesabı): Bazett {qtc.qtc_bazett_ms} ms | Fridericia {qtc.qtc_fridericia_ms} ms
              {qtc.recommended_formula ? ` | Esas alınan: ${qtc.recommended_formula}` : ""} —{" "}
              {qtc.interpretation}
            </div>
          )}
          {s4.summary && (
            <div style={{ marginTop: 8, fontSize: "0.8rem", color: "#cbd5e1" }}>{fmt(s4.summary)}</div>
          )}
        </div>

        {/* Adım 5 */}
        <div className="step-card span-2">
          <div className="step-head">
            <span className="step-num">Adım 5 — Anatomik Duvar Morfolojisi (ST / T / Q)</span>
          </div>
          {territories.length > 0 && (
            <div style={{ overflowX: "auto" }}>
              <table className="territory-table">
                <thead>
                  <tr>
                    <th>Anatomik Duvar</th>
                    <th>ST Segmenti</th>
                    <th>T Dalgası</th>
                    <th>Q Dalgası</th>
                    <th>Durum</th>
                  </tr>
                </thead>
                <tbody>
                  {territories.map((t, idx) => {
                    const st = TERRITORY_STATUS[upper(t.status)] || TERRITORY_STATUS.UNASSESSED;
                    return (
                      <tr key={idx}>
                        <td style={{ fontWeight: 600, color: "#e2e8f0" }}>{fmt(t.wall)}</td>
                        <td>{fmt(t.st_segment)}</td>
                        <td>{fmt(t.t_wave)}</td>
                        <td>{fmt(t.q_wave)}</td>
                        <td>
                          <span className={`badge ${st.cls}`}>{st.label}</span>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          )}
          {s5.summary && (
            <div style={{ marginTop: 10, fontSize: "0.82rem", color: "#38bdf8" }}>{fmt(s5.summary)}</div>
          )}
        </div>

        {/* Adım 6 */}
        <div className="step-card span-2">
          <div className="step-head">
            <span className="step-num">Adım 6 — Ayırıcı Tanı, Kılavuz Eşleşmesi & Klinik Aksiyon</span>
            <ClipboardCheck size={16} color="#10b981" />
          </div>

          <div className="steps-grid" style={{ marginTop: 6 }}>
            <div>
              <div style={{ fontSize: "0.78rem", fontWeight: 700, color: "#94a3b8", marginBottom: 6 }}>
                ÖNERİLEN KLİNİK AKSİYONLAR
              </div>
              <ul className="list-clean">
                {actions.map((act, i) => (
                  <li key={i} style={{ display: "flex", alignItems: "flex-start", gap: 6 }}>
                    <CheckCircle2 size={14} color="#10b981" style={{ marginTop: 3, flexShrink: 0 }} />
                    <span>{fmt(act)}</span>
                  </li>
                ))}
              </ul>

              {guidelineMatches.length > 0 && (
                <>
                  <div
                    style={{
                      fontSize: "0.78rem",
                      fontWeight: 700,
                      color: "#94a3b8",
                      marginTop: 12,
                      marginBottom: 4,
                    }}
                  >
                    EŞLEŞEN ESC/AHA KILAVUZ KRİTERLERİ
                  </div>
                  <ul className="list-clean" style={{ color: "#cbd5e1" }}>
                    {guidelineMatches.map((g, i) => (
                      <li key={i}>{fmt(g)}</li>
                    ))}
                  </ul>
                </>
              )}
            </div>

            <div>
              <div style={{ fontSize: "0.78rem", fontWeight: 700, color: "#94a3b8", marginBottom: 6 }}>
                AYIRICI TANI DEĞERLENDİRMESİ
              </div>
              {differentials.length > 0 ? (
                <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                  {differentials.map((dd, i) => (
                    <div
                      key={i}
                      style={{
                        padding: "8px 10px",
                        borderRadius: 8,
                        background: "#090f1e",
                        border: "1px solid rgba(148,163,184,0.14)",
                        fontSize: "0.8rem",
                      }}
                    >
                      <div
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                          gap: 8,
                          fontWeight: 600,
                        }}
                      >
                        <span>{fmt(dd.diagnosis)}</span>
                        <span className="badge badge-muted">{fmt(dd.likelihood)}</span>
                      </div>
                      <div style={{ color: "#94a3b8", fontSize: "0.76rem", marginTop: 3 }}>
                        {fmt(dd.rationale)}
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div style={{ fontSize: "0.8rem", color: "#94a3b8" }}>
                  Belirgin alternatif ayırıcı tanı listelenmedi.
                </div>
              )}
            </div>
          </div>
        </div>

        {/* ECG-Reasoning-Benchmark Doğrulama Zinciri */}
        {erbSteps.length > 0 && (
          <div className="step-card span-2">
            <div className="step-head">
              <span className="step-num">
                ECG-Reasoning-Benchmark Doğrulama Zinciri (Criterion → Finding → Visual Grounding → Decision)
              </span>
              {analysis.erb_reasoning_chain.target_dx && (
                <span className="badge badge-cyan mono">{fmt(analysis.erb_reasoning_chain.target_dx)}</span>
              )}
            </div>

            <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
              {erbSteps.map((erbStep, idx) => (
                <div
                  key={idx}
                  style={{
                    padding: "10px 12px",
                    borderRadius: 9,
                    background: "#090f1e",
                    border: "1px solid rgba(34, 211, 238, 0.2)",
                    fontSize: "0.8rem",
                  }}
                >
                  <div
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      alignItems: "center",
                      gap: 10,
                      flexWrap: "wrap",
                      marginBottom: 6,
                    }}
                  >
                    <strong style={{ color: "#e2e8f0" }}>
                      Kriter {idx + 1}: {fmt(erbStep.criterion_selection)}
                    </strong>
                    <span
                      className={`badge ${
                        /doğrulandı/i.test(String(erbStep.diagnostic_decision))
                          ? "badge-emerald"
                          : /dışlandı/i.test(String(erbStep.diagnostic_decision))
                          ? "badge-rose"
                          : "badge-amber"
                      }`}
                    >
                      {fmt(erbStep.diagnostic_decision)}
                    </span>
                  </div>
                  <div style={{ color: "#cbd5e1", marginBottom: 6 }}>
                    <strong>Bulgu Doğrulaması:</strong> {fmt(erbStep.finding_identification)}
                  </div>
                  {erbStep.ecg_grounding && typeof erbStep.ecg_grounding === "object" && (
                    <div
                      className="mono"
                      style={{
                        display: "flex",
                        flexWrap: "wrap",
                        gap: 8,
                        fontSize: "0.74rem",
                        color: "#38bdf8",
                      }}
                    >
                      {asList(erbStep.ecg_grounding.lead_grounding).length > 0 && (
                        <span className="badge badge-muted">
                          Derivasyon: {fmt(asList(erbStep.ecg_grounding.lead_grounding))}
                        </span>
                      )}
                      {erbStep.ecg_grounding.wave_grounding && (
                        <span className="badge badge-muted">
                          Dalga/Segment: {fmt(erbStep.ecg_grounding.wave_grounding)}
                        </span>
                      )}
                      {erbStep.ecg_grounding.measurement_grounding && (
                        <span className="badge badge-cyan">
                          Ölçüm: {fmt(erbStep.ecg_grounding.measurement_grounding)}
                        </span>
                      )}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      {analysis.disclaimer && (
        <div
          style={{
            marginTop: 12,
            display: "flex",
            alignItems: "center",
            gap: 8,
            fontSize: "0.74rem",
            color: "#64748b",
          }}
        >
          <AlertTriangle size={14} color="#64748b" />
          <span>{analysis.disclaimer}</span>
        </div>
      )}
    </div>
  );
}
