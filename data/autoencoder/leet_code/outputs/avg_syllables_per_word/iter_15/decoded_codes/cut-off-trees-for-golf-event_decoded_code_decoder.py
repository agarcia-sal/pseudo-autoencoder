from collections import deque
from typing import List, Tuple

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1

        m, n = len(forest), len(forest[0])

        trees = sorted(
            (forest[i][j], i, j)
            for i in range(m)
            for j in range(n)
            if forest[i][j] > 1
        )

        def bfs(start: Tuple[int, int], end: Tuple[int, int]) -> int:
            if start == end:
                return 0
            queue = deque([start])
            visited = {start}
            steps = 0
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x + dx, y + dy
                        if (
                            0 <= nx < m and 0 <= ny < n and
                            (nx, ny) not in visited and
                            forest[nx][ny] != 0
                        ):
                            if (nx, ny) == end:
                                return steps + 1
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                steps += 1
            return -1

        x = y = total_steps = 0
        for _, tx, ty in trees:
            steps = bfs((x, y), (tx, ty))
            if steps == -1:
                return -1
            total_steps += steps
            x, y = tx, ty

        return total_steps