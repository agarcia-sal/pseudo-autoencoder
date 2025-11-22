import heapq
from math import inf

class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 3

        min_heap = []
        min_sums = [0] * (2 * n + 1)
        for i in range(2 * n):
            heapq.heappush(min_heap, -nums[i])
            if len(min_heap) > n:
                heapq.heappop(min_heap)
            if len(min_heap) == n:
                min_sums[i] = -sum(min_heap)

        max_heap = []
        max_sums = [0] * (2 * n + 1)
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(max_heap, nums[i])
            if len(max_heap) > n:
                heapq.heappop(max_heap)
            if len(max_heap) == n:
                max_sums[i] = sum(max_heap)

        min_diff = inf
        for i in range(n - 1, 2 * n):
            min_diff = min(min_diff, min_sums[i] - max_sums[i + 1])

        return min_diff