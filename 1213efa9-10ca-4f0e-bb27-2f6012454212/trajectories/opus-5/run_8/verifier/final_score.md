# Score — opus-5/run_8

Task: secdev__scapy-3461 (`1213efa9-10ca-4f0e-bb27-2f6012454212`)  
Status: scored  
Gate: open  
Judge: gpt-5.6-sol  

| channel | score |
|---|--:|
| outcome | 0.67 |
| deterministic (soft) | 0.8333 |
| rubric | 0.9661 |
| **process** = (det + rubric) / 2 | 0.8997 |

| composed score | value |
|---|--:|
| **score_eval** = gate·((1−2α)·outcome + 2α·process), α=0.05 | 0.6930 |
| **score_rl** — same form over the process score normalised within this task's outcome stratum | 0.7030 |

<!-- quality -->
## Quality (publish-only, never part of reward)

Judge: gpt-5.6-sol  
Version: quality-v1, prompt 6169e82413340627  
Status: scored (shadow, uncalibrated)  

| dimension | verdict |
|---|---|
| conventions (Q1) | pass |
| minimal_diff (Q2) | pass |
| abstraction (Q3) | pass |
| readability (Q4) | pass |
| naming (Q5) | fail |
| idiomaticity (Q6) | pass |
| dead_code (Q7) | fail |
| **score_quality** = passed weight / total weight | 0.7143 |
<!-- /quality -->
