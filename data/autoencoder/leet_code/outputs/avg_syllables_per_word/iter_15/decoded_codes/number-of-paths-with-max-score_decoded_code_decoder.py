from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        dp = [[[-float('inf'), 0] for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = [0, 1]
        directions = [(1, 0), (0, 1), (1, 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                c = board[i][j]
                if c in ('X', 'S'):
                    continue
                value = 0 if c == 'E' else int(c)
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        next_score, next_count = dp[ni][nj]
                        curr_score, curr_count = dp[i][j]
                        if next_score == -float('inf'):
                            continue
                        total_score = next_score + value
                        if total_score > curr_score:
                            dp[i][j] = [total_score, next_count]
                        elif total_score == curr_score and curr_score != -float('inf'):
                            dp[i][j][1] = (curr_count + next_count) % MOD

        if dp[0][0][0] == -float('inf'):
            return [0, 0]
        return dp[0][0]