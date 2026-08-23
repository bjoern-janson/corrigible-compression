# BL-001 Freeze-Completion Repair

Status before this artifact:

```text
BL-001 = SPECIFICATION_INCOMPLETE
Delta = undefined
```

This artifact completes only four execution degrees of freedom left unresolved by the original BL-001 design:

1. the 32-member candidate topology family `H`;
2. the exact eight measurement pairs `Q8`;
3. deterministic tie-breaking;
4. the seed/noise and analysis schedule.

Everything else in BL-001 remains conceptually unchanged. This is **protocol completion, not scientific redesign**.

No realized world, noise sample, policy output, regret, or allocation outcome was inspected before fixing this artifact.

## Existing frozen scientific design

```text
N = 12
D0 = (0.15,0.15,0.20,0.20,0.40,0.40,0.55,0.55,0.70,0.70,0.85,0.85)
eta = 0.25
sigma = 0.08

T_base[i,(i+1) mod 12] = 0.60
T_base[i,(i+3) mod 12] = 0.35
T_base[i,(i+5) mod 12] = 0.15
all other off-diagonal entries = 0
```

For a chosen deep-probe region `i`:

```text
D'_i = D_i + eta * (1-D_i)
D'_j = D_j + eta * T*[i,j] * (1-D_j), j != i
G(D) = mean_j D_j
```

Measurements:

```text
Y_ij = T*[i,j] + epsilon_ij
epsilon_ij ~ Normal(0, sigma^2)
```

Policies remain:

- `P_topo`: uniform prior over `H`, Gaussian likelihood on the same eight measurements, posterior-mean topology completion, then choose the action maximizing posterior-expected `G(D')`.
- `P_raw`: same eight measurements; measured entries equal `Y`; unmeasured entries remain at their prior marginal means; choose the action maximizing estimated `G(D')`.
- `P_depth`: ignore transfer and choose maximal local headroom.
- `P_random`: uniform random action; descriptive only.
- `P_oracle`: use the realized `T*`; upper bound only.

Primary regret:

```text
R_P = G(D'_(oracle)) - G(D'_(P))
Delta = R_topo - R_raw
```

## 1. Candidate topology family H

Node indices are zero-based.

For each permutation `p = (p_0,...,p_11)`, relabel the base topology by

```text
T^(h)[p_i,p_j] = T_base[i,j].
```

The frozen 32 permutations, in candidate order `h = 0,...,31`, are:

```json
[
  [6,3,7,5,1,4,0,10,8,11,9,2],
  [5,4,3,7,6,1,2,10,9,11,8,0],
  [7,2,9,0,1,10,5,8,11,3,6,4],
  [4,10,3,11,8,6,7,0,9,5,2,1],
  [1,11,6,7,0,4,5,3,9,2,10,8],
  [2,11,6,4,0,5,3,1,7,8,9,10],
  [5,8,6,3,11,2,0,4,7,10,1,9],
  [8,0,9,10,7,2,4,1,5,6,11,3],
  [10,1,3,11,4,7,5,9,6,8,2,0],
  [5,2,0,4,10,1,8,6,9,7,11,3],
  [10,5,0,1,9,3,6,7,8,4,11,2],
  [11,10,7,3,6,1,5,0,2,8,4,9],
  [8,0,10,5,1,7,2,9,11,4,6,3],
  [11,1,3,5,9,2,6,8,0,4,7,10],
  [1,9,8,6,3,0,2,7,5,10,4,11],
  [3,7,0,6,1,10,2,4,9,5,11,8],
  [10,8,2,1,4,6,9,3,11,0,7,5],
  [11,7,0,2,10,5,8,1,3,6,9,4],
  [11,4,9,2,1,6,3,7,8,10,5,0],
  [3,1,4,8,2,11,7,10,0,6,5,9],
  [7,1,9,2,10,11,4,0,6,5,3,8],
  [7,11,6,9,2,4,1,3,10,0,8,5],
  [11,4,0,2,6,1,8,7,10,9,3,5],
  [1,9,3,2,5,11,7,8,6,4,0,10],
  [6,3,4,9,7,1,2,5,8,11,10,0],
  [10,6,8,3,4,1,0,11,2,5,9,7],
  [6,3,9,4,1,10,5,0,11,8,2,7],
  [8,1,9,6,2,7,0,4,11,5,3,10],
  [7,10,5,1,4,3,0,8,2,9,11,6],
  [5,2,4,9,3,7,11,0,8,10,1,6],
  [10,8,5,1,7,11,3,0,6,4,9,2],
  [11,8,0,1,10,2,9,6,5,7,4,3]
]
```

SHA-256 of the compact JSON permutation list:

```text
a599a5e21f91ec76a55fee4df5551a5d3ea459d2f6aed8572e18c1c6358ca3c3
```

The prior is exactly uniform:

```text
P(h) = 1/32.
```

## 2. Exact Q8

For every directed off-diagonal pair `(i,j)`, compute the population variance of `T^(h)[i,j]` over the 32 frozen candidates. Sort by decreasing variance, breaking exact ties lexicographically by `(i,j)`. Select the first eight.

