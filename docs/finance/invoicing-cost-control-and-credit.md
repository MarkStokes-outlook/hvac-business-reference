# Invoicing, Cost Control and Credit

## Purpose

Frostline's financial administration connects quoted work, delivered work, supplier cost, labour, customer approval and cash collection. The finance team cannot determine every invoice from accounting records alone; operational evidence and commercial context are often required.

This document uses the record meanings in [Canonical terminology and record relationships](../governance/canonical-terminology-and-record-relationships.md), the authority rules in [Decision rights and operational authority](../governance/decision-rights-and-operational-authority.md), and the exception controls in [Exceptions, handoffs and next-action control](../operations/exceptions-handoffs-and-next-action-control.md).

Finance confirms financial treatment. It does not retrospectively invent technical completion, customer authority or warranty responsibility where the operational evidence does not support them.

## Financial record boundaries

Frostline distinguishes:

- customer account;
- contracting legal entity;
- site and operational contact;
- quotation or contract;
- customer purchase order;
- job or project;
- attendance;
- supplier purchase order;
- supplier invoice;
- customer invoice;
- credit note;
- warranty claim or recovery; and
- payment.

These records may be linked many-to-many. One customer invoice may cover several jobs. One job may use several supplier invoices. One warranty recovery may relate to a failed component originally purchased for a project and replaced on a later remedial job.

Using one reference field to stand in for all of these relationships creates fragile accounting and poor auditability.

## Customer accounts

A customer account represents the continuing commercial relationship, but the legal entity expected to pay may differ from the site owner, occupier, facilities manager or person who requested attendance.

Accounts may contain:

- legal and trading names;
- company registration and VAT details;
- billing addresses;
- accounts-payable contacts;
- purchase-order and portal requirements;
- cost-centre or site coding;
- credit limit and risk status;
- payment terms;
- disputed or overdue balances; and
- restrictions on who may authorise work.

Multi-site customers may require invoices split or routed differently by site, region, contract or cost centre.

A familiar brand name is not sufficient evidence of the contracting entity.

## Credit approval and exposure

New customers and material increases in exposure may require credit checks, deposits, pro-forma payment or director approval.

Credit exposure includes more than issued invoices. Frostline considers:

- overdue and not-yet-due debt;
- uninvoiced completed work;
- work in progress;
- committed materials and subcontract cost;
- accepted but not yet started work;
- retention;
- disputed value;
- pending credits; and
- obligations that cannot readily be cancelled.

A customer can appear within its credit limit while Frostline has substantial unbilled commitment. Significant release decisions therefore use current and forecast exposure, not ledger balance alone.

## Customer authority and purchase orders

Many customers require a purchase order or other reference before invoicing. The absence of that reference does not always mean Frostline lacked authority to attend, particularly for emergency work, but it can delay or prevent payment.

Staff distinguish between:

- authority to investigate;
- authority to incur a limited call-out charge;
- authority to perform a repair;
- authority to order specified parts;
- authority to proceed up to a spending limit;
- authority to undertake a replacement or project; and
- authority to vary an existing scope.

These permissions may come from different people and have different financial limits.

A purchase-order number quoted in an email is validated against:

- customer entity;
- supplier name;
- scope description;
- value and currency;
- site or project;
- VAT treatment where relevant;
- expiry or release conditions; and
- whether the issuer had authority.

A purchase order does not automatically override Frostline's quotation, accept unreviewed customer terms or authorise work outside the stated value.

## Commercial release

Customer acceptance is necessary but may not be sufficient for Frostline to commit cost.

Before significant procurement or mobilisation, the appropriate owner confirms:

- accepted scope and revision;
- valid customer authority;
- credit or deposit position;
- Frostline delegated approval;
- expected margin and risk;
- supplier or subcontract commitment required;
- invoicing route and evidence requirements; and
- material conditions still outstanding.

