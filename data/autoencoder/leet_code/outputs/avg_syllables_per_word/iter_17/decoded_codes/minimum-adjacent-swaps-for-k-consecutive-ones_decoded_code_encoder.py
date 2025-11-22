from typing import List

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # Extract positions of 1s in nums
        positions = [i for i, num in enumerate(nums) if num == 1]

        def calculate_cost(start: int, end: int) -> int:
            mid = (start + end) // 2
            median = positions[mid]
            cost = 0
            for i in range(start, end):
                cost += abs(positions[i] - median - (mid - i))
            return cost

        min_cost = float('inf')
        for i in range(len(positions) - k + 1):
            min_cost = min(min_cost, calculate_cost(i, i + k))

        return min_cost