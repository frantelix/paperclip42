# NEW-224 Recovery Resolution

Date: 2026-05-31
Recovery issue: `NEW-224`
Source issue: `NEW-223`
Technical blocker issue: `NEW-225`

## Purpose

Record why the latest recovery wrapper for `NEW-223` should be replaced by a first-class CTO blocker instead of staying parked as an editorial recovery issue.

## Exact stop point

- Paperclip opened `NEW-224` after Writer retry run `9a5ca943-ff03-488b-99d6-fe9ad7e0e31b` succeeded but still left `NEW-223` without a live execution path.
- The latest Writer comments on `NEW-223` report the active failure as `CreateProcessAsUserW failed: 1920`.
- The same comments framed the block as missing readable packet inputs, but the canonical refreshed packet is readable from the shared workspace in the current heartbeat.

## Verified state

- `NEW-222` is already `done`, so the ranking refresh itself is not waiting on another editorial stage.
- Verified readable files in `20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/`:
  - `08_ranking_refresh_after_source_recheck.md`
  - `Claim_Ledger_2026-05-31_Morgenbriefing_V1_8.md`
  - `06_source_verification_2026-05-31_Morgenbriefing_V1_8.md`
  - `Shortlist_Scorecard_2026-05-31_Morgenbriefing_V1_8.md`
  - `Watchlist_2026-05-31_Morgenbriefing_V1_8.md`
- The refreshed ranking handoff narrows the active Top-Story set to `K1`, `K2`, `K3`, marks `K12` as `raus`, and keeps `K10` on `hold`.
- This means the real unresolved blocker is not editorial packet availability. It is the Writer runtime path that still fails before the rewrite can start.
- A CTO-owned blocker issue now exists as [NEW-225](/NEW/issues/NEW-225).

## Recovery fields

- `source_issue`: the writer-stage issue that still needs a valid next action.
- `technical_blocker_issue`: the current actionable engineering issue that owns the real stop point.
- `recovery_issue`: the temporary manager-owned wrapper used only to repair routing when the source issue stranded.
- `close_condition`: the recovery wrapper can close once the source issue points at the correct technical blocker or is otherwise intentionally resolved.

## Recovery action

1. Keep `NEW-223` in `blocked`.
2. Replace its blocker list so it is blocked by `NEW-225` instead of `NEW-224`.
3. Leave a source-issue comment naming the readable packet and the exact remaining runtime blocker.
4. Close `NEW-224` after the blocker rewrite lands.

## Daily-use instruction

When a role reports unreadable local inputs after an upstream packet refresh, verify the canonical workspace packet before treating the stop as editorial. If the packet is present, replace the recovery wrapper with a first-class technical blocker so the issue graph names the real owner and next action.
