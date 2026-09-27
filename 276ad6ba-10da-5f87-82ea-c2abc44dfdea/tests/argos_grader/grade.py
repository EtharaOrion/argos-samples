"""Grade one trial: filter + apply the agent patch, run tests, score the outcome.

The verifier is sealed, so it computes the two channels that need no network --
the outcome (score_v2g) and the deterministic checks -- and writes
``reward.json`` (the outcome, so a stock Harbor run is interpretable) plus
``metrics.json``, or ``invalid.json``. The rubric judge needs the network, so it
and the composition run on the host in ``argos.tools.score``, which rewrites
``reward.json`` with the composed reward. See README.md for the output contract.
"""

from __future__ import annotations

import functools
import json
import os
import traceback
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from . import deterministic, judge, msb, outcome, patch
from .version import grader_version

DEFAULT_WEIGHT_IN_REWARD = 0.10
MAX_WEIGHT_IN_REWARD = 0.25
MIN_QUOTE_CHARS = 12
FINAL_OUTPUTS = ("reward.json", "reward.txt", "invalid.json", "metrics.json")
RUN_LOGS = ("test-output.log", "control-output.log", "filtered.patch")


# Composition: the same math as argos.tools.score (alpha_for_task / process_score / compose).
ALPHA_CAP = 0.05
MIN_MEANINGFUL_GAP = 0.02


def _alpha_for_task(n_targets: int) -> float:
    unit = 1.0 / n_targets if n_targets else 1.0
    d = max(unit, MIN_MEANINGFUL_GAP)
    return min(ALPHA_CAP, d / (2.0 * (1.0 + d)))


def _compose(*, outcome: float, process: float, alpha: float, gate: int) -> float:
    return gate * ((1.0 - 2.0 * alpha) * outcome + 2.0 * alpha * process)


def _status_of(hard_failures: list[str], judged: bool) -> str:
    if any(h.startswith("C") for h in hard_failures):
        return "voided"
    if "B2-no-exception" in hard_failures:
        return "invalid"
    if not judged:
        return "unjudged"
    return "voided" if hard_failures else "scored"


def _judge_and_compose(doc: dict[str, Any], out_dir: Path, tests_dir: Path) -> None:
    """Judge the rubric with ARGOS_JUDGE_* and compose the reward, in the verifier container."""
    cfg = judge.load_config(os.environ)
    rubric = doc.get("rubric")
    if cfg is None or not rubric or not (out_dir / "filtered.patch").exists():
        return
    instruction_path = tests_dir / "instruction.md"
    instruction = instruction_path.read_text() if instruction_path.exists() else ""
    items, weight, rubric_votes, _dropped = load_rubric(tests_dir, instruction)
    diff = (out_dir / "filtered.patch").read_text(errors="replace")
    if not items:
        return
    if len(diff) > judge.JUDGE_DIFF_BUDGET:
        doc["rubric"] = {**rubric, "status": "diff_exceeds_judge_budget"}
        return
    votes = judge.resolve_votes(cfg, rubric_votes)
    trajectory = TRAJECTORY_PATH.read_text(errors="replace") if TRAJECTORY_PATH.exists() else ""
    test_log = out_dir / "test-output.log"
    verification_output = test_log.read_text(errors="replace") if test_log.exists() else ""
    outcome = doc["outcome"]
    diagnostics = outcome.get("diagnostics") or {}
    summary = {"resolved": outcome.get("resolved", 0), "targets_hit": diagnostics.get("targets_hit", 0),
               "targets_total": diagnostics.get("targets_total", 0),
               "preserve_broken_count": diagnostics.get("broken_p2p_count", 0)}
    try:
        grader = judge.Judge(cfg, out_dir / "judge_calls.jsonl")
        score, results = grader.grade(items, votes, instruction, diff, summary, trajectory, verification_output)
    except Exception as exc:  # a judge outage must not void or crash the run
        doc["rubric"] = {**rubric, "status": "judge_error", "error": f"{type(exc).__name__}: {exc}"[:300]}
        return
    det = doc["deterministic"]
    det_score = float(det.get("soft_score") or 0.0)
    gate = int(det.get("gate", 1))
    hard = [c if isinstance(c, str) else str(c.get("id")) for c in (det.get("hard_failures") or [])]
    n_targets = int(diagnostics.get("targets_total") or 0)
    alpha = _alpha_for_task(n_targets)
    process = (det_score + score) / 2.0
    reward = round(_compose(outcome=outcome["score"], process=process, alpha=alpha, gate=gate), 4)
    doc["rubric"] = {
        **rubric,
        "status": "scored",
        "model": cfg["model"],
        "votes": votes,
        "score": round(score, 4),
        "numerator": sum(r["weight"] for r in results if r["verdict"] == "yes"),
        "denominator": sum(r["weight"] for r in results if r["weight"] > 0),
        "n_items": sum(1 for r in results if not r["is_guardrail"]),
        "n_guardrails": sum(1 for r in results if r["is_guardrail"]),
    }
    doc["process"] = {"score": round(process, 4), "deterministic": round(det_score, 4), "rubric": round(score, 4), "gate": gate}
    doc["composition"] = {"alpha": alpha, "n_targets": n_targets, "reward": reward,
                          "formula": "gate * ((1 - 2a) * outcome + 2a * process)"}
    doc["status"] = _status_of(hard, judged=True)
    doc["reward"] = reward
    doc["reward_formula"] = "gate * ((1 - 2a) * outcome + 2a * process), composed in the verifier"
    lines = []
    for item in results:
        for n, vote in enumerate(item["votes"], start=1):
            lines.append(json.dumps({"item_id": item["id"], "weight": item["weight"], "is_guardrail": item["is_guardrail"],
                                     "evaluation_target": item["evaluation_target"], "vote": n, "verdict": vote,
                                     "majority": item["verdict"], "model": cfg["model"]}, sort_keys=True))
    (out_dir / "verdicts.jsonl").write_text("\n".join(lines) + "\n")
    (out_dir / "final_score.md").write_text(
        f"# Score - {doc['task'].get('instance_id', '')}\n\n"
        f"Status: {doc['status']}  \nGate: {'open' if gate else 'VOID - ' + ', '.join(hard)}  \n"
        f"Judge: {cfg['model']} ({votes} vote(s) per item)  \n\n"
        f"| channel | score |\n|---|--:|\n| outcome | {outcome['score']} |\n"
        f"| deterministic (soft) | {det_score:.4f} |\n| rubric | {score:.4f} |\n"
        f"| **process** = (det + rubric) / 2 | {process:.4f} |\n\n"
        f"| composed score | value |\n|---|--:|\n"
        f"| **reward** = gate*((1-2a)*outcome + 2a*process), a={alpha:g} | {reward} |\n"
    )

