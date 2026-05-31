# NEW-191 Recovery Resolution

Date: 2026-05-30
Recovery issue: `NEW-191`
Source issue: `NEW-186`
Technical blocker issue: `NEW-190`

## Purpose

Record the exact control-plane recovery action for the latest stranded recovery on `NEW-186`.

## Verified state

- `NEW-186` is currently `blocked` and already contains current Scout evidence in its thread.
- The real unresolved blocker is not editorial and not routing. It is the CTO-owned runtime issue `CreateProcessAsUserW failed: 1920`.
- `NEW-190` is the active technical follow-up for that blocker and is currently `in_progress` with CTO ownership.
- Before this recovery closes, `NEW-186` must point at `NEW-190` as its explicit blocker rather than at `NEW-191`.

## Recovery fields

- `source_issue`: the issue that must keep a valid execution path or explicit blocker.
- `technical_blocker_issue`: the current actionable engineering issue that owns the real stop point.
- `recovery_issue`: the temporary manager-owned issue used only to repair routing/governance when Paperclip strands the source issue.
- `close_condition`: the recovery issue can close once the source issue points at the correct live blocker or has otherwise been intentionally resolved.

## Recovery action

1. Keep `NEW-186` in `blocked`.
2. Replace its blocker list so it is blocked by `NEW-190`.
3. Close `NEW-191` after the blocker rewrite lands.

## Daily-use instruction

If `NEW-186` strands again before `NEW-190` resolves, first verify whether the source issue still points at the real technical blocker. If it does, do not create duplicate recovery routing; only create another recovery issue when the blocker path or ownership becomes invalid.
