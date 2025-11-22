from collections import deque
from typing import List, Set, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        if m == 0:
            return []
        n = len(heights[0])
        if n == 0:
            return []

        def bfs(queue: deque[Tuple[int, int]], visited: Set[Tuple[int, int]]) -> None:
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            while queue:
                length = len(queue)
                for _ in range(length):
                    i, j = queue.popleft()
                    for a, b in directions:
                        x, y = i + a, j + b
                        if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                            if heights[x][y] >= heights[i][j]:
                                visited.add((x, y))
                                queue.append((x, y))

        vis1: Set[Tuple[int, int]] = set()
        vis2: Set[Tuple[int, int]] = set()
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

        result_list = []
        for i in range(m):
            for j in range(n):
                if (i, j) in vis1 and (i, j) in vis2:
                    result_list.append([i, j])

        return result_list