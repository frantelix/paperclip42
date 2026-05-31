# Relevant News – V1.8 Start hier

**Projekt:** lokale Paperclip-News-Firma Relevant News
**Offizieller Firmenname:** Relevant News
**Slug / Ordnername:** `relevant-news`
**Zweck:** tägliches, kompaktes News-Briefing mit harter Priorisierung
**Status:** lokaler Paperclip-Testaufbau, kein Produktivsystem; lokaler V1.8-Operator-Testversand ist nur ueber die V1.8-Gates erlaubt
**Kernänderung gegenüber V1.7:** V1.8 schärft die redaktionelle Priorität weg von Makro-/Datenlastigkeit hin zu **konkreten Entscheidungen, realen Ereignissen und fassbaren Bürger-/Unternehmensfolgen**. Der CMO bleibt Control Tower, aber prüft jetzt zusätzlich aktiv, ob der Prozess konkrete A-/B-Kandidaten gesucht und Makro streng begrenzt hat.

---

## 0. Schnellanker

Relevant News ist ein lokaler Paperclip-Testaufbau für ein tägliches kompaktes News-Briefing. Aktive Grundlage bleibt `relevant-news-v1.8`; der technische Slug und der Ordner `docs/relevant-news` werden nicht umbenannt.

Aktive Kernartefakte für einen Morgenlauf:

- Setup-Validierung
- CMO-Control-Board
- Kandidatenliste
- Quellenbasis
- Shortlist-Scorecard
- Claim-Ledger
- Source Verification
- Watchlist
- Briefing-Draft
- Adversarial Review
- Qualitätslog
- Management-Status

Grober Rollenfluss:

```text
Scout -> Ranking Editor -> Source Verifier -> Briefing Writer -> Adversarial Reviewer -> CMO
```

Harte V1.8-Gates:

- Keine Top Story ohne Source Verification.
- Maximal 1 Makro-/Daten-/Markt-Top-Story.
- Jede Top Story braucht konkrete Bürger-/Unternehmens-/Sicherheitsfolge.
- Keine Auffüllmeldung.
- Watchlist nur mit Triggern.
- Gelb/Rot braucht Fehlercode.
- Datenqualitäts-Hinweis muss konkrete Schwäche benennen.

Alte ZIPs sind Archivartefakte und nicht aktive Quelle für den V1.8-Lauf.

---

## 1. Leitformel

```text
CEO führt die Firma.
CMO führt die News-Abteilung als Control Tower.
Spezialrollen erledigen die redaktionelle Arbeit.
CTO setzt Technik, Mail und Automatisierung um.

Scout findet breit – besonders konkrete Entscheidungen und reale Ereignisse.
Ranking Editor entscheidet hart – A/B vor C/Makro bei vergleichbarer Tragweite.
Source Verifier begrenzt Claims und prüft, ob etwas wirklich beschlossen/passiert ist.
Briefing Writer schreibt nur aus freigegebenem Material und nennt konkrete Folgen.
Adversarial Reviewer widerspricht und blockiert.
CMO prüft Prozessvollständigkeit und Makro-Disziplin, nicht einzelne Nachrichten nach Geschmack.
CEO bekommt Status, ersetzt aber nicht den Review.
CTO versendet oder automatisiert erst nach expliziter Freigabe – im Testlauf gar nicht.
```

---

## 2. Warum diese Struktur wichtig ist

Die schlechte Qualität früherer Läufe entstand vor allem durch zwei Muster:

1. Rollenvermischung: Eine Rolle fand Themen, schrieb, prüfte sich selbst und gab freundlich frei.
2. Datenlastigkeit: Ölpreise, CPI/PPI/BIP, Arbeitsmarkt- oder Marktstress wurden zu oft als Top Stories behandelt, obwohl konkrete Entscheidungen oder reale Ereignisse nützlicher gewesen wären.

V1.8 verhindert beides durch Arbeitsteilung, harte Übergaben und ein neues Konkretheits-/Makro-Budget.

---

## 3. Zielstruktur in Paperclip

```text
CEO
└── CMO / News-Abteilungsleiter / Control Tower
    ├── relevant-news Scout
    ├── relevant-news Ranking Editor
    ├── relevant-news Source Verifier
    ├── relevant-news Briefing Writer
    └── relevant-news Adversarial Reviewer

CTO = technische Querschnittsrolle für Paperclip, Mail, Automation und Setup.
```

### Managementrollen

1. `CEO`
   Oberchef der Firma. Strategische Aufsicht, keine operative Briefing-Arbeit.

2. `CMO`
   News-Abteilungsleiter. Orchestriert Spezialrollen, prüft Handoffs und stoppt bei Gate-Verstößen. Kein Ersatz-Reviewer. In V1.8 zusätzlich Wächter gegen Makro-/Datenlastigkeit.

3. `CTO`
   Technische Umsetzung: Paperclip-Setup, Mail, Automation, Dateistruktur, technische Fehler. Kein redaktioneller Reviewer.

### Spezialrollen unter dem CMO

4. `relevant-news Scout`
   Recherchiert breit und baut die Kandidatenliste. Sucht gezielt konkrete Entscheidungen, Vollzüge, Urteile, Förderungen, Fristen und reale Ereignisse.

