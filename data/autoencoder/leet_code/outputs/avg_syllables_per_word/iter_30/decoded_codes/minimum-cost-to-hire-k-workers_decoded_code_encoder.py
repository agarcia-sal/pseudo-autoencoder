import heapq
from math import inf
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Create a list of (ratio, quality) pairs and sort by ratio ascending
        workers = sorted(((w/q, q) for q, w in zip(quality, wage)), key=lambda x: x[0])

        max_heap = []
        total_quality = 0
        min_cost = inf

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                # Pop the largest quality to minimize total quality sum
                total_quality += heapq.heappop(max_heap)  # heapq.heappop returns negative, so adding reduces total_quality

            if len(max_heap) == k:
                cost = total_quality * ratio
                if cost < min_cost:
                    min_cost = cost

        return min_cost