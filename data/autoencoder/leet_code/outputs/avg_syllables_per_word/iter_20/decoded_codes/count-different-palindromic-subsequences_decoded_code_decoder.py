class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        def initialize_grid(rows: int, columns: int) -> list[list[int]]:
            return [[-1] * columns for _ in range(rows)]

        next_occurrence = initialize_grid(4, n)
        prev_occurrence = initialize_grid(4, n)

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

        dp = initialize_grid(n, n)
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for c in range(4):
                    left = next_occurrence[c][i]
                    right = prev_occurrence[c][j]
                    if left > j or right < i or left == -1 or right == -1:
                        continue
                    if left == right:
                        dp[i][j] = (dp[i][j] + 1) % MOD
                    else:
                        dp[i][j] = (dp[i][j] + dp[left + 1][right - 1] + 2) % MOD

        return dp[0][n - 1] if n > 0 else 0