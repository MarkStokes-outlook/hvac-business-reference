# Hidden reference reasoning — B012

## Material facts and uncertainties

Fixtures B012-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E028 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Invoice triggers | 118–145 | B012-C3: Minor snag and material incomplete scope remain distinguishable. |
| E099 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Completion states | 309–323 | B012-C1: Running plant is not certified commissioning.; B012-C5: States and subsequent events are understandable.; B012-CF1 |
| E106 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Testing and commissioning | 263–272 | B012-C1: Running plant is not certified commissioning.; B012-CF1 |
| E107 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Handover | 290–308 | B012-C2: Outstanding documentation/registration are actively controlled. |
| E108 | [docs/manufacturers/manufacturer-relationships.md](../../../../../docs/manufacturers/manufacturer-relationships.md) — Warranty registration | 154–177 | B012-C2: Outstanding documentation/registration are actively controlled.; B012-CF1 |
| E109 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Defects, snags and incomplete work | 273–289 | B012-C3: Minor snag and material incomplete scope remain distinguishable. |
| E110 | [docs/projects/installation-project-delivery.md](../../../../../docs/projects/installation-project-delivery.md) — Project closure review | 330–346 | B012-C3: Minor snag and material incomplete scope remain distinguishable. |
| E111 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Project invoicing | 181–203 | B012-C4: Later contractual retention is assessed separately.; B012-CF2 |
| E112 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Financial closure | 451–464 | B012-C4: Later contractual retention is assessed separately. |
| E113 | [docs/finance/invoicing-cost-control-and-credit.md](../../../../../docs/finance/invoicing-cost-control-and-credit.md) — Warranty cost and recovery | 292–312 | B012-C5: States and subsequent events are understandable.; B012-CF2 |

## Reasoning path and minimum defensible outcomes

1. **Running plant is not certified commissioning.** Retain uncommissioned/partially complete status for required untested controls interface; do not infer practical completion from local running. Arrange authorised Friday competent commissioning/tests with result capture and conditions. Sources: E106, E099.
2. **Outstanding documentation/registration are actively controlled.** Assign final serial schedule/manuals, commissioning evidence submission and registration acceptance chase with owners/dates. Keep registration submitted/evidence incomplete distinct from accepted warranty registration. Sources: E107, E108.
3. **Minor snag and material incomplete scope remain distinguishable.** Classify cosmetic touch-up separately from required functional tests, with responsible owner and target date. Keep project closure and unsupported final invoice held while mandatory evidence is absent, or explicitly transfer eligible residual obligations under authority. Sources: E109, E110, E028.
4. **Later contractual retention is assessed separately.** On later notice, treat defects-period expiry/no notified defects as its own evidenced retention trigger, not dependent solely on manufacturer recovery. Keep warranty recovery owner/review and retention-release owner/entitlement distinct. Sources: E111, E112.
5. **States and subsequent events are understandable.** Give the initial customer a precise incomplete work/Friday test and handover update without promising manufacturer acceptance. On later notice, communicate/release eligible retention through finance while keeping linked warranty recovery visible; do not erase project evidence. Sources: E099, E113.

## Alternatives

- Practical completion may be decided after required tests pass with genuinely minor recorded residuals; operational project closure can transfer controlled continuing warranty obligations. No single status spelling is required. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E018, E019, E028, E099, E106, E107, E108, E109, E110, E111, E112, E113.

## Conclusions to reject

- Certify commissioning/practical completion/full closure before the required untested interface is resolved, or state registration accepted from submission. (E106, E099, E108).
- Declare manufacturer recovery received from retention payment or close an ownerless recovery because retention has been released. (E111, E113).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
