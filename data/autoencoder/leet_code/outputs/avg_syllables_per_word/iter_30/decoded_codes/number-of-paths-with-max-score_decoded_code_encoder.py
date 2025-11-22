class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        # dp[i][j] = [max_score, count_of_paths] from cell (i,j) to bottom-right
        # Initialize with [-inf, 0]
        dp = [[[-float('inf'), 0] for _ in range(n)] for _ in range(n)]
        dp[n - 1][n - 1] = [0, 1]  # bottom-right corner 'E'

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                cell = board[i][j]
                if cell == 'X' or cell == 'S':
                    continue

                if cell != 'E':
                    value = int(cell)
                else:
                    value = 0

                for x, y in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < n:
                        nxt_score, nxt_count = dp[ni][nj]
                        cur_score, cur_count = dp[i][j]
                        if nxt_score + value > cur_score:
                            dp[i][j][0] = nxt_score + value
                            dp[i][j][1] = nxt_count
                        elif nxt_score + value == cur_score:
                            dp[i][j][1] = (dp[i][j][1] + nxt_count) % MOD

        if dp[0][0][0] == -float('inf'):
            return [0, 0]
        return dp[0][0]