from collections import deque
from math import inf

class Solution:
    def maximumMinutes(self, grid):
        m = len(grid)
        n = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def can_escape(wait):
            fire_times = [[inf] * n for _ in range(m)]
            queue = deque()

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        queue.append((i, j, 0))
                        fire_times[i][j] = 0

            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and fire_times[nx][ny] == inf:
                        fire_times[nx][ny] = t + 1
                        queue.append((nx, ny, t + 1))

            queue = deque([(0, 0, wait)])
            visited = {(0, 0)}

            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == 0:
                        arrival_time = t + 1
                        # If destination reached
                        if nx == m - 1 and ny == n - 1:
                            if fire_times[nx][ny] >= arrival_time:
                                return True
                            else:
                                return False
                        if fire_times[nx][ny] > arrival_time:
                            visited.add((nx, ny))
                            queue.append((nx, ny, arrival_time))

            return False

        left, right = 0, m * n
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if can_escape(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        if result == m * n:
            return 10 ** 9
        return result