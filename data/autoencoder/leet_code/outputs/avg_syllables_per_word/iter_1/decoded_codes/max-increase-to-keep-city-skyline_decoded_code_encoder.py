def calculate_total_increase(grid):
    n = len(grid)
    row_max = [max(row) for row in grid]
    col_max = [max(col) for col in zip(*grid)]
    total_inc = 0
    for i in range(n):
        for j in range(n):
            total_inc += max(0, min(row_max[i], col_max[j]) - grid[i][j])
    return total_inc