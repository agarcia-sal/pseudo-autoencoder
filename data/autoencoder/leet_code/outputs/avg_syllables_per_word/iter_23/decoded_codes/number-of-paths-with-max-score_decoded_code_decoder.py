class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        # dp[i][j] = [max_score, num_paths]
        # Initialize with negative infinity score and 0 paths
        dp = [[[float('-inf'), 0] for _ in range(n)] for _ in range(n)]
        # At the bottom-right corner (the end 'E'), score = 0 and number of ways = 1
        dp[n - 1][n - 1] = [0, 1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or board[i][j] == 'E':
                    # Skip obstacles and end cell as starting points (except bottom-right which was pre-set)
                    # But we must continue for end only if it's bottom-right; otherwise skip
                    if i == n - 1 and j == n - 1:
                        continue
                    else:
                        continue
                # Determine cell value
                if board[i][j] == 'S':
                    value = 0
                else:
                    value = int(board[i][j])
                # For each next step: down (1,0), right (0,1), diagonal (1,1)
                for x, y in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < n:
                        next_score, next_paths = dp[ni][nj]
                        curr_score, curr_paths = dp[i][j]
                        if next_score == float('-inf'):
                            continue
                        new_score = next_score + value
                        if new_score > curr_score:
                            dp[i][j] = [new_score, next_paths]
                        elif new_score == curr_score:
                            dp[i][j][1] = (dp[i][j][1] + next_paths) % MOD

        if dp[0][0][0] == float('-inf'):
            return [0, 0]
        return dp[0][0]