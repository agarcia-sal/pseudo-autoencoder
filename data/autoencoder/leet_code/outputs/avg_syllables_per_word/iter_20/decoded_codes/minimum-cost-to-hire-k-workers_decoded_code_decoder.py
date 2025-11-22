import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted(((w / q, q) for w, q in zip(wage, quality)), key=lambda x: x[0])
        max_heap = []
        total_quality = 0
        min_cost = float('inf')
        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q
            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)
            if len(max_heap) == k:
                min_cost = min(min_cost, total_quality * ratio)
        return min_cost