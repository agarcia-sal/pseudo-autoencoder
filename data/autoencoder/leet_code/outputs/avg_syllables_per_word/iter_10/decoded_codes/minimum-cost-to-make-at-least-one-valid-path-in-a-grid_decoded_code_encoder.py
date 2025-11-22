import heapq

class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        costs = [[float('inf')] * n for _ in range(m)]
        costs[0][0] = 0
        pq = [(0, 0, 0)]
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
                    new_cost = cost + (0 if k + 1 == grid[i][j] else 1)
                    if new_cost < costs[ni][nj]:
                        costs[ni][nj] = new_cost
                        heapq.heappush(pq, (new_cost, ni, nj))
        return -1