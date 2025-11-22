from math import inf

class Solution:
    def minMoves(self, nums):
        positions = []
        for index, value in enumerate(nums):
            if value == 1:
                positions.append(index)

        def calculate_cost(start, end):
            mid = (start + end) // 2
            median = positions[mid]
            cost = 0
            for i in range(start, end):
                cost += abs(positions[i] - (median - (mid - i)))
            return cost

        min_cost = inf
        n = len(positions)
        for i in range(n - k + 1):
            current_cost = calculate_cost(i, i + k)
            if current_cost < min_cost:
                min_cost = current_cost

        return min_cost