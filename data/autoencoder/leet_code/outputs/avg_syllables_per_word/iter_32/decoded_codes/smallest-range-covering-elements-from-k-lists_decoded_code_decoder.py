import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_value = float('-inf')

        # Initialize heap with the first element of each list and track the max value
        for i in range(len(nums)):
            if nums[i]:  # Ensure the list is not empty
                first_val = nums[i][0]
                heapq.heappush(min_heap, (first_val, i, 0))
                if first_val > max_value:
                    max_value = first_val

        smallest_range = float('inf')
        result = [-100000, 100000]

        while min_heap:
            min_value, list_index, element_index = heapq.heappop(min_heap)

            # Update smallest range and result if better range is found
            if max_value - min_value < smallest_range:
                smallest_range = max_value - min_value
                result = [min_value, max_value]

            # If there is a next element in the same list, push it to heap
            if element_index + 1 < len(nums[list_index]):
                next_value = nums[list_index][element_index + 1]
                heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
                if next_value > max_value:
                    max_value = next_value
            else:
                # One of the lists is exhausted, no more ranges covering all lists possible
                break

        return result