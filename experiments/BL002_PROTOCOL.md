# BL-002 Specification-001 — Active Surveying Within a Supplied Topology Family

Status entering this artifact:

```text
BL-001 = POSITIVE — TOPOLOGY UTILIZATION
BL-002 = QUESTION EARNED — NOT DESIGNED
BL-003 = UNOPENED
```

This artifact designs **BL-002 only**. It does not execute BL-002 and does not design BL-003.

The scientific question is:

> **Given the same limited measurement budget, can conditioning future measurement choices on evidence already observed produce a more consequentially useful inferred topology than committing to the measurements in advance?**

The single new edge is:

```text
E_t -> q_(t+1)
```

where `q_(t+1)` is the next relational measurement selected.

The downstream chain is inherited from BL-001:

```text
measurement policy
-> evidence
-> posterior over supplied topology family
-> posterior-mean topology
-> deep-probe allocation
-> regret
```

The primary success criterion remains consequential allocation value, not uncertainty reduction.

---

## 1. Inherited BL-001 scientific structure

BL-002 is based directly on the BL-001 scientific freeze:

```text
496b7829606db74635819afdf5dad5f2c0445d0f
```

and inherits unchanged:

```text
N = 12
D0 = (0.15,0.15,0.20,0.20,0.40,0.40,0.55,0.55,0.70,0.70,0.85,0.85)
eta = 0.25
sigma = 0.08
```

Base directed transfer topology:

```text
T_base[i,(i+1) mod 12] = 0.60
T_base[i,(i+3) mod 12] = 0.35
T_base[i,(i+5) mod 12] = 0.15
all other off-diagonal entries = 0
```

The exact 32 permutations and uniform prior are the BL-001 family `H` with permutation hash:

```text
a599a5e21f91ec76a55fee4df5551a5d3ea459d2f6aed8572e18c1c6358ca3c3
```

The true topology is always one of the supplied candidates:

```text
T* in H.
```

This boundary is load-bearing. BL-002 is active surveying **within a supplied topology family**, not topology construction or invention.

Deep-probe update remains:

```text
D'_i = D_i + eta * (1-D_i)
D'_j = D_j + eta * T[i,j] * (1-D_j), j != i
G(D) = mean_j D_j
```

The deep action is chosen from the posterior-mean topology exactly as in BL-001. The oracle remains evaluator-only and supplies an upper bound.

Regret remains:

```text
R_P = G(D'_(oracle)) - G(D'_(P)).
```

---

## 2. Candidate measurements and budget

Candidate measurement space:

```text
Q = {(i,j): i,j in {0,...,11}, i != j}
|Q| = 132.
```

Compact-JSON hash of the lexicographically enumerated candidate list:

```text
1530d983ef04da9c4d21e8c587aa5e1bc3710154c9becc950f9ade3979c05067
```

Every measurement is directed.

Each edge may be measured at most once per policy/specimen.

Measurement budget:

```text
B_meas = 8.
```

Every adaptive and fixed policy therefore observes exactly eight scalar measurements.

---

## 3. Common measurement field

Matched policies must not receive different stochastic specimens.

For every realized world `h`, specimen index `s`, and candidate edge `q=(i,j)`, define a full latent noisy measurement field before any policy path is revealed:

```text
Y_(h,s)(i,j) = T^(h)[i,j] + sigma * Z_(h,s,i,j).
```

`Z_(h,s,i,j)` is generated deterministically:

```text
digest = SHA256(ASCII("BL002|h={h}|s={s}|i={i}|j={j}"))
x = unsigned big-endian integer from digest bytes 0..7
y = unsigned big-endian integer from digest bytes 8..15
u1 = (x + 0.5) / 2^64
u2 = (y + 0.5) / 2^64
Z = sqrt(-2 ln u1) * cos(2 pi u2)
```

Thus all policies face the same edge-indexed noisy world. If two policies measure the same edge, they observe exactly the same value. If they measure different edges, they reveal different coordinates of the same pre-defined measurement field.

No mutable PRNG state is used.

Policies cannot inspect unselected coordinates.

---

## 4. Posterior and downstream inference

Given observed history:

```text
E_t = {((i_k,j_k), y_k)}_(k=1..t),
```

the posterior over the same 32 supplied candidates is:

```text
log w_h(E_t)
  = constant
    - (1 / (2 sigma^2)) * sum_k (y_k - T^(h)[i_k,j_k])^2.
```

Normalize over `h=0,...,31`.

The prior is uniform.

After eight measurements:

```text
T_hat(E_8) = sum_h w_h(E_8) T^(h).
```

The deep action is:

```text
i_depth = argmax_i G(D' | T_hat(E_8), i).
```

All downstream topology inference and allocation are therefore shared between adaptive and fixed policies. Only the measurement-selection path differs.

