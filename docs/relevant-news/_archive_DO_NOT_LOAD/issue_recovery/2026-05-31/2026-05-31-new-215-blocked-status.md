## NEW-215 Briefing Writer Status

Date: 2026-05-31
Issue: `NEW-215 Briefing Writer: Briefing-Draft (2026-05-31 Morgenbriefing)`
Run: current V1.8 morning briefing run
Status: blocked
Blocker: `NEW-214 Source Verification: Top-Story Verification (2026-05-31 Morgenbriefing)`

### Board Cleanup Decision

This issue stays in the current V1.8 run from 2026-05-31 and waits for `NEW-214`.

### Writer Constraint While Blocked

Do not draft the briefing before verified top stories, claim ledger, and source verification are available from `source-verifier`.

### Required Output Once Unblocked

Create one compact daily briefing with:

- top news
- why each top story matters
- a short watchlist
- short macro context
- a short data-quality note

### Editorial Priorities From The Latest Comment

- prioritize genuinely important and current topics
- avoid weak stories being promoted to top stories
- maintain international balance

### Next Action

Resume drafting only after `NEW-214` is complete and its verified handoff artifacts are available.

Expected inbound from `source-verifier`:

- verified top stories
- claim ledger
- source verification

Expected outbound after drafting:

- briefing draft
- required handoff artifacts for `adversarial-reviewer`
