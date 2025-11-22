class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = self.initialize_dp_table(s, p)
        dp[0][0] = True

        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[len(s)][len(p)]

    def initialize_dp_table(self, s: str, p: str) -> list[list[bool]]:
        dp = []
        for _ in range(len(s) + 1):
            row = [False] * (len(p) + 1)
            dp.append(row)
        return dp