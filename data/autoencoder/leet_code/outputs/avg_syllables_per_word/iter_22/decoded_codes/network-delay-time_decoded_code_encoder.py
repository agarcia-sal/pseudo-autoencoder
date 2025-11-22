import heapq
from math import inf
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {i: inf for i in range(1, n + 1)}
        dist[k] = 0
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
        return max_time if max_time != inf else -1