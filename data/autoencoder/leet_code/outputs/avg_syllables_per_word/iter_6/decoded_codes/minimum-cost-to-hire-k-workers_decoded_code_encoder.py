import heapq
import math

class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted((w/q, q) for q, w in zip(quality, wage))
        max_heap = []
        total_quality = 0
        min_cost = math.inf

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)  # heappop returns negative q

            if len(max_heap) == k:
                min_cost = min(min_cost, total_quality * ratio)

        return min_cost