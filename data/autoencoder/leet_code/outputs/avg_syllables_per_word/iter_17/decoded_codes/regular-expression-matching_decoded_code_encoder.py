class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def create_boolean_list(length: int) -> list[bool]:
            return [False] * length

        def create_boolean_matrix(rows: int, columns: int) -> list[list[bool]]:
            return [create_boolean_list(columns) for _ in range(rows)]

        dp = create_boolean_matrix(len(s) + 1, len(p) + 1)
        dp[0][0] = True

        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[len(s)][len(p)]