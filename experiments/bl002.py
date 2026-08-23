#!/usr/bin/env python3
import argparse
import hashlib
import json
import math
import platform

import numpy as np
from scipy import stats

SPEC_VERSION = "BL002_SPEC_001"
N = 12
D0 = np.array([0.15,0.15,0.20,0.20,0.40,0.40,0.55,0.55,0.70,0.70,0.85,0.85], dtype=np.float64)
ETA = 0.25
SIGMA = 0.08
BUDGET = 8
TIE_EPS = 1e-15

PERMS = [
    (6,3,7,5,1,4,0,10,8,11,9,2),
    (5,4,3,7,6,1,2,10,9,11,8,0),
    (7,2,9,0,1,10,5,8,11,3,6,4),
    (4,10,3,11,8,6,7,0,9,5,2,1),
    (1,11,6,7,0,4,5,3,9,2,10,8),
    (2,11,6,4,0,5,3,1,7,8,9,10),
    (5,8,6,3,11,2,0,4,7,10,1,9),
    (8,0,9,10,7,2,4,1,5,6,11,3),
    (10,1,3,11,4,7,5,9,6,8,2,0),
    (5,2,0,4,10,1,8,6,9,7,11,3),
    (10,5,0,1,9,3,6,7,8,4,11,2),
    (11,10,7,3,6,1,5,0,2,8,4,9),
    (8,0,10,5,1,7,2,9,11,4,6,3),
    (11,1,3,5,9,2,6,8,0,4,7,10),
    (1,9,8,6,3,0,2,7,5,10,4,11),
    (3,7,0,6,1,10,2,4,9,5,11,8),
    (10,8,2,1,4,6,9,3,11,0,7,5),
    (11,7,0,2,10,5,8,1,3,6,9,4),
    (11,4,9,2,1,6,3,7,8,10,5,0),
    (3,1,4,8,2,11,7,10,0,6,5,9),
    (7,1,9,2,10,11,4,0,6,5,3,8),
    (7,11,6,9,2,4,1,3,10,0,8,5),
    (11,4,0,2,6,1,8,7,10,9,3,5),
    (1,9,3,2,5,11,7,8,6,4,0,10),
    (6,3,4,9,7,1,2,5,8,11,10,0),
    (10,6,8,3,4,1,0,11,2,5,9,7),
    (6,3,9,4,1,10,5,0,11,8,2,7),
    (8,1,9,6,2,7,0,4,11,5,3,10),
    (7,10,5,1,4,3,0,8,2,9,11,6),
    (5,2,4,9,3,7,11,0,8,10,1,6),
    (10,8,5,1,7,11,3,0,6,4,9,2),
    (11,8,0,1,10,2,9,6,5,7,4,3),
]

PERM_HASH = "a599a5e21f91ec76a55fee4df5551a5d3ea459d2f6aed8572e18c1c6358ca3c3"
EDGES = [(i, j) for i in range(N) for j in range(N) if i != j]
EDGES_HASH = "1530d983ef04da9c4d21e8c587aa5e1bc3710154c9becc950f9ade3979c05067"
POLICY_NAMES = ("VAR", "EDGE_ENTROPY", "ACTION_MI")
POLICY_HASH = "6f7d396f903b6aa25b56298c6bc83cc278d33275bbc9e35e3b779a5d81e94665"

FIXED = {
    "VAR": [(6,3),(9,2),(10,5),(9,3),(2,10),(4,9),(1,9),(7,10)],
    "EDGE_ENTROPY": [(10,5),(6,4),(5,8),(1,9),(3,7),(8,0),(9,2),(7,11)],
    "ACTION_MI": [(0,10),(11,6),(5,1),(11,0),(7,4),(5,9),(1,9),(2,5)],
}
FIXED_HASH = {
    "VAR": "71e0fbff2485edbd5e6cbe1244398a4f24377f84da3e3f96e942e7f793f963b5",
    "EDGE_ENTROPY": "798862423b1ad25798ac3779a7494c0e6e077f5ab723cbe4aa7c04375fd443ff",
    "ACTION_MI": "7a8e6816ac88bdf4c0df8ce7610515342dde1750143befaa7a81afeec004f9b0",
}
EDGE_VALUES = np.array([0.0, 0.15, 0.35, 0.60], dtype=np.float64)


def hash_compact(obj):
    return hashlib.sha256(json.dumps(obj, separators=(",", ":")).encode("utf-8")).hexdigest()


def base_topology():
    T = np.zeros((N, N), dtype=np.float64)
    for i in range(N):
        T[i, (i + 1) % N] = 0.60
        T[i, (i + 3) % N] = 0.35
        T[i, (i + 5) % N] = 0.15
    return T


