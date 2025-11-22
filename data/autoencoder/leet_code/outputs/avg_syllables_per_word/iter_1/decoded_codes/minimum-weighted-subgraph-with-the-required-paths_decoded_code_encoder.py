import heapq
import math

def dijkstra(g, s):
    n = len(g)
    dist = [math.inf] * n
    dist[s] = 0
    heap = [(0, s)]
    while heap:
        cd, u = heapq.heappop(heap)
        if cd > dist[u]:
            continue
        for v, w in g[u]:
            nd = cd + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

# Assume n, edges, src1, src2, dest are defined
graph = [[] for _ in range(n)]
rev_graph = [[] for _ in range(n)]
for u, v, w in edges:
    graph[u].append((v, w))
    rev_graph[v].append((u, w))

d1 = dijkstra(graph, src1)
d2 = dijkstra(graph, src2)
dt = dijkstra(rev_graph, dest)

res = math.inf
for i in range(n):
    if d1[i] < math.inf and d2[i] < math.inf and dt[i] < math.inf:
        res = min(res, d1[i] + d2[i] + dt[i])

print(res if res < math.inf else -1)