class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD = 10**9 + 7
        max_roll = max(rollMax)
        dp = [[[0] * (max_roll + 1) for _ in range(6)] for _ in range(n + 1)]

        # Base case: for roll 1, each face can appear once consecutively
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                limit_j = rollMax[j]
                for k in range(1, limit_j + 1):
                    if k > 1:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        total_sum = 0
                        for x in range(6):
                            if x != j:
                                limit_x = rollMax[x]
                                for y in range(1, limit_x + 1):
                                    total_sum += dp[i - 1][x][y]
                        dp[i][j][k] = total_sum % MOD

        result = 0
        for j in range(6):
            limit_j = rollMax[j]
            for k in range(1, limit_j + 1):
                result += dp[n][j][k]

        return result % MOD