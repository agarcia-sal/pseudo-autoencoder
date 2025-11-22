from typing import List, Dict, Tuple
import heapq
import math

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.construct_graph(times, n)
        dist = self.initialize_distances(n, k)

        min_heap = [(0, k)]
        while min_heap:
            current_dist, node = heapq.heappop(min_heap)

            if current_dist > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        max_time = max(dist.values())
        if max_time == math.inf:
            return -1
        else:
            return max_time

    def construct_graph(self, times: List[List[int]], n: int) -> Dict[int, List[Tuple[int, int]]]:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        return graph

    def initialize_distances(self, n: int, k: int) -> Dict[int, float]:
        dist = {i: math.inf for i in range(1, n + 1)}
        dist[k] = 0
        return dist