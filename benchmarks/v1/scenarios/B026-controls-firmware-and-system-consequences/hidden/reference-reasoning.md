# Hidden reference reasoning — B026

## Material facts and uncertainties

Fixtures B026-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B026-C5: The technical and authority dependencies remain actionable. |
| E011 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Customer communication | 225–241 | B026-C5: The technical and authority dependencies remain actionable. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E023 | [docs/field-engineering/site-visits-and-engineer-workflow.md](../../../../../docs/field-engineering/site-visits-and-engineer-workflow.md) — Testing and recommissioning | 239–255 | B026-C3: A system update includes change and testing controls. |
| E054 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — Temporary measures | 165–181 | B026-C4: Energy and troubleshooting do not defeat required service.; B026-CF2 |
| E094 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Design and responsibility boundaries | 125–138 | B026-C3: A system update includes change and testing controls. |
| E122 | [docs/technical-support/diagnostics-controls-and-technical-escalation.md](../../../../../docs/technical-support/diagnostics-controls-and-technical-escalation.md) — Diagnostic principles | 9–27 | B026-C1: Manufacturer advice remains bounded technical evidence. |
| E204 | [docs/environment/refrigerants-energy-and-environmental-performance.md](../../../../../docs/environment/refrigerants-energy-and-environmental-performance.md) — Controls and optimisation | 63–68 | B026-C4: Energy and troubleshooting do not defeat required service.; B026-CF2 |
| E210 | [docs/manufacturers/manufacturer-relationships.md](../../../../../docs/manufacturers/manufacturer-relationships.md) — Advice records and authority | 112–136 | B026-C1: Manufacturer advice remains bounded technical evidence. |
| E211 | [docs/manufacturers/manufacturer-relationships.md](../../../../../docs/manufacturers/manufacturer-relationships.md) — Software and firmware | 291–308 | B026-C2: Significant update requires supported prerequisites.; B026-C3: A system update includes change and testing controls.; B026-CF1 |
| E212 | [docs/technical-support/diagnostics-controls-and-technical-escalation.md](../../../../../docs/technical-support/diagnostics-controls-and-technical-escalation.md) — Controls and BMS interfaces | 70–90 | B026-C2: Significant update requires supported prerequisites. |
| E213 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Technical decisions | 28–41 | B026-C2: Significant update requires supported prerequisites.; B026-CF1 |
| E214 | [docs/technical-support/diagnostics-controls-and-technical-escalation.md](../../../../../docs/technical-support/diagnostics-controls-and-technical-escalation.md) — Temporary measures | 91–96 | B026-C4: Energy and troubleshooting do not defeat required service. |
| E215 | [docs/manufacturers/manufacturer-relationships.md](../../../../../docs/manufacturers/manufacturer-relationships.md) — Escalation and relationship ownership | 392–405 | B026-C5: The technical and authority dependencies remain actionable. |

## Reasoning path and minimum defensible outcomes

1. **Manufacturer advice remains bounded technical evidence.** Retain support case, symptom/log/test evidence, conditions and uncertain root cause rather than call update a proven complete remedy. Keep manufacturer advice distinct from customer scope, Frostline expenditure and safe local execution authority. Sources: E210, E122.
2. **Significant update requires supported prerequisites.** Do not assign Rina significant firmware update beyond authorisation; arrange Sol/controls contractor under explicit allocation and scope authority. Verify current/target versions, gateway dependencies, release notes and warranty/support effects before intervention. Sources: E211, E212, E213.
3. **A system update includes change and testing controls.** Arrange authorised downtime, configuration backup and rollback plan with customer/controls owner involvement. Specify and retain recommissioning tests for heating/cooling/required ventilation and record resulting configuration/change, not just disappearance of alarm. Sources: E211, E023, E094.
4. **Energy and troubleshooting do not defeat required service.** Reject disabling required occupied ventilation as proposed energy saving/testing shortcut without a justified safe authorised method. Preserve documented temporary workaround limits/review and permanent resolution owner while the update remains conditional. Sources: E204, E214, E054.
5. **The technical and authority dependencies remain actionable.** Assign gateway/backup/customer-approval/specialist chase owner and decision review before tomorrow 10:00 workaround trigger. Update both affected customer interests with verified partial service, unknowns and next action without promising permanent fix from advisory note. Sources: E009, E215, E011.

## Alternatives

- Further diagnostic monitoring or a reviewed update may be chosen; temporary workaround continuation requires authorised reviewed limits. A gateway/controls-contractor intervention is valid only within its established safe scope and authority. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E009, E011, E018, E019, E023, E054, E094, E122, E204, E210, E211, E212, E213, E214, E215.

## Conclusions to reject

- Direct significant firmware change outside competence/authority without compatibility, backup and controlled downtime/test prerequisites. (E211, E213).
- Disable required occupied ventilation to claim savings or leave the temporary workaround as unreviewed permanent service. (E204, E054).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
