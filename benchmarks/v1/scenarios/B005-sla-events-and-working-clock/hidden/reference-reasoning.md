# Hidden reference reasoning — B005

## Material facts and uncertainties

Fixtures B005-F1 onward establish this episode only. The unknowns declared in `public/fixtures.json` remain unresolved except where an administrator event expressly supplies later evidence. Read the evidence map below alongside the named outcomes; it does not grant missing authority or invent a diagnosis.

## Evidence map

| ID | Authoritative document and heading | Source lines | Governed interpretation |
|---|---|---|---|
| E012 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Core terminology | 11–27 | B005-C2: Different service events remain distinct.; B005-CF2 |
| E013 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Communication commitments | 220–235 | B005-C5: The event analysis remains actionable. |
| E018 | [docs/governance/repository-constitution.md](../../../../../docs/governance/repository-constitution.md) — 4. Preserve uncertainty | 21–24 | Preserve declared uncertainty and separate required authorities |
| E019 | [docs/governance/decision-rights-and-operational-authority.md](../../../../../docs/governance/decision-rights-and-operational-authority.md) — Core principle | 9–19 | Preserve declared uncertainty and separate required authorities |
| E039 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Service credits | 282–289 | B005-C4: Attainment is not an invented service-credit decision.; B005-CF2 |
| E049 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Coverage hours | 84–97 | B005-C1: The attendance deadline follows covered time. |
| E050 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Attendance targets | 130–145 | B005-C1: The attendance deadline follows covered time.; B005-CF1 |
| E051 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Clock stops | 161–181 | B005-C1: The attendance deadline follows covered time.; B005-C3: Only permitted genuinely blocking time is excluded.; B005-CF1 |
| E052 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Restoration and resolution | 146–160 | B005-C2: Different service events remain distinct.; B005-C4: Attainment is not an invented service-credit decision. |
| E053 | [docs/contracts/slas-response-and-coverage.md](../../../../../docs/contracts/slas-response-and-coverage.md) — Subcontractor and third-party dependencies | 197–202 | B005-C3: Only permitted genuinely blocking time is excluded.; B005-CF1 |
| E054 | [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../../docs/operations/exceptions-handoffs-and-next-action-control.md) — Temporary measures | 165–181 | B005-C5: The event analysis remains actionable. |

## Reasoning path and minimum defensible outcomes

1. **The attendance deadline follows covered time.** Calculate nominal deadline Monday 12:00: Friday one hour plus Monday three. Apply the evidenced 45-minute permitted no-access stop to give adjusted deadline Monday 12:45; attendance 12:15 attains it with 3h30 measured working time. Sources: E049, E050, E051.
2. **Different service events remain distinct.** Record receipt, acknowledgement, remote response, car-park arrival and meaningful attendance separately. Record restoration Monday 14:00 and resolution Wednesday 10:00; do not call temporary service permanent repair. Sources: E012, E052.
3. **Only permitted genuinely blocking time is excluded.** Retain no-access evidence, exact interval, expected keyholder, Pat chase and restart event. Reject retrospective subcontractor-choice clock stop rather than removing Frostline accountability. Sources: E051, E053.
4. **Attainment is not an invented service-credit decision.** Do not calculate or grant credit without applicable contractual eligibility/formula and authorised finance treatment. Do not invent a resolution target or use out-of-hours/premium assumptions to change credit terms. Sources: E039, E052.
5. **The event analysis remains actionable.** Provide customer-attainable explanation of measured attendance and access delay without obscuring elapsed experience. Retain temporary limits/review and owner of permanent repair in history, plus owner for contract/credit questions. Sources: E013, E054.

## Alternatives

- Report both unadjusted breach and contract-adjusted attainment if labels, stop evidence and arithmetic are clear; alternative clock representation is acceptable with identical measured time. Sources: the applicable criterion/uncertainty entries in the evidence map above; full dependency IDs E012, E013, E018, E019, E039, E049, E050, E051, E052, E053, E054.

## Conclusions to reject

- Use car-park time to certify meaningful attendance, or create the retrospective subcontractor stop to improve performance. (E050, E051, E053).
- Claim permanent resolution from Monday temporary restoration, or invent service-credit entitlement. (E012, E039).

## Administration

Score all supplied stages. Issue only the neutral next-stage event from `admin-events.json` at the stage boundary; never supply this reasoning or oracle. No additional records or approvals may be invented to repair a candidate decision. Assess business-equivalent relationships and outcomes, including an owned refusal, escalation or clarified hold where justified.
