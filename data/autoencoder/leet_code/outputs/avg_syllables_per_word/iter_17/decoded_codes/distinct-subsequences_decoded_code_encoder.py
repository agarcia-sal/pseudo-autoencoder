class Solution:
    def numDistinct(self, string_s: str, string_t: str) -> int:
        length_m = len(string_s)
        length_n = len(string_t)

        # Create two-dimensional dp array with (length_m+1) rows and (length_n+1) columns
        dp = [[0] * (length_n + 1) for _ in range(length_m + 1)]

        for i in range(length_m + 1):
            dp[i][0] = 1  # An empty string_t is a subsequence of any prefix of string_s

        for i in range(1, length_m + 1):
            for j in range(1, length_n + 1):
                if string_s[i - 1] == string_t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[length_m][length_n]