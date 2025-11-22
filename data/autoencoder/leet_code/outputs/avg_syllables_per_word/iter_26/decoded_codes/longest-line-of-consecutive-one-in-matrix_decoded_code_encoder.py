from typing import List

class Solution:
    def longestLine(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        max_length = 0

        def check(x: int, y: int, delta_x: int, delta_y: int) -> int:
            length = 0
            while 0 <= x < m and 0 <= y < n and matrix[x][y] == 1:
                length += 1
                x += delta_x
                y += delta_y
            return length

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    for delta_x, delta_y in directions:
                        prev_x, prev_y = i - delta_x, j - delta_y
                        if prev_x < 0 or prev_y < 0 or prev_y >= n or matrix[prev_x][prev_y] == 0:
                            length = check(i, j, delta_x, delta_y)
                            if length > max_length:
                                max_length = length

        return max_length