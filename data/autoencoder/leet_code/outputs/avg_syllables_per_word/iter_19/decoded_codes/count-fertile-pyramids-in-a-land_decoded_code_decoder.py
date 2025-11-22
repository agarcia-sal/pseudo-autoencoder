from typing import List

class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        def count_pyramids_from_top(grid: List[List[int]]) -> int:
            if not grid or not grid[0]:
                return 0
            m, n = len(grid), len(grid[0])
            dp = [[0] * n for _ in range(m)]
            count = 0

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        if i == 0 or j == 0 or j == n - 1:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
                        if dp[i][j] > 1:
                            count += dp[i][j] - 1
            return count

        def count_pyramids_from_bottom(grid: List[List[int]]) -> int:
            if not grid or not grid[0]:
                return 0
            m, n = len(grid), len(grid[0])
            dp = [[0] * n for _ in range(m)]
            count = 0

            for i in range(m - 1, -1, -1):
                for j in range(n):
                    if grid[i][j] == 1:
                        if i == m - 1 or j == 0 or j == n - 1:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = 1 + min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])
                        if dp[i][j] > 1:
                            count += dp[i][j] - 1
            return count

        return count_pyramids_from_top(grid) + count_pyramids_from_bottom(grid)