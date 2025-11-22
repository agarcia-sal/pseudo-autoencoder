class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        # Precompute changes needed to convert s[i:j+1] to palindrome
        changes = [[0]*n for _ in range(n)]
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                changes[i][j] = changes[i+1][j-1] + (s[i] != s[j] if length > 1 else 0)

        dp = [[float('inf')] * (k+1) for _ in range(n+1)]
        dp[0][0] = 0

        for i in range(1, n+1):
            for j in range(1, min(k, i) + 1):
                for start in range(i):
                    dp[i][j] = min(dp[i][j], dp[start][j-1] + changes[start][i-1])

        return dp[n][k]