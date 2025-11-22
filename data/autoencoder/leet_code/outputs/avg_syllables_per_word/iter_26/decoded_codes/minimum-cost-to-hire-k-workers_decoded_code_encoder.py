import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Pair each worker's ratio (wage/quality) with their quality and sort by ratio
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])

        max_heap = []
        total_quality = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)  # Push negative quality to simulate max heap
            total_quality += q

            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)  # remove the largest quality (negative) and add back
            if len(max_heap) == k:
                min_cost = min(min_cost, total_quality * ratio)

        return min_cost