from typing import List

class Solution:
    def spiralMatrixIII(self, rrows: int, ccols: int, rrStart: int, ccStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0
        steps = 0
        increment = 0
        visited = []
        x, y = rrStart, ccStart

        while len(visited) < rrows * ccols:
            if increment % 2 == 0:
                steps += 1
            for _ in range(steps):
                if 0 <= x < rrows and 0 <= y < ccols:
                    visited.append([x, y])
                dx, dy = directions[direction_index]
                x += dx
                y += dy
            direction_index = (direction_index + 1) % 4
            increment += 1

        return visited