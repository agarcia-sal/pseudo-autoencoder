class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # east, south, west, north
        direction_index = 0
        steps = 0
        increment = 0
        visited = []
        x, y = rStart, cStart

        while len(visited) < rows * cols:
            if increment % 2 == 0:
                steps += 1
            dx, dy = directions[direction_index]
            for _ in range(steps):
                if 0 <= x < rows and 0 <= y < cols:
                    visited.append([x, y])
                x += dx
                y += dy
            direction_index = (direction_index + 1) % 4
            increment += 1

        return visited