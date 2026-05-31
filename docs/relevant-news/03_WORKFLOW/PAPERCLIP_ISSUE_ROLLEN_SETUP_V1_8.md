# Paperclip-Issue – Rollen-Setup relevant-news V1.8

## Ziel

Richte die Rollenstruktur für den relevanten News-Workflow sauber ein, bevor der erste Testlauf startet.

---

## Managementrollen aktualisieren

- CEO mit `01_KI_MITARBEITER/01_CEO_COMPANY_LEAD_PROMPT_V1_8.md`
- CMO mit `01_KI_MITARBEITER/02_CMO_NEWS_DIRECTOR_PROMPT_V1_8.md`
- CTO mit `01_KI_MITARBEITER/03_CTO_TECH_OPS_PROMPT_V1_8.md`

---

## Spezialrollen anlegen

- relevant-news Scout
- relevant-news Ranking Editor
- relevant-news Source Verifier
- relevant-news Briefing Writer
- relevant-news Adversarial Reviewer

---

## Zu prüfende Trennung

```text
CEO = Oberchef, keine operative News-Arbeit.
CMO = Control Tower, keine operative Spezialrolle.
CTO = Technik, kein redaktioneller Review.
Reviewer ≠ Writer.
Reviewer ≠ Ranking Editor.
```

---

## Erwarteter Output

- Setup-Validierung nach `02_TEMPLATES/SETUP_VALIDATION_TEMPLATE_V1_8.md`
- kurze technische Notiz des CTO, falls Setup-Probleme behoben wurden

---

## Stop

Kein Morgenbriefing starten, solange Setup-Validierung nicht bestanden ist.
