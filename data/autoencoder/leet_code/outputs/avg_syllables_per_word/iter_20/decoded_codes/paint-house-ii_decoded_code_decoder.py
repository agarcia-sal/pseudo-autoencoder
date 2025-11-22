import math
from typing import List

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n = len(costs)
        k = len(costs[0])
        if k == 1:
            return costs[0][0] if n == 1 else math.inf

        for i in range(1, n):
            min_cost = math.inf
            min_cost_index = -1
            second_min_cost = math.inf

            prev_costs = costs[i - 1]
            for j in range(k):
                c = prev_costs[j]
                if c < min_cost:
                    second_min_cost = min_cost
                    min_cost = c
                    min_cost_index = j
                elif c < second_min_cost:
                    second_min_cost = c

            for j in range(k):
                if j == min_cost_index:
                    costs[i][j] += second_min_cost
                else:
                    costs[i][j] += min_cost

        return min(costs[-1])