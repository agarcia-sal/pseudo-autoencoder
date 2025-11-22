import heapq
from typing import List

class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def min_operations_to_non_decreasing(nums: List[int]) -> int:
            max_heap = []
            operations = 0
            for num in nums:
                if max_heap and -max_heap[0] > num:
                    max_val = -heapq.heappop(max_heap)
                    operations += max_val - num
                    heapq.heappush(max_heap, -num)
                heapq.heappush(max_heap, -num)
            return operations

        def min_operations_to_non_increasing(nums: List[int]) -> int:
            min_heap = []
            operations = 0
            for num in nums:
                if min_heap and min_heap[0] < num:
                    min_val = heapq.heappop(min_heap)
                    operations += num - min_val
                    heapq.heappush(min_heap, num)
                heapq.heappush(min_heap, num)
            return operations

        return min(min_operations_to_non_decreasing(nums), min_operations_to_non_increasing(nums))