class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, n + 1):
            prefix_sum = 0
            if s[i - 1] == 'I':
                for j in range(n - i + 1):
                    prefix_sum = (prefix_sum + dp[i - 1][j]) % MOD
                    dp[i][j] = prefix_sum
            else:
                prefix_sum = 0
                for j in range(n - i, -1, -1):
                    prefix_sum = (prefix_sum + dp[i - 1][j + 1]) % MOD
                    dp[i][j] = prefix_sum

        result = sum(dp[n]) % MOD
        return result