from collections import deque
from math import inf

class Solution:
    def updateMatrix(self, mat):
        if not mat or not mat[0]:
            return mat

        rows = len(mat)
        cols = len(mat[0])
        dist = self.createMatrixWithInfiniteValues(rows, cols)
        queue = self.initializeEmptyQueue()

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                    self.appendPositionToQueue(queue, row, col)

        directions = self.defineDirectionOffsets()

        while queue:
            r, c = self.popLeftFromQueue(queue)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    self.appendPositionToQueue(queue, nr, nc)

        return dist

    def createMatrixWithInfiniteValues(self, rows, cols):
        # Create a matrix filled with infinity values
        return [[inf] * cols for _ in range(rows)]

    def initializeEmptyQueue(self):
        # Use deque for efficient pop from left and append operations
        return deque()

    def appendPositionToQueue(self, queue, row, col):
        queue.append((row, col))

    def defineDirectionOffsets(self):
        # Up, Down, Left, Right
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def popLeftFromQueue(self, queue):
        return queue.popleft()