# Score — opus-5/run_3

Task: DTStack__molecule-641 (`46ab8719-a8fe-496f-95a5-42f3bc3def5d`)  
Status: scored  
Gate: open  
Judge: gpt-5.6-sol  

| channel | score |
|---|--:|
| outcome | 0.0 |
| deterministic (soft) | 0.6667 |
| rubric | 0.6368 |
| **process** = (det + rubric) / 2 | 0.6517 |

| composed score | value |
|---|--:|
| **score_eval** = gate·((1−2α)·outcome + 2α·process), α=0.05 | 0.0652 |
| **score_rl** — same form over the process score normalised within this task's outcome stratum | 0.0934 |

<!-- quality -->
## Quality (publish-only, never part of reward)

Judge: gpt-5.6-sol  
Version: quality-v1, prompt 6169e82413340627  
Status: scored (shadow, uncalibrated)  

| dimension | verdict |
|---|---|
| conventions (Q1) | fail |
| minimal_diff (Q2) | pass |
| abstraction (Q3) | fail |
| readability (Q4) | pass |
| naming (Q5) | fail |
| idiomaticity (Q6) | pass |
| dead_code (Q7) | pass |
| **score_quality** = passed weight / total weight | 0.5714 |
<!-- /quality -->
