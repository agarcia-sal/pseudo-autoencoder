class Solution:
    def pathsWithMaxScore(self, board):
        MODULO = 10**9 + 7
        n = len(board)
        dp = [[[float('-inf'), 0] for _ in range(n)] for _ in range(n)]
        dp[n - 1][n - 1] = [0, 1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                cell = board[i][j]
                if cell == 'X' or cell == 'S':
                    continue
                value = 0 if cell == 'E' else int(cell)
                for x, y in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < n:
                        next_score, next_count = dp[ni][nj]
                        current_score, current_count = dp[i][j]
                        if next_score > current_score:
                            dp[i][j][0] = next_score + value
                            dp[i][j][1] = next_count
                        elif next_score == current_score and next_score != float('-inf'):
                            dp[i][j][1] = (dp[i][j][1] + next_count) % MODULO

        if dp[0][0][0] == float('-inf'):
            return [0, 0]
        return [dp[0][0][0], dp[0][0][1]]