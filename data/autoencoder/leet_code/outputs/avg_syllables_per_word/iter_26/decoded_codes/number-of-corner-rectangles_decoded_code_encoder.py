from typing import List

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        count = 0

        for i in range(number_of_rows):
            for j in range(i + 1, number_of_rows):
                columns_with_ones = 0
                for k in range(number_of_columns):
                    if grid[i][k] == 1 and grid[j][k] == 1:
                        columns_with_ones += 1
                if columns_with_ones >= 2:
                    count += columns_with_ones * (columns_with_ones - 1) // 2

        return count