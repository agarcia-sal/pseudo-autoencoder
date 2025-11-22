import heapq
from typing import List, Optional


class Solution:
    def convertArray(self, nums: List[int]) -> int:

        def min_operations_to_non_decreasing(nums: List[int]) -> int:
            max_heap: List[int] = []
            operations = 0
            for num in nums:
                if max_heap and -max_heap[0] > num:
                    removed = -heapq.heappop(max_heap)
                    operations += removed - num
                    heapq.heappush(max_heap, -num)
                heapq.heappush(max_heap, -num)
            return operations

        def min_operations_to_non_increasing(nums: List[int]) -> int:
            min_heap: List[int] = []
            operations = 0
            for num in nums:
                if min_heap and min_heap[0] < num:
                    removed = heapq.heappop(min_heap)
                    operations += num - removed
                    heapq.heappush(min_heap, num)
                heapq.heappush(min_heap, num)
            return operations

        return min(min_operations_to_non_decreasing(nums), min_operations_to_non_increasing(nums))