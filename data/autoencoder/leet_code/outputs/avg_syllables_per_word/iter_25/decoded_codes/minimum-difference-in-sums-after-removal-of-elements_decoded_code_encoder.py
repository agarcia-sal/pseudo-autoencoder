import heapq
from math import inf
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        min_heap = []
        min_sums = [0] * (2 * n + 1)

        # Process first 2n elements to find minimum sums for left partition
        for i in range(2 * n):
            heapq.heappush(min_heap, -nums[i])
            if len(min_heap) > n:
                heapq.heappop(min_heap)
            if len(min_heap) == n:
                min_sums[i] = -sum(min_heap)

        max_heap = []
        max_sums = [0] * (2 * n + 1)

        # Process last 2n elements to find maximum sums for right partition
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(max_heap, nums[i])
            if len(max_heap) > n:
                heapq.heappop(max_heap)
            if len(max_heap) == n:
                max_sums[i] = sum(max_heap)

        min_diff = inf

        # Compute minimal difference
        for i in range(n - 1, 2 * n):
            diff = min_sums[i] - max_sums[i + 1]
            if diff < min_diff:
                min_diff = diff

        return min_diff