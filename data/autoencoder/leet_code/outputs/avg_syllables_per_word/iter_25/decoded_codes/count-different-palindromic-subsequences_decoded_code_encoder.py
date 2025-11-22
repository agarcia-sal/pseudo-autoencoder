class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MODULO = 10**9 + 7
        n = len(s)

        next_occurrence = [[-1] * n for _ in range(4)]
        previous_occurrence = [[-1] * n for _ in range(4)]

        for c in range(4):
            ch = chr(ord('a') + c)
            last_pos = -1
            for i in range(n):
                if s[i] == ch:
                    last_pos = i
                previous_occurrence[c][i] = last_pos

            last_pos = -1
            for i in range(n - 1, -1, -1):
                if s[i] == ch:
                    last_pos = i
                next_occurrence[c][i] = last_pos

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for c in range(4):
                    left = next_occurrence[c][i]
                    right = previous_occurrence[c][j]
                    if left == -1 or right == -1 or left > j or right < i:
                        continue
                    if left == right:
                        dp[i][j] = (dp[i][j] + 1) % MODULO
                    else:
                        if left + 1 <= right - 1:
                            dp[i][j] = (dp[i][j] + dp[left + 1][right - 1] + 2) % MODULO
                        else:
                            # when left+1 > right-1, the substring inside is empty, count 2 
                            # for the two characters at left and right positions
                            dp[i][j] = (dp[i][j] + 2) % MODULO

        return dp[0][n - 1] if n > 0 else 0