---

## 5. Candidate adaptive policy family

BL-002 does **not** nominate one acquisition principle as the theory of active surveying.

It freezes a three-member candidate family:

```text
A = {VAR, EDGE_ENTROPY, ACTION_MI}
```

Compact-JSON hash of this ordered policy-name list:

```text
6f7d396f903b6aa25b56298c6bc83cc278d33275bbc9e35e3b779a5d81e94665
```

At each step, an adaptive policy scores only currently unmeasured edges under its **current posterior**.

### 5.1 VAR — posterior edge variance

For candidate edge `q`:

```text
score_VAR(q | E_t)
  = Var_(h ~ w(E_t)) [ T^(h)[q] ].
```

This is a magnitude-sensitive disagreement score.

### 5.2 EDGE_ENTROPY — latent edge-value entropy

All candidate edge values lie in:

```text
V = {0.00, 0.15, 0.35, 0.60}.
```

Define:

```text
p_q(v | E_t)
  = sum_(h: T^(h)[q] = v) w_h(E_t).
```

Then:

```text
score_EDGE_ENTROPY(q | E_t)
  = - sum_v p_q(v | E_t) ln p_q(v | E_t),
```

with `0 ln 0 = 0`.

This is a categorical topology-discrimination score.

### 5.3 ACTION_MI — decision-relevant edge/action mutual information

For each supplied candidate topology `h`, precompute the evaluator-defined oracle-optimal deep action under frozen `D0` and `eta`:

```text
a*(h) = argmax_i G(D' | T^(h), i).
```

This is a property of the supplied candidate family and frozen downstream utility; it does not reveal the realized world.

For candidate edge `q`, let `V_q = T^(h)[q]` under the current posterior. Then:

```text
score_ACTION_MI(q | E_t)
  = I_w(V_q ; a*).
```

Equivalently:

```text
H_w(a*) - sum_v p_q(v | E_t) H_w(a* | V_q=v).
```

This score is decision-relevant rather than full-map-reconstruction oriented.

### Adaptive selection rule

For policy `m` in the candidate family:

```text
q_(t+1)
  = argmax_(q not yet measured) score_m(q | E_t).
```

Observe `Y(q_(t+1))`, append it to `E_t`, recompute the posterior, and repeat until eight measurements have been taken.

No candidate edge may be remeasured.

---

## 6. Matched non-adaptive controls

Each adaptive rule receives a matched fixed counterpart using the **same acquisition score**, but evaluated only under the initial uniform prior.

The fixed counterpart ranks all 132 edges once before any realized measurement value is observed and commits to the top eight.

This keeps score semantics matched while removing the new BL-002 edge:

```text
E_t -> q_(t+1).
```

The frozen fixed sequences are:

### VAR fixed

```text
[(6,3),(9,2),(10,5),(9,3),(2,10),(4,9),(1,9),(7,10)]
```

Hash:

```text
71e0fbff2485edbd5e6cbe1244398a4f24377f84da3e3f96e942e7f793f963b5
```

This is exactly the BL-001 `Q8`.

### EDGE_ENTROPY fixed

```text
[(10,5),(6,4),(5,8),(1,9),(3,7),(8,0),(9,2),(7,11)]
```

Hash:

```text
798862423b1ad25798ac3779a7494c0e6e077f5ab723cbe4aa7c04375fd443ff
```

### ACTION_MI fixed

```text
[(0,10),(11,6),(5,1),(11,0),(7,4),(5,9),(1,9),(2,5)]
```

Hash:

```text
7a8e6816ac88bdf4c0df8ce7610515342dde1750143befaa7a81afeec004f9b0
```

All fixed sequences are recomputed during the static audit and must match exactly before scientific execution is permitted.

---

## 7. Tie-breaking

Measurement-selection scores use:

```text
TIE_EPS = 1e-15.
```

If multiple unmeasured edges lie within `1e-15` of the maximum score, choose the lexicographically smallest `(i,j)`.

If all remaining scores are zero, choose the lexicographically smallest remaining edge.

Deep-action argmax remains the BL-001 rule: smallest zero-based action index among exact floating-point ties.

Posterior MAP diagnostics choose the smallest topology index on exact ties.

No stochastic tie-breaking is permitted.

---

## 8. Experiment family and pairing

Reuse the BL-001 evaluation family shape:

```text
h = 0,...,31
s = 0,...,255
32 * 256 = 8192 paired specimens.
```

The realized world/topology is the replication unit for inference.

For every `(h,s)`, run all three adaptive selectors and all three matched fixed selectors against the same edge-indexed measurement field.

No policy may use `h`, `T*`, oracle regret, or unobserved measurement coordinates in its measurement-selection rule.

---

## 9. Primary estimand

BL-002 deliberately does **not** select the best acquisition rule after seeing outcomes.

