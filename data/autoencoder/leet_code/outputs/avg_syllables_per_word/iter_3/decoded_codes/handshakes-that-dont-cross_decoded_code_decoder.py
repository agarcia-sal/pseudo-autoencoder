class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (numPeople + 1)
        dp[0], dp[2] = 1, 1

        for i in range(4, numPeople + 1, 2):
            total = 0
            for j in range(0, i - 1, 2):
                total += dp[j] * dp[i - 2 - j]
            dp[i] = total % MOD

        return dp[numPeople]