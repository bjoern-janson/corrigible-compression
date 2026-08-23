# BL-002 Audited Result and Execution Provenance

Status:

```text
BL-002 = POSITIVE — ACTIVE SURVEYING
execution provenance = RECOVERED VIA VALIDATED SEMANTIC-EQUIVALENCE EVALUATOR
reference executable = TIMED OUT / NO RESULT PAYLOAD
```

This record preserves the scientific result **and** the execution-provenance qualification. It must not be rewritten later as if the committed reference executable completed normally.

## Frozen scientific specification

Design branch:

```text
bl-002/specification-001
```

Design-freeze commit:

```text
80b77f1ba98a669f191742738cc95186d3971441
```

Committed reference executable blob:

```text
experiments/bl002.py
blob SHA = 48f6321e3f238f402e144c6284c8d94512fabd91
```

BL-002 inherited the BL-001 world family and downstream topology-inference / depth-allocation machinery. The newly tested capability was only:

```text
E_t -> q_(t+1)
```

under the same supplied finite topology family, measurement budget, deterministic common-randomness field, posterior topology inference, and downstream allocation machinery.

Load-bearing boundary:

```text
T* in H
```

Therefore this is active surveying **within a supplied topology family**, not topology invention.

## Pre-run audit

The committed audit-only path passed before scientific execution:

```text
32 unique candidate topologies
132 candidate directed edges
permutation hash PASS
edge-set hash PASS
policy-family hash PASS
all three fixed comparator sequences reproduce exactly
all fixed comparator hashes PASS
8 unique edges per fixed comparator
```

No conceptual or protocol changes were made between audit and attempted execution.

## Reference-executable execution history

The committed reference invocation was:

```text
python experiments/bl002.py --execute
```

The execution harness timed out before the reference implementation emitted a BL-002 result payload. Repeated identical attempts also timed out. These interruptions are apparatus/runtime events, not scientific outcomes.

The record is therefore:

```text
reference executable
-> frozen audit PASS
-> --execute
-> runtime timeout
-> no result payload
```

No scientific code, constants, policy definitions, noise field, seed schedule, tie-breaking, or analysis rule was changed in response to the timeout.

## Semantic-equivalence recovery

To recover the frozen result without redesigning the assay, a vectorized evaluator implementing the same frozen equations, deterministic edge-indexed noise field, policy semantics, posterior inference, allocation rule, regret definition, and world-level analysis was used.

Before accepting the recovered aggregate, the evaluator was cross-checked against the committed scalar/reference semantics on 30 selected policy/specimen evaluations:

```text
15 adaptive evaluations
15 matched fixed evaluations
```

For every cross-check, the following agreed exactly:

```text
measurement sequence
posterior
posterior-mean topology
selected depth action
regret
```

Thus the accepted execution provenance is:

```text
reference executable
-> timeout / no payload

semantically equivalent evaluator
-> 30 scalar cross-checks
-> exact agreement on sequence/posterior/map/action/regret
-> recovered aggregate result
```

This provenance qualifier is permanent.

## Primary result

Frozen primary estimand:

```text
Delta_BL2 = E_world E_noise [ R_adaptive_family - R_fixed_family ]
```

Recovered value:

```text
Delta_BL2 = -0.00014556248982747346
```

Frozen world-level one-sample directional analysis:

```text
t(31) = -2.84807
one-sided p = 0.00387079
one-sided 95% upper confidence bound = -0.0000589060
95% two-sided CI = [-0.000249800, -0.0000413247]
```

Because the preregistered one-sided 95% upper bound is below zero:

```text
ACTIVE_SURVEYING_ADDS_ALLOCATION_VALUE
```

Mean regret:

```text
R_adaptive_family = 0.00000144323
R_fixed_family    = 0.000147006
```

The earned scientific edge is therefore only:

```text
existing evidence
-> adaptive measurement choice
-> better allocation of scarce depth
```

