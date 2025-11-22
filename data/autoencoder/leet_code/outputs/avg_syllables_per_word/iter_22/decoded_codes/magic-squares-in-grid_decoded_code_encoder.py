from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(i: int, j: int) -> bool:
            # Check center cell is 5
            if grid[i][j] != 5:
                return False

            numbers = set()
            # Check cells and their values
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    val = grid[x][y]
                    if val < 1 or val > 9 or val in numbers:
                        return False
                    numbers.add(val)

            # Check rows and columns sum to 15
            for start in range(i - 1, i + 2):
                row_sum = grid[start][j - 1] + grid[start][j] + grid[start][j + 1]
                if row_sum != 15:
                    return False
                col_sum = grid[i - 1][start] + grid[i][start] + grid[i + 1][start]
                if col_sum != 15:
                    return False

            # Check diagonals sum to 15
            diag1 = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
            if diag1 != 15:
                return False
            diag2 = grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1]
            if diag2 != 15:
                return False

            return True

        count = 0
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        # Iterate only over cells that can be center of 3x3 subgrid
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if is_magic(i, j):
                    count += 1
        return count