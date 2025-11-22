import heapq
from math import inf
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        min_heap = []
        min_sums = [0] * (2 * n + 1)
        min_heap_sum = 0

        # Build the min_sums from left to right
        for i in range(2 * n):
            heapq.heappush(min_heap, -nums[i])
            min_heap_sum += nums[i]
            if len(min_heap) > n:
                val = -heapq.heappop(min_heap)
                min_heap_sum -= val
            if len(min_heap) == n:
                min_sums[i] = min_heap_sum

        max_heap = []
        max_sums = [0] * (2 * n + 1)
        max_heap_sum = 0

        # Build the max_sums from right to left
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(max_heap, nums[i])
            max_heap_sum += nums[i]
            if len(max_heap) > n:
                val = heapq.heappop(max_heap)
                max_heap_sum -= val
            if len(max_heap) == n:
                max_sums[i] = max_heap_sum

        min_diff = inf
        for i in range(n - 1, 2 * n):
            candidate_diff = min_sums[i] - max_sums[i + 1]
            if candidate_diff < min_diff:
                min_diff = candidate_diff

        return min_diff