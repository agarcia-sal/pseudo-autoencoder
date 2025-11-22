from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        d_idx = 0
        step_count = 0
        increment_counter = 0
        visited = []
        x, y = rStart, cStart

        while len(visited) < rows * cols:
            if increment_counter % 2 == 0:
                step_count += 1
            dx, dy = directions[d_idx]
            for _ in range(step_count):
                if 0 <= x < rows and 0 <= y < cols:
                    visited.append([x, y])
                x += dx
                y += dy
            d_idx = (d_idx + 1) % 4
            increment_counter += 1

        return visited