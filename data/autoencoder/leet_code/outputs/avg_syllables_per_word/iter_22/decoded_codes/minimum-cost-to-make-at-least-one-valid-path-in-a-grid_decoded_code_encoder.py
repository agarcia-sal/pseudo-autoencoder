from heapq import heappush, heappop
from math import inf

class Solution:
    def minCost(self, grid):
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        costs = [[inf] * n for _ in range(m)]
        costs[0][0] = 0
        pq = [(0, 0, 0)]  # cost, i, j
        visited = set()

        while pq:
            cost, i, j = heappop(pq)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i == m - 1 and j == n - 1:
                return cost

            for k, (di, dj) in enumerate(directions):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    # if direction (k+1) matches grid[i][j], no extra cost; else cost + 1
                    new_cost = cost + (0 if (k + 1) == grid[i][j] else 1)
                    if new_cost < costs[ni][nj]:
                        costs[ni][nj] = new_cost
                        heappush(pq, (new_cost, ni, nj))

        return -1