# Paperclip-Rollen und Skill-Zuordnung – relevant-news V1.8

Diese Datei beantwortet die praktische Frage: Welche Mitarbeiter/Rollen sollen in Paperclip angelegt werden und welche Skills braucht wer?

---

## 1. Grundsatz

Die Qualität steigt nicht dadurch, dass ein einzelner Agent mehr Regeln liest. Die Qualität steigt dadurch, dass verschiedene Rollen unterschiedliche Fehler finden.

```text
Eine Rolle darf nicht gleichzeitig Recherche, finale Auswahl, Textproduktion und Review übernehmen.
```

---

## 2. Managementrollen

| Rolle | Hauptaufgabe | Skills | Darf nicht |
|---|---|---|---|
| `CEO` | Firmenführung, Ziel, Statusabnahme | Aufgaben beauftragen, Status lesen | Ranking, Schreiben, Review, Gelb überstimmen |
| `CMO` | News-Abteilungsleiter / Control Tower | Aufgaben verteilen, Artefakte prüfen, Handoffs, Statusbericht | selbst Review ersetzen, Gelb freigeben, operative Inhalte nach Geschmack ändern |
| `CTO` | technisches Setup, Mail, Automation, Fehlerbehebung | Paperclip-Konfiguration, Mail, Automatisierung, Dateien | redaktionelles Review, Ranking, Briefing schreiben |

---

## 3. Spezialrollen unter dem CMO

| Mitarbeiter | Hauptaufgabe | Wichtigste Skills | Darf nicht |
|---|---|---|---|
| `relevant-news Scout` | breit suchen, Longlist, Quellen sammeln | Websuche, aktuelle Nachrichten, Quellen sammeln, Datei schreiben | Top Stories final entscheiden, Briefing schreiben, freigeben |
| `relevant-news Ranking Editor` | harte Auswahl, Score, Score-Caps, Challenger | Analyse, Ranking, Tabellen, Quellen lesen | fertiges Briefing schreiben, Review freigeben |
| `relevant-news Source Verifier` | Claims gegen Quellen prüfen | Websuche, Quellenlesen, Primärquellensuche | Ranking entscheiden, Briefing schreiben, Review ersetzen |
| `relevant-news Briefing Writer` | kompaktes Briefing schreiben | Schreiben, Kürzen, Strukturieren, Datei lesen | neue Meldungen recherchieren, Quellenclaims verstärken, freigeben |
| `relevant-news Adversarial Reviewer` | Fehler finden, blockieren, Korrektur verlangen | Quellenprüfung, Kritik, Ranking-Review, Webcheck | Briefing selbst schreiben, eigene Fehler absegnen |
| `relevant-news Quality Analyst` optional | Testläufe auswerten, Verbesserungen ableiten | Evaluation, Qualitätslog, Mustererkennung | Tagesbriefing freigeben |

---

## 4. Skill-Zuordnung im Detail

### CEO

Aktivieren:

- Aufgaben beauftragen,
- Management-Status lesen,
- strategische Verbesserungen anstoßen.

Nicht nutzen:

- Websuche für operative News-Auswahl,
- Review,
- Mailversand,
- Ranking.

---

### CMO

Aktivieren:

- Dateien lesen,
- Aufgaben an Rollen verteilen,
- Handoff-/Artefaktstatus prüfen,
- Workflow-Status dokumentieren,
- Korrekturtickets zuweisen.

Nicht nutzen:

- operative Recherche als Ersatz für Scout,
- Ranking-Entscheidung als Ersatz für Ranking Editor,
- Quellenprüfung als Ersatz für Source Verifier,
- Review ersetzen,
- Gelb/Rot freigeben,
- Technik konfigurieren.

Output:

- Arbeitsauftrag an Spezialrollen,
- Handoffs,
- CMO-Control-Board,
- Management-Status an CEO,
- ggf. Aufgaben an CTO für technische Korrekturen.

---

### CTO

Aktivieren:

- Rollen technisch anlegen,
- Skills konfigurieren,
- Dateistruktur prüfen,
- Mail/Automation technisch vorbereiten,
- technische Fehler beheben.

Nicht nutzen:

