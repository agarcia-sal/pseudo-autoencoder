class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][k] := number of sequences of length i with
        # j = count of 'A's (Absents) in the sequence (0 or 1)
        # k = count of consecutive 'L's (Late) at the end of the sequence (0,1,2)
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]

        dp[0][0][0] = 1

        for i in range(1, n+1):
            for j in range(2):
                for k in range(3):
                    # Add 'P' (Present): reset consecutive L to 0, same count of 'A's
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD
                    # Add 'A' (Absent): can only add if no 'A' yet (j==0)
                    if j == 0:
                        dp[i][1][0] = (dp[i][1][0] + dp[i-1][0][k]) % MOD
                    # Add 'L' (Late): increase consecutive L by 1 if less than 2
                    if k < 2:
                        dp[i][j][k+1] = (dp[i][j][k+1] + dp[i-1][j][k]) % MOD

        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD
        return result