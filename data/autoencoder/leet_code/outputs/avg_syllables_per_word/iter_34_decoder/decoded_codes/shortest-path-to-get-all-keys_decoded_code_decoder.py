from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        start = None
        num_keys = 0

        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell == '@':
                    start = (i, j)
                elif 'a' <= cell <= 'z':
                    # Count unique keys
                    num_keys += 1

        # BFS queue: (x, y, keys_bitmask, steps)
        queue = deque([(start[0], start[1], 0, 0)])
        visited = set([(start[0], start[1], 0)])

        all_keys_mask = (1 << num_keys) - 1

        while queue:
            x, y, keys, steps = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    cell = grid[nx][ny]
                    if cell == '#':
                        continue

                    new_keys = keys
                    if 'A' <= cell <= 'Z':
                        required_key_bit = 1 << (ord(cell.lower()) - ord('a'))
                        if (keys & required_key_bit) == 0:
                            continue

                    if 'a' <= cell <= 'z':
                        new_keys = keys | (1 << (ord(cell) - ord('a')))
                        if new_keys == all_keys_mask:
                            return steps + 1

                    if (nx, ny, new_keys) not in visited:
                        visited.add((nx, ny, new_keys))
                        queue.append((nx, ny, new_keys, steps + 1))

        return -1