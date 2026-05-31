# Canonicalization Report - 2026-05-31 Claim Ledger and Source Verification

## Scope

This report compares the available 2026-05-31 Claim Ledger and Source
Verification candidates after merged PR #1 and PR #2.

Base snapshot:

- Repository: `frantelix/paperclip42`
- Branch used: `codex-relevant-news-canonicalize-claim-source-2026-05-31`
- Base ref: `origin/master`
- Base commit: `7c62da2455802dc8f760d9584a6d7fb6f1e1960a`

Preflight:

- `git pull --ff-only`: already up to date.
- `git status --short`: clean before PR #3 edits.
- `python3 scripts/relevant-news/repo_audit.py`: passed before PR #3 edits.
- `git diff --check`: passed before PR #3 edits.
- PR #2 archive folder exists at
  `docs/relevant-news/_archive_DO_NOT_LOAD/issue_recovery/2026-05-31/`.
- Archive count: 31 tracked files including `INDEX.md`; therefore 30 archived
  recovery/status notes plus the index are tracked.

Read-first note:

- `docs/relevant-news/STAGING_PLAN_RELEVANT_NEWS.md` is not present in this
  clean snapshot.
- The available tracked staging note is
  `docs/relevant-news/99_NOTIZEN/2026-05-31-clean-import-staging-plan.md`.

Local artifact note:

- The clean post-PR #2 `origin/master` tree did not contain the four prompt
  artifact files.
- The local main checkout contained those four files as untracked artifacts.
- This PR copied the two run-scoped final artifacts into their original
  run-scoped location and copied the two root-level fallback variants into
  `superseded/root-level/`.
- Additional local 2026-05-31 delivery, runtime, scheduling, log, draft, review, and
  broad run artifacts were inspected but not pulled into this PR.

No new source verification was performed. No editorial claim was rewritten.

## Canonical Decision

Canonical Claim Ledger:

`docs/relevant-news/20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/Claim_Ledger_2026-05-31_Morgenbriefing_V1_8.md`

Canonical Source Verification:

`docs/relevant-news/20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/06_source_verification_2026-05-31_Morgenbriefing_V1_8.md`

Reason:

- The run-scoped Claim Ledger is the complete 2026-05-31 controlled automation
  pilot ledger. It contains the final active `K1`, `K2`, `K3` claim boundaries,
  removed/held `K12` and `K10` boundaries, verb-ladder limits, and
  concreteness checks.
- The run-scoped Source Verification file explicitly marks itself as the
  authoritative Source Verification boundary inside the
  `2026-05-31_controlled-automation-pilot` packet. It states that only `K1`,
  `K2`, and `K3` are active and that `K10` is `hold` and `K12` is `raus`.
- The root-level local fallback files are narrower update/fallback artifacts.
  They do not provide a better run-scoped packet boundary.

## Compared Primary Candidates

| File path | Tracked/untracked status before PR #3 | File size | SHA-256 | Likely role | Complete, partial, blocker-only, or superseded | Actual claim/source content or status text | Incoming references found in tracked docs | Recommendation |
|---|---:|---:|---|---|---|---|---|---|
| `docs/relevant-news/Claim_Ledger_2026-05-31_Morgenbriefing_V1_8.md` | untracked local artifact in main checkout; archived by this PR under `superseded/root-level/` | 1180 bytes | `2c76cc599f72788c46ecff6ab349cf16e8b28fb342ecb07b5d69ac8614a17ed7` | root-level Claim Ledger fallback/update | partial and superseded | claim-boundary update for `K12` and `K10`; no full `K1`/`K2`/`K3` ledger | Basename references in archived notes: `NEW-219-recovery-resolution.md`, `NEW-220_SOURCE_VERIFICATION_2026-05-31.md`, `NEW-220_SOURCE_VERIFICATION_BLOCKER_2026-05-31.md`, `NEW-224-recovery-resolution.md`; run-scoped basename also referenced by `NEW-231-recovery-resolution.md`. | superseded |
| `docs/relevant-news/06_source_verification_2026-05-31_Morgenbriefing_V1_8.md` | untracked local artifact in main checkout; archived by this PR under `superseded/root-level/` | 1887 bytes | `3d9afc3a69a67e6a45bc78cb98aa49371d7304c949cc4ea48fa20e03b80e37d1` | root-level Source Verification fallback/update | partial and superseded | conservative no-strengthening boundary for `K12` and `K10`; does not claim complete run packet authority | Basename references in archived notes: `2026-05-31-source-verification-status.md`, `NEW-219-recovery-resolution.md`, `NEW-220_SOURCE_VERIFICATION_2026-05-31.md`, `NEW-220_SOURCE_VERIFICATION_BLOCKER_2026-05-31.md`, `NEW-224-recovery-resolution.md`, `NEW-231-recovery-resolution.md`. | superseded |
| `docs/relevant-news/20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/Claim_Ledger_2026-05-31_Morgenbriefing_V1_8.md` | untracked local artifact in main checkout; tracked by this PR | 5142 bytes | `810d328c8ef5f4264463bb60330954ebb665bdaad6d07bf9be4a4a6e219552c5` | run-folder Claim Ledger | complete for final tracked 2026-05-31 run boundary | actual claim ledger content for `K1`, `K2`, `K3`, plus removed/held `K12` and `K10` limits | Full run-scoped path referenced by `NEW-231-recovery-resolution.md`; basename references in `NEW-219-recovery-resolution.md`, `NEW-220_SOURCE_VERIFICATION_2026-05-31.md`, `NEW-220_SOURCE_VERIFICATION_BLOCKER_2026-05-31.md`, and `NEW-224-recovery-resolution.md`. | canonical |
| `docs/relevant-news/20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/06_source_verification_2026-05-31_Morgenbriefing_V1_8.md` | untracked local artifact in main checkout; tracked by this PR | 1358 bytes | `d206ae5e406505707295ca1ab814685b653420ec2a7b09cb79f1b68e6a8a4b26` | run-folder Source Verification boundary | complete as final run-scoped packet boundary | actual source-verification boundary text; marks `K1`/`K2`/`K3` active, `K10` hold, `K12` raus | Full run-scoped path referenced by `2026-05-31-source-verification-status.md` and `NEW-231-recovery-resolution.md`; basename references in `NEW-219-recovery-resolution.md`, `NEW-220_SOURCE_VERIFICATION_2026-05-31.md`, `NEW-220_SOURCE_VERIFICATION_BLOCKER_2026-05-31.md`, and `NEW-224-recovery-resolution.md`. | canonical |

