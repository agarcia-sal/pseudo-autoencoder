from typing import List, Set, Tuple

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(x: int, y: int, visited: Set[Tuple[int, int]]) -> None:
            if (
                x < 0 or x >= rows or
                y < 0 or y >= cols or
                (x, y) in visited or
                grid[x][y] == 0
            ):
                return
            visited.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy, visited)

        def is_connected() -> bool:
            visited = set()
            land_cells = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 1]
            if not land_cells:
                return True
            dfs(land_cells[0][0], land_cells[0][1], visited)
            return len(visited) == len(land_cells)

        if not is_connected():
            return 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not is_connected():
                        grid[i][j] = 1
                        return 1
                    grid[i][j] = 1

        return 2