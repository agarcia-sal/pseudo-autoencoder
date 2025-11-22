def numberOfBoomerangs(points):
    ans = 0
    for p1 in points:
        cnt = {}
        for p2 in points:
            d = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
            ans += cnt.get(d, 0)
            cnt[d] = cnt.get(d, 0) + 1
    return ans * 2