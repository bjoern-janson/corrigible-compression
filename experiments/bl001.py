#!/usr/bin/env python3
import hashlib
import json
import math
import platform

import numpy as np
from scipy import stats

N = 12
D0 = np.array([0.15,0.15,0.20,0.20,0.40,0.40,0.55,0.55,0.70,0.70,0.85,0.85], dtype=np.float64)
ETA = 0.25
SIGMA = 0.08
PERMS = [(6, 3, 7, 5, 1, 4, 0, 10, 8, 11, 9, 2), (5, 4, 3, 7, 6, 1, 2, 10, 9, 11, 8, 0), (7, 2, 9, 0, 1, 10, 5, 8, 11, 3, 6, 4), (4, 10, 3, 11, 8, 6, 7, 0, 9, 5, 2, 1), (1, 11, 6, 7, 0, 4, 5, 3, 9, 2, 10, 8), (2, 11, 6, 4, 0, 5, 3, 1, 7, 8, 9, 10), (5, 8, 6, 3, 11, 2, 0, 4, 7, 10, 1, 9), (8, 0, 9, 10, 7, 2, 4, 1, 5, 6, 11, 3), (10, 1, 3, 11, 4, 7, 5, 9, 6, 8, 2, 0), (5, 2, 0, 4, 10, 1, 8, 6, 9, 7, 11, 3), (10, 5, 0, 1, 9, 3, 6, 7, 8, 4, 11, 2), (11, 10, 7, 3, 6, 1, 5, 0, 2, 8, 4, 9), (8, 0, 10, 5, 1, 7, 2, 9, 11, 4, 6, 3), (11, 1, 3, 5, 9, 2, 6, 8, 0, 4, 7, 10), (1, 9, 8, 6, 3, 0, 2, 7, 5, 10, 4, 11), (3, 7, 0, 6, 1, 10, 2, 4, 9, 5, 11, 8), (10, 8, 2, 1, 4, 6, 9, 3, 11, 0, 7, 5), (11, 7, 0, 2, 10, 5, 8, 1, 3, 6, 9, 4), (11, 4, 9, 2, 1, 6, 3, 7, 8, 10, 5, 0), (3, 1, 4, 8, 2, 11, 7, 10, 0, 6, 5, 9), (7, 1, 9, 2, 10, 11, 4, 0, 6, 5, 3, 8), (7, 11, 6, 9, 2, 4, 1, 3, 10, 0, 8, 5), (11, 4, 0, 2, 6, 1, 8, 7, 10, 9, 3, 5), (1, 9, 3, 2, 5, 11, 7, 8, 6, 4, 0, 10), (6, 3, 4, 9, 7, 1, 2, 5, 8, 11, 10, 0), (10, 6, 8, 3, 4, 1, 0, 11, 2, 5, 9, 7), (6, 3, 9, 4, 1, 10, 5, 0, 11, 8, 2, 7), (8, 1, 9, 6, 2, 7, 0, 4, 11, 5, 3, 10), (7, 10, 5, 1, 4, 3, 0, 8, 2, 9, 11, 6), (5, 2, 4, 9, 3, 7, 11, 0, 8, 10, 1, 6), (10, 8, 5, 1, 7, 11, 3, 0, 6, 4, 9, 2), (11, 8, 0, 1, 10, 2, 9, 6, 5, 7, 4, 3)]
Q8 = [(6, 3), (9, 2), (10, 5), (9, 3), (2, 10), (4, 9), (1, 9), (7, 10)]
PERM_HASH = "a599a5e21f91ec76a55fee4df5551a5d3ea459d2f6aed8572e18c1c6358ca3c3"
Q8_HASH = "71e0fbff2485edbd5e6cbe1244398a4f24377f84da3e3f96e942e7f793f963b5"
TIE_EPS = 1e-15


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


def hash_compact(obj):
    return hashlib.sha256(json.dumps(obj, separators=(",", ":")).encode("utf-8")).hexdigest()


def derive_q8(H):
    rows = []
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            v = float(np.var(H[:, i, j], ddof=0))
            rows.append((v, i, j))
    rows.sort(key=lambda x: (-x[0], x[1], x[2]))
    return [(i, j) for _, i, j in rows[:8]]


def normal_bank(h, s):
    out = []
    for b in range(4):
        msg = f"BL001|h={h}|s={s}|b={b}".encode("ascii")
        d = hashlib.sha256(msg).digest()
        x = int.from_bytes(d[0:8], "big", signed=False)
        y = int.from_bytes(d[8:16], "big", signed=False)
        u1 = (x + 0.5) / (2 ** 64)
        u2 = (y + 0.5) / (2 ** 64)
        r = math.sqrt(-2.0 * math.log(u1))
        th = 2.0 * math.pi * u2
        out.append(r * math.cos(th))
        out.append(r * math.sin(th))
    return np.array(out, dtype=np.float64)


def gain(T_est, action):
    D = D0.copy()
    for j in range(N):
        if j == action:
            D[j] = D[j] + ETA * (1.0 - D[j])
        else:
            D[j] = D[j] + ETA * T_est[action, j] * (1.0 - D[j])
    return float(np.mean(D))


def action_from_map(T_est):
    vals = [gain(T_est, i) for i in range(N)]
    return int(np.argmax(np.asarray(vals, dtype=np.float64)))


