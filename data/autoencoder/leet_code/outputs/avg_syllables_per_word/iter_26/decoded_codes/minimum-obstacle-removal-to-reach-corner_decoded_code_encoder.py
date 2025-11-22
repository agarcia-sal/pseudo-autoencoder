import heapq
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minimum_heap = [(0, 0, 0)]  # cost, x, y
        visited_positions = {(0, 0)}

        while minimum_heap:
            cost, x_coordinate, y_coordinate = heapq.heappop(minimum_heap)

            if (x_coordinate, y_coordinate) == (number_of_rows - 1, number_of_columns - 1):
                return cost

            for dx, dy in directions:
                new_x = x_coordinate + dx
                new_y = y_coordinate + dy

                if 0 <= new_x < number_of_rows and 0 <= new_y < number_of_columns and (new_x, new_y) not in visited_positions:
                    visited_positions.add((new_x, new_y))
                    new_cost = cost + grid[new_x][new_y]
                    heapq.heappush(minimum_heap, (new_cost, new_x, new_y))

        return -1