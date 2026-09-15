# Hidden reference reasoning — B022

## Material facts and uncertainties

Fixtures B022-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B022-C5: The complaint remains open until its controlled outcome. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E064 | [docs/field-engineering/site-visits-and-engineer-workflow.md](../../../../../docs/field-engineering/site-visits-and-engineer-workflow.md) — Specific hazard responses | 221–238 | B022-C2: Ongoing property/electrical risk is protected. |
| E155 | [docs/risk/insurance-claims-and-business-risk.md](../../../../../docs/risk/insurance-claims-and-business-risk.md) — Evidence preservation | 53–58 | B022-C3: Investigation and notification run under their own controls.; B022-CF2 |
| E162 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Disputes | 395–415 | B022-C4: Goodwill, liability and debt are separate. |
| E163 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Credits, write-offs and goodwill | 313–328 | B022-C4: Goodwill, liability and debt are separate.; B022-CF2 |
| E174 | [docs/customer-service/complaints-escalations-and-service-recovery.md](../../../../../docs/customer-service/complaints-escalations-and-service-recovery.md) — What counts as a complaint | 9–25 | B022-C1: The expressed dissatisfaction becomes an owned complaint. |
| E175 | [docs/customer-service/complaints-escalations-and-service-recovery.md](../../../../../docs/customer-service/complaints-escalations-and-service-recovery.md) — Complaint ownership | 41–46 | B022-C1: The expressed dissatisfaction becomes an owned complaint. |
| E176 | [docs/customer-service/complaints-escalations-and-service-recovery.md](../../../../../docs/customer-service/complaints-escalations-and-service-recovery.md) — Initial response | 26–40 | B022-C1: The expressed dissatisfaction becomes an owned complaint. |
| E177 | [docs/risk/insurance-claims-and-business-risk.md](../../../../../docs/risk/insurance-claims-and-business-risk.md) — Incident response | 39–52 | B022-C2: Ongoing property/electrical risk is protected.; B022-CF1 |
| E178 | [docs/customer-service/complaints-escalations-and-service-recovery.md](../../../../../docs/customer-service/complaints-escalations-and-service-recovery.md) — Service recovery | 80–96 | B022-C2: Ongoing property/electrical risk is protected. |
| E179 | [docs/customer-service/complaints-escalations-and-service-recovery.md](../../../../../docs/customer-service/complaints-escalations-and-service-recovery.md) — Severity and escalation | 64–79 | B022-C3: Investigation and notification run under their own controls.; B022-CF1 |
| E180 | [docs/risk/insurance-claims-and-business-risk.md](../../../../../docs/risk/insurance-claims-and-business-risk.md) — Claims handling | 59–64 | B022-C3: Investigation and notification run under their own controls. |
| E181 | [docs/customer-service/complaints-escalations-and-service-recovery.md](../../../../../docs/customer-service/complaints-escalations-and-service-recovery.md) — Liability and goodwill | 97–102 | B022-C4: Goodwill, liability and debt are separate.; B022-CF2 |
| E182 | [docs/risk/insurance-claims-and-business-risk.md](../../../../../docs/risk/insurance-claims-and-business-risk.md) — Insurance arrangements | 27–32 | B022-C4: Goodwill, liability and debt are separate. |
| E183 | [docs/customer-service/complaints-escalations-and-service-recovery.md](../../../../../docs/customer-service/complaints-escalations-and-service-recovery.md) — Closure | 115–127 | B022-C5: The complaint remains open until its controlled outcome.; B022-CF1 |
| E184 | [docs/customer-service/complaints-escalations-and-service-recovery.md](../../../../../docs/customer-service/complaints-escalations-and-service-recovery.md) — Learning and prevention | 128–132 | B022-C5: The complaint remains open until its controlled outcome. |

## Reasoning path and minimum defensible outcomes

1. **The expressed dissatisfaction becomes an owned complaint.** Capture complaint despite no formal word/channel and name a severity-appropriate manager communication owner. Acknowledge promptly with evidence/investigation steps and realistic update rather than reflexive admission or denial. Sources: E174, E175, E176.
2. **Ongoing property/electrical risk is protected.** Arrange available competent authorised containment/isolation and relevant electrical escalation. Preserve safe-state/residual risk and follow-on action; small goodwill or attendance is not safety closure. Sources: E177, E178, E064.
3. **Investigation and notification run under their own controls.** Preserve photos/removed components/chronology, record cause alternatives and coordinate insurance/warranty evidence custody. Notify management/broker promptly via authorised route; seek applicable regulatory/contract duties without inventing law or waiting for final blame. Sources: E155, E179, E180.
4. **Goodwill, liability and debt are separate.** Do not approve £5,000 settlement/full-and-final terms or £100 credit without delegated review, and do not promise insurer cover. Keep £400 undisputed invoice value visible/collectible and £300 disputed with evidence/owner; do not erase all debt. Sources: E181, E162, E163, E182.
5. **The complaint remains open until its controlled outcome.** Record corrective/safety, commercial, communication and customer-response dependencies with owners/review dates. Do not close just because attendance/apology/credit is offered; retain learning action for repeat leak/missed updates. Sources: E183, E184, E009.

## Alternatives

- Apology, independent inspection, authorised goodwill or firm evidence-backed liability outcome may differ; safety, notification, evidence and approval controls remain required. Domain complaint closure is used; reporting wording conflict is recorded in gaps. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E009, E018, E019, E064, E155, E162, E163, E174, E175, E176, E177, E178, E179, E180, E181, E182, E183, E184.

## Conclusions to reject

- Close complaint while known water/electrical risk remains uncontrolled, or defer required prompt broker notification solely until final investigation. (E183, E177, E179).
- Promise compensation/full-and-final settlement or erase debt without delegated approval; destroy available active claim evidence. (E181, E163, E155).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
