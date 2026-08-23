# XM-CRCB-001 — Held-Out Regional Repair Factorization

Status:

```text
XM-CRCB-001 = QUESTION EARNED / PROTOCOL DESIGN OPEN / NOT FROZEN
EXECUTABLE  = NONE
SCIENCE RUN = NOT AUTHORIZED
ENDPOINT    = NOT FROZEN
SEEDS       = NOT FROZEN
```

This document opens a fresh experimental-design lineage after the terminal authority-grounding reduction. It does **not** modify `docs/AUTHORITY_GROUNDING.md`, reopen BL-003, revive the real-XM authority-starvation hypothesis, or claim evidence for `H_CRCB`.

The experimental chassis is the previously audited continuous-XM / ImageNet setup. The scientific object is new: **repair factorization and held-out repair transfer**.

---

## 1. Scientific question

Primary question:

> **Can a fixed low-description repair basis constructed from dedicated repairs on one prospectively frozen subset of latent contexts generate functionally useful repairs on held-out contexts, within a fixed repair language, evidence interface, resource budget, and evaluator?**

The intended reduction target is the open compact reusable correction basis hypothesis:

```text
H_CRCB:
there exist structured failure classes for which reusable repair machinery
supports held-out recovery at lower frozen resource cost than direct
failure-specific retention, under an honest accounting boundary.
```

XM-CRCB-001 is not an optimizer-mechanism assay. A positive result would concern **structure of bounded repair representations**, not a new optimization primitive.

---

## 2. Three distinct possible positive claims

The protocol must permanently separate:

```text
A. FUNCTIONAL TRANSFER
   generated held-out repairs improve recovery on unseen contexts.

B. STRUCTURAL / ARTIFACT COMPRESSION
   the transferring repair representation has lower prospectively charged
   retained repair cost than a declared direct-retention artifact baseline.

C. INTRINSIC OPTIMUM SEPARATION
   the factorized architecture beats the unrestricted minimum repair cost.
```

XM-CRCB-001 may realistically establish **A** and, under an explicit cost ledger, **B**.

XM-CRCB-001 cannot establish **C** without a matching lower bound over the unrestricted repair architecture class.

Permanent firewall:

```text
functional transfer
!= artifact/resource compression
!= intrinsic optimum separation
```

---

## 3. Explicit non-goals

This assay does not test:

- authority starvation;
- regional winner-authority topology;
- high-K authority/competence coupling;
- whether `rho` predicts repairability;
- a new corrigibility optimizer;
- authority grounding;
- topology invention / BL-003;
- unrestricted minimum correction complexity;
- full-ImageNet generality;
- universal low-rank repair structure.

The old real-XM authority line remains fossilized external evidence. No `rho` endpoint is needed here.

---

## 4. Inherited organism and apparatus

The intended organism is the previously audited class-conditional continuous image DiT / flow-matching XM implementation, using the same real-ImageNet cache construction and deterministic latent-region interface already validated in the real-XM authority work.

Inherited useful facts:

```text
fixed 4-bit sign partition over latent noise
16 prior-symmetric regions
region assignment independent of model loss / winner / history
private deterministic region-conditioned noise generation
fixed held-out flow-matching competence measurement machinery
custody-audited ImageNet latent cache construction
fresh-seed training infrastructure
```

These are apparatus assets only. Their prior authority interpretation is not inherited.

Initial intended training regime:

```text
K_train = 2
K_repair = 1
```

`K_repair = 1` means no best-of-K repair search is permitted in the first assay. Once a context `r` and retained basis `B` are supplied, repair construction is deterministic.

This keeps:

```text
stored reusable structure
!= runtime repair search
```

---

## 5. Context space

Use the already defined four fixed latent-sign coordinates.

Represent each region as:

```text
r = (r_1,r_2,r_3,r_4) in {-1,+1}^4.
```

Thus:

```text
R = {-1,+1}^4
|R| = 16.
```

No region may be redefined from observed loss, repair magnitude, winner allocation, generation quality, or science outcomes.

---

## 6. Prospective development / held-out split

Candidate fixed split:

```text
R_dev  = { r : product_j r_j = +1 }
R_test = { r : product_j r_j = -1 }
```

so:

```text
|R_dev|  = 8
|R_test| = 8.
```

This split is a **single predetermined combinatorial split**, not a family of partitions to search.

The opposite parity assignment may only be used later as a separately frozen replication. It may not be opened post hoc as a rescue analysis.

The parity split is attractive because the development design matrix for intercept + four main effects has full rank and orthogonal columns.

---

## 7. Repair-language gate

A negative factorization result is uninterpretable if the chosen repair language cannot produce dedicated repairs in the first place.

Therefore the assay requires a prospective repair-language adequacy gate.

### 7.1 Initial candidate language

