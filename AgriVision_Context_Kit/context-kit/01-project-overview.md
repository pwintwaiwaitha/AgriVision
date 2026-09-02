# 01 - Project Overview

## Product name

**AgriVision**

## Product vision

AgriVision is a web-based, ASEAN-wide farmer-continuity and agricultural-transition
platform. It helps current farmers reduce avoidable workload and uncertainty, helps
interested youth explore realistic agricultural pathways, and connects willing
experienced farmers with learners through consent-based mentorship.

## Core principle

> Do not replace farmers with technology. Use technology to support today's farmers
> and help the next generation enter agriculture responsibly.

## Sustainable Development Goal

Primary alignment: **SDG 2 - Zero Hunger**.

The prototype contributes through continuity, learning, resource efficiency, and
responsible transition. It must not claim that software usage alone proves improved
food security.

## Problem statement

ASEAN farming communities face a combined continuity problem:

- Many experienced farmers carry physically demanding workloads.
- Farm decisions are affected by weather, water, pests, costs, and incomplete data.
- Interested youth may lack land access, training, mentors, capital, or realistic
  information about agricultural careers.
- Valuable local knowledge can be lost when transfer is informal or unsupported.
- Regional comparisons are often misleading because countries use different years,
  definitions, denominators, and levels of data coverage.

AgriVision addresses these problems without assuming that every older farmer wants
to retire, every youth wants to farm, or every family has a successor.

## Three connected solution tracks

| Track | Goal | Main functions |
|---|---|---|
| Sustain | Help current farmers continue safely and productively | IoT monitoring, irrigation decision support, workload tracking, crop-image screening, alerts, action verification |
| Attract | Help interested youth explore agriculture realistically | Interest profile, pathway discovery, training and institution referrals, digital-twin scenarios, staged learning plan |
| Bridge | Support voluntary intergenerational continuity | Mentor and learner profiles, explainable matching, mutual consent, structured mentorship, knowledge-transfer controls, safeguarding |

## Target users

- Current farmers and experienced farmers
- Youth explorers and prospective apprentices
- Mentors
- Extension workers and cooperative facilitators
- Programme managers and institutions
- Researchers using approved, de-identified data
- System administrators

## Product promises

AgriVision will:

- Explain the reason behind important recommendations.
- Show data source, status, date, geography, unit, and limitations.
- Offer a low-bandwidth or assisted path when possible.
- Let users correct their information.
- Require human review for high-consequence actions.
- Protect private contact, location, financial, health, and tenure information.
- Keep simulated, synthetic, estimated, and observed values clearly separated.

## Non-goals

The MVP is not:

- A replacement for agronomists, veterinarians, extension workers, legal advisers,
  financial advisers, or local authorities.
- An autonomous controller for real pumps, machinery, or pesticide application.
- A guarantee of yield, profit, land, employment, financing, or successful matching.
- A complete ranking of ASEAN countries by succession risk.
- Proof that a programme has produced long-term food-security impact.

## MVP success criteria

The MVP is successful when it demonstrates:

1. One complete Sustain workflow with an offline-assisted alternative.
2. One complete Attract workflow with three labelled scenarios.
3. One complete Bridge workflow with mutual consent and safe contact release.
4. Switching between at least two country/language/connectivity profiles.
5. Clear separation of observed, user-provided, estimated, scenario, synthetic, and
   missing data.
6. Six data charts using approved data without fabricated values.
7. Automated tests for core algorithms, API validation, permissions, consent,
   safety flags, and data-status rules.

