import React, { useState } from "react";
import { LayoutGrid, X, ZoomIn } from "lucide-react";

export default function LeadCropsGallery({ leadCrops }) {
  const [selectedCrop, setSelectedCrop] = useState(null);

  if (!leadCrops || leadCrops.length === 0) {
    return null;
  }

  return (
    <>
      <div className="panel">
        <div className="panel-header">
          <h2 className="panel-title">
            <LayoutGrid size={16} color="#22d3ee" />
            Otomatik Kırpılan Anatomik Derivasyon Bölgeleri
          </h2>
          <span className="badge badge-muted">Büyütmek için karta tıklayın</span>
        </div>

        <div className="crops-grid">
          {leadCrops.map((crop) => (
            <div
              key={crop.id}
              className="crop-card"
              onClick={() => setSelectedCrop(crop)}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => {
                if (e.key === "Enter" || e.key === " ") setSelectedCrop(crop);
              }}
            >
              <div className="crop-img-wrap">
                <img src={crop.image_b64} alt={crop.title} />
              </div>
              <div className="crop-meta">
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "space-between",
                    gap: 6,
                  }}
                >
                  <span className="crop-title">{crop.title}</span>
                  <ZoomIn size={14} color="#22d3ee" />
                </div>
                <div className="crop-territory">{crop.territory}</div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {selectedCrop && (
        <div className="modal-backdrop" onClick={() => setSelectedCrop(null)}>
          <div className="modal-box wide" onClick={(e) => e.stopPropagation()}>
            <div className="panel-header">
              <div>
                <h3 style={{ margin: 0, fontSize: "1.05rem" }}>{selectedCrop.title}</h3>
                <div style={{ fontSize: "0.8rem", color: "#94a3b8", marginTop: 2 }}>
                  {selectedCrop.territory}
                </div>
              </div>
              <button type="button" className="btn btn-sm" onClick={() => setSelectedCrop(null)}>
                <X size={15} />
                Kapat
              </button>
            </div>
            <div
              style={{
                background: "#fff",
                borderRadius: 10,
                padding: 8,
                overflow: "auto",
                maxHeight: "68vh",
              }}
            >
              <img
                src={selectedCrop.image_b64}
                alt={selectedCrop.title}
                style={{ width: "100%", height: "auto", display: "block" }}
              />
            </div>
          </div>
        </div>
      )}
    </>
  );
}
