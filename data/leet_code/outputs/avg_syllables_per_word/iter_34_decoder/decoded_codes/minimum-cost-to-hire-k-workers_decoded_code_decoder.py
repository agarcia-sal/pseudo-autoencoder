import heapq
from math import inf

class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        # Create pairs of (wage/quality ratio, quality)
        workers = [(w / q, q) for q, w in zip(quality, wage)]
        # Sort workers by their ratio
        workers.sort(key=lambda x: x[0])

        max_heap = []
        total_quality = 0
        min_cost = inf

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                removed = heapq.heappop(max_heap)
                total_quality += removed  # removed is negative, so this subtracts 

            if len(max_heap) == k:
                current_cost = total_quality * ratio
                if current_cost < min_cost:
                    min_cost = current_cost

        return min_cost