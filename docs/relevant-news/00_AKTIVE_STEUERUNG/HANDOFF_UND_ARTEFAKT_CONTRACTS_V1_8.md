# Handoff- und Artefakt-Contracts – relevant-news V1.8

Diese Datei macht Übergaben verbindlich. Eine Rolle darf erst starten, wenn der benötigte Input vollständig ist.

V1.8-Zusatz: Jede Übergabe muss zeigen, dass konkrete Entscheidungen/Ereignisse aktiv gesucht wurden und Makro-/Datenmeldungen nicht die Auswahl dominieren.

---

## 1. Scout → Ranking Editor

### Input für Ranking Editor

- Kandidatenliste,
- Quellenbasis,
- internationaler Scanblock,
- Konkret-Scan,
- Konkretheitsklasse A/B/C/D je Kandidat,
- konkrete Bürger-/Unternehmens-/Sicherheitsfolge je Kandidat,
- Candidate Pool mit 40–60 gesichteten Leads,
- mindestens 25 ernsthafte Longlist-Kandidaten,
- mindestens 15 publikationsfähige Tier-A-/Tier-B-Kandidaten,
- mindestens 5 Top-Story-Challenger,
- mindestens 2 ernsthafte Nicht-USA/EU-Challenger, sofern die Quellenlage das hergibt,
- mindestens 3 A-/B-Challenger, sofern die Quellenlage das hergibt,
- Markierung von KI, Deutschland-konkret, Makro/Daten.

### Stop, wenn fehlt

- weniger als 25 ernsthafte Longlist-Kandidaten ohne begründeten nachrichtenarmen Tag,
- weniger als 15 publikationsfähige A-/B-Kandidaten ohne Qualitätsbegründung,
- Quellen ohne Datum/Quellentyp,
- keine Challenger,
- kein Konkret-Scan,
- keine Konkretheitsklassen,
- nur USA/EU/Big-Tech ohne Gegenprüfung,
- Longlist wird von Makro-/Daten-/Marktstorys dominiert, ohne konkrete Kandidaten zu prüfen.

---

## 2. Ranking Editor → Source Verifier

### Input für Source Verifier

- Shortlist-Scorecard,
- Claim-Ledger,
- Watchlist,
- Quellenbasis,
- Begründung für jede Top Story,
- Tier-B-Liste für weitere relevante Kurzmeldungen,
- veröffentlichte Meldungsanzahl Top Stories + Kurzmeldungen,
- Konkretheitsklasse je Top Story,
- konkrete Folge je Top Story,
- Makro-Exception-Satz, falls Makro-Top.

### Stop, wenn fehlt

- Score-Caps/Kill-Switches nicht sichtbar,
- Top Stories ohne Top-Story-Satz,
- Kurzmeldungen ohne Quelle, Frischeanker oder Relevanzsatz,
- weniger als 15 oder mehr als 20 veröffentlichte Meldungen ohne Begründung,
- Top Stories ohne konkrete Folge,
- Claim-Ledger unvollständig,
- Makro-Budget nicht geprüft,
- mehr als 1 Makro-/Daten-/Markt-Top-Story ohne Ausnahme,
- Cluster-Budget nicht geprüft.

---

## 3. Source Verifier → Briefing Writer

### Input für Writer

- geprüfte Top Stories,
- geprüfte Kurzmeldungen,
- Source Verification,
- aktualisierter Claim-Ledger,
- maximale erlaubte Formulierung,
- konkrete Folge je Top Story,
- enger Claim-Scope und Quellen-/Unsicherheitshinweis je Kurzmeldung,
- bewusst nicht behauptete Aussagen.

### Stop, wenn fehlt

- Top Story mit Verifikationsstatus offen,
- Kurzmeldung ohne tragfähigen Quellen-/Frischeanker,
- konkrete Folge nicht belegt oder zu stark formuliert,
- starke Claim-Formulierung ohne Primärquelle oder zwei tragfähige Quellen,
- Deutschland-konkret ohne Primäranker,
- Reprint-only bei starkem Claim,
- Makro-Top ohne überzeugenden Exception-Satz.

---

## 4. Writer → Reviewer

### Input für Reviewer

- Briefing-Draft,
- Kandidatenliste,
- Quellenbasis,
- Shortlist-Scorecard,
- Claim-Ledger,
- Source Verification,
- Watchlist.

### Stop, wenn fehlt

- Draft enthält Thema, das nicht in Shortlist/Claim-Ledger steht,
- Unsicherheit wurde entfernt,
- Top Stories wurden durch Writer neu sortiert,
- Top Story enthält keine konkrete Folge,
- Kurzmeldung enthält keine Relevanz oder keinen Quellen-/Unsicherheitshinweis,
- Watchlist wird als Ersatz für fehlende veröffentlichte Meldungen genutzt,
- Makro-Kontext füllt statt zu erklären,
- Qualitätshinweis ist generisch.

---

## 5. Reviewer → CMO

### Input für CMO

- Review Grün/Gelb/Rot,
- Fehlercodes,
- Entscheidung je Top Story,
- Anzahl veröffentlichter Meldungen und Entscheidung je Tier,
- Konkretheitsurteil,
- Makro-Budget-Urteil,
- Korrekturticket bei Gelb/Rot,
- Re-Review falls Korrektur erfolgt.

### Stop, wenn fehlt

- Review ist nur Lob ohne harte Prüfung,
- keine Fehlercodes bei Gelb/Rot,
- keine Entscheidung je Top Story,
- kein Urteil zu Konkretheit/Makro-Budget,
- Gelb wird als „fast freigegeben" behandelt.
