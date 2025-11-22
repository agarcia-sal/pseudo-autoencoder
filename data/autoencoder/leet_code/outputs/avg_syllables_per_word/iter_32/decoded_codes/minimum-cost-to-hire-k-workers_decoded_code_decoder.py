import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted(((w / q, q) for q, w in zip(quality, wage)), key=lambda x: x[0])
        max_heap = []
        total_quality = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                removed_quality = heapq.heappop(max_heap)
                total_quality += removed_quality  # removed_quality is negative, so this subtracts quality

            if len(max_heap) == k:
                cost = total_quality * ratio
                if cost < min_cost:
                    min_cost = cost

        return min_cost