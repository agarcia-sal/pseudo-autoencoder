from typing import List, Tuple

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int, island: List[Tuple[int, int]]):
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
                min_x = new_island[0][0]
                min_y = min(p[1] for p in new_island)
                normalized_shape = [(x - min_x, y - min_y) for x, y in new_island]
                shapes.append(tuple(normalized_shape))
            original_count = len(shapes)
            for i in range(original_count):
                rotated_shape = [(y, -x) for x, y in shapes[i]]
                shapes.append(tuple(rotated_shape))
            return min(shapes)

        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = []
                    dfs(i, j, island)
                    islands.add(normalize(island))
        return len(islands)