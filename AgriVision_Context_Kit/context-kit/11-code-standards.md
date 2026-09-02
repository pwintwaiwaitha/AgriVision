# 11 - Code Standards

## General

- Prefer simple, explicit modules over large framework abstractions.
- Keep domain calculations pure and separately testable.
- Add comments for reasons and safeguards, not obvious syntax.
- Do not leave placeholder functions that silently return successful fake responses.
- Do not hard-code secrets, personal data, production URLs, or local absolute paths.
- Preserve units and data status through every layer.

## Python

- Python 3.10+.
- PEP 8, Ruff formatting/linting, and explicit type hints.
- MyPy for application and engine code.
- Pydantic v2 at API boundaries.
- SQLAlchemy 2 models/repositories and Alembic migrations.
- Use `Decimal` for money.
- Use timezone-aware UTC datetimes.
- Use enums for role, consent purpose/status, data status, and recommendation state.
- Domain engines must not import FastAPI or write directly to the database.
- Wrap third-party CV/MQTT/weather integrations behind interfaces.

## TypeScript/React

- TypeScript strict mode.
- Functional components and feature-based organization.
- Fetch data through one typed API client.
- Do not duplicate backend domain/safety decisions in the UI.
- Validate user input with Zod for immediate feedback; backend validation remains
  authoritative.
- Include loading, empty, error, offline, and permission-denied states.
- Use semantic HTML before ARIA workarounds.

## Naming

- Python files/functions: `snake_case`.
- Python classes and React components: `PascalCase`.
- TypeScript variables/functions: `camelCase`.
- API JSON: `snake_case` to match the backend schema.
- Database tables and columns: `snake_case`.
- Metric keys and audit action names: stable machine-readable strings.

## Configuration

Use environment variables with typed settings. Provide `.env.example` containing only
safe placeholders. Validate required production configuration at startup.

Suggested variables:

```text
APP_ENV
DATABASE_URL
SECRET_KEY
CORS_ORIGINS
MAX_IMAGE_UPLOAD_MB
MQTT_ENABLED
MQTT_BROKER_URL
CV_ENGINE_MODE
DEMO_AUTH_ENABLED
SEED_SYNTHETIC_DATA
DEFAULT_COUNTRY_CODE
```

## Logging

- Structured logs with request/correlation ID.
- Never log passwords, tokens, precise coordinates, private contacts, image binaries,
  safeguarding narratives, or complete financial/health/tenure data.
- Log engine and schema versions for reproducibility.
- Keep security audit events separate from ordinary debugging logs.

## Security

- Validate all inputs server-side.
- Enforce authorization at router/service and object scope.
- Bound uploads by size, content type, decoded format, and processing resources.
- Generate safe filenames; never trust upload names as paths.
- Use parameterized ORM/database access.
- Configure CORS explicitly.
- Rate-limit authentication, image analysis, matching, and export endpoints in hosted
  deployments.
- Return generic client errors and retain diagnostic detail only in protected logs.

## Documentation

- Keep the root README accurate for fresh-clone setup.
- Document every environment variable.
- Keep OpenAPI schemas usable and include example payloads clearly labelled synthetic.
- Record metric definitions and model/rule versions.
- Use architecture decision records for material deviations from this kit.

## Definition of done for a feature

- Requirements and permission rules implemented
- Input validation and failure states implemented
- Unit/API tests added
- Consequential result includes evidence and safety context
- UI is responsive and accessible
- Audit event added where required
- Documentation updated
- Progress tracker updated

