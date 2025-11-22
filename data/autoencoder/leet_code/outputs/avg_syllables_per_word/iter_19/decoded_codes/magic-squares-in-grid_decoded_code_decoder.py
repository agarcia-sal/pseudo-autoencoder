class Solution:
    def numMagicSquaresInside(self, grid):
        def is_magic(i, j):
            # The center must be 5
            if grid[i][j] != 5:
                return False

            numbers = set()
            # Check all 3x3 cells around (i,j)
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    val = grid[x][y]
                    # Values must be in 1..9 and unique
                    if val < 1 or val > 9 or val in numbers:
                        return False
                    numbers.add(val)

            # Check rows and columns sum to 15
            for start in range(i - 1, i + 2):
                row_sum = grid[start][j - 1] + grid[start][j] + grid[start][j + 1]
                col_sum = grid[i - 1][start] + grid[i][start] + grid[i + 1][start]
                if row_sum != 15 or col_sum != 15:
                    return False

            # Check diagonals sum to 15
            diag1 = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
            diag2 = grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1]
            if diag1 != 15 or diag2 != 15:
                return False

            return True

        count = 0
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        # Iterate only where a 3x3 subgrid with center at (i,j) exists
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if is_magic(i, j):
                    count += 1

        return count