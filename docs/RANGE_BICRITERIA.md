# Range-Constrained Synthesis Frontier — Mathematical Freeze 003

Status:

```text
UNCONSTRAINED RELATION / SKOLEM SYNTHESIS = ESTABLISHED THEORY TERRITORY
BOOLEAN RELATION MINIMIZATION              = ESTABLISHED THEORY TERRITORY
SHARED IMPLEMENTATION / CIRCUIT SHARING    = ESTABLISHED THEORY TERRITORY
EVIDENCE QUOTIENT tau^O                    = CLEAN REDUCTION
EXPLICIT RANGE-BOUNDED FEASIBILITY         = NP-COMPLETE / SET-COVER TERRITORY
SUCCINCT RANGE-BOUNDED FEASIBILITY         = SIGMA_2^P-COMPLETE UNDER THE STATED ENCODING
RANGE-CONSTRAINED SELECTOR SPECTRUM        = TARGETED SPECIALIZATION — NOVELTY UNKNOWN
RFP AS NEW FOUNDATIONAL PRIMITIVE          = NOT ESTABLISHED
CC-SPECIFIC IRREDUCIBILITY                  = UNESTABLISHED
H_CRCB                                     = OPEN
BL-003                                     = UNOPENED
NEW ASSAY                                  = NONE
```

This document is a **mathematical continuation**, not a new empirical result. It preserves the reduction of the repair-factorization program into established covering and synthesis theory and isolates the surviving bicriteria problem.

It does not modify or reinterpret any frozen experimental artifact.

---

## 1. Current reduction chain

For fixed evidence interface `O`, tolerance `epsilon`, horizon/resource bound `H`, and repair relation, the mathematical layer is now:

```text
pairwise conflict relaxation
-> unrestricted repair hypergraph cover
-> evidence-quotient cover
-> range-constrained minimum implementation complexity
-> static-budget inverse frontier
```

The central hierarchy is:

```text
chi(G_conf)
<= tau_{epsilon,H}
<= tau^O_{epsilon,H}
<= nu_{epsilon,H}(ell).
```

Interpretation:

```text
chi -> tau      = higher-order incompatibility beyond pairwise conflict
tau -> tau^O    = evidence-routing / aliasing penalty
tau^O -> nu     = joint architecture-realizability penalty
```

The first three layers are combinatorial/information-interface objects. The final gap is an implementation/synthesis object.

---

## 2. Evidence quotient remains solved in the finite deterministic setting

For each realized observation `z`, define the evidence fiber:

```text
F_z = O^{-1}(z).
```

For bounded repair policy `pi`, define its validity set:

```text
V_{epsilon,H}(pi)
  = { e : pi is epsilon-valid for e within H }.
```

The evidence-quotient hyperedge induced by `pi` is:

```text
Vhat^O(pi)
  = { z : F_z subseteq V_{epsilon,H}(pi) }.
```

The quotient repair hypergraph is:

```text
H^O_{epsilon,H}
  = { Vhat^O(pi) : pi in Pi_H }.
```

Then:

```text
tau^O_{epsilon,H}
  = tau(H^O_{epsilon,H}).
```

Thus evidence-realizable cover is an ordinary hypergraph-cover problem on observation fibers.

If some observation fiber belongs to no quotient hyperedge, then:

```text
tau^O_{epsilon,H} = infinity.
```

This is **evidence infeasibility**, not merely high implementation complexity.

---

## 3. Architecture layer as constrained relation synthesis

Let `R_O(z,pi)` denote the evidence-quotiented admissibility relation:

```text
R_O(z, pi)
iff
pi is epsilon-valid within H for every failure e with O(e)=z.
```

For branch budget `m`, define the valid selector class:

```text
F^O_{epsilon,H}(m)
  = {
      f : O(E) -> Pi_H
      such that
      R_O(z, f(z)) for every z,
      and |range(f)| <= m
    }.
```

