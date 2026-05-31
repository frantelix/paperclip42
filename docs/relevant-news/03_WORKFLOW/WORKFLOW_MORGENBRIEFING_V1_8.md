# Workflow Morgenbriefing – relevant-news V1.8

## Ziel

Breiter Tagesstart mit harter Auswahl. Ergebnis ist ein kompaktes Briefing mit 15-20 veröffentlichten Meldungen: 5-7 Top Stories, 8-13 Kurzmeldungen, 3-5 Watchlist-Themen, sehr knappem Makro-Kontext und Datenqualitätsnotiz. Wenn die Qualität nicht trägt, wird nicht aufgefüllt.

V1.8-Ziel:

```text
Konkrete Entscheidungen, reale Ereignisse und fassbare Folgen zuerst. Makro nur sparsam und begründet.
```

---

## Ablauf

### 0. Setup-Validierung

- CMO prüft Rollen, Skills und aktiven Kontext.
- CTO unterstützt nur technisch, falls Rollen/Skills nicht korrekt angelegt sind.

Output:

- Setup-Validierung bestanden / nicht bestanden.

Gate:

- Bei nicht bestandenem Setup keinen News-Testlauf starten.

---

### 1. CEO beauftragt CMO

- CEO setzt Ziel und Rahmen.
- CEO greift nicht operativ in Ranking oder Review ein.

Output:

- Auftrag an CMO.

---

### 2. CMO startet Testlauf

- Run Mode: Morgenbriefing.
- Kein Versand.
- Keine Automation.
- V1.8 als einzige aktive Grundlage.
- Spezialrollen werden nacheinander beauftragt.
- CMO nutzt das Control-Board.
- CMO prüft besonders: konkrete A-/B-Kandidaten und Makro-Budget.

Output:

- Handoff an Scout.

---

### 3. News Scout

Output:

- Kandidatenliste,
- Quellenbasis,
- internationale Scanabdeckung,
- Konkret-Scan,
- Konkretheitsklasse A/B/C/D je Kandidat,
- konkrete Bürger-/Unternehmens-/Sicherheitsfolge je Kandidat,
- mindestens 5 Top-Story-Challenger,
- mindestens 2 ernsthafte Nicht-USA/EU-Challenger, sofern Quellenlage das hergibt,
- mindestens 3 A-/B-Challenger, sofern Quellenlage das hergibt.

Gate:

- mindestens 12 ernsthafte Kandidaten,
- Quellenstatus sichtbar,
- KI/Deutschland-konkret/Makro markiert,
- Makro-/Datenkandidaten separat markiert,
- keine Longlist, die fast nur aus Makro-/Daten-/Marktmeldungen besteht.

---

### 4. Ranking Editor

Output:

- Shortlist-Scorecard,
- Claim-Ledger,
- finale Top-Story-Auswahl,
- Watchlist,
- Raus-Entscheidungen,
- Makro-Exception-Satz falls Makro-Top.

Gate:

- 5-7 Top Stories oder weniger mit Qualitätsbegründung,
- 8-13 Kurzmeldungen oder weniger mit Qualitätsbegründung,
- 3-5 Watchlist-Themen,
- maximal 1 Makro-/Daten-/Markt-Top-Story,
- jede Top Story mit konkreter Folge,
- Score >= 8 oder Score 7 mit Zusatzbegründung,
- kein roter Gate-Verstoß,
- Score-Caps angewendet,
- Cluster-Budget geprüft,
- mindestens 5 bewusste Nicht-Aufnahmen dokumentiert,
- sichtbar beantwortet: Welche A-/B-Meldung wurde zugunsten einer C-/Makro-Meldung verdrängt – und warum?

---

### 5. Source Verifier

Pflicht für jede Top Story.

Output:

- Source Verification,
- ggf. aktualisierter Claim-Ledger,
- maximal erlaubte Formulierung,
- bewusst nicht behauptete Aussagen,
- Prüfung: beschlossen / in Kraft / geplant / berichtet / Datenpunkt,
- Prüfung: konkrete Folge belegt oder nur abgeleitet.

Wichtig:

```text
Diese Aufgabe liegt beim Source Verifier, nicht beim CTO.
```

---

### 6. Briefing Writer

Output:

- Briefing-Draft.

Gate:

- keine neuen Themen,
- keine Ranking-Änderung,
- Claim-Ledger und Source Verification eingehalten,
- jede Top Story enthält: Was ist entschieden/passiert / Konkrete Folge / Warum wichtig / Offen,
- Makro-Kontext maximal 2 Bulletpoints und nur erklärend,
- Unsicherheit sichtbar,
- Datenqualität konkret.

---

### 7. Adversarial Reviewer

Output:

- Review mit Grün/Gelb/Rot,
- Fehlercodes,
- Entscheidung je Top Story,
- Konkretheits- und Makro-Budget-Urteil,
- bei Gelb/Rot Korrekturticket.

Wichtig:

```text
Reviewer-Grün ist erforderlich.
CMO, CEO oder CTO dürfen Gelb/Rot nicht weichzeichnen.
```

---

### 8. Korrekturschleife bei Gelb/Rot

- CMO weist Korrekturticket an zuständige Rolle zu.
- Zuständige Rolle korrigiert nur ihren Teil.
- Reviewer prüft erneut.
- Gelb bleibt keine Freigabe.

---

### 9. Qualitätslog und Management-Status

Bei Grün:

- Qualitätslog erstellen,
- Management-Status an CEO,
- kein Versand im Testlauf.

Pflichtkennzahlen:

- Top Stories Klasse A/B/C/D,
- Makro-/Daten-/Markt-Top-Stories,
- geprüfte A-/B-Challenger,
- konkrete Folgen vorhanden ja/nein,
- wichtigste Korrektur gegenüber altem Workflow.
