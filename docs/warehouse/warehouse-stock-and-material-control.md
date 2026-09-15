# Warehouse, Stock and Material Control

## Purpose

Frostline's warehouse supports service, projects, van replenishment and warranty handling. Its purpose is not merely to hold items, but to preserve identity, condition, ownership, allocation and availability so that engineers can rely on what the business says it has.

A quantity physically present is not automatically available stock. It may be reserved, customer-owned, project-specific, damaged, quarantined, awaiting return or required as evidence.

This document follows [Canonical terminology and record relationships](../governance/canonical-terminology-and-record-relationships.md), [Purchasing and supplier control](../procurement/purchasing-and-supplier-control.md), and [Exceptions, handoffs and next-action control](../operations/exceptions-handoffs-and-next-action-control.md).

## Stock categories

Warehouse holdings may include:

- general service consumables;
- common electrical and controls components;
- filters, belts and drainage materials;
- copper, insulation, fittings and supports;
- refrigerant-related materials;
- installation sundries;
- PPE and cleaning materials;
- tools and test equipment awaiting issue;
- customer-specific spares;
- project materials;
- customer-owned equipment;
- removed warranty components;
- supplier returns;
- quarantined goods;
- recovered materials; and
- obsolete or disposal stock.

Different categories require different controls. A low-value consumable does not need the same custody as a compressor, calibrated instrument, refrigerant cylinder or failed part under investigation.

## Stock identity

A stock record should distinguish where relevant:

- internal item identifier;
- manufacturer and manufacturer part number;
- supplier reference;
- description;
- unit of measure;
- technical rating or variant;
- batch, serial or lot number;
- condition;
- ownership;
- storage requirement;
- physical location;
- available quantity;
- reserved quantity;
- quarantine quantity; and
- supersession or approved-alternative relationship.

Similar descriptions must not be treated as interchangeable where technical differences matter.

## Receipt of goods

Goods receipt records:

- supplier and purchase order;
- delivery date and carrier;
- item and quantity received;
- visible condition;
- model, part or serial information where needed;
- documents and certificates;
- job, project or stock allocation;
- shortage or back-order;
- person receiving; and
- immediate quarantine or damage decision.

Signing a carrier note confirms a delivery event, not final technical acceptance.

## Receipt exceptions

Where goods are damaged, incomplete, incorrect or undocumented, the receiver:

- separates them from available stock;
- records photographs and packaging condition where useful;
- links the purchase order and delivery evidence;
- notifies procurement;
- identifies operational impact;
- assigns the next action; and
- preserves return deadlines.

Quietly placing uncertain goods on a shelf creates false availability and weakens supplier recovery.

## Put-away and location control

Goods are stored in a defined location suitable for their size, value, environmental needs and handling risk.

Project-specific, customer-owned, warranty, recovered and quarantined materials are visibly segregated from general stock.

Moves between locations are recorded where item value, scarcity, traceability or operational dependence makes location material.

## Available, reserved and quarantined states

Frostline distinguishes:

- **available** — suitable and uncommitted for authorised issue;
- **reserved** — committed to a named job, project, customer or purpose;
- **picked** — removed from normal storage for imminent issue;
- **issued** — custody transferred to an engineer, van, site or project;
- **quarantined** — not permitted for use pending decision;
- **return pending** — controlled for supplier or manufacturer return;
- **evidence hold** — preserved for technical, warranty, insurance or dispute reasons;
- **obsolete** — no longer suitable for normal use; and
- **disposed** — removed under authorised disposal control.

One generic “in stock” status is insufficient.

## Reservation and allocation

A reservation identifies:

- item and quantity;
- intended job, project, contract or customer;
- requester;
- accountable work owner;
- required date;
- reservation date;
- review or expiry date;
- substitution permission; and
- consequence if reallocated.

Reserved stock is not reassigned merely because another job is urgent. Reallocation requires review of both commitments and notification to the displaced owner.

Long-standing reservations are reviewed so cancelled, delayed or superseded work does not lock useful inventory indefinitely.

## Picking and issue

Picking confirms that the intended item, quantity and condition have been selected for the correct work.

Issue records may include:

- job or project;
- engineer or recipient;
- van or site destination;
- item and quantity;
- serial or batch where relevant;
- date and time;
- source location;
- whether the issue is chargeable, included, warranty-related or temporary; and
- required return of unused or failed material.

Physical custody and financial allocation are related but not identical. A part can be issued before its final warranty or customer-charge treatment is known.

## Returns from engineers and sites

Returned items are assessed before re-entry to available stock.

The assessment considers whether the item is:

- unused and sealed;
- opened but complete;
- damaged;
- contaminated;
- electrically or mechanically suspect;
- missing accessories;
- customer-owned;
- removed from service;
- subject to supplier return;
- warranty evidence; or
- suitable only for disposal.

A returned item is not automatically reusable merely because it looks intact.

## Warranty and evidence custody

Removed components linked to suspected warranty, product failure, insurance or technical investigation are controlled through chain of custody.

The record should identify:

- source customer, site, system and asset;
- related job and warranty case;
- date removed;
- engineer;
- reported and observed failure;
- photographs or test references;
- condition and packaging;
- storage location;
- return or inspection deadline;
- manufacturer or supplier reference; and
- person owning the next action.

