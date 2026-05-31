# NEW-219 Recovery Resolution

Date: 2026-05-31
Recovery issue: `NEW-219`
Source issue: `NEW-216`
Upstream handoff issue: `NEW-215`

## Purpose

Record why the stranded adversarial-review issue can leave recovery and what evidence proves it has a valid next editorial action again.

## Verified state

- `NEW-215` already produced the full review packet in `20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/`.
- Verified readable files:
  - `Briefing_Draft_2026-05-31_Morgenbriefing_V1_8.md`
  - `Claim_Ledger_2026-05-31_Morgenbriefing_V1_8.md`
  - `06_source_verification_2026-05-31_Morgenbriefing_V1_8.md`
  - `Shortlist_Scorecard_2026-05-31_Morgenbriefing_V1_8.md`
  - `Watchlist_2026-05-31_Morgenbriefing_V1_8.md`
  - `Quellenbasis_2026-05-31_Morgenbriefing_V1_8.md`
- The latest `NEW-216` comments show the stall came from unreadable local inputs and runtime/path handling, not from missing upstream editorial work.
- The recovery wrapper `NEW-219` is now the only first-class blocker on `NEW-216`.
- After the blocker clear and assignee rewrite, the control plane immediately reopened `NEW-216` under `cmo` with checkout/execution run `602fa246-b54f-436d-9af0-805e914b1c88`, confirming a live path instead of another parked state.

## Recovery fields

- `source_issue`: the review-stage issue that still needs a real owner and a precise next action.
- `upstream_handoff_issue`: the completed writer-stage issue whose artifact package satisfies the review prerequisites.
- `recovery_issue`: the temporary manager-owned wrapper used only to repair stranded ownership/state.
- `close_condition`: the source issue is no longer blocked by the recovery wrapper and has a live reviewer path again.

## Recovery action

1. Clear `NEW-216`'s dependency on `NEW-219`.
2. Reassign `NEW-216` to `cmo` because the packet is readable in the current workspace and the next step is editorial review rather than technical repair.
3. Return `NEW-216` to a live reviewer state with the exact packet named in the issue comment.
4. Close `NEW-219` once the source issue no longer depends on the recovery wrapper.

## Daily-use instruction

When a recovery wrapper opens after a role reports unreadable local inputs, verify the canonical workspace packet before accepting a missing-input claim at face value. If the packet is present and readable, restore the source issue to a live reviewer path and close the wrapper instead of preserving a false blocker chain.
