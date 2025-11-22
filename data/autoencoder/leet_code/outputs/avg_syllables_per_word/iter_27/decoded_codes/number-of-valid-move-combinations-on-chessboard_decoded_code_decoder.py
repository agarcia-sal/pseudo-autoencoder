from itertools import product
from typing import List, Tuple, Dict, Sequence


class Solution:
    def countCombinations(self, pieces: List[str], positions: List[Tuple[int, int]]) -> int:
        directions: Dict[str, List[Tuple[int, int]]] = {
            "rook": [(1, 0), (-1, 0), (0, 1), (0, -1)],
            "bishop": [(1, 1), (1, -1), (-1, 1), (-1, -1)],
        }
        directions["queen"] = directions["rook"] + directions["bishop"]

        # Convert positions from 1-based to 0-based indexing
        zero_based_positions: List[Tuple[int, int]] = [
            (r - 1, c - 1) for r, c in positions
        ]

        def get_destinations(start: Tuple[int, int], piece_type: str) -> List[Tuple[int, int]]:
            r, c = start
            dests = [start]
            for dr, dc in directions.get(piece_type, []):
                nr, nc = r + dr, c + dc
                while 0 <= nr < 8 and 0 <= nc < 8:
                    dests.append((nr, nc))
                    nr += dr
                    nc += dc
            return dests

        all_destinations: List[List[Tuple[int, int]]] = [
            get_destinations(pos, piece) for pos, piece in zip(zero_based_positions, pieces)
        ]

        def is_valid_combination(combination: Sequence[Tuple[int, int]]) -> bool:
            pos = zero_based_positions.copy()
            n = len(pos)
            while True:
                if len(set(pos)) < n:
                    return False

                all_reached = True
                new_pos = pos.copy()

                for i in range(n):
                    if pos[i] == combination[i]:
                        continue
                    all_reached = False
                    r, c = pos[i]
                    tr, tc = combination[i]

                    dr = 1 if tr > r else (-1 if tr < r else 0)
                    dc = 1 if tc > c else (-1 if tc < c else 0)

                    nr, nc = r + dr, c + dc
                    # Defensive check: nr, nc should stay within bounds, but logic ensures it.
                    if not (0 <= nr < 8 and 0 <= nc < 8):
                        # Movement out of bounds - no valid path
                        return False
                    new_pos[i] = (nr, nc)

                pos = new_pos

                if all_reached:
                    return True

        valid_count = 0
        for combination in product(*all_destinations):
            if is_valid_combination(combination):
                valid_count += 1

        return valid_count