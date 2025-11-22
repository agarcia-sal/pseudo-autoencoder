def falling_squares(positions):
    intervals = []
    max_h = 0
    res = []

    for L, side in positions:
        R = L + side - 1
        h = side
        for l, r, H in intervals:
            if L <= r and R >= l:
                h = max(h, side + H)
        intervals.append((L, R, h))
        max_h = max(max_h, h)
        res.append(max_h)

    return res