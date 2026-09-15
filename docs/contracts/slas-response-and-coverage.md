# SLAs, Response and Coverage

## Purpose

Service-level agreements define measurable service commitments, operating boundaries and communication duties. They align customer expectations with a service model Frostline can realistically resource and control.

An SLA does not replace the underlying contract, technical judgement or safety obligations. It describes what Frostline has committed to measure and manage under defined conditions.

This document uses the work and attendance meanings in [Canonical terminology and record relationships](../governance/canonical-terminology-and-record-relationships.md), the authority distinctions in [Decision rights and operational authority](../governance/decision-rights-and-operational-authority.md), and the exception controls in [Exceptions, handoffs and next-action control](../operations/exceptions-handoffs-and-next-action-control.md).

## Core terminology

SLA events are distinct:

- **Request received** — the agreed service channel has received sufficient information to create a work request.
- **Acknowledgement** — Frostline confirms receipt and provides a reference or ownership route.
- **Initial response** — first meaningful human or agreed automated response, potentially including remote triage.
- **Attendance dispatched** — a suitable engineer has been released to travel; this is not arrival.
- **Attendance** — a suitable engineer reaches the agreed service location and is reasonably able to begin the intended intervention.
- **Diagnosis** — a supported technical conclusion or defined investigation outcome.
- **Restoration** — return of an agreed minimum service level, including an authorised temporary measure where applicable.
- **Resolution** — completion of the agreed remedial outcome, not merely attendance or temporary restoration.
- **Closure** — operational, evidential and commercial actions are sufficiently complete for the relevant record.
- **Clock stop** — a contractually permitted exclusion of elapsed time because a defined dependency prevents progress.

These events must not be collapsed into one “completed” timestamp.

## Contract hierarchy

Where SLA wording conflicts with the signed contract, accepted quotation, schedule of service or formally agreed variation, the applicable contractual hierarchy is reviewed rather than silently selecting the most convenient interpretation.

Operational teams should know:

- which document defines the target;
- which customer, sites and assets are covered;
- effective dates and renewal position;
- coverage hours;
- exclusions;
- service-credit rules; and
- who can approve a change.

Informal promises by an engineer or coordinator do not amend an SLA unless made by an authorised person and properly recorded.

## Priority and severity

Priority reflects current impact and required response, not customer seniority or volume of chasing.

A typical model is:

### Priority 1 — critical

Immediate or severe risk to people, property, critical stock, essential operation or environmental control, with no adequate workaround.

### Priority 2 — high

Major operational degradation or substantial loss of service where impact is serious but not presently at Priority 1 severity.

### Priority 3 — normal

Partial failure, comfort issue or non-critical defect where the customer remains broadly operational.

### Priority 4 — planned

Minor defect, advisory work or activity suitable for normal scheduling.

Priority is provisional until enough facts exist and may move up or down. The reason, evidence, time and decision-maker for a material reclassification are recorded.

## Impact assessment

Assessment considers:

- immediate safety and property risk;
- total or partial service loss;
- critical areas, processes or occupants;
- backup plant and redundancy;
- food, medicine, stock or data exposure;
- weather and expected duration;
- operating hours and business continuity;
- temporary measures already in place; and
- contractual criticality designations.

The same failed asset can produce different priorities at different sites.

## Coverage hours

The agreement states:

- time zone;
- covered days and hours;
- public-holiday treatment;
- seasonal arrangements;
- whether clocks run continuously or only in covered time;
- service channels valid out of hours; and
- whether remote response and attendance have different coverage.

A four-working-hour target is materially different from four elapsed hours. Reporting preserves that distinction.

## Request channels and clock start

The SLA identifies which channels start a response clock. Examples include a service desk number, monitored mailbox, customer portal or agreed alarm integration.

Messages to an individual engineer, account manager or unmonitored mailbox may not start the clock unless the contract expressly says so.

Where the initial request lacks basic information, Frostline records what was received and whether the clock begins immediately, begins after clarification or runs while triage continues. This treatment must follow the contract rather than being invented after a breach.

## Geographic coverage

Targets reflect realistic travel, engineer distribution, site access and competence. Geographic zones may have different commitments.

Attendance risk is affected by:

- travel from actual engineer locations;
- congestion and road closures;
- parking and security;
- rural or remote access;
- weather;
- specialist competence availability; and
- whether travel occurs inside or outside normal hours.

The company avoids selling response commitments based only on depot-to-postcode distance.

## Remote triage

Remote triage may satisfy an initial-response target where the SLA permits it. It can gather evidence, reduce risk and determine whether attendance is required.

Remote triage may include controls review, alarm confirmation, safe basic checks, photographs, system history and impact clarification.

It must not instruct unqualified site contacts to remove covers, bypass protections, handle refrigerants, work live or undertake another hazardous action.

## Attendance targets

An attendance target defines:

- start event;
- target duration;
- priority;
- coverage calendar;
- geographic scope;
- required engineer suitability;
- permitted clock stops;
- evidence of arrival; and
- treatment of no access or incorrect site information.

A person reaching the car park does not necessarily constitute meaningful attendance where the agreed service location remains inaccessible. Equally, customer delay after a documented arrival may trigger a permitted clock stop.

