---
name: Workflow Orchestration
slug: workflow-orchestration
description: Koordiniert den manuellen V1.8-News-Lauf über Rollen, Handoffs, Artefakte und Stop-Gates.
---

# Workflow Orchestration

## Zweck

Sichert, dass der Morgenbriefing-Testlauf als Rollenpipeline läuft und keine Managementrolle operative Spezialarbeit ersetzt.

## Wann verwenden?

Wenn der CMO einen Lauf startet, Handoffs prüft, Rollen blockiert/freigibt oder einen Status an den CEO vorbereitet.

## Vorgehen

1. Run Mode und Ziel anhand der V1.8-Workflow-Dateien festlegen.
2. Benötigte Rollen und Pflichtartefakte je Stufe prüfen.
3. Handoff erst akzeptieren, wenn Input, Output und Stop-Gates sichtbar sind.
4. Bei Gelb/Rot Korrekturticket an die zuständige Rolle zurückgeben.
5. Nach Reviewer-Grün Management-Status und Testlauf-Auswertung vorbereiten.

## Harte Stop-/Fail-Kriterien

- Rolle überschreitet ihre Grenzen oder ersetzt eine Spezialrolle.
- Pflichtartefakt, Claim-Ledger, Source Verification oder Review fehlt.
- Gelb/Rot wird als Grün behandelt.
- Versand, Routine oder Automation wird im lokalen Test aktiviert.

## V1.8-Referenzen

- `00_AKTIVE_STEUERUNG/CMO_CONTROL_TOWER_V1_8.md`
- `00_AKTIVE_STEUERUNG/HANDOFF_UND_ARTEFAKT_CONTRACTS_V1_8.md`
- `03_WORKFLOW/WORKFLOW_MORGENBRIEFING_V1_8.md`
