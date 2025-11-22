from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        m = len(grid)
        n = len(grid[0])
        start = None
        num_keys = 0

        # Identify start position and count keys
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == '@':
                    start = (i,j)
                elif 'a' <= c <= 'z':
                    num_keys += 1

        all_keys_mask = (1 << num_keys) - 1
        queue = deque()
        visited = set()

        # Keys bitmask initially 0, steps 0
        queue.append((start[0], start[1], 0, 0))
        visited.add((start[0], start[1], 0))

        while queue:
            x, y, keys, steps = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    cell = grid[nx][ny]
                    if cell == '#':
                        continue
                    if 'A' <= cell <= 'Z':
                        key_needed = 1 << (ord(cell.lower()) - ord('a'))
                        if (keys & key_needed) == 0:
                            continue
                    new_keys = keys
                    if 'a' <= cell <= 'z':
                        new_keys |= (1 << (ord(cell) - ord('a')))
                        if new_keys == all_keys_mask:
                            return steps + 1
                    if (nx, ny, new_keys) not in visited:
                        visited.add((nx, ny, new_keys))
                        queue.append((nx, ny, new_keys, steps + 1))

        return -1