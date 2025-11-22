from collections import deque

def cutOffTree(forest):
    trees = [(h, i, j) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1]
    trees.sort(key=lambda x: x[0])

    def bfs(start, end):
        if start == end:
            return 0
        m, n = len(forest), len(forest[0])
        queue = deque([start])
        visited = {start}
        steps = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and forest[nx][ny] != 0 and (nx, ny) not in visited:
                        if (nx, ny) == end:
                            return steps + 1
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            steps += 1
        return -1

    pos = (0, 0)
    total = 0
    for _, tx, ty in trees:
        steps = bfs(pos, (tx, ty))
        if steps == -1:
            return -1
        total += steps
        pos = (tx, ty)

    return total