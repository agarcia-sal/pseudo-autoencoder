from collections import defaultdict

def count_pairs(n, edges, queries):
    deg = [0] * (n + 1)
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1

    shared = defaultdict(int)
    for u, v in edges:
        if u > v:
            u, v = v, u
        shared[(u, v)] += 1

    sd = sorted(deg[1:])  # skipping index 0 to match nodes 1-based

    res = []
    for q in queries:
        cnt = 0
        l, r = 0, n - 1
        while l < r:
            if sd[l] + sd[r] > q:
                cnt += r - l
                r -= 1
            else:
                l += 1
        for (u, v), c in shared.items():
            s = deg[u] + deg[v]
            if s > q and s - c <= q:
                cnt -= 1
        res.append(cnt)

    return res