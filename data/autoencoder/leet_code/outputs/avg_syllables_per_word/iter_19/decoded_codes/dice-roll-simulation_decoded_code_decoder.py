class Solution:
    def dieSimulator(self, n, rollMax):
        MOD = 10**9 + 7
        max_roll = max(rollMax)

        # dp[i][j][k]: number of sequences of length i, ending with face j,
        # where face j has appeared consecutively k times
        dp = [[[0] * (rollMax[j] + 1) for j in range(6)] for _ in range(n + 1)]

        # Base case: sequences of length 1
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):  # current face
                limit = rollMax[j]
                for k in range(1, limit + 1):
                    if k > 1:
                        # Extending the previous same face count by one
                        dp[i][j][k] = dp[i - 1][j][k - 1] % MOD
                    else:
                        # Starting a new streak for face j; sum over previous sequences ending with other faces
                        s = 0
                        for x in range(6):
                            if x == j:
                                continue
                            for y in range(1, rollMax[x] + 1):
                                s += dp[i - 1][x][y]
                        dp[i][j][k] = s % MOD

        result = 0
        for j in range(6):
            limit = rollMax[j]
            for k in range(1, limit + 1):
                result += dp[n][j][k]
        return result % MOD