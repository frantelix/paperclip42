# NEW-186 Startup Canary Evidence

Datum: 2026-05-30
Issue: `NEW-186`
Status: `partial evidence recorded`

## Zweck

Kleinste sichere Scout-Canary fuer `NEW-176 startup workspace/trust verification`, ohne Editorial-Arbeit und ohne Send-Aktionen.

## Verifizierte Evidenz aus diesem Heartbeat

- Der vom Harness gesetzte aktuelle Arbeitskontext zeigt:
  - `cwd = C:\Users\frank\Downloads\paperclip42\docs\relevant-news`
- Das ist ein Projekt-Workspace-Pfad und kein offensichtlicher Fallback-Pfad.
- Die Session selbst wurde fuer diesen Workspace resumed; ein Startup-Abbruch vor Session-Kontext lag damit in diesem Lauf nicht vor.

## Trust-Repo-Pruefung

- Der String `Not inside a trusted directory and --skip-git-repo-check was not specified.` erscheint nicht im bereitgestellten Wake-/Resume-Kontext dieses Heartbeats.
- Direkt verifizieren, ob er spaeter in einem vollstaendigen lokalen Transcript steht, war in diesem Lauf nicht moeglich, weil jeder Shell-Aufruf vor Ausfuehrung scheiterte.

## Aktueller exakter Fehler

Alle getesteten Shell-Aufrufe scheiterten stattdessen mit:

`windows sandbox: runner error: CreateProcessAsUserW failed: 1920`

## Nachtest nach gemeldetem Unblock

Nach einem spaeteren `issue_blockers_resolved`-Wake wurden minimale Kommandos erneut getestet:

- `Get-Location`
- `$PWD.Path`

Beide scheiterten weiterhin vor Ausfuehrung mit demselben Fehler:

`windows sandbox: runner error: CreateProcessAsUserW failed: 1920`

## Einordnung

- Vorlaeufiges Canary-Signal: Workspace-Resolution wirkt korrekt genug, um in den Projektpfad `docs/relevant-news` zu starten.
- Der fruehere Codex-Trust-Repo-Fehler ist in diesem Heartbeat nicht der beobachtete Blocker.
- Der aktuelle naechste Blocker liegt nach Startup bei der lokalen Shell-/Prozess-Ausfuehrung.

## Luecken gegenueber Vollnachweis

- Run-ID dieses Heartbeats ist im bereitgestellten Agent-Kontext nicht sichtbar.
- Eine Issue-Kommentierung direkt in der Control Plane konnte in diesem Lauf nicht nachgezogen werden, weil kein lesbarer lokaler/API-Zugriff verfuegbar war.

## Naechster unblock owner/action

Owner: Plattform/Operator
Action: Shell-/Prozessausfuehrung fuer den Agenten reparieren oder den vollstaendigen Startup-Transcript fuer diesen Run bereitstellen, damit Run-ID und Trust-Repo-Pruefung final in den Issue-Kommentar uebernommen werden koennen.
