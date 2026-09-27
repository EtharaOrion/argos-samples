# argos_grader

The grader that `tests/test.sh` runs inside the verifier container. It applies the agent's
patch to the repository, runs the repository's own test suite, checks how the agent worked,
judges the rubric, and writes the reward. Python 3.10+, standard library only.

```
PYTHONPATH=/tests python3 -P -m argos_grader --tests-dir /tests \
    --patch /logs/artifacts/agent.patch --out-dir /logs/verifier
```

## Inputs

| Path in the container | What it is |
|---|---|
| `/tests/config.json` | repo path, base commit, test command, target test lists (f2p, n2p, p2p) |
| `/tests/test.patch` | the held-out tests, applied by the test command |
| `/tests/rubrics.json` | rubric items (`criterion`, `evaluation_rule`, `evaluation_target`, `instruction_quote`) |
| `/tests/instruction.md` | the task instruction; every rubric item must quote it verbatim |
| `/logs/artifacts/agent.patch` | the agent's change (`git diff` against the base commit) |
| `/logs/agent/trajectory.json` | the agent's trajectory; needed for the deterministic checks and trajectory rubric items |

Harbor mounts `/logs` from the trial. To grade a recorded run by hand, mount its `run_N/`
folder as `/logs` (it has the same layout); the grader rewrites `verifier/` there.

## Stages

1. **Environment** - the repository must be at `repo_dir`, clean, at `base_commit`; otherwise
   the run is `invalid` (`environment_unclean`).
2. **Filter** - edits to files that `test.patch` touches are removed, so graded tests cannot be
   changed by the agent. The result is `filtered.patch`.
3. **Control run** - `test.patch` is applied and the test command runs on the original code
   (`control-output.log`). This is the baseline.
4. **Agent run** - the repository is reset, `filtered.patch` is applied, and the test command
   runs again (`test-output.log`).
5. **Outcome** - both logs are parsed and compared with the target lists in `config.json`:
   f2p tests must go from failing to passing, n2p tests must pass, p2p tests must keep passing.
   The outcome is the share of targets met; `resolved = 1` only when all are met.
6. **Deterministic checks** - rule checks on the trajectory and diff: fair play (no fetching
   upstream code, no reading the reference solution, no rewriting graded tests), run health,
   record quality, and whether the files the reference fix changes were reached. Hard-check
   failures void the run (`gate = 0`). Checks that need Harbor's `result.json` (A1, A4, B1, B2,
   B4) abstain here.
7. **Rubric** - each grounded item in `rubrics.json` is judged against its `evaluation_target`
   (the diff, the trajectory, or the test output) by the judge model configured in `task.toml`
   (see below). Verdicts are yes/no with cited evidence; several votes per item take a majority.
8. **Reward**

```
process = (deterministic + rubric) / 2
reward  = gate * ((1 - 2a) * outcome + 2a * process)     a = min(0.05, d / (2(1 + d))), d = max(1/targets, 0.02)
```

Without a judge configured, stages 1-6 run, `reward.json` holds the outcome only, and the rubric
is reported as `deferred_to_host` (to be scored later with `tools/score.py`).

## Enabling the rubric judge in the container

Set the judge in the task's `task.toml`. The verifier needs network access to reach it:

```toml
[verifier]
network_mode = "public"                 # also under [verifier.environment]

[verifier.env]
ARGOS_JUDGE_MODEL = "openai/<model>"    # or "anthropic/<model>"
ARGOS_JUDGE_BASE_URL = "https://api.openai.com/v1"
ARGOS_JUDGE_API_KEY = "<your key>"
ARGOS_JUDGE_VOTES = "1"                 # odd number of votes per item
```

- `openai/<model>` uses the OpenAI Responses API (`<base_url>/responses`);
  `anthropic/<model>` uses the Anthropic Messages API (`<base_url>/v1/messages`).
  Other providers need an endpoint compatible with one of these.
- The key is read from the environment inside the verifier container, which also runs the
  agent's patched code. Prefer a proxy endpoint that holds the key over pasting a raw key.
- A judge outage does not void the run: the rubric is recorded as `judge_error` and the
  outcome-only reward is kept.

## Outputs (`/logs/verifier/`)

| File | Content |
|---|---|
| `reward.json` | `reward` (composed when judged, outcome only otherwise), `score_outcome`, `score_binary`; plus `score_process`, `gate`, `alpha` when judged |
| `metrics.json` | everything: outcome with diagnostics, patch filtering, control run, deterministic checks, rubric, composition |
| `final_score.md` | one-page summary per channel (when judged) |
| `verdicts.jsonl` | one line per rubric item and vote: `item_id`, `verdict`, `majority`, `weight`, `evaluation_target`, `model` |
| `judge_calls.jsonl` | every judge request and response, for audit |
| `filtered.patch`, `control-output.log`, `test-output.log` | the graded patch and the two test logs |
| `invalid.json` | written instead of a reward when the run cannot be measured |

## `tools/` (host side, not used by `test.sh`)

- `score.py` - re-score a recorded run with a different judge:
  `PYTHONPATH=tests python3 -m argos_grader.tools.score <run_dir> --task <task_dir> --judge-model ... --judge-base-url ... --judge-api-key ... --votes 1`
- `process_score.py` - Harbor plugin that runs `score.py` after each trial
  (`--plugin argos_grader.tools.process_score:ArgosProcessScore`).
- `patch_grader.py` - applies the in-container judging step to an unpatched `grade.py`.

`version.py` hashes the grader's `*.py` files; the `tools/` folder and this file are not part of
the hash.