Let `C_H(f)` be the chosen resource-bounded implementation complexity of the full evidence-to-repair transducer.

The inverse implementation spectrum is:

```text
Lambda^O_{epsilon,H}(m)
  = min_{f in F^O_{epsilon,H}(m)} C_H(f) + O(1).
```

The static-budget frontier is its threshold inverse:

```text
nu_{epsilon,H}(ell)
  = min { m : Lambda^O_{epsilon,H}(m) <= ell }.
```

Therefore the architecture question is no longer:

```text
How many repairs exist?
```

It is:

> **Among all evidence-valid selectors using at most `m` distinct repair behaviors, how small can the joint bounded implementation be?**

---

## 4. Fixed-selector implementation reduces to ordinary implementation complexity

For a fixed evidence-valid cover/routing pair `(C,r)`, define the induced repair transducer:

```text
T_{C,r}(z,x)
  = pi_{r(z)}(x).
```

Under equivalent universal implementation languages:

```text
J_H(C,r)
  = C_H(T_{C,r}) + O(1).
```

Thus a fixed routing-and-repair selector does not require a new complexity primitive. Shared substructure is already credited by the complexity of the full joint transducer.

The potentially nontrivial object is the semantic minimization:

```text
min_{f models R_O, |range(f)| <= m} C_H(f).
```

---

## 5. Shared generation is not repair overlap

This distinction remains load-bearing:

```text
shared generation
!=
repair overlap.
```

A parameterized family can require `m=N` distinct runtime repair behaviors while admitting a constant-size common synthesis law.

Example form:

```text
pi_theta(x) = S(theta, x)
```

with evidence routing:

```text
theta = r(z).
```

Then:

```text
C_H(f)
<= C_H(r) + C_H(S) + O(1),
```

rather than:

```text
C_H(r) + sum_theta C_H(pi_theta).
```

But if the repairs remain operationally incompatible across failures, the runtime branch requirement does not fall.

Therefore two distinct improvements must never be collapsed:

```text
implementation compression
= Lambda(m) decreases at fixed m

online-discrimination compression
= nu(ell) decreases under a larger static budget.
```

The first does not imply the second.

---

## 6. Canonical implementation regimes

### Independent branches

When routing and repair branches contain little or no reusable structure:

```text
Lambda(m)
approx
C_H(r) + sum_j C_H(pi_j)
```

up to ordinary encoding/permutation overhead.

### Parameterized / shared branches

When branches are generated by a common bounded template:

```text
Lambda(m)
lesssim
C_H(r) + C_H(S) + O(1).
```

The number of behaviors can grow while the static generator remains compact.

### Arbitrary lookup

For a generic unique repair map:

```text
f : [N] -> [R],
```

counting yields typical/worst-case implementation burden:

```text
C_H(f) = Theta(N log R)
```

when the bounded implementation model permits an explicit table and no reusable structure is present.

These regimes are implementation-complexity regimes, not distinct computational complexity classes.

---

## 7. Literature-level reduction status

The broad reduction check supports the following claim ceiling:

```text
unconstrained selector synthesis
= established Boolean relation / functional synthesis territory

minimization over compatible selector implementations
= established Boolean relation minimization / Skolem implementation territory

shared substructure in a fixed implementation
= established circuit sharing / functional decomposition territory

interactive bounded repair policies
= closer to reactive/controller synthesis territory
```

No standard named quantity was identified here for the exact specialization:

```text
min_{f models R_O, |range(f)| <= m} C_H(f).
```

This absence is **not evidence of novelty**.

Current responsible statement:

> **Unconstrained synthesis is established; the global range-budget coupling remains an identifiable specialization whose novelty is unestablished.**

---

## 8. Decision problem: RANGE-BOUNDED-SYNTH

A clean decision form is:

```text
RANGE-BOUNDED-SYNTH

Input:
  relation R(z,pi),
  implementation model C_H,
  branch budget m,
  static implementation budget ell.

Question:
  does there exist selector f such that

    R(z,f(z)) for every z,
    |range(f)| <= m,
    C_H(f) <= ell ?
```

