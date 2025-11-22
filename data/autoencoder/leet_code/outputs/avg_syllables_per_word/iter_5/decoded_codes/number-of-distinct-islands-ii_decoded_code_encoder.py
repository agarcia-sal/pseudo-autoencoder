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
            for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_island = sorted((x * dx, y * dy) for x, y in island)
                min_x = new_island[0][0]
                min_y = min(p[1] for p in new_island)
                norm = tuple((x - min_x, y - min_y) for x, y in new_island)
                shapes.append(norm)
            for i in range(len(shapes)):
                shapes.append(tuple((y, -x) for x, y in shapes[i]))
            return min(shapes)

        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = []
                    dfs(i, j, island)
                    shapes = normalize([(x - i0, y - j0) for x, y in island]) if (i0:=island[0][0]) or True else normalize(island)
                    islands.add(normalize([(x - island[0][0], y - island[0][1]) for x, y in island]))
        return len(islands)