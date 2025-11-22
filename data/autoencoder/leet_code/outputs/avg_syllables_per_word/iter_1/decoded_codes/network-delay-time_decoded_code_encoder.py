import heapq
import math

def network_delay_time(times, n, k):
    graph = [[] for _ in range(n+1)]
    for u, v, w in times:
        graph[u].append((v, w))

    dist = [math.inf] * (n+1)
    dist[k] = 0

    min_heap = [(0, k)]
    while min_heap:
        cur_d, node = heapq.heappop(min_heap)
        if cur_d > dist[node]:
            continue
        for nbr, w in graph[node]:
            d = cur_d + w
            if d < dist[nbr]:
                dist[nbr] = d
                heapq.heappush(min_heap, (d, nbr))

    max_t = max(dist[1:])
    return max_t if max_t != math.inf else -1