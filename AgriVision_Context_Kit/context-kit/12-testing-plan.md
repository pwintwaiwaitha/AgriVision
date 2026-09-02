# 12 - Testing Plan

Tests must verify the domain rules and the safeguards around them. A passing happy-path
demo alone is not sufficient.

## Backend unit tests

### IoT engine

- Moisture `29.9` returns `PUMP_ON_RECOMMENDED`.
- Moisture `30.0` and above returns `PUMP_OFF_RECOMMENDED`.
- Moisture below 0 or above 100 is rejected.
- Volume calculation matches the documented formula.
- Proposed volume is labelled illustrative.
- Stale/synthetic readings carry correct status and warnings.
- Weekly reclaimed hours count only confirmed eligible cycles.

### Crop-image engine

- Valid JPEG and PNG are accepted.
- Unsupported, oversized, corrupted, and decompression-risk images are refused safely.
- Mask and lesion ratio are deterministic for fixtures.
- Exactly 15% follows the specified `greater than 15%` boundary.
- Output does not claim confirmed leaf blight or pest damage from HSV alone.
- Cost savings remain null without documented cost inputs.
- Low-quality image produces a quality warning or indeterminate result.

### Matching engine

- Geography score equals 1 at or below 10 km and 0 at or above 100 km.
- Linear values between 10 and 100 km are correct.
- Haversine or PostGIS distance handles realistic coordinates.
- Weighted score equals `0.4 geo + 0.4 crop + 0.2 scale`.
- Missing components are not silently set to zero.
- No suggestion is produced without opt-in consent.
- Private contact fields cannot appear in match result schemas.

### Digital twin

- Baseline yield uses 2,500 kg/ha.
- High technology applies +35% yield and -40% labour once.
- Climate factors apply correctly and are not duplicated.
- Five yearly results and cumulative totals reconcile.
- Revenue, cost, profit, and ROI use decimal arithmetic.
- Zero investment does not divide by zero.
- Conservative, central, and stress scenarios are reproducible.

### Analytics

- Missing input remains null/missing, not zero.
- Metric metadata validation rejects absent definitions/units/status where required.
- Employment and GDP shares are not directly subtracted into a `productivity gap`.
- Scenario and synthetic records cannot be exported as observed.

## Permission and consent tests

- A farmer cannot read another farmer's private farm.
- A youth cannot read mentor contact before mutual consent.
- One-sided match acceptance does not release contact.
- Withdrawn consent blocks future protected use.
- Researcher receives de-identified/approved data only.
- Facilitator access is limited to assigned scope.
- Admin routes require administrator role.
- Minor direct-contact flow requires configured safeguarding review.
- Safeguarding event details are restricted from ordinary programme users.

## API tests

- Validation errors follow the standard envelope.
- Request IDs are returned and logged.
- Response metadata includes status, time, and engine version where applicable.
- Idempotency prevents duplicate consent/contact/export actions.
- Object-level authorization cannot be bypassed by changing an ID in a request.
- Image errors do not return internal paths or stack traces.
- OpenAPI includes every required endpoint and schema.

## Integration tests

- REST telemetry creates an observation, recommendation, and audit event.
- Simulated MQTT message follows the same normalization path as REST.
- Crop screening stores protected image reference and result metadata.
- Scenario creates all three variants and exportable results.
- Match suggestion to mutual consent to contact release works end to end.
- SAC export includes filter, schema version, source/status fields, and audit record.

## Frontend tests

- Role-aware navigation shows permitted routes and handles server denial.
- Status badges render for observed, user-provided, calculated, scenario, synthetic,
  and missing values.
- Missing data display `Data unavailable`, not `0`.
- Simulation assumptions remain visible beside results.
- Bridge UI never displays private contact before authorized release.
- Offline queue distinguishes pending from server-confirmed actions.
- Error messages identify fields without exposing internals.

## Accessibility tests

- Automated axe checks on critical pages.
- Complete keyboard path for primary flows.
- Focus moves to validation summary after failed submission.
- Charts include accessible summary and data table.
- Colour is not the only status signal.
- 200% zoom and 360 px layout do not hide primary actions.

## End-to-end demonstration tests

1. Sustain: enter a low moisture reading, review illustrative advice, confirm an
   action, and record a follow-up outcome.
2. Attract: complete an exploration profile and compare three digital-twin scenarios.
3. Bridge: opt in two demo users, generate suggestions, accept both sides, release
   contact, create a learning plan, then pause or end safely.
4. Adaptation: switch country, language, and connectivity mode.
5. Analytics: view six chart shells/data, missingness, metadata, and an SAC export.

## CI quality gates

- Backend lint and formatting
- Backend type check
- Backend unit/API/integration tests
- Frontend lint and type check
- Frontend unit/component tests
- Critical Playwright flows
- Dependency and secret scan
- Production build

