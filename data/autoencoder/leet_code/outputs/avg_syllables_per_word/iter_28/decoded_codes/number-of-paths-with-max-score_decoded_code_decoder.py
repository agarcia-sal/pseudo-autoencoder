from math import inf

class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 1
        n = len(board)

        dp = [[[-inf, 0] for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = [0, 1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or board[i][j] == 'S':
                    continue

                value = 0 if board[i][j] == 'E' else int(board[i][j])

                for x, y in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < n:
                        nxt_score, nxt_count = dp[ni][nj]
                        cur_score, cur_count = dp[i][j]
                        if nxt_score > cur_score:
                            dp[i][j] = [nxt_score + value, nxt_count]
                        elif nxt_score == cur_score and cur_score != -inf:
                            dp[i][j][1] = (cur_count + nxt_count) % MOD

        if dp[0][0][0] == -inf:
            return [0, 0]
        return dp[0][0]