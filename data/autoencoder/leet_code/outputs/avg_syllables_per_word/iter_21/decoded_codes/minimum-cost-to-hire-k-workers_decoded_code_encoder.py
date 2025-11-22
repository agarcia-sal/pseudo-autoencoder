from heapq import heappush, heappop

class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted(((w / q, q) for w, q in zip(wage, quality)))
        max_heap = []
        total_quality = 0
        min_cost = float('inf')
        for ratio, q in workers:
            heappush(max_heap, -q)
            total_quality += q
            if len(max_heap) > k:
                total_quality += heappop(max_heap)
            if len(max_heap) == k:
                min_cost = min(min_cost, total_quality * ratio)
        return min_cost