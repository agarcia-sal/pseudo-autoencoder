from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(grid[i][j] for i in range(n)) for j in range(n)]

        total_increase = 0
        for i in range(n):
            for j in range(n):
                max_height = min(row_maxes[i], col_maxes[j])
                potential_increase = max_height - grid[i][j]
                if potential_increase > 0:
                    total_increase += potential_increase
        return total_increase