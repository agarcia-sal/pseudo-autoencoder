import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Create list of (ratio, quality) pairs
        workers = sorted([(w / q, q) for q, w in zip(quality, wage)])

        max_heap = []
        total_quality = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)  # pop returns negative quality, so adds (-q)

            if len(max_heap) == k:
                candidate_cost = total_quality * ratio
                if candidate_cost < min_cost:
                    min_cost = candidate_cost

        return min_cost