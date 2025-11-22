def hIndex(citations):
    n = len(citations)
    l, r, h = 0, n - 1, 0
    while l <= r:
        m = l + (r - l) // 2
        if citations[m] >= n - m:
            h = n - m
            r = m - 1
        else:
            l = m + 1
    return h