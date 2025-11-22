import heapq
import math
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        min_value = math.inf

        for num in nums:
            # If num is odd, multiply by 2 to make it even
            if num % 2 == 1:
                num *= 2
            if num < min_value:
                min_value = num
            # Push negative num to simulate max-heap
            heapq.heappush(max_heap, -num)

        min_deviation = math.inf

        # While the maximum value is even (top of max_heap is negative, so check sign and parity accordingly)
        while True:
            max_value = -heapq.heappop(max_heap)
            min_deviation = min(min_deviation, max_value - min_value)

            if max_value % 2 == 0:
                max_value //= 2
                if max_value < min_value:
                    min_value = max_value
                heapq.heappush(max_heap, -max_value)
            else:
                # Max value is odd, stop processing
                break

        return min_deviation