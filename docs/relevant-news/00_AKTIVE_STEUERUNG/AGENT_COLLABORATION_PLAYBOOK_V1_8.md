# Agent Collaboration Playbook V1.8

## Controlled Recovery Swarm

Nutzen bei:

- Agent status error.
- Stalled issue.
- Degraded probe.
- Unclear terminal state.
- Adapter-, Shell-, Sandbox- oder Permission-Problem.

Ablauf:

1. CMO prueft Scope, Status und fachliche Vollstaendigkeit.
2. CMO stoppt fachfremde Folgearbeit.
3. CTO prueft technische Ursache read-only, bevor Settings veraendert werden.
4. Betroffener Agent fuehrt nur einen isolierten Probe aus.
5. CMO dokumentiert Terminalentscheidung.

Erlaubte Terminalstatus:

- `recovered_clean`
- `recovered_degraded_followup`
- `blocked_runtime_issue`
- `blocked_config_issue`
- `blocked_permission_issue`
- `no_action_stale_status_only`

## Editorial Production Chain

Normale redaktionelle Produktion bleibt:

Scout -> Ranking Editor -> Source Verifier -> Briefing Writer -> Adversarial Reviewer -> Quality Analyst/CMO.

Regeln:

- CMO koordiniert, ersetzt keine Spezialrolle.
- CTO bleibt Technik.
- CEO priorisiert und nimmt Status entgegen, ersetzt aber Ranking/Review nicht.
- Versand bleibt separat gegatet.

## Technical Recovery Chain

Technische Recovery laeuft:

CMO -> CTO -> betroffener Agent-Probe.

CTO prueft:

- Runtime API.
- Adapter-Konfiguration.
- Shell-/Process-Execution.
- Sandbox/Bypass.
- Permissions.
- lokale Workspace-Faehigkeit.

Bypass/Sandbox:

- nur explizit,
- nur mit Zweck,
- nur mit Risiko-Hinweis,
- nur mit Rueckrollplan.
- nach Recovery immer per Live-Read verifizieren,
- wenn noch aktiv: `bypass_still_enabled_needs_decision`.
- darf nach Recovery nicht stillschweigend aktiv bleiben.
- Abschlussstatus `recovered_clean` erst nach Bypass `false` oder dokumentierter Ausnahmeentscheidung.
- Bei Bypass-Reset keine neuen Probes erzwingen, sofern Postcheck ausreichend ist.

Historische Run-Fehler:

- Alte Adapter-/Auth-Fehler duerfen nach Modell- oder Adaptermigration nicht als aktueller Fehler der neuen Runtime gelesen werden.
- Fuer den aktuellen Zustand zaehlen neue Runs mit aktueller Adapter-/Modell-Evidenz und ein read-only Agent-Config-Read.

## Versandgrenzen

Recovery gibt nie Versandfreigabe.

Immer verboten in Recovery:

- SMTP.
- Send-Preview.
- echter Send.
- Empfaengerableitung.
- Daily-Briefing-Kette.
- Versandpfade aus alten Versionen.

## Exit-Status

Jeder Recovery-Task braucht vor Start ein Terminalkriterium.

Gute Beispiele:

- Probe antwortet mit festen Feldern.
- Shell-only Check liest genau einen erlaubten Pfad.
- Config-Read bestaetigt Zielwerte.
- Recovery endet als blocked mit konkretem Owner.

Schlechte Beispiele:

- "Pruefe mal, ob alles geht."
- "Starte den Agenten nochmal."
- "Mach weiter, bis es funktioniert."

## Anti-Patterns

- Retry alter Runs ohne Kontext.
- Heartbeat als Diagnose-Default.
- CEO/CTO als redaktioneller Reviewer-Ersatz.
- Writer mit Search bei sendbarem Draft.
- Recovery ohne Terminalstatus.
- Bypass aktiv lassen ohne Follow-up.
- Bypass-Reset ohne separate Entscheidung und Verifikation.
- Technischen Erfolg als Versandfreigabe lesen.
- Alte Run-Fehler als aktuelle Agent-Konfiguration interpretieren.
- DB-Direktaenderung zur Statuskosmetik.
