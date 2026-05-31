# Entscheidungs-Gates – relevant-news V1.8

Diese Datei bündelt die harten Freigaberegeln.

---

## 1. Gate-Reihenfolge

Ein Briefing darf erst geschrieben und intern testfreigabefähig gemeldet werden, wenn diese Gates bestanden sind:

1. Setup- und Rollen-Gate
2. Run-Mode-Gate
3. Longlist-Gate
4. Konkretheits- und Bürgernutzen-Gate
5. Quellen- und Claim-Scope-Gate
6. Shortlist-/Score-Gate
7. Score-Cap-/Kill-Switch-Gate
8. Top-Story-Challenger-Gate
9. Makro-Budget-Gate
10. Cluster-/Regionen-Budget-Gate
11. Source-Verification-Gate
12. Writer-Gate
13. Adversarial-Review-Gate
14. Korrekturschleifen-Gate bei Gelb/Rot
15. Qualitätslog-Gate

---

## 2. Setup- und Rollen-Gate

Vor dem ersten Lauf muss klar sein:

- CEO, CMO, CTO sind korrekt geschnitten,
- Spezialrollen sind angelegt,
- Writer und Reviewer sind getrennt,
- CTO ist kein redaktioneller Reviewer,
- CMO ist Control Tower und ersetzt keine Spezialrolle,
- nur V1.8 ist aktive Grundlage.

Bei Verstoß:

```text
Status: Rot für Setup – erst Rollen/Skills/Kontext korrigieren.
```

---

## 3. Run-Mode-Gate

Vor jedem Lauf wird entschieden:

| Mode | Wann? | Ergebnis |
|---|---|---|
| Morgenbriefing | Tagesstart / voller Scan | 15–20 veröffentlichte Meldungen: 5–7 Top Stories, 8–13 Kurzmeldungen, 3–5 Watchlist-Themen, kurzer Makro-Kontext, Qualitätshinweis |
| Delta-Update | Mittags/Abends mit echten neuen Deltas | kurzes Update, keine Wiederholung |
| No-Update | keine echten Deltas | transparente No-Update-Notiz |
| Review-only | bestehender Output soll geprüft werden | Review + Korrekturticket |

Ohne Run-Mode-Entscheidung:

```text
Status: Gelb – Lauf unklar, erst Mode festlegen.
```

---

## 4. Longlist-Gate

Mindestanforderung Morgenbriefing:

- 40–60 gesichtete Kandidaten/Leads im Candidate Pool,
- mindestens 25 ernsthafte Longlist-Kandidaten,
- mindestens 15 publikationsfähige Tier-A-/Tier-B-Kandidaten,
- internationaler Scanblock vorhanden,
- Konkret-Scan vorhanden,
- Konkretheitsklasse A/B/C/D je Kandidat,
- konkrete Bürger-/Unternehmens-/Sicherheitsfolge je Kandidat,
- mindestens 5 bewusst geprüfte Top-Story-Challenger,
- mindestens 2 ernsthafte Nicht-USA/EU-Challenger, sofern die Quellenlage das hergibt,
- mindestens 3 A-/B-Challenger, sofern die Quellenlage das hergibt,
- mindestens 5 klare `raus`- oder `Watchlist`-Entscheidungen,
- KI-Kandidaten separat markiert,
- Deutschland-konkret-Kandidaten separat markiert,
- Makro-/Datenkandidaten als solche markiert,
- alte Watchlist-Punkte geprüft: hochstufen / offen / erledigt / raus.

Wenn diese Mindestanforderung nicht erfüllt ist:

```text
Status: Gelb – Longlist nacharbeiten.
```

---

## 5. Konkretheits- und Bürgernutzen-Gate

Jeder Top-Kandidat braucht:

```text
Konkretheitsklasse: A/B/C/D
Konkrete Folge: Für [Bürger/Haushalte/Unternehmen/Verwaltung/Sicherheit] ändert sich [was] ab/wegen [wann/wodurch].
```

Konkretheitsklassen:

| Klasse | Bedeutung | Default |
|---|---|---|
| A | Entscheidung/Vollzug/Rechts-/Kostenfolge | bevorzugt Top-fähig |
| B | konkretes Ereignis mit realer Folge | Top-fähig bei Tragweite |
| C | Daten/Makro/Markt | Kontext; Top nur als Ausnahme |
| D | Erwartung/Agenda/Kommentar/PR | Watchlist/raus |