This explicitly separates:

```text
m = unbounded
-> ordinary relation-constrained synthesis

ell = unbounded
-> evidence-realizable repair-cover cardinality

m, ell finite
-> coupled bicriteria problem.
```

---

## 9. Explicit relation encoding

Suppose the relation is given explicitly as a finite incidence table.

Ignoring or making nonbinding the implementation bound, a selector of range at most `m` exists iff at most `m` repair validity sets cover every evidence row.

Therefore the feasibility problem is exactly Set Cover / hypergraph cover:

```text
EXPLICIT-RANGE-SYNTH
= NP-complete.
```

With a polynomially represented selector circuit and an implementation bound `ell` that can be checked against the explicit table:

```text
EXPLICIT-RANGE-BOUNDED-SYNTH
in NP,
```

and it remains NP-hard because the implementation bound can be chosen nonbinding in the Set-Cover reduction.

Hence, under this conventional explicit encoding:

```text
EXPLICIT-RANGE-BOUNDED-SYNTH
= NP-complete.
```

The exact encoding assumptions remain part of the theorem statement.

---

## 10. Succinct Boolean relation encoding

Let the relation be represented succinctly by a Boolean circuit/formula:

```text
R(z,y).
```

Let the selector be a polynomially encoded circuit of size at most `ell`, and let `m`/output width be encoded so that the witness remains polynomial size.

The decision condition is:

```text
exists selector f and range representatives y_1,...,y_m
such that
for every z:

  R(z,f(z))
  and
  f(z) in {y_1,...,y_m}.
```

This has the quantifier form:

```text
exists witness
forall z
polynomial-time predicate,
```

so:

```text
SUCCINCT-RANGE-BOUNDED-SYNTH
in Sigma_2^P.
```

Hardness already holds for `m=1` by reduction from an existential-universal QBF:

```text
exists u forall z phi(u,z).
```

Set:

```text
R(z,y) = phi(y,z),
m = 1.
```

A range-one selector is constant, so a valid selector exists exactly when some `u` satisfies `phi(u,z)` for every `z`.

Thus, under the stated succinct encoding:

```text
SUCCINCT-RANGE-BOUNDED-SYNTH
= Sigma_2^P-complete,
```

with hardness already at `m=1`.

This does **not** establish a new complexity class for the range constraint. Classical succinct synthesis already occupies second-level polynomial-hierarchy territory.

---

## 11. Coarse complexity question is exhausted for current purposes

The current reduction is:

```text
explicit relation
-> NP / Set-Cover territory

succinct relation
-> Sigma_2^P / synthesis territory.
```

Therefore the range constraint does not earn novelty merely from worst-case decision complexity.

The surviving mathematical object is the bicriteria Pareto frontier:

```text
(m, ell)
=
(number of distinct runtime repair behaviors,
 static implementation complexity).
```

Equivalent representations:

```text
Lambda(m)
= minimum static implementation complexity at range budget m

nu(ell)
= minimum range achievable at static budget ell.
```

---

## 12. Permanent three-way anti-collapse

The mathematical branch must permanently distinguish:

```text
semantic feasibility
!=
minimum implementation size
!=
difficulty of finding / synthesizing the implementation.
```

More explicitly:

```text
FEASIBILITY
Does any valid selector exist?

MINIMUM IMPLEMENTATION SIZE
How small can a valid selector be under the chosen implementation model?

SYNTHESIS / SEARCH COMPLEXITY
How much computation is required to discover or output such a selector?
```

A compact valid controller may exist while being computationally difficult to discover.

Conversely, an easy synthesis method may return a selector far from minimum size.

No theorem should substitute one of these claims for another.

---

## 13. Bicriteria frontier is the surviving theory seam

Current target:

```text
Characterize the Pareto frontier over

  m   = runtime repair-behavior count
  ell = static implementation complexity.
```

