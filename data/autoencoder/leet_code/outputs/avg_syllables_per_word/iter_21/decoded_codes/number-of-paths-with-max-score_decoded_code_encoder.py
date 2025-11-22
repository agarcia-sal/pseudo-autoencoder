class Solution:
    def dp_initialization_function(self, n):
        # Initialize dp table: each cell holds [max_score, path_count]
        # max_score initialized to -inf, path_count to 0
        result = [[[-float('inf'), 0] for _ in range(n)] for _ in range(n)]
        result[n - 1][n - 1] = [0, 1]  # starting position bottom-right
        return result

    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        dp = self.dp_initialization_function(n)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                c = board[i][j]
                if c in ('X', 'S'):
                    continue
                value = 0 if c == 'E' else int(c)
                # positions to move: down, right, diagonal down-right
                for x, y in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < n:
                        next_score, next_paths = dp[ni][nj]
                        cur_score, cur_paths = dp[i][j]
                        if next_score + value > cur_score:
                            dp[i][j][0] = next_score + value
                            dp[i][j][1] = next_paths
                        elif next_score + value == cur_score:
                            dp[i][j][1] = (cur_paths + next_paths) % MOD

        max_score, path_count = dp[0][0]
        if max_score == -float('inf'):
            return [0, 0]
        return [max_score, path_count]