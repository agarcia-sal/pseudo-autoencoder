class Solution:
    def minCostII(self, costs):
        if not costs:
            return 0

        n, k = len(costs), len(costs[0])

        if k == 1:
            return costs[0][0] if n == 1 else float('inf')

        for i in range(1, n):
            min_cost = float('inf')
            min_cost_index = -1
            second_min_cost = float('inf')

            for j in range(k):
                if costs[i - 1][j] < min_cost:
                    second_min_cost = min_cost
                    min_cost = costs[i - 1][j]
                    min_cost_index = j
                elif costs[i - 1][j] < second_min_cost:
                    second_min_cost = costs[i - 1][j]

            for j in range(k):
                costs[i][j] += second_min_cost if j == min_cost_index else min_cost

        return min(costs[-1])