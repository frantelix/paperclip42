# Organisation und Rollentrennung – relevant-news V1.8

Diese Datei ist das wichtigste Organisations-Gate für V1.8.

---

## 1. Organisationsprinzip

```text
Management steuert.
CMO koordiniert als Control Tower.
Spezialrollen arbeiten.
Reviewer widerspricht.
Technik versendet nur nach Freigabe.
```

---

## 2. Rollenebenen

### Ebene 1: CEO

- Oberchef der Firma.
- Setzt Ziel und Rahmen.
- Beauftragt den CMO.
- Bekommt Management-Status.
- Greift nicht in Ranking, Text oder Review ein.

### Ebene 2: CMO

- News-Abteilungsleiter / Control Tower.
- Verantwortlich für Prozess, Rollen, Handoffs und Artefakte.
- Koordiniert Spezialrollen.
- Nimmt nur den Prozess nach Reviewer-Grün intern ab.
- Ersetzt keine operative Spezialrolle.

### Ebene 3: News-Spezialrollen

- Scout recherchiert.
- Ranking Editor priorisiert.
- Source Verifier prüft Claims.
- Writer schreibt.
- Adversarial Reviewer blockiert bei Fehlern.

### Technische Querschnittsrolle: CTO

- Richtet Paperclip, Skills, Mail und Automation ein.
- Kein redaktioneller Reviewer.
- Kein Ranking Editor.
- Kein Writer.

---

## 3. Harte Trennungsregeln

Nicht erlaubt:

```text
CEO = Reviewer
CEO = Ranking Editor
CMO = Adversarial Reviewer
CMO = Ranking Editor
CMO = Briefing Writer
CTO = Adversarial Reviewer
Writer = Reviewer
Ranking Editor = Reviewer
Scout = Writer ohne Ranking-Gate
```

Erlaubt nur im Ausnahmefall:

```text
Ranking Editor + vorbereitende Claim-Prüfung
```

Aber nur, wenn ein sichtbares Claim-Ledger entsteht und der Source Verifier oder Adversarial Reviewer danach unabhängig prüft.

---

## 4. Freigabeprinzip

```text
Grün vom Adversarial Reviewer + vollständige Pflichtartefakte = intern testfreigabefähig.
Gelb = Korrektur nötig, keine Freigabe.
Rot = Lauf stoppen oder neu aufsetzen.
```

CMO darf bei Grün einen Status an den CEO melden. CMO darf Gelb/Rot nicht in Grün umdeuten. CEO darf Gelb/Rot nicht per Bauchgefühl überstimmen.

---

## 5. Warum diese Regel wichtig ist

Die schlechte Qualität früherer Läufe entstand nicht primär durch fehlende Regeln, sondern dadurch, dass eine Rolle zu viel gleichzeitig tat:

- Themen finden,
- Auswahl rechtfertigen,
- Briefing schreiben,
- eigene Auswahl prüfen,
- Freigabe erteilen.

V1.8 verhindert genau diese Selbstbestätigung und macht die CMO-Rolle klar: führen, nicht selbst operativ produzieren.
