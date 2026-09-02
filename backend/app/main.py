"""FastAPI application for the AgriVision demonstration MVP."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal
from uuid import uuid4

import cv2
import numpy as np
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .engines import (
    ENGINE_VERSION,
    irrigation_recommendation,
    rank_bridge_matches,
    run_digital_twin,
)


ROOT_DIR = Path(__file__).resolve().parents[2]
FRONTEND_DIR = ROOT_DIR / "frontend"
MAX_IMAGE_BYTES = 8 * 1024 * 1024

app = FastAPI(
    title="AgriVision MVP API",
    version="1.0.0",
    description="Decision-support prototype for Sustain, Attract and Bridge workflows.",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000", "http://localhost:8000"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


class IrrigationInput(BaseModel):
    farm_id: str = "demo-farm-mm-01"
    soil_moisture_pct: float = Field(ge=0, le=100)
    temp_c: float = Field(default=30, ge=-20, le=70)
    npk_nitrogen_ppm: float = Field(default=40, ge=0)
    confirmed_cycles_this_week: int = Field(default=0, ge=0)
    source_type: Literal["manual", "sensor", "mqtt", "synthetic"] = "manual"


class SimulationInput(BaseModel):
    land_area_ha: float = Field(gt=0)
    initial_capital: float = Field(gt=0)
    tech_level: Literal["LOW", "MEDIUM", "HIGH"]
    climate_shock: bool = False
    price_per_kg: float = Field(ge=0)
    annual_operating_cost: float = Field(ge=0)
    technology_investment: float = Field(ge=0)
    base_labour_hours: float = Field(default=1000, ge=0)
    currency: str = Field(default="USD", min_length=3, max_length=3)


class MentorInput(BaseModel):
    display_name: str
    lat: float = Field(ge=-90, le=90)
    lon: float = Field(ge=-180, le=180)
    crops: list[str]
    offered_ha: float = Field(gt=0)
    matching_consent: bool


class CandidateInput(BaseModel):
    candidate_id: str
    display_name: str
    approximate_area: str
    lat: float = Field(ge=-90, le=90)
    lon: float = Field(ge=-180, le=180)
    crops: list[str]
    preferred_ha: float = Field(gt=0)
    matching_consent: bool


class MatchInput(BaseModel):
    mentor: MentorInput
    candidates: list[CandidateInput]


def envelope(
    data: Any,
    *,
    data_status: str,
    summary: str = "",
    confidence: str = "medium",
    human_review_required: bool = False,
    risks: list[str] | None = None,
    safeguards: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "data": data,
        "meta": {
            "request_id": str(uuid4()),
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "rule_or_model_version": ENGINE_VERSION,
            "data_status": data_status,
        },
        "recommendation_context": {
            "summary": summary,
            "risks": risks or [],
            "safeguards": safeguards or [],
            "confidence": confidence,
            "human_review_required": human_review_required,
        },
    }


@app.get("/", include_in_schema=False)
def website() -> FileResponse:
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/health")
@app.get("/api/v1/health")
def health() -> dict[str, Any]:
    return {"status": "ok", "version": "1.0.0", "mode": "demonstration"}


@app.get("/api/v1/countries")
def countries() -> dict[str, Any]:
    names = [
        ("BN", "Brunei Darussalam"),
        ("KH", "Cambodia"),
        ("ID", "Indonesia"),
        ("LA", "Lao PDR"),
        ("MY", "Malaysia"),
        ("MM", "Myanmar"),
        ("PH", "Philippines"),
        ("SG", "Singapore"),
        ("TH", "Thailand"),
        ("TL", "Timor-Leste"),
        ("VN", "Viet Nam"),
    ]
    return envelope(
        [{"code": code, "name": name} for code, name in names],
        data_status="observed",
        summary="AgriVision regional scope includes all 11 ASEAN Member States.",
        confidence="high",
    )


@app.post("/api/v1/sustain/irrigation/recommend")
def irrigation(payload: IrrigationInput) -> dict[str, Any]:
    result = irrigation_recommendation(
        payload.soil_moisture_pct,
        payload.confirmed_cycles_this_week,
    )
    result["source_type"] = payload.source_type
    return envelope(
        result,
        data_status="synthetic" if payload.source_type == "synthetic" else "calculated",
        summary="Review the illustrative irrigation recommendation before taking action.",
        confidence="low",
        human_review_required=True,
        risks=["Incorrect water volume could harm crops or equipment."],
        safeguards=["Confirm crop, soil, farm area, rainfall and equipment capacity locally."],
    )


@app.post("/api/v1/sustain/crop-screenings")
async def crop_screening(image: UploadFile = File(...)) -> dict[str, Any]:
    if image.content_type not in {"image/jpeg", "image/png"}:
        raise HTTPException(status_code=415, detail="Upload a JPEG or PNG image.")
    content = await image.read(MAX_IMAGE_BYTES + 1)
    if len(content) > MAX_IMAGE_BYTES:
        raise HTTPException(status_code=413, detail="Image must be 8 MB or smaller.")

    decoded = cv2.imdecode(np.frombuffer(content, dtype=np.uint8), cv2.IMREAD_COLOR)
    if decoded is None:
        raise HTTPException(status_code=400, detail="The image could not be decoded.")
    hsv = cv2.cvtColor(decoded, cv2.COLOR_BGR2HSV)
    green = cv2.inRange(hsv, np.array([35, 30, 30]), np.array([90, 255, 255]))
    lesion = cv2.inRange(hsv, np.array([5, 40, 20]), np.array([34, 255, 255]))
    valid_leaf = cv2.bitwise_or(green, lesion)
    valid_pixels = int(cv2.countNonZero(valid_leaf))
    if valid_pixels == 0:
        raise HTTPException(status_code=422, detail="No clear green/yellow/brown leaf area was detected.")
    lesion_pixels = int(cv2.countNonZero(lesion))
    ratio = lesion_pixels / valid_pixels
    label = "POSSIBLE_LEAF_STRESS_REVIEW" if ratio > 0.15 else "NO_LARGE_VISIBLE_LESION_DETECTED"
    result = {
        "screening_label": label,
        "lesion_ratio": round(ratio, 4),
        "lesion_percent": round(ratio * 100, 1),
        "threshold_percent": 15,
        "image_width": int(decoded.shape[1]),
        "image_height": int(decoded.shape[0]),
        "cost_savings_usd": None,
        "limitations": [
            "Colour screening cannot confirm a disease or pest.",
            "Lighting, background and camera quality can change the result.",
        ],
    }
    return envelope(
        result,
        data_status="calculated",
        summary="This is a preliminary colour-based screening, not a confirmed diagnosis.",
        confidence="low",
        human_review_required=ratio > 0.15,
        risks=["A visual similarity may have several different causes."],
        safeguards=["Ask a qualified local extension worker before treatment."],
    )


@app.post("/api/v1/attract/simulations")
def simulation(payload: SimulationInput) -> dict[str, Any]:
    result = run_digital_twin(**payload.model_dump(exclude={"currency"}))
    result["currency"] = payload.currency.upper()
    return envelope(
        result,
        data_status="scenario",
        summary="Compare all three scenarios before considering a major commitment.",
        confidence="low",
        human_review_required=True,
        risks=["Prices, yields, costs and climate conditions may differ from the assumptions."],
        safeguards=["Try a small, reversible pilot and review it with a local professional."],
    )


@app.post("/api/v1/bridge/matches/suggest")
def match_suggestions(payload: MatchInput) -> dict[str, Any]:
    try:
        results = rank_bridge_matches(
            payload.mentor.model_dump(),
            [candidate.model_dump() for candidate in payload.candidates],
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return envelope(
        results,
        data_status="calculated",
        summary="These are explainable suggestions, not assignments.",
        confidence="medium",
        human_review_required=True,
        risks=["A numeric score cannot establish trust, suitability or safety."],
        safeguards=["Require mutual acceptance and safety review before contact release."],
    )


@app.get("/api/v1/analytics/charts")
def analytics_charts() -> dict[str, Any]:
    charts = [
        ("agriculture-employment", "Agriculture employment share across ASEAN"),
        ("agriculture-gdp", "Agriculture GDP share across ASEAN"),
        ("age-60-64", "Age 60-64 agriculture-employment indicator"),
        ("indonesia-age-band", "Indonesia agriculture employment by age band"),
        ("undernourishment-2022", "CY2022 undernourishment comparison"),
        ("digital-readiness", "Digital-readiness comparison"),
    ]
    data = [
        {
            "key": key,
            "title": title,
            "data_status": "missing",
            "message": "Approved numerical dataset has not been added. Values were not invented.",
        }
        for key, title in charts
    ]
    return envelope(
        data,
        data_status="missing",
        summary="Six chart specifications are ready; approved source values are still required.",
        confidence="high",
    )

