# Clean-Import-Staging-Plan - Relevant News V1.8

Status: freigegebener Staging-Plan fuer PR 1.

## Ziel

`docs/relevant-news` wird als sauberes Paperclip-Package getrackt. Der PR importiert aktiven Kontext, nicht den forensischen Arbeitsdump aus Recovery-, Runtime-, Send- oder Laufartefakten.

## Aktiv zu stagen

- `docs/relevant-news/.paperclip.yaml`
- `docs/relevant-news/COMPANY.md`
- `docs/relevant-news/MANIFEST_V1_8.md`
- `docs/relevant-news/AGENTS.md`
- `docs/relevant-news/00_AKTIVE_STEUERUNG/*`
- `docs/relevant-news/00_START_HIER/*` nach Markierung von `03` und `04` als derived/non-canonical
- `docs/relevant-news/01_KI_MITARBEITER/*`
- `docs/relevant-news/02_TEMPLATES/*`
- `docs/relevant-news/03_WORKFLOW/*`
- `docs/relevant-news/04_RULES/*`
- `docs/relevant-news/05_EVALUATION/*`
- `docs/relevant-news/20_LAUFARTEFAKTE/README_OUTPUTS_HIER_ABLAGEN_V1_8.md`
- `docs/relevant-news/agents/*/AGENTS.md`
- `docs/relevant-news/projects/relevant-news/PROJECT.md`
- `docs/relevant-news/skills/*/SKILL.md`
- `docs/relevant-news/tasks/*/TASK.md`
- `scripts/relevant-news/repo_audit.py`
- `.gitignore`

## Reference-only

- `docs/relevant-news/00_AKTIVE_STEUERUNG/LEGACY_GMX_SEND_REFERENCE_V1_8.md` wird nur als verbotene Legacy-Referenz aufgenommen. Sie ist keine aktive Versandfreigabe und kein V1.8-Send-Pfad.

## Nicht zu stagen

- Root-Level `NEW-*.md`, `SCOUT-PROBE-*.md`, `2026-05-*.md`, `Claim_Ledger_*.md`, `06_source_verification_*.md`
- non-empty Laufartefakte unter `20_LAUFARTEFAKTE`, ausser der README
- Recovery-Notizen, Runlogs, Send-Logs, Runtime-Exports, `_LATEST`
- `06_BEISPIELE`, `04_Arbeitslaeufe`, `99_NOTIZEN` ausser diesem Plan
- bestehende Send-, SMTP-, Empfaenger-, Runtime- oder Schedule-Implementierung

## Aktiver Vertrag

- Morgenbriefing: 15-20 veroeffentlichte Meldungen
- Top Stories: 5-7
- Kurzmeldungen: 8-13
- Watchlist: 3-5
- Maximal 1 Makro-/Daten-/Markt-Top-Story
- Kein Auffuellen ohne Qualitaet

## Acceptance

- `git diff --cached --name-only -- docs/relevant-news | sort` zeigt nur freigegebenen aktiven Kontext plus bewusst freigegebene Reference-only-Dateien.
- Artefakt-Grep gegen den staged diff zeigt hoechstens `20_LAUFARTEFAKTE/README_OUTPUTS_HIER_ABLAGEN_V1_8.md`.
- `scripts/relevant-news/repo_audit.py` laeuft ohne Netzwerkzugriff und blockiert versehentliche Artefakt-Imports.
