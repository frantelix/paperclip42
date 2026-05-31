---
name: Paperclip Tech Ops
slug: paperclip-tech-ops
description: Unterstützt lokale Paperclip-Setup-Prüfung für Relevant News ohne DB-, Seed-, API- oder Automationseingriffe.
---

# Paperclip Tech Ops

## Zweck

Hilft, das lokale Company-Package, Rollen, Skill-Zuordnung und Setup-Artefakte technisch sauber und importnah zu halten.

## Wann verwenden?

Wenn der CTO Package-Struktur, lokale Testfähigkeit, Rollenanlage oder technische Blocker prüft.

## Vorgehen

1. Package-Dateien und Slugs gegen agentcompanies/v1-Konventionen prüfen.
2. Rollen, `reportsTo` und Skill-Referenzen gegen vorhandene Dateien abgleichen.
3. Keine Secrets, Provider-Konfigurationen, Schedules oder lokalen absoluten Pfade ergänzen.
4. Bei Importfragen einen Dry-Run-Vorschlag formulieren statt API-Calls auszuführen.
5. Technische Blocker knapp mit Besitzer und nächstem Schritt melden.

## Harte Stop-/Fail-Kriterien

- DB-, Seed- oder API-Dateien sollen geändert werden.
- Eine Routine, Automation oder ein Versand wird aktiviert.
- ZIP-Dateien sollen geöffnet, entpackt, gelöscht oder verändert werden.
- Provider-Secrets oder maschinenlokale Runtime-Pfade werden verlangt.

## V1.8-Referenzen

- `00_START_HIER/01_PAPERCLIP_SETUP_CHECKLIST_V1_8.md`
- `00_START_HIER/08_SETUP_VALIDIERUNG_VOR_TESTLAUF_V1_8.md`
- `03_WORKFLOW/PAPERCLIP_ISSUE_ROLLENSETUP_UND_TESTLAUF_V1_8.md`
