import heapq
from math import inf
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(w / q, q) for q, w in zip(quality, wage)])
        max_heap = []
        total_quality = 0
        min_cost = inf

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)  # heap pop returns negative value, adding restores correct sum

            if len(max_heap) == k:
                min_cost = min(min_cost, total_quality * ratio)

        return min_cost