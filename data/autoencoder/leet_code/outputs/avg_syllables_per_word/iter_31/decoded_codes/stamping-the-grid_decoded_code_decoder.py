from typing import List


class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0

        def prefix_sum(matrix: List[List[int]]) -> List[List[int]]:
            p = [[0] * (n + 1) for _ in range(m + 1)]
            for r in range(1, m + 1):
                row_mat = matrix[r - 1]
                row_p = p[r]
                row_p_prev = p[r - 1]
                for c in range(1, n + 1):
                    # prefix sum calculation
                    row_p[c] = row_mat[c - 1] + row_p[c - 1] + row_p_prev[c] - row_p_prev[c - 1]
            return p

        def submatrix_sum(p: List[List[int]], r1: int, c1: int, r2: int, c2: int) -> int:
            # Adjust indices by +1 for prefix sums indexing
            return p[r2 + 1][c2 + 1] - p[r2 + 1][c1] - p[r1][c2 + 1] + p[r1][c1]

        p_grid = prefix_sum(grid)

        # p_stamps[r][c] == 1 means a stamp can start at (r,c)
        p_stamps = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    if r + stampHeight <= m and c + stampWidth <= n:
                        # check if submatrix of grid covered by stamp is all zeros
                        if submatrix_sum(p_grid, r, c, r + stampHeight - 1, c + stampWidth - 1) == 0:
                            p_stamps[r][c] = 1

        p_stamps_sum = prefix_sum(p_stamps)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    r1 = max(0, r - stampHeight + 1)
                    c1 = max(0, c - stampWidth + 1)
                    # check if at least one stamp covers (r,c)
                    if submatrix_sum(p_stamps_sum, r1, c1, r, c) == 0:
                        return False
        return True