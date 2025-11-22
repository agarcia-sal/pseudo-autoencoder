from collections import deque
from math import inf

class Solution:
    def updateMatrix(self, mat):
        if mat is None or len(mat) == 0 or mat[0] is None:
            return mat

        rows = len(mat)
        cols = len(mat[0])
        dist = self.createMatrixInfinity(rows, cols)
        queue = self.createEmptyQueue()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    self.appendToQueue(queue, (r, c))

        directions = self.createDirectionList()

        while queue:
            r, c = self.popFromQueue(queue)
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    self.appendToQueue(queue, (nr, nc))

        return dist

    def createMatrixInfinity(self, rows, cols):
        return [[inf] * cols for _ in range(rows)]

    def createEmptyQueue(self):
        return deque()

    def appendToQueue(self, queue, element):
        queue.append(element)

    def popFromQueue(self, queue):
        return queue.popleft()

    def createDirectionList(self):
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]