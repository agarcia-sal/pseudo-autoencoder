from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        if cols == 0:
            return 0

        # Flip rows where the first element is 0, so each row starts with 1
        for r in range(rows):
            if grid[r][0] == 0:
                for c in range(cols):
                    grid[r][c] = 1 - grid[r][c]

        # For each column (starting from 1), if number of ones less than half rows, flip the column
        for c in range(1, cols):
            count_ones = 0
            for r in range(rows):
                count_ones += grid[r][c]
            if count_ones < rows / 2:
                for r in range(rows):
                    grid[r][c] = 1 - grid[r][c]

        # Calculate the score by interpreting each row as a binary number
        score = 0
        for r in range(rows):
            # Convert list of bits to integer directly
            decimal_value = 0
            for bit in grid[r]:
                decimal_value = (decimal_value << 1) | bit
            score += decimal_value

        return score