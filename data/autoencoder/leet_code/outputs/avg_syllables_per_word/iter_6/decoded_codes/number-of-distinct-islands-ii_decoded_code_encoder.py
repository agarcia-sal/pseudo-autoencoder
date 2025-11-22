class Solution:
    def numDistinctIslands2(self, grid):
        def dfs(x, y, island):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return
            grid[x][y] = 0
            island.append((x, y))
            dfs(x + 1, y, island)
            dfs(x - 1, y, island)
            dfs(x, y + 1, island)
            dfs(x, y - 1, island)

        def normalize(island):
            shapes = []
            # rotations and reflections
            for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_island = sorted((x * dx, y * dy) for x, y in island)
                min_x = new_island[0][0]
                min_y = min(p[1] for p in new_island)
                normalized = tuple((x - min_x, y - min_y) for x, y in new_island)
                shapes.append(normalized)
            # add 90 degree rotations of each shape above
            for i in range(len(shapes)):
                rotated = tuple((y, -x) for x, y in shapes[i])
                shapes.append(rotated)
            return min(shapes)

        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = []
                    dfs(i, j, island)
                    # Normalize based on relative coordinates to origin
                    base_x, base_y = island[0]
                    island_rel = [(x - base_x, y - base_y) for x, y in island]
                    islands.add(normalize(island_rel))
        return len(islands)