import heapq
import math

class Solution:
    def minCost(self, grid):
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        costs = self.initializeCosts(m, n)
        costs[0][0] = 0

        pq = self.initializePriorityQueue()
        self.pushHeap(pq, (0, 0, 0))
        visited = self.initializeVisitedSet()

        while pq:
            cost, i, j = self.popHeap(pq)

            if (i, j) in visited:
                continue
            visited.add((i, j))

            if i == m - 1 and j == n - 1:
                return cost

            for k in range(len(directions)):
                di, dj = directions[k]
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n:
                    grid_direction = grid[i][j]
                    increment_cost = 0 if (k + 1) == grid_direction else 1
                    new_cost = cost + increment_cost

                    if new_cost < costs[ni][nj]:
                        costs[ni][nj] = new_cost
                        self.pushHeap(pq, (new_cost, ni, nj))

        return -1

    def initializeCosts(self, m, n):
        return [[math.inf] * n for _ in range(m)]

    def initializePriorityQueue(self):
        return []

    def initializeVisitedSet(self):
        return set()

    def popHeap(self, pq):
        return heapq.heappop(pq)

    def pushHeap(self, pq, element):
        heapq.heappush(pq, element)