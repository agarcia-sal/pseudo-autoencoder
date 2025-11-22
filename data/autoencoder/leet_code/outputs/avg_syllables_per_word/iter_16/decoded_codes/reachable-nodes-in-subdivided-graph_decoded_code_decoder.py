import heapq
from math import inf
from collections import defaultdict

class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        graph = {i: [] for i in range(n)}
        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))

        distances = [inf] * n
        distances[0] = 0
        priority_queue = [(0, 0)]

        while priority_queue:
            dist, node = heapq.heappop(priority_queue)
            if dist > distances[node]:
                continue

            for neighbor, cnt in graph[node]:
                new_dist = dist + cnt + 1
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(priority_queue, (new_dist, neighbor))

        reachable_nodes = sum(1 for d in distances if d <= maxMoves)

        used_edges = {}
        for u, v, cnt in edges:
            moves_u = max(0, maxMoves - distances[u])
            moves_v = max(0, maxMoves - distances[v])
            reachable_new_nodes = min(cnt, moves_u + moves_v)
            reachable_nodes += reachable_new_nodes
            used_edges[(u, v)] = reachable_new_nodes

        return reachable_nodes