For each specimen define family-average regrets:

```text
R_adaptive(h,s)
  = (1/3) * sum_m R_adaptive,m(h,s)

R_fixed(h,s)
  = (1/3) * sum_m R_fixed,m(h,s).
```

Then:

```text
d_(h,s) = R_adaptive(h,s) - R_fixed(h,s)
delta_h = mean_s d_(h,s)
Delta_BL2 = mean_h delta_h.
```

Primary directional hypothesis:

```text
H0: E_world[delta_h] >= 0
H1: E_world[delta_h] < 0.
```

Use a one-sample t statistic on the 32 world-level `delta_h` values.

Report:

- `Delta_BL2`;
- one-sided 95% upper confidence bound using `t_(0.95,31)`;
- two-sided 95% t confidence interval;
- one-sided p-value;
- family-average adaptive and fixed regret;
- per-rule adaptive-minus-fixed deltas as descriptive diagnostics only.

Primary positive classification requires:

```text
one-sided 95% upper bound for Delta_BL2 < 0.
```

The per-rule results do not select or redefine the primary result.

---

## 10. Secondary topology diagnostics

Map accuracy remains secondary to allocation value.

For each adaptive/fixed rule pair, after eight measurements compute posterior-mean topology MSE against the evaluator-known realized topology:

```text
MSE = mean_(i != j) (T_hat[i,j] - T*[i,j])^2.
```

Average the three adaptive MSEs and the three matched fixed MSEs per specimen.

Define the world-level family-average map-MSE difference exactly analogously to the primary allocation difference and apply the same 32-world directional t summary.

Also report final posterior entropy:

```text
H(w_8) = - sum_h w_h ln w_h.
```

and the family-average difference:

```text
H_adaptive - H_fixed.
```

Entropy reduction is secondary and cannot establish BL-002 success by itself.

Report sequence-divergence diagnostics for each adaptive rule:

- fraction of specimens whose adaptive 8-edge sequence differs from its matched fixed sequence;
- first divergence step.

The first measurement will generally be prior-determined; BL-002 concerns whether later measurements become evidence-conditioned.

---

## 11. Frozen outcome decomposition

After a pre-run structural audit passes:

1. If the one-sided 95% upper bound for `Delta_BL2` is below zero:

   ```text
   ACTIVE_SURVEYING_ADDS_ALLOCATION_VALUE
   ```

2. Otherwise, if no adaptive sequence differs from its matched fixed sequence in any specimen:

   ```text
   ADAPTIVITY_NOT_EXPRESSED
   ```

3. Otherwise, if the one-sided 95% upper bound for family-average adaptive-minus-fixed map MSE is not below zero:

   ```text
   ADAPTIVE_MEASUREMENT_NO_DEMONSTRATED_TOPOLOGY_GAIN
   ```

4. Otherwise:

   ```text
   TOPOLOGY_GAIN_WITHOUT_ALLOCATION_GAIN
   ```

The decomposition preserves:

```text
measurement-selection expression
!= topology improvement
!= consequential allocation improvement.
```

---

## 12. Static pre-run audit

Before any BL-002 noisy outcome is evaluated, verify:

1. the inherited 32 topology candidates reproduce exactly;
2. permutation hash matches BL-001;
3. all 132 directed off-diagonal candidate measurements exist exactly once;
4. candidate-edge hash matches;
5. ordered acquisition-family hash matches;
6. all three fixed 8-edge sequences recompute exactly from their initial-prior scores;
7. all fixed-sequence hashes match;
8. every fixed sequence contains eight unique valid candidate edges;
9. the executable defaults to audit-only and requires an explicit `--execute` flag for scientific execution.

If any static audit item fails:

```text
SPECIFICATION_AUDIT_FAILURE
```

and no BL-002 scientific result may be interpreted.

---

## 13. Claim ceiling

A positive BL-002 result can earn only:

> Within the frozen BL-001 32-member supplied topology family and an equal eight-measurement budget, a preregistered family of evidence-conditioned measurement selectors reduced eventual deep-allocation regret on average relative to matched non-adaptive selectors using the same acquisition scores under the initial prior.

It would establish an **active-surveying witness within a supplied topology family**.

It would not establish:

- topology invention;
- out-of-family topology discovery;
- a universal acquisition rule;
- superiority of active learning in general;
- real neural competence topology;
- human knowledge geometry;
- general broad learning.

BL-003 remains unopened.

---

## 14. Current status

This branch is a design/calibration artifact only:

```text
BL-002 = DESIGNED — NOT EXECUTED
BL-003 = UNOPENED
```

The intended protocol is:

```text
design
-> freeze
-> static pre-run audit
-> execute once
-> audit
-> narrow result.
```

No BL-002 outcome may be inspected before the scientific freeze SHA is declared.