Structural phenomena of interest:

```text
flat regions
= additional static complexity buys no branch reduction

thresholds
= a newly expressible shared repair or controller collapses branch count

no-exchange floors
= incompatible repair requirements impose m >= M for all static budgets

implementation compression
= Lambda(m) falls without reducing m

composition
= product-system assumptions may yield subadditivity of log m

approximation
= epsilon enlarges validity hyperedges and may move both tau^O and Lambda(m).
```

No universal convexity or smooth scaling law is currently claimed.

---

## 14. Next theorem class: structural scaling laws

The next mathematical burden is not another complexity-class label.

The target is:

> **Under explicit structural conditions on the evidence-quotiented repair relation, derive scaling laws or threshold bounds for `Lambda(m)` and therefore for `nu(ell)`.**

Examples of acceptable theorem forms include:

```text
Lambda(m) = Theta(g(m))
```

for a prospectively defined family, or explicit threshold locations:

```text
ell < ell_1  -> nu(ell) >= m_1
ell >= ell_1 -> nu(ell) <= m_2
```

with the drop explained by a concrete change in jointly realizable repair structure.

The theorem must preserve the distinction between:

```text
shared implementation structure
and
actual repair overlap.
```

---

## 15. Relation to the broader program

This mathematical line is deliberately downstream of, and separate from, the empirical BL program.

Repository interpretation remains:

```text
science
-> program synthesis
-> adaptive-control reduction
-> correction-complexity formalization
-> static/online RFP
-> range-constrained synthesis frontier.
```

The empirical claims remain unchanged:

```text
BL-001    = POSITIVE
BL-002    = POSITIVE
BL×CC-001 = POSITIVE / AUDITED / PARKED
```

The current interpretation of BL×CC-001 remains:

```text
evidence for controllable corrective feedback
!=
evidence for a distinct CC mechanism.
```

No result in this document is new empirical evidence for CC, CRCB, BL-003, acquisition/retention corrigibility, or meta-authority closure.

---

## 16. Current mathematical status

```text
chi <= tau <= tau^O <= nu(ell)
                              = ACTIVE RELAXATION HIERARCHY

tau^O
                              = EXACT EVIDENCE-QUOTIENT COVER IN FINITE DETERMINISTIC SETTING

Lambda^O_{epsilon,H}(m)
                              = RANGE-CONSTRAINED MINIMUM IMPLEMENTATION SPECTRUM

nu_{epsilon,H}(ell)
                              = THRESHOLD INVERSE OF Lambda(m)

fixed-selector joint complexity
                              = REDUCED TO RESOURCE-BOUNDED PROGRAM/CIRCUIT COMPLEXITY

unconstrained relation synthesis
                              = ESTABLISHED

explicit range-bounded decision problem
                              = NP-COMPLETE UNDER STATED ENCODING

succinct range-bounded decision problem
                              = SIGMA_2^P-COMPLETE UNDER STATED ENCODING

range/implementation bicriteria frontier
                              = SURVIVING RESEARCH SEAM

RFP as new foundational complexity theory
                              = NOT ESTABLISHED

CC-specific irreducibility
                              = UNESTABLISHED

H_CRCB
                              = OPEN

BL-003
                              = UNOPENED

NEW ASSAY
                              = NONE
```

---

## 17. Next-action discipline

No assay is opened by this freeze.

Do not move the empirical program by default.

The next mathematical task is:

```text
derive structural bicriteria theorems for Lambda(m) / nu(ell),
not another scalar definition and not another coarse complexity-class result.
```

The standing novelty discipline is:

> **Anything already explained by set cover, Boolean relation synthesis, circuit sharing, MDL, information theory, or standard resource-bounded complexity should be reduced to that theory rather than renamed.**

The surviving question is deliberately narrow:

> **When does a semantic repair relation admit a jointly compact selector at a restricted behavioral range, and how does that minimum implementation cost scale as the allowed range changes?**
