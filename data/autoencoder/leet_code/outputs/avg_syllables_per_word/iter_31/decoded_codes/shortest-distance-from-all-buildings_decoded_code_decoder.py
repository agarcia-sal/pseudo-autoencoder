from collections import deque
from math import inf
from typing import List

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        total_distance = [[0] * n for _ in range(m)]
        reach_count = [[0] * n for _ in range(m)]
        building_count = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(start_x: int, start_y: int) -> int:
            visited = [[False] * n for _ in range(m)]
            visited[start_x][start_y] = True
            queue = deque([(start_x, start_y)])
            distance = 0
            reachable = 0

            while queue:
                distance += 1
                size = len(queue)
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

        return min_distance if min_distance != inf else -1