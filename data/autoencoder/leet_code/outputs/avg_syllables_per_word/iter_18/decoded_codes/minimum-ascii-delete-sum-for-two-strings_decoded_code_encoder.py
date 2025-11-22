class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = self.initialize_dp_table(m, n)

        # Initialize first row
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        # Initialize first column
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        # Fill dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    cost_del_s1 = dp[i - 1][j] + ord(s1[i - 1])
                    cost_del_s2 = dp[i][j - 1] + ord(s2[j - 1])
                    dp[i][j] = min(cost_del_s1, cost_del_s2)

        return dp[m][n]

    def initialize_dp_table(self, m: int, n: int) -> list[list[int]]:
        # Create a (m+1) x (n+1) 2D list initialized to zero
        return [[0] * (n + 1) for _ in range(m + 1)]