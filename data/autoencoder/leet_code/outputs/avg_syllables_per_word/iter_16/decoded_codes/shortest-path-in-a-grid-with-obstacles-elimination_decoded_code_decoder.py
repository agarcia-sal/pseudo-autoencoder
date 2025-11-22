from collections import deque

class Solution:
    def shortestPath(self, grid, k):
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:
            return m + n - 2

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        queue = deque([(0, 0, k, 0)])  # x, y, remaining_k, steps
        visited = {(0, 0, k)}

        while queue:
            x, y, remaining_k, steps = queue.popleft()
            if x == m - 1 and y == n - 1:
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_k = remaining_k - grid[nx][ny]
                    if new_k >= 0 and (nx, ny, new_k) not in visited:
                        visited.add((nx, ny, new_k))
                        queue.append((nx, ny, new_k, steps + 1))

        return -1