def myPow(x, n):
    def qpow(a, m):
        ans = 1
        while m > 0:
            if m & 1:
                ans *= a
            a *= a
            m >>= 1
        return ans
    return qpow(x, n) if n >= 0 else 1 / qpow(x, -n)