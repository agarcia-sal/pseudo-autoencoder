from typing import List

class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        def count_pyramids_from_top(grid: List[List[int]]) -> int:
            if not grid or not grid[0]:
                return 0
            rows, cols = len(grid), len(grid[0])
            dp = [[0] * cols for _ in range(rows)]
            count = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        if r == 0 or c == 0 or c == cols - 1:
                            dp[r][c] = 1
                        else:
                            dp[r][c] = 1 + min(
                                dp[r - 1][c - 1],
                                dp[r - 1][c],
                                dp[r - 1][c + 1]
                            )
                        if dp[r][c] > 1:
                            count += dp[r][c] - 1
            return count

        def count_pyramids_from_bottom(grid: List[List[int]]) -> int:
            if not grid or not grid[0]:
                return 0
            rows, cols = len(grid), len(grid[0])
            dp = [[0] * cols for _ in range(rows)]
            count = 0
            for r in range(rows - 1, -1, -1):
                for c in range(cols):
                    if grid[r][c] == 1:
                        if r == rows - 1 or c == 0 or c == cols - 1:
                            dp[r][c] = 1
                        else:
                            dp[r][c] = 1 + min(
                                dp[r + 1][c - 1],
                                dp[r + 1][c],
                                dp[r + 1][c + 1]
                            )
                        if dp[r][c] > 1:
                            count += dp[r][c] - 1
            return count

        total_from_top = count_pyramids_from_top(grid)
        total_from_bottom = count_pyramids_from_bottom(grid)
        return total_from_top + total_from_bottom