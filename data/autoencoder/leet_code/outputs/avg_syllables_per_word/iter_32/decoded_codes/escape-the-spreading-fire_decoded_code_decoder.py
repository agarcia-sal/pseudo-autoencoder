from collections import deque
from math import inf

class Solution:
    def maximumMinutes(self, grid) -> int:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def can_escape(wait: int) -> bool:
            fire_times = [[inf]*n for _ in range(m)]
            queue = deque()

            # Initialize fire positions and times
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        queue.append((i, j, 0))
                        fire_times[i][j] = 0

            # BFS to compute earliest fire arrival times to each cell
            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and fire_times[nx][ny] == inf:
                        fire_times[nx][ny] = t + 1
                        queue.append((nx, ny, t + 1))

            # BFS for the person starting at (0, 0) after waiting 'wait' minutes
            if fire_times[0][0] <= wait:
                # Fire reaches start before or at wait time, no escape
                return False

            queue = deque()
            queue.append((0, 0, wait))
            visited = {(0, 0)}

            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == 0:
                        nt = t + 1
                        # If reached bottom-right corner
                        if nx == m - 1 and ny == n - 1:
                            # Can stay there after arrival, fire arrives at fire_times[nx][ny]
                            # Person escapes if fire arrives at same time or later
                            if fire_times[nx][ny] >= nt:
                                return True
                            else:
                                return False
                        # If safe to move there before fire arrives
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
            return 10**9