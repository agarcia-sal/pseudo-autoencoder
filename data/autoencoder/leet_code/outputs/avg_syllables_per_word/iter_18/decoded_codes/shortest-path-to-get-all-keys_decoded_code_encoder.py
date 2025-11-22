from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
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
                    num_keys += 1

        # Bitmask representing all keys collected: (1 << num_keys) - 1
        all_keys_mask = (1 << num_keys) - 1
        queue = deque([(start[0], start[1], 0, 0)])  # x, y, keys bitmask, steps
        visited = {(start[0], start[1], 0)}

        while queue:
            x, y, keys, steps = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    cell = grid[nx][ny]
                    if cell == '#':
                        continue
                    # If uppercase letter, check if key is collected
                    if 'A' <= cell <= 'Z':
                        key_needed = 1 << (ord(cell.lower()) - ord('a'))
                        if (keys & key_needed) == 0:
                            continue
                    # If lowercase letter, collect key
                    if 'a' <= cell <= 'z':
                        new_keys = keys | (1 << (ord(cell) - ord('a')))
                        if new_keys == all_keys_mask:
                            return steps + 1
                    else:
                        new_keys = keys
                    if (nx, ny, new_keys) not in visited:
                        visited.add((nx, ny, new_keys))
                        queue.append((nx, ny, new_keys, steps + 1))

        return -1