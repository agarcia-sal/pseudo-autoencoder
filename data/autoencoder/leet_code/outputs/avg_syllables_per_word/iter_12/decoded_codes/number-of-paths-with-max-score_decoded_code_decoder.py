class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        def initialize_dp(n):
            # dp[i][j] = [max_score_from_i_j, number_of_ways]
            return [[[-float('inf'), 0] for _ in range(n)] for _ in range(n)]

        dp = initialize_dp(n)
        dp[n - 1][n - 1] = [0, 1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] in ('X', 'S'):
                    continue

                value = 0 if board[i][j] == 'E' else int(board[i][j])

                for dx, dy in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        next_score, next_ways = dp[ni][nj]
                        current_score, current_ways = dp[i][j]

                        if next_score == -float('inf'):
                            continue

                        new_score = next_score + value

                        if new_score > current_score:
                            dp[i][j] = [new_score, next_ways]
                        elif new_score == current_score:
                            dp[i][j][1] = (current_ways + next_ways) % MOD

        if dp[0][0][0] == -float('inf'):
            return [0, 0]

        return dp[0][0]