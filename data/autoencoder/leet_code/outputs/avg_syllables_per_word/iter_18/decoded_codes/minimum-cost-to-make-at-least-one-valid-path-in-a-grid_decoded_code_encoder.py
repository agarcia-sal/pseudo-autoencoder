import heapq
from typing import List, Tuple

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        column_count = len(grid[0])
        # directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        costs = self.generate_initial_costs(row_count, column_count)
        costs[0][0] = 0
        priority_queue = [(0, 0, 0)]  # (cost, row, column)
        visited_positions = set()

        while priority_queue:
            current_cost, current_row, current_column = self.extract_minimum_from_heap(priority_queue)

            if (current_row, current_column) in visited_positions:
                continue
            visited_positions.add((current_row, current_column))

            if current_row == row_count - 1 and current_column == column_count - 1:
                return current_cost

            for direction_index, (dr, dc) in enumerate(directions):
                next_row = current_row + dr
                next_column = current_column + dc

                if 0 <= next_row < row_count and 0 <= next_column < column_count:
                    # direction_index + 1 because grid directions are 1-based index for directions
                    if (direction_index + 1) != grid[current_row][current_column]:
                        additional_cost = 1
                    else:
                        additional_cost = 0

                    proposed_cost = current_cost + additional_cost

                    if proposed_cost < costs[next_row][next_column]:
                        costs[next_row][next_column] = proposed_cost
                        self.push_to_heap(priority_queue, (proposed_cost, next_row, next_column))

        return -1

    def generate_initial_costs(self, row_count: int, column_count: int) -> List[List[int]]:
        # create a 2D list filled with infinity values representing unreachable costs initially
        INF = float('inf')
        return [[INF for _ in range(column_count)] for _ in range(row_count)]

    def extract_minimum_from_heap(self, heap: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:
        # pop smallest element from heap
        return heapq.heappop(heap)

    def push_to_heap(self, heap: List[Tuple[int, int, int]], element: Tuple[int, int, int]) -> None:
        # push element into heap maintaining heap property
        heapq.heappush(heap, element)