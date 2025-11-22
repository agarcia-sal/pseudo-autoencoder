from typing import List, Tuple

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines_set = set(tuple(mine) for mine in mines)

        # dp[i][j] holds a list of 4 integers representing counts in directions:
        # 0: left, 1: up, 2: right, 3: down
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]

        # First pass: count left and up arms
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    # Left count
                    if j > 0:
                        dp[i][j][0] = dp[i][j - 1][0] + 1
                    else:
                        dp[i][j][0] = 1
                    # Up count
                    if i > 0:
                        dp[i][j][1] = dp[i - 1][j][1] + 1
                    else:
                        dp[i][j][1] = 1

        result = 0

        # Second pass: count right and down arms and compute the minimum arms length
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) not in mines_set:
                    # Right count
                    if j < n - 1:
                        dp[i][j][2] = dp[i][j + 1][2] + 1
                    else:
                        dp[i][j][2] = 1
                    # Down count
                    if i < n - 1:
                        dp[i][j][3] = dp[i + 1][j][3] + 1
                    else:
                        dp[i][j][3] = 1

                    plus_sign_order = min(dp[i][j])
                    if plus_sign_order > result:
                        result = plus_sign_order

        return result