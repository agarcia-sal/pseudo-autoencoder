def minOneBitOps(n):
    if n == 0:
        return 0
    k = 0
    while (1 << (k + 1)) <= n:
        k += 1
    msb = 1 << k
    return (1 << (k + 1)) - 1 - minOneBitOps(n ^ msb)