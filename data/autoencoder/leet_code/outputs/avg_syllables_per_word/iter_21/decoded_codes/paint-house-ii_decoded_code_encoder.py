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

            # Find min and second min cost from previous row
            for j in range(k):
                cost_prev = costs[i - 1][j]
                if cost_prev < min_cost:
                    second_min_cost = min_cost
                    min_cost = cost_prev
                    min_cost_index = j
                elif cost_prev < second_min_cost:
                    second_min_cost = cost_prev

            for j in range(k):
                if j == min_cost_index:
                    costs[i][j] += second_min_cost
                else:
                    costs[i][j] += min_cost

        return min(costs[-1])