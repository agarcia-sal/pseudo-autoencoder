from collections import defaultdict, deque
from math import inf

class Solution:
    def isPrintable(self, targetGrid):
        colorBounds = defaultdict(lambda: [inf, inf, -inf, -inf])
        for rowIndex in range(len(targetGrid)):
            for columnIndex in range(len(targetGrid[0])):
                color = targetGrid[rowIndex][columnIndex]
                bounds = colorBounds[color]
                bounds[0] = min(bounds[0], rowIndex)       # minimal row
                bounds[1] = min(bounds[1], columnIndex)    # minimal column
                bounds[2] = max(bounds[2], rowIndex)       # maximal row
                bounds[3] = max(bounds[3], columnIndex)    # maximal column

        graph = defaultdict(list)
        inDegree = defaultdict(int)

        for color, (min_r, min_c, max_r, max_c) in colorBounds.items():
            for r in range(min_r, max_r + 1):
                for c in range(min_c, max_c + 1):
                    if targetGrid[r][c] != color:
                        otherColor = targetGrid[r][c]
                        graph[otherColor].append(color)
                        inDegree[color] += 1

        queue = deque([color for color in colorBounds if inDegree[color] == 0])
        visitedColors = 0

        while queue:
            color = queue.popleft()
            visitedColors += 1
            for nextColor in graph[color]:
                inDegree[nextColor] -= 1
                if inDegree[nextColor] == 0:
                    queue.append(nextColor)

        return visitedColors == len(colorBounds)