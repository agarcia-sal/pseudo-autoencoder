MOD = 10**9 + 7

from math import comb

def waysToBuildRooms(prev):
    n = len(prev)
    graph = {i: [] for i in range(n)}
    for r in range(1, n):
        graph[prev[r]].append(r)

    def dp(node):
        if not graph[node]:
            return (1, 1)
        ways = 1
        size = 1
        children = [dp(c) for c in graph[node]]
        for w, s in children:
            ways = ways * comb(size + s - 1, s) * w % MOD
            size += s
        return (ways, size)

    return dp(0)[0]