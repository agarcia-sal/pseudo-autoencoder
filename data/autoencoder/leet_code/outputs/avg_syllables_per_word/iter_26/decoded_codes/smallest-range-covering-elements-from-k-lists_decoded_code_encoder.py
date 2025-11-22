import heapq
from math import inf

class Solution:
    def smallestRange(self, nums):
        min_heap = []
        max_value = -inf

        for index in range(len(nums)):
            heapq.heappush(min_heap, (nums[index][0], index, 0))
            if nums[index][0] > max_value:
                max_value = nums[index][0]

        smallest_range = inf
        result = [-10**9, 10**9]

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