from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        def bfs(queue, visited):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for a, b in directions:
                        x, y = i + a, j + b
                        if 0 <= x < m and 0 <= y < n and (x, y) not in visited and heights[x][y] >= heights[i][j]:
                            visited.add((x, y))
                            queue.append((x, y))

        pacific_visited = set()
        atlantic_visited = set()
        pacific_queue = deque()
        atlantic_queue = deque()

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pacific_visited.add((i, j))
                    pacific_queue.append((i, j))
                if i == m - 1 or j == n - 1:
                    atlantic_visited.add((i, j))
                    atlantic_queue.append((i, j))

        bfs(pacific_queue, pacific_visited)
        bfs(atlantic_queue, atlantic_visited)

        result = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific_visited and (i, j) in atlantic_visited:
                    result.append([i, j])

        return result