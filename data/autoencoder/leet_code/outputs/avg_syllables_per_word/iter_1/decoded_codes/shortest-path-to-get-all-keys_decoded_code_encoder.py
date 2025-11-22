from collections import deque

def shortest_path_all_keys(grid):
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    m, n = len(grid), len(grid[0])
    start = None
    num_keys = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)
            elif grid[i][j].islower():
                num_keys += 1

    queue = deque([(start[0], start[1], 0, 0)])
    visited = {(start[0], start[1], 0)}

    while queue:
        x, y, keys, steps = queue.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                c = grid[nx][ny]
                if c == '#':
                    continue
                if c.isupper():
                    mask = 1 << (ord(c.lower()) - ord('a'))
                    if (keys & mask) == 0:
                        continue
                new_keys = keys
                if c.islower():
                    new_keys = keys | (1 << (ord(c) - ord('a')))
                    if new_keys == (1 << num_keys) - 1:
                        return steps + 1
                if (nx, ny, new_keys) not in visited:
                    visited.add((nx, ny, new_keys))
                    queue.append((nx, ny, new_keys, steps + 1))

    return -1