# 05 - UI and UX Rules

## Experience principles

The interface should feel like a trustworthy agricultural operations platform, not
a generic chatbot or an AI illustration. Use real product components, readable data,
clear status labels, and realistic empty/error states.

Priorities:

1. Clarity for frontline users
2. Large, safe actions
3. Visible data status and uncertainty
4. Low-bandwidth resilience
5. Role-appropriate information
6. Respectful intergenerational language

## Recommended visual system

- Primary forest green: `#14532D`
- Action green: `#16A34A`
- Light field background: `#F3F7F1`
- Warm harvest accent: `#EAB308`
- Information blue: `#2563EB`
- Warning amber: `#D97706`
- Danger red: `#B91C1C`
- Main text: `#17221B`
- Muted text: `#5B665E`
- White surfaces with restrained shadows and 12-16 px corner radius

Do not use green alone to convey status. Pair colour with an icon and label.

## Accessibility

- Meet WCAG 2.2 AA contrast.
- Minimum body text: 16 px; farmer-mode body text: 18 px where space permits.
- Minimum interactive target: 44 x 44 px.
- Provide keyboard focus, labels, error summaries, and screen-reader descriptions.
- Charts need accessible summaries and a data-table view.
- Support text enlargement without clipped cards.
- Avoid long paragraphs on task screens.
- Use plain language and preserve units.

## Navigation

Desktop navigation:

- Overview
- Sustain
- Attract
- Bridge
- Analytics
- Records
- Help
- Profile and active role

Mobile navigation should expose no more than five primary destinations. Put secondary
items in a labelled menu.

## Required pages

### Shared

- Landing and project disclaimer
- Role selection/onboarding
- Country, language and connectivity setup
- Notifications and action centre
- Records/history
- Help, privacy and consent centre

### Sustain

- Farmer dashboard
- Add sensor/manual observation
- Irrigation support result
- Crop-image screening
- Workload and actions history
- Follow-up/outcome recording

### Attract

- Youth exploration profile
- Pathway discovery
- Digital-twin input
- Three-scenario comparison
- Training and institution referrals
- Learning progress

### Bridge

- Mentor/learner profile
- Match suggestions with score explanation
- Invitation and mutual-consent flow
- Mentorship plan
- Check-in, pause, end, and report-safety controls

### Institution/admin

- Programme overview
- Data-quality dashboard
- Activity/output/outcome/impact dashboard
- Safeguarding queue with restricted access
- SAC export and export history
- Configuration and audit views

## Standard result card

Every consequential result card must show:

- Result or recommendation
- Status: observed, user-provided, calculated, scenario, synthetic, or missing
- Confidence with a short reason
- Inputs and assumptions
- Risks and safeguards
- Human review requirement
- One safe next action
- Correct-input and report-problem actions
- Rule/model version and generated time in expandable details

## Status language

Use:

- `Preliminary screening`
- `Illustrative calculation`
- `Human review required`
- `Synthetic demonstration data`
- `Source data missing`
- `Waiting for consent`
- `Mutually accepted`

Avoid:

- `AI confirmed`
- `Guaranteed yield`
- `Safe to apply`
- `Perfect match`
- `Highest-risk country` without valid evidence
- `Impact achieved` for a scenario or target

## Offline and low-bandwidth behaviour

- Display connectivity status.
- Cache essential reference content and current drafts.
- Queue safe form submissions with timestamp and visible sync state.
- Never queue contact release, role changes, safeguarding closure, or real-world
  control actions without an online server confirmation.
- Compress optional images and let users submit observations without images.
- Provide printable or facilitator-assisted summaries.

## Chart rules

- Never animate bars in a way that obscures exact values.
- Preserve missing values as gaps marked `Data unavailable`.
- Show geography, unit, period, source, coverage, and status beside every chart.
- Do not calculate a combined score unless its definition is documented.
- Provide `What this chart shows` and `What this chart cannot prove` captions.

## Responsive acceptance criteria

- No horizontal scrolling at 360 px viewport width except data tables with a clearly
  labelled scroll container.
- Primary task is usable with one hand on a phone.
- Dashboard cards reflow without truncating units or status badges.
- File upload supports camera capture and regular file selection.

