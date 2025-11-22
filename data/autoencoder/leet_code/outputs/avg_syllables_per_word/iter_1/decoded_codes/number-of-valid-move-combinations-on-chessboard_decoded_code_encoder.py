from itertools import product

dirs = {
    "rook": [(1, 0), (-1, 0), (0, 1), (0, -1)],
    "queen": [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)],
    "bishop": [(1, 1), (-1, 1), (1, -1), (-1, -1)],
}

def get_dests(start, piece):
    r, c = start
    dests = [start]
    for dr, dc in dirs[piece]:
        nr, nc = r + dr, c + dc
        while 0 <= nr < 8 and 0 <= nc < 8:
            dests.append((nr, nc))
            nr, nc = nr + dr, nc + dc
    return dests

def is_valid(comb, pos):
    cur = pos[:]
    n = len(cur)
    while True:
        if len(set(cur)) < n:
            return False
        done = True
        for i in range(n):
            if cur[i] != comb[i]:
                done = False
                r, c = cur[i]
                tr, tc = comb[i]
                dr = 1 if tr > r else (-1 if tr < r else 0)
                dc = 1 if tc > c else (-1 if tc < c else 0)
                cur[i] = (r + dr, c + dc)
        if done:
            return True

def count_valid_combinations(positions, pieces):
    pos = [(r - 1, c - 1) for r, c in positions]
    all_dests = [get_dests(p, piece) for p, piece in zip(pos, pieces)]
    valid_comb_count = 0
    for comb in product(*all_dests):
        if is_valid(comb, pos):
            valid_comb_count += 1
    return valid_comb_count