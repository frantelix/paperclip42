# Erste Umsetzung in Paperclip – relevant-news V1.8

Diese Datei beschreibt die nächsten Schritte ganz praktisch.

---

## Schritt 1: ZIP entpacken

Entpacke die ZIP und nutze ausschließlich diesen Ordner als aktive Grundlage:

```text
relevant-news-v1.8
```

Nicht gleichzeitig alte V1.2/V1.3/V1.4/V1.5/V1.6/V1.7-Ordner als aktive Wissensbasis laden.

---

## Schritt 2: Managementrollen aktualisieren

Bestehende Rollen behalten:

- CEO,
- CMO,
- CTO.

Aber Prompts aktualisieren:

```text
CEO  -> 01_KI_MITARBEITER/01_CEO_COMPANY_LEAD_PROMPT_V1_8.md
CMO  -> 01_KI_MITARBEITER/02_CMO_NEWS_DIRECTOR_PROMPT_V1_8.md
CTO  -> 01_KI_MITARBEITER/03_CTO_TECH_OPS_PROMPT_V1_8.md
```

Wichtig:

```text
CEO = strategische Aufsicht.
CMO = Control Tower / News-Abteilungsleiter.
CTO = Technik.
```

---

## Schritt 3: Spezialrollen anlegen

Unter dem CMO diese Rollen anlegen:

```text
relevant-news Scout
relevant-news Ranking Editor
relevant-news Source Verifier
relevant-news Briefing Writer
relevant-news Adversarial Reviewer
```

Prompts:

```text
01_KI_MITARBEITER/10_NEWS_SCOUT_PROMPT_V1_8.md
01_KI_MITARBEITER/11_RANKING_EDITOR_PROMPT_V1_8.md
01_KI_MITARBEITER/12_SOURCE_VERIFIER_PROMPT_V1_8.md
01_KI_MITARBEITER/13_BRIEFING_WRITER_PROMPT_V1_8.md
01_KI_MITARBEITER/14_ADVERSARIAL_REVIEWER_PROMPT_V1_8.md
```

---

## Schritt 4: Skills zuordnen

Nutze:

```text
00_AKTIVE_STEUERUNG/PAPERCLIP_ROLLEN_UND_SKILLS_V1_8.md
```

Kurzfassung:

- Scout: Websuche + Quellen + Datei schreiben.
- Ranking Editor: Analyse + Tabellen + Score-/Cluster-Gates.
- Source Verifier: Quellenprüfung + Primärquellensuche + Verb-Ladder.
- Writer: Schreiben + Kürzen, keine freie Recherche.
- Reviewer: Kritik + Quellencheck + Fehlercodes + Korrekturtickets.
- CMO: Control Tower, nicht operativ.
- CTO: Technik, nicht Redaktion.

---

## Schritt 5: Setup validieren

Vor dem ersten Lauf:

```text
00_START_HIER/08_SETUP_VALIDIERUNG_VOR_TESTLAUF_V1_8.md
02_TEMPLATES/SETUP_VALIDATION_TEMPLATE_V1_8.md
```

Wenn Setup nicht bestanden: keinen Testlauf starten.

---

## Schritt 6: Ersten Testlauf starten

CMO nutzt:

```text
03_WORKFLOW/PAPERCLIP_ISSUE_MORGENBRIEFING_V1_8.md
```

Wichtig:

```text
Kein Versand.
Keine Automation.
Nur Testlauf.
```

---

## Schritt 7: Nach dem Testlauf auswerten

Prüfen:

- Hat der Scout mindestens 12 echte Kandidaten gefunden?
- Hat der Ranking Editor mindestens 5 Challenger ernsthaft geprüft?
- Gab es mindestens 2 Nicht-USA/EU-Challenger oder eine gute Begründung?
- Hat der Source Verifier jede Top Story geprüft?
- Hat der Writer keine neuen Themen hinzugefügt?
- Hat der Reviewer wirklich widersprochen?
- Wurde maximal 1 Makro-/Daten-/Markt-Top-Story verwendet?
- Hat jede Top Story eine konkrete Bürger-/Unternehmens-/Sicherheitsfolge?
- Gab es bei Gelb/Rot ein Korrekturticket?
- Hat der CMO nur koordiniert und nicht reviewt?
- Hat der CTO nur Technik gemacht?

Wenn einer dieser Punkte scheitert, zuerst Rollen-/Skill-Zuordnung korrigieren, nicht sofort neue Regeln schreiben.
