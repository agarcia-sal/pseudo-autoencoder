import heapq
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        min_heap = []
        min_sums = [0] * (2 * n + 1)
        # Use a max heap (by pushing negative) to find sum of smallest n elements in first 2n elements
        current_sum = 0
        for i in range(2 * n):
            heapq.heappush(min_heap, -nums[i])
            current_sum += nums[i]
            if len(min_heap) > n:
                removed = -heapq.heappop(min_heap)
                current_sum -= removed
            if len(min_heap) == n:
                min_sums[i] = current_sum

        max_heap = []
        max_sums = [0] * (2 * n + 1)
        # Use a min heap to find sum of largest n elements in last 2n elements, iterating backward
        current_sum = 0
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(max_heap, nums[i])
            current_sum += nums[i]
            if len(max_heap) > n:
                removed = heapq.heappop(max_heap)
                current_sum -= removed
            if len(max_heap) == n:
                max_sums[i] = current_sum

        min_diff = float('inf')
        for i in range(n - 1, 2 * n):
            diff = min_sums[i] - max_sums[i + 1]
            if diff < min_diff:
                min_diff = diff

        return min_diff