Bei vergleichbarer Tragweite gilt:

```text
A vor B vor C vor D.
```

Wenn konkrete Folge fehlt:

```text
maximal Score 6, keine starke Top Story.
```

---

## 6. Quellen- und Claim-Scope-Gate

Jeder Kandidat mit `nehmen` braucht:

- mindestens einen klickbaren Link oder eindeutig identifizierte Quelle,
- Quelle trägt den konkreten Claim,
- Datum/Timing ist plausibel,
- Quellentyp ist markiert: Primärquelle / Original / Agentur / Fachquelle / Reprint / Anbieterangabe,
- Claim-Typ ist markiert: Entscheidung / offizieller Bericht / Vollzug / Datenveröffentlichung / Marktreaktion / Analyse / Erwartung,
- Claim-Scope ist benannt,
- Verifikationsstatus: bestätigt / teilbestätigt / offen,
- maximale erlaubte Briefing-Formulierung.

Top Story mit starkem Claim braucht mindestens:

```text
Primärquelle oder zwei unabhängige tragfähige Quellen.
```

Reprint zählt nicht als unabhängiger Zweitanker, wenn er nur dieselbe Agenturmeldung wiederholt.

Verifikationsstatus `offen`:

```text
Roter Gate-Verstoß – keine Top Story.
```

---

## 7. Shortlist-/Score-Gate

Mini-Score 0–10:

| Kriterium | 0 | 1 | 2 |
|---|---|---|---|
| Delta/Neuheit | kein neues Delta | Update | harter neuer Anlass |
| Tragweite | nischig | mittel | breit/global/konkret relevant |
| Quellenstärke | schwach/Reprint-only | solide Agentur/Fachquelle | Primärquelle + Bestätigung |
| konkrete Folge | abstrakt | einordnend | fassbare Bürger-/Unternehmens-/Sicherheitsfolge |
| Sicherheit | offen/unsicher | teilweise | klar bestätigt |

Regel:

- 8–10: Top-Story-fähig, wenn kein rotes Gate.
- 7: nur mit Zusatzbegründung und klarem Sieg gegen Challenger.
- 6–7: Kurzmeldungs-fähig, wenn Frische, Quelle und enger Claim-Scope tragen.
- 0–5: keine veröffentlichte Meldung, außer eng als Kontext/Watchlist begründet.

---

## 8. Score-Cap-/Kill-Switch-Gate

Score-Caps schlagen Bauchgefühl.

| Schwäche | Folge |
|---|---|
| Quelle trägt Claim nicht | Rot, raus oder neu formulieren |
| Verifikationsstatus offen | keine Top Story |
| Reprint-only bei starkem Claim | max. 6, außer Zusatzprüfung |
| Teilbestätigt | max. 7 und eng formulieren |
| Erwartung/Vorfeld/Agenda | Watchlist, außer außergewöhnliche Folge ist selbst belegt |
| KI-Anbieterclaim ohne Zweitanker | max. 6 |
| Deutschland-konkret ohne Primäranker | max. 6 |
| Kein echtes Delta | max. Watchlist / raus |
| Kein klarer Bürger-/Unternehmensnutzen | max. 6 |
| Makrozahl ohne konkrete Folge | max. 5 |
| Öl-/Börsen-/Index-Tick ohne neue reale Ursache | max. 5 |
| Zweiter ähnlicher Makrodatensatz des Tages | max. 4 |
| Konkrete A-/B-Challenger nicht geprüft | max. 6 |
| Kein Challenger geprüft | Auswahl nicht freigeben |
| Mehr als 2 Top Stories gleicher Cluster ohne Tagesdominanz-Begründung | Gelb |
| Mehr als 1 Makro-/Daten-/Markt-Top-Story ohne Ausnahme | Gelb |

---

## 9. Top-Story-Challenger-Gate

Jede Top-Story-Auswahl muss gegen Alternativen antreten.

Mindestformat:

```text
Top Story, weil [neuer konkreter Anlass] + [Tragweite] + [konkrete Folge] und stärker als [Challenger].
```

Bei Makro-Top zusätzlich:

