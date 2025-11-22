from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Flip rows to make sure the first element in each row is 1
        for row in grid:
            if row[0] == 0:
                for i in range(n):
                    row[i] = 1 - row[i]

        # For each column from the second to last, flip if zeros are more than ones
        for col in range(1, n):
            count_ones = 0
            for row in range(m):
                count_ones += grid[row][col]
            if count_ones < m / 2:
                for row in range(m):
                    grid[row][col] = 1 - grid[row][col]

        score = 0
        for row in grid:
            binary_number = ''.join(str(bit) for bit in row)
            score += int(binary_number, 2)

        return score