class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD = 10**9 + 7
        max_roll = max(rollMax)
        dp = [[[0] * (max_roll + 1) for _ in range(6)] for _ in range(n + 1)]

        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                max_k = rollMax[j]
                for k in range(1, max_k + 1):
                    if k > 1:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        total = 0
                        for x in range(6):
                            if x != j:
                                total += sum(dp[i - 1][x][1:rollMax[x] + 1])
                        dp[i][j][k] = total % MOD

        result = 0
        for j in range(6):
            result += sum(dp[n][j][1:rollMax[j] + 1])
        return result % MOD