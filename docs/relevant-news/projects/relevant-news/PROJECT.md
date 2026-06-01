---
kind: project
slug: relevant-news
name: Relevant News
description: Lokales Relevant-News-Projekt für manuelle und kontrolliert automatisierte Morgenbriefing-Testläufe nach V1.8.
owner: cmo
tags:
  - controlled-automation
  - manual-test
  - v1-8
---

# Relevant News

Dieses Projekt buendelt manuelle Testlaeufe und die drei V1.8-Regel-Send-Anlaesse fuer Relevant News. Es bleibt ein lokaler Testaufbau ohne Produktivstatus; echter Send ist nur im Operator-Testbetrieb und nur ueber den V1.8-News-Send-Pfad erlaubt.

## Arbeitsgrundlage

- `MANIFEST_V1_8.md`
- `00_AKTIVE_STEUERUNG/CONTROLLED_AUTOMATION_PILOT_GATES_V1_8.md`
- `03_WORKFLOW/WORKFLOW_MORGENBRIEFING_V1_8.md`
- `00_AKTIVE_STEUERUNG/HANDOFF_UND_ARTEFAKT_CONTRACTS_V1_8.md`
- `05_EVALUATION/TESTLAUF_AUSWERTUNG_TEMPLATE_V1_8.md`

## Kontrollierter Pilot

- `tasks/scheduled-morning-briefing-v18/TASK.md`, `tasks/scheduled-midday-delta-v18/TASK.md` und `tasks/scheduled-evening-briefing-v18/TASK.md` sind die aktiven V1.8-Regel-Slot-Vorlagen.
- `tasks/controlled-automation-pilot/TASK.md` bleibt historische Referenz und ist im Package schedule-disabled.
- Echter Send ist nur mit Source Verification, Claim-Disziplin, passendem finalem Slot-Mailtext, Duplicate-Schutz, `recipientCount=1`, gesetzter V1.8-SMTP-Env und sanitisierten Logs erlaubt.
- Kein Apply, solange aktive alte V1.2-Routinen oder ein paralleler alter Morgenlauf in der Runtime laufen.
- Nach jedem riskanten Runtime-Schritt wird ein Log ausserhalb von `docs/relevant-news` in einem nicht geladenen Runtime-Ausgabeordner abgelegt.
