class Solution:
    def matrixScore(self, grid):
        for row in grid:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]
        cols = len(grid[0])
        rows = len(grid)
        for col in range(1, cols):
            count_ones = 0
            for row_index in range(rows):
                count_ones += grid[row_index][col]
            if count_ones < rows / 2:
                for row_index in range(rows):
                    grid[row_index][col] = 1 - grid[row_index][col]
        score = 0
        for row in grid:
            binary_number = ''.join(str(num) for num in row)
            score += int(binary_number, 2)
        return score