def regret(T_true, action):
    oracle_vals = np.array([gain(T_true, i) for i in range(N)], dtype=np.float64)
    oracle_action = int(np.argmax(oracle_vals))
    return float(oracle_vals[oracle_action] - oracle_vals[action]), oracle_action


def posterior_mean(H, y):
    pred = np.array([[H[h, i, j] for (i, j) in Q8] for h in range(len(H))], dtype=np.float64)
    resid = pred - y[None, :]
    logw = -0.5 * np.sum((resid / SIGMA) ** 2, axis=1)
    logw -= np.max(logw)
    w = np.exp(logw)
    w /= np.sum(w)
    That = np.tensordot(w, H, axes=(0, 0))
    return That, w


def raw_map(H, y):
    M = np.mean(H, axis=0).copy()
    for k, (i, j) in enumerate(Q8):
        M[i, j] = y[k]
    return M


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


def main():
    H = topology_family()

    audit = {}
    audit["perm_hash_match"] = hash_compact(PERMS) == PERM_HASH
    audit["q8_hash_match"] = hash_compact(Q8) == Q8_HASH
    audit["unique_topology_count"] = len({H[h].tobytes() for h in range(len(H))})
    audit["derived_q8"] = derive_q8(H)
    audit["q8_exact_match"] = audit["derived_q8"] == Q8
    sigs = [tuple(H[h, i, j] for (i, j) in Q8) for h in range(len(H))]
    audit["unique_noiseless_q8_signatures"] = len(set(sigs))
    audit_pass = (
        audit["perm_hash_match"]
        and audit["q8_hash_match"]
        and audit["unique_topology_count"] == 32
        and audit["q8_exact_match"]
        and audit["unique_noiseless_q8_signatures"] == 32
    )
    audit["pass"] = bool(audit_pass)

    if not audit_pass:
        print(json.dumps({"status": "MEASUREMENT_INTERFACE_FAILURE", "audit": audit}, indent=2, sort_keys=True))
        return 2

    raw_regrets = []
    topo_regrets = []
    deltas = []
    topo_mses = []
    raw_mses = []
    map_diffs = []
    world_delta = []
    world_mapdiff = []
    map_correct = 0

    for h in range(32):
        Ttrue = H[h]
        d_h = []
        m_h = []
        for s in range(256):
            eps = SIGMA * normal_bank(h, s)
            y = np.array([Ttrue[i, j] for (i, j) in Q8], dtype=np.float64) + eps
            Ttopo, post = posterior_mean(H, y)
            Traw = raw_map(H, y)

            atop = action_from_map(Ttopo)
            araw = action_from_map(Traw)

            rtop, _ = regret(Ttrue, atop)
            rraw, _ = regret(Ttrue, araw)
            delta = rtop - rraw

            mt = offdiag_mse(Ttopo, Ttrue)
            mr = offdiag_mse(Traw, Ttrue)
            md = mt - mr

            topo_regrets.append(rtop)
            raw_regrets.append(rraw)
            deltas.append(delta)
            topo_mses.append(mt)
            raw_mses.append(mr)
            map_diffs.append(md)
            d_h.append(delta)
            m_h.append(md)
            if int(np.argmax(post)) == h:
                map_correct += 1

        world_delta.append(float(np.mean(d_h)))
        world_mapdiff.append(float(np.mean(m_h)))

    primary = t_summary(world_delta)
    mapdiag = t_summary(world_mapdiff)
    Rtop = float(np.mean(topo_regrets))
    Rraw = float(np.mean(raw_regrets))
    delta = float(np.mean(deltas))
    wins = sum(1 for d in deltas if d < -TIE_EPS)
    ties = sum(1 for d in deltas if abs(d) <= TIE_EPS)
    losses = sum(1 for d in deltas if d > TIE_EPS)

    if primary["upper95_one_sided"] < 0.0:
        status = "TOPOLOGY_ADDS_ALLOCATION_VALUE"
    elif mapdiag["upper95_one_sided"] >= 0.0:
        status = "TOPOLOGY_INFERENCE_FAILS"
    else:
        status = "ALLOCATION_FAILURE"

    result = {
        "status": status,
        "audit": audit,
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": __import__("scipy").__version__,
            "platform": platform.platform(),
        },
        "family": {"worlds": 32, "noise_seeds_per_world": 256, "paired_specimens": 8192},
        "primary": primary,
        "Delta": delta,
        "regret": {
            "topo_mean": Rtop,
            "raw_mean": Rraw,
            "topo_median": float(np.median(topo_regrets)),
            "raw_median": float(np.median(raw_regrets)),
            "win_count": wins,
            "tie_count": ties,
            "loss_count": losses,
            "win_fraction": wins / 8192,
            "tie_fraction": ties / 8192,
            "loss_fraction": losses / 8192,
            "oracle_gap_fraction_closed": ((Rraw - Rtop) / Rraw if Rraw > 0 else None),
        },
        "map_diagnostic": {
            **mapdiag,
            "topo_mse_mean": float(np.mean(topo_mses)),
            "raw_mse_mean": float(np.mean(raw_mses)),
            "map_mse_difference_mean": float(np.mean(map_diffs)),
            "map_candidate_MAP_accuracy": map_correct / 8192,
        },
        "claim_ceiling": "Frozen finite-family allocation result only; no adaptive surveying or topology invention.",
        "bl002_designed": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
