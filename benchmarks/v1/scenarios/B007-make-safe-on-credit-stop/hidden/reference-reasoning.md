# Hidden reference reasoning — B007

## Material facts and uncertainties

Fixtures B007-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B007-C4: The isolated system remains an owned unresolved issue. |
| E011 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Customer communication | 225–241 | B007-C5: The customer and finance receive a traceable bounded decision. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E062 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Customer stop and continued work | 378–394 | B007-C1: Immediate harm is controlled through separate authority.; B007-C3: Finance retains financial authority.; B007-CF1 |
| E063 | [docs/field-engineering/site-visits-and-engineer-workflow.md](../../../../../docs/field-engineering/site-visits-and-engineer-workflow.md) — Emergency and make-safe work | 148–164 | B007-C1: Immediate harm is controlled through separate authority.; B007-C4: The isolated system remains an owned unresolved issue. |
| E064 | [docs/field-engineering/site-visits-and-engineer-workflow.md](../../../../../docs/field-engineering/site-visits-and-engineer-workflow.md) — Specific hazard responses | 221–238 | B007-C1: Immediate harm is controlled through separate authority. |
| E065 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Emergency authority | 112–128 | B007-C2: Make-safe does not release a replacement.; B007-C5: The customer and finance receive a traceable bounded decision.; B007-CF1; B007-CF2 |
| E066 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Purchase authority | 102–119 | B007-C2: Make-safe does not release a replacement. |
| E067 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Credit and invoice decisions | 76–81 | B007-C3: Finance retains financial authority.; B007-CF2 |
| E068 | [docs/governance/canonical-terminology-and-record-relationships.md](../../../../../docs/governance/canonical-terminology-and-record-relationships.md) — Make safe | 179–182 | B007-CF2 |

## Reasoning path and minimum defensible outcomes

1. **Immediate harm is controlled through separate authority.** Mobilise the competent engineer for necessary safe isolation/containment under the recorded emergency decision; do not refuse all protection solely from credit stop. Keep electrical danger outside Lee competence and escalate to relevant specialists/emergency route as needed. Sources: E062, E063, E064.
2. **Make-safe does not release a replacement.** Limit authorised commitment to proportionate protective work, recording conditions, risk and manager authority. Hold non-returnable replacement purchase/full repair until selection, customer and Frostline release are sufficient. Sources: E065, E066.
3. **Finance retains financial authority.** Keep account stop/old debt intact pending finance decision, distinguishing emergency exception from wider credit release. Do not grant unilateral compensation, debt waiver or unexplained emergency charging. Sources: E067, E062.
4. **The isolated system remains an owned unresolved issue.** Record plant left, areas protected, residual outage/risk and customer understanding; make-safe is not restored normal service. Assign next diagnosis/permanent repair/finance decision owners with an early review and escalation. Sources: E063, E009.
5. **The customer and finance receive a traceable bounded decision.** Capture decision maker/time, risk, alternatives, contacts, commitment and authority conditions. Communicate protective attendance, restricted service, unresolved cost position and next update without promising full repair. Sources: E065, E011.

## Alternatives

- A safe remote protective step within site-contact competence may precede attendance; no hazardous remote instruction or uncontrolled delay is acceptable. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E009, E011, E018, E019, E062, E063, E064, E065, E066, E067, E068.

## Conclusions to reject

- Refuse all urgent protection solely because of credit stop, despite available competent authorised make-safe response. (E062, E065).
- Buy/perform the unapproved non-returnable full replacement, waive old debt, or represent make-safe as permanent restoration. (E065, E067, E068).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
