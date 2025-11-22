class Solution:
    def orderOfLargestPlusSign(self, n, mines):
        mines_set = set(tuple(mine) for mine in mines)
        dp = [[[0]*4 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    dp[i][j][0] = (dp[i][j-1][0] + 1) if j > 0 else 1
                    dp[i][j][1] = (dp[i-1][j][1] + 1) if i > 0 else 1

        result = 0
        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if (i, j) not in mines_set:
                    dp[i][j][2] = (dp[i][j+1][2] + 1) if j < n - 1 else 1
                    dp[i][j][3] = (dp[i+1][j][3] + 1) if i < n - 1 else 1
                    plus_sign_order = min(dp[i][j])
                    if plus_sign_order > result:
                        result = plus_sign_order

        return result