The cleanest first candidate is:

```text
L_A^(1) = DiT final_layer.linear weight + bias only.
```

Reason:

- it is a fixed explicit parameter subspace;
- it excludes `final_layer.adaLN_modulation`, which is a separate conditioning-sensitive mechanism;
- it makes repair vectors share a common coordinate origin and accounting rule;
- its retained parameter cost is simple to audit.

### 7.2 Calibration-only escalation ladder

Before science freeze, a calibration-only specimen may test a **prospectively declared** nested repair-language ladder if `L_A^(1)` cannot produce reliable direct repair.

Example design ladder:

```text
L_A^(1): output projection only
L_A^(2): full DiT FinalLayer
L_A^(3): final transformer block + FinalLayer
```

The exact ladder, calibration data, adequacy criterion, maximum escalation depth, and selection rule must be frozen before calibration.

Science cannot begin until exactly one repair language `L_A` is selected and frozen.

If no declared candidate passes the direct-repair adequacy gate:

```text
REPAIR_LANGUAGE_INSUFFICIENT
```

and no `H_CRCB` conclusion is earned.

---

## 8. Dedicated regional repair construction

For each independently trained base model `theta_0` and each development region `r in R_dev`, construct a dedicated repair from the **same base checkpoint**:

```text
theta_r^direct = theta_0 + Delta_r.
```

All dedicated repair trajectories must restart from `theta_0`; no sequential cross-region adaptation is allowed.

The repair construction procedure must be frozen and bounded:

```text
fixed repair parameter subspace L_A
fixed optimizer family
fixed number J of update steps
fixed learning rate / schedule
fixed examples per step
fixed region-conditioned repair-construction RNG stream
fixed timestep construction
fixed regularization / clipping, if any
```

A simple optimizer with minimal hidden state is preferred. If an optimizer with persistent state is used, that state and its cost must be accounted for whenever it is part of the retained repair artifact.

Each `Delta_r` is therefore an explicit bounded repair artifact produced under identical construction resources.

Held-out dedicated repairs `Delta_r` for `r in R_test` may be constructed **evaluator-side only** to establish repair-language adequacy and a direct-repair ceiling. They may not be inputs to the reusable basis or constructor.

---

## 9. Factorized repair basis

Let the context feature map be:

```text
x(r) = [1, r_1, r_2, r_3, r_4].
```

Let `X_dev` stack the eight development context rows and let `D_dev` stack the flattened development repair vectors `Delta_r`.

Use one fixed least-squares constructor:

```text
B = (X_dev^T X_dev)^(-1) X_dev^T D_dev.
```

For the parity design:

```text
X_dev^T X_dev = 8 I,
```

so this is equivalent to the orthogonal main-effect averages.

`B` contains five repair components:

```text
B = (b_0,b_1,b_2,b_3,b_4).
```

For any context `r`, including held-out regions:

```text
Delta_hat_r = G(B,r) = x(r)^T B
            = b_0 + sum_j r_j b_j.
```

`G` is frozen, deterministic, and receives no hidden failure identity beyond the admissible context code `r`, no evaluator success label, and no oracle repair label.

---

## 10. Mandatory controls

### 10.1 Base / no repair

```text
theta_0
```

establishes untreated regional competence.

### 10.2 Dedicated direct repair ceiling

```text
theta_0 + Delta_r^direct
```

for each held-out region, evaluator-side only.

This determines whether the frozen repair language can repair that region under the declared resource budget.

### 10.3 Mean repair

Use only:

```text
b_0.
```

This tests generic shared correction without context geometry.

### 10.4 Nearest memorized development repair

Store the eight dedicated development repairs and apply a prospectively defined nearest-context retrieval rule to held-out contexts.

This is an explicit direct-retention / retrieval comparator using only development repairs.

### 10.5 Random-code factorization — mandatory geometry control

Freeze a random bijective relabeling / code map:

```text
c : R -> {-1,+1}^4
```

before any repair or science outcome is observed.

The random-code development design must have full rank for intercept + four code bits. Rank checking is permitted because it depends only on the frozen code design, not outcomes.

Fit the **same five-component least-squares constructor** using:

```text
x_rand(r) = [1,c_1(r),...,c_4(r)]
```

and evaluate on the same held-out regions.

Thus the structured and random-code arms have matched:

```text
basis dimensionality
constructor form
repair parameter subspace
repair-construction data
runtime construction budget
```

and differ only in whether the actual latent-sign geometry or a frozen arbitrary code organizes repair composition.

The key geometry-sensitive comparison is therefore:

```text
factorized true-code transfer
vs
factorized random-code transfer.
```

No random-code seed may be selected based on science outcomes.

---

## 11. Evidence interface and evaluator separation

The repair constructor and recovery evaluator must use disjoint stochastic specimens.

