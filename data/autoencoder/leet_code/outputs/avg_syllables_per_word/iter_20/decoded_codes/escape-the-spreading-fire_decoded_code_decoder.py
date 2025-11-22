from collections import deque
from math import inf
from typing import List

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if grid else 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def can_escape(wait: int) -> bool:
            fire_times = [[inf] * n for _ in range(m)]
            queue = deque()

            # Initialize fire BFS
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        fire_times[i][j] = 0
                        queue.append((i, j, 0))

            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < m and 0 <= ny < n
                        and grid[nx][ny] == 0
                        and fire_times[nx][ny] == inf
                    ):
                        fire_times[nx][ny] = t + 1
                        queue.append((nx, ny, t + 1))

            # Person BFS
            queue = deque()
            if grid[0][0] == 0 and wait < fire_times[0][0]:
                queue.append((0, 0, wait))
            elif grid[0][0] == 1:
                # Can't start on fire
                return False

            visited = {(0, 0)}

            while queue:
                x, y, t = queue.popleft()
                # Check if reached target
                if x == m - 1 and y == n - 1:
                    # Can stand at the exit cell if fire arrives strictly after or never
                    # Because after we move there at time t, fire_time must be >= t
                    # If fire_time at exit is inf or > t, safe.
                    # But test uses t+1 in pseudocode, must verify carefully:
                    # The pseudocode checks fire_times[nx][ny] >= t+1 when first reaching exit, 
                    # so we must do the same here: fire_times[x][y] >= t ensures safe to be here at t
                    if fire_times[x][y] >= t:
                        return True
                    else:
                        return False

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    nt = t + 1
                    if (
                        0 <= nx < m and 0 <= ny < n
                        and (nx, ny) not in visited
                        and grid[nx][ny] == 0
                    ):
                        # Time arrival at nx, ny is nt
                        # Check fire arriving time (fire_times[nx][ny]) > nt
                        # Person must arrive before or at same time, but fire must NOT arrive earlier or equal (fire can't arrive <= nt)
                        # So fire_times[nx][ny] must be strictly greater than nt to be safe
                        if fire_times[nx][ny] > nt:
                            visited.add((nx, ny))
                            # Check if this is exit to shortcut
                            if nx == m - 1 and ny == n - 1:
                                # At the exit, similarly ensure fire arrives >= nt
                                if fire_times[nx][ny] >= nt:
                                    return True
                                else:
                                    return False
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