from collections import deque
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        start = None
        num_keys = 0

        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell == '@':
                    start = (i, j)
                elif 'a' <= cell <= 'z':
                    # Count total number of keys
                    num_keys = max(num_keys, ord(cell) - ord('a') + 1)

        # If start is not found, no valid path
        if start is None:
            return -1

        # Bitmask representation: keys are 0..num_keys-1 bits.
        # Target is all keys collected: (1 << num_keys) - 1
        target_keys_mask = (1 << num_keys) - 1

        queue = deque()
        # Store: (x, y, collected_keys, steps)
        queue.append((start[0], start[1], 0, 0))
        visited = set()
        visited.add((start[0], start[1], 0))

        while queue:
            x, y, keys, steps = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    cell = grid[nx][ny]
                    if cell == '#':  # wall
                        continue

                    # If cell is uppercase, check if corresponding key is collected
                    if 'A' <= cell <= 'Z':
                        key_needed = 1 << (ord(cell.lower()) - ord('a'))
                        if (keys & key_needed) == 0:
                            continue

                    # If cell is lowercase, pick up the key
                    if 'a' <= cell <= 'z':
                        new_keys = keys | (1 << (ord(cell) - ord('a')))
                        if new_keys == target_keys_mask:
                            return steps + 1
                    else:
                        new_keys = keys

                    state = (nx, ny, new_keys)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nx, ny, new_keys, steps + 1))

        return -1