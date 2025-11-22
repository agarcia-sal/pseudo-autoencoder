from heapq import heappush, heappop
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

        directions: List[Tuple[int, int]] = [(0,1), (0,-1), (1,0), (-1,0)]
        costs = [[inf]*n for _ in range(m)]
        costs[0][0] = 0

        pq: List[Tuple[int, int, int]] = [(0, 0, 0)]  # (cost, i, j)
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
                    # grid[i][j] is 1-based direction index, directions list is 0-based
                    # So if k+1 != grid[i][j], cost increases by 1; else zero
                    new_cost = cost if (k + 1) == grid[i][j] else cost + 1
                    if new_cost < costs[ni][nj]:
                        costs[ni][nj] = new_cost
                        heappush(pq, (new_cost, ni, nj))
        return -1