# DES Payoff Audit — Synthesis Payoff Without Intrinsic Frontier Gain

Status: **PARKED LITERATURE-TRANSLATION AUDIT**

This note records a targeted payoff hunt against an independently motivated repair/control-synthesis family: scalable supervisory control of repeated-agent discrete-event systems (DES). It is a mathematical/literature translation layer only. It does not modify the empirical record, does not open BL-003, and does not claim a CC-specific mechanism.

## Executive result

The DES lane earns a real positive result on **construction/synthesis effort** and compact control-equivalent implementations, but it does **not** establish a strict improvement in the intrinsic range/implementation frontier

```text
Lambda^O(m)
= minimum implementation complexity among all valid selectors/controllers
  with at most m runtime behavioral classes.
```

The decisive inclusion is:

```text
A_template subseteq A_raw
=> Lambda_raw(m) <= Lambda_template(m).
```

If a template/relabeling method constructs a compact ordinary supervisor over the original plant alphabet, that supervisor is already a feasible point in the unrestricted raw architecture class. The template construction therefore cannot beat the unrestricted optimum on the same validity criterion and implementation measure merely by virtue of being found through a quotient.

The demonstrated payoff is instead:

```text
symmetry/template quotient
-> agent-count-independent synthesis/construction
-> compact control-equivalent implementation
```

not:

```text
strict intrinsic Lambda(m) improvement.
```

This is a useful negative result because it preserves the standing firewall:

```text
valid implementation exists
!= minimum implementation size
!= difficulty of finding / synthesizing the implementation.
```

## Candidate family

Primary literature family:

- scalable supervisory control of multi-agent discrete-event systems with repeated/isomorphic agents;
- relabeling of agent-specific events into template events;
- synthesis on fixed template structures;
- inverse relabeling / localization back to concrete agents.

The family is natural independently of this repository: repeated machines, robots, vehicles, and other interchangeable agents arise directly in supervisory-control applications.

The targeted transfer-line example uses repeated agent groups connected through shared buffers. In that example, the scalable supervisor is reported to reproduce the monolithic controlled marked behavior under the paper's stated sufficient condition, so the translation audit can use one common control-validity criterion rather than comparing optimal monolithic control against merely admissible scalable control.

## Frozen translation quantities

For a supervisor `S`, do not identify runtime branch complexity with raw state count.

### Implementation size

A first literature-facing proxy is

```text
ell_Q(S) = |Q_S|
```

because the scalable DES literature directly reports supervisor state counts and agent-count-independent state-size scaling.

For a stricter explicit automaton encoding, use something like

```text
ell_enc(S) = |Q_S| + |delta_S|
```

or another prospectively frozen complete code-size measure.

Important boundary:

```text
|Q_S| = O(1)
!=
ell_enc(S) = O(1).
```

Inverse relabeling can replace one template transition by many concrete agent-specific event transitions. A constant-state supervisor can therefore have a growing explicit transition table. Symbolic grouped labels can compress those transitions, but then the symbolic label language and relabeling map are part of the implementation representation and must be charged consistently.

### Runtime behavioral classes

Let `chi(q)` denote the future-relevant control decision associated with supervisor state `q`. A minimal local version is the set of controllable events disabled at that state:

```text
chi(q) = { controllable events disabled at q }.
```

If the frozen recovery/control semantics require more than the immediate disable set, augment `chi` prospectively with exactly that future-relevant behavior.

Define

```text
m(S) = | { chi(q) : q in Q_S } |.
```

Thus

```text
m(S) != |Q_S|
```

in general.

This prevents a large-state supervisor with only a few distinct runtime control decisions from being falsely credited with large `m`.

## Artifact-level DES observations

The scalable/local-controller construction already supplies a concrete state-versus-behavior separation.

For the reported transfer-line local controllers, each local controller is associated with one controllable event and its reachable states divide into only two immediate control signatures for that event: enable versus disable. The reported local-controller state counts are larger than two.

The relevant qualitative result is therefore:

```text
implementation states
!=
runtime control-decision classes.
```

A system-level `m(SUP)` or `m(SSUP)` cannot be recovered from state counts alone. It requires the reachable global control signature at every supervisor state, or an equivalent machine-readable automaton/control map.

## What the literature demonstrably pays for

Under fixed group/template parameters, the scalable construction synthesizes on template structures whose state size and synthesis computation do not grow with the number of repeated agents in the way the conventional monolithic construction does.

This supports a genuine statement about construction/synthesis resources:

```text
C_synth(template method)
<<
C_synth(conventional monolithic construction)
```

for the repeated-agent scaling family under the paper's assumptions.

It also produces compact control-equivalent supervisors/local controllers in the reported examples.

This is a real external payoff for contextual symmetry/relabeling.

## What it does NOT establish

### 1. No intrinsic frontier improvement from nested architecture classes

If

```text
A_template subseteq A_raw,
```

then by minimization over a superset,

```text
Lambda_raw(m) <= Lambda_template(m)
```

for every common branch budget `m` and common validity/cost definition.

Therefore the desired claim

```text
exists m:
Lambda_template(m) < Lambda_raw(m)
```

cannot hold under that natural unrestricted interpretation.

The quotient method may discover a good point in the raw feasible set much more efficiently; it does not lower the mathematical minimum merely because the point was discovered through a quotient.

### 2. Standard synthesized supervisor size is not Lambda

