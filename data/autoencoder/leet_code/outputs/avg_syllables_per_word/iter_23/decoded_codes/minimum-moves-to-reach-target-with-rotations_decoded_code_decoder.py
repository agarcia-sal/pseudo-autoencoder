from collections import deque

class Solution:
    def minimumMoves(self, grid):
        n = len(grid)
        # The snake is represented by two cells: (r1, c1) and (r2, c2)
        # It always occupies two adjacent cells either horizontally or vertically.
        # Start position is top-left horizontal snake: (0,0) and (0,1)
        queue = deque([(0, 0, 0, 1, 0)])
        visited = {(0, 0, 0, 1)}

        while queue:
            r1, c1, r2, c2, steps = queue.popleft()

            # Check if snake reached bottom-right corner in horizontal position
            if r1 == n - 1 and c1 == n - 2 and r2 == n - 1 and c2 == n - 1:
                return steps

            # Move right: check if right cells are free and inside grid
            if c2 + 1 < n and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0:
                state = (r1, c1 + 1, r2, c2 + 1)
                if state not in visited:
                    visited.add(state)
                    queue.append((r1, c1 + 1, r2, c2 + 1, steps + 1))

            # Move down: check if bottom cells are free and inside grid
            if r2 + 1 < n and grid[r1 + 1][c1] == 0 and grid[r2 + 1][c2] == 0:
                state = (r1 + 1, c1, r2 + 1, c2)
                if state not in visited:
                    visited.add(state)
                    queue.append((r1 + 1, c1, r2 + 1, c2, steps + 1))

            # Rotation clockwise: from horizontal to vertical. Snake head is at (r1,c1)
            if r1 == r2 and r1 + 1 < n:
                # cells below both parts must be empty
                if grid[r1 + 1][c1] == 0 and grid[r1 + 1][c2] == 0:
                    state = (r1, c1, r1 + 1, c1)
                    if state not in visited:
                        visited.add(state)
                        queue.append((r1, c1, r1 + 1, c1, steps + 1))

            # Rotation counterclockwise: from vertical to horizontal. Snake head is at (r1,c1)
            if c1 == c2 and c1 + 1 < n:
                # cells to the right of both parts must be empty
                if grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0:
                    state = (r1, c1, r1, c1 + 1)
                    if state not in visited:
                        visited.add(state)
                        queue.append((r1, c1, r1, c1 + 1, steps + 1))

        return -1