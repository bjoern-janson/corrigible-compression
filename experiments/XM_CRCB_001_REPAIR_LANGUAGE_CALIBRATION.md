# XM-CRCB-001 — Repair-Language Adequacy Calibration

Status:

```text
CALIBRATION PROTOCOL = FROZEN
CALIBRATION RUN      = UNRUN
SCIENCE RUN          = NOT AUTHORIZED
FACTORIAL ENDPOINT   = SEALED / NOT INVOKED
SCIENCE SEEDS        = NOT FROZEN
```

This document freezes the **calibration-only repair-language adequacy gate** for `XM-CRCB-001`.

It answers exactly one question:

> **Can a prospectively declared bounded repair language produce reliable region-specific competence improvement with bounded collateral damage at all?**

It does **not** test parity factorization, held-out repair transfer, `H_CRCB`, authority starvation, high-`K` coupling, or any intrinsic correction-complexity claim.

If this gate fails, the science assay does not proceed.

---

## 1. Permanent separation

The calibration result is only about viability of the primitive repair substrate.

```text
repair-language adequacy
!= repair factorization
!= held-out transfer
!= artifact compression
!= intrinsic optimum separation
```

The only legitimate terminal calibration classifications are:

```text
REPAIR_LANGUAGE_ADEQUATE
REPAIR_LANGUAGE_INSUFFICIENT
CALIBRATION_APPARATUS_FAILURE
```

No calibration output may be used to claim that repair structure factorizes.

---

## 2. Calibration must not consume science contexts

The eventual science assay uses the already inherited 4-bit XM region partition with region seed:

```text
SCIENCE_REGION_SEED = 314159
```

and the 8/8 parity split over that partition.

Calibration must not use any of those 16 science contexts for language selection.

Therefore calibration uses a **separate 4-bit latent partition** on the same latent dimensionality:

```text
CAL_REGION_SEED = 271829
flat_dim        = 4096
CAL_COORDS      = [651, 1449, 2382, 3402]
```

The inherited science coordinates are:

```text
SCIENCE_COORDS = [808, 1575, 2250, 2349]
```

and the two coordinate sets are disjoint.

The calibration partition is fixed before any calibration outcome and may not be changed after execution.

Calibration region IDs:

```text
R_cal = {0, 5, 10, 15}
```

These four contexts are balanced over every calibration sign bit.

No science region, science parity assignment, science repair, or science endpoint is inspected during calibration.

---

## 3. Calibration-only base organisms

Calibration uses two independently trained base models:

```text
CAL_BASE_SEEDS = {606, 707}
```

These seeds are permanently reserved for calibration and may not later be counted as XM-CRCB-001 science replication units.

Each base model uses the frozen real-XM/ImageNet chassis:

```text
K_train                  = 2
model                     = class-conditional continuous image DiT
model size                = vit_base
image size                = 256x256
patch size                = 2
supervision               = velocity / flow matching
train examples            = 4096 frozen ImageNet latent cache
validation examples       = 256 frozen ImageNet latent cache
optimizer steps           = 2049
batch size                = 8
peak training LR          = 1e-4
weight decay              = 0.01
warmup steps              = 20
gradient clip             = 1.0
CFG dropout               = 0.1
EMA                       = 0.9999
precision                 = 16-mixed on P100
```

The data/cache identities must match the already-audited real-XM specimen before calibration training begins.

The final **raw non-EMA model state** at step 2049 is `theta_0` for repair construction and calibration evaluation.

A final checkpoint must be written and custody-hashed for each calibration base seed.

The authority observer is not required and no `rho` quantity is read.

---

## 4. Calibration-only example partition

The frozen 256-example validation cache is partitioned by index:

```text
0   .. 63   = CAL_CONSTRUCT_POOL
64  .. 127  = CAL_EVAL_POOL
128 .. 255  = SCIENCE_RESERVED_POOL
```

The science-reserved pool is untouched by language calibration.

No example may move between these pools after calibration begins.

The base model was not trained on the validation cache.

---

## 5. Repair-language ladder

Exactly three nested candidate languages are declared.

### L_A^(1) — output projection only

Trainable parameters:

```text
model.final_layer.linear.weight
model.final_layer.linear.bias
```

All other parameters are frozen.

### L_A^(2) — full DiT FinalLayer

Trainable parameters:

```text
model.final_layer.*
```

including the output projection and `final_layer.adaLN_modulation`.

