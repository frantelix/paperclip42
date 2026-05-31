---
kind: task
slug: morning-briefing-test-run
name: Manueller Morgenbriefing-Testlauf
assignee: cmo
project: relevant-news
tags:
  - manual-test
  - v1-8
---

# Manueller Morgenbriefing-Testlauf für Relevant News

## Ziel

Führe einen manuellen Morgenbriefing-Testlauf nach V1.8 durch. Keine Routine, kein Versand, keine API-Aktion und keine produktive Automation aktivieren.

## Erwartete Handoff-Kette

`ceo -> cmo -> scout -> ranking-editor -> source-verifier -> briefing-writer -> adversarial-reviewer -> cmo -> ceo`

Der CMO koordiniert nur. Spezialrollen produzieren die operativen Artefakte.

## Benötigte Artefakte

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
- Testlauf-Auswertung

## Stop-Gates

- Pflichtrolle oder Pflichtartefakt fehlt.
- Source Verification für eine Top Story fehlt.
- Writer fügt neue Themen oder Claims hinzu.
- Mehr als 1 Makro-/Daten-/Markt-Top-Story ohne harte Ausnahme.
- Review-Gelb/Rot wird weichgezeichnet.
- Versand, Routine oder Automation droht.

## Review mit Fehlercodes

Der Adversarial Reviewer muss bei Gelb/Rot Fehlercodes aus `05_EVALUATION/FEHLER_TAXONOMIE_V1_8.md` nennen und ein Korrekturticket an den CMO zurückgeben.

## Testlauf-Auswertung

Nach Grün oder begründetem Stop wertet der CMO optional mit `quality-analyst` aus: Artefakte, Fehlercodes, Stop-Gates, Korrekturschleifen und kleinste sinnvolle nächste Verbesserung.
