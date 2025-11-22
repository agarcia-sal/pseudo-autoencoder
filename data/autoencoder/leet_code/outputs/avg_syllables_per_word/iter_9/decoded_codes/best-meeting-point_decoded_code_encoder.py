class Solution:
    def minTotalDistance(self, grid):
        rows, cols = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        rows.sort()
        cols.sort()
        median_row = rows[len(rows) // 2]
        median_col = cols[len(cols) // 2]
        min_distance = sum(abs(r - median_row) for r in rows) + sum(abs(c - median_col) for c in cols)
        return min_distance