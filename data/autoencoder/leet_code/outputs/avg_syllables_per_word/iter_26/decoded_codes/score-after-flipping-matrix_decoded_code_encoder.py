from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0]) if row_count > 0 else 0

        # Ensure the first element in each row is 1 by flipping the entire row if needed
        for row in grid:
            if row[0] == 0:
                for i in range(col_count):
                    row[i] = 1 - row[i]

        # For each column starting from the second, flip the column if it has fewer than half ones
        for col in range(1, col_count):
            count_ones = sum(grid[row][col] for row in range(row_count))
            if count_ones < row_count / 2:
                for row in range(row_count):
                    grid[row][col] = 1 - grid[row][col]

        # Calculate the total score by interpreting each row as a binary number
        total_score = 0
        for row in grid:
            binary_str = ''.join(str(bit) for bit in row)
            total_score += int(binary_str, 2)

        return total_score