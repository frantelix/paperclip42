# Score-Caps und Kill-Switches – relevant-news V1.8

Score-Caps verhindern, dass ein Agent schwache Meldungen durch gute Sprache „hochscoren" kann.

V1.8 ergänzt eine zentrale Priorität:

```text
Konkrete Entscheidungen, Ereignisse und Bürger-/Unternehmensfolgen schlagen abstrakte Makrodaten.
```

---

## 1. Mini-Score

Maximal 10 Punkte:

1. Delta/Neuheit: 0–2
2. Tragweite: 0–2
3. Quellenstärke: 0–2
4. konkrete Bürger-/Unternehmensfolge: 0–2
5. Sicherheit: 0–2

Regel:

- 8–10: Top-Story-fähig, wenn kein Kill-Switch.
- 7: nur mit Zusatzbegründung und Challenger-Sieg.
- 6–7: Kurzmeldungs-fähig, wenn Quelle, Frische und enger Claim-Scope tragen.
- 0–5: keine veröffentlichte Meldung, außer eng als Kontext/Watchlist begründet.

---

## 2. Konkretheitsklassen

| Klasse | Bedeutung | Default |
|---|---|---|
| A | Entscheidung/Vollzug/Rechts-/Kostenfolge | Top-fähig |
| B | konkretes Ereignis mit realer Folge | Top-fähig |
| C | Daten/Makro/Markt | Kontext; Top nur als Ausnahme |
| D | Erwartung/Agenda/Kommentar/PR | Watchlist/raus |

Bei vergleichbarer Tragweite gilt:

```text
A vor B vor C vor D.
```

---

## 3. Kill-Switches

Bei Kill-Switch ist Top Story ausgeschlossen.

| Kill-Switch | Folge |
|---|---|
| Quelle trägt Claim nicht | raus oder Claim neu formulieren |
| Verifikationsstatus offen | keine Top Story |
| Keine Source Verification | Writer darf nicht finalisieren |
| Kein neues Delta | Watchlist/raus |
| Reine Erwartung/Vorfeld ohne Folge | Watchlist |
| Starker Claim ohne Primärquelle oder zwei unabhängige tragfähige Quellen | keine Top Story oder eng formulieren |
| Reine Makro-/Marktzahl ohne konkrete Folge | keine Top Story |
| Zweite Makro-/Daten-Top-Story ohne außergewöhnliche Tagesdominanz | herabstufen |
| Writer ergänzt neues Thema | Draft ungültig |
| Reviewer fehlt | keine Freigabe |
| Gelb/Rot ohne Korrekturticket | keine Freigabe |
| CMO/CEO/CTO ersetzt Reviewer | Setup-/Rollenverstoß |

---

## 4. Score-Caps

Score-Caps begrenzen den Maximalwert.

| Schwäche | Maximaler Score |
|---|---:|
| Reprint-only bei starkem Claim | 6 |
| Anbieterangabe ohne Zweitanker | 6 |
| Deutschland-konkret ohne Primäranker | 6 |
| Teilbestätigter Claim | 7 |
| Kein klarer Bürger-/Unternehmensnutzen | 6 |
| Nur Agenda/Vorfeld, aber mit plausibler Relevanz | 6 oder Watchlist |
| Makrozahl ohne konkrete Folge | 5 |
| Öl-/Börsen-/Index-Tick ohne neue reale Ursache | 5 |
| Zweiter ähnlicher Makrodatensatz des Tages | 4 |
| Konkrete A-/B-Challenger nicht geprüft | 6 |
| Keine internationale Gegenprüfung | 7 |
| Mehr als 2 Top Stories gleicher Cluster ohne Tagesdominanz-Begründung | Gelb, Auswahl nacharbeiten |
| Mehr als 1 Makro-/Daten-/Markt-Top-Story ohne Ausnahme | Gelb, Auswahl nacharbeiten |
| Kein Challenger dokumentiert | Auswahl nicht freigeben |

---

## 5. Zusatzbegründung für Score 7

Bei Score 7 braucht der Ranking Editor diesen Satz:

```text
Trotz Score 7 Top Story, weil [außergewöhnliche Tagesrelevanz] und stärker als [Challenger]; konkrete Folge ist [Folge]; Unsicherheit wird so formuliert: [...] .
```

Wenn dieser Satz nicht überzeugt: Watchlist oder raus.

---

## 6. Makro-Exception-Satz

Jede Makro-/Daten-/Markt-Top-Story braucht:

```text
Trotz Makro-Charakter Top Story, weil [konkrete Folge] und stärker als [konkrete A-/B-Challenger].
```

Ohne diesen Satz: Makro-Kontext oder Watchlist.

---

## 7. Kein Auffüllen

Morgenbriefings enthalten 15 bis 20 veröffentlichte Meldungen:

```text
5 bis 7 Top Stories plus 8 bis 13 weitere relevante Kurzmeldungen.
```

Wenn weniger als 15 Meldungen publikationsfähig sind, bleibt es unter 15 und der Qualitätslog nennt den Grund. Wenn mehr als 20 Meldungen publikationsfähig sind, werden die schwächsten B-Items in Watchlist/Hold verschoben. Watchlist zählt nicht als veröffentlichte Meldung.
