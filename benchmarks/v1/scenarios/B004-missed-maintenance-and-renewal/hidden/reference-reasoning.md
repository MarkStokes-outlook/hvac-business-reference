# Hidden reference reasoning — B004

## Material facts and uncertainties

Fixtures B004-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B004-C5: Open renewal inputs and customer commitments have owners. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E037 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Maintenance obligations and schedules | 30–45 | B004-C1: The Q3 miss remains attributed to its due period.; B004-CF1 |
| E039 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Service credits | 282–289 | B004-C4: Renewal is reviewed beyond inflation. |
| E040 | [docs/reporting/business-metrics-and-kpis.md](../../../../../docs/reporting/business-metrics-and-kpis.md) — Planned maintenance completion | 33–36 | B004-C1: The Q3 miss remains attributed to its due period. |
| E041 | [docs/dispatch/resource-planning-and-scheduling.md](../../../../../docs/dispatch/resource-planning-and-scheduling.md) — Planned-maintenance capacity | 262–269 | B004-C2: Authorised recovery is scheduled and owned. |
| E042 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Priority and urgency | 100–118 | B004-C2: Authorised recovery is scheduled and owned. |
| E043 | [docs/contracts/service-contracts.md](../../../../../docs/contracts/service-contracts.md) — Asset schedules | 46–64 | B004-C3: The renewal reflects installed equipment.; B004-CF2 |
| E044 | [docs/assets/equipment-and-asset-records.md](../../../../../docs/assets/equipment-and-asset-records.md) — Replacement and retirement | 121–133 | B004-C3: The renewal reflects installed equipment. |
| E045 | [docs/contracts/service-contracts.md](../../../../../docs/contracts/service-contracts.md) — Review and renewal | 172–188 | B004-C4: Renewal is reviewed beyond inflation. |
| E046 | [docs/contracts/service-contracts.md](../../../../../docs/contracts/service-contracts.md) — Multi-site contracts | 148–153 | B004-C4: Renewal is reviewed beyond inflation. |
| E047 | [docs/contracts/service-contracts.md](../../../../../docs/contracts/service-contracts.md) — Frostline obligations | 142–147 | B004-C5: Open renewal inputs and customer commitments have owners. |
| E048 | [docs/contracts/service-contracts.md](../../../../../docs/contracts/service-contracts.md) — Variations | 189–194 | B004-CF2 |

## Reasoning path and minimum defensible outcomes

1. **The Q3 miss remains attributed to its due period.** Record Q3 delivery 3/4 or 75%, with Site D capacity/displacement cause and breach against Q3 requirement. October recovery does not relabel Q3 as on time or create a second Q4 completion from the same obligation. Sources: E037, E040.
2. **Authorised recovery is scheduled and owned.** Arrange the available 7 October attendance with customer confirmation and maintained safety/competence readiness. Record a manager-owned recovery/communication plan for repeated displacement, rather than erasing overdue work. Sources: E041, E042.
3. **The renewal reflects installed equipment.** Verify removal/new installation evidence and retain retired histories. Route schedule variation/repricing to management/customer; avoid knowingly charging removed plant or silently including new assets. Sources: E043, E044.
4. **Renewal is reviewed beyond inflation.** Use actual labour, access/subcontract costs, equipment condition and site-specific response failures to review sustainable scope/price. Keep proposed terms and approval separate from accepted contract, and do not award invented credits. Sources: E045, E046, E039.
5. **Open renewal inputs and customer commitments have owners.** Assign new-asset survey, cost review and authorised renewal offer decisions with dates before 1 November. Explain Q3 miss/recovery and proposed review honestly, with Site D consequences visible. Sources: E009, E047.

## Alternatives

- Recovery can be brought forward if an equally ready agreed window exists; renewal options can vary if evidence-backed and separately approved. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E009, E018, E019, E037, E039, E040, E041, E042, E043, E044, E045, E046, E047, E048.

## Conclusions to reject

- Rewrite the Q3 completion/breach history as compliant because the visit occurs in October. (E037).
- Automatically renew a knowingly inaccurate schedule charging removed equipment or granting unagreed new cover. (E043, E048).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
