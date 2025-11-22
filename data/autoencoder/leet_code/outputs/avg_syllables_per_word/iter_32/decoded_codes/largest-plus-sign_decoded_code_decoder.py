from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines_set = set((x, y) for x, y in mines)

        # dp[i][j] = [count_left, count_up, count_right, count_down]
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]

        # First pass: count consecutive ones from left and up directions
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    dp[i][j][0] = dp[i][j - 1][0] + 1 if j > 0 else 1  # left count
                    dp[i][j][1] = dp[i - 1][j][1] + 1 if i > 0 else 1  # up count

        result = 0
        # Second pass: count consecutive ones from right and down directions, and compute min arm length
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) not in mines_set:
                    dp[i][j][2] = dp[i][j + 1][2] + 1 if j < n - 1 else 1  # right count
                    dp[i][j][3] = dp[i + 1][j][3] + 1 if i < n - 1 else 1  # down count

                    plus_sign_order = min(dp[i][j])
                    if plus_sign_order > result:
                        result = plus_sign_order

        return result