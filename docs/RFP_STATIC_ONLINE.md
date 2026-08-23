# Repair-Factorization Profile — Static/Online Frontier

Status:

```text
MATHEMATICAL CONTINUATION = CONCEPTUAL / NO NEW EMPIRICAL RESULT
RFP                         = COUPLED PROFILE CANDIDATE
NU_{eps,H}(ell)             = CENTRAL STATIC/ONLINE FRONTIER CANDIDATE
B*_{eps,H}(ell)             = ceil(log2 NU_{eps,H}(ell))
PAIRWISE OVERLAP GRAPH      = USEFUL LOWER-BOUND OBJECT, NOT GENERALLY EXACT
REPAIR-COVER HYPERGRAPH     = EXACT UNCONSTRAINED COMBINATORIAL OBJECT
GENERIC CONVEXITY/CONCAVITY = NOT ASSUMED
COMPOSITION SUBADDITIVITY   = CONDITIONAL ON EXPLICIT MODULARITY ASSUMPTIONS
NEW FOUNDATIONAL THEORY     = NOT ESTABLISHED
NEW ASSAY                   = NONE
BL-003                      = UNOPENED
```

This note is a **mathematical continuation** of [`CORRECTION_COMPLEXITY.md`](CORRECTION_COMPLEXITY.md). It does not modify the experimental record, the frozen program checkpoint, or the interpretation of any completed assay.

The empirical program remains parked while the mathematical question is attacked.

The central correction made here is:

> **Static repair structure does not substitute for information about which failure occurred. It reduces online information demand only by changing which failures can safely share the same bounded repair policy.**

That shifts the repair-factorization profile from two parallel bookkeeping axes to a genuine architecture-constrained tradeoff.

---

## 1. Fixed setting

Let:

- `E` be the failure space;
- `O : E -> Z` be the fixed admissible evidence interface;
- `H` be the fixed recovery horizon/resource budget;
- `Pi_H` be the class of repair policies executable within `H`;
- `d(e, pi)` be the frozen operational recovery distortion;
- `epsilon >= 0` be the allowed worst-case distortion;
- `L(p)` be the static description/resource cost of repair architecture `p` under the frozen implementation language and accounting rule.

A static architecture `p` contains whatever fixed decoder/synthesizer machinery is admissible. At runtime it receives only the evidence `z = O(e)` and produces an online branch state:

```text
J_p(z) in {1, ..., m_p}
```

followed by a branch repair policy:

```text
pi_{p, J_p(z)} in Pi_H.
```

The runtime causal form is therefore:

```text
failure e
-> evidence O(e)
-> online branch J_p(O(e))
-> bounded repair policy pi_{p,J_p(O(e))}.
```

The static program `p` is fixed before the runtime failure is sampled. It is **not** failure-specific side information.

---

## 2. Why the generic `ell + b` bound was mis-scoped

Suppose the online state has at most `2^b` values and the static architecture has description length at most `ell`.

It is tempting to write:

```text
ell + b >= log2(number of runtime failure cases).
```

That is not a valid generic interpretation when `p` is fixed before the failure.

The `ell` static bits do not tell the system which runtime failure occurred. They specify the reusable architecture shared across all episodes.

If `M` runtime cases require mutually incompatible repairs, then the online path still needs at least `M` distinct repair branches:

```text
b >= ceil(log2 M)
```

independently of static sophistication.

Likewise, if a repair-relevant class variable `C=C(E)` is sampled only after fixed `P=p` is installed, then in the ordinary fixed-task setting:

```text
H(C | P) = H(C).
```

Static structure only reduces runtime information demand when it changes the **operational repair partition** — for example by enabling one shared bounded policy to repair several failures that otherwise required separate branches.

---

## 3. Central object: architecture-constrained repair-cover number

Define the exact worst-case static/online frontier:

```text
nu_{epsilon,H}(ell)
  = inf over architectures p {
      |range(J_p)| :
      L(p) <= ell,
      sup_{e in E} d(e, pi_{p,J_p(O(e))}) <= epsilon
    }.
```

If no architecture of cost at most `ell` satisfies the recovery requirement, define:

```text
nu_{epsilon,H}(ell) = infinity.
```

Then define the minimum fixed-length online branch budget:

