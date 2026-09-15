# Hidden reference reasoning — B001

## Material facts and uncertainties

Fixtures B001-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E001 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Reactive requests | 80–99 | B001-C1: A symptom-led request remains under triage with contract and impact checks. |
| E002 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Impact assessment | 68–83 | B001-C1: A symptom-led request remains under triage with contract and impact checks. |
| E003 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Priority and severity | 44–67 | B001-C1: A symptom-led request remains under triage with contract and impact checks. |
| E004 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Attendance authority | 135–150 | B001-C2: A useful diagnostic response can progress within released scope. |
| E005 | [docs/dispatch/resource-planning-and-scheduling.md](../../../../../docs/dispatch/resource-planning-and-scheduling.md) — Engineer capability | 79–97 | B001-C2: A useful diagnostic response can progress within released scope.; B001-CF2 |
| E006 | [docs/field-engineering/site-visits-and-engineer-workflow.md](../../../../../docs/field-engineering/site-visits-and-engineer-workflow.md) — Dispatch acceptance | 31–44 | B001-C2: A useful diagnostic response can progress within released scope. |
| E007 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Operational decisions | 42–47 | B001-C3: Specialist movement and chargeable work remain conditional.; B001-CF2 |
| E008 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Customer authority and purchase orders | 72–100 | B001-C3: Specialist movement and chargeable work remain conditional.; B001-CF2 |
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B001-C4: The unresolved request has an accountable next action. |
| E010 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — Handoffs | 81–98 | B001-C4: The unresolved request has an accountable next action. |
| E011 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Customer communication | 225–241 | B001-C5: Priya receives an honest operational update. |
| E012 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Core terminology | 11–27 | B001-C5: Priya receives an honest operational update. |
| E013 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Communication commitments | 220–235 | B001-C5: Priya receives an honest operational update. |
| E014 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Contract hierarchy | 28–43 | B001-CF1 |
| E015 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Customer-scope decisions | 48–63 | B001-CF1 |
| E016 | [docs/governance/canonical-terminology-and-record-relationships.md](../../../../../docs/governance/canonical-terminology-and-record-relationships.md) — Resolution | 171–174 | B001-CF3 |
| E017 | [docs/operations/work-lifecycle.md](../../../../../docs/operations/work-lifecycle.md) — 10. Closure and retained knowledge | 152–159 | B001-CF3 |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |

## Reasoning path and minimum defensible outcomes

1. **A symptom-led request remains under triage with contract and impact checks.** Record partial service loss and reported safety facts without inventing a cause or emergency status. Assign urgent checks of applicable contract, covered equipment, priority and response target. Sources: E001, E002, E003.
2. **A useful diagnostic response can progress within released scope.** Dispatch or prepare Samir only for commercially released diagnosis within his competence, with engineer acceptance. Keep advanced BMS intervention conditional on specialist competence and access evidence. Sources: E004, E005, E006.
3. **Specialist movement and chargeable work remain conditional.** Seek Helen/project-owner decision before displacing Ellie and preserve commissioning consequences. Validate authority for chargeable diagnosis, parts and specialist cost; annual maintenance PO is not unlimited approval. Sources: E007, E008.
4. **The unresolved request has an accountable next action.** Retain coordinator ownership of coverage/access/dispatch checks until an accepted handoff. Set a concrete near-term review, such as 10:45, and manager escalation if a material dependency persists. Sources: E009, E010.
5. **Priya receives an honest operational update.** Communicate the next checks, conditional response and useful access/impact clarification. Record update timing and preserve attendance/restoration/resolution differences without promising repair by 15:00. Sources: E011, E012, E013.

## Alternatives

- Bounded Samir diagnosis, brief owned hold for urgent checks, or management-approved specialist reservation are equivalent if authority, delay and displaced work are controlled. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E001, E002, E003, E004, E005, E006, E007, E008, E009, E010, E011, E012, E013, E014, E015, E016, E017, E018, E019.

## Conclusions to reject

- Commit to controls being covered, emergency/SLA entitlement or restoration by 15:00 without the missing evidence. (E014, E015).
- Direct advanced BMS work by Samir, move Ellie without the required management decision, or authorise chargeable reactive spend on the maintenance PO without validation. (E005, E007, E008).
- Mark the customer issue permanently resolved or the job operationally complete merely from dispatch. (E016, E017).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
