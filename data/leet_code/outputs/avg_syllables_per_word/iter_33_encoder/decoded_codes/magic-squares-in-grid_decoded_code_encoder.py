from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(i: int, j: int) -> bool:
            # Center must be 5
            if grid[i][j] != 5:
                return False
            numbers = set()
            # Check numbers in 3x3 subgrid and collect them
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    val = grid[x][y]
                    if val < 1 or val > 9 or val in numbers:
                        return False
                    numbers.add(val)
            # Check sums of rows and columns
            for start in range(i - 1, i + 2):
                row_sum = grid[start][j - 1] + grid[start][j] + grid[start][j + 1]
                col_sum = grid[i - 1][start] + grid[i][start] + grid[i + 1][start]
                if row_sum != 15 or col_sum != 15:
                    return False
            # Check sums of diagonals
            if (grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1] != 15 or
                grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1] != 15):
                return False
            return True

        count = 0
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if is_magic(i, j):
                    count += 1
        return count