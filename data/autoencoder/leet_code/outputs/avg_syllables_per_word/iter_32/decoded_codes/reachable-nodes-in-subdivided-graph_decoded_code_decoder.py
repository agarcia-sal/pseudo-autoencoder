import heapq
from typing import List, Tuple, Dict

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # Build the graph as an adjacency list: node -> list of (neighbor, edge_weight)
        graph: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}
        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))

        # distances[i] = shortest distance from node 0 to node i
        distances = [float('inf')] * n
        distances[0] = 0

        # Min-heap priority queue for Dijkstra's algorithm (distance, node)
        priority_queue: List[Tuple[int, int]] = [(0, 0)]

        while priority_queue:
            dist, node = heapq.heappop(priority_queue)
            if dist > distances[node]:
                continue

            for neighbor, cnt in graph[node]:
                new_dist = dist + cnt + 1  # distance to neighbor going through this edge
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(priority_queue, (new_dist, neighbor))

        reachable_nodes = 0
        for d in distances:
            if d <= maxMoves:
                reachable_nodes += 1

        used_edges: Dict[Tuple[int,int], int] = {}
        for u, v, cnt in edges:
            moves_u = max(0, maxMoves - distances[u]) if distances[u] != float('inf') else 0
            moves_v = max(0, maxMoves - distances[v]) if distances[v] != float('inf') else 0
            reachable_new_nodes = min(cnt, moves_u + moves_v)
            reachable_nodes += reachable_new_nodes
            used_edges[(u,v)] = reachable_new_nodes

        return reachable_nodes