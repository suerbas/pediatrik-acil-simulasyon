import React, { useEffect, useRef, useState } from "react";
import {
  Activity,
  AlertCircle,
  BookOpen,
  Calculator,
  Settings,
  X,
} from "lucide-react";

import EcgCanvasViewer from "./components/EcgCanvasViewer.jsx";
import LeadCropsGallery from "./components/LeadCropsGallery.jsx";
import PatientContextForm from "./components/PatientContextForm.jsx";
import ReasoningStepper from "./components/ReasoningStepper.jsx";
import {
  ANATOMICAL_TERRITORIES,
  calculateQtc,
  CLINICAL_CRITERIA_KB,
  ERB_BENCHMARK_TREES,
  SAMPLE_CASES,
} from "./utils/clinicalData.js";
import {
  analyzeEcgClientOrServer,
  fetchServerlessStatus,
  generateSyntheticEcgInBrowser,
  preprocessEcgInBrowser,
} from "./utils/ecgClientEngine.js";

const LOCAL_CFG_KEY = "ecg_helper_config";

const DEFAULT_LOCAL_CFG = {
  provider: "openrouter",
  openrouter_model: "google/gemini-3.8-flash",
  openrouter_base_url: "https://openrouter.ai/api/v1",
  openrouter_api_key: "",
  gemini_model: "gemini-2.0-flash",
  gemini_api_key: "",
  openai_model: "gpt-4o",
  openai_api_key: "",
};

function loadLocalConfig() {
  try {
    const raw = localStorage.getItem(LOCAL_CFG_KEY);
    if (!raw) return { ...DEFAULT_LOCAL_CFG };
    return { ...DEFAULT_LOCAL_CFG, ...JSON.parse(raw) };
  } catch {
    return { ...DEFAULT_LOCAL_CFG };
  }
}

function saveLocalConfig(cfg) {
  try {
    localStorage.setItem(LOCAL_CFG_KEY, JSON.stringify(cfg));
  } catch {
    // ignore storage quota errors
  }
}

const SECRET_KEYS = ["openrouter_api_key", "gemini_api_key", "openai_api_key"];

function buildPublicStatus(cfg) {
  const provider = cfg.provider || "openrouter";
  const hasOpenrouter = Boolean(cfg.openrouter_api_key);
  const hasGemini = Boolean(cfg.gemini_api_key);
  const hasOpenai = Boolean(cfg.openai_api_key);
  const active =
    provider === "openrouter" ? hasOpenrouter : provider === "gemini" ? hasGemini : hasOpenai;
  return {
    provider,
    openrouter_model: cfg.openrouter_model,
    openrouter_base_url: cfg.openrouter_base_url,
    gemini_model: cfg.gemini_model,
    openai_model: cfg.openai_model,
    has_openrouter_key: hasOpenrouter,
    has_gemini_key: hasGemini,
    has_openai_key: hasOpenai,
    active_key_configured: active,
    mode: active ? "live_llm" : "demo_simulation",
  };
}

const EMPTY_PATIENT = {
  age: "",
  sex: "Belirtilmedi",
  chief_complaint: "",
  history: "",
  notes: "",
};

