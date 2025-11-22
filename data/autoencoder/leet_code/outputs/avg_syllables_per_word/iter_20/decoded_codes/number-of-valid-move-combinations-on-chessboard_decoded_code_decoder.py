from typing import List, Tuple
from itertools import product


class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        directions = {
            "rook": [(1, 0), (-1, 0), (0, 1), (0, -1)],
            "queen": [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)],
            "bishop": [(1, 1), (1, -1), (-1, 1), (-1, -1)],
        }

        # Convert positions to zero-based indexing
        positions_zero_based = [(r - 1, c - 1) for r, c in positions]

        def get_destinations(start: Tuple[int, int], piece_type: str) -> List[Tuple[int, int]]:
            row, col = start
            dests = [start]
            for dr, dc in directions[piece_type]:
                new_r, new_c = row + dr, col + dc
                while 0 <= new_r < 8 and 0 <= new_c < 8:
                    dests.append((new_r, new_c))
                    new_r += dr
                    new_c += dc
            return dests

        all_destinations = [
            get_destinations(pos, piece) for pos, piece in zip(positions_zero_based, pieces)
        ]

        def is_valid_combination(combination: List[Tuple[int, int]]) -> bool:
            pos = list(positions_zero_based)
            n = len(pos)
            while True:
                if len(set(pos)) < n:
                    return False
                all_reached = True
                for i in range(n):
                    if pos[i] == combination[i]:
                        continue
                    all_reached = False
                    r, c = pos[i]
                    tr, tc = combination[i]
                    dr = 1 if tr > r else (-1 if tr < r else 0)
                    dc = 1 if tc > c else (-1 if tc < c else 0)
                    pos[i] = (r + dr, c + dc)
                if all_reached:
                    return True

        valid_count = 0
        for combination in product(*all_destinations):
            if is_valid_combination(combination):
                valid_count += 1

        return valid_count