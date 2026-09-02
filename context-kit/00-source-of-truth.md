# 00 - Source of Truth and Conflict Resolution

## Precedence

When requirements disagree, use this order:

1. Safety, consent, privacy, evidence honesty, and human-review rules in this kit.
2. The three-track product model in this kit.
3. Existing repository behaviour that is already tested and does not conflict with
   items 1 or 2.
4. Technical module suggestions from the implementation PDF.

Do not silently choose between conflicting requirements. Record material decisions
in `14-progress-tracker.md`.

## Resolved differences between the source PDFs

### Three tracks, not two

The system PDF requires Sustain, Attract, and Bridge. The implementation PDF
mentions only Sustain and Attract and places succession matching under Attract.
This kit corrects that mismatch:

- Track 1 Sustain owns IoT automation, workload reduction, alerts, and crop-screening.
- Track 2 Attract owns youth discovery, training pathways, and the digital twin.
- Track 3 Bridge owns mentor/successor matching, mutual consent, mentorship plans,
  knowledge transfer, safeguarding, and exit options.

### The prototype is decision support, not autonomous farm control

The moisture threshold and water-volume calculation are classroom prototype logic.
The UI and API must indicate `DEMO`, `SIMULATED`, or `REVIEW_REQUIRED` until farm
area, crop, soil, weather, equipment limits, and local professional approval are
available. A real pump must never be activated from this MVP.

### Crop-image output is preliminary screening

HSV lesion measurement is a mock visual-screening method, not a reliable disease
diagnosis. The system may say `possible leaf stress`, `possible lesion`, or
`review recommended`; it must not claim laboratory-level certainty. Treatment
advice must be framed as an option for local expert review.

### Matching is consent-based and belongs to Bridge

The matching score produces suggestions, not assignments. Do not expose contact
details until both parties consent. Users under the local age of majority cannot
enter unsupervised direct-contact matching.

### Synthetic and scenario data are not observed results

Seed data must include `data_status: synthetic` and must be visibly labelled in the
UI and exports. Scenario projections must never be reported as achieved impact.

### ASEAN scope

Regional views must include the 11 current ASEAN Member States in this project:
Brunei Darussalam, Cambodia, Indonesia, Lao PDR, Malaysia, Myanmar, Philippines,
Singapore, Thailand, Timor-Leste, and Viet Nam. Country-specific functionality must
adapt to language, crops, institutions, connectivity, and verified local context.

### Chart integrity

The six analytics charts are specifications, not permission to invent numbers.
Use only the project's approved datasets. Missing values remain missing, never zero.

## Known source-document limitation

The code block in `AgriVision_System_Prompt.pdf` is clipped at the right edge on
many pages. This kit preserves the visible requirements and resolves them into
implementable rules; it does not pretend that clipped wording was fully recoverable.

