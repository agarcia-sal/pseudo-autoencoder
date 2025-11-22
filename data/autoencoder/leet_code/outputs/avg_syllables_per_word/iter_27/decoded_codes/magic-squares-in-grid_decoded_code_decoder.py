from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(i: int, j: int) -> bool:
            # The center of the 3x3 grid must be 5
            if grid[i][j] != 5:
                return False

            numbers = set()
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    val = grid[x][y]
                    # Check if val is in the valid range and not seen before
                    if val < 1 or val > 9 or val in numbers:
                        return False
                    numbers.add(val)

            for start in range(i - 1, i + 2):
                # Check rows sum
                if (grid[start][j - 1] + grid[start][j] + grid[start][j + 1]) != 15:
                    return False
                # Check columns sum
                if (grid[i - 1][start] + grid[i][start] + grid[i + 1][start]) != 15:
                    return False

            # Check main diagonal sum
            if (grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]) != 15:
                return False
            # Check secondary diagonal sum
            if (grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1]) != 15:
                return False

            return True

        count = 0
        rows = len(grid)
        if rows < 3:
            return 0
        cols = len(grid[0])
        if cols < 3:
            return 0

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if is_magic(i, j):
                    count += 1

        return count