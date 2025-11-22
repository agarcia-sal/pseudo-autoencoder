class Solution:
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        result = []
        r = c = 0
        direction = 1

        for _ in range(m * n):
            result.append(mat[r][c])
            new_r = r - 1 if direction == 1 else r + 1
            new_c = c + 1 if direction == 1 else c - 1

            if new_r < 0 or new_r == m or new_c < 0 or new_c == n:
                if direction == 1:
                    if new_c == n:
                        new_r, new_c = r + 1, c
                    else:
                        new_r, new_c = 0, c + 1
                else:
                    if new_r == m:
                        new_r, new_c = r, c + 1
                    else:
                        new_r, new_c = r + 1, 0
                direction = -direction

            r, c = new_r, new_c

        return result