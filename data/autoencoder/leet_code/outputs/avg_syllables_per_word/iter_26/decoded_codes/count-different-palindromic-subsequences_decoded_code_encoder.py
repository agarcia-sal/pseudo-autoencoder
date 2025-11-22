class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MODULO = 10**9 + 7
        n = len(s)

        next_occurrence = [[-1] * n for _ in range(4)]
        prev_occurrence = [[-1] * n for _ in range(4)]

        for char_index in range(4):
            character = chr(ord('a') + char_index)
            last_occ = -1
            for pos in range(n):
                if s[pos] == character:
                    last_occ = pos
                prev_occurrence[char_index][pos] = last_occ

            last_occ = -1
            for pos in range(n - 1, -1, -1):
                if s[pos] == character:
                    last_occ = pos
                next_occurrence[char_index][pos] = last_occ

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for start_index in range(n - length + 1):
                end_index = start_index + length - 1
                total = 0
                for char_index in range(4):
                    character = chr(ord('a') + char_index)
                    left_pos = next_occurrence[char_index][start_index]
                    right_pos = prev_occurrence[char_index][end_index]

                    if left_pos == -1 or right_pos == -1 or left_pos > end_index or right_pos < start_index:
                        continue
                    elif left_pos == right_pos:
                        total += 1
                    else:
                        total += (dp[left_pos + 1][right_pos - 1] + 2) % MODULO
                dp[start_index][end_index] = total % MODULO

        return dp[0][n - 1] if n > 0 else 0