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

            # Find the minimum and second minimum cost for the previous house
            for j in range(k):
                cost = costs[i - 1][j]
                if cost < min_cost:
                    second_min_cost = min_cost
                    min_cost = cost
                    min_cost_index = j
                elif cost < second_min_cost:
                    second_min_cost = cost

            # Update costs for current house
            for j in range(k):
                if j == min_cost_index:
                    costs[i][j] += second_min_cost
                else:
                    costs[i][j] += min_cost

        return min(costs[-1])