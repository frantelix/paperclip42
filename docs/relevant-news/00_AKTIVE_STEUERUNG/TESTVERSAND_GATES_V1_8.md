# Testversand-Gates - Relevant News V1.8

Dieses Dokument definiert die technischen und organisatorischen Gates fuer einen spaeteren kontrollierten Testversand. Es ist keine Versandfreigabe und kein Produktivstatus.

## Grundsatz

Ein Testversand ist ein separater Runtime-Schritt. Ein Routine-Sofortlauf, ein Briefing-Artefakt oder ein Management-Status ist fuer sich kein Mail-/Send-Pfad.

`POST /api/routines/:id/run` darf nur als manueller Routine-Run behandelt werden, solange der Code keinen klaren nachgelagerten Mail-/Send-Dispatch zeigt.


## RN-SCHEDULE-SEND-01 Operator-Testbetrieb

Stand 2026-05-31 gelten zusaetzlich diese Entscheidungen:

- `global_send_ban_removed`
- `actual_news_send_allowed`
- `operator_news_send_delivered`
- `scheduled_send_enabled`

Fuer die drei Anlaesse `scheduled_morning`, `scheduled_midday` und `scheduled_evening` ist `actualSend=true` erlaubt, wenn alle Slot- und Send-Gates erfuellt sind. Der einzige erlaubte News-Send-Pfad ist `scripts/relevant-news/send-briefing-mail.py`.

Die RN-06/RN-MAIL-01-No-Send-Semantik bleibt historisch fuer Preview-/Design-Aufgaben gueltig, ist aber nicht mehr die globale Default-Sperre fuer diese drei Operator-Test-Slots.

## Send-Preview-Semantik

Die Send-Preview trennt technische Preview-Ausfuehrbarkeit von Versandfreigabe:

- `previewStatus`: `pass` oder `block` fuer die technische Preview-Ausfuehrbarkeit.
- `pipelineReady`: `true` oder `false` fuer die technische Preview-Pipeline.
- `sendCandidateStatus`: `eligible`, `blocked` oder `not_applicable` fuer die redaktionelle Send-Eignung.
- `wouldSend`: nur `true`, wenn `pipelineReady=true`, `sendCandidateStatus=eligible` und eine ausdrueckliche Send-Freigabe erkannt wurde.
- `actualSend`: in RN-06/RN-06d immer `false`.

Technische No-Send-/No-Update-Kandidaten koennen eine technisch gruene Preview haben, bleiben aber `sendCandidateStatus=not_applicable` oder `blocked` und damit `wouldSend=false`.

Die Preview muss konservativ `wouldSend=false` setzen, wenn Review-, Management- oder Kandidatenartefakte Formulierungen enthalten wie "Rot fuer echten Versand", "keine Versandfreigabe", "kein echtes Nachrichtenbriefing", "technischer Preview-Kandidat", "No-Send", "nicht ausreichend fuer echten Versand" oder "kein Send-Kandidat".

Preview-Logs duerfen keine Empfaengerwerte, Domains oder Secrets enthalten. Zulaessig bleibt nur der Empfaengerstatus und die Empfaengeranzahl.

## Testversand Erlaubt Nur Bei

- Runtime unter der bewusst gesetzten API-Base erreichbar, bevorzugt `http://127.0.0.1:3100`.
- Ziel-Company eindeutig geprueft: `485a2bb7-0c62-4468-97c7-d9a0a1043482`.
- Testempfaenger explizit ausserhalb des Packages gesetzt, bevorzugt ueber `RELEVANT_NEWS_TEST_RECIPIENTS`.
- Im Log steht nur: Empfaenger gesetzt ja/nein und Anzahl; keine vollstaendigen Adressen.
- Mail-/Send-Mechanik ist technisch klar: Befehl oder API-Pfad, Eingaben, Gate-Verhalten, Fehlerverhalten.
- V1.8-Send-Mechanik ist freigegeben; alte V1.2-Mailabschlusslogik ist ausgeschlossen.
- Send-Preview oder Dry-Run ist vorhanden und vor Versand sauber gelaufen.
- Frischer Delta- oder No-Update-Lauf liegt fuer den konkreten Slot vor.
- Source Verification ist fuer alle Top-Claims vollstaendig.
- Adversarial Reviewer gibt ausdruecklich Gruen fuer genau diesen Lauf.
- Kein offenes Gelb oder Rot liegt vor.
- Datenqualitaet ist konkret benannt und glaettet keine Unsicherheit.
- Versandlog kann vorab an einem konkreten Pfad ausserhalb von `docs/relevant-news` geschrieben werden.
- Versand ist ausdruecklich Testversand, kein Produktivstatus.

## Testversand Blockiert Bei

- Runtime nicht erreichbar oder falsche API-Base.
- Ziel-Company nicht eindeutig geprueft.
- Testempfaenger fehlen oder muessten aus Markdown, Git, Logs oder Annahmen abgeleitet werden.
- Empfaengerwerte oder Secrets muessten in Dateien geschrieben werden.
- Mail-/Send-Mechanik unklar oder nur als alte V1.2-Beschreibung vorhanden.
- Fehlende Send-Preview oder fehlender Dry-Run.
- Alte V1.2-Artefakte, alte Mailvorlagen, alte Versandlogs oder alte Routinen sollen als Grundlage dienen.
- `POST /api/routines/:id/run` ist der einzige gefundene Pfad.
- Source Verification fehlt oder ist unvollstaendig.
- Adversarial Reviewer fehlt, ist Gelb/Rot oder wurde durch CMO/CEO/CTO ueberstimmt.
- Datenqualitaet ist generisch, unscharf oder widerspruechlich.
- Produktivstatus, unbekannte Empfaenger, CC/BCC oder nicht freigegebene Provider-Konfiguration waeren beteiligt.

## Minimaler Send-Preview-Plan, Falls Keine Mechanik Existiert

Solange keine echte V1.8-Send-Preview existiert, bleibt Versand blockiert. Der kleinste sichere naechste technische Plan ist:

1. Eine V1.8-kompatible Preview-Spezifikation schreiben: Eingaben, erlaubte Artefakte, Gates, Ausgabeformat und Logpfad.
2. Preview nur aus freigegebenem Briefing, Source Verification, Review-Gruen und gesetzter Empfaenger-Env erzeugen.
3. Preview-Log ohne Empfaengerwerte schreiben: API-Base, Company-ID, Run-ID oder Artefaktpfad, Empfaengeranzahl, Gate-Ergebnis, kein Secret.
4. Send-Funktion getrennt halten und standardmaessig blockieren, bis Preview sauber ist und ein separater Level-3-Auftrag vorliegt.
5. Duplicate-/Block-Logik definieren, bevor SMTP, Provider-API oder andere externe Zustellung angebunden wird.

Nicht Teil dieses Plans: Produktivversand, neue grosse Architektur, Secrets im Repo, DB-Direktzugriff oder Reaktivierung alter V1.2-Scripts.
