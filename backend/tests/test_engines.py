from app.engines import (
    geography_score,
    irrigation_recommendation,
    rank_bridge_matches,
    run_digital_twin,
)


def test_irrigation_threshold_and_volume() -> None:
    below = irrigation_recommendation(24, 8)
    at_threshold = irrigation_recommendation(30, 0)
    assert below["status"] == "PUMP_ON_RECOMMENDED"
    assert below["illustrative_volume_l"] == 75
    assert below["weekly_reclaimed_hours"] == 6
    assert at_threshold["status"] == "PUMP_OFF_RECOMMENDED"


def test_geography_score_boundaries() -> None:
    assert geography_score(10) == 1
    assert geography_score(100) == 0
    assert round(geography_score(55), 3) == 0.5


def test_match_requires_consent_and_hides_contact() -> None:
    mentor = {
        "lat": 16.8409,
        "lon": 96.1735,
        "crops": ["rice"],
        "offered_ha": 2,
        "matching_consent": True,
    }
    candidates = [
        {
            "candidate_id": "y-1",
            "display_name": "Youth A",
            "approximate_area": "Yangon Region",
            "lat": 16.85,
            "lon": 96.18,
            "crops": ["rice"],
            "preferred_ha": 2,
            "matching_consent": True,
            "phone": "must-not-leak",
        }
    ]
    result = rank_bridge_matches(mentor, candidates)
    assert result[0]["score_percent"] == 100
    assert "phone" not in result[0]
    assert result[0]["contact_released"] is False


def test_simulator_returns_three_five_year_scenarios() -> None:
    result = run_digital_twin(
        land_area_ha=2,
        initial_capital=10000,
        tech_level="HIGH",
        climate_shock=True,
        price_per_kg=0.5,
        annual_operating_cost=1000,
        technology_investment=2000,
        base_labour_hours=1000,
    )
    assert result["data_status"] == "scenario"
    assert len(result["scenarios"]) == 3
    assert all(len(scenario["years"]) == 5 for scenario in result["scenarios"])
    assert result["assumptions"]["climate_factor"] == 0.85

