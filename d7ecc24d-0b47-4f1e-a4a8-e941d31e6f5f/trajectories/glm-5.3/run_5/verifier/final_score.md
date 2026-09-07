# Score — glm-5.3/run_5

Task: feldroy__air-246 (`d7ecc24d-0b47-4f1e-a4a8-e941d31e6f5f`)  
Status: scored  
Gate: open  
Judge: gpt-5.6-sol  

| channel | score |
|---|--:|
| outcome | 0.17 |
| deterministic (soft) | 0.2857 |
| rubric | 0.8782 |
| **process** = (det + rubric) / 2 | 0.5820 |

| composed score | value |
|---|--:|
| **score_eval** = gate·((1−2α)·outcome + 2α·process), α=0.05 | 0.2112 |
| **score_rl** — same form over the process score normalised within this task's outcome stratum | 0.2030 |

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
| naming (Q5) | pass |
| idiomaticity (Q6) | pass |
| dead_code (Q7) | pass |
| **score_quality** = passed weight / total weight | 1.0000 |
<!-- /quality -->