All earlier transformer blocks and embedders remain frozen.

### L_A^(3) — final transformer block + FinalLayer

Trainable parameters:

```text
model.blocks[-1].*
model.final_layer.*
```

All preceding blocks and embedders remain frozen.

No fourth language may be invented after observing calibration outcomes.

---

## 6. Sequential stopping rule

The ladder is evaluated strictly in order:

```text
L_A^(1) -> L_A^(2) -> L_A^(3)
```

For candidate `k`:

```text
if L_A^(k) passes all frozen adequacy gates:
    select L_A^star = L_A^(k)
    stop calibration
    do not evaluate any larger language
else:
    advance to the next declared language
```

If `L_A^(3)` fails:

```text
REPAIR_LANGUAGE_INSUFFICIENT
```

and XM-CRCB-001 science remains unauthorized.

Rows above the selected language are recorded as failed.
Rows below the selected language are recorded as:

```text
NOT_RUN_BY_STOP_RULE
```

No "best-performing language" selection is permitted.

---

## 7. Dedicated repair construction budget

Every dedicated repair starts from the identical base state `theta_0` for its calibration base seed.

No repair is initialized from another repaired model.

For every attempted language, base seed, calibration region, and construction replicate, use:

```text
optimizer        = AdamW
learning rate    = 1e-4
betas            = (0.9, 0.95)
eps              = 1e-8
weight decay     = 0.0
repair steps J   = 32
batch size       = 8
gradient clip    = 1.0
```

Only parameters inside the current candidate `L_A^(k)` have `requires_grad=True`.

No learning-rate sweep, optimizer sweep, step-count sweep, or per-language hyperparameter tuning is allowed.

Optimizer state is ephemeral construction machinery. It is not part of the retained repair artifact, but construction compute/time must be logged for later resource accounting.

---

## 8. Construction RNG domains

Three independent repair-construction replicate seeds are frozen:

```text
CAL_REPAIR_SEEDS = {1101, 1102, 1103}
```

For every `(base_seed, region, repair_seed)` tuple, the repair-construction RNG domain determines:

- permutation of the 64 construction examples;
- region-conditioned Gaussian noise;
- continuous flow-matching timesteps;
- any other stochastic quantity not already fixed by the base checkpoint.

Each 32-step repair presents exactly:

```text
32 * 8 = 256
```

example instances.

The 64 construction examples are traversed once per 8-step cycle, for four cycles total. Each cycle uses a seed-derived fresh permutation and fresh region-conditioned noise/timesteps.

No construction RNG stream is reused as an evaluation RNG stream.

---

## 9. Construction objective

The repair objective is the same per-example velocity / flow-matching prediction loss used by the organism, restricted to calibration-region-conditioned latent noise.

For repair construction:

- use the raw `theta_0` model;
- gradients are enabled only for `L_A^(k)`;
- classifier labels are retained;
- no best-of-K repair search is permitted;
- the candidate calibration region is supplied only through the frozen region-conditioned noise construction;
- no evaluator result, held-out repair, science region, or factorization object is available.

The repair artifact is the parameter difference:

```text
Delta_{base,region,repair_seed}^{(k)}
= theta_repaired - theta_0
```

restricted to `L_A^(k)`.

---

## 10. Fresh calibration evaluator

Freeze one evaluator RNG domain:

```text
CAL_EVAL_SEED = 1201201
```

The evaluator uses only `CAL_EVAL_POOL` indices 64..127.

For each of the 16 calibration-partition regions, construct one fixed evaluation bank containing matched:

```text
64 validation examples
64 labels
64 continuous timesteps
64 region-conditioned Gaussian noise tensors
```

The bank is constructed once from `CAL_EVAL_SEED` and then reused identically across:

- base model;
- null-update control;
- every dedicated repair replicate;
- every attempted repair language.

Thus every calibration contrast is paired at the example/timestep/noise level.

`CAL_EVAL_SEED` is unavailable to repair construction.

The old real-XM authority holdout seed `271828` is not reused.

---

## 11. Base, target-gain, and collateral quantities

For a target calibration region `r`, let:

```text
L_0(q)
```

be the mean frozen evaluator loss of the base model in calibration region `q`.

For a dedicated repair targeted to `r`, let:

```text
L_direct(r -> q)
```

be the evaluator loss of the repaired model in region `q`.

Define relative target gain:

```text
G_rel(r)
  = [L_0(r) - L_direct(r -> r)] / L_0(r).
```

