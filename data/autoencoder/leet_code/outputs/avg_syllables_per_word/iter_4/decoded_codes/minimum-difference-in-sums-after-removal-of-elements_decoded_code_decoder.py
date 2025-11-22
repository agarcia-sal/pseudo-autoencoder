from typing import List
import heapq
import math

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        min_heap = []
        min_sums = [0] * (2 * n + 1)
        sum_min_heap = 0

        for i in range(2 * n):
            # Push negative to simulate max-heap
            heapq.heappush(min_heap, -nums[i])
            sum_min_heap += nums[i]
            if len(min_heap) > n:
                removed = -heapq.heappop(min_heap)
                sum_min_heap -= removed
            if len(min_heap) == n:
                min_sums[i] = sum_min_heap

        max_heap = []
        max_sums = [0] * (2 * n + 1)
        sum_max_heap = 0

        # min-heap naturally supports smallest elements, we want max heap
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(max_heap, nums[i])
            sum_max_heap += nums[i]
            if len(max_heap) > n:
                removed = heapq.heappop(max_heap)
                sum_max_heap -= removed
            if len(max_heap) == n:
                max_sums[i] = sum_max_heap

        min_diff = math.inf
        for i in range(n - 1, 2 * n):
            current_diff = min_sums[i] - max_sums[i + 1]
            if current_diff < min_diff:
                min_diff = current_diff

        return min_diff