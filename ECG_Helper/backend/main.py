"""ECG_Helper FastAPI sunucusu: EKG görüntü ön işleme, sentetik vaka üretimi ve 6 adımlı klinik LLM analizi."""

import base64
import re
from typing import Dict, Any, List, Optional

import cv2
from fastapi import FastAPI, File, HTTPException, Query, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from clinical_guidelines import (
    ANATOMICAL_TERRITORIES,
    CLINICAL_CRITERIA_KB,
    calculate_qtc,
    load_erb_benchmark_trees,
)
from ecg_preprocessor import SAMPLE_CASES, generate_synthetic_ecg, preprocess_ecg_image
from ecg_reasoning_engine import ECGReasoningEngine


app = FastAPI(
    title="ECG_Helper Klinik Karar Destek API",
    description="OpenCV ön işleme + ECG-Reasoning-Benchmark tabanlı 6 adımlı LLM klinik muhakeme motoru.",
    version="1.0.0",
)

# Arayüz Vite proxy'si üzerinden aynı kökenden konuşur. CORS yalnızca yerel geliştirme kökenlerine
# açılır: "*" bırakılırsa ziyaret edilen herhangi bir web sitesi /api/config'e yazıp
# openrouter_base_url'i değiştirerek API anahtarını ve EKG görsellerini kendi sunucusuna yönlendirebilir.
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^https?://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

engine = ECGReasoningEngine()


class ConfigUpdateRequest(BaseModel):
    provider: Optional[str] = Field(default=None, description="openrouter, gemini veya openai")
    openrouter_model: Optional[str] = None
    openrouter_api_key: Optional[str] = None
    openrouter_base_url: Optional[str] = None
    gemini_model: Optional[str] = None
    openai_model: Optional[str] = None
    gemini_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None


class AnalyzeRequest(BaseModel):
    image_b64: Optional[str] = None
    enhanced_b64: Optional[str] = None
    lead_crops: Optional[List[Dict[str, Any]]] = None
    quality: Optional[Dict[str, Any]] = None
    patient_context: Dict[str, Any] = Field(default_factory=dict)
    caliper_measurements: Dict[str, Any] = Field(default_factory=dict)
    case_hint: Optional[str] = None


class QtcRequest(BaseModel):
    qt_ms: float
    hr_bpm: float
    sex: Optional[str] = None
    age: Optional[Any] = None


def _preprocess_or_400(image_bytes: bytes) -> Dict[str, Any]:
    """Ön işlemeyi çalıştırır; okunamayan görselde 500 yerine anlaşılır bir 400 hatası döndürür."""
    try:
        return preprocess_ecg_image(image_bytes)
    except (ValueError, cv2.error) as exc:
        raise HTTPException(status_code=400, detail=f"Görsel işlenemedi: {exc}") from exc


def _decode_b64_image(data_or_uri: str) -> bytes:
    """Data URI veya saf base64 dizesini ham görüntü baytlarına çevirir."""
    raw_str = data_or_uri.split(",", 1)[1] if "," in data_or_uri else data_or_uri
    try:
        return base64.b64decode(raw_str)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Geçersiz base64 görsel verisi: {exc}") from exc


def _public_preprocess_payload(processed: Dict[str, Any]) -> Dict[str, Any]:
    """Ön işleme sözlüğünden JSON serileştirilemeyen ham bayt alanını ayırır."""
    return {k: v for k, v in processed.items() if k != "enhanced_bytes"}


@app.get("/api/health")
def health_check() -> Dict[str, Any]:
    """Sunucu sağlık durumu ve aktif LLM sağlayıcı özetini döndürür."""
    status = engine.get_public_status()
    return {"status": "ok", "service": "ECG_Helper", **status}


@app.get("/api/config")
def get_config() -> Dict[str, Any]:
    """Mevcut LLM yapılandırma durumunu anahtarları gizleyerek döndürür."""
    return engine.get_public_status()


@app.post("/api/config")
def update_config(payload: ConfigUpdateRequest) -> Dict[str, Any]:
    """LLM sağlayıcısını, modeli ve API anahtarını günceller."""
    updates = payload.model_dump(exclude_none=True)
    if "provider" in updates and updates["provider"] not in ("openrouter", "gemini", "openai"):
        raise HTTPException(
            status_code=400,
            detail="Desteklenen sağlayıcılar: 'openrouter', 'gemini' veya 'openai'.",
        )
    base_url = updates.get("openrouter_base_url")
    if base_url and not re.match(r"^https://[^\s/]+|^http://(localhost|127\.0\.0\.1)(:\d+)?(/|$)", base_url.strip()):
        raise HTTPException(
            status_code=400,
            detail="OpenRouter Base URL 'https://' ile başlamalıdır (yalnızca localhost için http kabul edilir).",
        )
    engine.save_config(updates)
    return {"saved": True, **engine.get_public_status()}


