class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][k]:
        # i: length of the record
        # j: number of 'A's used (0 or 1)
        # k: number of consecutive 'L's at the end (0 to 2)
        dp = [[[0] * 3 for _ in range(2)] for __ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for j in range(2):  # number of 'A's used: 0 or 1
                for k in range(3):  # consecutive 'L's count: 0 to 2
                    val = dp[i - 1][j][k]
                    if val == 0:
                        continue
                    # Add 'P' (present): resets consecutive L to 0
                    dp[i][j][0] = (dp[i][j][0] + val) % MOD
                    # Add 'A' (absent): only if no 'A's used yet
                    if j == 0:
                        dp[i][1][0] = (dp[i][1][0] + val) % MOD
                    # Add 'L' (late): can add if k < 2, increase consecutive L by 1
                    if k < 2:
                        dp[i][j][k + 1] = (dp[i][j][k + 1] + val) % MOD

        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD
        return result