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

            # Initialize fire BFS with all initially burning cells
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        fire_times[i][j] = 0
                        queue.append((i, j, 0))

            # BFS for fire spread times
            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and fire_times[nx][ny] == inf:
                        fire_times[nx][ny] = t + 1
                        queue.append((nx, ny, t + 1))

            # BFS for player escape starting after waiting 'wait' minutes
            queue = deque()
            visited = set()

            # Starting position with time 'wait'
            if fire_times[0][0] <= wait:
                # Fire reaches start before or at wait time => cannot start safely
                return False
            queue.append((0, 0, wait))
            visited.add((0, 0))

            while queue:
                x, y, t = queue.popleft()
                # If at target cell, check fire time vs arrival time
                if x == m - 1 and y == n - 1:
                    # The player arrives at time t
                    # Player can stand at destination if fire arrives later or never arrives
                    if fire_times[x][y] >= t:
                        return True
                    else:
                        # Fire arrives sooner than or at player's arrival => fail
                        return False

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    nt = t + 1
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                        # Player can only move into the cell if fire arrives after player arrives
                        if fire_times[nx][ny] > nt:
                            visited.add((nx, ny))
                            queue.append((nx, ny, nt))

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

        if result != m * n:
            return result
        else:
            return 10 ** 9