from collections import deque
from typing import List, Tuple, Set

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m: int = len(grid)
        n: int = len(grid[0]) if m > 0 else 0

        start: Tuple[int, int] = None
        num_keys: int = 0

        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == '@':
                    start = (i, j)
                elif 'a' <= c <= 'z':
                    num_keys += 1

        if start is None:
            # No start position found, cannot proceed
            return -1

        # Bitmask for collecting keys: all keys collected when keys == (1 << num_keys) - 1
        all_keys_mask = (1 << num_keys) - 1

        # queue entries: (x, y, keys_bitmask, steps)
        queue: deque = deque()
        queue.append((start[0], start[1], 0, 0))

        # visited states: (x, y, keys_bitmask)
        visited: Set[Tuple[int, int, int]] = set()
        visited.add((start[0], start[1], 0))

        while queue:
            x, y, keys, steps = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    cell = grid[nx][ny]
                    if cell == '#':
                        continue  # wall
                    if 'A' <= cell <= 'Z':
                        # Door: check if key is collected
                        key_needed = 1 << (ord(cell.lower()) - ord('a'))
                        if (keys & key_needed) == 0:
                            continue  # key not collected yet, cannot pass door
                    if 'a' <= cell <= 'z':
                        new_keys = keys | (1 << (ord(cell) - ord('a')))
                    else:
                        new_keys = keys
                    if new_keys == all_keys_mask:
                        return steps + 1
                    state = (nx, ny, new_keys)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nx, ny, new_keys, steps + 1))
        return -1