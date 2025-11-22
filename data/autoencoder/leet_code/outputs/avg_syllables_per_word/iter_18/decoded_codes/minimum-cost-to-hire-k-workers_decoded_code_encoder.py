import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Pair each worker's wage/quality ratio with their quality, and sort by ratio
        workers = sorted(((w / q, q) for q, w in zip(quality, wage)), key=lambda x: x[0])

        max_heap = []
        total_quality = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)  # max heap emulated with negation
            total_quality += q

            if len(max_heap) > k:
                removed_quality = heapq.heappop(max_heap)  # smallest element is most negative quality
                total_quality += removed_quality  # removed_quality is negative, so sum decreases

            if len(max_heap) == k:
                possible_cost = total_quality * ratio
                if possible_cost < min_cost:
                    min_cost = possible_cost

        return min_cost