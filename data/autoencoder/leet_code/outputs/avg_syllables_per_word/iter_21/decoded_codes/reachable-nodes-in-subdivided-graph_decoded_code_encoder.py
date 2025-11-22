import heapq
from typing import List, Dict, Tuple


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = self.buildGraph(edges, n)
        distances = self.dijkstra(graph, n)
        reachable_nodes = 0
        for dist in distances:
            if dist <= maxMoves:
                reachable_nodes += 1
        used_edges = self.initializeUsedEdges(edges)
        for edge in edges:
            u, v, cnt = edge
            moves_u = max(0, maxMoves - distances[u])
            moves_v = max(0, maxMoves - distances[v])
            reachable_new_nodes = min(cnt, moves_u + moves_v)
            reachable_nodes += reachable_new_nodes
            self.storeUsedEdges(used_edges, u, v, reachable_new_nodes)
        return reachable_nodes

    def buildGraph(self, edges: List[List[int]], n: int) -> Dict[int, List[Tuple[int, int]]]:
        graph = {i: [] for i in range(n)}
        for edge in edges:
            u, v, cnt = edge
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))
        return graph

    def dijkstra(self, graph: Dict[int, List[Tuple[int, int]]], n: int) -> List[int]:
        distances = [float('inf')] * n
        distances[0] = 0
        priority_queue = [(0, 0)]  # (distance, node)
        while priority_queue:
            dist, node = heapq.heappop(priority_queue)
            if dist > distances[node]:
                continue
            for neighbor, cnt in graph[node]:
                new_dist = dist + cnt + 1
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(priority_queue, (new_dist, neighbor))
        return distances

    def initializeUsedEdges(self, edges: List[List[int]]) -> Dict[Tuple[int, int], int]:
        used_edges = {}
        for edge in edges:
            u, v = edge[0], edge[1]
            used_edges[(u, v)] = 0
        return used_edges

    def storeUsedEdges(self, used_edges: Dict[Tuple[int, int], int], u: int, v: int, reachable_new_nodes: int):
        used_edges[(u, v)] = reachable_new_nodes