# Hidden reference reasoning — B021

## Material facts and uncertainties

Fixtures B021-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E005 | [docs/dispatch/resource-planning-and-scheduling.md](../../../../../docs/dispatch/resource-planning-and-scheduling.md) — Engineer capability | 79–97 | B021-C3: Historical experience/course attendance does not replace qualification. |
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B021-C5: Equipment/people review outcomes have owners and records. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E058 | [docs/people/roles-skills-and-availability.md](../../../../../docs/people/roles-skills-and-availability.md) — Apprentices and supervision | 54–59 | B021-C4: Approved limited apprentice work remains usable.; B021-CF1 |
| E079 | [docs/information/records-documents-and-communication.md](../../../../../docs/information/records-documents-and-communication.md) — Corrections and history | 89–94 | B021-C5: Equipment/people review outcomes have owners and records.; B021-CF2 |
| E166 | [docs/fleet/vans-tools-and-calibration.md](../../../../../docs/fleet/vans-tools-and-calibration.md) — Out-of-calibration equipment | 136–141 | B021-C1: Failed calibration overrides apparent label.; B021-C2: Potentially invalid prior evidence is investigated.; B021-CF1; B021-CF2 |
| E167 | [docs/fleet/vans-tools-and-calibration.md](../../../../../docs/fleet/vans-tools-and-calibration.md) — Calibration | 120–135 | B021-C1: Failed calibration overrides apparent label. |
| E168 | [docs/fleet/vans-tools-and-calibration.md](../../../../../docs/fleet/vans-tools-and-calibration.md) — Gas analysers and specialist instruments | 142–147 | B021-C1: Failed calibration overrides apparent label. |
| E169 | [docs/compliance/safety-quality-and-environment.md](../../../../../docs/compliance/safety-quality-and-environment.md) — Quality control | 66–73 | B021-C2: Potentially invalid prior evidence is investigated. |
| E170 | [docs/people/training-competence-and-career-development.md](../../../../../docs/people/training-competence-and-career-development.md) — Expiring qualifications | 59–64 | B021-C3: Historical experience/course attendance does not replace qualification.; B021-CF1 |
| E171 | [docs/people/training-competence-and-career-development.md](../../../../../docs/people/training-competence-and-career-development.md) — Competence records | 43–58 | B021-C3: Historical experience/course attendance does not replace qualification. |
| E172 | [docs/people/training-competence-and-career-development.md](../../../../../docs/people/training-competence-and-career-development.md) — Authorisation and restriction | 129–134 | B021-C4: Approved limited apprentice work remains usable. |
| E173 | [docs/compliance/safety-quality-and-environment.md](../../../../../docs/compliance/safety-quality-and-environment.md) — Incident and near-miss management | 58–65 | B021-C5: Equipment/people review outcomes have owners and records. |

## Reasoning path and minimum defensible outcomes

1. **Failed calibration overrides apparent label.** Remove/quarantine I-21 from measurement use pending adjustment/repair/replacement and evidence. Use verified G-21 with pre-use condition checks for task requiring valid measurement; no invented calibration interval. Sources: E166, E167, E168.
2. **Potentially invalid prior evidence is investigated.** Link I-21 to A/B reports, lab error and test conditions; assign competent impact review. Determine whether retest/customer safety/notifications are needed from error size and safety significance, without declaring all old tests valid or invalid unexamined. Sources: E166, E169.
3. **Historical experience/course attendance does not replace qualification.** Do not assign Eli required combustion work on expired qualification or planned course attendance. Allocate Gia current qualified/authorised task rather than unnecessarily blocking all safe work. Sources: E170, E171, E005.
4. **Approved limited apprentice work remains usable.** Allow Fen filter maintenance only within defined remote-supervision authorisation and suitable arrangement. Do not promote Fen to combustion task or demand direct supervision for every task where approved remote supervision is sufficient. Sources: E058, E172.
5. **Equipment/people review outcomes have owners and records.** Assign I-21 repair/retest, A/B impact review and Eli renewal verification owners/review triggers. Preserve original measurements and corrections, communicate material consequences through appropriate manager/compliance route. Sources: E009, E079, E173.

## Alternatives

- Approved competent alternative resource/equipment can substitute for Gia/G-21; historical review may conclude no retest necessary if evidenced impact is immaterial. Fen authorised remote-supervised filter work can proceed. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E005, E009, E018, E019, E058, E079, E166, E167, E168, E169, E170, E171, E172, E173.

## Conclusions to reject

- Use I-21 for material certification despite unacceptable error or allocate required combustion work to Eli/Fen without current competence/qualification. (E166, E170, E058).
- Erase/replace historical readings or declare affected prior safety evidence sound solely from in-date label. (E166, E079).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
