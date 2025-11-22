from collections import deque
from typing import List, Tuple

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1

        trees = self.getAllTrees(forest)
        self.sortTrees(trees)

        def bfs(start: Tuple[int, int], end: Tuple[int, int]) -> int:
            if start == end:
                return 0

            m, n = len(forest), len(forest[0])
            queue = self.initializeQueue(start)
            visited = self.initializeVisitedSet(start)
            steps = 0
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                currentLevelSize = len(queue)
                for _ in range(currentLevelSize):
                    x, y = queue.popleft()

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and forest[nx][ny] != 0:
                            if (nx, ny) == end:
                                return steps + 1
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                steps += 1

            return -1

        x = y = total_steps = 0
        for height, tx, ty in trees:
            steps = bfs((x, y), (tx, ty))
            if steps == -1:
                return -1
            total_steps += steps
            x, y = tx, ty

        return total_steps

    def getAllTrees(self, forest: List[List[int]]) -> List[Tuple[int, int, int]]:
        result = []
        rows = len(forest)
        columns = len(forest[0])
        for i in range(rows):
            for j in range(columns):
                height = forest[i][j]
                if height > 1:
                    result.append((height, i, j))
        return result

    def sortTrees(self, trees: List[Tuple[int, int, int]]):
        trees.sort(key=lambda x: x[0])

    def initializeQueue(self, start: Tuple[int, int]) -> deque:
        queue = deque()
        queue.append(start)
        return queue

    def initializeVisitedSet(self, start: Tuple[int, int]) -> set:
        visited = set()
        visited.add(start)
        return visited