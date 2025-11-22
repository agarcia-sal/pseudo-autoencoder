import heapq
from typing import List, Tuple, Dict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        dist: Dict[int, float] = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0

        min_heap: List[Tuple[int, int]] = [(0, k)]
        heapq.heapify(min_heap)

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
        if max_time == float('inf'):
            return -1
        else:
            return max_time