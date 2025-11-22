def grayCode(n):
    if n == 0:
        return [0]
    prev = grayCode(n - 1)
    m = 1 << (n - 1)
    return prev + [m | x for x in reversed(prev)]