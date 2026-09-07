# Score — glm-5.3/run_7

Task: secdev__scapy-3461 (`1213efa9-10ca-4f0e-bb27-2f6012454212`)  
Status: scored  
Gate: open  
Judge: gpt-5.6-sol  

| channel | score |
|---|--:|
| outcome | 0.0 |
| deterministic (soft) | 0.6667 |
| rubric | 0.8365 |
| **process** = (det + rubric) / 2 | 0.7516 |

| composed score | value |
|---|--:|
| **score_eval** = gate·((1−2α)·outcome + 2α·process), α=0.05 | 0.0752 |
| **score_rl** — same form over the process score normalised within this task's outcome stratum | 0.1000 |

<!-- quality -->
## Quality (publish-only, never part of reward)

Judge: gpt-5.6-sol  
Version: quality-v1, prompt 6169e82413340627  
Status: scored (shadow, uncalibrated)  

| dimension | verdict |
|---|---|
| conventions (Q1) | pass |
| minimal_diff (Q2) | pass |
| abstraction (Q3) | fail |
| readability (Q4) | pass |
| naming (Q5) | pass |
| idiomaticity (Q6) | pass |
| dead_code (Q7) | pass |
| **score_quality** = passed weight / total weight | 0.8571 |
<!-- /quality -->
