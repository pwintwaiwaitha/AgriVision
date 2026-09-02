"""Pure calculation engines for the AgriVision demonstration MVP."""

from __future__ import annotations

from math import asin, cos, radians, sin, sqrt
from typing import Any


ENGINE_VERSION = "agrivision-mvp-1.0.0"


def irrigation_recommendation(
    soil_moisture_pct: float,
    confirmed_cycles_this_week: int = 0,
) -> dict[str, Any]:
    """Return guarded prototype irrigation decision support."""
    if not 0 <= soil_moisture_pct <= 100:
        raise ValueError("Soil moisture must be between 0 and 100 percent.")
    if confirmed_cycles_this_week < 0:
        raise ValueError("Confirmed cycles cannot be negative.")

    needs_water = soil_moisture_pct < 30.0
    volume = round((30.0 - soil_moisture_pct) * 12.5, 2) if needs_water else 0.0

    return {
        "status": "PUMP_ON_RECOMMENDED" if needs_water else "PUMP_OFF_RECOMMENDED",
        "soil_moisture_pct": soil_moisture_pct,
        "threshold_pct": 30.0,
        "illustrative_volume_l": volume,
        "weekly_reclaimed_hours": round(confirmed_cycles_this_week * 0.75, 2),
        "data_status": "calculated",
        "engine_version": ENGINE_VERSION,
        "assumptions": [
            "12.5 litres per moisture-percentage-point is a classroom MVP assumption.",
            "Each confirmed automated cycle is estimated to reclaim 0.75 labour hours.",
        ],
        "limitations": [
            "Farm area, crop, soil, rainfall, root depth, irrigation efficiency and pump capacity are not included.",
            "This result must not activate real equipment.",
        ],
    }


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate geodesic distance between two WGS84 coordinate pairs."""
    for value, minimum, maximum, label in (
        (lat1, -90, 90, "latitude"),
        (lat2, -90, 90, "latitude"),
        (lon1, -180, 180, "longitude"),
        (lon2, -180, 180, "longitude"),
    ):
        if not minimum <= value <= maximum:
            raise ValueError(f"Invalid {label}.")

    earth_radius_km = 6371.0088
    phi1, phi2 = radians(lat1), radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)
    a = sin(delta_phi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(delta_lambda / 2) ** 2
    return earth_radius_km * 2 * asin(sqrt(a))


def geography_score(distance_km: float) -> float:
    if distance_km <= 10:
        return 1.0
    if distance_km >= 100:
        return 0.0
    return (100 - distance_km) / 90


def scale_score(preferred_ha: float, offered_ha: float) -> float:
    if preferred_ha <= 0 or offered_ha <= 0:
        raise ValueError("Land-area preferences must be greater than zero.")
    return max(0.0, 1 - abs(preferred_ha - offered_ha) / max(preferred_ha, offered_ha))


def rank_bridge_matches(
    mentor: dict[str, Any],
    candidates: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Rank consented learner profiles without exposing contact details."""
    if not mentor.get("matching_consent"):
        raise ValueError("The mentor must opt in to matching.")

    mentor_crops = {str(crop).strip().lower() for crop in mentor.get("crops", [])}
    results: list[dict[str, Any]] = []

    for candidate in candidates:
        if not candidate.get("matching_consent"):
            continue
        distance = haversine_km(
            float(mentor["lat"]),
            float(mentor["lon"]),
            float(candidate["lat"]),
            float(candidate["lon"]),
        )
        geo = geography_score(distance)
        candidate_crops = {str(crop).strip().lower() for crop in candidate.get("crops", [])}
        crop = 1.0 if mentor_crops & candidate_crops else 0.0
        scale = scale_score(float(candidate["preferred_ha"]), float(mentor["offered_ha"]))
        total = 0.4 * geo + 0.4 * crop + 0.2 * scale
        results.append(
            {
                "candidate_id": candidate["candidate_id"],
                "display_name": candidate["display_name"],
                "approximate_area": candidate.get("approximate_area", "Not provided"),
                "shared_crops": sorted(mentor_crops & candidate_crops),
                "distance_km": round(distance, 1),
                "score": round(total, 3),
                "score_percent": round(total * 100),
                "components": {
                    "geography": round(geo, 3),
                    "crop": round(crop, 3),
                    "scale": round(scale, 3),
                },
                "contact_released": False,
                "consent_status": "WAITING_FOR_MUTUAL_ACCEPTANCE",
                "explanation": "Score uses 40% geography, 40% crop overlap and 20% land-scale preference.",
            }
        )

    return sorted(results, key=lambda item: item["score"], reverse=True)[:3]


