# BL×CC-001 Freeze-Completion Specification — Wrong-Map Escape Under Endogenous Acquisition

Status entering this artifact:

```text
BL-001 = POSITIVE — TOPOLOGY UTILIZATION
BL-002 = POSITIVE — ACTIVE SURVEYING
BL-003 = QUESTION EARNED — UNOPENED
CC = META-HYPOTHESIS
BL×CC-001 = QUESTION / CAUSAL STRUCTURE FROZEN; APPARATUS DESIGNED; NOT EXECUTED
```

This artifact prospectively freezes **BL×CC-001 only**. It does not execute the assay and does not open BL-003.

Scientific question:

> When an adaptive epistemic allocator begins from a wrong but representationally repairable map, and that map governs the ordinary intervention used to acquire future evidence, does allowing a matched ordinary task consequence to acquire developmental influence increase first sustained correct allocation relative to cutting only that consequence `W_corr -> U_corr` channel?

Load-bearing representational boundary:

```text
T* in H.
```

BL×CC-001 is therefore not topology invention.

Frozen causal cut:

```text
A/C: W_corr -> U_corr open
B/D: W_corr -> U_corr cut
```

Frozen primary endpoint:

```text
first sustained correct allocation
m = 2 consecutive rounds
```

Frozen competence guardrail:

```text
D_t^allocation = D0 for all diagnostic rounds.
```

The prospective calibration prediction is approximately:

```text
Delta_esc^(A-B) ~= +0.08821044
```

This is **calibration prediction only**, not an empirical BL×CC result and not part of the positive decision rule.

---

## 1. Supplied symmetric world family

Number of regions:

```text
N = 4.
```

Shared local transfer strength:

```text
alpha = 0.20.
```

Weak/strong cross-route strengths:

```text
beta_L = 0.30
beta_H = 0.70.
```

The supplied family is exactly:

```text
H = {T^L, T^R}.
```

Matrices use zero-based indices and rows as source regions:

```text
T^L =
[[0.00,0.20,0.00,0.00],
 [0.20,0.00,0.70,0.00],
 [0.00,0.00,0.00,0.20],
 [0.30,0.00,0.20,0.00]]

T^R =
[[0.00,0.20,0.00,0.00],
 [0.20,0.00,0.30,0.00],
 [0.00,0.00,0.00,0.20],
 [0.70,0.00,0.20,0.00]].
```

The two worlds are mirror images under:

```text
0 <-> 2
1 <-> 3
T^L <-> T^R.
```

Both realized worlds are evaluated prospectively:

```text
world in {L,R}.
```

The learner's true topology is always exactly one supplied candidate.

---

## 2. Fixed BL-style allocation machinery

Frozen competence state:

```text
D0 = (0.50,0.50,0.50,0.50)
eta = 0.25.
```

For candidate depth action `i` and topology `T`:

```text
D'_i = D0_i + eta * (1-D0_i)
D'_j = D0_j + eta * T[i,j] * (1-D0_j), j != i
G(D') = mean_j D'_j.
```

`D0` is restored for every diagnostic decision. Executing an action does **not** modify the allocation-evaluation competence state for later rounds.

Under `T^L`, action `1` is the unique oracle-optimal allocation.

Under `T^R`, action `3` is the unique oracle-optimal allocation.

The evaluator may use these oracle labels only for endpoint scoring. They are unavailable to learner policy/scoring.

---

## 3. Intentionally wrong but repairable prior

Each mirror world gives the realized truth exactly 0.30 initial posterior support:

```text
P0(T*) = 0.30
P0(other topology) = 0.70.
```

The operative learner state is log odds in favor of `T^R`:

```text
L_t = log(P(T^R)/P(T^L)).
```

Thus:

```text
world R: L_0 = log(.30/.70) < 0, initial MAP = T^L
world L: L_0 = log(.70/.30) > 0, initial MAP = T^R.
```

The realized truth retains nonzero support, so repair requires no out-of-family invention.

---

## 4. Ordinary throughput interventions

Two symmetric ordinary task interventions are available:

```text
q_L: perturb/inject standardized workload at region 1 and observe downstream completions at region 2
q_R: perturb/inject standardized workload at region 3 and observe downstream completions at region 0.
```

Throughput scale:

```text
c = 4.
```

Poisson rates:

