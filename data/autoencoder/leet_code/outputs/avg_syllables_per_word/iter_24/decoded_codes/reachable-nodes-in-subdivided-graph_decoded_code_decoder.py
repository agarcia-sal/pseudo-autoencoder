import heapq
from math import inf
from collections import defaultdict
from typing import List, Tuple

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(list)  # node -> list of (neighbor, cnt)
        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))

        distances = [inf] * n
        distances[0] = 0
        priority_queue: List[Tuple[int, int]] = [(0, 0)]
        heapq.heapify(priority_queue)

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
            moves_u = max(0, maxMoves - distances[u]) if distances[u] != inf else 0
            moves_v = max(0, maxMoves - distances[v]) if distances[v] != inf else 0
            reachable_new_nodes = min(cnt, moves_u + moves_v)
            reachable_nodes += reachable_new_nodes
            used_edges[(u, v)] = reachable_new_nodes

        return reachable_nodes