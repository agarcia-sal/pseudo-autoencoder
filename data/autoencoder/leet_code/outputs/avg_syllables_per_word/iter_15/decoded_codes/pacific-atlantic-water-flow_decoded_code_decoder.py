from collections import deque
from typing import List, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        def bfs(queue: deque, visited: set):
            directions: List[Tuple[int, int]] = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            while queue:
                i, j = queue.popleft()
                for a, b in directions:
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited and heights[x][y] >= heights[i][j]:
                        visited.add((x, y))
                        queue.append((x, y))

        visited_pacific = set()
        visited_atlantic = set()
        queue_pacific = deque()
        queue_atlantic = deque()

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    visited_pacific.add((i, j))
                    queue_pacific.append((i, j))
                if i == m - 1 or j == n - 1:
                    visited_atlantic.add((i, j))
                    queue_atlantic.append((i, j))

        bfs(queue_pacific, visited_pacific)
        bfs(queue_atlantic, visited_atlantic)

        result = []
        for i in range(m):
            for j in range(n):
                if (i, j) in visited_pacific and (i, j) in visited_atlantic:
                    result.append([i, j])

        return result