Release may be limited to a defined purchase, survey, mobilisation stage or value. Conditional release is recorded with the condition, owner and review point.

## Invoice triggers

Invoices may be raised on:

- completion of a chargeable attendance;
- completion of an approved repair;
- delivery of a maintenance period or scheduled attendance group;
- delivery of equipment or materials where contractually agreed;
- project deposit or milestone;
- application for payment;
- practical completion;
- approved variation;
- cancellation or aborted attendance under agreed terms; or
- another defined contractual event.

The invoice trigger must identify both the commercial entitlement and the evidence that the event occurred.

Completion in the engineer diary is not automatically sufficient. Finance may require:

- accepted quotation, contract or rate basis;
- customer purchase order or recorded exception;
- attendance and labour evidence;
- materials and subcontract detail;
- completion or commissioning evidence;
- variation approval;
- customer acknowledgement where required; and
- manager review of unusual or disputed treatment.

## Operational completion and financial closure

Frostline distinguishes:

- attendance complete;
- authorised job scope complete;
- project practically complete;
- customer issue resolved;
- invoiceable event achieved;
- invoice issued;
- invoice paid;
- cost and recovery finalised; and
- job or project financially closed.

These states may occur at different times. A job may be operationally complete but held from invoicing because authority or evidence is incomplete. A staged project invoice may be issued before practical completion. A warranty repair may be complete while manufacturer recovery remains outstanding.

No single generic "closed" status should conceal those differences.

## Reactive and service invoicing

Reactive work commonly combines call-out, labour, travel, parts, access equipment and subcontract cost. Contract cover may remove, cap or alter some charges.

A single reported fault can create several attendances, purchases and decisions. Frostline may:

- invoice the diagnostic attendance separately;
- invoice authorised temporary or make-safe work;
- quote follow-on repair;
- invoice each stage under schedule-of-rates terms;
- consolidate after resolution; or
- hold customer charging pending a suspected warranty decision.

The chosen treatment follows the contract, authority and customer communication. It must not be inferred solely from the job description.

Maintenance contracts may be billed annually, quarterly, monthly or against visit completion. Billing timing does not necessarily match the physical delivery pattern. Deferred or missed maintenance obligations remain visible even where periodic billing has already occurred.

## Project invoicing

Installation projects may use deposits, staged invoices, applications for payment, completion invoices and retention. The commercial basis is inherited from the accepted quotation or contract and any approved variations.

Frostline distinguishes:

- value applied for;
- value assessed or certified;
- value invoiced;
- value paid;
- retention withheld;
- variations pending approval;
- contra-charges or deductions; and
- final account position.

The difference between applied, certified, invoiced and paid values remains visible until resolved.

Where retention is withheld pending a defects or warranty period, the retention release is a distinct financial event from warranty-case closure. Retention may be released once the contractual defects period expires without outstanding notified defects, even if a separate warranty recovery against a manufacturer remains in progress. Conversely, a warranty case closed in Frostline's favour does not automatically trigger retention release if other contractual conditions remain unsatisfied. Each record has its own owner and review date.

Variations need enough contemporaneous evidence to support entitlement and value. Work performed without timely commercial notice may be technically valid but difficult to recover.

A disputed valuation is an active exception with an owner, evidence requirement, next action and escalation point.

## Job and project cost

Frostline assesses work using relevant combinations of:

- direct labour hours;
- overtime or out-of-hours premium;
- equipment and materials;
- subcontract labour;
- access, lifting and hire charges;
- freight and carriage;
- travel and accommodation where applicable;
- refrigerant and consumables;
- return and restocking cost;
- warranty recovery;
- credits and rebates; and
- allocated overhead or standard labour recovery.

Quoted cost is an estimate. Frostline distinguishes:

- estimated cost;
- budget cost;
- committed cost;
- accrued cost;
- invoiced supplier cost;
- actual recorded cost;
- forecast-to-complete; and
- expected final cost.

