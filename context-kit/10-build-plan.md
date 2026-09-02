# 10 - Build Plan

The builder must inspect the existing repository before editing. Preserve working code,
configuration, assets, and user changes. Do not initialize a replacement project on top
of an existing application without explicit approval.

## Phase 0 - Repository audit

Deliverables:

- Existing stack, routes, models, scripts, tests, and deployment summary
- Gap list mapped to this context kit
- Conflict and migration risks
- Proposed file-level implementation plan

Exit criteria:

- No code changes until the existing structure is understood.
- Unrelated user changes remain untouched.

## Phase 1 - Foundation

Build:

- Backend/frontend skeleton only if missing
- Configuration and `.env.example`
- Database session and first migration
- User roles and backend permission dependencies
- Adaptation profile and country configuration
- Standard API response/error envelopes
- Audit service
- Health endpoint
- Seeded demo accounts and visibly synthetic data

Exit criteria:

- Application starts with documented commands.
- CI runs lint, type checks, and foundation tests.
- Production mode cannot use demo authentication silently.

## Phase 2 - Track 1 Sustain

Build:

- Observation and telemetry ingestion
- Irrigation recommendation engine with guardrails
- Workload-reclaimed calculation
- Farmer dashboard
- Crop-image screening with cautious output
- Action confirmation and outcome follow-up

Exit criteria:

- Threshold boundaries and invalid inputs are tested.
- Real equipment activation is impossible in the MVP.
- Image result displays limitations and human review.
- Weekly hours count only confirmed eligible cycles.

## Phase 3 - Track 2 Attract

Build:

- Exploration profile
- Pathway catalogue and filters
- Five-year three-scenario simulator
- Assumption editor and comparison UI
- Institution/training referral view

Exit criteria:

- Conservative, central, and stress outputs are reproducible.
- All assumptions and scenario status are visible.
- No income, land, or success guarantee appears.

## Phase 4 - Track 3 Bridge

Build:

- Mentor/learner profiles
- Explainable matching engine
- Invitations and two-party response
- Consent-gated contact release
- Mentorship plan, check-in, pause, end, and safety report
- Minor and facilitator safeguards

Exit criteria:

- Contact cannot be retrieved before mutual consent and safety checks.
- Decline, pause, and end work without penalty.
- Private fields never appear in suggestion responses.

## Phase 5 - Analytics and six charts

Build:

- Metric/source model
- Chart API and accessible chart components
- Six chart specifications from `09-analytics-and-sac.md`
- Data-status badges and missing-data rendering
- Activity/output/outcome/impact separation
- Audited SAC CSV/Excel export

Exit criteria:

- No fabricated chart numbers.
- Every chart shows source, unit, period, coverage, status, and limitations.
- Missing data do not render as zero.

## Phase 6 - Adaptation and resilience

Build:

- Country/language/config switching
- Offline draft and safe sync queue
- Low-bandwidth image and data behaviour
- Facilitator-assisted views
- Accessibility improvements

Exit criteria:

- At least two country/language/connectivity profiles work end to end.
- Consequential operations are not falsely confirmed while offline.

## Phase 7 - Hardening and delivery

Build:

- Full test suite
- Error and loading-state polish
- Logging and audit inspection
- Docker setup
- CI
- Seed reset command
- API and deployment documentation
- Security and privacy review

Exit criteria:

- All acceptance tests pass.
- Repository has no secrets or private sample data.
- A fresh clone can run by following the README.

## Commit strategy

Prefer small, reviewable commits by phase or bounded feature. Examples:

- `docs: add AgriVision development context kit`
- `feat: add role and adaptation foundation`
- `feat: implement guarded irrigation recommendation`
- `feat: add consent-based bridge matching`
- `feat: add evidence-aware analytics export`
- `test: cover safety and data-status rules`

