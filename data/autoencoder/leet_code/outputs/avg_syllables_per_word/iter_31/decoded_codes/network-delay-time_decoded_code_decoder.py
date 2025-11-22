from typing import List
from heapq import heappush, heappop
from collections import defaultdict
import math

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for element in times:
            u, v, w = element
            graph[u].append((v, w))

        dist = {i: math.inf for i in range(1, n + 1)}
        dist[k] = 0

        min_heap = [(0, k)]

        while min_heap:
            current_dist, node = heappop(min_heap)
            if current_dist > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heappush(min_heap, (distance, neighbor))

        max_time = max(dist.values())
        return -1 if max_time == math.inf else max_time