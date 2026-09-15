# Hidden reference reasoning — B015

## Material facts and uncertainties

Fixtures B015-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E060 | [docs/dispatch/resource-planning-and-scheduling.md](../../../../../docs/dispatch/resource-planning-and-scheduling.md) — Dynamic rescheduling | 180–196 | B015-C3: Failed supply changes the dependent mobilisation. |
| E095 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Materials and equipment | 158–175 | B015-C3: Failed supply changes the dependent mobilisation. |
| E113 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Warranty cost and recovery | 292–312 | B015-CF2 |
| E128 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Open purchasing exceptions | 307–320 | B015-C5: The unresolved financial and operational actions remain visible. |
| E129 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Direct deliveries | 191–205 | B015-C1: Delivery signature does not create usable stock. |
| E130 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Receipt and technical acceptance | 206–222 | B015-C1: Delivery signature does not create usable stock.; B015-CF1 |
| E131 | [docs/warehouse/warehouse-stock-and-material-control.md](../../../../../docs/warehouse/warehouse-stock-and-material-control.md) — Receipt exceptions | 73–86 | B015-C1: Delivery signature does not create usable stock.; B015-C2: Supplier exception protects replacement/credit rights.; B015-CF1 |
| E132 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Supplier errors and returns | 223–238 | B015-C2: Supplier exception protects replacement/credit rights. |
| E133 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Invoice matching | 269–282 | B015-C4: Disputed and undisputed amounts are differentiated.; B015-CF2 |
| E134 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Supplier invoices | 259–276 | B015-C4: Disputed and undisputed amounts are differentiated.; B015-CF2 |
| E135 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Accruals and uninvoiced cost | 277–291 | B015-C5: The unresolved financial and operational actions remain visible. |

## Reasoning path and minimum defensible outcomes

1. **Delivery signature does not create usable stock.** Record two physical packages/one accepted unit and wrong-damaged quarantine with provenance. Exclude wrong/damaged unit from available stock and two-unit readiness. Sources: E129, E130, E131.
2. **Supplier exception protects replacement/credit rights.** Preserve packaging/photos, exact wrong-model/condition, original PO and receipt evidence. Assign procurement return authority/replacement/credit chase before five-working-day deadline. Sources: E132, E131.
3. **Failed supply changes the dependent mobilisation.** Notify project owner that tomorrow two-unit installation is not ready and decide reschedule/safe independent stage under authority. Record affected labour/customer commitment, replacement date confidence and next review. Sources: E095, E060.
4. **Disputed and undisputed amounts are differentiated.** Identify £2,000 correct unit and £100 agreed freight as evidenced potentially undisputed amounts, subject to confirmed delivery terms; wrong unit £2,000 and premium £150 remain disputed. Do not pay full invoice from carrier signature or automatically withhold valid undisputed amount just to hide unmatched lines. Sources: E133, E134.
5. **The unresolved financial and operational actions remain visible.** Retain £2,150 disputed amount, expected credit/replacement and separate accepted cost allocation without treating credit as received. Give finance/project/customer proportionate update with owner, due/review and invoice-payment decision route. Sources: E135, E128.

## Alternatives

- If contract terms condition all freight on full correct delivery, mark £100 under reviewed uncertainty rather than force payment; fixture establishes agreed freight value but not that condition. A reviewed safe independent stage is acceptable. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E018, E019, E060, E095, E113, E128, E129, E130, E131, E132, E133, E134, E135.

## Conclusions to reject

- Install or count the wrong/damaged unit as available, or certify two-unit readiness from signed packages. (E130, E131).
- Release full supplier invoice/extra freight solely from proof of delivery, or mark unreceived credit as cash recovery. (E133, E134, E113).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
