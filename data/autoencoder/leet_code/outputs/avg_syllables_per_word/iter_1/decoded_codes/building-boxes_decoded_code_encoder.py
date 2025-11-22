def triangular_pyramid(k):
    return k * (k + 1) * (k + 2) // 6

def bin_search(n):
    l, r = 0, n
    while l < r:
        m = (l + r + 1) // 2
        if triangular_pyramid(m) <= n:
            l = m
        else:
            r = m - 1
    return l

def minimumBoxes(n):
    k = bin_search(n)
    used = triangular_pyramid(k)
    rem = n - used
    floor = k * (k + 1) // 2
    add = 0
    while rem > 0:
        add += 1
        rem -= add
    return floor + add