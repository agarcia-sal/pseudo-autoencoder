from typing import List, Tuple
from itertools import product

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[Tuple[int, int]]) -> int:
        # Directions for each piece type: each entry is a list of (dr, dc) moves
        directions = {
            "rook":    [(1, 0), (-1, 0), (0, 1), (0, -1)],
            "bishop":  [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            "queen":   [(1, 0), (-1, 0), (0, 1), (0, -1),
                        (1, 1), (1, -1), (-1, 1), (-1, -1)],
            "king":    [(1, 0), (-1, 0), (0, 1), (0, -1),
                        (1, 1), (1, -1), (-1, 1), (-1, -1)],
            "knight":  [(2, 1), (2, -1), (-2, 1), (-2, -1),
                        (1, 2), (1, -2), (-1, 2), (-1, -2)],
            "pawn":    [(1, 0)]  # Assuming pawn moves only one step forward (downwards)
        }

        # Normalize positions to zero-based indexing
        positions = [(pos[0] - 1, pos[1] - 1) for pos in positions]

        def get_destinations(start: Tuple[int, int], piece_type: str) -> List[Tuple[int, int]]:
            r, c = start
            dests = [start]
            for dr, dc in directions.get(piece_type, []):
                nr, nc = r + dr, c + dc
                # Pawn moves only one step, no continuous moves
                if piece_type == "pawn":
                    if 0 <= nr < 8 and 0 <= nc < 8:
                        dests.append((nr, nc))
                # King moves only one step in each direction
                elif piece_type == "king" or piece_type == "knight":
                    if 0 <= nr < 8 and 0 <= nc < 8:
                        dests.append((nr, nc))
                else:
                    # For rook, bishop, queen continuous moves
                    while 0 <= nr < 8 and 0 <= nc < 8:
                        dests.append((nr, nc))
                        nr += dr
                        nc += dc
            return dests

        all_destinations = [get_destinations(pos, piece) for pos, piece in zip(positions, pieces)]

        def is_valid_combination(combination: Tuple[Tuple[int, int], ...]) -> bool:
            pos = positions.copy()
            n = len(pos)
            while True:
                # Check if positions are unique
                if len(set(pos)) < n:
                    return False

                all_reached = True
                new_pos = []
                for i in range(n):
                    if pos[i] == combination[i]:
                        new_pos.append(pos[i])
                        continue
                    all_reached = False
                    r, c = pos[i]
                    tr, tc = combination[i]

                    dr = 1 if tr > r else (-1 if tr < r else 0)
                    dc = 1 if tc > c else (-1 if tc < c else 0)

                    nr, nc = r + dr, c + dc
                    new_pos.append((nr, nc))
                pos = new_pos
                if all_reached:
                    return True

        valid_count = 0
        for combination in product(*all_destinations):
            if is_valid_combination(combination):
                valid_count += 1

        return valid_count