Define at least three private RNG domains:

```text
S_construct  = dedicated repair construction
S_calibrate  = protocol / language calibration only
S_eval       = untouched science evaluation
```

The old authority-observer holdout seed `271828` should **not** be reused as the scientific `S_eval` field, because that surface has already been repeatedly inspected.

For science evaluation, freeze a fresh private seed family before execution.

Within an evaluation event, arms must receive matched:

```text
validation examples
labels
timesteps
region-conditioned noise
```

so arm contrasts are paired.

Evaluator inputs must not be available to `G` during repair construction.

---

## 12. Recovery quantities

For each held-out region `r`, define on fresh evaluator data:

```text
L_0(r)       = base-model loss
L_direct(r)  = dedicated evaluator-side repair loss
L_fact(r)    = true-code factorized repair loss
L_rand(r)    = random-code factorized repair loss
L_mean(r)    = mean-repair loss
L_retr(r)    = nearest-retained-repair loss
```

A useful descriptive normalized transfer quantity is:

```text
F_fact(r)
  = [L_0(r) - L_fact(r)]
    / [L_0(r) - L_direct(r)]
```

when the denominator is positive and passes the direct-repair adequacy rule.

Analogous `F_rand`, `F_mean`, and `F_retr` quantities may be recorded.

Interpretation:

```text
F = 0  -> none of the dedicated-repair gain recovered
F = 1  -> all of the dedicated-repair gain recovered
```

This ratio is descriptive unless promoted prospectively into the frozen primary endpoint.

---

## 13. Recovery must include damage guardrails

Target-region loss alone is insufficient because a nominal repair could improve one region by damaging general competence elsewhere.

The frozen recovery evaluator `Rec^dagger` must therefore combine:

```text
target-region improvement
AND
cross-region / global damage bound.
```

Exact thresholds are **not frozen in this design document**.

They must be selected from calibration-only data or independent prior reasoning before science execution.

A candidate binary form is:

```text
Rec^dagger(r,Delta) = 1[
    target improvement >= delta_min
    AND
    global/cross-region damage <= eta_max
].
```

The same evaluator must be applied identically to every repair arm.

---

## 14. Cost ledger

Do not use `16D / 5D = 3.2x` as a scientific compression claim.

Every arm requires a prospectively frozen resource ledger.

Candidate decomposition:

```text
C_total
  = C_common
  + C_repair_artifact
  + C_constructor
  + C_routing
  + C_runtime
  + C_retained_state.
```

Where:

```text
C_common
= base model, fixed region interface, evaluator-independent infrastructure
  shared identically across compared arms.

C_repair_artifact
= retained repair coefficients / vectors / tables under one fixed precision and
  serialization rule.

C_constructor
= executable description / retained learned parameters needed to map retained
  repair structure + admissible context evidence to a repair.

C_routing
= any retained context-to-repair mapping not already included in the fixed
  admissible evidence interface.

C_runtime
= bounded computation required to instantiate / apply the repair.

C_retained_state
= any optimizer, memory, cache, or side state required at deployment.
```

For paired arms, both absolute total cost and incremental repair-specific cost may be reported, but the accounting convention must be identical.

The factorized arm must not receive a free constructor while direct-retention arms are charged for equivalent routing machinery.

The random-code factorization must be cost-matched to the true-code factorization.

---

## 15. Direct-retention baseline distinction

Two different direct objects must remain separate.

### Development-only retained table

Stores the eight observed development repairs and uses a frozen retrieval rule at held-out contexts.

This is a legitimate competing architecture under the same held-out information boundary.

### Full 16-region dedicated table

Includes dedicated repairs for held-out regions.

This may be used only as an evaluator-side **explicit full-family artifact cost reference / repair ceiling** unless the protocol explicitly defines a setting where all failure identities were available before deployment.

It is not a fair held-out-transfer learner arm.

Therefore:

```text
direct oracle ceiling
!= direct-retention architecture under held-out transfer.
```

---

## 16. Independent replication unit

The scientific replication unit must be the independently trained base model / training seed.

The eight held-out regions within one model are paired repeated conditions, not eight independent system replications.

Thus no science analysis may treat:

```text
8 regions x N seeds
```

as `8N` independent trained-system replicates.

Exact science seed count and seed values remain OPEN until freeze.

Fresh science seeds should be disjoint from calibration-only seeds and, preferably, from the previously inspected authority-replication training seeds.

---

## 17. Candidate primary discriminator

The primary science question should be formulated at the **training-seed level**, using a prospectively frozen aggregate over the eight held-out contexts.

The preferred qualitative target is:

```text
true-code factorization
>
random-code factorization
```

on held-out repair performance, conditional on direct-repair adequacy.

