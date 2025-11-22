import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_value = float('-inf')
        for i, lst in enumerate(nums):
            if lst:  # handle empty lists edge case
                heapq.heappush(min_heap, (lst[0], i, 0))
                if lst[0] > max_value:
                    max_value = lst[0]

        smallest_range = float('inf')
        result = [-100000, 100000]

        while min_heap:
            min_value, list_idx, elem_idx = heapq.heappop(min_heap)
            current_range = max_value - min_value
            if current_range < smallest_range:
                smallest_range = current_range
                result = [min_value, max_value]
            if elem_idx + 1 < len(nums[list_idx]):
                next_value = nums[list_idx][elem_idx + 1]
                heapq.heappush(min_heap, (next_value, list_idx, elem_idx + 1))
                if next_value > max_value:
                    max_value = next_value
            else:
                break

        return result