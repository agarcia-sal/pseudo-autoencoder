class Solution:
    def longestLine(self, mat):
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        max_length = 0

        def check(x, y, dx, dy):
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
                        if not (0 <= prev_x < m and 0 <= prev_y < n and mat[prev_x][prev_y] == 1):
                            max_length = max(max_length, check(i, j, dx, dy))
        return max_length