# Hidden reference reasoning — B027

## Material facts and uncertainties

Fixtures B027-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E004 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Attendance authority | 135–150 | B027-C3: Diagnostic authority is not unlimited motor spend. |
| E008 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Customer authority and purchase orders | 72–100 | B027-C3: Diagnostic authority is not unlimited motor spend. |
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B027-C5: Outage, dispute and breach recovery remain controlled. |
| E011 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Customer communication | 225–241 | B027-C5: Outage, dispute and breach recovery remain controlled. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E026 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Labour recording | 234–241 | B027-C4: Credits, billing and debt retain distinct approvals. |
| E039 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Service credits | 282–289 | B027-C1: Premium attendance does not amend the agreed target.; B027-C5: Outage, dispute and breach recovery remain controlled.; B027-CF2 |
| E049 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Coverage hours | 84–97 | B027-C1: Premium attendance does not amend the agreed target. |
| E050 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Attendance targets | 130–145 | B027-C1: Premium attendance does not amend the agreed target. |
| E051 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Clock stops | 161–181 | B027-CF2 |
| E067 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Credit and invoice decisions | 76–81 | B027-C4: Credits, billing and debt retain distinct approvals.; B027-CF2 |
| E079 | [docs/information/records-documents-and-communication.md](../../../../../docs/information/records-documents-and-communication.md) — Corrections and history | 89–94 | B027-CF1 |
| E100 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Delegated limits | 94–111 | B027-C3: Diagnostic authority is not unlimited motor spend.; B027-CF1 |
| E162 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Disputes | 395–415 | B027-C2: Contemporaneous instruction and later dispute are both preserved. |
| E163 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Credits, write-offs and goodwill | 313–328 | B027-C4: Credits, billing and debt retain distinct approvals. |
| E216 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Verbal instructions | 129–134 | B027-C2: Contemporaneous instruction and later dispute are both preserved.; B027-CF1 |
| E217 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Conflicts and escalation | 135–147 | B027-C2: Contemporaneous instruction and later dispute are both preserved. |

## Reasoning path and minimum defensible outcomes

1. **Premium attendance does not amend the agreed target.** Calculate deadline Sunday 00:00, actual attendance 00:30 and 30-minute breach with no retrospective stop. Identify £100 contractual credit eligibility subject to supplied approval condition; premium diagnostic rate does not remove credit under these terms. Sources: E049, E050, E039.
2. **Contemporaneous instruction and later dispute are both preserved.** Retain Ana 20:10 diagnosis/minor-repair total £600 instruction and separate internal limit without rewriting history from later denial. Seek written confirmation/escalate disputed scope and finance evidence sufficiency with source/time and uncertainty visible. Sources: E216, E217, E162.
3. **Diagnostic authority is not unlimited motor spend.** Recognise proposed £300+£500 = £800 exceeds original total £600 cap even if contemporaneous instruction is accepted. Hold/quote motor separately until current valid customer and internal authority, safe readiness and approved price are adequate. Sources: E004, E008, E100.
4. **Credits, billing and debt retain distinct approvals.** Route £300 diagnosis charging and £100 service credit through finance/evidence/approval decisions; no invented automatic netting or motor invoice. Do not erase unrelated old debt or move actual labour/cost merely to achieve apparent credit/margin outcome. Sources: E163, E026, E067.
5. **Outage, dispute and breach recovery remain controlled.** Record safely isolated asset, unresolved motor repair and named customer-approval/dispute/finance next action with due review/escalation. Give customer verified late attendance, potential contractual credit, disputed instruction and permanent repair next steps without declaring liability resolved. Sources: E011, E009, E039.

## Alternatives

- The £300 diagnostic charge may be held pending finance dispute review without abandoning contractual credit assessment; approved credit may later net against this invoice under finance direction, but cannot be assumed or erase other debt. A £200 potential net diagnosis invoice is conditional on entitlement/evidence and both approvals, not already released. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E004, E008, E009, E011, E018, E019, E026, E039, E049, E050, E051, E067, E079, E100, E162, E163, E216, E217.

## Conclusions to reject

- Remove or invent verbal authority evidence after denial, commit to the £500 motor under a £600 total cap, or claim unapproved motor work was delivered. (E216, E100, E079).
- Deny stated service credit solely from premium attendance, invent a clock stop to erase breach or waive unrelated debt without finance authority. (E039, E051, E067).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
