import heapq
from math import inf

class Solution:
    def minCost(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        # Directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        costs = [[inf] * n for _ in range(m)]
        costs[0][0] = 0
        pq = [(0, 0, 0)]  # (cost, i, j)
        visited = set()

        while pq:
            cost, i, j = heapq.heappop(pq)
            if (i, j) in visited:
                continue
            visited.add((i, j))

            if i == m - 1 and j == n - 1:
                return cost

            for k, (di, dj) in enumerate(directions):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if cost + 1 < costs[ni][nj] and (k + 1) != grid[i][j]:
                        new_cost = cost + 1
                    else:
                        new_cost = cost
                    if new_cost < costs[ni][nj]:
                        costs[ni][nj] = new_cost
                        heapq.heappush(pq, (new_cost, ni, nj))

        return -1