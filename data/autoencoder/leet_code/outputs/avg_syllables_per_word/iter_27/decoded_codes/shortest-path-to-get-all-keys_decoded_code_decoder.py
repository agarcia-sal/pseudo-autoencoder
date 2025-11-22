from collections import deque
from typing import List, Tuple, Set

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        directions = [(0, 0), (0, -1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        start: Tuple[int, int] = (-1, -1)
        num_keys = 0

        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell == '@':
                    start = (i, j)
                elif 'a' <= cell <= 'z':
                    num_keys += 1

        if start == (-1, -1):
            return -1  # no start found

        queue: deque[Tuple[int, int, int, int]] = deque()
        visited: Set[Tuple[int, int, int]] = set()

        # The first direction is (0, 0) which means we stay in place.
        # From the pseudocode, it seems allowed to consider the current cell with no move.
        # Implement accordingly.
        queue.append((start[0], start[1], 0, 0))  # (x, y, keys, steps)
        visited.add((start[0], start[1], 0))

        all_keys_bitmask = (1 << num_keys) - 1  # bitmask representing all keys collected

        while queue:
            x, y, keys, steps = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    cell = grid[nx][ny]

                    if cell == '#':
                        continue

                    # Check if cell is a lock (uppercase letter)
                    if 'A' <= cell <= 'Z':
                        key_bit = 1 << (ord(cell.lower()) - ord('a'))
                        if (keys & key_bit) == 0:
                            continue  # Key not collected yet

                    # Update keys if cell is a key (lowercase letter)
                    if 'a' <= cell <= 'z':
                        new_keys = keys | (1 << (ord(cell) - ord('a')))
                        if new_keys == all_keys_bitmask:
                            return steps + 1
                    else:
                        new_keys = keys

                    state = (nx, ny, new_keys)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nx, ny, new_keys, steps + 1))

        return -1