## Additional Related Local Artifacts Pulled Into The Run Packet

These files were untracked in the local main checkout and were pulled because
they directly explain or support the final Claim/Source packet boundary. They
are not new verification.

| File path | File size | SHA-256 | Likely role | Recommendation |
|---|---:|---|---|---|
| `docs/relevant-news/20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/07_source_verifier_completion_note_2026-05-31.md` | 1522 bytes | `e5d2e5c85fec5fd044c82b1ee7a252c9cac93d9d09e80385d0ffd194c62ed914` | source-verifier completion/handoff note naming the final three-story boundary | supporting context |
| `docs/relevant-news/20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/08_ranking_refresh_after_source_recheck.md` | 2204 bytes | `b7f0fcf1b8a09c577e0a62f5b3a91503e625f2bd98aa940ec89f9b85d7a87191` | ranking refresh after source recheck; references canonical Claim Ledger and Source Verification | supporting context |
| `docs/relevant-news/20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/Source_Verifier_Blocker_Note_2026-05-31_NEW-220.md` | 2783 bytes | `ec635670ca7601c59c28ccd18bb7119055ef2e8345cbd3b43b8e810f8632c6c2` | earlier blocker note for `K12` freshness and `K10` primary-trail gates | superseded/supporting context |
| `docs/relevant-news/20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/Source_Verifier_Sync_Target_2026-05-31_NEW-230.md` | 2055 bytes | `a5347075e1e76acc5f99e1593b1f54ca4f04980aaa9a7192e3f2d40432474f6a` | sync target explaining why the run-folder Source Verification needed final packet authority | supporting context |

## Available Archived Notes With Source/Claim Mentions

These files were already tracked under
`_archive_DO_NOT_LOAD/issue_recovery/2026-05-31/`. They are historical notes,
not active artifact candidates.

