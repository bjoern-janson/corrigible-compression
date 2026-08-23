# BL-001 Result

## Provenance

Scientific freeze commit:

```text
496b7829606db74635819afdf5dad5f2c0445d0f
```

Execution status before run:

```text
BL-001 = SPECIFICATION_COMPLETE
```

The pre-execution structural audit passed before any noisy specimen was evaluated:

```text
unique topology count            = 32
Q8 exact recomputation           = PASS
permutation hash                 = PASS
Q8 hash                          = PASS
unique noiseless Q8 signatures  = 32
```

Therefore the measurement/interface precondition passed.

## Frozen experiment family

```text
worlds                    = 32
noise specimens per world = 256
paired specimens           = 8192
```

Execution environment:

```text
Python 3.13.5
NumPy  2.3.5
SciPy  1.17.0
Linux 6.18.35 x86_64 glibc 2.41
```

## Primary result

Frozen estimand:

```text
Delta = R_topo - R_raw
```

Observed:

```text
Delta                           = -0.004517676035563136
95% one-sided upper bound       = -0.0035304210090615247
95% two-sided CI                = [-0.005705229911285542,
                                   -0.0033301221598407297]
one-sided p                     = 4.696482726098215e-09
world-level t(31)                = -7.758688855601526
```

Regret:

```text
mean R_topo                      = 0.00007041931152343696
mean R_raw                       = 0.004588095347086573
median R_topo                    = 0
median R_raw                     = 0.004322916666666621
oracle-gap fraction closed       = 0.9846517331929135
```

Specimen-level paired outcomes:

```text
topology better  = 6767 / 8192 = 0.8260498046875
tie              = 1363 / 8192 = 0.1663818359375
topology worse   =   62 / 8192 = 0.007568359375
```

Frozen classification:

```text
TOPOLOGY_ADDS_ALLOCATION_VALUE
```

## Diagnostic decomposition

### Measurement/interface

PASS.

All 32 frozen candidate worlds have unique noiseless signatures under the frozen Q8 measurement interface.

### Topology inference

The topology-aware completion also improved the frozen full-map MSE diagnostic:

```text
mean MSE_topo                  = 0.0007656433471752654
mean MSE_raw                   = 0.0314224967407782
mean difference                = -0.030656853393602926
95% one-sided upper bound      = -0.03001038980090432
95% two-sided CI               = [-0.031434474499005736,
                                  -0.02987923228820012]
one-sided p                    = 7.46000553609915e-38
MAP candidate accuracy         = 0.9842529296875
```

Thus the run is not classified as measurement failure or map failure.

### Allocation

PASS under the frozen primary rule because the one-sided 95% upper bound for `Delta` is below zero.

## Earned claim

Within this frozen finite family of directed transfer structures, sparse relational measurements supported topology-aware completion that improved allocation of a scarce local-learning operation relative to an equally informed non-topological baseline.

No stronger claim is earned.

In particular, BL-001 does **not** establish:

- adaptive surveying;
- topology construction or invention;
- unknown-domain discovery;
- real neural competence topology;
- human knowledge geometry;
- general broad learning.

## Scope discipline

```text
BL-001: FROZEN -> AUDITED -> EXECUTED -> NARROW POSITIVE RESULT
BL-002: NOT DESIGNED
```
