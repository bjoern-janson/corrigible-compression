# Reduction Gate and Generative Correction Complexity — Conceptual Freeze 001

Status:

```text
FIXED-BASIS ADAPTIVE EPISTEMIC CONTROL = SUPPORTED PROGRAM ABSTRACTION
CORRECTIVE REACH                         = SUPPORTED LOCALLY
CC-SPECIFIC IRREDUCIBILITY              = UNESTABLISHED
FIXED-BASIS CC MECHANISMHOOD            = REDUCIBLE IN CURRENT COMPLETED SETTING
KAPPA_GEN                                = FORMAL CANDIDATE — RELATIVE / FALSIFIABLE
H_CRCB                                   = OPEN HYPOTHESIS
META-AUTHORITY CLOSURE                   = OPEN
BL-003                                   = UNOPENED
NEW ASSAY                                = NONE
```

This document is a **conceptual freeze**, not a new empirical result. It records the current reduction gate, the conditional fixed-basis reduction, the bounded-reopenability pressure test, and a formal candidate measure for reusable correction machinery.

It must not be cited as evidence that corrigible compression is an independent mechanism.

---

## 1. Reduction gate

The current empirical ladder is compatible with a common abstraction:

```text
measure / intervene
-> update
-> allocate
-> act
-> consequence
-> update
-> reallocate
```

The narrow shared object is:

```text
fixed-basis adaptive epistemic control
```

with two separable capabilities:

```text
E_alloc = allocation efficiency
R_corr  = corrective reach
```

The reduction gate is:

> **Before any purported CC-specific assay, specify a prediction under a CC hypothesis that a genuinely strong adaptive-control hypothesis cannot reproduce.**

A strong adaptive-control comparator must already include, where relevant:

```text
complete relevant task state
+ full current belief state
+ channel state and dynamics
+ future information value
+ delayed consequences
+ long-horizon control value
```

Therefore:

```text
information helps    != CC-specific
exploration helps    != CC-specific
feedback helps       != CC-specific
error correction     != CC-specific
useful channels help != CC-specific
```

BL×CC-001 is evidence for a **controllable feedback property**. It is not yet evidence for corrigibility as a distinct mechanism.

---

## 2. Conditional fixed-basis reduction

Let a strong Bayes-adaptive controller use hyperstate:

```text
Z_t = (X_t, B_t, C_t)
```

where:

- `X_t` is complete relevant task state;
- `B_t` is sufficient belief over the supplied world/model family;
- `C_t` contains consequential observation, intervention, feedback, and correction-channel state.

Assume:

```text
A1: T* is inside the represented model/hypothesis support relevant to the task.
A2: B_t is sufficient for represented uncertainty.
A3: C_t contains all consequential channel state.
A4: relevant channel transitions are correctly represented.
A5: the relevant objective is fixed and represented.
A6: epistemic retention/update is lossless for relevant represented state.
A7: planning is sufficiently long-horizon and optimal for the fixed objective.
```

Under these assumptions, any represented future value of preserving a corrective route `Xi` appears in ordinary action value:

```text
Q*(Z_t, Preserve(Xi)) - Q*(Z_t, Delete(Xi)).
```

If preserving `Xi` changes represented future observations, beliefs, action opportunities, or consequences, strong adaptive control can price it.

If preserving `Xi` changes none of those represented quantities, then any later benefit must come from a failure of the closure assumptions.

Current conditional compression:

> **Within the completed fixed-basis setting, no independent CC behavioral remainder has yet been identified beyond sufficiently complete adaptive control.**

This is a conceptual reduction result, not an empirical theorem about all controllers.

---

## 3. Universal-support pressure test

Literal finite support failure is not by itself a fundamental escape from adaptive control.

An ideal universal Bayesian mixture can assign positive support to every environment expressible in a fixed universal language. Hierarchical uncertainty over model classes can likewise be marginalized into a larger mixture when the relevant possibilities remain representable.

Therefore:

```text
uncertainty about H_t
!= automatic CC-specific content
```

The sharper distinction is:

```text
syntactic support
!= operationally priceable support
```

A bounded learner may have a compact universal language while lacking the computation, memory, information, or time required to identify and price the correction-relevant possibilities before the decision deadline.

The unresolved bounded-control problem is therefore about **effective accessibility**, not merely formal membership in a hypothesis language.

---

## 4. Weak universal coverage is too weak

Suppose correction routes are countable:

```text
Xi = {xi_1, xi_2, ...}
```

A bounded policy can preserve one route while assigning:

```text
P(xi_i preserved) = 2^-i.
```

Every route then has positive pointwise preservation probability while expected preservation cost remains finite.

So the statement:

```text
boundedness + universal nonzero pointwise coverage + selectivity is impossible
```

is false.

The meaningful object must require a **uniformly nontrivial recoverability guarantee**, not mere positive support.

---

## 5. Bounded uniform reopenability

Let `P_H` be the random set of correction routes preserved through horizon `H`.

With unit preservation cost, impose:

```text
E_pi |P_H| <= K < infinity.
```

For environment `e`, define evaluator-side recovery event:

```text
R_H(e, pi) = 1[learner can recover by H].
```

