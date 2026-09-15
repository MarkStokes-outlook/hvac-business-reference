# Hidden reference reasoning — B013

## Material facts and uncertainties

Fixtures B013-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E004 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Attendance authority | 135–150 | B013-C4: New fault can progress under an explicit authorised route. |
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B013-C4: New fault can progress under an explicit authorised route. |
| E015 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Customer-scope decisions | 48–63 | B013-CF2 |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E035 | [docs/assets/equipment-and-asset-records.md](../../../../../docs/assets/equipment-and-asset-records.md) — Record quality | 134–138 | B013-C2: Shared address does not merge separate obligations.; B013-CF1 |
| E043 | [docs/contracts/service-contracts.md](../../../../../docs/contracts/service-contracts.md) — Asset schedules | 46–64 | B013-C3: Replacement does not silently amend agreed cover.; B013-CF2 |
| E044 | [docs/assets/equipment-and-asset-records.md](../../../../../docs/assets/equipment-and-asset-records.md) — Replacement and retirement | 121–133 | B013-C1: Verified replacement identity supersedes copied labels without erasing history.; B013-CF1 |
| E073 | [docs/governance/canonical-terminology-and-record-relationships.md](../../../../../docs/governance/canonical-terminology-and-record-relationships.md) — Identity and duplicate records | 300–313 | B013-C2: Shared address does not merge separate obligations.; B013-CF1 |
| E079 | [docs/information/records-documents-and-communication.md](../../../../../docs/information/records-documents-and-communication.md) — Corrections and history | 89–94 | B013-C5: Historical delivery/commercial evidence remains correctly attributable. |
| E114 | [docs/assets/equipment-and-asset-records.md](../../../../../docs/assets/equipment-and-asset-records.md) — Identity | 26–40 | B013-C1: Verified replacement identity supersedes copied labels without erasing history. |
| E115 | [docs/governance/canonical-terminology-and-record-relationships.md](../../../../../docs/governance/canonical-terminology-and-record-relationships.md) — Asset identifier | 55–58 | B013-C1: Verified replacement identity supersedes copied labels without erasing history. |
| E116 | [docs/customers/customer-and-site-model.md](../../../../../docs/customers/customer-and-site-model.md) — Commercial relationships | 26–40 | B013-C2: Shared address does not merge separate obligations. |
| E117 | [docs/assets/equipment-and-asset-records.md](../../../../../docs/assets/equipment-and-asset-records.md) — Assets under contract | 99–104 | B013-C3: Replacement does not silently amend agreed cover. |
| E118 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Suspected warranty service | 217–224 | B013-C4: New fault can progress under an explicit authorised route. |
| E119 | [docs/assets/equipment-and-asset-records.md](../../../../../docs/assets/equipment-and-asset-records.md) — Service and work history | 82–98 | B013-C5: Historical delivery/commercial evidence remains correctly attributable. |

## Reasoning path and minimum defensible outcomes

1. **Verified replacement identity supersedes copied labels without erasing history.** Distinguish NEW-13 from retired OLD-13 despite retained tag/location. Keep separate manufacturer serial/customer tag/internal identity and preserve replacement relationship/source evidence. Sources: E114, E044, E115.
2. **Shared address does not merge separate obligations.** Keep Tenant A/B commercial relationships, systems and B-13 history separate. Flag uncertain copied F-13/Calder association, retaining aliases and provenance until reconciled rather than asserting false certainty. Sources: E073, E116, E035.
3. **Replacement does not silently amend agreed cover.** Refer OLD-13 to NEW-13 schedule discrepancy to management for coverage/variation review. Do not automatically grant all new-unit entitlement or knowingly renew billing for removed equipment without review. Sources: E043, E117.
4. **New fault can progress under an explicit authorised route.** Create symptom-led triage/new-unit response with separate contract, warranty/customer-care or diagnostic-release decision. Record specific owner, missing coverage/authority, physical access and near-term next action/escalation. Sources: E004, E118, E009.
5. **Historical delivery/commercial evidence remains correctly attributable.** Keep OLD-13 invoices/warranty/refrigerant work attached to old identity with correction explanation. Communicate corrected asset/scope discrepancy to engineers/account/finance as needed without inventing new history. Sources: E079, E119.

## Alternatives

- Logical duplicate entries can be consolidated after evidenced reconciliation if old source references, distinct replaced plant and tenant boundaries survive; implementation-specific record counts do not matter. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E004, E009, E015, E018, E019, E035, E043, E044, E073, E079, E114, E115, E116, E117, E118, E119.

## Conclusions to reject

- Merge tenants/assets on postal address or CU-1 label, overwrite OLD-13 history with NEW-13, or copy unverified serials to complete the register. (E073, E035, E044).
- Commit to new-unit contract entitlement solely because the replaced unit was listed. (E043, E015).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
