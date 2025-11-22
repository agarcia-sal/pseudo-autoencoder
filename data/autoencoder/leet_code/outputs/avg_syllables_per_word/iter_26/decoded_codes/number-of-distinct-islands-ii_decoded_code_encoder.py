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
            # Four transformations with dx, dy in {(1,1), (1,-1), (-1,1), (-1,-1)}
            for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_island = sorted((x * dx, y * dy) for x, y in island)
                min_x = new_island[0][0]
                min_y = min(y for _, y in new_island)
                normalized = tuple((x - min_x, y - min_y) for x, y in new_island)
                shapes.append(normalized)

            size = len(shapes)
            # Rotate each shape 90 degrees clockwise: (x, y) -> (y, -x)
            for i in range(size):
                rotated = sorted((y, -x) for x, y in shapes[i])
                min_x = rotated[0][0]
                min_y = min(y for _, y in rotated)
                normalized_rotated = tuple((x - min_x, y - min_y) for x, y in rotated)
                shapes.append(normalized_rotated)

            return min(shapes)

        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = []
                    dfs(i, j, island)
                    islands.add(normalize(island))
        return len(islands)