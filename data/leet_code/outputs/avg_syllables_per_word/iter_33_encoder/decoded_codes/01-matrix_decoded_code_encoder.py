from collections import deque
from math import inf

class Solution:
    def updateMatrix(self, mat):
        if not mat or not mat[0]:
            return mat
        rows = len(mat)
        cols = len(mat[0])
        dist = [[inf] * cols for _ in range(rows)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()
            current_dist = dist[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] > current_dist + 1:
                    dist[nr][nc] = current_dist + 1
                    queue.append((nr, nc))
        return dist