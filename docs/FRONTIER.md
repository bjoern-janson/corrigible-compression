# Current Frontier

This document records the live questions that follow from the current freeze. These are **not** yet repository claims unless explicitly marked otherwise.

## 1. Typed corrective-reach graph

The strongest candidate mathematical abstraction is not a single corrigibility score but a typed corrective-reach graph.

Candidate scaffold:

```text
G_t^corr = (V, E, tau, c)
```

where nodes/edges retain semantic types such as:

```text
F, D/H, I, W, U, Pi
```

and capacities `c_e` represent admissible notions of effective reach.

Possible failure mappings:

```text
interface aliasing          -> D/H -> I degradation
authority starvation        -> I   -> W degradation
ineffective authority       -> W   -> U degradation
epistemic foreclosure       -> future path deletion
adversarial source control  -> F degradation
```

This graph is a **candidate formal refinement only**. Do not freeze it as a universal pipeline or ontology until evidence requires the additional structure.

BL×CC-001 now gives one direct synthetic intervention witness on the `W -> U` distinction, but a single local witness does not validate the entire graph or establish the typed sequence as a universal architecture.

## 2. Protected source versus protected ingress

The current source condition is:

```text
Reach_pi(Z_t) = 0
AND
H_min(Z_t | E_t^kappa) > 0
```

This protects the source relative to the threat model, but may not protect the entire ingress channel.

A learner could potentially manipulate:

- which source samples are admitted;
- timing;
- censoring;
- transduction or measurement;
- routing;
- interpretation;
- aggregation;
- the map from evidence to authority.

Therefore the following distinction remains open and important:

```text
protected source != protected ingress channel
```

A future formulation may need an explicit measurement/ingress map, for example:

```text
Z_t -> M_t -> E_t -> I_t -> W_{t+1}
```

where source independence does not imply that `M_t` is learner-independent.

This is structurally related to recursive challenge failure: reality may be outside the learner's control while its route into the learner still passes through assumptions shared with the current interface.

## 3. Temporal survivability

The deepest unresolved requirement is temporal.

Pointwise corrigibility is insufficient if the learner's own development can destroy the route later.

The open question is not only:

```text
Does a corrective path exist at time t?
```

but:

> **Does the corrective path remain viable under the learner's own future updates, optimization pressure, resource use, and interface changes?**

A system may satisfy:

```text
Z_t -> Pi_{t+1}
```

while later producing:

```text
Reach_correction(t+n) -> 0
```

without an explicit anti-corrigibility objective.

BL×CC-001 established a finite-horizon witness in which preserving one matched consequence `W_corr -> U_corr` route improved sustained escape from a wrong but repairable allocation regime. It does **not** establish long-horizon corrective-path survivability under self-modification or changing architecture.

This motivates a future object like **corrective-path survivability** or a path-capacity process over time, but no specific formalism is yet frozen.

## 4. Identification gate

The standing anti-collapse rule is:

```text
D/H != I
```

Fresh evidence, successful detection, or a valid challenge does not automatically identify the dimension along which authority may legitimately change.

The older governing constraint remains relevant:

> **Evidence may increase authority only along the dimensions it can identify.**

A future architecture may therefore require an explicit identification gate before authority transfer.

Failure mode to preserve:

```text
fresh + detected + causally effective
but mislocalized
=> unjustified revision
```

Do not treat freshness as epistemic warrant by itself.

BL×CC-001 held identification fixed and matched across A/B before the `W -> U` intervention. It therefore does not answer how identification should be constructed when the relevant distinction is ambiguous or absent from the current representation.

## 5. Authority versus realized influence

The standing anti-collapse rule is:

```text
W != U
```

AA-002 established an existential toy separation: equal cumulative authority need not imply equal realized developmental influence or recovery.

BL×CC-001 now adds a prospective intervention witness on that distinction. In the frozen symmetric supplied-family assay, A/B science pairs were identical through matched `W_corr`; allowing versus cutting only `W_corr -> U_corr` changed first sustained two-round correct allocation:

```text
A = 0.61083984375
B = 0.51464843750
Delta_esc = +0.09619140625
one-sided exact McNemar p = 1.8858785303612578e-97
```

The direction was positive in both mirror worlds.

Earned local compression:

```text
warranted corrective evidence
-> developmental influence
-> increased sustained escape
```

under endogenous epistemic allocation.

This does **not** establish a universal `W -> U` mechanism, nor does it imply that every authority/influence distinction should be modeled with the same gate. Any future graph or metric must preserve the distinction without overgeneralizing the specimen.

The secondary BL×CC controls are mechanistic diagnostics only:

```text
C-D = +0.056884765625
B-D = -0.0665283203125
(A-B)-(C-D) = +0.039306640625
```

Do not promote the interaction to a standalone confirmed mechanism without a prospectively frozen assay for that question.

## 6. BL-003 — topology invention remains unopened

The broad-learning ladder now has:

