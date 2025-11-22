def max_points_on_line(points):
    if not points:
        return 0

    max_points = 0
    for i in range(len(points)):
        slopes = {}
        x_i, y_i = points[i]
        for j in range(len(points)):
            if i == j:
                continue
            x_j, y_j = points[j]
            if x_i == x_j:
                slope = float('inf')
            else:
                slope = (y_i - y_j) / (x_i - x_j)
            slopes[slope] = slopes.get(slope, 0) + 1
        max_points = max(max_points, max(slopes.values(), default=0))
    return max_points + 1