def relabel(T, p):
    M = np.zeros_like(T)
    for i in range(N):
        for j in range(N):
            M[p[i], p[j]] = T[i, j]
    return M


def topology_family():
    B = base_topology()
    return np.stack([relabel(B, p) for p in PERMS], axis=0)


def gain(T_est, action):
    D = D0.copy()
    for j in range(N):
        if j == action:
            D[j] = D[j] + ETA * (1.0 - D[j])
        else:
            D[j] = D[j] + ETA * T_est[action, j] * (1.0 - D[j])
    return float(np.mean(D))


def action_from_map(T_est):
    vals = np.asarray([gain(T_est, i) for i in range(N)], dtype=np.float64)
    return int(np.argmax(vals))


def oracle_actions(H):
    return np.asarray([action_from_map(H[h]) for h in range(len(H))], dtype=np.int64)


def regret(T_true, action):
    vals = np.asarray([gain(T_true, i) for i in range(N)], dtype=np.float64)
    oracle_action = int(np.argmax(vals))
    return float(vals[oracle_action] - vals[action]), oracle_action


def entropy(probs):
    p = np.asarray(probs, dtype=np.float64)
    p = p[p > 0.0]
    if len(p) == 0:
        return 0.0
    return float(-np.sum(p * np.log(p)))


def posterior_from_history(H, history):
    logw = np.zeros(len(H), dtype=np.float64)
    for (i, j), y in history:
        resid = y - H[:, i, j]
        logw += -0.5 * (resid / SIGMA) ** 2
    logw -= np.max(logw)
    w = np.exp(logw)
    w /= np.sum(w)
    return w


def posterior_mean(H, w):
    return np.tensordot(w, H, axes=(0, 0))


def edge_value_probs(H, w, q):
    i, j = q
    x = H[:, i, j]
    return np.asarray([np.sum(w[x == v]) for v in EDGE_VALUES], dtype=np.float64)


def score_var(H, w, q, astar):
    i, j = q
    x = H[:, i, j]
    m = float(np.sum(w * x))
    return float(np.sum(w * (x - m) ** 2))


def score_edge_entropy(H, w, q, astar):
    return entropy(edge_value_probs(H, w, q))


def score_action_mi(H, w, q, astar):
    p_a = np.asarray([np.sum(w[astar == a]) for a in range(N)], dtype=np.float64)
    h_a = entropy(p_a)
    i, j = q
    x = H[:, i, j]
    cond = 0.0
    for v in EDGE_VALUES:
        mask_v = x == v
        p_v = float(np.sum(w[mask_v]))
        if p_v <= 0.0:
            continue
        p_a_given_v = np.asarray([
            np.sum(w[mask_v & (astar == a)]) / p_v
            for a in range(N)
        ], dtype=np.float64)
        cond += p_v * entropy(p_a_given_v)
    return float(h_a - cond)


SCORERS = {
    "VAR": score_var,
    "EDGE_ENTROPY": score_edge_entropy,
    "ACTION_MI": score_action_mi,
}


def choose_measurement(H, w, selected, policy_name, astar):
    scorer = SCORERS[policy_name]
    best_q = None
    best_score = -float("inf")
    for q in EDGES:
        if q in selected:
            continue
        score = float(scorer(H, w, q, astar))
        if best_q is None or score > best_score + TIE_EPS:
            best_q, best_score = q, score
        elif abs(score - best_score) <= TIE_EPS and q < best_q:
            best_q = q
    return best_q, best_score


def derive_fixed(H, policy_name, astar):
    w0 = np.ones(len(H), dtype=np.float64) / len(H)
    rows = []
    scorer = SCORERS[policy_name]
    for q in EDGES:
        rows.append((float(scorer(H, w0, q, astar)), q))
    rows.sort(key=lambda z: (-z[0], z[1][0], z[1][1]))
    out = []
    remaining = list(rows)
    while remaining and len(out) < BUDGET:
        max_score = remaining[0][0]
        tied = [z for z in remaining if abs(z[0] - max_score) <= TIE_EPS]
        q = min(z[1] for z in tied)
        out.append(q)
        remaining = [z for z in remaining if z[1] != q]
        remaining.sort(key=lambda z: (-z[0], z[1][0], z[1][1]))
    return out


def edge_noise(h, s, q):
    i, j = q
    msg = f"BL002|h={h}|s={s}|i={i}|j={j}".encode("ascii")
    d = hashlib.sha256(msg).digest()
    x = int.from_bytes(d[0:8], "big", signed=False)
    y = int.from_bytes(d[8:16], "big", signed=False)
    u1 = (x + 0.5) / (2 ** 64)
    u2 = (y + 0.5) / (2 ** 64)
    r = math.sqrt(-2.0 * math.log(u1))
    th = 2.0 * math.pi * u2
    return float(r * math.cos(th))


