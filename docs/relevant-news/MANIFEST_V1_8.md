# Manifest – relevant-news V1.8

## Zweck

V1.8 ist die optimierte Arbeitsgrundlage für die lokale Paperclip-News-Firma Relevant News.

`docs/relevant-news` ist active-context-only: Der Baum enthält nur die ladbaren Regeln, Rollen, Skills, Tasks und Projektdefinitionen. Historische Archive, Laufartefakte, Beispiele, Notizen, Logs und generierte Outputs liegen nicht im aktiven Paperclip-Kontext.

Sie kombiniert:

- CEO als Oberchef,
- CMO als News-Abteilungsleiter / Control Tower,
- CTO als Technikrolle,
- Spezialrollen für operative News-Qualität,
- harte Gates für Ranking, Quellen, Claims, Cluster und Review,
- klare Priorität für konkrete Entscheidungen und reale Ereignisse,
- strenges Makro-/Daten-Budget.

---

## Wichtigste Struktur

```text
CEO = Oberchef.
CMO = News-Abteilungsleiter / Control Tower.
CTO = Technik.
Spezialrollen = operative News-Qualität.
```

---

## Wichtigste V1.8-Ergänzungen

- Konkretheitsklassen A/B/C/D.
- Maximal 1 Makro-/Daten-/Markt-Top-Story pro Morgenbriefing.
- Makro-Kontext maximal 2 Bulletpoints.
- Morgenbriefing-Vertrag: 15-20 veröffentlichte Meldungen, davon 5-7 Top Stories und 8-13 Kurzmeldungen; dazu 3-5 Watchlist-Themen.
- Jede Top Story braucht eine konkrete Bürger-/Unternehmens-/Sicherheitsfolge.
- Scout muss konkrete Entscheidungen und reale Ereignisse aktiv suchen.
- Ranking Editor muss Makro-Ausnahmen begründen.
- Reviewer prüft Konkretheitsmix und Makro-Budget.
- CMO stoppt, wenn Makro dominiert oder konkrete Kandidaten fehlen.

---

## Enthaltene Hauptbestandteile

- Startdateien für Setup und Copy-Paste,
- Management-Prompts,
- Spezialrollen-Prompts,
- Rollen-/Skill-Zuordnung,
- CMO-Control-Tower-Runbook,
- Setup-Validierung,
- Workflow-Runbooks,
- Qualitätsgates,
- Templates,
- Fehler-Taxonomie,
- Regressionstests,
- Review alter Briefings zu Makro-Lastigkeit.

---

## Nicht enthalten / bewusst ausgeschlossen

- alte Briefings als aktive Stilvorlage,
- alte freundliche Reviews als Qualitätsmaßstab,
- öffentlicher Produktivversand,
- ungegatete oder alte automatische Routinen,
- alte V1.2-Mail-Skripte, alte Empfängerableitung und alte Legacy-Send-Pfade,
- CTO als redaktioneller Reviewer,
- CEO als operativer Entscheider,
- CMO als Ersatz-Redakteur,
- Makro-/Datenmeldungen als Standardfüllung,
- historische Archive und Recovery-Notizen,
- Laufartefakte, Versandlogs, Runtime-Exports und generierte Outputs.

---

## Empfohlener nächster Schritt

1. Managementrollen aktualisieren.
2. Spezialrollen unter CMO anlegen.
3. Setup validieren.
4. Redaktionellen Testlauf ohne Versand starten oder einen lokalen V1.8-Operator-Testslot nur nach `TESTVERSAND_GATES_V1_8.md` ausführen.
5. Output ausserhalb von `docs/relevant-news` pruefen und nur aus echten Testlauf-Fehlern weiter optimieren.
