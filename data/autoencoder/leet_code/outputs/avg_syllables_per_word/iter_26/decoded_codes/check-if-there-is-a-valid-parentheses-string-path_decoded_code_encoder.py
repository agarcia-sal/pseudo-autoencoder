class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        row_count = len(grid)
        column_count = len(grid[0]) if row_count > 0 else 0

        # If the total length of the path is odd, cannot have a valid parentheses sequence
        if (row_count + column_count - 1) % 2 != 0:
            return False

        max_k = row_count + column_count  # dimension for the parentheses balance state

        # Initialize 3D DP array with False
        # dp[i][j][k] means: is there a valid path to cell (i-1, j-1) with parentheses balance k
        dp = [[[False] * (row_count + 1) for _ in range(column_count + 1)] for __ in range(max_k + 1)]

        # Start with dp[0][0][1] = True since the first cell must be '(' to have a valid start
        # However, pseudocode sets dp[0][0][1] True, but indexes differ;
        # Adjust indices carefully:
        # The pseudocode sets dp[row+1][0][0] = True which reads dp[1][0][0]=True
        # But dp dimensions: (row_count+column_count+1) x (column_count+1) x (row_count+1)
        # We interpret i as row index, j as column index, k as balance
        # The pseudocode implies:
        # dp[i+1][j][k] holds the state for (i,j) cell
        # so dp[1][0][0] corresponds to cell (0,0) with balance 0
        # But balance 0 invalid at start if first cell is '('; need to match pseudocode precisely.

        # So follow pseudocode strictly:
        # dp[row+1][0][0] = True
        dp[1][0][0] = True

        for i in range(row_count):
            for j in range(column_count):
                for k in range(max_k + 1):
                    if dp[i + 1][j][k] or dp[i][j + 1][k]:
                        c = grid[i][j]
                        if c == '(' and k + 1 < max_k + 1:
                            dp[i + 1 + 1][j + 1][k + 1] = True
                        elif c == ')' and k - 1 >= 0:
                            dp[i + 1 + 1][j + 1][k - 1] = True

        # final check dp[row_count][column_count][0]
        return dp[row_count][column_count][0]