Define maximin reopenability:

```text
Gamma_K(E)
  = sup_{pi: E|P_H| <= K}
      inf_{e in E} P_pi(R_H = 1 | e).
```

For the symmetric adversarial family `E_N = {e_1,...,e_N}` with:

1. pre-reveal learner-visible histories identical across all `e_i`;
2. environment `e_i` recoverable iff unique route `xi_i` is preserved;

then:

```text
Gamma_K(E_N) = min(1, K/N)
```

for integer `K <= N`, with the upper bound achieved by uniformly choosing a `K`-element subset.

If an open-ended class contains such disjoint indistinguishable subfamilies for arbitrarily large `N`, then for every finite `K`:

```text
Gamma_K(E_infty) = 0.
```

Durable statement:

> **Without structure that reduces correction diversity or reveals which corrective route matters, finite preservation capacity cannot provide a uniform positive recoverability guarantee over an open-ended family of mutually indistinguishable, correction-diverse failures.**

This constrains every bounded policy. It is not a CC-specific theorem.

---

## 6. Correction-cover complexity

For each environment `e`, let `K(e)` be the set of directly preserved routes sufficient for recovery.

Define direct correction-cover cost:

```text
kappa(E)
  = inf_{P subset Xi} {
      c(P):
      P intersects K(e) for every e in E
    }.
```

This is a hitting-set quantity.

Important distinction:

```text
environmental complexity
!= correction-cover complexity
```

A very large environment class may be easy to keep recoverable if many failures share a small set of correction routes.

---

## 7. Fixed correction architecture

The generative extension must be defined relative to a prospectively fixed architecture:

```text
A = (L_A, B_adm, G, O, c, H, Rec^dagger)
```

where:

- `L_A` = permitted language of corrective affordances;
- `B_adm` = admissible preserved bases;
- `G` = fixed evidence-conditioned repair constructor;
- `O` = fixed admissible observation/challenge interface;
- `c` = preservation cost model;
- `H` = fixed recovery horizon/resource budget;
- `Rec^dagger` = independently specified evaluator-side recovery criterion.

For failure `e`, admissible evidence is:

```text
Z_e^H ~ O(e, B, G)
```

and the fixed constructor produces:

```text
pi_e^B = G_H(B, Z_e^H).
```

`G` does not receive hidden environment identity, oracle repair labels, or evaluator success labels.

---

## 8. Generative correction complexity

For a preserved basis `B`, define:

```text
p_e(B)
  = P[Rec^dagger(e, pi_e^B, Z_e^H) = 1].
```

Then define the formal candidate:

```text
kappa_gen^{H,rho}(E | A, Rec^dagger)
  = inf_{B in B_adm} {
      c(B):
      inf_{e in E} p_e(B) >= rho
    }.
```

If no finite-cost basis reaches the required uniform recovery level:

```text
kappa_gen^{H,rho} = infinity.
```

Interpretation:

> **Minimum cost of a fixed reusable affordance basis from which the frozen constructor can generate sufficient recovery procedures across the stated failure class within the stated horizon and recovery threshold.**

This is a relative complexity measure, not a scalar measure of “corrigibility.”

---

## 9. Anti-tautology admissibility conditions

The candidate measure is meaningful only if the correction answer cannot be hidden in the basis, constructor, evidence interface, or evaluator.

### A1 — Basis precedes failure identity

The preserved basis is fixed before hidden held-out failure identity is revealed, conditional only on prospectively admissible information.

### A2 — Fixed constructor

`G` is frozen independently of held-out failures.

### A3 — Constructor complexity is not free

When comparing architectures with different constructors, account for constructor description size, retained working state, construction compute, and other relevant resources. A tiny `B` with a giant failure lookup table inside `G` is not low correction complexity.

### A4 — No evaluator leakage

```text
Rec^dagger not in Inputs(G).
```

### A5 — Evidence provenance fixed

`O` prospectively determines what evidence is available, when it arrives, and which channels can be influenced by the learner.

### A6 — Recovery resources counted

A tiny basis followed by unbounded repair search does not satisfy bounded correction complexity. `H` must constrain the relevant time, compute, retained state, and interactions.

### A7 — Recovery criterion independent of mechanism

`Rec^dagger` is fixed independently of `B` and `G`.

### A8 — Reusability requires transfer

Claims of generic reusable correction structure require the same frozen basis/constructor architecture to succeed on held-out failures. Memorizing the development failure set is not evidence for a compact reusable correction basis.

---

## 10. Basic sanity properties

Under a fixed architecture and cost model, the candidate should satisfy:

```text
E_1 subset E_2
=> kappa_gen(E_1) <= kappa_gen(E_2)
```

```text
rho_1 <= rho_2
=> kappa_gen^{H,rho_1} <= kappa_gen^{H,rho_2}
```

and, when a larger horizon only enlarges the admissible recovery computation/interactions:

```text
H_1 <= H_2
=> kappa_gen^{H_2,rho} <= kappa_gen^{H_1,rho}.
```

The direct hitting-set measure is recovered as a special case when `G` cannot synthesize new repair procedures and can only invoke directly preserved routes.

