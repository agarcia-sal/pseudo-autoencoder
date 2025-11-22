import heapq
from typing import List
import math

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        min_value = math.inf

        # Convert all odd numbers to even by doubling, and find the minimum value
        for num in nums:
            if num % 2 == 1:
                num *= 2
            if num < min_value:
                min_value = num
            heapq.heappush(max_heap, -num)

        min_deviation = math.inf

        # Reduce the maximum element while it is even
        while True:
            max_value = -heapq.heappop(max_heap)
            min_deviation = min(min_deviation, max_value - min_value)

            if max_value % 2 == 0:
                max_value //= 2
                if max_value < min_value:
                    min_value = max_value
                heapq.heappush(max_heap, -max_value)
            else:
                break

        # Check deviation with the current maximum again
        if max_heap:
            current_max = -max_heap[0]
            min_deviation = min(min_deviation, current_max - min_value)

        return min_deviation