| File path | Tracked/untracked status | File size | SHA-256 | Likely role | Complete, partial, blocker-only, or superseded | Actual claim/source content or status text | Incoming references found in tracked docs | Recommendation |
|---|---:|---:|---|---|---|---|---|---|
| `docs/relevant-news/_archive_DO_NOT_LOAD/issue_recovery/2026-05-31/2026-05-31-NEW-216-review-gate.md` | tracked | 1365 bytes | `cda219b898e2f4d128737c45c8063fc987b8051dae216d9c6971f1fbe7ea4b57` | adversarial review gate note | blocker-only | status/gate text; no claim ledger or source verification body | Listed in `INDEX.md`. | blocker/status-only |
| `docs/relevant-news/_archive_DO_NOT_LOAD/issue_recovery/2026-05-31/2026-05-31-new-215-blocked-status.md` | tracked | 1259 bytes | `cf4bf724ae211b22d6eb944c708eb10ded5981c70aaa5e1e390700039754aa6c` | briefing writer blocked status | blocker-only | status text; names required inbound artifacts but contains no artifact body | Listed in `INDEX.md`. | blocker/status-only |
| `docs/relevant-news/_archive_DO_NOT_LOAD/issue_recovery/2026-05-31/2026-05-31-source-verification-status.md` | tracked | 1512 bytes | `fe8609fe389f72aab1fe03effdae3f5110dee2482216b856160984cfbf12b1bc` | source verification status note | superseded | status/resolution text; points to the canonical run-folder Source Verification | Listed in `INDEX.md`. | superseded |
| `docs/relevant-news/_archive_DO_NOT_LOAD/issue_recovery/2026-05-31/NEW-178-source-verification-blocked-2026-05-31.md` | tracked | 1681 bytes | `b264eadc31108fd8ffb5779fc9eee9741238e1302ff62097fcec49c25fdf9390` | source verification blocker note | blocker-only | blocker and unblock instructions; no completed verification | Listed in `INDEX.md`. | blocker/status-only |
| `docs/relevant-news/_archive_DO_NOT_LOAD/issue_recovery/2026-05-31/NEW-219-recovery-resolution.md` | tracked | 2455 bytes | `0311b1326e8b713c7631326bd71929fe2ccff528e6a2b21b2755cc2d209e6199` | recovery resolution for review issue | superseded/status-only | recovery evidence naming expected artifacts; no artifact body | Listed in `INDEX.md`. | superseded |
| `docs/relevant-news/_archive_DO_NOT_LOAD/issue_recovery/2026-05-31/NEW-220_SOURCE_VERIFICATION_2026-05-31.md` | tracked | 901 bytes | `0a2d59785c6d9ad0d4f65652698048b84e1aca48dd255e6897230aef8ca68d77` | NEW-220 source-verification stub | partial and superseded | limited allowed/not-claimed boundary for K10/K12 only; explicitly says it is a stub and not active | Listed in `INDEX.md`. | superseded; not canonical |
| `docs/relevant-news/_archive_DO_NOT_LOAD/issue_recovery/2026-05-31/NEW-220_SOURCE_VERIFICATION_BLOCKER_2026-05-31.md` | tracked | 1912 bytes | `6300f5a432f64e28d17e267a4bba4607b9fbe61c81fcb32f37cfc7a479ee66ed` | NEW-220 blocker note | blocker-only and superseded | blocker text plus safe downstream boundary; no completed verification | Listed in `INDEX.md`. | blocker/status-only |
| `docs/relevant-news/_archive_DO_NOT_LOAD/issue_recovery/2026-05-31/NEW-223-blocker-note-2026-05-31.md` | tracked | 2952 bytes | `ba376d89b545358d956e2d40260ad1196735752a144e5d016df0f9648f80d56e` | briefing writer blocker note | superseded/status-only | status and constraints; names Claim Ledger and Source Verification as required inputs | Listed in `INDEX.md`. | superseded |
| `docs/relevant-news/_archive_DO_NOT_LOAD/issue_recovery/2026-05-31/NEW-224-recovery-resolution.md` | tracked | 2704 bytes | `a2cbd06e70bf7ec801c490eaf8b9e78ca961dbaade09bd642924239463292abe` | recovery resolution for writer issue | superseded/status-only | recovery evidence naming expected artifacts; no artifact body | Listed in `INDEX.md`. | superseded |
| `docs/relevant-news/_archive_DO_NOT_LOAD/issue_recovery/2026-05-31/NEW-229-recovery-resolution.md` | tracked | 3008 bytes | `b7d0638a85f915173bcce7423fce1d35fa044ccbec6e576dc448753cfbcfc0cd` | recovery resolution for stale writer wrapper | superseded/status-only | completion/status evidence; mentions source verification but contains no artifact body | Listed in `INDEX.md`. | superseded |
| `docs/relevant-news/_archive_DO_NOT_LOAD/issue_recovery/2026-05-31/NEW-231-recovery-resolution.md` | tracked | 2899 bytes | `0cd1d1c71654d521bf1b4b3c80421abed6e752a7e72fd59b8972bb34bbd8c563` | recovery resolution for packet consistency | superseded/status-only | status evidence saying final run-folder files existed and matched a three-story boundary; no artifact body | Listed in `INDEX.md`. | superseded |

## Reference Updates

- `08_ranking_refresh_after_source_recheck.md` now points to
  `06_source_verification_2026-05-31_Morgenbriefing_V1_8.md` in the same
  run folder instead of a root-level fallback path.
- No archived historical note was rewritten.
- No active delivery, runtime, scheduling, or automation reference was changed.

## Not Pulled

The local main checkout contains many other untracked artifacts under
`docs/relevant-news/20_LAUFARTEFAKTE/`, including delivery logs, scheduling notes,
runtime exports, PowerShell files, drafts, reviews, scorecards, watchlists, and
older run packets. They were deliberately not pulled because this PR is scoped
to the 2026-05-31 Claim Ledger and Source Verification canonicalization.

## Recommendation

Use the run-scoped files as canonical for the 2026-05-31 controlled automation
pilot packet:

- `../../20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/Claim_Ledger_2026-05-31_Morgenbriefing_V1_8.md`
- `../../20_LAUFARTEFAKTE/2026-05-31_controlled-automation-pilot/06_source_verification_2026-05-31_Morgenbriefing_V1_8.md`

Keep the copied root-level variants only under `superseded/root-level/`.

No further human decision is required for this PR.
