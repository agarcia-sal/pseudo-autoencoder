class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10**9 + 1
        dp = [0] * (numPeople + 1)
        dp[0] = 1
        dp[2] = 1

        for i in range(4, numPeople + 1, 2):
            for j in range(0, i, 2):
                dp[i] += dp[j] * dp[i - 2 - j]
            dp[i] %= MOD

        return dp[numPeople]