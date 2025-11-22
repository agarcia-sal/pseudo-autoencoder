class Solution:
    def numMagicSquaresInside(self, grid):
        def is_magic(i, j):
            # Center must be 5
            if grid[i][j] != 5:
                return False

            numbers = set()
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    val = grid[x][y]
                    # Check if values are in 1..9 and unique
                    if val < 1 or val > 9 or val in numbers:
                        return False
                    numbers.add(val)

            # Check sums of rows and columns
            for start in range(i - 1, i + 2):
                if (grid[start][j - 1] + grid[start][j] + grid[start][j + 1] != 15 or
                    grid[i - 1][start - (i - 1)] + grid[i][start - (i - 1)] + grid[i + 1][start - (i - 1)] != 15):
                    # The above checks rows and columns sums together incorrectly,
                    # so we rewrite separately:
                    # We'll check row sums and column sums separately below
                    return False

            # Instead, checking rows and columns sums separately:
            # (rewrite above loop)
            for row in range(i - 1, i + 2):
                if sum(grid[row][j - 1:j + 2]) != 15:
                    return False
            for col in range(j - 1, j + 2):
                if (grid[i - 1][col] + grid[i][col] + grid[i + 1][col]) != 15:
                    return False

            # Check the two diagonals
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