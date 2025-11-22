from collections import deque
from typing import List, Tuple, Set

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])

        # If k is large enough to go straight to the end without considering obstacles
        if k >= m + n - 2:
            return m + n - 2

        directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue: deque = deque()
        visited: Set[Tuple[int, int, int]] = set()

        # Each element is (x, y, remaining_k, steps)
        queue.append((0, 0, k, 0))
        visited.add((0, 0, k))

        while queue:
            x, y, remaining_k, steps = queue.popleft()

            if x == m - 1 and y == n - 1:
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_k = remaining_k - grid[nx][ny]
                    if new_k >= 0:
                        state = (nx, ny, new_k)
                        if state not in visited:
                            visited.add(state)
                            queue.append((nx, ny, new_k, steps + 1))

        return -1