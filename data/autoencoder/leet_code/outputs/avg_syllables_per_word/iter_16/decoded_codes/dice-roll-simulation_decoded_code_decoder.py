class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD = 10**9 + 7
        max_roll = max(rollMax)
        dp = [[[0] * (max_roll + 1) for _ in range(6)] for __ in range(n + 1)]

        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                limit = rollMax[j]
                for k in range(1, limit + 1):
                    if k > 1:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        s = 0
                        for x in range(6):
                            if x != j:
                                limit_x = rollMax[x]
                                s += sum(dp[i - 1][x][1:limit_x + 1])
                        dp[i][j][k] = s % MOD

        result = 0
        for j in range(6):
            limit = rollMax[j]
            result += sum(dp[n][j][1:limit + 1])
        return result % MOD