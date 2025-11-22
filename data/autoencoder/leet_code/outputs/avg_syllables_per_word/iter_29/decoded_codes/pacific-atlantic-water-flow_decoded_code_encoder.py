from collections import deque
from typing import List, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(queue: deque[Tuple[int, int]], visited: set[Tuple[int, int]]) -> None:
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for a, b in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                        x, y = i + a, j + b
                        if 0 <= x < m and 0 <= y < n and (x, y) not in visited and heights[x][y] >= heights[i][j]:
                            visited.add((x, y))
                            queue.append((x, y))

        m, n = len(heights), len(heights[0]) if heights else 0
        if m == 0 or n == 0:
            return []

        vis1 = set()
        vis2 = set()
        q1 = deque()
        q2 = deque()

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    vis1.add((i, j))
                    q1.append((i, j))
                if i == m - 1 or j == n - 1:
                    vis2.add((i, j))
                    q2.append((i, j))

        bfs(q1, vis1)
        bfs(q2, vis2)

        result = []
        for i in range(m):
            for j in range(n):
                if (i, j) in vis1 and (i, j) in vis2:
                    result.append([i, j])

        return result