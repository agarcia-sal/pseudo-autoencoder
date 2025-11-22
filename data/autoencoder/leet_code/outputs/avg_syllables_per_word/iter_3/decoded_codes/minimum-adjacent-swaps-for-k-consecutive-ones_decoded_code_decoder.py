from typing import List

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        positions = [i for i, val in enumerate(nums) if val == 1]

        def calculate_cost(start: int, end: int) -> int:
            mid = (start + end) // 2
            median = positions[mid]
            return sum(abs(positions[i] - (median - (mid - i))) for i in range(start, end))

        min_cost = float('inf')
        for i in range(len(positions) - k + 1):
            current_cost = calculate_cost(i, i + k)
            if current_cost < min_cost:
                min_cost = current_cost

        return min_cost