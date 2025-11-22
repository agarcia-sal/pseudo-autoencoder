from math import inf
from typing import List

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        positions = [i for i, num in enumerate(nums) if num == 1]

        def calculate_cost(start: int, end: int) -> int:
            mid = (start + end) // 2
            median = positions[mid]
            cost = 0
            for i in range(start, end):
                diff = abs(positions[i] - (median - (mid - i)))
                cost += diff
            return cost

        min_cost = inf
        for i in range(len(positions) - k + 1):
            current_cost = calculate_cost(i, i + k)
            if current_cost < min_cost:
                min_cost = current_cost

        return min_cost