Evidence items are not stripped for parts, scrapped or mixed with general returns until authorised.

## Customer-owned and consignment stock

Customer-owned, consignment or manufacturer-loaned goods remain distinct from Frostline-owned inventory.

Records identify:

- owner;
- agreement or purpose;
- custody location;
- permitted use;
- insurance or loss position;
- replenishment responsibility; and
- return conditions.

Physical possession does not transfer ownership.

## Van stock

Van stock is distributed inventory, not personal property or invisible contingency.

Profiles reflect engineer role, geography, common work and vehicle capacity. Replenishment considers actual use, criticality and scarcity.

Transfers between vans record the item, quantity, source, destination and job where relevant. Informal transfers without records undermine both stock availability and job cost.

Engineers should not hoard scarce parts because they may be useful later.

## Project materials

Project materials are controlled against:

- accepted and released scope;
- project allocation;
- delivery sequence;
- site-storage capacity;
- theft and damage risk;
- installation programme;
- returnability;
- customer ownership where applicable; and
- changes or cancellation.

Delivering all equipment early can increase risk and cash exposure. Delivering late can stop labour. Staging is therefore a project-control decision rather than warehouse convenience.

## Direct-to-site goods

Goods delivered directly to site still require receipt and condition evidence.

The responsible recipient confirms:

- correct site and work area;
- item and quantity;
- visible condition;
- secure storage;
- shortages or damage;
- delivery documentation; and
- whether the goods are available for use or must be quarantined.

A supplier's proof of delivery does not establish that the project team received the correct complete equipment.

## Refrigerants and controlled materials

Refrigerants, gases, chemicals and controlled materials are stored and handled under applicable safety, environmental and legal controls.

Cylinder records distinguish:

- owner;
- refrigerant or content;
- virgin, recovered, recycled or waste status;
- quantity where tracked;
- cylinder identity;
- issue and return;
- job relationship; and
- disposal or recovery route.

Recovered refrigerant is never treated as clean product without an authorised assessment and process.

## Tools and test equipment

Tools and instruments held in the warehouse may require:

- unique identity;
- assigned custodian;
- issue and return;
- calibration status;
- inspection status;
- repair status;
- accessories; and
- quarantine where damaged or out of date.

An instrument physically present but out of calibration is not available for work requiring valid measurement evidence.

## Minimum, target and emergency holdings

Stock levels reflect:

- consumption;
- supplier lead time and reliability;
- item criticality;
- seasonality;
- installed customer base;
- shelf life;
- storage and cash cost;
- substitution options; and
- consequence of shortage.

A rarely used but operationally critical item may justify emergency holding. A fast-moving item may require little stock where replenishment is reliable.

## Reorder decisions

Reorder signals are reviewed against reservations, outstanding purchase orders, expected projects, supplier changes and obsolete demand.

Automatic or habitual replenishment should not continue where the underlying installed base, product range or business need has changed.

## Stock counts and reconciliation

Counts focus effort according to value, movement, risk and discrepancy history.

A discrepancy investigation considers:

- unrecorded issue or return;
- wrong unit of measure;
- duplicate item identity;
- receipt against the wrong record;
- van or site transfer;
- reservation error;
- damage or disposal;
- theft;
- picking error; and
- stock physically present but in the wrong state.

Adjustments record cause or acknowledged uncertainty. The objective is not merely to force the system number to match the shelf.

## Obsolete and slow-moving stock

Stock may become obsolete because of:

- equipment-range change;
- part supersession;
- refrigerant transition;
- shelf-life expiry;
- damage or contamination;
- lost customer base;
- changed regulation;
- unsupported controls platform; or
- project cancellation.

Review considers return, redeployment, sale, component recovery where safe, controlled retention, write-down or disposal.

Past purchase cost is not evidence of current value.

## Security and housekeeping

Access control is proportionate to value, hazard and ownership. High-value equipment, tools, refrigerants, customer-owned goods and evidence items receive stronger custody.

Safe stacking, segregation, clear aisles, spill control and clean storage protect people and material condition. Warehouse housekeeping is an operational reliability control.

## Write-offs and disposal

Stock write-off requires evidence of item, quantity, reason, value, authority and disposal route.

Technical disposal, environmental disposal and financial write-off may require separate actions. Marking an item as obsolete does not physically or financially dispose of it.

## Performance

Useful measures include:

- credible available stock;
- stockout-related lost time;
- emergency purchase frequency;
- reservation age;
- receipt discrepancies;
- quarantined stock age;
- obsolete and slow-moving value;
- write-offs;
- supplier-return recovery;
- warranty evidence overdue for action; and
- inventory-count variance by cause.

Low stock value is not automatically good if it creates repeated engineer delay. High availability is not automatically good if achieved through uncontrolled overstocking.

## Operating reality

Warehouse knowledge often accumulates in the heads of people who know which shelf, van, box or old project contains a useful item. That knowledge is valuable but fragile.

Frostline therefore treats identity, state, ownership and allocation as the minimum information needed to decide whether stock is genuinely usable—not as administrative polish.
