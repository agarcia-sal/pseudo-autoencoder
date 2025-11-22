class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dp = self.initialize_dp(m, n)

        def dfs(x, y):
            if dp[x][y] != -1:
                return dp[x][y]

            max_length = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    possible_length = 1 + dfs(nx, ny)
                    if possible_length > max_length:
                        max_length = possible_length

            dp[x][y] = max_length
            return max_length

        longest_path = 0
        for i in range(m):
            for j in range(n):
                candidate_path = dfs(i, j)
                if candidate_path > longest_path:
                    longest_path = candidate_path

        return longest_path

    def initialize_dp(self, m, n):
        return [[-1] * n for _ in range(m)]