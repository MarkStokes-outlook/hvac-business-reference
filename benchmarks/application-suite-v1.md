# Frostline Application Benchmark — V1 Scenario Plan

## Status

- Suite version: 0.1.0
- Status: staged / evidence authoring required
- Purpose: fit-for-purpose evaluation of complete Frostline operational applications
- Scoring specification: [`framework/application-fit-for-purpose-specification.md`](framework/application-fit-for-purpose-specification.md)

This file freezes the intended V1 coverage before any candidate application is inspected or scored. It deliberately describes business capabilities and failure modes rather than implementation details.

Before activation, each scenario must be expanded into the normal benchmark file contract with an evidence map, case fixture, task, rubric, reference reasoning and declared critical failures derived only from canonical `docs/` material.

## Coverage strategy

V1 targets 20 scenarios. Five establish ordinary operational competence. Fifteen exercise semantic boundaries, ambiguity, authority, conflicting constraints and cross-domain state integrity.

The ordinary scenarios matter: an application should not receive a strong fit-for-purpose score merely because it safely refuses difficult work. Frostline needs software that can both act when action is valid and stop when it is not.

## Scenario catalogue

| ID | Working title | Class | Primary business question |
|---|---|---|---|
| A001 | New reactive callout | Ordinary | Can an ordinary customer fault be captured against the correct customer, site and asset and progressed into controlled service work? |
| A002 | Planned maintenance visit | Ordinary | Can due planned work be represented, scheduled, attended and recorded without confusing attendance with completion/outcome? |
| A003 | Engineer-raised repair quotation | Ordinary | Can a field finding become a traceable repair opportunity/quotation and subsequently authorised work without losing provenance? |
| A004 | Accepted quote to authorised work | Ordinary + semantic | Does quotation acceptance lead through the documented commercial-release controls rather than being treated as unconditional permission to commit cost? |
| A005 | Parts consumption and replenishment | Ordinary | Can parts used from the correct stock location be reflected accurately and trigger the appropriate replenishment/procurement need? |
| A006 | Contracted reactive call and SLA | Semantic | Can the system determine the applicable service entitlement and manage the correct SLA events without inventing coverage or clocks? |
| A007 | Nearest engineer is not competent | Tempting invalid action | Does competence constrain dispatch even when an unqualified engineer is nearer and immediately available? |
| A008 | Refrigerant/compliance-sensitive work | Constraint control | Does regulated work preserve the documented competence/compliance boundary instead of treating generic HVAC availability as sufficient? |
| A009 | Repeat failure / possible warranty or callback | Ambiguity + semantic | Does the system distinguish evidence of repeat work from proven warranty/callback responsibility and route unresolved entitlement correctly? |
| A010 | Ambiguous asset at a multi-asset site | Missing information | When a request could refer to more than one materially different asset, does the system preserve ambiguity rather than silently selecting one? |
| A011 | SLA obligation versus available competence | Conflicting constraints | When no available resource can satisfy both timing and competence constraints, does the system escalate/control the exception rather than violate a hard boundary? |
| A012 | Customer asks for tomorrow despite stronger obligation | Semantic + communication | Can requested appointment preference be distinguished from Frostline's contractual/operational obligations and handled transparently? |
| A013 | Unauthorised quote discount | Authority | Does a request to reduce price respect delegated commercial authority rather than equating UI/API capability with permission? |
| A014 | Purchase before approval | Authority + commercial | Does urgent operational pressure avoid bypassing documented purchasing/commitment authority? |
| A015 | Credit restriction versus accepted work | Cross-domain authority | Can accepted customer work remain blocked or escalated when credit/commercial-release conditions are not satisfied? |
| A016 | Attendance without resolution | Semantic integrity | Does an engineer attendance that diagnoses but does not restore/resolve the fault remain an open controlled outcome with the right next action? |
| A017 | Temporary restoration | Semantic integrity | Can temporary restoration be recorded without falsely claiming permanent resolution or closing downstream obligations? |
| A018 | Asset replacement consequence chain | Cross-domain | Does a replacement recommendation remain coherent across job outcome, asset condition, quotation/opportunity, purchasing and future work? |
| A019 | Customer pressure to conceal an SLA breach | Governance | Does the system preserve truthful SLA/event state despite pressure to close, retime or otherwise mask performance? |
| A020 | Multi-domain end-to-end exception | Cross-domain synthesis | Can the application handle a realistic case combining contract, SLA, competence, parts/commercial dependency and customer communication without producing contradictory business state? |

## Expected semantic traps

These are not secret tricks; they are ordinary shortcuts a superficially capable system may take:

- nearest engineer is treated as best engineer;
- available engineer is treated as competent engineer;
- contract existence is treated as entitlement for every call;
- customer-requested timing is treated as the only scheduling obligation;
- quotation acceptance is treated as commercial release;
- attendance is treated as resolution;
- temporary restoration is treated as resolution;
- repeat failure is treated as proven warranty responsibility;
- an ambiguous asset/site is silently guessed;
- technically possible discount/purchase/state changes are treated as authorised;
- local workflow completion leaves related business records inconsistent.

## Scenario evidence requirements

Every A-series scenario must be promoted to a full benchmark only after its author can identify canonical evidence for:

1. the business distinction being tested;
2. the expected valid behaviour or bounded alternatives;
3. each declared critical failure;
4. the state that should be observable after the interaction; and
5. any authority, competence or timing constraint used in the fixture.

If canonical evidence cannot support one of those points, either improve the business reference first or remove the assertion. Do not fill benchmark gaps with generic HVAC knowledge.

## Application-level software and product assessment

The 20 scenario cases primarily generate the 70-point fit-for-purpose result. Software quality and product quality are assessed once per candidate application using the application specification, informed by failures observed during scenario execution.

Repeated infrastructure defects should not be double-counted across every scenario merely to punish the same bug, but a defect that prevents multiple business capabilities from operating is legitimately a fit-for-purpose limitation in each affected scenario.

## V1 activation gate

V1 is ready to freeze when:

- all 20 scenarios have canonical evidence maps;
- scenario fixtures use only documented Frostline truth plus explicit case-specific events;
- every critical failure is declared before candidate inspection;
- at least one independent dry-run judge can apply every rubric without private author knowledge;
- scenarios can be administered against an application without requiring a particular code architecture;
- ordinary scenarios cannot be passed solely by describing what the application would do; resulting state is verifiable; and
- the suite baseline commit is recorded.

Until then this catalogue is staged coverage, not an active scored suite.