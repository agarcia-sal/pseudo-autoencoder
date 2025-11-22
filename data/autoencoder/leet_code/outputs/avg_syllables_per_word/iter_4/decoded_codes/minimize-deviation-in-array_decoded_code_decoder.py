import heapq
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        min_value = float('inf')

        for num in nums:
            if num % 2 == 1:
                num *= 2
            if num < min_value:
                min_value = num
            heapq.heappush(max_heap, -num)

        min_deviation = float('inf')

        while (-max_heap[0]) % 2 == 0:
            max_value = -heapq.heappop(max_heap)
            min_deviation = min(min_deviation, max_value - min_value)
            max_value //= 2
            if max_value < min_value:
                min_value = max_value
            heapq.heappush(max_heap, -max_value)

        min_deviation = min(min_deviation, (-max_heap[0]) - min_value)
        return min_deviation