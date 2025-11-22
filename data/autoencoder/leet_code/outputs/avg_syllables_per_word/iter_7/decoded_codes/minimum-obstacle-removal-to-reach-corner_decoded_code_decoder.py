from heapq import heappush, heappop
from typing import List, Tuple

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        min_heap: List[Tuple[int, int, int]] = [(0, 0, 0)]  # cost, x, y
        visited = {(0, 0)}

        while min_heap:
            cost, x, y = heappop(min_heap)
            if (x, y) == (m - 1, n - 1):
                return cost
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    new_cost = cost + grid[nx][ny]
                    heappush(min_heap, (new_cost, nx, ny))

        return -1