def find_min_arrows(points):
    points.sort(key=lambda x: x[1])
    arrows = 0
    last_pos = float('-inf')
    for start, end in points:
        if start > last_pos:
            arrows += 1
            last_pos = end
    return arrows