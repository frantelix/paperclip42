---
kind: task
slug: scheduled-evening-briefing-v18
name: Scheduled Evening Briefing V1.8
assignee: cmo
project: relevant-news
recurring: true
tags:
  - scheduled-send
  - scheduled-evening
  - v1-8
---

# Scheduled Evening Briefing V1.8

## mailOccasion

`scheduled_evening`

## Run Mode

`evening_closeout_briefing`

## Format

Tagesabschluss mit Dedupe gegen Morgen und Mittag, offenen Watchlist-Triggern fuer morgen und neuen Top Stories nur bei starkem Abend-Delta.

## Mindestartefakte

- `RELEVANT_NEWS_TEXTDOKUMENT.md`
- `05_final_mail_text.md`
- `send-log.md`
- `send-log.json`
- `HANDOFF.md`

## Send-Verhalten

Echter Send ist erlaubt, wenn alle V1.8-Send-Gates erfuellt sind:

- `recipientCount=1`
- finaler Mailtext fuer `scheduled_evening` und aktuelles Datum existiert
- Mailtext nicht leer
- Mailtext passt zum Tagesabschluss
- Duplicate-Schutz blockiert nicht
- SMTP-Konfiguration set
- keine Secrets, Empfaengerwerte oder Domains im Log

## Quality-Hinweis

Der Mailtext enthaelt:

```text
Hinweis: Lokaler Operatorbetrieb mit 1 Empfaenger. Quellen- und Claim-Disziplin werden weiter verbessert; bekannte Unsicherheiten stehen im Qualitaetshinweis.
```

## Dedupe-Regel

Keine Wiederholung von Morgen oder Mittag ohne neues Delta. Watchlist-Trigger sind besser als aufgewaermte Top Stories.

## Pfadkonvention

```text
docs/relevant-news/20_LAUFARTEFAKTE/YYYY-MM-DD_scheduled_evening/
```

Zusaetzlich aktualisieren:

- `docs/relevant-news/20_LAUFARTEFAKTE/_LATEST/RELEVANT_NEWS_TEXTDOKUMENT.md`
- `docs/relevant-news/20_LAUFARTEFAKTE/_LATEST/EVENING.md`

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
