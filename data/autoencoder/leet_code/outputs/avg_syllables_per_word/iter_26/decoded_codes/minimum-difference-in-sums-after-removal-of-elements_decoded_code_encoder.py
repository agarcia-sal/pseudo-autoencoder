import heapq
from math import inf

class Solution:
    def minimumDifference(self, list_of_numbers):
        n = len(list_of_numbers) // 3

        min_heap = []
        min_sums = [0] * (2 * n + 1)

        running_sum = 0
        # Build min_sums: prefix sums of smallest n elements using max heap simulated by negation
        for i in range(2 * n):
            heapq.heappush(min_heap, -list_of_numbers[i])
            running_sum += list_of_numbers[i]
            if len(min_heap) > n:
                removed = -heapq.heappop(min_heap)
                running_sum -= removed
            if len(min_heap) == n:
                min_sums[i] = running_sum

        max_heap = []
        max_sums = [0] * (2 * n + 1)

        running_sum = 0
        # Build max_sums: suffix sums of largest n elements using min heap directly
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(max_heap, list_of_numbers[i])
            running_sum += list_of_numbers[i]
            if len(max_heap) > n:
                removed = heapq.heappop(max_heap)
                running_sum -= removed
            if len(max_heap) == n:
                max_sums[i] = running_sum

        min_diff = inf

        for i in range(n - 1, 2 * n):
            diff = min_sums[i] - max_sums[i + 1]
            if diff < min_diff:
                min_diff = diff

        return min_diff