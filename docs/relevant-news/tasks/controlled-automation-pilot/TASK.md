---
kind: task
slug: controlled-automation-pilot
name: Controlled Automation Pilot - Daily Briefing
assignee: cmo
project: relevant-news
recurring: true
tags:
  - controlled-automation
  - daily-briefing
  - v1-8
---

# Controlled Automation Pilot - Daily Briefing

## Ziel

Starte täglich einen kontrollierten Morgenbriefing-Pilotlauf für Relevant News. Der Pilot erzeugt nur Paperclip-Arbeitsobjekte und Laufartefakte. Er ist kein Produktivbetrieb und kein Versandauftrag.


## RN-SCHEDULE-SEND-01 Status

Dieser alte 06:30-Pilot ist im Package durch `relevant-news-scheduled-morning-v18` ersetzt. Sein Schedule ist in `.paperclip.yaml` pausiert und disabled, damit kein zweiter Morgenlauf mit gleichem Zweck parallel aktiv bleibt.

Diese Task-Datei bleibt nur als historische Referenz fuer den Controlled-Automation-Pilot erhalten. Neue Morgenlaeufe verwenden `docs/relevant-news/tasks/scheduled-morning-briefing-v18/TASK.md`.

## Ablauf

1. CMO prüft Setup, Run Mode und Stop-Gates.
2. CMO koordiniert die Handoff-Kette `scout -> ranking-editor -> source-verifier -> briefing-writer -> adversarial-reviewer`.
3. Spezialrollen erzeugen die Pflichtartefakte nach V1.8.
4. Adversarial Reviewer entscheidet Grün/Gelb/Rot mit Fehlercodes.
5. Bei Grün erstellt CMO Management-Status und optional Qualitätslog.
6. CMO legt ein kurzes Runtime-Log ausserhalb von `docs/relevant-news` in einem nicht geladenen Runtime-Ausgabeordner ab.

## Pflichtartefakte

- Setup-/Run-Mode-Check
- Kandidatenliste
- Quellenbasis
- Shortlist-Scorecard
- Claim-Ledger
- Watchlist
- Source Verification
- Briefing-Draft
- Adversarial Review
- Korrekturticket bei Gelb/Rot
- Management-Status
- Qualitätslog oder kurze Auswertung

## Harte Stop-Gates

- Kein Versand.
- Keine Empfänger ableiten, erfinden oder aus Markdown lesen.
- Kein Versandtest ohne explizit konfigurierte Testempfänger in der Runtime.
- Kein Import-Apply, solange aktive alte V1.2-Routinen in der Runtime laufen.
- Keine alte V1.2-Routine, kein V1.2-Mailabschluss und kein altes Versandscript als Grundlage übernehmen.
- Keine Ausgabe finalisieren, wenn Source Verification für eine Top Story fehlt.
- Reviewer-Gelb oder Reviewer-Rot ist keine Freigabe.
- CMO, CEO und CTO dürfen den Adversarial Reviewer nicht ersetzen oder überstimmen.
- Bei fehlenden Quellen, unklarem Run Mode oder Rollenvermischung: stoppen und Log ablegen.

## Versandgrenze

Dieser Pilot darf nur einen versandfähigen Kandidaten vorbereiten. Ein tatsächlicher Testversand ist ein separater, explizit freigegebener Runtime-Schritt und bleibt blockiert, solange eine dieser Bedingungen fehlt:

- Source Verification vollständig,
- Adversarial Reviewer Grün,
- explizit konfigurierte Testempfänger,
- technisches Log ausserhalb von `docs/relevant-news`.

## Collision- und Runtime-Gate

Vor Import-Apply muss `00_AKTIVE_STEUERUNG/CONTROLLED_AUTOMATION_PILOT_GATES_V1_8.md` erfüllt sein. Für bestehende Runtime-Agenten `ceo`, `cmo` und `cto` gilt `--collision skip`; diese Agenten dürfen durch den Package-Import nicht ersetzt werden.
