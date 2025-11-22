from collections import deque
from math import inf

class Solution:
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        total_distance = self.initializeMatrix(m, n)
        reach_count = self.initializeMatrix(m, n)
        building_count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(start_x, start_y):
            queue = self.initializeQueue(start_x, start_y)
            visited = self.initializeVisited(m, n)
            distance = 0
            reachable = 0

            while queue:
                size = len(queue)
                distance += 1
                for _ in range(size):
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            total_distance[nx][ny] += distance
                            reach_count[nx][ny] += 1
                            reachable += 1
            return reachable

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    building_count += 1
                    if bfs(i, j) < building_count - 1:
                        return -1

        min_distance = inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach_count[i][j] == building_count:
                    if total_distance[i][j] < min_distance:
                        min_distance = total_distance[i][j]

        return -1 if min_distance == inf else min_distance

    def initializeMatrix(self, rows, cols):
        return [[0] * cols for _ in range(rows)]

    def initializeQueue(self, start_x, start_y):
        q = deque()
        q.append((start_x, start_y))
        return q

    def initializeVisited(self, rows, cols):
        return [[False] * cols for _ in range(rows)]