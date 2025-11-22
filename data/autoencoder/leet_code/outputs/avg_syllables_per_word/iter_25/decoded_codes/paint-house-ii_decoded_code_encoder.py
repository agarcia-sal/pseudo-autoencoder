from math import inf

class Solution:
    def minCostII(self, costs):
        if not costs:
            return 0
        n = len(costs)
        k = len(costs[0])
        if k == 1:
            return costs[0][0] if n == 1 else inf

        for i in range(1, n):
            min_cost, min_cost_index = inf, -1
            second_min_cost = inf
            # Find min and second min in previous row
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