# Hidden reference reasoning — B010

## Material facts and uncertainties

Fixtures B010-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B010-C4: Dependencies have accountable decision paths. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E089 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Project release states | 60–77 | B010-C1: Approved procurement can progress. |
| E090 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Purchase orders | 128–146 | B010-C1: Approved procurement can progress. |
| E091 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Supplier acknowledgement | 147–161 | B010-C1: Approved procurement can progress. |
| E092 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Internal release decision | 78–94 | B010-C2: Procurement release does not release unsafe site work.; B010-CF2 |
| E093 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Pre-start planning | 103–124 | B010-C2: Procurement release does not release unsafe site work.; B010-CF1 |
| E094 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Design and responsibility boundaries | 125–138 | B010-C3: Outside design ownership does not permit blind installation.; B010-CF1 |
| E095 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Materials and equipment | 158–175 | B010-C4: Dependencies have accountable decision paths. |
| E096 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Programme and resource planning | 139–157 | B010-C4: Dependencies have accountable decision paths. |
| E097 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Decision evidence | 148–163 | B010-C5: The permitted stage and held stage are clear. |
| E098 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Project creation and identity | 17–36 | B010-C5: The permitted stage and held stage are clear. |
| E099 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Completion states | 309–323 | B010-C5: The permitted stage and held stage are clear. |
| E100 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Delegated limits | 94–111 | B010-CF2 |

## Reasoning path and minimum defensible outcomes

1. **Approved procurement can progress.** Issue specified U-10 order within £24,000 scoped release and agreed £23,500 basis; avoid needless blanket hold of approved purchase. Record exact specification, budget/authority, non-cancellable condition, delivery allocation and acknowledgement chase after issue. Sources: E089, E090, E091.
2. **Procurement release does not release unsafe site work.** Keep Monday start provisional/operationally and technically held for named enabling prerequisites. Do not send installation labour for dependent physical work before reviewed readiness/mobilisation authority. Sources: E092, E093.
3. **Outside design ownership does not permit blind installation.** Identify consultant/customer structural design ownership and what Frostline has/has not verified. Escalate unsupported structural suitability rather than infer all design responsibility transferred from drawing approval. Sources: E094.
4. **Dependencies have accountable decision paths.** Assign structural/electrical customer actors and Frostline chase owner with hold-point dates. Protect delivery/storage and resource plan from provisional dates and assess delay/non-cancellable exposure. Sources: E095, E096, E009.
5. **The permitted stage and held stage are clear.** Tell customer what has been released, what prevents start and next evidence/update requirement. Preserve release decision scope/conditions and linked customer, purchase and project references without collapsing states. Sources: E097, E098, E099.

## Alternatives

- A separately reviewed survey/preparation attendance is permissible without implying dependent installation mobilisation; purchase date may vary within supplier terms if rationale and exposure are explicit. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E009, E018, E019, E089, E090, E091, E092, E093, E094, E095, E096, E097, E098, E099, E100.

## Conclusions to reject

- Mobilise dependent installation on unsupported structures from customer urgency, drawing approval or procurement release. (E094, E093).
- Extend procurement beyond the specified released item/value without new authority. (E092, E100).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
