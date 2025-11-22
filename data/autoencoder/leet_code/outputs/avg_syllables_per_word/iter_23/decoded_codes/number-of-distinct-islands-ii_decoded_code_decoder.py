from typing import List, Tuple, Set

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
            for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_island = [(x * dx, y * dy) for x, y in island]
                new_island.sort()
                min_x = min(x for x, _ in new_island)
                min_y = min(y for _, y in new_island)
                normalized = tuple((x - min_x, y - min_y) for x, y in new_island)
                shapes.append(normalized)
            # add rotations: (x, y) -> (y, -x)
            shape_count = len(shapes)
            for i in range(shape_count):
                new_shape = tuple((y, -x) for x, y in shapes[i])
                shapes.append(new_shape)
            return min(shapes)

        islands: Set[Tuple[Tuple[int, int], ...]] = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = []
                    dfs(i, j, island)
                    islands.add(normalize(island))
        return len(islands)