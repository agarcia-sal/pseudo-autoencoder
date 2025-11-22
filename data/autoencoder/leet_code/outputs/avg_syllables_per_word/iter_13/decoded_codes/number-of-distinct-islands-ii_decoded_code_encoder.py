class Solution:
    def numDistinctIslands2(self, grid):
        def dfs(x, y, island):
            if (
                x < 0
                or x >= len(grid)
                or y < 0
                or y >= len(grid[0])
                or grid[x][y] == 0
            ):
                return
            grid[x][y] = 0
            island.append((x, y))
            dfs(x + 1, y, island)
            dfs(x - 1, y, island)
            dfs(x, y + 1, island)
            dfs(x, y - 1, island)

        def normalize(island):
            shapes = []
            # Four sign reflections
            for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_island = [(x * dx, y * dy) for x, y in island]
                new_island.sort()
                min_x = min(x for x, _ in new_island)
                min_y = min(y for _, y in new_island)
                shapes.append(tuple((x - min_x, y - min_y) for x, y in new_island))
            # Add rotations of previous shapes (90 degrees rotation: (x, y) -> (y, -x))
            for i in range(len(shapes)):
                shape = shapes[i]
                rotated = tuple((y, -x) for x, y in shape)
                shapes.append(rotated)
            return min(shapes)

        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = []
                    dfs(i, j, island)
                    islands.add(normalize(island))
        return len(islands)