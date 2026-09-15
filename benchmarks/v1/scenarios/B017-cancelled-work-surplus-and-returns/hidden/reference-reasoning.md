# Hidden reference reasoning — B017

## Material facts and uncertainties

Fixtures B017-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B017-C5: Closure waits for or transfers controlled residual decisions. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E025 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Materials and stock cost | 242–258 | B017-C2: Reusable and suspect materials follow different states.; B017-CF1 |
| E028 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Invoice triggers | 118–145 | B017-CF2 |
| E079 | [docs/information/records-documents-and-communication.md](../../../../../docs/information/records-documents-and-communication.md) — Corrections and history | 89–94 | B017-CF1 |
| E112 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Financial closure | 451–464 | B017-C5: Closure waits for or transfers controlled residual decisions. |
| E132 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Supplier errors and returns | 223–238 | B017-C4: Approved return progresses before its deadline. |
| E134 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Supplier invoices | 259–276 | B017-C4: Approved return progresses before its deadline. |
| E144 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — Cancellation and abandonment | 201–206 | B017-C1: Operational cancellation preserves remaining obligations. |
| E145 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Cancellation and surplus commitments | 255–268 | B017-C1: Operational cancellation preserves remaining obligations.; B017-C3: Custom purchase remains a real company commitment. |
| E146 | [docs/warehouse/warehouse-stock-and-material-control.md](../../../../../docs/warehouse/warehouse-stock-and-material-control.md) — Returns from engineers and sites | 147–166 | B017-C2: Reusable and suspect materials follow different states.; B017-CF1 |
| E147 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Credit approval and exposure | 54–71 | B017-C3: Custom purchase remains a real company commitment. |
| E148 | [docs/warehouse/warehouse-stock-and-material-control.md](../../../../../docs/warehouse/warehouse-stock-and-material-control.md) — Obsolete and slow-moving stock | 318–335 | B017-C3: Custom purchase remains a real company commitment. |
| E149 | [docs/warehouse/warehouse-stock-and-material-control.md](../../../../../docs/warehouse/warehouse-stock-and-material-control.md) — Write-offs and disposal | 342–347 | B017-C5: Closure waits for or transfers controlled residual decisions.; B017-CF2 |

## Reasoning path and minimum defensible outcomes

1. **Operational cancellation preserves remaining obligations.** Record authorised cancellation, actual site condition and original commitments/history. Separate operational project cancellation from unresolved purchase, return, stock and financial actions. Sources: E144, E145.
2. **Reusable and suspect materials follow different states.** Return assessed sealed £400 goods to controlled available stock with source/allocation trail under existing authority. Quarantine £100 suspect parts for assessment; do not assume reuse or silently erase cost. Sources: E146, E025.
3. **Custom purchase remains a real company commitment.** Retain £6,000 exposure and reviewed named owner for alternative use/storage/value provision or disposal. Do not automatically invoice customer absent cancellation entitlement or call custom goods worthless solely from cancellation. Sources: E145, E147, E148.
4. **Approved return progresses before its deadline.** Arrange £300 RMA dispatch/chain of custody and supplier receipt/credit chase within seven days. Keep expected credit separate from received value and preserve original wrong-order responsibility. Sources: E132, E134.
5. **Closure waits for or transfers controlled residual decisions.** Record cost/allocation corrections transparently and seek delegated write-off/settlement decisions where needed. Assign finance/procurement review and customer update dates; no ownerless return or exposure is lost at closure. Sources: E112, E149, E009.

## Alternatives

- Project operational closure with residual exposures transferred to linked accepted owners is valid; authorised redeployment/write-down/settlement may differ with evidence. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E009, E018, E019, E025, E028, E079, E112, E132, E134, E144, E145, E146, E147, E148, E149.

## Conclusions to reject

- Delete committed cost/old delivery evidence on cancellation, mark expected supplier credit received or make suspect goods available without assessment. (E025, E146, E079).
- Automatically bill £6,000 cancellation loss or dispose of custom goods without the required entitlement/authority. (E028, E149).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
