from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Flip rows so that first element is 1
        for row in grid:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]

        # Flip columns (except first) to maximize number of 1s
        n_rows = len(grid)
        n_cols = len(grid[0])
        for col in range(1, n_cols):
            count_ones = 0
            for row in range(n_rows):
                count_ones += grid[row][col]
            if count_ones < n_rows / 2:
                for row in range(n_rows):
                    grid[row][col] = 1 - grid[row][col]

        score = 0
        for row in grid:
            binary_number = ''.join(str(bit) for bit in row)
            score += int(binary_number, 2)

        return score