from typing import List, Set, Tuple

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines_set: Set[Tuple[int, int]] = set((x, y) for x, y in mines)

        # dp[i][j] = [right, down, left, up]
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]

        # First pass: compute counts for right and down directions
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    if j > 0:
                        dp[i][j][0] = dp[i][j - 1][0] + 1  # right
                    else:
                        dp[i][j][0] = 1
                    if i > 0:
                        dp[i][j][1] = dp[i - 1][j][1] + 1  # down
                    else:
                        dp[i][j][1] = 1

        result = 0

        # Second pass: compute counts for left and up directions, and calculate max plus sign order
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) not in mines_set:
                    if j < n - 1:
                        dp[i][j][2] = dp[i][j + 1][2] + 1  # left
                    else:
                        dp[i][j][2] = 1
                    if i < n - 1:
                        dp[i][j][3] = dp[i + 1][j][3] + 1  # up
                    else:
                        dp[i][j][3] = 1

                    plus_sign_order = min(dp[i][j])
                    if plus_sign_order > result:
                        result = plus_sign_order

        return result