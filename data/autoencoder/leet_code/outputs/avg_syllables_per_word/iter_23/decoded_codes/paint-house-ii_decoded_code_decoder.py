from math import inf
from typing import List

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
                return inf

        for i in range(1, n):
            min_cost = inf
            min_cost_index = -1
            second_min_cost = inf

            # Find min_cost and second_min_cost from the previous house (i-1)
            for j in range(k):
                prev_cost = costs[i-1][j]
                if prev_cost < min_cost:
                    second_min_cost = min_cost
                    min_cost = prev_cost
                    min_cost_index = j
                elif prev_cost < second_min_cost:
                    second_min_cost = prev_cost

            # Update current house cost by adding either min_cost or second_min_cost
            for j in range(k):
                if j == min_cost_index:
                    costs[i][j] += second_min_cost
                else:
                    costs[i][j] += min_cost

        return min(costs[-1])