```text
lambda_L = c * beta_L = 1.20
lambda_H = c * beta_H = 2.80.
```

Observation laws:

```text
             T^L                  T^R
q_L    Pois(lambda_H)       Pois(lambda_L)
q_R    Pois(lambda_L)       Pois(lambda_H).
```

`Y_q` is an ordinary operational throughput count. The learner's intervention objective is expected throughput, not information gain.

Learner-visible survey log-likelihood ratio is fixed prospectively:

```text
Lambda_q(y) = log p(y | q,T^R) - log p(y | q,T^L).
```

No realized-world argument is permitted in this scoring function.

Corrective information is action×world dependent:

```text
I_wrong = KL(Pois(1.2) || Pois(2.8)) > 0
I_right = KL(Pois(2.8) || Pois(1.2)) > I_wrong.
```

The ordering reverses under `L <-> R`. No probe has intrinsically privileged sensor quality.

---

## 5. Endogenous and map-blind acquisition policies

Frozen exploration parameter:

```text
epsilon = 0.10.
```

At each round, expected operational value is:

```text
V_op(q | L_t) = E[Y_q | L_t].
```

### Endogenous policy (A/B)

If one probe has strictly larger expected throughput:

```text
preferred probe probability = 1 - epsilon/2 = 0.95
other probe probability     = epsilon/2     = 0.05.
```

This is exactly equivalent to:

```text
(1-epsilon) * delta_preferred + epsilon * Uniform({q_L,q_R}).
```

If expected throughputs tie within `TIE_EPS`, choose `q_L/q_R` 50/50 from the frozen hash random field.

### Open-loop map-blind policy (C/D)

```text
P(q_L)=P(q_R)=0.50
q_t independent of L_t.
```

This control removes map dependence from acquisition while preserving both interventions and their ordinary task meaning.

The control is mechanistic/secondary. It cannot redefine the primary A/B classification.

---

## 6. Round chronology

Exactly three rounds are evaluated:

```text
t = 0,1,2.
```

For every cell/world/specimen:

```text
L_t
-> choose q_t
-> observe throughput Y_t
-> add Lambda_q(Y_t)
-> choose depth action d_t from posterior-mean BL gain
-> [round 0 only: possibly instantiate designated ordinary consequence event]
-> obtain L_(t+1).
```

Survey likelihood updates always influence the operative map in all four cells.

There is exactly one designated consequence opportunity, at round `0`, and only if the post-survey MAP still equals the learner's initial MAP. This trigger is defined from learner state, not from `T*` or evaluator correctness.

If the round-0 survey has already moved the learner away from its initial MAP, the designated consequence event is inactive and:

```text
W_corr = U_corr = 0
```

for both members of the paired comparison.

---

## 7. Ordinary task consequence and frozen W->U cut

The ordinary consequence is a noisy realized one-step allocation performance:

```text
C_0 | (T,d_0) ~ Normal(mu_C(T,d_0), sigma_C^2)
mu_C(T,d) = G(D' | T,d).
```

The two consequential actions have equal mirror separation:

```text
Delta_C = |mu_C(T^R,d)-mu_C(T^L,d)| = 0.0125, d in {1,3}.
```

Frozen consequence signal-to-noise ratio:

```text
kappa_C = Delta_C / sigma_C = 0.79242459.
```

Therefore:

```text
sigma_C = Delta_C / kappa_C
        = 0.015774371666078663...
```

The learner-visible consequence likelihood ratio is:

```text
Lambda_C(c,d)
  = log p(c | d,T^R) - log p(c | d,T^L).
```

Again, no realized-world argument enters the learner scorer.

Typed corrective event fields:

```text
D/H  = standardized discrepancy from current posterior-predictive consequence mean
I    = identified supplied contrast "T_L_vs_T_R"
W_corr = Lambda_C(c,d)
```

At the matched event A/B and C/D compute the same `D/H`, `I`, and `W_corr`.

The sole intended intervention is:

```text
A: U_corr = W_corr
B: U_corr = 0
C: U_corr = W_corr
D: U_corr = 0.
```

The cut applies to the entire designated consequence likelihood signal, regardless of sign. The apparatus never asks whether a realized consequence happened to favor the true topology before applying the gate.

---

## 8. Four-cell causal matrix

