from heapq import heappush, heappop
from math import inf

class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 3

        min_heap = []
        min_sums = [0] * (2 * n + 1)

        # Process first 2*n elements to find min sums of size n
        for index in range(2 * n):
            heappush(min_heap, -nums[index])
            if len(min_heap) > n:
                heappop(min_heap)
            if len(min_heap) == n:
                min_sums[index] = -sum(min_heap)

        max_heap = []
        max_sums = [0] * (2 * n + 1)

        # Process last 2*n elements in reverse to find max sums of size n
        for index in range(3 * n - 1, n - 1, -1):
            heappush(max_heap, nums[index])
            if len(max_heap) > n:
                heappop(max_heap)
            if len(max_heap) == n:
                max_sums[index] = sum(max_heap)

        min_diff = inf
        for index in range(n - 1, 2 * n):
            diff = min_sums[index] - max_sums[index + 1]
            if diff < min_diff:
                min_diff = diff

        return min_diff