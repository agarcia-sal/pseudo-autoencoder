from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dp = self.initializeDP(m, n)

        def dfs(x: int, y: int) -> int:
            if dp[x][y] != -1:
                return dp[x][y]

            max_length = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    length = 1 + dfs(nx, ny)
                    if length > max_length:
                        max_length = length

            dp[x][y] = max_length
            return max_length

        longest_path = 0
        for i in range(m):
            for j in range(n):
                current_length = dfs(i, j)
                if current_length > longest_path:
                    longest_path = current_length

        return longest_path

    def initializeDP(self, m: int, n: int) -> List[List[int]]:
        dp = []
        for _ in range(m):
            row = [-1] * n
            dp.append(row)
        return dp