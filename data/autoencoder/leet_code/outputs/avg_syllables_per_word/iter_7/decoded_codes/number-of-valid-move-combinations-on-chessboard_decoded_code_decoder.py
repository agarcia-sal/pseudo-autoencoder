from typing import List, Tuple, Dict
from itertools import product
import copy


class Solution:
    def countCombinations(self, pieces: List[str], positions: List[Tuple[int, int]]) -> int:
        directions: Dict[str, List[Tuple[int, int]]] = {
            "rook": [(1, 0), (-1, 0), (0, 1), (0, -1)],
            "bishop": [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            "queen": [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)],
        }

        positions = [(r - 1, c - 1) for r, c in positions]

        def get_destinations(start: Tuple[int, int], piece_type: str) -> List[Tuple[int, int]]:
            r, c = start
            dests = [start]
            for dr, dc in directions[piece_type]:
                nr, nc = r + dr, c + dc
                while 0 <= nr < 8 and 0 <= nc < 8:
                    dests.append((nr, nc))
                    nr += dr
                    nc += dc
            return dests

        all_destinations: List[List[Tuple[int, int]]] = [
            get_destinations(pos, piece) for pos, piece in zip(positions, pieces)
        ]

        def is_valid_combination(combination: Tuple[Tuple[int, int], ...]) -> bool:
            pos = positions.copy()
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
                    cr, cc = combination[i]

                    if cr > r:
                        dr = 1
                    elif cr < r:
                        dr = -1
                    else:
                        dr = 0

                    if cc > c:
                        dc = 1
                    elif cc < c:
                        dc = -1
                    else:
                        dc = 0

                    pos[i] = (r + dr, c + dc)
                if all_reached:
                    return True

        valid_count = 0
        for combination in product(*all_destinations):
            if is_valid_combination(combination):
                valid_count += 1

        return valid_count