from collections import deque
from typing import List, Tuple, Set

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue: deque[Tuple[int, int, int, int, int]] = deque()
        visited: Set[Tuple[int, int, int, int]] = set()

        # Initial position: snake occupies (0,0) and (0,1), steps = 0
        queue.append((0, 0, 0, 1, 0))
        visited.add((0, 0, 0, 1))

        while queue:
            r1, c1, r2, c2, steps = queue.popleft()

            if (r1, c1, r2, c2) == (n - 1, n - 2, n - 1, n - 1):
                return steps

            # Move Right
            if (
                c2 + 1 < n
                and grid[r1][c1 + 1] == 0
                and grid[r2][c2 + 1] == 0
                and (r1, c1 + 1, r2, c2 + 1) not in visited
            ):
                visited.add((r1, c1 + 1, r2, c2 + 1))
                queue.append((r1, c1 + 1, r2, c2 + 1, steps + 1))

            # Move Down
            if (
                r2 + 1 < n
                and grid[r1 + 1][c1] == 0
                and grid[r2 + 1][c2] == 0
                and (r1 + 1, c1, r2 + 1, c2) not in visited
            ):
                visited.add((r1 + 1, c1, r2 + 1, c2))
                queue.append((r1 + 1, c1, r2 + 1, c2, steps + 1))

            # Rotate clockwise (horizontal to vertical)
            if (
                r1 == r2
                and r1 + 1 < n
                and grid[r1 + 1][c1] == 0
                and grid[r1 + 1][c2] == 0
                and (r1, c1, r1 + 1, c1) not in visited
            ):
                visited.add((r1, c1, r1 + 1, c1))
                queue.append((r1, c1, r1 + 1, c1, steps + 1))

            # Rotate counterclockwise (vertical to horizontal)
            if (
                c1 == c2
                and c1 + 1 < n
                and grid[r1][c1 + 1] == 0
                and grid[r2][c2 + 1] == 0
                and (r1, c1, r1, c1 + 1) not in visited
            ):
                visited.add((r1, c1, r1, c1 + 1))
                queue.append((r1, c1, r1, c1 + 1, steps + 1))

        return -1