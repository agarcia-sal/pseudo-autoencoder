class Solution:
    def orderOfLargestPlusSign(self, n, mines):
        mines_set = set((x, y) for x, y in mines)

        # dp dimensions: 4 directions (left, up, right, down), each n x n grid
        dp = [[[0] * n for _ in range(n)] for _ in range(4)]

        # First pass: left and up directions
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    dp[0][i][j] = (dp[0][i][j-1] + 1) if j > 0 else 1  # left
                    dp[1][i][j] = (dp[1][i-1][j] + 1) if i > 0 else 1  # up

        # Second pass: right and down directions, and get maximum plus sign order
        result = 0
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i, j) not in mines_set:
                    dp[2][i][j] = (dp[2][i][j+1] + 1) if j < n - 1 else 1  # right
                    dp[3][i][j] = (dp[3][i+1][j] + 1) if i < n - 1 else 1  # down
                    plus_sign_order = min(dp[0][i][j], dp[1][i][j], dp[2][i][j], dp[3][i][j])
                    if plus_sign_order > result:
                        result = plus_sign_order

        return result