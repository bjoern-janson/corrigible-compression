# Corrigible Memory and Provenance

This document applies the corrigible-compression heuristic recursively to research memory itself.

## Core rule

> **Compress conclusions. Compress provenance without destroying its corrective affordances. Keep correction paths open.**

The shorter earlier form — “Compress conclusions. Preserve provenance. Keep correction paths open.” — is directionally correct but too literal if read as a demand for full trace preservation.

Full provenance grows without a natural size cap. Under finite memory, provenance must itself be compressed.

Therefore:

```text
provenance itself is a bounded compression problem
```

## Provenance content versus provenance access

A bounded system need not keep an entire derivation in active memory if it preserves a reliable route back to the underlying evidence.

Hence:

```text
provenance content != provenance access
traceability       != full trace preservation
```

A rewrite is not a diff. A summary can preserve the present conclusion while destroying the path by which that conclusion became justified.

That path can matter because a future contradiction may need to know:

- which premise was load-bearing;
- which objection forced a revision;
- why that objection was judged resolved;
- what evidence originally supported the claim;
- where the source record lives;
- what would reopen the claim.

## Minimal corrigible-memory record

A useful compact schema is:

```text
M_t = (
    claim,
    support,
    load-bearing objection,
    resolution,
    source pointer,
    reopen trigger
)
```

The purpose is not historical completeness. The purpose is to preserve enough structure that future evidence can travel back from a compressed conclusion to the evidence or assumption that must be reconsidered.

A good compressed memory therefore looks like:

```text
short active summary
+ reliable provenance pointers
+ reopen triggers
```

not:

```text
short summary = truth
```

## Why objections matter

A final conclusion is not informationally equivalent to the same conclusion plus the objection that forced it.

```text
final conclusion
!=
final conclusion + load-bearing objection + resolution
```

The second form preserves information about why the conclusion is currently trusted and where it is vulnerable.

Therefore a high-value provenance trace often includes **the objection that changed the formulation**, not every intermediate wording change.

This is compressed provenance: preserve revision-relevant history, not chronology for its own sake.

## Reopenability criterion for memory

Let a provenance history be `P_{1:t}` and let:

```text
Gamma(P_{1:t}) = P_tilde_t
```

be a bounded memory compression.

The target is not:

```text
P_tilde_t = P_{1:t}
```

but approximately:

> `P_tilde_t` retains enough structure that a relevant future contradiction can reopen the associated claim and recover or re-interrogate its support.

If the original source remains externally recoverable, the active summary may be small.

If the underlying source is destroyed or inaccessible, the compressed record must retain more content because the correction route has narrowed.

## Recursive geometry

The recursion is over the **constraint geometry**, not over identical mechanism:

```text
bounded representation
-> compression
-> possible consequential omission
-> surviving correction route
```

At different levels:

| Level | Typical compressed object | Typical correction route |
|---|---|---|
| world/model | state distinctions | new observation / challenge / model revision |
| reasoning | hypotheses and alternatives | contradiction / re-analysis |
| memory | provenance and history | source pointer / reopen trigger |
| institution | audit and authority paths | independent review / escalation / correction |

This preserves the standing rule:

```text
same geometry != same mechanism
```

## What not to preserve

The principle does not demand preservation of every intermediate thought, every draft, or every discarded hypothesis.

That would defeat boundedness.

The stronger design question is:

> **Would losing this item destroy or materially weaken a future route for discovering that the current compressed conclusion is wrong?**

If no, it is a candidate for omission.

If yes, preserve either the item itself or a reliable pointer/reopen condition that keeps the correction route viable.

## Standing caveat

“Worth preserving” is itself a bounded judgment.

The memory system cannot know every future challenge in advance. Therefore it must not self-certify completeness merely because the retained summary appears coherent.

The safe posture is:

```text
compress aggressively where warranted
+ retain independent ways for consequential contradiction to reopen the record
```

The recursive endpoint is:

> **Corrigible compression means that even the compression process itself remains correctable.**
