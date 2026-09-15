# Hidden reference reasoning — B024

## Material facts and uncertainties

Fixtures B024-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B024-C5: The readout identifies actionable unresolved work. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E024 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Operational completion and financial closure | 146–163 | B024-C4: Uninvoiced cost/recovery uncertainty are visible.; B024-CF2 |
| E037 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Maintenance obligations and schedules | 30–45 | B024-C2: Period delivery does not erase overdue obligations.; B024-CF1 |
| E039 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Service credits | 282–289 | B024-C2: Period delivery does not erase overdue obligations. |
| E040 | [docs/reporting/business-metrics-and-kpis.md](../../../../../docs/reporting/business-metrics-and-kpis.md) — Planned maintenance completion | 33–36 | B024-C2: Period delivery does not erase overdue obligations. |
| E135 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Accruals and uninvoiced cost | 277–291 | B024-C4: Uninvoiced cost/recovery uncertainty are visible.; B024-CF2 |
| E153 | [docs/manufacturers/manufacturer-relationships.md](../../../../../docs/manufacturers/manufacturer-relationships.md) — Labour and warranty recovery | 230–246 | B024-C4: Uninvoiced cost/recovery uncertainty are visible.; B024-CF2 |
| E174 | [docs/customer-service/complaints-escalations-and-service-recovery.md](../../../../../docs/customer-service/complaints-escalations-and-service-recovery.md) — What counts as a complaint | 9–25 | B024-C5: The readout identifies actionable unresolved work.; B024-CF1 |
| E189 | [docs/reporting/business-metrics-and-kpis.md](../../../../../docs/reporting/business-metrics-and-kpis.md) — First-time fix rate | 41–46 | B024-C1: First-time fix reflects eligible durable outcomes. |
| E190 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — First-time fix | 167–182 | B024-C1: First-time fix reflects eligible durable outcomes. |
| E191 | [docs/reporting/business-metrics-and-kpis.md](../../../../../docs/reporting/business-metrics-and-kpis.md) — Recall or callback rate | 71–74 | B024-C1: First-time fix reflects eligible durable outcomes. |
| E192 | [docs/reporting/business-metrics-and-kpis.md](../../../../../docs/reporting/business-metrics-and-kpis.md) — Mean time to respond | 47–52 | B024-C3: Response, attendance, restoration and resolution are distinct. |
| E193 | [docs/reporting/business-metrics-and-kpis.md](../../../../../docs/reporting/business-metrics-and-kpis.md) — Mean time to repair | 53–56 | B024-C3: Response, attendance, restoration and resolution are distinct. |
| E194 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Performance measurement | 264–281 | B024-C3: Response, attendance, restoration and resolution are distinct. |
| E195 | [docs/reporting/business-metrics-and-kpis.md](../../../../../docs/reporting/business-metrics-and-kpis.md) — Gross margin | 103–106 | B024-C4: Uninvoiced cost/recovery uncertainty are visible. |
| E196 | [docs/reporting/business-metrics-and-kpis.md](../../../../../docs/reporting/business-metrics-and-kpis.md) — Data quality | 247–261 | B024-C5: The readout identifies actionable unresolved work.; B024-CF1 |
| E197 | [docs/reporting/business-metrics-and-kpis.md](../../../../../docs/reporting/business-metrics-and-kpis.md) — Ownership and action | 262–266 | B024-C5: The readout identifies actionable unresolved work. |

## Reasoning path and minimum defensible outcomes

1. **First-time fix reflects eligible durable outcomes.** Calculate suitable denominator R1/R2/R6 = 3 and numerator R1 = 1; first-time fix 1/3 (33.3% rounded). Separate diagnostic completion, planned return, unsafe/no justified repair exclusions and R6 callback; do not count temporary R2 as durable first-time success. Sources: E189, E190, E191.
2. **Period delivery does not erase overdue obligations.** Report on-time completion 2/4 = 50%, retaining M3 no-access and M4 late capacity cause. Keep later recovery separate from in-window attainment and do not invent automatic service credits. Sources: E037, E040, E039.
3. **Response, attendance, restoration and resolution are distinct.** Report mean initial response 15 min, attendance 90 min and attendance attainment 2/2 = 100% including Y boundary. Report mean restoration 3h30 and permanent resolution 14h; preserve X 24h versus Y 4h permanent outcomes and small-sample/breach context. Sources: E192, E193, E194.
4. **Uninvoiced cost/recovery uncertainty are visible.** Accrue/forecast £4,000 delivered subcontract cost: total £22,000; gross margin £8,000 and 26.7% of £30,000, not £12,000/40%. Do not treat conditional £1,000 as realised recovery. Keep £8,000 invoice issued/not due separate from cash received (£0 for that invoice); do not assert whole-business profit or cash from missing data. Sources: E135, E195, E153, E024.
5. **The readout identifies actionable unresolved work.** Capture X complaint despite no formal word, unresolved diagnostic/temporary/unsafe outcomes and responsible follow-up rather than declare everything complete/no complaints. Assign owners/review for repeat failure, missed updates, maintenance backlog and financial evidence; disclose definitions/eligibility and insufficient trend/sample information. Sources: E174, E196, E197, E009.

## Alternatives

- Equivalent fractions and normal rounding are accepted. Callback count R6 = 1 is sufficient; no unique overall callback-rate denominator is established for these mixed issue records, so an explicit defensible scope or refusal to fabricate one receives credit. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E009, E018, E019, E024, E037, E039, E040, E135, E153, E174, E189, E190, E191, E192, E193, E194, E195, E196, E197.

## Conclusions to reject

- Publish the proposed 100% fix/maintenance or no-complaint headline while suppressing known incomplete/late/complaint evidence. (E196, E037, E174).
- Represent £12,000 as actual gross margin ignoring delivered subcontract cost, conditional credit as received, or invoice as cash paid. (E135, E153, E024).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
