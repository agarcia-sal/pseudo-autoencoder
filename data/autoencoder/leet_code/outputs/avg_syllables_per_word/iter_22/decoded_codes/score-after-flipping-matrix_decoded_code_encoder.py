class Solution:
    def matrixScore(self, grid):
        # Flip rows where the leading bit is 0
        for row in grid:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]
        # Flip columns where more than half are 0s (except the first column)
        for j in range(1, len(grid[0])):
            count_ones = sum(grid[i][j] for i in range(len(grid)))
            if count_ones < len(grid) / 2:
                for i in range(len(grid)):
                    grid[i][j] = 1 - grid[i][j]
        # Calculate total score
        score = 0
        for row in grid:
            binary_str = ''.join(str(bit) for bit in row)
            score += int(binary_str, 2)
        return score