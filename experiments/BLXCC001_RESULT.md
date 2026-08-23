# BL×CC-001 Audited Result

Status:

```text
BL×CC-001 = POSITIVE — CORRECTIVE INFLUENCE ADDS SUSTAINED ESCAPE
execution provenance = REFERENCE EXECUTABLE COMPLETED
post-run audit = PASS
```

This result comes from the prospectively frozen reference executable and science seed schedule. The design-stage calibration prediction is preserved separately and is not used as evidence.

## Frozen lineage

Freeze branch:

```text
blxcc-001/freeze-completion
```

Prospective freeze/audit head:

```text
ba69512b51d6d3aac82358c3c0a92cd2d750200c
```

Frozen protocol blob:

```text
experiments/BLXCC001_PROTOCOL.md
7991d82df732df513d1c81b5af4fd17cc5aefbab
```

Frozen reference executable blob:

```text
experiments/blxcc001.py
bf4c72a9c2cdb102f55fdead71a82a0120fe5caa
```

Frozen configuration SHA256:

```text
3b06b39fb942aaecdccad138ceb763a5495092231e5a26bf07c2d0fc921559ba
```

Before scientific execution, the exact frozen executable blob was materialized and its Git object hash was independently recomputed as:

```text
bf4c72a9c2cdb102f55fdead71a82a0120fe5caa
```

The exact audit-only invocation then reproduced:

```text
PRE_RUN_AUDIT_PASS
22 / 22 checks PASS
config hash matches
science_execution_performed = false
```

Scientific execution was then opened exactly as frozen:

```text
python experiments/blxcc001.py --execute
```

No protocol, executable, parameter, seed schedule, endpoint, or analysis rule was changed between freeze and execution.

## Raw result provenance

The untouched raw JSON is stored at:

```text
experiments/BLXCC001_RAW_RESULT.json
```

SHA256 of the raw result payload:

```text
ededa31557928037fa8b167d0afe6543ed016ae028915f801275b6f654d1c79c
```

The reference executable reported:

```text
execution_provenance = REFERENCE_EXECUTABLE_COMPLETED
n_paired_specimens = 8192
seeds_per_world = 4096
worlds = {L,R}
```

## Primary result

Frozen primary estimand:

```text
Delta_esc = P(A first sustained m=2 correct allocation) - P(B first sustained m=2 correct allocation)
```

Observed sustained-escape rates:

```text
A = 0.61083984375
B = 0.51464843750
```

Therefore:

```text
Delta_esc = +0.09619140625
```

Paired discordances:

```text
A=1, B=0: 1139
A=0, B=1:  351
net favorable discordances: 788
```

Frozen one-sided exact McNemar/binomial test:

```text
p = 1.8858785303612578e-97
alpha = 0.05
```

Because:

```text
Delta_esc > 0
and
p < 0.05
```

the frozen primary classification is:

```text
CORRECTIVE_INFLUENCE_ADDS_SUSTAINED_ESCAPE
```

## Mirror-world decomposition

The primary direction is positive in both mirror worlds:

```text
world L:
  A = 0.601318359375
  B = 0.506591796875
  A-B = +0.094726562500

world R:
  A = 0.620361328125
  B = 0.522705078125
  A-B = +0.097656250000
```

The aggregate result is therefore not being driven by only one orientation of the symmetric world pair.

## Secondary descriptive controls

Frozen as secondary/descriptive only:

```text
C = 0.6380615234375
D = 0.5811767578125

C-D = +0.056884765625
B-D = -0.0665283203125
(A-B)-(C-D) = +0.039306640625
```

These controls cannot redefine the primary classification.

Descriptively, consequence influence improves sustained escape in the map-blind control row as well (`C-D > 0`), but the A/B effect is larger than C/D. Also, the endogenous cut condition B performs worse than the map-blind cut condition D (`B-D < 0`). These are mechanism diagnostics only; BL×CC-001 does not preregister a standalone interaction claim.

## Post-run audit

The post-run audit is stored at:

```text
experiments/BLXCC001_POSTRUN_AUDIT.json
```

Status:

```text
POST_RUN_AUDIT_PASS
```

Verified after execution:

```text
exact frozen executable blob matches
config hash unchanged
reference executable completed
8192 paired specimens present
Delta arithmetic exact
discordant net exactly matches Delta
exact McNemar p recomputes identically
classification follows the frozen rule
all 8192 A/B science pairs are identical through W_corr
all 2541 specimens without a consequence event remain scientifically identical across A/B
A-B positive in both mirror worlds
secondary-control arithmetic exact
prospective prediction remains distinct from observed result
```

A first external post-run audit attempt produced a false audit failure because it compared complete trace dataclasses, including the treatment label `cell="A"` versus `cell="B"`, when checking no-intervention equality. The check was corrected to compare scientific state fields rather than treatment labels and then passed 2541/2541 inactive specimens. This was an audit-implementation correction only; the frozen executable, raw scientific result, and frozen analysis were unchanged.

## Prospective prediction versus observation

Frozen calibration prediction:

```text
Delta_esc^(A-B) ~= +0.08821044
```

Observed result:

```text
Delta_esc^(A-B) = +0.09619140625
```

Difference:

```text
observed - predicted = +0.00798096625
```

The prediction had no role in the frozen decision rule and receives no evidential credit for being close to the observation.

## Earned claim

BL×CC-001 earns only:

> Within this frozen symmetric supplied two-topology synthetic world, fixed allocation-competence state, map-conditioned ordinary throughput-intervention policy, and three-round horizon, allowing the matched ordinary task-consequence likelihood signal to acquire developmental influence increased the probability of first sustained two-round correct allocation relative to cutting only that consequence `W_corr -> U_corr` channel.

The primary empirical edge is therefore:

```text
same wrong but repairable map
+ same endogenous acquisition process
+ same ordinary consequence through W_corr
+ preserved W_corr -> U_corr
-> greater sustained escape from the wrong allocation regime
```

within the frozen specimen.

## What is not earned

This does not establish:

```text
topology invention
out-of-family representation expansion
general corrigible compression
a universal W->U mechanism
a universal acquisition rule
human or neural competence topology
architecture-level blindness repair
retention-stage corrigibility
real-world broad intelligence
```

In particular:

```text
T* in H
```

remains load-bearing.

The C/D controls also do not justify the stronger universal claim that endogenous acquisition is always self-sealing. They are descriptive controls within this finite world and horizon.

## Ledger after execution

```text
BL-001 = POSITIVE — TOPOLOGY UTILIZATION
BL-002 = POSITIVE — ACTIVE SURVEYING
BL-003 = QUESTION EARNED — UNOPENED
CC = META-HYPOTHESIS
BL×CC-001 = POSITIVE — CORRECTIVE INFLUENCE ADDS SUSTAINED ESCAPE
```

BL×CC-001 is evidence for the narrow intersection question inside a supplied representational family. It is not evidence for topology invention and does not by itself validate the full corrigible-compression meta-hypothesis.
