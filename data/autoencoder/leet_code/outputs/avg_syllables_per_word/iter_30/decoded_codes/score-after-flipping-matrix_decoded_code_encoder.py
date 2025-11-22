class Solution:
    def matrixScore(self, grid):
        for row in grid:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]
        for col in range(1, len(grid[0])):
            count_ones = sum(grid[row][col] for row in range(len(grid)))
            if count_ones < len(grid) / 2:
                for row in range(len(grid)):
                    grid[row][col] = 1 - grid[row][col]
        score = 0
        for row in grid:
            binary_number = ''.join(str(num) for num in row)
            score += int(binary_number, 2)
        return score