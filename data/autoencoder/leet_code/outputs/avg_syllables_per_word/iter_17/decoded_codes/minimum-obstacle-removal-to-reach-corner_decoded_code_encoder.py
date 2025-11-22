import heapq
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        min_heap = [(0, 0, 0)]
        visited = {(0, 0)}

        while min_heap:
            cost, x, y = heapq.heappop(min_heap)
            if (x, y) == (number_of_rows - 1, number_of_columns - 1):
                return cost
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < number_of_rows and 0 <= ny < number_of_columns and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    new_cost = cost + grid[nx][ny]
                    heapq.heappush(min_heap, (new_cost, nx, ny))

        return -1