```text
b*_{epsilon,H}(ell)
  = ceil(log2 nu_{epsilon,H}(ell)),
```

with:

```text
ceil(log2 infinity) = infinity.
```

Interpretation:

> **`nu_{epsilon,H}(ell)` is the minimum number of runtime repair branches required after allowing at most `ell` units of reusable static repair architecture.**

The central static/online exchange is therefore not “one static bit replaces one online bit.” It is:

```text
more reusable static structure
-> broader / more compositional bounded repairs become expressible
-> more failures can safely share one runtime branch
-> nu_{epsilon,H}(ell) decreases
-> b*_{epsilon,H}(ell) decreases.
```

---

## 4. Immediate monotonicity properties

Under the fixed accounting convention:

### Static budget

If `ell_1 <= ell_2`, every architecture feasible at `ell_1` remains feasible at `ell_2`, so:

```text
nu_{epsilon,H}(ell_2)
<=
nu_{epsilon,H}(ell_1).
```

Thus:

```text
b*_{epsilon,H}(ell)
```

is nonincreasing in `ell`.

### Recovery tolerance

If `epsilon_1 <= epsilon_2`, the larger distortion tolerance weakens the requirement:

```text
nu_{epsilon_2,H}(ell)
<=
nu_{epsilon_1,H}(ell).
```

### Horizon/resources

When increasing `H` only enlarges the admissible policy/construction class:

```text
H_1 <= H_2
=>
nu_{epsilon,H_2}(ell)
<=
nu_{epsilon,H_1}(ell).
```

### Evidence refinement

If `O_1 = h o O_2`, so `O_2` is at least as informative as `O_1`, an architecture under `O_2` can discard information and reproduce `O_1`:

```text
nu_{epsilon,H}^{O_2}(ell)
<=
nu_{epsilon,H}^{O_1}(ell).
```

The entire RFP weakly improves under evidence refinement.

---

## 5. Shape: integer step frontier, not automatically convex

With integer-valued prefix description length, `nu_{epsilon,H}(ell)` is an integer-valued nonincreasing step function taking values in:

```text
{1, 2, ..., |relevant evidence classes|} union {infinity}
```

for a finite problem.

This immediately supports three qualitative regimes:

```text
NO EXCHANGE:
nu(ell) is bounded below by a permanent diagnostic floor.

THRESHOLD EXCHANGE:
nu(ell) drops sharply when a sufficiently expressive shared repair becomes representable.

PROGRESSIVE EXCHANGE:
nu(ell) drops through several plateaus as increasingly broad repair modules become available.
```

No generic convexity or concavity is currently claimed.

Without additional structural assumptions, arbitrary monotone threshold patterns can be engineered by assigning useful shared repair mechanisms prescribed description thresholds. Therefore any convexity, smoothness, or diminishing-returns theorem must come from an explicit repair-compositionality assumption, not from the definition of `nu` alone.

---

## 6. Evidence quotient: aliasing must be handled before repair covering

The runtime branch is a function of `O(e)`, not hidden failure identity.

Define the observation fibers:

```text
Q_O = { O^{-1}(z) : z in range(O) }.
```

For a repair policy `pi`, define the set of observation fibers that `pi` repairs uniformly:

```text
C_{epsilon,H}(pi)
  = {
      q in Q_O :
      d(e, pi) <= epsilon for every e in q
    }.
```

If some reachable observation fiber `q` satisfies:

```text
there is no pi in Pi_H
such that
d(e,pi) <= epsilon for every e in q,
```

then failures inside that single evidence class require incompatible repairs while remaining observationally aliased.

Therefore:

```text
nu_{epsilon,H}(ell) = infinity
for every ell.
```

This is **evidence/interface infeasibility**, not high repair complexity.

Durable separation:

```text
missing discriminating evidence
!=
expensive bounded repair synthesis.
```

---

## 7. Exact unconstrained combinatorial object: repair-cover hypergraph

The pairwise repair-overlap graph is useful but not exact in general.

Three observation fibers can be pairwise jointly repairable while no single policy repairs all three simultaneously. Pairwise edges therefore do not fully encode higher-order compatibility.

The exact unconstrained object is the policy-coverage hypergraph on observation fibers:

```text
H_{epsilon,H}^{repair}
  = (Q_O, A),
```

where every admissible bounded repair policy contributes a hyperedge:

