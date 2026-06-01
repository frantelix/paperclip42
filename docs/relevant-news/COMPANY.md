---
schema: agentcompanies/v1
kind: company
slug: relevant-news
name: Relevant News
description: Lokale Paperclip-News-Firma für ein kompaktes, quellengeprüftes tägliches News-Briefing.
version: 0.2.0
tags:
  - news
  - briefing
  - local-test
  - paperclip
---

# Company – Relevant News

Diese Datei ist ein Paperclip-Setup-Entwurf für die lokale Paperclip-News-Firma Relevant News. Sie ist keine Produktionskonfiguration. Stand RN-SCHEDULE-SEND-01 sind drei V1.8-Regel-Send-Anlaesse fuer den lokalen Operator-Testbetrieb erlaubt; der fruehere kontrollierte Daily-Briefing-Pilot ohne Versand ist durch die neuen Slot-Routinen ersetzt.

## Basis

- Name: Relevant News
- Slug: `relevant-news`
- Status: lokaler Paperclip-Testaufbau, kein Produktivsystem
- Automationsstatus: drei V1.8-Regel-Send-Anlaesse vorbereitet (`scheduled_morning`, `scheduled_midday`, `scheduled_evening`); echter Send ist im lokalen Operator-Testbetrieb erlaubt, wenn Source Verification, Claim-Disziplin, passender finaler Slot-Mailtext, Duplicate-Schutz, `recipientCount=1` und V1.8-SMTP-Env-Gates erfuellt sind.
- Mission: Täglich ein kompaktes, quellengeprüftes News-Briefing erstellen, das konkrete Entscheidungen, reale Ereignisse und fassbare Folgen priorisiert.
- Leserziel: Menschen, die morgens schnell verstehen wollen, welche Nachrichten heute praktisch relevant sind und warum.
- Briefing-Zielbild: Morgenbriefings zielen auf 15-20 veröffentlichte Meldungen: 5-7 Top Stories plus 8-13 publikationsfähige Kurzmeldungen. Wenn die Qualität nicht trägt, wird nicht aufgefüllt; Watchlist zählt nicht als Ersatz.

## Rollenliste

- CEO / Company Lead
- CMO / News Director / Control Tower
- CTO / Tech Ops
- relevant-news Scout
- relevant-news Ranking Editor
- relevant-news Source Verifier
- relevant-news Briefing Writer
- relevant-news Adversarial Reviewer
- relevant-news Quality Analyst optional

## Reports-to- und Handoff-Struktur

- CEO führt die Firma und beauftragt den CMO.
- CMO führt die News-Abteilung und koordiniert Scout, Ranking Editor, Source Verifier, Briefing Writer und Adversarial Reviewer.
- CTO ist technische Querschnittsrolle für Paperclip-Setup, Mail, Dateistruktur und spätere technische Folgeaufgaben.
- Scout übergibt Kandidatenliste und Quellenbasis an den Ranking Editor.
- Ranking Editor übergibt Shortlist-Scorecard, Claim-Ledger und Watchlist an den Source Verifier.
- Source Verifier übergibt geprüfte Top Stories, Source Verification und Claim-Scope an den Briefing Writer.
- Briefing Writer übergibt den Draft mit allen Pflichtartefakten an den Adversarial Reviewer.
- Adversarial Reviewer übergibt Grün/Gelb/Rot, Fehlercodes und ggf. Korrekturticket an den CMO.
- CMO meldet nach Reviewer-Grün Management-Status an den CEO.

## Tageslauf in 7 Schritten

1. CMO prüft Setup, Rollen, Skills und aktive V1.8-Grundlage; CTO unterstützt nur technisch.
2. CEO beauftragt den CMO mit dem Morgenbriefing-Testlauf.
3. Scout erstellt Kandidatenliste und Quellenbasis mit konkreten A-/B-Challengern.
4. Ranking Editor erstellt Shortlist, Claim-Ledger und Watchlist unter Makro-Budget.
5. Source Verifier prüft jede Top Story und begrenzt die erlaubten Claims.
6. Briefing Writer schreibt nur aus freigegebenem Material den Briefing-Draft.
7. Adversarial Reviewer prüft hart; bei Gelb/Rot folgt Korrekturschleife, bei Grün Qualitätslog und Management-Status.

## Qualitätsgates

- Keine Top Story ohne Source Verification.
- Maximal 1 Makro-/Daten-/Markt-Top-Story.
- Jede Top Story braucht eine konkrete Bürger-/Unternehmens-/Sicherheitsfolge.
- Keine Auffüllmeldung.
- Watchlist nur mit Triggern.
- Gelb/Rot braucht Fehlercode.
- Datenqualitäts-Hinweis muss konkrete Schwäche benennen.
- Writer darf keine neuen Themen hinzufügen.
- CMO, CEO und CTO ersetzen keine operative Spezialrolle und keinen Adversarial Reviewer.

## Scheduled Send V1.8

- Regel-Slots: `scheduled_morning` 05:30, `scheduled_midday` 11:30, `scheduled_evening` 18:30 Europe/Berlin.
- Erlaubter News-Send-Pfad: `scripts/relevant-news/send-briefing-mail.py`.
- Verboten bleiben alte V1.2-Slots, Daily News Briefing v1, Legacy-Mailpfade und Legacy-Env-Fallbacks.
- Logs duerfen keine Secrets, Empfaengerwerte, Domains oder SMTP-User-Werte enthalten.
- Der alte `controlled-automation-pilot` ist im Package pausiert und schedule-disabled, damit kein zweiter Morgenlauf parallel bleibt.

## Controlled Automation Pilot

- Routine-Slug: `controlled-automation-pilot`
- Projekt: `relevant-news`
- Assignee: `cmo`
- Status: historische Referenz; durch `relevant-news-scheduled-morning-v18` ersetzt.
- Zweck: frueher taeglich ein kontrolliertes Morgenbriefing-Arbeitsobjekt erzeugen, nicht senden.
- Schedule-Fidelity liegt in `.paperclip.yaml`.
- Jeder Runtime-Schritt nach Import-Apply, Trigger-Aktivierung oder Testversand-Vorbereitung braucht ein Log ausserhalb von `docs/relevant-news` in einem nicht geladenen Runtime-Ausgabeordner.
- Der Pilot stoppt vor Versand, wenn Source Verification, Reviewer-Grün oder explizit konfigurierte Testempfänger fehlen.
- Apply ist blockiert, solange alte V1.2-Routinen aktiv sind oder `ceo/cmo/cto` per Import-Replace überschrieben würden.

## Verweise

- Pilot-Gates: `00_AKTIVE_STEUERUNG/CONTROLLED_AUTOMATION_PILOT_GATES_V1_8.md`
- V1.8-Evaluation: `05_EVALUATION/QUALITAETS_RUBRIK_V1_8.md`
- Fehler-Taxonomie: `05_EVALUATION/FEHLER_TAXONOMIE_V1_8.md`
- Regressionstests: `05_EVALUATION/REGRESSION_TESTS_TYPISCHE_FEHLER_V1_8.md`
- Testlauf-Auswertung: `05_EVALUATION/TESTLAUF_AUSWERTUNG_TEMPLATE_V1_8.md`
- Morgenlauf-Workflow: `03_WORKFLOW/WORKFLOW_MORGENBRIEFING_V1_8.md`
- Handoff-Artefakte: `00_AKTIVE_STEUERUNG/HANDOFF_UND_ARTEFAKT_CONTRACTS_V1_8.md`
