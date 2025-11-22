class Solution:
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        n = len(floor)
        dp = self.initializeDP(n, numCarpets)

        # Base case: no carpets used
        for i in range(1, n + 1):
            dp[i][0] = dp[i-1][0] + (1 if floor[i-1] == 1 else 0)

        for c in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                option_one = dp[i-1][c] + (1 if floor[i-1] == 1 else 0)
                option_two = dp[max(0, i - carpetLen)][c-1]
                dp[i][c] = min(option_one, option_two)

        return dp[n][numCarpets]

    def initializeDP(self, n, numCarpets):
        return [[0] * (numCarpets + 1) for _ in range(n + 1)]