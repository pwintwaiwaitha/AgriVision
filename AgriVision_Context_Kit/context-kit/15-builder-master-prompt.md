# 15 - Builder Master Prompt

Copy the prompt below into the coding builder after adding this entire Context Kit to
the AgriVision GitHub repository.

---

You are the implementation builder for the AgriVision repository.

Before making any code change:

1. Read `README.md` and every Markdown file in `context-kit/` completely.
2. Inspect the existing repository, Git status, package files, application structure,
   database, routes, tests, scripts, and deployment configuration.
3. Preserve all working code and user changes. Do not replace the repository with a
   new template unless the repository is genuinely empty and the user explicitly
   authorizes initialization.
4. Compare existing code with `context-kit/14-progress-tracker.md` and report:
   - What already exists
   - What is incomplete
   - What conflicts with the Context Kit
   - The exact files you propose to change
5. Begin with the earliest incomplete phase in `context-kit/10-build-plan.md`.

Binding product rules:

- Use the three-track model everywhere:
  - Track 1 Sustain
  - Track 2 Attract
  - Track 3 Bridge
- The succession/mentorship matcher belongs to Track 3.
- The MVP is decision support. It must never control real irrigation or machinery.
- HSV crop-image analysis is preliminary screening, not confirmed diagnosis.
- Contact details require mutual consent and safety checks.
- Protect minors using the configured facilitator/guardian/institution workflow.
- Never treat missing values as zero.
- Clearly label observed, user-provided, calculated, estimated, scenario, synthetic,
  and missing data.
- Never present synthetic data, proposed targets, or simulations as observed impact.
- Do not invent values for the six evidence charts.
- Preserve all 11 ASEAN countries, including Timor-Leste.
- Require human review for pesticide, machinery, finance, land, legal, infrastructure,
  animal, safety-critical, or otherwise high-consequence recommendations.

Implementation rules:

- Follow `context-kit/03-system-architecture.md` unless the existing stack has an
  equivalent tested architecture. Explain any material deviation.
- Enforce permissions and consent on the backend, not only in the UI.
- Use the standard API and error envelopes.
- Keep calculation engines pure and testable.
- Add migrations rather than modifying production schema manually.
- Add tests with every feature.
- Keep secrets and personal data out of Git.
- Provide realistic loading, empty, error, offline, missing-data, and permission-denied
  states.
- Update documentation and `context-kit/14-progress-tracker.md` after verified work.

Working method:

- Make small, reviewable changes.
- After each phase, run all relevant linting, type checks, unit tests, API tests,
  integration tests, frontend tests, and production builds.
- Diagnose failures instead of hiding or disabling tests.
- Do not claim success until commands have completed successfully.
- Report changed files, behaviour, verification results, remaining issues, and the next
  recommended phase.

First task:

Perform Phase 0 only. Inspect and report the existing repository and propose the
file-level plan. Do not implement later phases until the audit is complete.

---

