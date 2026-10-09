GENERATED SECTION. DO NOT HAND-EDIT.

<p align="center"><img src="images/hero.svg" alt="Argos" width="720"></p>

# Argos: samples

<p align="center"><b>The samples lane: 3 of 30 Harbor task bundles.</b></p>

<p align="center"><a href="#summary"><img src="https://img.shields.io/badge/bundles-3_of_30-845EF7" alt="bundles: 3 of 30"></a> <a href="#evidence-status"><img src="https://img.shields.io/badge/sealed-0-845EF7" alt="sealed: 0"></a> <a href="#difficulty-tiers"><img src="https://img.shields.io/badge/difficulty-measured-845EF7" alt="difficulty: measured"></a></p>

<p align="center"><sub><a href="#abstract">Abstract</a> | <a href="#summary">Summary</a> | <a href="#difficulty-tiers">Difficulty tiers</a> | <a href="#evidence-status">Evidence status</a> | <a href="#coverage">Coverage</a> | <a href="#dataset-structure">Dataset structure</a> | <a href="#trajectory-structure">Trajectory structure</a> | <a href="#verification-and-quality-assurance">Verification and quality assurance</a> | <a href="#reproduction">Reproduction</a> | <a href="#cite">Cite</a> | <a href="#license">License</a> | <a href="#contact">Contact</a></sub></p>

## Abstract

The curated lane of this corpus: at most 30 Harbor task bundles, every anchor seated first and every other bundle in seal order. Bundles past that ceiling live in `delivery/`.

Each bundle is one Harbor task in a directory named by its content-derived uuid5, so the name doubles as an integrity check. This page is rendered from the resident bundles on every reconcile; a value a bundle does not carry reads `absent`, and the page never fills one in.

## Summary

| Property | Value |
| --- | --- |
| Bundles | 3 of 30 |
| Sealed | 0 of 3 |
| Registrations | unregistered (3) |
| Audit verdicts | none (3) |
| Harbor schema | 1.4 (3) |

## Difficulty tiers

Difficulty is measured by the signed pilot alone and never declared in a bundle, so this page states no tier a bundle claims.

## Evidence status

The verdict is the audit outcome recorded at the sealed digest, and `none` means no verdict has landed for that digest yet. Only a FORGE invocation removes a bundle from this lane, so removal waits for the next one.

| uuid | Verdict | Sealed digest | Stream |
| --- | --- | --- | --- |
| 24d2a5dc-2e40-5735-8fe2-342c4fd8e311 | none | absent | none |
| 276ad6ba-10da-5f87-82ea-c2abc44dfdea | none | absent | none |
| 4056d683-bddd-57a4-8cf3-e807654c7c9c | none | absent | none |

## Coverage

| Keyword | Bundles |
| --- | --- |
| issue-resolving | 3 |
| python | 2 |
| air | 1 |
| gitoxide | 1 |
| rust | 1 |
| scapy | 1 |

## Dataset structure

| Bundle | Task | Keywords | Registration | Sealed at |
| --- | --- | --- | --- | --- |
| [`24d2a5dc-2e40-5735-8fe2-342c4fd8e311`](24d2a5dc-2e40-5735-8fe2-342c4fd8e311/) | `argos/GitoxideLabs__gitoxide-2191` | gitoxide, issue-resolving, rust | unregistered | unsealed |
| [`276ad6ba-10da-5f87-82ea-c2abc44dfdea`](276ad6ba-10da-5f87-82ea-c2abc44dfdea/) | `argos/feldroy__air-246` | air, issue-resolving, python | unregistered | unsealed |
| [`4056d683-bddd-57a4-8cf3-e807654c7c9c`](4056d683-bddd-57a4-8cf3-e807654c7c9c/) | `argos/secdev__scapy-3461` | issue-resolving, python, scapy | unregistered | unsealed |

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#131a33","primaryTextColor":"#e8ecff","primaryBorderColor":"#845EF7","lineColor":"#22d3ee","fontFamily":"monospace"}}}%%
flowchart LR
    bundle["&lt;uuid&gt;/"]
    bundle --> n0["task.toml<br/>runner manifest"]
    bundle --> n1["instruction.md<br/>objective the agent reads"]
    bundle --> n2["environment/<br/>agent sandbox image"]
    bundle --> n3["tests/<br/>verifier, hidden from the agent"]
    bundle --> n4["solution/<br/>private oracle"]
    bundle --> n5["trajectories/<br/>private rollout evidence"]
```

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#131a33","primaryTextColor":"#e8ecff","primaryBorderColor":"#845EF7","lineColor":"#22d3ee","fontFamily":"monospace"}}}%%
flowchart LR
    staging["staging/"]
    staging --> samples["samples/<br/>3 of 30"]
    samples --> delivery["delivery/<br/>0 of 10000"]
    delivery --> stock["stock/<br/>0 of 10000"]
```

## Trajectory structure

3 of 3 resident bundles carry a `trajectories/` subtree of private rollout evidence. The signed pilot reads it; this page never restates a rollout.

## Verification and quality assurance

Each bundle's signed provenance carrier holds its screening roots, screening instant, and absolute expiry. Placement moves that carrier into the private derivation set, which this page never reads, so reconcile lists no root it cannot verify here.

## Reproduction

Each bundle directory is a complete Harbor task: `task.toml` is the runner manifest, `instruction.md` the objective, `environment/` the sandbox image, and `tests/` the verifier. Point a Harbor runner at one bundle directory to reproduce it; `solution/` and `trajectories/` stay private.

## Cite

```bibtex
@misc{argos2026,
  title  = {Argos: Execution-Verified Reinforcement Learning Environments for Agentic Software Engineering},
  author = {{Ethara.AI}},
  year   = {2026},
  note   = {Task corpus, container environments, and recorded solver trajectories}
}
```

## License

Released under the MIT License, Copyright (c) 2026 Ethara.AI. See [LICENSE](LICENSE) for the full text. Task bundles pin third party repositories at specific commits and those repositories remain under their own licenses.

## Contact

Ethara.AI is at [github.com/EtharaOrion](https://github.com/EtharaOrion). For a vulnerability or a benchmark-integrity concern, including a leaked task byte, a contamination report, or a gameable shortcut, write to security@ethara.ai rather than opening a public issue. For conduct concerns, write to conduct@ethara.ai.
