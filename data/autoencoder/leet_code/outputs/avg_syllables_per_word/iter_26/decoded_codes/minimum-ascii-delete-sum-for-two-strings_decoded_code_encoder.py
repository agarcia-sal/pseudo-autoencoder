class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        length_m = len(s1)
        length_n = len(s2)

        # Initialize dp array with zeros
        dp = [[0] * (length_n + 1) for _ in range(length_m + 1)]

        # Fill the first row with ASCII sums of s2 characters
        for j in range(1, length_n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        # Fill the first column with ASCII sums of s1 characters
        for i in range(1, length_m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        # Fill the rest of the dp table
        for i in range(1, length_m + 1):
            for j in range(1, length_n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),
                        dp[i][j - 1] + ord(s2[j - 1])
                    )

        return dp[length_m][length_n]