def run_digital_twin(
    *,
    land_area_ha: float,
    initial_capital: float,
    tech_level: str,
    climate_shock: bool,
    price_per_kg: float,
    annual_operating_cost: float,
    technology_investment: float,
    base_labour_hours: float,
) -> dict[str, Any]:
    """Return conservative, central and stress five-year scenarios."""
    if land_area_ha <= 0:
        raise ValueError("Land area must be greater than zero.")
    if initial_capital <= 0:
        raise ValueError("Initial capital must be greater than zero.")
    if min(price_per_kg, annual_operating_cost, technology_investment, base_labour_hours) < 0:
        raise ValueError("Financial and labour inputs cannot be negative.")

    tech_level = tech_level.upper()
    if tech_level not in {"LOW", "MEDIUM", "HIGH"}:
        raise ValueError("Technology level must be LOW, MEDIUM or HIGH.")

    tech_yield_factor = {"LOW": 1.0, "MEDIUM": 1.15, "HIGH": 1.35}[tech_level]
    labour_factor = {"LOW": 1.0, "MEDIUM": 0.8, "HIGH": 0.6}[tech_level]
    climate_factor = 1.0
    if climate_shock:
        climate_factor = 0.85 if tech_level == "HIGH" else 0.50

    scenario_rules = {
        "conservative": {"yield": 0.90, "price": 0.90, "cost": 1.10},
        "central": {"yield": 1.00, "price": 1.00, "cost": 1.00},
        "stress": {"yield": 0.75, "price": 0.80, "cost": 1.20},
    }
    scenarios: list[dict[str, Any]] = []

    for name, factors in scenario_rules.items():
        years: list[dict[str, Any]] = []
        cumulative_profit = 0.0
        for year in range(1, 6):
            yield_kg = (
                land_area_ha
                * 2500
                * tech_yield_factor
                * climate_factor
                * factors["yield"]
            )
            adjusted_price = price_per_kg * factors["price"] * (1.02 ** (year - 1))
            revenue = yield_kg * adjusted_price
            operating_cost = annual_operating_cost * factors["cost"] * (1.03 ** (year - 1))
            total_cost = operating_cost + (technology_investment if year == 1 else 0)
            net_profit = revenue - total_cost
            cumulative_profit += net_profit
            roi_pct = ((cumulative_profit - initial_capital) / initial_capital) * 100
            years.append(
                {
                    "year": year,
                    "yield_kg": round(yield_kg, 2),
                    "revenue": round(revenue, 2),
                    "operating_cost": round(total_cost, 2),
                    "net_profit": round(net_profit, 2),
                    "cumulative_roi_pct": round(roi_pct, 2),
                    "labour_hours": round(base_labour_hours * labour_factor, 2),
                }
            )
        scenarios.append(
            {
                "name": name,
                "years": years,
                "five_year_net_profit": round(cumulative_profit, 2),
                "five_year_roi_pct": years[-1]["cumulative_roi_pct"],
            }
        )

    return {
        "data_status": "scenario",
        "engine_version": ENGINE_VERSION,
        "scenarios": scenarios,
        "assumptions": {
            "base_yield_kg_ha": 2500,
            "technology_yield_factor": tech_yield_factor,
            "technology_labour_factor": labour_factor,
            "climate_factor": climate_factor,
            "annual_price_growth_pct": 2,
            "annual_cost_growth_pct": 3,
        },
        "disclaimer": "Illustrative scenarios based on user inputs and MVP assumptions; not forecasts or guarantees.",
    }

