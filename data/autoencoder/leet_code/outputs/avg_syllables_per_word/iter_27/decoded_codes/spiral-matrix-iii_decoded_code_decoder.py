from typing import List

class Solution:
    def spiralMatrixIII(
        self,
        rRows: int,
        rCols: int,
        rStart: int,
        cStart: int
    ) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # East, South, West, North
        direction_index = 0
        steps = 0
        increment = 0
        visited = []
        x, y = rStart, cStart

        while len(visited) < rRows * rCols:
            if increment % 2 == 0:
                steps += 1
            dx, dy = directions[direction_index]
            for _ in range(steps):
                if 0 <= x < rRows and 0 <= y < rCols:
                    visited.append([x, y])
                    if len(visited) == rRows * rCols:
                        break
                x += dx
                y += dy
            direction_index = (direction_index + 1) % 4
            increment += 1

        return visited