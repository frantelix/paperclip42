# Quellen- und Claim-Scope-Gate – relevant-news V1.8

## Grundsatz

Nicht „Quelle vorhanden“ zählt, sondern:

```text
Die Quelle trägt den konkreten Claim.
```

---

## Quellentypen

| Typ | Bedeutung |
|---|---|
| Primärquelle | Behörde, Regierung, Unternehmen, Gericht, Parlament, Zentralbank, Statistikamt, offizielles Dokument |
| Original | ursprünglicher Medien-/Agenturbericht, nicht sichtbar kopiert |
| Agentur | große Nachrichtenagentur oder klar identifizierter Agenturbericht |
| Fachquelle | spezialisierte, einschlägige Quelle |
| Reprint | Weiterveröffentlichung fremder Meldung |
| Anbieterangabe | Blog, Pressemitteilung, Produktseite eines Anbieters |

---

## Verifikationsstatus

- `bestätigt`: Quelle trägt Claim direkt.
- `teilbestätigt`: Quelle trägt nur Teile oder engeren Scope.
- `offen`: Quelle reicht nicht.

Regel:

```text
Offen darf nicht Top Story sein.
```

---

## Claim-Scope

Für jede Top Story muss klar sein:

- Was trägt die Quelle?
- Was trägt sie nicht?
- Welche Formulierung ist maximal erlaubt?
- Welche Formulierung wäre zu stark?

---

## Reprint-Regel

Reprint-only bei Top Story ist Gelb.

Zulässig nur, wenn:

- Claim eng formuliert ist,
- Original/Primärquelle nicht naheliegend verfügbar ist,
- Reviewer die Schwäche in Datenqualität benennt.

Bei starkem Rechts-, Markt-, Sicherheits- oder Kostenclaim reicht Reprint-only normalerweise nicht.

---

## Beispiele

Nicht erlaubt:

```text
Quelle sagt: Gespräche beginnen.
Briefing sagt: Ergebnis steht fest.
```

Erlaubt:

```text
Quelle sagt: Gespräche beginnen.
Briefing sagt: Gespräche beginnen; Ergebnisse offen.
```
