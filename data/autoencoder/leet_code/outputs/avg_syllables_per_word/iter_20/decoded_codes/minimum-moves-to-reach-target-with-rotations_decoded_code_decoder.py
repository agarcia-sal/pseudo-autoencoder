from collections import deque
from typing import List

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # States are represented by tail and head coordinates: (r1, c1, r2, c2)
        # The snake always occupies two adjacent cells either horizontally or vertically
        # Start state: tail at (0,0), head at (0,1), steps=0
        queue = deque([(0, 0, 0, 1, 0)])
        visited = {(0, 0, 0, 1)}

        while queue:
            r1, c1, r2, c2, steps = queue.popleft()

            # Check if reached the target position:
            # tail at (n-1, n-2) and head at (n-1, n-1)
            if r1 == n - 1 and c1 == n - 2 and r2 == n - 1 and c2 == n - 1:
                return steps

            # Move right: if tail and head can both move right
            if c2 + 1 < n and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0:
                state = (r1, c1 + 1, r2, c2 + 1)
                if state not in visited:
                    visited.add(state)
                    queue.append((r1, c1 + 1, r2, c2 + 1, steps + 1))

            # Move down: if tail and head can both move down
            if r2 + 1 < n and grid[r1 + 1][c1] == 0 and grid[r2 + 1][c2] == 0:
                state = (r1 + 1, c1, r2 + 1, c2)
                if state not in visited:
                    visited.add(state)
                    queue.append((r1 + 1, c1, r2 + 1, c2, steps + 1))

            # Rotate clockwise: if snake is horizontal and can rotate downwards
            if r1 == r2 and r1 + 1 < n and grid[r1 + 1][c1] == 0 and grid[r1 + 1][c2] == 0:
                state = (r1, c1, r1 + 1, c1)
                if state not in visited:
                    visited.add(state)
                    queue.append((r1, c1, r1 + 1, c1, steps + 1))

            # Rotate counterclockwise: if snake is vertical and can rotate rightwards
            if c1 == c2 and c1 + 1 < n and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0:
                state = (r1, c1, r1, c1 + 1)
                if state not in visited:
                    visited.add(state)
                    queue.append((r1, c1, r1, c1 + 1, steps + 1))

        return -1