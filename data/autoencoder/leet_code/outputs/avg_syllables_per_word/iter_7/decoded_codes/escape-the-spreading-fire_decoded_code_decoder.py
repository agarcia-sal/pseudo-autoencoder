from collections import deque
from typing import List

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def can_escape(wait: int) -> bool:
            fire_times = [[float('inf')] * n for _ in range(m)]
            queue = deque()

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        queue.append((i, j, 0))
                        fire_times[i][j] = 0

            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and fire_times[nx][ny] == float('inf'):
                        fire_times[nx][ny] = t + 1
                        queue.append((nx, ny, t + 1))

            queue = deque()
            queue.append((0, 0, wait))
            visited = {(0, 0)}

            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == 0:
                        time_after_move = t + 1
                        if nx == m - 1 and ny == n - 1:
                            if fire_times[nx][ny] >= time_after_move:
                                return True
                            else:
                                return False
                        if fire_times[nx][ny] > time_after_move:
                            visited.add((nx, ny))
                            queue.append((nx, ny, time_after_move))
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

        return 10**9 if result == m * n else result