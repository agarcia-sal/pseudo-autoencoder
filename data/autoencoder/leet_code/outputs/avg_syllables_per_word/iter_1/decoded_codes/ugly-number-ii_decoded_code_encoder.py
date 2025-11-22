def nth_ugly_number(n):
    ugly = [1]
    i2 = i3 = i5 = 0
    while len(ugly) < n:
        n2 = ugly[i2] * 2
        n3 = ugly[i3] * 3
        n5 = ugly[i5] * 5
        nxt = min(n2, n3, n5)
        ugly.append(nxt)
        if nxt == n2:
            i2 += 1
        if nxt == n3:
            i3 += 1
        if nxt == n5:
            i5 += 1
    return ugly[n-1]