from typing import List


class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0]) if grid else 0

        def prefix_sum(matrix: List[List[int]]) -> List[List[int]]:
            p = [[0] * (n + 1) for _ in range(m + 1)]
            for r in range(1, m + 1):
                row_mat = matrix[r - 1]
                row_p = p[r]
                prev_row_p = p[r - 1]
                for c in range(1, n + 1):
                    row_p[c] = (
                        row_mat[c - 1]
                        + prev_row_p[c]
                        + row_p[c - 1]
                        - p[r - 1][c - 1]
                    )
            return p

        def submatrix_sum(p: List[List[int]], r1: int, c1: int, r2: int, c2: int) -> int:
            # All indexes r1, c1, r2, c2 are zero-based inclusive
            # p uses 1-based indexing internally
            return (
                p[r2 + 1][c2 + 1]
                - p[r2 + 1][c1]
                - p[r1][c2 + 1]
                + p[r1][c1]
            )

        if m == 0 or n == 0:
            # No cells, trivially True
            return True

        p_grid = prefix_sum(grid)

        p_stamps = [[0] * (n + 1) for _ in range(m + 1)]

        # Mark positions where stamp can be placed
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    bottom_r = r + stampHeight
                    bottom_c = c + stampWidth
                    if bottom_r <= m and bottom_c <= n:
                        if submatrix_sum(p_grid, r, c, bottom_r - 1, bottom_c - 1) == 0:
                            p_stamps[r][c] = 1

        p_stamps = prefix_sum(p_stamps)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    r1 = max(0, r - stampHeight + 1)
                    c1 = max(0, c - stampWidth + 1)
                    if submatrix_sum(p_stamps, r1, c1, r, c) == 0:
                        return False

        return True