The forecast is updated when new evidence changes expected outcome. It is not kept artificially aligned to the original estimate merely because final invoices have not arrived.

## Labour recording

Engineers record time against work for costing, capacity and payroll-related purposes. Travel, site labour, workshop activity, training, absence, supervision and non-chargeable remedial work may need different treatment.

Time recorded is not automatically time chargeable to the customer. Commercial rules, quotation basis, contract entitlement, warranty status and management judgement determine recoverability.

Corrections to labour records preserve the original entry, reason, approver and revised allocation where material. Moving time between jobs solely to improve apparent margin is not acceptable.

## Materials and stock cost

Materials may be:

- purchased directly for a job or project;
- issued from warehouse stock;
- used from van stock;
- returned unused;
- transferred between jobs;
- scrapped;
- replaced under warranty; or
- retained as project surplus.

The financial record should preserve quantity, cost basis, source, destination and relevant return or recovery.

Unused project materials do not disappear from cost merely because they remain in a van or depot. They are returned to controlled stock, retained against a named future requirement or written off under authority.

## Supplier invoices

Purchase invoices are matched where practical to:

- approved supplier order;
- goods or service receipt;
- job, project, stock or overhead destination;
- agreed price and quantity;
- delivery and carriage;
- returns or shortages; and
- applicable VAT treatment.

Differences may arise from carriage, restocking, substitutions, partial deliveries, price changes or consolidated supplier billing.

Materials bought locally during urgent work may arrive through card receipts or engineer expenses rather than the normal purchase-order route. These still need evidence, authority and attribution to the correct job or overhead category.

Where an invoice cannot be matched, the exception identifies the disputed element, operational owner, supplier action and payment decision. Finance should not guess technical equivalence or receipt from a vague description.

## Accruals and uninvoiced cost

Work may consume goods or services before the supplier invoice arrives. Material uninvoiced cost is accrued or forecast so project and period performance are not overstated.

Sources include:

- supplier goods received but not invoiced;
- subcontract attendance completed;
- access or hire still running;
- estimated utility or disposal charges;
- engineer expenses not yet submitted; and
- warranty replacements expected to become chargeable if recovery fails.

Accruals are reviewed and released when actual invoices, credits or final decisions arrive.

## Warranty cost and recovery

Warranty treatment follows [Warranty responsibility and remedial work](../warranty/warranty-responsibility-and-remedial-work.md).

Frostline records separately:

- remedial labour and travel;
- parts, refrigerant and consumables;
- access, freight and subcontract cost;
- customer invoice or agreed charge;
- customer credit or goodwill value;
- manufacturer or supplier claim;
- subcontract recovery;
- value approved;
- value actually received; and
- final cost absorbed by Frostline.

Zero-price customer work is not zero-cost work. A promised manufacturer credit is not recovered value until confirmed and processed.

The remedial job may close operationally while the warranty case remains financially open. Conversely, a claim credit may arrive after the original project has otherwise closed and must still be attributed to the correct case and reporting period.

## Credits, write-offs and goodwill

Frostline distinguishes:

- correction of an incorrect invoice;
- contractual credit;
- service-recovery goodwill;
- warranty responsibility;
- bad-debt write-off;
- supplier credit; and
- accounting adjustment.

A customer credit note changes the financial record but does not delete the original operational history or technical conclusion.

Material credits and write-offs require a recorded reason and delegated approval. Goodwill is a commercial decision; it must not be used to disguise recurring delivery defects or rewrite responsibility.

## Invoice validation and release

Before release, finance checks evidence proportionate to value and risk. Typical checks include:

- correct customer legal entity;
- billing address, portal and purchase-order requirements;
- invoice trigger achieved;
- scope and charging basis;
- labour, material and subcontract completeness;
- VAT treatment;
- approved variations;
- warranty or goodwill status;
- previous deposits, applications or invoices;
- retention and deductions; and
- known disputes.