within the frozen supplied-family synthetic setting.

## Diagnostic decomposition

### 1. Adaptivity expressed

PASS.

Every adaptive selector diverged from its matched fixed measurement sequence in all 8192 paired specimens:

```text
VAR          8192 / 8192
EDGE_ENTROPY 8192 / 8192
ACTION_MI    8192 / 8192
```

First divergence:

```text
EDGE_ENTROPY: measurement 2 in every specimen
ACTION_MI:    measurement 2 in every specimen
VAR:          measurement 2 in 7552 specimens
              measurement 3 in  640 specimens
```

Therefore the tested edge `E_t -> q_(t+1)` was actually exercised.

### 2. Global topology reconstruction

A statistically secured global-map improvement was **not demonstrated** under the frozen family-level MSE diagnostic.

```text
Delta_MSE = MSE_adaptive - MSE_fixed
          = -0.000569009
one-sided 95% upper bound = +0.000485282
```

Since the upper bound crosses zero, BL-002 does not earn a claim that adaptive surveying improves global topology MSE.

Posterior entropy likewise did not show a secured family-level improvement:

```text
Delta_H = H_adaptive - H_fixed
        = -0.0313078
one-sided 95% upper bound = +0.0246742
```

Therefore BL-002 does not earn a claim that adaptive surveying demonstrably reduces posterior entropy.

### 3. Allocation consequence

PASS.

Despite no statistically secured global-map-MSE or posterior-entropy improvement, the preregistered allocation endpoint was positive:

```text
Delta_BL2 < 0
and
UCB_95%,1s(Delta_BL2) < 0
```

So the durable negative distinction is:

```text
better allocation
!=
demonstrably better global topology reconstruction
```

A stronger descriptive compression is:

> Measurement can become more decision-relevant without making the overall map measurably better under the frozen global diagnostics.

This remains a BL-002 specimen result, not a universal theorem.

## Per-rule descriptive results

These were frozen as descriptive only and cannot redefine the primary endpoint.

```text
VAR
  allocation Delta = -0.0000620969
  one-sided 95% UCB = -0.0000219780

EDGE_ENTROPY
  allocation Delta = -0.0000222905
  one-sided 95% UCB = -0.00000768870

ACTION_MI
  allocation Delta = -0.000352300
  one-sided 95% UCB = -0.0000978412
```

All three candidate adaptive rules had negative descriptive allocation contrasts, but no method-selection claim is earned from these secondary comparisons.

## Claim ceiling

BL-002 earns only:

> Within this frozen finite supplied topology family, conditioning future measurement choices on previously observed evidence improved eventual allocation of a scarce local-learning operation relative to matched fixed measurement selection under the same budget and stochastic field.

It does **not** establish:

```text
topology invention
out-of-family topology construction
general active learning
real neural competence topology
human knowledge geometry
broad intelligence
```

In particular:

```text
T* in H
```

remains load-bearing.

## Broad-learning ledger after BL-002

```text
BL-001 = POSITIVE — TOPOLOGY UTILIZATION
BL-002 = POSITIVE — ACTIVE SURVEYING
BL-003 = QUESTION EARNED — NOT DESIGNED / UNOPENED AS AN ASSAY
```

The earned BL-003 frontier question is only:

> Can the learner construct useful relational structure that was not already supplied by the candidate topology family?

No BL-003 acquisition rule, topology representation, benchmark family, endpoint, or executable design is introduced by this result artifact.

## Permanent provenance rule

Future summaries must preserve both facts simultaneously:

```text
scientific classification:
ACTIVE_SURVEYING_ADDS_ALLOCATION_VALUE

execution provenance:
RECOVERED VIA VALIDATED SEMANTIC-EQUIVALENCE EVALUATOR;
REFERENCE EXECUTABLE TIMED OUT WITHOUT A RESULT PAYLOAD
```

Do not compress the second fact away when citing the first.
