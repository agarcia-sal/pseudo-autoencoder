from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        # Flip rows where the first element is 0
        for row in grid:
            if row[0] == 0:
                for i in range(cols):
                    row[i] = 1 - row[i]

        # For columns from 1 to end, flip if count of ones is less than half the number of rows
        for col in range(1, cols):
            count_ones = 0
            for row_index in range(rows):
                count_ones += grid[row_index][col]

            if count_ones < rows / 2:
                for row_index in range(rows):
                    grid[row_index][col] = 1 - grid[row_index][col]

        # Calculate the score by converting each row's bits to decimal and summing
        score = 0
        for row in grid:
            # Convert list of bits to string, then to int with base 2
            binary_str = ''.join(str(bit) for bit in row)
            score += int(binary_str, 2)

        return score