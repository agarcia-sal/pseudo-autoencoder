import heapq
from collections import defaultdict
from math import inf

def reachable_nodes(edges, maxMoves, n):
    graph = defaultdict(list)
    for u, v, cnt in edges:
        graph[u].append((v, cnt))
        graph[v].append((u, cnt))

    dist = [inf] * n
    dist[0] = 0
    pq = [(0, 0)]  # (dist, node)
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for nbr, cnt in graph[node]:
            nd = d + cnt + 1
            if nd < dist[nbr]:
                dist[nbr] = nd
                heapq.heappush(pq, (nd, nbr))

    res = sum(d <= maxMoves for d in dist)

    for u, v, cnt in edges:
        mu = max(0, maxMoves - dist[u])
        mv = max(0, maxMoves - dist[v])
        res += min(cnt, mu + mv)

    return res