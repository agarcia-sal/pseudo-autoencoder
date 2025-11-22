class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD = 10**9 + 7
        max_rollMax_element = max(rollMax)

        # dp dimensions: (n+1) x 6 x (max_rollMax_element+1)
        dp = [[[0] * (max_rollMax_element + 1) for _ in range(6)] for __ in range(n + 1)]

        # Initialize dp for i=1 (first roll)
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    if k > 1:
                        dp[i][j][k] = dp[i-1][j][k-1]
                    else:
                        sum_value = 0
                        for x in range(6):
                            if x != j:
                                sum_value += sum(dp[i-1][x][1:rollMax[x]+1])
                        dp[i][j][k] = sum_value % MOD

        result = 0
        for j in range(6):
            result += sum(dp[n][j][1:rollMax[j]+1])
        return result % MOD