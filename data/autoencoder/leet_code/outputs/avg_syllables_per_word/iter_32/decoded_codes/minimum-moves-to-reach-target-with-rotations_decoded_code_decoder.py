from collections import deque
from typing import List, Set, Tuple

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Queue stores tuples: (r1, c1, r2, c2, steps)
        queue = deque([(0, 0, 0, 1, 0)])
        visited: Set[Tuple[int, int, int, int]] = {(0, 0, 0, 1)}

        while queue:
            r1, c1, r2, c2, steps = queue.popleft()

            # Check if the snake is in the bottom-right position
            if r1 == n - 1 and c1 == n - 2 and r2 == n - 1 and c2 == n - 1:
                return steps

            # Move right
            if c2 + 1 < n and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0:
                new_state = (r1, c1 + 1, r2, c2 + 1)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((r1, c1 + 1, r2, c2 + 1, steps + 1))

            # Move down
            if r2 + 1 < n and grid[r1 + 1][c1] == 0 and grid[r2 + 1][c2] == 0:
                new_state = (r1 + 1, c1, r2 + 1, c2)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((r1 + 1, c1, r2 + 1, c2, steps + 1))

            # Rotate clockwise (from horizontal to vertical)
            if r1 == r2 and r1 + 1 < n and grid[r1 + 1][c1] == 0 and grid[r1 + 1][c2] == 0:
                new_state = (r1, c1, r1 + 1, c1)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((r1, c1, r1 + 1, c1, steps + 1))

            # Rotate counterclockwise (from vertical to horizontal)
            if c1 == c2 and c1 + 1 < n and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0:
                new_state = (r1, c1, r1, c1 + 1)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((r1, c1, r1, c1 + 1, steps + 1))

        return -1