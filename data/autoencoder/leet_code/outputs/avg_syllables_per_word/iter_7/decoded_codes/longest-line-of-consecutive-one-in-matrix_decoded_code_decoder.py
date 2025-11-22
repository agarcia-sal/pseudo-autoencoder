from typing import List, Tuple

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        m, n = len(mat), len(mat[0])
        directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (1, 1), (1, -1)]
        max_length = 0

        def check(x: int, y: int, dx: int, dy: int) -> int:
            length = 0
            while 0 <= x < m and 0 <= y < n and mat[x][y] == 1:
                length += 1
                x += dx
                y += dy
            return length

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    for dx, dy in directions:
                        prev_x, prev_y = i - dx, j - dy
                        if prev_x < 0 or prev_y < 0 or prev_y >= n or (0 <= prev_x < m and mat[prev_x][prev_y] == 0):
                            max_length = max(max_length, check(i, j, dx, dy))
        return max_length