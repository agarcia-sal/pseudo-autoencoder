from collections import deque
from typing import List

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def can_escape(wait: int) -> bool:
            fire_times = [[float('inf')] * n for _ in range(m)]
            queue = deque()

            # Initialize fire times and queue with all fire sources
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        fire_times[i][j] = 0
                        queue.append((i, j, 0))

            # BFS to compute fire arrival times
            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 0 and fire_times[nx][ny] == float('inf'):
                            fire_times[nx][ny] = t + 1
                            queue.append((nx, ny, t + 1))

            # BFS for the person to escape starting after waiting `wait` minutes
            queue = deque()
            visited = set()
            if fire_times[0][0] <= wait:
                # Fire reaches start before or at wait time, can't start
                return False
            queue.append((0, 0, wait))
            visited.add((0, 0))

            while queue:
                x, y, t = queue.popleft()
                if x == m - 1 and y == n - 1:
                    # If we already at exit, check if fire arrives later or at same time but allow that?
                    # Problem states fire_times is time fire arrives, so:
                    # If arrival time fire >= t, then safe, else no.
                    # Here t is current time (when person arrives)
                    if fire_times[x][y] >= t:
                        return True
                    else:
                        # Even if at exit but fire here earlier, must fail based on problem statement.
                        return False
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    nt = t + 1
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 0 and (nx, ny) not in visited:
                            # Fire should arrive after person moves in
                            if fire_times[nx][ny] >= nt:
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