# Planned and Reactive Service

## Overview

Frostline's service operation combines scheduled maintenance with reactive fault response. The same engineers may perform both kinds of work, but the planning logic, customer expectations, authority and commercial treatment are different.

This document uses the record meanings in [Canonical terminology and record relationships](../governance/canonical-terminology-and-record-relationships.md), the authority rules in [Decision rights and operational authority](../governance/decision-rights-and-operational-authority.md), and the ownership controls in [Exceptions, handoffs and next-action control](../operations/exceptions-handoffs-and-next-action-control.md).

A **job** is the operational container. An **attendance** is one intervention against that job. Completing an attendance does not automatically complete the job, resolve the customer issue or settle its financial treatment.

## Planned maintenance

Planned preventive maintenance is delivered against agreed schedules. Its purpose is to keep equipment safe, reliable, efficient and compliant with applicable requirements while identifying deterioration before failure.

A planned attendance may include:

- visual inspection;
- cleaning and routine servicing;
- filter, belt or consumable attention;
- operational testing;
- temperature, pressure or electrical readings;
- leak checking where applicable;
- controls and set-point checks;
- identification of defects;
- review of access and equipment condition; and
- completion of service evidence.

The exact tasks depend on equipment type, manufacturer guidance, legal obligations, contract scope and engineering judgement. Contract inclusion does not permit work outside competence, safe method or the authorised maintenance scope.

## Maintenance obligations and schedules

Maintenance can be scheduled annually, six-monthly, quarterly or at another agreed frequency. Different assets at the same site may require different frequencies, task sets or evidence.

The company distinguishes:

- contractual maintenance obligations;
- statutory or certification-related activities;
- manufacturer-recommended maintenance;
- customer-requested additional tasks; and
- advisory activities that are not part of the current contract.

Coordinators try to group work efficiently by site and geography without allowing contractual dates to drift. School holidays, retail peaks, hospitality occupancy, tenant access and plant shutdown windows can constrain attendance.

A missed attendance does not disappear. The associated obligation remains active until it is completed, formally rescheduled, varied, cancelled under authority or recorded as no longer recoverable with the consequences understood. Where a contract defines SLA targets for maintenance delivery (such as completing all quarterly visits within the quarter), the missed-maintenance obligation and any resulting SLA breach are recorded against the contractual period in which they were due, not the period in which they are eventually completed.

## Maintenance completion states

A maintenance attendance may be:

- complete;
- partially complete;
- unable to complete because of access;
- unable to complete because of safety;
- unable to complete because the asset or system could not be identified;
- unable to complete because prerequisite customer action was absent; or
- complete with defects or recommendations requiring separate follow-on action.

The maintenance job or contractual obligation must not be marked complete merely because an engineer attended site. Completion requires the authorised task set and evidence, or an explicit exception decision.

## Defects found during maintenance

Engineers distinguish between maintenance completed within the authorised attendance and defects requiring further action.

A defect may lead to:

- an immediate minor repair within both customer and Frostline authority;
- make-safe action;
- isolation for safety;
- a return attendance under existing authority;
- a repair quotation;
- a replacement recommendation;
- specialist investigation;
- a suspected warranty case; or
- monitored deterioration with an agreed review point.

Finding a defect is not authority to repair it. The engineer records the condition, consequence, evidence, technical recommendation and immediate safety status. Operations then establishes whether the next action is already covered, separately chargeable, subject to quotation or dependent on another party.

Vague notes such as "unit faulty" are not sufficient when a technical, safety or commercial decision is required.

## Reactive requests

Reactive work begins when a customer reports a fault, loss of service, alarm, leak, unusual noise, comfort complaint or other operational problem.

The initial report may be inaccurate or incomplete. A customer may describe an entire system as failed when one zone is affected, or report an air-conditioning fault that is actually caused by controls, power supply or building conditions.

The incoming request should distinguish:

- who is reporting the issue;
- whether that person can authorise attendance or expenditure;
- affected site, service location, system and asset where known;
- symptom and operational impact;
- immediate safety, environmental or property risk;
- when the issue began;
- actions already taken;
- access availability; and
- applicable contract or charging basis.

Coordinators gather enough information to triage response. Engineers remain responsible for diagnosis within their competence.

## Priority and urgency

Frostline considers several factors when prioritising reactive work:

- risk to people or property;
- complete or partial loss of critical service;
- site type and operating hours;
- vulnerable occupants;
- food, stock, process or technology risk;
- contractual response commitment;
- availability of safe temporary measures;
- customer relationship;
- engineer travel and capability; and
- the effect of displacing already-promised work.

Priority is a decision, not simply a label supplied by the requester. It is not determined only by who calls most loudly. A loss of cooling in a server room or refrigeration failure may outrank a comfort complaint even when the latter customer is more persistent.

Where reprioritisation threatens another contractual commitment, the displaced work receives its own owner, communication and recovery plan.

## Response commitments

Some maintenance contracts include target acknowledgement, remote response, attendance or restoration times. These events must not be collapsed into one generic SLA status.

A response commitment usually relates to a defined milestone, not guaranteed permanent repair. Resolution can depend on diagnosis, parts lead time, specialist access, customer approval, manufacturer response and equipment availability.

The job record should therefore identify:

- the applicable response target;
- the event that starts the clock;
- coverage hours and exclusions;
- the event that stops or satisfies the clock;
- pauses or dependencies permitted by contract;
- actual response evidence; and
- any breach, reason and recovery action.

