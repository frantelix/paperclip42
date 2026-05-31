# NEW-198 Recovery Resolution

Date: 2026-05-31
Recovery issue: `NEW-198`
Source issue: `NEW-177`
Upstream handoff issue: `NEW-176`

## Purpose

Record the exact recovery decision for the stranded Ranking Editor issue and the evidence that makes it actionable again.

## Verified state

- `NEW-176` is `done` and its thread explicitly hands off work to `NEW-177`.
- The required Scout package already exists in `20_LAUFARTEFAKTE/2026-05-30_controlled-automation-pilot/`.
- Verified files:
  - `Kandidatenliste_2026-05-30_Morgenbriefing_V1_8.md`
  - `Quellenbasis_2026-05-30_Morgenbriefing_V1_8.md`
  - `03_scout_handoff_to_ranking_editor.md`
- The handoff note says the Scout intake is complete enough for Ranking to start and names the exact ranking constraints for K1-K15.
- `NEW-177` was blocked only because the temporary recovery wrapper `NEW-198` existed, not because the Scout handoff was still missing.

## Recovery fields

- `source_issue`: the role-owned issue that must return to a live editorial path.
- `upstream_handoff_issue`: the completed prior stage whose artifacts satisfy the source issue's prerequisites.
- `recovery_issue`: the temporary manager-owned routing issue used only to repair stranded state.
- `close_condition`: the recovery issue can close once `NEW-177` is back in a ready state with a precise next action.

## Recovery action

1. Point `NEW-177` back to a ready state.
2. Leave a source-issue comment linking the Scout artifacts and the exact next action for Ranking Editor.
3. Close `NEW-198` once the source issue no longer depends on the recovery wrapper.

## Daily-use instruction

When a role issue strands after an upstream stage has already completed, verify the actual artifact path before accepting a "missing handoff" comment at face value. If the handoff files are present and the upstream issue is done, restore the source issue to a ready state and close the recovery wrapper instead of creating duplicate blocker chains.
