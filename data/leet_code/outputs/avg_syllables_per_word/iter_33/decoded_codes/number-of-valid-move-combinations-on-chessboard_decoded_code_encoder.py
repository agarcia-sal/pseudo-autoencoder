from itertools import product
from copy import copy

class Solution:
    def countCombinations(self, pieces, positions):
        directions = {
            'rook': [(1, 0), (-1, 0), (0, 1), (0, -1)],
            'queen': [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (-1, 1), (1, -1), (-1, -1)],
            'bishop': [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        }

        # Adjust positions to zero-based indexing
        positions = [(r - 1, c - 1) for r, c in positions]

        def get_destinations(start, piece_type):
            row, col = start
            dests = [start]
            for dr, dc in directions[piece_type]:
                nr, nc = row + dr, col + dc
                while 0 <= nr < 8 and 0 <= nc < 8:
                    dests.append((nr, nc))
                    nr += dr
                    nc += dc
            return dests

        all_destinations = [get_destinations(pos, piece) for pos, piece in zip(positions, pieces)]

        def is_valid_combination(combination):
            current_positions = list(positions)
            n = len(current_positions)

            while True:
                if len(set(current_positions)) < n:
                    return False
                all_reached = True
                for i in range(n):
                    if current_positions[i] == combination[i]:
                        continue
                    all_reached = False
                    row, col = current_positions[i]
                    target_row, target_col = combination[i]

                    if target_row > row:
                        dr = 1
                    elif target_row < row:
                        dr = -1
                    else:
                        dr = 0

                    if target_col > col:
                        dc = 1
                    elif target_col < col:
                        dc = -1
                    else:
                        dc = 0

                    current_positions[i] = (row + dr, col + dc)
                if all_reached:
                    return True

        valid_count = 0
        for combination in product(*all_destinations):
            if is_valid_combination(combination):
                valid_count += 1

        return valid_count