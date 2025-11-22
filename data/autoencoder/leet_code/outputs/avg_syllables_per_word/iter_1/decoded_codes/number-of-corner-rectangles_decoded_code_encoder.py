def count_corner_rectangles(grid):
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    count = 0
    for i in range(m):
        for j in range(i + 1, m):
            cols = sum(1 for k in range(n) if grid[i][k] == 1 and grid[j][k] == 1)
            if cols >= 2:
                count += cols * (cols - 1) // 2
    return count