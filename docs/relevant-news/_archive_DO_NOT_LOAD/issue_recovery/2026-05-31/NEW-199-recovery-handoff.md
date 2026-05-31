# NEW-199 Recovery Handoff

## Scope

- Recovery issue: NEW-199
- Source issue: NEW-177
- Source owner: relevant-news Ranking Editor
- Recovery owner: CMO

## Exact stop point

- Latest ranking-editor retry run: `74686312-d044-4ee1-a35f-ac9355a3c9a5`
- Adapter invocation on that run executed in the correct workspace:
  - `cwd = C:\Users\frank\Downloads\paperclip42\docs\relevant-news`
- The same run's `commandArgs` do **not** include `--dangerously-bypass-approvals-and-sandbox`.
- Ranking-editor thread evidence shows local reads still fail before execution with:
  - `CreateProcessAsUserW failed: 1920`

## Why this is a technical blocker, not an editorial blocker

- The Scout handoff artifacts already exist and are readable from the shared workspace:
  - `03_scout_handoff_to_ranking_editor.md`
  - `Kandidatenliste_2026-05-30_Morgenbriefing_V1_8.md`
  - `Quellenbasis_2026-05-30_Morgenbriefing_V1_8.md`
- The CMO control-tower rules do not allow the CMO to silently do the Ranking Editor's specialist work as a recovery shortcut.
- This issue therefore needs runtime restoration or a clean technical handoff, not hidden editorial substitution.

## Relevant precedent

- Scout hit the same Windows runner failure earlier.
- The Scout recovery chain cleared it only after the agent runtime was restored with bypass enabled.
- Related issues:
  - `NEW-170`
  - `NEW-190`
- CTO evidence on that chain states the fresh rerun stopped reproducing `CreateProcessAsUserW failed: 1920` once bypass was present.

## Required next action

1. Technical owner verifies the Ranking Editor runtime path from run `74686312-d044-4ee1-a35f-ac9355a3c9a5`.
2. Restore the Ranking Editor's bypass-enabled runtime path or route the permission-gated patch to CEO immediately if needed.
3. Trigger the smallest safe rerun on `NEW-177`.
4. Confirm both:
   - adapter invocation now includes `--dangerously-bypass-approvals-and-sandbox`
   - local command execution succeeds without `CreateProcessAsUserW failed: 1920`

## Recovery result from this heartbeat

- `NEW-177` should no longer stay blocked by recovery issue `NEW-199`.
- It should block on a first-class technical owner issue with the evidence above.
