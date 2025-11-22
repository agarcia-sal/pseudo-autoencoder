import heapq
import math

class Solution:
    def minimumDeviation(self, nums):
        max_heap = []
        min_value = math.inf

        for num in nums:
            # If num is odd, multiply by 2 to make it even
            if num % 2 == 1:
                num *= 2
            if num < min_value:
                min_value = num
            # Push negative num to create a max heap using heapq (min heap)
            heapq.heappush(max_heap, -num)

        min_deviation = math.inf

        # While the maximum element is even, try to reduce it
        while (-max_heap[0]) % 2 == 0:
            max_value = -heapq.heappop(max_heap)
            min_deviation = min(min_deviation, max_value - min_value)
            max_value //= 2
            if max_value < min_value:
                min_value = max_value
            heapq.heappush(max_heap, -max_value)

        # Final check after no more even max values can be halved
        min_deviation = min(min_deviation, -max_heap[0] - min_value)

        return min_deviation