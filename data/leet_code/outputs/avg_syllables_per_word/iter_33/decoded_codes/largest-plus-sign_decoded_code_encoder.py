class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        mines_set = set(tuple(mine) for mine in mines)

        # dp[i][j] = [right, down, left, up] counts of continuous ones
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    # right direction (left to right)
                    dp[i][j][0] = dp[i][j-1][0] + 1 if j > 0 else 1
                    # down direction (top to bottom)
                    dp[i][j][1] = dp[i-1][j][1] + 1 if i > 0 else 1

        result = 0
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i, j) not in mines_set:
                    # left direction (right to left)
                    dp[i][j][2] = dp[i][j+1][2] + 1 if j < n-1 else 1
                    # up direction (bottom to top)
                    dp[i][j][3] = dp[i+1][j][3] + 1 if i < n-1 else 1

                    plus_sign_order = min(dp[i][j])
                    if plus_sign_order > result:
                        result = plus_sign_order

        return result