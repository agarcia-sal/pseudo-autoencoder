class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        mines_set = set(tuple(mine) for mine in mines)

        # dp[i][j] holds 4 directional counts:
        # dp[i][j][0]: continuous 1's to the left (including current)
        # dp[i][j][1]: continuous 1's upwards
        # dp[i][j][2]: continuous 1's to the right
        # dp[i][j][3]: continuous 1's downwards
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]

        # Fill dp for left and up directions
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    # Left direction
                    if j > 0:
                        dp[i][j][0] = dp[i][j-1][0] + 1
                    else:
                        dp[i][j][0] = 1
                    # Up direction
                    if i > 0:
                        dp[i][j][1] = dp[i-1][j][1] + 1
                    else:
                        dp[i][j][1] = 1

        result = 0

        # Fill dp for right and down directions, and calculate result
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i, j) not in mines_set:
                    # Right direction
                    if j < n - 1:
                        dp[i][j][2] = dp[i][j+1][2] + 1
                    else:
                        dp[i][j][2] = 1
                    # Down direction
                    if i < n - 1:
                        dp[i][j][3] = dp[i+1][j][3] + 1
                    else:
                        dp[i][j][3] = 1

                    plus_sign_order = min(dp[i][j])
                    if plus_sign_order > result:
                        result = plus_sign_order

        return result