5. `relevant-news Ranking Editor`
   Priorisiert hart, nutzt Score-Caps, Konkretheitsklassen, Makro-Budget, erstellt Shortlist, Watchlist und Claim-Ledger.

6. `relevant-news Source Verifier`
   Prüft jede Top Story gegen Quellen, Claim-Scope, Timing und maximal erlaubte Formulierung.

7. `relevant-news Briefing Writer`
   Schreibt das Briefing nur aus freigegebenem Material und formuliert je Top Story die konkrete Folge.

8. `relevant-news Adversarial Reviewer`
   Prüft hart, findet Fehler, setzt Grün/Gelb/Rot und erzwingt Korrekturtickets.

---

## 4. Die wichtigsten V1.8-Regeln

```text
15 bis 20 veröffentlichte Meldungen: 5 bis 7 Top Stories und 8 bis 13 Kurzmeldungen. Nicht auffüllen, wenn die Qualität nicht trägt.
3 bis 5 Watchlist-Themen, nicht als Ersatz für veröffentlichte Meldungen.
Konkrete Entscheidungen/Ereignisse vor abstrakten Makrodaten.
Jede Top Story braucht eine konkrete Bürger-/Unternehmens-/Sicherheitsfolge.
Maximal 1 Makro-/Daten-/Markt-Top-Story pro Morgenbriefing.
Makro-Kontext: maximal 2 Bulletpoints, nur wenn er konkrete Nachrichten erklärt.
Gelb ist keine Freigabe.
Source Verification ist für jede Top Story Pflicht.
Jede Top Story braucht Claim-Ledger + maximal erlaubte Formulierung.
Jede Top Story braucht einen klaren Challenger-Sieg.
Maximal zwei Top Stories aus demselben Cluster, außer der Reviewer akzeptiert eine Tagesdominanz.
Mindestens zwei ernsthafte Nicht-USA/EU-Challenger im Morgenlauf, sofern die Quellenlage das hergibt.
Mindestens drei A-/B-Challenger prüfen, sofern die Quellenlage das hergibt.
Writer darf keine neuen Themen hinzufügen.
Reviewer darf nicht Writer, Ranking Editor, CEO, CMO oder CTO sein.
CMO darf stoppen und nachfordern, aber nicht selbst reviewen.
CTO bleibt Technik.
```

---

## 5. Konkretheitsklassen

| Klasse | Bedeutung | Default |
|---|---|---|
| A | Entscheidung/Vollzug/Rechts-/Kostenfolge | bevorzugt Top-fähig |
| B | konkretes Ereignis mit realer Folge | Top-fähig bei Tragweite |
| C | Daten/Makro/Markt | Kontext; Top nur als Ausnahme |
| D | Erwartung/Agenda/Kommentar/PR | Watchlist/raus |

Bei vergleichbarer Tragweite gilt:

```text
A vor B vor C vor D.
```

---

## 6. Erster praktischer Ablauf

1. ZIP entpacken.
2. Nur `relevant-news-v1.8` als aktive Grundlage nutzen.
3. Bestehende Managementrollen aktualisieren: CEO, CMO, CTO.
4. Spezialrollen unter dem CMO anlegen.
5. Setup-Validierung ausführen.
6. CMO startet den Morgenbriefing-Testlauf.
7. Redaktioneller Testlauf: kein Versand und keine Automation. Lokaler Operator-Testversand ist nur separat über V1.8-Gates erlaubt; kein Produktivbetrieb.
8. Nach dem Testlauf Qualitätslog und Management-Status prüfen.

---

## 7. Startdateien

Für die Umsetzung zuerst lesen:

```text
00_START_HIER/01_PAPERCLIP_SETUP_CHECKLIST_V1_8.md
00_START_HIER/02_COPY_PASTE_CEO_AUFTRAG_AN_CMO_V1_8.md
00_START_HIER/03_COPY_PASTE_MANAGEMENT_PROMPTS_V1_8.md
00_START_HIER/04_COPY_PASTE_SPEZIALROLLEN_PROMPTS_V1_8.md
00_START_HIER/05_WELCHE_DATEIEN_PRO_ROLLE_LADEN_V1_8.md
00_START_HIER/06_ERSTE_UMSETZUNG_IN_PAPERCLIP_V1_8.md
00_START_HIER/07_CMO_CONTROL_TOWER_RUNBOOK_V1_8.md
00_START_HIER/08_SETUP_VALIDIERUNG_VOR_TESTLAUF_V1_8.md
```

---

## 8. Wichtig für Paperclip

Nicht jede Rolle soll die ganze ZIP lesen. Zu viel Kontext macht die Ausgabe schlechter. Je Rolle nur die Dateien laden, die in `05_WELCHE_DATEIEN_PRO_ROLLE_LADEN_V1_8.md` genannt sind.

Alte Ausgaben und alte Reviews sind keine Regeln. Aktiv gilt nur V1.8.

---

## 9. Qualitätsziel

Eine gute Ausgabe ist nicht die Ausgabe mit fünf gefüllten Plätzen. Eine gute Ausgabe ist die Ausgabe, in der jeder Platz gegen Alternativen, Quellen, Claim-Scope und konkrete Leserfolge verteidigt werden kann.

```text
Lieber weniger starke veröffentlichte Meldungen als aufgeblasene Makro-/Lagepunkte.
```
