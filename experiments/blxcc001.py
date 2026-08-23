#!/usr/bin/env python3
"""BLxCC-001 frozen reference executable.

Default invocation performs STATIC/AUDIT-ONLY checks and never evaluates the
scientific seed schedule. Scientific execution requires explicit --execute.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from typing import Dict, List, Tuple

EXPERIMENT_ID = "BLXCC001"
WORLDS = ("L", "R")
N = 4
ALPHA = 0.20
BETA_L = 0.30
BETA_H = 0.70
THROUGHPUT_SCALE = 4.0
LAMBDA_L = THROUGHPUT_SCALE * BETA_L
LAMBDA_H = THROUGHPUT_SCALE * BETA_H
D0 = (0.50, 0.50, 0.50, 0.50)
ETA = 0.25
P_TRUE_INITIAL = 0.30
EPSILON = 0.10
ROUNDS = 3
PERSISTENCE_M = 2
SEEDS_PER_WORLD = 4096
ALPHA_PRIMARY = 0.05
KAPPA_C = 0.79242459
TIE_EPS = 1e-15
PROBES = ("qL", "qR")
CELLS = ("A", "B", "C", "D")
OPEN_CONSEQUENCE_CELLS = frozenset(("A", "C"))
ENDOGENOUS_CELLS = frozenset(("A", "B"))
AUDIT_SENTINELS = (0, 1, 17, 255)
EXPECTED_CONFIG_HASH = "3b06b39fb942aaecdccad138ceb763a5495092231e5a26bf07c2d0fc921559ba"

T_L = (
    (0.0, ALPHA, 0.0, 0.0),
    (ALPHA, 0.0, BETA_H, 0.0),
    (0.0, 0.0, 0.0, ALPHA),
    (BETA_L, 0.0, ALPHA, 0.0),
)
T_R = (
    (0.0, ALPHA, 0.0, 0.0),
    (ALPHA, 0.0, BETA_L, 0.0),
    (0.0, 0.0, 0.0, ALPHA),
    (BETA_H, 0.0, ALPHA, 0.0),
)
TOPOLOGIES = {"L": T_L, "R": T_R}


def canonical_config() -> Dict[str, object]:
    return {
        "experiment_id": EXPERIMENT_ID,
        "worlds": list(WORLDS),
        "N": N,
        "alpha": ALPHA,
        "beta_l": BETA_L,
        "beta_h": BETA_H,
        "throughput_scale": THROUGHPUT_SCALE,
        "lambda_l": LAMBDA_L,
        "lambda_h": LAMBDA_H,
        "D0": list(D0),
        "eta": ETA,
        "p_true_initial": P_TRUE_INITIAL,
        "epsilon": EPSILON,
        "rounds": ROUNDS,
        "persistence_m": PERSISTENCE_M,
        "seeds_per_world": SEEDS_PER_WORLD,
        "alpha_primary": ALPHA_PRIMARY,
        "kappa_c": KAPPA_C,
        "tie_eps": TIE_EPS,
        "probes": list(PROBES),
        "cells": list(CELLS),
        "open_consequence_cells": sorted(OPEN_CONSEQUENCE_CELLS),
        "endogenous_cells": sorted(ENDOGENOUS_CELLS),
        "T_L": [list(row) for row in T_L],
        "T_R": [list(row) for row in T_R],
        "science_seed_schedule": {"worlds": list(WORLDS), "s": [0, SEEDS_PER_WORLD - 1]},
        "random_field_version": "sha256-v1",
        "primary_test": "one-sided exact McNemar on paired sustained-escape indicators",
    }


def config_hash() -> str:
    payload = json.dumps(canonical_config(), sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def g_after(T: Tuple[Tuple[float, ...], ...], action: int) -> float:
    d = list(D0)
    out = list(d)
    out[action] = d[action] + ETA * (1.0 - d[action])
    for j in range(N):
        if j == action:
            continue
        out[j] = d[j] + ETA * T[action][j] * (1.0 - d[j])
    return sum(out) / N


def posterior_p_r(log_odds_r_over_l: float) -> float:
    if log_odds_r_over_l >= 0:
        z = math.exp(-log_odds_r_over_l)
        return 1.0 / (1.0 + z)
    z = math.exp(log_odds_r_over_l)
    return z / (1.0 + z)


def posterior_mean_gain(log_odds: float, action: int) -> float:
    p_r = posterior_p_r(log_odds)
    return (1.0 - p_r) * g_after(T_L, action) + p_r * g_after(T_R, action)


def correct_action(world: str) -> int:
    scores = [g_after(TOPOLOGIES[world], i) for i in range(N)]
    best = max(scores)
    winners = [i for i, v in enumerate(scores) if abs(v - best) <= TIE_EPS]
    if len(winners) != 1:
        raise AssertionError(f"oracle action not unique in world {world}: {winners}")
    return winners[0]


def _digest(*parts: object) -> bytes:
    text = "|".join(str(x) for x in parts)
    return hashlib.sha256(text.encode("ascii")).digest()


def hash_uniform(domain: str, stream: str, world: str, seed: int, t: int, tag: str = "") -> float:
    d = _digest(EXPERIMENT_ID, domain, stream, f"world={world}", f"s={seed}", f"t={t}", tag)
    x = int.from_bytes(d[:8], "big", signed=False)
    return (x + 0.5) / 2**64


def hash_normal(domain: str, stream: str, world: str, seed: int, t: int, tag: str = "") -> float:
    d = _digest(EXPERIMENT_ID, domain, stream, f"world={world}", f"s={seed}", f"t={t}", tag)
    x = int.from_bytes(d[:8], "big", signed=False)
    y = int.from_bytes(d[8:16], "big", signed=False)
    u1 = (x + 0.5) / 2**64
    u2 = (y + 0.5) / 2**64
    return math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)


def poisson_from_uniform(lam: float, u: float) -> int:
    if not (lam > 0.0 and 0.0 < u < 1.0):
        raise ValueError("invalid Poisson inversion arguments")
    k = 0
    p = math.exp(-lam)
    cdf = p
    while u > cdf:
        k += 1
        p *= lam / k
        cdf += p
        if k > 1000:
            raise RuntimeError("Poisson inversion failed to converge")
    return k


def lambda_for(world: str, probe: str) -> float:
    if world == "L":
        return LAMBDA_H if probe == "qL" else LAMBDA_L
    if world == "R":
        return LAMBDA_L if probe == "qL" else LAMBDA_H
    raise ValueError(world)


def survey_llr_r_over_l(probe: str, y: int) -> float:
    lam_r = lambda_for("R", probe)
    lam_l = lambda_for("L", probe)
    return y * math.log(lam_r / lam_l) - (lam_r - lam_l)


def expected_throughput(log_odds: float, probe: str) -> float:
    p_r = posterior_p_r(log_odds)
    return (1.0 - p_r) * lambda_for("L", probe) + p_r * lambda_for("R", probe)


def choose_probe(policy_kind: str, log_odds: float, u: float) -> str:
    if policy_kind == "open":
        return "qL" if u < 0.5 else "qR"
    if policy_kind != "endo":
        raise ValueError(policy_kind)
    v_l = expected_throughput(log_odds, "qL")
    v_r = expected_throughput(log_odds, "qR")
    if abs(v_l - v_r) <= TIE_EPS:
        return "qL" if u < 0.5 else "qR"
    preferred = "qL" if v_l > v_r else "qR"
    other = "qR" if preferred == "qL" else "qL"
    preferred_prob = 1.0 - EPSILON / 2.0
    return preferred if u < preferred_prob else other


def choose_depth_action(log_odds: float, u_tie: float) -> int:
    scores = [posterior_mean_gain(log_odds, i) for i in range(N)]
    best = max(scores)
    winners = [i for i, v in enumerate(scores) if abs(v - best) <= TIE_EPS]
    if len(winners) == 1:
        return winners[0]
    if set(winners) == {1, 3}:
        return 1 if u_tie < 0.5 else 3
    return min(winners)


def initial_log_odds(world: str) -> float:
    p_r = P_TRUE_INITIAL if world == "R" else 1.0 - P_TRUE_INITIAL
    return math.log(p_r / (1.0 - p_r))


def initial_map_label(world: str) -> str:
    return "L" if initial_log_odds(world) < 0 else "R"


def map_label(log_odds: float) -> str | None:
    if log_odds < -TIE_EPS:
        return "L"
    if log_odds > TIE_EPS:
        return "R"
    return None


def consequence_mu(hypothesis: str, action: int) -> float:
    return g_after(TOPOLOGIES[hypothesis], action)


def consequence_gap() -> float:
    gaps = [abs(consequence_mu("R", a) - consequence_mu("L", a)) for a in (1, 3)]
    if abs(gaps[0] - gaps[1]) > TIE_EPS:
        raise AssertionError("mirror consequence gaps differ")
    return gaps[0]


def consequence_sigma() -> float:
    return consequence_gap() / KAPPA_C


def consequence_llr_r_over_l(c: float, action: int) -> float:
    mu_r = consequence_mu("R", action)
    mu_l = consequence_mu("L", action)
    sig = consequence_sigma()
    return -((c - mu_r) ** 2 - (c - mu_l) ** 2) / (2.0 * sig * sig)


def consequence_discrepancy(c: float, action: int, log_odds_pre: float) -> float:
    p_r = posterior_p_r(log_odds_pre)
    mu_pred = (1.0 - p_r) * consequence_mu("L", action) + p_r * consequence_mu("R", action)
    return (c - mu_pred) / consequence_sigma()


@dataclass
class RoundTrace:
    t: int
    log_odds_pre: float
    probe: str
    y: int
    survey_llr: float
    log_odds_post_survey: float
    depth_action: int


@dataclass
class Trace:
    cell: str
    world: str
    seed: int
    rounds: List[RoundTrace]
    consequence_active: bool
    consequence_value: float | None
    dh_discrepancy: float | None
    identification: str | None
    w_corr: float
    u_corr: float
    tau_escape: int | None
    success: int


def simulate(cell: str, world: str, seed: int, domain: str) -> Trace:
    if cell not in CELLS:
        raise ValueError(cell)
    policy_kind = "endo" if cell in ENDOGENOUS_CELLS else "open"
    consequence_open = cell in OPEN_CONSEQUENCE_CELLS
    log_odds = initial_log_odds(world)
    rounds: List[RoundTrace] = []
    consequence_active = False
    consequence_value = None
    dh = None
    ident = None
    w_corr = 0.0
    u_corr = 0.0

    for t in range(ROUNDS):
        pre = log_odds
        u_select = hash_uniform(domain, "select", world, seed, t)
        q = choose_probe(policy_kind, pre, u_select)
        u_y = hash_uniform(domain, "survey", world, seed, t, q)
        y = poisson_from_uniform(lambda_for(world, q), u_y)
        llr_q = survey_llr_r_over_l(q, y)
        post_survey = pre + llr_q
        u_tie = hash_uniform(domain, "action-tie", world, seed, t)
        d_action = choose_depth_action(post_survey, u_tie)
        rounds.append(RoundTrace(t, pre, q, y, llr_q, post_survey, d_action))
        log_odds = post_survey

        if t == 0 and map_label(post_survey) == initial_map_label(world):
            consequence_active = True
            sig = consequence_sigma()
            z = hash_normal(domain, "consequence", world, seed, 0)
            mu_true = consequence_mu(world, d_action)
            c = mu_true + sig * z
            consequence_value = c
            dh = consequence_discrepancy(c, d_action, post_survey)
            ident = "T_L_vs_T_R"
            w_corr = consequence_llr_r_over_l(c, d_action)
            u_corr = w_corr if consequence_open else 0.0
            log_odds = post_survey + u_corr

    oracle = correct_action(world)
    actions = [r.depth_action for r in rounds]
    tau = None
    for t in range(ROUNDS - PERSISTENCE_M + 1):
        if all(actions[t + k] == oracle for k in range(PERSISTENCE_M)):
            tau = t
            break
    return Trace(cell, world, seed, rounds, consequence_active, consequence_value, dh, ident, w_corr, u_corr, tau, 1 if tau is not None else 0)


def exact_mcnemar_one_sided(favorable: int, unfavorable: int) -> float:
    n = favorable + unfavorable
    if n == 0:
        return 1.0
    numerator = sum(math.comb(n, k) for k in range(favorable, n + 1))
    return float(numerator / (2 ** n))


def execute_science() -> Dict[str, object]:
    rows = []
    per_world = {}
    for world in WORLDS:
        traces: Dict[str, List[Trace]] = {c: [] for c in CELLS}
        for s in range(SEEDS_PER_WORLD):
            for c in CELLS:
                traces[c].append(simulate(c, world, s, domain="science"))
        per_world[world] = {c: sum(t.success for t in traces[c]) / SEEDS_PER_WORLD for c in CELLS}
        for s in range(SEEDS_PER_WORLD):
            rows.append({c: traces[c][s].success for c in CELLS})

    n = len(rows)
    rates = {c: sum(r[c] for r in rows) / n for c in CELLS}
    favorable_ab = sum(1 for r in rows if r["A"] == 1 and r["B"] == 0)
    unfavorable_ab = sum(1 for r in rows if r["A"] == 0 and r["B"] == 1)
    delta_ab = rates["A"] - rates["B"]
    p_ab = exact_mcnemar_one_sided(favorable_ab, unfavorable_ab)
    classification = (
        "CORRECTIVE_INFLUENCE_ADDS_SUSTAINED_ESCAPE"
        if delta_ab > 0.0 and p_ab < ALPHA_PRIMARY
        else "NO_DEMONSTRATED_CORRECTIVE_INFLUENCE_GAIN"
    )
    delta_cd = rates["C"] - rates["D"]
    delta_bd = rates["B"] - rates["D"]
    interaction = delta_ab - delta_cd
    return {
        "status": classification,
        "execution_provenance": "REFERENCE_EXECUTABLE_COMPLETED",
        "config_hash": config_hash(),
        "n_paired_specimens": n,
        "worlds": list(WORLDS),
        "seeds_per_world": SEEDS_PER_WORLD,
        "rates": rates,
        "primary": {
            "estimand": "P(A sustained escape) - P(B sustained escape)",
            "delta_esc": delta_ab,
            "discordant_A1_B0": favorable_ab,
            "discordant_A0_B1": unfavorable_ab,
            "one_sided_exact_mcnemar_p": p_ab,
            "alpha": ALPHA_PRIMARY,
        },
        "secondary_descriptive_controls": {
            "C_minus_D": delta_cd,
            "B_minus_D": delta_bd,
            "interaction_AB_minus_CD": interaction,
            "note": "Secondary/descriptive; cannot redefine the primary classification.",
        },
        "per_world_rates": per_world,
        "claim_ceiling": (
            "A positive primary result supports only that, within this frozen symmetric supplied two-topology synthetic world and three-round horizon, allowing the matched ordinary consequence likelihood signal to acquire developmental influence increased first sustained correct allocation relative to cutting only that consequence W->U channel under endogenous throughput-probe allocation."
        ),
    }


def kl_poisson(lam_p: float, lam_q: float) -> float:
    return lam_p * math.log(lam_p / lam_q) + lam_q - lam_p


def audit() -> Dict[str, object]:
    checks: List[Tuple[str, bool, str]] = []

    def ck(name: str, cond: bool, detail: str) -> None:
        checks.append((name, bool(cond), detail))

    ck("config hash", config_hash() == EXPECTED_CONFIG_HASH, f"config_hash={config_hash()}")
    ck("two supplied topologies", set(TOPOLOGIES) == {"L", "R"}, str(tuple(TOPOLOGIES)))
    ck("T* always representable", all(w in TOPOLOGIES for w in WORLDS), "T* in H={T_L,T_R}")
    ck("fixed allocation competence", D0 == (0.5, 0.5, 0.5, 0.5), f"D0={D0}")
    ck("unique oracle action L", correct_action("L") == 1, f"oracle_L={correct_action('L')}")
    ck("unique oracle action R", correct_action("R") == 3, f"oracle_R={correct_action('R')}")
    ck("mirror initial wrongness", initial_map_label("L") == "R" and initial_map_label("R") == "L", "true topology gets 0.30 prior")
    ck("throughput ordering", 0.0 < LAMBDA_L < LAMBDA_H, f"lambda_L={LAMBDA_L}, lambda_H={LAMBDA_H}")

    i_wrong = kl_poisson(LAMBDA_L, LAMBDA_H)
    i_right = kl_poisson(LAMBDA_H, LAMBDA_L)
    ck("wrong probe informative", i_wrong > 0.0, f"I_wrong={i_wrong:.12f}")
    ck("aligned probe more informative", i_right > i_wrong, f"I_right={i_right:.12f} > I_wrong={i_wrong:.12f}")
    ck("mirror evidence-kernel asymmetry", survey_llr_r_over_l("qL", 0) != survey_llr_r_over_l("qR", 0), "qL and qR LLR kernels differ")

    l_r = initial_log_odds("R")
    l_l = initial_log_odds("L")
    ck("mirror log-odds", abs(l_r + l_l) <= 1e-15, f"L0_R={l_r:.12f}, L0_L={l_l:.12f}")
    ck("endogenous preferred probe R-world", choose_probe("endo", l_r, 0.0) == "qL", "wrong map prefers qL")
    ck("endogenous preferred probe L-world", choose_probe("endo", l_l, 0.0) == "qR", "mirror wrong map prefers qR")
    ck("nonzero alternative floor", abs(EPSILON / 2.0 - 0.05) <= 1e-15, f"alternative-probe floor={EPSILON/2}")
    ck("open-loop map blind", choose_probe("open", -100.0, 0.25) == choose_probe("open", 100.0, 0.25), "q independent of map")
    ck("sustained endpoint temporal floor", ROUNDS == 3 and PERSISTENCE_M == 2, "t={0,1,2}; tau in {0,1}")
    ck("consequence gap positive", consequence_gap() > 0.0, f"Delta_C={consequence_gap():.12f}")
    ck("consequence sigma positive", consequence_sigma() > 0.0, f"sigma_C={consequence_sigma():.12f}")

    sentinel_ok = True
    sentinel_detail = []
    for world in WORLDS:
        for s in AUDIT_SENTINELS:
            a = simulate("A", world, s, domain="audit")
            b = simulate("B", world, s, domain="audit")
            fields_equal = (
                a.rounds[0] == b.rounds[0]
                and a.consequence_active == b.consequence_active
                and a.consequence_value == b.consequence_value
                and a.dh_discrepancy == b.dh_discrepancy
                and a.identification == b.identification
                and a.w_corr == b.w_corr
            )
            if not fields_equal:
                sentinel_ok = False
            if a.consequence_active and not (a.u_corr == a.w_corr and b.u_corr == 0.0):
                sentinel_ok = False
            sentinel_detail.append((world, s, a.consequence_active))
    ck("A/B identical through W on audit sentinels", sentinel_ok, repr(sentinel_detail))
    ck("truth-free survey scorer", survey_llr_r_over_l.__code__.co_argcount == 2, "survey_llr(probe,y)")
    ck("truth-free consequence scorer", consequence_llr_r_over_l.__code__.co_argcount == 2, "consequence_llr(c,action)")

    passed = all(ok for _, ok, _ in checks)
    return {
        "status": "PRE_RUN_AUDIT_PASS" if passed else "SPECIFICATION_AUDIT_FAILURE",
        "config_hash": config_hash(),
        "science_execution_performed": False,
        "checks": [{"name": n, "pass": ok, "detail": d} for n, ok, d in checks],
        "prospective_calibration_prediction": {
            "delta_esc_A_minus_B_approx": 0.08821044,
            "label": "CALIBRATION PREDICTION ONLY — NOT AN EMPIRICAL RESULT",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true", help="Execute the frozen scientific seed schedule. Omit for audit-only mode.")
    args = parser.parse_args()
    result = execute_science() if args.execute else audit()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
