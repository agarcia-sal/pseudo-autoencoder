from typing import List, Tuple


class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int, island: List[Tuple[int, int]]) -> None:
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

        def sortCoordinates(coords: List[Tuple[int, int]]) -> None:
            coords.sort()

        def shiftCoordinates(
            coords: List[Tuple[int, int]], min_x: int, min_y: int
        ) -> Tuple[Tuple[int, int], ...]:
            # shift all coords so that min_x and min_y map to (0,0)
            return tuple((x - min_x, y - min_y) for x, y in coords)

        def rotateCoordinates90(
            coords: Tuple[Tuple[int, int], ...],
        ) -> Tuple[Tuple[int, int], ...]:
            # rotate each coordinate 90 degrees clockwise: (x, y) -> (y, -x)
            rotated = [(y, -x) for x, y in coords]
            rotated = sorted(rotated)
            min_x = rotated[0][0]
            min_y = rotated[0][1]
            return tuple((x - min_x, y - min_y) for x, y in rotated)

        def normalize(island: List[Tuple[int, int]]) -> Tuple[Tuple[int, int], ...]:
            shapes = []
            for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_island = [(x * dx, y * dy) for x, y in island]
                sortCoordinates(new_island)
                min_x = new_island[0][0]
                min_y = min(y for _, y in new_island)
                shifted_shape = shiftCoordinates(new_island, min_x, min_y)
                shapes.append(shifted_shape)
            original_length = len(shapes)
            for i in range(original_length):
                rotated_shape = rotateCoordinates90(shapes[i])
                shapes.append(rotated_shape)
            canonical_shape = min(shapes)
            return canonical_shape

        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = []
                    dfs(i, j, island)
                    # Normalize relative positions
                    # Need to translate coordinates so minimal coordinate is (0,0)
                    # To do this relative to island min coords:
                    min_x = min(x for x, _ in island)
                    min_y = min(y for _, y in island)
                    relative_island = [(x - min_x, y - min_y) for x, y in island]
                    normalized_island = normalize(relative_island)
                    islands.add(normalized_island)
        return len(islands)