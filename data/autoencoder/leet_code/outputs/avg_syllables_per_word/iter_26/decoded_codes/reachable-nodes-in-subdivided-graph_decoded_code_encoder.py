import heapq
from collections import defaultdict
from math import inf

class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))

        distances = [inf] * n
        distances[0] = 0
        priority_queue = [(0, 0)]  # (distance, node)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node]:
                continue
            for neighbor, cnt in graph[current_node]:
                new_distance = current_distance + cnt + 1
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        reachable_nodes = sum(1 for d in distances if d <= maxMoves)

        used_edges = {}
        for u, v, cnt in edges:
            moves_from_u = max(0, maxMoves - distances[u])
            moves_from_v = max(0, maxMoves - distances[v])
            reachable_new_nodes = min(cnt, moves_from_u + moves_from_v)
            reachable_nodes += reachable_new_nodes
            used_edges[(u, v)] = reachable_new_nodes

        return reachable_nodes