from collections import deque

class Solution:
    def minimumMoves(self, grid):
        grid_size = len(grid)
        queue = deque([(0, 0, 0, 1, 0)])  # (r1, c1, r2, c2, steps)
        visited = {(0, 0, 0, 1)}

        while queue:
            r1, c1, r2, c2, steps = queue.popleft()

            if r1 == grid_size - 1 and c1 == grid_size - 2 and r2 == grid_size - 1 and c2 == grid_size - 1:
                return steps

            # Move right
            if c2 + 1 < grid_size and grid[r1][c1+1] == 0 and grid[r2][c2+1] == 0:
                state = (r1, c1+1, r2, c2+1)
                if state not in visited:
                    visited.add(state)
                    queue.append((*state, steps + 1))

            # Move down
            if r2 + 1 < grid_size and grid[r1+1][c1] == 0 and grid[r2+1][c2] == 0:
                state = (r1+1, c1, r2+1, c2)
                if state not in visited:
                    visited.add(state)
                    queue.append((*state, steps + 1))

            # Rotate clockwise (horizontal to vertical)
            if r1 == r2 and r1 + 1 < grid_size and grid[r1+1][c1] == 0 and grid[r1+1][c2] == 0:
                state = (r1, c1, r1+1, c1)
                if state not in visited:
                    visited.add(state)
                    queue.append((*state, steps + 1))

            # Rotate counterclockwise (vertical to horizontal)
            if c1 == c2 and c1 + 1 < grid_size and grid[r1][c1+1] == 0 and grid[r2][c2+1] == 0:
                state = (r1, c1, r1, c1+1)
                if state not in visited:
                    visited.add(state)
                    queue.append((*state, steps + 1))

        return -1