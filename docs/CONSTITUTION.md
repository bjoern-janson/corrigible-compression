# Corrigible Compression — Frozen Constitution

Status: **provisional meta-hypothesis**.

This document records the current conceptual freeze. It is not an OpenCore primitive, theorem, universal mechanism, or empirical validation claim.

## Core formulation

> **Corrigibility is not the absence of loss. It is the preservation of effective routes by which consequential loss can still be discovered and revised.**

Equivalent design heuristic:

> **Do not preserve everything. Preserve the distinctions, evidence routes, and causal pathways whose future loss would make warranted correction impossible or too late.**

Shortest operational seed:

> **Compress conclusions. Compress provenance without destroying its corrective affordances. Keep correction paths open.**

The standing scope clause is mandatory: claims are relative to **bounded resources, a stated consequence class, a stated horizon, and a stated threat model**.

## Meta-hypothesis

A bounded adaptive system must compress state, history, hypotheses, candidates, authority routes, compute, and time. Compression itself is not failure.

The candidate meta-hypothesis is that robust bounded intelligence depends partly on preserving **effective corrective causal reach**: routes by which consequential discrepancies can still alter future system state.

The current retrospective status is:

- **topological unification:** provisionally supported;
- **mechanism unification:** rejected;
- **universal mechanism:** unsupported;
- **general theorem:** unsupported.

The recurring pattern is:

```text
same high-level loss geometry
+ different mechanisms
+ explicit non-identities
```

Do not infer shared mechanism merely from shared corrective-path geometry.

## Compression versus closure

For a representation `Pi`, ordinary compression can collapse distinctions:

```text
Pi(s_a) = Pi(s_b)
```

That alone is not epistemic closure.

The dangerous case is loss of corrective reach: a consequentially relevant distinction is absent and no admissible surviving route can cause its consequences to regain enough authority to revise the representation within the relevant budget and horizon.

A useful relative object is therefore:

```text
R(Pi; C, H, B, T)
```

where:

- `C` = consequence/discrepancy class;
- `H` = admissible challenge channels;
- `B` = resource/information/compute budget;
- `T` = time horizon.

A corresponding cost object is:

```text
C_reopen(delta)
= minimum resources required for delta to regain corrective authority.
```

These are candidate measurable objects, not yet universal formal definitions.

## Typed corrective reach

The evidence does not support one untyped scalar called “corrective signal.” At minimum, the following non-identities are load-bearing:

```text
D/H != I
W   != U
```

where:

- `D/H` = detection / challenge;
- `I` = identification of the distinction or dimension that warrants revision;
- `W` = authority / authorization;
- `U` = realized developmental influence.

Thus:

```text
detection or challenge != identification
allocated authority      != realized influence
```

These constraints prevent two known collapses:

1. evidence can arrive without identifying the warranted representational change;
2. authority can be allocated without producing equivalent developmental influence.

A candidate typed scaffold for future falsification is:

```text
Z_t -> D/H -> I -> W -> U -> Pi_{t+1}
```

This is **not frozen as a literal universal pipeline**. Different systems may not instantiate these stages as modules, and causal order/mechanism may differ. The types are retained because collapsing them would erase distinctions already earned by prior evidence.

## Protected freshness

For an authority-bearing source `Z_t`, define relative to threat model `pi`:

```text
FreshProtected(Z_t) :=
    Reach_pi(Z_t) = 0
    AND
    H_min(Z_t | E_t^kappa) > 0
```

Interpretation:

1. **causal separation** — the learner cannot influence the source under the declared threat model;
2. **informational freshness** — before the event, the learner cannot fully predict it from all admissibly accessible side information.

These are independent requirements:

```text
causal separation != informational freshness
```

`E_t^kappa` must contain the full side information the adversary is allowed to access, including permitted quantum side information where relevant. Freshness may not be manufactured by leaving known information outside `E` by definition.

Increasing `kappa` means **more computation inside the same physical information boundary**. New sensors, actuators, covert channels, privileged variables, or other physical access constitute a threat-model change:

```text
pi -> pi'
```

not merely `kappa -> larger kappa`.

The engineering claim is adversary-relative and does not require a metaphysical claim that `Z_t` is ontologically indeterministic.

## Protected freshness is not corrigibility

A perfectly protected fresh source that never influences the learner has zero corrective power.

Therefore a candidate future-resistant corrective channel also needs a downstream route such as:

```text
Z_t -> Delta W_{t+1} -> Delta U_{t+1} -> Delta Pi_{t+1}
```

with identification inserted wherever warranted by the task.

The two compressed failure modes are:

> **freshness without reach is inert; reach without protected freshness is gameable.**

So the architectural floor is:

```text
protected freshness
+ effective downstream authority/influence path
= candidate future-resistant corrective channel
```

Again, this is an architectural condition, not a claim that all systems implement the same mechanism.

## Recursive form

Corrigible compression applies recursively to the **constraint geometry**, not necessarily to the mechanism.

At multiple levels:

```text
bounded representation
-> compression
-> possible consequential loss
-> need for a surviving correction route
```

Examples:

- world/model: state distinctions;
- reasoning: hypotheses and alternatives;
- memory: provenance and revision history;
- institutions: audit and authority pathways.

The recursive statement is:

> **Corrigible compression means that even the compression process itself remains correctable.**

Or more tightly:

> **Loss is acceptable; loss that destroys the routes for correcting the loss is not.**

The word “acceptable” is always relative to the stated consequence class, budget, horizon, and threat model.

## Standing caveat

“Worth preserving” is itself a bounded judgment.

A bounded system cannot know in advance every distinction future reality will make consequential. Therefore the design objective is not to retain exactly the right information. It is to avoid unnecessarily destroying all admissible routes by which future consequential evidence could reveal that the compression became insufficient.

The system does not get to certify its own compression as sufficient merely because the compressed representation says so.
