class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        NEG_INF = float('-inf')
        dp = [[[NEG_INF, 0] for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = [0, 1]

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] in ('X', 'S'):
                    continue

                if board[i][j] == 'E':
                    value = 0
                else:
                    value = int(board[i][j])

                for x, y in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < n:
                        next_score, next_count = dp[ni][nj]
                        if next_score == NEG_INF:
                            continue
                        curr_score, curr_count = dp[i][j]
                        total = next_score + value
                        if total > curr_score:
                            dp[i][j] = [total, next_count]
                        elif total == curr_score:
                            dp[i][j][1] = (dp[i][j][1] + next_count) % MOD

        if dp[0][0][0] == NEG_INF:
            return [0, 0]
        return dp[0][0]