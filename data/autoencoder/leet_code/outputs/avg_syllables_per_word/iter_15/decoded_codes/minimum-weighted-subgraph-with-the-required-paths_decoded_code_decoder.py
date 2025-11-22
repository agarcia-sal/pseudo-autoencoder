import heapq
from math import inf
from typing import List, Tuple

class Solution:
    def minimumWeight(self, n: int, edges: List[Tuple[int, int, int]], src1: int, src2: int, dest: int) -> int:
        def dijkstra(graph: List[List[Tuple[int, int]]], start: int) -> List[int]:
            distances = [inf] * n
            distances[start] = 0
            heap = [(0, start)]

            while heap:
                current_distance, current_node = heapq.heappop(heap)
                if current_distance > distances[current_node]:
                    continue
                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(heap, (distance, neighbor))
            return distances

        graph = [[] for _ in range(n)]
        reverse_graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            reverse_graph[v].append((u, w))

        dist_from_src1 = dijkstra(graph, src1)
        dist_from_src2 = dijkstra(graph, src2)
        dist_to_dest = dijkstra(reverse_graph, dest)

        min_weight = inf
        for i in range(n):
            if dist_from_src1[i] != inf and dist_from_src2[i] != inf and dist_to_dest[i] != inf:
                candidate_weight = dist_from_src1[i] + dist_from_src2[i] + dist_to_dest[i]
                if candidate_weight < min_weight:
                    min_weight = candidate_weight

        return -1 if min_weight == inf else min_weight