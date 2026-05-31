# Active News Skill – relevant-news V1.8

Diese Datei ist die zentrale operative Skill-Anweisung für den News-Workflow.

---

## Ziel

Erstelle ein aktuelles, hart priorisiertes News-Briefing für Leser mit wenig Zeit.

Das Morgenbriefing enthält täglich 15 bis 20 veröffentlichte Nachrichtenmeldungen:

- 5 bis 7 Top Stories mit voller Erklärung,
- 8 bis 13 weitere relevante Meldungen als Kurzmeldungen,
- eine kurze Watchlist mit 3 bis 5 Beobachtungspunkten.

Zur Zählung: Top Stories und Kurzmeldungen zählen als veröffentlichte Meldungen. Watchlist-Einträge und Makro-Kontext zählen nicht, außer ein Watchlist-Thema wird zusätzlich als Kurzmeldung ausgearbeitet.

Das Briefing enthält vor allem:

- was wirklich passiert ist,
- was entschieden wurde,
- was sich für Bürger, Unternehmen, Verwaltung, Sicherheit oder Märkte konkret ändert,
- warum es wichtig ist,
- eine kurze Watchlist,
- sehr knappen Makro-Kontext nur dort, wo er konkrete Nachrichten erklärt,
- einen kurzen Qualitätshinweis.

---

## V1.8-Leitprinzip

```text
Konkrete Entscheidungen und reale Ereignisse vor abstrakten Makrodaten.
```

Makro ist Kontext, nicht Standard-Topmeldung.

---

## Aktive Rollenlogik

```text
CEO = Oberchef, keine operative News-Arbeit.
CMO = News-Abteilungsleiter / Control Tower, koordiniert und stoppt.
CTO = Technik, keine redaktionelle Prüfung.
Spezialrollen = operative News-Qualität.
```

Spezialrollen:

1. Scout
2. Ranking Editor
3. Source Verifier
4. Briefing Writer
5. Adversarial Reviewer

---

## Kernprinzipien

1. Nicht schwach auffüllen: 15 bis 20 veröffentlichte Meldungen, aber keine Füllmeldungen.
2. Tier A: 5 bis 7 Top Stories mit neuem Delta, Tragweite, konkreter Leserfolge, starker Quelle und Challenger-Sieg.
3. Tier B: 8 bis 13 weitere relevante Meldungen, kürzer, publikationsfähig und sauber eingegrenzt.
4. Tier C: 3 bis 5 Watchlist-/Hold-Themen, noch nicht publikationsfähig oder nur Beobachtungspunkt.
5. Konkretheitsklasse A/B wird bevorzugt; C/Makro nur als Ausnahme in Top Stories.
6. Maximal 1 Makro-/Daten-/Markt-Top-Story pro Morgenbriefing; Makro-Kontext zählt nicht als Meldung.
7. Jede Top Story braucht Claim-Ledger und Source Verification; Kurzmeldungen brauchen mindestens tragfähigen Quellen-/Frischeanker und engen Claim-Scope.
8. Formuliere nie stärker als die Quelle trägt.
9. Gelb ist keine Freigabe.
10. CMO koordiniert, ersetzt aber keine Spezialrolle.
11. Reviewer bleibt unabhängig.
12. CTO bleibt Technik.
13. Alte Ausgaben und Reviews sind keine Stilvorlage.
14. Kleine, klare Artefakte statt Dokumentenmasse.

---

## Pflichtartefakte im Morgenlauf

- Kandidatenliste,
- Quellenbasis,
- Shortlist-Scorecard,
- Claim-Ledger,
- Source Verification,
- Watchlist,
- Briefing-Draft,
- Adversarial Review,
- Qualitätslog,
- Management-Status.

Bei Gelb/Rot zusätzlich:

- Korrekturticket,
- korrigiertes Artefakt,
- Re-Review.

---

## Redaktionslogik

Priorisiere wirklich wichtige und aktuelle Themen:

- politische Entscheidungen,
- Gesetze, Verordnungen, Urteile, Fristen, Förderungen, Entlastungen,
- konkrete Verwaltungs-, Kosten-, Rechte- oder Pflichtenfolgen,
- geopolitische Eskalation/Deeskalation mit realer Folge,
- konkrete Sicherheits-, Infrastruktur-, Energie- oder Versorgungslagen,
- Deutschland/EU konkret, wenn sauber belegt,
- Wirtschaft/Makro nur, wenn daraus eine konkrete Folge oder Entscheidung entsteht,
- Finanzmärkte nur bei breiter realer Wirkung,
- KI nur bei breiter Folge, Regulierung, Sicherheit, Kosten oder Infrastrukturwirkung.

Schwache Meldungen raus oder Watchlist:

- reine Erwartung,
- Agenda/Vorfeld,
- Kommentar ohne neues Faktum,
- PR/Anbieterclaim,
- Reprint-only bei starkem Claim,
- Wiederholung ohne Delta,
- reine CPI/PPI/BIP/Arbeitsmarkt-/Ölpreiszahl ohne konkrete Folge,
- Füllmeldung ohne eigenes Delta, konkrete Folge oder verlässlichen Quellenanker.

---

## Harte Qualitätsregel

```text
Ein Briefing mit 15 guten A-/B-Meldungen ist besser als ein Briefing mit 20 aufgeblasenen oder datenlastigen Meldungen.
```

Gute B-Items dürfen nicht in Watchlist/Hold verloren gehen, nur weil sie keine Top Story sind.
