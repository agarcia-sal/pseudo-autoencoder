class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        # Precompute the changes needed to make any substring palindrome
        changes = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                changes[start][end] = changes[start + 1][end - 1] + (s[start] != s[end])

        import math
        dp = [[math.inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                for start in range(i):
                    cost = changes[start][i - 1] if start <= i - 1 else 0
                    dp[i][j] = min(dp[i][j], dp[start][j - 1] + cost)

        return dp[n][k]