---
kind: task
slug: scheduled-midday-delta-v18
name: Scheduled Midday Delta V1.8
assignee: cmo
project: relevant-news
recurring: true
tags:
  - scheduled-send
  - scheduled-midday
  - v1-8
---

# Scheduled Midday Delta V1.8

## mailOccasion

`scheduled_midday`

## Run Mode

`midday_delta_update`

## Format

Delta-Update seit Morgen. Keine Wiederholung des Morgenbriefings. Bei wenig neuer Lage kurz halten oder sauber als No-Update senden. Kein Fuellbriefing.

## Mindestartefakte

- `RELEVANT_NEWS_TEXTDOKUMENT.md`
- `05_final_mail_text.md`
- `send-log.md`
- `send-log.json`
- `HANDOFF.md`

## Send-Verhalten

Echter Send ist erlaubt, wenn alle V1.8-Send-Gates erfuellt sind:

- `recipientCount=1`
- finaler Mailtext fuer `scheduled_midday` und aktuelles Datum existiert
- Mailtext nicht leer
- Mailtext benennt Delta oder No-Update ehrlich
- Duplicate-Schutz blockiert nicht
- SMTP-Konfiguration set
- keine Secrets, Empfaengerwerte oder Domains im Log

## Quality-Hinweis

Der Mailtext enthaelt:

```text
Hinweis: Lokaler Operatorbetrieb mit 1 Empfaenger. Quellen- und Claim-Disziplin werden weiter verbessert; bekannte Unsicherheiten stehen im Qualitaetshinweis.
```

## Dedupe-Regel

Keine Wiederholung ohne Delta. Wenn seit Morgen kein starkes neues Delta vorliegt, wird kein Pseudo-Briefing erzeugt.

## Pfadkonvention

```text
<operator-output-root>/relevant-news/YYYY-MM-DD_scheduled_midday/
```

Optional zusaetzlich aktualisieren, aber nur ausserhalb von `docs/relevant-news`:

- `<operator-output-root>/relevant-news/_LATEST/RELEVANT_NEWS_TEXTDOKUMENT.md`
- `<operator-output-root>/relevant-news/_LATEST/MIDDAY.md`

## Erlaubter Send-Pfad

```text
scripts/relevant-news/send-briefing-mail.py
```

## Verbotene Legacy-Pfade

- alte V1.2-Slot-Routinen
- alte Daily News Briefing v1
- alte Legacy-Mailpfade
- `POST /api/routines/:id/run` als Mail-/Send-Pfad
- `RELEVANT_NEWS_MAIL_TO`
- `MAIL_TO`
- `RELEVANT_NEWS_SMTP_PASS`
- `RELEVANT_NEWS_MAIL_FROM`
