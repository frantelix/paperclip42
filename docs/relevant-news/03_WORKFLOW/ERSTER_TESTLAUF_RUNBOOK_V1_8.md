# Erster Testlauf – Runbook V1.8

## Ziel

Prüfen, ob die neue Hierarchie und Spezialrollen-Struktur funktioniert und gegenüber dem alten Workflow bessere Ergebnisse liefert.

---

## Vorbereitung

1. V1.8-ZIP entpacken.
2. Nur `relevant-news-v1.8` als aktive Grundlage laden.
3. CEO, CMO und CTO mit V1.8-Prompts aktualisieren.
4. Spezialrollen unter dem CMO anlegen.
5. Skills je Rolle zuordnen.
6. Setup-Validierung ausfüllen.

Stop:

```text
Wenn Setup-Validierung nicht bestanden ist, keinen News-Testlauf starten.
```

---

## Ablauf

1. CEO gibt Auftrag an CMO.
2. CMO startet `PAPERCLIP_ISSUE_MORGENBRIEFING_V1_8.md`.
3. CMO führt `CMO_Control_Board`.
4. Scout liefert Longlist und Quellenbasis.
5. Ranking Editor liefert Scorecard, Claim-Ledger und Watchlist.
6. Source Verifier liefert Source Verification für jede Top Story.
7. Writer liefert Briefing-Draft.
8. Reviewer liefert Grün/Gelb/Rot und Entscheidung je Top Story.
9. Bei Gelb/Rot: Korrektur und Re-Review.
10. CMO liefert Qualitätslog und Management-Status.
11. CTO dokumentiert nur technische Auffälligkeiten, falls vorhanden.

---

## Erfolgskriterien

- Keine operative Arbeit durch CEO.
- Kein redaktionelles Review durch CTO.
- CMO koordiniert, statt selbst zu recherchieren/schreiben/reviewen.
- Reviewer blockiert wirklich, wenn nötig.
- Es gibt 15-20 veröffentlichte Meldungen: 5-7 Top Stories und 8-13 Kurzmeldungen; bei zu schwacher Qualität wird nicht aufgefüllt.
- Die Watchlist enthält 3-5 Themen und ersetzt keine veröffentlichte Meldung.
- Source Verification liegt für jede Top Story vor.
- Claim-Ledger begrenzt Formulierungen sichtbar.
- Cluster-/Regionen-Budget wurde geprüft.
- Qualitätslog nennt den schwächsten Punkt.

---

## Nach dem Testlauf

Auswertung anhand:

```text
05_EVALUATION/TESTLAUF_AUSWERTUNG_TEMPLATE_V1_8.md
```

Wichtigste Frage:

```text
Ist das Ergebnis besser, weil Rollen getrennt waren – oder hat Paperclip die Rollen trotzdem vermischt?
```
