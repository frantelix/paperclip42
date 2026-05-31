# Relevant News Agent Rules

Diese Regeln gelten fuer `docs/relevant-news` und die zugehoerigen lokalen Hilfsdateien.

## Sprache

- Standardsprache ist Deutsch, ausser der Auftrag verlangt ausdruecklich Englisch.
- Technische Schritte knapp und einfach erklaeren.

## Kontext

- Relevant News ist ein lokaler Paperclip-Testkontext, kein oeffentliches Produktivsystem.
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
- Laufartefakte sind Outputs, keine aktiven Regeln.

## Datei- und Runtime-Sicherheit

- Keine neuen Root-Level-Artefakte in `docs/relevant-news` erzeugen.
- Laufartefakte gehoeren nur unter `20_LAUFARTEFAKTE` und werden nicht als aktive Regeln importiert.
- Keine Send-, SMTP-, Empfaenger- oder Schedule-Implementierung ohne expliziten Auftrag aendern.
- Keine non-empty Laufartefakte verschieben oder loeschen, solange der Auftrag das nicht ausdruecklich verlangt.
