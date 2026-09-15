# Hidden reference reasoning — B008

## Material facts and uncertainties

Fixtures B008-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E009 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — The next-action principle | 9–21 | B008-C4: Mismatch has an active resolution path. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E069 | [docs/quoting/estimating-and-quotation.md](../../../../../docs/quoting/estimating-and-quotation.md) — Revision control | 214–221 | B008-C1: Ambiguous acceptance stays under validation. |
| E070 | [docs/quoting/estimating-and-quotation.md](../../../../../docs/quoting/estimating-and-quotation.md) — Acceptance validation | 222–237 | B008-C1: Ambiguous acceptance stays under validation.; B008-CF1 |
| E071 | [docs/quoting/estimating-and-quotation.md](../../../../../docs/quoting/estimating-and-quotation.md) — Options and alternatives | 162–177 | B008-C1: Ambiguous acceptance stays under validation. |
| E072 | [docs/customers/customer-and-site-model.md](../../../../../docs/customers/customer-and-site-model.md) — Contracting entity and billing entity | 90–95 | B008-C2: Commercial customer and site contact remain distinct.; B008-CF2 |
| E073 | [docs/governance/canonical-terminology-and-record-relationships.md](../../../../../docs/governance/canonical-terminology-and-record-relationships.md) — Identity and duplicate records | 300–313 | B008-C2: Commercial customer and site contact remain distinct. |
| E074 | [docs/quoting/estimating-and-quotation.md](../../../../../docs/quoting/estimating-and-quotation.md) — Internal approval | 199–213 | B008-C3: Approval to issue is not authority to procure.; B008-CF1 |
| E075 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Commercial release | 101–117 | B008-C3: Approval to issue is not authority to procure. |
| E076 | [docs/quoting/estimating-and-quotation.md](../../../../../docs/quoting/estimating-and-quotation.md) — Commercial release to delivery | 238–253 | B008-C4: Mismatch has an active resolution path. |
| E077 | [docs/quoting/estimating-and-quotation.md](../../../../../docs/quoting/estimating-and-quotation.md) — Handover after award | 254–261 | B008-C5: Delivery receives only the validated accepted basis. |
| E078 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Handover from sales and estimating | 37–59 | B008-C5: Delivery receives only the validated accepted basis. |
| E079 | [docs/information/records-documents-and-communication.md](../../../../../docs/information/records-documents-and-communication.md) — Corrections and history | 89–94 | B008-CF2 |

## Reasoning path and minimum defensible outcomes

1. **Ambiguous acceptance stays under validation.** Preserve Q-H8 revision histories; identify PO revision/value/scope mismatch rather than mark revision 2 unconditionally accepted. Clarify selected base/controls option and customer terms with an identifiable authorised party. Sources: E069, E070, E071.
2. **Commercial customer and site contact remain distinct.** Validate landlord/tenant contracting entity and intermediary authority before billing/release. Preserve issued PO/reference and evidence rather than merging group companies or silently editing the order. Sources: E072, E073.
3. **Approval to issue is not authority to procure.** Retain commercially held/awaiting acceptance validation state for incompatible order and deposit/credit conditions. Do not place the non-cancellable purchase from verbal “go ahead” or issue approval alone. Sources: E074, E075.
4. **Mismatch has an active resolution path.** Assign estimator/account owner to acceptance/entity clarification, and finance/purchasing actors for release decisions. Record chase/deadline and supplier price/availability review trigger before irreversible commitment. Sources: E009, E076.
5. **Delivery receives only the validated accepted basis.** Communicate the specific mismatches and remaining conditions honestly to customer without inventing a confirmed start. Keep handoff responsibility with estimator until receiving project owner accepts an adequate scope/release package. Sources: E077, E078.

## Alternatives

- Conditional reservation with no cost commitment may be explored; a limited survey may proceed only under separate explicit authority, not implied order acceptance. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E009, E018, E019, E069, E070, E071, E072, E073, E074, E075, E076, E077, E078, E079.

## Conclusions to reject

- Treat this mismatched PO as unconditional authority for revision 2 plus enhanced controls or order non-cancellable equipment before release. (E070, E074).
- Invent Morgan authority to bind landlord or silently change the liable customer/accepted quotation history. (E072, E079).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
