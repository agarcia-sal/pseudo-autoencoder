from collections import deque
from math import inf

class Solution:
    def maximumMinutes(self, grid):
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def can_escape(wait):
            fire_times = [[inf]*n for _ in range(m)]
            queue = deque()

            # Initialize fire_times with fire starting points and enqueue them
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        fire_times[i][j] = 0
                        queue.append((i, j, 0))

            # BFS for fire spreading times
            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and fire_times[nx][ny] == inf:
                        fire_times[nx][ny] = t + 1
                        queue.append((nx, ny, t + 1))

            # BFS for person escape considering wait time
            queue = deque()
            queue.append((0, 0, wait))
            visited = {(0, 0)}

            # If initial cell is on fire at or before wait start, no escape
            # Also if fire_time at start is 0 and wait > 0, no escape is possible
            # But per problem, if fire_times[0][0] <= wait, then cannot start safely (fire arrives before or immediately)
            if fire_times[0][0] <= wait:
                return False
            if grid[0][0] == 1:
                # start cell is fire, no escape
                return False

            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == 0:
                        # If we've reached the exit cell m-1,n-1
                        if nx == m - 1 and ny == n - 1:
                            # Person arrives at t+1, check if fire arrives same or earlier
                            # fire_times[nx][ny] is time fire arrives, can be inf if never
                            if fire_times[nx][ny] >= t + 1:
                                return True
                            else:
                                return False
                        # Person can only move to cell if fire comes strictly after t+1 (person arrives before fire)
                        if fire_times[nx][ny] > t + 1:
                            visited.add((nx, ny))
                            queue.append((nx, ny, t + 1))
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
            return 10**9
        else:
            return result