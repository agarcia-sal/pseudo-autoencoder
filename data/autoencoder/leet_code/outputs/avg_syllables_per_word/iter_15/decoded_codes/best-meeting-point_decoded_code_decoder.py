from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        rows.sort()
        cols.sort()

        median_row = rows[len(rows) // 2]
        median_col = cols[len(cols) // 2]

        min_distance = 0
        for row in rows:
            min_distance += abs(row - median_row)
        for col in cols:
            min_distance += abs(col - median_col)

        return min_distance