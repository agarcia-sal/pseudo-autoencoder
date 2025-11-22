from typing import List

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        positions = []
        for index in range(len(nums)):
            if nums[index] == 1:
                positions.append(index)

        def calculate_cost(start: int, end: int) -> int:
            mid = (start + end) // 2
            median = positions[mid]
            cost = 0
            for i in range(start, end):
                difference = positions[i] - (median - (mid - i))
                cost += abs(difference)
            return cost

        min_cost = float('inf')
        n = len(positions)
        for i in range(n - k + 1):
            current_cost = calculate_cost(i, i + k)
            if current_cost < min_cost:
                min_cost = current_cost

        return min_cost