A conventional monolithic synthesis procedure can output a very large supervisor even when a much smaller control-equivalent supervisor exists.

Therefore

```text
size(standard synthesized SUP)
!=
minimum valid implementation size.
```

State/synthesis scalability of one construction is not a lower bound on `Lambda_raw(m)`.

### 3. Compact state count is not compact full encoding

State-size independence does not by itself establish constant explicit transition/code size after inverse relabeling.

### 4. Produced-artifact measurements are not intrinsic optima

Measurements such as

```text
m_mono(n), ell_mono(n)
m_tmpl(n), ell_tmpl(n)
m_red(n),  ell_red(n)
```

are measurements of produced artifacts unless lower bounds or architecture restrictions establish that they equal the corresponding intrinsic minima.

Do not relabel artifact measurements as `Lambda` estimates without that additional argument.

## 2026 relabeling-observation-consistency boundary

The later relabeling-observation-consistency (ROC) work is useful as an **effectivity boundary** for the broader partial-observation DES family.

The relevant lesson is:

```text
useful quotient
!=
automatically cheap quotient validation.
```

General ROC verification is reported PSPACE-complete, while polynomial-time subclasses and composition results are available under explicit structural conditions.

This belongs with the contextual-quotient distinction:

```text
small/useful quotient
!=
effective quotient.
```

It is not retroactive evidence that every full-observation transfer-line quotient is difficult to validate.

## DES payoff ledger

```text
NATURAL INDEPENDENTLY MOTIVATED FAMILY  = YES
SYMMETRY / TEMPLATE QUOTIENT            = YES
COMMON CONTROL-VALIDITY COMPARISON       = YES ON TARGET TRANSFER-LINE CASE
AGENT-COUNT-INDEPENDENT SYNTHESIS        = YES UNDER STATED CONDITIONS
COMPACT CONTROL-EQUIVALENT IMPLEMENTATION= YES / LITERATURE-DEMONSTRATED
m != STATE COUNT WITNESS                 = YES
FULL EXPLICIT ell = O(1)                 = NOT ESTABLISHED
SYSTEM-LEVEL m FOR SUP/SSUP              = NOT YET RECOVERED
STRICT INTRINSIC Lambda(m) IMPROVEMENT   = NOT DEMONSTRATED
TEMPLATE BEATS UNRESTRICTED Lambda       = FALSE UNDER NESTED-CLASS READING
REAL SYNTHESIS / CONSTRUCTION PAYOFF     = YES
CONTEXTUAL-QUOTIENT THEORY PROMOTED      = NO
BL-003                                   = UNOPENED
NEW ASSAY                                = NONE
```

## Only worthwhile continuation

The DES lane is parked unless machine-readable artifacts are obtained or reconstructed for one existing instance.

A disciplined continuation would be:

```text
SUP / SSUP / SLOC automata
-> compute actual global control signatures m
-> freeze and compute explicit encoding ell_enc
-> measure synthesis/construction cost C_synth
-> report produced-artifact points only.
```

These quantities must remain artifact measurements unless matching lower bounds or explicitly restricted architecture classes justify an intrinsic frontier claim.

No new theoretical axis is introduced merely because DES exposes synthesis cost. The existing distinction between minimum implementation size and difficulty of finding that implementation is sufficient.

## Cross-program symmetry

The DES audit mirrors an existing program discipline:

```text
BL / CC branch
positive causal edge
-> generic adaptive-control reduction
-> no CC-specific residual identified

DES payoff branch
positive synthesis/scaling edge
-> unrestricted-controller inclusion reduction
-> no intrinsic Lambda-frontier residual identified
```

The shared rule is:

> **Observed improvement does not establish an irreducible mechanism or intrinsic optimum gap.**

## Claim ceiling

The DES payoff hunt may currently claim:

> In an established repeated-agent supervisory-control family, template/relabeling quotienting can substantially reduce synthesis/construction burden and yield compact control-equivalent implementations under stated conditions.

It may not currently claim:

- a strict improvement in the unrestricted intrinsic `Lambda(m)` frontier;
- that state count equals runtime repair/control behavior count;
- that constant supervisor state count implies constant full encoded implementation size;
- that produced monolithic/template/reduced supervisors are minimum-size solutions;
- a new repair-complexity primitive;
- a CC-specific mechanism;
- evidence for BL-003.

## Research state after audit

```text
EMPIRICAL PROGRAM             = PARKED
BLxCC-001                     = POSITIVE / AUDITED / PARKED
BL-003                        = UNOPENED
CONTEXTUAL-QUOTIENT BRANCH    = PARKED
DES PAYOFF HUNT               = REAL SYNTHESIS PAYOFF / STRICT RFP PAYOFF NOT EARNED
CC-SPECIFIC IRREDUCIBILITY    = UNESTABLISHED
NEW ASSAY                     = NONE
```

The next program-level demand remains:

> **Do not invent another abstraction. Find a setting where an existing one makes a falsifiable prediction or yields a payoff not already supplied by ordinary theory.**

## Literature pointers used in the translation audit

- scalable supervisory control of multi-agent discrete-event systems using relabeling/template structures (2019);
- supervisor reduction for discrete-event systems and control-equivalent supervisor minimization/reduction literature;
- deciding relabeling observation consistency in multi-agent discrete-event systems (arXiv:2608.18866, 2026).

These are external theoretical/literature sources, not new experiments in this repository.