export default function App() {
  const [hasLocalFastApi, setHasLocalFastApi] = useState(false);
  const [localConfig, setLocalConfig] = useState(() => loadLocalConfig());
  const [status, setStatus] = useState(() => buildPublicStatus(loadLocalConfig()));
  const [sampleCases, setSampleCases] = useState(SAMPLE_CASES);
  const [activeSampleId, setActiveSampleId] = useState(null);

  const [ecgData, setEcgData] = useState(null);
  const [patientContext, setPatientContext] = useState(EMPTY_PATIENT);
  const [caliperMeasurements, setCaliperMeasurements] = useState({});
  const [analysis, setAnalysis] = useState(null);

  const [isPreprocessing, setIsPreprocessing] = useState(false);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  // Modals
  const [showSettings, setShowSettings] = useState(false);
  const [showGuidelines, setShowGuidelines] = useState(false);

  // Settings form state
  const [cfgProvider, setCfgProvider] = useState(() => loadLocalConfig().provider);
  const [cfgOpenrouterModel, setCfgOpenrouterModel] = useState(() => loadLocalConfig().openrouter_model);
  const [cfgOpenrouterBaseUrl, setCfgOpenrouterBaseUrl] = useState(
    () => loadLocalConfig().openrouter_base_url
  );
  const [cfgOpenrouterKey, setCfgOpenrouterKey] = useState("");
  const [cfgGeminiModel, setCfgGeminiModel] = useState(() => loadLocalConfig().gemini_model);
  const [cfgOpenaiModel, setCfgOpenaiModel] = useState(() => loadLocalConfig().openai_model);
  const [cfgGeminiKey, setCfgGeminiKey] = useState("");
  const [cfgOpenaiKey, setCfgOpenaiKey] = useState("");
  const [cfgSaving, setCfgSaving] = useState(false);

  // Guidelines & QTc state
  const [guidelines, setGuidelines] = useState({
    territories: ANATOMICAL_TERRITORIES,
    criteria: CLINICAL_CRITERIA_KB,
    erb_benchmark_trees: ERB_BENCHMARK_TREES,
  });
  const [qtcInput, setQtcInput] = useState({ qt_ms: 400, hr_bpm: 75 });
  const [qtcOutput, setQtcOutput] = useState(null);
  const [qtcError, setQtcError] = useState("");
  const [serverlessStatus, setServerlessStatus] = useState(null);

  // Her yeni EKG yüklemesinde artar. Yavaş dönen bir ön işleme/analiz yanıtı, o sırada yüklenmiş
  // başka bir EKG'nin üzerine yazılmasın (yanlış EKG'ye yanlış rapor) diye kontrol edilir.
  const ecgSessionRef = useRef(0);

  const fetchInitialData = async () => {
    try {
      const healthRes = await fetch("/api/health");
      const contentType = healthRes.headers.get("content-type") || "";
      if (healthRes.ok && contentType.includes("application/json")) {
        const h = await healthRes.json();
        if (h?.service === "ECG_Helper") {
          setHasLocalFastApi(true);
          setStatus(h);
          setCfgProvider(h.provider || "openrouter");
          setCfgOpenrouterModel(h.openrouter_model || "google/gemini-3.8-flash");
          setCfgOpenrouterBaseUrl(h.openrouter_base_url || "https://openrouter.ai/api/v1");
          setCfgGeminiModel(h.gemini_model || "gemini-2.0-flash");
          setCfgOpenaiModel(h.openai_model || "gpt-4o");

          const [samplesRes, guideRes] = await Promise.all([
            fetch("/api/sample-cases"),
            fetch("/api/guidelines"),
          ]);
          if (samplesRes.ok) {
            const s = await samplesRes.json();
            if (s.cases?.length) setSampleCases(s.cases);
          }
          if (guideRes.ok) {
            setGuidelines(await guideRes.json());
          }
          return;
        }
      }
    } catch {
      // Yerel FastAPI yok; Vercel / Tarayıcı modunda sessizce devam et
    }
    setHasLocalFastApi(false);
    setStatus(buildPublicStatus(loadLocalConfig()));
    // Vercel: sunucu ortam değişkeninde anahtar varsa kullanıcı anahtar girmeden de canlı analiz çalışır
    setServerlessStatus(await fetchServerlessStatus());
  };

  useEffect(() => {
    fetchInitialData();
  }, []);

  const handleSelectSample = async (caseId) => {
    if (isPreprocessing) return;
    const session = ++ecgSessionRef.current;
    setErrorMsg("");
    setIsPreprocessing(true);
    setIsAnalyzing(false);
    setAnalysis(null);
    setCaliperMeasurements({});
    try {
      let data;
      if (hasLocalFastApi) {
        const res = await fetch(`/api/sample-cases/${caseId}`, { method: "POST" });
        if (!res.ok) {
          throw new Error(`Demo vaka yüklenemedi (${res.status})`);
        }
        data = await res.json();
      } else {
        data = await generateSyntheticEcgInBrowser(caseId);
      }
      if (session !== ecgSessionRef.current) return;
      setActiveSampleId(caseId);
      setEcgData({
        ...data,
        calibration: data.case?.calibration || null,
      });
      if (data.case) {
        setPatientContext({
          age: data.case.age ?? "",
          sex: data.case.sex ?? "Belirtilmedi",
          chief_complaint: data.case.chief_complaint ?? "",
          history: data.case.history ?? "",
          notes: data.case.notes ?? "",
        });
      }
    } catch (err) {
      if (session === ecgSessionRef.current) {
        setErrorMsg(err.message || "Demo vaka yüklenirken hata oluştu.");
      }
    } finally {
      if (session === ecgSessionRef.current) setIsPreprocessing(false);
    }
  };

  const handleUploadFile = async (file) => {
    if (isPreprocessing) return;
    if (file?.type && !file.type.startsWith("image/")) {
      setErrorMsg("Yalnızca görsel dosyaları (PNG, JPG, WEBP) yüklenebilir.");
      return;
    }
    const session = ++ecgSessionRef.current;
    setErrorMsg("");
    setIsPreprocessing(true);
    setIsAnalyzing(false);
    setAnalysis(null);
    setActiveSampleId(null);
    setCaliperMeasurements({});
    setPatientContext(EMPTY_PATIENT); // önceki vakanın hasta bilgisi yeni EKG'ye taşınmasın
    try {
      let data;
      if (hasLocalFastApi) {
        const formData = new FormData();
        formData.append("file", file);
        const res = await fetch("/api/preprocess", {
          method: "POST",
          body: formData,
        });
        if (!res.ok) {
          const errBody = await res.json().catch(() => ({}));
          throw new Error(errBody.detail || "Görsel işlenemedi.");
        }
        data = await res.json();
      } else {
        data = await preprocessEcgInBrowser(file);
      }
      if (session !== ecgSessionRef.current) return;
      setEcgData(data);
    } catch (err) {
      if (session === ecgSessionRef.current) {
        setEcgData(null);
        setErrorMsg(err.message || "Fotoğraf yüklenirken hata oluştu.");
      }
    } finally {
      if (session === ecgSessionRef.current) setIsPreprocessing(false);
    }
  };

  const handleSaveMeasurement = (key, val) => {
    setCaliperMeasurements((prev) => ({ ...prev, [key]: val }));
  };

  const handleRemoveMeasurement = (key) => {
    setCaliperMeasurements((prev) => {
      const next = { ...prev };
      delete next[key];
      return next;
    });
  };

  const handleRunAnalysis = async () => {
    if (!ecgData || isAnalyzing) return;
    const session = ecgSessionRef.current;
    setErrorMsg("");
    setIsAnalyzing(true);
    try {
      const result = await analyzeEcgClientOrServer({
        enhanced_b64: ecgData.enhanced_b64,
        lead_crops: ecgData.lead_crops || [],
        quality: ecgData.quality || null,
        patient_context: patientContext,
        caliper_measurements: caliperMeasurements,
        case_hint: activeSampleId,
        localConfig,
        hasLocalFastApi,
      });
      if (session !== ecgSessionRef.current) return;
      setAnalysis(result);
    } catch (err) {
      if (session === ecgSessionRef.current) {
        setErrorMsg(err.message || "Analiz sırasında hata oluştu.");
      }
    } finally {
      if (session === ecgSessionRef.current) setIsAnalyzing(false);
    }
  };

  const handleSaveConfig = async (e) => {
    e.preventDefault();
    setCfgSaving(true);
    setErrorMsg("");
    try {
      const nextLocal = {
        ...localConfig,
        provider: cfgProvider,
        openrouter_model: cfgOpenrouterModel,
        openrouter_base_url: cfgOpenrouterBaseUrl,
        gemini_model: cfgGeminiModel,
        openai_model: cfgOpenaiModel,
      };
      if (hasLocalFastApi) {
        // Yerel sunucu modunda anahtarlar yalnızca backend/config.json'da tutulur; tarayıcıya yazılmaz
        for (const key of SECRET_KEYS) nextLocal[key] = "";
      } else {
        if (cfgOpenrouterKey.trim() !== "") nextLocal.openrouter_api_key = cfgOpenrouterKey.trim();
        if (cfgGeminiKey.trim() !== "") nextLocal.gemini_api_key = cfgGeminiKey.trim();
        if (cfgOpenaiKey.trim() !== "") nextLocal.openai_api_key = cfgOpenaiKey.trim();
      }

      saveLocalConfig(nextLocal);
      setLocalConfig(nextLocal);

      if (hasLocalFastApi) {
        const body = {
          provider: cfgProvider,
          openrouter_model: cfgOpenrouterModel,
          openrouter_base_url: cfgOpenrouterBaseUrl,
          gemini_model: cfgGeminiModel,
          openai_model: cfgOpenaiModel,
        };
        if (cfgOpenrouterKey.trim() !== "") body.openrouter_api_key = cfgOpenrouterKey.trim();
        if (cfgGeminiKey.trim() !== "") body.gemini_api_key = cfgGeminiKey.trim();
        if (cfgOpenaiKey.trim() !== "") body.openai_api_key = cfgOpenaiKey.trim();

        const res = await fetch("/api/config", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(body),
        });
        if (!res.ok) {
          const errBody = await res.json().catch(() => ({}));
          throw new Error(
            typeof errBody.detail === "string" ? errBody.detail : "Ayarlar sunucuya kaydedilemedi."
          );
        }
        setStatus(await res.json());
      } else {
        setStatus(buildPublicStatus(nextLocal));
      }

      setCfgOpenrouterKey("");
      setCfgGeminiKey("");
      setCfgOpenaiKey("");
      setShowSettings(false);
    } catch (err) {
      setErrorMsg(err.message);
    } finally {
      setCfgSaving(false);
    }
  };

  const handleCalculateQtc = (e) => {
    e.preventDefault();
    // Formül istemci ve sunucuda aynıdır; ağ çağrısına gerek olmadan deterministik hesaplanır
    try {
      setQtcOutput(
        calculateQtc(qtcInput.qt_ms, qtcInput.hr_bpm, {
          sex: patientContext.sex,
          age: patientContext.age,
        })
      );
      setQtcError("");
    } catch (err) {
      setQtcOutput(null);
      setQtcError(err.message || "Geçersiz değer.");
    }
  };

  const serverKeyActive =
    !hasLocalFastApi && !status?.active_key_configured && Boolean(serverlessStatus?.server_key_configured);

  return (
    <div>
      {/* Üst Başlık Çubuğu */}
      <header className="topbar">
        <div className="brand">
          <div className="brand-icon">
            <Activity size={21} />
          </div>
          <div>
            <h1 className="brand-title">ECG_Helper</h1>
            <div className="brand-sub">
              Görüntü Ön İşleme + Dijital Pergel + 6 Adımlı LLM Klinik Muhakeme
            </div>
          </div>
        </div>

        <div className="topbar-actions">
          {status && (
            <span
              className={`badge ${
                status.active_key_configured || serverKeyActive ? "badge-emerald" : "badge-amber"
              }`}
            >
              {serverKeyActive
                ? `Canlı Mod: Sunucu Anahtarı (${serverlessStatus.model})`
                : status.active_key_configured
                ? `Canlı Mod: ${String(status.provider).toUpperCase()} (${
                    status.provider === "openrouter"
                      ? status.openrouter_model
                      : status.provider === "gemini"
                      ? status.gemini_model
                      : status.openai_model
                  })`
                : "Demo Modu (API Anahtarı Girilmedi)"}
            </span>
          )}

          <button type="button" className="btn btn-sm" onClick={() => setShowGuidelines(true)}>
            <BookOpen size={15} />
            Kılavuzlar &amp; QTc
          </button>

          <button type="button" className="btn btn-sm" onClick={() => setShowSettings(true)}>
            <Settings size={15} />
            API Ayarları
          </button>
        </div>
      </header>

      {errorMsg && (
        <div
          style={{
            maxWidth: 1640,
            margin: "12px auto 0",
            padding: "10px 16px",
            borderRadius: 10,
            background: "rgba(244, 63, 94, 0.14)",
            border: "1px solid rgba(244, 63, 94, 0.45)",
            color: "#fda4af",
            display: "flex",
            alignItems: "center",
            gap: 8,
            fontSize: "0.84rem",
          }}
        >
          <AlertCircle size={16} />
          <span>{errorMsg}</span>
        </div>
      )}

      {/* Ana Kokpit */}
      <main className="cockpit">
        <aside className="left-column">
          <PatientContextForm
            sampleCases={sampleCases}
            activeSampleId={activeSampleId}
            onSelectSample={handleSelectSample}
            onUploadFile={handleUploadFile}
            patientContext={patientContext}
            onChangePatient={setPatientContext}
            caliperMeasurements={caliperMeasurements}
            hasImage={Boolean(ecgData?.enhanced_b64)}
            isPreprocessing={isPreprocessing}
            isAnalyzing={isAnalyzing}
            onRunAnalysis={handleRunAnalysis}
          />
        </aside>

        <section className="right-column">
          <EcgCanvasViewer
            ecgData={ecgData}
            caliperMeasurements={caliperMeasurements}
            onSaveMeasurement={handleSaveMeasurement}
            onRemoveMeasurement={handleRemoveMeasurement}
          />

          <ReasoningStepper analysis={analysis} />

          <LeadCropsGallery leadCrops={ecgData?.lead_crops} />
        </section>
      </main>

      {/* API Ayarları Modal */}
      {showSettings && (
        <div className="modal-backdrop" onClick={() => setShowSettings(false)}>
          <div className="modal-box" onClick={(e) => e.stopPropagation()}>
            <div className="panel-header">
              <h3 style={{ margin: 0, display: "flex", alignItems: "center", gap: 8 }}>
                <Settings size={18} color="#22d3ee" />
                LLM Sağlayıcı &amp; API Anahtarı Ayarları
              </h3>
              <button type="button" className="btn btn-sm" onClick={() => setShowSettings(false)}>
                <X size={15} />
              </button>
            </div>

            <form onSubmit={handleSaveConfig}>
              <div className="field-group">
                <label className="field-label">Aktif Sağlayıcı</label>
                <select
                  className="select"
                  value={cfgProvider}
                  onChange={(e) => setCfgProvider(e.target.value)}
                >
                  <option value="openrouter">OpenRouter (Önerilen — Tüm Modeller)</option>
                  <option value="gemini">Google Gemini (Doğrudan API)</option>
                  <option value="openai">OpenAI Vision (Doğrudan API)</option>
                </select>
              </div>

              {cfgProvider === "openrouter" ? (
                <>
                  <div className="field-group">
                    <label className="field-label">
                      OpenRouter Model Kimliği (Vision destekli model seçin)
                    </label>
                    <input
                      type="text"
                      className="input mono"
                      value={cfgOpenrouterModel}
                      onChange={(e) => setCfgOpenrouterModel(e.target.value)}
                      placeholder="google/gemini-3.8-flash, openai/gpt-6.1-terra, openai/gpt-6.1-sol"
                    />
                  </div>
                  <div className="field-group">
                    <label className="field-label">
                      OpenRouter API Anahtarı{" "}
                      {status?.has_openrouter_key ? "(Kayıtlı anahtar mevcut — değiştirmek için yazın)" : ""}
                    </label>
                    <input
                      type="password"
                      className="input mono"
                      value={cfgOpenrouterKey}
                      onChange={(e) => setCfgOpenrouterKey(e.target.value)}
                      placeholder="sk-or-v1-..."
                    />
                  </div>
                  <div className="field-group">
                    <label className="field-label">OpenRouter Base URL</label>
                    <input
                      type="text"
                      className="input mono"
                      value={cfgOpenrouterBaseUrl}
                      onChange={(e) => setCfgOpenrouterBaseUrl(e.target.value)}
                    />
                  </div>
                </>
              ) : cfgProvider === "gemini" ? (
                <>
                  <div className="field-group">
                    <label className="field-label">Gemini Modeli</label>
                    <input
                      type="text"
                      className="input"
                      value={cfgGeminiModel}
                      onChange={(e) => setCfgGeminiModel(e.target.value)}
                      placeholder="gemini-2.0-flash"
                    />
                  </div>
                  <div className="field-group">
                    <label className="field-label">
                      Gemini API Anahtarı{" "}
                      {status?.has_gemini_key ? "(Kayıtlı anahtar mevcut — değiştirmek için yazın)" : ""}
                    </label>
                    <input
                      type="password"
                      className="input"
                      value={cfgGeminiKey}
                      onChange={(e) => setCfgGeminiKey(e.target.value)}
                      placeholder="AIza..."
                    />
                  </div>
                </>
              ) : (
                <>
                  <div className="field-group">
                    <label className="field-label">OpenAI Modeli</label>
                    <input
                      type="text"
                      className="input"
                      value={cfgOpenaiModel}
                      onChange={(e) => setCfgOpenaiModel(e.target.value)}
                      placeholder="gpt-4o"
                    />
                  </div>
                  <div className="field-group">
                    <label className="field-label">
                      OpenAI API Anahtarı{" "}
                      {status?.has_openai_key ? "(Kayıtlı anahtar mevcut — değiştirmek için yazın)" : ""}
                    </label>
                    <input
                      type="password"
                      className="input"
                      value={cfgOpenaiKey}
                      onChange={(e) => setCfgOpenaiKey(e.target.value)}
                      placeholder="sk-..."
                    />
                  </div>
                </>
              )}

              <div style={{ fontSize: "0.75rem", color: "#94a3b8", marginBottom: 14 }}>
                {hasLocalFastApi ? (
                  <>
                    Anahtarlar yalnızca bu bilgisayardaki <code>backend/config.json</code> dosyasında
                    saklanır (dilerseniz doğrudan o dosyayı da düzenleyebilirsiniz).
                  </>
                ) : (
                  <>
                    Anahtar bu tarayıcının yerel deposunda (localStorage) saklanır ve analiz sırasında
                    EKG görseliyle birlikte doğrudan seçili sağlayıcıya gönderilir. Paylaşılan
                    cihazlarda anahtar girmeyin.
                  </>
                )}
              </div>

              <div style={{ display: "flex", justifyContent: "flex-end", gap: 8 }}>
                <button type="button" className="btn" onClick={() => setShowSettings(false)}>
                  İptal
                </button>
                <button type="submit" className="btn btn-primary" disabled={cfgSaving}>
                  {cfgSaving ? "Kaydediliyor..." : "Ayarları Kaydet"}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Kılavuzlar & QTc Hesaplayıcı Modal */}
      {showGuidelines && (
        <div className="modal-backdrop" onClick={() => setShowGuidelines(false)}>
          <div className="modal-box wide" onClick={(e) => e.stopPropagation()}>
            <div className="panel-header">
              <h3 style={{ margin: 0, display: "flex", alignItems: "center", gap: 8 }}>
                <BookOpen size={18} color="#22d3ee" />
                ESC/AHA Hızlı Başvuru Kriterleri &amp; QTc Hesaplayıcı
              </h3>
              <button type="button" className="btn btn-sm" onClick={() => setShowGuidelines(false)}>
                <X size={15} />
              </button>
            </div>

            {/* QTc Hesaplayıcı */}
            <div className="step-card" style={{ marginBottom: 14 }}>
              <div className="step-head">
                <span className="step-num" style={{ display: "flex", alignItems: "center", gap: 6 }}>
                  <Calculator size={14} />
                  Hızlı QTc Hesaplayıcı (Bazett &amp; Fridericia)
                </span>
              </div>
              <form
                onSubmit={handleCalculateQtc}
                style={{ display: "flex", gap: 10, alignItems: "flex-end", flexWrap: "wrap" }}
              >
                <div>
                  <label className="field-label">Ölçülen QT (ms)</label>
                  <input
                    type="number"
                    className="input mono"
                    style={{ width: 140 }}
                    value={qtcInput.qt_ms}
                    onChange={(e) => setQtcInput({ ...qtcInput, qt_ms: e.target.value })}
                  />
                </div>
                <div>
                  <label className="field-label">Kalp Hızı (bpm)</label>
                  <input
                    type="number"
                    className="input mono"
                    style={{ width: 140 }}
                    value={qtcInput.hr_bpm}
                    onChange={(e) => setQtcInput({ ...qtcInput, hr_bpm: e.target.value })}
                  />
                </div>
                <button type="submit" className="btn btn-primary btn-sm">
                  Hesapla
                </button>
              </form>
              <div style={{ fontSize: "0.74rem", color: "#94a3b8", marginTop: 8 }}>
                Eşikler sol paneldeki hasta bilgisine göre seçilir (Cinsiyet:{" "}
                {patientContext.sex || "Belirtilmedi"}, Yaş: {patientContext.age || "—"}).
              </div>
              {qtcError && (
                <div style={{ marginTop: 8, fontSize: "0.8rem", color: "#fda4af" }}>{qtcError}</div>
              )}
              {qtcOutput && (
                <div
                  className="mono"
                  style={{
                    marginTop: 10,
                    padding: "8px 10px",
                    borderRadius: 8,
                    background: "#090f1e",
                    fontSize: "0.8rem",
                  }}
                >
                  Bazett QTc: <strong>{qtcOutput.qtc_bazett_ms} ms</strong> | Fridericia QTc:{" "}
                  <strong>{qtcOutput.qtc_fridericia_ms} ms</strong> | Esas alınan:{" "}
                  {qtcOutput.recommended_formula} — {qtcOutput.interpretation}
                </div>
              )}
            </div>

            {/* Kılavuz Kartları */}
            <div className="steps-grid">
              {(guidelines?.criteria || []).map((item) => (
                <div key={item.id} className="step-card">
                  <div className="step-head">
                    <span className="step-num">{item.title}</span>
                    <span
                      className={`badge ${
                        item.urgency === "CRITICAL"
                          ? "badge-rose"
                          : item.urgency === "URGENT"
                          ? "badge-amber"
                          : "badge-emerald"
                      }`}
                    >
                      {item.urgency}
                    </span>
                  </div>
                  <div style={{ fontSize: "0.78rem", color: "#94a3b8", marginBottom: 6 }}>
                    {item.summary}
                  </div>
                  <ul className="list-clean">
                    {item.criteria.map((c, idx) => (
                      <li key={idx}>{c}</li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>

            {/* Jwoo5/ecg-reasoning-benchmark 17 Tanı Karar Zincirleri */}
            {guidelines?.erb_benchmark_trees?.diagnoses && (
              <div style={{ marginTop: 18 }}>
                <div className="panel-header">
                  <h4 style={{ margin: 0, fontSize: "0.95rem", color: "#22d3ee" }}>
                    Jwoo5/ecg-reasoning-benchmark — 17 Temel EKG Tanısı ve Grounding Zincirleri
                  </h4>
                  <span className="badge badge-cyan">
                    {guidelines.erb_benchmark_trees.diagnosis_count} Tanı Şablonu Aktif
                  </span>
                </div>
                <div className="steps-grid">
                  {Object.values(guidelines.erb_benchmark_trees.diagnoses).map((dx) => (
                    <div key={dx.target_dx} className="step-card">
                      <div className="step-head">
                        <span className="step-num">{dx.display_name}</span>
                        <span className="badge badge-muted mono">{dx.target_dx}</span>
                      </div>
                      <ul className="list-clean" style={{ fontSize: "0.76rem" }}>
                        {(dx.steps || []).map((st, idx) => (
                          <li key={idx}>
                            <strong>Kriter {idx + 1}:</strong> {st.criterion}
                            {st.grounding_steps?.length > 0 && (
                              <span style={{ color: "#38bdf8" }}>
                                {" "}
                                [{st.grounding_steps.map((g) => g.question_type).join(", ")}]
                              </span>
                            )}
                          </li>
                        ))}
                      </ul>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
