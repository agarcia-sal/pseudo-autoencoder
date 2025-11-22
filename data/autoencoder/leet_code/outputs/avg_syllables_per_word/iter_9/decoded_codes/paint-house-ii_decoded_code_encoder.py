class Solution:
    def minCostII(self, costs):
        if not costs:
            return 0

        n, k = len(costs), len(costs[0])
        if k == 1:
            return costs[0][0] if n == 1 else float('inf')

        for i in range(1, n):
            min_cost = float('inf')
            min_index = -1
            second_min = float('inf')

            for j in range(k):
                prev_cost = costs[i-1][j]
                if prev_cost < min_cost:
                    second_min = min_cost
                    min_cost = prev_cost
                    min_index = j
                elif prev_cost < second_min:
                    second_min = prev_cost

            for j in range(k):
                if j == min_index:
                    costs[i][j] += second_min
                else:
                    costs[i][j] += min_cost

        return min(costs[-1])