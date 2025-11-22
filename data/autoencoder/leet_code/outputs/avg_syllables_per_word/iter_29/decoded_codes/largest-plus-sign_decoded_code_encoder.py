class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        mines_set = set(tuple(mine) for mine in mines)
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]

        # Left and Up directions
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    dp[i][j][0] = (dp[i][j - 1][0] + 1) if j > 0 else 1  # left
                    dp[i][j][1] = (dp[i - 1][j][1] + 1) if i > 0 else 1  # up

        # Right and Down directions
        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if (i, j) not in mines_set:
                    dp[i][j][2] = (dp[i][j + 1][2] + 1) if j < n - 1 else 1  # right
                    dp[i][j][3] = (dp[i + 1][j][3] + 1) if i < n - 1 else 1  # down
                    plus_sign_order = min(dp[i][j])
                    if plus_sign_order > 0:
                        dp[i][j] = [dp[i][j][d] for d in range(4)]  # ensure dp[i][j] not modified
                    if i == n - 1 and j == n - 1:
                        # initialize result outside loop
                        result = plus_sign_order
                    else:
                        result = max(result, plus_sign_order) if 'result' in locals() else plus_sign_order

        return result if 'result' in locals() else 0