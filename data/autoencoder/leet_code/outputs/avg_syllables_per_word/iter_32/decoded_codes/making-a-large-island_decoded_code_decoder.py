from typing import List, Dict, Set, Tuple

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_valid(x: int, y: int) -> bool:
            return 0 <= x < n and 0 <= y < n

        def dfs(x: int, y: int, index: int) -> int:
            area = 1
            grid[x][y] = index
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and grid[nx][ny] == 1:
                    area += dfs(nx, ny, index)
            return area

        island_areas: Dict[int, int] = {}
        index = 2  # start index at 2 to distinguish from original 0 and 1 in grid

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_areas[index] = dfs(i, j, index)
                    index += 1

        if not island_areas:
            # no island present, so flipping one 0 to 1 creates an island of size 1
            return 1

        max_island_size = max(island_areas.values())

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors: Set[int] = set()
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if is_valid(nx, ny) and grid[nx][ny] > 1:
                            neighbors.add(grid[nx][ny])
                    current_island_size = 1 + sum(island_areas[idx] for idx in neighbors)
                    if current_island_size > max_island_size:
                        max_island_size = current_island_size

        return max_island_size