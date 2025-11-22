class Solution:
    def matrixScore(self, grid):
        for row in grid:
            if row[0] == 0:
                # Flip the entire row
                for i in range(len(row)):
                    row[i] = 1 - row[i]
        cols = len(grid[0])
        rows = len(grid)
        for col in range(1, cols):
            count_ones = 0
            for row_idx in range(rows):
                count_ones += grid[row_idx][col]
            if count_ones < rows / 2:
                # Flip the column
                for row_idx in range(rows):
                    grid[row_idx][col] = 1 - grid[row_idx][col]
        score = 0
        for row in grid:
            score += self.convert_row_to_integer(row)
        return score

    def convert_row_to_integer(self, row):
        # Convert list of 0/1 to binary integer
        return int(''.join(str(e) for e in row), 2)