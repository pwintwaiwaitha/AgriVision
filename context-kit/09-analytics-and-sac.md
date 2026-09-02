# 09 - Analytics, Six Charts, and SAC Export

## Data-honesty contract

Every chart and exported metric must include:

- Metric name and definition
- Unit
- Geography
- Reference period
- Source and URL when available
- Coverage and denominator
- Data status
- Last-updated date
- Known limitations

Missing values remain missing and must be rendered as unavailable. Never use zero as a
visual substitute.

## Six required evidence charts

The PDFs describe the evidence categories but do not contain the actual numerical
dataset. The builder must create chart components and schemas, then use the exact
approved project data when supplied. Do not invent bar values.

### Chart 1 - Agriculture employment share across ASEAN

- Measure: share of employment in agriculture
- Scope: approved ASEAN country records
- Purpose: show the continuing importance of agricultural work
- Cannot prove: average farmer age, succession risk, or productivity

### Chart 2 - Agriculture GDP share across ASEAN

- Measure: agriculture share of GDP
- Purpose: economic context
- Important: it uses a different denominator from employment share
- Cannot prove: a `productivity gap` through direct subtraction from Chart 1

### Chart 3 - Age 60-64 agriculture-employment indicator

- Definition: among employed people aged 60-64, the share working in agriculture
- Show only countries with comparable available records
- Missing countries must be labelled unavailable
- Cannot prove: complete farmer-age distribution or succession status

### Chart 4 - Indonesia agriculture employment by age band

- Purpose: a country case illustration of age distribution
- Label clearly: `Indonesia case illustration`
- Must not be presented as an ASEAN ranking or regional average

### Chart 5 - CY2022 undernourishment/food-exposure comparison

- Reference period: CY2022
- Known coverage: eight countries in the referenced evidence base
- Show the three unavailable countries as missing, not zero
- Cannot prove: that farmer aging directly caused undernourishment

### Chart 6 - Digital-readiness comparison

- Scope: all 11 countries when the approved dataset contains them
- Use only the documented readiness definition and source
- Purpose: guide delivery mode, not judge farmer ability or willingness
- Cannot prove: that higher country income means every farmer owns a smartphone

## Regional scope rules

- Keep Brunei Darussalam, Cambodia, Indonesia, Lao PDR, Malaysia, Myanmar,
  Philippines, Singapore, Thailand, Timor-Leste, and Viet Nam in regional scope.
- Do not add China, Japan, regional aggregates, reference rows, or scenario rows to
  country charts unless the chart specification explicitly calls for them.
- Do not label a descriptive bubble chart as a causal priority score.
- Do not produce `highest risk` rankings from incomplete or incomparable metrics.

## Operational dashboards

Separate these measurement levels:

| Level | Example | Claim boundary |
|---|---|---|
| Activity | Recommendation generated | What the system did |
| Output | Farmer received and reviewed it | What the user received/completed |
| Outcome | Confirmed hours reduced after follow-up | What changed, with measurement method |
| Impact | Sustained continuity attributable to programme | Requires suitable evaluation design |

Recommended operational groups:

- Current-farmer continuity
- Youth exploration, training, viable starts, and retention
- Mentor participation and learning-plan completion
- Livelihood, food, climate, and resource outcomes
- Evidence quality and missingness

## SAC export

Preserve the implementation-PDF fields:

```text
Country
Country_Code
Year
Track1_Hours_Reclaimed
Track2_Youth_Onboarded
Net_Abandonment_Risk_Reduction
```

Add the metadata required for honest analysis:

```text
Metric_Key
Metric_Definition
Unit
Reference_Period
Source
Source_URL
Coverage
Denominator
Data_Status
Last_Updated
Limitations
Track3_Active_Matches
Track3_Completed_Learning_Plans
```

Preferred long-form export schema:

```text
Country,Country_Code,Reference_Period,Track,Metric_Key,Metric_Value,Unit,
Data_Status,Source,Source_URL,Coverage,Denominator,Last_Updated,Limitations
```

`Net_Abandonment_Risk_Reduction` must be empty or labelled scenario/estimated until a
documented definition, baseline, method, and evaluation design exist.

## Export safeguards

- Export generation requires programme-manager or approved analyst permission.
- Aggregate or de-identify records.
- Suppress small groups when re-identification is reasonably possible.
- Store export filters, requester, generated time, schema version, and audit ID.
- Include a `README` sheet or sidecar describing definitions and statuses for Excel.

