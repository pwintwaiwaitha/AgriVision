# 13 - Deployment and Operations

## Local developer experience

The repository README must provide one verified setup path for macOS, Windows, and
Linux where practical. A fresh clone should not require undocumented global tools.

Suggested layout:

```text
AgriVision/
├── frontend/
├── backend/
├── context-kit/
├── data/
├── docker-compose.yml
├── .env.example
└── README.md
```

## Local commands

Document the final verified commands. The expected pattern is:

```bash
# Backend
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
alembic upgrade head
python -m app.seed.demo
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# Frontend, separate terminal
cd frontend
npm install
npm run dev
```

Windows activation must be documented separately. Do not tell users to run `cd` into a
directory when they are already inside it.

## Docker

Provide:

- Backend multi-stage or slim production Dockerfile
- Frontend build/serve Dockerfile where applicable
- `docker-compose.yml` for app, database, and optional MQTT broker
- Health checks
- Non-root application user
- Persistent database volume for local container mode

The default Docker configuration must not expose a real equipment-control interface.

## Environment modes

### Development

- Debug-friendly logs
- SQLite allowed
- Demo authentication optionally enabled
- Synthetic seeding allowed and visibly labelled
- MQTT and external integrations optional

### Test

- Isolated temporary database
- Fixed clocks/seeds where needed
- No external network calls
- Deterministic model fixtures

### Production

- PostgreSQL/PostGIS
- Secure authentication
- Demo authentication disabled
- Synthetic seed disabled
- Explicit CORS origins
- HTTPS and protected secrets
- Rate limits and file-processing bounds
- Backup, retention, and access policies

## Seed data

- Seed records must use fictional names and non-sensitive approximate locations.
- Every seeded observation, metric, recommendation, and scenario has
  `data_status: synthetic`.
- Provide an idempotent seed command and a safe development reset command.
- Do not seed private real phone numbers, email addresses, precise locations, or images.

## Observability

- `/health` reports liveness and safe version details.
- Add readiness checks for database and required configured services.
- Structured error logging uses request IDs.
- Track performance of image processing and simulation endpoints.
- Monitor authorization failures, export generation, and safeguarding queue health
  without exposing private content in general telemetry.

## Data retention

Configuration must define retention for:

- Uploaded crop images
- Raw sensor payloads
- Contact-release information
- Private mentorship records
- Safeguarding records
- Audit events
- Generated exports

Deletion or withdrawal must respect legal/safety requirements while minimizing retained
personal data.

## GitHub Actions

On pull requests:

1. Install pinned backend/frontend dependencies.
2. Run format, lint, and type checks.
3. Run backend and frontend tests.
4. Run critical end-to-end tests.
5. Scan for committed secrets and vulnerable dependencies.
6. Build production artifacts.

Do not deploy unreviewed pull requests to a public production environment.

## Release checklist

- Migrations tested on a clean and upgraded database
- Demo authentication disabled in production
- Synthetic data visually labelled or removed
- Secrets excluded from repository and artifacts
- Consent/privacy/help content available
- Six charts verified against approved data
- Human-review wording verified
- Backup and rollback documented
- Version and change notes recorded

