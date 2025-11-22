class Solution:
    def minTotalDistance(self, grid):
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
            diff = row - median_row
            if diff < 0:
                diff = -diff
            min_distance += diff
        for col in cols:
            diff = col - median_col
            if diff < 0:
                diff = -diff
            min_distance += diff

        return min_distance