def measurement(T_true, h, s, q):
    i, j = q
    return float(T_true[i, j] + SIGMA * edge_noise(h, s, q))


def run_fixed(H, T_true, h, s, policy_name):
    history = []
    sequence = FIXED[policy_name]
    for q in sequence:
        history.append((q, measurement(T_true, h, s, q)))
    w = posterior_from_history(H, history)
    T_hat = posterior_mean(H, w)
    action = action_from_map(T_hat)
    r, _ = regret(T_true, action)
    return {
        "sequence": list(sequence),
        "posterior": w,
        "map": T_hat,
        "action": action,
        "regret": r,
    }


def run_adaptive(H, T_true, h, s, policy_name, astar):
    history = []
    selected = set()
    sequence = []
    for _ in range(BUDGET):
        w = posterior_from_history(H, history)
        q, _ = choose_measurement(H, w, selected, policy_name, astar)
        y = measurement(T_true, h, s, q)
        history.append((q, y))
        selected.add(q)
        sequence.append(q)
    w = posterior_from_history(H, history)
    T_hat = posterior_mean(H, w)
    action = action_from_map(T_hat)
    r, _ = regret(T_true, action)
    return {
        "sequence": sequence,
        "posterior": w,
        "map": T_hat,
        "action": action,
        "regret": r,
    }


def offdiag_mse(A, B):
    mask = ~np.eye(N, dtype=bool)
    d = A[mask] - B[mask]
    return float(np.mean(d * d))


def t_summary(world_values):
    v = np.asarray(world_values, dtype=np.float64)
    n = len(v)
    mean = float(np.mean(v))
    sd = float(np.std(v, ddof=1))
    se = sd / math.sqrt(n)
    df = n - 1
    if se == 0.0:
        if mean < 0:
            p_one = 0.0
        elif mean > 0:
            p_one = 1.0
        else:
            p_one = 0.5
        upper95 = mean
        ci95 = [mean, mean]
        tstat = float("-inf") if mean < 0 else (float("inf") if mean > 0 else 0.0)
    else:
        tstat = mean / se
        p_one = float(stats.t.cdf(tstat, df=df))
        upper95 = float(mean + stats.t.ppf(0.95, df=df) * se)
        c = float(stats.t.ppf(0.975, df=df) * se)
        ci95 = [mean - c, mean + c]
    return {
        "mean": mean,
        "sd": sd,
        "se": se,
        "t": tstat,
        "df": df,
        "p_one_sided": p_one,
        "upper95_one_sided": upper95,
        "ci95_two_sided": ci95,
    }


def static_audit():
    H = topology_family()
    astar = oracle_actions(H)
    derived = {name: derive_fixed(H, name, astar) for name in POLICY_NAMES}
    audit = {
        "spec_version": SPEC_VERSION,
        "perm_hash_match": hash_compact(PERMS) == PERM_HASH,
        "unique_topology_count": len({H[h].tobytes() for h in range(len(H))}),
        "edge_count": len(EDGES),
        "edges_hash_match": hash_compact(EDGES) == EDGES_HASH,
        "policy_hash_match": hash_compact(list(POLICY_NAMES)) == POLICY_HASH,
        "fixed": {},
    }
    for name in POLICY_NAMES:
        audit["fixed"][name] = {
            "derived": derived[name],
            "exact_match": derived[name] == FIXED[name],
            "hash_match": hash_compact(FIXED[name]) == FIXED_HASH[name],
            "unique_count": len(set(FIXED[name])),
        }
    audit["pass"] = bool(
        audit["perm_hash_match"]
        and audit["unique_topology_count"] == 32
        and audit["edge_count"] == 132
        and audit["edges_hash_match"]
        and audit["policy_hash_match"]
        and all(v["exact_match"] and v["hash_match"] and v["unique_count"] == BUDGET
                for v in audit["fixed"].values())
    )
    return audit


