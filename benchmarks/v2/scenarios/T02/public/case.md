# T02: Interrupted consequential action and recovery

Your business role: finance staff. All named customer/job/test facts here are synthetic episode inputs, not enduring company rules.

T02-F01: Fully approved invoice INV-T2 for £180 excluding VAT has complete diagnostic evidence, correct payer Birch Estates Ltd and no prior issue. Related approved warehouse issue STOCK-T2 is one controller, available quantity one. Administrator integration sink records issued invoice/order events with stable references.

T02-F02: Interruption conditions are sandbox-only. No uptime target, RPO/RTO, database engine or mandatory integration is supplied. Where application has no external transport, interrupt supported save/issue acknowledgement and observe native persisted record instead.
