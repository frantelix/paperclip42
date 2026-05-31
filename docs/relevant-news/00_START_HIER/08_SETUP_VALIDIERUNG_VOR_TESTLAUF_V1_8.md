# Setup-Validierung vor Testlauf – relevant-news V1.8

Vor dem ersten vollständigen News-Testlauf muss der CMO prüfen, ob die Paperclip-Konstellation wirklich sauber ist.

---

## Pflichtprüfung

| Bereich | Prüffrage | bestanden? |
|---|---|---|
| Aktive Grundlage | Ist nur `relevant-news-v1.8` geladen? | ja/nein |
| CEO | Ist CEO nur Auftraggeber/Oberchef? | ja/nein |
| CMO | Ist CMO Control Tower und nicht operativer Writer/Reviewer? | ja/nein |
| CTO | Ist CTO nur Technik und kein redaktioneller Reviewer? | ja/nein |
| Scout | Ist Scout angelegt und mit Scout-Prompt versehen? | ja/nein |
| Ranking Editor | Ist Ranking Editor angelegt und mit Score-/Konkretheitsregeln versehen? | ja/nein |
| Source Verifier | Ist Source Verifier angelegt und quellenprüfend? | ja/nein |
| Briefing Writer | Ist Writer getrennt vom Reviewer? | ja/nein |
| Adversarial Reviewer | Ist Reviewer getrennt, blockierend und mit Fehlercodes versehen? | ja/nein |
| Konkretheits-Gate | Ist das Gate für konkrete Entscheidungen/Bürgernutzen aktiv? | ja/nein |
| Makro-Budget | Ist maximal 1 Makro-/Daten-Top-Story geregelt? | ja/nein |
| Versand | Ist Versand/Automation im Testlauf deaktiviert? | ja/nein |

---

## Stop-Regel

Wenn eine Kernfrage mit `nein` beantwortet wird:

```text
Keinen News-Testlauf starten.
Erst Setup korrigieren.
```

---

## Minimaler Setup-Output

Nutze:

```text
02_TEMPLATES/SETUP_VALIDATION_TEMPLATE_V1_8.md
```
