import heapq
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        min_value = float('inf')

        for num in nums:
            # If num is odd, multiply by 2 to make it even
            if num % 2 == 1:
                num *= 2
            if num < min_value:
                min_value = num
            # Push negative num to simulate max-heap
            heapq.heappush(max_heap, -num)

        min_deviation = float('inf')

        # Continue while the max element is even
        while (-max_heap[0]) % 2 == 0:
            max_value = -heapq.heappop(max_heap)
            min_deviation = min(min_deviation, max_value - min_value)
            max_value //= 2  # halve the max_value
            if max_value < min_value:
                min_value = max_value
            heapq.heappush(max_heap, -max_value)

        # Check deviation one last time with current max
        max_value = -max_heap[0]
        min_deviation = min(min_deviation, max_value - min_value)

        return min_deviation