For every non-target region `q != r`, define positive relative collateral degradation:

```text
d(r -> q)
  = max(0, [L_direct(r -> q) - L_0(q)] / L_0(q)).
```

Define:

```text
D_mean(r)
  = mean_{q != r} d(r -> q)

D_max(r)
  = max_{q != r} d(r -> q).
```

These relative quantities are the frozen adequacy quantities. Absolute losses are also retained for audit.

---

## 12. Frozen per-repair recovery predicate

The numerical thresholds are frozen before calibration execution:

```text
delta_G      = 0.020   # at least 2.0% relative target-loss improvement
delta_D_mean = 0.005   # at most 0.5% mean positive collateral degradation
delta_D_max  = 0.020   # at most 2.0% worst positive collateral degradation
```

For one dedicated repair replicate:

```text
Rec_cal^dagger = 1
iff
    G_rel  >= delta_G
and D_mean <= delta_D_mean
and D_max  <= delta_D_max.
```

No threshold may be moved after seeing calibration results.

These thresholds are **calibration gates only**. They do not automatically become the science endpoint for held-out factorization.

---

## 13. Repeatability gate

For each `(base_seed, calibration_region)` group, there are exactly three repair-construction replicates from seeds `{1101,1102,1103}`.

The group passes the repeatability gate iff all of the following hold:

```text
1. at least 2 of 3 replicates satisfy Rec_cal^dagger = 1;
2. all 3 replicates have G_rel > 0;
3. max(G_rel) - min(G_rel) <= 0.030.
```

The third condition limits construction-seed spread to at most 3 percentage points of relative target gain.

No replicate may be discarded as an outlier.

---

## 14. Language-level adequacy gate

There are:

```text
2 calibration base seeds
x 4 calibration target regions
= 8 base-region groups.
```

Define:

```text
rho_lang = 7/8 = 0.875.
```

A candidate repair language `L_A^(k)` is **adequate** iff:

```text
A. at least 7 of 8 base-region groups pass the repeatability gate;

B. each calibration base seed has at least 3 of its 4 regions pass;

C. the null-update apparatus audit passes;

D. all expected repair/evaluation artifacts are custody-valid.
```

The first language satisfying A-D becomes:

```text
L_A^star.
```

No aggregate mean gain can override a failed group-count criterion.

---

## 15. Null-update control — mandatory apparatus gate

For every calibration base seed, clone `theta_0`, execute the same evaluation pipeline, and allow zero parameter movement:

```text
Delta = 0.
```

For every calibration region `q`, require:

```text
abs(L_null(q) - L_0(q)) / max(L_0(q), 1e-12) <= 1e-5.
```

The null control must satisfy:

```text
Rec_cal^dagger = 0
```

for every nominal target region because its target gain is zero up to numerical tolerance.

If the null audit fails:

```text
CALIBRATION_APPARATUS_FAILURE
```

and no language decision is valid.

A random-update control may be recorded later as a descriptive calibration diagnostic, but it is not required for the frozen adequacy gate and cannot change the gate.

---

## 16. Calibration result table

The frozen calibration summary must contain one row per declared language:

```text
language
attempted? / NOT_RUN_BY_STOP_RULE
number of base-region groups passed / 8
empirical group pass fraction
per-base region pass counts
median G_rel across attempted repair replicates
range / distribution of G_rel
median D_mean
max observed D_max
null audit status
custody status
classification
```

The final calibration report emits exactly one terminal decision:

```text
REPAIR_LANGUAGE_ADEQUATE: L_A^star = <first passing language>
```

or:

```text
REPAIR_LANGUAGE_INSUFFICIENT
```

or:

```text
CALIBRATION_APPARATUS_FAILURE
```

---

## 17. No factorization peeking

During calibration it is forbidden to:

- form the parity development/test split on the science partition for evaluation;
- construct the five-component factorized basis;
- fit any true-code or random-code repair constructor;
- evaluate held-out science-context transfer;
- compare true-code versus random-code factorization;
- inspect a science endpoint;
- choose science seeds;
- change the calibration language ladder because a factorization result looks weak or strong.

Calibration may inspect only its own dedicated-repair adequacy quantities.

---

## 18. Repair-language failure interpretation

If no declared language passes, the earned conclusion is only:

> **Under the frozen calibration organisms, region interface, repair-construction budget, and declared three-level parameter-subspace ladder, no candidate repair language met the prospectively frozen direct-repair adequacy gate.**

