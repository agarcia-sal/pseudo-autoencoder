from typing import List

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        cost = self.prepareCostMatrix(houses, n)
        dp = self.prepareDPTable(n, k)

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i):
                    candidate_distance = dp[p][j - 1] + cost[p][i - 1]
                    if dp[i][j] > candidate_distance:
                        dp[i][j] = candidate_distance

        return dp[n][k]

    def prepareCostMatrix(self, houses: List[int], n: int) -> List[List[int]]:
        cost = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                cost[i][j] = cost[i + 1][j - 1] + houses[j] - houses[i]
        return cost

    def prepareDPTable(self, n: int, k: int) -> List[List[float]]:
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        return dp