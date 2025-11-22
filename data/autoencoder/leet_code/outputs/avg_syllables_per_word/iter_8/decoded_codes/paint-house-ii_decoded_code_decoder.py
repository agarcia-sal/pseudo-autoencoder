class Solution:
    def minCostII(self, costs):
        if not costs:
            return 0

        n = len(costs)
        k = len(costs[0])

        if k == 1:
            if n == 1:
                return costs[0][0]
            else:
                return float('inf')

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
                if j == min_cost_index:
                    costs[i][j] += second_min_cost
                else:
                    costs[i][j] += min_cost

        return min(costs[n - 1])