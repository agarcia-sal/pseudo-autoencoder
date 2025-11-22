class Solution:
    def minInsertions(self, s: str) -> int:
        def longest_palindromic_subsequence(s: str) -> int:
            n = len(s)
            dp = [[0] * n for _ in range(n)]

            for i in range(n):
                dp[i][i] = 1

            for length in range(2, n + 1):
                for start in range(n - length + 1):
                    end = start + length - 1
                    if s[start] == s[end]:
                        if length == 2:
                            dp[start][end] = 2
                        else:
                            dp[start][end] = dp[start + 1][end - 1] + 2
                    else:
                        dp[start][end] = max(dp[start][end - 1], dp[start + 1][end])
            return dp[0][n - 1]

        return len(s) - longest_palindromic_subsequence(s)