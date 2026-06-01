# Relevant News Agent Rules

Diese Regeln gelten fuer `docs/relevant-news` und die zugehoerigen lokalen Hilfsdateien.

## Sprache

- Standardsprache ist Deutsch, ausser der Auftrag verlangt ausdruecklich Englisch.
- Technische Schritte knapp und einfach erklaeren.

## Kontext

- Relevant News ist ein lokaler Paperclip-Testkontext, kein oeffentliches Produktivsystem.
- `docs/relevant-news` ist active-context-only. Paperclip darf diesen Baum als ladbaren Arbeitskontext behandeln.
- Lokaler V1.8-Operator-Testversand ist nur ueber die aktiven V1.8-Gates erlaubt.
- Oeffentlicher Produktivbetrieb, alte V1.2-Routinen, alte Mail-Skripte und alte Empfaengerableitung bleiben verboten.

## Aktiver Morgenbriefing-Vertrag

- 15-20 veroeffentlichte Meldungen.
- 5-7 Top Stories.
- 8-13 Kurzmeldungen.
- 3-5 Watchlist-Themen.
- Maximal 1 Makro-/Daten-/Markt-Top-Story.
- Kein Auffuellen ohne Qualitaet.

## Quellen der Regeln

- `01_KI_MITARBEITER` ist kanonisch fuer Langprompts.
- `agents/*/AGENTS.md` ist die runtime-nahe Kurzfassung.
- `00_START_HIER/03_COPY_PASTE_MANAGEMENT_PROMPTS_V1_8.md` und `00_START_HIER/04_COPY_PASTE_SPEZIALROLLEN_PROMPTS_V1_8.md` sind abgeleitete Copy-Paste-Indizes, keine kanonischen Quellen.
- Laufartefakte sind Outputs, keine aktiven Regeln, und gehoeren nicht in diesen aktiven Kontext.

## Datei- und Runtime-Sicherheit

- Keine neuen Root-Level-Artefakte in `docs/relevant-news` erzeugen.
- Keine Laufartefakte, Archive, Beispiele, Notizen, Logs, Runtime-Exports oder generierten Outputs in `docs/relevant-news` schreiben.
- Output-Pfade muessen ausserhalb von `docs/relevant-news` liegen oder in einem separat ausgeschlossenen Pfad, der nicht von Paperclip geladen wird.
- Keine Send-, SMTP-, Empfaenger- oder Schedule-Implementierung ohne expliziten Auftrag aendern.
- Bestehende historische Artefakte bleiben ueber Git-History und externe Operator-Backups nachvollziehbar, aber nicht im aktiven Paperclip-Ladekontext.
