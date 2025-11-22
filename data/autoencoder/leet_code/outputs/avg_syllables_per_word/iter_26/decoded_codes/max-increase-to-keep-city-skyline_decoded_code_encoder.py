from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        total_increase = 0
        for i in range(n):
            for j in range(n):
                max_height = min(row_maxes[i], col_maxes[j])
                current_height = grid[i][j]
                height_difference = max_height - current_height
                if height_difference > 0:
                    total_increase += height_difference

        return total_increase