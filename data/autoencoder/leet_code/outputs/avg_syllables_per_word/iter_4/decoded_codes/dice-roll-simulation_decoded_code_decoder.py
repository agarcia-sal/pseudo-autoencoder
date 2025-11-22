class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD = 10**9 + 7
        maxRoll = max(rollMax)
        dp = [[[0] * (maxRoll + 1) for _ in range(6)] for _ in range(n + 1)]

        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                max_j = rollMax[j]
                for k in range(1, max_j + 1):
                    if k > 1:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        total = 0
                        for x in range(6):
                            if x != j:
                                for y in range(1, rollMax[x] + 1):
                                    total += dp[i - 1][x][y]
                        dp[i][j][k] = total % MOD

        result = 0
        for j in range(6):
            for k in range(1, rollMax[j] + 1):
                result += dp[n][j][k]

        return result % MOD