```text
                 consequence influence open     consequence influence cut
endogenous                A                              B
open-loop                 C                              D
```

Primary causal comparison:

```text
A vs B.
```

Secondary/descriptive control quantities:

```text
C-D                 generic consequence-influence effect under map-blind acquisition
B-D                 endogenous-vs-open-loop survey/acquisition difference with consequence cut
(A-B)-(C-D)         descriptive interaction.
```

These secondary quantities cannot redefine primary success and do not by themselves establish a general acquisition-feedback theorem.

---

## 9. Sustained-escape endpoint

For each realized world, the evaluator-only oracle action is:

```text
T^L -> action 1
T^R -> action 3.
```

With `m=2` and rounds `0,1,2`, define:

```text
tau_esc = 0 if d_0 and d_1 are both oracle-correct
tau_esc = 1 if d_1 and d_2 are both oracle-correct and the first condition failed
otherwise tau_esc = infinity.
```

Binary primary endpoint:

```text
Y_esc = 1[tau_esc finite].
```

For paired specimen `s`:

```text
d_s = Y_esc^A - Y_esc^B.
```

Primary estimand pooled over the two mirror worlds and the frozen seed schedule:

```text
Delta_esc = mean_s d_s
          = P(A sustained escape) - P(B sustained escape).
```

A one-round posterior crossing or map movement without sustained correct allocation does not count as primary success.

---

## 10. Common-randomness construction

No mutable PRNG state is permitted.

All stochastic fields are deterministic SHA256 functions of immutable coordinates.

Science domain keys use the prefix:

```text
BLXCC001|science|...
```

Static audit sentinels use the disjoint prefix:

```text
BLXCC001|audit|...
```

so the pre-run audit never reveals a scientific-seed outcome.

### Probe-selection field

For world `w`, seed `s`, round `t`:

```text
U_select(w,s,t)
```

is derived from the first 64 bits of the SHA256 digest and mapped to `(0,1)` via `(x+0.5)/2^64`.

The same `U_select` is supplied to all four cells; each cell maps it through its frozen policy.

### Survey potential outcomes

For every `(w,s,t,q)` define before the policy path is known:

```text
U_survey(w,s,t,q).
```

The selected probe's Poisson count is the inverse-CDF transform at the world/probe rate. If two cells select the same probe at the same world/seed/round, they observe exactly the same throughput count.

Unselected potential outcomes remain inaccessible to policy.

### Consequence potential outcome

For every `(w,s)` define one SHA256/Box-Muller standard normal:

```text
Z_C(w,s).
```

When the designated consequence event is active:

```text
C_0 = mu_C(T*,d_0) + sigma_C * Z_C(w,s).
```

A/B share the identical realized consequence because their paths are identical through `W_corr`. C/D are paired analogously.

---

## 11. Seed schedule and replication

Both mirror worlds are included:

```text
world = L,R.
```

Science seed schedule:

```text
s = 0,...,4095
4096 seeds per world
8192 paired A/B specimens total.
```

All four cells are evaluated on every world/seed specimen.

The audit-only sentinel schedule is:

```text
s in {0,1,17,255}
```

under the separate `audit` hash domain. Audit sentinel values are not scientific observations.

---

## 12. Tie handling

Frozen tolerance:

```text
TIE_EPS = 1e-15.
```

If endogenous expected throughput ties within tolerance, choose `q_L/q_R` 50/50 from the frozen selection field.

If posterior-mean depth actions `1` and `3` tie within tolerance, choose between them 50/50 from a separate frozen action-tie hash field.

Any other unexpected multi-action tie falls back to the smallest zero-based action index and is reported by audit if it affects the supplied oracle uniqueness checks.

The stochastic `1/2` tie rule is required for exact `L <-> R` symmetry; deterministic left-favoring tie-breaking is prohibited.

---

## 13. Primary statistical test

The primary outcome is paired binary.

Let:

```text
b = number of paired specimens with A=1,B=0
c = number of paired specimens with A=0,B=1.
```

Primary directional hypotheses:

```text
H0: P(A-only success | discordant) <= 0.5
H1: P(A-only success | discordant) > 0.5.
```

Use the exact one-sided McNemar/binomial test:

```text
p = P[Binomial(b+c,0.5) >= b].
```

Frozen significance level:

```text
alpha_primary = 0.05.
```

Positive classification requires both:

