---
name: Error Taxonomy Review
slug: error-taxonomy-review
description: Verwendet die V1.8-Fehlercodes für Review, Korrektur und Testlauf-Auswertung.
---

# Error Taxonomy Review

## Zweck

Macht Fehler konsistent benennbar, damit Korrekturen und spätere Auswertungen vergleichbar bleiben.

## Wann verwenden?

Bei Gelb/Rot im Review, bei Korrekturtickets und bei der Quality-Analyst-Auswertung.

## Vorgehen

1. Passenden Fehlercode aus der Taxonomie bestimmen.
2. Betroffene Story, Claim oder Artefaktstelle benennen.
3. Schweregrad und Korrekturbedarf knapp begründen.
4. Korrektur an die zuständige Rolle zurückführen.
5. Häufungen für die Testlauf-Auswertung sammeln.

## Harte Stop-/Fail-Kriterien

- Gelb/Rot ohne Fehlercode.
- Fehlercode passt nicht zum konkreten Problem.
- Korrekturauftrag nennt keinen Besitzer oder nächsten Schritt.
- Auswertung verwässert Blocker zu Stilhinweisen.

## V1.8-Referenzen

- `05_EVALUATION/FEHLER_TAXONOMIE_V1_8.md`
- `02_TEMPLATES/KORREKTURTICKET_TEMPLATE_V1_8.md`
- `05_EVALUATION/TESTLAUF_AUSWERTUNG_TEMPLATE_V1_8.md`
