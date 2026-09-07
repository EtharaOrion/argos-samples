# Score — glm-5.3/run_2

Task: DTStack__molecule-641 (`46ab8719-a8fe-496f-95a5-42f3bc3def5d`)  
Status: scored  
Gate: open  
Judge: gpt-5.6-sol  

| channel | score |
|---|--:|
| outcome | 0.0 |
| deterministic (soft) | 0.3333 |
| rubric | 0.2861 |
| **process** = (det + rubric) / 2 | 0.3097 |

| composed score | value |
|---|--:|
| **score_eval** = gate·((1−2α)·outcome + 2α·process), α=0.05 | 0.0310 |
| **score_rl** — same form over the process score normalised within this task's outcome stratum | 0.0086 |

<!-- quality -->
## Quality (publish-only, never part of reward)

Judge: gpt-5.6-sol  
Version: quality-v1, prompt 6169e82413340627  
Status: scored (shadow, uncalibrated)  

| dimension | verdict |
|---|---|
| conventions (Q1) | pass |
| minimal_diff (Q2) | fail |
| abstraction (Q3) | fail |
| readability (Q4) | pass |
| naming (Q5) | fail |
| idiomaticity (Q6) | pass |
| dead_code (Q7) | fail |
| **score_quality** = passed weight / total weight | 0.4286 |
<!-- /quality -->
