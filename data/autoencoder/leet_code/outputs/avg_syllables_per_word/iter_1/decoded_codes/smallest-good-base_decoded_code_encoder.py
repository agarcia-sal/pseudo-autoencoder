import math

def find_k(n):
    n = int(n)
    max_len = int(math.log2(n)) + 1
    for m in range(max_len, 1, -1):
        k = int(n ** (1 / (m - 1)))
        if k < 2:
            continue
        if (k**m - 1) // (k - 1) == n:
            return str(k)
    return str(n - 1)