import heapq
from math import inf

class Solution:
    def minCost(self, grid):
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        costs = [[inf] * number_of_columns for _ in range(number_of_rows)]
        costs[0][0] = 0
        priority_queue = [(0, 0, 0)]  # (cost, i, j)
        visited_positions = set()

        while priority_queue:
            cost, i, j = heapq.heappop(priority_queue)
            if (i, j) in visited_positions:
                continue
            visited_positions.add((i, j))

            if i == number_of_rows - 1 and j == number_of_columns - 1:
                return cost

            for k, (delta_i, delta_j) in enumerate(directions):
                new_i = i + delta_i
                new_j = j + delta_j
                if 0 <= new_i < number_of_rows and 0 <= new_j < number_of_columns:
                    additional_cost = 0 if (k + 1) == grid[i][j] else 1
                    new_cost = cost + additional_cost
                    if new_cost < costs[new_i][new_j]:
                        costs[new_i][new_j] = new_cost
                        heapq.heappush(priority_queue, (new_cost, new_i, new_j))

        return -1