def execute():
    audit = static_audit()
    if not audit["pass"]:
        return {"status": "SPECIFICATION_AUDIT_FAILURE", "audit": audit}

    H = topology_family()
    astar = oracle_actions(H)
    world_delta = []
    world_mapdiff = []
    world_entropydiff = []
    per_rule_world = {name: [] for name in POLICY_NAMES}
    per_rule_map_world = {name: [] for name in POLICY_NAMES}
    divergence = {name: 0 for name in POLICY_NAMES}
    first_divergence = {name: [0] * (BUDGET + 1) for name in POLICY_NAMES}
    total_pairs = 32 * 256

    all_adaptive_regret = []
    all_fixed_regret = []

    for h in range(32):
        T_true = H[h]
        d_h = []
        m_h = []
        e_h = []
        per_rule_d_h = {name: [] for name in POLICY_NAMES}
        per_rule_m_h = {name: [] for name in POLICY_NAMES}

        for s in range(256):
            r_ad = []
            r_fx = []
            m_ad = []
            m_fx = []
            h_ad = []
            h_fx = []

            for name in POLICY_NAMES:
                A = run_adaptive(H, T_true, h, s, name, astar)
                F = run_fixed(H, T_true, h, s, name)

                r_ad.append(A["regret"])
                r_fx.append(F["regret"])
                m_ad.append(offdiag_mse(A["map"], T_true))
                m_fx.append(offdiag_mse(F["map"], T_true))
                h_ad.append(entropy(A["posterior"]))
                h_fx.append(entropy(F["posterior"]))

                dd = A["regret"] - F["regret"]
                mm = offdiag_mse(A["map"], T_true) - offdiag_mse(F["map"], T_true)
                per_rule_d_h[name].append(dd)
                per_rule_m_h[name].append(mm)

                if A["sequence"] != F["sequence"]:
                    divergence[name] += 1
                    fd = next(
                        (k + 1 for k, (qa, qf) in enumerate(zip(A["sequence"], F["sequence"])) if qa != qf),
                        BUDGET + 1,
                    )
                    first_divergence[name][fd] += 1
                else:
                    first_divergence[name][0] += 1

            ra = float(np.mean(r_ad))
            rf = float(np.mean(r_fx))
            ma = float(np.mean(m_ad))
            mf = float(np.mean(m_fx))
            ea = float(np.mean(h_ad))
            ef = float(np.mean(h_fx))

            all_adaptive_regret.append(ra)
            all_fixed_regret.append(rf)
            d_h.append(ra - rf)
            m_h.append(ma - mf)
            e_h.append(ea - ef)

        world_delta.append(float(np.mean(d_h)))
        world_mapdiff.append(float(np.mean(m_h)))
        world_entropydiff.append(float(np.mean(e_h)))
        for name in POLICY_NAMES:
            per_rule_world[name].append(float(np.mean(per_rule_d_h[name])))
            per_rule_map_world[name].append(float(np.mean(per_rule_m_h[name])))

    primary = t_summary(world_delta)
    mapdiag = t_summary(world_mapdiff)
    entdiag = t_summary(world_entropydiff)

    any_divergence = any(divergence[name] > 0 for name in POLICY_NAMES)
    if primary["upper95_one_sided"] < 0.0:
        status = "ACTIVE_SURVEYING_ADDS_ALLOCATION_VALUE"
    elif not any_divergence:
        status = "ADAPTIVITY_NOT_EXPRESSED"
    elif mapdiag["upper95_one_sided"] >= 0.0:
        status = "ADAPTIVE_MEASUREMENT_NO_DEMONSTRATED_TOPOLOGY_GAIN"
    else:
        status = "TOPOLOGY_GAIN_WITHOUT_ALLOCATION_GAIN"

    return {
        "status": status,
        "audit": audit,
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": __import__("scipy").__version__,
            "platform": platform.platform(),
        },
        "family": {
            "worlds": 32,
            "noise_seeds_per_world": 256,
            "paired_specimens": 8192,
            "measurement_budget": BUDGET,
            "candidate_edges": len(EDGES),
            "adaptive_rules": list(POLICY_NAMES),
        },
        "primary": primary,
        "Delta_BL2": float(np.mean(world_delta)),
        "regret": {
            "adaptive_family_mean": float(np.mean(all_adaptive_regret)),
            "fixed_family_mean": float(np.mean(all_fixed_regret)),
        },
        "topology_diagnostic": {
            "map_mse_difference": mapdiag,
            "posterior_entropy_difference_adaptive_minus_fixed": entdiag,
        },
        "per_rule_descriptive": {
            name: {
                "allocation_delta": t_summary(per_rule_world[name]),
                "map_mse_delta": t_summary(per_rule_map_world[name]),
                "sequence_divergence_count": divergence[name],
                "sequence_divergence_fraction": divergence[name] / total_pairs,
                "first_divergence_histogram": first_divergence[name],
            }
            for name in POLICY_NAMES
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Execute the frozen BL-002 scientific family. Omit for static specification audit only.",
    )
    args = parser.parse_args()

    if not args.execute:
        audit = static_audit()
        print(json.dumps({
            "status": "DESIGN_AUDIT_PASS_NOT_EXECUTED" if audit["pass"] else "SPECIFICATION_AUDIT_FAILURE",
            "audit": audit,
        }, indent=2, sort_keys=True))
        return 0 if audit["pass"] else 2

    result = execute()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] != "SPECIFICATION_AUDIT_FAILURE" else 2


if __name__ == "__main__":
    raise SystemExit(main())
