# 02 - Product Requirements

## Global requirements

The system MUST:

- Ask or derive the active user role before showing protected workflows.
- Ask for the minimum context needed for the current task.
- Support all 11 ASEAN countries without assuming identical conditions.
- Display data status and prototype limitations near consequential results.
- Maintain an audit event for consequential recommendations, simulations, matches,
  consent changes, contact release, exports, and administrator actions.
- Allow users to correct their data and withdraw optional consent.
- Provide loading, empty, error, offline, and missing-data states.

The system MUST NOT:

- Treat missing data as zero.
- Promise farming success, yield, profit, financing, land, employment, or matching.
- Expose exact location or contact details without permission.
- present scenario or synthetic data as observed impact.
- Use registration count as proof of youth retention or farm continuity.

## Track 1 - Sustain

### S1. Farmer support profile

Capture goals, crops, farm scale, constraints, preferred language, accessibility,
connectivity, available equipment, and voluntarily supplied context.

Acceptance criteria:

- Optional fields may remain unknown.
- Unknown values are displayed as unknown, not converted to defaults without notice.
- The user can edit or delete optional profile information.

### S2. IoT and manual observation intake

Accept soil-moisture, temperature, and NPK readings from REST, simulated sensors,
manual entry, and an MQTT adapter.

Acceptance criteria:

- Every reading stores unit, timestamp, source, farm, device or entry method, and
  status.
- Stale or invalid readings do not create a normal recommendation.
- The MVP never activates a real physical pump.

### S3. Irrigation decision support

Run the prototype threshold rule and return a recommendation, assumptions,
confidence, safeguards, human-review status, and next step.

Acceptance criteria:

- Moisture below 30% creates `PUMP_ON_RECOMMENDED`, not an unqualified real-world
  command.
- Proposed volume is marked illustrative.
- The result provides a low-cost/manual alternative.
- The user may record the action actually taken and later record the outcome.

### S4. Workload-reclaimed estimate

Estimate 0.75 hours per confirmed automated cycle for the demonstration.

Acceptance criteria:

- Weekly total equals confirmed eligible cycles multiplied by 0.75 hours.
- The UI labels it as an estimate based on a prototype assumption.
- Unconfirmed recommendations do not count as completed cycles.

### S5. Crop-image screening

Accept JPEG or PNG leaf images and perform a preliminary lesion-colour analysis.

Acceptance criteria:

- File type and size are validated.
- Output uses cautious language and includes confidence and limitations.
- High-risk or unclear results recommend qualified local review.
- No chemical quantity or unsafe application instruction is generated.

## Track 2 - Attract

### A1. Youth exploration profile

Capture interests, skills, time, location, language, accessibility, connectivity,
land-access pathway, and capital constraints. Do not assume land ownership.

### A2. Pathway discovery

Show several realistic pathways such as production, farm services, agritech,
processing, logistics, marketing, training, or apprenticeships.

Acceptance criteria:

- Each pathway shows skills, time, cost range, risks, support needs, and assumptions.
- The system provides a low-cost trial before recommending a major commitment.
- Outcomes are explicitly not guaranteed.

### A3. Digital twin

Compare conservative, central, and stress scenarios over five years.

Acceptance criteria:

- Inputs and editable assumptions remain visible.
- Outputs show revenue, operating costs, net profit, ROI, labour, and yield.
- Scenario outputs are labelled calculated scenarios, not forecasts.
- Missing price or cost inputs trigger an explicit demo assumption or an incomplete
  result, never a hidden guess.

### A4. Training and institution referrals

Provide verified local institutions when available. If none are verified, show a
data gap and suggest a facilitator-assisted next step.

## Track 3 - Bridge

### B1. Mentor and learner profiles

Create profiles containing only disclosed matching attributes. Separate matching
data from private contact data.

### B2. Explainable match suggestions

Rank up to three candidates using geography, crop/livelihood compatibility, and
scale preference. Explain the component scores and missing information.

Acceptance criteria:

- Results are suggestions, not assignments.
- No contact details appear before mutual consent.
- Users can decline without penalty.
- A facilitator pathway is available.

### B3. Consent workflow

Record separate consent from each party for matching, contact release, mentorship,
and optional knowledge capture.

Acceptance criteria:

- Consent has purpose, version, timestamp, status, and withdrawal timestamp.
- Contact release requires current consent from both parties.
- A minor cannot enter unsupervised contact release.

### B4. Mentorship plan

After mutual acceptance, create goals, cadence, tasks, boundaries, review date,
escalation contact, and exit options.

### B5. Safeguarding and exit

Allow either participant to pause or end a match. Provide reporting and human
escalation for harassment, coercion, discrimination, exploitation, unsafe work,
or inappropriate contact.

## Cross-track adaptation

Create an adaptation profile containing country, subnational area, language,
literacy/accessibility needs, livelihood, farm scale/tenure where voluntarily
provided, connectivity, available institutions, and verified climate/market context.

Choose one delivery mode:

- Offline-assisted
- Low-bandwidth digital
- Connected assisted
- Connected self-service

