from typing import List, Optional

class Solution:
    def findDiagonalOrder(self, mat: Optional[List[List[int]]]) -> List[int]:
        if mat is None or len(mat) == 0 or mat[0] is None or len(mat[0]) == 0:
            return []

        m = len(mat)
        n = len(mat[0])
        result = []
        r = 0
        c = 0
        direction = 1  # 1 means moving up-right, -1 means moving down-left

        for _ in range(m * n):
            result.append(mat[r][c])
            if direction == 1:
                new_r = r - 1
                new_c = c + 1
            else:
                new_r = r + 1
                new_c = c - 1

            if new_r < 0 or new_r == m or new_c < 0 or new_c == n:
                if direction == 1:
                    if new_c == n:
                        new_r = r + 1
                        new_c = c
                    else:
                        new_r = 0
                        new_c = c + 1
                else:
                    if new_r == m:
                        new_r = r
                        new_c = c + 1
                    else:
                        new_r = r + 1
                        new_c = 0
                direction *= -1
            r, c = new_r, new_c

        return result