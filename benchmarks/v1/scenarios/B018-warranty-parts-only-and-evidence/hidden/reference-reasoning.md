# Hidden reference reasoning — B018

## Material facts and uncertainties

Fixtures B018-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B018-C5: Commercial uncertainty is communicated honestly. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E112 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Financial closure | 451–464 | B018-C4: Remedial job and warranty/insurance records are independent. |
| E113 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Warranty cost and recovery | 292–312 | B018-C1: Restored service does not decide responsibility.; B018-CF2 |
| E150 | [docs/warranty/warranty-responsibility-and-remedial-work.md](../../../../../docs/warranty/warranty-responsibility-and-remedial-work.md) — Core principle | 11–25 | B018-C1: Restored service does not decide responsibility. |
| E151 | [docs/warranty/warranty-responsibility-and-remedial-work.md](../../../../../docs/warranty/warranty-responsibility-and-remedial-work.md) — Warranty records | 46–62 | B018-C1: Restored service does not decide responsibility. |
| E152 | [docs/warranty/warranty-responsibility-and-remedial-work.md](../../../../../docs/warranty/warranty-responsibility-and-remedial-work.md) — Cost control | 225–243 | B018-C2: Gross exposure and expected recovery are separate. |
| E153 | [docs/manufacturers/manufacturer-relationships.md](../../../../../docs/manufacturers/manufacturer-relationships.md) — Labour and warranty recovery | 230–246 | B018-C2: Gross exposure and expected recovery are separate. |
| E154 | [docs/warehouse/warehouse-stock-and-material-control.md](../../../../../docs/warehouse/warehouse-stock-and-material-control.md) — Warranty and evidence custody | 167–186 | B018-C3: Repair completion does not permit destruction of claim evidence.; B018-CF1 |
| E155 | [docs/risk/insurance-claims-and-business-risk.md](../../../../../docs/risk/insurance-claims-and-business-risk.md) — Evidence preservation | 53–58 | B018-C3: Repair completion does not permit destruction of claim evidence.; B018-CF1 |
| E156 | [docs/manufacturers/manufacturer-relationships.md](../../../../../docs/manufacturers/manufacturer-relationships.md) — Returns and RMAs | 247–254 | B018-C3: Repair completion does not permit destruction of claim evidence. |
| E157 | [docs/warranty/warranty-responsibility-and-remedial-work.md](../../../../../docs/warranty/warranty-responsibility-and-remedial-work.md) — Closure criteria | 270–285 | B018-C4: Remedial job and warranty/insurance records are independent.; B018-CF2 |
| E158 | [docs/warranty/warranty-responsibility-and-remedial-work.md](../../../../../docs/warranty/warranty-responsibility-and-remedial-work.md) — Customer communication | 244–258 | B018-C5: Commercial uncertainty is communicated honestly. |
| E159 | [docs/manufacturers/manufacturer-relationships.md](../../../../../docs/manufacturers/manufacturer-relationships.md) — Claim authority | 197–212 | B018-CF1 |

## Reasoning path and minimum defensible outcomes

1. **Restored service does not decide responsibility.** Record tested permanent remedial job outcome while case remains inconclusive/responsibility and recovery outstanding. Preserve internal customer-care authority and do not treat no initial invoice as admission or zero cost. Sources: E150, E151, E113.
2. **Gross exposure and expected recovery are separate.** Record £2,000 gross cost and £900 conditional parts-only claim; no £900 received value yet. Describe potential net £1,100 only if £900 is realised, with other costs unrecovered and responsibility still open. Sources: E152, E153.
3. **Repair completion does not permit destruction of claim evidence.** Keep labelled compressor in evidence hold with identity, tests, location and custodian. Coordinate insurer preservation and RMA return/inspection before release or disposal; preserve five-day return risk and escalate conflict. Sources: E154, E155, E156.
4. **Remedial job and warranty/insurance records are independent.** Allow operational repair completion while recovery/responsibility/insurance actions retain linked owners. Hold final case closure until decisions, recoveries/write-offs, customer treatment and required learning actions are complete or explicitly accepted under authority. Sources: E157, E112.
5. **Commercial uncertainty is communicated honestly.** Explain verified working condition, investigation and limited manufacturer offer without promising full free cover/reimbursement. Assign claim/evidence decision owner, insurer/manufacturer actors and next update/review time. Sources: E158, E009.

## Alternatives

- Authorised agreed goodwill absorption may conclude customer treatment without rewriting technical cause; insurer/manufacturer-approved photographed inspection/return arrangements may vary if evidence needs and deadlines are met. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E009, E018, E019, E112, E113, E150, E151, E152, E153, E154, E155, E156, E157, E158, E159.

## Conclusions to reject

- Scrap/strip/return the only failed component before reconciling active insurer/claim evidence needs, or represent parts offer as full recovery received. (E154, E155, E159).
- Close all responsibility/recovery actions solely because remedial service is restored or falsely record warranty work as zero cost. (E157, E113).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
