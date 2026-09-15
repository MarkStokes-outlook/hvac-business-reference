# Hidden reference reasoning — B014

## Material facts and uncertainties

Fixtures B014-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E011 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Customer communication | 225–241 | B014-C5: The isolated plant and procurement wait are actively controlled. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E087 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Customer approval and company approval | 120–127 | B014-C3: Restricted approval and diagnostic scope are respected.; B014-CF1 |
| E091 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Supplier acknowledgement | 147–161 | B014-C4: Tomorrow remains provisional until dependencies are sufficient. |
| E120 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Purchase requirement | 11–31 | B014-C1: Identification request remains distinct from purchase. |
| E121 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Requirement maturity | 32–47 | B014-C1: Identification request remains distinct from purchase.; B014-CF2 |
| E122 | [docs/technical-support/diagnostics-controls-and-technical-escalation.md](../../../../../docs/technical-support/diagnostics-controls-and-technical-escalation.md) — Diagnostic principles | 9–27 | B014-C1: Identification request remains distinct from purchase. |
| E123 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Substitutions | 170–190 | B014-C2: Supplier assertion does not establish a suitable substitute.; B014-CF1 |
| E124 | [docs/manufacturers/manufacturer-relationships.md](../../../../../docs/manufacturers/manufacturer-relationships.md) — Spare parts and supersession | 309–325 | B014-C2: Supplier assertion does not establish a suitable substitute. |
| E125 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Approved, conditional and restricted suppliers | 68–82 | B014-C3: Restricted approval and diagnostic scope are respected. |
| E126 | [docs/dispatch/resource-planning-and-scheduling.md](../../../../../docs/dispatch/resource-planning-and-scheduling.md) — Parts and materials readiness | 134–150 | B014-C4: Tomorrow remains provisional until dependencies are sufficient.; B014-CF2 |
| E127 | [docs/service/planned-and-reactive-service.md](../../../../../docs/service/planned-and-reactive-service.md) — Parts and return attendances | 183–192 | B014-C4: Tomorrow remains provisional until dependencies are sufficient. |
| E128 | [docs/procurement/purchasing-and-supplier-control.md](../../../../../docs/procurement/purchasing-and-supplier-control.md) — Open purchasing exceptions | 307–320 | B014-C5: The isolated plant and procurement wait are actively controlled. |

## Reasoning path and minimum defensible outcomes

1. **Identification request remains distinct from purchase.** Keep request at identification/technical-review stage, collecting model/serial/photo/rating/test basis rather than calling it ordered. Assign engineering owner to verified cause and usable specification/question for supplier/manufacturer. Sources: E120, E121, E122.
2. **Supplier assertion does not establish a suitable substitute.** Require technical review of voltage, controls, physical fit, duty and supersession changes before accepting alternative. Separate customer specification/approval and commercial/warranty consequences from technical recommendation. Sources: E123, E124.
3. **Restricted approval and diagnostic scope are respected.** Escalate supplier use outside approved category or select appropriately approved supplier. Keep purchase on hold until customer/Frostline commitment authorities or explicit manager-owned exposure decision are evidenced. Sources: E125, E087.
4. **Tomorrow remains provisional until dependencies are sufficient.** Do not represent quotation/identification enquiry as ordered, acknowledged or received stock. Confirm exact part/availability/reservation, shutdown/access and competence before firm return attendance. Sources: E091, E126, E127.
5. **The isolated plant and procurement wait are actively controlled.** Record safe isolated condition, technical/approval/supply dependencies and named chase/review/escalation. Tell customer verified unknowns, alternatives being checked and next update without promising tomorrow repair. Sources: E128, E011.

## Alternatives

- Further diagnosis, original compatible part, or reviewed substitute may each be correct; emergency substitution still needs explicit safe suitability and scoped authority. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E011, E018, E019, E087, E091, E120, E121, E122, E123, E124, E125, E126, E127, E128.

## Conclusions to reject

- Purchase/fit the changed-interface fan on supplier assurance alone or outside current technical/customer/Frostline authority. (E123, E087).
- Mark the distributor identification enquiry as confirmed ordered/delivered and promise a ready repair from it. (E121, E126).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
