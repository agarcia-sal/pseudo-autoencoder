class Solution:
    def matrixScore(self, grid):
        m, n = len(grid), len(grid[0])
        # Flip rows where the first element is 0
        for row in grid:
            if row[0] == 0:
                for i in range(n):
                    row[i] = 1 - row[i]
        # For each column from 1 to n-1, flip if count of 1s is less than half
        for col in range(1, n):
            count_ones = sum(grid[row][col] for row in range(m))
            if count_ones < m / 2:
                for row in range(m):
                    grid[row][col] = 1 - grid[row][col]
        # Calculate score by interpreting each row as a binary number
        score = 0
        for row in grid:
            val = 0
            for bit in row:
                val = (val << 1) | bit
            score += val
        return score