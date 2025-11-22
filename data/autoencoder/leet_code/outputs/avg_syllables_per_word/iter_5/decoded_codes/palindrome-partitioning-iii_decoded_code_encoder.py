class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        # Precompute the cost to convert any substring s[i:j] into a palindrome
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i + 1][j - 1] + (s[i] != s[j])

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                for start in range(i):
                    dp[i][j] = min(dp[i][j], dp[start][j - 1] + cost[start][i - 1])

        return dp[n][k]