## Attendance authority

Before dispatch, Frostline establishes the authority relied upon for the attendance. This may be:

- an included contract entitlement;
- an agreed call-out or diagnostic rate;
- a customer purchase order;
- an accepted quotation;
- a pre-agreed spending limit;
- an internal customer-care or warranty-investigation decision; or
- emergency make-safe authority.

Authority to diagnose does not automatically include authority to repair, order parts, work overtime or appoint a specialist.

Where customer authority cannot be confirmed but immediate risk exists, action is limited to what is reasonably necessary to make safe or prevent escalation, with the decision and follow-up recorded.

## Diagnosis and technical escalation

Reactive attendance aims to establish the verified cause or the next justified test, not merely to clear an alarm or replace the component most commonly associated with a fault code.

Engineers use equipment history, readings, controls state, environmental conditions and manufacturer information. Where evidence is insufficient or the issue exceeds competence, they escalate through the route defined in [Diagnostics, controls and technical escalation](../technical-support/diagnostics-controls-and-technical-escalation.md).

The technical conclusion should distinguish:

- observed facts;
- tests performed;
- verified cause;
- likely but unconfirmed cause;
- temporary restoration;
- permanent recommendation; and
- remaining uncertainty.

## First-time fix

A first-time fix is desirable but not always realistic. It is more likely when:

- the fault description is accurate;
- asset information is available;
- the engineer has the right skills;
- common parts are held in van stock;
- access is available;
- the repair is within scope and competence; and
- both customer and Frostline commercial authority exist.

For reporting, first-time fix means that the suitable reactive issue was durably restored or resolved during the first attendance without an unplanned further engineering attendance. It excludes cases where return work was always planned, where investigation was the authorised scope, or where no safe and justified repair could reasonably be expected.

Engineers must not fit speculative parts merely to improve the measure.

## Parts and return attendances

Where parts are required, the engineer or coordinator provides enough evidence for procurement to identify the correct item. This may include photographs, model and serial details, verified part numbers, dimensions and technical discussion with the supplier or manufacturer.

A return attendance continues authorised work only where the remaining scope and commercial basis are clear. Otherwise the finding creates follow-on work requiring separate authority.

A return attendance should not be booked until the necessary dependencies are understood. Having the part in the depot is not enough if lifting access, isolation, another trade, customer shutdown approval or specialist competence is also required.

The waiting state should identify the exact dependency, expected actor, owner of the chase and review date.

## Temporary measures and make-safe work

Out-of-hours and urgent service often produces temporary measures rather than permanent repair. Examples include isolation, controlled manual operation, limited operation, temporary heating or cooling and protection against further leakage or damage.

The record must state:

- what was made safe or temporarily restored;
- what remains unavailable or at risk;
- operating limitations;
- who authorised the measure;
- customer understanding;
- inspection or expiry point; and
- owner of permanent resolution.

A make-safe attendance is not a completed repair. A temporary measure without a future trigger is an unmanaged permanent condition.

## Out-of-hours service

Out-of-hours support is primarily available to contracted customers and is delivered through an engineer rota backed by management escalation.

The on-call engineer may provide telephone advice, attend site or determine that a safe temporary measure is appropriate until normal hours. The on-call engineer controls local safety and technical activity but does not have unlimited authority to commit replacement equipment, extended labour or subcontract cost.

Where entitlement is uncertain, the engineer records the basis on which action was taken and routes commercial review to the next available owner.

## Suspected warranty service

A report concerning recently supplied, installed or repaired equipment creates a suspected warranty case, not an automatic free job.

Frostline follows [Warranty responsibility and remedial work](../warranty/warranty-responsibility-and-remedial-work.md) to separate immediate customer support from technical cause, contractual responsibility and financial recovery.

The remedial attendance may be operationally complete while manufacturer recovery, subcontract responsibility or customer charging remains unresolved. These are linked records with separate owners and closure criteria.

## Customer communication

Customers value updates almost as much as attendance. Coordinators communicate:

- acknowledgement and assessed priority;
- the applicable response commitment;
- expected attendance;
- delays or changes;
- engineer findings at an appropriate level of confidence;
- immediate safety and operating status;
- temporary limitations;
- parts, evidence or approval requirements;
- current commercial position where known; and
- next action, owner and review point.

Communication is especially important when a job is waiting. "Open" is not a useful customer explanation. Frostline states what is being awaited, what it is doing next and when the position will be reviewed.

## Job and issue closure

A reactive attendance can close when its assigned activity and evidence are complete. The job closes only when the authorised operational scope is complete or has been deliberately cancelled, transferred or superseded.

The wider customer issue may remain unresolved after job closure, for example where:

- replacement has been recommended but not approved;
- another contractor owns the root cause;
- a manufacturer investigation remains open;
- the customer chooses to operate with a known limitation; or
- financial responsibility remains disputed.

Closure must preserve those residual actions rather than bury them in engineer notes.

## Service performance

Frostline monitors service performance through a mixture of formal measures and management judgement. Useful indicators include:

- maintenance obligations completed when due;
- reactive acknowledgement and attendance performance;
- jobs by explicit waiting reason and owner;
- repeat attendances;
- first-time fix where meaningful;
- temporary measures overdue for review;
- quotation turnaround;
- customer complaints;
- engineer utilisation; and
- contract profitability.

No single measure defines good service. Fast attendance with poor diagnosis is not success, and high utilisation can hide an overloaded team with no capacity for urgent work.