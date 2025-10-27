class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * (rollMax[j] + 1) for j in range(6)] for _ in range(n + 1)]

        # Initialize for single roll sequences
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    if k > 1:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        temp_sum = 0
                        for x in range(6):
                            if x != j:
                                temp_sum += sum(dp[i - 1][x][1 : rollMax[x] + 1])
                        dp[i][j][k] = temp_sum % MOD

        result = 0
        for j in range(6):
            result += sum(dp[n][j][1 : rollMax[j] + 1])
        return result % MOD