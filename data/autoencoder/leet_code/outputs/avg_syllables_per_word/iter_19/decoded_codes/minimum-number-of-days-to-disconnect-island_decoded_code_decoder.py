from typing import List, Set, Tuple

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int, visited: Set[Tuple[int, int]]) -> None:
            if (
                x < 0 or x >= len(grid) or
                y < 0 or y >= len(grid[0]) or
                (x, y) in visited or
                grid[x][y] == 0
            ):
                return
            visited.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy, visited)

        def is_connected() -> bool:
            visited = set()
            land_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1]
            if not land_cells:
                return True
            start_x, start_y = land_cells[0]
            dfs(start_x, start_y, visited)
            return len(visited) == len(land_cells)

        if not is_connected():
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not is_connected():
                        return 1
                    grid[i][j] = 1

        return 2