# Hidden reference reasoning — B003

## Material facts and uncertainties

Fixtures B003-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B003-C5: Lena controls the incomplete work and customer update. |
| E011 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Customer communication | 225–241 | B003-C5: Lena controls the incomplete work and customer update. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | B003-CF2; Preserve declared uncertainty and separate required authorities |
| E030 | [docs/field-engineering/site-visits-and-engineer-workflow.md](../../../../../docs/field-engineering/site-visits-and-engineer-workflow.md) — Sign-off | 315–326 | B003-C2: Motor replacement follows a separate controlled path. |
| E033 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Maintenance completion states | 46–59 | B003-C1: Only evidenced maintenance is complete.; B003-CF1 |
| E034 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Defects found during maintenance | 60–79 | B003-C1: Only evidenced maintenance is complete.; B003-C2: Motor replacement follows a separate controlled path.; B003-CF2 |
| E035 | [docs/assets/equipment-and-asset-records.md](../../../../../docs/assets/equipment-and-asset-records.md) — Record quality | 134–138 | B003-C3: The next attendance is prepared rather than blindly repeated.; B003-CF1 |
| E036 | [docs/dispatch/resource-planning-and-scheduling.md](../../../../../docs/dispatch/resource-planning-and-scheduling.md) — Customer access and site readiness | 164–179 | B003-C3: The next attendance is prepared rather than blindly repeated. |
| E037 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Maintenance obligations and schedules | 30–45 | B003-C4: The contractual obligation survives the attendance and billing. |
| E038 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Reactive and service invoicing | 164–180 | B003-C4: The contractual obligation survives the attendance and billing. |
| E039 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Service credits | 282–289 | B003-C4: The contractual obligation survives the attendance and billing. |

## Reasoning path and minimum defensible outcomes

1. **Only evidenced maintenance is complete.** Recognise AHU-1 maintenance completed with defect recommendation, not failed merely because a defect was found. Preserve AHU-2 and B-1 outstanding obligations with their specific access/identity reasons. Sources: E033, E034.
2. **Motor replacement follows a separate controlled path.** Create owned repair quotation/review recommendation from measured wear and safety condition. Do not perform/authorise motor replacement from maintenance entitlement or caretaker acknowledgement. Sources: E034, E030.
3. **The next attendance is prepared rather than blindly repeated.** Assign permit confirmation and physical boiler reconciliation without copying a serial or merging boiler histories. Keep Wednesday provisional until access and identification method/competence are sufficient. Sources: E035, E036.
4. **The contractual obligation survives the attendance and billing.** Retain partial maintenance/job status and due-period obligations despite signed attendance and prior billing. Review any due-window risk against actual contract; do not invent automatic credits or waived duties. Sources: E037, E038, E039.
5. **Lena controls the incomplete work and customer update.** Record named chase owner, school actor, next review and escalation for permit and identity waits. Send a summary separating work delivered, work omitted, safety finding and separately proposed repair. Sources: E009, E011.

## Alternatives

- One partial job or linked attendance/obligation records are equivalent; AHU-1 may close independently if unresolved tasks remain visible and owned. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E009, E011, E018, E019, E030, E033, E034, E035, E036, E037, E038, E039.

## Conclusions to reject

- Certify all scheduled maintenance complete from site attendance/signature, or fabricate boiler identity/readings. (E033, E035).
- Replace the excluded motor without both required authorities. (E034, E019).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
