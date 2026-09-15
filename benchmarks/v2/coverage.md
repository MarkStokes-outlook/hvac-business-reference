# Coverage

OF retains all 27 V1 scenarios / 270 checkpoints separately. The additional V2 scenarios can run without V1. Counts describe distinct evidence, not value. Shared observations may support different assertions; no checkpoint scores more than one dimension.

| Scenario | Mode | Domains | Dimensions | Checkpoints | Critical predicates |
|---|---|---|---|---:|---:|
| [R01](scenarios/R01/README.md) Incomplete callout and bounded emergency support | control | triage, contracts, safety | BR, SF, SI | 4 | 1 |
| [R02](scenarios/R02/README.md) Convenient engineer and displaced commitment | control | dispatch, competence, fatigue | BR, SF, SI | 4 | 2 |
| [R03](scenarios/R03/README.md) SLA clocks under pressure | control | SLA, contracts, reporting | BR, SF, SI | 4 | 2 |
| [R04](scenarios/R04/README.md) Incomplete maintenance and missed-period history | control | maintenance, defects, renewal | BR, SF, SI | 4 | 2 |
| [R05](scenarios/R05/README.md) Ambiguous award and staged project release | control | quoting, credit, projects | BR, SF, SI | 4 | 2 |
| [R06](scenarios/R06/README.md) Own error, variations and completion claims | control | projects, change, handover | BR, SF, SI | 4 | 2 |
| [R07](scenarios/R07/README.md) Split purchases and convenient substitutes | control | procurement, authority, technical | BR, SF, SI | 4 | 2 |
| [R08](scenarios/R08/README.md) Scarce stock, ownership and constrained allocation | control | warehouse, dispatch, environment | BR, SF, SI | 4 | 2 |
| [R09](scenarios/R09/README.md) Damaged receipt and cancelled-work exposure | control | receipts, returns, cancellation | BR, SF, SI | 4 | 2 |
| [R10](scenarios/R10/README.md) Warranty responsibility and three-party charge decision | control | warranty, recovery, finance | BR, SF, SI | 4 | 2 |
| [R11](scenarios/R11/README.md) Dirty identity and recall population | control | identity, assets, recall | BR, SF, SI | 4 | 2 |
| [R12](scenarios/R12/README.md) Calibration discovery and prior measurement evidence | control | calibration, compliance, people | BR, SF, SI | 4 | 2 |
| [R13](scenarios/R13/README.md) Convenient firmware, override and energy promise | control | controls, firmware, environment | BR, SF, SI | 4 | 2 |
| [R14](scenarios/R14/README.md) Dissatisfaction, incident and convenient settlement | control | complaints, risk, information | BR, SF, SI | 4 | 2 |
| [R15](scenarios/R15/README.md) Invoice entitlement, corrections and purpose boundaries | control | finance, audit, confidentiality | BR, SF, SI | 4 | 2 |
| [R16](scenarios/R16/README.md) Honest management measures and incomplete data | control | reporting, finance, open-work | BR, SF, SI | 4 | 2 |
| [R17](scenarios/R17/README.md) Rejected handoff and temporary measure review | control | handoffs, exceptions, temporary measures | BR, SF, SI | 4 | 2 |
| [U01](scenarios/U01/README.md) Receive an unclear call | usability | triage, contracts | IU | 2 | 0 |
| [U02](scenarios/U02/README.md) Report an unsuccessful mobile visit | usability | field, mobile | IU | 2 | 0 |
| [U03](scenarios/U03/README.md) Understand and continue a parts wait | usability | dispatch, parts | IU | 2 | 0 |
| [U04](scenarios/U04/README.md) Prepare an evidenced invoice | usability | finance, customers | IU | 2 | 0 |
| [U05](scenarios/U05/README.md) Handle a damaged delivery | usability | warehouse, procurement | IU | 2 | 0 |
| [U06](scenarios/U06/README.md) Clarify a quotation acceptance | usability | quoting, authority | IU | 2 | 0 |
| [U07](scenarios/U07/README.md) Record dissatisfaction and urgent concern | usability | complaints, safety | IU | 2 | 0 |
| [U08](scenarios/U08/README.md) Review open work for management | usability | reporting, exceptions | IU | 2 | 0 |
| [T01](scenarios/T01/README.md) Actual authentication and purpose-limited authorisation | technical | permissions, confidentiality | PT | 3 | 3 |
| [T02](scenarios/T02/README.md) Interrupted consequential action and recovery | technical | reliability, persistence, continuity | PT, SI | 3 | 2 |
| [T03](scenarios/T03/README.md) Dirty source data and unsafe content consequences | technical | data, security, history | PT | 3 | 2 |
| [T04](scenarios/T04/README.md) Delivered operability and accessible work | technical | deployment, accessibility, mobile | PT | 3 | 0 |
| [S01](scenarios/S01/README.md) Surface-wide semantic fidelity inventory | semantic | business identity, policy, workflows, defaults | SF | 6 | 2 |

Additional checkpoint totals: BR 34, IU 16, PT 11, SF 23, SI 18. Each assertion scores one dimension.

Critical coverage: **42 declared checkpoint predicates** covering unsafe/restricted dispatch, false completion/SLA evidence, unapproved commercial commitment/charge, stock custody/ownership, claim/compliance history destruction, untrusted-data disclosure/action and imposed material invented policy. One incident can trigger multiple predicates; incident count is not predicate count. See [critical inventory](hidden/critical-inventory.md).
