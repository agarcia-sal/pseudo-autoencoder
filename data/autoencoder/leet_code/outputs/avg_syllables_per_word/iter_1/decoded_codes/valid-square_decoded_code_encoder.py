def dist_squared(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def check_points(pts):
    dists = {dist_squared(pts[i], pts[j]) for i in range(len(pts)) for j in range(i + 1, len(pts))}
    if 0 in dists:
        return False
    return len(dists) == 2