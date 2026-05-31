Issue: `NEW-223 Rewrite briefing draft after ranking refresh (2026-05-31 Morgenbriefing)`

Status: resolved / superseded

Resolution note:
- The runtime blocker described below was cleared in a later heartbeat.
- The rewrite has since been executed in `20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/Briefing_Draft_2026-05-31_Morgenbriefing_V1_8.md`.
- The reviewer handoff has since been written to `20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/09_briefing_writer_handoff_to_adversarial_reviewer.md`.
- Follow-up closure confirmed that `NEW-229` was only a stale recovery wrapper, not an active blocker on this issue.
- This note is retained only as incident history for the earlier stop-point.

Reason:
- The local shell runner is unavailable in this session (`CreateProcessAsUserW failed: 1920`), so the checked local handoff files cannot be read.
- A continuation retry on the same issue hit the same runner failure, so the block is persistent across heartbeats rather than a one-off read error.
- Follow-up comment `298ccf02-d121-4d76-bf28-a341b708d365` clarifies that the refreshed packet is readable in `20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/`; the remaining blocker is runtime-only and is tracked on `NEW-225`.

Constraint:
- Per briefing-writer rules, no draft may be written when `Claim-Ledger` or `Source Verification` are missing or unreadable.

What was attempted:
- Local shell reads in the workspace and instruction directories.
- GitHub fallback against accessible repositories to find versioned briefing artifacts.
- Branch and repository discovery fallback.

Outcome:
- No briefing draft produced.
- No adversarial-reviewer handoff produced.
- The rewrite constraints from the parent review remain unapplied because this runtime still cannot read the refreshed packet locally:
  - `K12` must not appear as a top story.
  - `K10` must not be used unless the refreshed packet explicitly re-clears it.

Correction after follow-up comment:
- The refreshed packet should be treated as present and readable at the documented artifact path.
- The blocker is no longer "missing inputs"; it is specifically the inability of this runtime to read those local files because `CreateProcessAsUserW failed: 1920`.

Unblock owner and next action:
- CTO / runtime owner on `NEW-225`: restore the Briefing Writer local runtime so this agent can read `20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/` and execute the rewrite.
- Briefing Writer next action after `NEW-225` clears: open the refreshed packet, rewrite `Briefing_Draft_2026-05-31_Morgenbriefing_V1_8.md`, remove `K12`, and only retain `K10` if the refreshed packet explicitly clears it.

Required accessible inputs before drafting:
- refreshed top-story set for `2026-05-31 Morgenbriefing`
- `Claim-Ledger`
- `Source Verification`
- any updated data-quality note if story count, weakest claim, or challenger handling changed during the recheck
