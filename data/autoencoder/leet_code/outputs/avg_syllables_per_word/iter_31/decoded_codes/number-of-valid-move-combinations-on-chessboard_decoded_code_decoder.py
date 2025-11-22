from typing import List, Tuple
from itertools import product

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        directions = {
            'rook': [(1, 0), (-1, 0), (0, 1), (0, -1)],
            'queen': [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)],
            'bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        }

        # Adjust positions from 1-based to 0-based indexing
        adjusted_positions: List[Tuple[int, int]] = [
            (row - 1, col - 1) for row, col in positions
        ]

        def get_destinations(start: Tuple[int, int], piece_type: str) -> List[Tuple[int, int]]:
            row, col = start
            result = [start]
            for delta_row, delta_col in directions[piece_type]:
                new_row, new_col = row + delta_row, col + delta_col
                while 0 <= new_row < 8 and 0 <= new_col < 8:
                    result.append((new_row, new_col))
                    new_row += delta_row
                    new_col += delta_col
            return result

        all_destinations: List[List[Tuple[int, int]]] = [
            get_destinations(pos, piece) for pos, piece in zip(adjusted_positions, pieces)
        ]

        def is_valid_combination(combination: Tuple[Tuple[int, int], ...]) -> bool:
            current_positions = adjusted_positions.copy()
            total_pieces = len(current_positions)

            while True:
                if len(set(current_positions)) < total_pieces:
                    return False

                all_reached = True
                updated_positions = []

                for idx in range(total_pieces):
                    current = current_positions[idx]
                    destination = combination[idx]

                    if current == destination:
                        updated_positions.append(current)
                        continue

                    all_reached = False

                    r_cur, c_cur = current
                    r_des, c_des = destination

                    delta_row = (r_des > r_cur) - (r_des < r_cur)
                    delta_col = (c_des > c_cur) - (c_des < c_cur)

                    updated_positions.append((r_cur + delta_row, c_cur + delta_col))

                current_positions = updated_positions
                if all_reached:
                    return True

        valid_count = 0
        for combination in product(*all_destinations):
            if is_valid_combination(combination):
                valid_count += 1

        return valid_count