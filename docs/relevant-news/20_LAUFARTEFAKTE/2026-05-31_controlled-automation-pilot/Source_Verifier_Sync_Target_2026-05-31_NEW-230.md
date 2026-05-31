# Source Verifier Sync Target

Datum: 2026-05-31
Bezug: `NEW-216` blocked on `NEW-230`
Zweck: enger Sync-Target-Handoff fuer die finale Packet-Konsistenz

## Aktueller Stand

Die inhaltliche Re-Review ist in `R3` bereits eng genug:
- `K1` pass
- `K2` pass
- `K3` pass
- `K10` hold
- `K12` raus

`NEW-216` bleibt trotzdem geblockt, weil der erforderliche Run-Ordner noch keine eindeutige, selbstkonsistente Source-Verifier-Endfassung traegt.

## Konkreter Konflikt

- Die autoritative finale Source-Verifier-Grenze lebt aktuell nicht sauber im Run-Packet selbst.
- Im Run-Ordner liegt weiterhin eine aeltere, konfliktfaehige Datei: `06_source_verification_2026-05-31_Morgenbriefing_V1_8.md`.
- Solange diese Run-Ordner-Fassung nicht mit der finalen Boundary synchronisiert oder klar supersediert ist, bleibt die Packet-Spur auditierbar unklar.

## Was NEW-230 exakt liefern muss

Der Run-Ordner muss nach Abschluss von `NEW-230` fuer einen Auditor aus sich selbst heraus klar lesbar machen:

1. `K1`, `K2` und `K3` sind source-verifier-seitig freigegeben.
2. `K10` ist nicht freigegeben, sondern hold.
3. `K12` ist nicht nur abgeschwaecht, sondern aus der finalen Story-Menge entfernt.
4. Es gibt im Run-Ordner keine aeltere `06_source_verification...`-Fassung mehr, die diesen Stand widerspricht oder verwischt.

## Nicht ausreichend fuer den Unblock

- Eine richtige Endfassung nur am Repo-Root.
- Eine neue Endfassung im Run-Ordner, waehrend die alte `06_source_verification...` dort weiter als gleichrangige Gegenfassung stehen bleibt.
- Eine Endfassung, die `K10` oder `K12` wieder uneindeutig macht.

## Closure-Gate fuer NEW-216

Wenn `NEW-230` den obigen Sync abgeschlossen hat, braucht `NEW-216` keine neue breite Inhaltspruefung mehr. Dann reicht eine kurze Abschluss-Re-Review mit engem Scope:

- Stimmen Run-Ordner und finale Boundary ueberein?
- Ist `K10` klar hold?
- Ist `K12` klar raus?
- Gibt es keine konkurrierende aeltere Source-Verification mehr im Packet?

Erst dann kann die Gelb-Entscheidung sauber gegen Gruen neu bewertet werden.
