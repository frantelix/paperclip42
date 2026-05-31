# NEW-196 Post-Patch Rerun Evidence

Date: 2026-05-30
Issue: `NEW-196`
Target canary: `NEW-186`
Fresh run id: `d5ee5d38-0e12-4810-9bd5-670497db9c55`

## Adapter invocation

- Adapter type: `codex_local`
- Command args:
  - `--search exec --json --dangerously-bypass-approvals-and-sandbox --model gpt-5.4 -c model_reasoning_effort="high" -`

## Fresh run result

- The current run started in the intended workspace: `C:\Users\frank\Downloads\paperclip42\docs\relevant-news`
- Minimal shell commands completed successfully in this same run:
  - `Get-ChildItem -Force`
  - `Get-ChildItem -Recurse -File | Select-Object -ExpandProperty FullName`
- The old blocker string `windows sandbox: runner error: CreateProcessAsUserW failed: 1920` was not observed as a fresh runtime failure in this run.

## Important nuance

- The run log still contains many textual matches for `CreateProcessAsUserW failed: 1920`, but those come from reading older `NEW-186` evidence files and from explicit search commands during this heartbeat.
- Stderr was present, but only for early path/wrapper mistakes in this heartbeat; there were zero stderr hits for:
  - `CreateProcessAsUserW failed: 1920`
  - `windows sandbox: runner error`
  - `Not inside a trusted directory and --skip-git-repo-check was not specified.`

## Operational conclusion

- The CEO patch claim behind `NEW-194` is corroborated by the fresh `adapter.invoke` event: the bypass flag is back in the live Scout invocation.
- The earlier `CreateProcessAsUserW failed: 1920` blocker did not recur as a fresh runtime error in this rerun.

## Next action

Owner: CTO on `NEW-195`
Action: propagate this fresh rerun evidence to `NEW-190`, `NEW-192`, and `NEW-193`, then decide whether `NEW-186` can move from blocked canary evidence to direct follow-up.
