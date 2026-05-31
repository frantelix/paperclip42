---
name: Claim Ledger and Verb Ladder
slug: claim-ledger-and-verb-ladder
description: Führt erlaubte Claims, Quellenanker, Unsicherheiten und passende Verb-Stärke.
---

# Claim Ledger and Verb Ladder

## Zweck

Sichert, dass Ranking, Verification, Writing und Review dieselbe belegte Claim-Grenze verwenden.

## Wann verwenden?

Bei Ranking, Source Verification, Writing und Review, sobald Claims formuliert oder geprüft werden.

## Vorgehen

1. Pro Top Story Claim, Quelle, Status und erlaubte Verb-Stufe erfassen.
2. Unsichere oder indirekte Claims als begrenzt markieren.
3. Nicht erlaubte Aussagen sichtbar ausschließen.
4. Writer-Formulierungen gegen die erlaubte Verb-Stufe prüfen.
5. Review-Abweichungen mit Fehlercode markieren.

## Harte Stop-/Fail-Kriterien

- Claim-Ledger fehlt oder ist nicht je Top Story geführt.
- Writer formuliert stärker als der Ledger erlaubt.
- Unsicherheit wird entfernt.
- Review kann Draft und Ledger nicht zusammenführen.

## V1.8-Referenzen

- `02_TEMPLATES/CLAIM_LEDGER_TEMPLATE_V1_8.md`
- `04_RULES/ZWEI_QUELLEN_UND_VERB_LADDER_GATE_V1_8.md`
- `00_AKTIVE_STEUERUNG/HANDOFF_UND_ARTEFAKT_CONTRACTS_V1_8.md`
