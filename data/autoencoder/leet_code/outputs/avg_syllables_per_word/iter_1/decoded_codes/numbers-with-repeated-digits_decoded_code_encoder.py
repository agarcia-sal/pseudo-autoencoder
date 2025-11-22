def perm(m, n):
    if n == 0:
        return 1
    product = 1
    for i in range(n):
        product *= (m - i)
    return product

def count_unique_digits(x):
    s = str(x)
    L = len(s)
    count = 0
    for i in range(1, L):
        count += 9 * perm(9, i - 1)
    seen = set()
    for i, d in enumerate(s):
        start = 0 if i > 0 else 1
        for digit in range(start, int(d)):
            if digit not in seen:
                count += perm(9 - i, L - i - 1)
        if int(d) in seen:
            break
        seen.add(int(d))
    else:
        count += 1
    return count

def numDupDigitsAtMostN(n):
    return n - count_unique_digits(n)