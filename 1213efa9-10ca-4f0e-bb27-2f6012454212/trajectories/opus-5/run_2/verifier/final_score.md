# Score — opus-5/run_2

Task: secdev__scapy-3461 (`1213efa9-10ca-4f0e-bb27-2f6012454212`)  
Status: scored  
Gate: open  
Judge: gpt-5.6-sol  

| channel | score |
|---|--:|
| outcome | 0.67 |
| deterministic (soft) | 0.4444 |
| rubric | 0.8257 |
| **process** = (det + rubric) / 2 | 0.6351 |

| composed score | value |
|---|--:|
| **score_eval** = gate·((1−2α)·outcome + 2α·process), α=0.05 | 0.6665 |
| **score_rl** — same form over the process score normalised within this task's outcome stratum | 0.6030 |

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
