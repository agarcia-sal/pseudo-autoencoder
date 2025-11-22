import heapq
from collections import defaultdict

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))

        distances = [float('inf')] * n
        distances[0] = 0
        pq = [(0, 0)]

        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distances[node]:
                continue
            for neighbor, cnt in graph[node]:
                new_dist = dist + cnt + 1
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        reachable_nodes = sum(1 for d in distances if d <= maxMoves)

        for u, v, cnt in edges:
            moves_u = max(0, maxMoves - distances[u])
            moves_v = max(0, maxMoves - distances[v])
            reachable_new_nodes = min(cnt, moves_u + moves_v)
            reachable_nodes += reachable_new_nodes

        return reachable_nodes