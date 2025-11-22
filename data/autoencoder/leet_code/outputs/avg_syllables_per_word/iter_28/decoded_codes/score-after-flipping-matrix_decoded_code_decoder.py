from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in grid:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]

        rows, cols = len(grid), len(grid[0])
        for col in range(1, cols):
            count_ones = sum(grid[row][col] for row in range(rows))
            if count_ones < rows / 2:
                for row in range(rows):
                    grid[row][col] = 1 - grid[row][col]

        score = 0
        for row in grid:
            binary_number = ''.join(str(e) for e in row)
            score += int(binary_number, 2)

        return score