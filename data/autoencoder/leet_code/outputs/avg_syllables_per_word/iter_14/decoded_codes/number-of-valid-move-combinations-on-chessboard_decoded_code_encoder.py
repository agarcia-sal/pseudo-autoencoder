from itertools import product

class Solution:
    def countCombinations(self, pieces, positions):
        directions = {
            'rook': [(1, 0), (-1, 0), (0, 1), (0, -1)],
            'queen': [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)],
            'bishop': [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        }

        positions = [(r-1, c-1) for r, c in positions]

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

        all_destinations = [get_destinations(pos, piece) for pos, piece in zip(positions, pieces)]

        def is_valid_combination(combination):
            pos = list(positions)
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
                    target_r, target_c = combination[i]
                    if target_r > r:
                        dr = 1
                    elif target_r < r:
                        dr = -1
                    else:
                        dr = 0
                    if target_c > c:
                        dc = 1
                    elif target_c < c:
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