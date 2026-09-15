# Exceptions, Handoffs and Next-Action Control

## Purpose

Frostline's most persistent operational failures rarely come from a total absence of activity. They arise when work is partially progressed, ownership becomes ambiguous and every participant believes somebody else is acting.

This document defines how the company controls exceptions, handoffs and waiting states across service, projects, purchasing, finance and customer communication. It uses the record meanings in [Canonical terminology and record relationships](../governance/canonical-terminology-and-record-relationships.md) and the authority distinctions in [Decision rights and operational authority](../governance/decision-rights-and-operational-authority.md).

## The next-action principle

Every active job, project issue, quotation, purchase requirement, warranty case, complaint or invoice dispute should have:

- one current state;
- one clearly described next material action;
- one accountable owner for that action;
- a due date or review trigger;
- the dependency preventing immediate progress, where applicable; and
- an escalation route if the action cannot be completed.

A list of people copied into a message is not ownership. A generic team queue is useful for intake, but an ageing exception must eventually have a named accountable owner or a deliberately assigned duty role.

## Normal flow and exception flow

Normal flow is work proceeding under expected scope, evidence, authority and timing.

Exception flow begins when an event invalidates an assumption or prevents the next planned step. Typical triggers include:

- no site access;
- unsafe conditions;
- inaccurate asset information;
- diagnosis differing from the quoted scope;
- missing parts or supplier delay;
- engineer competence mismatch;
- customer approval not received;
- purchase order value or scope mismatch;
- subcontractor non-performance;
- failed commissioning;
- repeat fault;
- disputed invoice;
- warranty responsibility uncertainty; or
- incomplete field evidence.

An exception is not necessarily a failure. It becomes a control failure when it is not made visible, owned and driven to a decision.

## Required exception record

A material exception should state:

- what was expected;
- what actually occurred;
- operational and customer impact;
- immediate safety or asset condition;
- evidence available;
- work completed so far;
- work not completed;
- decision or information required;
- owner of the next action;
- target date or review trigger; and
- parties who must be informed.

The record should distinguish fact, engineer judgement, customer statement and unresolved assumption.

## Waiting states

“Waiting” is incomplete without the object and owner of the wait.

Preferred states include:

- waiting for customer approval;
- waiting for purchase order correction;
- waiting for supplier acknowledgement;
- waiting for part availability date;
- waiting for manufacturer warranty decision;
- waiting for site access confirmation;
- waiting for engineer evidence;
- waiting for technical review; and
- waiting for finance decision.

Each waiting state should identify who is expected to act and when Frostline will chase, review or escalate. Waiting indefinitely is not a valid operational strategy.

## Handoffs

A handoff transfers responsibility for the next action, not merely information.

A complete handoff identifies:

- the receiving owner;
- the outcome required;
- relevant deadline or urgency;
- decisions already made;
- authority already obtained;
- unresolved questions;
- customer commitments made;
- documents and evidence available; and
- what will happen if the receiver does not accept the handoff.

The sender retains responsibility until the receiving person or duty role has accepted the handoff, either explicitly or through a defined operating rule.

## Common handoff boundaries

### Sales or estimating to operations

The handoff should include accepted scope, price basis, assumptions, exclusions, promised dates, customer responsibilities, survey evidence, equipment selections and any unresolved qualifications.

Operations should not discover after mobilisation that a key dependency was merely assumed.

### Service coordination to engineer

The engineer should receive the reported problem, customer priority, site and asset information, contract status, access arrangements, known hazards, previous relevant history and commercial limits.

A diary entry containing only a postcode and “unit not working” is not an adequate handoff.

### Engineer to office

The engineer should record condition found, diagnosis, work performed, parts used, readings, safety status, customer discussion, completion state and precise follow-on need.

“Needs parts” must identify which parts, the basis for identification, whether the asset is safe to operate and whether further diagnosis is still required.

### Operations to purchasing

