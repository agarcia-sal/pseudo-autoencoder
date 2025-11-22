import heapq
from typing import List

class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def min_operations_to_non_decreasing(nums: List[int]) -> int:
            max_heap = []
            operations = 0
            for num in nums:
                while max_heap and -max_heap[0] > num:
                    largest = -heapq.heappop(max_heap)
                    operations += largest - num
                heapq.heappush(max_heap, -num)
            return operations

        def min_operations_to_non_increasing(nums: List[int]) -> int:
            min_heap = []
            operations = 0
            for num in nums:
                while min_heap and min_heap[0] < num:
                    smallest = heapq.heappop(min_heap)
                    operations += num - smallest
                heapq.heappush(min_heap, num)
            return operations

        return min(min_operations_to_non_decreasing(nums), min_operations_to_non_increasing(nums))