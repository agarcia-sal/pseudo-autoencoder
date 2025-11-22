from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        # Flip rows if the first element is 0
        for row in grid:
            if row[0] == 0:
                for i in range(cols):
                    row[i] = 1 - row[i]

        # For each column from 1 to end, flip column if count of ones is less than half
        for col in range(1, cols):
            count_ones = 0
            for row_idx in range(rows):
                count_ones += grid[row_idx][col]
            if count_ones * 2 < rows:
                for row_idx in range(rows):
                    grid[row_idx][col] = 1 - grid[row_idx][col]

        score = 0
        for row in grid:
            binary_number = ''.join(str(e) for e in row)
            score += int(binary_number, 2)

        return score