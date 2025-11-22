MOD = 10**9 + 7

def rectangle_area(rectangles):
    y_coords = sorted({y for _, y1, _, y2 in rectangles for y in (y1, y2)})
    y_index = {y: i for i, y in enumerate(y_coords)}
    count = [0] * (len(y_coords))

    events = []
    for x1, y1, x2, y2 in rectangles:
        events.append((x1, 1, y1, y2))
        events.append((x2, -1, y1, y2))
    events.sort(key=lambda x: x[0])

    prev_x = 0
    area = 0
    for x, t, y1, y2 in events:
        length = 0
        for i in range(1, len(count)):
            if count[i-1] > 0:
                length += y_coords[i] - y_coords[i-1]
        area += length * (x - prev_x)
        area %= MOD
        for i in range(y_index[y1], y_index[y2]):
            count[i] += t
        prev_x = x
    return area % MOD