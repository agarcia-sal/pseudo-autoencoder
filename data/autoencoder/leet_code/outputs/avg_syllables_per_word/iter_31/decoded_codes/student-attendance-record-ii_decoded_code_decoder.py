from typing import List

class Solution:
    def checkRecord(self, n: int) -> int:
        MODULO = 10**9 + 7

        # dp[i][j][k] represents the count of attendance records of length i
        # with j A's (absences) used (j ∈ {0, 1})
        # and k consecutive L's (late) at the end (k ∈ {0, 1, 2})
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        dp[0][0][0] = 1  # Base case: empty record

        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    # Add 'P' (present), resets consecutive L count to 0
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MODULO

                    # Add 'A' (absent), only if no A has been used yet; resets L count to 0
                    if j == 0:
                        dp[i][1][0] = (dp[i][1][0] + dp[i-1][0][k]) % MODULO

                    # Add 'L' (late), only if consecutive L count < 2,
                    # increments consecutive L count by 1, A count stays the same
                    if k < 2:
                        dp[i][j][k+1] = (dp[i][j][k+1] + dp[i-1][j][k]) % MODULO

        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MODULO

        return result