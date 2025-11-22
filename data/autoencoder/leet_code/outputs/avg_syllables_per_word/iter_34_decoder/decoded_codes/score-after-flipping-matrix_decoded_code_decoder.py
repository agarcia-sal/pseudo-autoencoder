from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Flip rows where the first element is 0
        for row in grid:
            if row[0] == 0:
                for i in range(1, len(row)):
                    row[i] = 1 - row[i]

        # For each column from the second one, flip if more zeros than ones
        rows = len(grid)
        cols = len(grid[0])
        for col in range(1, cols):
            count_ones = 0
            for row in range(rows):
                count_ones += grid[row][col]
            if count_ones < rows / 2:
                for row in range(rows):
                    grid[row][col] = 1 - grid[row][col]

        # Calculate the score by converting each row's binary to int
        score = 0
        for row in grid:
            binary_str = ''.join(str(bit) for bit in row)
            score += int(binary_str, 2)
        return score