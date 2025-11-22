from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Flip rows where the first element is 0
        for row in grid:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]

        # Flip columns where the count of ones is less than half the number of rows
        for col in range(1, len(grid[0])):
            count_ones = 0
            for row_index in range(len(grid)):
                count_ones += grid[row_index][col]
            if count_ones < len(grid) / 2:
                for row_index in range(len(grid)):
                    grid[row_index][col] = 1 - grid[row_index][col]

        # Calculate total score
        score = 0
        for row in grid:
            binary_number = ''.join(str(bit) for bit in row)
            score += int(binary_number, 2)

        return score