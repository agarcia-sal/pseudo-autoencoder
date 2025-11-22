import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_value = float('-inf')

        # Initialize the heap with the first element of each list along with the index info
        for index in range(len(nums)):
            val = nums[index][0]
            heapq.heappush(min_heap, (val, index, 0))
            if val > max_value:
                max_value = val

        smallest_range = float('inf')
        result = [-100000, 100000]

        while min_heap:
            min_value, list_index, element_index = heapq.heappop(min_heap)
            if max_value - min_value < smallest_range:
                smallest_range = max_value - min_value
                result = [min_value, max_value]

            if element_index + 1 < len(nums[list_index]):
                next_value = nums[list_index][element_index + 1]
                heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
                if next_value > max_value:
                    max_value = next_value
            else:
                break

        return result