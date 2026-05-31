# Regressionstests – typische Fehler V1.8

Diese Tests helfen zu prüfen, ob die Rollen/Gates wirklich funktionieren.

---

## Test 1 – Vorfeldmeldung wird zu Top Story

Input:

```text
Quelle sagt: Ein CEO reist zu einem Gipfel mit. Gespräche beginnen morgen. Konkrete Agenda offen.
```

Erwartung:

- keine Top Story,
- Watchlist,
- Formulierung: „möglicher Prüfpunkt, Ergebnisse offen".

Fehlercode bei Verstoß:

- F3 Claim zu stark,
- F4 kein echtes Delta,
- F11 Auffüllmeldung.

---

## Test 2 – Deutschland konkret ohne Primärquelle

Input:

```text
Reprint berichtet angeblichen Kabinettsbeschluss mit Kostenfolge für Haushalte. Kein offizielles Dokument geprüft.
```

Erwartung:

- Gelb,
- Primäranker suchen,
- eng formulieren oder Watchlist.

Fehlercode:

- F5 Reprint-only,
- F7 Deutschland-konkret ohne Primäranker.

---

## Test 3 – KI-Anbieterclaim klingt groß

Input:

```text
Anbieterblog kündigt neues Tooling-Feature an. Kein unabhängiger Zweitanker, keine Breitenwirkung belegt.
```

Erwartung:

- Praxisnotiz oder raus,
- keine Top Story.

Fehlercode:

- F6 KI übergewichtet.

---

## Test 4 – Fünfte Meldung ist schwach

Input:

```text
Vier starke Top Stories, fünfte Meldung nur Wiederholung ohne Delta.
```

Erwartung:

- nur 4 Top Stories,
- keine Auffüllmeldung.

Fehlercode:

- F11 Auffüllmeldung.

---

## Test 5 – Internationale Balance nur formal

Input:

```text
Scanblock nennt Afrika und Lateinamerika, aber keine Challenger und keine Begründung.
```

Erwartung:

- Gelb,
- Challenger ergänzen oder Null-Entscheidung begründen.

Fehlercode:

- F8 internationale Balance nur formal,
- F20 Nicht-USA/EU nur formal geprüft.

---

## Test 6 – Writer erfindet neues Thema

Input:

```text
Briefing enthält eine Meldung, die nicht in Shortlist/Claim-Ledger steht.
```

Erwartung:

- Draft ungültig,
- zurück an Writer,
- bei wiederholtem Fehler Rot.

Fehlercode:

- F13 Rollenvermischung oder Writer-Gate-Verstoß.

---

## Test 7 – Source Verification fehlt

Input:

```text
Top Stories haben Claim-Ledger, aber keine separate Source Verification.
```

Erwartung:

- Gelb,
- Source Verifier nachbeauftragen,
- Writer darf nicht finalisieren.

Fehlercode:

- F16 Source Verification fehlt.

---

## Test 8 – CMO springt operativ ein

Input:

```text
CMO korrigiert selbst Ranking und formuliert Teile des Briefings um, statt Korrekturticket an Ranking Editor/Writer zu geben.
```

Erwartung:

- Gelb,
- Rollentrennung korrigieren,
- Korrektur an Spezialrolle zurückgeben.

Fehlercode:

- F18 CMO-Rolle falsch genutzt,
- F13 Rollenvermischung.

---

## Test 9 – Cluster-Dominanz unbegründet

Input:

```text
Vier von fünf Top Stories stammen aus KI/Big-Tech, aber es gibt keine Tagesdominanz-Begründung und keine starken Challenger-Vergleiche.
```

Erwartung:

- Gelb,
- Cluster-Budget prüfen,
- schwache Cluster-Meldungen herabstufen.

Fehlercode:

- F17 Cluster-Dominanz unbegründet,
- F6 KI übergewichtet.

---

## Test 10 – Verb-Ladder verletzt

Input:

```text
Quelle sagt: Regierung will Entwurf vorlegen. Draft schreibt: Regierung beschließt neue Pflicht.
```

Erwartung:

- Gelb,
- Formulierung auf „will vorlegen/plant" senken,
- nicht als vollzogene Pflicht darstellen.

Fehlercode:

- F3 Claim zu stark,
- F19 Verb-Ladder verletzt.

---

## Test 11 – Makrodaten verdrängen konkrete Entscheidung

Input:

```text
Shortlist enthält U.S.-PPI als Top Story und eine bestätigte neue Förderung/Regel mit direkter Bürgerfolge nur als Nebenmeldung.
```

Erwartung:

- konkrete A-Meldung gegen PPI neu prüfen,
- PPI nur Top, wenn Makro-Exception-Satz überzeugt,
- sonst PPI in Makro-Kontext verschieben.

Fehlercode:

- F21 konkrete Entscheidung verdrängt,
- F22 Makro-Budget überschritten,
- F23 Bürger-/Unternehmensfolge fehlt.

---

## Test 12 – Ölpreis-Tick wird als Top Story aufgeblasen

Input:

```text
Öl fällt/steigt intraday leicht. Keine neue Entscheidung, keine neue operative Lage, keine neue Versorgungsauswirkung.
```

Erwartung:

- keine Top Story,
- höchstens Makro-Kontext zur eigentlichen Energie-/Sicherheitslage,
- Score-Cap 5.

Fehlercode:

- F24 Daten-/Preis-Tick aufgeblasen,
- F10 Makro und Top Stories vermischt.

---

## Test 13 – Zweite Makro-Top-Story im Morgenbriefing

Input:

```text
Top Stories enthalten CPI und PPI oder Ölpreis und BIP gleichzeitig.
```

Erwartung:

- maximal eine Makro-/Daten-/Markt-Top-Story,
- zweite Makro-Meldung Kontext/Watchlist/raus,
- Reviewer setzt mindestens Gelb, wenn keine extreme Ausnahme belegt ist.

Fehlercode:

- F22 Makro-Budget überschritten.

---

## Test 14 – Top Story ohne konkrete Folge

Input:

```text
Top Story erklärt nur: Lage bleibt angespannt, Märkte reagieren, Daten sind gemischt.
```

Erwartung:

- herabstufen oder konkretisieren,
- Pflichtsatz nachfordern: Was ändert sich für wen?

Fehlercode:

- F23 Bürger-/Unternehmensfolge fehlt.
