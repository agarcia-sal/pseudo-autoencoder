from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for row in grid:
            if row[0] == 0:
                for c in range(cols):
                    row[c] = 1 - row[c]
        for c in range(1, cols):
            count_ones = 0
            for r in range(rows):
                count_ones += grid[r][c]
            if count_ones < rows / 2:
                for r in range(rows):
                    grid[r][c] = 1 - grid[r][c]
        score = 0
        for row in grid:
            binary_str = ''.join(str(x) for x in row)
            score += int(binary_str, 2)
        return score