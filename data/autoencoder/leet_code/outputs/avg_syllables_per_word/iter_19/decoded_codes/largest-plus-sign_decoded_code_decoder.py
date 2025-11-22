from typing import List, Set, Tuple

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines_set: Set[Tuple[int, int]] = set((x, y) for x, y in mines)
        # dp[i][j] = [left_count, up_count, right_count, down_count]
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]

        # Calculate left and up counts
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    dp[i][j][0] = dp[i][j - 1][0] + 1 if j > 0 else 1  # left
                    dp[i][j][1] = dp[i - 1][j][1] + 1 if i > 0 else 1  # up

        result = 0
        # Calculate right and down counts, and determine the max order
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) not in mines_set:
                    dp[i][j][2] = dp[i][j + 1][2] + 1 if j < n - 1 else 1  # right
                    dp[i][j][3] = dp[i + 1][j][3] + 1 if i < n - 1 else 1  # down
                    plus_sign_order = min(dp[i][j])
                    if plus_sign_order > result:
                        result = plus_sign_order

        return result