import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        max_heap = []
        total_quality = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                removed_quality = -heapq.heappop(max_heap)
                total_quality -= removed_quality

            if len(max_heap) == k:
                current_cost = total_quality * ratio
                if current_cost < min_cost:
                    min_cost = current_cost

        return min_cost