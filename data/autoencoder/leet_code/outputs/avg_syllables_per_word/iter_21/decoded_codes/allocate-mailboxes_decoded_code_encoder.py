from math import inf
from typing import List

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        cost = self.construct_cost_matrix(houses, n)
        dp = self.construct_dp_table(n, k)

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i):
                    potential_distance = dp[p][j - 1] + cost[p][i - 1]
                    if potential_distance < dp[i][j]:
                        dp[i][j] = potential_distance

        return dp[n][k]

    def construct_cost_matrix(self, houses: List[int], n: int) -> List[List[int]]:
        cost = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                cost[i][j] = cost[i + 1][j - 1] + houses[j] - houses[i]
        return cost

    def construct_dp_table(self, n: int, k: int) -> List[List[float]]:
        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        return dp