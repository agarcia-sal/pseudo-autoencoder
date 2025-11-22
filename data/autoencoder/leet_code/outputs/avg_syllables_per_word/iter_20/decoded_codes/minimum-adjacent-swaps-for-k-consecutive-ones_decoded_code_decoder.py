from math import inf
from typing import List

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        positions = [i for i, num in enumerate(nums) if num == 1]

        def calculate_cost(start: int, end: int) -> int:
            middle = (start + end) // 2
            median_value = positions[middle]
            total_cost = 0
            for index in range(start, end):
                # offset_difference corresponds to adjusting for the median's index position
                offset_difference = median_value - middle + index
                distance = abs(positions[index] - offset_difference)
                total_cost += distance
            return total_cost

        min_cost = inf
        n = len(positions)
        for i in range(n - k + 1):
            candidate_cost = calculate_cost(i, i + k)
            if candidate_cost < min_cost:
                min_cost = candidate_cost

        return min_cost