- Quelleninhalt bewerten,
- Ranking entscheiden,
- Review machen,
- Briefing schreiben.

---

### News Scout

Aktivieren:

- Websuche / Browsing / Recherche,
- Zugriff auf aktuelle Nachrichtenquellen,
- Datei-/Markdown-Erstellung,
- Quellen sammeln.

Output:

- `Kandidatenliste_YYYY-MM-DD_[Slot]_V1_8.md`
- `Quellenbasis_YYYY-MM-DD_[Slot]_V1_8.md`

---

### Ranking Editor

Aktivieren:

- Lesen der Kandidatenliste,
- Analyse/Ranking,
- Tabellen/Scorecard,
- Score-Cap-/Kill-Switch-Prüfung,
- Cluster-/Regionen-Budget-Prüfung,
- optional Webcheck bei strittigen Claims.

Output:

- `Shortlist_Scorecard_YYYY-MM-DD_[Slot]_V1_8.md`
- `Claim_Ledger_YYYY-MM-DD_[Slot]_V1_8.md`
- `Watchlist_YYYY-MM-DD_[Slot]_V1_8.md`

---

### Source Verifier

Aktivieren:

- gezielte Quellenprüfung,
- Primärquellensuche,
- Reprint-/Originalprüfung,
- Claim-Scope-Prüfung,
- Timing-/Datumsprüfung.

Output:

- `Source_Verification_YYYY-MM-DD_[Slot]_V1_8.md`

---

### Briefing Writer

Aktivieren:

- Lesen freigegebener Kandidatenliste,
- Lesen Quellenbasis,
- Lesen Claim-Ledger,
- Lesen Source Verification,
- Schreiben/Kürzen,
- Markdown-Ausgabe.

Output:

- `Briefing_Draft_YYYY-MM-DD_[Slot]_V1_8.md`

---

### Adversarial Reviewer

Aktivieren:

- Lesen aller Artefakte,
- Web-/Quellenprüfung,
- kritische Bewertung,
- Korrekturanweisung,
- Fehler-Taxonomie.

Output:

- `Adversarial_Review_YYYY-MM-DD_[Slot]_V1_8.md`
- bei Gelb/Rot: `Korrekturticket_YYYY-MM-DD_[Slot]_V1_8.md`

---

## 5. Nicht kombinieren

```text
Writer + Reviewer
Ranking Editor + finaler Reviewer
CEO + Reviewer
CMO + Reviewer
CTO + Reviewer
```

---

## 6. Empfohlenes Minimal-Setup

Für den ersten Testlauf:

1. CMO koordiniert.
2. Scout recherchiert.
3. Ranking Editor entscheidet Shortlist.
4. Source Verifier prüft Claims.
5. Writer schreibt.
6. Reviewer widerspricht.
7. CMO meldet Status an CEO.
8. CTO bleibt Technik.


---

## 7. V1.8-Spezialanforderungen

Damit die Briefings weniger makro-/datenlastig werden, müssen diese Rollen die folgenden Zusatzfähigkeiten aktiv nutzen:

| Rolle | Zusatzanforderung V1.8 |
|---|---|
| Scout | gezielt konkrete A-/B-Kandidaten finden: Beschlüsse, Vollzug, Urteile, Fristen, Förderungen, reale Ereignisse |
| Ranking Editor | Konkretheitsklasse A/B/C/D vergeben und maximal 1 Makro-/Daten-/Markt-Top-Story zulassen |
| Source Verifier | prüfen, ob etwas wirklich beschlossen/passiert ist oder nur berichtet/geplant/als Datenpunkt vorhanden ist |
| Writer | je Top Story „Was ist entschieden/passiert“ und „Konkrete Folge“ formulieren |
| Reviewer | Makro-Budget, Konkretheitsmix und verdrängte A-/B-Kandidaten prüfen |
| CMO | Handoff stoppen, wenn konkrete Kandidaten fehlen oder Makro dominiert |
| CTO | keine redaktionelle Qualitätsbewertung, nur technische Umsetzung |

```text
Makro ist Kontext. Konkrete Entscheidungen und reale Ereignisse sind der Kern.
```
