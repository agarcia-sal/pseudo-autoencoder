from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MODULO = 10**9 + 7
        n = len(board)

        # dp[i][j] = [max_score, num_paths]
        # max_score: max score achievable from cell (i,j) to bottom-right
        # num_paths: number of such max score paths modulo MODULO
        dp = [[[-float('inf'), 0] for _ in range(n)] for _ in range(n)]

        # Start from bottom-right cell (the 'E' cell; treat score as 0)
        dp[n-1][n-1] = [0, 1]

        for i in reversed(range(n)):
            for j in reversed(range(n)):
                c = board[i][j]
                if c in ('X', 'S'):
                    continue

                value = 0 if c == 'E' else int(c)

                for dx, dy in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        next_score, next_paths = dp[ni][nj]
                        if next_score == -float('inf'):
                            continue
                        curr_score, curr_paths = dp[i][j]

                        total_score = next_score + value
                        if total_score > curr_score:
                            dp[i][j][0] = total_score
                            dp[i][j][1] = next_paths % MODULO
                        elif total_score == curr_score:
                            dp[i][j][1] = (dp[i][j][1] + next_paths) % MODULO

        max_score, paths = dp[0][0]
        if max_score == -float('inf'):
            return [0, 0]
        return [max_score, paths]