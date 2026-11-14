import React, { useEffect, useRef, useState } from "react";
import {
  Activity,
  Crosshair,
  Eye,
  EyeOff,
  Maximize2,
  RotateCcw,
  Ruler,
  Trash2,
  ZoomIn,
  ZoomOut,
} from "lucide-react";

const MIN_ZOOM = 0.5;
const MAX_ZOOM = 5.5;
const TAP_SLOP_PX = 6;
const PAPER_SPEEDS = [25, 50];
const GAINS = [5, 10, 20];

const clampZoom = (z) => Math.max(MIN_ZOOM, Math.min(MAX_ZOOM, Number(z.toFixed(2))));

// (vx, vy) görünüm noktasının altındaki görüntü pikseli sabit kalacak şekilde yakınlaştırır
function zoomAround(view, nextZoom, vx, vy) {
  const zoom = clampZoom(nextZoom);
  const ratio = zoom / view.zoom;
  return { zoom, x: vx - (vx - view.x) * ratio, y: vy - (vy - view.y) * ratio };
}

export default function EcgCanvasViewer({
  ecgData,
  caliperMeasurements,
  onSaveMeasurement,
  onRemoveMeasurement,
}) {
  const [viewMode, setViewMode] = useState("enhanced");
  const [view, setView] = useState({ zoom: 1, x: 0, y: 0 });
  const [isDragging, setIsDragging] = useState(false);

  const [showOverlay, setShowOverlay] = useState(false);
  const [caliperMode, setCaliperMode] = useState("off"); // "off" | "measure" | "calibrate"
  const [pxPerMm, setPxPerMm] = useState(7.0);
  // Yüklenen fotoğraflarda px/mm yalnızca kaba bir tahmindir; kullanıcı kalibre edene kadar
  // ölçümler LLM'e "kesin referans" olarak kaydedilemez.
  const [isCalibrated, setIsCalibrated] = useState(false);
  const [paperSpeed, setPaperSpeed] = useState(25); // mm/sn
  const [gain, setGain] = useState(10); // mm/mV
  const [notice, setNotice] = useState("");
  const [p1, setP1] = useState(null);
  const [p2, setP2] = useState(null);
  const [hoverPt, setHoverPt] = useState(null);
  const [imgNatural, setImgNatural] = useState({ w: 1900, h: 1060 });

  const viewportRef = useRef(null);
  const imgRef = useRef(null);
  const viewRef = useRef(view);
  viewRef.current = view;
  const pointersRef = useRef(new Map());
  const gestureRef = useRef(null);

  const clearPoints = () => {
    setP1(null);
    setP2(null);
    setHoverPt(null);
    setNotice("");
  };

  useEffect(() => {
    setView({ zoom: 1, x: 0, y: 0 });
    setP1(null);
    setP2(null);
    setHoverPt(null);
    setNotice("");
    setPaperSpeed(25);
    setGain(10);
    pointersRef.current.clear();
    gestureRef.current = null;
    if (ecgData?.calibration?.px_per_mm) {
      setPxPerMm(ecgData.calibration.px_per_mm);
      setIsCalibrated(true);
    } else if (ecgData?.dimensions?.width) {
      // Gerçek fotoğraf için tahmini başlangıç (standart 250mm EKG kağıdı ~ %90 genişlik varsayımı)
      setPxPerMm(Number(((ecgData.dimensions.width * 0.9) / 250).toFixed(2)));
      setIsCalibrated(false);
    }
  }, [ecgData]);

  const activeSrc =
    viewMode === "original"
      ? ecgData?.original_b64
      : viewMode === "waveform"
      ? ecgData?.waveform_b64
      : ecgData?.enhanced_b64;
  const hasImage = Boolean(activeSrc);

  // React wheel olayını pasif dinleyici olarak bağladığı için preventDefault() etkisiz kalır ve
  // yakınlaştırırken sayfa da kayar; bu yüzden tekerlek dinleyicisi doğrudan DOM'a eklenir.
  useEffect(() => {
    const el = viewportRef.current;
    if (!el || !hasImage) return undefined;
    const onWheel = (e) => {
      e.preventDefault();
      const rect = el.getBoundingClientRect();
      const factor = e.deltaY < 0 ? 1.14 : 0.88;
      setView((v) => zoomAround(v, v.zoom * factor, e.clientX - rect.left, e.clientY - rect.top));
    };
    el.addEventListener("wheel", onWheel, { passive: false });
    return () => el.removeEventListener("wheel", onWheel);
  }, [hasImage]);

  const zoomAtCenter = (delta) => {
    const el = viewportRef.current;
    if (!el) return;
    setView((v) => zoomAround(v, v.zoom + delta, el.clientWidth / 2, el.clientHeight / 2));
  };

  const clientToNatural = (clientX, clientY) => {
    if (!imgRef.current) return null;
    const rect = imgRef.current.getBoundingClientRect();
    if (rect.width <= 0 || rect.height <= 0) return null;
    const x = ((clientX - rect.left) / rect.width) * imgNatural.w;
    const y = ((clientY - rect.top) / rect.height) * imgNatural.h;
    return {
      x: Math.max(0, Math.min(imgNatural.w, x)),
      y: Math.max(0, Math.min(imgNatural.h, y)),
    };
  };

  const applyPointPick = (clientX, clientY) => {
    const pt = clientToNatural(clientX, clientY);
    if (!pt) return;
    setNotice("");
    if (!p1 || p2) {
      setP1(pt);
      setP2(null);
      setHoverPt(null); // önceki ölçümden kalan imleç konumu yeni çizgiyi yanlış yere bağlamasın
    } else if (caliperMode === "calibrate") {
      // Eğik çekilmiş fotoğraflarda da doğru sonuç için iki nokta arası gerçek mesafe kullanılır
      const dist = Math.hypot(pt.x - p1.x, pt.y - p1.y);
      setP1(null);
      setP2(null);
      setHoverPt(null);
      if (dist < 10) {
        setNotice("Kalibrasyon noktaları birbirine çok yakın; 5 büyük karenin iki ucunu işaretleyin.");
        return;
      }
      // 5 büyük kare = 25 mm (kağıt hızından bağımsız)
      setPxPerMm(Number((dist / 25).toFixed(2)));
      setIsCalibrated(true);
      setCaliperMode("measure");
    } else {
      setP2(pt);
    }
  };

  // Fare ve dokunmatik tek bir Pointer Events akışıyla yönetilir. Ayrı mouse + touch dinleyicileri,
  // dokunuştan sonra tarayıcının ürettiği taklit mouse olayları yüzünden her dokunuşu iki kez
  // işliyor (P1 ve P2 aynı noktaya düşüyor) ve mobilde pergeli kullanılamaz kılıyordu.
  const viewportPoint = (e) => {
    const rect = viewportRef.current.getBoundingClientRect();
    return { x: e.clientX - rect.left, y: e.clientY - rect.top };
  };

  const startDragGesture = (pt, alreadyMoved) => {
    gestureRef.current = { type: "drag", start: pt, startView: viewRef.current, moved: alreadyMoved };
  };

  const handlePointerDown = (e) => {
    if (!hasImage) return;
    if (e.pointerType === "mouse" && e.button !== 0) return;
    try {
      // Parmak/fare görünümün dışına çıksa da hareketi izlemeye devam et
      e.currentTarget.setPointerCapture(e.pointerId);
    } catch {
      // Yakalama desteklenmiyorsa hareket yine de çalışır; yalnızca alan dışı izleme olmaz
    }
    const pt = viewportPoint(e);
    pointersRef.current.set(e.pointerId, pt);

    if (pointersRef.current.size === 2) {
      const [a, b] = [...pointersRef.current.values()];
      gestureRef.current = {
        type: "pinch",
        startDist: Math.hypot(b.x - a.x, b.y - a.y),
        startMid: { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 },
        startView: viewRef.current,
      };
    } else if (pointersRef.current.size === 1) {
      startDragGesture(pt, false);
    }
  };

  const handlePointerMove = (e) => {
    const pointers = pointersRef.current;
    const gesture = gestureRef.current;

    if (!pointers.has(e.pointerId)) {
      // Basılı olmayan fare: ikinci nokta seçilene kadar lastik çizgiyi imlece bağla
      if (e.pointerType === "mouse" && caliperMode !== "off" && p1 && !p2) {
        const pt = clientToNatural(e.clientX, e.clientY);
        if (pt) setHoverPt(pt);
      }
      return;
    }

    const pt = viewportPoint(e);
    pointers.set(e.pointerId, pt);
    if (!gesture) return;

    if (gesture.type === "pinch" && pointers.size >= 2) {
      const [a, b] = [...pointers.values()];
      const dist = Math.hypot(b.x - a.x, b.y - a.y);
      if (gesture.startDist < 10) return;
      const mid = { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
      const zoomed = zoomAround(
        gesture.startView,
        gesture.startView.zoom * (dist / gesture.startDist),
        gesture.startMid.x,
        gesture.startMid.y
      );
      // İki parmağın orta noktası kaydıkça görüntü de onunla birlikte kayar
      setView({
        zoom: zoomed.zoom,
        x: zoomed.x + (mid.x - gesture.startMid.x),
        y: zoomed.y + (mid.y - gesture.startMid.y),
      });
      return;
    }

    if (gesture.type === "drag") {
      const dx = pt.x - gesture.start.x;
      const dy = pt.y - gesture.start.y;
      if (!gesture.moved && Math.hypot(dx, dy) < TAP_SLOP_PX) return;
      if (!gesture.moved) {
        gesture.moved = true;
        setIsDragging(true);
      }
      setView({ zoom: gesture.startView.zoom, x: gesture.startView.x + dx, y: gesture.startView.y + dy });
    }
  };

  const handlePointerEnd = (e, isRelease) => {
    const pointers = pointersRef.current;
    if (!pointers.has(e.pointerId)) return;
    pointers.delete(e.pointerId);
    const gesture = gestureRef.current;

    // Sürüklemeden bırakılan tek dokunuş/tıklama = pergel noktası. Sürükleme ise pergel modunda da
    // görüntüyü kaydırır; böylece yakınlaştırılmış görüntüde ikinci noktaya ulaşılabilir.
    if (isRelease && gesture?.type === "drag" && !gesture.moved && caliperMode !== "off") {
      applyPointPick(e.clientX, e.clientY);
    }

    if (pointers.size === 1) {
      // Kıstırma bitti, bir parmak hâlâ ekranda: kaydırmaya devam et ama dokunuş sayma
      startDragGesture([...pointers.values()][0], true);
    } else if (pointers.size === 0) {
      gestureRef.current = null;
      setIsDragging(false);
    }
  };

  const resetView = () => {
    setView({ zoom: 1, x: 0, y: 0 });
  };

  const msPerMm = 1000 / paperSpeed;
  const mvPerMm = 1 / gain;
  const endPt = p2 || hoverPt;
  let metric = null;
  if (p1 && endPt && pxPerMm > 0) {
    const dxMm = Math.abs(endPt.x - p1.x) / pxPerMm;
    // Ekranda y aşağı doğru artar: pozitif değer ikinci noktanın birinciden YUKARIDA olduğunu gösterir
    const dyMmSigned = (p1.y - endPt.y) / pxPerMm;
    const ms = dxMm * msPerMm;
    const bpm = ms >= 150 ? Math.round(60000 / ms) : null;
    const sign = dyMmSigned > 0 ? "+" : dyMmSigned < 0 ? "−" : "";
    metric = {
      dxMm: dxMm.toFixed(1),
      dyMm: Math.abs(dyMmSigned).toFixed(1),
      ms: Math.round(ms),
      mv: (Math.abs(dyMmSigned) * mvPerMm).toFixed(2),
      bpm,
      sign,
      stLabel: dyMmSigned > 0 ? "elevasyon" : dyMmSigned < 0 ? "depresyon" : "izoelektrik",
    };
  }

  const saveMeasurement = (key, value) => {
    onSaveMeasurement(key, value);
    // Standart dışı kağıt ayarı LLM'e de bildirilir; aksi halde model kareleri 25 mm/sn varsayarak sayar
    if (paperSpeed !== 25 || gain !== 10) {
      onSaveMeasurement("Kağıt Ayarı", `${paperSpeed} mm/sn, ${gain} mm/mV`);
    }
  };

  const savedKeys = Object.keys(caliperMeasurements || {});

  return (
    <div className="panel">
      <div className="canvas-toolbar">
        <div className="seg-group" role="group" aria-label="Görüntü modu">
          <button
            type="button"
            className={`seg-btn ${viewMode === "original" ? "active" : ""}`}
            onClick={() => setViewMode("original")}
            disabled={!ecgData}
          >
            Orijinal
          </button>
          <button
            type="button"
            className={`seg-btn ${viewMode === "enhanced" ? "active" : ""}`}
            onClick={() => setViewMode("enhanced")}
            disabled={!ecgData}
          >
            Kontrast İyileştirilmiş
          </button>
          <button
            type="button"
            className={`seg-btn ${viewMode === "waveform" ? "active" : ""}`}
            onClick={() => setViewMode("waveform")}
            disabled={!ecgData}
          >
            Izgara Bastırılmış
          </button>
        </div>

        <div style={{ display: "flex", alignItems: "center", gap: 6, flexWrap: "wrap" }}>
          <button
            type="button"
            className={`btn btn-sm ${caliperMode === "measure" ? "btn-active" : ""}`}
            onClick={() => {
              clearPoints();
              setCaliperMode((m) => (m === "measure" ? "off" : "measure"));
            }}
            disabled={!ecgData}
            title="İki nokta seçerek ms, bpm ve mV ölçün"
          >
            <Ruler size={14} />
            Dijital Pergel
          </button>

          <button
            type="button"
            className={`btn btn-sm ${caliperMode === "calibrate" ? "btn-active" : ""}`}
            onClick={() => {
              clearPoints();
              setCaliperMode((m) => (m === "calibrate" ? "off" : "calibrate"));
            }}
            disabled={!ecgData}
            title="Yatayda 5 büyük kare (25 mm) işaretleyerek gerçek kağıt fotoğraflarını kalibre edin"
          >
            <Crosshair size={14} />
            Kalibre Et
          </button>

          <button
            type="button"
            className={`btn btn-sm ${showOverlay ? "btn-active" : ""}`}
            onClick={() => setShowOverlay((s) => !s)}
            disabled={!ecgData?.lead_crops?.length}
          >
            {showOverlay ? <Eye size={14} /> : <EyeOff size={14} />}
            Derivasyon Bölgeleri
          </button>

          <div className="seg-group">
            <button
              type="button"
              className="seg-btn"
              onClick={() => zoomAtCenter(-0.25)}
              disabled={!ecgData}
              title="Uzaklaştır"
            >
              <ZoomOut size={14} />
            </button>
            <span className="mono" style={{ fontSize: "0.75rem", padding: "4px 6px", color: "#cbd5e1" }}>
              {Math.round(view.zoom * 100)}%
            </span>
            <button
              type="button"
              className="seg-btn"
              onClick={() => zoomAtCenter(0.25)}
              disabled={!ecgData}
              title="Yakınlaştır"
            >
              <ZoomIn size={14} />
            </button>
            <button
              type="button"
              className="seg-btn"
              onClick={resetView}
              disabled={!ecgData}
              title="Görünümü sıfırla"
            >
              <RotateCcw size={13} />
            </button>
          </div>
        </div>
      </div>

      <div
        ref={viewportRef}
        className="canvas-viewport"
        style={{
          touchAction: "none",
          cursor:
            caliperMode !== "off"
              ? "crosshair"
              : isDragging
              ? "grabbing"
              : activeSrc
              ? "grab"
              : "default",
        }}
        onPointerDown={handlePointerDown}
        onPointerMove={handlePointerMove}
        onPointerUp={(e) => handlePointerEnd(e, true)}
        onPointerCancel={(e) => handlePointerEnd(e, false)}
      >
        {!activeSrc ? (
          <div className="canvas-empty">
            <Activity size={40} color="#22d3ee" />
            <div style={{ fontWeight: 600, color: "#e2e8f0" }}>
              Henüz EKG Görüntüsü Yüklenmedi
            </div>
            <div style={{ fontSize: "0.82rem", maxWidth: 420 }}>
              Sol panelden bir EKG fotoğrafı yükleyin veya hazır klinik demo vakalarından birini
              seçerek görüntü iyileştirme ve dijital pergeli deneyin.
            </div>
          </div>
        ) : (
          <div
            style={{
              position: "relative",
              transform: `translate(${view.x}px, ${view.y}px) scale(${view.zoom})`,
              transformOrigin: "0 0",
              width: "100%",
            }}
          >
            <img
              ref={imgRef}
              src={activeSrc}
              alt="EKG Görüntüsü"
              draggable={false}
              onLoad={(e) => {
                setImgNatural({
                  w: e.currentTarget.naturalWidth || 1900,
                  h: e.currentTarget.naturalHeight || 1060,
                });
              }}
              style={{ display: "block", width: "100%", height: "auto" }}
            />

            <svg
              viewBox={`0 0 ${imgNatural.w} ${imgNatural.h}`}
              style={{
                position: "absolute",
                inset: 0,
                width: "100%",
                height: "100%",
                pointerEvents: "none",
              }}
            >
              {showOverlay &&
                (ecgData?.lead_crops || []).map((crop, idx) => {
                  const [x1, y1, x2, y2] = crop.bbox;
                  const bx = x1 * imgNatural.w;
                  const by = y1 * imgNatural.h;
                  const bw = (x2 - x1) * imgNatural.w;
                  const bh = (y2 - y1) * imgNatural.h;
                  const palette = ["#22d3ee", "#10b981", "#f59e0b", "#a78bfa", "#f43f5e"];
                  const stroke = palette[idx % palette.length];
                  return (
                    <g key={crop.id}>
                      <rect
                        x={bx}
                        y={by}
                        width={bw}
                        height={bh}
                        fill={`${stroke}14`}
                        stroke={stroke}
                        strokeWidth={Math.max(2, 3 / view.zoom)}
                        strokeDasharray="10 6"
                        rx={8}
                      />
                      <rect
                        x={bx + 8}
                        y={by + 8}
                        width={Math.min(bw - 16, 280)}
                        height={30}
                        fill="rgba(7, 12, 23, 0.85)"
                        rx={6}
                      />
                      <text
                        x={bx + 18}
                        y={by + 28}
                        fill={stroke}
                        fontSize={16}
                        fontWeight="700"
                      >
                        {crop.leads.join(", ")}
                      </text>
                    </g>
                  );
                })}

              {p1 && (
                <circle
                  cx={p1.x}
                  cy={p1.y}
                  r={Math.max(5, 7 / view.zoom)}
                  fill="#22d3ee"
                  stroke="#070c17"
                  strokeWidth={2 / view.zoom}
                />
              )}

              {p1 && endPt && (
                <>
                  <line
                    x1={p1.x}
                    y1={p1.y}
                    x2={endPt.x}
                    y2={endPt.y}
                    stroke={caliperMode === "calibrate" ? "#f59e0b" : "#22d3ee"}
                    strokeWidth={Math.max(2, 3 / view.zoom)}
                    strokeDasharray={p2 ? undefined : "6 4"}
                  />
                  {/* Yatay ve dikey kılavuz çizgiler */}
                  <line
                    x1={p1.x}
                    y1={p1.y}
                    x2={endPt.x}
                    y2={p1.y}
                    stroke="rgba(34,211,238,0.5)"
                    strokeWidth={Math.max(1, 1.5 / view.zoom)}
                    strokeDasharray="4 4"
                  />
                  <line
                    x1={endPt.x}
                    y1={p1.y}
                    x2={endPt.x}
                    y2={endPt.y}
                    stroke="rgba(16,185,129,0.55)"
                    strokeWidth={Math.max(1, 1.5 / view.zoom)}
                    strokeDasharray="4 4"
                  />
                  <circle
                    cx={endPt.x}
                    cy={endPt.y}
                    r={Math.max(5, 7 / view.zoom)}
                    fill={caliperMode === "calibrate" ? "#f59e0b" : "#10b981"}
                    stroke="#070c17"
                    strokeWidth={2 / view.zoom}
                  />
                </>
              )}
            </svg>
          </div>
        )}
      </div>

      {/* Pergel Durum ve Kayıt Çubuğu */}
      <div className="caliper-bar">
        <div style={{ display: "flex", alignItems: "center", gap: 10, flexWrap: "wrap" }}>
          <span className={`badge mono ${isCalibrated ? "badge-muted" : "badge-amber"}`}>
            {isCalibrated ? "Kalibrasyon" : "Tahmini kalibrasyon"}: {pxPerMm} px/mm
          </span>

          <label className="mono" style={{ fontSize: "0.74rem", color: "#94a3b8", display: "inline-flex", alignItems: "center", gap: 4 }}>
            Hız
            <select
              className="select"
              style={{ width: "auto", padding: "3px 6px", fontSize: "0.74rem" }}
              value={paperSpeed}
              onChange={(e) => setPaperSpeed(Number(e.target.value))}
              disabled={!ecgData}
              aria-label="Kağıt hızı"
            >
              {PAPER_SPEEDS.map((v) => (
                <option key={v} value={v}>
                  {v} mm/sn
                </option>
              ))}
            </select>
          </label>

          <label className="mono" style={{ fontSize: "0.74rem", color: "#94a3b8", display: "inline-flex", alignItems: "center", gap: 4 }}>
            Kazanç
            <select
              className="select"
              style={{ width: "auto", padding: "3px 6px", fontSize: "0.74rem" }}
              value={gain}
              onChange={(e) => setGain(Number(e.target.value))}
              disabled={!ecgData}
              aria-label="Kalibrasyon kazancı"
            >
              {GAINS.map((v) => (
                <option key={v} value={v}>
                  {v} mm/mV
                </option>
              ))}
            </select>
          </label>

          {caliperMode === "calibrate" && (
            <span className="badge badge-amber">
              Kalibrasyon Modu: Yatayda 5 büyük karenin (25 mm) iki ucuna dokunun / tıklayın.
            </span>
          )}

          {caliperMode === "measure" && !p1 && (
            <span className="badge badge-cyan">
              Ölçüm Modu: Başlangıç noktasına dokunun (sürükleyerek kaydırabilirsiniz).
            </span>
          )}

          {caliperMode === "measure" && p1 && !p2 && (
            <span className="badge badge-cyan">
              Şimdi bitiş noktasını seçin...
            </span>
          )}

          {notice && <span className="badge badge-amber">{notice}</span>}

          {caliperMode !== "off" && (p1 || p2) && (
            <button type="button" className="btn btn-sm" onClick={clearPoints}>
              <RotateCcw size={13} />
              Noktaları Sıfırla
            </button>
          )}

          {metric && caliperMode === "measure" && (
            <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
              <span className="badge badge-emerald mono">
                Δt: {metric.ms} ms ({metric.dxMm} mm) {metric.bpm ? `≈ ${metric.bpm} bpm` : ""} | ΔV:{" "}
                {metric.sign}
                {metric.mv} mV ({metric.sign}
                {metric.dyMm} mm)
              </span>
              {p2 && !isCalibrated && (
                <span className="badge badge-amber">
                  Bu fotoğraf henüz kalibre edilmedi; ölçümü kaydetmek için önce &quot;Kalibre Et&quot; ile
                  5 büyük kareyi işaretleyin.
                </span>
              )}
              {p2 && isCalibrated && (
                <div className="chip-row" style={{ marginTop: 0 }}>
                  <button
                    type="button"
                    className="chip"
                    onClick={() => saveMeasurement("PR", `${metric.ms} ms`)}
                  >
                    + PR Kaydet
                  </button>
                  <button
                    type="button"
                    className="chip"
                    onClick={() => saveMeasurement("QRS", `${metric.ms} ms`)}
                  >
                    + QRS Kaydet
                  </button>
                  <button
                    type="button"
                    className="chip"
                    onClick={() => saveMeasurement("QT", `${metric.ms} ms`)}
                  >
                    + QT Kaydet
                  </button>
                  <button
                    type="button"
                    className="chip"
                    onClick={() =>
                      saveMeasurement(
                        "R-R",
                        metric.bpm ? `${metric.ms} ms (${metric.bpm} bpm)` : `${metric.ms} ms`
                      )
                    }
                  >
                    + R-R Kaydet
                  </button>
                  <button
                    type="button"
                    className="chip"
                    title="1. nokta: izoelektrik hat (PR/TP segmenti), 2. nokta: J noktası"
                    onClick={() =>
                      saveMeasurement(
                        "ST Sapması",
                        `${metric.sign}${metric.dyMm} mm (${metric.sign}${metric.mv} mV) ${metric.stLabel}`
                      )
                    }
                  >
                    + ST Kaydet
                  </button>
                </div>
              )}
            </div>
          )}
        </div>

        {savedKeys.length > 0 && (
          <div style={{ display: "flex", alignItems: "center", gap: 6, flexWrap: "wrap" }}>
            <span style={{ fontSize: "0.74rem", color: "#94a3b8" }}>Kayıtlı Ölçümler:</span>
            {savedKeys.map((k) => (
              <span key={k} className="badge badge-cyan mono">
                {k}: {caliperMeasurements[k]}
                <button
                  type="button"
                  onClick={() => onRemoveMeasurement(k)}
                  style={{
                    background: "none",
                    border: "none",
                    padding: 0,
                    marginLeft: 4,
                    cursor: "pointer",
                    display: "inline-flex",
                    color: "inherit",
                  }}
                  title="Ölçümü sil"
                >
                  <Trash2 size={12} />
                </button>
              </span>
            ))}
          </div>
        )}
      </div>

      {/* Görüntü Kalitesi Uyarıları */}
      {ecgData?.quality && (
        <div
          style={{
            marginTop: 8,
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            gap: 10,
            flexWrap: "wrap",
            fontSize: "0.76rem",
            color: "#94a3b8",
          }}
        >
          <div className="mono">
            Çözünürlük: {ecgData.quality.width}×{ecgData.quality.height} px • Netlik:{" "}
            {ecgData.quality.sharpness_score} • Kalite:{" "}
            <strong
              style={{
                color:
                  ecgData.quality.overall_status === "GOOD"
                    ? "#10b981"
                    : ecgData.quality.overall_status === "FAIR"
                    ? "#f59e0b"
                    : "#f43f5e",
              }}
            >
              {ecgData.quality.overall_status}
            </strong>
          </div>
          {ecgData.quality.warnings?.length > 0 && (
            <div style={{ color: "#f59e0b" }}>{ecgData.quality.warnings.join(" ")}</div>
          )}
        </div>
      )}
    </div>
  );
}
