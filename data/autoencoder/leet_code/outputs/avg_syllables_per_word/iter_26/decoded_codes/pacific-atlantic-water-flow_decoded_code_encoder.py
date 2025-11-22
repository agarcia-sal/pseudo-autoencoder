from collections import deque
from typing import List, Set, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(queue: deque, visited_set: Set[Tuple[int, int]]) -> None:
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for a, b in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                        x, y = i + a, j + b
                        if 0 <= x < m and 0 <= y < n and (x, y) not in visited_set and heights[x][y] >= heights[i][j]:
                            visited_set.add((x, y))
                            queue.append((x, y))

        m, n = len(heights), len(heights[0]) if heights else 0
        if m == 0 or n == 0:
            return []

        visited_set_one = set()
        visited_set_two = set()
        queue_one = deque()
        queue_two = deque()

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    visited_set_one.add((i, j))
                    queue_one.append((i, j))
                if i == m - 1 or j == n - 1:
                    visited_set_two.add((i, j))
                    queue_two.append((i, j))

        bfs(queue_one, visited_set_one)
        bfs(queue_two, visited_set_two)

        return [[i, j] for i in range(m) for j in range(n)
                if (i, j) in visited_set_one and (i, j) in visited_set_two]