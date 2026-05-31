---
kind: task
slug: scheduled-morning-briefing-v18
name: Scheduled Morning Briefing V1.8
assignee: cmo
project: relevant-news
recurring: true
tags:
  - scheduled-send
  - scheduled-morning
  - v1-8
---

# Scheduled Morning Briefing V1.8

## mailOccasion

`scheduled_morning`

## Run Mode

`morning_full_briefing`

## Format

Vollbriefing mit breitem Scan und klarem Mengenvertrag: Candidate Pool 40-60, Longlist 25-35, 15-20 veröffentlichte Meldungen, 5-7 Top Stories, 8-13 publikationsfähige Kurzmeldungen und 3-5 Watchlist-Themen. Wenn die Qualität nicht trägt, wird nicht aufgefüllt; Watchlist und Makro-Kontext zählen nicht als veröffentlichte Meldung.

## Mindestartefakte

- `RELEVANT_NEWS_TEXTDOKUMENT.md`
- `05_final_mail_text.md`
- `send-log.md`
- `send-log.json`
- `HANDOFF.md`

## Send-Verhalten

Echter Send ist erlaubt, wenn alle V1.8-Send-Gates erfuellt sind:

- `recipientCount=1`
- finaler Mailtext fuer `scheduled_morning` und aktuelles Datum existiert
- Mailtext nicht leer
- Duplicate-Schutz blockiert nicht
- SMTP-Konfiguration set
- keine Secrets, Empfaengerwerte oder Domains im Log

## Quality-Hinweis

Der Mailtext enthaelt:

```text
Hinweis: Lokaler Operatorbetrieb mit 1 Empfaenger. Quellen- und Claim-Disziplin werden weiter verbessert; bekannte Unsicherheiten stehen im Qualitaetshinweis.
```

## Dedupe-Regel

Der Morgenlauf darf keinen bereits zugestellten Morgenbriefing-Fingerprint erneut senden.

## Pfadkonvention

```text
docs/relevant-news/20_LAUFARTEFAKTE/YYYY-MM-DD_scheduled_morning/
```

Zusaetzlich aktualisieren:

- `docs/relevant-news/20_LAUFARTEFAKTE/_LATEST/RELEVANT_NEWS_TEXTDOKUMENT.md`
- `docs/relevant-news/20_LAUFARTEFAKTE/_LATEST/MORNING.md`

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
