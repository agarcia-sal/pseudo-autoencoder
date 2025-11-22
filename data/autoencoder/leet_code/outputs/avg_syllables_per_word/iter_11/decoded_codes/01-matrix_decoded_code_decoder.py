from collections import deque
from math import inf

class Solution:
    def updateMatrix(self, mat):
        if mat is None or len(mat) == 0 or mat[0] is None:
            return mat

        rows = len(mat)
        cols = len(mat[0])
        dist = self.initializeDistanceMatrix(rows, cols)
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))

        directions = self.initializeDirections()

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    dist[nr][nc] > dist[r][c] + 1):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        return dist

    def initializeDistanceMatrix(self, rows, cols):
        return [[inf for _ in range(cols)] for _ in range(rows)]

    def initializeDirections(self):
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]