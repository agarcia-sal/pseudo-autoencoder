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
                cell = grid[i][j]
                if cell == '@':
                    start = (i, j)
                elif 'a' <= cell <= 'z':
                    num_keys += 1

        if start is None:
            return -1  # No start found

        # All keys bitmask: (1 << num_keys) - 1
        all_keys_bitmask = (1 << num_keys) - 1

        queue: deque = deque([(start[0], start[1], 0, 0)])  # x, y, keys_bitmask, steps
        visited: Set[Tuple[int, int, int]] = set([(start[0], start[1], 0)])

        while queue:
            x, y, keys, steps = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    cell = grid[nx][ny]

                    if cell == '#':
                        continue

                    # If cell is uppercase letter (lock)
                    if 'A' <= cell <= 'Z':
                        key_needed = 1 << (ord(cell.lower()) - ord('a'))
                        if (keys & key_needed) == 0:
                            continue

                    # If cell is lowercase letter (key)
                    if 'a' <= cell <= 'z':
                        key_bit = 1 << (ord(cell) - ord('a'))
                        new_keys = keys | key_bit
                        if new_keys == all_keys_bitmask:
                            return steps + 1
                    else:
                        new_keys = keys

                    state = (nx, ny, new_keys)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nx, ny, new_keys, steps + 1))

        return -1