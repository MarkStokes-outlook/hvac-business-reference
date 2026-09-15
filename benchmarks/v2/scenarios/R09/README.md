# R09 — Damaged receipt and cancelled-work exposure

Mode: control · version 2.0.0 · role: warehouse assistant · domains: receipts, returns, cancellation.

Administration condition: Replay carrier delivery event DEL-9 twice, then replay cancellation and return-request event after restart.

V1 context only: B015, B017. No V1 checkpoints or results are rescored.
