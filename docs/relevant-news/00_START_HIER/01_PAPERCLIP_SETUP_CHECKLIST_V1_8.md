# Paperclip-Setup-Checkliste – relevant-news V1.8

Diese Checkliste richtet die V1.8-Struktur so ein, dass Managementrollen und redaktionelle Spezialrollen getrennt bleiben und das Briefing nicht wieder makro-/datenlastig wird.

---

## 1. Zielbild

```text
CEO
└── CMO / News-Abteilungsleiter / Control Tower
    ├── relevant-news Scout
    ├── relevant-news Ranking Editor
    ├── relevant-news Source Verifier
    ├── relevant-news Briefing Writer
    └── relevant-news Adversarial Reviewer

CTO = technische Umsetzung quer dazu: Paperclip-Setup, Mail, Automatisierung, technische Fehler.
```

---

## 2. Bestehende Rollen aktualisieren

### CEO

```text
01_KI_MITARBEITER/01_CEO_COMPANY_LEAD_PROMPT_V1_8.md
```

CEO ist nicht Ranking Editor, nicht Reviewer, nicht Writer.

### CMO

```text
01_KI_MITARBEITER/02_CMO_NEWS_DIRECTOR_PROMPT_V1_8.md
```

CMO ist Control Tower. Er koordiniert Spezialrollen, prüft Handoffs und stoppt bei Gate-Verstößen. Er ersetzt die Spezialrollen nicht. In V1.8 stoppt er auch, wenn konkrete Entscheidungen fehlen oder Makro zu stark dominiert.

### CTO

```text
01_KI_MITARBEITER/03_CTO_TECH_OPS_PROMPT_V1_8.md
```

CTO ist kein redaktioneller Reviewer. Er prüft nicht, ob die News-Auswahl gut ist.

---

## 3. Spezialrollen unter dem CMO anlegen

Lege in Paperclip diese zusätzlichen KI-Mitarbeiter an:

1. `relevant-news Scout`
2. `relevant-news Ranking Editor`
3. `relevant-news Source Verifier`
4. `relevant-news Briefing Writer`
5. `relevant-news Adversarial Reviewer`

Optional später:

6. `relevant-news Quality Analyst`

Prompts:

```text
01_KI_MITARBEITER/10_NEWS_SCOUT_PROMPT_V1_8.md
01_KI_MITARBEITER/11_RANKING_EDITOR_PROMPT_V1_8.md
01_KI_MITARBEITER/12_SOURCE_VERIFIER_PROMPT_V1_8.md
01_KI_MITARBEITER/13_BRIEFING_WRITER_PROMPT_V1_8.md
01_KI_MITARBEITER/14_ADVERSARIAL_REVIEWER_PROMPT_V1_8.md
01_KI_MITARBEITER/15_OPTIONAL_QUALITY_ANALYST_PROMPT_V1_8.md
```

---

## 4. Skill-Zuordnung

Nutze:

```text
00_AKTIVE_STEUERUNG/PAPERCLIP_ROLLEN_UND_SKILLS_V1_8.md
```

Kurzfassung:

- Scout: Websuche, Quellen, Dateien, konkrete Entscheidungen finden.
- Ranking Editor: Analyse, Score, Konkretheitsklassen, Makro-Budget, Cluster-/Regionen-Gate.
- Source Verifier: Quellenprüfung, Primärquellen, Claim-Scope, Verb-Ladder, Beschluss-/Vollzugsstatus.
- Writer: Schreiben/Kürzen, konkrete Folgen formulieren, keine Recherche.
- Reviewer: kritische Prüfung, Fehlercodes, Makro-/Konkretheits-Gate, Tickets.
- CMO: Handoffs, Status, Stopps.
- CTO: Technik.

---

## 5. Rollentrennung prüfen

Nicht kombinieren:

```text
Writer + Reviewer
Ranking Editor + finaler Reviewer
CEO + Reviewer
CMO + Reviewer
CTO + Reviewer
```

---

## 6. Aktiven Kontext begrenzen

Nur laden:

```text
relevant-news-v1.8
```

Nicht parallel laden:

```text
alte Briefings
alte Reviews
alte Versandlogs
V1.2/V1.3/V1.4/V1.5/V1.6/V1.7
```

---

## 7. V1.8-Gates aktiv prüfen

Vor dem ersten Testlauf müssen diese Dateien in den passenden Rollen bekannt sein:

```text
04_RULES/KONKRETE_ENTSCHEIDUNGEN_UND_BUERGERNUTZEN_GATE_V1_8.md
04_RULES/MAKRO_BUDGET_UND_DATEN_DISZIPLIN_GATE_V1_8.md
04_RULES/MAKRO_KONTEXT_GATE_V1_8.md
00_AKTIVE_STEUERUNG/SCORE_CAPS_UND_KILL_SWITCHES_V1_8.md
```

---

## 8. Setup validieren

Vor dem ersten Testlauf:

```text
00_START_HIER/08_SETUP_VALIDIERUNG_VOR_TESTLAUF_V1_8.md
```

Wenn Setup nicht bestanden ist, keinen News-Testlauf starten.
