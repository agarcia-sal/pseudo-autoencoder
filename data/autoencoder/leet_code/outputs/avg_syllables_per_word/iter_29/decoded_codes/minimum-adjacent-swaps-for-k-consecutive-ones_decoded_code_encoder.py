from math import inf

class Solution:
    def minMoves(self, nums: list[int], k: int) -> int:
        positions = [i for i, num in enumerate(nums) if num == 1]

        def calculate_cost(start: int, end: int) -> int:
            mid = (start + end - 1) // 2
            median = positions[mid]
            cost = 0
            for i in range(start, end):
                distance = abs(positions[i] - median + mid - i)
                cost += distance
            return cost

        min_cost = inf
        for i in range(len(positions) - k + 1):
            current_cost = calculate_cost(i, i + k)
            if current_cost < min_cost:
                min_cost = current_cost

        return min_cost