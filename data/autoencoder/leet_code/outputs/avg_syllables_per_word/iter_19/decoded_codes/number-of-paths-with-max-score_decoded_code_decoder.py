class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        # dp[i][j] = (max_score_from_here, count_of_paths)
        # Initialize with (-inf, 0)
        dp = [[(float('-inf'), 0) for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = (0, 1)  # bottom-right corner (S)

        directions = [(1, 0), (0, 1), (1, 1)]  # down, right, diagonal down-right

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] in ('X', 'S'):
                    continue
                value = 0 if board[i][j] == 'E' else int(board[i][j])

                max_score, count = float('-inf'), 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        next_score, next_count = dp[ni][nj]
                        if next_score == float('-inf'):
                            continue
                        candidate_score = next_score + value
                        if candidate_score > max_score:
                            max_score = candidate_score
                            count = next_count
                        elif candidate_score == max_score:
                            count = (count + next_count) % MOD

                if max_score != float('-inf'):
                    dp[i][j] = (max_score, count)

        if dp[0][0][0] == float('-inf'):
            return [0, 0]
        return [dp[0][0][0], dp[0][0][1]]