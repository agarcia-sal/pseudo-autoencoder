class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        next_occurrence = [[-1] * n for _ in range(4)]
        prev_occurrence = [[-1] * n for _ in range(4)]

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

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = 0
                for c in range(4):
                    left = next_occurrence[c][i]
                    right = prev_occurrence[c][j]
                    if left == -1 or right == -1 or left > j or right < i:
                        continue
                    if left == right:
                        total += 1
                    else:
                        total += dp[left + 1][right - 1] + 2
                    total %= MOD
                dp[i][j] = total

        return dp[0][n - 1] if n > 0 else 0