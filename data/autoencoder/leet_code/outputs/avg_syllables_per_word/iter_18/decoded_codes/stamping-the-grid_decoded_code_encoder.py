from typing import List

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0

        def prefix_sum(matrix: List[List[int]]) -> List[List[int]]:
            p = [[0] * (n + 1) for _ in range(m + 1)]
            for r in range(1, m + 1):
                for c in range(1, n + 1):
                    p[r][c] = matrix[r - 1][c - 1] + p[r - 1][c] + p[r][c - 1] - p[r - 1][c - 1]
            return p

        def submatrix_sum(p: List[List[int]], r1: int, c1: int, r2: int, c2: int) -> int:
            # using prefix sums, get sum of submatrix grid[r1..r2][c1..c2]
            return p[r2 + 1][c2 + 1] - p[r2 + 1][c1] - p[r1][c2 + 1] + p[r1][c1]

        p_grid = prefix_sum(grid)
        p_stamps = [[0] * (n) for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    if r + stampHeight <= m and c + stampWidth <= n:
                        # sum for the stamp-sized submatrix should be zero (no 1's)
                        if submatrix_sum(p_grid, r, c, r + stampHeight - 1, c + stampWidth - 1) == 0:
                            p_stamps[r][c] = 1

        p_stamps = prefix_sum(p_stamps)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    row_start = max(0, r - stampHeight + 1)
                    col_start = max(0, c - stampWidth + 1)
                    if submatrix_sum(p_stamps, row_start, col_start, r, c) == 0:
                        return False

        return True