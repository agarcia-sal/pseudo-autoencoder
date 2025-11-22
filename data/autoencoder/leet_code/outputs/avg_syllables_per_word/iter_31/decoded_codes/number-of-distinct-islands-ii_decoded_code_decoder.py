from typing import List, Set, Tuple

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int, island: List[Tuple[int, int]]) -> None:
            if (
                x < 0 or x >= len(grid)
                or y < 0 or y >= len(grid[0])
                or grid[x][y] == 0
            ):
                return
            grid[x][y] = 0
            island.append((x, y))
            dfs(x + 1, y, island)
            dfs(x - 1, y, island)
            dfs(x, y + 1, island)
            dfs(x, y - 1, island)

        def normalize(island: List[Tuple[int, int]]) -> Tuple[Tuple[int, int], ...]:
            shapes = []
            # 4 reflections: (dx, dy)
            for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_island = [(x * dx, y * dy) for x, y in island]
                new_island.sort()
                min_x = new_island[0][0]
                min_y = min(p[1] for p in new_island)
                normalized = tuple((x - min_x, y - min_y) for x, y in new_island)
                shapes.append(normalized)

            # For each shape above, add its 90-degree rotation (x,y) -> (y, -x)
            original_len = len(shapes)
            for i in range(original_len):
                shape = shapes[i]
                rotated = tuple(sorted((y, -x) for x, y in shape))
                min_x = rotated[0][0]
                min_y = min(p[1] for p in rotated)
                normalized_rotated = tuple((x - min_x, y - min_y) for x, y in rotated)
                shapes.append(normalized_rotated)

            return min(shapes)

        islands: Set[Tuple[Tuple[int, int], ...]] = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island: List[Tuple[int, int]] = []
                    dfs(i, j, island)
                    islands.add(normalize(island))

        return len(islands)