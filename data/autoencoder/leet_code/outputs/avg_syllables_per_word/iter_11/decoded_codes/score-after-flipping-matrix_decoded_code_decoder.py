class Solution:
    def matrixScore(self, grid):
        for row in grid:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]

        for col in range(1, len(grid[0])):
            count_ones = 0
            for row_index in range(len(grid)):
                count_ones += grid[row_index][col]
            if count_ones < len(grid) / 2:
                for row_index in range(len(grid)):
                    grid[row_index][col] = 1 - grid[row_index][col]

        score = 0
        for row in grid:
            binary_number_string = ""
            for bit in row:
                binary_number_string += str(bit)
            score += int(binary_number_string, 2)

        return score