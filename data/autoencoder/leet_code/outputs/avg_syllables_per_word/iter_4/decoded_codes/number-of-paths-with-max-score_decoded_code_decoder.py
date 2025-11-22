class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        # dp[i][j] = [max_score_from_i_j_to_end, count_of_max_score_paths]
        # Initialize with [-inf, 0]
        dp = [[[-float('inf'), 0] for _ in range(n)] for _ in range(n)]

        dp[n-1][n-1] = [0, 1]  # Start point

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X' or board[i][j] == 'S':
                    continue

                value = 0 if board[i][j] == 'E' else int(board[i][j])

                for x, y in [(1,0), (0,1), (1,1)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < n:
                        next_score, next_count = dp[ni][nj]
                        if next_score == -float('inf'):
                            continue
                        total_score = next_score + value
                        if total_score > dp[i][j][0]:
                            dp[i][j][0] = total_score
                            dp[i][j][1] = next_count
                        elif total_score == dp[i][j][0]:
                            dp[i][j][1] = (dp[i][j][1] + next_count) % MOD

        if dp[0][0][0] == -float('inf'):
            return [0, 0]
        return [dp[0][0][0], dp[0][0][1]]