```text
BL-001 = POSITIVE — TOPOLOGY UTILIZATION
BL-002 = POSITIVE — ACTIVE SURVEYING
BL×CC-001 = POSITIVE — CORRECTIVE INFLUENCE ADDS SUSTAINED ESCAPE
BL-003 = QUESTION EARNED — UNDESIGNED
```

The load-bearing boundary for all three completed assays remains:

```text
T* in H
```

Therefore topology invention remains open.

BL-003 question:

> **Can the learner construct useful relational structure that was not already supplied by the candidate topology family?**

Equivalently:

```text
Can representational capacity expand?
```

This is distinct from BL×CC-001:

```text
BL×CC-001:
Can the learner escape a wrong representation that still contains the truth?

BL-003:
Can the learner expand what it can represent when the needed structure is absent?
```

No BL-003 world, policy, representation, endpoint, or executable is currently frozen.

## 7. Acquisition × retention corrigibility

A separate frontier emerged while designing BL×CC-001:

```text
architecture
-> acquisition
-> retention
-> representation
-> authority
-> influence
```

Three failure depths must remain distinct:

```text
policy blindness:
current model says "do not look there"

retention blindness:
current model says "do not keep that"

embodiment blindness:
there is no available way to look there
```

Two model-independent stochastic protections have different jobs:

```text
undirected acquisition
-> protects reachable observations from model-driven screening

undirected retention
-> protects acquired observations from model-driven deletion
```

Neither substitutes for the other:

```text
acquisition openness != retention openness
```

and neither can repair a missing architectural channel.

Durable boundary:

> **Randomness can protect against endogenous selection; it cannot create an observation or intervention channel that the architecture does not possess.**

Open question:

> **Can a bounded learner preserve access to consequential evidence that is invisible to its current model, at both the acquisition and retention stages?**

Status:

```text
ACQUISITION×RETENTION CORRIGIBILITY = QUESTION EARNED — NO ASSAY
```

Do not treat BL×CC-001 as evidence for this question. Its true topology remained representable and its corrective channels were explicitly available in the architecture.

## 8. Reopenability under boundedness

A central candidate question is:

> **Which distinctions and causal paths must survive bounded compression so that consequential reality can still force revision later?**

The challenge is that “which distinctions will matter later” is not known in advance.

Therefore the target is not perfect preservation. It is maintenance of admissible routes by which future consequence can expose that a compression omitted something important.

Candidate relative objects remain:

```text
R(Pi; C, H, B, T)
C_reopen(delta)
```

Neither is yet validated as a general measure.

BL×CC-001 provides one finite synthetic witness that preserving a particular corrective influence route can improve bounded-horizon recovery. It does not validate either candidate general quantity.

## 9. Real-XM replication target

The matched real-XM `K in {1,2,5,8,12}` surface produced a negative result for gross/monotonic marginal authority topology but raised a narrower open signal at high `K`: regional authority/competence coupling.

The clean next empirical knife is fresh-seed replication with:

```text
K = 2   low-pressure anchor
K = 8   candidate emergence regime
K = 12  candidate emergence regime
```

Same frozen 16 regions, same observer, same holdout construction, same data specimen and schedule unless a new freeze explicitly says otherwise.

Fresh training seed is the replication unit.

Primary question:

> **At high K, do small regional deviations in winner authority reproducibly associate with conditional competence while low-K remains near null and gross marginal authority remains consistent with the finite-count calibration?**

Causal direction remains open. At least three structures must remain live:

```text
competence -> winner allocation
winner allocation -> competence
stable latent difficulty -> both
```

Replication can establish reproducibility, not causal direction.

## 10. What would force theory revision

The meta-hypothesis should be weakened or discarded if retrospective or prospective evidence shows that:

1. the proposed corrective-reach compression only works by erasing mechanism distinctions;
2. the typed non-identities repeatedly prove unnecessary or misleading;
3. systems with apparently destroyed correction routes remain robust for reasons the framework cannot represent without ad hoc relabeling;
4. proposed reopenability measures fail to predict recovery/robustness beyond simpler existing quantities;
5. “corrigible compression” becomes merely a vocabulary for redescribing any adaptive process after the fact;
6. BL×CC-style positive results fail to replicate under close but prospectively frozen changes that preserve the claimed mechanism.

The central falsification discipline is:

```text
better verbal compression
+ mechanism collapse
=> meta-hypothesis too coarse
```

## 11. What not to do next

Until new evidence forces otherwise:

- do not promote the typed graph to a primitive;
- do not invent a universal scalar corrigibility score;
- do not reinterpret hard regions as starved without direct authority evidence;
- do not treat protected freshness as sufficient for correction;
- do not convert fresh-seed replication into a causal claim;
- do not modify the real-XM observer merely to make the high-K signal easier to see;
- do not promote the BL×CC secondary interaction to a primary mechanism claim;
- do not treat BL×CC-001 as topology invention;
- do not treat BL×CC-001 as evidence for acquisition×retention or architecture-level blindness repair;
- do not erase the post-run audit-comparator correction from BL×CC provenance;
- do not let theory outrun the ledger.

The research posture remains:

```text
freeze -> execute -> audit -> narrow claim -> local revision
```
