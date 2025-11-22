class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        dp = [[(float('-inf'), 0) for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = (0, 1)

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X' or board[i][j] == 'S':
                    continue
                if board[i][j] == 'E':
                    value = 0
                else:
                    value = int(board[i][j])

                max_score, count = float('-inf'), 0
                for x, y in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < n:
                        score, ways = dp[ni][nj]
                        if score == float('-inf'):
                            continue
                        tot_score = score + value
                        if tot_score > max_score:
                            max_score, count = tot_score, ways
                        elif tot_score == max_score:
                            count = (count + ways) % MOD

                if max_score != float('-inf'):
                    dp[i][j] = (max_score, count)

        if dp[0][0][0] == float('-inf'):
            return [0, 0]
        return [dp[0][0][0], dp[0][0][1]]