from typing import List

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m = len(grid)
        if m == 0:
            return True  # Empty grid trivially stamps
        n = len(grid[0])
        if n == 0:
            return True

        def prefix_sum(matrix: List[List[int]]) -> List[List[int]]:
            p = [[0] * (n + 1) for _ in range(m + 1)]
            for r in range(1, m + 1):
                row_sum = 0
                for c in range(1, n + 1):
                    row_sum += matrix[r - 1][c - 1]
                    p[r][c] = p[r - 1][c] + row_sum
            return p

        def submatrix_sum(p: List[List[int]], r1: int, c1: int, r2: int, c2: int) -> int:
            # Sum of submatrix from (r1, c1) to (r2, c2) inclusive using prefix sums
            return p[r2 + 1][c2 + 1] - p[r2 + 1][c1] - p[r1][c2 + 1] + p[r1][c1]

        p_grid = prefix_sum(grid)

        p_stamps = [[0]*(n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    if r + stampHeight <= m and c + stampWidth <= n:
                        total = submatrix_sum(p_grid, r, c, r + stampHeight - 1, c + stampWidth - 1)
                        if total == 0:
                            p_stamps[r][c] = 1

        p_stamps = prefix_sum(p_stamps)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    r1 = max(0, r - stampHeight + 1)
                    c1 = max(0, c - stampWidth + 1)
                    total = submatrix_sum(p_stamps, r1, c1, r, c)
                    if total == 0:
                        return False
        return True