import heapq
from math import inf

class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 3

        min_heap = []
        min_sums = [0] * (2 * n + 1)
        min_heap_sum = 0
        for i in range(2 * n):
            # Push negative to simulate max-heap behavior with min-heap
            heapq.heappush(min_heap, -nums[i])
            min_heap_sum += nums[i]
            if len(min_heap) > n:
                removed = -heapq.heappop(min_heap)
                min_heap_sum -= removed
            if len(min_heap) == n:
                min_sums[i] = min_heap_sum

        max_heap = []
        max_sums = [0] * (2 * n + 1)
        max_heap_sum = 0
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(max_heap, nums[i])
            max_heap_sum += nums[i]
            if len(max_heap) > n:
                removed = heapq.heappop(max_heap)
                max_heap_sum -= removed
            if len(max_heap) == n:
                max_sums[i] = max_heap_sum

        min_diff = inf
        for i in range(n - 1, 2 * n):
            diff = min_sums[i] - max_sums[i + 1]
            if diff < min_diff:
                min_diff = diff

        return min_diff