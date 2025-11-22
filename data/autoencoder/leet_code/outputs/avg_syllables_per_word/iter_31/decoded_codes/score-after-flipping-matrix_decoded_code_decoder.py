from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        # Flip rows if the first element is 0 to ensure leading 1
        for row in grid:
            if row[0] == 0:
                for i in range(cols):
                    row[i] = 1 - row[i]

        # For each column (except first), flip column if number of 1's is less than half of rows
        for col in range(1, cols):
            count_ones = sum(grid[row][col] for row in range(rows))
            if count_ones < rows / 2:
                for row in range(rows):
                    grid[row][col] = 1 - grid[row][col]

        total_score = 0
        for row in grid:
            binary_str = ''.join(str(bit) for bit in row)
            total_score += int(binary_str, 2)

        return total_score