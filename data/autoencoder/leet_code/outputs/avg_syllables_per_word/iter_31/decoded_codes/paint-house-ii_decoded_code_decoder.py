from typing import List
import math

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n = len(costs)
        k = len(costs[0])

        if k == 1:
            if n == 1:
                return costs[0][0]
            else:
                return math.inf

        for i in range(1, n):
            min_cost = math.inf
            min_cost_index = -1
            second_min_cost = math.inf

            for j in range(k):
                prev_cost = costs[i-1][j]
                if prev_cost < min_cost:
                    second_min_cost = min_cost
                    min_cost = prev_cost
                    min_cost_index = j
                elif prev_cost < second_min_cost:
                    second_min_cost = prev_cost

            for j in range(k):
                if j == min_cost_index:
                    costs[i][j] += second_min_cost
                else:
                    costs[i][j] += min_cost

        return min(costs[-1])