```text
A_pi = C_{epsilon,H}(pi).
```

The unconstrained minimum number of repair branches is the minimum number of policy-coverage hyperedges whose union covers all observation fibers:

```text
nu_{epsilon,H}^{infty}
  = min {
      m :
      exists pi_1,...,pi_m in Pi_H,
      Q_O subset union_j C_{epsilon,H}(pi_j)
    }.
```

Under a universal enough static implementation language and no static cost bound, this is the asymptotic floor:

```text
inf_ell nu_{epsilon,H}(ell)
=
nu_{epsilon,H}^{infty}.
```

The equality is conditional on the architecture language being able to encode any finite admissible policy family and branch map with finite cost.

Interpretation:

> **The ultimate online-information floor is determined by how many bounded repair policies are intrinsically needed to cover the evidence-distinguishable failure space.**

---

## 8. Repair conflict graph: useful lower bound

Define a conflict graph on observation fibers:

```text
G_conf = (Q_O, E_conf)
```

with edge `(q_i,q_j)` whenever no single bounded policy is epsilon-valid for every failure in both fibers.

Each runtime branch must correspond to a set of fibers containing no conflict edge.

Therefore every feasible branch assignment induces a proper coloring of `G_conf`, giving:

```text
chi(G_conf)
<=
nu_{epsilon,H}^{infty}
<=
nu_{epsilon,H}(ell).
```

Hence:

```text
b*_{epsilon,H}(ell)
>=
ceil(log2 chi(G_conf)).
```

This gives a permanent no-exchange lower bound.

But the graph can be loose because it misses higher-order incompatibility. The repair-cover hypergraph is the exact combinatorial object; graph coloring is a lower-bound relaxation.

---

## 9. No-exchange theorem

Suppose there exists a set of `M` observation fibers:

```text
q_1,...,q_M
```

that are pairwise conflict-connected, meaning no bounded repair policy can repair any two of them simultaneously within distortion `epsilon`.

Then:

```text
chi(G_conf) >= M
```

for that clique, hence:

```text
nu_{epsilon,H}(ell) >= M
for every ell.
```

Therefore:

```text
b*_{epsilon,H}(ell)
>=
ceil(log2 M)
for every ell.
```

No increase in static repair sophistication can remove this diagnostic floor unless the admissible repair policy class itself changes — for example through a larger horizon, new actions, or a different recovery criterion.

---

## 10. Threshold exchange

Suppose `N` evidence-distinguishable failures initially require separate specialized repairs, but there also exists one bounded policy `g` that repairs all of them.

Assume the cheapest static architecture that can realize `g` has cost `L_g`, and no architecture below `L_g` can realize any intermediate shared repair.

Then:

```text
nu(ell) = N     for ell < L_g,
nu(ell) = 1     for ell >= L_g.
```

Therefore:

```text
b*(ell) = ceil(log2 N)   for ell < L_g,
b*(ell) = 0              for ell >= L_g.
```

This is genuine exchange:

```text
additional static structure
-> broader common repair becomes realizable
-> runtime failure identity no longer needs to determine the repair branch.
```

The static program did not encode which failure occurred. It changed which distinctions remained operationally necessary.

---

## 11. Progressive exchange

Let increasingly expensive shared repair modules induce a nested sequence of valid covers:

```text
P_0, P_1, ..., P_k
```

with architecture thresholds:

```text
ell_0 < ell_1 < ... < ell_k
```

and branch counts:

```text
m_0 > m_1 > ... > m_k.
```

Then:

```text
nu(ell) <= m_j
for ell >= ell_j.
```

If matching lower bounds show that no cheaper architecture can realize a smaller cover, the RFP follows the corresponding staircase exactly.

The mathematical burden in a real theory is therefore to characterize which repair modules induce which cover contractions and how their implementation costs compose.

---

## 12. Architecture-realizable cover families

The unconstrained hypergraph records which bounded policies exist. It does not yet account for the cost of implementing a *family* of policies plus the branch map.

For each static architecture `p`, define its realized policy family:

```text
P(p)
  = {
      pi_{p,j} :
      j in range(J_p)
    }.
```

and its induced repair cover:

```text
C(p)
  = {
      C_{epsilon,H}(pi_{p,j}) :
      j in range(J_p)
    }.
```

