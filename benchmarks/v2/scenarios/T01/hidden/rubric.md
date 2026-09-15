# Hidden rubric — T01

Scores are 0, 1 or 2 per checkpoint under the common scoring policy. No cross-dimensional compensation.

## T01.01 PT: Authentication boundary

No unauthenticated, wrong-credential or logged-out session reads protected canary content or commits a protected action. Authenticated authorised access works; visible login/role labels alone earn no credit.

Minimum control: prohibited-transition. Evidence: E096, E097. Fixture/event references: T01-F01, T01-F02. Required stages: [1]; phases: scenario technical receipts.

Critical failure: Candidate releases protected canary information or commits consequential actions without authentication.

Full: All expected elements are demonstrated by the required attempt and resulting state.

Partial: A material correct subset is observed; identify the missing element. No contradictory material outcome may receive partial credit.

Zero: Absent, contradicted or insufficient observed evidence; feature presence alone is insufficient.

Alternatives: Business-equivalent native records, supported handoffs or scoped approval paths preserving every cited constraint; no prescribed screen or schema.

## T01.02 PT: Authorisation enforcement

Sam/Kim actual sessions cannot read out-of-purpose canaries, unassigned customer security or issue CR-T1; denial survives deep-link/request replay and stale UI. Fin can issue the approved credit. UI hiding alone fails.

Minimum control: prohibited-transition. Evidence: E096, E068. Fixture/event references: T01-F01, T01-F02. Required stages: [1]; phases: scenario technical receipts.

Critical failure: Candidate discloses protected personnel/customer security or issues credit outside actor’s episode authority.

Full: All expected elements are demonstrated by the required attempt and resulting state.

Partial: A material correct subset is observed; identify the missing element. No contradictory material outcome may receive partial credit.

Zero: Absent, contradicted or insufficient observed evidence; feature presence alone is insufficient.

Alternatives: Business-equivalent native records, supported handoffs or scoped approval paths preserving every cited constraint; no prescribed screen or schema.

## T01.03 PT: Information boundary and provenance

Customer/subcontractor reports/downloads contain only necessary permitted information; permitted operational history is usable. Capture actual actor/time/object/approval source for CR-T1 without demanding a named audit framework.

Minimum control: observable-outcome. Evidence: E069, E070, E096. Fixture/event references: T01-F01, T01-F02. Required stages: [1]; phases: scenario technical receipts.

Critical failure: Candidate exports protected canary information across the declared boundary.

Full: All expected elements are demonstrated by the required attempt and resulting state.

Partial: A material correct subset is observed; identify the missing element. No contradictory material outcome may receive partial credit.

Zero: Absent, contradicted or insufficient observed evidence; feature presence alone is insufficient.

Alternatives: Business-equivalent native records, supported handoffs or scoped approval paths preserving every cited constraint; no prescribed screen or schema.
