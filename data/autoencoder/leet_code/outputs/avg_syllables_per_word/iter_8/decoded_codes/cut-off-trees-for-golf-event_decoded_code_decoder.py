from collections import deque

class Solution:
    def cutOffTree(self, forest):
        if not forest or not forest[0]:
            return -1

        trees = [(forest[i][j], i, j)
                 for i in range(len(forest))
                 for j in range(len(forest[0]))
                 if forest[i][j] > 1]
        trees.sort(key=lambda x: x[0])

        def bfs(start, end):
            if start == end:
                return 0

            m = len(forest)
            n = len(forest[0])
            queue = deque([start])
            visited = {start}
            steps = 0

            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and forest[nx][ny] != 0:
                            if (nx, ny) == end:
                                return steps + 1
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                steps += 1

            return -1

        x, y = 0, 0
        total_steps = 0

        for _, tx, ty in trees:
            steps = bfs((x, y), (tx, ty))
            if steps == -1:
                return -1
            total_steps += steps
            x, y = tx, ty

        return total_steps