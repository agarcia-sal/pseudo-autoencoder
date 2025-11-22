from collections import deque
from typing import List

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque([(0, 0, 0, 1, 0)])  # (r1, c1, r2, c2, steps)
        visited = {(0, 0, 0, 1)}

        while queue:
            r1, c1, r2, c2, steps = queue.popleft()

            if r1 == n - 1 and c1 == n - 2 and r2 == n - 1 and c2 == n - 1:
                return steps

            # Move right
            if c2 + 1 < n and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0:
                state = (r1, c1 + 1, r2, c2 + 1)
                if state not in visited:
                    visited.add(state)
                    queue.append((r1, c1 + 1, r2, c2 + 1, steps + 1))

            # Move down
            if r2 + 1 < n and grid[r1 + 1][c1] == 0 and grid[r2 + 1][c2] == 0:
                state = (r1 + 1, c1, r2 + 1, c2)
                if state not in visited:
                    visited.add(state)
                    queue.append((r1 + 1, c1, r2 + 1, c2, steps + 1))

            # Rotate clockwise from horizontal to vertical
            # Conditions:
            # - The snake is in horizontal position (r1 == r2)
            # - The two cells below the snake are empty
            # - The cell below r1,c1 and r1,c2 must be zero
            # After rotation, head is at (r1, c1), tail is at (r1+1, c1)
            if r1 == r2 and r1 + 1 < n and grid[r1 + 1][c1] == 0 and grid[r1 + 1][c2] == 0:
                state = (r1, c1, r1 + 1, c1)
                if state not in visited:
                    visited.add(state)
                    queue.append((r1, c1, r1 + 1, c1, steps + 1))

            # Rotate counterclockwise from vertical to horizontal
            # Conditions:
            # - The snake is in vertical position (c1 == c2)
            # - The two cells to the right of the snake are empty
            # - The cell right to r1,c1 and r2,c2 must be zero
            # After rotation, head is at (r1, c1), tail is at (r1, c1+1)
            if c1 == c2 and c1 + 1 < n and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0:
                state = (r1, c1, r1, c1 + 1)
                if state not in visited:
                    visited.add(state)
                    queue.append((r1, c1, r1, c1 + 1, steps + 1))

        return -1