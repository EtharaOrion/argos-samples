"""Patch argos_grader/grade.py (this package) so test.sh can judge the rubric and compose the reward in-container.

Usage: python3 tests/argos_grader/tools/patch_grader.py [path/to/grade.py]   (default: the grade.py beside this tools/ folder)

Adds `_judge_and_compose`: when ARGOS_JUDGE_* is set (task.toml [verifier.env]) it judges the
grounded rubric items with the bundled judge.py and rewrites reward.json/metrics.json with the
composed reward (same math as argos.tools.score); without a judge it leaves the outcome-only
behaviour unchanged. A judge failure records `judge_error` instead of crashing the grader.
"""

import sys
from pathlib import Path

grade_py = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "grade.py"

HELPERS = '''

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
    (out_dir / "verdicts.jsonl").write_text("\\n".join(lines) + "\\n")
    (out_dir / "final_score.md").write_text(
        f"# Score - {doc['task'].get('instance_id', '')}\\n\\n"
        f"Status: {doc['status']}  \\nGate: {'open' if gate else 'VOID - ' + ', '.join(hard)}  \\n"
        f"Judge: {cfg['model']} ({votes} vote(s) per item)  \\n\\n"
        f"| channel | score |\\n|---|--:|\\n| outcome | {outcome['score']} |\\n"
        f"| deterministic (soft) | {det_score:.4f} |\\n| rubric | {score:.4f} |\\n"
        f"| **process** = (det + rubric) / 2 | {process:.4f} |\\n\\n"
        f"| composed score | value |\\n|---|--:|\\n"
        f"| **reward** = gate*((1-2a)*outcome + 2a*process), a={alpha:g} | {reward} |\\n"
    )
'''

old_write = '''        _write_json(out_dir / "metrics.json", doc)
        outcome_block = doc["outcome"]
        _write_json(
            out_dir / "reward.json",
            {
                # The outcome is the reward until the host composes the process
                # channel into it and rewrites this file.
                "reward": outcome_block["score"],
                "score_outcome": outcome_block["score"],
                "score_binary": float(outcome_block["resolved"]),
            },
        )
'''
new_write = '''        _judge_and_compose(doc, out_dir, tests_dir)
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
'''


def main() -> None:
    t = grade_py.read_text()
    if "_judge_and_compose" in t:
        print(f"already patched: {grade_py}")
        return
    anchor_helpers = 'RUN_LOGS = ("test-output.log", "control-output.log", "filtered.patch")\n'
    assert t.count(anchor_helpers) == 1
    t = t.replace(anchor_helpers, anchor_helpers + HELPERS)

    assert t.count(old_write) == 1
    t = t.replace(old_write, new_write)

    if "\nimport os\n" not in t:
        anchor_import = "import json\n"
        assert t.count(anchor_import) == 1
        t = t.replace(anchor_import, "import json\nimport os\n")

    grade_py.write_text(t)
    print(f"patched {grade_py}")


if __name__ == "__main__":
    main()
