from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        dp = [[-1]*n for _ in range(m)]

        def dfs(x: int, y: int) -> int:
            if dp[x][y] != -1:
                return dp[x][y]

            max_length = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    candidate_length = 1 + dfs(nx, ny)
                    if candidate_length > max_length:
                        max_length = candidate_length

            dp[x][y] = max_length
            return max_length

        longest_path = 0
        for i in range(m):
            for j in range(n):
                candidate_path = dfs(i, j)
                if candidate_path > longest_path:
                    longest_path = candidate_path

        return longest_path