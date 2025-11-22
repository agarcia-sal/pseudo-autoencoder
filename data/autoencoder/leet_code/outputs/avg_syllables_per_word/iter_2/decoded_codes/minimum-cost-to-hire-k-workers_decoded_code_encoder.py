import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted([(w / q, q) for q, w in zip(quality, wage)])

        max_heap = []
        total_quality = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                removed_quality = heapq.heappop(max_heap)
                total_quality += removed_quality  # removed_quality is negative

            if len(max_heap) == k:
                cost = total_quality * ratio
                if cost < min_cost:
                    min_cost = cost

        return min_cost