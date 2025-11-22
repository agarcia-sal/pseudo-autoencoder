from typing import List, Set, Tuple

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines_set: Set[Tuple[int, int]] = set((mine[0], mine[1]) for mine in mines)

        # dp[i][j] = [count_right, count_down, count_left, count_up]
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]

        # First pass: count left and up directions
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    # left (0) direction count
                    dp[i][j][0] = dp[i][j-1][0] + 1 if j > 0 else 1
                    # up (3) direction count
                    dp[i][j][3] = dp[i-1][j][3] + 1 if i > 0 else 1

        # Second pass: count right and down directions, and calculate max order
        result = 0
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i, j) not in mines_set:
                    # right (2) direction count
                    dp[i][j][2] = dp[i][j+1][2] + 1 if j < n - 1 else 1
                    # down (1) direction count
                    dp[i][j][1] = dp[i+1][j][1] + 1 if i < n - 1 else 1

                    plus_sign_order = min(dp[i][j])
                    if plus_sign_order > result:
                        result = plus_sign_order

        return result