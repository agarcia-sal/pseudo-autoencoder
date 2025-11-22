from collections import deque
from typing import List, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        def bfs(queue: deque, visited: set):
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for a, b in directions:
                        x, y = i + a, j + b
                        if (0 <= x < m and 0 <= y < n and 
                            (x, y) not in visited and 
                            heights[x][y] >= heights[i][j]):
                            visited.add((x, y))
                            queue.append((x, y))

        visited_one = set()
        visited_two = set()
        queue_one = deque()
        queue_two = deque()

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    visited_one.add((i, j))
                    queue_one.append((i, j))
                if i == m - 1 or j == n - 1:
                    visited_two.add((i, j))
                    queue_two.append((i, j))

        bfs(queue_one, visited_one)
        bfs(queue_two, visited_two)

        result = []
        for i in range(m):
            for j in range(n):
                if (i, j) in visited_one and (i, j) in visited_two:
                    result.append([i, j])

        return result