class Solution:
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1

        m = len(grid)
        n = len(grid[0])
        total_distance = [[0 for _ in range(n)] for _ in range(m)]
        reach_count = [[0 for _ in range(n)] for _ in range(m)]
        building_count = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(start_x, start_y):
            from collections import deque

            queue = deque()
            queue.append((start_x, start_y))
            visited = [[False for _ in range(n)] for _ in range(m)]
            visited[start_x][start_y] = True
            distance = 0
            reachable = 0

            while queue:
                size = len(queue)
                distance += 1
                for _ in range(size):
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy
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

        min_distance = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach_count[i][j] == building_count:
                    if total_distance[i][j] < min_distance:
                        min_distance = total_distance[i][j]

        if min_distance == float('inf'):
            return -1
        else:
            return min_distance