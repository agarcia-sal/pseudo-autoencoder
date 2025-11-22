from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        n = len(grid)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n

        def dfs(x, y, index):
            area = 1
            grid[x][y] = index
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and grid[nx][ny] == 1:
                    area += dfs(nx, ny, index)
            return area

        island_areas = {}
        index = 2  # Start from 2 to mark islands uniquely

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_areas[index] = dfs(i, j, index)
                    index += 1

        if not island_areas:
            return 1  # No islands, flipping one zero would make island size 1

        max_island_size = max(island_areas.values())

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if is_valid(nx, ny) and grid[nx][ny] > 1:
                            neighbors.add(grid[nx][ny])
                    current_island_size = 1 + sum(island_areas[k] for k in neighbors)
                    if current_island_size > max_island_size:
                        max_island_size = current_island_size

        return max_island_size