# Hidden reference reasoning — B016

## Material facts and uncertainties

Fixtures B016-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B016-C5: Urgent and displaced dependencies remain visible. |
| E011 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Customer communication | 225–241 | B016-C5: Urgent and displaced dependencies remain visible. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E054 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — Temporary measures | 165–181 | B016-C5: Urgent and displaced dependencies remain visible. |
| E059 | [docs/dispatch/resource-planning-and-scheduling.md](../../../../../docs/dispatch/resource-planning-and-scheduling.md) — Emergency displacement | 197–209 | B016-C3: One urgent request does not silently steal another commitment. |
| E136 | [docs/warehouse/warehouse-stock-and-material-control.md](../../../../../docs/warehouse/warehouse-stock-and-material-control.md) — Available, reserved and quarantined states | 95–110 | B016-C1: State and ownership qualify physical quantities. |
| E137 | [docs/warehouse/warehouse-stock-and-material-control.md](../../../../../docs/warehouse/warehouse-stock-and-material-control.md) — Customer-owned and consignment stock | 187–202 | B016-C1: State and ownership qualify physical quantities.; B016-C4: Custody does not create rights to use property.; B016-CF1 |
| E138 | [docs/dispatch/resource-planning-and-scheduling.md](../../../../../docs/dispatch/resource-planning-and-scheduling.md) — Van stock and distributed inventory | 151–163 | B016-C1: State and ownership qualify physical quantities.; B016-CF2 |
| E139 | [docs/warehouse/warehouse-stock-and-material-control.md](../../../../../docs/warehouse/warehouse-stock-and-material-control.md) — Van stock | 203–212 | B016-C2: A suitable authorised van transfer can meet the need. |
| E140 | [docs/warehouse/warehouse-stock-and-material-control.md](../../../../../docs/warehouse/warehouse-stock-and-material-control.md) — Picking and issue | 129–146 | B016-C2: A suitable authorised van transfer can meet the need. |
| E141 | [docs/warehouse/warehouse-stock-and-material-control.md](../../../../../docs/warehouse/warehouse-stock-and-material-control.md) — Reservation and allocation | 111–128 | B016-C3: One urgent request does not silently steal another commitment.; B016-CF1 |
| E142 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Lead times and expediting | 162–169 | B016-C3: One urgent request does not silently steal another commitment.; B016-CF2 |
| E143 | [docs/governance/canonical-terminology-and-record-relationships.md](../../../../../docs/governance/canonical-terminology-and-record-relationships.md) — Responsible party | 273–276 | B016-C4: Custody does not create rights to use property. |

## Reasoning path and minimum defensible outcomes

1. **State and ownership qualify physical quantities.** Identify reserved Project board and Lake-owned spare as unavailable for unrestricted urgent issue. Verify Dana quantity/variant/condition/reservation before relying on van record. Sources: E136, E137, E138.
2. **A suitable authorised van transfer can meet the need.** Choose/prepare Dana-to-Omar transfer after verification, within exact repair authority and practical travel. Record item/quantity, source van, destination engineer/job, time, custody and replenishment consequence. Sources: E139, E140.
3. **One urgent request does not silently steal another commitment.** If reserved board is considered, seek reviewed authorised reallocation, Pat notification and impact/replacement plan. Do not treat indicative supplier next-day date as confirmed cover for tomorrow commissioning. Sources: E141, E059, E142.
4. **Custody does not create rights to use property.** Keep Lake spare distinct and do not consume or relabel as Frostline property without agreement. If Lake use is proposed, require permitted-use/owner and commercial/return/replenishment decision before issue. Sources: E137, E143.
5. **Urgent and displaced dependencies remain visible.** Record J-16 temporary workaround/limits, source-verification owner and near-term review/escalation. Communicate confirmed versus provisional response to customer and affected project owner. Sources: E054, E009, E011.

## Alternatives

- Explicitly approved reservation reallocation is valid after both commitments are reviewed and displaced owner notified. Lake-owned use is possible only with newly evidenced agreement, not mere possession. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E009, E011, E018, E019, E054, E059, E136, E137, E138, E139, E140, E141, E142, E143.

## Conclusions to reject

- Take Lake property without permitted use/owner agreement or silently reassign reserved board without reviewed consequences/notification. (E137, E141).
- Fabricate physical availability or guaranteed next-day replenishment to certify repair/project readiness. (E138, E142).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
