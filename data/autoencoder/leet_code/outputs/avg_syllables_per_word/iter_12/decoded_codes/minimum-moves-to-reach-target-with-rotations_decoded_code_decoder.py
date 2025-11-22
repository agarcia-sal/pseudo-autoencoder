from collections import deque

class Solution:
    def minimumMoves(self, grid):
        n = len(grid)
        queue = deque([(0, 0, 0, 1, 0)])  # r1, c1, r2, c2, steps
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

            # Rotate clockwise (horizontal to vertical)
            if r1 == r2 and r1 + 1 < n and grid[r1 + 1][c1] == 0 and grid[r1 + 1][c2] == 0:
                state = (r1, c1, r1 + 1, c1)
                if state not in visited:
                    visited.add(state)
                    queue.append((r1, c1, r1 + 1, c1, steps + 1))

            # Rotate counter-clockwise (vertical to horizontal)
            if c1 == c2 and c1 + 1 < n and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0:
                state = (r1, c1, r1, c1 + 1)
                if state not in visited:
                    visited.add(state)
                    queue.append((r1, c1, r1, c1 + 1, steps + 1))

        return -1