A mean/median normalized-transfer contrast, paired recovery-count contrast, or another seed-level statistic may be selected at freeze.

No endpoint is frozen by this design document.

Do not define the endpoint after observing science seeds.

---

## 18. Decision hierarchy

The first classification gate is repair-language adequacy.

```text
IF dedicated direct repair fails declared adequacy:
    REPAIR_LANGUAGE_INSUFFICIENT
    -> no factorization / H_CRCB conclusion.
```

Conditional on adequate dedicated repair:

```text
IF true-code factorization fails held-out transfer:
    NO_DEMONSTRATED_REPAIR_FACTORIZATION_IN_FROZEN_LANGUAGE

IF true-code factorization transfers but does not beat matched random-code / mean / retrieval controls:
    HELDOUT_TRANSFER_OBSERVED_BUT_GEOMETRIC_FACTORIZATION_NOT_IDENTIFIED

IF true-code factorization prospectively beats matched controls:
    HELDOUT_REPAIR_FACTORIZATION_SUPPORTED_IN_FROZEN_SPECIMEN
```

Only if the frozen cost ledger also shows a lower charged retained-resource cost at matched recovery may an additional artifact-level statement be made:

```text
STRUCTURAL_REPAIR_COMPRESSION_SUPPORTED_RELATIVE_TO_FROZEN_BASELINE
```

This remains an artifact/baseline-relative claim, not an unrestricted `kappa_gen < kappa_direct` theorem.

---

## 19. Claim ceiling

A positive XM-CRCB-001 result may support at most:

> **In the frozen XM-trained ImageNet-subset specimen, under the frozen repair language, context interface, repair-construction budget, constructor, and independent evaluator, a compact factorized repair representation built only from development-region repairs generated functionally useful repairs for prospectively held-out latent contexts, and [if separately earned] did so at lower charged retained-resource cost than the declared direct-retention artifact baseline.**

It may not establish:

- intrinsic minimum correction complexity;
- universal `H_CRCB`;
- a new optimizer mechanism;
- general corrigible compression;
- authority starvation or competence-selective routing;
- full-ImageNet scaling;
- topology invention;
- that the four sign coordinates are uniquely privileged;
- that all repair geometry is first-order / additive;
- that a successful constructor cannot be reduced to ordinary approximation / compression theory.

A negative result must also remain local to the frozen repair language, constructor, context family, budget, and horizon.

---

## 20. Anti-tautology audit mapping

The design must explicitly satisfy the correction-complexity admissibility conditions:

```text
A1 basis precedes held-out failure identity
   -> B fitted only from R_dev dedicated repairs.

A2 fixed constructor
   -> least-squares main-effect constructor frozen before science.

A3 constructor complexity not free
   -> C_constructor charged in cost ledger.

A4 no evaluator leakage
   -> Rec^dagger / S_eval not inputs to G.

A5 evidence provenance fixed
   -> region code and construction/evaluation RNG domains frozen.

A6 recovery resources counted
   -> J, runtime application cost, retained state, and any search counted.

A7 recovery criterion independent of mechanism
   -> identical Rec^dagger across all arms.

A8 reusability requires transfer
   -> primary evidence comes from R_test and fresh trained-system seeds.
```

Any protocol freeze must contain an explicit pass/fail audit for these eight conditions.

---

## 21. What remains OPEN before protocol freeze

No executable should be written until the following are prospectively resolved:

```text
1. exact frozen base organism commit and model hyperparameters
2. exact repair-language calibration ladder
3. direct-repair adequacy criterion
4. repair optimizer, J, LR, examples, timestep/noise construction
5. random-code seed / code-map generation rule and rank audit
6. fresh evaluator seed family
7. exact Rec^dagger target-improvement and damage thresholds
8. exact cost / precision / serialization accounting rule
9. exact training-seed replication count and science seeds
10. primary seed-level endpoint and analysis rule
11. stopping / exclusion rules for regions with inadequate direct repair
12. custody format and frozen output schema
```

Calibration may resolve declared calibration questions only. It may not inspect or optimize against science-seed outcomes.

---

## 22. Current status after opening this lineage

```text
XM-CRCB-001                    = QUESTION EARNED
PROTOCOL DESIGN                = OPEN
PROTOCOL FREEZE                = NOT YET
EXECUTABLE                     = NONE
SCIENCE EXECUTION              = NOT AUTHORIZED
H_CRCB EVIDENCE                = NONE
OLD XM AUTHORITY HYPOTHESIS    = NOT REOPENED
AUTHORITY_GROUNDING CHECKPOINT = UNCHANGED
BL-003                         = UNOPENED
```

Shortest current compression:

> **Use XM as a repair-factorization chassis: test whether dedicated corrections across fixed latent contexts admit a compact, prospectively frozen representation that transfers to unseen contexts under honest resource accounting.**
