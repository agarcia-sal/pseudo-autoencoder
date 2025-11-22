from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid):
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        m, n = len(grid), len(grid[0])
        start = None
        num_keys = 0

        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == '@':
                    start = (i, j)
                elif 'a' <= c <= 'z':
                    num_keys += 1

        queue = deque([(start[0], start[1], 0, 0)])
        visited = {(start[0], start[1], 0)}
        target = (1 << num_keys) - 1

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
                        if keys & key_needed == 0:
                            continue
                    if 'a' <= cell <= 'z':
                        new_keys = keys | (1 << (ord(cell) - ord('a')))
                        if new_keys == target:
                            return steps + 1
                    else:
                        new_keys = keys
                    state = (nx, ny, new_keys)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nx, ny, new_keys, steps + 1))
        return -1