# 07 - Database Schema

## Database targets

- MVP: SQLite with foreign keys enabled.
- Production: PostgreSQL with PostGIS.
- Use SQLAlchemy models and Alembic migrations for both.
- Do not store secrets in the database seed or repository.

## Common fields

Most mutable entities include:

- `id` UUID
- `created_at` UTC timestamp
- `updated_at` UTC timestamp
- `created_by` nullable UUID where relevant
- `record_status` active, archived, or deleted where soft deletion is required

Metrics and recommendations additionally include provenance, version, and data status.

## Identity and access

### `users`

`id`, `display_name`, `preferred_language`, `country_code`, `account_status`,
`age_band`, `is_minor`, timestamps.

Keep email/phone in a separate protected identity/contact table if the authentication
system does not own them.

### `user_roles`

`user_id`, `role`, `scope_type`, `scope_id`, `granted_at`, `revoked_at`.

### `consents`

`user_id`, `purpose`, `policy_version`, `status`, `granted_at`, `withdrawn_at`,
`evidence_method`, `facilitator_id`, `guardian_or_institution_ref` where required.

## Adaptation and programme context

### `countries`

`code`, `name`, `enabled`, `default_language`, `age_of_majority_config`,
`connectivity_modes`, `configuration_version`.

### `locations`

`id`, `country_code`, `subnational_name`, `coarse_geography`, protected geometry.

### `adaptation_profiles`

`user_id`, `location_id`, `language`, `literacy_support`, `accessibility_needs`,
`connectivity`, `delivery_mode`, `livelihood_context`, `institution_context`,
`verified_context_at`.

### `institutions`

`id`, `country_code`, `name`, `type`, `service_area`, `verified_at`, `source_id`,
`public_contact`, `active`.

## Track 1 - Sustain

### `farm_profiles`

`id`, `owner_user_id`, `location_id`, `display_name`, `area_ha`, `area_status`,
`tenure_status_optional`, `connectivity`, `goals`, `constraints`.

### `crop_livelihoods`

`id`, `farm_id`, `category`, `name`, `season`, `area_ha`, `data_status`.

### `sensor_devices`

`id`, `farm_id`, `device_type`, `external_ref`, `unit_config`, `last_seen_at`,
`status`. Store device credentials outside ordinary database columns.

### `observations`

`id`, `farm_id`, `observed_at`, `observation_type`, `value`, `unit`, `source_type`,
`source_id`, `data_status`, `quality_status`, `raw_payload_ref`.

### `support_requests`

`id`, `farm_id`, `goal`, `constraint_text`, `urgency`, `status`.

### `recommendations`

`id`, `user_id`, `farm_id`, `track`, `recommendation_type`, `plain_action`,
`why`, `assumptions_json`, `risks_json`, `safeguards_json`, `confidence`,
`confidence_reason`, `human_review_required`, `human_review_reason`,
`next_safe_action`, `engine_version`, `data_status`.

### `farmer_actions`

`id`, `recommendation_id`, `action_taken`, `confirmed_by`, `confirmed_at`,
`automated_cycle_confirmed`.

### `crop_screenings`

`id`, `farm_id`, `image_object_ref`, `lesion_ratio`, `screening_label`,
`confidence`, `limitations_json`, `review_status`, `engine_version`.

## Track 2 - Attract

### `exploration_profiles`

`user_id`, `interests_json`, `skills_json`, `time_available`, `land_access_path`,
`capital_constraint`, `accessibility_needs`, `consent_id`.

### `pathways`

`id`, `country_code`, `name`, `category`, `skills_json`, `time_requirements`,
`cost_range`, `risks_json`, `verified_source_id`, `active`.

### `scenarios`

`id`, `user_id`, `input_json`, `assumption_version`, `currency`, `data_status`,
`created_at`.

### `scenario_results`

`scenario_id`, `scenario_type`, `year`, `yield_kg`, `revenue`, `operating_cost`,
`net_profit`, `roi_pct`, `labour_hours`, `calculation_json`.

## Track 3 - Bridge

### `mentor_profiles` and `learner_profiles`

Store disclosed crops/livelihoods, skills/interests, approximate geography,
language, availability, scale preference, facilitator preference, visibility, and
matching-consent ID. Do not store contact details here.

### `mentorship_matches`

`id`, `mentor_user_id`, `learner_user_id`, `geo_score`, `crop_score`, `scale_score`,
`total_score`, `explanation_json`, `status`, `matcher_version`, `minor_review_status`.

### `match_responses`

`match_id`, `party_user_id`, `response`, `responded_at`, `consent_id`.

### `contact_release_events`

`match_id`, `released_at`, `authorized_by`, `consent_checks_json`,
`safeguarding_check`, `revoked_at`.

### `learning_plans`

`match_id`, `goals_json`, `cadence`, `tasks_json`, `boundaries_json`, `review_at`,
`escalation_contact_ref`, `status`.

### `safeguarding_events`

Restricted table: `reporter_id`, `match_id`, `category`, `description_protected`,
`severity`, `status`, `assigned_reviewer_id`, `resolution_protected`, timestamps.

## Evidence, measurement, and audit

### `sources`

`id`, `title`, `publisher`, `url`, `reference_period`, `retrieved_at`, `license`,
`limitations`.

### `metrics`

`id`, `metric_key`, `definition`, `value`, `unit`, `geography`, `reference_period`,
`source_id`, `coverage`, `denominator`, `data_status`, `last_updated`, `limitations`.

Allowed data status values:

- observed
- user_provided
- calculated
- estimated
- scenario
- synthetic
- missing

### `outcome_records`

`id`, `user_id`, `farm_id`, `match_id`, `outcome_type`, `value`, `unit`,
`reference_period`, `confirmation_method`, `data_status`, `source_id`.

### `audit_events`

Append-only: `id`, `actor_user_id`, `active_role`, `action`, `object_type`,
`object_id`, `request_id`, `data_used_json`, `rule_or_model_version`, `result_code`,
`created_at`.

## Relationship rules

- A recommendation is never itself an outcome.
- A scenario result never becomes an observed metric through copying.
- A match requires two separate responses.
- Contact release requires current matching/contact consent from both parties.
- Withdrawing contact consent prevents future access but does not erase the minimum
  audit record required for safety and accountability.
- Image binary data should use protected object storage; database rows store only
  controlled references and metadata.

