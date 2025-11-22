from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Flip rows where the first element is 0
        for row in grid:
            if row[0] == 0:
                for i in range(cols):
                    row[i] = 1 - row[i]

        # Flip columns (except first) where count of 1s is less than half the number of rows
        for col in range(1, cols):
            count_of_ones = 0
            for row_index in range(rows):
                count_of_ones += grid[row_index][col]
            if count_of_ones < rows / 2:
                for row_index in range(rows):
                    grid[row_index][col] = 1 - grid[row_index][col]

        total_score = 0
        for row in grid:
            # Convert bits to integer directly using int with base=2
            binary_representation = ''.join(str(bit) for bit in row)
            numeric_value = int(binary_representation, 2)
            total_score += numeric_value

        return total_score