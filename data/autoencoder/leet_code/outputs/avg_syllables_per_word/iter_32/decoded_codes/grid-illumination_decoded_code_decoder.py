from collections import defaultdict
from typing import List, Tuple


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row_count = defaultdict(int)
        col_count = defaultdict(int)
        diag_count = defaultdict(int)       # key: row - col
        anti_diag_count = defaultdict(int)  # key: row + col

        lamp_positions = set()

        for r, c in lamps:
            if (r, c) not in lamp_positions:
                lamp_positions.add((r, c))
                row_count[r] += 1
                col_count[c] += 1
                diag_count[r - c] += 1
                anti_diag_count[r + c] += 1

        # directions: 8 adjacent + the cell itself
        directions = [
            (0, 0),
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]

        result = []

        for r, c in queries:
            if (row_count[r] > 0 or
                col_count[c] > 0 or
                diag_count[r - c] > 0 or
                anti_diag_count[r + c] > 0):
                result.append(1)
            else:
                result.append(0)

            # Turn off lamps in the query cell and adjacent cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in lamp_positions:
                    lamp_positions.remove((nr, nc))
                    row_count[nr] -= 1
                    if row_count[nr] == 0:
                        del row_count[nr]
                    col_count[nc] -= 1
                    if col_count[nc] == 0:
                        del col_count[nc]
                    diag_key = nr - nc
                    diag_count[diag_key] -= 1
                    if diag_count[diag_key] == 0:
                        del diag_count[diag_key]
                    anti_diag_key = nr + nc
                    anti_diag_count[anti_diag_key] -= 1
                    if anti_diag_count[anti_diag_key] == 0:
                        del anti_diag_count[anti_diag_key]

        return result