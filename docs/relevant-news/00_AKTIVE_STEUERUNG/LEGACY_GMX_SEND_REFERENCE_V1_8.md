# Legacy-GMX-Send-Referenz - relevant-news V1.8

Dieses Dokument ist nur eine technische Referenz fuer spaetere Arbeit. Es ist keine Versandfreigabe und kein V1.8-Send-Pfad.

## Frueherer technischer Hinweis

Aus alten Lauf-/Audit-Hinweisen ergibt sich, dass ein frueherer Relevant-News-Mailpfad offenbar ueber folgende Bausteine funktionierte:

- Python `smtplib`
- GMX SMTP
- GMX App-Passwort
- ein Script mit dem Namen `send_relevant_news_mail.py`
- ein Versandlog

Das Script wurde im aktuellen Repo nicht gefunden. Selbst wenn es extern wieder auftaucht, bleibt es Legacy-Kontext und darf in RN-06 nicht reaktiviert werden.

## Empfaenger-Konventionen

Alte Konventionen:

- `RELEVANT_NEWS_MAIL_TO`
- `MAIL_TO`

Neue V1.8-Testempfaenger-Konvention:

- `RELEVANT_NEWS_TEST_RECIPIENTS`

Die alten Konventionen werden nicht automatisch uebernommen. Es gibt keinen Fallback von `RELEVANT_NEWS_TEST_RECIPIENTS` auf `RELEVANT_NEWS_MAIL_TO` oder `MAIL_TO`.

Wenn alte Empfaenger-Env-Namen in einem Prozess sichtbar sind, darf RN-06 nur warnen:

```text
Legacy recipient env present; not used by V1.8 unless explicitly mapped.
```

## Spaetere RN-07-Env-Namen

Nur Namen, keine Werte:

- `RELEVANT_NEWS_TEST_RECIPIENTS`
- `RELEVANT_NEWS_SMTP_HOST`
- `RELEVANT_NEWS_SMTP_PORT`
- `RELEVANT_NEWS_SMTP_USER`
- `RELEVANT_NEWS_SMTP_APP_PASSWORD`
- `RELEVANT_NEWS_SMTP_FROM`

Werte, echte Adressen, Domains, App-Passwoerter, SMTP-Passwoerter, Authorization-Header und andere Secrets duerfen nicht in Markdown, Handoffs, Preview-Logs oder Repo-Dateien geschrieben werden.

## RN-06-Grenze

RN-06 bleibt Preview-only:

- kein echter Versand
- kein SMTP-Aufruf
- kein Mailprovider-Aufruf
- keine Zustellung
- keine alte V1.2-Mailabschlusslogik
- `actualSend` bleibt immer `false`

Der GMX-Transport ist hoechstens ein Kandidat fuer einen spaeteren RN-07-Testsend. Dafuer braucht es separate Freigabe, eine klare Send-Mechanik, ein Versandlog, Duplicate-/Re-Send-Sperre und erfolgreiche Preview-Gates.