The request should identify job or project, required item or service, specification, quantity, delivery location, required date, approved supplier constraints, budget or authority and consequence of delay.

Purchasing should not be expected to infer technical equivalence from an informal description.

### Operations to finance

The handoff should provide delivery evidence, agreed charging basis, variations, customer purchase order, disputed items and any reason invoicing should be held.

Finance should not need to reconstruct commercial scope from fragmented emails.

### Complaint owner to operational teams

The complaint owner defines the response commitment, evidence needed and service-recovery decision route. Operational contributors provide facts and corrective actions without sending uncoordinated explanations directly to the customer.

## Rejection of a handoff

A receiver may reject a handoff where:

- essential information is missing;
- the requested action is outside their role or competence;
- authority is absent;
- the deadline is impossible without reprioritisation;
- the request conflicts with another commitment; or
- the handoff would create an unmanaged safety or commercial risk.

Rejection must be prompt and explicit. Quietly leaving the item untouched is not rejection; it is loss of control.

## Ageing and escalation

Exceptions are reviewed by age, impact and risk rather than age alone.

Examples requiring earlier escalation include:

- equipment left unsafe or unavailable;
- critical customer operations affected;
- temporary controls approaching their review date;
- high-value materials ordered without final scope certainty;
- repeated failed attendances;
- contractual response or completion deadlines at risk;
- customer silence blocking essential safety work; and
- disputed responsibility causing cost to accumulate.

Low-value administrative items may tolerate longer review cycles, but they still require closure or deliberate cancellation.

## Temporary measures

Temporary repairs, overrides, loan equipment and partial-service arrangements create a mandatory future action.

The record should state:

- what temporary measure was introduced;
- why it was necessary;
- operational limits;
- residual risk;
- who approved it;
- customer understanding;
- inspection or expiry date; and
- permanent resolution owner.

A temporary measure without an expiry or review trigger is an undocumented permanent change waiting to cause trouble.

## Failed attendance review

Not every incomplete attendance warrants management review, but repeated or avoidable failure does.

Review considers whether the cause was:

- inadequate triage;
- poor asset information;
- missing access arrangements;
- incorrect skill allocation;
- parts not identified or reserved;
- unrealistic duration;
- customer unavailability;
- unsafe site conditions;
- defective supplier information; or
- an unavoidable technical discovery.

The purpose is to improve planning and decision quality, not to punish engineers for discovering reality.

## Cancellation and abandonment

Work may be cancelled by the customer, Frostline or another authorised party. Cancellation should record commercial consequences, materials already committed, site condition, outstanding safety issues and whether any records or recommendations remain active.

Frostline may close an item as no longer pursued only after making the reason explicit. “No response” should state what contact attempts were made, what warning was given and whether the underlying risk was transferred back to the customer.

## Closure criteria

An exception can be closed when:

- the required action is complete;
- a competent authority has made the necessary decision;
- responsibility has been transferred and accepted;
- the item has been cancelled with consequences recorded; or
- no further action is justified and the rationale is documented.

Closure should not be used merely to remove an ageing item from view.

## Management information

Useful exception measures include:

- open exceptions by reason and owner;
- age since last meaningful action;
- jobs waiting for customer authority;
- jobs waiting for parts without a confirmed date;
- repeat attendances;
- temporary repairs overdue for review;
- engineer reports awaiting clarification;
- uninvoiced completed work;
- disputed invoices awaiting operational evidence; and
- exceptions reopened after apparent closure.

Counts alone can mislead. A small number of high-risk unmanaged exceptions matters more than a large number of routine parts waits with confirmed delivery dates.

## Operating reality

Frostline relies heavily on experienced coordinators and managers who remember promises, chase suppliers and notice when something feels stuck. That human awareness is valuable, but it is vulnerable to absence, workload and fragmented communication.

The company therefore treats explicit next-action ownership as an operating control, not clerical tidiness. The question is not simply “Is the job open?” It is “What happens next, who owns it, and what will make us notice if it does not happen?”