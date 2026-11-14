import React, { useRef, useState } from "react";
import {
  BrainCircuit,
  Camera,
  FileImage,
  FolderOpen,
  Loader2,
  Sparkles,
  UploadCloud,
  UserCheck,
} from "lucide-react";

const COMPLAINT_CHIPS = [
  "Göğüs ağrısı",
  "Çarpıntı",
  "Senkop / Baş dönmesi",
  "Nefes darlığı",
  "Rutin kontrol",
];

export default function PatientContextForm({
  sampleCases,
  activeSampleId,
  onSelectSample,
  onUploadFile,
  patientContext,
  onChangePatient,
  caliperMeasurements,
  hasImage,
  isPreprocessing,
  isAnalyzing,
  onRunAnalysis,
}) {
  const [dragging, setDragging] = useState(false);
  const fileInputRef = useRef(null);
  const cameraInputRef = useRef(null);

  const handleFiles = (files, inputEl = null) => {
    if (files && files[0] && !isPreprocessing) {
      onUploadFile(files[0]);
    }
    if (inputEl) {
      inputEl.value = "";
    }
  };

  const updateField = (key, val) => {
    onChangePatient({ ...patientContext, [key]: val });
  };

  const caliperEntries = Object.entries(caliperMeasurements || {});

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
      {/* EKG Yükleme & Hazır Demo Vakalar */}
      <div className="panel">
        <div className="panel-header">
          <h2 className="panel-title">
            <FileImage size={16} color="#22d3ee" />
            1. EKG Görüntü Kaynağı
          </h2>
          {isPreprocessing && (
            <span className="badge badge-cyan">
              <Loader2 size={12} className="spin" />
              İşleniyor...
            </span>
          )}
        </div>

        <div
          className={`dropzone ${dragging ? "dragging" : ""}`}
          onClick={() => fileInputRef.current?.click()}
          onDragOver={(e) => {
            e.preventDefault();
            setDragging(true);
          }}
          onDragLeave={() => setDragging(false)}
          onDrop={(e) => {
            e.preventDefault();
            setDragging(false);
            handleFiles(e.dataTransfer.files);
          }}
        >
          <input
            ref={fileInputRef}
            type="file"
            accept="image/*"
            style={{ display: "none" }}
            onChange={(e) => handleFiles(e.target.files, e.target)}
          />
          <input
            ref={cameraInputRef}
            type="file"
            accept="image/*"
            capture="environment"
            style={{ display: "none" }}
            onChange={(e) => handleFiles(e.target.files, e.target)}
          />
          <UploadCloud size={26} color="#22d3ee" style={{ marginBottom: 6 }} />
          <div style={{ fontSize: "0.84rem", fontWeight: 600 }}>
            EKG Fotoğrafı Yükle / Sürükle-Bırak
          </div>
          <div style={{ fontSize: "0.73rem", color: "#94a3b8", marginTop: 3 }}>
            PNG, JPG, WEBP veya mobil arka kamera çekimi
          </div>
        </div>

        <div className="field-row" style={{ marginBottom: 12 }}>
          <button
            type="button"
            className="btn btn-primary btn-sm"
            onClick={() => cameraInputRef.current?.click()}
            disabled={isPreprocessing}
          >
            <Camera size={14} />
            Kamerayla EKG Çek
          </button>
          <button
            type="button"
            className="btn btn-sm"
            onClick={() => fileInputRef.current?.click()}
            disabled={isPreprocessing}
          >
            <FolderOpen size={14} />
            Galeriden / Dosyadan Seç
          </button>
        </div>

        <div className="field-label" style={{ marginBottom: 7, display: "flex", alignItems: "center", gap: 5 }}>
          <Sparkles size={13} color="#10b981" />
          Hızlı Test İçin Hazır Demo Vakaları
        </div>
        <div className="sample-list" style={{ marginBottom: 0 }}>
          {sampleCases.map((sc) => (
            <button
              key={sc.id}
              type="button"
              className={`sample-btn ${activeSampleId === sc.id ? "active" : ""}`}
              onClick={() => onSelectSample(sc.id)}
              disabled={isPreprocessing}
            >
              <div className="sample-title">{sc.title}</div>
              <div className="sample-sub">{sc.subtitle}</div>
            </button>
          ))}
        </div>
      </div>

      {/* Hasta Klinik Bilgileri & Analiz Başlatma */}
      <div className="panel">
        <div className="panel-header">
          <h2 className="panel-title">
            <UserCheck size={16} color="#22d3ee" />
            2. Hasta Klinik Bağlamı
          </h2>
        </div>

        <div className="field-row">
          <div className="field-group">
            <label className="field-label" htmlFor="age-input">
              Yaş
            </label>
            <input
              id="age-input"
              type="number"
              min="0"
              max="120"
              className="input"
              placeholder="Örn: 58"
              value={patientContext.age ?? ""}
              onChange={(e) => updateField("age", e.target.value)}
            />
          </div>

          <div className="field-group">
            <label className="field-label" htmlFor="sex-select">
              Cinsiyet
            </label>
            <select
              id="sex-select"
              className="select"
              value={patientContext.sex ?? "Belirtilmedi"}
              onChange={(e) => updateField("sex", e.target.value)}
            >
              <option value="Belirtilmedi">Belirtilmedi</option>
              <option value="Erkek">Erkek</option>
              <option value="Kadın">Kadın</option>
            </select>
          </div>
        </div>

        <div className="field-group">
          <label className="field-label" htmlFor="complaint-input">
            Başvuru Şikayeti
          </label>
          <input
            id="complaint-input"
            type="text"
            className="input"
            placeholder="Örn: 1 saattir göğüs ağrısı, terleme"
            value={patientContext.chief_complaint ?? ""}
            onChange={(e) => updateField("chief_complaint", e.target.value)}
          />
          <div className="chip-row">
            {COMPLAINT_CHIPS.map((c) => (
              <button
                key={c}
                type="button"
                className="chip"
                onClick={() => updateField("chief_complaint", c)}
              >
                {c}
              </button>
            ))}
          </div>
        </div>

        <div className="field-group">
          <label className="field-label" htmlFor="history-input">
            Özgeçmiş / Risk Faktörleri
          </label>
          <input
            id="history-input"
            type="text"
            className="input"
            placeholder="HT, DM, KAH, antikoagülan kullanımı..."
            value={patientContext.history ?? ""}
            onChange={(e) => updateField("history", e.target.value)}
          />
        </div>

        <div className="field-group">
          <label className="field-label" htmlFor="notes-input">
            Klinik Notlar / Vitaller
          </label>
          <textarea
            id="notes-input"
            className="textarea"
            placeholder="TA, SpO2, troponin veya ek hekim notu..."
            value={patientContext.notes ?? ""}
            onChange={(e) => updateField("notes", e.target.value)}
          />
        </div>

        {caliperEntries.length > 0 && (
          <div
            style={{
              padding: "8px 10px",
              borderRadius: 8,
              background: "rgba(34, 211, 238, 0.08)",
              border: "1px solid rgba(34, 211, 238, 0.25)",
              marginBottom: 12,
              fontSize: "0.76rem",
            }}
          >
            <div style={{ fontWeight: 600, color: "#22d3ee", marginBottom: 4 }}>
              LLM&apos;e Aktarılacak Pergel Ölçümleri:
            </div>
            <div className="mono" style={{ color: "#e2e8f0" }}>
              {caliperEntries.map(([k, v]) => `${k}: ${v}`).join(" • ")}
            </div>
          </div>
        )}

        <button
          type="button"
          className="btn btn-primary btn-full"
          disabled={!hasImage || isAnalyzing || isPreprocessing}
          onClick={onRunAnalysis}
        >
          {isAnalyzing ? (
            <>
              <Loader2 size={17} className="spin" />
              6 Adımlı Muhakeme Çalışıyor...
            </>
          ) : (
            <>
              <BrainCircuit size={17} />
              6 Adımlı Klinik Analizi Başlat
            </>
          )}
        </button>
      </div>
    </div>
  );
}