---

## 11. Compact reusable correction basis hypothesis

The substantive open hypothesis is:

```text
H_CRCB:
there exist structurally meaningful failure classes for which
kappa_gen^{H,rho}
<<
kappa_direct^{H,rho}
under a prospectively frozen architecture and evaluator.
```

In words:

> **Some structured failure classes may admit substantial compression of recovery machinery: a fixed low-cost affordance basis and constructor can generate successful repairs across held-out failures much more cheaply than directly preserving failure-specific repairs.**

This hypothesis can fail because:

- `G` fails to generalize;
- required evidence is unavailable;
- construction exceeds `H`;
- basis cost grows with failure diversity;
- held-out failures require new affordances;
- recovery probability falls below `rho`;
- apparent compression was hidden in `G`;
- or `Rec^dagger` shows that the generated changes were not recoveries.

No empirical evidence for `H_CRCB` is currently claimed.

---

## 12. Information versus correction diversity

For a clean finite model with `N` disjoint correction requirements, preservation capacity `K`, and at most `M` perfectly discriminating transcript classes before preservation is finalized, the earlier adversarial argument yields:

```text
Gamma_{K,M}(E_N) <= min(1, K M / N).
```

If `M = 2^b`, then:

```text
Gamma_{K,b} <= min(1, K 2^b / N).
```

This is a schematic deterministic-information extension, not a general noisy-channel theorem.

It exposes the resource tradeoff:

```text
preservation capacity
x discriminating information
vs correction diversity.
```

---

## 13. Purpose / authority is a separate axis

Ordinary epistemic correction updates beliefs while keeping the objective fixed:

```text
P_t(M) -> P_{t+1}(M).
```

Purpose correction changes the criterion itself:

```text
U_t -> U_{t+1}.
```

If a fixed meta-objective or authority rule `Phi^dagger` adjudicates legitimate objective changes, then purpose correction can be represented as generalized adaptive control over an augmented state containing the current objective and authority channel.

Therefore:

```text
purpose correction under fixed Phi^dagger
= reducible to generalized adaptive control in principle.
```

The open recursive boundary is **meta-authority closure**:

> What determines legitimate changes to the rule that determines legitimate changes?

This is not currently identified as a CC-specific mechanism.

---

## 14. Recovery evaluator boundary

Correction machinery and authority for deciding what counts as correction are distinct:

```text
correction architecture
!= authority/evaluator defining recovery.
```

When `U_t` itself is the object being corrected, the evaluator cannot silently be `U_t`:

```text
Rec^dagger != U_t
```

otherwise the potentially wrong objective defines whether replacing itself counts as success.

Purpose-level correction complexity is therefore explicitly relative to a prospectively fixed external or higher-order authority/evaluation rule.

There is no evaluator-free claim here that one purpose revision is “correct.”

---

## 15. Three non-collapsed axes

Current conceptual map:

```text
WORLD / MODEL
P(M) -> H -> R

PURPOSE / AUTHORITY
U -> U-family -> Phi / authority

CORRECTION COMPRESSION
E -> direct correction requirements -> kappa -> kappa_gen^{H,rho}
```

These axes answer different questions:

1. What models/distinctions can the learner express?
2. What counts as success, and what can legitimately revise that criterion?
3. How much reusable corrective machinery must survive for the stated failure class?

Do not collapse them.

---

## 16. Current scientific posture

```text
BL-001                         = POSITIVE
BL-002                         = POSITIVE
BL×CC-001                      = POSITIVE / AUDITED / PARKED
fixed-basis adaptive control   = SUPPORTED PROGRAM ABSTRACTION
corrective feedback reach      = SUPPORTED LOCALLY
CC-specific irreducibility     = UNESTABLISHED
fixed-basis CC mechanismhood   = REDUCIBLE IN CURRENT COMPLETED SETTING
H_CRCB                         = OPEN
kappa_gen^{H,rho}              = FORMAL CANDIDATE
meta-authority closure         = OPEN
BL-003                         = UNOPENED
new assay                      = NONE
```

Current strongest compression:

> **Compress the machinery required to remain repairable across a structured failure class, not the list of future failures themselves.**

Immediate constraint:

> **Correction complexity is always relative to a frozen affordance language, constructor, evidence interface, cost model, horizon, and independently specified recovery criterion.**

And the reduction firewall remains active:

> **A useful correction architecture does not by itself imply a CC-specific mechanism. If strong adaptive control can price the same structure, the behavioral explanation remains reducible.**

---

## 17. Next-action discipline

No experiment is opened by this conceptual freeze.

The next mathematical task is:

```text
derive nontrivial upper/lower bounds for kappa_gen^{H,rho}
and attempt constructive examples where reusable correction machinery
compresses direct recovery cost without hiding the compression in G.
```

Three acceptable outcomes:

```text
CONSTRUCTIVE:
large failure diversity + provably small kappa_gen.

LOWER BOUND:
kappa_gen necessarily scales with a stated structural complexity of E.

COLLAPSE:
apparent compression can always be re-expressed as complexity moved into G
under the chosen accounting boundary.
```

Do not design `CC-002` or `BL-003` by default.