An invoice may be held where evidence is incomplete, but the hold itself must have a reason, owner and target action. "Waiting for paperwork" is insufficient without identifying what is missing and who must provide it.

## Credit control

Finance monitors due and overdue invoices and follows up according to value, age, dispute status and customer relationship.

An unpaid invoice may be caused by:

- simple delay;
- missing purchase-order data;
- invoice rejection;
- disputed scope or price;
- incomplete evidence;
- incorrect legal entity;
- portal or submission failure;
- customer cash-flow difficulty; or
- genuine inability to pay.

Credit-control action is more effective when the reason is known.

Useful states include:

- issued and not yet due;
- due;
- overdue, no dispute stated;
- rejected administratively;
- disputed operationally;
- promise to pay received;
- payment plan active;
- legal or collection escalation;
- credit held pending correction; and
- written off under authority.

## Customer stop and continued work

Frostline may restrict further non-essential work for customers materially outside terms. The decision considers:

- debt age and value;
- dispute credibility;
- current exposure;
- critical site or safety implications;
- existing contractual obligations;
- deposits or security;
- customer communication; and
- likelihood of recovery.

Finance controls credit status, but operational and safety implications are escalated rather than handled by a rigid automatic rule.

Emergency make-safe work may proceed under separate authority without implying that wider service has been released or that old debt is waived.

## Disputes

Invoice disputes often require input from engineers, coordinators, estimators, project managers or account owners. Finance records the disputed amount and reason but does not invent the operational answer.

A useful dispute record includes:

- invoice and disputed line or amount;
- customer's stated reason;
- accepted scope and authority;
- delivery evidence;
- chronology;
- relevant correspondence;
- Frostline technical and commercial position;
- owner of the response;
- next action and due date; and
- proposed outcome or escalation.

Resolution may involve additional evidence, correction of administrative details, commercial negotiation, partial credit, variation agreement or firm enforcement of the original charge.

The undisputed portion should remain separately visible and collectible where appropriate.

## Work in progress and revenue view

Management reporting distinguishes cash, invoicing, operational progress and accounting recognition.

Work in progress may include:

- delivered but uninvoiced work;
- partially completed projects;
- materials purchased for future installation;
- accrued supplier or subcontract cost;
- approved but not yet billed variations;
- applications awaiting certification; and
- work whose recoverability is uncertain.

The treatment must not imply certainty where customer authority, evidence or valuation remains disputed.

## Period-end review

Month-end and year-end review may cover:

- jobs operationally complete but not invoiced;
- invoices held for missing evidence;
- project applications and certifications;
- committed and accrued cost;
- stock and project material allocations;
- pending supplier credits;
- open warranty recoveries;
- customer credits not yet issued;
- aged disputes;
- retention;
- doubtful debt; and
- stale open jobs with no financial rationale.

The apparent performance of a period can be distorted by delayed project billing, equipment purchased ahead of installation, old warranty credits or work delivered without complete records. Narrative explains material distortion and uncertainty.

## Financial closure

A job or project is financially closed when:

- all material labour, materials and subcontract costs are recorded or deliberately accrued;
- invoicing entitlement has been exercised or consciously waived under authority;
- customer credits and disputes are resolved or transferred to controlled cases;
- supplier credits and returns are processed or written off;
- warranty recoveries are received, rejected or closed under authority;
- final value and expected margin are credible; and
- no ownerless financial action remains.

Financial closure does not erase future warranty obligations, retention or latent disputes. Those remain linked records with their own owners and review dates.

## Current operating reality

The finance team maintains reliable accounting records, but job-level truth is assembled from several sources. A missing worksheet, unclear contract entitlement, unrecorded variation or unresolved warranty assumption can block an otherwise valid invoice or distort margin.

Experienced staff bridge these gaps through calls and personal knowledge. Frostline treats that capability as valuable but fragile. The durable control is explicit relationship between authority, work evidence, cost, invoice, recovery, owner and next action.