class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MODULO = 10**9 + 7
        n = len(s)

        # Map character index 0-3 to actual characters 'a', 'b', 'c', 'd'
        def char(ci: int) -> str:
            return chr(ord('a') + ci)

        next_occurrence = [[-1] * n for _ in range(4)]
        previous_occurrence = [[-1] * n for _ in range(4)]

        # Compute previous_occurrence arrays
        for ci in range(4):
            c = char(ci)
            last_pos = -1
            for i in range(n):
                if s[i] == c:
                    last_pos = i
                previous_occurrence[ci][i] = last_pos

            last_pos = -1
            for i in range(n - 1, -1, -1):
                if s[i] == c:
                    last_pos = i
                next_occurrence[ci][i] = last_pos

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                for ci in range(4):
                    left_pos = next_occurrence[ci][start]
                    right_pos = previous_occurrence[ci][end]

                    if left_pos == -1 or left_pos > end or right_pos == -1 or right_pos < start:
                        continue
                    elif left_pos == right_pos:
                        dp[start][end] = (dp[start][end] + 1) % MODULO
                    else:
                        dp[start][end] = (dp[start][end] + dp[left_pos + 1][right_pos - 1] + 2) % MODULO

        return dp[0][n - 1] if n > 0 else 0