```text
Delta_esc > 0
one-sided exact McNemar p < 0.05.
```

Classification labels:

```text
CORRECTIVE_INFLUENCE_ADDS_SUSTAINED_ESCAPE
NO_DEMONSTRATED_CORRECTIVE_INFLUENCE_GAIN
```

No secondary control can override or redefine the primary classification.

---

## 14. Required reporting fields

A scientific execution payload must report at minimum:

```text
status/classification
execution provenance
frozen config hash
worlds and seed count
success rates A,B,C,D
Delta_esc = A-B
A=1,B=0 discordant count
A=0,B=1 discordant count
one-sided exact McNemar p
C-D descriptive control effect
B-D descriptive acquisition-control effect
(A-B)-(C-D) descriptive interaction
per-world success rates
claim ceiling.
```

Prospective calibration predictions must remain labeled as predictions and must never be rewritten as empirical results.

---

## 15. Truth-leakage prohibition

Learner policy/scoring must never receive:

```text
T*
q_right
q_wrong
oracle action / A*
future potential outcomes
unselected survey outcomes
primary success indicator
regret / evaluator labels.
```

Learner-facing survey scorer is exactly:

```text
Lambda_q(y) = log p(y|q,T^R) - log p(y|q,T^L).
```

Learner-facing consequence scorer is exactly:

```text
Lambda_C(c,d) = log p(c|d,T^R) - log p(c|d,T^L).
```

`T*` is available only to environment generation and evaluator-only endpoint scoring.

---

## 16. Frozen configuration hash

Canonical compact JSON of the executable configuration has SHA256:

```text
3b06b39fb942aaecdccad138ceb763a5495092231e5a26bf07c2d0fc921559ba
```

The reference executable audits this hash before scientific execution is interpreted.

---

## 17. Static pre-run audit requirements

Default executable invocation must be audit-only:

```text
python experiments/blxcc001.py
```

Scientific execution requires explicit:

```text
python experiments/blxcc001.py --execute
```

Before execution, static audit must verify at least:

1. frozen config hash matches;
2. exactly two supplied topologies exist and `T* in H` for both realized worlds;
3. fixed allocation competence and unique mirror oracle actions;
4. mirrored wrong initial posterior;
5. `0 < lambda_L < lambda_H`;
6. wrong probe has positive topology information;
7. aligned probe has greater expected topology information;
8. q-conditioned evidence kernels differ;
9. endogenous policy prefers the mirror-wrong probe initially;
10. alternative probe retains a nonzero 0.05 acquisition floor;
11. open-loop probe selection is map-blind;
12. `m=2,T=3` temporal endpoint is coherent;
13. consequence gap and sigma are positive and mirrored;
14. audit-domain A/B sentinels are identical through `W_corr` and differ only at `U_corr` when the event is active;
15. learner-facing survey/consequence scorer signatures contain no realized-world argument;
16. default invocation reports `science_execution_performed=false`.

Any failed audit item yields:

```text
SPECIFICATION_AUDIT_FAILURE
```

and no scientific output may be interpreted.

---

## 18. Claim ceiling

A positive primary result can earn only:

> Within this frozen symmetric supplied two-topology synthetic world, fixed allocation-competence state, map-conditioned ordinary throughput-intervention policy, and three-round horizon, allowing the matched ordinary task-consequence likelihood signal to acquire developmental influence increased the probability of first sustained two-round correct allocation relative to cutting only that consequence `W_corr -> U_corr` channel.

It does **not** establish:

```text
topology invention
out-of-family representation expansion
general corrigible compression
universal value of random exploration
human or neural competence topology
general active learning
architecture-level blindness repair
retention-stage corrigibility
a universal W->U mechanism.
```

A positive A/B primary result alone also does not establish that endogenous acquisition feedback is the unique cause of the effect. C/D, B/D, and the interaction are mechanistic controls/diagnostics and remain secondary.

---

## 19. Prospective freeze status

This specification uniquely determines one experiment together with `experiments/blxcc001.py`.

Until an explicit `--execute` invocation occurs and completes:

```text
BL×CC-001 = PROSPECTIVELY FROZEN — NOT EXECUTED
```

The calibration prediction remains:

```text
Delta_esc^(A-B) ~= +0.08821044
```

and must continue to be labeled prediction-only.
