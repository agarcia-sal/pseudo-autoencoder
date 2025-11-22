class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        # Initialize dp array with zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill first row: cost of deleting all chars from s2 up to j
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        # Fill first column: cost of deleting all chars from s1 up to i
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        # Fill the rest of the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    first_option = dp[i - 1][j] + ord(s1[i - 1])
                    second_option = dp[i][j - 1] + ord(s2[j - 1])
                    dp[i][j] = min(first_option, second_option)

        return dp[m][n]