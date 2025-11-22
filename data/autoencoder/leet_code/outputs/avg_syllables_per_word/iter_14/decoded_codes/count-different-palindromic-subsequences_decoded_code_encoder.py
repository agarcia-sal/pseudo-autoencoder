class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 1
        n = len(s)

        def initialize_matrix(rows: int, columns: int):
            return [[-1] * columns for _ in range(rows)]

        next_occurrence = initialize_matrix(4, n)
        prev_occurrence = initialize_matrix(4, n)

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

        def initialize_two_dimensional_list(size: int):
            return [[0] * size for _ in range(size)]

        dp = initialize_two_dimensional_list(n)
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for c in range(4):
                    char = chr(ord('a') + c)
                    left = next_occurrence[c][i]
                    right = prev_occurrence[c][j]

                    if left > j or right < i:
                        continue
                    elif left == right:
                        dp[i][j] = (dp[i][j] + 1) % MOD
                    else:
                        dp[i][j] = (dp[i][j] + dp[left + 1][right - 1] + 2) % MOD

        return dp[0][n - 1]