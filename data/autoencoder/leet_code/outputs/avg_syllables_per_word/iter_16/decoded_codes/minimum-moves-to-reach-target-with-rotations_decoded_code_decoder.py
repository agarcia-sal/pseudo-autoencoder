from collections import deque

class Solution:
    def minimumMoves(self, grid):
        n = len(grid)
        queue = deque([(0, 0, 0, 1, 0)])  # tail row, tail col, head row, head col, steps
        visited = set([(0, 0, 0, 1)])

        while queue:
            r1, c1, r2, c2, steps = queue.popleft()

            if (r1, c1, r2, c2) == (n - 1, n - 2, n - 1, n - 1):
                return steps

            # Move right
            if c2 + 1 < n and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0:
                nxt = (r1, c1 + 1, r2, c2 + 1)
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((*nxt, steps + 1))

            # Move down
            if r2 + 1 < n and grid[r1 + 1][c1] == 0 and grid[r2 + 1][c2] == 0:
                nxt = (r1 + 1, c1, r2 + 1, c2)
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((*nxt, steps + 1))

            # Rotate clockwise from horizontal to vertical
            if r1 == r2 and r1 + 1 < n and grid[r1 + 1][c1] == 0 and grid[r1 + 1][c2] == 0:
                nxt = (r1, c1, r1 + 1, c1)
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((*nxt, steps + 1))

            # Rotate clockwise from vertical to horizontal
            if c1 == c2 and c1 + 1 < n and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0:
                nxt = (r1, c1, r1, c1 + 1)
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((*nxt, steps + 1))

        return -1