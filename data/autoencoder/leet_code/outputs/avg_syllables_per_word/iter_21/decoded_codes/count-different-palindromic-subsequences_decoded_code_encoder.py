class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        def initialize_2d_list(rows, columns, default_value):
            return [[default_value] * columns for _ in range(rows)]

        next_occurrence = initialize_2d_list(4, n, -1)
        prev_occurrence = initialize_2d_list(4, n, -1)

        for c in range(4):
            char = chr(ord('a') + c)
            last = -1
            for i in range(n):
                if s[i] == char:
                    last = i
                prev_occurrence[c][i] = last

            last = -1
            for i in range(n - 1, -1, -1):
                if s[i] == char:
                    last = i
                next_occurrence[c][i] = last

        dp = initialize_2d_list(n, n, 0)
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for c in range(4):
                    left = next_occurrence[c][i]
                    right = prev_occurrence[c][j]
                    if left == -1 or left > j or right == -1 or right < i:
                        continue
                    if left == right:
                        dp[i][j] = (dp[i][j] + 1) % MOD
                    else:
                        dp[i][j] = (dp[i][j] + dp[left + 1][right - 1] + 2) % MOD

        return dp[0][n - 1] if n > 0 else 0