import heapq
from math import inf
from typing import List, Tuple

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        if n == 0:
            return -1

        # directions correspond to right, left, down, up
        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # costs matrix initialized to infinity
        costs = [[inf] * n for _ in range(m)]
        costs[0][0] = 0

        # Min-heap priority queue, elements are tuples: (cost, i, j)
        pq = [(0, 0, 0)]

        visited = set()

        while pq:
            cost, i, j = heapq.heappop(pq)

            if (i, j) in visited:
                continue
            visited.add((i, j))

            # If reached bottom-right cell
            if i == m - 1 and j == n - 1:
                return cost

            for k, (di, dj) in enumerate(directions):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    # According to grid[i][j], the direction at cell (i,j) is grid[i][j]
                    # The directions list is 0:right,1:left,2:down,3:up
                    # If direction matches k, then no additional cost, else +1
                    additional_cost = 0 if (k + 1) == grid[i][j] else 1
                    new_cost = cost + additional_cost
                    if new_cost < costs[ni][nj]:
                        costs[ni][nj] = new_cost
                        heapq.heappush(pq, (new_cost, ni, nj))

        return -1