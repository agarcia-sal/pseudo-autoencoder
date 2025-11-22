from typing import List, Tuple

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int, island: List[Tuple[int, int]]) -> None:
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return
            grid[x][y] = 0
            island.append((x, y))
            dfs(x + 1, y, island)
            dfs(x - 1, y, island)
            dfs(x, y + 1, island)
            dfs(x, y - 1, island)

        def normalize(island: List[Tuple[int, int]]) -> Tuple[Tuple[int, int], ...]:
            shapes = []
            transforms = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dx, dy in transforms:
                new_island = []
                for x, y in island:
                    new_island.append((x * dx, y * dy))
                new_island.sort()
                min_x = new_island[0][0]
                min_y = new_island[0][1]
                shape = tuple((x - min_x, y - min_y) for x, y in new_island)
                shapes.append(shape)
            # add 90 degree rotations (x, y) -> (y, -x)
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
                    if island:
                        islands.add(normalize(island))
        return len(islands)