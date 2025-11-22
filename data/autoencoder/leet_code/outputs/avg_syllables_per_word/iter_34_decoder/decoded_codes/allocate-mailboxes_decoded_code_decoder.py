class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        cost = [[0] * n for _ in range(n)]

        # Precompute cost[i][j]: minimal distance sum when placing one mailbox for houses[i..j]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                median = (i + j) // 2
                dist_sum = 0
                for x in range(i, j + 1):
                    dist_sum += abs(houses[x] - houses[median])
                cost[i][j] = dist_sum

        # dp[i][j]: minimal distance sum for first i houses using j mailboxes
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i):
                    val = dp[p][j - 1] + cost[p][i - 1]
                    if val < dp[i][j]:
                        dp[i][j] = val

        return dp[n][k]