import heapq
from math import inf
from typing import List

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        def dijkstra(graph: List[List[List[int]]], start: int) -> List[int]:
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
            d1 = dist_from_src1[i]
            d2 = dist_from_src2[i]
            d3 = dist_to_dest[i]
            if d1 != inf and d2 != inf and d3 != inf:
                candidate = d1 + d2 + d3
                if candidate < min_weight:
                    min_weight = candidate

        return -1 if min_weight == inf else min_weight