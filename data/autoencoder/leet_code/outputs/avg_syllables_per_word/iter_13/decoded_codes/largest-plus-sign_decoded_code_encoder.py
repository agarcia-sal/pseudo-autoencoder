class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        mines_set = set((x, y) for x, y in mines)
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]

        # Directions are present in pseudocode but unused, so we omit them

        # Forward pass: compute counts for right and down directions
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    dp[i][j][0] = dp[i][j - 1][0] + 1 if j > 0 else 1  # right count
                    dp[i][j][1] = dp[i - 1][j][1] + 1 if i > 0 else 1  # down count

        result = 0
        # Backward pass: compute counts for left and up directions and find max order
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) not in mines_set:
                    dp[i][j][2] = dp[i][j + 1][2] + 1 if j < n - 1 else 1  # left count
                    dp[i][j][3] = dp[i + 1][j][3] + 1 if i < n - 1 else 1  # up count

                    plus_sign_order = min(dp[i][j])
                    if plus_sign_order > result:
                        result = plus_sign_order

        return result