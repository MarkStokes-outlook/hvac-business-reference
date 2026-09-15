# Frostline Mechanical Services Ltd

Frostline Mechanical Services Ltd is a fictional, independently owned HVAC engineering business based in Greater Manchester. It designs, installs, maintains and repairs commercial heating, ventilation and air-conditioning systems across North West England.

The company began as a small refrigeration and air-conditioning contractor and has grown into a regional engineering business serving offices, retail sites, hospitality venues, schools, light-industrial premises and multi-site commercial customers. Its work now spans new installations, planned maintenance, reactive call-outs, equipment replacement, commissioning and warranty support.

This repository describes Frostline as a business: its history, organisation, services, customers, operating practices, commercial model, decision-making and working culture. It is intended to be internally coherent and realistic enough to stand on its own as a fictional company and detailed enough for an AI agent to reason from without silently inventing industry assumptions.

## Repository contents

### Company

- [Company profile](docs/company/company-profile.md)
- [Company history](docs/company/company-history.md)
- [Culture and values](docs/company/culture-and-values.md)

### Organisation and people

- [Organisation overview](docs/organisation/organisation-overview.md)
- [Roles, skills and availability](docs/people/roles-skills-and-availability.md)
- [Training, competence and career development](docs/people/training-competence-and-career-development.md)

### Customers, sales and service relationships

- [Customer and site model](docs/customers/customer-and-site-model.md)
- [Customer acquisition and account development](docs/sales/customer-acquisition-and-account-development.md)
- [Complaints, escalations and service recovery](docs/customer-service/complaints-escalations-and-service-recovery.md)
- [Service contracts](docs/contracts/service-contracts.md)
- [SLAs, response and coverage](docs/contracts/slas-response-and-coverage.md)
- [Warranty responsibility and remedial work](docs/warranty/warranty-responsibility-and-remedial-work.md)

### Assets and technical estate

- [Equipment and asset records](docs/assets/equipment-and-asset-records.md)
- [Manufacturer relationships](docs/manufacturers/manufacturer-relationships.md)
- [Refrigerants, energy and environmental performance](docs/environment/refrigerants-energy-and-environmental-performance.md)
- [Diagnostics, controls and technical escalation](docs/technical-support/diagnostics-controls-and-technical-escalation.md)

### Services and operations

- [Services overview](docs/services/services-overview.md)
- [Work lifecycle](docs/operations/work-lifecycle.md)
- [Exceptions, handoffs and next-action control](docs/operations/exceptions-handoffs-and-next-action-control.md)
- [Planned and reactive service](docs/service/planned-and-reactive-service.md)
- [Field-engineering workflow](docs/field-engineering/site-visits-and-engineer-workflow.md)
- [Resource planning and scheduling](docs/dispatch/resource-planning-and-scheduling.md)
- [Installation project delivery](docs/projects/installation-project-delivery.md)

### Commercial, finance and risk

- [Commercial model](docs/commercial/commercial-model.md)
- [Estimating and quotation](docs/quoting/estimating-and-quotation.md)
- [Invoicing, cost control and credit](docs/finance/invoicing-cost-control-and-credit.md)
- [Business metrics and KPIs](docs/reporting/business-metrics-and-kpis.md)
- [Insurance, claims and business risk](docs/risk/insurance-claims-and-business-risk.md)

### Supply chain, stock and field resources

- [Suppliers, stock and subcontractors](docs/supply-chain/suppliers-stock-and-subcontractors.md)
- [Purchasing and supplier control](docs/procurement/purchasing-and-supplier-control.md)
- [Warehouse, stock and material control](docs/warehouse/warehouse-stock-and-material-control.md)
- [Vans, tools and calibration](docs/fleet/vans-tools-and-calibration.md)

### Compliance and information

- [Safety, quality and environmental controls](docs/compliance/safety-quality-and-environment.md)
- [Records, documents and communication](docs/information/records-documents-and-communication.md)

### Governance and semantic consistency

- [Repository constitution](docs/governance/repository-constitution.md)
- [Decision rights and operational authority](docs/governance/decision-rights-and-operational-authority.md)
- [Canonical terminology and record relationships](docs/governance/canonical-terminology-and-record-relationships.md)

### Reasoning benchmarks and generated public artefacts

- [Benchmark framework](benchmarks/README.md)
- [Benchmark specification](benchmarks/framework/benchmark-specification.md)
- [B001 — Reactive callout triage and control](benchmarks/B001-reactive-callout-triage-and-control/README.md)
- [B001 public brand and marketing brief](benchmarks/B001-reactive-callout-triage-and-control/public-brand/brand-and-marketing-brief.md)
- [Reusable website generation assignment](prompts/website-generation.md)

## Repository boundaries

This repository does not define a software product, target architecture, CRM implementation, technology stack or preferred delivery method. Business facts must not be introduced merely to favour or disadvantage a later software-development approach.

Information may eventually be represented through several forms, including internal reference documents, public website content, sample business records and stakeholder conversations. Those representations may differ in detail and perspective, as they would in a real organisation, while remaining consistent with the underlying business.

The benchmark layer under `benchmarks/` evaluates reasoning from the business reference. It may introduce case-specific events, but it does not own or redefine enduring Frostline facts. Those remain authoritative under `docs/`.

A benchmark may define its own public-brand projection for websites and other external artefacts. That projection selects and markets an appropriate public subset of canonical knowledge; it is not a complete representation of the internal business. Generated websites belong to the benchmark and must not be treated as universal or canonical Frostline assets.

## Interpretation rules

The governance documents define how the repository should be interpreted:

- canonical terminology gives precise meanings to recurring concepts while allowing realistic informal language;
- decision authority separates technical judgement, customer approval, safety authority and Frostline financial commitment;
- operational records should identify the next action, accountable owner and unresolved dependency; and
- uncertainty, disagreement and incomplete evidence should be represented rather than silently normalised.

Domain documents may add more specific controls, but should not redefine these foundations without explicitly reconciling the change.

Public artefacts should remain factually supported while translating internal truth into audience-appropriate marketing language. Canonical correctness does not require publishing every internal fact or reproducing internal terminology verbatim.

## Current status

The repository covers the principal structure and operating model of a mature regional HVAC contractor, including customer acquisition, contracts, service delivery, installation projects, field engineering, dispatch, estimating, purchasing, stock, fleet, technical escalation, workforce competence, finance, reporting, risk, environmental performance, warranty responsibility and service recovery.

Every operational domain document explicitly references the governance layer it depends on. Key concepts (restoration, resolution, escalation, attendance, job, project, competence, commercial release, handoff, exception, priority, first-time fix, practically complete, triage, waiting state, clock stop) are defined canonically and used consistently across documents. Decision authority boundaries are preserved throughout — domain documents describe authority at the operational level without creating competing frameworks.

The canonical terminology includes a domain-owned state model registry mapping 15 lifecycle records to their authoritative state definitions. Sibling documents that share operational boundaries are cross-referenced bidirectionally.

The first benchmark reference implementation tests cross-domain operational reasoning against that business model. It now also defines a benchmark-specific public-brand projection and a reproducible website-generation assignment, allowing generated public artefacts to be assessed without exposing or redefining the full internal knowledge base.

Remaining improvements should favour demonstrable reasoning gaps, contradictory terms or business decisions that cannot yet be explained from repository evidence over indiscriminate document creation.