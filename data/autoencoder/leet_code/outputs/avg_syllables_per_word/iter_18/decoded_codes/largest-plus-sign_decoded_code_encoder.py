from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines_set = set((mine[0], mine[1]) for mine in mines)
        # dp[i][j] = [right, down, left, up] counts of continuous 1's in those directions
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]

        # First pass: calculate right and down counts
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    dp[i][j][0] = dp[i][j - 1][0] + 1 if j > 0 else 1  # right from left to right
                    dp[i][j][1] = dp[i - 1][j][1] + 1 if i > 0 else 1  # down from top to bottom

        # Second pass: calculate left and up counts and find max plus sign order
        result = 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) not in mines_set:
                    dp[i][j][2] = dp[i][j + 1][2] + 1 if j < n - 1 else 1  # left from right to left
                    dp[i][j][3] = dp[i + 1][j][3] + 1 if i < n - 1 else 1  # up from bottom to top
                    plus_sign_order = min(dp[i][j])
                    if plus_sign_order > result:
                        result = plus_sign_order

        return result