The resulting frozen order is:

```text
Q8 = [(6,3),(9,2),(10,5),(9,3),(2,10),(4,9),(1,9),(7,10)]
```

SHA-256 of compact JSON `Q8`:

```text
71e0fbff2485edbd5e6cbe1244398a4f24377f84da3e3f96e942e7f793f963b5
```

The eight pairs are fixed before all realized worlds and noise.

## 3. Tie-breaking

All domain-action argmax operations (`P_topo`, `P_raw`, `P_depth`, `P_oracle`) choose the **smallest zero-based domain index** among exact floating-point ties.

For descriptive MAP-topology diagnostics, posterior ties choose the smallest candidate index.

No stochastic tie-breaking is allowed.

## 4. Deterministic experiment family and noise schedule

Evaluate every candidate topology as a realized world:

```text
h = 0,...,31
```

For every world, evaluate exactly 256 measurement-noise specimens:

```text
s = 0,...,255
```

Total paired specimens:

```text
32 * 256 = 8192.
```

Noise is generated without mutable PRNG state.

For each `(h,s)` and each block `b = 0,1,2,3`, compute:

```text
digest = SHA256(ASCII("BL001|h={h}|s={s}|b={b}"))
x = unsigned big-endian integer from digest bytes 0..7
y = unsigned big-endian integer from digest bytes 8..15
u1 = (x + 0.5) / 2^64
u2 = (y + 0.5) / 2^64
z0 = sqrt(-2 ln u1) * cos(2 pi u2)
z1 = sqrt(-2 ln u1) * sin(2 pi u2)
```

Assign `z0,z1` to consecutive positions in the frozen `Q8` order and set:

```text
epsilon_k = sigma * z_k.
```

Thus the specification uniquely determines every noise value.

## Pre-execution structural audit

Before inspecting any noisy outcome:

1. verify all 32 topology matrices are distinct;
2. recompute `Q8` from the frozen family and verify exact equality with the stored list;
3. verify the noiseless `Q8` signature is unique for all 32 candidate topologies;
4. verify all constants, hashes, world indices, seed indices, and tie rules.

If noiseless signatures are not unique, classify:

```text
MEASUREMENT_INTERFACE_FAILURE
```

and do not interpret topology inference or allocation.

## Analysis schedule

The primary replication unit for inference is the realized topology/world, not the 8192 individual noise specimens.

For each world:

```text
delta_h = mean_s(R_topo[h,s] - R_raw[h,s]).
```

Primary estimand:

```text
Delta = mean_h delta_h.
```

Primary directional test:

```text
H0: E_world[delta_h] >= 0
H1: E_world[delta_h] < 0
```

Use a one-sample t statistic on the 32 `delta_h` values. Report:

- grand `Delta`;
- one-sided 95% upper confidence bound using `t_(0.95,31)`;
- two-sided 95% t confidence interval;
- one-sided p-value;
- mean and median `R_topo` and `R_raw` over all 8192 paired specimens;
- specimen-level topology/raw win, tie, loss fractions, where tie means `abs(R_topo-R_raw) <= 1e-15`;
- oracle-gap fraction closed: `(mean(R_raw)-mean(R_topo))/mean(R_raw)` if `mean(R_raw)>0`.

### Frozen map diagnostic

For every specimen compute full off-diagonal matrix MSE against the realized `T*`:

```text
MSE_topo = mean_(i!=j) (T_hat_topo[i,j]-T*[i,j])^2
MSE_raw  = mean_(i!=j) (T_hat_raw[i,j]-T*[i,j])^2.
```

For each world average over its 256 noise specimens and define:

```text
m_h = mean_s(MSE_topo-MSE_raw).
```

Use the same 32-world one-sided t procedure for:

```text
H0_map: E_world[m_h] >= 0
H1_map: E_world[m_h] < 0.
```

### Outcome classification

After the structural audit passes:

1. If the one-sided 95% upper bound for `Delta` is below zero:
   ```text
   TOPOLOGY_ADDS_ALLOCATION_VALUE
   ```
2. Otherwise, if the one-sided 95% upper bound for the map-MSE difference is not below zero:
   ```text
   TOPOLOGY_INFERENCE_FAILS
   ```
3. Otherwise:
   ```text
   ALLOCATION_FAILURE
   ```
   meaning topology completion demonstrably improves the map under the frozen MSE diagnostic but does not demonstrate improved depth allocation.

`COMPLETION_ADDS_NO_DEMONSTRATED_VALUE` is the umbrella interpretation for cases 2 and 3.

Map accuracy remains secondary to allocation value.

## Claim ceiling

A positive BL-001 result can earn only:

> Within this frozen finite family of directed transfer structures, sparse relational measurements supported topology-aware completion that improved allocation of a scarce local-learning operation relative to an equally informed non-topological baseline.

It does not establish adaptive surveying, topology invention, real neural competence topology, human knowledge geometry, or general broad learning.

No BL-002 design follows from this artifact.
