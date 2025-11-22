from itertools import product

class Solution:
    def countCombinations(self, pieces, positions):
        directions = {
            'rook': [(1, 0), (-1, 0), (0, 1), (0, -1)],
            'queen': [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)],
            'bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
        }

        adjusted_positions = [(r - 1, c - 1) for r, c in positions]

        def get_destinations(start, piece_type):
            r, c = start
            dests = [start]
            for dr, dc in directions[piece_type]:
                nr, nc = r + dr, c + dc
                while 0 <= nr < 8 and 0 <= nc < 8:
                    dests.append((nr, nc))
                    nr += dr
                    nc += dc
            return dests

        all_destinations = [get_destinations(pos, piece) for pos, piece in zip(adjusted_positions, pieces)]

        def is_valid_combination(combination):
            pos = adjusted_positions[:]
            n = len(pos)
            while True:
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
                    new_pos.append((r + dr, c + dc))
                pos = new_pos
                if all_reached:
                    return True

        valid_count = 0
        for combination in product(*all_destinations):
            if is_valid_combination(combination):
                valid_count += 1

        return valid_count