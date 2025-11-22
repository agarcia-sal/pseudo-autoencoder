import heapq
from math import inf
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Pair each worker's ratio (wage/quality) with their quality, sort by ratio ascending
        workers = sorted(((w / q, q) for w, q in zip(wage, quality)), key=lambda x: x[0])

        max_heap = []
        total_quality = 0
        min_cost = inf

        for ratio, q in workers:
            # Push quality as negative to simulate max-heap
            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                # Remove worker with highest quality to keep group size k
                total_quality += heapq.heappop(max_heap)  # Note: pop returns negative quality

            if len(max_heap) == k:
                min_cost = min(min_cost, total_quality * ratio)

        return min_cost