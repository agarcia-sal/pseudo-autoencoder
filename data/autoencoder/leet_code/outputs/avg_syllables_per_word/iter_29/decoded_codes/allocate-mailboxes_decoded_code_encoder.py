from math import inf

class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        # Precompute cost[i][j]: minimal cost to place one mailbox for houses[i..j]
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                # median index minimizes sum of distances
                mid = (i + j) // 2
                total = 0
                for x in range(i, j + 1):
                    total += abs(houses[x] - houses[mid])
                cost[i][j] = total

        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i):
                    candidate_value = dp[p][j - 1] + cost[p][i - 1]
                    if candidate_value < dp[i][j]:
                        dp[i][j] = candidate_value

        return dp[n][k]