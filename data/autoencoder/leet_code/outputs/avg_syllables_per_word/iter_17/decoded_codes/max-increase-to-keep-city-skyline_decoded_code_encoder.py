from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Compute max in each row
        row_maxes = self.compute_max_values(grid)
        # Compute max in each column, grid transposed
        col_maxes = self.compute_max_values(list(zip(*grid)))

        total_increase = 0
        for i in range(n):
            for j in range(n):
                max_height = min(row_maxes[i], col_maxes[j])
                difference = max_height - grid[i][j]
                if difference > 0:
                    total_increase += difference
        return total_increase

    @staticmethod
    def compute_max_values(grid_collection: List[List[int]]) -> List[int]:
        # For each list in the collection, return the maximum value
        return [max(row) if row else 0 for row in grid_collection]