Then `nu_{epsilon,H}(ell)` is equivalently the smallest realized cover cardinality among architecture programs with:

```text
L(p) <= ell
```

whose decoder assigns every observation fiber to a branch whose policy covers that fiber.

This is where static constructor complexity enters the combinatorics:

```text
policy cover exists
!=
policy cover is jointly generatable within static budget ell.
```

---

## 13. Distributional static/online frontier

For a failure distribution `mu`, worst-case branch count can be replaced by expected online coding burden.

For architecture `p`, let:

```text
J_p = J_p(O(E)).
```

For deterministic branch encoding, define:

```text
R_{mu,epsilon,H}(ell)
  = inf over p {
      H_mu(J_p) :
      L(p) <= ell,
      E_{E~mu}[d(E, pi_{p,J_p})] <= epsilon
    }.
```

Optimal prefix coding gives expected online message length within one bit of:

```text
H_mu(J_p).
```

This is the correct entropy analogue of the static/online tradeoff.

The quantity that changes with static architecture is **not** generically `H(C | P)` for a fixed runtime class variable. It is the entropy of the repair partition induced by the architecture:

```text
H(J_p).
```

A richer static architecture can lower `H(J_p)` only by enabling broader shared repair policies or otherwise changing the valid operational partition.

---

## 14. Approximate recovery and rate-distortion form

For graded recovery distortion, a natural extension is:

```text
R_{mu,H}(ell, epsilon)
  = inf I(E ; J_p)
```

or, for deterministic branch maps:

```text
R_{mu,H}(ell, epsilon)
  = inf H(J_p)
```

subject to:

```text
L(p) <= ell
E[d(E, pi_{p,J_p})] <= epsilon.
```

This resembles rate-distortion theory with an additional constraint on the reusable implementation complexity of the reproduction architecture.

No claim is made here that this is a new foundational rate-distortion theory. The static architecture constraint is the feature that couples otherwise familiar ingredients.

---

## 15. Conditional composition bound

Suppose two correction problems factorize:

```text
E = E_1 x E_2,
O(e_1,e_2) = (O_1(e_1), O_2(e_2)),
```

and bounded repair policies compose independently:

```text
pi = pi_1 tensor pi_2,
```

with additive static architecture cost and compatible horizon accounting.

If architecture `p_1` of cost `ell_1` uses `m_1` branches and architecture `p_2` of cost `ell_2` uses `m_2` branches, their product architecture uses at most:

```text
m_1 m_2
```

branches at cost at most:

```text
ell_1 + ell_2 + O(1).
```

Therefore, under these explicit composability assumptions:

```text
nu_{12}(ell_1 + ell_2 + O(1))
<=
nu_1(ell_1) nu_2(ell_2).
```

Equivalently:

```text
b*_{12}(ell_1 + ell_2 + O(1))
<=
b*_1(ell_1) + b*_2(ell_2) + O(1).
```

This is a conditional subadditivity result, not a universal property of arbitrary repair relations.

---

## 16. Static-to-online exchange rate

Where the discrete frontier changes, define a local finite-difference quantity:

```text
X(ell_1 -> ell_2)
  = [log2 nu(ell_1) - log2 nu(ell_2)]
    / [ell_2 - ell_1].
```

Interpretation:

> **Online repair-discrimination bits eliminated per additional unit of reusable static architecture across the specified budget interval.**

This quantity is architecture- and class-relative.

It may be:

```text
0          in no-exchange plateaus,
large      at threshold transitions,
variable   under progressive modular repair,
infinite / undefined across infeasible boundaries.
```

No universal exchange rate is expected.

---

## 17. Relation to the earlier repair-factorization profile

The earlier RFP separated:

```text
online information bottleneck b
static reusable machinery Phi(b)
construction resources H.
```

The corrected static/online frontier is now:

```text
S_{epsilon,H}
  = {
      (ell,b) :
      there exists a repair architecture p with
      L(p) <= ell,
      |range(J_p)| <= 2^b,
      worst-case distortion <= epsilon
    }.
```

The lower Pareto boundary can be represented either as:

```text
b*_{epsilon,H}(ell)
```

or its inverse:

```text
ell*_{epsilon,H}(b)
  = inf {
      ell :
      nu_{epsilon,H}(ell) <= 2^b
    }.
```

