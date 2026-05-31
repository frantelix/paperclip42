# NEW-189 Recovery Handoff

Date: 2026-05-30
Recovery issue: `NEW-189`
Source issue: `NEW-186`
Technical follow-up: `NEW-190`

## Purpose

Record why `NEW-189` can close without touching the Scout-owned source issue directly.

## Verified control-plane state

- `NEW-186` is no longer a stranded `in_progress` issue. Before closeout it had been moved to `blocked` for intervention visibility, and after closeout it auto-resumed to a fresh Scout run.
- `NEW-186` already has durable Scout evidence in its own thread, plus local artifacts `NEW-186-startup-canary-evidence.md` and `NEW-186-issue-comment-draft.md`.
- The latest Scout comments state that workspace resolution points at `C:\Users\frank\Downloads\paperclip42\docs\relevant-news`.
- The current exact blocker remains `windows sandbox: runner error: CreateProcessAsUserW failed: 1920`.
- CTO follow-up `NEW-190` exists as a direct child of `NEW-186` and is currently `in_progress`.
- `NEW-190` is explicitly scoped to confirm or repair the `CreateProcessAsUserW failed: 1920` runtime failure and to report the unblock result back to `NEW-186`.

## Recovery decision

- No further CMO-side mutation is needed on `NEW-186`.
- The live execution path has been restored by routing the current technical blocker to CTO via `NEW-190`.
- `NEW-189` can therefore close as complete recovery orchestration rather than remain open as a duplicate blocker.
- After `NEW-189` closed, Paperclip auto-resumed `NEW-186` to `in_progress` on Scout run `b51adb1d-e246-4e74-bce3-a71e656570be`.

## Next action

Owner: CTO on `NEW-190`
Action: confirm whether `CreateProcessAsUserW failed: 1920` is still the active stop point, repair it if possible, and comment the exact unblock result back on `NEW-186`.