## Restoration and resolution

Restoration is defined in customer-relevant terms, such as minimum temperature control, operation of one duty unit, safe restricted use or temporary equipment.

A temporary restoration records:

- achieved service level;
- operating limits;
- residual risk;
- expiry or review trigger;
- customer understanding; and
- owner of permanent resolution.

Resolution targets are used only where Frostline can reasonably control the dependencies. Where parts, third parties or customer decisions dominate elapsed time, the contract may instead require diagnosis, action planning, escalation and scheduled updates.

## Clock stops

A clock stop is permitted only where the contract allows it and the dependency genuinely prevents the measured action.

Common reasons include:

- no access;
- absent permit or induction;
- customer-directed delay;
- waiting for customer authority;
- unsafe conditions outside Frostline's control;
- unavailable utilities;
- third-party work;
- specialist access arrangements;
- manufacturer decision; or
- part availability.

The record includes reason, start time, evidence, expected actor, Frostline owner, chase or review point and restart event.

Clock stops must not be added retrospectively merely to improve attainment.

## Parts and external dependencies

After diagnosis, Frostline communicates:

- required item or intervention;
- whether identification is confirmed;
- whether availability is confirmed;
- expected date and confidence;
- alternative or temporary options;
- continued-operation risk;
- commercial authority needed; and
- next update time.

“Awaiting parts” without a confirmed owner and review point is not controlled SLA management.

## Subcontractor and third-party dependencies

Where resolution depends on a subcontractor or specialist trade, Frostline remains accountable to the customer for SLA targets unless the contract explicitly transfers that accountability. The relevant Frostline manager monitors subcontractor progress, escalates delay and arranges alternatives where the subcontractor's programme threatens a contracted target.

Clock stops may apply where the contract permits them for defined third-party dependencies, but cannot be claimed merely because Frostline chose to use a subcontractor rather than completing the work directly.

## Escalation

Escalation increases decision authority, expertise or operational attention. It may involve service coordination, management, senior engineering, manufacturers, suppliers, subcontractors and the customer's contract owner.

Escalation criteria may include:

- likely or actual target breach;
- worsening safety or business impact;
- failed temporary measure;
- repeated attendance;
- disputed priority;
- uncertain technical path;
- unavailable competence; or
- customer dissatisfaction despite nominal target achievement.

Escalation is an action, not a label. The record states who is now expected to decide or act.

## Communication commitments

For significant incidents, updates occur at the agreed interval even when there is no material technical change.

A useful update states:

- current impact and safety condition;
- latest verified finding;
- what remains uncertain;
- restoration status;
- dependency and owner;
- next action; and
- next update time.

An update saying only “still chasing” provides little control value unless it identifies what is being chased and what happens next.

## Out-of-hours coverage

Out-of-hours coverage is delivered through a defined rota and escalation route. The on-call engineer may triage remotely, attend, make safe or establish temporary restoration.

Out-of-hours capability may be constrained by supplier opening, specialist support, access equipment and available backup. Contracts should distinguish guaranteed response from guaranteed permanent repair.

## Critical equipment and site registers

Where applicable, the contract maintains criticality information including:

- site, service location, system and asset;
- supported function;
- consequence of failure;
- redundancy or backup;
- priority rule;
- escalation contacts;
- access and shutdown restrictions;
- recovery actions; and
- review date.

Criticality is reviewed after asset replacement, building-use change or repeated incident experience.

## Exclusions and events outside reasonable control

Exclusions may cover extreme weather, civil emergency, major infrastructure failure, denied access or other events defined by contract.

An exclusion does not remove the duty to communicate, preserve safety, mitigate where practical and resume activity when conditions allow.

## Performance measurement

Reporting may include:

- acknowledgement attainment;
- initial-response attainment;
- attendance attainment;
- restoration attainment;
- resolution attainment where applicable;
- breaches by priority and cause;
- clock-stop frequency and duration;
- priority changes;
- update compliance;
- repeat incidents; and
- unresolved incidents by age and dependency.

Every measure states denominator, exclusions, time basis and source event. Averages are supplemented by percentiles, breach counts and significant-case narrative.

## Service credits

Service credits apply only where contract conditions are met. Credit calculation, caps, exclusions, evidence and approval are kept separate from the technical incident record.

A credit does not automatically establish negligence or full liability. Equally, a low-value credit does not remove the need to investigate recurring service failure.

Where an attendance occurs outside normal hours and attracts premium rates, the contract determines whether different response targets apply and whether those targets affect credit eligibility. The mere fact that Frostline chose to attend out of hours to meet a target does not alter the credit calculation unless the contract specifies otherwise.

## Review and change control

SLA reviews examine demand, attainment, clock stops, recurring faults, critical assets, access failures, capacity, customer behaviour and contract economics.

Where the service model no longer matches reality, Frostline seeks an explicit contract change rather than normalising recurring breach or manipulating classifications.

## Operating reality

SLA performance depends on disciplined event capture. A business can appear compliant or non-compliant simply because different people record “response”, “attendance” or “resolution” differently.

Frostline therefore treats definitions, timestamps, evidence and exception ownership as part of service delivery itself—not as reporting decoration added at month end.