Classification:

```text
REPAIR_LANGUAGE_INSUFFICIENT
```

Not allowed:

```text
H_CRCB false
repair does not factorize
XM has no reusable repair structure
regional competence is irreparable
```

The failure locus is the chosen repair substrate/budget until independent evidence supports a deeper conclusion.

---

## 19. Adequacy-pass interpretation

If a language passes, the earned conclusion is only:

> **The first passing frozen repair language can produce repeatable target-region competence improvements with bounded collateral damage on the separate calibration organisms and calibration partition under the declared construction budget.**

Classification:

```text
REPAIR_LANGUAGE_ADEQUATE
```

This authorizes preparation of the separate science freeze.

It does **not** itself support:

- repair factorization;
- held-out transfer;
- lower repair complexity;
- intrinsic compression;
- a CC-specific optimizer;
- an authority claim.

---

## 20. Custody schema

Calibration must fail closed unless every executed object is preserved and hash-auditable.

### 20.1 Global calibration manifest

Record:

```text
corrigible-compression protocol commit
xm-oc scientific/apparatus commit
calibration launcher/executable blob hashes
exact Python/PyTorch/CUDA environment
ImageNet dataset revision
train/validation cache hashes
CAL_REGION_SEED and CAL_COORDS
R_cal
CAL_BASE_SEEDS
CAL_REPAIR_SEEDS
CAL_EVAL_SEED
validation example index partition
repair-language ladder
optimizer / J / LR / batch / clipping
all numeric adequacy thresholds
sequential stopping rule
```

### 20.2 Per-base-seed custody

For each calibration base seed preserve:

```text
base training stdout/stderr log
base training configuration
final step-2049 raw checkpoint
checkpoint SHA-256
training exit code
data/cache identity audit
```

### 20.3 Per-repair custody

For every attempted `(language, base_seed, region, repair_seed)` preserve:

```text
repair configuration JSON
construction RNG identity
ordered construction example indices
parameter-name whitelist for L_A^(k)
pre-repair selected-parameter hash
post-repair selected-parameter hash
Delta artifact in deterministic safetensors or equivalent frozen format
Delta SHA-256
construction loss trace
optimizer-step count
construction wall-clock and device metadata
evaluation JSON with L_0, L_direct, G_rel, D_mean, D_max, Rec_cal^dagger
process exit code
```

### 20.4 Evaluator custody

Preserve one canonical evaluator-bank manifest containing hashes of:

```text
CAL_EVAL_POOL indices
labels
timesteps
region-conditioned noise bank per calibration region
CAL_EVAL_SEED
```

The evaluator bank must be identical across all attempted arms.

### 20.5 Language-summary custody

For each attempted language preserve:

```text
8 base-region repeatability-group decisions
per-replicate gate values
null-update audit
language-level A-D gate decisions
terminal pass/fail classification
```

All hashes must be collected before proceeding to a larger repair language or declaring adequacy.

---

## 21. Science-seed firewall

No XM-CRCB-001 science training seed is frozen by this calibration protocol.

Future science seeds must:

```text
exclude {606,707}
be frozen only after calibration custody is complete
be independent of CAL_REPAIR_SEEDS and CAL_EVAL_SEED
```

The future science evaluator must use the untouched `SCIENCE_RESERVED_POOL` or a separately frozen fresh evaluator specimen.

Calibration outcomes may determine only `L_A^star` according to the sequential rule. They may not determine the science parity split, constructor family, random-code seed, or science endpoint direction.

---

## 22. Execution authorization boundary

This document freezes the calibration design only.

It does not yet add an executable to either repository.

The next allowed engineering step is:

```text
implement calibration launcher/evaluator
-> apparatus audit on synthetic or no-op witness
-> verify hashes / null control / parameter whitelist
-> freeze executable
-> run calibration exactly under this protocol
```

No XM-CRCB-001 science execution is authorized until calibration ends in:

```text
REPAIR_LANGUAGE_ADEQUATE
```

with complete custody.

---

## 23. Terminal compression

The adequacy gate is:

```text
bounded dedicated repair
-> fresh target-region improvement
-> bounded non-target damage
-> repeatability across construction seeds
-> reproducibility across calibration base organisms
```

The selected repair language is:

```text
L_A^star = first declared language passing all gates.
```

And the scientific firewall is:

> **First establish that the repair language can repair. Only then ask whether repair itself factorizes and transfers.**
