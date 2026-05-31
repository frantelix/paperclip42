# Setup Validation – [Datum] – V1.8

## Ergebnis

**Setup-Status:** bestanden / nicht bestanden

---

## Rollenprüfung

| Rolle | angelegt? | richtiger Prompt? | richtige Skills? | Problem |
|---|---|---|---|---|
| CEO | ja/nein | ja/nein | ja/nein | ... |
| CMO | ja/nein | ja/nein | ja/nein | ... |
| CTO | ja/nein | ja/nein | ja/nein | ... |
| relevant-news Scout | ja/nein | ja/nein | ja/nein | ... |
| relevant-news Ranking Editor | ja/nein | ja/nein | ja/nein | ... |
| relevant-news Source Verifier | ja/nein | ja/nein | ja/nein | ... |
| relevant-news Briefing Writer | ja/nein | ja/nein | ja/nein | ... |
| relevant-news Adversarial Reviewer | ja/nein | ja/nein | ja/nein | ... |

---

## Rollentrennung

| Check | Status |
|---|---|
| Writer und Reviewer getrennt | ja/nein |
| CTO nicht redaktioneller Reviewer | ja/nein |
| CEO nicht Ranking/Review | ja/nein |
| CMO nicht operativer Writer/Reviewer | ja/nein |
| Reviewer darf Gelb/Rot setzen | ja/nein |

---

## V1.8-Regelprüfung

| Check | Status |
|---|---|
| Nur `relevant-news-v1.8` aktiv geladen | ja/nein |
| Konkretheits-Gate geladen | ja/nein |
| Makro-Budget-Gate geladen | ja/nein |
| Score-Caps/Kill-Switches geladen | ja/nein |
| Scout muss A-/B-Kandidaten suchen | ja/nein |
| Ranking Editor hat maximal 1 Makro-Top-Regel | ja/nein |
| Writer muss konkrete Folge je Top Story nennen | ja/nein |
| Reviewer muss Makro-Budget und Konkretheitsmix prüfen | ja/nein |
| Versand/Automation deaktiviert | ja/nein |

---

## Entscheidung

```text
Wenn alle Kernchecks ja: Testlauf darf starten.
Wenn ein Kerncheck nein: Setup korrigieren, kein Testlauf.
```

---

## Offene Setup-Korrekturen

1. ...
2. ...
3. ...
