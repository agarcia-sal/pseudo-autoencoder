from math import inf
from typing import List

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        cost = self.initialize_two_dimensional_list(n, n, 0)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                cost[i][j] = cost[i + 1][j - 1] + houses[j] - houses[i]

        dp = self.initialize_two_dimensional_list(n + 1, k + 1, inf)
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i):
                    potential_value = dp[p][j - 1] + cost[p][i - 1]
                    if dp[i][j] > potential_value:
                        dp[i][j] = potential_value

        return dp[n][k]

    def initialize_two_dimensional_list(self, rows: int, columns: int, initial_value) -> List[List]:
        return [[initial_value for _ in range(columns)] for _ in range(rows)]