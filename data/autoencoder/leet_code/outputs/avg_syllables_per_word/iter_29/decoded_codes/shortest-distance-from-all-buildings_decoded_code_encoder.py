from collections import deque
from math import inf

class Solution:
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1

        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        total_distance = [[0] * number_of_columns for _ in range(number_of_rows)]
        reach_count = [[0] * number_of_columns for _ in range(number_of_rows)]
        building_count = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(start_x, start_y):
            queue = deque([(start_x, start_y)])
            visited = [[False] * number_of_columns for _ in range(number_of_rows)]
            visited[start_x][start_y] = True
            distance = 0
            reachable = 0

            while queue:
                size = len(queue)
                distance += 1
                for _ in range(size):
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if (0 <= nx < number_of_rows and 0 <= ny < number_of_columns and
                            not visited[nx][ny] and grid[nx][ny] == 0):
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            total_distance[nx][ny] += distance
                            reach_count[nx][ny] += 1
                            reachable += 1
            return reachable

        for i in range(number_of_rows):
            for j in range(number_of_columns):
                if grid[i][j] == 1:
                    building_count += 1
                    if bfs(i, j) < building_count - 1:
                        return -1

        min_distance = inf
        for i in range(number_of_rows):
            for j in range(number_of_columns):
                if grid[i][j] == 0 and reach_count[i][j] == building_count:
                    if total_distance[i][j] < min_distance:
                        min_distance = total_distance[i][j]

        return -1 if min_distance == inf else min_distance