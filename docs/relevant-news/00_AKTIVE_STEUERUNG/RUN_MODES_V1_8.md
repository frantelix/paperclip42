# Run Modes – relevant-news V1.8

Vor jedem Lauf muss klar sein, welche Art von Output erzeugt wird. Viele schwache Ausgaben entstehen, weil Morgenbriefing, Delta-Update und No-Update vermischt werden.

V1.8 ergänzt: Viele schwache Ausgaben entstehen auch, wenn Daten-/Makro-/Marktbewegungen konkrete Entscheidungen verdrängen.

---

## RN-SCHEDULE-SEND-01 Zusatz - Regel-Send-Anlaesse

Stand 2026-05-31 sind drei Regel-Anlaesse fuer den lokalen Operator-Testbetrieb als echte Send-Kandidaten erlaubt:

- `scheduled_morning`: Vollbriefing um 05:30 Europe/Berlin.
- `scheduled_midday`: Delta-Update um 11:30 Europe/Berlin.
- `scheduled_evening`: Tagesabschluss um 18:30 Europe/Berlin.

Die fruehere No-Send-Default-Annahme aus RN-MAIL-01 war Design-Scope und ist fuer diese drei Operator-Test-Slots ueberholt. Die redaktionellen Gates bleiben bestehen. `actualSend=true` ist nur ueber `scripts/relevant-news/send-briefing-mail.py` erlaubt und nur mit `recipientCount=1`, passendem finalem Slot-Mailtext, Duplicate-Schutz und sanitisierten Logs.

## 1. Morgenbriefing

Zweck:

- Tagesstart,
- breiter Scan,
- 15-20 veröffentlichte Meldungen,
- 5-7 Top Stories,
- 8-13 weitere relevante Meldungen als Kurzmeldungen,
- 3-5 Watchlist-Themen,
- sehr kurzer Makro-Kontext,
- Qualitätshinweis.

Pflicht:

- 40-60 gesichtete Kandidaten/Leads im Candidate Pool,
- 25-35 ernsthafte Longlist-Kandidaten,
- 15-20 publikationsfähige Tier-A-/Tier-B-Kandidaten,
- internationaler Scan,
- Konkret-Scan,
- Konkretheitsklasse A/B/C/D je Kandidat,
- mindestens 5 Challenger,
- mindestens 3 A-/B-Challenger, sofern Quellenlage das hergibt,
- Claim-Ledger,
- Source Verification,
- adversariales Review.

Nicht tun:

- 20 Meldungen erzwingen, wenn die Qualität nicht trägt,
- alte News wiederholen,
- Makroblock zur Top-Story aufblasen, wenn kein neues Delta vorliegt,
- mehr als 1 Makro-/Daten-/Markt-Top-Story ohne Ausnahme,
- konkrete A-/B-Meldungen zugunsten bequemer Datenmeldungen verdrängen.

Watchlist und Makro-Kontext zählen nicht als veröffentlichte Meldung. Wenn weniger als 15 Meldungen publikationsfähig sind, bleibt das Briefing unter 15 und der Qualitätslog nennt den Grund.

---

## 2. Delta-Update / Mittag / Abend

Zweck:

- nur echte neue Deltas seit dem letzten Briefing,
- keine Wiederholung des Morgens.

Echtes Delta:

- Entscheidung,
- offizielle Bestätigung,
- harte neue Datenveröffentlichung mit konkreter Folge,
- Eskalation/Deeskalation,
- Urteil/Beschluss/Vollzug,
- konkrete Markt-, Kosten-, Regulierungs- oder Sicherheitsfolge.

Kein echtes Delta:

- neue Reaktion,
- Kommentar,
- erwarteter Termin,
- Artikel mit gleicher Faktenlage,
- Preis-/Index-Tick ohne neue reale Ursache,
- Anbieter-PR ohne Praxiswert.

---

## 3. No-Update

Zweck:

- transparent sagen, dass kein relevantes Update vorliegt.

No-Update ist ein Qualitätsmerkmal, kein Scheitern.

No-Update wählen, wenn:

- keine echten Deltas,
- nur schwache Reprints,
- nur Erwartung/Vorfeld,
- nur Daten-/Marktbewegung ohne konkrete Folge,
- keine Quelle trägt einen starken Claim.

---

## 4. Review-only

Zweck:

- bestehende Ausgabe kritisch prüfen.

Output:

- Review,
- Fehlercodes,
- Korrekturticket,
- keine neue Ausgabe, außer explizit beauftragt.

---

## 5. Setup-/Trockenlauf

Zweck:

- Rollen und Gates testen, ohne vollständiges Briefing.

Gute erste Tests:

1. Nur Scout-Longlist.
2. Nur Ranking-Scorecard.
3. Nur Reviewer auf einem alten Beispiel.
4. Voller Lauf ohne Versand.

---

## Rollenregel V1.8

Der CMO wählt und koordiniert den Run Mode als Control Tower. Der CEO kann den Rahmen setzen, entscheidet aber nicht operativ über Ranking oder Review. Der CTO wird nur bei technischen Run Modes oder technischen Folgeaufgaben eingesetzt.

---

## V1.8-Zusatz

Bei jedem Run Mode mit Top Story oder Delta-Claim gilt: Source Verification ist Pflicht. Bei No-Update reicht eine kurze Quellen-/Delta-Notiz.

Bei jedem Run Mode mit Top Stories gilt:

```text
Konkrete Folge prüfen.
Makro-Budget prüfen.
```
