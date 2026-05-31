# Rollenmatrix – relevant-news V1.8

| Rolle | Ebene | Input | Output | Muss prüfen | Darf nicht |
|---|---|---|---|---|---|
| CEO | Management | Management-Status | strategischer Auftrag, Stop-/Verbesserungsauftrag | Prozessstatus auf Managementebene | Ranking, Schreiben, Review, Gelb freigeben |
| CMO | News-Leitung / Control Tower | CEO-Auftrag, Handoffs, Artefakte | Aufgaben, CMO-Control-Board, Statusbericht, Korrekturzuweisung | Vollständigkeit, Rollentrennung, Pflichtartefakte, Reviewer-Status | Spezialrollen ersetzen, Top Stories per Bauchgefühl ändern, CTO als Reviewer nutzen |
| CTO | Technik | technischer Auftrag | Setup-Status, Mail-/Automation-Status | technische Funktionsfähigkeit | redaktionelles Review, Ranking, Briefing |
| Scout | Spezialrolle | CMO-Auftrag, aktuelle Quellen | Kandidatenliste, Quellenbasis | Breite, Delta, Quellen, internationale Scanabdeckung, Challenger | Top Stories final entscheiden, Briefing schreiben |
| Ranking Editor | Spezialrolle | Kandidatenliste, Quellenbasis | Scorecard, Claim-Ledger, Watchlist | Relevanz, Score-Caps, Kill-Switches, Challenger, Cluster-Budget | fertiges Briefing, Freigabe |
| Source Verifier | Spezialrolle | Scorecard, Claim-Ledger, Quellen | Source Verification | Claim-Scope, Reprint, Primäranker, Timing, Verb-Ladder | Ranking final entscheiden, Briefing schreiben, Review ersetzen |
| Briefing Writer | Spezialrolle | freigegebene Shortlist, Claim-Ledger, Source Verification | Briefing-Draft | Claim-Scope, Klarheit, Kürze, Unsicherheit | neue Themen, Ranking ändern, Quellen neu deuten |
| Adversarial Reviewer | Spezialrolle | alle Artefakte | Review, ggf. Korrekturticket | Ranking, Quellen, Claims, Balance, Datenqualität, Rollentrennung | Briefing selbst neu schreiben, Gelb freigeben |
| Quality Analyst optional | Evaluation | abgeschlossene Läufe | Testlauf-Auswertung | Muster, wiederkehrende Fehler | Tagesfreigabe |

---

## Kombinationsregeln

Nicht erlaubt:

- Writer + Reviewer.
- Ranking Editor + finaler Reviewer.
- CEO ersetzt Reviewer.
- CMO ersetzt Spezialrolle.
- CMO ersetzt Reviewer.
- CTO ersetzt Reviewer.
- Scout + Writer ohne Ranking-Editor-Gate.

Nur als Ausnahme erlaubt:

- Ranking Editor macht vorbereitende Claim-Prüfung im Claim-Ledger.

Aber auch dann gilt:

```text
Source Verification oder Adversarial Review muss danach unabhängig prüfen.
```

---

## Qualitätsprinzip

```text
Jede Rolle soll andere Fehler finden als die vorherige.
Management darf den Prozess verbessern, aber nicht die Qualitätsgates weichzeichnen.
```
