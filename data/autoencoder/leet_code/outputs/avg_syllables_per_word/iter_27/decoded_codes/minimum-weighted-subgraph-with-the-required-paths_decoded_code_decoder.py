import heapq
from typing import List, Tuple

class Solution:
    def minimumWeight(self, n: int, edges: List[Tuple[int, int, int]], src1: int, src2: int, dest: int) -> int:
        def dijkstra(graph: List[List[Tuple[int, int]]], start: int) -> List[int]:
            distances = [float('inf')] * n
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
            if 0 <= u < n and 0 <= v < n and w >= 0:
                graph[u].append((v, w))
                reverse_graph[v].append((u, w))

        dist_from_src1 = dijkstra(graph, src1)
        dist_from_src2 = dijkstra(graph, src2)
        dist_to_dest = dijkstra(reverse_graph, dest)

        min_weight = float('inf')
        for i in range(n):
            d1, d2, d3 = dist_from_src1[i], dist_from_src2[i], dist_to_dest[i]
            if d1 != float('inf') and d2 != float('inf') and d3 != float('inf'):
                total = d1 + d2 + d3
                if total < min_weight:
                    min_weight = total

        return -1 if min_weight == float('inf') else min_weight