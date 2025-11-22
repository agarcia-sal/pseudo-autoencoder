class Solution:
    def numMagicSquaresInside(self, grid):
        def is_magic(i, j):
            if grid[i][j] != 5:
                return False
            numbers = set()
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    val = grid[x][y]
                    if val < 1 or val > 9 or val in numbers:
                        return False
                    numbers.add(val)
            for start in range(i - 1, i + 2):
                # Check rows sum
                if sum(grid[start][y] for y in range(j - 1, j + 2)) != 15:
                    return False
                # Check columns sum
                if sum(grid[x][start] for x in range(i - 1, i + 2)) != 15:
                    return False
            # Check diagonals sums
            if grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1] != 15:
                return False
            if grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1] != 15:
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