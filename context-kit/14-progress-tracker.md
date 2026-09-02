# 14 - Progress Tracker

Update this document as the repository changes. Do not mark an item complete until its
acceptance criteria and relevant tests pass.

## Phase 0 - Audit

- [x] Existing repository inspected
- [x] Current stack and run commands recorded
- [x] Existing user changes preserved
- [x] Gap analysis completed
- [x] File-level implementation plan approved

## Phase 1 - Foundation

- [x] Frontend/backend foundation confirmed
- [x] Typed configuration and `.env.example`
- [ ] Database and migrations
- [ ] Roles and object permissions
- [ ] Adaptation profile
- [ ] Consent records
- [ ] Audit service
- [x] Standard API envelopes
- [x] Health endpoint
- [x] Synthetic seed data with visible labels
- [ ] Foundation tests and CI

## Phase 2 - Sustain

- [x] Telemetry/manual observation intake
- [ ] MQTT adapter or documented stub
- [x] Guarded irrigation recommendation
- [x] Workload-reclaimed estimate
- [x] Crop-image screening
- [ ] Action confirmation
- [ ] Outcome follow-up
- [ ] Farmer dashboard and offline alternative
- [ ] Sustain tests

## Phase 3 - Attract

- [ ] Youth exploration profile
- [ ] Pathway catalogue
- [x] Three-scenario digital twin
- [x] Assumption editor
- [ ] Training/institution referrals
- [x] Attract tests

## Phase 4 - Bridge

- [x] Mentor profile
- [x] Learner profile
- [x] Explainable score components
- [x] Match invitations
- [ ] Two-party acceptance
- [ ] Consent-gated contact release
- [ ] Minor/facilitator safeguards
- [ ] Mentorship plan
- [ ] Pause, end, and safety report
- [ ] Bridge permission and safety tests

## Phase 5 - Analytics

- [ ] Metric and source models
- [ ] Chart 1: agriculture employment share
- [ ] Chart 2: agriculture GDP share
- [ ] Chart 3: age 60-64 indicator
- [ ] Chart 4: Indonesia age-band case
- [ ] Chart 5: CY2022 undernourishment
- [ ] Chart 6: digital readiness
- [x] Missing-data states
- [ ] Activity/output/outcome/impact separation
- [ ] SAC CSV/Excel export
- [ ] Analytics tests

## Phase 6 - Adaptation and UX

- [ ] At least two country profiles
- [ ] At least two language profiles
- [ ] Four connectivity/delivery modes represented
- [ ] Offline drafts and safe sync state
- [ ] Mobile responsive QA
- [ ] Accessibility QA

## Phase 7 - Release

- [ ] Docker and Compose verified
- [ ] Fresh-clone README verified
- [ ] CI green
- [ ] No secrets/private sample data
- [ ] Production configuration validated
- [ ] Security/privacy review
- [ ] Demonstration script verified
- [ ] Release notes prepared

## Decisions log

| Date | Decision | Reason | Files/impact | Decided by |
|---|---|---|---|---|
| 2026-09-02 | Build a dependency-light FastAPI + static frontend MVP | Runs from one service and demonstrates all three tracks | `backend/`, `frontend/` | Project team |
| 2026-09-02 | Keep analytics values missing until approved sources are supplied | Prevents synthetic values from appearing as evidence | Analytics API and UI | Project governance |

## Known issues

| ID | Severity | Issue | Owner | Next action | Status |
|---|---|---|---|---|---|
| AGRI-001 | High | No persistent database, user accounts or role permissions yet | Backend | Implement Phase 1 data and identity services | Open |
| AGRI-002 | High | Hardware/MQTT flow is a documented stub only | IoT | Add adapter and hardware-in-the-loop tests before real control | Open |
| AGRI-003 | Medium | Bridge acceptance is a UI demonstration and is not persisted | Product | Add invitation, consent and safety workflow tables | Open |
| AGRI-004 | Medium | Approved values and sources for the six charts are not supplied | Research | Add source records and verified datasets | Open |

## Latest verified run

- Commit: this implementation commit (see repository history for SHA)
- Date: 2026-09-02
- Backend command: `cd backend && python -m uvicorn app.main:app --host 127.0.0.1 --port 8000`
- Frontend command: served by FastAPI at `/`
- Database: not implemented in this demonstration slice
- Tests passed: Python compilation, 15 direct engine assertions, HTML structure check, JavaScript syntax check
- Known failures: full pytest/API smoke run was not available in the build workspace because project dependencies could not be downloaded; run it from a networked environment
