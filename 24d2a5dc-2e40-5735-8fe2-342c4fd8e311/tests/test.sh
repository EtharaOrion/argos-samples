#!/bin/bash
# Runs the vendored Argos grader (tests/argos_grader/README.md). Always exits 0:
# the trial result is /logs/verifier/reward.json (scored) or invalid.json.
set -u
# Agent code can plant modules in the repo (the image WORKDIR) or in /: run from /
# with -P so python never imports from the cwd.
cd / || exit 0
out=/logs/verifier
mkdir -p "$out"
rm -f "$out/reward.json" "$out/reward.txt" "$out/invalid.json" "$out/grading.json"
PYTHONPATH=/tests /opt/python/bin/python3 -P -m argos_grader \
  --tests-dir /tests --patch /logs/artifacts/agent.patch --out-dir "$out"
rc=$?
# The grader exits 0 after writing its result. Otherwise (e.g. agent test code
# killed it) anything in $out may be planted, so it is discarded.
if [ "$rc" -ne 0 ] || { [ ! -f "$out/reward.json" ] && [ ! -f "$out/invalid.json" ]; }; then
  rm -f "$out/reward.json" "$out/reward.txt" "$out/grading.json"
  printf '{"schema_version": "argos-invalid/1", "reason": "grader_crashed", "stage": "test.sh", "detail": "argos_grader exited %s"}\n' \
    "$rc" > "$out/invalid.json"
fi
# The two are exclusive, and Harbor reads reward.json first.
if [ -f "$out/invalid.json" ]; then rm -f "$out/reward.json" "$out/reward.txt"; fi
exit 0
