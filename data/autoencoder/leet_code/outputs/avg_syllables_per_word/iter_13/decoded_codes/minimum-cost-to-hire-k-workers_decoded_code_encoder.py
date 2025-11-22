from heapq import heappush, heappop, heapify
from math import inf
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])

        max_heap = []
        total_quality = 0
        min_cost = inf

        for ratio, q in workers:
            heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                total_quality += heappop(max_heap)  # since heappop returns negative quality, add it
            if len(max_heap) == k:
                min_cost = min(min_cost, total_quality * ratio)

        return min_cost