```text
Trotz Makro-Charakter Top Story, weil [konkrete Folge] und stärker als [konkrete A-/B-Challenger].
```

Wenn der Satz nicht überzeugt:

```text
Kurzmeldung, Watchlist, Makro-Kontext oder raus.
```

---

## 10. Makro-Budget-Gate

Für Morgenbriefings gilt:

```text
Maximal 1 Top Story aus Makro/Daten/Märkten.
Makro-Kontext maximal 2 Bulletpoints.
Kein Makroblock, wenn er nichts erklärt.
```

Makro darf Top Story sein, wenn mindestens zwei Bedingungen erfüllt sind:

- frisch und stark abweichend,
- konkrete Folge für Zinsen, Preise, Sozialleistungen, Staatshaushalt, Unternehmen, Verbraucher oder Marktstabilität,
- primäre/starke Quelle,
- keine stärkere konkrete A-/B-Meldung wird verdrängt,
- Makro-Exception-Satz überzeugt.

Wenn nicht:

```text
Makro-Kontext, Watchlist oder raus.
```

---

## 11. Cluster-/Regionen-Budget-Gate

- Maximal 2 Top Stories aus demselben Cluster, außer Tagesdominanz ist begründet.
- Mindestens 2 Nicht-USA/EU-Challenger im Morgenlauf, sofern Quellenlage das hergibt.
- Keine schwache Auslandsmeldung künstlich hochziehen.
- Aber: USA/EU/Big-Tech nicht aus Bequemlichkeit übergewichten.

---

## 12. Source-Verification-Gate

Jede Top Story braucht Source Verification.

Jede Kurzmeldung braucht mindestens:

- tragfähige Quelle oder klar benannte Quellenlage,
- plausibles frisches Delta,
- eng formulierten Claim-Scope,
- sichtbaren Unsicherheitshinweis, wenn Primärquelle oder Zweitanker fehlen.

Ohne Source Verification:

```text
keine Freigabe, Writer darf nicht finalisieren.
```

---

## 13. Writer-Gate

Writer darf nur aus freigegebenem Material schreiben.

Pflicht:

- keine neuen Themen,
- keine Ranking-Änderung,
- keine stärkeren Claims als erlaubt,
- Unsicherheit sichtbar,
- jede Top Story mit konkreter Folge,
- jede Kurzmeldung mit Headline, 2–3 Sätzen Erklärung, Relevanzsatz und Quellen-/Unsicherheitshinweis,
- 15–20 veröffentlichte Meldungen insgesamt, sofern Qualität trägt,
- Watchlist zählt nicht als Ersatz für veröffentlichte Meldungen,
- Makro kurz und erklärend,
- Qualitätshinweis konkret.

Bei Verstoß:

```text
Draft ungültig / Gelb.
```

---

## 14. Adversarial-Review-Gate

Reviewer muss prüfen:

- veröffentlichte Meldungen 15–20,
- Top Stories 5–7 und sichtbar stärker als Kurzmeldungen,
- Kurzmeldungen 8–13 und publikationsfähig,
- Watchlist 3–5 und nicht als Ersatz für echte Meldungen missbraucht,
- falsches Ranking,
- fehlende wichtigere Story,
- konkrete A-/B-Meldungen verdrängt,
- Makro-Budget überschritten,
- fehlende Bürger-/Unternehmensfolge,
- Quelle trägt Claim,
- Claim-Scope eingehalten,
- Reprint-/Anbieter-/KI-Risiken,
- Deutschland-konkret,
- internationale Balance,
- Cluster-Dominanz,
- Watchlist-Nutzen,
- Rollenvermischung.

Status:

```text
Grün = intern testfreigabefähig
Gelb = Korrektur nötig, keine Freigabe
Rot = nicht freigabefähig
```

---

## 15. Korrekturschleifen-Gate

Bei Gelb/Rot:

- Korrekturticket erstellen,
- zuständige Rolle korrigiert,
- Reviewer prüft erneut.

Ohne Re-Review:

```text
keine Freigabe.
```

---

## 16. Qualitätslog-Gate

Nach finalem Status:

- Qualitätslog erstellen,
- Konkretheitsmix dokumentieren,
- Makro-Budget dokumentieren,
- stärkste Schwäche dokumentieren,
- 1–3 konkrete Verbesserungen für nächsten Lauf.