This is the current clean core of the RFP.

The older covering/packing and structured-generator bounds remain useful for controlling the **static implementation cost** of candidate covers. The new `nu(ell)` object controls how much those implementations can actually contract the runtime repair partition.

---

## 18. Relationship to repair-overlap structure

The central mathematical target is now:

> **Characterize `nu_{epsilon,H}(ell)` using the overlap structure of bounded valid repairs while retaining the architecture cost required to realize useful repair covers.**

Three nested objects should remain distinct:

```text
PAIRWISE CONFLICT GRAPH
-> cheap lower-bound relaxation

POLICY-COVER HYPERGRAPH
-> exact unconstrained overlap structure

ARCHITECTURE-REALIZABLE COVER FAMILY
-> budgeted object defining nu_{epsilon,H}(ell).
```

The graph is not allowed to silently replace the hypergraph.

The hypergraph is not allowed to ignore constructor/program cost.

The architecture budget is not allowed to alter the evidence interface after the fact.

---

## 19. What would constitute a genuinely useful theorem

A nontrivial theory should do more than restate monotonicity.

Useful targets include:

1. **Overlap lower bounds**
   
   Derive bounds on `nu(ell)` from conflict graph chromatic number, higher-order incompatibility, fractional covers, or packing structure.

2. **Architecture upper bounds**
   
   Show that explicit reusable modules of total cost `ell` realize a policy cover of cardinality `m(ell)`.

3. **Matching regimes**
   
   Identify structured families where lower and upper bounds match in scaling.

4. **Composition laws**
   
   Establish subadditivity or other regularity only under explicit modularity assumptions.

5. **Evidence-sensitive phase boundaries**
   
   Characterize when an observation refinement changes the frontier from infeasible to finite, or lowers the permanent diagnostic floor.

6. **Horizon-sensitive phase boundaries**
   
   Characterize when additional interaction time allows one adaptive repair policy to cover failures that required multiple one-shot branches.

A theorem that merely combines a standard graph-cover bound with a separately quoted program-length bound is useful bookkeeping but does not yet establish new mathematics.

---

## 20. Current mathematical claim ceiling

Current status:

```text
packing / covering arguments               = STANDARD / DERIVED
constructor-accounted cover upper bound    = DERIVED
repair-factorization profile               = COHERENT COUPLED ORGANIZING OBJECT
nu_{epsilon,H}(ell)                        = CENTRAL FRONTIER CANDIDATE
b*_{epsilon,H}(ell)                        = CLEAN ONLINE-BRANCH FORM
monotonicity                               = IMMEDIATE
pairwise conflict chromatic lower bound    = VALID BUT NOT GENERALLY TIGHT
repair-cover hypergraph                    = EXACT UNCONSTRAINED COMBINATORIAL OBJECT
architecture-realizable cover family       = EXACT BUDGETED OBJECT
universal convexity / concavity            = NOT ESTABLISHED / NOT EXPECTED WITHOUT STRUCTURE
conditional composition subadditivity      = AVAILABLE UNDER EXPLICIT FACTORIZATION ASSUMPTIONS
new foundational complexity theory         = NOT ESTABLISHED
new empirical assay                        = NONE
```

The current strongest compression is:

> **Static repair structure does not buy runtime information by storing failure identity in advance. It buys runtime information only when additional reusable machinery makes previously distinct failures share a valid bounded repair policy.**

And the next mathematical knife is:

> **Determine which overlap/compositional properties of the bounded repair-policy family control the shape of `nu_{epsilon,H}(ell)`, including permanent diagnostic floors, threshold contractions, and progressive contractions as static architecture budget increases.**

---

## 21. Program boundary

This mathematical continuation does not reopen any empirical line.

```text
BL-001       = POSITIVE
BL-002       = POSITIVE
BL×CC-001    = POSITIVE / AUDITED / PARKED
BL-003       = UNOPENED
H_CRCB       = OPEN
CC-specific irreducibility = UNESTABLISHED
NEW ASSAY    = NONE
```

The empirical result remains interpreted narrowly as evidence for controllable corrective feedback in the frozen supplied-family setting.

The mathematical branch is asking a different question:

> **How much reusable repair architecture is required to reduce the number of runtime distinctions that must remain operationally available for bounded recovery?**
