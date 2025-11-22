import heapq
from math import inf

class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        max_heap = []
        total_quality = 0
        min_cost = inf
        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q
            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)
            if len(max_heap) == k:
                current_cost = total_quality * ratio
                if current_cost < min_cost:
                    min_cost = current_cost
        return min_cost