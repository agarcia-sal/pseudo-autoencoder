def num_distinct_islands(grid):
    def dfs(x, y, island):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return
        grid[x][y] = 0
        island.append((x, y))
        dfs(x + 1, y, island)
        dfs(x - 1, y, island)
        dfs(x, y + 1, island)
        dfs(x, y - 1, island)

    islands = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                island = []
                dfs(i, j, island)
                shapes = []
                for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    transformed = sorted((x * dx, y * dy) for x, y in island)
                    min_x = transformed[0][0]
                    min_y = min(p[1] for p in transformed)
                    shifted = tuple((x - min_x, y - min_y) for x, y in transformed)
                    shapes.append(shifted)
                # Add rotated 90 degree versions
                for s in shapes[:4]:
                    rotated = tuple((y, -x) for x, y in s)
                    shapes.append(rotated)
                islands.add(min(shapes))
    return len(islands)