# 08 - Engine Specifications

All engines must be deterministic for the same validated inputs unless a documented
model version explicitly introduces controlled stochastic behaviour. Each result
includes engine version, input IDs, data status, assumptions, confidence, limitations,
human-review requirement, and generated timestamp.

## Engine 1 - IoT irrigation and workload support

### Required input

```json
{
  "farm_id": "uuid",
  "soil_moisture_pct": 24.0,
  "temp_c": 31.0,
  "npk_nitrogen_ppm": 42.0,
  "observed_at": "ISO-8601 timestamp",
  "source_type": "manual|sensor|mqtt|synthetic",
  "unit_system": "metric"
}
```

Phosphorus and potassium may be added with the same validation pattern. The source
PDF mentions NPK but its example payload includes only nitrogen; do not pretend P and
K were measured when they are absent.

### Prototype rule

If `soil_moisture_pct < 30.0`:

```text
status = PUMP_ON_RECOMMENDED
illustrative_volume_l = (30.0 - soil_moisture_pct) * 12.5
```

Otherwise:

```text
status = PUMP_OFF_RECOMMENDED
illustrative_volume_l = 0
```

### Guardrails

- This is illustrative decision support, never a real equipment command.
- Reject moisture outside 0-100.
- A stale, missing, low-quality, or synthetic reading must be labelled.
- Farm area, crop, soil, rainfall, root depth, irrigation efficiency, and equipment
  capacity are missing from the formula; list them as limitations.
- Require human/local review before real application.

### Reclaimed labour

```text
weekly_reclaimed_hours = confirmed_eligible_automated_cycles * 0.75
```

Count only completed, confirmed cycles. Label 0.75 hours as an MVP assumption, not a
measured regional standard.

## Engine 2 - Crop-image screening

### MVP pipeline

1. Decode a validated JPEG/PNG safely.
2. Normalize orientation and resize for bounded processing.
3. Convert RGB/BGR to HSV.
4. Calculate green-pixel and yellow/brown lesion-candidate masks.
5. Compute `lesion_ratio = lesion_candidate_pixels / valid_leaf_pixels`.
6. If ratio is greater than 0.15, return `POSSIBLE_LEAF_STRESS_REVIEW`.
7. Otherwise return `NO_LARGE_VISIBLE_LESION_DETECTED`.

Do not label the result `Leaf Blight` or `Pest Damage` as confirmed solely from colour.

### Output

- Screening label
- Lesion ratio
- Confidence and reason
- Image-quality warnings
- Possible categories, clearly labelled preliminary
- Organic/low-risk management option for local review
- Human-review flag
- Limitations
- Engine/model version

`input_cost_savings_usd` must remain null unless a documented calculation has cost
inputs, currency, geography, reference period, and assumptions.

## Engine 3 - Bridge succession/mentorship matcher

This is Track 3, not Track 2.

### Eligibility

- Both profiles opted into matching.
- Required consent is current.
- Visibility and programme-scope rules permit comparison.
- Minor safeguarding requirements are satisfied before any direct-contact step.

### Score

```text
S = 0.4 * S_geo + 0.4 * S_crop + 0.2 * S_scale
```

#### Geography component

Let `d` be geodesic distance in kilometres:

```text
S_geo = 1.0                         when d <= 10
S_geo = (100 - d) / 90              when 10 < d < 100
S_geo = 0.0                         when d >= 100
```

Use PostGIS or a Haversine calculation. Do not calculate distance from unprojected
latitude/longitude with a simple Euclidean formula.

#### Crop component

Use disclosed crop/livelihood tags:

- `1.0`: at least one exact domain overlap
- `0.5`: related configured category overlap
- `0.0`: no overlap
- Missing: do not silently convert to zero; mark the component unavailable and explain
  the reduced confidence.

#### Scale component

For positive disclosed preferred and offered areas:

```text
S_scale = max(0, 1 - abs(preferred_ha - offered_ha) /
                    max(preferred_ha, offered_ha))
```

When area is missing, show a data gap and reduce confidence. Do not infer land
ownership from land preference.

### Result

Return at most three suggestions with component scores, total score, matching reasons,
missing data, safeguarding state, and next step. Never return private contact details.

## Engine 4 - Digital twin and gamified simulator

### Required inputs

- Land area in hectares
- Initial capital and ISO currency
- Crop or livelihood
- Technology level: low, medium, high
- Climate-shock toggle or configured stress profile
- Price per kg or documented demo value
- Operating cost categories
- Technology investment and maintenance cost
- Labour hours/cost
- Five-year assumption set

### Source-PDF demonstration assumptions

- Base yield: 2,500 kg/ha
- High technology yield factor: +35%
- High technology labour factor: -40%
- Climate shock without high IoT support: -50% yield
- Climate shock with high technology: -15% yield

These values are prototype scenario assumptions, not forecasts or observed regional
effects.

### Scenario set

Produce:

- Conservative
- Central
- Stress

Each scenario must show the exact factors used. Do not apply two climate factors to the
same scenario unintentionally.

### Annual calculations

```text
yield_kg = land_area_ha * base_yield_kg_ha * tech_factor * climate_factor
revenue = yield_kg * price_per_kg
operating_cost = sum(year_cost_categories)
net_profit = revenue - operating_cost
roi_pct = ((cumulative_net_profit - initial_investment) / initial_investment) * 100
```

Handle zero initial investment without division by zero. Use decimal money arithmetic.

### Output

Return yearly and cumulative yield, revenue, costs, net profit, ROI, labour, assumptions,
warnings, data status, and calculation version. Allow JSON/CSV export.

## Engine 5 - Recommendation policy

Wrap engine calculations into the user-facing recommendation format:

- User goal
- Context used
- Plain-language recommendation
- Why it may help
- Assumptions and gaps
- Risks and safeguards
- Confidence and explanation
- Human reviewer and timing
- One practical, reversible next action

The calculation engine must not bypass this policy for consequential results.

