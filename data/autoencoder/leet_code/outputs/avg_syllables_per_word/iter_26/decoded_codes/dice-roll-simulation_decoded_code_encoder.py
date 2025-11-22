class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD = 10**9 + 1

        max_roll = max(rollMax)
        # dp[i][j][k] = number of sequences of length i where
        # the last roll is face j (0-based) and it has been rolled k times consecutively
        dp = [[[0] * (rollMax[j] + 1) for j in range(6)] for _ in range(n + 1)]

        # Base case: for sequences of length 1, each face can appear once consecutively
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    if k > 1:
                        # If we roll the same face again, increase consecutive count by 1
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        # If rolling a different face, sum over all sequences where last face is not j
                        s = 0
                        for x in range(6):
                            if x == j:
                                continue
                            s += sum(dp[i - 1][x][1: rollMax[x] + 1])
                        dp[i][j][k] = s % MOD
                    dp[i][j][k] %= MOD

        # Result is sum of all sequences of length n over all faces and consecutive counts
        result = 0
        for j in range(6):
            result += sum(dp[n][j][1: rollMax[j] + 1])
        return result % MOD