@app.get("/api/sample-cases")
def list_sample_cases() -> Dict[str, Any]:
    """Hazır demo klinik EKG vakalarının listesini döndürür."""
    return {"cases": list(SAMPLE_CASES.values())}


@app.post("/api/sample-cases/{case_id}")
def load_sample_case(case_id: str) -> Dict[str, Any]:
    """Seçilen sentetik vakayı üretir, OpenCV ön işlemeden geçirir ve hasta bilgileriyle döndürür."""
    if case_id not in SAMPLE_CASES:
        raise HTTPException(status_code=404, detail=f"Vaka bulunamadı: {case_id}")

    png_bytes, case_meta = generate_synthetic_ecg(case_id)
    processed = preprocess_ecg_image(png_bytes)
    return {
        "case": case_meta,
        **_public_preprocess_payload(processed),
    }


@app.post("/api/preprocess")
async def preprocess_uploaded_ecg(file: UploadFile = File(...)) -> Dict[str, Any]:
    """Yüklenen EKG fotoğrafını OpenCV ile netleştirir, kırpar ve kalite skorlarını döndürür."""
    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Boş dosya yüklendi.")
    processed = _preprocess_or_400(content)

    return {
        "filename": file.filename,
        **_public_preprocess_payload(processed),
    }


@app.post("/api/analyze")
def analyze_ecg(payload: AnalyzeRequest) -> Dict[str, Any]:
    """EKG görselini, hasta öyküsünü ve dijital pergel ölçümlerini 6 adımlı klinik muhakeme motoruyla analiz eder."""
    enhanced_bytes: Optional[bytes] = None
    lead_crops = payload.lead_crops or []
    quality = payload.quality

    if payload.enhanced_b64:
        enhanced_bytes = _decode_b64_image(payload.enhanced_b64)
    elif payload.image_b64:
        raw_bytes = _decode_b64_image(payload.image_b64)
        processed = _preprocess_or_400(raw_bytes)
        enhanced_bytes = processed["enhanced_bytes"]
        if not lead_crops:
            lead_crops = processed["lead_crops"]
        if not quality:
            quality = processed["quality"]
    elif payload.case_hint and payload.case_hint in SAMPLE_CASES:
        png_bytes, _ = generate_synthetic_ecg(payload.case_hint)
        processed = preprocess_ecg_image(png_bytes)
        enhanced_bytes = processed["enhanced_bytes"]
        if not lead_crops:
            lead_crops = processed["lead_crops"]
        if not quality:
            quality = processed["quality"]
    else:
        raise HTTPException(
            status_code=400,
            detail="Analiz için 'enhanced_b64', 'image_b64' veya geçerli bir 'case_hint' gönderilmelidir.",
        )

    return engine.analyze(
        enhanced_bytes=enhanced_bytes,
        lead_crops=lead_crops,
        patient_context=payload.patient_context,
        caliper_measurements=payload.caliper_measurements,
        case_hint=payload.case_hint,
        quality=quality,
    )


@app.get("/api/guidelines")
def get_guidelines(
    qt_ms: Optional[float] = Query(default=None, gt=0),
    hr_bpm: Optional[float] = Query(default=None, gt=0),
) -> Dict[str, Any]:
    """ESC/AHA hızlı başvuru kriterlerini ve istenirse QTc hesaplama sonucunu döndürür."""
    resp: Dict[str, Any] = {
        "territories": ANATOMICAL_TERRITORIES,
        "criteria": CLINICAL_CRITERIA_KB,
        "erb_benchmark_trees": load_erb_benchmark_trees(),
    }
    if qt_ms is not None and hr_bpm is not None:
        resp["qtc_result"] = calculate_qtc(qt_ms, hr_bpm)  # cinsiyetsiz hızlı sorgu
    return resp


@app.post("/api/qtc")
def compute_qtc_endpoint(payload: QtcRequest) -> Dict[str, Any]:
    """Bazett ve Fridericia formülleriyle QTc hesaplar."""
    try:
        return calculate_qtc(payload.qt_ms, payload.hr_bpm, sex=payload.sex, age=payload.age)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
