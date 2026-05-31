# Mail Occasions - Relevant News V1.8

## Entscheidung

Stand 2026-05-31:

- `global_send_ban_removed`
- `actual_news_send_allowed`
- `operator_news_send_delivered`
- `scheduled_send_enabled`

Die fruehere RN-MAIL-01-No-Send-Default-Annahme war Scope der Designaufgabe. Sie ist fuer den lokalen Operator-Testbetrieb durch die spaetere Operator-Entscheidung ueberholt.

## Grundmodell

Alle Mail-Laeufe verwenden eine gemeinsame V1.8-Mail-Occasion-Pipeline mit Anlassprofilen:

```text
Occasion Intake
-> Run Mode Decision
-> Scout
-> Ranking Editor
-> Source Verifier
-> Briefing Writer
-> Adversarial Reviewer
-> Quality Analyst/CMO
-> Send Gate
```

Pflichtmetadatum:

```text
mailOccasion
```

Erlaubte Anlasswerte:

- `scheduled_morning`
- `scheduled_midday`
- `scheduled_evening`
- `operator_adhoc`
- `breaking_alert`

## Drei aktivierte Regel-Send-Anlaesse

| mailOccasion | Default-Zeit | Format | Send-Status |
|---|---:|---|---|
| `scheduled_morning` | 05:30 Europe/Berlin | Vollbriefing | echter Send erlaubt |
| `scheduled_midday` | 11:30 Europe/Berlin | Delta-Update seit Morgen | echter Send erlaubt |
| `scheduled_evening` | 18:30 Europe/Berlin | Tagesabschluss, Dedupe, Watchlist | echter Send erlaubt |

Die drei Anlaesse sind nicht drei getrennte redaktionelle Systeme. Sie teilen dieselben Rollen, dieselbe Claim-Disziplin und denselben Send-Pfad.

## Send-Pfad

Der einzige erlaubte V1.8-News-Send-Pfad ist:

```text
scripts/relevant-news/send-briefing-mail.py
```

Erlaubte Env-Namen:

- `RELEVANT_NEWS_TEST_RECIPIENTS`
- `RELEVANT_NEWS_SMTP_HOST`
- `RELEVANT_NEWS_SMTP_PORT`
- `RELEVANT_NEWS_SMTP_SECURITY`
- `RELEVANT_NEWS_SMTP_USER`
- `RELEVANT_NEWS_SMTP_APP_PASSWORD`
- `RELEVANT_NEWS_SMTP_FROM`

Verbotene Legacy-Env-Namen:

- `RELEVANT_NEWS_MAIL_TO`
- `MAIL_TO`
- `RELEVANT_NEWS_SMTP_PASS`
- `RELEVANT_NEWS_MAIL_FROM`

Logs duerfen nur set/unset, true/false, `recipientCount` und Statusfelder enthalten. Empfaengerwerte, Domains, SMTP-User, Passwoerter, Tokens und Secrets bleiben aus allen Artefakten raus.

## Send-Erlaubnis je Slot

`actualSend=true` ist fuer `scheduled_morning`, `scheduled_midday` und `scheduled_evening` erlaubt, wenn alle Gate-Bedingungen erfuellt sind:

- `recipientCount=1`
- finaler Mailtext fuer genau diesen Slot existiert
- Mailtext ist nicht leer
- Mailtext passt zu aktuellem Datum und `mailOccasion`
- Duplicate-Schutz blockiert nicht
- SMTP-Konfiguration ist set
- keine Secrets, Empfaengerwerte oder Domains werden geloggt
- keine alten V1.2-Pfade werden genutzt
- bekannte ungestuetzte Claims sind entfernt, enger formuliert oder im Qualitaetshinweis markiert

Qualitaetsrisiken sind im Operator-Testbetrieb Warnungen, keine automatische globale Sperre. Ungestuetzte Claims duerfen aber nicht unmarkiert versendet werden.
