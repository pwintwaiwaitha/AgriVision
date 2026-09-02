# AgriVision

AgriVision is a runnable demonstration MVP for ASEAN farmer continuity. It brings
together three connected tracks: immediate decision support for current farmers
(`Sustain`), realistic farming scenarios for interested youth (`Attract`), and
consent-based knowledge transfer (`Bridge`).

The repository also contains the authoritative development context distilled from
`AgriVision_System_Prompt.pdf` and
`AgriVision_System_Implementation_Prompt.pdf`.

> **Demonstration status:** this MVP does not control real equipment, diagnose crop
> disease, provide financial advice, or release private contact information.

## What works now

- Responsive single-page website covering Overview, Sustain, Attract, Bridge and Analytics.
- Guarded irrigation recommendation from a manual moisture observation.
- Real OpenCV HSV image processing for preliminary visible leaf-colour screening.
- Five-year conservative, central and stress digital-twin scenarios.
- Explainable mentorship ranking using geography, crop overlap and land scale.
- Consent filtering and hidden contact details in the matching flow.
- Six analytics chart specifications that visibly report missing data instead of inventing values.
- Versioned FastAPI endpoints, standard evidence envelopes and health checks.

## Run locally

### Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
cd backend
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Open <http://127.0.0.1:8000>. API documentation is available at
<http://127.0.0.1:8000/docs>.

### Docker

```bash
docker compose up --build
```

Then open <http://127.0.0.1:8000>.

## Test

```bash
cd backend
python -m pytest
```

## Repository structure

```text
AgriVision/
├── backend/          FastAPI application, engines and tests
├── frontend/         Responsive HTML, CSS and JavaScript interface
├── context-kit/      Product, architecture, safety and build specifications
├── docker-compose.yml
├── .env.example
└── README.md
```

## How future builders should use the context kit

1. Read every document in `context-kit/` before changing code.
2. Inspect the existing repository and preserve working features and user changes.
3. Treat `MUST`, `MUST NOT`, and acceptance criteria as binding.
4. Use the three-track model everywhere:
   - Track 1: Sustain
   - Track 2: Attract
   - Track 3: Bridge
5. Keep prototype calculations labelled as illustrative. Never present synthetic,
   estimated, or scenario data as observed impact.
6. Implement the work in the phases defined in `10-build-plan.md`.
7. Update `14-progress-tracker.md` after each completed phase.

## Document index

| File | Purpose |
|---|---|
| `00-source-of-truth.md` | Precedence rules and resolved PDF conflicts |
| `01-project-overview.md` | Vision, problem, goals, scope, and non-goals |
| `02-product-requirements.md` | Three-track functions and acceptance criteria |
| `03-system-architecture.md` | Complete frontend, backend, data, AI, and IoT architecture |
| `04-user-roles-permissions.md` | Role model and least-privilege rules |
| `05-ui-ux-rules.md` | Screens, design system, accessibility, and offline behaviour |
| `06-api-standards.md` | REST/WebSocket contracts and response envelopes |
| `07-database-schema.md` | MVP entities, relationships, and data classifications |
| `08-engine-specifications.md` | IoT, CV, matching, and digital-twin algorithms |
| `09-analytics-and-sac.md` | Six charts, metric rules, and SAC export |
| `10-build-plan.md` | Safe implementation order and deliverables |
| `11-code-standards.md` | Repository, Python, TypeScript, security, and documentation rules |
| `12-testing-plan.md` | Unit, API, integration, safety, accessibility, and data-honesty tests |
| `13-deployment-and-operations.md` | Local setup, Docker, seeding, CI, logging, and deployment |
| `14-progress-tracker.md` | Builder checklist and decisions log |
| `15-builder-master-prompt.md` | Copyable execution prompt for an AI builder |

## Core project statement

AgriVision is an ASEAN-wide farmer-continuity and agricultural-transition
platform. It uses technology to help current farmers continue more safely,
help interested youth explore agriculture realistically, and support voluntary,
consent-based knowledge transfer between generations. It supports SDG 2 - Zero
Hunger, but it must never claim that the prototype has already produced regional
impact.
