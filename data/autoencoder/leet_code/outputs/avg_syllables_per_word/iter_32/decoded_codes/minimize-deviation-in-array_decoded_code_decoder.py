import heapq
from math import inf
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        min_value = inf

        # Normalize all numbers: if odd, multiply by 2 to make even
        for num in nums:
            if num % 2 == 1:
                num *= 2
            min_value = min(min_value, num)
            # Push negative to simulate max heap using heapq (a min heap)
            heapq.heappush(max_heap, -num)

        min_deviation = inf

        # While the max element is even, we can divide it by 2 and possibly reduce deviation
        while True:
            max_value = -heapq.heappop(max_heap)
            min_deviation = min(min_deviation, max_value - min_value)

            if max_value % 2 == 0:
                max_value //= 2
                min_value = min(min_value, max_value)
                heapq.heappush(max_heap, -max_value)
            else:
                # If max value is odd, we cannot reduce it further, stop
                break

        # After loop, min_deviation is best found deviation
        return min_deviation