Runner = Callable[[dict[str, Any], Path, Path], dict[str, Any]]
# Declared in task.toml artifacts, so a separate verifier receives it.
TRAJECTORY_PATH = Path("/logs/agent/trajectory.json")


class InvalidTrial(Exception):
    def __init__(self, reason: str, detail: str = ""):
        super().__init__(reason)
        self.reason = reason
        self.detail = detail


def _clear(out_dir: Path, names: tuple[str, ...]) -> None:
    for name in names:
        (out_dir / name).unlink(missing_ok=True)


def _write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=False) + "\n")


def _apply(repo: Path, patch_bytes: bytes, reverse: bool = False) -> str | None:
    """git apply the patch from stdin; returns stderr on failure."""
    args = ["apply", "--binary", "--whitespace=nowarn"] + (["-R"] if reverse else [])
    proc = patch.git(repo, *args, "-", stdin=patch_bytes)
    if proc.returncode != 0:
        return proc.stderr.decode("utf-8", "replace") or f"exit {proc.returncode}"
    return None


def _read_log(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def load_rubric(
    tests_dir: Path, instruction: str
) -> tuple[list[dict[str, Any]], float, Any, list[dict[str, str]]]:
    """(grounded items, weight_in_reward, rubric votes, dropped items) per contract C6."""
    path = tests_dir / "rubric.json"
    if not path.exists():
        # Generated bundles carry tests/rubric.json; the delivered flat bundles carry
        # tests/rubrics.json. Their items already validate against this contract -- same
        # id, weight, criterion, evaluation_rule and grounded instruction_quote -- so the
        # only difference was the name. Reading one spelling reported no_grounded_items on
        # every delivered sample and silently dropped the rubric channel.
        path = tests_dir / "rubrics.json"
    if not path.exists():
        return [], DEFAULT_WEIGHT_IN_REWARD, None, []

    def reject(reason: str) -> tuple[list[Any], float, None, list[dict[str, str]]]:
        return [], DEFAULT_WEIGHT_IN_REWARD, None, [{"id": "*", "reason": reason}]

    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        return reject(f"rubric_unreadable: {exc}")
    if not isinstance(data, dict):
        return reject("unsupported_schema_version")
    schema_version = data.get("schema_version")
    # The delivered bundles state no schema_version. Absent is allowed and a wrong one is
    # not, because the per-item validation below is what actually protects the score: an
    # item missing a weight in {1,3,5}, a criterion, an evaluation_rule or a quote that
    # appears verbatim in the instruction is dropped and named in `dropped`. A
    # foreign-shaped file therefore yields no items rather than wrong ones.
    if schema_version is not None and schema_version != "argos-rubric/2":
        return reject("unsupported_schema_version")
    weight = data.get("weight_in_reward", DEFAULT_WEIGHT_IN_REWARD)
    if (
        isinstance(weight, bool)
        or not isinstance(weight, int | float)
        or not 0 <= weight <= MAX_WEIGHT_IN_REWARD
    ):
        return reject(f"weight_in_reward_out_of_range: {weight!r}")
    normalized_instruction = judge.normalize(instruction)
    items: list[dict[str, Any]] = []
    dropped: list[dict[str, str]] = []
    seen: set[str] = set()
    for raw, from_guardrails in [(x, False) for x in data.get("items") or []] + [
        (x, True) for x in data.get("guardrails") or []
    ]:
        item = raw if isinstance(raw, dict) else {}
        item_id = item.get("id")
        quote = item.get("instruction_quote")
        quote = judge.normalize(quote) if isinstance(quote, str) else ""
        reason = None
        if not isinstance(item_id, str) or not item_id:
            reason = "missing_id"
        elif item_id in seen:
            reason = "duplicate_id"
        elif type(item.get("weight")) is not int or abs(item["weight"]) not in (
            1,
            3,
            5,
        ):
            # abs(): a guardrail prices its harm with a negative weight. Testing the
            # signed value rejected every guardrail as invalid_weight, which is half
            # of why the guardrail channel never reached the judge.
            reason = "invalid_weight"
        elif not all(
            isinstance(item.get(k), str) and item[k].strip()
            for k in ("criterion", "evaluation_rule")
        ):
            reason = "missing_criterion_or_evaluation_rule"
        elif not from_guardrails and (
            len(quote) < MIN_QUOTE_CHARS or quote not in normalized_instruction
        ):
            # Grounding is enforced on requirement items only. A guardrail is authored
            # against the protocol rather than derived from the instruction, so none
            # carry a quote; demanding one dropped the entire channel.
            reason = "ungrounded_instruction_quote"
        if reason is not None:
            dropped.append({"id": str(item_id), "reason": reason})
            continue
        seen.add(str(item_id))
        keys = ("id", "weight", "criterion", "evaluation_rule")
        entry: dict[str, Any] = {k: item[k] for k in keys}
        entry["instruction_quote"] = item.get("instruction_quote")
        entry["evaluation_target"] = item.get("evaluation_target") or "final_diff"
        entry["is_guardrail"] = item["weight"] < 0
        items.append(entry)
    return items, float(weight), data.get("votes"), dropped


def _grade(
    ctx: dict[str, Any],
    tests_dir: Path,
    patch_path: Path,
    out_dir: Path,
    env: Mapping[str, str],
    runner: Runner | None,
    trajectory_path: Path,
) -> dict[str, Any]:
    # Load everything the grade depends on before agent code runs in tests.
    ctx["stage"] = "load"
    cfg = json.loads((tests_dir / "config.json").read_text())
    ctx["task"] = {
        "name": cfg.get("task_name"),
        "instance_id": cfg.get("instance_id"),
        "uuid_v5": cfg.get("uuid_v5"),
        # Recorded at generation; the trial repeats them so a run says which
        # tree built it and which toolchain graded it (PRD R7).
        "harness_commit": cfg.get("harness_commit"),
        "msb_rev": cfg.get("msb_rev"),
    }
    test_patch_path = tests_dir / "test.patch"
    test_patch_bytes = test_patch_path.read_bytes() if test_patch_path.exists() else b""
    instruction_path = tests_dir / "instruction.md"
    instruction = instruction_path.read_text() if instruction_path.exists() else ""
    items, weight, rubric_votes, dropped = load_rubric(tests_dir, instruction)
    sites, generated_paths = deterministic.load_sites(_rubric_doc(tests_dir))

    ctx["stage"] = "patch"
    try:
        raw_patch = patch_path.read_bytes()
    except OSError as exc:
        raise InvalidTrial("patch_artifact_missing", f"{patch_path}: {exc}") from exc

    ctx["stage"] = "environment"
    repo_dir = Path(cfg["repo_dir"]).resolve()
    if not repo_dir.is_dir():
        raise InvalidTrial("environment_unclean", f"repo_dir {repo_dir} is missing")
    head = patch.git(repo_dir, "rev-parse", "HEAD")
    head_sha = head.stdout.decode().strip()
    if head.returncode != 0 or head_sha != cfg.get("base_commit"):
        raise InvalidTrial(
            "environment_unclean",
            f"HEAD {head_sha or head.stderr.decode('utf-8', 'replace')!r} "
            f"!= base_commit {cfg.get('base_commit')!r}",
        )
    git_status = patch.git(repo_dir, "status", "--porcelain")
    lines = git_status.stdout.decode("utf-8", "replace").splitlines()
    modified = [line for line in lines if not line.startswith("??")]
    if git_status.returncode != 0 or modified:
        stderr = git_status.stderr.decode("utf-8", "replace")
        detail = stderr or "\n".join(modified[:50])
        raise InvalidTrial("environment_unclean", f"modified tracked files:\n{detail}")

    ctx["stage"] = "filter"
    try:
        filtered = patch.filter_patch(repo_dir, raw_patch, test_patch_bytes)
    except patch.PatchApplyError as exc:
        raise InvalidTrial("patch_apply_failed", str(exc)) from exc
    filtered_bytes = filtered.text
    (out_dir / "filtered.patch").write_bytes(filtered_bytes)
    patch_block = {
        "files_total": filtered.files_total,
        "files_applied": filtered.applied,
        "stripped_files": filtered.stripped,
        "empty_after_filter": not filtered.applied,
    }

    def rubric_block() -> dict[str, Any] | None:
        """What the host judge will grade, not a verdict: the judge needs the
        network and this container is sealed."""
        if not items:
            return None
        return {
            "status": "deferred_to_host",
            "weight_in_reward": weight,
            "votes": rubric_votes,
            "items": [item["id"] for item in items],
            "dropped_items": dropped,
        }

    def deterministic_block(
        diagnostics: dict[str, Any], score: float | None, binary: float | None
    ) -> dict[str, Any]:
        """The checks this verifier can decide; the host decides the rest.

        The trajectory and the agent's diff are what the process channel reads,
        and both are here (the patch as an artifact, the trajectory as a
        declared one). What is not here is result.json, which Harbor writes
        after the verifier exits, so A1/A4/B1/B2/B4 abstain as deferred and
        ``argos.tools.score`` decides them.
        """
        report = deterministic.evaluate(
            deterministic.Context(
                trajectory_path=trajectory_path,
                # The raw patch, not the filtered one: C3 and C4 ask whether the
                # run wrote a graded test, and filtering is what removed it.
                patch_text=patch.decode(raw_patch),
                config=cfg,
                sites=tuple(sites),
                generated_paths=generated_paths,
                diagnostics=diagnostics,
                outcome_score=score,
                outcome_binary=binary,
                test_patch=patch.decode(test_patch_bytes),
            )
        )
        return report.to_dict()

    def document(outcome_block: dict[str, Any]) -> dict[str, Any]:
        """metrics.json: the outcome, the channels measured here, and why."""
        return {
            "schema_version": "argos-metrics/1",
            "grader_version": ctx["grader_version"],
            "task": ctx["task"],
            "reward": outcome_block["score"],
            "reward_formula": "outcome (process channel composed by the host)",
            "outcome": outcome_block,
            "patch": patch_block,
            "control": ctx.get("control"),
            "deterministic": deterministic_block(
                outcome_block["diagnostics"],
                outcome_block["score"],
                float(outcome_block["resolved"]),
            ),
            "rubric": rubric_block(),
        }

    def zero_outcome(status: str, diagnostics: dict[str, Any]) -> dict[str, Any]:
        return {
            "score": 0.0,
            "resolved": 0,
            "status": status,
            "diagnostics": diagnostics,
        }

    if not filtered.applied:
        return document(zero_outcome("empty_patch", {}))

    if runner is None:
        # Load the MSB parser while the repo is still clean: tests run agent code
        # as root, which could otherwise edit multi_swe_bench before it is imported.
        ctx["stage"] = "load_parser"
        runner = functools.partial(msb.run_tests, instance=msb.load_instance(cfg))

    # The baseline is measured here, not read from the record: the dataset's test
    # stage was measured elsewhere, usually with network up. scapy recorded 27
    # p0f/nmap "Fetch database" tests passing that a sealed verifier cannot run,
    # so its gold patch scored 0.0 against the recorded set. The agent's work is
    # set aside by construction -- it is the patch file, not yet applied, and the
    # environment check above refused anything but a clean tree at base_commit.
    ctx["stage"] = "control"
    control_log = out_dir / "control-output.log"
    control_stage = runner(cfg, tests_dir, control_log)
    reason = msb.invalid_reason(control_stage, _read_log(control_log))
    if reason is not None:
        raise InvalidTrial(
            "environment_broken",
            f"control run (base + test.patch) is not scorable: {reason} "
            f"(exit {control_stage.get('exit_code')})",
        )
    ctx["stage"] = "restore"
    if (error := patch.restore_base(repo_dir, cfg["base_commit"])) is not None:
        raise InvalidTrial("control_restore_failed", error)
    excluded = sorted(
        set(cfg.get("p2p_tests") or {}) & set(control_stage["failed_tests"])
    )
    ctx["control"] = {
        "passed": len(control_stage["passed_tests"]),
        "failed": len(control_stage["failed_tests"]),
        "skipped": len(control_stage["skipped_tests"]),
        "exit_code": control_stage.get("exit_code"),
        "excluded_p2p": excluded,
    }

    ctx["stage"] = "apply"
    error = _apply(repo_dir, filtered_bytes)
    if error is not None:
        raise InvalidTrial("patch_apply_failed", error)

    ctx["stage"] = "tests"
    fix_log = out_dir / "test-output.log"
    fix_stage = runner(cfg, tests_dir, fix_log)
    if (reason := msb.invalid_reason(fix_stage, _read_log(fix_log))) is not None:
        # The same command in the same container scored the control run minutes
        # ago, so the environment is not what changed: the patch is.
        return document(zero_outcome("build_broken_by_patch", {"fix_stage": reason}))

    ctx["stage"] = "score"
    report = {
        # The measured stage, not cfg["test_patch_result"]: the recorded one was
        # measured in another environment (patch 0014).
        "test_patch_result": control_stage,
        "fix_patch_result": fix_stage,
    }
    scored = outcome.compute_score_v2g(cfg, report)
    if scored["status"] != "scored":
        raise InvalidTrial(
            f"task_invalid:{scored['status']}", json.dumps(scored["diagnostics"])
        )
    outcome_block = {
        "score": float(scored["scores"]["score"]),
        "resolved": int(scored["scores"]["score_binary"]),
        "status": "scored",
        "diagnostics": scored["diagnostics"],
    }
    return document(outcome_block)


def _rubric_doc(tests_dir: Path) -> dict[str, Any] | None:
    """tests/rubric.json as a document, for its ``sites`` table. None when absent."""
    for name in ("rubric.json", "rubrics.json"):
        path = tests_dir / name
        if path.is_file():
            try:
                doc = json.loads(path.read_text())
            except ValueError:
                return None
            return doc if isinstance(doc, dict) else None
    return None


def run(
    tests_dir: Path,
    patch_path: Path,
    out_dir: Path,
    env: Mapping[str, str] | None = None,
    runner: Runner | None = None,
    trajectory_path: Path = TRAJECTORY_PATH,
) -> dict[str, Any]:
    """Grade and write outputs; returns the grading or invalid document. Never raises
    for trial-level failures (they become invalid.json)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    _clear(out_dir, FINAL_OUTPUTS + RUN_LOGS)
    ctx: dict[str, Any] = {
        "stage": "load",
        "task": {"name": None, "instance_id": None, "uuid_v5": None},
        "grader_version": grader_version(),
    }
    try:
        doc = _grade(
            ctx,
            tests_dir,
            patch_path,
            out_dir,
            os.environ if env is None else env,
            runner,
            trajectory_path,
        )
        # Tests ran agent code: drop anything it may have planted, reward last.
        _clear(out_dir, FINAL_OUTPUTS)
        _judge_and_compose(doc, out_dir, tests_dir)
        _write_json(out_dir / "metrics.json", doc)
        outcome_block = doc["outcome"]
        reward_json = {
            "reward": doc["reward"],
            "score_outcome": outcome_block["score"],
            "score_binary": float(outcome_block["resolved"]),
        }
        if "composition" in doc:
            reward_json["score_process"] = doc["process"]["score"]
            reward_json["gate"] = doc["process"]["gate"]
            reward_json["alpha"] = doc["composition"]["alpha"]
        _write_json(out_dir / "reward.json", reward_json)
        return doc
    except InvalidTrial as exc:
        reason, detail = exc.reason, exc.detail
    except Exception:
        reason, detail = "grader_crashed", traceback.format_exc()
    invalid = {
        "schema_version": "argos-invalid/1",
        "grader_version": ctx["grader_version"],
        "reason": reason,
        "stage": ctx["stage"],
        "detail": detail,
        "task": ctx["task"],
    }
    _clear(out_dir, FINAL_OUTPUTS)
    _write_json(out_dir / "invalid.json", invalid)
    return invalid
