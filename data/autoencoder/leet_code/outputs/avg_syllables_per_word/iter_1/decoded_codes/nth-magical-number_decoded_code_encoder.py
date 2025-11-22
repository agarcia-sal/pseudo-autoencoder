def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def find_nth_number(a, b, n):
    MOD = 10**9 + 7
    L = lcm(a, b)
    left, right = 1, n * min(a, b)

    while left < right:
        mid = (left + right) // 2
        count = mid // a + mid // b - mid // L
        if count < n:
            left = mid + 1
        else:
            right = mid

    return left % MOD