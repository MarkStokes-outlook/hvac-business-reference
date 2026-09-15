# Hidden reference reasoning — B002

## Material facts and uncertainties

Fixtures B002-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E015 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Customer-scope decisions | 48–63 | B002-C5: The customer receives completion evidence and remaining limits.; B002-CF1 |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E020 | [docs/field-engineering/site-visits-and-engineer-workflow.md](../../../../../docs/field-engineering/site-visits-and-engineer-workflow.md) — Minor repairs | 165–170 | B002-C1: The adequately authorised repair proceeds. |
| E021 | [docs/dispatch/resource-planning-and-scheduling.md](../../../../../docs/dispatch/resource-planning-and-scheduling.md) — Readiness checks | 59–78 | B002-C1: The adequately authorised repair proceeds. |
| E022 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Financial record boundaries | 11–32 | B002-C1: The adequately authorised repair proceeds. |
| E023 | [docs/field-engineering/site-visits-and-engineer-workflow.md](../../../../../docs/field-engineering/site-visits-and-engineer-workflow.md) — Testing and recommissioning | 239–255 | B002-C2: The repair is evidenced by the supplied report.; B002-CF2 |
| E024 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Operational completion and financial closure | 146–163 | B002-C2: The repair is evidenced by the supplied report. |
| E025 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Materials and stock cost | 242–258 | B002-C3: Actual consumption remains attributable. |
| E026 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Labour recording | 234–241 | B002-C3: Actual consumption remains attributable. |
| E027 | [docs/governance/canonical-terminology-and-record-relationships.md](../../../../../docs/governance/canonical-terminology-and-record-relationships.md) — Cost | 189–192 | B002-C3: Actual consumption remains attributable. |
| E028 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Invoice triggers | 118–145 | B002-C4: An evidenced authorised invoice can be released. |
| E029 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Invoice validation and release | 329–346 | B002-C4: An evidenced authorised invoice can be released.; B002-CF2 |
| E030 | [docs/field-engineering/site-visits-and-engineer-workflow.md](../../../../../docs/field-engineering/site-visits-and-engineer-workflow.md) — Sign-off | 315–326 | B002-C5: The customer receives completion evidence and remaining limits. |
| E031 | [docs/field-engineering/site-visits-and-engineer-workflow.md](../../../../../docs/field-engineering/site-visits-and-engineer-workflow.md) — Customer handover | 300–314 | B002-C5: The customer receives completion evidence and remaining limits. |
| E032 | [docs/field-engineering/site-visits-and-engineer-workflow.md](../../../../../docs/field-engineering/site-visits-and-engineer-workflow.md) — Authority to proceed | 136–147 | B002-CF1 |

## Reasoning path and minimum defensible outcomes

1. **The adequately authorised repair proceeds.** Allocate/dispatch Mae against the accepted revision and reserved correct part; do not impose an invented approval blocker. Keep customer, site, PO, job and attendance references distinct and linked. Sources: E020, E021, E022.
2. **The repair is evidenced by the supplied report.** Record pump replacement and successful drainage/operating tests under reported conditions, not an outcome before the report. Record authorised attendance/job scope complete without treating payment as received. Sources: E023, E024.
3. **Actual consumption remains attributable.** Issue/consume one reserved pump with actual labour/travel attributed to the repair. Do not add separate time/material charges beyond the fixed £420 basis or treat cost as equal to selling price. Sources: E025, E026, E027.
4. **An evidenced authorised invoice can be released.** Raise/release £420 excluding VAT to Willow Foods Ltd using the valid PO and worksheet; defer numeric VAT only if finance rate input is needed. Link invoice trigger to tested delivery and keep invoice issued separate from paid and financially closed. Sources: E028, E029.
5. **The customer receives completion evidence and remaining limits.** Give Jo the verified outcome and finance the correct scope/evidence; do not treat Jo signature as extra authority. Reject or separately quote Jo optional remote-monitoring enhancement, preserving the approved repair outcome. Sources: E030, E031, E015.

## Alternatives

- Invoice preparation awaiting finance entry of the confirmed VAT rate is acceptable if the £420 entitlement and release evidence are complete; no arbitrary technical hold is justified. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E015, E018, E019, E020, E021, E022, E023, E024, E025, E026, E027, E028, E029, E030, E031, E032.

## Conclusions to reject

- Perform or bill the requested monitoring enhancement without new scope and expenditure authority. (E015, E032).
- Record durable completion before tests, invoice the site manager as payer, or bill £420 plus duplicate included labour/materials. (E023, E029).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
